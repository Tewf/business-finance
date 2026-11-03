"""Runway, break-even and the three states of a plan, from a model's numbers.

Reads a toml file (see three-states.toml) and prints:
  - runway: months of cash, with the event-driven model and with the spreadsheet rule (cash over gross burn);
  - break-even: the first month operating cash flow is not negative, and the units per month that cover costs;
  - the three states (before launch, at launch, at scale) and the event that moves each;
  - one line per scenario, each naming the one number it changes;
  - faults a program can find from the numbers alone;
  - every value not named in [measured] tagged PROVISIONAL.

Usage: python3 runway.py model.toml
"""
import math
import sys
import tomllib

STATES = ("registration", "launch", "scale")  # the event that opens each state; before launch = registration


def load(path):
    with open(path, "rb") as f:
        return tomllib.load(f)


def simulate(data, override=None):
    """Month by month. Returns (rows, events): rows of (month, state, units, cash_end, operating), events by name."""
    m = dict(data["model"])
    if override:
        m[override[0]] = override[1]
    cash = m["start_cash"]
    events = {"registration": 0}
    rows = []
    for t in range(m["horizon_months"]):
        units = 0
        if t >= m["launch_month"]:
            events.setdefault("launch", t)
            units = min(m["capacity"], m["units_at_launch"] * (1 + m["unit_growth"]) ** (t - m["launch_month"]))
        if "launch" in events and "scale" not in events and units >= m["scale_units"]:
            events["scale"] = t
        state = "scale" if "scale" in events else "launch" if "launch" in events else "registration"
        operating = units * (m["price"] - m["unit_cost"])
        for c in data.get("cost", []):
            opened = events.get(c["event"])
            if opened is None:
                continue
            if c["kind"] == "monthly" or (c["kind"] == "once" and opened == t):
                operating -= c["amount"]
        cash += operating
        rows.append((t, state, units, cash, operating))
    return rows, events


def runway(rows):
    """Months with cash not below zero before the first negative balance; None if cash holds through the horizon."""
    for t, _, _, cash, _ in rows:
        if cash < 0:
            return t
    return None


def break_even_month(rows, events):
    launch = events.get("launch")
    if launch is None:
        return None
    for t, _, _, _, operating in rows:
        if t >= launch and operating >= 0:
            return t
    return None


def monthly_costs(data, upto):
    """Monthly amount of every cost opened by the states up to and including `upto`."""
    order = STATES.index(upto)
    return sum(c["amount"] for c in data.get("cost", []) if c["kind"] == "monthly" and STATES.index(c["event"]) <= order)


def break_even_units(data, state):
    margin = data["model"]["price"] - data["model"]["unit_cost"]
    if margin <= 0:
        return None
    return math.ceil(monthly_costs(data, state) / margin)


def spreadsheet_runway(data):
    """The practice B1 compares with: cash over gross burn, the burn being every monthly cost at month 0 (Andreessen 2015)."""
    burn = monthly_costs(data, "registration")
    return None if burn == 0 else data["model"]["start_cash"] / burn


def faults(data, rows, events):
    out = []
    m = data["model"]
    for c in data.get("cost", []):
        if c.get("event") not in STATES:
            out.append(f"cost '{c.get('name')}' has no event in {STATES}: it would be paid before any event")
    first_negative = runway(rows)
    if first_negative is not None and first_negative < m["launch_month"]:
        out.append(f"cash ends in month {first_negative}, before the launch event in month {m['launch_month']}")
    scale_month = events.get("scale", math.inf)
    if first_negative is not None and first_negative < scale_month:
        out.append(f"cash ends in month {first_negative}, before the state at scale opens")
    if m["price"] <= m["unit_cost"]:
        out.append("unit cost is not below price: there is no break-even volume")
    elif "scale" not in events:
        out.append(f"scale is not reached within {m['horizon_months']} months: the third state never opens")
    if m["scale_units"] > m["capacity"]:
        out.append("scale threshold is above capacity: the third state cannot open")
    if m["launch_month"] >= m["horizon_months"]:
        out.append("launch is outside the horizon")
    return out


def provisional(data):
    measured = set(data.get("measured", {}))
    names = [f"model.{k}" for k in data["model"]] + [f"cost.{c['name']}" for c in data.get("cost", [])]
    return [n for n in names if n.split(".", 1)[1] not in measured]


def describe(data):
    rows, events = simulate(data)
    lines = []
    r = runway(rows)
    lines.append("RUNWAY")
    lines.append(f"  event-driven: {'holds through ' + str(len(rows)) + ' months' if r is None else str(r) + ' months'}")
    s = spreadsheet_runway(data)
    lines.append(f"  spreadsheet (cash / month-0 gross burn): {'no burn' if s is None else f'{s:.1f} months'}")
    be = break_even_month(rows, events)
    lines.append("BREAK-EVEN")
    lines.append(f"  first month operating cash flow >= 0: {'none in horizon' if be is None else be}")
    for state in STATES[1:]:
        u = break_even_units(data, state)
        lines.append(f"  units per month to cover costs open in state '{state}': {'none' if u is None else u}")
    lines.append("STATES")
    why = {"registration": "registration (month 0)", "launch": f"first sale, planned month {data['model']['launch_month']}",
           "scale": f"units per month reach {data['model']['scale_units']}"}
    names = {"registration": "before launch", "launch": "at launch", "scale": "at scale"}
    for st in STATES:
        month = events.get(st)
        lines.append(f"  {names[st]}: opens on event '{why[st]}', month {'never' if month is None else month}")
    lines.append("SCENARIOS")
    for sc in data.get("scenario", []):
        rr, ev = simulate(data, (sc["change"], sc["value"]))
        rw = runway(rr)
        lines.append(f"  {sc['name']} (changes {sc['change']} to {sc['value']}): runway "
                     f"{'holds' if rw is None else str(rw) + ' months'}, lowest cash {min(x[3] for x in rr):.0f}")
    lines.append("FAULTS")
    fs = faults(data, rows, events)
    lines.extend(f"  {f}" for f in fs) if fs else lines.append("  none found")
    lines.append("PROVISIONAL (not named in [measured])")
    lines.extend(f"  {n} PROVISIONAL" for n in provisional(data))
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    print(describe(load(sys.argv[1])))

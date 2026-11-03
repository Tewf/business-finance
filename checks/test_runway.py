import copy
import pathlib
import sys
import unittest

LOCAL = pathlib.Path(__file__).parent / "local"
sys.path.insert(0, str(LOCAL))
import runway  # noqa: E402

FIXTURE = LOCAL / "three-states.toml"


def base():
    return runway.load(FIXTURE)


class Runway(unittest.TestCase):
    def test_cash_ends_in_the_launch_month_when_tooling_is_paid_then(self):
        rows, _ = runway.simulate(base())
        self.assertEqual(runway.runway(rows), 12)

    def test_spreadsheet_rule_is_cash_over_month_zero_burn(self):
        self.assertAlmostEqual(runway.spreadsheet_runway(base()), 10000 / 150)

    def test_the_two_runways_disagree_on_the_fixture(self):
        d = base()
        rows, _ = runway.simulate(d)
        self.assertGreater(runway.spreadsheet_runway(d), runway.runway(rows))

    def test_a_cost_moved_to_its_event_extends_runway(self):
        d = base()
        d["cost"][1]["event"] = "scale"  # tooling paid at scale instead of launch
        rows, _ = runway.simulate(d)
        self.assertGreater(runway.runway(rows) or 10**6, 12)

    def test_events_open_states_in_order(self):
        _, ev = runway.simulate(base())
        self.assertEqual(ev["registration"], 0)
        self.assertEqual(ev["launch"], 12)
        self.assertGreater(ev["scale"], ev["launch"])

    def test_break_even_units(self):
        d = base()
        self.assertEqual(runway.break_even_units(d, "launch"), 20)    # (150+200)/18
        self.assertEqual(runway.break_even_units(d, "scale"), 159)    # (150+200+2500)/18 = 158.3, rounded up

    def test_no_break_even_when_cost_reaches_price(self):
        d = base()
        d["model"]["unit_cost"] = 40
        self.assertIsNone(runway.break_even_units(d, "scale"))
        rows, ev = runway.simulate(d)
        self.assertIn("no break-even", " ".join(runway.faults(d, rows, ev)))

    def test_fault_for_cost_without_event(self):
        d = base()
        d["cost"][0]["event"] = ""
        rows, ev = runway.simulate(d)
        self.assertTrue(any("no event" in f for f in runway.faults(d, rows, ev)))

    def test_fault_cash_ends_before_scale(self):
        d = base()
        rows, ev = runway.simulate(d)
        self.assertTrue(any("before the state at scale" in f for f in runway.faults(d, rows, ev)))

    def test_fault_scale_above_capacity(self):
        d = base()
        d["model"]["scale_units"] = 99999
        rows, ev = runway.simulate(d)
        self.assertTrue(any("above capacity" in f for f in runway.faults(d, rows, ev)))

    def test_every_value_is_provisional_until_measured(self):
        d = base()
        self.assertIn("model.price", runway.provisional(d))
        d["measured"] = {"price": "a source"}
        self.assertNotIn("model.price", runway.provisional(d))

    def test_output_has_every_section_and_does_not_mutate_input(self):
        d = base()
        before = copy.deepcopy(d)
        text = runway.describe(d)
        for head in ("RUNWAY", "BREAK-EVEN", "STATES", "SCENARIOS", "FAULTS", "PROVISIONAL"):
            self.assertIn(head, text)
        self.assertEqual(d, before)


if __name__ == "__main__":
    unittest.main()

# Baseline

Step 5 of the review: the baseline the program is compared against. It is the practice of the spreadsheet forecast, written down for this review. It names no tool and no company. Evidence is in [review](review.md).

**Shape:** [baseline](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/baseline.md)

## B1: the spreadsheet runway

1. **Cash over burn.** Runway is the cash balance divided by the monthly gross burn at month 0 (Andreessen 2015 for burn).
2. **One burn.** Every cost is a monthly line that runs from the start; no cost waits for an event.
3. **Default alive.** The founder asks whether, with expenses as they are and growth as it has been, the cash lasts until profit (Graham 2015).
4. **One scenario.** One column of numbers, edited by hand when the plan changes.
5. **Break-even by hand.** Break-even units are fixed costs over contribution margin per unit (OpenStax 2026).

## Compared with what the review found

| Item | In B1 | Fit |
|---|---|---|
| Costs that start at an event | not modelled: all costs run from month 0 | lacks |
| Three states with their events | not modelled | lacks |
| Break-even volume | one formula | matches |
| A range, not an average | one scenario (Savage 2002) | lacks |
| Optimism corrected by past cases (Buehler 1994) | none | lacks |
| Unmeasured values marked | none | lacks |

## What B1 lacks

- It cannot see a cost that opens at launch: the fixture in the program shows 66.7 months by B1 and 12 months by the event-driven model (checks/local/runway.py).
- It cannot say that cash ends before an event; the program reports it as a fault.
- It marks no value as unmeasured; the program tags each PROVISIONAL.

## How it is measured

- Run `python3 checks/local/runway.py checks/local/three-states.toml` and compare the two runway lines.
- The difference in months between B1 and the event-driven runway, on plans with a known answer.
- The number of faults found on the plan.
- The reference model is the program's month-by-month balance, not the world; a test against real outcomes is not run here.

## The review is finished

The baseline is named: B1. The next job is a design document for the program, and a test of B1 against the program on plans with known outcomes.

# 0002: The baseline is the spreadsheet runway

**Decision:** The baseline for a runway and break-even model is the spreadsheet rule of practice, and the program in `checks/local/runway.py` is compared with it on a plan in three states.

**Status:** accepted, 2026-11-04. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/65e42472e2d4cbfd994c2a86e95a47e5dc7301ca/shapes/decision-record.md).

## Context

- The first review ([evidence/finance-runway](../evidence/finance-runway/)) found no formal definition of runway and no open program for a runway driven by events.
- Practice defines gross burn (terms in the [frame](../evidence/finance-runway/frame.md)) (Andreessen 2015) and asks whether cash lasts to profit (Graham 2015). The usual tool is a spreadsheet.
- The front page asks for a program compared with a spreadsheet forecast as the practice.

## Decision

- B1 is the spreadsheet runway: cash over the gross burn of month 0, every cost running from the start, one scenario.
- The program takes its numbers from a toml file. It reads three states, each opened by an event, and tags every value PROVISIONAL until the file names the source that measured it.
- The program's own month-by-month balance is the reference model. It is not tested against real outcomes yet.
- The repository keeps its name. The frame notes that the field says entrepreneurial finance; the maintainer decides a rename.

## Consequences

- The comparison is repeatable on a fixture of invented values: the two runways differ by 54.7 months there.
- **Bad:** the reference is a model, so a gap between B1 and the program shows a difference of method, not of accuracy. A test against plans with known outcomes is the next job.
- **Bad:** break-even units count monthly costs only; one-off costs enter the runway but not the volume.

## See also

[Decisions](README.md); [the review's baseline](../evidence/finance-runway/baseline.md); [the program](../checks/local/runway.py).

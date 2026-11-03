# Protocol: how the pool was built

A first pass of a multivocal literature review to Garousi 2019, run on 2026-11-04 by one reviewer. Terms are in [frame](frame.md).

**Shape:** [protocol](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/protocol.md)

## 1. Why grey literature

Garousi's seven questions, answered for this topic.

| Question | Answer |
|---|---|
| Is the context broader than academic? | yes: runway is used by founders, investors and accelerators |
| Is the practice ahead of the research? | yes: the word runway has no formal definition in these searches |
| Do practitioners hold the data? | yes: post-mortem counts and investor metrics |
| Are the formal sources thin? | yes: no formal study of runway was found (F1) |
| Is the topic contested? | yes: grants and accelerators have mixed results |
| Does practice need a baseline? | yes: this review ends on one |
| Do formal sources miss the form? | yes: the cash forecast is a spreadsheet, not a paper |

## 2. Questions

- Q1 runway: how is it defined, and how long does cash last when revenue comes late?
- Q2 funding: what does each source cost a small venture?
- Q3 returns: what do measured effects of grants and accelerators say?
- Q4 scenarios and the program: how do forecasts fail, and which faults can a program find?

## 3. Existing reviews

- Found: a survey of public R&D subsidies (Zuniga-Vicente 2012) and a meta-regression of 52 evaluations (Dimos 2016).
- Also found: a systematic review of accelerators (Crisan 2019, located only), a review of small business finance (Berger 1998) and a review of venture capital (Gompers 2001).
- Not found: a review of runway, of cash forecasts for small ventures, or of event-driven cost discipline.

## 4. Formal search

Database: OpenAlex, field title and abstract, sorted by citations, top 6 screened, no key and no identity sent. Counts are of 2026-11-04.

| Id | String as run | Count | New concept |
|---|---|---|---|
| F1 | startup runway burn rate | 11 | ynynnn |
| F2 | financial bootstrapping new ventures | 62 | ynyynn |
| F3 | accelerator venture performance causal | 14 | ynnnnn |
| F4 | R&D grants small firms causal effect survey | 3 | nnn |
| F5 | cash flow forecasting small firms uncertainty | 31 | nnnynn |
| F6 | break-even analysis small business | 916 | nnnnnn |
| F7 | venture financing staged real options entrepreneurial | 31 | ynnnnn |

- Known-item lookups: about 20 works were located by title in Crossref and their abstracts read in OpenAlex.
- A title that returned no abstract is marked located only. Four abstracts were read through web searches for the title.
- Wrong first guesses were corrected by title: a guessed identifier for seven works resolved to unrelated papers and was discarded.
- Backward snowball: the bibliography of Berger 1998 and Howell 2017 was not read; works were added by name from the strands of the questions. Forward snowball: not run, for the first pass.

## 5. Grey search

| Id | Producer or engine | String or what was read | Result | New concept |
|---|---|---|---|---|
| G1 | GitHub repository search, unauthenticated | runway calculator | 5 screened, 0 included | nnnnn |
| G2 | GitHub repository search, unauthenticated | startup financial model python | 5 screened, 0 included | nnnnn |
| G3 | GitHub repository search, unauthenticated | cash flow forecast monte carlo | 5 screened, 0 included | nnnnn |
| G4 | web search | runway definition in the formal literature | 1 written answer, 0 included | not recorded |

- Seven pages were read by name, not by a search string. Each was read in part through a text extract and is counted in [sources](sources.md).
  - an essay by an accelerator founder (read in full), and an investor's metrics guide;
  - an analysis of failed companies, and a venture investor's essay on recovering acquisition cost;
  - an open forecasting textbook, a management magazine article and an open managerial accounting textbook.
- Not searched: forums, Q/A sites, talks, videos, patents, social media, regulators' guides, tax rules by country.

## 6. Stopping rule

- Effort bounded: top 6 results per formal string and top 5 per repository search.
- Saturation: a string stops after 5 consecutive results that add no concept. F6 and G1 to G3 stopped by it.

## 7. Selection

- Include: a study or document that defines runway, burn or break-even, measures the effect of a funding source on a small or young firm, or tests a forecast.
- Exclude: macro studies of financial development, valuation of large firms, personal finance, tutorials without data.
- Quality: formal sources carry an evidence grade; grey sources are scored in section 8.

## 8. Quality of grey sources

Garousi's 20 criteria, scored 1, 0.5 or 0 and summed in eight groups: authority 4, methodology 6, objectivity 4, date 1, position 1, novelty 2, impact 1, outlet 1. The threshold is 10 of 20. Scores are in [sources](sources.md).

## 9. Extraction and synthesis

- Formal works: the abstract was read; a figure is marked (secondary). Four abstracts were read through a search summary and are marked secondary.
- Grey pages were read through a text extract; figures from them are marked (secondary). One essay was read in full as plain text.
- Synthesis is narrative by question.

## 10. Not searched, and limits

- Not searched: corporate finance texts beyond one located title, regulators' and tax guides, equity crowdfunding, debt contracts, grant schemes by country.
- Limits: one reviewer, no second rater; OpenAlex shares a daily budget and its counts change; most formal figures come from abstracts.
- Not recorded: G4 is a web search that returns a written answer and not a list of results, so there is no list to letter.

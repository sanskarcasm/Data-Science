# Airport Catering Performance Analysis

An interactive Excel dashboard and written analysis built from 18 months of catering sales and passenger data for a UK airport. The company name is withheld and the dataset is anonymised.

**Tools:** Excel (SUMIFS, INDEX/MATCH, MAXIFS, data validation, charts)

---

## Overview

I was given monthly sales and transaction data for five catering outlets at a UK airport, together with monthly passenger numbers, and asked to turn it into something a commercial team could use day to day. The goal was to track how each outlet trades, compare performance over time, and make the numbers easy to read at a glance.

## The data

The dataset ran from January 2024 to June 2026. It covered five outlets: two coffee bars and three restaurants, in different parts of the terminal. Each row held the number of transactions, total sales, the unit size in square metres, and the outlet's location. Passenger counts came as a separate monthly table.

Two things needed fixing before any analysis:

- Outlet names and years were stored in merged cells, so most rows were blank and no formula could read them. I flattened this into a clean table with a value on every row.
- 2026 only ran to June, so comparing full years would make the current year look like a collapse when the data simply stops halfway through.

## Approach

The workbook runs on live formulas rather than values pasted out of a pivot, so every figure traces back to the source and the whole model updates if the data changes.

- Totals use `SUMIFS` against the cleaned table.
- The per-outlet view uses `INDEX` and `MATCH` to pull each outlet's type and location, and `MAXIFS` for its current size, since two units were expanded partway through the period.
- The dashboard links to a single calculation tab, so nothing is typed in by hand.
- An outlet dropdown (data validation) drives one of the charts, giving interactivity without a pivot table.

The main judgement call was comparing the same six months, January to June, across all three years. That is the only fair read given the partial 2026, and it also sidesteps a data problem found in August 2024.

## Key findings

- **Growth is real but slowing.** Like-for-like first-half sales rose from £10.0m (2024) to £13.3m (2025) to £14.4m (2026). The rate dropped from about 32% to about 9%.
- **One outlet carries the estate.** North Kitchen brings in roughly £8.2m of the £14.4m, more than half of all catering revenue, and is the largest unit by floor space.
- **One outlet is shrinking.** Terminal Kitchen fell from £2.4m to £2.2m to £1.9m across the three half-years, and its transactions dropped sharply in early 2026. That pattern usually points to a closure or a refit.
- **New outlets explain much of the growth.** Gate Bistro opened in late 2024 and Sky Deli in mid 2025, so a good part of the headline rise is new units rather than existing outlets selling more.
- **A likely data error.** August 2024 for Terminal Kitchen reads £5.16m at an average spend near £134 per transaction, against a normal figure around £13. That is roughly 10x too high and looks like a typo. I flagged it rather than deleting it, and the January to June comparison does not depend on it.
- **Spend per passenger.** Catering spend per passenger rose from £1.38 to £1.71 to £1.76 across the three half-years.

## Dashboard

The dashboard shows the headline year-to-date numbers, a monthly sales trend with a separate line per year, and a per-outlet view controlled by a dropdown. The 2026 line stops at June on purpose, so empty future months are not read as zero sales.

## Files

- `Commercial_Analyst_Task_COMPLETED.xlsx` : the workbook, with a cleaned Data tab, a formula-driven Output tab, the Dashboard, and a Summary.
- `Airport_Catering_Analysis.pdf` : a written report covering methods, findings, and screenshots.

## Limitations and next steps

With only 18 months of data I can see one year-on-year step, not a trend worth staking much on. The August 2024 figure needs confirming with whoever owns the data, and I would want to know what happened at Terminal Kitchen in early 2026 before reading too much into its decline. Given longer history I would look at seasonality properly and at how each outlet's sales move with passenger numbers month to month.

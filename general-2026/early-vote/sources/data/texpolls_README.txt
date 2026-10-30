Texas 2026 General Election: County Early Voting

texpolls-texas-2026-general-early-voting-by-county.csv lists cumulative early-voting totals by Texas county and reporting date. Each row is a running total through report_date, not the number who voted that day. Do not sum counts across dates.

How to Credit
Source: TexPolls (texpolls.com), using Texas Secretary of State and county election office reports.
Link to the dataset: https://texpolls.com/turnout#download-data
Each CSV ends with publisher, dataset_url, and attribution columns so credit stays with imported or shared rows. These fields describe the dataset publisher; existing source columns identify the underlying government reports.

TexPolls publishes the Texas Secretary of State's figures alongside county election offices' own reports. The Secretary of State's in_person figure can lag county reports. Check county_office_in_person for the county office's cumulative count through the same date, with report links in county_office_source. Blank county columns mean no validated same-date county report is available.

Dallas rows marked roster_corrected use the Secretary of State's own early-voter roster count instead of its higher summary figure. sos_in_person keeps the original summary count, and note explains the correction.

Texas Secretary of State Source: the Texas Secretary of State's early-voting turnout report
https://goelect.txelections.civixapps.com/ivis-evr-ui/evr
County-Office Sources: the report links in county_office_source. Multiple links separated by | identify all reports supporting a cumulative count.

These reports are unofficial and provisional, not final election results. Mail means ballots received, not a final count of valid ballots. FIPS is a five-character county identifier; import it as text.

Secretary of State reports in this file run through October 26, 2026. Some county figures can still describe an earlier point in time.
No interior reporting dates are missing. We include a statewide report date only after completeness and consistency checks pass.
The original Secretary of State columns stay unchanged. TexPolls-selected counts appear in separate columns. Counts for earlier dates can decrease when source reports are revised. Only aggregate counts are published.

Roster Corrections:
October 23, 2026, Travis: Texas Secretary of State roster 198,923; original Secretary of State summary 208,711. The CSV note gives the county-office comparison.
October 24, 2026, Travis: Texas Secretary of State roster 223,528; original Secretary of State summary 233,316. The CSV note gives the county-office comparison.
October 25, 2026, Travis: Texas Secretary of State roster 242,161; original Secretary of State summary 251,949. The CSV note gives the county-office comparison.
October 26, 2026, Travis: Texas Secretary of State roster 275,453; original Secretary of State summary 285,241. The CSV note gives the county-office comparison.

County reports show 42,426 more in-person votes than the Secretary of State report through October 26, 2026. Adding those differences to the 5,079,994 ballots in the Secretary of State report gives 5,122,420 early ballots reported. This combines the available Secretary of State and county reports and may change. Secretary of State CSV columns keep the figures from the Secretary of State report; each affected row's note includes the county count and every supporting source. County-office columns separately show validated county observations.

Secretary of State Columns
report_date: ISO date through which counts accumulate.
ev_day: calendar position from October 19, 2026 (day 1); missing reports do not renumber later days.
fips: five-character Texas county FIPS code.
county: county name.
in_person: cumulative in-person count from the Secretary of State, including roster corrections described in note.
mail: cumulative mail ballots received, including receipts before early voting opened.
total: in_person plus mail.
registered: registered voters in the Secretary of State's report.
turnout_pct: total divided by registered, as a percentage rounded to one decimal place.
sos_in_person: original in-person figure in the Secretary of State's summary.
value_source: sos for Texas Secretary of State summary figures, or roster_corrected when the Secretary of State's voter roster supplies in_person.
note: correction counts, reporting caveats, or an earlier snapshot's status.

County-Office Columns
The separate county-office columns do not change the Secretary of State figures.
county_office_in_person: cumulative in-person count from a validated county-office report for report_date; blank without one.
county_office_source: county report URL, or all supporting URLs separated by | for all reports used to calculate the cumulative count; blank without one.

TexPolls and Comparison Columns
texpolls_in_person: selected in-person count using the same dated publication metadata as the site; otherwise the published Secretary of State count.
texpolls_source: secretary_of_state, roster_corrected, or county_office; county selections cite their supporting report URLs in note, including an earlier validated version when applicable.
gap_vs_secretary_of_state: county_office_in_person minus in_person, including any roster correction; blank without a same-date county report. sos_in_person separately preserves the original summary.
turnout_pct_2022_same_day: the 2022 county total divided by its own registered voters, matched by calendar day position, rounded to one decimal; blank without a matched baseline.
change_pts_vs_2022: (texpolls_in_person plus Secretary of State mail) divided by this row's 2026 registered voters, minus the 2022 rate, in percentage points; calculated before rounding to one decimal. Existing turnout_pct remains the Secretary of State rate.

County Reference
texpolls-texas-2026-county-reference.csv has one row per county. registered, registered_through_date, and registered_source identify the latest published registration count and source. pres2024_rep, pres2024_dem, pres2024_other, and pres2024_total are official 2024 presidential results. pres2024_r_minus_d_margin_pts is 100 times (Republican votes minus Democratic votes) divided by total votes, rounded to one decimal; pres2024_source links the official source. These results are historical context, not a forecast.

Revisions
texpolls-texas-2026-general-early-voting-revisions.csv records changes we observed to Secretary of State figures and value_source. Tracking starts with the first saved Secretary of State snapshot on 2026-10-22T20:17:25.147Z. Earlier changes are not reconstructed.

Each row records report_date, fips, county, field, old, new, and seen_at (UTC). The explanation column adds context for specific revisions; other rows leave it blank. Repeated unchanged runs add nothing.

Source Revisions Through October 19, 2026
The Texas Secretary of State revised Callahan's October 19, 2026 in-person count from 934 to 467. The cause hasn't been confirmed.
The Texas Secretary of State revised Hardin's October 19, 2026 in-person count from 2,152 to 1,902. The cause hasn't been confirmed; our October 22 review found no county count to compare.
The Texas Secretary of State revised Hidalgo's October 19, 2026 in-person count from 17,831 to 17,319, closer to the county office's 17,400. The revised figure is still 81 lower.

October 21, 2026 Source Comparison
The first figure in each pair is from the saved publication at commit b999bd5c2426a1a80ee57335c5ef975558f8447f. The second is from the revised Secretary of State report observed on October 22, 2026 (Central).
Callahan: in person and total 2,297 to 1,149; mail stayed at 0.
Hardin: in person 5,683 to 5,099; mail stayed at 1 (total 5,684 to 5,100).
Hidalgo: in person 51,943 to 50,474; mail stayed at 3,137 (total 55,080 to 53,611). The revised in-person figure is closer to the county office's 50,739: 265 below, compared with 1,204 above before.

Saved Source Copies (Live Links Can Change)
October 19, 2026 original Secretary of State aggregate SHA-256: 6dda642720c9c6bf5392a5f0cf7dfd10d9e8084f80ed83e6ecfe0116d58eb564
October 19, 2026 revised Secretary of State aggregate SHA-256: b948ed0444a90fa08e92c22b0523ad5cff709bd60f6f09ed6a0369bc10f584df
https://goelect.txelections.civixapps.com/api-ivis-system/api/v1/getFile?type=EVR_EARLYVOTING&electionId=53815&electionDate=10%2F19%2F2026
Saved b999 publication SHA-256: 422b2feba20764cebca8530a57e79d78f0f9f7593b32ffc3b91b8311699c82c6
https://github.com/texastentialism/texas-elections/blob/b999bd5c2426a1a80ee57335c5ef975558f8447f/data/2026/general/early-voting.json
October 21, 2026 revised Secretary of State aggregate SHA-256: 565ade84205bb59fb5d0d6f61488d10c5fdf7f6e66c7e99e86387240c89756e0
https://goelect.txelections.civixapps.com/api-ivis-system/api/v1/getFile?type=EVR_EARLYVOTING&electionId=53815&electionDate=10%2F21%2F2026
Hidalgo County unofficial aggregate, October 19-21, 2026 columns only, PDF SHA-256: 3c7eb78db1012e5c8edaba60fbb5e2d9e0aa3c18652502d0fc469481910eb89a
https://www.hidalgocounty.us/DocumentCenter/View/73361/EV-SUBS

County-office columns, county spelling, and editorial note changes are excluded. This log records our observations, not every change the Secretary of State may have made. Earlier reporting dates kept for reference use their last saved Secretary of State values and are identified in note.

License: Creative Commons Attribution 4.0 International (CC BY 4.0)
https://creativecommons.org/licenses/by/4.0/
Data are provided as is, without warranty.

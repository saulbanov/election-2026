# RAW BUCKET — faithful pulls only

Texas 2026 general-election public polls, released or fielded Oct. 15, 2026 onward. Collected Nov. 2, 2026 by a collector agent. No ranking, averaging, or judgment. Over-inclusive: borderline-window polls are listed at the end and flagged.

**Source tiers used below**
- **PRIMARY**: pollster's own release, PDF topline, or sponsor document, fetched. Quotes are verbatim.
- **SECONDHAND**: news report or aggregator, fetched. Quotes are verbatim from that report.
- **WIKIPEDIA-ONLY**: row from a Wikipedia poll table (raw wikitext fetched via `action=raw`, Nov. 2). The pollster's own page was not fetched or was blocked. The row is reproduced as the table gives it.
- **SNIPPET ONLY**: from a WebSearch summary; not fetched.

Local captures (HTML, PDFs, extracted text) for every fetch: `/private/tmp/claude-501/-Users-saulelbein-Documents-Claude-Code/7485ee41-940e-4ab8-b4a7-d26a34a4b7f1/scratchpad/polls_cap/`

Wikipedia index pages used (raw wikitext): `2026_United_States_Senate_election_in_Texas`, `2026_Texas_gubernatorial_election`, `2026_Texas_lieutenant_gubernatorial_election`, `2026_Texas_Attorney_General_election`, `2026_Texas_Commissioner_of_Agriculture_election`, `2026_Texas_Railroad_Commissioner_election`.

Race key: SEN = U.S. Senate (Talarico D / Paxton R / Brown L). GOV = Governor (Hinojosa D / Abbott R / Dixon L). LTG = Lt. Governor (Goodwin D / Patrick R / Cristo L / McCormick G). AG = Attorney General (Nathan Johnson D / Middleton R / Oxford L). AGC = Agriculture Commissioner (Tucker D / Sheets R / Kelly L). RRC = Railroad Commissioner (Rosenthal D / French R / DiBianca L).

---

## 1. Trafalgar Group (R) — Oct. 31–Nov. 1

- Tier: PRIMARY (PDF). URL: https://www.thetrafalgargroup.org/wp-content/uploads/2026/11/TX-Midterms-Report-1101.pdf
- Released: Nov. 1, 2026 (per Wikipedia citation date; PDF header says "November 2026"). Sponsor: none stated.
- Verbatim methodology: "Conducted 10/31/26 - 11/01/26 • 1089 Respondents • Likely General Election Voters • Response Rate: 4.5% • Margin of Error: 2.9% • Confidence: 95%". Mode: not stated in PDF text; points to "TheTrafalgarGroup.org/Polling-Methodology".
- SEN, verbatim (Total column): "Ken Paxton Column % 48.1%", "James Talarico Column % 47.5%", "Ted Brown Column % 2.4%", "Undecided Column % 2.0%".
- GOV, LTG, AG, AGC, RRC: not in PDF text (PDF covers U.S. Senate ballot only).
- Secondhand: Newsweek: "A Trafalgar Group survey conducted October 31 to November 1 found the candidates tied at 48 percent." 270toWin lists "Trafalgar Group 11/01/2026 1,089 LV · Margin of error ±2.9% 48% 48% 4%".

## 2. AtlasIntel — Oct. 28–Nov. 1

- Tier: PRIMARY PDF fetched for methodology; **vote-intention figures are chart images, not extractable text**, so the numbers below are SECONDHAND.
- PDF: https://cdn1.atlasintel.org/2026_midterms__texas_110126_73e0a3a507f76a2e.pdf
- PDF verbatim: "TARGET POPULATION Texas adult population", "SAMPLE SIZE 1,678 respondents", "METHODOLOGY Random Digital Recruitment (Atlas RDR)", "MARGIN OF ERROR ±2 p.p.", "POLLING PERIOD 10/28/2026 - 11/01/2026". Sponsor: none stated.
- Newsweek (https://www.newsweek.com/james-talaricos-chances-beating-ken-paxton-final-texas-polls-show-12648344), verbatim: "Talarico received 51.3 percent compared with 45.4 percent for Paxton in an AtlasIntel poll, giving Talarico a 5.9-point lead ahead of voting this week." and "The poll surveyed 1,678 respondents from October 28 to November 1 using AtlasIntel's online Random Digital Recruitment method. It reported a margin of error of plus or minus 2 percentage points at a 95 percent confidence level."
- WIKIPEDIA-ONLY rows: SEN "1,678 (A) | ±2.0% | Paxton 45% | Talarico 51% | Other 3% ("Other" with 2%; "Would not vote" with 1%) | Undecided 1%". GOV "1,678 (A) | ±2.2% | Abbott 48% | Hinojosa 49% | Other 2% ("Other" with 1%; "Would not vote" with 1%) | Undecided 1%". (Wikipedia gives two different MOEs for the same poll.)
- Note: population is all adults per PDF ("Texas adult population"). Down-ballot: not reported anywhere fetched.

## 3. New York Times / Siena (SRI / ReconMR) — fielded late Oct.–Nov. 1

- Tier: PRIMARY (Siena release page). NYT toplines page returned HTTP 403.
- URL: https://sri.siena.edu/2026/11/01/nytimes-siena-poll-of-likely-voters-alaska-iowa-kansas-maine-michigan-ohio-and-texas/ (posted November 1, 2026). Sponsor: The New York Times.
- Verbatim: "Texas: U.S. Senate: James Talarico (D) 50% – Ken Paxton (R) 43%" / "Governor: Gina Hinojosa (D) 48% – Greg Abbott (R) 47%"
- Verbatim MOE: "3.4 points in Texas, including a design effect of 1.29;"
- Verbatim quote: "Our final U.S. Senate polls show Democrats with leads of 5 to 11 points in Kansas (5), Ohio (5), Maine (6), Texas (7), and Michigan (11)" (Don Levy). "both Kansas and Texas are too close to call" (governor).
- Field dates and n: not in the fetched Siena text. **Conflict:** WIKIPEDIA-ONLY row says "October 27 – November 1, 2026 | 1,215 (LV) | ±3.4% | Paxton 43% | Talarico 50% | Other 0% ("Another candidate" with 0%) | Undecided 6%" and GOV "Abbott 47% | Hinojosa 48% | Other 0% | Undecided 6%". 270toWin: "Siena College 11/01/2026 1,215 LV · Margin of error ±3.3% 50% 43% 7%". Newsweek instead says: "The Texas portion surveyed 5,708 likely voters from October 23 to November 1." (5,708 may be the seven-state total; not verified.)
- Mode: not stated in fetched text.
- Down-ballot: not in fetched text; NYT toplines (blocked) not checked. Toplines URL: https://www.nytimes.com/interactive/2026/11/01/polls/times-siena-tx-poll-toplines.html
- Related, NOT a poll: Siena/ReconMR "ReconMR Texas Poll: Recontacting Voters" (posted Nov. 1; https://sri.siena.edu/2026/11/01/reconmr-texas-poll-recontacting-voters/), verbatim: "This is not a poll but rather a series of interviews ... drawn from the 729 respondents who chose to respond to a recontact survey". Its PDF says previous ReconMR polls had "Talarico ... led by nearly 5 points on average since then, while Abbott has held a lead of about a point across the four surveys."

## 4. On Point Polling — Nov. 1 (final)

- Tier: PRIMARY. URL: https://onpointpolitics.substack.com/p/final-texas-poll-talarico-leads-paxton (post dated Nov 02, 2026; byline "On Point Polling · November 1, 2026")
- Verbatim methodology: "On Point Polling interviewed 847 Texas registered voters online through the Cint Exchange on November 1, 2026, with quotas on party, age, gender, race, education and region." Header: "847 Texas registered voters · margin of error ±3.4 · all ballot results have undecided voters leaned". WebFetch read of same page: "The margin of error is ±4.2 points for likely voters and ±3.4 for registered voters." Likely-voter n: not stated. Sponsor: earlier On Point post says "On Point Polling is not paid for by any candidate or c[...]" (truncated in capture).
- Results (likely voters, leaned), verbatim:
  - SEN: "James Talarico: 51.6%", "Ken Paxton: 46.1%", "Ted Brown: 2.2%", "Still undecided: 0.1%"
  - GOV: "Greg Abbott: 51.6%", "Gina Hinojosa: 47.0%", "Pat Dixon: 1.4%", "Still undecided: 0.1%"
  - LTG: "Dan Patrick: 52.5%", "Vikki Goodwin: 44.4%", "Anthony Cristo: 1.7%", "Kevin McCormick: 1.1%"
  - AG, AGC, RRC, generic: not included.
- Crosstabs (Google Sheet): https://docs.google.com/spreadsheets/d/1AOPVvI4VL4gH_30WjHfaBLrKPAalByhNozW9-vybnyc/edit?usp=sharing (not fetched)

## 5. On Point Polling — Oct. 27

- Tier: PRIMARY. URL: https://onpointpolitics.substack.com/p/texas-poll-talarico-leads-paxton-bf8 (post dated Oct 30, 2026)
- Verbatim: "On Point Polling interviewed 1,184 Texas registered voters online on October 27, 2026, with quotas on age, gender and where respondents live." "The margin of error is ±2.9 points for likely and registered voters." Header: "On Point Polling · October 27, 2026 · 1,184 Texas registered voters · likely voters ±2.9".
- SEN verbatim: "Talarico leads Paxton 50.6% to 44.1% as asked. The few undecided voters lean toward Paxton, 62 to 38, so the lead narrows slightly to 51.7% to 45.8% with leaners." Listed: as asked "James Talarico: 50.6%", "Ken Paxton: 44.1%", "Ted Brown: 2.2%", "Undecided: 3.2%"; with leaners "James Talarico: 51.7%", "Ken Paxton: 45.8%", "Ted Brown: 2.3%", "Still undecided: 0.2%".
- GOV verbatim: as asked "Greg Abbott: 49.3%", "Gina Hinojosa: 47.2%", "Pat Dixon: 1.5%", "Undecided: 2.1%"; with leaners "Greg Abbott: 50.1%", "Gina Hinojosa: 48.3%", "Pat Dixon: 1.5%", "Still undecided: 0.1%".
- Down-ballot: none found in capture.

## 6. Kreate Strategies (KStrat) — Oct. 27–30

- Tier: WIKIPEDIA-ONLY. Release page https://kstrat.net/press/texas-2026-senate-governor-talarico-leads-paxton-october is a JavaScript app; curl and WebFetch returned only the site shell. Not fetched.
- Wikipedia citation title: "KStrat Poll: Talarico Leads Paxton by 3 Points, Abbott Leads Hinojosa by 2 Points in Texas General Election Survey", dated October 30, 2026.
- SEN row: "October 27–30, 2026 | 900 (LV) | ±3.3% | Paxton 45% | Talarico 48% | Brown 0% | Other 0% | Undecided 6%"
- GOV row: "October 27–30, 2026 | 900 (LV) | ±3.3% | Abbott 49% | Hinojosa 47% | 1% | 1% ("Another candidate or write-in" with 1%) | 3%"
- 270toWin (SECONDHAND): "Kreate Strategies 10/30/2026 900 LV · Margin of error ±3.3% 48% 45% 7%".

## 7. YouGov — Oct. 26–29

- Tier: PRIMARY (PDF). URL: https://d3nkl3psvxxpe9.cloudfront.net/documents/ttw_tx_20261026_lv.pdf
- Released: Nov. 1, 2026 (Wikipedia citation date). Sponsor: not named in PDF.
- Verbatim: "Sample 2,141 Texas Likely Voters / Conducted October 26-29, 2026 / Margin of Error ±2.9%". Mode: not stated in PDF text.
- Question note, verbatim: "Respondents who had already voted were asked who they voted for. Undecided voters were asked which candidate they lean toward; leaners are included, and those still undecided are shown as Not sure."
- SEN verbatim: "James Talarico (Democrat) 51%", "Ken Paxton (Republican) 47%", "Someone else 1%", "Not sure 1%", "I would not vote 1%"
- GOV verbatim: "Gina Hinojosa (Democrat) 49%", "Greg Abbott (Republican) 50%", "Someone else 1%", "Not sure 0%", "I would not vote 1%"
- Down-ballot and generic: not asked.

## 8. Quantus Insights (R) — Oct. 26–28

- Tier: PRIMARY (text recovered from the page's embedded blog JSON; the rendered page is JS). URL: https://quantusinsights.org/polling/f/texas-survey-paxton-up-one-abbott-ahead-by-five (post date 2026-10-30)
- Verbatim: "Our October 26 to 28 survey of 1,221 likely voters has Paxton at 48.7 percent and James Talarico at 47.6. Ted Brown, the Libertarian, takes 1.4 and 2.2 percent are undecided. The margin of error on the difference between two candidates runs about ±6.4"
- Verbatim GOV: "Abbott leads Gina Hinojosa 50.7 to 45.8, with Pat Dixon at 1.2 and 2.3 percent undecided."
- Verbatim leaners: "We pushed the 27 undecided Senate respondents to lean and they split almost evenly: nine Talarico, eight Paxton, ten still undecided. The combined ballot is 49.4 to 48.4, Paxton by one. On the Governor side the 28 undecideds broke ten Abbott to six Hinojosa, which widens that race to 51.6 to 46.3."
- Verbatim prior: "Our October 9 to 11 survey had Paxton 47.2 to 46.7."
- MOE per Fox 7 (SECONDHAND, https://www.fox7austin.com/news/paxton-slips-past-talarico-latest-poll-senate-race-enters-final-days): "It has a margin of error of +/- 3.2%." Fox 7 also: "Republicans made up the majority of respondents at 46.7%, with Democrats comprising 39.4% of respondents and Independents at 13.9%." and "The poll found that more than half of respondents had already voted."
- Mode and sponsor: not stated in recovered text. Down-ballot: not reported.

## 9. ActiVote — Oct. 29 readings (all six races)

- Tier: PRIMARY. ActiVote race pages, each "400 likely midterm voters · MoE ±4.9%". Mode: ActiVote app (pages say "Want to be included in our next poll? Check out the app!"). Two-way results only (no undecided or third-party shown). Note: one search summary called the sample "400 registered voters"; the pages say likely.
- SEN (https://www.activote.net/polls/2026/tx-u-s-senate/): "52.1% James Talarico (D) 47.9% Ken Paxton (R) D+4.2%". "The poll was in the field between October 22 and October 28 (median field date of October 25)." "Compared with our October 21 poll, Talarico's lead widened from 2.0% to 4.2%."
- GOV (https://www.activote.net/polls/2026/tx-governor/): "52.1% Greg Abbott (R) 47.9% Gina Hinojosa (D) R+4.2%". "The poll was in the field between October 23 and October 29 (median field date of October 26)." "Compared with our October 21 poll, Abbott's lead narrowed from 5.0% to 4.[2%]".
- LTG (https://www.activote.net/polls/2026/tx-lt-governor/): "56.4% Dan Patrick (R) 43.6% Vikki Goodwin (D) R+12.8%". "The poll was in the field between October 18 and October 29 (median field date of October 24)." "Compared with our October 17 poll, Patrick's lead widened from 7.6% to 12.8%."
- AG (https://www.activote.net/polls/2026/tx-attorney-general/): "53.0% Mayes Middleton (R) 47.0% Nathan Johnson (D) R+6.0%". "The poll was in the field between October 18 and October 29 (median field date of October 23)." "Compared with our October 17 poll, Middleton's lead is essentially unchanged, at 6.0% against 5.8%."
- AGC (https://www.activote.net/polls/2026/tx-agriculture-commissioner/): "50.5% Nate Sheets (R) 49.5% Clayton Tucker (D) R+1.0%". "The poll was in the field between October 18 and October 29 (median field date of October 24)." "Compared with our October 17 poll, the race is essentially unchanged, with Sheets ahead by 1.0% against 0.6%."
- RRC (https://www.activote.net/polls/2026/tx-railroad-commissioner/): "54.6% Bo French (R) 45.4% Jon Rosenthal (D) R+9.2%". "The poll was in the field between October 18 and October 29 (median field date of October 23)." "Compared with our October 17 poll, French's lead widened from 4.2% to 9.2%."

## 10. ActiVote — Oct. 17 and Oct. 21 readings

- LTG Oct. 17, PRIMARY (https://www.activote.net/polls/2026/tx-lt-governor/2026-10-17/): "53.8% Dan Patrick (R) 46.2% Vikki Goodwin (D)". "The poll was in the field between September 27 and October 17 (median field date of October 7)."
- AGC Oct. 17: SNIPPET ONLY (search summary): "Sheets led 50.3% to 49.7%". Consistent with the 0.6 lead quoted on the Oct. 29 page.
- AG Oct. 17: lead 5.8 per Oct. 29 page (shares not fetched). RRC Oct. 17: lead 4.2 per Oct. 29 page. WIKIPEDIA-ONLY RRC row: "ActiVote | September 25 – October 17, 2026 | 400 (LV) | ± 4.9% | French 52% | Rosenthal 48%".
- SEN Oct. 21, WIKIPEDIA-ONLY: "October 17–21, 2026 | 400 (LV) | ±4.9% | Paxton 49% | Talarico 51%". Citation title "Talarico Holds Narrow Lead Over Paxton in Texas Senate Race".
- GOV Oct. 21, WIKIPEDIA-ONLY: "October 17–21, 2026 | 400 (LV) | ±4.9% | Abbott 52% | Hinojosa 48%".
- Sep. 30–Oct. 14 reading (released Oct. 15), WIKIPEDIA-ONLY: SEN "Paxton 48% | Talarico 52%"; GOV "Abbott 51% | Hinojosa 49%".

## 11. A2 Insights — Oct. 23–27

- Tier: WIKIPEDIA-ONLY. Source link is a Google Drive file (https://drive.google.com/file/d/1UACnmnM84Dd1hU0l6iqHNgXkyh5oCelO/view), not fetched.
- SEN row: "October 23–27, 2026 | 631 (LV) | ±4.9% | Paxton 47% | Talarico 50% | Brown — | Other 2% | Undecided 0%"
- 270toWin (SECONDHAND): "A2 Insights 10/29/2026 631 LV · Margin of error ±4.9% 50% 47% 3%"
- GOV: not in Wikipedia governor table.

## 12. CNN / SSRS — Oct. 20–27

- Tier: SECONDHAND. DocumentCloud (https://www.documentcloud.org/documents/28856724-cnn-poll-conducted-by-ssrs-texas-october/) and its API returned HTTP 403.
- Yahoo/syndicated report (https://www.yahoo.com/news/politics/articles/cnn-poll-dems-leading-texas-145034769.html), verbatim: "according to CNN polls released Thursday." "In Texas, Democrat James Talarico leads Republican Ken Paxton by 6 percentage points, 49% to 43%". "However, at least 1 in 8 likely voters in Texas said they could still change their minds before Election Day." "In Texas, 59% disapproved of Trump's job performance, compared with 41% who approved."
- SNIPPET ONLY (search summary): "The poll covered 923 likely voters, interviewed online and by phone Oct. 20-27 and weighted by turnout likelihood ... margin of error of ±4.2 points"; "Republican Texas Gov. Greg Abbott held a narrower 48% to 46% lead over Democrat Gina Hinojosa."
- WIKIPEDIA-ONLY: SEN "October 20–27, 2026 | 923 (LV) | ±4.2% | Paxton 43% | Talarico 49% | Other 5% ("Neither" with 5%) | Undecided 3%". GOV "Abbott 48% | Hinojosa 46% | Other 6% ("Neither" with 4%) | Undecided 0%".
- Breitbart (SECONDHAND) also refers to "a CNN/SSRS poll conducted Oct. 20 to 27".

## 13. Data for Progress (D) — Oct. 23–26/27

- Tier: PRIMARY. URL: https://www.dataforprogress.org/blog/2026/10/30/democratic-senate-candidates-lead-in-maine-michigan-and-texas (Lew Blank, October 30, 2026)
- Verbatim: "Data for Progress surveyed likely voters from October 23-27 in Maine, Michigan, and Texas". (Wikipedia gives October 23–26.)
- SEN verbatim: "In Texas, Democratic State Representative James Talarico leads Republican Attorney General Ken Paxton 49% to 45% in the race for Senate. Libertarian Ted Brown receives 2% of the vote."
- GOV verbatim: "Republican Governor Greg Abbott leads Democratic State Representative Gina Hinojosa 48% to 47%".
- n, MOE, mode: not in fetched text. WIKIPEDIA-ONLY: "712 (LV) | ±4.0%", SEN undecided 4%; GOV Dixon 2%, undecided 4%.

## 14. 254 Labs / YouGov Blue (D) — Oct. 21–26

- Tier: PRIMARY (release page and PDF). URL: https://254labs.io/news/2026-10-tx (PDF: https://254labs.io/news/2026-10-tx.pdf). Released "Wednesday, October 28, 2026". Sponsor: 254 Labs ("YouGov Blue interviewed ... on behalf of 254 Labs").
- Verbatim: "A new 254 Labs poll of Texas statewide races, conducted October 21–26 among 1,000 registered voters, weighted to likely voter targets provided by 254 Labs that include early voting turnout, finds Democrats ahead in all of the statewide contests polled."
- Verbatim mode/MOE: "YouGov Blue interviewed 1,000 Texas registered voters online and via text-to-web from October 21–26, 2026". "The margin of error (a 95% confidence interval) is approximately 4.6%." Leaners: "undecided respondents asked which candidate they lean toward, and those responses combined into a total vote".
- SEN verbatim: "Talarico leads Paxton 51% to 43%, with 5% undecided."
- GOV/LTG/AG/RRC verbatim: "Gina Hinojosa leads Greg Abbott 49% to 46% for governor; Vikki Goodwin leads Dan Patrick 48% to 45% for lieutenant governor; Nathan Johnson leads Mayes Middleton 47% to 45% for attorney general; and Jon Rosenthal leads Bo French 47% to 43% for railroad commissioner."
- AGC: not reported. Crosstabs: subscribers only.
- texpolls.com flags this poll "Political sponsor · excluded from average".

## 15. Texas Southern University (Barbara Jordan Center) — Oct. 21–25

- Tier: PRIMARY (report PDF). URL: https://www.jordanresearchcenter.org/s/TSUStatewideOct2026.pdf (also at https://static1.squarespace.com/static/67aa7aa3e284b002cd6a420e/t/6ae28aaadbf6636957aa51e7/1793231530759/TSUStatewideOct2026.pdf). Released Thursday Oct. 29 (San Angelo Live). Authors listed: Michael O. Adams, Mark P. Jones.
- Verbatim methodology: "a representative survey of 2,000 Texans who are likely to cast a ballot in the November 2026 general election (margin of error of +/- 2.19%). This probability-based survey was fielded (in English and Spanish) between October 21 and October 25, 2026 by contacting a random sample of Texas registered voters via SMS text messages through which the respondents were directed to an online survey platform." Also: "a little more than one-third of the respondents reported they had cast their ballot prior to completing the survey."
- SEN verbatim: "Democrat James Talarico (49%) leads Republican Ken Paxton (47%) by 2 percentage points, with 3% supporting Libertarian Ted Brown and 1% undecided."
- GOV verbatim: "Republican Greg Abbott (50%) leads Democrat Gina Hinojosa (47%) by 3 percentage points, with 2% supporting Libertarian Pat Dixon and 1% undecided."
- LTG verbatim: "Republican Dan Patrick (49%) leads Democrat Vikki Goodwin (45%) by 4 percentage points, with 2% supporting Libertarian Anthony Cristo, 1% supporting the Green Party's Kevin McCormick and 3% undecided."
- AG verbatim: "Republican Mayes Middleton (49%) leads Democrat Nathan Johnson (45%) by 4 percentage points, with 2% supporting Libertarian Tom Oxford and" [4% undecided per San Angelo Live: "Libertarian Tom Oxford received 2%, and 4% were undecided."]
- AGC verbatim: "Republican Nate Sheets (48%) leads Democrat Clayton Tucker (44%) by 4 percentage points, with 2% supporting Libertarian Austin Kelly and 6% undecided." Also: "A super-majority of Texas likely voters do not know enough about either Sheets (65%) or Tucker (66%) to have an opinion of them."
- RRC verbatim: "Republican Bo French (47%) leads Democrat Jon Rosenthal (46%) by 1 percentage point, with 3% supporting Libertarian Arthur DiBianca and 4% undecided."
- Comptroller (SECONDHAND, San Angelo Live): "Republican Don Huffines led Democrat Sarah Eckhardt 50% to 44%. Libertarian V. Alonzo Echavarria-Garza received 1%, Green Party candidate Shehla Faizi received 0%, and 5% were undecided."
- Generic ballot: not in report text.

## 16. Rasmussen Reports — Oct. 20–21

- Tier: PRIMARY. URL: https://www.rasmussenreports.com/public_content/politics/elections/election_2026/election_2026_texas_senate ("Friday, October 23, 2026")
- Verbatim: "The latest Rasmussen Reports national telephone and online survey finds that, if the election were held today, 45% of Likely Texas voters would vote for Paxton, while 45% would vote for Talarico. Five percent (5%) support Libertarian candidate Ted Brown, and five percent (5%) are undecided."
- Verbatim: "The survey of 965 Texas Likely Voters was conducted on October 20-21, 2026 by Rasmussen Reports. The margin of sampling error is +/- 3 percentage points with a 95% level of confidence. Field work for all Rasmussen Reports surveys is conducted by Pulse Opinion Research, LLC."
- Other races: not on page.

## 17. N+ Univision / YouGov — Oct. 13–21

- Tier: PRIMARY (Univision is the sponsor/publisher). URL: https://www.univision.com/noticias/politica/poll-univision-texas-latinos (Wikipedia citation date Oct. 27, 2026)
- Verbatim: "A new N+ Univision/YouGov poll conducted October 13–21, 2026, among 1,000 registered Texas voters finds a closely divided electorate heading into the midterm elections. The statewide sample has an approximate margin of error of ±3.8 percentage points. The survey also includes a total sample of 980 registered Latino voters, with an approximate margin of error of ±3.7 points."
- Verbatim: "Republican Gov. Greg Abbott leads Democrat Gina Hinojosa, 48% to 46%, while Republicans hold a 48% to 45% advantage on the generic U.S. House ballot. In the U.S. Senate contest, Democrat James Talarico leads Republican Ken Paxton 50% to 45%."
- Mode verbatim: "interviewed 1,000 registered voters in Texas online through YouGov from Oct. 13 to Oct. 21, 2026".
- Latino subsample verbatim: "Hinojosa leads Abbott 52% to 43% among Latino voters. Talarico's advantage over Paxton expands to 55% to 37%, while Democrats lead the generic House ballot 52% to 41%."
- Undecided shares: not in text. WIKIPEDIA-ONLY: SEN Other 1%, Undecided 5%; GOV Other 1%, Undecided 5%.

## 18. VoteHub / Verasight — Oct. 1–20

- Tier: PRIMARY (PDF). URL: https://cdn.votehub.com/pdfs/VoteHub_Verasight_Oct_2026_Texas_Report_D8A925D0.pdf
- Verbatim: "Verasight collected survey data for a likely voter model from 601 Texas registered voters between October 1 and October 20 with a margin of error of 4.3 percentage points at the 95% confidence level. The effective sample size for likely voters is 509, and the effective sample size of registered voters is 517. The design effect is 1.18."
- Likely voters (Initial % / With leaners %), verbatim:
  - GOV: "Gina Hinojosa (D) 43.9 46.4", "Greg Abbott (R) 46.5 47.7", "Pat Dixon (L) 2.1 0.7", "Margin (with leaners) R +1.3"
  - SEN: "James Talarico (D) 45.6 47.6", "Ken Paxton (R) 41.4 45.2", "Ted Brown (L) 3.8 1.4", "Margin (with leaners) D +2.4"
  - Generic ballot: "Democrat 43.4 45.1", "Republican 47.4 48.5", "Margin (with leaners) R +3.4" (level of office not specified in text)
- Registered voters, verbatim: GOV "Gina Hinojosa (D) 42.1 44.9", "Greg Abbott (R) 46.3 47.6", "Pat Dixon (L) 2.6 0.9"; SEN "James Talarico (D) 43.3 46.1", "Ken Paxton (R) 41.4 45.3", "Ted Brown (L) 4.5 1.5"; Generic "Democrat 41.2 42.8", "Republican 48.4 49.5", "Margin (with leaners) R +6.7".
- Mode: not stated in text (Verasight panel). Down-ballot: none.

## 19. Emerson College Polling / Nexstar Media — Oct. 17–19

- Tier: PRIMARY. URL: https://emersoncollegepolling.com/texas-2026-poll-toss-up/ (October 22nd, 2026). Sponsor verbatim: "The survey was sponsored by Nexstar Media."
- SEN verbatim: "48% of voters support Democrat James Talarico for U.S. Senate, 46% Republican Ken Paxton, 1% Libertarian Ted Brown, and 5% are undecided. When undecided voters are asked which candidate they lean toward, Talarico's support increases to 49%, Paxton to 48%, and Brown to 3%."
- GOV verbatim: "49% support incumbent Republican Greg Abbott, while 45% support Democrat Gina Hinojosa, and 1% support Libertarian Pat Dixon. Four percent are undecided. With the candidate undecided voters lean toward accounted for, 51% support Abbott, 47% Hinojosa, and 2% Dixon."
- Methodology verbatim: "conducted October 17-19, 2026. The overall sample of Texas likely voters, n=1,000, has a credibility interval, similar to a poll's margin of error (MOE), of +/- 3.1 percent." Mode verbatim: "Data was collected by contacting registered voters via probability-based panel of voters provided by Consensus Strategies using MMS text-to-web, landline using interactive voice response, and additional panel interviews provided by PureSpectrum. The survey was offered in both English and Spanish." (Wikipedia lists ±3.0%.)
- Down-ballot: none in release.

## 20. Fox News Poll (Beacon Research D / Shaw & Co. R) — Oct. 15–19

- Tier: PRIMARY (topline PDF). URL: https://static.foxnews.com/foxnews.com/content/uploads/2026/10/fox_october-15-19-2026_texas_topline_october-21-release.pdf. Release: "for release after 6PM/ET Wednesday, October 21, 2026."
- Verbatim methodology: "Conducted October 15-19, 2026 under the joint direction of Beacon Research (D) and Shaw & Company Research (R), this Fox News Poll includes interviews with a sample of 2,011 Texas registered voters randomly selected from a statewide voter file. Respondents spoke with live interviewers on landlines (205) and cellphones (1,303) or completed the survey online by following a link received via text message (503)." "Results based on the full sample have a margin of sampling error of ±2 percentage points. A subsample of 1,398 has been defined as likely voters (LV), with a margin of error of ±2.5 percentage points."
- SEN verbatim (15-19 Oct 26): Likely Voters "Democrat James Talarico 49%", "Republican Ken Paxton 49", "(Other) *", "(Wouldn't vote) *", "(Don't know) 1". Registered Voters "Democrat James Talarico 52%", "Republican Ken Paxton 46", "(Other) *", "(Wouldn't vote) *", "(Don't know) 1".
- GOV verbatim (15-19 Oct 26): Likely Voters "Democrat Gina Hinojosa 47%", "Republican Greg Abbott 52", "(Other) *", "(Wouldn't vote) -", "(Don't know) 1". Registered Voters "Democrat Gina Hinojosa 49%", "Republican Greg Abbott 50", "(Other) *", "(Wouldn't vote) -", "(Don't know) 1".
- Question wording, verbatim (Q9): "[IF NOT ALREADY VOTED: If the Texas election for governor were today, would you vote for: [IF DON'T KNOW: Do you lean closer to one candidate?]] [IF ALREADY VOTED: When you cast your early or absentee ballot in the election for governor, did you vote for:]". The PDF labels the first block "Likely Voters". Wikipedia's GOV row lists only the RV figures: "2,011 (RV) | Abbott 50% | Hinojosa 49%".
- Down-ballot, generic: not asked (PDF titled "TEXAS SENATE AND GOVERNOR").

## 21. Texas Public Opinion Research (TPOR) — Oct. 15–18

- Tier: PRIMARY. URL: https://texaspublicopinionresearch.substack.com/p/october-poll-in-texas-general-election (released Oct 23, 2026). Topline folder: https://drive.google.com/drive/folders/1vrAnY9diOMs_8_inndJBF6Wfq43ahRzT (not fetched).
- Self-description verbatim: "Texas Public Opinion Research (TPOR)—a nonpartisan polling initiative". Page footer: "© 2026 Luke Warford". Wikipedia labels it "(D)"; texpolls.com says "TPOR director Luke Warford is a Democratic strategist" and flags it "Political sponsor · excluded from average". Sponsor of this wave: not stated.
- Verbatim: "The survey of 969 likely Texas voters was conducted from October 15 to October 18, 2026, and has a margin of error of ±3.9 percentage points." "Note: For this tracking poll, topline results reflect final push tallies, which we introduced for the final leg of the cycle, and forces undecided voters to choose a candidate." Mode: not stated on page (texpolls says "via an online panel").
- SEN verbatim: "Democrat James Talarico (51%) leads Republican Ken Paxton (47%) by four points in the U.S. Senate race, while Libertarian Ted Brown receives 2% of the vote."
- GOV verbatim: "Republican Greg Abbott (51%) leads Democrat Gina Hinojosa (48%) by three points in the Governor's race, with Libertarian Pat Dixon receiving 1% of the vote."
- LTG verbatim: "Republican Dan Patrick (50%) leads Democrat Vikki Goodwin (47%) by three points in the Lieutenant Governor's race. Libertarian Anthony Cristo receives 2% of the vote, and Green Party candidate Kevin McCormick receives less than 1%."
- AG verbatim: "Republican Mayes Middleton (50%) leads Democrat Nathan Johnson (48%) by two points in the Attorney General's race, with Libertarian Tom Oxford receiving 2% of the vote."
- AGC verbatim: "Republican Nate Sheets (50%) leads Democrat Clayton Tucker (48%) by two points in the Agriculture Commissioner's race, with Libertarian Austin Kelly receiving 3% of the vote."
- RRC verbatim: "Republican Bo French (50%) leads Democrat Jon Rosenthal (48%) by two points in the Railroad Commissioner's race, with Libertarian Arthur DiBianca receiving 2% of the vote."
- Comptroller verbatim: "Republican Donald Huffines (50%) leads Democrat Sarah Eckhardt (48%) by two points". Land verbatim: "Republican Dawn Buckingham (49%) leads Democrat Benjamin Flores (48%) by one point".
- Generic verbatim: "Republicans lead by two points on the generic congressional ballot, 51% to 49%." and "Republicans lead by two points on the generic state legislature ballot, 51% to 49%. When asked whether they would vote for the Democratic candidate or the Republican candidate for House of Representatives in their district, 51% choose the generic Republican candidate, while 49% choose the generic Democratic candidate."
- **Variant figures (SECONDHAND, texpolls.com, labeled "includes leaners", i.e. the intermediate push rather than final push):** AGC "Tucker 46% · Sheets 49% ... Undec. 3%"; LTG Goodwin 46%, Patrick 49%, 3%; AG Johnson 46%, Middleton 47%, 5%; RRC Rosenthal 47%, French 49%, 2%.

## 22. Pollfinity Research — Oct. 15–18

- Tier: PRIMARY. URL: https://pollfinity.com/polls/tx-governor-senate-2026-oct ("Released October 22, 2026"; "APTOS, CA")
- Verbatim methodology: "Conducted by Pollfinity Research LLC / Field dates October 15–18, 2026 / Population Registered voters, Texas statewide / Sample size 278 Senate-ballot respondents (297 started) / Margin of error ±6.5 percentage points (95% confidence, weighted)". "Method Text message to web survey (SMS-to-web)". Sponsor: "Exclusive Pollfinity Research Survey"; none named.
- Verbatim results: "Talarico 48% · Paxton 43% · Brown (L) 2% · Someone else 2% · Undecided 5%"; "Hinojosa 46% · Abbott 45% · Dixon (L) 2% · Someone else 2% · Undecided 5%"; "Patrick 46% · Goodwin 42% · Cristo (L) 2% · McCormick (G) 1% · Someone else 2% · Undecided 6%".
- Note: Wikipedia's GOV row lists "Abbott 46% | Hinojosa 45%", the reverse of the release text above.

## 23. CBS News / YouGov — Oct. 8–16 (published Oct. 18)

- Tier: PRIMARY (CBS article + toplines PDF). Article: https://www.cbsnews.com/news/texas-senate-talarico-paxton-poll/ ("Updated on: October 18, 2026"). PDF: https://assets1.cbsnewsstatic.com/hub/cms/prod_cms_alt/file/2026/10/18/a2543f6e-33c4-4bc3-af45-fc50a0b98b34/cbsnews_20261018_texas__sun.pdf
- Verbatim methodology: "This CBS News/YouGov survey was conducted with a representative sample of 1,492 registered voters in Texas interviewed between October 8-16, 2026. ... The margin of error is ± 3.4 points for the sample of registered voters, and ± 3.5 points for likely voters." LV n not stated. Mode: not stated in fetched text.
- SEN verbatim (PDF Q6, "Among likely voters, including those leaning toward Talarico or Paxton"): "James Talarico 51%", "Ken Paxton 49%", "Someone else 0%", "Not sure 0%".
- GOV verbatim (PDF Q11, likely voters incl. leaners): "Gina Hinojosa 48%", "Greg Abbott 52%", "Someone else 0%", "Not sure 0%".
- Down-ballot, generic: not in PDF text.
- Note: 270toWin lists "YouGov 10/18/2026 1,458 LV 51% 49%", likely this poll (LV n not confirmed).

## 24. Cor Strategies (R) for Heritage Action — Oct. 10–15

- Tier: PRIMARY (crosstabs PDF). URL: https://static.dailysignalmedia.org/2026/10/TX-Poll-Crosstabs.pdf (footer "HERITAGE ACTION / TEXAS ELECTION INTEGRITY"). Release date: not stated in PDF; Wikipedia access-date Oct. 28.
- Verbatim header: "TX Election Integrity / Texas | October 10–15, 2026 | 1,409 responses | MoE ±2.61 points". Population and mode: not stated in PDF text (Wikipedia lists "(LV)").
- SEN verbatim: "If the election for U.S. Senate were held today, for whom would you vote? The Democrat, James Talarico, or the Republican Ken Paxton?" Statewide: "James Talarico 44%", "Ken Paxton 40%", "Undecided 16%".
- Other races: none.

## 25. InsiderAdvantage — Oct. 13–14 (posted Oct. 15)

- Tier: PRIMARY (headline only). URL: https://insideradvantage.com/insideradvantage-senate-surveys-texas-paxton-49-talarico-48-kansas-marshall-48-hamilton-47-maine-jackson-49-collins-47/ ("Posted on October 15, 2026")
- Verbatim title: "InsiderAdvantage Senate Surveys: Texas, Paxton 49, Talarico 48; ... Update: All Conducted 10/13-14"
- Verbatim methodology: "Each state 1200 LV; Mixed Mode Text/ Panel;Weighted for Age, Race, Gender, and Political Affiliation; MOE 2.83%" and "Top Line Tabs To Be Posted Separately."
- Brown/undecided: not on page. WIKIPEDIA-ONLY: "Brown 2% | Undecided 1%". No later InsiderAdvantage Texas poll appeared in its Oct. 30–Nov. 1 post list.

## 26. University of Houston Hobby School — Oct. 10–14 (released Oct. 19)

- Tier: PRIMARY. Page: https://www.uh.edu/hobby/texas2026/index.php ("Media Release October 19, 2026"). Report 1 PDF: https://www.uh.edu/hobby/texas2026/statewide26.pdf
- Verbatim methodology: "the Hobby School of Public Affairs at the University of Houston conducted an online statewide survey of likely voters in Texas, with an oversample of Latino and rural voters, between Oct. 10 and Oct. 14, 2026. Likely voters were contacted via SMS text message and directed to an online survey platform with the option to answer the survey in English or Spanish. The overall sample population of 2,000 (margin of error of +/- 2.19%) likely voters was adjusted via multidimensional calibration weighting". Sponsor: none stated.
- SEN verbatim: "Democrat James Talarico (48%) leads Republican challenger Ken Paxton (46%) by two points in the race for the U.S. Senate. Libertarian Ted Brown follows with 3%, and another 3% are undecided."
- GOV verbatim: "Republican incumbent Greg Abbott (49%) leads Democrat Gina Hinojosa (46%) by three percentage points. Libertarian Pat Dixon follows with 2%, and 3% are undecided."
- LTG verbatim: "Incumbent Republican Dan Patrick leads Democrat Vikki Goodwin by five points, 47% to 42%, in the election for lieutenant governor. Libertarian Anthony Cristo follows with 3% and Green Party candidate Kevin McCormick with 1%. 7% were unsure."
- AG verbatim: "Republican Mayes Middleton is leading Democrat Nathan Johnson 47% to 42%. Libertarian Tom Oxford has 3%, and 8% are unsure."
- AGC verbatim: "Republican Nate Sheets is leading Democrat Clayton Tucker, 46% to 40%, in the election for agriculture commissioner. Libertarian Austin Kelly has 2%, and 12% are unsure."
- RRC verbatim: "Republican Bo French is leading Democrat Jon Rosenthal, 45% to 43%, in the race for Texas Railroad Commissioner. Libertarian Arthur DiBianca has 2%, and 10% are unsure."
- Comptroller verbatim: "Republican Don Huffines is leading Democrat Sarah Eckhardt, 47% to 40%". Land verbatim: "incumbent Republican Dawn Buckingham has support from 47% of likely voters, while Democrat Benjamin Flores has 40%."
- Rural subsample verbatim (Report 2): "Among Texas rural voters, Republican Ken Paxton leads Democrat James Talarico by 38 percentage points, 65% to 27%, with 4% supporting Brown and 4% still unsure." "Republican Greg Abbott leads Democratic challenger Gina Hinojosa among rural voters, 66% to 29%." "Republican Dan Patrick has a 40-percentage point advantage over Democrat Vikki Goodwin, 65% to 25%".
- Generic ballot: not in report text.

## 27. GS Strategy Group (R) / New River Strategies (D) for Cook Political Report — Oct. 9–13

- Tier: WIKIPEDIA-ONLY. Cook page (https://www.cookpolitical.com/analysis/survey-research/battleground-district-project/senate-battleground-district-project-october) returned HTTP 403. 270toWin publication date 10/21/2026, so it falls in the release window.
- SEN row: "October 9–13, 2026 | 934 (LV) | — | Paxton 44% | Talarico 49% | Brown 3% | — | Undecided 4%"
- GOV row: "Abbott 48% | Hinojosa 46% | 3% | — | 3%" (footnote: "Poll sponsored by The Cook Political Report").
- 270toWin (SECONDHAND): "New River / GSG 10/21/2026 934 LV 49% 44% 7%".

## 28. Talarico campaign internal polling (no numbers released)

- Tier: SECONDHAND (Breitbart, citing an unfetched NYT report). URL: https://www.breitbart.com/politics/2026/10/31/report-talaricos-own-polls-show-texas-senate-race-tighter-than-democrats-admit/
- Verbatim: "Democrat Senate candidate James Talarico's private polling shows his Texas race against Republican Attorney General Ken Paxton far closer than the high-profile public surveys that have handed him a lead, according to a report published Saturday." "The candidate's internal numbers match those tighter surveys, people close to the campaign told the Times."
- No toplines, dates, or n published.

---

## Borderline: fielded before Oct. 15 and released Oct. 12–14 (outside the stated window; listed for completeness)

- **UT / Texas Politics Project** (PRIMARY, http://texaspolitics.utexas.edu/blog/latest-ut-texas-politics-poll-finds-historic-levels-of-competition-in-texas-midterm-elections, dated "October 13, 2026"). Verbatim: "The poll was conducted September 25 to October 5, 2026, with trial ballot results presented among a sample of 861 likely voters (LV), producing a margin of error of +/- 3.34 percentage points." Likely voters were "drawn from an overall sample of 1,200 registered voters". Mode per the August wave: internet, conducted by YouGov.
  - SEN: "Paxton trails State Representative James Talarico 47% to 50%, with 1% preferring Libertarian Party candidate Ted Brown, and 2% preferring a non-specified 'someone else.'"
  - GOV: "Hinojosa holding a statistically insignificant one-point lead over the incumbent, 49% to 48%, with 3% preferring an unspecified 'someone else.' The Libertarian Pat Dixon received 1%"
  - LTG: "Dan Patrick (incumbent) (R) 46%, Vikki Goodwin (D) 49%, Anthony Christo (L) 2%, Kevin McCormick 1%, 'someone else' 2%."
  - AG: "Mayes Middleton (R) 47%, Nathan Johnson (D) 48%, Tom Oxford (L) 1%, 'someone else' 3%."
  - RRC: "Bo French (R) 46%, Jon Rosenthal (D) 47%, Arthur DiBianca (L) 3%, 'someone else' 4%."
  - Comptroller: "Don Huffines (R) 47%, Sarah Eckhardt (D) 46%, V. Alonzo Echavarria-Garza (L) 2%, Shehla Faizi (G) 1%, 'someone else' 3%."
  - AGC: not found in captured text.
  - Generic verbatim: "47% to 42% for the U.S. Congress, and 48% to 43% in the Texas Legislature" (registered voters); "likely voters only preferring the generic Republican congressional candidate by one point over the generic Democrat, 48% to 47%, and by a similar 1-point margin, 49% to 48% for generic candidates running for the Texas Legislature."
  - Note: search results described this as the "final" UT/TPP pre-election poll; no later TPP poll was found.
- **Marist** (WIKIPEDIA-ONLY; PDF https://maristpoll.marist.edu/wp-content/uploads/2026/10/Marist-Poll_TX-NOS-and-Tables_202610131056%5Eal3j7.pdf not fetched). Oct. 8–11. SEN LV "Paxton 45% | Talarico 47% | Other 4% | Undecided 4%" (±4.9%); RV 1,196 "Paxton 44% | Talarico 48%" (±4.3%). GOV LV "Abbott 49% | Hinojosa 45% | 2% | 3%". 270toWin publication date 10/14/2026.
- **Quantus Insights (R)** Oct. 9–11 (WIKIPEDIA-ONLY; also quoted in the Oct. 30 Quantus post as "Paxton 47.2 to 46.7"). 854 LV ±3.6%. Wikipedia: "Paxton 47% | Talarico 47% | Brown 2% | Undecided 4%".
- **ReconMR / Siena** Oct. 5–8 (WIKIPEDIA-ONLY; PDF https://reconmr.com/wp-content/uploads/2026/10/TXP004-October-Press-Release.pdf, "For Immediate Release: Tuesday, October 13, 2026", not fetched). 617 LV ±4.4%. SEN "Paxton 44% | Talarico 48% | Other 3% | Undecided 5%"; GOV "Abbott 48% | Hinojosa 47% | Other 2% | Undecided 3%". **Conflict:** a search summary said this poll "had Paxton at 47% and Talarico at 46%"; snippet only, not verified.
- **GBAO (D) for the Hinojosa campaign** Oct. 5–8 (WIKIPEDIA-ONLY; memo https://ginafortexas.com/wp-content/uploads/2026/10/TX-Gov-Poll-Memo-101226.pdf, not fetched). 800 LV ±3.5%. GOV "Abbott 45% | Hinojosa 47% | Dixon 4% | Undecided 4%".

---

## Aggregates

- **270toWin, Senate** (SECONDHAND, fetched: https://www.270towin.com/2026-senate-polls/texas). Verbatim: "Talarico vs. Paxton ... Average of 11 Polls† 49.5% 46.1%". Method note verbatim: "The average includes all polls within seven days of the date of the most recent poll, limited to one poll from any source." The page lists polls by publication date, including "CNN / SSRS 10/29/2026 923 LV · Margin of error ±4.2% 49% 43% 8%" and "Texas Southern University 10/29/2026 2,000 LV · Margin of error ±2.2% 49% 47% 4%". AtlasIntel, 254 Labs, Cor Strategies, Pollfinity, Rasmussen and On Point do not appear in the captured list.
- **RealClearPolling** (https://www.realclearpolling.com/polls/senate/general/2026/texas/talarico-vs-paxton): HTTP 403, not fetched.
- **Wikipedia aggregate table, Senate** (WIKIPEDIA-ONLY; secondhand of the aggregators): 270toWin "October 13 – November 1 | updated November 2 | Paxton 46.1% | Talarico 49.5% | Talarico +3.4%"; Decision Desk HQ "through November 1 | 45.1% | 49.2% | Talarico +4.1%"; FiftyPlusOne "45.6% | 49.4% | Talarico +3.8%"; RealClearPolitics "October 15 – November 1 | 46.5% | 49.0% | Talarico +2.5%"; Texas Tribune "through October 28 | 46.4% | 49.1% | Talarico +2.7%"; Silver Bulletin "45.9% | 49.2% | Talarico +3.3%".
- **Wikipedia aggregate table, Governor** (WIKIPEDIA-ONLY): 270toWin "Abbott 49.3% | Hinojosa 47.1% | Abbott +2.2%"; DDHQ "49.1% | 47.4% | Abbott +1.7%"; FiftyPlusOne "48.9% | 47.4% | Abbott +1.5%"; RCP "October 15 – November 1 | 49.8% | 47.3% | Abbott +2.5%"; Silver Bulletin "49.2% | 47.1% | Abbott +2.1%".
- **Quantus's own citation of averages** (PRIMARY, Quantus post): "Published averages at the end of our fieldwork had the Senate race at Talarico +2.1 (RealClearPolling) and +3.5 (270toWin). ... For Governor, the averages show Abbott +2.1 to +2.5".
- **texpolls.com, down-ballot** (SECONDHAND aggregator, fetched). Excludes campaign- and operative-sponsored polls (TPOR, 254 Labs, Stratus) from its averages; does not list ActiVote.
  - LTG (https://texpolls.com/races/lt-governor-2026): "Goodwin 44.8 %", "Patrick 47.0 %", "5-poll average · R+2.2 · likely voters · Sept. 11 to Oct. 25"
  - AG (https://texpolls.com/races/attorney-general-2026): "Johnson 43.7 %", "Middleton 46.7 %", "7-poll average · R+3.0 · likely voters · July 30 to Oct. 25"
  - RRC (https://texpolls.com/races/railroad-commissioner-2026): "Rosenthal 44.3 %", "French 45.5 %", "4-poll average · R+1.2 · likely voters · July 30 to Oct. 25"
  - AGC (https://texpolls.com/races/agriculture-commissioner-2026): "Too few polls for a full average Mean of 2 polls, latest Texas Southern University, Oct. 25"; "Democrat : Clayton Tucker Democrat 42 % percent in these polls", "Republican : Nate Sheets Republican 47 % percent in these polls".
- Decision Desk HQ and Split Ticket pages: not fetched (fetch cap).

## Generic legislative / congressional ballot (collected above, gathered here as pointers)

- TPOR Oct. 15–18: state legislature R 51, D 49; congressional R 51, D 49 (section 21).
- Univision/YouGov Oct. 13–21: generic U.S. House R 48, D 45 (section 17).
- VoteHub/Verasight Oct. 1–20: "Generic ballot" LV R 48.5, D 45.1 with leaners (office not specified; section 18).
- UT/TPP (borderline, released Oct. 13): Texas Legislature LV R 49, D 48; RV R 48, D 43 (borderline section).
- No other in-window generic Texas Legislature ballot was found.

## Searched for, nothing in-window found

Texas Lyceum, Dallas Morning News/UT Tyler, Quinnipiac, Morning Consult, Cygnal, co/efficient, Echelon Insights, Texas Hispanic Policy Foundation, and any October Mason-Dixon or AARP Texas poll. These came from one extended WebSearch per group plus the Wikipedia tables. The search was not exhaustive: absence from those results does not establish that no such poll exists. 270toWin lists Mason-Dixon (9/15) and AARP (9/10), both before the window.

# Texas 2026: Early-Vote Benchmarks for the Final Calls

*Set in advance on Oct. 30, 2026, so the goalposts can't move afterward. This is a rough model built on public data, not a forecast.*

## How to read the data

**Source:** Transparency USA statewide page (turnout.transparencyusa.org/2026-general/), and its downloadable snapshot PDF.

**Timing:** each day's data is posted the **next day after 11 a.m.** Always check the "through" date at the top of the page.

| Checkpoint | Data covers |
|---|---|
| Friday, Oct. 30 | Through Thursday (Day 11) |
| Saturday, Oct. 31 | Through Friday (Day 12, last day of early voting) |
| Sunday, Nov. 1 | Cleanup: the last counties plus late mail |

## The three measures

| Measure | How to compute | Through Wed., Oct. 28 | Through Thu., Oct. 29 (244 of 254 counties) |
|---|---|---|---|
| **Primary margin** | (DEM Only + DEM Mixed) − (GOP Only + GOP Mixed) | **D +59,761** | **D +45,173** |
| **Reliable-voter gap** | Not-yet-voted Republicans who voted in 3 or 4 of the last four GOP primaries, minus the same for Democrats ("Party affiliation" page of the snapshot) | **about 203,000** | **174,183** |
| **Young-voter share** | (Ages 18–24 voted + 25–34 voted) ÷ total votes cast ("Age bands" page) | **18.0%** | **18.7%** |

**Check the county count before reading any snapshot.** The through-Thursday snapshot first posted at 10:37 a.m. Friday with 95 of 254 counties and showed D +81,624. By 12:52 p.m., with 244 counties, it showed D +45,173. The big Democratic counties report first, so an early post overstates the Democratic lead. Wait for about 240 counties.

## Assumptions behind the benchmarks

- Voters with no primary history lean **D +5 to +12**. Evidence: Hispanic polling D +10 to +18 this year; younger and more female electorate; Ryan's note that these voters lean "center and/or left"; 2018 adjusted for the classification problem ≈ D +10 to +14. Counter-evidence: 2022 ≈ R +4; 2024's new-voter surge helped Trump.
- Election Day adds roughly **200,000 net Republican primary voters**, the size of their reliable reserve.
- About 95% of primary voters back their party's candidates (Ryan's rule of thumb).
- Final non-primary electorate ≈ 4 million, so each point of lean ≈ 40,000 votes.
- **Each 100,000 votes of early-vote primary margin moves the result only about 1 point.** How the new voters break matters more, and it isn't visible until votes are counted.
- Abbott runs about **2.5 points ahead of Paxton** in the polls, so Hinojosa needs roughly a **Talarico +3** night.

## Friday (data through Thursday): trend check only

| Democratic primary lead | Signal |
|---|---|
| Above 45,000 | Republican catch-up slowing. Slight nudge toward Talarico |
| 25,000–45,000 | On trend (expected ≈ 40,000). No change |
| Below 25,000 | Republicans closing faster. Slight nudge toward Paxton |

**Result (read Oct. 30 from the 12:52 p.m. snapshot, 244 of 254 counties):** D +45,173. That's 173 votes over the line, inside the noise of the 10 missing counties. Read: **on trend, no nudge.** Details in [`analysis.md`](analysis.md#friday-trend-check-data-thru-thu-oct-29-read-oct-30). Thresholds above are unchanged.

## Saturday (data through Friday): the main read

| Final early-vote primary margin | U.S. Senate | Governor |
|---|---|---|
| D +25,000 or more | **Lean Talarico** (+1 to +3) | Toss-up, leaning Abbott |
| R +50,000 to D +25,000 | **Lean Talarico, narrowly** (0 to +2) | Lean Abbott |
| R +50,000 to R +150,000 | **Toss-up** | Likely Abbott |
| Worse than R +150,000 | **Lean Paxton** | Abbott |

**Adjustments:**
- **Move up one row (toward Talarico)** if the reliable-voter gap is **under 150,000** OR the young-voter share is **19% or more**.
- **Move down one row (toward Paxton)** if the reliable-voter gap is **over 225,000** OR the young-voter share is **under 17.5%**.

**Expected landing spot:** about **D +20,000**, the "Lean Talarico, narrowly" row, before adjustments.

## Sunday: confirm, or flag a problem

- **Counties catching up:** if the last counties plus late mail move the margin by **more than 25,000** either way, re-check Saturday's row.
- **Final polls:**
  - If the Abbott–Paxton gap **grows past 4 points**, move the governor call one step toward Abbott.
  - If it **shrinks below 2 points**, move it one step toward Hinojosa.

## When turnout alone gets us to ~75% (added Oct. 30)

*These are pre-count signals only: the final early-vote composition and Election Day turnout, before any votes are counted. They supersede the confidence levels implied by the Saturday table above.*

### The model

**Projected Talarico margin (pts) ≈ 1.6 + 0.9 × (final early-vote primary margin ÷ 100,000)**

- Inputs: non-primary voters lean D +5 to +12 (central ~D +8.5) and number ~4M; Election Day adds ~200,000 net Republican primary voters; 95% primary-voter loyalty; ~10M total votes.
- **Uncertainty: about ±2.3 pts**, so ~75% confidence means a projected margin of at least ~1.55 pts either way.
- The uncertainty was narrowed from ±2.7 after reviewing the evidence that the 2024 shift among occasional voters has reversed:
  - 2025 NJ and VA results
  - State legislative specials since Jan. 2025 averaging D +5.6, with Democrats keeping ~10 pts more of their prior turnout (Ballotpedia)
  - 27 Democratic flips to Republicans' 0, including SD-9 (NBC)
  - Texas Hispanic voters swinging ~11 pts toward Democrats since 2024 (Univision)
  - In a non-presidential year, Trump's occasional voters tend to stay home
- A 2022-style break, with non-primary voters at **R +4** (their 2022 lean), is treated as a **10–15% tail risk**. Against the central D +8.5, that is 12.5 points of lean across ~4M voters, about 500,000 votes, so every result shifts **~5 pts toward Republicans**. If the early vote ends near D +30,000, Talarico +1.9 becomes Paxton +3.1. Turnout data won't show it. *(Corrected Oct. 30: this line first said "slightly Republican" and ~3.5 pts, which matches a near-even lean, not 2022's R +4.)*
- **Overall odds before Saturday's data:** ~70–75% Talarico.

### Thresholds: final early-vote primary margin (Saturday's data)

| Race | Democrat ~75% if final early margin is... | Republican ~75% if... |
|---|---|---|
| U.S. Senate | **About even or better** | R +350,000 or worse |
| Lt. Governor | D +22,000 or better | R +322,000 or worse |
| Agriculture | D +160,000 or better | R +185,000 or worse |
| Attorney General | D +244,000 or better | R +100,000 or worse |
| Governor | D +272,000 or better | **R +72,000 or worse** |

Each race's margin is (Senate margin − 0.5) − its candidate adjustment − its drop-off, with the adjustments in [`analysis.md`](analysis.md#down-ballot-statewide-races); ~75% means a margin of at least 1.55 pts either way. *(Corrected Oct. 30: the Lt. Governor row first read D +50,000 / R +295,000, which used an adjustment of −0.75 instead of the analysis's −1. Governor and AG were one row at D +270,000 / R +72,000; AG on its own is D +244,000 / R +100,000.)*

### Adjustments

| Signal | When | Effect on projected Talarico margin |
|---|---|---|
| Reliable-voter gap **under 150,000** | Sunday | +0.4 pts (≈ +45,000 votes of early margin) |
| Reliable-voter gap **over 225,000** | Sunday | −0.4 pts |
| Election Day turnout **light**: big counties under ~30% of their early vote | Tuesday afternoon | +0.5 pts |
| Election Day turnout **heavy**: over ~40%, especially Republican-base counties | Tuesday afternoon | −0.7 pts |

### Timing

- **Saturday (after 11 a.m., possibly as late as evening):**
  - The Wednesday data posted at 6:40 p.m. Thursday, so updates can come late.
  - Confirm the page says data runs **through Friday, Oct. 30**, and check how many counties have reported (247 of 254 through Wednesday). If a big county is missing, wait for Sunday.
  - **Projected landing spot ≈ D +20,000. That clears the Senate's 75% line**, so the model would put Talarico at ~75% before Election Day.
- **Sunday:** the reliable-voter gap adjustment.
- **Tuesday afternoon:** the Election Day turnout adjustment, from the marker counties.
- **Governor, AG and Agriculture can't reach 75% for the Democrat on turnout alone.** Abbott can reach 75% if the early margin ends R +72,000 or worse, and Middleton at R +100,000 or worse, or with heavy Republican-county Election Day turnout. Goodwin is the one down-ballot Democrat who can: at D +22,000 or better.

## What it means for the Legislature

Applies to any "Lean Talarico" outcome:

| Chamber | Now | Expected |
|---|---|---|
| Texas Senate | 19 R – 12 D (16 of 31 seats on the ballot) | Democrats at 13–14. **14 is about a coin flip**; it would let Democrats block bills from reaching the floor. No majority. |
| Texas House | 88 R – 62 D (all 150 seats on the ballot) | Democrats gain **4–8**. Republicans keep the majority, with a thinner margin and a Speaker more dependent on Democratic votes. A majority only comes into play at Talarico +5 or better. |

## Election night rule of thumb

Early votes are counted first, so Democrats will look strong early.
- **Talarico up ~4+ on the early vote:** likely holds.
- **Up only 1–2:** likely doesn't, once Election Day votes come in.

## Election Day turnout: marker counties

### When you'll know

| When | What you get |
|---|---|
| Tuesday, during the day | Big counties post running check-in counts on their elections websites (frequency varies by county). There is **no statewide figure** during the day, so add up the counties yourself. |
| 7 p.m. Central | Most polls close; El Paso closes at 8 p.m. Central. Early-vote results are released first. |
| ~9–11 p.m. | Election Day votes mostly counted in big counties. This is the real Election Day total. |
| Overnight | Firm statewide number. |

### The yardstick

**Compare each county's Election Day votes with its own final early-vote total** (early in person plus mail).

- Statewide, I expect ~7.4M early votes and ~10M total, so ~2.6M on Election Day, about **35% of the early vote**. That's similar in raw numbers to 2022 (2.59M).
- **Above ~40%:** heavy. Good for Republicans; the Democratic early lead is at risk.
- **~30–40%:** normal. Benchmarks hold.
- **Below ~30%:** light. The early vote mostly is the election, which is good for Democrats this year.
- **Where the heavy turnout is matters as much as how heavy it is.** Heavy in Republican counties is a Republican sign; heavy in Democratic counties is a Democratic sign.
- **Midday counts are a pace check, not a verdict.** By early afternoon a county may be a third to halfway to its final count. That's an assumption about the usual daily pattern, not verified.
- **Lines aren't turnout.** Tarrant cut 92 polling places, so long lines there may mean fewer sites, not more voters. Use check-in counts.

### How to read the table

- **Day 8 votes** and **primary-voter lead** come from the county Day 8 table: Democratic primary voters (incl. mixed) minus Republican primary voters (incl. mixed), in percentage points of early voters.
- **Gain vs. 2022** is the change in turnout points from the same day in 2022 (TexPolls).
- **Est. final early** = Day 8 votes × 1.45, the statewide ratio of projected final early vote to Day 8.
- **Light below** and **Heavy above** are 30% and 40% of that estimate.
- **Recompute all three with each county's actual final early-vote total** once it's posted Saturday or Sunday.

### Democratic base: heavy turnout here helps Democrats

| County | Day 8 votes | Gain vs. 2022 | Primary-voter lead | Est. final early | Light below | Heavy above | Why watch |
|---|---|---|---|---|---|---|---|
| Harris | 705,585 | +8.0 | D +17 | 1,023,000 | 307,000 | 409,000 | Largest county; edges of the county showed purple on House maps |
| Dallas | 419,555 | +10.8 | D +31 | 608,000 | 183,000 | 243,000 | Turnout gain second only to Tarrant among big counties |
| Travis | 288,708 | +9.0 | D +42 | 419,000 | 126,000 | 167,000 | Deepest-blue big county; tests Democratic intensity |
| Bexar | 335,516 | +6.6 | D +21 | 486,000 | 146,000 | 195,000 | Slowest-growing big blue county; HD-118, 121, TX-35 |
| El Paso | 105,659 | +8.4 | D +34 | 153,000 | 46,000 | 61,000 | Lowest turnout of the big counties (20%); polls close an hour later |
| Fort Bend | 184,797 | +9.0 | D +12 | 268,000 | 80,000 | 107,000 | Diverse suburb; Houston-area House seats |
| Hays | 63,449 | +8.2 | D +18 | 92,000 | 28,000 | 37,000 | Austin-San Antonio growth corridor; college voters |

### Swing: whoever wins Election Day here likely wins the county

| County | Day 8 votes | Gain vs. 2022 | Primary-voter lead | Est. final early | Light below | Heavy above | Why watch |
|---|---|---|---|---|---|---|---|
| Tarrant | 390,729 | +11.7 | D +7 | 567,000 | 170,000 | 227,000 | The swing county; county judge; SD-9; many purple House seats. Lines ≠ turnout here |
| Williamson | 159,588 | +9.4 | D +6 | 231,000 | 69,000 | 93,000 | Austin suburbs; House map still pink |
| Collin | 257,275 | +8.2 | R +4 | 373,000 | 112,000 | 149,000 | Suburban Republicans; the Paxton backlash test |
| Denton | 223,396 | +8.8 | R +4 | 324,000 | 97,000 | 130,000 | Same as Collin |
| Brazoria | 79,515 | +9.5 | R +6 | 115,000 | 35,000 | 46,000 | Fast-growing Houston suburb; big turnout gain |
| Nueces | 49,455 | +4.2 | D +1 | 72,000 | 22,000 | 29,000 | Corpus Christi; HD-34 and TX-34; weak turnout gain |
| Bell | 55,964 | +6.5 | R +5 | 81,000 | 24,000 | 32,000 | Military (Fort Cavazos); low turnout |
| Jefferson | 41,459 | +6.4 | D +3 | 60,000 | 18,000 | 24,000 | Beaumont; working-class swing |
| Brazos | 34,906 | +7.7 | R +11 | 51,000 | 15,000 | 20,000 | Texas A&M; young voters; 35% non-primary voters |

### Republican base: heavy turnout here is the Republican comeback signal

| County | Day 8 votes | Gain vs. 2022 | Primary-voter lead | Est. final early | Light below | Heavy above | Why watch |
|---|---|---|---|---|---|---|---|
| Montgomery | 120,877 | +3.0 | R +27 | 175,000 | 53,000 | 70,000 | **Lagging early vote.** A big Election Day here is the clearest Republican catch-up sign |
| Comal | 45,983 | +3.4 | R +28 | 67,000 | 20,000 | 27,000 | Also lagging; Hill Country suburbs |
| Galveston | 75,000 | +7.5 | R +13 | 109,000 | 33,000 | 44,000 | Coastal Republican suburb |
| Ellis | 45,775 | +7.9 | R +11 | 66,000 | 20,000 | 27,000 | DFW exurb, south |
| Parker | 38,715 | +7.2 | R +48 | 56,000 | 17,000 | 22,000 | Deep-red DFW exurb, west |
| Rockwall | 28,113 | +6.8 | R +29 | 41,000 | 12,000 | 16,000 | Affluent DFW exurb |
| Kaufman | 30,939 | +7.9 | R +9 | 45,000 | 13,000 | 18,000 | Fast-growing DFW exurb, east |
| Johnson | 36,781 | +7.2 | R +28 | 53,000 | 16,000 | 21,000 | DFW exurb, south of Tarrant |
| Guadalupe | 34,858 | +4.8 | R +10 | 51,000 | 15,000 | 20,000 | San Antonio exurb; lagging |
| Lubbock | 53,372 | +6.4 | R +25 | 77,000 | 23,000 | 31,000 | West Texas anchor |
| Midland | 20,473 | +4.4 | R +42 | 30,000 | 9,000 | 12,000 | Oil patch; lagging |
| Smith | 45,854 | +6.1 | R +28 | 66,000 | 20,000 | 27,000 | East Texas anchor (Tyler) |

### Hispanic and border: did 2024's shift toward Trump hold?

Democratic-primary history **overstates** Democratic strength here, because local races are decided in Democratic primaries. Trump won several of these counties in 2024.

| County | Day 8 votes | Gain vs. 2022 | Primary-voter lead | Est. final early | Light below | Heavy above | Why watch |
|---|---|---|---|---|---|---|---|
| Hidalgo | 113,939 | +8.6 | D +35 | 165,000 | 50,000 | 66,000 | Biggest Valley county; TX-15 and TX-34 |
| Cameron | 53,960 | +6.4 | D +28 | 78,000 | 23,000 | 31,000 | HD-37, TX-34; record Democratic primary turnout in March |
| Webb | 29,532 | +6.9 | D +54 | 43,000 | 13,000 | 17,000 | Laredo; TX-28 (Cuellar) |
| Maverick | 6,137 | +5.2 | D +63 | 9,000 | 3,000 | 4,000 | Eagle Pass; swung hard to Trump in 2024 |
| Val Verde | 6,583 | +6.3 | D +5 | 10,000 | 3,000 | 4,000 | Del Rio; TX-23 |
| **Starr** | 5,906 | **+0.2** | D +76 | 9,000 | 3,000 | 3,000 | **Lagging badly.** Swung hardest to Trump; low turnout here is a warning for Democrats |
| **Zapata** | 1,345 | **−6.1** | D +86 | 2,000 | 1,000 | 1,000 | **Below 2022.** Went Republican in 2020 and 2024 |

### Quick read on election night

- **Republican catch-up:** Montgomery, Comal, Midland and Guadalupe go heavy (above 40%) while Dallas, Travis and Harris stay normal or light.
- **Democratic hold:** the Republican-base counties come in normal or light, and Tarrant, Collin and Denton stay under ~35%.
- **Border warning:** Starr, Zapata and Maverick stay light while Hidalgo and Cameron are normal. Hispanic Democrats aren't turning out where 2024's shift was biggest.

## Sources

- Ryan Data & Research, *Early Voting Report: Texas, Day 8* (2022 and 2024 same-day comparisons; 2018 and 2022 final totals)
- Transparency USA / JPM Strategies, statewide and Tarrant snapshots through Oct. 28, 2026
- TexPolls county early-voting dataset (2022 same-day turnout by county)
- Polling: University of Houston Hobby School, Univision, Emerson, Marist, YouGov; PollCheck and MultiState averages

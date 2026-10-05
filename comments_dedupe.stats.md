# Comment dedupe stats report

mode: FULL
original records: 273756 (yt=210496, cb=63260)
overlap between files: 10127 shared commentIds, 17 shared videoIds

## Noise bucket
- too_short: 25235
- single_word: 23721
- empty_or_emoji_only: 2146
- spam_pattern: 743
- mentions_only: 294
- promo_link: 95
- source yt: 35883/210496 dropped (17.0%)
- source cb: 16351/63260 dropped (25.8%)

## Collapsing
- exact duplicates removed: 14525
- near-dup groups merged: 1739 (covering 4179 records)
- theme clusters: 168 (covering 51976 records)
- tail uniques kept in full: 159211

## Reduction
- volume represented in cleaned output: 221522 of 273756 (80.9%; the other
  19.1% sits in the noise bucket above, preserved as counts not text)
- output rows: 159379 (159211 unique + 168 clusters) = 41.8% fewer rows;
  every kept record counted exactly once (verified: unique dup_counts +
  cluster counts = 221522)

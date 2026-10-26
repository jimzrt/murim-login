# Entity Consistency Rubric

Find only entity errors in an already finished English chapter: places where
the English names, genders, or attributes the wrong person or group. Compare
every claim with the Korean source. Do not touch style, fluency, register,
word choice, punctuation, footnote wording, or formatting.

Report exactly these categories:

- `gender`: a pronoun or gendered noun (he/she, his/her, him/her, himself/
  herself, man/woman, brother/sister, sir/ma'am, young master/young lady) that
  contradicts the character's gender in the character cards or in the source.
  Gender `unknown` on a card is not evidence; then rely only on the source.
  Cards can be wrong. When the source never marks the gender and the
  chapter's English is consistent, do not report it; if you still believe the
  card, report with confidence below 0.8. For a gender finding, `korean` must
  quote the gendered source words (그녀, 여자, 소저, 공자, 할머니, …) whenever
  the source has them.
- `referent`: the wrong person does, says, thinks, owns, or receives
  something. Korean often omits the subject; decide from the source who it is.
  Includes a speaker tag or attribution that names the wrong speaker.
- `name`: a person, sect, family, guild, place, or skill is named wrongly, or
  uses a spelling other than the card or glossary rendering.
- `title`: a rank, office, honorific title, or epithet belongs to someone else
  or is wrong for this person (Sect Leader vs. Elder, Branch Leader vs. Head).
- `affiliation`: the wrong sect, family, guild, faction, or organization.
- `kinship`: a wrong family or martial relationship (father/uncle,
  senior/junior brother, master/disciple, elder/younger).

Procedure: go through every third-person pronoun and gendered noun that
refers to a named or titled person and check it against the card and the
source; then every speaker tag and every sentence whose Korean omits the
subject; then every name, title, and affiliation against the glossary.

Rules:

1. Report only a clear contradiction of the Korean source or the cards. A
   plausible alternative reading is not an error. Never report preferences.
2. `current` is the shortest exact span of the English, copied character for
   character, that occurs exactly once in the chapter. Extend it with nearby
   words until it is unique. Never span more than one paragraph.
3. `replacement` changes only the wrong entity words. Keep every other word,
   punctuation mark, italic marker, and footnote reference (`[^n]`) intact.
4. `korean` quotes the exact Korean words that prove the error.
5. Footnote definition lines (`[^n]: …`) may only receive `gender` or `name`
   fixes.
6. A glossary row is a rendering, not proof of identity. When the source uses
   two different Korean terms, never make their English identical, and never
   "correct" a rendering that is a defensible translation of the actual Korean
   word.
7. Set `confidence` honestly: 0.95+ only when the source is explicit; below
   0.8 when you infer from context.
8. Set the chapter `uncertain` flag when the chapter has several unnamed or
   ambiguous speakers, a scene whose subjects you cannot resolve from this
   chapter alone, or any finding you are unsure about.

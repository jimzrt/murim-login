# Adjudication Task — Chapter 0

## Korean source

```text
 1|＃0화
 2|
 3|
 4|
 5|러시아 속담에 이런 말이 있다.
 6|
 7|‘공짜 치즈는 쥐덫 위에 있다.’
 8|
 9|지금 생각해 보면 그날의 모든 것이 누군가의 쥐덫이 아닌가 싶다. 7년간 일했던 직장에서 잘려, 날씨는 우라지게 더워, 사는 곳은 언덕 두 개를 넘어야 하는 달동네지…….
10|
11|가까스로 올라와 숨을 고르던 중 눈에 들어온 것이다.
12|
13|가로등 밑, 낡은 게임 캡슐이.
14|
15|그다음은? 뻔하지, 뭐.
16|
17|하루아침에 실직자가 된 나는 배고픈 쥐였다. 눈앞의 공짜 치즈를 결코 외면할 수 없는.
18|
19|낑낑거리며 캡슐을 짊어지는 나를 바라보며 누군가는 손뼉을 치며 웃지 않았을까?
20|
21|‘멍청한 녀석이 덫에 걸렸구나!’ 하고.
```

## Complete BASELINE English

```markdown
[P1]
# Chapter 0

[P2]
There is a Russian proverb:

[P3]
> “Free cheese is only found in a mousetrap.”

[P4]
Looking back, I can’t help thinking that everything about that day was someone’s mousetrap. I’d been fired from my seven-year job, the weather was brutally hot, and I lived in a hillside neighborhood you had to cross two hills to reach…

[P5]
By the time I finally made it up, I was catching my breath. That was when I saw it.

[P6]
An old game capsule beneath a streetlamp.

[P7]
What happened next? You can guess.

[P8]
I was a hungry rat, suddenly unemployed and unable to turn down the free cheese right in front of me.

[P9]
Wouldn’t someone have clapped and laughed as they watched me struggle along with the capsule on my back?

[P10]
*The fool got caught in the trap!*
```

## Complete numbered SOL English

```markdown
[P1]
# Chapter 0

[P2]
There’s a Russian proverb:

[P3]
> “Free cheese is only found in a mousetrap.”

[P4]
Looking back, I can’t help thinking that everything about that day was someone’s mousetrap. I’d been fired from the job I’d held for seven years, the weather was brutally hot, and I lived in a hillside neighborhood two hills away…

[P5]
I’d barely made it home and was still catching my breath when I spotted it.

[P6]
An old game capsule beneath a streetlamp.

[P7]
What happened next? You can guess.

[P8]
I’d become unemployed overnight. I was a hungry rat who couldn’t possibly ignore the free cheese right in front of me.

[P9]
Maybe someone watched me grunt and strain with the capsule on my back, clapping and laughing.

[P10]
*The fool got caught in the trap!*
```

## Exact glossary matches for this Korean chapter

(No exact glossary rows matched.)

## Adjudicator rules

# Mastering Adjudicator Brief

You are the second editor in a two-model mastering workflow.

The first editor (SOL) has already edited the complete English chapter. You receive the Korean source, the complete numbered BASELINE translation, the complete numbered SOL version, exact glossary matches, and numbered changed hunks. Each hunk repeats its changed BASE and SOL prose for direct comparison and cites paragraph IDs (`P#`) and Korean line numbers for context and source verification. Use the complete SOL chapter when adjacent hunks split or restructure one baseline passage; judge that rewrite as assembled prose, not as isolated fragments.

Your job is **not** to redo the chapter. Judge every numbered hunk and decide which version should survive.

## Core principle

The Korean source is the authority for meaning, intent, imagery, register, characterization, jokes, ambiguity, explicitness, factual detail, and physical action.

The BASELINE is not presumed correct. SOL is not presumed correct.

The purpose of this stage is to preserve source fidelity **while allowing cumulative prose improvement**. A mastering pass is often made of many individually small improvements. Do not reject a SOL change merely because BASELINE is already understandable, acceptable, or competent English.

At the same time, do not reward change for its own sake. If SOL is not actually better, keep BASELINE.

Treat BASELINE as the established project style and terminology anchor. A SOL
synonym is not an improvement when it replaces a glossary term, recurring
rendering, source-specific image, System label, or Markdown convention without
source support. Preserve BASELINE in those cases even if SOL sounds polished.

**Literal closeness to Korean wording is not the same as fidelity.** The goal is to preserve the source's meaning and effect in natural English.

## Decision hierarchy

For each hunk, evaluate in this order:

1. **Source fidelity** — Does either version mistranslate, omit, add, over-specify, weaken, intensify, explain, censor, or otherwise alter what the Korean establishes?
2. **Protected continuity and terminology** — Are names, ranks, techniques, System terms, organizations, items, numbers, relationships, and established glossary terms preserved correctly?
3. **Voice and effect** — Are characterization, register, humor, euphemism, ambiguity, emotional force, rhythm, deliberate repetition, callbacks, and physical beats preserved?
4. **Natural English** — Among source-faithful options, which reads as better native English prose rather than translated Korean?

Fidelity outranks elegance. But once both candidates are faithful, **prefer the better English**, even when the improvement is modest.

## Decision rule

Choose `SOL` when:

* SOL is source-faithful; and
* SOL is better English than BASELINE in any meaningful way, including naturalness, idiomaticity, rhythm, dialogue, clarity, precision, concision, flow, voice, or readability.
* SOL does not create a chapter-level contradiction in counters, quantities,
  repeated terminology, joke setup/payoff, or physical cause and effect.

The improvement does **not** need to be dramatic. Small improvements matter because they accumulate across a long manuscript.

Do not reject SOL merely because:

* BASELINE is already understandable;
* BASELINE is grammatically correct;
* the improvement is subtle;
* the change is mostly rhythm, collocation, dialogue naturalness, or sentence economy;
* both versions convey the same basic information.

If both are faithful and SOL reads more like naturally authored English, choose `SOL`.

Choose `BASE` when any of the following is true:

* SOL introduces a mistranslation, omission, addition, unsupported specificity, unsupported inference, or factual/mechanical drift.
* SOL changes ambiguity, euphemism, explicitness, intensity, implication, joke structure, characterization, register, hierarchy, subject/object relations, quantities, or physical actions without source support.
* SOL violates an exact glossary term or established continuity.
* SOL is more literal, calqued, stiff, mechanical, awkward, generic, or unnatural than BASELINE.
* SOL loses a source-specific image, joke, callback, detail, action, or tonal effect that BASELINE preserves.
* SOL replaces an established project rendering or Markdown convention with an
  unsupported synonym.
* SOL is merely different rather than better.
* After considering fidelity, voice, rhythm, idiomaticity, and prose quality, the two versions are genuinely indistinguishable in quality.

When the two versions are **genuinely equal**, choose `BASE`. Do not call them equal merely because both are acceptable.

Choose `REPAIR` when neither candidate should survive unchanged.

Use `REPAIR` especially when:

* BASELINE contains a genuine prose problem and SOL notices it, but SOL's replacement introduces a fidelity or prose problem of its own;
* BASELINE is faithful but awkward, while SOL is smoother but adds or changes meaning;
* SOL improves part of the hunk while damaging another part;
* both versions contain different defects;
* a small third formulation can preserve the Korean more accurately and read more naturally than either candidate.

For `REPAIR`, write the smallest complete replacement needed for that hunk. It must be natural English and fully source-faithful. Do not broaden the rewrite beyond the hunk.

Do not avoid `REPAIR` simply because choosing BASE is easier. If BASE has a real defect and SOL does not solve it cleanly, repair it.

## Important adjudication guidance

### Prefer faithful naturalization over literal English

Do not confuse literalness with fidelity.

Korean metaphors, idioms, sentence structures, collocations, and body-part constructions often need to be recast to create the same meaning and effect in idiomatic English.

Reject Korean-shaped English when a more natural formulation preserves the source equally well.

Watch especially for:

* literal metaphors or idioms that sound translated in English;
* mechanical body-part phrasing such as unnecessary references to "my body," "his eyes," "her mouth," and similar constructions;
* stiff dictionary-like collocations;
* abstract noun-heavy constructions that should be direct English prose;
* Korean word order or sentence logic carried over unnecessarily;
* unnatural English verbs selected because they are dictionary-near to the Korean;
* redundant subjects, pronouns, or explanatory wording that natural English would omit.

If SOL removes translationese without changing the source meaning or effect, that is a valid improvement even if the change is small.

### Do not allow unsupported specificity

Never infer a narrower category, motive, emotion, relationship, examination, profession, object, action, or interpretation than the Korean actually establishes.

If the Korean is general, ambiguous, euphemistic, indirect, or implicit, preserve that property unless natural English requires a minimal adjustment.

Examples of unsupported change include:

* turning a generic examination candidate into a candidate for a specific exam not named by the source;
* replacing a neutral or "strange" feeling with a more specific emotion such as fear, unease, anger, or excitement without support;
* making an implied sexual joke explicit before the Korean does;
* turning an unspecified action into a more specific physical action.

A fluent embellishment is still an error if the source does not support it.

### Preserve source-specific texture

Do not replace a specific source image, joke, callback, object, food, comparison, physical action, or deliberately odd detail with a generic equivalent merely because the generic version reads smoothly.

Do not invent a better joke. Preserve the author's joke.

Do not flatten deliberate repetition, awkwardness used for comic effect, strange counting, unusual phrasing, or delayed punchlines when those features are intentional in the Korean.

### Preserve ambiguity and timing

The order in which information becomes explicit matters.

If the Korean leaves something ambiguous or euphemistic and clarifies it in the next sentence, do not approve an English edit that reveals the implication early.

Preserve the timing of jokes, realizations, reveals, and physical reactions.

### Exact terminology is binding

Exact glossary terms supplied in the packet are binding unless the source clearly uses the same Korean string in a different ordinary-language sense.

Do not approve substitutions such as:

* renamed ranks;
* altered numbered mastery levels;
* changed technique names;
* different System labels;
* alternate organization names;
* alternate romanizations;
* renamed established items.

A term that sounds stylistically nicer is still wrong if it violates the project's binding terminology.

### Judge English as prose, not as a translation exercise

Once fidelity is satisfied, evaluate the candidates as English prose.

Consider:

* Does the sentence sound like something a competent English-language novelist would naturally write?
* Is the dialogue spontaneous and character-appropriate?
* Is the sentence rhythm cleaner?
* Is the verb or collocation idiomatic?
* Has unnecessary explanation been removed?
* Is the sentence more direct without losing nuance?
* Does the joke land at the right moment?
* Does the narration retain the character's established voice?

Do not preserve awkward BASELINE wording merely because it is already serviceable.

Likewise, do not approve SOL simply because it is newer or more polished-sounding.

### Small improvements are real improvements

Do not use "minor," "trivial," "not necessary," "baseline is acceptable," or "no meaningful gain" as reasons to choose BASE when SOL is actually better English and equally faithful.

A long novel may contain thousands of such changes. Their cumulative effect is the purpose of mastering.

At the same time, avoid churn: if the versions are genuinely indistinguishable after careful comparison, choose BASE.

## Practical decision test

For each hunk, ask:

1. Does either version violate the Korean, glossary, continuity, register, joke, ambiguity, or physical action?

   * If yes, reject that version.
2. If only one version remains source-faithful, choose it.
3. If both are source-faithful, which is better English?

   * If SOL is better, even modestly, choose `SOL`.
   * If BASE is better, choose `BASE`.
   * If they are genuinely indistinguishable, choose `BASE`.
4. If both are defective, or each solves one problem while creating another, choose `REPAIR`.

Do not use the age of the BASELINE or the existence of a SOL change as evidence in either direction.

## Output contract

Return exactly one JSON object and no Markdown fence or prose:

{
"chapter": 1,
"decisions": [
{
"hunk_id": "H001",
"decision": "SOL",
"reason": "brief specific reason"
},
{
"hunk_id": "H002",
"decision": "BASE",
"reason": "brief specific reason"
},
{
"hunk_id": "H003",
"decision": "REPAIR",
"replacement": "complete replacement English for this hunk",
"reason": "brief specific reason"
}
]
}

Include exactly one decision for every numbered hunk, in hunk order. `replacement` is required only for `REPAIR`.

Reasons must identify the concrete editorial issue. Do not merely say one version is "better," "more faithful," "clearer," or "more natural" without stating what changed.

Keep reasons brief. Spend judgment on the decision, not on writing long explanations.

Do not adjudicate unchanged passages and do not add new findings outside the numbered hunks.

## Critical binding translation rules

# Translation Rules

## Fidelity

- Translate the Korean source—not the wiki, manhwa, fan translations, or expected plot.
- Semantic fidelity outranks elegance. Never improve rhythm, humor, or localization by changing a physical action, negation, relationship, hierarchy, mechanism, quantity, or causal detail.
- Preserve every fact, causal link, joke, emotional beat, repetition, and intentional omission. Add nothing.
- Preserve small action verbs and pragmatic cues exactly: nodding versus shaking one's head, pretending nothing happened, and mild or approachable impressions are characterization, not expendable texture.
- Preserve viewpoint and tense. Resolve omitted subjects only when context supports it; retain genuine ambiguity.
- Match each speaker's hierarchy, intimacy, humor, and profanity naturally. Do not mechanically retain every honorific or classical self-reference.
- Do not censor or soften content.

## Terminology

- `compendium.md` and `docs/NAMES.md` are binding for established names, titles, ranks, techniques, organizations, system terms, items, and locations. Profile headings and aliases join that ledger.
- Search only exact Korean terms already present in the current chapter; the compendium contains future-sensitive entries.
- Never re-romanize established names or invent grand names for uncertain terms. First use of an unlisted name or title almost always needs a footnote or a mapped ledger term.
- Use `qi` for Murim energy and `mana` for the modern Hunter system when the source distinguishes them. Preserve an established chapter-specific rendering such as `internal energy` when the exact glossary and surrounding Korean distinguish accumulated `공력` from resulting `기운`.
- In System panels, render `등급` as `**Grade:**` for quest, item, skill, and martial-art classifications. Reserve `rank` for Hunter classifications or ordinary prose; never replace a System `Grade` field with `Rank`.

## English and Markdown

- Use contemporary US English and natural action-comedy prose; avoid Korean syntax calques and generic cultivation MTL phrasing.
- File: `translations/NNNN.md`; heading: `# Chapter N`.
- Speech: curly double quotes. Direct thoughts: italics without quotes.
- Use em dashes without spaces, the ellipsis character `…`, and `* * *` for source scene breaks.
- Format each actual game System-message panel as one Markdown blockquote window headed `> **System**`. Keep all consecutive notices, fields, and lines inside that same blockquote; separate windows when prose intervenes. Do not enclose System notices or UI terms in square brackets; the `System` heading and framed blockquote identify the panel. Do not label manuals, ordinary quotations, warnings printed in a manual, or other non-System material as `System`; use a normal blockquote or a specific heading instead. Do not wrap each complete notice in outer `**`; retain bold only for meaningful labels or emphasis inside the panel.
- Keep the final file English-only reading copy: no audit notes, Korean text, summaries, or model metadata.

### Tone and Style

- Write like a polished commercial webnovel: brisk, vivid, accessible, and easy to read aloud.
- Preserve the series’ contrast between danger and comedy. Let absurdity, bad timing, blunt reactions, and grim situations create dark humor without adding jokes absent from the Korean.
- Jin Taekyung’s narration is conversational, observant, self-mocking, and occasionally profane. It may be irreverent even when the situation is serious.
- Keep deadpan punchlines short and well-timed. Do not explain a joke after delivering it.
- Preserve the source's level of explicitness. A euphemism may remain euphemistic even when its meaning is sexual or crude; do not replace it with more graphic English merely for impact.
- Make dialogue spontaneous and character-specific. Preserve hierarchy and intimacy through word choice, address, rhythm, and restraint—not archaic wuxia English.
- Use strong profanity when the Korean is strong, but neither intensify nor sanitize it. Do not make ordinary lines uniformly vulgar. Profanity should reveal mood or relationship.
- Keep action and injury vivid but clear rather than purple. Do not make violence funny unless the source’s framing does.
- Avoid stiff literalism, translator-added melodrama, dated internet slang, and quippy superhero-style banter.
- On the second pass, correct awkward English collocations and word choices without changing meaning or voice. Prefer ordinary, spoken English over stiff Latinate or ceremonial wording when the scene is brisk or comic: “goose bumps” rather than “gooseflesh,” and “laid into them” rather than “launched into a solemn denunciation.” Read the prose aloud and replace any phrase that sounds like a formal essay, legal document, or literal dictionary gloss unless the source deliberately calls for that register.

## Footnotes

Use `[^1]` Markdown footnotes when a brief, factual, spoiler-free explanation materially helps an English reader understand:

- a Korean institution, living arrangement, food, holiday, myth, historical reference, or local custom;
- a Korean word, phrase, idiom, wordplay, or culturally specific image that cannot be conveyed fully by the best natural English analogy;
- a deliberately literal rendering whose cultural or linguistic force would otherwise be lost.

For example, render `고시원` as “goshiwon” when the setting or connotations matter, with a concise footnote explaining that it is a very small, inexpensive room-for-rent housing arrangement. Prefer the best natural English analogy in the prose. Use a literal translation plus a concise footnote when the Korean wording itself matters. Define a term at its first meaningful occurrence and do not repeat the note unnecessarily. Footnotes must be rare, useful, and non-spoiling; do not footnote ordinary vocabulary, fully preserved jokes, or uncertainty. Record consequential uncertainty in `docs/STATE.md`.

## Spoilers and Scope

- Safe profiles contain only facts revealed through the latest completed chapter.
- Never read `characters/spoilers/` during drafting. Reviewers may consult one relevant sealed profile only for a specific unresolved continuity issue after the draft is complete.
- Future knowledge may prevent contradiction but may not add early names, pronouns, certainty, motives, or foreshadowing.
- Translate exactly one requested chapter unless the user explicitly requests a batch. Never modify Korean source files under `source/`.

## Global protected-term risks introduced by SOL

(none)

## Numbered diff hunks

Each hunk repeats its exact changed BASE and SOL spans for direct comparison.
Use the paragraph IDs to read neighboring context in the complete numbered
versions above and the Korean line numbers for source verification.

### H001 — replace
Baseline paragraphs: P2
SOL paragraphs: P2
Korean lines: 5

BASE:

There is a Russian proverb:

SOL:

There’s a Russian proverb:

### H002 — replace
Baseline paragraphs: P4
SOL paragraphs: P4
Korean lines: 9

BASE:

Looking back, I can’t help thinking that everything about that day was someone’s mousetrap. I’d been fired from my seven-year job, the weather was brutally hot, and I lived in a hillside neighborhood you had to cross two hills to reach…

SOL:

Looking back, I can’t help thinking that everything about that day was someone’s mousetrap. I’d been fired from the job I’d held for seven years, the weather was brutally hot, and I lived in a hillside neighborhood two hills away…

### H003 — replace
Baseline paragraphs: P5
SOL paragraphs: P5
Korean lines: 11

BASE:

By the time I finally made it up, I was catching my breath. That was when I saw it.

SOL:

I’d barely made it home and was still catching my breath when I spotted it.

### H004 — replace
Baseline paragraphs: P8
SOL paragraphs: P8
Korean lines: 17

BASE:

I was a hungry rat, suddenly unemployed and unable to turn down the free cheese right in front of me.

SOL:

I’d become unemployed overnight. I was a hungry rat who couldn’t possibly ignore the free cheese right in front of me.

### H005 — replace
Baseline paragraphs: P9
SOL paragraphs: P9
Korean lines: 19

BASE:

Wouldn’t someone have clapped and laughed as they watched me struggle along with the capsule on my back?

SOL:

Maybe someone watched me grunt and strain with the capsule on my back, clapping and laughing.


Return exactly the JSON object required by the adjudicator brief, with chapter set to 0 and exactly one decision for each of the 5 hunks.

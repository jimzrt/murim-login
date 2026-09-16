# Master Edit Task — Chapter 116

# Master Editorial Brief

You are the final English-language editor of an existing Korean-to-English novel translation.

The Korean source is the authority for meaning. The existing English is the baseline you are editing, not a draft to discard. Your task is to make the chapter read like professionally written native English commercial fiction while preserving the author's exact story, characterization, humor, register, pacing, ambiguity, and cultural texture.

## Editorial authority

You may freely recast sentences and paragraphs when the English is stiff, literal, repetitive for accidental reasons, awkwardly collocated, over-explained, or syntactically shaped by Korean. You may tighten dialogue, improve rhythm, repair transitions, and make action easier to follow. A technically correct sentence may still need rewriting if a fluent English novelist would not naturally phrase it that way.

Do not change text merely to make it different. If the baseline is already strong, leave it alone.

The accepted baseline is also the project's style and terminology anchor. Do not
replace an established rendering, cultural term, System label, Markdown form, or
recurring phrase with a synonym merely because the synonym sounds smoother.
Make that change only when the Korean source, `RULES.md`, or the exact glossary
requires it. In particular, do not turn a source-specific image into a nearby
English image, or change a gold-spoon joke, item name, technique name, or UI
label into a different expression without source support.

## Fidelity constraints

Never invent, omit, explain away, generalize, intensify, soften, or reinterpret source-supported content. In particular, preserve:

- exact actions, subjects, objects, directionality, causality, quantities, and physical details;
- deliberate ambiguity, euphemism, implication, profanity level, repetition, and withheld information;
- jokes and comic specificity, even when a more generic English joke would sound smoother;
- hierarchy, kinship, forms of address, characterization, and speaker attitude;
- System mechanics, Murim concepts, names, ranks, techniques, items, organizations, and established terminology.
- chapter-level logical consistency: interpret labels, counters, notifications, and repeated facts from how they behave across the scene, not from an isolated surface gloss;
- idioms by their narrative function rather than their component words, and jokes with their setup, recognition, and punchline timing intact;
- cross-sentence implications: do not create a claim that contradicts “again,” an increasing value, an earlier action, or the explanation immediately around it;
- repeated terminology and formatting: once the baseline or glossary establishes a rendering, keep it consistent throughout the chapter unless the source clearly changes the sense;

Do not add jokes, metaphors, explanations, emotional conclusions, or colorful details that are absent from the Korean. Do not replace a specific source image with a generic equivalent merely because the generic version is smoother.

When natural English and literal form conflict, preserve the source meaning and pragmatic effect while changing the English form as much as necessary.

Before returning the chapter, perform a silent continuity pass: trace every
counter, quantity, repeated System label, item or technique name, joke setup and
payoff, and physical cause-and-effect sequence from the Korean through the
finished English. Correct any local sentence that contradicts the sequence.

## Relationship to project files

`RULES.md` is binding. `POLISH.md` describes known translation-English failure modes and should guide the edit. Exact glossary matches are binding unless the packet explicitly marks them otherwise. Character/continuity material is context only and must never override the chapter's Korean source.

## Output

Return only the complete edited English Markdown chapter. Preserve the required chapter heading and project Markdown conventions. Do not provide commentary, a change log, explanations, or a Markdown code fence.

## Binding project rules

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

## Project polish guidance

# Polish Brief — Murim Login

## Goal
Make the English natural and fluent without changing meaning, pacing, humor, character voice, System terminology, or Korean/Murim cultural content.

**Core rule:** Translate the thought, not the Korean sentence structure. If meaning, idiom, or cultural context is unclear, always check the original Korean source before editing.

## Priorities
1. Rewrite literal or calqued English, awkward collocations, and cumbersome sentence structures.
2. Normalize tense and aspect; prefer natural English information order.
3. Replace mechanical body-part descriptions with character-centered actions where appropriate.
4. Preserve repetition when it serves comedy, panic, emphasis, pacing, or characterization.
5. Keep Taekyung’s voice contemporary, casual, blunt, sarcastic, gamer-aware, and syntactically simple.
6. Standardize System terminology, capitalization, hyphenation, names, and romanization.

## Typical repairs
Recast the whole phrase rather than editing word by word:

- “True to my words, he hadn’t looked inside.” → “Just as I’d said, he hadn’t even looked inside.”
- “The pronunciation was perfectly Korean.” → “She was speaking perfect Korean.”
- “I scanned the Status Window with a hawk’s eye.” → “I scrutinized the Status Window.”
- “The joy I’d felt that day threw me into confusion now.” → “Remembering how happy I’d been that day only made me more confused.”
- “Wolhwa held out her hands. Both spotless hands held a bowl…” → “Wolhwa held out a bowl of water in both hands.”
- “This character is totally born with a silver spoon…” → “This guy really was born with a silver spoon…”
- “Jinho pronounced it with the solemnity of a judge.” → “Jinho delivered the verdict with the solemnity of a judge.”
- “The most common among them is the weak monster even an F-rank Hunter like me can handle: the goblin.” → “The weakest and most common of them were goblins—even an F-rank Hunter like me could handle one.”
- “For a moment, silence flowed between us as we stared at each other.” → “For a moment, we stared at each other in silence.”
- “I thrust out my fist on reflex, forcing the words through my clenched voice.” → “I lashed out on reflex, forcing the words through clenched teeth.”
- “You could say they’re a deeply rooted old tree.” → “You could say they’re one of the region’s old, deeply rooted powers.”
- “I blinked. It felt like I’d been hit in the back of the head.” → “I blinked. I felt completely blindsided.”
- “But there were no take-backs. I’d just have to spit and move on.” → “But there were no take-backs. I’d just have to suck it up and move on.”
- “This time, a different kind of ecstasy swept over me than when I’d used the Status Window. Maybe it was pain.” → “This time, what swept through me was nothing like the exhilaration I’d felt from the Status Window. If anything, it was pain.”

Watch for abstractions or body parts acting unnaturally: “X feeling came over my body,” “X thought entered my mind,” “my eyes stopped at X,” and “X emotion threw me into Y.”

## Idioms and cultural phrasing
Translate idioms by function, but verify the Korean source before changing meaning. If “put up a whole building” means wealth or ownership, use “buy a whole building”; if the Korean literally means construction, retain that meaning. Keep useful terms such as **goshiwon**, **doenjang**, and **jeonse**, and naturalize the surrounding English.

## System style
Use formal capitalization in System/UI text and normal English in prose.

- UI occupation: `Third Rate Martial Artist`
- Prose: `third-rate martial artist`
- Interfaces: `Status Window`, `Skill Window`
- System classification field: `**Grade:**`; use `rank` only for Hunter classifications or ordinary prose.
- Formal UI values use title case (`Third Rate Martial Artist`); ordinary prose uses lowercase hyphenated forms (`a third-rate martial artist`).
- Preserve exact objective/completion terminology across a quest. In this arc, use `Check and Distribute Skill Window Points` in both places; use `Redistribute` only when previously assigned points are actually being reallocated.
- Use the established terminology sheet; resolve inconsistencies according to the Korean source.
- Use one consistent romanization style, including tone marks in Chinese pinyin (`Tài lěng le`, `Zhōngguó rén ma?`). Check the original before changing an unmarked form: `Shenme` remains unmarked here because the spelling supports Taekyung’s “Ms. Sunmi” mishearing joke.
- For Murim metaphors and idioms, check the Korean before rewriting. Preserve the image when it carries meaning, but render its function in natural English; do not retain calques such as “silence flowed” or “spit and move on” without a source-based reason.

## Passes
1. Native-English pass: remove calques, awkward structure, collocations, and tense problems.
2. Voice pass: preserve casual, blunt character voice and spoken dialogue.
3. Terminology pass: standardize System terms, ranks, capitalization, names, and romanization.
4. Source-check pass: verify idioms, jokes, metaphors, and cultural details against the original Korean.

**Final test:** Would a native English writer naturally phrase this sentence this way in context, while preserving what the Korean says?

## Output contract
Return only the complete English Markdown reading copy. The first nonblank line
must be `# Chapter N`. Do not prefix a status sentence, tool note, or thinking.

## Exact glossary matches for this Korean chapter

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 무신     | **Martial God**               | —              |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 정파     | **orthodox faction**                             |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈십이검 | **Crimson Blood Twelve Swords** | Peak-level martial arts manual discovered by Pung Yang. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 청강검 | **blue-steel sword** | Cheongpung's sword. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 이소월 | young_martial_artist_to_allied_sect_leader | Young Lady Lee | formal-polite | Taekyung uses 이 소저 while greeting Seowol at the banquet. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 110–114

## Plot

Cheol Mubaek, the Peak-level Tiger of Mount Heng, stops the Mount Heng Sword Sect’s elders from abandoning Lee Cheonbaek’s final wishes and forces them to recognize Lee Seowol as their Sect Leader. Seowol refuses to flee despite the sect’s overwhelming disadvantage, preparing a desperate defense with oil hidden throughout the estate while awaiting Jin Taekyung and Jin Mukyung.

Pung Yang leads more than two hundred Red Wind Band mounted bandits in surrounding Mount Heng. He offers Seowol a choice between total destruction and marriage, intending to preserve the sect’s useful forces under his control. Cheol kills the envoy, prompting the assault. The sect’s defenses initially repel the attackers, and Seowol’s concealed fire attack burns many mounted bandits, but the gate and walls eventually fall. Cheol holds the breached gate alone until Pung Yang confronts him.

Pung Yang swallows an unidentified red pill from a hard wooden case and gains enough power to defeat the mature Peak master Cheol, breaking all four of his limbs and severely injuring him. The surviving defenders retreat to a watchtower, where Seowol continues fighting until exhausted and signals Cheol with a fire arrow. Pung Yang reaches her and renews his demand that she marry him.

Taekyung, Mukyung, Mujin, and Wolhwa arrive at the fortress after a forced ride under Taekyung’s time-limited Peak Quest. Cheol recognizes Taekyung’s Taiyuan Jin Family affiliation, leaving the Jin party as the Mount Heng Sword Sect’s only immediate hope.

## Continuity

- Taekyung, Mukyung, Mujin, and Wolhwa have reached the Mount Heng Sword Sect after racing against the Quest’s irreversible twenty-two-hour deadline.
- Taekyung is Level 55; Mujin is Level 38.
- The Red Wind Band began the assault with more than two hundred mounted bandits, suffered at least one hundred casualties in the fire attack and initial fighting, and still retains more than one hundred fifty when Pung Yang enters personally.
- Pung Yang is an early Peak master whose saber and throwing-knife techniques are highly developed; the red pill temporarily raises his power far beyond Cheol Mubaek’s.
- Pung Yang possesses an unidentified hard wooden case containing the red pill and possibly a weapon or other anti-tiger object.
- Cheol Mubaek is alive but has four broken limbs and severe internal injuries. He refuses to surrender the single-successor Shura Annihilating Fist, though he fears for Lee Seowol’s safety.
- The Mount Heng fortress wall has been overrun. Lee Seowol and the remaining defenders are surrounded at the watchtower, while Pung Yang demands her marriage.
- Lee Seowol remains Sect Leader by choice and has not accepted Pung Yang’s demand.
- The Mount Heng Sword Sect’s survival, Seowol’s response, and Taekyung’s ability to rescue her and Cheol remain unresolved.
- The nature and origin of Pung Yang’s red pill remain unknown.
- The Peak Quest’s required invitation to the Jin Family for the coming Lunar New Year remains the governing objective.

## Translation Decisions

- Retain **Peak**, **early Peak**, **First Rate**, **shichen**, **Red Wind Band**, **mounted bandits**, **Sect Leader**, **Young Lady**, and **Taiyuan Jin Family**.
- Render **수라멸권** as **Shura Annihilating Fist**.
- Render **항산권문** as **Mount Heng Fist Sect**; retain **Mount Heng Sword Sect** where that established sect name is used.
- Render **화시** as **fire arrow**, **쇠뇌** as **crossbow**, **충차** as **battering ram**, and **벽곡단** as **fasting pills**.
- Render **멸문지화** as **total destruction**, **혼인 예물** as **wedding gift**, and **동귀어진** as **perishing together**.

### Prior accepted reading-copy tails

#### Chapter 114 tail (verified mastered)

…
every direction. Eyes gleaming with killing intent and desire shone between the torches held by the advancing enemies. “You damned bastards dare…” “I’ll tear every last one of you apart and throw the pieces to the dogs.” The killing intent of the mounted bandits surrounding the watchtower in a circle stabbed at their skin. Just as everyone was falling into despair, Lee Seowol suddenly drew her bowstring toward the sky. Whoooosh. Trailing a tail of flame, a single fire arrow descended toward the gate shrouded in darkness. It was a light meant to find one person. *Uncle Cheol.* The Tiger of Mount Heng, Cheol Mubaek. He was the Mount Heng Sword Sect’s final hope. That was when a man walked out beneath the light revealed by the fire arrow. Clomp. Clomp. “I suppose it’s a little late to say this now…” Lee Seowol had heard that voice only once, but she could never forget it, not even in her dreams. Unable to bring herself to look at him, she closed her eyes. Pung Yang beamed at her. “You’ll have to marry me.” * * * The hunter Cheol Mubaek had become the Tiger of Mount Heng because of a fortuitous encounter. While tracking a wolf on a mountainside in the vast Mount Heng range, he fell into a hidden cave between the cliffs. There, he discovered a martial arts manual and an elixir left behind by a reclusive master. *I’m going back. I’m going back alive, no matter what!* Cheol Mubaek learned martial arts to survive. When the fasting pills in the hidden cave ran out, he tore up grass growing between the cliffs or caught bats to eat as he trained. After no less than three years, he climbed the cliff with his bare hands and returned to the village. What awaited him was his home in ruins—and the deaths of his wife and child. *Had it been two months or so since we last heard from you? That bastard Hwang, who’d always had his eye on your wife…* By the time Cheol Mubaek came to his senses, he had already beaten the village’s great landowner and all his servants to death. After avenging his family, Cheol Mubaek returned to the hidden cave and resumed his martial arts training. It was a whip he used against himself, and atonement for his family. How much time had passed like that? Before he knew it, Cheol Mubaek was being called the Tiger of Mount Heng. But… “Huff. Even a tiger would cry.” Cheol Mubaek panted harshly. His once-brilliant eyes were clouded as if by dark clouds, and his beard was drenched in blood. *I have to hurry. I have to stop that bastard…* But all he had left was his will. With all four limbs broken, his body had already slipped beyond his control. He had displayed martial arts worthy of the title Tiger of Mount Heng, yet he still could not defeat Pung Yang. *How in the world did that bastard…?* The result seemed obvious. Pung Yang had only just entered the Peak realm, barely capable of creating blade qi, while Cheol Mubaek was a Peak master who had reached a mature realm stage. Pung Yang had been as precarious as a candle in the wind. Then he had suddenly changed after pulling an unidentified wooden case from inside his robes. *The red pill. Yes, that was definitely it.* Cheol Mubaek had made a mistake by retreating because he thought it might be a hidden weapon. After Pung Yang gulped down the pill, he was no longer the mere leader of a mounted-bandit group Cheol Mubaek had known. *How can a human being become that strong?* Cheol Mubaek’s eyes trembled as he recalled Pung Yang’s movements. The gap between them was so vast that it seemed impossible to win, even if they fought ten or a hundred more times. Pung Yang had overturned the battle in an instant, broken all four of Cheol Mubaek’s limbs, inflicted massive internal injuries, and then left. *I’ll let you live for now. I’ve decided I want the formula for your martial art as a wedding gift.* Cheol Mubaek’s eyes reddened as he recalled Pung Yang’s parting words. The Shura Annihilating Fist was a martial art passed down to a single successor and never taught to outsiders. He would choose suicide rather than hand it over to Pung Yang, but Lee Seowol—whom he cherished like a daughter and a granddaughter—troubled him. *What on earth am I supposed to do?* Cheol Mubaek was staring at the sky with a heavy heart when it happened. Thud-thud-thud-thud! The sound of hooves in the distance drew closer and closer before stopping abruptly at his feet. Beneath the brilliantly shining moon, four pairs of eyes looked down at him. “Doesn’t the Red Wind Band have a retirement age? Why is an old geezer still out here playing bandit?” “Young Master Jin, that’s Great Hero Cheol Mubaek, the Tiger of Mount Heng.” “Gah! I’m sorry. Hey, Mujin. Hurry up and apologize. What are you waiting for?” “You’re the one who made the mistake, Captain. Why should I…?” Smack! “Grandpa—no, Sir. Are you all right?” Instead of answering, Cheol Mubaek stared intently at the young man’s chest. A single character was embroidered on his navy martial robe. 進. “Taiyuan… the Jin Family?” “Oh, you recognize it?” The young man, Jin Taekyung, grinned.

#### Chapter 115 tail (verified mastered)

…
the Blood Wolf Sword’s secret martial art and the Tiger of Mount Heng’s martial arts formula would be enough. Ah, I should take that old man Cheol with me on the way back, too.” “…Uncle Cheol is still alive?” “Of course. How could I kill a Benefactor who’s going to hand over such a precious martial arts formula?” “…” “I’ll stake my life on this promise. It’s not too late even now, so marry me. If you do, I’ll let everyone live. I’ll stop at destroying their dantians.” That was the decisive blow. Lee Seowol’s eyelashes trembled for a while before she slowly lowered her hand. “Keep your promise.” “A wise choice.” A triumphant smile spread across Pung Yang’s face. As of today, he would begin his third life. He had gone from a beggar boy to a mounted bandit. Now he would finally don the mask of the orthodox faction and become the true master of the Mount Heng Sword Sect. Though there had been heavy losses, it didn’t matter. New wine belonged in new wineskins. Under the name of the Mount Heng Sword Sect, he would recruit martial artists and expand his power. *If the Blood Wolf Sword could do it thirty years ago, why can’t I?* Just as the corners of his mouth lifted with overflowing delight— “Pung Yang!” A shout infused with internal energy shook heaven and earth. Lee Seowol, Pung Yang, and every survivor turned their heads as if on cue. A young man dressed in robes as black as night was walking toward them from some fifty *jang* away.[^1] *A master.* The young man’s needle-sharp gaze sent a chill through a corner of Pung Yang’s chest. He was a master. More than that, he was a Peak master in no way inferior to Pung Yang himself. Pung Yang could tell just from the way the young man’s hand moved as it gripped his sword hilt. *There are only two Peak masters this young in Shanxi Province. And if he’s a swordsman…* The answer came immediately. Jin Mukyung, the Heaven Shaking Sword. A genius who had reached the Peak realm at barely twenty years of age. More importantly, behind him stood the Jin Family of Taiyuan, which had risen to become the foremost family in Shanxi. *At least he came alone.* But the next moment, another person cautiously stuck his head out through the fortress gate Jin Mukyung had entered. The young man wore a navy martial robe. His clothing, the dark iron spear in his hand, and above all, his nearly identical face told Pung Yang who he was. “The Sleeping Dragon of Shanxi?” Jin Taekyung flinched at the nickname someone blurted out and muttered, “Fuck. I knew this would happen.” Cursing crudely in a manner unbecoming a scion of a prestigious family, Jin Taekyung came sauntering forward beside the leisurely Jin Mukyung. The two brothers were heading straight toward Pung Yang. *The Taiyuan Jin Family, at a time like this… This is very bad.* The reputation the family had built over many years, combined with the fame it had earned in the battle at Eight Spring Gorge, had left the Jin Family’s current standing unrivaled. As a result, countless young people across Shanxi Province who dreamed of becoming martial artists were flocking to the Jin Family. That was why, even if Pung Yang swallowed the Mount Heng Sword Sect right now, he would still have to bow flat and hide his claws. *Once I get past this hurdle, my opportunity will come.* The Mount Heng Sword Sect had already collapsed. The Murim was a world where the strong preyed on the weak, and Pung Yang was a new power in that world. Even if his opponent was the Taiyuan Jin Family, he believed he had earned the right to be treated with respect. Clomp. Clomp. Clomp. With every step Jin Mukyung and Jin Taekyung took, the Red Wind Band’s mounted bandits scattered out of their way. When the brothers reached him, Pung Yang clasped his hands in salute. “I am Pung Yang, Red Wind Band Leader.” Had Pung Yang not been a seasoned martial artist who never let down his guard—had the effects of the Temporary Strength Pill not still lingered faintly—he would never have evaded that strike. Shiiiiing! He hurriedly twisted aside. A dazzling streak of Sword Energy skimmed past his neck and sliced through three mounted bandits behind him. “Is this the will of the Taiyuan Jin Family?” Jin Taekyung, who had already felled the nearby mounted bandits, muttered, “I’d rather talk it out.” “You fucking bast—” Before Pung Yang could finish speaking, another streak of Sword Energy flew in and grazed his back. Pain seared through him like fire. He barely evaded the attacks that followed and revised his assessment of Jin Mukyung. *He’s stronger than me.* At this level, Jin Mukyung’s movements were comparable to Cheol Mubaek’s. On top of that, Jin Taekyung was slaughtering Pung Yang’s subordinates. Pung Yang realized he had only one option left. *The Temporary Strength Pill.* While his subordinates died one after another trying to stop Jin Mukyung, Pung Yang pulled the wooden case hidden inside his robes and tipped the pill into his mouth. Shiiiiing! Jin Mukyung’s blue Sword Energy was reflected in Pung Yang’s eyes, which had turned blood-red. Slice! [^1]: A *jang* is a traditional unit of distance, roughly three meters.

## Korean source

```text
＃116화



진무경의 검기가 풍양의 등을 가른 순간, 나는 생각했다.

‘이 싸움, 이겼어.’

절정 고수들의 생사결은 어떻게 될지 짐작하기 어렵다.

그러나 아직 절정에 이르지 못한 내가 보기에도 진무경과 풍양의 격차는 확실했다.

‘진무경이 강한 건지, 아니면 풍양이 생각했던 것보다 약했던 건지.’

앞서 항산호 철무백과의 싸움에서 힘을 전부 소진했던 걸까?

중요한 건 진무경이 압도적인 우세를 점하고 있다는 사실이다.

서걱, 촤아악!

“으아악!”

수하들을 방패 삼아 뒤로 몸을 빼는 풍양, 거침없이 베어 나가며 추격하는 진무경. 푸른 검기를 피해 적풍단의 마적들이 사방으로 흩어지자 홀로 남은 풍양의 모습이 드러났다.

‘끝났다.’

내심 주먹을 불끈 움켜쥔 그때였다. 놈의 손에 들려 있는 붉은 단환이 눈에 들어온 것은.

‘잠깐, 붉은 단환?’

철무백이 말했던 바로 그것이다. 머릿속 경고등이 울림과 동시에 풍양이 단환을 한입에 털어 넣었다.

그 틈을 놓치지 않고 진무경의 푸른 검기가 놈의 정수리를 향해 내리꽂혔다.

쉬이이잉! 서걱!

허공에 흩뿌려지는 핏물, 깊게 베인 어깨.

비틀거리며 물러나는 한 사람은 다름 아닌…… 진무경이다.

나는 눈을 깜빡거렸다.

‘방금 도대체…….’

무슨 일이 일어난 거지?

내 의문에 시스템이 응답했다.

띠링.



- 돌발 퀘스트가 생성되었습니다.



퀘스트



[잠력단]

현재 적풍단주 풍양은 잠력단(暫力丹)을 복용하여 비정상적인 힘을 얻은 상태입니다. 그를 쓰러트리고 항산검문을 구원하십시오.

* 이소월의 사망 시 퀘스트는 실패합니다!



등급 : 초절정

제한 : 진태경

임무 : [Lv.??? 풍양]을 저지, 혹은 승리 (미완료)

보상 : ???

실패 : ???





자그마치 초절정 등급의 퀘스트. 내용을 빠르게 훑어보니 저놈이 강해진 이유를 알 수 있었다.

“잠력단? 이거 설마.”

나는 입을 딱 벌리고 풍양을 바라봤다.

놈은 처음과 많이 달라진 모습이었다. 온통 핏빛으로 물든 눈동자. 소매 아래로 드러난 피부엔 핏줄이 불뚝 섰고 근육은 터질 것 같다. 거기에 다가가기도 두려울 만큼 막대한 기파까지.

‘빼박이네.’

아니, 시바…….

절정 고수라는 새끼가 치사하게 도핑을 해?



* * *



“크흐흐흐.”

풍양은 낮은 웃음을 흘렸다.

전신에서 용솟음치는 힘과 활력! 머리는 그 어느 때보다 뜨겁게 달아올랐고 시야에 들어오는 모든 것들이 나약하고 하찮게 느껴졌다.

거기에 더해 단전에서 끓어오르는 공력까지.

‘이것이 잠력단의 힘이다.’

일시적으로 갖고 있는 힘을 두 배, 아니 그 이상으로 끌어내는 미지의 단환. 누가, 어떻게 만들었는지는 풍양 자신도 모른다. 그건 말 그대로 하늘이 내린 기연이었으니까.

‘적혈십이검(赤血十二劍). 적혈심법(赤血心法). 그리고 잠력단 다섯 알이 담긴 목곽 하나.’

광활한 고원에 숨겨진 수많은 무덤 중 하나. 그곳에서 누가 남겼는지 모를 절정 비급과 잠력단을 발견한 순간, 풍양은 기연을 만났음을 깨달았다.

이런 보물은 아무와도 나눌 수 없다는 사실도.

‘그 시절로 열 번을 돌아간다 해도 같은 선택을 했겠지.’

수하들을 죽이고 기연을 독차지한 풍양은 아무도 찾지 않는 비처에서 수련을 시작했다. 그리고 불과 이 년 만에 절정의 경지에 올랐다.

비상식적인 성장 속도와 불쑥불쑥 솟구치는 살기에 사마외도(邪魔外道)의 무공을 익혔다는 걸 깨달았지만 그에게는 아무런 상관도 없었다.

‘이곳은 무림이다!’

힘이 곧 법칙인 세상에서 정, 사, 마를 논하는 것이 우스웠다. 고원으로 돌아온 풍양은 금방 두각을 드러내기 시작했다.

다른 마적들과는 확연히 다른 비상한 두뇌와 뛰어난 무공.

폭력과 보상을 적절히 이용하는 용인술로 빠른 속도로 수하들을 휘어잡았다. 물론 그에게도 위기가 없었던 것은 아니다.

그러나 풍양에게는 아무에게도 보여 주지 않은 귀물이 있었다.

‘그때 처음 잠력단의 효능을 알았지.’

일당백? 고작 그 정도가 아니다.

잠력단을 복용한 그는 고원에서 그 누구도 당해 낼 자가 없는 무적의 고수였다.

새로운 경쟁자를 제거하려던 대형 마적단 두 곳이 하루아침에 궤멸당했다. 풍양이 이끄는 적풍단이 그 자리를 차지한 것은 자연스러운 수순이었다.

‘하지만 딱 거기까지.’

사마외도의 무공은 속성으로 빠르게 익히는 것이 가능한 대신 깊이가 얕았다. 그 단점을 정종 무공으로 보완하려던 찰나 눈에 띈 곳이 바로 태원진가와 항산검문이다.

용과 호랑이의 싸움. 풍양은 누가 쓰러지든 상관없었다.

처음에는 이천백에게 태원진가의 무공을 약속받고 고용됐는데…… 일이 꼬여 지금에까지 왔다.

‘처음 항산검문을 쳤을 때 잠력단을 썼어야 했는데.’

항산검문은 언제든지 다시 쳐 굴복시킬 수 있지만 잠력단은 다시 구할 수 없다.

차라리 그때 잠력단을 복용했다면 이미 항산검문의 주인이 되어 있었을지도 모를 일이다.

“뭐, 이것도 나쁘지는 않구나. 태원진가와 항산검문의 무공을 모두 얻게 되었으니 말이다.”

어깨의 혈도를 짚어 상처를 지혈한 진무경이 입을 열었다.

“처음부터 그게 목적이었나? 난 또 웬 마적 놈 하나가 정파 대협 흉내가 내고 싶어서 안달이 난 줄 알았지.”

“대협? 오늘 진천검과 산서잠룡을 잡아 죽이면 마두 정도는 되겠지. 으하하하!”

“네깟 놈이 마두는 무슨. 그리고 그럴 일은 없으니까 걱정 마라.”

“철무백은 사지를 부러트려 놨지. 네놈은 말하는 본새가 글러 먹었으니 팔다리 두 개는 잘라야겠다.”

“아, 그래? 이건 내 아우가 자주 하는 말인데…….”

진무경이 가래를 탁 뱉었다.

“좆이나 까 잡숴.”

쉭!

이가 숭숭 나간 청강검은 볼품없어 보였지만 푸른 검기가 덧씌워지니 천하제일의 명검으로 돌변했다.

쐐애애애액! 쉬쉬쉬슁!

빗발치는 검기가 사방을 가르고 베었다. 끔찍한 비명이 여기저기서 터져 나왔지만 진무경은 검을 멈추지 않았다.

미처 피하지 못하고 휘말린 마적들의 비명일 뿐, 그가 원하는 목소리의 주인은 손쉽게 검을 피해 내고 있었기 때문이다.

“역시 진천검, 검 끝이 제법 날카롭군.”

진무경은 번개 같은 속도로 풍양의 허리를 베어 갔다.

쩡! 검기에 휩싸인 진무경의 검과 풍양의 곡도가 격돌하자 굉음이 터져 나왔다.

“사술 따위로 강해진 놈한테 들으니 기분이 더러운데.”

“중요한 사실은 강해졌다는 거지. 그 대단하다는 항산호가 나한테 몇 초나 버텼을 것 같나?”

“몰라.”

쉬이익!

이번에는 안면이다. 팔, 가슴, 배, 옆구리, 다리를 향해 쏟아지던 검격이 돌연 위로 쭉 솟구쳤다.

순간 황급히 고개를 뺀 풍양의 뺨 위로 검날이 아슬아슬하게 비껴갔다.

치이익.

그러나 예리한 풍압마저 피할 수는 없었다. 바람이 할퀴고 간 뺨에서 핏물이 뚝뚝 떨어졌다.

말없이 물러난 풍양이 상처를 확인하고 이를 갈았다.

“……이 어린놈이.”

진무경은 살기 어린 목소리에도 담담하게 입을 열었다.

“그래서?”

“뭐?”

“그래서 철 대협이 너한테 몇 초를 버텼나?”

진무경을 뚫어져라 노려보던 풍양이 대답했다.

“백 초.”

“나는 어떨까?”

“이백 초. 그 안에 끝내 주마.”

“그럴 능력은 되고?”

“사지를 자르기 전에 혀부터 뽑아야겠군. 아까부터 듣고 있자니 기분이 더러워.”

“내 아우와 싸우지 않은 걸 고맙게 여겨라. 저놈이 네 상대였으면 넌 이미 귀 막고 자결했어. 사람 놀리는 데는 도가 튼 놈이거든.”

“산서잠룡이? 그럼 저놈도 같이 뽑아야겠군.”

“……음. 그건 살짝 괜찮은 것 같기도 하고.”

“헛소리 그만하고 검을 들어라. 그래야 촌각이라도 더 발버둥 치다가 뒈지지.”

풍양의 붉은 눈동자가 요사스럽게 반짝인 순간, 늘어트린 곡도에서 막대한 공력이 솟구쳤다.

화아아악!

공력을 어떠한 매개체에 불어넣어 유형화시킬 수 있는 것을 검기(劍氣)라 한다. 그러나 잠력단을 복용한 풍양은 지금 이 순간, 그 경지를 뛰어넘었다.

“검강(劍罡)…….”

초절정 고수. 이른바 무신이라 불리는 자들의 상징.

비록 깨달음이 받쳐 주지 못한 탓에 진정한 검강이라 부를 수는 없지만, 그가 절정의 극에 다다랐다는 것은 분명했다.

“거참.”

진무경은 헛웃음을 흘렸다. 과연 풍양이 수련만으로 저 경지에 다다르려면 몇 년이 필요했을까. 십 년? 이십 년?

하지만 조그마한 붉은 단환 하나가 풍양으로 하여금 그 세월을 건너뛰게 만들었다. 무리(武理)에 대한 고민, 끊임없는 수련과 피땀. 그 모든 것을 뛰어넘도록.

“어떤 개 같은 놈이 저딴 걸 만들어서…….”

츠츠츠츠.

진무경의 검에서도 검기가 솟아올랐다. 풍양이 가소롭다는 듯이 말했다.

“이백 초를 버티면 살려 주마.”

“응, 좆 까.”

후우우웅!

천지를 가를 듯이 내리꽂히는 검강을 바라보며, 진무경은 문득, 자신이 건방진 막내아우를 닮아 간다는 생각이 들었다.

‘그런데 이놈은 뭐 하느라 이렇게 안 와?’

콰과과광!



* * *



구구구궁.

지진이라도 난 것처럼 지면이 흔들렸다. 삼십 장 밖에서 도대체 무슨 싸움을 하는 건지 몰라도 하나는 알겠다.

‘가면 안 돼.’

농담이 아니라 저 싸움에 끼었다가는 죽을 것 같다.

절정 고수 싸움에 일류 등 터지는 꼴을 직접 겪고 싶진 않거든. 그리고 무엇보다…….

쉭, 서걱!

“꺼어어어.”

이쪽도 충분히 힘들다. 이 정도면 일당백은 아니어도 일당칠십 정도는 되겠지. 나는 쏟아지는 핏물을 뒤집어쓴 채로 미친 듯이 무기를 휘둘렀다.

슈왁!

옆구리를 노리고 찔러 들어오려는 기병창을 붙잡고 그대로 당겼다. 등 뒤에서 도를 내리찍던 놈의 배에 박아 넣고 창대를 수도(手刀)로 내리친다.

우지직!

“허억!”

“다음부턴 철창 써. 무겁고 튼튼한 걸로. 스쿼트도 할 수 있고 얼마나 좋냐.”

덕담과 함께 마적의 턱을 후려갈겼다. 턱뼈가 으스러지는 소리와 함께 놈의 몸에서 힘이 빠져나간다.

쐐애액!

‘목, 옆구리, 다리.’

세 방향에서 내질러지는 단검은 눈으로 보지 않아도 읽을 수 있었다.

어떻게 이렇게 하나같이 느리고 뻔한지. 그리고 이 짧은 순간에 대응을 생각하고 실행에 옮길 수 있는 내 자신이 새삼 놀랍다.

타탁. 콰직!

인벤토리에 무기를 넣어 자유로워진 손으로 목과 옆구리를 찔러 오는 녀석들의 손목을 잡는 동시에 부러트리고 뒷발을 쭉 뻗었다.

짤막한 비명과 둔탁한 타격감은 적에게 정확히 명중했다는 증거다.

‘더, 더, 더.’

점점 더 손이 빨라지고 소리가 멀어진다. 나를 가득 둘러싼 적들의 몸을 스칠 때마다 인벤토리에서 불러들인 무기들이 나타났다가 사라진다. 찍고, 베고, 휘두르고. 부쉈다.

몇 명이나 쓰러트렸을까? 어느 한순간, 멀리 밀려나 있던 소음이 한 번에 찾아왔다.

털썩.

“끄으윽.”

“커헉.”

죽은 자들은 차가운 흙바닥에 얼굴을 처박은 채 미동이 없고, 살아남은 자들은 뒹굴며 신음한다. 죽지도, 다치지도 않은 이십여 명의 마적들은 나를 피해 뒷걸음질 쳤다.

“사, 산서잠룡…….”

한 걸음, 두 걸음.

겁에 질린 그들은 내가 다가선 만큼 물러났다. 아직 뒤에 성난 적들이 남아 있다는 사실을 잊은 채로.

쐐애애액! 퍼걱!

“죽여! 마적 놈들을 모조리 죽여라!”

“이 개새끼들!”

최후까지 살아남아 항전하던 항산검문의 무인들이다.

눈이 벌겋게 충혈되어 달려드는 그들의 기습에 마적들이 도미노처럼 쓰러졌다.

“크아아악!”

“제, 제발 살려……!”

온 사방이 온통 시체와 핏물, 신음으로 넘쳐흘렀다.

오늘 이곳에서 죽은 마적들이 몇 명이나 될까? 이백? 삼백? 모르겠다.

내가 아는 건, 한 사람이 죽기 전까지 이 전투는 끝나지 않을 거라는 사실이다.

‘풍양.’

저 치사한 약쟁이 놈을 처리해야 할 시간이다.

“…….”

할 수 있겠지? 할 수 있을 거야. 아마도…….
```

## Current accepted English baseline

```markdown
# Chapter 116

The moment Jin Mukyung’s Sword Energy split Pung Yang’s back, I thought,

*This fight is won.*

It was hard to predict the outcome of a life-and-death duel between Peak masters.

But even to me, someone who had yet to reach the Peak realm, the difference between Jin Mukyung and Pung Yang was obvious.

*Is Jin Mukyung really that strong, or was Pung Yang weaker than I thought?*

Had he exhausted all his strength in his earlier fight with Cheol Mubaek, the Tiger of Mount Heng?

What mattered was the fact that Jin Mukyung held an overwhelming advantage.

Slice! Shraaak!

“Gaaaaah!”

Pung Yang retreated, using his subordinates as shields, while Jin Mukyung pursued him without hesitation, cutting his way through them. As the mounted bandits of the Red Wind Band scattered in all directions to avoid the blue Sword Energy, Pung Yang was revealed standing alone.

*It’s over.*

That was when I clenched my fist in triumph.

Then I saw the red pill in his hand.

*Wait. A red pill?*

It was the very thing Cheol Mubaek had mentioned. At the same moment the warning bells began ringing in my head, Pung Yang tossed the pill into his mouth.

Jin Mukyung didn’t miss the opening. His blue Sword Energy plunged toward the crown of Pung Yang’s head.

Shiiiiing! Slice!

Blood sprayed through the air. One shoulder was cut deeply.

The person staggering backward was none other than Jin Mukyung.

I blinked.

*What the hell just…*

What had happened?

The System answered my question.

> **System**
>
> A sudden Quest has been generated.
>
> **Quest**
>
> **Temporary Strength Pill**
>
> Red Wind Band Leader Pung Yang has taken a Temporary Strength Pill (暫力丹) and is currently empowered by abnormal strength. Defeat him and save the Mount Heng Sword Sect.
>
> *The Quest will fail if Lee Seowol dies!*
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Task:** Stop or defeat **Lv.??? Pung Yang** (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???

A Quest with a Grade of Supreme Peak.

I skimmed through the details and immediately understood why that bastard had grown so strong.

“Temporary Strength Pill? Don’t tell me…”

I gaped at Pung Yang.

He looked completely different from before. His eyes had turned completely bloodred. Veins bulged beneath the skin exposed below his sleeves, and his muscles looked ready to burst. On top of that, the sheer force radiating from him made it frightening to even approach.

*There’s no mistaking it.*

No, fuck…

A fucking Peak master, cheating by doping?

* * *

“Heh-heh-heh.”

Pung Yang let out a low laugh.

Power and vitality surged throughout his body. His head burned hotter than ever, and everything in his field of vision seemed weak and insignificant.

The internal energy boiling in his dantian only added to the sensation.

*So this is the power of the Temporary Strength Pill.*

It was an unknown red pill capable of drawing out twice the strength a person currently possessed—no, even more than that—for a limited time. Pung Yang himself didn’t know who had made it or how.

It was, quite literally, a fortuitous encounter bestowed by the heavens.

*The Crimson Blood Twelve Swords. The Crimson Blood Cultivation Technique. And a wooden case containing five Temporary Strength Pills.*

Among the countless tombs hidden on the vast plateau, Pung Yang had discovered a Peak-level martial arts manual and the Temporary Strength Pills in one of them. The moment he found the Peak-level manual and Temporary Strength Pills left behind by an unknown person, he realized he had encountered a great opportunity.

He also realized that such treasures could not be shared with anyone.

*Even if I went back to that time ten times, I would have made the same choice.*

Pung Yang killed his subordinates and kept the fortuitous encounter for himself, then began training in a hidden refuge that no one ever visited. In only two years, he reached the Peak realm.

The absurd speed of his growth and the killing intent that surged from him at unpredictable moments made him realize he had learned demonic, heterodox arts.

But it didn’t matter to him.

*This is the Murim!*

In a world where strength was the law, arguing over whether something was orthodox, heterodox, or demonic was laughable. After returning to the plateau, Pung Yang quickly began to distinguish himself.

His intelligence was far beyond that of the other mounted bandits, and his martial arts were exceptional.

By using violence and rewards in just the right measure, he quickly bent his subordinates to his will. Of course, he had faced crises as well.

But Pung Yang possessed a wondrous treasure he had never shown to anyone.

*That was when I first learned what the Temporary Strength Pill could do.*

One against a hundred? It was far beyond that.

After taking a Temporary Strength Pill, he became an invincible master whom no one on the plateau could withstand.

Two major mounted-bandit groups that had tried to eliminate their new competitor were wiped out overnight. It was only natural that the Red Wind Band, led by Pung Yang, would take their place.

*But that was as far as I could go.*

Demonic, heterodox arts could be learned quickly through shortcuts, but they lacked depth. Just as Pung Yang was trying to make up for that weakness with orthodox martial arts, two places caught his eye: the Jin Family of Taiyuan and the Mount Heng Sword Sect.

A battle between a dragon and a tiger.

Pung Yang didn’t care which one fell.

At first, Lee Cheonbaek had hired him with the Jin Family of Taiyuan’s martial arts promised as payment…

But things had become complicated, leading him to this point.

*I should have used a Temporary Strength Pill when I first attacked the Mount Heng Sword Sect.*

He could attack the Mount Heng Sword Sect again and force it to submit whenever he wanted.

But he could never obtain another Temporary Strength Pill.

If he had taken one back then, he might already have become the master of the Mount Heng Sword Sect.

“Well, this isn’t bad either. I’ll obtain the martial arts of both the Jin Family of Taiyuan and the Mount Heng Sword Sect.”

Jin Mukyung, who had pressed an acupoint on his shoulder to staunch the bleeding, spoke.

“Was that your goal from the beginning? I thought some mounted-bandit bastard was desperate to play at being a Great Hero of the orthodox faction.”

“A Great Hero? If I kill the Heaven Shaking Sword and the Sleeping Dragon of Shanxi today, I might at least become a demon lord. Wahaha!”

“You? A demon lord? Don’t make me laugh. And you don’t have to worry about that happening.”

“I broke all four of Cheol Mubaek’s limbs. Your way of speaking is beyond saving, so I’ll have to cut off two of yours.”

“Oh, really? This is something my younger brother says often…”

Jin Mukyung spat out a wad of phlegm.

“Go fuck yourself.”

Whoosh!

The blue-steel sword was missing so many pieces from its edge that it looked pathetic. But once blue Sword Energy coated it, it transformed into the finest sword in the world.

Shraaaaak! Shishishiiing!

Sword Energy rained down, cutting through everything around them. Horrible screams erupted from all directions, but Jin Mukyung did not stop swinging his sword.

They were merely the screams of mounted bandits who had been caught in the attack after failing to evade it. The person whose voice Jin Mukyung actually wanted to hear was easily avoiding his sword.

“As expected of the Heaven Shaking Sword. The edge of your sword is fairly sharp.”

Jin Mukyung moved with lightning speed and slashed toward Pung Yang’s waist.

Clang!

When Jin Mukyung’s Sword Energy-wreathed blade collided with Pung Yang’s curved saber, a thunderous boom rang out.

“It’s disgusting hearing that from someone who grew stronger through sorcery.”

“The important thing is that I grew stronger. How many moves do you think that supposedly incredible Tiger of Mount Heng lasted against me?”

“I don’t know.”

Whoosh!

This time, the attack came for his face. Sword strikes poured toward his arms, chest, stomach, side, and legs before suddenly shooting straight upward.

Pung Yang hurriedly pulled his head back. The blade skimmed past his cheek by the narrowest margin.

Sizzle.

But he couldn’t avoid even the sharp pressure of the wind. Blood dripped from the cheek the wind had raked.

Pung Yang retreated without a word, checked the wound, and ground his teeth.

“…You little brat.”

Despite the murderous voice, Jin Mukyung calmly opened his mouth.

“So?”

“What?”

“So how many seconds did Sir Cheol last against you?”

Pung Yang glared at Jin Mukyung for a long moment before answering.

“A hundred moves.”

“What about me?”

“Two hundred moves. I’ll finish you before then.”

“Do you have what it takes?”

“Before cutting off your limbs, I should pull out your tongue first. Listening to you has been pissing me off for a while now.”

“Be grateful you didn’t have to fight my younger brother. If he were your opponent, you’d have already plugged your ears and killed yourself. He’s an expert at making fun of people.”

“The Sleeping Dragon of Shanxi? Then I suppose I should pull his tongue out too.”

“…That actually sounds kind of appealing.”

“Enough nonsense. Raise your sword. That way, you can struggle for even a moment longer before you die.”

The moment Pung Yang’s red eyes gleamed with an eerie light, immense internal energy surged from his lowered saber.

Fwoooosh!

When internal energy was infused into a medium and given tangible form, it was called Sword Energy.

But after taking the Temporary Strength Pill, Pung Yang had now surpassed that realm.

“Sword Force…”

A Supreme Peak master.

It was the symbol of those known as Martial Gods.

Though his enlightenment was insufficient for it to be called true Sword Force, there was no doubt that he had reached the absolute pinnacle of the Peak realm.

“Well, damn.”

Jin Mukyung let out a hollow laugh.

How many years would Pung Yang have needed to reach that realm through training alone? Ten years? Twenty?

But a tiny red pill had allowed him to leap over all those years—the contemplation of martial principles, the endless training, the blood and sweat.

It had let him surpass all of it.

“What kind of son of a bitch made something like that…”

Tsssss.

Sword Energy rose from Jin Mukyung’s sword as well. Pung Yang spoke with open contempt.

“Last two hundred moves, and I’ll let you live.”

“Yeah, go fuck yourself.”

Fwoooosh!

As he watched the Sword Force plunge down as though it meant to split heaven and earth, Jin Mukyung suddenly thought that he was beginning to resemble his insolent youngest brother.

*But what is that guy doing, taking so long to get here?*

KABOOOOM!

* * *

Rumble, rumble, rumble.

The ground shook as though an earthquake had struck.

I had no idea what kind of battle was taking place thirty jang away, but I knew one thing.

*I can’t go over there.*

I wasn’t joking. If I got caught up in that fight, I felt like I would die.

I had no desire to personally experience what happened when a First Rate got its back broken between Peak masters. And more importantly…

Whoosh! Slice!

“Gueeegh.”

This side was hard enough already.

At this point, I might not be a match for a hundred men, but I had to be good for at least seventy.

I swung my weapon like a madman, drenched in the blood pouring down around me.

Shwaaak!

I caught the cavalry spear thrusting toward my side and pulled it toward me. I drove it into the stomach of the man who had been bringing his saber down behind me, then chopped the shaft with the edge of my hand.

Crack!

“Gasp!”

“Use an iron spear next time. Something heavy and sturdy. You can even do squats with it. How great is that?”

Along with the friendly advice, I slammed my fist into the mounted bandit’s jaw. His body went limp as his jawbone shattered.

Shraaaaak!

*Throat, side, leg.*

I could read the daggers thrusting toward me from three directions without even looking at them.

How could every one of them be so slow and predictable?

I was also genuinely amazed by myself. In that brief moment, I could think of a response and put it into action.

Tap. Crack!

I put my weapon into my Inventory, freeing one hand. As I simultaneously caught the wrists of the men stabbing toward my throat and side and broke them, I kicked backward with my leg fully extended.

Their short screams and the dull impact were proof that I had struck them exactly where I intended.

*More. More. More.*

My hands gradually grew faster, and the sounds around me grew more distant.

Every time I brushed against the bodies of the enemies surrounding me, weapons summoned from my Inventory appeared and vanished.

Stabbed, slashed, swung.

Broke.

How many had I brought down?

At some point, the noise that had been pushed far away came rushing back all at once.

Thud.

“Ggh…”

“Urgh.”

The dead lay motionless with their faces buried in the cold dirt. The survivors rolled around, groaning. The twenty or so mounted bandits who had escaped death and injury took several steps backward to get away from me.

“T-the Sleeping Dragon of Shanxi…”

One step. Two steps.

Terrified, they retreated as I advanced, forgetting that furious enemies were still behind them.

Shraaaaak! Thud!

“Kill them! Kill every last mounted bandit!”

“You fucking bastards!”

They were martial artists of the Mount Heng Sword Sect who had survived and fought to the bitter end.

Caught by the bloodshot-eyed men’s surprise attack, the mounted bandits fell like dominoes.

“Kyaaaagh!”

“P-please, spare me…!”

Everywhere I looked, the ground overflowed with corpses, blood, and groans.

How many mounted bandits had died here today? Two hundred? Three hundred?

I didn’t know.

What I did know was that this battle would not end until one person died.

*Pung Yang.*

It was time to deal with that cheating, pill-popping bastard.

“…”

*I can do this, right? I should be able to. Probably…*
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 116`.

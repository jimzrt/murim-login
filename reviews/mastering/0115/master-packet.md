# Master Edit Task — Chapter 115

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
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 정파     | **orthodox faction**                             |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 팔천협    | **Eight Spring Gorge** |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 이소월 | young_martial_artist_to_allied_sect_leader | Young Lady Lee | formal-polite | Taekyung uses 이 소저 while greeting Seowol at the banquet. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 호승심 | polysemy | Competitive pride or fighting spirit; not merely a desire to test oneself. | test myself |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |

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

#### Chapter 113 tail (verified mastered)

…
erupted atop the walls. Screams and blood burst forth. “Ha ha! Kill them all!” “Don’t let them climb up!” Lee Seowol watched it all from the highest watchtower. Her lips trembled, and the color had drained from her face. *So this is the Murim.* The screams of the dying. The desperate struggles of those who wanted to live. The world of the strong preying on the weak that she had finally encountered was more brutal and frightening than she had imagined. But… *I can’t retreat.* Countless people had already died. Those who were going to leave had left, while those who remained were fighting with their lives on the line. Lee Seowol was now the Sect Leader who had to lead them, and she was bound to share her fate with the Mount Heng Sword Sect. “Sect Leader! The walls are in danger! We need to send reinforcements!” “They’re breaking down the gate with a battering ram!” “Sect Leader! You must do something!” “Sect Leader!” As urgent reports rained down from every direction, Lee Seowol spoke. “When I give the signal, fire one fire arrow toward the walls and two toward the gate. And, Uncle Cheol.” Cheol Mubaek, who had been standing guard beside her, answered. “Tell me what you need.” “The gate will be breached soon. Can you buy us a little time?” “By myself?” “I can only apologize for making such a difficult request.” “One against a hundred. I’ve always wanted to try that.” “The uncle I know is a master who can face ten thousand men. Still, please be careful.” “All right. Do you really think those bastards could get the better of me?” Cheol Mubaek laughed heartily and leaped down. With the Tiger of Mount Heng—a consummate Peak master—guarding the gate, no one would get through unless Pung Yang himself stepped forward. *More. Just a little longer.* Lee Seowol gazed down at the fierce battle before suddenly shouting like a thunderclap. “Now!” The two martial artists who had been waiting for her command each drew their bowstrings. The next moment, the fire arrows soared into the darkening winter sky and shone brightly above everyone’s heads. * * * The fire arrows falling like meteors were clearly visible even to Pung Yang, more than a hundred *jang* away. He muttered to himself. *So they had a move hidden up their sleeve.* It didn’t take long for his guess to become certainty. A moment later, enormous flames erupted around the walls. Fwoosh! Fwoooosh! “Aaargh!” Burning alive was one of the most painful ways to die. The mounted bandits of the Red Wind Band, massed beneath the walls like a swarm of ants, writhed and screamed horribly. The ropes attached to the grappling hooks snapped, and the wooden ladders were engulfed in flames. “Attack!” “Kill every last one of those mounted-bandit bastards!” Those waiting below to climb and those still climbing burned to death, while those who had already reached the top were stabbed and slashed by weapons converging from every direction. “So they did make some preparations…” As Pung Yang stared impassively at the battlefield, a mounted bandit returned, his body blackened in patches like charcoal. “What happened?” “L-Leader. Our losses are too great!” The moment he reached Pung Yang, the mounted bandit threw himself flat on the ground and continued breathlessly. “From the first assault until now, at least a hundred men must have died. More importantly, after that fire attack, our brothers’ morale is…” “The gate?” “Pardon?” “What happened to the gate?” “We broke through, but the Tiger of Mount Heng, Cheol Mubaek, is holding it alone…” “Alone?” “Yes. His martial arts are so formidable that no one dares step forward.” “Then that’s enough.” As he spoke, Pung Yang held out his hand. The mounted bandit instinctively reached to take it, only for his body to tilt and collapse. A dagger was buried deep between his brows, his expression frozen in confusion. “How many troops do we have left?” The subordinate who served as Pung Yang’s right hand was accustomed to such sights. He glanced at the corpse and answered. “By a rough count, a little over a hundred and fifty but not quite two hundred. It’s true that our losses are heavier.” “How much worse do you think theirs are? The men on those walls are the Mount Heng Sword Sect’s final bulwark.” “You mean those few men are all they have left?” “Yes.” “It isn’t that I doubt you, Leader, but what if they have another trap like that fire attack…?” “That’s what they’re counting on.” Pung Yang let out a derisive laugh. He didn’t know whose strategy it had been, but they had played it quite cleverly. *If I had been less experienced, I would have suspected another trap and pulled our forces back.* *They’re struggling to buy time. Are they waiting for someone’s support?* If so, there was even less reason to hesitate. The few could not stand against the many. Even after suffering considerable losses, the Red Wind Band would have no trouble wiping out the Mount Heng Sword Sect. And besides… “I’m going myself.” “You’re going yourself, Leader?” “Yes. We have a tiger to catch, don’t we?” Pung Yang burst into a hearty laugh and felt inside his robes out of habit. A hard wooden case rested there. Inside was something that could bring down a tiger in one go.

#### Chapter 114 tail (verified mastered)

…
every direction. Eyes gleaming with killing intent and desire shone between the torches held by the advancing enemies. “You damned bastards dare…” “I’ll tear every last one of you apart and throw the pieces to the dogs.” The killing intent of the mounted bandits surrounding the watchtower in a circle stabbed at their skin. Just as everyone was falling into despair, Lee Seowol suddenly drew her bowstring toward the sky. Whoooosh. Trailing a tail of flame, a single fire arrow descended toward the gate shrouded in darkness. It was a light meant to find one person. *Uncle Cheol.* The Tiger of Mount Heng, Cheol Mubaek. He was the Mount Heng Sword Sect’s final hope. That was when a man walked out beneath the light revealed by the fire arrow. Clomp. Clomp. “I suppose it’s a little late to say this now…” Lee Seowol had heard that voice only once, but she could never forget it, not even in her dreams. Unable to bring herself to look at him, she closed her eyes. Pung Yang beamed at her. “You’ll have to marry me.” * * * The hunter Cheol Mubaek had become the Tiger of Mount Heng because of a fortuitous encounter. While tracking a wolf on a mountainside in the vast Mount Heng range, he fell into a hidden cave between the cliffs. There, he discovered a martial arts manual and an elixir left behind by a reclusive master. *I’m going back. I’m going back alive, no matter what!* Cheol Mubaek learned martial arts to survive. When the fasting pills in the hidden cave ran out, he tore up grass growing between the cliffs or caught bats to eat as he trained. After no less than three years, he climbed the cliff with his bare hands and returned to the village. What awaited him was his home in ruins—and the deaths of his wife and child. *Had it been two months or so since we last heard from you? That bastard Hwang, who’d always had his eye on your wife…* By the time Cheol Mubaek came to his senses, he had already beaten the village’s great landowner and all his servants to death. After avenging his family, Cheol Mubaek returned to the hidden cave and resumed his martial arts training. It was a whip he used against himself, and atonement for his family. How much time had passed like that? Before he knew it, Cheol Mubaek was being called the Tiger of Mount Heng. But… “Huff. Even a tiger would cry.” Cheol Mubaek panted harshly. His once-brilliant eyes were clouded as if by dark clouds, and his beard was drenched in blood. *I have to hurry. I have to stop that bastard…* But all he had left was his will. With all four limbs broken, his body had already slipped beyond his control. He had displayed martial arts worthy of the title Tiger of Mount Heng, yet he still could not defeat Pung Yang. *How in the world did that bastard…?* The result seemed obvious. Pung Yang had only just entered the Peak realm, barely capable of creating blade qi, while Cheol Mubaek was a Peak master who had reached a mature realm stage. Pung Yang had been as precarious as a candle in the wind. Then he had suddenly changed after pulling an unidentified wooden case from inside his robes. *The red pill. Yes, that was definitely it.* Cheol Mubaek had made a mistake by retreating because he thought it might be a hidden weapon. After Pung Yang gulped down the pill, he was no longer the mere leader of a mounted-bandit group Cheol Mubaek had known. *How can a human being become that strong?* Cheol Mubaek’s eyes trembled as he recalled Pung Yang’s movements. The gap between them was so vast that it seemed impossible to win, even if they fought ten or a hundred more times. Pung Yang had overturned the battle in an instant, broken all four of Cheol Mubaek’s limbs, inflicted massive internal injuries, and then left. *I’ll let you live for now. I’ve decided I want the formula for your martial art as a wedding gift.* Cheol Mubaek’s eyes reddened as he recalled Pung Yang’s parting words. The Shura Annihilating Fist was a martial art passed down to a single successor and never taught to outsiders. He would choose suicide rather than hand it over to Pung Yang, but Lee Seowol—whom he cherished like a daughter and a granddaughter—troubled him. *What on earth am I supposed to do?* Cheol Mubaek was staring at the sky with a heavy heart when it happened. Thud-thud-thud-thud! The sound of hooves in the distance drew closer and closer before stopping abruptly at his feet. Beneath the brilliantly shining moon, four pairs of eyes looked down at him. “Doesn’t the Red Wind Band have a retirement age? Why is an old geezer still out here playing bandit?” “Young Master Jin, that’s Great Hero Cheol Mubaek, the Tiger of Mount Heng.” “Gah! I’m sorry. Hey, Mujin. Hurry up and apologize. What are you waiting for?” “You’re the one who made the mistake, Captain. Why should I…?” Smack! “Grandpa—no, Sir. Are you all right?” Instead of answering, Cheol Mubaek stared intently at the young man’s chest. A single character was embroidered on his navy martial robe. 進. “Taiyuan… the Jin Family?” “Oh, you recognize it?” The young man, Jin Taekyung, grinned.

## Korean source

```text
＃115화



항산호 철무백.

이미 몇 번 들어 본 이름이다. 월화는 그가 없었다면 항산검문은 진작 적풍단에게 멸문당했을 거라고 했다.



‘혈랑검 이천백과 비견되거나 그 이상이라고 평가받는 절정 고수예요.’



분명히 그랬었는데.

‘그 대단한 절정 고수가 왜 이 꼴이 되어 있나.’

기이한 방향으로 꺾여 있는 사지, 상의를 흠뻑 적신 검은 핏물은 심각한 내상의 증거다. 철무백이 흐릿한 눈빛으로 우리를 바라보았다.

“태원……진가?”

“어, 알아보시네?”

나는 억지로 입꼬리를 끌어 올렸다. 위중한 상태인 철무백을 조금이라도 안심시키기 위해서다.

지금 내 눈앞에 있는 그는 쟁쟁한 위명의 절정 고수가 아닌, 마지막 희망을 발견한 노인에 지나지 않았다.

“적풍단, 안에, 소월이가 위험…….”

힘겹게 이어 가는 철무백의 말을 듣지 않았어도 이 자리의 모두는 사태의 심각성을 알고 있다. 시선이 닿는 곳마다 시체와 핏물이 넘쳐 났으니까.

‘하지만 아직 늦지는 않았어.’



제한 시간 : 00:05:12



아슬아슬하게 시간을 맞췄다. 문제는 항산호 철무백을 이 꼴로 만들어 놓은 놈이 저 안에 있다는 사실이지.

월화도 나와 같은 생각을 한 모양이다. 그녀가 철무백을 진정시키며 물었다.

“철 대협, 풍양이 다른 고수와 합공을 했나요?”

철무백이 미약하게 고개를 저었다.

“풍양이 단신으로 철 대협을 꺾었다는 말씀이세요?”

“부, 붉은 단환. 놈을 조심…….”

붉은 단환?

더 물어보고 싶었지만 철무백의 한계는 거기까지였다. 소리 없이 입을 벙긋거리던 그의 고개가 푹 꺾이자 혁무진이 헛숨을 들이켰다.

“주, 죽었다.”

“……아직 살아 있어.”

“아, 그러네요. 숨결이 너무 미약해서 그만.”

산 사람마저 죽이는 혁무진 이 새끼는 도대체…….

그러나 녀석의 말도 아주 틀린 것은 아니다. 철무백의 가느다란 숨결은 언제 끊길지 모를 정도로 위태로웠다.

월화가 품 안에서 조그마한 자기병을 꺼낸 것은 그때였다.

“거기 목 좀 들어 주시겠어요?”

그녀가 기절한 철무백의 입으로 병을 기울였다.

정체 모를 녹색 액체가 흘러 들어가자 창백했던 안색에 조금씩 핏기가 도는 것이, 상당히 효과가 좋은 약물인 것 같았다.

“이걸로 한숨 돌릴 순 있겠지만 말 그대로 임시방편이에요. 지금의 철 대협의 상태로는 어린아이도 감당 못 해요, 아시죠?”

요컨대 누군가는 남아서 만약의 사태로부터 철무백을 지켜야 한다는 뜻이다. 나는 망설임 없이 고개를 끄덕였다.

“그럼 무진이가…….”

“두 사람이 남으시오.”

“응? 두 사람?”

이게 무슨 소리야. 나와 시선이 마주친 진무경이 뭐 잘못됐냐는 얼굴로 되물었다.

“왜?”

“아니, 우리 둘이 가자고?”

“문제 있나?”

“…….”

당연히 있지.

‘한가락 하는 절정 고수인 철무백을 반송장으로 만든 풍양에, 그 휘하 마적 놈들까지.’

고양이 손이라도 빌려야 할 판국인데, 뭐?

아직 불안한 수준인 혁무진은 몰라도 월화는 데려가야 한다는 게 내 생각이다.

“두 분이서 가능하시겠어요?”

월화의 물음에 내가 재빨리 입을 열었다.

“그거야 당연히…….”

“할 수 있소.”

불가능하다고 말하려던 찰나, 진무경의 깊고 검은 눈동자가 나를 응시했다.

“할 수 있다고 했다. 날 믿어라.”

그 담담하면서도 확신에 찬 한마디에 말문이 막혔다.

순간 치기 어린 젊은이의 객기인가 하는 생각도 들었지만, 내심 고개를 가로젓고 있는 스스로를 발견했다.

‘진천검. 무공의 천재.’

눈앞의 이 녀석은 노력과 재능이 결합해 탄생한 괴물이다. 지금까지 지켜본 바로는 스스로 개죽음을 자처할 만큼 어리석지도 않다.

그리고…….



제한 시간 : 00:02:21



젠장, 더 이상 망설일 시간도 없다.

나는 한숨을 푹 내쉬고 진무경을 향해 물었다.

“자신 있어?”

“이게 최선이다. 어중간한 수준으로는 오히려 짐만 될 뿐이야.”

진무경의 대답에 월화가 피식 웃었다.

“어머, 너무 솔직하신데요?”

“……그 부분은 미안하게 생각하오.”

“뭐, 괜찮아요. 틀린 말은 아니니까.”

저놈이 누구한테 사과하는 건 처음 보네.

다시 보기 힘든 이 희귀한 광경에 혁무진이 끼어들었다.

“이공자님, 저도 무인입니다!”

“그럼 따라오거라. 단, 살아남는 건 알아서 하고.”

“알아서…… 말입니까?”

“장담하건대, 싸움이 시작되면 적들은 너부터 노릴 것이다. 무인답게 장렬히 싸우다 죽는 것도 나쁘지 않겠지.”

잠깐 침묵하던 혁무진이 결의에 찬 얼굴로 대답했다.

“무인으로서, 같은 무도(武道)를 걷는 철 대협을 안전하게 모시고 있겠습니다.”

“…….”

가끔 보면 저게 사람인가 싶다.

‘시간만 있으면 두들겨 패는 건데.’

하지만 이 와중에도 시간은 계속해서 흐르고 있었다.



제한 시간 : 00:01:09



“후우.”

미리 꺼내어 둔 창을 단단히 말아 쥐며 진무경에게 말을 건넸다.

“내가 조무래기들을 맡을게.”

“보통 이런 시점에서는 스스로 우두머리를 맡겠다고 하지 않나?”

“응, 그런 고정 관념을 버려.”

“웃기는 놈이군.”

“분수를 안다고 해 두자.”

“투지와 호승심은 무인을 성장시킨다.”

“그리고 죽음을 촉진시키겠지. 상대를 봐 가면서 덤비는 건 배웠으니까 그 넘치는 투지와 호승심으로 풍양 좀 처리해 줘.”

“말은 청산유수로구나.”

“아, 그리고 들어가면 최대한 은밀히 접근한 다음 내가 신호하면 기습하고. 알았지?”

“기습?”

“기습의 묘리를 살려서 초반에 최대한 큰 피해를 입히고 시작하는 거지. 적들이 우왕좌왕하는 사이에 항산검문주를…….”

“그렇군.”

“좋아, 오랜만에 말이 통하네.”

이걸로 모든 준비는 끝났다. 40초, 39초, 38초.

떨어지는 숫자를 보며 문을 향해 걸음을 떼려던 찰나였다.

저벅.

말리고 자시고 할 시간도 없었다.

성큼 안으로 걸어 들어간 진무경이 공력을 실은 외침을 토해 냈다.

“풍양-!”

띠링.



- [제한 시간]이 사라집니다.



“…….”

진무경 이 개새끼야.



* * *



“혼인? 차라리 죽음을 택하겠다.”

자기 자신의 목에 은장도를 뽑아 겨눈 이소월을 보며 풍양은 혀를 찼다.

“어지간히 애먹이는군. 혈랑검의 여식다워.”

뛰어난 비도술의 소유자인 풍양이지만 현재로서는 그의 장기를 십분 발휘할 수 없었다.

‘망할 노인네…… 결국 잠력단(暫力丹)을 쓰게 만들다니.’

풍양에게도 고작 세 개밖에 없는 귀물이다. 그중 하나를 쓴 덕분에 철무백을 쓰러트릴 수 있었지만 후유증이 제법 컸다.

그는 사시나무처럼 떨리는 손을 소매 아래로 감추며 말했다.

“숨이 붙어 있는 놈들을 모두 끌고 와.”

“옛.”

명령이 떨어지고 얼마 되지 않아 곧장 포박당한 채 끌려오는 항산검문의 무인들. 이소월의 얼굴에 어둠이 내려앉았다.

“무슨 짓을 할 셈이냐?”

풍양이 빙긋 웃었다.

“대충 짐작하고 있을 텐데? 우선 소저가 보는 앞에서 저들의 사지를 하나씩 자를 거요. 팔, 다리, 뭐 이것저것. 썩 유쾌한 광경은 아니니 눈을 감고 있는 걸 추천하지.”

“그런 짓을 했다간…….”

“자결하겠다면 말리지는 않겠소. 충성심 깊은 수하들은 그 대가로 도륙을 당하겠지만.”

이소월이 이를 악물었다.

“당신이 원하는 게 그건 아닐 텐데?”

“혼인 상대가 죽어 버리겠다는데 어쩔 수 없지. 그래도 혈랑검의 독문무공과 항산호의 무공 구결 정도면 충분히, 아. 돌아가는 길에 철무백 그 노인네도 데려가야겠군.”

“……철 숙부가, 아직 살아 계신다고?”

“당연한 소리를. 귀한 무공 구결을 넘겨줄 은인을 그렇게 쉽게 죽일 수야 있나.”

“…….”

“내 목을 걸고 하나 약속하지. 지금이라도 늦지 않았으니 나와 혼인하시오. 하면 단전을 폐하는 선에서 모두 살려 주리다.”

그게 결정타였다. 한동안 속눈썹을 파르르 떨던 이소월이 천천히 손을 내렸다.

“약속은 지켜라.”

“좋은 선택이오.”

풍양의 얼굴에 득의양양한 웃음이 어렸다.

오늘부로 그는 세 번째 인생을 살게 됐다.

거지 소년에서 마적. 마적에서 비로소 정파의 탈을 뒤집어쓰고 항산검문의 실질적인 주인이 됐다.

비록 큰 피해를 입었지만 상관없다. 새 술은 새 부대에 담는 법. 항산검문의 이름으로 무인들을 모집하고 세력을 키워 나갈 것이다.

‘삼십여 년 전 혈랑검도 했던 일을 내가 못 하랴.’

넘치는 희열에 입꼬리가 솟구친 그 순간이었다.

“풍양-!”

공력이 담긴 외침이 천지를 뒤흔들었다.

이소월과 풍양. 그리고 살아남은 모든 이들이 약속이라도 한 듯이 고개를 틀었다.

밤처럼 새카만 흑의(黑衣)를 걸친 청년이 오십여 장 밖에서 걸어오고 있었다.

‘고수.’

풍양은 청년의 송곳 같은 눈빛에 가슴 한구석이 서늘해졌다.

고수다. 그것도 자신과 비교해 결코 떨어지지 않는 절정 고수. 검파를 잡아 가는 손놀림만 봐도 알 수 있었다.

‘이 정도로 젊은 절정 고수는 산서성에 둘뿐이지. 특히 검수(劍手)라면…….’

답은 바로 나왔다. 진천검 진무경. 불과 약관의 나이에 절정의 경지에 오른 천재.

무엇보다 그의 뒤에는 산서제일가로 우뚝 선 태원진가가 버티고 있다.

‘그나마 혼자 왔으니 다행이군.’

그러나 다음 순간, 진무경이 들어온 성문에서 또 다른 한 사람이 슬쩍 고개를 내밀었다.

청년은 남색 무복을 입고 있었다. 복식, 손에 든 묵색 철창, 무엇보다 진무경과 빼다 박은 얼굴이 그가 누구인지를 알려 주었다.

“산서잠룡?”

누군가의 입에서 튀어나온 별호에 진태경이 움찔하더니 중얼거렸다.

“시발, 내 이렇게 될 줄 알았다.”

명문가 자제답지 않은 걸쭉한 욕설과 함께 휘적휘적 걸어오는 진태경, 느긋한 걸음걸이의 진무경.

두 형제의 발걸음이 향하는 쪽에 풍양이 있었다.

‘하필 이럴 때 태원진가라…… 매우 좋지 않아.’

오랜 세월 가문이 쌓아 올린 평판과 팔천협 전투로 얻은 명성. 현재 태원진가의 위상은 독보적이었다.

그 덕분에 산서성 전역에서 수많은 젊은이가 무인을 꿈꾸며 앞다투어 태원진가로 몰려드는 중이다.

그것이 당장 풍양이 항산검문을 삼키더라도 넙죽 엎드린 채 발톱을 숨겨야 하는 이유였다.

‘이번 고비만 넘기면 기회는 온다.’

이미 항산검문은 무너졌다. 무림은 약육강식의 세계고 풍양은 새로운 강자다. 그는 상대가 태원진가라 해도 자신이 충분히 존중받을 만한 자격을 갖췄다고 생각했다.

저벅, 저벅, 저벅.

진무경, 진태경 형제가 발걸음을 옮길 때마다 적풍단의 마적들이 분분히 물러섰다.

풍양은 어느새 코앞까지 다가온 두 사람을 향해 포권을 취했다.

“적풍단주, 풍양이라 하오.”

풍양이 그 어느 때라도 경계심을 늦추지 않는 노련한 무림인이 아니었다면, 아직 잠력단의 효능이 미약하게 남아 있지 않았더라면 그 일격을 피하지 못했을 것이다.

쉬이이잉-!

그는 황급히 몸을 뒤집었다. 목을 스쳐 간 눈부신 검기(劍氣) 한 줄기가 뒤에 있던 마적 셋을 베어 냈다.

“이게 태원진가의 뜻이냐!”

풍양의 노호성에 이미 가까이 있는 마적들을 쓰러트린 진태경이 중얼거렸다.

“난 말로 하고 싶은데.”

“이런 개호로…….”

쉬이이익! 서걱!

말을 끝마치기도 전에 날아온 검기가 풍양의 등을 훑었다. 불에 덴 듯한 통증. 간신히 이어지는 공격을 피한 그는 진무경에 대한 평가를 수정해야 했다.

‘나보다 더 강하다.’

이 정도라면 철무백에게 비견될 만한 움직임이다. 거기에 더해 수하들을 학살하고 있는 진태경까지.

풍양은 자신에게 남은 선택지가 하나밖에 없음을 깨달았다.

‘잠력단.’

그는 품속에 감춰 뒀던 목곽을 꺼냈다. 진무경을 막기 위해 수하들이 죽어 나가는 사이, 단환을 입 안에 털어 넣었다.

쉬이이익!

어느새 핏빛으로 물든 풍양의 눈동자에 진무경의 푸른 검기가 비쳤다.

서걱!
```

## Current accepted English baseline

```markdown
# Chapter 115

Cheol Mubaek, the Tiger of Mount Heng.

I had heard that name several times already. Wolhwa had said that without him, the Mount Heng Sword Sect would have been wiped out by the Red Wind Band long ago.

*“He’s considered a Peak master comparable to or even stronger than the Blood Wolf Sword, Lee Cheonbaek.”*

She had definitely said that.

*Then why has that incredible Peak master ended up like this?*

His limbs were twisted at unnatural angles, and the black blood soaking his shirt was proof of severe internal injuries. Cheol Mubaek looked at us through hazy eyes.

“Taiyuan… Jin Family?”

“Oh, you recognize us?”

I forced the corners of my mouth upward. I wanted to reassure Cheol Mubaek, who was in critical condition, even if only a little.

The man before me was no longer the renowned Peak master known throughout the Murim. He was nothing more than an old man who had found his last hope.

“Red Wind Band… inside… Seowol’s in danger…”

Even without hearing Cheol Mubaek’s halting words, everyone here understood how serious the situation was. Everywhere we looked, there were corpses and pools of blood.

*But it’s not too late yet.*

> **System**  
> **Time Limit:** 00:05:12

We had made it just in time. The problem was that the bastard who had reduced the Tiger of Mount Heng to this state was still inside.

Wolhwa seemed to have reached the same conclusion. She calmed Cheol Mubaek and asked,

“Sir Cheol, did Pung Yang attack you together with another master?”

Cheol Mubaek gave a faint shake of his head.

“You’re saying Pung Yang defeated Sir Cheol by himself?”

“R-red pill. Be careful of that bastard…”

A red pill?

I wanted to ask more, but that was the limit of Cheol Mubaek’s strength. His lips moved soundlessly, then his head drooped. Hyuk Mujin sucked in a startled breath.

“H-he’s dead.”

“…He’s still alive.”

“Oh. So he is. His breathing was just so faint…”

Hyuk Mujin, you bastard. What kind of person kills even the living?

Still, he wasn’t entirely wrong. Cheol Mubaek’s thin breath was so precarious that it could stop at any moment.

That was when Wolhwa pulled a small porcelain bottle from inside her robes.

“Could you lift his head a little?”

She tilted the bottle into the unconscious Cheol Mubaek’s mouth.

As an unidentified green liquid trickled down his throat, color gradually returned to his pale face. It seemed to be a remarkably effective medicine.

“This will help him catch his breath, but it’s only a temporary measure. In his current condition, even a child would be too much for him to handle. You understand, right?”

In short, someone had to stay behind to protect Cheol Mubaek in case something happened. I nodded without hesitation.

“Then Mujin can—”

“Two people stay behind.”

“Huh? Two people?”

What was he talking about? Jin Mukyung met my gaze and looked back at me as if he couldn’t understand what the problem was.

“Why?”

“No, you mean the two of us should go?”

“Is there a problem?”

…

Of course there was.

*Pung Yang had turned a formidable Peak master like Cheol Mubaek into a half-dead man, and he still had all those mounted-bandit bastards under his command.*

We were at the point where we needed every hand we could get, and he was suggesting this?

I didn’t know about Hyuk Mujin, whose abilities were still questionable, but Wolhwa absolutely had to come with us.

“Can the two of you manage?” Wolhwa asked.

I hurriedly opened my mouth.

“Obviously, that’s—”

“We can.”

Just as I was about to say it was impossible, Jin Mukyung’s deep, dark eyes fixed on me.

“I said we can. Trust me.”

His calm yet confident words left me speechless.

For a moment, I wondered if this was merely the reckless bravado of an immature young man. But then I realized I was shaking my head inwardly.

*The Heaven Shaking Sword. A martial arts genius.*

The guy standing before me was a monster born from the combination of effort and talent. From everything I had seen, he wasn’t foolish enough to throw his life away for nothing.

And then…

> **System**  
> **Time Limit:** 00:02:21

Damn it. There was no time left to hesitate.

I let out a deep sigh and asked Jin Mukyung,

“Are you confident?”

“This is the best option. Someone of middling skill would only become a burden.”

Wolhwa let out a quiet laugh.

“My, you’re awfully honest.”

“…I apologize for that.”

“Well, that’s all right. You’re not wrong.”

That was the first time I had ever seen him apologize to anyone.

Hyuk Mujin interrupted this rare spectacle.

“Second Young Master, I’m a martial artist too!”

“Then follow us. But staying alive is your responsibility.”

“On my own…?”

“I guarantee that once the fighting begins, the enemy will target you first. There’s nothing wrong with fighting bravely as a martial artist and dying.”

After a brief silence, Hyuk Mujin answered with a resolute expression.

“As a martial artist, I will safely protect Sir Cheol, who walks the same path of martial arts as I do.”

…

Sometimes, I wondered if that guy was even human.

*If I had the time, I’d beat the hell out of him.*

But even now, time continued to pass.

> **System**  
> **Time Limit:** 00:01:09

“Whew.”

I gripped the spear I had already taken out and spoke to Jin Mukyung.

“I’ll handle the small fry.”

“Usually, at a time like this, shouldn’t you say that you’ll take the leader?”

“Yeah. Throw away that stereotype.”

“You’re ridiculous.”

“Let’s just say I know my place.”

“Fighting spirit and competitive pride help a martial artist grow.”

“And hasten his death. I’ve learned to choose my opponents carefully, so deal with Pung Yang using all that overflowing fighting spirit and competitive pride.”

“You certainly have a way with words.”

“Oh, and when we get inside, approach as quietly as possible. Then ambush them when I give the signal. Got it?”

“Ambush?”

“Use the essence of an ambush to inflict as much damage as possible at the beginning. While the enemies are thrown into confusion, we’ll get to the Sect Leader of the Mount Heng Sword Sect…”

“I see.”

“Good. It’s nice to be understood for once.”

That took care of every preparation. Forty seconds. Thirty-nine. Thirty-eight.

I watched the numbers fall and was just about to walk toward the door when—

Clomp.

There wasn’t even time to stop him.

Jin Mukyung strode inside and let out a shout infused with internal energy.

“Pung Yang!”

> **System**  
> **Time Limit** has disappeared.

…

Jin Mukyung, you fucking asshole.

* * *

“Marriage? I’d choose death instead.”

Pung Yang clicked his tongue as he watched Lee Seowol draw a silver dagger and hold it to her own throat.

“You’re making this awfully difficult. You really are the Blood Wolf Sword’s daughter.”

Though Pung Yang was a master of throwing knives, he couldn’t fully display his specialty in his current condition.

*Damn old man… He actually forced me to use the Temporary Strength Pill.[^1]*

Even Pung Yang possessed only three of these precious pills. Using one had allowed him to defeat Cheol Mubaek, but the aftereffects were considerable.

He hid his hands, trembling like aspen leaves, beneath his sleeves and said,

“Bring everyone who’s still breathing.”

“Yes, Leader.”

Not long after the order was given, martial artists from the Mount Heng Sword Sect were dragged over, bound hand and foot. Darkness settled over Lee Seowol’s face.

“What are you planning to do?”

Pung Yang smiled.

“You can probably guess. First, I’ll cut off their limbs one by one in front of you. Arms, legs, this and that. It won’t be a pleasant sight, so I recommend closing your eyes.”

“If you do that…”

“If you’re going to kill yourself, I won’t stop you. But your loyal subordinates will be slaughtered for it.”

Lee Seowol clenched her teeth.

“That isn’t what you want, is it?”

“If my bride-to-be says she’s going to die, what else can I do? Still, the Blood Wolf Sword’s secret martial art and the Tiger of Mount Heng’s martial arts formula would be enough. Ah, I should take that old man Cheol with me on the way back, too.”

“…Uncle Cheol is still alive?”

“Of course. How could I kill a Benefactor who is going to hand over such a precious martial arts formula?”

“…”

“I’ll stake my life on this promise. It’s not too late even now, so marry me. If you do, I’ll let everyone live. I’ll stop at destroying their dantians.”

That was the decisive blow.

Lee Seowol’s eyelashes trembled for a while before she slowly lowered her hand.

“Keep your promise.”

“A wise choice.”

A triumphant smile spread across Pung Yang’s face.

From this day forward, he would begin his third life.

He had gone from a beggar boy to a mounted bandit. Now, he would finally don the mask of an orthodox faction and become the true master of the Mount Heng Sword Sect.

Though there had been heavy losses, it didn’t matter. New wine belonged in new wineskins. Under the name of the Mount Heng Sword Sect, he would recruit martial artists and expand his power.

*If the Blood Wolf Sword could do the same thing over thirty years ago, why couldn’t I?*

Just as the corners of his mouth lifted with overflowing delight—

“Pung Yang!”

A shout infused with internal energy shook the heavens and earth.

Lee Seowol, Pung Yang, and every surviving person turned their heads as if they had made a pact.

A young man dressed in black as dark as night was walking toward them from some fifty jang away.[^2]

*A master.*

A chill ran through some corner of Pung Yang’s chest beneath the young man’s needle-sharp gaze.

He was a master. And not merely a master—he was a Peak master who was in no way inferior to Pung Yang himself. Pung Yang could tell just from the way the young man’s hand moved as it gripped his sword hilt.

*There are only two Peak masters this young in Shanxi. And if one of them is a swordsman…*

The answer came immediately.

Jin Mukyung, the Heaven Shaking Sword. A genius who had reached the Peak realm while still in his early twenties.

More importantly, behind him stood the Jin Family of Taiyuan, which had risen to become the foremost family in Shanxi.

*At least he came alone.*

But the next moment, another person cautiously stuck his head out through the fortress gate Jin Mukyung had entered.

The young man wore a navy martial robe. His clothing, the dark iron spear in his hand, and above all, his nearly identical face told Pung Yang who he was.

“The Sleeping Dragon of Shanxi?”

At the nickname that escaped someone’s mouth, Jin Taekyung flinched and muttered,

“Fuck. I knew this would happen.”

Jin Taekyung came sauntering forward, cursing crudely in a manner unbecoming a scion of a prestigious family, while Jin Mukyung followed at an easy pace.

The two brothers were heading straight toward Pung Yang.

*The Taiyuan Jin Family, at a time like this… This is very bad.*

The family’s reputation, built over many years, and the fame it had gained through the battle at Eight Spring Gorge had made the Jin Family’s current standing unrivaled.

Because of that, countless young people across Shanxi who dreamed of becoming martial artists were flocking to the Jin Family.

That was why, even if Pung Yang swallowed the Mount Heng Sword Sect right now, he would still have to bow flat and hide his claws.

*Once I get past this hurdle, my opportunity will come.*

The Mount Heng Sword Sect had already collapsed. The Murim was a world where the strong preyed on the weak, and Pung Yang was a new power in that world. Even if his opponent was the Taiyuan Jin Family, he believed he had earned the right to be treated with respect.

Clomp. Clomp. Clomp.

Each time Jin Mukyung and Jin Taekyung took a step, the mounted bandits of the Red Wind Band retreated in confusion.

By the time the two men reached him, Pung Yang raised his hands in a formal salute.

“I am Pung Yang, Red Wind Band Leader.”

If Pung Yang had not been a seasoned martial artist who never lowered his guard, or if the effects of the Temporary Strength Pill had not still lingered faintly, he would never have avoided that strike.

Shiiiiing!

He hurriedly twisted his body.

A dazzling streak of Sword Energy skimmed past his neck and sliced through three mounted bandits behind him.

“Is this the will of the Taiyuan Jin Family?”

Jin Taekyung, who had already felled the mounted bandits nearby, muttered,

“I’d rather talk it out.”

“You fucking bast—”

Before Pung Yang could finish speaking, another streak of Sword Energy flew in and grazed his back.

The pain felt like being burned by fire.

He barely avoided the continuing attack, and his assessment of Jin Mukyung had to change.

*He’s stronger than me.*

At this level, Jin Mukyung’s movements were comparable to Cheol Mubaek’s. On top of that, Jin Taekyung was slaughtering Pung Yang’s subordinates.

Pung Yang realized that he had only one option left.

*The Temporary Strength Pill.*

While his subordinates died one after another trying to stop Jin Mukyung, Pung Yang pulled the wooden case hidden inside his robes and tipped the pill into his mouth.

Shiiiiing!

Jin Mukyung’s blue Sword Energy was reflected in Pung Yang’s eyes, which had turned blood-red.

Slice!

[^1]: The pill’s name literally means “Temporary Strength Pill.”

[^2]: A jang is a traditional unit of distance, roughly three meters.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 115`.

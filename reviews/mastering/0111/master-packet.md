# Master Edit Task — Chapter 111

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
| 이소광    | **Lee Seogwang**   |
| 이소군    | **Lee Seogeun**    |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 일신     | **One God**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 초식     | **form**                                         | Numbered technique movement                           |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 은인     | **Benefactor**                               |
| 퀘스트              | **Quest**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 본문      | **our sect / this sect**                                        |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 정양 | **Jeongyang** | Shanxi location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 산서괴협 | **Strange Hero of Shanxi** | Epithet referenced for the absent martial artist. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |

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
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 105–109

## Plot

At the Phoenix Inn, Jin Taekyung and Hyuk Mujin subdue six mounted-bandit scouts bearing running-horse tattoos. Wolhwa, the inn’s proprietress, a courtesan, and the Lower District Sect’s Shanxi Branch Leader, explains that Lee Cheonbaek hired mounted bands during the war with the Mount Heng Sword Sect. She proposes accompanying Taekyung to Mount Heng to collect the Lower District Sect’s promised compensation and expand its influence in northern Shanxi. Taekyung accepts after Jin Mukyung’s training damages the inn’s private residence and leaves them unable to pay the resulting bill. Wolhwa cancels her sect’s investigation into Taekyung’s unexplained transformation and orders a gag order.

The group travels toward Mount Heng with Chunsam, a Level 50 First Rate martial artist serving as coachman and bodyguard. At an abandoned Guandi Temple, they encounter human traffickers transporting the Five-Colored Ghosts, former subordinates of Jang Sam who had abandoned banditry but recently turned to theft. Taekyung frees them, and Mukyung cripples the traffickers’ leader, Lee Sam, destroying his dantian. The Five-Colored Ghosts reveal that the Red Wind Band is preparing to leave for Saneum.

A messenger hawk from the Lower District Sect’s Sakju Branch reports that roughly two hundred Red Wind Band members are moving south. Wolhwa interrogates captured mounted bandits lethally, while the group rides day and night toward Mount Heng. Pung Yang, the Red Wind Band Leader, has already destroyed the Mount Heng Sword Sect’s Datong Branch and ordered that no prisoners be taken. The weakened sect, having lost nearly eighty percent of its strength in the war with the Jin Family of Taiyuan, learns that an attack may come within one or two days. As its leaders despair, the main hall doors suddenly explode, marking the attack’s beginning.

## Continuity

- Taekyung, Mukyung, Mujin, and Wolhwa are riding toward the Mount Heng Sword Sect without resting.
- Chunsam is a First Rate Lower District Sect martial artist who served as their carriage driver and bodyguard.
- Wolhwa is the Phoenix Inn’s proprietress, a courtesan, Shanxi Branch Leader, and major information broker.
- The Lower District Sect assisted the Jin Family during the war under a secret compensation pact. Wolhwa intends to collect its compensation and expand into northern Shanxi.
- Wolhwa has stopped investigating Taekyung’s transformation and ordered her organization to keep the matter confidential.
- The Five-Colored Ghosts and surviving mounted bandits are being transported to a nearby Lower District Sect branch.
- The Red Wind Band numbers approximately two hundred and is led by Pung Yang, who places his personal orders above plateau customs.
- Pung Yang’s forces destroyed the Mount Heng Sword Sect’s Datong Branch with no survivors and are moving south toward the sect’s headquarters.
- Mount Heng has lost nearly eighty percent of its strength since the war with the Jin Family. Its attack is expected within one or two days, and its main hall doors have been destroyed.
- Taekyung’s Quest difficulty has risen to Peak.
- Unresolved hooks remain: the identity of the surveillance property near Taekyung’s former home; whether the black Familiar and Kim Gwondong share instructions; Kim Hwajong’s reason for arriving and his current butler position; the Security Team’s final punishment; how Seong Jinho entered the capsule; Mount Heng’s response to the merger and Wolhwa’s compensation; and what follows the destruction of the main hall doors.

## Translation Decisions

- Retain **Familiar**, **Logout**, **Inventory**, **Qi Sense**, and **Fire Wall**.
- Render **마적/마적단** as **mounted bandits/mounted-bandit groups**, **적풍단** as **Red Wind Band**, **적풍단주** as **Red Wind Band Leader**, and **토호단** as **Earth Tiger Band**.
- Render **오색귀** as **Five-Colored Ghosts**, **전서응** as **messenger hawk**, and **관제묘** as **Guandi Temple**.
- Render **추종향** as **tracking scent**, **대동** as **Datong**, **산음** as **Saneum**, **풍양** as **Pung Yang**, and **춘삼** as **Chunsam**.
- Retain **Peak**, **First Rate**, **master beyond First Rate**, and **One Strike** for the established martial ranks and technique.
- Preserve Wolhwa’s addresses **Young Master**, **Young Master Jin**, and **Young Hero Jin**; render **대형** as **Boss**.

### Prior accepted reading-copy tails

#### Chapter 109 tail (verified mastered)

…
up the hill to report answered him. “We killed all the men and gathered the women and children together.” “Why?” “Pardon? Why, it’s the tradition of Gaoyuan…” Any male taller than a cartwheel—even a child—was killed without mercy, while the women were taken or sold as slaves. It was a tradition—or something close to one—passed down from the nomads. At the mounted bandit’s words, Pung Yang quietly crooked one finger. “Come closer.” The mounted bandit approached hesitantly and asked carefully, “Leader, did I perhaps make some serious mistake…” “Who were you with before?” “Until recently, I was the deputy leader of the Earth Tiger Band.” “The Earth Tiger Band? Ah, I remember. You were their deputy leader.” “Y-yes! I was so impressed by your formidable martial arts and noble character that I swore to become your loyal subordinate!” Pung Yang scratched his nose with an ambiguous expression. *Was that so?* All he remembered was killing a piece of trash in a single strike—the man who had swaggered around calling himself a bandit leader while commanding some thirty subordinates. “My memory differs a little, but thank you anyway.” “Not at all! It’s an honor!” “Still, whatever the Earth Tiger Band may have been like, things are different in the Red Wind Band. Petty matters like the traditions of Gaoyuan, for instance.” “Ah, I didn’t realize.” “My orders as leader take priority. Do you understand?” “I’ll keep that in mind—over and over again!” “Those fellows probably followed Gaoyuan’s traditions because they didn’t know any better. They all joined recently, just like you. Would you go and tell them what I want?” “Your command is my law. I won’t leave a single one alive.” The mounted bandit even gave an awkward military salute, though there was nothing military about a mounted bandit. Pung Yang waved him away. “Yes, go on.” “Yes, Leader!” Pung Yang watched him ride away, then suddenly flicked his sleeve. *Whoosh!* A streak of light split the air and pierced its target ten jang—about thirty meters—away. *Thnk! Thud.* The horse kept galloping. It had no idea that its rider was already dead, his foot caught in the stirrup and his body being battered to pieces against the ground. “Go and tell them. There are no prisoners. Kill them all and burn the place.” “Yes, Leader.” Not long after Pung Yang’s subordinate departed, the entire manor was engulfed in flames. As he watched the signboard burn away in an instant, a faint smile touched the corners of his mouth. Mount Heng Sword Sect, Datong Branch. It was the moment the Red Wind Band crossed Gaoyuan once more. * * * The messenger’s report left the people arguing in the spacious main hall breathless. “They’ve broken through Datong!” “A-already?” “What about the Datong Branch? What happened to the men who went out to stand guard?” “Wiped out. They were all wiped out. The Datong Branch was reduced to ashes, and there wasn’t a single survivor.” “What?” “Could the report be wrong? They must have suffered heavy losses last time, so how could they have come this far so quickly…?” “They appear to have absorbed another mounted-bandit group. At least two hundred men—possibly more.” “Is that certain?” “Yes, without a doubt.” “Th-then when will they reach us…?” “If they’re fast, the attack will begin within a day. At the latest, we expect it within two days.” “We’re finished.” The muttered words were not much different from what most of the people gathered there were thinking. There were a little over ten of them, all senior figures holding important positions in the Mount Heng Sword Sect. Yet every one of them was already turning the word *defeat* over in their minds. “Iron Sword Squad Leader, are you confident in this fight?” “Why are you asking me, when you’re a Pavilion Leader? Am I the only martial artist here?” They were squad leaders, hall leaders, and pavilion leaders of the great Mount Heng Sword Sect. There had been a time when he had desperately wanted to rise to that position. Once upon a time, that was. To hell with the great Mount Heng Sword Sect. What good is a promotion now, with the sect in this state? *We were already on the verge of collapse, and now a mounted-bandit group has come to raise hell. Let’s see… If we scrape together everyone we have left, we might reach a hundred.* The war with the Jin Family of Taiyuan had cost them nearly eighty percent of their strength. They had lost the elite martial artists they had painstakingly trained and the seasoned senior figures who had weathered countless trials in the martial world. Most painful of all was the loss of the Peak masters who embodied the sect’s power—and of its financial resources. “Damn it. If only the Sect Leader were still alive.” Lee Cheonbaek had started as a mere wandering martial artist and built the Mount Heng Sword Sect into what it was now. With his martial arts and resourcefulness, he could have turned this situation around. But the Blood Wolf Sword, Lee Cheonbaek, was already dead. Of his bloodline, only one person remained alive. “To think we have to serve some little girl who isn’t even twenty as Sect Leader at a time like this.” The moment someone spat out those words in anger— *Boom!* The tightly closed doors of the main hall exploded.

#### Chapter 110 tail (verified mastered)

…
the items I had obtained after defeating Jopil—including the Blazing Flame Divine Pill—were sitting untouched in my Inventory. *Of course, taking it wrong could send me straight to the grave.* Just then, Wolhwa, who had been riding at the front, spotted a stream and pulled to a stop. “We’ll rest for a little while. The horses are too exhausted.” How much time had passed? We had ridden without stopping since leaving the shrine. Dawn had broken, and now the sun hung high overhead. System messages announcing increases to my Strength and Stamina had even appeared twice, so this really had been a forced march. “Whew. My ass is killing me. If I’d known this would happen, I should’ve been born the son of a coachman instead of a farmer.” While the horses rested, Hyuk Mujin dropped heavily to the ground. Since he was the lowest-level member of the group, his exhaustion was obvious. “Having a hard time?” Hyuk Mujin wiped the sweat from his forehead with his sleeve before answering. “Honestly, yes… But strangely enough, it’s much better than last time.” “Last time?” “You’ve already forgotten? During the scouting mission.” “Ah, I remember.” I had nearly died after running into Jopil during a scouting mission for White Tiger Hall. We had taken horses with us then too. *Though we ended up abandoning them when the heavy snow came.* The memory drew a quiet laugh from me. “What’s wrong?” “I was thinking about you. You mouthed off to me without knowing any better and got the crap beaten out of you.” “……Do you really have to dredge up the past to feel better?” “You’re the one who asked, punk.” “Anyway, I’m saying it seems much better than back then.” “Really?” “Yes. We’ve ridden much farther than we did during the scouting mission, but I’m not even that tired. Maybe I’m getting used to riding?” “Maybe… Ah, wait.” “Hm?” Something suddenly occurred to me, so I heightened my Qi Sense. *Ding.* With the familiar System notification, a Level Window appeared over Hyuk Mujin’s bewildered face. > **System** > > **Level:** 38 — Hyuk Mujin “……Huh?” A breathy sound escaped my open mouth. When had Hyuk Mujin’s Level gotten this high? *Strictly speaking, it wasn’t all that high.* But considering that he had been only Level 20 when we first met, calling it astonishing progress wasn’t enough. At this point, it was practically like he had been reborn. *Come to think of it, his Level has been rising steadily ever since we met.* As I searched my memory, the details came back more clearly. It had been the same when we reunited as a scouting unit. Whenever I heightened my Qi Sense from time to time, Hyuk Mujin’s Level had risen by one or two. Now he was Level 38. In terms of time spent in Murim, he had nearly doubled his Level in just over two months. *Then maybe…?* With a doubtful heart, I stared intently at Hyuk Mujin. What if he received stat points like I did? Could I distribute them for him? *It’s possible.* Judging by how much stronger I was than a Hunter or martial artist of a similar Level, there seemed to be some kind of System enhancement effect… *It’s worth trying once.* “Why are you staring at me like that? Is there something on my face?” “No. You’re just ugly.” “……Seriously.” I grabbed Hyuk Mujin by the shoulder and shouted inwardly. *Open Status Window!* At that very moment— “What are you doing? My shoulder hurts.” “Oh. Okay.” Nothing happened. I thought at least something would appear. Then again, my main character was still far from reaching the Level cap. Why would my alt character get anything? Still, it was disappointing. *Should I try saying it out loud?* They would definitely treat me like some kind of weirdo, but it was better than moving on with the feeling of not washing my hands after using the bathroom. I stealthily placed my hand against Hyuk Mujin’s back—lightly, very lightly—and muttered under my breath. “Open Status Window.” “Seriously, what has gotten into you today?” I ignored him and shot to my feet. The notification I had been waiting for chimed, and a System Window appeared. “Yes! There it is!” *Ding.* > **System** > > The Quest condition **Time Limit** has been added. > > Arrive at the Mount Heng Sword Sect within **22:00:00**. If you are late, there will be no turning back. “Yes…” My voice died away. My eyes trembled. *A time limit? What the hell kind of time limit is this?* *Why are you doing this to me? Seriously.* As I let out a deep sigh, Wolhwa’s eyes widened and she asked, “Young Master Jin, are you hurt?” “No, it’s not that. Do you know around when we’ll arrive?” “Hmm. At today’s pace, before tomorrow evening?” “Ah.” It was a little past noon now. That meant we still had more than a full day’s ride ahead of us. Judging by the Quest Window’s change, it seemed the Red Wind Band bastards would attack the Mount Heng Sword Sect within that time limit… What was I supposed to do? “Shall we get going soon?” “The horses are tired. They need to rest for half a shichen.” “Horses, you’re fine, aren’t you? You heard that, right? They said they’re fine.” “……” Yeah. I knew you’d look at me like that.

## Korean source

```text
＃111화



두두두두!

네 마리 준마가 관도를 내달린다. 휴식이 부족했던 탓에 지칠 대로 지친 말들이 숨을 헐떡거렸지만 고삐를 늦출 수 없었다.



제한 시간 : 16:25:32



31, 30. 시간은 계속해서 줄어들고 있다.

벌써 세 시진, 자그마치 여섯 시간이 흘렀다. 오는 길에 작은 마을에 들러 갈아탈 말을 구하려 했지만 작고 느려 터진 짐말밖에 없었다.

‘휴식을 취하긴 해야 하는데.’

외통수다.

충분히 강행군을 이어 가고 있지만 제한 시간이 아슬아슬하고, 지금처럼 달리면 말이 버티지 못할 거다.

‘어쩔 수 없나.’

월화와 진무경에게 잠시라도 쉬어 가자고 말하려던 찰나였다.

“어?”

“진 공자! 앞에!”

굳이 월화의 외침이 아니더라도 나는 이미 놈들을 보고 있었다. 수십 장 앞, 관도를 막아선 시커먼 사내들.

하나같이 너저분한 옷차림에 허리춤에는 곡도 한 자루가 삐죽 튀어나와 있다. 이제 두말하면 입 아프다.

‘적풍단.’

양민으로 보이는 이들을 빙 둘러싸고 으름장을 놓던 놈들이 말발굽 소리에 고개를 홱 돌렸다.

멀찍이 선두에서 앞서 달리던 나를 발견한 마적들이 누런 이를 드러내며 웃는다.

“어이구, 벌써 다음 손님 오셨네. 정지!”

“어, 그래.”

멈추라는데 멈춰야지, 별수 있나.

퍼버벅!

“커허어억!”

“끄악!”

내가 타고 있는 준마는 앞을 가로막고 있던 두어 놈을 짓밟고 나서야 멈췄다. 마적들은 물론이고 붙잡혀 있던 행인들까지 눈을 동그랗게 뜨고 날 쳐다본다.

“너, 너 이 새끼!”

안장에서 훌쩍 뛰어내리며 물었다.

“혹시 몰라서 물어본다. 적풍단, 맞지?”

“웬 놈이냐!”

“반응 보니까 맞나 보네. 시간 없으니까 빨리 끝내자.”

망설임 없이 가장 가까이 있는 놈의 다리를 걷어찼다.

콰직, 섬뜩한 소리와 함께 정강이뼈가 부러진 놈이 주저앉는다.

창졸간에 벌어진 일. 순간 얼이 빠져 있던 놈들이 재빨리 곡도와 창을 들이댔다.

“죽여!”

“남자는 항상 후방을 주의해라.”

“뭐?”

“뒤에 조심하라고.”

열 쌍의 눈이 내 말이 끝나자마자 등 뒤를 돌아보던 그때.

콰드드득! 뻐억!

전속력으로 달려온 세 마리의 준마가 놈들을 쓸어 버렸다.



* * *



전투는 시작되기도 전에 끝났다. 말에 치여 볼링 핀처럼 나가떨어진 놈들은 산송장처럼 누워 있었고 나머지 놈들도 손쉽게 제압당했다.

“사, 살려만 주십시오.”

“안 죽인다. 몇 군데는 손봐 줘야겠지만.”

“히익!”

진무경이 살아남은 산적들의 팔다리를 똑똑 분지르는 사이 혁무진은 길옆에 매여 있던 말들을 끌고 왔다.

“여기 팔팔한 놈들로 갈아타면 될 것 같은데요? 열 마리는 되니까 아예 싹 가져가서 지칠 때마다 교체하고.”

나도 같은 생각이다. 지난번 놈들과는 달리 이번에 만난 마적들은 각자 말을 소지하고 있어서 다행이었다.

‘그나저나…….’

이놈의 적풍단 놈들은 도대체 몇 명이나 있는 거야?

사당에서 얻은 정보에 의하면 백 명이 넘는 잔당들이 산서 북부 곳곳으로 흩어졌다고 했다.

더러는 산자락으로, 더러는 궁벽한 마을 혹은 번화한 곳에서 숨어 있다가 명령에 따라 집결지로 모인다는 것이다.

‘이놈들, 패잔병이 아니야.’

놈들은 작전을 수행 중인 복병이다. 적풍단주는 고원에서 병력을 충원하여 남하(南下)하는 한편 남겨 둔 수하들을 북상(北上)시키고 있다.

월화가 적풍단주를 무서운 인물이라고 평한 이유를 충분히 짐작하고도 남는다.

‘전황이 불리하게 흘러가니 신속하게 물러나는 판단력, 그 와중에도 다음 계획을 준비하는 치밀함, 그리고 계획을 실행시키는 추진력.’

거기에 더해 그는 일신에 지닌 무공도 고강하다고 들었다.

이쯤 되면 단순한 마적 취급하기도 미안할 지경이다.

‘이거 일이 상당히 지저분하게 됐는데.’

왜 퀘스트 등급이 절정으로 바뀌었는지 알겠다. 점입가경으로 알고 보니까 뭐, 적풍단주가 절정 고수라든지 그런 건 아니겠지?

혹시나 하는 마음에 월화에게 물었더니 대번에 고개를 끄덕인다.

“네. 맞는데요?”

“……아.”

“이렇게 급속도로 두각을 드러낸 것에는 이유가 있기 마련이죠. 아직 널리 알려지지는 않았지만 본 문의 정보에 의하면 적풍단주는 절정 고수가 맞아요.”

나는 어이가 없어져서 물었다.

“아니, 절정 고수가 왜 마적질을 합니까?”

“산적, 수적 중에서는 초절정 고수도 있는데 마적이라고 못 할 것 있나요.”

“초절정 고수요? 산적, 수적이?”

“나중에 녹림맹주나 장강수로맹주를 만나면 물어보세요. 그럴 일은 없겠지만.”

“……제발 그랬으면 좋겠네요.”

초절정 고수라니, 진심으로 만나는 일이 없었으면 좋겠다.

고개를 절레절레 흔들고 새로 뺏은 말에 올라탔다. 적풍단의 마적들을 꽁꽁 묶어 양민들에게 넘긴 진무경과 혁무진이 그 뒤를 잇는다.



제한 시간: 15:59:13



이 순간에도 제한 시간은 흘러가는 중이다. 우리는 허리 숙여 감사를 표하는 양민들을 뒤로하고 말 옆구리를 걷어찼다.

“이랴!”



* * *



항산검문 깊숙한 내원에는 극소수의 사람들만 드나들 수 있는 화원이 존재한다. 항산호 철무백은 외부인 중 유일하게 그 자격을 부여받은 사람이었다.

“이곳에 온 것은 이번이 처음이구나.”

“특별한 공간이었으니까요. 아버지는 고민이 있으실 때마다 화원을 찾으셨죠.”

눈 덮인 화원을 사박사박 걷던 이소월이 서리 낀 꽃 한 송이를 발견하고 문득 걸음을 멈췄다.

“어머니가 좋아하시던 꽃이에요.”

“그랬느냐?”

“네, 화원을 가꿀 때면 항상 저를 이곳으로 데려와서 꽃의 이름을 알려 주시곤 했죠.”

잠시 곰곰이 생각에 잠겨 있던 이소월이 말을 이었다.

“그런데 지금은 기억이 안 나네요.”

“오래전 일이니 그럴 만하다. 괘념치 말거라.”

“철 숙부.”

“응?”

“저, 꽃 싫어해요. 어머니가 좋아서 따라왔을 뿐이지, 사실 꽃에는 관심도 없었어요. 아버지께서 화원을 찾으시는 이유와 같은 거죠.”

이소월은 눈 덮인 화원을 천천히 둘러보았다. 꽃은 시들었고 화원 중앙에 마련된 봉분(封墳)은 하나에서 넷으로 늘었다.

가족들이 잠들어 있는 봉분을 말없이 바라보는 그녀의 눈빛이 깊게 가라앉았다.

‘누구의 잘못일까?’

어쩌면 무림인의 딸로 태어난 자신의 잘못일지도 모르겠다.

그것이 십 년 전 어머니에 이어 아버지와 두 오라버니를 차례로 잃어야 했던 이유다.

‘끝까지 말렸어야 했는데…….’

문득 두 달 전의 기억이 떠올라 눈 앞을 가린다.

그건 어느 야심한 밤, 단둘이 나눴던 부녀(父女) 간의 대화였다.



‘널 태원진가의 셋째와 엮어야겠다.’

‘셋째라면. 설마 그 망나니와 절 맺어 줄 생각이신가요?’

‘아니다. 그러나 너로서는 견디기 힘든 추문(醜聞)이 될 것이다.’

‘그렇군요.’

‘그뿐이냐?’

‘어쩌겠어요. 비정한 아비를 둔 제 잘못이죠.’

‘알다가도 모를 아이구나. 정말 아무렇지 않은 게냐?’

‘제가 싫다고 하면, 마음을 돌리실 건가요?’

‘적어도 다른 방법을 찾아보겠지.’

‘결국 태원진가와의 전쟁은 기정사실이군요.’

‘산서괴협(山西怪俠)과 진천검이 없는 지금이 적기다. 두 번 다시 오지 않을 기회야.’

‘가주와 이공자가 없어도 태원진가는 강해요. 부디 재고를.’

‘불가(不可). 결정은 이미 내렸다.’

‘그렇다면 반드시 승리하세요. 산서 땅에서 저에 관한 추문 따위는 입도 벙긋 못 할 정도로 강해지세요.’

‘……네가 사내였다면 소문주로 삼았을 것이다.’

‘여인으로 태어나서 다행이네요. 본문의 소문주 따위, 관심도 없으니.’



우려는 얼마 지나지 않아 현실로 바뀌었다.

보름이나 지났을까, 이소군이 싸늘한 시신으로 돌아왔다. 그리고 얼마 후에는 이천백이, 결국은 큰 오라버니인 이소광마저 잃고 말았다.

‘이제는 나 혼자야.’

그렇게 혈랑검 이천백의 마지막 남은 혈육은 새로운 문주가 되었다.

말없이 봉분을 응시하는 이소월의 어깨를 따뜻한 손바닥이 조심스레 어루만졌다.

“미안하구나. 내가 더 빨리 왔어야 했는데…….”

“철 숙부, 그런 말씀 마세요. 숙부께서 와 주시지 않았다면 본 문은 지금까지 버티지도 못했을 테니까.”

적풍단의 거친 공세에 항산검문은 속절없이 밀리는 중이었다. 뒤늦게 이천백의 변고를 접하고 달려온 항산호라는 절정 고수가 없었다면 적들이 물러나는 일도 없었을 것이다.

“내 반드시 그놈의 사지를 찢어 죽일 것이다.”

적풍단주를 떠올린 이소월은 고개를 저었다.

절정 고수끼리의 생사결이라면 철무백이 한 수 앞선다.

이미 앞서 한 번의 격돌이 있었고 풍양은 가벼운 내상과 함께 물러난 전적이 있다.

‘하지만 두 번 다시 그런 기회는 오지 않아.’

항산검문은 북쪽 고원의 마적들에 관해 늘 정보를 수집하고 촉각을 곤두세우고 있었다.

고원에 존재하는 마적단은 수십 개지만 그중에서도 풍양이 이끄는 적풍단은 눈에 띌 정도로 무섭게 성장했다.

고원의 우두머리 중에서도 특히 강하고 치밀한 자. 그가 바로 풍양이다.

‘그런 자가 철 숙부와 생사결을 펼칠 리 없어. 섣불리 상대하려 했다가는 거꾸로 당하고 말 거야.’

이소월은 철무백을 향해 고개를 돌렸다.

“철 숙부. 풍양의 무공에 대해 다시 한번 말씀해 주실 수 있나요?”

“절정 초입. 도법과 비도술이 경지에 오른 자였다. 다만.”

철무백의 미간에 깊은 골이 파였다.

“초식 하나하나가 음험하기 짝이 없더구나. 아마 사마외도(邪魔外道)의 무공을 익힌 듯싶었다.”

“사마외도…….”

정마대전 이후 중원에서 사마외도는 곧 죽음이라는 단어와 동일시되었다. 정파를 표방하는 사파는 있을지언정, 당당히 사파라고 외치는 이들은 없다.

“아직까지는 짐작일 뿐이다. 다시 한번 붙어 보면 알게 되겠지.”

“철 숙부를 믿어요. 그러나 적풍단주를 우습게 보진 마세요. 그에게는 목숨을 대신할 수하들이 얼마든지 있으니까.”

위아래로 짓쳐 드는 적들을 합하면 삼백에 가까운 대병력.

반면 항산검문은 각 지부에 나가 있는 무인들까지 모두 끌어모았음에도 그 절반에도 못 미친다.

상황이 이렇다 보니 일반 무인들은 물론이고 새로 임명된 중진들의 사기도 저조했다.

“소월아. 내 한마디 해도 되겠느냐?”

죽은 벗과의 우정을 위해 자신의 목숨을 건 은인의 말이다. 이소월은 공손히 고개를 숙였다.

“새겨듣겠습니다.”

철무백이 무겁게 입을 뗐다.

“떠나거라.”

많은 의미가 담겨 있는 한마디.

그러나 이소월의 대답에는 한 치의 망설임도 없었다.

“죄송합니다.”

“아직 늦지 않았다. 넌 살아남아야 한다.”

“아직 끝나지 않았습니다. 살아남을 거고요.”

“천백이 그 친구가 이런 걸 원한다고 생각했다면…….”

“숙부님.”

단호한 목소리에 철무백이 입을 다물었다. 이소월의 맑은 눈동자엔 굳은 결의가 어려 있었다.

“제가 원한 겁니다. 항산검문의 문주로서.”

“휴우…….”

철무백은 대답 대신 한숨을 토해 냈다.

“숙부께는 이미 많은 신세를 졌습니다. 이대로 떠나신다고 해도 원망하지 않을 거예요.”

“굳이 내 대답을 들어야 직성이 풀리겠느냐?”

이소월은 고개를 저었다. 어릴 적부터 그녀를 자식처럼 아껴 주었던 철무백이다. 오히려 아버지보다 더 아버지 같은 사람이기도 했다.

“이 은혜는 결코 잊지 않겠습니다. 철 숙부는 저와 항산검문의 은인이십니다.”

“어려서부터 봤지만…… 너는 참 영악한 아이다.”

“어릴 때는 영악했고, 지금은 독한 년이죠.”

싱긋 웃는 이소월을 보며 철무백은 연신 깊은 한숨만 내쉬었다.

“승산은 있는 게냐?”

“지금이라면 일 할.”

“뭐라?”

“하지만 지원군이 도착한다면 오 할. 그 이상이죠.”

“지원군이라니, 혹시 태원진가에서?”

“두 시진 전에 하오문 정양 지부에서 보낸 전서구가 도착했어요.”

“얼마나 된다 하더냐? 백? 이백?”

“넷이요. 그중 하나는 진천검 진무경이고, 다른 하나는…….”

이소월이 실소를 흘렸다. 그와 얽힌 악연이 생각나서다.

“산서잠룡 진태경.”
```

## Current accepted English baseline

```markdown
# Chapter 111

*Thudthudthudthud!*

Four fine horses raced down the main road. Exhausted from their lack of rest, the horses were already gasping for breath, but there was no way we could loosen the reins.

> **System**
>
> **Time Limit:** 16:25:32

31, 30. The time kept ticking down.

Three *sijin*—six hours—had already passed. We had tried to stop at a small village along the way and find fresh horses, but all they had were small, painfully slow packhorses.

*We really do need to rest.*

We were trapped between a rock and a hard place.

We had been forcing our march as hard as we could, but the time limit was dangerously close. If we kept running like this, the horses wouldn’t hold out.

*Can’t be helped.*

I was just about to suggest to Wolhwa and Jin Mukyung that we rest, even if only briefly, when—

“Hm?”

“Young Master Jin! Ahead!”

Even without Wolhwa’s shout, I had already seen them. Several dozen *jang* ahead, a group of dark figures blocked the main road.

Every one of them wore filthy clothes, with a single curved saber sticking out from his belt. There was no need to say anything more.

*The Red Wind Band.*

The men had surrounded what appeared to be ordinary civilians and were threatening them. At the sound of hoofbeats, they whipped their heads around.

The mounted bandits spotted me riding well out in front and grinned, baring their yellow teeth.

“Well, look at that. Our next customers have already arrived. Stop!”

“Oh, sure.”

They told me to stop, so I had to stop. What else could I do?

*Thud! Thud!*

“Gaaah!”

“Argh!”

The fine horse I was riding didn’t come to a stop until it had trampled the two men blocking the road. The mounted bandits—and even the travelers they had been holding captive—stared at me with their eyes wide.

“You—you bastard!”

I hopped down from the saddle and asked,

“I’m asking just to make sure. You’re the Red Wind Band, right?”

“What the hell are you?”

“Judging by your reaction, I guess I was right. I’m short on time, so let’s finish this quickly.”

Without hesitation, I kicked the leg of the nearest man.

*Crack.*

With a chilling sound, his shinbone snapped, and he collapsed.

It all happened in an instant. The men who had been momentarily stunned quickly thrust curved sabers and spears at me.

“Kill him!”

“A man should always watch his rear.”

“What?”

“Be careful behind you.”

The instant I finished speaking, ten pairs of eyes turned to look behind them.

*Craack! Thud!*

Three fine horses charging at full speed swept the men away.

* * *

The battle was over before it had even begun. The men struck by the horses had been sent flying like bowling pins and lay sprawled out half-dead. The rest were easily subdued.

“P-Please, just spare my life.”

“I won’t kill you. But I’ll have to fix a few things first.”

“Eek!”

While Jin Mukyung methodically broke the limbs of the surviving bandits, Hyuk Mujin brought over the horses tied up beside the road.

“It looks like we can switch to these healthy ones. There must be at least ten of them, so we could take them all and switch whenever they get tired.”

I had been thinking the same thing. Unlike the last group we encountered, these mounted bandits each had their own horses. It was fortunate.

*But still…*

How many of these Red Wind Band bastards were there?

According to the information we obtained at the shrine, more than a hundred remnants had scattered throughout northern Shanxi.

Some were hiding in the foothills, while others were concealed in remote villages or crowded areas, gathering at a designated rendezvous point when ordered.

*These men aren’t stragglers.*

They were ambush forces carrying out an operation. The Red Wind Band Leader was replenishing his forces on the plateau and moving south, while sending the subordinates he had left behind north.

I could easily understand why Wolhwa had described the Red Wind Band Leader as such a terrifying man.

*The judgment to retreat swiftly when the battle turned against him. The meticulousness to prepare his next plan even in the middle of it all. And the drive to carry that plan out.*

On top of that, I had heard that his own martial arts were formidable.

At this point, I almost felt bad for treating him as nothing more than a mounted bandit.

*This has gotten seriously messy.*

Now I understood why the Quest Grade had risen to Peak. And when I thought about it, things seemed to be getting worse by the minute.

It couldn’t be that the Red Wind Band Leader was a Peak master too, could it?

I asked Wolhwa just in case.

She immediately nodded.

“Yes. He is.”

“…Ah.”

“There has to be a reason someone rose to prominence so quickly. He isn’t widely known yet, but according to our sect’s intelligence, the Red Wind Band Leader is indeed a Peak master.”

I was dumbfounded.

“Why would a Peak master become a mounted bandit?”

“There are even Supreme Peak masters among mountain bandits and water bandits. Why couldn’t a mounted bandit be one?”

“Supreme Peak masters? Among mountain bandits and water bandits?”

“When you meet the Green Forest Alliance Leader or the Alliance Leader of the Yangtze River Channel League, ask them yourself. Not that you ever will.”

“…I sincerely hope that’s true.”

A Supreme Peak master? I genuinely hoped I would never meet one.

I shook my head repeatedly and mounted one of the newly taken horses. Jin Mukyung and Hyuk Mujin followed after tying up the Red Wind Band’s mounted bandits and handing them over to the commoners.

> **System**
>
> **Time Limit:** 15:59:13

The time limit continued to tick down even now. Leaving the commoners behind as they bowed deeply in thanks, we kicked the horses in the ribs.

“Giddyap!”

* * *

Deep within the inner grounds of the Mount Heng Sword Sect stood a garden that only a very small number of people were allowed to enter. Cheol Mubaek, the Tiger of Mount Heng, was the only outsider granted that privilege.

“This is my first time here.”

“Because it was a special place. Whenever Father had something weighing on his mind, he would come to the garden.”

Lee Seowol walked through the snow-covered garden, her footsteps crunching softly. Then she suddenly stopped when she spotted a frost-covered flower.

“This was one of Mother’s favorite flowers.”

“Was it?”

“Yes. Whenever she tended the garden, she would always bring me here and tell me the names of the flowers.”

After thinking quietly for a moment, Lee Seowol continued.

“But I can’t remember it now.”

“It was a long time ago. Don’t trouble yourself over it.”

“Uncle Cheol.”

“Yes?”

“I don’t like flowers. I only followed Mother because she liked them. In truth, I never cared about flowers. It’s the same reason Father used to come to the garden.”

Lee Seowol slowly looked around the snow-covered garden. The flowers had withered, and the number of burial mounds in the center of the garden had grown from one to four.

Her gaze sank as she silently stared at the mounds where her family slept.

*Whose fault was it?*

Perhaps it was her own fault for being born the daughter of a Murim martial artist.

That was why she had lost her father and two older brothers one after another, after losing her mother ten years ago.

*I should have kept trying to stop him until the very end…*

A memory from two months ago suddenly resurfaced and blurred her vision.

It had been a conversation between father and daughter, held late one night with no one else present.

*“I’ll have to tie you to the third son of the Jin Family of Taiyuan.”*

*“The third son? Surely you’re not thinking of marrying me to that good-for-nothing?”*

*“No. But it will become an unbearable scandal for you.”*

*“I see.”*

*“Is that all you have to say?”*

*“What can I do? It’s my fault for having a heartless father.”*

*“You’re a child I can never understand. Are you really all right with this?”*

*“If I say I don’t like it, will you change your mind?”*

*“At the very least, I’ll look for another way.”*

*“So the war with the Jin Family of Taiyuan is a foregone conclusion.”*

*“Now that the Strange Hero of Shanxi and the Heaven Shaking Sword are absent, this is the perfect time. This opportunity will never come again.”*

*“The Jin Family of Taiyuan is strong even without the Family Head and the Second Young Master. Please reconsider.”*

*“No. My decision has already been made.”*

*“Then make sure you win. Become strong enough that no one in Shanxi can even open their mouth about a scandal involving me.”*

*“…If you had been a man, I would have made you the Young Sect Leader.”*

*“I’m glad I was born a woman. I have no interest in being this sect’s Young Sect Leader.”*

Her fears soon became reality.

Had even a fortnight passed before Lee Seogeun returned as a cold corpse? Not long after, she lost Lee Cheonbaek, and in the end, even her eldest older brother, Lee Seogwang.

*Now I’m alone.*

And so, the Blood Wolf Sword Lee Cheonbaek’s last surviving blood relative became the new Sect Leader.

A warm palm gently caressed Lee Seowol’s shoulder.

“I’m sorry. I should have come sooner…”

“Uncle Cheol, please don’t say that. If you hadn’t come, our sect wouldn’t have been able to hold out this long.”

Under the Red Wind Band’s fierce assault, the Mount Heng Sword Sect had been helplessly driven back. If not for the Peak master known as the Tiger of Mount Heng, who had rushed over after belatedly learning of Lee Cheonbaek’s calamity, the enemy would never have withdrawn.

“I’ll tear that bastard limb from limb and kill him.”

At the thought of the Red Wind Band Leader, Lee Seowol shook her head.

In a life-and-death duel between Peak masters, Cheol Mubaek had the edge.

They had already clashed once, and Pung Yang had retreated with a minor internal injury.

*But an opportunity like that will never come again.*

The Mount Heng Sword Sect had always gathered information on the mounted bandits of the northern plateau and remained constantly on alert.

There were dozens of mounted-bandit groups on the plateau, but among them, the Red Wind Band led by Pung Yang had grown frighteningly fast.

A man particularly strong and meticulous even among the plateau’s chieftains.

That man was Pung Yang.

*There’s no way someone like that would engage Uncle Cheol in a life-and-death duel. If Uncle Cheol rashly tried to confront him, Pung Yang would turn the tables on him instead.*

Lee Seowol turned toward Cheol Mubaek.

“Uncle Cheol, could you tell me once more about Pung Yang’s martial arts?”

“Early Peak. His saber arts and throwing-knife techniques had reached a high realm. However…”

A deep furrow formed between Cheol Mubaek’s brows.

“Every one of his forms was thoroughly insidious. I suspect he has learned demonic, heterodox martial arts.”

“Demonic, heterodox arts…”

After the Great Faction War, belonging to the evil and heretical paths was tantamount to death in the Central Plains. Unorthodox factions might present themselves as orthodox, but no one openly proclaimed themselves unorthodox.

“For now, it’s only a suspicion. We’ll know if we clash again.”

“I trust you, Uncle Cheol. But don’t underestimate the Red Wind Band Leader. He has any number of subordinates he can sacrifice in his place.”

With enemies bearing down from both directions, their combined force was close to three hundred strong.

Meanwhile, even after gathering every martial artist stationed at its branches, the Mount Heng Sword Sect had less than half that number.

Given the situation, morale was low among both the ordinary martial artists and the newly appointed senior members.

“Seowol. May I say something?”

These were the words of a benefactor who had risked his life out of loyalty to his dead friend. Lee Seowol bowed politely.

“I’ll take your words to heart.”

Cheol Mubaek spoke heavily.

“Leave.”

It was a single word laden with meaning.

But there was not the slightest hesitation in Lee Seowol’s answer.

“I’m sorry.”

“It isn’t too late. You must survive.”

“It isn’t over yet. And I will survive.”

“If you thought Cheonbaek would have wanted this…”

“Uncle.”

At her resolute voice, Cheol Mubaek closed his mouth. Firm determination filled Lee Seowol’s clear eyes.

“This is what I wanted. As the Sect Leader of the Mount Heng Sword Sect.”

“Whew…”

Cheol Mubaek let out a sigh instead of answering.

“I’m already deeply indebted to you, Uncle. Even if you leave now, I won’t resent you.”

“Do you really need to hear my answer before you’ll be satisfied?”

Lee Seowol shook her head. Cheol Mubaek had cherished her like his own child since she was young. In some ways, he had been more of a father to her than her actual father.

“I will never forget this debt. Uncle Cheol, you are the benefactor of both me and the Mount Heng Sword Sect.”

“I’ve watched you since you were little, but… you really are a sly child.”

“I was sly when I was young. Now I’m a ruthless bitch.”

Watching Lee Seowol smile faintly, Cheol Mubaek could only continue to sigh deeply.

“Do we have any chance of winning?”

“If we fought now? Ten percent.”

“What?”

“But if reinforcements arrive, fifty percent. More than that.”

“Reinforcements? From the Jin Family of Taiyuan?”

“A messenger pigeon sent by the Lower District Sect’s Jeongyang Branch arrived four hours ago.”

“How many are there? One hundred? Two hundred?”

“Four. One of them is the Heaven Shaking Sword, Jin Mukyung, and another is…”

Lee Seowol let out a wry laugh, reminded of her ill-fated connection with him.

“The Sleeping Dragon of Shanxi, Jin Taekyung.”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 111`.

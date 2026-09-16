# Master Edit Task — Chapter 110

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
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 살기     | **killing intent**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 대주     | **Squad Leader** / **Commander**             |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 귀환자 | **Returnee** | System Title |
| 승부사 | **Gambler** | System Title |
| 수문각 | **Gate Guard Pavilion** | Jin Family gate complex at the main entrance. |
| 주모 | **Lady of the House** | Title used in Wipeng's remark that Jin Wikyung lacks a wife or household mistress. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

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
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 소월 | 철검대주 | sect_leader_to_subordinate | Iron Sword Squad Leader | formal-commanding | Lee Seowol addresses him while issuing her final instruction about her title. |
| 소월 | 수문각주 | sect_leader_to_subordinate | Master of the Gatekeeper Pavilion | formal-commanding | Lee Seowol addresses him while asserting her authority as Sect Leader. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
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

#### Chapter 108 tail (verified mastered)

…
A deathly silence fell. Hyuk Mujin, one eye bruised deep blue, whispered to me, “Am I actually alive right now?” “Yeah. Your breath against my ear is giving me goose bumps, so move away.” “Just a moment ago, I was wondering how anyone could get beaten like a dog that badly, but now…” *Gulp.* Hyuk Mujin swallowed dryly, his gaze fixed on the fallen leader. “Hng… Hng…” With all four limbs broken and his dantian destroyed, the man struggled for breath. If he received proper care, he might be able to walk again, but his life as a martial artist was over. The Level window I sensed through Qi Sense was proof. > **System** > > **Level 2 — Lee Sam** *The dung flies those watchers used as Familiars were Level 1, if I remember right.* The culprit who had reduced a Level 25 martial artist—one who had once been close to First Rate—to a living corpse kept stealing glances in our direction. “Captain, please save me. I think the Second Young Master is still short on blood.” “Stop talking nonsense and move that guy somewhere suitable. He’ll die if you leave him like that.” “Doesn’t he deserve to die? They were selling perfectly innocent commoners.” “Move him anyway. He’s still alive.” One of the greatest sources of dissonance I had felt while moving between Murim and the modern world was the issue of killing people. For twenty-seven years, I had lived in a society governed by law and order. I had trained to kill enemies with bladed weapons, but my targets had been monsters, not living humans. *I was sure that was the case…* Now I couldn’t even remember how many people I had killed. Even after realizing that the enemies who had died by my hand might have been real people rather than NPCs, I hadn’t felt much guilt. *They were enemies. They were trying to kill me too.* I didn’t know whether it was because I had lived as a Hunter or because I had grown accustomed to Murim’s ways. I was only surprised by my own numbness and the simplicity of my self-justification. *For now, this much should be fine.* I was living in two completely different worlds. I couldn’t afford to play at being some half-baked Buddhist disciple. I shook off the thoughts clinging to me and approached the men cowering on the ground. “Eek!” “Uaaagh! Save me, Boss!” “You bastards make a fuss even when I’m trying to save you. Hold still.” I untied the ropes, and the Five-Colored Ghosts were free. They stood on trembling legs. “Th-thank you.” “We’ll serve you as our Benefactor for the rest of our lives!” “Like hell you will. Anyway, how did you end up getting caught by men like these? All five of you at once?” The Five-Colored Ghosts were small, but they were grown men, at least in name. They had been strong enough to commit banditry alongside the Heavenly Axe. “Um, well…” “…?” What was wrong with these guys? Sensing something off in their hesitation, I grabbed the nearest human trafficker by the collar and hauled him up. “How did you catch them?” “We caught them trying to steal our money pouches in the marketplace.” “…” What the hell, these Ten-Colored Ghosts. I thought they had quit being bandits and might have taken up farming, but they had only changed occupations? “Explain yourselves.” Under my piercing stare, the five men’s eyes darted around. “W-well…” “Boss, this is the only kind of thing people like us ever learned to do.” “E-even so, we only started recently!” “We tried to work honestly, but nothing went right… We said we’d pull just one job and get out, but then…” “If we’d known they were mounted bandits, we never would’ve touched them. We’re victims too. Boss, please forgive us just this once!” As I wondered what to do with these men, a familiar word made me pause. “What did you say?” “We’ll live honestly if you forgive us just one more time!” “No, not that. What did they say?” “Ah, do you mean the mounted-bandit group?” “Yeah. That.” “We only found out after they caught us. Some ruffians were throwing silver around at a pleasure house, so we followed them… Turns out they were from the Red Wind Band, infamous for their viciousness even among mounted bandits.” “The Red Wind Band? Are you sure?” “Yes. I heard it clearly with my own ears. Right?” The others began eagerly adding their own pieces. “They also said they were leaving at first light tomorrow.” “They said they’d have to ride without stopping to reach Saneum. They were even worried they might lose their heads if they arrived late.” “So that’s how it is.” Yesterday, and now today. Running into mounted bandits from the Red Wind Band two days in a row was already an uncanny coincidence. On top of that, Saneum was close to Eung-hyeon, where the Mount Heng Sword Sect’s headquarters stood. “Are these men telling the truth?” The human trafficker whose collar I held in my right hand—or rather, the mounted bandit from the Red Wind Band—nodded, trembling. At that moment— *Shriek!* A hawk landed in front of the shrine with a sharp cry. A small cylinder tied to its ankle caught my eye. *A messenger eagle.* Things were taking a strange turn. [^1]: A nickname meaning “Five-Colored Ghosts.”

#### Chapter 109 tail (verified mastered)

…
up the hill to report answered him. “We killed all the men and gathered the women and children together.” “Why?” “Pardon? Why, it’s the tradition of Gaoyuan…” Any male taller than a cartwheel—even a child—was killed without mercy, while the women were taken or sold as slaves. It was a tradition—or something close to one—passed down from the nomads. At the mounted bandit’s words, Pung Yang quietly crooked one finger. “Come closer.” The mounted bandit approached hesitantly and asked carefully, “Leader, did I perhaps make some serious mistake…” “Who were you with before?” “Until recently, I was the deputy leader of the Earth Tiger Band.” “The Earth Tiger Band? Ah, I remember. You were their deputy leader.” “Y-yes! I was so impressed by your formidable martial arts and noble character that I swore to become your loyal subordinate!” Pung Yang scratched his nose with an ambiguous expression. *Was that so?* All he remembered was killing a piece of trash in a single strike—the man who had swaggered around calling himself a bandit leader while commanding some thirty subordinates. “My memory differs a little, but thank you anyway.” “Not at all! It’s an honor!” “Still, whatever the Earth Tiger Band may have been like, things are different in the Red Wind Band. Petty matters like the traditions of Gaoyuan, for instance.” “Ah, I didn’t realize.” “My orders as leader take priority. Do you understand?” “I’ll keep that in mind—over and over again!” “Those fellows probably followed Gaoyuan’s traditions because they didn’t know any better. They all joined recently, just like you. Would you go and tell them what I want?” “Your command is my law. I won’t leave a single one alive.” The mounted bandit even gave an awkward military salute, though there was nothing military about a mounted bandit. Pung Yang waved him away. “Yes, go on.” “Yes, Leader!” Pung Yang watched him ride away, then suddenly flicked his sleeve. *Whoosh!* A streak of light split the air and pierced its target ten jang—about thirty meters—away. *Thnk! Thud.* The horse kept galloping. It had no idea that its rider was already dead, his foot caught in the stirrup and his body being battered to pieces against the ground. “Go and tell them. There are no prisoners. Kill them all and burn the place.” “Yes, Leader.” Not long after Pung Yang’s subordinate departed, the entire manor was engulfed in flames. As he watched the signboard burn away in an instant, a faint smile touched the corners of his mouth. Mount Heng Sword Sect, Datong Branch. It was the moment the Red Wind Band crossed Gaoyuan once more. * * * The messenger’s report left the people arguing in the spacious main hall breathless. “They’ve broken through Datong!” “A-already?” “What about the Datong Branch? What happened to the men who went out to stand guard?” “Wiped out. They were all wiped out. The Datong Branch was reduced to ashes, and there wasn’t a single survivor.” “What?” “Could the report be wrong? They must have suffered heavy losses last time, so how could they have come this far so quickly…?” “They appear to have absorbed another mounted-bandit group. At least two hundred men—possibly more.” “Is that certain?” “Yes, without a doubt.” “Th-then when will they reach us…?” “If they’re fast, the attack will begin within a day. At the latest, we expect it within two days.” “We’re finished.” The muttered words were not much different from what most of the people gathered there were thinking. There were a little over ten of them, all senior figures holding important positions in the Mount Heng Sword Sect. Yet every one of them was already turning the word *defeat* over in their minds. “Iron Sword Squad Leader, are you confident in this fight?” “Why are you asking me, when you’re a Pavilion Leader? Am I the only martial artist here?” They were squad leaders, hall leaders, and pavilion leaders of the great Mount Heng Sword Sect. There had been a time when he had desperately wanted to rise to that position. Once upon a time, that was. To hell with the great Mount Heng Sword Sect. What good is a promotion now, with the sect in this state? *We were already on the verge of collapse, and now a mounted-bandit group has come to raise hell. Let’s see… If we scrape together everyone we have left, we might reach a hundred.* The war with the Jin Family of Taiyuan had cost them nearly eighty percent of their strength. They had lost the elite martial artists they had painstakingly trained and the seasoned senior figures who had weathered countless trials in the martial world. Most painful of all was the loss of the Peak masters who embodied the sect’s power—and of its financial resources. “Damn it. If only the Sect Leader were still alive.” Lee Cheonbaek had started as a mere wandering martial artist and built the Mount Heng Sword Sect into what it was now. With his martial arts and resourcefulness, he could have turned this situation around. But the Blood Wolf Sword, Lee Cheonbaek, was already dead. Of his bloodline, only one person remained alive. “To think we have to serve some little girl who isn’t even twenty as Sect Leader at a time like this.” The moment someone spat out those words in anger— *Boom!* The tightly closed doors of the main hall exploded.

## Korean source

```text
＃110화



쾅!

굉음과 함께 나타난 것은 장대한 체구의 중년인이었다.

억세게 뻗친 눈썹 아래, 성난 맹수처럼 호목(虎目)을 부릅뜬 그가 좌중을 쓸어 본다.

“방금 헛소리를 지껄인 자가 누구냐?”

이 자리에 모인 이들은 모두 항산검문의 중진.

전임자만큼은 아니어도 일류의 무공과 일정 이상의 경륜을 지닌 이들이다. 그러나 그들조차도 목을 움츠리고 시선을 피하기 바빴다.

눈앞의 중년인은 그럴 자격이 충분히 있는 사람이니까.

‘제길, 하필이면 항산호(恒山虎)한테…….’

호사가들이 이르길, 항산에는 두 마리 맹수가 산다고 했다.

혈랑검과 항산호. 절친한 벗이자 서로가 넘어야 할 벽.

중년인, 철무백은 이미 수십 년 전부터 항산의 호랑이라 불리는 절정 고수였다.

“어느 놈이냐 물었다!”

그 포효 같은 외침에 항산검문의 중진들은 전신의 털이 쭈뼛 곤두섰다.

철무백이 한번 꼭지가 돌면 친우였던 이천백조차 자리를 피한다고 했다. 하물며 무공과 연배에서 한참 뒤처지는 그들이니 두말할 것도 없다.

“일치단결하여 저 말 도적놈들을 몰아내도 모자랄 판에, 감히 천백의 유지를 어기고 역심을 품어?”

화염이 쏟아질 듯한 눈빛에 항산검문의 중진들은 불에 덴 것처럼 화들짝 놀랐다.

“처, 철 대협. 오해십니다.”

“저희가 어찌 감히 역심을 품겠습니까.”

“그럼 내 나이가 늙어 귀가 어두워진 것이냐?”

그 순간, 대전 안의 사람들은 갈증을 느꼈다. 단순한 착각이 아니라 철무백이 뿜어내는 가공할 만한 열양지기(熱陽地氣) 때문이었다.

‘이런 미친.’

‘도대체 뭘 얼마나 처먹었기에 이런 무지막지한 공력이…….’

단순히 가까이 있는 것만으로도 숨이 막히고 땀이 줄줄 흐른다. 항산호. 약관 무렵부터 광활한 산맥의 어딘가에서 홀로 무공을 익혔다는 절정 고수의 진면목이 드러나는 순간이다.

“훅, 후우욱.”

“대협, 부디 고정하십, 후욱.”

거친 숨을 몰아쉬는 항산검문의 중진들, 그리고 용서의 기미 없이 그들을 노려보는 절정 고수.

대전 안의 공기가 용암처럼 들끓어 오르려던 그때였다.

“철 숙부, 더워요.”

시냇물처럼 청량한 목소리와 철무백의 소매를 잡아당기는 희고 가느다란 손가락. 그와 동시에 분노로 주름져 있던 철무백의 미간이 누군가 잡아당긴 것처럼 쫙 펴졌다.

“마, 많이 더웠느냐?”

“네, 숨도 못 쉬겠어요.”

“이런, 내가 미처 네 생각을 못 했구나. 지금은 어떠하냐?”

“한결 나아졌어요. 고마워요, 철 숙부.”

“그런 말은 하지 말거라. 소월이 너를 지키는 게 내 할 일인 것을.”

철무백의 강대한 열양지기가 사그라든다.

그제야 곳곳에서 참았던 숨이 터져 나왔다. 땀으로 흠뻑 젖은 사람들은 정신을 차리고 난 뒤에 철무백이 혼자가 아님을 깨달았다.

“아, 아가씨.”

“아가씨를 뵙습니다.”

황급히 자리에서 일어나 예의를 표하는 중진들의 모습에 눈썹을 치켜뜨는 철무백. 그러나 ‘아가씨’가 한발 빨랐다.

“철검대주님, 수문각주님. 두 분께 마지막으로 말씀드릴게요.”

철무백의 거구에 가려져 보이지 않던 그녀가 모습을 드러낸다. 마르고 늘씬한 체구. 푸른색 궁장 밑단이 바닥을 스칠 때마다 사각거렸다.

“호칭을 바꾸세요. 아가씨가 아니라 문주님, 으로.”

서리가 내려앉은 듯한 그녀의 눈빛을 마주한 사람들은 잠시 잊고 있던 사실 하나를 떠올렸다.

‘아, 그랬지.’

혈랑검 이천백.

이소월은 그의 피를 가장 진하게 이어받은 자식이다.



* * *



나는 승마에 관해서는 문외한이다. 무림에 온 후에야 몇 번 타 본 정도지. 현대에서 승마는 부자들에게만 허락된 귀족 스포츠나 다름없어서 접해 볼 기회가 없었다.

하지만 신체 능력이 워낙 좋은 데다가 잘 훈련된 말을 타고 있어서 그런지, 격렬한 질주 중에도 시스템창을 볼 만큼 여유가 있었다.

‘퀘스트창 오픈.’

띠링.



퀘스트



[어제의 적, 오늘의 동지]

모든 진실이 밝혀진 지금, 항산검문은 적이 아니라 손을 잡아야 할 동지입니다. 곧 다가오는 원단에 그들을 태원진가로 초대하십시오.



등급 : 절정

제한 : 진태경

임무 : 초대장 전달 (미완료)

보상 : ???

실패 : 없음





퀘스트는 유동적이다. 상황에 따라서 돌발 퀘스트가 발생하기도 하고 지금처럼 퀘스트가 갱신되기도 한다.

‘등급 상향 조정이라.’

퀘스트 등급이 일류에서 절정으로 바뀌었다는 것은 항산검문으로 가는 길이 녹록지 않아졌다는 걸 의미했다.

예를 들자면 적풍단이라든지. 혹은 적풍단이라든지. 아마 적풍단…… 됐다. 더 말해 봤자 마음만 아프다.

‘이 동네는 하루하루가 살얼음판이 따로 없네.’

간만에 쉬운 퀘스트 하나 받나 했더니 또 일이 터졌다.

하지만 예전만큼 초조하지 않은 이유는, 진무경이라는 든든한 존재 덕분도 있지만 나 자신이 강해졌기 때문이다.

‘상태창 오픈.’

띠링.



상태창



[Lv.55 진태경]

직업 : 일류 무인

명성 : 1300 (+150)

칭호 : 4개 (칭호 효과 적용 중)

- 귀환자 (모든 능력치 +10)

- 산서잠룡 (모든 능력치 +10, 명성 +100)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 승부사 (일대일 전투 시 전투 관련 능력치 +10%)

근력 : 196 (+25)체력 : 195 (+25)

민첩 : 192 (+25)지력 : 35(+25)

매력 : 35(+25)공력 : 15년

맷집 : 155(+25)

잔여 포인트 : 0





‘크으, 주모.’

혼자 잘 컸다, 잘 컸어.

각각 200포인트에 육박하는 근력, 민첩, 체력은 보기만 해도 배가 부르고, 진무경에게 두들겨 맞으면서 생겨난 맷집도 잘 크고 있다.

‘칭호 옵션 효과도 빵빵하고. 이 정도면 충분해.’

지금까지는 살기 위해 스탯을 올렸다. 퀘스트 하나 진행할 때마다 온갖 위기가 삼각파도처럼 밀려오는데 매력과 지력에 포인트를 투자할 여력이 있었을 리가.

‘지력 올려서 아이큐 180 되면 창을 과학적으로 찌르는 것도 아니고.’

매력도 마찬가지다. 조필이나 대장로가 얼굴 좀 잘생겼다고 살려 줄 것 같진 않거든.

물론 올려 둔다면 나중에 어떤 식으로든 도움이 되겠지만, 당장 목숨이 간당거리는 와중에 비전투 스탯에 투자할 용기가 없었다.

‘이제 내 한목숨 지키는 건 어느 정도 가능하다.’

이번 퀘스트만 끝나면 공력과 비전투 스탯에 신경을 써 볼 생각이다.

안 그래도 조필을 쓰러트리고 얻은 [열화신단]을 포함한 아이템들이 인벤토리에 고이 잠자고 있다.

‘물론 잘못 먹으면 골로 가겠지만.’

그때 선두에서 달려가던 월화가 개울을 발견하고 멈춰 섰다.

“잠시만 쉬어 갈게요. 말들이 너무 지쳐서.”

시간이 얼마나 흘렀을까?

사당에서부터 쉬지 않고 달리다 보니 동이 트고 해가 중천에 걸렸다. 중간에 근력과 체력이 올랐다는 시스템 메시지도 두 번이나 뜰 정도였으니 강행군은 강행군이었던 모양이다.

“후. 엉덩이 아파 죽겠네요. 이럴 줄 알았으면 농부가 아니라 마부 아들로 태어났어야 했는데.”

말이 휴식하는 틈을 타 혁무진이 털썩 주저앉았다. 일행 중 가장 레벨이 떨어지는 녀석이니만큼 체력 소모가 눈에 띄었다.

“힘드냐?”

혁무진이 소매로 이마의 땀을 훔치며 대답했다.

“솔직히 힘들긴 한데…… 이상하게 지난번보다는 훨씬 낫네요.”

“지난번이라니?”

“벌써 잊으셨어요? 정찰 임무 때요.”

“아, 기억난다.”

백호당 소속으로 정찰 임무를 맡았다가 조필을 만나는 바람에 죽을 뻔했던 일. 그때도 분명 말을 끌고 가긴 했었지.

‘나중에는 폭설이 내리는 바람에 말도 버리고 갔지만.’

예전 일을 떠올리자 피식 웃음이 새어 나왔다.

“왜 그러세요?”

“네 생각 나서. 나한테 멋모르고 까불다가 엄청 맞았잖아.”

“……꼭 그렇게 지난 얘기를 들춰내야 속이 후련하세요?”

“물어본 건 너야, 인마.”

“어쨌든, 그때보다는 훨씬 나아진 것 같다고요.”

“그래?”

“네. 정찰 임무 때보다 훨씬 많이 달렸는데 별로 지치지도 않고 그러네요. 말 타는 게 좀 익숙해져서 그런가?”

“그런 걸지도…… 아, 잠깐만.”

“예?”

문득 짚이는 구석이 있어 기감을 끌어올렸다.

띠링. 익숙한 시스템 알림과 함께 어리둥절해하는 혁무진의 얼굴 위로 레벨창이 떠오른다.



[Lv.38 혁무진]



“……엥?”

벌어진 입에서 바람 빠지는 소리가 새어 나온다. 혁무진이 언제부터 레벨이 이렇게 높았지?

‘엄밀히 말해서 엄청나게 높은 건 아니지만.’

녀석과 처음 만났을 때 20레벨에 불과했던 걸 생각하면 장족의 발전이라는 말도 부족하다. 이 정도면 거의 새로 태어난 수준인데?

‘그러고 보면 처음 만난 이후로 꾸준히 올랐던 것 같기도 하고.’

기억을 더듬어 보니 처음보다 또렷하게 떠올릴 수 있었다.

정찰조로 재회했을 때도 그랬고, 틈틈이 기감을 끌어올릴 때마다 옆에 있던 혁무진의 레벨은 1, 2씩 올라 있었다.

그러던 게 어느새 38레벨. 무림에서의 시간으로만 치면 근 두 달 남짓한 시간 동안 두 배 가까이 성장을 이룬 거다.

‘그럼 혹시?’

설마 하는 마음에 혁무진을 뚫어져라 바라봤다.

이 녀석도 나처럼 스탯 포인트를 받는다면? 그걸 내가 대신 분배해 줄 수도 있지 않을까?

‘가능성이 있는 이야기지.’

내가 비슷한 레벨의 헌터나 무인보다 훨씬 강한 걸로 봐서는 시스템 보정 효과가 있는 것 같긴 한데…….

‘한 번 시도해 볼 만해.’

“왜 그러세요? 제 얼굴에 뭐라도 묻었습니까?”

“아니. 그냥 못생겨서.”

“……아, 진짜.”

꿍얼거리는 혁무진의 어깨를 잡고 마음으로 외쳤다.

‘상태창 오픈!’

바로 그 순간.

“뭐 하세요? 어깨 아파요.”

“어, 그래.”

아무 일도 없네. 뭐 하나쯤 뜰 줄 알았는데.

하긴 본캐도 만렙 찍으려면 아직 한참 남았는데 부캐가 웬 말이냐. 그래도 아쉽긴 하다.

‘소리 내서 해 볼까?’

분명히 이상한 놈 취급받겠지만 화장실 다녀와서 손 안 닦는 기분으로 가는 것보단 낫겠지.

나는 슬그머니 혁무진의 등에 손을 살짝, 아주 살짝 가져다 대며 작게 중얼거렸다.

“상태창 오픈.”

“아, 진짜. 아까부터 진짜 왜 이러세요?”

녀석의 말을 무시하고 자리에서 벌떡 일어났다.

기다리던 알림 소리와 함께 시스템창이 떴기 때문이었다.

“이야아, 떴다!”

띠링.



- 퀘스트 조건에 [제한 시간]이 추가되었습니다.

- [22:00:00] 안에 항산검문에 도착하십시오. 늦는다면 돌이킬 수 없게 됩니다.



“이야아…….”

사그라지는 목소리. 흔들리는 눈동자.

‘제한 시간이라니. 뭔 놈의 제한 시간.’

나한테 왜 이러냐, 진짜.

한숨을 푹 내쉬는 내게 눈을 동그랗게 뜬 월화가 물었다.

“진 공자, 어디 아파요?”

“아뇨. 그건 아니고요. 혹시 우리 언제쯤 도착하는지 알 수 있어요?”

“음. 오늘 같은 속도라면 내일 저녁 전에?”

“아.”

지금 정오를 약간 넘긴 시간이니까 꼬박 하루는 넘게 달려야 한단 말이다.

퀘스트창이 변경된 걸 보니 그 제한 시간 안에 적풍단 놈들이 항산검문을 친다는 얘기 같은데…… 이걸 어쩐다?

“이제 슬슬 출발할까요?”

“말들이 지쳤어요. 반 시진은 쉬어야 해요.”

“말들아, 괜찮지? 방금 들으셨어요? 괜찮다고 대답한 거.”

“…….”

그래, 그런 눈으로 볼 줄 알았다.
```

## Current accepted English baseline

```markdown
# Chapter 110

*Bang!*

The person who appeared with the thunderous explosion was a middle-aged man of imposing stature.

Beneath his thick, sharply angled brows, he glared around the room with tiger eyes like an enraged beast.

“Who was the one spouting that nonsense just now?”

Everyone gathered here was a senior figure of the Mount Heng Sword Sect.

Even if they weren’t on their predecessor’s level, they possessed First Rate martial arts and more than enough experience. Yet even they were busy shrinking their necks and avoiding his gaze.

The middle-aged man before them had every right to make them do so.

*Damn it. Of all people, it had to be the Tiger of Mount Heng…*

The storytellers said that two beasts lived on Mount Heng.

The Blood Wolf Sword and the Tiger of Mount Heng. They were close friends, but each was also the wall the other had to overcome.

The middle-aged man, Cheol Mubaek, had been a Peak master known as the tiger of Mount Heng for decades.

“I asked which one of you it was!”

At that roar, the senior figures of the Mount Heng Sword Sect felt every hair on their bodies stand on end.

They said that whenever Cheol Mubaek lost his temper, even his friend Lee Cheonbaek would leave the area. These men were far inferior to him in both martial arts and age, so there was no need to say more.

“We should be united in driving out those mounted bandit bastards, and yet you dare defy Cheonbaek’s final wishes and harbor rebellious intentions?”

Under his gaze, which seemed ready to pour out flames, the senior figures of the Mount Heng Sword Sect flinched as though they had been burned.

“G-Great Hero Cheol. You misunderstand.”

“How could we ever dare harbor rebellious intentions?”

“Then have I grown old enough for my ears to fail me?”

At that moment, everyone inside the main hall felt thirsty. It wasn’t a simple illusion. It was caused by the terrifying Scorching Yang Qi radiating from Cheol Mubaek.

*What the hell?*

*What on earth has he been eating to build up such ridiculous internal energy…?*

Just being near him made it hard to breathe, and sweat poured down their bodies. The Tiger of Mount Heng. This was the moment the true nature of the Peak master who had supposedly trained alone somewhere in the vast mountain range since around the age of twenty revealed itself.

“Haah… Hoo…”

“Great Hero, please calm down… Hah.”

The senior figures of the Mount Heng Sword Sect panted harshly, while the Peak master glared at them without the slightest sign of forgiveness.

The air inside the main hall was about to boil like lava when—

“Uncle Cheol, it’s hot.”

A clear voice like a flowing stream, and slender white fingers tugging at Cheol Mubaek’s sleeve. At the same time, the wrinkles furrowed across his brow in anger smoothed out as though someone had pulled them flat.

“W-Was it very hot?”

“Yes. I can barely breathe.”

“Goodness, I didn’t think of you. How are you now?”

“Much better. Thank you, Uncle Cheol.”

“Don’t say such things. Protecting you, Seowol, is my duty.”

Cheol Mubaek’s powerful Scorching Yang Qi subsided.

Only then did the people throughout the hall finally release the breaths they had been holding. Once they came to their senses, their clothes drenched in sweat, they realized that Cheol Mubaek was not alone.

“Y-Young Lady.”

“We greet Young Lady.”

Cheol Mubaek raised his brows at the senior figures hurriedly standing to show their respect. But the “Young Lady” was faster.

“I’ll tell the two of you one last time, Iron Sword Squad Leader and Master of the Gatekeeper Pavilion.”

The woman who had been hidden behind Cheol Mubaek’s massive frame stepped forward. She was slim and graceful, and the hem of her blue gown rustled whenever it brushed the floor.

“Change how you address me. Not Young Lady. Sect Leader.”

Those who met her frost-cold gaze remembered one fact they had momentarily forgotten.

*Oh. That’s right.*

The Blood Wolf Sword, Lee Cheonbaek.

Lee Seowol was the child in whom his blood ran strongest.

* * *

I knew nothing about horseback riding. After coming to Murim, I had ridden only a few times. In the modern world, horseback riding was practically an aristocratic sport reserved for the rich, so I’d never had the chance to try it.

But perhaps because my physical abilities were so good and I was riding a well-trained horse, I had enough leisure to look at the System Window even during a furious gallop.

*Open Quest Window.*

*Ding.*

> **System**
>
> **Quest**
>
> **Yesterday’s Enemy, Today’s Ally**
>
> Now that all the truth has been revealed, the Mount Heng Sword Sect is not an enemy but an ally you must join hands with. Invite them to the Jin Family of Taiyuan during the upcoming Lunar New Year.
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Deliver the invitation (Incomplete)
>
> **Reward:** ???
>
> **Failure:** None

Quests were fluid. Sometimes sudden Quests appeared depending on the situation, and sometimes, like now, an existing Quest was updated.

*The Grade was raised.*

The Quest Grade changing from First Rate to Peak meant that the road to the Mount Heng Sword Sect had become anything but easy.

For example, the Red Wind Band. Or the Red Wind Band. Probably the Red Wind Band…

Never mind. Thinking about it any more would only hurt.

*Every day in this place is a walk across thin ice.*

I thought I’d finally received an easy Quest for once, but trouble had struck again.

The reason I wasn’t as anxious as before was partly because of the reliable presence of Jin Mukyung, but also because I myself had grown stronger.

*Open Status Window.*

*Ding.*

> **System**
>
> **Status Window**
>
> **Level:** 55 — Jin Taekyung
>
> **Class:** First Rate martial artist
>
> **Fame:** 1,300 (+150)
>
> **Titles:** 4 (Title effects active)
>
> — Returnee (All stats +10)
>
> — Sleeping Dragon of Shanxi (All stats +10, Fame +100)
>
> — Scion of a Prestigious Family (All stats +5, Fame +50)
>
> — Gambler (Combat-related stats +10% in one-on-one combat)
>
> **Strength:** 196 (+25)  
> **Stamina:** 195 (+25)
>
> **Agility:** 192 (+25)  
> **Intelligence:** 35 (+25)
>
> **Charm:** 35 (+25)  
> **Internal energy:** 15 years
>
> **Toughness:** 155 (+25)
>
> **Remaining Points:** 0

*Ahh, barkeep.*

*Look how well I’ve grown. All by myself.*

Strength, Agility, and Stamina were each nearing 200. Just looking at them made me feel full, and my Toughness, born from getting beaten by Jin Mukyung, was growing nicely too.

*The Title bonuses are hefty, too. This should be enough.*

Until now, I had raised my stats just to survive. Every time I advanced a Quest, one crisis after another came crashing down like three waves at once. There was no way I could afford to invest points in Charm or Intelligence.

*Even if I raised my Intelligence enough to reach an IQ of 180, it’s not like I’d start thrusting a spear scientifically.*

Charm was the same. It wasn’t as though Jopil or the Head Elder would spare me just because I was handsome.

Of course, raising them would help me in some way eventually. But with my life hanging by a thread, I hadn’t had the courage to invest in noncombat stats.

*I can protect this one life of mine to some extent now.*

Once this Quest was over, I planned to pay more attention to my internal energy and noncombat stats.

As it happened, the items I had obtained after defeating Jopil—including the Blazing Flame Divine Pill—were sitting untouched in my Inventory.

*Of course, if I screw up taking it, I could wind up dead.*

At that moment, Wolhwa, who had been riding at the front, spotted a stream and stopped.

“We’ll rest for a little while. The horses are too exhausted.”

How much time had passed?

We had ridden without stopping since leaving the shrine; dawn had broken, and now the sun was high overhead. System messages saying my Strength and Stamina had increased had even appeared twice, so it had definitely been a forced march.

“Whew. My butt hurts like hell. If I’d known this would happen, I should’ve been born the son of a coachman instead of a farmer.”

While the horses rested, Hyuk Mujin dropped heavily to the ground. Since he was the lowest-level member of the group, his exhaustion was obvious.

“Is it hard?”

Hyuk Mujin wiped the sweat from his forehead with his sleeve before answering.

“To be honest, it is… But strangely, it’s much better than last time.”

“Last time?”

“You’ve already forgotten? During the scouting mission.”

“Ah, I remember.”

I had nearly died after encountering Jopil while carrying out a scouting mission for White Tiger Hall. We’d taken horses with us then, too.

*Though we ended up abandoning them when the heavy snow came.*

Remembering the past, I let out a quiet laugh.

“What’s wrong?”

“I was thinking about you. You mouthed off to me without knowing what you were doing and got the crap beaten out of you.”

“……Do you really have to dredge up the past to feel better?”

“You’re the one who asked, punk.”

“Anyway, I’m saying it seems much better than back then.”

“Really?”

“Yes. We’ve ridden much farther than during the scouting mission, but I’m not even that tired. Maybe I’m getting used to riding?”

“Maybe… Ah, wait.”

“Hm?”

Something suddenly occurred to me, so I heightened my Qi Sense.

*Ding.*

Along with a familiar system notification, a Level Window appeared over Hyuk Mujin’s bewildered face.

> **System**
>
> **Level:** 38 — Hyuk Mujin

“……Huh?”

A breathy sound escaped his open mouth. When had Hyuk Mujin’s Level gotten this high?

*Strictly speaking, it wasn’t all that high.*

But considering that he had been only Level 20 when we first met, calling it astonishing progress wasn’t enough. At this point, it was practically like he had been reborn.

*Come to think of it, his Level did seem to keep rising after we first met.*

As I searched my memory, the details came back more clearly.

It had been the same when we reunited as a scouting unit. Whenever I heightened my Qi Sense from time to time, Hyuk Mujin’s Level had risen by one or two.

And now he was Level 38. In terms of time spent in Murim, he had nearly doubled his Level in only about two months.

*Then maybe…?*

With a doubtful heart, I stared intently at Hyuk Mujin.

What if he received stat points like I did? Could I distribute them for him?

*It’s possible.*

Judging by how much stronger I was than a Hunter or martial artist of a similar Level, there seemed to be some kind of System enhancement effect…

*It’s worth trying once.*

“Why are you looking at me like that? Do I have something on my face?”

“No. You’re just ugly.”

“……Seriously.”

I grabbed Hyuk Mujin’s shoulder and shouted inwardly.

*Open Status Window!*

At that very moment—

“What are you doing? My shoulder hurts.”

“Oh. Okay.”

Nothing happened. I thought at least something would appear.

Then again, my main character was still far from reaching the Level cap. Why would my alt character get anything? Still, it was disappointing.

*Should I say it out loud?*

They would definitely treat me like some kind of weirdo, but it was better than moving on with the feeling of not washing my hands after using the bathroom.

I stealthily placed my hand against Hyuk Mujin’s back—lightly, very lightly—and muttered under my breath.

“Open Status Window.”

“Seriously. What is wrong with you today?”

Ignoring him, I sprang to my feet.

The system window had appeared with the notification chime I’d been waiting for.

“Yes! There it is!”

*Ding.*

> **System**
>
> The Quest condition **Time Limit** has been added.
>
> Arrive at the Mount Heng Sword Sect within **22:00:00**. If you are late, there will be no going back.

“Yes…”

My voice faded. My eyes began to tremble.

*A time limit? What kind of time limit is this?*

*Why are you doing this to me?*

As I let out a deep sigh, Wolhwa’s eyes widened and she asked,

“Young Master Jin, are you hurt?”

“No, it’s not that. Do you know around when we’ll arrive?”

“Hmm. At today’s pace, before tomorrow evening?”

“Ah.”

It was a little past noon now. That meant we would have to ride for more than an entire day.

Judging by the Quest Window’s change, it seemed the Red Wind Band bastards would attack the Mount Heng Sword Sect within that time limit…

What was I supposed to do?

“Shall we get going soon?”

“The horses are tired. We need to rest for an hour.”

“Horses, you’re all right, aren’t you? You heard that, right? They said they’re fine.”

“……”

Yeah. I knew you’d look at me like that.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 110`.

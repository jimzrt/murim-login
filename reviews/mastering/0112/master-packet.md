# Master Edit Task — Chapter 112

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
| 이소광    | **Lee Seogwang**   |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 내공     | **internal energy**                              |                                                       |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 사제     | **Junior Brother**                           |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 광칠이 | **Gwangchil** | Former mounted-bandit boss who took in Pung Yang and was later killed by a First Rate master. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 수문각 | **Gate Guard Pavilion** | Jin Family gate complex at the main entrance. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 소월 | 수문각주 | sect_leader_to_subordinate | Master of the Gatekeeper Pavilion | formal-commanding | Lee Seowol addresses him while asserting her authority as Sect Leader. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 이소월 | young_martial_artist_to_allied_sect_leader | Young Lady Lee | formal-polite | Taekyung uses 이 소저 while greeting Seowol at the banquet. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |

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

#### Chapter 110 tail (verified mastered)

…
the items I had obtained after defeating Jopil—including the Blazing Flame Divine Pill—were sitting untouched in my Inventory. *Of course, taking it wrong could send me straight to the grave.* Just then, Wolhwa, who had been riding at the front, spotted a stream and pulled to a stop. “We’ll rest for a little while. The horses are too exhausted.” How much time had passed? We had ridden without stopping since leaving the shrine. Dawn had broken, and now the sun hung high overhead. System messages announcing increases to my Strength and Stamina had even appeared twice, so this really had been a forced march. “Whew. My ass is killing me. If I’d known this would happen, I should’ve been born the son of a coachman instead of a farmer.” While the horses rested, Hyuk Mujin dropped heavily to the ground. Since he was the lowest-level member of the group, his exhaustion was obvious. “Having a hard time?” Hyuk Mujin wiped the sweat from his forehead with his sleeve before answering. “Honestly, yes… But strangely enough, it’s much better than last time.” “Last time?” “You’ve already forgotten? During the scouting mission.” “Ah, I remember.” I had nearly died after running into Jopil during a scouting mission for White Tiger Hall. We had taken horses with us then too. *Though we ended up abandoning them when the heavy snow came.* The memory drew a quiet laugh from me. “What’s wrong?” “I was thinking about you. You mouthed off to me without knowing any better and got the crap beaten out of you.” “……Do you really have to dredge up the past to feel better?” “You’re the one who asked, punk.” “Anyway, I’m saying it seems much better than back then.” “Really?” “Yes. We’ve ridden much farther than we did during the scouting mission, but I’m not even that tired. Maybe I’m getting used to riding?” “Maybe… Ah, wait.” “Hm?” Something suddenly occurred to me, so I heightened my Qi Sense. *Ding.* With the familiar System notification, a Level Window appeared over Hyuk Mujin’s bewildered face. > **System** > > **Level:** 38 — Hyuk Mujin “……Huh?” A breathy sound escaped my open mouth. When had Hyuk Mujin’s Level gotten this high? *Strictly speaking, it wasn’t all that high.* But considering that he had been only Level 20 when we first met, calling it astonishing progress wasn’t enough. At this point, it was practically like he had been reborn. *Come to think of it, his Level has been rising steadily ever since we met.* As I searched my memory, the details came back more clearly. It had been the same when we reunited as a scouting unit. Whenever I heightened my Qi Sense from time to time, Hyuk Mujin’s Level had risen by one or two. Now he was Level 38. In terms of time spent in Murim, he had nearly doubled his Level in just over two months. *Then maybe…?* With a doubtful heart, I stared intently at Hyuk Mujin. What if he received stat points like I did? Could I distribute them for him? *It’s possible.* Judging by how much stronger I was than a Hunter or martial artist of a similar Level, there seemed to be some kind of System enhancement effect… *It’s worth trying once.* “Why are you staring at me like that? Is there something on my face?” “No. You’re just ugly.” “……Seriously.” I grabbed Hyuk Mujin by the shoulder and shouted inwardly. *Open Status Window!* At that very moment— “What are you doing? My shoulder hurts.” “Oh. Okay.” Nothing happened. I thought at least something would appear. Then again, my main character was still far from reaching the Level cap. Why would my alt character get anything? Still, it was disappointing. *Should I try saying it out loud?* They would definitely treat me like some kind of weirdo, but it was better than moving on with the feeling of not washing my hands after using the bathroom. I stealthily placed my hand against Hyuk Mujin’s back—lightly, very lightly—and muttered under my breath. “Open Status Window.” “Seriously, what has gotten into you today?” I ignored him and shot to my feet. The notification I had been waiting for chimed, and a System Window appeared. “Yes! There it is!” *Ding.* > **System** > > The Quest condition **Time Limit** has been added. > > Arrive at the Mount Heng Sword Sect within **22:00:00**. If you are late, there will be no turning back. “Yes…” My voice died away. My eyes trembled. *A time limit? What the hell kind of time limit is this?* *Why are you doing this to me? Seriously.* As I let out a deep sigh, Wolhwa’s eyes widened and she asked, “Young Master Jin, are you hurt?” “No, it’s not that. Do you know around when we’ll arrive?” “Hmm. At today’s pace, before tomorrow evening?” “Ah.” It was a little past noon now. That meant we still had more than a full day’s ride ahead of us. Judging by the Quest Window’s change, it seemed the Red Wind Band bastards would attack the Mount Heng Sword Sect within that time limit… What was I supposed to do? “Shall we get going soon?” “The horses are tired. They need to rest for half a shichen.” “Horses, you’re fine, aren’t you? You heard that, right? They said they’re fine.” “……” Yeah. I knew you’d look at me like that.

#### Chapter 111 tail (verified mastered)

…
again.”* *“The Jin Family of Taiyuan is strong even without the Family Head and the Second Young Master. Please reconsider.”* *“No. My decision has already been made.”* *“Then make sure you win. Become strong enough that no one in Shanxi can even open their mouth about a scandal involving me.”* *“…If you had been a man, I would have made you the Young Sect Leader.”* *“I’m glad I was born a woman. I have no interest in being this sect’s Young Sect Leader.”* Her fears soon became reality. Had even a fortnight passed before Lee Seogeun returned as a cold corpse? Not long after, she lost Lee Cheonbaek. In the end, even her eldest brother, Lee Seogwang, was gone. *Now I’m alone.* And so, the Blood Wolf Sword Lee Cheonbaek’s last surviving blood relative became the new Sect Leader. As she silently gazed at the burial mounds, a warm palm gently caressed her shoulder. “I’m sorry. I should have come sooner…” “Uncle Cheol, please don’t say that. If you hadn’t come, our sect wouldn’t have been able to hold out this long.” Under the Red Wind Band’s fierce assault, the Mount Heng Sword Sect had been helplessly driven back. If not for the Peak master known as the Tiger of Mount Heng, who had rushed over after belatedly learning of Lee Cheonbaek’s calamity, the enemy would never have withdrawn. “I’ll tear that bastard limb from limb and kill him.” At the thought of the Red Wind Band Leader, Lee Seowol shook her head. In a life-and-death duel between Peak masters, Cheol Mubaek had the edge. They had already clashed once, and Pung Yang had retreated with a minor internal injury. *But an opportunity like that will never come again.* The Mount Heng Sword Sect had always gathered information on the mounted bandits of northern Gaoyuan and remained constantly on alert. There were dozens of mounted-bandit groups in Gaoyuan, but among them, the Red Wind Band led by Pung Yang had grown frighteningly fast. A man particularly strong and meticulous even among Gaoyuan’s chieftains. That man was Pung Yang. *There’s no way someone like that would engage Uncle Cheol in a life-and-death duel. If Uncle Cheol rashly tried to confront him, Pung Yang would turn the tables on him instead.* Lee Seowol turned toward Cheol Mubaek. “Uncle Cheol, could you tell me once more about Pung Yang’s martial arts?” “Early Peak. His saber arts and throwing-knife techniques had reached a high realm. However…” A deep furrow formed between Cheol Mubaek’s brows. “Every one of his forms was thoroughly insidious. I suspect he has learned demonic, heterodox martial arts.” “Demonic, heterodox arts…” Ever since the Great Faction War, practicing demonic, heterodox arts had become synonymous with death in the Central Plains. Unorthodox factions might present themselves as orthodox, but no one openly declared themselves unorthodox. “For now, it’s only a suspicion. We’ll know if we clash again.” “I trust you, Uncle Cheol. But don’t underestimate the Red Wind Band Leader. He has any number of subordinates he can sacrifice in his place.” With enemies bearing down from both directions, their combined force was close to three hundred strong. Meanwhile, even after gathering every martial artist stationed at its branches, the Mount Heng Sword Sect had less than half that number. Given the situation, morale was low among both the ordinary martial artists and the newly appointed senior members. “Seowol. May I say something?” These were the words of a benefactor who had risked his life out of loyalty to his dead friend. Lee Seowol bowed politely. “I’ll take your words to heart.” Cheol Mubaek spoke heavily. “Leave.” It was a single word laden with meaning. But there was not the slightest hesitation in Lee Seowol’s answer. “I’m sorry.” “It isn’t too late. You must survive.” “It isn’t over yet. And I will survive.” “If you thought Cheonbaek would have wanted this…” “Uncle.” At her resolute voice, Cheol Mubaek closed his mouth. Firm determination filled Lee Seowol’s clear eyes. “This is what I wanted. As the Sect Leader of the Mount Heng Sword Sect.” “Whew…” Cheol Mubaek let out a sigh instead of answering. “I’m already deeply indebted to you, Uncle. Even if you leave now, I won’t resent you.” “Do you really need to hear my answer before you’ll be satisfied?” Lee Seowol shook her head. Cheol Mubaek had cherished her like his own child since she was young. In some ways, he had been more of a father to her than her actual father. “I will never forget this debt. Uncle Cheol, you are the benefactor of both me and the Mount Heng Sword Sect.” “I’ve watched you since you were little, but… you really are a sly child.” “I was sly when I was young. Now I’m a ruthless bitch.” Watching Lee Seowol smile faintly, Cheol Mubaek could only continue to sigh deeply. “Do we have any chance of winning?” “If we fought now? Ten percent.” “What?” “But if reinforcements arrive, fifty percent. More than that.” “Reinforcements? From the Jin Family of Taiyuan?” “A messenger pigeon from the Lower District Sect’s Jeongyang Branch arrived two *shichen* ago.” “How many are coming? A hundred? Two hundred?” “Four. One of them is the Heaven Shaking Sword, Jin Mukyung, and another is…” Lee Seowol let out a wry laugh, reminded of her ill-fated connection with him. “The Sleeping Dragon of Shanxi, Jin Taekyung.”

## Korean source

```text
＃112화



마적이 백주대낮에 대로를 활보한다?

평소라면 결코 있을 수 없는 일이다. 가장 먼저 인근의 무림 문파가 나설 것이고 그다음은 관아의 병졸들이 제압할 것이다.

그러나 마적들의 숫자가 수백에 달한다면, 그들을 토벌해야 할 무림 문파조차 압도한다면 관아의 벼슬아치도 눈을 감고 귀를 막을 수밖에 없다.

바로 지금처럼.

“저, 저놈들 마적 아니여?”

“놈이라니, 자네 목숨이 세 개쯤 되나? 그 악명 높다는 적풍단이잖아.”

“그 적풍단? 얼마 전에 항산검문이랑 붙어서 깨진 것 아니었나?”

“그런 줄 알았지. 한데 이번에는 좀 다른가 보더라고. 벌써 저잣거리에 항산검문이 멸문지화를 면치 못할 거라는 소문이 파다해.”

“그래도 깜냥이 있는데 설마하니 마적들 따위한테…….”

“어허, 그 입! 맨 앞에 가는 저 사내가 풍양이라고, 적풍단 두목인데 절정 고수라더군.”

“뭣이, 절정 고수?”

“그래, 마적이라고 무시할 게 못 된다니까. 듣기로는 무공만 강한 게 아니라 머리도 아주 비상하다던데.”

양민들의 두려움 섞인 웅성거림이 풍양과 휘하 마적들의 귓속을 파고들었다.

풍양의 오른편에서 말을 몰던 수하가 넌지시 말을 건넸다.

“저놈들의 주둥이를 찢어 놓을까요?”

“그리하고 싶으냐?”

“단주께서 허락해 주신다면 저 두 놈부터 처리한 다음 마을 전체를 불바다로 만들지요.”

“늙은이들은 죽이고, 젊은 놈들은 사로잡고, 여인들은 겁탈하겠다?”

“흐흐, 저 같은 놈들한테야 늘 하던 일 아닙니까. 어차피 항산검문 놈들은 지금쯤 겁을 잔뜩 집어먹고 담벼락 뒤에 숨어 있을 터인데.”

“그렇겠지. 모든 힘을 끌어모은 일전을 준비 중일 것이다.”

“그래 봤자 계란으로 바위 치깁니다. 단주께서 항산검문 놈들을 쓸어 버리고 그 자리를 차지하시는 건 기정사실이죠.”

“그래서 허락하지 않는 것이다.”

“예?”

풍양은 어리둥절한 수하의 반응에 너털웃음을 터트렸다.

하나같이 생각이 짧고 천성이 잔인하다. 그래서 마적이 된 것이고, 풍양이 그들을 곁에 두는 이유이기도 했다.

‘다루기가 쉬우니까.’

웃음을 그친 그가 입을 뗐다.

“대동지부를 몰살시킨 것은 전쟁의 일부다. 그러나 지금 양민들을 건드렸다가는 태원진가가 끼어들 구실을 만들어 주는 것밖에 안 돼.”

“그놈들이 산서성의 주인이라도 된답니까?”

“아직은 아니지만 머지않아 그리되겠지. 그전에 항산검문을 집어삼키고 개처럼 넙죽 엎드려 있어야 하지 않겠느냐?”

“저어, 단주님 말씀을 의심하는 건 아닙니다만…… 태원진가 같은 정파 놈들이 우리 같은 마적들을 좋게 보겠습니까?”

“마적? 누가 마적이냐?”

“예?”

“지난번에 보니 항산검문주의 미색(美色)이 대단하더구나.”

눈을 껌뻑거리던 풍양의 수하는 마침내 뜻을 알아차리고 입꼬리를 말아 올렸다.

“혼기가 꽉 찼으니 지아비를 맞이해야 하겠군요.”

“멸문지화와 혼인. 둘 중 하나를 택해야겠지.”

“그럼 적풍단은……?”

“알맹이를 취하고 껍데기는 뒤집어써야지. 어디 보자, 다른 놈들에 비해 네가 그나마 얼굴이 멀쩡하니 수문각주를 시켜 주마.”

“으하하! 목숨을 다 바쳐 충성하겠습니다.”

수하의 웃음소리를 들으며 풍양은 고삐를 움켜쥐었다.

‘마침내 여기까지 왔다.’

냉철한 성격의 소유자인 그였지만 야망을 향해 한 걸음 다가섰다는 생각에 가슴이 뛰었다.

오래전의 기억이 새록새록 떠올라 눈앞을 스친다.

‘벌써 이십 년이 훌쩍 넘었군.’

마적이 되는 길은 생각 이상으로 쉽고 간단했다. 제 발로 찾아가거나, 잡히거나. 풍양의 경우에는 후자였다.

어린 시절 죄를 지어 관아로 압송되어 가던 도중에 마적단의 습격을 받은 것이 인생의 전환점이었다.



‘두목, 여기 어린놈도 있는데요?’

‘응? 비쩍 곯아서 팔아 봤자 몇 푼 받지도 못하겠네. 꼬마야, 소매치기라도 하다가 걸렸냐?’

‘아뇨. 사람을 죽여서요.’

‘사람을 죽였다고? 네 나이가 몇인데?’

‘열셋이요.’

‘죽인 이유는?’

‘사흘 동안 굶었는데 왕초가 만두를…….’

‘만두? 동냥질한 걸 뺏긴 거냐? 그럼 눈 돌아갈 만하지.’

‘그게 아니라요. 배는 고프고, 동냥질할 힘도 없고. 앞에서는 만두를 먹으니까.’

‘……그래서 죽였다?’

‘뺏어 먹는 게 빠를 것 같아서요.’

‘야, 이놈 풀어 주고 뭐라도 먹여. 오늘부터 우리 식구다.’



풍양은 그날부로 마적이 됐다. 천애 고아로 유리걸식하던 그는 눈치가 비상했고 머리 회전도 빨랐다.

사흘에 한 끼를 먹을까 말까 했던 과거에 비하면 마적 생활은 풍요로웠다.

약탈? 살인? 고작 열세 살에 만두를 먹고 싶다는 이유로 살인을 저질렀던 풍양에게는 당연히 해야 할 일에 불과했다.



‘허 참, 내가 마적질만 십 년 넘게 했는데 너 같은 놈은 처음 본다. 죄책감이라는 게 없는 놈 같아.’

‘왜요? 전 마적이잖아요.’

‘자식이. 보통은 그게 아니라니까. 차차 익숙해지는 거지, 처음부터 능숙한 놈은 없다고.’

‘두목도 그러셨어요? 전 쉽던데.’

‘쉽다, 쉽다라……. 이거 범 새끼를 키우는 게 아닌가 싶긴 한데, 나한테 무공 한 수 배워 볼 테냐?’

‘무공이요?’

‘그래, 무공. 너야 아직 어린 나이니까 근골과 무재만 좀 받쳐 준다면 충분히 고수가 될 수 있을 게다.’

‘그럼 오늘부터 사부라고 부를게요.’

‘사제지간은 염병, 됐으니까 지금처럼만 해.’



사제지간을 맺지 않은 건 잘한 일이었다. 일 년 후, 두목은 일류 고수에게 목이 잘려 죽었고 풍양은 새로운 마적단에 둥지를 틀었다.



‘광칠이 밑에 있었다고?’

‘예. 배불리 먹여 주시기만 하면 충성을 바치겠습니다.’

‘눈치는 제법 있어 보이는군. 어린놈이라고 봐주는 거 없으니까 알아서 잘 따라와라.’



고원은 치열했다. 상단을 잘못 건드렸다가 마적단 전체가 몰살되는 일도 있었고 마적단들끼리의 알력 다툼도 끊이질 않았다. 그러나 풍양은 매번 살아남았고, 점점 강해졌다.

그의 나이 이립(而立)이 되었을 때, 무공은 일류에 접어들었고 제법 규모 있는 마적단의 조장 자리를 꿰찰 수 있었다.

‘하지만 딱 거기까지였지.’

힘의 법칙은 어디에나 적용되는 법.

고원도 결국 강자가 지배하는 무림의 일부분이었다.

풍양에게는 원대한 야망과 뛰어난 머리가 있었지만, 우두머리에 걸맞은 무력을 갖추지는 못했다.

‘삼류 무공의 한계.’

풍양의 무재는 뛰어났다.

어린 시절 명문 정파에 입문하여 훌륭한 내공심법과 무공을 익혔다면 진즉 절정의 벽을 넘어섰을지도 모른다.

그러나 거지 소굴에서 자라고 고원의 마적들에게 삼류 무공을 배운 그의 한계는 명확했다.

‘천운(天運)이 따르지 않았다면 지금도 제자리걸음이었겠지.’

풍양의 입가에 진한 웃음이 맺혔다.

삼 년 전, 그날을 기점으로 풍양의 인생은 송두리째 바뀌었다. 마적단의 일개 조장에서 고원의 한 축을 움직이는 적풍단의 단주, 그리고 이제는 무림 문파를 집어삼킬 차례다.

“단주!”

수하의 외침에 풍양은 상념에서 깨어났다. 저 멀리, 성벽처럼 높게 쌓아 올린 돌담이 마침내 모습을 드러내고 있었다.

‘항산검문.’

자신과 적풍단의 새로운 보금자리를 바라보던 풍양의 시선에 한 사람이 들어왔다. 멀리 떨어진 거리에서도 느껴지는 불같은 기세.

‘항산호 철무백.’

항산검문을 취하기 위해서는 반드시 넘어야 할 벽.

비록 지난번에는 약간의 손해를 보고 물러났지만…….

‘오늘은 다르지.’

풍양은 무의식적으로 품 안을 더듬었다. 단단한 목갑을 확인한 그의 웃음이 더더욱 진해졌다.

“단주, 명령을.”

“포위해라. 개미 새끼 한 마리 빠져나가지 못하도록. 그다음에 사자를 보내.”

멸문과 혼인.

항산검문에게 주어진 선택지는 두 개뿐이다.

“오늘 해가 지기 전에 항산검문을 손에 넣을 것이다.”



* * *



“놈들이 본 문을 빈틈없이 에워쌌습니다!”

“그 숫자가 이백이 훌쩍 넘어갑니다!”

“문주, 부디 결단을.”

상석에 앉아 있던 이소월은 침착한 얼굴로 입을 열었다.

“병력 배치는 끝났나요?”

“백여 명 중 절반은 문을 막고 나머지는 방패와 활로 무장시켰습니다.”

말이 백여 명이지, 실은 그것에 한참 못 미친다는 사실을 대전의 모두가 알고 있었다.

지난밤 항산검문의 중진 몇이 가족과 자신들을 따르는 수하들을 데리고 줄행랑을 쳤기 때문이다.

“철 숙부, 제가 따로 말씀드린 건 어떻게 됐나요?”

“네 말대로 조치해 두었다.”

이소월의 계책은 다름 아닌 기름이었다. 장원 곳곳에 마차 열 대 분량의 기름을 골고루 뿌려 놓았다.

잘 마른 건초 더미로 덮어 두었으니 불이 닿기만 해도 사방이 불바다로 변할 것은 자명했다.

‘동귀어진이라도 할 셈인가?’

철무백은 걱정스러웠지만 말을 아꼈다. 그가 오랜 세월 지켜봤던 이소월은 아주 어린 시절부터 언제나 침착하고 총명한 아이였다.

“하루, 딱 하루만 버티면 됩니다. 태원진가의 지원군이 오고 있으니 그때까지만 시간을 끌면 충분히 승산이 있어요.”

“태, 태원진가에서 지원군을 보냈습니까?”

“산서잠룡과 진천검이 직접 오고 있다는군요.”

대전에 모인 이들의 얼굴이 한층 밝아졌다. 진천검 진무경이야 이미 중원에서도 명성이 자자한 무공의 천재고, 산서잠룡 진태경은 떠오르는 샛별이다.

그가 항산검문과의 전쟁을 통해서 명성을 얻었다는 사실은 껄끄럽지만 한 편이라고 생각하니 천군만마가 따로 없다.

무엇보다…….

“풍양이 아무리 간 큰 놈이라고 해도 태원진가의 직계를 상대로 검을 겨누진 못할 겁니다.”

“……그렇겠죠.”

이소월은 내심 씁쓸했다. 얼마 전만 하더라도 태원진가와 어깨를 나란히 하던 항산검문이다.

산서 북부를 호령하던 무림 문파가 이제는 마적단을 상대로도 버티는 것에 주력해야 한다니.

‘오늘 일은 결코 잊지 않는다.’

입술을 질끈 깨문 그 순간이었다.

대전 문이 열리고 수문각의 무사가 헐레벌떡 뛰어와 외쳤다.

“문주님, 적들이 사자를 보내왔습니다!”

“사자?”

“예. 직접 만나 뵙고 전해 드릴 말이 있다고…….”

이소월은 망설임 없이 고개를 끄덕였다.

일각이라도 전투를 늦출 수 있다면 뭐든지 해야 한다.

“들여라.”

수문각 무사가 물러난 지 얼마 되지 않아 적풍단의 사자가 대전으로 안내되었다. 썩은 이를 드러내며 히죽 웃은 그가 과장되게 허리를 굽혔다.

“대항산검문의 문주님을 뵙소.”

다분히 조롱 섞인 태도였지만 중진들은 물론이고 불같은 성격인 철무백도 분노를 참았다. 앞서 이소월의 신신당부가 있었기 때문이다.

“무슨 일로 사자를 보냈지?”

“거, 먼 길 온 사람한테 탁주라도 한 사발 주고 물어봐야 하는 것 아니…… 헉.”

적풍단의 사자는 말을 잇지 못하고 몸을 부르르 떨었다.

분노를 참지 못한 철무백이 한 걸음 앞으로 나서며 엄청난 기세를 내뿜었기 때문이다.

“탁주가 그리 먹고 싶더냐?”

깊게 가라앉은 음성에 사자가 정신없이 고개를 흔들었다.

“아, 아닙니다. 목이 말라서 허, 헛소리를 그만.”

“철 숙부. 그만하세요.”

“……흥, 헛소리 그만하고 말이나 전해라.”

간신히 철무백의 기세에서 풀려난 사자가 더듬더듬 입을 열었다.

“다, 단주께서 말씀하시길, 무익한 전쟁은 멈추고 이제 우의를 다지자 하십니다.”

“우의?”

항산검문의 중진들은 자신의 귀를 의심했다.

전대 문주인 이천백을 배신하고 소문주 이소광마저 죽인 것이 누구인가? 심지어 바로 얼마 전에는 대동지부의 식솔들을 몰살시키기까지 하지 않았던가.

그러나 이소월의 반응은 달랐다. 그녀는 놀란 기색도 없이 사자를 똑바로 응시했다.

“거절한다면?”

“멸문지화를 면치 못할 거라 하셨습니다.”

“사람들을 살리고 싶으면 혼인 예물로 항산검문을 통째로 바치라는 뜻이군.”

“저, 저는 거기까지는 잘…….”

이쯤 되니 대전 안의 사람들도 풍양이 전한 ‘우의’의 의미를 알아차릴 수 있었다. 모두가 분노했지만 그중 가장 빠르게 움직인 사람은 항산호 철무백이었다.

퍽!

말 그대로 찰나의 순간, 십여 장의 거리를 뛰어넘은 철무백의 일 권이 사자의 가슴에 박혔다. 가공할 열기를 머금은 붉은 권기(拳氣)가 가슴뼈를 박살 내고 피와 살을 태웠다.

“꺼허어어.”

마지막 단말마와 함께 사자의 눈동자에서 빛이 사라졌다.

놈의 가슴에서 주먹을 뽑아낸 철무백이 이소월을 향해 몸을 돌렸다.

“백번 죽어 마땅한 놈이었다.”

“저도 같은 생각이에요. 다만…….”

천천히 자리에서 일어난 이소월이 말을 이었다.

“이제 싸움을 피할 수 없겠군요.”

반 시진 후, 항산검문의 모두는 사방에서 울리는 뿔피리 소리를 들을 수 있었다.
```

## Current accepted English baseline

```markdown
# Chapter 112

Mounted bandits openly riding down the main road in broad daylight?

Under normal circumstances, it would be unthinkable. The nearest Murim sect would be the first to act, followed by the soldiers from the local authorities.

But if there were hundreds of mounted bandits—enough to overwhelm even the Murim sect that was supposed to suppress them—the officials could only close their eyes and cover their ears.

Just like now.

“Ar-aren’t those mounted bandits?”

“Don’t call them ‘those guys.’ Do you have three lives or something? They’re the infamous Red Wind Band.”

“The Red Wind Band? Weren’t they defeated by the Mount Heng Sword Sect not long ago?”

“That’s what we thought. But this time seems different. Rumors are already spreading through the marketplace that the Mount Heng Sword Sect won’t escape total destruction.”

“Still, the sect has some ability. Surely they won’t lose to mere mounted bandits…”

“Hey, watch your mouth! The man riding at the front is Pung Yang, the leader of the Red Wind Band. They say he’s a Peak master.”

“What? A Peak master?”

“Yeah. You can’t dismiss them just because they’re mounted bandits. I hear he isn’t merely strong in martial arts—he’s exceptionally clever, too.”

The commoners’ fearful whispers wormed their way into Pung Yang’s ears and those of his mounted bandits.

A subordinate riding on Pung Yang’s right spoke softly.

“Shall I rip those bastards’ mouths apart?”

“Do you want to?”

“If the Leader permits it, I’ll deal with those two first, then turn the entire village into a sea of flames.”

“You’ll kill the old men, capture the young men, and rape the women?”

“Heh heh. Isn’t that what men like us always do? The Mount Heng Sword Sect bastards are probably cowering behind their walls by now, scared out of their wits.”

“They probably are. They’ll be preparing for a final battle by gathering every bit of strength they have.”

“It won’t matter. That’ll just be eggs thrown at a rock. It’s a foregone conclusion that the Leader will wipe out the Mount Heng Sword Sect and take its place.”

“That is why I won’t permit it.”

“What?”

Pung Yang burst into a hearty laugh at his subordinate’s bewildered reaction.

They were all shallow-minded and cruel by nature. That was why they had become mounted bandits—and why Pung Yang kept them close.

*Because they’re easy to handle.*

When his laughter subsided, he spoke.

“Destroying the Datong Branch was part of the war. But if we harm commoners now, all we’ll accomplish is giving the Jin Family of Taiyuan an excuse to intervene.”

“Are they the rulers of Shanxi or something?”

“Not yet. But they will be soon enough. Before that happens, shouldn’t we swallow the Mount Heng Sword Sect and lie flat like dogs?”

“Um, Leader, I’m not doubting your judgment, but… would orthodox factions like the Jin Family of Taiyuan really look favorably on mounted bandits like us?”

“Mounted bandits? Who’s a mounted bandit?”

“What?”

“Last time, I noticed that the Sect Leader of the Mount Heng Sword Sect was quite beautiful.”

Pung Yang’s subordinate blinked several times before finally understanding. The corners of his mouth curled upward.

“She’s of marriageable age, so she’ll need to take a husband.”

“She has two choices: total destruction or marriage.”

“Then what will happen to the Red Wind Band…?”

“We’ll take the heart of it and wear the outer shell. Let’s see… Compared to the others, your face is at least presentable. I’ll make you Master of the Gatekeeper Pavilion.”

“Ha ha ha! I’ll devote my life to serving you!”

As he listened to his subordinate’s laughter, Pung Yang tightened his grip on the reins.

*At last, I’ve made it this far.*

He was a cold and levelheaded man, but his heart pounded at the thought that he had taken another step toward his ambition.

Memories from long ago flickered before his eyes.

*It’s been well over twenty years already.*

Becoming a mounted bandit had been easier and simpler than he had expected. There were only two ways: go looking for them or get caught by them. In Pung Yang’s case, it had been the latter.

When he was young, he had committed a crime and was being taken to the local authorities when a mounted-bandit group attacked. That had been the turning point of his life.

*“Boss, there’s a little one here, too.”*

*“Hm? He’s so skinny that we wouldn’t get more than a few coins for him even if we sold him. Kid, did you get caught pickpocketing?”*

*“No. I killed someone.”*

*“You killed someone? How old are you?”*

*“Thirteen.”*

*“Why did you kill him?”*

*“I hadn’t eaten for three days, and the boss had dumplings…”*

*“Dumplings? Did he take away what you begged for? That would be enough to make anyone snap.”*

*“No. I was hungry, and I didn’t have the strength to beg. He was eating dumplings right in front of me.”*

*“…So you killed him?”*

*“I thought it would be faster to take them and eat them.”*

*“Hey, let this kid go and feed him something. He’s one of us from today.”*

Pung Yang became a mounted bandit that day.

An orphan abandoned by the world, he had wandered from place to place begging for food. He was exceptionally perceptive and quick-witted.

Compared to his past, when he had barely eaten a meal every three days, life as a mounted bandit was lavish.

Robbery? Murder?

To Pung Yang, who had committed murder at the age of thirteen simply because he wanted to eat dumplings, such things were nothing more than what had to be done.

*“Good grief. I’ve been a mounted bandit for more than ten years, but I’ve never seen anyone like you. It’s as if you don’t have a conscience.”*

*“Why? I’m a mounted bandit.”*

*“Kid, that’s not how it works. You gradually get used to it. No one is skilled from the very beginning.”*

*“Were you like that too, Boss? It was easy for me.”*

*“Easy, easy… I’m starting to wonder if I’m raising a tiger cub. How about learning a thing or two about martial arts from me?”*

*“Martial arts?”*

*“Yes, martial arts. You’re still young, so if your bones and martial talent are up to the task, you could become a master.”*

*“Then I’ll call you Master from today onward.”*

*“Master and disciple, my ass. Forget it. Just keep doing what you’re doing now.”*

Not forming a master-disciple relationship had been a wise decision.

A year later, his boss was beheaded and killed by a First Rate master, and Pung Yang found a new nest in another mounted-bandit group.

*“You were under Gwangchil?”*

*“Yes. If you feed me well, I’ll swear my loyalty to you.”*

*“You seem reasonably sharp. I won’t go easy on you because you’re young, so keep up on your own.”*

The plateau was brutal.

There were times when an entire mounted-bandit group was wiped out after attacking the wrong merchant caravan. The struggles for power between mounted-bandit groups never stopped, either.

But Pung Yang survived every time, growing stronger with each passing year.

By the time he turned thirty, his martial arts had entered the First Rate realm, and he managed to seize the position of squad leader in a mounted-bandit group of considerable size.

*But that was as far as I got.*

The law of strength applied everywhere.

The plateau was ultimately just another part of the Murim, where the strong ruled.

Pung Yang possessed grand ambitions and an exceptional mind, but he lacked the martial power befitting a leader.

*The limit of Third Rate martial arts.*

Pung Yang’s martial talent was extraordinary.

If he had entered a prestigious orthodox sect as a child and learned an excellent internal cultivation technique and martial arts, he might have crossed the wall to Peak long ago.

But he had grown up in a beggar’s den and learned Third Rate martial arts from the mounted bandits of the plateau. His limitations were clear.

*If heaven’s fortune hadn’t favored me, I’d probably still be standing in the same place.*

A deep smile settled over Pung Yang’s lips.

Three years ago, on that day, his life had changed completely. He had gone from being a mere squad leader in a mounted-bandit group to the leader of the Red Wind Band, one of the powers moving the plateau—and now it was time to swallow a Murim sect.

“Leader!”

Pung Yang snapped out of his thoughts at his subordinate’s shout.

Far in the distance, stone walls piled high like a fortress had finally come into view.

*The Mount Heng Sword Sect.*

As Pung Yang gazed at his and the Red Wind Band’s new home, one person entered his sight. Even from this distance, he could feel the man’s fiery aura.

*The Tiger of Mount Heng, Cheol Mubaek.*

A wall he would have to overcome in order to take the Mount Heng Sword Sect.

Although he had withdrawn after suffering a slight loss last time…

*Today will be different.*

Pung Yang unconsciously felt inside his robes. After confirming the hard wooden case there, his smile deepened.

“Leader, your orders?”

“Surround them. Don’t let even a single ant escape. Then send an envoy.”

Total destruction or marriage.

The Mount Heng Sword Sect had only two choices.

“I’ll have the Mount Heng Sword Sect in my hands before sunset.”

* * *

“They’ve surrounded our sect without leaving a gap!”

“Their numbers are well over two hundred!”

“Sect Leader, please make a decision!”

Seated in the place of honor, Lee Seowol calmly opened her mouth.

“Are the troops deployed?”

“Of the hundred or so men, half are blocking the sect entrance. The rest have been armed with shields and bows.”

Everyone in the main hall knew that “a hundred or so” was a generous estimate. In truth, they had far fewer than that.

Several of the Mount Heng Sword Sect’s senior figures had fled the previous night, taking their families and the subordinates who followed them.

“Uncle Cheol, what happened with what I asked you to do?”

“It has been arranged as you instructed.”

Lee Seowol’s plan involved oil.

They had spread enough oil to fill ten wagons evenly throughout the estate.

They had covered it with piles of well-dried hay, so it was obvious that the entire area would turn into a sea of flames the moment fire touched it.

*Does she intend for us to perish together with them?*

Cheol Mubaek was worried, but he kept his thoughts to himself. In all the years he had watched Lee Seowol, she had always been calm and clever, even from a very young age.

“We only need to hold out for one day. Exactly one day. Reinforcements from the Jin Family of Taiyuan are on their way, so we have a good chance of winning if we can stall them until then.”

“R-reinforcements from the Jin Family of Taiyuan?”

“I hear the Sleeping Dragon of Shanxi and the Heaven Shaking Sword are coming in person.”

The faces of everyone gathered in the main hall brightened.

The Heaven Shaking Sword, Jin Mukyung, was already renowned throughout the Central Plains as a martial arts genius, while the Sleeping Dragon of Shanxi, Jin Taekyung, was a rising star.

It was uncomfortable that he had earned his fame through a war against the Mount Heng Sword Sect, but knowing that he was now on their side made it feel as though they had gained a thousand troops.

Above all else…

“No matter how bold Pung Yang is, he won’t dare raise his sword against a direct descendant of the Jin Family of Taiyuan.”

“…That’s true.”

Lee Seowol felt bitter inside.

Not long ago, the Mount Heng Sword Sect had stood shoulder to shoulder with the Jin Family of Taiyuan.

Now, a Murim sect that had once commanded northern Shanxi had to focus all its strength on merely holding out against a mounted-bandit group.

*I will never forget what happened today.*

Just then, she bit down hard on her lip.

The doors to the main hall opened, and a martial artist from the Gatekeeper Pavilion came running in, shouting.

“Sect Leader, the enemy has sent an envoy!”

“An envoy?”

“Yes. He says there’s something he wishes to tell you in person…”

Lee Seowol nodded without hesitation.

If they could delay the battle by even a single moment, they had to do everything they could.

“Bring him in.”

Not long after the Gatekeeper Pavilion martial artist withdrew, the Red Wind Band’s envoy was escorted into the main hall.

He exposed his rotten teeth in a crooked grin and bowed deeply in an exaggerated manner.

“I pay my respects to the Sect Leader of the great Mount Heng Sword Sect.”

His attitude was clearly mocking, but the senior figures—and even Cheol Mubaek, whose temper was as fierce as fire—suppressed their anger. Lee Seowol had repeatedly warned them to do so beforehand.

“Why did you send an envoy?”

“Well, shouldn’t you give someone who has come such a long way a bowl of rice wine before asking—gasp.”

The Red Wind Band’s envoy was unable to finish his sentence and began trembling violently.

Cheol Mubaek, unable to contain his anger, had taken one step forward and released an overwhelming aura.

“Do you want rice wine that badly?”

At the deep, heavy voice, the envoy frantically shook his head.

“N-no, sir. I was thirsty, so I said something stu—stupid.”

“Uncle Cheol. That’s enough.”

“…Hmph. Stop talking nonsense and deliver your message.”

Barely freed from Cheol Mubaek’s aura, the envoy stammered.

“T-the Leader says we should stop this pointless war and now cement our friendship.”

“Friendship?”

The senior figures of the Mount Heng Sword Sect doubted their own ears.

Who had betrayed the previous Sect Leader, Lee Cheonbaek, and killed even the Young Sect Leader, Lee Seogwang? And hadn’t they massacred the families and dependents of the Datong Branch only a short while ago?

But Lee Seowol’s reaction was different. Without the slightest hint of surprise, she stared straight at the envoy.

“And if we refuse?”

“He said you won’t escape total destruction.”

“So he means that if we want to save our people, we must offer the Mount Heng Sword Sect in its entirety as a wedding gift.”

“I-I don’t know about anything beyond that…”

At this point, everyone in the main hall understood the meaning of the “friendship” Pung Yang had offered.

All of them were furious, but Cheol Mubaek was the quickest to act.

*Thud!*

In the literal blink of an eye, Cheol Mubaek crossed more than ten *jang* and drove one punch into the envoy’s chest.

The red fist aura carrying horrifying heat shattered his chest bones and burned his blood and flesh.

“Ghuuuh…”

With one final death rattle, the light vanished from the envoy’s eyes.

Cheol Mubaek pulled his fist from the man’s chest and turned toward Lee Seowol.

“He deserved to die a hundred times over.”

“I think so, too. But…”

Lee Seowol slowly rose from her seat and continued.

“We can no longer avoid the fight.”

One hour later, everyone in the Mount Heng Sword Sect heard the sound of horn calls ringing out from all directions.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 112`.

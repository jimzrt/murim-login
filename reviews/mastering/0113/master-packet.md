# Master Edit Task — Chapter 113

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
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 월화     | **Wolhwa**         |
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
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 체력               | **Stamina**                    |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 공자      | **Young Master**                                                |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 진위경 | 이소월 | host_to_new_sect_leader | Young Lady | formal-polite | Jin Wikyung addresses Lee Seowol as 소저 before accepting her oath. |
| 이소월 | 진위경 | new_sect_leader_to_lesser_family_head | Lesser Family Head | formal-deferential | Lee Seowol refers to Jin Wikyung as 소가주님 when describing his summons. |
| 철무백 | 진위경 | sect_elder_to_lesser_family_head | Lesser Family Head | formal-deferential | Cheol Mubaek formally greets Jin Wikyung as the Lesser Family Head of the Jin Family of Taiyuan. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
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

#### Chapter 111 tail (verified mastered)

…
again.”* *“The Jin Family of Taiyuan is strong even without the Family Head and the Second Young Master. Please reconsider.”* *“No. My decision has already been made.”* *“Then make sure you win. Become strong enough that no one in Shanxi can even open their mouth about a scandal involving me.”* *“…If you had been a man, I would have made you the Young Sect Leader.”* *“I’m glad I was born a woman. I have no interest in being this sect’s Young Sect Leader.”* Her fears soon became reality. Had even a fortnight passed before Lee Seogeun returned as a cold corpse? Not long after, she lost Lee Cheonbaek. In the end, even her eldest brother, Lee Seogwang, was gone. *Now I’m alone.* And so, the Blood Wolf Sword Lee Cheonbaek’s last surviving blood relative became the new Sect Leader. As she silently gazed at the burial mounds, a warm palm gently caressed her shoulder. “I’m sorry. I should have come sooner…” “Uncle Cheol, please don’t say that. If you hadn’t come, our sect wouldn’t have been able to hold out this long.” Under the Red Wind Band’s fierce assault, the Mount Heng Sword Sect had been helplessly driven back. If not for the Peak master known as the Tiger of Mount Heng, who had rushed over after belatedly learning of Lee Cheonbaek’s calamity, the enemy would never have withdrawn. “I’ll tear that bastard limb from limb and kill him.” At the thought of the Red Wind Band Leader, Lee Seowol shook her head. In a life-and-death duel between Peak masters, Cheol Mubaek had the edge. They had already clashed once, and Pung Yang had retreated with a minor internal injury. *But an opportunity like that will never come again.* The Mount Heng Sword Sect had always gathered information on the mounted bandits of northern Gaoyuan and remained constantly on alert. There were dozens of mounted-bandit groups in Gaoyuan, but among them, the Red Wind Band led by Pung Yang had grown frighteningly fast. A man particularly strong and meticulous even among Gaoyuan’s chieftains. That man was Pung Yang. *There’s no way someone like that would engage Uncle Cheol in a life-and-death duel. If Uncle Cheol rashly tried to confront him, Pung Yang would turn the tables on him instead.* Lee Seowol turned toward Cheol Mubaek. “Uncle Cheol, could you tell me once more about Pung Yang’s martial arts?” “Early Peak. His saber arts and throwing-knife techniques had reached a high realm. However…” A deep furrow formed between Cheol Mubaek’s brows. “Every one of his forms was thoroughly insidious. I suspect he has learned demonic, heterodox martial arts.” “Demonic, heterodox arts…” Ever since the Great Faction War, practicing demonic, heterodox arts had become synonymous with death in the Central Plains. Unorthodox factions might present themselves as orthodox, but no one openly declared themselves unorthodox. “For now, it’s only a suspicion. We’ll know if we clash again.” “I trust you, Uncle Cheol. But don’t underestimate the Red Wind Band Leader. He has any number of subordinates he can sacrifice in his place.” With enemies bearing down from both directions, their combined force was close to three hundred strong. Meanwhile, even after gathering every martial artist stationed at its branches, the Mount Heng Sword Sect had less than half that number. Given the situation, morale was low among both the ordinary martial artists and the newly appointed senior members. “Seowol. May I say something?” These were the words of a benefactor who had risked his life out of loyalty to his dead friend. Lee Seowol bowed politely. “I’ll take your words to heart.” Cheol Mubaek spoke heavily. “Leave.” It was a single word laden with meaning. But there was not the slightest hesitation in Lee Seowol’s answer. “I’m sorry.” “It isn’t too late. You must survive.” “It isn’t over yet. And I will survive.” “If you thought Cheonbaek would have wanted this…” “Uncle.” At her resolute voice, Cheol Mubaek closed his mouth. Firm determination filled Lee Seowol’s clear eyes. “This is what I wanted. As the Sect Leader of the Mount Heng Sword Sect.” “Whew…” Cheol Mubaek let out a sigh instead of answering. “I’m already deeply indebted to you, Uncle. Even if you leave now, I won’t resent you.” “Do you really need to hear my answer before you’ll be satisfied?” Lee Seowol shook her head. Cheol Mubaek had cherished her like his own child since she was young. In some ways, he had been more of a father to her than her actual father. “I will never forget this debt. Uncle Cheol, you are the benefactor of both me and the Mount Heng Sword Sect.” “I’ve watched you since you were little, but… you really are a sly child.” “I was sly when I was young. Now I’m a ruthless bitch.” Watching Lee Seowol smile faintly, Cheol Mubaek could only continue to sigh deeply. “Do we have any chance of winning?” “If we fought now? Ten percent.” “What?” “But if reinforcements arrive, fifty percent. More than that.” “Reinforcements? From the Jin Family of Taiyuan?” “A messenger pigeon from the Lower District Sect’s Jeongyang Branch arrived two *shichen* ago.” “How many are coming? A hundred? Two hundred?” “Four. One of them is the Heaven Shaking Sword, Jin Mukyung, and another is…” Lee Seowol let out a wry laugh, reminded of her ill-fated connection with him. “The Sleeping Dragon of Shanxi, Jin Taekyung.”

#### Chapter 112 tail (verified mastered)

…
shields and bows.” Everyone in the main hall knew that “a hundred or so” was a generous estimate. In truth, they fell well short of that number. Several of the Mount Heng Sword Sect’s senior figures had fled the previous night, taking their families and the subordinates who followed them. “Uncle Cheol, what happened with what I asked you to do?” “I took care of it as you instructed.” Lee Seowol’s plan involved oil. They had spread enough oil to fill ten wagons evenly throughout the estate. They had covered it with piles of well-dried hay, so it was obvious that the entire area would turn into a sea of flames the moment fire touched it. *Does she intend to take them down with us?* Cheol Mubaek was worried, but he kept his thoughts to himself. In all the years he had watched Lee Seowol, she had always been calm and clever, even from a very young age. “We only need to hold out for one day. Just one day. Reinforcements from the Jin Family of Taiyuan are on their way. If we can delay the enemy until then, we have a good chance of winning.” “R-reinforcements from the Jin Family of Taiyuan?” “I hear the Sleeping Dragon of Shanxi and the Heaven Shaking Sword are coming in person.” The faces of everyone gathered in the main hall brightened. The Heaven Shaking Sword, Jin Mukyung, was already renowned throughout the Central Plains as a martial arts genius, while the Sleeping Dragon of Shanxi, Jin Taekyung, was a rising star. It was uncomfortable that he had earned his fame through a war against the Mount Heng Sword Sect, but knowing that he was now on their side made it feel as though they had gained a thousand troops. Above all else… “No matter how bold Pung Yang is, he won’t dare raise his sword against a direct descendant of the Jin Family of Taiyuan.” “…I suppose not.” Lee Seowol felt bitter inside. Not long ago, the Mount Heng Sword Sect had stood shoulder to shoulder with the Jin Family of Taiyuan. Now, a Murim sect that had once commanded northern Shanxi had to focus all its strength on merely holding out against a mounted-bandit group. *I will never forget what happened today.* Just as she bit down hard on her lip, the doors to the main hall opened, and a martial artist from the Gatekeeper Pavilion came running in, shouting. “Sect Leader, the enemy has sent an envoy!” “An envoy?” “Yes. He says there’s something he wishes to tell you in person…” Lee Seowol nodded without hesitation. If they could delay the battle by even a single moment, they had to do everything they could. “Bring him in.” Not long after the Gatekeeper Pavilion martial artist withdrew, the Red Wind Band’s envoy was escorted into the main hall. Flashing his rotten teeth in a crooked grin, he bowed deeply in an exaggerated manner. “I pay my respects to the Sect Leader of the great Mount Heng Sword Sect.” His attitude was clearly mocking, but the senior figures—and even the fiery-tempered Cheol Mubaek—suppressed their anger. Lee Seowol had repeatedly warned them beforehand. “Why did you send an envoy?” “Well, shouldn’t you offer a man who has traveled so far a bowl of rice wine before you start asking—gasp!” The Red Wind Band’s envoy broke off and began trembling violently. Unable to contain his anger, Cheol Mubaek had taken one step forward and unleashed an overwhelming aura. “Do you want rice wine that badly?” At the deep, heavy voice, the envoy frantically shook his head. “N-no, sir. I was thirsty and said something stu—stupid.” “Uncle Cheol. That’s enough.” “…Hmph. Stop talking nonsense and deliver your message.” Barely freed from Cheol Mubaek’s aura, the envoy stammered. “T-the Leader says we should end this pointless war and cement our friendship.” “Friendship?” The senior figures of the Mount Heng Sword Sect doubted their own ears. Who had betrayed the previous Sect Leader, Lee Cheonbaek, and killed even the Young Sect Leader, Lee Seogwang? And hadn’t they massacred the families and dependents of the Datong Branch only a short while ago? But Lee Seowol reacted differently. Without the slightest hint of surprise, she stared straight at the envoy. “And if we refuse?” “He said you won’t escape total destruction.” “So he means that if we want to save our people, we must offer the Mount Heng Sword Sect in its entirety as a wedding gift.” “I-I don’t know anything beyond that…” By now, everyone in the main hall understood what Pung Yang had meant by “friendship.” They were all furious, but the first to act was the Tiger of Mount Heng, Cheol Mubaek. *Thud!* In the literal blink of an eye, Cheol Mubaek crossed more than ten *jang* and drove his fist into the envoy’s chest. The red fist aura carrying horrifying heat shattered his chest bones and burned his blood and flesh. “Ghuuuh…” With one final death rattle, the light vanished from the envoy’s eyes. Cheol Mubaek pulled his fist from the man’s chest and turned toward Lee Seowol. “He deserved to die a hundred times over.” “I agree. But…” Lee Seowol slowly rose from her seat and continued. “Now there’s no avoiding the fight.” One hour later, everyone in the Mount Heng Sword Sect heard the sound of horn calls ringing out from all directions.

## Korean source

```text
＃113화



항산검문으로 사자를 보낸 뒤 반 시진. 풍양은 망설임 없이 명령을 내렸다.

“쳐라.”

속전속결.

시간을 끌수록 그에게는 불리했다. 적풍단이 항산검문을 포위했다는 소문은 빠르게 퍼져 나갈 것이고 외부 세력, 특히 태원진가가 개입한다면 골치 아파진다.

‘어차피 무혈입성은 기대하지도 않았다.’

여인의 몸이라고는 하나 혈랑검 이천백의 핏줄이다.

대화와 손짓으로 길들일 수 없다면 폭력으로 굴복시켜야 한다. 풍양이 지금까지 해 왔던 방식 그대로.

부우우우.

힘찬 뿔피리의 울림이 곳곳에서 울려 퍼졌다. 고원의 마적단들이 사용하는 진격 신호에 항산검문을 에워싼 적풍단의 마적들이 일제히 말의 옆구리를 걷어찼다.

“돌겨어억!”

“한 놈도 남김없이 죽여라!”

두두두두두!

수백 개의 말발굽이 눈 덮인 지면을 짓밟으며 달렸다.

뿔피리 소리는 끊이지 않고 힘차게, 멀리 퍼져 나갔다.



* * *



띠링.



- [운기조식]을 성공적으로 완료했습니다.

- 피로와 체력이 소량 회복됩니다.



시스템 알림음이 들리고 눈을 뜨자마자 주위를 둘러봤다.

“방금 무슨 소리 못 들었어요?”

말에게 건초를 먹이고 있던 월화와 혁무진이 영문을 모르겠다는 얼굴로 묻는다.

“진 공자, 무슨 소리예요?”

“소리야 항상 나죠. 들어 보세요. 말들이 건초 씹는 소리, 바람 소리…….”

“그딴 거 말고, 이 자식아.”

“그럼 뭔데요?”

“부, 부부젤라?”

“부부, 뭐요?”

“스포츠 응원할 때 쓰는…… 됐다. 그런 게 있어.”

나는 설명하는 것을 포기하고 소리가 들려온, 아니 들려왔다고 생각한 방향을 응시했다. 우연의 일치인지 마침 우리가 향하고 있던, 항산검문이 있을 북쪽이다.

‘내가 잘못 들었나?’

월화의 말대로라면 앞으로 세 시진(여섯 시간)은 더 달려야 항산검문에 도착할 수 있다. 무슨 일이 벌어졌다 해도 여기까지 들릴 만한 거리가 아니다.

‘대포 소리라면 모를까.’

때마침 운기조식을 끝마친 진무경도 한마디를 보탰다.

“아무 소리도 안 들렸다.”

“그런데 분명히 뭔가 들은 것 같단 말이지.”

“착각이야.”

“혹시 항산검문에 무슨 일이 난 걸 수도 있잖아.”

“그럴 수도 있지. 하지만 나한테는 아무 소리도 안 들렸다.”

“근데 나는 들은 것 같다니까?”

“그러니까 착각이라는 거다.”

“무슨 근거로?”

“간단하지. 네가 들은 걸 내가 못 들었을 리 없으니까.”

“…….”

이거 상당히 열받는데 맞는 말이라 반박할 수가 없네.

말문이 막힌 나를 보며 진무경이 혀를 찼다.

“눈먼 칼에 죽고 싶지 않다면 심신을 다스리는 것에 집중해라. 전장은 무슨 일이 벌어질지 모르는 곳이니까.”

누가 누굴 가르쳐?

전투 경험으로는 이 중에서 나를 따라갈 사람이 없을 것이다.

워낙 익숙해졌기에 평소와 다름없어 보일 뿐, 전투를 준비하고 참여하는 것에 있어서는 이미 닳고 닳았다.

“적의 숫자가 많으니 공력을 최대한 아끼고 움직임을 최소화해라. 내가 앞장설 테니 뒤따르기만 하면 문제없다.”

그래도 한 핏줄이라고 걱정해 주는 건가?

생각해 보면 지금까지 진무경은 싫어하는 티를 팍팍 내면서도 내게 상당한 도움을 주었다.

수련도 도와주고, 이번에 항산검문도 함께 가 주고, 어린 시절에는 게을러터진 아우를 갱생시키고자 제법 노력도 했다고 들었다.

아무리 진위경의 부탁이 있었다고 해도 정말 나를 싫어했다면 할 수 없는 일들이다.

‘알고 보면 정 많은 놈일지도.’

이런 성격의 사람을 츤데레라고 하나?

새삼 약간 감동이 밀려올 것도 같아 감성적인 눈빛으로 진무경을 바라보는데, 시선이 딱 마주쳤다.

“뭘 봐? 눈 깔아.”

“…….”

“마적 놈들 따위한테 상처 하나라도 입었다가는 내 손에 죽을 줄 알아라.”

“……어, 그래.”

그럼 그렇지. 츤데레는 개뿔. 내가 잠깐 미쳐서 정신 나간 상상을 했구나.

현실을 인정하고 앞서 빼앗은 여분의 말로 안장을 옮기려는데, 어느새 슬쩍 다가온 혁무진이 근심 가득한 얼굴로 입을 열었다.

“이공자님이 저도 죽이는 건 아니겠죠?”

“……난 죽어도 된다는 소리냐?”

“아, 아니 말씀을 왜 그렇게 하세요?”

“넌 반드시 내가 죽이고 죽을 테니까 닥치고 출발 준비나 해.”

뭐라 구시렁거리는 혁무진의 엉덩이를 걷어차 주고 말에 올라탔다.

항산검문까지는 앞으로 세 시진. 이제부터는 정말 일체의 휴식 없이 빡세게 달려야 한다.



제한 시간 : 6:25:19



* * *



항산검문은 하나의 요새 같았다. 높게 쌓아 올린 돌담은 성벽이라 불러도 될 만큼 견고했고 수성(守城)을 위한 각종 방어 시설이 설치되어 있었다.

초대 문주인 이천백의 강경한 의지로 세워진 그것들은 삼십여 년 만에 비로소 제 역할을 발휘했다.

“쏴라!”

쉬쉬쉬쉭!

일제히 쏘아진 수십 발의 화살이 돌진하는 기마를 향해 내리꽂혔다.

그러나 고원에서 가장 흔히 찾아볼 수 있는 병기가 창과 도, 그리고 활이다. 고원의 전투에 익숙한 적풍단의 마적들은 누군가의 명령이 떨어지기도 전에 각자 한 손에 낀 방패를 치켜세웠다.

투둑, 퍼버벅!

낙마한 이는 고작 십여 명.

바짝 마른 나무에 늙은 말의 엉덩이 가죽을 덧대어 만든 방패는 훌륭히 화살들을 막아 냈다.

“크하하핫! 이놈들이 어르신들을 몰라뵙고 감히……!”

적풍단의 조장 하나가 웃음을 터트린 그 순간이었다.

쐐애애액, 퍼걱!

강맹한 기세로 날아온 무언가가 말의 목을 뚫고 조장의 가슴팍에 꽂혔다. 이제 막 일류 초입에 든 그는 믿을 수 없다는 듯 삐죽 튀어나온 화살을 바라보다가 애마와 함께 고꾸라졌다.

뒤따라 달려오던 기마 중 몇 기가 그 때문에 대열이 흐트러져 줄줄이 쓰러진다.

“쇠뇌, 쇠뇌를 조심해라!”

“응사하라!”

쉬쉬쉬쉭!

앞서 항산검문의 공격이 소낙비였다면 적풍단의 화살 세례는 장대비다. 말을 탄 상태에서도 연거푸 시위를 당기는 그들의 화살은 정확하고 빨랐다.

푸푸푸푹!

“크아악!”

“방패 뒤로 몸을 숨겨라! 고개를 내밀지 마!”

그 틈을 타 박차를 가한 마적들은 십여 장 높이의 성벽에 갈고리와 급조한 사다리를 대고 침투를 시도했다.

백병전이 시작된 성벽 위에선 비명과 피가 터져 나왔다.

“크하하! 모두 죽여라!”

“놈들이 올라오지 못하게 막아!”

이소월은 가장 높은 망루에서 이 모든 광경을 지켜보고 있었다. 입술이 파르르 떨리고 얼굴에는 핏기가 사라졌다.

‘이것이 무림.’

죽어 가는 자의 비명, 살고 싶은 자의 몸부림.

마침내 맞닥트린 약육강식의 세계는 그녀가 생각했던 것 이상으로 잔혹하고 두려웠다.

그러나…….

‘물러날 수 없어.’

이미 수많은 이들이 죽었다. 떠날 이들은 떠났고, 남은 이들은 목숨을 걸고 싸우고 있다.

이소월은 이제 그들을 이끌어야 할 문주이며 항산검문과 운명을 함께해야 하는 몸이다.

“문주! 성벽이 위태롭습니다. 지원을 보내야 합니다!”

“놈들이 충차(充車)로 문을 부수고 있습니다!”

“문주! 어서 조치를!”

“문주!”

그 순간, 사방에서 빗발치는 급보를 전해 듣던 이소월이 입을 열었다.

“내가 신호하면 성벽을 향해 화시(火矢)를 한 발, 문을 향해 두 발을 쏘아 올려라. 그리고 철 숙부.”

이소월의 옆을 지키고 있던 철무백이 대답했다.

“뭐든 말하거라.”

“곧 문이 뚫릴 거예요. 잠시 시간을 벌어 주실 수 있나요?”

“나 혼자 말이냐?”

“어려운 부탁을 드려 송구할 따름입니다.”

“일당백(一當百)이라. 언젠가 꼭 해 보고 싶었지.”

“제가 아는 숙부께선 만인적(萬人敵)의 고수십니다. 허나 부디 몸조심하세요.”

“오냐, 내 저런 놈들에게 당할 성싶으냐?”

껄껄 웃은 철무백이 훌쩍 뛰어내렸다. 항산호, 완숙한 절정 고수인 그가 갔으니 풍양이 나서지 않는 한 아무도 문을 넘을 수 없을 것이다.

‘더, 조금만 더.’

치열한 전장을 내려다보던 이소월이 돌연 벼락같은 외침을 토해 냈다.

“지금!”

그녀의 명령을 기다리고 있던 무인 둘이 각각 활시위를 당겼다.

다음 순간, 어느새 어둡게 물든 겨울 하늘 위로 날아오른 불화살이 모두의 머리 위에서 환하게 빛났다.



* * *



유성처럼 떨어지는 불화살은 백 장 너머에 있는 풍양의 눈에도 똑똑히 보였다. 그는 내심 중얼거렸다.

“숨겨 둔 한 수가 있었군.”

짐작이 확신으로 바뀌는 데까지는 그리 오랜 시간이 걸리지 않았다. 잠시 후, 성벽 둘레에서 엄청난 불길이 솟구쳤기 때문이다.

화륵, 화아아악!

“끄아아아악!”

불에 타 죽는 것은 가장 고통스러운 죽음 중 하나다. 성벽 밑에 개미 떼처럼 몰려 있던 적풍단의 마적들이 끔찍한 비명과 함께 몸부림쳤다.

성벽에 걸어 놓은 갈고리의 줄이 끊기고, 목제 사다리가 화염에 휩싸였다.

“쳐라!”

“마적 놈들을 전부 죽여라!”

성벽 밑에서 올라가기를 기다리던 자, 올라가던 자는 불에 타 죽고 이미 올라간 자들은 사방에서 짓쳐 들어오는 병장기에 찔리고 베였다.

“나름 준비를 했다 이거지…….”

덤덤하게 전장을 응시하는 풍양의 시선에 숯검정처럼 곳곳이 까맣게 그을린 채 돌아오는 마적 하나가 들어왔다.

“무슨 일인가?”

“다, 단주님. 피해가 너무 큽니다!”

마적은 그의 앞에 섬과 동시에 넙죽 엎드려 헐떡거리는 목소리로 말을 이었다.

“첫 공격부터 지금까지 족히 일백은 죽은 것 같습니다. 무엇보다 방금 화공(火攻) 때문에 형제들의 사기가…….”

“문은?”

“예?”

“문은 어찌 되었지?”

“뚫긴 했습니다만 항산호 철무백이 홀로 버티고 있어서…….”

“혼자란 말이냐?”

“예. 하지만 워낙 무공이 고강한지라 아무도 나서지 못하고 있습니다.”

“그럼 되었다.”

풍양은 말과 동시에 손을 내밀었다. 무심코 그 손을 맞잡으려던 마적의 신형이 기우뚱 쓰러진다.

어리둥절한 표정으로 굳어 가는 그의 미간에는 비수 한 자루가 깊숙이 박혀 있었다.

“병력은 얼마나 남아 있지?”

풍양의 오른팔 격인 수하에게는 이런 광경이 익숙했다. 시체를 흘끗 바라본 그가 대답했다.

“어림잡아 백오십은 약간 넘고, 이백이 조금 못 됩니다. 우리 측 희생이 더 큰 건 사실입니다.”

“적들은 오죽하겠느냐? 지금 성벽 위에 있는 놈들이 항산검문의 마지막 보루다.”

“저 얼마 안 되는 놈들이 전부란 말씀이십니까?”

“그래.”

“단주님을 못 믿는 건 아닙니다만 방금의 화공처럼 또 다른 함정을…….”

“그걸 노린 게지.”

풍양은 실소를 흘렸다. 누구 머리에서 나온 계략인지는 모르겠지만 제법 머리를 잘 굴렸다.

아마 지금보다 경륜이 부족했다면 풍양 역시 또 다른 함정을 의심하고 병력을 뒤로 물렸을 것이다.

‘시간을 벌기 위해 애쓰는군. 누군가의 지원을 기다리나?’

그렇다면 더욱 망설일 이유가 없다.

중과부적(衆寡不敵). 적풍단이 상당한 피해를 입었다고는 해도 항산검문을 쓸어 버리는 것은 일도 아니다.

거기에 더해…….

“내가 직접 간다.”

“단주님께서 직접 말씀이십니까?”

“그래, 호랑이를 잡아야 하지 않겠느냐?”

너털웃음을 터트린 풍양은 습관적으로 품 안을 더듬었다.

단단한 목곽, 그 안에 호랑이를 단숨에 거꾸러트릴 물건이 들어 있었다.
```

## Current accepted English baseline

```markdown
# Chapter 113

Half a shichen after sending an envoy to the Mount Heng Sword Sect, Pung Yang gave the order without hesitation.

“Attack.”

A quick, decisive battle.

The longer it dragged on, the worse it would be for him. Word that the Red Wind Band had surrounded the Mount Heng Sword Sect would spread quickly, and if outside forces—especially the Jin Family of Taiyuan—intervened, things would become troublesome.

*I never expected to enter without bloodshed in the first place.*

She might be a woman, but she carried the blood of the Blood Wolf Sword, Lee Cheonbaek.

If words and gestures couldn’t tame her, he would have to subdue her with violence. It was the same method Pung Yang had always used.

Bwooooooong!

The powerful sound of horns rang out from every direction. At the advance signal used by the mounted-bandit groups of the plateau, the mounted bandits surrounding the Mount Heng Sword Sect simultaneously kicked their horses in the ribs.

“Chaaaarge!”

“Kill every last one of them!”

Thundering hooves shook the ground.

Hundreds of horses raced forward, trampling the snow-covered earth.

The horn calls continued without pause, strong and carrying far into the distance.

* * *

Ding!

> **System**
> 
> **Circulate Qi** was successfully completed.
> 
> A small amount of Fatigue and Stamina has been restored.

The moment I opened my eyes at the sound of the System notification, I looked around.

“Did you guys just hear something?”

Wolhwa and Hyuk Mujin, who had been feeding hay to the horses, looked at me in confusion.

“Young Master Jin, what sound?”

“Sounds are always happening. Listen. The horses chewing hay, the wind…”

“Not that crap, you idiot.”

“Then what?”

“A-a vuvuzela?”

“Vuvu… what?”

“The thing people use to cheer at sporting events… Never mind. It’s something.”

I gave up explaining and stared in the direction the sound had come from—or rather, the direction I thought it had come from.

By coincidence, it was the north, where the Mount Heng Sword Sect lay—the very direction we were heading.

*Did I hear it wrong?*

According to Wolhwa, we still had to ride for another three shichen—six hours—before we could reach the Mount Heng Sword Sect. Whatever had happened, it wasn’t something that should have been audible from this distance.

*Unless it was cannon fire.*

Jin Mukyung, who had just finished circulating his qi, added his opinion.

“I didn’t hear anything.”

“But I could have sworn I heard something.”

“You imagined it.”

“Something might have happened at the Mount Heng Sword Sect.”

“That’s possible. But I didn’t hear anything.”

“But I’m telling you, I think I heard something.”

“So I’m telling you that you imagined it.”

“On what grounds?”

“It’s simple. There’s no way I could fail to hear what you heard.”

“…”

That was incredibly irritating, but he was right, so I couldn’t argue.

Seeing me rendered speechless, Jin Mukyung clicked his tongue.

“If you don’t want to die to a stray blade, focus on mastering your mind and body. You never know what might happen on a battlefield.”

*Look who’s lecturing whom.*

When it came to combat experience, no one here could match me.

I only seemed no different from usual because I had grown so accustomed to it. When it came to preparing for and taking part in battle, I was already thoroughly battle-hardened.

“There are a lot of enemies, so conserve your internal energy as much as possible and minimize your movements. I’ll take the lead. Just follow me, and there won’t be a problem.”

*Was he worried about me because we shared the same blood?*

Come to think of it, Mukyung had made his dislike painfully obvious, yet he had still helped me a great deal.

He had helped with my training, agreed to accompany me to the Mount Heng Sword Sect, and, I’d heard, had even made a considerable effort to reform his lazy little brother when they were children.

Even if Jin Wikyung had asked him to, those weren’t things he could have done if he truly hated me.

*Maybe he’s actually a soft-hearted guy.*

Was this what people called a tsundere?

I looked at Jin Mukyung with a sentimental gaze, feeling as though I might actually be moved.

Our eyes met.

“What are you looking at? Lower your eyes.”

“…”

“If you take even a single wound from those mounted-bandit bastards, I’ll kill you myself.”

“…Yeah, sure.”

*That’s more like it. Tsundere, my ass.*

I had briefly lost my mind and imagined something ridiculous.

Accepting reality, I was about to transfer my saddle to one of the spare horses we had taken earlier when Hyuk Mujin approached and spoke with a deeply worried expression.

“Second Young Master, you aren’t going to kill me too, are you?”

“…Are you saying it’s okay if I die?”

“Ah, no! Why are you putting it that way?”

“I’ll kill you before I die, so shut up and prepare to leave.”

I kicked Hyuk Mujin in the rear while he grumbled under his breath, then mounted my horse.

The Mount Heng Sword Sect was still three shichen away.

From this point onward, we had to ride hard without taking a single break.

> **System**
> 
> **Time Limit:** 6:25:19

* * *

The Mount Heng Sword Sect was like a fortress. The stone walls piled high around it were sturdy enough to be called castle walls, and all kinds of defensive facilities had been installed to hold the fortress.

Built more than thirty years ago under the uncompromising will of the founding Sect Leader, Lee Cheonbaek, those defenses were finally serving their intended purpose.

“Fire!”

Whoosh—whoosh—whoosh!

Dozens of arrows launched at once rained down on the charging cavalry.

But the weapons most commonly found on the plateau were spears, swords, and bows. Accustomed to fighting on the plateau, the mounted bandits of the Red Wind Band raised the shields strapped to one arm before anyone even gave the order.

Thud! Thump!

Only a dozen or so men were knocked from their horses.

The shields, made of bone-dry wood faced with hide from an old horse’s rump, did an excellent job of stopping the arrows.

“Ha ha ha! These punks don’t know their elders when they see them, and they dare—!”

That was when it happened.

Fwoosh—crack!

Something came flying with ferocious force. It pierced through a horse’s neck and buried itself in the squad leader’s chest.

He had only just entered the early stages of First Rate. He stared at the arrow protruding from his chest as though he couldn’t believe it, then toppled over together with his prized horse.

Several of the riders behind him lost formation and fell one after another.

“Crossbows! Watch for the crossbows!”

“Return fire!”

Whoosh—whoosh—whoosh!

If the Mount Heng Sword Sect’s attack had been a passing shower, the Red Wind Band’s arrow barrage was a torrential downpour.

Even while mounted, they drew their bowstrings again and again. Their arrows were fast and accurate.

Thwack! Thwack! Thwack!

“Aaargh!”

“Hide behind your shields! Don’t stick your heads out!”

Taking advantage of the opening, the mounted bandits spurred their horses forward and set grappling hooks and makeshift ladders against the walls, which stood more than ten *jang* high. They began attempting to breach the fortress.

A melee erupted atop the walls.

Screams and blood poured forth.

“Ha ha! Kill them all!”

“Stop them from climbing up!”

Lee Seowol watched the entire scene from the highest watchtower. Her lips trembled, and the color had drained from her face.

*So this is the Murim.*

The screams of those dying.

The desperate struggles of those who wanted to live.

The world of the strong preying on the weak that she had finally encountered was more brutal and frightening than she had imagined.

But…

*I can’t retreat.*

Countless people had already died. Those who were going to leave had left, while those who remained were fighting with their lives on the line.

Lee Seowol was now the Sect Leader who had to lead them. She was bound to share her fate with the Mount Heng Sword Sect.

“Sect Leader! The walls are in danger! We need to send reinforcements!”

“They’re breaking down the gate with a battering ram!”

“Sect Leader! You need to take action!”

“Sect Leader!”

As urgent reports rained down from every direction, Lee Seowol opened her mouth.

“When I give the signal, fire one fire arrow toward the walls and two toward the gate. And, Uncle Cheol.”

Cheol Mubaek, who had been standing beside her, answered.

“Tell me what you need.”

“The gate will be breached soon. Can you buy us a little time?”

“By myself?”

“I’m sorry to ask you to do something so difficult.”

“One against a hundred. I’ve always wanted to try that.”

“The uncle I know is a master who can face ten thousand men. But please be careful.”

“All right. Do you think those bastards can get the better of me?”

Cheol Mubaek laughed heartily, then leaped down.

With the Tiger of Mount Heng—a consummate Peak master—there, no one would be able to get through the gate unless Pung Yang himself stepped forward.

*Just a little longer. A little more.*

Lee Seowol watched the fierce battlefield below, then suddenly let out a thunderous shout.

“Now!”

The two martial artists who had been waiting for her command each drew their bowstrings.

The next moment, the fire arrows soared into the darkening winter sky and shone brightly above everyone’s heads.

* * *

The fire arrows falling like meteors were clearly visible even to Pung Yang, who stood more than a hundred *jang* away.

He thought to himself.

*They had a hidden ace.*

It didn’t take long for his suspicion to become certainty.

A moment later, enormous flames erupted around the walls.

Fwoosh! Fwoooosh!

“Aaargh!”

Burning to death was one of the most painful ways to die.

The mounted bandits of the Red Wind Band, massed beneath the walls like a swarm of ants, writhed and screamed horribly.

The ropes attached to the grappling hooks snapped, and the wooden ladders were engulfed in flames.

“Attack!”

“Kill every last one of those mounted-bandit bastards!”

Those waiting below to climb and those still making their way up burned to death. Those who had already reached the top were stabbed and slashed by weapons converging from every direction.

“So they did make some preparations…”

As Pung Yang stared impassively at the battlefield, one of the mounted bandits came back with parts of his body blackened like charcoal.

“What happened?”

“L-Leader. The casualties are too high!”

The moment he reached Pung Yang, the mounted bandit threw himself flat on the ground and continued in a breathless voice.

“From the first assault until now, at least a hundred men must have died. More importantly, after that fire attack, our brothers’ morale is…”

“The gate?”

“Pardon?”

“What happened to the gate?”

“We broke through, but the Tiger of Mount Heng, Cheol Mubaek, is holding it alone…”

“Alone?”

“Yes. His martial arts are so formidable that no one dares step forward.”

“Then it’s settled.”

At the same time, Pung Yang held out his hand.

The mounted bandit instinctively reached to take it, only for his body to list and collapse.

A dagger was buried deep between his brows.

“How many troops do we have left?”

This sort of scene was familiar to the subordinate who served as Pung Yang’s right hand. After glancing at the corpse, he answered.

“By a rough count, somewhere between a little over a hundred and fifty and just under two hundred. It’s true that our losses are greater.”

“Then imagine theirs. The men on those walls are the Mount Heng Sword Sect’s final bulwark.”

“You mean those few men are all they have left?”

“Yes.”

“I’m not doubting you, Leader, but couldn’t there be another trap like that fire attack?”

“That’s what they’re counting on.”

Pung Yang let out a derisive laugh. He didn’t know whose strategy it had been, but they had played it quite cleverly.

*If I had been less experienced, I would have suspected another trap and pulled our forces back.*

*They’re struggling to buy time. Are they waiting for someone’s support?*

If so, there was even less reason to hesitate.

The few couldn’t stand against the many. Even if the Red Wind Band had suffered considerable losses, wiping out the Mount Heng Sword Sect would be easy.

And besides…

“I’m going myself.”

“You’re going yourself, Leader?”

“Yes. We have to catch the tiger, don’t we?”

Pung Yang burst into a hearty laugh and habitually felt inside his robes.

A hard wooden case rested there.

Inside was something that could bring down a tiger in one go.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 113`.

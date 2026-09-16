# Master Edit Task — Chapter 158

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
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 화산파    | **Huashan**                      |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 내공     | **internal energy**                              |                                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 권법     | **fist technique**                               |                                                       |
| 장법     | **palm technique**                               |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 은인     | **Benefactor**                               |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 일격     | **One Strike**                         |
| 극양                        | **Extreme Yang**      |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 칭호               | **Title**                      |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 산서     | **Shanxi**             |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 천하제일인 | **greatest under heaven** | Superlative martial distinction used in Hong Jin and Jin Wikyung's banter. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 복호권 | **Crouching Tiger Fist** | Huashan martial art Cheongpung uses during the spar. |
| 암향표 | **Dark Fragrance Drift** | Movement technique Cheongpung uses to evade Taekyung's attacks. |
| 공수납백인 | **Empty-Hand Seizes the Blade** | Technique for catching an opponent's weapon between bare fingers. |
| 오행매화보 | **Five-Element Plum Blossom Steps** | Footwork technique Cheongpung combines with Dark Fragrance Drift. |
| 백전백패 | **Hundred Battles, Hundred Losses** | Taekyung's proposed teasing nickname for Mujin. |
| 너구리 | **Neoguri** | Instant-noodle brand used in Taekyung's flavor joke. |
| 진라면 | **Jin Ramen** | Instant-noodle brand used in Taekyung's flavor joke. |
| 푸라면 | **Puramyeon** | Instant-noodle brand used in Taekyung's flavor joke. |
| 귀환자 | **Returnee** | System Title |
| 승부사 | **Gambler** | System Title |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 호승심 | polysemy | Competitive pride or fighting spirit; not merely a desire to test oneself. | test myself |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 150–154

## Plot

Four days after losing to Cheongpung, Jin Mukyung isolates himself and trains, realizing that his reputation as the Heaven Shaking Sword and one of the Ten Dragons and Phoenixes had made him a frog in a well. The defeat sharpens his ambition, and his Sword Energy becomes denser and more refined.

Jin Taekyung attempts to force open his Conception and Governor Vessels using his accumulated internal energy and the Scorching Yang Qi from the Blazing Flame Divine Pill. The attempt fails, slightly damages his acupoints, reduces his Sinews and Meridians by one, and leaves him severely injured. Cheongpung explains that Mae Jonghak forbade forcing the vessels open and agrees to train Taekyung after revealing that his own Governor Vessel opened naturally through enlightenment. Taekyung also persuades Hyuk Mujin to join the training.

Cheongpung makes them run to the training hall and climb a sheer cliff using the Wall Lizard Technique, without internal energy or weapons. He throws rocks at them throughout the exercise, rescues Mujin from a fall with the Zaha Divine Technique, and demands ten total ascents. Taekyung and Mujin complete the climbs over three days. Taekyung gains Strength, Agility, and Stamina during the training, acquires Wall Lizard Technique, levels up with 10 Stat Points and 10 Skill Points, and advances from Beginner Trainee to Intermediate Trainee. Cheongpung’s satisfaction generates the linked quest *Sword Saint Training: A Secondhand Experience—2*. Taekyung jokingly claims to have come from another world with a System, but Mujin does not believe him.

Meanwhile, Jang Childeuk begins guarding the Jin Family’s mostly unused training hall. The post is maintained as a symbol because Founder Jin Muryang allegedly trained beneath its cliff and opened the base with One Strike. Taekyung later falls from the cliff, slowing himself with a dagger and surviving through his physique and toughness. Childeuk and the other guard mistake him for a jiangshi until Childeuk recognizes him; Taekyung’s first words after waking mention Taecho Village again.

## Continuity

- Jin Mukyung lost to Cheongpung after roughly three hundred exchanges and has secluded himself to train. His ambition and Sword Energy have strengthened.
- Taekyung failed to force open the Conception and Governor Vessels, suffering slight acupoint damage and a one-point reduction in Sinews and Meridians.
- Cheongpung’s Governor Vessel opened naturally through enlightenment two years earlier; Mae Jonghak warned him never to force either vessel open.
- Cheongpung is training Taekyung and Hyuk Mujin with Mae Jonghak’s cliff-climbing method. The ten climbs are complete.
- Taekyung now has Wall Lizard Technique, 10 additional Stat Points, 10 additional Skill Points, and the Intermediate Trainee rank.
- *Sword Saint Training: A Secondhand Experience—2* has begun or been generated; the number of linked quests in the sequence remains unknown.
- Hyuk Mujin has accepted Taekyung’s training invitation and demonstrated persistence and martial talent. He does not believe Taekyung’s story about another world and a System.
- Jang Childeuk is now a martial artist directly under Jin Wikyung and guards the Jin Family training hall. He remains intensely loyal to the family.
- Taekyung survived his fall at the training hall but again mentioned Taecho Village after regaining consciousness. What Taecho Village is, and why he says “again,” remain unresolved.
- New Year’s Day is ten days away; Prince Shangshan Zhu Bao is expected at the Jin Family’s grand banquet around then.
- Cheongpung still lacks a martial title, which Zhu Bao requires before accepting his autograph.
- Mae Jonghak’s disappearance, Cheongpung’s unexplained origin, and the meaning of the crane that supposedly delivered him remain unresolved.

## Translation Decisions

- Render **임독양맥** as “Conception and Governor Vessels,” **근맥** as “Sinews and Meridians,” **기해** as “qi sea,” and **환골탈태** as “Bone Transformation.”
- Render **벽호공** as “Wall Lizard Technique,” **연무장** as “training ground,” **수련동** as “training hall,” and **청석** as “bluestone.”
- Render **진무량 조사** as “Founder Jin Muryang,” **천응** as “Heavenly Eagle,” **강시** as “jiangshi,” and **태초 마을** as “Taecho Village.”
- Render **초보 수련자** and **중급 수련자** as “Beginner Trainee” and “Intermediate Trainee.”
- Render **검성 수련 간접 체험기** and **검성 수련 간접 체험기-2** as “Sword Saint Training: A Secondhand Experience” and “Sword Saint Training: A Secondhand Experience—2.”
- Retain “His Highness” for formal **전하**, “king” for literal **왕**, “Sword God” for **검신**, “Sword Saint” for **검성**, and “Zaha Divine Technique” for **자하신공**.

### Prior accepted reading-copy tails

#### Chapter 156 tail (verified mastered)

…
get back up anyway!” I wasn’t so sure. I had a feeling I wouldn’t be getting back up this time. I silently stared at the undulating energy of the Zaha Divine Technique and the blazing Sword Energy before finally managing to speak. “L-let’s put away the Sword Energy.” Let me live too, you bastard. * * * *Whoosh!* The spearhead tore through the air. A fast, razor-sharp strike. Cheongpung rolled his shoulder aside, and the second and third attacks followed like a storm. “Hah!” With a shout, spearheads rained down. The martial art itself was simple and heavy. But the movements of the man wielding the spear were light and fast. Hidden between his efficient movements were unpredictable attacks. *Swish! Swish-swish-swish!* A smile tugged at Cheongpung’s lips as he narrowly evaded the spearhead. *Wow, this is fun. Was Benefactor always this good?* He beamed as he watched the young man pressing him relentlessly. Jin Taekyung. They hadn’t known each other long, but he was the Benefactor who had helped Cheongpung in many ways. When Jin Taekyung had given him every last candied hawthorn skewer[^1] at their first meeting, Cheongpung had nearly cried. [^1]: Traditional fruit skewers coated in hardened sugar. *He’s a good person. He gave me something so precious.* Grandfather had been wrong. He had said Murim was crawling with frightening people who were vicious and utterly ruthless, but everyone Cheongpung had met was gentle and kind-hearted. He didn’t even dislike the Senior from the Zhongnan Sect whom he’d injured through his own mistake not long ago. *He’s my Senior, so he can’t be a bad person.* As far as Cheongpung knew, the bond between Seniors and Juniors was no ordinary relationship. It was a close tie forged by something thicker than blood. And Grandfather had always told him to protect the weak. The Senior from the Zhongnan Sect had been weak in martial arts. Cheongpung had felt terrible for hurting him. *But…* It was nice that there was no reason to feel bad about Jin Mukyung and Jin Taekyung. They were the strongest people Cheongpung had met since leaving Huashan. Even now, as he exchanged blows with Jin Taekyung, he was enjoying himself immensely. *Whoosh!* Cheongpung easily dodged the spear thrusting toward his shoulder, then burst out laughing despite himself. “Hehe.” “You laughing?” “Because I’m happy.” “You really need to watch what you say. That’s a dangerous thing to say.” *Swish-swish-swish!* Six killing attacks and twice as many feints came raining down from every direction. But Cheongpung was no longer where he had been. Jin Taekyung pierced the faint afterimage and shouted with the expression of someone who had seen a ghost. “What the hell was that?” “Dark Fragrance Drift. Hehe.” “That’s cheating!” “Would you like me to teach you?” “Great Hero Cheongpung, as for me, I’ve been barely scraping by in this harsh world with the paltry Jin Family’s Manoeuvre Technique…” “Oh, right. Grandfather told me not to teach it to anyone.” “This little bastard?” *Whoosh!* Jin Taekyung changed direction and thrust low. Just before the fiercely spinning spearhead pierced his instep, Cheongpung raised his foot with dazzling speed and pressed the spearhead down toward the ground instead. *Scrape!* “Wow, that was a little dangerous.” But Jin Taekyung wasn’t listening to him. With a short shout, he lifted the spear shaft beneath Cheongpung’s foot. “Hah!” “Benefactor, it’s no use. This is the Thousand-Catty Drop[^2]—” [^2]: A catty is a traditional East Asian unit of weight; the technique’s name evokes immense downward force. *Whoosh!* The next moment, Cheongpung felt himself floating. Jin Taekyung’s tremendous strength whipped the spear shaft skyward, flinging Cheongpung’s feet clear and leaving them treading empty air. He lost his balance for an instant and hurriedly drew up his internal energy. *Boom! Boom! Swish-swish!* The force of the Falling Flower Chasing Shadow Palm struck the air and shoved his body backward. A split second later, Jin Taekyung’s spear stabbed and slashed through the space where Cheongpung had been. *Wow.* Jin Taekyung’s strength was beyond Cheongpung’s imagination, even if it was still inferior to his grandfather’s. No. It wasn’t just his strength. He had incredible stamina, enough to fall countless times and keep getting back up. Agility that shouldn’t have been possible for someone with his build. And tremendous Toughness. *Even the way he uses martial arts is different from everyone else.* Cheongpung was a Peak master. He had been raised by the Sword Saint and had grown up watching the Sword Saint’s martial arts. He could gauge an opponent’s level from a single move and half a form of the martial arts they displayed. *Young Hero Jin Mukyung was sharp.* Jin Mukyung, whom he’d dueled a few days earlier, possessed an aura that seemed sharp enough to cut anyone who touched it. His martial arts were the same. But despite sharing the same blood, Jin Taekyung’s disposition and martial arts were the exact opposite of his brother’s. *What should I call this?* Though his martial arts were rough, still unrefined, and otherwise unremarkable, his movements created a strange tension. His aura seeped out naturally… “Whew. You coming? If not, I’m coming to you.” At the sight of the man striding toward him, Cheongpung finally thought of a word. *Wildness.* A beast hell-bent on biting through its prey’s throat. Jin Taekyung’s claws had not yet been honed, and that was precisely why they seemed even larger.

#### Chapter 157 tail (verified mastered)

…
was merely a consolation meant to preserve his pride. But Cheongpung was different. *Swish, swish-swish-swish!* The spearhead surged in from every direction, only to slice uselessly through empty air. Cheongpung’s face remained calm as he effortlessly dodged every attack. Then his hand blurred, and a streak of light split the air. *Whoosh! Boom!* “Hng!” Jin Taekyung let out a groan amid the thunderous impact. He had barely blocked the sword, but sword strikes poured toward him like a torrential downpour. Watching the scene, Hyuk Mujin opened his mouth without realizing it. At that moment, a single thought filled his mind. *Graceful.* That was the only way to describe it. Cheongpung’s movements were delicate and fluid, like the brushstrokes of a master painter. They resembled flower petals drifting and fluttering down at the end of the season. Hyuk Mujin watched in a daze before suddenly muttering, “Plum Blossom Sword Technique…” He had never seen Huashan’s martial arts before. But he could be certain of one thing. The very essence of Huashan martial arts had seeped into every one of Cheongpung’s movements. *He’s a monster. A monster in every sense of the word.* But “monster” was not a word that applied only to Cheongpung. *Swish-swish-swish-swish!* *Ka-ga-gang!* Another man was blocking every strike of the Plum Blossom Sword Technique unleashed by the Sword Saint’s disciple. The young man with a powerful build and striking, ruggedly handsome features ground his teeth. “Fuck, Huashan really made its martial arts a goddamn nightmare!” If Huashan had heard the thick profanity Jin Taekyung spat out, the entire sect would have turned upside down. A rough aura poured from his body. Its domineering force momentarily suppressed Cheongpung’s fluid grace before flowing straight into a counterattack. *Whoooosh! Boom!* A ferocious strike. Cheongpung went flying after blocking the spear amid the thunderous impact. Jin Taekyung had knocked aside Cheongpung’s offensive with a single move, but he immediately frowned. “Ow, that stings.” *Slice.* Before his words had even ended, the black martial robes he wore split open in a long tear. Several long wounds scored his exposed chest, blood welling freely from them. “What martial art was that?” “The Heavenly Eagle Claw.” “You really do have everything.” “Would you like me to teach you?” “You’re allowed to?” “Oh, I just remembered. My grandfather told me not to teach it to outsiders.” “Again? I knew it.” “Would you like to join Huashan?” “No!” Jin Taekyung shouted and kicked off the ground, charging forward. His movements were instinctive, like those of a wild beast, yet they barely retained the form of martial arts. Hyuk Mujin shuddered. *Why does that man get scarier the longer I watch him?* Everyone had their own distinctive aura. Jin Taekyung’s was tenacious and fierce. There was something about it that struck fear into anyone watching him. *It isn’t about his martial arts.* Jin Taekyung was certainly a highly skilled master, but he was not yet the equal of Cheongpung, the Sword Saint’s disciple and a true Peak master. Yet Hyuk Mujin had watched him from close by for the past several months, and he could say this with certainty. *Even if the sky fell, that man would survive.* No matter what kind of hell Jin Taekyung was thrown into, Hyuk Mujin felt certain he would return alive. Three Peak masters had tried to kill him so far, but in the end, they had been the ones to fall. In Murim, the one who survived was the strong one. And Jin Taekyung had survived to the bitter end. Besides… *Captain’s rate of growth is beyond imagination.* It was something Hyuk Mujin knew because he had watched him from closer than anyone else. From the moment Jin Taekyung defeated Jopil, One Question, One Kill, after a desperate battle to this very moment as he fought Cheongpung— Jin Taekyung was growing stronger every day. *And that’s still true right now.* Just a few days ago, he hadn’t been able to last even a hundred moves against the supreme techniques of Huashan that Cheongpung unleashed. But now? Hyuk Mujin had personally watched them exchange well over three hundred moves. Even after being struck by the Heavenly Eagle Claw, a martial art taught only to disciples of Huashan’s main sect, Jin Taekyung’s sole reaction had been, “Ow, that stings.” *He’s a monster. A monster.* Everyone around them was around the same age, and they were all Peak or advanced First Rate. Wasn’t that taking things too far? It seemed as though nothing but monsters surrounded him. Hyuk Mujin let out a deep sigh and recalled what Jin Taekyung had told him a few days earlier during their Wall Lizard Technique training. *If you don’t want to lose something precious, then risk your life and do it now. Working yourself to death while you’re still breathing is better than dying, isn’t it?* Those words were true. You had to work yourself to death to survive and become strong. Every second counted if you wanted to avoid being swept away by the waves of Murim. After silently watching the two men spar for a while, Hyuk Mujin rose to his feet. *I can’t finish this with just my little toe.* He had to become stronger. Strong enough to be recognized as Jin Taekyung’s right arm—or perhaps his heart. And… *Strong enough for everyone to remember the name Hyuk Mujin.* He gripped his sword case tightly.

## Korean source

```text
＃158화



칠주야(七晝夜).

청풍과의 비무를 시작한 지도 일곱 번의 밤낮이 지났다. 나는 눈을 감은 채 생각했다.

‘퀘스트 창에 적힌 대로라면 원단 전까진 청풍을 이겨야 하는데…….’

이제 고작 사흘밖에 남지 않았다. 내가 지금까지 청풍을 상대로 몇 번이나 싸웠더라?

적어도 60회 이상의 비무를 치렀다는 사실만 안다. 물론 단 한 번의 예외도 없는 깔끔한 전패(全敗) 행진이다.

‘심지어 검기는 쓰지도 않았지.’

지금의 청풍은 전력을 다하지 않고 있다. 절정 고수가 검기를 쓰지 않는다는 건 사실 엄청난 페널티였지만 굳이 검기를 사용하지 않아도 청풍은 강했다.

어린 시절부터 검성 매종학의 지도 아래, 화산파의 절기를 익혀 온 녀석이다.

현 정파 무림 최고의 후기지수 중 하나로 꼽히는 진무경도 청풍에게 패배했다.

‘진무경이 부상을 입은 상태긴 했지만…… 확실히 달라.’

질리도록 보았던 청풍의 움직임을 떠올렸다. 그야말로 유려(流麗), 그 자체다.

그가 익힌 무공의 특성이기도 하겠지만 무엇보다 스스로의 강함이 뒷받침되어야 가능한 것이기도 했다.

‘나보다 한 수 위라 이거지.’

사실 나도 팬티 속까지 탈탈 털어 보여 준 것은 아니다.

매번 그 역할을 톡톡히 해내는 스킬인 일섬과 인벤토리 시스템, 그리고 청풍의 검기에 맞설 수 있는 [이름 모를 검]도 있다.

하지만 이건 비무지, 목숨이 걸린 생사결이 아니다.

‘무공으로 승부해야 돼.’

내게 있어 시스템은 최후의 한 수다.

한 끗 차이로 목숨이 오고 가는 싸움에서 전세를 뒤엎기도 하지만 시스템을 이용했는데도 공격이 막힌다면 날 기다리는 것은, 죽음뿐이다.

말 그대로 최후의 한 수. 그다음은 없다.

‘매번 싸울 때마다 시스템에 의존할 수는 없지.’

천하는 넓고, 고수는 많다.

언제 맞닥트릴지 모르는 강한 적들에게 대비하기 위해서는 내 무공을 갈고 닦는 것이 첫 번째다.

“후우.”

깊은 날숨과 함께 도도히 흐르던 45년의 공력이 다시 단전에 똬리를 틀었다.

띠링.



- [운기조식]을 성공적으로 끝마쳤습니다.

- [진가심법]의 경지가 미약하게 상승합니다.

- 체력과 피로가 회복됩니다.



눈을 뜨자 치열한 접전을 벌이고 있는 청풍과 혁무진이 가장 먼저 시야에 들어왔다.

퍽! 퍼버버버벅!

“크허억!”

“…….”

정정한다. 치열한 접전이 아니라 박 터지게 맞는 것으로.

소나기처럼 쏟아지는 복호권의 초식에 정신을 못 차리던 혁무진이 이를 악물었다.

“합!”

녀석의 손에 들려 있던 검이 빛살처럼 뻗어 나간다.

변화무쌍한 초식, 심상치 않은 무리가 엿보이는 검공은 아니지만 기본기 하나는 확실하다. 아마 지금까지 수천, 수만 번도 넘게 같은 검을 휘둘렀을 것이다.

쉭! 쉬쉭!

머리와 어깨, 이어서 가슴까지. 순식간에 세 번의 공격을 피해 낸 청풍의 가슴을 향해 혁무진이 검을 찔렀다.

쐐애애액!

군더더기 없이 깔끔하고 날카로운 일격. 그러나 상대가 나빴다.

“와, 많이 느셨는데요?”

빙긋 웃는 청풍의 검지와 중지 사이, 힘이 잔뜩 들어간 검신이 부르르 떨렸다.

공수납백인(空手拉白刃).

상대방보다 무공이 월등히 높아야 가능한 수법이다.

뜻밖의 수치 플레이에 혁무진의 얼굴이 붉게 달아올랐다.

“흐읍!”

“힘줘 봤자 소용 없…….”

순간 청풍의 눈이 커다래졌다.

붙잡힌 검에 힘을 주는 듯싶던 혁무진이 돌연 검 자루를 놓고 그의 품 안으로 뛰어들었기 때문이었다.

‘저 자식 봐라.’

피식 웃음이 나왔다. 지금까지 정직한 무공을 펼치던 혁무진이 저러는 이유를 대충 알 것 같았기 때문이다.

‘서당 개 삼 년이면 풍월을 읊는다더니.’

저건 내가 자주 쓰던 방법이다. 무인에게 있어 생명과도 같은 병장기를 버리고 적의 의표를 찔러 실리를 취하는 것.

좋은 시도지만, 단 한 가지 실수가 있다면 이런 수법을 쓰기에는 상대방의 실력이 너무 높다는 거다.

펑!

북 터지는 소리와 함께 한 사람의 신형이 훨훨 날았다. 나는 실실 웃으며 내 발 앞까지 날아온 혁무진을 내려다봤다.

“졌냐?”

한바탕 기침과 헛구역질을 쏟아 낸 혁무진이 퉁명스럽게 대꾸했다.

“다 봤으면서 뭘 물어보십니까?”

“몇 번째야?”

“이걸로 벌써 아흔 번쨉니다.”

“조만간 백 번 채우겠네. 별호로 백전백패 어떠냐?”

“사양하겠습니다.”

“그래도 마지막은 괜찮았어.”

내 칭찬에 혁무진의 귀가 움찔거렸다.

“정말요?”

“응. 근데 수준 차이 너무 나더라. 상대 봐 가면서 해라.”

“그럼 그렇지. 웬일로 칭찬을 해 주시나 했네.”

“그렇게 해서 한 대 때려 볼 수나 있겠냐?”

“청풍 소협이 장법만 안 썼어도 한 대 정도는 때릴 수 있었다고요.”

입이 댓 발이나 튀어나온 혁무진이 투덜거릴 때 청풍이 해맑은 표정으로 뛰어왔다.

“괜찮으세요?”

“아니, 권법만 쓰기로 한 거 아니었습니까?”

“지금부터 쓰려고요. 실력이 생각보다 훨씬 빨리 느셔서.”

“크흠. 그럼 뭐 그렇게 하시든가.”

혁무진 저놈 저거, 입 찢어지려고 하는 것 봐라.

평소 같았으면 끼어들어 면박이라도 줬겠지만 청풍의 말에는 나도 상당 부분 동감했다.

‘빨리 늘긴 하네.’

지난 일주일 동안 성장한 것은 나뿐만이 아니다. 혁무진도 마찬가지였다.

비록 청풍의 도움이 있었다고는 하나 한참 떨어지는 능력치로 벽호공 수련을 끝마쳤고, 청풍이 먼저 장법을 꺼낼 만큼 실력도 늘었다.

‘그뿐만이 아니지.’

나는 [기감]을 일으켰다. 혁무진의 레벨을 확인하기 위해서다.

띠링.



- [기감]을 사용하셨습니다. 현재 6성의 경지이므로 Lv.80 이하, 60장 이내의 대상을 탐색할 수 있습니다.

- [기감]으로 대상을 파악했습니다.



[Lv.50 혁무진]



불과 열흘 전에 확인했던 혁무진의 레벨은 48. 그러나 수련을 거치면서 2레벨이나 올랐다.

‘50레벨이라고? 벌써?’

나는 시스템으로 레벨을 확인함으로써 상대방의 힘을 대략적으로 가늠해 볼 수 있다.

다만 대부분의 사람들은 레벨이 정체되어 있거나, 아니면 레벨 업 속도가 매우 느려 알아차리기가 힘들었다.

‘그런데 혁무진 이 녀석은 쭉쭉 오르네.’

문득 혁무진을 처음 만났을 때가 생각난다.

당시 녀석은 고작 20레벨. 이미 60레벨을 넘긴 나만큼은 아니지만 어쨌든 녀석도 레벨 업 속도가 장난이 아니다.

‘내 옆에서 하도 굴러서 그런가.’

그러고 보니 나랑 함께 다니면서 고생이란 고생은 다 했다. 실전을 겪으면서 자연스럽게 저절로 단련된 건가?

신기한 생물 바라보는 듯한 내 시선에 혁무진이 물었다.

“왜 그러세요?”

“응? 아냐. 내가 보기에도 확실히 많이 늘었다 싶어서.”

“커흠, 커흐흠!”

“인심 썼다. 앞으로는 새끼손가락이다.”

“……인심이 박하시네요.”

“아픈 새끼손가락이라는 말, 못 들어 봤어?”

“그럼 제가 조장님의 아픈 새끼손가락이라는 말씀?”

“아니. 그냥 그런 말이 있으니까 알아 두라고.”

“…….”

“자, 이제 우리 백전백패 혁무진 대협은 뒤로 빠지시고.”

“그 별호 안 쓴다니까요!”

혁무진의 외침을 한 귀로 흘린 나는 호흡을 가다듬으며 앞으로 나섰다.

“어떻게, 운기조식 한 번 하실래요?”

청풍이 방긋 웃으며 대답했다.

“별로 움직이지도 않아서 땀도 안 났는데요, 뭘.”

무진이 울겠다, 울겠어.

나도 해맑게 미소 짓는 청풍을 따라 웃었다.

“이제 땀 좀 흘리시겠네.”

“은인 정도면 재밌는 상대죠.”

청풍답지 않은 도전적인 말투다. 하지만 지금껏 지켜본 바로는 이게 청풍의 본 모습이었다. 무인 청풍으로서의 호승심.

진무경을 상대로 검을 펼칠 때의 녀석이 단 한 순간도 웃지 않았던 것을, 나는 똑똑히 기억하고 있다.

“이제 재미없어질 텐데.”

“괜찮아요. 이기는 건 항상 재밌으니까. 헤헤.”

“그 말, 후회 안 할 자신 있어요?”

“네! 지금도 검기도 안 쓰고 이기는데요, 뭘!”

“…….”

와, 씨. 순간 울컥했네.

팩트 폭력에 동요한 가슴을 가라앉힌 나는 힘껏 창을 움켜쥐었다.

“이번에는 좀 다를걸?”

“할아버지께서 말씀하셨어요. 그런 말은 하수들이나 하는 소리다. 진짜 고수들은 행동으로 보여 준다.”

“걱정 말아요. 지금부터 그럴 생각이니까.”

“기대되네요.”

나는 여전히 싱글벙글 웃고 있는 청풍을 바라보며 마음속으로 중얼거렸다.

‘상태창 오픈.’

띠링.



상태창



[Lv.64 진태경]

직업 : 일류 무인

명성 : 2400 (+250)

칭호 : 5개 (칭호 효과 적용 중)

- 귀환자 (모든 능력치 +10)

- 산서잠룡 (모든 능력치 +15, 명성 +200)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 승부사 (일대일 전투 시 전투 관련 능력치 +10%)

- 중급 수련자 (수련 속도 +20%)

근력 : 205 (+30)체력 : 207 (+30)

민첩 : 200 (+30)지력 : 40 (+30)

매력 : 40 (+30)공력 : 45년

맷집 : 200 (+30)

잔여 포인트 : 100

- 잔여 포인트를 분배하십시오.





벽호공 수련과 비무를 통해 마침내 200을 돌파한 전투 스탯. 그리고 적을 만났을 때를 대비해 꼬박꼬박 적립해 두었던 잔여 포인트까지.

지금 이 순간만큼은 천하제일인이 부럽지 않다.

“내가 진짜 아끼고 있었는데…… 당신 때문에 쓰는 겁니다.”

“네?”

“검기, 자하신공. 뭐든 좋습니다. 전력을 다하세요.”

“그럼 너무 싱거운데요?”

“그건 맛을 보고 말씀하셔야지. 매운지, 싱거운지.”

말이 끝나기도 전, 내 머릿속에서는 이미 한 가지 명령이 시스템에게 전달되고 있었다.

‘민첩에 50포인트 부여.’

쏴아아아.

이 세상에서 오직 나만이 느낄 수 있는 기운이다.

어디서부터 흘러들어 왔는지 모를 미증유의 힘이 파도처럼 전신을 휩쓴 순간.

“우선 너구리 순한 맛부터 갑시다.”

쐐애애애액!

창이 지금껏 본 적 없는 속도로 움직이기 시작했다.



* * *



쉭, 퍼벙!

청풍이 목을 틀었다. 목 뒤로 질끈 묶은 머리카락이 공기와 함께 터져 나갔다.

그러나 창의 움직임은 거기에서 끝나지 않았다.

후웅, 쐐애애액!

사방에서 달려드는 십여 개의 창영(槍影). 청풍은 망설임 없이 발을 내디뎠다.

콰콱!

그나마 남아 있던 청석이 박살 나며 흙이 솟구쳤다. 진태경이 어느새 삼 장이나 뒤로 물러난 청풍을 보며 물었다.

“그럴 줄 알았지. 암향표(暗香飄)?”

“거기에 오행매화보(五行梅花步)를 섞었죠.”

“그게 되나?”

“되던데요?”

“그래서 맛은?”

“싱거워요. 한참.”

“그럴 수 있지. 아직은.”

말을 마친 진태경이 돌연 몸을 부르르 떨더니 씩 웃었다.

“지금부터는 진라면 매운맛.”

도무지 의미를 알 수 없는 말이 끝남과 동시에 진태경이 달려들었다.

태양을 찌를 듯이 치켜올린 창날이 무시무시한 파공성과 함께 내리그어졌다.

후우우우웅!

그 순간, 청풍은 발검(拔劍)했다. 어느새 그의 검신에서는 자줏빛 검기가 선명하게 맺혀 있었다.

아니, 검뿐만이 아니라 그의 전신에서 자하신공이 흘러나왔다.

쾅!

힘과 힘의 충돌. 그리고 하늘이 쪼개지는 듯한 굉음.

청풍의 입가에서 웃음이 사라졌다. 시큰한 손목에서 적지 않은 반발력이 전해졌다.

‘도대체 어떻게?’

다르다. 달라도 너무 다르다. 괄목상대(刮目相對)라는 말도 무색할 정도다.

눈을 비비기도 전에 진태경은 강해졌고, 또 다시 강해졌다.

‘그리고 공력이…….’

자하신공은 극양의 성질을 띤 내공심법이다. 그러나 진태경의 창에서 전해지는 공력도 그에 못지않았다.

청풍은 검을 찍어 누르는 창날로부터 희미한 떨림을 느꼈다.

우웅, 우우웅.

절정의 벽에 다다른 자들은 벽을 깨기 전 누군가의 울음소리를 듣는다고 했다.

무인의 목숨과도 같은 병장기가 가장 먼저 주인의 변화를 알아차리는 것이다.

경지에 다다른 공력과 절정 고수가 될 준비를 끝마친 근골.

그 모든 것이 충족되었을 때 지금 같은 소리가 난다.

‘검명(劍鳴)?’

검이 아니라 창이니 창명(槍鳴)이다.

입을 벌리는 청풍을 보며 진태경이 씩 웃었다.

“자, 지금부터는 푸라면 매운맛.”

꾸구구국.

천근거력과 함께 창의 울음소리가 더욱 크게 울려 퍼졌다.
```

## Current accepted English baseline

```markdown
# Chapter 158

Seven days and nights.

Seven days and nights had passed since I began sparring with Cheongpung. I thought with my eyes closed.

*If I’m supposed to defeat Cheongpung before New Year’s Day, just like the Quest says…*

There were only three days left. How many times had I fought Cheongpung by now?

All I knew was that we had dueled at least sixty times. Of course, I had lost every single one of them without exception.

*He hasn’t even used Sword Energy.*

Cheongpung wasn’t fighting at full strength. It was an enormous handicap for a Peak master not to use Sword Energy, but Cheongpung was still strong even without it.

He had learned Huashan’s supreme martial arts under the guidance of Sword Saint Mae Jonghak since childhood.

Even Jin Mukyung, considered one of the greatest young prodigies in the current orthodox Murim, had lost to Cheongpung.

*Although Jin Mukyung was injured at the time… this is definitely different.*

I recalled Cheongpung’s movements, which I had seen so many times that I was sick of them.

They were the very definition of grace.

That was probably a characteristic of the martial arts he had learned, but it was only possible because his own strength supported them.

*He’s simply a cut above me.*

Of course, I hadn’t shown him everything, right down to my underwear.

I still had One Annihilation, the Inventory System, and the Unnamed Sword, which could stand against Cheongpung’s Sword Energy.

But this was a spar, not a life-and-death duel.

*I have to win with martial arts.*

As far as I was concerned, the System was my final card.

In a battle where life and death could be decided by the smallest margin, the System could overturn the tide of battle. But if even a System-assisted attack was blocked, then all that awaited me was death.

It was literally my final card. There was nothing after that.

*I can’t rely on the System every time I fight.*

The world was vast, and there were many masters.

To prepare for powerful enemies who could appear at any moment, sharpening my martial arts had to come first.

“Whew.”

With a deep exhale, the forty-five years of internal energy that had been flowing steadily curled back up in my dantian.

> **System**
>
> - You have successfully completed circulating your qi.
> - The realm of the Jin Family’s Cultivation Technique has risen slightly.
> - Your stamina is restored and your fatigue relieved.

When I opened my eyes, the first thing I saw was Cheongpung and Hyuk Mujin locked in a fierce battle.

*Whack! Whack-whack-whack!*

“Gaaagh!”

“…”

I take that back. It wasn’t a fierce battle. Mujin was just getting beaten until his head nearly burst.

Hyuk Mujin was unable to keep his senses amid the forms of the Crouching Tiger Fist raining down like a sudden shower. He gritted his teeth.

“Hah!”

The sword in his hand shot forward like a ray of light.

The forms weren’t particularly unpredictable, nor did the sword technique reveal any extraordinary profundity, but his fundamentals were solid. He had probably swung that same sword thousands, perhaps tens of thousands, of times by now.

*Swish! Swish-swish!*

Head, shoulder, then chest. After avoiding three attacks in an instant, Cheongpung found Hyuk Mujin’s sword thrusting toward his chest.

*Whooosh!*

A clean, sharp strike without any unnecessary movement.

Unfortunately, his opponent was too strong.

“Wow, you’ve improved a lot!”

Between Cheongpung’s index and middle fingers, the blade he had seized trembled under the force being applied to it.

Empty-Hand Seizes the Blade.[^1]

It was a technique possible only when one’s martial arts were overwhelmingly superior to the opponent’s.

Humiliated by the unexpected display, Hyuk Mujin’s face flushed red.

“Hngh!”

“It won’t do you any good to put more force into—”

Cheongpung’s eyes suddenly widened.

Hyuk Mujin had appeared to be putting more strength into the sword he had seized, but he abruptly released the hilt and lunged into Cheongpung’s arms.

*Look at that bastard.*

I let out a quiet laugh. I had a pretty good idea why Hyuk Mujin, who had used honest martial arts until now, had suddenly pulled something like that.

*They say even a dog at a village school can recite poetry after three years.*

That was a method I often used. Abandoning the weapon that was as precious as life itself to a martial artist, catching the enemy off guard, and taking advantage of the opening.

It was a good attempt. But if there was one problem, it was that his opponent was far too strong for a trick like this.

*Boom!*

With a sound like a drum bursting, someone’s body went flying. I grinned as I looked down at Hyuk Mujin, who had landed right in front of my feet.

“Did you lose?”

After coughing and gagging for a while, Hyuk Mujin answered irritably.

“You saw everything. Why are you asking?”

“What number was that?”

“That makes ninety.”

“You’ll hit a hundred soon. How about Hundred Battles, Hundred Losses as your nickname?”

“I’ll pass.”

“Still, the last one wasn’t bad.”

Hyuk Mujin’s ears twitched at my praise.

“Really?”

“Yeah. But the difference in skill was way too great. Size up your opponent before trying that.”

“I knew it. I was wondering why you were praising me for once.”

“Do you think you could have landed even one hit with a move like that?”

“If Young Hero Cheongpung hadn’t used a palm technique, I could have hit him at least once.”

As Hyuk Mujin grumbled with his lower lip sticking out, Cheongpung ran over with an innocent expression.

“Are you all right?”

“No, weren’t you going to use only fist techniques?”

“I was going to start using palm techniques now. You’ve improved much faster than I expected.”

“Ahem. Then go ahead and do that.”

Look at him. Mujin’s mouth was about to split open.

Normally, I would have interrupted to give him a hard time, but I agreed with Cheongpung to a considerable extent.

*He really is improving quickly.*

I wasn’t the only one who had grown over the past week. Hyuk Mujin had as well.

Even though he had Cheongpung’s help, he had completed his Wall Lizard Technique training despite having far inferior stats. He had also improved enough for Cheongpung to bring out his palm techniques first.

*That’s not all.*

I activated Qi Sense to check Hyuk Mujin’s Level.

> **System**
>
> - You used **Qi Sense**. At your current six-star realm, you can search for targets at Level 80 or below within 60 jang.
> - **Qi Sense** has identified the target.
>
> **Lv. 50 Hyuk Mujin**

Only ten days ago, Hyuk Mujin had been Level 48. But after training, he had gone up two Levels.

*Level 50? Already?*

By checking Levels with the System, I could roughly gauge an opponent’s strength.

The problem was that most people’s Levels either stagnated or rose so slowly that it was difficult to notice.

*But this guy’s Level keeps shooting up.*

I suddenly remembered when I had first met Hyuk Mujin.

Back then, he had been only Level 20. He wasn’t anywhere near me—I had already passed Level 60—but even so, his Level-up speed was no joke.

*Maybe it’s because he’s been dragged around with me.*

Now that I thought about it, he had gone through every kind of hardship while traveling with me. Had actual combat naturally trained him?

Under my gaze—as though I were studying some fascinating creature—Hyuk Mujin asked,

“Why are you looking at me like that?”

“Huh? Nothing. I was just thinking that you really have improved a lot.”

“Ahem. Ahem!”

“That was me being generous. From now on, you’ll get the pinky.”

“…You’re awfully stingy.”

“Never heard the phrase about a painful pinky?”

“So I’m your painful pinky, Captain?”

“No. It’s just a saying. Remember it.”

“…”

“All right, our Great Hero Hyuk Mujin of Hundred Battles, Hundred Losses can step back now.”

“I told you I’m not using that nickname!”

I let Hyuk Mujin’s shout pass in one ear and stepped forward after steadying my breathing.

“How about circulating your qi once?”

Cheongpung smiled brightly.

“I barely moved, so I didn’t even sweat. Why would I?”

Mujin was going to cry. He really was.

I smiled along with Cheongpung’s radiant expression.

“You’re going to sweat a little now.”

“Someone at your level makes an interesting opponent, Benefactor.”

That was an unusually challenging tone for Cheongpung. But based on everything I had seen so far, this was his true nature—the competitive pride of Cheongpung the martial artist.

I clearly remembered how he hadn’t smiled even once while fighting Jin Mukyung with his sword.

“It’s going to get less fun now.”

“That’s all right. Winning is always fun. Hehe.”

“Are you sure you won’t regret saying that?”

“Yes! I’m already winning without using Sword Energy!”

“…”

Damn. That hit a nerve.

I calmed my shaken heart after being struck by such blatant facts and gripped my spear tightly.

“This time will be different.”

“My grandfather told me something. He said only weaklings say things like that. True masters show it through their actions.”

“Don’t worry. That’s what I intend to do now.”

“I’m looking forward to it.”

I looked at Cheongpung, who was still grinning from ear to ear, and murmured inwardly.

*Open Status Window.*

> **System**
>
> **Status Window**
>
> **Lv. 64 Jin Taekyung**
>
> **Job:** First Rate martial artist  
> **Fame:** 2,400 (+250)  
> **Titles:** 5 (Title effects active)
>
> - **Returnee** (All stats +10)
> - **Sleeping Dragon of Shanxi** (All stats +15, Fame +200)
> - **Scion of a Great Family** (All stats +5, Fame +50)
> - **Gambler** (Combat-related stats +10% in one-on-one combat)
> - **Intermediate Trainee** (Training speed +20%)
>
> **Strength:** 205 (+30)  **Stamina:** 207 (+30)  
> **Agility:** 200 (+30)  **Intelligence:** 40 (+30)  
> **Charm:** 40 (+30)  **Internal Energy:** 45 years  
> **Toughness:** 200 (+30)
>
> **Remaining Points:** 100
>
> - Distribute your remaining points.

My combat stats had finally broken through 200 thanks to training the Wall Lizard Technique and sparring. And I still had the points I had diligently saved in preparation for encountering an enemy.

At this moment, I wasn’t envious even of the greatest under heaven.

“I was really saving these up… but I’m using them because of you.”

“Huh?”

“Sword Energy, the Zaha Divine Technique—anything is fine. Give it everything you’ve got.”

“Then it’ll be too bland.”

“You should taste it before deciding whether it’s spicy or bland.”

Before I had even finished speaking, an order had already been delivered to the System in my head.

*Assign fifty points to Agility.*

*Whooosh.*

It was a force only I could feel in this world.

The moment an unprecedented power, whose origin I could not identify, flowed through my entire body like a wave—

“Let’s start with mild Neoguri.”[^3]

*Whooosh!*

My spear began moving at a speed it had never reached before.

* * *

*Swish—boom!*

Cheongpung twisted his neck. His hair, tied tightly behind his head, burst through the air.

But the spear’s movement did not end there.

*Whoom—whooosh!*

More than ten spear images charged in from every direction. Cheongpung stepped forward without hesitation.

*Crack!*

The remaining bluestone shattered, and dirt erupted into the air.

Jin Taekyung looked at Cheongpung, who had retreated three jang in an instant, and asked,

“I knew you’d do that. Dark Fragrance Drift?”

“I mixed it with the Five-Element Plum Blossom Steps.”[^2]

“Can you even do that?”

“It worked, didn’t it?”

“And how does it taste?”

“It’s bland. Very bland.”

“That can happen. For now.”

After finishing his sentence, Jin Taekyung suddenly shuddered from head to toe and grinned.

“From now on, Jin Ramen spicy flavor.”

The incomprehensible words had barely left his mouth when Jin Taekyung charged.

The spearhead rose as if it would pierce the sun, then slashed downward with a terrifying sound as it tore through the air.

*Whoooooosh!*

At that moment, Cheongpung drew his sword. Vivid violet Sword Energy had already gathered along its blade.

No—the Zaha Divine Technique was flowing from his entire body, not just his sword.

*Boom!*

Force collided with force.

A thunderous roar rang out as though the sky itself were splitting apart.

The smile vanished from Cheongpung’s lips. A considerable backlash traveled through his aching wrist.

*How?*

It was different. Far too different.

Even the phrase *looking at someone with new eyes* failed to describe it.

Before he could even rub his eyes, Jin Taekyung had grown stronger—and then stronger again.

*And his internal energy…*

The Zaha Divine Technique was an internal-energy cultivation technique of the Extreme Yang nature. But the internal energy transmitted through Jin Taekyung’s spear was no less powerful.

Cheongpung felt a faint trembling from the spearhead pressing down on his sword.

*Vrrr, vrrr.*

They said that those who reached the wall of the Peak realm could hear someone crying before breaking through it.

A martial artist’s weapon, as precious as life itself, was the first to notice its owner’s transformation.

Internal energy that had reached the realm, and a physique ready to become a Peak master.

When all of those conditions were met, this was the sound that rang out.

*A Sword Cry?*

It wasn’t a sword. It was a spear.

So it was a Spear Cry.

As Cheongpung stared with his mouth hanging open, Jin Taekyung grinned.

“All right. From now on, Puramyeon spicy flavor.”

*Krrrnnng.*

With the force to move a thousand catties, the spear’s cry rang out even louder.[^4]

[^1]: *Empty-Hand Seizes the Blade* is a technique for catching an opponent’s weapon between the bare fingers.

[^2]: *Five-Element Plum Blossom Steps* is a footwork technique combining Five-Element movement with Plum Blossom steps.

[^3]: Neoguri, Jin Ramen, and Puramyeon are instant-noodle names; Taekyung uses their flavor labels as a joke.

[^4]: A catty is a traditional East Asian unit of weight. “A thousand catties” is an expression for tremendous force.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 158`.

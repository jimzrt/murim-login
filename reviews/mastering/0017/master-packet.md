# Master Edit Task — Chapter 17

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

| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 이소군    | **Lee Seogeun**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 영약     | **elixir**                                       |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 제자     | **Disciple**                                 |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 칭호               | **Title**                      |
| 아이템              | **Item**                       |
| 로그아웃             | **Logout**                     |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 한엽 | **Han Yeop** |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 10–14

## Plot

Taekyung enters a staged confinement in the training hall, secretly arranged by Jin Wikyung to protect him from the Elder Council. He acquires and trains the Jin Family’s Spear Technique, combines it with his Manoeuvre Technique, and creates a crater with the Sky-Piercing Strike. The Unity of Self and Object achievement grants him the Clear-Heart Pill, a ring that improves concentration and cultivation. During three days of intensive training, his Cultivation Technique reaches the Third Stage, his Spear and Manoeuvre Techniques reach the Fourth Stage, and he reaches Level 14. Training Mode lets him practise against adjustable versions of opponents, including Hyuk Mujin.

After confinement ends, Taekyung is taken to the main assembly hall rather than allowed home. Lee Seogeun, a Level 30 envoy of the Mount Heng Sword Sect, accuses him of attempting to rape the sect leader’s daughter and demands that the Jin Family withdraw from every commandery and county except Taiyuan. When Jin Wikyung refuses the demand and the duel, Taekyung accepts the System’s Duel Quest to prevent war and his designation as a public enemy. Lee initially overwhelms him with killing intent, but Taekyung blocks more than twenty strikes, kicks Lee’s exposed chest, and breaks through the Intimidation effect. The duel continues with Taekyung promising to defeat him.

## Continuity

- Taekyung is Lv. 14. His Cultivation Technique is Third Stage; his Spear and Manoeuvre Techniques are Fourth Stage.
- The Clear-Heart Pill is a ring that steadies Taekyung’s mind and improves concentration and cultivation.
- Training Mode can summon prior opponents and partially adjust their abilities; Hyuk Mujin is Lv. 20.
- Taekyung’s three-day protective confinement has ended. He is at the main training ground, still not returned to his residence.
- Jin Wikyung is Taekyung’s protective eldest brother and Lesser Family Head; Wipeng restrains him from entering the duel and supports the protective plan.
- The Mount Heng Sword Sect and the Jin Family are sworn enemies. Lee Seogeun is a Lv. 30 envoy acting on Mount Heng’s behalf.
- The Myeongwollu evidence remains suspicious: witnesses claim Taekyung entered the wrong room while drunk and that someone heard screaming, while Taekyung denies the alleged assault through his amnesia pretence.
- Taekyung accepted the Duel Quest. Its reward is the Gambler title, EXP, and Fame 50; refusal would cause the Sex Fiend title, injury, war with Mount Heng, and public-enemy status.
- Taekyung can read and block Lee’s attacks despite the Level gap, has kicked Lee’s chest, and has lost the Intimidation status effect.
- The capsule’s purpose, route home, and the limits of Murim’s death and resurrection rules remain unresolved.

## Translation Decisions

- Retain **Mount Heng Sword Sect**, **Taiyuan**, **Myeongwollu**, **Lesser Family Head**, **Sound Transmission**, and the Jin Family’s **Cultivation**, **Spear**, and **Manoeuvre Techniques**.
- Render the achievement as **Unity of Self and Object**, the reward as the **Clear-Heart Pill**, and the quest titles as **Gambler** and **Sex Fiend**.
- Render Mount Heng’s demand as withdrawal from every commandery and county except Taiyuan.
- Preserve the brisk dark action-comedy, Taekyung’s self-mocking profanity, and the distinction between the first weapon clash (“Kra-kra-kraang”) and later cannon-like impacts.
- Preserve the gold-spoon/**God-Spoon** wordplay with a brief footnote where needed.

### Prior accepted reading-copy tails

#### Chapter 15 tail (verified mastered)

…
**Duel** Quest has been successfully completed! > > - Quest rewards will be distributed! > > - You have acquired the Title **Gambler**! > > - You have gained EXP and Fame! > > - An additional reward has been granted for your overwhelming performance! > > - **Jin Family’s Cultivation Technique** has risen to the Fourth Stage! > > - **Qi Sense** has risen to the Third Stage. You can now detect targets up to Level 50. > > - Level up! > > - Level up! > > - Level up! The System notifications rang out like celebratory fireworks. * * * The Mount Heng Sword Sect left. Since they had all arrived on horseback, the Jin Family of Taiyuan even had to lend them a carriage to transport the injured. But Lee Seogeun was one thing. Who was the other guy? Every one of his teeth was gone, and the cloth stuffed into his mouth was soaked with blood. Good Lord. What kind of bastard had— Just then, Jin Wikyung patted me on the shoulder with a solemn expression. “Well done. You did even better than I expected.” “Ah, yes. Thank you—” “Why are you looking at me like that?” *Because there’s blood splattered on your cheek.* I had no idea why, but in that brief span of time, he had somehow turned a man into a cripple. “So, what do you think?” “Pardon? What do you mean?” “About ending your confinement. It is true that your usual conduct has been disgraceful, but the remarkable performance you showed today is a great blessing for our family.” Jin Wikyung looked around as he continued. “What do the rest of you think?” The senior members looked displeased, but none seemed particularly inclined to object. Compared to the looks they had given me in the meeting hall earlier, I almost felt that they were favorable. *Is it because they’re Murim people?* In novels, Murim was a place where justice mattered, but strength came first. Maybe defeating Lee Seogeun had influenced them. “You should answer me. Hahaha.” …Or maybe it was because of Jin Wikyung. His mouth was smiling, but his eyes were not. Combined with the blood on his cheek, it was a scene straight out of a horror movie. “I wholeheartedly agree,” Wipeng said. Once Wipeng’s manipulation of public opinion was added to the mix, one by one, the others voiced their agreement. Jin Wikyung watched the coerced vote, enforced through a show of force, and smiled in satisfaction. * * * *Damn it. Damn it. Damn it!* Lee Seogeun bit down hard on his lip. Jin Taekyung’s face refused to leave his mind. *I lost? To trash like him?* The matter with the Jin Family of Taiyuan had given them more than enough justification. If the Mount Heng Sword Sect profited from it, all well and good. If the Jin Family refused and the conflict escalated into full-scale war, that would also have counted as a success. If he had turned Jin Taekyung into a half-cripple, word would have spread throughout Shanxi. The Jin Family of Taiyuan had suffered humiliation at the hands of the Mount Heng Sword Sect. But he had failed. *How could this have happened?* He had taken up a sword as a child. He wasn’t a genius, but neither was he mediocre. The second son of the Mount Heng Sword Sect. A promising young martial artist. A First Rate swordsman. He had always been someone others admired… *Damn it!* Everything he had possessed had been shattered today. For the first time, he had been brought to his knees by Jin Taekyung’s merciless violence—and lost consciousness. When he opened his eyes, he was already inside a carriage. Even this carriage belonged to the Jin Family of Taiyuan. Fire poured from Lee Seogeun’s eyes. *I’ll kill you. I’ll kill you with my own hands, Jin Taekyung!* Unable to contain his rising fury, he slammed his fist into the carriage wall. The carriage stopped. Lee Seogeun shouted harshly, “What are you doing? Don’t dawdle. Get moving again!” At that moment, the spot between his eyebrows prickled. - Get moving? We should. But going to the Mount Heng Sword Sect would be a little troublesome. *Sound Transmission?* “Who is it!” Lee Seogeun shouted, but no sound escaped his throat. His chest felt tight, and his throat hurt as if it were on fire. The carriage began moving again. - Let’s do this. Mount Beimang first. We can go to the Mount Heng Sword Sect afterward.[^2] *What does that—* It took no longer than a few blinks. His limbs went numb, and pain flared violently through his body. Lee Seogeun turned his trembling head. Someone wearing a mask was staring at him. “Grrk… grrrk.” *Who are you?* Instead of his voice, dark, discolored blood poured from his mouth. His vision blurred. The sounds around him grew distant. *Sa… save me…* That was his final thought. The next moment, he plunged headfirst into darkness. “Farewell, Young Hero Lee.” The masked man smiled brightly as he retrieved the large blue-black needle from the dead man’s brow. [^1]: *Ssaksuga norata*—“the sprouts are yellow”—means someone is a hopeless case. The line pushes yellow all the way to gold to make that worse, not to imply that he was born rich. [^2]: Mount Beimang is a traditional burial ground; “going to Beimang” means dying.

#### Chapter 16 tail (verified mastered)

…
been plain to see during the duel. And second. *I don’t have enough internal energy.* In terms of internal energy alone, Lee Seogeun had been ahead of me. No, he had been overwhelmingly ahead. What the hell had he eaten growing up? I had smashed him dozens of times with the shaft of my spear and pounded him one-sidedly from the mount, yet he had endured it all. He had even counterattacked and drawn on more internal energy at the very end. *I currently have ten years of internal energy.* Lee Seogeun probably had twenty years—twice as much as I did. That led me to a third realization. *The difference in internal energy determines the stage of one’s martial arts.* I had defeated Lee Seogeun, a First Rate martial artist. Yet the realm displayed by the System still listed me as Second Rate. I thought the reason lay in internal energy. Once I raised the one ability I lacked, wouldn’t my realm finally rise as well? After organizing my thoughts that far, another idea suddenly occurred to me. *This is basically just Hunter rank classification.* Every newly awakened Hunter had to visit a designated center to have their abilities, suitable profession, and mana capacity assessed. No matter how high their physical abilities were, anyone with insufficient mana received a frosty reception during their rank evaluation. That was also why mages started at D-rank at the lowest. Because of their profession, mages had plenty of basic mana from the start. *Still, the game is better than reality.* At least you could grow here. Reality had no such thing. Even I had only managed to get lumped in with the E-ranks after working my ass off for seven years. I was still an F-rank Hunter. Anyway, I had now drawn a rough outline. *My stats are high enough. I’ll cycle the Jin Family’s Cultivation Technique whenever I have time and prioritize Quests that reward EXP.* It had been over a week since I was trapped in this godforsaken game. I didn’t know what kind of nonsense was happening in the real world, but I could forget about being rescued. I needed to prepare properly and finish this. “Open Quest window.” Ding. > **System** > > **Quest** > > **Logout** > > You must now make your way through this harsh Murim. > > Become stronger and more famous. > > For the day that will someday come… > > **Grade:** Main Quest > **Restriction:** Jin Taekyung > **Mission:** Achieve the **First Rate** realm (Incomplete) > > &nbsp;&nbsp;&nbsp;&nbsp;Reach Level 30 (17 / 30) > > &nbsp;&nbsp;&nbsp;&nbsp;Reach Fame 500 (70 / 500) > > **Reward:** **Logout** “Ugh. This is brutal.” I sat cross-legged. Two days remained before my seclusion ended. I intended to gather as much internal energy as possible. > **System** > > Fame has risen by 3 due to the influence of the **Sleeping Dragon of Shanxi** rumor. The Fame-increase messages that chimed from time to time offered a small measure of comfort. * * * Late that night, the lights came on in the main assembly hall. At the Lesser Family Head’s request, a secret meeting of the family council had been convened. The hour was late and the summons abrupt, leaving several senior members with sour expressions. “A sudden summons? What is this about?” “Exactly. Calling us here at this hour without even telling us why…” “That’s what happens when the Lesser Family Head is still young. He doesn’t know procedure or etiquette.” “He must have grown rather full of himself after yesterday’s events. Though I suppose his only weakness has disappeared. No one expected the Third Young Master to be that capable.” “That must have taken the wind out of the Elder Council’s sails. They were probably preparing to make a major move over the Third Young Master.” “Hmph. Even now, the Head Elder ought to step forward and set the family straight.” “Careful. Watch your tongue…” At that moment, every sound abruptly stopped. The doors to the meeting room opened from both sides, and Jin Wikyung entered. Opinions of the Lesser Family Head varied among the senior members, but the silence that settled over the room the instant he appeared proved that he possessed the qualities of a leader. “Thank you all for answering my summons at this late hour.” Jin Wikyung took the seat of honor and spoke his opening words, but he found it difficult to continue. *What should he say? Where—and how—should he begin?* His head throbbed. But this was something he had to tell them. “The reason I called everyone here today is…” That was when a strange voice interrupted him. “It must be because of the Mount Heng Sword Sect.” The voice was bizarre. At first, it sounded like an old man’s. And yet it was young as well—rough one moment, smooth the next. There was also an inexplicable resonance to it. *Could it be…?* Jin Wikyung’s face twisted. The doors to the meeting hall, which had seemed as though they would never open again, began to part. Step. Step. Step. Five old men walked in as if they were gliding across the floor. The instant everyone recognized the old man at the front, they hurriedly stood and bowed their heads. “We pay our respects, Head Elder!” The Head Elder. He had appeared after keeping himself shut away from the world for years.

## Korean source

```text
＃17화



운기조식.

숨을 고르게 하여 기운을 다스리는 방법이다. 외부의 기를 내부로 받아들여 순환, 축적하는 행위.

지금 나는 진가심법이 적용된 운기조식을 하고 있었다.

‘이건 매번 신기하단 말이야.’

몰랐다. 내 몸에 이렇게 많은 혈이 존재하는지.

일전에 주워듣기로 인체의 혈도는 360여 개에 달한다고 했는데, 직접 심법을 운용하며 느낀 바로는 그 이상이다.

게임 속 가상 캐릭터라 그런가?

‘뭐 어때.’

단전에서 끌어 올린 10년의 공력이 신체를 순환한다. 공력이 자동차라면 혈도는 고속도로다. 나는 운전대에 앉아 그저 액셀을 밟으면 된다.

직선과 곡선이 반복되는 신체의 혈도를 달린 공력은 다시 단전으로 돌아간다.

‘그리고 여기서부터가 진짜 문제지.’

나는 길게 심호흡했다. 그리고 느꼈다.

내 의지에도 꿈쩍하지 않는, 거대한 바위처럼 단전을 차지하고 있는 또 다른 공력을.

‘넌 도대체 뭐냐.’

처음 운기조식을 했을 때부터 의문이었다. 터줏대감처럼 자리 잡고 있는 정체불명의 기운.

어디서, 어떻게 생겼고 왜 사용할 수 없는지는 모르겠지만 한 가지는 확실하다. 이 정체불명의 기운은, 내가 가진 10년의 공력보다도 더 큰 힘을 품고 있다.

‘지금까지는 건드릴 엄두가 안 났었지.’

정확히 말하면 건드릴 생각도 없었다. 며칠 전까지는 적당히 목숨 부지하면서 내심 구조를 기다리는 입장이었으니까.

하지만 이제는 다르다.

‘공력이 필요해.’

상황이 바뀌었다. 자력으로 탈출하려면 로그아웃 퀘스트 조건을 충족시켜야 하고, 충족 조건은 [일류]의 경지에 오르는 것.

그리고 일류가 되기 위해서는 이소군 정도의 공력이 필요하다는 것도 알았다.

‘내 것으로 만든다.’

나는 신중하게 공력을 움직이기 시작했다.

불안 반, 기대 반의 마음으로 정체불명의 기운을 향해 공력을 흘려보낸 순간, 깨달았다.

‘턱도 없네.’

공력은 엄연히 말해서 형체가 없는 기(氣), 그 자체다. 그런데 단순히 접촉하는 것만으로도 강한 거부와 반발이 느껴진다.

아니, 오히려 끌어당기기까지 한다. 이러다간 오히려 잡아먹힐 기세다.

‘야, 야, 야. 잠깐만!’

나는 황급히 공력을 회수했다. 끝까지 물고 늘어지는 정체불명의 기운을 뿌리쳤다. 동시에 시스템 알림이 울렸다.

띠링.



- [진가심법]을 수련했습니다. 공력이 소량 상승합니다.

- 반복 수련의 결과로 근맥과 근골이 1씩 상승합니다.



“아니, 뭐 저딴 게 다 있어?”

식겁한 마음을 진정시키며 상태창을 열었다.



상태창



[Lv.17 진태경]

직업 : 이류 무인

명성 : 70

칭호 : 4개 (칭호 효과 적용 중)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 가문의 수치 (모든 능력치 –5, 명성 –50)

- 초보 수련자 (수련 속도 +10%)

- 승부사 (일대일 승부 시 전투 관련 능력치 10% 향상)

근력 : 65체력 : 65

민첩 : 75 지력 : 10

매력 : 10 공력 : 10년

잔여 포인트 : 0





이제는 제법 높은 수치를 기록하고 있는 상태창이다.

비무 퀘스트를 통해 한꺼번에 3레벨이 올랐고, 30포인트를 근력, 체력, 민첩에 균등 분배한 결과였다.

하지만 상태창을 보는 내 마음은 쓰라렸다.

‘에휴, 공력만 제자리걸음이네.’

이 빌어먹을 시스템은 말만 공력이 상승했다고 하지, 정작 상태창에 표시되는 공력은 그대로다.

‘영단, 영약. 뭐 이런 거라도 하나 먹어야 되나?’

나는 진위경을 떠올렸다. 눈 딱 감고 형, 나 영단 하나만 주라, 하면 단칼에 거절하진 않을 것 같은데.

다음에 만나면 물어봐야겠다. 내 단전에 존재하는 정체불명의 기운에 관해서도.

쿠구궁.

그때 수련동의 입구가 열리더니 두 사람이 들어왔다.

“저어, 진 공자님?”

한엽이다. 그 뒤에는 처음 보는 무사가 서 있었다. 생긴 것만큼이나 무뚝뚝한 말투로 무사가 말했다.

“가로회의에 참석하시라는 소가주님의 명입니다.”

“소가주님이요?”

마침 잘됐네. 물어볼 거 있었는데.



* * *



“틀림없소. 몇 군데 부러지고 약간의 내상이 있었지만 그 정도로는 절대…….”

“확실해? 약왕당주의 이름을 걸고?”

“아, 맞다고. 내가 직접 진찰했다고!”

“맞으면 됐지. 왜 반말이야. 어? 같은 당주라고 대접해 주니까 내가 우스워 보여!”

“백호당주 당신이 먼저 반말했잖아!”

나는 멍하니 회의실 천장을 바라봤다. 사방에서 난무하는 고함과 욕설에 귀가 따끔거린다.

‘뭐여, 이게.’

내가 생각한 가로회의는 이런 게 아니었는데. 조용하고 질서정연한 분위기에서 서로의 의견을 주고받고 합의점을 찾는, 뭐 그런 거였는데…….

“당주라고 다 같은 당주인 줄 알아! 어디 의원 나부랭이가.”

“어린 노무 새끼가 말하는 본새 보소. 대침으로 회음혈을 쑤셔 버릴라.”

M자 탈모가 진행 중인 4, 50대 아저씨 두 명이 서로의 멱살을 잡고 흔드는 모습을 보니 골이 다 아파 온다.

문제는 이런 상황이 곳곳에서 벌어지고 있다는 사실이다.

그 때문인지는 몰라도 대부분의 사람들은 내가 문을 열고 들어와 자리에 앉은 것도 모르는 눈치였다.

- 왔느냐?

귀가 아니라 머리를 통해 들리는 듯한 목소리. 전음이다.

고개를 돌리자 상석의 진위경과 시선이 마주쳤다. 그는 피곤한 웃음을 지어 보였다.

- 난장판이지?

그러게. 이 난장판에 날 왜 불러 이 양반아.

내가 비난의 시선을 보내자 진위경이 찔리는 듯한 표정으로 전음을 날렸다.

- 나도 어쩔 수 없었다. 장로원에서 네 출석을 요구했거든. 어찌 되었건…… 태경이 네가 이 일에 연관된 것은 사실이니까.

장로원? 내가 이 일에 연관되어 있다고?

‘내가 무슨 일에 연관…… 아. 항산검문?’

나는 사람들의 고성방가 속에서 빠르게 퍼즐을 조합했다.

우선 최근에 나와 연관된 일이라면 항산검문밖에 없고, 그 일로 장로원인가 뭔가 하는 곳에서 나를 불러오게 했다. 이건데.

‘그러고 보니 못 보던 할아버지들이 있네.’

숫자는 네 명. 하나같이 검버섯이 가득한 얼굴에 머리가 하얗게 셌다.

그들은 탈모인들의 멱살잡이를 차가운 눈으로 바라보고 있었다. 누가 봐도 양로원, 아니 장로원이다.

- 그리고…… 대장로께서 와 계신다.

무심코 진위경 쪽으로 고개를 돌린 나는 흠칫했다.

‘뭐야. 저 노인네.’

언제부터 저기 있었지? 이제야 알아차렸지만 오늘의 상석은 두 자리였다. 진위경의 오른편에 앉아 나를 응시하고 있는 노인의 시선에 얼굴이 따끔거렸다.

‘저 노인이 대장로?’

백발, 백염, 백미. 오래된 그림에서 튀어나온 신선 같은 모습이다. 꼿꼿한 허리와 딱 벌어진 어깨, 팽팽한 피부는 나이가 무색해 보였다.

‘그런데 왜 저렇게 빤히 쳐다봐?’

눈에 힘을 빡 주고 대장로를 노려……보려다가 슬그머니 시선을 돌렸다. 붙으면 질 것 같아서가 아니라, 노인 공경이다. 노인 공경. 정말이다.

‘……쭈그리고 있자.’

그사이에도 진위경의 전음은 꾸준히 들려왔다.

- 기억을 잃어서 모르겠지만 대장로께서는 네 작은할아버님이자 가문의 최고 어르신이다. 언행에 각별히 신경 쓰거라.

아버지라는 양반 얼굴도 못 봤는데 작은할아버지란다.

어쩌면 이 자리에 사돈에 팔촌, 오촌 당숙까지 있을지도 모르겠다. 나는 진위경에게 살짝 고개를 끄덕여 보였다.

- 그리고…… 지금부터 벌어지는 일에 결코 당황해서는 안 된다. 차분하게 진실만을 고해라. 알겠느냐?

정확히 무슨 상황인지는 모르겠지만 진위경이 내 편이라는 사실은 확실했다. 이번에도 작게 고개를 끄덕이자 진위경이 희미한 미소를 지으며 일어났다.

“모두 정숙하십시오.”

공력이 담긴 목소리가 회의장을 휩쓸었다.

“이 자리는 태원진가의 가로회의이며, 우리는 중대한 사안을 위해 모였습니다. 때마침 증인이 도착했으니 심문을 시작하고자 합니다.”

어느새 조용해진 회의장의 중심. 사람들의 이목이 집중된 가운데 진위경이 입을 열었다.

“소가주이자 현 가주 대행의 권한으로 심문을 시작한다. 삼공자 진태경은 앞으로 나서라.”

나는 사람들의 시선을 느끼며 걸어 나왔다. 여기까진 충분히 예상했다. 괜히 나를 부르진 않았을 테니까.

하지만…….

“묻겠다. 네가 항산검문의 이소군을 독살했느냐?”

이건 예상 못 했다.



* * *



“아닙니다.”

간신히 입을 뗐다. 갑작스러운 말에 머릿속이 뒤죽박죽이다.

이소군이 죽었다고? 그것도 독에 중독돼서?

“진실을 고하라. 만일 거짓으로 밝혀진다면…….”

“이소군의 독살은 저와 아무런 연관이 없습니다.”

칼 같은 내 대답에 진위경은 안도 섞인 한숨을 내쉬었다.

- 지금처럼만 하면 된다.

심문은 빠르게 진행되었다. 그들은 묻고, 나는 답한다.

진위경을 시작으로 차례차례 질문이 쏟아졌다.

이소군과의 독살에 연관되어 있느냐는 질문이 절반이었고, 나는 계속해서 부정했다.

‘사실이니까.’

혹시나 해서 몰래 시스템창을 띄워 확인해 봤지만 확실했다. 내가 가진 무공, 능력들은 독과는 아무 관련이 없다. 그런 아이템도 없고.

그래서 망설임 없이 대답할 수 있었다.

“아닙니다.”

문제는 어느 순간부터 회의장 분위기가 묘하게 흘러가고 있다는 사실이었다.

“혹시 입증할 수 있는 증거가 있소?”

“증거요?”

백호당주라고 했나? 이름도 모르는 그는 썩 달갑지 않은 눈초리로 나를 응시했다.

“그렇소. 증거. 삼공자의 무죄를 입증할 만한 증거 말이오.”

이 새끼가 지금 뭐라는 거야.

“그걸 왜 내가 입증해야 하는데요?”

“뭐?”

“뭐는 반말이고.”

“이보시오. 삼공자!”

“날 의심하는 건 좋은데, 증거는 그쪽에서 찾아야 하는 거 아닌가? 예? 안 그래요?”

이 새끼들이 보자 보자 하니까 누굴 보자기로 보나. 나는 씨근덕거리며 자리에 앉는 백호당주를 노려보다가 문득 이상한 점을 발견했다.

‘허. 이것 봐라.’

흘끗 장로원 노인네들에게 시선을 보내는 백호당주의 모습.

공교로운 사실은 나를 추궁하고 압박하는 질문을 하는 이들 모두가 비슷한 모습을 보이고 있다는 것이다.

그 숫자가 참석 인원의 절반 가까이 되니 모른 척하기가 미안할 지경이었다.

‘파벌이라 이거지.’

진위경과 장로원.

한 집안의 웃어른과 그 손자뻘 되는 소가주의 힘 싸움이 이 순간에도 벌어지고 있었다니.

‘집안 꼴 잘 돌아간다.’

이제 남은 이들은 몇 되지 않았다. 문제는 그들의 면면이었다. 검버섯 핀 얼굴. 노회한 눈빛. 바로 장로원의 노인네들이었다.

그중 가장 늙고 뚱뚱한 노인이 입을 열었다.

“실속 없는 문답은 집어치우지. 이 늙은이가 말하고 싶은 건 단 하나일세. 이 문제는 어디서부터 비롯되었는가?”

장로원에 동조하는 중진들이 기다렸다는 듯이 대답했다.

“삼공자입니다.”

“문란한 언행으로 본가의 명성에 먹칠을 하고 다닌 것은 누구인가?”

“그 또한 삼공자입니다.”

같은 대답이 여기저기서 튀어나왔다.

“하면, 항산검문의 장중보옥을 건드려 작금의 사태에 이르게 한 것은 누구인가?”

“…….”

그냥 죽여라, 이 새끼들아.
```

## Current accepted English baseline

```markdown
# Chapter 17

Circulating qi.

It was a method of regulating one’s energy by evening one’s breathing: drawing qi from outside the body, circulating it within, and accumulating it.

Right now, I was circulating qi using the Jin Family’s Cultivation Technique.

*This still feels incredible every time.*

I had never realized there were so many acupoints in my body.

I had once heard that the human body contained more than three hundred and sixty acupoints, but based on what I could feel while circulating qi through the cultivation technique, there were even more than that.

*Is it because I’m a virtual game character?*

*Whatever.*

The ten years of internal energy I drew up from my dantian circulated through my body. If internal energy was a car, then the meridians were a highway. All I had to do was sit behind the wheel and press the accelerator.

The internal energy raced along the straight and curving meridians throughout my body before returning to my dantian.

*And this is where the real problem starts.*

I took a long, deep breath. Then I felt it.

A second internal energy occupied my dantian like an enormous boulder that would not budge, no matter how hard I willed it to.

*What the hell are you?*

It had been a mystery ever since I first circulated qi. An unidentified energy that had taken root like it owned the place.

I didn’t know where it had come from, how it had been formed, or why I couldn’t use it, but one thing was certain. This unidentified energy contained more power than the ten years of internal energy I possessed.

*Until now, I hadn’t even dared touch it.*

To be more precise, I hadn’t intended to. Until a few days ago, I had been waiting for rescue while doing just enough to stay alive.

But things were different now.

*I need more internal energy.*

If I wanted to escape on my own, I had to fulfill the Logout Quest’s condition: reaching the First Rate realm.

I also knew that I needed internal energy on the level of Lee Seogeun’s to become First Rate.

*I’ll make it mine.*

I cautiously began moving my internal energy.

The moment I sent it toward the unidentified energy, half anxious and half expectant, I realized something.

*Not even close.*

Internal energy was, strictly speaking, qi itself—something without a physical form. And yet the instant the two energies touched, I felt powerful rejection and resistance.

No. It was even pulling me in. At this rate, it was going to eat me alive.

*Hey, hey, hey! Wait a second!*

I hurriedly withdrew my internal energy and shook off the unidentified energy, which clung to me until the very end. At the same time, a System notification rang out.

Ding.

> **System**
>
> - You have trained the **Jin Family’s Cultivation Technique**. Internal energy has risen slightly.
>
> - As a result of repeated training, **Sinews** and **Bones** have each increased by 1.

“What the hell was that?”

I calmed my pounding heart and opened my Status Window.

> **Status Window**
>
> **Lv. 17 Jin Taekyung**
>
> **Class:** Second Rate martial artist  
> **Fame:** 73  
> **Titles:** 4 (Title effects active)
>
> - **Scion of a Prestigious Family** — All stats +5, Fame +50
> - **Family’s Shame** — All stats –5, Fame –50
> - **Novice Trainee** — Training speed +10%
> - **Gambler** — Combat-related stats +10% in one-on-one matches
>
> **Strength:** 65  **Stamina:** 65  
> **Agility:** 75  **Intelligence:** 10  
> **Charm:** 10  **Internal Energy:** 10 years
>
> **Remaining Points:** 0

The numbers in my Status Window were fairly impressive by now.

I had gained three levels all at once through the Duel Quest, then distributed the thirty points equally among Strength, Stamina, and Agility.

But looking at the Status Window still left a bitter taste in my mouth.

*My internal energy is the only thing that hasn’t changed.*

This damn System kept saying that my internal energy had risen, but the amount displayed in the Status Window remained exactly the same.

*Do I need to take a spirit pill, an elixir, something like that?*

I thought of Jin Wikyung. If I screwed up my courage and said, *Big brother, just give me one spirit pill,* I didn’t think he would refuse me outright.

I’d ask him the next time I saw him. I would also ask about the unidentified energy inside my dantian.

Krrrummble.

At that moment, the entrance to the training hall opened, and two people stepped inside.

“Um, Young Master Jin?”

It was Han Yeop. Behind him stood a martial artist I had never seen before. The man spoke in a blunt tone that matched his appearance.

“The Lesser Family Head commands you to attend the family council.”

“The Lesser Family Head?”

That worked out perfectly. There was something I wanted to ask him about.

* * *

“It is beyond doubt. A few bones were broken, and there was some minor internal damage, but that level of injury could never—”

“Are you sure? You swear that on the name of the Medicine King Hall Leader?”

“I said it’s true! I examined him myself!”

“Then why are you talking down to me? I treated you with respect because you’re another Hall Leader, and now you think I’m a joke!”

“You were the one who started talking down to me, White Tiger Hall Leader!”

I stared blankly at the ceiling of the meeting room. The shouts and curses flying from every direction made my ears ring.

*What the hell is this?*

This wasn’t what I had imagined a family council would be like. I had pictured a quiet, orderly atmosphere where everyone exchanged opinions and searched for common ground…

“You think every Hall Leader is your equal? You’re nothing but some quack doctor!”

“Listen to this young bastard. I ought to shove a large needle straight into his perineal acupoint!”

Two men in their forties or fifties, both with receding, M-shaped hairlines, were grabbing each other by the collars and shaking one another. Just watching them made my head hurt.

The problem was that scenes like this were unfolding all over the room.

Maybe that was why most of the people there didn’t seem to notice me opening the door and taking my seat.

—You came?

The voice sounded as if it had entered through my head rather than my ears. It was Sound Transmission.

I turned my head and met Jin Wikyung’s gaze from the seat of honor. He gave me a tired smile.

—It’s a madhouse, isn’t it?

*You said it. Why did you call me to this madhouse, you old man?*

When I shot him a reproachful look, Jin Wikyung sent another message through Sound Transmission, his expression turning sheepish.

—I couldn’t help it. The Elder Council demanded your attendance. In any case… you are involved in this matter.

*The Elder Council? I’m involved in this matter?*

*What matter am I involved in…? Oh. The Mount Heng Sword Sect?*

I quickly pieced things together amid the shouting and cursing.

If there was one recent incident connected to me, it was the Mount Heng Sword Sect. And because of that incident, this thing called the Elder Council had summoned me.

That had to be it.

*Come to think of it, there are some old men here I’ve never seen before.*

There were four of them. Every one had a face covered in age spots and hair that had gone completely white.

They watched the men with the M-shaped hairlines grab each other by the collars with cold eyes. Anyone could see it was a nursing home—or rather, the Elder Council.

—And… the Head Elder is here.

I turned toward Jin Wikyung without thinking, then flinched.

*What the hell? Where did that old man come from?*

I had only just noticed that there were two seats of honor today. An old man was sitting to Jin Wikyung’s right, staring at me. His gaze made my face prickle.

*Is that old man the Head Elder?*

White hair, a white beard, and white eyebrows. He looked like an immortal who had stepped out of an old painting. His back was straight, his shoulders broad, and his skin taut enough to make his age seem meaningless.

*But why is he staring at me so intently?*

I gathered strength in my eyes and tried to glare back at the Head Elder…

Then I quietly looked away.

Not because I thought I would lose if we locked eyes. It was respect for my elders. Respect for my elders. Really.

*I’ll just keep my head down.*

Jin Wikyung’s Sound Transmission continued in the meantime.

—You may not know this because you lost your memory, but the Head Elder is your great-uncle and the most senior elder in the family. Be especially careful with your words and actions.

I hadn’t even seen my father’s face, and now I had a great-uncle.

*Maybe this place has relatives by marriage, distant cousins, and every kind of obscure uncle, too.*

I gave Jin Wikyung a small nod.

—And… you must not be flustered by what happens from this point onward. Calmly tell them only the truth. Do you understand?

I didn’t know exactly what was going on, but one thing was certain: Jin Wikyung was on my side.

I nodded again, and Jin Wikyung rose with a faint smile.

“Silence, everyone.”

His voice, infused with internal energy, swept across the meeting hall.

“This is a family council of the Jin Family of Taiyuan, and we have gathered to discuss a grave matter. Since our witness has arrived, I intend to begin the interrogation.”

The meeting hall had gone quiet without me noticing. With everyone’s attention focused on him, Jin Wikyung spoke.

“By the authority of the Lesser Family Head and current acting Family Head, I begin this interrogation. Third Young Master Jin Taekyung, step forward.”

I felt everyone’s eyes on me as I walked forward. I had expected this much. They hadn’t summoned me for no reason.

But…

“I ask you this. Did you poison Lee Seogeun of the Mount Heng Sword Sect?”

That was something I hadn’t expected.

* * *

“No.”

I barely managed to force the word out. My thoughts were a mess from the sudden question.

*Lee Seogeun was dead? Poisoned, at that?*

“Tell us the truth. If it turns out to be a lie…”

“I have nothing to do with Lee Seogeun’s poisoning.”

My answer was as sharp as a blade. Jin Wikyung let out a sigh of relief.

—Keep doing exactly this.

The interrogation proceeded quickly. They asked questions, and I answered them.

Starting with Jin Wikyung, they fired one question after another at me.

About half of the questions concerned whether I had been involved in poisoning Lee Seogeun, and I continued to deny it.

*Because it was true.*

Just in case, I secretly opened my System Window to check. I was certain of it. None of my martial arts or abilities had anything to do with poison. I didn’t have any such Items, either.

That was why I could answer without hesitation.

“No.”

The problem was that, at some point, the atmosphere in the meeting hall began to grow strange.

“Do you have any evidence to prove it?”

“Evidence?”

White Tiger Hall Leader, was it? The man whose name I didn’t even know stared at me with obvious displeasure.

“That is correct. Evidence. I mean evidence that would prove the Third Young Master’s innocence.”

*What the hell is this bastard talking about?*

“Why do I have to prove it?”

“What?”

“Don’t talk down to me.”

“Listen here, Third Young Master!”

“You’re free to suspect me, but shouldn’t you be the ones looking for evidence? Am I wrong?”

I’d been letting it slide, and these bastards thought they could wrap me up like a cloth?[^1]

Fuming, I glared at the White Tiger Hall Leader as he sat down, then noticed something strange.

*Well, well. Look at this.*

The White Tiger Hall Leader kept stealing glances at the old men of the Elder Council.

The strange thing was that everyone who had been pressing and interrogating me was doing something similar.

Nearly half the people in attendance were acting this way. It was getting difficult to pretend I hadn’t noticed.

*So this is a factional struggle.*

The Elder Council and Jin Wikyung.

Even now, a power struggle was taking place between the senior members of the family and the Lesser Family Head who was young enough to be their grandson.

*What a family.*

Only a few people remained to question me. The problem was who those people were.

Faces covered in age spots. Canny, experienced eyes.

The old men of the Elder Council.

The oldest and fattest of them opened his mouth.

“Enough of this empty questioning. There is only one thing this old man wishes to ask. Where did this matter begin?”

The senior members allied with the Elder Council answered as if they had been waiting for the question.

“The Third Young Master.”

“Who was it that dragged our family’s reputation through the mud with disorderly words and conduct?”

“The Third Young Master.”

The same answer came from several places around the room.

“Then who was it that provoked the Mount Heng Sword Sect’s prized treasure and brought us to this crisis?”

“…”

*Just kill me already, you bastards.*

[^1]: In Korean, the line puns on *boja* (“let’s see / wait and see”) and *bojagi*, a wrapping cloth.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 17`.

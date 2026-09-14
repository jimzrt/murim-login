# Master Edit Task — Chapter 18

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

| 진위경    | **Jin Wikyung**    |
| 위팽     | **Wipeng**         |
| 이소군    | **Lee Seogeun**    |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 기루     | **pleasure house**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |

## Matched risk notes

(No matching risk notes.)

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

#### Chapter 16 tail (verified mastered)

…
been plain to see during the duel. And second. *I don’t have enough internal energy.* In terms of internal energy alone, Lee Seogeun had been ahead of me. No, he had been overwhelmingly ahead. What the hell had he eaten growing up? I had smashed him dozens of times with the shaft of my spear and pounded him one-sidedly from the mount, yet he had endured it all. He had even counterattacked and drawn on more internal energy at the very end. *I currently have ten years of internal energy.* Lee Seogeun probably had twenty years—twice as much as I did. That led me to a third realization. *The difference in internal energy determines the stage of one’s martial arts.* I had defeated Lee Seogeun, a First Rate martial artist. Yet the realm displayed by the System still listed me as Second Rate. I thought the reason lay in internal energy. Once I raised the one ability I lacked, wouldn’t my realm finally rise as well? After organizing my thoughts that far, another idea suddenly occurred to me. *This is basically just Hunter rank classification.* Every newly awakened Hunter had to visit a designated center to have their abilities, suitable profession, and mana capacity assessed. No matter how high their physical abilities were, anyone with insufficient mana received a frosty reception during their rank evaluation. That was also why mages started at D-rank at the lowest. Because of their profession, mages had plenty of basic mana from the start. *Still, the game is better than reality.* At least you could grow here. Reality had no such thing. Even I had only managed to get lumped in with the E-ranks after working my ass off for seven years. I was still an F-rank Hunter. Anyway, I had now drawn a rough outline. *My stats are high enough. I’ll cycle the Jin Family’s Cultivation Technique whenever I have time and prioritize Quests that reward EXP.* It had been over a week since I was trapped in this godforsaken game. I didn’t know what kind of nonsense was happening in the real world, but I could forget about being rescued. I needed to prepare properly and finish this. “Open Quest window.” Ding. > **System** > > **Quest** > > **Logout** > > You must now make your way through this harsh Murim. > > Become stronger and more famous. > > For the day that will someday come… > > **Grade:** Main Quest > **Restriction:** Jin Taekyung > **Mission:** Achieve the **First Rate** realm (Incomplete) > > &nbsp;&nbsp;&nbsp;&nbsp;Reach Level 30 (17 / 30) > > &nbsp;&nbsp;&nbsp;&nbsp;Reach Fame 500 (70 / 500) > > **Reward:** **Logout** “Ugh. This is brutal.” I sat cross-legged. Two days remained before my seclusion ended. I intended to gather as much internal energy as possible. > **System** > > Fame has risen by 3 due to the influence of the **Sleeping Dragon of Shanxi** rumor. The Fame-increase messages that chimed from time to time offered a small measure of comfort. * * * Late that night, the lights came on in the main assembly hall. At the Lesser Family Head’s request, a secret meeting of the family council had been convened. The hour was late and the summons abrupt, leaving several senior members with sour expressions. “A sudden summons? What is this about?” “Exactly. Calling us here at this hour without even telling us why…” “That’s what happens when the Lesser Family Head is still young. He doesn’t know procedure or etiquette.” “He must have grown rather full of himself after yesterday’s events. Though I suppose his only weakness has disappeared. No one expected the Third Young Master to be that capable.” “That must have taken the wind out of the Elder Council’s sails. They were probably preparing to make a major move over the Third Young Master.” “Hmph. Even now, the Head Elder ought to step forward and set the family straight.” “Careful. Watch your tongue…” At that moment, every sound abruptly stopped. The doors to the meeting room opened from both sides, and Jin Wikyung entered. Opinions of the Lesser Family Head varied among the senior members, but the silence that settled over the room the instant he appeared proved that he possessed the qualities of a leader. “Thank you all for answering my summons at this late hour.” Jin Wikyung took the seat of honor and spoke his opening words, but he found it difficult to continue. *What should he say? Where—and how—should he begin?* His head throbbed. But this was something he had to tell them. “The reason I called everyone here today is…” That was when a strange voice interrupted him. “It must be because of the Mount Heng Sword Sect.” The voice was bizarre. At first, it sounded like an old man’s. And yet it was young as well—rough one moment, smooth the next. There was also an inexplicable resonance to it. *Could it be…?* Jin Wikyung’s face twisted. The doors to the meeting hall, which had seemed as though they would never open again, began to part. Step. Step. Step. Five old men walked in as if they were gliding across the floor. The instant everyone recognized the old man at the front, they hurriedly stood and bowed their heads. “We pay our respects, Head Elder!” The Head Elder. He had appeared after keeping himself shut away from the world for years.

#### Chapter 17 tail (verified mastered)

…
eyebrows. He looked like an immortal who had stepped out of an old painting. His straight back, broad shoulders, and taut skin seemed to defy his age. *But why is he staring at me so intently?* I put some force into my gaze and tried to glare back at the Head Elder… Then I quietly looked away. Not because I thought I would lose if we fought. It was respect for my elders. Respect for my elders. Really. *I’ll just keep my head down.* Jin Wikyung’s Sound Transmission continued in the meantime. —You may not know this because you lost your memory, but the Head Elder is your great-uncle and the most senior elder in the family. Be especially careful with your words and actions. I hadn’t even seen my father’s face, and now I had a great-uncle. *Maybe there were in-laws, eighth-degree relatives, and even one of my father’s cousins somewhere in this room.* I gave Jin Wikyung a small nod. —And… you must not be flustered by what happens from this point onward. Calmly tell them only the truth. Do you understand? I didn’t know exactly what was going on, but one thing was certain: Jin Wikyung was on my side. I nodded again, and Jin Wikyung rose with a faint smile. “Silence, everyone.” His voice, infused with internal energy, swept across the meeting hall. “This is a family council of the Jin Family of Taiyuan, and we have gathered to discuss a grave matter. Since the witness has arrived, I intend to begin the interrogation.” The meeting hall had fallen silent before I knew it. With everyone’s attention fixed on him, Jin Wikyung spoke. “By the authority of the Lesser Family Head and current acting Family Head, I begin this interrogation. Third Young Master Jin Taekyung, step forward.” I felt everyone’s eyes on me as I walked forward. I had expected this much. They hadn’t summoned me for no reason. But… “I ask you this. Did you poison Lee Seogeun of the Mount Heng Sword Sect?” That was something I hadn’t expected. * * * “No.” I barely managed to get the word out. My thoughts were a mess from the sudden question. *Lee Seogeun was dead? Poisoned, at that?* “Tell us the truth. If your words are proven false…” “I had nothing to do with poisoning Lee Seogeun.” My answer was as sharp as a blade. Jin Wikyung let out a sigh tinged with relief. —Keep doing exactly this. The interrogation proceeded quickly. They asked questions, and I answered. Starting with Jin Wikyung, they fired one question after another at me. About half of the questions concerned whether I had been involved in poisoning Lee Seogeun, and I continued to deny it. *Because it was true.* Just in case, I secretly opened my System Window and checked. I was certain. None of my martial arts or abilities had anything to do with poison. I didn’t have any such Items, either. That was why I could answer without hesitation. “No.” The problem was that, at some point, the atmosphere in the meeting hall began to take a strange turn. “Do you have any evidence to prove it?” “Evidence?” White Tiger Hall Leader, was it? The man whose name I didn’t even know stared at me with obvious displeasure. “That is correct. Evidence. I mean evidence that would prove the Third Young Master’s innocence.” *What the hell is this bastard talking about?* “Why do I have to prove it?” “What?” “Don’t ‘what’ me.” “Listen here, Third Young Master!” “You’re free to suspect me, but shouldn’t you be the ones looking for evidence? Am I wrong?” I’d let this go on long enough. Did these bastards think I was some damn wrapping cloth?[^1] Fuming, I glared at the White Tiger Hall Leader as he sat down, then noticed something strange. *Well, well. Look at this.* The White Tiger Hall Leader kept stealing glances at the old men of the Elder Council. The strange thing was that everyone who had been pressing and interrogating me was doing something similar. Nearly half the people in attendance were acting this way. It was getting difficult to pretend I hadn’t noticed. *So this is a factional struggle.* Jin Wikyung and the Elder Council. Even now, a power struggle was taking place between the senior members of the family and the Lesser Family Head who was young enough to be their grandson. *What a family.* Only a few people remained to question me. The problem was who those people were. Faces covered in age spots. Canny, experienced eyes. The old men of the Elder Council. The oldest and fattest of them opened his mouth. “Enough of this empty questioning. There is only one thing this old man wishes to ask. Where did this matter begin?” The senior members allied with the Elder Council answered as if they had been waiting for the question. “The Third Young Master.” “Who was it that dragged our family’s reputation through the mud with disorderly words and conduct?” “The Third Young Master.” The same answer came from several places around the room. “Then who was it that laid hands on the Mount Heng Sword Sect’s treasured jewel and brought about the present crisis?” “…” *Just kill me already, you bastards.* [^1]: In Korean, the line puns on *boja* (“let’s see / wait and see”) and *bojagi*, a wrapping cloth.

## Korean source

```text
＃18화



분위기는 점점 최악으로 치닫기 시작했다.

“중요한 사실은 비무가 정당했다는 것입니다!”

“정당? 요즘은 독을 쓰는 걸 정당하다고 하나? 여기가 무슨 사천당문이야?”

“본인이 아니라고 하지 않소! 그리고 앞서 약왕당주가 말했듯이 이소군은 멀쩡했…….”

“삼공자야 당연히 아니라고 하겠지. 그리고 저 돌팔이 말을 어떻게 믿어?”

“돌팔이? 이 새끼가 진짜!”

그때 잔뜩 흥분한 목소리 하나가 귓가를 파고들었다.

“필요하다면 삼공자의 목을 바쳐서라도 전쟁을 막아야지!”

……뭐?

“그 무슨 망발이오!”

“내 말이 틀렸소? 이제 그만 인정합시다. 항산검문은 본가보다 강하오. 전쟁이 시작되면 수백이 죽거나 다칠 테고, 최악의 경우에는 멸문이오. 모든 원인인 삼공자를 넘기면 끝나는 일 아닌가!”

저게 말이냐, 방구냐. 모처럼 대단한 개소리를 들었더니 뒷골이 당기고 가슴이 답답해져 온다. 하지만 나보다 먼저 나선 사람이 있었다.

“방금 뭐라 했소?”

나직한 목소리지만 힘이 실려 있었다. 오히려 나직하기에 더 선명하게 들린다.

진위경이다. 그가 무표정한 얼굴로 사람들을 둘러봤다.

“누구. 목을. 바치자고?”

한 음절씩 뚝뚝 끊어지는 음성에 서리가 꼈다. 나도 순간적으로 몸이 으슬으슬할 정도의 분위기인데, 백호당주가 냉큼 입을 열었다.

“그거야 당연히 이 일의 주범인 삼공자…… 아.”

저 새끼는 모발도 없는데 눈치까지 없네. 백호당주는 말꼬리를 흐렸지만 이미 늦었다.

“그래서, 확인되지도 않은 일로 삼공자의 목을 항산검문에 갖다 바치시겠다? 그게 가문 당주의 입에서 나올 말이오?”

“아니, 내 말은 그런 뜻이 아니라…….”

백호당주가 진위경의 기세에 눌려 그의 눈을 피한다. 진위경이 가만히 백호당주를 노려보았다. 안 그러던 사람이 화가 나니 더 무섭다.

하얗게 질린 백호당주의 얼굴을 보니 10년 묵은 체증이 내려가는 기분이다. 자리에서 일어난 진위경은 냉엄한 얼굴로 좌중을 내려다봤다.

“이미 다들 알고 있소.”

진위경이 모두를 둘러보며 단호히 말했다.

“비무는 공정했고 이소군의 독살은 음모라는 것을. 그 사실을 알면서도 두려움 때문에 저들에게 굴복하자는 거요?”

장로원 측 인사들이 시선을 회피했다. 진위경의 냉소가 더욱 짙어졌다.

“누가 쥐여 줬는지는 모르겠지만, 항산검문은 명분이라는 칼자루를 쥐고 있소. 오늘일지, 내일일지. 아니면 이미 뽑혔는지도 모르지만 우리가 되돌리기에는 늦었소. 방법은 단 하나. 맞서 싸우는 것뿐이오.”

“…….”

“살고 싶소? 가문을 지키고 싶소? 진정 그렇다면 무사들을 준비시키고 전쟁을 준비하시오. 아니면 나와 내 아우의 목을 베어 저들에게 바치시든가. 그저 부귀영화만을 바란다면 그것도 나쁘지 않은 방법이겠지.”

숨 막히는 정적이 대회의장을 점령했다.

다음 순간, 한 사람이 입을 열지 않았다면 몇 시간이고 그 정적에 짓눌려 있었을지도 몰랐다.

“훌륭하다.”

지금까지 말없이 사태를 관망하던 한 사람.

대장로였다.



* * *



대장로.

요주의 인물이다. 가문의 최고 웃어른이자 장로원의 수장.

나는 앞서 들었던 진위경의 전음을 떠올렸다.

‘조심하라고 했었지.’

진위경이라는 NPC는 내게 있어 가장 큰 아군이자 조언자다.

나는 그 말을 허투루 듣지 않았고, 틈틈이 대장로를 주시했다.

그리고 한 가지 결론을 내렸다.

‘시바, 도저히 모르겠다.’

이 거지 같은 게임을 시작한 뒤 한 번이라도 마주친 NPC들의 숫자를 세라고 하면 족히 백은 넘어간다.

그들에겐 각자의 표정과 성격이 있었다. 기루에서 만난 하인은 삶에 찌든 영업용 미소를 지었고, 나를 데려다준 마부는 허당끼가 있었으며 가문에서 만난 중진들은 의외로 단순하고 과격한 면모가 있다.

하지만 대장로는…….

‘표정을 못 읽겠어.’

그는 그저 묘한 웃음을 지으며 이 모든 것을 지켜볼 뿐이다.

심문이 시작되었을 때도, 중진들이 각자의 파벌에서 고함을 내지를 때도, 그리고 지금 이 순간에도.

짝. 짝. 짝.

대장로의 힘찬 박수 소리가 울려 퍼졌다.

“어리게만 생각했건만, 어느새 소가주가 이리 당당한 무인이 되었구려. 훌륭하오. 그래야 본가의 소가주라 할 수 있지.”

“못난 꼴을 보여 드려 죄송할 따름입니다.”

“과한 겸손은 오만으로 비치는 법. 소가주는 사과할 것 없소.”

대장로의 칭찬에도 진위경은 여전히 굳은 얼굴이었다.

“이 늙은이도 한마디 보탤까 하는데, 소가주의 생각은 어떠신가?”

“새겨듣겠습니다.”

천천히 자리에서 일어난 대장로에게 수십 쌍의 시선이 꽂혔다.

가문의 최고 웃어른이다. 가문 내 권위나 입지로 치자면 진위경을 뛰어넘을지도 모른다.

가장 큰 문제는 그가 반대 세력인 장로원의 수장이라는 거고.

‘시발, 좆 됐네.’

최악의 상황을 대비해 슬금슬금 문 쪽으로 몸을 돌리는 내 귓가에, 대장로의 첫 마디가 파고들었다.

“썩어 빠졌구나.”

응?

고개를 홱 돌렸다. 대장로는 여전히 특유의 묘한 웃음을 짓고 있었다. 내가 잘못 들었나?

하지만 아니었다.

“하물며 짐승들조차도, 제 굴에 적이 들어오면 함께 힘을 합쳐 싸우는 법이다. 그런데 가문의 중진씩이나 되는 것들이 직계의 목을 바치고 전쟁을 막겠다는 걸 대책이라고 내어놓고 있구나. 허허. 이런 놈들이 본가의 가로회의에 앉아 있단 말이지.”

“노, 노야. 오해십니다. 그것은 그저…….”

“백호당주.”

서늘한 대장로의 부름에 백호당주가 바짝 긴장했다.

“내 외유가 너무 길었던 것인가? 아니면 가주가 자리를 비웠기 때문인가?”

“노, 노야.”

표정만 보면 밥 먹었냐 물어보는 헬스장 몸짱 할아버진데, 말하는 내용은 살벌하기 그지없다.

‘뭐야, 이거.’

어떻게 돌아가는 거야? 왜 우리 편을 들어?

눈동자를 팽팽 돌려 봤지만, 사람들의 반응도 나와 다르지 않았다. 양측 모두 당황한 기색이 역력했다.

“어찌 생각하시오, 소가주?”

“무엇을 말씀하시는 것인지.”

“전쟁이 기정사실화되었다면 내부를 단속하는 것이 우선이겠지. 그러니 역도나 다름없는 저들의 목을 베는 게 우선일 텐데?”

얼어붙은 공기 속, 진위경은 한동안 물끄러미 대장로를 바라보다가 한숨처럼 대답을 토해 냈다.

“그럴 수는 없습니다.”

휴우. 백호당주가 안도의 한숨을 내쉬었다. 아까 내 목을 갖다 바치느니 마니 했던 걸 생각하면 살짝 아쉽다.

……저 자식만 죽이자고 말해 볼까.

“저들은 가문의 직계를 모함하는 것으로도 모자라 적들에게 넘기자고 주장했는데, 너무 무른 처사라고 생각하지 않나?”

“오랜 세월 본가에 충성한 이들입니다. 흥분해서 나온 실언이라고 생각하겠습니다.”

진위경의 대답에 대장로가 껄껄 웃었다.

“실언, 실언이라. 그래. 소가주의 그릇은 내 생각 이상으로 크구려. 과연 소가주요. 그렇다면 이들에 대한 책임은 묻지 않기로 하지. 늙은이들의 실언을 담대하게 용서해 준 소가주께 감사를 표하는 바요.”

이어 대장로가 고개를 숙이자 사람들이 다급하게 손사래를 치며 마주 허리를 굽혔다.

“아이고, 노야. 아닙니다. 저희의 생각이 짧았습니다.”

“제발 이러지 마십시오.”

“이러시면 저희가 더욱 부끄러워집니다. 부디…….”

“노야……!”

살려 준 건 진위경인데 난리가 났다. 아주 생쇼를 해라, 생쇼를.

내심 혀를 차며 그 모습을 지켜보던 순간이었다.

‘아니, 잠깐만. 쇼?’

정체 모를 위화감이 온몸을 감싼다. 나는 황급히 대장로 주위에 모여든 이들을 살폈다. 그리고 발견했다.

앞서 나를 몰아세웠던 장로원. 그들의 입가에 스치는 웃음을.

‘설마…….’

계획된 거라고? 이 모든 게 다?

도대체 무슨 의도로, 뭘 위해서? 수많은 물음이 떠올랐다 사라진다. 머릿속이 엉망진창이었다.

‘진위경은 뭔가 알고 있을까?’

고개를 돌려 찾을 필요도 없었다. 대장로가 진위경의 손을 번쩍 들고 외치고 있었으니까.

“가주가 자리를 비운 지금, 소가주가 가주나 다름없소. 이 일에 대해서 나는 소가주를 지지하겠소. 그를 중심으로 뭉친다면 저들이 아무리 대단하다 해도 감히 진가를 넘볼 수 없을 것이오!”

달아오른 분위기, 사람들의 연호와 함성.

이걸 어디서 봤더라, 왠지 모르게 익숙한 느낌이다.

그리고.

“감사합니다.”

파르르 떨리는 진위경의 입꼬리와 대장로의 묘한 웃음을 보는 순간, 나는 익숙한 느낌의 정체를 깨달았다.

‘선거 유세.’

대장로의 모습과 TV 속 정치인이 겹쳐 보였다.



* * *



상당히 찜찜하긴 했지만, 일단 대장로가 진위경의 손을 들어 주자 회의는 일사천리로 진행되었다.

장로원 측에서 끈질기게 물고 늘어졌던 비무 관련 이야기는 쏙 들어가고, 전쟁을 전제로 한 회의 내용이 주를 이뤘다.

“현재 가용 인원은 어떻게 되나?”

“외부 파견 중인 무사들까지 불러들인다면…… 이백 남짓입니다.”

이백 명이나 된다고? 나는 의외로 많은 숫자에 혀를 내둘렀지만 이어지는 대화에 입을 다물었다.

“일류 이상의 정예로 엄선한다면?”

“스물이 채 안 됩니다. 물론 이 자리에 계신 분들을 포함하면 다르겠지만 말입니다.”

중진들을 포함하면 일류 고수의 숫자는 3, 40명 남짓.

이곳 사정은 잘 모르지만, 이 정도면 양호한 수준인 것 같다.

역시 뿌리 깊은 명문세가. 200년을 이어 온 저력이 어디 가는 게 아니다.

“항산검문 측은?”

“우선 확인된 무사들만 최소 삼백입니다.”

삼백. 그것도 최소로 잡았으니 백 명 이상의 차이다.

하지만 괜찮다. 원래 싸움은 머릿수로 하는 게…….

“그리고 일류는 오십 이상입니다.”

이 전쟁, 어렵다. 그래도 진위경과 위팽 같은 고수들이 있다면 해 볼 만한 싸움이다. 그들은 기감으로도 읽지 못하는 고레벨의 NPC들이니까. 아마 대장로도 그 범주에 포함되는 존재일 것이다.

“본가의 절정 고수는 소가주와 노야, 위 대협까지 총 셋입니다. 그리고 항산검문의 절정 고수는 다섯이지요.”

……거지 같아서 못 해 먹겠네. 진짜.

‘뭐? 뿌리 깊은 명문세가? 200년 역사?’

이 새끼들은 200년 동안 뭘 한 거야. 듣자 하니 항산검문의 역사가 30년도 안 된다는데, 전력 면에서 밀리다 못해 압살이다. 압살.

‘작년에 흑사병이라도 돌았나.’

흑사병이 돌았건 말건 당장 내가 돌아 버릴 것 같다. 나는 어느새 노래진 회의실 천장을 바라보다 문득 다짐했다.

‘튀어야겠다.’

새벽 네 시 정도면 적당하겠지. 다들 잠들어 있을 때 몰래 담을 넘어서 멀리 도망가는 거다.

지금의 나라면 천력부 정도의 수준은 대여섯이 덤벼도 손쉽게 해치울 수 있다.

보이는 산마다 싹 뒤지면서 경험치와 명성을…….

“항산, 항산검문에서 전서구가 도착했습니다!”

황급히 들이닥친 무사의 외침이었다. 누군가 돌돌 말린 종이를 받아 펼치자 피로 쓴 듯 붉은 글자가 눈에 들어왔다.

굳이 시스템이 번역해 주지 않아도 알아볼 수 있는 글자였다.



不俱戴天



‘불구대천.’

하늘 아래 같이 살 수 없는 원수.

진위경이 무거운 얼굴로 입을 열었다.

“현 시간부로 본가는 전시 상황에 돌입한다. 내 인(印) 없이는 지위 고하를 막론하고 세가 외 출입을 금하며, 삼엄한 경계 태세를 유지해야 할 것이다. 개미 새끼 한 마리도 들이지 말라. 알겠는가!”

“옛!”

“…….”

넋이 반쯤 나간 내 귓가로, 시스템 알림이 울렸다.

띠링.



- [항산검문]이 [태원진가]에 선전포고했습니다.

- [전쟁] 관계가 양측 진영에 성립되었습니다.

- [항산검문]이 당신을 문파 공적으로 지목합니다.

- 도망칠 경우 심각한 불이익을 받게 될 것입니다.

- [메인 퀘스트 - 전쟁]이 생성되었습니다.



……허허. 허허허허.
```

## Current accepted English baseline

```markdown
# Chapter 18

The atmosphere grew worse by the second.

“The important fact is that the duel was fair!”

“Fair? Since when is using poison considered fair? Is this the Sichuan Tang Clan or something?”

“The man himself said he didn’t do it! And as the Medicine King Hall Leader said earlier, Lee Seogeun was perfectly fine—”

“Of course the Third Young Master would say he didn’t. And how can you believe that quack?”

“A quack? You little bastard!”

Then one particularly agitated voice pierced my ears.

“If necessary, we should stop the war even if it means offering up the Third Young Master’s head!”

…What?

“What kind of outrageous nonsense is that?”

“Am I wrong? Let’s just admit it. The Mount Heng Sword Sect is stronger than our family. If war begins, hundreds will die or be injured, and in the worst case, our family could be destroyed. If we hand over the Third Young Master, who caused all this, won’t everything be over?”

What kind of bullshit was that? I hadn’t heard such spectacular nonsense in a long time. The back of my neck tightened, and my chest grew tight.

But someone else stepped forward before I could.

“What did you just say?”

His voice was quiet, but it carried power. In fact, its quietness made it sound even clearer.

It was Jin Wikyung. He looked around the room with an expressionless face.

“Whose. Head. Did you say we’d offer?”

Each syllable fell separately, frost coating his voice. The atmosphere was so chilling that even I shivered.

The White Tiger Hall Leader spoke up at once.

“Obviously, the Third Young Master, the main culprit behind this—ah.”

That bastard was bald, and he couldn’t read the room either. The White Tiger Hall Leader let his words trail off, but it was already too late.

“So you intend to hand the Third Young Master’s head over to the Mount Heng Sword Sect over something that has not even been confirmed? Is that something a hall leader of this family should be saying?”

“No, that’s not what I meant…”

The White Tiger Hall Leader was overwhelmed by Jin Wikyung’s aura and avoided his eyes. Jin Wikyung silently glared at him.

He wasn’t normally like this, which made him even scarier now that he was angry.

Looking at the White Tiger Hall Leader’s pale face made me feel as if ten years of indigestion had finally been cured. Jin Wikyung rose from his seat and looked down at everyone with a cold expression.

“You all already know.”

He looked around the room and spoke firmly.

“That the duel was fair, and Lee Seogeun’s poisoning was a conspiracy. Knowing that, are you suggesting we submit to them out of fear?”

The members of the Elder Council faction avoided his gaze. Jin Wikyung’s sneer grew deeper.

“I don’t know who placed it in their hands, but the Mount Heng Sword Sect holds the hilt of a sword called justification. Whether it happens today or tomorrow—or whether the sword has already been drawn—we are already too late to reverse it. There is only one way forward. We fight.”

“……”

“Do you want to live? Do you want to protect the family? If you truly do, prepare the martial artists and prepare for war. Or cut off my head and my younger brother’s, then offer them to the Mount Heng Sword Sect. If all you want is wealth and glory, I suppose that isn’t a bad option, either.”

A suffocating silence took over the main assembly hall.

If one person hadn’t opened his mouth the next moment, we might have been crushed beneath that silence for hours.

“Excellent.”

It was the man who had watched the situation without saying a word until now.

The Head Elder.

* * *

The Head Elder.

A person to watch out for. The family’s highest-ranking elder and the head of the Elder Council.

I remembered the Sound Transmission Jin Wikyung had sent me earlier.

*He told me to be careful.*

Jin Wikyung was the greatest ally and adviser I had among the NPCs.

I hadn’t taken his warning lightly. Whenever I had the chance, I kept an eye on the Head Elder.

And I reached one conclusion.

*Fuck, I can’t figure him out at all.*

If someone asked me to count the number of NPCs I had encountered even once since starting this godforsaken game, the number would easily be over a hundred.

Each of them had their own expressions and personalities. The servant I met at the pleasure house wore a business smile worn down by life. The coachman who brought me here had a goofy side. The senior members I met in the family were surprisingly simple-minded and aggressive.

But the Head Elder…

*I can’t read his expression.*

He merely watched everything with that strange smile of his.

When the interrogation began. When the senior members of each faction shouted at one another. And even now.

Clap. Clap. Clap.

The Head Elder’s vigorous applause rang through the hall.

“I thought of you as nothing more than a youngster, but before I knew it, the Lesser Family Head had become such a dignified martial artist. Excellent. That is how the Lesser Family Head of our family should be.”

“I can only apologize for showing you such an unseemly side.”

“Excessive humility can look like arrogance. You have nothing to apologize for.”

Despite the Head Elder’s praise, Jin Wikyung’s face remained stiff.

“May this old man add a word? What do you think, Lesser Family Head?”

“I will take it to heart.”

The Head Elder slowly rose from his seat, and dozens of pairs of eyes locked onto him.

He was the family’s highest-ranking elder. In terms of authority and standing within the family, he might even surpass Jin Wikyung.

The biggest problem was that he was the head of the opposing faction—the Elder Council.

*Fuck, I’m screwed.*

Preparing for the worst, I started edging toward the door when the Head Elder’s first words reached my ears.

“You’re rotten to the core.”

Huh?

I whipped my head around. The Head Elder still wore that same strange smile.

*Did I hear him wrong?*

But I hadn’t.

“Even beasts join forces and fight when an enemy enters their den. And yet men who are supposedly senior members of this family offer up the head of a direct-line member as a solution to stop a war. Heh. So men like this sit in our family council.”

“N-no, Head Elder. You’ve misunderstood. It was merely…”

“White Tiger Hall Leader.”

At the Head Elder’s chilly call, the White Tiger Hall Leader stiffened.

“Have I been away for too long? Or is it because the Family Head is absent?”

“N-no, Head Elder.”

Going by the Head Elder’s expression, he looked like a muscular old man at a gym asking whether you’d eaten. But the content of his words was vicious beyond belief.

*What is this?*

What was going on? Why was he taking our side?

I looked around frantically, but everyone else was just as confused as I was. Both factions were visibly flustered.

“What do you think, Lesser Family Head?”

“I’m not sure what you mean.”

“If war has become inevitable, then our first priority should be to discipline those within our ranks. Wouldn’t it be best to cut off the heads of those men who are little different from rebels?”

In the frozen air, Jin Wikyung stared at the Head Elder for a long moment before answering in something like a sigh.

“That cannot be done.”

Whew. The White Tiger Hall Leader let out a relieved sigh.

Considering how he had just been talking about offering up my head, I was a little disappointed.

*Should I suggest that we kill just him?*

“Those men not only framed a direct-line member of the family, but even argued we should hand him over to the enemy. Don’t you think that is too lenient a response?”

“They have served our family loyally for many years. I will consider it an ill-considered remark made in the heat of the moment.”

The Head Elder laughed heartily.

“An ill-considered remark. An ill-considered remark, indeed. Yes. The Lesser Family Head’s capacity is greater than I expected. Truly worthy of being the Lesser Family Head. In that case, I will not hold them responsible. I offer my thanks to the Lesser Family Head for magnanimously forgiving the thoughtless words of old men.”

When the Head Elder bowed, the others hurriedly waved their hands and bent at the waist in return.

“Oh, Head Elder, no. Our thoughts were shallow.”

“Please, don’t do this.”

“You’re only making us more ashamed. Please…”

“Head Elder!”

Jin Wikyung was the one who had spared them, yet they were making a huge scene.

Go on, put on a show. A real show.

I was watching the spectacle with a private click of my tongue when—

*Wait. A show?*

An indescribable sense of wrongness settled over me. I hurriedly examined the people gathered around the Head Elder.

And then I noticed it.

The smiles flickering around the lips of the Elder Council members who had pressured me earlier.

*No way…*

Was this all planned? Every bit of it?

Why? For what purpose? Countless questions rose and vanished. My thoughts were a complete mess.

*Does Jin Wikyung know something?*

I didn’t even need to turn around to look for him. The Head Elder was already holding Jin Wikyung’s hand high in the air and shouting.

“With the Family Head absent, the Lesser Family Head is effectively the Family Head. I support the Lesser Family Head in this matter. If we unite around him, then no matter how formidable they are, they will not dare challenge the Jin Family!”

The heated atmosphere. The people’s cheers and shouts.

*Where had I seen this before?*

It felt strangely familiar.

And then—

“Thank you.”

The moment I saw the corners of Jin Wikyung’s mouth quiver and the Head Elder’s strange smile, I realized where that familiar feeling came from.

*An election campaign.*

The Head Elder’s figure overlapped with the politicians I had seen on television.

* * *

It was deeply unsettling, but once the Head Elder raised Jin Wikyung’s hand, the meeting proceeded swiftly.

The discussion about the duel, which the Elder Council faction had stubbornly kept dragging out, disappeared entirely. Instead, the meeting focused on preparing for war.

“How many men are currently available?”

“If we call back the martial artists stationed outside, roughly two hundred.”

As many as two hundred?

I was astonished by the unexpectedly large number, but the next question made me shut my mouth.

“If we select only elites of First Rate or higher?”

“Fewer than twenty. Of course, that number would be different if we included everyone present.”

Including the senior members, there were around thirty or forty First Rate masters.

I didn’t know much about the circumstances here, but that seemed like a decent number.

As expected of a prestigious family with deep roots. Two hundred years of accumulated strength didn’t simply vanish.

“What about the Mount Heng Sword Sect?”

“At least three hundred martial artists have been confirmed so far.”

Three hundred. And that was the minimum, meaning there was a difference of more than a hundred men.

But it was fine. Fights came down to numbers anyway—

“And they have more than fifty First Rate martial artists.”

This war was going to be difficult.

Still, with masters like Jin Wikyung and Wipeng, it was a fight worth attempting. They were high-level NPCs beyond what my Qi Sense could read. The Head Elder probably belonged to that category, too.

“Our family has three Peak masters in total: the Lesser Family Head, the Head Elder, and Sir Wipeng. The Mount Heng Sword Sect has five.”

…This was so damn hopeless I couldn’t even deal with it.

*What? A prestigious family with deep roots? Two hundred years of history?*

What the hell had these bastards been doing for two hundred years? I heard the Mount Heng Sword Sect had existed for less than thirty, but in terms of military strength, we weren’t merely outmatched.

We were being steamrolled. Steamrolled.

*Did the Black Death sweep through last year or something?*

Whether there had been a plague or not, I felt like I was going insane. I was staring at the meeting-hall ceiling, which had yellowed before I knew it, when I suddenly made a decision.

*I need to run.*

Around four in the morning should do. Once everyone was asleep, I’d sneak over the wall and run as far away as possible.

At my current level, I could easily take down five or six martial artists around the Heavenly Axe’s level.

I could scour every mountain I came across and rack up EXP and Fame—

“Mount Heng—A messenger pigeon has arrived from the Mount Heng Sword Sect!”

A martial artist had rushed into the hall and shouted.

Someone accepted the tightly rolled sheet of paper and unrolled it. Red words, as if written in blood, appeared before my eyes.

Even without a System translation, I could understand them.

> **Enemies Who Cannot Live Beneath the Same Sky**

*Enemies who cannot coexist beneath heaven.*

Jin Wikyung spoke with a grim expression.

“From this moment onward, our family enters a state of war. Without my seal, no one may enter or leave the family grounds, regardless of rank. Maintain a strict state of vigilance. Do not let a single ant through. Understood?”

“Yes!”

“……”

With my mind half gone, I heard a System notification ring in my ears.

Ding.

> **System**
>
> - The **Mount Heng Sword Sect** has declared war on the **Jin Family of Taiyuan**.
>
> - A **War** relationship has been established between both factions.
>
> - The **Mount Heng Sword Sect** has designated you as a public enemy of the sect.
>
> - You will incur severe penalties if you flee.
>
> - The **Main Quest — War** has been created.

…Heh. Heh heh heh.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 18`.

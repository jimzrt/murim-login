# Master Edit Task — Chapter 19

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
| 진위경    | **Jin Wikyung**    |
| 위팽     | **Wipeng**         |
| 이소군    | **Lee Seogeun**    |
| 월화     | **Wolhwa**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 무인     | **martial artist**                               | Default term                                          |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 기녀     | **courtesan**                                    |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 지부장    | **Branch Leader**                            |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |
| 은소월 | **Eun Sowol** |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |

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

#### Chapter 17 tail (verified mastered)

…
eyebrows. He looked like an immortal who had stepped out of an old painting. His straight back, broad shoulders, and taut skin seemed to defy his age. *But why is he staring at me so intently?* I put some force into my gaze and tried to glare back at the Head Elder… Then I quietly looked away. Not because I thought I would lose if we fought. It was respect for my elders. Respect for my elders. Really. *I’ll just keep my head down.* Jin Wikyung’s Sound Transmission continued in the meantime. —You may not know this because you lost your memory, but the Head Elder is your great-uncle and the most senior elder in the family. Be especially careful with your words and actions. I hadn’t even seen my father’s face, and now I had a great-uncle. *Maybe there were in-laws, eighth-degree relatives, and even one of my father’s cousins somewhere in this room.* I gave Jin Wikyung a small nod. —And… you must not be flustered by what happens from this point onward. Calmly tell them only the truth. Do you understand? I didn’t know exactly what was going on, but one thing was certain: Jin Wikyung was on my side. I nodded again, and Jin Wikyung rose with a faint smile. “Silence, everyone.” His voice, infused with internal energy, swept across the meeting hall. “This is a family council of the Jin Family of Taiyuan, and we have gathered to discuss a grave matter. Since the witness has arrived, I intend to begin the interrogation.” The meeting hall had fallen silent before I knew it. With everyone’s attention fixed on him, Jin Wikyung spoke. “By the authority of the Lesser Family Head and current acting Family Head, I begin this interrogation. Third Young Master Jin Taekyung, step forward.” I felt everyone’s eyes on me as I walked forward. I had expected this much. They hadn’t summoned me for no reason. But… “I ask you this. Did you poison Lee Seogeun of the Mount Heng Sword Sect?” That was something I hadn’t expected. * * * “No.” I barely managed to get the word out. My thoughts were a mess from the sudden question. *Lee Seogeun was dead? Poisoned, at that?* “Tell us the truth. If your words are proven false…” “I had nothing to do with poisoning Lee Seogeun.” My answer was as sharp as a blade. Jin Wikyung let out a sigh tinged with relief. —Keep doing exactly this. The interrogation proceeded quickly. They asked questions, and I answered. Starting with Jin Wikyung, they fired one question after another at me. About half of the questions concerned whether I had been involved in poisoning Lee Seogeun, and I continued to deny it. *Because it was true.* Just in case, I secretly opened my System Window and checked. I was certain. None of my martial arts or abilities had anything to do with poison. I didn’t have any such Items, either. That was why I could answer without hesitation. “No.” The problem was that, at some point, the atmosphere in the meeting hall began to take a strange turn. “Do you have any evidence to prove it?” “Evidence?” White Tiger Hall Leader, was it? The man whose name I didn’t even know stared at me with obvious displeasure. “That is correct. Evidence. I mean evidence that would prove the Third Young Master’s innocence.” *What the hell is this bastard talking about?* “Why do I have to prove it?” “What?” “Don’t ‘what’ me.” “Listen here, Third Young Master!” “You’re free to suspect me, but shouldn’t you be the ones looking for evidence? Am I wrong?” I’d let this go on long enough. Did these bastards think I was some damn wrapping cloth?[^1] Fuming, I glared at the White Tiger Hall Leader as he sat down, then noticed something strange. *Well, well. Look at this.* The White Tiger Hall Leader kept stealing glances at the old men of the Elder Council. The strange thing was that everyone who had been pressing and interrogating me was doing something similar. Nearly half the people in attendance were acting this way. It was getting difficult to pretend I hadn’t noticed. *So this is a factional struggle.* Jin Wikyung and the Elder Council. Even now, a power struggle was taking place between the senior members of the family and the Lesser Family Head who was young enough to be their grandson. *What a family.* Only a few people remained to question me. The problem was who those people were. Faces covered in age spots. Canny, experienced eyes. The old men of the Elder Council. The oldest and fattest of them opened his mouth. “Enough of this empty questioning. There is only one thing this old man wishes to ask. Where did this matter begin?” The senior members allied with the Elder Council answered as if they had been waiting for the question. “The Third Young Master.” “Who was it that dragged our family’s reputation through the mud with disorderly words and conduct?” “The Third Young Master.” The same answer came from several places around the room. “Then who was it that laid hands on the Mount Heng Sword Sect’s treasured jewel and brought about the present crisis?” “…” *Just kill me already, you bastards.* [^1]: In Korean, the line puns on *boja* (“let’s see / wait and see”) and *bojagi*, a wrapping cloth.

#### Chapter 18 tail (verified mastered)

…
Wikyung was the one who had spared them, yet they were making a huge scene. Go on, put on a show. A real show. I watched the spectacle, clicking my tongue inwardly, when— *Wait. A show?* An inexplicable sense of wrongness settled over me. I hurriedly examined the people gathered around the Head Elder. And then I noticed it. The smiles flickering around the lips of the Elder Council members who had cornered me earlier. *No way…* Had all of this been planned? Every last bit of it? Why? For what purpose? Countless questions rose and vanished. My thoughts were a complete mess. *Does Jin Wikyung know something?* I didn’t even need to turn around to look for him. The Head Elder was already holding Jin Wikyung’s hand high in the air and shouting. “With the Family Head absent, the Lesser Family Head is effectively the Family Head. I support the Lesser Family Head in this matter. If we unite around him, then no matter how formidable they are, they will not dare challenge the Jin Family!” The heated atmosphere. The people’s cheers and shouts. *Where had I seen this before?* It felt strangely familiar. And then— “Thank you.” The moment I saw the corners of Jin Wikyung’s mouth quiver and the Head Elder’s strange smile, I realized where that familiar feeling came from. *A campaign rally.* The Head Elder’s figure overlapped with the politicians I had seen on television. * * * It left a bad taste in my mouth, but once the Head Elder raised Jin Wikyung’s hand, the meeting proceeded swiftly. The discussion about the duel, which the Elder Council faction had stubbornly kept dragging out, disappeared entirely. Instead, the meeting focused on preparing for war. “How many men are currently available?” “If we call back the martial artists stationed outside… roughly two hundred.” As many as two hundred? I was astonished by the unexpectedly large number, but the next question made me shut my mouth. “If we select only elites of First Rate or higher?” “Fewer than twenty. Of course, that number would be different if we included everyone present.” Including the senior members, there were around thirty or forty First Rate masters. I didn’t know much about how things worked here, but that seemed like a decent number. As expected of a prestigious family with deep roots. Two hundred years of accumulated strength didn’t simply vanish. “What about the Mount Heng Sword Sect?” “At least three hundred martial artists have been confirmed so far.” Three hundred. And that was only the minimum, putting the difference at more than a hundred men. But that was fine. It wasn’t as if fights were decided by numbers— “And they have more than fifty First Rate martial artists.” This war was going to be difficult. Still, with masters like Jin Wikyung and Wipeng, it was a fight worth attempting. They were high-level NPCs beyond what my Qi Sense could read. The Head Elder probably belonged to that category, too. “Our family has three Peak masters in total: the Lesser Family Head, the Head Elder, and Sir Wipeng. The Mount Heng Sword Sect has five.” …Fuck this. I couldn’t do it. Seriously. *What? A prestigious family with deep roots? Two hundred years of history?* What the hell had these bastards been doing for two hundred years? I’d heard the Mount Heng Sword Sect was less than thirty years old, yet we weren’t merely outmatched in military strength. We were being steamrolled. Steamrolled. *Did the Black Death sweep through last year or something?* Whether there had been a plague or not, I felt like I was going insane. I was staring at the meeting-hall ceiling, which had yellowed before I knew it, when I suddenly made a decision. *I need to run.* Around four in the morning should do. Once everyone was asleep, I’d sneak over the wall and run as far away as possible. At my current level, I could easily take down five or six martial artists around the Heavenly Axe’s level. I could scour every mountain I came across and rack up EXP and Fame— “Mount Heng—A messenger pigeon has arrived from the Mount Heng Sword Sect!” A martial artist had rushed into the hall and shouted. Someone took the tightly rolled sheet of paper and unrolled it. Red characters, as if written in blood, appeared before my eyes. Even without the System translating them, I could understand what they said. > **Enemies Who Cannot Live Beneath the Same Sky** *Enemies who cannot coexist beneath heaven.* Jin Wikyung spoke, his expression grim. “From this moment onward, our family enters a state of war. Without my seal, no one may enter or leave the family grounds, regardless of rank. Maintain a strict state of vigilance. Do not let so much as a single ant through. Understood?” “Yes!” “…” With my mind half gone, I heard a System notification ring in my ears. Ding. > **System** > > - The **Mount Heng Sword Sect** has declared war on the **Jin Family of Taiyuan**. > > - A **War** relationship has been established between the two factions. > > - The **Mount Heng Sword Sect** has designated you as a public enemy of the sect. > > - You will incur severe penalties if you flee. > > - The **Main Quest — War** has been created. …Heh. Heh heh heh.

## Korean source

```text
＃19화



퀘스트



[전쟁]

두 가문의 명운을 건 전쟁이 시작되었습니다.

무림에서 자신을 증명하는 것은 오로지 힘! 살아남는 자가 강하고, 강한 자만이 살아남을 것입니다.

당신의 무운을 빕니다.



등급 : 메인 퀘스트

제한 : 진태경

임무 : 항산검문의 항복 또는 멸문 (미완료)

보상 : ???

실패 : ???





뚫어져라 퀘스트창을 노려보는 내게, 진위경이 말했다.

“많이 피곤한가 보구나.”

피곤? 현재 내 심리 상태를 그렇게 간단한 단어로 정의할 수 있다는 사실에 놀랐다.

나는 대답 대신 김이 모락모락 피어오르는 찻잔을 바라봤다.

‘이미 엎질러진 물이다.’

나름 노력했지만 전쟁을 막을 수는 없었다. 가로회의는 작전 회의로 바뀌었고, 대장로의 전폭적인 지지를 받은 진위경은 망설임 없이 지휘봉을 들었다.



태원진가의 무사들은 지금 즉시 본가로 집결하라!



동틀 무렵 수십 마리의 전서구가 하늘을 날았고, 전령은 말을 달렸다. 철저한 경계망이 그물처럼 펼쳐졌다.

그렇게 바짝 긴장된 분위기에서 가로회의가 파하자 나와 진위경, 위팽은 소가주 집무실로 자리를 옮겼다.

“언젠가 벌어질 일이었다. 태경이 네 탓이 아니야.”

진위경의 따스한 말에 눈물이 날 것 같다. 감동해서가 아니라, 억울해서다.

‘당연히 내 탓이 아니지!’

그리고 말이 나왔으니 말인데, 그 ‘언젠가 벌어질 일’이 왜 하필 지금 벌어지냐고.

내심 분통을 터트리고 있을 때 위팽이 불쑥 입을 열었다.

“그런데 주군.”

“왜 그러나?”

“대장로 말입니다만…… 도무지 의중을 모르겠습니다.”

대장로. 그 이름을 듣는 순간 다른 생각은 내팽개쳤다. 이 게임에서 만난 NPC 중 가장 꺼림칙한 인물이다.

진심으로 가문을 위하는 것 같기도 하고, 자신의 이익을 위해 움직이는 정치인의 냄새도 풍기고.

나는 조심스럽게 입을 열었다.

“대장로는 어떤 사람이죠?”

“높은 경지의 무인이면서 심계도 깊다. 무림에서 가장 위험한 부류라 할 수 있지.”

“그 정도인가요?”

진위경이 무겁게 고개를 끄덕였다.

“다른 장로들조차 대장로의 수족에 불과하다. 그는 모습을 좀처럼 드러내지 않으면서도, 장로원이라는 손발을 이용해 중진들을 포섭하고 휘하로 끌어들였지. 그 세월이 수십 년이다.”

“그럼 가로회의에서 우리 손을 들어 준 것도…….”

“정확한 사실은 알 수 없지만 꿍꿍이가 있을 것이다. 분명해.”

“다 죽였어야 했습니다.”

위팽이 차가운 목소리로 불쑥 끼어들었다.

“불충한 역도들입니다. 대장로가 그들을 죽이자고 제안했을 때, 저는 솔직히 주군께서 받아들이셨으면 했습니다.”

나도 그랬다. 하지만 그것은 대장로의 교묘한 화법에 불과했다. 이 정도에서 물러나는 게 어떻겠냐는.

만약 진위경이 미친 척 그 제안을 수락했다면 결과는 뻔하다.

“혈사가 일어났겠지.”

“압니다. 그래서 참은 거고요.”

태원진가의 수뇌부가 반으로 갈라져 죽고 죽이는 싸움을 계속할 것이다. 지면 죽음이고, 이겨도 큰 피해를 입었을 것이다.

‘어쩌면 그게 대장로가 바랐던 결과일지도.’

대장로. 보이지 않는 손. 문득 떠오른 생각에 등골이 오싹했다. 마침 내가 느낀 대장로의 이미지와도 딱 맞아떨어진다.

한발 물러나 때를 기다리는 하이에나 같은 정치인.

진위경이 찻잔을 기울였다.

“하지만 어디까지나 짐작일 뿐. 대장로의 의중이 무엇인지는 모르는 것이다. 아직 그는 본가의 어른이며 강력한 아군이다. 주의는 하되 적대하지 말거라. 지금은 사람을 경계하기보다 상황을 헤쳐 나가야 할 때야.”

나무가 아니라 숲을 보라는 이야기다.

문제는 그 숲도 썩 좋은 상황이 아니라는 거지.

내 생각을 읽은 것처럼 위팽이 그에 관련된 이야기를 꺼냈다.

“상황도 좋지 않습니다. 외부 소식통에 의하면 이소군이 독살당했다는 소문이 퍼지면서 본가의 평판이 추락하고 있답니다.”

“고작 반나절 만에?”

“예. 산서성 전체가 그 얘기로 들썩거리고 있습니다.”

진위경의 얼굴에 근심이 서렸다.

“빠르군. 소문이 빨라도 너무 빨라. 확실히 뒤에 누군가 있어.”

여기에 인터넷이 있는 것도 아니고, 이 넓은 땅덩어리에 벌써 소문이 퍼졌다는 것은 확실히 이상한 일이다.

‘보이지 않는 적이라.’

도대체 누굴까. 제삼의 세력? 항산검문의 자작극?

나는 가급적 후자이기를 바랐다. 드러나지 않는 적만큼 위험한 건 없으니까.

“민심은 아직까지 반신반의하는 모양이지만 다른 문파들은…….”

“아직도 답이 없나?”

위팽은 대답 대신 고개를 숙였다.

진위경은 이소군의 독살 정보를 입수한 직후 곧장 산서성의 다른 중소 문파들에게 지원 요청을 했다. 하지만 빠짐없이 수포로 돌아간 모양이었다.

‘갈수록 최악인데 이건.’

진짜 도망쳐야 되나.

그런 생각을 하며 창밖을 바라보고 있을 때였다. 푸드득. 홰치는 소리와 함께 비둘기 한 마리가 창가에 내려앉았다.

“……답장, 온 것 같은데요?”



* * *



태원진가.

웅장한 필체로 적힌 현판, 그리고 삼엄한 기세로 정문을 지킨 무사들이 가까워지자 마부는 고삐를 느슨하게 늘어트렸다.

“정지. 신원과 목적을 밝히시오!”

수문위사가 크게 외치며 마차를 가로막았다. 상황이 상황인지라 그의 목소리에는 긴장감이 배어 있었다.

더군다나.

‘범상치 않다.’

고삐를 쥔 마부에게서는 단련된 무인의 냄새가 물씬 풍겼고, 네 마리 준마가 끄는 사두마차는 화려함과 동시에 기품이 있다.

‘그런데 왠지 낯이 익은데?’

마부도 그렇고. 마차도 그렇고. 어디서 봤더라?

잠깐 떠오른 의문은 마부의 날카로운 눈매를 보는 순간 잊혔다. 저 기세, 눈빛. 역시 범상치 않은 손님이다.

꿀꺽 침을 삼킨 수문위사가 재차 입을 열었다.

“신원과 목적을 밝혀 주십시오.”

마차의 문이 열리고, 붉은색 비단신이 사뿐히 내려앉았다.

그리고 봄바람처럼 살랑거리는 목소리가 수문위사의 귓가에 내려앉았다.

“홍화루에서 왔어요. 이름은 비밀.”

목소리와 함께 드러나는 얼굴.

수문위사의 눈이 몽롱하게 풀어졌다. 비단 그 혼자만의 일이 아니었다. 여인의 얼굴을 확인한 모두가 같은 반응이었다.

수문위사의 입에서 넋 나간 목소리가 흘러나왔다.

“아, 비밀…… 그럼 어떤 용무로 오셨는지.”

여인, 월화는 매혹적인 미소와 함께 대답했다.

“음. 외상값 받으러?”



* * *



“잘 지냈어요? 나 안 보고 싶었고?”

나는 엉거주춤 일어선 채로 굳어 버렸다.

잊을 수 없는 얼굴. 그리고 여기 있어서는 안 되는 얼굴이다.

“월화?”

이 게임에서 처음 만난 NPC. 홍화루의 기녀이자 나, 진태경의 새끼손가락. 그거.

누나가 왜 거기서 나와……?

“역시 기억하시네. 우리 진 공자님.”

월화가 까르르 웃는다. 얘는 얼굴도 예쁜데 웃음소리도 예쁘고, 예쁜 애가 웃으니까 더 예뻐…… 아니, 지금 이럴 때가 아닌데.

나는 잔뜩 숨죽인 목소리로 속삭였다.

“여긴 어쩐 일로 왔어요. 아, 됐고. 나가요. 나가.”

팔꿈치로 슬쩍슬쩍 월화의 몸을 밀었다. 와, 진짜 미치겠다.

하필이면 이런 분위기에 나타나다니.

가문 전체에 비상 경계령이 떨어졌는데 기녀 불렀다고 소문이라도 나 봐라. 내 평판이 어떻게 될지 상상만 해도 눈앞이 아찔하다.

“찌르지 마요. 간지럽잖아.”

“알겠으니까 빨리 나가요. 여기 지금 다른 사람들도 있는데 갑자기 와서 뭐 하자는 겁니까? 중요한 손님도 오시기로 했는데.”

타이밍도 참 더럽게 안 좋다. 나는 소가주 집무실에서 하오문이라는 문파의 손님을 기다리는 중이었다.

당연하게도 진위경, 위팽과 함께였다.

“태경아.”

진위경의 부름. 나는 뒤도 돌아보지 않고 황급히 손을 내저었다.

“아, 생각하시는 그런 거 아닙니다. 저 안 불렀어요. 이분도 이제 가실 거래요. 그렇죠?”

월화의 웃음소리가 높아졌다.

“우리 진 공자님은 여전히 귀여우셔. 근데 잘못 짚었어. 나 여기 볼일 있어서 온 거거든.”

“어허, 우리 진 공자는 무슨. 나 오늘부터 순결하게 살 거예요. 이제 그쪽 볼일 없으니까 빨리 나가요.”

“음. 싫은데?”

그럼 어쩔 수 없지. 힘으로 옮기는 수밖에. 나는 절박한 심정으로 월화의 허리를 붙잡고 번쩍 들어서…….

“응?”

뭐야, 이거. 왜 안 들려. 월화가 겉보기에는 늘씬하지만 통뼈라 무게가 많이 나가나?

‘개소리지.’

내 힘 스탯이 몇인데. 단순 근력으로만 해도 돌멩이를 가루로 만들어 버릴 수 있다. 그런데 내가 여자 NPC 하나 못 든다는 건…….

“저, 태경아?”

진위경의 두 번째 부름은 무시한 나는 슬그머니 손을 풀었다. 그리고 [기감]을 끌어올렸다.

“아하하하하! 미치겠다, 진짜.”

웃겨 죽는 월화의 머리 위로 레벨창이 뜸과 동시에, 진위경의 세 번째 부름이 들려왔다.



[Lv.50 은소월]



“태경아, 인사드려라. 하오문 산서 지부장님이시다…….”

아아. 아아아.

죽고 싶다.



* * *



“인사 올립니다. 하오문 산서 지부장, 월화입니다.”

은소월. 아니, 일단은 월화라고 해 두자. 그녀는 지금까지의 모습과는 달랐다. 동작 하나하나에 귀부인 같은 기품과 우아함이 묻어 나왔다.

“태원진가의 진위경이오.”

“위팽입니다.”

“…….”

벙어리 삼룡이마냥 입을 다물고 있는 내게 월화가 씩 웃어 보였다. 불길한 웃음이다.

‘안 돼. 웃지 마.’

말 걸지도 마. 제발 그러지 마.

“한 분 소개를 못 들은 것 같은데요.”

시선이 따갑다. 탁자 아래로 누군가 내 발을 밟았다.

나는 피를 토하는 심정으로 입을 열었다.

“……진태경입니다.”

“네에. 저도 잘 부탁드려요. 진 공자님.”

커흠. 진위경이 헛기침과 함께 힐끔 나를 살폈다.

“내 동생과 친분이 있는 줄은 몰랐소만.”

“저희 가게 단골이시거든요. 태원에 있는 홍화루. 본 문의 산서지부이기도 하지요.”

“아, 단골…….”

나는 사람들의 시선을 회피했다. 풉, 웃음을 터트린 월화가 본론을 꺼내 들었다.

“이제 일 얘기를 해 볼까요?”

여러 번 느끼는 거지만 역시 시원시원한 여자다. 진위경과 위팽도 내게서 시선을 떼고 대화에 임했다.

“우선 하오문의 도움에 진심 어린 감사를 표하오.”

“별말씀을요.”

“한데, 본가를 도우려는 이유를 알 수 있겠소?”

진위경의 말에 월화가 싱긋 웃었다.

“이유라…… 필요하다면 말씀드리지요. 우선 첫째, 본 문의 이득을 위해서입니다.”

“이득이라. 구체적으로 어떤 보상을 원하시오?”

“항산검문이 소유한 점포와 재화의 절반.”

“좋소.”

“주군!”

위팽이 황급히 나섰지만 진위경은 아랑곳하지 않았다.

월화도 살짝 놀란 기색이었다.

“결정이 빠르시군요.”

“가문의 모든 걸 걸었으니까.”

“이미 합의된 내용인가요?”

“나는 소가주고, 아버님이 안 계신 지금 가주 대행의 권한을 갖고 있소.”

“내부의 반발이 꽤 거센 걸로 아는데요. 예를 들면 장로원이라든가?”

“역시 하오문. 정보가 빠르군.”

“어쩔 수 없지요. 이 삭막한 무림에서 살아남으려면 정보가 필수인데. 이런 수완이라도 있어야 먹고살지 않겠어요?”

월화의 웃음을 보면서, 문득 한 가지 생각이 들었다.

‘저 정보. 혹시 내가, 아니 진태경이 흘린 건가?’

하오문, 그 이름을 어디서 들어봤나 했더니 무협 소설에서 단골로 등장하는 정보 문파다. 즉, 지부장인 월화는 베테랑 정보 상인인 셈이고.

거기에 더해 50레벨의 출중한 무인이기도 하다. 저런 여자가 기녀로 위장해서 진태경 같은 놈을 만나?

‘개가 웃을 소리지.’

나는 월화를 응시했다. 여신이 내려왔나 싶을 정도로 눈부신 외모다. 그녀가 웃을 때마다 장미가 생각났다. 그 화려함에 숨겨진 날카로운 가시가 이제야 보인다.

진위경이 굳은 얼굴로 말했다.

“그럼 이제 두 번째 이유를 말하시오.”

월화가 예의 화사한 미소를 지으며 대답했다.

“진 공자가 마음에 들어서요.”

“예?”

“어린 데다가 얼굴 잘생겼고, 몸 좋고, 성격도 귀엽고.”

“…….”

“…….”

도대체 어디까지가 진심이고 농담이야?
```

## Current accepted English baseline

```markdown
# Chapter 19

> **System**
>
> **Quest**
>
> **War**
>
> A war that will decide the fate of two factions has begun.
>
> In Murim, the only way to prove yourself is through strength! Those who survive are strong, and only the strong will survive.
>
> May fortune favor you in battle.
>
> **Grade:** Main Quest  
> **Restriction:** Jin Taekyung  
> **Mission:** Surrender or destruction of the Mount Heng Sword Sect (Incomplete)  
> **Reward:** ???  
> **Failure:** ???

Jin Wikyung spoke to me as I stared fixedly at the Quest Window.

“You look very tired.”

Tired? I was amazed that my current state of mind could be summed up in such a simple word.

Instead of answering, I looked at the steaming teacup.

*The water’s already been spilled.*

I had done my best, but I couldn’t stop the war. The family council had turned into a war council, and with the Head Elder’s full support, Jin Wikyung had taken up command without hesitation.

> Martial artists of the Jin Family of Taiyuan, assemble at the main family residence immediately!

At dawn, dozens of messenger pigeons took to the sky while messengers rode hard on horseback. A tight security net was thrown over the entire area.

When the family council finally broke up in that tense atmosphere, Jin Wikyung, Wipeng, and I moved to the Lesser Family Head’s office.

“It was bound to happen someday. This isn’t your fault, Taekyung.”

I felt like crying at Jin Wikyung’s warm words. Not because I was moved, but because it felt so unfair.

*Of course it wasn’t my fault!*

And since we were on the subject, why the hell did that “bound to happen someday” have to happen now?

While I was fuming inwardly, Wipeng suddenly spoke.

“My lord.”

“Why?”

“The Head Elder… I simply cannot figure out what he’s thinking.”

The Head Elder. The moment I heard that name, I abandoned all other thoughts. He was the most unsettling person among the NPCs I had encountered in this game.

He seemed genuinely devoted to the family, yet he also gave off the unmistakable air of a politician maneuvering for his own benefit.

I cautiously opened my mouth.

“What kind of person is the Head Elder?”

“He is a martial artist of a high realm, and his schemes run deep. You could call him one of the most dangerous types of people in Murim.”

“That dangerous?”

Jin Wikyung nodded heavily.

“Even the other Elders are little more than the Head Elder’s hands and feet. He rarely reveals himself, yet he has used the Elder Council to win over influential members and bring them under his command. He has been doing so for decades.”

“Then his supporting us at the family council…”

“We cannot know the exact truth, but he must have an ulterior motive. Of that, I am certain.”

“We should have killed them all.”

Wipeng cut in abruptly, his voice cold.

“They are disloyal rebels. When the Head Elder proposed killing them, I honestly hoped you would accept.”

I had felt the same way. But that had merely been the Head Elder’s clever way of speaking—a suggestion that perhaps we should back down at this point.

If Jin Wikyung had pretended to be insane and accepted that proposal, the result would have been obvious.

“A bloodbath would have broken out.”

“I know. That’s why I held back.”

The Jin Family of Taiyuan’s leadership would have split in two and continued fighting until they killed one another. If we lost, we would die. Even if we won, we would suffer tremendous damage.

*Maybe that was exactly what the Head Elder wanted.*

The Head Elder. An invisible hand.

A chill ran down my spine at the thought. It fit the image I had formed of him perfectly.

A politician like a hyena, stepping back and waiting for his moment.

Jin Wikyung tilted his teacup.

“But that is only a guess. We do not know what the Head Elder truly intends. He is still one of the family’s elders, and a powerful ally. Be wary of him, but do not make an enemy of him. For now, we need to overcome the situation rather than distrust everyone around us.”

He was telling me to look at the forest, not the trees.

The problem was that the forest itself wasn’t exactly in good shape, either.

As if he had read my thoughts, Wipeng brought up the subject.

“The situation is not good, either. According to our outside sources, rumors that Lee Seogeun was poisoned have begun spreading, and the main family’s reputation is falling.”

“In only half a day?”

“Yes. All of Shanxi is in an uproar over it.”

Concern clouded Jin Wikyung’s face.

“That is fast. Far too fast. Someone is definitely behind this.”

There was no internet here, and yet rumors had already spread across this vast land. It was certainly strange.

*An invisible enemy.*

Who could it be? A third faction? A staged act by the Mount Heng Sword Sect?

I hoped it was the latter if possible. Nothing was more dangerous than an enemy who remained unseen.

“The people are still taking the rumors with a grain of salt, but the other sects…”

“Still no replies?”

Wipeng lowered his head instead of answering.

Immediately after obtaining the information about Lee Seogeun’s poisoning, Jin Wikyung had sent requests for support to the other small and mid-sized sects in Shanxi. But it seemed every one of them had failed.

*This keeps getting worse.*

*Do I really need to run?*

I was looking out the window, thinking that, when—

Flap, flap.

A pigeon landed on the windowsill with the sound of beating wings.

“…It looks like a reply has arrived?”

* * *

The Jin Family of Taiyuan.

As the carriage approached the grand signboard written in magnificent calligraphy and the martial artists standing guard at the main gate with a stern aura, the coachman loosened the reins.

“Stop. State your identity and purpose!”

The gate guard called out loudly and blocked the carriage. Given the circumstances, there was tension in his voice.

More than that—

*This isn’t ordinary.*

The coachman holding the reins gave off the unmistakable air of a trained martial artist, while the four-horse carriage had both luxury and dignity.

*But why does he look familiar?*

The coachman, too. The carriage, too. Where had he seen them?

The question vanished the moment he saw the coachman’s sharp eyes. That aura, that gaze. This was certainly no ordinary visitor.

The gate guard swallowed and spoke again.

“Please state your identity and purpose.”

The carriage door opened, and a red silk slipper stepped lightly onto the ground.

Then a voice as gentle as a spring breeze drifted into the guard’s ear.

“I’m from Honghwaru. My name is a secret.”

Her face appeared along with her voice.

The gate guard’s eyes grew dazed. He wasn’t the only one. Everyone who saw the woman reacted the same way.

A vacant voice escaped the gate guard’s mouth.

“Ah, a secret… Then what brings you here?”

The woman, Wolhwa, answered with a charming smile.

“Hmm. I’m here to collect an unpaid tab?”

* * *

“How have you been? Didn’t you miss me?”

I froze halfway to standing.

A face I could never forget. And a face that had no business being here.

“Wolhwa?”

The first NPC I had met in this game. A courtesan at Honghwaru—and my precious little finger. That thing.

*Why is noona coming out of there…?*

“You remember me after all. Our Young Master Jin.”

Wolhwa giggled. She was beautiful, had a beautiful laugh, and when a beautiful woman laughed, she became even more beautiful…

*No, this is not the time for that.*

I whispered in a tightly restrained voice.

“What brings you here? No, never mind. Leave. Get out.”

I nudged Wolhwa with my elbow.

*This is driving me insane.*

Of all times, she had to show up in this atmosphere.

The entire family was on high alert. If word got out that I had called for a courtesan, I couldn’t even imagine what would happen to my reputation. Just thinking about it made my vision swim.

“Don’t poke me. That tickles.”

“I know, so get out quickly. There are other people here. What are you trying to do by suddenly coming here? We’re expecting an important guest, too.”

The timing was damn awful, too. I was waiting for a guest from a sect called the Lower District Sect in the Lesser Family Head’s office.

Naturally, Jin Wikyung and Wipeng were there with me.

“Taekyung.”

Jin Wikyung called my name. Without even turning around, I hurriedly waved my hands.

“Ah, it’s not what you think. I didn’t call her. She’s leaving now, too. Right?”

Wolhwa’s laughter rose in pitch.

“Our Young Master Jin is still so adorable. But you guessed wrong. I came here because I have business to attend to.”

“Don’t call me ‘our Young Master Jin.’ I’m going to live chastely from today onward. I don’t have any business with you anymore, so get out quickly.”

“Hmm. No.”

Then there was no helping it. I would have to move her by force.

In desperation, I grabbed Wolhwa around the waist and hoisted her up—

“Huh?”

What the hell? Why won’t she lift?

Wolhwa looked slender, but was she so big-boned that she weighed a lot?

*That’s bullshit.*

What was my Strength stat again? With pure physical strength alone, I could grind a rock into powder. And yet I couldn’t lift one female NPC, which meant—

“Taekyung?”

I ignored Jin Wikyung’s second call and furtively let go. Then I heightened my Qi Sense.

“Ahahahahaha! This is driving me insane!”

As Wolhwa laughed herself to death, a Level Window appeared above her head. At the same time, I heard Jin Wikyung call my name for the third time.

> **System**
>
> **Lv. 50 Eun Sowol**

“Taekyung, greet her. She is the Branch Leader of the Lower District Sect’s Shanxi branch…”

Ah. Ahhh.

*I want to die.*

* * *

“Greetings. I am Wolhwa, Branch Leader of the Lower District Sect’s Shanxi branch.”

Eun Sowol.

No, for now, let’s just call her Wolhwa.

She was different from how she had acted until now. Every movement carried the grace and elegance of a noblewoman.

“I am Jin Wikyung of the Jin Family of Taiyuan.”

“I’m Wipeng.”

I kept my mouth shut like mute Samryong,[^1] and Wolhwa flashed me a grin.

It was an ominous grin.

*Don’t. Don’t smile.*

*Don’t talk to me. Please don’t.*

“It seems I haven’t been introduced to one person.”

Her gaze stung. Someone stepped on my foot beneath the table.

I opened my mouth with a feeling like I was coughing up blood.

“…I’m Jin Taekyung.”

“Yes. I hope we get along too, Young Master Jin.”

“Ahem.”

With a cough, Jin Wikyung glanced at me.

“I didn’t realize you were acquainted with my younger brother.”

“He is a regular at our establishment—the Honghwaru in Taiyuan. It also serves as this sect’s Shanxi branch.”

“Ah. A regular…”

I avoided everyone’s gaze. Wolhwa let out a burst of laughter, then brought up the real subject.

“Shall we talk business now?”

I had felt it several times before, but she really was a refreshingly direct woman. Jin Wikyung and Wipeng also turned their attention away from me and joined the conversation.

“First, allow me to offer my sincere thanks for the Lower District Sect’s assistance.”

“Think nothing of it.”

“But may I ask why you wish to help our family?”

Wolhwa smiled sweetly at Jin Wikyung’s question.

“The reason… I will tell you if necessary. First, we are doing this for our sect’s benefit.”

“Benefit. What specific compensation do you want?”

“Half of the shops and assets owned by the Mount Heng Sword Sect.”

“Good.”

“My lord!”

Wipeng hurriedly stepped forward, but Jin Wikyung paid him no heed.

Wolhwa also looked slightly surprised.

“You decide quickly.”

“Because I have staked everything the family has.”

“Has this already been agreed upon?”

“I am the Lesser Family Head, and with Father absent, I possess the authority of the acting Family Head.”

“I hear the internal opposition is quite fierce. The Elder Council, for example?”

“As expected of the Lower District Sect. Your information is fast.”

“It cannot be helped. Information is essential for survival in this bleak Murim. We need skills like these to make a living, don’t we?”

Watching Wolhwa smile, I suddenly had a thought.

*That information. Did I—or rather, did Jin Taekyung—let it slip?*

I had wondered where I had heard the name Lower District Sect before. It was an information-gathering sect that appeared regularly in martial-arts novels. In other words, Wolhwa, its Branch Leader, was a veteran information merchant.

On top of that, she was an outstanding martial artist at Level 50. A woman like that had disguised herself as a courtesan to meet a guy like Jin Taekyung?

*Even a dog would laugh at that.*

I stared at Wolhwa.

Her beauty was dazzling enough to make me wonder if a goddess had descended. Whenever she smiled, roses came to mind. Only now could I see the sharp thorns hidden beneath all that splendor.

Jin Wikyung spoke with a stiff expression.

“Then tell us the second reason.”

Wolhwa answered with her usual radiant smile.

“Because I like Young Master Jin.”

“Excuse me?”

“He’s young, handsome, well-built, and has such a cute personality.”

“…”

“…”

*How much of that was sincere, and how much was a joke?*

[^1]: Samryong is the mute protagonist of a well-known Korean short story; his name literally means “Three Dragons.”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 19`.

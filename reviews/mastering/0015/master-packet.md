# Master Edit Task — Chapter 15

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
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 이소군    | **Lee Seogeun**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 문주     | **Sect Leader**                              |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |

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

#### Chapter 13 tail (verified mastered)

…
Yet right now, they were united in glaring at me. “Fuck…” Wipeng turned his head at my mutter. “The Lesser Family Head believes in you. Don’t forget that.” Right. Jin Wikyung was there. My greatest hope and my shield. As I reminded myself of that fact, Wipeng threw open the doors to the main assembly hall. “I’ve brought the Third Young Master.” I took a deep breath and stepped into the pavilion, repeating the same words over and over in my head. *Even if a tiger carries you off, you can survive as long as you keep your wits about you. Even if a tiger carries you off, as long as you keep your wits…* The moment I entered the hall, the low murmurs abruptly stopped. A dozen men, young and old, stood arrayed along either side, while Jin Wikyung occupied the seat of honor. And in the center stood a young man. “It’s been a while, Young Master Jin.” The instant I met that unpleasant smile— Ding. > **System** > > - **Killing intent** detected! …At least use your blinker before pulling in. * * * Killing intent. I knew it well. Monsters were literally bundles of malice and killing intent. I had felt it countless times and thought I had grown used to it. But this guy… *He was different.* This was on an entirely different level from anything I had experienced. If I had to compare it, it was like the difference between a low-level monster and a mid-level monster. His killing intent was far more refined, more furtive, and more chilling. “I caught a glimpse of you in the marketplace last time. I don’t know whether you remember me.” Lee Seogeun spat out each word. A System window floated in the air above his head. > **System** > > **Lv. 30 Lee Seogeun** That was the Level I had read with Qi Sense the instant I detected his killing intent. It was more than twice my Level. *This is insane.* Even worse were the looks from everyone else. Dozens of sinister gazes, young and old alike, were fixed on me. My knees began to tremble. In that atmosphere, Lee Seogeun opened his mouth. “What a shame. If you had come a little earlier, we could have had a deeper conversation. We were discussing something interesting until just now.” “…Were you?” “Aren’t you curious what we were discussing?” “N-no, I’m fine.” I could only hope it hadn’t been a discussion about whether to cut off my head or my balls. And if that miserable guess was correct, I would rather they cut off my balls than my head. *If I’m lucky, a Level Up might heal them… Why the hell do I even have to think about this?* It was simply miserable. Lee Seogeun studied my expression before speaking again. “I heard you returned to the family a few days ago. Where were you?” “Honghwaru.” “Then where were you before you went to Honghwaru?” *I was at a goshiwon, you bastard.* I wanted to tell him everything honestly. *I got fired from my Guild that day, had a glass of soju with the hyung from the goshiwon, then went into the capsule and fell asleep. When I opened my eyes, I was at Honghwaru, and now I’m working hard toward Logout. Something like that.* *I’d be lucky if he didn’t draw his sword.* As I hesitated, unable to answer, Lee Seogeun pulled something from inside his robes. I thought he really was drawing a sword, but it turned out to be a bundle of papers. “Since you don’t seem to remember, I’ll tell you. The night before you went to Honghwaru, you visited Myeongwollu. You went to the deluxe room you had reserved.” “Myeongwollu?” “The pleasure house you used to visit all the time? Don’t try to make excuses by saying you’ve never heard of it. These are the testimonies and signatures of the people who saw you there that day.” In other words, it was a list of witness statements. I read through the papers, thinking I might as well take a look. Then I noticed something strange. “What is this?” “You don’t know even after seeing it yourself?” This bastard was casually dropping the formal speech now. “I’m saying that because I read it. There isn’t a single proper testimony here.” I read every one of the dozens of statements, but there wasn’t a decisive testimony anywhere. They all said roughly the same thing. Jin Taekyung had gotten thoroughly drunk and gone to the wrong room. That room belonged to a daughter of the Mount Heng Sword Sect. Then someone heard screaming. “The bastard who tore my sister’s clothes and tried to rape her is shameless beyond belief. You really are exactly as the rumors say.” “No, that’s not what—” “You bastard!” Flutter! “Ah.” The bundle of papers smacked me in the face and scattered across the floor. Lee Seogeun spat a wad of phlegm onto them. *Well, look at this asshole.* I wasn’t annoyed. Just suspicious. How should I put it? This whole chain of events—especially the testimonies—felt incredibly contrived. But I had no time to dwell on that unease. “Come out with me, you bastard! I’ll make you pay for what you’ve done!” The instant Lee Seogeun shouted— Ding. > **System** > > - A **Duel** Quest has been generated. What’s this now?

#### Chapter 14 tail (verified mastered)

…
afraid. Fine. If you answer my questions honestly, I’ll go easy on you.” ……To be honest, I almost wavered. “Cut the bullshit.” “Oh? Putting on airs because you’re the son of a martial family, are you?” Lee Seogeun laughed as if I were ridiculous. “Let me ask you one thing. What gave you the confidence to accept this duel? Your martial arts are pathetic, and you’re known as a coward. I want to hear your reason.” “My reason?” No matter how much I thought about it, this was the only way. If war broke out, I would become a public enemy of the Mount Heng Sword Sect. Hunting? Leveling up? I could forget about it. The moment I stepped outside the fence of the Jin Family of Taiyuan, assassins who caught my scent would come running. *As long as I stay alive, there’ll be another chance.* I had magic. The recovery magic called leveling up. My mind eased slightly. “I thought someone like you might be manageable.” “Pfft! You’re just a wet-behind-the-ears pup.” It was a mild provocation, but it didn’t work. He was confident in his abilities, and it showed in his relaxed manner. “Is it my turn to ask a question now?” “I never said I’d answer them… but I’ll indulge you as if they were your last words.” “This incident. You fabricated it, didn’t you?” Perhaps the question caught him off guard, because Lee Seogeun’s expression stiffened awkwardly. That expression was answer enough. *So I was right.* I had wondered if that was the case, but sure enough. No wonder the whole thing had smelled rotten from beginning to end. “You petty bastards. You should’ve just declared war.” “……I’ll tear that mouth apart.” Lee Seogeun lifted his massive greatsword and muttered ominously. I raised the Sharp Spear I had taken out beforehand. *All right. Let’s do this.* I had learned martial arts. I also had instincts honed through seven years of real combat. An F-rank Hunter and a Second Rate Murim martial artist. Don’t underestimate the skills I’d honed working two jobs! “Graaah!” Lee Seogeun was more agile than I’d imagined. He closed the distance in an instant, and I blocked the greatsword crashing straight down with the shaft of my spear. Kra-kra-kraang. “Urgh.” I’d worried the Sharp Spear might be cut clean in half, but it was sturdy, as befitted a solid piece of steel. Even so, the force behind the greatsword began driving both my feet into the ground. “Die, you insect!” “Hup!” Up close, his aura was even more suffocating. Was this what a monster’s Fear felt like? “Kneel and beg for forgiveness now! Then I’ll let you off with one arm!” - Little brother! Over Lee Seogeun’s shoulder, I saw Jin Wikyung spring to his feet. The Mount Heng Sword Sect’s people watched while snickering, and the Jin Family people turned their heads away as if they couldn’t bear to watch. *I have to hold out.* At least until Jin Wikyung gets here! “Graaah!” Lee Seogeun’s greatsword struck from every direction in a relentless barrage. The weapons were clearly clashing, iron against iron, but all I could hear was cannon fire. Boom! Boom! Boom! I blocked them. “Graaah!” “Hup!” Boom! Boom! I blocked them again. “Graaah!” “Haaah!” Boom! I blocked another. “Graaah…” “Haaah…” “……?” “……?” The next moment, Lee Seogeun and I locked eyes. The instant I saw the bewilderment and confusion in his gaze, I knew he was thinking exactly what I was. *What the hell is this?* Lee Seogeun was strong. He had the brute strength of a giant monster, moved with surprising agility for someone so muscular, and swung his massive greatsword like a matchstick. And that wasn’t all. He was a Young Master of the Mount Heng Sword Sect—a sect that could actually throw its weight around. The martial arts he used had to be quite advanced. And yet… *This is… doable?* Even now, I was blocking each and every strike of the continuously swinging greatsword. More than twenty attacks. And more than twenty blocks. I could see them. That was why I could block them. I slowly lifted one of my legs, which had been buried in the ground up to the ankle. It came right out. *Could it be…* No way. Surely not. Ssshwip! At that moment, I deflected the greatsword flying toward my waist along the shaft of my spear. Then, without thinking, I kicked Lee Seogeun in his unguarded chest. Whack! “Urgh!” ……Huh? Clutching his stomach, Lee Seogeun skidded back five or six steps. Then he casually rubbed the bridge of his nose as if nothing had happened. “Not bad. You’ve got a trick or two despite being trash.” “……” “Heh. I won’t hold back anymore.” “……Hey.” “With my next strike, I’ll smash your head—what?” I raised a hand, looking awkward, and pointed at his mouth. “You’re bleeding.” A beat later, a thin line of blood ran down from the corner of Lee Seogeun’s mouth. He had probably bitten his tongue. That had to hurt. “Ah! Eeng! Eek! Hup!” Lee Seogeun wiped away the blood with a series of ridiculous yelps. “Don’t wipe it. Leave it.” “……?” “It’ll be easier to wipe it all off at once later.” Because from now on, I was going to beat the absolute shit out of him. > **System** > > - The Status Effect **Intimidation** has been removed!

## Korean source

```text
＃15화



위팽은 생각했다.

‘지금 내가 뭘 보고 있는 거지?’

보면서도 믿을 수 없는 일이 벌어지고 있었다. 삼공자가, 다른 사람도 아닌 바로 그 삼공자가 이소군을 상대로 팽팽하게 맞서다니.

‘환각인가?’

이소군이 누군가.

항산검문주의 무공을 이은 혈육이자 일류 검객이다.

처음 삼공자가 이소군의 비무를 받아들였을 때, 위팽은 내심 한숨을 내쉬었다. 간신히 삼류를 면한 놈이 무슨 배짱으로.

그리고 뭐? 나오라고? 한판 뜨자고?

‘미친놈, 지랄한다.’

근래 들어 뭔가 바뀐 것 같긴 했다. 갑자기 꼬박꼬박 존댓말을 쓰질 않나, 밤늦게까지 무공을 익히지 않나.

아, 기억을 잃었다는 개소리도 있었지.

그때는 저놈이 미쳤나, 싶었는데 오늘 항산검문의 장중보옥을 건드렸다는 얘길 듣고 깨달음이 왔다. 하마터면 그대로 우화등선할 뻔했다.

‘그럼 그렇지. 인간이 하루아침에 바뀔 리 없지.’

태원진가에 몸담은 세월이 십 년이 넘는다. 위팽의 눈에 비친 진태경은 싹수가 노란 정도를 넘어 황금빛에 가깝다.

하지만 별수 있나. 그는 주군의 사랑을 한 몸에 받는 막냇동생이고 태원진가의 직계다. 이소군에게 반병신이 되기 전에 구해야겠다는 생각이었다.

그런데…….

퍽, 퍽, 퍽!

이제는 사정없이 두드려 팬다. 진태경이 이소군을.

위팽도 익히 알고 있는 무공이었다. 진가보법과 진가창법.

두 무공을 연계하는 솜씨도 제법인데, 뒷골목에서 십 년쯤 굴러먹다 온 낭인의 노련미까지 엿보였다.

‘이게 도대체…….’

무공은 하루 이틀의 노력으로 이룰 수 있는 것이 아니다.

그것이 위팽이 믿는 순리였고, 그는 이 순리를 무시하는 존재를 딱 한 명 알고 있었다.

‘이공자.’

태원진가의 이공자, 진무경. 약관 전에 이미 절정의 경지에 오른 그야말로 순리를 거스르는 천재였다.

‘혹시 삼공자가…….’

위팽의 생각은 더 이어지지 못했다. 주변에서 소란이 일었기 때문이었다.

“이 비무는 무효요!”

“당장 비무를 멈춰라!”

“태원진가에서 더러운 술수를 부렸다!”

“맞다! 그렇지 않고서야 우리 공자님이 저런 쓰레기에게……”

방금까지만 해도 낄낄거리던 항산검문의 무사들이 검자루에 손을 올리고 있었다.

‘저런 미친놈들을 봤나.’

근래에 항산검문의 위세가 대단한 것은 사실이지만 저런 아랫것들까지 행패를 부리다니.

도저히 참지 못한 위팽이 나서려던 순간이었다.

쉬익- 빡!

바람이 불었고, 십여 개의 이빨이 하늘을 날았다.

입가로 피를 철철 흘리는 항산검문의 무사가 멍한 얼굴로 자신에게 드리워진 거대한 그림자를 올려봤다.

“뭔 레기?”

어버. 어버버.

발음도 제대로 못 하는 무사를 가만히 내려다보던 진위경이 솥뚜껑만 한 손바닥으로 무사의 아구창을 갈겼다.

쫙! 후두둑.

따귀 한 대에 남은 이빨들을 모두 뱉어 낸 무사가 정신을 잃고 고꾸라졌다.

얼어붙은 항산검문 측을 뒤로하고, 진위경은 다시 자리로 돌아와 비무 직관을 시작했다.

위팽이 한숨을 내쉬었다.

“문제가 생길 수도 있습…….”

“위팽.”

“예?”

“아무 말도 하지 말게.”

진위경은 반짝거리는 눈으로 자신의 막냇동생을 바라보며 덧붙였다.

“지금이 내 인생 최고의 순간이야.”



* * *



무공을 실전에서 사용해 보는 것은 처음이다. 무공을 익힌 후에는 누군가와 싸울 일도 없었고, 싸우고 싶지도 않았으니까.

‘하지만…….’

항상 생각했다. 만약 적과 마주친다면, 실전에서 무공을 써야 할 순간이 온다면 어떻게 대응할지.

그런 부분에서 수련동에서의 시간은 상당한 의미가 있었다.

퍽!

“크헉!”

창대에 복부를 직격당한 이소군의 허리가 새우처럼 꺾였다.

놈이 들고 있던 대검은 떨어트린 지 오래다. 나는 계속 전진하며 창대를 휘둘렀고, 그때마다 이소군의 비명이 터져 나왔다.

퍽, 퍽, 퍽!

“끄아아악!”

사실 처음에는 당황스러웠다. 내 발차기가 먹혀? 30레벨인 이소군이 14레벨에 불과한 나한테?

그러나 오십 합을 넘게 겨루면서 깨달았다.

‘내가 더 강하다.’

이소군은 분명 강하다. 현실로 치자면 최소 C급 헌터에 버금갈 정도로.

하지만 내가 더 강하다. 미세한 차이지만 분명히 그랬다. 근력, 체력, 민첩.

‘그리고 경험.’

“크아아아!”

이소군이 괴성을 지르며 달려들었다. 빨랐다. 그리고 파괴적이었다. 보보마다 연무장 바닥이 움푹 패고 갈라진다.

‘하지만 요령이 없어.’

이소군은 어리다. 어리다 보니 경험이 적다. 하수를 상대한다면 힘으로 경험을 커버할 수 있겠지만 나는 달랐다.

더 강하고, 경험도 풍부하다.

‘내가 이긴다. 분명히.’

다짐이 아니라 확신이다. 그게 미련 없이 창을 버린 이유였다. 둘 다 무기가 없는 맨몸 간의 격돌. 창을 버리는 내 모습에 이소군의 눈에서 불길이 쏟아졌다.

“나를 얕봤단 말이냐! 감히, 감히!”

분노는 몸을 경직시키고 동작을 단순하게 만든다. 나는 황소처럼 달려드는 이소군의 다리를 걸어 넘어트렸다. 그리고 일어나려는 녀석의 가슴에 올라탔다.

“이게 무슨……!”

당황한 눈동자를 내려다보며 물었다.

“풀 마운트(Full Mount)라고 들어 봤냐?”

대답을 기다리지 않고, 그대로 주먹을 내리꽂았다. 이소군은 필사적으로 고개를 휘저었지만 소용없었다.

퍼퍼퍼퍽!

턱, 뺨, 이마, 코…… 안면의 모든 부위를 가리지 않고 소나기처럼 퍼부었다. 끝없이 몸을 뒤틀고 악을 지르던 이소군도 어느 순간 축 늘어졌다.

‘이 정도면 됐겠지.’

애초에 비무에 임한 목적은 항산검문과의 전쟁 회피다.

이소군이 중상을 입으면 곤란하다. 적당 선에서 멈춰야 했다.

나는 약간의 걱정을 담아 이소군의 어깨를 흔들었다.

“야, 너 괜찮…….”

팍-!

순간 눈앞이 번쩍했다. 약간의 어지러움. 쓰라린 턱에서는 선홍빛 핏방울이 뚝뚝 떨어졌다.

이소군의 주먹이 스친 결과였다.

‘아, 방심했다.’

순간적으로 고개를 젖히지 않았더라면 큰 낭패를 봤을 것이다. 공력이 실려 있던 일격이었다.

“그걸 피했다고?”

그 틈을 타 잽싸게 마운트를 풀고 빠져나온 이소군은 극도로 당황한 얼굴이었다. 하긴. 나 같은, 아니. 진태경 같은 놈한테 이런 수모를 당할 줄은 몰랐을 것이다.

더군다나 회심의 일격까지 무효로 돌아갔으니.

“이럴 리가…… 이럴 리가 없는데.”

홀린 듯이 중얼거리는 이소군에게 친절하게 대답했다.

“원래 살다 보면 별일이 다 있지.”

“도대체 왜! 어떻게! 이런 일이 벌어진단 말이냐. 나는 이소군이다. 항산검문의 이소군이란 말이다!”

이소군은 핏발 선 눈으로 외쳤다.

“십 년을 갈고 닦았다. 한데 왜! 너 같은 놈이. 너처럼 방탕하고 게으른 쓰레기 따위에게 내가!”

비록 게임 속 캐릭터라지만, 이 순간만큼은 이소군의 심정에 공감했다. 그동안의 노력이 배신당하는 기분. 그 허무와 공허.

‘나도 그랬지.’

7년 동안 느꼈다. 그건 시간이 지남에 따라 무뎌질지언정 사라지지는 않는 박탈감이었다. 나는 결국 받아들였었다.

잔인한 현실이다. 이소군을 향해 말했다.

“이제 그만 항복해라. 넌 나보다 약해.”

그 말을 들은 이소군의 눈이 뒤집혔다.

“그 입 닥쳐!”

다음 순간 주변의 공기가 짜르르 울렸다. 남은 힘을 모두 끌어모은 이소군의 신형이 화살처럼 쏘아졌다.

“난 분명히 말했다. 선택은 네가 한 거야.”

“개소리하지 마!”

후웅.

바람이 갈라지는 소리와 함께 녀석의 주먹이 아슬아슬하게 안면을 스쳤다. 단지 그것뿐인데 살이 베이고 핏물이 흘렀다.

지금껏 봤던 어떤 공격보다도 빠르고 강하다.

‘하지만 그건 나도 마찬가지야.’

오른발에 공력을 실어 이소군의 발등을 내려찍었다. 콰직. 뼈가 부러지는 소리와 함께 이소군의 발이 연무장 바닥에 박혀 든다.

“크아아아아!”

비명을 지르는 놈의 얼굴에 정권을 꽂아 넣었다. 코가 부러지고 이빨이 비산한다. 다리가 종아리까지 파묻힌 탓에 몸을 빼지도 못한다.

한 대 더. 더. 더.

퍽. 퍽. 퍽.

가슴. 옆구리. 배. 그리고 마지막.

‘명치.’

뻑!

제대로 들어갔다. 그것도 그냥 주먹이 아니라 공력을 잔뜩 집중시킨 한 방이다. 이소군의 눈동자가 크게 떠졌다.

“크헙.”

놈의 동공이 초점을 잃는다. 힘이 풀린 허리가 뒤로 꺾이고 그대로 쓰러지는 모습이 슬로 모션처럼 눈에 들어왔다.

내 오른발이 녀석의 복부를 향해 내질러지는 모습까지도.

펑!

풍선 터지는 소리와 함께 이소군의 신형이 훨훨 날았다.

모두가 그 장면을 지켜봤다. 진위경, 위팽. 태원진가의 사람들과 항산검문의 무사들. 그리고 나도.

쿠웅.

십여 미터를 날아간 이소군은 혼절했는지 미동도 하지 않았다.

나는 참았던 숨을 내쉬었다. 이소군에게서 내게로 옮겨진 수십 명의 시선을 받으며 우뚝 서 있었다.

“후우, 후우.”

띠링.



- [비무] 퀘스트를 성공적으로 완수하셨습니다!

- 퀘스트 보상이 지급됩니다!

- 칭호, [승부사]를 얻었습니다!

- 경험치와 명성을 얻었습니다!

- 압도적인 성과로 인한 추가 보상이 지급됩니다!

- [진가심법]의 경지가 4성으로 올랐습니다!

- [기감]의 경지가 3성으로 오릅니다. 50레벨까지의 대상을 파악할 수 있습니다.

- 레벨 업!

- 레벨 업!

- 레벨 업!



시스템 알림이 축포처럼 들렸다.



* * *



항산검문이 떠났다. 모두 말을 타고 왔던 탓에 태원진가에서 부상자들을 옮길 마차까지 빌려야 했다.

그런데 이소군은 그렇다 치고, 다른 한 놈은 뭐야?

무슨 일이 있었는지 이빨이 몽땅 날아가고 입에 물린 헝겊은 피로 흥건하다. 세상에, 도대체 어떤 놈이…….

그때 진위경이 근엄한 얼굴로 내 어깨를 두드렸다.

“잘했다. 기대 이상으로 잘해 줬어.”

“아, 예. 감사합…….”

“왜 그러느냐?”

그거야 당신 볼에 튄 핏자국 때문이지.

무슨 이유에선지는 모르지만 그 잠깐 사이에 사람 하나를 병신으로 만들어 놨다.

“그래서, 어떻게 생각하느냐?”

“예? 무슨 말씀이신지?”

“이제 폐관을 끝내는 것에 대해서 말이다. 비록 네 평소 행실이 불량했던 것은 사실이나, 오늘 괄목할 만한 모습을 보여 주었으니 본가의 큰 홍복이다.”

진위경이 주위를 둘러보며 말을 이었다.

“다른 분들은 어떻게 생각하시는지?”

중진들은 떨떠름한 기색이었지만 딱히 반대하는 눈치는 아니었다. 앞서 회의장에서의 시선과 비교하자면 호의적이라고 느낄 정도다.

‘무림인들이라 그런가?’

소설에서 보면 무림은 정의도 정의지만 힘이 우선시되는 곳이던데, 아마 내가 이소군을 꺾은 것이 영향을 준 모양이었다.

“대답을 하셔야지요. 하하하.”

……아니면 진위경 때문일 수도 있고.

입은 웃는데, 눈은 안 웃는다. 볼에 묻은 핏방울까지 더해지니 호러 무비가 따로 없다.

“저는 적극 동의 합니다.”

거기에 위팽의 여론 조작까지 더해지자 하나둘 찬성 의사를 표했다. 무력 시위에 의한 부정 투표를 지켜본 진위경이 만족스럽게 웃었다.



* * *



‘젠장. 젠장. 젠장!’

이소군은 입술을 질끈 깨물었다. 진태경. 그 빌어먹을 놈의 얼굴이 눈앞을 떠나지 않았다.

‘졌다고? 내가 그런 쓰레기한테?’

이번 태원진가 건은 충분한 명분이 있었다.

이 일로 항산검문이 이득을 얻는다면 그걸로 좋고, 거절 시 본격적인 전면전으로 들어갔어도 성공이었다.

진태경. 그놈을 반병신으로 만든다면 산서성 전역에 소문이 퍼졌을 것이다. 태원진가가 항산검문에게 치욕을 당했다고.

그런데 실패했다.

‘이게 도대체.’

어린 시절부터 검을 잡았다. 천재는 아니었지만 범재도 아니었다.

항산검문의 차남. 전도유망한 후기지수. 일류 검객. 늘 선망의 대상이 되었던 자신인데…….

‘빌어먹을!’

오늘 갖고 있던 모든 것들이 박살 났다. 무자비한 진태경의 폭력 앞에서 처음으로 무릎을 꿇고, 정신을 잃었다.

눈을 떴을 때는 이미 마차 안이었다. 이 마차조차도 태원진가의 것이다. 이소군의 눈에서 불길이 쏟아졌다.

‘죽인다. 너는 꼭 내 손으로 죽인다. 진태경!’

차오르는 분을 참지 못해 벽면을 후려치자 마차가 움직임을 멈췄다. 이소군은 거칠게 소리쳤다.

“뭣 하느냐! 꾸물거리지 않고 다시 출발해!”

그 순간, 미간이 따끔했다.

- 출발? 해야지. 하지만 항산검문으로 가는 건 좀 곤란한데.

‘전음?’

누구냐! 이소군은 외쳤지만 소리가 새어 나가지 않았다.

가슴이 답답하고 목이 타는 듯 아프다. 마차가 다시 움직이기 시작했다.

- 이렇게 하자. 우선은 북망산 먼저. 항산검문은 다음에 가는 걸로 하자고.

‘그게 무슨.’

눈 몇 번 깜빡일 만한 시간이었다. 사지가 마비되고 통증은 거세게 타올랐다. 이소군은 덜덜 떨리는 고개를 돌렸다.

복면을 쓴 누군가가 그를 바라보고 있었다.

“그륵, 그르륵.”

웬 놈이냐. 목소리 대신 시커멓게 변색된 핏물만이 흘러넘쳤다. 시야가 흐려지고 소리가 멀어졌다.

‘사, 살려…….’

그게 마지막이었다.

다음 순간 그는 암흑 속으로 곤두박질쳤다.

“잘 가게, 이 소협.”

복면인은 싱긋 웃으며 망자의 미간에 꽂힌 검푸른 대침을 회수했다.
```

## Current accepted English baseline

```markdown
# Chapter 15

Wipeng thought,

*What am I looking at right now?*

Something unbelievable was happening before his eyes. The Third Young Master—of all people, that very Third Young Master—was holding his own against Lee Seogeun.

*Am I hallucinating?*

Who was Lee Seogeun?

He was the Sect Leader’s blood relative, had inherited his martial arts, and was a first-rate swordsman.

When the Third Young Master first accepted Lee Seogeun’s challenge to a duel, Wipeng had inwardly sighed. *What nerve did a guy who had barely escaped third-rate think he had?*

And then what? *Come out? Let’s have a go?*

*Crazy bastard. He’s talking shit.*

Something did seem to have changed lately. Hadn’t he suddenly started using polite speech without fail? Hadn’t he started practicing martial arts until late at night?

Oh, and there was also that bullshit about losing his memory.

At the time, Wipeng had wondered if the man had gone insane. But when he heard today that the Third Young Master had laid a hand on the Mount Heng Sword Sect’s cherished jewel, it dawned on him. He had nearly died of shock right then and there.

*Of course. A human being can’t change overnight.*

Wipeng had served in the Jin Family of Taiyuan for more than ten years. In his eyes, Jin Taekyung was past a bad seed with yellow sprouts—he was practically gold.[^1]

But what could he do? Taekyung was his lord’s beloved youngest brother and a direct-line member of the Jin Family. Wipeng had been planning to rescue him before Lee Seogeun turned him into a half-cripple.

And yet…

Whack! Whack! Whack!

Now Taekyung was beating Lee Seogeun without mercy.

Jin Taekyung.

Wipeng knew the martial arts he was using: the Jin Family’s Manoeuvre Technique and Spear Technique.

He was fairly skilled at linking the two techniques together, and there was even a seasoned air to his movements—the hard-won experience of a wandering martial artist who had spent around ten years roughing it in back alleys.

*What in the world…?*

No one could master martial arts in a day or two.

That was the natural order Wipeng believed in, and he knew exactly one person who defied it.

*The Second Young Master.*

Jin Mukyung, the Second Young Master of the Jin Family of Taiyuan. A genius who had reached the Peak realm before the age of twenty—a true prodigy who had gone against the natural order.

*Could the Third Young Master possibly…?*

Wipeng’s thoughts went no further. A commotion had broken out around them.

“This duel is invalid!”

“Stop the duel immediately!”

“The Jin Family of Taiyuan used underhanded tricks!”

“That’s right! Otherwise, how could our Young Master possibly lose to trash like that—”

The Mount Heng Sword Sect warriors who had been snickering moments ago now had their hands on their sword hilts.

*What a bunch of lunatics.*

It was true that the Mount Heng Sword Sect had been riding high lately, but for these underlings to cause such a scene—

Just as Wipeng, unable to tolerate it any longer, was about to step forward—

Whoosh—smack!

The wind blew, and some ten teeth went flying through the air.

A Mount Heng Sword Sect warrior, blood pouring from the corner of his mouth, stared blankly up at the enormous shadow looming over him.

“What trash?”

Buh. Buh-buh.

Jin Wikyung looked down calmly at the warrior, who could no longer get the words out. Then he struck the man across the mouth with a palm as large as a cauldron lid.

Smack! Clatter.

The warrior spat out every tooth he had left, then lost consciousness and collapsed.

Leaving the frozen Mount Heng Sword Sect behind, Jin Wikyung sat back down and resumed watching the duel.

Wipeng sighed.

“There could be a problem…”

“Wipeng.”

“Yes?”

“Don’t say anything.”

Jin Wikyung looked at his youngest brother with shining eyes and added,

“This is the best moment of my life.”

* * *

This was my first time using martial arts in a real fight. After learning martial arts, I hadn’t had any reason to fight anyone—and I hadn’t wanted to fight anyone, either.

*But…*

I had always thought about it. If I ever encountered an enemy, if the moment came when I had to use my martial arts in an actual battle, how would I respond?

In that respect, my time in the training hall had meant a great deal.

Whack!

“Guh!”

Lee Seogeun’s back bent like a shrimp when the shaft of my spear struck him directly in the abdomen.

He had dropped the greatsword in his hands a long time ago. I kept advancing and swinging the shaft, and every time I did, Lee Seogeun’s screams rang out.

Whack! Whack! Whack!

“Gaaaah!”

At first, I had been bewildered. *My kick had worked? Lee Seogeun was Level 30, and I was only Level 14.*

But after exchanging more than fifty blows, I realized the truth.

*I’m stronger.*

Lee Seogeun was definitely strong. If I compared him to Hunters, he was at least equivalent to a C-rank Hunter.

But I was stronger. The difference was slight, but it was undeniable. Strength, Stamina, Agility.

*And experience.*

“Graaah!”

Lee Seogeun charged at me with a roar. He was fast. And destructive. Every step he took left the training-ground floor dented and cracked.

*But he has no finesse.*

Lee Seogeun was young. And because he was young, he lacked experience. Against a weaker opponent, he could make up for that lack with sheer strength. But I was different.

I was stronger, and I had more experience.

*I’m going to win. Without a doubt.*

It wasn’t a decision. It was certainty.

That was why I threw away my spear without hesitation. A clash between two unarmed bodies.

The moment Lee Seogeun saw me discard my weapon, fire poured from his eyes.

“You looked down on me? You dare—how dare you!”

Anger stiffened the body and simplified its movements. I tripped Lee Seogeun’s leg as he charged like a bull and sent him tumbling.

Then I climbed onto his chest as he tried to get up.

“What is this…?”

Looking down at his bewildered eyes, I asked,

“Have you ever heard of full mount?”

I didn’t wait for an answer. I drove my fist straight down.

Lee Seogeun desperately shook his head from side to side, but it did him no good.

Bam-bam-bam-bam!

Chin, cheek, forehead, nose… I rained blows down on every part of his face without discrimination. Lee Seogeun twisted his body endlessly and screamed until, at some point, he went limp.

*This should be enough.*

My original purpose in accepting the duel was to avoid war with the Mount Heng Sword Sect.

It would be a problem if Lee Seogeun suffered serious injuries. I had to stop at a reasonable point.

Concerned, I shook Lee Seogeun by the shoulder.

“Hey, are you oka—”

Smack!

The world flashed before my eyes.

A little dizziness. Drops of bright-red blood dripped from my stinging chin.

The result of Lee Seogeun’s fist grazing me.

*Ah. I let my guard down.*

If I hadn’t instinctively jerked my head back, I would have been in serious trouble. That blow had been imbued with internal energy.

“You dodged that?”

Lee Seogeun quickly broke free of the mount and scrambled away, his face filled with extreme bewilderment.

Of course. He probably hadn’t imagined that a guy like me—no, a guy like Jin Taekyung—would humiliate him like this.

Especially after his decisive strike had been rendered useless.

“This can’t be… This can’t be happening.”

I answered Lee Seogeun, who muttered as if he were bewitched.

“Life’s full of surprises.”

“Why! How! How could this possibly happen? I’m Lee Seogeun. I’m Lee Seogeun of the Mount Heng Sword Sect!”

Lee Seogeun shouted with bloodshot eyes.

“I honed my skills for ten years. So why! Why do I lose to trash like you? To someone as debauched and lazy as you!”

Although he was only a game character, for that moment I could sympathize with Lee Seogeun’s feelings. The sensation of having all his efforts betray him. The futility and emptiness.

*I felt that way, too.*

I had felt it for seven years. It had dulled with time, but the sense of deprivation had never disappeared. In the end, I had accepted it.

Reality was cruel.

I spoke to Lee Seogeun.

“Give up now. You’re weaker than me.”

Those words made Lee Seogeun’s eyes go wild with rage.

“Shut your mouth!”

The air around us crackled.

Lee Seogeun gathered every last bit of strength he had left, then shot forward like an arrow.

“I told you clearly. You made your choice.”

“Stop spouting bullshit!”

Whoosh.

With the sound of air splitting apart, his fist grazed my face by a hair. That alone sliced my skin and drew blood.

It was faster and stronger than any attack I had seen from him so far.

*But the same goes for me.*

I channeled internal energy into my right foot and brought it down on the top of Lee Seogeun’s foot.

Crack!

With the sound of breaking bone, his foot slammed into the training-ground floor and sank into it.

“Graaah!”

I drove my knuckles into his screaming face. His nose broke, and teeth scattered through the air. With his leg buried up to the calf, he couldn’t even pull himself free.

One more.

More.

More.

Whack. Whack. Whack.

Chest. Side. Stomach.

And finally—

*The solar plexus.*

Thump!

It landed cleanly. And it wasn’t merely a punch. It was a single blow with a tremendous concentration of internal energy behind it.

Lee Seogeun’s eyes widened.

“Guh!”

His pupils lost focus. His strength left him, his back bent backward, and he collapsed. I watched the motion as if it were happening in slow motion.

I even saw my right foot shoot toward his abdomen.

Pop!

With a sound like a balloon bursting, Lee Seogeun’s body went flying through the air.

Everyone watched it happen. Jin Wikyung, Wipeng, the people of the Jin Family of Taiyuan, and the warriors of the Mount Heng Sword Sect.

And me, too.

Thud.

Lee Seogeun flew more than ten meters before landing. Whether he had passed out or not, he did not move.

I let out the breath I had been holding and stood tall beneath the dozens of gazes that had shifted from Lee Seogeun to me.

“Whoo. Whoo.”

Ding.

> **System**
>
> - The **Duel** Quest has been successfully completed!
>
> - Quest rewards will be distributed!
>
> - You have acquired the Title **Gambler**!
>
> - You have gained EXP and Fame!
>
> - An additional reward has been granted for your overwhelming performance!
>
> - **Jin Family’s Cultivation Technique** has risen to the Fourth Stage!
>
> - **Qi Sense** has risen to the Third Stage. You can now detect targets up to Level 50.
>
> - Level up!
>
> - Level up!
>
> - Level up!

The System notifications sounded like celebratory fireworks.

* * *

The Mount Heng Sword Sect left.

Since they had all arrived on horseback, the Jin Family of Taiyuan even had to lend them a carriage to transport the injured.

But Lee Seogeun was one thing. Who was the other guy?

All his teeth were gone, and the cloth stuffed into his mouth was soaked with blood. Good Lord. What kind of bastard had—

Jin Wikyung patted me on the shoulder with a solemn expression.

“Well done. You performed better than I expected.”

“Ah, yes. Thank you—”

“Why are you looking at me like that?”

*Because there’s blood splattered on your cheek.*

I had no idea why, but somehow he had turned a person into a cripple in that brief span of time.

“So, what do you think?”

“Pardon? What do you mean?”

“About ending your confinement. It is true that your usual conduct has been disgraceful, but after the remarkable performance you showed today, this is a great blessing for our family.”

Jin Wikyung looked around as he continued.

“What do the rest of you think?”

The senior members looked displeased, but none seemed particularly inclined to object. Compared to the looks they had given me in the meeting hall earlier, I almost felt that they were favorable.

*Is it because they’re Murim people?*

In the novels, Murim was a place where justice mattered, but strength came first. Maybe defeating Lee Seogeun had influenced them.

“You should answer him. Hahaha.”

…Or maybe it was because of Jin Wikyung.

His mouth was smiling, but his eyes were not. With the blood on his cheek, he looked like something out of a horror movie.

“I wholeheartedly agree.”

Once Wipeng’s manipulation of public opinion was added to the mix, one by one, the others voiced their agreement.

Jin Wikyung watched the coerced vote, produced by a show of force, and smiled in satisfaction.

* * *

*Damn it. Damn it. Damn it!*

Lee Seogeun bit down hard on his lip. Jin Taekyung’s face refused to leave his mind.

*I lost? To trash like him?*

The Jin Family of Taiyuan incident had given him more than enough justification.

If the Mount Heng Sword Sect gained something from the matter, that would be enough. And if the Jin Family refused, escalating into a full-scale war would also have been a success.

If he turned Jin Taekyung into a half-cripple, word would have spread throughout Shanxi. The Jin Family of Taiyuan had suffered humiliation at the hands of the Mount Heng Sword Sect.

But he had failed.

*How could this have happened?*

He had taken up a sword as a child. He wasn’t a genius, but he wasn’t ordinary, either.

The second son of the Mount Heng Sword Sect. A promising young martial artist. A first-rate swordsman. He had always been the object of admiration…

*Damn it!*

Everything he had possessed had been smashed to pieces today. For the first time, he had been forced to kneel before Jin Taekyung’s merciless violence—and he had lost consciousness.

When he opened his eyes, he was already inside a carriage.

Even this carriage belonged to the Jin Family of Taiyuan.

Fire poured from Lee Seogeun’s eyes.

*I’ll kill you. I’ll kill you with my own hands, Jin Taekyung!*

Unable to contain his rising fury, he slammed his fist into the carriage wall.

The carriage stopped moving.

Lee Seogeun shouted roughly,

“What are you doing? Don’t dawdle. Get moving again!”

At that moment, his brow prickled.

- We should get moving, yes. But going to the Mount Heng Sword Sect would be a little troublesome.

*Sound Transmission?*

“Who is it!” Lee Seogeun shouted, but no sound escaped his throat.

His chest felt tight, and his throat hurt as if it were on fire. The carriage began moving again.

- Let’s do this. Mount Beimang first. We can go to the Mount Heng Sword Sect after.[^2]

*What does that mean—*

It took only the time it would have taken to blink a few times.

His limbs went numb, and pain flared violently through his body. Lee Seogeun turned his trembling head.

Someone wearing a mask was staring at him.

“Grrk… grrrk.”

*Who are you?*

Instead of a voice, dark, discolored blood poured from his mouth.

His vision blurred. The sounds around him grew distant.

*Sa… save me…*

That was his final thought.

The next moment, he plunged headfirst into darkness.

“Farewell, Young Hero.”

The masked man smiled brightly as he retrieved the large blue-black needle from the dead man’s brow.

[^1]: *Ssaksumyeon norata*—“the sprouts are yellow”—means a hopeless case. The line pushes yellow all the way to gold to make that worse, not to call him born rich.

[^2]: Mount Beimang is a traditional burial ground; “going to Beimang” means dying.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 15`.

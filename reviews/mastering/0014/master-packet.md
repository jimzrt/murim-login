# Master Edit Task — Chapter 14

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
| 철수     | **Cheol Soo**      |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 큰형     | **eldest brother**                           |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 민첩               | **Agility**                    |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 큰형 | kinship | Eldest older brother, not a generic older brother. | |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 5–9

## Plot

Taekyung completes the tutorial, learns that Logout requires First Rate, Lv. 30, and 500 Fame, and is taken to the Medicine King Hall after his fight with Hyuk Mujin. He begins cultivating the Jin Family’s Cultivation Technique, pretends that his memory has not returned, and discovers an unused room filled with martial arts manuals. The System reveals that martial arts occupy ten slots, three of which are already filled. Jin Wikyung and Wipeng catch him practicing footwork at night, but accept his explanation. In Chapter 9, Taekyung sorts the manuals, acquires the Jin Family’s Manoeuvre Technique, completes its achievement, and earns the title Novice Trainee. Seeking a proper place to practice, he asks for an empty room. Jin Wikyung instead orders his indefinite confinement in the training hall as a protective measure against the Elder Council’s coming attack. Wipeng secretly explains the plan through Sound Transmission and promises to release him within seven days; Taekyung negotiates that down to three days before being escorted away.

## Continuity

- Taekyung remains trapped in Murim; Logout and death rules remain unresolved.
- Logout requires First Rate, Lv. 30, and 500 Fame.
- He is practicing the Jin Family’s Cultivation Technique and has acquired the Jin Family’s Manoeuvre Technique; he has also located the Jin Family’s Spear Technique.
- His martial arts interface has ten slots, with three already filled.
- Taekyung continues pretending that his memory has not fully returned.
- Jin Wikyung is the Lesser Family Head and Taekyung’s protective older brother; Wipeng is his capable aide and can use Sound Transmission.
- The Elder Council is preparing to challenge Jin Wikyung’s authority by attacking Taekyung’s conduct.
- Taekyung is being held in the training hall for an indefinite period, with Wipeng promising release within three days after their negotiation.

## Translation Decisions

- The hereditary martial art is rendered **Jin Family’s Manoeuvre Technique**, using British spelling consistently with the chapter’s terminology.
- The achievement reward is rendered as the title **Novice Trainee**.
- `음성 전송` is rendered **Sound Transmission**.
- `소가주` is rendered **Lesser Family Head**.
- System messages remain grouped into `> **System**` blockquote windows whenever consecutive.

### Prior accepted reading-copy tails

#### Chapter 12 tail (verified mastered)

…
artist ought to use martial arts.* Those were the words he had thrown at me while toying with me last time. He was nothing more than an illusion I had created, but… *God, that’s pissing me off.* *If you’re so confident, stop dodging and come at me.* Hyuk Mujin picked up on my thought and rushed at me in a smooth glide. But this was a fight between a spear and a fist. If I let him land that attack, it would mean I’d wasted the last seven years. “Not so fast!” Whoom— I swung the spear shaft. If he had been real instead of an illusion, it would have made a solid *thwack*. Even if he had dodged it, he would have failed to close the distance. *Let’s see how far you can dodge.* The second form began. Faced with the torrent of attacks, Hyuk Mujin didn’t even dare approach. He retreated step by step. Combat had a flow. I had caught that flow, and Hyuk Mujin had been swept along by it. Looking at Hyuk Mujin rolling across the ground with an exhausted expression, I thought, *He’s weak.* I could see his movements. The Hyuk Mujin projected here was a fist fighter. By watching his feet, I could tell how he would move and predict what he would do next. His fists couldn’t reach me. Ssshk-swish-swish! In a single instant, I thrust three times in succession. It was an attack F-rank Hunter Jin Taekyung couldn’t perform. But Jin Taekyung the Murim martial artist, drawing on internal energy, could. “Kraaagh!” Hyuk Mujin seemed to scream as the spear pierced his chest. Without hesitation, I shoved the spear deeper and twisted it. The spearhead crushed through his breastbone and split his heart. The fallen Hyuk Mujin slowly faded away. “Ah. This is way too easy.” The fight had already been decided in less than five seconds. I had even held the upper hand throughout the entire battle, only for it to end anticlimactically. *Was half just too weak?* I sank into thought as I circulated my qi to recover the internal energy I had depleted. Hyuk Mujin was Level 20 and a martial artist who had trained in martial arts for at least several years. There was no way he could be this weak. *All right. Again.* I stood up with the spear in my hand and closed my eyes, imagining a new Hyuk Mujin. A height of 180 centimeters. Lean muscles and insolent eyes. I fed in the movements I had seen back then. When I opened my eyes, an illusion exactly as I had imagined stood before me. But I wasn’t finished. Hyuk Mujin needed to be stronger. *Your physical abilities are superior to mine.* After I fed in a few more conditions, Hyuk Mujin’s illusion smiled pleasantly. He had become much faster and gained stamina that would never run out. “Yeah. Now this is worth fighting.” Those words were the starting signal. As Hyuk Mujin charged at me like a streak of light, I thrust my spear. Ssshk-swish! * * * Vroooom. Boom! The spearhead tore through the air. The air burst with the drone of a swarm of bees, stirring up a gust of wind. It was the final form of the Jin Family’s Spear Technique: Sky-Piercing Strike. “Kheugh…” Hyuk Mujin’s illusion looked down at the gaping hole in his chest, disbelief filling his eyes. Then his knees buckled, and the illusion scattered. “This isn’t right.” I scratched my head roughly as I heard the message that my Mastery of the Jin Family’s Spear Technique had increased. *Why am I still winning?* Had the System made a mistake, or… *Did I just get stronger?* I brushed the thought away as soon as it came to me. That couldn’t be it. I wasn’t some peerless genius. I had only learned a couple of martial arts. *At this rate, it isn’t much use.* This was supposed to be a simulation to test what would happen if I faced a powerful opponent. What was the point if I kept winning? If I at least knew which martial arts Hyuk Mujin had learned, I could draw out their power. But wait. “There’s an easier way.” The Jin Family’s Manoeuvre Technique and Spear Technique. What if I grafted those two onto the Level 20 Hyuk Mujin? I might even be able to identify their strengths and weaknesses from a third-party perspective. Yeah. That would be better. “You think so too, right?” At some point, Hyuk Mujin’s illusion had reappeared. He grinned and nodded. “Then let’s fight again.” I raised the spear diagonally and took one step forward with my left foot. Like a mirror, the illusion assumed the same stance. “You’ll regret this.” “Regret, my ass.” Now I was even talking to an illusion. If anyone saw me, there would be no convincing them I wasn’t completely insane. “Crazy bastard.” …It was my imagination, but it still pissed me off. “You’re dead.” Without hesitation, I pointed my spear at him. The same weapon. The same martial arts. This looked like it would be an interesting fight. “Interesting? You really are a lunatic.” Yeah. I suppose so. Finding this fun in a situation like this meant I was pretty damn crazy, too. [^1]: A goshiwon is inexpensive lodging made up of tiny private rooms, often rented by students preparing for major exams.

#### Chapter 13 tail (verified mastered)

…
Yet right now, they were united in glaring at me. “Fuck…” Wipeng turned his head at my mutter. “The Lesser Family Head believes in you. Don’t forget that.” Right. Jin Wikyung was there. My greatest hope and my shield. As I reminded myself of that fact, Wipeng threw open the doors to the main assembly hall. “I’ve brought the Third Young Master.” I took a deep breath and stepped into the pavilion, repeating the same words over and over in my head. *Even if a tiger carries you off, you can survive as long as you keep your wits about you. Even if a tiger carries you off, as long as you keep your wits…* The moment I entered the hall, the low murmurs abruptly stopped. A dozen men, young and old, stood arrayed along either side, while Jin Wikyung occupied the seat of honor. And in the center stood a young man. “It’s been a while, Young Master Jin.” The instant I met that unpleasant smile— Ding. > **System** > > - **Killing intent** detected! …At least use your blinker before pulling in. * * * Killing intent. I knew it well. Monsters were literally bundles of malice and killing intent. I had felt it countless times and thought I had grown used to it. But this guy… *He was different.* This was on an entirely different level from anything I had experienced. If I had to compare it, it was like the difference between a low-level monster and a mid-level monster. His killing intent was far more refined, more furtive, and more chilling. “I caught a glimpse of you in the marketplace last time. I don’t know whether you remember me.” Lee Seogeun spat out each word. A System window floated in the air above his head. > **System** > > **Lv. 30 Lee Seogeun** That was the Level I had read with Qi Sense the instant I detected his killing intent. It was more than twice my Level. *This is insane.* Even worse were the looks from everyone else. Dozens of sinister gazes, young and old alike, were fixed on me. My knees began to tremble. In that atmosphere, Lee Seogeun opened his mouth. “What a shame. If you had come a little earlier, we could have had a deeper conversation. We were discussing something interesting until just now.” “…Were you?” “Aren’t you curious what we were discussing?” “N-no, I’m fine.” I could only hope it hadn’t been a discussion about whether to cut off my head or my balls. And if that miserable guess was correct, I would rather they cut off my balls than my head. *If I’m lucky, a Level Up might heal them… Why the hell do I even have to think about this?* It was simply miserable. Lee Seogeun studied my expression before speaking again. “I heard you returned to the family a few days ago. Where were you?” “Honghwaru.” “Then where were you before you went to Honghwaru?” *I was at a goshiwon, you bastard.* I wanted to tell him everything honestly. *I got fired from my Guild that day, had a glass of soju with the hyung from the goshiwon, then went into the capsule and fell asleep. When I opened my eyes, I was at Honghwaru, and now I’m working hard toward Logout. Something like that.* *I’d be lucky if he didn’t draw his sword.* As I hesitated, unable to answer, Lee Seogeun pulled something from inside his robes. I thought he really was drawing a sword, but it turned out to be a bundle of papers. “Since you don’t seem to remember, I’ll tell you. The night before you went to Honghwaru, you visited Myeongwollu. You went to the deluxe room you had reserved.” “Myeongwollu?” “The pleasure house you used to visit all the time? Don’t try to make excuses by saying you’ve never heard of it. These are the testimonies and signatures of the people who saw you there that day.” In other words, it was a list of witness statements. I read through the papers, thinking I might as well take a look. Then I noticed something strange. “What is this?” “You don’t know even after seeing it yourself?” This bastard was casually dropping the formal speech now. “I’m saying that because I read it. There isn’t a single proper testimony here.” I read every one of the dozens of statements, but there wasn’t a decisive testimony anywhere. They all said roughly the same thing. Jin Taekyung had gotten thoroughly drunk and gone to the wrong room. That room belonged to a daughter of the Mount Heng Sword Sect. Then someone heard screaming. “The bastard who tore my sister’s clothes and tried to rape her is shameless beyond belief. You really are exactly as the rumors say.” “No, that’s not what—” “You bastard!” Flutter! “Ah.” The bundle of papers smacked me in the face and scattered across the floor. Lee Seogeun spat a wad of phlegm onto them. *Well, look at this asshole.* I wasn’t annoyed. Just suspicious. How should I put it? This whole chain of events—especially the testimonies—felt incredibly contrived. But I had no time to dwell on that unease. “Come out with me, you bastard! I’ll make you pay for what you’ve done!” The instant Lee Seogeun shouted— Ding. > **System** > > - A **Duel** Quest has been generated. What’s this now?

## Korean source

```text
＃14화



“따라 나와라, 네놈이 저지른 짓의 대가를 치르게 해 주마!”

이소군이 분노에 가득 찬 고함을 내지른 그 순간이었다.

띠링.



퀘스트



[비무]

당신의 방탕함이 드디어 일을 냈습니다!

자신의 일은 스스로 해결해야 하는 법. 쥐꼬리만큼 남은 명예와 항산검문의 분노를 피하기 위해서 남은 방법은 하나뿐입니다.



종류 : 돌발 퀘스트

등급 : 일류

제한 : 진태경

임무 : 비무에서 승리 (미완료)

보상 : 칭호, [승부사]

 대량의 경험치

 명성 50

실패 : 칭호, [색마]

 부상



[비무] 퀘스트를 수락하시겠습니까?

수락    /    거절



“…….”

아니, 고등학교 이후로 연애도 해 본 적 없는 내가 색마 소리까지 들어야 하나?

하루 절반을 레이드 뛰고 고시원에서 쓰러져 자는 게 일상인데 이제는 게임에서 내가 싸지도 않은 똥을 치워야 한다.

‘퀘스트나 좀 잘 주든가.’

30레벨인 이소군을 무슨 수로 상대하란 말인가.

‘이런 미친, 레벨 차이가 두 배가 넘어가는데…….’

이건 절대 하면 안 되는 싸움이다.

나는 퀘스트를 거절했다. 아니, 거절하려고 했다. 하지만 이소군이 한발 빨랐다.

“만약 이 자리에서 도망친다면…… 태원진가는 합당한 대가를 치르게 될 것이다.”

띠링.



- 퀘스트 정보가 갱신되었습니다.

- 퀘스트 거부 시, [항산검문]이 [태원진가]에 선전포고합니다. 또한 [진태경]을 문파 공적으로 지목합니다.



……내 이럴 줄 알았다. 웬일로 선택권을 주나 했지.

내가 한숨을 푹 내쉴 때, 회의장은 숯불 위 가마솥처럼 끓어오르는 중이었다.

“무례하다!”

“어린놈이 가문의 위세를 업고 못 하는 말이 없구나!”

“아무리 삼공자가 개만도 못한 짓을 했어도 그렇지, 본가를 업신여기다니!”

“…….”

다 좋은데 마지막 누구냐.

분위기가 험악해지자 소가주인 진위경이 나섰다.

“모두 진정하시지요. 이 소협도 그만하게. 이번 한 번은 말실수로 생각하고 넘어가지.”

가장 상석에 앉아 낮은 목소리로 경고하는데, 포스가 장난이 아니다. 뿌리 있는 명문가의 차기 가주답다고나 할까.

이소군도 기세에 눌렸는지 확연히 줄어든 목소리로 대답했다.

“알겠습니다. 하지만…….”

“하지만?”

“말실수가 아닙니다. 제가 개인의 자격으로 오늘 이 자리에 왔다고 생각하십니까?”

그 말에 진위경은 물론이고 사람들의 안색이 굳어진다.

맞다. 이소군은 항산검문이 정식으로 보낸 사자(使者)다.

“아버님, 아니 문주께서 제게 모든 권한을 일임하셨습니다.”

“……그래서 원하는 게 뭔가?”

“이미 말씀드렸다시피 삼공자와의 비무를 원합니다.”

아니. 그건 내가 싫은데.

돌아가는 상황을 보아하니 항산검문 이 자식들, 작정하고 시비 털러 온 거다.

이 일로 얻을 수 있는 건 최대한 얻고, 그게 실패하더라도 나 하나 정도는 작살내 버리겠다는 것 같은데…… 이렇게 노골적으로 저격당하니 등골이 서늘하다.

“다른 길도 있겠지. 정말 원하는 걸 말해 보게.”

“태원을 제외한 모든 군현(郡縣)에서 철수. 이 정도면 제 누이의 혼삿길을 막은 대가로 적절하지요.”

말이 끝나기가 무섭게 회의장에 고함이 빗발쳤다.

드문드문 들리는 말로는, 한마디로 속옷 빼고 다 벗겨 먹겠다는 소리였다. 소가주인 진위경의 선택은 보나 마나다.

“불가.”

“하면 비무를…….”

“그 또한 거절하겠네.”

막냇동생에게는 껌뻑 죽는 진위경이다. 척 봐도 위험한 비무에 나를 밀어 넣을 리 없었다.

진위경의 대답에 이소군은 득의양양한 미소를 지어 보였다.

“그럼 남은 길은 하나뿐이군요.”

전쟁.

그 단어를 떠올린 것은 나뿐만이 아니었다. 전쟁이 주는 무게감에 회의장은 침묵에 휩싸였다.

그 침묵 사이에서, 나는 허공을 바라봤다.



퀘스트를 수락하시겠습니까?

수락    /    거절



- 퀘스트 거절 시, [항산검문]이 [태원진가]에 선전포고합니다. 또한 [진태경]을 문파 공적으로 지목합니다.



시스템 메시지 읽고, 땅 보고. 하늘 보고. 그리고 다시 읽고.

‘씨바…….’

어쩔 수 없다. 방법은 하나뿐이다.

“하겠습니다.”

이번만큼은 모든 이들의 반응이 일치했다. 부릅뜬 눈, 벌어진 입. 비무를 제안한 이소군, 거절한 진위경. 회의실 모두가 자신의 귀를 의심하고 있었다.

“자, 잠깐만. 태경아?”

황급히 만류하려는 진위경을 뒤로하고, 이소군에게 말했다.

“나와. 한판 붙자.”

이소군의 입꼬리가 잔인하게 올라갔다.



* * *



겨울바람이 차갑다. 구름 낀 하늘을 바라보며 심호흡했다.

“후우.”

이소군과 마주 선 이곳은 태원진가의 대연무장이다. 멀찍이 떨어진 오십여 명의 사람들은 자리에 앉아 우리를 바라보고 있었다.

태원진가 사람들은 저 새끼가 뭘 잘못 먹었나, 하는 얼굴이고, 항산검문 똘마니들은 손에 팝콘만 없지 아주 놀러 온 모양새다.

아. 전음을 보내는 사람도 있다.

- 막내야. 심호흡해. 심호흡. 후. 하. 후. 하…….

하고 있어. 이 양반아.

근엄한 얼굴을 하고선 똥 마려운 강아지처럼 엉덩이를 들썩거린다. 위팽이 어깨를 누르고 있지 않았다면 당장이라도 난입했을 기세다.

- 걱정 마라. 위험하다 싶으면 이 큰형님이. 막. 어? 저놈이 우리 막내한테 손만 댔다 하면 콱, 씨! 어? 알겠지? 흥분하지 말고 천천히, 안전하게. 할 수 있다. 진태경!

……알겠으니까 진정 좀.

아까 회의장에서는 포스가 철철 흘러넘치더니, 역시 기대를 저버리지 않는 진위경이다.

‘그래도 없는 것보다는 백배 낫지.’

최소한 반병신이 되기 전에는 구해 줄 사람이 있으니까.

진위경에 위팽까지 하면 생명 보험이 두 개다. 좋아.

그렇게 한결 가벼워진 마음으로 이소군을 바라봤을 때, 나는 곧바로 생각을 철회했다.

‘좋긴 뭐가 좋아. 시발.’

항산검문 놈들이 왜 그렇게 자신만만했는지 알겠다.

난데없이 상의를 훌렁훌렁 벗어 던지는데, 연체동물처럼 꿈틀거리는 근육에 숨이 턱 막히고…….



[Lv.30 이소군]



피처럼 붉은 레벨창에 손발이 저려 온다.

자그마치 16레벨 차이. 압도적이다. 그 사실을 알려 주듯이 시스템창이 울렸다.



- 상태 이상 [위축]에 걸렸습니다!



‘누가 구해 주기 전에 세 번은 죽겠다.’

이런 내 반응을 눈치챘는지 이소군이 잔인한 미소를 지어 보였다.

“이제 상황 파악이 되나? 숨이 턱 막히고 손발이 저려 오지?”

이제는 관심법까지 쓰네. 하지만 싸움은 기세가 반이다.

나는 짐짓 표정을 가다듬고 대답했다.

“헛소리.”

“목소리가 떨리는군. 당연히 겁먹었겠지. 좋아, 내가 하는 질문에 성실하게 답변한다면 살살 해 주마.”

……솔직히 살짝 흔들릴 뻔했다.

“헛소리는 집어치워.”

“오, 주제에 무가의 자제라 이건가?”

이소군이 가소롭다는 듯이 웃었다.

“하나만 묻자. 무슨 자신감으로 비무를 받아들였나? 무공도 보잘것없고 겁쟁이로 소문난 네놈이. 그 이유가 듣고 싶다.”

“이유?”

아무리 생각해도 방법은 이것 하나뿐이었다. 전쟁이 일어나면 나는 항산검문의 문파 공적이 된다.

사냥? 레벨 업? 꿈도 못 꾼다. 태원진가라는 울타리를 벗어난 순간 냄새를 맡은 암살자들이 득달같이 달려들 거다.

‘목숨이라도 붙어 있으면 다음 기회가 있다.’

내게는 마법이 있다. 레벨 업이라는 회복 마법이.

마음이 조금 편안해졌다.

“너 정도면 해 볼 만한 것 같아서.”

“푸핫! 하룻강아지 같은 놈.”

가벼운 도발인데 역시 먹히지 않는다. 본인의 실력에 자신이 있는지 여유가 제법이다.

“이제 내가 질문할 차롄가?”

“대답해 준다는 말은 없었는데…… 유언인 셈 치고 들어 주마.”

“이번 일. 너희들이 조작한 거지?”

예상치 못한 질문이었는지 이소군의 얼굴이 어색하게 굳어졌다.

그 표정이 내게는 충분한 대답이었다.

‘맞네.’

혹시나 했는데, 역시다. 어쩐지 처음부터 끝까지 구린내가 진동을 하더라.

“어이구, 이 치졸한 새끼들. 차라리 선전포고를 하지.”

“……그 아가리를 찢어 주마.”

이소군이 거대한 대검을 들어 보이며 음산하게 중얼거렸다.

나도 미리 꺼내 둔 [예리한 창]을 곧추세웠다.

‘그래, 해 보자.’

나도 무공을 익혔다. 7년간 실전으로 다져진 감각도 있다.

F급 헌터 겸 이류 무림인. 투잡으로 갈고닦은 실력을 무시하지 마라!

“크아아아압!”

이소군은 상상 이상으로 민첩했다. 순식간에 거리를 좁히고 수직으로 내리꽂히는 대검을 창대로 막아 냈다.

카가가각.

“큭.”

그대로 양단되면 어쩌나 했는데, 예리한 창은 통짜 강철답게 튼튼했다. 그러나 대검에 실린 힘에 의해 두 발이 땅을 파고들기 시작했다.

“죽어라, 이 벌레 같은 놈!”

“흡!”

가까이서 마주하니 더욱 숨 막히는 기세다. 몬스터의 피어(Fear)가 이럴까.

“지금이라도 무릎을 꿇고 용서를 빌어라! 그럼 팔 하나 정도로 끝내 주지!”

- 막내야!

이소군의 어깨 너머로 벌떡 일어난 진위경이 보인다. 항산검문 놈들은 킬킬거리며 지켜보고, 태원진가 사람들은 차마 못 보겠다는 듯 고개를 돌리고 있다.

‘버텨야 해.’

적어도 진위경이 올 때까지만이라도!

“크아압!”

종횡무진. 사방에서 이소군의 대검이 연달아 작렬했다. 분명 철끼리 부딪치는데, 내 귀에는 대포 소리가 들린다.

쾅! 쾅! 쾅! 막았다.

“크아아!”

“하압!”

쾅! 쾅! 다시 막았다.

“크아아아!”

“하아아압!”

쾅! 또 막았다.

“크아아압…….”

“하아앗…….”

“……?”

“……?”

다음 순간, 이소군과 시선이 부딪쳤다.

그 얼떨떨하고 당황해하는 눈빛을 보는 순간, 녀석이 나와 똑같은 생각을 하고 있음을 알 수 있었다.

‘뭐여, 이게.’

이소군은 강하다. 대형 몬스터를 연상시키는 괴력에, 근육에 맞지 않게 민첩하며, 무지막지한 대검을 성냥개비처럼 휘두른다.

그뿐인가, 방귀 좀 뀐다는 항산검문의 자제다. 펼치는 무공도 제법 높은 수준일 것이다.

그런데…….

‘할 만한데?’

나는 지금도 끊임없이 휘둘러지는 대검을 하나하나 막아 내고 있었다. 20회가 넘어가는 공격. 그리고 방어.

보인다. 보여서 막을 수 있는 거다. 어느새 발목까지 파묻힌 다리를 슬며시 들어 보였다. 쑥 뽑힌다.

‘이거 혹시…….’

에이, 설마. 아니겠지.

쐐액-!

그 순간, 허리를 노리고 날아든 대검을 창간으로 흘렸다. 그리고 나도 모르게 순간적으로 텅 빈 이소군의 가슴을 걷어찼다.

빠악!

“컥!”

……응?

주르륵, 복부를 부여잡고 대여섯 발자국을 밀려난 이소군이 아무 일도 없었다는 듯 콧잔등을 슥 문질렀다.

“제법이군. 쓰레기답지 않게 한 수 재간은 있어.”

“…….”

“후후. 양보도 여기까지다.”

“……야.”

“다음 일격에 네놈의 머리통을…… 왜?”

나는 떨떠름한 얼굴로 손을 들어 녀석의 입을 가리켰다.

“너, 피 나.”

주륵. 한 박자 늦게 피 한 줄기가 이소군의 입가를 타고 흐른다. 저거 아무래도 혀 깨물었나 본데. 아프겠다.

“앗! 잉! 엑! 훅!”

뭔 개 같은 추임새를 넣으며 피를 닦아 내는 이소군에게, 내가 말했다.

“닦지 마. 놔둬.”

“……?”

“이따 한 번에 닦는 게 편해.”

왜냐하면 지금부터 나한테 존나 맞아야 하거든.



- 상태 이상, [위축]이 해제됩니다!
```

## Current accepted English baseline

```markdown
# Chapter 14

“Come out with me, you bastard! I’ll make you pay for what you’ve done!”

The instant Lee Seogeun shouted those words, filled with fury—

Ding.

> **System**
>
> **Quest**
>
> **Duel**
>
> Your debauchery has finally caught up with you!
>
> A man must deal with his own mess. To protect the tiny scrap of honor you have left and to avoid the anger of the Mount Heng Sword Sect, only one option remains.
>
> **Type:** Sudden Quest  
> **Grade:** First Rate  
> **Restriction:** Jin Taekyung  
> **Mission:** Win the duel (Incomplete)
>
> **Reward:** Title: **Gambler**
>
> - A large amount of EXP
> - Fame 50
>
> **Failure:** Title: **Sex Fiend**
>
> - Injury
>
> Would you like to accept the **Duel** Quest?
>
> **Accept** / **Decline**

“……”

Seriously? I hadn’t even dated anyone since high school, and I had to be called a sex fiend?

I spent half my day on raids and collapsed asleep in my goshiwon every night. Now I had to clean up a mess I hadn’t even made in a game.

*At least give me a decent Quest.*

How was I supposed to fight a Level 30 like Lee Seogeun?

*This is insane. The Level gap is more than twice mine…*

This was a fight I couldn’t possibly take.

I declined the Quest. Or I was going to. But Lee Seogeun beat me to it.

“If you run away from this place… the Jin Family of Taiyuan will pay the appropriate price.”

Ding.

> **System**
>
> - Quest information has been updated.
>
> - If the Quest is declined, the **Mount Heng Sword Sect** will declare war on the **Jin Family of Taiyuan**. In addition, **Jin Taekyung** will be designated a public enemy of the sect.

*…I knew it.*

I had wondered why the System was giving me a choice for once.

As I let out a deep sigh, the assembly hall was boiling like a cauldron over charcoal.

“How dare you!”

“That young punk thinks he can say anything because he has his family’s backing!”

“Even if the Third Young Master did something lower than a dog, how dare he look down on our family!”

“……”

The first two were fine, but who the hell was that last guy?

As the atmosphere turned hostile, Jin Wikyung, the Lesser Family Head, stepped forward.

“Everyone, calm yourselves. And you, Young Hero, enough. Let us consider this a verbal slip and let it go this once.”

Seated in the place of honor, he issued the warning in a low voice. His presence was no joke. He really did have the bearing of the next Family Head of a prestigious house with deep roots.

Perhaps cowed by that aura, Lee Seogeun answered in a noticeably quieter voice.

“Understood. However…”

“However?”

“It was not a verbal slip. Do you think I came here as a private individual?”

At those words, Jin Wikyung’s expression hardened, and so did everyone else’s.

Right. Lee Seogeun was an envoy officially sent by the Mount Heng Sword Sect.

“My father—no, the Sect Leader—has entrusted me with all authority.”

“……Then what is it you want?”

“As I already said, I want a duel with the Third Young Master.”

*No. I don’t want that.*

Judging by how things were unfolding, those bastards from the Mount Heng Sword Sect had come here looking for a fight.

They intended to get as much as possible out of this incident, and even if that failed, they were going to wreck me, at least. Being targeted so blatantly sent a chill down my spine.

“There must be another way. Tell me what you truly want.”

“Withdraw from every commandery and county except Taiyuan. That should be an appropriate price for ruining my sister’s chances of marriage.”

The instant he finished speaking, shouts erupted throughout the assembly hall.

From the bits and pieces I could make out, he was basically saying they intended to strip us of everything but our underwear. Jin Wikyung’s answer was obvious.

“Impossible.”

“Then accept the duel—”

“That too, I must refuse.”

Jin Wikyung was a complete pushover when it came to his youngest brother. There was no way he would push me into a duel that was obviously dangerous.

At Jin Wikyung’s answer, Lee Seogeun smiled triumphantly.

“Then there is only one path left.”

War.

I wasn’t the only one who thought of that word. The assembly hall fell silent beneath the weight of it.

Amid that silence, I looked up at the empty air.

> **System**
>
> Would you like to accept the Quest?
>
> **Accept** / **Decline**
>
> - If the Quest is declined, the **Mount Heng Sword Sect** will declare war on the **Jin Family of Taiyuan**. In addition, **Jin Taekyung** will be designated a public enemy of the sect.

I read the System message, looked at the floor, looked at the ceiling, and then read it again.

*Fuck…*

There was no choice. Only one way remained.

“I’ll do it.”

Everyone reacted the same way this time. Wide eyes. Open mouths. Lee Seogeun, who had proposed the duel. Jin Wikyung, who had refused it. Every person in the assembly hall looked as if they doubted their own ears.

“W-wait. Taekyung?”

I left Jin Wikyung’s frantic attempt to stop me behind me and spoke to Lee Seogeun.

“Come out. Let’s have a go.”

The corners of Lee Seogeun’s mouth rose cruelly.

* * *

The winter wind was cold. I took a deep breath while looking up at the cloudy sky.

“Whoo.”

I faced Lee Seogeun on the Jin Family of Taiyuan’s main training ground. About fifty people sat some distance away, watching us.

The Jin Family people wore expressions that seemed to ask what the hell I had eaten, while the Mount Heng Sword Sect’s goons looked like they had come out for a day of entertainment. The only thing missing was popcorn.

Ah. Someone was sending me Sound Transmission, too.

- Little brother. Deep breaths. Deep breaths. In. Out. In. Out…

*I’m doing it, man.*

Jin Wikyung had a solemn expression, but he kept shifting his hips like a puppy that needed to poop. If Wipeng hadn’t been holding him down by the shoulder, he looked ready to charge into the training ground at any moment.

- Don’t worry. If it looks dangerous, this eldest brother of yours will jump in. What? If that bastard so much as lays a hand on our youngest brother, I’ll—fuck! Got it? Don’t get worked up. Take it slow and stay safe. You can do it, Jin Taekyung!

*……I get it, so calm down.*

He had radiated such overwhelming force in the assembly hall, yet Jin Wikyung was once again living up to my expectations.

*Still, he’s a hundred times better than having no one.*

At least someone would save me before I became a half-crippled wreck.

With Jin Wikyung and Wipeng, I had two life insurance policies. Excellent.

But the moment I looked at Lee Seogeun with that slightly lighter feeling, I withdrew my thoughts.

*What’s so excellent about this? Fuck.*

Now I understood why the Mount Heng Sword Sect’s people had been so confident.

Lee Seogeun suddenly stripped off his upper garments, and my breath caught at the muscles writhing like some kind of mollusk.

> **System**
>
> **Lv. 30 Lee Seogeun**

My hands and feet began to tingle at the sight of the blood-red Level window.

The sixteen-Level gap was overwhelming. As if to drive that fact home, the System rang.

Ding.

> **System**
>
> - You have been afflicted with the Status Effect **Intimidation**!

*I’ll die three times before anyone gets here to save me.*

Perhaps he noticed my reaction, because Lee Seogeun gave me a cruel smile.

“Do you understand the situation now? Your breath is caught, and your hands and feet are tingling, aren’t they?”

He could read minds now, too?

But momentum was half the fight.

I deliberately composed my expression before answering.

“Bullshit.”

“Your voice is trembling. Of course you’re afraid. Fine. If you answer my questions honestly, I’ll go easy on you.”

……To be honest, I almost wavered.

“Cut the bullshit.”

“Oh? Putting on the airs of a martial family’s son, are you?”

Lee Seogeun laughed as if I were ridiculous.

“Let me ask you one thing. What made you accept the duel? You, whose martial arts are pathetic and who is infamous for being a coward. I want to hear the reason.”

“The reason?”

No matter how much I thought about it, this was the only way.

If war broke out, I would become a public enemy of the Mount Heng Sword Sect.

Hunting? Leveling up? I could forget about it. The moment I left the fence of the Jin Family of Taiyuan, assassins who caught my scent would come running.

*As long as I stay alive, there will be another chance.*

I had magic. The recovery magic of leveling up.

My mind eased slightly.

“I thought someone like you might be manageable.”

“Pfft! You’re just a wet-behind-the-ears pup.”

It was a mild provocation, but it didn’t work. He was confident in his own abilities, and it showed in his relaxed manner.

“Is it my turn to ask questions now?”

“I never said I’d answer them… but I’ll indulge you as if they were your last words.”

“This incident. You fabricated it, didn’t you?”

Perhaps the question was unexpected, because Lee Seogeun’s expression stiffened awkwardly.

That expression was answer enough.

*There it is.*

I had wondered if that was the case, but sure enough. No wonder the whole thing had smelled rotten from beginning to end.

“You petty bastards. You should have just declared war.”

“……I’ll tear that mouth apart.”

Lee Seogeun lifted a massive greatsword and muttered ominously.

I raised the Sharp Spear I had drawn earlier.

*All right. Let’s do this.*

I had learned martial arts. I also had instincts honed by seven years of real combat.

An F-rank Hunter and a second-rate Murim martial artist. Don’t underestimate the skills I had honed working two jobs!

“Graaah!”

Lee Seogeun was more agile than I had imagined. He closed the distance in an instant, and I blocked the greatsword crashing down vertically with the shaft of my spear.

Kra-kra-kraang.

“Urgh.”

I had wondered if I would be split in two, but the Sharp Spear was sturdy as a solid piece of steel. However, the force behind the greatsword began driving both my feet into the ground.

“Die, you insect!”

“Hup!”

Up close, his aura was even more suffocating. Was this what a monster’s Fear felt like?

“Kneel and beg for forgiveness now! Then I’ll let you off with one arm!”

- Little brother!

Over Lee Seogeun’s shoulder, I saw Jin Wikyung spring to his feet. The Mount Heng Sword Sect’s people watched while snickering, and the Jin Family people turned their heads away as if they couldn’t bear to watch.

*I have to hold out.*

At least until Jin Wikyung got here!

“Graaah!”

Lee Seogeun’s greatsword struck from every direction in a blurring barrage. The weapons were clearly clashing, iron against iron, but all I could hear was the sound of cannons.

Boom! Boom! Boom! I blocked them.

“Graaah!”

“Hup!”

Boom! Boom! I blocked them again.

“Graaah!”

“Haaah!”

Boom! I blocked another.

“Graaah…”

“Haaah…”

“……?”

“……?”

The next moment, Lee Seogeun and I met each other’s eyes.

The moment I saw the bewilderment and confusion in his gaze, I knew he was thinking exactly what I was.

*What the hell is this?*

Lee Seogeun was strong. He possessed the brute strength of a giant monster, moved with surprising agility for someone with that much muscle, and swung his massive greatsword like a matchstick.

And that wasn’t all. He was a Young Master of the Mount Heng Sword Sect—a sect that could actually throw its weight around. The martial arts he used had to be quite advanced.

And yet…

*This is… doable?*

Even now, I was blocking each and every strike of the continuously swinging greatsword. More than twenty attacks. And more than twenty blocks.

I could see them. That was why I could block them.

I slowly lifted one of my legs, which had been buried in the ground up to the ankle. It came free with ease.

*Could this be…*

No way. Surely not.

Ssshwip!

At that moment, I redirected the greatsword flying toward my waist along the shaft of my spear. Then, without thinking, I kicked Lee Seogeun in his unguarded chest.

Whack!

“Urgh!”

……Huh?

Lee Seogeun slid back five or six steps while clutching his chest. Then he casually rubbed the bridge of his nose as if nothing had happened.

“You’re not bad. You’ve got a trick or two, despite being trash.”

“……”

“Heh. I won’t hold back anymore.”

“……Hey.”

“With my next strike, I’ll smash your head—what?”

With a queasy look, I raised a hand and pointed at his mouth.

“You’re bleeding.”

A beat later, a thin line of blood ran down from the corner of Lee Seogeun’s mouth. He had probably bitten his tongue. That had to hurt.

“Ah! Eeng! Eek! Hup!”

Lee Seogeun wiped away the blood while letting out some ridiculous yelps.

“Don’t wipe it. Leave it.”

“……?”

“It’ll be easier to wipe it all off at once later.”

Because from now on, I was going to beat the absolute shit out of him.

> **System**
>
> - The Status Effect **Intimidation** has been removed!
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 14`.

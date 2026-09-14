# Master Edit Task — Chapter 49

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
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 아이템              | **Item**                       |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 40–44

## Plot

Taekyung wakes in reality after dreaming of the Jin Family’s battle. Seong Jinho cannot see the Ark - 2020 manual’s text, confirming that its contents are visible only to Taekyung. Taekyung tests a popular virtual-reality game, but its artificial NPCs and sensations cannot compare with Murim. After speaking with his sister Hayeon and thinking of his mother, he accepts that he has returned home and decides to live with his family. He discards the capsule and leaves for work; Jinho, still skeptical but curious, begins investigating H Soft.

Taekyung returns to Hunter work after Sopung Guild fires him. His old acquaintance Im Kkeokjeong, now the E-rank Hunter Im Hyeokjun, recommends him to Team Leader Choi of the newly formed Peace Guild. Taekyung joins an E-rank Gate as a porter. Inside, Choi and the veteran Hunters defeat a Hobgoblin group, while Taekyung efficiently processes the corpses.

In the Boss Zone, an old Hobgoblin Priest uses nearly one hundred corpses to restore a stone gate, trap the party, and summon a C-rank Hobgoblin Great Warrior. The Great Warrior overwhelms Im and the other veterans, leaving them unconscious. Taekyung lures it away, then returns to protect them and blocks its greatsword. This triggers Character Synchronization in reality: “Synchronization complete” and “All systems are inherited.” The System identifies the monster as Level 45. Taekyung reverses the fight with his spear. Choi kills the Hobgoblin Priest, then watches in disbelief as the supposedly F-rank porter severely maims the Great Warrior.

## Continuity

- Taekyung is back in reality, officially an F-rank Hunter and working as a porter for Peace Guild.
- Character Synchronization has restored all of Taekyung’s systems in reality, though the consequences and limits of this restoration are unknown.
- Im Kkeokjeong/Im Hyeokjun and the other veteran E-rank Hunters are unconscious but alive in the Boss Zone.
- Team Leader Choi is a C-rank Hunter, Peace Guild’s leader for this raid, and an equipment-focused fighter who uses a sword and wind-based Haste magic.
- Peace Guild is newly formed and has only three members, including its Guild Master.
- The Hobgoblin Priest is dead. The Level 45 Hobgoblin Great Warrior has been severely wounded, but its final fate and whether Taekyung can defeat it remain unresolved.
- The party remains inside the Boss Zone; the stone gate and route out have not been resolved.
- The Ark - 2020 capsule’s purpose, H Soft’s connection to it, Character Synchronization’s full scope, and any route back to Murim remain unexplained. The manual’s permanent user binding and adjustable time ratio remain binding facts.
- Murim’s death and resurrection limits remain unknown.
- The Head Elder’s Sound Transmission accomplice and the wider plan against the Jin Family remain unresolved.

## Translation Decisions

- Preserve **Ark - 2020**, **H Soft**, **Character Synchronization**, **Synchronization complete**, and **All systems are inherited** exactly.
- Use **Hunter Manpower Office**, **Peace Guild**, **E-rank**, **F-rank**, **porter**, **Gate**, **Boss Zone**, **Hobgoblin Priest**, and **Hobgoblin Great Warrior** consistently.
- Keep **Level 45** for the System level and **rank** for Hunter classifications.
- Use **Im Kkeokjeong/Im Hyeokjun** consistently; retain **hyung** for his informal address.
- Preserve Taekyung’s dry, self-mocking modern voice, blunt sibling banter, and brisk dark action-comedy.
- Render **gukbap** with a first-use footnote as Korean soup served with rice.

### Prior accepted reading-copy tails

#### Chapter 47 tail (verified mastered)

…
what was going on, but strangely, it didn’t feel ominous. *I’ve got a good feeling about this.* My heart pounding, I drew up my internal energy. Ssshhh. At the call of the Jin Family’s Cultivation Technique, fifteen years of internal energy surged up and shot toward the measuring device. * * * At the lobby entrance. “Well done.” Kim Sangshik patted a young man on the shoulder. As of today, the promising young man had officially been recognized as a D-rank Awakened. He would soon join Sopung Guild and be assigned to Kim Sangshik’s team. Thinking of that coming day, Kim Sangshik smiled proudly. “Father and son on the same team. That’s my boy.” “Come on, I’m not even an official Hunter yet. I still have to enter the training center.” “Don’t worry. Your father already made arrangements.” “Wait, really? Didn’t you say there weren’t any openings in the Guild?” “There’s always a way.” He didn’t mention that, in the process, he’d cut the lowest-rank Hunter who’d been a thorn in his side. “Anyway, get plenty of rest this week. Starting next week, we’ll go to work together—” Kim Sangshik’s expression suddenly twisted. “What’s wrong?” “…Nothing. Go wait in the car.” After his son left, he was alone. He rolled up his shirtsleeve. His wrist had already swollen to a dark blue-black. The sight made him grind his teeth. “Jin Taekyung, that fucking bastard.” He’d disliked that bastard from the start. An F-rank Hunter as deputy team leader, and the way he’d been like brothers with the former team leader, who was dead now. *That bastard should’ve fucking died with him back then.* The unfortunate accident two years ago had been a stroke of tremendous luck for Kim Sangshik. After various sex scandals had forced him away from the front lines, he’d made a triumphant return as team leader. A few days ago, he’d even managed to force Jin Taekyung out. *But did that bastard really reawaken?* Kim Sangshik stared down at his throbbing wrist. It had lasted only an instant, but the strength he’d felt had been tremendous. Taekyung might have reawakened as an E-rank, or possibly even a D-rank. “No. Reawakening isn’t child’s play.” Maybe he’d grown weaker because he hadn’t exercised lately. Kim Sangshik was muttering, mixed up inside, when— “We have breaking news from the measurement room.” “Someone good?” “They say a big fish surfaced. C-rank.” “C-rank? Not bad, but that’s not enough to call a big fish, is it?” “But they say his mana control is A-rank.” “What? A-rank! Get a straw in him, now!” “Yes. This is Choi Min-su from Sangdong Guild. The thing is—” A stir spread through the scouts prowling the lobby entrance like hyenas. Most had been dispatched by small and midsized Guilds, but the handful from major Guilds were already moving quickly. *C-rank alone is impressive, and he’s gifted with mana control on top of it?* This was a jackpot. Kim Sangshik’s mind snapped into focus. He shoved every thought of Jin Taekyung far away and pulled out his phone. —Hey, Team Leader Kim. Did that business go well? The deep voice on the other end belonged to Sopung Guild’s Guild Master. Kim Sangshik answered urgently. “Guild Master, all hell has broken loose here. A C-rank just appeared, and they say his mana control is at the level of a high-ranking Hunter.” —What? Where did a guy like that come from? “Exactly. The major Guilds always snatch them up midway, but it looks like they were a step late this time.” —Good. So that’s how it is… Huff. Huff. Rough breaths came through the phone, as if the Guild Master was excited. Even the way he addressed Kim Sangshik changed. —Sangshik. Hold on to this guy no matter what. Tell him we’ll meet any conditions he asks for. “How high can we go on the money?” —Don’t worry about it. Pile plenty on top of whatever the others offer. The major Guilds will drop out if they decide it isn’t profitable enough. It’s not like they’re desperate. “Yes, yes.” —I’m on my way. Keep hold of him until I get there. If you pull this off… you know what that means, right? Kim Sangshik hung up and clenched his fist. *We’ve got this!* He’d been worn smooth by years in this business. Holding on to a newly Awakened rookie was nothing. This was a world where money could put even ghosts to work. *Twice what everyone else offers. I’ll quote double, no matter what.* The commotion grew louder. The elevator that had stopped on the third floor, where the measurement room was, was coming down toward the lobby. “He’s coming!” “Hey, stop shoving.” About twenty scouts clung to the entrance like a swarm of ants. Kim Sangshik had muscled his way into the lead and was ready to hand over his business card. Ding. At last, the elevator doors opened. Kim Sangshik bowed low and launched into the words he’d prepared. “Hello. I’m Team Leader Kim Sangshik of Sopung Guild. We’re a prestigious Guild with a long tradition here in Bucheon—” “This is the first time I’ve heard anyone call Sopung a prestigious Guild.” “…What?” The familiar voice made Kim Sangshik lift his head, gingerly. Their eyes met. At the same moment, Kim Sangshik’s buttonhole-sized eyes flew wide open. “You, you…” Jin Taekyung grinned. “We meet again, Mr. Kim Sangshik.”

#### Chapter 48 tail (verified mastered)

…
a long story.” Jinho hyung chuckled and gripped the scissors. “And your life’s a short one?” Where was I even supposed to start? I had decided not to say anything more about the capsule. I figured it was better if, for Jinho hyung, it just stayed an absurd lie. “Two Rare Monsters showed up at the Gate today, and…” At a life-or-death moment, the luck of a reawakening had come, and I’d been able to take them down. Then I told him about the Association. It was a story hastily stitched together, but Jinho hyung bought it. “So now you’re a C-rank Hunter?” “The reassessment procedure will take a few days, so technically, not yet.” “Same thing, you idiot.” His face was dazed, his voice hoarse. Jinho hyung stared at me for a long moment. Moisture gathered in his eyes. *What’s gotten into this guy?* “…Don’t tell me you’re crying?” “The fuck I am. What kind of bullshit is that?” He turned away with an unnecessary curse, but he couldn’t hide the single tear that fell. I watched him out of the corner of my eye as he roughly rubbed his face with his sleeve. “Hyung?” “Turn the meat over. It’s burning.” “Changing the subject?” “I said it’s burning!” “Ah, all right.” Sizzle. As I turned the meat, I felt flustered, and yet a corner of my chest tickled. *Come to think of it, I’ve known Jinho hyung for a long time.* Six years? Seven? I didn’t know. I’d never counted. Whenever I came back to the goshiwon after a hard day, he had always been there. Sometimes I wondered if this was what it would have felt like to have a real older brother. We had lived like brothers, like friends. “Hey.” Jinho hyung broke the awkward silence. I turned the meat over one more time for no reason. “Yeah? What?” “Good for you.” “…Yeah.” “And…” His quiet voice followed. “You worked hard.” At just those words, something surged up from deep inside me. The emotions and memories that had stacked up over the past seven years all came rushing in at once. “Congratulations on becoming a C-rank Hunter. I guess I can’t tease you anymore.” “Hyung…” “Taekyung…” “Hyung!” “Taekyung!” We hugged each other tightly across the grill. Jinho hyung whispered in my ear, his voice shaking. “Do you remember what I said earlier?” “I know how you feel, hyung. Thank you.” “That’s not what I meant. The finder’s fee.” “…What?” “You have to pay me the finder’s fee. Hyung’s having a hard time these days.” “…” “You make a lot of money now.” Should I really kill him? * * * I staggered back to my room and threw myself onto the bed. A short laugh escaped me as I thought of the one person who was probably cleaning up the roof while grumbling. *You really can’t let your guard down around him.* That was Jinho hyung. The way he congratulated me, and that last prank. I knew it was all just his way of expressing himself. *You worked hard.* Those words kept circling in my head. It was embarrassing to admit, but at that moment, I’d almost cried. *Yeah. I really did work hard.* After my father died, I had run nonstop. I graduated high school while working part-time jobs, and I had to hold on and keep holding on for my sick mother and little sister. At some point, all of it had become a given. And then— Ding. > **System** > > - You have been afflicted with the Status Effect: Dead Drunk. > - It can be detoxified by circulating your qi. *Something that wasn’t a given had entered my life.* It had all started with that unidentified piece-of-junk game capsule. “A game capsule, huh?” I didn’t even know what to call the thing anymore. It had made me a C-rank Hunter, so should I call it a gift from God? No. Maybe it was a gift from the devil. *Is this really okay?* The reason I was thinking this even after the best day of my life was simple. *Nothing comes for free.* That was the world I knew. Everything had a price tag. Visible or not, sooner or later you had to pay. *How expensive is the System?* A hundred billion? A quadrillion? Maybe even more? I laughed weakly and felt my eyelids growing heavy. *Oh, right. I was dead drunk.* Chirp. Chirp-chirp. Outside the window, the grass insects chirped loudly. My vision darkened, and sleep poured over me. That night, I dreamed. I dreamed that somewhere deep in the mountains, someone was shaking me awake. “Squad Leader, Squad Leader!” Weirdly, just hearing it made me want to punch whoever it belonged to. Part of me wanted to see who that familiar voice belonged to, but I was too sleepy to open my eyes. “What do we do?” “We have to tell the main force right away…” “Why is the Squad Leader suddenly like this now of all times…” It felt like listening to a broken radio. The voices had static in them, and they kept cutting out. *I’m sleepy…* As my consciousness drifted farther away, I heard a small but clear voice. “Youngest, survive.” But when I woke the next day, I couldn’t remember any of it. [^2]: A pun: the Korean word for a goshiwon manager sounds like “prime minister.”

## Korean source

```text
＃49화



이른 아침.

나는 슬그머니 눈을 떴다.

띠링.



- [수면 모드]를 종료합니다.



시스템 알림과 동시에 안도의 한숨이 흘러나왔다.

“후우.”

다행이다. 모든 게 꿈이 아니어서.

고작 하루였지만 어제는 내 인생이 바뀐 날이었다. F급 헌터 진태경으로 눈을 떴다면 현실이 악몽처럼 느껴졌겠지.

부스럭거리며 일어난 그때였다.



- 상태 이상, [숙취]에 걸렸습니다.



“윽.”

어젯밤의 후폭풍이 장난이 아니다. 나는 어지러운 머리를 부여잡고 침대 매트리스 위에서 가부좌를 틀었다.

시스템이 알려 준 바에 의하면 운기조식의 기능 중에는 해독도 있었다.



- [운기조식]을 시작합니다.



진가심법의 구결에 따라 공력을 인도했다. 운기조식을 시작함과 동시에 두통이 옅어졌고, 10분 정도가 지나자 기다리던 메시지가 떴다.



- [숙취]가 사라집니다.



하지만 나는 멈추지 않았다. 도중에 갑자기 마무리 지으면 운기조식의 효율이 떨어진다는 사실을 알고 있었기 때문이다.

‘무림에서의 경험이지.’

마침내 가부좌를 푼 것은 한 시간이 지난 후였다. 머리는 맑았고 몸에는 활력이 넘친다.

문제는…….

‘왜 이렇게 들어오는 기운이 적지?’

외부의 기를 받아들여 내부에 저장, 순환시켜야 공력이 증가한다. 그런데 현실에서의 첫 운기조식은 이상할 정도로 그 기운이 적었다.

‘게다가 탁하기까지.’

비유하자면 양도 적고 맛도 없는 음식인데, 그마저도 한참을 기다려야 하는 셈이다. 저절로 눈살이 찌푸려졌다.

‘환경 오염 문제인가?’

자연의 순수한 기를 바탕으로 한 공력이다 보니 그럴 수도 있겠다. 무림과 비교하자면 현대 사회의 자연환경은 심각한 수준이니까.

‘아니면 장소가 문제일지도.’

지어진 지 수십 년이 넘은 고시원 원룸이 딱히 자연 친화적인 장소는 아니지. 냄새도 구리고, 시설도 낡았다.

진호 형은 고시원 총무인 주제에 항상 이곳의 정체를 의심했다.



‘고문실 아니었을까. 대격변 때 몬스터 잡아와서 나이프로 불알 툭툭 치면서 마왕 어딨냐, 하면 마왕 부모님 위치까지 불었을 것 같은데.’



……상상력 하나는 알아줘야 한다.

‘지금쯤이면 자고 있겠지?’

오전에 일어나는 걸 수치로 여기는 인간이니 굳이 확인할 필요도 없다. 아침이라도 먹으러 갈까, 고민하던 그때였다.

지이잉.

핸드폰으로 문자 한 통이 도착했다.



〈 명품충



명품충

시간 괜찮으십니까?



발신인은 명품충, 아니 최 팀장이었다.



* * *



번쩍이는 샹들리에. 맵시 있게 차려입은 사람들과 잔잔하게 흐르는 클래식 음악.

약속 장소는 카페인지, 고급 레스토랑인지 구분이 안 되는 곳이었다.

“주문하시겠습니까?”

시바, 여긴 웨이터도 연예인 수준이네. 모델 비율에 얼굴은 잘생긴 그리스 신 같다.

‘다들 이렇게 게이가 되는 건가.’

정체성 혼란을 느끼는 나와는 달리 최 팀장은 여유롭게 주문을 시작했다.

“블랙 아이보리 한 잔 주시고. 태경 씨는요?”

그리스 신이 내게 고개를 돌렸다.

왠지 카라멜 마끼아또 달라고 하면 안 될 것 같은 이 느낌.

“같은 걸로 주세요.”

잠시 후 나온 커피는 그럭저럭 괜찮았다.

“좋은데요. 이게 블랙…… 뭐라고요?”

“블랙 아이보리.”

사실 들어도 뭐가 뭔지 모른다. 그런가 보다, 하는 거지.

나는 솔직한 감상을 중얼거렸다.

“비싸 보이네요. 원두 좋은 거 쓰나?”

“코끼리 똥이에요.”

“아.”

나는 조용히 커피잔을 내려놨다. 최 팀장은 피식 웃더니 입을 열었다.

“축하드립니다.”

뜬금없는 축하 인사였지만 바로 알아들었다.

그는 전날의 등급 재측정 결과를 말하고 있었다.

“빠르시네요. 개인 정보라 협회에서도 전부 오픈하지는 않았을 텐데.”

“C급 재각성자는 드무니까요. 게다가 어제 그 모습을 직접 봤는데 모를 수가 없죠.”

그것도 그러네.

수긍하는 내게 최 팀장이 뭔가를 내밀었다. 테이블 위에 가지런히 놓인 봉투 한 장.

“이게 뭡니까?”

“보시면 압니다.”

설마, 돈?

나는 봉투 안의 내용물을 확인했다. 수표 대신 깨알처럼 박힌 글자들이 눈에 들어왔다.

“계약서군요.”

“저희 길드가 제시할 수 있는 최대한의 조건입니다. 한 번 읽어 보시죠.”

안 그래도 이미 읽고 있다. 첫 줄부터 마지막까지. 조항마다 놀라움의 연속이다.

“C급 계약서가 아닌 것 같은데요.”

이 바닥에서 7년쯤 굴렀더니 본 것도, 주워들은 것도 많다.

그런 나도 이 정도로 후한 계약서는 처음 본다.

“B급 중에서도 괜찮은 조건이니까요.”

“그런데 왜 저한테…….”

“저를 믿으니까요.”

“네?”

“제 촉을 믿고, 사람 보는 눈을 믿습니다. 그래서 진태경 씨를 꼭 잡고 싶어요.”

최 팀장이 빈 커피잔을 내려놨다.

“계약, 하시겠습니까?”

솔직히 흔들린다. 그것도 아주 많이.

계약 조건을 떠나 누군가가 나를 알아봤고, 이렇게 원하고 있다는 사실에 당장이라도 고개를 끄덕이고 싶다.

그래서 오늘의 망설임은 어제보다 길었다. 마침내 결정을 내렸을 때는 커피가 식은 후였다.

“죄송합니다.”

이유는 어제와 같았다.

계약서에 따르면 최소 1년간 소속 헌터로 활동해야 한다.

제의는 고맙지만…… 나로서는 성급하게 행동할 수 없었다.

“이미 계약하신 겁니까? 아니면 예정이라도?”

“아뇨. 단지 시간이 더 필요해서요.”

“시간이라.”

최 팀장은 한숨을 내쉬었다.

“어쩔 수 없군요.”

다시 한번 사과의 말을 건네려던 그때.

“두 번째 제안입니다.”

“예?”

최 팀장의 품속에서 또 다른 봉투가 나왔다. 어안이 벙벙한 상태로 받아 내용을 확인했다.

“가계약?”

“어떤 건지는 대충 아시죠?”

알지. 잘 알지.

인력 사무소가 일일 근로자라면 길드와의 가계약은 비정규직이다. 짧은 기간 동안 길드에 소속되어 활동하는 일종의 용병인 셈이다.

“이것까지 거절하시지는 않겠죠?”

앞서 받은 정식 계약서보다는 덜하지만, 역시 후하기는 마찬가지다. 거기에 내게 가장 중요한 계약 기간은 텅 빈 공란.

“원하는 기간을 적으세요.”

“아, 네.”

최 팀장이 내미는 펜을 얼떨결에 받아들었다.

그리고 고민 끝에 7일을 적어 넣었다. 일주일이면 시스템이 유지되는지 지켜보기에 충분한 시간이라고 생각했다.

사인까지 마치자 최 팀장이 손을 내밀었다.

“잘 부탁합니다.”

“제가 할 말이죠.”

굳게 손을 맞잡으니 C급 헌터로 첫발을 내디뎠다는 게 실감이 났다.

‘비록 가계약이지만.’

가슴이 벅찼다.

“내일부터 출근하면 되나요?”

“아뇨.”

최 팀장이 시계를 톡톡 두드렸다.

“지금부터.”



* * *



부우웅.

최 팀장의 차는 커다란 군용 차량이었다. 고가의 슈퍼카를 모을 것 같은 이미지라 의외다 싶었는데, 게이트에 도착한 후에야 그 이유를 알았다.

“고르세요.”

“뭘요?”

“장비.”

최 팀장이 작은 버튼을 누르자 성인 남성 다섯 명이 누워도 될 만한 트렁크가 나타났다.

“작업용으로 개조했어요. 집에 놔두기도 뭐해서.”

나는 입을 쩍 벌린 채 트렁크 안을 구경했다.

‘와, 미쳤다.’

적어도 수백만 원을 호가하는 장비들이 차곡차곡 분류되어 있었다. 방어구에 무기는 기본이요. 각종 포션과 비싸서 못 쓴다는 일회용 마법 스크롤까지 없는 게 없다.

“……이게 다 팀장님 거예요?”

“일단은요. 선물 받은 것도 있고, 예뻐서 산 것도 있고.”

그렇구나. 장비가 예뻐서 사는구나.

‘돈이 얼마나 많아야 저런 마인드가 되는 거냐.’

C급 헌터가 잘 벌긴 하지만 최 팀장의 씀씀이는 이미 그 이상이다. 원래 돈 걱정 안 하고 살 만큼 부자인 거겠지.

꿀꺽.

“그냥 대여소에서 빌리는 게 나을 것 같은데요. 괜히 빌렸다가 망가지기라도 하면 좀.”

“유행 지난 거라 상관없어요.”

그렇구나. 장비 디자인 유행도 따지는구나.

나는 그쯤에서 생각하는 걸 포기하고 장비를 골랐다.

시스템이 있으니 장비 고르는 것도 쉬웠다.

‘아이템 확인.’

띠링.



아이템창



[리자드맨 사냥꾼의 가죽 세트]

종류 : 방어구

등급 : 일류

제한 : 無

설명 : 리자드맨의 가죽을 통으로 벗겨 제작했다.

 전 세트 장착 시 [비늘 갑옷] 발동.





‘이거 괜찮네.’

무게도 가볍고, 가죽은 질기면서 단단했다.

모두 장착하자 [비늘 갑옷]의 세트 효과가 발동되었다.

“오.”

가죽 위로 솟아난 녹색 비늘이 온몸을 촘촘하게 뒤덮는다. 그런 내 모습에 최 팀장이 고개를 끄덕였다.

“괜찮은 거 고르셨네요. 안목이 좋으신데요.”

시스템이 좋은 거다.

나는 어색하게 웃으며 무기를 뒤적거렸다. 생각해 보면 최 팀장 이 인간, 검 쓰는 것밖에 못 봤는데 트렁크 안의 무기만 해도 다섯 종류가 넘어간다.

‘손때도 묻어 있고.’

스스로에게 맞는 걸 찾기 위해 노력한 흔적이 보인다.

잠시 후, 내 손에는 창 한 자루가 들려 있었다.



아이템창



[리자드맨 학살자의 작살]

종류 : 무기

등급 : 일류

제한 : 無

설명 : 공격 성공 시 높은 확률로 [출혈] 발동





누가 보면 리자드 성애자인 줄 알겠다. 창을 마지막으로 장비 선택이 끝나자 최 팀장이 피식 웃었다.

“왜 그러세요?”

“일이 잘 풀린다 싶어서요.”

“예?”

“곧 알게 될 겁니다.”

뭔 소린가 싶었지만 일단 최 팀장을 따라 게이트 앞으로 갔다. 관리청 직원 대신 웬 남자가 그곳에 있었다.

“오셨습니까.”

깍듯한 90도 인사. 더 놀라운 건 그 모습을 자연스럽게 받아들이는 최 팀장의 태도다.

“게이트 상황은요?”

“예. 어제 연락받고 출입 통제했습니다.”

“고생하셨어요.”

“아닙니다. 도련님.”

도련님이란 결혼하지 않은 시동생을 높여 이르거나 부르는 말인데, 일단 저 남자가 최 팀장의 형수일 리는 없고…….

‘최 팀장. 부잣집 도련님이었구나.’

어쩐지.

위아래로 명품 장비 쫙 빼입었을 때부터 알아봤어야 했다.

거기에 장비 디자인까지 따지는 패션피플, 어지간한 금수저가 아니고서야 불가능하지.

‘저 인간은 다 가졌네.’

그 다 가진 인간이 내게 고개를 돌렸다.

“자, 이제 들어갑시다.”

“지금 당장이요?”

“장비도 해결됐고, 무슨 문제라도 있습니까?”

너무 당연하다는 말투에 주위를 둘러보았다.

나와 최 팀장. 그리고 낯선 아저씨까지. 셋이 전부다.

“다른 팀원은요?”

“여기 있잖습니까. 팀원.”

“아, 그렇구나. 저분도 들어가시는 거죠?”

아저씨가 묵직한 음성으로 끼어들었다.

“전 아닙니다.”

“그럼……?”

“우리 둘이 전붑니다. 추가 인원은 없어요.”

최 팀장의 말에 나는 어안이 벙벙해졌다.

“없어요?”

“네.”

“한 사람도?”

“개 한 마리 안 데려갑니다.”

단호한 거 보소. 포청천인 줄.

“그럼 단둘이서 게이트를 돈다고요?”

“못 할 거 있습니까? 고작 D급 게이트인데.”

“저 D급 게이트 처음인데요.”

“전 많이 다녀 봤습니다.”

아니, 시발…….

D급 게이트가 무슨 동네 할인 마트도 아니고.

“단둘뿐이라면 빠지겠습니다.”

D급 게이트라면 동일 등급의 헌터 열 명이 팀을 짜야 안전한 레이드를 할 수 있다. 내가 아무리 시스템을 사용할 수 있고, 무공을 익혔다지만 그걸로 모든 위험이 사라지는 건 아니다.

“진태경 씨가 어떤 생각을 하고 있는지 압니다. 하지만 한 가지만 말씀드리죠.”

최 팀장이 느긋한 목소리로 말을 이었다.

“저도 재각성 헌터입니다.”

“재각성이요? 팀장님은 C급으로 알고 있는데…….”

“C급은 처음 측정 당시 나온 등급이죠. 재각성은 그 후의 일이었고.”

말인즉슨 최소 B급 이상의 실력자라는 뜻이다.

가능성은 희박하지만 그 이상일 수도 있고.

‘B급 헌터라.’

그렇다면 말이 달라진다. 단둘뿐이니 그만큼 내게 떨어지는 액수도 늘어날 테고.

“돌아가신다면 말리지는 않겠습니다. 저야 혼자 들어가도 되니까요. 그런 적이 한두 번도 아니고.”

혼자 D급 게이트를 수시로 드나들어?

“그럼 조심히 들어가세요. 내일부터는 E급으로 알아보죠.”

그 말이 결정타였다.

나는 돌아서는 그의 어깨를 덥석 붙잡았다.

“최 팀장님.”

“네.”

“레이드가…… 하고 싶어요.”

최 팀장이 따스하게 웃었다.

“잘해 봅시다.”
```

## Current accepted English baseline

```markdown
# Chapter 49

Early morning.

I eased my eyes open.

Ding.

> **System**
>
> Exiting Sleep Mode.

The System notification came with a sigh of relief.

“Phew.”

Thank goodness. It hadn’t all been a dream.

It had only been one day, but yesterday was the day my life changed. If I’d opened my eyes as Jin Taekyung, F-rank Hunter, reality would have felt like a nightmare.

I rustled my way up—and that was when it hit.

> **System**
>
> Afflicted with the status ailment Hangover.

“Urgh.”

Last night’s aftermath was no joke. I clutched my spinning head and sat cross-legged on the mattress.

The System had told me circulating qi could detoxify, too.

> **System**
>
> Beginning Qi Circulation.

Following the formula of the Jin Family’s Cultivation Technique, I guided my internal energy. The moment I started circulating qi, the headache began to fade. After about ten minutes, the message I’d been waiting for appeared.

> **System**
>
> Hangover disappears.

But I didn’t stop. I knew that wrapping it up halfway through would tank the efficiency.

*Experience from Murim.*

I didn’t uncross my legs until a full hour had passed. My head was clear, and my body was bursting with energy.

The problem was…

*Why is so little energy coming in?*

Internal energy only increased if you took in qi from outside, stored it, and circulated it. But my first circulation in reality brought in strangely little.

*And it’s murky, too.*

It was like a tiny serving of bland food—and even that took forever to arrive. I frowned.

*Environmental pollution, maybe?*

Internal energy was based on pure natural qi, so it was possible. Compared to Murim, the natural environment of modern society was in pretty dire shape.

*Or maybe the location is the problem.*

A one-room in a goshiwon built decades ago was hardly a nature-friendly place. It stank, and the facilities were old.

Jinho hyung was always suspicious of what this place really was, and he was the goshiwon manager.

*Maybe it used to be a torture chamber. During the Great Cataclysm they probably dragged monsters in, tapped their balls with a knife, and asked where the Demon King was. The monsters would’ve given up his parents’ location, too.*

…You had to give him credit for his imagination.

*He should be sleeping by now, right?*

He treated getting up in the morning as a disgrace, so there was no need to check. I was wondering whether to go grab breakfast when—

Bzzzt.

A text arrived on my phone.

〈 Luxury Nutjob

Luxury Nutjob

Do you have some time?

The sender was Luxury Nutjob—or rather, Team Leader Choi.

* * *

A glittering chandelier. Stylishly dressed people, and soft classical music in the background.

I couldn’t tell if the meeting place was a café or a high-end restaurant.

“May I take your order?”

*Shit. Even the waiter here looks like a celebrity.*

Model proportions, and a face like a handsome Greek god.

*Is this how everyone turns gay?*

While I was having an identity crisis, Team Leader Choi calmly started ordering.

“One Black Ivory, please. What about you, Mr. Taekyung?”

The Greek god turned toward me.

Something about the vibe said I shouldn’t order a caramel macchiato.

“I’ll have the same.”

The coffee that came out a little later was pretty decent.

“It’s good. This is Black… what was it?”

“Black Ivory.”

Even after hearing it, I still had no idea what that meant. I just went, well, okay then.

I muttered my honest take.

“It looks expensive. Do they use good beans?”

“It’s elephant dung.”

“Oh.”

I quietly set down my cup. Team Leader Choi chuckled, then spoke.

“Congratulations.”

It came out of nowhere, but I knew what he meant right away.

He was talking about yesterday’s rank reassessment.

“You’re fast. It’s personal information—the Association wouldn’t have opened all of it.”

“C-rank reawakened Hunters are rare. Besides, I saw what happened yesterday with my own eyes. There was no way I wouldn’t know.”

That was true.

As I granted him that, Team Leader Choi held something out. A single envelope, laid neatly on the table.

“What is this?”

“You’ll know when you look.”

*Don’t tell me—money?*

I checked the contents. Instead of a check, tiny printed letters packed the page.

“It’s a contract.”

“The best terms our Guild can offer. Give it a read.”

I was already reading it. From the first line to the last. Every clause was another shock.

“This doesn’t look like a C-rank contract.”

After about seven years knocking around this business, I’d seen plenty, and overheard plenty more.

Even I had never seen a contract this generous.

“They’re good terms even among B-rank contracts.”

“Then why are you offering this to me…?”

“Because they trust me.”

“What?”

“They trust my instincts, and they trust my eye for people. That’s why I want to hold on to Jin Taekyung.”

Team Leader Choi set down his empty cup.

“Will you sign?”

Honestly, I was wavering. A lot.

It wasn’t only the terms. Someone had recognized me and wanted me this badly. I wanted to nod right then.

That was why today’s hesitation ran longer than yesterday’s. By the time I finally decided, the coffee had gone cold.

“I’m sorry.”

The reason was the same as yesterday.

According to the contract, I would have to work as an affiliated Hunter for at least one year.

I was grateful for the offer, but… I couldn’t rush this.

“Have you already signed with someone else? Or are you planning to?”

“No. I just need more time.”

“Time.”

Team Leader Choi sighed.

“I suppose it can’t be helped.”

I was about to apologize again when he said,

“This is my second offer.”

“Pardon?”

Another envelope came out of Team Leader Choi’s jacket. Still dazed, I took it and checked the contents.

“A provisional contract?”

“You have a rough idea of what that is, right?”

I did. I knew it well.

If the Manpower Office was day labor, a provisional contract with a Guild was temp work. You’d be attached to the Guild for a short stretch, basically a mercenary.

“You won’t turn this one down too, will you?”

It was less generous than the formal contract he’d given me, but it was still more than generous enough. And the part that mattered most to me—the contract period—was a blank.

“Write down whatever period you want.”

“Oh. Right.”

I took the pen he held out, half in a daze.

After thinking it over, I wrote seven days. A week should be enough time to see whether the System would last.

Once I’d signed, Team Leader Choi held out his hand.

“I look forward to working with you.”

“That’s my line.”

When we shook hands firmly, it sank in that I’d taken my first step as a C-rank-level Hunter.

*Even if it’s only a provisional contract.*

My chest swelled.

“Should I come in tomorrow?”

“No.”

Team Leader Choi tapped his watch.

“Starting now.”

* * *

Vroom.

Team Leader Choi’s car was a large military vehicle. He looked like the type to collect expensive supercars, so this was unexpected. I only understood why after we arrived at the Gate.

“Pick something.”

“Pick what?”

“Equipment.”

Team Leader Choi pressed a small button, and a trunk large enough for five grown men to lie down in appeared.

“I had it modified for work. Leaving all this at home felt kind of off.”

I stared into the trunk with my mouth hanging open.

*Holy crap.*

Gear worth at least several million won was stacked and sorted. Armor and weapons were a given. Potions of every kind, even disposable magic scrolls people said were too expensive to actually use. He had everything.

“…Is all this yours, Team Leader?”

“For now. Some of it was gifts, and some I bought because it looked nice.”

Ah. So he buys gear because it looks nice.

*How rich do you have to be to think like that?*

C-rank Hunters made good money, but Team Leader Choi’s spending was already beyond that. He must have been rich enough that money was never a concern.

Gulp.

“It might be better to rent from a rental shop. If I borrow something and it gets wrecked, it’d be kind of…”

“They’re out of fashion, so it doesn’t matter.”

Ah. So he even cares whether gear is in fashion.

I gave up thinking about it around there and picked my equipment.

Having the System made it easy.

*Item check.*

Ding.

> **System**
>
> Item Window
>
> Lizardman Hunter’s Leather Set
>
> Type: Armor
>
> **Grade:** First Rate
>
> Restriction: None
>
> Description: Made by stripping off a lizardman’s hide in one piece.
>
> Scale Armor activates when the full set is equipped.

*This is pretty good.*

It was light, and the leather was tough and hard.

Once I had everything on, the set effect Scale Armor activated.

“Oh.”

Green scales rose from the leather and covered my whole body in a tight layer. Team Leader Choi nodded at the sight of me.

“You picked a good one. You’ve got a good eye.”

*It’s the System that’s good.*

I smiled awkwardly and rummaged through the weapons. Come to think of it, I’d only ever seen this guy use a sword, but the trunk alone had more than five kinds of weapons.

*And they’ve got wear on them, too.*

You could see the traces of him trying to find what suited him.

A little later, I had a spear in my hand.

> **System**
>
> Item Window
>
> Lizardman Slayer’s Harpoon
>
> Type: Weapon
>
> **Grade:** First Rate
>
> Restriction: None
>
> Description: Upon a successful attack, Bleeding activates with a high probability.

Anyone watching would think I had a lizardman fetish.

With the spear as the last piece, I was done choosing. Team Leader Choi chuckled.

“What’s so funny?”

“I was thinking things are going well.”

“Pardon?”

“You’ll find out soon enough.”

I had no idea what he meant, but I followed him to the front of the Gate. Instead of an Administration staffer, some man was standing there.

“You’ve arrived.”

A perfectly proper ninety-degree bow. Even more surprising was the way Team Leader Choi took it as natural.

“How’s the Gate?”

“Yes. I received your call yesterday and restricted access.”

“Thanks for your hard work.”

“Not at all, young master.”

*Young master?*

The term was an honorific for an unmarried younger brother-in-law, but there was no way that man was Team Leader Choi’s sister-in-law…

*Team Leader Choi. So he was a rich family’s young master.*

No wonder.

I should have known from the moment I saw him dripping in luxury gear from head to toe.

Add being fashion-conscious enough to care about equipment design, and you couldn’t pull that off unless you were one hell of a gold spoon.

*That guy has everything.*

The guy who had everything turned to me.

“All right. Let’s go in.”

“Right now?”

“The equipment’s taken care of. Is there a problem?”

His tone made it sound so obvious that I looked around.

Me, Team Leader Choi, and some middle-aged guy I didn’t know. That was everyone.

“What about the other team members?”

“They’re right here. The team members.”

“Oh, I see. He’s going in too, right?”

The middle-aged man cut in, his voice heavy.

“I’m not.”

“Then…?”

“It’s just the two of us. There’s no one else.”

Team Leader Choi’s words left me slack-jawed.

“No one else?”

“No.”

“Not even one person?”

“We’re not bringing so much as a dog.”

Look at how decisive he was. Who was he, Pocheongcheon?[^2]

“So the two of us are running the Gate alone?”

“Why couldn’t we? It’s only a D-rank Gate.”

“This is my first D-rank Gate.”

“I’ve been to plenty.”

No, fuck…

A D-rank Gate wasn’t some neighborhood discount mart.

“If it’s just the two of us, I’m backing out.”

A safe raid on a D-rank Gate needed a team of ten Hunters of the same rank. I could use the System, and I’d learned martial arts, but that didn’t make the danger go away.

“I know what you’re thinking, Mr. Jin Taekyung. But let me tell you one thing.”

Team Leader Choi went on in a relaxed voice.

“I’m a reawakened Hunter, too.”

“Reawakened? I thought you were C-rank, Team Leader…”

“C-rank was the rank I received when I was first measured. The reawakening happened afterward.”

Meaning he was at least B-rank in ability.

The odds were slim, but he could be even higher than that.

*A B-rank Hunter.*

If that was true, the situation changed. Just the two of us also meant a bigger cut for me.

“If you want to go back, I won’t stop you. I can go in alone. It wouldn’t be the first time, or the second.”

He walked in and out of D-rank Gates alone on the regular?

“Then be careful in there. From tomorrow, we’ll look at E-rank.”

That was the deciding blow.

I grabbed his shoulder as he turned away.

“Team Leader Choi.”

“Yes?”

“I want to… raid.”

Team Leader Choi smiled warmly.

“Let’s do our best.”

[^2]: Pocheongcheon is a famously incorruptible judge in Chinese legend and popular storytelling.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 49`.

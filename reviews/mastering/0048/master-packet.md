# Master Edit Task — Chapter 48

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
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 김상식 | **Kim Sangshik** |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
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

#### Chapter 46 tail (verified mastered)

…
Jinho hyung scratched his head. “If I saw them, I saw them. If I didn’t, I didn’t.” Was that even an answer, or just crap? When I glared at him, he smiled sheepishly. “Look, it’s not like I’m asking for a finder’s fee or anything…” He was definitely asking for a finder’s fee. Anyway, that wasn’t the point. I shot to my feet and asked, “You saw them? You’re sure?” “If I have to pick, I saw them.” “Who? Where did they go?” “I’m not asking for a finder’s fee, but what’s the expected amount, roughly?” “…100,000 won?” “Oh, dear. Maybe I’m getting old. My memory’s a little hazy.” “For fuck’s sake.” “Right. It’s hot out, so good luck with that.” “The finder’s fee is 180,000 won.”[^5] Apparently satisfied with the amount, Jinho hyung broke into a bright smile. “Your capsule. I picked it up.” “…?” It took me exactly three seconds to understand. *Have you ever seen a daylight robber like this?* I was so dumbfounded I couldn’t even breathe. He’d hit me in the back of the head like this? “But there wasn’t anywhere suitable to put it. My room’s too small, you know.” “So?” “I put it back in your room. I did good, right?” How was I supposed to hit this guy so cleanly that people would say I’d really done it right? My fists trembled. * * * “It really is here.” Seeing the capsule taking up half the studio as if nothing had happened, all I could do was let out a hollow laugh. *Should I call this lucky?* Of all the people who could have taken it, it had been Jinho hyung. I opened the capsule lid, picked up the user manual tossed onto the worn seat, and flipped to the last page. > **Main Features** > > - A customized capsule for one person! Once a user is registered, the capsule becomes permanently bound to that user and remains so until their death. …Come on. No way. *It has to be a simple coincidence.* But I couldn’t shake the unease. I glared at the capsule, the source of everything that had happened. *What even is this thing?* The reason I’d thrown the capsule into the recycling area that morning was so I could forget everything. My life was already dry enough; I wanted to write it off as one nightmare and keep living my life as I was. But now the situation had changed. *Because the System is here.* The System… Then something occurred to me. I placed my hand on the surface of the capsule and murmured, “Item check.” Ding. Just as I thought. The corners of my mouth had just begun to rise when— > **System** > > This Item cannot be read. “…It can’t be read?” This had never happened before. *Is it because I’m not in Murim?* Flustered, I checked every object in the room at random. The television, a ballpoint pen, even the pillow. Every time, the System displayed accurate information. But there was one exception. The capsule couldn’t be read. “Wow. This is driving me nuts.” Just in case, I picked up the user manual. The result was the same. Ding. > **System** > > This Item cannot be read. I flopped onto the bed. I stared blankly at the old, yellow-stained ceiling and thought. *What’s going on?* For now, none of it made sense. But one thing was certain. *I’ve become stronger. Incomparably stronger.* Power had soaked into every fiber of my body. Internal energy writhed in my dantian. Synchronization had given me strength. Strength far beyond that of an F-rank Hunter. Strength enough to defeat a C-rank Rare Monster alone. *Would you like to join the Guild?* It was the first recruitment offer I’d ever received. But I refused. When someone recognized me, fear had come before joy. *Can’t blame me.* I’d endured seven years under the name of F-rank Hunter. A caterpillar that had only ever crawled through the dirt had, one day, grown wings called the System. Fear was only natural. *But what if I can keep using this power—keep using the System?* My heart pounded at the mere thought. At the same time, the past seven years flashed through my mind. The name F-rank, stamped on me like a brand despite all the insane effort I’d put in. Even the memories from two years ago, when I’d trembled at other people’s contempt, at the guilt and the helplessness. “Fuck…” I couldn’t take it anymore. I shot to my feet, burst out of the goshiwon, and flagged down a passing taxi. “Where would you like to go?” I already knew the destination. “Take me to the Bucheon Branch of the Hunter Association.” A Hunter rank reassessment. An F-rank Hunter. I’d start by breaking this loathsome shackle that had tormented me for so long. *Let’s give it a shot.* As I clenched my fist, the taxi driver said, “This is a Seoul taxi.” “Oh.” [^1]: Bigu pills are traditional fasting pills said to sustain the body without ordinary food. [^2]: Yukhoe is seasoned Korean raw beef. [^3]: The Korean words for “talent” and “human disaster” share the same pronunciation, though they use different characters. [^4]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement. [^5]: In Korean, *sip-pal* (“eighteen”) echoes the swear he just used, and he switches abruptly to stiff politeness.

#### Chapter 47 tail (verified mastered)

…
what was going on, but strangely, it didn’t feel ominous. *I’ve got a good feeling about this.* My heart pounding, I drew up my internal energy. Ssshhh. At the call of the Jin Family’s Cultivation Technique, fifteen years of internal energy surged up and shot toward the measuring device. * * * At the lobby entrance. “Well done.” Kim Sangshik patted a young man on the shoulder. As of today, the promising young man had officially been recognized as a D-rank Awakened. He would soon join Sopung Guild and be assigned to Kim Sangshik’s team. Thinking of that coming day, Kim Sangshik smiled proudly. “Father and son on the same team. That’s my boy.” “Come on, I’m not even an official Hunter yet. I still have to enter the training center.” “Don’t worry. Your father already made arrangements.” “Wait, really? Didn’t you say there weren’t any openings in the Guild?” “There’s always a way.” He didn’t mention that, in the process, he’d cut the lowest-rank Hunter who’d been a thorn in his side. “Anyway, get plenty of rest this week. Starting next week, we’ll go to work together—” Kim Sangshik’s expression suddenly twisted. “What’s wrong?” “…Nothing. Go wait in the car.” After his son left, he was alone. He rolled up his shirtsleeve. His wrist had already swollen to a dark blue-black. The sight made him grind his teeth. “Jin Taekyung, that fucking bastard.” He’d disliked that bastard from the start. An F-rank Hunter as deputy team leader, and the way he’d been like brothers with the former team leader, who was dead now. *That bastard should’ve fucking died with him back then.* The unfortunate accident two years ago had been a stroke of tremendous luck for Kim Sangshik. After various sex scandals had forced him away from the front lines, he’d made a triumphant return as team leader. A few days ago, he’d even managed to force Jin Taekyung out. *But did that bastard really reawaken?* Kim Sangshik stared down at his throbbing wrist. It had lasted only an instant, but the strength he’d felt had been tremendous. Taekyung might have reawakened as an E-rank, or possibly even a D-rank. “No. Reawakening isn’t child’s play.” Maybe he’d grown weaker because he hadn’t exercised lately. Kim Sangshik was muttering, mixed up inside, when— “We have breaking news from the measurement room.” “Someone good?” “They say a big fish surfaced. C-rank.” “C-rank? Not bad, but that’s not enough to call a big fish, is it?” “But they say his mana control is A-rank.” “What? A-rank! Get a straw in him, now!” “Yes. This is Choi Min-su from Sangdong Guild. The thing is—” A stir spread through the scouts prowling the lobby entrance like hyenas. Most had been dispatched by small and midsized Guilds, but the handful from major Guilds were already moving quickly. *C-rank alone is impressive, and he’s gifted with mana control on top of it?* This was a jackpot. Kim Sangshik’s mind snapped into focus. He shoved every thought of Jin Taekyung far away and pulled out his phone. —Hey, Team Leader Kim. Did that business go well? The deep voice on the other end belonged to Sopung Guild’s Guild Master. Kim Sangshik answered urgently. “Guild Master, all hell has broken loose here. A C-rank just appeared, and they say his mana control is at the level of a high-ranking Hunter.” —What? Where did a guy like that come from? “Exactly. The major Guilds always snatch them up midway, but it looks like they were a step late this time.” —Good. So that’s how it is… Huff. Huff. Rough breaths came through the phone, as if the Guild Master was excited. Even the way he addressed Kim Sangshik changed. —Sangshik. Hold on to this guy no matter what. Tell him we’ll meet any conditions he asks for. “How high can we go on the money?” —Don’t worry about it. Pile plenty on top of whatever the others offer. The major Guilds will drop out if they decide it isn’t profitable enough. It’s not like they’re desperate. “Yes, yes.” —I’m on my way. Keep hold of him until I get there. If you pull this off… you know what that means, right? Kim Sangshik hung up and clenched his fist. *We’ve got this!* He’d been worn smooth by years in this business. Holding on to a newly Awakened rookie was nothing. This was a world where money could put even ghosts to work. *Twice what everyone else offers. I’ll quote double, no matter what.* The commotion grew louder. The elevator that had stopped on the third floor, where the measurement room was, was coming down toward the lobby. “He’s coming!” “Hey, stop shoving.” About twenty scouts clung to the entrance like a swarm of ants. Kim Sangshik had muscled his way into the lead and was ready to hand over his business card. Ding. At last, the elevator doors opened. Kim Sangshik bowed low and launched into the words he’d prepared. “Hello. I’m Team Leader Kim Sangshik of Sopung Guild. We’re a prestigious Guild with a long tradition here in Bucheon—” “This is the first time I’ve heard anyone call Sopung a prestigious Guild.” “…What?” The familiar voice made Kim Sangshik lift his head, gingerly. Their eyes met. At the same moment, Kim Sangshik’s buttonhole-sized eyes flew wide open. “You, you…” Jin Taekyung grinned. “We meet again, Mr. Kim Sangshik.”

## Korean source

```text
＃48화



“네, 네가 왜 거기 있어?”

“그러게요. 내가 왜 여기 있을까.”

“그럼 혹시……?”

“혹시는 무슨. 역시지.”

김상식의 안색이 똥독 오른 사람처럼 거무죽죽하게 변했다.

그 모습을 보니 10년 묵은 숙변이 내려가는 기분이다. 아아, 이것이 바로 똥르가즘.

“그건 그렇고, 뒤로 좀 갑시다. 여기 혼자만 있는 거 아니잖아요?”

내가 한 걸음 내딛자 김상식이 힘없이 뒷걸음질 친다.

다른 스카우터들이 명함을 들고 나를 둘러쌌다.

“상동 길드입니다. 최고 대우를 약속드립니다.”

“이럴 게 아니라 따로 자리를 옮겨서 말씀을…….”

사방에서 스카우트 제의가 빗발친다. 잠깐 사이에 내 손에는 수십 장의 명함이 들려 있었다.

‘이런 기분이었구나.’

신기하면서도 묘한 기분이다. 7년 동안 단 한 번도 경험하지 못한 일들이 눈앞에서 펼쳐지고 있다.

고작 반나절 만에 나를 둘러싼 세상이 변했다.

아니.

‘내가 변한 거겠지.’

이 바닥에서는 C급 헌터부터가 진짜라는 말이 있다. 뛰어난 능력에 고액 연봉, 사회가 인정하는 중급 헌터.

비로소 그 길에 들어섰다는 사실이 실감 났다.

‘그리고…….’

이건 시작에 불과하다.

시스템의 힘이라면 나는 계속해서 성장해 나갈 수 있다.

그렇게, 어떤 헌터보다 빠르게 새로운 길로 접어들 것이다.

“각성자님, 원하는 조건이 있으시면 무조건 맞춰 드리겠습니다.”

“아, 네. 나중에 연락드릴게요.”

“정말이죠? 기다리겠습니다!”

아냐. 기다리지 마. 연락 안 할 거니까.

“자자, 이제 다들 진정하세요.”

끈질기게 달라붙는 스카우터들을 협회 경비원들이 막아섰다.

사실 C급 헌터를 상대로 저렇게까지 하는 경우는 없는데, 내가 워낙 흔치 않은 케이스라 이목이 많이 쏠리는 모양이었다.

‘하긴, 재각성 한 번으로 껑충 뛰었으니.’

이런 기분도 나쁘진 않다. 아니, 오히려 좋다.

나는 자꾸만 올라가는 입꼬리를 억누르며 협회를 빠져나왔다. 하지만 이 와중에도 따라붙은 한 사람이 있었다.

“진태경! 아니, 태경 씨!”

“허.”

나는 김상식을 보며 헛웃음을 삼켰다.

불과 30분 전만 해도 새끼 소리를 들었는데, 이제는 무려 ‘태경 씨’다.

“왜요?”

“아까, 아까는 내가 미안했어요. 예전에 서운했던 일도 전부 다.”

김상식은 횡설수설하며 과거 자신이 내게 저지른 잘못들을 쏟아 냈다. 때아닌 고해성사를 끝낸 그가 본론을 꺼내 들었다.

“그러니까, 다 잊고 비즈니스로 생각합시다.”

“비즈니스.”

그 단어를 혀끝에서 굴려 본다.

어감 좋고, 느낌은 별로다. 비즈니스 상대가 김상식, 소풍 길드라서 더더욱 그랬다.

“솔직히 태경 씨도 알잖아요. 대형 길드 아닌 이상 거기서 거기인 거.”

“알죠. C급이면 대형 길드에서도 손 내미는 것도 알고.”

“잘 생각해 보란 거죠. 그쪽은 아쉬울 게 없어요. C급 헌터 정도는 어렵지 않게 찾아볼 수 있는 동네니까. 대우도 딱 그 정도일 거고.”

김상식이 침을 튀겨 가며 말을 이었다.

“어디서 얼마를 부르든, 무조건 더 얹어 드릴게. 이 부분은 길드장님 허락도 떨어진 거니까 확실해요.”

소풍 길드는 몇 년간 꾸준한 하락세를 보였다.

그런 상황이니 길드장도 어지간히 똥줄이 탄 모양이다.

‘이 인간도 마찬가지고.’

가뜩이나 길드 내 평가도 바닥인데 며칠 전 멋대로 잘라 버린 F급 헌터가 C급으로 재각성을 해 버렸다.

다혈질로 소문난 길드장이 그 사실을 알면 무슨 일이 벌어질지, 기대감에 입꼬리가 올라갔다.

“긍정적으로만 생각해 줘요. 아, 이럴 게 아니라 어디 괜찮은 가게라도 가서 허심탄회하게 이야기를 해 봅시다. 길드장님도 지금 오고 계시…….”

“김상식 씨.”

나직한 목소리에 상식 씨가 입을 다물었다.

“저 영입하고 싶으면, 길드장님한테 토씨 하나 안 빠트리고 전하세요.”

“무슨?”

“꼴도 보기 싫은 인간. 그 인간 하나만 치워 주면 생각해 본다고.”

누굴 가리키는 말인지는 명백했다.

와락 일그러진 얼굴의 김상식을 뒤로하고, 나는 택시에 올랐다.

‘그래, 이거면 된 거야.’

푹신한 시트에 한껏 몸을 기댔다.

등급 재측정과 옛 악연과의 만남. 뭐라 표현할 수 없는 고양감과 동시에 속이 후련했다.

“어디로 모실까요?”

“송내역 희망 고시원이요.”

택시 기사가 나를 보며 허허 웃었다.

“아까 그 손님이네.”

“아.”

염병할 서울 택시.



* * *



“웬일이냐? 네가 소고기를 다 사 오고.”

고시원 옥상에 돗자리와 불판을 깔았다. 진호 형은 익어 가는 고기들을 흐뭇하게 바라보며 말했다.

“좋아. 네 성의를 봐서 사례금은 없었던 일로 하지.”

“줄 생각도 없었어.”

“양아치냐?”

“그 말 그대로 돌려주지.”

우리는 마주 앉아 소주잔을 기울였다.

“그런데 돈은 어디서 났어? 당장 이번 달도 힘들다고 징징거리던 놈이.”

“오늘 일당.”

“그거 몇 푼이나 된다고. 길드 잘리더니 인생 포기했냐?”

“몇 푼?”

나도 모르게 피식 웃음이 나왔다.

“어쭈, 웃어?”

“웃어야지 그럼. 천만 원을 푼돈 취급 하는데.”

진호 형이 우뚝 멈췄다.

“얼마?”

“천만 원.”

“오늘 일당으로 천만 원을 벌었다고?”

“좀 더 들어오긴 했는데 일단은.”

“너 설마.”

진호 형이 침을 꿀꺽 삼켰다. 눈치가 꽤 빠르군. 그를 향해 의미심장한 미소를 지어 보였다.

“맞아, 나 오늘…….”

“장기 팔았냐?”

죽일까.

나는 한숨을 푹 내쉰 다음 술잔을 털어 넣었다.

“사실대로 말해. 이 형은 고시원 총무로서 알아야 할 의무가 있다.”

얼핏 들으면 고시원 총무가 아니라 국무총리인 줄 알겠다.

“게이트 가서 번 거야.”

“증거 가져와. 난 내 눈으로 본 것만 믿는다.”

“그러시든가, 여기.”

진호 형에게 핸드폰을 건네줬다. 협회에서 재측정을 마치고 돌아오던 길에 받은 문자였다.

발신인은…….

“명품충? 누구야 이건?”

“오늘 같이 레이드 뛴 팀장.”

“돈 많나 보네. 의형제 맺고 싶다.”

이 인간 나랑 생각하는 게 비슷하다.

잠시 후, 문자 내용을 확인한 진호 형이 눈을 부릅떴다.

“천삼십만 원? 이거 내가 제대로 본 거냐?”

“그럴걸.”

계약서대로라면 지급 금액은 30만 원. 최 팀장은 거기에 천만 원을 추가 지급했다.

‘심지어 잔금이 남았지.’

홉 고블린 주술사와 대전사는 C급의 레어 몬스터. 놈들의 장비와 가죽, 마정석은 판매처를 찾고 있다고 최 팀장은 덧붙였다.



‘판매되는 대로 추가 지급하겠습니다.’



정신을 차려 보니 근처 마트에서 소고기를 닥치는 대로 쓸어 담고 있는 나를 발견했다.

“너…….”

진호 형이 멍한 얼굴로 나와 손에 쥔 핸드폰을 번갈아 봤다.

“도대체 어디서 뭘 하고 온 거야?”

“말하자면 긴데.”

허허 웃은 진호 형이 가위를 움켜쥐었다.

“네 명줄은 짧고?”

이걸 어디서부터 얘기해야 하나.

캡슐에 관련해서는 더 이상 말하지 않기로 했다.

진호 형에게는 허무맹랑한 거짓말로 남는 게 좋을 것 같다는 판단이었다.

“오늘 게이트에서 레어 몬스터 두 마리가 나왔는데…….”

목숨이 위태로운 절체절명의 순간, 재각성의 행운이 찾아와 놈들을 무찌를 수 있었다는 것. 그리고 협회에서의 일까지.

급하게 이어 붙인 스토리였지만 진호 형에게는 먹혀들었다.

“그래서, 이제는 C급 헌터라고?”

“재조정 절차 끝나려면 며칠 걸려서 아직은 아닌데.”

“그게 그거지, 인마.”

넋 나간 얼굴, 잔뜩 쉰 목소리.

물끄러미 나를 바라보던 진호 형의 눈에 물기가 맺혔다.

이 양반 왜 이래, 이거.

“……설마 우냐?”

“울기는 시발. 뭔 개소리야.”

괜한 욕과 함께 고개를 돌려보지만 툭 떨어지는 한 방울 눈물까지 감출 수는 없었다. 나는 소매로 얼굴을 벅벅 문지르는 진호 형의 눈치를 살폈다.

“형?”

“고기나 뒤집어. 탄다.”

“딴소리는.”

“탄다고!”

“아, 알았어.”

치이익.

고기를 뒤집는데, 뭔가 당황스러우면서도 가슴 한구석이 간질거린다.

‘그러고 보니까 진호 형이랑 안 지도 오래됐네.’

6년? 7년째던가. 세어 보지 않아서 모르겠다. 힘든 하루를 마치고 고시원에 들어오면 그는 늘 그곳에 있었다.

내게 친형이 있다면 이런 느낌이 아니었을까, 가끔 그런 생각이 들 정도로 우리는 형제처럼, 친구처럼 지냈다.

“야.”

어색한 침묵을 깬 것은 진호 형이었다. 나는 괜히 고기를 한 번 더 뒤집었다.

“어, 왜.”

“잘됐어.”

“……그래.”

“그리고.”

작은 목소리가 뒤를 이었다.

“고생했다.”

고작 그 한마디에.

저 밑에서부터 울컥 솟구치는 뭔가가 있었다. 지난 7년간 켜켜이 쌓여 있던 감정과 기억들이 한꺼번에 밀려들었다.

“C급 헌터 된 거. 축하한다. 이젠 놀리지도 못하겠네.”

“형…….”

“태경아…….”

“형!”

“태경아!”

우리는 불판을 사이에 두고 뜨겁게 포옹했다. 진호 형이 떨리는 목소리로 귓가에 속삭였다.

“아까 내가 했던 말, 기억해?”

“형 마음 다 알아. 고마워, 형.”

“그거 말고. 사례금.”

“……응?”

“사례금 꼭 줘라. 형 요즘 힘들다.”

“…….”

“너 이제 돈 많이 벌잖아.”

진짜 죽일까.



* * *



비틀비틀 방으로 돌아온 나는 침대에 몸을 던졌다.

지금쯤 투덜거리며 옥상을 치우고 있을 한 사람을 생각하니 피식 웃음이 나왔다.

‘하여간 방심할 수가 없어요.’

진호 형답다. 축하하는 방식도, 마지막의 장난도.

전부 그 나름의 표현 방식이라는 사실을 나는 잘 알고 있다.

‘고생했다.’

그 한마디가 자꾸만 머릿속을 맴돈다. 인정하면 쪽팔리지만…… 그때만큼은 살짝 울 뻔했다.

‘그래, 고생했지.’

아버지가 돌아가신 뒤 나는 쉴 새 없이 달려왔다. 알바를 병행하며 고등학교를 졸업했고, 아픈 어머니와 어린 여동생을 위해 버티고 또 버텨야 했다.

어느 순간 그 모든 것들이 내게는 당연한 것이 되어 버렸다.

그리고.

띠링.



- 상태 이상, [만취]에 걸렸습니다.

- [운기조식]으로 해독할 수 있습니다.



‘당연하지 않은 것’이 내 인생에 끼어들었다.

정체불명의 고물 게임 캡슐에서부터 시작된 일이었다.

“게임 캡슐이라.”

이제는 저걸 뭐라고 불러야 할지조차 모르겠다. 나를 C급 헌터로 만들어 줬으니 신의 선물이라고 불러야 하나?

아니, 어쩌면 악마가 준 선물일지도 모르지.

‘이대로 괜찮은 건가?’

인생 최고의 날을 보냈음에도 이런 생각을 하는 이유는 간단하다.

‘공짜는 없으니까.’

내가 경험한 세상은 그랬다. 모든 것에는 가격표가 매겨져 있다. 보이든, 보이지 않든 언젠가는 그 값을 치르기 마련이다.

‘시스템은 얼마나 비쌀까.’

천억? 천조? 어쩌면 그 이상?

비실비실 웃던 나는 눈꺼풀이 무거워지는 걸 느꼈다.

‘아, 맞다. 나 만취 상태였지.’

찌륵. 찌르륵.

창밖에는 풀벌레 우는 소리가 요란했다. 시야가 어두워지며 잠이 쏟아져 내린다. 그리고 그날 밤, 나는 꿈을 꿨다.

깊은 산 속 어딘가에서 누군가 나를 흔들어 깨우는 꿈을.

- 조장, 조장!

이상하게 듣는 것만으로도 때려 주고 싶은 목소리. 한편으로는 낯익은 그 목소리의 주인을 확인하고 싶었지만 너무 졸려 눈을 뜰 수 없었다.

- 어떡하지?

- 당장 본대에 알려야…….

- 조장은 왜 갑자기 이럴 때…….

고장 난 라디오를 듣는 기분이다. 목소리에는 노이즈가 꼈고 뚝뚝 끊겼다.

‘졸려…….’

멀어지는 의식 속에서, 작지만 또렷한 목소리가 들린다.

- 막내야, 살아남아라.

그러나 다음 날 잠에서 깼을 때, 나는 그것들을 기억해 내지 못했다.
```

## Current accepted English baseline

```markdown
# Chapter 48

“Y-you? What are you doing there?”

“Good question. What am I doing here?”

“Then, could it be…?”

“What do you mean, ‘could it be’? It is.”

Kim Sangshik’s face went dark and sallow, like a man with shit poisoning.

Seeing him like that felt like ten years of constipation finally letting go. Ah. So this was a shitgasm.

“Anyway, let’s take a step back. We’re not the only ones here, you know.”

I took a step forward, and Kim Sangshik backed away weakly.

The other scouts surrounded me with business cards in hand.

“Sangdong Guild. We promise the best possible treatment.”

“Instead of doing this here, why don’t we move somewhere private and talk…”

Recruitment offers poured in from every direction. In no time at all, dozens of business cards were in my hands.

*So this is what it feels like.*

It was a novel, peculiar feeling. Things I hadn’t experienced even once in seven years were unfolding right in front of me.

In a mere half day, the world around me had changed.

No.

*I’m the one who changed.*

People said that in this business, C-rank was where you started being a real Hunter. Exceptional ability, a high salary, and society’s recognition as a mid-level Hunter.

At last, it sank in that I had stepped onto that path.

*And…*

This was only the beginning.

With the System’s power, I could keep growing.

That was how I would step onto a new path faster than any other Hunter.

“Sir, if you have any conditions you want, we’ll meet them no matter what.”

“Ah, yes. I’ll get in touch later.”

“You really will, right? We’ll be waiting!”

No. Don’t wait. I’m not going to call.

“All right, everyone, calm down.”

Association security guards stepped in and blocked the scouts who kept clinging to me.

They didn’t usually go that far for a C-rank Hunter. I was just such a rare case that I seemed to be drawing a lot of attention.

*Well, I did jump that far from a single reawakening.*

It wasn’t a bad feeling. No—it felt good.

I fought down a smile that kept trying to break out and left the Association. Even then, one person still followed me.

“Jin Taekyung! No, Mr. Taekyung!”

“Heh.”

I looked at Kim Sangshik and swallowed a hollow laugh.

Only thirty minutes ago, he’d been calling me a bastard. Now I was suddenly *Mr. Taekyung*.

“What do you want?”

“I’m sorry about earlier. Really. And I’m sorry about everything from before, too.”

Kim Sangshik rambled, spilling out every wrong he’d done to me in the past. When that untimely confession was over, he finally got to the point.

“So let’s forget all of it and treat this as business.”

“Business.”

I rolled the word around on my tongue.

It sounded good. The feeling was terrible. Even more so because the business partner was Kim Sangshik and Sopung Guild.

“You already know this, Mr. Taekyung. Unless it’s a major Guild, they’re all more or less the same.”

“I know. I also know that once you’re C-rank, even the major Guilds will reach out.”

“I’m telling you to think it through. They won’t be hurting for you. That’s the kind of place where a C-rank Hunter isn’t hard to find. The treatment will be exactly that level, too.”

Kim Sangshik kept going, spraying spit as he talked.

“No matter what they offer, we’ll add more on top. The Guild Master already signed off on that, so you can count on it.”

Sopung Guild had been in steady decline for several years.

Given the situation, the Guild Master seemed scared shitless.

*This guy’s no different.*

The Guild’s opinion of him was already at rock bottom, and now the F-rank Hunter he’d fired on a whim a few days ago had reawakened as C-rank.

I found myself smiling at the thought of what would happen when the Guild Master, notorious for his temper, found out.

“Just look at it positively. Actually, forget standing around here. Why don’t we go somewhere decent and talk it out honestly? The Guild Master is on his way here right—”

“Mr. Kim Sangshik.”

At my quiet voice, Sangshik shut his mouth.

“If you want to recruit me, tell the Guild Master this. Don’t leave out a single word.”

“Tell him what?”

“I’ll think about it if he gets rid of one man I can’t stand the sight of.”

It was obvious who I meant.

Leaving Kim Sangshik behind with his face twisted in fury, I got into a taxi.

*Yeah. This should do it.*

I sank back into the soft seat.

The rank reassessment. Running into old bad blood. An indescribable rush, and at the same time a sense of relief.

“Where would you like to go?”

“Huimang Goshiwon at Songnae Station.”

The taxi driver looked at me and chuckled.

“Oh, you’re that passenger from earlier.”

“Ah.”

*Goddamn Seoul taxis.*

* * *

“What’s gotten into you? You actually bought beef.”

We laid out a mat and a grill on the goshiwon roof. Jinho hyung gazed happily at the meat as it cooked.

“All right. Seeing your sincerity, I’ll forget about the finder’s fee.”

“I wasn’t planning to give you one.”

“Are you a punk?”

“Right back at you.”

We sat across from each other and tilted our soju glasses.

“But where did you get the money? You were whining that even this month was going to be tough.”

“Today’s pay.”

“How much could that be? Did you give up on life after getting fired from the Guild?”

“How much?”

I couldn’t help letting out a little laugh.

“Oh, you’re laughing?”

“I should laugh. You’re treating ten million won like pocket change.”

Jinho hyung froze.

“How much?”

“Ten million won.”

“You made ten million won in one day’s pay?”

“A little more came in, but that’s for now.”

“You didn’t…”

Jinho hyung swallowed hard. He caught on fast. I gave him a meaningful smile.

“That’s right. Today I—”

“Did you sell an organ?”

Should I kill him?

I let out a long sigh, then downed my drink.

“Tell me the truth. As the goshiwon manager, I have a duty to know.”

If you only heard that, you’d think he was the prime minister, not a goshiwon manager.[^2]

“I made it at a Gate.”

“Bring me proof. I only believe what I see with my own eyes.”

“Suit yourself. Here.”

I handed him my phone. It was the message I’d gotten on the way back from the Association after the reassessment.

The sender was…

“Luxury Nutjob? Who’s that?”

“The Team Leader I ran the raid with today.”

“He must be rich. I want to become sworn brothers with him.”

This guy and I really did think alike.

A moment later, Jinho hyung finished the message and his eyes went wide.

“10.3 million won? Am I reading this right?”

“Probably.”

According to the contract, the payment was supposed to be 300,000 won. Team Leader Choi had added another ten million.

*And there’s still a balance left.*

The Hobgoblin Priest and Great Warrior had been C-rank Rare Monsters. Team Leader Choi had added that he was looking for buyers for their equipment, leather, and Magic Gems.

> “We’ll make an additional payment as soon as they’re sold.”

When I came to, I found myself in a nearby supermarket, grabbing every piece of beef I could get my hands on.

“You…”

Jinho hyung stared blankly, looking from me to the phone in my hand.

“Where the hell have you been, and what did you do?”

“It’s a long story.”

Jinho hyung chuckled and gripped the scissors.

“And your lifespan is short?”

Where was I even supposed to start?

I had decided not to say anything more about the capsule.

I figured it was better if, for Jinho hyung, it just stayed an absurd lie.

“Two Rare Monsters showed up at the Gate today, and…”

At a life-or-death moment, the luck of a reawakening had come, and I’d been able to take them down. Then I told him about the Association.

It was a story hastily stitched together, but Jinho hyung bought it.

“So now you’re a C-rank Hunter?”

“The reassessment procedure will take a few days, so technically, not yet.”

“Same thing, you idiot.”

His face was dazed, his voice hoarse.

Jinho hyung stared at me for a long moment. Moisture gathered in his eyes.

*What’s gotten into this guy?*

“…Don’t tell me you’re crying?”

“The fuck I am. What kind of bullshit is that?”

He turned away with an unnecessary curse, but he couldn’t hide the single tear that slipped down. I watched him out of the corner of my eye as he roughly rubbed his face with his sleeve.

“Hyung?”

“Turn the meat over. It’s burning.”

“Changing the subject?”

“I said it’s burning!”

“Ah, all right.”

Sizzle.

As I turned the meat, I felt flustered, and yet a corner of my chest tickled.

*Come to think of it, I’ve known Jinho hyung for a long time.*

Six years? Seven? I didn’t know. I’d never counted. Whenever I came back to the goshiwon after a hard day, he had always been there.

Sometimes I wondered if this was what it would have felt like to have a real older brother. We had lived like brothers, like friends.

“Hey.”

Jinho hyung broke the awkward silence. I turned the meat over one more time for no reason.

“Yeah? What?”

“Good for you.”

“…Yeah.”

“And…”

His quiet voice followed.

“You worked hard.”

At just those words, something surged up from deep inside me. The emotions and memories that had stacked up over the past seven years all came rushing in at once.

“Congratulations on becoming a C-rank Hunter. I guess I can’t tease you anymore.”

“Hyung…”

“Taekyung…”

“Hyung!”

“Taekyung!”

We hugged each other tightly across the grill. Jinho hyung whispered in my ear, his voice shaking.

“Do you remember what I said earlier?”

“I know how you feel, hyung. Thank you.”

“That’s not what I meant. The finder’s fee.”

“…What?”

“You have to pay the finder’s fee. Hyung’s having a hard time these days.”

“…”

“You make a lot of money now.”

Should I really kill him?

* * *

I staggered back to my room and threw myself onto the bed.

I let out a little laugh, thinking of the one person who was probably cleaning up the roof while grumbling.

*You really can’t let your guard down around him.*

That was Jinho hyung. The way he congratulated me, and that last prank.

I knew all of it was just his way of showing it.

*You worked hard.*

Those words kept circling in my head. It was embarrassing to admit, but for a moment there, I had almost cried.

*Yeah. I really did work hard.*

After my father died, I had run nonstop. I graduated high school while working part-time jobs, and I had to hold on and keep holding on for my sick mother and little sister.

At some point, all of it had become a given.

And then.

Ding.

> **System**
>
> - You have been afflicted with a Status Effect: Dead Drunk.
> - It can be detoxified by circulating your qi.

*Something that wasn’t a given had entered my life.*

It had all started with that unidentified junk game capsule.

“A game capsule, huh?”

I didn’t even know what to call the thing anymore. It had made me a C-rank Hunter, so should I call it a gift from God?

No. Maybe it was a gift from the devil.

*Is this really okay?*

The reason I was thinking this even after the best day of my life was simple.

*Nothing comes for free.*

That was the world I knew. Everything had a price tag. Visible or not, sooner or later you had to pay.

*How expensive is the System?*

A hundred billion? A quadrillion? Maybe even more?

I laughed weakly and felt my eyelids growing heavy.

*Oh, right. I was dead drunk.*

Chirp. Chirp-chirp.

Outside the window, the grass insects were crying loudly. My vision darkened, and sleep poured over me.

That night, I dreamed.

I dreamed that somewhere deep in the mountains, someone was shaking me awake.

“Squad leader, squad leader!”

Weirdly, just hearing it made me want to punch whoever it belonged to. Part of me wanted to see who that familiar voice belonged to, but I was too sleepy to open my eyes.

“What do we do?”

“We have to tell the main force right away…”

“Why is the squad leader suddenly like this now of all times…”

It felt like listening to a broken radio. The voices had static in them, and they kept cutting out.

*I’m sleepy…*

As my consciousness drifted farther away, I heard a small but clear voice.

“Youngest, survive.”

But when I woke the next day, I couldn’t remember any of it.

[^2]: A pun: the Korean word for a goshiwon manager sounds like “prime minister.”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 48`.

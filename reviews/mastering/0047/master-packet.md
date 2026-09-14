# Master Edit Task — Chapter 47

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
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 동기화              | **Synchronization** / **Sync** |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 김상식 | **Kim Sangshik** |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
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

#### Chapter 45 tail (verified mastered)

…
but every piece of gear I had is ruined.” “…” “The armor that protected me for seven years—and now even my spear.” “The spear looks perfectly—” Right then, I pressed down steadily on the middle of the spear with one foot. Under the majesty of a three-digit Strength stat, the iron spear bent like a stick of taffy. “Looks perfectly fine? This?” “…” Team Leader Choi shut his mouth. * * * As the person in charge, Team Leader Choi was called away by the dispatched officials, and the other four were moved to an ambulance for treatment. Instead of the musty break room, I was left alone in a spacious, comfortable office. Now that the moment had actually come, my heart started pounding. *St-Status Window?* At that half-doubtful call, the System answered. Ding. > **System** > > **Status Window** > > **Lv. 33 Jin Taekyung** > > **Job:** First Rate Martial Artist > > **Fame:** 0 > > **Titles:** 2 (Title effects active) > > - Novice Trainee (Training speed +10%) > - Gambler (Combat-related stats +10% in one-on-one matches) > > **Strength:** 120 **Stamina:** 125 > > **Agility:** 121 **Intelligence:** 20 > > **Charm:** 20 **Internal Energy:** 15 years > > **Remaining Points:** 30 > > Synchronization is complete. Changes have occurred to Titles and Fame. “Fuck. It really came up.” I stared blankly at the Status Window for a moment before noticing something strange. *The Status Window… changed?* The first two things that jumped out were Fame reset to zero and the missing Title. The last line gave me a rough idea why. *Because this isn’t Murim?* All five hundred Fame I’d stacked had been earned as a martial artist in Murim. The Title that had vanished, *Scion of a Prestigious Family*, made sense the same way. *Well, I’m not the son of some prestigious family here. And I’m definitely no Sleeping Dragon.* If I were getting a Title here, it’d obviously be something like *Scion of the Common Folk*, or *Earthworm* instead of Sleeping Dragon. “How much else changed?” For about ten minutes I turned every System function on and off one by one and tested them. The only thing that had changed was the Status Window. No—there was one more. The Quest Window. Ding. > **System** > > **Quest** > > **Traitor** > > You have discovered the traitor’s identity. Rejoin the main force, inform them that there is a traitor, and lead the battle to victory! > > **Grade:** Peak > > **Restriction:** Jin Taekyung > > **Mission:** Eliminate the traitor (Incomplete) > > Battle victory (Incomplete) > > **Reward:** Vast EXP and Fame > > Valuable iron chest > > **Failure:** Death It was the Chain Quest I’d received after killing Gwak Jun and the assassins. My thoughts grew tangled. *Am I supposed to go back? To Murim?* I knew it now. The Murim I’d been through wasn’t an illusion, and it wasn’t a game. A wildly unrealistic story, sure, but Murim was probably… Creak. I turned at the sudden sound. Team Leader Choi was standing in the doorway. “Let’s go, Mr. Taekyung.” Looked like the talk had wrapped up. I folded the thought away and stood. “The others…?” “They should be on their way to the hospital by now. They’ll need to stay for about a week. You don’t need to worry.” I wasn’t particularly worried. They had the sturdy bodies of combat-type Hunters, not to mention potions and healing magic. They would be back on their feet soon enough. And… “How did it go?” “They’ll contact us again in a few days. An investigator will probably visit you as well.” An investigator. Not a type I wanted to run into again. But that wasn’t the answer I’d wanted, so I asked again. “What about the other thing?” “Hmm.” Team Leader Choi looked at me with an odd expression. Like he was studying some fascinating animal. *Did he tell them the truth?* I didn’t want my strength out in the open. Even less now, when I still barely knew why I could see the System in reality, or what it had to do with Murim. An F-rank Hunter killing a C-rank Rare Monster alone was unheard of. An awl in a bag pokes through. I’d lived the opposite kind of life, nothing sticking out, so I had to be careful. So I’d asked him: "Could you keep anything about me a secret?" It must have been a difficult request for Team Leader Choi. I was asking him to give a false statement for someone he’d only just met. “Mr. Jin Taekyung.” “Yes.” His heavy voice made my heart grow heavy with it—and then: “Let’s get some food.” “What?” “Look.” Team Leader Choi held out his wrist. A glittering Magic Gem electronic watch pointed to two in the afternoon. “It’s an N Company model carved from a whole C-rank Magic Gem. It’s enchanted with enhancement magic, so in an emergency, you can even use it as a shield—” *So that’s where he was going.* “…Let’s go.” Impossible man to read. “Let’s get some meat. Do you like Hanwoo?[^1]” “Hanwoo?” “Yes. Highest grade.” And rich, too. “I can never get enough of it.” Not just any beef. Hanwoo. Top-grade Hanwoo at that. System or whatever—first I had to fill a hungry stomach. [^1]: Hanwoo is beef from Korean native cattle, prized as premium meat.

#### Chapter 46 tail (verified mastered)

…
Jinho hyung scratched his head. “If I saw them, I saw them. If I didn’t, I didn’t.” Was that even an answer, or just crap? When I glared at him, he smiled sheepishly. “Look, it’s not like I’m asking for a finder’s fee or anything…” He was definitely asking for a finder’s fee. Anyway, that wasn’t the point. I shot to my feet and asked, “You saw them? You’re sure?” “If I have to pick, I saw them.” “Who? Where did they go?” “I’m not asking for a finder’s fee, but what’s the expected amount, roughly?” “…100,000 won?” “Oh, dear. Maybe I’m getting old. My memory’s a little hazy.” “For fuck’s sake.” “Right. It’s hot out, so good luck with that.” “The finder’s fee is 180,000 won.”[^5] Apparently satisfied with the amount, Jinho hyung broke into a bright smile. “Your capsule. I picked it up.” “…?” It took me exactly three seconds to understand. *Have you ever seen a daylight robber like this?* I was so dumbfounded I couldn’t even breathe. He’d hit me in the back of the head like this? “But there wasn’t anywhere suitable to put it. My room’s too small, you know.” “So?” “I put it back in your room. I did good, right?” How was I supposed to hit this guy so cleanly that people would say I’d really done it right? My fists trembled. * * * “It really is here.” Seeing the capsule taking up half the studio as if nothing had happened, all I could do was let out a hollow laugh. *Should I call this lucky?* Of all the people who could have taken it, it had been Jinho hyung. I opened the capsule lid, picked up the user manual tossed onto the worn seat, and flipped to the last page. > **Main Features** > > - A customized capsule for one person! Once a user is registered, the capsule becomes permanently bound to that user and remains so until their death. …Come on. No way. *It has to be a simple coincidence.* But I couldn’t shake the unease. I glared at the capsule, the source of everything that had happened. *What even is this thing?* The reason I’d thrown the capsule into the recycling area that morning was so I could forget everything. My life was already dry enough; I wanted to write it off as one nightmare and keep living my life as I was. But now the situation had changed. *Because the System is here.* The System… Then something occurred to me. I placed my hand on the surface of the capsule and murmured, “Item check.” Ding. Just as I thought. The corners of my mouth had just begun to rise when— > **System** > > This Item cannot be read. “…It can’t be read?” This had never happened before. *Is it because I’m not in Murim?* Flustered, I checked every object in the room at random. The television, a ballpoint pen, even the pillow. Every time, the System displayed accurate information. But there was one exception. The capsule couldn’t be read. “Wow. This is driving me nuts.” Just in case, I picked up the user manual. The result was the same. Ding. > **System** > > This Item cannot be read. I flopped onto the bed. I stared blankly at the old, yellow-stained ceiling and thought. *What’s going on?* For now, none of it made sense. But one thing was certain. *I’ve become stronger. Incomparably stronger.* Power had soaked into every fiber of my body. Internal energy writhed in my dantian. Synchronization had given me strength. Strength far beyond that of an F-rank Hunter. Strength enough to defeat a C-rank Rare Monster alone. *Would you like to join the Guild?* It was the first recruitment offer I’d ever received. But I refused. When someone recognized me, fear had come before joy. *Can’t blame me.* I’d endured seven years under the name of F-rank Hunter. A caterpillar that had only ever crawled through the dirt had, one day, grown wings called the System. Fear was only natural. *But what if I can keep using this power—keep using the System?* My heart pounded at the mere thought. At the same time, the past seven years flashed through my mind. The name F-rank, stamped on me like a brand despite all the insane effort I’d put in. Even the memories from two years ago, when I’d trembled at other people’s contempt, at the guilt and the helplessness. “Fuck…” I couldn’t take it anymore. I shot to my feet, burst out of the goshiwon, and flagged down a passing taxi. “Where would you like to go?” I already knew the destination. “Take me to the Bucheon Branch of the Hunter Association.” A Hunter rank reassessment. An F-rank Hunter. I’d start by breaking this loathsome shackle that had tormented me for so long. *Let’s give it a shot.* As I clenched my fist, the taxi driver said, “This is a Seoul taxi.” “Oh.” [^1]: Bigu pills are traditional fasting pills said to sustain the body without ordinary food. [^2]: Yukhoe is seasoned Korean raw beef. [^3]: The Korean words for “talent” and “human disaster” share the same pronunciation, though they use different characters. [^4]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement. [^5]: In Korean, *sip-pal* (“eighteen”) echoes the swear he just used, and he switches abruptly to stiff politeness.

## Korean source

```text
＃47화



헌터 협회.

삼십여 년 전, 대격변의 종전과 동시에 등장한 이름이다.

피로 얼룩진 대격변에서 살아남은 1세대 헌터들이 깃발을 세웠고, 헌터 협회는 세월의 흐름에 따라 엄청난 위상을 지닌 단체로 발돋움했다.

꿀꺽.

나는 침을 삼키며 우뚝 선 협회 건물을 바라봤다. 이 빽빽한 빌딩 숲에서도 눈에 띄는 크기와 높이. 특별한 것 없는 평일에도 수많은 사람이 그곳을 드나들고 있었다.

‘이게 몇 년 만이지?’

모든 각성자는 협회의 감독하에 등급 측정을 실시한다.

나도 마찬가지였다. 설레는 마음으로 이곳을 찾았던 스무 살의 진태경을 생각하니 피식 웃음이 나오……긴 개뿔.

‘막상 오니까 엄청 긴장되네.’

경직된 걸음으로 로비로 들어섰다. 운동장만 한 로비는 인파로 득실거렸다. 곳곳에 설치된 전광판을 따라 걸음을 옮기니 원하는 곳을 찾을 수 있었다.



[측정 대기실]



창구 직원의 안내에 따라 서류를 작성하고 들어갔다. 대기실에는 수십 명의 인원이 측정을 기다리고 있었다.

쿵. 문 닫히는 소리에 시선들이 화살처럼 날아와 꽂힌다.

‘숨 막힌다, 숨 막혀.’

이곳은 공기부터 다르다. 팽팽한 긴장감이 대기실 전체를 짓누르고 있었다.

‘측정 한 번에 헌터 인생이 결정 나는 거니까.’

나도 마찬가지였다. 너무 긴장한 탓에 감독관 앞에서 방귀를 뀐 적도 있으니 말 다 했지, 뭐.

이런저런 생각을 하며 순서를 기다리고 있을 때였다.

“진태경?”

등 뒤로 들려오는 익숙한 목소리. 천천히 고개를 돌리자 그곳에 그가 있었다.

“설마 했는데, 맞네.”

주먹코에 배불뚝이의 중년인. 잊으려야 잊을 수 없는 얼굴이었다.

‘……김 팀장?’

김상식. 내가 수년간 몸담았던 소풍 길드의 창립 멤버이자 팀장인 그는 한 단어로 설명할 수 있다.

전(前) 직장 상사.

“이야, 이런 데서 볼 줄은 몰랐네. 반가워.”

김 팀장이 너털웃음과 함께 손을 불쑥 내민다. 나는 잠깐 망설이다가 그의 손을 맞잡았다.

“그러게요. 오랜만이네요.”

“오랜만은 무슨. 며칠이나 됐다고.”

“그 며칠이, 저는 꽤 길게 느껴지더라고요.”

무림을 떠올리며 한 말이었지만 김 팀장에게는 다른 의미로 들릴 것이다. 그도 그럴 것이, 불과 며칠 전 내게 해고 통보를 한 장본인이니까.

“여름이라 그래. 나도 요즘 하루가 길어.”

“그래요?”

능구렁이처럼 넘어가는 그를 보자 실소가 흘러나왔다.

언제 봐도 재미있는 양반이다. 여러 가지 의미로.

“그런데 여긴 어쩐 일이야?”

“볼일이 좀 있어서요. 팀장님은요?”

“스카우트차 왔지. 이번에 괜찮은 놈이 있다는 얘길 들어서.”

해고 사유는 구조 조정으로 인한 인원 감축인데 스카우트라.

“그렇군요.”

내가 할 말은 그것밖에 없었다. 다들 아는 뻔한 스토리. 그것도 완결 난 이야기에 더 이상 미련은 없다.

“그러는 너는 왜 왔어? 설마 재측정이라도 해 보려고?”

“네.”

김 팀장이 웃는 얼굴로 말했다.

“거, 시도는 좋지만 너무 돈 낭비 아냐? 재측정 비용이 한두 푼도 아니고. F급 헌터 처지에 부담될 텐데.”

“그래도 해 보는 거죠. 혹시나 하는 마음에.”

“젊을 때 모아 놔야지. 안 되는 거 계속 붙잡고 있으면 뭐가 달라지나.”

“글쎄요. 이번엔 좀 다를 것 같아서요.”

“그게 그렇게 쉬운 일이 아닌…….”

“팀장님.”

“어, 왜?”

나는 부드럽게 웃었다.

“적당히 하시죠.”

순간 김 팀장의 웃음에 실금이 갔다.

“뭐?”

“적당히 하시라고요. 이제 길드도 나갔으니 저한테 신경 끄시고.”

“무슨 뜻이야?”

무슨 뜻이긴.

“아시잖아요. 제가 무슨 말을 하는 건지.”

“…….”

“어쩔 수 없었다. 너라도 살아서 다행이다. 다 잊고 새 시작 하자. 위로하는 척하면서 뒤에서 열심히 쪼아 대셨던데요.”

“너…….”

“길드장님한테 저 자르자고 처음 얘기 꺼낸 것도 팀장님 아닙니까. 제가 모를 줄 아셨어요?”

김 팀장은 한마디로 어중간한 소인배다.

인간성도, 능력도 부족한 인간.

게이트에서도 제 목숨 챙기기에 급급해 길드 내의 평가는 바닥을 기었다.

“저 자르고 그 자리에 누구 넣었습니까? 얼마 받고 꽂아 주기로 했어요?”

“야, 진태경이.”

김 팀장이 내 어깨를 짓누르며 으르렁거렸다. 저래 봬도 소풍 길드에서 셋밖에 없다는 D급 헌터다. 이 정도 힘이면 F급 헌터 따위는 한 손으로도 갖고 놀 수 있다.

하지만…….

“손 떼.”

나는 눈 하나 깜짝하지 않았다. 동기화된 것은 시스템뿐만이 아니다. 무공과 능력치. 그리고 강철 같은 근골까지 포함이다.

“셋 센다. 손 떼.”

“이 새끼가 보자 보자 하니까…….”

나는 망설이지 않고 입을 열었다.

“하나, 둘.”

셋. 동시에 김 팀장의 손목을 움켜쥔 그 순간이었다.

덜컹.

“다음 분들 들어오세요. 21번부터 30번!”

서류철을 든 협회 감독관의 등장에 우리는 누가 먼저랄 것도 없이 떨어졌다. 협회에 찍혀 봤자 서로에게 좋을 게 없다.

“운 좋은 줄 알아라.”

“누구. 내가? 아니면 당신?”

벌겋게 달아오른 김 팀장의 얼굴이 퍽 우습다. 기감으로 파악한 그의 레벨창까지도.



[Lv.24 김상식]



“만나서 기분 더러웠고, 다신 보지 맙시다.”

미련 없이 자리를 털고 일어났다. 내가 받은 대기 번호는 30번. 감독관을 향해 걸어가는 발걸음은 더 이상 경직되어 있지 않았다.



* * *



“21번. 앞으로 나와 주세요.”

긴장된 얼굴의 각성자가 측정기 앞에 섰다. A급 마정석을 재료로 만든 등급 측정기는 그의 전신을 스캔, 체내의 마나를 수치로 환산한다.

지이잉-

수치를 확인한 감독관이 입을 열었다.

“체내 마나 분포량, F급.”

각성자의 얼굴이 흙빛으로 변했다. 하지만 절망하기에는 이르다. 두 번째 기회가 있으니까.

“마나를 움직여 보세요. 최대한 집중해서 측정기로 쏘아 보낸다는 느낌으로.”

마나 컨트롤을 보는 거다. 아직 끝나지 않았다는 사실을 깨달은 각성자가 이를 악물고 힘을 끌어 올렸다.

젖 먹던 힘까지 빡!

뿌우웅.

“…….”

“…….”

감독관이 토할 것 같은 얼굴로 말했다.

“제어 능력, F급.”

“한 번만! 다시 한번만 해 볼게요!”

“안 됩니다. 다음.”

순서가 휙휙 넘어간다.

죄다 E급, F급에 심지어는 비각성자인 놈까지 나왔다.

“이거 사기야, 사기! 저 측정기 중국산이지! 어? 이 새끼들아!”

“처리하세요.”

감독관의 말에 대기하고 있던 경비 헌터들이 사기꾼을 질질 끌고 나갔다. 아마 저놈은 기적적으로 각성한다고 해도 협회 블랙리스트에 등록될 거다.

“다음, 30번.”

올 게 왔구나.

나는 크게 숨을 들이켜고 앞으로 나섰다. 감독관이 손에 든 서류철을 흘끗 보더니 말했다.

“재측정이시네요?”

“네.”

“진태경 씨, 7년 전 F급 취득하셨고…… 재측정은 따로 비용 청구되는 건 아시죠?”

대충 들어 보니 괜히 헛돈 쓰지 말고 기회 줄 때 집에나 가란 소리다. F급 헌터를 보는 흔한 시선들.

‘누굴 거지로 아나.’

익숙한 것과 기분이 더러운 건 별개다. 내가 노려보자 감독관이 피식 웃었다.

“혹시 싶어 말씀드리는 건데 비용은 2백만 원입니다.”

“……가격 올랐어요?”

“몇 년 됐죠.”

시벌, 그걸 몰랐네.

지금 내 통장 잔고가 얼마더라…….

“그럼 측정 시작하겠습니다.”

나는 떨리는 마음으로 눈을 감았다. 그리고 다음 순간.

지이잉.

측정기에서 흘러나온 마력의 파동이 전신을 훑고 지나갔다.

15년의 공력이 그에 감응해 부르르 떨었다.

‘몇 급일까?’

C급? 아니, D급만 되어도 좋다. 하지만 십여 초를 기다려도 감독관의 입은 열리지 않았다.

“어어, 이게 왜 이러지?”

“왜요?”

당황한 얼굴로 측정기와 나를 번갈아 보던 그가 헛기침했다.

“오류가 좀 생긴 것 같은데…… 일단 다음 순서로 넘어가겠습니다.”

뭐가 어떻게 돌아가는 건지는 모르겠지만 어쩐지 불길하게 느껴지진 않는다.

‘느낌이 좋아.’

나는 두근거리는 심장 박동을 느끼며 공력을 끌어 올렸다.

스아아.

진가심법의 부름에 따라 솟구친 15년의 공력이 측정기를 향해 쏘아졌다.



* * *



로비 입구.

“잘했다.”

김상식은 청년의 어깨를 두드렸다. 오늘부로 D급 각성자로 공인받은 전도유망한 젊은이다.

그는 곧 소풍 길드에 가입, 김상식의 팀에 배정될 것이다. 곧 다가올 그 날을 떠올린 김상식은 뿌듯하게 웃었다.

“부자(父子)가 한 팀을 이루겠구나. 역시 내 아들이야.”

“뭘요, 아직 정식 헌터가 된 것도 아닌데. 훈련소도 들어가야 하고.”

“걱정하지 마라. 이 아버지가 미리 손써 뒀으니까.”

“어, 진짜요? 길드에 자리 없다고 하지 않았나?”

“다 방법이 있지.”

그 과정에서 눈엣가시 같던 최하급 헌터를 잘랐다는 사실은 말하지 않았다.

“어쨌든 이번 주는 푹 쉬고, 다음 주부터 같이 출근…….”

문득 김상식의 표정이 일그러졌다.

“왜 그래요?”

“……아니다. 먼저 차에 가 있어.”

아들이 떠난 후 홀로 남은 그는 셔츠 소매를 걷어 올렸다.

어느새 검푸른색으로 부어오른 손목을 확인하자 이가 갈린다.

“진태경, 이 개새끼가.”

그 자식은 처음부터 마음에 안 들었다. F급 헌터인 주제에 부팀장인 것도, 지금은 죽고 없는 전 팀장과 형제처럼 지내던 모습도 그랬다.

‘저 새끼도 그때 같이 뒈졌어야 했는데.’

2년 전 벌어진 불의의 사고는 김상식에게 있어 천운이었다.

각종 성추문으로 일선에서 물러나 있던 그는 팀장으로 금의환향했고, 며칠 전 진태경까지 내보낼 수 있었으니까.

‘그런데 이놈, 정말 재각성인가?’

김상식은 욱신거리는 손목을 내려다봤다.

그야말로 찰나의 순간이었지만 그때 느낀 힘은 어마어마했다. E급, 어쩌면 D급으로 재각성 했을지도 모를 일이다.

“아니지, 재각성이 무슨 애들 장난도 아니고.”

요즘 운동을 안 해서 약해진 건가. 김상식이 복잡한 심정으로 중얼거리던 순간이었다.

“측정실에서 속보 왔습니다.”

“괜찮은 놈 있대?”

“월척 하나 떴답니다. C급.”

“C급? 나쁘진 않은데 월척 소리 들을 정도는 아니잖아?”

“그런데 마나 컨트롤이 A급이랍니다.”

“뭐? A급! 빨대 꽂아, 빨리!”

“예. 상동 길드 최민숩니다. 다름이 아니고…….”

로비 입구를 하이에나처럼 어슬렁거리던 스카우터들 사이로 술렁임이 번졌다.

대부분이 중소 길드에서 파견된 이들이었지만 대형 길드에서 나온 몇몇은 이미 발 빠르게 움직이고 있다.

‘C급만 해도 상당한데, 마나 컨트롤까지 타고났어?’

이건 대박이다.

김상식은 정신이 번쩍 들었다. 진태경에 관한 생각은 저 멀리 내팽개치고 핸드폰을 꺼내 들었다.

- 어, 김 팀장. 갔던 일은 잘됐고?

수화기 너머 굵은 목소리의 주인은 소풍 길드장이었다.

김상식이 다급하게 말했다.

“길드장님. 지금 여기 난리 났습니다. C급 떴어요. 거기에 마나 컨트롤은 상위 헌터 수준이랍니다.”

- 뭐? 그런 놈이 어디서 튀어나와?

“그러니까요. 대형 길드 놈들, 매번 중간에 가로채더니 이번에는 한발 늦은 모양입니다.”

- 좋아, 그렇단 말이지…….

후욱. 훅.

흥분했는지 거친 숨소리가 흘러나왔다. 김상식을 부르는 호칭도 바뀌었다.

- 상식아. 너 이거 꼭 붙잡아라. 무조건 원하는 조건에 맞춘다고 해.

“금액 어디까지 됩니까?”

- 신경 쓰지 말고 다른 놈들 부르는 금액에 듬뿍 얹어 줘. 대형 길드 놈들이야 수지 좀 안 맞는다 싶으면 떨어질 거야. 그것들은 아쉬울 것도 없잖아?

“예, 예.”

- 나 지금 간다. 꼭 붙잡고 있어. 이거 성공시키면…… 알지?

전화를 끊은 김상식은 주먹을 불끈 움켜쥐었다.

‘됐다!’

이 바닥에서 닳고 닳은 그다. 이제 막 각성한 신출내기 각성자 정도쯤이야 붙잡아 두는 건 일도 아니다.

돈이면 귀신도 부리는 세상 아닌가.

‘다른 놈들보다 무조건 두 배. 두 배 부른다.’

그때 웅성거림이 더 커졌다. 측정실이 있는 3층에서 멈춘 엘리베이터가 로비를 향해 내려오고 있었다.

“온다!”

“아 거, 밀치지 좀 맙시다.”

스카우터 이십여 명이 개미 떼처럼 입구에 달라붙었다. 우악스럽게 선두 자리를 차지한 김상식이 명함을 건넬 만반의 준비를 마쳤다.

띵.

그리고 마침내 열리는 엘리베이터 문.

김상식은 넙죽 고개를 숙이며 준비해 둔 말을 꺼냈다.

“안녕하십니까. 소풍 길드의 김상식 팀장입니다. 저희는 전통 있는 부천의 명문 길드로서…….”

“소풍 길드가 명문이라는 소리는 또 처음 들어 보네.”

“……네?”

익숙한 목소리. 김상식의 고개가 슬그머니 들렸다.

그리고 두 사람의 시선이 부딪쳤다. 단춧구멍 같던 김상식의 눈이 부릅떠진 것도 동시였다.

“너, 너…….”

진태경이 씩 웃었다.

“또 만났네요. 김상식 씨.”
```

## Current accepted English baseline

```markdown
# Chapter 47

Hunter Association.

The name had appeared some thirty years ago, at the same time the Great Cataclysm ended.

The first-generation Hunters who survived that blood-soaked catastrophe raised their flag, and over the years the Hunter Association grew into an organization of tremendous stature.

Gulp.

I swallowed as I stared up at the Association building standing tall before me. Even in this dense forest of skyscrapers, its size and height stood out. Even on an ordinary weekday, people streamed in and out.

*How many years has it been?*

Every Awakened underwent rank measurement under the Association’s supervision.

I was no different. The thought of twenty-year-old Jin Taekyung walking in here all excited almost made me snort—like hell it did.

*Now that I’m actually here, I’m incredibly nervous.*

I went into the lobby on stiff legs. The place was the size of a sports field and packed with people. I followed the electronic signs posted throughout until I found what I wanted.

**Measurement Waiting Room**

On the clerk’s instructions, I filled out the paperwork and went inside. Dozens of people were waiting to be measured.

Thud.

The door shut, and everyone’s eyes shot into me like arrows.

*Suffocating. This is suffocating.*

Even the air was different here. A taut tension pressed down on the entire waiting room.

*One measurement decides your whole Hunter life.*

I was no different. I’d been so nervous I’d even farted in front of an examiner once. That pretty much said it all.

I was waiting my turn, thinking about this and that, when—

“Jin Taekyung?”

A familiar voice from behind me. I turned my head slowly.

There he was.

“I didn’t think it would be, but it is.”

A middle-aged man with a bulbous nose and a potbelly. A face I couldn’t forget no matter how hard I tried.

*…Team Leader Kim?*

Kim Sangshik. A founding member and team leader of Sopung Guild, where I’d spent years. He could be summed up in one word.

Former boss.

“Wow, I never expected to run into you somewhere like this. Good to see you.”

Team Leader Kim thrust out his hand with a hearty laugh. I hesitated a moment, then took it.

“Likewise. It’s been a while.”

“What do you mean, a while? It’s only been a few days.”

“Those few days felt pretty long to me.”

I’d said it thinking of Murim, but Team Leader Kim would hear something else. After all, he was the one who’d handed me my dismissal only a few days ago.

“It’s because it’s summer. My days have felt long lately too.”

“Really?”

Watching him slide past it like a sly old fox, I let out a hollow laugh.

He was a funny guy, no matter when you saw him.

In more ways than one.

“So what brings you here?”

“I had some business. What about you, Team Leader?”

“Came to scout. Heard there was a decent one this time.”

They’d fired me for staff cuts in a restructuring. And he was here to scout.

“I see.”

That was all I had to say. Everyone knew that tired story, and it was already over. I had no lingering attachment left.

“What about you? Why are you here? Don’t tell me you’re trying to get reassessed.”

“Yes.”

Team Leader Kim spoke with a smile.

“Nice try, but isn’t that a waste of money? A reassessment isn’t cheap. Must be a burden for an F-rank Hunter.”

“Still, I figured I’d try. Just in case.”

“You should save up while you’re young. What’s going to change if you keep clinging to something that isn’t going to work?”

“Who knows? I think this time might be different.”

“It’s not that easy—”

“Team Leader.”

“Huh? What?”

I smiled, gentle.

“That’s enough.”

A crack ran through Team Leader Kim’s smile.

“What?”

“I said that’s enough. I’ve left the Guild now, so stay out of my business.”

“What’s that supposed to mean?”

What did it mean?

“You know what I mean.”

“…”

“It couldn’t be helped. You’re lucky you survived. Forget it all and make a fresh start. You pecked away at me behind my back while pretending to console me.”

“You…”

“Weren’t you the one who first told the Guild Master to cut me? Did you think I wouldn’t know?”

Kim Sangshik was a half-baked, petty little man.

Short on humanity, short on ability.

Even in Gates, he was too busy saving his own skin. His reputation in the Guild was rock-bottom.

“Who did you put in my place after you fired me? How much did you take to slot someone in?”

“Hey. Jin Taekyung.”

Team Leader Kim clamped down on my shoulder and growled. He didn’t look it, but he was one of only three D-rank Hunters in Sopung Guild. With that kind of strength, he could have toyed with an F-rank Hunter like me with one hand.

But—

“Take your hand off.”

I didn’t even blink. It wasn’t only the System that had synchronized. My martial arts, my stats, and even my steel-like Sinews and Bones had come with it.

“I’ll count to three. Take your hand off.”

“You little bastard. I’ve been putting up with you, but—”

I didn’t hesitate.

“One. Two.”

Three.

The instant I grabbed Kim Sangshik’s wrist—

Clack.

“Would the next group please come in. Numbers twenty-one through thirty!”

An Association examiner walked in with a file, and we both let go before the other could. Getting marked by the Association wouldn’t do either of us any good.

“Consider yourself lucky.”

“Who. Me? Or you?”

Kim Sangshik’s flushed face looked downright ridiculous. Even the Level Window I’d picked up through Qi Sense.

> **System**
> Lv. 24 Kim Sangshik

“Meeting you was disgusting. Let’s never see each other again.”

I got up without a shred of regret. My waiting number was thirty. The steps I took toward the examiner weren’t stiff anymore.

* * *

“Number twenty-one. Please come forward.”

An Awakened with a tense face stood in front of the measuring device. Made from an A-rank Magic Gem, it scanned his whole body and converted the mana inside him into numbers.

Bzzzzzt—

The examiner checked the reading and spoke.

“Mana distribution in the body: F-rank.”

The Awakened’s face turned ashen. But it was too soon to despair. He had a second chance.

“Try moving your mana. Concentrate as hard as you can, and imagine firing it into the measuring device.”

They were checking his mana control. Realizing it wasn’t over yet, the Awakened gritted his teeth and drew up his strength.

Every last ounce of it—ngh!

Bwoooom.

“…”

“…”

The examiner spoke with a face that looked ready to vomit.

“Control ability: F-rank.”

“Just once! Let me try one more time!”

“No. Next.”

The line moved fast.

All E-rank or F-rank. One guy wasn’t even Awakened.

“This is a scam! A scam! That measuring device is made in China, isn’t it? Huh? You bastards!”

“Handle him.”

At the examiner’s word, the security Hunters waiting nearby dragged the fraud out. Even if that guy miraculously Awakened, he’d probably end up on the Association’s blacklist.

“Next. Number thirty.”

Here it came.

I took a deep breath and stepped forward. The examiner glanced at the file in his hand.

“This is a reassessment?”

“Yes.”

“Mr. Jin Taekyung, you received F-rank seven years ago… and you know there’s a separate fee for reassessments, right?”

From the way he said it, he might as well have been telling me not to waste my money and to go home while I still could. The usual look people gave an F-rank Hunter.

*Do they think I’m a beggar?*

Familiar was one thing. Still filthy was another. When I glared at him, the examiner gave a short puff of a laugh.

“I’m only mentioning it in case you weren’t aware, but the fee is two million won.”

“…The price went up?”

“It’s been a few years.”

*Fuck. I didn’t know that.*

How much was in my account right now…?

“Then we’ll begin the assessment.”

Nervous, I closed my eyes.

And the next moment—

Bzzzzzt.

A wave of mana rolled out of the measuring device and swept through my whole body.

Fifteen years of internal energy answered it and shuddered.

*What rank will it be?*

C-rank? No, I’d be happy with D-rank. But ten seconds or so passed, and the examiner still didn’t open his mouth.

“Uh… why is it doing this?”

“Why?”

He looked from the device to me, flustered, then cleared his throat.

“There seems to be some kind of error… We’ll move on to the next step for now.”

I had no idea what was going on, but strangely, it didn’t feel ominous.

*This feels good.*

Feeling my heart pound, I drew up my internal energy.

Ssshhh.

At the call of the Jin Family’s Cultivation Technique, fifteen years of internal energy surged up and shot toward the measuring device.

* * *

The lobby entrance.

“Well done.”

Kim Sangshik patted a young man on the shoulder. As of today, he was a promising young D-rank Awakened, officially recognized.

He would soon join Sopung Guild and be assigned to Kim Sangshik’s team. Thinking of that coming day, Kim Sangshik smiled, proud.

“Father and son on the same team. That’s my boy.”

“What are you talking about? I’m not even an official Hunter yet. I still have to go through the training center.”

“Don’t worry. Your father already took care of it.”

“Wait, really? Didn’t you say the Guild didn’t have a spot?”

“There’s always a way.”

He didn’t mention that, in the process, he’d cut the lowest-rank Hunter who’d been a thorn in his eye.

“Anyway, rest up this week, and starting next week we’ll commute together—”

Kim Sangshik’s face suddenly twisted.

“What’s wrong?”

“…Nothing. Go wait in the car.”

After his son left, he was alone. He rolled up his shirtsleeve.

His wrist had already swollen a dark blue-green. The sight made him grind his teeth.

“Jin Taekyung, you fucking bastard.”

He’d disliked that bastard from the start. An F-rank Hunter as deputy team leader, and the way he’d been like brothers with the old team leader, who was dead now.

*That bastard should’ve fucking died with him back then.*

The unfortunate accident two years ago had been a stroke of luck for Kim Sangshik.

After being sidelined by various sex scandals, he’d made a triumphant return as team leader. A few days ago, he’d even gotten Jin Taekyung thrown out.

*But was this bastard really a reawakening?*

Kim Sangshik stared down at his throbbing wrist.

It had only lasted an instant, but the strength he’d felt then had been tremendous. Taekyung might have reawakened as E-rank—or even D-rank.

“No. Reawakening isn’t child’s play.”

Maybe he’d gotten weaker from not exercising lately. Kim Sangshik was muttering, mixed up inside, when—

“We have breaking news from the measurement room.”

“Someone good?”

“They say a big fish surfaced. C-rank.”

“C-rank? Not bad, but that’s not enough to call a big fish, is it?”

“But they say his mana control is A-rank.”

“What? A-rank! Get a straw in him, now!”

“Yes. This is Choi Min-su from Sangdong Guild. The thing is—”

A stir spread through the scouts prowling the lobby entrance like hyenas.

Most of them had been sent by small and midsized Guilds, but a few from the major ones were already moving fast.

*C-rank alone is impressive, and he’s gifted with mana control on top of it?*

This was a jackpot.

Kim Sangshik’s mind snapped clear. He shoved every thought of Jin Taekyung far away and pulled out his phone.

—Hey, Team Leader Kim. Did that business go well?

The deep voice on the other end belonged to Sopung Guild’s Guild Master.

Kim Sangshik spoke in a rush.

“Guild Master, it’s chaos here. A C-rank just showed up. And they say his mana control is at the level of a high-ranking Hunter.”

—What? Where did a guy like that come from?

“Exactly. The major Guilds always snatch them up midway, but it looks like they were a step late this time.”

—Good. So that’s how it is…

Huff. Huff.

Rough breaths came through the phone, as if he was excited. Even the way he addressed Kim Sangshik changed.

—Sangshik. You hold on to this guy no matter what. Tell him we’ll meet whatever conditions he wants.

“How high can we go on the money?”

—Don’t worry about it. Pile plenty on top of whatever the others offer. The major Guilds will drop out if they decide it isn’t profitable enough. It’s not like they need him.

“Yes, yes.”

—I’m on my way. Keep hold of him until I get there. If we pull this off… you know what that means, right?

After hanging up, Kim Sangshik clenched his fist.

*We’ve got this!*

He’d been worn smooth by years in this business. Holding on to a newly Awakened rookie was nothing.

This was a world where money could put even ghosts to work.

*Twice what everyone else offers. I’ll quote double, no matter what.*

The commotion grew louder. The elevator that had stopped on the third floor, where the measurement room was, was coming down toward the lobby.

“He’s coming!”

“Hey, stop shoving.”

About twenty scouts clung to the entrance like a swarm of ants. Kim Sangshik had muscled his way into the lead and was ready to hand over his card.

Ding.

At last, the elevator doors opened.

Kim Sangshik bowed low and launched into the words he’d prepared.

“Hello. I’m Team Leader Kim Sangshik of Sopung Guild. We’re a prestigious Guild with a long tradition here in Bucheon—”

“This is the first time I’ve heard anyone call Sopung a prestigious Guild.”

“…What?”

The familiar voice made Kim Sangshik lift his head, gingerly.

Their eyes met.

At the same time, Kim Sangshik’s buttonhole-sized eyes went wide.

“You, you…”

Jin Taekyung grinned.

“We meet again, Mr. Kim Sangshik.”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 47`.

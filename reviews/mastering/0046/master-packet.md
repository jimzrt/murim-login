# Master Edit Task — Chapter 46

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
| 최민우    | **Choi Minwoo**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 살기     | **killing intent**                               |                                                       |
| 가주     | **Family Head**                              |
| 시스템              | **System**                     |
| 명성               | **Fame**                       |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 동기화              | **Synchronization** / **Sync** |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 산서     | **Shanxi**             |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 당장은 | polysemy | Right away / for now / at the moment; not the broader “anytime soon.” | anytime soon |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |

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

#### Chapter 44 tail (verified mastered)

…
was still going on at the altar in the distance. A tired voice came through the explosions. “What?!” “Are you still not done? It feels like it’s been more than five minutes!” Boom! Boom! Fwoosh! Lightning struck, and flames surged. Team Leader Choi screamed, “Three more minutes!” Anyone who didn’t know better would think he was a soccer referee. His bold call for extra time left me speechless. —Karruk, karruk. The Hobgoblin Great Warrior came on slowly. A cruel smile hung on its wide-slit mouth. I edged backward in time with its steps. “That’s right. Come on. Come on.” No choice. Same as before: run like hell and stall. —Grrk. But the Great Warrior didn’t move the way I expected. “Huh?” Its bulging eyes rolled toward my teammates sprawled unconscious on the ground. I had a very bad feeling about this. “Don’t tell me…” That was exactly it. My heart sank as I watched its back heading for Im Kkeokjeong. “Hey! Hey, you bastard!” It ignored me completely. Now I was the one panicking. *If I leave it like this, they’re all dead.* I had to draw its attention somehow. I grabbed one of the rocks scattered around me and hurled it at the monster’s head. Thwack! Direct hit. The Hobgoblin Great Warrior turned and glared at me. “Yeah. Come here.” —Grrr. Its narrowed eyes flicked between me and Im Kkeokjeong. Then it started running toward Im Kkeokjeong. Boom, boom, boom! “You crazy bastard!” At this rate, not only Im Kkeokjeong but the rest of the team would be wiped out too. I was the only one who could stop it. *Stop that thing? Me?* A one-on-one fight against a C-rank Rare Monster. A fight I could never win. But… *Ah, fuck.* I was already charging at it. Sometimes you have to fight even when there’s no chance. This was one of those times. “Hey, you son of a bitch!” Whoosh—! The instant I thrust my spear at its broad back— —Kururuk. The green giant turned like it had been waiting. A smug smile sat on its mouth. The greatsword swept in horizontally, a streak of light shooting for my side. *That’s what you were after.* My mind went blank. Could I even block that? Had I made the wrong call out of some cheap guilt and heroics? But the die was already cast. *I have to hold.* There are times you fight with your life on the line. This was one of them. *Please!* I clenched my teeth and turned the iron spear into the greatsword’s path. At the same time, the greatsword smashed into it. Rrrrrumble— A roar of impact. Then enormous pressure. The greatsword, iron spear and all, split straight through my waist— “…Huh?” The iron spear was fine. So was my waist. All that had happened was my feet had been pushed back a little. A very, very little. “…?” What was this? —G-Grrk? The Hobgoblin Great Warrior’s face flushed bright red. It pulled the greatsword back and smashed it against the iron spear again. Even through my confusion, I tightened my grip and blocked. Boom! My body slid back. Maybe thirty centimeters? “…Uhh.” —…Grrk. The Hobgoblin Great Warrior’s eyes met mine in the air between us. I’d been through this somewhere before. *That’s right. The duel with Lee Seogeun. It was exactly like this.* I’d freaked out after seeing his Level and thought I was dead, only to discover that he was a complete pushover. How could I forget a moment that absurd? *But I had the System backing me there.* This was reality. I was an F-rank Hunter with nothing. No System, no nothing. *How the hell is this…* Ding. “Huh?” I froze. For that instant, I couldn’t see or hear anything. This can’t be. This seriously makes no sense. Ding. > **System** > > Synchronization complete. > > All systems are inherited. And yet, it actually happened. “Ha… hahaha.” A laugh slipped out of me like I’d lost my mind. The Hobgoblin Great Warrior stared at me like I was the crazy one. > **System** > > Lv. 45 Hobgoblin Great Warrior Right. So that was how it was. “I don’t know what the hell just happened…” I grinned at the monster. “But you’re fucking dead.” * * * Gurgle. A wrinkled hand clutched at its throat. But the old goblin had neither the strength to stop the blood pouring out like a waterfall nor the time to spit out the spell still hovering on the tip of its tongue. “What a nuisance.” With that from Team Leader Choi, the light went out of the Hobgoblin Priest’s eyes. *I’m tired.* But he turned around at once. He still had work to do. There was no telling how brutal the fight against a C-rank Rare Monster would be— Slash— “Kuwaaaaargh!” Team Leader Choi thought he was seeing things. That same Hobgoblin Great Warrior was screaming. One arm severed, it was staggering back. *Who did that?* He watched the fight, even forgetting he was supposed to help. Ghostlike movement. A spear-point pouring like water, carving the green giant to pieces. Wait. A spear? Of everyone gathered here today, only one person used a spear. *The porter—no, Jin Taekyung?* It was him. The F-rank Hunter who’d been carrying a backpack and skinning hides! “What on earth…” Team Leader Choi’s mouth slowly fell open. “What’s going on?”

#### Chapter 45 tail (verified mastered)

…
but every piece of gear I had is ruined.” “…” “The armor that protected me for seven years—and now even my spear.” “The spear looks perfectly—” Right then, I pressed down steadily on the middle of the spear with one foot. Under the majesty of a three-digit Strength stat, the iron spear bent like a stick of taffy. “Looks perfectly fine? This?” “…” Team Leader Choi shut his mouth. * * * As the person in charge, Team Leader Choi was called away by the dispatched officials, and the other four were moved to an ambulance for treatment. Instead of the musty break room, I was left alone in a spacious, comfortable office. Now that the moment had actually come, my heart started pounding. *St-Status Window?* At that half-doubtful call, the System answered. Ding. > **System** > > **Status Window** > > **Lv. 33 Jin Taekyung** > > **Job:** First Rate Martial Artist > > **Fame:** 0 > > **Titles:** 2 (Title effects active) > > - Novice Trainee (Training speed +10%) > - Gambler (Combat-related stats +10% in one-on-one matches) > > **Strength:** 120 **Stamina:** 125 > > **Agility:** 121 **Intelligence:** 20 > > **Charm:** 20 **Internal Energy:** 15 years > > **Remaining Points:** 30 > > Synchronization is complete. Changes have occurred to Titles and Fame. “Fuck. It really came up.” I stared blankly at the Status Window for a moment before noticing something strange. *The Status Window… changed?* The first two things that jumped out were Fame reset to zero and the missing Title. The last line gave me a rough idea why. *Because this isn’t Murim?* All five hundred Fame I’d stacked had been earned as a martial artist in Murim. The Title that had vanished, *Scion of a Prestigious Family*, made sense the same way. *Well, I’m not the son of some prestigious family here. And I’m definitely no Sleeping Dragon.* If I were getting a Title here, it’d obviously be something like *Scion of the Common Folk*, or *Earthworm* instead of Sleeping Dragon. “How much else changed?” For about ten minutes I turned every System function on and off one by one and tested them. The only thing that had changed was the Status Window. No—there was one more. The Quest Window. Ding. > **System** > > **Quest** > > **Traitor** > > You have discovered the traitor’s identity. Rejoin the main force, inform them that there is a traitor, and lead the battle to victory! > > **Grade:** Peak > > **Restriction:** Jin Taekyung > > **Mission:** Eliminate the traitor (Incomplete) > > Battle victory (Incomplete) > > **Reward:** Vast EXP and Fame > > Valuable iron chest > > **Failure:** Death It was the Chain Quest I’d received after killing Gwak Jun and the assassins. My thoughts grew tangled. *Am I supposed to go back? To Murim?* I knew it now. The Murim I’d been through wasn’t an illusion, and it wasn’t a game. A wildly unrealistic story, sure, but Murim was probably… Creak. I turned at the sudden sound. Team Leader Choi was standing in the doorway. “Let’s go, Mr. Taekyung.” Looked like the talk had wrapped up. I folded the thought away and stood. “The others…?” “They should be on their way to the hospital by now. They’ll need to stay for about a week. You don’t need to worry.” I wasn’t particularly worried. They had the sturdy bodies of combat-type Hunters, not to mention potions and healing magic. They would be back on their feet soon enough. And… “How did it go?” “They’ll contact us again in a few days. An investigator will probably visit you as well.” An investigator. Not a type I wanted to run into again. But that wasn’t the answer I’d wanted, so I asked again. “What about the other thing?” “Hmm.” Team Leader Choi looked at me with an odd expression. Like he was studying some fascinating animal. *Did he tell them the truth?* I didn’t want my strength out in the open. Even less now, when I still barely knew why I could see the System in reality, or what it had to do with Murim. An F-rank Hunter killing a C-rank Rare Monster alone was unheard of. An awl in a bag pokes through. I’d lived the opposite kind of life, nothing sticking out, so I had to be careful. So I’d asked him: "Could you keep anything about me a secret?" It must have been a difficult request for Team Leader Choi. I was asking him to give a false statement for someone he’d only just met. “Mr. Jin Taekyung.” “Yes.” His heavy voice made my heart grow heavy with it—and then: “Let’s get some food.” “What?” “Look.” Team Leader Choi held out his wrist. A glittering Magic Gem electronic watch pointed to two in the afternoon. “It’s an N Company model carved from a whole C-rank Magic Gem. It’s enchanted with enhancement magic, so in an emergency, you can even use it as a shield—” *So that’s where he was going.* “…Let’s go.” Impossible man to read. “Let’s get some meat. Do you like Hanwoo?[^1]” “Hanwoo?” “Yes. Highest grade.” And rich, too. “I can never get enough of it.” Not just any beef. Hanwoo. Top-grade Hanwoo at that. System or whatever—first I had to fill a hungry stomach. [^1]: Hanwoo is beef from Korean native cattle, prized as premium meat.

## Korean source

```text
＃46화



치이이익.

불판 위에 고기가 올라갔다. 붉고 두툼한, 마블링이 흰 눈꽃처럼 올올이 박혀 있는 최고급 한우다.

형태, 소리, 냄새. 모두 황홀했다. 한 가지 마음에 안 드는 건 가격이었지만…….

“이걸로 되겠어요? 먹고 더 시키죠. 특수 부위로.”

돈 많은 C급 헌터님이 내는 거니까, 뭐.

‘이게 얼마 만의 한우냐.’

무림의 음식은 맵고 짜고 싱겁다. 그마저도 제대로 못 먹는 날이 더 많았다. 30일간 내 위장은 육포와 벽곡단, 주먹밥으로 혹사당했다.

우걱. 우걱우걱.

소고기의 좋은 점은 금방 먹을 수 있다는 거다. 대충 익었다 싶으면 그대로 입으로 직행.

한번 씹을 때마다 구름 위를 걷는 기분이다. 이것도, 요것도, 저것도, 하나같이 천국의 맛이다.

“흐어어.”

그런 나를, 최 팀장은 특유의 묘한 표정으로 바라봤다.

“더 드실래요?”

“아뇨. 과식은 자제해야죠.”

“지금 25인분짼데…….”

“각자 12인분이면 그렇게 많지도 않네요.”

“전 3인분밖에 안 먹었습니다.”

“아, 육회 시켜도 돼요?”

“……네.”

“공깃밥도.”

“…….”

그렇게 폭풍 같은 식사가 끝난 뒤. 드디어 최 팀장의 입이 열렸다.

“제가 잡았다고 했습니다. 제사장과 대전사, 둘 다.”

“아, 감사합니다.”

“천만에요. 정당한 거래라고 해 둡시다. 오히려 제가 감사한 부분도 있죠.”

정당한 거래라.

맞는 말이다. 나는 생각할 시간을 벌었고, 그는 명성을 얻게 될 것이다. 하급 헌터 다섯을 데리고 중급 레어 몬스터를 둘이나 잡았으니까.

그 과정에서 사망자 하나 나오지 않았다는 사실은 길드 홍보에도 큰 도움이 될 테고.

‘만약 내가 동기화로 힘을 찾지 못했다면?’

글쎄, 누군가는 죽지 않았을까 싶다. 어쩌면 아무도 살아 나오지 못했을 수도 있고.

“이미 그렇게 생각하고 계셨군요.”

마냥 괴짜는 아니다. 이렇게 눈치가 빠른 걸 보면.

나는 어색하게 웃었다.

“서로에게 좋은 일이니까요.”

“서로에게 좋다. 서로에게…….”

중얼거리던 최 팀장이 불쑥 물었다.

“길드 가입하실래요?”

“푸웁.”

식탁보를 들어 물을 막아 낸 최 팀장이 세련된 솜씨로 명함 한 장을 꺼냈다.



[평화 길드 1팀장 최민우]



뭐야, 이거. 순간 엄청 당황했다.

“스, 스카우트 제의하신 건가요. 지금?”

“그렇죠. 인재는 항상 필요하니까.”

명함을 받아 든 나는 왠지 감개무량해졌다.

새우처럼 허리 굽히고 다니면서 면접 보던 게 엊그제 같은데…….

‘오래 살다 보니 별일이 다 있네.’

무려 인재 취급받으면서 스카우트 제의라니. F급 헌터 진태경, 많이 컸다.

“우리 길드가 아직 신생이고 인원수도 적긴 합니다만, 실속이 매우 훌륭합니다. 음, 예를 들자면…….”

최 팀장이 우아하게 와인잔을 흔들었다. 세상에 저건 또 언제 시켰대.

“재정이 굉장히 탄탄하죠.”

“오오, 재정!”

“그렇다 보니 직원 복지도 좋고요.”

“오오, 탄탄한 재정을 바탕으로 한 복지!”

“길드장님은 B급 헌터시고.”

“오오, 탄탄한 재정의 원천인 상위 헌터!”

“구조 조정 걱정은 없습니다.”

“오오, 안정된 직장!”

최 팀장이 부유한 미소를 머금고 물었다.

“오시겠습니까?”

나는 머리를 긁적였다.

“아뇨. 그건 좀.”

“……예?”

“제가, 당장은 곤란한 사정이 있어서요. 시간이 필요합니다.”

마음 같아서는 당장 계약서에 싸인, 도장, 지장, 키스 마크까지 남기고 싶다.

‘하지만 내일 당장 시스템이 사라져 버리면?’

바로 개털이다.

하루아침에 인재(人才)에서 인재(人災) 소리 듣게 되는 거지.

“혹시 돈 문제입니까?”

돈 문제야 항상 있지.

하지만 이건 더 중요한 문제다. 당장 눈앞의 돈뭉치에 홀려서 덥석 결정할 수 없다.

“말씀드리기가 어렵네요. 아쉽지만 지금 당장 결정할 문제가 아닌…….”

“일억.”

“억?”

“순수 계약금만. 나머지는 최소 C급 헌터 조건으로 맞춰 드리죠.”

위험했다. 이번엔 진짜 위험했어.

그러나 나는 초인적인 인내심으로 참았다. 세상살이가 그렇게 호락호락한 게 아니라는 건 진즉 깨닫지 않았나.

먹고 체하는 돈이 될 수도 있다.

“죄송합니다.”

나를 물끄러미 바라보던 최 팀장은 이내 고개를 끄덕였다.

“연락 기다리겠습니다.”



* * *



한 사람은 떠나고, 한 사람은 남았다.

최 팀장, 아니 최민우는 진태경이 떠난 자리를 말없이 바라보다가 핸드폰을 꺼냈다.

뚜, 뚜, 달칵.

- 이 자식, 귀신이네. 안 그래도 연락하려고 했는데.

“아까 말한 거, 어떻게 됐어?”

- 일단 네 부탁이니까 알아보긴 했는데…… 이 진태경이라는 사람, 뭐 있냐?

“그게 궁금해서 너한테 연락한 거지. 그래서 결과는?”

- 널리고 널린 케이스지 뭐. 7년 전 스무 살에 각성, 측정 결과 F급. 헌터 훈련소에서 수석으로 수료한 기록이 있고…….

수화기 너머로 진태경의 지난 7년이 흘러나왔다. 그러던 어느 순간, 최민우의 눈썹이 꿈틀했다.

“뭐? 상동역 변이 게이트?”

- 어. 너도 그 사건 알지?

모를 리가 있나. 불과 2년 전의 일이라 최민우도 똑똑히 기억하고 있었다.

- 그 사건 유일한 생존자더라고. 그 부분은 나도 확인하고 좀 놀랐다.

최민우는 물잔을 기울였다. 중급 레어 몬스터를 단신으로 잡은 F급 헌터, 그 실마리를 잡았다고 생각하니 목이 탔다.

“그리고?

- 반년 동안 휴직. 관리청 쪽에서 조사관들 수시로 보내고, 뭐 이래저래 마음도 추스르고 했나 보더라고. 너도 알다시피 사안이 좀 컸으니까.

“그래서?”

- 그게 끝. 다시 길드 복직해서 일 년 반 동안 좆 빠지게 게이트 돌다가 잘렸어. 그게 딱 사흘 전이고.

“잘린 이유는?”

- 일단 구조 조정이긴 한데…… 코딱지만 한 중소 길드가 무슨. 아마 그 사건 영향이 클 거야. 관리청 눈치 슬금슬금 보다가 내보낸 거지. 그쪽 입장에서는 껄끄러울 테니까.

“그게 끝이야?”

- 내가 보기에는. 따로 파일 보내 줘?

“바로 보내. 그럼 끊는다.”

- 야, 야!

뚝.

최민우는 긴 손가락으로 탁자를 두드렸다.

진태경. F급 헌터. 상동역 변이 게이트의 유일한 생존자.

그리고…….

‘최소 C급 헌터.’

말 그대로 최소로 잡았을 때의 이야기다. C급 레어 몬스터를 혼자, 그것도 압도적인 힘과 기술로 몰아붙이던 그 모습이 눈앞에 아른거렸다.

‘그런데 F급이란 말이지.’

둘 중 하나다. 힘을 숨겼거나, 최근 재각성을 했거나.

최민우는 후자라고 짐작했지만, 그것 역시 상식을 벗어난 일임에는 변함이 없었다.

평생 승급 한 번 못 해 보고 은퇴하는 헌터가 한둘인가.

F급에서 C급으로의 재각성은, 단언컨대 극히 드문 일이다.

‘이게 무슨 게임도 아니고. 도대체 정체가 뭐야?’

최민우는 고개를 저었다. 귀신에 홀린 기분이다.

‘좀 더 알아봐야겠군.’

자리에서 일어나는 그에게 사장이 다가와 계산서를 내밀었다.

“193만 7천 원입니다.”

“…….”

정말 귀신에 홀린 기분이다.



* * *



“시바, 좆 됐다.”

나는 털썩 주저앉았다. 너저분한 분리수거장. 응당 있어야 할 물건이 보이지 않았다.

“없다, 없어. 내 캡슐이 없어.”

최 팀장과 헤어질 때부터 초조하긴 했다. 하지만 반나절도 안 돼서 누가 가져갈 줄이야. 나는 허공을 향해 부르짖었다.

“어떤 새끼야!”

그리고 대답이 들려왔다.

“나다, 이 십새끼야.”

고시원 건물 옥상. 아침에 봤던 그 자리에서 진호 형이 담배를 피우고 있었다. 뭔가 아련한 표정으로 담배 연기를 뿜어낸 그가 말을 이었다.

“내가 10년 동안 울면서 후회하고 다짐했는데…….”

“진짜 울면서 후회하게 해 줘?”

“재미없는 새끼. 너 이 영화 모르지?”

“장난치지 마. 지금 심각하니까.”

“왜, 오늘 허탕 쳤냐.”

“아니.”

나는 힘이 쭉 빠진 목소리로 말을 이었다.

“캡슐.”

“……엉?”

“어떤 새끼가 내 캡슐 가져갔어.”

“콜록, 콜록콜록!”

담배 연기를 잘못 빨아들였는지 미친 듯이 기침하던 진호 형이 겨우 말문을 열었다.

“그, 필요 없어서 버린 거 아니냐?”

“그랬지.”

시스템이 돌아오기 전까지는.

불과 몇 시간 만에 상황이 이렇게 변하리라곤 나도 생각하지 못했다.

‘하루만 더 갖고 있을걸.’

어디서부터 찾아야 하나. 나는 한숨을 푹 내쉬었다.

“형, 혹시 누가 가져갔는지 못 봤지?”

“어…… 그게.”

진호 형이 머리를 긁적였다.

“봤다면 본 거고. 못 봤다면 못 본 건데.”

이게 말이냐, 똥이냐.

내가 노려보자 그가 쑥스럽다는 듯 웃었다.

“그 뭐냐, 내가 사례금 같은 걸 바라는 건 절대 아니고…….”

사례금을 바라는 게 절대 맞는 것 같은데.

아무튼 그게 중요한 게 아니다. 나는 벌떡 일어나 물었다.

“봤어? 확실해?”

“굳이 따지자면 본 쪽이지.”

“누구? 어디로 갔어!”

“사례금을 바라는 건 아니지만, 예상 금액은 어느 정도?”

“……10만 원?”

“어이구, 나도 나이가 들었나. 기억이 가물가물하네.”

“이런 시팔.”

“그래, 날 더운데 수고해라.”

“사례금은 십팔만 원입니다.”

금액이 마음에 드는지 진호 형이 환하게 웃었다.

“네 캡슐. 내가 주웠다.”

“……?”

이해하는 데 딱 3초 걸렸다.

‘이런 날강도 같은 인간을 봤나.’

기가 막히고 코가 막힌다. 이런 식으로 사람 뒤통수를 쳐?

“근데 마땅히 놔둘 데가 없더라고. 내 방에 놓기에는 너무 좁잖아.”

“그래서?”

“네 방에 다시 놔뒀어. 잘했지?”

저 인간을 어떻게 때려야 야무지게 때렸다고 소문이 날까.

나는 주먹을 부르르 떨었다.



* * *



“진짜 있네.”

아무 일도 없던 것처럼 원룸 절반을 차지한 캡슐을 보니 헛웃음만 나왔다.

‘이걸 운이 좋다고 해야 하나.’

그 많은 사람 중에서 캡슐을 가져간 게 진호 형이라니.

나는 캡슐 뚜껑을 열었다. 낡은 좌석에 던지듯 넣어 놓은 사용 설명서를 집어 들어 마지막 페이지를 펼쳤다.



[주요 기능]

- 한 사람만을 위한 맞춤형 캡슐! 사용자 등록 시 캡슐이 영구 귀속되며, 이는 사망 전까지 유효합니다.



……에이, 설마.

‘단순한 우연이겠지.’

하지만 찜찜함이 가시지 않는다. 나는 이 모든 사건의 근원인 캡슐을 노려보았다.

‘이거 뭐 하는 물건이야?’

오늘 아침 캡슐을 분리수거장에 버렸던 이유는 다 잊기 위함이었다. 가뜩이나 퍽퍽한 인생, 악몽 한 번 꿨다 생각하고 지금처럼 내 인생을 살기 위해서.

하지만 이제는 상황이 달라졌다.

‘시스템이 생겼으니까.’

시스템이라…….

그때 문득 생각나는 게 있었다. 나는 캡슐 표면에 손을 올리고 중얼거렸다.

“아이템 확인.”

띠링.

그럼 그렇지. 입꼬리가 올라간 그 순간이었다.



- 해당 아이템을 읽을 수 없습니다.



“……읽을 수 없다고?”

이런 경우는 처음이다.

‘무림이 아니라서 그런가?’

나는 당황스러운 마음에 방 안의 물건들을 닥치는 대로 확인했다. TV부터 볼펜, 심지어는 베개까지. 그때마다 시스템은 정확한 정보를 표시해 줬다.

그런데 딱 하나. 캡슐만큼은 읽을 수 없다.

“와, 이거 골 때리네.”

혹시 싶어 사용 설명서를 집어 들었지만 역시나.

띠링.



- 해당 아이템을 읽을 수 없습니다.



나는 침대에 벌렁 드러누웠다. 낡고 누렇게 찌든 천장을 멍하니 바라보며 생각했다.

‘무슨 일이 벌어지고 있는 거야?’

현재로서는 이해할 수 없는 일들이다. 하지만 한 가지는 확실했다.

‘나는 강해졌다. 비교할 수 없을 정도로.’

전신에 올올이 스며든 힘. 단전에서 꿈틀거리는 공력.

동기화를 거침으로써 내게는 힘이 생겼다. F급 헌터를 아득히 뛰어넘는 힘. 혼자서 C급 레어 몬스터를 쓰러트릴 수 있는 힘이.



‘길드 가입하실래요?’



난생처음 받아 본 스카우트 제의. 하지만 거절했다. 누군가 나를 인정해 준다는 사실에 기쁨보다 두려움이 앞서서.

‘그럴 만도 하지.’

F급 헌터라는 이름으로 7년을 버텼다. 흙바닥만 기어 다니던 애벌레에게 어느 날 시스템이라는 날개가 생긴 것이다.

두려움은 당연한 감정이다.

‘하지만 이 힘을, 시스템을 계속해서 쓸 수 있다면?’

상상만으로도 심장이 쿵쿵 뛰었다.

동시에 지난 7년의 시간이 머릿속을 스쳤다. 미친 듯이 노력했음에도 낙인처럼 찍혀 있던 F급이라는 이름. 타인들의 무시와 죄책감과 무력감에 몸을 떨어야 했던 2년 전의 기억까지.

“시발…….”

더 이상은 못 참겠다. 나는 자리에서 벌떡 일어났다. 곧장 고시원을 뛰쳐나와 지나가던 택시를 붙잡았다.

“어디로 모실까요?”

목적지는 이미 정해져 있었다.

“헌터 협회 부천 지부로 가주세요.”

헌터 등급 재측정.

F급 헌터. 오랫동안 나를 괴롭혀 온 이 지긋지긋한 족쇄를 끊어 내는 것부터 시작이다.

‘어디 한번 해 보자고.’

주먹을 불끈 움켜쥔 내게 택시 기사가 말했다.

“이거 서울 택신데요.”

“아.”
```

## Current accepted English baseline

```markdown
# Chapter 46

Sizzle.

The meat hit the grill. Thick, red, and marbled with white streaks like snowflakes—it was the finest Hanwoo beef.

The shape, the sound, the smell. All of it was intoxicating. The only thing I didn’t like was the price…

“Will this be enough? Let’s order more after we eat. Some special cuts, too.”

A rich C-rank Hunter was paying, so whatever.

*How long had it been since I’d last had Hanwoo?*

Food in Murim was spicy, salty, and bland. And even then, more days than not, I couldn’t eat properly. For thirty days, my stomach had been abused with beef jerky, bigu pills,[^1] and rice balls.

Chomp. Chomp-chomp.

The best thing about beef was how quickly you could eat it. The moment it looked more or less done, it went straight into my mouth.

Every chew felt like walking on clouds. This piece, that piece, that one too—every last one tasted like heaven.

“Hnnngh.”

Team Leader Choi watched me with that peculiar look of his.

“Would you like some more?”

“No. I should hold back on overeating.”

“We’re at twenty-five servings…”

“Twelve servings each isn’t all that much.”

“I’ve only eaten three servings.”

“Oh, can we order some yukhoe?[^2]”

“…Yes.”

“Rice, too.”

“…”

And so that storm of a meal came to an end. At last, Team Leader Choi opened his mouth.

“I said I was the one who killed them. The Priest and the Great Warrior, both.”

“Oh. Thank you.”

“Don’t mention it. Let’s call it a fair deal. If anything, there’s something I should thank you for, too.”

A fair deal.

He wasn’t wrong. I’d bought myself time to think, and he would gain a reputation. After all, he had led five low-rank Hunters and killed two mid-grade Rare Monsters.

The fact that nobody had died in the process would be a huge help for Guild publicity, too.

*What if I hadn’t found my strength through Synchronization?*

Who knew? Someone probably would have died. Maybe nobody would have made it out alive.

“You were already thinking along those lines.”

He wasn’t just some eccentric. Not with instincts that sharp.

I smiled awkwardly.

“It’s good for both of us.”

“Good for both of us. Both of us…”

Team Leader Choi muttered to himself, then asked out of nowhere,

“Would you like to join the Guild?”

“Pffft.”

Team Leader Choi lifted the tablecloth and blocked the water, then smoothly produced a business card with practiced elegance.

> **Peace Guild, Team 1 Leader Choi Minwoo**

What the hell was this? For a second I was completely thrown.

“Y-you’re making me a recruitment offer? Right now?”

“That’s right. We always need talent.”

I took the card, and for some reason I felt deeply moved.

It seemed like only yesterday that I’d been going to interviews with my back bent like a shrimp…

*Live long enough and you really do see everything.*

An actual recruitment offer, treating me like talent. F-rank Hunter Jin Taekyung, you’d come a long way.

“Our Guild is still new, and we don’t have many people, but we’re excellent where it counts. For example…”

Team Leader Choi elegantly swirled his wineglass. When had he even ordered that?

“Our finances are extremely solid.”

“Oh, finances!”

“And because of that, our employee benefits are excellent.”

“Oh, benefits based on solid finances!”

“Our Guild Master is a B-rank Hunter.”

“Oh, a high-ranking Hunter—the source of those solid finances!”

“There’s no need to worry about restructuring.”

“Oh, a stable workplace!”

Team Leader Choi asked with an affluent smile,

“Will you come?”

I scratched my head.

“No. That’s a little…”

“…Pardon?”

“I have some circumstances that make it difficult right now. I need time.”

If I followed my heart, I wanted to sign the contract right away—signature, stamp, thumbprint, even a kiss mark.

*But what if the System vanished tomorrow?*

I’d be dead broke.

Overnight, I’d go from being called talent to being called a human disaster.[^3]

“Is it a money problem?”

There was always a money problem.

But this was more important than that. I couldn’t get dazzled by the wad of cash right in front of me and snatch at it.

“It’s difficult to explain. I’m sorry, but this isn’t something I can decide right now…”

“100 million won.”

“100 million?”

“Just the signing bonus. The rest will match the minimum terms for a C-rank Hunter.”

That was dangerous. This time it was really dangerous.

But I held out with superhuman patience. Hadn’t I already learned that life wasn’t that easy?

It could be money I’d end up choking on.

“I’m sorry.”

Team Leader Choi looked at me quietly, then nodded.

“I’ll wait for your call.”

* * *

One person left, and one person stayed.

Team Leader Choi—no, Choi Minwoo—looked in silence at the seat Jin Taekyung had left, then took out his phone.

Beep. Beep. Click.

“—You bastard, you’re a ghost. I was just about to call you.”

“How did that thing I asked about turn out?”

“—I looked into it because you asked, but… is there something about this Jin Taekyung guy?”

“That’s why I called you. So? What did you find?”

“—It’s a dime-a-dozen case. Seven years ago he Awakened at twenty and was assessed as F-rank. There’s a record he finished first at the Hunter training center…”

Jin Taekyung’s past seven years spilled from the other end of the phone. Then, at one point, Choi Minwoo’s eyebrows twitched.

“What? The Sangdong Station Mutated Gate?”

“—Yeah. You know about that incident, right?”

How could he not? It had happened only two years ago, so Choi Minwoo remembered it clearly.

“—He was the only survivor. I checked that part myself, and it surprised me, too.”

Choi Minwoo tipped his glass of water. Thinking he’d grabbed a lead on how an F-rank Hunter had killed a mid-grade Rare Monster alone made his throat burn.

“And?”

“—He took six months off. The Hunter Administration kept sending investigators, and I guess he spent the time trying to get himself back together. You know how serious the incident was.”

“And then?”

“—That’s it. He went back to his Guild, ran Gates his ass off for a year and a half, then got fired. That was exactly three days ago.”

“Why was he fired?”

“—It was technically restructuring, but a booger-sized little Guild, restructuring? Please. The incident probably had a lot to do with it. They kept glancing nervously at the Administration, then pushed him out. From their perspective, he’d have been awkward to keep around.”

“That’s all?”

“—As far as I can tell. Want me to send you the file separately?”

“Send it now. I’m hanging up.”

“—Hey, hey!”

Click.

Choi Minwoo tapped the table with his long fingers.

Jin Taekyung. F-rank Hunter. The sole survivor of the Sangdong Station Mutated Gate.

And…

*At least a C-rank Hunter.*

That was the absolute minimum. The image of Taekyung driving a C-rank Rare Monster into a corner alone, with overwhelming strength and skill, kept flickering before his eyes.

*And yet he’s F-rank.*

There were only two possibilities. He had been hiding his strength, or he had recently reawakened.

Choi Minwoo suspected the latter, but that was still far beyond common sense.

It wasn’t as if only one or two Hunters retired without ever ranking up even once.

Reawakening from F-rank to C-rank was, without question, extraordinarily rare.

*This isn’t some kind of game. What the hell is he?*

Choi Minwoo shook his head. He felt as if a ghost had possessed him.

*I’ll have to look into this further.*

As he rose from his seat, the restaurant owner approached and held out the bill.

“1,937,000 won.”

“…”

He really did feel as if a ghost had possessed him.

* * *

“Shit. I’m fucked.”

I dropped heavily onto the ground. The recycling area was a mess. The thing that should have been there was nowhere to be seen.

“It’s gone. It’s gone. My capsule is gone.”

I’d been anxious ever since leaving Team Leader Choi. But I hadn’t expected someone to take it in less than half a day. I shouted into the empty air.

“Who the fuck was it?!”

And I got an answer.

“Me, you son of a bitch.”

On the roof of the goshiwon building,[^4] Jinho hyung was smoking in the same spot where I’d seen him that morning. He exhaled a plume of smoke with a wistful look, then went on.

“I spent ten years crying, regretting it, and making vows…”

“You want me to make you really cry and regret it?”

“You’re no fun. You haven’t seen this movie, have you?”

“Quit joking around. This is serious.”

“What, you come up empty today?”

“No.”

My voice drained of strength as I went on.

“The capsule.”

“…Huh?”

“Some bastard took my capsule.”

“Cough, cough-cough!”

Maybe he’d inhaled the cigarette smoke wrong. Jinho hyung coughed like a maniac before he finally managed to speak.

“D-didn’t you throw it away because you didn’t need it?”

“I did.”

Until the System came back.

I hadn’t expected the situation to change this much in just a few hours.

*I should’ve kept it for one more day.*

Where was I even supposed to start looking? I sighed heavily.

“Hyung, you didn’t happen to see who took it, did you?”

“Uh… well.”

Jinho hyung scratched his head.

“If I saw it, then I saw it. If I didn’t, then I didn’t.”

Was that even an answer, or just crap?

When I glared at him, he smiled sheepishly.

“Look, it’s not that I want a finder’s fee or anything…”

It definitely sounded like he wanted a finder’s fee.

Anyway, that wasn’t the point. I shot to my feet and asked,

“You saw them? You’re sure?”

“If I have to pick, I saw them.”

“Who? Where did they go?”

“I’m not asking for a finder’s fee, but what’s the expected amount, roughly?”

“…100,000 won?”

“Oh, dear. Maybe I’m getting old. My memory’s a little hazy.”

“For fuck’s sake.”

“Right. It’s hot out, so good luck with that.”

“The finder’s fee is 180,000 won.”[^5]

Apparently satisfied with the amount, Jinho hyung broke into a bright smile.

“Your capsule. I picked it up.”

“…?”

It took me exactly three seconds to understand.

*Have you ever seen a daylight robber like this?*

I was so dumbfounded I couldn’t even breathe. He’d hit me in the back of the head like this?

“But there wasn’t anywhere suitable to put it. My room’s too small, you know.”

“So?”

“I put it back in your room. I did good, right?”

How was I supposed to hit this guy so cleanly that people would say I’d really done it right?

I clenched my fists until they shook.

* * *

“It really is here.”

Seeing the capsule taking up half the studio as if nothing had happened, all I could do was let out a hollow laugh.

*Should I call this lucky?*

Of all the people in the world, Jinho hyung had taken the capsule.

I opened the capsule lid. Then I picked up the user manual, which had been tossed onto the worn seat, and flipped to the last page.

> **Main Features**
>
> - A customized capsule for one person! Once a user is registered, the capsule becomes permanently bound to that user and remains so until their death.

…Come on. No way.

*It has to be a simple coincidence.*

But I couldn’t shake the unease. I stared at the capsule, the source of all these events.

*What even is this thing?*

The reason I’d thrown the capsule into the recycling area that morning was so I could forget everything. My life was already dry enough; I wanted to write it off as one nightmare and keep living my life as I was.

But the situation had changed now.

*Because the System is here.*

The System…

Then something occurred to me. I placed my hand on the surface of the capsule and murmured,

“Item check.”

Ding.

Just as I thought. The corners of my mouth had just begun to rise when—

> **System**
>
> This Item cannot be read.

“…It can’t be read?”

This had never happened before.

*Is it because I’m not in Murim?*

Flustered, I checked every object in the room at random. The television, a ballpoint pen, even the pillow. Every time, the System displayed accurate information.

But there was one exception.

The capsule couldn’t be read.

“Wow. This is driving me nuts.”

Just in case, I picked up the user manual. Same result.

Ding.

> **System**
>
> This Item cannot be read.

I flopped onto the bed. I stared blankly at the old, yellow-stained ceiling and thought.

*What’s going on?*

For now, these were things I couldn’t understand. But one thing was certain.

*I’ve become stronger. Incomparably stronger.*

Power had soaked into every fiber of my body. Internal energy writhed in my dantian.

Synchronization had given me strength. Strength far beyond that of an F-rank Hunter. Strength enough to defeat a C-rank Rare Monster alone.

*Would you like to join the Guild?*

It was the first recruitment offer I’d ever received. But I refused. When someone recognized me, fear had come before joy.

*Can’t blame me.*

I’d endured seven years under the name of F-rank Hunter. A caterpillar that had only ever crawled through the dirt had, one day, grown wings called the System.

Fear was a natural feeling.

*But what if I can keep using this power—keep using the System?*

My heart pounded at the mere thought.

At the same time, the past seven years flashed through my mind. The name F-rank, stamped on me like a brand despite all the insane effort I’d put in. Even the memories from two years ago, when I’d trembled at other people’s contempt, at the guilt and the helplessness.

“Fuck…”

I couldn’t take it anymore. I shot to my feet, burst out of the goshiwon, and flagged down a passing taxi.

“Where would you like to go?”

I already knew the destination.

“Take me to the Bucheon Branch of the Hunter Association.”

A Hunter rank reassessment.

An F-rank Hunter. I’d start by breaking this loathsome shackle that had tormented me for so long.

*Let’s give it a shot.*

As I clenched my fist, the taxi driver said,

“This is a Seoul taxi.”

“Oh.”

[^1]: Bigu pills are traditional fasting pills said to sustain the body without ordinary food.

[^2]: Yukhoe is seasoned Korean raw beef.

[^3]: The Korean words for “talent” and “human disaster” share the same pronunciation, though they use different characters.

[^4]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.

[^5]: In Korean, *sip-pal* (“eighteen”) echoes the swear he just used, and he switches abruptly to stiff politeness.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 46`.

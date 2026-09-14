# Master Edit Task — Chapter 50

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
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 창법     | **spear technique**                              |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 진가창법   | **Jin Family's Spear Technique**       |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 장비               | **Equipment**                  |
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 김상호 | **Kim Sangho** |
| 김상식 | **Kim Sangshik** |
| 대한민국 | **Korea** | Country reference. |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 45–49

## Plot

Taekyung kills the Level 45 Hobgoblin Great Warrior after Character Synchronization restores his System in reality. His Status Window shows Level 33, First Rate Martial Artist, powerful renewed stats, fifteen years of Internal Energy, and the incomplete Traitor Chain Quest. Officials investigate how two C-rank Rare Monsters appeared in an E-rank Gate, while Taekyung asks Team Leader Choi to conceal his strength.

Choi offers Taekyung a 100 million won Peace Guild position, but Taekyung refuses a long-term contract because he fears the System may disappear. After recovering the Ark - 2020 capsule from Seong Jinho, Taekyung confirms that its manual binds it permanently to its user and that the System cannot read either the capsule or manual. He visits the Hunter Association for reassessment, where his former boss Kim Sangshik confronts him. Taekyung effortlessly crushes Kim’s wrist when Kim grabs him, but the reassessment device malfunctions while scanning his Internal Energy.

The Association recognizes Taekyung as C-rank-level, prompting Guild recruitment offers. Taekyung rejects Kim’s apology and says he will consider Sopung Guild only if it removes someone he hates—clearly Kim. He tells Jinho a false account of his reawakening and the Gate, then becomes afflicted with Dead Drunk and dreams of indistinct Murim voices telling the youngest to survive. After detoxifying a Hangover through qi circulation, Taekyung signs a seven-day provisional contract with Peace Guild.

Choi takes Taekyung into a D-rank Gate alone after giving him expensive equipment. Taekyung equips a First Rate Lizardman Hunter’s Leather Set and Lizardman Slayer’s Harpoon. Choi reveals that he was already C-rank before a later reawakening, leading Taekyung to infer that Choi is at least B-rank. They enter the Gate together.

## Continuity

- The Hobgoblin Priest and Level 45 Hobgoblin Great Warrior are dead. Im Hyeokjun and the other veteran Hunters survived but require hospitalization.
- Taekyung’s restored System shows Level 33, First Rate Martial Artist, 120 Strength, 125 Stamina, 121 Agility, 20 Intelligence, 20 Charm, fifteen years of Internal Energy, and 30 Remaining Points.
- Fame is 0; Taekyung’s active Titles are Novice Trainee and Gambler. The Traitor Chain Quest remains incomplete and carries a death penalty for failure.
- Taekyung is recognized as C-rank-level but is not yet formally registered as a C-rank Hunter; the official reassessment takes several days.
- Taekyung has signed a seven-day provisional Peace Guild contract, not the offered one-year contract. He enters a D-rank Gate with Choi alone.
- Taekyung’s equipment includes the First Rate Lizardman Hunter’s Leather Set, whose Scale Armor effect activates when complete, and the Lizardman Slayer’s Harpoon, which can cause Bleeding.
- Choi was C-rank before reawakening. Taekyung infers that Choi is at least B-rank, but Choi’s exact current rank remains unknown.
- Kim Sangshik helped arrange Taekyung’s dismissal from Sopung Guild and is now threatened with expulsion if Sopung wants Taekyung’s consideration. Choi Min-su remains a C-rank Hunter with A-rank mana control whom Sopung is trying to recruit.
- Taekyung continues hiding Murim, the capsule’s true nature, and the System from Seong Jinho. The capsule remains permanently bound to Taekyung until death, and its purpose and route back to Murim are unresolved.
- Reality’s qi is weak and polluted. Murim’s death and resurrection limits, the Head Elder’s accomplice, the officials’ investigation, Taekyung’s formal registration, and the outcome of the D-rank raid remain unresolved.

## Translation Decisions

- Preserve **Character Synchronization**, **Synchronization complete**, and **All systems are inherited** exactly.
- Keep **First Rate Martial Artist**, **Internal Energy**, **Fame**, **Titles**, **Remaining Points**, **Dead Drunk**, and **Hangover** as established System terminology.
- Distinguish Hunter **rank** from System item **Grade**.
- Use **C-rank-level** for the Association’s provisional recognition until formal registration.
- Preserve **Peace Guild**, **Sopung Guild**, **Hunter Association**, **D-rank Gate**, **Lizardman Hunter’s Leather Set**, and **Lizardman Slayer’s Harpoon**.
- Retain Taekyung’s dry, self-mocking voice, Kim’s petty obsequiousness, Jinho’s emotional support and finder’s-fee jokes, and Choi’s measured dialogue.
- Preserve the exact unreadable-item notification **“This Item cannot be read.”** and the capsule’s permanent user-binding rule.
- Keep **young master**, **Black Ivory**, and the concise Pocheongcheon footnote.

### Prior accepted reading-copy tails

#### Chapter 48 tail (verified mastered)

…
a long story.” Jinho hyung chuckled and gripped the scissors. “And your life’s a short one?” Where was I even supposed to start? I had decided not to say anything more about the capsule. I figured it was better if, for Jinho hyung, it just stayed an absurd lie. “Two Rare Monsters showed up at the Gate today, and…” At a life-or-death moment, the luck of a reawakening had come, and I’d been able to take them down. Then I told him about the Association. It was a story hastily stitched together, but Jinho hyung bought it. “So now you’re a C-rank Hunter?” “The reassessment procedure will take a few days, so technically, not yet.” “Same thing, you idiot.” His face was dazed, his voice hoarse. Jinho hyung stared at me for a long moment. Moisture gathered in his eyes. *What’s gotten into this guy?* “…Don’t tell me you’re crying?” “The fuck I am. What kind of bullshit is that?” He turned away with an unnecessary curse, but he couldn’t hide the single tear that fell. I watched him out of the corner of my eye as he roughly rubbed his face with his sleeve. “Hyung?” “Turn the meat over. It’s burning.” “Changing the subject?” “I said it’s burning!” “Ah, all right.” Sizzle. As I turned the meat, I felt flustered, and yet a corner of my chest tickled. *Come to think of it, I’ve known Jinho hyung for a long time.* Six years? Seven? I didn’t know. I’d never counted. Whenever I came back to the goshiwon after a hard day, he had always been there. Sometimes I wondered if this was what it would have felt like to have a real older brother. We had lived like brothers, like friends. “Hey.” Jinho hyung broke the awkward silence. I turned the meat over one more time for no reason. “Yeah? What?” “Good for you.” “…Yeah.” “And…” His quiet voice followed. “You worked hard.” At just those words, something surged up from deep inside me. The emotions and memories that had stacked up over the past seven years all came rushing in at once. “Congratulations on becoming a C-rank Hunter. I guess I can’t tease you anymore.” “Hyung…” “Taekyung…” “Hyung!” “Taekyung!” We hugged each other tightly across the grill. Jinho hyung whispered in my ear, his voice shaking. “Do you remember what I said earlier?” “I know how you feel, hyung. Thank you.” “That’s not what I meant. The finder’s fee.” “…What?” “You have to pay me the finder’s fee. Hyung’s having a hard time these days.” “…” “You make a lot of money now.” Should I really kill him? * * * I staggered back to my room and threw myself onto the bed. A short laugh escaped me as I thought of the one person who was probably cleaning up the roof while grumbling. *You really can’t let your guard down around him.* That was Jinho hyung. The way he congratulated me, and that last prank. I knew it was all just his way of expressing himself. *You worked hard.* Those words kept circling in my head. It was embarrassing to admit, but at that moment, I’d almost cried. *Yeah. I really did work hard.* After my father died, I had run nonstop. I graduated high school while working part-time jobs, and I had to hold on and keep holding on for my sick mother and little sister. At some point, all of it had become a given. And then— Ding. > **System** > > - You have been afflicted with the Status Effect: Dead Drunk. > - It can be detoxified by circulating your qi. *Something that wasn’t a given had entered my life.* It had all started with that unidentified piece-of-junk game capsule. “A game capsule, huh?” I didn’t even know what to call the thing anymore. It had made me a C-rank Hunter, so should I call it a gift from God? No. Maybe it was a gift from the devil. *Is this really okay?* The reason I was thinking this even after the best day of my life was simple. *Nothing comes for free.* That was the world I knew. Everything had a price tag. Visible or not, sooner or later you had to pay. *How expensive is the System?* A hundred billion? A quadrillion? Maybe even more? I laughed weakly and felt my eyelids growing heavy. *Oh, right. I was dead drunk.* Chirp. Chirp-chirp. Outside the window, the grass insects chirped loudly. My vision darkened, and sleep poured over me. That night, I dreamed. I dreamed that somewhere deep in the mountains, someone was shaking me awake. “Squad Leader, Squad Leader!” Weirdly, just hearing it made me want to punch whoever it belonged to. Part of me wanted to see who that familiar voice belonged to, but I was too sleepy to open my eyes. “What do we do?” “We have to tell the main force right away…” “Why is the Squad Leader suddenly like this now of all times…” It felt like listening to a broken radio. The voices had static in them, and they kept cutting out. *I’m sleepy…* As my consciousness drifted farther away, I heard a small but clear voice. “Youngest, survive.” But when I woke the next day, I couldn’t remember any of it. [^2]: A pun: the Korean word for a goshiwon manager sounds like “prime minister.”

#### Chapter 49 tail (verified mastered)

…
it looks nice. *How rich do you have to be to think like that?* C-rank Hunters made good money, but Team Leader Choi’s spending was already beyond that. He must have been rich enough that money was never a concern. Gulp. “It might be better to rent from a rental shop. If I borrow something and it gets wrecked, it’d be kind of…” “They’re out of fashion, so it doesn’t matter.” Ah. So he even cares whether equipment is in fashion. I gave up thinking about it around there and picked my equipment. Having the System made it easy. *Item check.* Ding. > **System** > > **Item Window** > > Lizardman Hunter’s Leather Set > > **Type:** Armor > > **Grade:** First Rate > > **Restriction:** None > > **Description:** Made by stripping a lizardman’s hide off in one piece. > > Scale Armor activates when the full set is equipped. *This is pretty good.* It was light, and the leather was both tough and hard. Once I had everything on, the set effect Scale Armor activated. “Oh.” Green scales rose from the leather, densely covering my entire body. Team Leader Choi nodded at the sight of me. “You picked a good one. You’ve got a good eye.” *It’s the System that’s good.* I smiled awkwardly and rummaged through the weapons. Come to think of it, I’d only ever seen this guy use a sword, but the trunk alone had more than five kinds of weapons. *And they’ve got wear on them, too.* You could see the traces of him trying to find what suited him. A little later, I had a spear in my hand. > **System** > > **Item Window** > > Lizardman Slayer’s Harpoon > > **Type:** Weapon > > **Grade:** First Rate > > **Restriction:** None > > **Description:** Upon a successful attack, Bleeding has a high chance of activating. Anyone watching would think I had a lizard fetish. With the spear as the last piece, I was done choosing. Team Leader Choi chuckled. “What’s so funny?” “I was thinking things are going well.” “Pardon?” “You’ll find out soon enough.” I had no idea what he meant, but I followed him to the front of the Gate. Instead of an Administration staffer, some man was standing there. “You’ve arrived.” A perfectly proper ninety-degree bow. Even more surprising was the way Team Leader Choi took it as natural. “How’s the Gate?” “Yes. I was contacted yesterday, and I restricted access.” “Thanks for your hard work.” “Not at all, young master.” *Young master?* The term was an honorific a woman used for her husband’s unmarried younger brother, but there was no way that man was Team Leader Choi’s sister-in-law… *Team Leader Choi. So he was a rich family’s young master.* No wonder. I should have known from the moment I saw him decked out in luxury gear from head to toe. Add being enough of a fashionista to care about equipment design, and you couldn’t pull that off unless you were one hell of a gold spoon. *That guy has everything.* The guy who had everything turned to me. “All right. Let’s go in.” “Right now?” “The equipment’s taken care of. Is there a problem?” His tone made it sound so obvious that I looked around. Me, Team Leader Choi, and some middle-aged guy I didn’t know. That was everyone. “What about the other team members?” “They’re right here. The team members.” “Oh, I see. He’s going in too, right?” The middle-aged man cut in, his voice heavy. “I’m not.” “Then…?” “It’s just the two of us. There’s no one else.” Team Leader Choi’s words left me slack-jawed. “No one else?” “No.” “Not even one person?” “We’re not bringing so much as a dog.” Look at how decisive he was. Who was he, Pocheongcheon?[^2] “So the two of us are running the Gate alone?” “Why couldn’t we? It’s only a D-rank Gate.” “This is my first D-rank Gate.” “I’ve been to plenty.” No, fuck… A D-rank Gate wasn’t some neighborhood discount mart. “If it’s just the two of us, I’m backing out.” A safe raid on a D-rank Gate required a team of ten D-rank Hunters. I could use the System, and I had learned martial arts, but that didn’t make every danger disappear. “I know what you’re thinking, Mr. Jin Taekyung. But let me tell you one thing.” Team Leader Choi continued in a relaxed voice. “I’m a reawakened Hunter, too.” “Reawakened? I thought you were C-rank, Team Leader…” “C-rank was what I received when I was first measured. My reawakening happened afterward.” Meaning he was at least B-rank in ability. The odds were slim, but he could be even higher than that. *A B-rank Hunter.* If that was true, the situation changed. And with just the two of us, my cut would be that much bigger. “If you want to go back, I won’t stop you. I can go in alone. It wouldn’t be the first time, or the second.” He went in and out of D-rank Gates alone on the regular? “Then be careful in there. From tomorrow, we’ll look at E-rank.” That was the deciding blow. I grabbed his shoulder as he turned away. “Team Leader Choi.” “Yes?” “I want to… raid.” Team Leader Choi smiled warmly. “Let’s do our best.” [^2]: Pocheongcheon is a famously incorruptible judge in Chinese legend and popular storytelling.

## Korean source

```text
＃50화



나는 눈 앞에 펼쳐진 광경에 입을 딱 벌렸다.

뜨겁고 습한 열기 속, 빽빽한 숲을 따라 끝도 없이 펼쳐진 습지가 그곳에 있었다.

“이게 D급 게이트…….”

상위 게이트일수록 공간이 광활해진다는 사실은 알고 있었다. 하지만 이 정도로 차이가 날 줄이야.

“넓죠?”

나는 화내는 것도 잊은 채 대답했다.

“그러네요. 막막할 만큼.”

“이 정도면 그럭저럭 평균입니다. B급 게이트부터는 길잡이도 따로 고용해야 할 정도니까요.”

“……길잡이는 지금도 필요한 것 같은데요.”

“오늘은 괜찮습니다.”

최 팀장이 코팅된 종이를 꺼내어 보여 줬다.

“뭡니까, 그게?”

“지도. 권리 양도받을 때 같이 주더군요.”

지도라, 그럼 길 잃을 일은 없겠…….

“잠깐만요. 뭐라고요?”

“지도라고 말씀드렸습니다만.”

“아뇨, 그거 말고. 그 뒤에 뭐라고 하셨잖아요.”

“권리 양도 말하는 겁니까?”

그래, 인마. 그거.

“그게 무슨 말이에요?”

“말 그대로죠.”

최 팀장이 대수롭지 않다는 듯 말했다.

“이 게이트, 제 겁니다.”

“예?”

“정확히는 독점권을 가지고 있는 거지만요.”

습지대라 그런가. 손에 땀이 맺히고 목이 바짝바짝 탄다.

마른침을 꿀꺽 삼켰다.

‘게이트 독점권이라고?’

대한민국에서 게이트는 국가 재산이다.

대격변 이래 마정석은 핵심 에너지원으로 자리 잡았고, 게이트는 마르지 않는 다이아몬드 광산이나 다름없다. 그런데 그런 게이트의 독점권을 갖고 있다니.

‘도대체 정체가 뭐야?’

부잣집 도련님인 건 알았지만 이 정도일 줄이야.

“슬슬 출발하시죠.”

성큼성큼 앞서 나가는 최 팀장의 뒷모습이 눈부시다. 아아, 저 황금빛 광채, 범접할 수 없는 부의 향기.

‘당신의 길드에 뼈를 묻겠습니다.’

나는 굳게 다짐했다.



* * *



습지대는 미로 같았다.

최 팀장이라는 유능한 길잡이가 없었다면 한참을 헤맸을 것이다. 그렇게 얼마나 걸었을까.

- 키이잇.

공력을 끌어 올리자 더욱 선명히 들리는 울음소리. 몬스터의 등장이었다.

‘최소 스무 마리.’

오는 길에 들었던 최 팀장의 설명에 의하면 이번 게이트에 출현하는 몬스터는 습지대 리자드맨이다.

놈들은 하나의 부족 아래 여러 군락으로 나누어 생활하는데, 그중 하나인 모양이었다.

“입구에서 가장 가까운 소규모 군락입니다. 스무 마리 정도니까 빨리 해치우고 이동합시다.”

최 팀장은 넝쿨을 쳐내며 나아갔다. 평소에는 곱상한 도련님인데 막상 실전에 돌입하니 장난 아니다. 핸들이 고장 난 8톤 트럭처럼 밀고 나가는 뒷모습에서 마초의 냄새가 물씬 풍겼다.

‘존나 멋있어.’

리자드맨 서른 마리가 아니라 백 마리가 와도 최 팀장과 함께라면 쓸어버릴 수 있을 것 같은 이 기분.

왜 온라인 게임에서 고레벨 유저한테 쩔 받는지 알겠다.

“키이잇!”

그래서인지 리자드맨과의 첫 대면도 별 긴장감이 없었다.

다만 사진이나 영상으로만 봤던 몬스터에 대한 신기함만 있을 뿐.

“오, 크다.”

스무 마리 중 가장 작은 놈도 나보다 머리 하나가 더 크다.

최소 2m의 신장과 날렵한 근육, 두툼한 꼬리까지 있어서 그런지 더 커 보인다.

‘물론 어제 상대했던 홉 고블린 대전사만큼은 아니지만.’

이 흉측하게 생긴 농구 유망주들은 우리의 등장이 썩 반갑지 않은 듯했다.

- 키잇!

- 킷, 킷!

각기 손에 든 수십 개의 작살이 번쩍 빛난다. 나는 에워싸는 형태로 전방에서 접근해 오는 놈들을 보며 말했다.

“궁수는 없네요.”

“습지대 리자드맨은 대부분 작살을 씁니다. 혹시 모르니 투창 조심하세요.”

“넵.”

역시 리잘알. 여유롭게 팔짱까지 끼고 있다.

“키이잇!”

불과 이십여 미터 앞까지 접근해 왔다. 나는 최 팀장을 보며 씩 웃었다.

“이놈들이 겁이 없네요.”

“리자드맨 특성입니다. 저돌적이고, 정면 승부를 선호하죠.”

“아하.”

그사이 거리가 10m로 좁혀졌다. 나는 최 팀장의 팔짱이 신경 쓰이기 시작했다.

“슬슬 싸워야 할 것 같은데요.”

“싸워야겠네요.”

“……아, 네. 그래야죠.”

쐐애액-!

그때 작살 서너 개가 바람을 찢으며 쇄도했다. F급 헌터 시절이었다면 주마등이 스쳤겠지만 이제는 뭐, 가볍게 창을 휘둘러 튕겨 냈다.

터터텅!

뭔가 이상함을 느낀 건 그다음이었다.

- 끼이이잇!

- 킷! 키이잇!

저놈들 왜 저래?

눈을 허옇게 뒤집어 까고 괴성을 질러 대는데, 이건 적의를 넘어 거의 증오 수준이다.

어리둥절한 내게 최 팀장이 한마디를 툭 던졌다.

“장비 때문입니다.”

장비? 장비가 왜…… 아!

‘리자드맨 가죽 세트, 학살자의 창.’

시바, 이름 봐라.

내가 리자드맨이었어도 작살 날렸겠다.

‘그러고 보니 작살도 나한테만 날렸네.’

동족의 원수가 코앞에 있으니 최 팀장은 투명 인간 취급이다.

이렇게 되면 나만 줄창 공격당하게 생겼…… 아니, 잠깐만.

“이거 노린 겁니까?”

“뭘 말입니까?”

“저한테 이거 입혀서 어그로 끌고 본인이 쓱싹 하겠다, 딱 그 전략이잖아요, 이거!”

“맹세코 아닙니다.”

정색한 최 팀장이 덧붙였다.

“저는 가만히 있을 거거든요.”

“예?”

“태경 씨가 어그로 끌고, 레이드도 할 겁니다. 괜한 오해하지 마세요.”

이게 뭔 개소리야.

“그러니까…… 저 혼자 싸우라고요?”

“네.”

“최 팀장님은 거기서 팔짱 끼고 구경하시고?”

“팔짱은 풀겠습니다.”

“아니, 시벌…….”

“작살 날아옵니다.”

쐐애액-!

투창(投槍)과 동시에 사방에서 녹색 비늘이 번뜩이며 쇄도한다. 훌쩍 물러난 최 팀장이 비장하게 외쳤다.

“화이팅!”

저거 완전히 미친놈 아냐.

당장이라도 달려가 멱살을 붙잡고 싶었지만 사방에서 작살이 날아들었다.

캉!

- 키이잇!

“이 새끼들이.”

나는 이를 갈며 [기감]을 끌어올렸다. 곧 놈들의 머리 위로 스무 개의 창이 불쑥 솟아올랐다.



[Lv.40 리자드맨 부족민]



40레벨이라…….

나는 창을 꽉 움켜쥐었다.

“너넨 다 죽었어.”

띠링.



- [리자드맨 가죽 세트]의 효과로 해당 몬스터에게 입히는 피해가 10% 상승합니다.

- [리자드맨 학살자의 창]의 효과로 해당 몬스터에게 입히는 피해가 20% 상승합니다.

- 해당 게이트의 모든 [리자드맨]이 당신을 적대합니다. 그들은 이 원한을 갚기 전까지 결코 멈추지 않을 것입니다!



동시에 학살자의 창이 묵직한 궤적을 그려냈다. 칠 성에 이른 진가창법의 초식들이 놈들을 향해 쏟아졌다.

콰드득!



* * *



- 키이…….

노란 파충류의 눈이 스르륵 감긴다. 녹색 습지대는 앞서 죽은 놈들의 시체와 핏물로 잠겨 있었고, 더 이상 서 있는 리자드맨은 존재하지 않았다.

띠링.



- 레벨 업!

- 레벨 업!



경쾌한 시스템 알림을 뒤로하고 돌아섰다. 나무에 기대어 서 있던 최 팀장이 보였다. 팔짱 안 낀다고 하더니 끼고 있어서 두 배로 열받는다.

“뭐 하는 짓입니까?”

말없이 나를 바라보던 최 팀장이 뭔가를 던졌다. 조그만 드링크 병에 담긴 빨간 액체. 소진된 체력을 회복시켜 주는 포션이다.

“지금 병 주고 약 줍니까?”

“병든 것치고는 건강해 보이시는데요. 긁힌 상처 하나 없는 거 보면.”

……그럴듯한데. 순간 납득할 뻔했다.

내가 주춤하는 사이 최 팀장의 입이 열렸다.

“미안합니다.”

거기에 그치지 않고 허리를 굽힌다. 뭐라 할 말이 없을 정도로 정중한 사과였다. 순간 마음이 누그러졌지만 이유는 들어야겠다.

“왜 그랬어요?”

“실력을 봐야 하니까요.”

“겨우 그것 때문에?”

“저한테는 중요합니다. 태경 씨가 어떻게 움직이고, 얼마나 상대할 수 있는지. 또 어디까지 함께할 수 있는지를 알아야 하니까요.”

“그렇다고 몬스터 득실거리는데 혼자 빠져요?”

“태경 씨가 못 미더웠다면 그러지도 않았을 겁니다.”

잘난 놈이 띄워 주니까 솔직히 기분 좋다.

‘무엇보다 다치지도 않았고, 레벨 업도 두 번이나 했지.’

나는 은근히 기대하며 물었다.

“결과는요?”

“음.”

특유의 묘한 눈빛으로 나를 응시하던 최 팀장이 마침내 입을 열었다.

“아직 모르겠습니다.”

“예?”

“그래서 말인데.”

최 팀장이 뭔가를 꺼내 내게 던졌다. 안이 보이지 않는 길쭉한 원통이다. 흔들어 보니 액체가 찰랑거렸다.

“이게 뭡니까, 포션?”

“아래쪽에 버튼 있죠? 눌러 보세요.”

누르면 열리는 구조인가?

고개를 갸웃거리면서 버튼을 눌렀다. 달칵, 하는 소리와 함께 원통 앞부분이 활짝 열렸다.

문제는…….

피유우우우-

펑!

그 안에 있던 게 폭죽처럼 치솟더니 공중에서 터져 버렸다는 거다. 공중에서 터진 분홍색 액체는 넓게 퍼져 나갔다.

“어?”

저게 뭐지?

멍하니 그 광경을 바라보던 내 귓가로 최 팀장의 목소리가 파고들었다.

“페로몬입니다.”

“페로몬? 향수?”

“비슷합니다.”

“……?”

“암컷 리자드맨에게서 채취한 거거든요.”

그의 말이 끝나기가 무섭게 어디선가 진동이 느껴졌다.

땅이다. 땅이 울리고 있었다. 최 팀장이 친절히 덧붙였다.

“효과가 아주 강력합니다.”

너 이 새끼…….



* * *



“3팀장아.”

반백의 장년인이 한 시간 만에 내뱉은 첫 마디다. 그가 줄담배를 피우는 동안 하염없이 기다리던 김상식이 대답했다.

“예, 길드장님.”

“궁금하지? 이 인간이 또 뭔 지랄을 떨려고 아침부터 불렀나, 싶지?”

“아, 아닙니다.”

소풍 길드장이 사람 좋게 웃었다.

“맞아.”

“예?”

“지랄 떨려고 부른 거라고.”

“…….”

“내가 오늘 어디 다녀왔는지 알아?”

길드장이 담배 연기를 내뿜으며 말했다.

“길드 연합 조찬 모임.”

중소 길드도 기업체다. 지역마다 연합과 친목 도모를 위해 각 길드장끼리 모임을 갖는 일이 있는데, 그게 바로 오늘이었다.

“공복에 겨우 한술 뜨려는데, 상동 길드장 그 새끼가 재미있는 얘기를 하더라. 이번에 각성한 C급짜리가 며칠 전까지 우리 길드 식구였다고.”

“……길드장님, 그게.”

길드장이 손을 들어 김상식의 이어지는 말을 막았다.

“뭔 개소린가 싶었지. 근데 상동 길드장이 싸가지 없는 새끼인 건 맞는데, 없는 얘기까지 지어낼 놈은 아니거든. 그것도 연합 모임에서.”

“제가, 제가 다시 알아보겠습니다!”

“3팀장이? 아냐, 그럴 필요 없어.”

길드장이 구겨진 종이 뭉치를 휙 던졌다.

“내가 따로 알아봤으니까.”

김상식은 이 구겨진 종이 뭉치의 정체가 누군가의 신상 명세서라는 사실을 알 수 있었다. 그의 이름도.

“진태경, 3팀장도 아는 이름이지?”

‘씨발.’

눈을 질끈 감는 김상식을 보며 길드장이 담뱃재를 털었다.

“3팀장 마음 알아. 나름 길드 창립 멤버고, 마음에 안 드는 최하급 헌터 하나 자를 수도 있지. 빈자리에 사랑하는 아들도 꽂아 주고. 안 그래?”

“예, 예.”

“그런데 실컷 박대하고 내쫓았던 F급 미꾸라지가 용 돼서 돌아왔네? 길드장이 꼭 영입하라고 신신당부까지 했는데 사실대로 말하면 지랄 떨 게 뻔하고, 사람도 못 알아보는 개눈깔이라고 소문날 것 같고. 그래서 허위 보고 올린 거지? 그렇지?”

치지직.

길드장은 담배를 비벼 껐다. 불씨가 흩어지며 그의 마지막 인내심도 사라졌다.

“3팀장. 아니, 상식아. 우리가 20년쯤 됐나?”

김상식이 불안한 목소리로 대답했다.

“21년입니다, 길드장님.”

“그게 아니지.”

“……예, 형님.”

“그래, 듣기 좋네. 앞으로 쭉 그렇게 해.”

“예?”

“21년 끌고 와 줬으면 할 만큼 했다. 3팀 애들한테는 따로 말할 테니까 오늘부로 퇴사해.”

“혀, 형님!”

“조용히 입 닥치고 꺼지면 앞길은 안 막는다. 나가서 뭘 하든 네 마음대로 해.”

분노를 꾹꾹 눌러 담은 길드장의 목소리.

김상식은 더 이상 선택지가 없다는 사실을 깨달았다.

‘나가라고? 길드를?’

20년 넘게 몸담았던 직장이다. 그런데 고작 이런 일로 나가라니. 망설임 없이 내치다니.

‘이런 씨발…….’

이를 악물고 사무실을 나서는 그의 등 뒤로 마지막 한 방이 날아왔다.

“어, 인사팀장. 오늘 두 명 퇴사 처리 해. 김상식이랑 김상호.”

그 후, 며칠간 소풍 길드는 부자(父子) 동시 퇴사라는 보기 드문 사건으로 시끄러웠다.

그와 함께 길드 내 핫이슈로 떠오른 건 얼마 전 퇴사한 최하급 헌터의 근황이었다.

“C급이래. 재각성.”

“어머, 태경 씨가요? 내가 아는 그 태경 씨?”

“그렇다니까. 완전히 로또 맞은 거지. 김상식 그 인간이 누군지도 모르고 영입하러 갔다가 제대로 뺀찌 먹었다는데.”

“온갖 트집 잡아서 자르더니, 뿌린 대로 거뒀네요. 듣기로는 김 팀장님, 돌아다니면서 부당 해고라고 길드장님 욕하고 다닌다던데.”

“정신 못 차린 거지. 크, 아무튼 부럽다. 나도 언제쯤 그런 인생 살아 보나.”

“솔직히 태경 씨는 자격 있죠. 그렇게 열심히 살던 사람이니까 행운도 찾아온 거지.”

“자격은 무슨. 그럼 우리는 죄다 흥청망청 사는 사람들이야? 다 운빨이지, 운빨.”

부러움 반, 질투 반인 대화의 끝은 늘 한 가지 의문으로 끝맺었다.

“태경 씨, 지금 어디서 뭐 하고 있을까?”
```

## Current accepted English baseline

```markdown
# Chapter 50

My mouth fell open at the sight in front of me.

In the hot, humid heat, wetlands stretched on without end along a dense forest.

“This is a D-rank Gate…”

I knew higher-ranked Gates had more space. I just hadn’t thought the difference would be this big.

“Pretty big, right?”

I forgot to be angry and answered.

“Yeah. Big enough to feel lost.”

“This is fairly average. From B-rank Gates on, you even have to hire a separate guide.”

“…Feels like we need one now.”

“We’ll be fine today.”

Team Leader Choi pulled out a laminated sheet and showed it to me.

“What’s that?”

“A map. They gave it to me along with the transfer of rights.”

A map. Then we wouldn’t get lost—

“Wait. What did you say?”

“I said it was a map.”

“No, not that. You said something after that.”

“You mean the transfer of rights?”

Yeah, you. That.

“What does that mean?”

“Exactly what it sounds like.”

Team Leader Choi spoke as if it were nothing.

“This Gate is mine.”

“What?”

“More precisely, I have the exclusive rights to it.”

Maybe it was the wetlands. Sweat beaded on my palms, and my throat went bone-dry.

I swallowed a dry gulp.

*Exclusive rights to a Gate?*

In South Korea, Gates were national property.

Since the Great Cataclysm, Magic Gems had become a core energy source, and Gates were no different from diamond mines that never ran dry. And this guy had exclusive rights to one of those Gates.

*What the hell is he?*

I knew he was a rich family’s young master, but I hadn’t thought it went this far.

“Let’s get moving.”

Team Leader Choi strode ahead. The sight of his back was dazzling.

Ah, that golden radiance. The scent of wealth I could never touch.

*I’ll bury my bones in your Guild.*

I swore it then and there.

* * *

The wetlands were a maze.

Without a capable guide like Team Leader Choi, I would have wandered for a long time. How long had we been walking when—

- Keeiik.

The cry grew even clearer as I drew up my internal energy.

A monster had appeared.

*At least twenty.*

According to Team Leader Choi’s explanation on the way here, the monsters in this Gate were swamp Lizardmen.

They lived in several colonies under a single tribe, and this seemed to be one of them.

“This is the small colony closest to the entrance. About twenty of them, so let’s take them out fast and move on.”

Team Leader Choi hacked through the vines as he advanced. He was usually a pretty-faced young master, but once real combat started, he was no joke. The back driving forward like an eight-ton truck with a broken steering wheel reeked of machismo.

*He’s fucking cool.*

Even if it weren’t thirty Lizardmen but a hundred, I felt like we could sweep them all as long as Team Leader Choi was with me.

Now I understood why people let high-level players carry them in online games.

“Keiik!”

Maybe that was why my first face-to-face with Lizardmen didn’t come with much tension.

All I had was the novelty of seeing monsters I’d only ever seen in photos and videos.

“Oh, they’re big.”

Even the smallest of the twenty was a head taller than me.

They were at least two meters tall, with sleek muscle and thick tails that made them look even bigger.

*Of course, still not as big as the Hobgoblin Great Warrior I fought yesterday.*

These hideous basketball prospects didn’t seem too happy to see us.

- Keiik!

- Keet, keet!

Dozens of harpoons flashed in their hands. Watching them close in from the front in an encircling formation, I spoke.

“No archers.”

“Swamp Lizardmen mostly use harpoons. Watch out for thrown spears, just in case.”

“Yep.”

As expected of a lizard expert. He even had his arms folded, nice and easy.

“Keiik!”

They’d come within twenty meters. I grinned at Team Leader Choi.

“These guys have no fear.”

“That’s a Lizardman trait. They’re reckless, and they prefer a head-on fight.”

“Aha.”

Meanwhile the distance closed to ten meters. Team Leader Choi’s folded arms were starting to get on my nerves.

“I think we should start fighting soon.”

“Guess we should.”

“…Ah. Right. We should.”

Whoosh!

Then three or four harpoons tore through the air. If I’d still been an F-rank Hunter, my life would have flashed before my eyes. Now I just swung my spear and batted them aside.

Clang, clang, clang!

It was only after that that I sensed something off.

- Kieeeik!

- Keet! Keiik!

*What’s wrong with them?*

Their eyes rolled back white as they shrieked. This had gone past hostility. It was practically hatred.

As I stood there bewildered, Team Leader Choi tossed out a line.

“It’s because of your equipment.”

Equipment? Why would equipment—

Ah.

*Lizardman Hunter’s Leather Set. Lizardman Slayer’s Harpoon.*

*Shit. Look at those names.*

If I were a Lizardman, I’d throw harpoons too.

*Come to think of it, they only threw them at me.*

With the enemy of their kind standing right in front of them, Team Leader Choi might as well have been invisible.

At this rate I was going to get attacked nonstop—

No, wait.

“Did you plan this?”

“Plan what?”

“You put this on me to pull aggro so you could mop them up. That’s the strategy, isn’t it!”

“I swear it isn’t.”

Team Leader Choi’s face turned serious as he added,

“Because I’m going to stay put.”

“What?”

“You’ll pull the aggro, and you’ll do the raid too. Don’t get the wrong idea.”

*What the hell is this bullshit.*

“So… I have to fight them alone?”

“Yes.”

“And you’ll stand there with your arms folded and watch?”

“I’ll uncross my arms.”

“No, for fuck’s sake…”

“Harpoons incoming.”

Whoosh!

As the spears were thrown, green scales flashed from every direction and they charged.

Team Leader Choi sprang back and shouted with heroic gravity,

“You got this!”

Was this guy completely insane?

I wanted to run over and grab him by the collar, but harpoons were already flying in from all sides.

Clang!

- Keiik!

“You bastards.”

Grinding my teeth, I drew up my Qi Sense. Soon, twenty spears sprang up over their heads.

> **System**
>
> **Lv. 40 Lizardman Tribesman**

Level 40, huh?

I tightened my grip on my spear.

“You’re all dead.”

Ding.

> **System**
>
> - Damage dealt to this monster increases by 10% due to the effect of **Lizardman Hunter’s Leather Set**.
>
> - Damage dealt to this monster increases by 20% due to the effect of **Lizardman Slayer’s Harpoon**.
>
> - All **Lizardmen** in this Gate are hostile toward you. They will never stop until they repay this grudge!

At the same time, the Lizardman Slayer’s Harpoon traced a heavy arc. The forms of the Jin Family’s Spear Technique, having reached Seven Stars, poured toward them.

Crunch!

* * *

- Keiik…

The yellow reptilian eyes slowly closed.

The green wetlands were soaked with the corpses and blood of the ones already dead. Not a single Lizardman was left standing.

Ding.

> **System**
>
> - Level Up!
>
> - Level Up!

Leaving the cheerful System notifications behind me, I turned around.

Team Leader Choi was leaning against a tree. He’d said he wouldn’t fold his arms, and there he was with them folded. That made me twice as pissed.

“What do you think you’re doing?”

Team Leader Choi looked at me in silence, then tossed something over.

A small drink bottle of red liquid. A potion that restored depleted Stamina.

“So you give me the disease and then the medicine?”

“You look pretty healthy for a sick man. Not a scratch on you.”

…That actually sounded plausible. I nearly bought it.

While I hesitated, Team Leader Choi spoke.

“I’m sorry.”

He didn’t stop there. He even bowed at the waist.

It was such a formal apology I had nothing to say. My anger eased a little, but I still needed the reason.

“Why did you do that?”

“I had to see your skill.”

“Just for that?”

“It’s important to me. I need to know how you move, how much you can take on, and how far we can go together.”

“So you just slipped out alone while it was crawling with monsters?”

“If I hadn’t trusted you, I wouldn’t have.”

When a capable guy hyped me up like that, I had to admit it felt good.

*More importantly, I didn’t even get hurt, and I leveled up twice.*

I asked, quietly hopeful.

“And the results?”

“Hmm.”

Team Leader Choi studied me with that peculiar look of his. At last he opened his mouth.

“I still don’t know.”

“What?”

“Which is why.”

Team Leader Choi pulled something out and tossed it to me.

A long, opaque cylinder. When I shook it, liquid sloshed inside.

“What is this, a potion?”

“There’s a button on the bottom, right? Press it.”

*Does it open when I press it?*

I tilted my head and pressed the button.

Click.

The front of the cylinder sprang wide open.

The problem was—

Fwoooosh—

Boom!

Whatever had been inside shot up like a firework and burst in midair. The pink liquid that exploded there spread out over a wide area.

“Huh?”

*What is that?*

As I stared blankly at the sight, Team Leader Choi’s voice dug into my ear.

“It’s pheromones.”

“Pheromones? Perfume?”

“Something like that.”

“…?”

“It was collected from female Lizardmen.”

The instant he finished speaking, I felt a tremor from somewhere.

The ground. The ground was rumbling.

Team Leader Choi kindly added,

“The effect is extremely powerful.”

*You bastard…*

* * *

“Team Leader Three.”

That was the first thing the middle-aged man with half-gray hair had said in an hour. Kim Sangshik, who had been waiting endlessly while the Guild Master chain-smoked, answered.

“Yes, Guild Master.”

“Curious, aren’t you? Figured I called you in first thing this morning to raise hell?”

“Ah, no, sir.”

The Sopung Guild Master smiled good-naturedly.

“That’s right.”

“What?”

“I called you to raise hell.”

“…”

“Do you know where I went today?”

The Guild Master exhaled a plume of cigarette smoke.

“The Guild Alliance breakfast meeting.”

Small and midsize Guilds were corporations too. In each region, Guild Masters held meetings to form alliances and socialize. That was where he’d been today.

“I was on an empty stomach, just about to take a bite, when that Sangdong Guild Master bastard told me something interesting. He said the C-rank who awakened recently had been one of our Guild people until a few days ago.”

“…Guild Master, that…”

The Guild Master raised a hand and stopped Kim Sangshik from continuing.

“I wondered what kind of bullshit that was. But rude as the Sangdong Guild Master is, he isn’t the type to make up a story. Not at an alliance meeting, either.”

“I’ll look into it again myself!”

“Team Leader Three? No. No need.”

The Guild Master threw a crumpled bundle of papers across the room.

“I already looked into it myself.”

Kim Sangshik recognized the crumpled papers for what they were: someone’s personal file.

And the name on it, too.

“Jin Taekyung. Team Leader Three knows that name too, right?”

*Fuck.*

Kim Sangshik squeezed his eyes shut. The Guild Master tapped the ash from his cigarette.

“I know how you feel, Team Leader Three. You’re a founding member of the Guild, after all. You’re allowed to fire one bottom-tier Hunter you don’t like. Stick your beloved son in the vacancy. Right?”

“Yes, yes.”

“But the F-rank loach you treated like dirt and kicked out turned into a dragon and came back, huh? I even made a point of telling you to recruit him, but if you told the truth I’d obviously raise hell. You’d get a reputation for having dog eyes that can’t even recognize someone. So you filed a false report, right?”

Sizzle.

The Guild Master crushed out his cigarette. As the embers scattered, the last of his patience went with them.

“Team Leader Three. No, Sangshik. Have we been together about twenty years?”

Kim Sangshik answered in an uneasy voice.

“Twenty-one years, Guild Master.”

“That’s not what I meant.”

“…Yes, hyung.”

“Good. That sounds nice. Keep calling me that from now on.”

“What?”

“Twenty-one years of dragging you along is enough. You’ve done your part. I’ll talk to the Team Three kids separately, so as of today, you’re out.”

“H-hyung!”

“Shut your mouth, leave quietly, and I won’t block your path. Once you’re out, do whatever you want.”

The Guild Master’s voice was packed with tightly suppressed fury.

Kim Sangshik realized he had no choices left.

*Leave? Leave the Guild?*

This was the workplace he’d spent more than twenty years in. And now he was being told to leave over something like this. Thrown out without a second thought.

*Fuck…*

He clenched his teeth and walked out of the office.

One last blow came after him.

“Hey, HR. Process two resignations today. Kim Sangshik and Kim Sangho.”

For the next few days, Sopung Guild was in an uproar over the rare event of a father and son resigning at the same time.

Along with that, the hottest topic in the Guild became the recent whereabouts of the bottom-tier Hunter who had quit not long before.

“They say he’s C-rank. A reawakening.”

“Oh my, Mr. Taekyung? The Taekyung I know?”

“That’s what I’m saying. He hit the lottery. Apparently Kim Sangshik went to recruit him without even knowing who he was and got shut down hard.”

“He found every excuse he could to fire him, and now he’s reaped what he sowed. I heard Team Leader Kim’s been going around calling it wrongful dismissal and badmouthing the Guild Master.”

“He still hasn’t come to his senses. Still, I’m jealous. When do I ever get to live a life like that?”

“Honestly, Taekyung deserves it. He worked so hard, so luck found him.”

“Deserves it, my ass. Then are the rest of us all just living it up? It’s luck. All luck.”

Half envy, half jealousy, the conversations always ended with the same question.

“Where is Mr. Taekyung now, and what’s he doing?”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 50`.

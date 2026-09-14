# Master Edit Task — Chapter 51

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
| 살기     | **killing intent**                               |                                                       |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 레벨               | **Level**                      |
| 장비               | **Equipment**                  |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 산서     | **Shanxi**             |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |
| 고생하셨습니다 | register | Subordinate courtesy (“thank you for your hard work”), not a superior’s “Good work.” | |

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

#### Chapter 49 tail (verified mastered)

…
it looks nice. *How rich do you have to be to think like that?* C-rank Hunters made good money, but Team Leader Choi’s spending was already beyond that. He must have been rich enough that money was never a concern. Gulp. “It might be better to rent from a rental shop. If I borrow something and it gets wrecked, it’d be kind of…” “They’re out of fashion, so it doesn’t matter.” Ah. So he even cares whether equipment is in fashion. I gave up thinking about it around there and picked my equipment. Having the System made it easy. *Item check.* Ding. > **System** > > **Item Window** > > Lizardman Hunter’s Leather Set > > **Type:** Armor > > **Grade:** First Rate > > **Restriction:** None > > **Description:** Made by stripping a lizardman’s hide off in one piece. > > Scale Armor activates when the full set is equipped. *This is pretty good.* It was light, and the leather was both tough and hard. Once I had everything on, the set effect Scale Armor activated. “Oh.” Green scales rose from the leather, densely covering my entire body. Team Leader Choi nodded at the sight of me. “You picked a good one. You’ve got a good eye.” *It’s the System that’s good.* I smiled awkwardly and rummaged through the weapons. Come to think of it, I’d only ever seen this guy use a sword, but the trunk alone had more than five kinds of weapons. *And they’ve got wear on them, too.* You could see the traces of him trying to find what suited him. A little later, I had a spear in my hand. > **System** > > **Item Window** > > Lizardman Slayer’s Harpoon > > **Type:** Weapon > > **Grade:** First Rate > > **Restriction:** None > > **Description:** Upon a successful attack, Bleeding has a high chance of activating. Anyone watching would think I had a lizard fetish. With the spear as the last piece, I was done choosing. Team Leader Choi chuckled. “What’s so funny?” “I was thinking things are going well.” “Pardon?” “You’ll find out soon enough.” I had no idea what he meant, but I followed him to the front of the Gate. Instead of an Administration staffer, some man was standing there. “You’ve arrived.” A perfectly proper ninety-degree bow. Even more surprising was the way Team Leader Choi took it as natural. “How’s the Gate?” “Yes. I was contacted yesterday, and I restricted access.” “Thanks for your hard work.” “Not at all, young master.” *Young master?* The term was an honorific a woman used for her husband’s unmarried younger brother, but there was no way that man was Team Leader Choi’s sister-in-law… *Team Leader Choi. So he was a rich family’s young master.* No wonder. I should have known from the moment I saw him decked out in luxury gear from head to toe. Add being enough of a fashionista to care about equipment design, and you couldn’t pull that off unless you were one hell of a gold spoon. *That guy has everything.* The guy who had everything turned to me. “All right. Let’s go in.” “Right now?” “The equipment’s taken care of. Is there a problem?” His tone made it sound so obvious that I looked around. Me, Team Leader Choi, and some middle-aged guy I didn’t know. That was everyone. “What about the other team members?” “They’re right here. The team members.” “Oh, I see. He’s going in too, right?” The middle-aged man cut in, his voice heavy. “I’m not.” “Then…?” “It’s just the two of us. There’s no one else.” Team Leader Choi’s words left me slack-jawed. “No one else?” “No.” “Not even one person?” “We’re not bringing so much as a dog.” Look at how decisive he was. Who was he, Pocheongcheon?[^2] “So the two of us are running the Gate alone?” “Why couldn’t we? It’s only a D-rank Gate.” “This is my first D-rank Gate.” “I’ve been to plenty.” No, fuck… A D-rank Gate wasn’t some neighborhood discount mart. “If it’s just the two of us, I’m backing out.” A safe raid on a D-rank Gate required a team of ten D-rank Hunters. I could use the System, and I had learned martial arts, but that didn’t make every danger disappear. “I know what you’re thinking, Mr. Jin Taekyung. But let me tell you one thing.” Team Leader Choi continued in a relaxed voice. “I’m a reawakened Hunter, too.” “Reawakened? I thought you were C-rank, Team Leader…” “C-rank was what I received when I was first measured. My reawakening happened afterward.” Meaning he was at least B-rank in ability. The odds were slim, but he could be even higher than that. *A B-rank Hunter.* If that was true, the situation changed. And with just the two of us, my cut would be that much bigger. “If you want to go back, I won’t stop you. I can go in alone. It wouldn’t be the first time, or the second.” He went in and out of D-rank Gates alone on the regular? “Then be careful in there. From tomorrow, we’ll look at E-rank.” That was the deciding blow. I grabbed his shoulder as he turned away. “Team Leader Choi.” “Yes?” “I want to… raid.” Team Leader Choi smiled warmly. “Let’s do our best.” [^2]: Pocheongcheon is a famously incorruptible judge in Chinese legend and popular storytelling.

#### Chapter 50 tail (verified mastered)

…
a potion?” “There’s a button on the bottom, right? Press it.” *Does it open when I press it?* I tilted my head and pressed the button. Click. The front of the cylinder sprang wide open. The problem was— Fwoooosh— Boom! Whatever had been inside shot up like a firework and burst in midair. The pink liquid that exploded there spread out over a wide area. “Huh?” *What is that?* As I stared blankly at the sight, Team Leader Choi’s voice dug into my ear. “It’s pheromones.” “Pheromones? Perfume?” “Something like that.” “…?” “It was collected from female Lizardmen.” The instant he finished speaking, I felt a tremor from somewhere. It was the ground. The ground was rumbling. Team Leader Choi kindly added, “The effect is extremely powerful.” *You bastard…* * * * “Team Leader Three.” That was the first thing the middle-aged man with half-gray hair had said in an hour. Kim Sangshik, who had been waiting endlessly while the Guild Master chain-smoked, answered. “Yes, Guild Master.” “You’re curious, aren’t you? Wondering what kind of shit this guy plans to pull this time, calling you in first thing in the morning?” “Ah, no, sir.” The Sopung Guild Master smiled good-naturedly. “That’s right.” “What?” “I called you to raise hell.” “…” “Do you know where I went today?” The Guild Master exhaled a plume of cigarette smoke. “The Guild Alliance breakfast meeting.” Small and midsize Guilds were corporations too. In each region, Guild Masters held meetings to form alliances and socialize. That was where he’d been today. “I was on an empty stomach, just about to take a bite, when that Sangdong Guild Master bastard told me something interesting. He said the C-rank who awakened recently had been one of our Guild people until a few days ago.” “…Guild Master, that…” The Guild Master raised a hand, cutting Kim Sangshik off. “I wondered what kind of bullshit that was. But rude as the Sangdong Guild Master is, he isn’t the type to make up a story. Not at an alliance meeting, either.” “I-I’ll look into it again myself!” “Team Leader Three? No. No need.” The Guild Master threw a crumpled bundle of papers across the room. “I already looked into it myself.” Kim Sangshik recognized the crumpled papers for what they were: someone’s personal file. And the name on it, too. “Jin Taekyung. Team Leader Three knows that name too, right?” *Fuck.* Kim Sangshik squeezed his eyes shut. The Guild Master tapped the ash from his cigarette. “I know how you feel, Team Leader Three. You’re a founding member of the Guild, after all. You’re allowed to fire one bottom-tier Hunter you don’t like. Stick your beloved son in the vacancy. Right?” “Yes, yes.” “But the F-rank loach you treated like dirt and kicked out turned into a dragon and came back, huh? I even made a point of telling you to recruit him, but if you told the truth I’d obviously raise hell. You’d get a reputation for having dog eyes that can’t even recognize someone. So you filed a false report, right?” Sizzle. The Guild Master crushed out his cigarette. As the embers scattered, the last of his patience went with them. “Team Leader Three. No, Sangshik. Have we been together about twenty years?” Kim Sangshik answered in an uneasy voice. “Twenty-one years, Guild Master.” “That’s not what I meant.” “…Yes, hyung.” “Good. That sounds nice. Keep calling me that from now on.” “What?” “You’ve helped me keep this Guild going for twenty-one years. You’ve done more than enough. I’ll talk to the Team Three kids separately, so as of today, you’re out.” “H-hyung!” “Shut your mouth, leave quietly, and I won’t block your path. Once you’re out, do whatever you want.” The Guild Master’s voice was packed with tightly suppressed fury. Kim Sangshik realized he had no choices left. *Leave? Leave the Guild?* This was the workplace he’d spent more than twenty years in. And now he was being told to leave over something like this. Thrown out without a second thought. *Fucking hell…* He clenched his teeth and walked out of the office. One last blow came after him. “Hey, HR Team Leader. Process two terminations today. Kim Sangshik and Kim Sangho.” For the next few days, Sopung Guild was in an uproar over the rare event of a father and son being fired at the same time. Along with that, the hottest topic in the Guild became the recent whereabouts of the bottom-tier Hunter who had left not long before. “They say he’s C-rank. A reawakening.” “Oh my, Mr. Taekyung? The Taekyung I know?” “That’s what I’m saying. He hit the lottery. Apparently Kim Sangshik went to recruit him without even knowing who he was and got shut down hard.” “He found every excuse he could to fire him, and now he’s reaped what he sowed. I heard Team Leader Kim’s been going around calling it wrongful dismissal and badmouthing the Guild Master.” “He still hasn’t come to his senses. Still, I’m jealous. When do I ever get to live a life like that?” “Honestly, Taekyung deserves it. He worked so hard, so luck found him.” “Deserves it, my ass. Then are the rest of us all just living it up? It’s luck. All luck.” Half envy, half jealousy, the conversations always ended with the same question. “Where is Mr. Taekyung now, and what’s he doing?”

## Korean source

```text
＃51화



쉬쉬쉭!

검, 도끼, 철퇴.

수십 개의 무기가 소나기처럼 쏟아졌다. 그러나 내게는 똑똑히 보인다. 공격 하나하나가 어디로, 어떻게 향하는지.

그 틈을 파고들었다.

서걱-

C급 몬스터, 리자드맨 전사의 목을 쳐 날리는 게 시작이었다. 창날이 반원을 그림과 동시에 사방에서 핏물이 솟구쳤다.

띠링. 띠링. 띠링.



- [Lv.40 리자드맨 전사]를 처치했습니다!

- [Lv.41 늪지대 리자드맨]을 처치했습니다!

- [Lv.40 늪지대 리자드맨]을…….



- 키이이…….

살아남은 놈들이 주춤거리며 물러선다. 동족의 원수를 만나 살기를 뿜어내던 녀석들이, 지금은 두려움에 떨고 있다.

하지만 그것도 잠시.

- 크워어어!



- 보스 몬스터, [Lv.52 리자드맨 대족장]이 출현했습니다!

- 스킬, [전장의 함성]을 사용합니다!



최소 두 배는 큰 덩치. 거대한 철퇴를 든 리자드맨 족장의 외침에 공기가 터져 나간다. 우두머리의 등장에 뒷걸음질 치던 리자드맨들이 정신을 차리고 대열을 갖췄다.

‘어쩐 일로 쉽게 끝나나 했다.’

등 뒤로 최 팀장의 느긋한 목소리가 들렸다.

“가능하겠어요?”

“그게 며칠 동안 손 하나 까딱 안 한 사람이 할 소립니까?”

“이야기가 다르죠. C급 게이트니까.”

“그럼 도와주시든가.”

곰곰이 생각하던 최 팀장이 대답했다.

“그건 안 되겠네요. 제가 오늘 한정판을 입고 와서. 피라도 튀면 마음 아프잖습니까.”

“……진짜 아프게 해 드려요?”

대화를 이어 갈수록 내상을 입은 것처럼 속이 쓰리고 뒷골이 당긴다. 차라리 몬스터와 싸우는 게 낫지.

성큼 앞으로 한 걸음 내딛는 내게 최 팀장이 한 마디를 툭 던졌다.

“후퇴도 또 하나의 방법입니다.”

한정판 장비에 피 튈까 봐 뒤에서 팔짱만 끼고 있는 인간이 제법 맞는 말을 한다. 처맞는 말.

그리고…….

“더 좋은 방법이 있는데 뭐 하러요?”

저 앞. 리자드맨 대족장을 필두로 몬스터들이 파도처럼 밀려오고 있다. C급과 D급 몬스터가 뒤섞인, 평범한 C급 헌터라면 맞설 엄두도 못 낼 전력이었다.

평범한 C급 헌터라면, 말이다.

‘상태창 오픈.’

띠링.

시스템이 즉각 응답했다.

헌터 일을 다시 시작하고 일주일이 지난 지금, 상태창에는 40레벨이라는 숫자와 맨 밑에 적힌 글씨가 반짝반짝 빛나고 있었다.



- 잔여 포인트 : 100



현실로 돌아온 이래 나는 한 번도 잔여 포인트를 쓰지 않았다. 순전히 호기심 때문이었다. 지금의 내가 어디까지 갈 수 있을까, 하는 의문.

하지만 이 이상 아끼는 건 만용이다.

‘근력, 체력에 각각 30. 민첩에 40 부여.’

다음 순간, 잔여 포인트가 바닥을 드러냈다.

하지만 그와는 반대로 내 몸속 깊숙한 곳에서는 새로운 힘이 솟구쳤다. 불과 몇 초전의 진태경과는 또 다른 내가 지금 이곳에 있었다.

‘그래, 이거지.’

희열감에 몸이 부르르 떨리던 그때.

- 크아아아!

리자드맨 대족장이 포효와 함께 돌진했다. 그림자를 드리운 거대한 철퇴를 향해, 나는 창을 뻗었다.

“일섬(一晱).”

창날의 끝에서, 바람의 길이 열렸다.



* * *



“허.”

최 팀장, 최민우는 헛웃음을 흘렸다.

늪지대를 감싸 안은 농밀한 피 안개, 그리고 그 아래 널브러진 몬스터들의 사체가 그의 눈에 비쳤다.

‘이게 무슨.’

보스 몬스터를 포함한 수십 마리의 몬스터가 한순간에 몰살당했다. 이 모든 게 고작 며칠 전 재각성한 C급 헌터의 창끝으로부터 벌어진 일이었다.

‘이런 게 가능한가?’

진태경을 처음 만난 날부터 품고 있던 의문이었다. 별생각 없이 E급 게이트에 갔던 그날, C급 헌터 두엇은 달라붙어야 하는 레어 몬스터를 압도적으로 밀어붙이던 그 모습.

거기에 더해 지난 며칠 동안 그가 보여 준 힘은…….

‘C급 헌터라니, 웃기지도 않지.’

진태경과 단둘이 레이드를 시작한 이유는 간단했다.

이 흥미로운 인물의 한계를 보기 위해서. 그리고 다른 이들에게 들키지 않기 위해서.

그러나 문득 그런 생각이 들었다.

‘혹시 나보다…….’

아니, 아니다. 그럴 리가 없다.

애써 이어지는 생각을 털어 내는 최민우의 눈에 진태경이 들어왔다. 그는 상반신이 날아간 보스 몬스터의 사체를 붙잡고 애통한 외침을 토해 내고 있었다.

“안 돼! 내 가죽! 이거 비싼 건데!”

……저런 인간이 그럴 리가 없지. 아니, 그러면 안 되지.

최민우는 문득 억울해졌다.



* * *



불타는 금요일. 줄여서 불금.

20대 청춘들은 무리지어 술 마시고, 클럽을 들락거리겠지만 나는 최 팀장과 게이트를 돌았다.

오전에 한 번. 오후에 두 번. 그렇게 C급 게이트 세 번을 돌고 나오자 밖은 이미 어두운 밤이었다.

“고생하셨습니다, 도련님.”

이제는 익숙한 얼굴이다. 선 굵은 외모의 이 40대 아저씨를 최 팀장은 이렇게 불렀다.

“김 집사님도 수고하셨어요.”

김 집사. 비서도 아니고 집사다.

워낙 현실성 없는 단어라 처음에는 잘못 들은 줄 알았다.

‘나는 교회 집사밖에 못 만나 봤는데.’

그는 일주일 용돈으로 천 원을 받던 나의 코흘리개 시절, 십일조로 백 원을 내라고 강요하던 불한당이었다.

물론 나를 도련님이라고 불러 주지도 않았고, 심지어는 내가 십일조를 내기 싫다고 버티자 사탄의 자식이라고 중얼거렸다.

그리고 일곱 살이었던 나는 궁금한 건 꼭 물어보는 성격이었다.



‘엄마. 엄마가 사탄이야?’

‘응? 사탄?’

‘어. 교회 집사님이 그랬는데, 내가 사탄의 자식이래. 난 엄마 자식이니까 엄마가 사탄이지? 그치?’



그 말이 엄마를 사탄으로 만들었다. 나는 두 번 다시 교회 떡볶이를 못 먹게 됐고 교회 집사는 주님 곁으로 갈 뻔했다.

다시 생각해 보니 인생 진짜 버라이어티 하네.

“하실 말씀이라도……?”

김 집사의 말에 정신을 차렸다.

“아무것도 아닙니다. 잠깐 다른 생각 좀 하느라.”

“이제 퇴근합시다.”

최 팀장은 어느새 사복 차림으로 갈아입었다. 얇은 맞춤 정장을 입은 모습이 꼭 연예인 같다.

‘인생 진짜. 더럽게 불공평하네.’

나는 내심 투덜거리며 장비를 벗기 시작했다. 물론 조심스러운 손길로. 첫날 검색해 봤는데 가격이…… 됐다, 말을 말자.

김 집사가 장비를 건네받아 차에 싣는 사이, 나는 최 팀장에게 물었다.

“내일은 몇 시에 나와야 합니까?”

“내일 말입니까?”

최 팀장이 의아한 듯한 목소리로 되묻는다.

“오늘 금요일입니다.”

“네.”

“내일은 토요일이고요.”

“금요일 다음이 토요일인 건 저도 알죠.”

이게 누굴 병신으로 보나.

“아니, 그러니까.”

최 팀장이 눈썹을 찡그렸다.

“설마, 주말도 일하시게요?”

“……당연한 거 아니에요?”

“…….”

“…….”

최 팀장이 충격받은 얼굴로 물었다.

“아니, 주말에 안 쉬면 언제 쉽니까?”

“음. 일 못 구할 때?”

“그게 얼마나 되는데요.”

“글쎄요. 많이 쉬면 한 달에 한 번?”

“길드 소속이었잖습니까. 주말에도 출근했어요?”

“했죠. 일 있으면.”

“그거 헌터 근로법 위반 아닙니까?”

완벽해 보이던 최 팀장도 모르는 게 딱 하나 있었다.

세상 물정.

나는 피식 웃었다.

“그거 꼬박꼬박 지키는 중소 길드가 어디 있어요. 다들 추가 수당 더 얹어 주고 레이드 시키지. 뭐, 저야 좋지만.”

“예? 좋다고요?”

“주말에는 인력 사무소 가거든요. 그거 갈 바에야 길드에서 추가 수당 받는 게 훨씬 나으니까. 기록 남을까 봐 현찰로 딱딱 주고.”

“…….”

“뭐, 다 그런 거죠.”

최 팀장이 고개를 절레절레 저었다.

“우리 길드는 근로법 준수합니다. 가계약도 마찬가지예요.”

그거 아쉽네. 이번 주말에는 인력 사무소에 가야 할 모양인가 보다.

입맛을 다시는 나를 최 팀장이 특유의 묘한 눈빛으로 바라본다.

“그렇게까지 하는 이유가 뭡니까?”

“이유?”

“이제 C급 헌터잖아요. 좀 쉬면서 해도 될 텐데요.”

“그건…….”

시스템이 언제 사라질지 몰라서요.

목구멍에서 불쑥 튀어나오려는 말을 붙잡았다. 그건 누구한테도 말할 수 없는 나만의 비밀이다.

“별 이유 없어요. 물 들어왔을 때 노 저어야죠.”

“그렇게 일하다가는 노 부러집니다. 같이 배 타고 있는 사람도 생각하세요.”

“같이 타고 있는 사람? 최 팀장님이요?”

“뭐, 이를테면…….”

최 팀장이 멈칫하더니 말을 이었다.

“가족이라든가.”

가족.

고작 한 단어일 뿐인데, 몸 구석구석 온기가 스며든다. 통화는 가끔 하지만 벌써 두 달이 넘도록 보지 못했다. 무림에서의 시간까지 포함한다면 석 달이다.

‘벌써 그렇게 됐나.’

아버지가 돌아가신 이후 내 인생은 줄곧 오르막길을 달리는 차 같았다.

그래서 엑셀만 밟을 수밖에 없었다. 발을 떼면 굴러떨어질 것 같아서. 금방이라도 시동이 꺼질 것 같아서.

“아무튼 주말은 쉽니다. 인력 사무소 갈 생각하지 말고 쉬세요. 그거 계약 위반이니까.”

“아, 네.”

이렇게까지 억지로 쉬라는 거 보면 최 팀장 이 인간, 은근히 인성이 괜찮은…….

아니지, 겨우 이 정도 감성 팔이에 넘어가면 안 되지. 그동안 나 혼자 어떤 개고생을 했는데.

‘최 팀장은 악덕 고용주다. 악덕 고용주.’

주말에 쉬라는 것도 당장 다음 주부터 대차게 부려 먹기 위함인 게 뻔했다. 엄한 데 체력 소모하지 말라는 노예 농장주의 마음가짐인 거지. 지독한 인간.

“준비 끝났습니다, 도련님.”

그때 장비를 실으러 갔던 김 집사가 돌아왔다.

저 양반도 악덕 고용주 밑에서 고생이다. 밤 열 시가 다 돼 가도록 퇴근을 못 하고 있네.

“아, 말씀드린 건요?”

“가져왔습니다.”

“드리세요.”

악덕 고용주의 말에 김 집사가 손에 든 작은 박스를 내밀었다.

“받으시죠, 헌터님.”

나한테.

“예? 저요?”

보기에는 드링크병 박스 같은데. 눈만 끔뻑거리다가 머릿속을 번뜩 스치는 생각이 있어 조심스레 물었다.

“설마 이거 돈이에요?”

“주급으로 계약했잖습니까. 잊으셨어요?”

깜빡했다. 당연히 일요일에 받을 줄 알았거든.

나는 얼떨떨한 얼굴로 박스를 받아 들었다. 묵직하다.

“보통 현금 지급인가요?”

“당연히 아니죠.”

“그럼…….”

“진태경 씨가 현금이 좋다면서요. 특히 빳빳한 신권.”

어제였나, 그저께 흘리듯이 얘기한 건데 이런 식으로 돌아올 줄이야. 악덕 고용주에서 평가가 조금 더 올라갔다.

‘물론 가장 중요한 게 남았지.’

화요일부터 금요일까지. 총 4일 치 급여다. C급 헌터로서 받는 첫 주급이고. 금액이 기대될 수밖에 없다.

꿀꺽. 침을 삼키고 입을 열었다.

“그럼 이게 다 얼마…….”

“계약서보다 좀 더 챙겨 넣었습니다. 안에 정산 내역 있으니까 확인해 보시고요. 이만 갑니다.”

“다음에 또 뵙겠습니다, 헌터님.”

최 팀장과 김 집사가 쌩하니 사라졌다.

그야말로 순식간에 벌어진 일.

황당한 얼굴로 멀어지는 자동차 불빛을 바라보던 나는 드링크 박스를 열었다. 흐릿한 달빛 아래 두툼한 지폐 묶음이 눈에 들어온다.

‘하나, 둘, 셋…….’

숫자는 여섯에서 더 이상 올라가지 않았다.

백 장 묶음 여섯 개. 그러니까 6백만 원이다.

“뭐야, 이게.”

사기.

순간 뇌리를 스친 단어에 다리 힘이 풀리려는 찰나.

“어?”

내가 잘못 봤나? 왜 지폐 색깔이 누렇지?

“잠깐, 잠깐만!”

공력을 눈에 집중시키자 눈앞이 밝아진다. 그리고 봤다.

지폐 속, 한복을 입고 인자하게 웃고 있는 아주머니를.

“으아어어어! 신사임당! 현모양처! 아들이 율곡 이이! 남편은 이원수!”

나도 모르게 방언이 터져 나온다. 미쳤다. 이건 미쳤어.

신사임당 백 장이 한 묶음. 그게 여섯 개니까…….

“사, 삼억!”

이번에는 풀리는 다리를 붙잡지 못했다. 쿵, 소리가 날 만큼 세게 무릎을 꿇은 나는 넋 나간 눈빛으로 드링크 박스 안을 바라봤다.

지폐 묶음 밑, 흰 종이가 박스 바닥에 깔려 있었다.

‘맞다. 정산서!’

허겁지겁 종이를 펼쳤다.

그곳에는 지난 4일간의 수익이 빠짐없이 기록되어 있었다.

내게 지급되는 최종 금액까지.

‘정산서에는 3천만 원으로 나와 있는데?’

뭐지? 착각했나?

혼란하다, 혼란해. 흔들리던 내 동공이 마지막 줄에 가서 딱 멈췄다.



보너스 : 270,000,000



그리고 최 팀장이 떠나며 남겼던 마지막 말까지.



‘계약서보다 좀 더 챙겨 넣었습니다.’



쿠르릉.

머릿속에서 천둥 번개가 휘몰아친다. 나는 후들거리는 다리로 일어났다. 저 멀리, 이미 희미해진 차의 불빛이 보인다.

그건 마치 한 줄기 빛 같았다.

“아아. 아아아…….”

최 팀장. 아니, 그는 ‘빛’이다.
```

## Current accepted English baseline

```markdown
# Chapter 51

Swish, swish, swish!

Swords, axes, maces.

Dozens of weapons poured down like rain. But I could see every one of them clearly—where each attack was headed, and how.

I slipped through the gaps.

Slice—

It started with me taking the head off a C-rank monster, a Lizardman Warrior. The instant the spearhead drew a semicircle, blood spurted in every direction.

Ding. Ding. Ding.

> **System**
>
> - You defeated **Lv. 40 Lizardman Warrior**!
>
> - You defeated **Lv. 41 Swamp Lizardman**!
>
> - You defeated **Lv. 40 Swamp Lizardman**…

- Keeee…

The survivors hesitated and backed away. The same creatures that had been pouring out killing intent at the enemy of their kin were now trembling with fear.

But that lasted only a moment.

- Gwoooaar!

> **System**
>
> - Boss Monster, **Lv. 52 Lizardman Great Chieftain**, has appeared!
>
> - Uses Skill **Battle Cry**!

A frame at least twice as large as the others. The roar of the Lizardman Chieftain, gigantic mace in hand, exploded through the air. The Lizardmen that had been backing away came to their senses at their leader’s appearance and formed ranks.

*I was wondering why this was wrapping up so easily.*

Team Leader Choi’s unhurried voice came from behind me.

“Can you handle it?”

“Is that something someone who hasn’t lifted a finger for days should be asking?”

“This is a different story. It’s a C-rank Gate.”

“Then help, why don’t you.”

Team Leader Choi thought it over before answering.

“I don’t think I can. I wore a limited edition today. It’d break my heart if blood splattered on it.”

“……Should I make it hurt for real?”

The longer we talked, the more my gut burned and the back of my head throbbed, like I’d taken internal injuries. Fighting monsters would have been better.

As I took a long stride forward, Team Leader Choi tossed out a single line.

“Retreat is another option.”

The man standing behind me with his arms folded so blood wouldn’t splatter on his limited-edition Equipment had said something pretty sensible.

A punchable kind of sensible.

And then…

“Why bother, when there’s a better way?”

Ahead of us, the monsters were surging forward like a wave, led by the Lizardman Great Chieftain. C- and D-rank monsters mixed together—a force an ordinary C-rank Hunter wouldn’t even dream of facing.

An ordinary C-rank Hunter, that is.

*Status Window, open.*

Ding.

The System answered at once.

A week had passed since I’d started Hunter work again. On the Status Window, the number 40 and the line written at the very bottom were shining bright.

> **System**
>
> - Remaining Points: 100

Since returning to reality, I hadn’t spent a single Remaining Point. Purely out of curiosity.

*How far can I go as I am now?*

But hoarding them any further would be reckless.

*Assign 30 each to Strength and Stamina. Assign 40 to Agility.*

The next moment, my Remaining Points hit zero.

In exchange, new power surged up from deep inside me. A different me from the Jin Taekyung of only a few seconds ago was standing here now.

*Yeah. This is it.*

My body was still shivering with exhilaration when—

- Gwaaaar!

The Lizardman Great Chieftain charged with a roar. I thrust my spear toward the gigantic mace that cast a shadow over me.

“One Flash.”

At the spearhead, a path through the wind opened.

* * *

“Hah.”

Team Leader Choi—Choi Minwoo—let out a hollow laugh.

A dense fog of blood wrapped the wetlands, and beneath it the monsters’ corpses lay sprawled.

*What the hell…*

Dozens of monsters, the boss included, had been slaughtered in an instant. All of it had come from the spear-tip of a C-rank Hunter who had reawakened only a few days ago.

*Is something like this even possible?*

It was a question he had carried since the day he first met Jin Taekyung.

That day, they had gone to an E-rank Gate without much thought. There, Taekyung had overwhelmingly overpowered a Rare Monster that normally took a couple of C-rank Hunters to bring down.

And on top of that, the strength he had shown over the past few days was…

*Calling him a C-rank Hunter is a joke.*

The reason Choi had started raiding with Taekyung alone was simple.

To see this fascinating man’s limits.

And to keep anyone else from finding out.

But another thought suddenly occurred to him.

*Could he be stronger than me…?*

No. No.

That was impossible.

Choi Minwoo forced the thought aside. That was when Jin Taekyung entered his vision.

He was clutching the boss monster’s corpse—its upper body gone—and wailing in grief.

“No! My hide! This was expensive!”

……There was no way a guy like that could be.

No. He *mustn’t* be.

Choi Minwoo suddenly felt cheated.

* * *

Burning Friday. *Bulgeum*, for short.[^1]

People in their twenties would be drinking in packs and drifting in and out of clubs. I was running Gates with Team Leader Choi.

Once in the morning. Twice in the afternoon.

By the time we finished three C-rank Gates and came back out, it was already dark.

“Good work, young master.”

That face was familiar now. Team Leader Choi called this broad-featured man in his forties that.

“You worked hard too, Mr. Kim.”

Kim the Butler. Not secretary—*butler*.[^2]

The word was so absurdly unrealistic I thought I’d misheard it at first.

*I’ve only ever met church deacons.*

Back when I was a snot-nosed kid getting a thousand won a week in allowance, he had been the bastard who forced me to put in a hundred won as a tithe.

Of course, he hadn’t called me young master. When I dug in and refused to pay, he’d even muttered that I was the child of Satan.

And I had been seven—the kind of kid who always asked when he was curious.

*Mom. Are you Satan?*

*Huh? Satan?*

*Yeah. The church deacon said I was Satan’s child. I’m your kid, so that makes you Satan, right? Right?*

That turned my mother into Satan.

I never got to eat the church tteokbokki again,[^3] and the church deacon nearly went to be with the Lord.

Thinking about it again, my life really was one hell of a variety show.

“Did you have something to say…?”

Butler Kim’s voice pulled me back.

“Nothing. I was just thinking about something else.”

“Let’s call it a day.”

Team Leader Choi had already changed into street clothes. In a thin tailored suit, he looked just like a celebrity.

*Life is so damn unfair.*

I grumbled inwardly as I started taking off my Equipment. Carefully, of course. I’d looked up the price on the first day, and it was…

Never mind. Let’s not go there.

While Butler Kim took the Equipment and loaded it into the car, I asked Team Leader Choi,

“What time should I come in tomorrow?”

“Tomorrow?”

Team Leader Choi asked back, sounding puzzled.

“Today is Friday.”

“Yes.”

“And tomorrow is Saturday.”

“I know Saturday comes after Friday.”

*Does he take me for a fucking idiot?*

“No, I mean…”

Team Leader Choi furrowed his brow.

“Don’t tell me you’re planning to work on the weekend too?”

“……Isn’t that obvious?”

“……”

“……”

Team Leader Choi asked with a shocked look,

“If you don’t take weekends off, when do you rest?”

“Um. When I can’t find work?”

“How often is that?”

“I don’t know. If I take a lot of time off, maybe once a month?”

“You used to belong to a Guild. You worked weekends then too?”

“I did, if there was work.”

“Isn’t that a violation of the Hunter Labor Law?”

Even Team Leader Choi, who seemed perfect, didn’t know one thing.

How the world actually worked.

I chuckled.

“What small or midsize Guild follows that to the letter? They all throw on extra pay and send you out on raids. Worked out for me, anyway.”

“Excuse me? You *liked* it?”

“I go to the Manpower Office on weekends. Getting extra pay from the Guild beats going there. They paid cash on the spot so there wouldn’t be a record.”

“……”

“That’s just how it is.”

Team Leader Choi shook his head in disbelief.

“Our Guild follows the Labor Law. Provisional contracts are no different.”

*That’s a shame. Looks like I’ll have to go to the Manpower Office this weekend.*

Team Leader Choi looked at me with that peculiar expression of his as I smacked my lips over the missed chance.

“Why do you go that far?”

“Why?”

“You’re a C-rank Hunter now. You could take it a little easier.”

“That’s…”

*Because I don’t know when the System might disappear.*

I caught the words before they jumped out of my throat. That was my secret—something I couldn’t tell anyone.

“No particular reason. You have to row when the tide comes in.”

“If you keep working like that, you’ll snap the oars. Think about the people in the boat with you.”

“The people in the boat with me? You, Team Leader?”

“Well, for example…”

Team Leader Choi paused, then went on.

“Your family, perhaps.”

Family.

It was only one word, but warmth seeped into every corner of my body. We talked on the phone now and then, but I hadn’t seen them in more than two months. Counting the time in Murim, it had been three.

*Has it already been that long?*

Ever since my father died, my life had been a car running uphill.

So I’d had no choice but to keep my foot on the gas. Take it off, and it felt like I’d roll backward. Like the engine might die at any second.

“Anyway, weekends are off. Don’t even think about going to the Manpower Office. Rest. That would be a contract violation.”

“Ah. Right.”

*Forcing me to rest this hard… Maybe this guy Choi isn’t such a bad person after all…*

No.

I couldn’t let myself get taken in by a little emotional appeal. Not after all the hell I’d gone through on my own.

*Team Leader Choi is an exploitative employer. An exploitative employer.*

It was obvious he only wanted me resting on the weekend so he could work me to the bone starting next week. The mindset of a slave plantation owner who didn’t want stamina wasted in the wrong places.

What a vicious man.

“Preparations are finished, young master.”

Butler Kim was back from loading the Equipment.

*That man’s suffering under an exploitative employer too. It’s almost ten at night, and he still hasn’t gotten off work.*

“Ah. What about the thing I mentioned?”

“I brought it.”

“Give it to him.”

At the exploitative employer’s word, Butler Kim held out the small box in his hands.

“Please take this, Hunter.”

To me.

“Huh? Me?”

It looked like a box of tonic drinks. I just blinked at it, then a thought flashed through my head and I asked carefully,

“Don’t tell me this is money?”

“We contracted for weekly pay. Did you forget?”

I had. I’d naturally assumed I’d get it on Sunday.

I took the box with a dazed look. It was heavy.

“Is it usually paid in cash?”

“Of course not.”

“Then…”

“You said you liked cash, Mr. Jin Taekyung. Especially crisp new bills.”

I’d mentioned it in passing yesterday—or the day before. I hadn’t expected it to come back like this.

My opinion of the exploitative employer rose a little.

*Of course, the important part’s still left.*

Four days of pay, Tuesday through Friday. My first weekly paycheck as a C-rank Hunter.

Of course I couldn’t help looking forward to the amount.

I swallowed and opened my mouth.

“Then how much is all of this…”

“We put in a little more than the contract. The settlement details are inside, so check them. We’ll be going.”

“Until next time, Hunter.”

Team Leader Choi and Butler Kim took off in a flash.

It really did happen in an instant.

I stared after the receding car lights, bewildered, then opened the drink box. In the faint moonlight, thick bundles of bills caught my eye.

*One, two, three…*

The count stopped at six.

Six bundles of a hundred bills.

In other words, six million won.

“What is this?”

*Scam.*

The word flashed through my mind, and just as my legs were about to give out—

“Huh?”

Had I seen it wrong? Why were the bills yellowish?

“Wait. Wait a second!”

I focused internal energy into my eyes, and the world in front of me brightened.

Then I saw her.

A kindly smiling woman in a hanbok, right there on the bill.

“Shin Saimdang! Wise mother and virtuous wife! Her son is Yulgok Yi I! Her husband is Yi Wonsu!”

Dialect burst out of me before I knew it.

This was insane. Completely insane.

One bundle was a hundred Shin Saimdang bills. Six of those, so…

“Th-three hundred million!”

This time I couldn’t catch my legs as they gave out. I dropped to my knees hard enough to thud and stared blankly into the drink box.

Under the bundles, a white sheet of paper lined the bottom.

*Right. The settlement sheet!*

I unfolded the paper in a panic.

It had a complete record of the past four days’ earnings.

Down to the final amount being paid to me.

*The settlement says thirty million won?*

What? Had I imagined it?

I was confused. Completely confused.

My shaking gaze froze on the last line.

**Bonus: 270,000,000**

And then Team Leader Choi’s last words as he left.

*We put in a little more than the contract.*

Thunder and lightning tore through my head.

I stood on trembling legs. Far off, the car’s lights were already fading.

They looked like a single ray of light.

“Ahh. Aaaah…”

Team Leader Choi.

No—he was the Light.

[^1]: Korean slang for Friday night, from “burning Friday.”
[^2]: In Korean, the same word, *jipsa*, means both butler and church deacon.
[^3]: Tteokbokki is a Korean dish of chewy rice cakes in a spicy sauce. Korean churches often sell it as a snack.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 51`.

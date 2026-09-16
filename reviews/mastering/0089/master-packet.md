# Master Edit Task — Chapter 89

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
| 조필     | **Jopil**          |
| 삼류     | **Third Rate**    |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 내공     | **internal energy**                              |                                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 살기     | **killing intent**                               |                                                       |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 아이템              | **Item**                       |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 팀장      | **Team Leader**       |
| 힐러      | **healer**            |
| 대사      | **Master** for a senior Buddhist monk                           |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 뭐랄까 | comedy | Keep the hesitation beat; do not delete the hedge before the realization. | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 80–84

## Plot

During a safety-inspection period following a fatal Gate accident, the Peace Guild bribes its way into the B-rank Gate **The Minotaur’s Labyrinth** alongside Sangdong Guild’s fifteen-person raid team. The team includes seven B-rank Hunters; Im Kkeokjeong is registered as an E-rank tank despite the danger, while Butler Kim vouches for his twenty years of experience.

Upon entry, Jin Taekyung receives the restricted **B-rank Gate Clear Quest**, whose first-clear Reward and failure condition remain undisclosed. Team Leader Choi equips the Peace Guild with powerful loaned gear, including Taekyung’s Peak-grade Masterwork Black Drake Leather Set and Masterwork Black Thorn Spear. Kkeokjeong receives Matador’s Full-Body Armor and Matador’s Shield, which provide bonuses against bovine monsters.

Eight Minotaur Warriors emerge from five cavern holes, overwhelming Sangdong’s advance. Im Changsoo, Sangdong’s Level 65 team leader and Guild Master’s son, mocks Taekyung and deliberately misnames him Jang Taekyung. Taekyung answers by calling him Shit Changsoo, escalating their hostility. When Changsoo’s attempts to court Song Song fail, he challenges Taekyung to defeat the eight Minotaurs alone: 500 million won per monster, all byproduct rights, and Song Song’s transfer to Sangdong Guild as the additional stake. Song Song rejects Changsoo’s womanizing, money-flaunting character but accepts the wager, which the Guild Master and Choi also approve.

Taekyung accepts after judging that he can win. He crosses the cavern instantly, beheads one Minotaur, and kills all eight, triggering Bleeding and a Level Up. Changsoo agrees to pay the promised 4 billion won and surrender the byproducts. After Taekyung recalls Changsoo’s behavior toward Song Song, Changsoo draws his sword but is disarmed and subdued. He agrees to apologize to Taekyung and the Peace Guild. Taekyung openly identifies himself as both a Hunter and a Murim martial artist.

## Continuity

- The Peace Guild has entered The Minotaur’s Labyrinth with Sangdong Guild as a fifteen-person raid team.
- The B-rank Gate Clear Quest is active for Taekyung; its Reward and failure condition are unknown.
- Taekyung is using the Masterwork Black Drake Leather Set and Masterwork Black Thorn Spear. The set grants Strength, Stamina, Agility, and Toughness +10; the spear has a 90% chance to inflict Bleeding on hit.
- Im Kkeokjeong is serving as the front-line tank with Matador’s Full-Body Armor and Matador’s Shield.
- Im Changsoo is Sangdong Guild’s Level 65 team leader, the Guild Master’s son, and a notorious womanizer nicknamed Horndog. He treats his subordinates abusively and sponsors the C-rank mage Hye-rin.
- Song Song rejected Changsoo’s romantic advance but agreed to transfer to Sangdong Guild if Taekyung lost the wager.
- Taekyung defeated all eight Minotaurs, received a Level Up, and won the wager. Changsoo owes him 4 billion won and all byproducts and agreed to apologize; whether he fulfills these promises remains unresolved.
- Team Leader Choi has recognized that Taekyung’s abilities and conduct are inconsistent with an ordinary C-rank Hunter.
- Taekyung’s identity as both a Hunter and Murim martial artist is now known to Changsoo and the surrounding raid members.

## Translation Decisions

- Retain **Peace Guild**, **Sangdong Guild**, **Hunter Association**, **The Minotaur’s Labyrinth**, **Minotaur Warrior**, **Black Drake**, **Masterwork Black Drake Leather Set**, **Masterwork Black Thorn Spear**, **Bleeding**, **artifact**, **Peak**, **Matador’s Full-Body Armor**, **Matador’s Shield**, **Taunt**, and **Hallucination**.
- Retain **Shit Changsoo** for the insulting surname pun and **Horndog** for Changsoo’s nickname.
- Use **Top-tier** for 초일류 and **First Rate** for 일류.
- Render 껄떡쇠 as **lech** and retain **oppа** in Changsoo’s coercive, possessive speech.
- Retain the **baram** wind/infidelity pun with a concise footnote, and use **big bills** for 큰 거.
- Render 발설지옥 as **tongue-pulling hell**, with a footnote explaining its Buddhist punishment reference.

### Prior accepted reading-copy tails

#### Chapter 87 tail (verified mastered)

…
she’s taking it out on her.* *She should watch the counter properly herself in the first place. How many orders did Jeonghee take while she was off having fun?* They had plenty to say, but they could only keep it to themselves. The kitchen ajumma who had finally lost her patience and stood up for Kim Jeonghee had been fired the previous week. “How am I supposed to feel comfortable leaving this place in your hands?” “…I’m sorry.” “I heard your son is a Hunter. He should be making decent money, so why don’t you just stay home and cook? Why come all the way here and be a nuisance to someone else’s business? Ah, is his income not very good because he’s an F-rank Hunter?” The moment a sneer appeared at the corners of the owner’s mouth, Kim Jeonghee slowly raised her bowed head. “Boss. You’ve gone too far.” “What?” “I said you went too far.” “Are you saying I said something wrong?” “Yes.” The unfamiliar sensation left the owner speechless. Kim Jeonghee had always been quiet and gentle, but now her eyes had sunk into a deep stare. “Please apologize for what you just said.” “A-apologize?” “Right here. Right now.” “O-oh my. Fine, then. What part of what I said was wrong? Your son really is an F-rank Hunter!” “Is his rank really that important?” “Of course it is. What good is an F-rank Hunter? You have to be at least my son’s caliber to make good money and have women lining up for you. This shop, too…” “Your son, the D-rank Hunter, opened it for you. I know. I’ve heard it dozens—no, hundreds—of times.” The employees, who had pricked up their ears, unconsciously nodded. The owner’s bragging about her son was a familiar routine they heard several times a day. How much he made, how big his house was, what kind of car he drove, and how filial he was—so filial that he had even opened a shop for his mother to have something to do. She had repeated it so often that even the regular customers were sick of hearing it. “Then you know all about it. I run this place as a hobby, but you’re different, aren’t you? You’re working in the kitchen because your son doesn’t make enough money, aren’t you?” “No. That’s not why.” Kim Jeonghee continued calmly. “Our Taekyung grew up right. He never once caused his parents any trouble, even when he was little. He’s still working hard for his family. Money? He earns more than enough.” “That’s all an excuse.” “An excuse? This is money my child earned by risking his life. How could I, as his parent, accept it and spend it?” “Ajumma, was that meant for me to hear?” “That depends on how you choose to take it. And since we’re on the subject, when does that amazing son of yours ever show his face?” “Wh-what?” “I’ve worked here for over a year, but that devoted son of yours hasn’t visited even once. He does at least call you, doesn’t he?” The kitchen fell deathly silent. The owner’s face turned bright red, and her eyes bulged. “Where does a bitch with such a pathetic son get off—” The employees knew what was coming next. Along with the owner’s machine-gun burst of abuse, the word “fired” was bound to come flying out. But none of them could have predicted Kim Jeonghee’s reaction. “Watch your mouth, you goddamn bitch.” “…!” “…!” It was as if a bomb had gone off. A deathly silence descended as everyone’s eyes trembled with disbelief. Every person in the kitchen wondered if they had heard correctly. *What did I just hear?* *Did Jeonghee ajumma just swear? My God.* Kim Jeonghee had always been gentle and quick to smile. Even when the owner picked fights with her day after day, she had bowed her head without a single word of complaint. Now she glared at the owner with eyes as cold as ice. “W-what did you say? What did you just call me?” “I called you a goddamn bitch, you fucking bitch.” “F-fucking bitch?!” Before the shock had even faded, a second bomb went off. The owner’s shriek rang all the way out into the dining area. “Did someone just swear?” “You heard that too? I think someone just called somebody a fucking bitch.” “What the hell? Are the employees fighting?” The murmuring grew louder. Customers and employees alike turned their attention toward the kitchen. That was when it happened. Thud. Thud. A large young man with his cap pulled low. No one had noticed when he entered, or how long he had been standing there. Not until he started walking toward the kitchen. “S-sir. I’ll take your order…” The young man smiled faintly at the male employee who hurried to block his path. “It’s all right. I’m not here to order.” “No, but still, right now…” “Excuse me.” Tap. It was only a gentle push, but the burly employee staggered and fell. Without hesitation, the young man shoved the half-open kitchen door wide. And then… “Mom.” He came face-to-face with the person he loved most in the world. [^1]: A goshiwon is a tiny, inexpensive room-for-rent housing arrangement, often with shared facilities. [^2]: *Ajumma* is a familiar Korean term for a married or middle-aged woman, commonly used by customers or employers to address service workers.

#### Chapter 88 tail (verified mastered)

…
the owner examined the thin silver card I handed her, her mouth fell open. “…C-rank Hunter?” “Personally, I think rank is everything for Hunters. What do you think, Boss?” “N-no way. I heard you were F-rank…” “I was F-rank. I’m C-rank now. You’re pretty slow about updating your information.” “I-isn’t this fake? The color is completely different from my Minsu’s license!” “His license is brass-colored, right?” “…” “I used one of those myself in the past. Lower-rank Hunters have brass-colored licenses, while mid-rank Hunters have silver ones. You didn’t know that?” Suppressed laughter erupted from all around us. The atmosphere had flipped in an instant. My mother slipped her arm through mine with a proud smile, while the owner’s face turned bright red and she began making excuses. “D-does a Hunter’s rank really matter? C-rank and D-rank are only one step apart. They’re practically the same.” *Was that supposed to be an argument or a fart?* All I could do was laugh hollowly at her absurd struggle. “That’s not something a person who looked down on someone for their Hunter rank should be saying.” “Is a person’s title all that matters? The company they work for matters more. People respect an Assistant Manager at a major corporation more than a section manager at a small company. Am I wrong?” “I don’t know about that, but the customers here don’t seem to agree with you.” I gestured toward the customers filling the dining area. Dozens of office workers from small and midsize companies were glaring at the owner without bothering to hide their displeasure. “What’s with that ajumma?” “My appetite’s completely gone.” “The food hasn’t even come out yet. Should we just leave?” “Yeah. Let’s go.” “Everyone, let’s eat somewhere else. There’s a decent set-meal place right up ahead. I may not be an Assistant Manager at a major corporation, but I’m a section manager at a small company, so lunch is on me.” Scrape. At the middle-aged man’s words, five or six of his subordinates stood and followed him. Similar scenes began unfolding throughout the dining area. “Customers, that’s not what I meant. Customers!” “What do you mean, it’s not? Just watch me never come back here.” “But your orders have already gone in. If you leave like this…” “Looking at that kitchen, it’ll take an hour anyway. Forget it. We’re leaving too.” Despite the dining staff’s attempts to stop them, the customers streamed out like the receding tide. Barely a minute later, fewer than ten customers remained in the dining area. *Damn. I can already hear the sound of this place going under.* The owner was trembling with anger and bewilderment. “You… You people…” “So which Guild did you say your son was with?” “Our Minsu is a real hotshot Hunter in Sangdong Guild! Someone like you…” “What? Which Guild?” “Sangdong Guild! They even gave him a house and a car.” “Oh, Sangdong Guild. Could you wait just a moment?” What an incredible coincidence. Holding back my laughter, I pulled out my smartphone and made a call. Beep. Beep. Beep. Click. “Uh, what is it?” “What do you mean, what is it? Are we only supposed to call each other when we have business?” “…I sent you the promised four billion won, though.” “Ah, I checked that. It came through fine.” The conversation continued over speakerphone, loud enough for everyone to hear. Four billion won. The moment it became clear that what I had said earlier was true, everyone’s eyes nearly popped out of their heads. I ignored all the stares and got to the point. “Do you happen to know a Kim Minsu?” “Kim Minsu? That’s the first I’ve heard of him.” “You’re a Team Leader in Sangdong Guild, and you don’t even know him? Apparently, he’s a D-rank Hunter in your Guild.” “D-rank Hunters are a dime a dozen. How am I supposed to know all of them? Is that why you called?” “Yeah. Bye.” Getting Im Changsoo’s business card in case he tried to stiff me had been a stroke of genius. Click. As soon as I hung up, the owner asked in a faltering voice. “W-who was that?” “Didn’t you hear? He’s a Team Leader in Sangdong Guild. Put simply, he’s Mr. Minsu’s boss.” “…Team Leader? His boss?” “Oh, and one more thing. He’s also a future employer Mr. Minsu will want to impress. His father is the Guild Master of Sangdong Guild.” “…” Her face went white as a sheet. There was no longer any reason or need to exchange another word with her. I turned toward my mother. “Let’s go now.” “Shall we, son?” My mother, Kim Jeonghee, flashed a broad smile and shoved her work clothes into the sink. Of course, she didn’t forget to leave the owner with one final remark. “If you’re a parent, act like one and live right, you ajumma. Where do you get off casually running your mouth about someone else’s precious child?” The final blow. The owner lowered her head without answering, and we left the restaurant with light steps. “Son, have you eaten? There’s cheonggukjang and kimchi pancakes at home.” “Wow. What a feast.” The weather was beautiful. [^1]: *Ajumma* is a familiar Korean term for a married or middle-aged woman, commonly used by customers or employers to address service workers. [^2]: A *goshiwon* is a tiny, inexpensive room-for-rent housing arrangement, often with shared facilities.

## Korean source

```text
＃89화



“아들, 천천히 먹어. 체하겠다.”

“헌터 관두고 먹방 스트리머 해도 되겠네.”

엄마의 걱정과 하연이의 감탄 속에서 식사를 끝마쳤다.

고봉밥만 다섯 그릇에 한 냄비 가득 끓인 청국장과 수십 장의 김치전이 사라진 후였다.

“휴, 이제 좀 배가 차네.”

“……미쳤나 봐. 평소에는 얼마나 먹는 거야?”

“맛있으면 끝도 없이 들어가지.”

예전에도 많이 먹긴 했지만 이 정도는 아니었다.

하지만 지금은 신진대사며 내부 장기가 전과는 비교할 수도 없이 향상되어서 그런지 어지간한 푸드파이터 저리 가라다.

“진짜 먹방 스트리머나 해 볼까.”

“아냐, 그 사람들도 먹고살아야지. 인간들끼리 경쟁하게 놔둬.”

“난 인간이 아니란 소리냐?”

“응, 내 눈에는 돼지 그 이상인데.”

혀를 내두른 하연이가 수저를 내려놨다. 밥그릇을 슬쩍 들여다보니 절반이 그대로다.

“밥 남기면 벌 받는다.”

“어르신처럼 말하네.”

“한국인은 곧 죽어도 밥심인 거 몰라? 먹어야 감기도 빨리 낫는 거야.”

“입맛이 없어. 머리도 아프고.”

“병원은?”

“다녀왔어. 처방받은 약도 먹었고.”

나는 가만히 하연이를 응시했다. 불그스름하게 달아오른 얼굴, 이마에는 땀이 송골송골 맺혀 있다. 기껏 조퇴해서 공부한답시고 버티더니 아까보다 더 열이 오른 모양이다.

‘처방받은 약이 효과가 별로 없는 것 같은데.’

솔직히 병이 낫는 가장 간단한 방법은 따로 있다.

전문 힐러에게 치료받거나, 혹은 시중에서 판매하는 포션을 마시는 것. 하지만 비싼 비용 때문에 대부분의 일반인들은 꺼리는 일이다.

‘미련하긴.’

내가 쉬지 않고 일했던 이유는 가족들이 안전하게, 아프지 않고 행복하게 살기를 바랐기 때문인데.

그 돈을 쉽게 쓰지 못하는 이유를 알면서도, 답답한 마음이 드는 건 어쩔 수 없다. 그깟 포션 한 병에 얼마나 한다고.

‘하다못해 운기조식 한 번이면 훨씬 괜찮아질…… 어라?’

문득 스치는 생각에 멈칫했다.

잠깐만, 혹시 이게 되려나?

“잠깐 손 줘 봐.”

“응?”

“쓰읍. 손 좀 줘 보라고.”

하연이가 희귀 생물을 보는 듯한 눈빛으로 나를 훑었다.

“이게 무슨 상황이지? 징그럽게 왜 이래?”

“하여간 내 말이라면 죽어도 안 듣지.”

덥석.

“우리 남매야, 알지?”

“헛소리 그만하고.”

나는 어느 때보다 신중하게 공력을 끌어 올렸다. 천천히, 아주 천천히 공력 한 줄기를 손을 따라 하연이의 몸을 향해 흘려보낸 그때.

“아!”

하연이의 탄성. 녀석도 공력이 주는 이질감을 알아챈 것이 분명했다.

순간 공력이 흩어질까 염려했지만 이미 경지에 오른 진가심법은 타인의 몸에서도 순순히 통제를 따랐다.

‘이 정도면 충분해.’

간단한 시범 테스트가 끝났으니 다음은 정규 테스트다. 이번엔 공력을 하연이의 단전으로 흘려보냈다.

평소였다면 숨 쉬는 것처럼 간단한 일이었겠지만 하연이의 신체는 달랐다. 혈도는 좁았고, 내부에는 노폐물들이 가득 끼어 있었다.

‘이건 좀 힘들겠는데.’

현대와 무림. 두 곳을 따로따로 분리하고 생각해 봐도 나는 일반인을 훨씬 뛰어넘는 신체의 소유자였다.

그러나 하연이는 평범한 고등학생. 지난 19년간 축적된 노폐물들의 존재는 어쩌면 당연했다.

‘그래도 되는 데까지는 해 봐야지.’

진가심법의 안정성과 내 통제력을 믿기에 가능한 일이다.

만약의 사태에 대비하여 하연이에게 미리 말하는 것도 잊지 않았다.

“조금 아파도 참아라, 알겠지?”

“뭐야, 뭔데?”

“음. 안정성이 굉장히 뛰어난 한의학 치료법이라고 해야 하나.”

설거지를 하던 엄마가 눈을 동그랗게 떴다.

“어머, 한의학? 아들 그런 것도 할 줄 알아?”

“그냥 좀 배웠어요.”

“잘됐네. 한번 해 봐.”

반면 하연이의 반응은 떨떠름했다.

“웬 한의학? 난 그런 거 좀 별론데.”

“그럼 나 믿고 조금만 참아 봐.”

“엄마, 그동안 키워 줘서 고마웠어. 못난 딸은 효도도 못 해 보고 가네.”

“…….”

아니, 이 새끼가?

하마터면 공력이 흐트러질 뻔했다. 한 시간을 뛰어다녀도 땀 한 방울 안 나는데 지금은 좀 덥다.

“농담이야. 설마 하나뿐인 여동생한테 안 좋은 짓이라도 하겠어?”

“그럼 입 다물고 있어. 좀 아파도 최대한 움직임 자제하고.”

“오케이.”

깊게 심호흡했다. 지금부터 하연이의 혈도를 깨끗이 청소할 생각이었다. 청소부는 나, 빗자루는 15년의 공력이다.

“준비됐지?”

“네네, 선생님. 그런데 이거 도대체 언제 시작하나요?”

“지금 바로.”

대답과 동시에 공력을 흘려보냈다.

스아아아.

부드럽고 강한 공력의 파도가 하연이의 전신 세맥을 휩쓸기 시작했다. 하연이의 몸 안 가득 쌓인 노폐물을 씻어 내리며…….



* * *



“후우.”

“푸하.”

손을 뗀 순간 동시에 터져 나온 두 개의 숨은 각각 의미가 달랐다. 나는 안도감, 하연이는 후련함이다.

띠링.



- [운기요상]을 성공적으로 완료했습니다.

- [공력]이 소량 증가합니다.



시스템의 말대로 운기요상은 성공적으로 끝났다.

진가심법은 공력 축적 속도가 느린 대신 안정성이 극히 뛰어난 내공심법. 쌓인 노폐물이 워낙 많이 탓에 다소 시간이 걸리긴 했지만 큰 위기 없이 끝냈다.

“오빠, 이게 뭐야?”

오빠 소리가 자연스럽게 나오는 걸 보니 하연이도 놀라긴 한 모양이다. 나는 긴장감 때문에 맺힌 땀방울을 닦아 내며 대답했다.

“말했잖아. 안정적인 한의학 치료라고.”

“손만 잡고 있었는데 그게 돼?”

되겠냐? 이게 다 네 오빠의 뛰어남 덕분이지.

나는 자연스럽게 화제를 돌렸다.

“그래서, 어땠어?”

“처음에는 아팠는데…… 시간이 가면 갈수록 시원해졌어. 몸도 가벼워지고 두통도 사라지고. 뭐랄까.”

미간을 좁힌 하연이가 한마디로 정의를 내렸다.

“다시 태어난 느낌? 내 안에 있던 안 좋은 기운들이 싹 씻겨 내려간다고 해야 하나. 아씨, 모르겠네.”

그 정도면 제법 정확하게 알고 있는 것 같은데?

어쨌건 확연히 나아진 안색을 보니 해 준 보람이 있다. 나는 피식 웃으며 말했다.

“어, 그럼 이제 씻고 와.”

“응?”

“응은 무슨 응이야. 너 코 막혔어? 냄새 장난 아니니까 빨리 샤워부터 하라고.”

“아침에 씻었는데 도대체 무슨 냄새가 난다는…… 악!”

자신의 몸에서 진동하는 악취를 깨달은 하연이가 코를 움켜쥐고 난리법석을 피운다.

‘자연스러운 일이지.’

몸 안에 있던 노폐물들이 어디로 가겠나. 다 몸 밖으로 분출되는 거지. 이를테면 땀이라든가, 아니면…….

꾸르륵. 뽕.

뭐, 저렇게도 나오는 거다.

“…….”

그런데 노폐물 양이 많아서 그런가. 냄새가 장난이 아니다.

이 정도면 똥을 싼 건 아닌지 의심해 봐야 하는 정도인데?

“아흑.”

몸을 흠뻑 적신 땀에 더해 배에서 오는 이상 신호까지. 거의 기어가다시피 화장실로 직행하는 하연이를 보며 엄마는 벌린 입을 다물지 못했다.

“세상에.”

“효과 좋죠?”

“그러게. 엄마도 어릴 때 한의원 몇 번 가 보긴 했는데 신통하다.”

“제가 잘 배워서 그래요. 혹시 한의원 가실 거면 그냥 저한테 오세요. 지금 바로 하셔도 좋고.”

“그럴까? 안 그래도 내가 요즘 소화가 잘…….”

엄마가 방긋 웃으며 손을 내준 그때였다.

부아아앙. 푸드득. 푸드득.

“…….”

“…….”

엄마가 슬그머니 손을 뺐다.

“……하연이 나오면 시작할까?”

“……네.”

우리 집은 화장실이 하나다.



* * *



쏴아아아.

화장실 물 내려가는 소리가 들리고 얼마 후, 세상 시원한 얼굴의 엄마가 나왔다.

“몸은 어떠세요?”

“10년은 젊어진 기분이야.”

결코 과장이 아니다. 열아홉 살인 하연이도 몸 안의 노폐물을 전부 배출하기까지 한 시간이 넘게 걸렸다.

중년에 접어든 엄마는 살아온 세월만큼 노폐물의 양도 많았다. 두 시간이 넘는 운기요상으로 전과는 비교할 수도 없을 만큼 몸 상태가 좋아졌을 것이다.

“그치? 나도 아까까지만 해도 머리 아프고, 어지럽고 그랬는데 지금은 싹 나았다니까? 화장실 나오자마자 열 재 봤는데 정상 체온이더라고.”

하연이가 신기한 듯이 나를 바라봤다. 녀석은 화장실에서 나오자마자 언제 입맛이 없다고 말을 했냐는 듯 밥을 두 공기나 비웠다.

“도대체 이런 건 어디서 배우는 거야? 오빠 힐러였어?”

“힐러는 무슨. 그냥 어쩌다가 배운 거지.”

“어디 한의원에서 배웠는데? 가까우면 나도 한 번 가 보게.”

“……너 거기 가면 큰일 난다.”

“왜?”

“몰라도 돼. 그냥 무서운 아저씨들 많다고만 알아 둬.”

“침을 아프게 놓나?”

“……좀 그런 편이야.”

그 침이 칼침이라는 걸 알면 저 녀석이 무슨 표정을 지을까.

나는 꼬치꼬치 캐묻는 하연이를 밀어 내며 주머니에 손을 넣었다.

‘인벤토리 오픈.’

익숙한 시스템 알림과 함께 반투명한 인벤토리창이 떴다.

만약 무림이었다면 조필을 쓰러트리고 얻은 전리품과 각종 병장기가 가득 쌓여 있었겠지만 이곳은 현실이다.

‘인벤토리가 통합되어 있으면 좋을 텐데.’

각각 인벤토리가 분리되어 있다는 게 생각할수록 아쉽다.

무림에 상급 포션 몇 개만 들고 가도 여벌의 목숨을 챙긴 거나 다름없을 테니까.

‘뭐, 레벨 업으로 어느 정도 회복할 수 있다는 것에 만족해야지.’

내심 혀를 차며 주머니에서 손을 뺐을 때, 내 손바닥에는 붉은색 액체가 찰랑거리는 작은 병 두 개가 들려 있었다.



아이템창



[하급 포션]

종류 : 치료제

등급 : 삼류

설명 : 미약한 치료 마법이 깃든 액체. 시중에서 쉽게 구할 수 있다.

효과 : 섭취 시 신체를 회복시켜 준다. 효과는 미비하다.





어제 레이드 보급품으로 지급받은 물건이다. 딱히 쓸 일이 없어 고스란히 남았던 것을 인벤토리에 넣어 뒀었다.

‘원래는 반납해야 하지만.’

아무리 하급 포션이라도 개당 20만 원이 넘어가는 고가의 물건.

최 팀장처럼 턱턱 내어 주는 후한 고용주는 찾아보기 힘들다.

“하나씩 드세요.”

“어? 포션이네.”

“뭘 또 포션까지…… 지금도 충분히 괜찮은데.”

“부작용이 있을까 봐 그래요. 지금 안 마시면 나중에 돈 더 나갈걸요.”

원기 보양 차원에서 권하는 것뿐, 사실 운기요상에 부작용은 없다.

“빨리 드세요. 하연이 너도.”

주저하던 엄마가 먼저 포션을 섭취했고, 눈치를 보던 하연이가 뒤를 이었다.

꿀꺽. 꿀꺽.

“어때?”

시원하게 원샷을 때린 하연이가 고개를 갸웃거렸다.

“힘이 좀 나는 것 같기도 하고, 아닌 것 같기도 하고. 내가 뭐 포션을 먹어 봤어야 알지.”

“엄마도 잘은 모르겠구나.”

“피곤하거나 아플 때 먹으면 효과가 확실히 느껴질 거예요. 한 박스 사다 놓을 테니까 그럴 때마다 드세요.”

“한 박스? 한 박스면 몇 개야?”

“큰 걸로 사면 50개?”

“하나에 20만 원쯤 하니까 50개면…… 천만 원? 오빠 미쳤어?”

깜짝 놀란 하연이가 내 팔뚝을 찰싹 때렸다.

“이번에 돈 좀 벌었다고 너무 막 쓰는 거 아냐? 그렇게 막 과소비하면 3억 그거 금방 사라져.”

“괜찮아. 요즘 잘 벌어.”

“내가 인터넷 검색해 봤는데 C급 헌터 되면 뭐 장비도 바꿔야 하고 그렇다며. 억 단위는 우습게 나가던데.”

“괜찮다니까. 어제도 40억 벌었어.”

“40억 있으면 이렇게 흥청망청…… 잠깐, 얼마라고?”

“40억.”

“…….”

순간 하연이의 몸이 딱 굳었다. 나를 멍한 눈빛으로 바라보던 녀석이 엄마를 향해 말했다.

“엄마, 오빠가 40억 벌었대.”

엄마는 어색하게 웃으며 고개를 끄덕였다. 그제야 하연이가 떨리는 목소리로 묻는다.

“진짜야?”

“응.”

“40억?”

“그렇다니까.”

하연이의 눈빛에 결심이 깃들었다.

“오빠. 나 학교 자퇴해도 돼?”

“…….”

배움에는 끝이 없다고 하지 않았냐?
```

## Current accepted English baseline

```markdown
# Chapter 89

“Son, slow down. You’ll make yourself sick.”

“You could quit being a Hunter and become a mukbang streamer.”

I finished my meal amid Mom’s concern and Hayeon’s admiration.

That was after five heaping bowls of rice, a whole pot of cheonggukjang, and dozens of kimchi pancakes had vanished.

“Whew. I’m finally starting to feel full.”

“……Are you insane? How much do you usually eat?”

“If it’s tasty, it just keeps going in.”

I had always eaten a lot, but never this much.

Maybe it was because my metabolism and internal organs had improved to a degree that couldn’t even be compared to before. These days, I could put even professional food fighters to shame.

“Maybe I really should become a mukbang streamer.”

“No. Those people need to make a living too. Let humans compete among themselves.”

“Are you saying I’m not human?”

“Yeah. In my eyes, you’re something beyond a pig.”

Hayeon could only shake her head in disbelief as she put down her spoon. I glanced into her rice bowl and saw that half of it was still there.

“If you leave rice, you’ll be punished.”

“You sound like an old man.”

“Don’t you know Koreans run on rice even at death’s door? You have to eat if you want your cold to go away faster.”

“I don’t have an appetite. My head hurts too.”

“Did you go to the hospital?”

“I did. I took the medicine they prescribed, too.”

I stared at Hayeon in silence. Her face was flushed, and beads of sweat had formed on her forehead. She had left school early and stubbornly tried to study, but it seemed her fever had risen even higher than before.

*The medicine she was prescribed doesn’t seem to be working very well.*

Honestly, there was a much simpler way to cure an illness.

She could get treated by a professional healer or drink a potion sold on the market. But most ordinary people avoided doing that because of the expense.

*What a fool.*

The reason I had worked nonstop was so my family could live safely, happily, and without getting sick.

Even though I knew why they couldn’t spend money so easily, I couldn’t help feeling frustrated. How much could one lousy potion cost?

*At the very least, circulating qi once would make her feel much better… Huh?*

A thought suddenly flashed through my mind, and I stopped.

*Wait. Could this actually work?*

“Give me your hand for a second.”

“Huh?”

“Tsk. I said give me your hand.”

Hayeon looked me over as if I were some rare creature.

“What is happening here? Why are you being so gross?”

“You’d rather die than listen to a word I say.”

I grabbed her hand.

“We’re siblings, okay?”

“Stop talking nonsense.”

I raised my internal energy more carefully than ever. Slowly—very slowly—I let a thread of internal energy flow along my hand and into Hayeon’s body.

“Aah!”

Hayeon let out a startled cry. She had clearly noticed the strange sensation caused by my internal energy.

I was worried that it might scatter, but the Jin Family’s Cultivation Technique had already reached a realm stage. It obeyed my control without resistance, even inside someone else’s body.

*This much should be enough.*

The simple demonstration test was over. Now came the real test.

This time, I guided my internal energy toward Hayeon’s dantian.

Under normal circumstances, it would have been as easy as breathing. But Hayeon’s body was different. Her acupoints were narrow, and her insides were clogged with waste.

*This is going to be difficult.*

Even if I separated the modern world and the Murim and considered them independently, I possessed a body far beyond that of an ordinary person.

Hayeon, however, was an ordinary high school student. The waste accumulated over her nineteen years of life was only natural.

*Still, I should do everything I can.*

I could only attempt this because I trusted the Jin Family’s Cultivation Technique’s stability and my own control.

I also remembered to warn Hayeon in advance, just in case.

“It might hurt a little, so bear with it, okay?”

“What? What are you doing?”

“Hmm. I suppose you could call it a particularly stable form of traditional Korean medicine.”

Mom, who had been washing dishes, opened her eyes wide.

“Oh my, traditional medicine? You know how to do that too?”

“I just learned a little.”

“That’s wonderful. Give it a try.”

Hayeon, on the other hand, looked less than enthusiastic.

“Why traditional medicine? I’m not really into that kind of thing.”

“Then trust me and put up with it for a little while.”

“Mom, thank you for raising me all this time. Your useless daughter is leaving without even getting the chance to repay you.”

“…….”

*What the hell, you little shit?*

I almost lost control of my internal energy. I could run around for an hour without sweating a drop, but I was starting to feel a little hot now.

“I’m joking. It’s not like you’d do anything bad to your only little sister, right?”

“Then shut up and stay as still as possible, even if it hurts.”

“Okay.”

I took a deep breath. From this moment on, I was going to clean out Hayeon’s acupoints.

The cleaner was me.

The broom was fifteen years of internal energy.

“Ready?”

“Yes, yes, Teacher. But when exactly are we starting?”

“Right now.”

As soon as I answered, I sent my internal energy flowing.

*Whooosh.*

A wave of gentle yet powerful internal energy began sweeping through the minor meridians throughout Hayeon’s body, washing away the waste that had built up inside her…

* * *

“Hoo.”

“Phew.”

The two breaths that escaped us simultaneously after I let go of her hand carried completely different meanings.

Mine expressed relief.

Hayeon’s expressed refreshment.

*Ding.*

> **System**
>
> - **Circulate Qi for Healing** has been completed successfully.
> - **Internal Energy** increases slightly.

As the System had announced, Circulate Qi for Healing had ended successfully.

The Jin Family’s Cultivation Technique was an internal energy cultivation technique that accumulated internal energy slowly but possessed exceptional stability. Hayeon had accumulated so much waste that the process took some time, but it ended without any major problems.

“Oppa, what was that?”

The fact that she naturally called me Oppa showed that she had been surprised too. I wiped away the sweat that had formed from the tension and answered.

“I told you. It’s a stable traditional medicine treatment.”

“That worked when you were only holding my hand?”

*Do you think it would? It’s all thanks to your brother’s excellence.*

I smoothly changed the subject.

“So? How was it?”

“It hurt at first, but as time passed, it started feeling better and better. My body feels lighter, and my headache is gone. What should I call it…”

Hayeon furrowed her brow before defining it in a single phrase.

“Like I was reborn? Like all the bad energy inside me was washed away. Ah, damn it, I don’t know.”

*That sounds pretty accurate to me.*

In any case, seeing how much better her complexion looked made all the effort worthwhile. I let out a short laugh and said,

“Yeah, then go wash up.”

“Huh?”

“What do you mean, ‘huh’? Is your nose stuffed up? You stink, so go take a shower. Now.”

“I washed this morning. What do you mean I smell—Aagh!”

Hayeon realized that a terrible stench was radiating from her own body, grabbed her nose, and began making a huge fuss.

*It’s only natural.*

Where else would the waste inside her body go? It had to come out somehow. Through sweat, for example, or maybe…

*Grrrbl. Pffft.*

Well, it could come out that way too.

“…….”

But maybe it was because there had been so much waste. The smell was unbelievable.

At this point, I had to wonder if she had actually crapped herself.

“Aah.”

On top of the sweat soaking her body, her stomach had begun sending strange signals. Hayeon almost crawled to the bathroom, while Mom stood there with her mouth hanging open.

“My goodness.”

“It works well, doesn’t it?”

“It really does. I went to a traditional medicine clinic a few times when I was young, but this is amazing.”

“I learned properly. If you ever want to go to a traditional medicine clinic, just come to me. You can do it right now, if you want.”

“Should I? As it happens, I’ve been having some trouble digesting lately…”

Mom smiled brightly and held out her hand.

That was when—

*Bwaaaang. Frrt. Frrt.*

“…….”

“…….”

Mom quietly withdrew her hand.

“……Should we start when Hayeon comes out?”

“……Yes.”

There was only one bathroom in our house.

* * *

*Whooosh.*

Some time after the sound of the toilet flushing, Mom emerged with the most refreshed expression in the world.

“How do you feel?”

“I feel ten years younger.”

That wasn’t an exaggeration.

Even Hayeon, who was only nineteen, had needed more than an hour to expel all the waste from her body.

Mom was middle-aged, so the amount of waste she had accumulated was proportional to the years she had lived. After more than two hours of circulating qi for healing, her condition must have improved to a degree that couldn’t even be compared to before.

“Right? Until just a little while ago, I had a headache and felt dizzy, but now I’m completely better. I took my temperature as soon as I came out of the bathroom, and it was normal.”

Hayeon looked at me as if I were some kind of marvel. The moment she came out of the bathroom, she ate two bowls of rice as if she had never once complained about having no appetite.

“Where did you learn something like this? Were you a healer, Oppa?”

“A healer? No. I just happened to learn it.”

“Which traditional medicine clinic did you learn it at? If it’s nearby, I’ll go there too.”

“……You’d be in big trouble if you went there.”

“Why?”

“You don’t need to know. Just know that there are lots of scary men there.”

“Do they stick the needles in painfully?”

“……They do tend to.”

*If she knew those ‘needles’ were actually knife stabs, what kind of expression would she make?*

I pushed Hayeon away as she kept peppering me with questions and slipped a hand into my pocket.

*Open Inventory.*

A translucent inventory window appeared along with the familiar System notification.

If I had been in the Murim, it would have been packed with the spoils I had obtained after defeating Jopil and various weapons.

But this was reality.

*It would be nice if the inventories were integrated.*

The fact that they were separate seemed more unfortunate the more I thought about it.

Taking just a few high-grade potions to the Murim would be no different from bringing along a few extra lives.

*Well, I should be satisfied that I can recover to some degree by leveling up.*

I clicked my tongue inwardly and pulled my hand from my pocket. Two small bottles filled with red liquid were sloshing in my palm.

### Item Window

**Lesser Potion**

- **Type:** Medicine
- **Grade:** Third Rate
- **Description:** A liquid infused with weak healing magic. It is readily available on the market.
- **Effect:** Restores the body when consumed. The effect is minimal.

They had been issued as raid supplies yesterday. Since I had no particular use for them, I had put them in my Inventory and left them untouched.

*I’m technically supposed to return them.*

Even lesser potions cost more than 200,000 won apiece. It was difficult to find an employer as generous as Team Leader Choi, who handed them out so freely.

“Take one each.”

“Huh? It’s a potion.”

“Why go as far as using a potion? I’m perfectly fine now.”

“I’m worried there might be side effects. If you don’t drink it now, it’ll cost you more later.”

In truth, I was only recommending them to restore their vitality. Circulating qi for healing had no side effects.

“Drink up. You too, Hayeon.”

Mom hesitated, then took hers first. Hayeon cautiously took her cue from Mom and followed suit.

*Gulp. Gulp.*

“How is it?”

Hayeon finished hers in one go and tilted her head.

“I feel a little stronger, maybe. Or maybe not. How would I know? It’s not like I’ve had a potion before.”

“I guess I don’t really know either.”

“You’ll definitely notice the effect when you’re tired or sick. I’ll buy a box and keep it here, so drink one whenever that happens.”

“A box? How many come in a box?”

“Fifty, if you buy the large one?”

“At about 200,000 won each, fifty would be… ten million won? Oppa, are you crazy?”

Hayeon smacked my forearm.

“Just because you made some money this time, are you really going to spend it so recklessly? If you keep overspending like that, that 300 million won will disappear in no time.”

“It’s fine. I’ve been earning well lately.”

“I searched online, and I heard that when you become a C-rank Hunter, you have to replace your equipment and all that. They said you can burn through hundreds of millions like it’s nothing.”

“I told you, it’s fine. I made four billion won yesterday, too.”

“Even if you had four billion won, you shouldn’t throw money around like—wait, how much did you say?”

“Four billion won.”

“…….”

Hayeon’s body went completely rigid.

She stared blankly at me, then turned toward Mom.

“Mom, Oppa says he made four billion won.”

Mom gave an awkward smile and nodded.

Only then did Hayeon ask in a trembling voice,

“Is that true?”

“Yeah.”

“Four billion won?”

“I’m telling you, it is.”

Determination filled Hayeon’s eyes.

“Oppa. Can I drop out of school?”

“…….”

*Didn’t you say there was no end to learning?*
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 89`.

# Master Edit Task — Chapter 53

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
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 경험치              | **EXP**                        |
| 동기화              | **Synchronization** / **Sync** |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 본가      | **our family / this family**                                    |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |

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

#### Chapter 51 tail (verified mastered)

…
out of my throat. That was my secret—something I couldn’t tell anyone. “No particular reason. You have to row when the tide comes in.” “If you keep working like that, you’ll snap the oars. Think about the people in the boat with you.” “The people in the boat with me? You, Team Leader?” “Well, for example…” Team Leader Choi paused, then went on. “Your family, perhaps.” Family. It was only one word, but warmth seeped into every corner of my body. We talked on the phone now and then, but I hadn’t seen them in more than two months. Counting the time I’d spent in Murim, it had been three. *Has it already been that long?* Ever since my father died, my life had been like a car running uphill. So I’d had no choice but to keep my foot on the gas. Take it off, and it felt like I’d roll backward. Like the engine might die at any second. “Anyway, weekends are off. Don’t even think about going to the day-labor agency. Rest. Going there would be a contract violation.” “Ah. Okay.” *Forcing me to rest this hard… Maybe this guy Choi isn’t such a bad person after all…* No. I couldn’t let myself get taken in by a little emotional appeal. Not after all the hell I’d gone through on my own. *Team Leader Choi is an exploitative employer. An exploitative employer.* It was obvious he only wanted me resting on the weekend so he could work me to the bone starting next week. The mindset of a slave plantation owner who didn’t want stamina wasted in the wrong places. What a vicious man. “Preparations are complete, young master.” Butler Kim was back from loading the Equipment. *That man’s suffering under an exploitative employer too. It’s almost ten at night, and he still hasn’t gotten off work.* “Ah. What about the thing I mentioned?” “I brought it.” “Give it to him.” At the exploitative employer’s word, Butler Kim held out the small box in his hands. “Please take this, Hunter.” To me. “Huh? Me?” It looked like a box of tonic drinks. I just blinked at it, then a thought flashed through my head and I asked carefully, “Don’t tell me this is money?” “We contracted for weekly pay. Did you forget?” I had. I’d naturally assumed I’d get it on Sunday. I took the box with a dazed look. It was heavy. “Is it usually paid in cash?” “Of course not.” “Then…” “You said you liked cash, Mr. Jin Taekyung. Especially crisp new bills.” I’d mentioned it in passing yesterday—or maybe the day before. I hadn’t expected it to come back like this. My opinion of the exploitative employer rose a little. *Of course, the most important part is still left.* Four days of pay, Tuesday through Friday. My first weekly paycheck as a C-rank Hunter. Of course I couldn’t help looking forward to the amount. I swallowed and opened my mouth. “Then how much is all of this…?” “We put in a little more than the contract says. The settlement details are inside, so check them. We’ll be going.” “Until next time, Hunter.” Team Leader Choi and Butler Kim took off in a flash. It really did happen in an instant. I stared after the receding car lights, bewildered, then opened the drink box. In the faint moonlight, thick bundles of bills caught my eye. *One, two, three…* The count stopped at six. Six bundles of a hundred bills. In other words, six million won. “What is this?” *Scam.* The word flashed through my mind just as my legs were about to give out— “Huh?” Had I seen it wrong? Why were the bills yellowish? “Wait. Wait a second!” I focused internal energy into my eyes, and my vision brightened. Then I saw her. A kindly smiling woman in a hanbok, right there on the bill. “Shin Saimdang! Wise mother and virtuous wife! Her son is Yulgok Yi I! Her husband is Yi Wonsu!” I started speaking in tongues before I even realized it. This was insane. Completely insane. One bundle contained a hundred Shin Saimdang bills. Six of those meant… “Th-three hundred million!” This time I couldn’t catch myself as my legs gave out. I dropped to my knees hard enough to make a thud and stared blankly into the drink box. A white sheet of paper lay beneath the bundles, lining the bottom. *Right. The settlement sheet!* I unfolded the paper in a panic. It contained a complete record of the past four days’ earnings. Right down to the final amount being paid to me. *The settlement says thirty million won?* What? Had I imagined it? I was confused. Completely confused. My shaking gaze froze on the last line. **Bonus: 270,000,000** And then Team Leader Choi’s last words as he left. *We put in a little more than the contract says.* Thunder and lightning tore through my head. I rose on trembling legs. Far off, the car’s lights were already fading. They looked like a single ray of light. “Ahh. Aaaah…” Team Leader Choi. No—he was the Light. [^1]: Korean slang for Friday night, from “burning Friday.” [^2]: In Korean, the same word, *jipsa*, can mean either butler or church deacon. [^3]: Tteokbokki is a Korean dish of chewy rice cakes in a spicy sauce. Korean churches often sell it as a snack.

#### Chapter 52 tail (verified mastered)

…
what do we do!” The broth had boiled down to almost nothing, and the fish had turned into lumps of charcoal. I’d been looking forward to a home-cooked meal after so long, but… Well, this wasn’t such a bad turn of events either. “Let’s go out to eat. It’s been a while.” On any other day, Mom would’ve launched into a lengthy speech about the absurd price of restaurant food, while Hayeon would’ve asked us to order fried chicken. This time, both of them stayed quiet. “Little sister.” “Yes, dear brother.” “Grab the money.” “Yessir.” Hayeon swept up the bundles like she’d been waiting for the order. * * * “I’m sorry, but our restaurant has a dress code…….” The manager of the upscale restaurant—where a course meal cost several hundred thousand won per person—gave us an awkward smile. “A dress code?” “Yes. As you can see, the other guests are the same.” He was right. Men and women alike, all in suits and dresses. Some were even in evening gowns. *Shit. Anyone watching would think they’d come here to dance at a ball.* What was this, eighteenth-century France? For someone like me, who’d only ever gone to gukbap[^1] places, it was a massive culture shock. “Let’s just go somewhere else.” “Yeah. Hayeon knows a lot of good restaurants around here.” The family looked even more embarrassed than I did, so I just walked out. The three of us were reflected in the restaurant glass. We’d clearly dressed up for our first meal out in a long time, but every piece we owned was cheap market-brand stuff that already looked well-worn. *Had they been that short on money?* I’d sent most of what I earned home, scrimping on my own food and clothes to do it. Even as an F-rank Hunter, I’d worked twice as hard as everyone else. It shouldn’t have been a small amount. “Son, should we go get pork belly? Maybe greasy food is a bit much this early in the morning.” “Pork belly sounds good. Mom knows what’s what. A friend went to the barbecue place at the intersection up ahead and said it was amazing.” Just pork belly. I had a C-rank Hunter license in my wallet and a bag stuffed with cash. It wasn’t like they didn’t know that. They could splurge without worrying. *That’s why I work.* Someone once said you can’t buy happiness with money. That happiness doesn’t have a price tag. Personally, I had one thing to say to people who talked like that. *Fuck off.* Money’s what you can’t spend because you don’t have it. And after thinking all night about how to use this money, I’d finally made up my mind. At least for today, I would spare no expense on my family. Now that decision swelled even bigger. “Let’s eat a little later.” Without waiting for an answer, I flagged down a passing taxi. “Where can I take you?” “Mirae Department Store.” It was supposed to be the biggest and most expensive department store in the area. In the rearview mirror, Mom’s eyes went round. “The department store?” Meanwhile, the corners of Hayeon’s mouth curled up slyly. “Nice. My rich oppa can buy me clothes too.” Sharp as ever. I only had to say the word and she got it. I snorted. “Buy whatever you want.” “Really?” “Pick out Mom’s things first.” “Okay.” “You’ve got yourself a devoted son, ma’am. Ha ha.” Only then did Mom smile at the driver’s banter. * * * “You’re really buying everything?” “Everything.” Once I confirmed it for the last time, Hayeon tore through the department store like a colt off its reins. She had a viciously sharp eye for clothes, and she moved so fast I started to wonder if she was an Awakened. At first, Mom looked at the price tags more than the clothes. Before long, even she started shopping in earnest. “Mom, what do you think of this?” “Isn’t it too short?” “This one!” “That’s nice.” “This too!” “That’s pretty. Excuse me, miss—do you have this in one size larger?” Two hours passed, and I felt a change in my body. *I’m dying.* Crushing shortness of breath and agonizing pain in my legs, for no reason I could name. Helplessness wrapped around my whole body at about the same level as when I’d faced Jopil in Murim. “Oppa, how do I look?” “Ugly. Get lost.” “Son, try this on.” “I don’t think I need to try it. I’ll take that.” I don’t know how many clothes we bought that day, or how much we spent. All I know is, by the time we finished shopping and headed out, someone high up at the department store had come to see us off. “Welcome.” The manager of the restaurant that had been so strict about its dress code didn’t even recognize us. “Wow, I’ve never eaten anything like this before.” “I know. How do they make the food look this pretty?” Mom and Hayeon whispered to each other, their cheeks flushed. We'd spent dozens of times the price of the several-hundred-thousand-won course meal just to eat it, but it was a day when not a single won felt wasted. “But I want rice. This is too rich.” “Why are the portions so small?” ……I pretended it wasn’t a waste. [^1]: A cheap Korean rice-and-soup meal, typically eaten at modest diners.

## Korean source

```text
＃53화



띠링.



- 수면 모드가 종료되었습니다.



“……빠, 오빠!”

헉, 헛숨과 함께 눈을 떴다.

제일 먼저 눈에 들어온 건 고시원 천장이 아니라 하연이의 얼굴이었다.

아, 맞다. 어제 집에 왔었지.

“악몽이라도 꿨어?”

“응?”

“아까부터 소리 지르던데. 땀도 엄청 흘리고.”

내가?

되묻기도 전에 깨달았다. 전신이 땀에 흠뻑 젖어 있었고 모래라도 삼킨 것처럼 목이 따끔거렸다.

‘몸 상태가 왜 이래?’

내가 가진 시스템은 깨어 있을 때만 적용되는 것이 아니다. 수면 모드는 숙면을 취하게 해 줌과 동시에 컨디션 최고로 끌어 올리는 효과가 있었다.

지금 같은 상황은 무림에서도, 동기화가 된 이후에도 없었던 일이다. 게다가 악몽이라니.

‘무슨 꿈을 꾼 거지?’

하지만 머리만 지끈거릴 뿐, 꿈 내용은 기억나지 않았다.

그런 내게 하연이가 걱정스러운 목소리로 물었다.

“요즘 안 좋은 일이라도 있어?”

“없어, 그런 거.”

“있으면 말해. 혼자 끙끙 앓지 말고.”

“네, 누나.”

“장난 아니거든.”

조그만 주먹이 가슴을 퍽 친다. 하연이의 진지한 표정에 할 말이 없어진 나는 턱만 긁적였다.

“진짜 없어? 고민이나, 힘든 일.”

“없다니까.”

거짓말이다. 7년 전에도 있었고 7년 후에도 있을 것이다. 혼자 방에 틀어박혀 운 날도, 진호 형과 진탕 술을 퍼마시며 잊은 날도 있었다.

‘그걸로 충분해.’

어린 두 남매 키우느라 무릎 연골이 닳도록 일한 어머니, 이제 수능을 준비 중인 고3 여동생에게는 말할 수 없는 일들이 있다.

혼자 버티고 극복하는 것. 이제는 익숙해졌다.

나는 아무렇지 않은 척 씩 웃어 보였다.

“이제 인생 펼 일만 남았는데 무슨 고민이 있겠냐? 아, 하나 있긴 하네. 앞으로 돈 어떻게 써야 하나, 뭐 그런 거?”

“허세는.”

분위기가 살짝 가벼워졌다. 나는 짐짓 얼굴을 구겼다.

“허세? 어제 기억 안 나냐? 돈다발 다시 보여 줘?”

“그건 인정. 재수는 없는데 할 말이 없네.”

“지금 내 27년 인생 그래프 꼭대기 찍었다. 별일 없으니까 너는 공부나 열심히 해.”

“내 성적 전국 0.1%거든? 충분히 잘하고 있으니까 걱정 마셔.”

입을 삐죽 내민 하연이가 방을 나가려다 말고 멈칫, 다시 돌아선다.

“오빠, 그런데.”

“응?”

“진위경이 누구야?”

“……뭐?”

생각지도 못한 타이밍에 등장한 한 사람의 이름.

몸이 뻣뻣하게 굳었다.



* * *



아삭.

갓 담근 총각김치를 한 입 베어 물었다. 그토록 먹고 싶었던 엄마 음식이었지만 맛이 거의 느껴지지 않았다.

방금 전, 하연이와 나눴던 대화 때문이다.



‘너, 그 이름 어디서 들었어?’

‘오빠한테. 아까 자면서 계속 그 이름을 부르더라고.’



그리고 마지막 한마디.



‘아는 사람이야? 꿈에도 나올 정도면 친한가 보네.’



그 질문에는 대답하지 못했다. 무림에서도, 현실에서도 그 답을 찾지 못했기 때문이다. 아니, 더 이상 찾을 이유도 없었다. 나는 현실로 돌아왔고, 진위경은 무림에 있으니까.

‘그런데 왜 갑자기 진위경이 꿈에…….’

머리가 복잡했다. 무림에서의 후유증 때문일까? PTSD. 외상 후 스트레스성 장애라는 단어도 떠올랐다.

‘미치겠네.’

나도 모르게 표정이 굳은 모양이다. 엄마가 넌지시 물었다.

“입맛이 없니? 너 좋아하는 걸로 차렸는데.”

“아, 아니에요. 김치는 언제 담그셨어요? 된장찌개도 아주 제대로네.”

황급히 변명하며 수저를 들었다. 오랜만에 세 식구가 한 식탁에 모였다. 이 소중한 순간을 망칠 수는 없다.

‘별일 아니겠지. 별일 아닐 거야.’

후루룩.

그럼에도 불구하고 구수한 된장찌개에서는 약간의 쓴맛이 느껴졌다.



* * *



찜찜했던 마음 한구석은 금방 평소대로 돌아왔다.

가족들과 하루 종일 웃고, 떠들고. 낮잠까지 푹 자고 나니 저녁이었다. 이제는 돌아가야 할 때다.

“며칠 더 있다 가지. 내일 수육 하려고 했는데.”

“우리 김 여사님 또 시작이네. 나도 수육 먹을 줄 알거든?”

미련이 뚝뚝 떨어지는 엄마의 말에 하연이가 구시렁거렸다.

“반찬도 잔뜩 챙겨 보내는데 뭐가 그렇게 걱정이야? 저 정도면 반찬 가게를 열어도 되겠구만.”

“……그건 그래.”

현관문 앞, 엄마가 준비해 둔 쇼핑백들 안에는 반찬이 한가득했다. 이것도 겨우 설득한 끝에 얻어 낸 협의점이다.

‘넣을 곳도 없는데.’

3평짜리 고시원 방에 냉장고까지 들여놓으면 정말 발 디딜 곳이 없을 것이다. 아니, 들여놓을 자리도 없다.

이미 냉장고만 한 캡슐이 있으니까.

‘슬슬 이사라도 가야 하나.’

그런 생각을 하며 어젯밤 미리 싸 놨던 배낭을 어깨에 멘 순간이었다.

“……?”

뭐가 이렇게 묵직해? 넣은 거라곤 기껏해야 어제 샀던 옷 몇 벌이 전부인데.

의아함에 배낭을 내려놓자 다급해진 건 가족들이었다.

“아들, 내일부터 바쁘지? 빨리 가서 씻고 푹 자.”

“……아까는 며칠 더 있다가 가라면서요?”

“오빠, 차 시간 늦겠다.”

“택시 타고 갈 건데?”

“야간 할증. 야간 할증 붙잖아.”

이쯤에서 대충 감을 잡았다.

“언제 넣었어?”

“뭐, 뭘?”

“돈.”

표정이 곧 대답이다. 나는 한숨을 내쉬었다.

“말했잖아요. 두고 필요할 때 쓰시라니까.”

“…….”

“저 돈 많이 벌어요. 앞으로도 그럴 거고요.”

사실과 거짓을 반반 섞었다.

C급 헌터 평균 연봉이 5억이다. 최 팀장이라는 후한 고용주를 만나 상상치도 못한 거액을 보너스로 받았지만, 시스템이 사라진다면 모든 게 물거품으로 사라질 거다.

그래서 더 가족에게 주고 싶었던 건데…….

“네가 목숨 걸고 벌어 온 돈이잖아. 너 위해서 써. 응?

“엄마.”

“아들.”

다음 순간, 조용히 흘러나온 엄마의 한마디에 나는 말문이 턱 막혔다.

“무리하지 마. 다치지도 말고. 엄마는 그거면 돼.”

더 이상 무슨 말을 해야 할까.

잠시 후, 나는 여름밤의 습한 공기 속으로 발을 내딛었다.

반찬이 든 쇼핑백과 돈다발이 가득한 배낭을 메고서.

부우웅.

택시를 타고 고시원으로 돌아가는 길 내내 엄마의 마지막 말과 그 온기를 떠올렸다.



‘살아남아라, 뒤도 돌아보지 말고 도망치란 말이다. 그게 네 임무다.’



점점 흐릿해지는 기억 속 누군가의 목소리도.



* * *



촤아악-

핏물이 솟구쳤다. 몬스터의 녹색 피가 아닌, 인간의 붉은 피다. 타는 듯한 허벅지의 통증을 느끼며 리자드맨 족장의 가슴에 창을 쑤셔 박았다.

“키이…….”

띠링.



- [Lv.50 리자드맨 족장]을 처치했습니다!

- 경험치를 획득했습니다!



게이트 클리어. 숨이 끊긴 리자드맨 족장의 시체 위에 밖으로 통하는 마력장이 생성됐다.

최 팀장이 나무에서 등을 뗀 것도 그때였다.

“세 번.”

“예?”

“진태경 씨가 오늘 다친 횟수입니다.”

단단하고 길쭉한 손가락이 내 몸 곳곳을 가리켰다.

이미 포션으로 치료된 목덜미와 팔, 그리고 아직도 피가 흘러나오고 있는 허벅지.

“괜찮아요. 스친 정도라 하급 포션으로도 충분히…….”

“안 괜찮습니다.”

단호한 어조로 말을 잘라 낸다. 평소에도 속을 알 수 없는 표정의 최 팀장이지만 이번만큼은 뭔가 달랐다.

확실한 건 저 표정에서 묻어 나오는 감정이 단순한 걱정이 아니라는 거다.

“지난주에는 한 번도 부상을 입지 않았습니다. 같은 게이트, 같은 몬스터를 상대하는데 이렇다면 이유는 하나죠.”

그의 투명한 눈이 나를 향했다.

“진태경 씨. 무슨 문제라도 있습니까?”



* * *



하루, 이틀, 사흘.

시간이 지났지만 상황은 나아지지 않았다. 결국 나흘째 되는 날엔 다섯 군데에 부상을 입고 말았다.



‘지금 상태로는 안 됩니다. 퇴근하세요.’



최 팀장의 말을 뒤로하고 고시원으로 향하는 길, 머릿속이 복잡했다.

‘뭐가 문제지?’

모든 게 잘 풀리고 있었다. 시스템은 사라지지 않았고, 내 계좌에는 은행에 맡긴 3억 상당의 돈이 예치되어 있다. 이제는 C급 헌터로서 승승장구할 일만 남았는데…….

‘빌어먹을 꿈.’

그때부터였다. 본가에서 보낸 첫날 밤 이후부터 나는 악몽을 꾸기 시작했다.

악몽 속 장면은 점점 또렷해졌고 꿈이 끝나면 땀에 흠뻑 젖어 깨어났다. 운기조식으로 몸 상태를 끌어 올려 놔도 정신이 불안정하니 실수만 늘었다.

‘이대로라면 곤란한데.’

몸은 현실에 있지만 정신은 아직도 무림에 붙잡혀 있는 상황. 정신과라도 가 봐야 하나 고민하며 고시원 방에 도착했다.

달칵.

“어, 왔어?”

인사가 너무 자연스러워서 잘못 들어왔나 헷갈릴 정도다.

나는 기가 막힌 얼굴로 물었다.

“뭐 하냐?”

진호 형이 대답했다.

“분해 및 조립.”

드라이버를 들고 캡슐 앞에 앉아 있는 모습에 순간 눈앞이 노래진다. 이 인간이 지금 설마…….

“미쳤어? 비켜!”

“야, 야. 한국말은 끝까지 들어야지.”

진호 형이 황급히 손을 내저었다.

“아직 시작도 안 했어.”

“뭐?”

“나도 막 들어왔다고. 진짜야.”

표정을 보니 거짓말하는 것 같지는 않다. 멀쩡한 캡슐을 확인하고 나서야 안도의 한숨이 흘러나왔다.

“후우.”

내 반응에 진호 형이 당황한 얼굴로 물었다.

“작동도 안 되는 고물 캡슐 하나에 왜 이렇게 난리야? 짐짝처럼 내다 버릴 때는 언제고.”

“그때는 그때고.”

동기화에 관한 일을 진호 형이 알 리 없다. 그에게는 고물 캡슐로 보이는 저 정체불명의 물건이 내게 어떤 의미를 갖는지도.

“아무튼 절대 건드리지 마. 알았어?”

“아주 때려죽일 기세네.”

“찢어 죽일 거야.”

“…….”

황당한 얼굴의 진호 형을 무시하고 침대에 풀썩 드러누웠다.

잠깐의 해프닝에 몸 안의 기운이 쭉 빠져나간 기분이다.

“무슨 일 있냐?”

“일은 무슨.”

“요즘 너 때문에 민원 장난 아냐. 오늘도 옆방 아저씨가 난리 치는 거 겨우 달래서 보냈다.”

뭐 때문인지는 짐작이 간다.

진호 형이 바닥에 늘어놓은 공구를 주섬주섬 챙기며 말을 이었다.

“밤새 끙끙거리니까 미칠 것 같대. 아, 그리고 진위경이 누구냐는데?”

또 나왔다. 저 이름.

나는 베개에 얼굴을 파묻었다.

“그냥 여자 친구라고 해.”

순간, 멍키 스패너를 쥔 그의 손이 부르르 떨리는 게 보였다.

“여자 친구 생겼냐? 이런 배신자 새끼.”

“…….”

“예뻐? 몇 살? 사진 보여 주라.”

저 인간이 서른이라니. 통탄을 금치 못하겠다.

“근데 이름이 좀 이국적이네. 조선족이셔? 아니면 중국인?”

“……중국인.”

틀린 말은 아니지, 뭐.

“이 새끼 C급 헌터 됐다고 벌써 글로벌하게 노네. 아무튼 여자 소개 좀. 나 중국 좋아해. 니하오마. 워아이니. 또 뭐 있더라.”

“니씨팔롬아.”

“병신. 성조랑 발음 다 틀렸다. 그래서 100일이나 채우겠냐? 따라 해 봐. 니 취팔러마.”

“니씨팔롬아.”

“다시. 니 취팔러마.”

“니씨팔롬아.”

“……아니 이 새끼가?”

새삼스러운 깨달음에 분노하는 진호 형을 무시하고, 나는 문을 가리켰다.

“나가.”

제발 혼자만의 시간 좀 갖자.



* * *



조용해진 방, 침대에서 몸을 일으킨 나는 캡슐로 다가가 낡고 때에 찌든 캡슐 표면을 톡톡 두드리며 중얼거렸다.

“너, 뭐 하는 놈이야?”

당연하게도 대답은 돌아오지 않았다.

내심 기대했는데, 아쉽다.

‘시스템도 현실에 동기화된 마당인데 기계가 말할 수도 있지 뭘.’

사실 진짜 기계인지도 의문이다. 아무리 현실이 판타지가 된 지 오래라지만 이건 새로운 장르 아닌가.

만약 지금 내 상황을 소설로 쓴다면 장르를 어떻게 정해야 할까. 판타지? 게임 소설? 그것도 아니면.

‘차원 이동?’

푸흐흐. 바람 빠지는 소리가 흘러나왔다. 차원 이동이라니, 내가 점점 미쳐 가는구나. 그런 게 가능할 리가 없다.

가능할 리가…….

얼음물을 뒤집어쓴 것처럼 정신이 번쩍 들었다.

‘……가능하잖아.’

차원 이동은 과거에도 있었고, 현재에도 남아 있다.

마왕 아스모데우스의 침공, 그리고 게이트가 그 증거다.

우리는 게이트를 통해 현실을 오고 갈 뿐이지만, 수십 년 전 몬스터 군단은 거길 통해 또 다른 차원에서 지구로 넘어왔다.

‘마계(魔界).’

악의 땅. 몬스터들의 고향. 마왕의 영지.

인간 중 그 누구도 발을 디디지 못한, 엿볼 수도 없는 미지의 차원. 인류는 그렇게 정의 내렸다.

그런데 만약 눈앞의 이 캡슐이 또 다른 차원으로 향하는 일종의 게이트라면, 무림이 알려지지 않은 또 다른 차원이라면…….

‘무림은 또 하나의 현실이다.’

그곳에서 보고 겪은 모든 것들이.

물, 흙, 바람. 그리고 사람까지도.

‘NPC가 아니었어.’

나는 빛바랜 캡슐 표면 위에 비친 얼빠진 내 얼굴을 바라봤다.

그 후로도 한참 동안.
```

## Current accepted English baseline

```markdown
# Chapter 53

Ding.

> **System**
>
> - Sleep Mode has ended.

“…O-oppa!”

I gasped and opened my eyes.

The first thing I saw wasn’t the ceiling of my goshiwon[^1] but Hayeon’s face.

*Oh, right. I came home yesterday.*

“Did you have a nightmare?”

“Huh?”

“You’d been screaming. And you were sweating like crazy.”

*I was?*

Before I could even ask, I understood. My whole body was soaked in sweat, and my throat stung as if I’d swallowed sand.

*Why do I feel like this?*

The System I had didn’t only work while I was awake. Sleep Mode let me sleep deeply and pulled my condition up to its peak at the same time.

Nothing like this had happened in Murim, or after Synchronization. And a nightmare, on top of that?

*What did I even dream?*

My head just throbbed. I couldn’t remember the dream at all.

Hayeon asked, worried,

“Has something bad happened lately?”

“No. Nothing like that.”

“If there is, tell me. Don’t suffer by yourself.”

“Yes, nuna.”

“I’m not joking.”

Her little fist thumped my chest. Hayeon’s serious face left me with nothing to say. I scratched my chin.

“Really? No worries? Nothing hard going on?”

“I told you, there’s nothing.”

It was a lie. There had been things seven years ago, and there would be things seven years from now. There’d been days I locked myself in my room and cried, and days I drank myself senseless with Jinho hyung just to forget.

*That’s enough.*

There were things I couldn’t tell my mother, who’d worked until the cartilage in her knees wore down raising two young kids, or my little sister, a high-school senior now preparing for her college entrance exam.

Enduring and getting through things alone. I was used to it by now.

I flashed a grin, like nothing was wrong.

“My life’s finally about to take off. What would I have to worry about? Ah, there is one thing. How I’m supposed to spend all this money. Something like that.”

“Show-off.”

The mood lightened a little. I made a face on purpose.

“Show-off? Don’t you remember yesterday? Want me to show you the bundles of cash again?”

“I’ll give you that. You’re obnoxious, but I can’t argue.”

“I’ve hit the peak of my twenty-seven-year life graph. Nothing’s going on, so you just study hard.”

“My grades are in the top 0.1 percent nationwide, okay? I’m doing more than well enough, so don’t worry.”

Hayeon pouted and started to leave, then stopped and turned back.

“Oppa. But…”

“Yeah?”

“Who’s Jin Wikyung?”

“…What?”

A name I never expected, at a moment like that.

My body went rigid.

* * *

Crunch.

I bit into a piece of freshly made young-radish kimchi. It was Mom’s cooking, the food I’d wanted so badly, but I could barely taste it.

Because of the conversation I’d just had with Hayeon.

“Where did you hear that name?”

“From you. You kept calling it in your sleep.”

And then her last question.

“Someone you know? If they show up in your dreams, you must be close.”

I couldn’t answer. I hadn’t found that answer in Murim or in reality.

No. I no longer had any reason to look for it. I had come back to reality, and Jin Wikyung was in Murim.

*Then why did Jin Wikyung suddenly show up in my dream…?*

My head was a mess. An aftereffect of Murim? The word PTSD surfaced—post-traumatic stress disorder.

*This is driving me crazy.*

I must have looked grim without realizing it. Mom asked carefully,

“Have you lost your appetite? I made all your favorites.”

“Oh, no. When did you make the kimchi? And this doenjang-jjigae is perfect.”

I scrambled for an excuse and picked up my spoon. For the first time in ages, the three of us were together at one table. I couldn’t ruin this.

*It’s nothing. It has to be nothing.*

Slurp.

Even so, the savory doenjang-jjigae tasted faintly bitter.

* * *

That uneasy corner of my mind soon went back to normal.

I laughed and talked with my family all day. I even took a long nap, and then it was evening.

Time to go back.

“Stay a few more days. I was going to make boiled pork tomorrow.”

“Our Mrs. Kim is starting again. I know how to eat boiled pork too, you know?”

Hayeon grumbled at the reluctance dripping from Mom’s words.

“She packed you a ton of side dishes already, so why are you so worried? At this rate she could open a side-dish shop.”

“…That’s true.”

The shopping bags Mom had ready by the front door were packed with side dishes. This, too, was the compromise I’d only gotten after talking her down.

*There’s nowhere to put them.*

If I put a fridge in my three-pyeong goshiwon room, there really wouldn’t be anywhere to stand. No—there wasn’t even room to put a fridge.

I already had a capsule the size of one.

*Should I start looking at moving?*

I was thinking that as I slung the backpack I’d packed last night over my shoulder.

“…?”

Why was it so heavy? All I’d put in were a few outfits I’d bought yesterday.

When I set the backpack down, my family was the ones who suddenly got frantic.

“Son, you’ll be busy starting tomorrow, right? Hurry back, wash up, and get a good night’s sleep.”

“…A minute ago you told me to stay a few more days.”

“Oppa, you’re going to miss your bus.”

“I’m taking a taxi, though?”

“Night surcharge. There’s a night surcharge.”

At that point, I had a pretty good idea.

“When did you put it in?”

“P-put what in?”

“The money.”

Their faces answered for them. I sighed.

“I told you to keep it and use it when you needed it.”

“….”

“I make plenty of money. And I will from now on, too.”

I mixed fact and fiction fifty-fifty.

The average annual salary of a C-rank Hunter was five hundred million won. I’d met a generous employer in Team Leader Choi and gotten a bonus I never imagined, but if the System disappeared, all of it would go up in smoke.

That was why I’d wanted to give even more to my family, but…

“That’s money you risked your life to earn. Spend it on yourself. All right?”

“Mom.”

“Son.”

The next moment, the quiet words that came from Mom left me speechless.

“Don’t push yourself. Don’t get hurt, either. That’s enough for Mom.”

What else was I supposed to say?

A little later, I stepped out into the humid air of a summer night.

With shopping bags full of side dishes and a backpack stuffed with bundles of cash.

Vroom.

The whole taxi ride back to the goshiwon, I thought of Mom’s last words, and the warmth in them.

And of a voice in a memory that was growing fainter and fainter.

“Survive. I’m telling you to run without looking back. That’s your mission.”

* * *

Shaaah—

Blood spurted. Not the green blood of a monster, but red human blood. Feeling the burning pain in my thigh, I rammed my spear into the Lizardman Chieftain’s chest.

“Keee…”

Ding.

> **System**
>
> - You defeated **Lv. 50 Lizardman Chieftain**!
>
> - You gained EXP!

Gate cleared. A mana field leading outside formed over the Lizardman Chieftain’s lifeless body.

That was when Team Leader Choi pushed away from the tree.

“Three.”

“Pardon?”

“The number of times you’ve been injured today, Mr. Jin Taekyung.”

His long, sturdy fingers pointed to spot after spot on my body.

The nape of my neck and my arm, already treated with potions, and my thigh, still bleeding.

“I’m fine. It only grazed me. A low-grade potion is more than enough…”

“You’re not fine.”

He cut me off, his tone firm. Team Leader Choi’s expression was always unreadable, but this time was different.

One thing was certain. The emotion in that look wasn’t simple concern.

“You weren’t injured even once last week. Same Gate, same monsters. If this is happening, there’s only one reason.”

His clear eyes turned on me.

“Mr. Jin Taekyung. Is something wrong?”

* * *

One day. Two days. Three days.

Time passed, but things didn’t improve. In the end, on the fourth day, I took injuries in five places.

“Not in your current condition. Go home.”

Leaving Team Leader Choi’s words behind, I headed for the goshiwon, my head a mess.

*What’s the problem?*

Everything had been going well. The System hadn’t disappeared, and my account had some three hundred million won sitting in the bank. All that was left was to keep riding high as a C-rank Hunter, but…

*Damn dreams.*

That was when it started. After the first night at my family’s house, I began having nightmares.

The scenes in them grew clearer and clearer, and when a dream ended I woke up soaked in sweat. Even if I circulated my qi and pulled my condition up, my mind was unstable, so the mistakes only multiplied.

*This is going to be a problem.*

My body was in reality, but my mind was still trapped in Murim. I was wondering whether I should see a psychiatrist when I reached my goshiwon room.

Click.

“Oh, you’re back?”

The greeting was so natural I almost wondered if I’d walked into the wrong room.

I asked, incredulous,

“What are you doing?”

Jinho hyung answered,

“Disassembly and assembly.”

He was sitting in front of the capsule with a screwdriver. For a second my vision went yellow.

*This bastard isn’t actually—*

“Are you crazy? Move!”

“Hey, hey. You have to hear Korean all the way through.”

Jinho hyung hurriedly waved his hands.

“I haven’t even started yet.”

“What?”

“I just got here too. Seriously.”

He didn’t look like he was lying. Only after I checked that the capsule was still intact did a sigh of relief slip out.

“Phew.”

Jinho hyung looked thrown by my reaction.

“Why are you making such a fuss over one junk capsule that doesn’t even work? What happened to tossing it out like a piece of luggage?”

“That was then.”

There was no way Jinho hyung could know about Synchronization. Or what that unidentified thing—just a junk capsule to him—meant to me.

“Anyway, don’t touch it. Got it?”

“You look ready to beat me to death.”

“I’ll tear you apart.”

“….”

I ignored Jinho hyung’s baffled face and flopped onto the bed.

After that little episode, it felt like all the energy had drained out of me.

“Something going on?”

“Going on, my ass.”

“Complaints about you have been no joke lately. Today I barely calmed the guy next door down and sent him off.”

I could guess why.

Jinho hyung scooped up the tools he’d spread on the floor and went on.

“He says he’s going crazy because you keep groaning all night. Oh, and he asked who Jin Wikyung is.”

That name again.

I buried my face in the pillow.

“Just tell him she’s my girlfriend.”

I saw his hand quiver around the monkey wrench.

“You got a girlfriend? You traitorous bastard.”

“….”

“She pretty? How old? Show me a picture.”

This guy was thirty. I couldn’t help but despair.

“The name’s a bit exotic, though. Is she an ethnic Korean from China? Or Chinese?”

“…Chinese.”

Not exactly wrong.

“This bastard hits C-rank and he’s already gone global. Anyway, introduce me to a girl. I like China. Nǐ hǎo ma? Wǒ ài nǐ. What else was there?”

“You fucking bastard.”

“Idiot. You got the tones and the pronunciation all wrong. With that, you think you’ll last a hundred days? Repeat after me. Nǐ chī fàn le ma?”[^2]

“You fucking bastard.”

“Again. Nǐ chī fàn le ma?”

“You fucking bastard.”

“…What the hell is this bastard doing?”

I ignored Jinho hyung, who was getting angry at this sudden realization, and pointed at the door.

“Get out.”

*Please. Just let me have some time to myself.*

* * *

Once the room was quiet, I sat up on the bed and went over to the capsule. I tapped its old, grime-caked surface and muttered,

“What the hell are you?”

As expected, no answer came back.

I’d been hoping, privately. Shame.

*The System’s already synchronized with reality. Why couldn’t a machine talk too?*

Honestly, I wasn’t even sure it was a real machine. Reality had been fantasy for a long time now, but wasn’t this a whole new genre?

If I wrote my current situation as a novel, what genre would I even pick? Fantasy? A game novel? Or—

*Dimensional travel?*

Pffhh. A deflating sound slipped out. Dimensional travel? I really was losing it. There was no way something like that was possible.

There was no way it could be…

It was like ice water over my head. My mind snapped clear.

*…It is possible.*

Dimensional travel had happened in the past, and it still existed now.

The invasion of the Demon King Asmodeus, and the Gates, were the proof.

We only used Gates to come and go from reality, but decades ago a monster army had crossed through one from another dimension to Earth.

*The Demon World.*

A land of evil. The home of monsters. The Demon King’s domain.

An unknown dimension no human had ever set foot in, or even glimpsed. That was how humanity defined it.

But what if this capsule in front of me was a kind of Gate to another dimension? What if Murim was another unknown dimension?

*Murim is another reality.*

Everything I had seen and been through there.

Water. Earth. Wind. And people, too.

*They weren’t NPCs.*

I stared at my vacant face reflected on the capsule’s faded surface.

For a long while after that.

[^1]: A *goshiwon* is a tiny, inexpensive room-for-rent housing arrangement; three pyeong is roughly ten square meters.

[^2]: *Nǐ chī fàn le ma?* means “Have you eaten?” In Korean, its pronunciation resembles a profanity, which is why Taekyung keeps answering with “You fucking bastard.”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 53`.

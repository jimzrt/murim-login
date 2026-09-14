# Master Edit Task — Chapter 52

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
| 진하연    | **Jin Hayeon**    |
| 시스템              | **System**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |

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

#### Chapter 50 tail (verified mastered)

…
a potion?” “There’s a button on the bottom, right? Press it.” *Does it open when I press it?* I tilted my head and pressed the button. Click. The front of the cylinder sprang wide open. The problem was— Fwoooosh— Boom! Whatever had been inside shot up like a firework and burst in midair. The pink liquid that exploded there spread out over a wide area. “Huh?” *What is that?* As I stared blankly at the sight, Team Leader Choi’s voice dug into my ear. “It’s pheromones.” “Pheromones? Perfume?” “Something like that.” “…?” “It was collected from female Lizardmen.” The instant he finished speaking, I felt a tremor from somewhere. It was the ground. The ground was rumbling. Team Leader Choi kindly added, “The effect is extremely powerful.” *You bastard…* * * * “Team Leader Three.” That was the first thing the middle-aged man with half-gray hair had said in an hour. Kim Sangshik, who had been waiting endlessly while the Guild Master chain-smoked, answered. “Yes, Guild Master.” “You’re curious, aren’t you? Wondering what kind of shit this guy plans to pull this time, calling you in first thing in the morning?” “Ah, no, sir.” The Sopung Guild Master smiled good-naturedly. “That’s right.” “What?” “I called you to raise hell.” “…” “Do you know where I went today?” The Guild Master exhaled a plume of cigarette smoke. “The Guild Alliance breakfast meeting.” Small and midsize Guilds were corporations too. In each region, Guild Masters held meetings to form alliances and socialize. That was where he’d been today. “I was on an empty stomach, just about to take a bite, when that Sangdong Guild Master bastard told me something interesting. He said the C-rank who awakened recently had been one of our Guild people until a few days ago.” “…Guild Master, that…” The Guild Master raised a hand, cutting Kim Sangshik off. “I wondered what kind of bullshit that was. But rude as the Sangdong Guild Master is, he isn’t the type to make up a story. Not at an alliance meeting, either.” “I-I’ll look into it again myself!” “Team Leader Three? No. No need.” The Guild Master threw a crumpled bundle of papers across the room. “I already looked into it myself.” Kim Sangshik recognized the crumpled papers for what they were: someone’s personal file. And the name on it, too. “Jin Taekyung. Team Leader Three knows that name too, right?” *Fuck.* Kim Sangshik squeezed his eyes shut. The Guild Master tapped the ash from his cigarette. “I know how you feel, Team Leader Three. You’re a founding member of the Guild, after all. You’re allowed to fire one bottom-tier Hunter you don’t like. Stick your beloved son in the vacancy. Right?” “Yes, yes.” “But the F-rank loach you treated like dirt and kicked out turned into a dragon and came back, huh? I even made a point of telling you to recruit him, but if you told the truth I’d obviously raise hell. You’d get a reputation for having dog eyes that can’t even recognize someone. So you filed a false report, right?” Sizzle. The Guild Master crushed out his cigarette. As the embers scattered, the last of his patience went with them. “Team Leader Three. No, Sangshik. Have we been together about twenty years?” Kim Sangshik answered in an uneasy voice. “Twenty-one years, Guild Master.” “That’s not what I meant.” “…Yes, hyung.” “Good. That sounds nice. Keep calling me that from now on.” “What?” “You’ve helped me keep this Guild going for twenty-one years. You’ve done more than enough. I’ll talk to the Team Three kids separately, so as of today, you’re out.” “H-hyung!” “Shut your mouth, leave quietly, and I won’t block your path. Once you’re out, do whatever you want.” The Guild Master’s voice was packed with tightly suppressed fury. Kim Sangshik realized he had no choices left. *Leave? Leave the Guild?* This was the workplace he’d spent more than twenty years in. And now he was being told to leave over something like this. Thrown out without a second thought. *Fucking hell…* He clenched his teeth and walked out of the office. One last blow came after him. “Hey, HR Team Leader. Process two terminations today. Kim Sangshik and Kim Sangho.” For the next few days, Sopung Guild was in an uproar over the rare event of a father and son being fired at the same time. Along with that, the hottest topic in the Guild became the recent whereabouts of the bottom-tier Hunter who had left not long before. “They say he’s C-rank. A reawakening.” “Oh my, Mr. Taekyung? The Taekyung I know?” “That’s what I’m saying. He hit the lottery. Apparently Kim Sangshik went to recruit him without even knowing who he was and got shut down hard.” “He found every excuse he could to fire him, and now he’s reaped what he sowed. I heard Team Leader Kim’s been going around calling it wrongful dismissal and badmouthing the Guild Master.” “He still hasn’t come to his senses. Still, I’m jealous. When do I ever get to live a life like that?” “Honestly, Taekyung deserves it. He worked so hard, so luck found him.” “Deserves it, my ass. Then are the rest of us all just living it up? It’s luck. All luck.” Half envy, half jealousy, the conversations always ended with the same question. “Where is Mr. Taekyung now, and what’s he doing?”

#### Chapter 51 tail (verified mastered)

…
out of my throat. That was my secret—something I couldn’t tell anyone. “No particular reason. You have to row when the tide comes in.” “If you keep working like that, you’ll snap the oars. Think about the people in the boat with you.” “The people in the boat with me? You, Team Leader?” “Well, for example…” Team Leader Choi paused, then went on. “Your family, perhaps.” Family. It was only one word, but warmth seeped into every corner of my body. We talked on the phone now and then, but I hadn’t seen them in more than two months. Counting the time I’d spent in Murim, it had been three. *Has it already been that long?* Ever since my father died, my life had been like a car running uphill. So I’d had no choice but to keep my foot on the gas. Take it off, and it felt like I’d roll backward. Like the engine might die at any second. “Anyway, weekends are off. Don’t even think about going to the day-labor agency. Rest. Going there would be a contract violation.” “Ah. Okay.” *Forcing me to rest this hard… Maybe this guy Choi isn’t such a bad person after all…* No. I couldn’t let myself get taken in by a little emotional appeal. Not after all the hell I’d gone through on my own. *Team Leader Choi is an exploitative employer. An exploitative employer.* It was obvious he only wanted me resting on the weekend so he could work me to the bone starting next week. The mindset of a slave plantation owner who didn’t want stamina wasted in the wrong places. What a vicious man. “Preparations are complete, young master.” Butler Kim was back from loading the Equipment. *That man’s suffering under an exploitative employer too. It’s almost ten at night, and he still hasn’t gotten off work.* “Ah. What about the thing I mentioned?” “I brought it.” “Give it to him.” At the exploitative employer’s word, Butler Kim held out the small box in his hands. “Please take this, Hunter.” To me. “Huh? Me?” It looked like a box of tonic drinks. I just blinked at it, then a thought flashed through my head and I asked carefully, “Don’t tell me this is money?” “We contracted for weekly pay. Did you forget?” I had. I’d naturally assumed I’d get it on Sunday. I took the box with a dazed look. It was heavy. “Is it usually paid in cash?” “Of course not.” “Then…” “You said you liked cash, Mr. Jin Taekyung. Especially crisp new bills.” I’d mentioned it in passing yesterday—or maybe the day before. I hadn’t expected it to come back like this. My opinion of the exploitative employer rose a little. *Of course, the most important part is still left.* Four days of pay, Tuesday through Friday. My first weekly paycheck as a C-rank Hunter. Of course I couldn’t help looking forward to the amount. I swallowed and opened my mouth. “Then how much is all of this…?” “We put in a little more than the contract says. The settlement details are inside, so check them. We’ll be going.” “Until next time, Hunter.” Team Leader Choi and Butler Kim took off in a flash. It really did happen in an instant. I stared after the receding car lights, bewildered, then opened the drink box. In the faint moonlight, thick bundles of bills caught my eye. *One, two, three…* The count stopped at six. Six bundles of a hundred bills. In other words, six million won. “What is this?” *Scam.* The word flashed through my mind just as my legs were about to give out— “Huh?” Had I seen it wrong? Why were the bills yellowish? “Wait. Wait a second!” I focused internal energy into my eyes, and my vision brightened. Then I saw her. A kindly smiling woman in a hanbok, right there on the bill. “Shin Saimdang! Wise mother and virtuous wife! Her son is Yulgok Yi I! Her husband is Yi Wonsu!” I started speaking in tongues before I even realized it. This was insane. Completely insane. One bundle contained a hundred Shin Saimdang bills. Six of those meant… “Th-three hundred million!” This time I couldn’t catch myself as my legs gave out. I dropped to my knees hard enough to make a thud and stared blankly into the drink box. A white sheet of paper lay beneath the bundles, lining the bottom. *Right. The settlement sheet!* I unfolded the paper in a panic. It contained a complete record of the past four days’ earnings. Right down to the final amount being paid to me. *The settlement says thirty million won?* What? Had I imagined it? I was confused. Completely confused. My shaking gaze froze on the last line. **Bonus: 270,000,000** And then Team Leader Choi’s last words as he left. *We put in a little more than the contract says.* Thunder and lightning tore through my head. I rose on trembling legs. Far off, the car’s lights were already fading. They looked like a single ray of light. “Ahh. Aaaah…” Team Leader Choi. No—he was the Light. [^1]: Korean slang for Friday night, from “burning Friday.” [^2]: In Korean, the same word, *jipsa*, can mean either butler or church deacon. [^3]: Tteokbokki is a Korean dish of chewy rice cakes in a spicy sauce. Korean churches often sell it as a snack.

## Korean source

```text
＃52화



오전 여섯 시.

택시 기사 김 씨는 오늘의 첫 손님을 태웠다. 그리고 10분 만에 후회했다.

‘재수 옴 붙었네.’

겉보기로는 멀쩡하게 생긴 청년이다. 근육질의 듬직한 덩치에 얼굴은 멀끔해서 많이 쳐 줘야 20대 중후반으로 보였다.

그런데…….

“킁카킁카.”

이상하다. 좀 많이.

“흐어어.”

웬 드링크 박스를 보물처럼 꼭 껴안고, 30초에 한 번씩 슬쩍 열어 냄새를 맡는다. 그리고 뭐에 홀린 것처럼 몸을 부르르 떤다.

‘시방 저게 뭐 하는 짓이여.’

김 씨는 뒷골이 싸했다. 10년 넘게 택시를 몰았지만 이런 종류의 진상은 처음이다.

그가 계속해서 옆자리 청년을 곁눈질하던 그 순간.

“아저씨.”

“예, 예?!”

심장 떨어질 뻔했다.

방금 전까지만 해도 퀭하던 청년의 눈동자가, 야수처럼 번뜩이고 있었다.

“뒤에 트럭이요.”

“트, 트럭이요? 파란색?”

“네. 아까 사거리에서부터 따라오는 것 같지 않아요?”

“예? 아니 뭐, 그렇긴 한 것 같은데.”

“미행일지도 모르잖아요.”

이건 또 무슨 참신한 개소린가.

김 씨는 눈동자를 뒤룩뒤룩 굴리다가 결국 그가 원하는 듯해 보이는 원하는 대답을 내놨다.

“여, 옆쪽으로 빠지겠습니다.”

청년은 파란 트럭이 시야에서 사라질 때까지 드링크 박스를 꼭 껴안고 있었다. 마치 누군가가 뺏어 가기라도 할 것처럼.

“습하. 습하.”

물론 틈틈이 냄새를 맡는 것도 빼놓지 않았다.

‘이건 제대로 미친놈이다.’

차 내부는 에어컨 바람이 쌩쌩 부는데, 김 씨의 등허리는 식은땀으로 축축했다. 첫 개시부터 이 모양이라니.

아주 재수 옴 붙은 날이다.



* * *



부아앙.

요금을 건네고 문을 닫자마자 택시가 총알처럼 튀어 나간다.

누가 보면 뒤에서 몬스터라도 쫓아오는 줄 알겠네. 사고라도 나면 어쩌려고. 나는 쯧쯧 혀를 차고 아파트 단지로 들어섰다.

품에는 어제 받은 드링크 박스를 소중히 껴안은 채였다.

‘3억.’

내가 F급 헌터 시절부터 꼬박 3년을 일해서 모은 돈이랑 비슷한 액수다. 물론 지금은 한 푼도 안 남았다.

‘빚 갚는 데 다 썼지.’

그렇게 빚에 허덕이던 때가 있었는데, 이 악물고 하다 보니 점점 나아졌다. 가족을 일산 근처의 안전지대 아파트로 이사 보내기도 했고. 근래 들어서는 뭐, 인생이 롤러코스터 같다.

시스템이 사라지면 추락하는 롤러코스터…….

아니다. 몇 달 만에 오는 집인데 이런 생각은 집어치우자.

‘그런데 몇 동 몇 호였지?’

두어 달에 한 번 꼴로 오는 집이다 보니 늘 이렇다.

나는 다닥다닥 붙어 있는 아파트 단지를 노려보다가 핸드폰을 꺼내 전화를 걸었다. 한참 신호음이 울린 뒤에야 연결됐다.

딸칵.

- 여보세요?

아직 이른 시각이라 자고 있을 줄 알았는데, 하연이의 목소리는 또렷했다.

“일어나 있었어?”

- 일어나 있어야지. 시간이 몇 신데.

“아직 일곱 시도 안 됐는데.”

- 일찍 일어나야 공부가 잘돼.

내 동생이지만 감탄스럽다. 오전 기상을 7대 죄악쯤으로 여기는 진호 형이 이걸 들었어야 했는데.

- 왜 전화했어?

“내가 지금 집 앞이거든.”

- 응? 집 앞이라고?

“어. 근데 우리 집이 어딘지 까먹었어.”

- ……또? 가지가지 한다, 진짜. 기다려.

끊긴 전화를 붙잡고 몇 분쯤 기다렸을까, 어느 동 입구에서 여자애 하나가 슬리퍼를 질질 끌며 나타났다.

멀리서도 느껴지는 날백수 포스. 세상 귀찮다는 그 표정을 보자 나도 모르게 웃음이 나왔다.

“진하연!”

“소리 지르지 마. 사람들 깨.”

……그래, 이래야 내 동생이지.

“웬일이야? 말도 없이.”

“내가 우리 집 오는데 말하고 와야 되냐?”

“하도 드문드문 오니까 그렇지. 부녀회장이 오빠보다 우리 집 더 자주 올걸?”

“그 정도냐?”

“그 정도지.”

그때 엘리베이터가 멈췄다. 현관문 앞에 선 하연이가 비밀번호를 입력하고 문고리를 돌린다.

그리고 그곳에…….

“아들!”

환하게 웃고 있는 한 사람이 있다. 주름진 손과 반쯤 풀린 파마머리. 깜짝 선물을 받은 어린아이처럼 좋아하는 그 모습.

순간 목이 막힌 나는 턱을 긁적이다가 풀썩 웃어 버렸다.

“저 왔어요, 엄마.”

드디어 돌아왔다.

가족이 기다리고 있는 그곳. 집으로.



* * *



지글지글.

엄마는 부엌에서 아침 준비로 한창이다. 기분 좋은 냄새가 코끝을 맴돌았다.

“오랜만에 아들 왔다고 아주 신나셨네, 우리 김 여사.”

하연이가 배를 벅벅 긁으며 옆자리에 주저앉았다.

낡은 소파가 푹 꺼진다. 돼지 같은 년.

“요리 많이 준비하고 계셔?”

“어. 완전 진수성찬. 덕분에 잘 먹겠네.”

대답은 하는데, 눈은 핸드폰 화면에 박혀 있다.

“넌 오랜만에 오빠 봤는데 반갑지도 않냐?”

“응?”

“아니, 뭐. 고생했다고 어깨라도 좀 주물러 줄 수도 있고.”

하연이가 한숨을 푹 내쉬었다.

“왜 이래, 태경 씨. 우리 그런 사이 아니잖아.”

“……말하는 싸가지 봐라.”

이렇게 티격태격 하는 게 하루 이틀은 아니지만 괜히 섭섭하다.

나는, 어? 그렇게 죽을 고비 넘겨 가면서 겨우 돌아왔는데!

“지금 울컥했다. 울컥했지?”

눈치 하나는 귀신이다.

“학교 갈 준비나 해. 급식충아.”

“응. 오늘 개교기념일.”

주먹이 파르르 떨린다. 당장이라도 저 얄미운 뒤통수를 후려치고 싶지만 그러면 진짜 지는 거다.

“때리고 싶죠? 주먹 부들부들 하죠?”

“넌 여자라서 살았다. 불알만 달려 있었어도…….”

“엄마! 오빠가 나 성추행해!”

“야, 야!”

“오빠가 나한테 불. 읍, 읍!”

입을 틀어 막힌 하연이가 발버둥 친다. 때리고, 꼬집고. 그래 봤자 열아홉 살 여자애라 아프지도 않다.

그러다가 우연히, 녀석이 내뻗은 발이 소파 한구석에 고이 모셔 둔 드링크 박스를 강타했다.

퍽.

촤르르륵.

활짝 열린 박스. 거실 바닥에 쏟아지는 누런 지폐 뭉치.

순간, 하연이의 몸이 굳었다.

“이제 그만들 싸우고 아침 먹……어.”

거기에 부엌에서 나온 엄마까지.

일시 정지 버튼을 누른 것처럼 모든 게 멈춘 거실에, 찌개 끓는 소리만 잔잔하게 깔렸다.

지글지글.

나는 어색하게 웃으며 입을 열었다.

“밥 먹고 말하면 안 될까요?”

“……아들?”

“읍읍읍.”

아무래도 아침 식사는 한참 뒤로 미뤄질 것 같다.



* * *



가족들에게 지금까지의 일들을 적당히 각색해서 들려 주었다.

C급으로의 재각성, 그리고 돈의 출처까지.

“그렇게 된 거예요.”

반응은 두 가지로 나뉘었다.

“그렇구나.”

멍하니 고개를 끄덕이는 엄마.

그리고.

“증거.”

“…….”

그래, 넌 기대도 안 했다. 나는 한숨과 함께 지갑을 던져 주었다.

“뭐야?”

“확인해 봐.”

하연이가 의구심 가득한 눈으로 나를 바라보다가 지갑을 뒤지기 시작한다. 워낙 든 게 없는 지갑이라 ‘그것’을 찾는 데에는 얼마 걸리지 않았다.

“헐.”

손에 들린 카드 한 장. 이틀 전 협회에서 발급받은 C급 헌터 자격증이다.

“위조된 거 아냐?”

“맞을래?”

“진짠가 보네.”

“그거 위조하면 중범죄야, 인마.”

“저 돈은? 오빠 말대로 그, 최 팀장인가 뭔가 하는 그 사람이 준 거야?”

“몇 번 말해야 믿을래.”

“350번 정도?”

말과는 달리 이제는 믿는 눈치다. 은색으로 반짝이는 C급 헌터 자격증, 차곡차곡 쌓은 3억 원의 돈다발.

전부 이 낡고 좁은 거실과는 동 떨어진 물건들이다.

멍한 눈으로 앉아 있던 엄마가 신음처럼 중얼거렸다.

“이게 다 무슨 일이라니…….”

하연이도 세상 다 산 노인네처럼 허허 웃는다.

“그러게. 살다 보니 별일이 다 있네.”

“너 아직 스무 살도 안 됐거든.”

“말이 그렇다는 거지. 근데 엄마.”

“으, 응?”

“탄내 나.”

“맞다, 찌개!”

반쯤 풀려 있던 엄마의 눈이 번쩍 뜨인다. 급한 대로 내가 몸을 일으켰지만, 부엌은 이미 초토화가 되어 있었다.

뒤이어 따라온 엄마가 발을 동동 굴렀다.

“아이고, 이걸 어째!”

잔뜩 졸아 버린 국물에 숯덩이가 된 생선. 오랜만에 집밥을 먹을 수 있을 것 같아 기대했는데…….

뭐, 이런 전개도 나쁘지 않지.

“오랜만에 외식이나 하러 가요.”

평소 같았으면 식당 가격의 부조리를 일장연설 했을 엄마도, 치킨이나 시켜 달라고 했을 하연이도 이번만큼은 조용했다.

“동생아.”

“네, 오라버니.”

“돈 챙겨라.”

“옛썰.”

하연이가 기다렸다는 듯이 돈다발을 쓸어 담았다.



* * *



“손님. 죄송하지만 저희 레스토랑은 복장 규정이…….”

코스 요리 먹는 데 1인당 수십만 원을 지불해야 한다는 고급 레스토랑의 지배인이 난처한 웃음을 지었다.

“복장 규정이요?”

“네. 보시면 아시겠지만 다른 손님들도 마찬가지거든요.”

진짜네. 남자고 여자고 할 것 없이 죄다 정장에 원피스, 심지어는 드레스도 있다.

‘시바, 누가 보면 무도회장에 춤추러 온 줄 알겠네.’

여기가 무슨 18세기 프랑스야?

국밥집만 드나들었던 내게는 엄청난 문화 충격이다.

“그냥 다른 데 가자.”

“그래, 하연이가 이 근처 맛집 많이 알더라.”

나보다도 식구들이 더 무안해하는 것 같아 그냥 나왔다.

레스토랑 유리에 우리 셋의 모습이 비친다. 오랜만의 외식이라고 신경 써서 입었을 게 분명한데, 가진 옷이라고는 죄다 시장 메이커에 오래 입은 티가 난다.

‘돈이 부족했나?’

나 먹는 거, 입는 거 아껴 가며 번 돈의 대부분을 집에 보냈다.

F급 헌터였을 때도 남들보다 배로 일하니 결코 적은 돈은 아니었을 텐데.

“아들, 삼겹살 먹으러 갈까? 아침부터 기름진 음식은 좀 그런가?”

“삼겹살 좋지. 엄마가 뭘 좀 아네. 친구가 저 앞 사거리 고기집 갔는데 엄청 맛있었대.”

겨우 삼겹살.

지갑에는 C급 헌터 자격증이 있고 가방에는 돈다발이 가득하다. 그걸 모를 리 없는데, 걱정 없이 사치 부려도 되는데.

‘내가 일하는 이유가 그건데.’

누가 그랬다.

행복은 돈으로 살 수가 없다고. 행복에는 가격표가 없다고.

개인적으로 그런 소리 하는 놈들한테 한마디만 하고 싶다.

‘좆 까.’

없어서 못 쓰는 게 돈이다. 그리고 이 돈을 어떻게 써야 할지 어젯밤 내내 고민한 끝에 마침내 결심했다.

적어도 오늘 하루만큼은 가족을 위해 아낌없이 쓰기로.

지금, 그 결심이 훨씬 크기를 부풀렸다.

“우리 밥 좀 늦게 먹자.”

대답을 기다리지 않고 지나가는 택시를 붙잡았다.

“어디로 모실까요?”

“미래 백화점이요.”

근방에서 가장 크고 비싸다는 백화점이다. 룸미러 속 엄마가 눈을 동그랗게 떴다.

“백화점?”

반면 하연이의 입꼬리는 음흉하게 솟구쳤다.

“좋네. 돈 많은 오빠가 옷도 사 주고.”

역시 눈치 빠른 녀석. 척하면 착이다. 나는 피식 웃었다.

“사고 싶은 거 다 사.”

“진짜?”

“엄마 것부터 골라 주고.”

“오케이.”

“효자 아드님 두셨네. 허허.”

기사의 너스레에 비로소 엄마가 웃었다.



* * *



“진짜 다 산다?”

“다 사.”

최종 확인이 끝나자 하연이는 고삐 풀린 망아지처럼 백화점을 누볐다. 옷을 스캔하는 눈썰미도 매섭고 동작은 또 어찌나 빠른지 각성자가 아닌지 의심될 정도다.

처음에는 옷보단 가격표를 보던 엄마도 어느 순간부터 적극적으로 움직이기 시작했다.

“엄마, 이거 어때?”

“너무 짧지 않니?”

“이거!”

“괜찮네.”

“이것도!”

“예쁘네. 저기 언니, 이 옷 한 사이즈 더 큰 거 없어요?”

그렇게 두 시간이 지나고…… 나는 신체의 변화를 느꼈다.

‘죽겠다.’

이유를 알 수 없는 극심한 호흡 곤란과 다리 통증.

무림에서 조필을 상대했을 때와 비슷한 수준의 무력감이 온몸을 감싼다.

“오빠, 나 어때?”

“못생겼어. 저리 꺼져.”

“아들, 이거 입어 봐.”

“안 입어 봐도 될 것 같아요. 그걸로 살게요.”

그날 우리가 몇 벌의 옷을 샀고, 얼마를 썼는지는 모르겠다.

다만 쇼핑을 모두 끝내고 돌아갈 때쯤에는 백화점 높은 분이 우리를 배웅했으며.

“어서 오십시오.”

복장 규정이 철저하다던 레스토랑의 지배인은 우리를 알아보지도 못했다.

“우와, 나 이런 거 처음 먹어 봐.”

“그러게. 어쩜 요리를 이렇게 예쁘게 하지?”

소곤거리는 엄마와 하연이의 뺨이 불그스름하다.

수십만 원짜리 코스 요리를 먹으려고 그 수십 배쯤 되는 돈을 썼지만 하나도 아깝지 않은 날이었다.

“근데 밥 먹고 싶다. 느끼해.”

“여기 왜 이렇게 양이 적니?”

……아깝지 않은 척했다.
```

## Current accepted English baseline

```markdown
# Chapter 52

Six in the morning.

Taxi driver Mr. Kim picked up his first fare of the day.

And regretted it ten minutes later.

*I’ve been jinxed.*

The young man looked perfectly normal at first glance. Sturdy, muscular build, clean-cut face—even being generous, he only looked mid-to-late twenties.

But then…

“Sniff, sniff.”

Something was off. Very off.

“Huuugh.”

He was hugging a drink box like treasure, cracking it open every thirty seconds to smell it, then shuddering like he was possessed.

*What in the world is he doing?*

A chill crawled up the back of Mr. Kim’s neck. He had been driving a taxi for more than ten years, but he had never had a problem customer quite like this.

He kept stealing glances at the young man in the passenger seat, and in that moment—

“Mister.”

“Yes, yes?!”

He nearly had a heart attack.

The young man’s eyes, hollow only a moment ago, were gleaming like a beast’s.

“There’s a truck behind us.”

“A-a truck? A blue one?”

“Yes. Doesn’t it look like it’s been following us since that intersection?”

“Huh? Well, I suppose it does.”

“It might be tailing us.”

What fresh bullshit was this?

Mr. Kim’s eyes darted around, and in the end he gave the answer the young man seemed to want.

“I-I’ll peel off to the side.”

The young man hugged the drink box tight until the blue truck disappeared from view. As if someone might snatch it away.

“Sniff. Sniff.”

Of course, he didn’t skip smelling it whenever he got the chance.

*This guy’s completely insane.*

The AC was blasting inside the car, but Mr. Kim’s back was soaked with cold sweat.

And this was the first fare of the day.

A thoroughly jinxed day.

* * *

Vroom.

The moment I handed over the fare and shut the door, the taxi shot off like a bullet.

Anyone watching would’ve thought a monster was chasing it. What if he got in an accident?

I clicked my tongue and headed into the apartment complex.

I still had yesterday’s drink box hugged carefully to my chest.

*Three hundred million won.*

About as much as I’d saved over three full years as an F-rank Hunter. Of course, I didn’t have a single won of that left now.

*I spent it all paying off debts.*

There had been a time when I was drowning in debt, but I’d gritted my teeth and kept at it until things gradually got better. I’d even moved my family to a safe-zone apartment near Ilsan.

Lately, though, my life had been like a roller coaster.

A roller coaster that dropped whenever the System disappeared…

No. I was coming home for the first time in months. I should drop thoughts like that.

*Which building and unit was it again?*

I only came here once every couple of months, so it was always like this.

I glared at the apartment buildings packed in tight, then pulled out my phone and called. The ringtone went on for a long time before the line finally connected.

Click.

“Hello?”

I’d figured Hayeon would still be asleep this early, but her voice was clear.

“You were already up?”

“I have to be. Do you know what time it is?”

“It’s not even seven.”

“I study better when I get up early.”

My little sister never failed to impress me. Jinho hyung, who treated getting up in the morning like one of the seven deadly sins, should’ve heard that.

“Why’d you call?”

“I’m out front.”

“Huh? Out front?”

“Yeah. But I forgot which place is ours.”

“……Again? You really do the damnedest things. Wait there.”

I stood there holding the dead phone. After a few minutes, a girl appeared at the entrance of one of the buildings, dragging her slippers.

Even from a distance, she radiated total bum energy. That face said the whole world was too much trouble, and I couldn’t help smiling.

“Jin Hayeon!”

“Don’t yell. You’ll wake people up.”

……Yeah. That was my little sister.

“What brings you here? You didn’t even tell us you were coming.”

“Do I have to announce it every time I come to my own house?”

“You come so rarely. The residents’ association president probably visits more than you do.”

“That bad?”

“That bad.”

The elevator stopped. Hayeon punched in the password at the front door and turned the handle.

And there—

“Son!”

Someone stood there beaming.

Wrinkled hands. A perm half fallen out. She looked as happy as a kid getting a surprise gift.

My throat tightened. I scratched my chin, then burst out laughing.

“I’m home, Mom.”

I had finally come back.

To the place where my family was waiting.

Home.

* * *

Sizzle, sizzle.

Mom was busy with breakfast in the kitchen. A good smell hung in the air.

“Mrs. Kim is really excited now that her son’s home after so long.”

Hayeon scratched her stomach and plopped down beside me.

The old sofa sagged.

What a pig.

“Is she making a lot?”

“Yeah. A whole feast. Looks like we’re eating well today.”

She answered, but her eyes stayed glued to her phone.

“You haven’t seen your brother in ages. Aren’t you happy to see me?”

“Huh?”

“I mean, you could at least massage my shoulders after all the work I did.”

Hayeon let out a long sigh.

“What’s gotten into you, Mr. Taekyung? We’re not that kind of siblings.”

“……Listen to that attitude.”

It wasn’t like we’d only started bickering yesterday, but I still felt a pang.

I mean, I’d barely made it back after brushing past death!

“That got to you just now, didn’t it?”

Her radar was scary.

“Go get ready for school, you little cafeteria parasite.”

“Mm. Today’s the school founding anniversary.”

My fist trembled.

I wanted to smack the back of that irritating head right then and there, but doing it would mean I’d really lost.

“You want to hit me, don’t you? Your fist is shaking.”

“You’re lucky you’re a girl. If you had balls, I would’ve—”

“Mom! My brother’s sexually harassing me!”

“Hey, hey!”

“He said my b—mmph!”

I clamped a hand over Hayeon’s mouth. She thrashed, hitting and pinching, but she was still just a nineteen-year-old girl. It didn’t hurt.

Then, by pure coincidence, the foot she flung out slammed into the drink box I’d set so carefully in the corner of the sofa.

Thump.

Flutter.

The box flew wide open.

Yellow bundles of bills spilled across the living-room floor.

Hayeon froze.

“Come on, stop fighting and eat your breakf—”

Mom had come out of the kitchen too.

Everything in the living room stopped as if someone had hit pause. Only the quiet sound of stew simmering filled the space.

Sizzle, sizzle.

I smiled awkwardly and opened my mouth.

“Can’t we talk about this after breakfast?”

“……Son?”

“Mmph, mmph, mmph.”

Breakfast was probably going to be delayed for quite a while.

* * *

I told my family a suitably edited version of everything that had happened so far.

My reawakening as a C-rank Hunter, and where the money had come from.

“So that’s how it happened.”

Their reactions split in two.

“I see.”

Mom nodded blankly.

And then—

“Proof.”

“……”

Yeah. I hadn’t expected anything else from you.

I sighed and tossed her my wallet.

“What’s this?”

“Check it.”

Hayeon looked at me with suspicion, then started digging through the wallet. There was barely anything in it, so it didn’t take her long to find *it*.

“Whoa.”

A single card in her hand.

The C-rank Hunter license the Association had issued me two days ago.

“This isn’t fake, is it?”

“Want to get hit?”

“Guess it’s real.”

“Forging one is a serious crime, you idiot.”

“What about that money? Did that Team Leader Choi or whoever really give it to you, like you said?”

“How many times do I have to tell you before you believe me?”

“About three hundred and fifty?”

Despite her words, she seemed to believe me now.

The C-rank Hunter license gleaming silver. Neatly stacked bundles of three hundred million won.

Every bit of it looked completely out of place in this old, cramped living room.

Mom sat there staring blankly and muttered, almost a groan.

“What on earth is all this……?”

Hayeon let out a hollow laugh like an old woman who had seen everything life had to offer.

“I know. You live long enough, you see it all.”

“You’re not even twenty yet.”

“It’s just an expression. But, Mom.”

“Y-Yes?”

“I smell burning.”

“Oh, right! The stew!”

Mom’s half-lidded eyes flew open. I got up in a hurry, but the kitchen was already a wreck.

Mom followed me in, stomping her feet.

“Oh no, what do we do!”

The broth had boiled down to almost nothing, and the fish had turned to lumps of charcoal. I’d been looking forward to a home-cooked meal after so long, but……

Well, this kind of development wasn’t so bad either.

“Let’s go eat out. It’s been a while.”

On any other day, Mom would’ve launched into a whole speech about how ridiculous restaurant prices were, and Hayeon would’ve asked us to order chicken. This time, both of them stayed quiet.

“Little sister.”

“Yes, dear brother.”

“Grab the money.”

“Yessir.”

Hayeon swept up the bundles like she’d been waiting for the order.

* * *

“I’m sorry, but our restaurant has a dress code…….”

The manager of the upscale restaurant—where a course meal ran to several hundred thousand won a person—gave us an awkward smile.

“A dress code?”

“Yes. As you can see, the other guests are the same.”

He was right. Men and women alike, all in suits and dresses. Some were even in evening gowns.

*Shit. Anyone watching would think they’d come here to dance at a ball.*

What was this, eighteenth-century France?

For someone like me, who’d only ever gone to gukbap[^1] places, it was a massive culture shock.

“Let’s just go somewhere else.”

“Yeah. Hayeon knows a lot of good restaurants around here.”

The family looked even more embarrassed than I did, so I just walked out.

The three of us were reflected in the restaurant glass. We’d clearly dressed up for our first meal out in a long time, but every piece we owned was cheap market-brand stuff that already looked well-worn.

*Had they been that short on money?*

I’d sent most of what I earned home, cutting back on food and clothes for myself.

Even as an F-rank Hunter, I’d worked twice as hard as other people. It shouldn’t have been a small amount.

“Son, should we go get pork belly? Maybe greasy food is a bit much this early in the morning.”

“Pork belly’s good. Mom knows what’s what. A friend went to the meat place at the intersection up ahead and said it was amazing.”

Just pork belly.

I had a C-rank Hunter license in my wallet and a bag stuffed with cash. It wasn’t like they didn’t know that. They could splurge without worrying.

*That’s why I work.*

Someone once said you can’t buy happiness with money. That happiness doesn’t have a price tag.

Personally, I had one thing to say to people who talked like that.

*Fuck off.*

Money’s what you can’t spend because you don’t have it.

And after thinking all night about how to use this money, I’d finally made up my mind.

At least for today, I would spend it freely on my family.

Right now, that decision had swollen even bigger.

“Let’s eat a little later.”

Without waiting for an answer, I flagged down a passing taxi.

“Where can I take you?”

“Mirae Department Store.”

It was supposed to be the biggest, most expensive department store in the area. In the rearview mirror, Mom’s eyes went round.

“The department store?”

Meanwhile, the corners of Hayeon’s mouth curled up slyly.

“Nice. My rich oppa can buy me clothes too.”

Sharp as ever. I only had to say the word and she got it.

I snorted.

“Buy whatever you want.”

“Really?”

“Pick out Mom’s things first.”

“Okay.”

“You’ve got yourself a devoted son, ma’am. Ha ha.”

Only then did Mom smile at the driver’s banter.

* * *

“You’re really buying everything?”

“Everything.”

Once I confirmed it for the last time, Hayeon tore through the department store like a colt off its reins. The way she scanned clothes was viciously sharp, and she moved so fast I started to wonder if she was an Awakened.

At first, Mom looked at the price tags more than the clothes. Before long, she started moving with enthusiasm too.

“Mom, what do you think of this?”

“Isn’t it too short?”

“This one!”

“That’s nice.”

“This too!”

“That’s pretty. Excuse me, miss—do you have this in one size larger?”

Two hours passed, and I felt a change in my body.

*I’m dying.*

Crushing shortness of breath and pain in my legs, for no reason I could name.

Helplessness wrapped around my whole body at about the same level as when I’d faced Jopil in Murim.

“Oppa, how do I look?”

“You’re ugly. Get lost.”

“Son, try this on.”

“I don’t think I need to try it. I’ll take that.”

I don’t know how many clothes we bought that day, or how much we spent.

All I know is, by the time we finished shopping and headed out, someone high up at the department store had come to see us off.

“Welcome.”

The manager of the restaurant that had been so strict about its dress code didn’t even recognize us.

“Wow, I’ve never eaten anything like this before.”

“I know. How do they make the food look this pretty?”

Mom and Hayeon spoke in hushed voices, their cheeks flushed.

We’d spent dozens of times more than the several-hundred-thousand-won course meal just to eat it, but it was a day when not a single won felt wasted.

“But I want rice. This is too rich.”

“Why are the portions so small?”

……I pretended it didn’t.

[^1]: A cheap Korean rice-and-soup meal, typically eaten at modest diners.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 52`.

# Master Edit Task — Chapter 86

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

| 임춘수    | **Im Chunsoo**    |
| 임창수    | **Im Changsoo**   |
| 명성               | **Fame**                       |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 임꺽정 | **Im Kkeokjeong** |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 대한민국 | **Korea** | Country reference. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 고생하셨습니다 | register | Subordinate courtesy (“thank you for your hard work”), not a superior’s “Good work.” | |

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

#### Chapter 84 tail (verified mastered)

…
“Im Chunsu.” “What’s the Sangdong Guild Master’s name?” “Im Chunsu.” What a strange coincidence. Im Changsoo’s father and the Sangdong Guild Master had the same name. Then again, the world was a big place, and plenty of people shared the same name. “Hey, I’m only asking just in case, so forgive me for prying… but what does your father do for a living?” “He’s a Hunter.” “Just a Hunter?” “He runs a Guild.” “Oh, I see.” This bastard was the Sangdong Guild Master’s son. A brief silence passed, and in that short interval, I realized what had seemed so familiar about Im Changsoo. “Are you that guy?” “A dog?” “No, I’ve heard about you before.” It was a story I’d heard around this time two years ago and let go in one ear and out the other. The Sangdong Guild Master’s only son, born late in his life, had awakened as a B-rank Hunter and secured a position in his father’s Guild. But he was such a womanizer that he had become a constant headache. And the nickname he had earned was… “Horndog. Right?” Im Changsoo answered by hanging his head. It was an embarrassing nickname to hear in front of other people, to be sure. But since I had to collect four billion won, I comforted him in a warm voice. “It’s okay, man. Guys can be like that sometimes. I used to dream of living like you, too.” But reality was cruel, and that dream had seeped into a hundred-terabyte USB drive. Jinho hyung, a renowned authority in the world of porn, once borrowed my USB. When he showed up again, he had a hollow-eyed expression and left me with a one-line review. *This should be designated a UNESCO World Heritage Site.* Anyway. Im Changsoo lifted his head at my warm consolation. “Really?” *Of course not.* Did I look like the kind of guy who hit on just any woman? I was the sunflower of this era, gazing at only one person in the entire world—Miss Song-i… *Wait a second.* This bastard had hit on Miss Song-i earlier. “You little shit.” “Ack!” Frightened before I had even done anything, Im Changsoo reflexively placed his hand on his sword hilt. Shing. Clack. But the blade had barely made it halfway out before it was forced back into its sheath. I had closed the distance like lightning, pressing down on his sword hilt as I kicked his legs out from under him. Crash! He lost his balance and fell. When I pressed down on his neck, his face went white. “Ghk! Cough!” “You little bastard. Where do you get off pulling that thing on me?” Getting beaten by Jin Mukyung had certainly paid off. In the past, I wouldn’t have been able to subdue a B-rank Hunter with such a simple, fluid movement. Im Changsoo was probably surprised, but I was even more surprised. “This is a Gate, you idiot. You said so yourself earlier. Did you already forget?” “I’m sorry! I’m sorry!” I wanted to beat him senseless, but since it had only been an attempt, I decided to let him off. *It absolutely wasn’t because I hadn’t received the four billion yet.* “Damages.” “Ghk. What?” “You drew your sword. Don’t you know that’s attempted murder? And you owe me and Miss Song-i—no, all our Guild members—a sincere apology.” “What are you talking about?” Im Changsoo looked around at the others with an aggrieved expression, but no one came to his aid. His team members merely shrank back whenever my gaze landed on them. Meanwhile, our Guild members, who had been watching the spectacle, took it one step further. “Drawing a sword on a member of a partner Guild. Well, I never.” Butler Kim clicked his tongue as if he felt sorry for him. “You’re only doing this because you don’t want to pay, aren’t you? My goodness, Changsoo, that’s so low. Isn’t it, Uncle?” “Hmm? Uh-huh. What a nasty young man!” Miss Song and Im Kkeokjeong delivered a lowlife-and-nasty-man combo. Then Team Leader Choi dealt the final blow. “Now, would everyone take a look at my helmet? This product is a custom-made helmet produced by Xyliton, a famous Finnish equipment manufacturer. It has all sorts of functions, but most importantly, it has been enchanted with a video-recording spell…” Im Changsoo stared at everyone with his mouth hanging open, betrayed and utterly dumbfounded. Then he let out a long sigh. “I’ll do it.” “What did you say?” “I said I’ll do everything you tell me to!” That was the answer I had been waiting for. I happily helped him back to his feet. “Good choice, kid. We can discuss the damages at our leisure.” “…This is driving me crazy. If my boomer finds out, I’m dead.” “Would you rather die here?” “You don’t want the four billion?” “You’ve got some nerve.” Im Changsoo let out another deep sigh before speaking. “May I ask one question?” “One hundred million per question.” “…” “I’m kidding. Go ahead.” “What do you really do?” Was he really that curious? I let out a quiet laugh and answered him. “Someone with two jobs.” A Hunter and a Murim martial artist. The only two-job combination in the world. [^1]: *Hongik Ingan*, meaning “to broadly benefit humanity,” is Korea’s national founding ideal. Taekyung twists the opening sound *hong* into a joke about Im Changsoo’s reddening face.

#### Chapter 85 tail (verified mastered)

…
raid team made up of four B-rank Hunters and five C-rank Hunters who would obey his commands. He had trained every one of them to eat only from his hand. “Fine. Then listen carefully to what I’m about to say…” After a short and simple explanation, the team members couldn’t hide their nervousness. “Will it work?” “It does seem possible.” “Oppa, you’re not suggesting what I think you are, right? If you mean killing someone, I don’t know if I can do that.” “Didn’t you just say you’d do anything I told you?” “Even so, that’s a little…” “Forget it. I’d like to, but I’m not reckless enough to go that far. First, we take the camera. Then we put that son of a bitch through a humiliation he’ll never live down.” “Whew. That’s a relief. Then I’m definitely on your side, oppa.” “Do it right. You know what happens if anyone hesitates this time or holds back even a little, right?” “Of course.” “Just trust us, Team Leader. No, hyungnim. Hehe.” A sinister smile spread across Im Changsoo’s lips. *If he trampled on my pride, he has to pay the price.* In the Boss Zone ahead, he would make Jin Taekyung understand exactly who he had dared to cross. There was even a monster there capable of standing against him. *The Minotaur Great Warrior.* The boss monster of **The Minotaur’s Labyrinth**. Despite being only a B-rank monster, it was a monstrous creature whose physical abilities rivaled those of an A-rank. *Once the Great Warrior wears him down, we’ll make our move.* Set a barbarian against a barbarian. Defeat a monster with a monster. The moment both sides were exhausted would be their chance. In one stroke, he could recover both the money he was about to lose for nothing and the pride that had been dragged through the dirt. “Hey, hurry up! It’s the Boss Zone!” Jin Taekyung’s shout rang out the next moment. Im Changsoo smiled broadly. “Yes! Coming!” His steps toward the Boss Zone were remarkably light. * * * “One Annihilation.” Kraaaaaash! The sound of the sky splitting erupted from the tip of my spear. A white vortex that tore apart and devoured everything it touched slammed into the Great Warrior’s muscular chest. —Moo? Crack-crack-crack! There was no need to check whether it was alive or dead. The moment I pulled my spear from its chest, the System notification rang out. Ding. > **System** > > - Defeated **Lv. 70 Minotaur Great Warrior**! > > - Level Up! > > - Quest, **B-rank Gate Clear**, completed! > > - Calculating your contribution… Complete! > > - The Quest Success Reward has been deposited into your Inventory! “Whew.” The last one should always end with one big hit. My body was incredibly tired, though. I shook the blood from my spear and turned around. “Let’s collect the byproducts and get out of here. I’m starving to dea—why are you all looking at me like that?” Im Kkeokjeong spoke for everyone. “You really have to ask?” He looked back and forth between the boss monster’s corpse and me. His eyes demanded some kind of explanation for how I had finished off a B-rank boss monster with a single blow. “Hmm. Let’s just say I got lucky.” “Lucky?” “Yes. Lucky.” It really was because I had been lucky. Lucky that I had lived in a goshiwon.[^1] Lucky that a capsule had been discarded in front of it. All of it. “Good grief. I’m too dumbfounded to speak. Fine.” The others reacted much the same way as Im Kkeokjeong. Even Team Leader Choi, who had already been on a raid with me, looked stunned. “I didn’t realize you were this capable.” “If you know now, that’s enough.” “Could we discuss this?” “Of course.” Not now. Later. I still had something more important to take care of. With my most charming smile, I approached one person. “Miss Song, could I ask you for a heal—what are you guys doing over there?” “Ah.” “What are you doing? Why are you here?” “We’re just…just standing here.” “I-I just think she’s so beautiful.” The Sangdong Guild members clustered around Song Song jumped in surprise and began blurting out whatever came to mind. *What’s with these guys?* I only meant that they should get lost because they were getting in the way between me and Miss Song. *Do I really look that scary?* “Where’s Im Changsoo?” At a single word from me, the Sangdong Guild members split apart like the Red Sea. Im Changsoo answered from behind them, his face white as a sheet. “I’m here.” “What’s wrong with your face? Are you sick?” “I-I think I’m coming down with something.” “Tsk, tsk. Take a potion, you idiot. Your family’s rich.” “…” “Anyway, hurry up and collect the byproducts. Let’s go. I’m tired.” “Yes, yessir.” Once Im Changsoo disappeared with the nuisances, the moment I had been waiting for finally arrived. I flashed Song Song a bright smile. “You’re hungry, right? How about steak at a nice restaurant for dinner?” Song Song smiled back at me. “I’m sorry, but I’m a vegetarian.” “That’s strange. You seemed to eat meat just fine yesterday. How about a salad bar?” “I’m a carnivore.” “…” *I got rejected, right?* [^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement, often used by students and people on tight budgets.

## Korean source

```text
＃86화



“아이고, 고생하셨습니다.”

담당 공무원이 허겁지겁 뛰쳐나와 우리를 맞이했다.

뭐, 정확히는 임창수를 맞이했다고 해야 옳겠지.

우리가 가져온 각종 부산물이며 마정석을 꼼꼼하게 확인한 그가 호들갑을 떤다.

“이야, 물량이 엄청나네요. 이 정도면 미로에 있는 미노타우로스들이 씨가 말랐겠어요.”

“…….”

창백한 안색의 임창수가 대답 없이 고개만 끄덕이니 담당 공무원이 눈치를 살폈다.

“팀장님, 혹시 편찮으신 곳이라도?”

언제부터 담당 공무원이 헌터 건강까지 챙겨 줬는지 모르겠군.

나는 괜한 말이 나오기 전에 임창수를 옆구리를 쿡 찔렀다.

“대답하셔야죠. 창. 수. 씨.”

“……아닙니다. 전 괜찮아요.”

“아, 그러시다면 다행이고요.”

이상한 분위기를 감지한 걸까? 담당 공무원이 미심쩍은 눈빛으로 나를 쳐다봤지만 딱 거기까지였다.

“부산물 처리는 어떻게 하시겠습니까? 아시는 대로 두 가지 방법이 있습니다만.”

담당 공무원의 말대로 부산물의 판매 방식은 두 가지로 나뉜다.

개인 판매와 위탁 판매. 전자의 경우는 말 그대로 해당 물품의 소유주인 개인이 알아서 거래를 하는 방식이고, 위탁 판매는 관리청, 즉 정부 기관에 맡겨 판매하는 거다.

‘각기 장단점이 있지.’

희소성이 있는 물건은 개인 판매가 이득이고, 그게 아니라면 정부 기관에 넘기는 게 속 편하다. 명품 경매와 시장 경매의 차이랄까?

“어떻게 할까요?”

임창수의 물음에 김 집사가 나섰다. 이번 게이트의 레이드에서는 한 번도 나선 적 없지만 그도 베테랑 헌터다. 오히려 이쪽에 대해선 이 중 누구보다도 더 빠삭할 것이다.

“관리청에 판매하겠습니다.”

소는 버릴 게 없다더니, 미노타우로스도 마찬가지였다.

가죽은 장비 제작에, 뼈는 푹 고아 보양식으로 쓰이며 뿔은 마니아들에게 수집품으로 인기가 있다.

“잘 생각하셨습니다.”

담당 공무원이 세상 기쁜 표정으로 부산물을 정산하기 시작했다. 사는 건 관리청인데 저 아저씨가 좋아하는 이유는 뻔하다.

‘떡고물 좀 떨어지나 보네.’

뭐, 담당 공무원이 얼마를 해 먹든 내 알 바 아니다.

오늘 내가 챙긴 떡고물이 훨씬 크니까.

툭툭.

“약속한 금액은?”

임창수가 바짝 굳은 얼굴로 대답했다.

“드, 드리겠습니다.”

“언제까지?”

“내일까지 보내 드리겠습니다.”

40억을 내일까지? 확실히 부잣집 아들이라 시원시원하다. 나는 활짝 웃으며 쪽지를 건넸다.

“어휴, 그럼 나야 좋지. 여기 내 계좌 번호. 가보처럼 간직하고 있다가 내일 보내 줘. 나중에 잃어버렸다고 하면 재미없어요. 알죠?”

“……넵.”

이 정도면 됐겠지? 나는 임창수의 등을 툭 치는 걸로 작별 인사를 대신했다.

비틀거리는 걸음으로 멀어지는 녀석의 뒷모습을 흐뭇하게 지켜보고 있던 내게 임꺽정이 물었다.

“저놈이 약속한 돈을 줄까?”

“안 주면요?”

“그 뭐냐. 좀 거시기 하잖아. 상동 길드면 근방에서 힘깨나 쓰는 중견 길드인데. 저놈이 배 째라 식으로 나오면…….”

“에이, 증거 영상도 있는데 설마.”

“증거야 없애면 되는 거고. 뭣보다 내가 좀 들은 게 있어서 그래.”

“그게 뭔데요?”

이렇게까지 말하니까 살짝 신경이 쓰이기 시작한다.

잠시 눈치를 살피며 주위를 두리번거린 임꺽정이 작은 목소리로 속삭였다.

“상동 길드장. 누군지는 대충 알지?”

“네. 이름은 오늘 처음 들어 봤지만.”

임춘수. 왠지 모르게 술배 불룩하게 나온 중년 아저씨가 연상되는 이름이지만 상상과 현실은 정반대다.

“대격변 때 혁혁한 전공을 세웠던 A급 헌터잖아요. 사람들이 뭐라고 부르더라? 프, 프. 갑자기 생각이 안 나네.”

“프로즌(Frozen).”

“아, 맞다. 프로즌. 빙결 전문 마법사.”

유명한 헌터들의 경우 그에 맞는 이명(異名)이 붙는다.

임춘수의 경우도 그랬다. A급 헌터인 그는 대격변에서 큰 활약을 보여 준 마법사였고, 그중에서도 특히 빙결 관련 마법에 능해서 프로즌이라는 이명이 붙었다.

“그 양반이 빙결 계통으로는 국내 다섯 손가락 안에 들지. 그 명성을 바탕으로 지금의 상동 길드를 키워 낸 거고.”

처절했던 대격변이 종막을 고하자 1세대 헌터들은 선택의 기로에 섰다. 은퇴를 할 것인가, 현역으로 남을 것인가. 임춘수는 후자를 선택했고 상동 길드를 세웠다.

“대단하네요. 아들은 별거 없던데.”

아무리 A급 헌터라도 맨주먹 하나로 대격변에서 살아남아 부와 명예 모두를 얻은 경우는 흔치 않다. 임춘수의 현재는 많은 헌터들이 꿈꾸는 미래다.

“대단? 확실히 대단하지. 핏줄이라는 게.”

임꺽정이 멀어져 가는 임창수의 뒷모습을 턱짓했다.

“저 녀석이 누구 피를 물려받았는지 잊지 마라.”

“그게 무슨…….”

“자랑은 아니지만 내가 이 바닥 생활 시작한 지 20년이 넘었어. 내가 생초짜이던 시절에 상동 길드가 세워졌지.”

“그런데요?”

“지금도 그렇지만 당시 부천은 길드들끼리 경쟁이 치열했거든. 도저히 신생 길드가 끼어들 틈이 없었어.”

“임춘수는 그걸 뚫었다?”

“그렇지. 그래서 무서운 사람인 거고.”

“음.”

이게 그렇게 연결이 되나?

길드 간 경쟁 심리야 하루 이틀 일이 아니고 능력 있는 쪽이 살아남는 건 실력 위주의 사회에선 당연한 일이다.

“그 사람 정도면 헌터로서의 능력도 출중하고 명성도 있었잖아요. 인맥도 빵빵했을 거고.”

“다른 길드장들은 아니었을 것 같냐?”

“네?”

“임춘수에 비해 명성은 조금 부족했을지 몰라도 하나같이 다 전쟁 영웅 출신들이었어. 상동 길드보다 몇 년이나 앞서 시장을 개척하고 상당수의 게이트를 점유하고 있었지.”

임꺽정이 낮은 목소리로 말을 이었다.

“아직 체계가 완벽히 잡히지 않아서 온갖 불법이 횡행할 때였다. 지금 상동 길드가 존재할 수 있는 건 임춘수가 경쟁자들을 모두 박살 냈기 때문이야. 결코 호락호락한 사람이 아니라는 거지.”

문득 뇌리를 스치는 생각이 있었다.

임춘수가 오늘 있었던 일을 알게 된다면? 하나뿐인 아들이 개망신을 당했다는 말에 어떤 반응을 보일까?

‘일이 좀 꼬일 수도 있겠는데.’

대한민국 하면 빼놓을 수 없는 것이 학연, 지연, 혈연이다.

20년간 한자리를 굳건히 자리를 지킨 상동 길드가 지역 유지라면 우리 길드는 신생아나 다름없는 수준.

상동 길드가 작정하고 덤비면 출생 신고서부터 찢어질 거다.

“혹시 상동 길드장, 성격 좋아요?”

“나야 모르지. 소문으로만 대충 들었어.”

“그것만이라도 알려 줘요.”

잠시 고민하던 임꺽정이 대답했다.

“오늘 임창수를 보니까 옛말이 하나 떠오르더라. 호부견자(虎父犬子).”

“훌륭한 아버지에 못난 아들이라면 어쨌든 좋은 뜻이잖아요. 말은 통하는 사람인가?”

“아니, 한자 그대로 해석해 봐.”

“……호랑이 아버지에 개 아들?”

“임창수 성격이 개새끼면 임춘수는 호랑이야. 성격이 아주 지랄 맞대.”

“…….”

“나이 먹고 성격 죽었다는 얘기도 있는데, 사람 성격이 그렇게 쉽게 바뀔까 싶다.”

이런 시발.

들으면 들을수록 왠지 등골이 서늘한 게, 꼭 무슨 일이 하나 터질 것 같은 느낌이다.

‘아씨, 내기하지 말 걸 그랬나.’

수십억을 받을 생각에 한껏 들뜬 것도 잠시. 이제는 큰일 보고 뒤 안 닦은 것처럼 찝찝하다.

나야 둘째치고 다른 길드원들이 피해를 입는 건 절대 사양인데.

“태경아, 너무 신경 쓰지 마라. 나도 혹시나 해서 말해 본 거니까.”

“이거 사고 친 거 아니겠죠?”

“괜찮아. 최 팀장도 재미있다고 내기 거들었잖아.”

“어, 맞네?”

“그렇지. 그리고 임창수 저놈 하는 짓 봐라. 내가 아버지였으면 반쯤 죽여 놨을걸. 쪽팔려서 어디에 말도 못 해.”

확실히 일리가 있군. 뭐 별일이야 있겠어?

그 얘길 들으니 한결 마음이 가벼워진다. 저절로 웃음이 나올 정도다.

“고마워요. 꺽정 아저씨, 아니 형님.”

“그럼 갑부 된 기념으로 소고기 사. 아니지, 나 말고 송 양이랑 먹어야지.”

“……아.”

가슴에 대못을 박는구나.

사람 두 번 죽이는 임꺽정의 말에 나는 눈물을 삼켰다.



* * *



“무슨 일로 왔나?”

목소리의 주인은 이색적인 외모의 사내였다.

오십 줄에 접어든 나이였으나 피부는 팽팽했고 철사처럼 뻗친 머리카락은 검었다. 부리부리한 눈매는 보는 것만으로도 오금을 저리게 했다.

‘무슨 놈의 눈빛이…….’

K은행의 지점장에게도 그건 예외는 아니었다. 이미 수차례 만난 적 있지만 자신은 일반인이었고 상대는 A급 헌터, 그것도 대격변을 온몸으로 겪은 산증인이 아닌가.

저절로 혀가 꼬이고 식은땀이 흘렀다.

“그게…….”

“아까운 시간 뺏으러 온 거면 그만 돌아가고. 아니면 이 자리에서 당장 얘기하게.”

내용은 날이 섰지만 말투는 제법 온화하다.

나이 먹고 성격 죽이려고 노력한다는 소문은 들었는데 아예 헛수고는 아닌 모양이었다.

‘에이, 시발.’

지점장은 눈을 딱 감고 질렀다.

“죄송합니다, 길드장님. 아드님 일로 찾아뵈었습니다.”

아드님. 그 세 글자에 상동 길드장 임춘수의 눈썹이 꿈틀거렸다.

“창수? 그 녀석이 왜?”

“일전에 아드님께서 은행 관련 업무를 이용하게 되면 꼭 알려 달라고 하셔서…….”

임춘수가 감 잡았다는 듯이 고개를 끄덕였다.

“이번엔 뭔가? 내 인감이라도 훔쳤나? 아니면 담보 대출?”

“상당한 금액을 한 번에 이체하셨습니다.”

“또 계집질이겠지. 뻔해. 액수가 어떻게 되나?”

“두 개의 계좌에 각기 40억씩. 합해서 80억입니다.”

“얼마?”

“80억…… 헙.”

지점장은 황급히 숨을 삼켰다. 임춘수의 등 뒤에 있는 유리창이 빠르게 얼어붙는 광경을 목격했기 때문이었다.

파스스.

밖은 늦여름인데 사무실을 지배한 것은 추위와 냉기다.

오들오들 떨고 있는 지점장에게 그가 손짓했다.

“더 할 말은?”

“과, 관련 자료를 가져왔습니다.”

지점장이 떨리는 손으로 책상 위에 서류 뭉치를 내려놨다.

“잘했어. 이만 나가 보게.”

“다, 다음에 뵙겠습니다.”

지점장이 도망치듯 방 안을 빠져나간 뒤 임춘수는 수화기를 들었다. 냉기 저항 기능이 있는 전화기는 아무 문제 없이 빠르게 신호를 발신했다.

뚜, 뚜, 달칵.

- 네. 길드장님. 1팀장 전화 받았습니다.

“그 자식 당장 잡아 와.”

- ……임창수 팀장 말씀이십니까?

“팀장은 무슨. 오늘부터 해고야. 그 새끼 당장 잡아 와!”

쾅! 수화기의 수명은 거기까지였다. 수백 조각으로 나뉜 얼음 파편이 책상 위를 덮었다.

“이런 한심한, 내 그리 일렀는데도…….”

서늘한 눈으로 난장판이 된 사무실을 노려보던 임춘수의 시선이 한곳에 멎었다. K은행의 지점장이 놓고 간 서류 뭉치.

저 안에 80억의 행방이 들어 있을 게 분명했다.

‘멍청한 놈. 이번에는 어느 년한테 홀랑 넘어간 거냐?’

한 장, 한 장 넘겨 가며 읽기를 십여 분.

임춘수가 마지막 장을 덮었을 때, 누군가 질질 끌려오는 소리와 함께 문이 활짝 열렸다.

“임창수 팀장. 여기 데려왔습니다.”

푸근한 인상의 중년인. 그리고 중년에게 꽉 붙잡힌 한 청년.

“아, 아버지!”

“내 자랑스러운 아들 왔구나.”

아들의 등장에 아버지가 손을 내밀었다.

물론 결코 용서의 의미는 아니었다.

파츠츠츠.

임춘수의 손아귀에서 냉기가 솟구친다. 기체에서 액체, 액체에서 고체로 변한 그것은 강철만큼 단단한 얼음 몽둥이로 변화를 끝마쳤다.

“물어볼 게 많지만 우선 맞자.”

“아버지!”

“닥쳐, 이 새끼야!”

임창수를 데려온 중년인, 상동 길드의 1팀장은 조용히 문을 닫았다. 앞으로 반나절 동안 이곳은 출입 금지다.
```

## Current accepted English baseline

```markdown
# Chapter 86

“Oh, thank you for your hard work.”

The government official in charge came rushing out to greet us.

Well, more accurately, he came to greet Im Changsoo.

After meticulously checking all the byproducts and Magic Gems we had brought, he made a fuss.

“Wow, that’s an incredible amount. There can’t be many Minotaurs left in the labyrinth after this.”

“…”

Im Changsoo’s face was pale. He only nodded without answering, making the official glance around uneasily.

“Team Leader, are you feeling unwell?”

Since when did government officials start worrying about Hunters’ health?

Before he could say anything unnecessary, I jabbed Im Changsoo in the ribs.

“You have to answer him. Chang. Soo.”

“Um… No, I’m fine.”

“Ah, that’s a relief, then.”

Maybe he had sensed the strange atmosphere. The official looked at me suspiciously, but that was as far as it went.

“How would you like to handle the byproducts? As you know, there are two methods.”

As the official explained, there were two ways to sell byproducts.

Personal sales and consignment sales. With the former, the individual owner of the goods handled the transaction personally. With the latter, the goods were entrusted to the Administration, meaning a government agency, for sale.

*Each method has its pros and cons.*

Rare items sold better privately. For everything else, handing it over to a government agency was less of a hassle. It was like the difference between a luxury auction and a market auction.

“What should we do?”

At Im Changsoo’s question, Butler Kim stepped forward. He hadn’t once taken the lead during this Gate raid, but he was still a veteran Hunter. When it came to this sort of thing, he probably knew more than anyone else here.

“We’ll sell them to the Administration.”

They said there was nothing to waste from a cow. The same went for Minotaurs.

Their hides were used to make Equipment, their bones were boiled down into restorative food, and their horns were popular collector’s items among enthusiasts.

“You made the right choice.”

The government official began calculating the byproducts with an expression of pure delight. The Administration was the one buying them, so the reason he was happy was obvious.

*He must be getting a little something off the top.*

Still, whatever the official skimmed off wasn’t my concern.

The cut I was getting today was much bigger.

Tap, tap.

“What about the agreed-upon amount?”

Im Changsoo answered with a rigid expression.

“I-I’ll pay it.”

“By when?”

“I’ll send it by tomorrow.”

Four billion won by tomorrow? The son of a rich family certainly knew how to be decisive. I smiled broadly and handed him a slip of paper.

“Well, that works for me. Here’s my account number. Keep it safe as if it were an heirloom, then send the money tomorrow. It won’t be funny if you say you lost it later. Got it?”

“…Yes, sir.”

That should be enough, right? I said goodbye by giving Im Changsoo a light pat on the back.

As I watched with satisfaction as he staggered away, Im Kkeokjeong asked me,

“Do you think that punk will actually pay?”

“What happens if he doesn’t?”

“You know… it could get a little awkward. Sangdong Guild is a mid-tier Guild with some serious influence around here. If he decides to brazen it out and refuses to pay…”

“Come on, we have video evidence. Surely he wouldn’t.”

“Evidence can be destroyed. More importantly, I’ve heard a few things.”

“Like what?”

Now that he had put it that way, I was starting to get a little worried.

Kkeokjeong glanced around, checking everyone’s reactions, then leaned in and whispered,

“You know who the Sangdong Guild Master is, right?”

“Yes. I heard his name for the first time today, though.”

Im Chunsoo. For some reason, the name brought to mind a middle-aged man with a bulging drinker’s belly, but reality was the exact opposite.

“He’s an A-rank Hunter who made an impressive name for himself during the Great Cataclysm. What do people call him again? Fro… Fro… It’s suddenly slipping my mind.”

“Frozen.”

“Ah, right. Frozen. A mage specializing in ice magic.”

Famous Hunters were often given nicknames to match their abilities.

The same was true of Im Chunsoo. An A-rank Hunter, he had made a name for himself as a mage during the Great Cataclysm. He was particularly skilled with ice-related magic, which had earned him the nickname Frozen.

“When it comes to ice magic, that man is one of the top five in Korea. He used that Fame to build Sangdong Guild into what it is today.”

When the brutal Great Cataclysm finally came to an end, the first-generation Hunters faced a choice.

Retire, or remain active.

Im Chunsoo chose the latter and founded Sangdong Guild.

“That’s impressive. His son doesn’t seem like much.”

Even among A-rank Hunters, it was rare for someone to survive the Great Cataclysm with nothing but their bare fists and gain both wealth and fame. Im Chunsoo’s present was the future many Hunters dreamed of.

“Impressive? It certainly is—the power of bloodlines, that is.”

Kkeokjeong jerked his chin toward Im Changsoo’s retreating back.

“Don’t forget whose blood that punk inherited.”

“What does that…”

“I’m not bragging, but I’ve been in this business for over twenty years. Sangdong Guild was founded when I was still a complete rookie.”

“And?”

“Bucheon was just as fiercely competitive between Guilds back then as it is now. There was no room for a new Guild to squeeze in.”

“But Im Chunsoo broke through anyway?”

“That’s right. That’s why he’s a frightening man.”

“Hmm.”

Did that really mean so much?

Competition between Guilds was nothing new, and in a merit-based society, it was only natural for the capable to survive.

“A man like him would have had excellent abilities as a Hunter and plenty of Fame. He must have had powerful connections, too.”

“Do you think the other Guild Masters didn’t?”

“What?”

“They might have had slightly less Fame than Im Chunsoo, but every one of them had been a war hero. They had entered the market several years before Sangdong Guild and occupied a substantial number of Gates.”

Kkeokjeong continued in a low voice.

“It was a time when all kinds of illegal activity ran rampant because the system hadn’t been fully established yet. The only reason Sangdong Guild exists today is that Im Chunsoo crushed every one of his competitors. He’s no pushover.”

A thought suddenly flashed through my mind.

What would happen if Im Chunsoo found out about what had happened today? How would he react to hearing that his only son had been utterly humiliated?

*This could get complicated.*

When you talked about Korea, you couldn’t leave out connections through school, region, and blood.

Sangdong Guild had held its ground for twenty years. If it was a local power, our Guild was practically a newborn.

If Sangdong Guild came at us in earnest, they’d tear up our birth certificate before we even got started.

“Is the Sangdong Guild Master a nice person, at least?”

“I wouldn’t know. I’ve only heard rumors.”

“Tell me what you’ve heard.”

After thinking for a moment, Kkeokjeong answered,

“Seeing Im Changsoo today reminded me of an old saying. A tiger father and a dog son.”

“A great father and a worthless son? That’s still a compliment, isn’t it? Is he the kind of person you can reason with?”

“No. Try interpreting it literally.”

“…A tiger for a father and a dog for a son?”

“If Changsoo’s personality is that of a son of a bitch, then Im Chunsoo is a tiger. I hear his temper is absolutely fucking terrible.”

“…”

“I’ve also heard that he mellowed out with age, but can a person’s temper really change that easily?”

*For fuck’s sake.*

The more I heard, the colder my spine felt. I had the distinct feeling that something was about to go horribly wrong.

*Damn it. I shouldn’t have made that bet.*

My excitement at the thought of receiving several billion won had lasted only a moment. Now I felt uneasy, like I had taken a huge dump and forgotten to wipe.

I didn’t care what happened to me, but I absolutely refused to let the other Guild members get hurt.

“Taekyung, don’t worry about it too much. I only brought it up just in case.”

“I didn’t just cause trouble, did I?”

“It’ll be fine. Team Leader Choi thought it would be fun and joined the bet, too.”

“Oh, right.”

“Exactly. And look at the way Im Changsoo acted. If I were his father, I would’ve beaten him half to death. He’d be too embarrassed to tell anyone about it.”

He had a point. What could possibly happen?

Hearing that made me feel considerably lighter. I even found myself smiling.

“Thanks, Kkeokjeong ajusshi. No, hyungnim.”

“Then buy us some beef to celebrate becoming a rich man. Wait, no. You should eat it with Miss Song, not me.”

“…Ah.”

He was driving a nail straight through my heart.

As Im Kkeokjeong killed me with words for the second time, I swallowed my tears.

* * *

“What brings you here?”

The speaker was a man with a distinctive appearance.

He was nearing fifty, but his skin was taut and his wiry, spiky hair was black. His large, piercing eyes were enough to make anyone’s knees go weak.

*What the hell is with that look in his eyes…*

The manager of a K Bank branch was no exception. He had already met the man several times, but he was an ordinary person, while the other man was an A-rank Hunter—a living witness who had endured the Great Cataclysm with his entire body.

His tongue tied itself in knots, and cold sweat trickled down his back.

“Well…”

“If you came to waste my valuable time, go back. Otherwise, speak now.”

The words were sharp, but his tone was fairly gentle.

The manager had heard the rumor that Im Chunsoo was trying to mellow his temper with age. Apparently, it hadn’t been a complete waste of effort.

*Damn it.*

The branch manager steeled himself and blurted out,

“I’m sorry, Guild Master. I’ve come regarding your son.”

At the mention of his son, Sangdong Guild Master Im Chunsoo’s eyebrow twitched.

“Changsoo? What about him?”

“Some time ago, you asked me to let you know whenever your son used any of the bank’s services…”

Im Chunsoo nodded as if he understood.

“What is it this time? Did he steal my seal? Or take out a loan against collateral?”

“He transferred a considerable amount of money all at once.”

“He must be fooling around with women again. Obviously. How much?”

“Four billion won to each of two accounts. Eight billion won in total.”

“How much?”

“Eight billion… Hup.”

The branch manager hurriedly swallowed his breath. He had just watched the window behind Im Chunsoo rapidly freeze over.

Hiss.

It was late summer outside, but the office was suddenly ruled by cold and frost.

Im Chunsoo gestured at the trembling branch manager.

“Anything else?”

“I-I brought the relevant documents.”

With shaking hands, the branch manager placed a stack of papers on the desk.

“Good. You may leave.”

“I-I’ll see you next time.”

After the branch manager fled the room, Im Chunsoo picked up the receiver. The phone had a cold-resistance function, so it transmitted the signal without any problems.

Beep, beep. Click.

—Yes, Guild Master. Team One’s Leader speaking.

“Bring that bastard here immediately.”

—…Do you mean Team Leader Im Changsoo?

“Team Leader, my ass. He’s fired as of today. Bring that bastard here now!”

Bang!

The receiver’s life ended there. Ice shattered into hundreds of pieces and covered the desk.

“What a pathetic fool. Even after I warned him…”

Im Chunsoo glared coldly at the wrecked office, then his gaze stopped on one spot: the stack of papers left behind by the K Bank branch manager.

There was no doubt that the documents contained the whereabouts of eight billion won.

*You stupid bastard. Which woman did you fall for this time?*

He read through the papers, turning them one page at a time, for more than ten minutes.

When Im Chunsoo closed the final page, the door flew open with the sound of someone being dragged along.

“Team Leader Im Changsoo. I brought him here.”

An affable-looking middle-aged man stood there. In his firm grip was a young man.

“F-Father!”

“My proud son has arrived.”

At his son’s appearance, the father extended a hand.

Of course, it was not meant as a gesture of forgiveness.

Crackle, crackle, crackle.

Cold surged from Im Chunsoo’s grasp. It changed from gas to liquid, then from liquid to solid, completing its transformation into an ice club as hard as steel.

“I have a lot to ask you, but first, you’re getting hit.”

“Father!”

“Shut up, you little shit!”

The middle-aged man who had brought Im Changsoo there—the Team Leader of Sangdong Guild’s Team One—quietly closed the door.

For the next half a day, no one was allowed to enter.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 86`.

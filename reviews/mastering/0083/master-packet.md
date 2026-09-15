# Master Edit Task — Chapter 83

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
| 최민우    | **Choi Minwoo**   |
| 송송이    | **Song Song**     |
| 임창수    | **Im Changsoo**   |
| 생도     | **cadet**                                    |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 귀가      | **your family**                                                 |
| 임꺽정 | **Im Kkeokjeong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

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

# Chapters 75–79

## Plot

Taekyung logs out after roughly twenty days in Murim, finding that only 2:05:35 has passed in the modern world. He reunites with Seong Jinho, signs a contract to join Team Leader Choi’s new Peace Guild, and learns that the deal includes a 500 million won signing bonus, a 50 million won monthly salary, a seventy-percent settlement share, housing, and other benefits. The Guild house is Sooni’s Super, a dilapidated corner store in Bucheon.

Taekyung meets the Guild’s other members: Im Kkeokjeong, Song Song, and Butler Kim. He immediately develops feelings for Song Song and awkwardly attempts to confess during the Guild’s first gathering, but Team Leader Choi repeatedly interrupts him by turning the occasion into a membership celebration. The gathering ends with Song Song drunk and the others revealing their backgrounds: Choi formerly led a team in the Ares Guild, Song Song served on that team, and Butler Kim is a retired mage and former Hunter. Choi establishes Butler Kim as Guild Master and himself as Team Leader.

The next morning, the hungover members learn that the Peace Guild must begin working. Choi presents footage of the Bucheon Terminal Guild’s raid against seven B-rank Minotaurs in The Minotaur’s Labyrinth. Although the monsters were defeated, two C-rank Hunters died. Taekyung uses Qi Sense to assess the Peace Guild’s members—Choi Minwoo at Level 75, Kim Hwajong at Level 80, Song Song at Level 64, and Im Hyeokjun at Level 24—and concludes that their first raid will be dangerous.

## Continuity

- Taekyung is a Peace Guild member and has completed the Guild Membership achievement, receiving 10 points.
- His Peace Guild contract provides a 500 million won signing bonus, a fixed monthly salary of 50 million won, a seventy-percent settlement share, housing, a car, and other benefits.
- The Peace Guild has five members: Guild Master Butler Kim, Team Leader Choi, Taekyung, Im Kkeokjeong, and Song Song. Choi leads Team 1; Taekyung, Im, and Song Song are its members.
- Sooni’s Super is the Guild house, located in a dilapidated, Gate-dense district of Bucheon. The property cost slightly more than 2 billion won per pyeong.
- Im Kkeokjeong joined after Choi recruited him while he was hospitalized. He is married and has two children.
- Song Song previously worked under Choi in the Ares Guild. Taekyung is attracted to her, but his interrupted confession leaves her response unclear.
- Butler Kim is a retired mage and former Hunter. He and Taekyung trained at Nonsan’s 28th Regiment, 1st Battalion, but Kim’s former rank and wider background remain unknown.
- The Peace Guild is preparing for its first raid. The Bucheon Terminal Guild’s recent raid against seven B-rank Minotaurs killed two C-rank Hunters despite defeating all the monsters, establishing the danger of the upcoming operation.
- The members’ displayed Levels are Choi Minwoo 75, Kim Hwajong 80, Song Song 64, and Im Hyeokjun 24.
- Essence of the Himalayas temporarily increases Taekyung’s Intelligence by 1 for one hour.
- In Murim, Taekyung, Jin Mukyung, and Hyuk Mujin are traveling to Eung-hyeon to visit the Mount Heng Sword Sect. The forced [Yesterday’s Enemy, Today’s Ally] Quest—to deliver Jin Wikyung’s New Year’s Day invitation—remains unresolved.
- The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed. The possible connection to Song Sword Sect is also unresolved.
- Jin Wikyung still plans to summon Shanxi’s sects on New Year’s Day and may seek the Alliance Leader position. Whether the sects will respond remains unknown.

## Translation Decisions

- Retain **Peace Guild**, **Ares Guild**, **Guild Master**, **Team Leader Choi**, **Butler Kim**, **Song Song**, **Miss Song**, **Im Kkeokjeong**, and **Sooni’s Super**.
- Use **Minotaur**, **Bucheon Terminal Guild**, and **The Minotaur’s Labyrinth**.
- Retain **Qi Sense**, **Essence of the Himalayas**, **Sleep Mode**, **Return**, **Returnee**, **New Year’s Day**, **Alliance Leader**, and **Quest**.
- Use **mage** for 마법사, **Senior** for Taekyung’s deferential address to Butler Kim, and **haejangguk** and **makgeolli** with concise cultural footnotes.
- Retain **pyeong**, with a footnote explaining that it is approximately 3.3 square meters.

### Prior accepted reading-copy tails

#### Chapter 81 tail (verified mastered)

…
with my tongue, but I nodded anyway. *We’ll probably only see each other once, anyway.* He had helped us with the issue concerning Im Kkeokjeong, so I still felt a little grateful to him. “Did you need something?” “Haha, it’s nothing I’d call business. This is fate, so I thought we could at least exchange names. You heard my introduction earlier, so you already know who I am. I look forward to working with you.” Someone once said you couldn’t spit in a smiling face. It was a little awkward, but I clasped the hand Im Changsoo offered with a broad smile on his face. “Ah, yes. I look forward to working with you too.” A Team Leader from another Guild—someone I had never even met before—had offered me a handshake first. I had participated in cooperative raids several times over the past seven years and had plenty of experience as a day-labor Hunter, but this was the first time something like this had happened. *Then again, I was an F-rank back then.* In those days, people had treated me like air. Maybe being a C-rank Hunter meant I was finally being treated like a person. It left me with a strange feeling. *But why me?* The question was answered almost immediately. “That’s a Black Drake Leather Set, right?” “Ah.” *This guy’s a Designer-Brand Junkie too.* Im Changsoo looked my equipment up and down, exclaiming in admiration. “Wow, I’ve only ever seen this in pictures. Where did you buy it? Did you order it from overseas? Or get it in Cheongdam-dong?” “I rented it.” “You leased it from a company, then. I heard you’re a C-rank Hunter, but can you really afford to maintain something like this? Ah, I’m sorry. I absolutely didn’t mean anything by that. Did I offend you?” *Of course I’m offended, you moron.* But I wasn’t stupid enough to let my true feelings show so openly. What Im Changsoo had said was also a cold reality. *Still, this guy really has no tact.* I waved a hand with deliberate composure, mixing in a little self-deprecating humor. “It’s already breaking my back. Every penny I earn goes toward maintenance. The people around me call me crazy.” “Haha, but is there anything more important than your life? Right?” “That’s true.” “Then I suppose the same goes for the others.” “Sorry?” “The others. The Peace Guild members. Their equipment looked pretty good too.” “Did it? I don’t know much about that sort of thing.” Im Changsoo laughed as if he had heard an amusing joke. “Come on. That’s not something a person who spends a fortune leasing equipment gets to say.” The equipment was leased, but it hadn’t cost me a fortune. Team Leader Choi had loaned it to me free of charge. I briefly considered explaining that, but soon abandoned the thought. *What would be the point?* Explaining it would only waste my breath. I was already tired of talking about equipment, so I gave him a vague answer. “They’re all about the same as me.” “I see.” At that moment, one of Im Changsoo’s team members ran over and told him that preparations were complete. “Oh, dear. We’ve been chatting for too long. I’d better go. I need to check on my team members one last time, and then we should all move together.” “Take care.” “Yes.” Im Changsoo bowed politely and was about to leave when he suddenly asked, “Oh, right. There’s something I’ve been meaning to ask you.” “……?” “Have we met somewhere before?” I would have been overjoyed if Miss Song had asked me that, but hearing it from a male in heavy armor left me feeling less than pleased. “This is our first meeting.” “Really?” “Yes.” I only thought his name sounded familiar. This was definitely our first meeting. At my firm answer, Im Changsoo’s smile deepened. “All right, then. I’ll be going.” What was that? Something about his final smile rubbed me the wrong way. As I watched him walk away, Team Leader Choi approached without my noticing and asked, “Do you know him?” “No. He just said he wanted to be friends.” “He didn’t make a recruitment offer?” “Not at all. I think he only came over because he’s a gear nerd. He walked up out of nowhere and asked where I bought my equipment.” “I bought it in Cheongdam-dong.” “……” *I wasn’t asking.* * * * “Changsoo hyung, why did you suddenly go talk to that bastard?” “No reason. His equipment looked decent, so I sounded him out.” “Holy crap, it really does. Is that stuff really his?” “Use your brain, asshole. How could a C-rank wear something like that?” “Then he leased it? Crazy bastard. The maintenance costs must be insane.” “Leave him alone. It’s cute, watching him overextend himself trying to make something of himself.” Im Changsoo let out a quiet laugh. *As expected, they were nothing special.* Admittedly, he had felt a little uneasy when they showed up out of nowhere decked out in expensive equipment. If he messed with the wrong people, things could get out of hand. But now that he had them figured out, he felt at ease. *Song Song.* Money and ability. With only those two things, he believed he could do anything. Getting his hands on one woman would be no trouble at all. “Let’s get moving. Pass it on.” “Yes, sir!”

#### Chapter 82 tail (verified mastered)

…
> **System** > > **Level 58 Minotaur Warrior** “—Moooooo!” They looked far more vivid and imposing in person than they had in the video, but… “That’s all?” “There’s only one?” There really was just one. *Could that Minotaur have gotten lost in the labyrinth, too?* “At that level, we should be able to handle it without ranged support, shouldn’t we?” “Hye-rin, I’ll be right back.” The Sangdong Guild members confidently stepped forward. Two tanks and two damage dealers, all of them B-rank Hunters. Their intention to show off in front of the women was painfully obvious. *Oh, you morons.* Guys like that always fooled around and ended up dead. Of course, that probably wouldn’t happen because of a single Minotaur. “If you’re going to do it, finish it quickly.” With Im Changsoo’s permission, the four men drew their weapons and started toward the monster. That was when— *Boom. Boom.* “Hm?” “—Moo.” A Minotaur popped out of the second of the five holes. “Oh, now there are two.” “That one’s a little smaller. It looks weaker, so you take it.” “What the hell are you saying? Says the weakest bastard here.” *Boom. Boom.* “—Moo.” The third hole. “Oh, three. At this rate, this might actually be a pretty fun fight.” “Anyone who gets so much as a scratch buys drinks tonight. How about it?” “I’m in.” “I’m in. The guy who suggests these things always ends up paying.” *Boom. Boom.* “—Moo.” “Ah, shit. What is this?” “Four might be a bit much.” “We should probably form up and take them out one at a time.” “Agreed.” Team Leader Choi, who had been watching the situation, scratched his neck. “Maybe we should wait a little longer before coming up with a strategy.” “Huh?” “The holes. Don’t you get the feeling more might come out?” “No way. It’s not like they’re introducing Olympic athletes.” *Boom-boom-boom-boom!* *He was right.* Lane five—no, the fifth hole—had news for us, too. The only unexpected part was that this time, it wasn’t alone. “—Moooooo!” Maybe it had a lot of friends. Four Minotaurs came stampeding out together. Including the ones that had already appeared, there were eight in total. Four B-rank Hunters had no chance against that many. Team Leader Choi spoke. “What do you think?” “It might be difficult.” *Difficult, my ass. If you don’t want to die, stay behind the tank.* I had toned it down for the benefit of the ears around us. “What about you, Mr. Taekyung?” “Me?” “Yes. You, Mr. Taekyung.” “Hmm.” Minotaurs were B-rank monsters, and their Levels were in the mid-to-late fifties. For a martial artist, that would be close to Top-tier. But if I fought them, I would have to account for all sorts of variables. Simply put, I would have to fight them to know. “I’m not sure.” “You’re not sure… Do you know something?” Team Leader Choi stared at me with a strange look in his eyes. “Most C-rank Hunters don’t answer like that. They wouldn’t take time to think about a question like that, much less take it seriously.” I felt a sudden twinge of unease. I had no reason to hide my strength, but I also had no desire to brag about it to the whole neighborhood. For now, I wanted to avoid attention and keep it as my own secret. A Hunter who was just a little more capable than everyone else. That was all. “I’ve known this for a while, but you really are an interesting person, Jin Taekyung.” “No, wait, Team Leader. I think there may be some misunderstanding here.” I had just begun to speak when— “Haha, I see. Listening to you, even I’m getting interested.” Im Changsoo suddenly cut in, his gaze sweeping over Team Leader Choi and me. “You were having such an interesting conversation that I couldn’t help overhearing some of it. You don’t mind, do you?” *Was it my imagination, or did that sound like “If you do mind, what are you going to do about it?”* “For a C-rank with fuck-all to his name, you sure had a lot to say about Minotaurs and whatnot. You were practically writing a novel.” *Ah. So I wasn’t imagining it.* I looked at Im Changsoo with fresh eyes. *It suits him.* Everyone had clothes that suited them. The same went for smiles and attitudes. That was how Im Changsoo looked to me now. The mockery gathered in the raised corners of his mouth suited him perfectly. It was practically made for him. “I didn’t mean to offend you.” At Team Leader Choi’s characteristically impassive expression and tone, Im Changsoo let out a short laugh. “Why would I be offended? It’s the truth. These guys are fucking lousy. They only look impressive because people keep calling them B-rank. Among B-ranks, they’re complete bottom-of-the-barrel trash. But…” Im Changsoo jerked his chin toward me. “They’re still better than a C-rank. Isn’t that right, Mr. Jang Taekyung?” I finally said what I had been holding back all this time. “It’s Jin Taekyung.” “Whether you’re Jin Taekyung or Jang Taekyung, I don’t care what your surname is.” “Then should I call you Shit Changsoo?” “What?” “Im Changsoo or Shit Changsoo. I don’t care what your surname is either.” The smile disappeared from Im Changsoo’s face. [^1]: The tongue-pulling hell is a Buddhist hell where liars and slanderers are punished by having their tongues pulled out.

## Korean source

```text
＃83화



임창수의 신경은 아까부터 온통 송송이를 향해 있었다.

‘젠장, 비싸게 굴기는.’

일부러 자꾸 근처를 맴돌고 지나가듯 말도 몇 번 붙여 봤지만 송송이의 반응은 무미건조했다. 아, 네. 감사합니다. 알겠어요.

자신이 거둔 소득치고는 너무 초라하다.

‘까다로운 년.’

여자가 남자를 볼 때 대부분 어릴 때는 얼굴, 나이 먹으면 몸과 능력을 본다고 했다. 이 세 가지를 모두 갖고 있는 임창수는 작업에 실패해 본 적이 없다.

가벼운 그의 인간관계에 환멸을 느낀 여자가 먼저 떠나거나, 그전에 그가 질려서 차 버린 일은 있었어도 지금 같은 무관심은 처음이다.

‘지 잘난 건 알아 가지고.’

짜증이 나다가도 송송이의 매끈한 몸매와 몽환적인 얼굴을 보면 화가 스르륵 풀렸다. 다른 여자들의 화장품 냄새와는 차원이 다른 향긋한 체취도 한몫했다.

‘조급해하지 말자. 어차피 넘어오게 되어 있어.’

아직 시간은 많다. 미노타우로스의 미로는 말 그대로 미로. 레이드 타임이 다른 게이트와 비교해 두 배까지도 늘어날 수 있다. 그 정도면 여자 하나 꼬시기에는 충분한 시간이다.

다만 한 가지 문제가 있다면…….

‘한 놈이 자꾸 거슬리네.’

최민우라고 했나? 게이트 속이 아니라 화보 잡지 속에 있는 게 더 어울릴 것 같은 놈이다. 번드르르한 얼굴도, 길쭉한 팔다리도. 특유의 덤덤한 표정도 마음에 안 들었다.

‘나머지는 뭐, 병신들이고.’

허허 웃고만 있는 할배와 산적 같은 아저씨는 애초부터 제외니까.

그나마 장태경이라고 젊은 놈이 하나 더 있긴 한데 경쟁자 축에도 못 낀다.

‘왠지 모르게 기분 나쁜 놈이지만.’

흔해 빠진 C급 헌터. 대형 길드 소속도 아니고, 주제에 안 맞는 고급 장비를 리스 해서 연명하는 하루살이에 불과한데 태도나 말투는 묘하게 당당하다.

조금 전 대화의 마지막에서는 자신을 향한 귀찮음마저 느껴질 정도였다.

‘가오는 살린다 이건가?’

장태경, 최민우. 거슬리는 두 놈이 붙어 있으니 임창수의 눈과 귀가 그쪽에서 떨어지지 않았던 것도 당연했다.

- 음모오오오!

미노타우로스가 줄줄이 등장하기 시작했을 때였다.

“어떻게 생각하십니까?”

“아마 힘들지 않을까요.”

이 자식들 봐라?

안 그래도 막 부하들을 물리려던 임창수가 입을 다물며 귀를 기울였다.

“태경 씨라면 어떻겠습니까?”

“저 말입니까?”

여기까지만 들어도 이미 기가 차는데, 더 가관인 것은 잠시 후 들려온 대답이었다.

“잘 모르겠네요.”

C급 헌터가 미노타우로스 여덟 마리를 상대로, 뭐? 잘 몰라?

일대일로 붙어도 1분 안에 시체가 될 놈이 입만 살았다.

‘미친놈들. 아주 소설을 써라.’

피식, 웃음을 흘리던 임창수가 순간 멈칫했다.

마음에 안 드는 두 놈을 송송이 앞에서 개망신 줄 수 있는 기회라는 생각이 뇌리를 스쳤기 때문이었다.

두 사람의 사이로 불쑥 끼어든 것도 그런 이유에서였다.

“워낙 재미있는 얘기들을 하고 계셔서 좀 들었습니다. 괜찮으시죠?”

사과도 받고, 비웃어 주고. 이참에 누가 더 우위에 있는지 확실히 각인시켜 줄 생각이었다.

그런데…….

“그럼 씹창수라고 불러 드려요?”

“뭐?”

“임창수든 씹창수든. 그쪽 성이 뭐든 내 알 바 아니잖아요.”

씹창수.

난생처음 들어 보는 폭언에 임창수의 뇌가 정지했다.



* * *



사방이 침묵에 잠겼다. 상동 길드, 평화 길드. 심지어는 미노타우로스들까지 울음소리를 멈춘 듯했다.

그 숨 막히는 정적 속에서, 굳게 닫혀 있던 놈의 입이 열렸다.

“……야, 이 새끼야.”

사실 이쯤 되면 존댓말을 쓰는 것도 우습다.

나도 시원시원하게 대답해 주었다.

“뭐, 이 새끼야.”

“너 진짜. 돌았냐?”

“원래 지구인들은 다 돌고 있어. 천동설도 모르냐? 이 무식한 새끼.”

그때 최 팀장이 끼어들었다.

“그건 지동설입니다. 천동설은 지구가 우주의 중심으로 고정되어 있어서 움직이지 않으며, 지구의 둘레를 달, 태양, 행성들이 각기 고유의 천구를 타고 공전한다고 하는 우주관…….”

텁.

은밀하게 다가온 임꺽정의 솥뚜껑만 한 손이 최 팀장의 입을 틀어막았다.

“읍. 이게 뭐 하는. 읍읍.”

“…….”

그냥 이대로 콱 죽어 버렸으면 좋겠다. 눈치가 없어도 정도가 있지. 상동 길드에서 돈이라도 받았나 의심될 정도다.

“내가 이런 놈들이랑 말을 섞다니.”

임창수가 어이없다는 듯한 얼굴로 나와 최 팀장을 바라봤다.

“너희같이 얼빠진 놈들이 어떻게 헌터가 된 거지?”

“그럼 뭐, 내신 등급 보고 뽑냐? 토익 900점 이상이면 B급이고 중국어까지 가능하면 A급이야?”

“그 입 닥치는 게 좋을 거다. 오래 살고 싶으면.”

“이야, 이제 협박까지? 무서워서 상동 길드 쪽으로 오줌도 못 싸겠어.”

으드득. 임창수의 두 눈에서 불꽃이 쏟아졌다.

“잊었나 본데…… 여긴 게이트야.”

“나도 알아, 인마. 저기 멀리에서 미노타우로스 여덟 마리가 우리 쪽으로 오는 중인 것도 알고.”

호랑이도 제 말 하면 온다더니.

딱 알맞은 타이밍에 황소의 울음소리가 울려 퍼진다.

- 모오오오!

“오, 온다!”

“어쩌지?”

“뭘 어떡해. 돌아가! 빨리!”

쿵. 쿵. 쿵.

미노타우로스 무리가 움직일 때마다 동굴 바닥이 진동한다.

꽁무니가 빠져라 도망쳐 오는 팀원들의 모습을 보며 임창수가 가래를 탁 뱉었다.

“너, 운 좋은 줄 알아라.”

“내가 좀 그런 편이지.”

시스템을 얻은 덕분에 제2의 인생을 살고 있다고 해도 과언이 아니다. 죽을 만한 고생도 했지만 운 하나는 기똥찬 편이지.

“저놈들을 처리한 후에 보자고.”

“그것도 괜찮고.”

“뱉은 말에 책임을 질 수 있는 놈이면 좋겠군.”

“책임질 수 있을걸.”

나는 놈의 머리 위에 둥둥 떠 있는 레벨 창을 바라봤다.



[Lv.65 임창수]



65레벨. 높다. 녀석의 다른 팀원들과 비교해도 10레벨 가까이 차이 나는 걸 보면 B급 헌터 중에서도 썩 괜찮은 실력일 것이다. 물론 나만큼은 아니겠지만.

‘뭐, 인성이랑 실력이 비례하는 건 아니지.’

헌터는 토익이나 내신 등급, 인성 적성 검사로 뽑히는 게 아니니까. 고개를 절레절레 흔들며 돌아선 그때였다.

“지금은 어때?”

“……?”

“미노타우로스. 혼자서도 자신 있다고 하지 않았나?”

아하. 무슨 말을 하려는 건지 대충 감이 잡힌다.

의도가 뻔히 보이는 말투와 표정에 피식 웃음이 새어 나왔다.

“글쎄, 그런 말을 한 기억은 없는데.”

“뱉은 말에 책임은 져야지.”

“유치해서 못 놀아 주겠네. 불만 있으면 레이드 끝나고 일대일로 해결해.”

평온한 얼굴로 상황을 지켜보던 김 집사와 송이 씨도 입을 열었다.

“두 분 모두 진정하는 게 좋겠군요.”

“저기요, 지금 이럴 때가 아닌 것 같은데.”

쿵쿵쿵.

이 순간에도 미노타우로스 무리는 시시각각 가까워지고 있었다. 놈들이 신중하게 접근해서 망정이지, 마음만 먹었다면 진작 전투가 벌어졌을 수도 있을 것이다.

“들었지? 괜한 사람들 피해 입히지 말고 나중에…….”

“다섯 장.”

“응?”

임창수가 손가락 다섯 개를 쫙 폈다.

저건 별이 다섯 개……가 아니고 다섯 장이라니. 설마?

“내가 생각하는 그건가?”

“저 미노타우로스 무리. 혼자 처리하면 마리당 큰 거 다섯 장씩 주지.”

“큰 거?”

“그래, 큰 거.”

한 마리당 5천만 원이니까 여덟 마리면 4억이다.

C급 헌터가 된 지금의 내게도 상당한 거금.

‘하지만…….’

모두가 보는 앞에서, 특히 송이 씨가 보는 앞에서 돈에 약한 모습을 보이기는 싫다. 이건 자존심 문제다!

‘송이 씨. 제 마음이 들리시나요.’

그윽한 눈길로 그녀를 바라본 내가 대답했다.

“거절한다.”

임창수의 눈썹이 꿈틀거린다.

“부산물에 대한 일체의 권한까지 준다고 해도?”

“싫어.”

“마정석이 나올 수도 있을 텐데.”

“안 돼.”

청소년 법원 판사처럼 단호한 내 대답에 임창수가 입술을 깨물었다.

“쓸데없이 자존심만 강한 놈이군. 40억에 부산물 권한까지 주겠다는데 그걸 거절하다니.”

“돌아가…… 잠깐. 지금 뭐라고?”

내 귀가 잘못됐나?

몇 초간 오만 가지 생각이 들었다. 머릿속을 정리한 뒤에야 간신히 입술을 뗄 수 있었다.

“얼마? 40억?”

“말하지 않았나? 큰 거 다섯 장이라고.”

“…….”

“그럼…… 한 마리당 5억?”

존나 큰 다섯 장이라고 했어야지.

세상에, 40억이라니. 상상을 초월하는 액수에 나는 물론이고 송이 씨와 임꺽정까지 입을 딱 벌렸다.

‘이 자식은 뭐 이렇게 통이 커?’

중견 길드의 팀장인 데다 B급 헌터니까 잘 벌기야 할 테지만 지금처럼 수십억을 툭 제시하는 건 말이 안 된다.

“그걸 그냥 준다고? 40억을?”

“그냥? 그건 곤란하지. 이건 내기야.”

“무슨 내기?”

“나도 얻는 게 있어야지.”

임창수의 입꼬리가 비틀렸다.

“네가 죽거나 도망칠 경우 지금까지의 보상은 무효다. 거기에 더해서…….”

놈의 고개가 스르륵 움직였다. 그 시선이 멈춘 곳에는 한 사람이 있었다.

“저요?”

“예, 송송이 씨를 저희 길드로 모시고 싶습니다.”

임창수가 예의 바르게 고개를 숙였다. 지금까지의 모습과는 너무 달라 소름 돋을 정도의 태세 전환이다.

“어우, 소름 돋아. 그냥 하던 대로 해요. 가식 떠는 것보다는 그게 훨씬 나아 보이니까.”

“…….”

“…….”

송이 씨, 솔직한 성격이구나.

진짜 소름이 돋았는지 몸을 부르르 떤 그녀가 팔짱을 꼈다.

“씹창, 아니 임창수 씨라고 했죠.”

“……네.”

“음. 단도직입적으로 말할게요. 그쪽, 내 취향 아니에요.”

시속 160km. 몸 쪽 꽉 찬 돌직구에 임창수의 눈빛이 흔들렸다.

“예?”

“키 크고 잘생겼는데 딱 바람 잘 피울 것 같아요. 제가 바람을 싫어하거든요. 간만에 머리 잘됐는데 헝클어지면…… 아, 이게 아닌가?”

“예, 예?”

“아무튼 내 타입 아니에요. 바람둥이에 너무 돈 자랑하는 사람은 딱 질색.”

처음 봤다. 임창수의 벙찐 모습.

아마 다른 사람이 보면 지금 나도 같은 표정이지 않을까.

“어, 방금 그 모습은 좀 괜찮네. 그런데 아까부터 쭉 지켜보니까 평소 인성이 좀, 그쪽 스스로도 느끼죠?”

가까스로 표정을 수습한 임창수가 대답했다.

“그거야 하나씩 맞춰 가면 되죠.”

“에이, 똥인지 된장인지 찍어 먹어 봐야 아나요. 그쪽은 나랑 배꼽 맞추는 것밖에 관심 없어 보이는데. 맞죠?”

“……!”

“……!”

나를 포함한 모두가 입을 딱 벌렸다. 수줍은 듯이 머리를 매만지며 한마디씩 하는데, 한 방 한 방이 거의 핵폭탄 급이다.

“그렇다고 뭐, 딱히 상동 길드가 싫은 건 아니에요.”

쉴 새 없이 두드려 맞던 임창수가 반색하며 물었다.

“정말입니까?”

“네. 어차피 다시 옮기면 되니까.”

“…….”

송이 씨, 천잰데?

해맑은 얼굴로 빅 엿을 먹인 송이 씨가 말을 이었다.

“그런데 일단 길드를 옮기려면 양해를 구해야 돼서요. 그렇죠, 길드장님?”

“아, 물론이죠.”

흥미로운 눈빛으로 구경하고 있던 김 집사의 대답에 송이 씨가 고개를 돌렸다.

“팀장님은 어떻게 생각하세요?”

“뭘 말입니까? 송이 씨가 길드를 옮기는 것?”

“이 내기에 졌을 경우에는 그렇게 되겠죠.”

최 팀장이 덤덤하게 고개를 끄덕였다.

“그러시죠.”

“……너무 쉽게 대답하는 것 아니에요?”

“쉬운 질문이라 쉽게 대답한 겁니다.”

순간 송이 씨의 눈빛에 서운함이 묻어 있다고 생각한 건 나만의 착각일까?

‘에이, 아니겠지.’

다시 보기에는 너무 빨리 스쳐 간 감정이었다. 시원 털털한 모습으로 돌아온 송이 씨가 이번엔 임창수에게 말했다.

“그럼 전 내기 찬성. 태경 씨는?”

“저는…….”

고민은 짧지 않았다. 처음 최 팀장의 질문을 들었을 때부터, 이미 마음 깊은 곳에서는 묘한 확신이 자리 잡았으니까.

내가 놈들보다 더 강하다는 확신이.

“내기에 응하겠습니다.”

최 팀장의 입가에 웃음이 번졌다.

“저도 참가하죠. 내기는 판이 커야 재밌지 않겠습니까.”

“이야, 아주 도박사 나셨구만. 그래서 얼마?”

“40억. 물론 진태경 씨가 여덟 마리 모두 쓰러트린다에 걸겠습니다.”

“뭐?”

잠시 최 팀장을 노려보던 임창수가 픽 웃었다.

“재밌는 놈들이네. 한 놈은 죽고 싶어서 난리고, 다른 한 놈은 돈 버리고 싶어서 안달 났고.”

“그래서 대답은?”

“당연히 예스지.”

“계약서라도 쓸까요?”

“계약서? 사람을 뭘로 보고. 난 한 번 뱉은 말은 지킨다. 그쪽은…… 안 지켜도 좋아. 지키게 만들어 줄 테니까. 모두 뒤로 물러나!”

거대하고 축축한 동굴이 콜로세움으로 바뀌는 순간이었다.

엄청난 액수가 걸린 투기장. 나는 미노타우로스 무리와 싸워야 하는 검투사다.

“최 팀장님. 제가 지면 어쩌시려고요?”

“이길 겁니다.”

이 자신감의 근원이 어딜까? 자기 자신에 대한 믿음? 아니면 그동안 지켜본 내 모습?

상관없다. 난 최선을 다해 목적을 달성할 뿐이다.

쿵쿵쿵쿵쿵!

- 모오오오!

20m 앞. 놈들의 하나하나가 똑똑히 눈에 들어온다.

뜨거운 콧김, 열기, 근육과 치켜올린 무기.

‘소랑 싸우는 건 처음인데.’

재밌는 경험이 되겠군.

나는 창을 쥐었다. 투우사처럼 소 떼를 향해 달려들었다.
```

## Current accepted English baseline

```markdown
# Chapter 83

Im Changsoo’s attention had been fixed entirely on Song Song for some time.

*Damn, she sure knows how to play hard to get.*

He had deliberately kept circling near her and tried striking up conversations in passing several times, but Song Song’s responses had been utterly matter-of-fact.

“Oh, okay.”

“Thank you.”

“I understand.”

For all his effort, the results were pathetic.

*What a difficult bitch.*

They said that when women looked at men, they cared about their faces when they were young, but their bodies and abilities once they got older. Im Changsoo possessed all three, and he had never failed at picking up a woman.

There had been women who became disgusted with his shallow relationships and left first, or ones he had grown tired of and dumped before they could leave.

But he had never encountered indifference like this.

*She sure knows she’s hot shit.*

Even when he grew irritated, the anger slowly melted away whenever he looked at Song Song’s sleek figure and dreamlike face. Her fragrant natural scent, completely different from the smell of other women’s cosmetics, helped, too.

*Don’t get impatient. She’ll fall for me eventually.*

There was still plenty of time. The Minotaur’s Labyrinth was a labyrinth in the truest sense of the word. Raid times could stretch to twice as long as those of other Gates.

That was more than enough time to pick up one woman.

There was only one problem…

*One guy keeps getting on my nerves.*

Choi Minwoo, was it? He looked more suited to a fashion magazine than a Gate. His polished face, his long limbs—even his characteristically impassive expression irritated Im Changsoo.

*The rest are just fucking idiots.*

The old geezer who did nothing but chuckle and the bandit-like middle-aged man were out of the running from the start.

There was one more young guy named Jang Taekyung, but he didn’t even qualify as competition.

*He’s weirdly irritating, though.*

A run-of-the-mill C-rank Hunter. He wasn’t even part of a major Guild, just a small-timer scraping by with high-end equipment he’d leased despite it being above his station. Yet his attitude and way of speaking were strangely confident.

In fact, at the end of their conversation a moment ago, Taekyung had seemed almost annoyed with him.

*Trying to save face, are we?*

With the two irritating bastards, Jang Taekyung and Choi Minwoo, standing together, it was only natural for Im Changsoo to keep his eyes and ears trained on them.

—Mooooo!

It was when the Minotaurs began appearing one after another.

“What do you think?”

“It would probably be difficult, wouldn’t it?”

*Well, look at these bastards.*

Im Changsoo, who had just been about to call his men back, closed his mouth and listened.

“What about you, Mr. Taekyung?”

“Me?”

That was already absurd enough, but the answer that came a moment later was even more ridiculous.

“I’m not sure.”

A C-rank Hunter facing eight Minotaurs, and what? He wasn’t sure?

The bastard would be a corpse within a minute even in a one-on-one fight, but all he had going for him was his mouth.

*Crazy bastards. Go ahead and write a novel.*

Im Changsoo let out a short laugh, then suddenly paused.

An idea had flashed through his mind: this was a chance to humiliate the two men he disliked in front of Song Song.

That was why he abruptly stepped between them.

“You were having such an interesting conversation that I couldn’t help overhearing some of it. You don’t mind, do you?”

He planned to get an apology, laugh at them, and make it unmistakably clear who held the upper hand.

But then…

“Then should I call you Shit Changsoo?”

“What?”

“Im Changsoo or Shit Changsoo. I don’t care what your surname is.”

Shit Changsoo.

Im Changsoo’s brain froze at an insult unlike anything he had ever heard in his life.

* * *

Silence fell all around us.

Sangdong Guild. Peace Guild.

Even the Minotaurs seemed to stop mooing.

In that suffocating silence, the man’s tightly closed mouth finally opened.

“…You little shit.”

At this point, using polite speech would have been ridiculous.

I gave him an equally breezy answer.

“What, you little shit?”

“You really… Are you insane?”

“Everyone on Earth is already spinning. Don’t you know geocentrism, you ignorant bastard?”

“That’s heliocentrism. Geocentrism is the cosmological view that the Earth is fixed at the center of the universe, unmoving, while the Moon, Sun, and planets orbit around it, each traveling along its own celestial sphere…”

*Smack.*

Im Kkeokjeong’s enormous, cauldron-lid-sized hand had approached so quietly that no one noticed it until it clamped over Team Leader Choi’s mouth.

“Mmph. What are you doing? Mmph, mmph.”

…

I wished he would just drop dead right there.

There was a limit to having no sense of the situation. I almost wondered whether Sangdong Guild had paid him.

“I can’t believe I’m talking to people like you.”

Im Changsoo looked at Team Leader Choi and me as if we were unbelievable.

“How did airheaded bastards like you even become Hunters?”

“What, do they recruit based on school transcripts? Get a TOEIC score of 900 and you’re B-rank, and if you can speak Chinese, you’re A-rank?”

“You’d better shut that mouth if you want to live a long time.”

“Wow, threats now? I’m so scared I won’t even be able to piss in Sangdong Guild’s direction.”

Im Changsoo ground his teeth, sparks flying from his eyes.

“You seem to have forgotten… This is a Gate.”

“I know, asshole. I also know that eight Minotaurs are coming toward us from over there.”

They say even a tiger comes when you talk about it.

Right on cue, the bellow of a bull echoed through the cavern.

—Moooooo!

“They’re coming!”

“What do we do?”

“What do you think? Get back! Hurry!”

*Boom. Boom. Boom.*

The cavern floor shook every time the herd of Minotaurs moved.

Watching his team members run back with their tails between their legs, Im Changsoo spat out a wad of phlegm.

“You should consider yourself lucky.”

“I tend to be pretty lucky.”

Thanks to the System, it wouldn’t be an exaggeration to say that I was living a second life. I had gone through enough hardships to die from, but I had always been blessed with incredible luck.

“We’ll see each other after I deal with those bastards.”

“That works, too.”

“I hope you’re prepared to take responsibility for what you said.”

“I think I can handle that.”

I looked at the Level window floating above his head.

> **System**
>
> **Level 65 Im Changsoo**

Level 65. High.

Compared to his other team members, he was nearly ten Levels higher, which meant he was probably quite capable even among B-rank Hunters.

Of course, he still wasn’t as good as me.

*Well, character and ability aren’t proportional.*

Hunters weren’t selected based on TOEIC scores, school grades, or personality tests.

I shook my head and turned away.

“How about now?”

“…?”

“The Minotaurs. Didn’t you say you were confident you could handle them alone?”

Ah. I had a rough idea of what he was getting at.

His intentions were obvious from his tone and expression, and a short laugh escaped me.

“I don’t remember saying anything like that.”

“You should take responsibility for what you said.”

“You’re too childish. I can’t indulge you. If you have a problem, settle it one-on-one after the raid.”

Butler Kim and Miss Song, who had been watching the situation with calm expressions, spoke up as well.

“It would be better if both of you calmed down.”

“Excuse me, but don’t you think this is a bad time?”

*Boom-boom-boom.*

Even now, the Minotaur herd was drawing closer by the second.

It was fortunate that they were approaching cautiously. If they had really wanted to, the battle could have begun long ago.

“You heard them, right? Don’t put innocent people in danger. We’ll deal with this later…”

“Five bills.”

“Huh?”

Im Changsoo spread all five fingers wide.

*That wasn’t five stars… it was five bills.*

Was he talking about the thing I thought he was?

“The Minotaur herd over there. If you handle them alone, I’ll give you five big bills per head.”

“Big bills?”

“Yeah. Big bills.”

That meant fifty million won per Minotaur, or four hundred million for all eight.

Even for me, a C-rank Hunter, that was a considerable sum.

*But…*

I didn’t want to look weak in front of everyone, especially Song Song, by showing how easily money swayed me.

This was a matter of pride!

*Miss Song. Can you hear my heart?*

I gazed deeply into her eyes and answered.

“I refuse.”

Im Changsoo’s eyebrow twitched.

“Even if I give you all rights to the byproducts?”

“No.”

“Magic Gems might come out of them.”

“Still no.”

My answer was as firm as a juvenile court judge’s. Im Changsoo bit his lip.

“What a pointlessly proud bastard. I’m offering four billion won and all rights to the byproducts, and you’re refusing?”

“Get lost… Wait. What did you just say?”

Had I heard him wrong?

All kinds of thoughts raced through my mind. Only after sorting them out could I finally part my lips.

“How much? Four billion won?”

“Didn’t I say? Five big bills.”

…

“Then… five hundred million per Minotaur?”

*You should’ve said five fucking huge bills.*

Four billion won.

The mind-boggling sum left not only me, but Song Song and Im Kkeokjeong, gaping.

*What the hell, is this guy made of money?*

He was the team leader of a mid-sized Guild and a B-rank Hunter, so he probably earned a lot.

But casually offering billions of won like this was absurd.

“You’re just giving me four billion?”

“Just? That won’t do. This is a bet.”

“What kind of bet?”

“I need something to gain, too.”

The corners of Im Changsoo’s lips curled.

“If you die or run away, all the rewards promised so far are void. On top of that…”

His head slowly turned.

His gaze stopped on one person.

“Me?”

“Yes. I’d like to invite Miss Song to join our Guild.”

Im Changsoo bowed politely.

The sudden change in attitude was so different from how he had acted until now that it was downright creepy.

“Ugh, that’s giving me goose bumps. Just act the way you were. It looks much better than putting on a fake act.”

…

…

Song Song had an honest personality.

She shuddered, as if she really had gotten goose bumps, and folded her arms.

“Shit Changsoo—no, Im Changsoo, right?”

“…Yes.”

“Okay. I’ll be blunt. You’re not my type.”

Her blunt declaration came in like a 160-kilometer-per-hour fastball, tight and inside. Im Changsoo’s gaze wavered.

“You’re tall and handsome, but you look exactly like you’d cheat. I hate wind, you see.[^1] I finally got my hair looking nice, and if it gets mussed up… Ah, no, that’s not what I mean, is it?”

“Y-yes? Yes?”

“Anyway, you’re not my type. I absolutely can’t stand womanizers who flaunt their money.”

I had never seen Im Changsoo look so dumbfounded.

To anyone else, I probably had the same expression right now.

“Oh, that look you just had was kind of okay. But I’ve been watching you for a while, and your personality is kind of… You can tell that yourself, can’t you?”

Im Changsoo barely managed to compose his expression before answering.

“We can work those things out one by one.”

“Do you really have to taste something to know whether it’s shit or soybean paste? You don’t seem interested in anything but bumping bellies with me. Am I right?”

“……!”

“……!”

Everyone, myself included, was left gaping.

As if bashful, she toyed with her hair while delivering one line after another, each blow landing like a nuclear bomb.

“It’s not like I particularly dislike Sangdong Guild.”

Im Changsoo, who had been taking hit after hit without a break, brightened and asked:

“Really?”

“Yes. I can always switch again anyway.”

…

*Miss Song, are you a genius?*

After delivering a massive fuck-you with an innocent expression, Song Song continued.

“But I’d need to ask permission before switching Guilds. Right, Guild Master?”

“Ah, of course.”

Butler Kim had been watching with an interested look in his eyes. Song Song turned toward him.

“Team Leader, what do you think?”

“What do you mean? About Song Song switching Guilds?”

“If we lose this bet, that’s what will happen, right?”

Team Leader Choi calmly nodded.

“Go ahead.”

“Isn’t that a little too easy an answer?”

“I answered easily because it was an easy question.”

For just a moment, I thought I saw hurt in Song Song’s eyes.

*No, surely not.*

The emotion had passed too quickly for me to be certain.

Returning to her frank, easygoing self, Song Song turned to Im Changsoo and said:

“Then I’m in on the bet. What about you, Mr. Taekyung?”

“I…”

My deliberation wasn’t short.

From the moment I first heard Team Leader Choi’s question, a strange certainty had already taken root deep in my heart.

The certainty that I was stronger than those bastards.

“I’ll take the bet.”

A smile spread across Team Leader Choi’s lips.

“I’ll join in, too. A bet is more fun when the stakes are high, isn’t it?”

“Wow, look at you, a proper gambler. How much?”

“Four billion won. Of course, I’m betting that Jin Taekyung will take down all eight.”

“What?”

Im Changsoo stared at Team Leader Choi for a moment, then let out a short laugh.

“You’re an interesting bunch. One of you is desperate to get himself killed, and the other is dying to throw away his money.”

“So what’s your answer?”

“Obviously, yes.”

“Should we write up a contract?”

“A contract? What do you take me for? I keep my word once I’ve given it. You don’t have to keep yours. I’ll make you keep it. Everyone, move back!”

The enormous, damp cavern transformed into a Colosseum.

An arena with an absurd amount of money at stake.

I was the gladiator who had to fight the Minotaur herd.

“Team Leader Choi. What will you do if I lose?”

“You will win.”

Where did this confidence come from?

Faith in himself? Or in what he’d seen of me so far?

It didn’t matter.

I would simply do my best to achieve my goal.

*Boom-boom-boom-boom-boom!*

—Moooooo!

Twenty meters ahead, I could see each of them clearly.

Hot breath steaming from their nostrils. Heat. Muscles. Weapons held high.

*This is my first time fighting a cow.*

It should be an interesting experience.

I gripped my spear and charged at the herd like a matador.

[^1]: The Korean word *baram* can mean either “wind” or an affair, making her next line a deliberate pun.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 83`.

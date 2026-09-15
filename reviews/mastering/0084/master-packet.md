# Master Edit Task — Chapter 84

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
| 진무경    | **Jin Mukyung**    |
| 임창수    | **Im Changsoo**   |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 임꺽정 | **Im Kkeokjeong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 꼰대 | **boomer** | Modern slang for a hidebound older person; used by Cheongpung. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |

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

#### Chapter 82 tail (verified mastered)

…
> **System** > > **Level 58 Minotaur Warrior** “—Moooooo!” They looked far more vivid and imposing in person than they had in the video, but… “That’s all?” “There’s only one?” There really was just one. *Could that Minotaur have gotten lost in the labyrinth, too?* “At that level, we should be able to handle it without ranged support, shouldn’t we?” “Hye-rin, I’ll be right back.” The Sangdong Guild members confidently stepped forward. Two tanks and two damage dealers, all of them B-rank Hunters. Their intention to show off in front of the women was painfully obvious. *Oh, you morons.* Guys like that always fooled around and ended up dead. Of course, that probably wouldn’t happen because of a single Minotaur. “If you’re going to do it, finish it quickly.” With Im Changsoo’s permission, the four men drew their weapons and started toward the monster. That was when— *Boom. Boom.* “Hm?” “—Moo.” A Minotaur popped out of the second of the five holes. “Oh, now there are two.” “That one’s a little smaller. It looks weaker, so you take it.” “What the hell are you saying? Says the weakest bastard here.” *Boom. Boom.* “—Moo.” The third hole. “Oh, three. At this rate, this might actually be a pretty fun fight.” “Anyone who gets so much as a scratch buys drinks tonight. How about it?” “I’m in.” “I’m in. The guy who suggests these things always ends up paying.” *Boom. Boom.* “—Moo.” “Ah, shit. What is this?” “Four might be a bit much.” “We should probably form up and take them out one at a time.” “Agreed.” Team Leader Choi, who had been watching the situation, scratched his neck. “Maybe we should wait a little longer before coming up with a strategy.” “Huh?” “The holes. Don’t you get the feeling more might come out?” “No way. It’s not like they’re introducing Olympic athletes.” *Boom-boom-boom-boom!* *He was right.* Lane five—no, the fifth hole—had news for us, too. The only unexpected part was that this time, it wasn’t alone. “—Moooooo!” Maybe it had a lot of friends. Four Minotaurs came stampeding out together. Including the ones that had already appeared, there were eight in total. Four B-rank Hunters had no chance against that many. Team Leader Choi spoke. “What do you think?” “It might be difficult.” *Difficult, my ass. If you don’t want to die, stay behind the tank.* I had toned it down for the benefit of the ears around us. “What about you, Mr. Taekyung?” “Me?” “Yes. You, Mr. Taekyung.” “Hmm.” Minotaurs were B-rank monsters, and their Levels were in the mid-to-late fifties. For a martial artist, that would be close to Top-tier. But if I fought them, I would have to account for all sorts of variables. Simply put, I would have to fight them to know. “I’m not sure.” “You’re not sure… Do you know something?” Team Leader Choi stared at me with a strange look in his eyes. “Most C-rank Hunters don’t answer like that. They wouldn’t take time to think about a question like that, much less take it seriously.” I felt a sudden twinge of unease. I had no reason to hide my strength, but I also had no desire to brag about it to the whole neighborhood. For now, I wanted to avoid attention and keep it as my own secret. A Hunter who was just a little more capable than everyone else. That was all. “I’ve known this for a while, but you really are an interesting person, Jin Taekyung.” “No, wait, Team Leader. I think there may be some misunderstanding here.” I had just begun to speak when— “Haha, I see. Listening to you, even I’m getting interested.” Im Changsoo suddenly cut in, his gaze sweeping over Team Leader Choi and me. “You were having such an interesting conversation that I couldn’t help overhearing some of it. You don’t mind, do you?” *Was it my imagination, or did that sound like “If you do mind, what are you going to do about it?”* “For a C-rank with fuck-all to his name, you sure had a lot to say about Minotaurs and whatnot. You were practically writing a novel.” *Ah. So I wasn’t imagining it.* I looked at Im Changsoo with fresh eyes. *It suits him.* Everyone had clothes that suited them. The same went for smiles and attitudes. That was how Im Changsoo looked to me now. The mockery gathered in the raised corners of his mouth suited him perfectly. It was practically made for him. “I didn’t mean to offend you.” At Team Leader Choi’s characteristically impassive expression and tone, Im Changsoo let out a short laugh. “Why would I be offended? It’s the truth. These guys are fucking lousy. They only look impressive because people keep calling them B-rank. Among B-ranks, they’re complete bottom-of-the-barrel trash. But…” Im Changsoo jerked his chin toward me. “They’re still better than a C-rank. Isn’t that right, Mr. Jang Taekyung?” I finally said what I had been holding back all this time. “It’s Jin Taekyung.” “Whether you’re Jin Taekyung or Jang Taekyung, I don’t care what your surname is.” “Then should I call you Shit Changsoo?” “What?” “Im Changsoo or Shit Changsoo. I don’t care what your surname is either.” The smile disappeared from Im Changsoo’s face. [^1]: The tongue-pulling hell is a Buddhist hell where liars and slanderers are punished by having their tongues pulled out.

#### Chapter 83 tail (verified mastered)

…
Kkeokjeong gaping. *Why’s this bastard such a big spender?* He was the team leader of a mid-sized Guild and a B-rank Hunter, so he probably earned a lot. But casually offering billions of won like this was absurd. “You’re giving me four billion just like that?” “Just? That won’t do. This is a bet.” “What kind of bet?” “I need something to gain, too.” The corners of Im Changsoo’s lips twisted upward. “If you die or run away, every reward I’ve offered so far is void. On top of that…” His head slowly turned. His gaze stopped on one person. “Me?” “Yes. I’d like to invite Miss Song Song to join our Guild.” Im Changsoo bowed politely. The sudden change in attitude was so different from how he had acted until now that it was downright creepy. “Ugh, that’s giving me goose bumps. Just act the way you were before. It looks much better than putting on a fake act.” “…” “…” Miss Song-i certainly had an honest personality. She shuddered as if she really had gotten goose bumps, then folded her arms. “Shit Chang—no, Im Changsoo, right?” “…Yes.” “Okay. I’ll be blunt. You’re not my type.” Her blunt declaration came in like a 160-kilometer-per-hour fastball, tight and inside. Im Changsoo’s gaze wavered. “You’re tall and handsome, but you look exactly like the cheating type. And I hate wind, you see.[^1] I finally got my hair looking nice, and if the wind musses it up… Ah, no, that’s not what I meant, was it?” “Y-yes? Yes?” “Anyway, you’re not my type. I absolutely can’t stand womanizers who flaunt their money.” I had never seen Im Changsoo look so dumbfounded. To anyone else, I probably had the same expression right now. “Oh, that look you just had was kind of okay. But I’ve been watching you for a while, and your personality is kind of… You can tell that yourself, can’t you?” Im Changsoo barely managed to compose his expression before answering. “We can work those things out one by one.” “Do you really have to taste something to know whether it’s shit or soybean paste? You don’t seem interested in anything but bumping bellies with me. Am I right?” “…!” “…!” Everyone, myself included, was left gaping. She toyed with her hair as if bashful while delivering one line after another, each blow landing like a nuclear bomb. “It’s not like I particularly dislike the Sangdong Guild.” Im Changsoo, who had been taking hit after hit without a break, brightened and asked: “Really?” “Yes. I can always switch again anyway.” “…” *Miss Song, are you a genius?* After delivering a massive fuck-you with an innocent expression, Miss Song continued. “But I’d need to ask permission before switching Guilds. Right, Guild Master?” “Ah, of course.” Butler Kim had been watching with an interested look in his eyes. Miss Song turned toward Team Leader Choi. “Team Leader, what do you think?” “What do you mean? About you switching Guilds?” “If we lose this bet, that’s what will happen, right?” Team Leader Choi calmly nodded. “Go ahead.” “Isn’t that a little too easy an answer?” “It was an easy question, so I answered easily.” For just a moment, I thought I saw hurt in Miss Song’s eyes. *No, surely not.* The emotion had passed too quickly for me to be certain. Returning to her frank, easygoing self, Miss Song turned to Im Changsoo. “Then I’m in on the bet. What about you, Mr. Taekyung?” “I…” I thought it over for a while. From the moment I first heard Team Leader Choi’s question, a strange certainty had already taken root deep in my heart. The certainty that I was stronger than those bastards. “I’ll take the bet.” A smile spread across Team Leader Choi’s lips. “I’ll join in, too. A bet is more fun when the stakes are high, isn’t it?” “Wow, look at you. A real gambler. How much?” “Four billion won. Of course, I’m betting that Jin Taekyung will take down all eight.” “What?” Im Changsoo stared at Team Leader Choi for a moment, then let out a short laugh. “You’re an interesting bunch. One of you is desperate to get himself killed, and the other is dying to throw away his money.” “So what’s your answer?” “Obviously, yes.” “Should we write up a contract?” “A contract? What do you take me for? Once I give my word, I keep it. You don’t have to keep yours. I’ll make you keep it. Everyone, move back!” At that moment, the enormous, damp cavern transformed into a Colosseum. An arena with an absurd amount of money at stake. And I was the gladiator who had to fight the Minotaur herd. “Team Leader Choi. What will you do if I lose?” “You will win.” Where did that confidence come from? Faith in himself? Or faith in what he’d seen of me so far? It didn’t matter. I would simply do my best to achieve my goal. *Boom-boom-boom-boom-boom!* —Moooooo! Twenty meters ahead, I could see every one of them clearly. Hot breath steaming from their nostrils. Heat. Muscles. Weapons held high. *This is my first time fighting a cow.* It should be an interesting experience. I gripped my spear and charged at the herd like a bullfighter. [^1]: The Korean word *baram* can mean either “wind” or an affair, making her next line a deliberate pun.

## Korean source

```text
＃84화



임꺽정은 생각했다.

‘미친 짓이야.’

진태경은 C급 헌터다. 반면 미노타우로스는 B급 몬스터.

게다가 한 마리도 아니고 여덟 마리나 된다. 그의 눈에 비친 상황은 무모함을 넘어 절망적이었다.

‘그깟 돈이 뭐라고.’

40억은 분명 인생을 바꿀 수 있을 만한 금액이지만 목숨을 버릴 정도는 아니다. 임창수는 돈으로 진태경의 눈을 가렸고, 진태경은 판단력을 상실했다.

‘내가, 내가 말려야 돼.’

저 악랄한 상동 길드 놈들도, 말리지 않는 김 집사도, 최 팀장도 전부 미쳤다. 아끼는 동생의 개죽음만큼은 막아야 했다.

“태경아!”

임꺽정이 막 창을 꼬나 쥔 진태경을 향해 손을 뻗으려던 그 순간이었다.

쉭-

“……어?”

바람 소리와 함께 진태경이 사라졌다. E급 헌터인 임꺽정은 닿을 수도, 제대로 볼 수도 없는 속도로 질주를 시작했다.

눈 깜짝할 사이에 벌어진 일. 임꺽정은 얼빠진 음성을 토해 냈다.

“어, 어어.”

이게 뭐지? 무슨 일이 벌어지고 있는 거지? 태경이가 저 정도였나? 아니, C급 헌터가 이렇게 빠를 수가 있나?

쉬이이익!

검은 번개가 동굴을 가로지른다. 한 걸음, 두 걸음, 세 걸음.

수십 미터의 거리가 단숨에 좁혀진 건 찰나에 불과했고 창날이 번쩍 빛났다.

쐐애애액! 서걱!

미노타우로스. 3미터가 넘는 놈의 거체가 기우뚱거린다.

어깨 위로 있어야 할 굵은 목은 이미 그 자리에 없었다.

인간의 몸과 소의 머리를 한 반인반수가 지금 이 순간만큼은 그저 평범한 인간 같다는 착각이 들었다.

툭.

순식간에 베인 머리가 동굴 바닥에 떨어지고.

쿵.

머리를 잃은 몬스터의 신형이 허물어진다. 깔끔하게 잘려 나간 목의 단면에서 핏물이 왈칵 쏟아졌다.

“이게 무슨……!”

누군가가 토해 낸 목소리가 모두의 마음을 대변한다.

보이지 않는 충격과 경악 속에서, 한 사람이 씩 웃었다.

“할 만한데?”

그 한마디가 결정타다.

임꺽정은 다리에 힘이 풀렸고, 임창수는 저도 모르게 중얼거렸다.

“시발…… 내 40억.”



* * *



미노타우로스는 근접 전투에 특화된 체형이다.

중형 몬스터답게 거구인 데다 엄청나게 단단한 근육으로 똘똘 뭉쳐 있고, 사용하는 무기도 메이스나 도끼 같은 중병기다.

콰쾅!

그러면 뭐 해. 못 맞추면 말짱 황인데.

있는 힘껏 휘둘러 봤자 애꿎은 동굴 바닥만 박살 낼 뿐이다.

‘힘 하나는 인정.’

하지만 싸움은 힘만으로 하는 게 아니다. 나는 한 놈의 품 안으로 파고들며 아랫배를 찔렀다.

푸푹.



- 정확한 공격!

- 상태 이상, [출혈]이 발동됩니다!



- 모오오오.

미노타우로스의 울음소리가 애처롭다. 처음처럼 광포하게 달려들기에는 이미 너무 많은 피를 흘렸다. 아마 조금 전의 그 공격이 마지막 힘을 쥐어짠 일격이었을 것이다.

- 모오, 모오오.

비틀거리며 뒷걸음질 치는 녀석에게로 다가갔다. 송아지 같은 눈망울을 보니 마음이 약해……지기는 개뿔, 이게 다 5억짜리 돈다발로 보인다.

“다음 생에는 부디 강원도 횡성에서 태어나라.”

- 모오오!

서걱.

미노타우로스의 숨이 끊겼다. 거대한 피 웅덩이가 여덟 개. 몬스터 사체도 여덟 구로 늘어난 순간이었다.

띠링.



- 레벨 업!



경쾌한 시스템 알림은 영화 BGM이고, 이 영화의 진짜 백미는 따로 있다. 나는 활짝 웃으며 돌아섰다.

“자, 즐거운 정산 시간.”

경악과 침묵에 휩싸여 있는 사람들 중 유독 한 사람이 눈에 띄었다.

나는 반쯤 얼어붙은 임창수가 들을 수 있도록 큰 소리로 정산을 시작했다.

“보자, 일단 두당 5억이니까…….”

움찔.

“하나, 둘, 셋, 넷. 여덟 마리. 도합 40억. 와, 몇 마리는 마정석도 떨궜네? 부산물도 다 내 거랬지?”

움찔. 움찔.

“창수야. 왜 대답이 없니? 설마 나한테 거짓말 친 거니?”

임창수가 어색한 미소를 지었다.

“당연히 아니지.”

“말이 짧다.”

“그럴 리가 있겠습니까. 저는 그냥…….”

“그냥. 뭐?”

“태경 씨. 잠시만 제 얘기를…….”

“태경 씨? 아까부터 물어보고 싶었는데 우리 창수 몇 살?”

“……스물다섯 살입니다.”

“어이구. 요, 요 잔망스러운 새끼. 스물다섯밖에 안 됐으면서 어른들한테 그렇게 싸가지 없게 군 거야?”

“…….”

“아까부터 혓바닥이 반 토막이 났나, 반말 찍찍 하길래 아흔다섯은 되는 줄 알았네. 얼굴은 왜 이렇게 삭았냐? 출생 신고 늦게 한 거 아니지?”

계속 이어지는 내 말에 임창수의 얼굴이 분노로 벌겋게 달아올랐다.

“표정 관리 잘하자. 한 번만 더 홍익인간 되면 진짜 빨갛게 만들어 준다.”

“……죄송합니다.”

가까스로 표정 관리에 성공한 녀석이 조심스럽게 입을 열었다.

“저어, 하나만 여쭤봐도 되겠습니까?”

“여쭤봐.”

“정말 C급 헌터 맞으신지…….”

“응. 맞는데?”

임창수는 불신에 찬 눈빛으로 나와 널브러진 미노타우로스 사체를 번갈아 바라봤다.

“뭐, 왜.”

“꼭 밝히고 싶지 않으시면 말씀 안 해 주셔도 됩니다.”

“그건 뭐 알아서 생각하고.”

“아, 아닙니다.”

말은 아니라고 했지만 머릿속으로는 상상의 나래를 펼치고 있는 게 분명하다. 평범한 C급 헌터라고 생각했던 내가 B급 몬스터를, 그것도 여덟 마리를 정면 승부로 발라 버렸으니까.

‘그래, 많이 상상해라.’

괜히 상동 길드랑 틀어져 봤자 좋을 게 없다. 저쪽에서 이렇게 알아서 숙여 주니 그냥 고마울 따름이다.

“그럼 혹시 신분 세탁…… 아니시죠. 아니시겠죠. 네.”

헛소리를 지껄이려던 임창수가 내 창을 곁눈질하더니 바로 말을 돌린다. 이거 은근히 반응 재밌네.

“그래서?”

“예?”

“예는 무슨. 돈 줘야지. 40억.”

사실 배 째라 식으로 나올까 봐 살짝 걱정이다.

40억이 뉘 집 개 이름도 아니고, 일반인들은 평생 벌어도 만져 보기 힘든 거금 아닌가.

하지만 임창수는 달랐다.

“아, 물론 드려야죠.”

“……확실해?”

“예. 약속은 지킵니다.”

너무 시원시원한 대답이라 의심이 갈 정도다.

제아무리 B급 헌터라고 해도 평균 수입이라는 게 있는데, 임창수는 수십억을 주머니 속 천 원처럼 말한다.

“이렇게 말해 놓고 잠수 타는 거 아니지? 계약서 없다고 쌩 까고 그러면 나 많이 섭섭하다.”

은근슬쩍 창을 쓰다듬자 녀석이 화들짝 놀란다.

“절대, 절대 아닙니다. 그 정도 능력은 충분히 됩니다.”

“흐음. 돈 좀 버나 보네. 상동 길드에서 대우 잘해 주나 봐?”

“아뇨. 남들이랑 다를 것도 없습니다.”

“당연히 다를 게 없겠지. 네가 무슨 길드장 아들이라도 되냐? 뭐 잘났다고 잘해 줘?”

“…….”

“……?”

“…….”

이거 뭔가 공기가 묘한데.

나는 곰곰이 생각하다가 물었다.

“아버님 성함이?”

“임, 춘 자에 수 자 쓰십니다.”

“상동 길드장님 성함은?”

“임, 춘 자에 수 자 쓰십니다.”

기묘한 우연이다. 임창수의 아버지와 상동 길드장의 이름이 같다니. 하긴, 세상은 넓고 동명이인은 많은 법이니까.

“야, 이건 혹시나 해서 물어보는 건데…… 실례지만 아버님 직업이 어떻게 되시냐?”

“헌터신데요.”

“그냥 헌터?”

“길드 운영하고 계십니다.”

“아, 그래.”

이 자식 상동 길드장 아들이었구나.

짧은 침묵이 흘렀고, 그 잠깐 사이 나는 임창수에게 느꼈던 낯익음의 정체를 깨달았다.

“네가 걔야?”

“개요?”

“아니, 너에 대해 들어 본 적이 있어서.”

재작년 이맘때쯤인가, 한 귀로 듣고 한 귀로 흘렸던 이야기다. 상동 길드장의 하나뿐인 늦둥이 아들이 B급 헌터로 각성, 아버지 길드에서 한자리 꿰찼는데 여자를 그렇게 밝혀서 골칫거리라더라.

그래서 붙여진 별명이…….

“껄떡쇠. 맞지?”

임창수는 고개를 푹 숙이는 것으로 대답을 대신했다.

하긴 사람들 앞에서 듣기에는 쪽팔린 별명이긴 하다. 하지만 40억을 수금해야 하는 나는 따뜻한 목소리로 녀석을 위로했다.

“괜찮아, 인마. 남자가 그럴 수도 있지. 나도 전에는 너처럼 사는 게 꿈이었어.”

하지만 현실은 냉혹한 법이었고, 꿈은 100TB USB로 스며들었다. 야동계의 이름난 권위자인 진호 형은 내 USB를 빌려 간 후, 퀭한 얼굴로 나타나 한 줄 평을 남기기도 했다.



‘이건 유네스코 세계 문화유산에 지정되어야 한다.’



뭐 어쨌든.

내 따뜻한 위로에 임창수가 고개를 들었다.

“정말이십니까?”

당연히 아니지. 내가 아무 여자한테나 들이대는 그런 놈으로 보이니? 나야말로 이 시대의 해바라기. 오직 송이 씨 한 사람만 바라보는…….

잠깐만, 이 새끼 아까 전에 송이 씨한테 집적거렸잖아.

“이 자식이.”

“헉!”

지레 겁을 먹은 임창수가 반사적으로 검 자루에 손을 올렸다.

스릉. 탁.

그러나 검날은 채 반도 빠져나오지 못하고 도로 모습을 감출 수밖에 없었다. 번개처럼 다가간 내가 놈의 검 자루를 내리누름과 동시에 다리를 걷어찼기 때문이다.

쿠당탕!

중심을 잃고 넘어진 녀석의 목을 지그시 누르자 안색이 하얗게 질린다.

“컥, 커컥!”

“이 새끼가. 어디서 연장을 꺼내?”

진무경에게 얻어맞으면서 배운 보람이 있다. 예전 같았으면 지금처럼 간단히, 부드러운 동작으로 B급 헌터를 제압할 수는 없었을 텐데. 임창수도 놀랐겠지만 내가 더 놀랐다.

“여기 게이트야, 인마. 아까 네가 했던 말인데 벌써 잊었어?”

“죄, 죄송합니다!”

마음 같아서는 흠씬 두들겨 패 주고 싶지만 미수에 그쳤으니 봐주기로 했다. 40억을 못 받아서 그런 게 절대 아니다.

“위자료.”

“컥. 네?”

“검 뽑았잖아. 살인미수 몰라? 거기에 나랑 송이 씨. 아니지, 우리 길드원들 모두에게 정중한 사과.”

“그게 무슨!”

임창수가 억울한 눈빛으로 사람들을 바라봤지만 도움의 손길은 없었다.

임창수의 팀원들은 내 눈이 닿기만 해도 찔끔 물러날 뿐이었고, 오히려 구경하고 있던 우리 길드원들은 한 술 더 떴다.

“협력 길드의 길드원을 상대로 검을 뽑다니. 이것 참.”

안타깝다는 듯 혀를 차는 김 집사.

“돈 주기 싫어서 그런 거 아니에요? 세상에, 창수 씨 너무 저질이다. 안 그래요, 아저씨?”

“응? 으응. 젊은 친구가 아주 악질이네!”

송이 씨와 임꺽정의 저질, 악질 콤보에 이어서.

“자, 다들 제 투구를 봐 주시겠습니까? 이 제품은 핀란드의 유명한 장비 제작사 자일리톤에서 제작한 맞춤 투구로서…… 온갖 기능이 있지만 가장 중요한 영상 녹화 마법이 걸려 있습니다.”

최 팀장의 마지막 한 방까지.

배신감과 황당함에 입을 딱 벌리고 사람들을 바라보던 임창수가 한숨을 푹 내쉬었다.

“하겠습니다.”

“뭐라고?”

“시키는 대로 다 한다고요!”

기다리던 대답이다.

나는 기쁜 마음으로 녀석을 일으켜 세워 주었다.

“자식, 잘 생각했다. 위자료는 천천히 논의해 보자.”

“……미치겠네. 우리 꼰대가 알면 저 죽어요.”

“여기서 죽을래?”

“40억 받기 싫으세요?”

“어쭈.”

다시 한숨을 푹 내쉰 임창수가 입을 열었다.

“질문 하나만 해도 됩니까?”

“하나당 1억.”

“…….”

“농담이야. 해 봐.”

“진짜 뭐 하시는 분입니까?”

그게 그렇게 궁금했나?

나는 피식 웃으며 대답해 주었다.

“투잡 뛰는 사람.”

헌터 겸 무림인.

이 세상에 하나뿐인 투잡이다.
```

## Current accepted English baseline

```markdown
# Chapter 84

Im Kkeokjeong thought.

*This is insane.*

Jin Taekyung was a C-rank Hunter. A Minotaur, on the other hand, was a B-rank monster.

And there wasn’t just one of them. There were eight. To Im Kkeokjeong, the situation looked like more than recklessness. It looked hopeless.

*What the hell does money matter?*

Four billion won was certainly enough to change a person’s life, but it wasn’t worth throwing away one’s life for. Im Changsoo had blinded Jin Taekyung with money, and Taekyung had lost his ability to think clearly.

*I have to stop him. I have to.*

Those vicious bastards from Sangdong Guild, Butler Kim for not stopping him, even Team Leader Choi—they were all insane. He had to prevent his cherished little brother from throwing his life away like a stray dog.

“Taekyung!”

It was at that very moment, when Im Kkeokjeong reached out toward Jin Taekyung, who had just gripped his spear at the ready.

Whoosh—

“…Huh?”

Along with the sound of wind, Jin Taekyung vanished. Jin Taekyung began sprinting at a speed that Im Kkeokjeong, an E-rank Hunter, could neither match nor properly see.

It had all happened in the blink of an eye. Im Kkeokjeong let out a dazed sound.

“Uh, uh-oh.”

What was this? What was happening? Had Taekyung always been this strong? No, wait. Could a C-rank Hunter really move that fast?

Whoooooosh!

A black bolt of lightning shot across the cavern.

One step. Two steps. Three steps.

The distance of several dozen meters vanished in an instant, and the spearhead flashed.

Swoooosh! Slice!

The Minotaur—the over-three-meter-tall monster’s enormous body tilted to one side.

The thick neck that should have been above its shoulders was already gone.

For one moment, it seemed as if the half-human, half-beast creature with a human body and a bull’s head were nothing more than an ordinary person.

Thump.

The head that had been severed in an instant dropped to the cavern floor.

Crash.

The headless monster collapsed. Blood burst from the cleanly severed cross-section of its neck.

“What the…!”

Someone’s voice spoke for everyone’s thoughts.

Amid the invisible shock and stunned disbelief, one person grinned.

“This is doable.”

That one remark delivered the final blow.

Im Kkeokjeong’s legs gave out, and Im Changsoo muttered without realizing it.

“Fuck… my four billion.”

* * *

Minotaurs had bodies specialized for close-quarters combat.

Like any mid-sized monster, they were huge, packed with incredibly dense muscles, and armed with heavy weapons such as maces and axes.

Boom!

But what good was that? If they couldn’t hit anything, it was all for nothing.

No matter how hard they swung, all they could do was smash the innocent cavern floor.

*I’ll give them one thing—their strength is impressive.*

But fights weren’t won with strength alone. I slipped inside one monster’s guard and stabbed it in the lower abdomen.

Squish.

> **System**
>
> **Precise Attack!**
>
> **Status Effect: Bleeding activated!**

—Mooooo.

The Minotaur’s cry was pitiful. It had already lost too much blood to charge in as ferociously as before. The attack it had launched moments ago had probably squeezed out the last of its strength.

—Moo. Mooooo.

I approached the creature as it staggered backward.

Looking into its calf-like eyes almost made me feel sorry for it…

*Like hell.*

All I could see was a stack of five hundred million won.

“In your next life, please be born in Hoengseong, Gangwon Province.”

—Mooooo!

Slice.

The Minotaur’s breathing stopped.

A moment later, there were eight enormous pools of blood.

And eight monster corpses.

Ding.

> **System**
>
> **Level Up!**

The cheerful System notification was the movie’s background music. The real highlight of the movie was something else entirely.

I turned around with a wide smile.

“Now, for the fun part—the settlement.”

Among the people engulfed in shock and silence, one person stood out in particular.

I began settling the accounts loudly enough for the half-frozen Im Changsoo to hear.

“Let’s see. Five hundred million per head to start with…”

He flinched.

“One, two, three, four… Eight of them. Four billion in total. Wow, a few of them even dropped Magic Gems. You said all the byproducts were mine, too, right?”

He flinched again. And again.

“Changsoo. Why aren’t you answering? Don’t tell me you lied to me.”

Im Changsoo forced an awkward smile.

“Of course not.”

“Watch your tone.”

“How could that possibly be the case? I was just…”

“Just what?”

“Mr. Taekyung. If you could just listen to me for a moment…”

“Mr. Taekyung? I’ve been meaning to ask you this for a while. How old is our Changsoo?”

“…I’m twenty-five.”

“Oh, my. What a cheeky little shit. You’re only twenty-five, and you’ve been acting so disrespectfully toward your elders?”

“…”

“What happened to your tongue? You kept spitting out casual speech, so I thought you were ninety-five. Why does your face look so weathered? You didn’t just register your birth late, did you?”

As I kept going, Im Changsoo’s face grew bright red with anger.

“Keep that expression under control. If you turn into a Hongik Ingan one more time, I’ll make you genuinely red.”[^1]

“I’m… sorry.”

After barely managing to compose his expression, he cautiously opened his mouth.

“Um, may I ask you one thing?”

“Ask.”

“Are you really a C-rank Hunter…?”

“Yeah. I am.”

Im Changsoo looked at me and the sprawled-out Minotaur corpses in turn, his eyes filled with disbelief.

“What? Why?”

“If you’d rather not reveal it, you don’t have to tell me.”

“Just think whatever you want.”

“Oh, no. That’s not what I meant.”

He said it wasn’t, but there was no doubt he was letting his imagination run wild.

He had thought I was an ordinary C-rank Hunter, yet I had just beaten eight B-rank monsters in a head-on fight.

*That’s right. Imagine away.*

There was nothing to gain from antagonizing Sangdong Guild for no reason. Since they were bowing their heads on their own, I was simply grateful.

“So, perhaps you’re laundering your identity—no, you aren’t. You wouldn’t be. Right.”

Im Changsoo had been about to spout some nonsense, but he glanced sideways at my spear and immediately changed the subject.

This guy’s reactions were kind of fun.

“So?”

“Pardon?”

“Don’t ‘pardon’ me. You have to pay me. Four billion.”

To be honest, I was a little worried that he might tell me to go to hell.

Four billion won wasn’t some random dog’s name. It was a huge sum of money that ordinary people could hardly hope to lay their hands on even after working their entire lives.

But Im Changsoo was different.

“Ah, of course I’ll pay you.”

“…Are you sure?”

“Yes. I keep my promises.”

His answer was so straightforward that it was almost suspicious.

No matter how much money a B-rank Hunter made, there was such a thing as an average income. Yet Im Changsoo talked about billions of won as casually as if it were a thousand-won bill in his pocket.

“You’re not going to disappear after saying that, are you? If you act like none of this matters because there’s no contract, I’ll be very disappointed.”

I casually stroked my spear, and he flinched violently.

“Absolutely not. Absolutely not. I can easily afford that.”

“Hmm. You must make pretty good money. Sangdong Guild treats you well?”

“No. There’s nothing particularly different about my treatment.”

“Of course there isn’t. It’s not like you’re the Guild Master’s son or something. Why would they treat you especially well?”

“…”

“…?”

“…”

Something about the atmosphere felt strange.

I thought about it carefully before asking:

“What’s your father’s name?”

“Im Chunsu.”

“What’s the Sangdong Guild Master’s name?”

“Im Chunsu.”

What a strange coincidence. Im Changsoo’s father and the Sangdong Guild Master had the same name.

Then again, the world was a big place, and there were plenty of people with the same name.

“Hey, I’m only asking just in case, so forgive me for prying…but what does your father do for a living?”

“He’s a Hunter.”

“Just a Hunter?”

“He runs a Guild.”

“Oh, I see.”

This bastard was the Sangdong Guild Master’s son.

A brief silence passed, and in that short interval, I realized what had seemed so familiar about Im Changsoo.

“Are you that guy?”

“A dog?”

“No, I’ve heard about you before.”

It was a story I had heard around this time the year before last and let pass in one ear and out the other.

The Sangdong Guild Master’s only late-born son had awakened as a B-rank Hunter and secured a position in his father’s Guild. But he was such a womanizer that he was apparently a constant headache.

And the nickname he had earned was…

“Horndog. Right?”

Im Changsoo answered by lowering his head.

It was an embarrassing nickname to hear in front of other people, to be sure.

But since I had to collect four billion won, I comforted him in a warm voice.

“It’s okay, man. Guys can be like that sometimes. I used to dream of living like you, too.”

But reality was cold, and that dream seeped into a 100-terabyte USB drive.

Jinho hyung, a renowned authority in the world of adult videos, once borrowed my USB. When he returned, he had a hollow-eyed expression and left me with a one-line review.

*This should be designated a UNESCO World Heritage Site.*

Anyway.

Im Changsoo lifted his head at my warm consolation.

“Really?”

*Of course not.*

Did I look like the kind of guy who hit on just any woman? I was the sunflower of this era, gazing at only one person in the entire world—Miss Song…

*Wait a second.*

This bastard had hit on Miss Song earlier.

“You little shit.”

“Gasp!”

Im Changsoo, frightened before I had even done anything, reflexively placed his hand on his sword hilt.

Shing. Clack.

But the blade had barely made it halfway out before it was forced back into its sheath.

I had moved like lightning, pressing down on his sword hilt while kicking his legs out from under him.

Crash!

When I pressed down on the neck of the man who had lost his balance and fallen, his face went white.

“Ghk! Cough!”

“You little bastard. Where do you get off pulling that thing on me?”

Getting beaten by Jin Mukyung had certainly paid off.

In the past, I wouldn’t have been able to subdue a B-rank Hunter with such a simple, fluid movement. Im Changsoo was probably surprised, but I was even more surprised.

“This is a Gate, you idiot. You already said that yourself. Did you forget so soon?”

“I’m sorry! I’m sorry!”

I wanted to beat him senseless, but since it had only been an attempt, I decided to let him off.

*It absolutely wasn’t because I hadn’t received the four billion yet.*

“Damages.”

“Ghk. What?”

“You drew your sword. Don’t you know that’s attempted murder? And you owe me and Miss Song—no, all our Guild members—a sincere apology.”

“What are you talking about?”

Im Changsoo looked around at the others with an aggrieved expression, but no one came to his aid.

His team members only shrank back whenever my eyes landed on them. Meanwhile, our Guild members, who had been watching the spectacle, took it one step further.

“Drawing a sword on a member of an allied Guild. Well, I never.”

Butler Kim clicked his tongue as if he felt sorry for him.

“You’re only doing this because you don’t want to pay, aren’t you? My goodness, Changsoo, that’s so low. Isn’t it, Uncle?”

“Hmm? Uh-huh. What a nasty young man!”

That was Miss Song and Im Kkeokjeong’s lowlife-and-nasty-man combo.

And then Team Leader Choi delivered the final blow.

“Now, would everyone take a look at my helmet? This product is a custom-made helmet produced by Xyliton, a famous Finnish equipment manufacturer. It has all sorts of functions, but most importantly, it has been enchanted with a video-recording spell…”

Im Changsoo stared at everyone with his mouth hanging open, betrayed and utterly dumbfounded. Then he let out a long sigh.

“I’ll do it.”

“What did you say?”

“I said I’ll do everything you tell me to!”

That was the answer I had been waiting for.

I happily helped him back to his feet.

“Good choice, kid. We can discuss the damages slowly.”

“…This is driving me crazy. If my old man finds out, I’m dead.”

“Would you rather die here?”

“You don’t want the four billion?”

“You’ve got some nerve.”

Im Changsoo let out another deep sigh before opening his mouth.

“May I ask one question?”

“One hundred million per question.”

“…”

“I’m kidding. Go ahead.”

“What do you really do?”

Was he really that curious?

I let out a quiet laugh and answered him.

“Someone with two jobs.”

A Hunter and a Murim martial artist.

The only two-job combination in the world.

[^1]: *Hongik Ingan*, meaning “to broadly benefit humanity,” is a Korean national founding ideal. Taekyung twists the phrase into a joke about Im Changsoo’s reddening face.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 84`.

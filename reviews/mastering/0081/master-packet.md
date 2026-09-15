# Master Edit Task — Chapter 81

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
| 송송이    | **Song Song**     |
| 임창수    | **Im Changsoo**   |
| 일류     | **First Rate**    |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 힐러      | **healer**            |
| 마법사     | **mage**              |
| 마정석     | **Magic Gem**         |
| 귀가      | **your family**                                                 |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 임꺽정 | **Im Kkeokjeong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
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
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |

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

#### Chapter 79 tail (verified mastered)

…
its elegant design and outstanding performance, it’s sold exclusively to a select number of VIPs……” “Just give me the conclusion.” “I loaded some raid footage onto it. Watch.” He could’ve just said that from the start. Im Kkeokjeong and I put our heads together and watched the video stored on the tablet. “All right, stay calm. Stay calm. Especially the tanks! Keep those shields up. If they break through, everyone here is dead. Of course, I’ll kill you myself before that happens.” “Yes, sir!” Around fifteen Hunters formed an orderly formation at the raid leader’s command. Every one of them was visibly tense. *Four tanks, melee and ranged damage dealers. They’ve even got a mage and a healer.* Their teamwork seemed decent, and so did the team composition. And then…… *So that’s a Minotaur.* A B-rank monster I had only ever seen in monster encyclopedias appeared on the screen. “Moooooo!” A cow’s head on a human body. Seven half-human, half-beast Minotaurs advanced toward the intruders. No—they charged. “Mooooooo!” Their bellowing echoed through the cave. Rock dust shook loose and fell in little showers as the battle began. “Ranged! Fire!” The raid leader screamed himself hoarse. At the same moment, around twenty mana-infused arrows struck the lead Minotaur in the head. Fwish-fwish-fwish! Focusing fire on one target instead of using a wide-area attack had been a good choice. Aiming precisely for its head had been especially effective. No matter how strong a B-rank monster was, it couldn’t reinforce its eyeballs. The Minotaur clawed at its own face in agony. The finishing blow came from the companions following behind it. Crunch! A dark iron club smashed the cow’s head apart. And then— Thud, thud, thud! *Huh.* They used the dead Minotaur’s corpse as a shield and charged straight ahead. Arrows and magic rained down, but they only shredded the corpse. The Minotaurs hiding behind it were unharmed. *These bastards……* They knew how to use their heads. They were at least as intelligent as goblins and dozens of times stronger. That made them all the more dangerous. “Hold!” “Urrrgh!” At the team leader’s shout, the tanks’ veins bulged. Their shields, covered in hazy mana, blocked the iron clubs carrying tremendous force. Wham! Wham! Wham! A small shadow suddenly dropped out of the air between them. A stealth-type Hunter drove a black-painted dagger into another Minotaur’s eye, then vanished. “Moooo……” B-rank monsters weren’t invincible. With support from the other melee damage dealers, archers, and mage, two more Minotaurs fell in the blink of an eye. But the crisis came quickly. *They’re breaking through!* No sooner had the thought occurred to me than the wavering tank line collapsed. Kra-koom! “Graaagh!” “Healer! Healer!” Screams and roars filled the cave. Through the billowing dust, I could see the cow-headed monsters tearing through the formation and swinging their iron clubs. “Moooooo!” “Tanks, damage dealers! Ranged, don’t hold back your mana—pour it all in! Ranged, open up some distance!” Wham-wham-wham! “Mooooooo!” “Healeeeer!” The video continued for about ten minutes before cutting off. The battle hadn’t ended yet. The camera had simply been smashed by an iron club. “Mooooooo!” Bzzzt. As the Minotaur’s roar rang out, the screen filled with static and faded to black and white. Im Kkeokjeong swallowed hard. “……This is no joke.” *Of course it isn’t, old man.* I handed the tablet back to Team Leader Choi and asked, “What Guild was that?” “It was footage of the Bucheon Terminal Guild’s raid last week.” “……” *Whoever named that Guild had one hell of a sense for names.* Not that I had much room to talk as a member of the Peace Guild, but at least our name was better than Bucheon Terminal Guild. “What was the result?” “The Minotaurs were wiped out. Two Hunters died.” People dying during raids wasn’t particularly rare. Being a Hunter meant repeatedly drawing close to death, then running away from it. Even so, I couldn’t help feeling heavy-hearted. It was a burden the survivors would have to carry for the rest of their lives. Just as I did now. “I see.” That was all I could manage. I pulled out my smartphone and searched for the incident. Several related articles appeared. > **A Bucheon Guild: The Sacrifice Brought on by a Reckless Raid** > > On the sixteenth, C-rank Hunters identified as Mr. Lee and Mr. Park died in the B-rank Gate *The Minotaur’s Labyrinth*. The Hunter Association authorities…… So the Hunters who died had been C-rank. That made sense. A small-to-medium Guild like that couldn’t possibly have enough talent to fill all fifteen or so spots on a raid team with B-rank Hunters. *Then……* I quickly looked over the Guild members. The Qi Sense I had activated a moment earlier had already brought up their Level windows. Ding. Ding. Ding. > **System** > > **Level 75 — Choi Minwoo** > > **Level 80 — Kim Hwajong** > > **Level 64 — Song Song** The next moment, my eyes met Im Kkeokjeong’s. “What’s wrong?” “It’s nothing.” I answered as casually as I could and turned away, but my thoughts were anything but casual. > **System** > > **Level 24 — Im Hyeokjun** *This raid is dangerous.* [^1]: Haejangguk, literally “hangover soup,” is a Korean soup traditionally eaten after drinking to help ease a hangover. [^2]: Makgeolli is a traditional Korean rice wine with a milky appearance and a mildly sweet, tangy flavor.

#### Chapter 80 tail (verified mastered)

…
by K Company. Nicholas, known as the greatest craftsman in North America…” Clatter! “Wow, it really is! Taekyung, look at this. It’s huge inside!” “It is.” “World-renowned designers also participated…” “Wow, I’ve never seen anything like this before. I could probably sleep in here.” “Once you close the suitcase, you won’t be able to get out until someone opens it.” “Really?” “This product keeps stored items in optimal condition through proper temperature control and ventilation at all times……” Click, click. “This is awesome. What do you think? Does it suit me?” “It fits you perfectly. I thought it was a tailored suit.” “You look good too. What’s that?” “It says it’s a Black Drake Leather Set. I mean, it’s a leather set.” “Really? If it’s Team Leader Choi’s, it must be good. Hahaha! Thanks, Team Leader Choi!” “…Don’t mention it.” Team Leader Choi had completely lost the will to fight by then and changed into his equipment without another word. Meanwhile, I checked each piece of equipment I was wearing. *Item Check.* Ding. > **System** > > **Item Window** > > **Masterwork Black Drake Leather Set** > > **Type:** Armor > **Grade:** Peak > **Description:** An armor set made from the leather of the B-rank monster Black Drake. The work of a superb craftsman is evident. > > **Effect:** Strength, Stamina, Agility, Toughness +10 > > — Full Set Effect is active. > > **Item Window** > > **Masterwork Black Thorn Spear** > > **Type:** Spear > **Grade:** Peak > **Description:** A spear made from the spine of the B-rank monster Black Drake. It is both extremely hard and sharp. The work of a superb craftsman is evident. > > **Effect:** Bleeding has a 90% chance to activate upon hitting an enemy. After checking them, I had exactly one thought. *This is insane.* An armor set that gave me forty points simply by wearing it, plus a spear that could make an enemy bleed to death with nearly every stab. The item information alone made it clear how incredible the effects were. *So this is what gear advantage feels like.* When I suddenly remembered my time in Murim, tears clouded my vision. *Armor, my ass.* I had fought in soft scraps of cloth and broken dozens of cheap spears. The people of Murim were the very definition of hard-boiled—the real tough guys. “Maybe it’s because it’s designer gear, but it feels different right away.” I turned my head and saw Im Kkeokjeong hopping up and down in place, his face flushed with excitement. “It’s incredibly light, and I feel faster too. Is it just my imagination?” “I doubt it.” There was no way it was just his imagination. Team Leader Choi had prepared this equipment specifically for Im Kkeokjeong, a D-rank Hunter. Of course it was good. *Should I take a quick look?* Just as I was about to place my hand on the full plate armor Im Kkeokjeong was wearing, Team Leader Choi approached us, already fully equipped. “If you’re ready, let’s head out.” “What about Butler Kim?” “Out here, he’s the Guild Master.” At Team Leader Choi’s pointed correction, Butler Kim chuckled. “It’s fine. Besides… I’m always wearing my equipment.” As he spoke, he unbuttoned his suit jacket, revealing bracelets on both wrists and a necklace. They were no ordinary accessories, of course. The necklace was set with a Magic Gem, while the bracelets were engraved with strange yet beautiful patterns. “An artifact?” “I find these more convenient than a staff.” Butler Kim answered modestly, but it was rare to see a mage dressed so lightly. Most wore at least some light armor or carried a staff for self-defense to improve their chances of survival. *Well, he's probably no ordinary mage.* Anyone from Ares Guild commanded respect. I suddenly found myself curious about Butler Kim’s past, but the question was wiped clean from my mind the next moment. Knock, knock. “Hey, guys. Are you still not done?” “Ah, we’re ready.” It was Miss Song’s voice from outside the changing room. As soon as Team Leader Choi answered, the door eased open. “Hurry up. People will be waiting.” “Whoa.” Her long, straight hair was tied up tightly, and she was wearing light leather armor. I swallowed a startled breath at the sight of her. *Can a person really be this beautiful?* It wasn’t just love making me see her through rose-colored glasses. That was simply the truth. I knew that much just from seeing Im Kkeokjeong, who had treated her like a cute niece until now, swallow hard. Gulp. “…” *I’d better keep an eye on this guy.* If even Im Kkeokjeong was reacting like this, the other guys would be no exception. Any young guy who seemed even moderately capable would come by the truckload to hit on her. *Take Im Changsoo, for example. Im Changsoo, say. Or maybe Im Changsoo…* Im Changsoo. The young Team Leader from Sangdong Guild. His face had been hovering in my mind since earlier. *I was sure I’d never seen him before.* And yet… why was he bothering me so much? Was it because that punk seemed interested in Miss Song? “What are you doing? Aren’t you coming out?” “Ah, yes.” My thoughts were cut short. At Im Kkeokjeong’s urging, I hurried out of the changing room. [^1]: Go-stop is a Korean card game traditionally played with a deck of flower cards.

## Korean source

```text
＃81화



게이트 앞, 헌터 복장을 한 열 명의 남녀가 화기애애한 분위기 속에 대화를 나누고 있었다.

“오빠들, 우리 괜찮은 거 맞지?”

여자 헌터의 말에 상동 길드 소속의 B급 헌터가 흉갑을 두드렸다.

“걱정 말라니까. 우리 못 믿어?”

“아이, 믿지. 그런데 지난주에 여기서 사람 죽었다잖아.”

“그 병신들은 신경 쓰지 마. 실력도 안 되는 놈들이 깝치다가 뒈진 걸 누굴 탓해? 안 그래요, 창수 형?”

가만히 듣고 있던 임창수가 허공에 담배 연기를 내뿜으며 말했다.

“불안하면 집에 가라. 분위기 좆같이 만들지 말고.”

순간 싸해진 분위기. 앞서 말을 꺼냈던 여자 헌터가 억지로 입꼬리를 끌어 올렸다.

“아니 오빠, 나는 그냥.”

“닥치고. 어쩔래.”

“……미안.”

“그럼 구석에 찌그러져 있어. 너 아니어도 데려올 년들 차고 넘치니까.”

거친 언행에도 누구 하나 반발하는 법이 없다. 그저 어색한 웃음으로 분위기를 환기시키려 애쓸 뿐이다.

이런 광경이 임창수에게는 익숙하고도 당연했다.

‘병신들.’

게이트는 마정석이라는 황금 알을 낳는 거위고 헌터는 황금 알을 수확하는 일꾼이다. 마름 집안에서 태어난 그는 시작점부터 달랐다.

“지금 호텔 갈 거 아니면 작작 붙어 있어. 괜히 또 좆 같은 소문 퍼지면 귀찮아지니까.”

“형, 얘들은 믿어도 돼요.”

“안 믿어, 새꺄. 지난번 걔들도 믿을 만하다며?”

“그건, 뭐…….”

상동 길드가 인근에서 방귀깨나 뀌는 중견 길드라지만 대중의 시선을 무시할 정도는 아니다. 지금까지 몇 번 여자를 잘못 건드렸다가 길드장인 아버지에게 경고를 듣기도 했다.

“문제 생기지 않게 잘하자. 응?”

“넵. 명심하겠습니다. 충성!”

“쯧. 대답은 잘해요.”

임창수가 반쯤 타들어 간 담배를 튕겼다. 기다렸다는 듯 옆에서 주문이 들려왔다.

“윈드(Wind).”

마법으로 생성된 바람이 담배꽁초와 냄새를 저 멀리 날려 보낸다. 주문을 외운 여 마법사가 매력적인 웃음을 지어 보였다.

“나 잘했지?”

임창수는 여 마법사를 위아래로 훑었다. 매끈한 몸매에 뇌쇄적인 미녀인 그녀와는 일종의 스폰 관계였다.

뛰어난 미모와는 달리 형편없는 실력의 C급 헌터. 그러나 길드장 아들의 애인이라는 사실만으로 상동 길드에 들어왔다.

그밖에도 집, 차, 수많은 명품…… 모두 임창수의 주머니에서 나왔지만 아깝다는 생각은 안 해 봤다.

‘뭐, 지금까지는 그랬지.’

하지만 오늘 생각이 바뀌었다. 몸매, 외모, 분위기. 30분 전쯤 만났던 그 여자에 비하면 촌스럽고 싸 보인다.

‘송송이라고 했나?’

떠올리는 것만으로도 아랫배가 묵직해졌다.

허접한 신생 길드에 있기에는 너무 아까운 꽃. 잔뿌리 하나 상하지 않게 뽑아서 자신의 화분에 심을 생각이었다.

“오빠, 뭐 좋은 일 있어? 왜 그렇게 웃어?”

임창수는 대답하지 않았다. 대신 저 멀리서 모습을 드러낸 다섯 사람을 향해 손을 흔들었다.

“아, 여깁니다!”

물론 전(前) 애인을 향해 작은 목소리로 한마디 덧붙이는 것도 잊지 않았다.

“누가 네 오빠야, 썅년아.”



* * *



껄떡쇠, 아니 임창수가 환하게 웃으며 말했다.

“오셨군요. 아, 여기는 제 팀원들입니다.”

상동 길드 소속으로 보이는 이들이 고개를 꾸벅 숙였다.

임창수를 포함하면 딱 남자 다섯에 여자 다섯이다. 하나같이 번쩍거리는 고가의 장비를 착용했는데, 실용성보다는 디자인을 중시한 차림이었다.

특히…….

‘오우야.’

여성 헌터들 같은 경우에는 눈을 어디에 둬야 할지 모르겠다. 애 둘 딸린 유부남인 임꺽정은 굳은 얼굴로 속삭였다.

“끝내주는데.”

“…….”

나도 모르게 고개를 끄덕일 뻔했지만 간신히 참았다.

송이 씨가 좋지 않은 표정으로 우리를 바라보고 있었기 때문이다.

‘그나저나…….’

이게 레이드냐, 소개팅이냐. 잘생기고 예쁜 남녀가 짝을 맞춰서 하하 호호 웃으며 게이트에 들어갔다가는 골로 가기 십상이다.

뭐, 레벨이나 장비를 봐서는 괜찮을 것 같긴 하지만.

“다들 모이셨습니까?”

게이트를 담당하는 중년 공무원이 인원과 자격증을 체크했다. 진입 전 반드시 거쳐야 하는 절차 중 하나다.

“상동 길드, B급 다섯 분에 C급 다섯 분. 맞으시죠?”

임창수가 예의 바른 웃음을 지어 보였다.

“맞습니다.”

“그럼 평화 길드. B급 두 분에 C급 두 분, 그리고…….”

헌터 자격증을 휙휙 넘기던 공무원의 손이 멈칫했다.

“E급 한 분? 어디 계시죠?”

임꺽정이 털이 숭숭 난 팔을 번쩍 치켜들었다.

“어, 납니다.”

“혹시 포지션이?”

“담당자님께서 눈썰미가 없으시네. 이런 무식한 방패 들고 다니면서 마법 쓰겠소? 흐흐.”

“탱커시군요.”

공무원이 미간을 찡그렸다.

탱커는 말 그대로 최전방에서 몬스터들의 공격을 막아 내는 인간 방패다. 그 위험 때문에 힐러와 함께 헌터 중 가장 많은 수당을 지급받기도 하고, 사망률도 높다.

“E급이 여길 왜 와. 그것도 탱커? 나 참.”

“한 방에 많이 땡길 수 있잖아. 혹시 아냐? 마정석이라도 우르르 떨구면 로또 맞은 거지.”

“오빠, 오늘 정말 괜찮은 거 맞지?”

“걱정 마. 혜린이 너는 이 오빠가 지킨다.”

임창수의 팀원들 사이로 수군거림이 번졌다. 우리를 들여보내야 하는 공무원도 예외는 아니었다.

“E급 탱커라…….”

그의 우려 섞인 목소리에 김 집사가 나섰다.

“그는 20년 경력의 베테랑입니다. 위험을 대비해서 충분한 장비도 착용했으니 문제는 없다고 생각합니다만.”

“베테랑 좋죠, 좋긴 한데. 아시잖아요. 지난주에 사망 사고. C급 탱커 둘이 죽었어요. 이런 상황에 이게 참.”

뜻밖의 지원군이 나타난 건 그때였다.

“담당자님, 어떻게 안 되겠습니까?”

임창수다. 그는 조곤조곤 말을 이었다.

“이미 협동 레이드 계약서에 사인도 했고, 이렇게 좋은 분들을 만났는데 무효로 돌리는 건 좀 아쉬워서요.”

“저, 그러니까 이게.”

“살짝 유도리 있게 넘어가 주시면 참 감사할 것 같은데…… 부탁드립니다.”

신기한 놈일세. 입에서 나오는 말은 감사와 부탁인데, 목은 뻣뻣하고 행동은 고압적이다.

순간 움찔한 공무원이 이내 한숨을 내쉬었다.

“좋습니다. 대신 팀장님께서 잘 단속해 주셔야 합니다.”

“물론이죠.”

단속이라. 어감이 영 별로다.

임창수의 도움으로 허가는 내려졌지만 개미가 기어가는 것처럼 가슴 한구석이 근질거렸다.

‘뭐, 좋은 게 좋은 거겠지.’

당사자인 임꺽정도 덤덤한 표정인데, 내가 기분 나빠하는 것도 우습다.

“그럼 진입하셔도 좋습니다.”

공무원의 말에 사람들이 게이트 앞에 섰다. 상동 길드 열 명, 평화 길드 다섯 명. 총합 열다섯에 B급 헌터만 일곱에 달하는 정예 레이드 팀이다.

“그럼…….”

당연하다는 듯 선두에 선 임창수가 윙크했다.

“게이트에서 뵙죠.”

쏴아악-!

임창수가 마력장 너머로 사라지자 송이 씨가 중얼거렸다.

“재수 없어.”

저도 그렇게 생각합니다.



* * *



쏴악.

마력 특유의 음습하고 끈적끈적한 기운이 몸을 휘감은 것도 잠시. 눈을 뜨자 새로운 공간이 펼쳐져 있었다.

F급 게이트와는 비교도 되지 않는 거대한 크기의 동굴. 그리고 아가리를 쩍 벌린 입구 세 개. 오는 길에 영상으로 봤던 그곳이다.

‘다른 게 있다면…….’

띠링.



- [미노타우로스의 미로]에 입장하셨습니다.

- 퀘스트, [B급 게이트 클리어]가 생성되었습니다.



나한테만 들리는 시스템 알림이 있다는 거지. 거기에 더해 퀘스트도.

“자, 들어가기 전에 인원, 장비 점검 한 번씩 합시다.”

사람들이 각자 물건을 확인하는 사이, 슬그머니 동굴 구석으로 이동한 나는 마음속으로 뇌까렸다.

‘퀘스트 확인.’

띠링.



퀘스트



[B급 게이트 클리어]

당신은 난생처음 B급 게이트에 진입했습니다.

최초 1회에 한해 레이드 성공 시, 그에 상응하는 보상이 주어집니다.



등급 : 일류

제한 : 진태경

임무 : B급 게이트 클리어 (미완료)

보상 : ???

실패 : ???





산뜻한 시작이군. 내가 훈훈한 미소와 함께 퀘스트창을 닫은 그때였다.

“혼자서 뭐 해요?”

등 뒤에서 불쑥 들려온 목소리. 고개를 돌리자 이쪽으로 걸어오는 임창수의 모습이 보였다.

“저요?”

사람 잘못 봤나 했는데, 아니었다.

“평화 길드의 장태경 씨. 맞죠?”

“진태경인데요.”

“네, 장태경 씨.”

이 인간이 귀가 먹은 건지, 내 혀가 잘못된 건지는 모르겠지만 일단 고개를 끄덕여 줬다.

‘어차피 한번 보고 말 사이니까.’

앞서 임꺽정의 일로 나름 힘써 준 터라 약간의 고마움도 남아 있었다.

“저한테 무슨 용무라도?”

“하하, 용무라고 할 것까진 없고요. 이것도 인연인데 통성명이나 하자는 거죠. 제 소개는 아까 했으니 아실 테고. 잘 부탁드립니다.”

누가 그랬다. 웃는 얼굴에 침 못 뱉는다고. 조금 껄끄럽긴 했지만 얼굴 가득 미소를 머금고 악수를 청하는 임창수의 손을 맞잡았다.

“아, 예. 저도 잘 부탁드립니다.”

일면식도 없는 타 길드의 팀장이 먼저 악수를 청한다?

지난 7년간 협동 레이드도 몇 번 뛰어 보고 일용직 헌터 경험도 꽤 있지만 지금 같은 경우는 처음이다.

‘하긴, 그때는 F급이었으니까.’

그 시절에는 완전히 공기 취급이었는데, C급 헌터라고 사람대접해 주는 건가 싶어 기분이 묘해진다.

‘그런데 왜 하필 나지?’

의문은 금방 풀렸다.

“흑색 드레이크 가죽 세트. 맞죠?”

“아.”

이 자식도 명품충이구나. 내 장비를 위아래로 훑어본 임창수가 연신 감탄사를 내뱉었다.

“이야, 이거 사진으로나 보던 건데. 어디서 사셨어요? 해외 직구? 아니면 청담동?”

“대여했어요.”

“업체에서 리스 하셨구나. C급 헌터이신 걸로 알고 있는데 이게 유지가 되나……. 아, 죄송합니다. 악의가 있어서 한 말은 절대 아닙니다. 혹시 기분 나쁘셨어요?”

당연히 기분 나쁘지, 인마.

하지만 속마음을 대놓고 티 낼 정도로 멍청하진 않다.

임창수가 한 말이 사실 냉정한 현실이기도 하고.

‘그런데 인간이 좀 눈치가 없네.’

나는 점잖게 손을 내저었다. 약간의 넉살도 섞어서.

“안 그래도 허리 휘고 있어요. 버는 족족 유지비로 다 나갑니다. 주위 사람들은 미친놈이라고 욕하고.”

“하하, 그래도 목숨보다 중요한 게 있겠습니까. 안 그래요?”

“그렇죠.”

“그럼 다른 분들도 마찬가지겠네요.”

“네?”

“다른 분들이요. 평화 길드원분들. 다들 장비가 좋으시던데.”

“그런가요? 제가 그쪽은 잘 몰라서.”

임창수가 재미있는 농담을 들은 것처럼 웃었다.

“에이, 거금 들여서 장비 리스까지 하시는 분이 하실 말씀은 아니다.”

리스는 맞지만 거금을 들이진 않았다. 최 팀장이 무상 대여 해 주는 거니까. 사실대로 얘기해야 하나 잠깐 고민했지만 이내 마음을 접었다.

‘그런 거 말해 봐야 뭐 해.’

설명해 봤자 내 입만 아프지.

더 이상 장비에 대해 얘기하는 것도 귀찮아진 나는 적당히 얼버무렸다.

“다들 저랑 비슷해요.”

“그렇군요.”

그때, 임창수의 팀원 중 하나가 달려와 준비가 끝났다고 알렸다.

“이런, 너무 잡담이 길었네요. 그럼 전 이만. 마지막으로 팀원들 점검하고 다 같이 움직여야 할 것 같아서요.”

“수고하세요.”

“옙.”

예의 바르게 꾸벅 고개를 숙이고 떠나려던 임창수가 대뜸 물었다.

“맞다. 아까부터 묻고 싶었던 건데.”

“……?”

“혹시 우리 어디서 본 적 있나요?”

송이 씨한테 들었다면 날아갈 듯 기뻤겠지만 중갑옷을 걸친 수컷한테 들으니 기분이 별로다.

“초면입니다.”

“그래요?”

“네.”

어디선가 들어본 듯한 이름이라고 생각했을 뿐이지, 초면은 맞다. 내 단호한 대답에 임창수의 웃음이 진해졌다.

“알겠습니다. 그럼 이만.”

뭐지. 마지막 웃음은 왠지 기분 나쁜데.

그의 뒷모습을 응시하고 있을 때, 어느샌가 다가온 최 팀장이 물었다.

“아는 사입니까?”

“아뇨. 그냥 친하게 지내자는데요.”

“흠. 스카우트 제의는 아니고요?”

“전혀요. 그냥 장비 덕후라 말 건 것 같은데. 대뜸 오더니 어디서 샀냐고 물어보더라고요.”

“청담동에서 샀습니다.”

“…….”

난 안 궁금해.



* * *



“창수 형, 저 새끼는 갑자기 왜요?”

“그냥. 보니까 장비 괜찮아서 슬쩍 떠본 거지.”

“헐, 진짜네. 저거 자기 거래요?”

“생각을 해, 이 새끼야. C급 주제에 저런 걸 어떻게 입고 다녀.”

“그럼 리스? 미친놈이네요. 유지비 장난 아닐 텐데.”

“놔둬라. 귀엽잖아. 지도 나름 살아 보겠다고 무리하는 게.”

임창수는 피식 웃었다.

‘역시 별것 아닌 놈들이었어.’

난데없이 고가의 장비를 쫙 빼입고 오기에 혹시나 하는 마음이 든 건 사실이다. 괜히 잘못 건드렸다가 일이 커질 수도 있을 테니까.

하지만 파악이 끝난 지금은 마음이 편해졌다.

‘송송이.’

돈과 능력. 두 가지만 있으면 뭐든 할 수 있다. 여자 하나 얻는 건 일도 아니다. 임창수는 그렇게 믿었다.

“슬슬 출발하자. 전달해.”

“옙!”
```

## Current accepted English baseline

```markdown
# Chapter 81

In front of the Gate, ten men and women dressed as Hunters were chatting in a friendly atmosphere.

“Oppas, we’re really okay, right?”

At the female Hunter’s question, a B-rank Hunter from Sangdong Guild thumped his breastplate.

“Don’t worry. Don’t you trust us?”

“Of course I do. But I heard someone died here last week.”

“Don’t worry about those idiots. They died mouthing off despite not having the skill to back it up. Who can they blame? Right, Changsoo hyung?”

Im Changsoo, who had been listening quietly, exhaled a cloud of smoke into the air.

“If you’re nervous, go home. Don’t make the mood fucking miserable.”

The atmosphere instantly turned cold. The female Hunter who had spoken first forced the corners of her mouth upward.

“No, oppa, I was just—”

“Shut up. What are you going to do?”

“…Sorry.”

“Then go make yourself scarce in a corner. I’ve got more than enough bitches to bring along even without you.”

Despite his rough words and behavior, not one of them dared to object. They merely tried to lighten the mood with awkward smiles.

This sort of thing was familiar—and perfectly natural—to Im Changsoo.

*Idiots.*

Gates were geese that laid golden eggs called Magic Gems, and Hunters were the laborers who harvested them. Born into a family of estate managers, he had started out on a completely different footing.

“If you’re not heading to a hotel right now, quit clinging to each other. It’ll be a pain if another shitty rumor starts spreading.”

“Hyung, these ones are trustworthy.”

“I don’t trust them, asshole. Didn’t you say those last ones were trustworthy too?”

“Well, that was…”

Sangdong Guild might have been a respectable mid-sized Guild that threw its weight around in the area, but it wasn’t powerful enough to ignore public scrutiny. Im Changsoo had already received warnings from his father, the Guild Master, several times for messing with the wrong women.

“Let’s make sure there aren’t any problems, okay?”

“Yes, sir. We’ll bear it in mind. Loyalty!”

“Tsk. You’re good at answering.”

Im Changsoo flicked away his half-burned cigarette. As if she had been waiting for it, someone beside him called out a spell.

“Wind.”

A magically generated breeze sent the cigarette butt and its smell flying far away. The female mage who had cast the spell gave him a charming smile.

“I did good, right?”

Im Changsoo looked her up and down. She had a sleek figure and was an alluring beauty, and the two of them had a sort of sponsorship arrangement.

Despite her outstanding looks, she was a C-rank Hunter with pathetic skills. But the fact that she was the Guild Master’s son’s lover had been enough to get her into Sangdong Guild.

Her house, her car, and countless designer goods—all of them had come out of Im Changsoo’s pocket. But he had never once thought it was a waste.

*Well, that was true until now.*

But today, his mind had changed. Her figure, her looks, her entire air—all of it seemed tacky and cheap compared to the woman he had met about thirty minutes earlier.

*Was her name Song Song?*

Just thinking about her made his lower abdomen feel heavy.

She was a flower far too precious for some pathetic new Guild. He intended to pull her out without damaging a single root and plant her in his own flowerpot.

“Oppa, did something good happen? Why are you smiling like that?”

Im Changsoo didn’t answer. Instead, he waved toward the five people who had appeared in the distance.

“Ah, over here!”

Of course, he didn’t forget to add a quiet remark to his ex-girlfriend.

“Who the hell are you calling oppa, you fucking bitch?”

* * *

That lech—or rather, Im Changsoo—spoke with a bright smile.

“You’ve arrived. Ah, these are my team members.”

The people who appeared to belong to Sangdong Guild bowed their heads.

Including Im Changsoo, there were exactly five men and five women. Every one of them wore expensive, gleaming equipment, and their outfits clearly prioritized design over practicality.

Especially…

*Oh, wow.*

When it came to the female Hunters, I had no idea where to look. Im Kkeokjeong, a married man with two children, whispered with a stiff expression.

“They’re incredible.”

“……”

I almost nodded before managing to stop myself.

Miss Song was looking at us with a displeased expression.

*Come to think of it…*

Was this a raid or a blind date? Handsome and beautiful men and women pairing up, laughing and chatting as they entered a Gate—it was a perfect recipe for getting themselves killed.

Well, judging by their Levels and equipment, they would probably be fine.

“Is everyone here?”

The middle-aged official in charge of the Gate checked our numbers and Hunter licenses. It was one of the procedures we had to complete before entering.

“Sangdong Guild. Five B-ranks and five C-ranks. Correct?”

Im Changsoo gave him a courteous smile.

“That’s right.”

“Then Peace Guild. Two B-ranks, two C-ranks, and…”

The official’s hand paused as he flipped through the Hunter licenses.

“One E-rank? Where is he?”

Im Kkeokjeong thrust up his heavily furred arm.

“Uh, me.”

“What’s your position?”

“Sir, you’re not very observant. Would I carry around a huge brute of a shield like this if I were a mage? Heh heh.”

“You’re a tank.”

The official furrowed his brow.

A tank was exactly what the name suggested: a human shield who stood on the front line and blocked monster attacks. Because of the danger, tanks were among the best-paid Hunters, along with healers. They also had a high fatality rate.

“Why is an E-rank coming here? And he’s a tank, no less? Good grief.”

“You can make a lot in one go. Who knows? If the Magic Gems come tumbling out, we’ll have hit the jackpot.”

“Oppa, we’re really okay today, right?”

“Don’t worry. This oppa will protect you, Hye-rin.”

Murmurs spread among Im Changsoo’s team members. The official who had to let us enter was no exception.

“An E-rank tank…”

Butler Kim stepped forward at the concern in his voice.

“He is a veteran with twenty years of experience. He is also wearing sufficient equipment to prepare for any danger, so I don’t believe there will be a problem.”

“Veteran is good, of course. But you know what happened last week. Two C-rank tanks died. In a situation like this, letting him…”

That was when an unexpected ally appeared.

“Sir, can’t you make an exception?”

It was Im Changsoo. He continued in a soft voice.

“We’ve already signed the cooperative raid contract, and after meeting such fine people, it would be a shame to render it invalid.”

“Well, I mean…”

“If you could be just a little flexible, we’d really appreciate it… Please.”

What a strange guy. The words coming out of his mouth were all gratitude and requests, but his neck was stiff and his manner was high-handed.

The official flinched for a moment, then sighed.

“All right. But Team Leader, you’ll have to keep them under control.”

“Of course.”

*Keep them under control.* What an unpleasant way to put it.

With Im Changsoo’s help, permission was granted, but an ant seemed to be crawling around in one corner of my chest.

*Well, better to let it go.*

Even Im Kkeokjeong, the person involved, looked completely unfazed. It was ridiculous for me to take offense on his behalf.

“You may enter, then.”

At the official’s words, everyone stepped in front of the Gate. Ten Hunters from Sangdong Guild and five from Peace Guild. Fifteen people in total, including no fewer than seven B-rank Hunters—a highly elite raid team.

“Well, then…”

Im Changsoo, who had naturally taken the lead, winked.

“See you inside the Gate.”

Whoosh!

As Im Changsoo disappeared beyond the field of magic, Miss Song muttered,

“What a creep.”

*I agree.*

* * *

Whoosh.

The damp, sticky energy unique to magic wrapped around my body for a moment. When I opened my eyes, a new space unfolded before me.

It was a cavern so vast that it couldn’t even be compared to an F-rank Gate. Three entrances gaped open like enormous maws. It was the place we had seen in the video on the way here.

*The only difference was…*

Ding.

> **System**
>
> You have entered **The Minotaur’s Labyrinth**.
>
> Quest **B-rank Gate Clear** has been created.

There was a System notification that only I could hear. And, on top of that, a Quest.

“All right, let’s check our numbers and equipment one more time before we go in.”

While everyone checked their belongings, I quietly moved to a corner of the cavern and muttered inwardly.

*Check Quest.*

Ding.

> **System**
>
> **Quest**
>
> **B-rank Gate Clear**
>
> You have entered a B-rank Gate for the first time in your life.
>
> Upon successfully completing the raid, you will receive a corresponding Reward. This applies only once.
>
> **Grade:** First Rate
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Clear the B-rank Gate *(Incomplete)*
>
> **Reward:** ???
>
> **Failure:** ???

What a refreshing start.

I had just closed the Quest window with a warm smile when—

“What are you doing over here by yourself?”

A voice suddenly came from behind me. I turned my head and saw Im Changsoo walking toward me.

“Me?”

I thought he had mistaken me for someone else, but he hadn’t.

“You’re Jang Taekyung from Peace Guild, right?”

“I’m Jin Taekyung.”

“Yes, Jang Taekyung.”

I wasn’t sure whether he was deaf or my tongue was malfunctioning, but I nodded for the moment.

*We’ll probably only see each other once, anyway.*

He had helped out over the matter with Im Kkeokjeong, so I still felt a little grateful toward him.

“Did you need something?”

“Haha, it’s nothing I’d call business. This is fate, so I thought we could at least exchange names. You heard my introduction earlier, so you already know who I am. I look forward to working with you.”

Someone once said you couldn’t spit in a smiling face. It was a little awkward, but I clasped the hand Im Changsoo offered with a broad smile on his face.

“Ah, yes. I look forward to working with you too.”

A Team Leader from another Guild—someone I had never even met before—had offered me a handshake first.

I had participated in cooperative raids several times over the past seven years and had plenty of experience as a day-labor Hunter, but this was the first time something like this had happened.

*Then again, I was an F-rank back then.*

In those days, people had treated me like air. Maybe being a C-rank Hunter meant I was finally being treated like a person. It left me with a strange feeling.

*But why me?*

The question was answered almost immediately.

“That’s a Black Drake Leather Set, right?”

“Ah.”

*This guy’s a Designer-Brand Junkie too.*

Im Changsoo looked over my equipment from head to toe and let out one exclamation after another.

“Wow, I’d only ever seen this in pictures. Where did you buy it? Did you order it from overseas? Or get it in Cheongdam-dong?”

“I rented it.”

“You leased it from a company, then. I heard you’re a C-rank Hunter, but can you really keep something like this maintained? Ah, I’m sorry. I absolutely didn’t mean anything by it. Did I offend you?”

*Of course I’m offended, you moron.*

But I wasn’t stupid enough to let my true feelings show so openly.

What Im Changsoo had said was also a cold reality.

*Still, this guy really has no tact.*

I waved a hand with deliberate composure and added a little self-deprecating humor.

“It’s already breaking my back. Every penny I earn goes toward maintenance. The people around me call me crazy.”

“Haha, but is there anything more important than your life? Right?”

“That’s true.”

“Then I suppose the same goes for the others.”

“Sorry?”

“The others. The Peace Guild members. Their equipment looked pretty good too.”

“Did it? I don’t know much about that sort of thing.”

Im Changsoo laughed as if he had heard an amusing joke.

“Come on. That’s not something someone who spends a fortune leasing equipment gets to say.”

The equipment was leased, but it hadn’t cost me a fortune. Team Leader Choi had loaned it to me free of charge. I briefly considered explaining that, but soon abandoned the thought.

*What’s the point of bringing that up?*

Explaining it would just be a waste of breath.

I was already tired of talking about equipment, so I gave him a vague answer.

“They’re all about the same as mine.”

“I see.”

At that moment, one of Im Changsoo’s team members ran over and told him that preparations were complete.

“Oh, dear. We’ve been chatting for too long. I’d better go. I need to check on my team members one last time, and then we should all move together.”

“Take care.”

“Yes.”

Im Changsoo politely bowed his head and was about to leave when he suddenly asked,

“Oh, right. There’s something I’ve been meaning to ask you.”

“……?”

“Have we met somewhere before?”

I would have been overjoyed if Miss Song had asked me that, but hearing it from a male in heavy armor left me feeling less than pleased.

“This is our first meeting.”

“Really?”

“Yes.”

I only thought his name sounded familiar, but this was definitely our first meeting. At my firm answer, Im Changsoo’s smile deepened.

“All right, then. I’ll be going.”

What was that? His final smile rubbed me the wrong way.

As I watched his back, Team Leader Choi approached without my noticing and asked,

“Do you know him?”

“No. He just said he wanted to be friends.”

“He didn’t make a recruitment offer?”

“Not at all. I think he only came over because he’s a gear enthusiast. He suddenly walked up and asked where I bought my equipment.”

“I bought it in Cheongdam-dong.”

“……”

*I wasn’t asking.*

* * *

“Changsoo hyung, why did you suddenly go talk to that bastard?”

“Nothing. His equipment looked decent, so I sounded him out.”

“Holy crap, seriously? Is that stuff really his?”

“Use your brain, asshole. How could a C-rank wear something like that?”

“Then he leased it? Crazy bastard. The maintenance costs must be insane.”

“Leave him alone. It’s cute, watching him overextend himself trying to make something of himself.”

Im Changsoo let out a quiet laugh.

*As expected, they were nothing special.*

It was true that he had felt a little uneasy when they showed up out of nowhere decked out in expensive equipment. If he messed with the wrong people, things could get out of hand.

But now that he had them figured out, he felt at ease.

*Song Song.*

Money and ability. With only those two things, he believed he could do anything. Getting his hands on one woman would be no trouble at all.

“Let’s get moving. Pass it on.”

“Yes, sir!”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 81`.

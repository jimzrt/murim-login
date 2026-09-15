# Master Edit Task — Chapter 87

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
| 임창수    | **Im Changsoo**   |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 대격변     | **Great Cataclysm**   |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |

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

#### Chapter 85 tail (verified mastered)

…
raid team made up of four B-rank Hunters and five C-rank Hunters who would obey his commands. He had trained every one of them to eat only from his hand. “Fine. Then listen carefully to what I’m about to say…” After a short and simple explanation, the team members couldn’t hide their nervousness. “Will it work?” “It does seem possible.” “Oppa, you’re not suggesting what I think you are, right? If you mean killing someone, I don’t know if I can do that.” “Didn’t you just say you’d do anything I told you?” “Even so, that’s a little…” “Forget it. I’d like to, but I’m not reckless enough to go that far. First, we take the camera. Then we put that son of a bitch through a humiliation he’ll never live down.” “Whew. That’s a relief. Then I’m definitely on your side, oppa.” “Do it right. You know what happens if anyone hesitates this time or holds back even a little, right?” “Of course.” “Just trust us, Team Leader. No, hyungnim. Hehe.” A sinister smile spread across Im Changsoo’s lips. *If he trampled on my pride, he has to pay the price.* In the Boss Zone ahead, he would make Jin Taekyung understand exactly who he had dared to cross. There was even a monster there capable of standing against him. *The Minotaur Great Warrior.* The boss monster of **The Minotaur’s Labyrinth**. Despite being only a B-rank monster, it was a monstrous creature whose physical abilities rivaled those of an A-rank. *Once the Great Warrior wears him down, we’ll make our move.* Set a barbarian against a barbarian. Defeat a monster with a monster. The moment both sides were exhausted would be their chance. In one stroke, he could recover both the money he was about to lose for nothing and the pride that had been dragged through the dirt. “Hey, hurry up! It’s the Boss Zone!” Jin Taekyung’s shout rang out the next moment. Im Changsoo smiled broadly. “Yes! Coming!” His steps toward the Boss Zone were remarkably light. * * * “One Annihilation.” Kraaaaaash! The sound of the sky splitting erupted from the tip of my spear. A white vortex that tore apart and devoured everything it touched slammed into the Great Warrior’s muscular chest. —Moo? Crack-crack-crack! There was no need to check whether it was alive or dead. The moment I pulled my spear from its chest, the System notification rang out. Ding. > **System** > > - Defeated **Lv. 70 Minotaur Great Warrior**! > > - Level Up! > > - Quest, **B-rank Gate Clear**, completed! > > - Calculating your contribution… Complete! > > - The Quest Success Reward has been deposited into your Inventory! “Whew.” The last one should always end with one big hit. My body was incredibly tired, though. I shook the blood from my spear and turned around. “Let’s collect the byproducts and get out of here. I’m starving to dea—why are you all looking at me like that?” Im Kkeokjeong spoke for everyone. “You really have to ask?” He looked back and forth between the boss monster’s corpse and me. His eyes demanded some kind of explanation for how I had finished off a B-rank boss monster with a single blow. “Hmm. Let’s just say I got lucky.” “Lucky?” “Yes. Lucky.” It really was because I had been lucky. Lucky that I had lived in a goshiwon.[^1] Lucky that a capsule had been discarded in front of it. All of it. “Good grief. I’m too dumbfounded to speak. Fine.” The others reacted much the same way as Im Kkeokjeong. Even Team Leader Choi, who had already been on a raid with me, looked stunned. “I didn’t realize you were this capable.” “If you know now, that’s enough.” “Could we discuss this?” “Of course.” Not now. Later. I still had something more important to take care of. With my most charming smile, I approached one person. “Miss Song, could I ask you for a heal—what are you guys doing over there?” “Ah.” “What are you doing? Why are you here?” “We’re just…just standing here.” “I-I just think she’s so beautiful.” The Sangdong Guild members clustered around Song Song jumped in surprise and began blurting out whatever came to mind. *What’s with these guys?* I only meant that they should get lost because they were getting in the way between me and Miss Song. *Do I really look that scary?* “Where’s Im Changsoo?” At a single word from me, the Sangdong Guild members split apart like the Red Sea. Im Changsoo answered from behind them, his face white as a sheet. “I’m here.” “What’s wrong with your face? Are you sick?” “I-I think I’m coming down with something.” “Tsk, tsk. Take a potion, you idiot. Your family’s rich.” “…” “Anyway, hurry up and collect the byproducts. Let’s go. I’m tired.” “Yes, yessir.” Once Im Changsoo disappeared with the nuisances, the moment I had been waiting for finally arrived. I flashed Song Song a bright smile. “You’re hungry, right? How about steak at a nice restaurant for dinner?” Song Song smiled back at me. “I’m sorry, but I’m a vegetarian.” “That’s strange. You seemed to eat meat just fine yesterday. How about a salad bar?” “I’m a carnivore.” “…” *I got rejected, right?* [^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement, often used by students and people on tight budgets.

#### Chapter 86 tail (verified mastered)

…
“I’ve also heard he mellowed with age, but can a person’s temper really change that easily?” *For fuck’s sake.* The more I heard, the colder my spine felt. I had the distinct feeling that something was about to go horribly wrong. *Damn it. I shouldn’t have made that bet.* My excitement at the thought of receiving several billion won had lasted only a moment. Now I felt uneasy, like I’d taken a huge dump and forgotten to wipe. I could deal with whatever happened to me, but I absolutely refused to let the other Guild members get hurt. “Taekyung, don’t worry about it too much. I only brought it up just in case.” “I didn’t just cause trouble, did I?” “It’ll be fine. Team Leader Choi thought it sounded fun and joined the bet, too.” “Oh, right.” “Exactly. And look at the way Im Changsoo acted. If I were his father, I would’ve beaten him half to death. He’ll be too embarrassed to tell anyone what happened.” He had a point. What could possibly happen? Hearing that made me feel considerably lighter. I even found myself smiling. “Thanks, Kkeokjeong ajusshi. No, hyungnim.” “Then buy us some beef to celebrate becoming a rich man. Wait, no. You should eat it with Miss Song, not me.” “…Ah.” He was driving a nail straight through my heart. As Im Kkeokjeong killed me with words for the second time, I swallowed my tears. * * * “What brings you here?” The speaker was a man with a distinctive appearance. He was nearing fifty, but his skin was taut and his black hair bristled like wire. His large, piercing eyes alone were enough to make anyone’s knees go weak. *What the hell is with that look in his eyes…?* The manager of a K Bank branch was no exception. He had already met the man several times, but he was an ordinary person, while the other man was an A-rank Hunter—a living witness who had endured the Great Cataclysm with his entire body. His tongue tied itself in knots, and cold sweat trickled down his back. “Well…” “If you came to waste my valuable time, go back. Otherwise, speak now.” The words were sharp, but his tone was fairly gentle. The manager had heard the rumor that Im Chunsoo was trying to mellow his temper with age. Apparently, it hadn’t been a complete waste of effort. *Damn it.* The branch manager squeezed his eyes shut and blurted it out. “I’m sorry, Guild Master. I’ve come regarding your son.” At the mention of his son, Sangdong Guild Master Im Chunsoo’s eyebrow twitched. “Changsoo? What about him?” “Some time ago, you asked me to let you know whenever your son used any of the bank’s services…” Im Chunsoo nodded as if he understood where this was going. “What is it this time? Did he steal my seal? Or take out a secured loan?” “He transferred a considerable amount of money all at once.” “He must be fooling around with women again. Obviously. How much?” “Four billion won to each of two accounts. Eight billion won in total.” “How much?” “Eight billion… Hup.” The branch manager hurriedly swallowed his breath. He had just watched the window behind Im Chunsoo rapidly freeze over. Hiss. It was late summer outside, but cold and frost now ruled the office. Im Chunsoo motioned to the trembling branch manager. “Anything else?” “I-I brought the relevant documents.” With shaking hands, the branch manager placed a stack of papers on the desk. “Good. You may leave.” “I-I’ll see you next time.” After the branch manager fled the room, Im Chunsoo picked up the receiver. The phone had a cold-resistance function, so it transmitted the signal quickly without any problems. Beep, beep. Click. —Yes, Guild Master. Team One’s Leader speaking. “Bring that bastard here immediately.” —…Do you mean Team Leader Im Changsoo? “Team Leader, my ass. He’s fired as of today. Bring that bastard here now!” Bang! The receiver’s life ended there. It shattered into hundreds of icy fragments that covered the desk. “What a pathetic fool. Even after I warned him…” Im Chunsoo glared coldly at the wrecked office, then his gaze stopped on one spot. The stack of papers left behind by the K Bank branch manager. There was no doubt that the documents contained the whereabouts of eight billion won. *You stupid bastard. Which bitch did you get taken in by this time?* He read through the papers, turning them one page at a time, for more than ten minutes. When Im Chunsoo closed the final page, the door flew open with the sound of someone being dragged along. “Team Leader Im Changsoo. I brought him here.” An affable-looking middle-aged man stood there. Clutched firmly in his grasp was a young man. “F-Father!” “My proud son is here.” At his son’s appearance, the father extended a hand. Of course, it was not a gesture of forgiveness. Crackle, crackle, crackle. Cold surged from Im Chunsoo’s grasp. It changed from gas to liquid, then from liquid to solid, completing its transformation into an ice club as hard as steel. “I have a lot to ask you, but first, you’re getting hit.” “Father!” “Shut up, you little shit!” The middle-aged man who had brought Im Changsoo—the Team Leader of Sangdong Guild’s Team One—quietly closed the door. The room would be off-limits for the next half day.

## Korean source

```text
＃87화



“엣취!”

후두두둑!

라면과 밥알을 뒤집어쓴 진호 형이 침착하게 물티슈로 얼굴을 문질렀다.

“마음에 안 들면 말로 해, 말로.”

“그런 거 아냐. 갑자기 막 튀어나왔어.”

“변명하지 마. 더 추해 보인다.”

진짠데. 나는 대답 대신 코를 슥 문질렀다.

어떤 놈이 내 욕이라도 하고 있나?

‘생각해 보니까 그럴 만한 놈이 하나 있긴 한데.’

임창수 그 녀석이라면 범행 동기가 충분하다 못해 차고 넘친다. 그래도 뭐, 내게 40억을 선물한 산타클로스니까 욕 몇 번 정도는 기쁘게 먹을 수 있다.

‘혹시나 했는데, 의외로 약속은 지키는 놈이었어.’

나는 아침에 받은 문자를 떠올렸다. 스마트폰에 깔아 둔 은행 어플 알림은 입, 출금 내역을 빠짐없이 알려 준다.



[진태경님의 110-***-*** 계좌에 4,000,000,000원이 입금되었습니다.]



사소한 해프닝이 있었다면 그걸 처음 발견한 게 진호 형이라는 거다. 샤워하겠다고 스마트폰을 방에 놓고 간 게 실수다.

“넌 돈도 많은 놈이 라면이 뭐냐, 라면이?”

“거 되게 말 많네. 소고기 넣어 줬잖아. 소고기라면 싫어?”

“인마, 지금 그 뜻이 아니잖아.”

탕! 진호 형이 거칠게 수저를 내려놨다.

물론 한마디 하려고 그런 게 아니라 배가 불러서다.

“통장에 40억이 있는데 왜 고시원에서 라면을 먹고 있냐 이거지. 내 말은.”

“뭔 상관이야. 내 맘이지.”

“……그렇긴 한데.”

“그리고 돈 들어온 지 한 시간밖에 안 됐거든? 나도 어떻게 해야 될지 모르겠으니까 조용히 해 봐.”

멀쩡한 척하고 있지만 사실은 아까부터 멍하다. 일개미처럼 독하게 돈을 벌어 왔지만 쓰는 곳은 항상 정해져 있었으니까.

그러던 중 거금이 하늘에서 뚝 떨어진 거다.

40억은 많은 일을 할 수 있는 돈이다. 많은 생각이 뒤따를 수밖에 없었다.

“뭔 놈의 고민이 그렇게 많아? 돈 생기면 가장 먼저 하고 싶은 일이 있었을 거 아냐.”

가장 먼저 하고 싶은 일이라…….

‘그거라면 하나 있지.’

후루룩. 마지막 면발을 빨아들인 나는 자리에서 일어났다.

방을 나서기 전 진호 형에게 한마디 남기는 것도 잊지 않았다.

“고마워.”

“별말씀을.”

“냄비 설거지 잊지 말고. 간다.”

“야, 야!”



* * *



“어?”

현관문 앞, 하연이가 눈을 동그랗게 떴다.

“진짜네. 인터폰 화면 보고 설마 했는데.”

“……진짜가 아니면 뭔데.”

“음. 그래픽?”

“그게 오랜만에 만난 오빠한테 할 소리냐?”

“무슨 소리래. 그저께도 와 놓고.”

아, 맞다. 현실 시간으로는 얼마 안 됐지.

워낙 시간 차가 크다 보니 나도 종종 헷갈린다. 신발을 벗으며 물었다.

“뭐 하고 있었어?”

“공부.”

“그러고 보니까 학교는? 평일이잖아.”

하연이가 코맹맹이 목소리로 대답했다.

“열이 39도래. 2교시까지 버티다가 조퇴했어. 어차피 내일부터 여름 방학이라 얼마 전부터는 계속 자습이고.”

“너 이제 방학이냐? 아니, 그 전에 조퇴했는데 공부를 해?

어째 절정 고수보다 얘가 더 대단해 보인다. 난 이상하게 학교에서 엄청 아파도 조퇴하고 집에 오면 아픈 게 싹 낫던데.

열이 39도나 되는 이 상황에서도 공부라니, DNA가 다른가?

“배움에는 끝이 없는 법.”

학생주임 같은 하연이의 말을 뒤로하고 거실로 들어섰다. 집에서는 우리 둘을 제외하곤 인기척 하나 느껴지지 않는다.

“엄마는?”

“은행.”

“기다렸다는 듯이 대답하네.”

“진짠데?”

“엄마가 그러라고 시켰어?”

“응? 뭘?”

누굴 닮았는지 연기가 천연덕스럽다. 만약 그 사실을 모르고 있었다면 깜빡 속아 넘어갔을 것이다.

‘진작 말씀드렸어야 했는데.’

나도 모르게 씁쓸한 웃음이 흘러나왔다. 현관을 향해 되돌아가는 나를 하연이가 붙잡았다.

“어디 가는데?”

“엄마 찾으러.”

“여기 은행이 한두 개야? 밥 차려 줄 테니까 먹고 있어. 잠시 후면 오실 테니까.”

“괜찮아. 은행 가는 거 아니니까.”

“뭐?”

“마트 앞 사거리 식당. 맞지?”

하연이의 손에서 힘이 스르륵 풀렸다.

“……알고 있었어?”

“응. 한참 전부터.”

“엄마가 부탁했어. 비밀로 해 달라고.”

“그것도 알고.”

“오빠, 안 가면 안 돼?”

하연이의 오랜 습관이다. 중요한 부탁에는 꼭 앞에 오빠를 붙이는 것.

“다녀올게.”

나는 하연이의 머리를 헤집어 주고 현관문을 나섰다.

내려가는 엘리베이터 안에서 가만히 손에 남아 있는 녀석의 온기를 생각했다. 이마가 펄펄 끓는 와중에도 녀석이 공부를 하고 있는 이유도.



* * *



주민등록증에 적힌 이름은 하나지만 살면서 불리는 이름은 여러 개다. 올해로 꼭 쉰이 된 김정희도 마찬가지였다.

“아줌마, 여기 삼겹살 2인분 추가요.”

“네, 잠시만요.”

요즘 가장 많이 불리는 이름은 ‘아줌마’다. 그전에는 ‘하연 엄마’. 또 그전에는 ‘태경 엄마’였다. 아이들이 다 크고 일이 바빠지자 들을 수 없게 된 이름들.

그녀의 진짜 이름을 불러 주었던 한 사람은 이미 오래전 세상을 떠났다.



‘정희 씨.’



스물둘에 만난 그는 다정다감했다. 혼란스러웠던 대격변 시기, 대피소에서 만난 두 남녀는 순식간에 사랑에 빠졌다.

행복한 결혼 생활이었다. 세월이 흘러도 그는 여전히 자신의 이름을 불러 주었다.



‘정희야.’



가끔은 다른 사람 앞에서 이름을 불리는 게 부끄러워 물어본 적이 있다.



‘왜 당신은 내 이름만 불러요? 다른 집 남편들은 누구 엄마. 여보. 마누라. 다들 그렇게 부르던데.’

‘그래서 싫어?’

‘아니, 싫은 게 아니라 그냥 궁금해서. 우리 나이도 먹었잖아요.’

‘나이가 뭐가 중요해. 나는 태경 엄마보다 정희를 더 사랑해서 그렇게 부르는 건데.’

‘애들 앞에서 왜 이래요.’

‘어? 엄마 볼 빨개졌다. 엄마 아빠 아침에도 레슬링 해? 맨날 밤에 하던데.’

‘……태경이 오늘부터 일찍 자라.’



이별은 생각보다 일찍 찾아왔다. 예고도 없이 시내 한복판에 열린 게이트로 두 아이는 아버지를 잃었고 그녀는 남편을 잃었다. 유일하게 자신의 이름을 불러 주었던 한 사람을.

“아줌마!”

김정희는 퍼뜩 정신을 차렸다. 파마머리에 화려한 귀걸이를 한 중년 여성이 그녀를 노려보고 있었다.

“아, 네. 사장님.”

“뭐 하느라 사람이 부르는 소리도 못 들어?”

“죄송합니다.”

“불판은? 설거지 끝났어?”

“저어, 그게.”

잠시 다른 생각을 하느라 손이 멈춰 있었다. 싱크대를 확인한 사장이 눈을 치켜떴다.

“아줌마, 일 이따위로 할 거야?”

“…….”

“참 나. 이럴 거면 내가 직접 하지, 뭣 하러 비싼 돈 줘 가면서 아줌마를 고용했겠어? 안 그래?”

김정희는 고개를 푹 숙였고, 주방의 다른 직원들은 사장의 목소리를 못 들은 척 할 일을 계속했다.

‘비싼 돈은 무슨. 가장 바쁜 시간에 최저 시급으로 부려 먹으면서.’

‘나이 먹었으면 철 좀 들지. 화장 떡칠하고 꾸며도 정희 아줌마보다 안 되는 거 뻔히 아니까 괜히 화풀이야.’

‘애초에 지가 카운터를 똑바로 보고 있든가. 놀러 간 사이에 정희 씨가 받은 주문이 몇 갠데.’

하고 싶은 말은 많지만 생각으로 끝내야 한다. 참다못해 김정희를 편들었던 주방 아줌마는 지난주에 잘렸다.

“이래서 내가 맘 편히 자리를 비울 수 있겠어?”

“……죄송합니다.”

“아줌마 아들 헌터라며. 벌이 괜찮을 텐데 집구석에서 음식이나 하지 왜 여기까지 와서 남의 장사에 민폐를…… 아, F급 헌터라 벌이는 별론가?”

사장의 입가에 비웃음이 맺힌 그 순간.

푹 숙이고 있던 김정희의 고개가 천천히 올라갔다.

“사장님. 말씀이 과하시네요.”

“뭐?”

“과하셨다고요.”

“내가 틀린 말이라도 했다는 거야, 지금?”

“네.”

낯선 느낌에 사장은 말문이 막혔다. 늘 조용하고 온순하던 그녀의 눈동자가 깊이 가라앉아 있었다.

“방금 그 말씀, 사과해 주세요.”

“사, 사과?”

“이 자리에서 지금 당장이요.”

“어, 어머. 그래, 내가 한 말 중에 뭐가 틀렸는데? 아줌마 아들 F급 헌터 맞잖아!”

“등급이 그렇게 중요한가요?”

“당연하지. F급 헌터를 어디에다 써? 우리 아들 정도는 돼야 돈도 잘 벌고 여자도 줄을 서는 거지. 이 가게도…….”

“D급 헌터인 아드님께서 차려 주신 거죠. 알아요. 수십 수백 번도 넘게 들었으니까.”

귀를 쫑긋 세우고 있던 직원들이 저도 모르게 고개를 끄덕였다. 사장의 아들 자랑은 하루에도 몇 번씩 듣는 단골 레퍼토리다.

연봉은 얼마고 집은 몇 평이며 차는 뭔지, 효심까지 깊어 어머니 소일거리 삼아 가게도 열어 줬다는 얘기는 너무 자주 해서 이젠 단골손님도 학을 뗀다.

“그럼 잘 알겠네. 나야 취미 삼아 하는 거지만 아줌마는 다르잖아? 아들 벌이가 시원찮으니까 주방 일 하는 거 아니야?”

“네, 아니에요.”

김정희는 차분하게 말을 이어 갔다.

“우리 태경이, 어릴 때부터 부모 속 한 번 안 썩히고 바르게 컸어요. 가족 위해서 지금도 열심히 일하고 있고요. 돈? 부족하지 않게 벌어요.”

“그런 거 다 핑계지.”

“핑계요? 제 자식이 목숨 걸고 벌어 온 돈인데 부모가 되어서 어떻게 그걸 받아 쓸 수 있겠어요?”

“아줌마, 지금 그거 나 들으라고 하는 소리야?”

“그거야 받아들이기 나름이죠. 그리고 기왕 얘기가 나왔으니 말인데. 그 대단한 아드님은 언제쯤 얼굴을 비추나요?”

“뭐, 뭐?”

“제가 여기서 일한 지 1년이 넘어가는데 그 효심 깊은 아들이 한 번도 찾아오질 않아서요. 전화도 안 하는 건 아니죠?”

쥐 죽은 듯 조용해진 주방 안, 얼굴이 시뻘겋게 달아오른 사장이 눈을 부릅떴다.

“자식도 변변찮은 년이 어디서…….”

직원들은 뒤에 나올 말을 알아차렸다. 사장의 따발총 같은 욕과 함께 해고라는 단어가 튀어나올 게 뻔했다.

그러나 그들 중 아무도 김정희의 반응을 예측한 사람은 없었다.

“말조심해. 이 개 같은 년아.”

“……!”

“……!”

순간 폭탄이 떨어진 듯했다. 죽음 같은 침묵과 믿을 수 없다는 듯 흔들리는 눈동자들. 주방의 모두가 자신의 귀를 의심했다.

‘내가 방금 뭘 들은 거지?’

‘정희 아줌마가 욕을? 세상에.’

언제나 순하고 웃음 많던 김정희다. 하루가 멀다 하고 시비를 걸어오는 사장한테도 싫은 소리 한 번 없이 고개를 숙이던 그녀가, 얼음처럼 차가운 눈빛으로 사장을 노려보고 있다.

“뭐, 뭐라고? 너 지금 뭐라고 했어!”

“개 같은 년이라고 했다. 이 썅년아.”

“쌰, 썅년?!”

충격이 가시기도 전에 2차 폭탄이 떨어진다. 외마디 비명처럼 내지른 사장의 외침은 주방 밖 홀까지 울려 퍼졌다.

“방금 누가 욕하지 않았어?”

“너도 들었어? 방금 누가 썅년이라고 했던 것 같은데.”

“뭐야, 직원들끼리 싸우나?”

웅성거림이 커져 갔다. 손님도, 직원도. 가게 안의 모든 사람들의 이목이 주방을 향해 쏠린 그때였다.

저벅저벅.

모자를 눌러쓴 덩치 큰 청년. 언제 들어왔는지, 언제부터 그곳에 있었는지 아무도 알아채지 못했다. 그가 주방을 향해 걸음을 옮기기 전까지는.

“소, 손님. 주문은 제가…….”

황급히 막아서는 남자 직원의 말에 청년이 빙긋 웃었다.

“괜찮아요. 주문 때문에 온 거 아니니까.”

“아니, 그래도 지금은.”

“실례.”

툭.

부드럽게 밀었을 뿐인데 건장한 체구의 직원이 휘청거리며 쓰러진다. 청년은 반쯤 열린 주방문을 거침없이 밀어젖혔다.

그리고…….

“엄마.”

세상에서 가장 사랑하는 사람의 얼굴과 마주했다.
```

## Current accepted English baseline

```markdown
# Chapter 87

“Achoo!”

Rattle, rattle!

Jinho hyung calmly wiped his face with a wet tissue after getting covered in ramen and grains of rice.

“If you don’t like it, say so. Use words.”

“It’s not like that. It just came out of nowhere.”

“Don’t make excuses. You look even more pathetic.”

But I was telling the truth. Instead of answering, I rubbed my nose.

*Is someone badmouthing me?*

*Now that I think about it, there is someone who might have reason to.*

If it was Im Changsoo, he had more than enough motive. His motive was overflowing. Still, he was the Santa Claus who had given me four billion won, so I was happy to take a few insults.

*I wondered if he would, but the bastard actually kept his promise.*

I remembered the text message I had received that morning. The banking app installed on my smartphone notified me of every deposit and withdrawal without exception.

> Jin Taekyung’s 110-***-*** account has been credited with 4,000,000,000 won.

The only minor incident was that Jinho hyung had been the first to discover it. Leaving my smartphone in my room when I went to take a shower had been a mistake.

“You’ve got plenty of money, so why are you eating ramen?”

“You sure are talkative. I put beef in it. You don’t like beef ramen?”

“That’s not what I mean, you punk.”

Bang!

Jinho hyung roughly set down his utensils.

Of course, he hadn’t done it to make a point. He was just full.

“I mean, you’ve got four billion won in your bank account, so why are you eating ramen in a goshiwon?[^1]”

“What’s it to you? I’ll do what I want.”

“…That’s true.”

“And the money only came in an hour ago, all right? I don’t know what to do with it either, so be quiet and let me think.”

I was pretending to be fine, but I had been dazed for a while. I had worked myself to the bone like a worker ant, but the money had always been earmarked for something.

Then a fortune had dropped out of the sky.

Four billion won was enough money to do a lot of things. Naturally, a lot of thoughts followed.

“What are you thinking so hard about? There must have been something you wanted to do first as soon as you got money.”

The thing I wanted to do first…

*There is one thing.*

Slurp.

After sucking in the last strand of noodles, I stood up.

Before leaving the room, I didn’t forget to leave Jinho hyung one parting remark.

“Thanks.”

“Don’t mention it.”

“Don’t forget to wash the pot. I’m off.”

“Hey, hey!”

* * *

“Huh?”

Hayeon’s eyes went round when she saw me standing in front of the front door.

“So it really is you. I saw you on the intercom screen and thought, no way.”

“…If it wasn’t really me, what would I be?”

“Hmm. A graphic?”

“Is that any way to talk to your older brother after not seeing him for so long?”

“What are you talking about? You came the day before yesterday.”

Ah, right. Not much time had passed in the real world.

The time difference was so large that I sometimes got confused myself. As I took off my shoes, I asked,

“What were you doing?”

“Studying.”

“Come to think of it, what about school? It’s a weekday.”

Hayeon answered in a nasal voice.

“They said my fever was thirty-nine degrees. I stuck it out until second period, then left early. Summer vacation starts tomorrow anyway, and we’ve been doing nothing but self-study lately.”

“You’re already on vacation? No, wait. You left school early because you were sick, and you’re studying?”

Somehow, she seemed more impressive than a Peak master. Whenever I got really sick at school, my illness mysteriously disappeared as soon as I left early and came home.

She had a raging fever, and she was still studying. Was her DNA different from mine?

“There is no end to learning.”

Leaving Hayeon, who sounded like a school disciplinarian, behind, I entered the living room. Apart from the two of us, there wasn’t a sign of anyone else in the house.

“Where’s Mom?”

“The bank.”

“You answered that awfully quickly.”

“It’s true.”

“Did Mom tell you to say that?”

“Huh? Tell me to say what?”

I wondered who she took after. Her acting was so natural that if I hadn’t known the truth, I would have been completely fooled.

*I should have told her long ago.*

A bitter smile escaped me before I could stop it. As I turned back toward the entrance, Hayeon grabbed me.

“Where are you going?”

“To find Mom.”

“There’s more than one bank around here. I’ll make you something to eat, so wait here. She’ll be back soon.”

“It’s fine. I’m not going to the bank.”

“What?”

“The restaurant at the intersection in front of the supermarket. Right?”

The strength slowly drained from Hayeon’s hand.

“…You knew?”

“Yeah. For a long time.”

“Mom asked me to keep it a secret.”

“I know that too.”

“Oppa, can’t you stay?”

It was one of Hayeon’s longtime habits. Whenever she had an important favor to ask, she always put *oppa* first.

“I’ll be back.”

I ruffled Hayeon’s hair and left the house.

As the elevator carried me down, I quietly thought about her warmth still lingering in my hand—and why she was studying even while her forehead was burning up.

* * *

A person had only one name written on their resident registration card, but they could be called by many names over the course of their life. Kim Jeonghee, who had turned exactly fifty that year, was no different.

“Ajumma, two more servings of pork belly over here.”

“Yes, just a moment.”

The name she was called most often these days was *ajumma*.[^2] Before that, it had been “Hayeon’s mom.” Before that, “Taekyung’s mom.” Once the children had grown up and work had become busy, those names had disappeared from her life.

The one person who had called her by her real name had already passed away long ago.

*Jeonghee.*

She had met him when she was twenty-two. He had been kind and affectionate. During the chaotic period of the Great Cataclysm, the two of them met in a shelter and fell in love at once.

It had been a happy marriage. Even as the years passed, he continued to call her by name.

*Jeonghee.*

Sometimes, embarrassed to hear him call her by name in front of other people, she had asked him about it.

*Why do you only call me Jeonghee? Other husbands call their wives “so-and-so’s mom,” “honey,” or “the missus.” That’s what everyone else does.*

*Does it bother you?*

*No, it’s not that. I was just curious. We’re getting older too.*

*What does age have to do with it? I call you Jeonghee because I love you as Jeonghee more than I love you as Taekyung’s mom.*

*Why are you acting like this in front of the kids?*

*Uh-oh, Mom’s cheeks are red. Mom and Dad, do you wrestle in the mornings too? You do it every night.*

*…Taekyung, starting today, go to bed early.*

Their parting came earlier than expected. Without warning, a Gate opened in the middle of downtown. The two children lost their father, and she lost her husband—the one person who had been the only one to call her by name.

“Ajumma!”

Kim Jeonghee jolted back to reality. A middle-aged woman with permed hair and flashy earrings was glaring at her.

“Oh, yes, ma’am.”

“What were you doing that you couldn’t even hear me calling you?”

“I’m sorry.”

“What about the grill plates? Are you done washing them?”

“Well, the thing is…”

Her hands had stopped while she was lost in thought. The owner checked the sink and raised her eyes sharply.

“Ajumma, are you going to work like this?”

“…”

“Honestly. If this is how you’re going to do things, I should do it myself. Why would I pay good money to hire you? Am I wrong?”

Kim Jeonghee lowered her head, while the other kitchen workers continued what they were doing, pretending not to hear the owner’s voice.

*Good money, my ass. She works us at minimum wage during the busiest hours.*

*She’s old enough to know better. She knows perfectly well that no amount of caked-on makeup and dressing up will make her a match for Jeonghee ajumma, so she’s taking it out on her.*

*She should watch the counter properly herself in the first place. How many orders did Jeonghee receive while she was off having fun?*

There were many things they wanted to say, but they could only keep them to themselves. The kitchen ajumma who had finally lost her patience and stood up for Kim Jeonghee had been fired last week.

“Can I really leave this place with you in charge?”

“…I’m sorry.”

“I heard your son is a Hunter. He should be making decent money, so why don’t you just stay home and cook? Why come all the way here and be a nuisance to someone else’s business? Ah, is his income not very good because he’s an F-rank Hunter?”

The moment a sneer appeared at the corners of the owner’s mouth, Kim Jeonghee slowly raised her bowed head.

“Boss. That was too much.”

“What?”

“I said you went too far.”

“Are you saying I was wrong?”

“Yes.”

The unfamiliar sensation left the owner speechless. Kim Jeonghee had always been quiet and gentle, but now her eyes had sunk into a deep, cold stare.

“Please apologize for what you just said.”

“A-apologize?”

“Right here. Right now.”

“O-oh my. Fine. Which part of what I said was wrong? Your son really is an F-rank Hunter!”

“Is his rank really that important?”

“Of course it is. What good is an F-rank Hunter? A son like mine has to make good money and have women lining up for him. This shop, too…”

“Your son, the D-rank Hunter, set it up for you. I know. I’ve heard it dozens, if not hundreds, of times.”

The employees, who had pricked up their ears, unconsciously nodded.

The owner’s boasting about her son was a familiar routine they heard several times a day.

How much he made, how big his house was, what kind of car he drove, and how filial he was—so filial that he had even opened a shop for his mother to have something to do. She had repeated it so often that even the regular customers were sick of hearing it.

“Then you know all about it. I run this place as a hobby, but you’re different, aren’t you? You’re working in the kitchen because your son doesn’t make enough money, aren’t you?”

“No, that’s not it.”

Kim Jeonghee continued calmly.

“Our Taekyung grew up right. He never once caused his parents any trouble, even when he was little. He’s still working hard for his family. Money? He earns more than enough.”

“That’s all an excuse.”

“An excuse? This is money my child earned by risking his life. How could I, as his parent, accept it and spend it?”

“Ajumma, are you saying that for my benefit?”

“That depends on how you choose to take it. And since we’re on the subject, when does that amazing son of yours ever show his face?”

“What?”

“I’ve worked here for over a year, but that devoted son of yours hasn’t visited even once. He does at least call you, doesn’t he?”

The kitchen fell silent as death. The owner’s face turned bright red, and her eyes widened.

“Where does a bitch with such a pathetic son get off—”

The employees knew what was coming next. Along with the owner’s machine-gun burst of abuse, the word “fired” was bound to come flying out.

But none of them could have predicted Kim Jeonghee’s reaction.

“Watch your mouth, you goddamn bitch.”

“…”

“…”

It was as if a bomb had gone off.

A deathly silence descended, and everyone’s eyes shook with disbelief. Every person in the kitchen wondered if they had heard correctly.

*What did I just hear?*

*Did Jeonghee ajumma just swear? My God.*

Kim Jeonghee had always been gentle and quick to smile. Even though the owner picked fights with her day after day, she had always bowed her head without a single word of complaint. Now she was glaring at the owner with eyes as cold as ice.

“W-what did you say? What did you just call me?”

“I called you a goddamn bitch, you fucking bitch.”

“Y-you fucking bitch?!”

Before the shock had even faded, a second bomb went off. The owner’s shriek rang all the way out into the dining area.

“Did someone just swear?”

“You heard that too? I think someone just called somebody a fucking bitch.”

“What the hell? Are the employees fighting?”

The murmuring grew louder. Customers and employees alike turned their attention toward the kitchen.

That was when it happened.

Thud. Thud. Thud.

A large young man with his cap pulled low. No one had noticed when he entered, or how long he had been standing there. Not until he started walking toward the kitchen.

“S-sir. I’ll take your order…”

The young man smiled faintly at the male employee who hurried to stop him.

“It’s okay. I didn’t come to order.”

“No, but still, right now…”

“Excuse me.”

Tap.

He had only given the employee a gentle push, but the burly man staggered and fell. The young man pushed open the half-open kitchen door without hesitation.

And then…

“Mom.”

He came face-to-face with the person he loved most in the world.

[^1]: A goshiwon is a tiny, inexpensive room-for-rent housing arrangement, often with shared facilities.

[^2]: *Ajumma* is a familiar Korean term for a married or middle-aged woman, commonly used by customers or employers to address service workers.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 87`.

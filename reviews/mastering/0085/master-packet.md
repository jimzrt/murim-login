# Master Edit Task — Chapter 85

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
| 혁무진    | **Hyuk Mujin**     |
| 최민우    | **Choi Minwoo**   |
| 송송이    | **Song Song**     |
| 임창수    | **Im Changsoo**   |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
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
| 대격변     | **Great Cataclysm**   |
| 임꺽정 | **Im Kkeokjeong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
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
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
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

#### Chapter 83 tail (verified mastered)

…
Kkeokjeong gaping. *Why’s this bastard such a big spender?* He was the team leader of a mid-sized Guild and a B-rank Hunter, so he probably earned a lot. But casually offering billions of won like this was absurd. “You’re giving me four billion just like that?” “Just? That won’t do. This is a bet.” “What kind of bet?” “I need something to gain, too.” The corners of Im Changsoo’s lips twisted upward. “If you die or run away, every reward I’ve offered so far is void. On top of that…” His head slowly turned. His gaze stopped on one person. “Me?” “Yes. I’d like to invite Miss Song Song to join our Guild.” Im Changsoo bowed politely. The sudden change in attitude was so different from how he had acted until now that it was downright creepy. “Ugh, that’s giving me goose bumps. Just act the way you were before. It looks much better than putting on a fake act.” “…” “…” Miss Song-i certainly had an honest personality. She shuddered as if she really had gotten goose bumps, then folded her arms. “Shit Chang—no, Im Changsoo, right?” “…Yes.” “Okay. I’ll be blunt. You’re not my type.” Her blunt declaration came in like a 160-kilometer-per-hour fastball, tight and inside. Im Changsoo’s gaze wavered. “You’re tall and handsome, but you look exactly like the cheating type. And I hate wind, you see.[^1] I finally got my hair looking nice, and if the wind musses it up… Ah, no, that’s not what I meant, was it?” “Y-yes? Yes?” “Anyway, you’re not my type. I absolutely can’t stand womanizers who flaunt their money.” I had never seen Im Changsoo look so dumbfounded. To anyone else, I probably had the same expression right now. “Oh, that look you just had was kind of okay. But I’ve been watching you for a while, and your personality is kind of… You can tell that yourself, can’t you?” Im Changsoo barely managed to compose his expression before answering. “We can work those things out one by one.” “Do you really have to taste something to know whether it’s shit or soybean paste? You don’t seem interested in anything but bumping bellies with me. Am I right?” “…!” “…!” Everyone, myself included, was left gaping. She toyed with her hair as if bashful while delivering one line after another, each blow landing like a nuclear bomb. “It’s not like I particularly dislike the Sangdong Guild.” Im Changsoo, who had been taking hit after hit without a break, brightened and asked: “Really?” “Yes. I can always switch again anyway.” “…” *Miss Song, are you a genius?* After delivering a massive fuck-you with an innocent expression, Miss Song continued. “But I’d need to ask permission before switching Guilds. Right, Guild Master?” “Ah, of course.” Butler Kim had been watching with an interested look in his eyes. Miss Song turned toward Team Leader Choi. “Team Leader, what do you think?” “What do you mean? About you switching Guilds?” “If we lose this bet, that’s what will happen, right?” Team Leader Choi calmly nodded. “Go ahead.” “Isn’t that a little too easy an answer?” “It was an easy question, so I answered easily.” For just a moment, I thought I saw hurt in Miss Song’s eyes. *No, surely not.* The emotion had passed too quickly for me to be certain. Returning to her frank, easygoing self, Miss Song turned to Im Changsoo. “Then I’m in on the bet. What about you, Mr. Taekyung?” “I…” I thought it over for a while. From the moment I first heard Team Leader Choi’s question, a strange certainty had already taken root deep in my heart. The certainty that I was stronger than those bastards. “I’ll take the bet.” A smile spread across Team Leader Choi’s lips. “I’ll join in, too. A bet is more fun when the stakes are high, isn’t it?” “Wow, look at you. A real gambler. How much?” “Four billion won. Of course, I’m betting that Jin Taekyung will take down all eight.” “What?” Im Changsoo stared at Team Leader Choi for a moment, then let out a short laugh. “You’re an interesting bunch. One of you is desperate to get himself killed, and the other is dying to throw away his money.” “So what’s your answer?” “Obviously, yes.” “Should we write up a contract?” “A contract? What do you take me for? Once I give my word, I keep it. You don’t have to keep yours. I’ll make you keep it. Everyone, move back!” At that moment, the enormous, damp cavern transformed into a Colosseum. An arena with an absurd amount of money at stake. And I was the gladiator who had to fight the Minotaur herd. “Team Leader Choi. What will you do if I lose?” “You will win.” Where did that confidence come from? Faith in himself? Or faith in what he’d seen of me so far? It didn’t matter. I would simply do my best to achieve my goal. *Boom-boom-boom-boom-boom!* —Moooooo! Twenty meters ahead, I could see every one of them clearly. Hot breath steaming from their nostrils. Heat. Muscles. Weapons held high. *This is my first time fighting a cow.* It should be an interesting experience. I gripped my spear and charged at the herd like a bullfighter. [^1]: The Korean word *baram* can mean either “wind” or an affair, making her next line a deliberate pun.

#### Chapter 84 tail (verified mastered)

…
“Im Chunsu.” “What’s the Sangdong Guild Master’s name?” “Im Chunsu.” What a strange coincidence. Im Changsoo’s father and the Sangdong Guild Master had the same name. Then again, the world was a big place, and plenty of people shared the same name. “Hey, I’m only asking just in case, so forgive me for prying… but what does your father do for a living?” “He’s a Hunter.” “Just a Hunter?” “He runs a Guild.” “Oh, I see.” This bastard was the Sangdong Guild Master’s son. A brief silence passed, and in that short interval, I realized what had seemed so familiar about Im Changsoo. “Are you that guy?” “A dog?” “No, I’ve heard about you before.” It was a story I’d heard around this time two years ago and let go in one ear and out the other. The Sangdong Guild Master’s only son, born late in his life, had awakened as a B-rank Hunter and secured a position in his father’s Guild. But he was such a womanizer that he had become a constant headache. And the nickname he had earned was… “Horndog. Right?” Im Changsoo answered by hanging his head. It was an embarrassing nickname to hear in front of other people, to be sure. But since I had to collect four billion won, I comforted him in a warm voice. “It’s okay, man. Guys can be like that sometimes. I used to dream of living like you, too.” But reality was cruel, and that dream had seeped into a hundred-terabyte USB drive. Jinho hyung, a renowned authority in the world of porn, once borrowed my USB. When he showed up again, he had a hollow-eyed expression and left me with a one-line review. *This should be designated a UNESCO World Heritage Site.* Anyway. Im Changsoo lifted his head at my warm consolation. “Really?” *Of course not.* Did I look like the kind of guy who hit on just any woman? I was the sunflower of this era, gazing at only one person in the entire world—Miss Song-i… *Wait a second.* This bastard had hit on Miss Song-i earlier. “You little shit.” “Ack!” Frightened before I had even done anything, Im Changsoo reflexively placed his hand on his sword hilt. Shing. Clack. But the blade had barely made it halfway out before it was forced back into its sheath. I had closed the distance like lightning, pressing down on his sword hilt as I kicked his legs out from under him. Crash! He lost his balance and fell. When I pressed down on his neck, his face went white. “Ghk! Cough!” “You little bastard. Where do you get off pulling that thing on me?” Getting beaten by Jin Mukyung had certainly paid off. In the past, I wouldn’t have been able to subdue a B-rank Hunter with such a simple, fluid movement. Im Changsoo was probably surprised, but I was even more surprised. “This is a Gate, you idiot. You said so yourself earlier. Did you already forget?” “I’m sorry! I’m sorry!” I wanted to beat him senseless, but since it had only been an attempt, I decided to let him off. *It absolutely wasn’t because I hadn’t received the four billion yet.* “Damages.” “Ghk. What?” “You drew your sword. Don’t you know that’s attempted murder? And you owe me and Miss Song-i—no, all our Guild members—a sincere apology.” “What are you talking about?” Im Changsoo looked around at the others with an aggrieved expression, but no one came to his aid. His team members merely shrank back whenever my gaze landed on them. Meanwhile, our Guild members, who had been watching the spectacle, took it one step further. “Drawing a sword on a member of a partner Guild. Well, I never.” Butler Kim clicked his tongue as if he felt sorry for him. “You’re only doing this because you don’t want to pay, aren’t you? My goodness, Changsoo, that’s so low. Isn’t it, Uncle?” “Hmm? Uh-huh. What a nasty young man!” Miss Song and Im Kkeokjeong delivered a lowlife-and-nasty-man combo. Then Team Leader Choi dealt the final blow. “Now, would everyone take a look at my helmet? This product is a custom-made helmet produced by Xyliton, a famous Finnish equipment manufacturer. It has all sorts of functions, but most importantly, it has been enchanted with a video-recording spell…” Im Changsoo stared at everyone with his mouth hanging open, betrayed and utterly dumbfounded. Then he let out a long sigh. “I’ll do it.” “What did you say?” “I said I’ll do everything you tell me to!” That was the answer I had been waiting for. I happily helped him back to his feet. “Good choice, kid. We can discuss the damages at our leisure.” “…This is driving me crazy. If my boomer finds out, I’m dead.” “Would you rather die here?” “You don’t want the four billion?” “You’ve got some nerve.” Im Changsoo let out another deep sigh before speaking. “May I ask one question?” “One hundred million per question.” “…” “I’m kidding. Go ahead.” “What do you really do?” Was he really that curious? I let out a quiet laugh and answered him. “Someone with two jobs.” A Hunter and a Murim martial artist. The only two-job combination in the world. [^1]: *Hongik Ingan*, meaning “to broadly benefit humanity,” is Korea’s national founding ideal. Taekyung twists the opening sound *hong* into a joke about Im Changsoo’s reddening face.

## Korean source

```text
＃85화



“형. 괜찮으세요?”

“안 다치셨어요?”

팀원들의 말에 임창수가 이를 악물었다.

“입 닥쳐, 이 새끼들아. 그동안 내가 해 준 게 얼만데 구경만 하고 있어?”

“아니, 저 그게…….”

“그때 상황이 좀 그랬어요. 죄송해요.”

“의리 없는 새끼들.”

팀원들과 의리로 묶인 관계는 아니지만 그래도 줄 건 주고, 받을 건 받았다고 생각했다. 훈련소 낙제생들을 억지로 길드에 꽂아 넣고, 차도 사 주고 용돈도 준 게 누군가.

그 대가로 충성을 받았는데…… 가장 중요한 순간에 외면당하니 뒤통수가 얼얼했다.

‘시발, 뭐 이런 엿 같은 경우가.’

수십 억? 분명 큰돈이긴 하지만 임창수로서는 감당 못 할 금액은 아니었다. 그의 명의로 잡힌 건물 한두 개만 팔아도 충분히 지급할 수 있다.

그러나 자존심이 짓밟힌 건 도저히 용납할 수 없었다.

‘쳐 죽일 놈.’

임창수가 부릅뜬 눈으로 한 사람의 등을 노려봤다.

검은 가죽 갑옷을 입고 있는 저놈, 진태경이 모든 일의 원흉이다.

‘어디서 뭐 하다 온 놈인지는 모르겠지만…… 이 치욕은 반드시 갚아 주마.’

놈의 정체가 뭔지는 아직 정확히 모르겠다. 확실한 건 결코 평범한 C급 헌터는 아니라는 거다.

B급 몬스터 여덟 마리를 정면 승부로 박살 낼 수 있는 C급 헌터는 세상 어디에도 없으니까.

‘정체는 왜 숨긴 거지? 혹시 도피 중인 범죄자? 아니면 부정 등록자? 일단 게이트에서 나가기만 하면 싹 다 털어 주마.’

임창수가 은밀히 복수심을 불태우고 있던 그때였다.

휙!

돌연 그쪽으로 고개를 돌린 진태경이 눈을 가늘게 떴다. 먹이를 바라보는 포식자의 눈빛에 임창수의 가슴이 덜컥 내려앉았다.

“야.”

“예, 예?”

“너 방금 내 욕 했지.”

“아, 아, 아닌데요.”

“아니긴. 말 더듬는 것만 봐도 사이즈 나오는데. 어쩐지 아까부터 뒤통수가 따끔따끔하더라.”

임창수는 대격변 시대의 헌터이자 전쟁 영웅인 아버지의 말씀을 떠올렸다. 위험한 상황일수록 의연하게 대처해라.

“진짜 아닙니다.”

“내 관심법은 네가 거짓말을 하고 있다고 알려 주는데?”

“관심법이라니, 그런 게 어디 있어요?”

“마법도 있는데 관심법이 왜 없어. 구태의연한 사고방식을 버려.”

“어쨌든 맹세코 아닙니다.”

“아냐. 맹세코 맞아. 그리고 너도 한 대 맞아.”

빡!

눈물이 핑 돌았다. 스무 살 이후로는 아버지한테도 맞아 본 적이 없는 꿀밤이다. 그런데 기껏해야 또래로 보이는 놈한테, 그것도 팀원들과 여자들 앞에서 이런 굴욕을 당하다니.

“제법 손맛이 있네. 딱 혁무진 때릴 때 느낌인데, 이거. 아무튼 조심해라. 응?”

혁무진이 누군지는 모르겠지만 어쨌든 임창수는 고개를 푹 숙였다.

“……예.”

“근데 이놈의 미로는 끝도 없네. 야, 여기 보스 존 얼마나 남았어?”

“저도 몰라요. 미로라서.”

“몬스터도 더 이상 안 나오고. 심심해 죽겠다.”

“…….”

보이는 족족 때려잡으니까 안 나오지!

임창수와 팀원들이 나설 필요도 없었다. 저 다섯 명만으로도 충분, 아니 진태경 한 명으로도 충분했다.

‘괴물 같은 놈. 진짜 A급 헌터라도 되나?’

진태경 혼자서만 서른 마리는 넘게 쓰러트린 것 같다. 좀 지쳤나 싶다가도 어느 순간을 기점으로는 또 펄펄 날아다녔다.

‘레이드 속도가 더 빨라지고 있어.’

보통은 레이드의 끝으로 갈수록 피로 축적으로 느려지는 게 정상이다.

그런데도 같은 몬스터를 상대하는데 레이드 속도가 빨라진다는 건…….

‘계속해서 강해진다?’

임창수는 순간 떠오른 생각을 애써 부정했다.

무슨 게임 캐릭터가 레벨 업 하는 것도 아니고 그게 말이 되나. 꿀밤을 맞더니 머리가 고장 난 기분이다.

“후우.”

깊은 한숨을 내쉬는 그에게 팀원들이 우물쭈물 다가왔다.

“창수 형…….”

“오빠, 괜찮아? 어떡해. 이마에 혹 났어.”

“기분 안 좋으니까 다 꺼져. 너희는 나가기만 하면 싹 다 모가지야. 알아?”

아무리 체면을 구겨도, 이빨이 뽑혀도 호랑이는 호랑이다.

임창수의 으름장에 팀원들이 숨을 삼켰다.

‘할부 안 끝났는데.’

‘상동 길드 나가면 어디에서 받아 주나.’

‘이번 달 카드값이…….’

이제껏 풍족한 생활을 영위할 수 있었던 이유는 임창수의 원조 덕분이다. 그들 모두 헌터니만큼 굶어 죽을 일은 없겠지만 어디를 가도 지금 같은 대우는 기대하기 어렵다.

“거기서 끝낼 줄 알아? 기대해. 어딜 가더라도 상동 길드 이름으로 전화 한 통씩 꼭 넣어 줄 테니까. 이 바닥 좁은 거 알지?”

쫓아내는 것도 모자라 앞길까지 방해한다는 말에 팀원들의 얼굴이 급변했다.

“창수 형, 그건 좀.”

“형? 너 좋을 때만 형이냐?”

“오빠, 꼭 그렇게까지 해야겠어?”

“그러니까 이 자식들아. 사람 잘 보고 줄을 댔어야지.”

당장 모두 뺨이라도 한 대씩 올려붙이고 싶었지만 꾹 참았다.

큰 소리를 냈다가는 언제 또 진태경이 돌아볼지 모르기 때문이다.

‘시발, 내가 어쩌다가…….’

꿀밤이 무서워서 화도 마음대로 못 내는 꼴이라니. 임창수가 바닥에 침을 탁 뱉고 돌아선 그때였다.

덥석.

“창수 형. 아니 임 팀장님, 이러시면 어떡해요.”

“한 번만 다시 생각해 줘, 오빠. 응?”

“놔라. 두 번 말하기 싫다.”

“이번엔 진짜. 진짜로 시키는 거 다 할게요. 예?”

“……시키는 거 다 한다고?”

동료의 손을 뿌리치려던 임창수가 문득 동작을 멈췄다.

힐끗 고개를 돌리니 길드원들과 실랑이를 벌이는 사이 거리가 벌어져 저 멀리 앞서가는 진태경 일행이 보인다.

멀리서도 눈에 띄는 송송이의 환상적인 뒤태도.

‘잠깐. 방법이 있을 것 같기도 한데.’

그의 눈에 비친 진태경은 괴물이지만 딱 한 가지 약점이 있어 보였다. 송송이라는 여자.

‘아까 보니까 완전 뻑이 갔던데.’

눈치채고 말고 할 것도 없다. 누구나 한 번 본 것만으로도 그가 송송이를 마음에 품고 있다는 사실을 알아차릴 수 있을 정도니까.

‘분명 C급 힐러라고 했지.’

힐러를 제압하는 것은 닭목 비트는 것보다 쉽다. 좋아하는 여자가 붙잡혀 있다면 진태경도 쉽게 손을 쓸 수 없을 것이다.

‘그럼 끝이지.’

진태경을 제외하면 나머지 셋은 큰 걱정거리가 아니다.

길드장이라는 노인네는 B급이지만 마법사라 근접전은 쥐약일 테고, E급 탱커인 아저씨는 논할 가치도 없다.

약간 마음에 걸리는 사람이 있다면 최민우. 그놈인데…….

“방금 그 말, 믿어도 되냐?”

“물론입니다.”

“저희만 믿으세요.”

“오빠, 사람을 왜 이렇게 못 믿어? 우리가 이 정도 사이밖에 안 돼?”

그에겐 명령에 복종할 B급 헌터 넷과 C급 헌터 다섯으로 이루어진 레이드 팀이 있다. 모두 임창수가 주는 먹이만 먹도록 길들여진 녀석들이다.

“좋아. 그럼 지금부터 내가 하는 말 똑똑히 들어…….”

짤막한, 그리고 간단한 설명이 끝나자 팀원들은 긴장된 기색을 숨기지 못했다.

“될까요?”

“가능성 있어 보이기는 하는데.”

“오빠, 설마 내가 생각하는 그거, 아니지? 사람 죽이는 거면 나는 좀.”

“시키는 대로 다 한다고 하지 않았냐?”

“그래도 그건 좀…….”

“됐어. 마음 같아서는 그러고 싶지만 내가 그 정도로 막 나가는 놈은 아니야. 일단 카메라 뺏고, 저 빌어먹을 놈한테 씻지 못할 굴욕을 안겨 줘야지.”

“휴우. 다행이다. 그럼 난 무조건 오빠 편이지.”

“잘해. 이번에 망설이거나 조금이라도 뒤로 빼는 놈 있으면 알지?”

“당연하죠.”

“저희만 믿으십쇼, 팀장님. 아니, 형님. 헤헤.”

임창수의 입가에 비릿한 미소가 맺혔다.

‘내 자존심을 짓밟았으면 그만한 대가를 치러야지.’

곧 나오는 보스 존(Boss Zone)에서 겁도 없이 누굴 건드렸는지 똑똑히 깨닫게 해 줄 생각이었다.

마침 진태경에게 대적할 만한 몬스터도 그곳에 있다.

‘미노타우로스 대전사.’

이곳, ‘미노타우로스의 미로’의 보스 몬스터.

B급 몬스터 주제에 육체 능력만큼은 A급에 맞먹는다는 괴물 같은 놈이다.

‘대전사가 놈의 힘을 소진시키면 그때 결행한다.’

이이제이(以夷制夷).

오랑캐는 오랑캐로. 괴물은 괴물로 물리친다.

양쪽 모두 지친 그때가 바로 기회다. 어이없이 잃게 될 돈도, 땅에 떨어진 자존심도 한 번에 회복할 수 있다.

“야, 빨리 와! 보스 존이잖아!”

다음 순간 진태경의 외침이 들려왔다. 임창수가 활짝 웃었다.

“예! 갑니다!”

보스 존을 향해 걸어가는 그의 발걸음은 경쾌하기 그지없었다.



* * *



“일섬(一殲).”

콰아아아.

창날 끝에서 하늘이 쪼개지는 소리가 났다. 닿는 모든 것을 찢고 집어삼키는 백색 와류가 근육질의 가슴에 닿았다.

- 모오?

콰드드득.

살았는지, 죽었는지 굳이 확인할 필요도 없었다.

놈의 가슴에서 창을 뽑아낸 순간 시스템 알림이 울렸으니까.

띠링.



- [Lv.70 미노타우로스 대전사]를 처치했습니다!

- 레벨 업!

- 퀘스트, [B급 게이트 클리어]를 완료했습니다!

- 당신의 기여도를 계산 중입니다…… 완료되었습니다!

- 퀘스트 성공 보상이 인벤토리로 지급됩니다!



“휴우.”

역시 마지막은 큰 거 한 방이지. 몸이 엄청 피곤하긴 하지만. 나는 창에 묻은 피를 털며 돌아섰다.

“빨리 부산물 챙겨서 나가죠. 배고파 죽겠…… 다들 왜 그러세요?”

임꺽정이 대표로 입을 열었다.

“그걸 몰라서 묻냐?”

그가 죽은 보스 몬스터의 사체와 나를 번갈아 바라봤다.

한 방에 B급 보스 몬스터를 끝장냈으니 무슨 변명이라도 해보라는 눈빛이다.

“음, 운이 좋았던 걸로 해 두죠.”

“운?”

“네, 운.”

정말 운이 좋아서다.

내가 고시원에 살았던 것도, 고시원 앞에 캡슐이 버려진 것도. 전부 다.

“허허, 기가 차서 말도 안 나오는구먼. 됐다.”

다른 사람들도 임꺽정과 비슷한 반응이다. 이미 나와 레이드를 경험한 적 있는 최 팀장도 어안이 벙벙한 표정으로 한마디를 건넸다.

“이 정도일 줄은 몰랐습니다만.”

“지금 알면 됐죠.”

“이에 관해 대화를 나눌 수 있을까요?”

“물론입니다.”

지금은 아니고, 나중에. 더 중요한 볼일이 남았거든.

나는 최대한 매력적인 미소를 지으며 한 사람에게 다가갔다.

“송이 씨, 저 힐 좀 부탁드려도 될…… 너희들은 거기서 뭐 하냐?”

“아.”

“뭐냐고. 왜 여기 있어?”

“그냥, 그냥 있는데요.”

“저, 저는 언니가 너무 예쁘셔서.”

송이 씨 옆에 붙어 있던 상동 길드원들이 화들짝 놀라며 아무 말 대잔치를 시작한다.

‘뭐야, 이것들.’

나랑 송이 씨 사이에서 방해되니까 꺼지란 소리였는데. 내가 그렇게 무섭게 보이나?

“임창수 어디 있어?”

한마디에 상동 길드원들이 홍해처럼 쫙 갈라졌다. 임창수가 백지장처럼 하얀 얼굴로 대답했다.

“여기 있습니다.”

“너 얼굴 왜 그래? 어디 아파?”

“모, 몸살 기운이 조금.”

“쯧쯧. 포션도 챙겨 먹고 그래, 인마. 너 집에 돈 많잖아.”

“…….”

“어쨌든 빨리 부산물 수거하고 가자. 피곤하다.”

“네, 넵.”

임창수가 방해꾼들을 데리고 사라지자 기다렸던 순간이 찾아왔다. 나는 송이 씨를 향해 활짝 웃어 보였다.

“배고프시죠? 저녁으로 근사한 레스토랑에서 스테이크 어떠세요?”

송이 씨도 나를 따라 웃었다.

“죄송하지만 제가 채식주의자라.”

“이상하네. 어제 고기 잘 드셨던 것 같은데. 그럼 샐러드 바 가실래요?”

“제가 육식주의자라.”

“…….”

이거 까인 거 맞지?
```

## Current accepted English baseline

```markdown
# Chapter 85

“Changsoo hyung. Are you okay?”

“Were you hurt?”

At his team members’ questions, Im Changsoo clenched his teeth.

“Shut up, you bastards. After everything I’ve done for you, you’re just standing around watching?”

“No, it’s just…”

“The situation was a little complicated then. I’m sorry.”

“You disloyal bastards.”

They weren’t bound together by loyalty, but Im Changsoo thought he had given them what they were due and received what he was owed in return. Who had been the one to force the training-camp washouts into the Guild, buy them cars, and give them spending money?

He had received their loyalty in exchange…but being abandoned at the most important moment felt like a stinging blow to the back of the head.

*Fuck, what kind of bullshit is this?*

Several billion won? It was certainly a large amount of money, but it wasn’t beyond Im Changsoo’s means. He could pay it in full by selling just one or two buildings registered under his name.

But he couldn’t tolerate having his pride trampled.

*That bastard deserves to be beaten to death.*

Im Changsoo glared at one person’s back with wide-open eyes.

That bastard in the black leather armor—Jin Taekyung—was the root cause of everything.

*I don’t know where he came from or what he was doing before this…but I’ll make him pay for this humiliation.*

He still didn’t know exactly what Taekyung’s identity was. The one thing he knew for certain was that Taekyung was no ordinary C-rank Hunter.

There wasn’t a single C-rank Hunter in the world who could crush eight B-rank monsters in a head-on fight.

*Why is he hiding his identity? Is he a fugitive criminal? Or someone with a fraudulent registration? The moment we get out of this Gate, I’ll dig up every last thing about him.*

It was at that moment that Jin Taekyung suddenly turned his head toward him and narrowed his eyes.

The predator’s gaze, fixed on its prey, made Im Changsoo’s heart drop.

“Hey.”

“Y-yes?”

“You were just cursing me in your head, weren’t you?”

“N-no, I didn’t.”

“Don’t give me that. The way you stammered gives it away. No wonder the back of my head has been prickling since earlier.”

Im Changsoo recalled the words of his father, a Hunter and war hero from the Great Cataclysm era.

*The more dangerous the situation, the more calmly you have to deal with it.*

“I really didn’t.”

“My mind-reading technique says you’re lying.”

“Mind-reading? There’s no such thing.”

“There’s magic, so why not mind-reading? Let go of your hidebound thinking.”

“Regardless, I swear I didn’t.”

“No, I swear you did. And you’re getting one too.”

Bonk!

Tears sprang to Im Changsoo’s eyes.

It was a forehead flick. He hadn’t even been hit by his father since turning twenty. And now, in front of his team members and several women, he had suffered this humiliation at the hands of someone who looked barely his age.

“Not bad. The feel is exactly like when I hit Hyuk Mujin. Anyway, watch yourself, okay?”

Im Changsoo didn’t know who Hyuk Mujin was, but he lowered his head anyway.

“…Yes.”

“But this damn labyrinth really doesn’t end. Hey, how much farther to the Boss Zone?”

“I don’t know. It’s a labyrinth.”

“And no more monsters are coming out. I’m bored to death.”

“…”

*Of course they aren’t coming out when you beat down every single one you see!*

Im Changsoo and his team didn’t even need to step in. Those five were more than enough. No, Jin Taekyung alone was enough.

*What a monster. Is he really an A-rank Hunter?*

Taekyung alone seemed to have brought down more than thirty monsters. Just when it seemed like he was getting tired, he would suddenly start flying around again.

*The raid is getting faster.*

Normally, a raid slowed down toward the end as fatigue accumulated.

But the raid was getting faster even though they were fighting the same monsters…

*Is he getting stronger the whole time?*

Im Changsoo desperately rejected the thought that had flashed through his mind.

*What is he, a game character leveling up? How could that make any sense?*

Getting hit on the forehead must have broken his brain.

“Hoo.”

As Im Changsoo let out a deep sigh, his team members approached him hesitantly.

“Changsoo hyung…”

“Oppa, are you okay? What do we do? You’ve got a bump on your forehead.”

“I’m in a bad mood, so get lost. The moment you leave, you’re all fired. Got it?”

No matter how badly his dignity had been crushed, even a tiger with its teeth pulled was still a tiger.

His team members swallowed nervously at Im Changsoo’s threat.

*My car payments aren’t even finished.*

*Where will I get accepted if I leave Sangdong Guild?*

*My credit-card bill this month…*

The reason they had been able to enjoy such comfortable lives was Im Changsoo’s support. Since they were all Hunters, they weren’t going to starve to death, but wherever they went, it would be difficult to expect the same treatment.

“You think you’re getting away with it just because you’re leaving? Just wait. Wherever you go, I’ll make sure to place a call in Sangdong Guild’s name. You know this field is small, right?”

At the threat that he would not only drive them out but also ruin their futures, their expressions changed completely.

“Changsoo hyung, that’s going too far.”

“Hyung? I’m only hyung when things are going your way?”

“Oppa, do you really have to take it that far?”

“That’s why you bastards should’ve picked the right person to hitch your wagon to.”

He wanted to slap every one of them across the face, but he forced himself to hold back.

If he raised his voice again, there was no telling when Jin Taekyung might turn around.

*Fuck, how did I end up…*

What kind of pathetic situation was this, being too afraid of a forehead flick to even get angry properly?

Im Changsoo spat on the floor and turned away.

That was when someone grabbed him.

“Changsoo hyung. No, Team Leader Im, you can’t do this.”

“Think it over one more time, oppa. Please?”

“Let go. I don’t want to say it twice.”

“This time, for real. I’ll do everything you tell me. Okay?”

“…Everything I tell you?”

Im Changsoo, who had been about to pull away from his colleague’s hand, suddenly stopped.

He glanced back and saw Jin Taekyung’s group far ahead of them. They had gotten some distance away while he was arguing with his Guild members.

Even from that distance, Song Song’s stunning figure from behind was impossible to miss.

*Wait. Maybe there is a way.*

To Im Changsoo, Jin Taekyung looked like a monster—but he seemed to have one weakness.

A woman named Song Song.

*He was completely smitten earlier.*

There was no need to be perceptive about it. Anyone could tell from a single glance that Jin Taekyung had feelings for Song Song.

*She said she was a C-rank healer, right?*

Subduing a healer was easier than twisting a chicken’s neck. If the woman he liked were being held hostage, Jin Taekyung wouldn’t be able to act freely.

*Then it’s over.*

Apart from Taekyung, the other three weren’t much of a concern.

The old man who was supposedly the Guild Master was a B-rank Hunter, but he was a mage, so close combat would be his worst area. The middle-aged man who was an E-rank tank wasn’t even worth discussing.

The only person who bothered Im Changsoo a little was Choi Minwoo. That guy…

“Can I trust what you just said?”

“Of course.”

“Just trust us.”

“Oppa, why don’t you trust people at all? Are we really only this close?”

Im Changsoo had a raid team made up of four B-rank Hunters and five C-rank Hunters who would obey his commands. They were all people he had trained to live solely on the scraps he handed them.

“Fine. Then listen carefully to what I’m about to say…”

After a short and simple explanation, the team members couldn’t hide their nervousness.

“Will it work?”

“It does seem possible.”

“Oppa, it’s not what I think it is, right? If you’re talking about killing someone, I’m not sure I can.”

“Didn’t you say you’d do everything I told you?”

“Even so, that’s a little…”

“Forget it. I’d like to do that, but I’m not reckless enough to go that far. First, we take the camera. Then we give that son of a bitch a humiliation he’ll never live down.”

“Whew. What a relief. Then I’m definitely on oppa’s side.”

“Do your best. You know what happens if anyone hesitates this time or holds back even a little, right?”

“Of course.”

“Just trust us, Team Leader. No, hyungnim. Hehe.”

A sinister smile spread across Im Changsoo’s lips.

*If he trampled on my pride, he has to pay the price.*

In the Boss Zone they were about to enter, Im Changsoo intended to make Jin Taekyung understand exactly whose toes he had stepped on.

There was even a monster there capable of standing against Jin Taekyung.

*The Minotaur Warrior.*

The boss monster of **The Minotaur’s Labyrinth**.

Despite being only a B-rank monster, it was a monstrous creature whose physical abilities rivaled those of an A-rank.

*Once the Minotaur Warrior wears him down, we’ll make our move.*

Set a barbarian against a barbarian.

Defeat a monster with a monster.

The moment both sides were exhausted would be their opportunity. He could recover both the money he was about to lose for no good reason and the pride that had been dragged through the dirt.

“Hey, hurry up! This is the Boss Zone!”

Jin Taekyung’s shout rang out the next moment.

Im Changsoo smiled broadly.

“Yes! Coming!”

His steps toward the Boss Zone were remarkably light.

* * *

“One Annihilation.”

Kraaaaaash!

From the tip of the spear came the sound of the sky splitting apart.

A white vortex that tore through and devoured everything it touched slammed into the muscular chest of the Minotaur Warrior.

—Moo?

Crack-crack-crack!

There was no need to check whether it was alive or dead.

The moment I pulled my spear from its chest, the System notification rang out.

Ding.

> **System**
>
> - Defeated **Lv. 70 Minotaur Warrior**!
>
> - Level Up!
>
> - Quest, **B-rank Gate Clear**, completed!
>
> - Calculating your contribution… Complete!
>
> - The Quest Success Reward has been deposited into your Inventory!

“Whew.”

The last one should always end with one big hit.

My body was incredibly tired, though.

I shook the blood from my spear and turned around.

“Let’s collect the byproducts and get out of here. I’m starving to dea—why are you all looking at me like that?”

Im Kkeokjeong spoke for everyone.

“You really have to ask?”

He looked back and forth between the dead boss monster’s corpse and me.

His eyes demanded some kind of explanation for how I had finished a B-rank boss monster with a single blow.

“Hmm. Let’s just say I got lucky.”

“Lucky?”

“Yes. Lucky.”

It really was because I had been lucky.

The fact that I had lived in a goshiwon.[^1] The fact that a capsule had been discarded in front of my goshiwon.

All of it.

“Good grief. I’m speechless. Fine.”

The others reacted much the same way as Im Kkeokjeong. Even Team Leader Choi, who had already experienced a raid with me, addressed me with a stunned expression.

“I didn’t expect you to be this capable.”

“If you know now, that’s enough.”

“Could we discuss this?”

“Of course.”

Not now. Later.

I still had something more important to take care of.

With my most charming smile, I approached one person.

“Miss Song, could I ask you for a heal—what are you guys doing over there?”

“Ah.”

“What are you doing? Why are you here?”

“We’re just… just standing here.”

“I-I just think she’s so beautiful.”

The Sangdong Guild members who had been standing next to Song Song jumped in surprise and began spouting all kinds of nonsense.

*What’s wrong with these guys?*

I only meant that they should get lost because they were getting in the way between me and Miss Song.

*Do I really look that scary?*

“Where’s Im Changsoo?”

At a single word from me, the Sangdong Guild members split apart like the Red Sea.

Im Changsoo answered from behind them, his face white as a sheet.

“I’m here.”

“What’s wrong with your face? Are you sick?”

“I-I think I’m coming down with something.”

“Tsk, tsk. Take a potion, you idiot. You’ve got plenty of money at home.”

“…”

“Anyway, hurry up and collect the byproducts. Let’s go. I’m tired.”

“Yes, yessir.”

Once Im Changsoo disappeared with the nuisances, the moment I had been waiting for finally arrived.

I smiled brightly at Song Song.

“You’re hungry, right? How about steak at a nice restaurant for dinner?”

Song Song smiled back at me.

“I’m sorry, but I’m a vegetarian.”

“That’s strange. I thought you ate meat just fine yesterday. How about a salad bar?”

“I’m a carnivore.”

“…”

*I got rejected, right?*

[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement, often used by students and people on tight budgets.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 85`.

# Master Edit Task — Chapter 12

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
| 혁무진    | **Hyuk Mujin**     |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 숙련도              | **Mastery**                    |
| 로그아웃             | **Logout**                     |
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 태원     | **Taiyuan**            |
| 대사      | **Master** for a senior Buddhist monk                           |
| 성진호 | **Seong Jinho** |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 5–9

## Plot

Taekyung completes the tutorial, learns that Logout requires First Rate, Lv. 30, and 500 Fame, and is taken to the Medicine King Hall after his fight with Hyuk Mujin. He begins cultivating the Jin Family’s Cultivation Technique, pretends that his memory has not returned, and discovers an unused room filled with martial arts manuals. The System reveals that martial arts occupy ten slots, three of which are already filled. Jin Wikyung and Wipeng catch him practicing footwork at night, but accept his explanation. In Chapter 9, Taekyung sorts the manuals, acquires the Jin Family’s Manoeuvre Technique, completes its achievement, and earns the title Novice Trainee. Seeking a proper place to practice, he asks for an empty room. Jin Wikyung instead orders his indefinite confinement in the training hall as a protective measure against the Elder Council’s coming attack. Wipeng secretly explains the plan through Sound Transmission and promises to release him within seven days; Taekyung negotiates that down to three days before being escorted away.

## Continuity

- Taekyung remains trapped in Murim; Logout and death rules remain unresolved.
- Logout requires First Rate, Lv. 30, and 500 Fame.
- He is practicing the Jin Family’s Cultivation Technique and has acquired the Jin Family’s Manoeuvre Technique; he has also located the Jin Family’s Spear Technique.
- His martial arts interface has ten slots, with three already filled.
- Taekyung continues pretending that his memory has not fully returned.
- Jin Wikyung is the Lesser Family Head and Taekyung’s protective older brother; Wipeng is his capable aide and can use Sound Transmission.
- The Elder Council is preparing to challenge Jin Wikyung’s authority by attacking Taekyung’s conduct.
- Taekyung is being held in the training hall for an indefinite period, with Wipeng promising release within three days after their negotiation.

## Translation Decisions

- The hereditary martial art is rendered **Jin Family’s Manoeuvre Technique**, using British spelling consistently with the chapter’s terminology.
- The achievement reward is rendered as the title **Novice Trainee**.
- `음성 전송` is rendered **Sound Transmission**.
- `소가주` is rendered **Lesser Family Head**.
- System messages remain grouped into `> **System**` blockquote windows whenever consecutive.

### Prior accepted reading-copy tails

#### Chapter 10 tail (verified mastered)

…
was no joke. By feel alone, the monster had to weigh close to fifty kilograms. My Stamina wouldn’t last if I swung something like this for hours. My current realm was Second Rate. Even with the System’s help, swinging around more than half a sack of rice as if it were a pinwheel was impossible. *It’s not like I suddenly have tiger power or something.* That was when it hit me. “…Huh?” What had I just said? The strength of a tiger? “I do have it.” This was a game. It had a System and stats. And I had internal energy. Ten years of internal energy that I could draw out through a cultivation technique! It was embarrassing that I had forgotten, even for a moment. “It’s not like I’ve ever used anything like that before…” They say you only know what something is like once you’ve experienced it. Was it any wonder an F-rank Hunter was F-rank? With barely any mana to speak of, I made do with my bare body. Even among Hunters, I was treated like a half-baked amateur. *Still, that solves one problem.* I let out a dumbfounded laugh, then picked up the spear. Slowly and carefully, I began drawing out my internal energy. The formula of the Jin Family’s Cultivation Technique, imprinted in my mind by the System, rewound rapidly through my thoughts, guiding my internal energy along its prescribed path. A prickling sensation ran through me. The response was immediate. The ten years of internal energy coiled in my dantian spread throughout my body. Because this was a game and I was a martial artist, I could feel it spreading through every part of me. *This is…* Power surged through my entire body. My vastly heightened physical abilities and senses once again brought exhilaration to someone who had spent his life as an F-rank Hunter. *How can a person change this much?* I gripped the spear and began practicing the *Jin Family’s Spear Technique*. The fifty-kilogram iron spear no longer felt heavy. It thrust and slashed through the air along the paths I wanted it to follow. Before long— Ding. > **System** > > - Successful attempts (6 / 100) The notification I had been waiting for began to ring. * * * Jin Wikyung spoke with a worried expression. “He’s doing well, right?” “He should be, if he has any sense of shame.” “He still hasn’t fully recovered… He’ll be all right, won’t he?” “Anyone who didn’t know better would think the Third Young Master was on death’s door. At that point, even spit would cure him.” “No. You only say that because you don’t know how frail the youngest has been since childhood.” Wipeng answered with an incredulous look. “The elixirs and tonics that have gone into the Third Young Master alone would be enough to fill an entire room. And have you already forgotten about the hundred-year snow ginseng theft last year?” “Ahem. That was…” “At the time, the Medicine King Hall Master was so furious that he ran around shouting that he was going to cut open the Third Young Master’s stomach. To be honest, even while I was stopping him, I found myself thinking that cutting him open would qualify as self-defense.” Jin Wikyung subtly averted his gaze. The matter had ultimately been settled by compensating the Medicine King Hall out of Jin Wikyung’s personal fortune, but the Hall Master’s fury at the time had been extraordinary. “He swallowed that much elixir. Whatever else may be true, he probably won’t suffer from minor ailments until the day he dies.” “It still isn’t enough. Can’t you tell just by looking at him? Every time I see the youngest, I feel sorry for him. He looks like a skeleton with a few scraps of flesh stuck to it. Every morning he’s so feeble and drained of strength.” “Drained of strength?” Wipeng suddenly remembered a rumor he had heard in the past. Among the courtesans of Taiyuan’s red-light district, Jin Taekyung was supposedly known as the Night King. *Just how impressive is he?* The medicine must have worked properly in at least one respect. Without realizing it, Wipeng raised his forearm and began imagining the size. “What are you doing?” “Ah, nothing.” Jin Wikyung sighed as he looked at the mountain of documents piled before him. “Between the youngest and everything happening inside and outside the family, there’s no end to my worries. Especially… I don’t like that ‘they’ have made contact.” “You mean the Mount Heng Sword Sect.” Mount Heng Sword Sect. The weight of that name was anything but light. Since an undefeated wandering martial artist first hung its signboard decades ago, the sect had grown at a frightening pace. Now, it had become powerful enough to threaten the Jin Family of Taiyuan’s position. “What could their intentions be?” “I’ve sent my subordinates to investigate.” Jin Wikyung fidgeted with the letter from the Mount Heng Sword Sect. Why were they coming? For what purpose? One question led to another, until he arrived at a single conclusion. “Notify every branch in Shanxi. Whatever the Mount Heng Sword Sect’s purpose may be, tell them to make every possible preparation.” This was Murim. Only those who were prepared would survive to see tomorrow. [^1]: In Korean, “gold spoon” is shorthand for someone born into wealth; “God-Spoon” is a pun that escalates the expression.

#### Chapter 11 tail (verified mastered)

…
different. Until now, it had felt like threads tangled in a jumble. This time, it felt like gears slipping past each other by a hair. How many times had I tried? Whoosh—Bang! It was a simple thrust. For a moment, I wondered if I had performed all the way through the seventh and final form without realizing it, but it was only one movement from the fifth form. “What was that?” A shiver ran down my spine. For one brief moment, the footwork and spear technique had meshed perfectly. The spear in my hand trembled. > **System** > > - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100) I shoved the System notification into a corner of my mind and tightened my grip on the spear. Recalling the sensation from a moment ago, I stepped forward. And again. Swish—Whoosh— *This is it.* I felt it the instant I thrust the spear. The footwork and the spear technique. The two gears meshed perfectly. Overwhelmed by indescribable exhilaration, I turned those two gears again and again. My steps, and the spearhead that thrust, slashed, and swung, were fast, precise, and powerful. My dantian grew hot. My internal energy became a ball of fire and seeped into the spear. I had to release it. *Right now!* “Hah!” The Sky-Piercing Strike—the final blow of the Jin Family’s Spear Technique, said to pierce the heavens—shot forward. A deep, muffled boom erupted through the cavern. Bang! Dust billowed, and stones scattered in every direction. The spear embedded in the training hall’s wall trembled. A massive hole had formed around the spearhead, which had plunged so deeply that it was no longer visible. A hole? No. This was a crater. The sight stole my breath away. “Huff, huff…” The exhilaration sent a shiver down my spine. *Fuck, that was me. I did it!* I had unleashed that insane strike—the kind that could take down a troll in one blow. Me! I staggered. *Huh?* I needed to shout my head off and take a proof photo. I needed to put Big Brother Jinho in his place—he used to call me a freeloader. *Oh, right. This was a game.* My vision blurred. The strength drained from my body. An unbearable wave of sleepiness washed over me. *I’m sleepy.* I stopped thinking and surrendered my body to instinct. A familiar sound gradually faded into the distance. Ding. Ding. Ding. . . . > **System** > > - All internal energy has been depleted. > > - You feel extreme fatigue. > > - You have completed the achievement **Unity of Self and Object**. A reward will be granted! > > - You have realized how to link martial arts together on your own. As a reward, the realms of your martial arts will rise substantially. > > - The realm of **Jin Family’s Cultivation Technique**… > > - The realm of **Jin Family’s Manoeuvre Technique**… > > - The realm of **Jin Family’s Spear Technique**… > > - Level up! > > - Level up! * * * > **System** > > - Sleep mode has ended. I opened my eyes. The cave ceiling, with stalactites hanging from it, came into view. *The training hall.* How long had I been unconscious? Half a day? Or a full day? I didn’t know. What mattered was that I was still in the game and had gotten plenty of rest. *I feel great, too.* My body felt strangely good. Come to think of it, I seemed to have heard System notifications just before I passed out. “Open Message Window.” The next moment, unread messages covered my vision. By the time I finished reading them all and sorting through my thoughts, more than ten minutes had passed. I muttered a brief reaction. “I really hit the jackpot.” The Jin Family’s Manoeuvre Technique and Spear Technique had risen all the way to the Third Stage, jumping two whole stages. The Jin Family’s Cultivation Technique had reached the Second Stage. And on top of that… “I went up two Levels?” I was happy, but also bewildered. I’d barely expected to Level up at all in the training hall. “Don’t you usually Level up by completing Quests or killing monsters?” Apparently, learning martial arts and gaining insight like I had could also lead to a Level Up. Was it because this was a martial-arts game? I really couldn’t make sense of it. “No wonder my body felt so light.” The Level Up effect must have restored my condition. The bruises and slight pain that had remained before I leveled up had vanished completely. “Open Status Window.” The Status Window had changed too. Reaching Level 13 had given me twenty remaining points, and the effects of training had slightly increased my Strength, Stamina, and Agility. “Level 13…” The Quest completion requirements were reaching the first-rate realm, Level 30, and 500 Fame. I wasn’t progressing quickly, but I was steadily leveling up through training alone. That meant I was cruising along. *Once I leave the training hall, I can spread my sails and surge forward.* I smiled contentedly and distributed my points. Now, all that remained was to check the reward I’d received for completing the Unity of Self and Object achievement. “Open Inventory.” > **System** > > - You have 1 new Item. Would you like to check it? Yeah. Hand it over.

## Korean source

```text
＃12화



10년 전쯤인가? 내가 고등학생 시절 일반인 수십 명이 정부 승인하에 게이트에 진입한 일이 있었다.

‘중국이었지, 아마.’

헌터들도 한눈팔면 시체가 되는 곳이 게이트인데 일반인들을 들여보내다니, 역시 미라클 대륙이다.

이 미친 짓거리가 벌어진 출정식 당일, 해외 언론과의 인터뷰에서 그들의 정체가 밝혀졌다.

중화 무술 연맹.

한마디로 현대판 무림인들인 셈이다. 완전한 비각성자들로 이루어진 그들은 도포를 펄럭이며 수백 대의 카메라를 향해 엄숙히 선언했다.

‘바로 오늘, 중화의 천년 무맥이 화려하게 부활할 것입니다.’

화려하긴 했다. 불과 반나절 만에 그들의 얼굴이 각종 뉴스 1면을 대문짝만하게 장식했으니까.



- 중화 무술 연맹 소속 25인. F급 게이트에서 몰살. 그중 절반 이상이 고블린 독침에 의해 사망한 것으로 밝혀져…….



천년 무맥이 얼마나 대단한 건지는 모르겠지만 그 사건으로 중국은 개망신을 당했고 중화 무술 연맹은 간판만 남았다.

‘아주 아작 났지.’

대륙에서 손꼽히는 무술인들이 고블린 독침에 맞아 죽고, 태극권의 고수는 이종 격투기 선수한테 얻어터진다.

그게 현실이다. 소설에서, 영화에서 나오는 장면들은 미디어 매체와 신비로움으로 포장한 허구라고 생각했다.

‘그런데…….’

이제는 모르겠다. 혁무진이 보여 준 움직임은 ‘진짜’였다.

직접 무공을 익히면서 의심은 점점 확신으로 변해 갔다. 현실에서처럼 힘없고 흐느적거리는 무공은 어디에도 없다.

이곳의 무공은 체계적이고, 수많은 동작을 포함한다. 현실의 무공이나 권투 따위에 비할 바가 아니었다.

‘어떻게 이런 게 가능하지? 단순히 게임이라서?’

스으읍. 후우우.

호흡과 함께 몸 밖의 기운을 느낀다. 그리고 끌어당긴다.

혈도를 따라 회전하는 10년 공력에 비하면 티끌에 불과한, 작고 약한 기운이었지만 나는 그마저도 아쉬운 처지다.

‘한 바퀴, 두 바퀴…….’

진가심법의 구결을 따라 운기조식을 이어 갔다. 마치 어릴 적부터 수련해 왔던 것처럼 자연스러운 행위였다.

‘견정(肩井), 아문(雅文), 봉안(鳳眼), 입동(入洞)…….’

지난 27년간 듣도 보도 못한 혈도의 명칭들이 머릿속에 떠오르고 사라진다. 그렇게 내 머릿속에 각인된 혈도가 수백 개에 달한다. 시스템의 기능은 어디까지인 걸까.

‘생각해 보면 기이할 정도지.’

인간의 뇌는 컴퓨터가 아니다. 하지만 시스템은 파일을 복사 붙여넣기 한 것처럼 내 머릿속에 입력시켜 놓았다. 다른 무공들도 마찬가지다.

이런 현상이 가능한가? 단지 게임이라는 이유만으로?

‘아니다. 우선 운기조식에만 집중하자.’

다시 호흡을 가다듬고 공력을 이끌었다. 10년 공력을 진가심법의 구결에 따라 꼬박 열두 바퀴를 돌린 후에야 눈을 떴다.

띠링.



- [운기조식]을 마쳤습니다.

- [진가심법]의 숙련도가 미약하게 오릅니다.

- 탁기가 소량 배출되었습니다.



“후우.”

진가심법 삼 성 달성이 코앞이다. 바닥부터 시작해서인지는 몰라도 제법 빠른 속도라고 느껴졌다.

‘아니면 아이템 덕분일 수도 있고.’

나는 오른손 중지에 끼워진 반지를 바라봤다.

앞서 [물아일체] 업적을 달성한 보상으로 받은 아이템이다.



아이템창



[청심환]

종류 : 반지

등급 : 無

제한 : 無

설명 : 매우 단단하고 재질을 알 수 없는 반지. 착용자의 마음을 안정시켜 집중을 돕는다.





청심환. 내가 알고 있는 것과 형태는 다르지만, 효과는 비슷하다. 확실히 이걸 낀 후부터 운기조식에 들어가는 시간은 짧아지고, 얻는 숙련도는 늘었다.

‘좋긴 좋은데…….’

찝찝한 기분이다. 로그아웃은 뭐, 내가 모르는 공돌이들의 기술적인 영역이라 치자. 하지만 무공 구결이나 이 반지, 청심환의 같은 경우는 어딘지 모르게 꺼림칙하다.

‘강제로 주입되는 기분이라고 해야 하나?’

내 생존에 도움이 된다지만 기분 좋은 일이 아닌 것은 분명하다. 여러모로 거지 같은 게임이다.

“성진호 이 인간은 도대체 뭘 하고 자빠진 거야. 고시원 총무라는 양반이.”

일어났으면 해장국이라도 한 그릇 하자고 날 깨웠어야 했다. 그런데도 아직 아무런 변화가 없다는 건…….

‘아냐. 아니야.’

최소한 현실의 나는 아직 살아 있다. 그러니까 아직까지 플레이어로 이 게임에 존재할 수 있는 거다.

현실에서도, 게임에서도 살아 있다. 그리고 반드시 살아 나갈 거다. 이렇게 개죽음당하기에는 내 삶이 너무 아쉽고, 내 짐이 너무 무겁다.

‘여기서 죽을 수는 없지.’

이를 악물고 가부좌를 틀었다. 청심환의 효과일까, 마음이 점차 가라앉고 호흡이 안정된다.

단전의 공력이 움직이는 것을 시작으로, 나는 몇 번째인지 모를 운기조식을 시작했다.



* * *



수련동에 들어온 지 이틀째.

나는 쉬지 않고 수련에 몰두했다. 창법, 보법에 미친 듯이 매달렸고 도중에 공력이 모두 소진되면 곧바로 운기조식을 시작했다.

띠링.



- [진가심법]의 경지가 삼 성으로 올랐습니다.

- 공력이 보다 정순해지고 효율적인 운기조식이 가능합니다.



삼 성의 진가심법. 다른 두 개에 비하면 느린 속도였지만 나쁘지 않다. 아니, 그렇게 생각하려고 노력 중이다.

‘이렇게라도 해야 버티지.’

그나마 무공 수련을 할 때는 나쁜 생각을 떨쳐 버릴 수 있어서 다행이었다.

쉭, 쉬쉭.

진가창법의 초식을 차례대로 풀어냈다. 진가보법과의 연관성을 깨달은 이후로 한층 정교하고 날카로워진 공격이 전방을 휩쓴다.

나는 아무도 없는 그곳에 누군가의 모습을 그려 내고 있었다.

‘혁무진.’

이 게임에서 처음으로 만난, 진짜배기 무림인. 나를 어린애처럼 갖고 놀았던 20레벨의 강자.

‘지금 상태라면 그놈을 이길 수 있을까?’

의문이 떠오른 그 순간이었다.

띠링.



- 새로운 기능, [수련 모드]가 활성화되었습니다.

- 지금까지 대결한 상대의 환영을 불러낼 수 있습니다. 단, 사용자의 레벨과 10레벨 이상 차이 나는 상대는 불가능합니다.

- 현재 소환 가능한 상대 : [Lv.20 혁무진], [Lv.10 천력부]



“엥?”

수련 모드? 지금까지 대결한 상대의 환영을 불러낼 수 있다고? 잠깐 망설이다가 새로운 기능을 시험해 보기로 마음먹었다.

“혁무진 소환.”



- [Lv.20 혁무진]를 소환합니다.



시스템 알림이 뜨기가 무섭게 투명한 형체가 불쑥 솟아올랐다. 태원진가의 남색 무복에 특유의 송충이 눈썹. 선 채로 눈을 감고 있는 형체는 혁무진의 모습 그대로였다.

“헐, 진짜네.”

나는 조심스럽게 다가가 혁무진의 몸을 짚었다. 하지만 환영이라서 그런 걸까, 손은 허무하게 녀석의 몸을 통과했다.

좋아, 이걸로 안전성 테스트는 통과다.



- 소환한 대상의 수준을 일부 변경할 수 있습니다.



“우선은 혁무진의 절반 정도로.”



- [Lv.20 혁무진]의 데이터를 입력합니다. 환영은 본체의 50% 실력을 발휘할 수 있습니다.



동시에 혁무진의 환영이 눈을 떴다. 실력이 아니라 성격도 닮았는지 싸가지 없는 눈빛으로 나를 바라본다.



- 수련을 시작하시겠습니까?



“물론!”

띠링.

시스템 알림이 신호탄이다. 나는 번개처럼 달려들어 창을 찔렀다. 비록 환영과의 싸움이지만 공력을 아끼지 않고 쏟아부었다.

‘일 초식.’

나아감과 동시에 찌르고, 창대를 비트는 걸로 시작한다. 첫 공격을 피하지 못한다면 적은 그것으로 끝이다.

쐐애액-

하지만 혁무진은 미꾸라지 같은 움직임으로 빠져나갔다. 다음 동작이 무의미해지는 순간이다.

‘이것도 피하나 보자.’

나는 계속해서 창법을 펼쳐 냈다. 바람이 찢어지는 소리가 났지만 혁무진은 모두 피해 냈다.

얼핏 그의 불투명한 얼굴에 비웃음이 떠오르는 듯했다.



‘그렇게 무식하게 싸워서야 쓰나. 무인이라면 응당 무공을 써야지.’



지난번 나를 농락하면서 쳤던 대사다. 내가 만들어 낸 허상일 뿐이지만…… 열받네, 이거.

‘자신 있으면 피하지만 말고 덤벼 보든가.’

내 생각을 전달받은 혁무진이 미끄러지듯이 달려들었다. 하지만 창과 주먹의 싸움이다. 이대로 공격을 허용하면 지난 7년 동안 삽질만 한 게 된다.

“어딜!”

후웅-

창대를 휘둘렀다. 만약 허상이 아닌 실제였다면 퍽, 소리가 났을 거다. 설령 피했더라도 거리를 좁히는 데에는 실패했겠지.

‘어디까지 피하나 보자.’

이 초식이 시작됐다. 쏟아지는 공격에 혁무진은 감히 다가올 생각도 못 하고 뒷걸음질 쳤다.

전투도 흐름이다. 나는 그 흐름 위에 올라탔고 혁무진은 휩쓸렸다. 지친 얼굴로 땅을 뒹구는 혁무진을 보며 생각했다.

‘약하다.’

녀석의 움직임이 내게는 보였다. 이 자리에 투영해 낸 혁무진은 권사(拳士)다. 발을 보면 움직임을 알 수 있고, 다음 행동을 예측할 수 있었다. 놈의 주먹은 내게 닿지 못한다.

쉬쉬쉭!

한순간, 세 번을 연달아 찔렀다. F급 헌터 진태경은 할 수 없는 공격. 그러나 공력을 끌어 올린 무림인 진태경이라면 가능하다.

- 크아아악!

가슴을 찔린 혁무진이 그런 비명을 지르는 듯했다.

나는 망설이지 않고 창대를 더욱 깊숙이 밀어 넣고 비틀었다. 창날이 가슴뼈를 부수고 심장을 갈랐다. 쓰러진 혁무진의 모습이 천천히 흐려졌다.

“아. 이건 너무 쉬운데.”

5초도 채 되지 않았는데 벌써 승부가 날 줄이야.

심지어 싸움 내내 우위를 점하다가 싱겁게 끝나 버렸다.

‘절반은 너무 약했나?’

운기조식으로 소진된 공력을 회복하며 생각에 잠겼다.

혁무진은 20레벨이고 최소 몇 년간 무공을 수련한 무인이다. 이렇게 약할 리가 없다.

‘좋아, 다시.’

창을 쥐고 일어났다. 눈을 감고 새로운 혁무진을 떠올렸다.

180센티의 키. 날렵한 근육과 싸가지 없는 눈매. 그때 봤던 움직임을 주입했다. 이윽고 눈을 뜨자 내가 생각한 그대로의 허상이 앞에 서 있었다.

하지만 아직 끝나지 않았다. 혁무진은 더 강해져야 했다.

‘넌 신체 능력이 나보다 우수하다.’

몇 개의 조건을 더 주입시키자 혁무진의 허상 기분 좋은 웃음을 지었다. 그는 훨씬 빠르고 결코 지치지 않는 체력을 갖게 됐다.

“그래, 이 정도는 돼야 할 만하지.”

그 말이 신호탄이었다. 빛살처럼 쇄도하는 혁무진을 향해, 나는 창을 찔러 넣었다.

쉬쉬쉭!



* * *



우우웅. 펑!

창날이 허공을 찢었다. 벌 떼 우는 소리와 함께 터져 나간 공기가 바람을 불러왔다. 진가창법의 최후 절초. 천관일이다.

- 커허…….

혁무진의 허상은 뻥 뚫린 자신의 가슴을 내려다봤다. 믿을 수 없다는 눈빛이다. 이내 무릎이 꺾이고 허상이 흩어진다.

“이게 아닌데.”

진가창법의 숙련도가 올랐다는 메시지를 들으며 머리를 벅벅 긁었다.

‘왜 아직도 내가 이기지?’

시스템이 착각한 건지, 아니면…….

‘그냥 내가 강해진 건가?’

문득 든 생각을 털어 냈다. 그럴 리가. 내가 무슨 불세출의 천재도 아니고. 겨우 무공 두어 개 익혔을 뿐인데.

‘이래서야 효과가 별로 없는데.’

강자를 상대했을 때 어떻게 되는지 실험하는 시뮬레이션에서 내가 이겨 버리면 무슨 의미가 있나 싶다.

적어도 혁무진이 무슨 무공을 익혔는지 알고 있다면 그 위력을 살려 볼 수 있을 텐데…… 아니, 잠깐.

“더 쉬운 방법이 있었네.”

진가보법과 진가창법. 20레벨의 혁무진에게 이 두 개를 접목시키면 어떨까.

제삼자의 시선에서 장단점을 파악할 수도 있을 것이다.

그래, 그게 낫겠다.

“너도 그렇게 생각하지?”

어느새 다시 나타난 혁무진의 허상이 씩 웃으며 고개를 끄덕였다.

“그래, 다시 한번 붙어 보자.”

창을 비스듬히 치켜들고 왼발을 한 발 내딛는다. 허상이 거울처럼 같은 자세를 취했다.

- 후회할걸.

“후회 같은 소리 하고 자빠졌네.”

이제는 허상이랑 대화도 하는구나. 누가 보면 빼도 박도 못하고 미친놈 소리 듣겠다.

- 미친놈.

……내 상상이지만 열받네.

“넌 죽었어.”

나는 망설임 없이 녀석을 향해 창을 겨누었다.

똑같은 무기, 똑같은 무공. 재미있는 싸움이 될 것 같았다.

- 재미? 정말 미친놈이구나. 너.

아, 그러게.

이 상황에서 재미를 느끼다니. 나도 어지간히 미친놈이다.
```

## Current accepted English baseline

```markdown
# Chapter 12

Was it about ten years ago? Back when I was in high school, several dozen ordinary people entered a Gate with government approval.

*China, I think.*

Gates were places where even Hunters became corpses if they let their attention wander, and they were sending ordinary people inside? It really was the Miracle Continent.

On the day of the expedition ceremony when this insane stunt took place, their identities were revealed during an interview with the overseas press.

The Chinese Martial Arts Alliance.

In other words, they were modern-day Murim martial artists. Made up entirely of non-awakened people, they solemnly declared their intentions toward hundreds of cameras, their robes fluttering in the wind.

*Today, the thousand-year martial lineage of China will be reborn in all its glory.*

It certainly was glorious. Their faces had been plastered across the front pages of all kinds of news outlets in less than half a day.

> **Chinese Martial Arts Alliance: Twenty-Five Members Massacred in an F-Rank Gate. More Than Half Confirmed Dead from Goblin Poison Needles…**

I didn’t know how impressive a thousand-year martial lineage was supposed to be, but the incident brought immense disgrace upon China, and the Chinese Martial Arts Alliance was left with nothing but its signboard.

*It got completely wrecked.*

Some of the most renowned martial artists on the continent were killed by goblin poison needles, and a tai chi master was beaten senseless by a mixed martial arts fighter.

That was reality. I had thought the scenes from novels and movies were fiction dressed up in media spectacle and mystery.

*But…*

Now, I wasn’t so sure. The movements Hyuk Mujin had shown me were *real*.

As I learned martial arts myself, my doubts gradually turned into certainty. There was nothing weak or floppy about the martial arts here, unlike in reality.

The martial arts of this world were systematic and involved countless movements. They couldn’t even be compared with real-world martial arts or boxing.

*How is this possible? Is it simply because this is a game?*

Ssshh. Hooouu.

As I breathed, I sensed the energy outside my body and drew it in.

Compared to the ten years of internal energy rotating through my acupoints, it was nothing but a speck of dust—small and weak. But I was in no position to complain about even that.

*One circuit. Two…*

I continued circulating my qi according to the formula of the Jin Family’s Cultivation Technique. It was a natural action, as if I had been practicing it since childhood.

*Gyeonjeong, Amun, Bongan, Ip-dong…*

Names of acupoints I had never heard or seen in my twenty-seven years surfaced and vanished in my mind. Hundreds of acupoints had been engraved into my memory like that. Just how far did the System’s functions go?

*Now that I think about it, it’s downright bizarre.*

The human brain wasn’t a computer. But the System had entered the information into my mind as if it had copied and pasted a file. The other martial arts were the same.

Was a phenomenon like this possible? Simply because this was a game?

*No. For now, focus on circulating qi.*

I steadied my breathing again and guided my internal energy. Only after circulating the ten years of internal energy through twelve complete circuits according to the formula of the Jin Family’s Cultivation Technique did I open my eyes.

Ding.

> **System**
>
> - You have completed **Circulating Qi**.
>
> - **Jin Family’s Cultivation Technique** Mastery has increased slightly.
>
> - A small amount of turbid qi has been expelled.

“Whew.”

The Third Stage of the Jin Family’s Cultivation Technique was within reach. I didn’t know whether it was because I had started from the very bottom, but it felt like a fairly fast pace.

*Or it could be thanks to the Item.*

I looked at the ring on my right middle finger.

It was the Item I had received as a Reward for completing the **Unity of Self and Object** achievement.

> **System**
>
> **Item Window**
>
> **Clear-Heart Pill**
>
> **Type:** Ring
>
> **Grade:** None
>
> **Restriction:** None
>
> **Description:** A very hard ring made of a material that cannot be identified. It calms the wearer’s mind and helps with concentration.

The Clear-Heart Pill. Its form was different from the one I knew, but its effects were similar. After I put it on, the time it took me to settle into circulating qi had definitely shortened, and the Mastery I gained had increased.

*It’s good, but…*

I still felt uneasy. I could chalk Logout up to the technical territory of engineering nerds beyond my understanding. But the martial arts formulas and this ring, the Clear-Heart Pill, were unsettling in a way I couldn’t quite explain.

*Was I supposed to call it the feeling of something being forcibly injected into me?*

Even if it helped me survive, it clearly wasn’t a pleasant experience. This game was a piece of shit in so many ways.

“What the hell was this Seong Jinho guy doing? That so-called goshiwon manager.[^1]”

If he’d gotten up, he should have woken me so we could at least have a bowl of hangover soup. And yet, the fact that nothing had changed even now meant…

*No. That’s not it.*

At the very least, I was still alive in the real world. That was why I could still exist in this game as a player.

I was alive in reality and in the game. And I would get out alive, no matter what. My life was too precious, and my burdens were too heavy, to die a pointless death like this.

*I can’t die here.*

I clenched my teeth and sat cross-legged. Perhaps it was the effect of the Clear-Heart Pill. My mind gradually settled, and my breathing steadied.

As the internal energy in my dantian began to move, I started yet another session of circulating qi.

* * *

It was the second day since I entered the training hall.

I devoted myself to training without stopping. I trained in the Spear Technique and Manoeuvre Technique like a madman, and whenever my internal energy was completely depleted, I immediately began circulating qi.

Ding.

> **System**
>
> - The realm of **Jin Family’s Cultivation Technique** has risen to the Third Stage.
>
> - Your internal energy has become purer, allowing for more efficient circulation of qi.

The Third Stage of the Jin Family’s Cultivation Technique. It had progressed more slowly than the other two, but it wasn’t bad. No, I was trying to think of it that way.

*I had to think of it that way if I was going to hold on.*

At least martial arts training allowed me to shake off my dark thoughts. For that, I was grateful.

Swish. Ssshk.

I performed the forms of the Jin Family’s Spear Technique in order. Ever since realizing its connection with the Jin Family’s Manoeuvre Technique, my attacks had grown more precise and sharper, sweeping through the empty space ahead of me.

I was projecting someone into that empty space.

*Hyuk Mujin.*

The first genuine martial artist I had met in this game. A Level 20 powerhouse who had toyed with me like a child.

*Could I beat that bastard in my current condition?*

That was the moment the question crossed my mind.

Ding.

> **System**
>
> - A new function, **Training Mode**, has been activated.
>
> - You can summon illusions of opponents you have fought so far. However, opponents whose Level differs from the user’s by ten or more cannot be summoned.
>
> - Currently summonable opponents: **Lv. 20 Hyuk Mujin**, **Lv. 10 Heavenly Axe**

“Huh?”

Training Mode? I could summon illusions of opponents I had fought so far? After a moment’s hesitation, I decided to test the new function.

“Summon Hyuk Mujin.”

> **System**
>
> - Summoning **Lv. 20 Hyuk Mujin**.

The moment the System notification appeared, a transparent figure abruptly sprang into existence. He wore the navy martial uniform of the Jin Family of Taiyuan and had Hyuk Mujin’s distinctive caterpillar eyebrows. The figure stood with his eyes closed, looking exactly like Hyuk Mujin.

“Holy shit, it’s real.”

I carefully approached and touched Hyuk Mujin’s body. But perhaps because it was an illusion, my hand passed straight through him.

*Good. That passes the safety test.*

> **System**
>
> - You can partially alter the summoned target’s abilities.

“For now, make him about half as strong as Hyuk Mujin.”

> **System**
>
> - Entering the data for **Lv. 20 Hyuk Mujin**. The illusion can use 50% of the original’s abilities.

At the same time, Hyuk Mujin’s illusion opened his eyes. Perhaps his personality had been copied along with his abilities, because he looked at me with the same insolent gaze.

> **System**
>
> - Would you like to begin training?

“Of course!”

Ding.

The System notification was the starting signal. I charged forward like lightning and thrust my spear. Even though I was fighting an illusion, I poured out my internal energy without holding anything back.

*First form.*

It began with a thrust as I advanced, followed by a twist of the spear shaft. If the enemy couldn’t evade the first attack, the fight was already over.

Ssshwip—

But Hyuk Mujin slipped away with the movement of a loach. That made the next movement pointless.

*Let’s see if you can dodge this, too.*

I continued unleashing the Spear Technique. The sound of wind splitting filled the air, but Hyuk Mujin dodged every attack.

For an instant, it seemed a sneer crossed his opaque face.

*How can you fight so stupidly? A martial artist ought to use martial arts.*

Those were the words he had used when he toyed with me last time. He was nothing more than an illusion I had created, but…

*God, that’s pissing me off.*

*If you’re so confident, stop dodging and come at me.*

Hyuk Mujin picked up on my thought and rushed at me in a smooth glide. But this was a fight between a spear and a fist. If I let him land that attack, it would mean I had spent the last seven years digging holes for nothing.

“Where do you think you’re going!”

Whoom—

I swung the spear shaft. If the illusion had been real, it would have made a solid *thwack*. Even if he had dodged it, he would have failed to close the distance.

*Let’s see how far you can dodge.*

I launched into the form. Faced with the torrent of attacks, Hyuk Mujin didn’t even dare to approach. He retreated step after step.

Combat had a flow. I had caught that flow, and Hyuk Mujin had been swept along by it. Looking at Hyuk Mujin rolling across the ground with an exhausted expression, I thought,

*He’s weak.*

I could see his movements. The Hyuk Mujin projected here was a fist fighter. I could tell how he would move by watching his feet, and I could predict his next action. His fists couldn’t reach me.

Ssshk-swish-swish!

In a single instant, I thrust three times in succession. It was an attack F-rank Hunter Jin Taekyung couldn’t perform. But Jin Taekyung the Murim martial artist, drawing on internal energy, could.

“Kraaagh!”

Hyuk Mujin seemed to scream as the spear pierced his chest.

Without hesitation, I shoved the spear deeper and twisted it. The spearhead crushed through his breastbone and split his heart. The fallen Hyuk Mujin slowly faded away.

“Ah. This is way too easy.”

The fight had already been decided in less than five seconds.

I had even held the upper hand throughout the entire battle, only for it to end anticlimactically.

*Was half just too weak?*

I fell into thought while recovering the internal energy I had depleted by circulating qi.

Hyuk Mujin was Level 20 and a martial artist who had trained in martial arts for at least several years. There was no way he could be this weak.

*All right. Again.*

I stood up with the spear in my hand and closed my eyes, imagining a new Hyuk Mujin.

A height of 180 centimeters. Lean muscles and insolent eyes. I infused him with the movements I had seen back then. When I opened my eyes, an illusion exactly as I had imagined stood before me.

But it still wasn’t over. Hyuk Mujin had to be stronger.

*Your physical abilities are superior to mine.*

After I fed in a few more conditions, Hyuk Mujin’s illusion smiled pleasantly. He had become much faster and gained stamina that would never run out.

“Yeah. Now this is worth fighting.”

Those words were the starting signal. I thrust my spear at Hyuk Mujin as he charged toward me like a ray of light.

Ssshk-swish!

* * *

Vroooom. Boom!

The spearhead tore through the air. The air burst with the sound of a swarm of bees, bringing a gust of wind with it. It was the final form of the Jin Family’s Spear Technique: Sky-Piercing Strike.

“Kheugh…”

Hyuk Mujin’s illusion looked down at his gaping chest. His eyes held pure disbelief. Then his knees buckled, and the illusion scattered.

“This isn’t right.”

I scratched my head roughly as I heard the message that my Mastery of the Jin Family’s Spear Technique had increased.

*Why am I still winning?*

Had the System made a mistake, or…

*Did I simply become stronger?*

I brushed the thought away as soon as it came to me. That couldn’t be it. I wasn’t some peerless genius. I had only learned a couple of martial arts.

*At this rate, this isn’t very useful.*

This was supposed to be a simulation for testing what happened when I fought a powerful opponent. If I kept winning, what was the point?

If I at least knew which martial arts Hyuk Mujin had learned, I could draw out their power. But wait.

“There’s an easier way.”

The Jin Family’s Manoeuvre Technique and Spear Technique. What if I grafted those two onto the Level 20 Hyuk Mujin?

I might even be able to identify their strengths and weaknesses from a third-party perspective.

Yeah. That would be better.

“You think so too, right?”

Hyuk Mujin’s illusion had reappeared at some point. It grinned and nodded.

“Then let’s fight again.”

I raised the spear diagonally and took one step forward with my left foot. The illusion assumed the same stance as if it were looking in a mirror.

“You’ll regret this.”

“Regret, my ass.”

I was even talking to an illusion now. Anyone who saw me would have no choice but to call me a certifiable lunatic.

“Crazy bastard.”

…It was my imagination, but it still pissed me off.

“You’re dead.”

Without hesitation, I pointed the spear at him.

Same weapon. Same martial arts. It looked like it would be an interesting fight.

“Interesting? You really are a lunatic.”

Yeah. I suppose so.

Finding this fun in a situation like this meant I was pretty damn crazy, too.

[^1]: A goshiwon is cheap boarding made up of tiny private rooms, often rented by exam students.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 12`.

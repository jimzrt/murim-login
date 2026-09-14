# Master Edit Task — Chapter 16

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
| 위팽     | **Wipeng**         |
| 이소군    | **Lee Seogeun**    |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 습득               | **Acquired**                   |
| 로그아웃             | **Logout**                     |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 헌터      | **Hunter**            |
| 마법사     | **mage**              |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 공자      | **Young Master**                                                |
| 도사      | **Daoist**                                                      |
| 한엽 | **Han Yeop** |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 10–14

## Plot

Taekyung enters a staged confinement in the training hall, secretly arranged by Jin Wikyung to protect him from the Elder Council. He acquires and trains the Jin Family’s Spear Technique, combines it with his Manoeuvre Technique, and creates a crater with the Sky-Piercing Strike. The Unity of Self and Object achievement grants him the Clear-Heart Pill, a ring that improves concentration and cultivation. During three days of intensive training, his Cultivation Technique reaches the Third Stage, his Spear and Manoeuvre Techniques reach the Fourth Stage, and he reaches Level 14. Training Mode lets him practise against adjustable versions of opponents, including Hyuk Mujin.

After confinement ends, Taekyung is taken to the main assembly hall rather than allowed home. Lee Seogeun, a Level 30 envoy of the Mount Heng Sword Sect, accuses him of attempting to rape the sect leader’s daughter and demands that the Jin Family withdraw from every commandery and county except Taiyuan. When Jin Wikyung refuses the demand and the duel, Taekyung accepts the System’s Duel Quest to prevent war and his designation as a public enemy. Lee initially overwhelms him with killing intent, but Taekyung blocks more than twenty strikes, kicks Lee’s exposed chest, and breaks through the Intimidation effect. The duel continues with Taekyung promising to defeat him.

## Continuity

- Taekyung is Lv. 14. His Cultivation Technique is Third Stage; his Spear and Manoeuvre Techniques are Fourth Stage.
- The Clear-Heart Pill is a ring that steadies Taekyung’s mind and improves concentration and cultivation.
- Training Mode can summon prior opponents and partially adjust their abilities; Hyuk Mujin is Lv. 20.
- Taekyung’s three-day protective confinement has ended. He is at the main training ground, still not returned to his residence.
- Jin Wikyung is Taekyung’s protective eldest brother and Lesser Family Head; Wipeng restrains him from entering the duel and supports the protective plan.
- The Mount Heng Sword Sect and the Jin Family are sworn enemies. Lee Seogeun is a Lv. 30 envoy acting on Mount Heng’s behalf.
- The Myeongwollu evidence remains suspicious: witnesses claim Taekyung entered the wrong room while drunk and that someone heard screaming, while Taekyung denies the alleged assault through his amnesia pretence.
- Taekyung accepted the Duel Quest. Its reward is the Gambler title, EXP, and Fame 50; refusal would cause the Sex Fiend title, injury, war with Mount Heng, and public-enemy status.
- Taekyung can read and block Lee’s attacks despite the Level gap, has kicked Lee’s chest, and has lost the Intimidation status effect.
- The capsule’s purpose, route home, and the limits of Murim’s death and resurrection rules remain unresolved.

## Translation Decisions

- Retain **Mount Heng Sword Sect**, **Taiyuan**, **Myeongwollu**, **Lesser Family Head**, **Sound Transmission**, and the Jin Family’s **Cultivation**, **Spear**, and **Manoeuvre Techniques**.
- Render the achievement as **Unity of Self and Object**, the reward as the **Clear-Heart Pill**, and the quest titles as **Gambler** and **Sex Fiend**.
- Render Mount Heng’s demand as withdrawal from every commandery and county except Taiyuan.
- Preserve the brisk dark action-comedy, Taekyung’s self-mocking profanity, and the distinction between the first weapon clash (“Kra-kra-kraang”) and later cannon-like impacts.
- Preserve the gold-spoon/**God-Spoon** wordplay with a brief footnote where needed.

### Prior accepted reading-copy tails

#### Chapter 14 tail (verified mastered)

…
afraid. Fine. If you answer my questions honestly, I’ll go easy on you.” ……To be honest, I almost wavered. “Cut the bullshit.” “Oh? Putting on airs because you’re the son of a martial family, are you?” Lee Seogeun laughed as if I were ridiculous. “Let me ask you one thing. What gave you the confidence to accept this duel? Your martial arts are pathetic, and you’re known as a coward. I want to hear your reason.” “My reason?” No matter how much I thought about it, this was the only way. If war broke out, I would become a public enemy of the Mount Heng Sword Sect. Hunting? Leveling up? I could forget about it. The moment I stepped outside the fence of the Jin Family of Taiyuan, assassins who caught my scent would come running. *As long as I stay alive, there’ll be another chance.* I had magic. The recovery magic called leveling up. My mind eased slightly. “I thought someone like you might be manageable.” “Pfft! You’re just a wet-behind-the-ears pup.” It was a mild provocation, but it didn’t work. He was confident in his abilities, and it showed in his relaxed manner. “Is it my turn to ask a question now?” “I never said I’d answer them… but I’ll indulge you as if they were your last words.” “This incident. You fabricated it, didn’t you?” Perhaps the question caught him off guard, because Lee Seogeun’s expression stiffened awkwardly. That expression was answer enough. *So I was right.* I had wondered if that was the case, but sure enough. No wonder the whole thing had smelled rotten from beginning to end. “You petty bastards. You should’ve just declared war.” “……I’ll tear that mouth apart.” Lee Seogeun lifted his massive greatsword and muttered ominously. I raised the Sharp Spear I had taken out beforehand. *All right. Let’s do this.* I had learned martial arts. I also had instincts honed through seven years of real combat. An F-rank Hunter and a Second Rate Murim martial artist. Don’t underestimate the skills I’d honed working two jobs! “Graaah!” Lee Seogeun was more agile than I’d imagined. He closed the distance in an instant, and I blocked the greatsword crashing straight down with the shaft of my spear. Kra-kra-kraang. “Urgh.” I’d worried the Sharp Spear might be cut clean in half, but it was sturdy, as befitted a solid piece of steel. Even so, the force behind the greatsword began driving both my feet into the ground. “Die, you insect!” “Hup!” Up close, his aura was even more suffocating. Was this what a monster’s Fear felt like? “Kneel and beg for forgiveness now! Then I’ll let you off with one arm!” - Little brother! Over Lee Seogeun’s shoulder, I saw Jin Wikyung spring to his feet. The Mount Heng Sword Sect’s people watched while snickering, and the Jin Family people turned their heads away as if they couldn’t bear to watch. *I have to hold out.* At least until Jin Wikyung gets here! “Graaah!” Lee Seogeun’s greatsword struck from every direction in a relentless barrage. The weapons were clearly clashing, iron against iron, but all I could hear was cannon fire. Boom! Boom! Boom! I blocked them. “Graaah!” “Hup!” Boom! Boom! I blocked them again. “Graaah!” “Haaah!” Boom! I blocked another. “Graaah…” “Haaah…” “……?” “……?” The next moment, Lee Seogeun and I locked eyes. The instant I saw the bewilderment and confusion in his gaze, I knew he was thinking exactly what I was. *What the hell is this?* Lee Seogeun was strong. He had the brute strength of a giant monster, moved with surprising agility for someone so muscular, and swung his massive greatsword like a matchstick. And that wasn’t all. He was a Young Master of the Mount Heng Sword Sect—a sect that could actually throw its weight around. The martial arts he used had to be quite advanced. And yet… *This is… doable?* Even now, I was blocking each and every strike of the continuously swinging greatsword. More than twenty attacks. And more than twenty blocks. I could see them. That was why I could block them. I slowly lifted one of my legs, which had been buried in the ground up to the ankle. It came right out. *Could it be…* No way. Surely not. Ssshwip! At that moment, I deflected the greatsword flying toward my waist along the shaft of my spear. Then, without thinking, I kicked Lee Seogeun in his unguarded chest. Whack! “Urgh!” ……Huh? Clutching his stomach, Lee Seogeun skidded back five or six steps. Then he casually rubbed the bridge of his nose as if nothing had happened. “Not bad. You’ve got a trick or two despite being trash.” “……” “Heh. I won’t hold back anymore.” “……Hey.” “With my next strike, I’ll smash your head—what?” I raised a hand, looking awkward, and pointed at his mouth. “You’re bleeding.” A beat later, a thin line of blood ran down from the corner of Lee Seogeun’s mouth. He had probably bitten his tongue. That had to hurt. “Ah! Eeng! Eek! Hup!” Lee Seogeun wiped away the blood with a series of ridiculous yelps. “Don’t wipe it. Leave it.” “……?” “It’ll be easier to wipe it all off at once later.” Because from now on, I was going to beat the absolute shit out of him. > **System** > > - The Status Effect **Intimidation** has been removed!

#### Chapter 15 tail (verified mastered)

…
**Duel** Quest has been successfully completed! > > - Quest rewards will be distributed! > > - You have acquired the Title **Gambler**! > > - You have gained EXP and Fame! > > - An additional reward has been granted for your overwhelming performance! > > - **Jin Family’s Cultivation Technique** has risen to the Fourth Stage! > > - **Qi Sense** has risen to the Third Stage. You can now detect targets up to Level 50. > > - Level up! > > - Level up! > > - Level up! The System notifications rang out like celebratory fireworks. * * * The Mount Heng Sword Sect left. Since they had all arrived on horseback, the Jin Family of Taiyuan even had to lend them a carriage to transport the injured. But Lee Seogeun was one thing. Who was the other guy? Every one of his teeth was gone, and the cloth stuffed into his mouth was soaked with blood. Good Lord. What kind of bastard had— Just then, Jin Wikyung patted me on the shoulder with a solemn expression. “Well done. You did even better than I expected.” “Ah, yes. Thank you—” “Why are you looking at me like that?” *Because there’s blood splattered on your cheek.* I had no idea why, but in that brief span of time, he had somehow turned a man into a cripple. “So, what do you think?” “Pardon? What do you mean?” “About ending your confinement. It is true that your usual conduct has been disgraceful, but the remarkable performance you showed today is a great blessing for our family.” Jin Wikyung looked around as he continued. “What do the rest of you think?” The senior members looked displeased, but none seemed particularly inclined to object. Compared to the looks they had given me in the meeting hall earlier, I almost felt that they were favorable. *Is it because they’re Murim people?* In novels, Murim was a place where justice mattered, but strength came first. Maybe defeating Lee Seogeun had influenced them. “You should answer me. Hahaha.” …Or maybe it was because of Jin Wikyung. His mouth was smiling, but his eyes were not. Combined with the blood on his cheek, it was a scene straight out of a horror movie. “I wholeheartedly agree,” Wipeng said. Once Wipeng’s manipulation of public opinion was added to the mix, one by one, the others voiced their agreement. Jin Wikyung watched the coerced vote, enforced through a show of force, and smiled in satisfaction. * * * *Damn it. Damn it. Damn it!* Lee Seogeun bit down hard on his lip. Jin Taekyung’s face refused to leave his mind. *I lost? To trash like him?* The matter with the Jin Family of Taiyuan had given them more than enough justification. If the Mount Heng Sword Sect profited from it, all well and good. If the Jin Family refused and the conflict escalated into full-scale war, that would also have counted as a success. If he had turned Jin Taekyung into a half-cripple, word would have spread throughout Shanxi. The Jin Family of Taiyuan had suffered humiliation at the hands of the Mount Heng Sword Sect. But he had failed. *How could this have happened?* He had taken up a sword as a child. He wasn’t a genius, but neither was he mediocre. The second son of the Mount Heng Sword Sect. A promising young martial artist. A First Rate swordsman. He had always been someone others admired… *Damn it!* Everything he had possessed had been shattered today. For the first time, he had been brought to his knees by Jin Taekyung’s merciless violence—and lost consciousness. When he opened his eyes, he was already inside a carriage. Even this carriage belonged to the Jin Family of Taiyuan. Fire poured from Lee Seogeun’s eyes. *I’ll kill you. I’ll kill you with my own hands, Jin Taekyung!* Unable to contain his rising fury, he slammed his fist into the carriage wall. The carriage stopped. Lee Seogeun shouted harshly, “What are you doing? Don’t dawdle. Get moving again!” At that moment, the spot between his eyebrows prickled. - Get moving? We should. But going to the Mount Heng Sword Sect would be a little troublesome. *Sound Transmission?* “Who is it!” Lee Seogeun shouted, but no sound escaped his throat. His chest felt tight, and his throat hurt as if it were on fire. The carriage began moving again. - Let’s do this. Mount Beimang first. We can go to the Mount Heng Sword Sect afterward.[^2] *What does that—* It took no longer than a few blinks. His limbs went numb, and pain flared violently through his body. Lee Seogeun turned his trembling head. Someone wearing a mask was staring at him. “Grrk… grrrk.” *Who are you?* Instead of his voice, dark, discolored blood poured from his mouth. His vision blurred. The sounds around him grew distant. *Sa… save me…* That was his final thought. The next moment, he plunged headfirst into darkness. “Farewell, Young Hero Lee.” The masked man smiled brightly as he retrieved the large blue-black needle from the dead man’s brow. [^1]: *Ssaksuga norata*—“the sprouts are yellow”—means someone is a hopeless case. The line pushes yellow all the way to gold to make that worse, not to imply that he was born rich. [^2]: Mount Beimang is a traditional burial ground; “going to Beimang” means dying.

## Korean source

```text
＃16화



“후우, 드디어 끝났군.”

진위경이 붓을 내려놓으며 한 말이었다. 언제나처럼 문가 옆 의자에 앉아 있던 위팽이 고개를 들었다.

“점점 일 처리가 빨라지시는군요. 오늘도 고생하셨…….”

위팽이 말꼬리를 흐렸다. 아직 탁자 위에 산더미처럼 쌓인 서류를 발견했기 때문이었다.

그러고 보니 아직 정오 무렵밖에 되지 않았다. 저 정도 양의 업무를 해치울 수 있는 시간이 아니었다.

‘잘못 들었나?’

“좋아. 이 정도면…….”

이번엔 환청이 아니었다. 서류 더미 위로 불쑥 솟은 진위경의 얼굴이 그 증거였다.

“위팽, 이리 와 보게. 아주 중요한 일이야.”

너무나도 진지한 음성에 위팽은 살짝 걱정되었다.

무슨 큰일이라도 났나?

서류에서 심각한 비리가 발견됐다거나, 호시탐탐 기회를 엿보고 있는 장로원에서 큰 사건을 터트렸을 수도 있다.

‘큰일이군. 아직 항산검문의 일도 마무리되지 않았는데.’

그리고 잠시 후, 진위경이 내민 문제의 서류를 받아 든 위팽의 표정이 괴상하게 일그러졌다.

“……뭡니까, 이게?”

“보면 모르나? 그림이지.”

진위경의 말대로였다. 위팽이 생각한 문제의 서류는 온데간데없고, 건네받은 것은 그림이 그려진 화선지 한 장이었다.

“아니, 그 말이 아니잖습니까. 난데없이 이게 무슨…….”

진위경이 비밀스러운 미소를 지으며 말을 잘랐다.

“자세히 보게. 평범한 그림이 아니야.”

평범한 그림이 아니다? 순간 위팽의 눈이 번쩍 뜨였다.

머릿속에는 무림에 떠도는 온갖 전설들이 휙휙 스쳐 지나갔다.

한 폭의 그림을 보고 우화등선한 도사. 오래된 동굴의 벽화를 보고 깨달음을 얻은 절대 고수!

한참 동안 화선지를 누비던 위팽의 시선이 어느 순간, 벼락 맞은 것처럼 파르르 떨렸다.

“이, 이것은 설마……!”

“알아차렸군. 맞네.”

진위경이 후후후, 웃으며 말을 이었다.

“어제의 비무를 그려 봤네.”

“…….”

“쓰러진 이소군과 당당히 서 있는 태경이! 훗날 천하제일인이 될 젊은 영웅의 머리 위로 펼쳐진 하늘!”

“…….”

“일부러 밑에서 올려다보는 구도로 그렸는데, 자네 소감은 어떤가. 잘 그렸지. 응? 잘 그렸지?”

화선지를 붙든 위팽의 손이 바들바들 떨렸다. 마음 같아서는 구기고, 찢고, 그 위에 일주일 치 대소변을 갈긴 다음 잘 말린 후 불태우고 싶었지만.

“……잘 그리셨군요.”

위팽은 이성적인 사내였다. 절정의 경지에 오른 무인의 위대한 정신력을 발휘해 냈다.

물론 그에겐 정신 상태가 의심되는 주군을 질책할 만한 용기도 있었다.

“지금 밀린 일이 얼마나 많은데, 아침부터 지금까지 겨우 이 그림 한 장 그렸다는 게 말이 됩니까!”

“당연히 말이 안 되지.”

“그걸 아시는 분이…….”

“내가 세 시진 동안 하나만 붙잡고 있었을까 봐?”

“예?”

“당연히 하나 더 그렸지. 나중에 보여 주려고 했는데 역시 눈치가 빠르구먼.”

위팽은 부들부들 떨리는 손으로 진위경이 건네는 화선지를 받아들었다. 진위경은 싱글벙글 웃으며 그림 설명을 시작했다.

“비무 직후 상황을 그려봤네. 현재에 만족하지 않고 수련동으로 돌아가겠다고 선언하는 젊은 영웅! 그리고 그 모습을 우러러보는 사람들!”

“뭐, 그 부분에 대해서는 저도 상당 부분 동의합니다. 삼공자, 정말 많이 변했더군요.”

“그렇지? 나도 깜짝 놀랐지 뭔가.”

이소군과의 비무에서 승리한 진태경은 모두의 예상을 깨고 수련동으로 돌아갔다. 전날의 기억을 떠올리는 진위경의 눈동자가 몽롱해졌다.

“언제고 이런 날이 올 줄 알았지. 막내는 천응(天鷹)이야. 위팽, 자네에게는 들리지 않나? 태경이의 힘찬 날갯짓 소리가…….”

“날갯짓 소리는 모르겠고, 헛소리는 들립니다.”

위팽이 모든 걸 포기한 한숨과 함께 화선지를 내려놓은 순간이었다.

푸드득.

“헉.”

“거봐! 들리잖아!”

황급히 고개를 돌린 위팽의 시선이 창문을 향했다. 막 내려앉은 매 한 마리가 깃털을 고르고 있었다. 발목에는 작은 통 하나가 매달려 있었다.

“전서응(傳書鷹)입니다.”

새끼 때부터 고도의 훈련을 거쳐 투입된 연락용 매.

태원진가에도 두 마리밖에 없는 전서응은 극히 긴급한 일에만 날리게 되어 있었다.

“문제가 생겼군.”

진위경이 가라앉은 목소리로 중얼거렸다.

그리고 그것은 곧 현실로 나타났다.



* * *



“한엽이라고 합니다.”

“예?”

“만나 뵙게 되어 영광입니다.”

뜬금없는 자기소개였다. 물론 아는 얼굴이긴 했다.

수련동에 들어온 이후 가장 자주 본 사람이었으니까.

‘수련동 경비원이라고 해야 하나?’

경비원. 경비무사. 용어가 어찌 됐건 눈앞의 NPC는 수련동을 담당하는 태원진가의 무사였다. 내게 식사와 탕약을 가져다주는 것도 그의 임무 중 하나고.

‘그런데 갑자기 웬 통성명?’

지금까지 말 한마디 섞어 본 적 없는 NPC다. 내게 악감정은 없어 보였지만 그렇다고 특별히 호의적이지도 않았다.

“아, 예. 저도 반가워요.”

떨떠름한 대답에도 경비원, 아니 한엽의 얼굴이 환하게 밝아졌다. 뭐야, 갑자기 왜 이래?

“저도 어제 그 자리에 있었습니다.”

“그 자리? 아.”

비무를 말하는 거구나. 워낙 많은 사람이 몰렸으니 그중 한엽이 있었다고 해도 놀랄 만한 일은 아니다.

“처음부터 끝까지 지켜봤지요. 그 악랄한 항산검문의 이소군에게 맞서 싸우던 공자님의 영웅적인 모습을!”

악랄해? 영웅적인 모습?

‘그게 그렇게 되나?’

솔직히 현대인의 시선에서 바라보자면 그놈이 그놈이다.

아니, 오히려 이소군의 손을 들어 주고 싶을 정도다. 나도 한 사람의 오빠로서, 내 여동생 성격이 아무리 지랄맞아도 진태경 같은 놈이랑 연애질한다고 하면 눈 뒤집힐 것 같거든.

물론 항산검문의 태도나 제안은 말도 안 되는 거였다. 그래서 어쩔 수 없이 싸운 거고.

“보는 내내 가슴이 떨렸습니다. 저뿐만 아니라 그 자리에 있던 모든 사람이 같은 마음이었을 겁니다.”

한엽은 상기된 얼굴로 말을 이어 갔다. 이거 단단히 착각하고 있는 것 같은데, 어느 타이밍에서 멈춰야 할지 모르겠다.

“저도 한때 공자님을 오해했던 적이 있습니다. 하지만 이제는 가문의 모두가 진실을 알고 있습니다.”

이번에는 반문하지 않을 수 없었다.

“진실? 무슨 진실?”

“그건…….”

한엽이 잔뜩 숨죽인 목소리로 속삭였다. 귀에 닿은 뜨거운 숨결은 둘째치고, 그 내용에 소름이 돋는다.

그러니까, 그 내용인즉슨.

“내가 태원진가의 비밀 병기다?”

“네, 네!”

한엽이 맹렬하게 고개를 끄덕였다.

“사실 지금까지의 모습은 모두 위장이고, 어릴 때부터 뼈를 깎는 수련을 거치며 문무겸전에 덕과 의를 갖춘, 잠. 잠……”

이 말만은 도저히 못 하겠다. 오그라드는 손발을 보호하려는 나를 대신해 한엽이 나섰다.

“산서잠룡! 지금 가문 내에 모르는 사람이 없습니다. 공자님께서 아직 하늘에 오르지 않고 물에 몸을 숨긴 산서성의 잠룡이라는 사실 말입니다!”

아, 제발. 살려 줘. 큰 소리로 외치지도 말아 줘.

잠룡이라니. 가문에 모르는 사람이 없다니!

‘만약 내가 죽는다면 사인은 수치사다, 수치사.’

극심한 심적 고통에 몸부림치는 내게, 한엽이 반짝거리는 눈빛으로 물었다.

“사실이지요? 실례인 줄은 알지만, 저한테만 살짝…….”

안 되겠다. 누가 뿌렸는지 모를 이 말도 안 되고 오그라드는 헛소문을 진압하기로 다짐하고 입을 열었다.

“도대체 누가 그런 소문을 퍼트렸는지 모르겠지만…….”

그때였다.

띠링.



- 태원진가에 [잠룡]에 대한 소문이 퍼지고 있습니다.

- 소문에 의한 영향으로 명성이 10 오릅니다.

- 소문을 믿는 사람이 많아질수록, 명성이 상승합니다.



나는 근엄한 얼굴로 말을 이었다.

“전부 틀림없는 사실입니다.”

“역시! 저는 철석같이 믿고 있었습니다!”

환희에 찬 얼굴로 떠나는 한엽의 등을 바라보며, 나는 한줄기 눈물을 흘렸다.

‘시발…….’

아, 엄마 보고 싶다.



* * *



이소군과의 비무를 통해 여러 가지 사실을 깨달았다.

첫째.

‘나는 강하다.’

게임 초기, 튜토리얼 NPC로 나온 천력부를 일격에 쓰러트린 일이 있었다. 당시의 짐작이 지금은 확신으로 바뀌었다.

나는 강하다. 30레벨인 이소군을 어렵지 않게 쓰러트릴 정도로. 전투 경험의 차이도 영향이 있겠지만 기본적으로 능력치가 월등하다.

‘힘, 체력, 민첩. 모두 비슷하거나 내가 약간 앞섰지.’

스탯(Stat). 즉 능력치의 차이다. 이 게임 속에서 나는 유저고, 시스템을 이용한 성장을 거듭해 왔다.

무공 습득, 수련과 여러 가지 퀘스트를 통해 빠른 속도로 스탯을 올렸고 그 결과는 비무에서 드러났다.

그리고 두 번째.

‘공력이 부족해.’

공력 하나만큼은 이소군이 나보다 앞섰다. 아니, 월등했다.

뭘 먹고 컸는지 창대로 수십 번을 후려쳐도, 마운트 자세에서 일방적으로 때려도 놈은 견뎌 냈다. 반격까지 하고 마지막 순간에도 공력을 끌어 올렸다.

‘현재 내 공력은 십 년.’

이소군은 내 두 배인 이십 년은 될 거다. 여기서 세 번째 사실을 깨달았다.

‘공력의 차이가 무공의 단계를 가른다.’

나는 일류인 이소군을 꺾었다. 하지만 시스템이 표시하는 내 경지는 여전히 이류다.

나는 그 이유가 공력에 있다고 생각했다. 내게 부족한 단 하나의 능력치를 올렸을 때, 그때 비로소 내 경지도 오르지 않을까?

거기까지 정리를 마치고 나니 문득 드는 생각이 있었다.

‘이거 완전히 헌터 등급 나누기네.’

최초 각성자는 반드시 지정된 센터에서 보유 능력과 적성 직업, 마나량을 체크받아야 하는데, 신체 능력이 아무리 높아도 마나량이 부족하면 등급 심사에서 찬바람을 맞는다.

마법사들이 최하 D등급부터 시작하는 이유이기도 하다. 마법사들은 직업 특성상 기본 마나부터가 빵빵하니까.

‘그래도 게임이 현실보단 낫네.’

여긴 그나마 성장이라도 하지. 현실은 그런 거 없다. 나만 해도 7년 동안 뭐 빠지게 굴러서 E급들 사이에 낀 거지, F급 헌터인 건 변함없었으니까.

아무튼 이제 대략적인 스케치는 그려졌다.

‘스탯은 충분. 공력은 시간 날 때마다 진가심법 돌리고, 경험치 위주로 퀘스트를 받자.’

이 빌어먹을 게임에 갇힌 지 일주일이 넘었다. 현실에서 무슨 헛짓거리를 하는지는 몰라도 구조받기는 글렀다.

확실하게 준비해서 끝내야지.

“퀘스트창 오픈.”

띠링.



퀘스트



[로그아웃]

이제 당신은 이 험난한 무림을 헤쳐 나가야 합니다.

더욱더 강해지고, 유명해지십시오.

언젠가 다가올 그 날을 위해…….



등급 : 메인 퀘스트

제한 : 진태경

임무 : [일류] 경지 달성 (미완료)

         Lv.30 달성 (17 / 30)

         명성 500 달성 (70 / 500)

보상 : [로그아웃]





“아, 빡세다.”

나는 가부좌를 틀었다. 폐관 완료까지 이틀. 최대한 공력을 끌어모을 생각이었다.



- [잠룡]에 대한 소문의 영향으로 명성이 3 상승합니다.



틈틈이 울리는 명성 상승 메시지가 한줄기 위로가 되었다.



* * *



늦은 밤. 대회의장에 불이 켜졌다. 소가주인 진위경의 요청에 의해 비밀리에 이루어진 가로회의였다.

워낙 늦은 시각이었고, 갑작스러운 소집이라 뚱한 표정을 짓고 있는 중진들도 있었다.

“갑자기 소집이라니. 이게 무슨 일이랍니까?”

“그러니까. 이유도 안 알려 주고 이 늦은 시각에.”

“소가주가 아직 젊어서 그래. 절차와 예의를 몰라.”

“어제 일로 상당히 기세등등해졌나 봅니다. 하긴, 유일한 약점이 사라진 셈이니까요. 삼공자가 그 정도일 줄은 아무도 예상 못 했습니다.”

“장로원에서 김 좀 샜겠군. 삼공자 건으로 크게 한번 터트리려고 준비 중이었을 텐데.”

“허어, 지금이라도 대장로께서 나서서 가문을 바로 잡으셔야 할 터인데.”

“어허. 말조심…….”

그때, 모든 소리가 뚝 끊겼다. 회의실의 문이 양옆으로 열리고 진위경이 들어왔기 때문이었다.

중진들 사이에서는 평가가 분분한 소가주였지만 진위경의 등장과 동시에 내려앉은 침묵은 그에게 우두머리의 자질이 있음을 알려 주는 증거였다.

“늦은 밤에 소집에 응해 주신 모든 분께 감사드립니다.”

상석에 앉은 진위경은 첫 마디를 꺼냈지만 쉽사리 말을 이어 가지 못했다.

무슨 말을, 어디서부터 어떻게 꺼내야 한단 말인가. 머리가 지끈거렸다. 하지만 알려야 하는 일이었다.

“제가 오늘 이 자리를 마련한 이유는…….”

그 순간이었다.

“항산검문 때문이겠지.”

그건 기이한 목소리였다. 처음에는 늙은이의 그것이었고, 한편으로는 젊었으며 거칠거나 부드러웠다. 그리고 알 수 없는 울림이 있었다.

‘설마.’

진위경의 얼굴이 일그러졌다. 다시는 열릴 것 같지 않았던 회의장의 문이 열리고 있었다.

저벅. 저벅. 저벅.

미끄러지듯이 걸어 들어오는 다섯 명의 노인. 그리고 가장 앞에 선 노인을 확인한 모두가 황급히 일어나 고개를 숙였다.

“노야(老爺)를 뵙습니다!”

노야. 수년간 두문불출하던 대장로의 등장이었다.
```

## Current accepted English baseline

```markdown
# Chapter 16

“Whew. Finally done.”

Jin Wikyung set down his brush as he spoke. Wipeng, who was sitting in a chair beside the door as always, raised his head.

“You’re getting faster at handling your work. You must be exhausted toda—”

Wipeng let his words trail off. He had just noticed the mountain of documents still piled on the table.

Come to think of it, it was only around noon. There was no way anyone could finish that much work in so little time.

*Did I hear him wrong?*

“Good. This should be enough…”

This time, it wasn’t a hallucination. Jin Wikyung’s face suddenly popped up above the pile of documents, proof enough of that.

“Wipeng, come here. This is very important.”

His voice was so serious that Wipeng grew slightly concerned.

*Did something major happen?*

Perhaps they had discovered some serious embezzlement in the documents. Or maybe the Elder Council, which had been constantly watching for an opportunity, had caused some kind of incident.

*This is bad. We haven’t even finished dealing with the Mount Heng Sword Sect yet.*

A moment later, Wipeng accepted the document in question from Jin Wikyung. His expression twisted into something bizarre.

“…What is this?”

“You can’t tell? It’s a drawing.”

The document Wipeng had feared was nowhere to be found. Instead, Jin Wikyung had handed him a single sheet of rice paper covered in drawings.

“No, that’s not what I meant. Why are you suddenly—”

Jin Wikyung cut him off with a secretive smile.

“Look closely. It isn’t an ordinary drawing.”

*It isn’t an ordinary drawing?*

Wipeng’s eyes lit up.

All kinds of legends circulating through Murim flashed through his mind.

A Daoist who achieved ascension after looking at a single painting. An absolute master who attained enlightenment after seeing a mural in an ancient cave!

Wipeng’s gaze roamed over the rice paper for a long while. Then, at some point, it began to tremble as if struck by lightning.

“T-this is, perhaps…!”

“You noticed. That’s right.”

Jin Wikyung continued with a chuckle.

“I tried drawing yesterday’s duel.”

“……”

“Lee Seogeun lying defeated, and Taekyung standing proudly! The sky spread above the head of the young hero who would one day become the greatest under heaven!”

“……”

“I deliberately chose a composition looking up from below. What do you think? It’s good, right? Isn’t it?”

Wipeng’s hands trembled around the rice paper. If he had been acting on impulse, he would have crumpled it, torn it apart, covered it with a week’s worth of piss and shit, dried it thoroughly, and burned it.

But—

“…It’s very well drawn.”

Wipeng was a rational man. He summoned the magnificent mental fortitude of a martial artist at the Peak realm.

Of course, he also had enough courage to reprimand a lord whose sanity was in serious doubt.

“How can you say that when there’s so much work piled up? Are you telling me that you spent the entire morning drawing this one picture?”

“Of course not.”

“Then you know how ridiculous this is—”

“Did you think I spent three hours focusing on only one thing?”

“What?”

“Of course I drew another one. I was going to show it to you later, but you really are quick to catch on.”

Wipeng accepted the next sheet of rice paper from Jin Wikyung with trembling hands. Grinning from ear to ear, Jin Wikyung began explaining the drawing.

“I tried to depict the scene immediately after the duel. The young hero declares that he won’t rest on his laurels and will return to the training hall! And the people gazing up at him in admiration!”

“I agree with a considerable part of that. The Third Young Master really has changed a great deal.”

“Right? I was surprised myself.”

After defeating Lee Seogeun in the duel, Jin Taekyung had defied everyone’s expectations and returned to the training hall. Jin Wikyung’s eyes grew hazy as he recalled the events of the previous day.

“I always knew a day like this would come. The youngest is a heavenly eagle. Wipeng, can’t you hear it? The powerful sound of Taekyung’s wings beating…”

“I don’t know about wings, but I can hear you spouting nonsense.”

Wipeng lowered the rice paper with a sigh of complete resignation.

Flap.

“Gasp.”

“See? You can hear it!”

Wipeng hurriedly turned toward the window. A hawk that had just landed was preening its feathers. A small container hung from its ankle.

“It’s a messenger hawk.”

These hawks were trained intensively from the time they were fledglings before being put to use as messengers.

The Jin Family of Taiyuan had only two messenger hawks, and they were sent out only for matters of extreme urgency.

“We have a problem.”

Jin Wikyung muttered in a subdued voice.

And that problem soon made itself known.

* * *

“My name is Han Yeop.”

“Pardon?”

“It’s an honor to meet you.”

It was a sudden introduction. Of course, I knew his face.

He was the person I had seen most often since entering the training hall.

*Should I call him the training hall’s guard?*

Guard. Martial-artist guard. Whatever the proper term was, the NPC in front of me was a Jin Family of Taiyuan martial artist assigned to the training hall. Bringing me meals and herbal decoctions was one of his duties, too.

*But why is he introducing himself all of a sudden?*

This was an NPC I had never exchanged a single word with. He didn’t seem to bear me any ill will, but he wasn’t especially friendly, either.

“Ah, yes. Nice to meet you, too.”

Despite my lukewarm response, the guard’s—or rather, Han Yeop’s—face brightened.

*What the hell? Why is he suddenly acting like this?*

“I was there yesterday, too.”

“There? Oh.”

He meant the duel. So many people had gathered that it wasn’t surprising for Han Yeop to have been among them.

“I watched from beginning to end. I saw the heroic way you fought against that vicious Lee Seogeun of the Mount Heng Sword Sect!”

*Vicious? Heroic?*

*That’s how it looked?*

Honestly, from a modern man’s perspective, one was as bad as the other.

No, I almost wanted to take Lee Seogeun’s side. As an older brother myself, even if my little sister’s personality were fucking awful, I’d lose my mind if she said she was dating a guy like Jin Taekyung.

Of course, the Mount Heng Sword Sect’s attitude and proposal had been absurd. That was why I had no choice but to fight.

“My heart trembled the entire time I watched. I’m sure everyone there felt the same way.”

Han Yeop continued with an excited expression. He seemed to be under a serious misunderstanding, and I had no idea when I was supposed to stop him.

“I used to misunderstand you, too, Young Master. But now everyone in the family knows the truth.”

This time, I couldn’t help asking.

“The truth? What truth?”

“That is…”

Han Yeop whispered in a voice so hushed that it was practically a secret. Leaving aside the hot breath against my ear, what he was saying gave me goose bumps.

In other words—

“I’m the Jin Family of Taiyuan’s secret weapon?”

“Yes, yes!”

Han Yeop nodded furiously.

“Your behavior until now was all an act, and ever since you were young, you’ve undergone bone-shattering training, becoming a man accomplished in both civil and martial arts, with virtue and righteousness, a sl—sl—”

I couldn’t bring myself to say that word. Han Yeop came to my rescue before my hands and feet could curl up from embarrassment.

“The Sleeping Dragon of Shanxi! Everyone in the family knows now! You’re Shanxi’s Sleeping Dragon, still hiding in the water instead of ascending to the heavens!”

*Oh, please. Somebody save me. And don’t shout it out loud.*

The Sleeping Dragon? There wasn’t a single person in the family who didn’t know?

*If I die, the cause of death will be death by embarrassment.*

As I writhed in agony, Han Yeop asked with shining eyes,

“It’s true, isn’t it? I know it’s rude, but just between us…?”

This wouldn’t do. I decided to suppress this ridiculous, cringe-inducing rumor whose origin I couldn’t even guess, then opened my mouth.

“I have no idea who started such an absurd rumor, but…”

That was when it happened.

Ding.

> **System**
>
> A rumor about the **Sleeping Dragon of Shanxi** is spreading throughout the **Jin Family of Taiyuan**.
>
> Fame has risen by 10 due to the influence of the rumor.
>
> The more people believe the rumor, the more Fame will rise.

I continued with a solemn expression.

“Every word of it is true.”

“I knew it! I believed it with all my heart!”

I watched Han Yeop walk away with a face full of rapture and shed a single tear.

*Fuck…*

*Ah, I miss my mom.*

* * *

I realized several things through my duel with Lee Seogeun.

First.

*I’m strong.*

Early in the game, I had knocked down the Heavenly Axe, who had appeared as the tutorial NPC, in a single hit. What had only been a suspicion back then had now become a certainty.

I was strong. Strong enough to defeat a Level 30 like Lee Seogeun without much trouble. The difference in combat experience had certainly played a part, but my basic stats were overwhelmingly superior.

*Strength, Stamina, Agility. They were all similar, or I had a slight edge.*

Stats. In other words, the difference in abilities. In this game, I was a player, and I had continued growing by using the System.

I had raised my stats rapidly by learning martial arts, training, and completing various Quests. The result had shown itself in the duel.

And second.

*I don’t have enough internal energy.*

Lee Seogeun had surpassed me in internal energy. No, he had been overwhelmingly ahead.

What had he been eating growing up? Even after I smashed him dozens of times with the spear shaft, and even when I beat him one-sidedly from a mount, he endured it. He even counterattacked and drew on more internal energy at the final moment.

*I currently have ten years of internal energy.*

Lee Seogeun probably had twenty years—twice as much as I did. That led me to a third realization.

*The difference in internal energy determines the stage of one’s martial arts.*

I had defeated Lee Seogeun, who was First Rate. But the realm displayed by the System still said I was Second Rate.

I thought the reason lay in internal energy. Once I raised the one ability I lacked, wouldn’t my realm finally rise as well?

After organizing my thoughts that far, another idea suddenly occurred to me.

*This is basically just Hunter rank classification.*

A newly awakened Hunter had to be tested at a designated center for their abilities, suitable profession, and mana capacity. No matter how high their physical abilities were, if their mana capacity was lacking, they received a cold reception during the rank evaluation.

That was also why mages started at D-rank at the lowest. Because of their profession, mages had plenty of basic mana from the start.

*Still, the game is better than reality.*

At least you could grow here. Reality had no such thing. Even I had only managed to get lumped in with the E-ranks after working my ass off for seven years. I was still an F-rank Hunter.

Anyway, I had now drawn a rough outline.

*My stats are sufficient. I’ll keep cycling the Jin Family’s Cultivation Technique whenever I have time, and focus on taking Quests that reward EXP.*

It had been over a week since I was trapped in this godforsaken game. I didn’t know what kind of nonsense was happening in the real world, but I could forget about being rescued.

I needed to prepare properly and finish this.

“Open Quest window.”

Ding.

> **System**
>
> **Quest**
>
> **Logout**
>
> You must now make your way through this harsh Murim.
>
> Become stronger and more famous.
>
> For the day that will come someday…
>
> **Grade:** Main Quest  
> **Restriction:** Jin Taekyung  
> **Mission:** Achieve the **First Rate** realm (Incomplete)
>
> &nbsp;&nbsp;&nbsp;&nbsp;Reach Level 30 (17 / 30)
>
> &nbsp;&nbsp;&nbsp;&nbsp;Reach Fame 500 (70 / 500)
>
> **Reward:** **Logout**

“Ugh. This is brutal.”

I sat cross-legged. Two days remained before my seclusion ended. I intended to gather as much internal energy as possible.

> **System**
>
> Fame has risen by 3 due to the influence of the Sleeping Dragon of Shanxi rumor.

The Fame-increase messages that chimed from time to time were a small source of comfort.

* * *

Late at night, the lights came on in the main assembly hall. At the request of the Lesser Family Head, a secret meeting of the family council was taking place.

It was very late, and the summons had been so sudden that several of the senior members wore sour expressions.

“A sudden summons? What is this about?”

“Exactly. They didn’t even tell us why they were calling us here at this hour.”

“That’s what happens when the Lesser Family Head is still young. He doesn’t know procedure or etiquette.”

“He must have grown rather full of himself after yesterday’s events. Though I suppose his only weakness has disappeared. No one expected the Third Young Master to be that capable.”

“The Elder Council must have been deflated. They were probably preparing to make a major move over the Third Young Master.”

“Hmph. Even now, the Head Elder should step forward and set the family straight.”

“Careful. Watch your tongue…”

At that moment, every sound abruptly stopped. The doors to the meeting room opened from both sides, and Jin Wikyung entered.

The senior members had varying opinions of their Lesser Family Head, but the silence that settled over the room the instant he appeared proved that he possessed the qualities of a leader.

“Thank you all for answering my summons at this late hour.”

Jin Wikyung took the seat of honor and spoke his opening words, but he found it difficult to continue.

*What should he say? Where should he begin, and how?*

His head throbbed. But this was something he had to tell them.

“The reason I called everyone here today is…”

That was when a strange voice interrupted him.

“It must be because of the Mount Heng Sword Sect.”

The voice was bizarre. At first, it sounded like an old man’s. And yet it was young as well—rough one moment, smooth the next. There was also an inexplicable resonance to it.

*Could it be…?*

Jin Wikyung’s face twisted.

The doors to the meeting room, which had seemed permanently sealed, began to part.

Step. Step. Step.

Five old men walked in as if they were gliding across the floor. The instant everyone recognized the old man at the front, they hurriedly stood and bowed their heads.

“We pay our respects, Head Elder!”

The Head Elder. He had appeared after keeping himself shut away from the world for years.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 16`.

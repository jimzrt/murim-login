# Master Edit Task — Chapter 24

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
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 지부장    | **Branch Leader**                            |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 체력               | **Stamina**                    |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 흑산도 | **Black Mountain Blade** |
| 공야청 | **Gong Yacheong** |
| 소천 | **Socheon** |
| 소율 | **Soyul** |
| 삭주 | **Sakju** | Jin Family branch location |
| 혼주 | **Honju** | Shanxi location |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 15–19

## Plot

Taekyung defeats Lee Seogeun in the duel, completing the Duel Quest and gaining three levels, the Gambler title, Fame, Fourth-Stage Cultivation, and Third-Stage Qi Sense. Lee is later killed in the departing Jin Family carriage by an unidentified masked assassin using Sound Transmission, paralysis or toxin, and a blue-black needle; “going to Mount Beimang” foreshadows his death.

The Jin Family’s belief that Taekyung is the Sleeping Dragon of Shanxi earns him additional Fame. While cultivating, he discovers a powerful unidentified energy in his dantian that rejects his contact and nearly consumes the internal energy he sends toward it. His cultivation raises his Sinews and Bones, but his Status Window still shows ten years of internal energy.

The Elder Council interrogates Taekyung over Lee’s poisoning and blames him for provoking Mount Heng. Jin Wikyung rejects the proposal to hand him over and calls for war. The Head Elder unexpectedly supports Wikyung and condemns the faction that framed Taekyung, though his political motives remain unclear. Mount Heng declares war, creating a System War relationship, designating Taekyung a public enemy, and triggering the Main Quest — War. Wikyung seals the family grounds and assumes operational control.

The Jin Family is badly outmatched: roughly 200 martial artists and three Peak masters against Mount Heng’s 300 or more martial artists and five Peak masters. With Shanxi sects refusing to answer the family’s requests for aid, Wikyung accepts assistance from Wolhwa, revealed to be Eun Sowol, the Level 50 Branch Leader of the Lower District Sect’s Shanxi branch. In exchange, she demands half of Mount Heng’s shops and exclusive rights to the pleasure district.

## Continuity

- Taekyung is Lv. 17. His Cultivation, Spear, and Manoeuvre Techniques are Fourth Stage; Qi Sense is Third Stage and detects targets through Lv. 50.
- The Main Quest still requires First Rate, Lv. 30, and Fame 500 for the reward of Logout. Taekyung has 17/30 levels and approximately 70/500 Fame.
- Taekyung’s ten years of internal energy remain insufficient for advancement despite his strong physical stats. An unidentified, much stronger energy occupies his dantian and resists control.
- The Sleeping Dragon of Shanxi rumor is spreading through the Jin Family. Taekyung deliberately confirms it, gaining 10 Fame, with later belief producing periodic Fame increases.
- Lee Seogeun is dead. His masked killer remains unidentified; the assassin used Sound Transmission, paralysis or poison, and a large blue-black needle.
- Jin Wikyung is Taekyung’s protective eldest brother and acting Family Head during the war. Wipeng remains his trusted Peak-level ally.
- The Head Elder is Taekyung’s great-uncle and the Jin Family’s highest-ranking elder. He supports Wikyung publicly, but his true plan is unresolved.
- Mount Heng Sword Sect and the Jin Family of Taiyuan are at war. Taekyung is a public enemy, and fleeing incurs severe System penalties. The family grounds are sealed without Wikyung’s authorization.
- Wolhwa is Eun Sowol, a Level 50 martial artist and Lower District Sect Branch Leader. Honghwaru is that sect’s Shanxi branch. Wikyung accepted her demand for half of Mount Heng’s shops and exclusive pleasure-district rights.
- The capsule’s purpose, the route home, and the limits of Murim’s death and resurrection rules remain unresolved.

## Translation Decisions

- Preserve **Mount Heng Sword Sect**, **Mount Beimang**, **Sleeping Dragon of Shanxi**, **Lower District Sect**, **Branch Leader**, **War relationship**, **Main Quest — War**, **First Rate**, **Peak**, **Fame**, and **Logout**.
- Keep **Sound Transmission**, **Elder Council**, **Head Elder**, **acting Family Head**, and the Jin Family’s **Cultivation**, **Spear**, and **Manoeuvre Techniques** consistent.
- Render the System’s war clause as: “Those who survive are strong, and only the strong will survive.”
- Preserve the brisk dark action-comedy and Taekyung’s dry, self-mocking profanity.
- Retain the gold-spoon/**God-Spoon** wordplay with a brief footnote where needed.
- Keep the assassination cues explicit: burning throat pain or loss of voice where applicable, paralysis or toxin effects, the Mount Beimang death idiom, and the masked assassin’s blue-black needle.

### Prior accepted reading-copy tails

#### Chapter 22 tail (verified mastered)

…
other reconnaissance squad members didn’t show their displeasure as openly as Hyuk Mujin, but they also looked at me anxiously. Everyone except one. “I’ll follow whatever the Squad Leader says!” Han Yeop shouted like a fangirl. The only difference was that he was holding a spear instead of an idol light stick. *Oh, right.* I grinned at the reconnaissance squad. “Now, raise your hand if you use a sword.” The core of party hunting was dividing up positions. * * * Raid strategies in the real world had been standardized into manuals long ago. Three tanks. Four damage dealers. Two mages and one healer. For a ten-person party, that was the ideal combination. *Of course, there are no mages or healers.* I had to balance the party as best I could using only tanks and damage dealers, but— “…You’re telling me no one knows how to use a shield?” My voice trembled at the shocking result. Good lord, all ten of them were damage dealers. Nine used swords, and Han Yeop was the only one with a spear. *What kind of horrifying single-species party is this?* A hybrid would be better. At least that would mean something had been mixed in. Hyuk Mujin spoke with an expression that suggested he couldn’t understand what was wrong. “A man ought to wield a sword.” Seeing the others nod along left me speechless. *You’ve had it way too easy. Way too easy.* Try slamming your head into a pool of blood and see if you still talk like that. Sword? Spear? There was no such distinction. You bashed people with whatever rock you happened to grab, threw dirt, climbed on top of them, and bit them with your teeth. On the line between life and death, anything in your hand was a weapon and a lifeline. These people had only ever fought bandits at best. They still didn’t understand that. *Do I need to start training them tomorrow?* Not for their sake. For my survival. Even teaching them a few tricks would make a real difference in a melee. *I worked like a dog for seven years. I can’t die because of a bunch of rookies.* That was when it happened. Ding. Ding. Ding. A great bell tolled three times. Here, where no one could tell the exact time, bells were rung at set intervals. The three tolls that had just sounded marked Mi-si, roughly one to three in the afternoon.[^1] And— “Get ready. This is our first deployment.” They also signaled the reconnaissance squad’s first mission. * * * “He should be doing fine.” Jin Wikyung looked up at Wipeng’s abrupt comment. Until a moment ago, he had been staring blankly at a teacup as it slowly cooled. “What are you talking about?” “The Third Young Master.” A full day had passed since the reconnaissance squad led by Jin Taekyung departed from the Jin Family of Taiyuan. Their mission was to scout the county towns near the Jin Family. “They left around noon yesterday, so they should arrive within two days.” “Ah. Taekyung.” Jin Wikyung let out a weak laugh. He looked exhausted. “I thought you meant something else. That’s not it.” “It’s not?” “How long are you going to treat him like a child? He’s a grown man now. I’m sure he’ll manage on his own.” “…I’m beginning to doubt my ears.” “I did coddle him quite a bit. He was very young back then.” “I agree, to some extent. He’s changed considerably over the past few days.” “Heroes grow by overcoming adversity.” “…” “Anyway, I can stop worrying about the youngest now. I’ll be able to focus more on the main family.” “You should rest for a while. You look tired.” “Wipeng. Members of our family have died.” Wipeng fell silent at the sorrow and determination in his voice, and Jin Wikyung returned to his work. But the silence broke after a mere two hours. “What is that…?” A black dot in the sky was gradually drawing closer. The messenger hawk spread its enormous wings and landed by the office window. It belonged to the Lower District Sect. Jin Wikyung hurriedly stood and opened the tube fastened to the hawk’s leg. The moment he unfolded the letter, tiny writing caught his eye. > One Question, One Kill Jopil and twenty members of a special detachment have appeared in Jeongyang. “Jeongyang…!” Beyond Jeongyang lay Honju. Beyond Honju lay Taiyuan. Even for a special detachment, he had never expected them to cover hundreds of li in only a few days. That wasn’t all. There were still family members from the branches who had not returned to the main family. What if the enemy was tracking them? *Every moment counts.* It didn’t take Jin Wikyung long to decide. “Select fifty martial artists immediately and send them to Jeongyang. One Question, One Kill Jopil is a brutal Peak master. Bring our family members—” He thought of the children. Their small limbs. Their faces twisted in pain. Their vacant eyes. Jin Wikyung clenched his teeth. “Bring our family members home safely.” “My lord.” Wipeng’s expression had hardened. Jin Wikyung stared blankly at him as though something had taken hold of him, then opened his mouth. “Taekyung. Where did you say Taekyung went?” His voice came out strained. “…Jeongyang.” [^1]: Mi-si is one of the traditional two-hour divisions of the day, corresponding roughly to 1–3 p.m.

#### Chapter 23 tail (verified mastered)

…
sprayed through the air in slow motion. His pupils were unfocused, and his legs hung limp. Yet somehow, he didn’t fall. He couldn’t—not unless I let go of his fist. “Five.” Smack! That was his limit. Hyuk Mujin could no longer endure and passed out. Something fell with a soft thud onto his body, sprawled out in a bizarre position. *Snow?* I raised my head toward the sky. The winter sky was raining down small white scraps of garbage. “Rest is over. We’re leaving.” I tossed out the words and turned away. Behind me, the reconnaissance squad members finally released the breaths they had been holding. * * * When Hyuk Mujin woke two hours later, the first thing he did was charge at me. “You fucking—!” Smack. Thud. “Move him.” “Y-yes, sir!” Another satisfying slap knocked him out cold. The other reconnaissance squad members dragged him into a corner of the cabin. *A cabin. We got lucky.* According to one squad member who knew the surrounding area well, we should have reached Jeongyang before sunset at the latest. But there was nothing we could do about the sudden heavy snowfall, and this cabin was the only place we had managed to find. Apparently, it was a hunters’ shelter known only to people familiar with the area. *It’s ridiculously small, but I’ll take it.* The mission might be delayed, but this was a hundred times better than walking through the snow all night and then running into the enemy while utterly exhausted. That was when— “Squad Leader?” It was Han Yeop. Behind him, the other squad members stole glances at me, trying to gauge my mood. “What should we do now?” “Hm? Sleep.” “N-no, that’s not what I meant…” As I looked at the fidgeting reconnaissance squad members, a thought struck me. *Don’t tell me…* “Do you want to train?” Nod, nod. Look at those heads bobbing furiously. Look at those eyes burning with enthusiasm. *Forget seeing once. One beating beats hearing something a hundred times.* One beating really was better than a hundred explanations. * * * It was around noon. Sunlight flashed along a sword blade. That was the only thing the martial artist managed to see. “Urgh.” Thud. His knees buckled, and his face slammed into the frozen ground. Blood poured from the gaping wound that ran from his shoulder to his chest. There was no recovering from an injury like that. The martial artist knew he was going to die. “The others… Please, spare them.” His exhausted voice cut off abruptly. Looking at the martial artist’s wide-open eyes, a middle-aged man clicked his tongue. “Good grief, you poor fool.” What were you thinking, charging in like that? The rest of his words never reached the dead man. The fifty-odd wandering martial artists surrounding them snickered. “Of all people, he had to run into the boss. What rotten luck.” “Only an orthodox-faction bastard would keep playing the hero right to the bitter end. What should we do, Boss?” Their gleaming eyes turned toward the remaining survivors—a group of six or seven women and children. “Great Hero, please spare the children.” At the plea from the oldest-looking woman, the middle-aged man—One Question, One Kill Jopil—smiled gently. “I’m sorry, but what can I do? I’m no Great Hero.” “But you’re still human. How can you kill children who can’t even tell right from wrong?” “Hah. You have quite a bit of spirit for a woman. Wait. I heard the Sakju Branch Leader’s family survived. Could you be…?” “He is my husband.” “Ah, I thought so. Who would have imagined such a pathetic man could have such a virtuous wife?” Jopil smiled, and the woman’s expression hardened. “You have no intention of sparing us.” “Don’t worry. I’m not in the habit of raping women before I kill them.” “The children…” “This is a harsh world. How could little ones survive without their mother?” “You’re worse than a beast.” “I heard your last words.” That was the signal. Swordlight flashed, and screams rang out. A short while later, the blood-soaked wandering martial artists tossed the corpses into the mountain thickets. “Looks like the wild animals will be the only ones feasting.” The man with tiny, birdlike eyes muttered. He was Jopil’s right-hand man, a first-rate wandering martial artist known as Black Mountain Blade. “We should feast, too. If we finish this job properly, what’s a mere thousand pieces of gold?” Jopil laughed with pleasure. The payment for this job would be enormous, but the situation itself was what he enjoyed. “I never imagined the day would come when we’d hunt the Jin Family of Taiyuan.” He planted a filthy leather shoe on the fallen martial artist’s corpse. The martial artist had belonged to the Sakju Branch, one of the ten or so branches of the Jin Family of Taiyuan. “Was that the last of them?” “No, Boss.” “They’re slipping away like rats. How many?” “Three in total. One martial artist and two children. They passed through Jeongyang only a few hours ago and are heading for Honju.” “That’s troublesome. It’ll take half a day.” “There’s no need for you to go yourself, Boss. I’ll take care of it.” “Would you?” A pleased smile spread across Jopil’s lips. “Good. Take half the men. You have half a day. How does that sound?” The answer was already decided. Black Mountain Blade bowed deeply.

## Korean source

```text
＃24화



뛰었다. 그저 뛰는 것밖에 할 수가 없었다.

아버지가, 가족처럼 지내던 삭주지부의 식솔들이 죽어 나가도 열네 살 소년이 할 수 있는 일은 단 하나, 도망치는 것뿐이었다.

“오빠, 추워.”

품에 안긴 여동생이 칭얼거렸다. 소년, 소천은 추위에 얼어붙은 동생의 손에 호호 입김을 불었다.

“거의 다 왔으니까 조금만 참아. 응?”

“집 언제 가? 소율이는 엄마 보고 싶은데…….”

“어제도 오셨는걸.”

“거짓말. 오빠도 봤어?”

“그럼, 봤지.”

꿈속에서. 소천은 이어지는 말을 꿀꺽 삼켰다.

지난 밤 꿈에 나타난 어머니는 사흘 전과 똑같았다. 지쳐 잠든 소율이를 한참 동안이나 쓰다듬고 바라보다가 말씀하셨다.



‘살아남아라. 반드시 살아남아야 한다.’



그 목소리가, 다른 사람들을 이끌고 떠나던 그 뒷모습이 아직도 눈앞에 아른거렸다.

‘어머니는 어떻게 되셨을까. 혹시…… 아니, 아니다. 그럴 리 없어.’

불길한 느낌을 애써 억누르던 그때였다.

부스럭.

“누구냐!”

어린 누이를 끌어안는 동시에 품고 있던 비수를 꺼내는 일련의 동작이 자연스럽다.

집이 불타고 수많은 죽음을 목격한 그날 밤 이후, 쾌활하던 소년은 짐승의 눈빛을 갖게 됐다.

“셋을 세겠다. 하나, 둘…….”

“나다.”

어둠 속에서 불쑥 나타난 얼굴에 비수가 스르르 내려갔다.

“공 숙부?”

“쉿. 목소리를 낮추어라.”

공 숙부라 불린 이는 지친 얼굴의 중년인이었다. 삭주 지부장인 소천의 아비와는 오랜 지기로, 현재는 어린 남매의 길잡이이자 보호자이기도 했다.

“반 시진이 넘도록 안 오시기에 걱정했습니다.”

“주의해야 했다. 꼬리가 붙었어.”

“벌써 말입니까?”

“그래. 한시가 급하다.”

소천은 망설이지 않고 일어났다. 영문을 몰라 하는 소율을 들쳐 업은 공 숙이 풀숲을 헤치며 앞장섰다.

“어디로 가는 것입니까?”

“혼주. 제아무리 잔악무도한 놈들이라고 해도 그곳까지 쫓아오지는 못할 것이다.”

과연 그럴까. 소천은 의구심이 들었다.

이미 삭주 지부가 무너졌다. 건물은 불탔고 모두가 죽었다. 놈들의 정체는 모르지만 목적은 확실했다.

‘몰살.’

떠오른 단어를 입김에 날려 보낸다. 소천은 다시 걷기 시작했다.

그렇게 얼마나 걸었을까, 진눈깨비처럼 흩날리던 흰 눈이 종아리까지 차오른 순간이었다.

“조용히.”

앞서 걷던 공 숙의 발걸음이 멈췄다. 소천도 덩달아 숨을 죽였다. 세찬 바람 소리. 앙상한 나뭇가지들이 서로 부딪치는 소리…… 단지 그뿐이었다.

그러나 소천은 직감했다.

“놈들입니까?”

공 숙이 딱딱하게 굳은 얼굴로 대답했다.

“최소 십여 명. 곧 따라잡힐 것이다.”

암담한 상황이다. 하지만 이상하게도 소천의 마음은 차분하게 가라앉았다.

“내 불찰이다. 눈이 내리기 전에 서둘렀어야 하는 것을…… 하늘이 원망스럽구나.”

“숙부께서는 최선을 다하셨습니다.”

소천은 품에서 비수를 꺼내 들었다. 일 년 전 아버지에게 물려받은 비수. 아버지가 남긴 유일한 흔적이다.

“저도 하찮게나마 무공을 배운 몸. 무인답게 싸우다 죽겠습니다.”

“……아직 포기하기에는 이르다.”

공 숙이 할 수 있는 말은 그것뿐이었다. 그들은 얼마 남지 않은 힘을 끌어 올려 이동을 시작했다.

하지만 며칠간 밤낮 없는 도주로 한계에 다다른 체력이 발목을 잡았다. 걸음이 점점 느려지고, 숨이 가빠진다.

“여기다!”

“거의 다 따라잡았어!”

이제는 소천도 들을 수 있었다. 추격자들의 목소리와 그들이 밝힌 횃불이 점점 가까워진다.

그때, 공 숙이 곤히 잠든 소율을 소천에게 건넸다.

“뒤따라가마.”

“숙부!”

“걱정마라. 이 공야청, 그리 호락호락한 놈이 아니다.”

“그래도 어찌…….”

“어서!”

소천은 공야청을 뒤로하고 다시 산을 올랐다. 한계에 다다른 체력, 하지만 멈추지 않았다.

그렇게 눈 덮인 산의 언덕에 다다랐을 때, 병장기 부딪치는 소리와 누군가의 비명이 울려 퍼졌다.

‘공 숙부.’

소천은 이를 악물었다. 당장이라도 비수를 뽑아 들고 저 아래로 뛰어들고 싶었다. 하지만…….

‘참자. 참아야 한다.’

지난 닷새 동안 수백, 수천 번을 다짐했다. 꼭 살아남겠다고, 품 안의 여동생을 지키고 흉수들에게 복수하겠노라고.

언덕 위, 소천은 불길이 쏟아지는 눈동자로 일렁이는 횃불들을 바라봤다.

‘나는 반드시 살아남는다.’

그리고 등을 돌려 언덕을 오른 다음 순간, 소천은 벼락 맞은 것처럼 몸을 떨었다.

“아, 아아…….”

언덕 위 너른 공터, 남색 무복을 입은 열 명의 사내가 소천을 바라보고 있었다.

가슴에 수실로 새겨 넣은 진(陳)이라는 한 글자가 크게 보였다.



* * *



이상한 낌새를 느낀 것은 훈련을 막 시작하려던 찰나였다.

세찬 바람 너머로 언뜻 들리는 소리. 공력을 끌어 올리자 더욱 선명해지는 그것의 정체는…….

‘사람 목소리?’

어림잡아도 열 명은 넘어가는 듯했다. 어떻게 이제야 눈치챘을까 싶을 정도로 가까운 거리다.

‘이 날씨에 저 정도 인원이라…….’

좋아, 결심했다.

“짐 싸라.”

“예?”

각자 무기를 들고 훈련을 준비하던 조원들이 어리둥절한 얼굴로 되묻는다.

“빨리 짐 싸. 한 명은 들어가서 혁무진…….”

“조장님. 저기 웬 꼬마가 있는데요?”

젠장. 진짜네. 조그만 아이를 업은 꼬마가 멍하니 우리를 바라보고 있었다.

“쟤 누구야.”

“모르겠는데요. 이 오두막 주인인가?”

제발 그랬으면 좋겠다. 하지만 뒤에 따라오는 놈들이 화목한 대가족 구성원이라는 생각이 들지 않는 건 왜일까.

“우는데요?”

누군가의 말처럼, 꼬마는 울고 있었다. 하염없이 펑펑 울면서 뛰고 있었다. 문제는 방향이다.

“어어, 이쪽으로 오는데…… 조장님 어디 가세요?”

의혹 어린 눈빛들이 나를 향했다. 나는 이미 멀찍이 뒤로 물러난 상태였다.

“말 타러. 슬슬 출발해야지.”

“이 날씨에요? 말도 못 움직일 텐데.”

“그래? 그럼 버리고 가자.”

“예?”

“원래 임무라는 게 그래. 눈이 오건 비가 오건 우리는 할 일을 해야지. 입 다물고 짐이나 챙겨.”

“그래도…….”

“짐 챙겨! 혁무진 깨워!”

불과 일 다경 전까지 우러러보던 시선은, 이제 정신병자를 보는 시선으로 바뀌어 있었다.

“갑자기 왜 이러세요?”

왜 이러긴. 느낌이 더럽게 안 좋으니까 그렇지.

이제 척하면 척이다. 꼬마가 가까워질수록 빅 엿의 냄새가 강하게 풍겨 오고 있다.

어떤 전개가 벌어질지 눈에 선했다. 방법은 하나뿐이다.

“그럼 나만 먼저 내려가 있을…….”

그 순간, 함성 소리와 함께 불청객들이 언덕 위로 모습을 드러냈다. 무려 이십여 명에 달하는 남자들이다.

‘아, 시발.’

띠링.



- [돌발 퀘스트]가 생성되었습니다!



퀘스트



[삭주 지부의 생존자]

당신은 태원진가 삭주지부의 생존자들과 마주쳤습니다.

항산검문의 잔인무도한 추격자들에 맞서 생존자들을 구해 내십시오!



등급 : 돌발 퀘스트

제한 : 진태경

임무 : 생존자 구출 (미완료)

보상 : 연계 퀘스트

???

실패 : ???





“…….”

“…….”

우리는 놈들을 봤다. 놈들도 우리를 봤다. 얼어붙은 공터에 죽음 같은 침묵이 흘렀다.

‘이럴 줄 알았어. 이렇게 될 줄 알았어.’

하지만 후회해도 늦었다. 내 팔자가 더러운 걸 어쩌겠나.

나는 한숨을 푹 내쉬고 외쳤다.

“공격 대형. 펼쳐!”

차차착. 갑작스러운 상황이었지만 조원들은 가르친 대로 움직였다. 순식간에 대형이 갖춰질 때쯤, 놈들도 우리의 정체를 깨닫고 고함을 내질렀다.

“태원진가의 애송이들이다!”

“머릿수도 얼마 안 돼. 쓸어 버려!”

애송이. 딸리는 머릿수.

족집게처럼 골라낸 팩트가 가슴을 헤집는다.

아직 다 가르치지도 못했는데, 이놈들 무공도 낮고 실전 경험도 없어서 완전 신병인데…….

‘안 되면 나 혼자라도 튀어야 하나.’

나는 암담함을 느끼며 [기감]을 사용했다. 내 눈에만 보이는 푸른 기의 물결이 괴성을 지르며 달려드는 적들을 훑는다.

띠링. 띠링. 띠링.



[Lv.12] [Lv.11] [Lv.12]



“……응?”

그때 정찰조원들이 새파랗게 질린 얼굴로 외쳤다.

“어떻게 합니까?”

“옵니다, 와요!”

“조자아아앙!”

30m, 20m…… 빠른 속도로 쇄도하는 적들을 바라보며 입을 뗐다.

“걱정하지 마라. 적들은 단순한 경험치…… 아니, 오합지졸에 지나지 않는다. 단!”

“단?”

“온 힘을 다해 막아라. 막기만 해.”

“예? 그게 무슨 말씀이십니까.”

무슨 말씀이긴. 막타 치지 말라는 소리다.

“수비 대형, 펼쳐!”

응. 경험치 다 내 거.



* * *



“조장!”

“안 됩니다. 조자아앙!”

“조장이 자살하러 갔다!”

그런 거 아니야, 미친놈들아. 나는 정찰조원들의 비명을 뒤로하고 적들을 향해 뛰어들었다.

단전에서 솟구친 공력이 사지백해로 뻗쳐 나간다.

“미친놈.”

선두의 적이 누런 이빨을 드러내며 웃는다.

나도 마주 웃어 주었다.

“예쁜 놈.”

“뭐?”

서걱.

목을 움켜쥐고 고꾸라지는 녀석을 스쳐 지나가는 순간. 기다리던 목소리가 들렸다.

띠링.



- 경험치를 획득했습니다.

- 50의 공적치를 얻었습니다!



“뭐, 뭐야!”

“이 개새끼가 감히…….”

적들의 면면은 실로 훌륭했다. 얼굴에 칼자국은 기본 옵션이요, 위생 상태도 심히 안 좋아 악취가 코를 찔렀다.

그런데…….

“어우, 좋다.”

꽃밭에 있는 기분이다. 경험치라는 꿀을 머금고 있는 스무 송이의 꽃들. 나는 행복한 얼굴로 꽃송이에 달려들어 꿀을 빨았다.

푹. 푹. 푹.

띠링. 띠링. 띠링.



- 경험치를 획득했습니다.

- 50의 공적치를……

- 경험치를 획득…….

- 50의 공적치…….



거침없이 그 사이를 헤집었다. 눈 깜짝할 사이에 선두가 무너지고 적들이 자신도 모르게 주춤거린다.

‘그러면 고맙지.’

진가보법과 진가창법은 전진에 기반을 둔 무공이다.

나는 보법을 밟아 나갔다. 중심으로 파고들며 창을 휘둘렀다.

“크악!”

“으아아악!”

예리한 창의 육중한 무게에 패도적인 창법까지. 더군다나 갈수록 적들이 물러서는 상황.

진가창법이 진가를 발휘할 시간이었다.

‘일 초식.’

보법과 함께 창을 휘두르기 시작했다. 한 번 휘두르고 내질러질 때마다 누군가의 비명과 피가 터져 나온다.

“컥.”

“꺼흐으윽.”

이 초식, 삼 초식. 사 초식.

어느 순간 나는 흐름에 몸을 맡겼다. 물결이 파도가 되고, 파도에 적들이 휩쓸린다. 전신의 감각이 오싹할 정도로 곤두섰다.

더, 더, 더…….

“이 개새끼가아!”

푹. 푸푹.

목, 가슴, 복부. 차례대로 찌르고 베어 낸다. 사망자 확인은 시스템 알림이 대신해 주었다.

그렇게 얼마나 지났을까. 땅에 발을 딛고 서 있는 자는 한 사람이 유일했다.

“대, 대형께서 반드시 널 찾아…….”

기다리지 않았다.

파도는 흐름이다. 그리고 마지막 파도가 내 창끝에서 터져 나왔다. 진가창법의 마지막 초식, 천관일(天貫軼).

푸화악!

마지막 한 사람, 뱁새눈은 조각조각 난 검을 바라보다가 그대로 무릎을 꿇었다. 놈의 가슴 한복판이 포탄에 맞은 것처럼 터져 나가 있었다.

띠링.



- [Lv.32 흑산도]를 처치하셨습니다!

- [생존자] 퀘스트를 완료했습니다!

- 연계 퀘스트가 생성되었습니다!

- 경험치를 대량 획득합니다!

- 공적치를 대량 획득합니다!

- 레벨이 올랐습니다!

- 레벨이 올랐습니다!

- 레벨이…….



쉼 없이 들리는 시스템 알림을 들으며 나는 배를 쓰다듬었다.

“꺼윽.”

어우, 배불러.
```

## Current accepted English baseline

```markdown
# Chapter 24

He ran. It was the only thing he could do.

Even as his father and the people of the Sakju Branch who had been like family to him died one after another, there was only one thing a fourteen-year-old boy could do: run.

“Oppa, I’m cold.”

His little sister whimpered in his arms. The boy, Socheon, blew warm breath onto her hands, which had gone stiff with cold.

“We’re almost there, so just hold on a little longer. Okay?”

“When are we going home? Soyul wants to see Mom…”

“She visited yesterday, too.”

“You’re lying. Did you see her?”

“Of course I did.”

*In my dream.*

Socheon swallowed the words that followed.

His mother had appeared in his dream the night before, exactly as she had three days earlier. She had spent a long time stroking and gazing at Soyul, who had fallen asleep from exhaustion, before speaking.

*Survive. You must survive.*

Her voice still rang in his ears, and the sight of her back as she led the others away still shimmered before his eyes.

*What happened to Mother? Could she have…? No. That can’t be.*

It was then, as he struggled to suppress his ominous feelings, that he heard something.

Rustle.

“Who’s there?”

The sequence of movements came naturally: pulling his little sister close while drawing the dagger from inside his clothes.

After the night when his home had burned and he had witnessed countless deaths, the cheerful boy had gained the eyes of a wild beast.

“I’ll count to three. One, two…”

“It’s me.”

The dagger slowly lowered when a face suddenly appeared from the darkness.

“Uncle Gong?”

“Shh. Keep your voice down.”

The man called Uncle Gong was a middle-aged man with a weary face. He had been an old friend of Socheon’s father, the Branch Leader of the Sakju Branch, and was now the young siblings’ guide and protector.

“I was worried because you hadn’t returned for more than half a shichen.[^1]”

“I should have been more careful. We have a tail.”

“Already?”

“Yes. Every moment counts.”

Socheon stood without hesitation. Uncle Gong hoisted the bewildered Soyul onto his back and led the way through the brush.

“Where are we going?”

“Honju. No matter how cruel those bastards are, they won’t pursue us that far.”

*Will they really not chase us that far?*

Socheon had his doubts.

The Sakju Branch had already fallen. The building had burned, and everyone was dead. He did not know who the attackers were, but their purpose was clear.

*Massacre.*

He blew the word away with his breath and started walking again.

How long had they walked?

The white snow, which had been drifting down like sleet, had risen to their calves when—

“Quiet.”

Uncle Gong stopped walking. Socheon held his breath as well. The only sounds were the howling wind and the clatter of bare branches striking one another.

But Socheon knew instinctively.

“Is it them?”

Uncle Gong answered with a rigid expression.

“At least ten. They’ll catch up soon.”

The situation was bleak. Yet strangely, Socheon’s heart settled into a calm stillness.

“It was my fault. I should have hurried before the snow began… I curse the heavens.”

“You did everything you could, Uncle.”

Socheon drew the dagger from inside his clothes. It had been handed down to him by his father a year ago—the only trace his father had left behind.

“I’ve learned a little martial arts myself. I’ll fight and die like a martial artist.”

“…It’s too soon to give up.”

That was all Uncle Gong could say. They summoned what little strength they had left and started moving again.

But their stamina, pushed to its limit by days and nights of nonstop flight, dragged at their feet. Their steps grew slower, and their breathing became labored.

“There!”

“We’re almost on them!”

Now Socheon could hear them, too. The pursuers’ voices and their torchlight were drawing closer.

At that moment, Uncle Gong handed the soundly sleeping Soyul to Socheon.

“I’ll bring up the rear.”

“Uncle!”

“Don’t worry. This Gong Yacheong isn’t such an easy man to take down.”

“But how can you…”

“Go!”

Socheon left Gong Yacheong behind and started up the mountain again. His stamina was at its limit, but he did not stop.

When he reached a hill on the snow-covered mountain, the clash of weapons and someone’s scream rang out.

*Uncle Gong.*

Socheon gritted his teeth. He wanted to draw his dagger and leap down there immediately. But…

*Hold on. I have to hold on.*

He had repeated those words hundreds, thousands of times over the past five days. He had sworn that he would survive, protect the little sister in his arms, and take revenge on the murderers.

From the hilltop, Socheon stared at the flickering torches with eyes that seemed to pour fire.

*I will survive.*

Then he turned his back and climbed the hill. The next moment, his body shook as if struck by lightning.

“A-ah…”

Ten men in navy martial uniforms were looking at Socheon from the wide clearing atop the hill.

A single character, 陳—the character for Jin—was prominently embroidered in silk thread across their chests.

* * *

I sensed something strange just as we were about to begin training.

A sound carried faintly over the howling wind. When I raised my internal energy, the sound grew clearer.

*A human voice?*

There had to be more than ten people. They were close enough that I wondered how I had failed to notice them until now.

*That many people in this weather…*

All right. I’d made up my mind.

“Pack your things.”

“Huh?”

The squad members, who had been preparing for training with their weapons in hand, stared at me, baffled.

“Pack up, quickly. One of you, go inside and get Hyuk Mujin—”

“Squad Leader. There’s a kid over there.”

Damn it. There really was one.

A little boy carrying an even smaller child on his back was staring blankly at us.

“Who’s that?”

“I don’t know. Is he the owner of this cabin?”

*Please let that be the case.*

But why did I find it so hard to believe that the people following him were members of one happy, extended family?

“He’s crying.”

As someone pointed out, the boy was crying. He was running while sobbing his heart out.

The problem was where he was headed.

“Uh, he’s coming this way… Squad Leader, where are you going?”

Suspicious gazes turned toward me. I had already retreated a good distance.

“I’m going to ride a horse. We should be leaving soon.”

“In this weather? The horses won’t even be able to move.”

“Really? Then we’ll leave them behind.”

“What?”

“That’s how missions work. Snow or rain, we still have a job to do. Shut up and pack your things.”

“But still…”

“Pack your things! Wake Hyuk Mujin!”

The admiring looks I’d enjoyed barely fifteen minutes ago had now turned into the sort reserved for a lunatic.

“What’s gotten into you all of a sudden?”

*What’s gotten into me?*

I had a really bad feeling about this.

By now, I knew the signs. The closer the kid got, the stronger the stink of a huge shitshow grew.

I could see exactly how this would play out. There was only one way out.

“Then I’ll head down first by my—”

At that moment, the uninvited guests appeared over the hill amid a chorus of shouts.

There were more than twenty men.

*Oh, fuck.*

Ding.

> **System**
>
> - Sudden Quest has been created!
>
> **Quest**
>
> **Survivors of the Sakju Branch**
>
> You have encountered survivors from the Sakju Branch of the Jin Family of Taiyuan.
>
> Rescue the survivors from the Mount Heng Sword Sect’s merciless pursuers!
>
> **Grade:** Sudden Quest
> **Limit:** Jin Taekyung  
> **Task:** Rescue the survivors — Incomplete  
> **Reward:** Chain Quest  
> ???  
> **Failure:** ???

“…”

“…”

We looked at them. They looked at us.

A deathly silence settled over the frozen clearing.

*I knew it. I knew this was how it would turn out.*

But regret was useless now. What could I do about my cursed luck?

I let out a deep sigh and shouted.

“Attack formation. Form up!”

Clack-clack-clack. Caught off guard, the squad members nevertheless moved as they had been taught. By the time they had formed up, the enemy had realized who we were and started shouting.

“They’re brats from the Jin Family of Taiyuan!”

“There aren’t many of them. Wipe them out!”

*Brats. Outnumbered.*

Those two facts hit me right in the chest.

I hadn’t even finished teaching them. Their martial arts were weak, they had no real combat experience, and they were complete rookies.

*If things go bad, should I bolt by myself?*

Feeling utterly hopeless, I used Qi Sense. Blue waves of qi, visible only to me, swept over the enemies charging forward with shrieks.

Ding. Ding. Ding.

> **System**
>
> - Level 12
> - Level 11
> - Level 12

“…Huh?”

The reconnaissance squad members turned deathly pale.

“What do we do?”

“They’re coming! They’re coming!”

“Squad Leadeeeer!”

As I watched the enemies rush toward us at incredible speed—thirty meters, twenty meters—I opened my mouth.

“Don’t worry. The enemy is nothing but simple EXP… I mean, a rabble. But!”

“But?”

“Stop them with everything you have. Just hold them back.”

“What? What do you mean?”

*What do I mean?*

*Don’t get the last hit.*

“Defensive formation. Form up!”

Yes. All the EXP was mine.

* * *

“Squad Leader!”

“No! Squad Leadeeeer!”

“The squad leader went to commit suicide!”

That wasn’t what I was doing, you lunatics.

I ignored the reconnaissance squad members’ screams and charged toward the enemies.

Internal energy surged from my dantian and spread through my limbs and bones.

“You crazy bastard.”

The enemy at the front grinned, baring yellow teeth.

I grinned back.

“Pretty boy.”

“What?”

Slash.

The man clutched his throat and collapsed. As I passed him, the voice I had been waiting for rang out.

Ding.

> **System**
>
> - You gained EXP.
> - You gained 50 Merit!

“What the—!”

“How dare this fucking bastard…”

The enemies were a spectacle in their own way. Facial scars were standard equipment, and their poor hygiene produced a stench that stabbed at my nose.

And yet…

“Ah, this is great.”

I felt like I was in a flower garden.

Twenty flowers filled with the sweet honey of EXP.

I charged into them with a blissful expression and sucked out the honey.

Stab. Stab. Stab.

Ding. Ding. Ding.

> **System**
>
> - You gained EXP.
> - You gained 50 Merit!
> - You gained EXP…
> - You gained 50 Merit…
> - You gained EXP…
> - You gained 50 Merit…

I tore through their ranks.

The front line collapsed in an instant, and the enemies instinctively began to falter.

*That works for me.*

The Jin Family’s Manoeuvre Technique and Spear Technique were martial arts built around advancing.

I advanced with the Manoeuvre Technique, drove into their center, and swung my spear.

“Gaaah!”

“Aaaargh!”

The spear was razor-sharp and massively heavy, and the technique was domineering to boot. On top of that, the enemies were steadily backing away.

It was time for the Jin Family’s Spear Technique to show its true worth.

*First form.*

I began swinging the spear in step with my footwork. Every swing and thrust brought forth someone’s scream and a burst of blood.

“Ghk.”

“Grrrgh.”

Second form. Third form. Fourth form.

At some point, I surrendered myself to the flow.

The ripples became waves, and the enemies were swept away by them. Every nerve in my body stood on end.

More. More. More…

“You fucking bastard!”

Stab. Slash.

Throat, chest, abdomen.

I stabbed and cut them down one after another. The System alerts confirmed the fatalities for me.

How much time passed?

Only one person remained standing.

“Our boss will find you no matter what…”

I didn’t wait.

A wave is momentum. The final wave burst from the tip of my spear.

The final form of the Jin Family’s Spear Technique:

*Sky-Piercing Strike*.

Splurt!

The last man, the one with the narrow birdlike eyes, stared at his sword, which had been shattered into pieces, before dropping to his knees.

The center of his chest had burst open as if struck by a cannonball.

Ding.

> **System**
>
> - You defeated **Level 32 Black Mountain Blade**!
> - You completed the **Survivors of the Sakju Branch** Quest!
> - A Chain Quest has been created!
> - You gain a large amount of EXP!
> - You gain a large amount of Merit!
> - You have leveled up!
> - You have leveled up!
> - You have leveled…

As the System alerts continued without pause, I rubbed my stomach.

“Buuurp.”

Ah, I’m stuffed.

[^1]: A shichen is a traditional Chinese time period of roughly two hours.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 24`.

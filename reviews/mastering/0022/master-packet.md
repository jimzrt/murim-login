# Master Edit Task — Chapter 22

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
| 혁무진    | **Hyuk Mujin**     |
| 조필     | **Jopil**          |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 하오문    | **Lower District Sect**          |
| 이류     | **Second Rate**   |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 레벨               | **Level**                      |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 탱커      | **tank**              |
| 힐러      | **healer**            |
| 마법사     | **mage**              |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 한엽 | **Han Yeop** |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
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

#### Chapter 20 tail (verified mastered)

…
carried the air of a master. He was the coachman who had brought me to the Jin Family of Taiyuan a few days ago. I never expected to see that face here. I was momentarily speechless, and Wolhwa spoke up. “I hear you two are acquainted. Last time, you crossed the boundary between life and death together and forged a deep friendship that transcended age and status…” *No. That isn’t what happened. Please stop.* I tugged at Wolhwa’s sleeve, but it was already too late. The coachman smiled gently and opened his mouth. “Even now, whenever I close my eyes, the memories of that day remain vivid. The Heavenly Axe… He was a truly strong bastard.” The gate guards, who had been listening intently, exclaimed in amazement. “Oh!” “The Heavenly Axe… Surely he means that Heavenly Axe of the Eighteen Strongholds of Green Forest?” “Wasn’t he the infamous Peak master of Green Forest? To kill a man like that, as expected, this gentleman must be…” “…” They seemed to have gotten something seriously wrong. I didn’t even know where to begin correcting them—or where to stop. While I stood there blankly, the coachman grabbed me in a hug. “If it hadn’t been for you, Young Master, I would have been in serious trouble.” This man certainly had a strange way of putting things. Without me, he would have been drinking a cup of makgeolli atop Mount Beimang by now.[^1] “Please let go of me first, then we can talk…” I was just about to pry him off when someone muttered, “Yama Whip. The master of the whip arts who vanished without a trace more than ten years ago. It’s him. It has to be.” A ripple passed through the gate guards. “Yama Whip? You mean that Peak master who roamed the realm beating down remnants of the Demonic path?” “I’ve heard that name, too. A master who stood between the orthodox and unorthodox paths, with neither his sect nor his past known… Come to think of it, didn’t his trail vanish somewhere near Shanxi?” “Then the Third Young Master—no, our Young Master—is acquainted with Great Hero Yama Whip.” “And not only that. He must have played a major role in taking down the Heavenly Axe.” “Oh! Ohhh!” Fervent gazes poured in from every direction. Perhaps sensing that something was wrong, the coachman tried to pull away, but my hand was gripping his shoulder tightly. “Young Master?” I gave him the brightest smile in the world. “To meet you again like this—Yama. Whip. Great Hero!” My words were like oil thrown onto a fire. “Woooah!” The overheated gate guards stomped their feet, while Wolhwa bent over, desperately trying to hold back her laughter. Ding. > **System** > > - Rumors about the **Poisoner** are dying down! > > - Rumors about the **Sleeping Dragon of Shanxi** are gaining credibility! > > - **Fame** increases by 20! > > - Passionate supporters have appeared! As the beautiful System notifications rang out, a famous saying came to mind. *The perfect lie… is a true story.* * * * The young man stared at the ceiling with his eyes wide open. The light had gone out of his once-bright black eyes, and his face was twisted with fear and pain. “Seogeun. My son.” A large, rough hand caressed the young man’s face. Intense poisonous energy seeped through the man’s skin, only to be stopped by the internal energy that instinctively surged within him. “How did this happen to you?” The middle-aged man lamented. He had grown up a complete orphan and spent decades in Murim. He had met countless people and watched countless people leave. From the days when he was a green twenty-year-old wandering martial artist to the moment he became the master of a sect, his memories were beyond counting. “Did it hurt? Were you so wronged that you couldn’t even close your eyes?” He quietly looked down at his son’s wide-open eyes. Every tiny blood vessel had burst, staining his eyes red. His son was barely twenty. Blood tears flowed from the eyes of a father who stood before his poisoned son. “My son.” The poisonous energy that had entered through his hand was spreading throughout his body. Within only a few breaths, his head began to spin and his limbs went numb. Such a deadly poison. He could vividly picture his son’s final moments—his entire body stiffening until he couldn’t even struggle. “I will remember this pain.” The next moment, powerful internal energy rose like a wildfire and drove the poisonous energy away. The poison that had been consuming his insides vanished in an instant, as if it had been torn apart by a pack of hundreds of wolves. “I’ll pay those bastards back a hundredfold. A thousandfold.” The Sect Leader of the Mount Heng Sword Sect, Blood Wolf Sword Lee Cheonbaek, left his son’s corpse behind and walked away. When he opened the pavilion door, he saw the black night sky and the flickering torches beneath it. A group of about two hundred fully armed men stood outside. The man at the front bowed his head. “Father.” Lee Cheonbaek nodded to his eldest son. “Go. Tonight… our revenge begins.” That night, about two hundred martial artists left the Mount Heng Sword Sect. [^1]: A reference to Mount Beimang, a famous burial ground traditionally used as a symbol of death.

#### Chapter 21 tail (verified mastered)

…
first time the Head Elder had spoken to me. “Greetings, Head Elder.” The Head Elder looked at me with a strange smile as I did my best to hide my surprise. “I’ve been hearing an interesting rumor within the family lately. Something about… the Sleeping Dragon of Shanxi?” I never expected to hear that ridiculous nickname from the Head Elder. “I’ve also heard that you are acquainted with Yama Whip. They say you joined forces with him to defeat the Heavenly Axe.” “Cough. Cough.” “Are you ill?” “N-no. I’m just feeling a little chilly.” “Oh dear. That won’t do for someone who is about to distinguish himself.” My awkward smile slowly froze. “What do you mean?” “Someone capable of helping eliminate an exceptional demon like the Heavenly Axe is a valuable asset in battle. Surely that rumor isn’t false.” “…” “Therefore, as a direct-line member of our family, I believe it is only natural that you lead from the front. What do you think, Lesser Family Head?” The Head Elder smiled faintly. Jin Wikyung, who had been gazing at that smile, asked me, “What do you think?” *Checkmate.* The moment the word came to mind, a familiar notification rang out. Ding. * * * > **System** > > **Quest** > > **Carry Out Missions** > > You have been appointed reconnaissance squad leader of White Tiger Hall. > > From now on, lead the subordinates assigned under you, carry out missions, and build merit! > > **Grade:** Repeating Quest > **Restriction:** Jin Taekyung > **Mission:** Achieve 100 Merit (0 / 100) > **Reward:** Changes according to the degree of success. > **Failure:** Changes according to the degree of failure. I closed the Quest Window. I had already seen it several times, and besides, the White Tiger Hall martial artist who had briefly stepped away had just returned. “These are the supplies issued to squad leaders.” A sword. A black martial uniform with a crudely embroidered white tiger. And a smooth wooden plaque that smelled strongly of fresh wood. That was everything. “The newly assigned members are waiting at the reconnaissance squad’s quarters. The location is…” Fortunately, I knew the place. The pavilion I had passed several times was the quarters assigned to the reconnaissance squad. After leaving White Tiger Hall, I first ducked into a deserted alley. *Open Inventory.* Ten seconds was enough to put on the full uniform. I changed clothes, shoved the sword deep into my Inventory, then pulled out the *Sharp Spear*. Until now, I had thoroughly enjoyed the privileges of being the Third Young Master in a lavish private pavilion. But things were different from here on out. *It’s communal living, right?* We would eat together and sleep together. I couldn’t exactly perform a magic trick where a two-meter iron spear popped out of thin air whenever I needed it. Once I hung the wooden plaque engraved with *Squad Leader* at my waist, I felt like I’d become Ordinary Martial Artist #1 of the Jin Family of Taiyuan. *Not just an ordinary martial artist. I’m a reconnaissance squad leader.* White Tiger Hall reconnaissance squad leader. I had never expected to receive a position like this. Of course, there had been some fierce disagreement over it. The Head Elder wanted to place me in a combat unit under the Elder Council faction, while Jin Wikyung had vehemently opposed him. *In the end, they compromised.* I received the relatively undemanding position of reconnaissance squad leader, but under the command of the White Tiger Hall Leader, who belonged to the Elder Council faction. Before I could get a word in, the position was mine. *I never imagined this was how I’d get dragged into the war.* I could have dug in my heels and told them to do their worst, but I held back. The first reason was the Head Elder’s eyes, which flashed every time Yama Whip was mentioned. The second reason was… The children. *It’s a game. It’s all graphics. Nothing but an illusion.* No matter how many times I repeated that to myself, the corpses and the character carved into their foreheads with a knife kept flickering before my eyes. Part of this decision had been emotional. At this rate, things weren’t looking good. *Don’t get sucked in. I can’t confuse reality with the game.* Things like this had been happening more and more often lately. At first, I had treated the NPCs like people for fun. But these days, I was actually thinking of them as real people and forming relationships with them. It startled me every time. Maybe this was a side effect of playing the game for too long. “Is this it?” Before I knew it, I had arrived at the reconnaissance squad’s quarters. My mouth fell open. Cracked wood and a musty smell. Good lord, there was even a beehive under the eaves. I had never seen one that big before. *Just like a company that treats its employees like family…* Look at those benefits. Or maybe it was a mean-spirited prank by the White Tiger Hall Leader, who disliked me. Perhaps he couldn’t openly give me grief yet, so this was his way of telling me to eat shit. *All right. Let’s give it a shot.* I took a deep breath, opened the door, and stepped inside. Creeeak. The old floor wailed beneath my foot, and the sound felt especially ominous.

## Korean source

```text
＃22화



방에 들어서자 곰팡이 냄새가 코를 찔렀다. 과거 군대 내무반을 연상시키는 그곳에 정찰조원들이 대기 중이었다.

‘열 명.’

나는 기감을 일으킴과 동시에 그들의 면면을 훑었다.

시선이 스쳐 갈 때마다 낯선 얼굴들 위로 레벨창이 불쑥불쑥 솟아오른다.

‘14레벨. 15레벨. 14레벨…….’

대부분이 비슷한 수준이었다. 그렇게 아홉 번째 인물로 넘어간 순간이었다.



[Lv.22 혁무진]



숫자가 훌쩍 뛰었다. 심지어 낯익은 얼굴이다.

‘혁무진?’

며칠 전 처음으로 태원진가에 도착했을 때 내게 시비를 걸었던 그 혁무진이 맞다. 시선이 마주치자 녀석이 입꼬리를 말아 올렸다.

“이렇게 또 뵙는군요. 삼. 공. 자.”

나는 적의가 드러나는 웃음을 빤히 쳐다보다 말했다.

“앞으로 조장님, 이라고 불러라.”

“……그리하지요.”

혁무진의 따가운 시선을 흘리고 열 번째 정찰조원을 바라봤다. 내가 처음 등장했을 때부터 환한 웃음을 짓고 있던 청년이 벌떡 일어났다.

“공자, 아니 조장님! 잘 부탁드립니다.”



[Lv.13 한엽]



전시 상황이다 보니 보직이 변경된 모양이다. 앞서 만난 백호당 서기는 정찰조 자체가 여러 곳에서 차출된 무사들로 구성되었다고 했다.

‘혁무진도 원래는 수문각 소속이니까.’

그래서인지 몰라도 방 안의 분위기는 어수선했다.

조원들은 낯선 이들끼리의 어색함과 전쟁에 대한 불안, 기대가 뒤섞인 표정들로 나를 바라보는 중이었다.

처음으로 입을 뗐다.

“백호당 정찰조장으로 임명된 진태경이다. 잘 부탁한다.”

짝짝짝. 누군가의 외로운 박수 소리는 불과 몇 초 만에 사그라지고 한엽이 무안한 얼굴로 손을 내렸다.

생각 이상으로 딱딱한 분위기다.

‘하지만 이것도 나쁘지 않지.’

지금은 전시 상황이다. 서로 웃으며 친목을 도모하는 것보다는 지금처럼 긴장감을 유지하는 게 낫다.

물론 그것도 과하면 독이 되고, 적당한 선에서 풀어 주는 게 조장인 내가 할 일 중 하나다.

‘그거야 뭐, 익숙하니까.’

처음 게이트에 입장한 초짜 헌터들은 말 그대로 얼어붙는다. 실전은 연습과 다르니까. 헌터 훈련소에서 배운 지식, 훈련은 우주 저 멀리 날아가고 원초적인 죽음의 냄새에 압도되는 것이다.

그래서 길드 내 베테랑들이 초짜의 멘탈 케어를 도왔는데, 나도 그중 하나였다.

‘그래 봤자 F급 전담이었지만.’

수준도 엇비슷하다. 내가 느낀 바로는 무림의 이류는 E급과 F급을 오가는 수준이니까.

그러니까 나는 열 명의 F급 파티를 이끄는 파티장이 된 셈이다. 내가 파티장이라, 해 본 적은 없었지만, 뭘 해야 하는지는 질리도록 봐 왔다.

“본인이 전투 경험이 있다. 거수.”

대뜸 던진 말에 정찰조 전원이 손을 들었다. 다들 어리둥절한 얼굴이다.

“5회 이상 전투를 겪었다. 거수.”

절반의 손이 내려갔다. 그중에는 한엽도 포함되어 있었다.

5회 이상 전투 경험자가 다섯 명이라. 이 정도면 나쁘지 않다. 아니, 기대 이상이다.

하지만 가장 중요한 마지막 질문이 남았다.

“살인 경험이 있다. 거수.”

힘없이 내려가는 네 개의 손. 나는 아직까지도 손을 들고 있는 유일한 정찰조원을 바라봤다.



[Lv.22 혁무진]



“얼마나 죽였지?”

녀석이 코웃음 쳤다.

“다섯. 작년 산적 토벌 때였소. 그중 하나는 부채주였고. 제법 강한 놈이었…….”

더 들을 것도 없이 말했다.

“좋아. 지금부터 네가 부조장이다.”

주절거리려던 혁무진의 입이 딱 다물어졌다.

“부조장?”

“어. 싫으면 지금 말해.”

초보들만 모인 지금, 무엇보다 중요한 건 경험자다.

망설임 없이 적에게 무기를 휘두를 수 있는 놈은 혁무진이 유일하다.

‘흑묘백묘.’

흰 고양이든 검은 고양이든, 싸가지 없는 고양이든 쥐만 잘 잡으면 장땡이지.

복잡한 얼굴로 생각에 잠겨 있던 혁무진이 대답했다.

“……흥. 명령이니까 어쩔 수 없군.”

부조장 하고 싶다는 말을 어렵게도 한다.

“그럼 혁무진이 부조장. 앞으로 부를 때는 일 호다.”

“일 호? 그건 또 뭐요?”

“번호 순서. 앞으로 정찰조는 이름 대신 번호로 통칭한다. 혁무진이 일 호. 그 다음에 저기 앉아 있는 너. 그래. 네가 이 호.”

일 호부터 십 호까지. 한 사람씩 가리키며 지명을 끝냈다.

혁무진이 눈살을 찌푸렸다.

“왜 그렇게 하는 거요?”

“이게 편하니까. 오늘 당장 전투가 벌어질지도 모르는데 하루 종일 이름만 외울래?”

“그건.”

“그럼 시키는 대로 해. 명령이다.”

굳은 얼굴로 나를 노려보는 혁무진을, 나는 피하지 않았다.

오히려 그때처럼 건방지게 나와 주기를 기대하는 마음도 있었다. 당장 며칠 안에 전투가 벌어질 수도 있는데 지금 같은 식이라면 곤란하다.

만약 덤빈다면 힘의 격차를 알려 줘야 한다. 확실하게.

“……명령에 따르겠소.”

“네가 뭐라고?”

“일 호, 일 호요.”

대답하는 혁무진의 목소리가 파르르 떨렸다. 생각보다 감이 좋은 놈이다. 산서잠룡에 관한 소문 때문인지도 모르고.

중요한 사실은 혁무진이 나에게 순응했다는 사실이다.

나는 내색하지 않고 말을 이었다.

“지금부터 하는 말이 낯설고 이상하게 들릴 수 있다. 하지만 참아. 그게 칼 맞아 죽는 것보다 낫잖아. 안 그래?”

혁무진만큼 대놓고 불만을 드러내진 않았지만, 다른 정찰조원들도 불안한 표정으로 나를 바라봤다.

한 사람만 빼고.

“저는 조장님 말씀을 따르겠습니다!”

한엽이 소녀 팬처럼 외쳤다. 차이점이 있다면 손에 아이돌 응원봉 대신 창이 들려 있다는 건데…….

‘아, 그렇지.’

나는 정찰조원들을 향해 씩 웃어 보였다.

“자, 본인이 검을 쓴다. 거수.”

파티 사냥의 핵심. 포지션 나누기다.



* * *



현실의 레이드 방식은 이미 교범화된 지 오래다.

탱커 셋. 딜러 넷. 마법사 둘과 힐러 하나. 10인 파티 기준으로 가장 이상적인 조합이다.

‘마법사, 힐러는 당연히 없고.’

탱커, 딜러만으로 최대한 균형을 맞춰야 하는데, 그런데…….

“……방패 쓸 줄 아는 사람이 없다고?”

충격적인 결과에 목소리가 떨렸다. 세상에, 딜러만 열 명이라니. 심지어 아홉이 검이고, 창은 한엽, 한 명밖에 없다.

‘이 무슨 끔찍한 단일종인가.’

차라리 혼종이 낫다. 그건 이것저것 섞여 있기라도 하니까.

혁무진이 뭐 잘못됐냐는 표정으로 말했다.

“사내라면 응당 검을 쥐어야지 않겠소.”

그 말에 고개를 끄덕이는 다른 놈들을 보니 기도 안 찬다.

‘아주 배가 불렀구먼. 배가 불렀어.’

피 웅덩이에 머리 박아 봐라, 저런 말이 나오나.

칼? 창? 그런 거 없다. 엉겁결에 잡은 돌멩이로 찍고, 흙 뿌리고 올라타서 이빨로 깨물고…….

사선(死線)에서는 손에 잡히는 게 무기고 생명줄이다.

기껏해야 산적들이나 상대해 왔던 이 녀석들은 아직 그걸 모른다.

‘당장 내일부터라도 연습시켜야 하나?’

저들을 위해서가 아니라, 내 생존을 위해서.

요령만 가르쳐도 난전에서는 확실한 효과를 발휘할 것이다.

‘7년 동안 개처럼 굴렀는데 초짜들 때문에 죽을 수는 없지.’

그런 생각을 할 때였다. 댕. 댕. 댕. 커다란 종소리가 세 번 울렸다.

개개인이 정확한 시간을 알 수 없는 이곳에서는 특정 시각마다 종을 치는데, 방금 울린 세 번의 종소리는 미시(未時:오후1~3시)가 되었다는 신호였다.

그리고…….

“준비해. 첫 출동이다.”

정찰조의 첫 임무를 알리는 신호탄이기도 했다.



* * *



“잘하고 있을 겁니다.”

위팽의 뜬금없는 말에 진위경이 고개를 들었다. 그는 방금까지 식어 가는 찻잔을 멍하니 바라보고 있던 중이었다.

“무슨 소린가?”

“삼공자 말입니다.”

진태경이 속한 정찰조가 태원진가를 출발한 지 꼬박 하루가 흘렀다. 태원진가 인근 현읍을 정찰하는 것이 이번 임무였다.

“어제 정오 무렵에 출발했으니 이틀 안에는 도착할 겁니다.”

“아. 태경이.”

진위경은 풀썩 웃었다. 어딘가 지쳐 보이는 웃음이었다.

“난 또 뭐라고. 아닐세.”

“아닙니까?”

“언제까지 어린아이 취급 할 텐가? 이제 그 아이도 당당한 사내야. 알아서 잘하겠지.”

“……제 귀가 의심되는군요.”

“그동안 내가 많이 감싸기는 했지. 그때는 많이 어렸거든.”

“저도 어느 정도는 동감입니다. 며칠 사이에 부쩍 달라졌어요.”

“영웅은 역경을 딛고 성장하는 법이니까.”

“…….”

“아무튼 이제 막내에 대해서는 한시름 놨네. 이제 좀 더 본가에 집중할 수 있겠어.”

“잠시 쉬시지요. 힘들어 보이십니다.”

“위팽. 본가의 식솔들이 죽었네.”

슬픔과 결의가 묻어 나오는 목소리에 위팽은 입을 다물었고, 진위경은 다시 업무를 보기 시작했다.

하지만 침묵은 불과 한 시진 만에 깨졌다.

“저건…….”

점점 가까워지는 하늘 위의 검은 점. 거대한 날개를 펼치며 집무실 창가에 내려앉은 전서응은 하오문의 그것이었다.

황급히 자리에서 일어난 진위경은 전서응의 발목에 고정된 통을 열었다. 서신을 펼친 순간 깨알처럼 적힌 글씨가 눈에 들어왔다.



일문일살一問一殺 조필 외 별동대 이십 인. 정양定壤 출현.



“정양……!”

정양을 넘으면 혼주. 혼주를 넘으면 태원이다. 제아무리 별동대라고 하지만 며칠 만에 수백 리를 주파할 줄이야.

그뿐만이 아니다.

아직까지 본가로 복귀하지 않은 지부의 식솔들이 있다. 설마 놈들이 그들을 추적하고 있다면?

‘한시가 급하다.’

진위경이 결단을 내리기까지는 오래 걸리지 않았다.

“지금 당장 무사 오십을 선별하여 정양으로 가게. 일문일살은 잔학무도한 절정 고수. 본가의 식솔들을…….”

아이들이 생각났다. 작은 팔다리, 고통스럽게 일그러진 얼굴과 공허한 그 눈동자. 진위경은 이를 악물었다.

“식솔들을 안전하게 데려와 주게.”

“주군.”

위팽의 표정이 딱딱하게 굳어 있었다. 진위경은 뭔가에 사로잡힌 듯, 멍하니 그의 얼굴을 바라보다가 입을 열었다.

“태경이. 태경이가 어디로 갔다고 했지?”

쥐어 짜낸 목소리가 흘러나왔다.

“……정양입니다.”
```

## Current accepted English baseline

```markdown
# Chapter 22

The smell of mold stabbed at my nose as soon as I entered the room. The place reminded me of a military barracks, and the members of the reconnaissance squad were waiting inside.

*Ten people.*

I sharpened my senses and looked over each of them.

Every time my gaze passed over an unfamiliar face, a Level display popped up.

*Level 14. Level 15. Level 14…*

Most of them were around the same level. Then, as I moved on to the ninth person—

> **Lv. 22 Hyuk Mujin**

The number jumped sharply. The face was familiar, too.

*Hyuk Mujin?*

It was the same Hyuk Mujin who had picked a fight with me when I first arrived at the Jin Family of Taiyuan a few days ago. When our eyes met, he smirked.

“What a pleasure to see you again, Third. Young. Master.”

I stared at his openly hostile smile and said,

“From now on, call me Squad Leader.”

“……As you wish.”

I ignored Hyuk Mujin’s piercing stare and looked at the tenth member of the reconnaissance squad. The young man who had been smiling brightly since I first appeared shot to his feet.

“Young Master—no, Squad Leader! I look forward to working with you.”

> **Lv. 13 Han Yeop**

It seemed some assignments had been changed because of the war. The White Tiger Hall clerk I had met earlier said that the reconnaissance squad itself was made up of martial artists drawn from several different places.

*Hyuk Mujin originally belonged to the Gate Watch Office, too.*

Maybe that was why the atmosphere in the room was so disorganized.

The squad members looked at me with expressions that mixed the awkwardness of strangers meeting for the first time with anxiety and anticipation about the war.

I spoke first.

“I’m Jin Taekyung, appointed leader of White Tiger Hall’s reconnaissance squad. I look forward to working with you.”

Clap, clap, clap.

Someone’s lonely applause died out within a few seconds, and Han Yeop lowered his hand with an embarrassed expression.

The atmosphere was stiffer than I had expected.

*But that isn’t necessarily a bad thing.*

We were in wartime. Maintaining the current tension was better than laughing together and trying to socialize.

Of course, too much tension could become poisonous. Easing it at the right moment was one of my duties as squad leader.

*That much, I’m used to.*

Newbie Hunters froze the moment they entered a Gate for the first time. Real combat was different from practice. Everything they had learned and trained for at the Hunter training center flew off into outer space, and they were overwhelmed by the primal scent of death.

That was why veterans in the Guild handled mental care for the rookies. I had been one of them.

*Though I was assigned exclusively to F-ranks.*

The levels were similar, too. From what I could tell, a second-rate martial artist from Murim was somewhere between an E-rank and an F-rank.

In other words, I had become the leader of a ten-person F-rank party. I had never actually been a party leader, but I had watched what they were supposed to do until I was sick of it.

“Raise your hand if you have combat experience.”

At my abrupt question, every member of the reconnaissance squad raised a hand. They all looked bewildered.

“Raise your hand if you’ve been in combat at least five times.”

Half the hands went down. Han Yeop was among them.

Five people with experience in at least five battles. That wasn’t bad. No, it was better than expected.

But the most important question remained.

“Raise your hand if you’ve killed someone.”

Four hands dropped weakly. I looked at the only member of the reconnaissance squad who still had his hand raised.

> **Lv. 22 Hyuk Mujin**

“How many?”

He snorted.

“Five. It was during last year’s bandit suppression campaign. One of them was a bandit chieftain. He was quite a strong bastard—”

I cut him off before he could continue.

“Good. You’re the deputy squad leader from now on.”

Hyuk Mujin’s mouth, which had been preparing to ramble on, snapped shut.

“Deputy squad leader?”

“Yeah. Speak up now if you don’t like it.”

With nothing but rookies gathered here, experience mattered more than anything.

Hyuk Mujin was the only one who could swing a weapon at the enemy without hesitation.

*Black cat, white cat.*

White cat, black cat, or even a rude cat—it didn’t matter as long as it caught mice.

Hyuk Mujin thought for a while with a complicated expression before answering.

“……Hmph. Since it’s an order, I suppose it can’t be helped.”

He sure had a difficult way of saying he wanted to be deputy squad leader.

“Then Hyuk Mujin is deputy squad leader. From now on, we’ll call you Number One.”

“Number One? What’s that supposed to mean?”

“Number order. From now on, the reconnaissance squad will be referred to by number instead of name. Hyuk Mujin is Number One. Next, you sitting over there. Yes, you’re Number Two.”

I finished assigning numbers one by one, from Number One to Number Ten.

Hyuk Mujin frowned.

“Why are you doing this?”

“It’s more convenient. We might be fighting today. Do you want to spend all day memorizing names?”

“That’s—”

“Then do as you’re told. It’s an order.”

I didn’t look away from Hyuk Mujin as he glared at me with a hard expression.

Part of me even hoped he would act insolent like he had that day. A battle could break out within the next few days. If things continued as they were, that would be a problem.

If he challenged me, I would have to show him the difference in our strength.

Clearly.

“……I will follow your orders.”

“What did you say?”

“Number One. I said Number One.”

Hyuk Mujin’s voice trembled as he answered. He was more perceptive than I had expected. Maybe it was because of the rumors about the Sleeping Dragon of Shanxi.

The important thing was that Hyuk Mujin had submitted to me.

Without showing anything on my face, I continued.

“What I’m about to say may sound strange and unfamiliar. But bear with it. It’s better than getting stabbed to death, isn’t it? Don’t you agree?”

The other reconnaissance squad members didn’t show their displeasure as openly as Hyuk Mujin, but they also looked at me anxiously.

Everyone except one.

“I’ll follow whatever the Squad Leader says!”

Han Yeop shouted like a teenage girl idol fan. The only difference was that he was holding a spear instead of an idol light stick.

*Oh, right.*

I grinned at the reconnaissance squad.

“Now, raise your hand if you use a sword.”

The core of party hunting was dividing up positions.

* * *

Raid strategies in the real world had been standardized into manuals long ago.

Three tanks. Four damage dealers. Two mages and one healer. For a ten-person party, that was the ideal combination.

*Of course, there are no mages or healers.*

I had to balance things as much as possible with tanks and damage dealers alone, but—

“……You’re telling me no one knows how to use a shield?”

My voice trembled at the shocking result. Good lord, there were ten damage dealers. Nine used swords, and the only person with a spear was Han Yeop.

*What kind of horrifying single-species party is this?*

A hybrid would be better. At least that would mean something had been mixed in.

Hyuk Mujin spoke with an expression that suggested he couldn’t understand what was wrong.

“A man ought to wield a sword.”

I was speechless when I saw the others nodding along with him.

*You’re too well-fed. Way too well-fed.*

Try slamming your head into a pool of blood and see if you still talk like that.

Sword? Spear? There was no such distinction. You bashed people with whatever rock you happened to grab, threw dirt, climbed on top of them, and bit them with your teeth.

On the line between life and death, anything in your hand was a weapon and a lifeline.

These people, who had only ever fought bandits at best, still didn’t understand that.

*Do I need to start training them tomorrow?*

Not for their sake. For my survival.

Even teaching them a few tricks would make a real difference in a melee.

*I worked like a dog for seven years. I can’t die because of a bunch of rookies.*

That was when it happened.

Ding. Ding. Ding.

A large bell rang three times.

Since no one could tell the exact time, bells were rung at set intervals. The three tolls that had just sounded marked Mi-si, roughly one to three in the afternoon.[^1]

And—

“Get ready. This is our first deployment.”

The bells also served as the signal announcing the reconnaissance squad’s first mission.

* * *

“He should be doing fine.”

Jin Wikyung looked up at Wipeng’s abrupt comment. Until a moment ago, he had been staring blankly at a teacup as it slowly cooled.

“What are you talking about?”

“The Third Young Master.”

A full day had passed since the reconnaissance squad led by Jin Taekyung departed from the Jin Family of Taiyuan. Their mission was to scout the county towns near the Jin Family.

“They left around noon yesterday, so they should arrive within two days.”

“Ah. Taekyung.”

Jin Wikyung let out a weak laugh. He looked exhausted.

“I thought you meant something else. That’s not it.”

“It’s not?”

“How long are you going to treat him like a child? He’s a grown man now. I’m sure he’ll manage on his own.”

“……I’m beginning to doubt my ears.”

“I did coddle him quite a bit. He was very young back then.”

“I agree, to some extent. He’s changed considerably over the past few days.”

“Heroes grow by overcoming adversity.”

“……”

“Anyway, I can stop worrying about the youngest now. I’ll be able to focus more on the main family.”

“You should rest for a while. You look tired.”

“Wipeng. Members of our family have died.”

At the sorrow and determination in his voice, Wipeng fell silent, and Jin Wikyung returned to his work.

But the silence broke after a mere two hours.

“What is that…?”

A black dot in the sky was gradually drawing closer. Spreading its enormous wings, the messenger hawk landed by the window of the office. It belonged to the Lower District Sect.

Jin Wikyung hurriedly stood and opened the tube fastened to the hawk’s leg. The moment he unfolded the letter, tiny writing caught his eye.

> Jopil, One Question, One Kill, and twenty members of a special detachment have appeared in Jeongyang.

“Jeongyang…!”

Beyond Jeongyang was Honju. Beyond Honju was Taiyuan. Even if they were a special detachment, he had never expected them to cover hundreds of li in only a few days.

That wasn’t all.

There were still family members from the branches who had not returned to the main family. What if the enemy was tracking them?

*Every moment counts.*

It didn’t take Jin Wikyung long to make a decision.

“Select fifty martial artists immediately and send them to Jeongyang. One Question, One Kill Jopil is a brutal Peak master. Bring our family members—”

He thought of the children.

Their small limbs. Their faces twisted in pain. Their vacant eyes.

Jin Wikyung clenched his teeth.

“Bring our family members home safely.”

“My lord.”

Wipeng’s expression had hardened. Jin Wikyung stared blankly at him, as though a thought had seized him, before speaking.

“Taekyung. Where did you say Taekyung went?”

His voice came out strained.

“……Jeongyang.”

[^1]: Mi-si is one of the traditional two-hour divisions of the day, corresponding roughly to 1–3 p.m.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 22`.

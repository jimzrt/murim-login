# Master Edit Task — Chapter 23

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
| 혁무진    | **Hyuk Mujin**     |
| 이소군    | **Lee Seogeun**    |
| 조필     | **Jopil**          |
| 태원진가   | **Jin Family of Taiyuan**        |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 낭인     | **wandering martial artist**                     |                                                       |
| 정파     | **orthodox faction**                             |                                                       |
| 지부장    | **Branch Leader**                            |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 탱커      | **tank**              |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 청해     | **Qinghai**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 흑산도 | **Black Mountain Blade** |
| 한엽 | **Han Yeop** |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
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

#### Chapter 21 tail (verified mastered)

…
first time the Head Elder had spoken to me. “Greetings, Head Elder.” The Head Elder looked at me with a strange smile as I did my best to hide my surprise. “I’ve been hearing an interesting rumor within the family lately. Something about… the Sleeping Dragon of Shanxi?” I never expected to hear that ridiculous nickname from the Head Elder. “I’ve also heard that you are acquainted with Yama Whip. They say you joined forces with him to defeat the Heavenly Axe.” “Cough. Cough.” “Are you ill?” “N-no. I’m just feeling a little chilly.” “Oh dear. That won’t do for someone who is about to distinguish himself.” My awkward smile slowly froze. “What do you mean?” “Someone capable of helping eliminate an exceptional demon like the Heavenly Axe is a valuable asset in battle. Surely that rumor isn’t false.” “…” “Therefore, as a direct-line member of our family, I believe it is only natural that you lead from the front. What do you think, Lesser Family Head?” The Head Elder smiled faintly. Jin Wikyung, who had been gazing at that smile, asked me, “What do you think?” *Checkmate.* The moment the word came to mind, a familiar notification rang out. Ding. * * * > **System** > > **Quest** > > **Carry Out Missions** > > You have been appointed reconnaissance squad leader of White Tiger Hall. > > From now on, lead the subordinates assigned under you, carry out missions, and build merit! > > **Grade:** Repeating Quest > **Restriction:** Jin Taekyung > **Mission:** Achieve 100 Merit (0 / 100) > **Reward:** Changes according to the degree of success. > **Failure:** Changes according to the degree of failure. I closed the Quest Window. I had already seen it several times, and besides, the White Tiger Hall martial artist who had briefly stepped away had just returned. “These are the supplies issued to squad leaders.” A sword. A black martial uniform with a crudely embroidered white tiger. And a smooth wooden plaque that smelled strongly of fresh wood. That was everything. “The newly assigned members are waiting at the reconnaissance squad’s quarters. The location is…” Fortunately, I knew the place. The pavilion I had passed several times was the quarters assigned to the reconnaissance squad. After leaving White Tiger Hall, I first ducked into a deserted alley. *Open Inventory.* Ten seconds was enough to put on the full uniform. I changed clothes, shoved the sword deep into my Inventory, then pulled out the *Sharp Spear*. Until now, I had thoroughly enjoyed the privileges of being the Third Young Master in a lavish private pavilion. But things were different from here on out. *It’s communal living, right?* We would eat together and sleep together. I couldn’t exactly perform a magic trick where a two-meter iron spear popped out of thin air whenever I needed it. Once I hung the wooden plaque engraved with *Squad Leader* at my waist, I felt like I’d become Ordinary Martial Artist #1 of the Jin Family of Taiyuan. *Not just an ordinary martial artist. I’m a reconnaissance squad leader.* White Tiger Hall reconnaissance squad leader. I had never expected to receive a position like this. Of course, there had been some fierce disagreement over it. The Head Elder wanted to place me in a combat unit under the Elder Council faction, while Jin Wikyung had vehemently opposed him. *In the end, they compromised.* I received the relatively undemanding position of reconnaissance squad leader, but under the command of the White Tiger Hall Leader, who belonged to the Elder Council faction. Before I could get a word in, the position was mine. *I never imagined this was how I’d get dragged into the war.* I could have dug in my heels and told them to do their worst, but I held back. The first reason was the Head Elder’s eyes, which flashed every time Yama Whip was mentioned. The second reason was… The children. *It’s a game. It’s all graphics. Nothing but an illusion.* No matter how many times I repeated that to myself, the corpses and the character carved into their foreheads with a knife kept flickering before my eyes. Part of this decision had been emotional. At this rate, things weren’t looking good. *Don’t get sucked in. I can’t confuse reality with the game.* Things like this had been happening more and more often lately. At first, I had treated the NPCs like people for fun. But these days, I was actually thinking of them as real people and forming relationships with them. It startled me every time. Maybe this was a side effect of playing the game for too long. “Is this it?” Before I knew it, I had arrived at the reconnaissance squad’s quarters. My mouth fell open. Cracked wood and a musty smell. Good lord, there was even a beehive under the eaves. I had never seen one that big before. *Just like a company that treats its employees like family…* Look at those benefits. Or maybe it was a mean-spirited prank by the White Tiger Hall Leader, who disliked me. Perhaps he couldn’t openly give me grief yet, so this was his way of telling me to eat shit. *All right. Let’s give it a shot.* I took a deep breath, opened the door, and stepped inside. Creeeak. The old floor wailed beneath my foot, and the sound felt especially ominous.

#### Chapter 22 tail (verified mastered)

…
other reconnaissance squad members didn’t show their displeasure as openly as Hyuk Mujin, but they also looked at me anxiously. Everyone except one. “I’ll follow whatever the Squad Leader says!” Han Yeop shouted like a fangirl. The only difference was that he was holding a spear instead of an idol light stick. *Oh, right.* I grinned at the reconnaissance squad. “Now, raise your hand if you use a sword.” The core of party hunting was dividing up positions. * * * Raid strategies in the real world had been standardized into manuals long ago. Three tanks. Four damage dealers. Two mages and one healer. For a ten-person party, that was the ideal combination. *Of course, there are no mages or healers.* I had to balance the party as best I could using only tanks and damage dealers, but— “…You’re telling me no one knows how to use a shield?” My voice trembled at the shocking result. Good lord, all ten of them were damage dealers. Nine used swords, and Han Yeop was the only one with a spear. *What kind of horrifying single-species party is this?* A hybrid would be better. At least that would mean something had been mixed in. Hyuk Mujin spoke with an expression that suggested he couldn’t understand what was wrong. “A man ought to wield a sword.” Seeing the others nod along left me speechless. *You’ve had it way too easy. Way too easy.* Try slamming your head into a pool of blood and see if you still talk like that. Sword? Spear? There was no such distinction. You bashed people with whatever rock you happened to grab, threw dirt, climbed on top of them, and bit them with your teeth. On the line between life and death, anything in your hand was a weapon and a lifeline. These people had only ever fought bandits at best. They still didn’t understand that. *Do I need to start training them tomorrow?* Not for their sake. For my survival. Even teaching them a few tricks would make a real difference in a melee. *I worked like a dog for seven years. I can’t die because of a bunch of rookies.* That was when it happened. Ding. Ding. Ding. A great bell tolled three times. Here, where no one could tell the exact time, bells were rung at set intervals. The three tolls that had just sounded marked Mi-si, roughly one to three in the afternoon.[^1] And— “Get ready. This is our first deployment.” They also signaled the reconnaissance squad’s first mission. * * * “He should be doing fine.” Jin Wikyung looked up at Wipeng’s abrupt comment. Until a moment ago, he had been staring blankly at a teacup as it slowly cooled. “What are you talking about?” “The Third Young Master.” A full day had passed since the reconnaissance squad led by Jin Taekyung departed from the Jin Family of Taiyuan. Their mission was to scout the county towns near the Jin Family. “They left around noon yesterday, so they should arrive within two days.” “Ah. Taekyung.” Jin Wikyung let out a weak laugh. He looked exhausted. “I thought you meant something else. That’s not it.” “It’s not?” “How long are you going to treat him like a child? He’s a grown man now. I’m sure he’ll manage on his own.” “…I’m beginning to doubt my ears.” “I did coddle him quite a bit. He was very young back then.” “I agree, to some extent. He’s changed considerably over the past few days.” “Heroes grow by overcoming adversity.” “…” “Anyway, I can stop worrying about the youngest now. I’ll be able to focus more on the main family.” “You should rest for a while. You look tired.” “Wipeng. Members of our family have died.” Wipeng fell silent at the sorrow and determination in his voice, and Jin Wikyung returned to his work. But the silence broke after a mere two hours. “What is that…?” A black dot in the sky was gradually drawing closer. The messenger hawk spread its enormous wings and landed by the office window. It belonged to the Lower District Sect. Jin Wikyung hurriedly stood and opened the tube fastened to the hawk’s leg. The moment he unfolded the letter, tiny writing caught his eye. > One Question, One Kill Jopil and twenty members of a special detachment have appeared in Jeongyang. “Jeongyang…!” Beyond Jeongyang lay Honju. Beyond Honju lay Taiyuan. Even for a special detachment, he had never expected them to cover hundreds of li in only a few days. That wasn’t all. There were still family members from the branches who had not returned to the main family. What if the enemy was tracking them? *Every moment counts.* It didn’t take Jin Wikyung long to decide. “Select fifty martial artists immediately and send them to Jeongyang. One Question, One Kill Jopil is a brutal Peak master. Bring our family members—” He thought of the children. Their small limbs. Their faces twisted in pain. Their vacant eyes. Jin Wikyung clenched his teeth. “Bring our family members home safely.” “My lord.” Wipeng’s expression had hardened. Jin Wikyung stared blankly at him as though something had taken hold of him, then opened his mouth. “Taekyung. Where did you say Taekyung went?” His voice came out strained. “…Jeongyang.” [^1]: Mi-si is one of the traditional two-hour divisions of the day, corresponding roughly to 1–3 p.m.

## Korean source

```text
＃23화



태원진가.

이름에서 알 수 있듯이 그 본거지는 태원이다. 그러나 현실에서의 대기업이 그렇듯, 태원진가의 영향력은 태원 한 곳에 국한되지 않았다.

가문이 세워진 지 200년. 산서성 곳곳에 산재한 현읍에 지부를 설치해 세력권을 넓힌 지 오래였다.



닷새 안에 정양 인근을 정찰하고 복귀할 것.



정찰조에게 내려진 첫 임무다. 명령 내용을 들은 조원들의 첫 반응은 두 가지로 나뉘었다.

“별거 아니군요.”

혁무진처럼 실망하는 자들이 있는가 하면, 한엽처럼 안도의 한숨을 내쉬는 자도 있었다.

물론 둘 다 내 마음에 드는 반응은 아니었다.

혁무진 쪽은 쓸데없는 공명심에 사로잡혀 있고, 한엽 쪽은 싸우는 것을 겁내고 있으니까.

‘그래, 차라리 안전한 임무가 낫지.’

이런 놈들 데리고 적들이랑 맞닥뜨려 봐라. 상상만 해도 끔찍하다. 차라리 믿을 만한 놈들이랑 일선에서 싸우는 게 덜 위험할 것이다.

‘보직 이동이라도 신청해야 되나.’

내심 한숨을 쉬며 주먹을 치켜올렸다. 앞서 숙지시킨 수신호 중 하나다. 뜻은 정지.

푸르륵.

적당한 속도로 달리고 있던 열한 마리의 말이 투레질 소리와 함께 멈췄다. 내 오른편에서 달리고 있던 혁무진이 퉁명스럽게 말했다.

“왜 멈추는 거요?”

“휴식.”

“또?”

“한 시진 이동. 일각 휴식. 내가 미리 말하지 않았나?”

“더 달릴 수 있소!”

“그럼 너 혼자 달리든가.”

나는 슬쩍 뒤를 턱짓했다. 다른 조원들이 거친 숨을 몰아쉬고 있었다. 말을 타고 이동하는 것은 속도가 빠른 대신, 상당한 스태미나를 소모한다.

레벨이 월등히 높은 혁무진은 그럭저럭 버틴다지만, 다른 조원들은 피로가 누적되고 있었다.

“쉬라면 쉬어. 명령이다.”

혁무진의 구겨진 얼굴을 무시하고 조원들을 향해 말했다.

“일각 동안 휴식.”

일각. 15분의 휴식 시간이 주어졌지만 정찰조원들의 표정은 썩 밝지 않았다. 내가 곧장 커다란 가죽 배낭을 꺼냈기 때문이다.

배낭에 손을 집어넣고 생각했다.

‘인벤토리 오픈.’

철그럭 소리와 함께 방패 세 개가 배낭 안으로 소환됐다.

표면에 철을 입힌 나무 방패는 태원진가를 떠나오기 전 무기고에서 얻어 온 것이었는데, 가볍고 단단해서 쓸 만했다.

“칠 호. 팔 호. 구 호.”

지명된 정찰조원 셋이 죽을상을 쓰며 방패를 받아 갔다.

그 셋이 내게 강제로 선택된, 탱커(Tanker)다.

‘딜러 일곱. 탱커 셋. 그리고 나.’

게이트에 들어갔다가는 몰살을 당할 조합이었지만 우선은 이 정도로 만족해야 한다.

“각자 위치로.”

다음은 포메이션이다.

“기본 대형.”

방패를 든 셋이 가장 앞에 서고, 일 호 혁무진부터 육 호까지 여섯 명의 검사가 제2열. 최후방에는 나와 한엽이 있다.

전방 위주의 경계다.

“펼쳐. 헤쳐 모여. 산개.”

불만이 가득한 얼굴들이었지만 이제는 제법 능숙하게 해낸다. 이정도면 이제 막 헌터 훈련소를 졸업한 F급 헌터보다 훨씬 낫다.

‘사람보다 여기 NPC가 낫네.’

공력의 유무에서 나오는 차이일 것이다.

마나 자체를 다루지 못하는 F급 헌터와 달리 무림의 NPC들은 미미하나마 공력을 사용할 줄 아니까.

단지 레벨이 낮고, 경험이 없을 뿐이지.

나는 포메이션의 마지막 단계로 접어들었다.

“전력 후퇴.”

순간 정찰조원들이 멈칫했다.

“예?”

“전력 후퇴는 뭡니까?”

“말 그대로지. 전력을 다해서 후퇴하라고.”

“그럼 어떤 대형을……?”

“그때쯤이면 대형이 무의미하지. 그냥 전력을 다해서 튀어라. 뒤도 돌아보지 말고 최대한 흩어져서.”

“큭큭. 그걸 말이라고 하는 거요?”

비웃음의 주인은, 당연하게도 혁무진이었다.

“이제 도저히 못 참겠군. 삼공자, 전쟁이 소꿉장난이오? 헛소리를 그럴듯하게 하려면 최소한 병법서 한 권 정도는 읽고 왔어야지.”

“병법서?”

“그래. 병법서! 질서정연하게 후퇴하는 것은 병법의 기본중의 기본인데 무슨 망발을 지껄이는 거요?”

혁무진이 대놓고 반발하자 정찰조원들 사이에서도 소극적인 목소리들이 새어 나왔다.

“맞는 말이긴 해.”

“우리가 관아의 군병도 아닌데 대형을 연습시키고, 억지로 방패까지 들게 하고…….”

“전력 후퇴? 그런 건 들어 본 적도 없어.”

봐라, 다들 나랑 같은 생각이다. 혁무진의 득의양양한 얼굴이 말하는 듯했다.

그때 한엽이 더듬거리는 목소리로 끼어들었다.

“저, 저는 그렇게 생각 안 하는데요.”

“뭐?”

“삼공자, 아니 조장님께서 다 생각이 있으셔서 그런 게 아닐까……요?”

“생각?”

혁무진이 눈을 부라렸다.

“생각은 무슨 생각! 어릴 때부터 수련은 뒷전이고 계집 끼고 술만 퍼마시던 게 삼공자다. 그런 주제에 사고란 사고는 다 치고 다녔지. 그뿐인가, 이 전쟁의 원인을 제공한 것도…….”

“그만하지?”

말을 가로막자 혁무진이 움찔한다. 스스로도 말실수를 했다는 걸 깨달은 모양이었다.

하지만 종종 그런 사람들이 있다. 물러서야 할 때, 오히려 한발 나아가는 그런 사람들이.

“원인을 제공한 것도 삼공자 아닌가!”

혁무진은 자신의 말을 멈추기에는 자존심이 너무나 강한 놈이었다.

결국 뱉어 낸 그 말에, 싸늘한 침묵이 내려앉았다.

꿀꺽. 누군가의 목울대가 크게 일렁였다. 아홉 쌍의 눈빛이 나와 혁무진을 바라보고 있었다.

“하, 할 말이라도 있소?”

할 말? 당연히 있지.

“전원 일 다경 더 휴식.”

동시에 곧게 편 손바닥으로 혁무진의 뺨을 후려쳤다.

쫙!

“한 대.”

혁무진의 턱이 돌아간다. 공력이 전혀 실리지 않은 단순한 따귀다. 갑작스러운 상황에 멍해진 그 얼굴로 두 번째 손바닥을 날렸다.

“이, 이게 무슨!”

그래도 영 맹탕은 아닌지, 팔을 들어 막는다. 녀석이 간과한 부분이 있다면 그건 바로 힘의 차이다.

쫙!

“두 대.”

상체 그대로 땅에 처박힌 혁무진이 벌떡 일어났다. 한쪽 뺨에는 내 손바닥 자국이 문신처럼 박혀 있었다.

당황이 분노로 바뀌기까지는 그리 오랜 시간이 걸리지 않았다.

“이 개새끼가!”

제대로 열받았군. 눈이 뒤집혀서 달려드는 녀석의 다리를 걸어 넘어트렸다. 동시에 왼손에 힘을 실어 후려쳤다.

쫙.

“세 대.”

“커헉.”

다리에 힘이 풀리는지 비틀거린다. 이 정도 힘으로 연달아 세 번을 맞았으니 골이 흔들릴 법도 하다.

“공력은 뒀다가 국 끓여 먹을래?”

이 말은 효과가 있었다. 휘청거리던 하체에 힘이 들어가고 몸에서는 힘이 흘러넘친다. 독기가 줄줄 새는 눈빛이 나를 노려봤다.

“후회하게 될 거야.”

“아닐걸.”

얼굴을 향해 날아오는 주먹을 붙잡았다. 속도, 힘, 타이밍.

전부 눈에 보인다. 이소군에 비하면 한참이나 떨어진다.

“네 대.”

혁무진의 얼굴이 뒤로 젖혀진다. 찐득한 핏물이 슬로우 모션처럼 허공에 흩뿌려졌다. 풀린 동공, 축 늘어진 다리.

하지만 용케도 쓰러지지 않았다.

그건 내가 녀석의 주먹을 놔줘야만 가능한 일이니까.

“다섯 대.”

쫙!

거기까지가 한계였다. 혁무진은 더 이상 버티지 못하고 혼절했다. 기이한 자세로 널브러진 혁무진의 몸뚱어리 위로 무언가가 투둑 떨어진다.

‘눈?’

고개를 들어 하늘을 바라봤다. 겨울 하늘이 희고 작은 쓰레기들을 쏟아 내는 중이었다.

“휴식 끝. 출발한다.”

한마디를 툭 던지고 돌아서는 내 등 뒤로, 정찰조원들이 참았던 숨을 토해 냈다.



* * *



두 시간 만에 깨어난 혁무진이 가장 먼저 한 일은 내게 달려드는 것이었다.

“이런 씨발!”

쫙. 털썩.

“치워.”

“예, 옛!”

찰진 따귀 소리와 함께 또 다시 기절한 녀석은, 다른 정찰조원들의 손에 의해 오두막 한 구석에 처박혔다.

‘오두막이라. 운 좋네.’

인근 지리에 빠삭한 조원의 말에 따르면 적어도 오늘 해가 떨어지기 전까지는 정양에 도착했어야 했다.

하지만 갑자기 쏟아지는 폭설에는 어쩔 도리가 없었고, 겨우 찾아낸 곳이 바로 이 오두막이었다.

아는 사람만 아는 사냥꾼 쉼터라던가?

‘턱 없이 작긴 한데, 이 정도면 땡큐지.’

임무가 늦어질 수도 있겠지만, 눈밭에서 밤새 걷다가 기진맥진한 상태에서 적과 마주치는 것보다는 백배 낫다.

그런 생각을 할 때였다.

“저, 조장님.”

한엽이다. 등 뒤로 조원들이 힐끔거리며 내 눈치를 살폈다.

“이제 어떡할까요?”

“응? 자야지.”

“저, 그게 아니라…….”

우물쭈물하는 정찰조원들을 보자 문득 떠오르는 게 있었다.

너희 설마…….

“수련하고 싶냐?”

끄덕끄덕. 맹렬하게 상하를 오가는 고갯짓과 열의에 가득 찬 저 눈빛을 봐라.

‘백문이 불여일퍽이라더니.’

백번 말하는 것보다 한 번 패는 게 낫구나.



* * *



정오 무렵이었다. 검날이 햇빛을 받아 번쩍였고, 그것이 무사가 볼 수 있었던 유일한 것이었다.

“커헉.”

털썩. 무릎이 꺾이고 얼어붙은 땅바닥에 얼굴이 처박힌다.

어깨부터 가슴까지, 쩍 벌어진 상처 사이로 피가 쏟아졌다. 회생 불능의 상처. 무사는 죽음을 직감했다.

“다른 이들은…… 제발 살려.”

힘을 다한 목소리가 뚝 끊겼다. 부릅뜬 무사의 눈동자를 보며 한 중년인이 혀를 찼다.

“어이구, 이 미련한 친구야.”

그렇게 다짜고짜 덤비면 어떡하나. 이어지는 말은 망자에게 닿지 못했다. 주위를 둘러싸고 있던 오십여 명의 낭인들이 낄낄거렸다.

“하필 대형한테 걸리다니, 운도 더럽게 없는 놈일세그려.”

“누가 정파 새끼 아니랄까 봐 마지막까지 협객 놀음은. 어쩔까요, 대형?”

번들거리는 시선들이 남아 있는 생존자들을 향했다. 여자와 아이들로 이루어진 예닐곱 명의 무리였다.

“대협. 아이들은 살려 주십시오.”

가장 연장자로 보이는 여인의 말에 중년인, 일문일살(一問一殺) 조필은 부드럽게 웃었다.

“미안하지만 어쩌지. 나는 대협이 아니라오.”

“하지만 사람이지요. 어찌 사리분별도 하지 못하는 아이들까지 죽이려 하십니까?”

“허, 아녀자의 몸으로 기개가 제법이오. 가만, 삭주 지부장의 일가가 살아남았다고 하던데. 혹시?”

“제 부군 되십니다.”

“아, 역시 그렇구려. 그런 못난 놈에게 이런 현숙한 부인이 있을 줄이야.”

조필은 빙긋 웃었고, 여인은 얼굴을 굳혔다.

“살려 줄 생각이 없군.”

“안심하시오. 나는 간살하는 취미는 없거든.”

“아이들은…….”

“이 험난한 세상. 어린것들이 어미 없이 어찌 살아남겠소?”

“금수만도 못한 놈.”

“유언, 잘 들었소.”

그 말이 신호탄이었다.

검광이 번뜩이고 비명이 울려 퍼졌다.

잠시 후 피를 흠뻑 뒤집어쓴 낭인들이 시체들을 산속 수풀로 던져 넣었다.

“산짐승 놈들만 포식하겠군요.”

뱁새눈이 중얼거렸다. 그는 조필의 오른팔 격인 인물로, 흑산도(黑山刀)라는 별호로 알려진 일급 낭인이었다.

“우리도 포식해야지. 이번 일만 잘 마무리 짓는다면 천금이 별건가?”

조필은 기분 좋게 웃었다. 이번 일로 받게 될 사례도 어마어마했지만, 그는 지금 이 상황 자체를 즐기고 있었다.

“태원진가 놈들을 사냥하는 날이 오다니. 상상도 못 했지.”

더러워진 가죽신이 고꾸라진 무사의 시신을 밟았다.

무사는 태원진가에 속한 십여 개 지부 중 하나인 삭주(朔州) 지부 소속이었다.

“방금 처리한 게 마지막인가?”

“아닙니다, 대형.”

“쥐새끼처럼 잘도 빠져나가는군. 머릿수는?”

“도합 셋. 무사 하나에 아이 둘입니다. 불과 몇 시진 전에 정양을 통과, 혼주로 향하고 있다고 합니다.”

“골치 아프군. 반나절은 걸릴 텐데.”

“대형께서 나서실 필요도 없이 제가 다녀오겠습니다.”

“그래 주겠나?”

조필의 입가에 흐뭇한 미소가 떠올랐다.

“좋아, 절반을 데려가게. 기한은 반나절, 어떤가?”

대답은 이미 정해져 있었다. 흑산도는 깊이 고개를 숙였다.
```

## Current accepted English baseline

```markdown
# Chapter 23

Jin Family of Taiyuan.

As its name suggests, its headquarters were in Taiyuan. But like a conglomerate in the real world, the Jin Family of Taiyuan’s influence was not limited to a single city.

The family had been established for two hundred years. It had long since expanded its sphere of influence by establishing branches in county towns scattered throughout Shanxi.

*Scout the area near Jeongyang and return within five days.*

That was the first mission assigned to the reconnaissance squad. When they heard the order, the squad members’ reactions fell into two categories.

“Doesn’t sound like much.”

Some, like Hyuk Mujin, were disappointed. Others, like Han Yeop, let out sighs of relief.

Of course, neither reaction pleased me.

Hyuk Mujin was caught up in a pointless hunger for glory, while Han Yeop was afraid of fighting.

*Still, I’d rather have a safe mission.*

Try running into the enemy with a bunch of guys like these. It was horrifying just to imagine. I’d be safer fighting on the front lines with people I could trust.

*Should I apply for a transfer?*

Suppressing a sigh, I raised my fist. It was one of the hand signals I had taught them earlier. It meant stop.

Snort.

The eleven horses moving at a moderate pace stopped with a chorus of snorts. Hyuk Mujin, riding to my right, spoke irritably.

“Why are we stopping?”

“Rest.”

“Again?”

“Two hours of travel, fifteen minutes of rest. Didn’t I tell you that beforehand?”

“I can keep going!”

“Then go by yourself.”

I jerked my chin toward the rear. The other squad members were breathing heavily. Riding a horse was faster than traveling on foot, but it consumed a considerable amount of stamina.

Hyuk Mujin’s much higher Level let him endure fairly well, but fatigue was accumulating in the others.

“Rest if I tell you to. That’s an order.”

Ignoring Hyuk Mujin’s crumpled face, I addressed the squad.

“Fifteen minutes of rest.”

They had fifteen minutes to rest, but the reconnaissance squad members didn’t look particularly happy. That was because I immediately pulled out a large leather backpack.

I reached into the backpack and thought,

*Open Inventory.*

With a clatter, three shields were summoned into the backpack.

The wooden shields had been coated with iron on the surface. I had taken them from the armory before leaving the Jin Family of Taiyuan. They were light, sturdy, and perfectly usable.

“Number Seven. Number Eight. Number Nine.”

The three designated reconnaissance squad members accepted the shields with faces that looked ready to die.

Those three had been forcibly selected by me as tanks.

*Seven damage dealers. Three tanks. And me.*

It was a party that would be wiped out the moment it entered a Gate, but for now, I had to be satisfied with this.

“Everyone to your positions.”

Next came formation.

“Basic formation.”

The three shield bearers stood at the front. Six swordsmen, from Number One Hyuk Mujin through Number Six, formed the second row. Han Yeop and I took the rear.

A formation focused on watching the front.

“Spread out. Scatter and assemble. Disperse.”

Their faces were still full of complaints, but they now carried out the commands fairly skillfully. At this point, they were much better than F-rank Hunters who had just graduated from a Hunter training center.

*These NPCs are better than people.*

The difference probably came down to whether they could use internal energy.

Unlike F-rank Hunters, who couldn’t manipulate mana at all, Murim’s NPCs could use internal energy, however faintly.

They were merely low-Level and inexperienced.

I moved on to the final stage of formation training.

“All-out retreat.”

The reconnaissance squad members froze.

“What?”

“What does ‘all-out retreat’ mean?”

“It means exactly what it says. Retreat with all your strength.”

“Then what formation should we—?”

“By then, formation will be meaningless. Just run with all your strength. Don’t even look back. Scatter as much as possible.”

“Heh. You call that an order?”

The owner of the mocking voice was, naturally, Hyuk Mujin.

“I can’t stand this any longer. Third Young Master, is war some children’s game? If you want to make nonsense sound convincing, you should at least have read one military strategy manual before coming here.”

“A military strategy manual?”

“Yes, a military strategy manual! Retreating in good order is one of the most basic principles of warfare. What kind of nonsense are you spouting?”

Hyuk Mujin’s open defiance drew hesitant voices from the other reconnaissance squad members.

“He’s not wrong.”

“We aren’t government soldiers, so why are we practicing formations and being forced to carry shields…?”

“I’ve never heard of an all-out retreat.”

See? Everyone thinks the same way I do. Hyuk Mujin’s smug face seemed to say exactly that.

Then Han Yeop joined in, his voice wavering.

“I-I don’t think that way.”

“What?”

“The Third Young Master—I mean Squad Leader—must have a reason for doing this… right?”

“A reason?”

Hyuk Mujin glared at him.

“What reason could there be? The Third Young Master spent his youth drinking with women instead of training. He caused every kind of trouble despite being like that. And that’s not all. He was also the one who caused this war—”

“Enough.”

Hyuk Mujin flinched when I cut him off. He seemed to realize that he had made a mistake.

But some people were like that. When they needed to back down, they took another step forward instead.

“Wasn’t the Third Young Master the one who caused this war?”

Hyuk Mujin’s pride was too great for him to stop himself.

The words finally left his mouth, and a chilly silence descended.

Gulp.

Someone’s throat bobbed loudly. Nine pairs of eyes turned toward Hyuk Mujin and me.

“D-do you have something to say?”

Something to say? Of course I did.

“Everyone gets another fifteen minutes of rest.”

At the same time, I slapped Hyuk Mujin across the cheek with my flat palm.

Smack!

“One.”

His jaw twisted to the side. It was an ordinary slap, without even a trace of internal energy. His face was still dazed by the sudden turn of events when I struck him a second time.

“What the—!”

He wasn’t completely helpless, at least. He raised his arm to block.

What he had failed to account for was the difference in strength.

Smack!

“Two.”

Hyuk Mujin’s upper body slammed into the ground. He sprang back up, a palm print stamped onto one cheek like a tattoo.

It didn’t take long for his bewilderment to turn into rage.

“You fucking bastard!”

He was properly furious now. As he charged at me with his eyes bulging, I hooked his leg and tripped him. At the same time, I put force into my left hand and struck him.

Smack.

“Three.”

“Urgh.”

His legs seemed to give out, and he staggered. After taking three consecutive blows with this much force, it was only natural that his head would be rattled.

“What, were you saving your internal energy to boil soup?”

That got through to him. Strength filled his wavering legs, and power surged through his body. His eyes glared at me, venom dripping from them.

“You’ll regret this.”

“No, I won’t.”

I caught the fist flying toward my face.

Speed, strength, timing.

I could see all of them. Compared to Lee Seogeun, he was far behind.

“Four.”

Hyuk Mujin’s head snapped back. Sticky blood sprayed through the air in slow motion. His pupils were unfocused, and his legs hung limp.

Yet somehow, he didn’t fall. He couldn’t—not unless I let go of his fist.

“Five.”

Smack!

That was his limit. Hyuk Mujin could no longer endure and passed out. Something fell with a soft thud onto his body, sprawled out in a bizarre position.

*An eye?*

I raised my head toward the sky. The winter sky was raining down small white scraps of garbage.

“Rest is over. We’re leaving.”

I tossed out the words and turned away. Behind me, the reconnaissance squad members finally exhaled the breath they had been holding.

* * *

When Hyuk Mujin woke up two hours later, the first thing he did was charge at me.

“You fucking—!”

Smack. Thud.

“Move him.”

“Y-yes, sir!”

After another ringing slap, he passed out again. The other reconnaissance squad members dragged him into a corner of the cabin.

*A cabin. We got lucky.*

According to one squad member who knew the surrounding area well, we should have reached Jeongyang before sunset at the latest.

But there had been nothing we could do about the sudden blizzard, and this cabin was the only place we had managed to find.

Apparently, it was a hunter’s shelter known only to those familiar with the area.

*It’s ridiculously small, but I’ll take it.*

The mission might be delayed, but this was a hundred times better than walking through the snow all night, collapsing from exhaustion, and then running into the enemy.

That was when—

“Squad Leader?”

It was Han Yeop. The squad members behind him glanced at me, gauging my reaction.

“What should we do now?”

“Hm? Sleep.”

“N-no, that’s not what I meant…”

As I looked at the fidgeting reconnaissance squad members, a thought struck me.

*Don’t tell me…*

“Do you want to train?”

Nod, nod.

Look at the vigorous nodding and those eyes full of passion.

*Seeing is believing, my ass. One beating beats a hundred explanations.*

One beating really was better than explaining a hundred times.

* * *

It was around noon. Sunlight flashed along a sword blade. That was all the martial artist saw.

“Urgh.”

Thud.

His knees buckled, and his face slammed into the frozen ground.

Blood poured from the gaping wound that stretched from his shoulder to his chest. It was a fatal injury. The martial artist knew he was going to die.

“The others… Please, let them live.”

His exhausted voice cut off abruptly. Looking at the martial artist’s wide-open eyes, a middle-aged man clicked his tongue.

“Good grief, you poor fool.”

What were you thinking, charging in like that?

The words that followed never reached the dead man. The fifty-odd wandering martial artists surrounding them snickered.

“Of all people, he had to run into the boss. What rotten luck.”

“Only an orthodox-faction bastard would keep playing the hero right to the end. What should we do, Boss?”

Their gleaming eyes turned toward the survivors. There were six or seven women and children huddled together.

“Great Hero, please spare the children.”

At the plea from the oldest-looking woman, the middle-aged man—Jopil, One Question, One Kill—smiled gently.

“I’m sorry, but what can I do? I’m no Great Hero.”

“But you’re still a person. How can you kill children who can’t even tell right from wrong?”

“Hah. For a woman, you have quite a bit of spirit. Wait. I heard that the family of the Sakju Branch Leader survived. Could it be…?”

“He is my husband.”

“Ah, so he is. I never imagined such a virtuous wife would belong to such a pathetic man.”

Jopil smiled broadly, and the woman’s expression hardened.

“You have no intention of sparing us.”

“Rest easy. I don’t have a taste for tormenting people.”

“The children…”

“This is a harsh world. How are little ones supposed to survive without their mother?”

“You’re worse than a beast.”

“I heard your last words.”

That was the signal.

Swordlight flashed, and screams rang out.

A short while later, the blood-soaked wandering martial artists tossed the corpses into the thickets in the mountains.

“Only the wild animals will feast tonight.”

The man with the tiny birdlike eyes muttered. He was Jopil’s right-hand man, a first-rate wandering martial artist known by the nickname Black Mountain Blade.

“We should feast, too. If we finish this job properly, what’s a mere thousand pieces of gold?”

Jopil laughed with pleasure. The payment for this job would be enormous, but the situation itself was what he enjoyed.

“I never imagined the day would come when we’d hunt the Jin Family of Taiyuan.”

His dirty leather shoe stepped on the fallen martial artist’s corpse.

The martial artist had belonged to the Sakju Branch, one of the ten or so branches of the Jin Family of Taiyuan.

“Was that the last one?”

“No, Boss.”

“They’re slipping away like rats. How many?”

“Three in total. One martial artist and two children. They passed through Jeongyang only a few hours ago and are headed for Honju.”

“That’s troublesome. It’ll take half a day.”

“You don’t need to go yourself. I’ll take care of it.”

“Would you?”

A pleased smile spread across Jopil’s lips.

“Good. Take half of them with you. You have half a day. How does that sound?”

Black Mountain Blade already knew the answer and bowed deeply.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 23`.

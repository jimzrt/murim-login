# Master Edit Task — Chapter 27

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
| 조필     | **Jopil**          |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 하오문    | **Lower District Sect**          |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 살기     | **killing intent**                               |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 낭인     | **wandering martial artist**                     |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 지부장    | **Branch Leader**                            |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 체력               | **Stamina**                    |
| 산서     | **Shanxi**             |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 대사      | **Master** for a senior Buddhist monk                           |
| 공야청 | **Gong Yacheong** |
| 한엽 | **Han Yeop** |
| 소천 | **Socheon** |
| 소율 | **Soyul** |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 당장은 | polysemy | Right away / for now / at the moment; not the broader “anytime soon.” | anytime soon |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 20–24

## Plot

The Jin Family and the Lower District Sect formalize a wartime alliance. In exchange for half of Mount Heng’s shops and exclusive rights to its pleasure district, the Lower District Sect stops selling Shanxi intelligence to other sects and devotes its resources to war intelligence. Wolhwa disguises the agreement by publicly claiming that she and Taekyung spent a passionate night together, presenting it as an unpaid Honghwaru tab. Her investigation has found neither evidence clearing Taekyung nor Lee Seogeun’s killer; she supports the Jin Family because either Taekyung is legitimate or the family is powerful enough to conceal the truth.

Taekyung recognizes Wolhwa’s coachman as Yama Whip, a Peak master. When the gate guards mistake Taekyung for the hero who helped Yama Whip defeat the Heavenly Axe, he encourages the story. The System reports that Poisoner rumors are fading, the Sleeping Dragon of Shanxi rumor is strengthening, and Taekyung gains 20 Fame. Meanwhile, Lee Cheonbaek, Mount Heng’s Sect Leader and Lee Seogeun’s father, expels the poison from his son’s body, vows revenge, and sends about two hundred armed martial artists toward the Jin Family.

Mount Heng’s attack begins with the murder of twenty-five children from the Jin Family’s Saneum, Eung-hyeon, and Sakju branches. The Head Elder calls the deaths necessary sacrifices and uses the Sleeping Dragon rumor and Taekyung’s supposed alliance with Yama Whip to force him into wartime service. Taekyung becomes leader of White Tiger Hall’s reconnaissance squad under the Head Elder’s faction and receives a repeating quest to earn 100 Merit.

The squad consists mostly of inexperienced second-rate martial artists. Taekyung appoints Level 22 Hyuk Mujin, who has killed five bandits, as deputy squad leader and assigns everyone numbers. He imposes a practical Hunter-style schedule, equips three members with wooden shields, and drills formations, dispersal, and all-out retreat. Hyuk mocks the retreat strategy and accuses Taekyung of causing the war. Taekyung knocks him unconscious with a sequence of slaps, then does so again when Hyuk attacks after waking in a hunter’s shelter during a blizzard. The rest of the squad accepts Taekyung’s methods and asks him to train them.

The squad is ordered to scout near Jeongyang and return within five days. A Lower District Sect messenger hawk reports that Jopil, One Question, One Kill, and a special detachment have appeared there. Jopil leads about fifty wandering martial artists in massacring survivors from the Sakju Branch, killing the defending martial artist and several women and children. He orders his First Rate subordinate Black Mountain Blade to pursue one escaping martial artist and two children toward Honju.

Fourteen-year-old Socheon flees with his younger sister, Soyul. Their mother led other survivors away earlier, while their father and the branch families were killed. Gong Yacheong, an old friend of Socheon’s father, guides the children and stays behind to delay the pursuers; his fate is unknown. The siblings reach the reconnaissance squad’s hunter’s shelter as more than twenty Mount Heng pursuers arrive. The System creates the Sudden Quest **Survivors of the Sakju Branch**.

Taekyung first orders an attack formation, then changes to a defensive formation so the squad can hold the enemy back while he claims the kills, EXP, and Merit. He charges alone through the low-level pursuers, using the Jin Family’s Manoeuvre and Spear Techniques and cycling through their forms. He finishes Level 32 Black Mountain Blade with Sky-Piercing Strike, completes the Survivors of the Sakju Branch Quest, receives substantial EXP and Merit, reaches at least Level 20, and triggers a Chain Quest.

## Continuity

- The Jin Family–Lower District Sect alliance lasts for the war. Its terms are half of Mount Heng’s shops, exclusive pleasure-district rights, and exclusive Lower District Sect intelligence support.
- Wolhwa is Eun Sowol, the Level 50 Branch Leader of the Lower District Sect’s Shanxi branch. Yama Whip is her Peak-level coachman.
- Lee Cheonbaek is Mount Heng’s Sect Leader, the Blood Wolf Sword, and Lee Seogeun’s father. He has committed Mount Heng to revenge.
- Taekyung leads ten reconnaissance-squad members in White Tiger Hall. The deployed group has eleven people including Taekyung. The group has nine sword users, one spear user—Level 13 Han Yeop—and no experienced shield user before Taekyung assigns three wooden shields.
- Hyuk Mujin is Level 22, has killed five bandits, and is Taekyung’s deputy squad leader. Han Yeop enthusiastically follows Taekyung’s orders.
- The squad is scouting near Jeongyang under a five-day return deadline. Taekyung’s standard movement cycle is two hours of travel followed by fifteen minutes of rest.
- Jopil, One Question, One Kill, commands about fifty wandering martial artists. Black Mountain Blade, his First Rate right-hand man, is dead.
- Socheon and Soyul survived the Sakju Branch massacre. Their mother’s fate and Gong Yacheong’s fate remain unresolved.
- Taekyung completed the Sudden Quest **Survivors of the Sakju Branch**, gained large EXP and Merit, levelled up repeatedly, and activated a Chain Quest. Its requirements and outcome remain unresolved.
- The war, the unidentified assassin who killed Lee Seogeun, the capsule’s purpose, the route home, and Murim’s death and resurrection rules remain unresolved.

## Translation Decisions

- Preserve **Lower District Sect**, **Branch Leader**, **Honghwaru**, **Yama Whip**, **White Tiger Hall**, **One Question, One Kill**, **Black Mountain Blade**, **Sakju Branch**, **Honju**, and **Jeongyang**.
- Keep the alliance terms precise: half of Mount Heng’s shops, exclusive pleasure-district rights, and exclusive wartime intelligence support.
- Render Taekyung’s staged introduction as: “Yama. Whip. Great Hero!”
- Preserve the repeating 100-Merit quest, the Sudden Quest **Survivors of the Sakju Branch**, and the Chain Quest as distinct System events.
- Retain Taekyung’s practical Hunter-style command, the numbered-squad joke, the formation commands “Form up,” and his EXP-driven decision to claim the enemies himself.
- Preserve the dark comedy and violence of the five-blow sequence, including Hyuk’s accusation and Taekyung’s grip holding him upright.
- Keep **Sky-Piercing Strike** as the final form of the Jin Family’s Spear Technique and retain “Splurt!” for the finishing impact.
- Render `반 시진` as “more than half a shichen,” with a brief factual footnote if used in the chapter translation.

### Prior accepted reading-copy tails

#### Chapter 25 tail (verified mastered)

…
down at the corpse. The face was twisted, its eyes wide open. Frozen beneath blood and snow, the man had been known by the nickname Black Mountain Blade. “Tsk, tsk. How did you end up like this, friend?” He had been loyal and clever. Jopil had never imagined he would die so pointlessly. “See? Haven’t I told you time and again to walk around with both eyes wide open?” Jopil grabbed Black Mountain Blade’s wide-open eyes and pried them even farther open. A horrible sound escaped as the frozen flesh tore. Rip. Riiip. The others watched without even daring to breathe. His expression and tone were no different from usual, but they could feel to their bones that Jopil was furious. The killing intent pouring from the Peak master choked the breath from their throats and sent cold sweat trickling down their backs. *No wonder.* More than twenty men had been wiped out. And all on a mission to deal with the remnants of the Sakju Branch. One Question, One Kill. Jopil was a bizarre man who always asked an enemy he liked exactly one question before killing them. The wandering martial artists considered Black Mountain Blade lucky to be dead. Had he survived, he would have suffered something far more horrifying. “That’s better.” Jopil wiped the blood on the waist of his trousers and rose. “Well, what does everyone think? Tell me without holding back.” “We should obviously follow the order.” One man stepped forward. The neatly dressed, dignified middle-aged man and the ten-odd martial artists standing at attention behind him were the overseers and guides the Mount Heng Sword Sect had sent to keep the wandering martial artists under control. Jopil smiled faintly. “Ah, yes. I’d forgotten our great Mount Heng Sword Sect Hall Master was here. But what’s this about an order?” “Wipe out the Sakju Branch and join the main force. Have you already forgotten the Young Sect Leader’s order?” “An order? I remember accepting a commission.” “Isn’t that the same thing?” The middle-aged man glared at Jopil, displeased. “Coming this far was your own unilateral decision in the first place. And what came of it? You lost more than twenty subordinates to the remnants of a single branch!” “Which is why we should pursue them. We can finish them off in half a day.” “Jeongyang might be another matter, but if you pursue them as far as Honju, we risk a counterattack. I won’t permit any more unilateral decisions.” “Permission. Permission…” Jopil mulled the word over, then spoke. “No. That won’t do. I don’t like it.” “What do you mea—” Crunch. The middle-aged man’s neck shattered, and he died before he could finish speaking. Jopil had twisted it at blinding speed. He licked his lips. “I like war. No matter who dies, they’re forgotten.” “You bastard!” The Mount Heng Sword Sect’s martial artists realized what had happened and drew their weapons, but Jopil had already plunged into their midst. Crunch! Slash! Warm blood poured onto the snowfield. Every time Jopil rampaged like a wild beast, someone’s neck, arm, or leg was torn free and sent flying. “Gaaah…” An unnamed martial artist’s groan was the last sound. Standing atop the heap of corpses, Jopil spoke into the crushing silence. “We’re pursuing them.” This time, no one said a word. As his subordinates hurried to prepare as though fleeing for their lives, Jopil continued to stare at the bodies. *What kind of man was he?* Jopil was a Peak master. From the scars on the corpses and the footprints, he could picture what his opponent looked like. A single man. A highly skilled spearman had been here, and he was the one who had slaughtered the other twenty-odd men. *He killed Black Mountain Blade in one strike. How could he be anything less?* The final strike that pierced through Black Mountain Blade’s chest had been particularly interesting. *This should be a fun fight.* Who was he? A master of the Jin Family of Taiyuan? Or someone unknown? It didn’t matter. Jopil let out a pleased laugh. “Let’s meet soon, friend.” * * * “What news has come in?” “None, sir. All we can do is move as quickly as possible…” “Damn it! Damn it!” Wipeng seethed with frustration, but there was nothing else he could do. As his subordinate had said, their only option was to find the Third Young Master as quickly as possible and protect him. *Jopil, One Question, One Kill…* Wipeng knew the man’s reputation well. If the Third Young Master fell into his hands, death would be the only possible outcome. *If that happens, I won’t be able to face my lord.* Jin Wikyung endured with superhuman patience. He was currently the head and center of the Jin Family of Taiyuan. He had placed the younger brother he loved more than anyone and hundreds of family members on the scales, and after much deliberation, he had sent his most trusted subordinate, Wipeng, to his brother. *But if I fail…* *I won’t be able to face my lord.* Wipeng’s grip tightened on the reins. He spurred his horse onward. More than twenty mounted riders followed in a long line behind him. [^1]: Hong Gil-dong is a legendary Korean outlaw and folk hero. [^2]: In the Hong Gil-dong tale, he demands the right to address his father as “Father” and his elder brother as “Brother.”

#### Chapter 26 tail (verified mastered)

…
through back alleys possibly leave behind? He should at least leave a hide. Leaving twenty stripped corpses behind, they continued onward. After the long night ended, they found the fugitives’ traces around daybreak. *We’ll be meeting soon, friend.* The corners of Jopil’s mouth lifted. This mysterious master was the first in a long while to pique his interest. His long-stiff heart began to pound. * * * I shuddered. “Ugh. What the hell?” A sudden chill ran through me. I raised my arm and found it covered in goose bumps. If this were a scene in a novel, the protagonist would have muttered, *Something feels off,* and gone on his way. But I was different. I acted on firm suspicion. “Hey. Get over here, quick.” I couldn’t see him, but I could feel it. Someone trudging behind me faltered. “W-why?” “I’m counting to three. One, two. Three.” The instant I hit three, Hyuk Mujin rushed over and pressed himself against my side. “It was you, wasn’t it?” “What?” “You were the one. Tell me the truth and I’ll let it slide.” “What are you talking about? It wasn’t me!” I silently stared at his face, swollen like a steamed bun. “You were cursing me behind my back just now, weren’t you?” “Gasp.” “You were cursing me, right?” “I-I was…” I knew it was this bastard. When I raised my hand, Hyuk Mujin squeezed his eyes shut. After getting beaten about three times, he had lost all his fighting spirit. On top of that, he had learned a valuable life lesson: Dodging only meant getting hit more. “Fine. Since you told the truth, I’ll let it go this once.” Hyuk Mujin jerked his head up. “Really?” I gave him a warm smile. “Of course. But don’t even think about deceiving me from now on. I’ll be watching you with mind-reading.” Hyuk Mujin stared at me with demon-filled eyes, then bolted back to his place. If I’d had enough time, I would have crushed his head with a mace. Swallowing my regret, I kept walking. “What’s mind-reading?” The chatter tickled my ears. It belonged to Soyul, Socheon’s little sister. Was she five years old? She was small enough to fit right inside my backpack. “Is it martial arts?” “Something like that.” “Is mind-reading strong?” “Really strong.” “Wow! Soyul wants to learn mind-reading, too!” “But you have to be one-eyed.” “Gasp!” I glanced over and saw Soyul staring at me, startled. Her eyes had gone huge. Ridiculously cute. *Hayeon used to be like that, too.* These days she was a gross little sister, but when she was little she had been a baby angel. She had even gotten offers to be a child model… Carrying her on my back felt exactly like carrying Hayeon when she was that age. “Want me to teach you?” “…Soyul doesn’t like martial arts. I want to become a proper young lady.” “That’s fine, too.” “Mm-hmm. Mister, do you like martial arts?” “Me?” “My brother says you’re really strong. Dad said only people who work hard can become strong.” “Your dad said that?” “Yes. My dad is really strong, too. Because…” She chattered excitedly for a while, then stuck out her lower lip. “Soyul wants to see Dad. But I guess Dad doesn’t want to see us. Oppa says he went out to play with Mom, leaving me and Oppa behind.” My heart dropped with a thud. An old memory filled my vision. In a funeral hall of black and white, little Hayeon had searched for our father, and I had no choice but to tell her an obvious lie. Just as Socheon had done for Soyul. It was the only thing I could say. “…I see.” What else could I say? I looked at Socheon, following along in the middle of the formation. He was panting hard, drenched in sweat. *He must be exhausted.* His willpower was far beyond his years. The saying that pain made people mature was fucked up, but it was true. Socheon hadn’t fallen behind even once, and the other reconnaissance squad members marveled at him for it. *But the real problem is somewhere else.* Gong Yacheong. His face was deathly pale; he still hadn’t shaken off his injuries. If not for the remarkable effects of the fasting pills I had given him, and the qi he had circulated last night, he might have collapsed long ago. *At this rate, we’ll be caught.* Even after the sun rose, the accumulated snow wouldn’t easily melt. I was out front, forcing a path through it, but everyone was exhausted, and our pace had slowed. On top of that, we had an injured man and children. *Should I run away by myself?* The thought came to me in an instant. It was a game. So what? Gong Yacheong, those two kids, the whole reconnaissance squad—every last one of them was created AI. Just NPCs. But me? I was alive. Among all of them, I was the only one who was real. The only one with a real body. But… *Fuck. It’s a simple problem… Why am I like this?* An inexplicable aversion surged through me. It was strong enough to startle me—strong enough to throw me off. *Why?* I didn’t know. I didn’t find the answer for hours after that, and then night came. [^1]: A shichen is a traditional time period of roughly two hours.

## Korean source

```text
＃27화



“일각 휴식.”

바람 빠지는 소리를 내며 순찰조원들이 주저앉는다.

힘들어 보이긴 하지만 저놈들이야 뭐, 별다른 걱정은 안 한다. 지켜본 대로라면 기초 체력은 탄탄했고, 전투 때도 넋 놓고 구경만 한 녀석들이니까.

다른 두 명이 문젠데…….

“괜찮아?”

“후욱. 괜찮, 괜찮습니다.”

소천이 거칠게 숨을 몰아쉬며 대답했다. 내가 보기에도 당장은 쓰러질 것 같진 않다. 하지만 지금처럼 이동했다가는 조만간 한계에 부딪힐 것이다.

‘어린 녀석이 고집은 세 가지고.’

앞서 나는 소천에게 제안했었다. 동생과 함께 내게 업혀 가는 게 어떻겠냐고. 답은 단호한 거절이었다.

“힘들면 말해. 너희 둘 정도는 감당할 수 있으니까.”

“지금으로도, 후욱. 충분합니다.”

아닌 것 같은데.

“모두를 위해서 하는 말이다. 쉽게 대답하지 마.”

“알겠습니다.”

대답하는 소천의 눈에 힘이 들어갔다. 나는 곤히 잠들어 있는 소율을 녀석에게 안겨 주고 돌아섰다.

“공 대협.”

핏기 없는 얼굴이 고개를 들었다.

“……진 공자.”

금방이라도 꺼질 듯한 목소리다. 이거 상태가 생각보다 심각한데. 괜찮습니까, 라는 물음이 혀끝에 맴돌다 흩어진다.

“얼마나 버틸 수 있겠어요?”

“모르겠소.”

솔직한, 그리고 심각한 대답이었다.

“벽곡단은요?”

그에게 남은 벽곡단을 몇 개 챙겨 주었었다. 하지만 공야청은 고개를 내저어 보였다.

“별 효력이 없더군요. 어떤 돌팔이가 만들었는지 입맛만 버렸소. 하하.”

“……지금 저 웃으라고 하는 소립니까?”

“재미없었소?”

“네. 하나도.”

“그거 안타깝…… 쿨럭.”

갑작스러운 기침. 흰 눈 위로 핏방울이 떨어진다.

이런 제기랄. 나는 혹여 누가 볼까, 황급히 공야청의 앞을 가로막았다.

“뭡니까? 이 정도는 아니었잖아요.”

반나절 만에 급속도로 악화된 모습이다. 지금의 공야청은 피로가 쌓인 것이 아니라 병자의 기색이 완연했다.

“예견된 일이오.”

공야청의 담담한 눈빛. 그래서 더 불길하다. 만류하는 그의 손길을 뿌리치고 상의 앞부분을 걷어 올렸다.

“아.”

그의 몸은 온갖 상처로 뒤덮여 있었다. 그러나 나를 놀라게 한 것은, 아랫배를 중심으로 퍼렇게 돋아난 핏줄이었다.

“이게 무슨…… 설마?”

공야청이 힘없는 손길로 상의를 여몄다. 다른 누군가, 특히 소천 남매가 볼까 염려하는 듯했다.

“이리 같은 놈들이오. 병장기에 독을 발라 놨더군.”

공야청이 벽곡단을 먹어도 회복되지 않는 이유를 이제야 알겠다. 벽곡단은 허기와 기력만 보충해 줄 뿐, 해독 능력은 전혀 없으니까.

“진작 말했어야죠!”

“그놈들, 돈이 없었는지 싸구려 독을 썼더군. 독기가 미약해서 지난밤에야 알아차렸소. 너무 늦었지.”

독에 당했을 때 공야청의 체력은 이미 바닥이었다. 그런 상황에서 이 날씨에 강행군을 계속했으니…….

“방법이 없습니까?”

“있소.”

“알려 주십시오.”

“하지만 시간이 허락해 주지 않겠지. 나 하나 때문에 천금 같은 시간을 버릴 수는 없소.”

맞는 말이다. 하지만.

“시도는 해 봐야죠.”

“공자.”

“다들 많이 지쳤습니다. 한 시진, 아니 반 시진만 쉬면서 방법을 시도해 보면 될 겁니다.”

“하하.”

“웃지 마시고요. 어차피 이쯤에서 쉬어 갈 생각이었으니까…….”

모르겠다. 지금 내가 무슨 말을 하는지. 횡설수설하는 나를 보는 공야청의 입가에 희미한 미소가 떠올랐다.

“가시오.”

“…….”

“공자도 알고 있지 않소? 지금 시간을 지체한다면 발목이 잡힐 거라는 사실을.”

나는 침묵했다. 그의 말이 맞다. 위태위태한 안색과 각혈하는 모습을 봤을 때부터, 어쩌면 어젯밤부터 이런 상황을 염두에 두고 있었다.

‘결국 이렇게 되나?’

공야청을 버려야 한다. 데려간다면 당장은 살겠지만 그 대신 모두의 발걸음이 느려질 것이다.

만약 내가 그를 짊어진다면?

시스템의 힘을 빌린다지만, 나도 사람이다. 선두에서 길을 만들어 가며 이틀을 걸었고 그만큼의 피로가 누적되었다.

‘남은 벽곡단은 두 개.’

서른 개에 달하던 벽곡단도 다 떨어져 간다. 남은 두 개로 공야청을 짊어진 채 놈들의 손아귀를 벗어날 수 있을까?

그렇게 하고도 끝내 놈들과 맞닥뜨리게 된다면? 지친 상태에서 놈들을, 절정 고수인 일문일살 조필을 상대할 수 있을까?

답은 오래전에 나왔다. 나도, 그도 알고 있었다.

“아이들을 부탁하오.”

공야청의 말과 동시에 시스템 알림이 울린다.

띠링.



퀘스트



[공야청의 마지막 부탁]

이제 그가 바라는 것은 하나뿐입니다. 살아남은 아이들을 안전하게 생환시켜 주십시오.



등급 : 無

제한 : 진태경

임무 : 소천, 소율의 생환 (미완료)

보상 : 없음



- 퀘스트를 수락하시겠습니까?



보상이 없다니.

내가 받아 본 것 중 가장 양심 없는 퀘스트다.

‘나 살기도 바빠, 이 양반아.’

하지만 나는 고개를 끄덕였다. 이걸로 마음 한구석 찝찝함을 덜어 낼 수 있다면 얼마든지.

“그렇게 하죠.”

공야청이 만족스럽게 웃었다.



* * *



“공 대협을 두고 간다고요?”

한엽이 충격받은 얼굴로 중얼거렸다. 혁무진은 무슨 생각을 하는지 말이 없었고, 다른 정찰조원들은 서로 눈치를 살피느라 바빴다.

“그래.”

“말도 안 됩니다!”

“목소리 줄여.”

소천이 알아봤자 좋을 게 없다. 함께 남겠다고 버티고 설 놈이라 더더욱 그랬다.

“하, 하지만 이건…….”

“공 대협이 결정한 거다. 내 생각도 같고.”

그때, 혁무진이 불쑥 입을 열었다.

“이유가 뭡니까?”

이 자식이 덜 맞았나. 나는 눈에 힘을 줬지만 혁무진은 겁먹지도, 물러서지도 않았다. 불끈 쥔 주먹에 힘이 풀렸다.

“상태가 심각해. 이대로라면 우리까지 위험하다.”

“그게 전부입니까?”

“그래.”

한엽이 붉어진 얼굴로 끼어들었다.

“안 됩니다.”

“명령이다.”

“그럼 항명하겠습니다.”

단호한 말투에 모두가 놀란 눈빛으로 한엽을 바라본다.

첫 만남부터 내 열렬한 신봉자를 자처하던 녀석이, 항명을 입에 담을 줄은 나도 몰랐다.

“네가 그런다고 달라지는 건 없어.”

“이대로 두고 갈 수는 없습니다.”

“두고 갈 수 없으면?”

갑자기 피곤이 몰려왔다. 나는 뻑뻑해진 눈가를 문질렀다.

“두고 갈 수 없으면. 네가 업고 갈래?”

“예. 제가 업겠습니다.”

“그리고 금방 지치겠지.”

한엽이 지치면 누군가 나서서 돕겠지. 그렇게 하나씩 지쳐 가고, 발걸음은 느려지고, 적들이 들이닥칠 것이다.

“상대는 절정 고수가 이끄는 닳고 닳은 낭인들이다. 우리가 살아남을 수 있을까?”

한엽은 대답하지 못하고 고개를 떨궜다. 다른 정찰조원들도 시선을 회피했다. 내 눈을 피하지 않는 건 한 사람뿐이다.

“일 호. 아직 할 말이 남았나?”

한참이나 말이 없던 혁무진이 고개를 숙였다.

“명령에 따르겠습니다, 조장님.”



* * *



우리는 다시 이동을 시작했다. 출발 직전, 공야청은 편안한 얼굴로 소천, 소율 남매의 머리를 쓰다듬어 주었다.

“잠시 후에 보자꾸나.”

소천은 씩씩하게 고개를 끄덕였고, 잠이 덜 깬 소율은 칭얼거리며 내 품에 안겼다. 쌕쌕거리는 숨소리를 들을 때마다 가슴 한구석이 불편해진다.

‘지금쯤이면 떠났을까?’

공야청은 어린 남매에게 자신의 부재를 알리고 싶지 않아 했다. 그래서 도중에 조용히 이탈하겠다고 내게 말했다.

소천은 대열의 중간이니 정찰조원들에 가려져 떠나는 그의 모습을 확인할 수 없을 것이다.

‘출발한 지 얼마나 지났지?’

한 식경? 반 시진? 모르겠다. 사방이 어둠에 잠긴 깊은 밤 속에서는 시간의 흐름도 느껴지지 않았다.

한 걸음씩 옮길 때마다 한 가지 생각이 머릿속에서 떠나가지 않는다.

‘떠났겠지. 지금쯤이면.’

당연한 일이었다. 공야청도 나도 알았고 한엽을 제외한 정찰조원들도 수긍했다. 무엇보다…… 내게는 기다리고 있는 가족이 있다. 나가서 맞닥트릴 현실이 있다.

‘그런데 기분이 왜 이렇게 더럽지?’

발이 무겁다. 종아리까지 쌓인 눈 때문만은 아니다. 앞길을 가로막는 풀과 나뭇가지 때문이 아니다.

공야청이라는, 일개 NPC가 자꾸만 마음에 걸렸다.

마지막 웃음이, 보상 하나 없는 싸구려 퀘스트가 생각났다.

항명하던 한엽이 생각났고, 혁무진의 담담한 눈빛이 가시처럼 가슴 한구석을 찔렀다.

‘당연한 건데 왜.’

게임이니까. 게임이라서.

안 버리면 다 죽는다고. 내가 죽는다고! 이 개새끼들아.

“씨이발…….”

목구멍에 턱 걸려 있던 욕이 흘러나온다. 선잠에서 깬 소율이 뭐라 웅얼거리며 내 목을 끌어안았다.

앙증맞을 정도로 작은 손은 차가웠다. 피부 위로 소름이 돋을 정도로 생생했다. 게임이라고는 생각할 수 없을 정도로.

고작 NPC 하나 버린 걸로 양심의 가책을 느낄 정도로.

“……게임 진짜 좆같이 만들었네.”

나는 돌아섰다.

“어디 가십니까?”

성큼성큼 왔던 길을 돌아갔다. 소천도, 정찰조원들의 얼굴도 눈에 들어오지 않았다.

그래서 알 수 없었다. 앞서 어딜 가냐 묻는 혁무진의 얼굴에 얼핏 웃음이 스친 것도, 가장 후미에 있어야 할 한엽의 얼굴이 보이지 않았던 것도.

“훅. 후욱.”

눈밭 위를 바람처럼 내달렸다. 그리고 발견했다.

언덕 아래, 숨이 턱에 차 헐떡거리면서도 이를 악물고 발걸음을 내딛는 한엽의 모습을.

녀석의 등에는 혼절한 공야청이 업혀 있었다.

“너…….”

무슨 말을 해야 할지 모르겠다. 나는 한숨과 함께 한엽의 손을 잡고 끌어올렸다.

“가, 감사합니다.”

시바…….

‘이젠 나도 모르겠다.’



* * *



이곳은 한 사람만을 위한 비처(秘處)다.

그는 삼십 년 전부터 이곳의 주인이 된 후 그 누구의 출입도 금했다. 그것은 세월이 흐르며 굳어 버린 법칙이었고, 다른 이들도 그렇게 생각했다.

- 일은 어떻게 되어 가고 있습니까?

미세한 공기의 울림과 함께 두 그림자는 전음으로 대화를 나누었다.

- 순조롭네. 그쪽은?

- 말해야 입 아프지요.

- 어련할까.

- 혈랑검. 별호치고는 정이 많더군요.

- 이리라고 혈육의 정이 없겠나. 그래서?

- 선발대만 이백입니다. 조필이라고, 웬 정신 나간 놈이 제멋대로 날뛰고 있긴 한데…… 뭐, 괜찮겠지요.

- 일문일살 조필? 혈랑검이 제대로 골랐군.

- 망나니 공자가 정신없이 쫓기고 있더군요. 예상에 없던 일이긴 합니다만 이것도 나쁘지 않죠.

- 하하하.

- 혹시?

- 맞네. 내가 보냈네. 끔찍이 아끼는 막냇동생의 목을 보면, 소가주도 마음을 달리 먹겠지.

- 크으, 피도 눈물도 없는 독심. 존경스럽습니다.

- 자네가 할 말인가?

- 저야 답 없는 목숨 하나를 취했을 뿐인데요.

- 덕분에 산서성에 피바람이 불 테고?

- 바라던 바 아닙니까?

- 부정할 수 없군. 맞네. 너무 오래 기다렸어.

- 과실은 더욱 달콤할 겁니다.

- 그러길 바라네.

- 아, 참. 하오문이 끼어들었습니다.

- 하오문? 그놈들이 어떻게?

- 새로 온 지부장이 코가 좋더군요. 이번 일만 마무리되면 쳐 낼 생각입니다.

- 조심하게. 천(天)이 아무리 대단해도 방심은 금물…….

그 순간, 바람이 그쳤다. 공기가 파르르 떨렸다.

- ……내가 실언을 했군.

다시 전음이 들려온 것은 한참 뒤였다.

- 언행에 주의하시는 편이 좋겠습니다.

고양이 발바닥처럼 부드러운 목소리. 그러나 듣는 이는 느꼈다. 시퍼렇게 날이 선 칼날을.

- 내 다시 한번 사과하지.

- 오늘은 이쯤 하지요. 문제가 생기면 일간 다시 찾아뵙겠습니다.

대화는 그것으로 끝이었다. 어떤 기척도, 소리도 없이 상대는 사라졌다.

‘귀신 같은 자들.’

가끔은 궁금할 때가 있었다. 저들의 진정한 정체가 무엇인지. 힘은 어느 정도고 구성원은 누구인지.

하지만 이내 고개를 가로저었다.

‘명을 단축할 뿐.’

인고의 세월을 견딘 것은 과실을 취하기 위해서다. 단순한 호기심으로 대사를 그르칠 수야 있나.

‘참으로 길었다.’

그림자는 달을 향해 손을 뻗었다. 손가락 사이로 새어 나온 희미한 달빛이 은빛 수염을 비추었다.

‘곧…… 모든 것이 제자리를 찾는다.’

대장로는 기껍게 웃었다.
```

## Current accepted English baseline

```markdown
# Chapter 27

“Fifteen-minute break.”

The reconnaissance squad members dropped to the ground with a sound like the air going out of them.

They looked exhausted, but I wasn’t particularly worried about those guys. As I’d observed, they had solid basic stamina, and during the battle they had done nothing but stand around and watch.

The other two were the problem…

“Are you all right?”

“Huff. I’m fine. I’m fine.”

Socheon answered while breathing heavily. He didn’t look like he was about to collapse just yet. But if he kept traveling like this, he would hit his limit before long.

*He’s a stubborn little brat.*

Earlier, I had offered to carry him and his sister. He had refused without hesitation.

“If you’re having trouble, tell me. I can handle carrying both of you.”

“Huff. I’m fine like this. It’s enough.”

*Doesn’t look like it.*

“I’m saying this for everyone’s sake. Don’t answer so quickly.”

“Understood.”

His eyes hardened as he answered. I placed the peacefully sleeping Soyul in his arms and turned around.

“Great Hero Gong.”

The pale-faced man raised his head.

“…Young Master Jin.”

His voice sounded like it might give out at any moment. His condition was worse than I’d expected. The question *Are you all right?* lingered on the tip of my tongue before fading away.

“How long can you hold out?”

“I don’t know.”

His answer was honest—and serious.

“What about the fasting pills?”

I had given him several of the fasting pills I had left. But Gong Yacheong shook his head.

“They’re not very effective. Some quack must have made them. They’ve done nothing but ruin my appetite. Hahaha.”

“…Are you telling me that to make me laugh?”

“Wasn’t it funny?”

“No. Not at all.”

“That’s a shame… Cough!”

A sudden cough.

Drops of blood fell onto the white snow.

*Damn it.*

Worried that someone might see, I hurriedly stepped in front of Gong Yacheong.

“What happened? You weren’t this bad before.”

His condition had deteriorated rapidly in half a day. Gong Yacheong no longer looked merely exhausted. He unmistakably looked like a sick man.

“It was inevitable.”

The calm look in his eyes made it even more ominous. I brushed aside the hand trying to stop me and pulled up the front of his robe.

“Ah.”

His body was covered in all kinds of wounds. But what shocked me were the blue veins spreading outward from his lower abdomen.

“What is this…? Don’t tell me…”

Gong Yacheong weakly fastened his robe again. He seemed worried that someone else—especially Socheon and Soyul—might see.

“Those wolf-like bastards coated their weapons with poison.”

Now I understood why Gong Yacheong hadn’t recovered even after taking the fasting pills. They could only stave off hunger and restore stamina. They had no detoxifying effect whatsoever.

“You should have told me sooner!”

“Those bastards must have been short on money. They used cheap poison. Its potency was weak, so I didn’t notice until last night. By then, it was too late.”

Gong Yacheong’s stamina had already been at rock bottom when he was poisoned. Then he had continued forcing himself through this weather…

“Isn’t there anything we can do?”

“There is.”

“Tell me.”

“But time won’t allow it. I can’t waste such precious time on one person.”

He was right.

But still…

“We have to try.”

“Young Master.”

“Everyone is exhausted. If we rest for one shichen[^1]—no, just half a shichen—and try the method, that should be enough.”

“Hahaha.”

“Please don’t laugh. I was planning to stop and rest around here anyway…”

I didn’t know what I was saying anymore. As Gong Yacheong watched me ramble, a faint smile appeared at the corner of his mouth.

“Go.”

“…”

“You know it too, don’t you? If we waste time here, we’ll be held back.”

I fell silent.

He was right. I had been considering this possibility since I saw his precarious complexion and the blood he coughed up. Perhaps I had been thinking about it since last night.

*So this is how it ends?*

I had to leave Gong Yacheong behind. If I took him with us, he might survive for now, but everyone’s pace would slow down.

What if I carried him myself?

Even with the System’s help, I was still human. I had spent two days walking at the front and clearing a path. Fatigue had piled up with it.

*Two fasting pills left.*

Even the thirty fasting pills I’d had were almost gone. Could I escape those bastards while carrying Gong Yacheong with only two pills remaining?

And if we still ended up running into them, would I be able to fight them while exhausted? Would I be able to face Jopil, One Question, One Kill, a Peak master?

The answer had been clear for a long time.

We both knew it.

“Please take care of the children.”

The moment Gong Yacheong spoke, the System notification rang.

Ding.

> **System**
>
> **Quest**
>
> **Gong Yacheong’s Last Request**
>
> He wants only one thing now. See that the surviving children make it back safely.
>
> **Grade:** None
>
> **Limit:** Jin Taekyung
>
> **Task:** Socheon and Soyul’s safe return (Incomplete)
>
> **Reward:** None
>
> - Would you like to accept the Quest?

There was no reward.

It was the most shameless Quest I had ever received.

*I’m busy trying to stay alive myself, old man.*

But I nodded.

If accepting it could ease even a little of the guilt sitting in the corner of my heart, I was willing to do it.

“Let’s do that.”

Gong Yacheong smiled with satisfaction.

* * *

“You’re saying we’re leaving Great Hero Gong behind?”

Han Yeop muttered with a shocked expression. Hyuk Mujin said nothing, as though he was lost in thought, while the other reconnaissance squad members were busy watching one another’s faces.

“Yes.”

“That makes no sense!”

“Lower your voice.”

There was nothing to gain from Socheon finding out. That was especially true because he would insist on staying behind with Gong Yacheong.

“B-but this…”

“It was Great Hero Gong’s decision. I agree with him.”

That was when Hyuk Mujin suddenly spoke.

“What’s the reason?”

*Has this bastard not been beaten enough?*

I glared at him, but Hyuk Mujin neither flinched nor backed down. My fist, which had tightened instinctively, slowly relaxed.

“His condition is serious. If we continue like this, he’ll put all of us in danger.”

“Is that all?”

“Yes.”

Han Yeop cut in, his face flushed.

“No.”

“It’s an order.”

“Then I’ll disobey.”

Everyone stared at Han Yeop in surprise.

I hadn’t expected the boy who had declared himself my ardent follower from the very first time we met to use the word *disobey*, either.

“Nothing will change just because you say that.”

“We can’t leave him like this.”

“If we can’t leave him behind, then what?”

Fatigue suddenly swept over me. I rubbed at the corners of my stiff eyes.

“I’ll carry him.”

“Yes. I’ll carry him.”

“And you’ll get tired soon.”

If Han Yeop got tired, someone else would step forward to help him. Then they would grow tired one by one, our pace would slow, and the enemy would catch up.

“Our opponents are a pack of battle-hardened wandering martial artists led by a Peak master. Do you think we can survive?”

Han Yeop lowered his head without answering. The other members of the reconnaissance squad avoided my gaze as well.

Only one person continued to meet my eyes.

“Number One. Do you still have something to say?”

Hyuk Mujin had been silent for a long time. He finally bowed his head.

“I’ll follow your orders, Squad Leader.”

* * *

We began moving again.

Just before we left, Gong Yacheong gently stroked Socheon and Soyul’s heads with a peaceful expression.

“I’ll see you soon.”

Socheon nodded bravely. Soyul, still half-asleep, whimpered and nestled into my arms.

Every time I heard her shallow, wheezing breaths, a pang of unease tightened in my chest.

*Has he left by now?*

Gong Yacheong hadn’t wanted the children to know he was gone. That was why he had told me he would quietly slip away along the way.

Socheon was in the middle of the formation, so the reconnaissance squad members would block his view. He wouldn’t be able to see Gong Yacheong leave.

*How long has it been since we left?*

A sikyeong? Half a shichen?

I didn’t know. In the dead of night, with darkness swallowing everything around us, I couldn’t even feel time passing.

With every step I took, one thought refused to leave my mind.

*He must have left by now.*

It was only natural. Gong Yacheong and I knew it, and everyone in the reconnaissance squad except Han Yeop had accepted it.

Most importantly…

I had a family waiting for me. The real world was waiting for me outside.

*Then why does this feel so damn awful?*

My feet felt heavy.

It wasn’t just because snow had piled up to my calves. It wasn’t because grass and branches blocked the path ahead.

It was because a mere NPC named Gong Yacheong kept weighing on my mind.

I thought about his final smile. I thought about the cheap Quest with no reward.

I thought about Han Yeop’s defiance. Hyuk Mujin’s calm gaze pricked my chest like a thorn.

*It’s only natural. So why?*

Because it was a game.

Because it was only a game.

*If I didn’t leave him behind, everyone would die. I’d die, too! You fucking bastards!*

“Fuuuck…”

The profanity that had been caught in my throat spilled out.

Soyul stirred from her light sleep and mumbled something as she wrapped her arms around my neck.

Her tiny hands were cold. They felt so real that goose bumps rose across my skin. Too real to believe this was a game.

Real enough that I felt guilty over abandoning a single NPC.

“…What a fucked-up game.”

I turned around.

“Where are you going?”

I strode back the way we had come. I couldn’t see Socheon’s face or the faces of the reconnaissance squad members.

That was why I didn’t notice the fleeting smile that crossed Hyuk Mujin’s face when he asked where I was going.

I also didn’t notice that Han Yeop, who should have been at the very rear, was no longer there.

“Huff. Huuuff.”

I sprinted across the snow like the wind.

And then I found him.

Below the hill, Han Yeop was gritting his teeth and forcing one foot in front of the other despite gasping for breath.

Gong Yacheong, unconscious, was on his back.

“You…”

I didn’t know what to say. With a sigh, I grabbed Han Yeop’s hand and pulled him up.

“Th-thank you.”

*Shit.*

*I don’t know anymore, either.*

* * *

This was a hidden retreat reserved for one person.

After becoming its owner thirty years ago, he had barred everyone else from entering. Over time, that had hardened into an unbreakable rule, and the others thought of it the same way.

“How are things going?”

As the air trembled faintly, the two shadows conversed through Sound Transmission.

“Smoothly. And you?”

“There’s no need to ask.”

“I wouldn’t expect otherwise.”

“The Blood Wolf Sword. He’s surprisingly fond of his family for someone with that epithet.”

“A wolf can still love its own blood. So?”

“The vanguard alone numbers two hundred. A madman named Jopil is running wild as he pleases, but… it should be fine.”

“Jopil, One Question, One Kill? The Blood Wolf Sword chose well.”

“The wastrel young master is being chased for his life. It wasn’t part of the plan, but it isn’t bad, either.”

“Hahahaha.”

“Could it be…?”

“That’s right. I sent him. When the Lesser Family Head sees the head of his beloved youngest brother, he’ll change his mind.”

“Whew. A heart as cold as poison, without blood or tears. Impressive.”

“Is that something you should be saying?”

“I only took one hopeless life.”

“And thanks to that, a bloody storm will sweep across Shanxi?”

“Isn’t that what you wanted?”

“I can’t deny it. Yes. I’ve waited too long.”

“The fruit will be all the sweeter.”

“I hope so.”

“Ah, yes. The Lower District Sect has gotten involved.”

“The Lower District Sect? How did they?”

“The new Branch Leader has a good nose. Once this matter is finished, I plan to drive them out.”

“Be careful. No matter how formidable Heaven may be, one must never let one’s guard down…”

At that moment, the wind stopped.

The air trembled.

“…I misspoke.”

It was a long while before another message came through Sound Transmission.

“It would be wise to watch your words and actions.”

The voice was soft as a cat’s paw.

But the listener could feel the razor-sharp blade hidden beneath it.

“Let me apologize once more.”

“Let’s end things here for today. If a problem arises, I’ll come see you again soon.”

The conversation ended there.

The other person vanished without a sound or trace.

*They were like ghosts.*

Sometimes, he wondered what their true identities were. How strong were they? Who were their members?

But he soon shook his head.

*That would only shorten my life.*

He had endured years of hardship to reap the fruit. He couldn’t let mere curiosity ruin his plans.

*It truly has been a long time.*

The shadow reached a hand toward the moon. Faint moonlight slipping between his fingers illuminated a silver beard.

*Soon… everything will fall into place.*

The Head Elder smiled with delight.

[^1]: A shichen is a traditional time period of roughly two hours; a sikyeong is a shorter traditional interval.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 27`.

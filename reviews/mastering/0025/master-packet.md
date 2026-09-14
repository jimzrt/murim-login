# Master Edit Task — Chapter 25

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
| 진위경    | **Jin Wikyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 조필     | **Jopil**          |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 살기     | **killing intent**                               |                                                       |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 낭인     | **wandering martial artist**                     |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 지부장    | **Branch Leader**                            |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 로그아웃             | **Logout**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 흑산도 | **Black Mountain Blade** |
| 공야청 | **Gong Yacheong** |
| 소천 | **Socheon** |
| 소율 | **Soyul** |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
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

#### Chapter 23 tail (verified mastered)

…
sprayed through the air in slow motion. His pupils were unfocused, and his legs hung limp. Yet somehow, he didn’t fall. He couldn’t—not unless I let go of his fist. “Five.” Smack! That was his limit. Hyuk Mujin could no longer endure and passed out. Something fell with a soft thud onto his body, sprawled out in a bizarre position. *Snow?* I raised my head toward the sky. The winter sky was raining down small white scraps of garbage. “Rest is over. We’re leaving.” I tossed out the words and turned away. Behind me, the reconnaissance squad members finally released the breaths they had been holding. * * * When Hyuk Mujin woke two hours later, the first thing he did was charge at me. “You fucking—!” Smack. Thud. “Move him.” “Y-yes, sir!” Another satisfying slap knocked him out cold. The other reconnaissance squad members dragged him into a corner of the cabin. *A cabin. We got lucky.* According to one squad member who knew the surrounding area well, we should have reached Jeongyang before sunset at the latest. But there was nothing we could do about the sudden heavy snowfall, and this cabin was the only place we had managed to find. Apparently, it was a hunters’ shelter known only to people familiar with the area. *It’s ridiculously small, but I’ll take it.* The mission might be delayed, but this was a hundred times better than walking through the snow all night and then running into the enemy while utterly exhausted. That was when— “Squad Leader?” It was Han Yeop. Behind him, the other squad members stole glances at me, trying to gauge my mood. “What should we do now?” “Hm? Sleep.” “N-no, that’s not what I meant…” As I looked at the fidgeting reconnaissance squad members, a thought struck me. *Don’t tell me…* “Do you want to train?” Nod, nod. Look at those heads bobbing furiously. Look at those eyes burning with enthusiasm. *Forget seeing once. One beating beats hearing something a hundred times.* One beating really was better than a hundred explanations. * * * It was around noon. Sunlight flashed along a sword blade. That was the only thing the martial artist managed to see. “Urgh.” Thud. His knees buckled, and his face slammed into the frozen ground. Blood poured from the gaping wound that ran from his shoulder to his chest. There was no recovering from an injury like that. The martial artist knew he was going to die. “The others… Please, spare them.” His exhausted voice cut off abruptly. Looking at the martial artist’s wide-open eyes, a middle-aged man clicked his tongue. “Good grief, you poor fool.” What were you thinking, charging in like that? The rest of his words never reached the dead man. The fifty-odd wandering martial artists surrounding them snickered. “Of all people, he had to run into the boss. What rotten luck.” “Only an orthodox-faction bastard would keep playing the hero right to the bitter end. What should we do, Boss?” Their gleaming eyes turned toward the remaining survivors—a group of six or seven women and children. “Great Hero, please spare the children.” At the plea from the oldest-looking woman, the middle-aged man—One Question, One Kill Jopil—smiled gently. “I’m sorry, but what can I do? I’m no Great Hero.” “But you’re still human. How can you kill children who can’t even tell right from wrong?” “Hah. You have quite a bit of spirit for a woman. Wait. I heard the Sakju Branch Leader’s family survived. Could you be…?” “He is my husband.” “Ah, I thought so. Who would have imagined such a pathetic man could have such a virtuous wife?” Jopil smiled, and the woman’s expression hardened. “You have no intention of sparing us.” “Don’t worry. I’m not in the habit of raping women before I kill them.” “The children…” “This is a harsh world. How could little ones survive without their mother?” “You’re worse than a beast.” “I heard your last words.” That was the signal. Swordlight flashed, and screams rang out. A short while later, the blood-soaked wandering martial artists tossed the corpses into the mountain thickets. “Looks like the wild animals will be the only ones feasting.” The man with tiny, birdlike eyes muttered. He was Jopil’s right-hand man, a first-rate wandering martial artist known as Black Mountain Blade. “We should feast, too. If we finish this job properly, what’s a mere thousand pieces of gold?” Jopil laughed with pleasure. The payment for this job would be enormous, but the situation itself was what he enjoyed. “I never imagined the day would come when we’d hunt the Jin Family of Taiyuan.” He planted a filthy leather shoe on the fallen martial artist’s corpse. The martial artist had belonged to the Sakju Branch, one of the ten or so branches of the Jin Family of Taiyuan. “Was that the last of them?” “No, Boss.” “They’re slipping away like rats. How many?” “Three in total. One martial artist and two children. They passed through Jeongyang only a few hours ago and are heading for Honju.” “That’s troublesome. It’ll take half a day.” “There’s no need for you to go yourself, Boss. I’ll take care of it.” “Would you?” A pleased smile spread across Jopil’s lips. “Good. Take half the men. You have half a day. How does that sound?” The answer was already decided. Black Mountain Blade bowed deeply.

#### Chapter 24 tail (verified mastered)

…
> - Sudden Quest has been created! > > **Quest** > > **Survivors of the Sakju Branch** > > You have encountered survivors from the Sakju Branch of the Jin Family of Taiyuan. > > Rescue the survivors from the Mount Heng Sword Sect’s merciless pursuers! > > **Grade:** Sudden Quest > **Limit:** Jin Taekyung > **Task:** Rescue the survivors — Incomplete > **Reward:** Chain Quest > ??? > **Failure:** ??? “…” “…” We looked at them. They looked at us. A deathly silence settled over the frozen clearing. *I knew it. I knew this was how it would turn out.* But it was too late for regrets. What could I do about my cursed luck? I let out a deep sigh and shouted. “Attack formation. Form up!” Clack-clack-clack. Despite being caught off guard, the squad members moved as they had been taught. By the time they had formed up, the enemy had realized who we were and started shouting. “They’re brats from the Jin Family of Taiyuan!” “There aren’t many of them! Wipe them out!” *Brats. Outnumbered.* They’d pinpointed the two facts that tore at my chest. I hadn’t even finished teaching these guys. Their martial arts were weak, they had no real combat experience, and they were complete rookies. *If things go bad, should I bolt by myself?* Feeling utterly hopeless, I used Qi Sense. Blue waves of qi, visible only to me, swept over the enemies charging forward with shrieks. Ding. Ding. Ding. > **System** > > - Level 12 > - Level 11 > - Level 12 “…Huh?” The reconnaissance squad members turned deathly pale. “What do we do?” “They’re coming! They’re coming!” “Squad Leadeeeer!” The enemies rapidly closed the distance—thirty meters, twenty meters… I opened my mouth. “Don’t worry. The enemy is nothing but simple EXP… I mean, a rabble. But!” “But?” “Stop them with everything you have. Just hold them back.” “What? What do you mean?” *What do I mean?* *Don’t get the last hit.* “Defensive formation. Form up!” Yep. All the EXP was mine. * * * “Squad Leader!” “No! Squad Leadeeeer!” “The squad leader went to commit suicide!” That wasn’t what I was doing, you lunatics. Leaving the reconnaissance squad members’ screams behind, I charged straight at the enemy. Internal energy surged from my dantian and coursed through my entire body. “You crazy bastard.” The enemy at the front grinned, baring yellow teeth. I grinned back. “Pretty boy.” “What?” Slash. The man clutched his throat and collapsed. As I passed him, the voice I had been waiting for rang out. Ding. > **System** > > - You gained EXP. > - You gained 50 Merit! “W-what?!” “How dare this fucking bastard…” The enemies were a magnificent bunch. Facial scars came standard, and their hygiene was so atrocious that the stench stabbed at my nose. And yet… “Ah, this is great.” I felt like I was in a flower garden. Twenty flowers filled with the sweet honey of EXP. I charged into them with a blissful expression and sucked out the honey. Stab. Stab. Stab. Ding. Ding. Ding. > **System** > > - You gained EXP. > - You gained 50 Merit… > - You gained EXP… > - You gained 50 Merit… I tore through their ranks without pause. Their front line collapsed in the blink of an eye, and the enemies instinctively began to falter. *That works for me.* The Jin Family’s Manoeuvre Technique and Spear Technique were martial arts built around advancing. I stepped forward with the Manoeuvre Technique, drove into their center, and swung my spear. “Gaaah!” “Aaaargh!” The spear was razor-sharp and massively heavy, and the technique was domineering to boot. On top of that, the enemies were steadily backing away. It was time for the Jin Family’s Spear Technique to show its true worth. *First form.* I began swinging my spear in step with my footwork. Every swing and thrust brought forth a scream and a burst of blood. “Ghk.” “Grrrgh.” Second form. Third form. Fourth form. At some point, I surrendered myself to the flow. The ripples became waves, and the enemies were swept away by them. Every nerve in my body stood on end. *More. More. More…* “You fucking bastard!” Stab. Stab-stab. Throat. Chest. Abdomen. I stabbed and slashed through them in turn. The System alerts confirmed each death for me. How much time had passed? Only one person remained standing. “Our boss will find you no matter what…” I didn’t wait. A wave is flow. And the final wave erupted from the tip of my spear. The final form of the Jin Family’s Spear Technique: *Sky-Piercing Strike*. Splurt! The last man—the one with the narrow, birdlike eyes—stared at the shattered pieces of his sword before dropping to his knees. The center of his chest had burst open as if struck by a cannonball. Ding. > **System** > > - You defeated **Level 32 Black Mountain Blade**! > - You completed the **Survivors** Quest! > - A Chain Quest has been created! > - You gain a large amount of EXP! > - You gain a large amount of Merit! > - You have leveled up! > - You have leveled up! > - You have leveled… As the System alerts continued without pause, I rubbed my stomach. “Buurp.” Ah, I’m stuffed. [^1]: A shichen is a traditional Chinese time period of roughly two hours.

## Korean source

```text
＃25화



“이곳은 저승인가?”

중년인이 깨어나자마자 한 말이었다.

내가 대답하기도 전에 조그마한 뭔가가 튀어나와 중년인의 품에 안겼다.

눈가에 눈물이 대롱대롱 매달린 꼬마가 외쳤다.

“공 숙부!”

“천아! 무사했구나. 그런데 이게 도대체……?”

혼란스러워하는 중년인에게 꼬마가 울음 섞인 목소리로 설명했다. 언덕 위에서 우리를 만났고, 내 손에 적들이 모두 죽었다는 말을 들은 중년인이 눈을 크게 떴다.

“본가의 인물이시오?”

“예. 맞습니다.”

“아, 하늘이 도왔구나!”

“…….”

내가 도운 거지, 이 양반아.

“난 분명히 산 밑으로 추락했는데…… 그걸로 끝이라고 생각했소.”

“거의 그럴 뻔했지요. 운이 좋았습니다.”

나는 손가락으로 능선 밑을 가리켰다. 적으로 추정되는 시체 두 구가 나무에 머리를 박고 누워 있었다.

그가 미끄러졌던 경로에 풀숲이 무성하지 않았다면, 그도 저 꼴이 났을 것이다.

‘나도 처음에는 몰랐지.’

중년인의 존재를 깨달은 건 퀘스트창 덕분이었다.

적들을 다 물리쳤는데도 [삭주 지부의 생존자] 퀘스트가 완료되지 않았던 것이다. 그건 생존자가 더 있다는 뜻이었다.

‘문제는 이 사람 말고도 생존자가 더 있냐는 건데…….’

일말의 불안감은 지친 중년인을 부축한 순간 간단히 해소됐다.

띠링.



- [생존자] 퀘스트를 완료했습니다!

- 연계 퀘스트가 생성되었습니다!

- 레벨이 올랐습니다!

- 레벨이 올랐습니다!

- 공적치와 명성이 상승합니다!



* * *



“후우.”

중년인이 호흡을 토해 냈다. 짧은 운기조식이었지만 최소한의 기력을 회복한 듯, 훨씬 나아진 모습이었다.

그는 자리에서 일어나 정중히 포권을 취했다.

“은인께서 모두를 살리셨습니다.”

“아닙니다. 마땅히 해야 할 일을 한 것뿐인데요.”

이제는 입만 열리면 거짓말이 술술 나온다. 한편으로는 틀린 말도 아니다. 어떻게든 퀘스트는 깨야 했으니까.

‘오히려 내가 고맙다고 절을 해야 할 판이지.’

하지만 이런 내 태도에 산타클로스, 아니 생존자들은 적잖이 감격한 모양이었다.

“뛰어난 무공에 의협심까지. 이 공야청, 진심으로 탄복했소.”

“소천과 소율이 대협께 큰 은혜를 입었습니다.”

덕분에 이름을 알았다. 중년인은 공야청, 어린 남매는 소천과 소율이다.

“실례가 안 된다면 은인의 성함을 여쭈어도 되겠소?”

“제 이름은…….”

그때, 문득 한 가지 생각이 뇌리를 스쳤다.

‘이거, 내 이름 들으면 칼 들고 달려드는 거 아냐?’

어떤 음모가 있었건 간에 이 전쟁의 도화선에 불을 붙인 건 다름 아닌 이 몸, 진태경이다. 터전과 가족을 잃은 두 사람이 내게 좋은 감정이 있을 것 같지 않았다.

그래, 선의의 거짓말이 필요한 시점이다.

“홍길동. 저는 홍길동이라고 합니다.”

“홍길동…… 처음 듣는 이름이오. 그러나 영웅의 풍모가 느껴지는구려.”

소천이 옆에서 거들었다.

“동에 번쩍 서에 번쩍. 신출귀몰할 것 같은 이름입니다.”

……저 녀석이 어떻게 알았지?

나는 호부호형 얘기가 나오기 전에 서둘러 화제를 돌렸다.

“그보다, 어떻게 된 일입니까?”

두 사람의 얼굴에 그림자가 짙게 내려앉았다.

말문을 연 것은 공야청이었다.

“불과 며칠 전의 일이었소.”

전쟁을 알리는 전서구가 도착했을 때는 이미 삭주 지부가 물 샐 틈 없이 포위된 상태였다. 항산검문이 고용한 낭인들이 사람들을 도륙하고, 건물을 불태웠다고 했다.

“그 숫자가 물경 일백에 달했소. 지부장과 휘하 무사들이 시간을 벌어 준 덕분에 비밀 통로로 빠져나올 수 있었지요. 탈출한 이들 대부분이 무공을 모르는 여인과 아이들이었소.”

다른 이들이 어떻게 되었는지는 물어보지 않아도 알 수 있었다.

내가 갖고 있는 시스템은 절대적이며 사실적이다. 퀘스트창이 알려 준 삭주 지부의 생존자는 세 사람이 전부였다.

“적들에 관해 알고 싶습니다.”

“낭인들이오.”

“낭인?”

“은인도 알다시피, 돈이라면 뭐든 하는 놈들이지. 그중에서도 특히 악질인 놈들이 항산검문의 의뢰를 받아 우리를 습격했소.”

“악질치고는 약하던데요.”

“악하고 선함에 강자와 약자가 따로 있겠소? 이번에 고용한 놈들은 널리고 널린 수준의 낭인이오. 다만 우두머리가 문제였지.”

공야청이 이를 악물었다.

“일문일살 조필. 그놈이었소. 지부장께서는 놈을 보자마자 패배를 직감하고 내게 식솔들을 부탁하셨지.”

소천의 작은 주먹이 부르르 떨렸다.

“제 손으로 직접 사지를 찢어 죽일 겁니다.”

꼬맹이치고는 남다른 어휘 선택이었지만, 뼈에 사무친 원한을 생각하면 당연하게 생각되었다.

나는 소천의 머리를 쓰다듬어 주었다.

“꼭 그렇게 될 것이다. 내 도와주마.”

“정말이십니까?”

“남아일언중천금. 내 한 입으로 두말할 것 같으냐? 내 반드시 그놈을 잡아 레벨 업을…….”

“예?”

“아니, 놈을 죽여 원한을 갚아 주마.”

“아아, 감사합니다. 정말 감사합니다. 홍 대협!”

“고맙소. 정말로 고맙소!”

두 사람은 연신 감사를 표했다. 아, 뭔가 되게 야비한 놈이 된 기분이라 가슴 한구석이 심하게 찔려 온다.

‘아니지. 저쪽은 원수가 죽어서 좋고, 나는 레벨 업 해서 좋고. 상부상조지. 상부상조.’

애써 자기합리화를 시키며 물었다.

“머릿수가 얼마나 됩니까?”

“적들의 위치를 파악하는 도중에 놈들이 하는 이야기를 들었소. 조필을 포함해 서른 남짓이라고 하더군.”

“서른? 삼십 명이요?”

“그렇소. 그러니 어서 피해야…….”

공야청의 목소리가 멀어진다. 그 대신 저 멀리서 희미한 소리가 가까워졌다. 띠링. 띠링. 띠링.

들린다. 레벨 업 하는 소리가. 로그아웃하는 소리가!

나는 자꾸만 치솟는 입꼬리를 억누르며 말했다.

“여기서 나머지 놈들을 기다립시다.”

“기다린다니. 그게 무슨 말이오?”

“일망타진! 그런 악독한 놈들을 살려 둘 수 없습니다!”

“아니, 홍 대협. 내 말을 좀…….”

“은인 같은 고수라면 할 수 있습니다! 감사합니다. 은인!”

소천이 눈물을 글썽이며 내 품에 달려들었다. 나는 두 팔 벌려 녀석을 끌어안았다.

“그래. 놈들을 다 죽이자!”

“죽이자!”

“조필 개새끼!”

“개새끼!”

그때 공야청이 입을 열었다.

“조필은 절정 고수요.”

“조필 씹새…… 예?”

“일문일살 조필. 산서성을 통틀어도 몇 안 되는 절정 고수란 말이오. 놈이 온갖 은원에 얽혀 있으면서도 지금까지 살아남을 수 있었던 이유가 무엇이겠소?”

“설마…….”

“그에게 덤비는 자는 다 죽었소. 조필은 그런 자요. 잔혹하고, 그만큼 강하지.”

“아.

뭔가 이상함을 감지한 어린 눈동자가 나를 올려다본다.

“소천아.”

“예. 대협.”

“생각해 보니 지금은 때가 아닌 것 같다.”

“예?”

“내가 어리석었다. 우선 너희 남매를 본가로 생환시키는 게 최우선인데. 그렇지?”

“…….”

“실은 아까 싸우다가 부상을 입기도 했고, 내 부하들도 많이 지쳐서 힘든 싸움이 될 듯싶다.”

소천의 눈동자가 내 위아래를 훑었다. 적들의 피로 흠뻑 젖어 있긴 했지만 찢어진 곳 하나 없이 멀쩡한 옷이다. 상처가 있을 리 만무했다.

“내상을 입었단다.”

“…….”

이번에는 고개를 돌려 정찰조원들을 바라봤다. 칼 한 번 안 휘두르고 전투가 끝난 바람에 쌩쌩하다 못해 펄펄 날아다닌다.

“보이는 게 다가 아니지.”

“……대협.”

슬그머니 소천을 떼어 내고 외쳤다.

“본가로 돌아간다. 모두 출발 준비해!”

잽싸게 조원들에게 돌아가려는데, 소천의 손이 옷깃을 꽉 붙잡고 놔주질 않는다. 동그란 눈에는 눈물이 글썽하다.

“대협.”

“야, 빨리빨리 안 움직여! 소천아, 내가 지금 좀 바빠서 그런데 이따 이야기하자. 알았지?”

“홍 대혀엽.”

“공야청 아저씨. 아니, 공 대협은 뭐 하세요. 한시가 급한데.”

“……소천아, 이리 오거라.”

공야청이 나를 병신 보듯이 바라보며 소천을 떼어 냈다. 저건 마치 범죄자의 접근을 차단하는 보호자의 손길.

소천이 거의 통곡했다.

“홍길동 대혀업!”

그리고 그 말이 신호탄이었다.

쾅! 굉음과 함께 오두막의 문이 박살 나며 한 사람이 나타났다.



[Lv.22 혁무진]



“진태경 이 씨발 새끼야아아!”

쒸익쒸익. 혁무진의 분노에 찬 눈동자가 정확히 나를 향하고 있었다. 공야청과 소천이 멍한 얼굴로 나를 바라봤다.

“홍 대협?”

“홍길동 대협?”

“아. 그게. 그러니까.”

……에이, 시발.



* * *



“흠.”

조필은 물끄러미 시체를 내려다보았다. 일그러진 표정에 부릅뜬 눈. 피와 눈으로 얼어붙은 그는 흑산도라는 별호로 불렸었다.

“쯧쯧. 이 친구, 어쩌다 이렇게 되었나.”

제법 충성심이 깊고 똘똘한 놈이었는데, 이렇게 허망하게 갈 줄은 몰랐다.

“그러게, 내가 누누이 말하지 않았나. 두 눈 크게 뜨고 다니라고.”

조필은 흑산도의 부릅뜬 눈을 잡고 벌렸다.

얼어붙은 살이 찢어지며 끔찍한 소리가 새어 나온다.

찌직. 찌지직.

다른 이들은 숨도 못 쉬고 그 모습을 지켜봤다.

평소와 다름없는 표정과 말투였지만 그들은 조필이 분노했다는 사실을 온몸으로 느끼고 있었다.

절정 고수가 뿜어내는 살기에 숨이 막히고 식은땀이 흘렀다.

‘그럴 만도 하지.’

이십여 명이 전멸했다. 그것도 고작 삭주 지부의 잔당이나 처리하는 임무에.

일문일살. 마음에 드는 적을 만나면 꼭 한 가지 질문을 하고 죽인다는 괴악한 성격의 조필이다.

낭인들은 흑산도가 죽어서 다행이라고 생각했다. 살아 있었다면 한층 더 끔찍한 일을 겪었을 테니까.

“이제 좀 낫구먼.”

조필이 바지춤에 피를 닦아 내며 일어났다.

“그래, 다들 어떻게 생각하나? 가감 없이 말해 보게.”

“당연히 명령대로 움직여야지.”

한 사람이 나섰다. 단정한 복장과 점잖은 태도의 중년인, 그리고 그 뒤로 시립한 십여 명의 무사들은 항산검문이 낭인들을 통제하기 위해 보낸 감시자이자 길잡이였다.

조필이 빙긋 웃었다.

“아, 그래. 우리 대항산검문의 당주님을 잊고 있었구려. 그런데 명령이라니?”

“삭주 지부를 지우고 본대와 합류하라. 소문주의 명령을 벌써 잊은 건가?”

“명령이라, 의뢰를 받은 기억은 있소만.”

“그게 그거 아닌가!”

중년인이 불쾌한 얼굴로 조필을 응시했다.

“애초에 여기까지 온 것부터가 그대의 독단이었지. 한데 그 결과가 어떤가? 일개 지부 잔당 따위한테 스물이 넘는 수하들을 잃지 않았나!”

“그러니까 쫓아야지. 반나절이면 놈들을 끝장낼 수 있소.”

“정양까지는 모르나, 혼주까지 쫓는다면 역공당할 우려가 있지. 이 이상의 독단은 내가 허락하지 않겠다.”

“허락이라, 허락…….”

곰곰이 생각에 잠겨 있던 조필이 입을 열었다.

“안 되겠어. 마음에 안 드는군.”

“그게 뭐……!”

퍼걱. 목뼈가 으스러진 그는 말을 끝마치지 못하고 절명했다. 빛살 같은 속도로 중년인의 목을 꺾은 조필이 입술을 핥았다.

“나는 전쟁이 좋아. 누가 죽어도 잊히거든.”

“이노옴!”

상황을 파악한 항산검문의 무사들이 병장기를 빼 들었지만, 조필은 이미 그들 사이로 파고든 뒤였다.

퍼걱, 촤악!

눈밭 위로 더운 피가 쏟아졌다. 조필이 맹수처럼 날뛸 때마다 누군가의 목이, 팔이, 다리가 뜯겨 훨훨 날았다.

“끄아아…….”

이름 모를 무사의 신음이 마지막이다.

시체 더미 위, 짓눌린 침묵 속에서 조필이 말했다.

“놈들을 추격한다.”

이번에는 아무도 입을 열지 않았다. 도망치듯 준비를 서두르는 수하들의 모습을 뒤로하고, 조필은 시신들을 바라봤다.

‘어떤 놈일까.’

그는 절정 고수다. 시신들의 몸에 남은 상흔과 족적을 통해 상대의 모습을 그려 낼 수 있었다.

단 한 사람. 뛰어난 실력의 창수(槍手)가 이 자리에 있었다. 다른 이십여 명을 도륙한 것도 바로 그자다.

‘흑산도를 일격에 죽인 놈이니 오죽할까.’

특히 가슴을 관통한 마지막 일격은…… 조필이 흥미를 갖기에 충분했다.

‘재미있는 싸움이 되겠어.’

누구일까. 태원진가의 고수? 아니면 알려지지 않은 누군가?

아무래도 상관없다. 조필은 기분 좋은 웃음을 터트렸다.

“조만간 만나자고. 친구.”



* * *



“들어온 소식은?”

“없습니다. 그저 최대한 빨리 이동하는 수밖에는…….”

“젠장, 젠장!”

위팽은 분통을 터트렸다. 하지만 방법이 없었다. 수하의 말처럼 최대한 빨리 삼공자를 찾아 보호하는 수밖에는.

‘일문일살 조필…….’

놈의 악명은 익히 들어서 알고 있다. 만일 삼공자가 놈의 손에 들어간다면 결과는 죽음뿐이다.

‘그렇게 되면 주군을 볼 면목이 없다.’

진위경은 초인적인 인내심으로 참아 냈다.

그는 현재 태원진가의 머리이자 중심에 있다. 누구보다 사랑하는 동생과 수백의 식솔을 저울에 올려놨고, 장고 끝에 가장 믿는 수하인 위팽을 동생에게 보냈다.

그런데 만약 실패한다면…….

‘주군을 볼 면목이 없어.’

고삐를 잡은 손에 힘이 들어간다. 위팽은 박차를 가했다. 그의 뒤로 이십여 기의 기마가 꼬리를 물고 달렸다.
```

## Current accepted English baseline

```markdown
# Chapter 25

“Is this the afterlife?”

That was the first thing the middle-aged man said when he woke up.

Before I could answer, something small sprang forward and threw itself into his arms.

The child, tears dangling from the corners of his eyes, shouted.

“Uncle Gong!”

“Socheon! You’re safe. But what in the world…?”

The confused middle-aged man listened as the child explained through sobs. When he heard that we had met on the hill and that all the enemies had died by my hand, his eyes widened.

“Are you from the main family?”

“Yes. That’s right.”

“Ah, Heaven has helped us!”

“…”

*I helped you, you old man.*

“I was sure I’d fallen to the bottom of the mountain… I thought that was the end of me.”

“You nearly did. You were lucky.”

I pointed below the ridge. Two corpses presumed to belong to the enemy lay with their heads buried in trees.

If the grass along the path where he had slipped had not been so thick, he would have ended up just like them.

*I didn’t realize it at first, either.*

I only became aware of the middle-aged man’s presence thanks to the Quest window.

Even after I defeated all the enemies, the **Survivors of the Sakju Branch** Quest had not been completed. That meant there were more survivors.

*The question was whether there were any survivors besides this man…*

The last trace of unease vanished the moment I helped the exhausted middle-aged man to his feet.

Ding.

> **System**
>
- You completed the **Survivors of the Sakju Branch** Quest!
> - A Chain Quest has been created!
> - You leveled up!
> - You leveled up!
> - Merit and Fame increase!

* * *

“Whew.”

The middle-aged man exhaled. Though he had only circulated his qi briefly, his complexion had improved noticeably.

He rose and respectfully clasped his hands in a salute.

“Benefactor, you saved everyone.”

“Not at all. I only did what anyone should have done.”

Every time I opened my mouth, lies came spilling out. It wasn’t entirely wrong, either. I had to clear the Quest somehow.

*If anything, I’m the one who should be bowing to them and thanking them.*

Still, Santa Claus—or rather, the survivors—seemed deeply moved by my attitude.

“Outstanding martial arts and a sense of chivalry, too. I, Gong Yacheong, sincerely admire you.”

“Socheon and Soyul owe Great Hero an enormous debt of gratitude.”

Thanks to that, I learned their names. The middle-aged man was Gong Yacheong, and the young siblings were Socheon and Soyul.

“If it isn’t too impertinent, may I ask our Benefactor’s name?”

“My name is…”

Then I had a thought.

*Wait. If I tell them my name, won’t they come running at me with swords?*

Whatever conspiracy had been involved, the person who had lit the fuse on this war was none other than me, Jin Taekyung. It was hard to believe that two people who had lost their home and family would look kindly on me.

*Yes. This is the moment for a well-intentioned lie.*

“Hong Gil-dong. My name is Hong Gil-dong.”[^1]

“Hong Gil-dong… I’ve never heard that name before. But I can feel the bearing of a hero.”

Socheon chimed in from the side.

“Here one moment, there the next. It sounds like the name of someone who appears and disappears like a ghost.”

*…How did that kid know?*

Before he could bring up the tale’s business about calling one’s father Father and one’s elder brother Brother,[^2] I hurriedly changed the subject.

“More importantly, what happened?”

Dark shadows fell across both their faces.

Gong Yacheong spoke first.

“It happened only a few days ago.”

By the time the carrier pigeon bearing word of war arrived, the Sakju Branch had already been surrounded so tightly that not even a drop of water could get through. The wandering martial artists hired by the Mount Heng Sword Sect had slaughtered people and burned down the buildings.

“There must have been a full hundred of them. Thanks to the Branch Leader and the martial artists under him buying us time, we were able to escape through a secret passage. Most of those who escaped were women and children who knew no martial arts.”

I didn’t need to ask what had happened to the others.

The System was absolute and factual. Those three were all the survivors of the Sakju Branch identified by the Quest Window.

“I want to know about the enemy.”

“They’re wandering martial artists.”

“Wandering martial artists?”

“As you know, they’re bastards who’ll do anything for money. The especially vile ones among them were hired by the Mount Heng Sword Sect to attack us.”

“They seemed pretty weak for such vile bastards.”

“Do good and evil determine who is strong and who is weak? The ones they hired this time were ordinary wandering martial artists, common as dirt. The leader was the problem.”

Gong Yacheong gritted his teeth.

“Jopil, One Question, One Kill. That was the man. The Branch Leader sensed defeat the moment he saw him and entrusted his family members to me.”

Socheon’s small fists trembled.

“I’ll tear him limb from limb and kill him with my own hands.”

That was an unusual choice of words for a child, but considering the grudge carved into his bones, it was understandable.

I gently patted Socheon on the head.

“That is exactly what will happen. I’ll help you.”

“Really?”

“A man’s word is worth a thousand pieces of gold. Do you think I’d say one thing and do another? I’ll definitely catch that bastard and level u—”

“Huh?”

“No, I mean I’ll kill him and avenge your grudge.”

“Ah… Thank you. Thank you so much, Great Hero Hong!”

“Thank you. Truly, thank you!”

The two of them repeatedly expressed their gratitude. I felt like a real scumbag, and a sharp stab tore through one corner of my chest.

*No. They’ll be happy when their enemy dies, and I’ll be happy when I level up. It’s mutually beneficial. Mutually beneficial.*

I forced myself to accept that justification and asked,

“How many of them are there?”

“While we were trying to determine the enemies’ position, I overheard them talking. They said there were about thirty, including Jopil.”

“Thirty? Thirty men?”

“That’s right. So we need to flee at once…”

Gong Yacheong’s voice began to fade. In its place, a faint sound from far away drew closer.

Ding. Ding. Ding.

I could hear it. The sound of leveling up. The sound of logging out!

Suppressing the corners of my mouth as they kept creeping upward, I said,

“Let’s wait here for the rest of them.”

“Wait? What do you mean?”

“Wipe them all out! We can’t let such vile bastards live!”

“No, Great Hero Hong, listen to me…”

“A master like you can do it! Thank you, Benefactor!”

Socheon came running into my arms with tears in his eyes. I opened both arms and pulled him into a hug.

“That’s right. Let’s kill them all!”

“Let’s kill them!”

“Jopil, you son of a bitch!”

“Son of a bitch!”

That was when Gong Yacheong spoke.

“Jopil is a Peak master.”

“Jopil is a fucking bast—huh?”

“Jopil, One Question, One Kill. He’s one of the few Peak masters in all of Shanxi. What do you think is the reason he has survived until now, despite being tangled up in all kinds of grudges and vendettas?”

“Don’t tell me…”

“Everyone who challenged him died. That’s the kind of man Jopil is. Cruel—and every bit as strong.”

“Ah.”

Sensing that something was wrong, Socheon looked up at me.

“Socheon.”

“Yes, Great Hero.”

“Now that I think about it, this probably isn’t the right time.”

“Huh?”

“I was being foolish. The priority should be getting you and your sister safely back to our family. Right?”

“…”

“I was injured during the fight earlier, too, and my men are exhausted. It looks like it would be a difficult battle.”

Socheon looked me up and down. My clothes were soaked in the enemies’ blood, but they were perfectly intact, without a single tear. There was no way I could have been injured.

“I have an internal injury.”

“…”

He turned to the reconnaissance squad. They had not even swung their swords once, and they were bursting with energy.

“What you see isn’t everything.”

“…Great Hero.”

I slipped Socheon off me and shouted,

“We’re returning to the main family. Everyone, prepare to leave!”

I hurried back toward the squad, but Socheon’s hand clutched my collar tightly and refused to let go. Tears glimmered in his round eyes.

“Great Hero.”

“Hey, why aren’t you moving? Move, move! Socheon, I’m a little busy right now, so let’s talk later. Okay?”

“Great Heeero.”

“Mister Gong Yacheong. No, Great Hero Gong, what are you doing? Every second counts.”

“…Socheon, come here.”

Gong Yacheong looked at me as if I were an idiot and pulled Socheon away. His hand came between me and Socheon like a guardian blocking a criminal.

Socheon almost wailed.

“Great Hero Hong Gil-dooong!”

And that was the starting gun.

With a thunderous boom, the cabin door was smashed apart, and someone burst in.

> **System**
>
> - **Level 22 Hyuk Mujin**

“Jin Taekyung, you fucking bastard!”

Hyuk Mujin huffed and puffed, his furious eyes locked on me. Gong Yacheong and Socheon stared at me with blank expressions.

“Great Hero Hong?”

“Great Hero Hong Gil-dong?”

“Ah. Well, you see…”

*…Fuck.*

[^1]: Hong Gil-dong is a legendary Korean outlaw and folk hero.

[^2]: In the Hong Gil-dong tale, he demands the right to address his father as “Father” and his elder brother as “Brother.”

* * *

“Hmm.”

Jopil stared down at the corpse. The face was twisted, its eyes wide open. Frozen beneath blood and snow, the man had been known by the nickname Black Mountain Blade.

“Tsk, tsk. How did you end up like this, friend?”

He had been loyal and clever. Jopil had never imagined he would die so pointlessly.

“See? Haven’t I always told you to walk around with both eyes wide open?”

Jopil grabbed Black Mountain Blade’s bulging eyes and pried them farther open.

A horrible sound escaped as the frozen flesh tore.

Rip. Riiip.

The others watched without even daring to breathe.

His expression and tone were no different from usual, but they could feel to their bones that Jopil was furious.

The killing intent radiating from a Peak master made it hard to breathe, and cold sweat trickled down their backs.

*It was understandable.*

More than twenty men had been wiped out. And all on a mission to deal with the remnants of the Sakju Branch.

Jopil, One Question, One Kill, was a bizarre man. Whenever he encountered an enemy he liked, he asked exactly one question before killing them.

The wandering martial artists thought it was fortunate that Black Mountain Blade was dead. If he had still been alive, they would have suffered something even more horrifying.

“That’s better.”

Jopil wiped the blood on his trousers and rose.

“Well, what does everyone think? Tell me without holding back.”

“We should obviously follow the order.”

One man stepped forward. The neatly dressed, dignified middle-aged man and the ten-odd martial artists standing at attention behind him were the overseers and guides the Mount Heng Sword Sect had sent to keep the wandering martial artists under control.

Jopil smiled faintly.

“Ah, yes. I’d forgotten our Mount Heng Sword Sect Hall Master was here. But what’s this about an order?”

“Wipe out the Sakju Branch and join the main force. Have you already forgotten the Young Sect Leader’s order?”

“An order? I remember accepting a commission.”

“Isn’t that the same thing?”

The middle-aged man glared at Jopil, displeased.

“Coming here in the first place was your own arbitrary decision. And what came of it? You lost more than twenty subordinates to the remnants of a single branch!”

“Then we should pursue them. We can finish them off in half a day.”

“Jeongyang might be another matter, but if you pursue them as far as Honju, we risk a counterattack. I won’t permit any more unilateral decisions.”

“Permission. Permission…”

After mulling it over, Jopil spoke.

“No. That won’t do. I don’t like it.”

“What do you mea—”

Crunch.

The middle-aged man’s neck shattered, and he died before he could finish speaking. Jopil had twisted it at blinding speed. He licked his lips.

“I like war. No matter who dies, people forget.”

“You bastard!”

The Mount Heng Sword Sect’s martial artists realized what had happened and drew their weapons, but Jopil had already plunged into their midst.

Crunch. Slash!

Warm blood poured onto the snowfield. Every time Jopil rampaged like a wild beast, someone’s neck, arm, or leg was torn free and sent flying.

“Gaaah…”

The groan of an unnamed martial artist was the last sound.

Standing atop the heap of corpses, Jopil spoke into the crushing silence.

“We’re pursuing them.”

This time, no one said a word. As his subordinates hurried to prepare as though fleeing for their lives, Jopil continued to stare at the bodies.

*What kind of man was it?*

Jopil was a Peak master. From the scars on the corpses and the footprints, he could picture what his opponent looked like.

*Only one man.*

A highly skilled spearman had been here. He was the one who had slaughtered the other twenty-plus men.

*If he killed Black Mountain Blade in one strike, he must be something else.*

The final strike that pierced through Black Mountain Blade’s chest had been particularly interesting.

*This should be a fun fight.*

Who was he? A master from the Jin Family of Taiyuan? Or someone unknown?

It didn’t matter. Jopil let out a pleased laugh.

“Let’s meet soon, friend.”

* * *

“What news have we received?”

“None, sir. All we can do is move as quickly as possible…”

“Damn it! Damn it!”

Wipeng was furious. But there was nothing he could do. As his subordinate had said, the only thing they could do was find the Third Young Master and protect him.

*Jopil, One Question, One Kill…*

Wipeng knew the man’s reputation well. If the Third Young Master fell into his hands, death would be the only possible outcome.

*If that happens, I won’t be able to face my lord.*

Jin Wikyung endured with superhuman patience.

He was currently at the head of the Jin Family of Taiyuan, its central pillar. He had placed his beloved younger brother and hundreds of family members on the scales, and after much deliberation, he had sent his most trusted subordinate, Wipeng, to his brother.

*But if I fail…*

*I won’t be able to face my lord.*

Wipeng’s grip tightened on the reins. He spurred his horse onward. More than twenty mounted riders followed in a long line behind him.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 25`.

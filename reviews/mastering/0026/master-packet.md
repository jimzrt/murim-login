# Master Edit Task — Chapter 26

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
| 혁무진    | **Hyuk Mujin**     |
| 조필     | **Jopil**          |
| 항산검문   | **Mount Heng Sword Sect**        |
| 삼류     | **Third Rate**    |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 낭인     | **wandering martial artist**                     |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 로그아웃             | **Logout**                     |
| 지능               | **Intelligence**               |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 공야청 | **Gong Yacheong** |
| 소천 | **Socheon** |
| 소율 | **Soyul** |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |

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

#### Chapter 24 tail (verified mastered)

…
> - Sudden Quest has been created! > > **Quest** > > **Survivors of the Sakju Branch** > > You have encountered survivors from the Sakju Branch of the Jin Family of Taiyuan. > > Rescue the survivors from the Mount Heng Sword Sect’s merciless pursuers! > > **Grade:** Sudden Quest > **Limit:** Jin Taekyung > **Task:** Rescue the survivors — Incomplete > **Reward:** Chain Quest > ??? > **Failure:** ??? “…” “…” We looked at them. They looked at us. A deathly silence settled over the frozen clearing. *I knew it. I knew this was how it would turn out.* But it was too late for regrets. What could I do about my cursed luck? I let out a deep sigh and shouted. “Attack formation. Form up!” Clack-clack-clack. Despite being caught off guard, the squad members moved as they had been taught. By the time they had formed up, the enemy had realized who we were and started shouting. “They’re brats from the Jin Family of Taiyuan!” “There aren’t many of them! Wipe them out!” *Brats. Outnumbered.* They’d pinpointed the two facts that tore at my chest. I hadn’t even finished teaching these guys. Their martial arts were weak, they had no real combat experience, and they were complete rookies. *If things go bad, should I bolt by myself?* Feeling utterly hopeless, I used Qi Sense. Blue waves of qi, visible only to me, swept over the enemies charging forward with shrieks. Ding. Ding. Ding. > **System** > > - Level 12 > - Level 11 > - Level 12 “…Huh?” The reconnaissance squad members turned deathly pale. “What do we do?” “They’re coming! They’re coming!” “Squad Leadeeeer!” The enemies rapidly closed the distance—thirty meters, twenty meters… I opened my mouth. “Don’t worry. The enemy is nothing but simple EXP… I mean, a rabble. But!” “But?” “Stop them with everything you have. Just hold them back.” “What? What do you mean?” *What do I mean?* *Don’t get the last hit.* “Defensive formation. Form up!” Yep. All the EXP was mine. * * * “Squad Leader!” “No! Squad Leadeeeer!” “The squad leader went to commit suicide!” That wasn’t what I was doing, you lunatics. Leaving the reconnaissance squad members’ screams behind, I charged straight at the enemy. Internal energy surged from my dantian and coursed through my entire body. “You crazy bastard.” The enemy at the front grinned, baring yellow teeth. I grinned back. “Pretty boy.” “What?” Slash. The man clutched his throat and collapsed. As I passed him, the voice I had been waiting for rang out. Ding. > **System** > > - You gained EXP. > - You gained 50 Merit! “W-what?!” “How dare this fucking bastard…” The enemies were a magnificent bunch. Facial scars came standard, and their hygiene was so atrocious that the stench stabbed at my nose. And yet… “Ah, this is great.” I felt like I was in a flower garden. Twenty flowers filled with the sweet honey of EXP. I charged into them with a blissful expression and sucked out the honey. Stab. Stab. Stab. Ding. Ding. Ding. > **System** > > - You gained EXP. > - You gained 50 Merit… > - You gained EXP… > - You gained 50 Merit… I tore through their ranks without pause. Their front line collapsed in the blink of an eye, and the enemies instinctively began to falter. *That works for me.* The Jin Family’s Manoeuvre Technique and Spear Technique were martial arts built around advancing. I stepped forward with the Manoeuvre Technique, drove into their center, and swung my spear. “Gaaah!” “Aaaargh!” The spear was razor-sharp and massively heavy, and the technique was domineering to boot. On top of that, the enemies were steadily backing away. It was time for the Jin Family’s Spear Technique to show its true worth. *First form.* I began swinging my spear in step with my footwork. Every swing and thrust brought forth a scream and a burst of blood. “Ghk.” “Grrrgh.” Second form. Third form. Fourth form. At some point, I surrendered myself to the flow. The ripples became waves, and the enemies were swept away by them. Every nerve in my body stood on end. *More. More. More…* “You fucking bastard!” Stab. Stab-stab. Throat. Chest. Abdomen. I stabbed and slashed through them in turn. The System alerts confirmed each death for me. How much time had passed? Only one person remained standing. “Our boss will find you no matter what…” I didn’t wait. A wave is flow. And the final wave erupted from the tip of my spear. The final form of the Jin Family’s Spear Technique: *Sky-Piercing Strike*. Splurt! The last man—the one with the narrow, birdlike eyes—stared at the shattered pieces of his sword before dropping to his knees. The center of his chest had burst open as if struck by a cannonball. Ding. > **System** > > - You defeated **Level 32 Black Mountain Blade**! > - You completed the **Survivors** Quest! > - A Chain Quest has been created! > - You gain a large amount of EXP! > - You gain a large amount of Merit! > - You have leveled up! > - You have leveled up! > - You have leveled… As the System alerts continued without pause, I rubbed my stomach. “Buurp.” Ah, I’m stuffed. [^1]: A shichen is a traditional Chinese time period of roughly two hours.

#### Chapter 25 tail (verified mastered)

…
down at the corpse. The face was twisted, its eyes wide open. Frozen beneath blood and snow, the man had been known by the nickname Black Mountain Blade. “Tsk, tsk. How did you end up like this, friend?” He had been loyal and clever. Jopil had never imagined he would die so pointlessly. “See? Haven’t I told you time and again to walk around with both eyes wide open?” Jopil grabbed Black Mountain Blade’s wide-open eyes and pried them even farther open. A horrible sound escaped as the frozen flesh tore. Rip. Riiip. The others watched without even daring to breathe. His expression and tone were no different from usual, but they could feel to their bones that Jopil was furious. The killing intent pouring from the Peak master choked the breath from their throats and sent cold sweat trickling down their backs. *No wonder.* More than twenty men had been wiped out. And all on a mission to deal with the remnants of the Sakju Branch. One Question, One Kill. Jopil was a bizarre man who always asked an enemy he liked exactly one question before killing them. The wandering martial artists considered Black Mountain Blade lucky to be dead. Had he survived, he would have suffered something far more horrifying. “That’s better.” Jopil wiped the blood on the waist of his trousers and rose. “Well, what does everyone think? Tell me without holding back.” “We should obviously follow the order.” One man stepped forward. The neatly dressed, dignified middle-aged man and the ten-odd martial artists standing at attention behind him were the overseers and guides the Mount Heng Sword Sect had sent to keep the wandering martial artists under control. Jopil smiled faintly. “Ah, yes. I’d forgotten our great Mount Heng Sword Sect Hall Master was here. But what’s this about an order?” “Wipe out the Sakju Branch and join the main force. Have you already forgotten the Young Sect Leader’s order?” “An order? I remember accepting a commission.” “Isn’t that the same thing?” The middle-aged man glared at Jopil, displeased. “Coming this far was your own unilateral decision in the first place. And what came of it? You lost more than twenty subordinates to the remnants of a single branch!” “Which is why we should pursue them. We can finish them off in half a day.” “Jeongyang might be another matter, but if you pursue them as far as Honju, we risk a counterattack. I won’t permit any more unilateral decisions.” “Permission. Permission…” Jopil mulled the word over, then spoke. “No. That won’t do. I don’t like it.” “What do you mea—” Crunch. The middle-aged man’s neck shattered, and he died before he could finish speaking. Jopil had twisted it at blinding speed. He licked his lips. “I like war. No matter who dies, they’re forgotten.” “You bastard!” The Mount Heng Sword Sect’s martial artists realized what had happened and drew their weapons, but Jopil had already plunged into their midst. Crunch! Slash! Warm blood poured onto the snowfield. Every time Jopil rampaged like a wild beast, someone’s neck, arm, or leg was torn free and sent flying. “Gaaah…” An unnamed martial artist’s groan was the last sound. Standing atop the heap of corpses, Jopil spoke into the crushing silence. “We’re pursuing them.” This time, no one said a word. As his subordinates hurried to prepare as though fleeing for their lives, Jopil continued to stare at the bodies. *What kind of man was he?* Jopil was a Peak master. From the scars on the corpses and the footprints, he could picture what his opponent looked like. A single man. A highly skilled spearman had been here, and he was the one who had slaughtered the other twenty-odd men. *He killed Black Mountain Blade in one strike. How could he be anything less?* The final strike that pierced through Black Mountain Blade’s chest had been particularly interesting. *This should be a fun fight.* Who was he? A master of the Jin Family of Taiyuan? Or someone unknown? It didn’t matter. Jopil let out a pleased laugh. “Let’s meet soon, friend.” * * * “What news has come in?” “None, sir. All we can do is move as quickly as possible…” “Damn it! Damn it!” Wipeng seethed with frustration, but there was nothing else he could do. As his subordinate had said, their only option was to find the Third Young Master as quickly as possible and protect him. *Jopil, One Question, One Kill…* Wipeng knew the man’s reputation well. If the Third Young Master fell into his hands, death would be the only possible outcome. *If that happens, I won’t be able to face my lord.* Jin Wikyung endured with superhuman patience. He was currently the head and center of the Jin Family of Taiyuan. He had placed the younger brother he loved more than anyone and hundreds of family members on the scales, and after much deliberation, he had sent his most trusted subordinate, Wipeng, to his brother. *But if I fail…* *I won’t be able to face my lord.* Wipeng’s grip tightened on the reins. He spurred his horse onward. More than twenty mounted riders followed in a long line behind him. [^1]: Hong Gil-dong is a legendary Korean outlaw and folk hero. [^2]: In the Hong Gil-dong tale, he demands the right to address his father as “Father” and his elder brother as “Brother.”

## Korean source

```text
＃26화



“그러니까……”

공야청이 묘한 눈빛으로 나를 바라봤다.

“바로 그 진태경 공자셨구려.”

결국 이 순간이 오고야 말았다. 나는 세 번째로 기절한 혁무진의 멱살을 놓고 어색하게 웃어 보였다.

“예, 제가 바로 그 진태경입니다.”

야영 준비를 하고 있던 순찰조원들의 귀가 쫑긋거린다. 지금 우리는 가문으로 복귀하는 길이다.

전투가 벌어진 오두막으로부터 다섯 시간을 넘게 쉬지 않고 말을 달렸다. 이동하는 내내 입을 다물고 있던 공야청이 이제야 처음으로 입을 연 것이다.

‘저 새끼만 아니었어도.’

나는 눈치 빠른 순찰조원에 의해 질질 끌려가는 혁무진을 노려보았다. 한 대만 더 때리고 놔줄걸.

아쉬워하는 내게 공야청이 말했다.

“공자의 소문은 익히 들었소.”

“……그러시군요.”

“세 살배기 어린아이도 공자를 알 거요. 아마 본가 최고의 유명 인사겠지.”

이쯤 되면 모르는 사람을 찾는 게 빠르지 않을까 싶다.

“천성이 게으르고 오만방자하다. 주색에 빠져 무공도 익히지 않는다…… 하지만 역시 강호의 소문은 믿을 게 못 되는구려. 오늘 공자가 보여 준 무위는 실로 대단했소.”

“…….”

강호의 소문들을 모은 강호일보, 뭐 이런 게 있다면 바로 구독 신청을 하고 싶다. 제법 신빙성이 있는데 그래.

‘그보다…….’

공야청 이 사람, 설마 모르고 있나?

항산검문 놈들이 어떤 개수작을 부렸든 간에 이 모든 사건의 중심에는 내가 있다.

그 과정에서 수많은 희생이 있다는 것은 명백한 사실.

공야청과 소천이 내게 원한을 품어도 이상하지 않다. 그래서 이름을 숨긴 거였고.

‘모른다면 다행이지.’

잔인무도한 절정 고수에게 쫓기는 상황이다. 괜한 분란은 사양이다.

“본가까지 얼마나 걸리겠소?”

공야청의 말에 퍼뜩 정신이 돌아왔다.

“이틀에서 사흘 정도면 도착할 수 있을 겁니다.”

“하필 이럴 때 눈이라니…….”

공야청이 한탄했다. 아직도 눈을 펑펑 쏟아 내는 하늘을 원망스럽게 바라본다.

“공자, 최악의 상황을 대비해야겠소.”

“최악의 상황이요?”

폭설에 발이 묶이긴 했지만 그건 적들도 마찬가지다. 더군다나 놈들이 추격을 포기했을 가능성도 존재했다.

그러나 공야청은 고개를 가로저었다.

“낭인을 우습게 보지 마시오. 내력의 정순함과 익힌 무공의 수준은 떨어질지 모르나 놈들이 가진 가장 큰 무기는 따로 있소.”

나는 정답을 말했다.

“경험.”

“맞소. 백전(百戰)을 치르며 얻은 경험. 우리를 쫓는 건 무인이 아니라 낭인이오. 같지만 아주 다른 존재지.”

같지만 다른 존재. 무슨 뜻인지 알 것 같다.

요컨대 놈들은 잘 훈련된 사냥개라는 뜻이다. 그 목줄을 쥔 자가 일문일살 조필이다.

“조필이 진정 두려운 이유는 놈이 절정 고수이기 때문만은 아니오. 그 집요함. 악랄함. 그는 단 한 번도 의뢰에 실패하거나 표적을 놓친 적이 없소.”

나는 한숨처럼 대답했다.

“이번에도 마찬가지겠군요.”

“아마도.”

공야청이 어둠 너머를 응시했다. 마치 뭔가가 튀어나와 우리를 삼키기라도 할 것처럼.

“우린 그런 놈에게 쫓기고 있는 거요.”

휘이잉. 눈바람이 어둠 속으로 녹아들었다.



* * *



야영 준비가 끝났다. 작은 토굴을 여러 개 판 다음 나뭇가지, 낙엽 따위로 입구를 막은 조잡한 형태였지만 찬물 더운물 가릴 때가 아니다.

“편안한 밤 되시구려.”

공야청은 어느새 곤히 잠든 남매를 안고 사라졌다. 그의 입가에 매달린 지친 미소가 자꾸 생각났다.

‘어른이구나.’

살고자 했으면 진작 도망칠 수 있었을 것이다. 공야청은 무공을 익힌 고수였고 경륜 있는 무림인이니까.

하지만 그러지 않았다. 그는 피 한 방울 섞이지 않은 어린 남매를 위해 목숨까지 걸어 가며 싸웠다.

그래서 공야청은 좋은 어른이다.

‘나라면 그럴 수 있을까?’

문득 드는 의문을 털어 냈다. 이곳은 게임이다. 곧 사라질 환상에 대해 깊이 생각하는 건 좋지 않다.

맞다, 곧 사라질 환상이다.

‘퀘스트창 오픈.’

띠링.



퀘스트



[로그아웃]

이제 당신은 이 험난한 무림을 헤쳐 나가야 합니다.

더욱더 강해지고, 유명해지십시오.

언젠가 다가올 그 날을 위해…….



등급 : 메인 퀘스트

제한 : 진태경

임무 : [일류] 경지 달성 (미완료)

         Lv.30 달성 (24/30)

         명성 500 달성 (250/500)

보상 : [로그아웃]





적들을 처리하고 받은 경험치와 명성. 거기에 퀘스트 보상까지. 슬슬 이 험산의 정상이 보인다.

상태창을 열어 남은 포인트를 모두 분배하니 지쳐 있던 몸에 활력이 돈다.

‘거의 다 왔어.’

이번 고비만 넘기면 된다. 일문일살 조필. 얼굴도 모르는 그놈만 피하면 이 지긋지긋한 여정에 종지부를 찍을 수 있다.

하지만 또 다른 문제가 있었다.

‘레벨이나 명성은 어찌어찌 채운다 치고, 이놈의 경지는 어떻게 올리는 거야?’

처음 튜토리얼 퀘스트를 깨기 시작할 무렵 능력치 분배로 삼류에서 이류로 경지를 올린 적이 있다. 그런데 그 후로는 영 깜깜무소식이다.

‘도대체 뭐가 부족한 거지?’

무림에서 나는 비상식적인 존재다. 누구보다 빠르게 무공을 익히고 능력치를 올릴 수 있다. 여러 부분에서 시스템의 힘을 빌려 강해졌다.

그게 널리고 널린 이류 주제에 어지간한 일류 무림인을 말 그대로 발라 버릴 수 있었던 이유다.

그런데 정작 내가 일류가 아니라니!

‘진위경한테라도 물어볼걸.’

처음엔 계속 스탯이나 공력을 올리면 되겠지, 싶었는데 근래 들어서 뭔가 헛짚고 있다는 생각이 든다.

‘레벨? 스탯? 공력?’

그게 뭘까. 이 퍼즐을 완성할 마지막 한 조각이.

답은 금방 나왔다.

‘모르면 찾아야지.’

지금까지 해 왔던 것처럼. 걷다 보면 출구는 나온다.

나는 가부좌를 틀고 호흡했다. 단전에 똬리 튼 공력이 내 부름에 응답했다.



* * *



“놓쳤군.”

조필이 중얼거렸다. 독사처럼 까만 눈동자가 주위를 훑었다.

놈들을 놓쳤다. 그러나 흔적은 남았다. 미세하게 남은 그 흔적들이 새로운 이정표가 될 것이다.

“스무 명 전후. 약 두 시진 전에 자리를 떴습니다.”

수하의 보고에 조필이 고개를 끄덕였다. 무공은 삼류지만 추종술은 절정이다. 그의 밑에는 이런 사냥개들이 수두룩했다.

‘두 시진이라.’

어느새 거리가 두 시진으로 좁혀졌다. 도망자들을 따라잡기까지 어느 정도의 시간이 걸릴까?

길어야 반나절이다.

‘있는 힘을 다해 도망쳤어야지. 뒤도 안 돌아보고. 거추장스러운 혹은 떼고 낙오자는 버리고 악착같이 뛰었어야지.’

그랬다면 거리는 좁혀지지 않았을 것이다. 그러나 놈들은 방심했다. 폭설에 발이 묶였다고 생각했을 것이고, 그 차이가 지금의 상황을 만들었다.

‘나는 좀 다르거든.’

지난밤은 길었다. 추적에는 이골이 난 수하 중에서도 낙오자가 생길 정도였다. 폭설이 내리는 산중에서의 낙오란 죽음과 동의어다.

전장에서의 죽음과 다른 점이 있다면 조금 천천히 죽는다는 것뿐이다. 그래서 조필은 지시했다.



‘죽여.’



호랑이는 죽어서 가죽을, 사람은 이름을 남긴다고 했다.

하지만 조필의 생각은 달랐다. 일평생 뒷골목을 전전하던 삼류 인생에게 남길 이름이 있겠나. 가죽이라도 남겨야지.

발가벗겨진 스무 구의 시신을 뒤로하고 그들은 계속 나아갔다. 그렇게 긴 밤이 끝나고 동틀 무렵, 놈들의 흔적을 발견할 수 있었다.

‘곧 만날 수 있겠군, 친구.’

조필의 입꼬리가 올라갔다. 오랜만에 그의 흥미를 끈 수수께끼의 고수다. 굳어 있던 심장이 펄떡거리며 뛰었다.



* * *



부르르.

“어흐. 뭐야.”

순간 오한이 들었다. 팔뚝을 들어 보니 닭살이 오소소 돋아 있다. 지금이 소설의 한 장면이었다면, 주인공은 왠지 꺼림칙하다는 말과 함께 가던 길을 갔을 것이다.

하지만 나는 다르다. 확실한 심증을 갖고 움직인다.

“야. 잽싸게 튀어와.”

보이지 않지만 느껴진다. 뒤에서 터벅터벅 걷고 있던 누군가의 발걸음이 움찔한다.

“왜, 왜요.”

“셋 센다. 하나, 둘. 셋.”

셋을 셈과 동시에 혁무진이 잽싸게 옆에 붙었다.

“너지?”

“예?”

“너잖아. 솔직히 말하면 봐준다.”

“뭘요? 저 아닙니다!”

나는 찐빵처럼 부푼 녀석의 얼굴을 가만히 응시했다.

“방금 뒤에서 나 욕했지?”

“헛.”

“욕한 거 맞지?”

“마, 맞습니다…….”

역시 이 자식이었군. 내가 손을 들어 올리자 혁무진이 눈을 질끈 감는다.

세 번 정도 얻어터지자 녀석은 전의를 잃어버렸다. 거기에 더해 생활의 지혜도 터득했다.

피하면 더 맞는다는 사실을.

“좋아. 솔직히 말했으니 이번만은 봐준다.”

혁무진이 고개를 번쩍 치켜든다.

“정말이십니까?”

내가 따뜻한 미소를 지어 보였다.

“물론. 하지만 앞으로도 나를 속일 생각은 하지 마라. 관심법으로 널 지켜보고 있을 테니.”

혁무진은 마구니가 가득 낀 눈빛으로 나를 바라보다가 제 자리로 튀어 갔다. 시간만 넉넉했다면 철퇴로 머리를 으깨 주었을 텐데. 나는 아쉬움을 삼키고 계속 걸었다.

“관심법이 모야?”

재잘거리는 목소리에 귀가 간지럽다. 소천의 여동생인 소율이다. 다섯 살이라고 했나? 녀석은 내 배낭에 쏙 들어갈 정도로 작았다.

“무공이야?”

“비슷하지.”

“관심법, 세?”

“엄청 세지.”

“와! 소율이도 관심법 배우고 싶어요!”

“근데 눈이 애꾸여야 돼.”

“헉!”

고개를 슬쩍 돌려보니 화들짝 놀란 소율의 얼굴이 보인다. 휘둥그레진 눈동자가 장난 아니게 귀엽다.

‘하연이도 저랬었는데.’

지금이야 징그러운 여동생이지만 어릴 때는 아기 천사가 따로 없었다. 아역 모델 제의도 받고 그랬었는데…….

딱 그 시절의 하연이를 업고 다니는 기분이다.

“나한테 배울래?”

“……소율이는 무공 같은 거 안 좋아해요. 참한 규수가 될래요.”

“그것도 좋지.”

“으응. 아저씨는 무공 좋아해요?”

“나?”

“우리 오빠가 그러는데요, 아저씨가 엄청 세대요. 아빠는 열심히 하는 사람만 세질 수 있다고 했어요.”

“아빠가 그러셨어?”

“네. 우리 아빠도 엄청 세요. 왜냐하면요…….”

조잘조잘. 한동안 잔뜩 신나서 떠들어 대던 소율이 입술을 삐죽 내밀었다.

“소율이는 아빠 보고 싶은데. 아빠는 아닌가 봐요. 오빠가 그러는데요, 나랑 오빠 놔두고 엄마랑 놀러 갔대요.”

순간 심장이 쿵 떨어졌다. 오래전의 기억이 눈 앞을 가린다. 온통 검고 흰 장례식장에서 어린 하연이는 아버지를 찾았고, 나는 뻔한 거짓말을 할 수밖에 없었다.

소천이 소율에게 했던 것처럼. 그 말밖에 할 수 없었다.

“……그렇구나.”

더 무슨 말을 하겠나. 나는 대열의 중간에서 따라오고 있는 소천을 바라봤다. 거친 숨을 몰아쉬는 녀석은 땀으로 흠뻑 젖어 있었다.

‘힘들 텐데.’

나이답지 않은 의지력이다. 고통이 사람을 성숙하게 한다는 말은 좆 같지만 사실이다.

소천은 단 한 번도 뒤처지지 않았고 그 모습에 다른 순찰조원들도 감탄했다.

‘문제는 따로 있어.’

공야청이다. 부상에서 벗어나지 못한 그의 얼굴은 창백하게 질려 있었다. 내가 준 벽곡단의 뛰어난 효능과 지난밤의 운기조식이 아니었다면 진작 쓰러졌을지도 모른다.

‘이대로라면…… 따라잡힌다.’

해가 떴음에도 쌓인 눈은 쉽사리 녹아내리지 않았다. 내가 앞장서서 눈을 헤치며 길을 뚫고 있지만 다들 지쳤고 속도는 느려진다. 거기에 더해 부상자와 아이까지.

‘혼자라도 도망칠까?’

순간 떠오른 생각이다.

게임인데 뭐 어때. 공야청도, 저 어린 남매와 순찰조원들 모두가 창조된 인공지능이고 NPC에 불과하다. 하지만 나는?

살아 있다. 이들 가운데 나 홀로 진짜고 실체다.

하지만…….

‘시발. 간단한 문젠데…… 왜 이래?’

이유 모를 거부감이 솟구쳤다. 스스로도 깜짝 놀랄 만큼의 거부감에 당황스럽기까지 하다.

‘도대체 왜?’

모르겠다. 그 후 몇 시간 동안이나 나는 정답을 찾지 못했고, 그렇게 밤이 찾아왔다.
```

## Current accepted English baseline

```markdown
# Chapter 26

“So…”

Gong Yacheong looked at me with a strange expression.

“So you are that Young Master Jin Taekyung.”

The moment had finally come. I let go of Hyuk Mujin’s collar—he’d passed out for the third time—and smiled awkwardly.

“Yes. I’m Jin Taekyung.”

The reconnaissance squad members preparing camp pricked up their ears. We were on our way back to the main family.

We had ridden for more than five hours without a break since leaving the cabin where the fight had taken place. Gong Yacheong had kept his mouth shut the entire way. Only now did he speak.

*If it weren’t for that bastard.*

I glared at Hyuk Mujin, who was being dragged along by one of the quicker-witted squad members. I should have hit him one more time before letting go.

As I was still regretting that, Gong Yacheong spoke.

“I’ve heard plenty about you, Young Master.”

“…I see.”

“Even a three-year-old knows who you are. You must be the main family’s biggest celebrity.”

At this point, it would have been faster to find someone who didn’t know me.

“You’re lazy by nature and arrogant beyond belief. You’re lost in wine and women and don’t even practice martial arts… But I see the rumors of the martial world aren’t worth believing after all. The martial prowess you displayed today was truly remarkable.”

“…”

If there were some kind of Martial World Daily that collected every rumor in the martial world, I’d subscribe immediately. It was surprisingly credible.

*More importantly…*

Did Gong Yacheong really not know?

Whatever bullshit the Mount Heng Sword Sect had pulled, I was at the center of this entire mess.

It was an undeniable fact that countless people had died along the way.

It wouldn’t have been strange if Gong Yacheong and Socheon held a grudge against me. That was why I had hidden my name.

*If he really doesn’t know, that’s a relief.*

We were being chased by a ruthless Peak master. I had no interest in stirring up extra trouble.

“How long until we reach the main family?”

Gong Yacheong’s question snapped me back.

“We should arrive in two or three days.”

“Of all times, it had to snow now…”

Gong Yacheong lamented. He glared resentfully at the sky, still dumping snow.

“Young Master, we should prepare for the worst.”

“The worst?”

The blizzard had us stuck, but it had our enemies stuck too. There was even a chance they had given up the chase.

Gong Yacheong shook his head.

“Don’t underestimate wandering martial artists. The purity of their internal energy and the martial arts they’ve learned may not amount to much, but their greatest weapon is something else.”

I gave him the answer.

“Experience.”

“Exactly. The experience gained from fighting a hundred battles. What’s chasing us isn’t martial artists. It’s wandering martial artists. Similar, but entirely different creatures.”

Similar, but different. I thought I understood what he meant.

In short, they were well-trained hunting dogs. And the man holding their leash was Jopil, One Question, One Kill.

“The reason Jopil is truly frightening isn’t simply because he’s a Peak master. It’s his persistence. His viciousness. He has never once failed a commission or allowed a target to escape.”

I answered with a sigh.

“It’ll be the same this time, then.”

“Probably.”

Gong Yacheong stared into the darkness ahead, as though something might leap out and swallow us whole.

“We’re being chased by a man like that.”

Whoosh. The snow-filled wind faded into the darkness.

* * *

We finished making camp. We had dug several small dugouts and blocked their mouths with branches, fallen leaves, and whatever else we could find. It was crude, but this was no time to be choosy.

“Have a comfortable night.”

Gong Yacheong had already vanished, carrying the sleeping siblings in his arms. I kept thinking of the exhausted smile at the corner of his mouth.

*He really is an adult.*

If he had wanted to live, he could have run away long ago. Gong Yacheong was a trained master, a seasoned man of the martial world.

But he hadn’t.

He had risked his life fighting for two children who didn’t share a drop of his blood.

That was why Gong Yacheong was a good adult.

*Could I have done the same?*

I shook the question off as soon as it came up. This was a game. It wasn’t good to think too deeply about an illusion that would soon disappear.

That was right. An illusion that would soon disappear.

*Open Quest Window.*

Ding.

> **System**
>
> **Logout**
>
> You must now make your way through this harsh Murim.
>
> Become stronger. Become famous.
>
> For the day that will come someday…
>
> **Grade:** Main Quest
>
> **Limit:** Jin Taekyung
>
> **Task:** Reach the First Rate realm — Incomplete  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reach Lv. 30 — 24/30  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reach Fame 500 — 250/500
>
> **Reward:** **Logout**

The EXP and Fame I had received for dealing with the enemies. The Quest reward on top of that.

I was starting to see the summit of this treacherous mountain.

I opened my Status Window and distributed all my remaining points. Vitality flowed back into my exhausted body.

*I’m almost there.*

I only had to get past this hurdle. If I could avoid that bastard Jopil, One Question, One Kill—the man whose face I didn’t even know—I could finally put an end to this miserable journey.

But there was another problem.

*Let’s say I can somehow fill up my Level and Fame. How am I supposed to raise this damn realm?*

Back when I first started clearing the tutorial Quests, I had raised my realm from Third Rate to Second Rate by distributing my stats. After that, radio silence.

*What the hell am I missing?*

I was an absurdity in Murim. I could learn martial arts and raise my stats faster than anyone else. I had grown stronger with the System’s help in all kinds of ways.

That was why I could literally wipe the floor with ordinary First Rate martial artists despite being a dime-a-dozen Second Rate.

And yet I wasn’t First Rate!

*I should’ve asked Jin Wikyung.*

At first, I thought I just needed to keep raising my stats or internal energy. Lately, though, I had started to feel I was barking up the wrong tree.

*Level? Stats? Internal energy?*

What was it? The last piece needed to finish this puzzle?

The answer came quickly.

*If I don’t know, I have to find out.*

Just like I had until now. If I kept walking, I would find an exit.

I sat cross-legged and regulated my breathing. The internal energy coiled in my dantian answered my call.

* * *

“We lost them.”

Jopil muttered. His black, viper-like eyes swept the surroundings.

They had lost the fugitives. But traces remained. Those faint traces would become new signposts.

“About twenty people. They left this place roughly two shichen ago.”[^1]

Jopil nodded at his subordinate’s report. The man’s martial arts were only Third Rate, but his tracking skills were Peak. Jopil had countless hunting dogs like that under his command.

*Two shichen.*

The gap was already down to two shichen. How long would it take to catch the fugitives?

Half a day at most.

*They should have run with everything they had. Without looking back. They should have thrown off every burden, abandoned any stragglers, and kept running for their lives.*

If they had done that, the distance would not have narrowed. But they had let their guard down. They must have thought the blizzard had them trapped.

That difference had created the current situation.

*But I’m a little different.*

The previous night had been long. Even among his pursuit-hardened subordinates, there had been stragglers.

In the mountains during a blizzard, falling behind was as good as dying.

The only difference from dying on a battlefield was that it took a little longer.

That was why Jopil had given the order.

*Kill them.*

They said that when a tiger died, it left its hide, and a person left a name.

But Jopil thought differently. What kind of name could a Third Rate nobody who’d spent his whole life drifting through back alleys leave behind?

They should at least leave a hide.

Leaving twenty stripped corpses behind, they continued onward. After the long night ended, they found the fugitives’ traces just before dawn.

*We’ll be meeting soon, friend.*

The corners of Jopil’s mouth lifted. A mysterious master—the first in a long while to catch his interest.

His long-stiff heart began to pound.

* * *

I shuddered.

“Ugh. What the hell?”

A chill had run through me. I lifted my arm and found it covered in goose bumps.

If this were a scene in a novel, the protagonist would have muttered, *Something feels off,* and gone on his way.

But I was different. I had a solid hunch, and I acted on it.

“Hey. Get over here, quick.”

I couldn’t see him, but I could feel it. Someone trudging behind me faltered.

“W-why?”

“I’m counting to three. One, two. Three.”

The instant I hit three, Hyuk Mujin hurried over and pressed himself against my side.

“It was you, wasn’t it?”

“What?”

“You were the one. Tell me the truth and I’ll let it slide.”

“What? I didn’t do anything!”

I silently stared at his face, swollen like a steamed bun.

“You were cursing me behind my back just now, weren’t you?”

“Hah.”

“You were cursing me, right?”

“I-I was…”

So it really had been this bastard. When I raised my hand, Hyuk Mujin squeezed his eyes shut.

After getting beaten about three times, he had lost all his fighting spirit. On top of that, he had learned a valuable life lesson:

Dodging only meant getting hit more.

“Fine. Since you told the truth, I’ll let it go this once.”

Hyuk Mujin jerked his head up.

“Really?”

I gave him a warm smile.

“Of course. But don’t even think about deceiving me from now on. I’ll be watching you with mind-reading.”

Hyuk Mujin glared at me like he wanted to kill me, then bolted back to his place. If I’d had enough time, I would have crushed his head with a mace.

Swallowing my regret, I kept walking.

“What’s mind-reading?”

The chatter tickled my ears. It belonged to Soyul, Socheon’s little sister. Was she five years old?

She was small enough to fit right inside my backpack.

“Is it martial arts?”

“Something like that.”

“Is mind-reading strong?”

“Very.”

“Wow! Soyul wants to learn mind-reading, too!”

“But you have to be one-eyed.”

“Gasp!”

I glanced over and saw Soyul staring at me, startled. Her eyes had gone huge. Ridiculously cute.

*Hayeon used to be like that, too.*

These days she was a creepy little sister, but when she was little she had been a baby angel. She had even gotten offers to be a child model…

Having her around felt exactly like piggybacking Hayeon at that age.

“Do you want me to teach you?”

“…Soyul doesn’t like martial arts. I want to become a proper young lady.”

“That’s fine, too.”

“Mm. Mister, do you like martial arts?”

“Me?”

“My brother says you’re really strong. Dad said only people who work hard can become strong.”

“Your dad said that?”

“Yes. My dad is really strong, too. Because…”

She chattered excitedly for a while, then stuck out her lower lip.

“Soyul wants to see Dad. But I guess Dad doesn’t want to see us. Oppa says he went out to play with Mom, leaving me and Oppa behind.”

My heart dropped with a thud.

An old memory filled my vision. In a funeral hall of black and white, little Hayeon had searched for our father, and I had no choice but to tell her an obvious lie.

Just as Socheon had done for Soyul.

It was the only thing I could say.

“…I see.”

What else could I say?

I looked at Socheon, following along in the middle of the formation. He was panting, soaked in sweat.

*He must be exhausted.*

His willpower was far beyond his years. The saying that pain made people mature was fucking bullshit, but it was true.

Socheon had never fallen behind even once, and the other reconnaissance squad members marveled at him for it.

*But the real problem is somewhere else.*

Gong Yacheong.

His face was deathly pale; he still hadn’t shaken off his injuries. If not for the remarkable effects of the fasting pills I had given him, and the qi he had circulated last night, he might have collapsed long ago.

*At this rate, we’ll be caught.*

Even after the sun rose, the packed snow wouldn’t melt. I was out front, clearing a path through it, but everyone was exhausted, and our pace had slowed.

On top of that, we had an injured man and children.

*Should I run away by myself?*

The thought came in an instant.

It was a game. So what?

Gong Yacheong, those two kids, the whole reconnaissance squad—every last one of them was created AI. Just NPCs.

But what about me?

I was alive. Among all of them, I was the only one who was real. The only one with a real body.

But…

*Fuck. It’s a simple problem… Why am I like this?*

An inexplicable aversion surged up. It was strong enough to startle me—strong enough to throw me off.

*Why?*

I didn’t know.

I didn’t find the answer for hours after that, and then night came.

[^1]: A shichen is a traditional time period of roughly two hours.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 26`.

# Master Edit Task — Chapter 60

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
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 마교     | **Demonic Cult**                                 |                                                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 일격     | **One Strike**                         |
| 스킬               | **Skill**                      |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 평화 | **Peace Guild** | Guild name. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 55–59

## Plot

Taekyung wakes in Murim after roughly two hours of deathlike sleep and learns that the reconnaissance squad has sent messengers to the Jin Family’s main force. He orders the exhausted squad to reach Eight Spring Gorge before the battle is lost. There, Mount Heng’s larger army is trapped in the Jin Family’s terrain-controlled gorge while hidden cliff archers fire on them. Lee Cheonbaek leads Mount Heng’s core forces in a desperate assault, but the Head Elder overwhelms him with Sword Energy and prepares to kill him.

Taekyung arrives, splits a spear aimed at the Head Elder, and publicly brands him a traitor. The Jin Family’s First, Second, and Third Elders reveal concealed Peak-level abilities and turn against their own side. A signal flare prompts the embedded Three Paths Sect, Byeokdo Sect, Gunggwimun, and other Five Gates of Shanxi forces to attack their supposed allies, exposing a decades-old conspiracy. The Head Elder confirms that “they” killed Lee Seogeun but does not identify the accomplice or explain the complete plan.

The Discipline Hall Master dies defending the Jin Family’s laws, rallying the Jin and Mount Heng fighters against the black-clad conspirators. The Second and Third Elders are killed, while the First Elder admits greed and glory as his stated motives and points Taekyung toward the Head Elder when Taekyung identifies revenge as the deeper cause. Jin Wikyung expels the First Elder and leaves him surrounded by Wipeng and ten senior members before leading guards toward Taekyung.

Taekyung attacks the Head Elder with the Gambler Title active but is decisively overpowered. The elder cuts his spear down to an iron rod. While trying to rescue Jin Wikyung, Taekyung grabs the wrong person and escapes with the gravely wounded, silenced, and paralyzed Lee Cheonbaek. With Hyuk Mujin and the reconnaissance squad, he forms an encirclement against the Head Elder, belatedly realizing that his raid-party tactics are useless without a tank, healer, or ranged damage dealer. The battle remains unresolved.

## Continuity

- The Eight Spring Gorge battle continues. The Head Elder remains the dominant combatant and can overpower Taekyung’s Gambler-boosted attacks with Sword Energy.
- The Head Elder’s betrayal and the Five Gates conspiracy are exposed, but the accomplice who killed Lee Seogeun, the meaning of the signal, the revenge motive, and the full conspiracy remain unresolved.
- The Second and Third Elders are dead. The First Elder is alive, expelled from the Jin Family, and surrounded by Wipeng and ten senior members; his fate is unresolved.
- Jin Wikyung is alive and leading guards toward the Head Elder. Taekyung mistakenly rescued Lee Cheonbaek instead of Wikyung.
- Lee Cheonbaek remains alive but unable to speak or move. Taekyung, Hyuk Mujin, and the reconnaissance squad are confronting the Head Elder.
- Taekyung knows that logging in or logging out leaves the other side in a deathlike sleep. The Ark - 2020 capsule’s safe operation, ultimate purpose, and route between realities remain unresolved.
- Taekyung’s Traitor Chain Quest remains active and requires punishing the traitor and leading the battle to victory; failure means death.

## Translation Decisions

- Preserve **Head Elder**, **First/Second/Third Elder**, **Discipline Hall Master**, **Peak master**, **Sword Energy**, **Blood Wolf Sword**, and **Blood Rain Group**.
- Use **Eight Spring Gorge**, **Three Paths Sect**, **Byeokdo Sect**, and **Gunggwimun** consistently.
- Retain the raid framing—**tank**, **healer**, and **damage dealer**—and Taekyung’s dry, profane self-mockery.
- Preserve the Head Elder’s unresolved Sound Transmission reveal that “they” killed Lee Seogeun.
- Keep **Gambler** as the System Title and **logged in** only for Taekyung’s connection to Murim.

### Prior accepted reading-copy tails

#### Chapter 58 tail (verified mastered)

…
> - The effect of the Title **Gambler** is applied. > - **Strength** temporarily increases. > - **Agility** temporarily increases. > - **Stamina** temporarily… The effect of the Gambler Title, which raised combat-related stats by ten percent in a one-on-one duel, seeped through my whole body. And on top of that— Whoosh! The boost to my stats accelerated the attack as well. In an instant, the spearhead dropped like a bolt of light, aimed at the crown of the Head Elder’s head. *This is going in.* That was a certainty. The certainty that even a monster like Jopil wouldn’t have been able to dodge it. But the man I was facing wasn’t Jopil. He was the Head Elder. Boom! The spear shaft shuddered with a thunderous crash. The Head Elder, having blocked the spear at a speed too fast to see properly, smiled faintly. “Not bad. Better than I expected.” Without even time to answer, I wrung out every last ounce of strength. The spear, loaded with tremendous force that even a decent master would have struggled to endure, crushed down on his sword. Grrrkk. With an ugly grinding sound, his sword began to rise… No. Wait. *It should be going down. Why is it coming up?* I’d put that much force into it, yet I was the one being pushed back. At my dumbfounded expression, the Head Elder’s smile deepened. “You tried, but did you think that would be enough?” The next instant, every hair on my body stood on end. Tsssss. A blue haze bloomed along the blade. Sword Energy. Before I could even react, the spearhead that had been slowly getting pushed back was sliced off like tofu. Shing. Now it wasn’t a spear but a staff. A long staff. Sword Energy flashed again toward me as I backed away. Shing. The long staff became a short staff. Shing. “…” Fuck. Even a pair of nunchucks would be longer than this. I threw the iron rod—no longer a spear or a staff—at the Head Elder. Shing. “Do you intend to run?” Run? That’s a hurtful thing to say. I’d already thrown myself sideways the instant I hurled the rod. I grabbed the collar of the man lying facedown as if he were dead. *Got him!* My only goal from the beginning had been to rescue Jin Wikyung. Now that I’d done it, there was no reason to fight that monstrous old man. I scooped Jin Wikyung into my arms and hurled myself away with all my strength. Whoosh—boom! The Sword Energy that arrived a beat later split the ground. Hyuk Mujin and the reconnaissance squad surrounded us as we slipped out of the Head Elder’s range by a hair. “Protect the Squad Leader!” “Are you all right?” I said nothing. I forgot we had to run from the Head Elder right now. I even forgot this was a battlefield. My head was full of a single question. *Who is this man?* I had definitely rescued Jin Wikyung. I was supposed to have rescued him… Then who was this macho middle-aged man in my arms? His face was covered in sword scars, and his eyes were bloodshot. In a trembling voice, I asked, “Excuse me, but who are you…?” At that moment, a single cry burst from Hyuk Mujin’s mouth. “Gah! Lee Cheonbaek!” Lee Cheonbaek? The name rang a bell. “You know him?” “Of course I do!” “Are you close?” “What kind of bullshit is that? That’s Blood Wolf Sword Lee Cheonbaek!” “Blood Wolf Sword?” “Yes! That Blood Wolf Sword…!” “Cool alias. Sounds like a master.” Hyuk tore at his hair and shouted, “He’s the Sect Leader of the Mount Heng Sword Sect! Blood Wolf Sword Lee Cheonbaek!” “…” I scrambled backward. This man was Lee Cheonbaek? Cold sweat rolled down my body. *He’s Lee Seogeun’s father.* He was the man who’d started a war because he thought I’d poisoned his son. He was also a cold-blooded killer who’d slaughtered adults and children alike in revenge. *Rescuing the wrong guy was unfair enough, and I nearly got stabbed too.* But Lee Cheonbaek no longer seemed to have the strength left for that. His entire body was covered in blood, and he couldn’t so much as twitch a finger. It looked as though he’d suffered severe internal injuries, or had his acupoints sealed. *Still, at least it isn’t Jin Wikyung.* As if he’d read my mind, Hyuk asked, “Then where is the Lesser Family Head?” “I don’t know. And…” I yanked him back by the nape of his neck. A sword came flying in and buried itself where Hyuk’s foot had been a moment before. *I’m really well and truly screwed.* I let out a deep sigh, then continued. “You think that old man is going to let us go?” The Head Elder burst into a hearty laugh. “Ha ha ha! Have you ever seen such an insolent brat!” “If I behave politely, will you let us go?” “Don’t you think you’ve come too far for that?” Tsssss. Sword Energy surged up. No more words were needed. I pulled a spear from where it was stuck among the corpses. Then, with everyone’s eyes on me, I spoke. “Encirclement formation. Spread out.” One of the oldest Hunter sayings went like this: *There are strong monsters, but no monster that can’t be taken down.* What made that possible was a raid.

#### Chapter 59 tail (verified mastered)

…
Mount Heng Sword Sect!” “I don’t know where you crawled out from, but wipe them all out!” Once the two forces joined up, it was the black-clad men who started to give ground. They were elites hardened by brutal training, but the deaths of the two Elders inevitably shook their morale. Blades poured in from every direction, exploiting every opening, and the black-clad men began to fall one after another. “Aaargh!” “Don’t fall back! Anyone who falls back dies!” Even amid the chaos, the First Elder silently swung his sword. Everything his eyes fell on, everything his hands reached toward, was an enemy. Shhk. Twenty? Thirty? He had lost count. Like a man possessed, the First Elder cut down everything in his path. Among his victims were men who had once addressed him with respect, as well as youths who looked barely twenty. *What does age matter to living and dying? Anyone who stands at the point of a sword is a person of Murim.* What blocked the First Elder, drenched in the blood of dozens, was a man built like a bear. His eyes looked ready to burn everything to ash. “Why did you do it?” “Wealth and glory. To seize the Jin Family of Taiyuan and swallow Shanxi whole.” The answer came without a hint of hesitation, and everyone trembled with rage. Everyone except one. Jin Wikyung shook his head. “That isn’t the answer I wanted.” “Then you answer, Lesser Family Head. Why would I, my brothers, and our lord do a thing like this?” “Revenge.” Jin Wikyung continued in a low voice. “The grand plan you talked about wasn’t for wealth and glory, or to become the ruler of a single province. Too many chances for that have already passed, and you’re all old. And…” “Enough.” “The Head Elder has no descendants. Neither do the Second Elder, the Third Elder, or you.” In that instant, a livid spark leapt from the First Elder’s still eyes. It was anger he had held down for a very long time—dregs that rose for the briefest moment, then sank again. “Why did you do it?” Instead of answering, the First Elder raised his sword and pointed it at Jin Wikyung. No—the tip pointed past Jin Wikyung’s shoulder, toward someone somewhere beyond him. “Hear it from him yourself.” In the end, the last key was in the Head Elder’s hands. Jin Wikyung took a long stride toward the First Elder. “I will. After I cut you down.” “Well? Can you really afford to take it this easy?” “What do you—” Jin Wikyung’s frown went rigid. *Taekyung!* His youngest brother, the apple of his eye, was standing in the Head Elder’s way. The instant he remembered the fact that had briefly slipped his mind, his blood seemed to turn cold. *If I delay any longer, something irreversible will happen.* Once he grasped the whole situation, a voice like frost burst from Jin Wikyung’s mouth. “Wipeng. Take care of the First Elder.” “I obey.” “The rest of you, lend him your strength.” “We follow the Lesser Family Head’s command.” Wipeng and some ten surviving senior members spread into a wide ring around the First Elder. “Everyone else, follow me and open a path! We’re going after the Head Elder!” Jin Wikyung was about to move with several dozen guards when he glanced at the First Elder. Even with his end closing in, the man showed no agitation. If anything, he looked unburdened. “First Elder.” “Do you have something left to say?” Jin Wikyung tossed out a single line. “By the authority vested in me as Lesser Family Head of the Jin Family of Taiyuan, I expel you from the family.” “Heh heh. Heh heh heh!” Leaving the First Elder’s laughter behind him, Jin Wikyung sprinted for the battlefield. Dozens of black-clad men tried to stop him, but the battle had long since turned against them. Martial artists converged from every direction and hacked them to pieces. “Open a path!” “It’s the Lesser Family Head! Kill anyone who gets in his way!” It was only a moment. For Jin Wikyung, an eternity passed. *Taekyung. Please, please…* He could not even bring himself to think the word *death*. How long had he run, clutching his pounding heart? When he finally reached his destination, his eyes flew wide. *What is this…* The scene in front of him was shock itself. * * * Raid. Until a few decades ago, it was a word that only meant anything in games. But after the Demon King appeared and the Great Cataclysm began, raids became the symbol of Hunters. Getting there had taken countless real battles and countless sacrifices. On that foundation, the raid methods used today had finally been set down. *Tank, damage dealer, healer.* The tank blocks. The damage dealer hits. The healer heals. It sounded simple, but to become a proper Hunter you had to study a mountain of raid manuals and prove yourself in actual combat. *Hunter training camp… that was a living hell.* But enduring it was what made me a Hunter. Now, as a seven-year veteran, I could come up with the right positions and response for any situation. And right now— “Hey, throw dirt! Keep throwing!” I realized that everything I’d learned wasn’t worth shit. Tank? Healer? Fuck… I was a fucking moron for thinking ten melee damage dealers counted as a raid.

## Korean source

```text
＃60화



대장로는 생각했다.

‘내가 너무 오래 살았나?’

그가 기억하는 무림은, 무림인은 이렇지 않았다.

합공은 수치요, 암습은 지탄을 받았으며 등에 흙이라도 묻으면 비웃음의 대상이 되었다.

그런데…….

“흙 뿌려! 계속 뿌려!”

팔십 평생 이런 경우는 처음이다. 뭐? 흙을 뿌려?

수십 년 전 원수처럼 싸웠던 마교도들조차 쓰지 않았던, 저열하고 비겁한 수법이다.

‘저놈이 정녕 무인이란 말인가.’

더욱 기가 막히는 것은 수하라는 놈들의 반응이었다.

“조장 명령이다! 흙 뿌려!”

“거리 벌려! 검기 조심해!”

군말 없이 명령을 따라 움직이는 놈들을 보니 현기증이 돌았다.

‘이런 쳐 죽일 놈들을 보았나.’

이놈들은 무인이 아니다. 아니, 사람도 아니다.

이건 무인에 대한 모욕이자 동시에 일평생을 검에 바친 대장로 자신에 대한 모욕이기도 했다.

“감히…….”

그가 검을 뽑아 들었을 때였다.

“이 멍청한 놈들!”

반 박자 빨리 터져 나온 준엄한 외침. 벌에라도 쏘였는지 얼굴이 퉁퉁 부은 청년이 사나운 눈빛으로 주위를 쓸어 보았다.

“지금 뭣들 하자는 거야!”

행색은 우습지만 기개는 제법이다. 맞다, 무인이라면 응당 저래야 한다.

‘그래도 멀쩡한 놈이 하나는 있군.’

대장로가 내심 고개를 끄덕이던 그 순간이었다.

“흙으로 되겠냐? 돌도 섞어!”

“……!”

대장로는 벼락 맞은 사람처럼 몸을 부르르 떨었다.

난생처음 느껴 보는 치욕에 검을 휘두르는 것도 잊은 그의 얼굴로 흙덩이가 날아왔다.

철퍽!

단언컨대, 팔십 평생을 돌이켜 봐도 가장 굴욕적이고 무방비하게 허용한 공격이다. 후두둑 쏟아지는 흙 사이로 야무지게 섞어 놓은 짱돌 하나가 보였다.

“으허, 으허허허.”

실성한 사람처럼 웃던 대장로의 웃음이 뚝 끊겼다.

그와 동시에.

츠츠츠.

일 갑자의 공력을 머금은 검기가 치솟았다.

“각오는 되었느냐?”

그 모습을 지켜본 진태경이 중얼거렸다.

“돌은 섞지 말지…….”

말이 떨어지기도 전에 대장로가 사자처럼 달려들었다. 십여 명의 양 떼들은 비명을 지르며 도망쳤다.

“산개! 산개해라!”

“흙도 뿌려!”

물론 그 와중에도 흙을 뿌리는 것은 잊지 않았다.



* * *



후우웅-

대장로의 검 끝에서 거센 돌풍이 불었다. 모래, 흙, 돌. 그게 뭐든 간에 상관없었다. 압도적인 힘 앞에 부서지고 흩어질 뿐이다.

‘저 인간을 어떻게 상대하나.’

정면 승부?

말이 좋아서 근접 딜러지, 정찰조를 대장로에게 붙여 놨다간 눈 깜짝할 사이에 무더기로 죽어 나갈 거다.

그래도 정든 놈들인데 무의미한 개죽음을 당하게 만들 수는 없지.

“조자아앙!”

저놈은 죽어도 싸지만.

‘그러니까 돌을 왜 섞어, 돌을.’

대장로의 1차 목표는 혁무진이었다. 용감무쌍하게 선방을 날렸으니 당연한 결과다. 나는 깊은 한숨을 내쉬며 혁무진에게로 몸을 날렸다.

쉬이이익!

대장로의 가슴을 향해 힘껏 내지른 창.

동시에 혁무진의 등을 베려던 검기가 방향을 틀었다.

슁.

저 망할 놈의 검기.

매끈하게 잘려 나간 창두를 확인할 시간도 없다. 나는 공포에 질린 혁무진의 목덜미를 잡아챘다.

“튀어!”

그러나 쉽게 포기할 대장로가 아니었다.

쐐애애액!

파공성과 함께 옆구리가 뜨거워졌다. 단순히 스친 것만으로도 살이 한 움큼 뜯겨 나가며 피가 튄다.

‘큭.’

더럽게 아프네. 하지만 지금 상황에서는 비명도 사치다.

‘시간을 벌어야 해.’

나는 혁무진을 옆으로 밀치며 돌아섰다. 그런 내 행동에 대장로가 눈썹을 치켜올렸다.

“네가?”

단 두 글자였지만 의미는 정확하게 전달받았다. 너 따위가 날 막을 수 있겠냐. 그런 뜻이겠지.

나는 태연한 척 대답했다.

“어, 내가.”

“목숨이 아깝지 않으냐?”

“더럽게 아깝다고 하면, 살려 줄래?”

“허허, 그놈 참. 어린 녀석이 혀가 짧구나.”

“할배, 고추는 서요?”

츠츠츠.

우뚝 섰다.

크고 아름다운 검기가.

“……정정하시네.”

창을 잡은 손이 땀으로 축축해졌다.

‘이거, 남은 밑천까지 탈탈 털어야 살 수 있겠는데.’

나는 대장로가 아는 것보다 훨씬 비밀이 많은 놈이다.

인벤토리를 활용한 공격과 순간적으로 몇 배의 힘을 일격에 쏟아붓는 스킬, 일섬(一殲).

‘이럴 때를 대비해서 한 번도 안 보여 줬지.’

이런 걸 무림에서는 최후 절초라고 하던가?

대장로, 아니 무림의 누구도 예상하지 못할 수법인 것은 확실하다. 거기에 더해서…….

“포위 대형, 펼쳐.”

스스슥.

혁무진과 정찰조원들이 사방에서 조여 오기 시작한다.

대장로라는 대어를 잡기에는 허술한 그물. 그러나 날카로운 작살이 있다면 해볼 만한 싸움이다.

“고작 이 정도로 되겠느냐?”

“노인네 하나 잡는데 이 정도면 충분하지.”

대장로가 재미있다는 듯 웃었다.

“겁 없는 철부지로군. 매를 맞아야 정신을 차리는.”

그러나 그의 바람은 이뤄지지 못했다. 다음 순간 불쑥 끼어든 목소리 때문이었다.

“내가 잘못 들은 것 같은데, 다시 한번 말해 보시오.”

산악 같은 덩치에 부리부리한 눈매. 두툼한 입술 사이로 흘러나오는 음성은 얼음장처럼 차가웠다.

“우리 애를 건드리겠다고?”

후우웅.

검신을 타고 들불처럼 일어난 검기가 대장로를 겨눈다.

구세주처럼 나타난 진위경이 나를 향해 눈을 찡긋했다.

“어떠냐, 형 멋있지?”

참, 여전하다.



* * *



한 달 만에 보는 얼굴.

진위경의 등장에 굳어 있던 몸이 스르륵 녹아내렸다.

반갑고, 그저 반가웠다.

‘다행이야, 살아 있어서.’

상당한 격전을 치렀는지 진위경은 피투성이였다. 찢어진 옷 사이로 크고 작은 상처들이 보였다.

하지만 그걸로 됐다. 살아 있다는 사실이 중요한 거니까.

‘하고 싶은 말은 많지만 대화는 나중으로.’

해후는 이 전쟁이 끝난 후에 나눠도 늦지 않다. 진위경도 같은 생각인지 정면을 향해 시선을 돌렸다.

우리의 시선 끝, 대장로가 천천히 입을 뗐다.

“네가 여기까지 왔다는 건…….”

진위경의 서늘한 목소리가 말꼬리를 잘랐다.

“이, 삼장로는 죽었소. 일장로도 시간문제고.”

희소식이다. 진위경이 이렇게 언급했다면 이 전쟁에서 장로들의 비중이 작지 않았다는 의미고, 대장로의 손발이 잘려 나갔다는 뜻이니까.

“두 사람은…… 편안하게 갔느냐?”

“아마도.”

대장로는 선선히 고개를 끄덕였다.

“무인답게 싸우다 죽겠다고 입버릇처럼 말했었지. 소원대로 됐으니 다행이야.”

“무인이 아닌 배신자로 기억될 거요. 당신들 모두.”

“역사는 승자가 쓰는 법이지.”

대장로가 우리 쪽으로 검을 겨눴다. 나와 진위경을 포함한 수십 명 앞에서도 그는 당당했다.

“이제 승자를 가려 보자꾸나.”

진위경은 할 말이 있는 듯 잠시 입을 열었지만, 이내 굳게 다물었다. 다음 순간 그의 입에서 우렁찬 포효가 터져 나왔다.

“역도를 처단하라!”

스릉. 스르릉.

수십 개의 병장기가 일제히 한 사람을 향해 뽑혀 나오는 장면은, 일대 장관이었다.

“존명!”

거대한 함성과 함께 수십의 무인이 한 덩어리가 되어 돌격한다. 물론 나도 예외는 아니었다. 창을 움켜쥔 손아귀에는 힘이 들어갔고, 가슴은 터질 것 같았다.

‘이길 수 있다. 아니, 무조건 이긴다.’

대형 따위는 찾아볼 수 없는 전면전. 그러나 우리에게는 절정 고수인 진위경이 있고 그를 따르는 수십의 무인이 있다.

‘그리고 내가 있지.’

대장로는 자신의 무력을 너무 맹신했다. 최소한의 호위도 남기지 않고 모조리 전선에 투입했고, 그 결과 지금 흑의인들은 태원진가와 항산검문의 합공에 발목이 잡혀 버렸다.

대장로는…… 바로 이 자리에서 죽는다.

‘끝이다!’

그러나 내 확신이 산산이 부서지기까지는 그리 오랜 시간이 걸리지 않았다.

슈슈슈슉!

난데없이 쏘아진 수십 개의 점. 공기를 가르며 날아든 그것들은 모두의 생각 이상으로 빠르고 강했다.

“탄지공(彈指公)이다!”

진위경의 외침. 내게 탄지공이 뭔지 생각할 시간 따위는 주어지지 않았다.

퍼버버벅!

카앙!

“크아아악!”

“커흑!”

누군가는 쓰러지고, 누군가는 튕겨 냈다. 그러나 쓰러진 자들은 다시 일어나지 못했다.

‘저거 설마…….’

짧은 순간이었지만 똑똑히 볼 수 있었다. 그들의 심장 어림과 얼굴에 산탄처럼 빼곡히 박히는 작은 점들을.

‘돌?’

지금은 파편에 가깝지만, 그건 분명히 돌이었다. 대장로의 공력을 견디지 못한 돌이 박살 남과 동시에 우리를 향해 쏘아진 것이다.

‘이게 가능해?’

소름이 돋았지만 아직 끝난 게 아니었다.

대장로가 이쪽으로 손을 내뻗고 있었다.

“산개!”

이번에는 나와 진위경이 동시에 외쳤다. 안 그래도 잔뜩 경계 중이던 무인들이 순식간에 뿔뿔이 흩어졌다.

‘됐어. 이번에는 안 늦었……!’

그러나 안도감도 잠시.

쐐애애액!

탄지공 대신 쏘아진 것은 대장로였다. 무인들 사이로 파고든 그는 맹수처럼 날뛰었다.

서걱, 서걱, 서걱.

“크르륵.”

“헉.”

어둠 사이로 검이 번뜩일 때마다 하나의 목숨이 스러진다. 대장로가 휩쓸고 지나간 자리마다 숨죽인 비명과 시체만이 남겨졌다.

“대장로-!”

분노한 진위경이 달려들었을 때, 대장로는 다섯 명을 해치운 후였다. 그런데도 피 한 방울 묻지 않은 흰 얼굴은 귀신을 연상시켰다.

“왔느냐?”

“감히!”

“다들 서투르구나. 평화가 너무 길었던 모양이야.”

단 하나, 부정할 수 없는 사실이 있다. 대장로가 정마대전의 영웅이라는 것.

그는 이 자리의 그 누구보다 강하고, 노련한 사람이다. 수많은 실전을 통해 완성된 절정의 무인인 것이다.

쉬이이익!

진위경이 뽑아낸 검기가 허공을 찔렀다. 단순히 고개를 까딱이는 것만으로 공격을 피해 낸 대장로는 손가락을 튕겼다.

목표는 바로 나였다.

쉭!

아무것도 보이지 않는다. 하지만 본능적으로 알아챘다.

‘공력.’

저건 말 그대로 기(氣)의 덩어리, 그 자체다. 나는 지체하지 않고 몸을 굴렸다.

푸슉.

“컥.”

창으로 막았어야 했는데, 거기까지 생각하기에는 너무나 생소한 공격이었다. 그 대가는 이름 모를 아군의 죽음.

기분이 더러웠다.

“나려타곤? 당나귀 같은 놈이구먼.”

나는 입 안에 들어간 흙을 퉤 뱉었다.

“살고 싶으면 뭔 짓을 못 해.”

“하하, 벌써 무림인이 다 됐구나.”

캉! 카카캉!

저런 괴물을 봤나. 말하는 와중에도 진위경의 검기를 모조리 튕겨 내는 대장로의 모습에 기가 막힐 따름이다.

퍽!

그 순간에도 공력을 실어 휘두른 주먹이 그의 등을 노리고 달려든 무인의 머리통을 박살 냈다.

“아직 이십 년은 이르다.”

전투를 시작한 지 얼마 되지도 않았는데, 차 한 잔 마실 시간조차 지나지 않았는데 벌써 스물에 가까운 무인들이 싸늘한 시신으로 변했다.

“이놈!”

쉬이익!

어딘가 눈에 익은 중년 무사는 검기에 목이 달아났고.

“죽어엇!”

펑!

스무 살이나 됐을 법한 앳된 얼굴의 청년은 가슴이 움푹 꺼져 무릎을 꿇었다. NPC가 아닌 진짜 사람들.

태원진가에서 한 번쯤 마주치고, 악수를 나눴던 그 얼굴들이다. 그 사실에 나는 이를 악물었다.

‘미안합니다.’

막을 힘이 없어서 미안한 것이 아니다. 그들을 죽음을 이용했기 때문에 하는 사과였다.

쉭!

대장로의 탄지공에 또 한 사람이 실 끊긴 인형처럼 쓰러진다. 그러나 금방이라도 뒤로 넘어갈 것 같던 시체는 오뚝이처럼 일어났다. 이어 대장로에게로 고꾸라졌다.

“허튼수작!”

쾅! 펑!

대장로는 한 손으로는 진위경의 검을, 다른 한 손으로는 시신을 향해 장력을 날렸다.

그리고…….

‘지금.’

훨훨 날아가는 시신의 뒤로 모습을 숨겼던 내가 창을 뻗었다.

“일섬.”

다음 순간.

고오오옹.

귀가 먹먹해지는 굉음이 있었다.
```

## Current accepted English baseline

```markdown
# Chapter 60

The Head Elder thought,

*Have I lived too long?*

The Murim he remembered was not like this. Martial artists were not like this.

Ganging up was shameful, ambushes were condemned, and anyone who got so much as dirt on their back became a laughingstock.

And yet…

“Throw dirt! Keep throwing it!”

In eighty years of life, he had never seen anything like this. What? Throw dirt?

It was a cheap, cowardly trick even the Demonic Cultists he had fought like sworn enemies decades ago had never used.

*Is that bastard really a martial artist?*

What left him even more speechless was the reaction of those so-called subordinates.

“Squad Leader’s orders! Throw dirt!”

“Open the distance! Watch the Sword Energy!”

Watching them obey without a word made him dizzy.

*Have I ever seen bastards this fit to die?*

These were not martial artists.

No, they were not even human.

This was an insult to martial artists—and an insult to the Head Elder himself, who had given his whole life to the sword.

“How dare you…”

He was drawing his sword when it happened.

“You idiots!”

A stern shout burst out half a beat sooner. A young man whose face was swollen as if bees had stung him swept a fierce look around them.

“What the hell do you think you’re doing?”

He looked ridiculous, but he had real mettle. Yes. That was how a martial artist was supposed to act.

*At least there’s one decent one here.*

The Head Elder was just nodding to himself when—

“Think dirt’s going to cut it? Mix in rocks too!”

“…!”

The Head Elder shuddered like a man struck by lightning.

In a humiliation he had never felt in his life, he even forgot to swing his sword as a clod of dirt flew at his face.

Splat!

He could say this without hesitation: looking back on eighty years, he had never taken a hit so humiliating, or so completely undefended.

Through the dirt pattering down, he spotted a chunk of stone mixed in nice and solid.

“Uh-heh, uh-heh-heh-heh.”

The Head Elder laughed like a madman.

Then the laugh cut off.

At the same time—

Tssssss.

Sword Energy surged up, loaded with sixty years of internal energy.

“Are you prepared?”

Jin Taekyung watched and muttered,

“Shouldn’t have mixed in the rocks…”

The words were barely out before the Head Elder charged like a lion. The dozen or so sheep screamed and scattered.

“Scatter! Scatter!”

“Throw dirt too!”

Even while they ran, they did not forget to throw dirt.

* * *

Fwoooosh—

A fierce gale tore from the tip of the Head Elder’s sword. Sand, dirt, stones—whatever it was, it made no difference. In the face of that much power, it only shattered and scattered.

*How are we supposed to fight this guy?*

A head-on fight?

Calling us melee damage dealers was putting it nicely. Leave the reconnaissance squad on the Head Elder and they’d be dying in piles before I could blink.

I’d gotten attached to the bastards, though. I couldn’t let them die a pointless dog’s death.

“Squad Leeeader!”

That one deserved to die, sure.

*So why mix in rocks? The rocks.*

The Head Elder’s first target was Hyuk Mujin. Naturally. He’d thrown the first punch without a shred of fear.

I let out a long breath and threw myself toward him.

Shiiiiing!

I drove my spear at the Head Elder’s chest with everything I had.

At the same time, the Sword Energy about to cut through Hyuk Mujin’s back changed direction.

Shing.

That damned Sword Energy.

No time to check the spearhead, sliced off clean. I snatched terrified Hyuk by the scruff of the neck.

“Run!”

But the Head Elder was not the type to let go.

Swoooosh!

A tearing whistle through the air, and my side went hot. Even a graze ripped out a handful of flesh and sent blood spraying.

*Kh.*

It hurt like hell. In this situation, though, even a scream was a luxury.

*I need to buy time.*

I shoved Hyuk aside and turned. The Head Elder raised an eyebrow at that.

“You?”

Only one word, but the meaning came through perfectly. *The likes of you, stopping me?* That was the idea.

I answered like I was calm.

“Yeah. Me.”

“Don’t you value your life?”

“If I say it’s damn precious, will you let me live?”

“Heh heh. Look at this one. Young as you are, you’ve got quite a mouth.”

“Gramps, does your pepper still stand?”

Tssssss.

It stood ramrod straight.

Large, beautiful Sword Energy.

“…You’re still going strong.”

My grip on the spear went slick with sweat.

*I’m going to have to shake out every last reserve I’ve got to survive this.*

I had a lot more secrets than the Head Elder knew.

Attacks that used my Inventory.

A Skill that dumped several times my strength into a single blow—One Flash.

*I never showed them, just in case something like this happened.*

Was this what they called a last-resort technique in Murim?

One thing was certain: neither the Head Elder nor anyone else in Murim would see it coming.

And on top of that…

“Encircling formation. Form up.”

Shff.

Hyuk Mujin and the reconnaissance squad began closing in from every side.

A flimsy net for a fish as big as the Head Elder.

But with a sharp harpoon, it was a fight we could try.

“You think this will be enough?”

“To catch one old man? This is plenty.”

The Head Elder smiled like he was entertained.

“What a fearless brat. The kind who only comes to his senses after a beating.”

But that wish of his did not come true. A voice cut in out of nowhere.

“I think I heard you wrong. Say that again.”

A mountain of a man with fierce, piercing eyes. The voice from between his thick lips was cold as ice.

“You were going to lay a hand on our boy?”

Fwoooosh.

Sword Energy climbed his blade like wildfire and pointed at the Head Elder.

Jin Wikyung, appearing like a savior, winked at me.

“Well? Big brother looks cool, doesn’t he?”

Still the same.

* * *

The first time I had seen that face in a month.

The moment Jin Wikyung appeared, the tension in my body melted away.

I was glad.

Just glad.

*Thank goodness he’s alive.*

Wikyung was covered in blood, like he’d just come through a brutal fight. Large and small wounds showed through the tears in his clothes.

But that was enough. The fact that he was alive was what mattered.

*I have a lot I want to say, but it can wait.*

A reunion after this war ended would not be too late. Wikyung seemed to think the same. He looked forward.

Where we were looking, the Head Elder slowly spoke.

“The fact that you made it this far means…”

Jin Wikyung’s chilly voice cut him off.

“The Second and Third Elders are dead. The First Elder is only a matter of time.”

Good news. If Wikyung put it that way, the Elders had been no small part of this war—and the Head Elder’s hands and feet had just been cut off.

“Did the two of them… go peacefully?”

“Probably.”

The Head Elder nodded readily.

“They were always saying they wanted to die fighting like martial artists. They got their wish, so that’s fortunate.”

“They’ll be remembered as traitors, not martial artists. Every last one of you.”

“History is written by the victors.”

The Head Elder pointed his sword at us. Even with dozens of people in front of him, including me and Jin Wikyung, he stood there utterly composed.

“Now, let’s see who the victor is.”

Jin Wikyung looked like he had something to say. His mouth opened, then shut tight.

The next moment, a thunderous roar burst from him.

“Strike down the rebels!”

Shing. Shrrring.

Dozens of weapons drawn at once, all aimed at a single man. It was quite a spectacle.

“Yes, sir!”

With a huge shout, dozens of martial artists charged as one mass. I was no exception. My grip tightened on the spear, and my chest felt ready to burst.

*We can win. No. We win, no matter what.*

A full-on brawl with no formation to speak of. But we had Jin Wikyung, a Peak master, and dozens of martial artists following him.

*And there’s me.*

The Head Elder had trusted his own strength too much. He had thrown every man into the front line without leaving even a minimal escort, and now the black-clad men were pinned down by the combined assault of the Jin Family of Taiyuan and the Mount Heng Sword Sect.

The Head Elder…

dies right here.

*It’s over!*

It did not take long for that certainty to shatter to pieces.

Shushushushush!

Dozens of tiny points shot out of nowhere. They cut through the air faster and harder than anyone had expected.

“Finger-Flicking Technique!”

Jin Wikyung’s shout. I was not given time to think about what that even was.

Pow-pow-pow-pow!

Clang!

“Aaargh!”

“Guh!”

Some went down. Others knocked the shots aside. The ones who fell did not get up again.

*Don’t tell me…*

It had lasted only an instant, but I saw it clearly. Tiny points packed into the area around their hearts and across their faces like buckshot.

*Stones?*

They were closer to fragments now, but they had definitely been stones. Stones that could not take the Head Elder’s internal energy had shattered as they were fired at us.

*Is this possible?*

I got goose bumps, but it was not over.

The Head Elder was stretching a hand this way.

“Scatter!”

This time Wikyung and I shouted together. The martial artists, already wound tight, scattered in an instant.

*Good. We weren’t late this ti—*

The relief lasted only a moment.

Swoooosh!

What shot at us this time was not the Finger-Flicking Technique. It was the Head Elder. He drove in among the martial artists and went berserk like a wild beast.

Slash. Slash. Slash.

“Grrk.”

“Hhk.”

Every time a sword flashed through the dark, another life went out. Wherever the Head Elder tore through, only stifled screams and corpses were left.

“Head Elder—!”

Jin Wikyung charged in a fury. By then the Head Elder had already finished five people. And still not a drop of blood on that white face, enough to make you think of a ghost.

“You’ve come?”

“How dare you!”

“You’re all clumsy. Peace must have lasted too long.”

There was one fact you could not deny. The Head Elder was a hero of the Great Faction War.

He was stronger and more seasoned than anyone here. A Peak martial artist finished in countless real fights.

Shiiiiing!

The Sword Energy Jin Wikyung drew out stabbed through empty air. The Head Elder slipped it with nothing more than a slight tilt of his head, then flicked a finger.

The target was me.

Shhk!

I could not see a thing. Instinct knew anyway.

*Internal energy.*

That was literally a lump of qi itself. I rolled without wasting a beat.

Pshk.

“Guh.”

I should have blocked with the spear, but the attack was too unfamiliar to think that far. The price was an unnamed ally’s death.

I felt rotten.

“Naryeotagon? What a donkey of a man.”[^1]

I spat out the dirt that had gotten in my mouth.

“If you want to live, what won’t you do?”

“Haha. You’ve already become a proper man of Murim.”

Clang! Clang-clang-clang!

Had anyone ever seen a monster like that. Even while talking, he knocked aside every last bit of Jin Wikyung’s Sword Energy. I was speechless.

Thud!

Even then, a fist loaded with internal energy smashed the skull of a martial artist who’d gone for his back.

“You’re still twenty years too early.”

The fight had barely started. Not even the time to drink a cup of tea had passed, and already nearly twenty martial artists had turned into cold corpses.

“You bastard!”

Shiiiiing!

A middle-aged warrior whose face looked vaguely familiar lost his head to Sword Energy.

“Die!”

Boom!

A young man with a baby face that might have been twenty had his chest caved in and dropped to his knees.

Not NPCs. Real people.

Faces I had run into at least once at the Jin Family of Taiyuan. Faces I had shaken hands with. I gritted my teeth at that.

*I’m sorry.*

I was not apologizing because I lacked the power to stop it. I was apologizing because I had used their deaths.

Shhk!

Another person dropped to the Head Elder’s Finger-Flicking Technique like a puppet with its strings cut. But the corpse that looked about to topple backward popped up like a roly-poly toy. Then it pitched toward the Head Elder.

“Cheap trick!”

Boom! Bang!

With one hand, the Head Elder took Jin Wikyung’s sword. With the other, he sent a palm strike at the corpse.

And then…

*Now.*

I had hidden behind the corpse as it sailed through the air. I thrust my spear.

“One Flash.”

The next instant—

Goooooong.

There was a roar that stuffed the ears.

[^1]: *Naryeotagon* is a martial-arts term for dropping and rolling on the ground to evade an attack; the Head Elder’s remark also compares Taekyung to a donkey.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 60`.

# Master Edit Task — Chapter 61

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
| 진무경    | **Jin Mukyung**    |
| 조필     | **Jopil**          |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 무림맹    | **Murim Alliance**               |
| 산서오문   | **Five Gates of Shanxi**         |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 초식     | **form**                                         | Numbered technique movement                           |
| 영약     | **elixir**                                       |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 마교     | **Demonic Cult**                                 |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 팔천협    | **Eight Spring Gorge** |
| 정마대전   | **Great Faction War**         |

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

#### Chapter 59 tail (verified mastered)

…
Mount Heng Sword Sect!” “I don’t know where you crawled out from, but wipe them all out!” Once the two forces joined up, it was the black-clad men who started to give ground. They were elites hardened by brutal training, but the deaths of the two Elders inevitably shook their morale. Blades poured in from every direction, exploiting every opening, and the black-clad men began to fall one after another. “Aaargh!” “Don’t fall back! Anyone who falls back dies!” Even amid the chaos, the First Elder silently swung his sword. Everything his eyes fell on, everything his hands reached toward, was an enemy. Shhk. Twenty? Thirty? He had lost count. Like a man possessed, the First Elder cut down everything in his path. Among his victims were men who had once addressed him with respect, as well as youths who looked barely twenty. *What does age matter to living and dying? Anyone who stands at the point of a sword is a person of Murim.* What blocked the First Elder, drenched in the blood of dozens, was a man built like a bear. His eyes looked ready to burn everything to ash. “Why did you do it?” “Wealth and glory. To seize the Jin Family of Taiyuan and swallow Shanxi whole.” The answer came without a hint of hesitation, and everyone trembled with rage. Everyone except one. Jin Wikyung shook his head. “That isn’t the answer I wanted.” “Then you answer, Lesser Family Head. Why would I, my brothers, and our lord do a thing like this?” “Revenge.” Jin Wikyung continued in a low voice. “The grand plan you talked about wasn’t for wealth and glory, or to become the ruler of a single province. Too many chances for that have already passed, and you’re all old. And…” “Enough.” “The Head Elder has no descendants. Neither do the Second Elder, the Third Elder, or you.” In that instant, a livid spark leapt from the First Elder’s still eyes. It was anger he had held down for a very long time—dregs that rose for the briefest moment, then sank again. “Why did you do it?” Instead of answering, the First Elder raised his sword and pointed it at Jin Wikyung. No—the tip pointed past Jin Wikyung’s shoulder, toward someone somewhere beyond him. “Hear it from him yourself.” In the end, the last key was in the Head Elder’s hands. Jin Wikyung took a long stride toward the First Elder. “I will. After I cut you down.” “Well? Can you really afford to take it this easy?” “What do you—” Jin Wikyung’s frown went rigid. *Taekyung!* His youngest brother, the apple of his eye, was standing in the Head Elder’s way. The instant he remembered the fact that had briefly slipped his mind, his blood seemed to turn cold. *If I delay any longer, something irreversible will happen.* Once he grasped the whole situation, a voice like frost burst from Jin Wikyung’s mouth. “Wipeng. Take care of the First Elder.” “I obey.” “The rest of you, lend him your strength.” “We follow the Lesser Family Head’s command.” Wipeng and some ten surviving senior members spread into a wide ring around the First Elder. “Everyone else, follow me and open a path! We’re going after the Head Elder!” Jin Wikyung was about to move with several dozen guards when he glanced at the First Elder. Even with his end closing in, the man showed no agitation. If anything, he looked unburdened. “First Elder.” “Do you have something left to say?” Jin Wikyung tossed out a single line. “By the authority vested in me as Lesser Family Head of the Jin Family of Taiyuan, I expel you from the family.” “Heh heh. Heh heh heh!” Leaving the First Elder’s laughter behind him, Jin Wikyung sprinted for the battlefield. Dozens of black-clad men tried to stop him, but the battle had long since turned against them. Martial artists converged from every direction and hacked them to pieces. “Open a path!” “It’s the Lesser Family Head! Kill anyone who gets in his way!” It was only a moment. For Jin Wikyung, an eternity passed. *Taekyung. Please, please…* He could not even bring himself to think the word *death*. How long had he run, clutching his pounding heart? When he finally reached his destination, his eyes flew wide. *What is this…* The scene in front of him was shock itself. * * * Raid. Until a few decades ago, it was a word that only meant anything in games. But after the Demon King appeared and the Great Cataclysm began, raids became the symbol of Hunters. Getting there had taken countless real battles and countless sacrifices. On that foundation, the raid methods used today had finally been set down. *Tank, damage dealer, healer.* The tank blocks. The damage dealer hits. The healer heals. It sounded simple, but to become a proper Hunter you had to study a mountain of raid manuals and prove yourself in actual combat. *Hunter training camp… that was a living hell.* But enduring it was what made me a Hunter. Now, as a seven-year veteran, I could come up with the right positions and response for any situation. And right now— “Hey, throw dirt! Keep throwing!” I realized that everything I’d learned wasn’t worth shit. Tank? Healer? Fuck… I was a fucking moron for thinking ten melee damage dealers counted as a raid.

#### Chapter 60 tail (accepted)

…
Shing. Shrrring. Dozens of weapons drawn at once, all aimed at a single man. It was quite a spectacle. “Yes, sir!” With a huge shout, dozens of martial artists charged as one mass. I was no exception. My grip tightened on the spear, and my chest felt ready to burst. *We can win. No. We win, no matter what.* A full-on brawl with no formation to speak of. But we had Jin Wikyung, a Peak master, and dozens of martial artists following him. *And there’s me.* The Head Elder had trusted his own strength too much. He had thrown every man into the front line without leaving even a minimal escort, and now the black-clad men were pinned down by the combined assault of the Jin Family of Taiyuan and the Mount Heng Sword Sect. The Head Elder… dies right here. *It’s over!* It did not take long for that certainty to shatter to pieces. Shushushushush! Dozens of tiny points shot out of nowhere. They cut through the air faster and harder than anyone had expected. “Finger-Flicking Technique!” Jin Wikyung’s shout. I was not given time to think about what that even was. Pow-pow-pow-pow! Clang! “Aaargh!” “Guh!” Some went down. Others knocked the shots aside. The ones who fell did not get up again. *Don’t tell me…* It had lasted only an instant, but I saw it clearly. Tiny points packed into the area around their hearts and across their faces like buckshot. *Stones?* They were closer to fragments now, but they had definitely been stones. Stones that could not take the Head Elder’s internal energy had shattered as they were fired at us. *Is this possible?* I got goose bumps, but it was not over. The Head Elder was stretching a hand this way. “Scatter!” This time Wikyung and I shouted together. The martial artists, already wound tight, scattered in an instant. *Good. We weren’t late this ti—* The relief lasted only a moment. Swoooosh! What shot at us this time was not the Finger-Flicking Technique. It was the Head Elder. He drove in among the martial artists and went berserk like a wild beast. Slash. Slash. Slash. “Grrk.” “Hhk.” Every time a sword flashed through the dark, another life went out. Wherever the Head Elder tore through, only stifled screams and corpses were left. “Head Elder—!” Jin Wikyung charged in a fury. By then the Head Elder had already finished five people. And still not a drop of blood on that white face, enough to make you think of a ghost. “You’ve come?” “How dare you!” “You’re all clumsy. Peace must have lasted too long.” There was one fact you could not deny. The Head Elder was a hero of the Great Faction War. He was stronger and more seasoned than anyone here. A Peak martial artist finished in countless real fights. Shiiiiing! The Sword Energy Jin Wikyung drew out stabbed through empty air. The Head Elder slipped it with nothing more than a slight tilt of his head, then flicked a finger. The target was me. Shhk! I could not see a thing. Instinct knew anyway. *Internal energy.* That was literally a lump of qi itself. I rolled without wasting a beat. Pshk. “Guh.” I should have blocked with the spear, but the attack was too unfamiliar to think that far. The price was an unnamed ally’s death. I felt rotten. “Naryeotagon? What a donkey of a man.”[^1] I spat out the dirt that had gotten in my mouth. “If you want to live, what won’t you do?” “Haha. You’ve already become a proper man of Murim.” Clang! Clang-clang-clang! Had anyone ever seen a monster like that. Even while talking, he knocked aside every last bit of Jin Wikyung’s Sword Energy. I was speechless. Thud! Even then, a fist loaded with internal energy smashed the skull of a martial artist who’d gone for his back. “You’re still twenty years too early.” The fight had barely started. Not even the time to drink a cup of tea had passed, and already nearly twenty martial artists had turned into cold corpses. “You bastard!” Shiiiiing! A middle-aged warrior whose face looked vaguely familiar lost his head to Sword Energy. “Die!” Boom! A young man with a baby face that might have been twenty had his chest caved in and dropped to his knees. Not NPCs. Real people. Faces I had run into at least once at the Jin Family of Taiyuan. Faces I had shaken hands with. I gritted my teeth at that. *I’m sorry.* I was not apologizing because I lacked the power to stop it. I was apologizing because I had used their deaths. Shhk! Another person dropped to the Head Elder’s Finger-Flicking Technique like a puppet with its strings cut. But the corpse that looked about to topple backward popped up like a roly-poly toy. Then it pitched toward the Head Elder. “Cheap trick!” Boom! Bang! With one hand, the Head Elder took Jin Wikyung’s sword. With the other, he sent a palm strike at the corpse. And then… *Now.* I had hidden behind the corpse as it sailed through the air. I thrust my spear. “One Flash.” The next instant— Goooooong. There was a roar that stuffed the ears. [^1]: *Naryeotagon* is a martial-arts term for dropping and rolling on the ground to evade an attack; the Head Elder’s remark also compares Taekyung to a donkey.

## Korean source

```text
＃61화



고오오옹.

대장로는 공기의 떨림을 느꼈다. 동시에 자신의 가슴을 향해 쏘아지는 창날이 어떤 파괴력을 지녔는지도 깨달았다.

‘이건…… 위험하다.’

살면서 몇 번 느껴 보지 못한 생명의 위협. 전신의 털이 바짝 곤두서고, 세상이 느려진다.

쉬이익!

정면에는 진태경의 창이, 등 뒤에서는 진위경의 검이 날아든다. 두 형제의 연수합격은 절묘하게 맞아떨어졌다.

그야말로 절체절명의 순간.

솨아아.

대장로의 단전에 웅크리고 있던 일 갑자의 공력이 전신 사지백해로 뻗어 나갔다. 노쇠한 근육에 활력을 불어넣고 혈맥을 깨웠다. 변화는 거기에서 그치지 않았다.

츠츠츠.

한 자(30cm) 가까이 솟구쳤던 검기가 절반으로 압축되었다.

그러나 그것은 힘의 감소가 아닌, 힘의 응축이었다. 실처럼 하늘거리던 검기는 검신 전체를 휘감으며 또 다른 검의 형태를 갖췄다.

검강(劍强).

절정이라는 벽을 넘어 위대한 영역을 개척한 초인들의 상징.

아직 불완전한 반쪽짜리에 불과했으나 그것은 분명 검강이었고, 대장로가 평생을 익혀 온 무학(武學)의 결정체였다.

서걱.

태원진가 대대로 내려져 오는 가문의 보검조차 검기를 두른 채로 잘려 나갔다. 한순간에 공력이 흩어지고 내부가 진탕된 진위경의 얼굴이 창백하게 변했다.

일 검이면 그의 목을 취할 수 있는 상황.

그러나 대장로에게는 그럴 만한 시간이 없었다.

쐐액!

대장로는 가슴 앞까지 다가온 창으로 손을 뻗었다. 그의 주름진 손 역시 눈부신 기의 빛무리에 휩싸여 있었다.

이 역시 불완전한 수강(手强)이었으나 진태경의 창을 멈춰 세우기에는 충분했다.

아니, 충분해 보였다.

콰아아아아.

창끝에서 흘러나온 와류(渦流)가 그를 집어삼키기 전까지는.



* * *



죽음 같은 정적이 내리깔렸다. 이 자리에 있는 수십, 어쩌면 전장에 선 모두가 우리를 지켜보고 있는 것 같았다.

아니, 우리가 아니다. 오직 한 사람이다.

“이게…….”

수많은 시선 끝에서, 대장로가 천천히 입을 뗐다.

“무슨 초식이지?”

내가 대답했다.

“일섬.”

말하는 것만으로도 극심한 허기가 느껴진다. 전신의 근육이 찌릿했고 체내에는 공력 한 줌 남아 있지 않았다.

하지만 딱 그 정도다. 나는 조필 때처럼 기절하지도, 꼴사납게 주저앉지도 않았다.

‘이제는 몸이 감당할 수 있다.’

나는 일섬의 부작용을 감당할 수 있을 만큼 성장했고, 내가 성장한 만큼 일섬의 위력도 강해졌다.

지금 대장로의 모습이 바로 그 증거다.

“일섬, 일섬이라.”

작게 중얼거린 그가 어깨의 혈도를 짚었다.

흐르던 피는 멈췄지만, 그뿐. 일섬이 뿜어낸 와류에 의해 흔적도 없이 갈려 나간 팔은 돌아오지 않았다.

“이 나이에 외팔이가 될 줄은 몰랐는데. 허허.”

허탈하게 웃은 대장로가 진위경을 향해 고개를 돌렸다.

“무서운 아우를 뒀구나.”

진위경이 파리한 얼굴로 되물었다.

“당신은 저 아이가 무섭소?”

“너는 어떠하냐?”

“자랑스럽소.”

한 치의 망설임도 없는 대답. 그의 창백한 안색 위로 웃음이 피어올랐다.

“금이야 옥이야 키웠는데 강철로 자랐지. 태경이는 그런 아이요.”

대장로는 그 미소를 물끄러미 바라보았다.

“너는 제법 괜찮은 인재다. 태원진가의 미래를 책임질 만한.”

“그렇소?”

“허나, 네 아우들만큼은 아니지.”

약관에 절정의 경지에 도달했다는 진무경이야 그렇다 치고, 나까지 높게 쳐 주니 황송하긴 한데…….

‘도대체 무슨 말을 하려고?’

내 생각을 읽은 듯 대장로가 말을 이었다.

“핏줄과도 나누지 않는 것. 그게 바로 권력이다. 그때가 되어도 네 아우들이 마냥 자랑스러울까?”

순식간에 장내가 싸늘하게 식었다.

지금 근거리에서 대장로와 대치하고 있는 이들은 전부 태원진가 소속. 조심스러운 시선들이 내 뺨에 달라붙었다가 슬그머니 사라진다.

‘가주? 그딴 거 할 생각도 없다. 이놈들아.’

그때였다. 진위경이 입을 뗀 것은.

“그랬구려.”

착잡함과 후련함이 묻어 나오는 목소리였다. 대장로의 눈썹이 꿈틀거린다.

“무엇을 말이냐?”

“당신이 배반한 이유. 오늘 같은 일이 일어난 이유.”

“……!”

대장로의 떨리는 눈동자가 대답을 대신했다. 나는 내심 한숨을 내쉬었다.

‘결국 그거였나.’

후계자 싸움.

커다란 퍼즐 조각이 맞춰진 기분이다. 아직 제자리를 찾지 못한 작은 조각들은 그들의 대화를 통해 하나둘씩 맞춰지고 있었다.

“무슨 일이 있었습니까?”

진위경이 공손한 말투로 물었다.

이 자리의 누구도 알아차리지 못할 만큼 자연스러운 변화였다.

“네 조부에 대해 아느냐?”

“들은 바가 없습니다. 아버님께서도 일언반구 없으셨지요.”

“냉혹한 사람이었다. 자식에게도, 하나뿐인 아우에게도. 그리고…….”

대장로는 피식 웃었다.

“소인배였지. 여러 이유로 한때 의좋은 형제였던 우리는 점차 멀어졌다. 그러던 와중에 그 일이 터진 거지.”

“정마대전.”

“십만마도(十萬魔度)라는 말을 아느냐? 그들은 끝없이 밀려왔다. 무림맹이 결성되었지만 구파일방의 연합에 불과했고, 제 근거지를 지키기에 바빴지.”

대장로가 본격적으로 이름을 떨치기 시작한 것도 그때였다.

그는 태원진가의 깃발 아래 산서성 무인들을 결집시켰고, 마침내 마교의 군세를 몰아냈다.

“바로 이곳, 팔천협에서 마지막 전투가 있었다.”

그의 시선이 먼 과거 어딘가를 더듬는 듯했다.

“긴 전쟁이었다. 많은 이들이 죽었고, 모두가 지쳐 있었지. 그러나 희망도 있었다. 이제 가족들의 품으로 돌아갈 수 있다는 희망. 삼백 명의 결사대가 같은 마음이었다.”

“결국 대승을 거두셨지요.”

삼백 대 삼천의 싸움. 결과는 마교의 전멸.

위대한 승리였고, 대장로가 지금까지 기억되는 이유기도 했다. 모두가 그 사실을 믿어 의심치 않았다.

적어도 방금까지는.

“매복이 있었다.”

뭐?

“협곡 깊숙한 곳까지 물러서며 싸웠지만 중과부적이었지. 미친 듯이 검을 휘두르면서도 한 가지 의문이 떠나지 않았다.”

이어지는 대장로의 목소리는, 소름 끼치도록 잔잔했다.

“어떻게 놈들이 미리 매복할 수 있었을까? 팔천협으로 오는 길은 형님이 막고 있을 터인데.”

“……!”

사람들 사이로 소리 없는 경악이 퍼져 나갔다. 가뜩이나 창백하던 진위경의 얼굴에선 아예 핏기가 사라졌다.

“전투는 반나절 동안 이어졌다. 오지 않는 지원군을 기다리며 싸웠지만 허사였지. 삼백의 결사대 중 생존자는 고작 여덟. 마침내 가문에 귀환했을 때, 나를 보던 형님의 표정을 잊을 수가 없다.”

“그게…… 사실입니까?”

“강산이 몇 번은 바뀌었을 시간이다. 단순한 의심으로 여기까지 왔을 거라 생각했느냐?”

수십 년의 세월은 의심을 확신으로 바꾸기에 차고 넘치는 시간이다. 대장로가 허탈하게 웃었다.

“형님은 전쟁을 기회로 만들었다. 나는 전장에서 영웅이 되었지만 그는 가주가 되었지. 나를 따르던 사람들은 모두 전장에서 죽거나 실종된 후였다.”

“그렇다면 곧장 장로원에 들어간 것도?”

“그래야 안심할 테니까. 그래야 나와 내 사람들의 목숨을 부지할 수 있었을 테니까.”

내 사람들?

앞서 그가 했던 말을 떠올렸다. 대장로를 따라 최후에 살아남은 여덟 명의 생존자. 그들의 정체를 유추하는 것은 그리 어렵지 않았다.

‘장로들과 산서오문의 문주들.’

살아남은 자들은 복수를 다짐했다. 자신들을 배신한 가주와 가문에 대한 복수였다. 대장로는 좌중을 천천히 쓸어 보았다.

“실로 오랜 기다림이었다.”

사람들은 침묵에 휩싸였다. 불신, 충격, 부끄러움. 감정은 제각각이었지만 아무도 쉽게 입을 떼지 못했다.

아, 물론 나는 제외지.

“개소리를 길게도 하네.”

“……!”

피식피식 새어 나오는 웃음을 참을 수 없다.

무슨 얘기까지 나오나 쭉 들어 봤는데, 이건 뭐.

“결국 목적은 하나잖아.”

나는 대장로를 향해 엄지를 까딱였다.

“복수고 자시고, 당신이 이거 되려는 거, 아냐?”

“뭐라?”

“맞잖아. 태원진가와 항산검문. 방해되는 거 싹 다 치워 버리고 산서성 꿀꺽하려는 거.”

“이놈-!”

노인네가 기차 화통을 삶아 먹었나. 아, 여기엔 기차가 없구나.

“복수? 좋지. 다 좋은데…….”

나는 귀를 후비적거리며 말을 이었다.

“그 복수를 왜 지금에 와서 해?”

자그마치 40년 전의 일이다. 대장로의 나이를 생각해도 반평생을 기다린 거다.

“당신 뒤통수쳤던 인간들이 지금 몇 명이나 살아 있는데? 뒷북도 정도껏 쳐야지. 아, 이건 제발 부탁인데, 군자의 복수는 십 년을 어쩌고 하는 개소리는 하지 마시고.”

10년 참았다고 군자면, 40년 참은 대장로는 예수냐?

그저 정신 나간 노인네의 자기 합리화에 지나지 않는다.

“뚫린 입이라고 말을 함부로 하는구나.”

“함부로 했다. 어쩔래?”

“네가 모든 걸 알고 있다고 생각하느냐?”

“꼭 알아야 하나? 이렇게까지 된 마당에?”

뻔한 물음에 어이가 없어 피식 웃으며 전장을 가리켰다. 시산혈해, 아비규환. 말 그대로의 광경이 눈앞에 있었다.

“그건…….”

서늘하던 대장로의 눈빛이 흔들린다. 하지만 찰나에 불과했다.

“그렇군. 무슨 말이 더 필요할까.”

자조하듯 중얼거린 그가 검을 들어 올렸다.

“대장로.”

진위경은 입술을 달싹였지만 딱 거기까지였다.

어느 한쪽이 죽어야 끝나는 싸움. 돌이키기에는 너무 멀리 와 버렸다.

“오너라.”

사양할 내가 아니었다.

“쳐!”

이제 상처 입은 맹수를 사냥할 시간이다.



* * *



대장로를 처음 본 날이 생각난다. 나이가 무색할 만큼 당당한 풍채와 위엄. 백발의 수염은 신선을 연상시켰다.

푸화악!

물론 가차 없이 사람을 반쪽 내는 신선은 없겠지만.

‘썩어도 준치라더니.’

피를 뒤집어쓴 채 쉴 새 없이 검을 휘두른다. 그런 그를 향해 경외와 두려움 섞인 시선이 쏟아졌다.

“괴물…….”

한쪽 팔을 잃었지만 대장로는 여전히 강했다. 그러나 분명 예전만큼은 아니었다.

‘해볼 만해.’

아무리 대장로가 절정 고수라지만 이 자리의 무인들 역시 태원진가의 정예다. 진위경을 따라 전장을 누비고, 앞선 대장로와의 전투에서 살아남을 만큼의 실력자들.

따다당!

사방에서 짓쳐 드는 검날을 튕겨 낸 대장로의 안색은 어두웠다. 예전 같았다면 검기로 가로막는 모든 걸 베었을 것이다.

마르지 않는 샘 같던 공력이 바닥을 드러냈다는 증거다.

거기에 늙어 버린 육체가 한계에 도달하기까지 했다.

촤아악.

대장로의 몸에 점차 검상이 늘기 시작했다. 지금까지와는 달리 대부분이 그의 피였다.

‘지금!’

그 틈을 놓칠 내가 아니다. 힘껏 내지른 창이 그의 옆구리 살을 한 움큼 뜯어냈다.

“흡!”

고통을 느끼는 와중에도 무인 하나를 베어 낸 대장로가 나를 향해 달려들었다. 제대로 작심한 듯, 휘둘러지는 검에는 미약한 검기가 맺혀 있었다.

하지만…….

서걱.

솟구치는 피보라와 함께 검기가 흩어졌다. 비틀거리는 그의 등 뒤로 진위경이 모습을 드러냈다.

“널 잊고 있었구나.”

대장로가 일그러진 얼굴로 돌아섰다.

“등에 칼을 꽂는 것은 형님에게 배웠느냐?”

“식솔들이 죽어 나가는데 암습 따위가 대수겠습니까.”

“무인으로서 부끄럽지도 않더냐?”

“무인이기 전에 소가주입니다.”

“소가주라, 허허.”

진위경은 착잡한 표정으로 대장로를 바라봤다.

“이미 대세는 기울었습니다.”

“그래서? 항복 권유라도 할 셈인가?”

“의미 없는 싸움을 멈춰 주십시오.”

전장의 흐름은 이미 이쪽으로 넘어온 지 오래다. 그러나 흑의인들은 끈질기게 저항했고, 아직도 비명과 시체는 줄어들지 않았다.

“네 말이 옳다. 의미 없는 싸움일지도 모르지. 하지만…….”

비틀거리던 대장로가 허리를 곧게 폈다. 어느새 눈에는 정광이 번뜩였고 칼날 같은 기세가 일어나기 시작했다.

“멈추기에는 너무 멀리 와 버렸어.”

마지막 발악?

아니, 그 정도가 아니다. 나는 문득 한 사람을 떠올렸다.

조필. 놈이 죽어 가기 직전 보여 준 마지막 모습이 지금의 대장로와 겹쳐졌다.

‘선천지기. 선천지기를 끌어올린 거야.’

공력이 운기조식과 영약을 통해 축적한, 후천적인 기운이라면 선천지기는 그 반대다. 생명력 그 자체라고 봐도 무방한 인체의 근원.

대장로는 지금 생명을 담보로 선천지기를 사용하고 있는 것이다.

“쿨럭.”

핏물을 토해 낸 대장로가 검을 치켜들었다. 빠르게 꺼져 가는 생명과는 반대로 그의 검은 어느 때보다 찬란하게 빛나고 있었다. 그 압도적인 광경을 본 순간, 나도 모르게 입 밖으로 한 단어가 흘러나왔다.

“검강…….”

그건 본능이었다. 단순히 보는 것만으로도 심장이 펄떡거린다. 검기를 아득히 뛰어넘는 무시무시한 기운이 느껴졌다.

그리고.

“그래, 네가 있었지.”

실핏줄이 툭툭 터져 나간 붉은 눈동자가 나를 응시한다.

진위경이 황급히 대장로를 막으려 달려들었다.

“안 돼!”

그러나 대장로는 이미 그 자리에 없었다. 한 걸음 만에 다섯 장의 거리를 압축시킨 그가 내게로 검을 내리그었다.

후우웅.

‘이렇게 죽는구나.’

피할 수도, 막을 수도 없는 공격. 난 죽었다. 죽을 것이다.

하지만…….

‘이대로 죽을 수는 없어.’

전신의 근육을 쥐어짰다. 한 줌 남짓한 공력이 창날을 향해 질주했다. 그건 마지막 발악이었고, 지금까지 치열하게 살아왔던 내 인생에 대한 예의였다.

“일섬.”

쐐애애액!

마지막 힘을 담은 일격이 쏘아졌다.
```

## Current accepted English baseline

```markdown
# Chapter 61

Gooooong.

The Head Elder felt the air tremble. In the same instant, he understood how much destructive power the spearhead shooting toward his chest carried.

*This is… dangerous.*

A threat to his life he had felt only a handful of times. Every hair on his body stood on end, and the world slowed.

Shiiiiing!

Jin Taekyung’s spear came from the front, while Jin Wikyung’s sword flew in from behind. The two brothers’ pincer attack meshed with perfect timing.

A truly life-or-death moment.

Fwoooosh.

The sixty years of internal energy coiled in the Head Elder’s dantian spread through every limb and bone. It poured vitality into his aging muscles and woke his blood vessels. The change did not stop there.

Tssssss.

The Sword Energy that had risen nearly a foot—thirty centimeters—compressed to half its size.

That was not a loss of power. It was condensation.

The Sword Energy that had fluttered like a thread wrapped the entire blade and took the shape of another sword.

Sword Force.

The symbol of the superhuman masters who had broken through the wall of the Peak realm and opened a great new domain.

It was still incomplete, only half-formed, but it was unmistakably Sword Force—the distilled essence of the martial arts the Head Elder had spent his life mastering.

Shhk.

Even the Jin Family of Taiyuan’s ancestral treasure sword was cut apart, Sword Energy and all. Jin Wikyung’s internal energy scattered in an instant, and his insides were wrenched. His face went pale.

One stroke would have been enough to take his neck.

But the Head Elder had no time.

Shwack!

He reached for the spear now almost at his chest. His wrinkled hand, too, was wrapped in a dazzling radiance of qi.

This, too, was an incomplete Hand Force, but it was enough to stop Jin Taekyung’s spear.

No. It looked like enough.

Kraaaaaash!

Until the vortex spilling from the spearhead swallowed him whole.

* * *

A deathly silence settled. It felt as if the dozens of people here—or perhaps everyone standing on the battlefield—were watching us.

No.

Not us.

One man.

“This…”

At the end of countless gazes, the Head Elder slowly opened his mouth.

“What form was that?”

I answered.

“One Flash.”

Even speaking the words brought on a vicious hunger. Every muscle in my body stung, and not a scrap of internal energy was left inside me.

But that was all.

Unlike with Jopil, I didn’t pass out or crumple pathetically to the ground.

*My body can handle it now.*

I had grown enough to take One Flash’s side effects. And as much as I had grown, One Flash’s power had grown with me.

The Head Elder’s current state was proof of that.

“One Flash. One Flash…”

He muttered it under his breath and pressed an acupoint on his shoulder.

The bleeding stopped, but that was all. The arm ground to nothing by the vortex One Flash had unleashed did not come back.

“I never thought I’d end up one-armed at this age. Heh heh.”

The Head Elder gave a hollow laugh and turned toward Jin Wikyung.

“You’ve got a frightening younger brother.”

Jin Wikyung asked, his face wan,

“Does that child frighten you?”

“What about you?”

“I’m proud of him.”

Not a hint of hesitation. A smile bloomed over his pale face.

“I raised him like gold and jade, but he grew into steel. That’s the kind of child Taekyung is.”

The Head Elder stared at that smile.

“You’re a fairly impressive talent. Enough to shoulder the future of the Jin Family of Taiyuan.”

“Am I?”

“But not as much as your younger brothers.”

Jin Mukyung reaching the Peak realm at twenty was one thing. Getting ranked that high myself was almost more than I could take, but…

*What is he getting at?*

As if he’d read my mind, the Head Elder went on.

“Power is what you don’t even share with your own blood. When that time comes, will you still be so proud of your younger brothers?”

The air around us went ice-cold in an instant.

Everyone facing the Head Elder at close range belonged to the Jin Family of Taiyuan. Cautious looks clung to my cheeks, then quietly slid away.

*Family Head? I have no intention of doing anything like that, you bastards.*

That was when Jin Wikyung spoke.

“So that was it.”

Bitterness and relief both sat in his voice. The Head Elder’s brow twitched.

“What are you talking about?”

“The reason you betrayed us. The reason a day like today happened.”

“…!”

The Head Elder’s trembling eyes answered for him. I sighed inwardly.

*So that was what this was about.*

A succession fight.

It felt like a huge puzzle piece had clicked into place. The smaller pieces that still hadn’t found their spots were fitting together one by one through their conversation.

“What happened?”

Jin Wikyung asked in a respectful tone.

The shift was so natural no one else there even noticed.

“Do you know anything about your grandfather?”

“I’ve heard nothing. Father never said a word about him.”

“He was a cold man. Toward his children, and toward his only younger brother. And…”

The Head Elder gave a dry little laugh.

“He was a petty man. For a lot of reasons, we brothers, who had once been close, drifted apart. And then that happened.”

“The Great Faction War.”

“Have you heard of the Ten Myriad Demonic Forces? They came in endless waves. The Murim Alliance was formed, but it was only an alliance of the Nine Sects and One Gang, and they were too busy defending their own bases.”

That was also when the Head Elder had begun making a real name for himself.

Under the Jin Family of Taiyuan’s banner, he rallied Shanxi’s martial artists and finally drove out the Demonic Cult’s forces.

“The last battle was right here, at Eight Spring Gorge.”

His gaze seemed to grope toward some distant point in the past.

“It was a long war. Many people died, and everyone was exhausted. But there was hope, too. Hope that they could finally return to their families. The three hundred volunteers sworn to die all shared that same hope.”

“In the end, you won a great victory.”

Three hundred against three thousand.

The result was the Demonic Cult’s annihilation.

It was a glorious victory, and the reason the Head Elder was still remembered. Everyone had believed that without question.

Until just now.

“There was an ambush.”

*What?*

“We fought as we fell back deep into the gorge, but we were hopelessly outnumbered. Even as I swung my sword like a madman, one question would not leave me.”

The Head Elder’s voice was unnervingly calm.

“How could they have set an ambush in advance? My elder brother should have been blocking the road into Eight Spring Gorge.”

“…!”

Silent shock spread through the crowd. What little color was left in Jin Wikyung’s already pale face vanished.

“The battle lasted half a day. We fought waiting for reinforcements that never came, and it was useless. Of the three hundred volunteers, only eight survived. When we finally returned to the family, I have never been able to forget the look on my brother’s face when he saw me.”

“Is that… true?”

“Enough time has passed for mountains and rivers to change several times over. Did you think I came this far on mere suspicion?”

Decades were more than enough to turn suspicion into certainty. The Head Elder laughed hollowly.

“My brother turned the war into an opportunity. I became a hero on the battlefield, but he became Family Head. Everyone who had followed me either died in battle or vanished afterward.”

“Then going straight into the Elder Council—was that why?”

“Because that was the only way he would feel at ease. The only way I and my people could stay alive.”

*My people?*

I thought back to what he had said. The eight survivors who had followed the Head Elder and lived to the end.

Guessing who they were was not hard.

*The Elders and the Sect Leaders of the Five Gates of Shanxi.*

The survivors had sworn revenge. Revenge on the Family Head and the family that had betrayed them.

The Head Elder slowly swept his gaze over the crowd.

“It had been a very long wait.”

Silence swallowed them. Disbelief, shock, shame. The feelings differed, but no one could easily speak.

Well. No one except me.

“You sure dragged that bullshit out.”

“…!”

I couldn’t hold back the little snorts of laughter leaking out of me.

I had listened all the way through to see where this was going, and this was what I got.

“In the end, you’ve only got one goal.”

I flicked my thumb at the Head Elder.

“Revenge, my ass. You’re trying to become this, aren’t you?”

“What did you say?”

“I’m right, aren’t I? Clear away everything in the way—the Jin Family of Taiyuan, the Mount Heng Sword Sect—and swallow Shanxi whole.”

“You insolent—!”

Had the old man swallowed a locomotive boiler? Oh, right. No trains here.

“Revenge? Sure. Fine, revenge…”

I picked at my ear and went on.

“But why now?”

This had happened a full forty years ago. Even counting the Head Elder’s age, he had waited half his life.

“How many of the people who stabbed you in the back are even still alive? There’s late, and then there’s this late. And please, I’m begging you—don’t start with that bullshit about a gentleman waiting ten years to take revenge.”

If holding out ten years made you a gentleman, did holding out forty make the Head Elder Jesus?

It was nothing more than a crazy old man’s self-justification.

“You run your mouth just because you’ve got one.”

“I did. What are you going to do about it?”

“Do you think you know everything?”

“Do I have to? After it’s gone this far?”

The question was so obvious I snorted a laugh and pointed at the battlefield.

A mountain of corpses, a sea of blood. Utter pandemonium. The scene in front of us was exactly that.

“That…”

The chill in the Head Elder’s eyes wavered. But only for an instant.

“I see. What more is there to say?”

He muttered it like a jab at himself, then raised his sword.

“Head Elder.”

Jin Wikyung’s lips moved, and that was all.

A fight that ended only when one side died. They had come too far to turn back.

“Come.”

I wasn’t about to decline.

“Attack!”

It was time to hunt the wounded beast.

* * *

I remembered the first day I saw the Head Elder.

A bearing and dignity that made his age meaningless. His white beard called an immortal to mind.

Fwoosh!

Of course, there were no immortals who mercilessly cut people in half.

*Even rotten, a prized fish is still a prized fish.*

Drenched in blood, he swung his sword without pause. Looks mixed with awe and fear poured toward him.

“Monster…”

He had lost an arm, but the Head Elder was still strong.

He just clearly wasn’t as strong as before.

*This is doable.*

Peak master or not, the martial artists here were the Jin Family of Taiyuan’s elite. Men who had fought across the battlefield under Jin Wikyung, skilled enough to have survived the earlier clash with the Head Elder.

Clang-clang-clang!

The Head Elder knocked aside blades driving in from every direction, his face darkening. In the old days, he would have cut down everything in his path with Sword Energy.

Proof that the internal energy that had once seemed like a spring that never ran dry had finally hit bottom.

On top of that, his aged body had reached its limit.

Shraaaak!

Sword wounds began to multiply across the Head Elder’s body. Unlike before, most of the blood was his.

*Now!*

I wasn’t about to miss that opening. The spear I drove with everything I had tore a handful of flesh from his side.

“Hk!”

Even through the pain, the Head Elder cut down a martial artist and charged me. He meant it this time; a faint Sword Energy gathered along the swinging blade.

But…

Shhk.

The Sword Energy scattered in a rising spray of blood. Jin Wikyung appeared behind the staggering Head Elder.

“I’d forgotten you were there.”

The Head Elder turned with a twisted face.

“Did my elder brother teach you to put a knife in someone’s back?”

“My family members are dying. Is a sneak attack really that important?”

“Aren’t you ashamed, as a martial artist?”

“I am the Lesser Family Head before I am a martial artist.”

“The Lesser Family Head, is it? Heh heh.”

Jin Wikyung looked at the Head Elder with a complicated expression.

“The tide has already turned.”

“So? Are you going to ask me to surrender?”

“Please stop this meaningless fight.”

The flow of the battlefield had been ours for a long time. But the black-clad men kept resisting stubbornly, and the screams and corpses still showed no sign of thinning out.

“You’re right. It may be a meaningless fight. But…”

The staggering Head Elder straightened his back. A sharp gleam was already flashing in his eyes, and a blade-like aura began to rise.

“We’ve come too far to stop.”

A last desperate struggle?

No. More than that. Someone suddenly came to mind.

Jopil.

The last sight of him as he was dying overlapped with the Head Elder now.

*Innate qi. He’s drawing up his innate qi.*

If internal energy was acquired power, piled up by circulating qi and taking elixirs, innate qi was the opposite. It was the root of the human body—life force itself, for all intents.

The Head Elder was staking his life to use it.

“Cough.”

He spat blood and raised his sword. His life was going out fast, but his sword shone more brilliantly than it ever had.

The moment I saw that overwhelming sight, a single word slipped out of me.

“Sword Force…”

It was instinct.

My heart pounded just from looking at it. I could feel a terrifying power that far outstripped Sword Energy.

And then—

“Yes. You were here.”

His red eyes, the capillaries bursting one after another, locked on me.

Jin Wikyung lunged to stop the Head Elder.

“No!”

But the Head Elder was already gone from that spot.

In a single step he compressed fifty feet and brought his sword down on me.

Whoooong.

*So this is how I die.*

An attack I couldn’t dodge or block.

I was dead. I was going to die.

But…

*I can’t die like this.*

I wrung every muscle in my body. The last scant handful of internal energy raced for the spearhead.

It was a final struggle, and a show of respect for the life I had lived so fiercely until now.

“One Flash.”

Shiiiiiiing!

The last strike, carrying every bit of strength I had left, shot forward.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 61`.

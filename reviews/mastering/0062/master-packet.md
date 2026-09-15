# Master Edit Task — Chapter 62

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
| 진백양    | **Jin Baekyang**   |
| 이천백    | **Lee Cheonbaek**  |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 화양검    | **Blade of Flowers**          | Jin Baekyang   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 산서오문   | **Five Gates of Shanxi**         |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 마교     | **Demonic Cult**                                 |                                                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 칭호               | **Title**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 귀문      | **your sect**                                                   |
| 공자      | **Young Master**                                                |
| 진충 | **Jin Chung** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 궁귀문 | **Gunggui Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |

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

#### Chapter 60 tail (verified mastered)

…
at a single man. It was a magnificent sight. “Yes, sir!” With a huge shout, dozens of martial artists charged as one mass. I was no exception. My grip tightened on the spear, and my chest felt ready to burst. *We can win. No—we win, no matter what.* It was an all-out clash with no formation to speak of. But we had Jin Wikyung, a Peak master, and dozens of martial artists following him. *And we have me.* The Head Elder had placed too much faith in his own strength. He had committed every last subordinate to the front lines without keeping even a minimal escort, and as a result, the black-clad men were now pinned down by the combined assault of the Jin Family of Taiyuan and the Mount Heng Sword Sect. The Head Elder… dies right here. *It’s over!* It did not take long for that certainty to shatter to pieces. Shushushushush! Dozens of tiny points shot out of nowhere. They cut through the air faster and harder than anyone had expected. “It’s the Finger-Flicking Technique!” Jin Wikyung’s shout. I was not given time to think about what that even was. Pow-pow-pow-pow! Clang! “Aaargh!” “Guh!” Some people fell. Others knocked the projectiles aside. Those who fell never rose again. *Don’t tell me…* It had lasted only an instant, but I saw it clearly. Tiny points packed into the area around their hearts and across their faces like buckshot. *Stones?* They were closer to shards now, but they had definitely been stones. Unable to withstand the Head Elder’s internal energy, they had shattered the instant he fired them at us. *Is this possible?* I got goose bumps, but it was not over. The Head Elder was stretching a hand this way. “Scatter!” This time Wikyung and I shouted together. The martial artists, already wound tight, scattered in an instant. *Good. We weren’t late this ti—* The relief lasted only a moment. Swoooosh! What shot toward us this time was not the Finger-Flicking Technique. It was the Head Elder. He plunged among the martial artists and rampaged like a wild beast. Slash. Slash. Slash. “Grrk.” “Hhk.” Every time a sword flashed through the dark, another life went out. Wherever the Head Elder tore through, only stifled screams and corpses were left. “Head Elder—!” Jin Wikyung charged at him in a fury. By then the Head Elder had already killed five people. And still not a drop of blood on that white face, enough to make you think of a ghost. “You’ve come?” “How dare you!” “You’re all clumsy. Peace must have lasted too long.” There was one fact none of us could deny. The Head Elder was a hero of the Great Faction War. He was stronger and more seasoned than anyone here—a Peak martial artist honed through countless real fights. Shiiiiing! The Sword Energy Jin Wikyung drew out stabbed through empty air. The Head Elder slipped it with nothing more than a slight tilt of his head, then flicked a finger. His target was me. Shhk! I could not see a thing. Instinct knew anyway. *Internal energy.* That was literally a lump of qi itself. I rolled without wasting a beat. Pshk. “Guh.” I should have blocked it with my spear, but the attack was too unfamiliar for me to think that far ahead. An ally whose name I did not know paid the price. I felt rotten. “Naryeotagon? What a donkey of a man.”[^1] [^1]: *Naryeotagon* is a martial-arts term for dropping and rolling on the ground to evade an attack; the Head Elder’s remark also compares Taekyung to a donkey. I spat out the dirt in my mouth. “If you want to live, what won’t you do?” “Haha. You’ve already become a proper man of Murim.” Clang! Clang-clang-clang! Had anyone ever seen a monster like that. Even while talking, he knocked aside every last bit of Jin Wikyung’s Sword Energy. I was speechless. Thud! Even then, a fist loaded with internal energy smashed the skull of a martial artist who’d gone for his back. “You’re still twenty years too early.” The battle had barely begun. Not even enough time had passed to drink a cup of tea, yet nearly twenty martial artists had already become cold corpses. “You bastard!” Shiiiiing! A middle-aged warrior whose face looked vaguely familiar lost his head to Sword Energy. “Die!” Boom! A young man with a baby face that might have been twenty had his chest caved in and dropped to his knees. Not NPCs. Real people. Faces I had run into at least once at the Jin Family of Taiyuan. Faces I had shaken hands with. I gritted my teeth at that. *I’m sorry.* I was not apologizing because I lacked the power to stop it. I was apologizing because I had used their deaths. Shhk! Another person dropped to the Head Elder’s Finger-Flicking Technique like a puppet with its strings cut. But the corpse that looked about to topple backward popped up like a roly-poly toy. Then it pitched toward the Head Elder. “Cheap trick!” Boom! Bang! With one hand, the Head Elder blocked Jin Wikyung’s sword. With the other, he launched a palm strike at the corpse. And then… *Now.* Hidden behind the corpse as it flew through the air, I thrust out my spear. “One Annihilation.” The next instant— Goooooong. There was a roar that stuffed the ears.

#### Chapter 61 tail (verified mastered)

…
years made you a gentleman, did waiting forty make the Head Elder Jesus? It was nothing more than a crazy old man’s self-justification. “You run your mouth just because you’ve got one.” “I did. What are you going to do about it?” “Do you think you know everything?” “Do I have to? After it’s gone this far?” The question was so obvious I snorted a laugh and pointed at the battlefield. A mountain of corpses. A sea of blood. Utter pandemonium. The scene before us was exactly that. “That…” The chill in the Head Elder’s eyes wavered. But only for an instant. “I see. What more is there to say?” He muttered it as if mocking himself, then raised his sword. “Head Elder.” Jin Wikyung’s lips moved, but that was all. This fight would end only when one side was dead. They had come too far to turn back. “Come.” I wasn’t about to decline. “Attack!” It was time to hunt the wounded beast. * * * I remembered the first day I saw the Head Elder. His imposing bearing and dignity had made his age seem meaningless. His white beard had called an immortal to mind. Fwoosh! Of course, no immortal would mercilessly cut a man in half. *Even rotten, a prized fish is still a prized fish.* Drenched in blood, he swung his sword without pause. Looks mixed with awe and fear poured toward him. “Monster…” He had lost an arm, but the Head Elder was still strong. He just clearly wasn’t as strong as before. *This is doable.* Peak master or not, the martial artists here were the Jin Family of Taiyuan’s elite. Men who had fought across the battlefield under Jin Wikyung, skilled enough to have survived the earlier clash with the Head Elder. Clang-clang-clang! The Head Elder knocked aside blades driving in from every direction, his face dark. In the old days, he would have cut down everything in his path with Sword Energy. Proof that the internal energy that had once seemed like a spring that never ran dry had finally hit bottom. On top of that, his aged body had reached its limit. Shraaaak! Sword wounds began multiplying across the Head Elder’s body. Unlike before, most of the blood was now his. *Now!* I wasn’t about to miss that opening. The spear I drove forward with all my strength tore a handful of flesh from his side. “Hk!” Even through the pain, the Head Elder cut down a martial artist and charged at me. He had clearly made up his mind. Faint Sword Energy gathered along his swinging blade. But… Shhk. The Sword Energy scattered in a rising spray of blood. Jin Wikyung appeared behind the staggering Head Elder. “I’d forgotten you were there.” The Head Elder turned with a twisted face. “Did my elder brother teach you to put a knife in someone’s back?” “My people are dying. Does a sneak attack really matter?” “Aren’t you ashamed, as a martial artist?” “I am the Lesser Family Head before I am a martial artist.” “The Lesser Family Head, is it? Heh heh.” Jin Wikyung looked at the Head Elder with a complicated expression. “The tide has already turned.” “So? Are you going to ask me to surrender?” “Please stop this meaningless fight.” The flow of the battlefield had shifted to our side long ago. But the black-clad men kept resisting stubbornly, and the screams and corpses still showed no sign of thinning out. “You’re right. It may be a meaningless fight. But…” The staggering Head Elder straightened his back. A sharp gleam was already flashing in his eyes, and a blade-like aura began to rise. “We’ve come too far to stop.” A last desperate struggle? No. It was more than that. Someone suddenly came to mind. Jopil. The Head Elder’s current appearance overlapped with the last sight of Jopil as he lay dying. *Innate qi. He’s drawing up his innate qi.* If internal energy was an acquired force accumulated by circulating one’s qi and consuming elixirs, innate qi was the opposite. It was the root of the human body—life force itself, for all intents and purposes. The Head Elder was staking his life to use it. “Cough.” He spat blood and raised his sword. His life was going out fast, but his sword shone more brilliantly than it ever had. The moment I saw that overwhelming sight, a single word slipped out of me. “Sword Force…” It was instinct. My heart pounded just from looking at it. I could feel a terrifying power that far outstripped Sword Energy. And then— “Yes. You were here.” His red eyes, the capillaries bursting one after another, locked on me. Jin Wikyung lunged to stop the Head Elder. “No!” But the Head Elder was already gone from that spot. In a single step he compressed fifty feet and brought his sword down on me. Whoooong. *So this is how I die.* An attack I couldn’t dodge or block. I was dead. I was going to die. But… *I can’t die like this.* I wrung every muscle in my body. The last scant handful of internal energy raced for the spearhead. It was a final desperate struggle, and a show of respect for the life I had lived so fiercely until now. “One Flash.” Shiiiiiiing! My final strike, carrying every last bit of strength I had, shot forward.

## Korean source

```text
＃62화



세상이 정지한 것 같았다. 심장 박동 소리가 천둥처럼 울렸고, 흩날리는 흙 알갱이 하나까지 또렷이 보였다.

그리고…….

후우웅.

섬광이 있었다. 검강이 뿜어내는 빛은 아름다우면서도 정확했다. 창날은 물론 내 육신까지 반으로 가를 수 있을 법한 파괴적인 힘이 느껴졌다.

‘끝났군.’

나는 최선을 다했다. 일말의 후회조차 없다면 거짓말이지만 결과는 바뀌지 않을 것이다.

그저 마지막까지 있는 힘껏 부딪쳐 갈 뿐.

슈화아악!

창날이 바람을 찢었고, 검강은 바람을 지웠다. 죽음이 성큼 다가온 그 순간이었다.

쐐애액! 푹!

대장로의 눈이 부릅떠졌다. 섬전 같은 속도로 일어나 그의 단전에 비수를 박아 넣은 것은 정체를 알 수 없는 괴인이었다.

“너…….”

“사혈을 짚었어야지.”

아무도 예상하지 못한 기습이었다.

방금까지만 해도 그는 주위에 널린 수많은 시신 중 하나에 불과했으니까. 하지만 아니었다.

괴인은 극한의 인내심으로 때를 기다렸을 뿐이다. 자식의 원수를 갚을 순간을.

대장로가 비명처럼 외쳤다.

“이천백!”

“크하하하!”

이천백이 광소를 터트린 순간, 내 창날이 그의 등을 파고들었다. 살과 뼈를 가르며 거침없이 뻗어 나갔다.

띠링.



- [Lv.75 이천백]을 처치했습니다!

- 레벨 업!

- 레벨 업!

- 레벨 업!

.

.

- 레벨 업의 중첩 효과로 모든 상태 이상이 회복됩니다!



변화가 일어났다. 욱신거리던 근육이, 무겁던 발이, 텅 비어 있던 단전이 새로운 힘으로 팽창했다.

동시에 나는 무엇을 해야 할지 깨달았다.

‘일섬.’

다시 한번. 백색 와류가 뿜어져 나왔다.

콰드드득!



* * *



구사일생.

저 네 글자가 이렇게 가슴에 와닿기는 난생처음이다.

진짜 죽다 살아났다. 지옥 입국 수속 밟고, 염라대왕이랑 찐한 포옹에 기념사진까지 한 방 찍는 환상까지 봤을 정도다.

이천백이 아니었다면 환상은 현실이 되었을 텐데.

‘구하길 잘했네.’

편히 갈 수 있도록 이천백의 눈을 감겨 주고 싶었지만 아직 해야 할 일이 남아 있다.

“그러니까 착하게 살지. 좀.”

내 말에 대장로가 피식 웃었다. 그의 모습은 처참했다.

일섬은 하나 남은 팔마저 집어삼킨 것으로 모자라 가슴에 주먹만 한 구멍을 뚫었다.

“심보 한번 고약한 녀석이군. 죽어 가는 노인에 대한 예의도 없느냐?”

“내가 아는 노인은 늘그막에 손주들 재롱 보는 맛으로 사는 분들이야. 당신처럼 손주들 죽이려고 날뛰는 영감탱이가 아니라.”

“예끼 이놈! 손주 노릇이나 하고 나서 그런 말을 해라.”

껄껄 웃는 그는 허탈하면서도, 모든 걸 털어낸 듯 후련해 보였다.

“태경이는 착한 아이입니다. 대장로께서 먼저 마음을 열었다면 좋은 조손 지간이 되었겠지요.”

대장로가 고개를 돌렸다. 검을 쥔 진위경이 그곳에 있었다.

“그 검으로 나를 찌를 셈이냐?”

“고민 중입니다.”

“그 고민, 빨리 끝내야 할 게다. 남은 시간이 많지 않으니.”

그의 말은 사실이었다. 양팔이 잘려 나간 단면과 아랫배에서는 멀쩡한 척 이야기를 나누는 지금도 핏물이 폭포수처럼 흐르고 있었다.

거기에 선천지기를 끌어올린 후폭풍까지. 그가 아직도 살아 있다는 사실이 기적처럼 느껴질 정도다.

“힘들어 보이십니다.”

“아니, 편안해지는 중이지.”

단호한 대답이었다.

“정마대전이 일어났을 때 내 나이가 고작 이립(而立)이었다. 그 후로 단 한순간도 맘 편히 쉬어 본 적이 없지. 아니…….”

대장로가 힘겨운 목소리로 말을 이어 갔다.

“사실 오래전부터 지쳐 있었는지도 모르겠다.”

나는 기가 차서 중얼거렸다.

“할 거 다해 놓고 이제 와서 뭔.”

“태경아!”

진위경은 가벼운 질책이 담긴 눈짓을 보냈지만, 대장로는 기분 나쁘지 않은 듯 다물었던 입에서 바람 빠지는 웃음소리가 새어 나왔다.

“푸흐흐. 그래, 네 말이 맞다. 노망난 늙은이의 지랄이라고 생각하거라.”

“진짜 죽을 때 됐나 보네.”

“어허! 이 녀석!”

“아, 왜요. 틀린 말 한 것도 아닌데.”

티격태격하는 나와 진위경을 대장로가 흐릿한 시선으로 바라봤다.

“우리에게도 너희 같은 때가 있었지. 그래, 분명히 그랬던 적이 있었어.”

하지만 대장로에게는 더 이상 추억을 더듬을 시간조차 남아 있지 않았다.

“쿨럭, 쿠에에엑!”

한 됫박은 될 법한 피를 토해 낸 대장로가 비틀거렸다. 그는 죽음을 목전에 두고 있었다. 눈의 실핏줄은 모조리 터져 나갔고, 몸에서 흘러나온 피는 웅덩이를 이룬 지 오래였다. 이제는 가망이 없다는 걸 한눈에도 알 수 있을 정도로.

‘정말 죽는다고? 저 대장로가?’

사람은 누구나 죽는다. 이 전장에서만 수백, 어쩌면 일천 이상의 목숨이 사라졌는지도 모른다.

하지만 대장로의 죽음은 쉬이 상상조차 할 수 없던 일이었다.

그만큼 그가 보여 준 무위는 압도적이었다. 그 탓에 지금의 모습이 처절해 보이기까지 했다. 그래서 더 궁금해졌다.

“그렇게까지 버티는 이유가 뭐지?”

대장로가 대답했다.

“먼저 떠나보낸 이들에게…… 최선을 다했다고 말하고 싶으니까.”

“후회는?”

“없다.”

그는 활짝 웃으며 가슴을 내밀었다.

“끝내라. 네 손으로 직접.”

나는 창을 들었다. 진위경은 착잡한 얼굴이었지만 그렇다고 말리지는 않았다.

쉭!

한 줄기 바람이 불었고, 꺾일 것 같지 않던 대장로의 무릎이 땅에 닿았다. 그의 주름진 얼굴 위로 편안한 미소가 떠올랐다.

마지막 순간, 입술이 달싹였지만 소리는 새어 나오지 않았다.

그뿐이었다.

띠링.



- [Lv.95 진백양]을 처치했습니다!

- 퀘스트, [배반자]를 완료했습니다!

- 레벨이 크게 올랐습니다!

- 명성치가 크게 올랐습니다!



아주 잠깐, 침묵이 흘렀다.

그리고 지금껏 들어 본 적 없는 거대한 함성이 터져 나왔다.

“산서잠룡 진태경이 화양검 진백양을 베었다!”



- 칭호, [산서잠룡]을 획득했습니다!



수십, 어쩌면 수백.

살아남은 모두가 내 이름을 외치고 있었다.

‘산서잠룡이라.’

제법 마음에 드는 새 이름이었다.



* * *



- 태원진가의 삼공자 진태경이 대장로를 베었다!

- 산서잠룡이 화양검을 꺾었다!

“산서잠룡이라.”

위팽은 피식 웃었다. 토룡(土龍) 소리도 못 듣던 망나니 삼공자다. 그러나 이제는 인정하지 않을 수 없다.

그는 잠룡이다. 여의주를 얻으면 창천을 누빌 수 있는.

“어떻게 생각하시오?”

일장로가 대답했다.

“저 말을 믿나?”

“모두가 대장로의 죽음을 외치고 있소만.”

“그건 주군이 원하셨기 때문이야. 삼공자 따위가 그분을? 웃기지도 않는 소리지.”

“여기서 그게 보인단 말이오? 눈도 좋군.”

“그렇게 한눈을 팔았으니 이 꼴이 된 것 아니겠나. 하하하.”

그는 시체 더미에 비스듬히 몸을 기대고 있었다. 어깨 어림부터 허리까지 사선으로 갈라진 검상에서는 피가 콸콸 쏟아졌다.

“투항하시오. 지금 치료한다면 살 수 있소.”

“아니. 노부의 끝은 이미 오래전에 정해 뒀네. 아주 고통스러운 죽음이지.”

위팽은 고개를 저었다.

“내가 허락하지 않을 거요.”

“내 죽음에는 허락이 필요 없네. 자네도, 심지어 나도 어찌할 수 없어.”

“그게 무슨.”

일장로의 말을 이해하지 못한 위팽이 미간을 좁혔을 때였다.

“암천(暗天)을 조심…… 크륵.”

한순간이었다. 일장로의 칠공에서 피가 쏟아졌다. 눈이 뒤집히고 전신이 경련했다.

“일장로!”

위팽이 황급히 다가섰을 때는 일장로의 숨이 이미 끊긴 후였다. 앞서 했던 말처럼 고통스러운 죽음을 맞이한 그의 얼굴은 잔뜩 일그러져 있었다.

‘이건.’

독? 혹은 금제?

지금으로써는 알 도리가 없다. 위팽은 그의 유언이 된 한 단어를 뇌리 깊숙이 새겼다.

‘암천. 분명 암천이라고 했다.’

일장로가 남긴 유일한 단서. 위팽은 복잡한 심경으로 죽은 이의 얼굴을 응시하다가 돌아섰다.

“나, 위팽이 일장로를 베었다!”

흑의인들의 얼굴에 절망이 깃들었다. 죽음과 항복. 두 가지 길에서 그들이 선택한 것은 후자였다.

텅. 터터텅.

힘없이 떨어지는 병장기들.

전쟁의 종지부였다.



* * *



죽은 자가 있다면 살아남은 자도 있다.

전투에 앞서 미리 절벽 위로 올라갔던 궁귀문(弓鬼門)의 문주, 진충이 바로 그런 경우였다.

“허망하구나.”

반평생을 바친 대계였다. 그러나 결과는 참혹했다.

주군으로 모셨던 대장로, 호형호제하던 장로들과 산서오문의 문주들이 모두 죽었다. 살아남은 자들의 발악도 끝났으니 이제 남은 것은 자신뿐이다.

‘결국 이리되는가.’

진충은 몸을 돌렸다. 궁귀문의 무사 오십 명이 그의 명령을 기다리고 있었다.

“떠나라.”

보이지 않는 동요가 번졌다. 가장 가까이에 있던 무사 하나가 조심스럽게 말을 꺼냈다.

“문주님, 그 말씀은……?”

“이미 끝난 싸움. 너희에게 희생을 강요하지 않으마. 이 길로 떠나라. 최대한 뿔뿔이 흩어져 산서를 벗어난다면 목숨만은 건질 수 있을 것이다.”

무사가 결연하게 고개를 끄덕였다.

“죽을 때까지 따르겠습니다.”

“나는…… 이곳에 남는다.”

“예?”

당황도 잠시, 무사의 목소리가 격정으로 떨렸다.

“저희 때문입니까?”

“천만에.”

진충은 단호하게 대답했지만 속마음은 달랐다.

‘내가 따라간다면 태원진가는 집요하게 추적하겠지.’

산서오문은 여럿이면서 하나. 하나면서도 여럿이다.

같은 목적으로 만들었으나 무사를 키우는 방식은 제각기 달랐다. 진충은…… 그들을 병기로 키우지 않았다. 제자로 받아들였다.

“문주님!”

“저희를 이끌어 주십시오!”

이들은 모두 갈 곳 없는 고아 출신이다.

최소 십 년. 길게는 이십 년 이상을 먹이고 재우며 무공을 가르쳤다. 대계가 성공했다면 산서 무림의 주축이 되었겠지만 실패한 지금은 반역자에 불과했다.

“지금 흘러가는 상황을 모르는 것이냐?”

“죽더라도 문주님과 함께하겠습니다.”

“이놈!”

“허락해 주십시오.”

맨 처음 나섰던 무사가 돌바닥에 이마를 찧었다. 이어 하나둘씩 무릎을 꿇기 시작하는 제자들의 모습에 진충은 하늘을 보며 한탄했다.

“대계가 미뤄지지 않았다면. 그들이 나서 주었더라면!”

‘그들’에 관한 이야기는 수뇌부 여덟 명만이 아는 비밀.

그 말을 입에 담았다는 것은 진충이 제자들과 최후를 함께하기로 결정했다는 것과 다름없었다.

‘이 또한 하늘의 뜻이겠지.’

컴컴한 밤하늘에서 시선을 돌린 진충이 엎드린 무사를 일으켜 세웠다. 그가 보여 준 충성심에 한없이 미안하고, 감격스러울 뿐이었다.

“되었다. 그만 일어나거라.”

따뜻한 목소리에 무사가 고개를 들었다. 이마에서 흐르는 한 줄기 핏방울을 날름 핥은 그가 히쭉 웃는다.

“예.”

퍼걱!

진충은 얼빠진 얼굴로 무사를 바라봤다. 그건 고통 따위는 느껴지지도 않을 정도의 충격이었다.

‘이게 도대체…….’

촤아악!

무사가 진충의 가슴에 박혀 있던 손을 빼냈다. 그의 손에는 달빛보다 환한 빛무리가 어려 있었다. 보는 것만으로도 불길함을 자아내는 핏빛 강기였다.

“넌…….”

“알면서 뭘 물어보시나. 아, 그리고 방금 당신이 했던 말. 간단하게 대답해 주지.”

무사의 웃음이 짙어졌다.

“우리가 왜 나서? 당신들 역할은 딱 여기까진데.”

진충은 눈을 부릅떴다. 그들이다. 마지막까지 결코 모습을 드러내지 않던 미지의 존재들.

암천!

“네놈들이!”

“어허, 이용당했다는 표정 짓지 마. 누구 덕분에 그 지옥에서 살아 나왔는지 잊었어?”

진충은 사십 년 전, 그날의 악몽을 떠올렸다. 주위에 가득한 아군의 시체와 끝없이 밀려오던 마교의 군세.

대장로를 중심으로 뭉친 그들은 죽음을 각오했다. 암천이 나타나기 전까지는.

“목숨도 살려 주고, 복수할 기회도 줬잖아. 뭘 더 바랐어?”

그의 말이 맞다. 마교의 군세를 몰살시킨 암천은 거래를 제의했고, 그들은 응했다. 머릿속에 고독을 심어야 했지만 복수를 위해서라면 뭐든 할 수 있었다.

하지만…….

“우리를 이용해서 산서를 지배하려던 속셈이 아니었나?”

“뭐, 처음에는 그랬을지도 모르지.”

“그럼 도대체 뭘 위해서?”

히죽.

“더 큰 그림.”

대답과 동시에 피 묻은 손이 진충의 가슴을 짚었다.

펑.

진충의 몸 안에서 작은 폭발이 일어났다. 고막을 터트리고 혈맥을 가닥가닥 끊어 낸 기운은 심장까지 다다랐다.

‘고작 이렇게…….’

생각은 이어지지 않았다. 이미 숨이 끊긴 진충의 몸뚱어리는 새처럼 훨훨 날아 절벽 아래로 추락했다.

쉬이이익, 쿵!

흘끗 아래를 내려다본 무사가 눈을 찡그렸다.

“아이고, 아프겠다.”

돌아선 그를 기다리는 것은 비명과 핏물이었다. 어디선가 홀연히 나타난 열 명의 흑의인이 궁귀문의 제자들을 학살하고 있었다.

“빨리 끝내고 가자.”

“존명.”

쐐애애액! 퍽!

무사는 절벽 아래로 시선을 돌렸다. 주위에서는 비명이 터져 나오고 있었지만 절벽 아래는 환호와 함성으로 가득했다.

- 산서잠룡!

- 진태경! 진태경!

“산서잠룡이라.”

계획은 성공했다. 그러나 진태경의 등장은 그도 예측하지 못한 변수였다. 그 사실이 마음에 들지 않았다.

‘쳐 낼까, 말까.’

마음만 먹는다면 뿌리째로 뽑아 버릴 수 있다. 깊어진 눈이 환호에 둘러싸인 진태경을 향했다.

- 우리 막내! 내 동생!

- 놔! 놔 이 인간아!

피식. 실소가 터져 나왔다.

‘살려 주마. 오늘은.’

무사가 돌아섰다. 그의 걸음마다 오십여 구의 시신이 융단처럼 깔려 있었다.
```

## Current accepted English baseline

```markdown
# Chapter 62

The world seemed to stop.

My heartbeat thundered in my ears, and I could see every last grain of dirt drifting through the air.

And then…

Whoooosh.

A flash of light.

The glow pouring from the Sword Force was beautiful—and precise. I could feel a destructive power in it that looked ready to split not only the spearhead, but my body itself, in two.

*It's over.*

I had done my best. It would be a lie to say I had no regrets at all, but that wouldn't change the outcome.

All I could do was smash into it with everything I had left.

Shwaaaak!

The spearhead tore through the wind. The Sword Force erased it.

That was the instant death came striding in.

Shreeeek! Thunk!

The Head Elder's eyes flew wide.

A freak of unknown identity had risen at lightning speed and driven a dagger into his dantian.

“You…”

“You should've struck a vital acupoint.”

It was an ambush no one could have expected.

Until a moment ago, he had been nothing more than one of the countless corpses scattered around us.

But he wasn't.

The freak had only been waiting, with extreme patience, for his moment—the moment he could avenge his child.

The Head Elder cried out like a scream.

“Lee Cheonbaek!”

“Kahahaha!”

The instant Lee Cheonbaek burst into maniacal laughter, my spearhead punched into his back.

It tore through flesh and bone, driving forward without resistance.

> **System**
>
> - You have defeated Lv. 75 Lee Cheonbaek!
> - Level up!
> - Level up!
> - Level up!
> - …
> - All status ailments have been recovered due to the stacked effect of the level-ups!

The change came at once.

My aching muscles, my heavy feet, my empty dantian—all of them swelled with new strength.

At the same time, I knew what I had to do.

*One Flash.*

Once more, a white vortex erupted.

Kraaaack!

* * *

A narrow escape.

Never in my life had those four syllables hit so close to home.

I had really died and come back. I'd even seen a vision of going through hell's immigration, sharing a passionate hug with King Yama, and snapping a commemorative photo together.

If it hadn't been for Lee Cheonbaek, that vision would have become reality.

*Good thing I saved him.*

I wanted to close Lee Cheonbaek's eyes so he could go in peace, but there was still work to do.

“So live a little nicer. Come on.”

The Head Elder let out a faint laugh at that. He looked horrific.

One Flash had swallowed his remaining arm, and it hadn't stopped there—it had punched a hole the size of a fist through his chest.

“What a nasty-hearted brat. Have you no manners toward a dying old man?”

“The old folks I know spend their later years enjoying their grandchildren's antics. They're not old bastards like you, running around trying to kill their own grandchildren.”

“Why, you brat! Play at being a grandson first, then say something like that.”

He laughed heartily. He looked hollow, and yet relieved, as if he had finally shaken everything off.

“Taekyung is a good kid. If you had opened your heart first, the two of you might have had a good grandfather-grandson relationship.”

The Head Elder turned his head.

Jin Wikyung stood there, sword in hand.

“Are you planning to stab me with that sword?”

“I'm considering it.”

“You'd better finish considering it quickly. I don't have much time left.”

His words were true.

Even now, as he talked as if nothing were wrong, blood poured like a waterfall from the severed stumps of both arms and from his lower abdomen.

On top of that, there was the backlash from drawing up his innate qi.

The fact that he was still alive felt like a miracle.

“You look like you're having a hard time.”

“No. I'm getting comfortable.”

The answer was firm.

“I was barely thirty when the Great Faction War began. After that, I never once rested easy—not even for a moment. No…”

The Head Elder went on in a strained voice.

“In truth, perhaps I've been tired for a very long time.”

I muttered, appalled.

“You did all that, and now you're coming out with this?”

“Taekyung!”

Jin Wikyung sent me a look of mild reproach, but the Head Elder did not seem offended. A breathy laugh leaked from behind the lips he had pressed shut.

“Puh-huh. Yes, you're right. Just think of it as a senile old man's bullshit.”

“Looks like it really is time for you to die.”

“Hey! You little brat!”

“What? It's not like I said anything wrong.”

The Head Elder watched Jin Wikyung and me bicker with a fading gaze.

“We had a time like yours too. Yes. There was definitely a time when we were like that.”

But he no longer had time left even to linger over those memories.

“Cough! Guaaack!”

The Head Elder staggered after vomiting what had to be a bowlful of blood.

He was at death's door. Every capillary in his eyes had burst, and the blood pouring from his body had long since pooled at his feet.

Anyone could see there was no hope left for him.

*He's really dying? That Head Elder?*

Everyone dies.

Hundreds of lives had vanished on this battlefield alone—perhaps more than a thousand.

But the Head Elder's death was something I had never even been able to imagine.

That was how overwhelming his martial prowess had been. It made his current state look all the more wretched.

And that only made me more curious.

“Why are you holding on this hard?”

The Head Elder answered.

“Because I want to tell those who left before me… that I did my best.”

“Regrets?”

“None.”

He smiled broadly and thrust out his chest.

“Finish it. With your own hands.”

I raised my spear.

Jin Wikyung wore a troubled expression, but he did not try to stop me.

Shhk!

A single gust of wind passed, and the Head Elder's knees—which had never seemed capable of buckling—touched the ground.

A peaceful smile rose on his wrinkled face.

At the final moment, his lips moved, but no sound came out.

That was all.

> **System**
>
> - You have defeated Lv. 95 Jin Baekyang!
> - Quest **Traitor** completed!
> - Your Level has increased greatly!
> - Your Fame has increased greatly!

For a very brief moment, silence fell.

Then a colossal roar erupted—unlike anything I had ever heard.

“The Sleeping Dragon of Shanxi, Jin Taekyung, has cut down the Blade of Flowers, Jin Baekyang!”

> **System**
>
> - You have acquired the Title **Sleeping Dragon of Shanxi**!

Dozens.

Maybe hundreds.

Everyone who had survived was shouting my name.

*The Sleeping Dragon of Shanxi.*

I rather liked my new name.

* * *

“Third Young Master Jin Taekyung of the Jin Family of Taiyuan cut down the Head Elder!”

“The Sleeping Dragon of Shanxi defeated the Blade of Flowers!”

“The Sleeping Dragon of Shanxi…”

Wipeng gave a faint smirk.

He was the wastrel Third Young Master who had never even been called an earth dragon.

But now, there was no denying it.

He was a sleeping dragon.

If he obtained the dragon pearl, he could roam the heavens.

“What do you make of it?”

The First Elder answered.

“Do you believe that?”

“Everyone is shouting that the Head Elder is dead.”

“That is because my lord wanted it that way. A mere Third Young Master killing him? It's laughable.”

“You can see that from here? Sharp eyes.”

“This is what comes of letting your attention wander. Hahaha.”

He was leaning diagonally against a heap of corpses.

A sword wound split him on a slant from about the shoulder to the waist, and blood poured from it in torrents.

“Surrender. If we treat you now, you can live.”

“No. This old man's end was decided long ago. A very painful death.”

Wipeng shook his head.

“I won't allow it.”

“My death does not require permission. Neither you nor even I can do anything about it.”

“What does that mean?”

Wipeng furrowed his brow, unable to follow, when—

“Beware Dark Heaven… Grrk.”

It happened in an instant.

Blood poured from all seven of the First Elder's orifices. His eyes rolled back, and his entire body convulsed.

“First Elder!”

By the time Wipeng hurried over, the First Elder's breath had already stopped.

Just as he had said, he had met a painful death. His face was twisted grotesquely.

*This is…*

*Poison? Or a restriction?*

There was no way to know yet.

Wipeng carved the single word that had become the First Elder's last deep into his mind.

*Dark Heaven. He definitely said Dark Heaven.*

The only clue the First Elder had left behind.

Wipeng stared at the dead man's face with complicated feelings, then turned away.

“I, Wipeng, cut down the First Elder!”

Despair spread across the faces of the black-clad men.

Faced with two paths—death or surrender—they chose the latter.

Clang. Clatter-clatter.

Weapons fell weakly to the ground.

It was the end of the war.

* * *

Where there were the dead, there were also those who had lived.

The Sect Leader of Gunggwimun,[^1] Jin Chung, was one of them. He had climbed to the top of the cliff before the battle began.

“How hollow.”

It had been a grand scheme to which he had devoted half his life.

The result was horrific.

The Head Elder he had served as his lord, the Elders he had called brother, and the Sect Leaders of the Five Gates of Shanxi had all died.

The survivors' last desperate struggle had ended as well.

Now, only he remained.

*So this is how it ends.*

Jin Chung turned around.

Fifty martial artists of Gunggwimun were waiting for his orders.

“Leave.”

An invisible stir ran through them.

One of the nearest martial artists spoke cautiously.

“Sect Leader, what do you mean…?”

“This fight is already over. I will not force you to sacrifice yourselves. Leave by this road. Scatter as widely as you can and get out of Shanxi. If you do, you may at least save your lives.”

The martial artist nodded resolutely.

“I will follow you until I die.”

“I… will remain here.”

“What?”

The confusion lasted only a moment before the martial artist's voice began to tremble with feeling.

“Is it because of us?”

“Not at all.”

Jin Chung answered firmly, but his thoughts were different.

*If I followed them, the Jin Family of Taiyuan would hunt them relentlessly.*

The Five Gates of Shanxi were many, yet one.

One, yet many.

They had been created for the same purpose, but each sect had raised its martial artists in a different way.

Jin Chung had not raised them as weapons.

He had taken them in as disciples.

“Sect Leader!”

“Please lead us!”

Every one of them had been an orphan with nowhere to go.

For at least ten years—twenty or more in some cases—he had fed them, sheltered them, and taught them martial arts.

If the grand scheme had succeeded, they would have become the backbone of Shanxi's Murim.

Now that it had failed, they were nothing more than traitors.

“Do you not understand how this is going?”

“Even if we die, we will die with you, Sect Leader.”

“You brat!”

“Please allow us.”

The martial artist who had stepped forward first slammed his forehead against the stone floor.

Then, one by one, his disciples began to kneel.

Jin Chung looked up at the sky and lamented.

“If only the grand scheme had not been delayed. If only they had stepped forward!”

Talk of *them* was a secret known only to the eight at the top.

To speak those words aloud was no different from deciding to share his final moments with his disciples.

*This too must be heaven's will.*

Jin Chung turned his gaze from the dark night sky and helped the prostrate martial artist to his feet.

He felt endlessly sorry—and deeply moved—by the loyalty the man had shown.

“That's enough. Get up.”

At the warmth in his voice, the martial artist lifted his head.

He flicked his tongue over the trickle of blood running down his forehead, then gave a crooked grin.

“Yes.”

Thuck!

Jin Chung stared at the martial artist with a blank look.

The shock was so great he could not even feel pain.

*What in the world…?*

Shwaaak!

The martial artist pulled his hand from Jin Chung's chest.

A glow brighter than moonlight clung to it—a blood-red Force that inspired dread just to look at.

“You…”

“You already know, so why ask? Oh, and about what you just said—I'll give you a simple answer.”

The martial artist's smile deepened.

“Why would we step forward? Your role ends right here.”

Jin Chung's eyes flew wide.

*Them.*

The unknown beings who had never revealed themselves until the very end.

Dark Heaven!

“You bastards!”

“Don't look at me like you've been used. Forgotten who got you out of that hell alive?”

Jin Chung remembered the nightmare from forty years ago.

The corpses of allies covering the ground around him.

The endless army of the Demonic Cult surging in.

They had gathered around the Head Elder and prepared themselves to die.

That was before Dark Heaven appeared.

“We saved your lives and gave you a chance at revenge. What more did you want?”

He was right.

Dark Heaven had annihilated the Demonic Cult's army, then proposed a deal.

They had accepted.

They had to have a gu planted in their heads, but they would have done anything for revenge.[^2]

But…

“Wasn't your real aim to use us to rule Shanxi?”

“Well, maybe that was the plan at first.”

“Then what was it all for?”

The martial artist grinned.

“A bigger picture.”

At the same time, his bloodstained hand pressed against Jin Chung's chest.

Boom.

A small explosion went off inside Jin Chung's body.

The energy burst his eardrums, severed his blood vessels strand by strand, and reached his heart.

*Just like this…*

The thought went no further.

Jin Chung's body, already dead, flew like a bird and plunged off the cliff.

Shiiiiik! Crash!

The martial artist glanced down and grimaced.

“Ouch. That must've hurt.”

When he turned around, screams and blood were waiting for him.

Ten black-clad men who had appeared out of nowhere were massacring Gunggwimun's disciples.

“Let's finish this quickly and go.”

“As you command.”

Shreeeeek! Thud!

The martial artist turned his gaze toward the bottom of the cliff.

Screams erupted all around him, but below the cliff the air was filled with cheers and shouts.

“The Sleeping Dragon of Shanxi!”

“Jin Taekyung! Jin Taekyung!”

“The Sleeping Dragon of Shanxi…”

The plan had succeeded.

But Jin Taekyung's appearance had been a variable even he had not anticipated.

He did not like that.

*Take him out, or let him be?*

If he set his mind to it, he could rip him out by the roots.

His deepening gaze turned toward Jin Taekyung, ringed by cheers.

“Our youngest! My little brother!”

“Let go! Let go, you bastard!”

A snort of laughter escaped him.

*I'll let you live. For today.*

The martial artist turned away.

Some fifty corpses lay like a carpet in his wake.

[^1]: 弓鬼門, lit. Bow Ghost Gate.
[^2]: A *gu* is a traditional poison associated with venomous creatures; in Murim fiction, it may be implanted in a person's body.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 62`.

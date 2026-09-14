# Master Edit Task — Chapter 58

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
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소군    | **Lee Seogeun**    |
| 조필     | **Jopil**          |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 이류     | **Second Rate**   |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 칭호               | **Title**                      |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 대사      | **Master** for a senior Buddhist monk                           |
| 곽준 | **Gwak Jun** |
| 평화 | **Peace Guild** | Guild name. |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 50–54

## Plot

Taekyung enters Choi Minwoo’s exclusive D-rank Gate and clears a colony of about twenty Level 40 swamp Lizardmen alone. Choi reveals the encounter was a test, then releases female-Lizardman pheromones that summon a much stronger horde. Taekyung spends all 100 Remaining Points—30 Strength, 30 Stamina, and 40 Agility—and uses One Flash to kill the Level 52 Lizardman Great Chieftain and dozens of monsters. He and Choi clear three C-rank Gates in one day, earning Taekyung 300 million won, while Choi privately recognizes that Taekyung may be stronger than himself.

Sopung Guild’s Guild Master learns that Kim Sangshik dismissed Taekyung and filed a false report. He expels Kim and orders the resignation of Kim’s son, Kim Sangho, provoking Guild-wide gossip about Taekyung’s reawakening.

Taekyung returns home with his C-rank Hunter license and cash, gives his mother and younger sister Hayeon an edited account of his reawakening, and spends the day treating them to clothes and an expensive meal. Back in the goshiwon, increasingly vivid Murim nightmares destabilize him despite Sleep Mode and qi circulation. His injuries worsen during raids, so Choi orders him home. Taekyung lies to Jinho that Jin Wikyung is his Chinese girlfriend, then concludes that Murim may be another reality and the Ark - 2020 capsule a dimensional Gate.

A dream of the Mount Heng Sword Sect–Jin Family battle convinces Taekyung that Murim’s people are real and that he must return. Choi and Butler Kim investigate him, find no evidence that he is an illegal Awakener or deliberately infiltrated Choi’s orbit, and offer an exceptionally generous contract. Taekyung refuses because he cannot abandon Murim, promises to return the next day, enters the capsule, and accepts the prompt to connect to Murim.

## Continuity

- Taekyung clears the Lizardman Gate without injury, then kills the Level 52 Lizardman Great Chieftain and the summoned horde with One Flash.
- He spends all 100 Remaining Points: 30 Strength, 30 Stamina, and 40 Agility. His equipment remains the First Rate Lizardman Hunter’s Leather Set and Lizardman Slayer’s Harpoon.
- Taekyung completes three C-rank Gates in one day and receives 300 million won, including a 270-million-won bonus. His seven-day provisional Peace Guild contract requires weekends off.
- Choi Minwoo suspects Taekyung may be stronger than him; Choi’s exact current rank remains unknown. Choi continues observing Taekyung and wants to recruit him.
- Sopung Guild expels Kim Sangshik after confirming his misconduct; Kim Sangho also leaves. Sopung’s recruitment of Taekyung remains unresolved.
- Taekyung now holds a C-rank Hunter license. His family knows only the edited explanation that he reawakened and earned money; Murim, the System, and the capsule remain concealed from them and from Seong Jinho.
- Hayeon is nineteen and still a high-school senior. Taekyung’s mother and Hayeon secretly give him additional cash and side dishes.
- Taekyung suffers recurring Murim nightmares and increasing injuries during raids. Sleep Mode repairs his body but does not resolve the mental disturbance.
- The Mount Heng–Jin Family battle is underway. The Head Elder’s third force is waiting for both sides to weaken; the traitor’s identity, betrayal, and the battle’s outcome remain unresolved.
- Taekyung has reconnected to Murim through the Ark - 2020 capsule. Whether the capsule can transport him safely and reliably, its ultimate purpose, and the consequences of his return remain unresolved.
- Choi’s offered contract includes a 500-million-won signing bonus, 50-million-won monthly salary, seventy-percent settlement split, officetel, sedan, and social insurance. Taekyung rejects it while intending to return from Murim.

## Translation Decisions

- Use **Lizardman Great Chieftain** for 대족장 and **One Flash** for 일섬.
- Preserve **swamp Lizardmen**, **Lizardman Hunter’s Leather Set**, **Lizardman Slayer’s Harpoon**, and the female-Lizardman pheromone lure.
- Keep **C-rank Hunter** distinct from System **Grade** terminology.
- Preserve **Sleep Mode**, **Remaining Points**, **Internal Energy**, **System**, and the exact prompt: **“Would you like to connect to Murim?”**
- Use **logged in** only for Taekyung’s action after accepting the prompt.
- Keep **Peace Guild**, **Sopung Guild**, **Hunter license**, **goshiwon**, and **officetel**.
- Preserve the distinction between Hayeon’s gender-neutral question about Jin Wikyung and Taekyung’s false claim that Wikyung is his girlfriend.
- Retain the dry, self-mocking narration; affectionate, profane family banter; Choi’s measured testing and recruitment; and the Guild Master’s “raise hell” callback.
- Keep *Bulgeum* as “Burning Friday,” with a concise Korean-slang footnote, and retain concise first-use footnotes for *gukbap* and *goshiwon*.

### Prior accepted reading-copy tails

#### Chapter 56 tail (verified mastered)

…
saw the white beard fluttering in the wind. And the sword in the old man’s hand. Boom! *Kh.* The thunderous impact sent Lee Cheonbaek reeling backward. He was not even given time to register the pain in his wrist. Boom! Boom! Boom! Every time the two swords met, thunder and lightning rolled. Sword Energy poured out in a continuous stream, smashing the ground and tearing the wind. Whoosh! “What in the world is that…?” The martial artists of both sides forgot they were fighting. They could only stare, slack-faced, at this staggering life-and-death duel. In that moment, every one of them was thinking the same thing. *Are those two really human beings like us?* The ceaseless thunder. A feast of Sword Energy so dazzling it left them spellbound just to watch. The movements of the two men at its center were faster and stronger than anyone they had ever seen. Someone muttered, almost a groan. “So this is a Peak master…” To their eyes, it was a fight where either outcome would have made sense. But the superiority in strength was obvious. After some three hundred exchanges, the Head Elder’s sword changed. Whoosh—slice! “Ghk.” Lee Cheonbaek bit his lip. Blood streamed from the forearm the Head Elder’s sword had raked. The strength drained from his sword hand. *Of all things.* He quickly shifted the sword to his other hand, but he was a right-handed swordsman by nature. Even at full power he would have been hard-pressed. Now that his sword arm was injured, the outcome was all but decided. Boom! Crack. A single blow snapped his wrist. His Sword Energy, weakened by the severe drain on his internal energy, could no longer stand against the Head Elder. But Lee Cheonbaek did not give up. *Not yet. It isn’t over yet.* He had suffered worse injuries than this countless times. Drawing on the strength in his arm, waist, and legs, Lee Cheonbaek swung his sword. No—he tried to. Slash! This time, it was the knee. With its tendons severed, the knee buckled slowly, with no regard for Lee Cheonbaek’s will. His sword carved uselessly through empty air. Shhk. Shhk-shhk-shhk. His side. His shoulder. His chest. Lightning stabbed and sliced through his entire body. The fierce Sword Energy did more than cut through flesh and bone—it churned his insides. “Bleeegh!” Lee Cheonbaek vomited blood mixed with pieces of his organs and looked up at the Head Elder through clouded eyes. The old man’s face was impassive. There was no thrill at having defeated his opponent. No joy that the war was ending. To him, all of this was simply the natural result. “Cough… So Shanxi’s Number One was standing right in front of me.” “If you’re not Number One Under Heaven, you’re nothing more than a martial brute from the frontier. Neither you nor I have that kind of capacity.” “Tell me what you want. I’ll give you my neck. I’ll make my men surrender, and I’ll seal the sect for ten years—or a hundred. So…” “Impossible. What I want is annihilation. Complete annihilation, without a single blade of grass left standing.” “Why…!” “Don’t ask me that. If you had won, our family would have been the one facing annihilation.” Lee Cheonbaek glared at the Head Elder with bloodshot eyes. He wanted to snap that wrinkled neck then and there. But with wounds this severe, all he could do was wring out a voice. “The Jin Family of Taiyuan… You bastards started this, didn’t you? You killed that young boy—my son!” “Ah, Lee Seogeun. That’s right. That child was where it began.” The Head Elder wore a sardonic smile. Even the master of the Mount Heng Sword Sect, one of the two powers that divided Shanxi between them, had failed to notice *their* intervention. Not even now, with death at his doorstep. —When you meet King Yama, ask him. Ask who killed Lee Seogeun. The Sound Transmission burrowed into Lee Cheonbaek’s ear, and his eyes flew wide. “What does that mean…?” It was a thoroughly impulsive act. Perhaps pity for Lee Cheonbaek, who was about to die knowing nothing. Or perhaps nothing more than an old man’s whim. —Fare for the road to the afterlife. Think it over on the long journey. The Head Elder raised his sword. The sunset beyond the winter ridge shattered into fragments along the blade. *With this…* With the death of the giant known as Lee Cheonbaek, the Mount Heng Sword Sect would collapse. Those who resisted would die. Those who surrendered would be taken prisoner. One war would end like that… And a new war would begin at the very moment everyone was drunk on victory. *It’s over.* At last, the Head Elder’s sword moved. Screeeech—! A sharp sound tore through the air. Sensing his end, Lee Cheonbaek closed his eyes. The blade wrapped in blue Sword Energy traced a beautiful line. Slice. But both the tearing sound that had come first and the direction of the sword defied Lee Cheonbaek’s expectations. The Head Elder split a spear that came flying at his back out of nowhere, cutting it apart with Sword Energy. An enraged roar burst from his mouth. “Who the hell are you!” The answer came the next instant. “It’s me, you fucking bastard!” The Head Elder saw the face of a young man standing tall on a low hill, and groaned. “Jin Taekyung?”

#### Chapter 57 tail (verified mastered)

…
this far because of his help.* Jin Wikyung thought the opposite. *We were able to come this far because this was what the Head Elder wanted.* A span too short even to call an instant. When Jin Wikyung finished the thought, he opened his mouth. “Wipeng.” “Your orders.” “Cut down the First Elder.” “What?” The stooped, emaciated old man—the First Elder—opened his eyes wide. The senior members around him were just as shocked. “L-Lesser Family Head!” “What in the world…!” But Wipeng did not hesitate. Before anyone knew it, his sword was flying toward the First Elder’s chest. Clang-clang-clang! Two swords suddenly cut in and knocked Wipeng’s blade aside. Two fat, exceptionally tall old men. They were the Second and Third Elders, who, together with the First Elder, styled themselves the Head Elder’s hands and feet. Wipeng’s brow twitched when he saw the faint Sword Energy gathered on their blades. “You’ve been hiding your martial arts.” Instead of answering, the First Elder threw a single punch. Boom! With internal energy as deep as the years he had lived, he sent Wipeng flying, then straightened his back. The field froze at the appearance of yet another Peak master who had spent his entire life hidden in the Head Elder’s shadow. “First Elder, what… what is this?” “Then could it be…!” *Betrayal.* The word stamped itself clearly into everyone’s minds. “That’s impossible!” The one who shouted was the White Tiger Hall Leader. If the Elders were the Head Elder’s hands and feet, he had thoroughly served as the First Elder’s. “Elder, Lesser Family Head. There seems to be some misunderstanding…” But he never finished. At a jerk of the First Elder’s chin, the Second Elder moved with blinding speed and severed the White Tiger Hall Leader’s neck. Shhk. Thud. Jin Wikyung and the First Elder locked eyes across the space between them. “You recruited the White Tiger Hall Leader too?” “He was a noisy man. That was all. The others were the same.” Jin Wikyung’s guess had been half right and half wrong. The Elders had betrayed the family, but the senior members of their faction had not. “Then why… Ah!” “Sharp. I’ll give you that.” The First Elder pulled a dark, grimy bamboo tube from inside his robes. Only a little of the fuse was left, and it was already burning down. “Could we tell important secrets to men like that? Even just throwing the inside into chaos had already served its purpose. Things were easier if they didn’t know what was happening outside.” Jin Wikyung’s shout came out as a scream. “Stop him!” “You’re too late.” The First Elder was right. The instant the fuse burned to its end, something burst, and a red flame shot high into the sky. Fwish—boom! It was a signal. The martial artists of the small and mid-sized sects known as the Five Gates of Shanxi—the Three Paths Sect, a union of three sects; the Byeokdo Sect, which trained chiefly with sabers; and Gunggwimun, which had been pouring arrows from the cliffs without pause—turned in an instant. “Kill everyone in your path!” “No exceptions! Sweep them all away!” They were no longer the clumsy third-rate martial artists they had seemed to be. Killing intent flowed from their eyes, and their sword paths were sharp. *This wasn’t something they prepared overnight.* Jin Wikyung’s face hardened. * * * Boom! The Head Elder looked up at the sky. Before the red flame had even faded, enormous roars erupted from every direction. *Too fast. Far too fast.* The signal was supposed to go up only after the Mount Heng Sword Sect had been annihilated. The Five Gates of Shanxi were a blade prepared over decades. It had to be swung only once and finish everything like a bolt of lightning. *Everything has its flow.* The plan that had proceeded without a hitch was beginning to veer off course. As the Head Elder smiled bitterly, a voice slipped into his ear. “So… it was you.” Lee Cheonbaek. His voice was faint, but his eyes burned more fiercely than ever. “You still have the strength to talk?” “I’ll tear you to pieces while you’re still alive.” But no sooner had he finished speaking than blood poured from his mouth. The Head Elder pressed one of his acupoints and murmured, “That would be inconvenient just yet. You still have something to do.” Lee Cheonbaek despaired. They had taken heavy losses, but hundreds of Mount Heng Sword Sect martial artists still remained. At this point, with even the leadership annihilated, if their Sect Leader were taken prisoner… *Kill me instead!* The anguished cry never escaped his mouth. The Head Elder pressed his Mute Acupoint and robbed him of his voice. Then his hand brushed the Paralysis Acupoint, and Lee Cheonbaek’s body went rigid. He had become a living corpse with his eyes still open. “You bastard! Get your hands off him!” At the same time, the air split with a shriek. Fwoooosh! The Head Elder did not panic. He swept his sword upward from below. Beyond the spear splitting in two along his Sword Energy, Jin Taekyung was charging toward him at terrifying speed. “Aaaaaah!” “Squad Leader! Please slow down a little!” Along with a dozen or so riffraff who had appeared from who knew where. [^1]: Red Hare is the legendary warhorse of Lü Bu in *Romance of the Three Kingdoms*.

## Korean source

```text
＃58화



전장은 혼돈으로 치달았다. 신호와 동시에 돌변한 이백 명의 무인들이 이리 떼처럼 사방을 덮쳤다.

“모두 죽여라!”

“으아아악!”

앞서 상대했던 곽준과 암살자들만큼은 아니지만, 놈들에게서는 잘 벼린 칼날 같은 기세가 뿜어져 나왔다.

태원진가와 항산검문. 양 세력의 무인들이 힘을 합친다면 충분히 승산이 있겠지만 지금 당장으로써는 어려워 보인다.

‘좋지 않아.’

최악의 경우 진위경만 빼내서 도망쳐야 할 수도 있다.

내심 그런 생각을 하고 있을 때, 등 뒤로 거친 숨소리와 함께 정찰조원들이 도착했다.

“조장, 좀 같이…… 헉!”

눈앞에 벌어진 상황을 보더니 하나같이 눈이 툭 튀어나온다. 뒤이어 엉금엉금 기어 올라온 혁무진도 입을 딱 벌렸다.

“우웨에엑!”

“……그쪽이었냐.”

힘들긴 했던 모양이다. 빠르고 굵은 구토를 끝낸 혁무진이 다 죽어 가는 얼굴로 말했다.

“전 여기까지인 것 같습니다.”

누가 보면 용감하게 싸우다가 칼 맞은 부상병인 줄 알겠다.

나는 녀석의 어깨를 힘주어 잡았다.

“무진아. 넌 할 수 있어.”

“아니에요. 전 틀렸어요. 가 봤자 짐만 될 거예요.”

“짐이라니! 넌 훌륭한 고기 방패…….”

“예?”

“방패! 넌 태원진가의 방패다!”

“고기 방패라고 했던 것 같은데.”

혁무진의 불신 섞인 중얼거림을 무시하고 녀석을 일으켜 세웠다. 지금은 고기 방패, 아니 손 하나가 아쉬운 시점이다.

더군다나 혁무진은 나를 제외하면 정찰조 중 최고의 실력을 지닌 고기 방패, 아 말이 자꾸 헛나오네.

나는 짐짓 목소리를 내리깔았다.

“본가가 위기에 처했는데 도망치겠다는 말이냐?”

솔직히 나였으면 도망쳤다.

“아닙니다!”

21세기 직장인이었다면 산재 처리 해 주겠다고 해도 면상에 침 뱉고 돌아섰을 텐데, 정찰조원들은 생각 이상으로 충성스러웠다. 혁무진도 창백한 얼굴로 검을 뽑아 들었다.

“좋습니다. 무인이라면 죽더라도 싸우다 죽어야죠.”

“각오는 좋은데, 죽지는 마라.”

“방금은 고기 방패라면서요?”

“너, 나 못 믿어?”

“예.”

혁무진의 칼 같은 대답에 정찰조원들 사이로 가벼운 웃음이 번졌다. 난생처음 겪는 대규모 전투에 얼어붙어 있던 몸이 한결 풀어지는 기분이다.

나도 씩 웃으며 창을 움켜쥐었다.

“눈 크게 뜨고, 귀 활짝 열어. 내 명령대로만 움직이면 살아서 돌아간다.”

그건 스스로에게 하는 다짐이었다. 이 녀석들만큼은 어떻게든 살려 보겠다는.

‘부디 죽지 마라.’

이 전쟁이 어떻게 끝날지, 누가 죽고 살지는 나도 모른다.

다만 최선을 다할 뿐이다.

“가자.”

그 말과 함께 우리는 질풍처럼 달려 나갔다. 나를 꼭짓점으로 한 화살이었고, 명중시켜야 할 목표는 정해져 있었다.

‘대장로.’

또렷한 시야 너머로 백발의 노인이 보인다. 그의 발아래 쓰러진 한 사람과 가득 고인 피 웅덩이도.

뱃속에서부터 뜨거운 불덩어리가 치솟았다.

“우리 형한테…….”

누군가의 시체 위에 묘비처럼 박혀 있던 창 한 자루를 뽑아 들었다. 그리고 다음 순간.

“손 떼, 이 새끼야!”

일직선으로 쏘아진 창이 수십 장의 거리를 압축시켰다.

정찰조원 중 누군가의 입에서 억눌린 외침이 튀어나왔다.

“됐다!”

대장로의 검이 움직인 것도 그때였다.

슉.

한 줄기 빛. 반쪽으로 갈라진 창이 양옆으로 튕겨져 나간다.

앞서와 똑같은 결과다. 하지만 이번에는 대장로와의 거리가 상당히 좁혀진 덕분에 똑똑히 목격할 수 있었다.

순간적으로 검신을 타고 솟구친 푸른 섬광을.

‘오라(Aura)?’

아니, 저게 여기서 왜 나와.



* * *



오라.

최소 A급 헌터는 되어야 뽑아낼 수 있다는 마나의 결정체.

마나와 공력은 이름만 다를 뿐, 기(氣)라는 면에서는 동일하다. 이곳은 무림이니까, 바꿔 말하자면 검기다. 검기.

허허허.

‘시발, 장난하나.’

대장로가 고수인 건 진작 알고 있었다. 여차하면 한판 붙을 각오도 했다. 문제는 ‘검기를 쓰는’ 대장로가 내 계획에 없었다는 거지.

‘이건 좀 아닌데.’

슬쩍 고개를 돌려 보니 십여 쌍의 흔들리는 동공들이 보인다.

그중에서도 혁무진의 눈동자는 거의 지진 수준이다.

“저, 조장.”

“으, 응?”

“방금 저거, 검기 같은데요.”

“그러게…….”

“조장도 검기 쓸 줄 아세요?”

“그런 거 있었으면 진작 썼지. 조필도 저 정도는 아니었어.”

“그렇죠?”

“그렇지. 근데 너 안 힘들어?”

“토할 것 같아요.”

우리는 약속이라도 한 것처럼 속도를 늦췄다. 100m 달리기에서 경보로 종목이 바뀌었지만 사자 아가리로 들어가는 기분은 똑같다.

“저기, 조장.”

혁무진이 핏기 하나 없는 얼굴로 입을 열었다. 피부색 하나만큼은 백인이라고 해도 좋을 정도다.

“대장로님이 배신한 거 확실해요?”

“확실해.”

“혹시 오해일 수도…….”

말이 끝나기도 전에 흑의인 서너 명이 고함과 함께 달려들었다.

“주군을 지켜라!”

“대장로님을 위하여!”

대사 봐라, 태원진가 망년회 건배사로 써도 되겠다. 달려드는 흑의인들을 모조리 베어 버린 나는 혁무진을 바라봤다.

“어, 무슨 말 하려고 했었냐?”

“……별말 아니었어요.”

정신 승리에 실패한 혁무진은 침통한 얼굴로 고개를 떨궜다.

하지만 그것도 잠시. 한 발, 한 발. 대장로와 가까워질수록 녀석은 필사적으로 살아 나갈 구멍을 찾기 시작했다.

“사람들은 왜 싸워야 하는 걸까요?”

이 새끼 노벨 평화상 노리나.

“아까는 싸우다가 죽겠다며. 무인답게.”

“그거야 최악의 경우고요. 대화로 해결하면 좋잖아요.”

“대화 좋지. 근데 저쪽에서 먼저 암살자 보냈잖아.”

“아.”

“나도 창 던졌고.”

“아아.”

“던지면서 욕도 했어.”

“앗, 아아아.”

대장로와의 거리가 십여 장 안으로 좁혀졌을 때, 혁무진의 얼굴은 까맣게 죽어 있었다. 다른 정찰조원들도 말은 안 했지만 덜덜 떨고 있는 게 눈으로 보일 정도다.

물론 나도 비슷하다. 검기를 떠올리는 것만으로도 가슴이 벌렁벌렁한다.

‘된통 걸렸네.’

하지만 도망칠 생각은 없다. 그럴 거였다면 처음부터 돌아오지도 않았겠지. 현실에 만족하며 그냥 그렇게 살았을 거다.

이미 너무 멀리 왔다. 남은 길은 하나뿐이다.

“정지.”

내 말에 모두가 기다렸다는 듯이 멈춰 섰다. 혁무진은 극적인 평화 조약을 기대하는 얼굴이었지만 나는 창을 쥐고 앞으로 나섰다.

“어, 어디 가세요?”

“싸우러. 너희는 여기서 대기해.”

“미쳤습니까? 차라리 소가주님이 올 때까지 기다렸다가 합공을…….”

“저기 엎어져 있는 사람 보이지?”

“어, 네.”

“우리 형이야.”

하늘이 무너진 표정으로 나를 바라보던 혁무진이 한숨을 푹 내쉬었다.

“그럼 같이 가요.”

“뭐?”

“저 같은 고기 방패라도 있어야 승산이 쥐꼬리만큼이라도 생길 거 아닙니까.”

이 자식이 이렇게 기특한 생각도 하네.

나는 피식 웃고는 돌아섰다.

“죽으러 가냐? 간 좀 보고 돌아올 테니까 기다리고 있어.”

이제 대장로와의 거리는 삼 장에 불과했다.

그와 나, 누구든 한순간에 좁힐 수 있는 거리다.

공간 사이로 무거운 침묵이 짓눌렀다. 잠깐 사이에 손바닥이 축축하게 젖어 든다.

‘후우.’

하지만 나도 호락호락한 놈은 아니다. 고작 이류였던 30레벨 때 이미 절정 고수인 조필을 꺾었고, 현실로 돌아간 후에도 발전을 거듭해 왔다.

40레벨인 지금은 현실과 무림, 어느 곳에서도 제법 먹히는 고수라고 자부한다. 아니, 고수 맞다.

‘최대한 거리를 유지하면서 싸운다면…….’

불과 몇 센티 차이로 생사가 판가름 나는 싸움에서 창의 공격 범위는 엄청난 장점이다.

나는 대장로의 얼굴을 보며 호흡을 가다듬었다.

‘해볼 만하다.’

단숨에 공력을 끌어 올려 쇄도했다. 일 장. 대장로에게 창날이 닿을 수 있는 거리. 그리고 대장로의 검이 내게 닿을 수 없는 거리.

‘지금!’

대장로의 정수리를 향해 창날을 내리찍었다.

동시에 기다리던 시스템 알림이 울렸다.

띠링.



- 칭호, [승부사]의 효과가 적용됩니다.

- [근력]이 일시적으로 상승합니다.

- [민첩]이 일시적으로 상승합니다.

- [체력]이 일시적으로…….



승부사. 일대일 승부 시 전투 관련 능력치를 10% 상승시켜 주는 칭호 효과가 전신 곳곳에 스며들었다.

거기에 더해서.

슈왁!

능력치의 상승은 공격의 가속에도 영향을 끼쳤다. 순간 빛살 같은 속도로 떨어지는 창날이 대장로의 정수리를 노렸다.

‘이건…… 들어갔다.’

그건 확신이었다.

설령 그 괴물 같은 조필이었어도 피하지 못할 거라는 확신. 그러나 내가 상대하고 있는 사람은 조필이 아니었다.

대장로였다.

쾅!

굉음과 함께 창대가 진동했다. 제대로 보이지도 않을 만큼 빠른 속도로 창을 막아 낸 대장로가 싱긋 웃었다.

“제법이구나. 기대 이상이야.”

나는 대답할 틈도 없이 젖 먹던 힘까지 끌어 올렸다. 어지간한 고수도 견디기 힘들 만한 거력(巨力)이 실린 창이 그의 검을 짓눌렀다.

그그극.

기분 나쁜 마찰음과 함께 검이 점차 위로 들리기 시작…….

아니, 잠깐만.

‘아래로 가야지 왜 위로 와.’

그토록 힘을 줬는데 밀리는 건 오히려 나다. 내 황당한 표정에 대장로의 웃음이 진해졌다.

“애썼다만, 그 정도로 되겠느냐?”

다음 순간, 머리털이 쭈뼛 서는 감각이 전신을 급습했다.

츠츠츠.

검신 위로 피어오르는 푸른 아지랑이. 검기다.

미처 대응할 사이도 없이, 서서히 밀리고 있던 창두가 두부처럼 잘려 나갔다.

슁.

이제는 창이 아니라 봉(棒)이다. 장봉.

물러서는 나를 향해 다시 한번 검기가 번쩍였다.

슁.

장봉이 단봉이 되었다.

슁.

“…….”

시발, 쌍절곤도 이것보다 길겠다. 나는 창도, 봉도 아니게 되어 버린 철 막대기를 대장로를 향해 집어 던졌다.

슁.

“도망칠 셈이더냐?”

도망치다니, 섭섭한 소리를.

이미 투척과 동시에 옆으로 몸을 날린 후였다. 죽은 듯이 엎드려 있는 진위경의 옷깃을 꽉 붙잡았다.

‘됐다!’

내 목적은 처음부터 단 하나, 진위경의 구출이었다.

목적을 달성했으니 저 괴물 같은 노인네와 싸울 필요도 없다. 나는 진위경을 끌어안고 온 힘을 다해 몸을 날렸다.

쉬익- 쾅!

뒤늦게 날아든 검기가 지면을 갈랐다.

간발의 차로 대장로의 공격 범위를 빠져나온 우리를 혁무진과 정찰조원들이 에워쌌다.

“조장을 보호해라!”

“괜찮으십니까?”

나는 침묵했다. 당장 대장로를 피해 도망쳐야 한다는 사실도, 이곳이 전장이라는 사실도 잊었다.

머릿속에는 한 가지 의문만 가득했다.

‘뭐야, 이 사람.’

분명히 진위경을 구했는데, 그랬어야 했는데…….

지금 내 품에 안겨 있는 이 마초 아저씨는 누구란 말인가.

얼굴 가득한 칼자국과 핏발 선 눈동자. 나는 떨리는 목소리로 물었다.

“실례지만 누구……세요?”

그때 혁무진의 입에서 외마디 비명이 터졌다.

“억! 이천백!”

이천백? 어디서 들어 봤는데.

“이 사람 알아?”

“당연히 알죠!”

“친해?”

“무슨 개소립니까! 혈랑검 이천백이잖아요!”

“혈랑검이라고?”

“네! 바로 그 혈랑검……!”

“별호 멋있네. 고수 같고.”

혁무진이 머리를 쥐어뜯으며 외쳤다.

“항산검문 문주잖아요! 혈랑검 이천백!”

“……!”

나는 후다닥 물러났다. 이 아저씨가 이천백이라니. 식은땀이 주르륵 흐른다.

‘이소군 아버지잖아.’

내가 자기 아들을 독살했다고 생각해서 전쟁까지 일으킨 인간이다. 보복 차원에서 어른, 아이 가리지 않고 죽여 버린 냉혈한이기도 했다.

‘엉뚱한 인간 구한 것도 억울한데, 칼침까지 맞을 뻔했네.’

그러나 이천백에게는 그럴 만한 힘이 더 이상 남아 있지 않은 듯했다.

전신이 피투성이인 데다, 손 하나 까딱 못 하는 게 심각한 내상 혹은 점혈을 당한 것처럼 보였다.

‘그래도 다행이다. 진위경이 아니라서.’

내 마음을 읽은 것처럼 혁무진이 물었다.

“그럼 소가주님께선 어디 계신 겁니까?”

“모르지. 그리고…….”

황급히 녀석의 목덜미를 잡아당겼다. 방금까지만 해도 혁무진의 발이 있던 자리에 검 한 자루가 날아와 박혔다.

‘진짜로 된통 걸렸네.’

나는 한숨을 푹 내쉬고 말을 이었다.

“저 노인네가 보내 주겠냐?”

대장로가 너털웃음을 터트렸다.

“으하하, 이런 버르장머리 없는 놈을 보았나!”

“예의 바르게 행동하면 그냥 보내 줄 수 있나?”

“그러기에는 너무 멀리 왔다고 생각하지 않느냐?”

츠츠츠.

솟구치는 검기. 더 이상 말이 필요 없다.

시체들 사이에 박혀 있던 창을 뽑아 들었다. 그리고 모두의 시선 속에서 입을 뗐다.

“포위 대형, 펼쳐.”

오래된 헌터 명언 중 하나.

‘강한 몬스터는 있어도 잡지 못하는 몬스터는 없다.’

그걸 가능케 하는 것이 레이드(Raid)다.
```

## Current accepted English baseline

```markdown
# Chapter 58

The battlefield descended into chaos. At the signal, two hundred martial artists suddenly turned and swarmed in every direction like a pack of wolves.

“Kill them all!”

“Aaaaargh!”

They weren’t quite on the level of Gwak Jun and the assassins we’d fought earlier, but a honed-blade aura still poured off them.

The Jin Family of Taiyuan and the Mount Heng Sword Sect. If both factions’ martial artists joined forces, we’d have a real shot—but right now, that looked difficult.

*This is bad.*

At worst, I might have to pull Jin Wikyung out and run.

I was thinking that when the reconnaissance squad arrived behind me, breathing hard.

“Squad Leader, maybe we can—huff!”

The moment they saw what was happening in front of them, their eyes all popped wide. Hyuk Mujin, who came crawling up behind them, gaped as well.

“Bweeegh!”

“…So that was it.”

It must have been rough. After a fast, heavy burst of vomiting, Hyuk looked half-dead as he spoke.

“I think this is as far as I go.”

Anyone looking at him might have taken him for a wounded soldier who’d been stabbed while fighting bravely.

I gripped his shoulder hard.

“Mujin. You can do this.”

“No. I’m finished. I’ll only be a burden if I go.”

“A burden? You’re an excellent meat shie—”

“Excuse me?”

“Shield! You’re the Jin Family of Taiyuan’s shield!”

“I could have sworn you said meat shield.”

Ignoring Hyuk’s suspicious muttering, I hauled him to his feet. Right now, even a meat shield—no, a single extra hand—was precious.

Besides, apart from me, Hyuk was the strongest meat shield in the reconnaissance squad. Ah, it kept slipping out.

I deliberately lowered my voice.

“Our family is in danger, and you’re saying you want to run?”

If it had been me, I would have run.

“No, sir!”

A twenty-first-century office worker would have spat in your face and walked away, even if you’d offered to file it as a workplace injury. But the reconnaissance squad was more loyal than I’d expected. Hyuk drew his sword with a pale face.

“Very well. If a martial artist has to die, he should die fighting.”

“That’s a fine resolve, but don’t die.”

“You just called me a meat shield.”

“You don’t trust me?”

“Yes.”

Hyuk’s answer was as sharp as a blade, and a light laugh spread through the reconnaissance squad. They’d been frozen stiff by the first large-scale battle of their lives, but they seemed to loosen up a little.

I grinned and gripped my spear.

“Eyes wide, ears open. Follow my orders, and you’ll make it back alive.”

That was a vow I was making to myself. I would get these guys out alive somehow.

*Please don’t die.*

I didn’t know how this war would end, or who would live and who would die.

All I could do was give it everything I had.

“Let’s go.”

At that, we charged forward like a gale. We were an arrow with me at the tip, and the target we had to hit was already set.

*The Head Elder.*

Clear in the distance, I could see a white-haired old man. At his feet lay a fallen man, and a pool of blood.

A hot lump of fire surged up from my gut.

“That’s my brother…”

I pulled a spear from where it had been driven into someone’s corpse like a gravestone. Then, in the next instant—

“Get your hands off him, you bastard!”

The spear shot in a straight line, compressing dozens of yards of distance.

Someone in the reconnaissance squad let out a muffled cry.

“We got him!”

That was when the Head Elder’s sword moved.

Shuk.

A streak of light. The spear split in half and bounced away to either side.

Same result as before. But this time we’d closed the distance considerably, so I could see it clearly.

The blue flash that had surged along the blade for an instant.

*Aura?*

No. Why was that showing up here?

* * *

Aura.

A crystallization of mana that only an A-rank Hunter or higher could draw out.

Mana and internal energy were different only in name. In terms of qi, they were the same. And this was Murim, so put another way, it was Sword Energy.

Sword Energy.

Heh heh heh.

*Fuck. Are you kidding me?*

I’d known for a long time that the Head Elder was a master. I’d even been ready to fight him if it came to that. The problem was that a Head Elder *using Sword Energy* hadn’t been part of the plan.

*This is a bit much.*

I glanced aside and saw ten-odd pairs of shaking eyes.

Hyuk Mujin’s were practically seismic.

“S-Squad Leader.”

“Y-Yeah?”

“That just now… that looked like Sword Energy.”

“Yeah…”

“Can you use Sword Energy too?”

“If I could, I would have used it already. Even Jopil wasn’t at that level.”

“Right?”

“Right. But aren’t you exhausted?”

“I feel like I’m going to throw up.”

As if we’d agreed on it, we slowed down. The event had switched from a hundred-meter dash to race walking, but it still felt like walking into a lion’s jaws.

“Uh, Squad Leader.”

Hyuk opened his mouth with a face drained of all color. As far as his skin went, he could have passed for a white man.

“Are you sure the Head Elder betrayed us?”

“I’m sure.”

“Could it possibly be a misunderstanding—”

Before he could finish, three or four black-clad men charged at us with a shout.

“Protect our lord!”

“For the Head Elder!”

Get a load of those lines. They’d work as a toast at a Jin Family of Taiyuan year-end party.

I cut down every last black-clad man charging us, then looked at Hyuk.

“Uh, what were you about to say?”

“…Nothing.”

Having failed to win the argument in his head, Hyuk hung his head, looking grim.

But only for a moment. Step by step. The closer we got to the Head Elder, the more desperately he started hunting for a way out.

“Why do people have to fight?”

*Is this bastard aiming for the Nobel Peace Prize?*

“You said earlier you’d fight and die. Like a martial artist.”

“That was the worst case. Wouldn’t it be better to settle this with talk?”

“Talk’s good. But they sent assassins after us first.”

“Oh.”

“And I threw a spear.”

“Ah.”

“And I cursed while throwing it.”

“Ah—ahhh.”

When we closed to within about a hundred feet of the Head Elder, Hyuk’s face looked like death. The other reconnaissance squad members didn’t say anything, but I could see them shaking.

Of course, I wasn’t much different. Just thinking about Sword Energy made my chest hammer.

*I’m well and truly screwed.*

But I had no intention of running. If I had, I never would have come back in the first place. I would have been content with reality and just lived that way.

I’d already come too far. There was only one path left.

“Stop.”

Everyone halted as if they’d been waiting for it. Hyuk’s face said he was hoping for a dramatic peace treaty, but I gripped my spear and stepped forward.

“W-Where are you going?”

“To fight. You wait here.”

“Are you insane? We’d be better off waiting for the Lesser Family Head and attacking together—”

“See the person lying over there?”

“Y-Yes.”

“That’s my brother.”

Hyuk looked at me like the sky had fallen, then let out a long sigh.

“Then I’m coming with you.”

“What?”

“Even a meat shield like me should bump our odds up by a hair, shouldn’t it?”

This guy actually came up with some admirable thoughts.

I snorted a laugh and turned away.

“You going there to die? I’m just going to test the waters and come back. Wait here.”

The distance to the Head Elder was now barely thirty feet.

A distance either of us could close in an instant.

A heavy silence crushed the space between us. In that brief interval, my palms went damp.

*Phew.*

But I wasn’t an easy mark either. At Level 30, when I was only Second Rate, I’d already beaten Jopil, a Peak master. And I’d kept improving after I went back to reality.

At Level 40, I could proudly call myself a master who held his own in both reality and Murim.

No. I was a master.

*If I fight while keeping as much distance as I can…*

In a fight where a few centimeters could decide life or death, a spear’s reach was a massive advantage.

I looked at the Head Elder’s face and steadied my breathing.

*This is doable.*

I drew up my internal energy in a single burst and charged. Ten feet—the range where my spearhead could reach the Head Elder, and his sword couldn’t reach me.

*Now!*

I brought the spearhead down toward the crown of his head.

At the same time, the System notification I’d been waiting for rang out.

Ding.

> **System**
>
> - The effect of the Title **Gambler** is applied.
> - **Strength** temporarily increases.
> - **Agility** temporarily increases.
> - **Stamina** temporarily…

The effect of the Gambler Title, which raised combat-related stats by ten percent in a one-on-one duel, seeped through my whole body.

And on top of that—

Whoosh!

The boost to my stats accelerated the attack as well. In an instant, the spearhead dropped like a bolt of light, aimed at the crown of the Head Elder’s head.

*This is going in.*

That was certainty.

The certainty that even a monster like Jopil wouldn’t have been able to dodge it. But the man I was facing wasn’t Jopil.

He was the Head Elder.

Boom!

The spear shaft shuddered with a thunderous crash. The Head Elder, having blocked the spear at a speed too fast to see properly, smiled faintly.

“Not bad. Better than I expected.”

Without even time to answer, I wrung out every last ounce of strength. The spear, loaded with tremendous force that even a decent master would have struggled to endure, crushed down on his sword.

Grrrkk.

With an ugly grinding sound, his sword began to lift…

No. Wait.

*It should be going down. Why is it coming up?*

I’d put that much force into it, and I was the one being pushed back. At my dumbfounded expression, the Head Elder’s smile deepened.

“You tried, but did you think that would be enough?”

The next instant, every hair on my body stood on end.

Tsssss.

A blue haze bloomed along the blade.

Sword Energy.

Before I could even react, the spearhead that had been slowly getting pushed back was sliced off like tofu.

Shing.

Now it wasn’t a spear but a staff. A long staff.

Sword Energy flashed again toward me as I backed away.

Shing.

The long staff became a short staff.

Shing.

“…”

Fuck. Even nunchaku would be longer than this.

I threw the iron rod—no longer a spear or a staff—at the Head Elder.

Shing.

“Do you intend to run?”

Run? That’s a hurtful thing to say.

I’d already thrown myself sideways at the same moment I threw it. I grabbed the collar of the man lying facedown as if he were dead.

*Got him!*

My only goal from the beginning had been to rescue Jin Wikyung.

Now that I’d done it, there was no reason to fight that monstrous old man. I scooped Jin Wikyung into my arms and hurled myself away with all my strength.

Whoosh—boom!

The Sword Energy that arrived a beat later split the ground.

Hyuk Mujin and the reconnaissance squad surrounded us as we slipped out of the Head Elder’s range by a hair.

“Protect the Squad Leader!”

“Are you all right?”

I said nothing. I forgot we had to run from the Head Elder right now. I even forgot this was a battlefield.

My head was full of a single question.

*Who is this man?*

I had definitely rescued Jin Wikyung. I was supposed to have rescued him…

Then who was this macho middle-aged man in my arms?

His face was covered in sword scars, and his eyes were bloodshot. In a trembling voice, I asked,

“Excuse me, but who are you…?”

At that moment, a single cry burst from Hyuk Mujin’s mouth.

“Gah! Lee Cheonbaek!”

Lee Cheonbaek? The name rang a bell.

“You know him?”

“Of course I do!”

“Are you close?”

“What kind of bullshit is that? That’s Blood Wolf Sword Lee Cheonbaek!”

“Blood Wolf Sword?”

“Yes! That Blood Wolf Sword…!”

“Cool alias. Sounds like a master.”

Hyuk tore at his hair and shouted,

“He’s the Sect Leader of the Mount Heng Sword Sect! Blood Wolf Sword Lee Cheonbaek!”

“…”

I scrambled backward.

This man was Lee Cheonbaek?

Cold sweat rolled down me.

*He’s Lee Seogeun’s father.*

He was the man who’d started a war because he thought I’d poisoned his son. He was also a cold-blooded killer who’d slaughtered adults and children alike in revenge.

*Rescuing the wrong guy was unfair enough, and I nearly got stabbed too.*

But Lee Cheonbaek no longer seemed to have the strength left for that.

His whole body was covered in blood, and he couldn’t so much as twitch a hand. It looked like severe internal injuries, or like his acupoints had been sealed.

*Still, at least it isn’t Jin Wikyung.*

As if he’d read my mind, Hyuk asked,

“Then where is the Lesser Family Head?”

“I don’t know. And…”

I yanked him back by the nape of his neck. A sword came flying in and buried itself where Hyuk’s foot had been a moment before.

*I’m really well and truly screwed.*

I let out a long sigh, then went on,

“You think that old man is going to let us go?”

The Head Elder burst into a hearty laugh.

“Ha ha ha! Have you ever seen such an insolent brat!”

“If I behave politely, will you let us go?”

“Don’t you think you’ve come too far for that?”

Tsssss.

Sword Energy surged up.

No more words were needed.

I pulled a spear stuck among the corpses. Then, with everyone’s eyes on me, I spoke.

“Encircling formation. Spread out.”

One of the oldest Hunter sayings was this:

*There are strong monsters, but no monster that can’t be taken down.*

What made that possible was a raid.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 58`.

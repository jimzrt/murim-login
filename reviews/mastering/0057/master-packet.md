# Master Edit Task — Chapter 57

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
| 이천백    | **Lee Cheonbaek**  |
| 이소군    | **Lee Seogeun**    |
| 화양검    | **Blade of Flowers**          | Jin Baekyang   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 산서오문   | **Five Gates of Shanxi**         |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 귀문      | **your sect**                                                   |
| 공자      | **Young Master**                                                |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |

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

#### Chapter 55 tail (verified mastered)

…
sudden? Seriously.” “No time. Answer quickly.” “You were breathing, that’s why you woke up. Otherwise you’d be dead.” Fair enough. Apparently, logging in or logging out put the other side into a deathlike state. *If I’d logged out before dealing with the assassins, there wouldn’t have been a body to come back to.* I’d think about that later. There was a more urgent problem. “The main force?” “We were already heading that way. We split two men off and sent them back to the family.” “Good. How much farther?” “At least another two hours.” “Two hours…” “Uh, Squad Leader. I’m sorry to say this, but… I think we have to consider the worst case.” Hyuk Mujin and every member of the reconnaissance squad clamped their mouths shut. Nobody had to ask what the worst case meant. *I’ve thought about it too.* From what Gwak Jun had said right before he died, this betrayal had been planned down to the last detail for a long time. But the plan had exactly one error. *Me.* The Head Elder had underestimated me. No—maybe, in another way, he’d overestimated me. He’d sent dozens of First Rate masters just to kill me. Even that hadn’t been enough. I had survived. *He made a mistake.* On top of that, when Gwak Jun first revealed his true colors, he’d said they needed to start moving soon if they wanted to make it on time. Which meant… “It’s not too late.” I met each squad member’s eyes and spoke firmly. “Don’t think about the worst case. No matter what it takes, I’ll change that outcome.” “Squad Leader…” “So, Mujin.” I gave Hyuk’s choked-up face a good-natured smile. “Get up. Now.” “I’m dying here.” “Want to get beaten to death instead?” “…” “Run even one more step in the time we’ve got. Don’t you know marathon spirit?” “I don’t.” Ah. Right. This was Murim. “Anyway, get up. Another hour will do it.” Hyuk grabbed his trembling legs and pushed himself up, then cocked his head. “An hour?” “Yeah. An hour.” “I already told you. Even at full speed, it’ll take two.” “Exactly. An hour.” “What are you even saying…” “Mujin.” “Yes?” Hyuk blinked at me, as simple as an ox. I smiled even brighter. “Ever heard of grit?” Two hours or four, I didn’t care. We were getting there in an hour. Period. “Run like hell. That’ll do it.” “Huk.” Every face in the reconnaissance squad went deathly pale. * * * “We’ve been blocked.” “Casualties are heavy. Sect Leader, please take action.” Despite the continuing reports, Blood Wolf Sword Lee Cheonbaek, Sect Leader of the Mount Heng Sword Sect, kept his eyes closed. *I was too hasty.* The war had begun in a rush, and their preparations had been equally inadequate. Their provisions were rapidly dwindling, morale was falling, and men were deserting one after another. *They read us completely.* Rage at losing his son and impatience with the situation had clouded his judgment. He had ignored his subordinates’ advice and taken the fastest route he could find. And that was how he had run into the Jin Family of Taiyuan in a narrow gorge whose very name was unfamiliar: Eight Spring Gorge. “Sect Leader!” At his subordinate’s shout, Lee Cheonbaek slowly opened his eyes. The fearsome vision of a Peak master pierced the battlefield. “Gaaah!” “Wipe them out! They’re nothing but rabble!” Well over a thousand of his own men were jammed at the narrow mouth and couldn’t advance. The wandering martial artists and mounted bandits he’d put at the front had numbers, but man for man they were worse than even the Jin Family’s rank-and-file. *Sword fodder, at best.* Just as he was clicking his tongue inwardly, several dozen wandering martial artists suddenly started peeling off the front line. The middle-aged wanderer at their head bellowed until his throat tore. “We’ll die like dogs at this rate! Brothers of the Blood Rain Group, fall back!” Those became the middle-aged wandering martial artist’s last words. Whoosh— A light breeze. The wandering martial artist felt nothing else. He did not know that Blood Wolf Sword Lee Cheonbaek had already brushed past him. He did not know that the wandering martial artists under him had frozen in terror. He only thought, suddenly, that his neck was hot. “Uh…” His cleanly severed head dropped with a dull thud. The headless body staggered a few more steps, then collapsed like a rotten old tree. “The Blood Rain Group, was it?” Lee Cheonbaek pointed his sword at the petrified wanderers. Not a single drop of blood stained its blade. “Go back.” A Peak master’s killing intent shot into them like a blade. The wandering martial artists charged toward the front even faster than they had come. They had decided that fighting on the front line was better than throwing themselves at the Peak master before them. “Rat bastards.” Lee Cheonbaek went after them. His burning gaze was aimed somewhere ahead, where the Jin Family of Taiyuan’s command had to be. “The Sect Leader is taking the lead!” “Everyone, charge! Wipe out the Jin Family of Taiyuan!” As Lee Cheonbaek stepped forward, the Mount Heng Sword Sect’s core forces followed. Three Peak masters and dozens of First Rate masters crashed toward the front. [^1]: A riff on the Korean pop song “My Ear’s Candy”; Taekyung follows it with a parody of the lyrics.

#### Chapter 56 tail (verified mastered)

…
saw the white beard fluttering in the wind. And the sword in the old man’s hand. Boom! *Kh.* The thunderous impact sent Lee Cheonbaek reeling backward. He was not even given time to register the pain in his wrist. Boom! Boom! Boom! Every time the two swords met, thunder and lightning rolled. Sword Energy poured out in a continuous stream, smashing the ground and tearing the wind. Whoosh! “What in the world is that…?” The martial artists of both sides forgot they were fighting. They could only stare, slack-faced, at this staggering life-and-death duel. In that moment, every one of them was thinking the same thing. *Are those two really human beings like us?* The ceaseless thunder. A feast of Sword Energy so dazzling it left them spellbound just to watch. The movements of the two men at its center were faster and stronger than anyone they had ever seen. Someone muttered, almost a groan. “So this is a Peak master…” To their eyes, it was a fight where either outcome would have made sense. But the superiority in strength was obvious. After some three hundred exchanges, the Head Elder’s sword changed. Whoosh—slice! “Ghk.” Lee Cheonbaek bit his lip. Blood streamed from the forearm the Head Elder’s sword had raked. The strength drained from his sword hand. *Of all things.* He quickly shifted the sword to his other hand, but he was a right-handed swordsman by nature. Even at full power he would have been hard-pressed. Now that his sword arm was injured, the outcome was all but decided. Boom! Crack. A single blow snapped his wrist. His Sword Energy, weakened by the severe drain on his internal energy, could no longer stand against the Head Elder. But Lee Cheonbaek did not give up. *Not yet. It isn’t over yet.* He had suffered worse injuries than this countless times. Drawing on the strength in his arm, waist, and legs, Lee Cheonbaek swung his sword. No—he tried to. Slash! This time, it was the knee. With its tendons severed, the knee buckled slowly, with no regard for Lee Cheonbaek’s will. His sword carved uselessly through empty air. Shhk. Shhk-shhk-shhk. His side. His shoulder. His chest. Lightning stabbed and sliced through his entire body. The fierce Sword Energy did more than cut through flesh and bone—it churned his insides. “Bleeegh!” Lee Cheonbaek vomited blood mixed with pieces of his organs and looked up at the Head Elder through clouded eyes. The old man’s face was impassive. There was no thrill at having defeated his opponent. No joy that the war was ending. To him, all of this was simply the natural result. “Cough… So Shanxi’s Number One was standing right in front of me.” “If you’re not Number One Under Heaven, you’re nothing more than a martial brute from the frontier. Neither you nor I have that kind of capacity.” “Tell me what you want. I’ll give you my neck. I’ll make my men surrender, and I’ll seal the sect for ten years—or a hundred. So…” “Impossible. What I want is annihilation. Complete annihilation, without a single blade of grass left standing.” “Why…!” “Don’t ask me that. If you had won, our family would have been the one facing annihilation.” Lee Cheonbaek glared at the Head Elder with bloodshot eyes. He wanted to snap that wrinkled neck then and there. But with wounds this severe, all he could do was wring out a voice. “The Jin Family of Taiyuan… You bastards started this, didn’t you? You killed that young boy—my son!” “Ah, Lee Seogeun. That’s right. That child was where it began.” The Head Elder wore a sardonic smile. Even the master of the Mount Heng Sword Sect, one of the two powers that divided Shanxi between them, had failed to notice *their* intervention. Not even now, with death at his doorstep. —When you meet King Yama, ask him. Ask who killed Lee Seogeun. The Sound Transmission burrowed into Lee Cheonbaek’s ear, and his eyes flew wide. “What does that mean…?” It was a thoroughly impulsive act. Perhaps pity for Lee Cheonbaek, who was about to die knowing nothing. Or perhaps nothing more than an old man’s whim. —Fare for the road to the afterlife. Think it over on the long journey. The Head Elder raised his sword. The sunset beyond the winter ridge shattered into fragments along the blade. *With this…* With the death of the giant known as Lee Cheonbaek, the Mount Heng Sword Sect would collapse. Those who resisted would die. Those who surrendered would be taken prisoner. One war would end like that… And a new war would begin at the very moment everyone was drunk on victory. *It’s over.* At last, the Head Elder’s sword moved. Screeeech—! A sharp sound tore through the air. Sensing his end, Lee Cheonbaek closed his eyes. The blade wrapped in blue Sword Energy traced a beautiful line. Slice. But both the tearing sound that had come first and the direction of the sword defied Lee Cheonbaek’s expectations. The Head Elder split a spear that came flying at his back out of nowhere, cutting it apart with Sword Energy. An enraged roar burst from his mouth. “Who the hell are you!” The answer came the next instant. “It’s me, you fucking bastard!” The Head Elder saw the face of a young man standing tall on a low hill, and groaned. “Jin Taekyung?”

## Korean source

```text
＃57화



“빨리, 더 빨리!”

“헉, 허억!”

우리는 그야말로 미친 듯이 달렸다. 혁무진은 당장 죽을 것처럼 헐떡거렸지만 죽지는 않았다. 발걸음이 느려질 때마다 등에 창날을 가져다 댔더니 적토마가 따로 없더라.

그리고 어느 순간, 소리가 들리기 시작했다.

누군가의 비명 소리, 철과 철이 부딪치는 소리…….

다행이다. 전투는 아직 끝나지 않았다.

안도감과 동시에 심장이 쿵쿵 뛰었다. 전투는 계속되고 있지만 진위경의 생사는 아직 확인하지 못했다.

일 분, 일 초 차이로 그가 죽는다면?

‘만약 그렇다면.’

까드득.

나도 모르게 창을 쥔 손에 힘이 들어갔다. 단전에서 끌어올린 공력을 두 다리로 흘려보냈다.

“조, 조장!”

빠르게 멀어져 가는 정찰조원들의 목소리를 뒤로하고 계속해서 달렸다. 앞서 본대가 새겨 놓은 무수한 족적, 점점 가까워지는 전장의 소음이 이정표였다.

‘살아 있어라. 살아 있어라. 제발 살아…….’

아! 비로소 보인다.

야트막한 언덕 아래, 불과 200여 미터도 떨어지지 않은 그곳에서 수많은 무인들이 죽고 죽이는 혈전을 벌이고 있었다.

“죽엇!”

“으아악!”

시체와 피, 그리고 더 많은 시체, 피!

순간 할 말을 잃을 정도로 눈앞에 펼쳐진 광경은 잔혹했다.

헌터 생활을 통해 내성을 기르지 않았다면 아마 한참 동안이나 충격에서 헤어 나오지 못했을 것이다.

‘진위경! 진위경은 어디 있지?’

하지만 가장 먼저 눈에 들어온 사람은 따로 있었다.

멀리서도 한눈에 들어오는 백발.

‘대장로!’

그는 검을 들고 누군가의 앞에 서 있었다.

대장로의 등에 가려 잘 보이지는 않았지만 무릎을 꿇은 그는 거구의 소유자였고, 손에는 검을 쥔 채였다.

‘큰 덩치와 검?’

한 사람밖에 생각나지 않았다.

진위경이다. 그를 구하려면 당장 움직여야 한다.

‘인벤토리 오픈.’

무림에서 사용하는 인벤토리에는 온갖 물건으로 가득했다.

창대는 나무로, 창두는 강철로 만들어진 이 창도 그중 하나다.

‘무기 장착.’

새로 꺼낸 창을 들고 뒤로 몇 걸음 물러났다.

200여 미터. 까마득한 거리다. 투창으로 누군가를 맞추기에는 더더욱. 하지만 해내야 한다.

‘못 할 것도 없지.’

근력, 체력, 민첩.

무림과 현실을 오가며 키워 온 능력치를 한껏 끌어 올렸다.

공력이 깃든 팔은 창을 좀 더 멀리, 강하게 쏘아 보낼 수 있을 것이다.

“후웁.”

숨을 멈추고 발을 디뎠다. 첫발은 천천히, 마지막 한 걸음은 무겁게. 채찍처럼 휘두른 손끝에서 창대가 쏘아졌다.

쐐애애액-!

투창은 내 예상보다 빠르고 정확했다. 금방이라도 대장로의 등을 꿰뚫을 것 같았다.

그런데…….

서걱.

‘뭐야, 저거.’

푸른빛이 번쩍하더니 창이 두 쪽으로 갈라졌다. 가장 윗부분인 창두부터 끝까지, 깔끔하게.

내가 던진 게 창인지 생일 케이크인지 헷갈릴 정도다.

“웬 놈이냐!”

노인네가 목청도 좋다.

“나다, 이 십새끼야!”

아마 대장로 평생 들어 본 적 없는 욕일 것이다.

심지어 무림에서 그와 나는 한 집안 사람이고, 족보로 따지자면 시조새와 병아리 정도의 항렬 차이가 있다.

이것만 해도 당황할 이유는 충분한데, 내게는 결정적인 한 방이 남아 있었다.

“대장로는!”

공력이 담긴 목소리가 쩌렁쩌렁 울렸다. 목소리를 낸 나도 놀랄 정도인데 다른 이들이 듣기에는 어떨까.

저 멀리, 차가운 표정으로 굳은 그를 응시하며 있는 힘껏 외쳤다.

“배신자다!”



* * *



진위경이 그 목소리를 들은 것은 항산검문의 절정 고수 세 명을 모두 쓰러트린 직후였다.

아니, 진위경뿐만 아니라 전장의 모두가 그 외침을 들었다.

- 웬 놈이냐!

- 나다, 이 십새끼야!

욕?

전장에서는 흔한 일이다. 그러나 욕설의 대상이 대장로라면, 난데없이 나타나 쌍욕을 퍼부은 청년이 진태경이라면 이야기가 달라진다.

“저거, 저거 삼공자 아냐?”

“뭣? 저놈이 진태경? 그런데 왜?”

“이게 무슨 일이야?”

진위경도 같은 생각을 했다.

‘무슨 일이 벌어지고 있는 거지?’

후방에 있어야 할 막내가 전장에 나타났다. 그것만으로도 당황스러운데, 가문의 웃어른에게 입에 담지도 못할 폭언을 쓰기까지 했다. 옆에 있던 위팽이 중얼거렸다.

“단단히 미쳤군.”

진위경이 저도 모르게 고개를 끄덕이려던 순간.

- 대장로는!

더 거대한 폭탄이 떨어졌다.

- 배신자다!

전장이 싸늘한 침묵에 잠겼다. 간간이 들려오던 병장기 부딪치는 소리도 뚝 끊겼다.

모두가 멍한 표정으로 진태경을 바라봤다.

‘이게 무슨 개소리야?’

‘배신? 대장로님께서?’

‘취한 거 아냐? 삼공자 저거 옛날 버릇 또 튀어나오네.’

태원진가의 무사는 말할 것도 없었고, 항산검문의 무사들도 비슷한 생각을 품었다.

최근 들어 진태경을 좋게 보기 시작한 중진들도 입을 딱 벌렸다.

“저런 미친놈.”

“노야께서 어떤 분이신 줄 알고!”

이 전쟁의 일등 공신을 꼽으라면 단연 대장로다.

진위경을 도와 가문의 힘을 결집시켰고 오늘 전투에서는 이천백을 꺾었다.

이처럼 이번 전쟁의 단순한 공(公)을 떠나 생각해 봐도 진태경의 말은 헛소리로 들릴 수밖에 없었다.

대장로가 누군가?

화양검이라 불리며 중원에까지 이름을 떨친 전대의 고수요, 정마대전에서 수많은 마두를 쓰러트린 의기의 표상이다.

산서성의 무인이라면 누구나 그에게 크고 작은 존경심을 품고 있었다.

“그런 분을, 뭐? 십새끼? 배신자?”

“허어, 저놈이 태원진가 삼백 년 역사에 똥칠을 하는구나.”

태원진가, 항산검문. 이 자리의 모두가 같은 생각을 품은 듯했다. 그러나 적어도 한 사람은 예외였다.

‘대장로, 배신.’

막내의 말을 들은 순간, 진위경은 온몸의 피가 싸늘하게 식는 것을 느꼈다. 그건 실체를 드러낸 위화감이었다.

‘이소군의 죽음이 시작이었지.’

그는 극독에 중독되어 죽었다. 항산검문은 태원진가를 범인으로 지목했고, 그것이 전쟁의 시발점이다.

하지만 가장 중요한 의문은 빠져 있었다.

‘흉수는 누구인가?’

전쟁이 막바지에 이른 지금까지도 배후에 숨겨진 흉수에 대해서는 밝혀지지 않았다. 아니, 막바지에 다다랐기 때문에 아무도 흉수의 정체를 신경 쓰지 않았다.

적자생존. 강한 자가 살아남아 모든 것을 독식할 테니까.

‘이 전쟁은…… 처음부터 잘못된 거였어.’

이소군의 죽음. 비상식적으로 빠른 소문의 확산.

항산검문이 전쟁을 선언했고, 태원진가가 대응하면서 본격적인 싸움이 시작되었다.

‘그리고 대장로가 있었다.’

두문불출하던 대장로가 나타난 것은 이소군의 독살 소식이 전해진 직후다. 가문 내에서 그의 역할은 지대했다.

존경받는 무인, 가문의 웃어른.

대장로가 적극 협조하지 않았다면 태원진가는 둘로 갈라졌을지도 모른다.

‘그의 도움 덕분에 여기까지 올 수 있었다.’

진위경은 반대로 생각했다.

‘여기까지 올 수 있었던 것은, 대장로가 원했기 때문이다.’

촌각(寸刻)이라 부르지도 못할 만큼 짧은 순간. 모든 생각을 끝마친 진위경의 입이 열렸다.

“위팽.”

“하명하십시오.”

“일장로를 베어라.”

“뭐라?”

허리가 구부정하고 깡마른 노인, 일장로가 눈을 부릅떴다.

그뿐만 아니라 주위에 있던 중진들 모두가 깜짝 놀랐다.

“소, 소가주!”

“이 무슨……!”

그러나 위팽은 망설이지 않았다. 부지불식간에 휘두른 검이 일장로의 가슴을 향해 날아갔다.

카가가각.

그때 갑자기 끼어든 두 개의 검이 위팽의 검을 밀어 냈다.

뚱뚱하고 키가 훌쩍 큰 두 명의 노인.

일장로와 함께 대장로의 수족을 자처하는 이, 삼장로였다.

그들의 검에 맺힌 희미한 검기를 확인한 위팽의 눈썹이 꿈틀거렸다.

“무공을 숨겼군.”

대답 대신 일장로의 일권(一拳)이 날아왔다.

쾅!

살아온 세월만큼이나 심후한 공력으로 위팽을 날려 보낸 일장로가 허리를 곧게 폈다.

평생을 대장로의 그늘에 가려져 있었던 또 다른 절정 고수의 등장에 장내가 얼어붙었다.

“일장로님, 이, 이게 도대체.”

“그럼 혹시!”

배신. 그 두 글자가 모두의 뇌리에 선명하게 박혔다.

“말도 안 되는 소리!”

빽 소리친 사람은 백호당주였다. 대장로의 수족이 장로들이라면 그는 일장로의 손발 노릇을 톡톡히 해냈다.

“어르신, 그리고 소가주. 뭔가 오해가 있으신 모양인데…….”

그러나 그의 말은 끝까지 이어지지 못했다. 일장로의 턱짓과 동시에 이장로가 눈부신 속도로 백호당주의 목을 베었기 때문이었다.

서걱. 툭.

진위경과 일장로의 시선이 허공에서 부딪쳤다.

“백호당주도 포섭한 게 아니었나?”

“시끄러운 놈이었네. 그뿐이야. 다른 놈들도 마찬가지고.”

진위경의 예상은 반은 맞고 반은 틀렸다.

장로들이 배신한 것은 맞지만, 장로파에 속한 중진들은 배신하지 않았다.

“그럼 왜…… 아!”

“영민하군. 칭찬해 줌세.”

일장로가 품에서 거무튀튀한 죽통(竹筒)을 꺼내 들었다. 이미 타들어 가고 있는 심지가 얼마 남지 않았다.

“저런 놈들에게 중요한 비밀을 말해 줄 수야 있나. 내부만 혼란스럽게 만들어도 쓰임새는 다한 거지. 밖에서 무슨 일이 벌어지는지 몰라야 일이 편했으니까.”

진위경이 비명처럼 외쳤다.

“막아!”

“늦었네.”

일장로의 말이 맞았다. 심지가 끝까지 타들어 간 순간, 무언가 터지는 소리와 함께 붉은 불꽃이 하늘 높이 솟구쳤다.

쉬이익, 펑!

그것이 신호였다.

세 개의 문파 연합체인 삼도문, 도를 중심으로 수련하는 벽도문, 절벽에서 쉴 새 없이 화살을 쏘아 대던 궁귀문까지.

이른바 산서오문이라 불리는 중소 문파의 무인들이 한순간에 돌변했다.

“닥치는 대로 죽여라!”

“가릴 것 없다! 모두 쓸어 버려라!”

그들은 더 이상 어설픈 삼류 무인들이 아니었다. 눈에서는 살기가 흘렀고 검로는 날카로웠다.

‘하루아침에 준비한 일이 아니다.’

진위경의 얼굴이 딱딱하게 굳었다.



* * *



펑!

대장로는 고개를 들어 하늘을 바라보았다. 붉은 불꽃이 사그라지기도 전에 사방에서 거대한 함성이 터져 나왔다.

‘빠르군. 너무 빨라.’

신호를 터트리는 순간은 항산검문이 괴멸한 뒤가 되어야 했다. 산서오문은 수십 년 동안 준비한 칼이다. 단 한 번 휘둘러 전광석화처럼 끝내야 했다.

‘모든 일에는 흐름이 있는 법이거늘.’

막힘없이 흘러가던 계획이 어긋나기 시작했다. 씁쓸하게 웃는 대장로의 귓가로 한 줄기 음성이 파고들었다.

“네, 네놈이었구나.”

이천백이다. 희미한 목소리였지만 눈은 어느 때보다도 맹렬하게 타오르고 있었다.

“아직도 말할 기운이 남아 있나?”

“네놈을 산채로 갈기갈기 찢어 죽일 것이다.”

그러나 말을 마치기가 무섭게 이천백의 입에서 핏물이 쏟아졌다. 대장로가 그의 혈도를 짚으며 중얼거렸다.

“아직은 곤란하네. 자네가 해야 할 일이 있거든.”

이천백은 절망했다.

큰 손실이 있었다고는 하나 아직 항산검문에는 수백의 무인이 남아 있다. 수뇌부까지 괴멸한 이 시점에서 문주가 포로로 잡힌다면…….

‘차라리 죽여라!’

비통한 외침은 입 밖으로 새어 나오지 못했다. 아혈(啞穴)이 짚여 말을 할 수 없게 되었고, 이어 대장로의 손이 마혈(痲穴)을 스치자 몸이 딱딱하게 굳었다.

이천백이 눈 뜬 산송장이 된 순간이었다.

“이 새끼야! 거기 손 안 떼!”

동시에 파공성이 일었다.

쐐애애액-!

대장로는 당황하지 않고 검을 아래에서 위로 그어 올렸다. 검기를 따라 반으로 갈라지는 창 너머, 진태경이 무서운 속도로 달려오고 있었다.

“이야아아아!”

“조장! 제발 천천히 좀!”

어디서 나타났는지 모를 십여 명의 떨거지들과 함께.
```

## Current accepted English baseline

```markdown
# Chapter 57

“Faster! Faster!”

“Huff… huff!”

We ran like mad. Hyuk Mujin was panting like he was about to drop dead, but he didn’t. Whenever his steps started to slow, I put the spearhead to his back, and he might as well have been Red Hare.[^1]

Then, at some point, the sounds started to reach us.

Someone’s screams. Steel ringing on steel…

Good. The battle wasn’t over yet.

Relief hit me, and my heart hammered at the same time. The fighting was still going on, but I still hadn’t confirmed whether Jin Wikyung was alive or dead.

What if he died because we were a minute—or even a second—too late?

*If that happens…*

Crack.

I tightened my grip on the spear without realizing it. I drew internal energy up from my dantian and sent it flowing through both legs.

“S-Squad Leader!”

I kept running, leaving the reconnaissance squad’s voices fading behind me. The countless tracks the main force had left, and the growing noise of the battlefield, were my landmarks.

*Stay alive. Stay alive. Please, stay—*

Ah. I could see it at last.

Below a low hill, not even two hundred meters away, countless martial artists were locked in a bloodbath, killing and being killed.

“Die!”

“Gaaah!”

Corpses and blood—and more corpses, more blood!

The sight in front of me was so brutal I was momentarily speechless.

If I hadn’t built up a tolerance from my life as a Hunter, I probably wouldn’t have been able to pull myself out of the shock for a long time.

*Jin Wikyung! Where is Jin Wikyung?*

But someone else caught my eye first.

White hair you could pick out at a glance even from far away.

*The Head Elder!*

He stood in front of someone, sword in hand.

Hidden behind the Head Elder’s back, the kneeling man was hard to see, but he was huge, and he had a sword in his hand.

*A big guy with a sword?*

Only one person came to mind.

Jin Wikyung. If I wanted to save him, I had to move now.

*Open Inventory.*

The Inventory I used in Murim was packed with all kinds of things.

This spear was one of them. Its shaft was wood, its head steel.

*Equip Weapon.*

I took the spear and stepped back a few paces.

Two hundred meters. Impossibly far. Even more so if I was trying to hit someone with a thrown spear.

But I had to do it.

*It’s not like I can’t.*

Strength, Stamina, Agility.

I pushed the stats I’d built up going back and forth between Murim and reality as far as they would go.

With internal energy in my arm, I could send the spear farther and harder.

“Hup.”

I held my breath and stepped in. The first step was slow. The last was heavy. I whipped my arm, and the spear shot from my fingertips.

Fwoooosh!

The throw was faster and more accurate than I’d expected. It looked like it would punch straight through the Head Elder’s back.

But then…

Shhk.

*What the hell was that?*

A flash of blue light, and the spear split in two. From the spearhead at the very top all the way to the end, a clean cut.

For a moment I couldn’t tell whether I’d thrown a spear or a birthday cake.

“Who the hell are you?”

The old man had quite a set of lungs.

“It’s me, you son of a bitch!”

It was probably a curse the Head Elder had never heard in his life.

On top of that, he and I were members of the same family in Murim. If you went by the genealogy, the generation gap between us was about an archaeopteryx and a chick.

That alone was plenty of reason to be stunned. But I still had one finishing blow left.

“The Head Elder is—!”

My voice, loaded with internal energy, thundered across the battlefield. Even I was surprised by how loud it was. I could only imagine what it sounded like to everyone else.

I stared at his frozen, cold face in the distance and shouted with everything I had.

“A traitor!”

* * *

Jin Wikyung heard the voice right after bringing down all three Peak masters of the Mount Heng Sword Sect.

No—not only him. Everyone on the battlefield heard that shout.

“Who the hell are you?”

“It’s me, you son of a bitch!”

Cursing?

That was common enough on a battlefield. But if the target of the abuse was the Head Elder, and the young man who had appeared out of nowhere to dump a double helping of it was Jin Taekyung, then it was a completely different matter.

“Isn’t that… isn’t that the Third Young Master?”

“What? That’s Jin Taekyung? But why?”

“What’s going on?”

Jin Wikyung was thinking the same thing.

*What in the world is happening?*

His youngest brother, who was supposed to be in the rear, had appeared on the battlefield. That alone was shocking enough, and on top of it he had hurled language unfit to repeat at one of the family’s elders.

Wipeng, standing beside him, muttered,

“He’s completely lost it.”

Jin Wikyung was just about to nod without realizing it when—

“The Head Elder is—!”

An even bigger bomb dropped.

“A traitor!”

The battlefield sank into an icy silence. Even the occasional clash of weapons cut off cold.

Everyone stared blankly at Jin Taekyung.

*What kind of bullshit is this?*

*Betrayal? The Head Elder?*

*Is he drunk? The Third Young Master’s old habits must be coming back.*

Needless to say, the martial artists of the Jin Family of Taiyuan thought so. The martial artists of the Mount Heng Sword Sect were much the same.

Even the senior members who had recently begun to look favorably on Jin Taekyung stood there with their mouths hanging open.

“What a madman.”

“Does he even know who the old master is?”

If they had to name the person who had contributed most to this war, it was, without question, the Head Elder.

He had helped Jin Wikyung gather the family’s strength, and in today’s battle he had defeated Lee Cheonbaek.

Even setting aside his merits in this war, Jin Taekyung’s words could only sound like nonsense.

Who was the Head Elder?

He was a master of the previous generation, famous even in the Central Plains as the Blade of Flowers, a symbol of righteousness who had struck down countless demonic masters during the Great Faction War.

Every martial artist in Shanxi held him in some degree of respect.

“That man? A son of a bitch? A traitor?”

“Good heavens. That boy is smearing shit on three hundred years of the Jin Family of Taiyuan’s history.”

The Jin Family of Taiyuan, the Mount Heng Sword Sect—everyone here seemed to share the same thought. But there was at least one exception.

*The Head Elder. Betrayal.*

The instant he heard his youngest brother’s words, Jin Wikyung felt the blood in his entire body run cold. It was a sense of wrongness, finally showing its true shape.

*Lee Seogeun’s death was where it began.*

He had died poisoned by a lethal toxin. The Mount Heng Sword Sect had named the Jin Family of Taiyuan as the culprit, and that had been the spark that started the war.

But the most important question had been left unanswered.

*Who was the murderer?*

Even now, with the war nearing its end, the killer hiding behind it all had never been identified. No—because the war was nearing its end, no one cared about the murderer’s identity anymore.

Survival of the fittest. The strong would live and take everything.

*This war… was wrong from the very beginning.*

Lee Seogeun’s death.

The unnaturally rapid spread of the rumors.

The Mount Heng Sword Sect had declared war, and the Jin Family of Taiyuan had answered. That was how the real fighting had begun.

*And the Head Elder had been there.*

The Head Elder, who had never left seclusion, had appeared immediately after news of Lee Seogeun’s poisoning reached the family. His role within the family had been enormous.

A respected martial artist. One of the family’s senior elders.

If the Head Elder had not cooperated so actively, the Jin Family of Taiyuan might have split in two.

*We were able to come this far because of his help.*

Jin Wikyung thought the opposite.

*We were able to come this far because this was what the Head Elder wanted.*

A span too short even to call an instant. When Jin Wikyung finished the thought, he opened his mouth.

“Wipeng.”

“Your orders.”

“Cut down the First Elder.”

“What?”

The stooped, emaciated old man—the First Elder—opened his eyes wide.

The senior members standing nearby were just as shocked.

“L-Lesser Family Head!”

“What in the world…!”

But Wipeng did not hesitate. Before anyone knew it, his sword was flying toward the First Elder’s chest.

Clang-clang-clang!

Two swords cut in out of nowhere and knocked Wipeng’s blade aside.

Two fat, exceptionally tall old men.

They were the Second and Third Elders, who, together with the First Elder, styled themselves the Head Elder’s hands and feet.

Wipeng’s brow twitched when he saw the faint Sword Energy gathered on their blades.

“You’ve been hiding your martial arts.”

The First Elder answered with a single punch.

Boom!

With internal energy as deep as the years he had lived, he sent Wipeng flying, then straightened his back.

The field froze at the appearance of yet another Peak master who had spent his entire life hidden in the Head Elder’s shadow.

“First Elder, what… what is this?”

“Then could it be…!”

*Betrayal.* The word stamped itself clearly into everyone’s minds.

“That’s impossible!”

The one who shouted was the White Tiger Hall Leader. If the Elders were the Head Elder’s hands and feet, he had thoroughly served as the First Elder’s.

“Elder, Lesser Family Head. It seems there has been some misunderstanding…”

But he could not finish. At a jerk of the First Elder’s chin, the Second Elder moved with blinding speed and cut the White Tiger Hall Leader’s throat.

Shhk. Thud.

Jin Wikyung’s gaze met the First Elder’s in the air between them.

“You recruited the White Tiger Hall Leader too?”

“He was a noisy man. That was all. The others were the same.”

Jin Wikyung’s guess had been half right and half wrong.

The Elders had betrayed them, but the senior members who belonged to the Elders’ faction had not.

“Then why… Ah!”

“Sharp. I’ll give you that.”

The First Elder pulled a dark, grimy bamboo tube from inside his robes. Only a little of the fuse was left, and it was already burning down.

“Could we tell important secrets to men like that? Even just throwing the inside into chaos had already served its purpose. Things were easier if they didn’t know what was happening outside.”

Jin Wikyung shouted like a scream.

“Stop him!”

“You’re too late.”

The First Elder was right. The instant the fuse burned to its end, something burst, and a red flame shot high into the sky.

Fwish—boom!

It was a signal.

The martial artists of the small and mid-sized sects known as the Five Gates of Shanxi—the Three Paths Sect, a union of three sects; the Tao-centered Byeokdo Sect; and Gunggwimun, which had been pouring arrows from the cliffs without pause—turned in an instant.

“Kill everyone in your path!”

“No exceptions! Sweep them all away!”

They were no longer the clumsy third-rate martial artists they had seemed to be. Killing intent flowed from their eyes, and their sword paths were sharp.

*This wasn’t something they prepared overnight.*

Jin Wikyung’s face hardened.

* * *

Boom!

The Head Elder looked up at the sky. Before the red flame had even faded, a massive roar erupted from every direction.

*Too fast. Far too fast.*

The signal was supposed to go up only after the Mount Heng Sword Sect had been annihilated. The Five Gates of Shanxi were a blade prepared over decades. It had to be swung once, and finish everything like a bolt of lightning.

*Everything has its flow.*

The plan, which had been running without a hitch, had begun to go off course. As the Head Elder smiled bitterly, a voice slipped into his ear.

“So… it was you.”

Lee Cheonbaek. His voice was faint, but his eyes burned more fiercely than ever.

“You still have the strength to talk?”

“I’ll tear you to pieces alive and kill you.”

But no sooner had he finished speaking than blood poured from his mouth. The Head Elder pressed one of his acupoints and murmured,

“That would be inconvenient just yet. You still have something to do.”

Lee Cheonbaek despaired.

They had taken heavy losses, but hundreds of Mount Heng Sword Sect martial artists still remained. At this point, with even the leadership annihilated, if their Sect Leader were taken prisoner…

*Kill me instead!*

The anguished cry never left his mouth. The Head Elder pressed the Mute Acupoint, taking his voice. Then his hand brushed the Paralysis Acupoint, and Lee Cheonbaek’s body went rigid.

He had become a living corpse with his eyes still open.

“You bastard! Get your hands off him!”

At the same time, the air split with a shriek.

Fwoooosh!

The Head Elder did not panic. He swept his sword up from below. Beyond the spear splitting in two along the Sword Energy, Jin Taekyung was charging at terrifying speed.

“Aaaaaah!”

“Squad Leader! Please slow down a little!”

Together with a dozen or so riffraff who had appeared from who knew where.

[^1]: Red Hare is the legendary warhorse of Lü Bu in *Romance of the Three Kingdoms*.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 57`.

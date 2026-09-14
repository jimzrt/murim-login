# Master Edit Task — Chapter 30

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
| 조필     | **Jopil**          |
| 태원진가   | **Jin Family of Taiyuan**        |
| 열화문    | **Fire Gate Clan**               |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 주화입마   | **qi deviation**                                 |                                                       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 태원     | **Taiyuan**            |
| 소천 | **Socheon** |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 25–29

## Plot

Gong Yacheong survives his fall and reunites with Socheon and Soyul. The **Survivors of the Sakju Branch** Quest completes, granting Taekyung EXP, Merit, Fame, and several level-ups before generating a Chain Quest. Gong identifies Jopil, One Question, One Kill, as the leader of the Sakju Branch massacre, and Socheon vows revenge. Taekyung promises to kill Jopil under the false name Hong Gil-dong, then tries to retreat after learning that Jopil is a Peak master. Hyuk Mujin exposes Taekyung’s identity to the survivors.

Jopil examines the massacre site, kills the Mount Heng overseers and guides, and deduces that an exceptionally skilled spearman killed Black Mountain Blade and the other pursuers. He tracks Taekyung’s group through the blizzard while Jin Wikyung sends Wipeng and more than twenty riders to find and protect Taekyung. The group struggles toward the main family as Gong’s poison worsens. Taekyung’s Main Quest still requires First Rate, Level 30, and Fame 500 for Logout; he has reached Level 24 with displayed progress of 24/30 and 250/500.

Gong asks Taekyung to return Socheon and Soyul alive, creating the no-reward **Gong Yacheong’s Last Request** Quest. Taekyung initially orders the squad to abandon Gong, but Han Yeop disobeys and carries him. Taekyung turns back after realizing that abandoning the seemingly fictional survivors is emotionally impossible. A secret Sound Transmission reveals that the Head Elder sent Jopil, expects Taekyung’s death to change Jin Wikyung’s mind, and intends to drive out the Lower District Sect afterward; the accomplice remains unidentified.

The System forces Taekyung to confront Jopil. Jopil admits he is employed for a mission, recognizes Taekyung as the Jin Family’s third Young Master and the Sleeping Dragon, and offers to release only Taekyung. Taekyung refuses to abandon Gong, Socheon, Soyul, or the reconnaissance squad. Jopil attacks, killing one unnamed squad member with a throwing knife and overwhelming Taekyung with Peak-level speed and strength. His Berserk effect magnifies his Strength and Agility but makes his attacks broad and imprecise. Taekyung’s cut triggers the effect, and he orders the squad to stay back to preserve his Gambler Title’s one-on-one bonus. Hyuk and Han Yeop ignore him and attack; Jopil shatters Hyuk’s sword, cuts the head from Han’s spear, and throws both into trees. Taekyung’s Sky-Piercing Strike fails, and Jopil repeatedly wounds him before preparing another killing blow.

## Continuity

- Gong Yacheong, Socheon, and Soyul are the three recognized survivors of the Sakju Branch massacre. Gong is poisoned by the pursuers’ weapon coating; fasting pills restore stamina but do not detoxify him.
- Taekyung accepted **Gong Yacheong’s Last Request**, promising to return Socheon and Soyul alive. The Quest has no reward.
- Taekyung used the alias Hong Gil-dong until Hyuk Mujin revealed that he is Jin Taekyung.
- Jopil, One Question, One Kill, is a Peak master employed to complete an unspecified mission. He leads roughly fifty wandering martial artists and tracks the group through the blizzard with the help of a subordinate who is Third Rate in martial arts but Peak-level in tracking.
- Jopil killed Black Mountain Blade, the other pursuers, and the Mount Heng overseers and guides. The identity of the highly skilled spearman Jopil inferred from the corpses remains unknown.
- Jin Wikyung sent Wipeng and more than twenty riders to locate and protect Taekyung.
- The reconnaissance squad is traveling toward the main family. One unnamed member is dead. Hyuk Mujin remains Taekyung’s injured deputy; Han Yeop remains the Level 13 spear user, though Jopil destroyed his spearhead.
- The Head Elder secretly sent Jopil and plans to exploit Taekyung’s death against Jin Wikyung before driving out the Lower District Sect. His Sound Transmission accomplice and their full plan remain unresolved.
- Taekyung’s forced System Quest against Jopil is limited to Taekyung, requires survival, and fails on death. Jopil’s Berserk effect has worn off by the end of the fight.
- Taekyung’s Gambler Title grants a 10% combat-stat increase only in a one-on-one fight. His Sky-Piercing Strike failed against Jopil’s defense.
- Taekyung, Hyuk Mujin, and Han Yeop are in immediate danger after Jopil’s final attack begins. The outcome remains unresolved.
- Logout still requires First Rate, Level 30, and Fame 500. Taekyung has not advanced to First Rate and still cannot move the unidentified energy in his dantian.
- Taekyung’s growing inability to abandon the survivors intensifies the unresolved conflict between his belief that NPCs are unreal and his experience that they feel real. The capsule’s purpose, route home, and Murim’s death and resurrection rules remain unresolved.

## Translation Decisions

- Preserve **Survivors of the Sakju Branch**, **Gong Yacheong’s Last Request**, and the forced Quest against Jopil as distinct System events.
- Keep Jopil’s epithet as **One Question, One Kill**, his Peak rank, and his recognition of Taekyung as the **Sleeping Dragon**.
- Preserve the Hong Gil-dong alias and briefly footnote the folk-hero and “Father”/“Brother” wordplay where needed.
- Retain **Sound Transmission**, **Gambler**, **Berserk**, **Sky-Piercing Strike**, **First Rate**, **Peak**, **Merit**, **Fame**, and **Logout** as established System or martial terminology.
- Preserve the contrast between wandering martial artists’ experience and ordinary martial artists, and keep Jopil’s tracking subordinate as Third Rate in martial arts but Peak-level in tracking.
- Keep the distinction between fasting pills that restore stamina and treatment that detoxifies poison.
- Preserve the dark action-comedy tone, including Taekyung’s Hong Gil-dong lie, his attempted retreat, the unnamed squad member’s death, and his conflicted attachment to NPCs.
- Footnote **Mount Beimang** as a burial mountain whose “hiking” idiom means dying, **goshiwon** as tiny inexpensive room-for-rent housing, and **junichi** as a fish-quality image if those references recur.

### Prior accepted reading-copy tails

#### Chapter 28 tail (verified mastered)

…
happen. Those bastards are painfully slow. It’ll take them half a shichen to catch up.[^2] By then, everything will be over.” One thing was certain. In the ending Jopil envisioned, his own death had no place. “Well?” “And if I refuse?” Jopil smiled softly. “I’ll be disappointed in you. Very disappointed.” I could more or less picture what would happen if he became disappointed. “Young friend, I have no grudge against you. No—if anything, I’m rather fond of you. Answer a few things truthfully, and I might even let you go.” “Wait. Let me go?” “Yes. I won’t harm you in any way. I’ll send you back in one piece.” “…Really?” “I’ll stake my neck on it. Is that enough?” The sincerity showed on Jopil’s face. Unpredictable psychopath or not, maybe everyone could walk out of this alive. “All right.” Even if the worst happened, what else could I do but fight? For now, I planned to buy some time and search for a weakness. “Good. A friend who listens to reason, haha.” Jopil clapped and laughed. The scabbard at his left hip swayed. *Right-handed. Swordsman.* I kept inputting the data in my head. “First, I’d like to ask your age.” “Twenty.” Jopil’s eyes went round. “My. To have reached that realm at twenty. Impressive.” I’d spent seven years as a Hunter without ever escaping F-rank, yet in this game, people treated me like a martial arts genius. It was a strange feeling. “Judging by your clothes, you seem to be from the Jin Family of Taiyuan.” I nodded readily. “Super First Rate at twenty. You wouldn’t be that famous Heaven Shaking Sword, so… your name?” “Jin Taekyung.” “Jin Taekyung. Jin Taekyung. I’ve heard that name somewhere. Ah!” Jopil had been turning it over. Then he exclaimed. “The wastrel Third Young Master! That’s you?” “I’m not a wastrel. These days, they call me the Sleeping Dragon.” “Puhahaha! I knew it. The Jin Family of Taiyuan, those rigid fools, poisoning someone? Please. I don’t know who set this board, but things are getting interesting.” Jopil looked at me, satisfied. “I’ve heard plenty of rumors about you. Was all of that a disguise?” “…Something like that.” “Good. A hidden blade, then. I like it. When did you start learning martial arts?” “Seven years.” Not entirely a lie. By Murim standards, Hunter combat methods were a kind of martial art too. “Seven years. And your master?” “Don’t have one.” “No master?” He studied me for a while, then said, “Doesn’t seem like a lie.” “You promised to spare me if I answered honestly. That was your promise, wasn’t it?” “Yes, it was. What an absurd yet entertaining story. A direct descendant of the Jin Family of Taiyuan, without a master, reaching that realm at twenty… My, my.” My mouth was bone-dry. I gripped the spear and scanned Jopil’s body. He was unbelievably riddled with openings. But was what I was seeing really all there was? *He could be baiting me into attacking first.* The thought went no further. Jopil suddenly burst out laughing. “Hahaha! Good. I like it. I’ll keep my promise.” He’d keep his promise? The thing I’d thought impossible was actually happening. I stared at Jopil in a daze. “No need to look at me like that. Truth is, at first I really wanted to kill you… But now that we’ve met, I find I want to watch you a little longer.” Jopil continued, his voice brimming with goodwill. “It’d be a waste to kill outstanding talent like this. Especially in a situation like this.” “A situation like this?” “Ah. You might not know. You’ll find out when you return. Go on, then. I hope you’ll have grown a little more by the next time we meet.” I could leave? He meant it? I backed away without dropping my guard. Jopil merely watched me with a smile. He looked like a fisherman letting a minnow go. *They say even if you walk into a tiger’s den, you live if you keep your head.* Who’d have thought Jopil’s wild-card personality would turn into an exit. Once I had a safe distance, the breath I’d been holding burst out. But there was no time to catch it. I had to leave this place a second sooner, if I could. “We’re moving. Hurry!” Then— “Hold on, young friend.” Jopil looked at me, puzzled. “What are you doing?” “What do you mean? Going back, like you promised…” “I only gave permission for you to leave. Alone.” “…What?” “I may not look it, but I’m in someone’s employ. I have to finish the mission I took on.” The mission. Don’t tell me. “The three survivors of the Sakju Branch. And those pieces of trash you call your subordinates. Leave them behind. I ought to be paid for two days’ work, don’t you think?” Eyes that had been clear as a child’s flashed. The next instant, they were a predator’s. “I’ll say this now. If you refuse, I’ll be very disappointed.” I stared blankly at Jopil, the reconnaissance squad, the young siblings, and the dying Gong Yacheong. Time was short, but after dozens of rounds of doubt and conflict, one line burst out. “Then be disappointed, you fucking bastard.” Jopil laughed savagely. [^1]: A zhang is a traditional Chinese unit of distance, roughly 3.3 meters. [^2]: A shichen is a traditional time period of roughly two hours.

#### Chapter 29 tail (verified mastered)

…
lasted this long. *Boom!* That wasn’t martial arts. It was a bombardment. But there was no precision in Jopil now. His movements were compact and fast, but the extra strength from **Berserk** had made them big and left him full of openings. *I just need him to show me one opening…* The problem was, I couldn’t see one. He had completely lost it and was turning the area around us into a wasteland. All I could do was dodge. I didn’t even dare to block. Step into range and I would be shredded. That much was obvious. “Squad Leader!” “We’re coming!” I hurriedly waved off the reconnaissance squad members running toward me. “Hey, don’t come! Don’t come! Fall back!” Had they lost their minds? Coming *here*? We had already lost one man for nothing. I didn’t want the entire reconnaissance squad wiped out. And besides— *If those guys come over here, the Gambler Title’s effect disappears!* **Gambler** only applied in a one-on-one. I was barely hanging on as it was. If the Title’s effect vanished too, I had no idea how much longer I could last. “Get back, you bastards!” I shouted and flung myself sideways. Sure enough, Jopil’s sword smashed the ground to pieces. *Crack!* “Squad Leader!” Hyuk Mujin’s shout came a beat late. For all I had tried to stop him, he was already charging. Behind him, I saw Han Yeop with a set, determined face. “Hey, don’t—” “Jopil, you vile bastard!” “Get away from the Squad Leader!” But it was a step too late. Hyuk Mujin and Han Yeop, who had come running with everything they had, thrust their weapons at Jopil, who was preoccupied with me. “Die!” Sword and spear. Spear and sword. Good timing, good attacks, like they had practiced it beforehand. There was just one problem. They had the wrong opponent. “How dare you, you rats!” Jopil’s response was instant. He drove his sword into the ground where he stood, spun around, and smashed both weapons with his bare hands. Facing a sword and spear empty-handed was suicide. But in Murim, things were different. More precisely, Jopil was different. He was a Peak master. *Crack—Crunch!* His palm had only brushed the side of the blade, and Hyuk Mujin’s sword still shattered into pieces before it reached him. Han Yeop stared in horror at his spear, the head sliced clean off. That was the result of Jopil’s straightened knife-hand. “What the…” “That’s impossi—” Before they could finish, Jopil slammed both hands into their chests. They smashed into trees, spraying fountains of blood. “I’ll kill you.” On his chillingly smiling face, the whites of his eyes were gone. **Berserk** had worn off. He was back in his right mind. “Fuck…” From bad to worse. Trouble on top of trouble. Surrounded on all sides. Jopil, you son of a bitch. The situation was hurtling toward the worst possible outcome. If anyone was going to stop him, it had to be me. “Jopil—!” The internal energy I had pulled up at full strength raced through my whole body. I kicked off the ground and shot toward him. Jopil grinned wide. “Right. I’ll kill you first.” But I had something to count on. *He’s empty-handed right now.* *It was a blunder he’d made while Berserk. And I was sure I could finish everything before he yanked the sword out of the ground behind him and swung it.* The next instant, I hauled up every bit of internal energy in my dantian. I focused all of it on a single point—the spear tip—and thrust. “Die!” The final form of the Jin Family’s Spear Technique, Sky-Piercing Strike. If it could pierce the heavens, why couldn’t it pierce Jopil’s heart? I was sure of it. *This is it… the end.* The world slowed, and I saw Jopil’s face. He was smiling. The moment I saw that smile, I knew. Something was wrong. *Skrrrng.* Jopil’s sword was faster than my spear. The blood-wet crimson blade shoved my spear shaft aside and drove inward. The instant my spearhead, laden with internal energy, stabbed into empty air— *Slash.* A chilling sound, and my chest felt cool. Then came the searing pain, and the blood bursting out. Fortunately, I had jerked back at the last moment and avoided a fatal wound. *Damn it.* What the hell had just happened? As I staggered back, Jopil charged. *Whoosh-whoosh-whoosh!* Crimson sword-light poured down. Every flash was so fast and powerful I could barely see it. I gritted my teeth and swung my spear, but Jopil had the edge in both momentum and martial arts. *Slash. Thunk. Splurt.* Lightning cut across my whole body. The blade stabbed my shoulder, slashed my knee, and punched through my side before coming back out with a spray of blood. “Guh.” “You didn’t drop your weapon. I’ll give you that.” Jopil added, “If you can take this, too.” The next instant, his hand slammed into my chest. [^1]: A zhang is a traditional Chinese unit of distance, roughly 3.3 meters. [^2]: Mount Beimang is a burial mountain; hiking it means being dead. [^3]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement. [^4]: Junchi is a fish traditionally prized in Korea; the saying means that something of quality retains its worth even in decline. [^5]: Silk-reeling force is a method of twisting the entire body in a continuous, coiling motion to release power.

## Korean source

```text
＃30화



화아악.

조필의 붉게 달아오른 손바닥이 내 가슴을 때린 순간, 용암처럼 뜨거운 기운이 내부를 휩쓸었다. 숨이 막히고 공력이 역류했다.

‘이건 뭐지?’

의문과 함께 나는 튕겨져 나갔다. 십여 장을 부딪치고 구른 후에야 멈출 수 있었다.

“쿨럭.”

턱을 타고 핏물이 주르륵 흘렀다. 간혹 섞여 나오는 정체불명의 덩어리는…… 시발. 내장 조각이다.

‘제대로 당했군.’

흐릿한 시야 너머로 걸어오는 조필이 보였다. 느긋한 걸음걸이에서 승자의 여유가 느껴졌다.

‘일어나야 해.’

손으로 옆을 더듬자 서늘한 창대가 잡혔다. 창을 지팡이 삼아 간신히 일어났을 때 조필의 찡그린 눈매가 보였다.

“칠 성의 화염신장(火焰神掌)을 맞고도 일어선단 말이지…… 손이 많이 가는 후배구먼.”

퍼벅!

또다시 그의 일장(一掌)이 작렬했다. 화염신장이라는 이름만큼이나 위력도 대단했다. 상의가 타들어 가고 살갗이 녹아 문드러졌다. 내부로 침투한 열기는 혈맥을 가닥가닥 끊었다.

“크헉.”

끔찍한 고통이 엄습한다. 그러나 고통에 몸부림치는 대신 조필의 급소를 향해 창을 찔러 넣었다.

턱.

“투견 같은 놈이군.”

창대를 잡아챈 조필이 혀를 찼다.

“자네 정도로는 날 어쩌지 못해.”

“좆…… 까!”

다음 순간, 나는 붙잡힌 창을 놓고 놈의 품속으로 뛰어들었다. 마지막 기회다. 모든 공력을 일점에 집중. 놈의 급소를 가격한다면 전세를 뒤집을 수 있다.

하지만…….

“헉.”

결과는 처참했다.

내상을 고려하지 않고 무리하게 공력을 끌어 올린 탓이다. 나는 그대로 쓰러져 번개에 맞은 것처럼 부들부들 떨었다.

입가에서 침이 줄줄 흐르는 것이 느껴졌다.

“푸핫. 푸하하! 이런 멍청한 놈을 봤나!”

조필이 광소를 터트리며 창날을 부러트렸다.

“자, 이제 어쩌지? 응? 태원진가의 막내 도련님?”

이제는 무기도 없다. 절망으로 눈앞이 캄캄해진다.

‘이렇게 죽는 건가?’

지난 7년간 지금만큼 죽음을 가깝게 느낀 적이 없었다. 천 번도 넘게 싸우고 살아남았던 내가. 고작 여기서 죽는다고?

이렇게 허무하게?

‘안 돼. 이렇게 죽을 수는…….’

손을 뻗었지만 거기까지였다.



- 조장!



노이즈 낀 외침을 마지막으로 모든 빛이 꺼졌다.



* * *



다시 눈을 떴을 때는 천국도, 지옥도 아니었다. 나는 땀에 흠뻑 젖은 상태로 헐떡이고 있었다. 온몸이 물먹은 솜처럼 무겁다.

‘꿈? 아니면 주마등?’

뭐든 간에 한 가지는 확실했다. 지금 이 상황이 과거, 그것도 7년 전의 기억이라는 사실이다. 낯익은 훈련 교관의 얼굴이 그 증거다.

“너, 너 이거…….”

교관은 말을 잇지 못했다. 그의 시선 끝에는 훈련용으로 제작된 강철 인형이 있었다. 몬스터의 형상을 본 따 제작된 그것은 이제 고철에 가까웠다. 온통 구부러지고 갈라진 고철.

“방금 그거 스킬이냐?”

과거의 내가 기진맥진한 목소리로 대답했다.

“있는 힘껏 찌르기요.”

“있는 힘껏 찌르기?”

“예. 그냥 있는 힘껏 찌르는 건데요.”

“어떻게 쓸 수 있는지는 잘 모르겠는데, 그냥 각성한 후부터는 자연스럽게 쓰게 됐고?”

“어, 네. 맞아요.”

“그게 스킬이야, 인마.”

황당한 표정의 교관이 손에 쥔 서류철로 시선을 돌렸다.

“진태경. 스무 살. 경기도 고양시 살고, F급 각성자. 이거 너 맞아?”

“네. 그런데요. 제 힘껏, 아니 스킬이요. 좋은 거 맞죠?”

“좋냐고?”

교관이 헛웃음을 지었다.

“훈련소에서만 15년짼데 이런 건 처음 본다. 이 정도면 최소 D급은 돼야 나올 만한 파괴력이니까.”

“시바, 이럴 줄 알았어. 저기 교관님. 저 퇴소할게요.”

“뭐?”

“그냥 심사 다시 보려고요. 솔직히 저 정도면 E급은 받아야 하잖아요.”

“아니, 그쪽에선 잘 판단한 것 같은데.”

“네?”

“스킬이 굉장한 건 맞아. F급에서 절대 나올 수 없는 수준이지. 그런데…….”

교관은 뒤통수를 긁적였다.

“너, 이거 못 쓴다.”

“왜, 왜요?”

“몸이 못 따라가. F급 수준의 마나와 신체 능력이 감당할 수 있는 스킬이 아냐. 네가 스킬 한 번 쓰고 퍼지는 이유도 거기 있지.”

“전 멀쩡한데요?”

“그래?”

고개를 끄덕이기도 전에 교관이 번개처럼 손을 뻗어 가슴을 툭 쳤다. 말 그대로 툭. 하지만 모든 힘을 소진한 나는 벌렁 자빠졌다.

온몸이 욱신거리는 통에 손 하나 까딱하기도 힘들다.

“이미 한계 이상의 힘을 내고 있어. 나중에 가면 단순히 쑤시는 정도로는 안 끝날 거다.”

“……다른 방법은요?”

“탄탄한 기본기와 훌륭한 테크닉. 그리고 너만의 전투 감각. 오래 살고 싶으면 스킬은 쓰지 마라. 아. 특별한 상황은 제외.”

“특별한 상황이요?”

교관이 씩 웃으며 덧붙였다.

“목숨이 위험한 상황. 그 스킬이 한 번쯤은 네 목숨을 살려 줄지도 모르지.”

다음 순간, 나는 차가운 눈밭 위에서 눈을 떴다.



* * *



“조장!”

마지막에 들었던 그 외침이 선명하게 들렸다. 엉망진창으로 망가진 몸 상태와 날카로운 고통도 느껴졌다.

‘아직 살아 있어.’

주마등은 아주 찰나의 순간에 불과했다. 조필은 손만 뻗으면 닿을 거리에서 뒤를 돌아보고 있었다.

“충성심이 제법이군. 실력은 형편없지만 말이야.”

놈의 시선 끝에는 한 무더기가 되어 달려오는 정찰조원들이 있었다.

“저놈들을 찢어 죽일까 하는데, 자네 생각은 어때?”

“……하게 싸웠어.”

“뭐?”

“멍청…… 싸웠어.”

나는 다시 한번 웅얼거렸다. 조필이 짜증난 얼굴로 허리를 숙였다.

“말도 똑바로 못하나?”

“그동안 멍청하게 싸웠다고.”

푸우웃!

기다리던 순간. 나는 놈의 얼굴을 향해 모아 둔 핏물을 뿜어냈다. 반 박자 빠르게 움직인 손은 놈의 발을 향해 내려 찍히고 있었다.

‘인벤토리 오픈.’

조필은 모르고 있다. 나는 헌터고 무림인이며, 시스템을 활용할 수 있는 유저라는 사실을!

‘비수 장착.’

텅 비었던 손아귀에 단단한 감촉이 느껴진다. 안면에 핏물을 뒤집어쓴 조필이 황급히 물러나려 했지만 이미 비수의 끝이 발등을 파고든 후였다.

푸푹!

“큭.”

절정 고수도 사람이다.

갑작스러운 고통에 놈의 몸이 덜컥 멈췄을 때 나는 비수를 놓고 발목을 향해 손을 뻗었다.

‘비수 장착.’

인벤토리에는 튜토리얼 때부터 해치운 적들의 무기가 쌓여 있다. 검, 창, 도끼, 비수…… 스무 자루가 넘는다.

조필의 부하들은 걸어 다니는 무기 창고였다.

서걱.

“크악!”

아킬레스건. 발목 힘줄을 끊자 비명이 터진다. 자세가 무너진 틈을 타 옆으로 구르며 비수를 휘두르고 쑤셨다. 남은 왼쪽 다리마저 피범벅이 되었다.

서걱. 푹. 푹. 푸푸푹!

분노와 고통으로 놈의 입이 쩍 벌어졌다.

“크아아악. 이 개새끼!”

두 다리를 못 쓰게 됐지만 조필은 절정 고수였다. 번개처럼 돌아서며 비수를 피한 그가 내 손목을 잡고 비틀었다.

우두둑.

“크악!”

공격은 거기서 끝나지 않았다. 붉게 달아오른 손바닥. 화염신장이다.

펑.

가슴이 움푹 꺼졌다. 눈앞이 새하얗게 물든다. 강력한 화기(火氣)가 몸속을 헤집었다.

펑.

몸에서 힘이 빠져나간다.

조필의 손아귀에 잡힌 목에서 뼈가 어긋나는 소리가 들렸다. 귓가로 스산한 목소리가 파고들었다.

“이제 깨달았겠지. 네가 누굴 건드렸는지.”

“……쿨럭.”

“염왕이 묻거든 내가 보냈다고 해라.”

말없이 시체처럼 축 늘어져 있는 내게, 조필이 환희에 찬 얼굴로 선언했다.

“죽어.”

그렇게 최후의 화염신장이 가슴을 향해 쏘아졌다. 붉게 타오르는 손바닥에는 내 생명을 송두리째 집어삼킬 용암이 깃들어 있었다.

그리고 마침내…….

턱.

세상이 정지했다. 용암도, 그 어떤 뜨거움도 없었다. 상처투성이에 못이 박힌 손바닥이 내 가슴을 짚었을 뿐이었다.

조필의 눈동자에 파문이 일었다.

“너…….”

목을 움켜쥔 손아귀에서 스르륵 힘이 빠진다. 주춤주춤 뒷걸음질 치는 조필의 배꼽 아래, 단전을 파고든 비수가 보였다.

“이게, 이게 도대체.”

다음 순간 조필의 턱을 타고 피가 흘렀다. 그건 시작에 불과했다. 두 눈, 코와 귀에서도 피가 흐르기 시작한 것이다. 칠공(七空)을 타고 흐르는 피의 폭포.

그 끔찍한 모습에 정찰조원들도 걸음을 멈췄다. 누군가 신음처럼 중얼거렸다.

“주화입마…….”

공력은 양날의 검이다. 나는 조필이 공력을 최고조로 끌어 올리는 순간을 기다렸고, 인벤토리에서 소환한 비수를 단전에 박아 넣었다.

그 결과는 공력의 역류. 주화입마다.

“분명히 넌 빈손이었는데.”

나는 피곤한 목소리로 대꾸했다.

“살다 보면 별일이 다 일어나는 법이지.”

“이렇게 죽을 수는 없어. 이건 말도 안 돼.”

조필은 넋 나간 사람처럼 중얼거리며 한 걸음씩 내디뎠다.

놈이 지나간 자리마다 피 웅덩이가 고였다.

“나는 조필이다. 일문일살 조필. 열화문의 십구 대 계승자. 너 같은 놈에게 죽어선 안 되는 몸이란 말이다!”

피를 뒤집어쓴 채 절규하는 조필의 모습에서 섬뜩한 귀기(鬼氣)가 느껴졌다. 결사의 각오로 뛰어왔던 정찰조원들도 두려움에 몸을 떨었다.

“그런데 왜, 네깟 놈에게 내가!”

그때. 꺼진 줄 알았던 불씨가 타올랐다.

변화는 조필의 몸에서 시작됐다. 흐르던 피가 멎고 전신의 핏줄이 푸르게 도드라진다. 그는 양발의 힘줄이 잘려 나간 고통도, 주화입마도 느끼지 못하는 사람 같았다.

내뱉는 숨에서 끔찍한 열기가 느껴졌다.

‘이게 뭐지?’

말 그대로의 부활? 아니다. 이건 조필의 마지막 발악이다.

모두가 공포에 사로잡혀 비명을 질렀지만 내게는 똑똑히 보였다. 시시각각 하얗게 세는 머리카락, 쪼그라드는 피부.

지금 놈은…… 생명을 태우고 있다.

‘나만큼은 죽이고 가겠다는 거겠지.’

가장 소중한 걸 버리면서 얻은 힘. 그 힘이 오롯이 나를 향하고 있다. 나는 본능적으로 피할 수 없다는 것을 깨달았다.

‘할 수 있을까, 내가?’

떨어져 있는 창을 주워들었다. 튜토리얼 때부터 지금까지 썼던 [예리한 창]이다. 창날이 부러진 그것은 이제 뾰족한 철봉에 불과했다.

‘나도 곧 이 꼴이 나겠군.’

남은 방법은 하나뿐.

성공하더라도 생명은 장담하지 못한다. 하지만 고민할 여유 따위는 없었다.

“진태경!”

“그래. 끝내자.”

나와 조필. 조필과 나.

우리는 서로를 향해 쏘아졌다. 놈에게서 뿜어져 나오는 열기에 쌓인 눈이 녹아내리고 입술이 바짝 말랐다. 나는 길게 호흡했다.

스읍. 후우.

주위의 소음이 멀어진다. 내 심장 박동과 호흡 소리가 천둥처럼 들렸다. 쿵. 쿵쿵. 쿵쿵쿵.

최고조에 다다른 심장 박동. 기계처럼 맞아떨어지는 호흡.

나는 확신했다.

‘지금.’

동시에 단전의 공력을 깨웠다. 기혈이 꼬이고 망가진 내부에 유일하게 남아 있는 건 바위처럼 굳은 제삼의 공력뿐이다.

유일한 선택지이자 내 스킬(Skill)을 채워 줄 마지막 한 조각.

‘네 멋대로 날뛰어라.’

깨어난 공력이 폭주했다. 망가진 기혈을 비집고 온몸으로 뻗쳐 나갔다. 아득한 고통이 느껴진다.

그러나 이내 공력이 주는 새로운 힘으로 잊혔다.

‘가라!’

전신의 근육이 팽팽하게 조여든다. 종아리와 허벅지, 허리를 지나 내질러지는 팔을 따라 전신의 모든 힘과 공력이 솟구쳤다. 부러진 창끝에서 응축된 공기가 터져 나간다.

그에 맞춰 조필이 화염신장을 내뻗었다.

“죽어어엇!”

콰아아아.

바람과 함께 눈 더미가 솟구쳤다. 나풀나풀 가라앉는 눈 사이로 조필의 모습이 드러났다.

화염신장을 펼쳤던 오른팔부터 어깨, 옆구리까지. 상반신의 절반이 증발해 버린 모습이었다.

“이게 무슨, 무공……?”

나는 창을 떨어트리며 대답했다.

“힘껏 찌르기.”

다음 순간 하늘과 땅이 뒤집혔다.

흐릿해지는 시야 너머로 이미 숨이 끊긴 조필의 목이 하늘 높이 솟구쳤다. 제 키만 한 검을 든 소천이 소리 내어 울고 있었다.
```

## Current accepted English baseline

```markdown
# Chapter 30

*Whoosh.*

The instant Jopil’s red-hot palm struck my chest, energy as hot as lava swept through me. My breath caught, and my internal energy surged backward.

*What is this?*

The question came with me as I was sent flying. I slammed and rolled some ten zhang before I could stop.

“Cough.”

Blood trickled down my chin. The unidentified chunks mixed in with it now and then were… fuck. Pieces of organ.

*He got me good.*

Through my blurry vision, Jopil walked toward me. His unhurried stride had a victor’s ease.

*I have to get up.*

I groped beside me and found a cool spear shaft. Using the spear as a cane, I barely made it to my feet—and saw Jopil’s scowling eyes.

“You can still stand after taking a seventh-stage Flame Divine Palm… What a high-maintenance junior.”

*Wham!*

His palm detonated into me again.

The Flame Divine Palm was every bit as powerful as its name. My shirt burned away, and my flesh melted and sloughed off. The heat that sank inside me severed my blood channels strand by strand.

“Guh.”

Horrible pain crashed in. Instead of writhing in it, I drove the spear at Jopil’s vital point.

*Thunk.*

“You’re like a fighting dog.”

Jopil snatched the spear shaft and clicked his tongue.

“Someone at your level can’t do anything to me.”

“Go… fuck yourself!”

The next moment, I let go of the seized spear and threw myself into his chest.

Last chance. Focus every bit of internal energy on a single point. If I struck his vital point, I could turn the tide.

But…

“Gasp.”

The result was disastrous.

I had forced my internal energy up without accounting for my internal injuries. I collapsed on the spot and shook like I’d been struck by lightning.

I could feel drool running from the corner of my mouth.

“Pfft. Puhahaha! Have you ever seen such a stupid bastard!”

Jopil burst into mad laughter and snapped the spearhead.

“Well? What now? Huh? Youngest Young Master of the Jin Family of Taiyuan?”

I had no weapon left. Despair blacked out my vision.

*Am I going to die like this?*

In the last seven years, I had never felt death this close. Me—who had fought more than a thousand times and lived. Die here, of all places?

This pointlessly?

*No. I can’t die like this…*

I reached out, but that was as far as I got.

—Squad Leader!

A shout crackling with static was the last thing I heard before all the light went out.

* * *

When I opened my eyes again, it was neither heaven nor hell. I was drenched in sweat and panting. My whole body felt heavy, like waterlogged cotton.

*A dream? Or my life flashing before my eyes?*

Either way, one thing was certain. This was the past—a memory from seven years ago. The familiar face of the training instructor was proof enough.

“You—you, this…”

The instructor couldn’t finish. His eyes were on a steel dummy built for training. Modeled after a monster, it was little more than scrap metal now.

Bent and split scrap, head to toe.

“Was that a skill just now?”

My younger self answered in an exhausted voice.

“Thrust with All My Might.”

“Thrust with All My Might?”

“Yes. I just thrust as hard as I could.”

“You don’t really know how to use it, but after Awakening you just started using it naturally?”

“Uh, yes. That’s right.”

“That’s a skill, you idiot.”

Looking incredulous, the instructor turned to the file in his hand.

“Jin Taekyung. Twenty years old. Lives in Goyang, Gyeonggi Province. F-rank Awakened. Is this you?”

“Yes. So? My full-power thrust—no, my skill. It’s good, right?”

“You’re asking if it’s good?”

The instructor let out a hollow laugh.

“I’ve been at this training center for fifteen years, and I’ve never seen anything like this. Destructive power like that should be at least D-rank.”

“Fuck, I knew it. Uh, Instructor. I’m leaving.”

“What?”

“I’m going to get reevaluated. Honestly, with power like that, I should at least be E-rank.”

“No. They seem to have judged you correctly over there.”

“What?”

“The skill really is incredible. It’s a level that could never come out of an F-rank. But…”

The instructor scratched the back of his head.

“You can’t use it.”

“Why? Why not?”

“Your body can’t keep up. That skill is beyond what F-rank mana and physical ability can handle. That’s why you collapse after using it once.”

“But I’m fine.”

“Are you?”

Before I could even nod, the instructor’s hand shot out like lightning and tapped my chest.

Literally a tap. But I’d used up all my strength, so I flopped onto my back.

My whole body throbbed. I could barely twitch a finger.

“You’re already putting out more power than your limits can handle. Later on, it won’t end with a little soreness.”

“…Is there another way?”

“Solid fundamentals and excellent technique. And your own combat sense. If you want to live a long time, don’t use that skill. Ah. Except in special circumstances.”

“Special circumstances?”

The instructor grinned and added,

“When your life is in danger. That skill might save you once.”

The next moment, I opened my eyes on the cold snowfield.

* * *

“Squad Leader!”

The shout I’d heard at the end came through clearly. So did my wrecked body, and the sharp pain.

*I’m still alive.*

The flash of my life had lasted only an instant. Jopil was looking behind him, close enough to reach if I stretched out a hand.

“Not bad loyalty. Their skill’s pathetic, though.”

The reconnaissance squad was charging toward us in a cluster, right where he was looking.

“I’m thinking of tearing those guys apart and killing them. What do you say?”

“…dly. Fought.”

“What?”

“Stupid… fought.”

I mumbled it again. Jopil bent down, irritated.

“Can’t you even talk straight?”

“I said I’ve been fighting stupidly this whole time.”

*Ptoo!*

The moment I’d been waiting for.

I spat the blood I’d gathered at his face. Half a beat faster, my hand was already slamming down toward his foot.

*Inventory Open.*

Jopil didn’t know. I was a Hunter, a man of Murim, and a player who could use the System!

*Equip Dagger.*

A solid weight filled my empty grip. Jopil, his face covered in blood, tried to jerk back, but the dagger’s tip had already punched through the top of his foot.

*Shunk!*

“Guh.”

Even a Peak master was still human.

When his body jerked to a halt from the sudden pain, I dropped the dagger and reached for his ankle.

*Equip Dagger.*

My Inventory was piled with weapons from enemies I’d taken down since the Tutorial. Swords, spears, axes, daggers… more than twenty of them.

Jopil’s men had been a walking armory.

*Slice.*

“Gaaah!”

The Achilles tendon. The moment I cut the tendon at his ankle, a scream burst out of him. As his stance collapsed, I rolled aside, slashing and stabbing. His remaining left leg was soaked in blood too.

*Slice. Thrust. Thrust. Stab-stab-stab!*

Jopil’s mouth fell open with rage and pain.

“Gaaaaah! You son of a bitch!”

He couldn’t use either leg, but Jopil was a Peak master. He spun like lightning, slipped the dagger, caught my wrist, and twisted.

*Crack.*

“Gah!”

The attack didn’t end there.

A red-hot palm.

The Flame Divine Palm.

*Boom.*

My chest caved in. My vision went white. Powerful fire qi tore through my body.

*Boom.*

The strength drained out of me.

From the neck in Jopil’s grip came the sound of bone slipping out of place. A chilling voice slid into my ear.

“You understand now, don’t you. Who you picked a fight with.”

“…Cough.”

“If King Yama asks, tell him I sent you.”

To me, hanging limp as a corpse, Jopil declared it with a face full of rapture.

“Die.”

The final Flame Divine Palm shot toward my chest. Lava that would swallow my life whole was imbued in that blazing palm.

And at last…

*Tap.*

The world stopped.

No lava. No heat of any kind. Only a scarred, callused palm resting against my chest.

A ripple ran through Jopil’s eyes.

“You…”

The grip on my throat slipped away. As Jopil staggered backward, I saw the dagger driven in below his navel—buried in his dantian.

“This… what the hell is this?”

The next moment, blood ran down Jopil’s chin.

That was only the beginning.

Blood started pouring from his eyes, his nose, and his ears as well. A waterfall of blood streamed from his seven orifices.

The reconnaissance squad stopped in their tracks at the horrifying sight. Someone muttered, almost a groan.

“Qi deviation…”

Internal energy was a double-edged sword.

I had waited for the moment Jopil drew his internal energy to its peak, then driven a dagger summoned from my Inventory into his dantian.

The result was a reversal of internal energy. Qi deviation.

“You were definitely empty-handed.”

I answered in a tired voice.

“You live long enough, all sorts of things happen.”

“I can’t die like this. This makes no sense.”

Jopil muttered like a man whose soul had left him and took one step after another.

Wherever he passed, pools of blood collected.

“I am Jopil. Jopil, One Question, One Kill. The nineteenth-generation successor of the Fire Gate Clan. I’m not someone who should die at the hands of a nobody like you!”

A chilling, ghostly aura came off him as he screamed, covered in blood. Even the reconnaissance squad members who had charged in ready to die were shaking with fear.

“Then why? Why, at the likes of you, would I—!”

That was when the ember I’d thought extinguished burst into flame.

The change started in Jopil’s body. The flowing blood stopped, and the veins all over him stood out blue. He looked like a man who couldn’t feel the pain of both tendons being cut—or even the qi deviation.

A terrible heat poured from his breath.

*What is this?*

A literal resurrection?

No. This was Jopil’s last desperate struggle.

Everyone screamed, seized by terror, but I could see it clearly. His hair was turning white by the second. His skin was shriveling.

Right now, that man was…

*Burning his life.*

*He’ll kill me, at least, before he goes.*

Power gained by throwing away the most precious thing he had. Every bit of it was aimed at me. I knew on instinct that I couldn’t dodge.

*Can I do this? Me?*

I picked up the fallen spear.

The *Sharp Spear* I’d used from the Tutorial until now.

Its spearhead was broken. Nothing left but a pointed iron rod.

*I’ll end up looking like this soon enough.*

I had only one option left.

Even if I succeeded, I couldn’t guarantee I’d live. But there was no luxury of hesitation.

“Jin Taekyung!”

“Yeah. Let’s finish this.”

Me and Jopil.

Jopil and me.

We shot toward each other. The heat pouring off him melted the piled snow and dried my lips. I drew a long breath.

*Sss. Hoo.*

The noise around me receded. My heartbeat and breathing sounded like thunder.

*Thump. Thump-thump. Thump-thump-thump.*

My heartbeat hit its peak. My breathing locked in, precise as a machine.

I was certain.

*Now.*

At the same time, I woke the internal energy in my dantian. Inside me, where my qi and blood channels were twisted and wrecked, the only thing left was the third internal energy, hardened like rock.

My only option—and the last piece that would fill my Skill.

*Run wild as you please.*

The awakened energy went berserk. It forced its way through my ruined qi and blood channels and spread through my whole body. A dizzying pain hit me.

But it was soon forgotten in the new strength the energy gave me.

*Go!*

Every muscle in my body pulled taut. From my calves and thighs, through my waist and along my thrusting arm, every bit of strength and internal energy in me surged forward.

Condensed air burst from the broken spear tip.

Matching it, Jopil thrust out his Flame Divine Palm.

“Dieeeee!”

*Whoooosh.*

A mound of snow erupted with the wind. Through the flakes drifting gently back down, Jopil came into view.

From the right arm that had unleashed the Flame Divine Palm, through his shoulder and his side—half of his upper body had evaporated.

“What kind of martial art…?”

I dropped the spear and answered.

“Thrust with All My Might.”

The next moment, heaven and earth flipped.

Beyond my blurring vision, Jopil’s already lifeless head shot high into the sky.

Socheon was crying out loud, holding a sword as tall as he was.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 30`.

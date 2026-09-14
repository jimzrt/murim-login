# Master Edit Task — Chapter 31

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
| 무인     | **martial artist**                               | Default term                                          |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 마정석     | **Magic Gem**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 삭주 | **Sakju** | Jin Family branch location |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |

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

#### Chapter 29 tail (verified mastered)

…
lasted this long. *Boom!* That wasn’t martial arts. It was a bombardment. But there was no precision in Jopil now. His movements were compact and fast, but the extra strength from **Berserk** had made them big and left him full of openings. *I just need him to show me one opening…* The problem was, I couldn’t see one. He had completely lost it and was turning the area around us into a wasteland. All I could do was dodge. I didn’t even dare to block. Step into range and I would be shredded. That much was obvious. “Squad Leader!” “We’re coming!” I hurriedly waved off the reconnaissance squad members running toward me. “Hey, don’t come! Don’t come! Fall back!” Had they lost their minds? Coming *here*? We had already lost one man for nothing. I didn’t want the entire reconnaissance squad wiped out. And besides— *If those guys come over here, the Gambler Title’s effect disappears!* **Gambler** only applied in a one-on-one. I was barely hanging on as it was. If the Title’s effect vanished too, I had no idea how much longer I could last. “Get back, you bastards!” I shouted and flung myself sideways. Sure enough, Jopil’s sword smashed the ground to pieces. *Crack!* “Squad Leader!” Hyuk Mujin’s shout came a beat late. For all I had tried to stop him, he was already charging. Behind him, I saw Han Yeop with a set, determined face. “Hey, don’t—” “Jopil, you vile bastard!” “Get away from the Squad Leader!” But it was a step too late. Hyuk Mujin and Han Yeop, who had come running with everything they had, thrust their weapons at Jopil, who was preoccupied with me. “Die!” Sword and spear. Spear and sword. Good timing, good attacks, like they had practiced it beforehand. There was just one problem. They had the wrong opponent. “How dare you, you rats!” Jopil’s response was instant. He drove his sword into the ground where he stood, spun around, and smashed both weapons with his bare hands. Facing a sword and spear empty-handed was suicide. But in Murim, things were different. More precisely, Jopil was different. He was a Peak master. *Crack—Crunch!* His palm had only brushed the side of the blade, and Hyuk Mujin’s sword still shattered into pieces before it reached him. Han Yeop stared in horror at his spear, the head sliced clean off. That was the result of Jopil’s straightened knife-hand. “What the…” “That’s impossi—” Before they could finish, Jopil slammed both hands into their chests. They smashed into trees, spraying fountains of blood. “I’ll kill you.” On his chillingly smiling face, the whites of his eyes were gone. **Berserk** had worn off. He was back in his right mind. “Fuck…” From bad to worse. Trouble on top of trouble. Surrounded on all sides. Jopil, you son of a bitch. The situation was hurtling toward the worst possible outcome. If anyone was going to stop him, it had to be me. “Jopil—!” The internal energy I had pulled up at full strength raced through my whole body. I kicked off the ground and shot toward him. Jopil grinned wide. “Right. I’ll kill you first.” But I had something to count on. *He’s empty-handed right now.* *It was a blunder he’d made while Berserk. And I was sure I could finish everything before he yanked the sword out of the ground behind him and swung it.* The next instant, I hauled up every bit of internal energy in my dantian. I focused all of it on a single point—the spear tip—and thrust. “Die!” The final form of the Jin Family’s Spear Technique, Sky-Piercing Strike. If it could pierce the heavens, why couldn’t it pierce Jopil’s heart? I was sure of it. *This is it… the end.* The world slowed, and I saw Jopil’s face. He was smiling. The moment I saw that smile, I knew. Something was wrong. *Skrrrng.* Jopil’s sword was faster than my spear. The blood-wet crimson blade shoved my spear shaft aside and drove inward. The instant my spearhead, laden with internal energy, stabbed into empty air— *Slash.* A chilling sound, and my chest felt cool. Then came the searing pain, and the blood bursting out. Fortunately, I had jerked back at the last moment and avoided a fatal wound. *Damn it.* What the hell had just happened? As I staggered back, Jopil charged. *Whoosh-whoosh-whoosh!* Crimson sword-light poured down. Every flash was so fast and powerful I could barely see it. I gritted my teeth and swung my spear, but Jopil had the edge in both momentum and martial arts. *Slash. Thunk. Splurt.* Lightning cut across my whole body. The blade stabbed my shoulder, slashed my knee, and punched through my side before coming back out with a spray of blood. “Guh.” “You didn’t drop your weapon. I’ll give you that.” Jopil added, “If you can take this, too.” The next instant, his hand slammed into my chest. [^1]: A zhang is a traditional Chinese unit of distance, roughly 3.3 meters. [^2]: Mount Beimang is a burial mountain; hiking it means being dead. [^3]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement. [^4]: Junchi is a fish traditionally prized in Korea; the saying means that something of quality retains its worth even in decline. [^5]: Silk-reeling force is a method of twisting the entire body in a continuous, coiling motion to release power.

#### Chapter 30 tail (verified mastered)

…
there. A red-hot palm. The Flame Divine Palm. *Boom.* My chest caved in. My vision went white. Powerful fire qi tore through my body. *Boom.* The strength drained out of me. I heard the bones in my neck shift out of place beneath Jopil’s grip. His chilling voice slid into my ear. “You understand now, don’t you. Who you picked a fight with.” “…Cough.” “If King Yama asks, tell him I sent you.” To me, hanging limp as a corpse, Jopil declared it with a face full of rapture. “Die.” The final Flame Divine Palm shot toward my chest. Lava that would swallow my life whole was imbued in that blazing palm. And at last… *Tap.* The world stopped. There was no lava. No heat of any kind. Only his scarred, callused palm resting against my chest. A ripple ran through Jopil’s eyes. “You…” The strength slowly drained from the hand around my throat. As Jopil staggered backward, I saw a dagger buried below his navel. It had pierced his dantian. “This… what the hell is this?” The next moment, blood ran down Jopil’s chin. That was only the beginning. Blood started pouring from his eyes, his nose, and his ears as well. A waterfall of blood streamed from his seven orifices. The reconnaissance squad stopped in their tracks at the horrifying sight. Someone muttered, almost a groan. “Qi deviation…” Internal energy was a double-edged sword. I had waited for the moment Jopil drew his internal energy to its peak, then driven a dagger summoned from my Inventory into his dantian. The result was a reversal of his internal energy. Qi deviation. “You were definitely empty-handed.” I answered in a tired voice. “You live long enough, all sorts of things happen.” “I can’t die like this. This makes no sense.” Jopil muttered like a man whose soul had left him and took one step after another. Pools of blood formed wherever he passed. “I am Jopil. Jopil, One Question, One Kill. The nineteenth-generation successor of the Fire Gate Clan. I’m not someone who should die at the hands of a nobody like you!” Covered in blood and screaming, Jopil radiated a chilling, ghostly aura. Even the reconnaissance squad members who had charged in ready to die trembled with fear. “Then why? Why, at the likes of you, would I—!” That was when the ember I’d thought extinguished burst into flame. The change started in Jopil’s body. The flowing blood stopped, and the veins all over him stood out blue. He looked like a man who couldn’t feel the pain of both tendons being cut—or even the qi deviation. A terrible heat poured from the breath he exhaled. *What is this?* A literal resurrection? No. This was Jopil’s last desperate struggle. Everyone screamed, seized by terror, but I could see it clearly. His hair was turning white by the second. His skin was shriveling. Right now, that man was… *Burning his life.* *He’ll kill me, at least, before he goes.* Power gained by throwing away the most precious thing he had. Every bit of it was aimed at me. I knew on instinct that I couldn’t dodge. *Can I do this? Me?* I picked up the fallen spear. The *Sharp Spear* I’d used from the Tutorial until now. With its spearhead broken off, it was nothing more than a pointed iron rod. *I’ll end up looking like this soon enough too.* There was only one option left. Even if I succeeded, there was no guarantee I would survive. But there was no luxury of hesitation. “Jin Taekyung!” “Yeah. Let’s finish this.” Me and Jopil. Jopil and me. We shot toward each other. The heat pouring off him melted the piled snow and dried my lips. I drew a long breath. *Sss. Hoo.* The noise around me receded. My heartbeat and breathing sounded like thunder. *Thump. Thump-thump. Thump-thump-thump.* My heartbeat reached its peak. My breathing fell into place with mechanical precision. I was certain. *Now.* At the same time, I woke the internal energy in my dantian. Inside me, where my qi and blood channels were twisted and wrecked, the only thing left was the third internal energy, hardened like rock. My only option—and the last piece that would fill my Skill. *Run wild all you want.* The awakened internal energy went berserk. It forced its way through my ruined qi and blood channels and spread through my whole body. A dizzying pain hit me. But it was soon forgotten in the new strength the energy gave me. *Go!* Every muscle in my body pulled taut. From my calves and thighs, through my waist and along my thrusting arm, every ounce of strength and internal energy in me surged forward. Condensed air burst from the broken spear tip. Matching it, Jopil thrust out his Flame Divine Palm. “Dieeeee!” *Whoooosh.* A mound of snow erupted with the wind. Through the flakes drifting gently back down, Jopil came into view. From the right arm that had unleashed the Flame Divine Palm, through his shoulder and his side—half of his upper body had evaporated. “What kind of martial art…?” I dropped the spear and answered. “Thrust with All My Might.” The next instant, heaven and earth flipped upside down. Beyond my blurring vision, Jopil’s already lifeless head shot high into the sky. Socheon was crying out loud, holding a sword as tall as he was.

## Korean source

```text
＃31화



“어쭈. 이 자식은 팔자도 좋네.”

슬며시 눈을 뜨자 익숙한 얼굴이 보인다.

“소풍 왔냐? 게이트에서 잠을 자?”

깜빡 졸았던 모양이다. 나는 뻔뻔한 얼굴로 대꾸했다.

“안 잤어요. 자긴 누가 잤다고 그래.”

“입가에 침 자국이나 닦고 구라를 쳐라.”

“씁.”

“어이고, 이걸 확.”

주먹을 흔들어 보였지만 입가에는 웃음이 맺혀 있다. 나는 뻐근한 목을 주물렀다.

“어우, 피곤해.”

“어제 여자라도 만났냐. 왜 레이드 뛰면서까지 병든 닭처럼 꾸벅꾸벅 졸아?”

“제가 여자 만날 시간이 어디 있어요. 사정 뻔히 아시면서.”

“그렇긴 하지.”

첫 전투 때부터 지금까지, 5년이나 동고동락한 처지다. 내가 그를 잘 아는 것처럼 그도 나를 잘 알았다.

“그럼 왜 그러는데?”

“왜 그러겠습니까. 돈 때문이지.”

“돈? 설마 너 투잡 뛰냐?”

한껏 낮아진 목소리다. 나는 그의 등 너머로 휴식을 취하고 있는 팀원들을 바라보며 고개를 끄덕였다.

“와, 이 자식 이거. 짬밥 좀 먹었다고 뒷주머니를 차네. 그것도 부팀장이라는 놈이.”

“요즘 레이드도 줄었고, 급해서 그래요. 급해서. 형님도 다 해 봤으면서 그러시네.”

프로 라이센스를 가진 헌터는 투잡이 법적으로 금지되어 있다. D급만 되어도 이렇게 살지는 않을 텐데, 우리 같은 F급들은 별수 없다. 그런 사정을 알기 때문에 길드에서 알아도 모른 척 넘어가는 거지.

“그렇긴 한데…… 조심해라. 관리청에 민원이라도 들어오면 골치 아파져.”

“믿을 만한 곳이에요. 페이도 당일 현찰로 받아서 문제없고. 제가 괜히 하겠습니까.”

“그래?”

표정을 보아하니 구미가 당기는 모양이다.

“형님도 돈 필요하세요?”

“애가 셋이다. 마당에 유전이라도 터져야 해.”

그는 슬픈 눈으로 말을 쏟아 냈다. 이미 수십 번 들었던 레퍼토리다. 육아의 괴로움과 분유값 상승, 장사치들의 파렴치함에 대해 울분을 토해 낸 뒤 내 어깨를 두드렸다.

“넌 결혼하지 마라.”

“안 해요.”

정확히는 못 하는 거지만.

여자도 없고, 돈도 없다. 5년 내로 안전 구역의 집을 한 채 사는 게 인생의 목표인 나로서는 내심 그가 부러웠다.

사랑하는 배우자와 아이들. 행복한 가정. 그런 걸 언제쯤 가질 수 있을지 모르겠다.

“결혼은 늪이야.”

말은 저렇게 해도 소문난 애처가에 좋은 아빠다. 가끔 가족사진을 꺼내 보면서 흐뭇하게 웃는 것을 나는 알고 있었다.

“인생이 빨려 들어가. 정신 차려 보면 가슴까지 파묻혀서 간신히 숨만 쉬고 있다니까.”

“…….”

잘못 알고 있었을 수도 있겠다.

“그러니까 너무 일만 하지 말고 쉬면서 해, 쉬면서. 연애, 취미 생활 이런 거 좋잖아.”

“글쎄요. 아직은 돈이 급해서.”

머리를 긁적이며 대답했다. 그가 안쓰러운 눈으로 바라본다.

“아까 보니까 식은땀까지 흘려 가면서 자던데. 그러다가 과로로 훅 간다.”

“제가요?”

그러고 보니 등허리가 식은땀으로 축축하다. 뭔가 안 좋은 꿈을 꾼 모양인데…….

‘기억이 안 나네.’

보나 마나 개꿈이겠지, 뭐.



* * *



게이트(Gate).

지금이야 나 같은 헌터들의 밥줄 역할을 하고 있지만 그 실체는 마계 군단의 침공 루트다.

마왕 아스모데우스가 쓰러지면서 그의 강대한 군대도 패퇴했지만 수십 년이 지난 지금도 게이트만은 남아 있었다.

“수비 대형!”

그의 지휘에 따라 거대한 타워 실드를 짊어진 헌터 셋이 전방을 막았다. 길이 좁은 동굴에서는 이 정도만으로 대부분의 공격을 해소할 수 있다.

캉. 카캉!

“끼이이익!”

이십여 마리의 고블린이 독침과 도끼, 창을 투척했지만 크고 아름다운 타워 실드에 모두 튕겨 나갔다.

“궁수!”

전방에서는 탱커가 모든 공격을 막아 내고, 후방에서는 궁수가 화살을 쏟아 낸다. 전진 압박을 가하며 절반가량을 쓰러트리자 고블린들이 당황한 울음을 토해 냈다.

“까아아악!”

“끼익!”

때에 맞춰 그가 명령했다.

“공격 대형!”

탱커들이 타워 실드를 떨어트리는 동시에 뛰쳐나간다. 하지만 그보다 내가 더 빨랐다.

“핫!”

철창을 크게 휘두르자 초록색 피가 터지며 선두가 흐트러진다. 그 사이로 뛰어들며 닥치는 대로 찌르고 베자 대열이 우르르 무너져 내렸다.

“돌격!”

이어 딜러와 탱커들이 가세하자 고블린 무리는 순식간에 시체가 되어 누웠다.

“오늘 되게 쉬운데?”

“솔직히 부팀장이 반은 했지. 아주 날아다니던데, 언제 저렇게 실력이 좋아졌…… 쉿. 팀장님 열받았다.”

잡담을 나누던 사람들은 그가 나타난 순간 입을 다물었다.

“야, 진태경!”

깜짝이야.

멍하니 생각에 빠져 있던 나는 화들짝 놀라 반문했다.

“왜요?”

“너 인마, 누가 단독 행동 하래? 네가 탱커야? 공격 순서 다 잊었어? 그러고도 네가 부팀장이야?”

“그게 아니라요…….”

“이따위로 할 거면 팀 옮겨. 다른 팀원들까지 위험해지니까.”

그의 험악한 얼굴을 보다가 한숨을 내쉬었다.

“죄송합니다. 제가 왜 그랬는지 모르겠어요. 그냥, 갑자기 별것 아닌 것 같더라고요. 잠깐 미쳤나 봐요.”

기분이 묘했다. 고블린 무리를 보는 순간, 혼자서 저놈들을 쓸어버릴 수 있다는 생각이 들었다. 아니, 그건 확신이었다.

“너…….”

그가 말을 삼켰다. 서로 등을 맡기고 싸워 온 지 어언 5년, 지금 같은 돌발 행동은 이번이 처음이었다.

“다음부턴 이러지 마라. 힘든 일 있으면 말하고.”

어깨를 두드리고 떠나는 그의 뒷모습을 바라봤다. 왠지 모르게 가슴 한구석이 욱신거렸다.

‘병원이라도 가 봐야 하나.’

하지만 통증 따위는 이내 신경도 쓰지 않게 되었다.



* * *



“마정석 나왔습니다!”

“나왔어요!”

“또!”

“떴다. 떴다. 떴다!”

“엄마! 하연아!”

아, 마지막 외침은 내가 한 거다. 그도 잔뜩 달아오른 얼굴로 중얼거린다.

“야, 이게 다 뭐냐…….”

바닥에는 크고 작은 스무 개의 마정석이 가지런히 놓여 있었다.

마정석. 겉보기에는 붉은 돌멩이지만 게이트의 꽃이라 불리는 물건이다. 몬스터가 지닌 이 마력 덩어리는 고차원 에너지인 동시에 몬스터의 부산물 중 가장 값진 거다.

“이 정도면 개당 백만 원은 넘겠는데.”

E급 헌터로 이 바닥에서 10년을 버틴 팀장의 말이다. 그 황홀한 광경에 사람들의 눈동자가 스르르 풀어졌다.

“원래 이런 건가요?”

신입의 질문에 모두가 맹렬히 고개를 흔들었다.

“절대 아니지.”

F급 게이트에서는 평균이 한두 개고 아무리 운이 좋아도 다섯 개를 못 채운다. 나는 돈 계산에 바빴다.

‘마정석만 최소 이천 잡고, 부산물에 장비까지 하면 오백. 거기에 각종 수당까지 더하면…….’

시발. 이게 다 얼마야. 헌터를 시작한 이래 최고의 대박이다.

심지어 아직 레이드가 끝난 것도 아니다.

“우리가 지금 얼마쯤 왔지?”

“거의 다 왔죠. 오른쪽 길로 꺾으면 바로 보스 존이에요.”

보스 존. 그 단어에 모두의 눈이 번쩍였다.

당연한 말이지만, 보스 존에는 보스가 있다. 보스 몬스터는 해당 게이트에서 가장 강력한 몬스터. 그리고 가장 비싼 부산물과 장비, 마정석을 갖고 있는 몬스터다.

‘보스 몬스터까지 잡으면?’

말 그대로 잭팟이다. F급 헌터로 살아가면서 다시없을 절호의 기회인 것이다. 모두가 그런 생각으로 환하게 웃고 있던 그때였다.

“잠깐. 생각 좀 해 보고.”

아니, 이 인간이 지금 뭐라는 거야?

“그게 무슨 말이에요?”

“그렇잖아. 마주치는 몬스터는 일반 고블린뿐인데. 마정석이 이렇게 많이? 아무래도 이상해.”

그가 한숨을 내쉬었다. 아직도 흥분이 채 가라앉지 않아 붉은 얼굴에는 갈등이 떠올라 있었다.

“너희 기분 알아. 아는데…… 이미 엄청나게 챙겼다. 이 정도에서 만족하고 돌아가자.”

만족? 지금 여기서, 여기까지 와서 돌아가자고?

나는 다른 팀원들을 바라봤다. 그중에는 2, 3년간 손발을 맞춘 이들도 있고, 신입도 있다. 하지만 다들 나와 같은 얼굴을 하고 있었다.

“저는 반대…….”

그 순간 숨이 턱 막혔다. 빌어먹을. 또 가슴 통증이다.

어떻게든 말을 이으려고 했지만 목소리가 나오지 않았다. 이제는 이명까지 들리기 시작한다.

‘이게 무슨.’

통증도, 이명도 점점 심해지고 있었다. 나는 무릎을 꿇고 숨을 헐떡였다.

‘누가 나 좀. 나 좀 도와줘.’

누군가의 바짓가랑이를 붙잡고 매달렸다. 바로 그다. 지난 5년간 형제처럼, 아버지처럼 나를 돌봐 준 그였다.

‘형. 제발 저 좀 살려 줘요.’

그가 덤덤한 시선으로 날 내려다봤다.

“내가? 모두를 두고 도망친 너를?”

뭐?

“나도 살고 싶었어.”

나는 통증도 잊고 멍하니 그를 바라봤다. 옷과 피부가 녹아내리고 뼈가 드러났다. 나를 제외한 모두가 해골이 되어 널브러졌다.

‘아. 그랬었지.’

모두 죽었다. 2년 전 그날. 내가 가자고 주장했던 그 보스 존에서 모두가 죽었다.

‘나 혼자 살아남았어.’

나는 기억에 파묻혀 허우적거렸다. 보스 존에 내려앉은 불길한 어둠. 불쾌한 냄새와 축축한 바닥을 떠올렸고 놈의 거대한 날개를 기억했다.

허공에서 갈기갈기 찢겨 나가는 시신. 공포에 질린 비명과 도망치는 사람들.



‘이런 개새끼가!’



하지만 내 모든 걸 쏟아부은 스킬로도 놈을 죽일 수 없었다. 죽음을 기다리고 있던 나를 그가 일으켜 세웠다.



‘태경아!’

‘형, 미안해요. 전부 제 잘못이에요.’



나만 아니었으면. 내가 욕심을 부리지 않았다면 모두가 살 수 있었을 텐데. 가족에게 돌아갈 수 있었을 텐데.

어린애처럼 엉엉 우는 내게 그는 애써 미소를 지어 보였다.



‘그게 왜 네 책임이야? 자식이 이제는 팀장 흉내까지 내고 있어.’



거대한 동체가 동굴을 부유했다. 종유석이 쏟아지고 마지막 팀원이 단말마를 내질렀다. 어둠 속, 놈의 붉은 눈동자가 우리를 향했다.



‘저 건방진 새끼. 태경아. 먼저 가라.’

‘형. 천수 형!’



가슴이 아팠다. 눈앞이 아득해질 정도의 고통이 밀려들어 왔다. 용암을 삼킨 것처럼, 내 안의 모든 것들이 타들어 가는 것 같았다. 간간이 들리던 이명은 괴물의 포효로 바뀌었다.

캬우우우!



* * *



“형-!”

비명과 함께 눈을 떴다. 하지만 그곳은 게이트가 아니었고 몬스터도, 팀원들도 없었다. 햇빛이 쏟아지는 창가에서 한 사람이 일어났다.

“주군에 관한 꿈을 꾸신 겁니까? 전해 드리면 좋아하시겠군요.”

차가움이 뚝뚝 묻어 나오는 얼굴. 진위경의 오른팔인 위팽이다. 그를 보자 아직 게임 속이라는 것이 실감이 났다.

“괜찮으십니까?”

“아뇨. 악몽이었어요.”

“그럼 그 부분은 빼고 전하겠습니다.”

“마음대로.”

땀으로 온몸이 흠뻑 젖어 있었다. 온몸에 칭칭 감긴 붕대 틈새로 피딱지가 돋은 살이 보인다.

“제가 얼마나 누워 있었죠?”

“닷새 동안 혼절해 계셨습니다. 상태가 워낙 위중해서 하루를 못 넘길 거라는 게 약왕당주의 결론이었고요.”

“그래요?”

“예. 그 얘기를 들은 주군께서 길길이 날뛰셨죠. 제가 안 말렸으면 약왕당주를 때려죽였을 겁니다.”

“아.”

며칠 전 회의 때 백호당주의 항문에 대침을 꽂아 넣겠다고 하던 늙은이가 생각났다. 아주 죽으라고 염불을 외웠구나.

“다른 일들은 없었나요?”

“많은 일이 있었죠. 그중에서도 좋은 소식과 더 좋은 소식이 있는데…… 어느 것부터 들으시겠습니까?”

“좋은 소식부터.”

“우선 정찰조와 삭주 지부의 생존자들은 무사히 복귀했습니다. 그중 두 명은 제법 큰 부상을 입긴 했지만 목숨에는 지장이 없을 겁니다.”

생존자. 그 세 글자에 가슴이 덜컥 내려앉는다.

‘칠 호.’

목과 미간에 비수가 박힌 채 마지막 숨을 토하던 그 얼굴이 떠올랐다. 기껏해야 스물이나 되었을까. 목숨을 잃기에는 너무 어린 나이였다.

“죽은 이를 생각하십니까?”

“시신은, 시신은 수습했나요?”

“잘 수습하여 장사 지냈습니다. 천애 고아인지라 유족이 없더군요.”

“…….”

“한 말씀 드려도 되겠습니까?”

위팽은 대답을 기다리지 않았다. 그가 나를 향해 한발 다가오며 입을 열었다.

“삼공자, 수하의 죽음을 개죽음으로 만들지 마십시오.”

“그게 무슨…….”

“무인은 보호받는 존재가 아니라 적과 싸워 스스로를 증명하는 자들입니다. 비록 손쓸 수 없을 만큼 강한 적을 만나 죽었지만, 사망(死亡)이 아닌 전사(戰事)라는 말입니다.”

전장에서 죽었으니 영예로운 죽음이라는 말은 희대의 개소리다. 영예로운 죽음은 없다. 지금도 2년 전 죽은 동료들의 비명과 숨이 끊긴 칠 호의 부릅뜬 눈이 생생하다.

“죽었다는 사실은 변하지 않아요.”

“결코 변하지 않는 사실에 집착하는 사람도 있더군요. 누구라고는 말하지 않겠습니다.”

“…….”

“후회됩니까?”

“당연히.”

“그럼 그의 몫까지 사십시오.”

위팽이 이제껏 들어 본 적 없는 부드러운 목소리로 말을 이었다.

“죽은 이들을 잊으라는 말이 아닙니다. 가슴에 묻고, 머리에 새기라는 뜻입니다. 그 후회를 발판 삼아 그들이 꿈꿨던 곳까지 비상하는 것이 공자가 가야 할 길입니다.”

내가 가야 할 길이라…….

듣는 것만으로도 가슴 한구석이 울렁거리는 그 한마디를 곰곰이 생각하다가 풀썩 웃어 버렸다.

“젠장. 가다가 다리 부러지겠네.”

“일평생이 걸리겠죠.”

“일평생을 바치면 도착할 수 있을까요?”

“모릅니다. 저도 제 길이 어디까지인지 모르는데 공자의 길을 어찌 알겠습니까.”

“위 대협이 가는 길 끝에는 뭐가 있는데요?”

“천하제일인(天下第一人).”

농담? 아니다. 지금의 위팽은 그 어느 때보다 진지하고, 단호했다.

“어렵네요.”

“꿈이니까요.”

맞다. 꿈이란 늘 이루기 어렵다. 떠나보낸 이들의 꿈까지 짊어진다면 더더욱.

“위 대협. 한 가지만 물어봐도 될까요?”

“얼마든지요.”

“그 녀석, 이름이 뭐였습니까?”

“그의 이름은…….”

위팽의 입술이 열린 순간, 겨울 찬바람이 창문을 흔들었다.

휘이잉. 서늘한 바람 소리 너머로 칠 호의 이름이 들려온다.

“멋진 이름이네요.”

“본인이 직접 지었다고 들었습니다. 그만큼 꿈도 컸죠.”

“뭔데요?”

“고금제일인(古今第一人).”

“…….”

“고생 좀 하실 겁니다.”

“그러게요. 어이가 없네.”

실소가 터져 나온다. 그제야 무거웠던 마음이 홀가분해진 것이 느껴졌다. 모두 위팽 덕분이다.

“이제야 좀 원래대로 돌아왔군요.”

“고맙습니다.”

“별말씀을.”

고개를 까딱인 위팽이 입을 열었다.

“이제 더 좋은 소식이 남았군요.”

아, 그랬지. 좋은 소식과 더 좋은 소식.

나는 한껏 기대하며 이어질 말을 기다렸다.
```

## Current accepted English baseline

```markdown
# Chapter 31

“Well, look at this. This bastard’s got it made.”

I slowly opened my eyes to a familiar face.

“Did you come here for a picnic? Sleeping in a Gate?”

I must have dozed off. I answered, shameless.

“I wasn’t sleeping. Who says I was?”

“Wipe the drool off your mouth before you start lying.”

“Tsk.”

“Oh, you little—”

He shook a fist at me, but a smile sat at the corners of his mouth. I rubbed my stiff neck.

“Ugh, I’m tired.”

“Did you meet a woman yesterday? Why are you nodding off like a sick chicken even in the middle of a raid?”

“When would I have time to meet a woman? You know my situation.”

“True enough.”

We’d been through thick and thin for five years, from our first battle until now. He knew me as well as I knew him.

“Then what’s wrong?”

“What do you think? Money.”

“Money? Don’t tell me you’re moonlighting.”

His voice dropped low. I looked past his shoulder at the team members resting nearby and nodded.

“Well, well. This bastard gets a little time under his belt and now he’s stuffing his back pocket. And he’s the vice team leader, no less.”

“Raids have been scarce lately, and I’m strapped. Really strapped. You’ve done it yourself, hyung, so don’t give me that.”

Hunters with professional licenses were legally barred from second jobs. Even a D-rank probably wouldn’t have to live like this, but F-ranks like us had no choice. That was why the Guild looked the other way even when they knew.

“True, but… be careful. If someone files a complaint with the Management Agency, it’ll become a real headache.”

“It’s a trustworthy place. They pay cash the same day, so there’s no problem. You think I’d do this for nothing?”

“Really?”

Judging by his face, he was tempted.

“Do you need money too, hyung?”

“I’ve got three kids. I’d need an oil well to blow in the yard.”

He poured it out with a miserable look. I’d already heard this routine dozens of times. After venting about the misery of raising kids, the rising price of formula, and the shamelessness of merchants, he patted my shoulder.

“Don’t get married.”

“I won’t.”

More precisely, I couldn’t.

I had no woman and no money. My life’s goal was to buy a house in a safe zone within five years, so deep down I envied him.

A spouse I loved, and kids. A happy family. I had no idea when I’d ever get something like that.

“Marriage is a swamp.”

For all that talk, he had a reputation as a devoted husband and a good father. I knew how he sometimes took out his family photos and smiled fondly at them.

“Your whole life gets sucked in. You come to your senses and you’re buried up to your chest, barely breathing.”

“…”

Maybe I’d had the wrong idea about him.

“So don’t just work. Take breaks. Dating, hobbies—stuff like that’s good for you.”

“I don’t know. I still need the money.”

I scratched my head as I answered. He looked at me with pity.

“I saw you sleeping earlier, sweating cold the whole time. Keep that up and you’ll drop dead from overwork.”

“Was I?”

Now that he mentioned it, my back was damp with cold sweat. Must have been a bad dream…

*Can’t remember.*

Probably just some stupid dream anyway.

* * *

A Gate.

These days it was how Hunters like me made a living, but its true nature was an invasion route for the Demon Realm’s army.

When Demon King Asmodeus fell, his mighty army was routed with him. Decades later, the Gates were still there.

“Defensive formation!”

At his command, three Hunters bearing huge tower shields blocked the front. In a narrow cave, that alone was enough to soak most attacks.

*Clang! Clang-clang!*

“Giiiiik!”

About twenty goblins hurled poison needles, axes, and spears, but every one of them bounced off those big, beautiful tower shields.

“Archers!”

Up front, the tanks blocked every attack. From the rear, the archers poured arrows. We pushed forward and dropped about half of them, and the goblins let out panicked cries.

“Gyaaaah!”

“Kieek!”

He timed the next order perfectly.

“Attack formation!”

The tanks dropped their tower shields and burst forward at the same time. I was faster.

“Hah!”

I swung the iron spear in a wide arc. Green blood burst, and the front rank broke. I dove into the gap, stabbing and cutting at everything I could reach, and the line came crashing down.

“Charge!”

The damage dealers and tanks piled in, and in an instant the goblin pack was a pile of corpses.

“Pretty easy today, huh?”

“Honestly, the vice team leader did half of it. He was flying around. When did he get that good…? Shh. The Team Leader’s pissed.”

The people chatting shut their mouths the moment he appeared.

“Hey, Jin Taekyung!”

That made me jump.

I’d been staring off, lost in thought, and I startled as I answered.

“What?”

“Who told you to go solo? Are you a tank? Forget the attack order? And you still call yourself vice team leader?”

“That’s not—”

“If you’re going to act like this, transfer teams. You’re putting the rest of them in danger too.”

I looked at his grim face and sighed.

“I’m sorry. I don’t know why I did that. They just… suddenly didn’t seem like a big deal. I must have lost it for a second.”

The feeling was strange. The moment I saw the goblin pack, I’d thought I could wipe them out by myself.

No. That hadn’t been a thought.

It had been certainty.

“You…”

He swallowed the rest. We’d had each other’s backs for five years now, and this was the first time I’d ever pulled something like this.

“Don’t do it again. If you’re having a hard time, tell me.”

I watched him walk away after patting my shoulder. For some reason, a spot in my chest throbbed.

*Should I see a doctor?*

But before long I wasn’t even thinking about the pain.

* * *

“Magic Gems!”

“Got some!”

“Another!”

“Jackpot! Jackpot! Jackpot!”

“Mom! Hayeon!”

Ah, that last shout was mine. His face was flushed too as he muttered.

“Hey, what is all this…?”

Twenty Magic Gems, large and small, lay neatly on the floor.

Magic Gems. They looked like red pebbles, but they were called the flower of the Gate. These lumps of mana that monsters carried were high-dimensional energy, and the most valuable byproduct a monster had.

“At this rate, each one’s got to be worth over a million won.”

That from the Team Leader, an E-rank Hunter who’d lasted ten years in this business. People’s eyes went slack at the intoxicating sight.

“Is it normally like this?”

At the new recruit’s question, everyone shook their heads hard.

“Absolutely not.”

In an F-rank Gate the average was one or two, and even with incredible luck you wouldn’t hit five.

I was busy doing the math.

*Twenty million from the Magic Gems alone, another five million for the byproducts and Equipment. Add all the various allowances and…*

*Fuck. How much is this?*

The biggest jackpot I’d hit since becoming a Hunter.

And the raid wasn’t even over yet.

“How far have we come?”

“Almost there. Turn right and it’s the boss zone.”

The words *boss zone* made everyone’s eyes light up.

It went without saying, but a boss zone had a boss. A boss monster was the strongest monster in that Gate—and the one with the most expensive byproducts, Equipment, and Magic Gems.

*If we take down the boss monster too?*

A literal jackpot. A once-in-a-lifetime chance for an F-rank Hunter.

Everyone was smiling bright at the thought when he spoke.

“Wait. Let me think.”

What the hell was he talking about?

“What do you mean?”

“Think about it. Every monster we’ve run into has been an ordinary goblin. This many Magic Gems? Something’s off.”

He sighed. Excitement still hadn’t left his flushed face, but there was conflict on it too.

“I know how you feel. I do… but we’ve already grabbed a fortune. Let’s be satisfied with this much and go back.”

Satisfied?

Here? After coming this far, turn back?

I looked at the other team members. Some had been in sync for two or three years; some were new. They all had the same look I did.

“I’m against—”

My breath caught.

*Damn it. The chest pain again.*

I tried to keep talking, but no voice came out. Now there was ringing in my ears too.

*What is this?*

The pain and the ringing got worse and worse. I dropped to my knees, gasping.

*Someone. Please, help me.*

I grabbed someone’s pant leg and hung on.

It was him. The man who’d looked after me like a brother, like a father, for the past five years.

*Hyung. Please save me.*

He looked down at me, indifferent.

“Me? You, who ran and left everyone behind?”

What?

“I wanted to live too.”

I forgot the pain and stared at him. Clothes and skin melted away, and bone showed through. Everyone except me had become skeletons, sprawled across the ground.

*Ah. That’s right.*

They were all dead.

That day two years ago. In the boss zone I had insisted we enter, they had all died.

*I was the only one who survived.*

I floundered, buried in the memories. I remembered the ominous darkness that had settled over the boss zone, the foul smell, the damp floor, and that thing’s enormous wings.

Bodies ripped to shreds in midair. Screams of terror. People running.

*You fucking bastard!*

But even the Skill I had poured everything into hadn’t been enough to kill it. As I waited to die, he pulled me to my feet.

*Taekyung!*

*Hyung, I’m sorry. It was all my fault.*

If it hadn’t been for me. If I hadn’t gotten greedy, everyone could have lived. They could have gone home to their families.

I wailed like a child, and he forced a smile.

*How is that your fault? Look at this kid, now you’re even playing Team Leader.*

The massive body drifted through the cave. Stalactites rained down, and the last member of the team let out a death cry. In the darkness, its red eyes turned toward us.

*That arrogant bastard. Taekyung, you go first.*

*Hyung. Cheonsu hyung!*

My chest hurt. Pain rolled in hard enough to blank my vision. It felt like I had swallowed lava, like everything inside me was burning away. The ringing in my ears turned into a monster’s roar.

*Kyaaaaau!*

* * *

“Hyung—!”

I woke with the scream.

But it wasn’t a Gate. There were no monsters, and no team members.

Someone stood up at the window, where sunlight poured in.

“Did you dream about my lord? He’ll be pleased if I tell him.”

Coldness dripped from his face.

Wipeng, Jin Wikyung’s right-hand man.

Seeing him made it real that I was still inside the game.

“Are you all right?”

“No. It was a nightmare.”

“Then I’ll leave that part out of the report.”

“Suit yourself.”

I was soaked in sweat. Through the gaps in the bandages wound tight around my whole body, I could see flesh raised with blood scabs.

“How long was I out?”

“You were unconscious for five days. Your condition was so critical that the Medicine King Hall Leader concluded you wouldn’t last the day.”

“Really?”

“Yes. When my lord heard that, he went berserk. If I hadn’t stopped him, he would have beaten the Medicine King Hall Leader to death.”

“Ah.”

I remembered the old man from the meeting a few days ago, the one who had threatened to shove a giant needle into the White Tiger Hall Leader’s anus.

*So he really had been chanting for me to die.*

“Did anything else happen?”

“A great deal happened. Among it, there’s good news and even better news. Which would you like to hear first?”

“The good news.”

“First, the reconnaissance squad and the survivors of the Sakju Branch returned safely. Two of them suffered fairly serious injuries, but their lives are not in danger.”

*Survivors.*

The word made my heart drop.

*Number Seven.*

I remembered his face as he gasped out his last breath, a dagger in his throat and another between his brows. Twenty at most. Far too young to lose his life.

“Are you thinking of the dead?”

“The body—did they recover the body?”

“We recovered it properly and buried him. He was an orphan with no one in the world, so there were no surviving relatives.”

“…”

“May I say something?”

Wipeng didn’t wait for an answer. He took a step toward me and went on.

“Third Young Master, do not turn your subordinate’s death into a dog’s death.”

“What does that…”

“Martial artists are not beings meant to be protected. They are people who fight their enemies and prove themselves. He died facing an enemy too strong to do anything about, but that was not mere death—it was death in battle.”

The idea that dying on a battlefield made it an honorable death was the biggest load of bullshit ever.

There was no such thing as an honorable death. Even now, the screams of my comrades who died two years ago and Number Seven’s wide-open eyes as his breath left him were still vivid.

“The fact that he died hasn’t changed.”

“There are people who cling to facts that will never change. I won’t say who.”

“…”

“Do you regret it?”

“Of course.”

“Then live his share as well.”

Wipeng continued in a gentler voice than I had ever heard from him.

“I’m not telling you to forget the dead. Bury them in your heart and carve them into your mind. Use that regret as a foothold and soar to the place they dreamed of reaching. That is the path you must take, Young Master.”

*The path I must take…*

Just hearing those words made something in my chest lurch. I turned them over for a while, then let out a sudden laugh.

“Damn. I’ll break a leg before I get there.”

“It will take a lifetime.”

“If I give it my whole life, can I make it there?”

“I don’t know. I don’t even know how far my own path goes, so how could I know yours?”

“What’s at the end of the road Great Hero Wipeng is walking?”

“Number One Under Heaven.”

A joke?

No. Wipeng was more serious and resolute than ever.

“That’s a hard one.”

“Because it’s a dream.”

He was right. Dreams were always hard to reach.

Even more so if you were carrying the dreams of those you had lost.

“Great Hero Wipeng. May I ask you one thing?”

“Anything.”

“That guy. What was his name?”

“His name was…”

The moment Wipeng opened his lips, a cold winter wind shook the window.

*Whoooosh.*

Beyond the chill of the wind, I heard Number Seven’s name.

“That’s a cool name.”

“I heard he chose it himself. His dream was just as big.”

“What was it?”

“Number One of All Time.”

“…”

“You’re going to have a hard time.”

“Yeah. That’s unbelievable.”

A laugh slipped out. Only then did I feel the weight in my heart lift.

It was all thanks to Wipeng.

“You’re finally back to your old self.”

“Thank you.”

“Don’t mention it.”

Wipeng tipped his head and spoke.

“Now, there’s still the even better news.”

Ah. Right.

Good news and even better news.

I waited, as expectant as I could get, for what he would say next.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 31`.

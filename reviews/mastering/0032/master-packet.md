# Master Edit Task — Chapter 32

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
| 조필     | **Jopil**          |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 낭인     | **wandering martial artist**                     |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 보상               | **Reward**                     |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 삭주 | **Sakju** | Jin Family branch location |
| 혼주 | **Honju** | Shanxi location |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
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

#### Chapter 30 tail (verified mastered)

…
there. A red-hot palm. The Flame Divine Palm. *Boom.* My chest caved in. My vision went white. Powerful fire qi tore through my body. *Boom.* The strength drained out of me. I heard the bones in my neck shift out of place beneath Jopil’s grip. His chilling voice slid into my ear. “You understand now, don’t you. Who you picked a fight with.” “…Cough.” “If King Yama asks, tell him I sent you.” To me, hanging limp as a corpse, Jopil declared it with a face full of rapture. “Die.” The final Flame Divine Palm shot toward my chest. Lava that would swallow my life whole was imbued in that blazing palm. And at last… *Tap.* The world stopped. There was no lava. No heat of any kind. Only his scarred, callused palm resting against my chest. A ripple ran through Jopil’s eyes. “You…” The strength slowly drained from the hand around my throat. As Jopil staggered backward, I saw a dagger buried below his navel. It had pierced his dantian. “This… what the hell is this?” The next moment, blood ran down Jopil’s chin. That was only the beginning. Blood started pouring from his eyes, his nose, and his ears as well. A waterfall of blood streamed from his seven orifices. The reconnaissance squad stopped in their tracks at the horrifying sight. Someone muttered, almost a groan. “Qi deviation…” Internal energy was a double-edged sword. I had waited for the moment Jopil drew his internal energy to its peak, then driven a dagger summoned from my Inventory into his dantian. The result was a reversal of his internal energy. Qi deviation. “You were definitely empty-handed.” I answered in a tired voice. “You live long enough, all sorts of things happen.” “I can’t die like this. This makes no sense.” Jopil muttered like a man whose soul had left him and took one step after another. Pools of blood formed wherever he passed. “I am Jopil. Jopil, One Question, One Kill. The nineteenth-generation successor of the Fire Gate Clan. I’m not someone who should die at the hands of a nobody like you!” Covered in blood and screaming, Jopil radiated a chilling, ghostly aura. Even the reconnaissance squad members who had charged in ready to die trembled with fear. “Then why? Why, at the likes of you, would I—!” That was when the ember I’d thought extinguished burst into flame. The change started in Jopil’s body. The flowing blood stopped, and the veins all over him stood out blue. He looked like a man who couldn’t feel the pain of both tendons being cut—or even the qi deviation. A terrible heat poured from the breath he exhaled. *What is this?* A literal resurrection? No. This was Jopil’s last desperate struggle. Everyone screamed, seized by terror, but I could see it clearly. His hair was turning white by the second. His skin was shriveling. Right now, that man was… *Burning his life.* *He’ll kill me, at least, before he goes.* Power gained by throwing away the most precious thing he had. Every bit of it was aimed at me. I knew on instinct that I couldn’t dodge. *Can I do this? Me?* I picked up the fallen spear. The *Sharp Spear* I’d used from the Tutorial until now. With its spearhead broken off, it was nothing more than a pointed iron rod. *I’ll end up looking like this soon enough too.* There was only one option left. Even if I succeeded, there was no guarantee I would survive. But there was no luxury of hesitation. “Jin Taekyung!” “Yeah. Let’s finish this.” Me and Jopil. Jopil and me. We shot toward each other. The heat pouring off him melted the piled snow and dried my lips. I drew a long breath. *Sss. Hoo.* The noise around me receded. My heartbeat and breathing sounded like thunder. *Thump. Thump-thump. Thump-thump-thump.* My heartbeat reached its peak. My breathing fell into place with mechanical precision. I was certain. *Now.* At the same time, I woke the internal energy in my dantian. Inside me, where my qi and blood channels were twisted and wrecked, the only thing left was the third internal energy, hardened like rock. My only option—and the last piece that would fill my Skill. *Run wild all you want.* The awakened internal energy went berserk. It forced its way through my ruined qi and blood channels and spread through my whole body. A dizzying pain hit me. But it was soon forgotten in the new strength the energy gave me. *Go!* Every muscle in my body pulled taut. From my calves and thighs, through my waist and along my thrusting arm, every ounce of strength and internal energy in me surged forward. Condensed air burst from the broken spear tip. Matching it, Jopil thrust out his Flame Divine Palm. “Dieeeee!” *Whoooosh.* A mound of snow erupted with the wind. Through the flakes drifting gently back down, Jopil came into view. From the right arm that had unleashed the Flame Divine Palm, through his shoulder and his side—half of his upper body had evaporated. “What kind of martial art…?” I dropped the spear and answered. “Thrust with All My Might.” The next instant, heaven and earth flipped upside down. Beyond my blurring vision, Jopil’s already lifeless head shot high into the sky. Socheon was crying out loud, holding a sword as tall as he was.

#### Chapter 31 tail (verified mastered)

…
team let out a death cry. In the darkness, its red eyes turned toward us. *That arrogant bastard. Taekyung, you go first.* *Hyung. Cheonsu hyung!* My chest hurt. Pain rolled in hard enough to blank my vision. It felt like I had swallowed lava, like everything inside me was burning away. The ringing in my ears turned into a monster’s roar. *Kyaaaaau!* * * * “Hyung—!” I woke with the scream. But it wasn’t a Gate. There were no monsters, and no team members. Someone stood up at the window, where sunlight poured in. “Did you dream about my lord? He’ll be pleased if I tell him.” Coldness dripped from his face. Wipeng, Jin Wikyung’s right-hand man. Seeing him drove home that I was still inside the game. “Are you all right?” “No. It was a nightmare.” “Then I’ll leave that part out when I tell him.” “Suit yourself.” My whole body was soaked in sweat. Through the gaps in the bandages wound tight around me, I could see flesh raised with blood scabs. “How long was I out?” “You were unconscious for five days. Your condition was so critical that the Medicine King Hall Leader concluded you wouldn’t last the day.” “Really?” “Yes. When my lord heard that, he went berserk. If I hadn’t stopped him, he would have beaten the Medicine King Hall Leader to death.” “Ah.” I remembered the old man from the meeting a few days ago, the one who had threatened to shove a giant needle into the White Tiger Hall Leader’s anus. *So he really had been chanting for me to die.* “Did anything else happen?” “A great deal happened. Among it, there’s good news and even better news. Which would you like to hear first?” “The good news.” “First, the reconnaissance squad and the survivors of the Sakju Branch returned safely. Two of them suffered fairly serious injuries, but their lives are not in danger.” *Survivors.* The word made my heart sink. *Number Seven.* I remembered his face as he gasped out his last breath, a dagger in his throat and another between his brows. Twenty at most. Far too young to lose his life. “Are you thinking of the dead?” “The body—did they recover the body?” “We recovered it properly and held a funeral for him. He was an orphan with no one in the world, so there were no surviving relatives.” “…” “May I say something?” Wipeng didn’t wait for an answer. He took a step toward me and went on. “Third Young Master, do not turn your subordinate’s death into a dog’s death.” “What does that…” “Martial artists are not beings meant to be protected. They are people who fight their enemies and prove themselves. He died facing an enemy too strong to do anything about, but that was not mere death—it was death in battle.” The idea that dying on a battlefield made it an honorable death was the biggest load of bullshit ever. There was no such thing as an honorable death. Even now, I could vividly hear the screams of my comrades who had died two years ago. I could still see Number Seven’s wide-open eyes as he breathed his last. “The fact that he died hasn’t changed.” “There are people who cling to facts that will never change. I won’t say who.” “…” “Do you regret it?” “Of course.” “Then live his share as well.” Wipeng continued in a gentler voice than I had ever heard from him. “I’m not telling you to forget the dead. Bury them in your heart and carve them into your mind. Use that regret as a foothold and soar to the place they dreamed of reaching. That is the path you must take, Young Master.” *The path I must take…* Just hearing those words made something in my chest lurch. I turned them over for a while, then let out a sudden laugh. “Damn. I’ll break my legs before I get there.” “It will take a lifetime.” “If I devote my whole life to it, can I make it there?” “I don’t know. I don’t even know how far my own path goes, so how could I know yours?” “What’s at the end of your path, Great Hero Wipeng?” “Number One Under Heaven.” A joke? No. Wipeng was more serious and resolute than ever. “That’s a hard one.” “Because it’s a dream.” He was right. Dreams were always hard to reach. Even more so if you were carrying the dreams of those you had lost. “Great Hero Wipeng. May I ask you one thing?” “Anything.” “That guy. What was his name?” “His name was…” The moment Wipeng opened his lips, a cold winter wind shook the window. *Whoooosh.* Beyond the chilly sound of the wind, I heard Number Seven’s name. “That’s a cool name.” “I heard he chose it himself. His dream was just as big.” “What was it?” “Number One of All Time.” “…” “You’re going to have a hard time.” “Yeah. This is ridiculous.” A laugh slipped out. Only then did I feel the weight lift from my heart. It was all thanks to Wipeng. “You’re finally back to your old self.” “Thank you.” “Don’t mention it.” Wipeng gave a slight nod and spoke. “Now, there’s still the even better news.” Ah. Right. Good news and even better news. Brimming with anticipation, I waited for him to continue.

## Korean source

```text
＃32화



“이틀 전 큰 전투가 있었습니다. 혼주(昏住)에서 본가의 정예 일백과 항산검문의 선봉 이백이 맞붙었죠.”

“전투가 있었다고요?”

심지어 수백 명이 투입된 큰 전투란다. 순간 가슴이 덜컥했지만 앞서 위팽이 했던 말이 생각났다.

좋은 소식과 더 좋은 소식. 결과는 이미 들은 셈이다.

“우리가 이겼군요.”

“대승입니다. 살아서 도망친 놈들은 서른이 채 되지 않습니다. 본가의 사상자 숫자와 비슷하죠.”

위팽의 이마부터 턱까지 그어진 상처를 보건대 상당히 격렬한 전투였던 모양이다.

‘하긴. 병력 차이가 두 배나 났으니까.’

아무튼 이겨서 다행이다. 태원진가 입장에서는 가문의 전력을 절반 가까이 쏟아부은 전투. 만약 졌다면 타격이 막대했을 것이다.

“항산검문의 소가주를 놓친 건 아쉽지만 항산쌍귀(恒山雙鬼)를 잡은 건 큰 수확입니다.”

“항산썅귀요?”

“항산쌍귀 말입니다. 항산검문 휘하의 절정 고수들인데…… 충성심 하나는 대단하더군요. 목숨을 도외시하고 덤비는 통에 어쩔 수 없이 죽였죠.”

위팽이 새로 생긴 상처를 톡톡 건드렸다.

“붙잡았다면 중요한 정보를 캐낼 수 있었을 텐데.”

“그쪽이, 아니 위 대협이 죽였나요?”

“주군과 제가 한 놈씩 맡았습니다. 제법이더군요.”

“…….”

호로록, 차를 들이켜는 위팽의 모습에 할 말을 잃었다.

‘이런 씨바…… 절정 고수가 장난이야?’

내 27년 인생을 통틀어 가장 치열한 싸움이었다. 온갖 내상에 스테이크처럼 칼질도 당했다. 그러고도 닷새 동안 뻗어 있었으니 요단강에서 반신욕 정도는 한 거다.

그런데 그 정도의 절정 고수를 잡아 놓고. 뭐, 제법이라고?

‘이건 완전히 괴물이잖아.’

이번 기회에 확실히 알았다. 절정 고수에도 급이 있다는 사실을. 그 정도의 고수들이 내 편이라는 게 천만다행이다.

“그건 그렇고.”

달그락.

찻잔을 내려놓은 위팽이 미묘한 눈빛으로 나를 응시했다.

“대단하시더군요.”

“예?”

“일문일살 조필 말입니다. 그를 해치운 건 대단하다는 말로도 표현이 불가능한 일입니다.”

“…….”

난 당신들이 더 대단해 보이는데. 이건 마치 A급 헌터에게 고블린 잘 잡는다고 칭찬받은 기분이다.

“아, 예. 뭐 감사합니다.”

조필에 관한 이야기는 이쯤에서 마무리 짓고 싶었다. 몸 상태도, 기분도 별로인 데다 밀려 있는 시스템 보상을 확인하고 싶었기 때문이다.

‘이제 좀 쉬자. 나 아직 환자야, 인마.’

그런 의미를 담아 윙크를 날리자 위팽이 눈살을 찌푸렸다.

“눈이 아프십니까? 의원을 부를까요?”

“……아뇨. 괜찮아요.”

“방금 눈 쪽에 경련이 일어났는데요.”

“그건 경련이 아닌데요.”

“맞습니다, 경련. 제대로 봤습니다.”

“아니, 방금 그건…….”

그때 위팽이 눈깔을 허옇게 뒤집고 부르르 떨었다.

탁자가 흔들리고 잔에서 찻물이 흘러넘쳤다. 나는 깜짝 놀라 외쳤다.

“세상에, 위 대협!”

이 인간 간질 환자구나. 아니, 무슨 절정 고수씩이나 되는 양반이 간질에 걸렸대?

내가 황급히 일어나려 할 때 떨림이 멈췄다. 정상으로 돌아온 위팽이 평온한 얼굴로 말했다.

“이러셨습니다.”

“괜찮으시…… 아니, 예?”

“삼공자께서 방금 이러셨다고요. 눈에 경련이 일어났어요.”

“그러니까. 절 따라 하신 거라고요?”

“예.”

아니, 이건 무슨 종류의 또라이야…….

나는 윙크와 간질의 차이를 설명해 주려 했지만, 말문이 막혔다. 위팽이 열받은 독재자처럼 나를 노려보는 중이었다.

“……그냥 조필 얘기나 마저 할까요?”

“그러시죠.”

위팽이 만족스럽게 고개를 끄덕였다.

‘또라이 새끼.’

결국 나는 조필과의 싸움을 처음부터 끝까지 털어놔야 했다.

그가 어떻게 움직였고 무슨 무공을 썼는지. 위팽의 날카로운 질문 때문에 긴장되는 순간도 있었다.

“비수로 조필의 다리 근맥을 끊으셨다고요?”

“네. 미리 숨겨 둔 거였죠.”

“조필이 그걸 못 알아차렸을 리가 없는데…… 계속하십시오.”

마침내 긴 이야기가 끝났을 때, 위팽은 참았던 숨을 토해 냈다. 나를 바라보는 눈빛에 복잡한 심정이 그대로 전해진다.

“삼공자. 실로 큰 공을 세우셨습니다.”

“아, 감사합니…….”

“인정하긴 싫지만 진심입니다.”

“……아, 예.”

“지금껏 사고 치신 걸 생각하면 피가 거꾸로 솟지만 정말 감탄했습니다. 진심입니다.”

“…….”

“누가 생각이나 했겠습니까. 허구한 날 가문 공금 훔쳐서 주루에 갖다 바치고, 술에 떡이 돼서 거리를 활보하며 가문 명성에 똥칠을 하던 삼공자께서 이리 큰사람이 되실 줄이야. 이 위팽, 진심으로 탄복했습니다.”

차라리 욕을 해, 이 새끼야…….

나는 튀어나오려는 쌍욕을 간신히 참으며 말했다.

“운이 좋았죠. 조필이 방심한 것도 있고요.”

위팽이 고개를 저었다.

“아닙니다. 전부 실력입니다. 누가 방심했고 비수를 숨겨 뒀느냐는 핑계가 되지 못합니다. 고작 그 정도로 조필을 죽일 수 있었다면 그는 일문일살 조필이 아니었을 겁니다. 무림은 강한 자만이 살아남는 곳이니까요.”

“강한 자만이 살아남는다.”

그 말을 조용히 혀끝에서 굴렸다. 어딘지 모르게 쓰고 달콤하다.

무림은, 이 게임은 처음부터 그런 곳이었다. 나는 그런 곳에서 살아남았고, 강해진 것이다.

“조필은 전심무공을 모두 발휘했습니다. 마지막에는 선천지기까지 끌어올렸고요. 절정 고수가 스스로의 목숨을 버려 가며 공자를 죽이려 한 겁니다. 하지만 결과는 어떻습니까?”

“제가 이겼죠.”

“예. 바로 그겁니다.”

“그럼 저는 조필보다 강했던 거군요.”

아까부터 떨떠름하던 위팽이 정색을 하고 말했다.

“무슨 소립니까. 조필이 더 강하죠. 절정 고수가 장난처럼 보이세요?”

“…….”

“기습으로 조필을 죽일 정도로만 강하신 겁니다.”

적당히 해라, 진짜.

인벤토리에서 무기를 꺼낼까 말까 고민하고 있을 때 위팽이 피식 웃었다. 처음 보는 그의 웃음이다.

“잘하셨습니다.”

나는 의심 어린 눈길로 위팽을 바라봤다.

“이번엔 또 무슨 말을 덧붙이시려고?”

웃음이 더욱 짙어졌다.

“진심입니다. 제가 공자를 상당히 싫어했던 건 사실이지만…… 이번만큼은 인정하지 않을 도리가 없군요.”

이렇게 나오면 할 말이 없다. 나는 왠지 모르게 민망해져서 헛기침을 내뱉었다.

“크흠. 뭐 죽을 뻔하긴 했지만 겨우 조필이랑 낭인 몇 명 잡은 게 전부인데요. 크흠.”

“한 성(城)에 절정 고수가 몇이나 있다고 생각하십니까? 본가가 위치한 산서를 통틀어도 채 스물이 되지 않습니다.”

스물이라. 예상보다 훨씬 적은 숫자다.

“항산검문 쪽 피해가 상당하겠네요. 그런 절정 고수를 셋이나 잃었으니.”

“하지만 가장 큰 타격은 따로 있지요.”

“그게 뭔데요?”

“그건…….”

위팽이 입을 연 그 순간이었다.

“명분. 이 전쟁을 시작하게 된 명분이 사라진 거지. 태원진가의 삼공자는 독 따위를 쓰지 않아도 충분히 강하니까. 암, 그렇고말고.”

문가에서 들려온 떨리는 목소리. 거구의 진위경이 울먹거리며 두 팔을 벌렸다.

“막내야아아!”

“…….”

제발 나 좀 내버려 둬.



* * *



결국 나는 지난 며칠간의 추격전과 조필과의 일전을 다시 한번 반복 재생해야 했다.

“그때 생존자들을 추적해 온 낭인들이…….”

“이런 찢어 죽일 놈들!”

쾅!

“조필의 화염신장에 내상을…….”

“죽일 놈! 악랄한 낭인 새끼가 감히! 오장육부를 뜯어내고 잘근잘근 씹어 먹어도 시원찮을 놈!”

쾅쾅쾅!

“…….”

나는 멍한 얼굴로 초토화가 된 침실을 바라봤다. 진위경의 과한 몰입감이 불러온 결과였다.

위팽은 진작 멀찍이 떨어져서 입을 벙긋거리고 있었다.

- 그 얘기는 다시 안 하는 게 좋겠습니다.

처음으로 우리 둘의 의견이 일치된 순간이었다.

진위경은 한참을 씨근덕거리다가 안정을 되찾았…….

“놈이 살아 있었다면 곱게 죽진 못했을 것이다.”

콰드득. 나는 침대 모서리가 가루가 되어 흩날리는 광경을 슬픈 눈으로 지켜봤다. 위팽이 고개를 절레절레 흔들었다.

“주군. 그만 진정하시지요. 공자께서 불안해하시는 것 같은데요.”

이번 말은 확실히 효과가 있었다. 온몸에 붕대를 두른 채 슬픈 눈으로 앉아 있는 나를 본 진위경이 눈시울을 붉혔다.

“우리 막내 좀 보게. 이 어린 녀석이 얼마나 고초를 겪었으면 이리 넋이 나가 있단 말인가.”

덥석!

솥뚜껑만 한 손이 어깨를 잡고 끌어당긴다. 나도 한 덩치 하는데 이 인간은 거의 소형 오우거급이다. 나는 그의 넓은 가슴에 안겨 두려움에 몸을 떨었다.

“그래, 막내야. 이제 괜찮다. 괜찮아.”

혼자만 감동적인 포옹을 끝낸 진위경이 코를 훌쩍였다.

“언제까지 어린아이일 줄만 알았는데…… 이제 다 컸구나. 위팽, 그거 아는가?”

위팽이 숨도 쉬지 않고 대답했다.

“예. 말씀 안 해 주셔도 됩니다.”

물론 진위경은 들은 척도 하지 않았다.

“본가는 물론이고 저잣거리에까지 소문이 퍼지고 있네. 결사대를 이끌고 적진을 기습. 일문일살 조필과 일백의 낭인들을 쓰러트리고 삭주 지부의 식솔들을 구출해 낸 영웅의 이야기 말일세.”

“와. 그거 대단…… 예?”

나는 눈을 깜빡였다. 잠깐만. 저게 내 이야기였어?

“저기, 뭔가 오해가 있는 것 같은데요.”

“맞습니다. 주군. 뭔가 오해가…….”

진위경은 흐뭇하게 웃었다.

“우리 막내, 겸손하기도 하지. 위팽 자네는 입 닥치게.”

“아뇨, 겸손이 아니라 소문이 좀 왜곡된 것 같은데.”

“맞습니다. 주군이 공자를 아끼시는 건 알지만 이건 너무 나가셨습니다. 소문이 너무 허황되면 사람들이 믿지 않을…….”

“소문? 허황?”

콰광!

위팽의 목소리는 굉음에 파묻혀 사라졌다. 나는 뻥 뚫린 침실 벽면을 바라보며 입을 딱 벌렸다.

‘뭔 짓거리야. 미친놈아.’

진위경이 다시 한번 주먹을 뻗었다. 압축된 공기가 터져 나가는 소리와 함께 그나마 남아 있던 벽이 무너져 내렸다.

이 층짜리 전각에서 나무와 벽돌이 쏟아져 내리니 밖에 있던 사람들이 아우성을 쳤다.

“삼공자다! 삼공차 처소가 무너지고 있다!”

“사람들 불러와. 빨리!”

모두가 충격에서 벗어나지 못하고 있을 때, 진위경이 내 몸을 번쩍 들어 올렸다.

‘놔. 놔, 이 미친놈아!’

온 힘을 다해 몸부림쳤지만 진위경을 당해 낼 수는 없었다. 한 발. 한 발. 뻥 뚫린 벽을 향해 걸어갈 때마다 공포가 밀려왔다.

‘떨어트릴 속셈이구나!’

밑에는 50명도 넘는 사람이 운집해 있었다. 말이 좋아 이 층이지, 전각이 워낙 커서 10m는 되는 높이다. 불어오는 바람이 아찔했다.

‘떨어지면 최소 골절이다.’

등골이 서늘한 순간에도 사람들은 꾸역꾸역 모여들고 있었다. 50명이 넘어가는 인원이 고개를 꺾어 우리를 바라봤다.

“누구야? 사고 난 거 아니었어?”

“소가주님인데? 품에 안긴 건 누구지?”

“삼공자. 삼공자다!”

누군가의 외침에 술렁임이 번졌다.

“삼공자, 아니 삼공자님이라고?”

“일문일살 조필을 쓰러트린 삼공자께서 깨어나셨다!”

이게 뭔 상황이야. 눈과 귀가 홱홱 돌아갈 때 진중한 목소리가 또렷이 들렸다.

“보이느냐?”

“아, 예. 보이긴 하는데요. 좀 내려 주실…….”

“들리느냐?”

“들리기도 하는데요. 일단 좀.”

“무엇이 느껴지느냐?”

“부끄러움이요. 그리고 수치심.”

“저들은 널 믿고 있다. 네 이름을 부르고 있다!”

“아니, 이 시발 놈아.”

마지막 욕은 사람들의 외침에 파묻혀 사라졌다.

“삼공자! 삼공자!”

그 잠깐 사이에 수십 명이 더 늘었다. 무수히 많은 시선이 우수수 날아와 꽂힌다.

‘아니, 이게 무슨.’

그때 진위경이 비장한 얼굴로 내 겨드랑이로 손을 집어넣었다. 그리고 번쩍 들어 올렸다.

때맞춰 우레 같은 함성이 터져 나왔다.

“와아아아아!”

“삼공자! 진태경!”

“산서잠룡! 산서잠룡!”

그리고…….

‘시발. 이건 뭐 아기 사자도 아니고.’

내 귀에는 오래된 애니메이션의 BGM이 울려 퍼졌다.
```

## Current accepted English baseline

```markdown
# Chapter 32

“There was a major battle two days ago. One hundred elite fighters from our family clashed with two hundred vanguard troops from the Mount Heng Sword Sect in Honju.”

“There was a battle?”

And a major one, no less—hundreds of people thrown in. My heart lurched for a moment, but then I remembered what Wipeng had said earlier.

Good news and even better news. I’d already heard the outcome.

“We won.”

“It was a great victory. Fewer than thirty of them escaped alive. That’s about the same as our family’s casualties.”

Judging by the scar running from Wipeng’s forehead to his chin, it must have been a fierce fight.

*Well, of course. They outnumbered us two to one.*

Still, it was a relief we’d won. From the Jin Family of Taiyuan’s perspective, we’d poured in nearly half our strength. If we’d lost, the damage would have been enormous.

“It’s unfortunate we let the Mount Heng Sword Sect’s Lesser Family Head escape, but taking the Mount Heng Twin Devils was a major haul.”

“The Mount Heng Twin D-Devils?”

“The Mount Heng Twin Devils. Peak masters under the Mount Heng Sword Sect, and their loyalty was something else… They kept throwing themselves at us without any regard for their lives, so we had no choice but to kill them.”

Wipeng tapped the fresh scar.

“If we’d captured them, we could have extracted some important information.”

“Did you—I mean, did Great Hero Wipeng kill them?”

“My lord and I took one each. They were pretty good.”

“…”

I was left speechless as Wipeng slurped his tea.

*For fuck’s sake… Are Peak masters a joke to him?*

It had been the fiercest fight of my twenty-seven years. All kinds of internal injuries, and I’d been sliced up like a steak. I’d been out for five days after that, so I’d practically taken a half-bath in the River Jordan.[^1]

And after taking down Peak masters of that caliber. What, *pretty good*?

*He’s a complete monster.*

I learned something for certain this time: even Peak masters came in different levels. It was a huge relief that people of that caliber were on my side.

“That aside…”

*Clink.*

Wipeng set down his teacup and looked at me with a peculiar expression.

“You were remarkable.”

“Pardon?”

“I’m talking about Jopil, One Question, One Kill. Defeating him isn’t something the word remarkable can even cover.”

“…”

*You people seem more remarkable to me.*

It felt like getting praised by an A-rank Hunter for being good at killing goblins.

“Ah. Yes. Thank you, I suppose.”

I wanted to wrap up the Jopil talk there. My body and my mood were both in bad shape, and I wanted to check the System Rewards still waiting for me.

*Let’s rest now. I’m still a patient, damn it.*

I put that meaning into a wink. Wipeng frowned.

“Does your eye hurt? Shall I call a physician?”

“…No. I’m fine.”

“Your eye just spasmed.”

“That wasn’t a spasm.”

“It was a spasm. I saw it clearly.”

“No, just now, that was…”

Then Wipeng rolled his eyes back until only the whites showed and started to tremble.

The table shook, and tea spilled over the rim of the cup. I cried out in alarm.

“My God, Great Hero Wipeng!”

*This guy’s epileptic. No—how does a Peak master even get epilepsy?*

Just as I hurriedly tried to stand, the trembling stopped. Back to normal, Wipeng spoke with a perfectly calm face.

“You did this.”

“Are you all ri—wait, what?”

“That’s what you did just now, Third Young Master. Your eye spasmed.”

“So you were imitating me?”

“Yes.”

*What kind of lunatic is this…*

I tried to explain the difference between a wink and an epileptic fit, but the words stuck. Wipeng was glaring at me like a pissed-off dictator.

“…Shall we just finish talking about Jopil?”

“By all means.”

Wipeng nodded, satisfied.

*You crazy bastard.*

In the end, I had to tell him everything about the fight with Jopil, from beginning to end.

How Jopil had moved, what martial arts he’d used. Wipeng’s sharp questions had me tensing up more than once.

“You severed the tendons in Jopil’s legs with daggers?”

“Yes. I had them hidden in advance.”

“There’s no way Jopil failed to notice them… Continue.”

When the long story finally ended, Wipeng let out the breath he’d been holding. The mixed feelings in the way he looked at me came through loud and clear.

“Third Young Master. You have accomplished a truly great deed.”

“Ah, thank you…”

“I hate to admit it, but I mean it.”

“…Ah. Yes.”

“When I think of all the trouble you’ve caused until now, my blood boils, but I was genuinely impressed. I mean that.”

“…”

“Who could have imagined that the Third Young Master who stole family funds day after day and poured them into pleasure houses, then paraded through the streets dead drunk and smeared shit all over the family’s reputation, would become such a great man? I, Wipeng, am genuinely in awe.”

*Just curse me out, you bastard…*

I barely held back the stream of swearing trying to burst out and said,

“I got lucky. Jopil let his guard down too.”

Wipeng shook his head.

“No. It was all skill. Who let their guard down and who hid a dagger beforehand are not excuses. If that had been enough to kill Jopil, he would not have been Jopil, One Question, One Kill. Murim is a place where only the strong survive.”

“Only the strong survive.”

I quietly rolled the words over my tongue. They tasted bitter and sweet at the same time.

Murim—this game—had been that kind of place from the beginning. I had survived there, and I had gotten stronger.

“Jopil used every martial art he possessed to its fullest. In the end, he even pulled up his innate qi. A Peak master threw away his own life trying to kill you. But what was the result?”

“I won.”

“Yes. Exactly.”

“Then I was stronger than Jopil.”

Wipeng, who’d been looking sour this whole time, turned serious.

“What are you talking about? Jopil was stronger. Do Peak masters look like a joke to you?”

“…”

“You were only strong enough to kill Jopil in a surprise attack.”

*Enough already. Seriously.*

While I was debating whether to pull a weapon from my Inventory, Wipeng let out a short chuckle. It was the first time I had ever seen him laugh.

“Well done.”

I looked at Wipeng suspiciously.

“What are you going to tack on this time?”

His smile deepened.

“I mean it. It’s true I disliked you quite a lot, but… this time, I have no choice but to acknowledge you.”

When he put it like that, I had nothing to say. I got embarrassed for some reason and cleared my throat.

“Ahem. Well, I almost died, but all I did was take down Jopil and a few wandering martial artists. Ahem.”

“How many Peak masters do you think there are in a single city? Across all of Shanxi, where our family is located, there are fewer than twenty.”

Twenty. Far fewer than I’d expected.

“The Mount Heng Sword Sect must have taken serious losses. They lost three Peak masters like that.”

“But the greatest blow is something else.”

“What is it?”

“That is…”

The instant Wipeng opened his mouth, a trembling voice came from the doorway.

“The pretext. The pretext for starting this war is gone. The Third Young Master of the Jin Family of Taiyuan is strong enough without using poison. Indeed, that’s exactly right.”

The enormous Jin Wikyung stood there, teary-eyed, both arms spread wide.

“My baby brother!”

“…”

*Please, just leave me alone.*

* * *

In the end, I had to replay the chase of the past several days and my fight with Jopil all over again.

“The wandering martial artists who chased the survivors…”

“Those bastards! I’ll tear them apart!”

*Boom!*

“Jopil’s Flame Divine Palm caused internal injuries…”

“I’ll kill him! How dare that vicious wandering martial artist bastard! Even if I ripped out his guts and chewed them to a pulp, it wouldn’t be enough!”

*Boom! Boom! Boom!*

“…”

I stared blankly at the wreckage of my bedroom. Jin Wikyung had gotten way too into the story.

Wipeng had already backed far away and was mouthing something.

—It would be best not to bring that story up again.

For the first time, the two of us were in complete agreement.

Jin Wikyung huffed and puffed for a long while before he finally calmed dow—

“If that bastard had still been alive, he wouldn’t have died peacefully.”

*Crunch.*

I watched with sad eyes as the corner of the bed crumbled into powder. Wipeng shook his head.

“My lord. Please calm down. The Young Master seems anxious.”

That one actually worked. Seeing me sitting there sadly, wrapped in bandages from head to toe, Jin Wikyung’s eyes reddened.

“Just look at my baby brother. How much has this child suffered, to be sitting there so out of it?”

*Grab!*

A hand the size of a cauldron lid seized my shoulder and yanked me in. I was a fairly big guy myself, but this man was practically a small ogre. Crushed against his broad chest, I trembled in fear.

“There, little brother. It’s all right now. It’s all right.”

After a heartfelt hug that only he found moving, Jin Wikyung sniffed.

“I thought you’d be a child forever… but you’ve grown up now. Wipeng, did you know?”

Wipeng answered without even taking a breath.

“Yes. You don’t need to tell me.”

Of course, Jin Wikyung pretended not to hear him.

“Rumors have spread throughout our family and even through the streets. The tale of the hero who led a death squad in a raid on the enemy camp, defeated Jopil, One Question, One Kill, and one hundred wandering martial artists, and rescued the Sakju Branch’s household.”

“Wow. That’s amaz—wait, what?”

I blinked.

*Hold on. That was my story?*

“Um, I think there’s been some misunderstanding.”

“That’s right, my lord. There seems to have been some misunder—”

Jin Wikyung smiled, pleased.

“Our little brother is modest, too. Wipeng, you shut your mouth.”

“No, it isn’t modesty. I think the rumor has been distorted a little.”

“That’s right. I know you care for the Young Master, my lord, but this is going too far. If the rumor gets too far-fetched, people won’t beli—”

“Rumor? Far-fetched?”

*BOOM!*

Wipeng’s voice vanished under the thunderous crash. I stared with my mouth hanging open at the hole blown through my bedroom wall.

*What the hell are you doing, you lunatic?*

Jin Wikyung threw another punch. With a sound like compressed air bursting, what was left of the wall came down.

Wood and bricks rained from the two-story pavilion, and the people outside started shouting.

“It’s the Third Young Master! The Third Young Mas—his residence is collapsing!”

“Get people over here! Hurry!”

While everyone was still stuck in shock, Jin Wikyung hoisted me into the air.

*Put me down. Put me down, you crazy bastard!*

I struggled with all my strength, but there was no fighting him off. One step. One step. Every step toward the gaping wall sent terror through me.

*He’s going to drop me!*

More than fifty people had gathered below. It was two stories in name, but the pavilion was so huge the drop was a good ten meters. The wind coming through made me dizzy.

*If I fall, that’s a fracture at the very least.*

Even with a chill running down my spine, people kept packing in. More than fifty of them had their heads cranked back, looking up at us.

“Who is that? Wasn’t there an accident?”

“That’s the Lesser Family Head, isn’t it? Who’s he holding?”

“The Third Young Master. It’s the Third Young Master!”

Someone’s shout sent a stir through the crowd.

“The Third Young Master—no, the Third Young Master, sir?”

“The Third Young Master who defeated Jopil, One Question, One Kill, has awakened!”

*What is this situation?*

While my eyes and ears were still whipping around, a solemn voice rang out clearly.

“Can you see?”

“Ah, yes, I can see. Could you put me down—”

“Can you hear?”

“I can hear too, but first, could you—”

“What do you feel?”

“Embarrassment. And shame.”

“They believe in you. They’re calling your name!”

“No, you fucking bastard.”

That last curse vanished, swallowed by the crowd’s shouts.

“Third Young Master! Third Young Master!”

Dozens more had shown up in that brief interval. Countless eyes came flying at me and stuck.

*No, what is this?*

Then, with a solemn face, Jin Wikyung shoved his hands into my armpits and lifted me high.

Right on cue, a thunderous cheer erupted.

“Woooooo!”

“Third Young Master! Jin Taekyung!”

“Sleeping Dragon of Shanxi! Sleeping Dragon of Shanxi!”

And then…

*Fuck. What is this, a baby lion?*

An old cartoon’s BGM rang in my ears.

[^1]: In Korean, “crossing the River Jordan” is a euphemism for dying; Taekyung twists it into taking a half-bath.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 32`.

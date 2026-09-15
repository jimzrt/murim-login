# Master Edit Task — Chapter 66

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
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 암천     | **Dark Heaven**                  |
| 산서오문   | **Five Gates of Shanxi**         |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 은인     | **Benefactor**                               |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 칭호               | **Title**                      |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 공야청 | **Gong Yacheong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 소천 | **Socheon** |
| 소율 | **Soyul** |
| 삭주 | **Sakju** | Jin Family branch location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
| 주공 | register | Retainer-to-lord address; established rendering is “my lord,” not a dropped vocative. | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 60–64

## Plot

At Eight Spring Gorge, Taekyung and the reconnaissance squad surround the Head Elder, but his Finger-Flicking Technique kills numerous allied martial artists. Jin Wikyung arrives and joins the assault. Taekyung uses One Flash to destroy the Head Elder’s arm, while the elder cuts apart Wikyung’s ancestral sword and reveals that his betrayal grew from revenge for an old Great Faction War disaster.

The wounded Head Elder forms Sword Force for a final attack. Lee Cheonbaek ambushes him with a dagger, giving Taekyung the opening to finish him with One Flash. Lee dies from the effort. The System records the defeats of Lee Cheonbaek and Jin Baekyang, completes the Traitor Chain Quest, grants Taekyung multiple level-ups and increased Fame, and awards him the Sleeping Dragon of Shanxi title. The First Elder dies after warning Wipeng about Dark Heaven, and the surviving black-clad forces surrender.

Dark Heaven then appears on the cliff. Its agent kills Jin Chung and the Gunggwimun disciples who stayed behind, explaining that Dark Heaven rescued the conspirators from the Demonic Cult decades earlier and implanted gu in their heads. The agent deliberately spares Taekyung.

Five days later, rumors credit the Sleeping Dragon of Shanxi with the Jin Family’s victory. Mount Heng Sword Sect is collapsing after Lee Seogeun and Lee Cheonbaek’s deaths, and its First Young Master is killed by bandits. Jin Mukyung, the Heaven Shaking Sword and Taekyung’s lookalike second older brother, returns after three years at Heaven’s Gate Temple. Taekyung reaches Level 50, advances the Jin Family’s Cultivation Technique to the Eighth Stage, and gains 100 unassigned points.

Mukyung immediately tests Taekyung with the Reformation Fist and grappling techniques. Despite using no internal energy, Mukyung overwhelms him. Taekyung spends ten of his points on Agility, briefly reads Mukyung’s movements, and is struck again. Their spar remains unresolved.

## Continuity

- Jin Baekyang, the former Head Elder, is dead. Lee Cheonbaek died helping Taekyung defeat him.
- The Eight Spring Gorge battle is over; the black-clad conspirators surrendered after the Head Elder’s death.
- The First Elder is dead after naming Dark Heaven. The Second and Third Elders are dead. Wipeng and the surviving senior members’ subsequent fate is unresolved.
- Dark Heaven rescued the conspirators from the Demonic Cult, implanted gu in them, and is pursuing a larger plan. Its agents, purpose, and reason for sparing Taekyung remain unresolved.
- Jin Chung and the Gunggwimun disciples who stayed with him were killed by Dark Heaven.
- Taekyung is Level 50 with Fame 1,180, fifteen years of Internal Energy, and 90 unassigned points after spending 10 on Agility. His four Titles include Sleeping Dragon of Shanxi, Scion of a Prestigious Family, Novice Trainee, and Gambler.
- Sleeping Dragon of Shanxi is a Peak-grade Title granting All Stats +10 and Fame +100.
- Taekyung’s Jin Family’s Cultivation Technique is at the Eighth Stage, but his Internal Energy remains fifteen years because accumulation is slow.
- Jin Mukyung is twenty-three, the Heaven Shaking Sword, a Peak-level martial genius, and Taekyung’s second older brother. He studied at Heaven’s Gate Temple in Henan for three years and is far stronger than Taekyung.
- Taekyung’s spar with Mukyung remains unresolved.
- Mount Heng Sword Sect is near collapse; Lee Seogeun and Lee Cheonbaek are dead, and the First Young Master was killed by mounted bandits.

## Translation Decisions

- Preserve **Dark Heaven**, **Sleeping Dragon of Shanxi**, **Heaven Shaking Sword**, **Sword Force**, **One Flash**, **Reformation Fist**, **Peak**, **Eighth Stage**, **Qi Circulation**, and **Internal Energy**.
- Use **gu** in italics at first use with the established footnote explaining its venomous-creature origin.
- Retain **hyung** for Taekyung’s address to Mukyung.
- Render 금나수 as **grappling technique** rather than assigning an unsupported proper name.
- Keep **Captain of the Gatekeepers**, **Gunggwimun**, **Heaven’s Gate Temple**, and **Mount Heng Sword Sect** consistent with prior chapters.

### Prior accepted reading-copy tails

#### Chapter 64 tail (verified mastered)

…
the wall and landed on the ground. Jin Mukyung watched me and gave a quiet snort. “Well, well.” I didn’t like where this was going. I scratched the back of my head. “Weren’t we close?” “We were. My fist and your body.” “Ah.” I was insane to believe Jin Wikyung. The man doted on his younger brothers like his life depended on it. *Shit. He should’ve explained that properly.* Jin Mukyung held out his fist. “This is your oldest friend. Say hello.” “Hello.” Ominously, his smile widened. “Our youngest has grown a lot. Acting cocky in front of your big brother.” Whoooosh! Jin Mukyung charged like lightning and threw a punch. The air tore before his fist. *He’s serious?* The blow carried no internal energy, but the raw force behind it was immense. I jerked my head aside in alarm. Bang! The wooden wall exploded. Fists rained down through the splinters scattering in the air. Bababang! Face, chest, shoulder, stomach. The punches seemed wild and random, but his movements flowed smoothly, and the area they covered was as tightly woven as a net. “A fist technique?” “Been a while since you had a taste of the Reformation Fist, hasn’t it?” *Fuck, what kind of name is that for a fist technique?* As I cursed inwardly, a move from the Reformation Fist slammed into my abdomen. Whump! “Hup.” “It’s not over yet.” I fought through the breath-stealing pain and blocked the incoming punch with my forearm. The dull impact made my bones throb. “You blocked?” Babababam! It hurt. It hurt like hell. Jin Mukyung outclassed me in every way—strength, speed, everything. But how should I put it… *This is more manageable than I expected.* Was it because he wasn’t using internal energy? At first, all I could do was take a one-sided beating. But after a while, his attacks slowly began to come into focus. Whoosh! Jin Mukyung’s fist sliced through empty air. A precise read. A clean dodge. He looked at me in surprise. “You’ve improved quite a bit.” I steadied my breathing and grinned. Since things had come to this, I figured we might as well have a satisfying fight. “Not quite a bit. A lot. Haven’t you heard the rumors?” “I have. Until I’m sick of them.” Jin Mukyung gave a quiet laugh. “Then prove how much of them is true.” Shwaaak! With a sharp sound of air being split, his hand shot toward my wrist. *Like hell!* I widened my eyes and slapped the incoming hand away. Or tried to. Tap, tat-tat-tat! Five attacks and defenses passed between us in less than a second. Then the match was decided in an instant. Clamp! “What the hell is this pathetic grappling technique?” Jin Mukyung finally twisted my wrist into a lock with a strange movement, then spoke as though I were hopeless. Being caught so helplessly already had me seething, but his next words set my chest on fire. “Again.” “…What are you trying to do?” “I already knew the rumors were nonsense. Now I need to correct the habits of a little brother who doesn’t know his place.” Jin Mukyung released my wrist and crooked a finger. “Come at me. I won’t go easy on you this time.” I stared at him in silence. Jin Mukyung was unquestionably a master far beyond me. The wall of the Peak realm was too high for my current abilities to overcome. I knew that. I knew all of it. *This is pissing me off.* And suddenly, I was curious. How far could I go? Just how strong was Jin Mukyung, the genius whose reputation had spread so far? This was competitive pride—not as a Hunter, but as a martial artist of Murim. *Let’s do this.* Jin Mukyung was the first to notice the change in me. “I didn’t know you could make a face like that.” “This is my normal face.” He laughed as though he found it amusing. “Fine. That’s all well and good… but are you still talking so casually?” At that moment, Jin Mukyung’s fist blurred. Whoosh! Whump! My vision flashed. Even though I had been concentrating to the extreme, I hadn't managed to avoid the attack completely. Jin Mukyung looked from his fist to me and back again. “That shouldn’t have happened.” The punch had been aimed at my temple. If it had landed cleanly, that would have been the last blow. Even though he hadn't used internal energy, I had managed to partially evade a Peak master's full-powered One Strike. “See? I’ve improved a lot.” “I admit it. But you’re not even a quarter as good as the rumors claim.” “Don’t worry. I’ll catch up little by little from here on.” “You’ll catch up to me? How long do you think that’ll take?” I answered. “Starting this very moment.” “Hold out for a quarter of an hour. Then you’re my big brother.” Jin Mukyung's form blurred once again. But this time, I was a step faster. *Assign ten points to Agility.* Ten level-ups gained through the war. A hundred points lying dormant in my Status Window. Some of them answered my command. Shwaaaak! The change was instantaneous. At the same time, certainty filled me. I could perfectly evade Jin Mukyung’s fist as it flew toward my face. Whoosh! *Too slow.* Without hesitation, I turned my head. Whump! *…Damn it. I should’ve used ten more points.*

#### Chapter 65 tail (verified mastered)

…
of his five-year-old sister showing off such sinister vocabulary, Socheon’s face turned red. “Yul, you mustn’t say things like that!” “Big brother’s a whole heap too!” “You mean he’s in on it.” At this point, any chance of getting some rest had gone out the window. Suppressing a sigh, I sat up. “Urgh.” “Benefactor, are you all right? You haven’t recovered yet…” “It’s not that bad. I’m just bruised.” I had been beaten a little—or rather, quite a lot—but all that had happened was that my bones ached and my entire body was covered in bruises. Jin Mukyung must have held back because I was his only younger brother. I’d counted on that, which was why I’d acted so recklessly. “Oh, I see. That’s a relief.” “But how did you know? Have the rumors already spread?” “Everyone in the family knows.” Naturally. A two-story pavilion had collapsed early in the morning. Curious to hear what was being said, I asked, “So what are people saying?” *The Sleeping Dragon of Shanxi got beaten like a dog by the Heaven Shaking Sword. Turns out he was nothing but hype.* Surely rumors like that had spread everywhere. *I can already see it…* “Everyone is furious. What a treacherous scheme!” “Huh?” A treacherous scheme? What was he talking about? Had Jin Mukyung used poison without my knowing? Had I been poisoned? As I searched my memory in bewilderment, Socheon ground his teeth, his face full of rage. “If he had crossed my path, I would have torn him apart, even if it meant dying with him.” “Thanks for caring, but isn’t that a little excessive? Calm down. Seriously, calm down.” Jin Mukyung probably wouldn’t simply laugh that off if he heard it. But despite my attempts to stop him, Socheon’s anger did not subside. “How could I? The Lesser Family Head himself has proclaimed the man’s immediate execution.” “…” *What the hell? That’s terrifying.* *Was this the kind of place where the second son got the death penalty for hitting his youngest brother?* *Is this what Murim is like?* I asked in a trembling voice. “Did they kill him?” Socheon shook his head regretfully. “He escaped. The pursuit team should be tracking his trail by now.” “Are you kidding me?” They had even formed a pursuit team. I barely restrained the urge to split open Jin Wikyung’s and Socheon’s heads and inspect their brains. “Was all that really necessary?” “Pardon?” “I mean, the guy was a little rough with me, but he didn’t seem like such a bad person.” “He tried to harm you, Benefactor!” “That happens. I understand.” I had a younger sister too, so I knew how it was. Sometimes I wished Hayeon had been a younger brother. If she were some hulking bastard of a man, I could beat him half to death without worrying about social criticism or pangs of conscience. “Look. I’m barely hurt. Spit on it, give me a day or two of rest, and I’ll be completely fine.” Socheon’s eyes trembled violently. “Benefactor… You are truly a *junzi*.[^2] I, Socheon, am sincerely moved.” Thump. This was driving me crazy. I pressed a hand to my forehead as Socheon abruptly dropped into a full bow. “Enough. Go tell them to call off the pursuit. No—going myself would be faster. Where’s my eldest brother?” Socheon immediately answered. “He should be in the office with the Second Young Master.” “Huh?” “Pardon?” “No, what did you say?” “The Lesser Family Head is in the office with the Second Young Master.” My thoughts became tangled. I barely managed to speak. “Then who is the pursuit team chasing?” Socheon tilted his head. “The assassin, of course.” “An assassin?” “What assassin?” Another voice suddenly cut in. Hyuk Mujin had woken up and spoke in a tone that clearly meant *What kind of bullshit is this?* “What is he talking about?” I ignored Hyuk Mujin and gestured for Socheon to continue. “For now, we suspect he may be the Head Elder’s hidden disciple. His martial arts were so formidable that if the Second Young Master hadn’t happened to arrive, you would have suffered a grave calamity… Isn’t that right?” Hyuk Mujin’s mouth fell open at the unbelievable story. “Are you crazy? Do you want me to tell you why I ended up like this?” Just as the shrimp whose back had been broken in the fight between two whales was about to tell the truth, Socheon spoke up. “Ah, I left out Warrior Hyuk. I heard that you fought bravely against the assassin.” Hyuk Mujin’s ears perked up. “Me? Who said that?” “The Lesser Family Head. You distinguished yourself in battle this time, and you were badly injured while protecting the Benefactor. Everyone is envious, saying your reward will be enormous. They say you’re a shoo-in to become the next Master of the Gatekeeper Pavilion.” “T-The next Master of the Gatekeeper Pavilion!” “But what were you going to tell us?” “That…” Hyuk Mujin flinched for a moment, then continued in a resolute voice. “About the assassin.” “Ooooooh!” “He was strong. Even I, the next Master of the Gatekeeper Pavilion, fought him for a hundred-odd exchanges without settling the match…” What a bumper crop of bullshit. [^1]: *Gongcheong seokyu* is a rare martial-arts elixir; *seokyu* is also the Korean word for petroleum. [^2]: A *junzi* is the Confucian ideal of a morally upright and virtuous gentleman.

## Korean source

```text
＃66화



저벅저벅.

청년이 발걸음을 옮길 때마다 사람들이 분분히 물러섰다.

조각처럼 수려한 외모도 외모지만, 그에게서 흘러나오는 강렬한 분위기에 압도된 탓이었다.

그는 멀리서도 단연 눈에 띄는 존재였다.

“와아, 잘생겼다.”

작년에 들어온 시녀의 철없는 말에 늙은 하인이 피식 웃었다.

“꿈 깨라.”

“누가 뭐래요? 그냥 처음 보는 얼굴이니까 그렇지.”

“아까 못 봤어? 삼공자님 전각 무너졌을 때.”

“그 난리 통에 본 사람이 한둘인가. 그래도 저 남자는 전쟁 통에 봤어도 못 잊을 것 같은데, 헤헤.”

“하긴, 그때는 행색이 말이 아니었으니까.”

곰곰이 생각하던 시녀가 눈을 동그랗게 떴다.

“아, 설마?”

“그래. 바로 그 이공자님이시다. 그러니까 헛꿈 꾸지 말고 가서 일이나 해.”

진무경은 주위의 수군거림을 무심한 얼굴로 흘려보내며 걸음을 옮겼다.

고풍스러운 전각에 도착하자 입구를 지키던 무인들이 문을 열어 주었다. 경외 어린 시선은 덤이다.

“소가주님께서 기다리고 계십니다.”

“고맙네.”

소가주 집무실에 들어선 그를 반긴 것은 짙은 다향(茶香)과 쿵쿵, 커다란 소리를 내며 달려오는 형, 진위경이었다.

“아우야!”

활짝 벌린 두 팔이 진무경을 꽉 끌어안았다.

순간 피할까 생각도 해 봤지만 그랬다가는 저 덩치가 어린애처럼 칭얼대는 꼴을 봐야 한다.

“숨 막힙니다.”

목각 인형처럼 딱딱한 말투였다.

“그게 삼 년 만에 만난 형한테 할 말이냐?”

진무경이 단호하게 대답했다.

“삼십 년 만에 만나도 마찬가집니다.”

“차가워졌구나. 많이 변했어.”

“예, 저는 피도 눈물도 없는 냉혈한이니까요.”

“괜찮아. 난 체질상 몸에 열이 많아.”

“……놓으십시오.”

잠시 후, 마주 앉은 두 사람이 대화를 시작했다.

“위 대협이 안 보이는군요.”

소가주의 곁에 늘 그림자처럼 붙어 있어야 할 위팽의 모습이 보이지 않는다.

차를 한 모금 마신 진위경이 대답했다.

“추격대 맡겨서 보냈다. 삼문협(三問峽)까지 다녀오려면 보름은 걸리겠지.”

“그렇게 멀리 말입니까?”

가문이 위치한 태원이 산서의 중심이라면 삼문협은 초입이자 끝자락이나 마찬가지다. 섬서(陝西)와 하남(河南)으로 이어지는 길목이기도 했으니 보름이라는 시간도 빡빡했다.

“어차피 요식 행위인데 너무 고생시키는 거 아닙니까?”

“왜, 미안해서?”

“일이 이렇게 커질 줄 몰랐죠.”

“나도 몰랐다. 네가 오자마자 그런 사고를 칠 줄은.”

“그건!”

“무경아.”

지금까지와는 달리 가벼운 질책이 담긴 눈빛에 진무경이 한숨을 내쉬었다.

“그렇게까지 할 생각은 없었습니다. 처음에는 단순히 몇 수 겨뤄 보려고 했을 뿐이에요.”

“그런데?”

“제법이더군요. 열이 받아서 힘이 과해졌습니다.”

“그랬겠지. 네가 알던 막내가 아니었을 테니까.”

진무경이 떨떠름한 표정으로 고개를 끄덕였다.

불과 한두 시진 전에 직접 손을 섞어 보기까지 했으니 이젠 인정하지 않을 수 없었다.

“말이 나왔으니 말인데, 도대체 무슨 일이 있었던 겁니까?”

“막내?”

“전부 다. 제가 받은 서신에는 항산검문 놈들이 쳐들어온다고만 적혀 있었습니다.”

항산검문이 선전포고를 한 직후 전서응을 날렸으니 그로서는 자세한 내막을 알 방법이 없었다.

기껏해야 태원진가로 오는 도중에 들었던 소문이 전부다.

“대장로가 배신했다는 말, 사실입니까?”

“그래. 말하자면 길다.”

“어느 정도로요?”

“사십 년 전, 정마대전까지 거슬러 올라가지.”

진위경이 굳은 표정으로 입을 연 순간이었다.

“그럼 됐습니다.”

“당시 대장로가…… 뭐라고?”

“어차피 끝난 얘기, 제가 들어 봤자 뭐 하겠습니까.”

대수롭지 않게 찻물을 한입에 털어 넣는 동생의 모습에 진위경의 얼굴이 황당함으로 물들었다.

“야, 인마!”

명색이 가문의 비사(秘史) 아닌가. 평소에도 무공밖에 모르는 녀석이긴 했지만 이 정도일 줄은 몰랐다.

“넌 알아야지! 본가의 직계…….”

“대장로가 배신했다. 그리고 죽었다. 그 과정에서 항산검문도 박살 났다. 태원진가가 최종 승자다. 제가 이해한 게 틀립니까?”

“아니, 맞긴 한데…….”

이제는 누가 비정상인지 헷갈린다. 혼란스러워하던 그는 불현듯 한 가지 사실을 떠올렸다.

“네가 전부 말해 달라며!”

“아, 그거 취소하겠습니다. 태어나기도 전에 있었던 일까지 듣는다면 이 자리에서 늙어 죽을 테니까요. 그 시간에 검이나 한 번 더 휘두르는 게 낫습니다.”

“…….”

“그럼 갑니다.”

“간다고? 어딜?”

“당연히 수련이죠.”

“수, 수련? 지금?”

“오랜만에 위 대협하고 비무나 하려고 온 건데, 없으니 혼자서라도 해야 하지 않겠습니까.”

진위경은 말문이 막혔다. 저게 삼 년 만에 형을 만난 동생의 태도란 말인가. 배신감에 가슴이 미어졌다.

“무경아!”

절절한 음성에 진무경이 차갑게 대꾸했다.

“차 잘 마셨습니다.”

뒤도 돌아보지 않고 집무실을 떠나는 둘째 동생의 뒷모습에, 진위경은 충격에 휩싸였다.

‘내가 널 어떻게 키웠는데.’

둘째도, 막내도 너무 훌쩍 커 버렸다. 각기 훌륭하게 장성한 동생들이 기특하면서도 가끔은 이렇게 서운하다.

‘그래, 이게 순리겠지.’

진위경은 땅이 꺼져라 한숨을 내쉬고는 집무용 탁자 앞에 앉았다. 그리고 아까 찢긴 비운의 걸작, ‘영웅의 탄생’을 신중하게 이어 붙이기 시작했다.



* * *



“흔적을 찾을 수 없습니다.”

“목격자도, 족적도 남기지 않았습니다. 신출귀몰한 놈입니다.”

수하의 말에 위팽은 쓴웃음을 삼켰다. 살수는 애초부터 없었으니 발견될 흔적도 없는 게 당연하다.

‘팔자에도 없는 연기를 해야 한다니.’

위팽의 머릿속에 한 시진 전, 진위경과 나눴던 대화가 스쳤다.



‘살수라니. 일을 너무 키우신 것 아닙니까?’

‘기회가 왔으니 이용해야지.’

‘그 기회가 삼공자 전각을 더 화려하게 새로 지을 기회는 아니겠지요.’

‘오, 그거 좋네. 추진해 봐.’

‘주공!’

‘장난일세, 장난.’

‘그럼 도대체 어떤 기회를 말씀하시는 겁니까?’



주군의 얼굴에서 웃음기가 사라진 것도 그때였다.



‘본가가 산서성 전역을 아우를 기회.’

‘……!’

‘지난 닷새 동안 가문의 모든 기록을 뒤져 봤네. 찾아야 하는 이름이 있었거든. 그게 무엇인지는 자네도 알겠지.’

‘암천(暗天).’

‘그 결과가 궁금하지 않나?’

‘못 찾으셨군요.’

‘구름이 몰려오고 있네. 지금까지 모습을 드러낸 적 없는 구름이. 그 전에 대비해야 해.’

‘하명하십시오.’

‘정예 서른을 붙여 줄 테니 곧장 남하하게. 공식적인 목표는 살수의 생포, 혹은 처단이지만 진짜 임무는 따로 있네.’



위팽은 저도 모르게 가슴을 더듬었다. 진위경에게 건네받았던 두툼한 종이 뭉치가 만져졌다.



‘이것은?’

‘곧 다가오는 새해 원단(元旦)에 산서성의 모든 문파를 본가로 소집할 생각이네.’



초청도, 초대도 아니다. 소집이다.

위팽은 그 뜻을 모를 정도로 멍청하지 않았다.



‘맹주(盟主)가 되려 하십니까?’

‘필요하다면.’



불과 얼마 전까지 세인들의 눈에 비친 산서 무림은 태원진가와 항산검문이라는 양대 산맥으로 나뉘어 있었다.

그러나 실상은 달랐다. 산서 무림은 세 발 달린 솥과 같은 형국이었다.

‘태원진가, 항산검문. 그리고 중소 문파.’

태원진가는 중부, 항산검문은 북부. 그리고 남부는 이십여 개 중소 문파들의 영역이었다. 이번 전쟁으로 사라진 산서오문은 그중에서도 특히 강성했던 다섯 개 문파를 칭하는 이름이었을 뿐이다.



‘그들의 연대는 끈끈합니다. 응하지 않을 수도 있습니다.’

‘전쟁이 일어나기 전이었다면 그랬겠지.’



세 발 달린 솥이 기울기 시작했다. 그리고 태원진가는 산서 무림이라는 솥을 홀로 지탱할 만한 힘과 명분이 있었다.



‘할 수 있겠나?’



대답은 정해져 있었다. 위팽은 작은 목소리로 중얼거렸다.

“받들겠습니다.”



그 시각, 진위경은 ‘영웅의 탄생’을 이어 붙이며 위팽을 욕하고 있었다.



* * *



상태창



[Lv.50 진태경]

직업 : 일류 무인

명성 : 1180 (+150)

칭호 : 4개 (칭호 효과 적용 중)

- 산서잠룡 (모든 능력치 +10, 명성 +100)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 초보 수련자 (수련 속도 +10%)

- 승부사 (일대일 전투 시 전투 관련 능력치 +10%)

근력 : 135 (+15)체력 : 142(+15)

민첩 : 180 (+15)지력 : 25(+15)

매력 : 25(+15)공력 : 15년

잔여 포인트 : 50

- 잔여 포인트를 분배하십시오.





나는 상태창을 보며 후회했다.

‘젠장. 포인트를 너무 많이 썼어.’

진무경을 상대하면서 자그마치 50포인트나 민첩에 꼴아박았다. 애써 유지해 온 능력치 균형이 무너졌으니 나로서는 속이 쓰릴 수밖에 없다.

‘기껏해야 2, 30포인트면 충분할 거라고 생각했는데.’

절정 고수의 벽은 높았다. 아니, 어쩌면 진무경이 생각 이상으로 강한 것인지도 모르겠다. 천재라는 꼬리표가 쉽게 붙는 게 아니니까.

“내가 오십 합을 버티자 살수도 낭패한 기색이 역력하더군. 얼마 전까지 수련에만 매진한 나는 아직 산서에 알려지지 않은 미지의 고수…….”

빡!

“컥!”

뒤통수를 얻어맞은 혁무진이 비명을 질렀다.

“뭡니까!”

“애들한테 헛소리 좀 그만해. 뒤지기 싫으면.”

하지만 소천은 반짝거리는 눈으로 뒷이야기를 기다리는 중이었다.

“전 괜찮습니다.”

“뒤지는 게 모야? 소율이도 뒤질래!”

“……넌 아직 한참 남았어.”

나는 소매를 잡아당기며 보채는 소율의 머리를 쓰다듬었다.

이 꼬마 남매와의 인연도 제법 깊다. 가만히 보고 있으니 문득 생각나는 사람이 있었다.

“공 대협은 요즘 어떠시냐?”

공야청. 소천과 소율이 숙부라고 부르는 중년인.

여전히 무림의 용어가 어색한 나도 공야청을 부를 때는 꼬박꼬박 대협을 붙인다. 그는 그럴 만한 자격이 있는 사람이니까.

“순조롭게 회복 중이십니다. 아직 거동이 불편하시긴 하지만요.”

“그래? 다행이네.”

“안 그래도 떠나기 전에 한번 뵈었으면 하시더군요.”

무심코 고개를 끄덕이려다가 멈칫했다.

“떠난다고?”

“예, 이번에 재건되는 삭주지부를 맡게 되실 겁니다.”

“그럼…….”

“저희도 따라가기로 했습니다.”

전쟁은 많은 것들을 앗아 간다. 소천과 소율은 항산검문의 습격으로 터전과 부모를 모두 잃었다. 지나간 시간을 되돌릴 수는 없겠지만 모든 것이 정리되었으니 이젠 소중한 추억이 서린 곳으로 돌아갈 것이다.

“감사했습니다, 은인.”

진심이 느껴지는 인사에 가슴 한구석이 간질거렸다. 어린 남매가 감당하기에는 너무 잔인한 현실이 아직 남아 있었다.

더군다나 소율은 아직 부모의 죽음조차 모른다.

‘다섯 살이라…….’

현재를 인지하고 받아들이기에는 너무나도 어린 나이다.

문득 22년 전의 기억을 떠올려 봤다. 흐릿하다.

“……너도 그랬으면 좋겠구나.”

소율이는 뜻을 모를 말에도 배시시 웃었다.

나는 소천을 향해 고개를 돌렸다.

“종종 보러 가도 되냐?”

내 말에 소천이 기다렸다는 듯 환하게 웃었다.

“은인이라면 언제나 환영입니다.”

우리 사이에 훈훈하게 흐르는 공기를 뚫고 가만히 듣고 있던 혁무진이 끼어들었다.

“그럼 언제쯤 떠나는 거야?”

“반년 후요.”

“…….”

내 감동. 아껴 둘걸.
```

## Current accepted English baseline

```markdown
# Chapter 66

Step. Step.

Each time the young man took a step, people hurriedly moved aside.

His sculpted, handsome features were part of it, but more than that, they were overwhelmed by the intense presence radiating from him.

He stood out even from a distance.

“Wow, he’s handsome.”

At the thoughtless remark from a maid who had joined the household the previous year, an old servant gave a quiet laugh.

“Wake up from your dream.”

“Who said anything? It’s just because I’ve never seen his face before.”

“Didn’t you see him earlier? When the Third Young Master’s pavilion collapsed?”

“With all that chaos, do you think I only saw one or two people? Still, I don’t think I’d ever forget that man, even if I’d seen him in the middle of a war. Hehe.”

“True enough. His appearance was a complete disaster back then.”

The maid thought about it for a moment, then her eyes went round.

“Oh, no way?”

“That’s right. He’s the Second Young Master. So stop dreaming nonsense and go do your work.”

Jin Mukyung ignored the whispers around him with an indifferent expression and continued walking.

When he reached the stately, traditional pavilion, the martial artists guarding the entrance opened the doors for him. The looks of awe came free of charge.

“The Lesser Family Head is waiting for you.”

“Thank you.”

The moment Jin Mukyung entered the Lesser Family Head’s office, he was greeted by the rich scent of tea—and by his older brother, Jin Wikyung, charging toward him with heavy, pounding footsteps.

“Little brother!”

Jin Wikyung spread his arms wide and pulled Jin Mukyung into a tight embrace.

For a moment, Mukyung considered dodging, but if he did, he would have to watch that hulking body whine like a child.

“I can’t breathe.”

His tone was as stiff as a wooden puppet’s.

“Is that what you say to your brother after not seeing him for three years?”

“Even if we had not seen each other for thirty years, my answer would be the same.”

“You’ve grown cold. You’ve changed so much.”

“Yes. I’m a cold-blooded man without blood or tears.”

“That’s all right. I naturally run hot.”

“……Let go.”

A short while later, the two brothers sat across from each other and began to talk.

“Sir Wipeng is nowhere to be seen.”

Wipeng, who was supposed to remain at the Lesser Family Head’s side like a shadow, was absent.

After taking a sip of tea, Jin Wikyung answered.

“I put him in charge of a pursuit team and sent him out. It’ll take at least half a month to go all the way to Three Questions Gorge and back.”

“That far?”

If Taiyuan, where the family was located, was the center of Shanxi, Three Questions Gorge was practically at its entrance and far edge. It was also a crossroads leading to Shaanxi and Henan, so even fifteen days was a tight schedule.

“It’s only a formality anyway. Aren’t you making him work too hard?”

“Why? Feeling sorry for him?”

“I didn’t expect things to get this big.”

“Neither did I. I didn’t expect you to cause such an incident the moment you arrived.”

“That’s not—”

“Mukyung.”

Unlike before, Jin Wikyung’s eyes held a light reproach. Jin Mukyung sighed.

“I didn’t intend to take it that far. At first, I only meant to exchange a few moves.”

“And then?”

“He was pretty good. I got heated and used too much force.”

“Of course you did. He wasn’t the youngest brother you remembered.”

Jin Mukyung nodded reluctantly.

He had personally exchanged blows with Jin Taekyung only an hour or two earlier. By now, he could no longer refuse to acknowledge the truth.

“Since we’re on the subject, what on earth happened?”

“The youngest?”

“Everything. The letter I received only said that the Mount Heng Sword Sect bastards were invading.”

A carrier hawk had been sent immediately after the Mount Heng Sword Sect declared war, so there had been no way for him to learn the details.

The rumors he had heard on the way to the Jin Family of Taiyuan were all he knew.

“Is it true that the Head Elder betrayed us?”

“Yes. It’s a long story.”

“How long?”

“It goes all the way back to the Great Faction War forty years ago.”

Jin Wikyung’s expression hardened as he began to speak.

“Then never mind.”

“Back then, the Head Elder… Wait, what did you say?”

“Never mind. It’s already over. What good would hearing about it do me?”

Jin Mukyung emptied his teacup in one gulp, and Jin Wikyung’s face filled with disbelief.

“You little bastard!”

It was, after all, the hidden history of the family. Jin Mukyung had always been a man who cared about nothing but martial arts, but Jin Wikyung had never imagined he could be this bad.

“You need to know! The direct line of our family—”

“The Head Elder betrayed us. Then he died. The Mount Heng Sword Sect was destroyed in the process. The Jin Family of Taiyuan was the final victor. Did I misunderstand anything?”

“No, that’s right, but…”

Jin Wikyung began to wonder which of them was the abnormal one.

Then he suddenly remembered something.

“You were the one who said you wanted to hear everything!”

“Ah, I take that back. If I listen to things that happened before I was even born, I’ll grow old and die right here. I’d rather spend that time swinging my sword one more time.”

“……”

“Then I’ll be going.”

“You’re leaving? Where?”

“To train, obviously.”

“Training? Right now?”

“I came to spar with Sir Wipeng after so long, but he’s gone. Shouldn’t I train by myself, at least?”

Jin Wikyung was speechless.

*Is that how a younger brother is supposed to act after seeing his older brother for the first time in three years?*

His heart ached with betrayal.

“Mukyung!”

Jin Mukyung answered the heartfelt call coldly.

“The tea was good. Thank you.”

He left the office without even looking back.

Jin Wikyung stared at the back of his departing younger brother, stunned.

*After everything I did to raise you…*

Both his second and youngest brothers had grown up so much. He was proud of how wonderfully they had each matured, but sometimes, moments like this still hurt.

*Yes. This is the natural order of things.*

Jin Wikyung let out a sigh that seemed to drain the earth itself, then sat down in front of his worktable.

He carefully began piecing together the unfortunate masterpiece that had been torn apart earlier: *The Birth of a Hero*.

* * *

“We haven’t found a single trace.”

“He left behind no witnesses or footprints. He’s an elusive bastard.”

At his subordinate’s report, Wipeng swallowed a bitter smile.

There had never been an assassin in the first place. Naturally, there would be no traces to find.

*I have to put on an act I was never meant to perform.*

A conversation he had shared with Jin Wikyung an hour earlier flashed through Wipeng’s mind.

*An assassin? Haven’t you made this affair too big?*

*An opportunity has presented itself. We have to use it.*

*You don’t mean the opportunity to rebuild the Third Young Master’s pavilion even more lavishly, do you?*

*Oh, that’s a good idea. Make it happen.*

*My lord!*

*I’m joking. Just joking.*

*Then what opportunity are you talking about?*

That was when the smile disappeared from his lord’s face.

*An opportunity for our family to encompass all of Shanxi Province.*

*……!*

*I spent the past five days searching through every record in the family. There was a name I needed to find. You know what it is, don’t you?*

*Dark Heaven.*

*Don’t you want to know what I found?*

*You didn’t find it.*

*Clouds are gathering. Clouds that have never shown themselves before. We need to prepare before they appear.*

*Give me your orders.*

*I’ll assign thirty elites to you. Head south immediately. The official objective is to capture or kill the assassin, but your true mission is something else.*

Wipeng unconsciously touched his chest. His fingers brushed against the thick bundle of papers Jin Wikyung had handed him.

*What is this?*

*On the coming New Year’s Day, I intend to summon every sect in Shanxi Province to our family.*

This was no invitation. It was a summons.

Wipeng was not foolish enough to misunderstand what that meant.

*Are you trying to become the Alliance Leader?*

*If necessary.*

Until recently, Shanxi Murim had appeared to the outside world as two towering peaks: the Jin Family of Taiyuan and the Mount Heng Sword Sect.

But the reality was different. Shanxi Murim was shaped like a three-legged cauldron.

*The Jin Family of Taiyuan, the Mount Heng Sword Sect, and the smaller sects.*

The Jin Family of Taiyuan held the central region, and the Mount Heng Sword Sect held the north. The south belonged to more than twenty mid-sized and small sects.

The Five Gates of Shanxi, which had vanished in the recent war, was merely the name given to the five especially powerful sects among them.

*Their alliance is strong. They may refuse to comply.*

*They might have, if this had been before the war.*

The three-legged cauldron had begun to tip.

And the Jin Family of Taiyuan had both the strength and the justification to support Shanxi Murim’s cauldron alone.

*Can you do it?*

The answer had already been decided.

Wipeng muttered in a low voice.

“I shall obey.”

At that same moment, Jin Wikyung was piecing together *The Birth of a Hero* and cursing Wipeng.

* * *

> **System**
>
> **Status Window**
>
> **Lv.50 Jin Taekyung**
>
> **Job:** First Rate martial artist
>
> **Fame:** 1,180 (+150)
>
> **Titles:** 4 (Title effects active)
>
> - **Sleeping Dragon of Shanxi** (All Stats +10, Fame +100)
>
> - **Scion of a Prestigious Family** (All Stats +5, Fame +50)
>
> - **Novice Trainee** (Training speed +10%)
>
> - **Gambler** (Combat-related stats +10% in one-on-one combat)
>
> **Strength:** 135 (+15)  
> **Stamina:** 142 (+15)  
> **Agility:** 180 (+15)  
> **Intelligence:** 25 (+15)  
> **Charm:** 25 (+15)  
> **Internal Energy:** 15 years
>
> **Remaining Points:** 50
>
> - Distribute your remaining points.

I stared at the Status Window and regretted it.

*Damn it. I spent too many points.*

While fighting Jin Mukyung, I had dumped no fewer than fifty points into Agility. The balance between my stats, which I had worked so hard to maintain, had collapsed. Naturally, it left a bitter taste in my mouth.

*I thought twenty or thirty points at most would be enough.*

The wall posed by a Peak master was high.

No—perhaps Jin Mukyung was simply stronger than I had expected. The title of genius was not something people handed out easily.

“When I lasted fifty exchanges, even the assassin looked visibly flustered. I had devoted myself to training until recently, so I was an unknown master in Shanxi—”

Smack!

“Ghk!”

Hyuk Mujin, who had been struck on the back of the head, let out a scream.

“What was that for?”

“Stop filling the kids’ heads with nonsense. Unless you want to croak.”

But Socheon was waiting for the rest of the story with shining eyes.

“I’m fine.”

“What does ‘croak’ mean? Soyul wants to croak too!”

“……You’ve still got a long time before that.”

I stroked Soyul’s head as she tugged on my sleeve and pestered me.

My connection with these little siblings had grown fairly deep. As I watched them quietly, someone suddenly came to mind.

“How is Great Hero Gong these days?”

Gong Yacheong—the middle-aged man Socheon and Soyul called their uncle.

Even now, Murim terminology felt awkward to me, but whenever I addressed Gong Yacheong, I always called him Great Hero. He was someone who deserved it.

“He’s recovering smoothly. He still has trouble moving around, though.”

“Really? That’s good to hear.”

“He said he wanted to see you before he left.”

I was about to nod without thinking when I stopped.

“Before he leaves?”

“Yes. He’ll be put in charge of the Sakju Branch, which is being rebuilt this time.”

“Then…”

“We’ve decided to go with him.”

War took many things away.

Socheon and Soyul had lost both their home and their parents in the Mount Heng Sword Sect’s attack. They could not turn back the years that had passed, but now that everything had been settled, they would return to the place steeped in precious memories.

“Thank you for everything, Benefactor.”

The sincerity in his farewell made something tickle in a corner of my chest. There was still a reality far too cruel for these young siblings to bear.

What was worse, Soyul did not even know that her parents were dead.

*She’s five…*

She was far too young to recognize and accept the present for what it was.

I suddenly recalled a memory from twenty-two years ago.

It was hazy.

“……I hope it will be that way for you, too.”

Soyul only smiled shyly at the words she did not understand.

I turned toward Socheon.

“Would it be all right if I came to see you from time to time?”

Socheon beamed as if he had been waiting for me to ask.

“You’re always welcome, Benefactor.”

Hyuk Mujin, who had been listening quietly, broke through the warm atmosphere between us.

“Then when are you leaving?”

“Half a year from now.”

“……”

*There went my touching moment. I should’ve saved it.*
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 66`.

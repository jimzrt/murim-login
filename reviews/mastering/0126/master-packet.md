# Master Edit Task — Chapter 126

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
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마교     | **Demonic Cult**                                 |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 삭주 | **Sakju** | Jin Family branch location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 평화 | **Peace Guild** | Guild name. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 폭혈단 | **Blood-Exploding Pill** | Demonic Cult pill said to kill the user after its time limit. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 산서제일인 | **Shanxi's Number One** | Jin Wikyung's reputation for physical strength. |
| 금잔디 | **Geum Jandi** | Heroine of Boys Over Flowers, referenced in a sarcastic comparison. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 소음인 | **Soeumin** | One of the constitutional types in Sasang medicine. |
| 태양인 | **Taeyangin** | One of the constitutional types in Sasang medicine. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 하오문도 | 진위경 | informant_to_lesser_family_head | Lesser Family Head | deferential | Uses 소가주님 while correcting Wikyung's misunderstanding about Mukyung's condition. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 위팽 | 진태경 | retainer_to_third_young_master | Third Young Master | formal-polite and admonishing | Uses 삼공자 while warning Taekyung to return by noon and behave respectfully toward Jang Taebo. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 120–124

## Plot

Jin Taekyung kills Pung Yang with the Unnamed Sword after its Ten-Thousand-Year Cold Iron destroys Pung Yang’s Body-Protecting Qi. The victory completes the Temporary Strength Pill Quest, restoring Taekyung’s health and granting five level-ups, substantial EXP and Fame, and medicines that save many wounded Mount Heng Sword Sect survivors. Taekyung also fully absorbs the Blazing Flame Divine Pill, reaching forty-five years of internal energy with the Scorching Yang Qi attribute.

The Mount Heng Sword Sect is devastated, but Lee Seowol remains Sect Leader and vows to rebuild it. She accepts Jin Wikyung’s invitation to the Jin Family of Taiyuan’s New Year gathering and offers the Jin Family the sect’s territorial rights as an apology. She also offers the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist in exchange for marrying Taekyung. Taekyung initially rejects the proposal because Seowol is seventeen and because he loves Song Song, while Jin Mukyung insists that the three Peak martial arts make the marriage worthwhile.

Taekyung reveals that Jopil left behind the Flame Divine Palm, a Supreme Peak secret art of the Fire Gate Clan restricted to practitioners with Scorching Yang Qi. Mukyung warns that possessing another sect’s secret technique could make the Jin Family thieves in the eyes of the Murim. The art belonged to the Fire King, one of the world’s twenty greatest experts, whose survival after a legendary battle at Mount Jiuhua remains unknown. Mukyung returns to the Jin Family while still recovering, accompanied by Hyuk Mujin. Wolhwa departs to tour northern Shanxi and promises to maintain close ties with the Jin Family. After the carriage leaves, Lee Seowol appears and addresses Taekyung as Benefactor.

## Continuity

- Pung Yang is dead, and the Red Wind Band’s remaining forces and wider response to his death remain unresolved.
- Taekyung has fully absorbed the Blazing Flame Divine Pill and possesses forty-five years of internal energy with the Scorching Yang Qi attribute.
- The Temporary Strength Pill Quest granted Taekyung five level-ups, major EXP and Fame, and Full Recovery; the pill’s origin and long-term effects remain unknown.
- Jin Mukyung survived his Internal Injuries and can travel, but he is not fully recovered.
- Cheol Mubaek has broken limbs and serious Internal Injuries and requires at least four months of recuperation.
- Twenty-five Mount Heng survivors remain, including Lee Seowol; five were initially unlikely to survive. The sect’s reconstruction remains uncertain.
- Lee Seowol is seventeen, remains Sect Leader, accepted the New Year invitation, and has proposed marriage to Taekyung in exchange for three Peak martial arts.
- Taekyung intends to reject Seowol’s political marriage because he loves Song Song, but the proposal and territorial transaction have not been resolved.
- Cheol Mubaek gave Lee Seowol the Shura Annihilating Fist manual despite its single-successor, transmission-only-to-the-worthy tradition.
- Taekyung possesses Jopil’s Flame Divine Palm manual. Jopil claimed to be its nineteenth-generation successor, but how he obtained it and whether the claim is true remain uncertain.
- The Flame Divine Palm is a Fire Gate Clan secret art restricted to owners of Scorching Yang Qi. The Fire Gate Clan follows a single-successor tradition.
- The Fire King, the art’s legendary master, may still be alive.
- Wolhwa is Eun Sowol, the Lower District Sect’s Shanxi Branch Leader, and plans to tour northern Shanxi while preserving the alliance with the Jin Family.

## Translation Decisions

- Retain **Peak**, **Supreme Peak**, **Internal Injury**, **Severe Injury**, **Body-Protecting Qi**, **Scorching Yang Qi**, **Red Wind Band**, **Sect Leader**, **Benefactor**, and **Taiyuan Jin Family**.
- Render **잠력단** as **Temporary Strength Pill**, **열화신단** as **Blazing Flame Divine Pill**, **완전 회복** as **Full Recovery**, **만년한철** as **Ten-Thousand-Year Cold Iron**, and **이름 없는 검** as **Unnamed Sword**.
- Render **혈랑검법** as **Blood Wolf Sword Technique**, **혈랑보법** as **Blood Wolf Footwork**, **절정 무공** as **Peak martial arts**, **파천신권** as **Shura Annihilating Fist**, and **열화문** as **Fire Gate Clan**.
- Render **화왕** as **Fire King**, **구화산** as **Mount Jiuhua**, **진무보법** as **Jin Family’s Manoeuvre Technique**, **일인전승** as **single successor**, and **비인부전** as **transmission only to the worthy**.
- Preserve the Samsung/Samseong pun with a clarifying footnote; retain **Jaringobi** with its explanatory footnote.

### Prior accepted reading-copy tails

#### Chapter 124 tail (verified mastered)

…
“Let’s give it back.” I wanted to live a long life. I didn’t want an event involving some insane old man who had single-handedly killed a thousand people added to my life. “We should leave right away. Anhui Province? Do people still say he lives there?” “No one knows. Perhaps that still hadn’t been enough to quell the Fire King’s anger. He spent an entire year crushing every Demonic Cult member he could find before disappearing into seclusion again.” “The Fire Gate Clan! We can find him if we go to the Fire Gate Clan.” “The Fire Gate Clan has only one successor at a time. It’s similar to Great Hero Cheol’s situation.” “…” So even if I wanted to return it, there was no one to give it to. Jopil had probably been the person closest to the Fire King, but he was already dead. I had no way to find the man. *The best-case scenario is that the Fire King is already dead…* He had already been an old man forty years ago, so it was entirely possible. On the other hand, as a Supreme Peak master, he might have lived an extraordinarily long life. “Hmm.” Was this a priceless treasure or a useless burden? As I stared at the Flame Divine Palm with a conflicted expression, Jin Mukyung said, “If the Fire King is dead… then you’re the master of the Fire Gate Clan now.” * * * Jin Mukyung recovered quickly. He had suffered considerable internal injuries from Pung Yang, so a full recovery would still take some time, but he had enough strength to return to the Jin Family of Taiyuan. “We’re finally going home.” Hyuk Mujin muttered with a deeply moved expression. “They say leaving home means hardship. From now on, I will never, ever leave the family grounds again!” “…Anyone listening would think you suffered the most, you punk.” “What are you talking about? I have my own hardships, you know.” “Try saying that to the person behind you.” Jin Mukyung, who still hadn’t been able to remove his bandages, came flying over and smacked Hyuk Mujin on the back of the head. *Whack!* “Urk!” “Enough nonsense. Drive the carriage.” “There’s a coachman. Why do I have to…?” Just as Hyuk Mujin said, we had a separate coachman—a member of the Lower District Sect whom Wolhwa had assigned to us. Wolhwa had come out ahead of time to see us off. “Goodbye. It’s a shame to part now that the time has come, isn’t it?” “Then would you like to come with us now?” I spoke jokingly to her as she winked at me. I was still wary of her, but after our journey together, we had become close enough to exchange jokes. “Oh my, I’d love to, but… I’m planning to take this opportunity to tour all of northern Shanxi.” Northern Shanxi, which the Mount Heng Sword Sect had kept under tight control until now, had become an open market. Naturally, Wolhwa—the Lower District Sect’s Chief Branch Leader for Shanxi Province—would be busy. “Things must have gone well with the Mount Heng Sword Sect?” “Secret. I may be the Chief Branch Leader, but I can’t go around telling outsiders our sect’s confidential information.” Her words said one thing, but her bright, carefree smile was answer enough. She was the sort of woman who could have nine tails and no one would find it strange, so she had probably obtained a more than satisfactory result. “I suppose we’ll meet at the Jin Family of Taiyuan next time.” “Oh, really?” “We were allies once. Wouldn’t it be better for both of us if we continued to maintain a close relationship?” Wolhwa smiled coyly and lifted the hem of her skirt slightly. “Make sure you come see me again then. Well, I’ll be off.” As soon as she climbed into the waiting carriage, the coachman cracked his whip. Two pairs of eyes gazed blankly after the carriage as it rapidly receded into the distance. “Tsk. She could’ve stayed a little longer.” “Hmm. Mmm…” Hyuk Mujin was one thing, but what was Jin Mukyung’s deal? As I watched the wistful look in his eyes, a thought suddenly occurred to me. *Could that bastard possibly…?* Was he interested in Wolhwa? Good heavens. I couldn’t believe it. The man who knew nothing but martial arts was showing an interest in a woman. I couldn’t keep this earth-shattering news to myself. I moved close to Hyuk Mujin and whispered in a voice as small as an ant. “Hey, Mujin.” “Ah! You startled me. What is it?” “Shh. Listen, but don’t be surprised. Don’t show even the slightest reaction. This is a secret we have to take to our graves.” Hyuk Mujin answered in a stiff voice. “Gasp. Yes. Go ahead.” “I think that guy… is interested in Young Lady Wolhwa.” “…” “Don’t tell anyone. This is a secret only I know, and I’m telling you alone.” Despite my serious whisper, Hyuk Mujin replied with a sour expression. “Oh, yes. Thank you. I’m so grateful I don’t know what to do with myself.” *Why, this little shit…* I was wondering how to correct that rude tone when— “Benefactor.” I slowly turned around. Lee Seowol stood there in a snow-white palace robe. [^1]: The Korean name “Samsung” is pronounced *Samseong*, the same as the Korean term rendered here as “Three Saints.”

#### Chapter 125 tail (verified mastered)

…
that the wounds were beginning to close. *Because everyone who caused them is dead.* The Head Elder and Lee Cheonbaek, each of whom had dreamed of revenge, had already met their ends. Wasn’t that why we had raced here day and night to save the Mount Heng Sword Sect? With a sincere apology and forgiveness… wounds could heal, even if the scars remained. Just as they were now. “I won’t accept your apology.” The words came out only after considerable thought. Without waiting for anyone else to react, I continued. “I’m not someone with the right to receive your apology or forgive you.” No one here had that right. The people they needed to apologize to were back at the Jin Family of Taiyuan. Lee Seowol and Cheol Mubaek seemed to understand. Both nodded. “I’ll see you on New Year’s Day.” “Taiyuan, is it? It will be my first journey away from home in thirty years.” The Mount Heng Sword Sect would hardly be a welcome guest. Especially now, diminished to such a pitiful state, they might have to endure all manner of humiliation and disgrace. But that was something they would have to bear themselves. There was nothing I could do, nor any reason for me to interfere. *Well done.* With Jin Mukyung’s brief Sound Transmission in my ear, I offered one last farewell. “Then we’ll be going.” I had just turned toward the carriage when Lee Seowol called out. “Benefactor.” “Yes?” “Did you know there are fewer than fifteen days left until New Year’s Day?” Her voice babbled on like a little stream. “I’m looking forward to hearing the answer I didn’t get last time.” I could only open and close my mouth in confusion as Jin Mukyung grabbed me and dragged me away. With Cheol Mubaek’s distinctly displeased cough sounding behind us, the carriage set off at full speed. * * * The journey back to the Jin Family of Taiyuan was quick and smooth. The coachman’s skill played a part, but with the impatience gone from my heart, everything seemed that way. “Phew.” Jin Mukyung had just finished circulating his qi when he suddenly muttered, “Now that I think about it, I didn’t even get to see a Peak martial art.” He had joined us after Jin Wikyung lured him in with the promise that he could see Peak martial arts at Mount Heng. I answered him calmly. “It’s fine. Thanks to Pung Yang, you got to see Mount Beimang.” “You call that consolation?” “No. I was making fun of you.” Bones cracked in Jin Mukyung’s hand. “You’ve grown a lot.” “Want to spar once your injuries are fully healed?” “I could do it right now… Urgh.” Jin Mukyung tried to spring to his feet, then immediately frowned. No matter how quickly he recovered, it had only been four days. That was nowhere near enough time for his injuries to heal completely. He collapsed back into his seat and glared at me. “Consider yourself lucky.” “I don’t know about lucky, but my lifeline sure is damn thick.” Considering how I kept surviving every brush with death, I must have been born with an unusually sturdy lifeline. Either that, or I had been blessed with heaven’s fortune. “Anyway, you did well.” “Huh?” “Eeeh?” Hyuk Mujin and I both widened our eyes at the unexpected praise sticker. Jin Mukyung looked at us as if he couldn’t understand what was wrong. “Why are you looking at me like that? You look as if you’ve heard something you weren’t supposed to.” “You’re practically a ghost.” “Wait, could Pung Yang have already killed you? Are you sitting here as a vengeful spirit?” It was a fairly plausible theory, but around Jin Mukyung, you had to watch your mouth at all times. As I watched Hyuk Mujin get beaten until dust flew, I felt around inside my robes. *Inventory open. Summon.* The next moment, my fingertips touched something round and hard. It was the only thing Pung Yang had left behind. No—the only thing I had taken from him. *Check Item.* *Ding.* > **System** > > **Item Window** > > **Temporary Strength Pill** > > **Type:** Elixir > **Grade:** ??? > **Restriction:** Peak martial artist or higher > **Description:** A pill manufactured by an unknown person. It greatly raises the user’s latent power for about one shichen, but a price must be paid in return. Do not take it except in the worst-case scenario. > **Effect:** Combat-related stats +100 > > **Internal energy:** +15 years > > **Body-Protecting Qi:** Available Even accounting for the short time limit, its effects were monstrous. I could understand why Pung Yang had been so confident. I had no idea how severe the aftereffects were, but if my life were in danger, I’d swallow twenty of them, not two. Obviously. But something else bothered me. *An elixir manufactured by an unknown person.* The Item’s Grade was marked with question marks, its exact aftereffects weren’t listed, and even its maker was shrouded in mystery. What kind of bastard had created something this bizarre? *This thing reeks of something shady.* I was rolling the Temporary Strength Pill around in my palm, lost in thought, when a distant cry drifted toward us. “Mukyuuung! Taekyuuung!” Jin Mukyung froze in the middle of enthusiastically hammering Hyuk Mujin’s forehead. “Was that a hallucination?” Yeah, no. [^1]: A jiazi is a traditional sixty-year cycle.

## Korean source

```text
＃126화



나흘 전, 모든 임무를 끝마치고 태원진가로 복귀한 위팽은 자신의 빠른 일 처리를 뼛속 깊이 후회했다.

‘하루만 늦게 올걸.’

그러나 이미 늦었다. 하오문의 전서응을 받은 진위경이 눈을 까뒤집고 길길이 날뛰고 있었으니까.

“이 개 같은 마적 놈들이 감히!”

“또 무슨 일입니까?”

“풍양, 적풍단, 항산검문, 내 동생들, 위험! 매우 위험! 당장 출발!”

“……호위대 소집하겠습니다.”

모든 장애물을 치워 버린 지금, 진위경의 권위는 절대적이었다. 반 시진이 채 지나기도 전에 두 사람은 오십 명의 정예 호위대와 함께 가문을 나섰고, 쉬지 않고 내달렸다.

그리고 이틀 후, 말을 갈아타기 위해 들른 하오문 지부에서 새로운 소식을 접했다.

“뭐라? 풍양이 죽고 적풍단이 궤멸했어?”

“옛! 본 문이 파악한 바에 의하면, 삼백여 명에 달하는 적의 병력 대부분이 몰살당했고 진태경 공자께서 풍양을 쓰러트리셨답니다.”

“오오, 오오오. 태경이가!”

세상을 다 가진 듯한 진위경의 웃음은 이어지는 말에 씻은 듯이 사라졌다.

“다시 한번 말해 보게. 무경이가 어찌 되었다고?”

“그, 그게, 풍양과의 생사결에서 상당한 부상을 입으셨다고…… 하지만 목숨에도 지장 없고 빠르게 회복 중이니 걱정하실 필요 없을 듯싶습니다.”

이미 틀렸다. 진위경의 귀에는 ‘상당한 부상’밖에 들리지 않았을 것이다.

어릴 적 아우들의 손가락에 가시라도 박히는 날이면 마치 손가락이 잘린 것처럼 야단법석을 피워 대던 그다.

‘그런데 약간의 부상도 아니고 상당한 부상이라니. 난리 났군.’

위팽은 지금까지의 경험을 토대로 다음 순간 벌어질 상황을 예측했고, 아니나 다를까 정확히 들어맞았다.

“무경이가 사경을 헤맨다니!”

진위경의 포효에 하오문도가 눈을 깜빡였다.

“예, 예?”

“풍양! 네놈이 감히 내 아우를 죽여!”

상당한 부상에서 사경을 헤매게 하더니, 이제는 죽이기까지 한다. 뒤늦게 정신을 차린 하오문도가 황급히 입을 열었다.

“저기, 소가주님. 뭔가 엄청난 오해가 있는 모양이신데…….”

“내 반드시 네놈의 사지를 갈기갈기 찢어 구주에 뿌리리라!”

“…….”

“…….”

진위경의 분노는 다시 하루가 지난 다음에야 누그러졌다.

“무경이와 태경이가 어제 항산검문에서 출발했다고?”

“예. 그러니까 이제 적당히 좀 하십쇼.”

“둘 다 무사한 건가?”

“안 무사했으면 수레에 실려서 오지, 마차 타고 오겠습니까?”

“그럼…….”

“내일 정오 무렵에는 만나실 수 있을 겁니다.”

비로소 쉴 수 있다고 생각하니 위팽은 속이 다 후련했다.

자신이 누군가, 귀검(鬼劍)이라는 별호까지 붙은 절정 고수다. 당장 어디를 가도 한 자리 차지할 수 있는 실력자인데 주군을 잘못 섬기는 바람에 이런 극한의 노동에 시달리고 있었다.

‘마지막으로 술을 마신 게 언제더라.’

오늘은 드디어 오리 구이에 따끈한 술 한잔 걸칠 수 있겠다. 위팽의 입가에 흐뭇한 미소가 맺힌 그 순간이었다.

“좋아. 그럼 빨리 준비하자고.”

“예? 뭘 준비합니까?”

“내 아우들이 수많은 역경을 딛고 임무를 성공적으로 마쳤으니 환영식을 열어야지.”

“……저는 뭐, 보름이 넘도록 강호 유람하다가 온 겁니까?”

“응? 누구? 아, 자네?”

눈을 깜빡이며 위팽을 바라보던 진위경이 호탕하게 웃었다.

“그거야 물론 자네도 포함이지! 설마 내가 잊고 있었겠나?”

이 인간, 설마 했는데 잊고 있었던 게 분명하다.

황당한 얼굴로 입만 벙긋거리는 위팽에게 진위경이 말했다.

“아, 수하들 시켜서 인근 포목점에서 천 좀 사 오게나. 최대한 큼지막한 것으로.”

“천을요? 갑자기 그건 또 왜요?”

“생각해 놓은 게 있네.”



* * *



“……그렇게 된 겁니다.”

못 본 사이 10년은 늙어 버린 위팽의 말을 들으며 주위를 둘러봤다.

항산검문을 출발한 지 이틀 만에 도착한 삭주(朔州)에는 때아닌 인파가 바글거렸고, 입구에는 검은 글씨가 적힌 거대한 흰색 천이 나부꼈다.



진무경, 진태경, 그리고 혁무진의 무사귀환을 축하합니다!

- 태원진가 일동 -



나도 모르게 신음이 흘러나왔다.

“오메 시벌, 저게 뭐여…….”

살다 살다 저런 건 처음 본다.

가로 길이만 20여 장에 달하는 같은 현수막. 넓은 대로(大路)를 사이에 두고 마주 보는 두 전각의 꼭대기에 연결된 그것은 항산검문에서도 보일 것 같았다.

‘쓸데없이 글씨체 용사비등한 것 보소.’

자식 명문대 보낸 극성 부모도 이 정도는 아니겠다.

나와 진무경, 혁무진은 약속이라도 한 듯 입을 벌리고 현수막을 바라봤다.

“제 이름은 왜 작죠?”

무슨 소린가 해서 다시 보니 아주 작은 글씨로 혁무진의 이름까지 들어가 있다.

“글씨 크기 작아서 섭섭하냐? 난 기쁠 것 같은데.”

“이상하잖아요. 아래에서 보면 잘 보이지도 않아요.”

“그럼 내 이름 빼고 네 거 넣을래? 진심이야.”

잠시 고민하던 혁무진이 대답했다.

“생각해 보니까 지금도 괜찮은 것 같습니다.”

“그럼 입 닥치고 있어.”

“옙.”

대화는 더 이상 이어지지 못했다. 극성 부모, 아니 진위경이 세상에서 가장 환한 웃음을 지으며 달려왔기 때문이다.

“이 녀석들!”

이게 사람이냐 불곰이냐.

2m가 넘어 가는 거한이 솥뚜껑만 한 손으로 나와 진무경을 끌어당겼다. 이대로 으스러져도 이상하지 않을 만큼 우악스러운 힘이다.

“무사해서 다행이다. 정말 다행이야!”

무사했다. 진위경이 있는 힘껏 끌어안기 전까지는.

우두둑.

“커헉!”

“헉, 무경아!”

……지금은 별로 무사하지 않은 것 같군.

고통에 몸을 부르르 떠는 피해자를 끌어안은 가해자가 소리쳤다.

“의원! 의원!”

“의원 불러야 할 것 같은데요? 진짜 아파 보이는데.”

내 질문에 위팽이 피곤한 얼굴로 대답했다.

“하루 이틀입니까? 이럴 줄 알고 미리 불러 놨습니다.”

“오오오.”

처음으로 위팽이 위대하게 느껴지는 순간이었다.



* * *



나를 포함한 태원진가의 삼 형제와 위팽이 한자리에 모인 것은 해가 떨어진 직후였다.

진무경이 한층 두꺼워진 붕대 차림으로 나타나자 진위경이 눈치를 살폈다.

“괜찮으냐?”

“주군 같으면 괜찮으시겠습니까? 가뜩이나 다친 사람을 그렇게 막 다루시면 어떡합니까?”

“나름 살살 한 건데…….”

무공으로는 모르겠지만 신체 피지컬로 따지자면 진위경이 산서제일인이다.

나는 슬그머니 의자를 옆으로 밀었고, 진무경은 초췌한 얼굴로 대답했다.

“전 괜찮습니다.”

“…….”

전혀 안 괜찮아 보이는데.

진무경이 절정 고수라 다행이지, 무공 한 수 익히지 못한 양민이었다면 걸어 다니지도 못했다.

“이공자께서 부상을 입었다고 듣긴 했습니다만, 이 정도일 줄은 몰랐군요. 아직 내상도 다 낫지 않았던데…….”

“정말 그 풍양이란 놈이 한 짓이냐?”

두 사람의 물음에 진무경이 담담하게 수긍했다.

“강하더군요. 생각 이상으로.”

진무경이 누군가. 천하에서도 주목하는 촉망받는 후기지수다. 눈부신 천재성과 노력을 바탕으로 일찍이 절정의 경지에 오른 그가 일개 마적 우두머리에게 패배한 것이다.

“놈이 그 정도의 강자라는 말씀이십니까?”

“풍양이라, 고원의 마적 중에 제법 뛰어난 고수들이 있다고는 들었지만. 글쎄…….”

문득 두 사람의 시선이 나를 향했다. 오리 구이는 그만 처먹고 말 좀 해 보라는 무언의 압박.

입 안 가득 쑤셔 넣은 음식을 꿀꺽 삼키고 입을 열었다.

“사실이에요. 항산호 대협 소식은 들어서 아시죠? 그 양반도 팔다리 아작 나서 요즘 휠체어 타고 다닙니다.”

“휭최어가 뭡니까?”

“아, 수레요, 수레.”

진위경이 굵은 손가락으로 탁자를 두드렸다.

“그 정도의 고수라면 진작 알려졌을 텐데. 혹 무경이 네가 방심한 것은 아니냐?”

이번엔 진무경이 망설임 없이 고개를 저었다.

“미처 예상치 못한 수에 당하긴 했지만 그게 변명이 될 수는 없습니다. 다시 싸운다 해도 결과는 같을 겁니다.”

“……그 정도였더냐?”

“호신강기(護身罡氣)를 사용하더군요. 압도적이었습니다.”

진위경과 위팽이 동시에 눈을 부릅떴다.

“호신강기!”

“이공자, 그게 사실입니까?”

굳이 대답은 필요 없었다. 진무경이 그런 뻔한 거짓말을 할 이유가 없으니까. 경악한 두 사람을 향해 진무경이 다시 말을 이었다.

“지금까지 싸워 본 적 중 가장 강했습니다. 아니, 정확히는 강해졌다고 해야 맞을 것 같습니다.”

“강해졌다니?”

“그건 또 무슨…….”

“피처럼 붉은 단환 한 알을 삼키자마자 무섭도록 강해지더군요.”

드디어 잠력단에 관한 이야기가 나온다.

나는 최대한 자연스럽게 행동하려 애썼다.

‘내가 갖고 있다는 사실을 들키면 안 돼.’

잠력단은 독이 든 성배다. 분명 불길하고 수상쩍은 물건이지만 엄청난 효력을 지니고 있음을 부정할 수는 없다.

나는 이미 죽음이라는 최악(最惡)의 순간에 쓸 수 있는 차악(次惡)의 대비책으로 잠력단을 사용하기로 마음먹었다.

“짧은 순간이었지만 놈이 단환을 복용하려 할 때 분명 목갑 안에 한 알이 남아 있는 걸 봤는데…….”

진무경이 말꼬리를 흐리며 나를 바라본다.

“혹시 나중에라도 풍양의 품에서 뭔가 발견하지 못했느냐?”

“응? 뭐가.”

“목갑이라든지. 내가 말한 붉은 단환이라든지.”

나는 짐짓 눈살을 찌푸렸다.

“잘 모르겠는데? 나중에 뭐 있나 싶어서 뒤져 봤는데 웬 나무 쪼가리만 우수수 쏟아지더라니, 그게 목갑 파편이었나?”

“그럼 단환, 단환은?”

“모르지. 당장 나도 힘들어서 죽겠는데 어떻게 그걸 다 뒤져 보겠어.”

이 정도면 제법 그럴싸한 핑계다.

사람이 한두 명 죽은 것도 아니고, 워낙 격렬한 전투였으니 지쳐서 못 찾아본 것도 어쩜 당연한 일인데 더 무슨 말을 하겠나.

“그런가?”

“항산검문 사람들이 발견했을 수도 있고, 아니면 널리고 널린 피 웅덩이에 그대로 녹아 버렸을 수도 있겠지.”

“흠.”

진무경이 약간 의구심 어린 눈빛으로 나를 응시했지만 그냥 어깨만 으쓱해 보였다.

‘어차피 뒤져 봐도 안 나온다. 이놈아.’

나만이 열고 닫을 수 있는 최고의 금고, 인벤토리 한구석에 고이 모셔 뒀으니 진무경이 아니라 천하의 어떤 대도(大盜)라고 해도 잠력단의 털끝 하나 건드릴 수 없다.

‘참 편하단 말이지.’

내가 다시 한번 시스템의 편리함에 감탄하고 있을 때, 진위경과 위팽은 잠력단의 정체에 대해 유추하기 시작했다.

“볼 것도 없이 사마외도의 유산이겠군. 정마대전 당시에 비슷한 효력의 단환이 상당수 사용되었다고 들은 기억이 있다.”

“한때 고원을 비롯한 산서 북부가 마교(魔敎)의 손아귀에 떨어진 적이 있었지요. 풍양이 그 흔적을 발견한 거라면 얼추 맞아떨어집니다.”

귀를 쫑긋 세우고 듣다가 멈칫했다.

‘잠깐만. 마교?’

마교란 무협 소설에서 절대 빠지지 않는 단골손님이자 약방의 감초, 금잔디의 명예 소방관 같은 존재다.

물론 세계 평화와 빈민 구제를 위해 힘쓰는 종교 단체는 아니고, 일종의 IS(이슬람 테러 단체)라고 할 수 있겠다.

한 줄 요약하자면, 엮여서 좋은 점이 단 하나도 없는 광신도 집단이라는 거지.

‘마교에서 잠력단을 만들었다면?’

지옥에서 막 올라온 악마처럼 붉게 물들었던 풍양의 눈동자. 상상을 뛰어넘는 힘을 일시적으로나마 선사하던 비상식적인 효능.

‘이거, 그림이 대충 그려지는데.’

찝찝하다. 더럽게 찝찝하다!

하지만 고통 없이 얻어지는 것은 없는 법. 부작용도 충분히 감당할 만한…….

“그때 당시에 마교도들이 사용했던 대표적인 것이 폭혈단(爆血團)이었지, 아마.”

“말로만 들어 봤습니다. 두 시진만 지나면 전신의 혈맥이 터져서 죽는다면서요?”

“사술(詐術)로 힘을 얻으려 한 대가지.”

“폭혈단이 그 정도인데 풍양이란 놈이 쓴 건 도대체 어느 정도일까요?”

“글쎄, 모르긴 몰라도 부작용이 상상을 초월하겠지. 선천지기가 상하는 것은 물론이고 제한 시간이 끝나면 몸에 큰 무리가 갈 걸세. 결국, 제 몸을 장작 삼아 짧은 시간을 불태우는 역할이니까.”

절로 마른침이 넘어간다. 나도 모르게 목소리가 튀어나왔다.

“그다음은요?”

“마교에서 만든 물건이니 오죽하겠느냐. 마기(魔氣)가 골수까지 치밀면…… 피밖에 모르는 살인귀가 되겠지.”

“……살인귀요? 마기가 골수까지 치밀어요?”

“그런 물건이 악인의 손에 들어가면 실로 큰일…… 태경아, 왜 그러느냐?”

진위경이 걱정스러운 얼굴로 나를 바라본다. 슬쩍 이마를 문질러 보니 땀이 송골송골 맺혀 있었다.

“그냥요, 좀 더워서.”

진무경이 퉁명스럽게 대꾸했다.

“무슨 소리야. 밖에 눈 오는데.”

“소음인 주제에 뭘 알아. 난 태양인이라 그래…….”

젠장. 이제 내가 무슨 말을 하는지도 모르겠다.

나는 세 사람을 향해 어색하게 웃어 보였다.

“저기. 아까 깜빡한 게 있는데요.”

“……?”

“……?”

“……?”

“그 환단. 생각해 보니까 제가 갖고 있네요. 허허, 허허허.”

“……!”

“……!”

“……!”
```

## Current accepted English baseline

```markdown
# Chapter 126

Four days ago, after completing every mission and returning to the Jin Family of Taiyuan, Wipeng deeply regretted how efficiently he had handled things.

*I should have come back a day later.*

But it was already too late. Jin Wikyung had received a messenger eagle from the Lower District Sect and was raging with his eyes bulging out of his head.

“Those goddamned mounted bandits dare!”

“What happened now?”

“Pung Yang, the Red Wind Band, the Mount Heng Sword Sect, my brothers—they’re in danger! Great danger! We leave at once!”

“...I’ll assemble the guards.”

Now that every obstacle had been removed, Jin Wikyung’s authority was absolute. Before even half a shichen had passed, the two of them left the family with fifty elite guards and raced off without stopping.

Two days later, while changing horses at a Lower District Sect branch, they received new information.

“What? Pung Yang is dead, and the Red Wind Band has been annihilated?”

“Yes! According to what our sect has learned, most of the enemy forces, numbering around three hundred, were slaughtered. Young Master Jin Taekyung defeated Pung Yang himself.”

“Oh. Ohhh. Taekyung!”

Jin Wikyung’s laughter, as if he had gained the whole world, vanished at the next words.

“Tell me again. What happened to Mukyung?”

“Th-that is... He suffered a considerable injury in his life-and-death duel with Pung Yang... But his life is not in danger, and he is recovering quickly, so you likely have nothing to worry about.”

It was already over. Jin Wikyung had probably heard nothing except *considerable injury*.

When his younger brothers were children, if even a thorn pierced one of their fingers, he would raise such a commotion that you would have thought the finger had been severed.

*And it wasn’t a minor injury. It was a considerable one. This is going to be a disaster.*

Based on his experience so far, Wipeng predicted what would happen next.

Sure enough, he was exactly right.

“Mukyung is hovering between life and death?!”

At Jin Wikyung’s roar, the Lower District Sect member blinked.

“Y-yes?”

“Pung Yang! You dare kill my little brother!”

First Jin Wikyung turned a considerable injury into hovering between life and death, and now he’d pronounced Mukyung dead outright. The Lower District Sect member finally came to his senses and hurriedly opened his mouth.

“Lesser Family Head, I think there’s been a terrible misunderstanding...”

“I’ll tear your limbs to shreds and scatter them across the Nine Provinces!”

“...”

“...”

Jin Wikyung’s anger did not subside until another day had passed.

“Mukyung and Taekyung left the Mount Heng Sword Sect yesterday?”

“Yes. So please take it down a notch.”

“Are they both safe?”

“If they weren’t, would they be coming in a carriage instead of being carried in on a cart?”

“Then...”

“You should be able to see them around noon tomorrow.”

The thought that he could finally rest brought Wipeng immense relief.

*Who am I?*

He was a Peak master, a skilled martial artist known by the epithet Ghost Sword. He had enough ability to claim an important position wherever he went, yet because he had chosen the wrong lord to serve, he was being subjected to this extreme labor.

*When was the last time I had a drink?*

Today, at last, he would be able to enjoy some roast duck with a warm glass of liquor.

A satisfied smile had just appeared around Wipeng’s lips when Jin Wikyung spoke.

“Good. Then let’s get ready.”

“Pardon? Get ready for what?”

“My brothers overcame countless hardships and successfully completed their mission. We have to hold a welcoming ceremony.”

“...Did I spend more than half a month touring the martial world for fun?”

“Hm? Who? Oh, you?”

Jin Wikyung blinked at Wipeng, then let out a hearty laugh.

“Of course that includes you! Surely you didn’t think I’d forgotten?”

*I’d thought surely not, but this guy had definitely forgotten.*

As Wipeng stared at him in disbelief, opening and closing his mouth without a word, Jin Wikyung continued.

“Oh, have your subordinates buy some cloth from a nearby fabric shop. As large as possible.”

“Cloth? Why do we suddenly need that?”

“I have an idea.”

* * *

“...And that’s how it happened.”

Listening to Wipeng, who looked ten years older than when I’d last seen him, I glanced around.

We had reached Sakju two days after leaving the Mount Heng Sword Sect. The city was unexpectedly packed with people, and at the entrance, a gigantic white cloth bearing black writing fluttered in the wind.

Congratulations on the safe return of Jin Mukyung, Jin Taekyung, and Hyuk Mujin!

—Everyone in the Jin Family of Taiyuan—

A groan escaped me before I could stop it.

“Oh, fuck. What the hell is that...?”

In all my life, I had never seen anything like it.

The banner was more than twenty jang—over sixty meters—wide.[^1] Strung between the tops of two pavilions facing each other across a broad avenue, it looked as though it might even be visible from the Mount Heng Sword Sect.

*Look at that unnecessarily flamboyant calligraphy.*

Even overbearing parents whose child had been accepted into a prestigious university wouldn’t go this far.

Jin Mukyung, Hyuk Mujin, and I all stared at the banner with our mouths hanging open, as if we had planned it.

“Why is my name so small?”

I looked again to see what he meant. Hyuk Mujin’s name had been included in tiny letters.

“Are you disappointed that the letters are small? I’d be happy if I were you.”

“It’s strange. You can barely see it from below.”

“Want me to remove my name and put yours there instead? I’m serious.”

Hyuk Mujin thought about it for a moment before answering.

“Now that I think about it, this is fine as it is.”

“Then shut up.”

“Yes, sir.”

The conversation could go no further. The overbearing parent—no, Jin Wikyung—came running toward us with the brightest smile in the world.

“You little rascals!”

Was he a man or a brown bear?

The giant, well over two meters tall, dragged Jin Mukyung and me close with hands as large as pot lids. His brute strength was so tremendous that it would not have been strange if he had crushed us to pieces.

“I’m so glad you’re safe. Really, so glad!”

We had been safe.

Right up until Jin Wikyung hugged us with all his strength.

*Crack.*

“Guh!”

“Mukyung!”

...He doesn’t look very safe now.

The perpetrator, still embracing his victim as he trembled in pain, shouted,

“Doctor! Doctor!”

“I think we should call a doctor. He looks like he’s in real pain.”

Wipeng answered my question with a weary expression.

“Is this your first day dealing with him? I knew this would happen, so I called one in advance.”

“Ohhh.”

It was the first time I had ever thought Wipeng was magnificent.

* * *

The three Jin brothers of the Jin Family of Taiyuan, including me, and Wipeng gathered together shortly after sunset.

When Jin Mukyung appeared wrapped in even thicker bandages, Jin Wikyung cautiously studied him.

“Are you all right?”

“Would you be all right if it were you, my lord? How could you handle someone who was already injured so roughly?”

“I was being as gentle as I could...”

Jin Wikyung might not have been the strongest in martial arts, but when it came to raw physical strength, he was number one in Shanxi.

I quietly slid my chair farther away, while Jin Mukyung answered with a haggard expression.

“I’m fine.”

“...”

He looked anything but fine.

It was fortunate that Jin Mukyung was a Peak master. If he had been an ordinary civilian who had never learned martial arts, he would not have been able to walk.

Wipeng spoke up.

“I heard that the Second Young Master was injured, but I didn’t realize it was this severe. His Internal Injury hasn’t even healed completely yet...”

“Was this really the work of that Pung Yang bastard?”

In response to their questions, Jin Mukyung nodded calmly.

“He was strong. Stronger than I expected.”

Who was Jin Mukyung? He was a promising young prodigy who drew attention throughout the realm. Based on his dazzling talent and relentless effort, he had reached the Peak realm at a young age—yet he had been defeated by a mere mounted-bandit leader.

“You mean he was truly that powerful?”

“Pung Yang... I’ve heard that there are some fairly skilled masters among the mounted bandits of the plateau. But still...”

Their gazes suddenly turned toward me.

It was a silent demand that I stop stuffing my face with roast duck and say something.

I swallowed the food filling my mouth and opened it.

“It’s true. You’ve heard the news about the Great Hero known as the Tiger of Mount Heng, right? He got his arms and legs wrecked too. These days, he gets around in a wheelchair.”

“What is a wheelchair?”

“Ah, a cart. A cart.”

Jin Wikyung tapped the table with one thick finger.

“A master of that caliber would have been known long ago. Mukyung, is it possible that you let your guard down?”

This time, Jin Mukyung shook his head without hesitation.

“I was caught by a move I hadn’t anticipated, but that cannot be an excuse. Even if we fought again, the result would be the same.”

“...Was he really that strong?”

“He used Body-Protecting Qi. It was overwhelming.”

Jin Wikyung and Wipeng both opened their eyes wide.

“Body-Protecting Qi!”

“Second Young Master, is that true?”

There was no need for an answer. Jin Mukyung had no reason to tell such an obvious lie. Facing their shock, he continued.

“He was the strongest opponent I’ve ever fought. No—in exact terms, it would be more accurate to say that he became stronger.”

“Became stronger?”

“What do you mean by that...?”

“The moment he swallowed a crimson pill, he became terrifyingly powerful.”

At last, the conversation had reached the Temporary Strength Pill.

I tried to act as naturally as possible.

*I can’t let them find out I have it.*

The Temporary Strength Pill was a poisoned chalice. It was unquestionably ominous and suspicious, but there was no denying that it possessed tremendous power.

I had already decided to use it as a second-worst contingency for the worst possible moment—when I was facing death.

“It was only for a brief moment, but when he was about to take the pill, I clearly saw that one pill remained inside the wooden case...”

Jin Mukyung let his voice trail off and looked at me.

“Did you happen to find anything on Pung Yang’s person afterward?”

“Something like what?”

“A wooden case. Or the red pill I mentioned.”

I deliberately furrowed my brow.

“I’m not sure. I searched him later to see if he had anything, but all that came spilling out were piles of wooden scraps. Could those have been fragments of the case?”

“Then the pill? The pill?”

“No idea. I was exhausted enough to die myself. How was I supposed to search through everything?”

It was a fairly convincing excuse.

It wasn’t as if only one or two people had died, and the battle had been brutally fierce. It was only natural that I had been too exhausted to search properly. What more could he say?

“Is that so?”

“The people from the Mount Heng Sword Sect might have found it. Or it could have melted into one of the countless pools of blood scattered across the ground.”

“Hmm.”

Jin Mukyung stared at me with faint suspicion, but I merely shrugged.

*You won’t find it even if you search, idiot.*

I had tucked it safely into a corner of the greatest vault in existence—my Inventory, which only I could open and close. Neither Jin Mukyung nor the greatest thief under heaven could touch a hair of the Temporary Strength Pill.

*It really is convenient.*

As I marveled at the convenience of the system once again, Jin Wikyung and Wipeng began speculating about the pill’s origin.

“It must be a relic of demonic, heterodox arts. I remember hearing that quite a few pills with similar effects were used during the Great Faction War.”

“There was a time when the northern part of Shanxi, including Gaoyuan, fell into the hands of the Demonic Cult. If Pung Yang discovered traces of it, that would make sense.”

I had been listening with my ears perked up when I suddenly froze.

*Wait. The Demonic Cult?*

The Demonic Cult was a regular fixture you could never leave out of a Murim novel, the licorice in every medicine shop, and Geum Jandi’s honorary firefighter.[^2]

Of course, it wasn’t a religious organization devoted to world peace and helping the poor. It was more like IS—the Islamic terrorist group.

In short, it was a fanatical organization with absolutely nothing to gain from getting involved with it.

*If the Demonic Cult created the Temporary Strength Pill...*

Pung Yang’s eyes had been stained red, like a demon that had just climbed out of hell. The pill had granted him an absurd amount of power, even if only temporarily.

*I was starting to get the picture.*

It felt bad. Really, really bad!

But nothing could be gained without suffering. The side effects should be something I could endure...

“The most famous thing the Demonic Cult used back then was the Blood-Exploding Pill, if I remember correctly.”

“I’ve only heard of it. They say that once two shichen pass, all the blood vessels in the body burst and the user dies?”

“That was the price of trying to gain power through dark arts.”

“If the Blood-Exploding Pill was that bad, how severe would the side effects of the one Pung Yang used be?”

“I don’t know, but they must be beyond imagination. It wouldn’t just damage his innate qi. Once the time limit ended, his body would suffer tremendous strain. In the end, the pill uses the body itself as kindling and burns it for a brief period.”

I swallowed dryly. Before I knew it, my voice had jumped out.

“What happens after that?”

“It was made by the Demonic Cult. What else would you expect? Once the demonic qi surges into your very marrow… you’d become a murderous fiend who knows nothing but blood.”

“...A murderous fiend? The demonic qi surges into his marrow?”

“If such an object fell into the hands of a villain, it would be a truly terrible disaster... Taekyung, what’s wrong?”

Jin Wikyung looked at me with concern. I rubbed my forehead and found it covered in beads of sweat.

“Nothing. I’m just a little hot.”

“What are you talking about? It’s snowing outside.”

“What would a Soeumin know? I’m a Taeyangin.[^3] That’s why…”

Damn it. I didn’t even know what I was saying anymore.

I gave the other three an awkward smile.

“There’s something I forgot earlier.”

“...?”

“...?”

“...?”

“That pill. Now that I think about it, I have it. Heh-heh. Heh-heh-heh.”

“...!”

“...!”

“...!”

[^1]: A jang is a traditional Korean unit of length measuring roughly three meters.

[^2]: Geum Jandi is the heroine of the Korean drama *Boys Over Flowers*.

[^3]: Soeumin and Taeyangin are two of the four constitutional types in traditional Korean Sasang medicine.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 126`.

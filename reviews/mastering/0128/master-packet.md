# Master Edit Task — Chapter 128

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
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 칭호               | **Title**                      |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 팔천협    | **Eight Spring Gorge** |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 현령 | **county magistrate** | County official who greets Jin Taekyung and delivers the City Lord's invitation. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 적토마 | **Red Hare** | Famous horse used in Hyuk Mujin's exaggerated comparison. |
| 여포 | **Lü Bu** | Historical warrior used in Hyuk Mujin's exaggerated comparison. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 귀환자 | **Returnee** | System Title |
| 승부사 | **Gambler** | System Title |
| 수문각 | **Gate Guard Pavilion** | Jin Family gate complex at the main entrance. |
| 주모 | **Lady of the House** | Title used in Wipeng's remark that Jin Wikyung lacks a wife or household mistress. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |

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
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 현령 | 진태경 | county_official_to_celebrated_martial_artist | Great Hero Jin | formal-polite and admiring | Uses 진 대협 while praising Taekyung's alleged exploits. |
| 진태경 | 현령 | martial_artist_to_county_official | County Magistrate | polite and lightly sarcastic | Uses 현령님 while explaining that the Lesser Family Head cannot receive visitors. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 현령 | 진위경 | county_official_to_lesser_family_head | Lesser Family Head | formal-polite and deferential | Uses 진 소가주님 when asking Taekyung to convey his regards. |
| 현령 | 진무경 | county_official_to_renowned_martial_artist | Heaven Shaking Sword | formal-polite and respectful | Uses 진천검 when asking Taekyung to convey his regards. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 위팽 | 진태경 | retainer_to_third_young_master | Third Young Master | formal-polite and admonishing | Uses 삼공자 while warning Taekyung to return by noon and behave respectfully toward Jang Taebo. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

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

#### Chapter 126 tail (verified mastered)

…
“He was the strongest opponent I’ve ever fought. No—to be precise, I should say he *became* that strong.” “Became?” “What do you mean by that...?” “The instant he swallowed a blood-red pill, he became terrifyingly powerful.” At last, the conversation had reached the Temporary Strength Pill. I tried to act as naturally as possible. *I can’t let them find out I have it.* The Temporary Strength Pill was a poisoned chalice. It was undeniably ominous and suspicious, but its tremendous effects couldn’t be ignored. I had already decided to use it as a second-worst contingency for the worst possible moment—when I was facing death. “It was only for a brief moment, but when he was about to take the pill, I clearly saw that one pill remained inside the wooden case...” Jin Mukyung trailed off and looked at me. “Did you happen to find anything on Pung Yang’s person afterward?” “Hm? Like what?” “A wooden case. Or the red pill I mentioned.” I deliberately furrowed my brow. “I’m not sure. I searched him afterward to see if he had anything, but a bunch of wooden splinters spilled out. Maybe those were pieces of the case?” “Then the pill? The pill?” “No idea. I was half-dead myself. How was I supposed to search through everything?” It was a fairly convincing excuse. It wasn’t as though only one or two people had died, and the battle had been brutally fierce. It was only natural that I’d been too exhausted to search properly. What more could he say? “Is that so?” “The people from the Mount Heng Sword Sect might have found it. Or it could have dissolved into one of the countless pools of blood scattered across the ground.” “Hmm.” Jin Mukyung stared at me with faint suspicion, but I merely shrugged. *You won’t find it even if you search, idiot.* I had tucked it safely into a corner of the greatest vault in existence—my Inventory, which only I could open and close. Neither Jin Mukyung nor the greatest thief under heaven could touch a hair of the Temporary Strength Pill. *It really is convenient.* While I marveled once more at the convenience of the System, Jin Wikyung and Wipeng began speculating about the pill’s origins. “It must be a relic of demonic, heterodox arts. I remember hearing that quite a few pills with similar effects were used during the Great Faction War.” “Northern Shanxi, including Gaoyuan, once fell into the hands of the Demonic Cult. If Pung Yang discovered some remnant they left behind, it would make sense.” I had been listening with my ears perked up when I suddenly froze. *Wait. The Demonic Cult?* The Demonic Cult was a regular fixture you could never leave out of a Murim novel, the licorice in every medicine shop, and Geum Jandi’s honorary firefighter.[^2] Of course, it wasn’t a religious organization devoted to world peace and helping the poor. It was more like IS—the Islamic terrorist group. In short, they were a bunch of fanatics you had absolutely nothing to gain from getting involved with. *What if the Demonic Cult made the Temporary Strength Pill?* Pung Yang’s eyes had been stained red, like a demon that had just climbed out of hell. The pill had granted him unimaginable power, even if only temporarily. *I’m starting to see the picture.* This felt wrong. Really fucking wrong! But nothing could be gained without suffering. The side effects should be something I could endure... “The best-known pill used by the Demonic Cult at the time was the Blood-Exploding Pill, if memory serves.” “I’ve only heard stories about it. Don’t all the blood vessels in the user’s body burst after two shichen, killing them?” “That was the price of trying to gain power through dark arts.” “If the Blood-Exploding Pill was that terrible, just how severe would the side effects of Pung Yang’s pill be?” “I don’t know, but they must be beyond imagination. It wouldn’t just damage his innate qi. Once the time limit ended, his body would suffer tremendous strain. In the end, the pill uses the body itself as kindling and burns it for a brief period.” I swallowed dryly. Before I knew it, my voice had jumped out. “And after that?” “It was made by the Demonic Cult. What else would you expect? Once the demonic qi surges into your very marrow… you’d become a murderous fiend who knows nothing but blood.” “...A murderous fiend? The demonic qi surges into his marrow?” “If an item like that fell into the hands of a villain, it would be a true disaster… Taekyung, what’s wrong?” Jin Wikyung looked at me with concern. I rubbed my forehead and found it covered in beads of sweat. “Nothing. I’m just a little hot.” “What are you talking about? It’s snowing outside.” “What would a Soeumin know? I’m a Taeyangin. That’s why…”[^3] Damn it. I didn’t even know what I was saying anymore. I gave the three of them an awkward smile. “There’s something I forgot earlier.” “…?” “…?” “…?” “That pill. Now that I think about it, I have it. Heh-heh. Heh-heh-heh.” “…!” “…!” “…!” [^1]: A jang is a traditional Korean unit of length measuring roughly three meters. [^2]: Geum Jandi is the heroine of the Korean drama *Boys Over Flowers*. [^3]: Soeumin and Taeyangin are two of the four constitutional types in traditional Korean Sasang medicine.

#### Chapter 127 tail (verified mastered)

…
How could I be the only one to sit out? I accepted the liquor Jin Wikyung poured and downed it in one gulp. Gulp, gulp. The notoriously potent fire liquor burned down my throat in a rush of heat. “Guhhh.” Wow. This was no joke. I knew it was strong, but drinking it myself, it was far more potent than I’d expected. At this strength, soju and beer couldn’t even hold a candle to it. Unlike me, who shuddered from head to toe, the other three immediately filled their empty glasses to the brim. “Drink!” “Pour it down!” “Keep going till we drop!” “….” It wasn’t until we had drunk through the entire night that I learned Shanxi Province was part of North China—and that every man from North China was an incredible drinker. * * * At noon the next day, I mounted my horse in a perfectly refreshed mood, and Hyuk Mujin stared at me as if I were a monster. “Is your stomach all right?” “Yeah. It’s fine.” “Don’t tell me you were the only one who didn’t drink last night. Or did you fall asleep halfway through?” “No. The four of us kept drinking.” “…All of it?” His mouth fell open. “How is that possible? Are you even human?” “It all went down.” “Good heavens. How many bottles did you drink through the night?” He had the wrong unit. Not bottles. Barrels. We kept emptying massive casks of liquor—the kind I’d only ever seen in pirate movies—and then emptying more. “I think it was close to twenty barrels. I stopped counting after ten, so I’m not sure.” “Wow. That’s incredible.” Hyuk Mujin raised his thumb in admiration. Just then, the inn door swung open. And three zombies—or rather, three Peak masters—emerged. “Uuugh.” “Urk.” “Huff, huff.” Pale faces, parched lips, and hollow eyes. Every last one of them dragged his feet straight into the carriage. The martial artists of the escort force stared wide-eyed. “Why are they suddenly getting into the carriage…?” “They look really unwell.” “That can’t be right. Haven’t you ever drunk with our Commander? Wipeng, the God of Drinking? Never heard of him?” “Wasn’t the Commander’s epithet Ghost Sword?” “Whatever else you might say, when it comes to drinking, he could probably beat even the Martial God. They’re probably just like this because all the fatigue they’ve accumulated finally caught up with them.” As the martial artists whispered among themselves, the carriage door suddenly flew open, and one person hurriedly dashed out and bent over. “Urrp, buuurrgh!” Splaaarsh. Wipeng spent a good while spewing nothing but pale liquid, then staggered back into the carriage. One of the martial artists who had been talking animatedly muttered in a dazed voice, “…This can’t be.” “It absolutely can. Anyone can see that’s a hangover. They drank like that all night without sleeping. Of course they’d end up like that.” “Then why is the Third Young Master so perfectly fine?” Every eye in the escort force turned toward me. The smell of liquor radiating from my entire body was strong enough to send chills down the spine. But in complete contrast, my face looked unbelievably refreshed, and my breathing was calm. “No way…” “The Third Young Master beat the Commander? That God of Drinking?” The courtyard buzzed with excitement. Hyuk Mujin’s look of admiration had gone beyond admiration and become outright reverence. “Ah, I knew it! That’s our Captain—the man who used to drink with courtesans every damn day!” “….” “I remember what the Chief Steward said. If Captain had kept drinking for three more years, he would have uprooted our family’s entire foundation. So that’s why you always had to steal from the family coffers!” “…Hey, you punk.” We weren’t alone. What did he think would happen to my image if he talked like that? As if the stares pouring in from every direction hadn’t already made my face feel hot enough. “Ahem. Ahem!” I cleared my throat and glanced around. And what do you know? The eyes of all those rough-looking men were sparkling brighter than stars in the night sky. “The true God of Drinking. That’s him.” “He’s famous in Taiyuan’s red-light district. Haven’t you heard of the Night King?” “The Night King? The epithet says it all. So he was already renowned for his drinking.” “No, not that… You know. That.” “Gasp. Is it true?” “How would I know? I’ve never seen it.” “Turns out he’s a true man among men.” > **System** > > Everyone gathered here is impressed by your drinking capacity and imposing presence! > > **Fame** rises by 20! > > **Fame** rises by 22! > > **Fame** rises by 25! > > If a particular rumor spreads, you may obtain a related **Title**. “….” Why the fuck was my Fame shooting up? And what was this about a related Title? No, thanks. Put it away. Please, just let me be satisfied with the Sleeping Dragon of Shanxi. *Stop it, you lunatics…* I turned away in inexplicable shame—only to find Hyuk Mujin staring intently at a certain part of my body. “…What are you doing?” “Oh, I was just measuring it by eye.” He answered so matter-of-factly that I was almost thrown off. Hyuk Mujin held out his forearm with an innocent smile. “Wow. As expected, you’re amazing. Hehe.” In return for his forearm, I offered him my fist. Thwack!

## Korean source

```text
＃128화



장 노인은 시끄러운 소리에 잠에서 깼다.

‘어느 육시랄 놈들이.’

가뜩이나 늙어서 점점 잠이 줄어드는 그로서는 달갑지 않은 상황이었다.

‘어떤 놈들인지 면상이나 한번 보자.’

뻐근한 몸을 이끌고 초가집을 나선 장 노인이 가장 먼저 발견한 것은 구름처럼 모여 있는 인파였다.

그 숫자가 어림잡아 수백. 마을 안에 발 달린 것들은 사람이고 짐승이고 죄다 모여 있는 것 같았다.

“이게 다 뭔 일이여?”

워낙 고만고만한 마을이다 보니 대부분 아는 얼굴이다.

장 노인의 중얼거림에 익숙한 얼굴의 시전 상인이 알은체를 했다.

“일어나셨습니까.”

“이렇게 난리를 쳐 대는데 안 일어나고 배겨?”

“하하, 어르신께서 이해하십시오. 귀한 손님이 오신다는 말에 다들 모여 있는 거니까요.”

장 노인이 퉁명스럽게 대꾸했다.

“귀한 손님? 황상(皇上)이라도 오나?”

“아이고, 또 그러신다. 황상께서 어르신 친굽니까?”

“나이로 따지면 내가 애비지.”

“그러다가 역모죄로 잡혀갑니다. 저기 관군들 안 보이세요?”

“관군?”

상인의 턱짓에 수십 명의 관군과 관복을 차려입은 현령(懸令)을 발견한 장 노인이 눈을 가늘게 떴다.

“마적 놈들 어슬렁거릴 때는 보이지도 않던 놈이 관복까지 차려입어? 그 귀한 손님이 고관대작이라도 되나?”

“고관대작은 아니지만 산서성에서는 이겁니다, 이거.”

상인이 엄지를 치켜세운 그 순간, 몰려 있던 사람들의 입에서 탄성이 터져 나왔다.

“저기 온다!”

“왔다!”

장 노인은 사람들의 시선을 따라 고개를 돌렸다. 멀리서부터 달려오는 오십 기의 기마와 휘날리는 깃발을 확인한 그는 그제야 귀한 손님의 정체를 알 수 있었다.

‘태원진가.’

세상 돌아가는 일에는 별 관심이 없는 장 노인이었지만 태원진가의 이름만은 귀가 닳도록 들었다.

장장 삼백 년간 명맥을 이어 온 명가(名家)이자 산서성의 패권을 틀어쥔 패자(霸者).

위풍당당한 행렬을 지켜보던 장 노인이 문득 미간을 좁혔다.

‘그놈이 누구였더라. 그, 뭐냐. 산서, 산서…… 무슨 용이었는데?’

나이를 먹으니 기억력도 떨어진다. 지나간 세월에 야속함을 느끼던 장 노인의 눈에 한 사람이 들어왔다.

“여보게, 저 젊은이가 누군가?”

“아, 저 소협 말입니까?”

당장 보이는 태원진가의 무인만 자그마치 수십 명이다. 그러나 상인은 대번에 알아들었다.

낭중지추. 젊은이의 존재는 주머니 속의 송곳과 같아서 어디에서나 눈에 띄니 이상한 일도 아니다.

“산서잠룡입니다.”

스릉-

마치 그 말을 들은 것처럼, 선두에 선 청년이 허리춤에 찬 검을 뽑아 들었다.

투명한 검신이 햇빛을 받아 번쩍 빛남과 동시에 거대한 함성이 터져 나왔다.

“와아아아아!”

“태원진가! 산서잠룡! 진천검!”



* * *



“산서잠룡! 진태경! 산서잠룡! 진태경!”

사방에서 울려 퍼지는 내 별호와 이름. 지난 며칠간 이미 몇 번을 겪었음에도 뿌듯하다.

‘아이돌이 이런 기분인가.’

저거 그거잖아. 우윳빛깔 진태경. 사랑해요. 진태경.

음악 예능에서나 보던 아이돌 팬클럽이 눈앞에 있다. 나는 흐뭇하게 웃으며 허리춤에 찬 [이름 없는 검]을 뽑아 들었다.

스르릉. 번쩍!

브랜드가 만년한철이라 그런지 시각 효과로는 이만한 게 없더라.

“우와아아아아!”

“꺄아악! 공자님 절 가져요!”

“응애! 응애!”

남녀노소, 전 연령대를 아우르는 전체 이용가 같은 남자.

그게 바로 나다.

띠링.



- 명성이 19 상승합니다!

- 명성이 26 상승합니다!

- 명성이 31 상승합니다!

.

..

- 명성이 대폭 상승합니다!

- 명성의 증가로 칭호, [산서잠룡]의 효과가 강화됩니다!



‘칭호 효과가 강화됐다고?’

생각지도 못한 수확이다. 변경된 내용도 확인해 볼 겸, 상태창을 켰다.

띠링.



상태창



[Lv.61 진태경]

직업 : 일류 무인

명성 : 2100 (+250)

칭호 : 4개 (칭호 효과 적용 중)

- 귀환자 (모든 능력치 +10)

- 산서잠룡 (모든 능력치 +15, 명성 +200)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 승부사 (일대일 전투 시 전투 관련 능력치 +10%)

근력 : 196 (+30)체력 : 195 (+30)

민첩 : 192 (+30)지력 : 35(+30)

매력 : 35 (+30)공력 : 45년

맷집 : 155 (+30)

잔여 포인트 : 60

- 잔여 포인트를 분배하십시오.





모든 능력치 10, 명성 100 상승이었던 산서잠룡의 칭호 효과가 확실히 변했다.

‘이름값이 높아졌다, 이건가?’

칭호라는 건 하늘에서 뚝 떨어지는 게 아니다.

나만 해도 잠룡이니 뭐니 하는 소문이 슬금슬금 퍼지더니 어느 순간 명성이 오르면서 산서잠룡이라는 칭호를 얻게 됐다.

아마 명성이 높아질수록 칭호 효과도 상승하는 듯싶었다.

‘레벨도 벌써 60이 넘었고.’

오랜만에 확인한 상태창은 쑥쑥 커 있었다. 훌쩍 솟구친 명성과 200에 가까워진 전투 능력치. 45년의 빵빵한 공력까지.

‘크으으. 주모!’

짜릿함에 몸을 부르르 떨자 오른편에서 깃발을 들고 있던 혁무진이 나를 정신병자 보듯 바라봤다.

“그렇게 좋으십니까?”

나는 짐짓 정색하며 대답했다.

“누가 좋아했다고 그래. 그냥 사람들이 좋아하니까 분위기 좀 띄워 준 거지.”

“……할 말은 많지만 하지 않겠습니다.”

“현명한 선택이야.”

사람들의 환호 속에서 걷던 우리는 말고삐를 당겨 속도를 늦췄다.

우르르 쏟아져 나와 앞길을 가로막은 수십 명의 사내 때문이었다.

그 가운데 혼자 화려한 붉은색 옷을 차려입은 뚱뚱이가 나를 보고 활짝 웃었다.

“허허, 듣던 대로 헌앙하시구려. 산서잠룡의 위명은 내 익히 들었소이다.”

“아, 예.”

나는 어리둥절해져서 물었다.

“그런데 누구세요?”

혁무진이 황급히 속삭였다.

“현령이잖아요, 현령.”

“현령이 뭔데.”

“네? 현령이 뭔지도 모르세요?”

“이장 같은 건가?”

“와, 미치겠네. 그냥 벼슬아치라고 생각하세요.”

“아, 벼슬아치. 그럼 뒤에 있는 사람들이 관군?”

“……왜 이러세요, 관군 처음 보는 사람처럼.”

“아니, 그냥 신기해서.”

사실 진짜 처음 본다.

나는 유심히 뚱뚱이, 아니 현령과 그 부하들을 살펴봤다.

이 세상에도 나라가 있고 관아나 법 집행 기관이 있다는 사실은 알았지만 이렇게 실제로 마주친 건 처음이다.

‘어떻게 코빼기도 안 비출 수가 있냐.’

하루에도 수십 건씩 강력 범죄가 일어나는 동네인데 관군들이 범인 잡아가는 건 구경도 못 해 봤다.

하기야, 약 2천 명이 맞붙었던 팔천협 전투나 이번 적풍단 관련해서도 아무런 제재가 없었던 걸 생각해 보면 그 정도는 당연한 건가.

‘그렇다고 어슬렁거리는 마적 놈들 때려잡는 것도 아니고.’

이 자식들은 하는 일이 뭘까?

현대였다면 무림인 중 절반은 살인죄로 교도소 독방에 갇혀 있을 거라는 상상을 할 때였다.

“커흠, 커흐흠!”

현령이 벌겋게 달아오른 얼굴로 헛기침을 했다.

저 양반도 나름 직위가 있는 벼슬아치일 텐데, 내게 무시당했다는 생각에 기분이 상한 모양이었다.

“어이고, 죄송합니다. 제가 얼마 전에 머리를 다쳐서 자꾸 정신을 놓고 다니네요.”

그냥 적당히 대처한 건데 그제야 현령의 얼굴이 살짝 풀린다.

“으흠, 아니올시다. 극악무도한 마적 놈들을 상대하시느라 노고가 크셨을 텐데. 아, 자그마치 오백이 넘는 마적을 죽였다지요?”

“어…… 오백 명이요?”

“그렇소. 진천검과 산서잠룡. 두 영웅의 무용담을 듣고 얼마나 기뻤는지. 허허.”

저건 어디서 튀어나온 숫자인지 모르겠네.

이번 전투에 참여한 마적들을 통틀어도 삼백 명이 될까 말까고, 그마저도 나와 진무경이 도착했을 때쯤에는 백 명도 채 남지 않았었다.

‘실제로는 풍양이랑 이미 지쳐 있던 마적 칠십 명? 그쯤 되려나?’

뭐, 원래 소문이라는 게 으레 과장되기 마련이지.

“에이, 그건 너무…….”

사실을 얘기해 주려던 찰나, 나와 현령의 대화를 숨죽이고 듣고 있던 사람들 사이로 술렁임이 번졌다.

“오백 명? 산서잠룡과 진천검 둘이서 간 것 아니었나?”

“허어, 그럼 둘이서 오백 명이 넘는 마적단을?”

“세상에, 사람이 어찌 그리 강할 수 있단 말인가!”

띠링.



- 사람들이 당신을 경외 어린 시선으로 바라봅니다.

- 명성이 40 상승합니다!



“너무, 뭐라고 했소?”

나는 어리둥절해하는 현령을 향해 말을 이었다.

“너무 축소됐네요. 실제로는 족히 육백 명 가까이 되었습니다.”

“육백!”

“저랑 둘째 형님이 반반씩 맡았죠.”

“그럼 한 사람당 삼백 명을!”

“음, 정확히는 이백팔십오 명쯤?”

현령은 물론이고 관군까지 입을 딱 벌렸다.

“오오!”

“이백팔십오 명! 심지어 자세해!”

띠링.



- 사람들이 당신을 경외 어린 시선으로 바라봅니다.

- 명성이 40 상승합니다!



혁무진이 이번엔 벌레 보는 것 같은 얼굴로 내게 속삭였다.

“그렇게까지 하고 싶습니까?”

“응.”

“괜히 전공 부풀렸다가 거짓말인 거 들통나면 어쩌시려고요?”

“너랑 월화, 항산검문만 입 다물면 돼. 그러니까 빨리 한마디 거들어.”

“싫습니다. 이 혁무진, 이래 봬도 하늘을 우러러 한 점 부끄러움 없는, 진실 된 삶을 살아온 놈입니다.”

나는 어이가 없어져서 물었다.

“진무경이 내 전각 무너트렸을 때, 있지도 않은 암살자랑 싸운 게 너 아니었냐?”

“…….”

“할 말 없으면 입 닥치고 표정 관리 잘하자. 내 이백팔십…… 몇 명이었지?”

“이백팔십오 명이요.”

“그래, 거기서 삼십 명 정도는 네가 처리한 걸로 해 줄게. 불알 달고 태어났으면 태원진가 수문각주 정도는 해 봐야지. 안 그래?”

“……!”

하늘을 우러러 한 점 부끄럼 없는 진실 된 인생을 살아왔다는 혁무진은, 현란한 혀 드리블로 현령의 마음을 쏙 빼놓았다.

대부분 이, 삼류였던 마적들은 하나같이 일류 고수요, 적토마를 탄 여포가 되었고 풍양은 일검에 산과 바다를 가르는 무적의 고수로 둔갑시켰다.

‘이 자식 입에서 나오는 말은 앞으로 믿고 거른다.’

어찌나 거짓말을 잘하는지 나조차도 저게 진짜인가 헷갈릴 정도다. 당사자인 나도 이런데, 다른 사람들이야 말할 것도 없지.

“……해서. 고원의 절대자 풍양과 극악무도한 적풍단은 항산검문에서 뼈를 묻게 되었지요.”

혁무진의 구라, 아니 이야기가 끝나자마자 곳곳에서 아쉬움 섞인 한숨이 터져 나왔다. 그중에서도 현령의 반응이 가장 열광적이었다.

“허어어어어, 이럴 수가. 어찌 그런 일이…… 무림은 참으로 놀라우면서도 무서운 곳이구려.”

혁무진이 우수에 젖은 눈으로 사람들을 훑어보았다.

“저 같은 무부(武夫)는 두려움이 없습니다. 검을 쥔 후부터 늘 죽음을 벗 삼아 살아가고 있으니까요. 다만 한 가지 소원이 있다면…….”

“있다면?”

“강자의 검에 죽는 것. 그것 말고는 바랄 것이 없습니다.”

“…….”

진짜 이 정도면 지랄이 풍작이다.

나는 혁무진의 뒤통수를 후려치고 싶은 충동을 억누르며 앞으로 나섰다.

명성치는 이미 쪽쪽 빨아 먹어서 더 오르지도 않는 상태. 굳이 배 나온 아저씨랑 계속 얘기를 나눌 이유가 없다.

“말씀 중에 죄송합니다만, 저희가 갈 길이 바빠서요.”

최면에 걸린 것처럼 몽롱한 눈빛으로 혁무진을 바라보던 현령이 그때 퍼뜩 정신을 차렸다.

“아, 미안하오. 내 원래 이러려던 게 아니었는데.”

“그럼 혹시 볼일이라도.”

“진 대협을 뵐 수 있겠소? 소가주님 말이오.”

현령의 시선이 내 등 뒤에 있는 마차를 향한다.

밖에서 보이지는 않지만 안에는 진위경과 진무경, 그리고 위팽이 타고 있었다.

‘술에 떡이 돼서 말이지.’

지난 3일 동안의 주량 대결에서 내게 처참하게 발린 패배자들이다. 하지만 사실대로 말할 수야 있나, 나는 표정 하나 변하지 않고 거짓말을 했다.

“죄송하지만 지금 운기조식 중이시라 뵐 수 없을 것 같습니다. 현령님께서도 아시다시피 상당히 위험한 일이라.”

“아, 그렇구려. 그럼 어쩔 수 없지.”

혀를 찬 현령이 소매에서 돌돌 말린 종이를 꺼내어 내게 건넸다.

“이게 뭡니까?”

“성주(城主)님께서 보내시는 초청장이오. 근래 진 소협의 활약을 들으시고는 아주 큰 감명을 받으셨는지 후기지수 몇 명과 함께 자리를 마련하셨소.”

띠링.



- 퀘스트가 생성되었습니다.
```

## Current accepted English baseline

```markdown
# Chapter 128

Old Man Jang woke to the sound of a commotion.

*What goddamn bastards are making all that noise?*

He was old enough that his hours of sleep were gradually dwindling, so this was hardly a welcome development.

*I’ll go see what their faces look like.*

Dragging his stiff body out of the thatched cottage, Old Man Jang’s eyes immediately fell on a crowd gathered like clouds.

There were hundreds of them, by his rough estimate. It looked as if everything in the village with legs—human or animal—had gathered in one place.

“What’s all this about?”

It was a small, unremarkable village, so he knew most of the faces.

At Old Man Jang’s muttering, a familiar market merchant greeted him.

“You’re awake, sir.”

“With this kind of racket, how could I stay asleep?”

“Ha-ha, please understand, sir. Everyone’s gathered because they heard an important guest was coming.”

Old Man Jang grunted.

“An important guest? Is the Emperor coming?”

“Oh, there you go again. Is the Emperor your friend?”

“By age, I’d be his father.”

“You’ll get arrested for treason talking like that. Can’t you see the government soldiers over there?”

“Government soldiers?”

Following the merchant’s nod, Old Man Jang spotted dozens of government troops and a man dressed in an official robe—the county magistrate. His eyes narrowed.

“That fellow never showed his face when the mounted bandits were prowling around, but now he’s dressed up in his official robes too? Is this important guest some high-ranking official?”

“Not a high-ranking official, but in Shanxi Province, they’re number one.”

The merchant raised his thumb.

At that very moment, an uproar erupted from the assembled crowd.

“They’re coming!”

“They’re here!”

Old Man Jang turned his head in the direction of everyone’s gaze. When he saw fifty mounted riders charging toward them from the distance, their flags snapping in the wind, he finally understood who the important guests were.

*The Jin Family of Taiyuan.*

Old Man Jang had little interest in the affairs of the world, but he had heard the name of the Jin Family of Taiyuan until his ears rang.

A prestigious family that had maintained its lineage for three hundred years, and the hegemon that held Shanxi Province in its grasp.

As Old Man Jang watched the imposing procession, his brow suddenly furrowed.

*Who was that fellow again? That… what was it? Shanxi, Shanxi… some kind of dragon?*

Age had weakened his memory as well. As Old Man Jang lamented the passing years, one person caught his eye.

“Say, who’s that young man?”

“Ah, that Young Hero?”

There were dozens of martial artists from the Jin Family of Taiyuan alone, all clearly visible. Yet the merchant immediately understood whom he meant.

An awl in a pocket. The young man’s presence was like an awl tucked inside a pouch, bound to stand out wherever he went, so there was nothing strange about it.

“That’s the Sleeping Dragon of Shanxi.”

Shing—

As if he had heard those words, the young man at the head of the procession drew the sword at his waist.

The transparent blade flashed in the sunlight, and a thunderous cheer erupted.

“Waaaaaah!”

“Jin Family of Taiyuan! Sleeping Dragon of Shanxi! Heaven Shaking Sword!”

* * *

“Sleeping Dragon of Shanxi! Jin Taekyung! Sleeping Dragon of Shanxi! Jin Taekyung!”

My epithet and name rang out from every direction. Even though I’d already experienced this several times over the past few days, it still made me feel proud.

*Is this how idols feel?*

It was just like that thing. *Milky-skinned Jin Taekyung. We love you, Jin Taekyung.*

An idol fan club, the kind I’d only ever seen on music variety shows, was right in front of me. Smiling contentedly, I drew the [Unnamed Sword] from my waist.

Shhhng. Flash!

Maybe it was the Ten-Thousand-Year Cold Iron brand, but nothing else came close when it came to visual effects.

“Waaaaaah!”

“Eeeeek! Young Master, take me!”

“Wah! Wah!”

A man for everyone, like something rated for all audiences—men and women, young and old.

That man was me.

Ding.

> **System**
>
> **Fame** rises by 19!
>
> **Fame** rises by 26!
>
> **Fame** rises by 31!
>
> …
>
> …
>
> **Fame** rises significantly!
>
> Due to the increase in **Fame**, the effect of the **Sleeping Dragon of Shanxi** **Title** has been strengthened!

*The Title effect has been strengthened?*

That was an unexpected bonus. I opened my Status Window to check the changes.

Ding.

> **System**
>
> **Status Window**
>
> **Lv. 61 Jin Taekyung**
>
> **Class:** First Rate martial artist
>
> **Fame:** 2,100 (+250)
>
> **Titles:** 4 (Title effects active)
>
> — Returned One (All stats +10)
>
> — Sleeping Dragon of Shanxi (All stats +15, Fame +200)
>
> — Scion of a Prestigious Family (All stats +5, Fame +50)
>
> — Gambler (Combat-related stats +10% in one-on-one combat)
>
> **Strength:** 196 (+30)  
> **Stamina:** 195 (+30)
>
> **Agility:** 192 (+30)  
> **Intelligence:** 35 (+30)
>
> **Charm:** 35 (+30)  
> **Internal energy:** 45 years
>
> **Toughness:** 155 (+30)
>
> **Remaining points:** 60
>
> — Distribute your remaining points.

The Sleeping Dragon of Shanxi’s Title effect had definitely changed from All stats +10 and Fame +100.

*So my name carries more weight now?*

Titles didn’t simply drop from the heavens.

In my case, rumors about me being some kind of sleeping dragon had gradually spread, and at some point, my Fame rose and I gained the Title Sleeping Dragon of Shanxi.

It seemed that the effect of a Title increased along with one’s Fame.

*My Level has already passed sixty, too.*

The Status Window, which I hadn’t checked in a while, had grown by leaps and bounds. My Fame had shot up, my combat-related stats were approaching 200, and I had a solid forty-five years of internal energy.

*Hehehe. Innkeeper!*

I shuddered with exhilaration, and Hyuk Mujin, who was carrying a flag on my right, looked at me as if I were mentally ill.

“Are you really that happy?”

I deliberately put on a serious face.

“Who said I was happy? People like me, so I was just helping to liven up the mood.”

“……I have a lot to say, but I won’t.”

“Wise choice.”

Walking amid the crowd’s cheers, we pulled on the reins and slowed down.

Dozens of men had poured out into the street and blocked our path.

Among them, a fat man dressed in splendid red robes smiled broadly at me.

“Heh-heh, you’re every bit as dignified and handsome as I’d heard. I’ve long been familiar with the great reputation of the Sleeping Dragon of Shanxi.”

“Ah, yes.”

Confused, I asked,

“But who are you?”

Hyuk Mujin hurriedly whispered,

“He’s the county magistrate. The county magistrate.”

“What’s a county magistrate?”

“What? You don’t even know what a county magistrate is?”

“Is he like a village head?”

“Wow, this is driving me crazy. Just think of him as an official.”

“An official. Then are the people behind him government troops?”

“……Why are you acting like you’ve never seen government troops before?”

“No, I just find it interesting.”

In fact, I really had never seen them before.

I studied the fat man—no, the county magistrate—and his subordinates carefully.

I knew that this world had a government, official offices, and law-enforcement agencies, but this was the first time I’d actually encountered them.

*How could they never show even the tips of their noses?*

Violent crimes happened dozens of times a day in this neighborhood, yet I had never once seen government troops drag away a criminal.

Then again, considering the authorities hadn’t intervened in the Battle of Eight Spring Gorge, where roughly two thousand people had clashed, or in this latest incident involving the Red Wind Band, perhaps that was only natural.

*It’s not as if they’re even beating up the mounted bandits who loiter around.*

What exactly did these bastards do?

I was imagining that, if this were modern times, half the martial artists in the Murim would be locked in solitary confinement for murder when the county magistrate cleared his throat.

“Ahem. Ahem!”

His face flushed red as he coughed awkwardly.

He was an official with a certain position, after all, and seemed offended that I had ignored him.

“Oh, I’m sorry. I injured my head a while ago, so I keep spacing out.”

I’d only offered a reasonable excuse, but the county magistrate’s expression relaxed slightly.

“Ahem, no, no. You must have gone through great hardship dealing with those vicious mounted bandits. Ah, I heard you killed more than five hundred of them?”

“Uh… five hundred?”

“That’s right. I was overjoyed to hear the tales of valor of the two heroes, the Heaven Shaking Sword and the Sleeping Dragon of Shanxi. Ha-ha.”

I had no idea where that number had come from.

Even if you counted every mounted bandit who took part in the battle, there might have been three hundred at most. And by the time Jin Mukyung and I arrived, fewer than a hundred of them had remained.

*In reality, there was Pung Yang and maybe seventy mounted bandits who were already exhausted. Something like that.*

Well, rumors were usually exaggerated.

“Come on, that’s too—”

Just as I was about to explain the truth, murmurs spread through the people who had been listening to my conversation with the county magistrate.

“Five hundred? Didn’t the Sleeping Dragon of Shanxi and the Heaven Shaking Sword go there alone?”

“Good heavens. The two of them defeated a mounted-bandit force of more than five hundred?”

“How can human beings be that strong?”

Ding.

> **System**
>
> People are looking at you with awe.
>
> **Fame** rises by 40!

“Too what did you say?”

I continued speaking to the bewildered county magistrate.

“That’s a serious understatement. In reality, there were nearly six hundred.”

“Six hundred!”

“My second brother and I took half each.”

“Then three hundred each!”

“Hmm. More precisely, about 285?”

The county magistrate—and even the government troops—gaped at me.

“Ooh!”

“Two hundred and eighty-five! And he even knows the exact number!”

Ding.

> **System**
>
> People are looking at you with awe.
>
> **Fame** rises by 40!

This time, Hyuk Mujin whispered to me with an expression usually reserved for looking at a bug.

“Do you really want to take it this far?”

“Yep.”

“What are you going to do if you inflate your achievements for no reason and get caught lying?”

“You, Wolhwa, and the Mount Heng Sword Sect just have to keep your mouths shut. So hurry up and back me up.”

“I refuse. Hyuk Mujin may not look it, but I’ve lived a truthful life without a single shameful moment before the heavens.”

I stared at him in disbelief.

“When Jin Mukyung destroyed my pavilion, weren’t you the one who fought assassins that didn’t even exist?”

“…….”

“If you have nothing to say, shut up and manage your expression. My two hundred and eighty… How many was it?”

“Two hundred and eighty-five.”

“Right. I’ll count about thirty of them as your kills. If you were born with balls, you ought to make Master of the Gatekeeper Pavilion in the Jin Family of Taiyuan at least once in your life. Don’t you think?”

“……!”

Hyuk Mujin, who had lived a truthful life without a single shameful moment before the heavens, used his dazzling tongue to completely win over the county magistrate.

The mounted bandits, most of whom had been Second Rate or Third Rate, became First Rate masters to a man—each a Lü Bu astride Red Hare. Pung Yang became an invincible master who could cleave mountains and seas with a single sword strike.

*From now on, I’m filtering anything that comes out of this bastard’s mouth.*

He was such a skilled liar that even I found myself wondering whether it was true. If even I, the person involved, was confused, there was no hope for anyone else.

“……and that was how Pung Yang, the absolute ruler of Gaoyuan, and the vicious Red Wind Band came to meet their end at the Mount Heng Sword Sect.”

The moment Hyuk Mujin finished his bullshit—his story, I mean—sighs of disappointment rose from all around us. The county magistrate’s reaction was the most enthusiastic of all.

“Whaaaat? How could such a thing happen? The Murim is truly a wondrous yet terrifying place.”

Hyuk Mujin swept his gaze over the crowd with melancholy eyes.

“A martial brute like me has no fear. Ever since I took up the sword, I’ve lived with death as my companion. But if I have one wish…”

“One wish?”

“To die by the sword of someone strong. That is all I could ask for.”

“…….”

At this point, this was a bumper crop of bullshit.

Suppressing the urge to smack Hyuk Mujin in the back of the head, I stepped forward.

I had already milked the Fame for all it was worth, and there was no reason to keep talking to a potbellied middle-aged man.

“Sorry to interrupt, but we’re in a hurry.”

The county magistrate, who had been gazing at Hyuk Mujin with dazed eyes as if hypnotized, suddenly came to his senses.

“Ah, my apologies. I didn’t mean for this to happen.”

“Then do you have some other business?”

“Could I meet Great Hero Jin? I mean, the Lesser Family Head.”

The county magistrate’s gaze shifted toward the carriage behind me.

They couldn’t be seen from outside, but Jin Wikyung, Jin Mukyung, and Wipeng were inside.

*Because they were drunk out of their minds.*

They were the losers who had been utterly crushed by me in our drinking contest over the past three days. But how could I tell him the truth? Without changing my expression, I lied.

“I’m sorry, but he’s currently circulating his qi and won’t be able to see you. As you know, County Magistrate, it’s quite dangerous.”

“Ah, I see. Then it can’t be helped.”

The county magistrate clicked his tongue, then pulled a tightly rolled piece of paper from his sleeve and handed it to me.

“What is this?”

“An invitation from the City Lord. After hearing about your recent exploits, Young Hero Jin, he seems to have been deeply impressed, so he arranged a gathering with several young prodigies.”

Ding.

> **System**
>
> A **Quest** has been created.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 128`.

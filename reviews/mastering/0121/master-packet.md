# Master Edit Task — Chapter 121

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
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 검법     | **sword technique**                              |                                                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 지부장    | **Branch Leader**                            |
| 큰형     | **eldest brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 아이템              | **Item**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 귀문      | **your sect**                                                   |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 은소월 | **Eun Sowol** |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 하수오 | **He Shou Wu** | Traditional medicinal herb; a thirty-year-old specimen is offered to Jang Taebo. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
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
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진위경 | 이소월 | host_to_new_sect_leader | Young Lady | formal-polite | Jin Wikyung addresses Lee Seowol as 소저 before accepting her oath. |
| 이소월 | 진위경 | new_sect_leader_to_lesser_family_head | Lesser Family Head | formal-deferential | Lee Seowol refers to Jin Wikyung as 소가주님 when describing his summons. |
| 철무백 | 진위경 | sect_elder_to_lesser_family_head | Lesser Family Head | formal-deferential | Cheol Mubaek formally greets Jin Wikyung as the Lesser Family Head of the Jin Family of Taiyuan. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진태경 | 이소월 | young_martial_artist_to_allied_sect_leader | Young Lady Lee | formal-polite | Taekyung uses 이 소저 while greeting Seowol at the banquet. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 큰형 | kinship | Eldest older brother, not a generic older brother. | |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
| 고생하셨습니다 | register | Subordinate courtesy (“thank you for your hard work”), not a superior’s “Good work.” | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 115–119

## Plot

Jin Taekyung and Jin Mukyung enter the Mount Heng fortress after finding Cheol Mubaek critically wounded by Pung Yang’s Temporary Strength Pill. Wolhwa and Hyuk Mujin remain behind to protect Cheol while the Jin brothers attack the Red Wind Band. Although Mukyung initially dominates, Pung Yang consumes another pill, gains enough power to produce imperfect Sword Force and Body-Protecting Qi, and reverses the fight. He reveals that he obtained the Crimson Blood Twelve Swords, the Crimson Blood Cultivation Technique, and five Temporary Strength Pills from a hidden plateau tomb, killing his companions to keep the legacy.

Mukyung appears to break Pung Yang’s defensive qi, but concealed throwing knives leave him unconscious. Taekyung consumes Jopil’s Blazing Flame Divine Pill, gaining thirty years of Scorching Yang Qi and temporarily raising his internal energy to forty-five years. He outmaneuvers Pung Yang and wounds him with a dagger before his Body-Protecting Qi fully forms, but the divine pill’s energy runs wild and severely damages Taekyung. As Pung Yang’s Temporary Strength Pill begins to wear off, Lee Seowol and nine surviving Mount Heng martial artists make a last stand so Taekyung can escape with Mukyung.

Taekyung refuses to flee and attacks with One Annihilation, but Pung Yang destroys it, severely injures him, and captures him. When Pung Yang attempts to mutilate him, Taekyung summons the Unnamed Sword. Its Ten-Thousand-Year Cold Iron destroys Pung Yang’s Body-Protecting Qi, leaving the confrontation unresolved.

## Continuity

- Cheol Mubaek is alive but critically injured, with broken limbs and severe internal injuries; Wolhwa’s medicine provides only temporary support.
- Jin Mukyung is unconscious after Pung Yang’s five concealed throwing knives; his recovery is unresolved.
- Pung Yang reached the Peak realm through the Crimson Blood martial arts and heterodox cultivation in two years.
- Pung Yang has approximately seventy percent mastery of the Crimson Blood Twelve Sabers and can temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi with a Temporary Strength Pill.
- Pung Yang’s Temporary Strength Pill began losing effect after roughly half a shichen. He retained one final pill but refused to take it because using three consecutively could endanger his life.
- Pung Yang still intends to capture both Jin brothers and obtain the Taiyuan Jin Family’s martial arts formulas.
- Taekyung consumed the Blazing Flame Divine Pill and gained the Scorching Yang Qi attribute, but its uncontrolled energy caused severe internal injury and a major drop in his stats. The Divine Pill Absorption Quest remains active, and his survival is uncertain.
- Taekyung’s iron spear was cut to less than half its length; he learned Pung Yang’s attack pattern before the final exchange.
- Lee Seowol and nine other surviving Mount Heng Sword Sect martial artists began a sacrificial last stand to protect Taekyung and Mukyung; their fate is unresolved.
- Taekyung’s Unnamed Sword destroyed Pung Yang’s Body-Protecting Qi at the endpoint. Taekyung’s and Pung Yang’s final conditions, and whether either survives, remain unresolved.
- The Peak Quest’s Lunar New Year invitation to the Jin Family remains the governing objective.

## Translation Decisions

- Retain **Peak**, **early Peak**, **First Rate**, **Red Wind Band**, **Sect Leader**, **Taiyuan Jin Family**, **Scorching Yang Qi**, and **Body-Protecting Qi**.
- Render **잠력단** as **Temporary Strength Pill**.
- Render **적혈십이도** as **Crimson Blood Twelve Sabers**, distinct from **Crimson Blood Twelve Swords**.
- Render **열화신단** as **Blazing Flame Divine Pill** and **영단 흡수** as **Divine Pill Absorption**.
- Render **만년한철** as **Ten-Thousand-Year Cold Iron** and **이름 없는 검** as **Unnamed Sword**.
- Render **내상** as **Internal Injury** and **중상** as **Severe Injury** in System notifications.
- Render **일 식경** as **one meal’s time** in this passage.
- Retain **Narye tagon** with a footnote explaining its lazy-donkey imagery; render **격산타우** as **Striking the Ox Across the Mountain** with a footnote explaining force through an obstacle.

### Prior accepted reading-copy tails

#### Chapter 119 tail (verified mastered)

…
snapped back. The iron arrow Pung Yang had been holding was embedded in his forehead. “Senior Brother!” As the belated scream rang out, Pung Yang smiled. “I was just about out of throwing knives… Thank you, Sect Leader.” Lee Seowol bit her lip. “Go! Hurry!” I took a deep breath. I had already mapped out every step in my head. Jin Mukyung lay only about twenty zhang—sixty meters—away. If I drew up as much internal energy as possible and ran with him on my back, enduring the internal injuries, I could reach the fortress gate in no time. Pung Yang might catch up by then, but if they bought me just a little more time, I could survive. *I can go back.* Back to the Jin Family of Taiyuan, where Jin Wikyung was. Back home, where my mother and Hayeon were waiting. If I lived to fight another day, I was confident I could return far stronger—strong enough to make Pung Yang look insignificant. *That’s enough.* I drew another deep breath and turned toward Lee Seowol. “I’ll avenge you. I swear.” For the briefest instant, I thought she smiled. Perhaps I imagined it. The moment passed too quickly, and when I looked again, only firm resolve remained on her face. “Go. Hurry.” Her words were the starting signal. The Mount Heng martial artists charged with furious shouts, Lee Seowol at the front. *Yes. I have to go.* I drew up every last bit of internal energy in my body. Sharp pain tore through me as the internal injuries left by the Scorching Yang Qi sent dark-red blood flowing from my nose, but I endured it. It only had to last a moment. A very brief moment. *Inventory open. Equip spear.* The cool shaft settled into my grip. Then I pushed off the ground once. *Boom.* I shot forward like an arrow—no, faster than an arrow. Not toward Jin Mukyung. Toward Pung Yang. I could see his broad smile. “That’s more like it!” “Shut up, you son of a bitch.” “Ha-ha-ha-ha!” Pung Yang’s curved saber was larger than ever before. Brimming with red saber qi, it swung toward me. *Whoooosh!* The wind exploded, and even the air seemed to vanish. I gripped the iron spear hard enough to crush it. *Please. Just this once.* I poured all fifteen years of my internal energy into the spear. Drawing my shoulder and waist as far back as they would go, I sent everything I had flying forward. *One Annihilation.* *Rumble-rumble-rumble!* The immense saber qi collided with the vortex. A thunderous roar filled the world, as though the sky itself were splitting apart. Through the raging wind, I saw it clearly. *Kaboom!* The white vortex shattered into pieces before the red saber qi. The massive concentration of qi completely pulverized One Annihilation. Pung Yang whispered with an ecstatic expression, “This is as far as you go.” The next instant, Pung Yang’s internal energy surged along the spear and slammed into me. *Boom!* Blinding pain and ringing ears rolled over me like waves. *Ding.* > **System** > - You have suffered **Internal Injury**! Your condition is extremely serious! > - **Scorching Yang Qi** is running wild! > - You have suffered a **Severe Injury**! All stats have dropped significantly! The System notifications rang out one after another, mingling with the Mount Heng martial artists’ shouts, Lee Seowol’s scream, and Pung Yang’s laughter. *It’s over.* The instant my legs gave out despite my will, a powerful hand clamped around my throat. “Guh. Guhh.” “That was fairly impressive. If I’d been even a moment slower, you might have won.” Pung Yang bared his teeth in a grin. The red light in his eyes was slowly fading. *Damn it. I was so damn close.* I wanted to say it aloud, but my mouth was full of blood, making even that difficult. “I swore by the gods of heaven and earth, didn’t I? I swore I’d pull out your tongue.” Had he said that? By now, I could barely remember who I was. Pung Yang pried open my mouth with his other hand. His rough fingers seized my blood-soaked tongue and pulled. “Ghh…” “When you were running that mouth, didn’t you know this would happen? Huh?” “Ghaa… hahahaa.” “Hahaha! What the hell are you babbling about? Shall I let you say your last words?” Pung Yang laughed heartily and released my tongue. Only then could I speak. I swallowed the blood in my mouth and said, “Salty.” “What?” Damn salty. “What kind of bullshit is that?” *What do you think?* *I’m saying the taste of your fingers brought me back to my senses a little.* Half-conscious, I muttered, *Inventory open. Summon anything.* *Ding.* > **System** > - No item named **Anything** can be found. The oldest item stored in your inventory will be summoned first. > - The **Unnamed Sword** has been summoned. *The Unnamed Sword? What was that again?* *Whatever.* I gathered the last of my strength and thrust the sword in my hand at Pung Yang’s chest, shrouded in Body-Protecting Qi. It was a futile last-ditch attack with an obvious conclusion. *Damn Body-Protecting Qi.* But this was enough. I had no regrets left. It was at that moment, as my head slowly drooped— *Shnk!* *Ding.* > **System** > - The **Unnamed Sword** has satisfied a specific condition. > - **Ten-Thousand-Year Cold Iron** has destroyed **Body-Protecting Qi**. …Huh?

#### Chapter 120 tail (verified mastered)

…
*Nine parts luck and one part qi* was much more appropriate.[^1] *Though I’m not sure this really counts as good luck.* I slowly looked around. A graveyard of weapons stood with their hilts buried in the ground. Some people had died with their faces planted in pools of blood. Others stared wide-eyed at the sky as dawn began to break. There were hundreds of corpses like that. “There’s a survivor here!” “Chunsam! Wake up!” Amid that horrific scene, the martial artists of the Mount Heng Sword Sect moved tirelessly. As I watched them rescue the few survivors with disciplined efficiency, I was suddenly seized by an inexplicable sense of wrongness. *What is it?* It felt like I’d forgotten something important… Just as I was frowning, one of the corpses that had been lying motionless sat up. “Guuuuuh.” “Oh.” Right. Good to see you, Mukyung. * * * By the time the two-shichen search was over, Lee Seowol was soaked in blood. “How many survivors?” “Twenty-five, including you, Sect Leader.” “How many did you say?” “Twenty-five. Five of them probably won’t make it through today.” Both Lee Seowol, who had asked the question, and the martial artist who answered it fell silent. The Mount Heng Sword Sect, which had once divided Shanxi Province with the Jin Family of Taiyuan, no longer existed. All that remained were the wounded and a young Sect Leader who wasn’t even twenty years old. *If I had abandoned this place and fled, if I had accepted Pung Yang’s marriage proposal from the beginning, could I have saved them?* Regret was always futile. But Lee Seowol had to regret. Although few remained, she was still the Sect Leader of a sect. Only by agonizing over her mistakes and regretting them to the bone could she avoid making the same mistakes again. That was her atonement to those who had died today and her effort on behalf of those who remained. *The Mount Heng Sword Sect will survive. If only for those who gave their lives for our sect.* Lee Seowol clenched her fist. Her fingernails, broken from drawing the bowstring, dug into her flesh. Blood seeped out, but she felt no pain. “What about the others?” “They’re all in the main hall. A woman from the Jin Family of Taiyuan knows a fair amount about medicine and is treating the wounded, but…” The martial artist’s expression darkened. It was proof of just how bad the condition of some of the wounded was. Lee Seowol asked no more questions and headed toward the main hall. *We haven’t even had time to collect ourselves, and already I’m sending them off again.* Unbearable fatigue pressed down on her entire body, but she held on through sheer willpower. At the very least, she had to be there for their final moments. *Creeeeak.* When Lee Seowol entered the main hall, the people from the Jin Family of Taiyuan were nowhere in sight. The wounded lying on the floor immediately caught her eye. The Tiger of Mount Heng, Cheol Mubaek, and more than a dozen martial artists noticed her and called out. “Ah, Seowol. You’ve come?” “You’re here, Sect Leader!” “We greet you, Sect Leader!” “…?” Was it just her imagination? For people on the verge of death, they seemed strangely full of energy. After staring at them in silence for a while, Lee Seowol realized what that energy meant. “A final rally…” Only then did she see the dark shadow of death hanging over their faces. Just as she hurriedly turned away to hold back her tears— *Bang!* Lee Seowol staggered after striking her forehead against something solid. As she began to fall, a large, firm hand caught her by the shoulder. “Oh, careful there. Are you all right?” “Ah, yes.” “Then we’re good.” Jin Taekyung looked down at Lee Seowol and let out a short laugh. * * * *Some final rally.* I barely held back a snort. Cheol Mubaek and the other wounded were all recovering vigorously. Of course, Jin Mukyung was no exception. *What would they have done without me?* More precisely, if not for the Quest rewards, half of them might have needed funerals. The thirty **Superior Wound Medicines** and thirty **Ten-Year He Shouwu** I’d received as rewards were remarkably effective at treating external wounds and Internal Injuries. *I did consider saving them for an emergency…* But I wasn’t heartless enough to ignore people dying right in front of me. Of course, the sheer quantity had played a part too. “Aren’t you coming in?” “What?” “If you’re not going in, I’ll go in first.” I was about to walk past Lee Seowol, who was standing there in a daze, when I suddenly remembered what I’d forgotten. *Wait. Where did I put that?* “Ah, here it is.” I pretended to rummage through my robes and pulled a bamboo slip from my Inventory. “Here. It’s from my hyung… no, from the Lesser Family Head.” Lee Seowol accepted the bamboo slip with a bewildered expression. The instant she took it, a System notification rang out. *Ding.* > **System** > - Invitation delivery complete. > - Quest **Yesterday’s Enemy, Today’s Ally** completed! Invitation delivery. If I had to do that twice, someone was going to die. [^1]: A playful variation on the Korean saying *seven parts luck, three parts skill*, replacing skill with *qi* and shifting the balance even further toward luck.

## Korean source

```text
＃121화



시체가 산을 이루고 피가 강이 되어 흐를 정도로 치열한 전투였으나 항산검문의 건축물들은 대부분 멀쩡하게 그 형태를 유지하고 있었다. 지금 이 전각처럼.

나는 의자에 쓰러지듯이 몸을 기댔다.

“으, 죽겠다.”

지금 같은 큰 전투를 치른 후에는 늘 피로가 뒤따른다.

몸의 피로야 레벨 업으로 회복할 수 있다지만 정신적인 피로까지는 어쩌지 못하는 법이니까.

오늘처럼 죽음의 문턱을 오고 간 뒤라면 훨씬 더하다.

‘진짜 위험했다.’

조필, 대장로, 풍양.

절정 고수라는 놈들과 엮여서 좋은 꼴을 본 적이 없다. 목숨이 다섯 개쯤 있으면 좋겠다는 생각이 들 때가 한두 번이 아니니까.

“조장님, 고생하셨습니다.”

“오냐.”

“어휴, 어깨가 심하게 뭉치셨네요.”

혁무진이 살살거리며 다가와 어깨를 주물렀다.

외부에서 철무백을 지키던 월화와 혁무진은 일이 어느 정도 마무리된 생존자 수색 작업 때 합류했다.

“제가 있었으면 풍양 그놈을 아주 확 그냥, 아시죠?”

“그럼, 당연히 알지. 확 그냥 죽어 버렸을 거라는 거.”

“…….”

“뭐, 인마. 좀 더 세게 주물러 봐.”

혁무진은 구시렁거리면서도 힘을 줘 내 어깨를 꾹꾹 주물렀다.

“진무경, 아니 둘째 형은?”

“이미 따로 모셨습니다. 의원들 말로는 걱정 없을 거라더군요. 다른 부상자들도 빠르게 회복 중이랍니다.”

“그래? 그럼 다행이고.”

“돌팔이들 아닐까요? 이공자님도 그렇고, 철무백 대협도 제법 큰 내상을 입으신 거로 아는데.”

“하오문에서 보낸 사람들이잖아. 실력을 믿어 보자고.”

사실 내가 믿는 건 의원들이 아니라 아이템의 효능이다.

어지간한 상처는 며칠 안에 아물게 해 준다는 [뛰어난 금창약]과 내상 치유에 탁월한 효과가 있는 [십년하수오]가 아니었다면 저들 중 몇 명은 벌써 요단강 건넜을 거다.

‘최소한의 응급 처치는 했으니 나머진 의원들이 알아서 해 주겠지.’

하오문, 아니 월화는 우리도 모르는 새에 발 빠르게 움직였다. 며칠 전 사당에서 수하를 돌려보내면서 인근에 있는 지부에 소집령을 내렸단다.

모든 전투가 끝나고 반나절 후에 도착한 하오문의 지원군은 곧장 뒷수습을 시작했다.

‘모두가 앞만 바라볼 때 뒤를 생각한 거지.’

하오문의 지원군은 전투가 아닌 구호를 목적으로 꾸려져 있었다.

의원은 물론이고, 숙수에 일꾼들까지 데려왔을 정도니 그 선견지명과 준비성 하나만큼은 혀를 내두를 지경이다.

‘역시 보통 사람이 아니야.’

하오문은 천하 어디에나 있는 정보 단체인 동시에 무림 문파라고 했다.

그 정도 규모의 문파에서 20대 중후반의 나이에 지부장이라는 자리를 맡은 월화도 결코 평범한 사람은 아닐 거다.

‘그러고 보니 월화라는 이름도 가명이지.’

기감으로 파악했던 월화의 실제 이름은 은소월이었다. 굳이 우리에게 이름을 숨기는 이유는 글쎄, 첩보 영화의 코드네임과 비슷한 거 아닐까 싶다.

확실한 건 저 정도 수완가를 적으로 돌리면 피곤해진다는 사실이다.

‘너무 가까이는 말고 적당히 선을 지키면서. 그래, 그 정도가 딱 적당해.’

다행히 그리 어렵지 않은 일이다. 월화는 처음부터 내게 이유 모를 호의와 호기심을 갖고 있었으니까.

그것이 순수한 감정인지, 베테랑 정보 상인으로서의 호기심인지는 좀 더 지켜봐야 알 것 같다.

“무진아.”

“더 세게 주무를까요?”

“아니, 그거 말고. 월화 소저에 대해 어떻게 생각하냐?”

“예쁘죠.”

“그리고?”

곰곰이 생각하던 혁무진이 대답했다.

“엄청 예쁘죠.”

“……어깨 말고 팔뚝 주물러.”

저 자식한테 뭘 물어본 내가 병신이지.

혁무진이 상처받은 얼굴로 뭐라 대꾸하려던 그때, 가벼운 발소리가 서서히 가까워져 오더니 문 앞에서 멈췄다.

‘월화?’

아니다. 문밖에서 느껴지는 기는 월화에 비해 턱없이 작고 약했다. 잠깐의 침묵 끝에 뜻밖의 손님이 입을 열었다.

“진 공자, 들어가도 될까요?”

맑고 또렷한 목소리. 이소월이었다.



* * *



혁무진이 전각을 나가자 이소월과 단둘이 남겨졌다. 나는 창밖으로 슬슬 어두워지는 하늘을 바라보며 괜한 헛기침을 내뱉었다.

“큼. 커흠.”

이 시간에 여자, 그것도 기가 막힌 미인과 단둘이 마주 보고 있으려니까 고역이 따로 없다.

심지어 얼마 전까지만 해도 철천지원수처럼 싸우던 항산검문의 문주 아닌가.

새 술은 새 부대에 담는다고 하지만 그녀는 태원진가를 무너뜨리려던 이천백의 하나뿐인 딸이며 나와는 추문(醜聞)으로 엮인 사이다.

‘이거 도대체 무슨 말을 해야 하나.’

삼가 고인의 명복을 빕니다? 아냐, 이건 너무 분위기가 무거워져. 얼마 전에 일가(一家)를 떠나보낸 거로도 모자라 풍양과의 전투에서 수하의 대부분을 잃은 그녀다.

나는 고민 끝에 입을 뗐다.

“식사는 하셨어요?”

“…….”

“힘드신 일 겪으신 건 알지만 이럴 때일수록 속이 든든해야…… 죄송합니다.”

시바, 그냥 입 다물고 있을걸.

마음속 깊이 후회하고 있을 때 이소월이 자리에서 일어나 내게 절을 올렸다.

“항산검문의 이소월이 은공께 인사 올립니다.”

말릴 새도 없이 벌어진 일. 당황한 나는 황급히 그녀를 일으켜 세웠다.

은공이라니. 맞는 말이지만 낯간지럽다.

“아이고, 왜 이러세요. 은공은 무슨.”

“아닙니다. 사람이라면 응당 은혜를 입고 감사할 줄 알아야 하는 법. 은공께서는 부디 저를 부끄럽게 만들지 말아 주세요.”

워낙 결의에 찬 말투라 더 이상 말릴 수도 없다.

‘틀린 말도 아니고.’

나와 진무경이 아니었다면 항산검문은 오늘부로 문 닫았을 거다. 큰절이 아니라 우리의 동상을 세워도 부족하긴 하지.

오늘 날짜를 ‘산서잠룡 오신 날’로 지정해서 매년 항산검문의 공휴일로…… 이건 너무 나갔지만 아무튼.

“이제 진정하고 자리에 앉으세요.”

“은공의 말씀을 따르겠습니다.”

“그 은공 소리는 안 하면 안 될까요?”

“예, 은공.”

미치겠네. 침착한 얼굴로 대답한 이소월이 자리에 앉고 나서야 비로소 나를 찾아온 이유를 들을 수 있었다.

“서신에 대한 답을 들려 드리러 왔어요.”

“서신? 아.”

초대장에 관한 이야기다. 곧 다가오는 새해 첫날 태원진가에서 밥 한 끼 하자는, 정중한 초대의 탈을 쓴 소집령.

태원진가가 산서 무림을 틀어쥔 지금, 초대에 응하지 않는 문파는 앞으로의 행보가 재미없을 거라는 사실은 불 보듯 뻔하다.

그건 간신히 궤멸을 면한 항산검문도 예외가 아니다.

“그래서 대답은요?”

“귀문의 제의에 기쁘게 응하겠습니다.”

충분히 예상했던 대답이다.

그러나 이소월은 거기서 멈추지 않고 말을 이어 나갔다.

“더불어 지난 일에 대한 사죄로 본 문이 갖고 있는 모든 권리를 태원진가에게 양도하겠습니다.”

“권리?”

“네. 본 문의 차지하고 있는 영역에 대한 일체의 권리 모두를요.”

그 말인즉슨, 산서 북부를 통째로 태원진가에 넘기겠다는 뜻인데…….

‘이렇게까지?’

항산검문이 태원진가에게 머리를 숙였다는 건 이미 기정사실이다. 그 과정에서 진위경이 배상금 명목으로 상당히 많은 걸 요구하겠지만 그렇다고 완전히 통째로 집어삼키지는 못한다.

월화도 지난 대화에서 비슷한 얘기를 했었고.

‘그런데 알아서 떠먹여 주네.’

은공, 은공 하더니 아주 헛말은 아닌 모양이다.

그래. 역시 감사라는 건 말로 끝내서는 안 되는 법이지. 음.

“감사합니다. 저희 큰형님이 흡족해하시겠네요.”

“거기에 더해서.”

뭐야, 아직 안 끝났어?

이소월이 품에서 꺼내 들어 내게 내민 것은 세 권의 책이었다. 나는 겉표지에 적힌 제목을 천천히 읽어 내려갔다.

“혈랑검법, 혈랑보법. 그리고.”

“수라멸권(修羅滅拳). 검법과 보법은 아버님께서 직접 창안하신 무공이고, 수라멸권은 철 숙부의 비전절기예요. 하나같이 빼어난 절정 무공이죠.”

“절정 무공…….”

마른침이 절로 넘어간다.

무림에서 뼈저리게 깨달은 것 중 하나가 바로 무공의 중요성이다. 시스템을 이용해서 그 부족함을 간신히 메꾸고 있는 나도 이럴진대, 다른 평범한 무림인들에게는 더 말할 것도 없다.

무인들에게 있어 훌륭한 절정 무공은 값어치를 매길 수 없는 무가지보(無價之寶)인 것이다.

‘산서 북부에 대한 권리, 그 이상.’

항산검문이 소유한 권리가 나무의 가지라면 지금 눈앞에 놓인 세 권의 비급은 뿌리다.

이소월은 지금 아버지의 유산이자 항산검문이 가진 가장 값진 것들을 저울에 올려놓은 것이다.

“이것도 선물입니까?”

“아뇨, 이건 거래예요.”

역시. 그럴 줄 알았지.

거래라. 진위경이라면 무슨 수를 써서라도 그 거래를 받아들일 것이다. 자그마치 세 개의 절정 무공이 걸려 있으니까.

‘도대체 뭘 요구하려는 거지?’

재물? 안전 보장? 아니면 또 다른 무언가?

현재 이소월은, 아니 항산검문은 절박하다 못해 절망적인 상황이다. 아무리 무공들을 헐값에 내놓았다 한들 그 또한 어려운 요구일 것이 분명했다. 나는 슬쩍 발을 뺐다.

“무슨 거래일지 궁금하긴 한데…… 아실지는 모르겠지만 저한텐 그 정도 권한이 없어서요.”

이소월이 호수처럼 맑은 눈동자로 나를 물끄러미 응시했다.

“그런가요?”

“네, 딱히 직책도 없고. 나중에 큰형님이랑 따로 상의해 보시는 게 맞는 것 같네요.”

“제 생각은 은공과 다른데요.”

“예?”

“은공께서 충분히 결정하실 수 있는 거래예요. 물론 많은 이야기가 오고 가야겠지만.”

“세 개의 절정 무공과 바꿀 만한 거래라…… 그럼 저희 쪽에서는 뭘 줘야 하는 거죠?”

“사람이요.”

“사람?”

순간 이소월의 입가에 미소가 스쳤다.

두 번째로 보는 그녀의 웃음이었고, 이번에는 결코 착각이 아니었다.

“저와 혼인해 주세요.”



* * *



“그럼 이만.”

전각 앞마당에 서성이던 혁무진은 등 뒤에서 들려오는 여인의 목소리에 돌아섰다. 보는 것만으로도 가슴 한구석이 간질거리는 미녀가 전각의 계단을 내려오는 중이었다.

‘허어, 절색이로다.’

수십 보(步)는 떨어져 있건만, 한겨울 찬 바람에 꽃향기가 섞여 불어오는 것 같기도 했다.

‘하여간 우리 조장은 복도 많아.’

잘생긴 얼굴, 자타 공인 산서제일가(山西第一家)인 태원진가의 막내 도련님인 데다가 무공도 뛰어나다.

월화와 함께 있을 때는 선남선녀라는 말이 딱 어울렸다.

거기에 이제는 항산검문의 문주까지 추가되다니.

혁무진은 저 멀리 사라지는 이소월의 뒷모습을 보며 한숨을 푹 내쉬었다.

‘잠깐이지만 사랑했소, 이 소저.’

다시 전각으로 돌아간 혁무진이 발견한 것은 반쯤 넋이 나가 있는 진태경이었다.

“조장, 왜 그러세요?”

“…….”

“조장. 정신 좀 차려 보세요!”

어깨를 붙잡고 흔들자 그제야 풀려 있던 눈동자가 또렷해졌다. 혁무진이 걱정스러운 얼굴로 물었다.

“무슨 일 있었습니까? 갑자기 왜 그러세요?”

꿀꺽. 마른침을 삼킨 진태경이 간신히 입을 뗐다.

“무진아.”

“예.”

“이소월, 몇 살인지 아냐?”

“이소월이 뭡니까, 이소월이. 문주나 소저라고 해야죠.”

“고(故) 혁무진이라고 불리기 싫으면 닥치고 대답해.”

“……몇 살이었더라? 슬슬 혼인할 나이긴 했던 것 같은데.”

곰곰이 생각하던 혁무진이 이마를 탁 쳤다.

“아, 생각났어요.”

“며, 몇 살인데?”

“열일곱이요.”

진태경이 입을 딱 벌렸다.

“시발, 급식이었어?”
```

## Current accepted English baseline

```markdown
# Chapter 121

It had been a fierce battle—fierce enough for corpses to pile up into mountains and blood to flow like rivers—yet most of the Mount Heng Sword Sect’s buildings remained standing, largely undamaged.

Like this pavilion, for instance.

I collapsed into a chair and leaned back.

“Ugh. I’m dying.”

A major battle like the one we had just fought always left exhaustion in its wake.

Leveling up could restore the fatigue in my body, but there was nothing I could do about mental exhaustion.

And after skirting the brink of death like I had today, it was even worse.

*That was seriously dangerous.*

Jopil. The Head Elder. Pung Yang.

I had never come out ahead after getting tangled up with Peak masters. More than once, I had wished I had about five lives.

“Squad Leader, you worked hard.”

“Yeah, yeah.”

“Oh, your shoulders are really tense.”

Hyuk Mujin approached with an ingratiating smile and began massaging my shoulders.

Wolhwa and Hyuk Mujin had been protecting Cheol Mubaek outside before joining the survivor search once things had more or less settled down.

“If I’d been there, I would’ve really laid into that bastard Pung Yang. You know what I mean, right?”

“Of course I do. You would’ve gotten yourself killed on the spot.”

“……”

“What? Come on, massage a little harder.”

Hyuk Mujin grumbled, but he put more strength into his hands and kneaded my shoulders.

“What about Jin Mukyung? I mean, my second brother?”

“We’ve already moved him elsewhere. The physicians said there’s no need to worry. They also said the other wounded are recovering quickly.”

“Really? That’s a relief.”

“Aren’t they quacks? I heard the Second Young Master and Great Hero Cheol Mubaek both suffered fairly serious Internal Injuries.”

“They were sent by the Lower District Sect. Let’s trust their skills.”

In truth, it wasn’t the physicians I trusted. It was the efficacy of the Items.

If not for the **Superior Wound Medicine**, which could heal most wounds within a few days, and the **Ten-Year He Shouwu**, which was exceptionally effective at treating Internal Injuries, some of them would already have crossed the River Jordan.

*I’ve given them the minimum emergency treatment. The physicians can take care of the rest.*

The Lower District Sect—or rather, Wolhwa—had moved quickly without any of us realizing it. Several days ago, when she sent one of her subordinates back from the shrine, she had apparently issued a mobilization order to a nearby branch.

The Lower District Sect’s support force arrived half a day after the battle ended and immediately began dealing with the aftermath.

*While everyone else was looking ahead, she was thinking about what came after.*

The Lower District Sect’s support force had been organized for rescue work, not combat.

They had brought not only physicians, but cooks and laborers as well. Their foresight and preparation were enough to make me whistle in admiration.

*She really isn’t an ordinary person.*

The Lower District Sect was an information organization found throughout the land, but it was also a Murim sect.

And Wolhwa, who had taken on the position of Branch Leader in a sect of that size while still in her mid-to-late twenties, was certainly no ordinary person.

*Come to think of it, Wolhwa isn’t even her real name.*

The name I had sensed through Qi Sense was Eun Sowol. As for why she had gone out of her way to hide her name from us, I supposed it was something like a code name in a spy movie.

One thing was certain: making an enemy of someone that capable would be exhausting.

*Don’t get too close. Keep a reasonable distance and stay within proper boundaries. Yes, that sounds about right.*

Fortunately, that wouldn’t be too difficult. Wolhwa had shown me inexplicable goodwill and curiosity from the very beginning.

Whether those were genuine feelings or simply the curiosity of a veteran information merchant was something I would have to watch a little longer to determine.

“Mujin-ah.”

“Should I massage harder?”

“No, not that. What do you think about Young Lady Wolhwa?”

“She’s pretty.”

“And?”

Hyuk Mujin thought hard before answering.

“She’s extremely pretty.”

“……”

“Massage my forearms instead of my shoulders.”

I was the idiot for asking that guy anything.

Hyuk Mujin looked wounded and was about to say something when light footsteps slowly approached and stopped in front of the door.

*Wolhwa?*

No. The qi I sensed outside the door was far weaker and smaller than Wolhwa’s.

After a brief silence, an unexpected guest spoke.

“Young Master Jin, may I come in?”

Her voice was clear and distinct.

It was Lee Seowol.

* * *

Once Hyuk Mujin left the pavilion, I was alone with Lee Seowol.

I gazed out the window at the sky slowly darkening and gave a pointless cough.

“Ahem. Ahem.”

Being alone with a woman at this hour—especially a stunning beauty—was a trial in itself.

To make matters worse, she was the Sect Leader of the Mount Heng Sword Sect, which I had been fighting like a sworn enemy only a short while ago.

They said new wine belonged in new wineskins, but she was the only daughter of Lee Cheonbaek, the man who had tried to bring down the Jin Family of Taiyuan, and she and I were already connected by a scandal.

*What the hell am I supposed to say?*

*May the deceased rest in peace?*

No. That would make the atmosphere far too heavy. It wasn’t enough that she had lost her family recently—she had also lost most of her subordinates in the battle against Pung Yang.

After agonizing over it, I finally opened my mouth.

“Have you eaten?”

“……”

“I know you’ve been through something difficult, but it’s even more important to keep your strength up at times like this, so……”

I stopped myself.

“Sorry.”

*Damn it. I should’ve just kept my mouth shut.*

As I was regretting my words from the bottom of my heart, Lee Seowol rose from her seat and bowed deeply to me.

“Lee Seowol of the Mount Heng Sword Sect pays her respects to her benefactor.”

It happened before I had a chance to stop her.

Flustered, I hurriedly helped her back to her feet.

*Benefactor?*

It was accurate, but hearing it made me cringe.

“Oh, come on. What are you doing? You don’t have to call me your benefactor.”

“No. A person ought to receive kindness and know how to be grateful for it. Please do not make me feel ashamed, Benefactor.”

Her tone was so resolute that I couldn’t stop her anymore.

*She’s not wrong.*

If not for Jin Mukyung and me, the Mount Heng Sword Sect would have shut its doors today. A deep bow wasn’t enough. They could have erected statues of us and it still wouldn’t have been sufficient.

Maybe they could designate today as the day the Sleeping Dragon of Shanxi came to visit and make it an annual holiday for the Mount Heng Sword Sect—

*That might be taking things too far.*

“Now, calm down and sit.”

“I will follow my benefactor’s instructions.”

“Could you not call me that?”

“Yes, Benefactor.”

*This is driving me crazy.*

Only after Lee Seowol answered with a calm expression and sat down was I finally able to hear why she had come to see me.

“I came to give you my answer regarding the letter.”

“The letter? Oh.”

She was talking about the invitation.

The polite invitation to have a meal at the Jin Family of Taiyuan on New Year’s Day, which was fast approaching—a summons disguised as a dinner invitation.

Now that the Jin Family of Taiyuan had Shanxi Murim firmly in its grasp, it was obvious that things would not go well for any sect that refused the invitation.

The Mount Heng Sword Sect, which had only barely escaped annihilation, was no exception.

“So what’s your answer?”

“We will gladly accept your sect’s proposal.”

It was the answer I had expected.

But Lee Seowol didn’t stop there. She continued speaking.

“Additionally, as an apology for what happened, I will transfer all the rights held by our sect to the Jin Family of Taiyuan.”

“Rights?”

“Yes. All rights to the territory currently occupied by our sect.”

In other words, she was saying that she would hand over all of northern Shanxi to the Jin Family of Taiyuan.

*She’s going this far?*

The fact that the Mount Heng Sword Sect had bowed its head to the Jin Family of Taiyuan was already a given. Jin Wikyung would demand a great deal in compensation, but even he couldn’t completely swallow the sect whole.

Wolhwa had said something similar during our previous conversation.

*And now she’s serving it up to us without even being asked.*

After calling me her benefactor over and over, it seemed she hadn’t just been paying lip service.

Yes. Gratitude shouldn’t end with words. Hm.

“Thank you. My eldest brother will be pleased.”

“There’s more.”

*What? She isn’t finished yet?*

Lee Seowol took three books from inside her robes and held them out to me.

I slowly read the titles written on their covers.

“Blood Wolf Sword Technique, Blood Wolf Footwork. And……”

“Shura Annihilating Fist. The sword technique and footwork technique were created by my father himself. The Shura Annihilating Fist is Uncle Cheol’s secret ultimate technique. Every one of them is an outstanding Peak martial art.”

“Peak martial arts……”

I swallowed hard.

One of the things I had learned painfully in the Murim was the importance of martial arts. Even I was barely able to make up for my deficiencies by relying on the System. For ordinary martial artists, it went without saying.

To martial artists, an excellent Peak martial art was a priceless treasure.

*These are worth more than the rights to northern Shanxi.*

If the rights to northern Shanxi were the branches of a tree, then the three martial arts manuals lying before me were its roots.

Lee Seowol had placed her father’s legacy—the most valuable things possessed by the Mount Heng Sword Sect—on the scale.

“Is this a gift too?”

“No. This is a transaction.”

*I knew it.*

A transaction.

If it was Jin Wikyung, he would accept the deal by any means necessary. Three Peak martial arts were at stake, after all.

*What on earth is she going to demand?*

Wealth? A guarantee of safety? Or something else entirely?

Lee Seowol—or rather, the Mount Heng Sword Sect—was in a situation so desperate that it had nearly become hopeless. Even if they were offering their martial arts at a bargain price, whatever they wanted in return was certain to be a difficult demand.

I cautiously backed away.

“I am curious what kind of transaction you have in mind, but I don’t know if you’re aware of this—I don’t have that kind of authority.”

Lee Seowol gazed steadily at me with eyes as clear as a lake.

“Is that so?”

“Yes. I don’t have a particular position, either. I think it would be best for you to discuss this separately with my eldest brother later.”

“My thoughts differ from yours, Benefactor.”

“Excuse me?”

“This is a transaction you are fully capable of deciding. Of course, there would need to be many discussions.”

“A transaction worth trading three Peak martial arts for…… Then what would our side have to give?”

“A person.”

“A person?”

For an instant, a smile flickered across Lee Seowol’s lips.

It was the second time I had seen her smile, and this time, I knew I hadn’t imagined it.

“Please marry me.”

* * *

“Well, I’ll be going.”

Hyuk Mujin, who had been pacing around the pavilion’s front courtyard, turned at the sound of the woman’s voice behind him.

A beauty who made one’s chest tickle just by looking at her was descending the pavilion steps.

*Good heavens. She’s breathtaking.*

Though she was dozens of paces away, it almost seemed as if the cold midwinter wind carried the scent of flowers with it.

*Our squad leader sure is lucky.*

He had a handsome face, was the youngest Young Master of the Jin Family of Taiyuan—the universally acknowledged First Family of Shanxi—and possessed excellent martial arts.

When he was with Wolhwa, the words *a celestial beauty and a handsome man* fit them perfectly.

And now the Sect Leader of the Mount Heng Sword Sect had been added to the list.

Hyuk Mujin let out a deep sigh as he watched Lee Seowol’s back disappear into the distance.

*I loved you for a moment, Young Lady Lee.*

When Hyuk Mujin returned to the pavilion, he found Jin Taekyung sitting there half out of his mind.

“Squad Leader, what’s wrong?”

“……”

“Squad Leader. Please come to your senses!”

Only after Hyuk Mujin grabbed him by the shoulders and shook him did the unfocused eyes finally clear.

Hyuk Mujin asked with a worried expression.

“Did something happen? Why are you suddenly acting like this?”

*Gulp.*

Jin Taekyung swallowed hard and barely managed to open his mouth.

“Mujin.”

“Yes.”

“Do you know how old Lee Seowol is?”

“What do you mean, ‘Lee Seowol’? You should call her Sect Leader or Young Lady.”

“If you don’t want me to start calling you the late Hyuk Mujin, shut up and answer me.”

“……”

Hyuk Mujin thought for a moment.

“How old was she again? I think she was about the age when people started getting married.”

He suddenly slapped his forehead.

“Oh, I remember.”

“H-How old is she?”

“Seventeen.”

Jin Taekyung’s mouth fell open.

“Fuck, she was still a high schooler?”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 121`.

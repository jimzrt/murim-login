# Master Edit Task — Chapter 122

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
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 검법     | **sword technique**                              |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 마적     | **mounted bandits**                              |                                                       |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 문주     | **Sect Leader**                              |
| 지부장    | **Branch Leader**                            |
| 사부     | **Master**                                   |
| 큰형     | **eldest brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 공자      | **Young Master**                                                |
| 대사      | **Master** for a senior Buddhist monk                           |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 정양지부장 | **Jeongyang Branch Leader** | Leader of the Lower District Sect's Jeongyang Branch. |
| 혼주지부장 | **Honju Branch Leader** | Leader of the Lower District Sect's Honju Branch. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
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
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 월화 | 혼주지부장 | chief_branch_leader_to_subordinate_branch_leader | Honju Branch Leader | formal-commanding | Wolhwa addresses him by branch title while directing rumor operations. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 이소월 | young_martial_artist_to_allied_sect_leader | Young Lady Lee | formal-polite | Taekyung uses 이 소저 while greeting Seowol at the banquet. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 당장은 | polysemy | Right away / for now / at the moment; not the broader “anytime soon.” | anytime soon |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 큰형 | kinship | Eldest older brother, not a generic older brother. | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

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

#### Chapter 120 tail (verified mastered)

…
*Nine parts luck and one part qi* was much more appropriate.[^1] *Though I’m not sure this really counts as good luck.* I slowly looked around. A graveyard of weapons stood with their hilts buried in the ground. Some people had died with their faces planted in pools of blood. Others stared wide-eyed at the sky as dawn began to break. There were hundreds of corpses like that. “There’s a survivor here!” “Chunsam! Wake up!” Amid that horrific scene, the martial artists of the Mount Heng Sword Sect moved tirelessly. As I watched them rescue the few survivors with disciplined efficiency, I was suddenly seized by an inexplicable sense of wrongness. *What is it?* It felt like I’d forgotten something important… Just as I was frowning, one of the corpses that had been lying motionless sat up. “Guuuuuh.” “Oh.” Right. Good to see you, Mukyung. * * * By the time the two-shichen search was over, Lee Seowol was soaked in blood. “How many survivors?” “Twenty-five, including you, Sect Leader.” “How many did you say?” “Twenty-five. Five of them probably won’t make it through today.” Both Lee Seowol, who had asked the question, and the martial artist who answered it fell silent. The Mount Heng Sword Sect, which had once divided Shanxi Province with the Jin Family of Taiyuan, no longer existed. All that remained were the wounded and a young Sect Leader who wasn’t even twenty years old. *If I had abandoned this place and fled, if I had accepted Pung Yang’s marriage proposal from the beginning, could I have saved them?* Regret was always futile. But Lee Seowol had to regret. Although few remained, she was still the Sect Leader of a sect. Only by agonizing over her mistakes and regretting them to the bone could she avoid making the same mistakes again. That was her atonement to those who had died today and her effort on behalf of those who remained. *The Mount Heng Sword Sect will survive. If only for those who gave their lives for our sect.* Lee Seowol clenched her fist. Her fingernails, broken from drawing the bowstring, dug into her flesh. Blood seeped out, but she felt no pain. “What about the others?” “They’re all in the main hall. A woman from the Jin Family of Taiyuan knows a fair amount about medicine and is treating the wounded, but…” The martial artist’s expression darkened. It was proof of just how bad the condition of some of the wounded was. Lee Seowol asked no more questions and headed toward the main hall. *We haven’t even had time to collect ourselves, and already I’m sending them off again.* Unbearable fatigue pressed down on her entire body, but she held on through sheer willpower. At the very least, she had to be there for their final moments. *Creeeeak.* When Lee Seowol entered the main hall, the people from the Jin Family of Taiyuan were nowhere in sight. The wounded lying on the floor immediately caught her eye. The Tiger of Mount Heng, Cheol Mubaek, and more than a dozen martial artists noticed her and called out. “Ah, Seowol. You’ve come?” “You’re here, Sect Leader!” “We greet you, Sect Leader!” “…?” Was it just her imagination? For people on the verge of death, they seemed strangely full of energy. After staring at them in silence for a while, Lee Seowol realized what that energy meant. “A final rally…” Only then did she see the dark shadow of death hanging over their faces. Just as she hurriedly turned away to hold back her tears— *Bang!* Lee Seowol staggered after striking her forehead against something solid. As she began to fall, a large, firm hand caught her by the shoulder. “Oh, careful there. Are you all right?” “Ah, yes.” “Then we’re good.” Jin Taekyung looked down at Lee Seowol and let out a short laugh. * * * *Some final rally.* I barely held back a snort. Cheol Mubaek and the other wounded were all recovering vigorously. Of course, Jin Mukyung was no exception. *What would they have done without me?* More precisely, if not for the Quest rewards, half of them might have needed funerals. The thirty **Superior Wound Medicines** and thirty **Ten-Year He Shouwu** I’d received as rewards were remarkably effective at treating external wounds and Internal Injuries. *I did consider saving them for an emergency…* But I wasn’t heartless enough to ignore people dying right in front of me. Of course, the sheer quantity had played a part too. “Aren’t you coming in?” “What?” “If you’re not going in, I’ll go in first.” I was about to walk past Lee Seowol, who was standing there in a daze, when I suddenly remembered what I’d forgotten. *Wait. Where did I put that?* “Ah, here it is.” I pretended to rummage through my robes and pulled a bamboo slip from my Inventory. “Here. It’s from my hyung… no, from the Lesser Family Head.” Lee Seowol accepted the bamboo slip with a bewildered expression. The instant she took it, a System notification rang out. *Ding.* > **System** > - Invitation delivery complete. > - Quest **Yesterday’s Enemy, Today’s Ally** completed! Invitation delivery. If I had to do that twice, someone was going to die. [^1]: A playful variation on the Korean saying *seven parts luck, three parts skill*, replacing skill with *qi* and shifting the balance even further toward luck.

#### Chapter 121 tail (verified mastered)

…
there. She continued speaking. “Furthermore, as an apology for what happened, I will transfer every right held by our sect to the Jin Family of Taiyuan.” “Rights?” “Yes. All rights to the territory currently occupied by our sect.” In other words, she was saying that she would hand over all of northern Shanxi to the Jin Family of Taiyuan. *She’s going this far?* The fact that the Mount Heng Sword Sect had bowed its head to the Jin Family of Taiyuan was already a given. Jin Wikyung would demand a great deal in compensation, but even he couldn’t completely swallow the sect whole. Wolhwa had said something similar during our previous conversation. *And now she’s serving it up to us without even being asked.* After calling me her benefactor over and over, it seemed she hadn’t just been paying lip service. Right. Gratitude shouldn’t end with words. Hm. “Thank you. My eldest brother will be pleased.” “There’s more.” *What? She isn’t finished yet?* Lee Seowol took three books from inside her robes and held them out to me. I slowly read the titles on their covers. “Blood Wolf Sword Technique, Blood Wolf Footwork. And……” “Shura Annihilating Fist. The sword technique and footwork technique were created by my father himself. The Shura Annihilating Fist is Uncle Cheol’s secret ultimate technique. Every one of them is an outstanding Peak martial art.” “Peak martial arts…” I swallowed hard. One of the things I had learned painfully in the Murim was the importance of martial arts. Even I was barely able to make up for my deficiencies by relying on the System. For ordinary martial artists, it went without saying. To them, an outstanding Peak martial art was a priceless treasure. *These are worth more than the rights to northern Shanxi.* If those rights were the branches of a tree, the three martial arts manuals before me were its roots. Lee Seowol had placed her father’s legacy—the most valuable possessions of the Mount Heng Sword Sect—on the scales. “Is this a gift too?” “No. This is a transaction.” *I knew it.* A transaction. If it was Jin Wikyung, he would accept the deal by any means necessary. Three Peak martial arts were at stake, after all. *What on earth is she going to demand?* Wealth? A guarantee of safety? Or something else? Lee Seowol—or rather, the Mount Heng Sword Sect—was in a situation beyond desperate. Even if they were offering their martial arts at a bargain price, whatever they wanted in return was certain to be a difficult demand. I cautiously distanced myself from the matter. “I’m curious what kind of transaction this is, but I don’t know if you’re aware—I don’t have that kind of authority.” Lee Seowol gazed steadily at me with eyes as clear as a lake. “Is that so?” “Yes. I don’t have a particular position, either. I think it would be best for you to discuss this separately with my eldest brother later.” “My thoughts differ from yours, Benefactor.” “Excuse me?” “This is a transaction you are fully capable of deciding. Of course, there would need to be many discussions.” “A transaction worth trading three Peak martial arts for…… Then what would our side have to give?” “A person.” “A person?” For an instant, a smile flickered across Lee Seowol’s lips. It was the second time I had seen her smile, and this time, I knew I hadn’t imagined it. “Please marry me.” * * * “Well, I’ll be going.” Hyuk Mujin, who had been pacing around the pavilion’s front courtyard, turned at the sound of a woman’s voice behind him. A beauty who made his chest tickle just by looking at her was descending the pavilion steps. *Good heavens. She’s breathtaking.* Though she was dozens of paces away, it almost seemed as if the cold midwinter wind carried the scent of flowers. *Our squad leader sure is lucky.* He had a handsome face, was the youngest Young Master of the Jin Family of Taiyuan—the universally acknowledged foremost family in Shanxi—and possessed excellent martial arts. When he was with Wolhwa, the words *a celestial beauty and a handsome man* fit them perfectly. And now the Sect Leader of the Mount Heng Sword Sect had been added to the list. Hyuk Mujin let out a deep sigh as he watched Lee Seowol’s back disappear into the distance. *I loved you, however briefly, Young Lady Lee.* When Hyuk Mujin returned to the pavilion, he found Jin Taekyung sitting there half out of his mind. “Squad Leader, what’s wrong?” “……” “Squad Leader. Please come to your senses!” Only after Hyuk Mujin grabbed him by the shoulders and shook him did his unfocused eyes finally clear. Hyuk Mujin asked with a worried expression, “Did something happen? Why are you suddenly acting like this?” *Gulp.* Jin Taekyung swallowed hard and barely managed to open his mouth. “Mujin.” “Yes.” “Do you know how old Lee Seowol is?” “What do you mean, ‘Lee Seowol’? You should call her Sect Leader or Young Lady.” “Unless you want people calling you the late Hyuk Mujin, shut up and answer.” “……” Hyuk Mujin thought for a moment. “How old was she again? I think she was about the age when people started getting married.” He suddenly slapped his forehead. “Oh, I remember.” “H-How old is she?” “Seventeen.” Jin Taekyung’s mouth fell open. “Fuck, she was still a high schooler?”

## Korean source

```text
＃122화



정보를 전달함에 있어 중요한 것은 두 가지다. 신속과 정확.

그것을 위해 정보를 취급하는 문파인 하오문은 지부마다 촘촘한 정보망을 구성해 두었다.

월화는 그중 산서성에 설치된 삼십여 개 지부에 동원령을 내릴 수 있는 권한을 지니고 있었다.

“일은? 마무리했어?”

그녀의 물음에 멀끔한 인상의 중년인, 하오문 정양지부장이 대답했다.

“시신은 모두 분리해서 옮겨 두었습니다. 항산검문 측 생존자는 더 없었고, 마적 중에 숨이 붙어 있는 놈들이 있더군요.”

“얼마나?”

“정확히 마흔일곱입니다.”

“많이도 살았네. 그중에 몇이나 살릴 수 있어?”

“지금 보유한 약재로는 서른 정도가 한계입니다.”

“모두 다 살릴 필요는 없겠지.”

월화의 한마디에 정양 지부장이 고개를 숙였다.

“조치하겠습니다.”

그것으로 살아남은 마적들의 운명이 결정되었다.

중상을 입었다면 산더미처럼 쌓인 동료들의 곁으로 돌아갈 것이고, 경상을 입었다면 생명을 조금 더 연장시킬 수 있을 것이다.

물론 치료가 끝나는 즉시 광산이나 투기장의 노예로 팔려 가겠지만.

“다음. 혼주지부장?”

“저희 쪽도 문제없습니다.”

혼주지부장은 얼굴에 검상이 가득한 거한이었다. 그는 철사처럼 빳빳한 턱수염을 긁적이며 말을 이었다.

“사실 나설 필요도 없더구먼요. 풍양이 죽고 적풍단이 아작 났다는 걸 알았는지 근처에 얼씬도 안 합디다.”

“당장은 그걸로 충분해. 발 빠르고 입 가벼운 애들로 골라서 소문 퍼트려. 그럼 알아서 내뺄 거야.”

풍양과 그 수하들을 해치웠다지만 아직 인근에는 상당한 숫자의 마적들이 이리처럼 주변을 어슬렁거리고 있었다.

항산검문이라는 손쉬운 먹잇감에 이빨을 박기 위해 호시탐탐 때를 노리는 것이다.

“산서잠룡과 진천검이 풍양을 일격에 때려죽였다. 뭐 이 정도면 놈들도 혼비백산하겠군요.”

“사실과는 좀 다르긴 한데…… 적당히 양념 쳐. 남의 집 싸움에 우리가 피 흘릴 수는 없잖아?”

소문의 진위는 중요하지 않다. 태원진가의 두 형제가 풍양과 적풍단으로부터 항산검문을 구했다는 것만 알려지면 된다.

“어차피 며칠 안에 태원진가가 움직일 거야. 아주 멍청한 놈들이 아니고서야 살고 싶으면 고원으로 돌아가겠지.”

항산검문의 뒤에 태원진가라는 대호(大虎)가 버티고 있다는 사실이야 곧 널리 퍼질 것이다. 산군의 포효 한 번이면 알아서 나가떨어질 놈들 아닌가.

“길어도 닷새야. 그때까지 고생 좀 하자고.”

두 지부장이 고개를 끄덕였다.

“고생이랄 게 있습니까. 총지부장님 명령인데 당연히 따라야죠.”

“전 좋습니다. 옆에 고원이 붙어 있어서 그런가, 탁 트여서 말 달리는 재미도 있고.”

“그럼 다행이고.”

월화가 피식 웃으며 곰방대를 빨아들였다.

“저어, 그런데 말입니다.”

“응?”

휘하 지부장 중 가장 호전적이고 무공 광으로 평가받는 혼주지부장이 눈을 반짝였다.

“여기 부상자들한테 듣기로는 풍양 그놈이 단신으로 항산호와 진천검을 쓰러트렸다던데. 사실입니까?”

“맞아. 나도 직접 보지는 못했지만.”

“허어, 대단하네요.”

“대단하지. 단기간에 그렇게 빨리 강해졌다는 점에서 구린내가 진동하지만.”

절정의 경지는 깨달음의 영역이다. 그때부터는 신체의 단련을 넘어 무리(武理)를 꿰뚫어야 보다 더 높은 경지로 나아갈 수 있는 것이다.

그러나 불과 얼마 전 항산호 철무백을 상대로 패퇴했던 풍양이다. 제아무리 깨달음이 받쳐 준다 해도 짧은 시일 안에 너무 강해졌다.

아직 잠력단의 존재를 모르는 월화는 그 부분을 짚었다.

“뭔가 수를 쓴 게 분명한데…… 자세히 한번 알아봐야겠어.”

눈치 빠른 정양지부장은 묵례를 취했고, 혼주지부장은 뒤통수를 벅벅 긁었다.

“물론 풍양, 그 마적 놈도 대단하지만 제가 말씀드린 건 다른 사람입니다.”

“누구? 아.”

“산서잠룡. 대단하지 않습니까? 본 문에서 파악한 바에 의하면 그의 무공은 아직 일류에 불과한데…… 매번 예상을 벗어나는군요.”

정보는 객관적 사실이 밑바탕 되어야 한다. 하오문도인 그들은 냉정하게 제삼자 입장에서 정보의 쓰임새를 판단하고, 사람과 상황에 적용시킨다.

그런 의미에서 진태경은 골칫덩이였다. 그에 관한 예상은 늘 빗나갔으니까.

“그런데 참 신기한 게, 점점 기대가 된다는 거죠.”

“기대?”

“다음에는 어떤 식으로 우리의 예상을 벗어날까. 뭐 그런 기대 말입니다.”

히죽거리던 혼주지부장은 월화의 냉담한 표정에 웃음을 멈췄다.

“죄송합니다. 제가 입방정을…….”

“잘 아네. 나가서 일 봐.”

두 지부장을 쫓아낸 월화는 다시 곰방대를 물었다.

달싹이는 입술에서 연기와 함께 아주 작은 목소리가 흘러나왔다.

“진태경이라, 진태경.”

문득, 언젠가 사부(師傅)와 나눴던 대화가 생각난다.



‘그런 자들이 있다. 늘 예측을 벗어나는 자, 정보로 판단할 수 없는 자들이.’

‘그럼 어떻게 하죠?’

‘판단하지 말고 그저 지켜보아라. 네가 직접 그에 대한 확신을 내릴 수 있을 때까지.’

‘그렇게까지 했는데도 확신을 내리지 못한다면요?’

‘예측불허. 그런 자가 있다면 언젠가 천하를 움직일 만한 재목이 아니겠느냐?’



‘천하를 움직일 재목…….’

월화는 곰방대의 재를 털고 전각을 빠져나왔다.

어둠이 짙게 내리깔린 밤, 타오르는 횃불을 이정표 삼아 걷던 그녀가 발걸음을 멈춘 곳은 진태경이 머무르는 전각 앞이었다.

“거기서 뭐 해요?”

전각 앞에 처량하게 쭈그려 앉아 있던 혁무진이 월화를 보고 반색했다.

“앗, 오셨습니까?”

“대충 일이 마무리되어 가는 중이라 잠깐 들렀어요. 안에 진 공자 있죠?”

사실 물어볼 필요도 없는 일이었다. 밖으로 환한 불빛이 새어 나오고 있었으니까.

하지만 혁무진은 어두운 얼굴로 고개를 저었다.

“안에 없어요?”

“아뇨, 계시긴 한데. 그…….”

한숨을 푹 내쉰 혁무진이 말을 이었다.

“상태가 별로 좋지 않으셔서요. 아까부터 뜻 모를 소리만 중얼거리고 계세요. 보면 소름이 돋는다니까요.”

“뜻 모를 소리요?”

“네. 혹시 급식이 무슨 뜻인지 아십니까?”

“급식이요?”

월화는 고개를 갸웃했다. 적지 않은 책을 읽었지만 처음 들어 보는 말이다.

“글쎄요. 처음 들어 보는 것 같은데.”

“그렇죠? 전 또 제가 무식한 놈이라 모르는 건가 싶었는데.”

“그래서요?”

“저희 조장님 성격 아시잖아요. 하도 급식, 급식 하시기에 무슨 뜻이냐고 여쭤봤다가 쫓겨났죠.”

처량한 얼굴로 이마를 슬슬 문지르는 걸 보니 곱게 쫓아내진 않은 모양이다.

‘무슨 일이지?’

궁금증을 참지 못한 월화가 문을 두드리려던 그때였다.

문틈 사이로 새어 나오는 누군가의 음산한 목소리.

“급식, 고딩, 철컹, 철컹…….”

순간 소름이 쭉 돋은 월화는 자신도 모르게 뒷걸음질 쳤다.

“바, 방금 들었어요?”

“아까부터 저 상태라니까요.”

그 와중에도 들려오는 의미 불명의 중얼거림에 그녀가 주춤주춤 물러났다.

“다, 다음에 올게요.”

다시 한번 깨달았다.

진태경이라는 인간은 여전히 예측불허라는 사실을.



* * *



이틀이라는 시간이 쏜살같이 흘렀다. 이소월은 그날 밤 이후 다시 찾아오지 않았고, 나도 굳이 전각을 나서지 않았다.

새로 얻은 열양지기를 다루는 데에 대부분의 시간을 보내는 와중에도 불쑥불쑥 그녀가 남긴 마지막 말이 생각났다.



‘혼인은 인륜지대사(人倫之大事)이니 천천히 생각해 보세요.’



당시에는 너무 당황해서 입만 벙긋거렸다. 여자에게 먼저 프러포즈를, 그것도 나보다 한참 어려 보이는 여자애한테 받을 줄이야.

비록 거래라는 단어를 쓸 정도로 삭막한 정략혼 제의였지만 프러포즈는 프러포즈다.

하지만 더 큰 충격이 남아 있었다.

‘열일곱 살이라니. 이거 실화냐.’

고등학교 1학년이면 한창 급식 먹을 나이다.

늦둥이 동생인 하연이보다 두 살이나 어리고, 나와는 무려 열 살 차이인 것이다.

‘역시 무림…….’

중학교 때 결혼하고 고등학생 때 부모 되어도 이상하지 않은 세상이다. 오히려 이 나이 먹도록 결혼 안 한 태원진가 삼 형제가 별종으로 보일 정도다.

아니, 잠깐만.

“뭘 그렇게 보냐?”

내 시선을 눈치챈 진무경이 퉁명스럽게 물었다. 풍양으로부터 상당한 부상을 입었던 그는 이제 스스로 거동이 가능할 정도로 회복되어 있었다.

‘그러고 보니…….’

진무경의 혼인 여부에 대해서는 한 번도 들어 본 적이 없다.

나는 설마 하는 마음에 입을 열었다.

“혹시나 해서 물어보는 건데.”

“뭐.”

“혼인했어?”

푸웁!

내 얼굴에 찻물을 뱉은 진무경이 황급히 외쳤다.

“무, 무슨 헛소리를!”

“아니면 말지. 왜 이렇게 당황해?”

뜻밖의 세수를 당한 나는 소매로 얼굴을 닦으며 질문을 이어 갔다.

“왜 안 했는데?”

잠깐 당황하는가 싶던 진무경이 순순히 대답했다.

“무공 익히기에도 바쁘다. 내게 여인은 사치야.”

“그렇게 말하니까 되게 검소하게 느껴지네.”

“네놈 같은 음탕한 한량과 동급으로 보지 마라. 그건 나에 대한 모욕이야.”

“…….”

음탕하긴 시벌, 27년 동안 모태 솔로로 살았던 나다.

연애를 사치라고 한다면 나는 자린고비 그 자체다. 약간 다른 점이 있다면 자린고비는 굴비를 쳐다보며 밥을 먹었지만 내게는 USB가 있었다는 것 정도지.

“뭐지, 그 표정은? 굉장히 슬퍼 보이는데.”

“지나간 삶에 대한 후회랄까.”

“드디어 사람이 되어 가는군.”

지나간 삶에 대한 해석이 다른 것 같은데…… 그래, 너 좋을 대로 해석해라.

“그런데 갑자기 혼인에 관해서는 왜 물어본 것이냐? 너도 뻔히 아는 사실을.”

“아, 항산검문주가 나랑 혼인하자고 그래서.”

“푸웁!”

“……후, 작작 뱉어라.”

두 번째 찻물을 닦아 내는 사이 평정심을 되찾은 진무경이 입을 열었다.

“항산검문주가?”

“어. 이틀 전에 그러더라고.”

“도대체 왜 너 같은 놈과…… 아, 당연히 정략혼이겠군.”

“…….”

거, 틀린 말은 아닌데 상당히 기분 나쁘네. 이제 나 정도면 무림에서나 현실에서나 일등 신랑감 아닌가?

“그래서, 할 생각이냐?”

“당연히 아니지. 한참 어린 애랑 어떻게 혼인을 해.”

“고작 약관인 놈이 못 하는 말이 없구나.”

몸은 스물이지만 정신은 스물일곱이다, 이놈아.

그리고 이소월의 제의에 대한 내 대답은 이미 정해진 지 오래였다.

사랑하는 사람이 있는데 두 집 살림을 차릴 순 없는 법. 지금 내게는 오직 한 사람뿐이다.

‘송이 씨는 지금 뭘 하고 있을까.’

상상만 해도 행복하다. 흐뭇하게 웃으며 찻잔을 기울이는 나를 진무경이 해괴한 표정으로 바라봤다.

“역겨운 표정이군.”

“아무튼, 여러 가지 이유로 혼인은 거절.”

“잘 생각했다. 적어도 정략혼이라면 우리가 얻는 것이 있어야 하는 법인데, 마음도 없는 상대와 혼인하면서 아무것도 얻지 못한다면 정략혼을 할 이유가 없지.”

무공밖에 모르는 바보인 줄 알았는데, 가끔 보면 제법 날카로운 현실주의자가 된다.

“그리고 무슨 제의를 하더라도 큰형님이 있는 한 어림없다. 널 정략혼으로 엮으실 분은 아니니까.”

“저쪽에서도 꽤 큰 제의를 하긴 했어.”

“흠. 뭘 주겠다더냐?”

진무경이 심드렁한 얼굴로 찻잔을 기울였다.

“혈랑검법, 혈랑보법. 그리고 수라멸권.”

푸웁!

“……아, 시바.”

이번에는 닦을 시간도 없다. 진무경이 내 멱살을 잡고 탈탈 털었다.

“당장 혼인해!”
```

## Current accepted English baseline

```markdown
# Chapter 122

There were two things that mattered when conveying information: speed and accuracy.

To that end, the Lower District Sect, a sect that dealt in information, had built an extensive information network at every branch.

Wolhwa had the authority to issue mobilization orders to the more than thirty branches established throughout Shanxi Province.

“How’s it going? Are you finished?”

A clean-cut middle-aged man answered her question. He was the Jeongyang Branch Leader of the Lower District Sect.

“We separated and moved all the corpses. There were no more survivors from the Mount Heng Sword Sect, but some of the mounted bandits were still breathing.”

“How many?”

“Exactly forty-seven.”

“That’s quite a lot who survived. How many of them can we save?”

“With the medicine we currently have, thirty at most.”

“We don’t need to save every last one.”

At Wolhwa’s words, the Jeongyang Branch Leader lowered his head.

“I’ll take care of it.”

That decided the surviving mounted bandits’ fates.

Those with serious injuries would rejoin the mountain-high pile of their comrades, while those with minor injuries might live a little longer.

Of course, the moment their treatment was finished, they would be sold as slaves to the mines or fighting pits.

“Next. Honju Branch Leader?”

“No problems on our end, either.”

The Honju Branch Leader was a hulking man whose face was covered in sword scars. He scratched at his stiff, wirelike beard and continued.

“Truth is, we didn’t even need to step in. They must’ve heard Pung Yang was dead and the Red Wind Band had been wrecked, because they didn’t come anywhere near the area.”

“For now, that’s enough. Pick the swiftest and most loose-lipped people you have and spread the rumor. They’ll run away on their own.”

Although Pung Yang and his subordinates had been dealt with, a considerable number of mounted bandits were still prowling around the area like wolves.

They were waiting for an opportunity to sink their teeth into the easy prey that was the Mount Heng Sword Sect.

“The Sleeping Dragon of Shanxi and the Heaven Shaking Sword beat Pung Yang to death with a single blow. If the others hear that, they’ll be scared out of their minds.”

“It’s not exactly true, but… Add enough seasoning. We can’t bleed for someone else’s fight, can we?”

The truth of the rumor was unimportant. All that mattered was that people learned the two brothers of the Jin Family of Taiyuan had rescued the Mount Heng Sword Sect from Pung Yang and the Red Wind Band.

“Besides, the Jin Family of Taiyuan will make a move within a few days. Unless they’re complete idiots, they’ll return to the plateau if they want to live.”

The fact that the great tiger known as the Jin Family of Taiyuan stood behind the Mount Heng Sword Sect would soon spread far and wide. Wouldn’t one roar from the mountain king be enough to send those bandits running?

“Five days at most. Let’s put in some effort until then.”

The two Branch Leaders nodded.

“What effort? It’s the Chief Branch Leader’s order. Of course we have to follow it.”

“I like it. Maybe it’s because the plateau is right next door, but there’s something fun about riding across all this open land.”

“Then that’s a relief.”

Wolhwa gave a short laugh and drew on her long-stemmed tobacco pipe.

“Um, by the way…”

“Yes?”

The Honju Branch Leader, considered the most aggressive and martial-arts-obsessed of her subordinates, had a bright gleam in his eyes.

“I heard from the wounded that bastard Pung Yang took down the Tiger of Mount Heng and the Heaven Shaking Sword all by himself. Is that true?”

“It is. Though I didn’t see it myself.”

“Wow. That’s impressive.”

“It is impressive. The fact that he grew so strong so quickly reeks of something fishy, though.”

The Peak realm was a domain of enlightenment. From that point onward, a martial artist had to see through the principles of martial arts rather than merely train the body in order to advance to a higher realm.

But Pung Yang had been defeated by Cheol Mubaek, the Tiger of Mount Heng, only a short while ago. No matter how much enlightenment supported him, he had become far too strong in far too little time.

Wolhwa, who still knew nothing of the Temporary Strength Pill, focused on that point.

“He definitely used some kind of trick… I’ll have to look into it more closely.”

The quick-witted Jeongyang Branch Leader offered a silent bow, while the Honju Branch Leader vigorously scratched the back of his head.

“Of course, Pung Yang, that mounted-bandit bastard, is impressive too. But I was talking about someone else.”

“Who? Ah.”

“The Sleeping Dragon of Shanxi. Isn’t he incredible? According to what our sect has determined, his martial arts are still only First Rate, but he keeps defying our expectations.”

Information had to be based on objective facts. As members of the Lower District Sect, they coolly judged how information could be used from a third-party perspective, then applied it to people and situations.

In that regard, Jin Taekyung was a headache. Every prediction concerning him had been wrong.

“But the strange thing is, I’m starting to look forward to it more and more.”

“Look forward to what?”

“Wondering how he’ll defy our expectations next time. That kind of anticipation.”

The Honju Branch Leader had been grinning broadly, but he stopped smiling when he saw Wolhwa’s impassive expression.

“I’m sorry. I was running my mouth.”

“At least you know it. Go outside and handle your work.”

After driving the two Branch Leaders out, Wolhwa put her pipe back between her lips.

A tiny voice slipped from her barely moving lips along with the smoke.

“Jin Taekyung. Jin Taekyung.”

She suddenly remembered a conversation she had once shared with her Master.

*There are people like that. People who always defy prediction, people who cannot be judged through information.*

*Then what should I do?*

*Don’t judge them. Just watch them until you can reach your own conclusion about them.*

*What if I still can’t reach a conclusion after going that far?*

*Unpredictable. If there is such a person, wouldn’t they be the sort of talent capable of moving the world someday?*

*A talent capable of moving the world…*

Wolhwa tapped the ash from her pipe and left the pavilion.

Night had fallen thick and dark. Guided by blazing torches that served as landmarks, she walked until she stopped in front of the pavilion where Jin Taekyung was staying.

“What are you doing out here?”

Hyuk Mujin, who had been sitting miserably in a crouch before the pavilion, brightened when he saw Wolhwa.

“Oh, you’re here?”

“I’ve mostly finished dealing with things, so I stopped by for a moment. Young Master Jin is inside, right?”

In truth, there was no need to ask. Bright light was spilling out through the pavilion.

But Hyuk Mujin shook his head with a grim expression.

“He isn’t inside?”

“No, he is. It’s just that…”

Hyuk Mujin let out a deep sigh before continuing.

“His condition isn’t very good. He’s been muttering things that make no sense for a while now. I get goose bumps just looking at him.”

“Things that make no sense?”

“Yes. Do you happen to know what ‘school lunch’ means?”[^1]

“School lunch?”

Wolhwa tilted her head. She had read a considerable number of books, but it was the first time she had ever heard the word used that way.

“I don’t think so. It sounds unfamiliar.”

“Right? I wondered if I was just too ignorant to know.”

“And then?”

“You know what our Squad Leader is like. He kept saying ‘school lunch, school lunch,’ so I asked him what it meant. Then I got kicked out.”

Judging by the way Hyuk Mujin miserably rubbed his forehead, it seemed he had not been politely shown the door.

*What happened?*

Wolhwa was just about to knock when an eerie voice seeped through the gap in the door.

“School lunch, high schooler, clank, clank…”

A chill ran over Wolhwa, and she took a step backward without realizing it.

“D-Did you hear that?”

“He’s been like that for a while.”

Even as the incomprehensible muttering continued, she slowly backed away.

“I-I’ll come another time.”

She realized it once again.

The man named Jin Taekyung was still utterly unpredictable.

* * *

Two days flew by in the blink of an eye. Lee Seowol did not come back after that night, and I didn’t bother leaving the pavilion, either.

Even while spending most of my time learning to control the newly acquired Scorching Yang Qi, her final words kept coming back to me.

*Marriage is one of life’s great human obligations, so take your time thinking it over.*

I had been so flustered at the time that I could only open and close my mouth.

Who would have thought I’d receive a proposal from a woman first—and from a girl who looked so much younger than me, at that?

Although it was a cold political marriage proposal—cold enough that calling it a transaction wasn’t an exaggeration—it was still a proposal.

But there was an even greater shock waiting for me.

*Seventeen years old? Is this for real?*

A first-year high school student was right in the prime school-lunch-eating years.

She was two years younger than my late-born little sister, Hayeon, and a full ten years younger than me.

*That’s the Murim for you…*

Getting married in middle school and becoming a parent in high school wouldn’t even be strange in this world. In fact, the three brothers of the Jin Family of Taiyuan looked like the oddballs for remaining unmarried at our age.

No, wait a second.

“What are you staring at?”

Jin Mukyung noticed my gaze and asked irritably. He had suffered considerable injuries at Pung Yang’s hands, but he had now recovered enough to move around on his own.

*Come to think of it…*

I had never heard whether Jin Mukyung was married.

I opened my mouth, half expecting the worst.

“Just asking in case.”

“What?”

“Are you married?”

Pffft!

Jin Mukyung spat tea into my face and hurriedly shouted.

“What kind of nonsense are you talking about?”

“If you’re not, then you’re not. Why are you so flustered?”

After receiving that unexpected facial wash, I wiped my face with my sleeve and continued asking questions.

“Why aren’t you?”

Jin Mukyung looked flustered for a moment, then answered readily.

“I’m too busy training in martial arts. Women are a luxury to me.”

“You make it sound downright frugal.”

“Don’t lump me in with a lecherous idler like you. That’s an insult to me.”

“…”

Lecherous, my ass. I had spent twenty-seven years as a lifelong single.

If dating was a luxury, then I was the very definition of a miser. The only slight difference was that while Jaringobi ate rice while staring at a strip of dried fish, I had a USB drive.[^2]

“What’s with that expression? You look incredibly sad.”

“Maybe it’s regret over the life I’ve lived.”

“At last, you’re becoming a human being.”

He seemed to have a different interpretation of my past life, but fine. He could interpret it however he wanted.

“But why did you suddenly ask about marriage? It’s something you already know perfectly well.”

“Oh, because the Sect Leader of the Mount Heng Sword Sect asked me to marry her.”

Pffft!

“…For fuck’s sake. Stop spitting.”

While I wiped away the second mouthful of tea, Jin Mukyung regained his composure and spoke.

“The Sect Leader of the Mount Heng Sword Sect?”

“Yeah. She said it two days ago.”

“Why on earth would she marry someone like you… Ah, of course. It must be a political marriage.”

“…”

He wasn’t wrong, but it was still pretty damn irritating. At this point, wasn’t I prime husband material both in the Murim and in the real world?

“So, are you thinking of doing it?”

“Of course not. How could I marry a girl so much younger than me?”

“You’re barely twenty, and you say things like that.”

*My body is twenty, but my mind is twenty-seven, you bastard.*

Besides, I had decided on my answer to Lee Seowol’s proposal a long time ago.

You can’t set up two households when there’s someone you love. There was only one person in my heart right now.

*What could Song-i be doing right now?*

Just imagining it made me happy. I tilted my teacup with a blissful smile, and Jin Mukyung stared at me with a bizarre expression.

“What a disgusting look.”

“Anyway, I’m turning down the marriage for various reasons.”

“You made the right decision. At the very least, a political marriage has to offer us something in return. If you marry someone you have no feelings for and gain nothing from it, there’s no reason to enter into a political marriage.”

I had thought he was a fool who knew nothing but martial arts, but every now and then, he turned into a surprisingly sharp realist.

“And no matter what she offers, it’s out of the question as long as our eldest brother is around. He isn’t the sort of person who’d arrange a political marriage for you.”

“They did make a pretty substantial offer, though.”

“Hm. What did she say they would give you?”

Jin Mukyung tilted his teacup with an uninterested expression.

“The Blood Wolf Sword Technique, the Blood Wolf Footwork, and the Shura Annihilating Fist.”

Pffft!

“…Ah, fuck.”

This time, I didn’t even have time to wipe it away. Jin Mukyung grabbed me by the collar and shook me hard.

“Marry her right now!”

[^1]: “School lunch” is Korean slang for a school-age kid, while “clank, clank” evokes handcuffs or prison bars—the joke is that sexual interest in a high schooler could land someone in jail.
[^2]: Jaringobi is a traditional Korean image of a miser who stares at dried fish while eating rice rather than eat the fish.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 122`.

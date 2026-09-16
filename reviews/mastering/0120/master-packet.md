# Master Edit Task — Chapter 120

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
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 조필     | **Jopil**          |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본문      | **our sect / this sect**                                        |
| 귀가      | **your family**                                                 |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 운칠기삼 | **seven parts luck and three parts skill** | Established Korean saying used in Taekyung's reflection. |
| 운구기일 | **nine parts luck and one part qi** | Taekyung's playful variation on 운칠기삼. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 하수오 | **He Shou Wu** | Traditional medicinal herb; a thirty-year-old specimen is offered to Jang Taebo. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 이소월 | young_martial_artist_to_allied_sect_leader | Young Lady Lee | formal-polite | Taekyung uses 이 소저 while greeting Seowol at the banquet. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |

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

#### Chapter 118 tail (verified mastered)

…
a few years of training, he had already attained seventy percent mastery of the Crimson Blood Twelve Sabers. It was more than enough to kill a brat hopelessly beneath him in both age and martial arts. “Die!” *Shiiing!* The Crimson Blood Twelve Sabers was a domineering martial art. Red saber qi shot from the curved saber and slashed wildly in every direction. The fierce momentum split open the surface of the earth and burst the air apart. Yet the target it was meant to cut was no longer there. Jin Taekyung dodged the attack by exactly half a step and thrust his spear. *Shweeeeeek!* The spearhead drove toward Pung Yang’s throat. He hastily twisted his head aside to evade it, and a chill ran through his chest. *Fast.* Fast and accurate. Jin Taekyung had yet to reach the stage of injuring others with Sword Energy, the hallmark of a Peak master, but his movements had already caught up to Pung Yang’s. *Could this brat have taken the Temporary Strength Pill too? No. It’s completely different from mine.* Pung Yang had taken the Temporary Strength Pill several times before. One look at Jin Taekyung’s body, flushed bright red with heat, was enough to tell him that the pill the brat had swallowed wasn’t a Temporary Strength Pill. *Then what did he—wait!* Pung Yang couldn’t finish the thought. Jin Taekyung had finally seized the initiative and begun unleashing the Jin Family’s Spear Technique in earnest. *Shh-shh-shh-shh-shhk!* Dozens of spear shadows poured down like a rain shower. The sight alone was suffocating. No, it wasn’t just an illusion. It really was suffocating. A bead of sweat rolled down Pung Yang’s forehead. *This is…* Scorching Yang Qi. And not just any Scorching Yang Qi. It was powerful enough to affect even Pung Yang, a Peak master. The Tiger of Mount Heng, Cheol Mubaek, had also possessed Scorching Yang Qi, but it couldn’t compare to what Jin Taekyung was emitting now. *He took a divine elixir—a Scorching Yang-type divine elixir!* *Whooooom!* Recognizing it changed nothing. The heat was dizzying, and the attacks were sharp. Pung Yang bit down hard on his lip as he retreated again and again, barely evading the spearhead. *Against a brat this young!* He had lived his entire life fiercely. Now, even after taking the Temporary Strength Pill, he felt humiliated to be driven back by a young brat who had only just begun making a name for himself. That anger flowed straight into his curved saber. The saber qi rising over the blade blazed redder than ever. *Hiss!* The Jin Family’s Spear Technique and the Crimson Blood Twelve Sabers differed in both weapon and form, but they had one thing in common: both were domineering martial arts. In the blink of an eye, Jin Mukyung’s iron spear and Pung Yang’s curved saber finally parted after more than ten fierce exchanges. “Hmm.” Jin Taekyung was the first to retreat. Blood flowed from his torn palm, and the heavy, sturdy iron spear had been cut by the sharp saber qi until less than half of it remained. “You fool.” Pung Yang smiled triumphantly. For a martial artist, losing one’s weapon meant defeat. Even the Tiger of Mount Heng, Cheol Mubaek, who had built his reputation with nothing but his fists and feet, had knelt before Pung Yang. Jin Taekyung hadn’t even crossed the wall into the Peak realm. The moment he lost his weapon, he was as good as dead. “Did you think you could defeat me head-on?” Jin Taekyung wiped the blood from his palm and answered. “No. But I did learn some valuable information.” “…Valuable information?” “Yeah. I figured out your attack pattern.” “Pat—what?” “Your attack pattern is strong, strong, strong, strong, strong.” *What kind of bullshit is this?* Pung Yang understood that the brat was talking about his martial arts, but he had never heard of this “pattern-whatever” before. And what did he mean by strong, strong, strong, strong, strong? Pung Yang glared at Jin Taekyung with murder in his eyes. “I’ll sever the sinews and meridians in all four of your limbs as payment for that nonsense.” Jin Taekyung opened his mouth with a bored expression. “You really like cutting off and pulling out people’s limbs. Do you have a limb fetish?” “You little bastard…” “You old bastard…” Pung Yang drew a deep breath. He was a Peak master who had spent his entire life possessing a cool, rational mind. But he couldn’t stop his voice from breaking into pieces with anger. “You. Will. Die. By. My. Hand.” “I. Sometimes. Cut off. Limbs. Sometimes. I don’t like this version of myself.” He felt his patience snap. He could swear that he had never been this furious in nearly ten years. “Graaaargh!” Pung Yang charged like a madman, unleashing a strange cry that could have been either a scream or a roar. Without using any form or martial art, he brought the curved saber down over the crown of Jin Taekyung’s head with all his strength. “Die!” That was when Jin Taekyung’s calm expression was reflected in Pung Yang’s bloodshot eyes gleaming with killing intent. In an instant, his mind snapped clear as though someone had dumped cold water over him. *Something’s wrong.* Pung Yang drew up his internal energy with all his might. As his Body-Protecting Qi rose, a dagger flashed in Jin Taekyung’s previously empty hand. *Shnk!*

#### Chapter 119 tail (verified mastered)

…
snapped back. The iron arrow Pung Yang had been holding was embedded in his forehead. “Senior Brother!” As the belated scream rang out, Pung Yang smiled. “I was just about out of throwing knives… Thank you, Sect Leader.” Lee Seowol bit her lip. “Go! Hurry!” I took a deep breath. I had already mapped out every step in my head. Jin Mukyung lay only about twenty zhang—sixty meters—away. If I drew up as much internal energy as possible and ran with him on my back, enduring the internal injuries, I could reach the fortress gate in no time. Pung Yang might catch up by then, but if they bought me just a little more time, I could survive. *I can go back.* Back to the Jin Family of Taiyuan, where Jin Wikyung was. Back home, where my mother and Hayeon were waiting. If I lived to fight another day, I was confident I could return far stronger—strong enough to make Pung Yang look insignificant. *That’s enough.* I drew another deep breath and turned toward Lee Seowol. “I’ll avenge you. I swear.” For the briefest instant, I thought she smiled. Perhaps I imagined it. The moment passed too quickly, and when I looked again, only firm resolve remained on her face. “Go. Hurry.” Her words were the starting signal. The Mount Heng martial artists charged with furious shouts, Lee Seowol at the front. *Yes. I have to go.* I drew up every last bit of internal energy in my body. Sharp pain tore through me as the internal injuries left by the Scorching Yang Qi sent dark-red blood flowing from my nose, but I endured it. It only had to last a moment. A very brief moment. *Inventory open. Equip spear.* The cool shaft settled into my grip. Then I pushed off the ground once. *Boom.* I shot forward like an arrow—no, faster than an arrow. Not toward Jin Mukyung. Toward Pung Yang. I could see his broad smile. “That’s more like it!” “Shut up, you son of a bitch.” “Ha-ha-ha-ha!” Pung Yang’s curved saber was larger than ever before. Brimming with red saber qi, it swung toward me. *Whoooosh!* The wind exploded, and even the air seemed to vanish. I gripped the iron spear hard enough to crush it. *Please. Just this once.* I poured all fifteen years of my internal energy into the spear. Drawing my shoulder and waist as far back as they would go, I sent everything I had flying forward. *One Annihilation.* *Rumble-rumble-rumble!* The immense saber qi collided with the vortex. A thunderous roar filled the world, as though the sky itself were splitting apart. Through the raging wind, I saw it clearly. *Kaboom!* The white vortex shattered into pieces before the red saber qi. The massive concentration of qi completely pulverized One Annihilation. Pung Yang whispered with an ecstatic expression, “This is as far as you go.” The next instant, Pung Yang’s internal energy surged along the spear and slammed into me. *Boom!* Blinding pain and ringing ears rolled over me like waves. *Ding.* > **System** > - You have suffered **Internal Injury**! Your condition is extremely serious! > - **Scorching Yang Qi** is running wild! > - You have suffered a **Severe Injury**! All stats have dropped significantly! The System notifications rang out one after another, mingling with the Mount Heng martial artists’ shouts, Lee Seowol’s scream, and Pung Yang’s laughter. *It’s over.* The instant my legs gave out despite my will, a powerful hand clamped around my throat. “Guh. Guhh.” “That was fairly impressive. If I’d been even a moment slower, you might have won.” Pung Yang bared his teeth in a grin. The red light in his eyes was slowly fading. *Damn it. I was so damn close.* I wanted to say it aloud, but my mouth was full of blood, making even that difficult. “I swore by the gods of heaven and earth, didn’t I? I swore I’d pull out your tongue.” Had he said that? By now, I could barely remember who I was. Pung Yang pried open my mouth with his other hand. His rough fingers seized my blood-soaked tongue and pulled. “Ghh…” “When you were running that mouth, didn’t you know this would happen? Huh?” “Ghaa… hahahaa.” “Hahaha! What the hell are you babbling about? Shall I let you say your last words?” Pung Yang laughed heartily and released my tongue. Only then could I speak. I swallowed the blood in my mouth and said, “Salty.” “What?” Damn salty. “What kind of bullshit is that?” *What do you think?* *I’m saying the taste of your fingers brought me back to my senses a little.* Half-conscious, I muttered, *Inventory open. Summon anything.* *Ding.* > **System** > - No item named **Anything** can be found. The oldest item stored in your inventory will be summoned first. > - The **Unnamed Sword** has been summoned. *The Unnamed Sword? What was that again?* *Whatever.* I gathered the last of my strength and thrust the sword in my hand at Pung Yang’s chest, shrouded in Body-Protecting Qi. It was a futile last-ditch attack with an obvious conclusion. *Damn Body-Protecting Qi.* But this was enough. I had no regrets left. It was at that moment, as my head slowly drooped— *Shnk!* *Ding.* > **System** > - The **Unnamed Sword** has satisfied a specific condition. > - **Ten-Thousand-Year Cold Iron** has destroyed **Body-Protecting Qi**. …Huh?

## Korean source

```text
＃120화



쉭!

느리지만 힘차게 찔러 들어오는 검 한 자루.

짧은 순간, 풍양의 입가에 비웃음이 떠올랐다.

‘그래, 이럴 줄 알았지.’

온갖 암수가 난무하는 고원에서 수십 년을 살았다. 같은 수법에 두 번이나 걸려들 만큼 어리석었다면 진즉 들개 밥이 되었을 것이다.

‘그런데 저 검은 어디서 튀어나온 거지?’

비수도 아니고 저만한 길이의 장검을 어디에 숨겨 놨던 걸까? 풍양은 가벼운 의문과 함께 호신강기를 끌어 올렸다.

스스스스.

예상했던 일이었기에 대처도 빨랐다. 순식간에 솟구쳐 오른 붉은 기가 빈틈없이 몸을 감싼다.

호신강기는 강력한 검기(劍氣)가 아닌 이상 생채기 하나 낼 수 없는 무적의 갑옷. 어린놈의 헛된 발악이 우습기만 했다.

‘지긋지긋한 놈. 이제 그만 죽어라.’

단숨에 진태경의 목을 꺾어 버리려던 그 순간이었다.

푹-!

“……어?”

몸 안을 파고드는 서늘한 냉기, 그리고 그 뒤를 잇는 뜨거운 통증. 풍양은 부릅뜬 눈으로 가슴을 관통한 검을 바라봤다.

‘이게 무슨.’

호신강기가 사라졌다. 아니, 파괴됐다.

진태경의 검은 호신강기를 두부 가르듯 베어 버리고 그의 가슴마저 꿰뚫었다.

피 한 방울 묻지 않은 투명한 검신을 내려다보던 풍양이 신음처럼 내뱉었다.

“만년한철……?”

들어 본 적이 있다. 천하의 그 무엇도 자르고 부술 수 있다는 신병이기(神兵利器)에 관한 이야기를.

“이걸 네놈이 어떻게.”

풍양은 일그러진 얼굴로 검의 주인을 바라봤다. 태원진가의 어린놈은 천진난만하게 눈을 깜빡이더니 입을 열었다.

“와, 이게 되네.”

“이런 개새끼가……!”

당장 목을 꺾어 버리고 싶었지만, 순간 눈앞이 아득해지며 손아귀에서 힘이 풀렸다. 몸 안에 가득 차 있던 힘이 썰물처럼 사라지고 무력감이 차오른다.

‘하필 이럴 때 잠력단의 효력이.’

비틀비틀 물러나는 풍양의 칠공(七空)에서 피가 흘러나왔다.

지금까지 입은 크고 작은 부상과 호신강기가 흩어지며 역류한 공력이 빠르게 그를 죽음으로 몰아가기 시작했다.

‘이대로, 이대로 죽을 수는 없어.’

풍양은 황급히 품을 더듬었다.

아직 잠력단 한 알이 남아 있다. 그것만 먹으면 놈들을 단매에 쳐 죽이고 이 자리를 뜰 수 있다. 잃은 것이 적진 않지만 몸을 추스른 다음 다시 무림에 나오면 되는 거다.

그래, 잠력단을 먹기만 하면…….

툭.

제기랄, 마음이 너무 급했다.

풍양의 다급한 손길에 떨어진 목곽이 땅에 부딪치며 활짝 열렸다. 피처럼 붉은빛이 도는 단환이 또르르 굴러가더니 누군가의 발아래에 멈춘다.

“아, 이게 잠력단이야?”

신기한 듯 잠력단을 주워 살펴보는 진태경을 향해 풍양이 외쳤다.

“내, 내놔라, 어서!”

“여기서 문제, 그런다고 내가 줄까?”

“놈!”

있는 힘을 다해 달려들었지만 이미 망가진 신체는 한계에 달해 있었다. 진태경에게 닿기도 전에 힘이 풀린 다리가 풀썩 주저앉았다.

이제 풍양에게 남은 길은 하나밖에 없었다.

“제발 부탁이다. 내게, 내게 그걸 다오.”

“만약에 준다면?”

풍양이 간절하게 외쳤다.

“다시는 네 눈에 띄지 않으마. 아니, 앞으로 네게 충성을 다하겠다!”

“오, 절정 고수 수하라. 그거 괜찮은데.”

“그, 그렇지? 그러니 어서 내게 잠력단을 다오!”

“일단 내 물건부터 돌려받고.”

“물건?”

그의 의문은 곧 풀렸다. 다가온 진태경이 가슴 한복판에 박혀 있던 검을 쑥 뽑은 것이다.

아찔한 고통과 함께 피가 폭포수처럼 흘렀다.

“쿠에에에엑!”

풍양은 자신이 토해 낸 핏물에 내장 조각이 섞인 것도 눈치채지 못했다.

단지 시야가 점점 어두워지고 소리가 아득히 멀어지는 것을 느꼈을 뿐이다.

그는 죽어 가고 있었고, 간절함에 반쯤 미쳐 있었다.

‘살고 싶다.’

일평생을 무자비한 약탈자로 살아온 풍양이다.

지금껏 무수히 많은 이들의 재물을, 혹은 목숨을 빼앗았지만, 자신이 이런 최후를 맞이할 것이라고는 꿈에도 생각하지 못했다.

“이제, 이제 제발 잠력단을…….”

흐릿한 시선 속, 고개를 가로젓는 진태경의 모습에 그가 애처롭게 중얼거렸다.

“왜? 어째서?”

그러나 대답은 다른 곳에서 들려왔다.

“뭐라? 어째서?”

“저 찢어 죽여도 시원찮을 놈이……!”

살아남은 항산검문의 무인들이 살기 어린 눈빛으로 각자의 병장기를 움켜쥐었다.

이소월 역시 입술을 깨물며 풍양에게로 활을 겨눴지만 진태경이 황급히 만류했다.

“막타 자제 좀…… 아니, 편안하게 죽이기에는 너무 악랄한 놈입니다. 저렇게 천천히 죽어 가도록 두는 게 나아요.”

짧은 시간, 이소월은 결국 수많은 갈등 끝에 활을 내렸다. 그러자 진태경이 풍양에게로 다가가 귓가에 작은 목소리로 속삭였다.

“나도 슬슬 힘들다. 이제 죽자.”

무슨 소리인지는 모르겠지만 하나는 확실하다.

죽음. 풍양은 자신의 죽음이 코앞으로 성큼 다가왔음을 깨달았다.

“원귀가 되어서라도 복수해 주마.”

“아멘. 부디 다음 생에는 비아그라 정도로 만족해라.”

풍양은 헛웃음을 터트렸다. 마지막 순간까지 저놈의 뜻 모를 헛소리를 들어야 하는 자신의 처지가 우습기 짝이 없었다.

‘제기랄. 날씨 하고는.’

고개를 들어 바라본 하늘은 온통 붉었다. 그리고 이내 암흑으로 물들었다.



* * *



스르륵.

풍양의 고개가 꺾임과 동시에 허공에서 축포가 터졌다.

띠링. 띠링. 띠링!



- [Lv.85 풍양]을 처치했습니다!

- [잠력단] 퀘스트를 성공적으로 완료했습니다!

- 막대한 경험치와 명성을 얻었습니다!

- 레벨 업!

- 레벨 업!

.

.



자그마치 다섯 번의 레벨 업과 명성치 상승을 알리던 시스템창은 이윽고 더 반가운 소식을 전해 주었다.



- 퀘스트 성공 보상이 인벤토리에 지급되었습니다!

- 퀘스트 성공 보상으로 [완전 회복]이 즉각 적용됩니다!



‘완전 회복?’

즉각 적용이라더니, 그 말대로 변화는 순식간에 일어났다.

금이 가고 부러졌던 뼈가 붙고, 베이거나 찔린 상처는 씻은 듯이 아물었다. 변화는 외관에서 그치지 않았다.

‘내상이…….’

신체 내부에서도 보이지 않는 회복이 이루어졌다. 모든 내상이 낫는 것까지는 예상했지만 생각한 것 이상의 소득도 있었다.



- [내상]이 모두 회복됩니다!

- 안정된 신체가 새로운 기운을 받아들입니다!

- [열화신단]을 완전히 흡수했습니다!

- [공력]이 45년으로 상승합니다!

- [공력-열양지기]의 특성이 부여됩니다!



열화신단의 완전한 흡수. 그리고 비약적으로 상승한 공력.

사지백해에 가득 찬 힘이 느껴진다. 용암처럼 내 몸을 태우던 열양지기는 어느새 따뜻한 봄바람이 되어 있었다.

‘해냈구나.’

레벨 업을 해서 몸이 어느 정도 회복되면 바로 운기조식으로 열양지기를 다스릴 생각이었는데…… 시스템 덕분에 어려운 일을 손쉽게 해치웠다.

‘세상에, 45년이면 얼마야.’

원래 가지고 있던 것에 비해 세 배, 자그마치 반 갑자(30년)의 공력이 추가로 늘어난 것이다.

‘반 갑자라.’

평범한 상황이었다면 열화신단을 복용하는 것은 뒤로 미뤄졌을 것이다. 그러나 도박처럼 시도했던 일이 신의 한 수가 되어 돌아왔다.

‘천운이 따라 주지 않았다면 죽었겠지만.’

두 번의 천운. 그중 하나는 열화신단이고, 다른 하나는 지금 내 손에 들려 있는 [이름 없는 검]이다.

모두 몇 달 전 조필을 쓰러트리고 얻은 전리품들.

‘이게 아니었으면 정말 큰일 날 뻔했어.’

그저 다른 검들보다 조금 더 날카롭고 단단한 검이라고 생각했는데, 이게 사실은 만년한철이고, 그런 효능이 있는 줄은 꿈에도 몰랐다.

그런 의미에서 오늘의 내게는 운칠기삼(運七技三)이 아니라 운구기일(運九氣一)이라는 말이 더 어울린다.

‘이걸 운이 좋다고 해야 할지는 모르겠지만.’

나는 천천히 주위를 둘러보았다. 거꾸로 꽂힌 병장기의 무덤, 누군가는 한가득 고인 피 웅덩이에 얼굴을 처박은 채로 죽었고 누군가는 부릅뜬 눈으로 여명이 밝아 오는 하늘을 바라보고 있다. 그런 시신들이 무려 수백에 이른다.

“여기 생존자가 있다!”

“춘삼아! 정신 좀 차려 보거라!”

그 참혹한 광경 속에서 부지런히 움직이는 항산검문의 무인들. 몇 안 되는 생존자들을 일사불란하게 구해 내는 그들을 보고 있는데 문득 알 수 없는 위화감에 휩싸였다.

‘뭐지?’

뭔가 중요한 사실 하나를 잊은 것 같은데…….

눈살을 찌푸리던 그때, 죽은 듯이 누워 있던 시체 하나가 상반신을 일으켰다.

“크으으으.”

“아.”

그래, 반갑다 무경아.



* * *



장장 두 시진에 걸친 수색 작업이 끝났을 때쯤, 이소월의 몸은 핏물로 흠뻑 젖어 있었다.

“생존자는?”

“문주님을 포함…… 스물다섯입니다.”

“몇 명이라고?”

“스물다섯 명입니다. 그중 다섯은 오늘을 넘기기 힘들 것 같습니다.”

물어본 이소월도, 대답한 무인도 입을 다물었다.

한때 태원진가와 함께 산서성을 양분하던 항산검문은 이제 더 이상 존재하지 않는다. 남은 것은 부상자들과 약관도 되지 않은 어린 문주뿐이다.

‘이곳을 버리고 도망쳤다면, 처음부터 풍양의 혼인 제안을 받아들였다면 그들을 살릴 수 있었을까?’

후회는 언제나 부질없다. 그러나 이소월은 후회해야 했다.

비록 얼마 남지 않았지만, 그녀는 여전히 일문(一門)의 문주였다. 뼈에 사무치게 고민하고 후회해야 이후에 같은 실수를 하지 않는다.

그것이 오늘 죽은 이들을 위한 속죄고 남은 이들을 위한 노력이다.

‘항산검문은 반드시 살아남는다. 본문을 위해 목숨을 바친 그대들을 위해서라도.’

이소월은 주먹을 움켜쥐었다. 활시위를 당기며 깨진 손톱이 살을 파고들며 피가 배어 나왔지만 고통도 느끼지 못했다.

“다른 사람들은?”

“모두 대전에 있습니다. 태원진가 측에 제법 의술을 아는 여인이 있어 그녀가 부상자들을 돌보는 중입니다만…….”

무인의 낯빛이 어두워졌다. 그만큼 몇몇 부상자들의 상태가 안 좋다는 증거다. 이소월은 더 이상 묻지 않고 대전을 향해 걸음을 옮겼다.

‘추스르기도 전에 또다시 떠나보내는구나.’

참을 수 없는 피로가 전신을 짓눌렀지만 정신력으로 버텼다. 적어도 떠나는 이들의 마지막은 지켜야 하지 않겠는가.

끼이이익.

대전으로 들어서자 태원진가에서 온 이들은 보이지 않았고, 누워 있는 부상자들이 곧장 눈에 띄었다.

항산호 철무백과 십수 명의 무인들이 그녀를 발견하고 말을 건넸다.

“아, 소월이 왔느냐?”

“오셨습니까. 문주님!”

“문주님을 뵙습니다!”

“……?”

기분 탓인가. 어쩐지 죽어 가는 것치고는 다들 활기가 넘친다. 한동안 말없이 그들을 바라보던 이소월은 활기의 정체를 깨달았다.

“회광반조(回光返照)…….”

그제야 저들의 얼굴 위에 짙게 드리운 죽음의 그림자가 보인다. 그녀가 터지려는 울음을 참으며 황급히 돌아선 그 순간이었다.

쿵!

뭔가 단단한 것에 이마를 부딪친 이소월이 비틀거렸다. 쓰러지려는 그녀의 어깨를 크고 단단한 손바닥이 감쌌다.

“아이고, 조심 좀 하시지. 괜찮아요?”

“아, 네.”

“그럼 됐고.”

이소월을 내려다보던 진태경이 피식 웃었다.



* * *



‘회광반조는 무슨.’

새어 나오려는 실소를 간신히 참았다. 철무백과 다른 부상자들은 다들 팔팔하게 살아나는 중이다.

아, 물론 진무경도 마찬가지고.

‘나 아니었으면 어쩔 뻔했나.’

정확히 말하면 퀘스트 보상이 아니었으면 저들 중 절반은 초상을 치렀을지도 모르겠다.

각각 서른 개씩이나 보상으로 지급받은 [뛰어난 금창약]과 [십년하수오]는 외상과 내상 치유에 뛰어난 효과가 있었다.

‘만약을 대비해서 아낄까도 생각해 봤지만…….’

사람이 죽어 가는데 모른 척할 정도로 모진 놈은 아니다. 물론 수량이 많았던 것도 한몫했다.

“안 들어가요?”

“네?”

“안 들어가실 거면 나 먼저 들어가고.”

어쩐지 멍한 채로 선 이소월을 지나치려다가 문득 잊고 있던 게 생각났다. 가만있자, 그걸 어디 뒀더라?

“아, 여기 있다.”

품을 뒤지는 척하면서 인벤토리에서 죽간 하나를 꺼냈다.

“여기요. 우리 형…… 아니, 소가주님이 보내시는 거.”

이소월이 얼떨떨한 얼굴로 죽간을 받아 들기가 무섭게 시스템 알림이 울렸다.

띠링.



- 초대장 전달을 완료했습니다.

- 퀘스트, [어제의 적, 오늘의 동지]를 완수했습니다!



초대장 전달. 두 번 했다가는 사람 잡겠다.
```

## Current accepted English baseline

```markdown
# Chapter 120

*Shwick!*

A sword thrust forward—slowly, but with tremendous force.

For the briefest moment, a mocking smile appeared at the corner of Pung Yang’s mouth.

*I knew this was coming.*

He had spent decades living on a plateau where every kind of underhanded trick ran rampant. If he had been foolish enough to fall for the same trick twice, he would have become wild-dog food long ago.

*But where did that sword come from?*

It wasn’t a dagger. Where had the brat hidden a longsword that size?

With that slight question in mind, Pung Yang drew up his Body-Protecting Qi.

*Fssssss.*

He had expected this, so his response was quick. Red qi surged upward in an instant and wrapped tightly around his body.

Body-Protecting Qi was invincible armor that nothing short of powerful Sword Energy could put so much as a scratch on. The young brat’s futile struggle was nothing but laughable.

*What an annoying bastard. Just die already.*

He was about to snap Jin Taekyung’s neck in a single motion when—

*Thud!*

“……Huh?”

A chilly coldness pierced into his body, followed by searing pain. Pung Yang stared wide-eyed at the sword that had pierced straight through his chest.

*What the hell?*

His Body-Protecting Qi had vanished.

No—it had been destroyed.

Jin Taekyung’s sword sliced through it as easily as cutting tofu, then pierced Pung Yang’s chest as well.

Pung Yang looked down at the transparent blade, not a drop of blood staining it, and muttered like he was groaning.

“Ten-Thousand-Year Cold Iron……?”

He had heard of it before. Stories about a divine weapon said to be capable of cutting and breaking anything in the world.

“How did you get this?”

Pung Yang glared at the sword’s owner with a twisted expression. The young brat from the Jin Family of Taiyuan blinked innocently before opening his mouth.

“Wow. This actually worked.”

“You fucking bastard……!”

He wanted to snap the brat’s neck right away, but his vision suddenly went hazy, and the strength drained from his fingers. The power that had filled his body vanished like the outgoing tide, leaving only helplessness in its wake.

*The Temporary Strength Pill had to wear off now of all times.*

Blood began flowing from the seven openings in Pung Yang’s face as he staggered backward.

His various injuries, both great and small, combined with the dispersal of his Body-Protecting Qi. The internal energy surging backward through his body began driving him rapidly toward death.

*I can’t die like this. I can’t.*

Pung Yang hurriedly searched inside his robes.

He still had one Temporary Strength Pill left. If he took it, he could beat the bastards to death in a single stroke and leave this place. He had lost quite a lot, but he could recover, then return to the Murim.

Yes. If he just took the Temporary Strength Pill……

*Clatter.*

Damn it. He was too desperate.

The wooden box slipped from Pung Yang’s frantic hand, struck the ground, and sprang open. A pill tinged with a blood-red color rolled across the ground before coming to a stop beneath someone’s foot.

“Oh, is this the Temporary Strength Pill?”

Jin Taekyung picked it up and examined it with curiosity. Pung Yang shouted at him.

“G-Give it to me! Hurry!”

“Here’s a question. Do you think I’ll give it to you just because you ask?”

“You bastard!”

Pung Yang threw himself forward with all his remaining strength, but his ruined body had already reached its limit. Before he could reach Jin Taekyung, his legs gave out and he collapsed.

Only one path remained to Pung Yang now.

“Please. I’m begging you. Give it to me. Give it to me!”

“What if I do?”

Pung Yang cried out desperately.

“You’ll never see me again. No—instead, I’ll swear my loyalty to you from now on!”

“Oh, having a Peak master as a subordinate. That sounds pretty good.”

“R-Really? Then hurry and give me the Temporary Strength Pill!”

“First, I’m taking my property back.”

“Your property?”

His question was answered a moment later. Jin Taekyung approached and yanked the sword from the center of Pung Yang’s chest.

Blood poured out like a waterfall, accompanied by dizzying pain.

“Gueeeeegh!”

Pung Yang did not even notice that chunks of his internal organs were mixed into the blood he vomited.

All he felt was his vision gradually darkening and the sounds around him receding into the distance.

He was dying, and desperation had driven him half-mad.

*I want to live.*

Pung Yang had spent his entire life as a ruthless marauder.

He had stolen the wealth—and sometimes the lives—of countless people, but he had never once imagined that he would meet an end like this.

“Now, now, please give me the Temporary Strength Pill……”

Through his blurred vision, he saw Jin Taekyung shake his head. Pung Yang mumbled piteously.

“Why? Why not?”

But the answer came from somewhere else.

“What? Why?”

“That bastard deserves to be torn limb from limb!”

The surviving martial artists of the Mount Heng Sword Sect gripped their weapons, their eyes brimming with killing intent.

Lee Seowol also bit down on her lip and drew her bow toward Pung Yang, but Jin Taekyung hurriedly stopped her.

“Let’s lay off the finishing blow for now…… No, he’s too vicious to let him die comfortably. It’s better to leave him there and let him die slowly.”

For a brief while, Lee Seowol struggled with herself. In the end, she lowered her bow. Jin Taekyung approached Pung Yang and whispered softly into his ear.

“I’m starting to get tired too. Let’s just die now.”

Pung Yang didn’t know what he meant, but one thing was certain.

Death.

Pung Yang realized that his own death was almost upon him.

“Even as a vengeful ghost, I’ll have my revenge.”

“Amen. In your next life, be satisfied with Viagra.”

Pung Yang gave a hollow laugh. It was absurd that he had to listen to that bastard’s incomprehensible nonsense until the very end.

*Damn. What terrible weather.*

He raised his head and looked at the sky. It was dyed entirely red.

Then it was swallowed by darkness.

* * *

As Pung Yang’s head lolled to the side, celebratory fireworks burst overhead.

*Ding. Ding. Ding!*

> **System**
> - Defeated **Lv. 85 Pung Yang**!
> - Successfully completed the **Temporary Strength Pill** Quest!
> - Obtained a massive amount of **EXP** and **Fame**!
> - Level Up!
> - Level Up!
> - …

After announcing five level-ups and an increase in Fame, the System window delivered even better news.

> **System**
> - The Quest success reward has been delivered to your **Inventory**!
> - **Full Recovery** has taken effect immediately as the Quest success reward!

*Full Recovery?*

It said the effect would be immediate, and the change happened exactly as promised.

Cracked and broken bones knitted back together. Cuts and punctures healed as if they had been washed clean. The changes did not stop at the surface.

*The Internal Injuries……*

Invisible healing took place inside my body as well. I had expected all my Internal Injuries to heal, but there was an even greater benefit than I had imagined.

> **System**
> - All **Internal Injuries** have healed!
> - Your stabilized body accepts new qi!
> - The **Blazing Flame Divine Pill** has been fully absorbed!
> - Your **internal energy** has risen to 45 years!
> - Your **internal energy** has gained the **Scorching Yang Qi** attribute!

The Blazing Flame Divine Pill had been completely absorbed.

And my internal energy had risen explosively.

I could feel power filling every limb and bone. The Scorching Yang Qi that had burned through my body like lava had somehow become a warm spring breeze.

*I did it.*

I had planned to circulate my qi and control the Scorching Yang Qi once my body recovered somewhat from the level-ups, but thanks to the System, I had handled the difficult part with ease.

*Forty-five years? How much is that?*

Compared to what I had originally possessed, it was three times as much—an additional half a jiazi, or thirty years, of internal energy.

*A half jiazi.*

Under normal circumstances, I would have put off taking the Blazing Flame Divine Pill. But the gamble I had taken had come back as a masterstroke.

*I would have died if luck hadn’t been on my side, though.*

Two strokes of heavenly luck.

One was the Blazing Flame Divine Pill, and the other was the **Unnamed Sword** in my hand.

Both were loot I had obtained after defeating Jopil several months ago.

*I would have been in serious trouble without this.*

I had thought it was merely a sword that was a little sharper and harder than other swords. I had never dreamed that it was actually Ten-Thousand-Year Cold Iron, or that it possessed such an ability.

In that sense, the saying *seven parts luck and three parts skill* didn’t suit me today. *Nine parts luck and one part qi* was much more appropriate.[^1]

*Though I’m not sure this can really be called good luck.*

I slowly looked around.

A graveyard of weapons stood with their hilts buried upside down. Some people had died with their faces planted in pools of blood. Others stared wide-eyed at the sky as dawn began to break.

There were hundreds of corpses like that.

“There’s a survivor here!”

“Chunsam! Come around!”

Amid that horrific scene, the martial artists of the Mount Heng Sword Sect moved tirelessly. As I watched them rescue the few survivors with disciplined efficiency, I was suddenly seized by an inexplicable sense of wrongness.

*What is it?*

It felt like I had forgotten something important……

Just as I was frowning, one of the corpses that had been lying motionless raised its upper body.

“Guuuuuh.”

“Oh.”

Right. Good to see you, Mukyung.

* * *

By the time the four-hour search was over, Lee Seowol’s body was soaked in blood.

“How many survivors?”

“Twenty-five, including you, Sect Leader.”

“How many did you say?”

“Twenty-five. Five of them probably won’t make it through today.”

Both Lee Seowol, who had asked the question, and the martial artist who answered it fell silent.

The Mount Heng Sword Sect, which had once divided control of Shanxi with the Jin Family of Taiyuan, no longer existed. All that remained were the injured and a young Sect Leader who was not even twenty years old.

*If I had abandoned this place and fled, if I had accepted Pung Yang’s marriage proposal from the beginning, could I have saved them?*

Regret was always pointless.

But Lee Seowol had to regret.

Although few remained, she was still the Sect Leader of a sect. Only by agonizing over her mistakes and regretting them to the bone could she avoid making the same mistakes again.

That was her atonement to those who had died today and her effort on behalf of those who remained.

*The Mount Heng Sword Sect will survive. If only for those who gave their lives for our sect.*

Lee Seowol clenched her fist. Her fingernails, broken from drawing the bowstring, dug into her flesh as she clenched her fist. Blood seeped out, but she felt no pain.

“What about the others?”

“They’re all in the main hall. There’s a woman from the Jin Family of Taiyuan who knows a fair amount about medicine, and she’s treating the wounded, but……”

The martial artist’s expression darkened. It was proof of just how bad the condition of some of the wounded was.

Lee Seowol did not ask anything else and headed toward the main hall.

*I’m sending them off again before we’ve even had time to recover.*

Unbearable fatigue pressed down on her entire body, but she held on through sheer willpower.

At the very least, she had to see off those who were leaving.

*Creeeeak.*

When Lee Seowol entered the main hall, the people from the Jin Family of Taiyuan were nowhere in sight. The wounded lying on the floor immediately caught her eye.

The Tiger of Mount Heng, Cheol Mubaek, and more than a dozen martial artists noticed her and called out.

“Ah, Seowol. You’ve come?”

“You’re here, Sect Leader!”

“We greet you, Sect Leader!”

“……?”

Was it just her imagination?

For people who were supposedly dying, they seemed strangely full of energy. After silently staring at them for a while, Lee Seowol realized what that energy meant.

“A final rally……”

Only then did she see the dark shadow of death lying heavily across their faces.

Just as she hurriedly turned away to hold back her tears—

*Bang!*

Lee Seowol staggered after striking her forehead against something solid. As she began to fall, a large, firm hand caught her shoulder.

“Oh, careful there. Are you all right?”

“Ah, yes.”

“Then we’re good.”

Jin Taekyung looked down at Lee Seowol and let out a short laugh.

* * *

*Some final rally.*

I barely held back a snort.

Cheol Mubaek and the other wounded were all recovering vigorously.

Of course, Jin Mukyung was no exception.

*What would they have done without me?*

To be precise, if not for the Quest rewards, there might have been funerals for half of them.

The thirty **Superior Wound Medicines** and thirty **Ten-Year He Shouwu** I had received as rewards each had remarkable effects on external and Internal Injury healing.

*I did consider saving them in case of an emergency……*

But I wasn’t heartless enough to ignore people dying right in front of me.

Of course, the sheer quantity had played a part too.

“Aren’t you coming in?”

“What?”

“If you’re not going in, I’ll go in first.”

I was about to walk past Lee Seowol, who was standing there in a daze, when I suddenly remembered something I had forgotten.

*Wait. Where did I put that?*

“Ah, here it is.”

I pretended to rummage around inside my robes and pulled a bamboo slip from my Inventory.

“Here. It’s from my hyung…… no, from the Lesser Family Head.”

Lee Seowol accepted the bamboo slip with a bewildered expression.

The System notification rang the instant she took it.

*Ding.*

> **System**
> - Invitation delivery complete.
> - Quest **Yesterday’s Enemy, Today’s Ally** completed!

Invitation delivery.

If I had to do that twice, someone was going to die.

[^1]: A playful variation on the Korean saying *seven parts luck, three parts skill*, replacing skill with *qi* and shifting the balance even further toward luck.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 120`.

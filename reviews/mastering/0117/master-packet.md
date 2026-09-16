# Master Edit Task — Chapter 117

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
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 조필     | **Jopil**          |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 화산파    | **Huashan**                      |
| 남궁세가   | **Nangong Family**               |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 검법     | **sword technique**                              |                                                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 정파     | **orthodox faction**                             |                                                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 체력               | **Stamina**                    |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 태산압정 | **Mount Tai Presses Down on the Crown** | First move of the Three Calamities Sword Technique. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 격산타우 | **Striking the Ox Across the Mountain** | Palm technique that transmits force through an intervening defense. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 매화검법 | **Plum Blossom Sword Technique** | Huashan sword technique Cheongpung performed at age ten. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
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
| 진위경 | 이소월 | host_to_new_sect_leader | Young Lady | formal-polite | Jin Wikyung addresses Lee Seowol as 소저 before accepting her oath. |
| 이소월 | 진위경 | new_sect_leader_to_lesser_family_head | Lesser Family Head | formal-deferential | Lee Seowol refers to Jin Wikyung as 소가주님 when describing his summons. |
| 철무백 | 진위경 | sect_elder_to_lesser_family_head | Lesser Family Head | formal-deferential | Cheol Mubaek formally greets Jin Wikyung as the Lesser Family Head of the Jin Family of Taiyuan. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진태경 | 이소월 | young_martial_artist_to_allied_sect_leader | Young Lady Lee | formal-polite | Taekyung uses 이 소저 while greeting Seowol at the banquet. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 110–114

## Plot

Cheol Mubaek, the Peak-level Tiger of Mount Heng, stops the Mount Heng Sword Sect’s elders from abandoning Lee Cheonbaek’s final wishes and forces them to recognize Lee Seowol as their Sect Leader. Seowol refuses to flee despite the sect’s overwhelming disadvantage, preparing a desperate defense with oil hidden throughout the estate while awaiting Jin Taekyung and Jin Mukyung.

Pung Yang leads more than two hundred Red Wind Band mounted bandits in surrounding Mount Heng. He offers Seowol a choice between total destruction and marriage, intending to preserve the sect’s useful forces under his control. Cheol kills the envoy, prompting the assault. The sect’s defenses initially repel the attackers, and Seowol’s concealed fire attack burns many mounted bandits, but the gate and walls eventually fall. Cheol holds the breached gate alone until Pung Yang confronts him.

Pung Yang swallows an unidentified red pill from a hard wooden case and gains enough power to defeat the mature Peak master Cheol, breaking all four of his limbs and severely injuring him. The surviving defenders retreat to a watchtower, where Seowol continues fighting until exhausted and signals Cheol with a fire arrow. Pung Yang reaches her and renews his demand that she marry him.

Taekyung, Mukyung, Mujin, and Wolhwa arrive at the fortress after a forced ride under Taekyung’s time-limited Peak Quest. Cheol recognizes Taekyung’s Taiyuan Jin Family affiliation, leaving the Jin party as the Mount Heng Sword Sect’s only immediate hope.

## Continuity

- Taekyung, Mukyung, Mujin, and Wolhwa have reached the Mount Heng Sword Sect after racing against the Quest’s irreversible twenty-two-hour deadline.
- Taekyung is Level 55; Mujin is Level 38.
- The Red Wind Band began the assault with more than two hundred mounted bandits, suffered at least one hundred casualties in the fire attack and initial fighting, and still retains more than one hundred fifty when Pung Yang enters personally.
- Pung Yang is an early Peak master whose saber and throwing-knife techniques are highly developed; the red pill temporarily raises his power far beyond Cheol Mubaek’s.
- Pung Yang possesses an unidentified hard wooden case containing the red pill and possibly a weapon or other anti-tiger object.
- Cheol Mubaek is alive but has four broken limbs and severe internal injuries. He refuses to surrender the single-successor Shura Annihilating Fist, though he fears for Lee Seowol’s safety.
- The Mount Heng fortress wall has been overrun. Lee Seowol and the remaining defenders are surrounded at the watchtower, while Pung Yang demands her marriage.
- Lee Seowol remains Sect Leader by choice and has not accepted Pung Yang’s demand.
- The Mount Heng Sword Sect’s survival, Seowol’s response, and Taekyung’s ability to rescue her and Cheol remain unresolved.
- The nature and origin of Pung Yang’s red pill remain unknown.
- The Peak Quest’s required invitation to the Jin Family for the coming Lunar New Year remains the governing objective.

## Translation Decisions

- Retain **Peak**, **early Peak**, **First Rate**, **shichen**, **Red Wind Band**, **mounted bandits**, **Sect Leader**, **Young Lady**, and **Taiyuan Jin Family**.
- Render **수라멸권** as **Shura Annihilating Fist**.
- Render **항산권문** as **Mount Heng Fist Sect**; retain **Mount Heng Sword Sect** where that established sect name is used.
- Render **화시** as **fire arrow**, **쇠뇌** as **crossbow**, **충차** as **battering ram**, and **벽곡단** as **fasting pills**.
- Render **멸문지화** as **total destruction**, **혼인 예물** as **wedding gift**, and **동귀어진** as **perishing together**.

### Prior accepted reading-copy tails

#### Chapter 115 tail (verified mastered)

…
the Blood Wolf Sword’s secret martial art and the Tiger of Mount Heng’s martial arts formula would be enough. Ah, I should take that old man Cheol with me on the way back, too.” “…Uncle Cheol is still alive?” “Of course. How could I kill a Benefactor who’s going to hand over such a precious martial arts formula?” “…” “I’ll stake my life on this promise. It’s not too late even now, so marry me. If you do, I’ll let everyone live. I’ll stop at destroying their dantians.” That was the decisive blow. Lee Seowol’s eyelashes trembled for a while before she slowly lowered her hand. “Keep your promise.” “A wise choice.” A triumphant smile spread across Pung Yang’s face. As of today, he would begin his third life. He had gone from a beggar boy to a mounted bandit. Now he would finally don the mask of the orthodox faction and become the true master of the Mount Heng Sword Sect. Though there had been heavy losses, it didn’t matter. New wine belonged in new wineskins. Under the name of the Mount Heng Sword Sect, he would recruit martial artists and expand his power. *If the Blood Wolf Sword could do it thirty years ago, why can’t I?* Just as the corners of his mouth lifted with overflowing delight— “Pung Yang!” A shout infused with internal energy shook heaven and earth. Lee Seowol, Pung Yang, and every survivor turned their heads as if on cue. A young man dressed in robes as black as night was walking toward them from some fifty *jang* away.[^1] *A master.* The young man’s needle-sharp gaze sent a chill through a corner of Pung Yang’s chest. He was a master. More than that, he was a Peak master in no way inferior to Pung Yang himself. Pung Yang could tell just from the way the young man’s hand moved as it gripped his sword hilt. *There are only two Peak masters this young in Shanxi Province. And if he’s a swordsman…* The answer came immediately. Jin Mukyung, the Heaven Shaking Sword. A genius who had reached the Peak realm at barely twenty years of age. More importantly, behind him stood the Jin Family of Taiyuan, which had risen to become the foremost family in Shanxi. *At least he came alone.* But the next moment, another person cautiously stuck his head out through the fortress gate Jin Mukyung had entered. The young man wore a navy martial robe. His clothing, the dark iron spear in his hand, and above all, his nearly identical face told Pung Yang who he was. “The Sleeping Dragon of Shanxi?” Jin Taekyung flinched at the nickname someone blurted out and muttered, “Fuck. I knew this would happen.” Cursing crudely in a manner unbecoming a scion of a prestigious family, Jin Taekyung came sauntering forward beside the leisurely Jin Mukyung. The two brothers were heading straight toward Pung Yang. *The Taiyuan Jin Family, at a time like this… This is very bad.* The reputation the family had built over many years, combined with the fame it had earned in the battle at Eight Spring Gorge, had left the Jin Family’s current standing unrivaled. As a result, countless young people across Shanxi Province who dreamed of becoming martial artists were flocking to the Jin Family. That was why, even if Pung Yang swallowed the Mount Heng Sword Sect right now, he would still have to bow flat and hide his claws. *Once I get past this hurdle, my opportunity will come.* The Mount Heng Sword Sect had already collapsed. The Murim was a world where the strong preyed on the weak, and Pung Yang was a new power in that world. Even if his opponent was the Taiyuan Jin Family, he believed he had earned the right to be treated with respect. Clomp. Clomp. Clomp. With every step Jin Mukyung and Jin Taekyung took, the Red Wind Band’s mounted bandits scattered out of their way. When the brothers reached him, Pung Yang clasped his hands in salute. “I am Pung Yang, Red Wind Band Leader.” Had Pung Yang not been a seasoned martial artist who never let down his guard—had the effects of the Temporary Strength Pill not still lingered faintly—he would never have evaded that strike. Shiiiiing! He hurriedly twisted aside. A dazzling streak of Sword Energy skimmed past his neck and sliced through three mounted bandits behind him. “Is this the will of the Taiyuan Jin Family?” Jin Taekyung, who had already felled the nearby mounted bandits, muttered, “I’d rather talk it out.” “You fucking bast—” Before Pung Yang could finish speaking, another streak of Sword Energy flew in and grazed his back. Pain seared through him like fire. He barely evaded the attacks that followed and revised his assessment of Jin Mukyung. *He’s stronger than me.* At this level, Jin Mukyung’s movements were comparable to Cheol Mubaek’s. On top of that, Jin Taekyung was slaughtering Pung Yang’s subordinates. Pung Yang realized he had only one option left. *The Temporary Strength Pill.* While his subordinates died one after another trying to stop Jin Mukyung, Pung Yang pulled the wooden case hidden inside his robes and tipped the pill into his mouth. Shiiiiing! Jin Mukyung’s blue Sword Energy was reflected in Pung Yang’s eyes, which had turned blood-red. Slice! [^1]: A *jang* is a traditional unit of distance, roughly three meters.

#### Chapter 116 tail (verified mastered)

…
“Two hundred moves. I’ll finish you before then.” “Are you even capable of that?” “Before cutting off your limbs, I should pull out your tongue first. Listening to you has been pissing me off for a while now.” “Be grateful you didn’t have to fight my younger brother. If he were your opponent, you’d have already plugged your ears and killed yourself. He’s mastered the art of making fun of people.” “The Sleeping Dragon of Shanxi? Then I suppose I should pull his tongue out too.” “…That actually sounds kind of appealing.” “Enough nonsense. Raise your sword. That way, you can struggle for even a moment longer before you die.” The instant Pung Yang’s red eyes gleamed eerily, immense internal energy surged from his lowered saber. Fwoooosh! When internal energy was infused into a medium and given tangible form, it was called Sword Energy. But after taking the Temporary Strength Pill, Pung Yang had now surpassed that realm. “Sword Force…” A Supreme Peak master. It was the symbol of those known as Martial Gods. Though his enlightenment was insufficient for it to be called true Sword Force, there was no doubt that he had reached the very pinnacle of the Peak realm. “Well, damn.” Jin Mukyung let out a hollow laugh. How many years would Pung Yang have needed to reach that realm through training alone? Ten? Twenty? But one tiny red pill had allowed him to leap over all those years—the contemplation of martial principles, the endless training, the blood and sweat. It had let him surpass all of it. “What kind of son of a bitch made something like that…” Tsssss. Sword Energy rose from Jin Mukyung’s sword as well. Pung Yang spoke with open contempt. “Last two hundred moves, and I’ll let you live.” “Yeah, go fuck yourself.” Fwoooosh! As he watched the Sword Force plunge down as though to split heaven and earth, Jin Mukyung suddenly thought he was beginning to resemble his insolent youngest brother. *But what is that guy doing, taking so long to get here?* KABOOOOM! * * * Rumble, rumble, rumble. The ground shook as though an earthquake had struck. I had no idea what kind of battle was taking place thirty jang away, but I knew one thing. *I can’t go over there.* I wasn’t joking. If I got caught up in that fight, I’d probably die. I had no desire to personally experience what happened when a First Rate got its back broken between Peak masters. And more importantly… Whoosh! Slice! “Gueeegh.” I had more than enough on my hands here. At this point, I might not be able to take on a hundred men, but I had to be good for at least seventy. I swung my weapon like a madman, drenched in the blood pouring down around me. Shwaaak! I caught the cavalry spear thrusting toward my side and pulled it toward me. I drove it into the stomach of the man bringing his saber down behind me, then chopped through the shaft with the edge of my hand. Crack! “Gasp!” “Use an iron spear next time. Something heavy and sturdy. You could even do squats with it. How great is that?” With that friendly advice, I smashed my fist into the mounted bandit’s jaw. His body went limp as his jawbone shattered. Shraaaaak! *Throat, side, leg.* I could read the daggers thrusting toward me from three directions without even looking. How could every last one of them be so slow and predictable? I was also genuinely amazed by myself. In that brief moment, I could think of a response and put it into action. Tap. Crack! I put my weapon into my Inventory, freeing my hands. As I simultaneously caught the wrists of the men stabbing toward my throat and side and broke them, I kicked backward with my leg fully extended. Their short screams and the dull impact told me I had struck exactly where I intended. *More. More. More.* My hands moved faster and faster, while the sounds around me grew more distant. Every time I brushed against the bodies of the enemies surrounding me, weapons summoned from my Inventory appeared and vanished. Stab. Slash. Swing. Broke. How many had I brought down? At some point, the noise that had been pushed far away came rushing back all at once. Thud. “Ggh…” “Urgh.” The dead lay motionless with their faces buried in the cold dirt. The survivors rolled around, groaning. The twenty or so mounted bandits who had escaped death and injury backed away from me. “T-the Sleeping Dragon of Shanxi…” One step. Two steps. Terrified, they retreated as I advanced, forgetting that furious enemies were still behind them. Shraaaaak! Thud! “Kill them! Kill every last mounted bandit!” “You fucking bastards!” They were the martial artists of the Mount Heng Sword Sect who had survived and fought to the bitter end. Caught by the surprise attack of those bloodshot-eyed men, the mounted bandits fell like dominoes. “Kyaaaagh!” “P-please, spare me…!” Everywhere I looked, the ground overflowed with corpses, blood, and groans. How many mounted bandits had died here today? Two hundred? Three hundred? I didn’t know. What I did know was that this battle would not end until one man died. *Pung Yang.* It was time to deal with that cheating, pill-popping bastard. “…” *I can do this, right? I should be able to. Probably…*

## Korean source

```text
＃117화



진무경은 그간 수많은 무공을 익혔다. 그중에는 과거 한 시대를 풍미한 절정 무공부터, 촌구석 좌판에서조차 쉽게 찾아볼 수 있는 삼류 무공까지 가리는 일도 없었다.

그러나 지금 이 순간, 그는 깨달았다.

‘강하다. 내가 지금까지 익힌 어떤 무공보다.’

후우우웅.

일도양단의 기세로 떨어지는 한 자루의 곡도.

남궁세가의 제왕검형, 화산파의 매화검법 같은 초절정의 무공이 아니다. 이건 길거리 삼류 잡배도 안다는 삼재검법의 일초, 태산압정(泰山壓頂)이었다.

‘태산을 누른다. 어떤 느낌인지 알 것 같군.’

도신 위로 일렁이는 붉은 도기(刀氣)는 태산을 누르는 것으로도 모자라 쪼갤 수도 있을 것 같다.

‘막을 수 없어.’

찰나에 불과한 시간, 진무경은 망설임 없이 몸을 날렸다.

쏴아아악!

아슬아슬하게 진무경의 옷깃을 스친 도기가 땅에 닿았다. 어떤 굉음도, 진동도 없이 지면이 쩍 갈라지는 광경은 전율 그 자체였다.

“이걸 피해?”

그러나 정작 풍양은 이 결과가 마음에 들지 않았다.

전력을 다한 일격이었다. 잠력단의 효능을 십이 할 끌어올렸음에도 진무경에게 작은 상처 하나 입히지 못했다.

‘항산호도 받아치는 게 고작이었는데.’

완숙한 절정 고수인 철무백조차 그 대가로 내상을 입고 물러나야 했다. 그런데 이립도 되지 않은 애송이가 어떻게?

“진천검…… 이름값은 한다 이거지?”

자세를 고쳐 잡은 진무경이 덤덤하게 대꾸했다.

“이 정도는 피해야지.”

“막을 수 없었던 건 아니고?”

풍양의 입가에 비웃음이 떠올랐다.

“하긴, 그 대단한 태원진가의 자제께서 나려타곤(懶驢打滾)으로 도망칠 정도니 오죽 다급했을까.”

나려타곤. 게으른 당나귀가 바닥을 구르는 모습에 빗댄 말이다. 위신을 중요시하는 명문 정파 출신의 무인들에게는 치욕이나 다름없는 말이었지만 진무경에겐 달랐다.

“당나귀든 노새든 상관없다. 체면이 밥 먹여 주나?”

“뭐?”

“목숨값에 비하면 싸게 먹힌 거지. 그리고…….”

시종일관 덤덤한 얼굴이던 그가 피식 웃었다.

“왜 웃지?”

“그냥, 절정 고수한테 돌팔매질하는 놈도 있는데 나려타곤이 대수일까 싶어서.”

의중을 알 수 없는 실없는 농담에 풍양은 자신도 모르게 되물었다.

“절정 고수한테 돌팔매질? 제정신인가?”

“처음 그 얘기를 들었을 때는 나도 비슷한 생각이었지. 그런데 곰곰이 생각해 보니 충분히 그러고도 남을 놈이라.”

“어떤 미친놈인지 얼굴 한번 보고 싶군.”

“금방 볼 수 있을 거다.”

“그게 무슨 말이지?”

풍양이 가벼운 의문을 느낀 그때였다.

쐐애애액!

등 뒤에서 느껴지는 날카로운 기세.

돌아선 그의 붉은 눈동자에 잘생긴 청년의 얼굴이 비쳤다.

‘산서잠룡.’

느리게 흐르는 시간 속에서 진태경이 씩 웃었다. 그가 쥔 철창은 이미 풍양의 가슴을 향해 쇄도하고 있었다.

콰아아아아!

일섬.

창날에서 뿜어져 나온 와류가 풍양을 집어삼켰다.



* * *



몸 상태는 완벽했다. 조무래기들을 처리하는 과정에서 레벨 업을 한 덕분에 피로와 체력이 완전히 회복되었기 때문이다.

타이밍도 괜찮았다. 풍양의 넓고 무방비한 등이 꼭 창으로 쑤셔 달라고 유혹하는 것 같았다.

이 그림을 장식할 마지막 화룡점정(畵龍點睛)으로 택한 것이 일섬이다. 지금까지 이거 맞고 멀쩡한 놈을 못 봤으니까.

그런데…….

“사람을 보고 덤볐어야지.”

짐승의 울음처럼 낮은 목소리. 풍양은 자신의 눈처럼 붉은 기(氣)의 장막에 휩싸여 있었다. 일섬이 뿜어내는 와류를 말끔히 막아 낸 그것은 살아 있는 갑옷처럼 꿈틀거렸다.

‘이런 걸 무협 소설에서 뭐라고 하더라.’

아, 그래. 기억났다. 나는 간신히 입술을 뗐다.

“호신강기(護身罡氣)?”

“개 눈깔은 아니군.”

“아니, 시바…….”

검기, 검강으로도 부족해서 이제는 호신강기야?

눈앞이 캄캄해져 멍하니 있는 나를 본 풍양이 입꼬리를 말아 올렸다.

“후회해도 늦었다.”

쉭!

곡도에서 솟구친 도기 한 가닥이 머리칼을 뭉텅 잘라 낸다. 바로 허리를 숙여서 망정이지, 아주 조금이라도 늦었다면 잘리는 건 머리였을 것이다.

‘미친.’

튀어나오려는 욕설을 삼키며 몸을 날리기 무섭게, 사나운 도격이 내가 있던 자리를 난도질했다.

쉬쉬쉬쉭!

문제는 그 도기 하나하나가 강력하기 짝이 없다는 사실이다. 얼어붙은 지면이 순두부처럼 쪼개지는 광경에 등골이 서늘해졌다.

‘이거, 까딱했다가는 진짜 골로 가겠는데.’

A급 마법 방어구를 차도 모자랄 판국에 천 쪼가리 하나 걸치고 싸우려니 살얼음판이 따로 없다.

무엇보다…….

‘저 자식은 지치지도 않나.’

호신강기를 유지하는 것만으로도 막대한 공력이 소모되고 있을 게 분명한데, 지금의 그는 공력이 마르지 않는 샘 같았다.

“형제라더니, 쥐새끼처럼 도망치는 모양새가 아주 똑 닮았구나.”

풍양이 비웃음을 흘린 그 순간이었다.

“별로 듣기 좋은 말은 아닌데.”

등 뒤에서 홀연히 나타난 진무경이 검을 흩뿌렸다. 쭉 뻗어 나간 푸른 섬광이 놈의 목을 노렸다.

쩡!

하지만 무엇이든지 베어 낼 것 같던 진무경의 검기도 호신강기를 뚫을 수는 없었다. 풍양이 여유로운 얼굴로 검기가 후려친 목을 쓰다듬었다.

“뻐근하군. 끝인가?”

“그럴 리가.”

쐐애애애액!

진무경이 거침없이 짓쳐 들어가자 동시에 풍양의 손에 들린 곡도가 움직였다. 공기의 흐름이 바뀌었다고 느낄 정도로 강대한 기세.

이건 내가 끼어들 수 없는 싸움이다.

쉭!

마침내 진무경의 푸른 검기와 풍양의 붉은 도기가 맞닿은 순간, 어마어마한 기파와 함께 귀가 먹먹해질 만큼 커다란 굉음이 터져 나왔다.

콰아아아아!

두 다리를 딛고 서 있던 이들 중 대부분이 중심을 잃고 휘청거렸다.

하지만 나는 눈을 부릅뜨고 이 엄청난 격돌의 결과를 지켜보았다.

‘누구냐.’

격돌의 충격으로 흩날리는 흙먼지 사이, 서로를 마주 보고 있는 두 사람이 보였다.

손잡이만 남은 도검과 굳게 다문 입술. 짧은 침묵을 먼저 깨트린 것은 풍양이었다.

바닥에 무릎을 꿇은 놈은 검붉은 핏물을 토해 냈다.

“큭, 쿠에에엑!”

장내에 작은 환호가 울려 퍼졌다. 당당히 서 있는 진무경과 무릎을 꿇은 풍양. 이 치열한 전투의 승패가 갈린 순간이다.

‘이겼어.’

얼마나 치열한 공방전이 있었는지 모두 보진 못했지만, 그 과정에서 풍양이 먼저 내상을 입은 것이 틀림없다.

그 증거로 놈의 가슴팍에는 지금까지 볼 수 없었던 선명한 장인(掌印)이 찍혀 있었다. 아마 저것이 결정타였을 것이다.

“쿨럭, 쿨럭.”

풍양이 피에 젖은 입가를 닦으며 비틀비틀 일어났다.

“격산타우(隔山打牛)라. 그렇다고 해도 호신강기가 이렇게 허무하게 깨질 줄은 몰랐는데…… 내 깨달음이 부족했던 건가?”

진무경의 묵묵부답에 놈이 혀를 찼다.

“빌어먹을, 잠력단을 쓰고도 이 지경이라니. 당분간은 심산유곡에 틀어박혀 무공이나 수련해야겠군.”

심산유곡? 수련?

나는 진심으로 궁금해져서 물었다.

“어딜 간다고?”

“기다리면 곧 알게 될 것이다. 너희 형제도 데려갈 생각이니까.”

이거 되게 당황스럽네.

집들이 초대니까 티슈라도 한 박스 사 가야 되나?

“어, 우리를?”

“그래, 네가 알고 있는 태원진가의 무공 구결이 필요하거든. 적혈심법의 난폭한 진기 운용을 보완하는 데 큰 도움이 되겠지.”

거기까지 듣고 나니 아까부터 혀끝에 맴돌던 말이 저절로 튀어나왔다.

“혹시 미친놈이세요?”

확인해 보진 않았지만 아마 다들 나와 같은 표정일 거다.

이미 승패가 명확히 갈린 마당에, 뭐?

“심산유곡에서 수련은 개뿔, 북망산 효도 관광 보내 줄 테니까 거기서 수련하시든가.”

“북망산? 네가 나를?”

“꼭 내가 아니더라도 댁을 북망산으로 보내 줄 사람들은 많지.”

어이없다는 듯 웃는 풍양에게 등 뒤를 턱짓해 보였다.

어느새 항산검문의 무인들이 병장기를 빼 들고 슬금슬금 다가오는 중이다.

그중 유난히 원독에 찬 눈빛을 보내는 미녀가 항산검문의 신임 문주 이소월이겠지.

‘이 인간도 편히 죽긴 글렀군.’

이제 지난 악행의 업보를 치를 시간이다. 나는 풍양을 향해 창을 까딱거렸다.

“이래도 자꾸 헛소리할래?”

잠시 우리를 물끄러미 바라보던 놈이 입을 열었다.

“글쎄, 큰 착각을 하고 있는 것 같은데.”

이어지는 목소리에는 숨길 수 없는 웃음기가 묻어 나왔다.

“너희들 중에 나를 쓰러트릴 수 있는 자가 있을까?”

“그게 무슨 개소리…….”

“믿기 힘들다면 내 앞에 있는 진천검에게 물어보는 게 빠르겠지. 자, 내 말에 대해 어떻게 생각하나?”

풍양의 물음에도 진무경은 대답하지 않았고, 나는 그제야 깨달았다.

아까부터 왜 그가 말이 없었는지. 왜 망부석처럼 그 자리에 서 있기만 했는지.

툭.

풍양의 손이 진무경의 가슴에 닿았다. 언제부터였을까, 이미 의식을 잃은 몸뚱어리가 힘없이 허물어진다.

그제야 보이는 그의 상반신에는 다섯 개의 비수가 나란히 꽂혀 있었다.

털썩.

침묵에 휩싸인 좌중을 쓸어 본 붉은 눈동자가 반달처럼 휘었다.

“자, 이제 마무리를 지어 볼까.”



* * *



‘마무리’는 빠르게 시작됐다.

느긋한 발걸음으로 우리를 향해 다가오던 그의 소매에서 튀어나온 십여 개의 비수가 시작이었다.

쉭! 푸푸푸푹!

제아무리 가까운 거리였다지만 진무경도 피하지 못한 비도술이다. 풍양이 던지는 비수는 정확히 표적을 꿰뚫었고, 어김없이 비명이 터져 나왔다.

“큭.”

“커헉!”

이미 피로가 극에 달한 데다 개개인의 무력도 높지 않은 항산검문의 무인들은 쉬운 사냥감이었다.

내가 비로소 풍양을 가로막았을 때는 이미 십여 명이 목숨을 잃은 후였다.

“멈춰.”

놈은 고개를 가로저었다.

“아니지, 그게 아니야. 명령은 강자에게 주어진 권리거든.”

“……넌 내가 죽인다.”

“진천검이라면 모를까, 너 같은 햇병아리가 감히?”

풍양의 비웃음에 나는 입을 다물었다. 틀린 말은 아니다. 놈을 막아선 것은 용기와 만용이 반쯤 뒤섞인 결정이었다.

‘하지만 어떻게 놈을 쓰러트리지?’

머릿속이 새하얗게 타들어 가는 것 같다. 복잡한 생각 속에 떠오르는 두 사람의 얼굴이 있었다.

그중 첫 번째는 대장로다. 지금까지 만난 무인 중 가장 고강하고 절망적이었던 상대. 그러나 그때에는 진위경과 태원진가 무인들의 도움이 있었다.

‘지금은?’

없다. 아무도 없다. 잠력단을 복용한 풍양은 대장로에 비견되거나 그 이상의 고수일 텐데, 놈을 상대할 사람은, 나뿐이다.

그러자 자연스럽게 두 번째 인물이 생각났다.

‘일문일살 조필.’

어쩌면 조필이야말로 나로 하여금 진짜 위기를 겪게 한 인물일지도 모른다. 무림에서 얻은 수하를 처음으로 잃었고, 죽기 직전까지 갔으니까. 그러고 나서야 놈을 쓰러트릴 수 있었다.

하지만 지금의 풍양은 조필과는 격이 다른 존재다.

‘이 개 같은 잠력단…….’

생각할수록 욕만 튀어나온다. 어떤 새끼가 만들었는지 면상 한번 보고 싶을 정도다.

“주제 파악이 끝났으면 조용히 찌그러져 있어라.”

잠력단을 믿고 천하제일 고수 행세를 하는 풍양을 보니 속이 뒤틀린다. 차라리 조필 정도만 됐었어도 어떻게 해 보는 건데…….

‘……어라?’

문득 잊고 있던 사실 하나가 뇌리를 스쳤다.

조필, 놈이 갖고 있던 물건 중에 살벌한 게 하나 있었지 아마?

‘열화신단.’

복용 시 반 갑자의 공력을 얻을 수 있는 희대의 영단(靈丹)인 동시에 까딱하면 영단이 품은 화기(火氣)에 죽을 수도 있는 양날의 검.

‘열화신단, 열화신단이라…….’

다음 순간.

멍하니 생각에 잠겨 있던 나는 불쑥 입을 열었다.

“야.”

어느새 나를 지나쳐 간 풍양이 멈칫하더니 돌아섰다.

“야? 지금 나한테 한 말이냐?”

“그래, 이 약쟁이 새끼야.”

“허, 이 핏덩이가 지금 뭐라 지껄이는…….”

“너만 약 처먹으니까 좋았냐?”

“……뭐?”

나는 황당함과 분노가 점철된 놈의 얼굴을 향해 또박또박 내뱉었다.

“혼자 약 처먹으니까 좋았냐고.”

이에는 이. 도핑에는 도핑.

이제는 나도 약 빨고 싸운다. 이 자식아.
```

## Current accepted English baseline

```markdown
# Chapter 117

Jin Mukyung had learned countless martial arts over the years. Among them were everything from Peak-level arts that had once defined an era to Third Rate martial arts easily found even on a street stall in some backwater village.

But at this very moment, he realized something.

*It’s strong. Stronger than any martial art I’ve learned until now.*

Fwoooosh.

A curved saber descended with the force of a single slash cleaving something in two.

It wasn’t a Supreme Peak art like the Nangong Family’s Emperor Sword Form or Huashan’s Plum Blossom Sword Technique. This was the first move of the Three Calamities Sword Technique, Mount Tai Presses Down on the Crown—the move even a Third Rate street thug would know.

*Pressing down Mount Tai. I think I know what that feels like.*

The red saber qi rippling over the blade seemed capable of doing more than merely pressing down Mount Tai. It looked like it could split the mountain apart.

*I can’t block it.*

In the briefest instant, Jin Mukyung threw himself aside without hesitation.

Shraaaaak!

The saber qi grazed Jin Mukyung’s clothes by a hair before striking the ground. The sight of the earth splitting wide open without a single boom or tremor sent a shiver through him.

“You dodged that?”

But Pung Yang was dissatisfied with the result.

That had been an all-out attack. Even after drawing out 120 percent of the Temporary Strength Pill’s effects, he hadn’t managed to leave so much as a small wound on Jin Mukyung.

*The Tiger of Mount Heng could barely parry that.*

Even Cheol Mubaek, a fully mature Peak master, had suffered internal injuries and been forced to retreat in exchange for blocking it. So how had a brat not even thirty years old managed this?

“So you do live up to the name Heaven Shaking Sword?”

Jin Mukyung adjusted his stance and replied flatly.

“This much should be dodged.”

“It’s not as though you couldn’t block it, is it?”

A sneer appeared at the corner of Pung Yang’s mouth.

“Of course, a young master of the mighty Jin Family of Taiyuan would have been desperate enough to flee by rolling across the ground like a lazy donkey.”[^1]

Narye tagon. It was a phrase comparing someone to a lazy donkey rolling on the ground. To martial artists from prestigious orthodox factions who valued their dignity, it was practically the ultimate humiliation.

But not to Jin Mukyung.

“Donkey or mule, I don’t care. Does dignity put food on the table?”

“What?”

“Compared to the price of my life, it was cheap. Besides…”

The face that had remained impassive the entire time cracked into a quiet laugh.

“Why are you laughing?”

“Just thinking that if there are people who pelt Peak masters with rocks, rolling across the ground isn’t such a big deal.”

Pung Yang involuntarily asked in response to the nonsensical joke, unable to understand what he meant.

“Throwing rocks at a Peak master? Are they insane?”

“When I first heard about it, I thought the same thing. But after thinking it over, I realized he was exactly the kind of bastard who would do something like that.”

“I’d like to see the face of this lunatic.”

“You’ll see him soon.”

“What does that mean?”

That was when Pung Yang felt a faint sense of puzzlement.

Shiiiiing!

A sharp aura came from behind him.

He turned around, and the face of a handsome young man was reflected in his red eyes.

*The Sleeping Dragon of Shanxi.*

Within the slow flow of time, Jin Taekyung grinned. The iron spear in his hands was already hurtling toward Pung Yang’s chest.

KABOOM!

One Annihilation.

A vortex erupted from the spearhead and swallowed Pung Yang whole.

* * *

My condition was perfect. Leveling up while dealing with the minions had completely restored my fatigue and Stamina.

The timing was pretty good, too. Pung Yang’s broad, defenseless back looked like it was begging to be stabbed with a spear.

As the finishing touch to this beautiful picture, I chose One Annihilation. I hadn’t seen anyone remain fine after taking this attack.

But then…

“You should’ve picked your opponent more carefully before charging in.”

A low voice like the growl of a beast.

Pung Yang was surrounded by a curtain of qi as red as his eyes. It had completely blocked the vortex unleashed by One Annihilation, and now writhed like living armor.

*What did wuxia novels call something like this again?*

Oh, right. I remembered. I barely managed to move my lips.

“Body-Protecting Qi?”

“At least you’re not blind.”

“No, for fuck’s sake…”

Sword Energy and Sword Force weren’t enough, and now he had Body-Protecting Qi too?

As I stood there dumbfounded, the sight before my eyes going dark, Pung Yang curled up the corner of his mouth.

“It’s too late for regret.”

Whoosh!

A strand of saber qi shot up from his curved saber and sliced off a clump of my hair. I had bent at the waist just in time. If I had been even slightly slower, it would have been my head that was cut off.

*Fuck.*

I swallowed the curse trying to burst out and leaped away. No sooner had I done so than savage saber strikes shredded the place where I had been standing.

Shh-shh-shh-shhk!

The problem was that every strand of saber qi was unbelievably powerful. Seeing the frozen ground split apart like soft tofu sent a chill down my spine.

*If I make one wrong move, I’m really going to die.*

Even an A-rank magic armor wouldn’t have been enough here, yet I was fighting while wearing nothing but a scrap of cloth. It was like walking across a sheet of thin ice.

More than anything else…

*Doesn’t that bastard ever get tired?*

Maintaining Body-Protecting Qi alone had to consume a massive amount of internal energy, but Pung Yang seemed like a spring that would never run dry.

“I heard you two were brothers, but the way you run away like rats is exactly the same.”

That was when a voice came from behind him.

“It’s not exactly a pleasant thing to hear.”

Jin Mukyung appeared out of nowhere and scattered a flurry of sword strikes. A long blue flash shot toward Pung Yang’s neck.

Clang!

But even Jin Mukyung’s Sword Energy, which seemed capable of cutting through anything, couldn’t pierce the Body-Protecting Qi. Pung Yang leisurely rubbed the neck struck by the Sword Energy.

“It’s a little stiff. Is that all?”

“Of course not.”

Shiiiiing!

As Jin Mukyung charged in without hesitation, the curved saber in Pung Yang’s hand moved at the same time. The aura was so powerful that I could feel the flow of the air change.

This wasn’t a fight I could join.

Whoosh!

At last, the moment Jin Mukyung’s blue Sword Energy met Pung Yang’s red saber qi, a tremendous wave of force erupted along with a boom loud enough to make my ears ring.

KABOOM!

Most of the people standing firmly on both feet lost their balance and staggered.

But I widened my eyes and watched the result of this incredible clash.

*Which one?*

Through the dust swirling from the impact, I saw two people facing each other.

A sword and saber reduced to nothing but their hilts. Tightly pressed lips.

Pung Yang was the first to break the brief silence.

The man kneeling on the ground spat out dark red blood.

“Urgh—bleeeargh!”

A small cheer rose through the battlefield. Jin Mukyung stood proudly while Pung Yang knelt on the ground. The winner of this fierce battle had been decided.

*We won.*

I hadn’t been able to see the entire exchange, but there was no doubt that Pung Yang had suffered internal injuries first.

The proof was the distinct palm print stamped across his chest—something that hadn’t been there before. That must have been the decisive blow.

“Cough, cough.”

Pung Yang wiped the blood from the corner of his mouth and staggered to his feet.

“Striking the Ox Across the Mountain.[^2] Even so, I never expected my Body-Protecting Qi to break so easily… Was my enlightenment lacking?”

When Jin Mukyung gave him no answer, Pung Yang clicked his tongue.

“Damn it. Even after using the Temporary Strength Pill, I’ve ended up like this. I suppose I should hole up in some remote mountain valley and train my martial arts for a while.”

“A remote mountain valley? Training?”

I was genuinely curious.

“Where are you going?”

“Wait, and you’ll find out soon enough. I plan to take you brothers with me, too.”

This was pretty awkward.

Since we’d been invited to a housewarming, should I at least bring a box of tissues?

“Uh, us?”

“Yes. I need the martial arts formulas you know from the Jin Family of Taiyuan. They should be a great help in supplementing the violent qi circulation of the Crimson Blood Cultivation Technique.”

After hearing that much, the words that had been lingering on the tip of my tongue came out on their own.

“Are you, by any chance, a lunatic?”

I hadn’t checked, but everyone probably wore the same expression I did.

The battle had already clearly decided its winner, and yet—what?

“Forget your remote mountain valley training. I’ll send you on a filial-piety tour of Mount Beimang. You can train there.”[^3]

“Mount Beimang? You think you can send me there?”

“Even if it isn’t me personally, there are plenty of people behind you who can send you to Mount Beimang.”

I jerked my chin toward the people behind him.

The martial artists of the Mount Heng Sword Sect were already approaching slowly, weapons drawn.

The beautiful woman among them, glaring at him with especially venomous hatred, had to be the Mount Heng Sword Sect’s new Sect Leader, Lee Seowol.

*This man isn’t going to get an easy death.*

It was time for him to pay for the karma of his past misdeeds. I flicked my spear toward Pung Yang.

“Are you still going to keep spouting nonsense?”

The bastard stared at us for a moment before opening his mouth.

“Perhaps you’re under a serious misconception.”

The laugh in his voice was impossible to hide.

“Is there anyone among you capable of defeating me?”

“What the fuck does that even—”

“If you find that hard to believe, it would be faster to ask the Heaven Shaking Sword standing before me. Well, what do you think of what I’ve said?”

Jin Mukyung didn’t answer Pung Yang’s question, and only then did I realize it.

Why he hadn’t said a word for some time. Why he had done nothing but stand in place like a stone statue.

Tap.

Pung Yang’s hand touched Jin Mukyung’s chest. At what point had it happened? His body had already lost consciousness, and now it crumpled limply.

Only then did I see the five throwing knives embedded in his upper body in a neat row.

Thud.

The red eyes sweeping across the silent crowd curved like crescent moons.

“Well, shall we finish things up?”

* * *

The “finishing” began quickly.

It started with the more than ten throwing knives that shot from Pung Yang’s sleeve as he approached us at an easy pace.

Whoosh! Thunk-thunk-thunk!

It might have been a close-range attack, but it was a throwing-knife technique that even Jin Mukyung hadn’t been able to evade. Pung Yang’s knives pierced their targets with perfect accuracy, and screams rang out without fail.

“Urgh.”

“Guhk!”

The martial artists of the Mount Heng Sword Sect were already at the limit of their endurance, and their individual martial prowess wasn’t particularly high, making them easy prey.

By the time I finally stepped in front of Pung Yang, more than ten of them had already lost their lives.

“Stop.”

He shook his head.

“No, that’s not how it works. An order is a right reserved for the strong.”

“…I’ll kill you.”

“I could see it if you were the Heaven Shaking Sword, but a wet-behind-the-ears fledgling like you dares?”

I closed my mouth at Pung Yang’s sneer. He wasn’t wrong. My decision to block him had been half courage and half foolhardiness.

*But how do I take him down?*

My mind felt like it was burning itself blank. Amid all the tangled thoughts, two faces surfaced.

The first was the Head Elder. He had been the most powerful and despair-inducing opponent I had ever faced. But back then, I’d had Jin Wikyung and the martial artists of the Jin Family to help me.

*What about now?*

No one. I had no one.

After taking the Temporary Strength Pill, Pung Yang had to be a master comparable to, or even stronger than, the Head Elder. And the only person left to face him was me.

That naturally brought the second person to mind.

*Jopil, One Question, One Kill.*

Perhaps Jopil was the person who had forced me to face a genuine crisis. For the first time, I’d lost one of the subordinates I’d gained in the Murim, and I’d nearly died. Only after that had I managed to defeat the bastard.

But the Pung Yang standing before me was on an entirely different level from Jopil.

*This goddamn Temporary Strength Pill…*

The more I thought about it, the more curses came out. I wanted to see the face of whatever son of a bitch had made it.

“Once you’ve learned your place, curl up quietly.”

Watching Pung Yang act like the greatest master under heaven simply because he trusted that pill twisted my gut. If he’d only been around Jopil’s level, I might have found a way to deal with him…

*…Wait.*

A forgotten fact suddenly flashed through my mind.

There had been something nasty among the things Jopil possessed. What was it again?

*The Blazing Flame Divine Pill.*[^4]

A peerless divine elixir that granted half a jiazi of internal energy when consumed—but was also a double-edged sword that could kill its user through the fire qi contained within it.[^5]

*The Blazing Flame Divine Pill. The Blazing Flame Divine Pill…*

The next moment, I abruptly opened my mouth.

“Hey.”

Pung Yang, who had already passed me, stopped and turned around.

“Hey? Were you talking to me?”

“Yeah, you pill-popping bastard.”

“Hah. What did this little brat just say…?”

“Did you enjoy being the only one popping pills?”

“…What?”

I looked straight at his face, mottled with bewilderment and fury, and enunciated each word.

“I asked if you enjoyed taking pills all by yourself.”

An eye for an eye. Doping for doping.

Now I was going to pop a pill and fight, too.

You bastard.

[^1]: *Narye tagon* literally compares someone to a lazy donkey rolling on the ground. For martial artists from prestigious orthodox factions, it implies humiliatingly abandoning dignity to survive.

[^2]: A martial-arts term describing force that passes through one object to strike another behind it.

[^3]: Mount Beimang is traditionally associated with burial grounds and the dead; sending someone there is a euphemism for killing them.

[^4]: The name literally combines “blazing flame” with “divine pill,” emphasizing the elixir’s dangerous fire qi.

[^5]: A *jiazi* is a sixty-year cycle; half a jiazi is thirty years.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 117`.

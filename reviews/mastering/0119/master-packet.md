# Master Edit Task — Chapter 119

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

| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 월화     | **Wolhwa**         |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 사형     | **Senior Brother**                           |
| 사숙     | **Martial Uncle**                            |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 아이템              | **Item**                       |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 귀가      | **your family**                                                 |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 진위경 | 이소월 | host_to_new_sect_leader | Young Lady | formal-polite | Jin Wikyung addresses Lee Seowol as 소저 before accepting her oath. |
| 이소월 | 진위경 | new_sect_leader_to_lesser_family_head | Lesser Family Head | formal-deferential | Lee Seowol refers to Jin Wikyung as 소가주님 when describing his summons. |
| 철무백 | 진위경 | sect_elder_to_lesser_family_head | Lesser Family Head | formal-deferential | Cheol Mubaek formally greets Jin Wikyung as the Lesser Family Head of the Jin Family of Taiyuan. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |
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

#### Chapter 117 tail (verified mastered)

…
him. The martial artists of the Mount Heng Sword Sect were already creeping closer with their weapons drawn. The beautiful woman among them, glaring at him with especially venomous hatred, had to be the Mount Heng Sword Sect’s new Sect Leader, Lee Seowol. *This man isn’t going to die peacefully.* It was time for him to pay for the karma of his past misdeeds. I flicked my spear toward Pung Yang. “Still going to keep spouting nonsense?” The bastard stared at us for a moment before speaking. “I think you’re laboring under a serious misconception.” The laugh in his voice was impossible to hide. “Is there anyone among you capable of defeating me?” “What the fuck does that even—” “If you find that hard to believe, it would be faster to ask the Heaven Shaking Sword standing before me. Well? What do you think?” Jin Mukyung didn’t answer Pung Yang’s question. Only then did I realize why he hadn’t said a word for some time. Why he had stood there like a stone statue without moving. Tap. Pung Yang’s hand touched Jin Mukyung’s chest. At what point had it happened? His unconscious body crumpled limply. Only then did I see the five throwing knives embedded in a neat row across his upper body. Thud. Pung Yang’s red eyes swept across the silent crowd and curved into crescent moons. “Well, shall we finish things up?” * * * The “finishing” began quickly. It started with the more than ten throwing knives that shot from Pung Yang’s sleeve as he approached us at an easy pace. Whoosh! Thunk-thunk-thunk! It might have been a close-range attack, but it was a throwing-knife technique that even Jin Mukyung hadn’t been able to evade. Pung Yang’s knives pierced their targets with perfect accuracy, and screams rang out without fail. “Urgh.” “Guhk!” The martial artists of the Mount Heng Sword Sect were already at the limits of their endurance, and none of them were particularly powerful. They were easy prey. By the time I finally stepped in front of Pung Yang, more than ten of them had already lost their lives. “Stop.” He shook his head. “No. That’s not how it works. Giving orders is a right reserved for the strong.” “…I’ll kill you.” “If you were the Heaven Shaking Sword, perhaps. But a wet-behind-the-ears fledgling like you dares?” I fell silent at Pung Yang’s sneer. He wasn’t wrong. My decision to block his path had been equal parts courage and recklessness. *But how do I take him down?* My mind felt like it was burning itself blank. Amid all the tangled thoughts, two faces surfaced. The first was the Head Elder. He had been the most powerful and despair-inducing opponent I had ever faced. But back then, I’d had Jin Wikyung and the martial artists of the Jin Family to help me. *What about now?* No one. There was no one. After taking the Temporary Strength Pill, Pung Yang had to be a master comparable to, or even stronger than, the Head Elder. And the only person left to face him was me. That naturally brought the second person to mind. *Jopil, One Question, One Kill.* Perhaps Jopil was the person who had forced me to face a genuine crisis. For the first time, I’d lost one of the subordinates I’d gained in the Murim, and I’d nearly died. Only after that had I managed to defeat the bastard. But the Pung Yang standing before me was on an entirely different level from Jopil. *This goddamn Temporary Strength Pill…* The more I thought about it, the more curses came out. I wanted to see the face of whatever son of a bitch had made it. “Once you’ve learned your place, curl up quietly.” Watching Pung Yang act like the greatest master under heaven simply because he trusted that pill twisted my gut. If he’d only been around Jopil’s level, I might have found a way to deal with him… *…Wait.* A fact I’d forgotten suddenly flashed through my mind. There had been something nasty among Jopil’s possessions. What was it again? *The Blazing Flame Divine Pill.* A peerless divine elixir that granted half a jiazi of internal energy when consumed—but also a double-edged sword that could kill its user with the fire qi it contained.[^4] *The Blazing Flame Divine Pill. The Blazing Flame Divine Pill…* The next moment, I abruptly spoke. “Hey.” Pung Yang, who had already walked past me, stopped and turned around. “Hey? Were you talking to me?” “Yeah, you pill-popping bastard.” “Hah. What did this little brat just say…?” “Did you enjoy being the only one popping pills?” “…What?” I looked straight at his face, mottled with bewilderment and fury, and enunciated each word. “I asked if you enjoyed taking pills all by yourself.” An eye for an eye. Doping for doping. Now I was going to pop a pill and fight, too. You bastard. [^1]: *Narye tagon* literally compares someone to a lazy donkey rolling on the ground. For martial artists from prestigious orthodox factions, it implies humiliatingly abandoning dignity to survive. [^2]: A martial-arts term describing force that passes through one object to strike another behind it. [^3]: Mount Beimang is traditionally associated with burial grounds and the dead; sending someone there is a euphemism for killing them. [^4]: A *jiazi* is a sixty-year cycle; half a jiazi is thirty years.

#### Chapter 118 tail (verified mastered)

…
a few years of training, he had already attained seventy percent mastery of the Crimson Blood Twelve Sabers. It was more than enough to kill a brat hopelessly beneath him in both age and martial arts. “Die!” *Shiiing!* The Crimson Blood Twelve Sabers was a domineering martial art. Red saber qi shot from the curved saber and slashed wildly in every direction. The fierce momentum split open the surface of the earth and burst the air apart. Yet the target it was meant to cut was no longer there. Jin Taekyung dodged the attack by exactly half a step and thrust his spear. *Shweeeeeek!* The spearhead drove toward Pung Yang’s throat. He hastily twisted his head aside to evade it, and a chill ran through his chest. *Fast.* Fast and accurate. Jin Taekyung had yet to reach the stage of injuring others with Sword Energy, the hallmark of a Peak master, but his movements had already caught up to Pung Yang’s. *Could this brat have taken the Temporary Strength Pill too? No. It’s completely different from mine.* Pung Yang had taken the Temporary Strength Pill several times before. One look at Jin Taekyung’s body, flushed bright red with heat, was enough to tell him that the pill the brat had swallowed wasn’t a Temporary Strength Pill. *Then what did he—wait!* Pung Yang couldn’t finish the thought. Jin Taekyung had finally seized the initiative and begun unleashing the Jin Family’s Spear Technique in earnest. *Shh-shh-shh-shh-shhk!* Dozens of spear shadows poured down like a rain shower. The sight alone was suffocating. No, it wasn’t just an illusion. It really was suffocating. A bead of sweat rolled down Pung Yang’s forehead. *This is…* Scorching Yang Qi. And not just any Scorching Yang Qi. It was powerful enough to affect even Pung Yang, a Peak master. The Tiger of Mount Heng, Cheol Mubaek, had also possessed Scorching Yang Qi, but it couldn’t compare to what Jin Taekyung was emitting now. *He took a divine elixir—a Scorching Yang-type divine elixir!* *Whooooom!* Recognizing it changed nothing. The heat was dizzying, and the attacks were sharp. Pung Yang bit down hard on his lip as he retreated again and again, barely evading the spearhead. *Against a brat this young!* He had lived his entire life fiercely. Now, even after taking the Temporary Strength Pill, he felt humiliated to be driven back by a young brat who had only just begun making a name for himself. That anger flowed straight into his curved saber. The saber qi rising over the blade blazed redder than ever. *Hiss!* The Jin Family’s Spear Technique and the Crimson Blood Twelve Sabers differed in both weapon and form, but they had one thing in common: both were domineering martial arts. In the blink of an eye, Jin Mukyung’s iron spear and Pung Yang’s curved saber finally parted after more than ten fierce exchanges. “Hmm.” Jin Taekyung was the first to retreat. Blood flowed from his torn palm, and the heavy, sturdy iron spear had been cut by the sharp saber qi until less than half of it remained. “You fool.” Pung Yang smiled triumphantly. For a martial artist, losing one’s weapon meant defeat. Even the Tiger of Mount Heng, Cheol Mubaek, who had built his reputation with nothing but his fists and feet, had knelt before Pung Yang. Jin Taekyung hadn’t even crossed the wall into the Peak realm. The moment he lost his weapon, he was as good as dead. “Did you think you could defeat me head-on?” Jin Taekyung wiped the blood from his palm and answered. “No. But I did learn some valuable information.” “…Valuable information?” “Yeah. I figured out your attack pattern.” “Pat—what?” “Your attack pattern is strong, strong, strong, strong, strong.” *What kind of bullshit is this?* Pung Yang understood that the brat was talking about his martial arts, but he had never heard of this “pattern-whatever” before. And what did he mean by strong, strong, strong, strong, strong? Pung Yang glared at Jin Taekyung with murder in his eyes. “I’ll sever the sinews and meridians in all four of your limbs as payment for that nonsense.” Jin Taekyung opened his mouth with a bored expression. “You really like cutting off and pulling out people’s limbs. Do you have a limb fetish?” “You little bastard…” “You old bastard…” Pung Yang drew a deep breath. He was a Peak master who had spent his entire life possessing a cool, rational mind. But he couldn’t stop his voice from breaking into pieces with anger. “You. Will. Die. By. My. Hand.” “I. Sometimes. Cut off. Limbs. Sometimes. I don’t like this version of myself.” He felt his patience snap. He could swear that he had never been this furious in nearly ten years. “Graaaargh!” Pung Yang charged like a madman, unleashing a strange cry that could have been either a scream or a roar. Without using any form or martial art, he brought the curved saber down over the crown of Jin Taekyung’s head with all his strength. “Die!” That was when Jin Taekyung’s calm expression was reflected in Pung Yang’s bloodshot eyes gleaming with killing intent. In an instant, his mind snapped clear as though someone had dumped cold water over him. *Something’s wrong.* Pung Yang drew up his internal energy with all his might. As his Body-Protecting Qi rose, a dagger flashed in Jin Taekyung’s previously empty hand. *Shnk!*

## Korean source

```text
＃119화



푹!

손끝을 타고 흐르는 찌릿한 전율. 지금까지 수천, 수만 번도 넘게 느낀 익숙한 감각이다.

‘들어갔구나.’

확신과 동시에 놈의 옆구리에 박아 넣은 비수를 비틀자 풍양의 입에서 비명이 터져 나왔다.

“크아아악!”

비수에 의한 고통도 있겠지만 지금의 일격으로 만만치 않은 내상(內傷)을 입었을 것이다. 미처 완성되지도 못하고 연기처럼 흩어지는 호신강기가 그 증거다.

‘아슬아슬했어.’

풍양의 본능은 보통이 아니었다. 정말 찰나의 순간, 호신강기가 완성되기 직전에 비수가 박히지 않았다면 오히려 내가 당했을 것이다.

“컥!”

풍양이 검은 핏물을 토하며 팔을 뻗었다. 순간 컴컴한 소매 안에서 빛이 번쩍 솟구친다.

쐐애애액!

나는 순간적으로 한 걸음 물러나며 고개를 젖혔다. 풍양의 소매에서 튀어나온 비수 한 자루가 아슬아슬하게 콧날을 스쳐 간다.

‘위험했다.’

물러서지 않았다면 콧날이 아니라 목젖에 박혔을 거다.

앞서 풍양이 비도술을 사용하는 것을 본 덕분에 피할 수 있었다. 나는 혀를 내밀어 콧날을 타고 흐르는 핏물을 날름 받아마셨다.

“고맙다. 안 그래도 목말랐는데.”

“이 쥐새끼 같은 놈이……!”

거리를 벌린 풍양이 이를 갈았다.

“처음부터 이걸 노린 거였나?”

“응. 아프지?”

“기다려라, 백배로 돌려줄 테니.”

“우리 사이에 뭘 또 그렇게까지. 안 갚아도 돼.”

“이이이익!”

놀리는 맛이 제법 쏠쏠하다. 저놈이 화병으로 죽어 주면 참 고맙겠는데 그럴 일은 없겠지.

‘좋은 기회였는데.’

도발로 풍양을 끌어들이는 데까지는 성공했지만 완전히 끝장내는 것은 실패했다. 열화신단을 복용했다지만 아직 나와 풍양의 격차는 컸다.

그리고 무엇보다.

‘슬슬 힘들어지네.’

전신이 불덩이처럼 뜨겁다. 처음부터 통제할 수 없었던 30년의 열양지기는 이제 제멋대로 날뛰는 중이다.

기존의 공력으로 억눌러도 될까 말까인데, 아예 고삐를 놓은 상태로 풍양과 접전을 벌였더니 점차 악화되어 가고 있었다.

‘젠장, 열화신단이 아니라 잠력단이었으면 좋았을 텐데.’

열화신단과 잠력단은 애당초 제조된 목적부터가 다르다.

잠재된 힘을 한계치까지 끌어 올리는 일시적 각성제라고 해야 되나? 비유하자면 한약과 각성제의 차이라고 할 수 있겠다.

‘저놈은 부작용도 없나. 더럽게 쌩쌩하네.’

내심 부러운 마음으로 풍양을 바라본 그때였다.

“쿨럭.”

어, 이것 봐라?

짧은 기침하는 풍양의 눈에, 순간 흰자위가 비쳤다.

시종일관 온통 핏빛처럼 붉었던 눈동자가 저렇게 변한 이유는 아무리 생각해 봐도 하나밖에 없다.

‘잠력단의 효력이 떨어지고 있다.’



* * *



풍양은 당황했다. 그는 자신의 몸에서 일어나는 이상 신호를 곧바로 알아차렸다.

‘벌써?’

잠력단의 효력은 한 시진 남짓. 한데 고작 반 시진이 지난 지금, 전신에서 용솟음치던 힘이 점차 사그라지고 있다.

느껴지지 않던 피로가 둔중하게 어깨를 짓누르고, 멀게 느껴지던 통증이 신경을 건드렸다.

“쿨럭.”

거기에 적지 않은 내상까지.

기침에 섞여 나온 검붉은 핏물에 풍양은 입술을 깨물었다.

‘힘을 너무 소진했어.’

잠력단은 가진 힘을 두 배, 혹은 그 이상으로 끌어 올리는 귀물이지만 그만큼의 대가가 따른다.

일시적으로 강대한 힘을 얻는 대신 신체 능력이 저하되고, 복용자의 신체가 받쳐 주지 않는다면 효능이 사라진다.

‘잠력단을 연이어 복용한 게 문제였다.’

항산호 철무백에 이어 태원진가의 어린놈들까지. 잠력단을 먹지 않았다면 진작 죽었을 테지만 그 대가를 알고 있는 풍양으로서는 후폭풍이 두려웠다.

‘지금 상태대로라면 잠력단의 효능은 길어 봤자 한 식경…….’

한 식경, 그 안에 승부를 봐야 한다.

마지막 남은 잠력단은 결코 쓰여선 안 된다. 연이어 세 개를 복용한다면 목숨이 위험할 수도 있다.

“한 식경이라…….”

작게 중얼거린 풍양이 남아 있는 사냥감들을 노려봤다.

“그 정도면 충분하지.”

언뜻 드러난 흰자위가 다시 핏빛으로 채워졌다.



* * *



착각이었나?

풍양이 다시 고개를 들었을 때, 놈의 눈은 붉었고 전신에서는 감당 못 할 기파가 쏟아져 나왔다.

“단칼에 죽여 주마.”

나는 놈의 곡도를 주시하며 입을 열었다.

“무공 구결 필요하다면서?”

“네가 아니라도 상관없다. 내가 굳이 진무경을 살려 둔 이유가 뭐라고 생각하지?”

“사랑해서.”

“천지신명께 맹세컨대…… 네 혓바닥은 반드시 잘라 주마.”

풍양이 곡도를 치켜세운 다음 순간이었다.

쐐애애액! 탁!

강맹한 기세로 날아온 철시(鐵矢)를 붙잡은 풍양이 눈살을 찌푸렸다.

“죽고 싶은 놈들이 널렸군. 아니, 이번에는 년인가?”

화살의 주인이 천천히 걸어와 내 옆에 섰다. 솜털처럼 가벼운 발걸음과 내 어깨에 닿을까 말까 한 신장. 이 급박한 와중에도 순간 시선을 뺏길 만큼 아름다운 외모.

항산검문주 이소월이 내게 작은 목소리로 속삭였다.

“우리가 시간을 벌게요.”

‘우리’라는 건 이소월을 포함한 살아남은 항산검문의 무인들이었다. 고작 열 명. 엄청난 격전에서 최후까지 버틴 이들답게 하나같이 일류 고수들이지만 상대가 풍양이라면 결과는 불 보듯 뻔하다.

‘전멸.’

이들이 나선다고 한들 얼마나 시간을 벌 수 있을까? 오히려 내게는 방해가 될 공산이 컸다. 냉정하지만 그게 현실이다.

나는 고개를 가로저었다.

“그렇다고 달라지는 건 없을 겁니다.”

“함께 싸우자는 이야기가 아니에요.”

“그럼.”

“형님을 데리고 도망쳐요.”

풍양과 우리의 거리는 고작 십여 장(30m) 남짓. 아무리 작게 말해도 절정 고수인 놈이 못 들었을 리 없다.

“뭐, 도망을 쳐? 크하하하!”

터져 나오는 풍양의 폭소에도 이소월은 아랑곳하지 않고 말을 이었다.

“촌각에 불과하겠지만 시간을 벌어 드릴게요. 최대한 멀리 도망치세요.”

나는 성문 밖으로 시선을 던졌다. 여기서부터 문까지는 약 백 장(300m)의 거리. 얼마 떨어지지 않은 곳에는 월화와 혁무진, 그리고 우리를 태울 말이 있다.

‘시도해 볼 만한 일이야.’

지금도 열화신단에 의해 내상을 입고 있지만 어느 정도는 버틸 만하다. 젖 먹던 힘까지 쥐어짠다면 진무경을 업는다 해도 탈출 가능성이 있다.

하지만…….

‘이들은 죽는다.’

단언컨대, 단 한 명도 예외는 없다. 앞서 이소월이 말한 ‘우리’에는 문주인 자신도 포함되어 있으니 그녀도 죽음을 각오하고 나선 것이다.

‘어째서?’

항산검문과 태원진가는 악연이다. 비록 대장로의 술수에 놀아났다고 해도 서로가 서로를 죽이고, 각자 수많은 피를 흘렸다. 그런데 이소월은 나를 구하려 한다.

자신과 수하들의 목숨을 바쳐서까지.

“그런 얼굴로 볼 필요 없어요. 심사숙고 끝에 내린 결론이니까. 대신 부탁 하나만 해도 될까요?”

내가 물었다.

“그 부탁이 뭡니까?”

“우리를 대신해서 원수를 갚아 주는 것.”

이소월이 서늘한 눈빛으로 풍양을 응시했다.

“저놈을 죽여 주면 돼요. 누구보다 잔인하게.”

한 사람의 죽음을 위해 열 사람이 목숨을 버렸다.

말 한마디, 한마디에 이소월이 품은 원한이 느껴진다. 내가 할 말을 잃은 그때, 비웃음을 띠고 우리를 지켜보던 풍양이 입을 열었다.

“제법 맹랑한 생각을 했다만, 그럴 일은 없을 게다. 너희는 여기서 모두 뼈를 묻을 테니까.”

항산검문의 무인 중 하나가 외쳤다.

“닥쳐라, 이 악독한 놈!”

퍽-!

다음 순간, 무인이 고개가 넘어갔다. 그의 이마에는 풍양이 쥐고 있던 철시가 박혀 있었다.

“사형!”

뒤늦게 터진 비명을 들으며 풍양이 빙긋 웃었다.

“안 그래도 비수가 다 떨어진 참이었는데……. 고맙네, 문주.”

이소월이 입술을 깨물었다.

“가요, 어서!”

나는 크게 심호흡했다. 이미 어떻게 해야 할지는 모두 머릿속에 그려 놓았다.

진무경이 쓰러져 있는 곳까지는 불과 이십여 장(60m). 내상을 감수하고서라도 최대한 공력을 일으켜 업고 달리면 성문까지는 금방이다.

아마 그때쯤에는 풍양에게 따라잡힐지도 모르지만, 이들이 조금만 더 시간을 벌어 준다면 살 수 있다.

‘돌아갈 수 있어.’

진위경이 있는 태원진가로, 어머니와 하연이가 기다리는 집으로 돌아갈 수 있다. 지금 후일을 기약한다면 풍양은 비교도 안 될 만큼 강해져서 돌아올 자신도 있다.

‘그럼 된 거야.’

깊게 심호흡한 나는 이소월을 향해 돌아섰다.

“원수는 갚을 겁니다. 반드시.”

아주 잠깐, 그녀가 웃었다고 생각한 것은 착각일까?

그것은 너무 찰나였고, 다시 본 이소월의 얼굴에는 굳은 결의만이 남아 있었다.

“가세요. 어서.”

그 말이 신호탄이었다. 항산검문의 무인들이 악에 받친 고함과 함께 돌격했다. 그 선두에 이소월이 있었다.

‘그래, 가야지.’

나는 전신의 모든 공력을 끌어 올렸다. 열양지기가 남긴 내상으로 인해 날카로운 통증과 함께 코에서 검붉은 피가 흘렀지만 참았다. 잠깐, 아주 잠깐이면 된다.

‘인벤토리 오픈, 창 장착.’

서늘한 창대가 손아귀에 잡힌다.

그리고 한 번의 발 구름.

쿵.

나는 화살처럼, 아니 화살보다 빠른 속도로 쏘아졌다.

진무경이 아닌 풍양에게로. 놈의 활짝 웃는 얼굴이 보였다.

“그래, 이렇게 나와야지!”

“닥쳐, 이 개새끼야.”

“으하하하!”

풍양의 곡도는 그 어느 때보다 거대했다. 붉은 도기를 한껏 머금은 그것이 나를 향해 휘둘러졌다.

쏴아아악!

바람이 터져 나가고 공기마저 지워지는 듯했다.

나는 철창을 으스러져라 움켜쥐었다.

‘제발, 단 한 번만.’

15년의 공력을 모두 창으로 흘려보냈다. 어깨와 허리를 한껏 젖히고 내 모든 걸 쏘아 보낸다.

‘일섬.’

구구구궁-!

거대한 도기와 와류의 충돌.

하늘이 갈라지는 듯한 굉음이 세상을 가득 메웠다. 휘몰아치는 바람 사이로 똑똑히 보였다.

콰아아아!

붉은 도기 앞에서 산산이 흩어지는 백색 와류. 거대한 기의 결정체는 일섬을 완전히 분쇄했다. 풍양이 희열에 찬 얼굴로 속삭였다.

“여기까지다.”

다음 순간, 창을 타고 솟구친 풍양의 공력이 나를 후려쳤다.

쾅! 아득한 고통과 이명(耳鳴)이 파도처럼 밀려온다.

띠링.



- [내상]을 입었습니다! 상태가 매우 심각합니다!

- [열양지기]가 폭주 중입니다!

- [중상]을 입었습니다! 모든 능력치가 크게 하락합니다!



연이어 울리는 시스템 알림, 항산검문 무인들의 고함, 이소월의 비명, 그리고 풍양의 웃음까지.

‘끝이구나.’

의지와는 상관없이 다리에 힘이 풀린 찰나, 억센 손아귀가 내 목을 틀어쥐었다.

“컥. 커헉.”

“제법이었다. 촌각만 늦었더라면 네가 이겼을지도 모르지.”

풍양이 이를 드러내며 웃었다. 놈의 눈동자에서 붉은 기운이 서서히 사라지고 있었다.

젠장, 더럽게 아깝네.

소리 내서 말하고 싶었지만 핏물이 가득 찬 탓에 그조차도 쉽지 않았다.

“천지신명께 맹세했었지. 반드시 네 혓바닥을 뽑겠다고.”

그런 말을 했었나? 이젠 내가 누구인지도 가물가물하다.

풍양이 다른 한 손으로 내 입을 벌렸다. 핏물로 흠뻑 젖은 혀를 잡아당기는 거친 손가락이 느껴진다.

“흐어…….”

“그 주둥이를 나불거릴 때는 이렇게 될 줄 몰랐나. 응?”

“흐아, 흐하하아.”

“으하하! 뭐라 지껄이는 거냐? 마지막 유언이라도 남기게 해 주랴?”

풍양이 껄껄 웃으며 혓바닥을 놔 주자 비로소 말을 할 수 있게 되었다. 나는 핏물을 꿀꺽 삼키며 말했다.

“짜.”

“뭐?”

“더럽게 짜다고.”

“그게 무슨 개소리냐?”

무슨 소리긴.

네 손가락 맛을 보고 약간 정신이 돌아왔다는 소리지.

나는 혼미한 정신으로 중얼거렸다.

‘인벤토리 오픈, 아무거나 소환.’

띠링.



- [아무거나]라는 아이템을 찾을 수 없습니다. 인벤토리에 보관된 것 중 가장 오래된 아이템부터 소환합니다.

- [이름 없는 검]이 소환되었습니다.



이름 없는 검? 그게 뭐였더라.

‘뭐든 어때.’

나는 마지막 힘을 끌어올려 손에 든 검을, 호신강기가 서린 풍양의 가슴을 향해 찔러 넣었다. 그건 결말이 뻔한 발악이었다.

‘빌어먹을 호신강기.’

하지만 이걸로 됐다. 더 이상 후회는 없으니까.

고개가 스르륵 내려가던 그 순간이었다.

푹-!

띠링.



- [이름 없는 검]이 특정 조건을 만족합니다.

- [만년한철]이 [호신강기]를 파괴했습니다.



……응?
```

## Current accepted English baseline

```markdown
# Chapter 119

*Thud!*

A tingling tremor ran through my fingertips. It was a familiar sensation, one I had felt thousands, tens of thousands of times before.

*It went in.*

At the same time as that certainty struck me, I twisted the dagger buried in Pung Yang’s side. A scream burst from his mouth.

“Graaaargh!”

The dagger itself must have caused excruciating pain, but that blow had also inflicted a serious internal injury. The Body-Protecting Qi that had failed to fully form before scattering like smoke was proof enough.

*That was close.*

Pung Yang’s instincts were extraordinary. If the dagger hadn’t pierced him in that fleeting moment, just before his Body-Protecting Qi was completed, I would have been the one in trouble.

“Guh!”

Pung Yang spat out dark blood and reached out with one arm. In that instant, a flash of light burst from inside his pitch-black sleeve.

*Shweeeeeek!*

I instinctively took a step back and tilted my head. A dagger shot from Pung Yang’s sleeve and narrowly grazed the bridge of my nose.

*That was dangerous.*

If I hadn’t stepped back, it would have struck my throat instead of my nose.

I was only able to evade it because I had seen Pung Yang use throwing knives earlier. I stuck out my tongue and licked up the blood running down the bridge of my nose.

“Thanks. I was thirsty anyway.”

“You little rat bastard…!”

Pung Yang widened the distance between us and ground his teeth.

“Was this what you were aiming for from the beginning?”

“Yeah. Does it hurt?”

“Wait. I’ll pay you back a hundredfold.”

“There’s no need to go that far between friends. You don’t have to pay me back.”

“Grrrrrgh!”

Teasing him was surprisingly satisfying. It would be nice if he died of rage, but there was no chance of that happening.

*It was a good opportunity.*

I had succeeded in drawing Pung Yang in by taunting him, but I had failed to finish him off completely. Even after taking the Blazing Flame Divine Pill, the gap between Pung Yang and me was still enormous.

And more importantly—

*This is getting difficult.*

My entire body was hot as a furnace. The thirty years of Scorching Yang Qi that I hadn’t been able to control from the beginning was now running wild of its own accord.

It would have been touch and go even if I’d tried to suppress it with my existing internal energy, but I’d fought Pung Yang at close quarters with the reins completely off, and my condition was steadily worsening.

*Damn it. I wish this had been a Temporary Strength Pill instead of the Blazing Flame Divine Pill.*

The Blazing Flame Divine Pill and the Temporary Strength Pill had been created for entirely different purposes.

Was the Temporary Strength Pill a stimulant that temporarily awakened latent power and raised it to its limit? To put it simply, the difference was like that between traditional herbal medicine and a stimulant.

*Does that bastard not have any side effects? He’s annoyingly full of energy.*

I was looking at Pung Yang with a trace of envy when—

“Cough.”

Oh? What was this?

For an instant, the whites of Pung Yang’s eyes showed through during his short cough.

His eyes had been completely blood-red the entire time. No matter how I thought about it, there could only be one reason for this change.

*The Temporary Strength Pill is losing its effect.*

* * *

Pung Yang was flustered. He immediately recognized the abnormal signs appearing in his body.

*Already?*

The Temporary Strength Pill’s effect lasted a little over one shichen. Yet now, after barely half a shichen had passed, the power that had been surging through his entire body was gradually fading.

Fatigue he hadn’t felt before pressed heavily down on his shoulders, and pain that had seemed distant began to prick at his nerves.

“Cough.”

On top of that, he had suffered a considerable internal injury.

Pung Yang bit his lip as dark-red blood came out with his cough.

*I’ve expended too much strength.*

The Temporary Strength Pill was a wondrous object that could draw out twice, or even more than twice, the strength a person possessed—but it demanded an equal price.

In exchange for temporarily granting tremendous power, it weakened the body’s physical abilities. If the user’s body could not support it, the effect would disappear.

*Taking the Temporary Strength Pills one after another was the problem.*

First the Tiger of Mount Heng, Cheol Mubaek, and then the young brats from the Jin Family of Taiyuan. If he hadn’t taken the pills, he would have died long ago, but Pung Yang knew the price he would have to pay and feared the aftermath.

*At this rate, the Temporary Strength Pill’s effect will last only one meal’s time longer at most…*

He had to settle the battle within that time.

He must not use the last Temporary Strength Pill. Taking three in succession could put his life at risk.

“One meal’s time…”

Pung Yang muttered under his breath and glared at the remaining prey.

“That’s more than enough.”

The whites of his eyes disappeared again, filled once more with blood-red light.

* * *

Had I been mistaken?

When Pung Yang raised his head again, his eyes were red, and an overwhelming aura poured from his entire body.

“I’ll kill you with a single stroke.”

I watched his curved saber and opened my mouth.

“I thought you needed the martial arts formulas.”

“It doesn’t have to be you. Why do you think I went to the trouble of keeping Jin Mukyung alive?”

“Because you love him.”

“I swear by the gods of heaven and earth… I will cut out your tongue.”

The next moment, Pung Yang raised his curved saber.

*Shweeeeeek! Clang!*

Pung Yang caught an iron arrow flying toward him with tremendous force and frowned.

“There are plenty of bastards who want to die. Or is it a bitch this time?”

The owner of the arrow slowly walked over and stood beside me. Her footsteps were light as down, and her height barely reached my shoulder. Even in this desperate situation, her beauty was enough to steal my gaze for an instant.

The Sect Leader of the Mount Heng Sword Sect, Lee Seowol, whispered to me in a low voice.

“We’ll buy you some time.”

*We* meant the surviving martial artists of the Mount Heng Sword Sect, including Lee Seowol. There were only ten of them. As befitted those who had survived until the end of such a brutal battle, every one of them was a First Rate master, but against Pung Yang, the outcome was obvious.

*They’ll all be wiped out.*

How much time could they buy even if they stepped forward? They were more likely to get in my way. It was coldhearted, but that was reality.

I shook my head.

“That won’t change anything.”

“We’re not saying we’ll fight alongside you.”

“Then?”

“Take your brother and run.”

The distance between Pung Yang and us was only a little over ten zhang—about thirty meters. No matter how quietly she spoke, there was no way a Peak master like him hadn’t heard her.

“What, run? Hahahaha!”

Despite Pung Yang’s booming laughter, Lee Seowol continued speaking without flinching.

“It may only be for a fleeting moment, but we’ll buy you time. Run as far away as you can.”

I turned my gaze toward the fortress gate. It was about one hundred zhang—three hundred meters—from here. Wolhwa, Hyuk Mujin, and the horses waiting to carry us were not far beyond it.

*It’s worth trying.*

I was already suffering internal injuries from the Blazing Flame Divine Pill, but I could still endure them to some extent. If I squeezed out every last bit of strength I had, I might be able to escape even while carrying Jin Mukyung on my back.

But…

*They’ll die.*

Every last one of them. Not a single exception.

Lee Seowol herself was included in the *we* she had mentioned. She had stepped forward prepared to die as well.

*Why?*

The Mount Heng Sword Sect and the Jin Family of Taiyuan were bitter enemies. Even if they had been manipulated by the Head Elder’s schemes, they had killed one another, and both sides had shed a great deal of blood.

And yet Lee Seowol was trying to save me.

She was willing to sacrifice her own life—and the lives of her subordinates—to do it.

“You don’t need to look at us like that. I reached this conclusion after careful consideration. In return, may I ask you for one thing?”

I asked her,

“What is it?”

“Aveng​e us in our place.”

Lee Seowol stared at Pung Yang with icy eyes.

“Kill that man. As cruelly as possible.”

Ten people were throwing away their lives for one person’s death.

I could feel the hatred Lee Seowol held in every word she spoke. Just as I was rendered speechless, Pung Yang, who had been watching us with a mocking smile, opened his mouth.

“That’s a bold idea, but it won’t happen. You’ll all bury your bones here.”

One of the Mount Heng martial artists shouted.

“Shut up, you vicious bastard!”

*Thwack!*

The next moment, the martial artist’s head jerked back. The iron arrow Pung Yang had been holding was embedded in his forehead.

“Senior Brother!”

As the belated scream rang out, Pung Yang smiled.

“I was just about out of throwing knives, too… Thank you, Sect Leader.”

Lee Seowol bit her lip.

“Go! Hurry!”

I took a deep breath. I had already drawn out every step in my mind.

Jin Mukyung had fallen only about twenty zhang—sixty meters—from here. If I drew out as much internal energy as possible, ran while carrying him on my back, and endured the internal injuries, I could reach the fortress gate quickly.

Pung Yang would probably catch up to me by then, but if these people bought me just a little more time, I could survive.

*I can go back.*

I could return to the Jin Family of Taiyuan, where Jin Wikyung was, and to the home where my mother and Hayeon were waiting. If I lived to fight another day, I was confident I could return much stronger—strong enough to make Pung Yang seem insignificant by comparison.

*That’s enough.*

After taking another deep breath, I turned toward Lee Seowol.

“I’ll avenge you. I swear.”

For the briefest instant, did Lee Seowol smile?

It was so fleeting that I might have imagined it. When I looked again, only firm resolve remained on her face.

“Go. Hurry.”

Her words were the starting signal. The Mount Heng martial artists charged with furious shouts, Lee Seowol at the front.

*Yes. I have to go.*

I drew up every last bit of internal energy in my body. Sharp pain tore through me as the internal injuries left by the Scorching Yang Qi sent dark-red blood flowing from my nose, but I endured it.

It only had to last a moment. A very brief moment.

*Inventory open, equip spear.*

The cool shaft of the spear settled into my grip.

Then I pushed off once.

*Boom.*

I shot forward like an arrow—no, faster than an arrow.

Not toward Jin Mukyung, but toward Pung Yang. I could see his broad smile.

“That’s more like it!”

“Shut up, you son of a bitch.”

“Ha-ha-ha-ha!”

Pung Yang’s curved saber was larger than ever before. Brimming with red saber qi, it swung toward me.

*Whoooosh!*

The wind exploded, and even the air seemed to vanish.

I gripped the iron spear until it felt as though it might crumble in my hands.

*Please. Just this once.*

I poured all fifteen years of my internal energy into the spear. Drawing back my shoulder and waist as far as I could, I sent everything I had flying forward.

*One Annihilation.*

*Rumble-rumble-rumble!*

A gigantic mass of saber qi collided with the vortex.

A thunderous roar filled the world, as though the sky itself were splitting apart. Through the raging wind, I saw it clearly.

*Kaboom!*

The white vortex shattered into pieces before the red saber qi. The massive concentration of qi completely pulverized One Annihilation.

Pung Yang whispered with an ecstatic expression,

“This is as far as you go.”

The next moment, Pung Yang’s internal energy surged along the spear and hammered into me.

*Boom!*

Blinding pain and ringing ears rolled over me like waves.

*Ding.*

> **System**
> - You have suffered **Internal Injury**! Your condition is extremely serious!
> - **Scorching Yang Qi** is running wild!
> - You have suffered a **Severe Injury**! All stats have dropped significantly!

System notifications rang out one after another, mixed with the shouts of the Mount Heng martial artists, Lee Seowol’s scream, and Pung Yang’s laughter.

*It’s over.*

The instant my legs gave out despite my will, a powerful hand clamped around my throat.

“Guh. Guhh.”

“That was fairly impressive. If I’d been only a moment slower, you might have won.”

Pung Yang bared his teeth in a grin. The red light in his eyes was slowly fading.

*Damn it. I was so damn close.*

I wanted to say it aloud, but my mouth was full of blood, making even that difficult.

“I swore by the gods of heaven and earth, didn’t I? I swore I’d pull out your tongue.”

Had he said that? By now, even who I was had become hazy.

Pung Yang pried open my mouth with his other hand. I felt his rough fingers tugging on my blood-soaked tongue.

“Ghh…”

“When you were flapping that mouth, didn’t you know this would happen? Huh?”

“Ghaa… hahahaa.”

“Hahaha! What the hell are you mumbling? Shall I let you leave some last words?”

Pung Yang laughed heartily and released my tongue. Only then could I speak. I swallowed the blood in my mouth and said,

“Salty.”

“What?”

“It’s insanely salty.”

“What kind of bullshit is that?”

*What do you think?*

*I’m saying the taste of your fingers brought me back to my senses a little.*

I muttered through my fading consciousness.

*Inventory open, summon anything.*

*Ding.*

> **System**
> - No item named **Anything** can be found. The oldest item stored in your inventory will be summoned first.
> - The **Unnamed Sword** has been summoned.

*The Unnamed Sword? What was that again?*

*Whatever.*

I gathered up the last of my strength and thrust the sword in my hand toward Pung Yang’s chest, which was shrouded in Body-Protecting Qi.

It was a futile last-ditch attack with an obvious conclusion.

*Damn Body-Protecting Qi.*

But this was enough. I had no regrets left.

It was at that moment, as my head slowly drooped—

*Thud!*

*Ding.*

> **System**
> - The **Unnamed Sword** satisfies a specific condition.
> - **Ten-Thousand-Year Cold Iron** has destroyed **Body-Protecting Qi**.

…Huh?
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 119`.

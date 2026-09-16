# Master Edit Task — Chapter 123

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

| 진무경    | **Jin Mukyung**    |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 조필     | **Jopil**          |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 천무학관   | **Heaven's Gate Temple**         |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 검법     | **sword technique**                              |                                                       |
| 권법     | **fist technique**                               |                                                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 호승심 | polysemy | Competitive pride or fighting spirit; not merely a desire to test oneself. | test myself |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
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

#### Chapter 121 tail (verified mastered)

…
there. She continued speaking. “Furthermore, as an apology for what happened, I will transfer every right held by our sect to the Jin Family of Taiyuan.” “Rights?” “Yes. All rights to the territory currently occupied by our sect.” In other words, she was saying that she would hand over all of northern Shanxi to the Jin Family of Taiyuan. *She’s going this far?* The fact that the Mount Heng Sword Sect had bowed its head to the Jin Family of Taiyuan was already a given. Jin Wikyung would demand a great deal in compensation, but even he couldn’t completely swallow the sect whole. Wolhwa had said something similar during our previous conversation. *And now she’s serving it up to us without even being asked.* After calling me her benefactor over and over, it seemed she hadn’t just been paying lip service. Right. Gratitude shouldn’t end with words. Hm. “Thank you. My eldest brother will be pleased.” “There’s more.” *What? She isn’t finished yet?* Lee Seowol took three books from inside her robes and held them out to me. I slowly read the titles on their covers. “Blood Wolf Sword Technique, Blood Wolf Footwork. And……” “Shura Annihilating Fist. The sword technique and footwork technique were created by my father himself. The Shura Annihilating Fist is Uncle Cheol’s secret ultimate technique. Every one of them is an outstanding Peak martial art.” “Peak martial arts…” I swallowed hard. One of the things I had learned painfully in the Murim was the importance of martial arts. Even I was barely able to make up for my deficiencies by relying on the System. For ordinary martial artists, it went without saying. To them, an outstanding Peak martial art was a priceless treasure. *These are worth more than the rights to northern Shanxi.* If those rights were the branches of a tree, the three martial arts manuals before me were its roots. Lee Seowol had placed her father’s legacy—the most valuable possessions of the Mount Heng Sword Sect—on the scales. “Is this a gift too?” “No. This is a transaction.” *I knew it.* A transaction. If it was Jin Wikyung, he would accept the deal by any means necessary. Three Peak martial arts were at stake, after all. *What on earth is she going to demand?* Wealth? A guarantee of safety? Or something else? Lee Seowol—or rather, the Mount Heng Sword Sect—was in a situation beyond desperate. Even if they were offering their martial arts at a bargain price, whatever they wanted in return was certain to be a difficult demand. I cautiously distanced myself from the matter. “I’m curious what kind of transaction this is, but I don’t know if you’re aware—I don’t have that kind of authority.” Lee Seowol gazed steadily at me with eyes as clear as a lake. “Is that so?” “Yes. I don’t have a particular position, either. I think it would be best for you to discuss this separately with my eldest brother later.” “My thoughts differ from yours, Benefactor.” “Excuse me?” “This is a transaction you are fully capable of deciding. Of course, there would need to be many discussions.” “A transaction worth trading three Peak martial arts for…… Then what would our side have to give?” “A person.” “A person?” For an instant, a smile flickered across Lee Seowol’s lips. It was the second time I had seen her smile, and this time, I knew I hadn’t imagined it. “Please marry me.” * * * “Well, I’ll be going.” Hyuk Mujin, who had been pacing around the pavilion’s front courtyard, turned at the sound of a woman’s voice behind him. A beauty who made his chest tickle just by looking at her was descending the pavilion steps. *Good heavens. She’s breathtaking.* Though she was dozens of paces away, it almost seemed as if the cold midwinter wind carried the scent of flowers. *Our squad leader sure is lucky.* He had a handsome face, was the youngest Young Master of the Jin Family of Taiyuan—the universally acknowledged foremost family in Shanxi—and possessed excellent martial arts. When he was with Wolhwa, the words *a celestial beauty and a handsome man* fit them perfectly. And now the Sect Leader of the Mount Heng Sword Sect had been added to the list. Hyuk Mujin let out a deep sigh as he watched Lee Seowol’s back disappear into the distance. *I loved you, however briefly, Young Lady Lee.* When Hyuk Mujin returned to the pavilion, he found Jin Taekyung sitting there half out of his mind. “Squad Leader, what’s wrong?” “……” “Squad Leader. Please come to your senses!” Only after Hyuk Mujin grabbed him by the shoulders and shook him did his unfocused eyes finally clear. Hyuk Mujin asked with a worried expression, “Did something happen? Why are you suddenly acting like this?” *Gulp.* Jin Taekyung swallowed hard and barely managed to open his mouth. “Mujin.” “Yes.” “Do you know how old Lee Seowol is?” “What do you mean, ‘Lee Seowol’? You should call her Sect Leader or Young Lady.” “Unless you want people calling you the late Hyuk Mujin, shut up and answer.” “……” Hyuk Mujin thought for a moment. “How old was she again? I think she was about the age when people started getting married.” He suddenly slapped his forehead. “Oh, I remember.” “H-How old is she?” “Seventeen.” Jin Taekyung’s mouth fell open. “Fuck, she was still a high schooler?”

#### Chapter 122 tail (verified mastered)

…
as I spent most of my time learning to control my newly acquired Scorching Yang Qi, her final words kept returning to me. *Marriage is one of life’s great human obligations, so take your time thinking it over.* I had been so flustered at the time that I could only open and close my mouth. Who would have thought a woman would propose to me first—and a girl who looked so much younger than me, at that? Although it was a cold political marriage proposal—cold enough that calling it a transaction wasn’t an exaggeration—a proposal was still a proposal. The greater shock, however, was still to come. *Seventeen years old? Is this for real?* A first-year high school student was right in the prime school-lunch-eating years. She was two years younger than my late-born little sister, Hayeon, and a full ten years younger than me. *That’s the Murim for you…* This was a world where getting married in middle school and becoming a parent in high school wouldn’t even be strange. If anything, the three brothers of the Jin Family of Taiyuan looked like the oddballs for remaining unmarried at our age. No, wait a second. “What are you staring at?” Jin Mukyung noticed my gaze and asked irritably. He had suffered considerable injuries at Pung Yang’s hands, but he had now recovered enough to move around on his own. *Come to think of it…* I had never heard whether Jin Mukyung was married. I opened my mouth, half expecting the worst. “Just asking in case.” “What?” “Are you married?” Pffft! Jin Mukyung spat tea into my face and hurriedly shouted. “W-What kind of nonsense is that?” “If you’re not, then you’re not. Why are you so flustered?” After receiving that unexpected facial wash, I wiped my face with my sleeve and continued asking questions. “Why haven’t you married?” Jin Mukyung seemed flustered for a moment, then answered readily. “I’m too busy training in martial arts. Women are a luxury to me.” “You make it sound downright frugal.” “Don’t lump me in with a lecherous idler like you. That’s an insult to me.” “…” Lecherous, my ass. I had spent all twenty-seven years of my life single. If dating was a luxury, then I was the very definition of a miser. The only slight difference was that while Jaringobi ate rice while staring at a strip of dried fish, I had a USB drive.[^2] “What’s with that expression? You look incredibly sad.” “Call it regret over the life I’ve lived.” “At last, you’re becoming human.” He seemed to have a different interpretation of my past life, but fine. He could interpret it however he wanted. “But why did you suddenly ask about marriage? It’s something you already know perfectly well.” “Oh, because the Sect Leader of the Mount Heng Sword Sect asked me to marry her.” Pffft! “…For fuck’s sake. Stop spitting.” As I wiped away the second mouthful of tea, Jin Mukyung regained his composure. “The Sect Leader of the Mount Heng Sword Sect?” “Yeah. She said it two days ago.” “Why on earth would she marry someone like you… Ah, of course. It must be a political marriage.” “…” He wasn’t wrong, but it was still pretty damn irritating. At this point, wasn’t I prime husband material both in the Murim and in the real world? “So, are you thinking of doing it?” “Of course not. How could I marry a girl so much younger than me?” “You’re barely twenty, and you say things like that.” *My body is twenty, but my mind is twenty-seven, you bastard.* Besides, I had decided on my answer to Lee Seowol’s proposal long ago. You can’t set up two households when there’s someone you love. There was only one person in my heart right now. *What could Song-i be doing right now?* Just imagining it made me happy. I tilted my teacup with a blissful smile, and Jin Mukyung stared at me with a bizarre expression. “What a disgusting look.” “Anyway, I’m turning down the marriage for various reasons.” “You made the right decision. At the very least, a political marriage has to offer us something in return. If you marry someone you have no feelings for and gain nothing from it, there’s no reason to enter into a political marriage.” I had thought he was a fool who knew nothing but martial arts, but every now and then, he became a surprisingly sharp realist. “And no matter what they offer, it’s out of the question as long as our eldest brother is around. He isn’t the sort of man who would bind you through a political marriage.” “They did make a pretty substantial offer, though.” “Hm. What did they say they would give you?” Jin Mukyung tilted his teacup with an uninterested expression. “The Blood Wolf Sword Technique, the Blood Wolf Footwork, and the Shura Annihilating Fist.” Pffft! “…Ah, fuck.” This time, I didn’t even have time to wipe my face. Jin Mukyung grabbed me by the collar and shook me hard. “Marry her right now!” [^1]: “School lunch” is Korean slang for a school-age kid, while “clank, clank” evokes handcuffs or prison bars—the joke is that sexual interest in a high schooler could land someone in jail. [^2]: Jaringobi is a traditional Korean image of a miser who stares at dried fish while eating rice rather than eat the fish.

## Korean source

```text
＃123화



전신에 붕대를 감은 채 누워 있는 중년인.

뭐가 마음에 안 드는지 미간은 잔뜩 찌푸려져 있고, 몸은 한시도 쉬지 않고 꿈지럭거린다.

“끄응.”

앓는 소리를 흘리자 곧장 면박이 날아왔다.

“너무 움직이지 마세요.”

“그게 아니라…….”

“철 숙부, 의원이 했던 말 못 들으셨어요?”

또 시작이군. 항산호 철무백은 천장만 멀거니 바라봤다. 그러자 이소월이 두툼한 솜이불을 그의 가슴까지 덮어 주며 말을 이었다.

“하루라도 빨리 나으셔야죠. 좀이 쑤시는 건 알겠지만 누워 계세요. 잠이라도 더 주무시고.”

“이미 충분히 잤다.”

“고작 한 시진밖에 안 주무셨잖아요.”

“고작이라니. 한 시진이면 충분하지.”

“그러시다가 몸만 더 상해요.”

“삼십 년을 넘게 그리 살았어. 끄떡없다.”

“지금까지는 이렇게 크게 다치신 적이 없었으니까 그렇죠.”

“……끙.”

이소월의 일침에 철무백은 입을 다물었다.

그녀의 말이 맞다. 수라멸권을 익힌 이래 지금처럼 큰 부상을 입은 적은 없었다. 부러진 사지와 심각한 내상. 의원의 말에 의하면 최소 넉 달은 요양해야 할 중상이라고 했다.

“네 아비와 만났을 때도 이 정도는 아니었는데.”

철무백의 푸념에 이소월이 반응했다.

“아버지요?”

“그래, 천백이 그 친구 말이다.”

“두 분 사이에 무슨 일이 있으셨는데요?”

“이야기한 적 없었더냐?”

“그냥 두 분의 마음이 맞아서 친구가 됐다고 알고 있었어요.”

“그랬지. 하지만 처음에는 목숨을 걸고 싸웠단다.”

“싸워요?”

철무백이 빙긋 웃었다.

“무인 두 사람이 만나서 뭘 했겠느냐? 둘 다 젊은 시절이라 호승심도 강했으니 불 보듯 뻔하지.”

철무백은 창밖을 바라봤다. 삼십여 년 전, 저 높이 솟은 산등성이 어딘가에서 두 사람은 처음으로 만났고, 싸웠다.

“날 찾기 위해 석 달 동안 산맥을 이 잡듯 뒤졌다고 했다. 거지 같은 몰골이었지만 기세가 범상치 않았지.”

고수는 고수를 알아보는 법이다. 아무도 찾지 않는 심산유곡에 틀어박혀 홀로 무공을 익힌 철무백과 수많은 전투를 통해 자신만의 무공을 완성한 이천백.

두 절정 고수의 첫 만남이었다.

“나보고 수하가 되라고 하더구나. 산맥 아래에 문파를 세울 테니 함께 초석을 다지자고 했다.”

“아버지답네요. 그래서요?”

“더 무슨 말이 필요했겠느냐? 싸웠지. 그것도 아주 살벌하게.”

이소월이 피식 웃었다.

“그렇군요.”

“어떻게 됐는지 궁금하지 않으냐?”

“들을 필요가 있나요. 철 숙부께서 지금까지 재야에 머물러 계시는 것만 봐도 알 수 있는 사실인데. 서로의 무공에 감복해서 벗이 되었다는 사내들의 낯 뜨거운 얘기 아닌가요?”

“으하하! 맞다! 딱 오백 합 만에 승부가 났…… 윽.”

큰 소리로 웃던 철무백이 갑작스러운 고통에 움찔하자 이소월이 한숨을 내쉬었다.

“저 때문에 상태가 더 안 좋아지시는 것 같은데…… 제가 없는 게 더 낫겠네요.”

“이 녀석. 혼자 늙어 가는 숙부가 가엾지도 않으냐?”

“생각 있으시면 언제든지 말씀하세요. 중매라도 서 드릴 테니.”

“됐다. 다 늙은 마당에 무슨.”

본인 스스로 한 말이지만 입맛이 씁쓸해진다. 철무백은 마음속으로 뇌까렸다.

‘그래, 어느새 이리 늙었구나.’

가족을 잃은 그 날 이후, 정확히 몇 년의 세월이 더 흘렀는지 철무백 자신조차도 알지 못한다.

심후한 내력과 극도로 단련된 신체 덕분에 본래의 나이보다 젊어 보일 뿐, 정신은 오래전부터 늙어 가고 있었다.

‘하나뿐인 벗도 떠나고, 평생 갈고 닦은 무공도 형편없이 꺾였으니, 허허.’

이제야 비로소 인정할 수 있었다. 항산의 호랑이가 이미 늙었다는 사실을. 하지만 철무백에게는 아직 지켜야 할 것이 남아 있다.

“소월아.”

이소월이 따스한 목소리로 대답했다.

“말씀하세요. 숙부.”

“나는 네가 행복해지길 바란다.”

“알아요.”

“아직 늦지 않았다. 사랑하는 사람과 혼인하거라. 태원진가의 도움을 받는다면 산서 땅 어디에서도 안전하고 행복한 가정을 꾸릴 수 있을 것이다.”

“제가 원하는 것은 가정이 아니라 항산검문이에요.”

철무백의 눈빛에 안타까움이 스쳤다. 갓난아이 시절부터 봐 온 이소월이다. 몰락한 문파를 재건하고 부흥시키는 것은 약관도 채 되지 않은 그녀가 감당하기엔 너무 버거운 짐이었다.

“지금의 선택을 후회할 수도 있다.”

“하지만 제가 무슨 선택을 하더라도 숙부님은 절 믿어 주시겠죠.”

“그렇지 않았다면 네게 수라멸권의 비급을 넘기지 않았을 게다.”

이소월이 철무백의 주름진 손을 움켜쥐었다.

그녀 역시 무가의 여식. 눈앞에 있는 이 늙은 무인이 얼마나 큰 결정을 했는지 알고 있었다.

“감사해요, 숙부.”

어느새 촉촉해진 그녀의 목소리에 철무백이 손을 내저었다.

“난 늙었다. 이제 와서 제자를 들이기도 곤란하던 참인데 좋은 기회가 온 게지.”

수라멸권은 일인전승(一人傳承), 비인부전(非人不傳)의 원칙을 따른다. 행동거지가 올곧고 심성이 바른 후인을 찾아 무맥을 이어 가라는 의도다.

그러나 구 대 계승자인 철무백은 그 원칙을 어기고 이소월에게 비급을 넘겼다. 비록 직접 가르침을 받지는 않았지만 사문(師門) 대대로 내려오는 전통을 깨트린 것이다.

그러나 철무백에게도 나름의 생각이 있었다.

‘진천검과 산서잠룡라면 소월이를 지켜 줄 수 있겠지.’

이소월이 정략혼을 마음먹었다면 그 두 사람이 최선이다.

무공에 대한 재능이야 말할 것도 없고, 불의(不義)에 맞서 목숨 걸고 싸울 만한 협기도 지니고 있다.

‘실제 성정은 어떨지 지켜봐야겠지만…….’

잘만 된다면 정략혼의 목적과 일인전승, 비인부전의 전통. 두 가지 모두를 충족시킬 수 있는 길인 것이다.

“그래서 말인데.”

철무백은 은근한 목소리로 말을 이었다.

“둘 중 누구를 택했느냐?”

이소월이 모르는 척 고개를 갸웃했다.

“어머, 뭐가요?”

“시치미 떼지 말고 말해 보아라. 진천검이냐? 아니면 산서잠룡?”

“글쎄요.”

“그놈이 그놈이긴 한데…… 아무래도 진천검이 낫지 않겠느냐?”

“산서잠룡은 마음에 안 드시나 봐요?”

“뭐, 마음에 안 들 것까지야 있겠냐마는…….”

철무백이 눈살을 찌푸렸다. 일 년의 대부분을 산속 깊은 곳에서 머무르는 그조차도 태원진가의 개망나니에 관한 소문은 들어 봤다.

“아무리 개과천선했다 한들 세 살 버릇 여든까지 가는 법이다. 나중에 네 가슴에 대못을 박지 않을까 걱정되는구나.”

“진천검은요?”

철무백의 찌그러졌던 안색이 펴졌다.

“형만 한 아우 없다고 했다. 어제 잠시 이야기를 나눠 봤는데 사람이 참 괜찮더라. 무재가 아주 뛰어나.”

“무공밖에 모르는 사람이라고 들리는데요.”

“떽! 계집질하는 것보다는 훨씬 낫지. 언행부터가 아주 의젓하고 무게감이 있어. 사내란 자고로 그래야지, 암. 그렇고말고.”

흐뭇하게 웃는 철무백이었다.



* * *



반쯤 눈을 뒤집어 깐 진무경이 내 멱살을 잡고 탈탈 털었다.

“당장 혼인해!”

“컥, 컥!”

가뜩이나 코로 찻물이 들어가는 바람에 사레가 들렀는데 쉬지 않고 멱살을 흔들어 대니 정신이 하나도 없다.

“놔, 안 놔?”

“수라멸권! 혈랑검법! 혈랑보법!”

“알았으니까 일단 놔!”

“이 멍청한 놈! 수라멸권이 어떤 무공인 줄 알고!”

“놓고 얘기하자고!”

“일인전승! 비인부전!”

“그만해, 이 미친놈아!”

잠시 후, 간신히 진무경의 손을 떼어 냈을 때는 전각 내부가 폭풍이라도 지나간 것처럼 엉망이 되어 있었다.

“헉, 허억.”

나는 숨을 고르며 주위를 둘러봤다.

탁자는 주저앉았고, 의자는 박살 났으며 산산조각 난 다기(茶器) 파편이 바닥에 굴러다녔다.

그때 차분해진 얼굴로 옷매무새를 가다듬은 진무경이 입을 열었다.

“음, 진정했다.”

“…….”

이거 생각 이상으로 미친놈이었네.

나는 그나마 덜 젖은 소매로 얼굴을 벅벅 문질렀다.

“수라멸권이 무슨 천하제일 무공이야? 왜 그렇게 집착해?”

“천하에서 열 손가락 안에 드는 권법이지. 아니, 이었다.”

“이었다?”

“이백 년 전의 일이니까. 수천, 수만 권의 서적이 있는 천무학관의 서고에도 기록으로만 남아 있는 무공이지. 그런데 항산호 대협이 바로 그 수라멸권의 당대 계승자였다니!”

상상만 해도 설레는지 진무경의 뺨이 붉게 달아오른다.

나는 코에 들어간 찻물을 털어 내며 물었다.

“그래서?”

“뭣이? 그래서라니!”

진무경이 믿을 수 없다는 눈빛으로 나를 바라봤다.

“바로 그 수라멸권이란 말이다! 이미 오래전 무맥이 끊겼다고 알려진 절정 무공!”

“이백 년 전의 천하십대권법이고?”

“바로 그거다!”

“어, 잠깐만 기다려 봐.”

나는 바닥에 굴러다니는 굵직한 나무 막대기를 주워 들었다. 불과 5분 전까지는 탁자 다리라고 불렸던 물건이다.

“이게 뭔지 알아?”

“몽둥이?”

“잘 아네.”

“그게 뭐 어쨌단 말이냐?”

“이게 이천 년 전쯤에는 천하십대병기. 뭐 그런 거 아니었을까?”

내가 하는 말을 못 알아들을 정도로 멍청한 놈이 아니다.

곧 진무경이 눈을 치켜떴다.

“수라멸권을 그따위 것에 비교하다니.”

“그럼 뭐가 다른데?”

“그건…….”

“물론 이런 나무 몽둥이보다는 훨씬 값어치 있는 물건이긴 하지. 하지만 지금도 마찬가지일까?”

과거 인류는 돌로, 몽둥이로 싸웠다. 그러나 청동과 철기가 등장하면서 시대의 흐름에 뒤로 밀려났다.

수라멸권도 크게 다르지 않다.

“물론 지금도 모두가 탐내는 뛰어난 절정 무공이긴 하겠지.”

그걸 몸소 입증한 것이 항산호 철무백이다. 그는 수라멸권으로 산서성에서 이름 높은 절정 고수가 되었다.

“하지만 수라멸권이 지금까지 천하십대권법인 건 아니잖아?”

돌과 몽둥이가 강철로 바뀐 것처럼, 무공도 발전한다.

나야 뭐, 지금 천하십대권법이 뭔지는 모르지만, 진무경의 표정은 내 말이 틀리지 않았음을 증명했다.

“막말로 수라멸권이 그렇게 강한 무공이었으면 풍양에게 질 일도 없었지. 그리고 이게 가장 중요한 건데……”

나는 탁자 다리를 대충 구석에 던지고 쐐기를 박았다.

“난 혼인할 생각 없어.”

“……!”

“당사자가 안 한다는데 뭐 어쩔 거야. 안 그래?”

“그건…… 그렇지.”

진무경이 한숨을 푹푹 내쉬었다. 여기서도 우기면 한 판 붙으려고 했는데, 의외로 순순하게 수긍하는 것 같다.

그래도 수라멸권의 비급이 자꾸 눈앞에 아른거리는지 아련한 눈빛을 하고 있긴 하지만.

‘이 자식도 어지간히 무공 덕후네.’

하긴, 무공을 더 익히고 싶어서 천무학관에 간 녀석이다.

바로 그 천무학관에서도 기록으로만 남아 있는 수백 년 전의 무공을 발견했으니 몸이 달 수밖에.

“후우우…….”

땅이 꺼져라 한숨을 내쉰 진무경이 중얼거렸다.

“아쉽구나, 아쉬워.”

“그렇게까지 아쉬울 것까지야. 인연이 닿으면 다음에 구할 수 있겠지.”

“멍청한 녀석. 절정 무공이 어디 하늘에서 뚝 떨어지는 줄 아느냐?”

“그래? 난 떨어지던데.”

“천하의 무공이 모두 모여 있다는 천무학관에서도 절정 무공들은 철저히 관리…… 뭐라고?”

“난 하늘에서 떨어졌다고.”

나는 품에서 낡은 서책 한 권을 꺼내 들었다. 겉면에 적힌 네 글자는 세월의 풍파로 흐릿했지만, 충분히 읽을 수 있을 만큼 또렷했다.

화염신장(火焰神掌).

호랑이는 죽어서 가죽을 남기고, 조필은 죽어서 초절정 무공을 남겼다.

“화, 화, 화…….”

아마 오늘이 진무경의 일생을 통틀어 가장 놀라운 날일 거다.

눈을 부릅뜨고 나와 비급을 번갈아 보는 녀석에게 씩 웃어 주었다.

“앞으로 형이라고 불러라.”
```

## Current accepted English baseline

```markdown
# Chapter 123

A middle-aged man lay in bed with bandages wrapped around his entire body.

His brow was deeply furrowed, as if something was bothering him, and his body kept fidgeting without a moment's rest.

“Ugh.”

The moment he let out a groan, a sharp rebuke came flying.

“Please don’t move so much.”

“That’s not it…”

“Uncle Cheol, didn’t you hear what the physician said?”

Here we go again. Cheol Mubaek, the Tiger of Mount Heng, stared blankly at the ceiling. Lee Seowol pulled a thick cotton blanket up to his chest and continued.

“You need to recover as quickly as possible. I know you’re feeling restless, but please stay in bed. At least get some more sleep.”

“I’ve already slept enough.”

“You only slept for two hours.”

“Only? Two hours is plenty.”

“You’ll just make yourself worse.”

“I’ve lived like this for more than thirty years. I’ll be fine.”

“That’s only because you’ve never been this badly injured before.”

“...Urgh.”

Cheol Mubaek fell silent at Seowol’s pointed remark.

She was right. He had never suffered injuries this severe since learning the Shura Annihilating Fist. Broken limbs and serious internal injuries. According to the physician, they were severe enough that he would need at least four months of recuperation.

“I wasn’t this badly hurt even when I met your father.”

Seowol reacted to his complaint.

“My father?”

“Yes. That friend of mine, Cheonbaek.”

“What happened between the two of you?”

“I never told you?”

“I only knew that the two of you became friends because you hit it off.”

“That’s true. But at first, we fought with our lives on the line.”

“You fought?”

Cheol Mubaek smiled faintly.

“What else would two martial artists do when they met? We were both young, and our competitive pride was strong. The answer was obvious.”

Cheol Mubaek looked out the window. More than thirty years ago, somewhere along those towering mountain ridges, the two men had met for the first time—and fought.

“He said he’d searched the mountain range for three months, combing through it inch by inch to find me. He looked like a beggar, but his aura was anything but ordinary.”

Masters recognized masters. Cheol Mubaek had secluded himself in a remote valley that no one visited, training in martial arts alone. Lee Cheonbaek had perfected his own martial arts through countless battles.

It had been the first meeting between two Peak masters.

“He told me to become his subordinate. He said he was going to establish a sect at the foot of the mountains and wanted me to lay its foundation with him.”

“That sounds like Father. So what happened?”

“What else needed to be said? We fought. And we fought viciously.”

Seowol snorted softly.

“I see.”

“Aren’t you curious what happened?”

“Do I need to hear it? I can tell just from the fact that you’ve remained unaffiliated all this time, Uncle Cheol. Isn’t this one of those embarrassing stories men tell about becoming friends after being moved by each other’s martial arts?”

“Ha-ha-ha! That’s right! The fight was decided in exactly five hundred exchanges… ugh.”

Cheol Mubaek had been laughing loudly when a sudden stab of pain made him flinch. Seowol sighed.

“I think I’m making your condition worse by being here… It might be better if I left.”

“Seowol. Don’t you feel sorry for an uncle who’s growing old all alone?”

“If you’re interested, just tell me anytime. I’ll even find someone to set you up with.”

“Forget it. What would I do at my age?”

Although he had said the words himself, they left a bitter taste in his mouth. Cheol Mubaek muttered inwardly.

*Yes. Somehow, I’ve grown this old.*

He did not even know exactly how many years had passed since the day he lost his family.

His deep internal energy and highly trained body made him look younger than his true age, but his mind had been growing old for a long time.

*My one and only friend is gone, and the martial arts I spent my entire life honing have been broken so thoroughly. Heh.*

Only now could he finally admit it. The Tiger of Mount Heng had grown old.

But Cheol Mubaek still had something left to protect.

“Seowol.”

Seowol answered him warmly.

“Yes, Uncle?”

“I want you to be happy.”

“I know.”

“It’s not too late. Marry the person you love. With the Jin Family of Taiyuan’s help, you could build a safe and happy home anywhere in Shanxi.”

“What I want isn’t a family. It’s the Mount Heng Sword Sect.”

A trace of sorrow crossed Cheol Mubaek’s eyes. He had watched Seowol since she was a baby. Rebuilding and reviving a fallen sect was far too heavy a burden for a girl who was not even twenty.

“You may regret the choice you’re making now.”

“But no matter what choice I make, you’ll believe in me, won’t you?”

“If I didn’t, I wouldn’t have given you the martial arts manual for the Shura Annihilating Fist.”

Seowol grasped Cheol Mubaek’s wrinkled hand.

She, too, was the daughter of a martial household. She understood what a momentous decision the old martial artist before her had made.

“Thank you, Uncle.”

At the moisture in her voice, Cheol Mubaek waved a hand.

“I’m old. I was having trouble taking on a Disciple at this point in my life anyway. This was simply a good opportunity.”

The Shura Annihilating Fist followed the principles of a single successor and transmission only to the worthy. Its intent was to find a successor of upright conduct and good character and pass the martial lineage on to them.

Yet Cheol Mubaek, the ninth-generation successor, had broken that principle and handed the martial arts manual to Seowol. Although she had not received direct instruction, he had still broken the tradition passed down through the sect’s generations.

But Cheol Mubaek had his own reasons.

*If she has the Heaven Shaking Sword and the Sleeping Dragon of Shanxi, they’ll be able to protect Seowol.*

If Seowol had decided to enter a political marriage, those two were the best options.

Their talent for martial arts went without saying, and they also possessed the chivalrous spirit to risk their lives standing against injustice.

*Still, I’ll have to watch and see what they’re really like…*

If everything went well, this could satisfy both the purpose of a political marriage and the traditions of a single successor and transmission only to the worthy.

“So, speaking of that…”

Cheol Mubaek continued in a suggestive tone.

“Which one did you choose?”

Seowol tilted her head as if she had no idea what he meant.

“My goodness. Which one?”

“Don’t play dumb. Is it the Heaven Shaking Sword? Or the Sleeping Dragon of Shanxi?”

“I’m not sure.”

“They’re both more or less the same sort, but… Wouldn’t the Heaven Shaking Sword be better?”

“You don’t like the Sleeping Dragon of Shanxi?”

“It’s not that I dislike him…”

Cheol Mubaek frowned. Even he, who spent most of the year deep in the mountains, had heard the rumors about the Jin Family of Taiyuan’s notorious delinquent.

“Even if he has truly reformed, old habits die hard. I’m worried he might break your heart someday.”

“What about the Heaven Shaking Sword?”

Cheol Mubaek’s crumpled expression smoothed out.

“They say a younger brother can’t measure up to his older brother. I spoke with him briefly yesterday, and he seems like a fine person. His talent for martial arts is outstanding.”

“I heard he knows nothing but martial arts.”

“Hey! He’s far better than chasing women. His speech and conduct are both dignified and weighty. That’s how a man ought to be, yes. Absolutely.”

Cheol Mubaek smiled contentedly.

* * *

Jin Mukyung grabbed me by the collar and shook me violently, his eyes half rolled back in his head.

“Marry her right now!”

“Cough, cough!”

Tea had gone up my nose and made me choke, and now Mukyung was shaking me by the collar without pause. I couldn’t think straight.

“Let go! Are you going to let go?”

“The Shura Annihilating Fist! The Blood Wolf Sword Technique! The Blood Wolf Footwork!”

“Fine, but let go first!”

“You stupid bastard! Do you even know what kind of martial art the Shura Annihilating Fist is?”

“Let go and then we’ll talk!”

“A single successor! Only the worthy may inherit it!”

“Enough, you crazy bastard!”

A short while later, by the time I finally pried Mukyung’s hand away, the inside of the pavilion looked as though a storm had passed through it.

“Huff… huff…”

I caught my breath and looked around.

The table had collapsed, the chairs were smashed to pieces, and fragments of broken teaware rolled across the floor.

Mukyung calmly straightened his clothes and spoke.

“Hmm. I’ve calmed down.”

“…”

This guy was even crazier than I’d thought.

I scrubbed my face with the sleeve that was relatively dry.

“Is the Shura Annihilating Fist some kind of greatest martial art in the world? Why are you so obsessed with it?”

“It was one of the ten greatest fist techniques in the world. No—it was.”

“It was?”

“It was two hundred years ago. Even in the library of Heaven’s Gate Temple, which contains thousands upon thousands of books, the only records of this martial art are written accounts. And yet the Great Hero Tiger of Mount Heng was the current successor to the Shura Annihilating Fist!”

His cheeks flushed with excitement at the thought.

I snorted the tea out of my nose and asked, “So?”

“What do you mean, ‘so’?”

Mukyung stared at me as if he couldn’t believe what he was hearing.

“I’m talking about the Shura Annihilating Fist! A Peak martial art whose lineage was believed to have died out long ago!”

“And it was one of the ten greatest fist techniques in the world two hundred years ago?”

“That’s exactly it!”

“Wait a second.”

I picked up a thick wooden stick rolling across the floor. Until five minutes ago, it had been called one of the table legs.

“Do you know what this is?”

“A club?”

“You know your stuff.”

“What does that have to do with anything?”

“Wouldn’t this have been one of the ten greatest weapons in the world around two thousand years ago?”

He wasn’t so stupid that he couldn’t understand what I was saying.

Mukyung’s eyes widened.

“How dare you compare the Shura Annihilating Fist to something like that.”

“Then what’s the difference?”

“That…”

“Of course, it’s far more valuable than a wooden club like this. But is it still the same now?”

In the past, humans fought with stones and clubs. But once bronze and iron appeared, those weapons were pushed aside by the march of the ages.

The Shura Annihilating Fist was no different.

“Of course, it’s still an outstanding Peak martial art that everyone would want.”

Cheol Mubaek himself had proven that. He had become a renowned Peak master in Shanxi Province through the Shura Annihilating Fist.

“But it isn’t still one of the ten greatest fist techniques in the world, is it?”

Just as stone and clubs had been replaced by steel, martial arts advanced as well.

I had no idea what the ten greatest fist techniques in the world were now, but Mukyung’s expression proved that I wasn’t wrong.

“To put it bluntly, if the Shura Annihilating Fist were really that powerful, Pung Yang wouldn’t have defeated him. And this is the most important part…”

I tossed the table leg carelessly into a corner and drove home the final point.

“I have no intention of getting married.”

“...!”

“If the person involved says he won’t do it, what can you do? Right?”

“Well… That’s true.”

Mukyung let out one deep sigh after another. I’d been prepared to fight him if he kept insisting, but he seemed surprisingly willing to accept it.

His wistful gaze still suggested that he couldn’t stop thinking about the martial arts manual for the Shura Annihilating Fist, though.

*This guy is a martial arts nut too.*

Then again, he had gone to Heaven’s Gate Temple because he wanted to learn more martial arts.

And now he had discovered a martial art from several hundred years ago that existed only in the records of that very same temple. Of course he couldn’t contain his excitement.

“Hoo…”

Mukyung let out a sigh deep enough to make the earth cave in and muttered,

“What a shame. What a shame.”

“It’s not that big a deal. If fate brings it around, we can get it another time.”

“You idiot. Do you think Peak martial arts just drop out of the sky?”

“Really? Mine did.”

“Even at Heaven’s Gate Temple, where all the martial arts in the world are gathered, Peak martial arts are strictly controlled… What did you say?”

“I said mine fell out of the sky.”

I pulled an old book from inside my clothes. The four characters written on its cover had been blurred by the ravages of time, but they were still clear enough to read.

**Flame Divine Palm.**

A tiger leaves its hide when it dies, and Jopil left behind Supreme Peak martial arts.

“Flame, Flame, Fla…”

Today was probably the most astonishing day of Jin Mukyung’s entire life.

I grinned at him as he stared wide-eyed, looking back and forth between me and the martial arts manual.

“From now on, call me hyung.”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 123`.

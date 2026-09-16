# Master Edit Task — Chapter 142

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
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 공일혁    | **Gong Ilhyuk**    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 검법     | **sword technique**                              |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 문주     | **Sect Leader**                              |
| 장문인    | **Sect Leader**                              |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 사숙     | **Martial Uncle**                            |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 매화검법 | **Plum Blossom Sword Technique** | Huashan sword technique Cheongpung performed at age ten. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 태사부 | **Grandmaster** | Huashan title referring to Mae Jonghak. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 꼰대 | **boomer** | Modern slang for a hidebound older person; used by Cheongpung. |
| 대종남파 | **Great Zhongnan Sect** | Expanded and formal reference to the Zhongnan Sect. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 공일혁 | 이풍 | martial_rivals | Li Feng of Huashan | casual and taunting | Mocks Li Feng's office and recalls his defeat at Huashan ten years earlier. |
| 이풍 | 공일혁 | martial_rivals | you bastard | hostile and furious | Responds to Gong Ilhyuk's insult toward Huashan with an openly aggressive form. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 공일혁 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | condescending and dismissive | Uses 후배님 while ordering Taekyung to move aside. |
| 진태경 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | polite but firm | Uses 선배님 while intervening on Cheongpung's behalf. |
| 공일혁 | 청풍 | senior_martial_artist_to_junior_martial_artist | Junior | impatient and condescending | Treats Cheongpung as a junior while demanding his introduction. |
| 청풍 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | deferential and apologetic | Uses 선배님 while apologizing for catching Ilhyuk's wrist. |
| 이풍 | 진태경 | senior_official_to_respected_young_martial_artist | Young Hero Jin | formal and respectful | Addresses Taekyung as 진 소협 after praising his reputation. |
| 공일혁 | 홍진 | junior_official_guest_to_senior_official | Deputy Military Commissioner | formal and deferential | Appeals to Hong Jin for his view on the impending disturbance. |
| 이풍 | 청풍 | Huashan lay disciple to martial uncle | Young Hero; Martial Uncle Cheongpung | formal and reverent | Li Feng initially addresses Cheongpung as 소협 while testing his knowledge, then recognizes him as 사숙 after witnessing his Huashan sword technique. |
| 홍진 | 공일혁 | political_host_to_guest | Great Hero Gong | polite but cutting | Hong Jin uses the respectful title while dismissing Gong Ilhyuk and exposing his poor judgment. |
| 청풍 | 이풍 | Martial Uncle to Martial Nephew | Martial Nephew Li Feng | exuberant and deferential | Cheongpung adopts the address to obtain royal-guard armor and weapons. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 진태경 | 이풍 | junior_to_respected_official_and_martial_ally | Great Hero Li | polite and respectful | Agrees with Li Feng's proposal that Zhu Bao visit the Jin Family's banquet. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |

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

# Chapters 135–139

## Plot

At Honghwa Inn, Jin Taekyung finishes humiliating Woo Jintae and beats the remaining four heirs of the Five Gates of Shanxi with sword-case blows. The inn’s guests recognize Taekyung as the Sleeping Dragon of Shanxi and side with the Jin Family of Taiyuan. Cheongpung, curious about violence, asks to strike the final heir himself. The injured heirs later discuss the collapse of the Mount Heng Sword Sect, the Jin Family’s growing influence, and their need to attend the City Lord’s luncheon. They also resolve to investigate Cheongpung.

Taekyung, Hyuk Mujin, and Cheongpung move to Honghwa Inn’s private annex and discover its hot springs. Cheongpung, who has never experienced one, decides to stay. Mujin’s warnings about hidden Murim grudges are based largely on wuxia novels, prompting Taekyung to punch him.

Prince Shangshan’s royal command summons the young prodigies to a noon luncheon. Because Mujin’s face is bruised and Woo Jintae remains unconscious, Taekyung substitutes Cheongpung as the delegation’s most impressive member. They travel in a six-horse carriage; Cheongpung’s complete lack of worldly and royal etiquette nearly causes repeated crises, including detaching a golden dragon ornament and calling the resident prince a king.

At the Shanxi Provincial Office, Assistant Military Commissioner Li Feng confronts Eunuch Hong, who has invited the Three Hands of Zhongnan to entertain the prince. Gong Ilhyuk taunts Li Feng over a defeat at Huashan ten years earlier. When Taekyung’s group arrives, the tense gathering includes Li Feng, Hong Jin, and three young martial artists from the Zhongnan Sect. Taekyung identifies himself as Jin Taekyung of the Jin Family, easing the hostility, then recognizes Zhongnan from a novel he once read before stopping himself from revealing too much.

## Continuity

- Woo Jintae is unconscious and severely swollen after Taekyung’s beating; the other four Five Gates heirs are injured but attend the luncheon.
- Jang Childeuk is present at Honghwa Inn as a Level 15 supporter of the Jin Family.
- Cheongpung is an undetectable-Level Peak master, was raised in the mountains, lacks worldly etiquette, and has now become interested in hot springs and firsthand martial experiences.
- The City Lord is Prince Shangshan, a ten-year-old member of the imperial family. His luncheon is held at the Shanxi Provincial Office, a heavily fortified palace-like complex with highly trained soldiers and long-term wartime stores.
- Hyuk Mujin remains at Honghwa Inn because Taekyung bruised his face; Taekyung continues to conceal the real reason for Woo Jintae’s absence.
- The unnamed martial official is Li Feng, Shanxi’s Level 68 Assistant Military Commissioner, a former Huashan lay disciple who left roughly ten years ago and has nearly mastered the Seven Plum Sword.
- Eunuch Hong is Shanxi’s powerful Deputy Military Commissioner and Li Feng’s political rival.
- Gong Ilhyuk is the third of the Three Hands of Zhongnan; Huashan and the Zhongnan Sect have been rivals in Shaanxi for about a century.
- Hong Jin is Level 22, delicate in appearance and voice, and welcomes Taekyung at the luncheon.
- The three Zhongnan martial artists’ names and individual identities remain unresolved. The earlier dispute involving Li Feng, Huashan, and an insult also remains unresolved.
- Taekyung nearly exposed that he knows Zhongnan from a novel, raising an unresolved question about what he intended to say and whether anyone noticed.

## Translation Decisions

- Render 칠매검 as **Seven Plum Sword**, 상산왕 as **Prince Shangshan**, 도지휘첨사 as **Assistant Military Commissioner**, 도지휘동지 as **Deputy Military Commissioner**, and 종남삼수 as **Three Hands of Zhongnan**.
- Render 육두마차 as **six-horse carriage**, 속가제자 as **lay disciple**, and 초일류 as **advanced First Rate**.
- Use **His Highness** for the formal royal address 전하; retain **king** when Cheongpung uses 왕 literally.
- Render 군문 as **military** when describing an affiliation.
- Render Cheongpung’s first-experience villain phrasing and his etiquette mistakes in a comic but politically dangerous tone.

### Prior accepted reading-copy tails

#### Chapter 140 tail (verified mastered)

…
Cheongpung, and I live in Shanxi.” Gong Ilhyuk had been left speechless, but he finally came to his senses and stammered out a question. “Ahem. Then you must also be one of the young prodigies of the Five Gates of Shanxi.” “Huh? No.” “You’re not?” “No. I came from Henan.” “You just said you were from Shanxi.” “I live in Shanxi, so that makes me a Shanxi man. Hehe.” “You… Whew.” A furrow appeared in Gong Ilhyuk’s forehead. He clearly wanted to throw a punch right then and there, but the occasion forced him to hold himself back. “Fine. Then which sect in Henan are you from? The Iron Blood Sect? The Five Tigers Sword Sect?” “Where are those?” “You’re from Henan, yet you’ve never heard of the Iron Blood Sect or the Five Tigers Sword Sect? How does that make any sense? What, are you from Shaolin Temple?” “Oh, I only stayed in Henan for about two weeks before moving to Shanxi, so I don’t know much about it.” “You said you were from Henan!” “I did come from Henan, but before that, I was in Shaanxi…” “You little bastard! Just say the whole world is your hometown!” Gong Ilhyuk finally exploded. With a roar, he reached for Cheongpung’s collar—or tried to. Grab. His wrist was caught with absurd ease. Gong Ilhyuk let out a hollow laugh. “Well, look at you. You know at least one trick, huh?” “Ah, I just reacted on instinct. I’m sorry, Senior.” “On instinct? And you’re apologizing?” Seeing Cheongpung apologize with a miserable expression, Gong Ilhyuk gave a short laugh. “No. There’s no need to let go. No need to apologize, either.” “Really?” “Yes. But you’ll pay dearly for your reckless bravado.” “What? What does that mean?” “You’re about to find out.” I stepped in at that exact moment. I threw myself in front of Cheongpung, and Gong Ilhyuk regarded me coldly. “Move aside, Junior.” “Pardon me, Senior.” “Pardon you… Should I take this to mean the Jin Family of Taiyuan intends to oppose the actions of our sect?” I answered calmly. “Not at all. I only want to stop this from becoming a bigger problem.” “A problem? What problem?” “His Highness will be arriving soon, won’t he? And there are plenty of eyes on us.” “Plenty of eyes. Deputy Military Commissioner, what do you think?” I could see Hong Jin smiling behind Gong Ilhyuk. His lilting voice followed. “Well, I don’t think it will be much of a problem.” Li Feng immediately objected. “This is the grand hall. We cannot tolerate even a minor disturbance.” “Assistant Commissioner Li, I find the word ‘tolerate’ unpleasant. Anyone listening might think you were my superior.” “Deputy Military Commissioner!” “Why, Assistant Military Commissioner?” No sooner had Hong Jin finished speaking than the other two members of the Three Hands of Zhongnan quietly stepped in front of Li Feng. True to the Zhongnan Sect’s reputation, both were at least advanced First Rate masters. Li Feng bit down hard on his lip, then looked at me and muttered, “I’m sorry.” Gong Ilhyuk smiled triumphantly. “Well? What will you do now?” What else could I do? I shrugged once and stepped back. Gong Ilhyuk’s smile deepened. “A wise choice.” “I only wanted to prevent the problem from getting bigger. You understand, right?” “Of course. Everyone here will remember it clearly.” “I hope so.” Cheongpung stared blankly at me. “Benefactor, did I do something wrong?” Gong Ilhyuk answered before I could. “What? Wrong?” His murderous gaze swung toward Cheongpung. “Are you insulting me and the Zhongnan Sect right now?” “That’s not it. I was just…” “Can’t you shut that mouth of yours?” A complicated, subtle expression appeared on Cheongpung’s face. Then he said the one thing more than enough to make Gong Ilhyuk lose his reason. “Wow, no one’s ever sworn at me before. This is fascinating.” “You goddamn bastard…!” Whoosh! A heavy sound split the air. Gong Ilhyuk’s fist shot toward Cheongpung’s ribs at blinding speed. Then— Crack. Crunch. “……!” “……!” Amid the stunned silence, one man’s mouth fell open in agony. His fist had been crushed. Bone jutted through the torn flesh of his forearm, and Gong Ilhyuk, drenched in blood, asked in a trembling voice, “Wh-what is this? What kind of fist technique…?” If he hadn’t asked, I would have. I had expected this result, but not to this extent. With a single counter, Cheongpung had rendered Gong Ilhyuk, a master above Level 70, completely helpless. And… “That wasn’t a fist technique.” At my mutter, Cheongpung answered with a face that looked ready to vomit. “Benefactor is right. It wasn’t a fist technique. It was a palm technique called the Taeeul Miri Palm. But Senior, you’re bleeding too much. The smell of blood is making my stomach churn. Urk!” What a lunatic. I let out a hollow laugh as Cheongpung flung Gong Ilhyuk aside and began to dry-heave. That was when— “Ta-Taeeul Miri Palm!” Li Feng asked with his eyes wide. “Did you just say Taeeul Miri Palm? Are you certain?” “Urk, yes. My grandfather taught me.” “M-May I ask his name?” “Urk, Mae Jonghak—bleeegh!” Splash! I was shocked that Cheongpung had vomited in the very place where the king was about to arrive, but Li Feng seemed unfazed. He trembled as though he had been struck by lightning, then squeezed out a single word. “The Sword Saint…!”

#### Chapter 141 tail (verified mastered)

…
breaking through ten formations did we reach his residence. Can you guess what I saw there?” Everyone present could guess. Li Feng’s gaze was fixed on Cheongpung’s face. “A cute little boy. He was much smaller than the other children his age, but he was diligently swinging a sword… No one could laugh. Who could laugh after seeing a monster perform the Plum Blossom Sword Technique at the age of ten?” “……!” “……!” Silent shock spread through the crowd. Gong Ilhyuk stammered. “That—that’s impossible. As far as I know, one must be at least First Rate to perform the Plum Blossom Sword Technique…” “Unimaginable things sometimes happen in Murim. Compared to that, pulling dirty tricks in a friendly duel is nothing.” Li Feng gave a self-deprecating laugh. “After more than a month of facing the wall in training, I came to a realization. I had no reason to remain there. That was why I left Huashan. What do you think? Isn’t it amusing?” Li Feng’s story hit hard. Everyone, myself included, stared silently at Cheongpung. Suddenly, I remembered the conversation I’d had with him at Honghwa Inn the night before. *“I was ten years old. One day, dozens of people came barging in and made a scene. I remember my grandfather shouting at them to get the hell out before he set fire to the mountain.”* *“Ah. So that’s why he keeps changing where he lives…?”* *“Yes. Fortunately, the mountain is so large that he’s managed to avoid them for ten years.”* Until then, I hadn’t known that the people who had come to cause trouble ten years ago were the leaders of Huashan, or that the Sword Saint Mae Jonghak was Cheongpung’s grandfather. And the part about them making a scene was only how it had appeared from young Cheongpung’s perspective. The reality had probably been very different. *Who would cause trouble for the Sword Saint? That’s a perfect way to get yourself killed.* The Sword Saint who had threatened to set fire to his own sect wasn’t exactly ordinary, either. In any case, on the day Huashan had nearly become a real volcano, Li Feng had met Cheongpung as a child and clearly despaired after witnessing his talent. *Fair enough. First Rate at the age of ten.* Countless people failed to reach First Rate even after turning twenty. Two of the rising martial artists from the Five Gates of Shanxi present here still fell short of being called First Rate masters. And yet Cheongpung had reached that realm at the age of ten. *Could Jin Mukyung have done the same?* The moment that question occurred to me, Gong Ilhyuk shouted as though having a fit. “Proof! What proof is there that he’s that child?” The rising martial artists of the Five Gates of Shanxi who had been trying desperately to curry favor, Hong Jin, who had been watching with great interest, and even the other two members of the Three Hands of Zhongnan all frowned as though they had planned it together. “There is no proof. All I have is my memory.” “Exactly. Mountains and rivers change in ten years. Should I really trust your paltry memory?” “No. To be honest, I’m not certain either. I don’t know how that child grew up.” Li Feng answered calmly, then suddenly drew his sword. *Shing.* He studied the blade as it radiated a cold chill, then asked Cheongpung, “Young Hero, how much do you know about Huashan’s martial arts?” Cheongpung answered with a bewildered expression. “Uh, I’m not from Huashan.” “You’re not from Huashan…” “No. My grandfather just taught me various things because he said they would be good to learn.” “Then allow me to ask. Of the Six Harmonies Sword, Plum Blossom Sword Technique, Supreme Clarity Sword, Taeeul Miri Palm, Falling Flower Chasing Shadow Palm, and Scattering Flowers Shadowless Hand… how many do you know?” “All of them.” “Heh. All of them. Every one.” Li Feng gave a hollow laugh and handed his sword to Cheongpung. “Could you perform the Plum Blossom Sword Technique?” “My grandfather told me not to show my martial arts to anyone.” “One form—no, a single sword stroke will suffice.” After hesitating, Cheongpung took hold of the hilt. “Then I’ll show you briefly.” The instant he finished speaking, something changed. *Sssssss.* *Sword Energy? No.* From Cheongpung’s head to his toes, tangible strands of purple qi flowed from his entire body. It was Extreme Yang internal energy so potent that merely being near it scorched the breath in one’s lungs. “The Zaha Divine Technique[^2]…!” Li Feng let out a cry of delight. At that moment— *Whoosh!* The tip of Cheongpung’s sword traced a beautiful arc. Like plum blossoms falling at the end of the season, a single streak of Sword Energy cleaved the enormous table in half. The food, the dishes, even the sturdy table. “Ah…” A gasp escaped me before I knew it. Breaking things was easy. But Cheongpung’s Sword Energy was so sharp and clean that, if the table hadn’t collapsed a moment later, no one would have noticed it had been cut. *Boom! Crash!* As the table split in two and collapsed, Li Feng clasped his fist and palm in an exceedingly respectful salute. “Li Feng, lay disciple of Huashan, pays his respects to Martial Uncle Cheongpung.” [^1]: Candied hawthorn skewers are fruit skewers coated in hardened sugar. [^2]: A Huashan internal-energy technique.

## Korean source

```text
＃142화



“화산파 속가제자 이풍, 청풍 사숙(師叔)께 인사 올립니다.”

자하신공과 매화검법. 마지막으로 이풍의 입에서 흘러나온 한 단어, 사숙.

이 믿기지 않는 상황에 공일혁의 얼굴이 시커멓게 물들었다.

‘그럼 정말 저놈이?’

검성의 친손자는 아니더라도 한 가지는 확실하다.

어리둥절한 얼굴로 허리만 꾸벅꾸벅 숙이는 저 얼간이가 검성 매종학의 모든 것을 물려받은 후인(後人)이라는 것.

“이, 이럴 리가 없는데. 이건 정말 말도 안 되는…….”

공일혁이 더듬거리며 현실을 부정하던 그때. 간드러진 목소리가 귓가에 닿았다.

“공 대협.”

“아, 도지휘동지.”

홍진을 발견한 공일혁의 안색이 한결 밝아졌다.

종남파는 관(官)과의 연계를 통해 여러 가지 사업을 벌이고 있었고, 홍진은 그 과정에서 알게 된 산서성의 권력자였다.

이 곤경에서 그에게 구원의 손길을 내밀 수 있는 유일한 사람이기도 하다.

“이게 어떻게 된 일인가요?”

홍진의 부드러운 목소리에 공일혁의 마음이 편안해졌다.

“제가 잠시 착각한 모양입니다.”

“착각이라니, 무슨 착각이요?”

“그저 검성의 이름을 팔고 다니는 사기꾼 정도로 생각했는데…….”

“글쎄요, 전 무공 쪽은 영 문외한이지만 사기꾼처럼 보이지는 않던데요?”

“야, 약간의 오해가 있었던 것뿐입니다.”

“오해라…….”

나지막이 읊조리던 홍진이 공일혁을 빤히 바라봤다.

“공 대협.”

“예, 도지휘동지.”

“내가 왜 공 대협을 비롯한 종남파의 분들을 이 자리에 초대했는지 알아요?”

“압니다, 잘 알지요.”

이유는 두 가지다.

첫 번째로는 산서 성주이자 황족인 상산왕과 안면을 트고 새로 벌이는 사업의 재가를 받기 위해서.

두 번째는 홍진의 정적인 이풍의 콧대를 바짝 눌러 주기 위해서다.

“그런데 공 대협도 알다시피 내가 근래 좀 바빴거든요. 그러다 보니 경황이 없어서 전하께 다른 손님이 오신다는 말씀을 못 드렸네?”

“그러시군요.”

콧소리가 빠진 목소리는 건조하기만 할 따름이었다. 공일혁이 불안한 얼굴로 물었다.

“한데 갑자기 그 말씀은 왜…….”

“오늘은 이만 가 줬으면 해요.”

“예?”

“아무래도 불청객이 있으면 전하께서 심기가 불편하시지 않겠어요?”

명백한 축객령이었다. 거기에 더해 불청객이라는 말까지.

공일혁이 항변했다.

“불청객이라니요, 도지휘동지. 그게 대체 무슨 말씀이십니까?”

“어머, 두 번 말해야 하나요? 앞서 했던 말 그대로예요. 전하께 미처 말씀드리지 못했어요.”

홍진은 본래 내관(內官)이다. 상산왕이 갓난아기였던 시절부터 옆을 지켰고 덕분에 산서성부의 실세이자 군부 이인자인 도지휘동지라는 자리까지 꿰찼다.

이처럼 어린 왕의 총애를 한 몸에 받는 그가 고작 미리 말을 못 했다는 이유로 손님을 돌려보낸다니?

“저, 저는 도지휘동지께서 무슨 말씀을 하시는 건지 이해가 잘…….”

당황한 공일혁을 향해 홍진이 싱긋 웃어 보였다.

“공 대협.”

“예.”

“그렇게 안 봤는데, 머리가 좀 나쁘네?”

“……예?”

“아니면 눈치가 없는 건가?”

갑작스러운 폭언에 사방이 고요해졌다. 공일혁을 비롯한 종남삼수의 다른 두 사람이 주먹을 부르르 떨었다.

“말씀이 과하시군요.”

“어머, 그렇게 느꼈다면 내 의도를 제대로 파악한 거예요. 일부러 좀 과하게 한 면이 없잖아 있거든.”

“도지휘동지!”

“목소리 줄여요, 여기 대전이야.”

“갑자기 이러시는 연유가 뭡니까! 설마 방금 일로 제게 실망이라도 하신 겁니까!”

“목소리 줄이라니까. 그리고 난 공 대협한테 실망한 것 없어요. 우리가 친구도 아니고, 서로에게 뭔가를 기대하고 실망할 사이는 아니잖아.”

“그런…… 우리 종남파와의 약조는 잊으신 겁니까?”

“약조? 아, 산서성 쪽에 길을 터 달라는 그거?”

홍진이 피식 웃으며 말을 이었다.

“원래 거래라는 게 그런 거예요. 일이 성사되기 전에는 언제 어그러질지 모르는 거거든. 설마 아직 전하의 재가도 안 떨어진 일을 말 몇 마디로 다 끝났다고 생각한 건 아니죠?”

공일혁은 끓어오르는 분노를 간신히 억눌렀다.

사문인 종남파에는 일이 끝난 것처럼 호언장담해 둔 상태.

이번 일이 성공하면 그에 상응하는 보상을 받겠지만 실패한다면 질책을 피할 수 없다. 그로서는 최대한 눈앞의 내관 놈을 구슬려야만 했다.

“이번 일이 잘만 성사된다면 도지휘동지께도 좋은 일이 아닙니까. 종남파는 결코 은원(恩怨)을 잊지 않습니다.”

은혜면 은혜지, 굳이 원한까지 덧붙인 것은 은근한 협박이었다. 구파일방 중 하나를 적으로 돌릴 수도 있다는 경고.

어린 시절부터 내관으로 지내며 온갖 암투를 지켜본 홍진이 그 말에 서린 속뜻을 못 알아들을 리 없다.

‘쯧쯧. 이래서 무림인들이란.’

홍진은 내심 혀를 찼다.

언행 하나하나가 서투르고 노골적이다.

그에겐 공일혁처럼 어중간하게 닳은 인물보다는 아예 무인답게 과묵하고 뚝심 있는 이풍이 훨씬 까다로운 적수였다.

‘지금 누가 칼자루를 쥐고 있는지도 모르고.’

원하는 목표가 있다면 설설 기어도 모자랄 텐데 협박까지 곁들이다니. 그러나 덕분에 그는 마음을 굳혔다.

“공 대협. 나처럼 여린 사람은 그런 말 들으면 무서워서 같이 일 못 해요.”

“아, 혹시 오해의 소지가 있었다면…….”

공일혁이 몰랐던 척 사과하려던 그때, 지루한 표정으로 두 사람을 지켜보던 진태경이 한마디를 툭 던졌다.

“오해의 소지는 무슨. 지나가던 개도 안 믿겠네.”

“이, 이……!”

“거, 종남파 선배님들. 뭐 얼마나 대단한 사업을 하시는지는 모르겠는데 나중에 따로 얘기하시면 안 됩니까? 안 그래도 밥상 엎어진 것도 서러워 죽겠는데.”

바닥을 뒹구는 음식들을 보며 입맛을 다시는 진태경의 모습에 홍진이 실소를 터트렸다.

“걱정 말아요. 이분들이 나가시면 새로 음식을 들이라 할 테니까. 그렇죠?”

이제는 나가라고 등까지 떠미는 상황. 공일혁이 이를 악물었다.

“도지휘동지. 제 안목이 형편없다는 건 인정합니다. 다만, 부디 오늘 일로 뭘 잃고 얻을지를 잘 생각하십시오.”

“뭘 착각하시는 모양인데, 철저하게 실익을 따져서 내린 결정인걸요?”

“그게 무슨……?”

“일은 계속 진행할 겁니다. 섬서와 산서를 연결하는 전용 무역로와 무역소도 지을 거고 규모도 늘릴 거예요.”

“그럼 더욱더 본문과 손을 잡아야 하지 않겠습니까!”

처절하게까지 느껴지는 외침에 홍진이 눈을 동그랗게 떴다.

“섬서에 있는 문파가 종남파밖에 없나요? 제가 알기로는 종남파보다 훨씬 오래되고 세간의 인식도 좋은 곳이 있다던데.”

“……지금 혹시 화산파를 말씀하시는 겁니까?”

공일혁의 얼굴이 와락 일그러졌다.

화산과 종남은 지난 수백 년간 수없이 신경전을 벌여 온 숙적 관계.

이번 일이 다른 문파도 아니고 화산에게 넘어간다면 가벼운 질책 정도로 끝날 리가 없었다.

“제게 어떻게 이러실 수 있습니까!”

“당연히 이럴 수 있죠. 더 좋은 선택지가 눈앞에 있는데.”

“본문도 결코 화산파에 밀리지 않습니다. 아니, 당대에 이르러서는 오히려 화산파를 넘어섰다고 자부할 수 있습니다.”

“자부할 수 있다라. 사문에 충성하는 모습은 보기 좋아요. 하지만 제 입장에서는 자타공인(自他共認)이라는 말이 더 듣기 좋지 않을까요?”

홍진은 막힘없이 말을 이었다.

“공 대협. 단도직입적으로 물어볼게요. 종남파에도 검성 같은 고수가 있나요?”

“……그건.”

“그럼 저기 있는 소협과 같은 걸출한 후기지수는요?”

“…….”

공일혁을 포함한 종남삼수 전원은 쉽게 입을 열지 못했다.

검성? 종남파의 문주인 풍운검군이 종종 십왕(十王)에 비견되기는 하나 딱 거기까지다.

하물며 청풍 같은 괴물은 듣도 보도 못했다. 특히 선공하고서도 일 합 만에 무릎을 꿇어야 했던 공일혁은 얼굴이 붉어졌다.

“하, 하지만 본문에 소속된 절정 고수들의 숫자는 결코 화산파에 비해 밀리지 않습니다.”

“내 듣자 하니 무림 문파의 힘은 고수가 몇 명이냐가 아니라 ‘어떤’ 고수를 품었느냐에 따라 달라진다고 하더군요.”

정곡을 찌르는 홍진의 한마디에 공일혁은 순간 말문이 막혔다.

그러나 어떻게든, 무슨 수를 쓰든 화산파에게 자리를 뺏기는 것만은 막아야 했다.

“또, 또한 지금까지 관과 협력했던 것 모두 성공적으로 마무리 지었고요. 반면에 화산파는 지금까지 이런 일을 추진해 본 경험이 없습니다. 서투르고 실수가 생길 수밖에 없죠.”

“어머, 그래요?”

싱긋 웃은 홍진이 누군가를 향해 고개를 돌렸다.

“이 첨사, 어떻게 생각해요?”

묵묵히 지켜보고 있던 이풍이 대답했다.

“맞는 말입니다. 화산은 관과 무림을 확실히 구분 짓는 편이지요.”

홍진이 눈살을 찌푸리고, 공일혁의 얼굴에 화색이 돌던 그때 이풍의 묵직한 목소리가 이어졌다.

“하지만 누군가에게나 처음이란 게 존재하지 않겠습니까?”

“이풍, 네놈이!”

홍진이 깔깔 웃었다.

“우리 이 첨사, 진짜 많이 늘었다니까.”

“누구 덕분이지요.”

불과 한 식경 전에도 같은 내용의 대화를 나눴지만 분위기는 그때와 정반대다.

두 사람은 화기애애한 분위기 속에서 대화를 이어 갔다.

“이 첨사가 다리를 놔 줬으면 하는데. 어떻게 생각해요?”

“물론입니다. 사부님께 전서구를 보내지요. 이 소식을 들으면 장문인께서도 좋아하실 겁니다.”

“아, 그리고 여기 귀한 손님이 계시다는 사실도 알려 드리고.”

홍진의 눈짓이 향하는 곳을 바라본 이풍이 슬며시 웃었다.

“그건 태사부께서 좋아하실 소식이고요.”

“시작이 좋네요.”

“제 생각도 그렇습니다.”

어느새 대화에서 완전히 배제된 공일혁은 신형을 부르르 떨었다.

이미 되돌리기에는 너무 와 버린 상황. 그는 분노와 배신감이 섞인 눈빛으로 좌중을 쓸어 봤다.

“감히, 감히 대종남파를 무시하다니.”

“저기, 아까부터 말하고 싶었는데.”

불쑥 끼어든 목소리의 주인공은 진태경이었다. 그가 피식 웃으며 말을 이었다.

“종남파를 무시한 게 아니라, 그쪽을 무시한 겁니다. 몰라서 그렇지, 나 종남파 엄청 좋아해요. 군림…… 아무튼 삼십사 권까지 꼬박꼬박 봤어.”

“그게 무슨 개소리냐! 족보도 없는 태원진가 따위가 끼어들 자리가 아니다!”

진태경이 상처받은 얼굴로 청풍의 옆구리를 찔렀다.

“청 소협. 저 아저씨가 우리 집 족보도 없대.”

“헉, 은인한테요?”

“응. 아무리 선배라지만 말이 너무 심한 거 아니야? 구파일방이라 무서워서 대답도 못 하겠고, 청 소협이 대신 말 좀 해 줘.”

“제, 제가요? 저 그런 거 잘 못하는데.”

“나 은인 아니야? 말만 은인이었어?”

“아뇨, 당연히 아니죠.”

“그럼 내가 알려 주는 대로 말해.”

뭐라 속닥거림이 끝나자 청풍이 머뭇거리며 입을 열었다.

“꺼, 꺼…….”

“청 소협, 더 크게! 당신은 할 수 있어!”

진태경의 응원에 힘을 얻은 청풍이 눈을 질끈 감고 외쳤다.

“꺼져, 이 꼰대 새끼들아!”

“……!”

“……!”

꼰대? 정확히 무슨 뜻인지는 모르겠지만 그건 중요하지 않다. 뒤에 새끼라는 단어가 붙었으니까.

“이런 쳐 죽일……!”

공일혁을 포함한 세 사람이 눈을 부릅떴다.

그들이 누구인가, 종남파의 본산 제자들이다. 사람들의 선망 어린 시선에 익숙해진 그들에겐 씻을 수 없는 치욕이었다.

하지만…….

“으득, 갑시다!”

공일혁은 울분을 참으며 돌아섰다. 이 치욕을 갚아 주기에는 상대도, 장소도 좋지 않다.

‘오늘 일은 언젠가 갚는다. 반드시!’

으스러져라 움켜쥔 주먹에서는 핏방울이 떨어졌다.

거친 발걸음으로 대전을 박차고 떠나는 그의 등 뒤로 진태경과 청풍의 목소리가 따라붙었다.

“이야, 욕 잘하네. 이것도 처음이에요?”

“네, 저 욕 처음 해 봐요!”

“처음치고는 제법 소질이 있는데. 앞으로 나한테 많이 배워요. 세상 살다 보면 쓰기 싫어도 쓸 데 많다?”

“네!”
```

## Current accepted English baseline

```markdown
# Chapter 142

“Li Feng, lay disciple of Huashan, pays his respects to Martial Uncle Cheongpung.”

Zaha Divine Technique. Plum Blossom Sword Technique. And finally, the last word to come from Li Feng’s mouth:

*Martial Uncle.*

Gong Ilhyuk’s face darkened at this unbelievable turn of events.

*Then is that bastard really…?*

Even if Cheongpung wasn’t the Sword Saint’s biological grandson, one thing was certain.

That idiot who kept bowing at the waist with a bewildered expression had inherited everything from Mae Jonghak, the Sword Saint.

“This, this can’t be. It’s impossible. This makes no sense…”

As Gong Ilhyuk stammered and denied reality, a lilting voice reached his ears.

“Great Hero Gong.”

“Ah, Deputy Military Commissioner.”

Gong Ilhyuk’s expression brightened when he spotted Hong Jin.

The Zhongnan Sect had been pursuing various ventures through its connections with the government, and Hong Jin was one of the powerful men of Shanxi Province whom they had come to know in the process.

He was also the only person who could possibly extend a hand of salvation to Gong Ilhyuk in this predicament.

“What happened?”

Hong Jin’s gentle voice put Gong Ilhyuk at ease.

“I must have been mistaken for a moment.”

“Mistaken? About what?”

“I merely thought he was some fraud going around trading on the Sword Saint’s name…”

“Well, I’m no expert in martial arts, but he doesn’t look like a fraud to me.”

“There, there was only a slight misunderstanding.”

“A misunderstanding…”

Hong Jin murmured the word quietly, then stared directly at Gong Ilhyuk.

“Great Hero Gong.”

“Yes, Deputy Military Commissioner.”

“Do you know why I invited you and the others from the Zhongnan Sect here?”

“Yes. Of course I do.”

There were two reasons.

First, to become acquainted with Prince Shangshan, the City Lord of Shanxi and a member of the imperial family, and receive his approval for their new business venture.

Second, to put Hong Jin’s political rival, Li Feng, firmly in his place.

“But as you know, I’ve been rather busy lately. I was so distracted that I forgot to tell His Highness that some other guests would be arriving.”

“I see.”

The nasal quality had vanished from Hong Jin’s voice, leaving it completely dry. Gong Ilhyuk asked anxiously,

“But why are you suddenly bringing that up…?”

“I’d like you to leave for today.”

“What?”

“Wouldn’t the presence of uninvited guests make His Highness uncomfortable?”

It was an unmistakable order to leave. And on top of that, Hong Jin had called them uninvited guests.

Gong Ilhyuk protested.

“Uninvited guests? Deputy Military Commissioner, what exactly do you mean?”

“Oh my, do I have to say it twice? I mean exactly what I said before. I failed to mention your arrival to His Highness.”

Hong Jin was a eunuch. He had remained at Prince Shangshan’s side since the prince was an infant, and thanks to that, he had risen to the post of Deputy Military Commissioner, becoming the power behind the Shanxi Provincial Office and the second-ranking figure in the military.

The young prince favored him above all others. And yet he was sending guests away simply because he had failed to inform His Highness in advance?

“I, I’m not sure I understand what you’re saying, Deputy Military Commissioner…”

Hong Jin smiled sweetly at the flustered Gong Ilhyuk.

“Great Hero Gong.”

“Yes?”

“I didn’t think you were like this, but you’re a little slow, aren’t you?”

“…What?”

“Or are you just bad at reading the room?”

The sudden verbal abuse plunged the hall into silence.

Gong Ilhyuk and the other two members of the Three Hands of Zhongnan trembled as they clenched their fists.

“Your words are excessive.”

“Oh my, if that’s how you feel, then you’ve understood my intentions perfectly. I’ll admit I deliberately went a little too far.”

“Deputy Military Commissioner!”

“Lower your voice. This is the grand hall.”

“Why are you suddenly acting like this? Are you disappointed in me because of what just happened?”

“I said lower your voice. And I’m not disappointed in you, Great Hero Gong. We aren’t friends, after all. We’re not close enough to expect anything from each other or feel disappointed.”

“How could you say that? Have you forgotten your agreement with our Zhongnan Sect?”

“Agreement? Oh, you mean the one about opening a route into Shanxi Province?”

Hong Jin gave a quiet laugh and continued.

“That’s how business works. Until a deal is finalized, it can fall apart at any moment. Surely you didn’t think a few words meant everything was settled when His Highness hasn’t even given his approval yet?”

Gong Ilhyuk barely managed to suppress his rising anger.

He had already boasted to his sect as though the deal were complete.

If the venture succeeded, he would receive a suitable reward. But if it failed, he would be unable to escape a harsh reprimand. For now, he had no choice but to coax the eunuch standing before him.

“If this deal succeeds, wouldn’t it benefit you as well, Deputy Military Commissioner? The Zhongnan Sect never forgets gratitude or grudges.”

The mention of grudges alongside gratitude was an indirect threat.

It was a warning that Hong Jin risked making an enemy of one of the Nine Sects and One Gang.

Hong Jin had spent his childhood and youth as an inner palace official, watching every kind of political struggle. There was no way he could fail to understand the hidden meaning in Gong Ilhyuk’s words.

*Hmph. This is why martial artists are so hopeless.*

Hong Jin clicked his tongue inwardly.

Every one of Gong Ilhyuk’s words and actions was clumsy and blatant.

Compared to a half-polished man like Gong Ilhyuk, Li Feng—quiet, stubborn, and martial artist to the bone—was a far more troublesome opponent.

*He doesn’t even realize who holds the upper hand right now.*

If he had a goal he wanted to achieve, he should have been crawling on the ground to get it. And yet he had added a threat on top of everything else.

That helped Hong Jin make up his mind.

“Great Hero Gong. I’m a delicate person, you see. Hearing words like that frightens me too much to continue working together.”

“Ah, if there was any room for misunderstanding…”

Gong Ilhyuk was about to apologize as though he had no idea what Hong Jin meant when Jin Taekyung, who had been watching the two men with a bored expression, casually tossed out a remark.

“Room for misunderstanding, my ass. A dog passing by wouldn’t believe that.”

“You, you…!”

“Hey, Seniors from the Zhongnan Sect. I don’t know what kind of incredible business you’re running, but couldn’t you discuss it somewhere else later? I’m already miserable enough seeing the entire meal overturned.”

Hong Jin let out a quiet laugh at the sight of Taekyung licking his lips while looking at the food scattered across the floor.

“Don’t worry. Once these gentlemen leave, I’ll have new food brought in. Isn’t that right?”

The situation had now progressed to Hong Jin practically pushing them out the door.

Gong Ilhyuk gritted his teeth.

“Deputy Military Commissioner. I admit my judgment is terrible. But please think carefully about what you will gain and lose from what happened today.”

“You seem to be mistaken. I made this decision after thoroughly weighing the practical benefits.”

“What does that mean?”

“We’ll continue with the project. We’ll build a dedicated trade route and trading post connecting Shaanxi and Shanxi, and we’ll expand the scale as well.”

“Then all the more reason you should join hands with our sect!”

Hong Jin’s eyes widened at the desperate shout.

“Is the Zhongnan Sect the only sect in Shaanxi? As far as I know, there’s a place far older than the Zhongnan Sect—and one with a much better reputation among the public.”

“……Are you talking about Huashan?”

Gong Ilhyuk’s face twisted.

Huashan and the Zhongnan Sect had been bitter rivals, constantly at odds, for the past several hundred years.

If this project went to Huashan instead of some other sect, Gong Ilhyuk knew he would face far more than a light reprimand.

“How could you do this to me?”

“Of course I can. There’s a better option right in front of me.”

“Our sect is by no means inferior to Huashan. In fact, in the current generation, I can proudly say that we’ve surpassed Huashan.”

“‘I can proudly say.’ It’s good to see such loyalty to one’s sect. But from my perspective, wouldn’t the phrase ‘acknowledged by all’ sound better?”

Hong Jin continued without hesitation.

“Great Hero Gong, let me ask you directly. Does the Zhongnan Sect have a master like the Sword Saint?”

“……That is…”

“Then what about a young prodigy as outstanding as that young hero over there?”

“……”

None of the Three Hands of Zhongnan, Gong Ilhyuk included, could easily answer.

The Sword Saint?

The Zhongnan Sect’s Sect Leader, the Wind-and-Cloud Sword Lord, was occasionally compared to the Ten Kings, but that was as far as it went.

As for a monster like Cheongpung, no one had ever heard or seen anything like him.

Gong Ilhyuk, who had been the one to attack first and still ended up on his knees in a single exchange, flushed red.

“B-but the number of Peak masters belonging to our sect is by no means inferior to Huashan’s.”

“I’ve heard that the strength of a Murim sect doesn’t depend on how many masters it has, but on what kind of masters it possesses.”

Hong Jin’s single remark struck the bull’s-eye, and Gong Ilhyuk was momentarily rendered speechless.

But no matter what it took, he had to prevent the position from being handed to Huashan.

“Also, everything we’ve done in cooperation with the government has been completed successfully. Huashan, on the other hand, has never attempted anything like this. They’re inexperienced. Mistakes are inevitable.”

“Oh my, is that so?”

Hong Jin smiled and turned toward someone.

“Assistant Commissioner Li, what do you think?”

Li Feng, who had been silently observing everything, answered.

“That is true. Huashan does tend to draw a firm line between the government and Murim.”

Hong Jin frowned, and color returned to Gong Ilhyuk’s face.

But Li Feng’s heavy voice continued.

“However, doesn’t everyone have a first time?”

“Li Feng, you bastard!”

Hong Jin burst into laughter.

“Our Assistant Commissioner Li has improved so much.”

“Thanks to you.”

The two men had exchanged almost exactly the same words only a quarter of an hour earlier, but the atmosphere was now the exact opposite.

They continued their conversation in a warm and friendly atmosphere.

“I’d like you to act as our intermediary, Assistant Commissioner Li. What do you think?”

“Of course. I’ll send a messenger pigeon to my Master. The Sect Leader will be pleased to hear this news as well.”

“Ah, and you should also tell him that we have a precious guest here.”

Li Feng followed Hong Jin’s meaningful glance and smiled faintly.

“That is news our Grandmaster will be pleased to hear.”

“It’s a good start.”

“I think so too.”

Gong Ilhyuk, who had been completely excluded from the conversation, trembled from head to toe.

The situation had gone too far to turn back now.

He swept his furious, betrayed gaze across the room.

“How dare you ignore the mighty Zhongnan Sect.”

“Hey, there’s something I’ve been meaning to say.”

The voice belonged to Jin Taekyung, who had suddenly cut into the conversation. He gave a quiet laugh and continued.

“It’s not the Zhongnan Sect we ignored. It’s you. You might not know this, but I really like the Zhongnan Sect. *The Reign…* Anyway, I kept up with it all the way through volume thirty-four.”

“What kind of bullshit are you talking about? The Jin Family of Taiyuan is a family without even a proper pedigree! This is no place for the likes of you to butt in!”

Taekyung put on a wounded expression and poked Cheongpung in the side.

“Young Master Cheongpung. That old man says our family doesn’t even have a family tree.”

“What? He said that to my Benefactor?”

“Yeah. I know he’s a Senior, but isn’t that going too far? I’m too scared of the Nine Sects and One Gang to answer him myself. Could you say something for me?”

“M-me? I’m not very good at things like that.”

“Am I not your Benefactor? Was I only a Benefactor in name?”

“No, of course not.”

“Then say what I tell you.”

After Taekyung whispered something to him, Cheongpung opened his mouth hesitantly.

“G-get, get…”

“Young Master Cheongpung, louder! You can do it!”

Encouraged by Taekyung, Cheongpung squeezed his eyes shut and shouted,

“Get lost, you boomer bastards!”

“……!”

“……!”

*Boomer?* They didn’t know exactly what it meant, but that wasn’t important. It had been followed by the word *bastards*.

“You goddamn bastards…!”

All three men, Gong Ilhyuk included, glared with their eyes wide open.

Who were they?

They were main disciples of the Zhongnan Sect’s headquarters. They were accustomed to the admiring gazes of others, and this was an insult they could never wash away.

But…

Gong Ilhyuk ground his teeth. “Let’s go!”

Gong Ilhyuk turned away, swallowing his outrage.

This was neither the right place nor the right opponent for him to repay this humiliation.

*I’ll make them pay for this someday. I swear it!*

Blood dripped from the fist he clenched so tightly that his knuckles creaked.

He stormed out of the grand hall, his footsteps heavy and violent.

Behind him came the voices of Jin Taekyung and Cheongpung.

“Wow, you’re good at swearing. Was that your first time too?”

“Yes! It was my first time ever!”

“For a first attempt, you’ve got some real talent. You should learn a lot from me from now on. As you go through life, there are plenty of times you’ll need to use them even if you don’t want to.”

“Yes!”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 142`.

# Master Edit Task — Chapter 140

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
| 공일중    | **Gong Iljung**    |
| 공일혁    | **Gong Ilhyuk**    |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 종남파    | **Zhongnan Sect**                |
| 소림     | **Shaolin**                      |
| 산서오문   | **Five Gates of Shanxi**         |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 권법     | **fist technique**                               |                                                       |
| 장법     | **palm technique**                               |                                                       |
| 영약     | **elixir**                                       |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 큰형     | **eldest brother**                           |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 철혈문 | **Iron Blood Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 오호검문 | **Five Tigers Sword Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 태을미리장 | **Taeeul Miri Palm** | Palm technique taught to Cheongpung by Mae Jonghak. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |

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
| 큰형 | kinship | Eldest older brother, not a generic older brother. | |

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

#### Chapter 138 tail (verified mastered)

…
His Highness with all our hearts.” *Split a bean? True and loyal subjects?* Li Feng asked bluntly, “Then may I call you Eunuch Hong?” Eunuch Hong’s smile stiffened for a moment. With that single word, Li Feng had touched his sore spot. “That’s… a little too familiar, don’t you think?” “I only followed your instructions.” “Well, this is a surprise. I had no idea Assistant Commissioner Li considered me that close.” “I’m overwhelmed that you finally understand how I feel.” “Assistant Commissioner Li.” “Did you call, Eunuch Hong? Or would you prefer that I go back to calling you Deputy Military Commissioner?” A heavy silence settled over the hall. It was a long while before Eunuch Hong spoke again. “Our Assistant Commissioner Li has improved quite a bit, hasn’t he?” “Have I?” “Yes. Compared to a few years ago, you’ve made remarkable progress.” “I’ve learned many things thanks to you.” “I thought you were only good with a sword, but now I see you’re good with your tongue, too. I’ll have to look at you differently.” “I’m still nowhere near as skilled as a certain someone.” Their gazes collided in midair. Amid the taut silence, Eunuch Hong smiled gently. “Well, we can talk about that later… May I ask you one thing?” His opponent was no pushover, but he had taken a step back. If Li Feng kept biting at him, he would only put himself at a disadvantage. He silently nodded. “Ask.” “You said you used to belong to Huashan, didn’t you?” Li Feng paused. Huashan was a place he both missed and remembered with pain. It had been nearly ten years since he had left Mount Hua, but the memories of that time still remained deep in his body and heart. “Yes. I was a lay disciple.” “And Huashan is in Shaanxi?” He and Eunuch Hong were what one might call political enemies. For that very reason, they knew one another inside and out. Eunuch Hong was neither careless nor stupid enough to ask about such a basic fact without a reason. If anything, he was a crafty bastard with a hundred snakes writhing inside him. That only made Li Feng more puzzled. “That’s right. But why are you suddenly asking?” “I’ve come to know a few people recently, and I wondered if you might know them, too.” “Are they martial artists?” “Yes. From Shaanxi, no less.” “Don’t tell me they’re from Huashan…?” “Oh, come on. If they were, I would have told you already.” Li Feng sighed in relief. In the end, he had left of his own accord, but Huashan was still the sect he would be proud of for the rest of his life. It was a tremendous relief that Huashan had not become entangled with a sycophant like Eunuch Hong. “There are more than one or two sects in Shaanxi. And I didn’t go outside while training at the main sect, so even if I heard their names, I might not recognize them.” “Is that so? Then perhaps you would recognize them if you saw their faces?” “…?” At the sight of Li Feng’s expression, Eunuch Hong picked up the chopsticks lying on the table. “You asked earlier why I was here, didn’t you?” The beautifully crafted silver chopsticks tapped against a wine cup. *Ping.* The clear sound spread through the hall. Eunuch Hong smiled with his eyes at the bewildered Li Feng. “I invited a few acquaintances. Famous and powerful martial artists whom His Highness would enjoy meeting.” At that moment, a powerful shout rang out from beyond the iron gate. “The Three Hands of Zhongnan request an audience!” “The Three Hands of Zhongnan… The Zhongnan Sect!” Li Feng’s complexion changed drastically. Huashan and the Zhongnan Sect had been bitter rivals fighting for supremacy in Shaanxi for a full hundred years. Eunuch Hong’s intentions were every bit as clear as the smile on his face. “They’re fellow Shaanxi men, so I thought I’d arrange a gathering. You don’t mind, do you?” Just as Li Feng clenched his fists, the massive iron gate opened and three imposing men strode into the hall. One of them had a familiar face. “Well, well. If it isn’t Li Feng of Huashan?” Li Feng shuddered. The moment he saw that man’s face, the humiliating memory from ten years ago came rushing back. “How did you get here?” The sharp-eyed man answered casually. “How else? When the Deputy Military Commissioner of Shanxi Province invites you, you have to come running even if it’s a thousand li away. Isn’t that right?” “You’re too kind. I’m the one grateful that you accepted the invitation.” Li Feng ground his teeth. Gong Ilhyuk, the third of the Three Hands of Zhongnan, grinned at him. “Anyway, you’ve done well for yourself. Assistant Military Commissioner, someone like you… Huashan must have spread around quite a few silver nyang for you. Hmm?” “How dare you insult Huashan?” “Insult Huashan? You’re the one who insulted it. Ten years ago, who was it that fell to his knees after only a hundred or so exchanges with that magnificent Huashan martial arts?” “You bastard!” A thunderous shout burst from Li Feng’s mouth. At the moment he glared at Gong Ilhyuk with eyes that seemed to pour out streams of flame, a third shout rang out from beyond the iron gate. “The young prodigies of Shanxi Murim request an audience!”

#### Chapter 139 tail (verified mastered)

…
Cheongpung blinked his clear eyes. “Why?” “…Young Master Jin. Do we really have to take this bastard—I mean, this person—with us?” “I don’t mind leaving him out. But are you sure you’ll be all right?” The official fell silent for a moment. If he took five people without Cheongpung, he would be reprimanded by his superiors and lose his job. But if Cheongpung let his tongue slip just once, he might lose his head. A moment later, when he spoke again, his face looked ten years older. “…Let’s just go.” Cheongpung beamed. “Thank you. If there’s time, I’ll put in a good word with the king—I mean, His Highness.” “Please, just keep that gentleman’s mouth shut.” While the official rattled off every precaution we needed to take, along with his earnest pleas, we finally reached the iron gate. The gate was enormous and incredibly thick. Quiet voices drifted from behind it. *Assistant Military Commissioner, Huashan, insult?* Those fragments alone gave me no clue what they were discussing. Still… *The atmosphere doesn’t seem very good.* I had a feeling this wasn’t the best place for people to sit across from one another over a meal. At that moment, a man standing at attention before the gate shouted loudly, “The young prodigies of Shanxi Murim request an audience!” *Groooan.* The iron gate began to open at the same time. The official gave me one final warning with a worried expression, stealing a sidelong glance at Cheongpung. “Please just keep that man’s mouth shut.” “…Ah. Yes.” He must have been seriously worried. * * * The moment we entered, it felt as though my eyes had brightened. The lavishly decorated grand hall was filled with a long table like the ones I had only seen in movies set in magic schools, along with all kinds of food. And the moment I saw the five people who had arrived ahead of us, only one thought crossed my mind. *We’re screwed.* When it came to reading the room, I was second to none. After scraping by as an F-rank Hunter for so long, always watching everyone’s mood, I could size up an atmosphere in 0.1 seconds. Like right now. *What a wonderful atmosphere.* The air around the five people was pulled taut. I had sensed something was wrong from outside, but it was even worse than I had expected. It was fortunate everyone was empty-handed given the occasion. If they’d had anything hanging from their waists, swords would already have been drawn. “Well… Now that our guests have arrived, shall we end this reunion here?” A man’s delicate voice broke the tension. Though was he really a man? He was slender enough to seem like a woman, with a pale face and lips as red as though they had been painted with dye. > **System** > > Level 22: Hong Jin He smiled at me. “What a strikingly handsome young man, just as one would expect of a young prodigy of the martial world. I heard a young hero from the Jin Family of Taiyuan would be joining us today. Might that be you…?” Now was the time for introductions. I performed a fist-and-palm salute toward the five men. “My name is Jin Taekyung of the Jin Family of Taiyuan.” The unpleasant atmosphere immediately eased somewhat. Surprise painted over the traces of displeasure and ridicule lingering on the other four faces. “If you’re Jin Taekyung of the Jin Family of Taiyuan…” A huge man dressed in black martial robes muttered. From the moment I first saw him, he had radiated tough-guy energy. His name was Li Feng, and the number 68 hovered above his head. *Is he affiliated with the military?* I couldn’t judge everything from a first meeting, but that was the impression he gave. A proud and upright soldier. That was my first impression of him. *Li Feng, Li Feng… At Level 68, he’s probably an advanced First Rate?* Just as I was engraving his name and Level into my mind, the other three men reacted. “Hm. That’s the Sleeping Dragon of Shanxi?” “He’s young. No, he’s a child.” “He doesn’t particularly look as impressive as the rumors claim…” Their curious gazes held surprise, a hint of jealousy, and a subtle sense of superiority. In situations like this, there was usually no need to ask about the other person’s identity. They were the sort of people desperate to show off. “Apologies for the late introduction, Junior.” A sharp-eyed man grinned as he spoke to me. The other two stood with their arms folded, looking at me like I was a cute little chick. *This is weirdly irritating.* Who the hell were they to act like my Seniors right off the bat? My question was answered soon enough. “Oh, you don’t know yet, do you? We came from Shaanxi. The Zhongnan Sect of Shaanxi—have you heard of it?” My mouth fell open before I knew it. “Th-the Zhongnan Sect? *That* Zhongnan Sect?” The three men’s faces blossomed with smiles. “Haha! Look how surprised he is.” “Exactly.” “Perhaps you know our sect well?” I shouted, suddenly brimming with excitement. “I do! I know it very well! I had so much fun reading about it!” “We’re glad to hear you know us… Wait. What do you mean, ‘reading about it’?” “What else? Obviously, *The Reign…*” I stopped halfway through my answer. *Ah. This wasn’t a novel.*

## Korean source

```text
＃140화



종남삼수(終南三手) 공일혁은 떨떠름한 표정으로 눈앞의 청년을 바라봤다.

‘뭐지, 이놈은?’

산서잠룡 진태경. 불과 몇 달 만에 섬서성까지 슬금슬금 이름을 알리고 있는 돌풍의 주역이다.

공일혁은 속으로 진태경이 했던 말을 곱씹었다.

‘군림…… 뭐라고?’

분명히 무슨 말을 하려다 말았던 것 같은데.

처음 종남파의 이름을 들었을 때 보여 줬던 열광적인 반응과 달리, 놈은 지금 김이 팍 샌 얼굴로 한숨만 푹푹 내쉬고 있었다.

“휴우.”

“……웬 한숨인가?”

“아닙니다. 아무것도 아니에요.”

“아니긴 뭐가 아닌가? 그러지 말고 마저 말해 보게.”

공일혁은 슬슬 기분이 나빠지기 시작했다. 자신의 사문이 어떤 곳인가, 바로 그 유명한 종남파(終南派)다.

수백 년의 역사와 뿌리 깊은 무맥을 바탕으로 당당히 구파일방(九派一幇)에 이름을 올린 무림의 거목 중 하나란 말이다.

그런데…….

‘알아봐 주는 것에 감사하지는 못할망정 한숨을 내쉬어?’

태원진가가 아무리 잘나가 봐야 아직은 변방의 일개 가문에 불과하다.

구파일방인 종남파와 비교하면 태양 앞의 반딧불 같은 존재. 출신 배경으로나, 개인의 명성으로나 까마득한 애송이 녀석이다.

‘시건방진 놈.’

종남파의 제자라는 자부심으로 평생을 살아 온 그다. 기분이 나쁜 것도 당연했다.

공일혁과 함께 종남삼수로 불리는 다른 두 사람 역시 진태경을 보는 시선이 곱지 않았다.

“크흠.”

“젊은 친구가 말을 하다가 마는 버릇이 있군.”

분위기가 영 텁텁해지자 진태경이 손을 내저었다.

“아뇨, 그런 게 아니고요. 그냥 혼자 착각했던 것뿐입니다.”

공일혁이 애써 너그러운 말투로 입을 열었다.

“무슨 착각? 말해 보게. 내 다 대답해 줄 터이니.”

“진짜 별거 아닌데…….”

“아, 말해 보라고!”

“엥, 왜 소리를 지르고 그러세요?”

공일혁은 호흡을 가다듬었다.

내일모레면 그의 나이 불혹이다. 그런데 이제 겨우 약관밖에 안 된 어린놈에게 이렇게 흥분하다니.

이상하게 저놈의 잘생긴 얼굴을 보고 있으면 약이 오르는 기분이다.

“그게 아니고…… 후우, 어쨌든 말해 보게.”

“으음.”

진태경이 어쩔 수 없다는 듯이 입을 열었다.

“그럼 하나만 여쭤봐도 되겠습니까?”

“뭐든지.”

“지금 종남파 회장님, 아니 장문인 존함이 어떻게 되시는지?”

“응? 장문인의 존함 말인가?”

“네.”

이게 무슨 뜬금없는 질문이란 말인가? 공일혁은 의아함을 느끼며 대답했다.

“공씨 성에 일 자, 중 자 쓰시네.”

“아아, 네.”

마치 그게 누구냐는 듯 심드렁한 대답이다. 공일혁을 포함한 세 사람의 이마에 핏대가 섰다.

“장문인의 존함을 들어 본 적 없나?”

진태경이 뒤통수를 긁적였다.

“글쎄요, 들어 본 것 같기도 하고. 아닌 것 같기도 하고…….”

“……그, 그럼 풍운검군(風雲劍君)이라는 별호는?”

“풍운검군 공일중, 풍운검군 공일중…… 쓰읍, 잘 모르겠는데요.”

기가 찰 노릇이다. 구파일방, 오대세가의 장문인과 가주들은 모두 천하에 이름이 쟁쟁한 고수들. 무림인이라면 모를 수 없는 존재다.

하물며 얼뜨기 무인도 아니고 태원진가의 자제라는 놈이 종남파 장문인을 모르다니.

심지어 제 친구라도 되는 마냥 이름을 불러 댄다.

‘이놈이 지금 종남파를 우롱하는 건가?’

공일혁이 충격으로 머리가 띵해 있는데, 문득 진태경이 고개를 들어 그를 바라봤다.

“어? 그러고 보니 이름이 비슷하시네요. 공일중, 공일혁.”

그나마 최소한의 눈치는 있는 놈이군. 공일혁의 심기가 살짝 누그러졌다.

“집안 어른이시네.”

“오, 집안 어른! 그럼 혹시 관계가…….”

“오촌 당숙 되시지.”

“오촌 당숙!”

눈이 휘둥그레진 진태경을 보자 공일혁의 어깨에 힘이 들어갔다.

다른 사람도 아니고 풍운검군이다. 종남파의 장문인과 한집안 사람이라는 건 엄청난 영광 아닌가.

“크흠, 너무 소문내지는 말아 주게. 아무래도 이 사실이 널리 알려지면 사람들이 날 대하는 태도가 달라질 테니 말일세.”

실제론 이 사실이 누구보다 알려지길 원하는 건 공일혁 본인이다.

그는 지금까지 풍운검군의 이름을 앞세워 온갖 혜택을 누려 왔다. 뛰어난 무공과 영약, 그리고 종남삼수라는 별호까지.

이대로만 승승장구를 거듭한다면 종남파의 요직을 꿰차는 것도 시간문제였다.

“내 말, 잘 알아들었지? 정 말하고 싶다면 가까운 벗 몇 명한테만…….”

진태경이 손을 내저었다.

“에이, 절대 말 안 합니다. 공 대협 평판에 누가 될 게 뻔한데. 연줄 믿고 여기까지 올라온 놈, 어이쿠. 죄송합니다. 어쨌든 그런 식으로 소문나면 곤란하잖아요.”

공일혁은 헛기침을 내뱉었다. 스스로 생각하기에도 아주 틀린 얘기는 아니었기 때문이다.

“크흠. 딱히 누가 될 것까지야 있겠나. 내 말은, 혹 나에 대해 궁금해하는 사람이 있을 수 있으니…….”

“궁금해하는 사람이요? 저 친구 한 명도 없어서 딱히 말해 줄 사람이 없는데.”

“……자네 큰형님인 진 소가주나, 아니면 진천검 소협이 궁금해할 수도 있지 않겠나?”

“아, 저희 가문 사정 잘 모르시는구나. 큰형님 지금 엄청 바빠요. 둘째 형은 무공 아니면 별 관심도 없고.”

“……그래?”

“예.”

그렇다는데 더 할 말도 없다. 언짢은 헛기침만 연발하는 그를 보며 진태경이 해맑게 웃었다.

“그리고 그거 말해 봤자 뭐해요. 오촌 당숙이면 거의 남이나 다름없는데. 저는 또 무슨 부자지간이라도 되시는 줄.”

“……!”



* * *



역시 웃는 얼굴로 엿 먹이는 게 세상에서 제일 짜릿하다.

특히 거만 떠는 놈들한테는 제대로 먹이기만 하면 쾌감은 두 배가 된다.

‘아, 중독될 것 같아.’

종남삼수라고 했나?

처음부터 마음에 안 들었던 놈들이다. 위에서 내려다보는 듯한 눈빛도, 대문파랍시고 거들먹거리는 태도도.

‘역시 소설이랑은 다르네.’

고등학교 다닐 때는 종남파 제자가 되는 게 꿈이었는데, 역시 현실은 시궁창이다.

나는 주먹을 부르르 떠는 공일혁을 보며 새어 나오는 웃음을 참았다.

‘귀여운 자식, 놀리는 맛이 쏠쏠하네.’

더 놀려 주고 싶지만 이쯤 해 둬야 한다. 태원진가가 지역구라면 저쪽은 전국구. 시비 붙어서 좋을 게 없으니까.

다행히 불쑥 끼어든 목소리가 분위기를 환기시켰다.

“너무 그쪽 분들만 대화하시는 거 아니에요? 다른 분들 외로우시겠다. 아직 소개도 다 못 했는데.”

콧소리가 듬뿍 들어간 간드러진 목소리에 한 번.

나를 보며 찡긋 웃는 미중년의 모습에 두 번 소름이 돋는다.

“아직 내 소개를 못 했죠? 산서성 도지휘동지, 홍진이라고 해요.”

“도지휘……뭐요?”

“도지휘동지요. 아, 무림인이시라 이런 직책은 처음 들어 보시는구나?”

“네.”

위원장 동지는 들어 봤어도 도지휘동지는 처음 들어 보네.

눈만 껌뻑이는 나를 보며 홍진이 까르르 웃었다. 세상에, 중년 남성이 까르르 웃다니.

“표정이 왜 그래요? 무슨 안 좋은 일이라도?”

“……아뇨. 너무 행복해서.”

“행복? 호호호, 너무 귀여우시다. 안 그래요, 이 첨사?”

귀엽대 시발, 저 새끼가 나한테 귀엽대.

간신히 구역질을 참고 있는데 앞서 스치듯이 본 이풍이라는 사내가 무뚝뚝하게 인사를 건넸다.

“산서성 도지휘첨사 이풍이오. 산서성부 소속 군사들의 훈련을 맡고 있지.”

“그리고 내 직속 부하죠. 그렇지 않나요, 이 첨사?”

순간 이풍의 굵은 눈썹이 꿈틀거렸다. 만난 지 5분도 안 됐지만 하나는 알겠다.

이풍이 홍진을 싫어한다는 것.

그거 하나만으로도 예의를 갖출 만한 상대다. 나는 공손히 포권을 취했다.

“태원진가의 진태경이라고 합니다.”

“위명은 익히 들었소. 산서 무림에 큰 신성이 떠올랐다고.”

“신성이라뇨, 과찬의 말씀이십니다.”

이풍이 진지한 얼굴로 고개를 저었다.

“아니오. 소문이라는 것이 왕왕 과장되기 마련인데, 내 오늘 진 소협을 보니 모두 사실임을 알겠소.”

오는 말이 고우면 가는 말도 고운 법.

나도 오는 길에 봤던 군사들 이야기를 꺼냈다.

“저야말로 군사들 수준이 상당히 뛰어나서 깜짝 놀랐습니다. 어떤 분이 훈련시켰는지 궁금했는데…… 역시는 역시네요.”

엄지를 척 치켜세워 주자 이풍의 입가에 웃음이 스친다.

이런 정상적이고 훈훈한 대화가 얼마 만인지, 감개가 무량할 지경이다.

“결례가 안 된다면 다른 분들도 소개해 주시겠소?”

“어이구, 그럼요. 이쪽은…….”

“안녕하십니까! 존경하는 무림의 선배님들과 불철주야 나라를 위해 힘쓰시는…….”

“…….”

대기업 면접이야, 뭐야.

호시탐탐 기회만 엿보고 있던 산서오문의 후기지수들이 앞다투어 과장된 자기소개와 아부를 한바탕 쏟아 내자 남은 한 사람에게 시선이 쏠렸다.

“그래, 거기 계신 후배님은 어디에서 온 누구신가?”

한껏 선배뽕에 취한 공일혁의 질문에 청풍이 눈을 깜빡였다.

“저요?”

“그럼 자네 말고 누가 있나?”

“하나, 둘, 셋, 넷…… 저 말고도 많은데요.”

공일혁의 이마에 핏대가 섰다.

“그거 말고! 아직 소개 안 한 건 자네뿐이잖아!”

“아하, 그렇군요. 후배라고 하시기에 제가 아닌 줄 알았어요.”

“어허, 원래 무림은 동도! 다 선후배지간인 걸 왜 모르는가!”

나 같았으면 잔뜩 비꼬았겠지만, 청풍은 역시 청풍.

일반인과는 클라스가 다르다.

“우와, 저 후배 처음 해 봐요! 잘 부탁드립니다!”

“……아니, 뭐 이런 놈이.”

가끔은 적당히 때 묻은 어른들보다 순수한 어린아이가 훨씬 대하기 어렵다. 청풍이 해맑은 웃음과 함께 입을 열었다.

“저는 산서에 살고 있는 청풍이라고 합니다.”

말문이 막혔던 공일혁이 그제야 정신을 차리고 더듬더듬 물었다.

“커, 커험. 그럼 자네도 산서오문의 후기지수겠군.”

“어? 아닌데요?”

“아니라고?”

“네. 전 하남에서 왔는데.”

“방금은 산서 사람이라며?”

“산서에 살고 있으니 산서 사람이지요. 헤헤.”

“그…… 후우우.”

공일혁의 이마에 골이 패었다. 당장이라도 주먹을 휘두르고 싶은데, 자리가 자리인 만큼 참는 기색이 역력했다.

“좋아, 그럼 하남 어느 문파 출신인가? 철혈문? 오호검문?”

“거기가 어디예요?”

“하남 출신이라면서 철혈문과 오호검문을 모르는 게 말이 되나? 응? 그럼 자네가 소림사 출신이라도 돼?”

“아, 하남에서는 보름 정도 머무르다가 산서로 넘어와서 잘 모릅니다.”

“하남 출신이라며?”

“하남에서 온 건 맞는데, 그전에는 섬서에…….”

“야, 이 새끼야! 차라리 그냥 천하가 네 고향이라고 해라!”

결국 폭발한 공일혁이 고함과 함께 청풍의 멱살을 붙잡았다. 아니, 붙잡으려던 찰나였다.

덥석.

너무나 간단하게 잡혀 버린 손목. 공일혁이 헛웃음을 흘렸다.

“허, 이놈 봐라. 한 수 재간은 있다, 이거지?”

“어어, 본능적으로 그만. 죄송합니다, 선배님.”

“본능적으로? 죄송해?”

울상이 된 얼굴로 사과하는 청풍을 보며 공일혁이 피식 웃었다.

“아니다. 놓을 것 없다. 사과할 것도 없고.”

“정말요?”

“그래, 그 대신 만용의 대가는 톡톡히 치러야겠지?”

“예? 그게 무슨.”

“이제부터 알게 될 거다.”

내가 끼어든 것은 바로 그 순간이었다. 몸을 날려 청풍의 앞을 막아선 나를, 공일혁이 건조한 눈빛으로 응시했다.

“비키시게, 후배님.”

“잠시 실례하겠습니다. 선배님.”

“실례라…… 본문의 행사에 태원진가가 반하겠다는 뜻으로 받아들이면 되겠나?”

나는 태연하게 대답했다.

“천만에요. 그저 문제가 커지는 걸 막고 싶을 뿐입니다.”

“문제? 무슨 문제?”

“곧 전하께서 오시지 않습니까? 여긴 보는 눈도 많고요.”

“보는 눈이라. 도지휘동지, 어떻게 생각하십니까?”

공일혁의 등 뒤로 빙긋 웃는 홍진의 얼굴이 보였다. 간드러진 목소리가 뒤를 잇는다.

“글쎄요, 제 생각엔 별문제 없을 것 같은데요?”

이풍이 즉시 반발했다.

“이곳은 대전입니다. 작은 소동도 용납할 수 없습니다.”

“이 첨사, 용납이라는 말은 듣기 거북하네? 누가 들으면 내 상관이라도 되는 줄 알겠어.”

“도지휘동지!”

“왜요, 도지휘첨사?”

홍진의 말이 떨어지기가 무섭게 종남삼수에 속한 다른 두 명이 슬그머니 이풍의 앞을 막아선다.

종남파라는 이름답게 각각 최소 초일류의 고수들. 이풍은 입술을 질끈 깨물더니 나를 보며 중얼거렸다.

“미안하오.”

공일혁이 득의양양하게 웃었다.

“자, 이제 어쩔 텐가?”

어쩌긴 뭘 어째. 어깨를 한번 으쓱하고 물러나자 공일혁의 웃음이 진해졌다.

“현명한 선택이야.”

“저는 문제가 커지는 걸 막고 싶었을 뿐입니다. 아시죠?”

“알다마다. 여기 있는 모두가 똑똑히 기억할 걸세.”

“그랬으면 좋겠네요.”

청풍은 멀뚱멀뚱 나를 쳐다봤다.

“은인, 혹시 제가 뭘 잘못했나요?”

내 대답보다 공일혁이 한발 빨랐다.

“뭐라? 잘못?”

찢어 죽일 듯한 눈빛이 청풍을 향했다.

“네가 지금 나와 종남파를 능멸하는 것이냐?”

“그게 아니고요. 저는 그저…….”

“그 입 닥치지 못할까!”

청풍의 얼굴 위로 복잡 미묘한 감정이 떠올랐다. 그리고 공혁일의 이성을 잃게 만들기에 충분한 한마디가 이어졌다.

“와, 저 누구한테 욕먹는 거 처음이에요. 신기하다.”

“이런 쳐 죽일……!”

후웅!

묵직한 파공성. 공혁일의 일권(一拳)이 눈부신 속도로 청풍의 옆구리를 향해 쏘아진 다음 순간이었다.

퍽, 우두둑.

“……!”

“……!”

소리 없는 경악 속, 한 사람이 고통으로 입을 딱 벌렸다.

으스러진 주먹과 팔뚝 살을 찢고 뛰어나온 뼈, 피투성이가 된 공혁일이 떨리는 목소리로 물었다.

“이, 이게 무슨. 도대체 어떤 권법…….”

그가 아니었다면 내가 물어봤을 거다. 이미 예상한 결과이기는 했지만, 이 정도일 줄이야.

청풍은 단 한 번 맞받아치는 것만으로 70레벨이 넘는 공일혁을 저항 불능으로 만들어 버렸다.

그리고…….

“권법이 아니었어.”

내 중얼거림에 청풍이 금방이라도 토할 것 같은 얼굴로 대답했다.

“은인 말씀이 맞아요. 권법이 아니라 태을미리장(太乙迷離掌)이라는 장법이에요. 그런데 선배님, 피가 너무 나요. 피 냄새 때문에 속 울렁거려요. 우욱!”

이런 미친놈.

공일혁을 내팽개치고 헛구역질을 시작하는 녀석을 보며 헛웃음을 흘리던 그때였다.

“태, 태을미리장!”

이풍이 부릅뜬 눈으로 물었다.

“지금 태을미리장이라고 했소? 정말 틀림없소?”

“우욱, 네. 저희 할아버지께서 가르쳐 주셨어요.”

“호, 혹시 그분의 존함을 여쭤봐도 되겠소?”

“우욱, 매종학, 우웨에에엑!”

촤아아악!

나는 청풍이 곧 왕이 도착할 자리에 토를 했다는 사실에 놀랐지만, 이풍은 아닌 듯했다.

벼락을 맞은 것처럼 부들부들 떨던 그가 목소리를 쥐어짜 냈다.

“검성……!”
```

## Current accepted English baseline

```markdown
# Chapter 140

Gong Ilhyuk of the Three Hands of Zhongnan stared at the young man in front of him with a dubious expression.

*What is this guy?*

Jin Taekyung, the Sleeping Dragon of Shanxi. He was the driving force behind a whirlwind that had quietly spread his name as far as Shaanxi in the span of only a few months.

Gong Ilhyuk mulled over what Jin Taekyung had said.

*“The Reign…” What was it?*

It definitely seemed as though he had been about to say something before stopping himself.

Unlike his enthusiastic reaction when he first heard the name of the Zhongnan Sect, he now looked completely deflated and let out one deep sigh after another.

“Whew.”

“…What’s with the sighing?”

“It’s nothing. Really.”

“What do you mean, nothing? Go on and finish what you were saying.”

Gong Ilhyuk was beginning to feel irritated. What kind of sect was his? It was none other than the famous Zhongnan Sect.

It was one of the great pillars of Murim, a sect that had proudly earned its place among the Nine Sects and One Gang on the strength of centuries of history and deeply rooted martial traditions.

And yet…

*Can’t he at least be grateful that I acknowledged him? Why is he sighing?*

No matter how successful the Jin Family of Taiyuan was, it was still merely a family from the frontier.

Compared to the Zhongnan Sect, one of the Nine Sects and One Gang, it was like a firefly before the sun. In terms of both background and personal fame, Jin Taekyung was a hopelessly insignificant greenhorn.

*What an arrogant bastard.*

Gong Ilhyuk had lived his entire life with pride in being a disciple of the Zhongnan Sect. It was only natural that he felt offended.

The other two men known alongside him as the Three Hands of Zhongnan were also looking at Jin Taekyung with displeasure.

“Ahem.”

“Young friend, you have a habit of stopping halfway when you speak.”

As the atmosphere grew increasingly unpleasant, Jin Taekyung waved his hand.

“No, it’s not like that. I just misunderstood something on my own.”

Gong Ilhyuk opened his mouth, deliberately adopting a generous tone.

“What did you misunderstand? Tell me. I’ll answer everything.”

“It’s really nothing…”

“Ah, just tell me!”

“Why are you shouting?”

Gong Ilhyuk took a deep breath.

He was almost forty years old. Yet here he was, getting worked up over a brat barely twenty.

For some reason, looking at that handsome face made his blood boil.

“It’s not that… Whew. Anyway, tell me.”

“Hmm.”

Jin Taekyung finally opened his mouth, as though he had no choice.

“Then may I ask you one thing?”

“Anything.”

“What is the name of the current chairman of the Zhongnan Sect—or rather, the Sect Leader?”

“Hm? You mean the Sect Leader’s name?”

“Yes.”

What kind of question was that? Gong Ilhyuk answered with a puzzled look.

“Gong Iljung.”

“Ah. Yes.”

Jin Taekyung’s response was so indifferent that it was as though he had no idea who that was.

The veins on the foreheads of all three men began to bulge.

“Have you never heard the Sect Leader’s name?”

Jin Taekyung scratched the back of his head.

“I think I have. Or maybe not…”

“…Then what about the title Wind-and-Cloud Sword Lord?”

“Wind-and-Cloud Sword Lord Gong Iljung. Wind-and-Cloud Sword Lord Gong Iljung… Hmm. I’m not sure.”

It was beyond absurd.

The Sect Leaders and Family Heads of the Nine Sects and One Gang and the Five Great Families were all renowned masters whose names were known throughout the world. No martial artist could possibly be unaware of them.

And yet this fellow, who was supposedly a member of the Jin Family of Taiyuan—not some half-baked martial artist—didn’t know the Sect Leader of the Zhongnan Sect.

He even called him by his given name, as though they were friends.

*Is this bastard making a mockery of the Zhongnan Sect?*

Gong Ilhyuk’s head was spinning from the shock when Jin Taekyung suddenly looked up at him.

“Oh? Now that I think about it, your names are similar. Gong Iljung, Gong Ilhyuk.”

At least he had some basic social awareness. Gong Ilhyuk’s irritation eased slightly.

“He’s a family elder.”

“Oh, a family elder! Then are you two…?”

“He’s my father’s cousin.”

“Your father’s cousin!”

Seeing Jin Taekyung’s eyes widen, Gong Ilhyuk straightened his shoulders.

It wasn’t just anyone. He was the Wind-and-Cloud Sword Lord. Being related to the Sect Leader of the Zhongnan Sect was an immense honor.

“Ahem. Don’t spread it around too much. If this became widely known, people’s attitudes toward me would change.”

In reality, Gong Ilhyuk wanted this fact to become known more than anyone.

He had enjoyed all kinds of benefits by putting the Wind-and-Cloud Sword Lord’s name out front: superior martial arts, elixirs, and even the title of Three Hands of Zhongnan.

If he continued advancing at this rate, it was only a matter of time before he seized an important position within the Zhongnan Sect.

“You understand what I mean, right? If you absolutely have to tell someone, just tell a few close friends…”

Jin Taekyung waved his hand.

“No way. I’d never tell anyone. It would obviously hurt Great Hero Gong’s reputation. People would say, ‘He’s a guy who climbed this high by relying on connections.’ Oops. Sorry. Anyway, that kind of rumor would be troublesome, wouldn’t it?”

Gong Ilhyuk gave a dry cough. Even he had to admit that the boy wasn’t entirely wrong.

“Ahem. It’s not as though it would hurt me that much. I only meant that there might be people who are curious about me…”

“People curious about you? I don’t have a single friend, so there’s no one I could tell.”

“…Your eldest brother, the Lesser Family Head of the Jin Family, might be curious. Or Young Hero Heaven Shaking Sword.”

“Oh, you don’t know much about my family situation. My eldest brother is incredibly busy right now. My second brother isn’t interested in much besides martial arts.”

“…Really?”

“Yes.”

There was nothing more to say after that.

As Gong Ilhyuk continued giving irritated coughs, Jin Taekyung smiled brightly.

“And what good would it do to tell anyone? If he’s only your father’s cousin, you’re practically strangers. I thought you two were father and son or something.”

“……!”

* * *

There was nothing more exhilarating than screwing someone over while smiling.

Especially when it was someone who acted arrogant. If I managed to get one over on them properly, the rush doubled.

*Ah. I think I could get addicted to this.*

Were they called the Three Hands of Zhongnan?

I hadn’t liked them from the moment I met them. Not their gazes, which seemed to look down on everyone, nor their swaggering attitude as members of a great sect.

*So it really is different from the novel.*

When I was in high school, becoming a disciple of the Zhongnan Sect had been one of my dreams.

As expected, reality was a cesspool.

I held back my laughter as I watched Gong Ilhyuk trembling with rage.

*What a cute bastard. He’s so much fun to tease.*

I wanted to keep going, but this was probably enough. If the Jin Family of Taiyuan was a local player, these people were national-level.

There was nothing to gain from picking a fight with them.

Fortunately, a voice suddenly cut in and lightened the atmosphere.

“Aren’t you gentlemen monopolizing the conversation a little? The other guests must be lonely. You haven’t even finished introducing yourselves.”

I got goose bumps once at the nasal, lilting voice.

Then I got them a second time when the pretty middle-aged man looked at me and winked.

“I haven’t introduced myself yet, have I? I’m Hong Jin, the Deputy Military Commissioner of Shanxi Province.”

“Deputy Military Commissioner… what?”

“The Deputy Military Commissioner. Ah, you’re a martial artist, so I suppose this is your first time hearing of the office?”

“Yes.”

*I’d heard of “Comrade Chairman,” but “Comrade Deputy Military Commissioner” was a new one.*

Hong Jin giggled as he looked at me blinking.

Good heavens. A middle-aged man was giggling.

“Why that expression? Did something bad happen?”

“…No. I’m just so happy.”

“Happy? Ho ho ho, you’re adorable. Don’t you agree, Assistant Commissioner Li?”

*He called me cute. Fuck, that bastard called me cute.*

I was barely holding back my nausea when the man I had seen only briefly earlier greeted me in a blunt voice.

“I am Li Feng, Assistant Military Commissioner of Shanxi Province. I oversee the training of the soldiers under the Shanxi Provincial Office.”

“And he’s my direct subordinate. Isn’t that right, Assistant Commissioner Li?”

Li Feng’s thick eyebrow twitched.

We had known each other for less than five minutes, but I already knew one thing.

Li Feng hated Hong Jin.

That alone made him someone worth treating with courtesy. I performed a fist-and-palm salute.

“My name is Jin Taekyung of the Jin Family of Taiyuan.”

“I have heard your reputation. A great new star has risen over the Shanxi martial world.”

“A new star? You flatter me.”

Li Feng shook his head with a serious expression.

“No. Rumors are often exaggerated, but after seeing Young Hero Jin today, I can tell they were all true.”

Kind words deserved kind words in return.

I brought up the soldiers I had seen on the way here.

“I was surprised by how skilled the soldiers were. I wondered who had trained them, but I suppose it was only natural that it would be you.”

I gave him a firm thumbs-up, and a smile flickered across Li Feng’s lips.

It had been so long since I’d had a normal, pleasant conversation that I was almost moved.

“If it isn’t discourteous, could you introduce the other guests as well?”

“Of course. This is…”

“Greetings! To the respected Seniors of Murim and those who toil day and night for the sake of the nation…”

“……”

What was this, an interview at a conglomerate?

The young prodigies of the Five Gates of Shanxi, who had been waiting for an opportunity, rushed to give exaggerated introductions and shower everyone with flattery.

That left only one person.

“All right. Junior, where are you from, and who are you?”

At Gong Ilhyuk’s question, delivered with all the smugness of someone high on his seniority, Cheongpung blinked.

“Me?”

“Who else would I mean?”

“One, two, three, four… There are lots of people besides me.”

The veins on Gong Ilhyuk’s forehead bulged.

“Not that! You’re the only one who hasn’t introduced himself!”

“Oh, I see. You called me a junior, so I didn’t think you meant me.”

“Good heavens! In Murim, we’re all fellow practitioners! We’re all seniors and juniors to one another. How do you not know that?”

If it were me, I would have responded with heavy sarcasm.

But Cheongpung was Cheongpung.

He was in a different class from ordinary people.

“Wow, this is my first time being a junior! I look forward to working with you!”

“…What kind of person is this?”

Sometimes, a pure child was much harder to deal with than an adult who had been properly tainted by the world.

Cheongpung spoke with a bright smile.

“My name is Cheongpung, and I live in Shanxi.”

Gong Ilhyuk had been left speechless, but he finally came to his senses and stammered out a question.

“Ahem. Then you must also be one of the young prodigies of the Five Gates of Shanxi.”

“Hm? No.”

“You’re not?”

“No. I came from Henan.”

“You just said you were from Shanxi.”

“I live in Shanxi, so I’m from Shanxi. Hehe.”

“Then… whew.”

A furrow appeared in Gong Ilhyuk’s forehead.

He clearly wanted to throw a punch right then and there, but the occasion forced him to hold himself back.

“All right, then. Which sect in Henan are you from? The Iron Blood Sect? The Five Tigers Sword Sect?”

“Where are those?”

“You’re from Henan, but you don’t know the Iron Blood Sect or the Five Tigers Sword Sect? Does that make any sense? Hm? Then are you from Shaolin?”

“Oh, I stayed in Henan for about half a month before moving to Shanxi, so I don’t know much about it.”

“You said you were from Henan?”

“It’s true that I came from Henan, but before that I was in Shaanxi…”

“You little bastard! Then just say the whole world is your hometown!”

At last, Gong Ilhyuk exploded. He shouted as he grabbed Cheongpung by the collar—or tried to.

Snag.

His wrist was caught with absurd ease.

Gong Ilhyuk let out a hollow laugh.

“Well, look at you. You know at least one trick, huh?”

“Ah, I just reacted on instinct. I’m sorry, Senior.”

“On instinct? And you’re apologizing?”

Seeing Cheongpung apologize with a miserable expression, Gong Ilhyuk gave a short laugh.

“Never mind. You don’t have to let go. There’s no need to apologize, either.”

“Really?”

“Yes. But you’ll pay dearly for your reckless bravado.”

“What? What does that mean?”

“You’ll find out soon enough.”

I stepped in at that exact moment.

I threw myself in front of Cheongpung, and Gong Ilhyuk looked at me with dry eyes.

“Move aside, Junior.”

“Pardon me, Senior.”

“Pardon you… Should I take this to mean the Jin Family of Taiyuan intends to oppose the actions of our sect?”

I answered calmly.

“Not at all. I only want to prevent this from becoming a bigger problem.”

“A problem? What problem?”

“His Highness will be arriving soon, won’t he? And there are plenty of eyes on us.”

“Plenty of eyes. Deputy Military Commissioner, what do you think?”

I could see Hong Jin smiling behind Gong Ilhyuk.

His delicate voice followed.

“Well, I don’t think it will be much of a problem.”

Li Feng immediately objected.

“This is the grand hall. We cannot tolerate even a minor disturbance.”

“Assistant Commissioner Li, I find the word ‘tolerate’ unpleasant. Anyone listening might think you were my superior.”

“Deputy Military Commissioner!”

“Why, Assistant Military Commissioner?”

The instant Hong Jin finished speaking, the other two members of the Three Hands of Zhongnan quietly stepped in front of Li Feng.

As befitted members of the Zhongnan Sect, both were at least advanced First Rate masters.

Li Feng bit down hard on his lip, then muttered to me,

“I’m sorry.”

Gong Ilhyuk smiled triumphantly.

“Well? What are you going to do now?”

What was I supposed to do?

I shrugged once and stepped back. Gong Ilhyuk’s smile deepened.

“A wise choice.”

“I only wanted to prevent the problem from getting bigger. You understand, right?”

“Of course. Everyone here will remember it clearly.”

“I hope so.”

Cheongpung stared blankly at me.

“Benefactor, did I do something wrong?”

Gong Ilhyuk was faster than I was with his response.

“What? Wrong?”

His gaze turned murderous as he glared at Cheongpung.

“Are you insulting me and the Zhongnan Sect right now?”

“That’s not it. I was just…”

“Can’t you shut that mouth of yours?”

A complicated, subtle expression appeared on Cheongpung’s face.

Then he said the one thing more than enough to make Gong Ilhyuk lose his reason.

“Wow, this is the first time anyone’s ever sworn at me. How fascinating.”

“You goddamn bastard…!”

Whoosh!

A heavy sound split the air.

Gong Ilhyuk’s fist shot toward Cheongpung’s ribs at blinding speed.

Then—

Crack. Crunch.

“……!”

“……!”

Amid the silent shock, one man opened his mouth wide in pain.

His fist had been crushed. Bone jutted through the torn flesh of his forearm, and blood covered Gong Ilhyuk as he asked in a trembling voice,

“Wh-what is this? What kind of fist technique…?”

If he hadn’t asked, I would have asked the same thing.

I had expected this result, but not to this extent.

With a single counter, Cheongpung had rendered Gong Ilhyuk, a Level 70-plus master, completely helpless.

And then…

“It wasn’t a fist technique.”

At my mutter, Cheongpung answered with a face that looked ready to vomit.

“Benefactor is right. It wasn’t a fist technique. It was a palm technique called the Taeeul Miri Palm. But Senior, you’re bleeding too much. The smell of blood is making my stomach churn. Urk!”

What a lunatic.

I gave a hollow laugh as Cheongpung flung Gong Ilhyuk aside and began dry heaving.

That was when—

“Ta-Taeeul Miri Palm!”

Li Feng asked with his eyes wide.

“Did you just say Taeeul Miri Palm? Are you certain?”

“Urk, yes. My grandfather taught me.”

“M-May I ask his name?”

“Mae Jonghak, urk—urgh!”

Splash!

I was shocked that Cheongpung had vomited in the very place where the king was about to arrive, but Li Feng seemed unfazed.

He trembled as though he had been struck by lightning, then squeezed out a single word.

“Sword Saint…”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 140`.

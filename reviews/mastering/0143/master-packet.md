# Master Edit Task — Chapter 143

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
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 검법     | **sword technique**                              |                                                       |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 사숙     | **Martial Uncle**                            |
| 사질     | **Martial Nephew**                           |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 아이템              | **Item**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 태사부 | **Grandmaster** | Huashan title referring to Mae Jonghak. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 근위대 | **royal guard** | Guard unit protecting Prince Shangshan. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 이풍 | 진태경 | senior_official_to_respected_young_martial_artist | Young Hero Jin | formal and respectful | Addresses Taekyung as 진 소협 after praising his reputation. |
| 이풍 | 청풍 | Huashan lay disciple to martial uncle | Young Hero; Martial Uncle Cheongpung | formal and reverent | Li Feng initially addresses Cheongpung as 소협 while testing his knowledge, then recognizes him as 사숙 after witnessing his Huashan sword technique. |
| 청풍 | 이풍 | Martial Uncle to Martial Nephew | Martial Nephew Li Feng | exuberant and deferential | Cheongpung adopts the address to obtain royal-guard armor and weapons. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 진태경 | 이풍 | junior_to_respected_official_and_martial_ally | Great Hero Li | polite and respectful | Agrees with Li Feng's proposal that Zhu Bao visit the Jin Family's banquet. |
| 이풍 | 주표 | official_to_prince | Your Highness | formal-deferential | Suggests that Zhu Bao visit the Jin Family's grand banquet in fifteen days. |
| 주표 | 청풍 | prince_to_young_martial_artist | you | formal and gatekeeping | Refuses Cheongpung's autograph until he acquires a martial title. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
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

#### Chapter 141 tail (verified mastered)

…
breaking through ten formations did we reach his residence. Can you guess what I saw there?” Everyone present could guess. Li Feng’s gaze was fixed on Cheongpung’s face. “A cute little boy. He was much smaller than the other children his age, but he was diligently swinging a sword… No one could laugh. Who could laugh after seeing a monster perform the Plum Blossom Sword Technique at the age of ten?” “……!” “……!” Silent shock spread through the crowd. Gong Ilhyuk stammered. “That—that’s impossible. As far as I know, one must be at least First Rate to perform the Plum Blossom Sword Technique…” “Unimaginable things sometimes happen in Murim. Compared to that, pulling dirty tricks in a friendly duel is nothing.” Li Feng gave a self-deprecating laugh. “After more than a month of facing the wall in training, I came to a realization. I had no reason to remain there. That was why I left Huashan. What do you think? Isn’t it amusing?” Li Feng’s story hit hard. Everyone, myself included, stared silently at Cheongpung. Suddenly, I remembered the conversation I’d had with him at Honghwa Inn the night before. *“I was ten years old. One day, dozens of people came barging in and made a scene. I remember my grandfather shouting at them to get the hell out before he set fire to the mountain.”* *“Ah. So that’s why he keeps changing where he lives…?”* *“Yes. Fortunately, the mountain is so large that he’s managed to avoid them for ten years.”* Until then, I hadn’t known that the people who had come to cause trouble ten years ago were the leaders of Huashan, or that the Sword Saint Mae Jonghak was Cheongpung’s grandfather. And the part about them making a scene was only how it had appeared from young Cheongpung’s perspective. The reality had probably been very different. *Who would cause trouble for the Sword Saint? That’s a perfect way to get yourself killed.* The Sword Saint who had threatened to set fire to his own sect wasn’t exactly ordinary, either. In any case, on the day Huashan had nearly become a real volcano, Li Feng had met Cheongpung as a child and clearly despaired after witnessing his talent. *Fair enough. First Rate at the age of ten.* Countless people failed to reach First Rate even after turning twenty. Two of the rising martial artists from the Five Gates of Shanxi present here still fell short of being called First Rate masters. And yet Cheongpung had reached that realm at the age of ten. *Could Jin Mukyung have done the same?* The moment that question occurred to me, Gong Ilhyuk shouted as though having a fit. “Proof! What proof is there that he’s that child?” The rising martial artists of the Five Gates of Shanxi who had been trying desperately to curry favor, Hong Jin, who had been watching with great interest, and even the other two members of the Three Hands of Zhongnan all frowned as though they had planned it together. “There is no proof. All I have is my memory.” “Exactly. Mountains and rivers change in ten years. Should I really trust your paltry memory?” “No. To be honest, I’m not certain either. I don’t know how that child grew up.” Li Feng answered calmly, then suddenly drew his sword. *Shing.* He studied the blade as it radiated a cold chill, then asked Cheongpung, “Young Hero, how much do you know about Huashan’s martial arts?” Cheongpung answered with a bewildered expression. “Uh, I’m not from Huashan.” “You’re not from Huashan…” “No. My grandfather just taught me various things because he said they would be good to learn.” “Then allow me to ask. Of the Six Harmonies Sword, Plum Blossom Sword Technique, Supreme Clarity Sword, Taeeul Miri Palm, Falling Flower Chasing Shadow Palm, and Scattering Flowers Shadowless Hand… how many do you know?” “All of them.” “Heh. All of them. Every one.” Li Feng gave a hollow laugh and handed his sword to Cheongpung. “Could you perform the Plum Blossom Sword Technique?” “My grandfather told me not to show my martial arts to anyone.” “One form—no, a single sword stroke will suffice.” After hesitating, Cheongpung took hold of the hilt. “Then I’ll show you briefly.” The instant he finished speaking, something changed. *Sssssss.* *Sword Energy? No.* From Cheongpung’s head to his toes, tangible strands of purple qi flowed from his entire body. It was Extreme Yang internal energy so potent that merely being near it scorched the breath in one’s lungs. “The Zaha Divine Technique[^2]…!” Li Feng let out a cry of delight. At that moment— *Whoosh!* The tip of Cheongpung’s sword traced a beautiful arc. Like plum blossoms falling at the end of the season, a single streak of Sword Energy cleaved the enormous table in half. The food, the dishes, even the sturdy table. “Ah…” A gasp escaped me before I knew it. Breaking things was easy. But Cheongpung’s Sword Energy was so sharp and clean that, if the table hadn’t collapsed a moment later, no one would have noticed it had been cut. *Boom! Crash!* As the table split in two and collapsed, Li Feng clasped his fist and palm in an exceedingly respectful salute. “Li Feng, lay disciple of Huashan, pays his respects to Martial Uncle Cheongpung.” [^1]: Candied hawthorn skewers are fruit skewers coated in hardened sugar. [^2]: A Huashan internal-energy technique.

#### Chapter 142 tail (verified mastered)

…
my perspective, wouldn’t the phrase ‘acknowledged by all’ sound better?” Hong Jin continued without missing a beat. “Great Hero Gong, let me ask you directly. Does the Zhongnan Sect have a master like the Sword Saint?” “…That is…” “Then does it have a young prodigy as outstanding as that Young Hero over there?” “……” None of the Three Hands of Zhongnan, Gong Ilhyuk included, could easily answer. The Sword Saint? The Zhongnan Sect’s Sect Leader, the Wind-and-Cloud Sword Lord, was occasionally compared to the Ten Kings, but that was as far as it went. As for a monster like Cheongpung, none of them had ever heard of such a person, much less seen one. Gong Ilhyuk in particular flushed red, having attacked first only to be brought to his knees in a single exchange. “B-but our sect has no fewer Peak masters than Huashan.” “I’ve heard that the strength of a Murim sect doesn’t depend on how many masters it has, but on *what kind* of masters it possesses.” Hong Jin’s remark struck the heart of the matter, leaving Gong Ilhyuk momentarily speechless. But no matter what it took, he had to prevent Huashan from taking their place. “Furthermore, every venture we’ve undertaken with the government has been completed successfully. Huashan, on the other hand, has no experience with this sort of project. They’re bound to be clumsy and make mistakes.” “Oh my, is that so?” Hong Jin smiled and turned toward someone. “Assistant Commissioner Li, what do you think?” Li Feng, who had watched everything in silence, answered. “That is true. Huashan does tend to draw a firm line between the government and Murim.” Hong Jin frowned, and color returned to Gong Ilhyuk’s face. But Li Feng’s heavy voice continued. “However, doesn’t everyone have a first time?” “Li Feng, you bastard!” Hong Jin burst out laughing. “Our Assistant Commissioner Li has truly come a long way.” “Thanks to you.” The two men had exchanged almost exactly the same words only a quarter of an hour earlier, but the atmosphere was now the exact opposite. They continued their conversation in a warm and friendly atmosphere. “I’d like you to act as our intermediary, Assistant Commissioner Li. What do you think?” “Of course. I’ll send a messenger pigeon to my Master. The Sect Leader will be pleased to hear this news as well.” “Ah, and you should also tell him that we have an honored guest here.” Li Feng followed Hong Jin’s meaningful glance and smiled faintly. “That is news our Grandmaster will be pleased to hear.” “It’s a good start.” “I think so too.” Completely excluded from the conversation, Gong Ilhyuk trembled from head to toe. Things had already gone too far to turn back. He swept a gaze filled with fury and betrayal across the room. “How dare you look down on the Great Zhongnan Sect.” “Hey, there’s something I’ve been meaning to say.” The voice belonged to Jin Taekyung, who had suddenly cut into the conversation. He gave a short laugh and continued. “We’re not looking down on the Zhongnan Sect. We’re looking down on you. You might not know this, but I’m a huge fan of the Zhongnan Sect. *The Reign…* Anyway, I faithfully kept up with it through volume thirty-four.” “What kind of bullshit are you spouting? A family without even a proper pedigree like the Jin Family of Taiyuan has no place butting in!” Taekyung put on a wounded expression and poked Cheongpung in the side. “Young Master Cheongpung, that old man says our family doesn’t even have a family tree.” “What? He said that to my Benefactor?” “Yeah. I know he’s a Senior, but isn’t that going too far? I’m too scared of the Nine Sects and One Gang to answer him myself, so could you say something for me?” “M-me? I’m not very good at things like that.” “Am I not your Benefactor? Was I only your Benefactor in name?” “No, of course not.” “Then say what I tell you.” After Taekyung finished whispering something to him, Cheongpung hesitantly opened his mouth. “G-get… get…” “Young Master Cheongpung, louder! You can do it!” Buoyed by Taekyung’s encouragement, Cheongpung squeezed his eyes shut and shouted, “Get lost, you boomer bastards!” “……!” “……!” *Boomer?* They didn’t know exactly what it meant, but that wasn’t important. It had been followed by the word *bastards*. “You goddamn…!” All three men, Gong Ilhyuk included, glared with their eyes wide open. Who were they? They were disciples of the Zhongnan Sect’s headquarters. They were accustomed to the admiring gazes of others, and this was a humiliation they could never wash away. But… Gong Ilhyuk ground his teeth. “Let’s go!” Swallowing his outrage, he turned away. Neither the opponent nor the place was suitable for repaying this humiliation. *I’ll make them pay for this someday. I swear it!* Blood dripped from the fist he clenched so hard it seemed it would crush. He stormed out of the grand hall, his footsteps heavy and violent. Behind him came the voices of Jin Taekyung and Cheongpung. “Wow, you’re good at swearing. Was that your first time too?” “Yes! I’ve never sworn before!” “For a first attempt, you’ve got some real talent. You should learn a lot from me from now on. As you go through life, there are plenty of times you’ll need to use them even if you don’t want to.” “Yes!”

## Korean source

```text
＃143화



개망신당한 종남삼수가 쿵쾅거리며 떠나자 홍진이 품에서 자그마한 종을 꺼내 흔들었다.

“자, 그럼 불청객들도 갔으니 정리가 필요하겠군요.”

뎅, 뎅, 뎅.

정확히 세 번. 종소리가 채 사라지기도 전에 철문이 열리더니 수십 명의 하인이 들어와 허리를 굽힌다.

“대전을 깨끗이 치우고 새로 음식을 내오너라.”

“명을 받들겠습니다.”

재차 허리를 굽힌 그들은 일사불란하게 움직였다.

쪼개진 탁자와 널브러진 음식물들, 심지어 청풍의 토사물조차도 눈썹 하나 깜짝하지 않고 척척 치워 나가기 시작했다.

‘프로네, 프로야.’

어지간한 청소 업체 저리 가라다.

감탄하는 나와는 달리 뭐 마려운 표정으로 끙끙거리던 청풍이 하인들을 향해 조심스레 다가갔다.

“죄, 죄송합니다. 제가 도와드릴게요.”

하인 중 하나가 고개를 저었다.

“아닙니다. 저희가 해야 할 일입니다.”

“그래도 제가 어질러 놨으니 이것만이라도…….”

하인들이 아무리 건장한 사내들이라고 해도 상대는 절정 고수. 그들은 청풍의 뜻을 따를 수밖에 없었다.

그러나 억지로 청소 도구를 빼앗아 토사물을 치우던 청풍의 움직임이 순간 덜컥 멈췄다.

“우욱, 우웨에에엑!”

“…….”

제발 가만히 있어. 괜히 일거리 늘리지 좀 말고.

또다시 한바탕 거하게 쏟아 내는 녀석의 모습에, 홍진이 미심쩍은 눈빛으로 이풍을 바라봤다.

“이 첨사, 저 청년이 정말 검성 매종학 대협의 제자가 맞나요?”

“확실합니다.”

“그런데 상태가 왜 저래요?”

“크흠.”

이풍이 붉어진 얼굴로 헛기침을 했다. 그에게 있어 청풍은 검성 매종학의 제자이자 사문의 어른이지만, 살짝 이상한 놈인 것도 부정할 수 없는 사실일 테다.

“아무래도 속세와는 동떨어진 삶을 살아오다 보니 저러시는 것 같습니다만.”

“아니, 아무리 그래도 그렇지. 매 대협이 기본적인 것도 안 가르쳐 줬단 말이에요?”

“그게…… 제가 보고 듣기로는 태사부께서도 범상치 않으신 분이라.”

범상치 않은 분이라.

혼신의 힘을 다한 포장이었지만 내 귀에는 ‘그놈이 그놈인데요.’로 들린다.

홍진도 비슷한 느낌을 받았는지 잠깐 침묵을 지켰다.

“이번 일, 화산파에게 맡겨도 되는 거죠?”

“……예.”

어쩐지 한 박자 늦은 이풍의 대답에 홍진이 고개를 절레절레 저었다.

“그 이야기는 나중에 나누도록 하고, 슬슬 가 볼까요?”

그 말에 의구심을 느낀 내가 물었다.

“어디를요? 아직 전하도 안 오셨는데.”

“바로 그 전하를 모시러 가려고요.”

“네?”

“이대로라면 기다리다가 해 떨어져요. 난 전하가 어디에 계시는지 대충 알거든.”

눈을 찡긋하며 돌아서는 홍진을 보며 생각했다.

‘저 짓거리만 안 해도 괜찮은 놈인데.’

우리 편 들어 준 건 고맙긴 한데, 그건 그거고 이건 이거다.

내 엉덩이는 소중하니까.



* * *



홍진과 이풍. 두 사람이 나란히 앞장서서 걸었다.

그 뒤를 따라가다 보니 그들이 이곳에서 어떤 위치이며, 어느 정도의 위상을 갖고 있는지 대강 파악할 수 있었다.

“충!”

사람은 눈빛과 태도, 목소리에서 감정이 묻어나오는 법.

이풍을 향해 힘차게 군례를 올리는 군사들의 모습에서 무한한 존경심을 읽어 낼 수 있었다.

‘그럴 만도 하지.’

화산파의 속가제자인 이풍은 초일류의 고수다. 강함을 숭상하는 건 수컷들의 본능인 데다 그는 척 봐도 사내다운 냄새가 물씬 풍겼다. 잠깐 지켜본 바로는 우직하고, 과묵하다.

‘그렇다고 해서 아주 꽉 막힌 사람도 아니고.’

홍진의 제안을 받아들인 것만 봐도 알 수 있다. 서로 으르렁거리던 관계가 분명한데, 손을 잡을 때와 놓을 때를 안다.

적당히 융통성 있는 상관을 싫어할 사람은 없지.

‘그럼 홍진은?’

나는 시선을 옆으로 옮겼다.

경박하게 궁둥이를 씰룩거리며 걸어가는 홍진에게는 군사 중 그 누구도 존경심을 표하지 않았다. 오히려 몇몇은 경멸 어린 시선을 던지기까지 했다.

다만…….

“도, 도지휘동지 대감을 뵙습니다.”

“응. 그래. 수고해요.”

“예, 옛!”

가는 길에 마주친 몇몇 관리와 하인들은 과장스러울 정도로 설설 기었다.

떨리는 목소리와 조심스러운 발걸음. 그들이 보여 준 감정은 명백한 두려움이다.

‘존경과 두려움이라.’

상반되는 감정이지만 한 가지 맥락에서는 같다.

그건 바로 사람들 다루는 용인술(用人術)이다. 이풍과 홍진은 각각 존경과 두려움으로 수하들의 지지를 받고 있었다.

‘한 사람은 군부를, 한 사람은 내정을 손에 쥔 셈인가?’

산서성은 변방으로 불리지만 그 규모는 무시할 수 없다.

광활한 면적과 호적에 등록된 인구만 수백만에 이르는 당당한 자치 구역인 것이다.

땅이 있는 곳에 사람이 모이고, 사람이 모인 곳에는 권력과 재물이 흐른다. 산서성부 내에서도 보이지 않는 치열한 힘겨루기가 계속되고 있었다.

‘아까부터 들어 보니 홍진이 더 앞선 것 같긴 하지만, 뭐. 내가 신경 쓸 문제는 아니지.’

먹고 살기도 바쁜 마당에 남의 집 권력 싸움에 끼어들 생각은 추호도 없다.

이런저런 생각을 하며 얼마나 걸었을까, 우리는 어느덧 아홉 개의 문을 지나 일단의 무리와 맞닥뜨렸다.

“도지휘동지, 그리고 도지휘첨사 오셨습니까.”

열 번째 문은 유독 크고 높았다. 정말 그렇게 지었는지, 아니면 물 샐 틈 없이 주위를 둘러싼 일백의 병력 때문에 그렇게 보이는지는 모르겠다.

‘이야, 경계 삼엄한 것 보소.’

절정 고수, 그것도 검기를 쓸 수 있을 정도는 돼야 어떻게 해 볼 수 있을까? 하나같이 갑주와 창, 검, 활 등으로 중무장한 그들은 투구 사이로 날카로운 눈빛을 뿜어냈다.

지금까지 주위를 구경하며 연신 탄성을 내지르던 청풍도 목소리를 한껏 죽이고 내게 속삭였다.

“우와아. 이분들은 뭐 하시는 분들이세요?”

“글쎄요, 아마도 상산왕 전하를 경호하는 근위대가 아닐까요?”

“근위대요? 멋있다…….”

멍한 얼굴로 중얼거리던 청풍이 주먹을 불끈 쥐었다.

“은인, 저 결심했어요.”

“뭘요?”

난 왜 얘가 입을 열 때마다 불안해질까?

물론 이번에도 예감은 정확히 들어맞았다.

“저도 근위대에 들어갈래요!”

“……그렇게 좋은 생각은 아닌 것 같은데요.”

검성이 좋아할 것 같지 않은 소식이다.

나는 지끈거리는 이마를 문지르며 말했다.

“그, 조부님 허락은 맡아야 하지 않겠어요?”

“괜찮아요. 할아버지가 그랬어요. 인생은 짧으니까 하고 싶은 게 생기면 뭐든 해 보라고.”

“그래서 그게 근위대다?”

“네.”

청풍은 반짝거리는 눈빛으로 칼같이 늘어선 근위대를 뚫어져라 응시했다. 정확히는 그들의 번쩍거리는 흑색 갑옷을.

아니, 이 새끼가 설마?

“……혹시 갑옷이 멋있어서 그런 건 아니죠?”

“헉.”

맞네. 이런 미친놈을 봤나.

‘근위대 굿즈가 탐나서 근위대에 들어가는 놈이 어디 있냐.’

우리의 대화를 듣고 있던 이풍이 10년은 늙은 얼굴로 다가왔다.

“청풍 사숙, 저야 보잘것없는 속가제자라지만 사숙께서는 화산의 미래를 짊어지실 적전제자이십니다. 사문을 버리고 군문에 투신하신다니요, 제발 언행에 주의를…….”

정곡이 찔린 얼굴로 서 있던 청풍이 다급하게 손을 내저었다.

“아, 아니에요. 진짜 아닌데.”

“정말이십니까?”

“네, 네!”

“그럼 그렇게 알고 있겠습니다. 혹시 필요하시다면 가시는 길에 갑옷 한 벌 챙겨 드리려고 했는데…….”

덥석.

“감사히 받을게요. 이 대협.”

“…….”

“…….”

아니, 이 새끼가 진짜?

싸해진 주변 상황도 모르고 청풍이 헤헤 웃었다.

“이 대협은 좋은 사람이에요.”

“대협이 아니라 사질입니다. 청풍 사숙.”

“사숙, 사질. 이런 말은 어색한데…… 그냥 서로 편하게 부르면 안 돼요?”

“안 됩니다. 본 파의 위계는 엄격합니다. 앞으로 사질이라고 부르십시오. 그래야 갑옷을 드릴 겁니다.”

“으음. 그래도…….”

망설이는 청풍을 향해 이풍이 마지막 한 방을 날렸다.

“앞으로 저를 사질이라고 부르신다면 근위대가 쓰는 병장기도 함께 드리겠습니다.”

“헉……!”

게임 끝이다.

굿즈의 완성은 세트 아이템인 법. [근위대 갑옷 세트]를 손에 넣게 된 청풍이 환희에 가득 찬 얼굴로 양팔을 벌렸다.

“이풍 사질!”

이풍이 엉거주춤 대답했다.

“처, 청풍 사숙.”

“저는 이풍 사질이 세상에서 제일 좋아요!”

“……감사합니다. 사숙.”

저런 놈을 손자라고 20년 동안 키운 검성이 불쌍해진다.

근위대마저 이 뜻밖의 촌극에 정신이 팔려 있을 때, 홍진이 한숨을 푹 내쉬며 입을 열었다.

“뭐 해요, 문 안 열고?”



* * *



가슴팍에나 닿으려나? 어린 왕, 상산왕(上山王) 주표(朱豹)는 내가 생각한 것보다 훨씬 작았고, 또 강했다.

쉬쉬쉬쉭!

고작 열 살짜리 어린아이가 휘두르는 검에서 날 만한 소리가 아니다. 날카로운 검로, 바쁘게 연무장 바닥을 누비는 보법.

검공에는 그리 조예가 깊지 않은 내게도 충분히 고개가 끄덕여질 만한 수준이었다.

‘괜히 우리를 초청한 게 아니었군.’

처음 상산왕의 초청을 받았을 때 든 생각은 하나였다.

가서 적당히 듣고 싶어 하는 무용담이나 몇 개 들려줘야지. 딱 이 정도?

하지만 저 아이는 다르다. 무용담이 아니라 무공에 대해 알려 줘야 할지도 모른다.

“전하를 본 소감이 어때요?”

연무장 바깥에서 대기 중이던 수행원들을 손짓 하나로 전부 물린 홍진이 물었다.

그 와중에도 무공에 몰입한 어린 왕은 누가 왔는지, 누가 가는지도 눈치채지 못하고 있었다.

“정확히 어떤 소감을 말씀하시는 겁니까?”

“글쎄, 일단은 무공?”

나는 솔직히 대답했다.

“생각 이상입니다. 아니, 뛰어나요. 언제부터 익히기 시작한 겁니까?”

“삼 년 전부터 무공에 흥미를 보이기 시작하셨죠.”

“삼 년…….”

“네. 처음 검을 쥔 그날부터 특별한 일이 없는 한 하루도 빠짐없이 무공을 수련하세요.”

이풍이 흐뭇하게 웃으며 덧붙였다.

“여러모로 어린아이답지 않으신 분이오. 대단한 집념의 소유자시지. 마치 진 소협처럼 말이오.”

“저요?”

“그렇소. 진 소협도 어린 시절부터 뼈를 깎는 노력을 했다지요? 태원진가가 비밀리에 심혈을 기울여 키운 고수답게 큰 활약을 펼치고 있잖소.”

“어…… 그렇죠.”

저건 대외적으로 태원진가에서 퍼트린 헛소문이다.

정작 나는 내가 열 살 때 뭘 했는지는 기억도 안 난다.

‘초등학교 다녔겠지, 뭐.’

이풍이 말을 이었다.

“전하께서 산서잠룡의 이야기를 들으시고는 얼마나 좋아하셨는지 모르오. 아마 오늘도 진 소협과 만나기를 학수고대하셨겠지.”

“……그런 것치고는 꽤 오래 기다리지 않았나요?”

거의 한 시간은 기다린 것 같은데. 왕이라서 그런가, 어린 녀석이 벌써부터 기본 매너가 없어요.

소심하게 투덜거리는 내게 이풍이 빙긋 웃었다.

“전하께선 긴장을 할수록 무공에 몰두하는 습관이 있으시지. 혹시 마음 상했다면 사과드리겠소.”

뭘 또 사과씩이나. 내가 손사래를 치던 그때, 홍진이 입에 두 손을 모아 외쳤다.

“저어어언하-!”

간드러진 외침에 검법을 펼치던 자그마한 신형이 우뚝 멈춘다. 이윽고 우리를 발견한 녀석이 손을 까딱였다.

“뭡니까 저게?”

“뭐긴, 전하께서 부르시는 거지요.”

“아니, 우리가 동네 똥갭니까?”

“와, 저 동네 똥개 처음 해 봐요!”

“……제발 입 좀 다물어. 여기 동네 똥개 해 본 사람 아무도 없어.”

나는 울화를 참으며 연무장을 향해 다가갔다.

상산왕 주표. 한 걸음마다 그의 얼굴이 가까워진다.

‘꼭 싸가지 없는 놈들이 잘생겼더라.’

어린 나이임에도 이미 완성된 이목구비는 뚜렷했고, 검은 눈동자는 나를 빤히 응시하고 있었다.

녀석의 앞에 다다르자 아직 한참 앳된 목소리가 흘러나왔다.

“과인이 누구인지 아는가?”

이미 기본적인 예의는 배웠다. 나는 한쪽 무릎을 꿇어 주표와 시선을 맞췄다.

“예. 상산왕 전하.”

“과인은 아직 그대의 이름을 모른다.”

“태원진가의 진태경이라 합니다.”

위엄 있던 눈동자에 희미한 놀라움이 떠올랐다.

“사, 산서잠룡 진태경이란 말이냐?”

“그렇습니다.”

과연 그가 무슨 반응을 보일까?

한참 말이 없던 어린 왕이 돌연 품에서 뭔가를 꺼냈다. 어른 손바닥만 한 목판과 단검이었다.

“이거…….”

“……?”

일단 주니까 받긴 했는데. 뭘 어쩌라고?

어리둥절한 내게 주표가 위엄 있는 한마디를 던졌다.

“서명을 부탁하마.”

“…….”

아, 사인해 달라고?
```

## Current accepted English baseline

```markdown
# Chapter 143

After the Three Hands of Zhongnan left in disgrace, their footsteps echoing heavily, Hong Jin pulled a small bell from inside his robes and shook it.

“Well, now that the uninvited guests are gone, I suppose we should clean up.”

*Ding. Ding. Ding.*

Exactly three times. Before the sound had even faded, the iron doors opened and dozens of servants entered, bowing at the waist.

“Clean the grand hall and bring out a fresh meal.”

“We’ll carry out your orders.”

After bowing once more, they moved with perfect coordination.

They began clearing away the broken tables and scattered food without batting an eye—not even at Cheongpung’s vomit.

*They’re professionals. Absolute professionals.*

They put most cleaning companies to shame.

Unlike me, Cheongpung had been groaning with an expression like he needed to use the bathroom. He cautiously approached the servants.

“I-I’m sorry. Let me help.”

One of the servants shook his head.

“No, sir. This is our duty.”

“But I made the mess, so at least let me…”

No matter how sturdy the servants were, they were facing a Peak master. They had no choice but to follow Cheongpung’s wishes.

However, the moment Cheongpung forcibly took the cleaning tools from them and began wiping up the vomit, his movements abruptly stopped.

“Urk, uweeek!”

“……”

*Please stay still. Stop making more work for them.*

As Cheongpung emptied his stomach once again, Hong Jin looked at Li Feng with a doubtful expression.

“Assistant Commissioner Li, is that young man really Sword Saint Mae Jonghak’s Disciple?”

“Certainly.”

“Then why is he like that?”

“Ahem.”

Li Feng cleared his throat, his face reddening.

To him, Cheongpung was both Sword Saint Mae Jonghak’s Disciple and an elder of his sect. But it was also impossible to deny that he was a slightly strange young man.

“I suppose he’s like this because he’s spent his life completely removed from the secular world.”

“No, but even so. Are you saying Great Hero Mae didn’t teach him the basics?”

“Well… from what I’ve seen and heard, my Grandmaster is not an ordinary person himself.”

*Not an ordinary person.*

It was an impressive effort at putting things politely, but what I heard was, *They’re two of a kind.*

Hong Jin must have gotten a similar impression, because he remained silent for a moment.

“Would it really be all right to leave this matter to Huashan?”

“……”

“Yes.”

Li Feng’s answer came half a beat late. Hong Jin shook his head in disbelief.

“We can discuss that later. Shall we get going?”

His words made me suspicious, so I asked,

“Where? His Highness hasn’t even arrived yet.”

“That’s exactly who I’m going to fetch.”

“What?”

“If we stay here, we’ll be waiting until sunset. I have a rough idea where His Highness is.”

I watched Hong Jin turn away with a wink.

*He’d be a decent guy if he just stopped doing that.*

I was grateful that he had taken our side, but that was that, and this was this.

*My backside is precious.*

* * *

Hong Jin and Li Feng walked side by side at the front.

As I followed them, I gradually began to understand what positions they held here and how much influence they possessed.

“Loyalty!”

People’s emotions show in their eyes, their posture, and their voices.

The soldiers snapped off energetic military salutes toward Li Feng, and I could read boundless respect in their faces.

*It’s understandable.*

Li Feng, a lay disciple of Huashan, was an advanced First Rate master. Respecting strength was a male instinct, and he radiated an unmistakably masculine presence. From what I had observed, he was steadfast and taciturn.

*But he isn’t completely inflexible, either.*

I could tell from the fact that he had accepted Hong Jin’s proposal. Their relationship had clearly been hostile, but Li Feng knew when to join hands and when to let go.

No one disliked a superior who was reasonably flexible.

*Then what about Hong Jin?*

I shifted my gaze to the side.

Not a single soldier showed Hong Jin any respect as he walked along, frivolously wiggling his backside. If anything, some of them even cast contemptuous looks his way.

However…

“I-I pay my respects to Deputy Military Commissioner Hong.”

“Mm. Yes. Good work.”

“Yes, sir!”

Several officials and servants we passed on the way practically groveled before him.

Their trembling voices and cautious footsteps made their emotions obvious.

They were afraid.

*Respect and fear.*

They were opposing emotions, but they were the same in one respect.

Both came from the art of handling people. Li Feng and Hong Jin each held the support of their subordinates through respect and fear.

*So one of them controls the military, while the other controls civil affairs?*

Shanxi Province was called a frontier region, but its size couldn’t be ignored.

It was a respectable autonomous territory with a vast area and a population of several million registered in its household records.

Where there was land, people gathered. And where people gathered, power and wealth flowed. Even within the Shanxi Provincial Office, an invisible and fierce struggle for power was still underway.

*From what I’ve heard, Hong Jin seems to be ahead. But that’s not my problem.*

I was too busy trying to make a living to get involved in someone else’s power struggle.

After walking for some time while lost in thought, we passed through nine gates and came upon a group of people.

“Deputy Military Commissioner, and Assistant Military Commissioner, have you arrived?”

The tenth gate was particularly large and tall. I couldn’t tell whether it had genuinely been built that way or only seemed so because a hundred soldiers surrounded it without leaving even a gap.

*Wow. Talk about tight security.*

Would a Peak master, and one capable of using Sword Energy at that, be needed to try anything here? Every one of the guards was heavily armed with armor, spears, swords, bows, and more. Sharp eyes gleamed from beneath their helmets.

Cheongpung, who had been looking around and exclaiming in wonder this entire time, lowered his voice and whispered to me.

“Wow. What do these people do?”

“I’m not sure. Perhaps they’re the royal guard protecting Prince Shangshan?”

“The royal guard? They’re amazing…”

Cheongpung muttered with a vacant expression, then clenched his fists.

“Benefactor, I’ve made up my mind.”

“About what?”

*Why do I get nervous every time he opens his mouth?*

Of course, my premonition proved correct again.

“I want to join the royal guard too!”

“……I don’t think that’s such a good idea.”

This was news the Sword Saint probably wouldn’t like.

I rubbed my throbbing forehead.

“Um, shouldn’t you get your grandfather’s permission first?”

“It’s all right. Grandfather said life is short, so whenever I want to do something, I should try it.”

“So that’s why you want to join the royal guard?”

“Yes.”

Cheongpung stared intently at the royal guards standing in perfect rows, his eyes shining.

More precisely, he was staring at their gleaming black armor.

*No way. Is this guy…?*

“……It’s not because the armor looks cool, is it?”

“Gasp.”

That was it.

What kind of lunatic joined the royal guard because he wanted their merchandise?

Li Feng, who had overheard our conversation, approached us with a face that looked ten years older.

“Martial Uncle Cheongpung, I may be nothing more than a lowly lay disciple, but you are Huashan’s direct Disciple, someone who will bear the future of the sect on your shoulders. To abandon the sect and devote yourself to the military… Please be careful with what you say and do…”

Cheongpung stood there with an expression that had clearly been hit right in the bull’s-eye, then frantically waved his hands.

“N-No, that’s not it. Really.”

“Is that so?”

“Yes, yes!”

“Then I’ll take your word for it. I was considering bringing you a suit of armor on the way out, if you needed one, but…”

Cheongpung took the bait immediately.

“Thank you. I’ll accept it gratefully, Great Hero Li.”

“……”

“……”

*Is this guy serious?*

Cheongpung, oblivious to the sudden chill in the air around us, grinned.

“Great Hero Li is a good person.”

“I’m not Great Hero. I’m your Martial Nephew, Martial Uncle Cheongpung.”

“Martial Uncle, Martial Nephew. Those words feel awkward…”

Cheongpung tilted his head.

“Can’t we just call each other whatever feels comfortable?”

“No. Our sect’s hierarchy is strict. Call me Martial Nephew from now on. Then I’ll give you the armor.”

“Hmm. Even so…”

Li Feng delivered his final blow to the hesitating Cheongpung.

“If you call me Martial Nephew from now on, I’ll give you the weapons used by the royal guard as well.”

“Gasp…!”

The game was over.

The finishing touch for merchandise was a complete set. Cheongpung, now on the verge of obtaining the Royal Guard Armor Set, spread both arms with a face full of joy.

“Martial Nephew Li Feng!”

Li Feng answered awkwardly.

“M-Martial Uncle Cheongpung.”

“I like Martial Nephew Li Feng best in the world!”

“……Thank you, Martial Uncle.”

I felt sorry for the Sword Saint, who had raised that guy as his grandson for twenty years.

While even the royal guards were distracted by this unexpected farce, Hong Jin let out a deep sigh and spoke.

“What are you doing? Why haven’t you opened the gate?”

* * *

The young prince barely came up to my chest, if that. Prince Shangshan, Zhu Bao,[^1] was much smaller than I had expected—and much stronger.

*Ssshhk, ssshhk, ssshhk!*

That was not a sound a mere ten-year-old child should have been able to make with a sword.

His sword paths were sharp, and his footwork technique carried him busily across the training ground.

Even I, who wasn’t particularly well versed in sword techniques, could tell that his skill was more than enough to make me nod in approval.

*So there was a reason he invited us.*

When I first received Prince Shangshan’s invitation, I had one thought.

*I’ll go and tell him a few of the heroic tales he wants to hear. That was about all I had expected.*

That was all I had expected.

But that child was different. I might have to teach him about martial arts instead of telling him stories about my exploits.

“What do you think of His Highness?”

Hong Jin had waved away all the attendants waiting outside the training ground with a single gesture before asking me.

Even then, the young prince, absorbed in his martial arts, didn’t notice who had arrived or who had left.

“What kind of opinion are you asking for?”

“Well, for starters, his martial arts?”

I answered honestly.

“He’s beyond my expectations. No, he’s outstanding. When did he begin learning?”

“He began showing an interest in martial arts three years ago.”

“Three years…”

“Yes. Ever since the day he first held a sword, he has trained in martial arts every single day unless something unusual happened.”

Li Feng smiled proudly and added,

“He is not like an ordinary child in many ways. He possesses astonishing determination. Much like Young Hero Jin.”

“Me?”

“That’s right. I heard Young Hero Jin worked himself to the bone from a young age. You’ve been making quite a name for yourself, just as one would expect from a master the Jin Family of Taiyuan secretly raised with such painstaking care.”

“Uh… yes, I suppose.”

That was a bogus rumor the Jin Family of Taiyuan had spread for public consumption.

In reality, I didn’t even remember what I had been doing at the age of ten.

*I must have been attending elementary school or something.*

Li Feng continued.

“You have no idea how delighted His Highness was when he heard the story of the Sleeping Dragon of Shanxi. He must have been eagerly awaiting the chance to meet Young Hero Jin today.”

“……For someone who was looking forward to it, didn’t he make us wait rather a long time?”

I felt as though we had been waiting for almost an hour. Was it because he was a prince? The little brat already had no basic manners.

Li Feng smiled faintly at my timid complaint.

“His Highness has a habit of immersing himself in martial arts whenever he is nervous. If he has offended you, please accept my apologies.”

There was no need to apologize over something like that. I was waving my hands dismissively when Hong Jin cupped both hands around his mouth and shouted,

“His Hiiiighness—!”

The little figure who had been practicing his sword technique stopped abruptly at the shrill call. A moment later, he noticed us and crooked a finger.

“What is that supposed to be?”

“What do you mean? His Highness is calling us.”

“No, I mean, are we neighborhood mutts?”

“Wow, this is my first time being a neighborhood mutt!”

“……Please shut your mouth. No one here has ever been a neighborhood mutt.”

Suppressing my frustration, I walked toward the training ground.

Prince Shangshan Zhu Bao. His face came closer with every step.

*The rude ones always seem to be handsome.*

Even at such a young age, his already fully formed features were sharp and distinct. His black eyes stared directly at me.

When I reached him, a voice that was still unmistakably childish drifted out.

“Do you know who I am?”

I had at least learned the basics of etiquette by now. I lowered myself onto one knee so that our eyes were level.

“Yes. His Highness, Prince Shangshan.”

“I do not yet know your name.”

“My name is Jin Taekyung of the Jin Family of Taiyuan.”

A faint trace of surprise appeared in his previously dignified eyes.

“T-The Sleeping Dragon of Shanxi, Jin Taekyung?”

“That’s right.”

I wondered what his reaction would be.

The young prince remained silent for a long moment. Then he suddenly pulled something from inside his robes.

A wooden tablet about the size of an adult’s palm, and a dagger.

“This…”

“……?”

He had handed them to me, so I accepted them. But what was I supposed to do with them?

As I stood there in bewilderment, Zhu Bao delivered a single dignified word.

“I would like your signature.”

“……”

*Oh. He wants an autograph?*

[^1]: Zhu Bao (朱豹) is Prince Shangshan’s personal name.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 143`.

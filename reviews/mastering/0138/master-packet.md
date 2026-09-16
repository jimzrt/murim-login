# Master Edit Task — Chapter 138

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
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 공일혁    | **Gong Ilhyuk**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 산서오문   | **Five Gates of Shanxi**         |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 도지휘사 | **Military Commissioner** | Provincial military commander's office |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 은자 | **silver nyang** | Silver currency unit. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 공일혁 | 이풍 | martial_rivals | Li Feng of Huashan | casual and taunting | Mocks Li Feng's office and recalls his defeat at Huashan ten years earlier. |
| 이풍 | 공일혁 | martial_rivals | you bastard | hostile and furious | Responds to Gong Ilhyuk's insult toward Huashan with an openly aggressive form. |
| 공일혁 | 청풍 | senior_martial_artist_to_junior_martial_artist | Junior | impatient and condescending | Treats Cheongpung as a junior while demanding his introduction. |
| 청풍 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | deferential and apologetic | Uses 선배님 while apologizing for catching Ilhyuk's wrist. |
| 이풍 | 청풍 | Huashan lay disciple to martial uncle | Young Hero; Martial Uncle Cheongpung | formal and reverent | Li Feng initially addresses Cheongpung as 소협 while testing his knowledge, then recognizes him as 사숙 after witnessing his Huashan sword technique. |
| 청풍 | 이풍 | Martial Uncle to Martial Nephew | Martial Nephew Li Feng | exuberant and deferential | Cheongpung adopts the address to obtain royal-guard armor and weapons. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 나발이고 | slang | Dismissive rejection of the preceding concern (to hell with X), not a neutral “or not.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 130–134

## Plot

Cheongpung, an eccentric young Peak master who recently fled Huashan’s Lotus Peak, travels toward Taiyuan after briefly joining a Seongun Escort Bureau escort run. At Honghwa Inn, he meets Jin Taekyung and Hyuk Mujin and begs for candied hawthorn skewers because he has not eaten all day. Taekyung feeds him, learning that Cheongpung was raised in the mountains by his grandfather and came down to test himself against the Ten Dragons and Phoenixes. Taekyung cannot identify Cheongpung’s Level through Qi Sense; his System Window displays `???`.

Five First Rate heirs of the current Five Gates of Shanxi mock Cheongpung, Taekyung, and Mujin from the inn’s second floor, then refuse to apologize. Their spokesman, Woo Jintae, heir to the Seongun Escort Bureau, is publicly slapped and humiliated by Taekyung, who fabricates the identity Tien Shinhan of the Dodong Sect when challenged about his affiliation. The other heirs—Seongryong, Cheonwoo, Myeonghwa, and Sohye—refuse to fight Taekyung. Mujin warns them that they will be next, secures their apology to Cheongpung, and orders them to prostrate themselves.

Woo Jintae had been using the Seongun Escort Bureau’s wealth, gifts, and hospitality to control the current Five Gates scions before their scheduled luncheon with Shanxi’s ten-year-old Prince City Lord. The luncheon, already locked in as The City Lord’s Invitation Quest, is due to take place the following day.

## Continuity

- Cheongpung is an exceptionally young Peak master with an undetectable Level, an innocent and eccentric personality, and a strong appetite. He was raised by his grandfather in the mountains from age five, and his grandfather repeatedly relocates because people keep finding him.
- Cheongpung recently left Huashan’s Lotus Peak and descended from the mountains to determine whether he or the Ten Dragons and Phoenixes are stronger. His status at Huashan, his grandfather’s identity, and his precise affiliation remain unresolved.
- Hyuk Mujin has returned to Taiyuan after five years. His parents are healthy textile merchants who own the city’s largest textile shop, with branches in Henan and Hebei.
- Woo Jintae is the married, nearly thirty-year-old heir and sole male heir in three generations of the Seongun Escort Bureau. He cultivated the current Five Gates scions through lavish hospitality, gifts, and bribes.
- The current Five Gates of Shanxi are an alliance of more than twenty small and medium-sized sects formed after the former Five Gates—including the Samdo Sect and Gunggui Sect—were annihilated at the Battle of Eight Spring Gorge for serving the Head Elder.
- The five scions are Seongryong, Cheonwoo, Myeonghwa, Sohye, and Woo Jintae. They are pampered First Rate martial artists; Jintae is Level 45 and served as spokesman.
- Taekyung has publicly humiliated Jintae and claimed the fabricated identity Tien Shinhan of the Dodong Sect. The other four scions apologized to Cheongpung and were ordered by Mujin to plant their heads on the floor; whether they obey and what consequences follow remain unresolved.
- The City Lord’s Invitation Quest requires Taekyung’s attendance at the next day’s luncheon with young prodigies. The City Lord is a ten-year-old Zhu Prince and the Emperor’s youngest brother; Woo Jintae and the Five Gates scions are also expected to attend.
- Taekyung still intends to reject Lee Seowol’s marriage proposal because he loves Song Song. The Mount Heng Sword Sect’s reconstruction, the Temporary Strength Pill and Dark Heaven, Pung Yang’s wider consequences, and the Fire King’s status remain unresolved.

## Translation Decisions

- Render 성운표국 as **Seongun Escort Bureau**, 표행 as **escort run**, 쟁자수 as **porter**, 표두 as **Escort Chief**, 은원보 as **silver ingot**, 은자 as **nyang of silver**, 사서삼경 as **the Four Books and Three Classics**, and 연화봉 as **Lotus Peak**.
- Render 빙당호로 as **candied hawthorn skewers**, with an explanatory footnote.
- Render 개방 as **Beggars’ Sect**, 삼도문 as **Samdo Sect**, 궁귀문 as **Gunggui Sect**, 산서오문 as **Five Gates of Shanxi**, and 십봉룡 as **Ten Dragons and Phoenixes**.
- Render 우진태 as **Woo Jintae**, 우 소협 as **Young Hero Woo**, 황 소저 as **Young Lady Hwang**, and 혁 아우 as **Little Brother Hyuk**.
- Render 도동파 as **Dodong Sect** and 천진반 as **Tien Shinhan**, preserving Taekyung’s fabricated identity joke.
- Render 대가리 박으십쇼 as **“bend over and plant your heads on the floor,”** retaining Mujin’s blunt comic coercion.
- Render 촉금 as **Shu brocade**, and retain **First Rate**, **Peak**, **City Lord**, **Prince**, and **The City Lord’s Invitation**.

### Prior accepted reading-copy tails

#### Chapter 136 tail (verified mastered)

…
“What do you mean? Surely you aren’t planning to leave just like this?” “Yes. It’s already late, so I was thinking of heading out.” *Going where? We barely got to talk because those random bastards barged in.* I hurriedly waved him off. “Come on, if it’s late, you should stay the night. You said you don’t have any travel money, right?” “It’s all right. I’m used to sleeping rough.” “You shouldn’t be used to that. Right, a new experience! Have you ever slept at an inn?” “I stayed at inns a few times before I lost my travel money. And I’ve already imposed on you both more than enough.” Hyuk Mujin muttered beside me. “That’s true. My candied hawthorn skewers[^1]…” [^1]: Traditional fruit skewers coated in hardened sugar. “You be quiet. So, are you really leaving?” “Yes. Fortunately, I still have business left in Shanxi Province, so if we happen to get the chance, we’ll meet again.” At this point, I had nothing left to say. If a Peak master was determined to leave of his own accord, I couldn’t exactly hold him back by claiming the roads were dangerous at night. Still, I was dying to know the identity of this oddball who had suddenly appeared out of nowhere. “If you have nowhere to go, come to the Jin Family of Taiyuan. Give them my name and they’ll let you in.” “Oh, come to think of it, you’re a Young Master of the Jin Family of Taiyuan, aren’t you? The Sleeping Dragon of Shanxi, Jin Taekyung… I’ll remember my Benefactor’s name.” He had known who I was for some time, but it hadn’t fazed him in the slightest. His reaction amounted to, *Oh, I see.* That was it. Hyuk Mujin subtly caught my eye before cutting in. “The Jin Family of Taiyuan. You don’t know it?” “Well, I think I’ve heard of it somewhere. It does sound familiar, but I don’t really know much about it.” Cheongpung tilted his head for a moment, then bowed to us. “If fate brings us together, we’ll meet again. Then I’ll be off.” I bid him farewell with deep regret. “Take care. And don’t forget the Jin Family of Taiyuan.” “Haha, of course I won’t.” He turned away with a hearty laugh. Thinking the conversation was over, the chief steward spoke. “Then I’ll escort you to the annex.” “Ah, yes. Mujin, let’s go.” “Oh! We get to sleep in the annex of the famous Honghwa Inn?” “We stayed in the annex at Phoenix Inn, too. Why are you acting like this is something new?” “What are you talking about? If Phoenix Inn is a young prodigy, then Honghwa Inn is a Peak master whose fame is already known. Its hot springs, in particular, are such a renowned attraction that even high officials and nobles visit them.” “Hot springs?” “I’ve only heard about them from rumors, but they say there’s no paradise like it.” The chief steward added calmly, “My father is turning eighty this year. He came here once and nearly departed for paradise.” “…Isn’t that dangerous?” “It only means the hot springs are that good. He’s still hale and hearty.” “Ah, I see. I hope he lives a long life.” Hot springs… I had gone to saunas plenty of times, but I had never visited a hot spring. Just thinking about sinking into pleasantly hot water already had me excited. “Ahem. Shall we go?” “I’ll escort you.” I was just about to follow the chief steward when a firm hand suddenly seized my shoulder. “Um. Did you just say hot springs?” “…You haven’t left yet?” Looking at Cheongpung’s sheepish grin, I was certain of one thing. I’d bet both my balls this bastard had never been to a hot spring. * * * In the early dawn, while darkness still lay thick over the estate’s training ground, a man was swinging a sword. He looked to be about thirty. His strong, rugged features were striking. *Swish, swish, swish!* He thrust, slashed, and swung without pause. Each form flowed smoothly into the next, like flower petals fluttering in the wind. As the Seven Plum Sword, in which he had reached eight-tenths mastery, cut through the chilly dawn air, a messenger opened the main gate and entered. “What is it? I forbade anyone from entering while I’m training.” “My apologies. But His Highness Prince Shangshan ordered me to deliver a message…” “His Highness?” “Yes. His Highness commands you to attend today’s luncheon at noon.” “The luncheon… You mean the gathering where the young prodigies of Murim are coming?” “Yes, sir.” The man let out a deep sigh. He was a Third-Rank Assistant Military Commissioner, an official who could easily be counted among the five highest-ranking figures in Shanxi Province. *I can’t refuse an order from His Highness. What a nuisance.* The position of Assistant Military Commissioner was by no means an idle one. It was a weighty office responsible for training the soldiers. But the order had come from Prince Shangshan, the City Lord and a man of royal blood. The man had no choice but to nod. “Tell His Highness that I accept the royal command.” “Yes, sir!” After the messenger departed, the man raised his sword once more. As he resumed the Seven Plum Sword, the plum blossoms of Huashan, which he had left long ago, seemed to bloom from his blade.

#### Chapter 137 tail (verified mastered)

…
prodigies of Murim, receive this royal command! I, the younger brother of the sacred Son of Heaven…” “Eek!” *Thud!* This time, the one who collapsed was a woman. The unexpected accident made the official’s breathing turn ragged for a moment. But he was the bearer of a royal command. He couldn’t let something so trivial throw him off. The official composed himself and took another breath. “I-I…” “Gasp!” *Thud!* “The command I bestow upon you…” “Eek!” *Thud!* This time, even the official couldn’t escape the disaster. Perhaps he had bitten his tongue, because a crunch came from his mouth, followed by blood streaming down his lips. The crowd fell silent, though for a different reason than before. As the official stood there in despair, one man strode confidently up to him and whispered, “Do we really have to do this outside? Why don’t we just do it inside?” The official considered Taekyung’s words for a moment before answering. “Let’sh do that.” “…Just nod. You’re getting blood on your clothes.” * * * The official spoke with a grave expression. “How on earth did this happen?” Everyone was watching me for a response. In the end, I had no choice but to explain the situation as briefly and clearly as possible. “The kids aren’t feeling well.” “Not feeling well? What do you mean?” “They’re the fresh young pillars of Murim, aren’t they? They trained so hard to become stronger that they wore themselves down. That’s why they keep collapsing.” “Is that really what happened?” “…” “…” It was quiet enough to hear a mouse breathe. I turned slightly and asked, “He’s asking whether that’s true. Did you not hear him?” The four young prodigies of the Five Gates of Shanxi jolted as though they had seen a ghost. “O-oh, no. We heard him. We were just thinking of an answer…” “Th-that’s right. I thought someone else would answer…” “What is there to think about? Just tell him the truth. Isn’t that right? Hahaha.” Of course, if they told the truth, they would get some private one-on-one time with me. The law was far away, and fists were close at hand. If the four of them wanted to keep living peacefully in Shanxi Murim, they had no choice but to stay on the Jin Family of Taiyuan’s good side. They forced the corners of their mouths upward. “Well, that’s what happened.” The official looked dubious as he asked another question. “But why is one person missing? As I understand it, there should be six of you, including Young Hero Jin.” “Ah, you mean the Young Bureau Head of the Seongun Escort Bureau.” “That must be him. His name was…” “Jintae. Woo Jintae.” “That’s right. Why hasn’t he come out?” *Because that one is in no condition to look human.* If I had known from the start that the Five Gates of Shanxi’s young prodigies had been invited to this luncheon with me, I wouldn’t have beaten him quite so badly. *Well, what’s done is done.* All I could do was clean up the mess as best I could. I shook my head with the most sympathetic expression I could manage. “Last night, he was injured in a minor altercation and still hasn’t regained consciousness.” “An altercation? Are you saying he got into a fistfight?” “Something like that. In any case, his face is in such a state that he simply can’t appear in front of people.” “Good heavens. What kind of fiend would do that to a guest invited by His Highness?” “…” This felt really strange. With the culprit standing right in front of him, the official muttered something about treason, then lamented. “This is a serious matter. Whatever the reason, the fact remains that he can’t attend the invitation. How furious will His Highness be when he learns of this?” “Could I perhaps explain things to him properly?” “Young Master, you don’t understand. Once His Highness takes offense, no one can stop him. The surrounding area will be turned into a wasteland for the time being.” “Turned into a wasteland? What do you mean by that?” “What else could I mean? First, they’ll arrest and severely punish the man who injured the Young Bureau Head of the Seongun Escort Bureau. Then, citing the terrible state of public order, dozens of officials will be forced to resign. I’ll probably be one of them.” “…” Why would they take it that far? The official, who looked like he was about to be laid off in the prime of his life, added the finishing touch with a tragic expression. “I have more than ten family members to feed… Sigh. I can only blame the heavens.” *He has a big family, too.* I was squirming in my seat and desperately racking my brain when— “Yaaawn.” A carefree yawn, completely at odds with the mood. My eyes lit up when I saw someone coming downstairs with a long stretch. “Hey, how about this?” “Hm? What do you mean?” “If we bring along an even more impressive young prodigy, there won’t be a problem. Right?” “I can’t be certain, but that’s probably true. His Highness wouldn’t complain if you found someone even more outstanding.” Perfect. With a triumphant smile, I waved at Cheongpung. He was a young prodigy who was no less than a Peak master. “Have you ever seen a member of the imperial family?”

## Korean source

```text
＃138화



호화로운 육두마차는 거침없이 질주했다.

척 봐도 정예로 보이는 군사들이 앞에서 길을 텄고, 개미처럼 바글바글하던 사람들은 양옆으로 쫙 갈라서서 바람처럼 달려가는 마차를 지켜봤다.

“모세가 이런 기분이었구나.”

내 중얼거림에 청풍이 반응했다.

“모세요? 그게 뭡니까?”

“있어요, 그런 사람이.”

“아, 네.”

혁무진이었다면 또 이상한 소릴 한다며 한참을 투덜거렸겠지만, 청풍은 달랐다.

그는 놀이동산에 온 어린애처럼 신난 얼굴로 마차 이곳저곳을 누르고 두드렸다.

“육두마차는 난생처음 타 봅니다!”

“……사두마차는요?”

“사두마차도 안 타 봤어요!”

“그냥 마차는…….”

“그냥 마차도 타 보고 싶습니다!”

“…….”

지하철이라도 태워 주면 기절하겠는데.

이쯤 되면 안 해 본 걸 세는 것보다 해 본 걸 세는 게 훨씬 빠르겠다.

나는 흥분 상태에 접어든 청풍을 물끄러미 바라봤다.

‘이거 도대체 뭐 하는 놈이야?’

얘를 순수하다고 해야 할지, 멍청하다고 해야 할지.

하긴, 평생을 산에서 살았다고 하니 어쩌면 당연한 것일지도 모른다.

‘다루기가 쉬워서 좋기도 하고.’

방금 그 표정이 잊히지 않는다. 황족이라는 한 단어에 쌍라이트가 번쩍하던 눈동자도.



‘혹시 황족 본 적 있어요?’

‘볼래요! 보겠습니다! 보게 해 주세요!’



그의 눈에 담겼던 건 일반적인 양민들이 가지는 황실에 대한 동경 같은 것이 아니었다. 굳이 따지자면 동물원 코끼리를 보러 가는 설렘이랄까.

‘진짜 특이한 놈일세.’

나만 그렇게 생각하는 건 아닌가 보다.

중상인 우진태를 제외한 산서오문의 후기지수들도 해괴한 것을 보는 듯한 표정으로 청풍을 바라보고 있었다.

“어째 상태가 좀…….”

“정말 이대로 가도 되는 거야?”

“괜히 전하 앞에서 말실수라도 하면 우리까지 피 볼 것 같은데.”

“말실수로 끝나면 다행이지. 황족 처음 봐서 신기하다고 귀라도 잡아당기면 그날로 끝이야, 끝.”

……제법 그럴듯한 추측인데?

후기지수들의 수군거림에 함께 마차에 타고 있던 관리도 불안한 얼굴로 귓속말을 건넸다.

“저기, 진 공자.”

“네?”

“저 사람…… 정말 괜찮은 것 맞소?”

“믿으십쇼. 제가 보증하는 고수라니까요.”

“아니, 고수고 나발이고 정신이 괜찮냐는 말이오.”

“아.”

“차라리 공자와 함께 있던 그 무사를 데려오는 게 더 낫지 않겠소?”

“누구, 아 혁무진이요?”

“그런 이름이었던 것 같소. 내 듣자 하니 그 무사도 상당한 무공의 소유자라던데.”

혁무진이 들었다면 좋아서 펄쩍 뛰었을 얘기다.

문제는 아침에 나한테 맞은 덕분에 얼굴에 시퍼런 멍이 들어 도저히 함께 갈 수 없다는 거지만.

‘그리고 혁무진 정도로는 안 돼.’

어린 왕의 심기를 거스르지 않게 하려면 보다 큰 선물을 가져가야 한다.

나는 걱정하는 관리를 향해 단호하게 고개를 저어 보였다.

“걱정 마십시오. 문제 안 생기도록 제가 책임지고 단속하겠습니다.”

내가 누군가, 명망 높은 태원진가의 직계이자 떠오르는 샛별, 산서 무림의 라이징 스타다.

내 호언장담에 관리의 얼굴이 약간 밝아졌다.

“그럼 본인은 진 공자만 믿겠…….”

우둑.

“……?”

“……?”

잠깐만. 이게 무슨 소리야.

약속이라도 한 듯이 동시에 고개를 돌린 우리의 시선에, 뭔가를 움켜쥐고 있는 청풍이 보였다.

“어, 이게 왜 떨어졌지?”

매우 정교하게 만들어진 황금 용을 들고 헤헤 웃는 녀석의 모습에 한참 침묵하던 관리가 나를 바라봤다.

“진 공자.”

“네.”

“정말 괜찮은 것 맞소?”

나는 고민 끝에 입을 열었다.

“아마도요.”



* * *



저택이 아니라 성(城)이라고 해도 될 만큼 드넓은 공간. 사내의 발걸음은 거침없었다.

굳게 다문 입술과 강건한 눈빛을 마주한 이들은 하나같이 공손히 예를 표했다.

“첨사 어른을 뵙습니다.”

그는 고개를 끄덕이는 것으로 인사를 대신하고 걸음을 재촉했다.

기둥들이 끝없이 늘어선 회랑(回廊)을 지나고 얼마나 걸었을까? 용이 음각된 거대한 철문이 나타나고서야 사내의 발걸음이 멈췄다.

“아뢰게.”

“충.”

그를 향해 군례를 취한 호위군 소속의 장수가 힘차게 외쳤다.

“산서성 도지휘첨사(都指揮僉事), 이풍(李灃) 영감 듭시오!”

얼마 지나지 않아 그에 응답하는 목소리가 들려왔다.

“들라 하라.”

“……!”

어린아이처럼 앳되지도, 그렇다고 장성한 사내처럼 굵지도 않은 목소리.

뭔가를 짐작한 사내, 이풍의 눈썹이 솟구친 그때, 육중한 소리와 함께 철문이 열렸다.

그그긍.

그곳은 호화롭게 치장된 대전(大殿)이었다. 사방이 금은보화로 번쩍거렸고 수십 명이 앉아도 될 만큼 넓은 탁자는 온갖 산해진미로 가득 차 있었다.

다른 사람이라면 입을 딱 벌렸을 만한 광경. 그러나 이풍의 시선은 한곳에 못 박혀 떠날 줄을 몰랐다.

‘저자가 어찌.’

이풍의 시선 끝, 탁자의 상석(上席)에 앉아 있던 한 사람이 빙긋 웃었다.

눈이 부실 만큼 화려한 붉은 비단으로 몸을 휘감은 사내의 입에서 간드러진 목소리가 흘러나왔다.

“이게 누구야, 우리 이 첨사 아니에요?”

우리 이 첨사?

이풍은 지그시 입술을 깨물며 군례를 취했다.

“……도지휘동지(都指揮同知)를 뵙습니다.”

도지휘동지는 종이품으로 각 성에 두 명밖에 없는 고위직.

군 총사령관인 도지휘사와 성주인 상산왕을 제외하면 가장 높은 직책이며, 부사령관인 만큼 실권 또한 막강했다.

실제로 알려진 것은 이러하지만, 눈앞의 사내가 가진 권한은 그 이상이었다.

‘쳐 죽일 놈 같으니.’

간사한 혓바닥과 잔재주로 어린 왕의 눈과 귀를 가리고 제 배만 채우는 간신이자 탐관오리. 그것이 사내에 대한 이풍의 평가였다.

그러나 이풍의 곱지 않은 눈길에도 그의 웃음은 여전했다.

“이 첨사, 오랜만에 보는데 분위기가 너무 험악한 거 아니에요? 혹시 내가 뭐 섭섭하게 한 거라도?”

“……그럴 리가 있습니까. 저는 그저 도지휘동지께서 이런 자리에 계신 것이 뜻밖이라 놀란 것뿐입니다.”

“이런 자리라니?”

“강호의 무부(武夫)들이 모이는 자리입니다. 워낙 거친 자들이라 도지휘동지께서 불편하시지 않을까 염려되는군요.”

말은 위해 주는 것 같지만 속뜻은 다르다. 두 사람 모두 그 사실을 모르지 않았다.

“왜요? 나 이런 자리 좋아해. 그리고 아까부터 호칭이 너무 딱딱하다. 그냥 편하게 불러요. 우리 사이인데 뭐 어때.”

“우리 사이라…… 그게 무슨 사입니까?”

“콩 한 쪽도 나눠 먹는 사이. 전하를 충심으로 보필하는 참된 신하들이지요.”

콩 한 쪽도 나눠 먹어? 참된 신하?

사내의 말에 이풍이 무뚝뚝하게 물었다.

“그럼 편하게 홍 내관이라고 부르면 되겠습니까?”

사내, 홍 내관의 웃음이 순간 경직됐다.

이풍은 고작 한 단어로 그의 역린을 건드렸다.

“그건…… 너무 편한데?”

“저야 말씀을 따른 것뿐입니다.”

“이거 참, 이 첨사가 나를 그 정도로 편하게 생각하는지는 몰랐네.”

“이제라도 제 마음을 알아주시니 몸 둘 바를 모르겠군요.”

“이 첨사.”

“부르셨습니까, 홍 내관. 아니, 다시 도지휘동지라고 불러 드릴까요?”

무겁게 내려앉은 정적.

홍 내관의 입이 다시금 열린 것은 한참 후였다.

“우리 이 첨사, 많이 늘었다?”

“그렇습니까?”

“응, 몇 년 전에 비하면 일취월장했는데?”

“덕분에 여러 가지 배웠습니다.”

“검만 잘 쓰는 줄 알았는데, 오늘 보니 혀도 잘 쓰네. 다시 봤어요.”

“누구보다는 아직 한참 모자랍니다.”

두 사람의 시선이 허공에서 부딪쳤다. 팽팽하게 조여진 공기 속에서 홍 내관이 부드럽게 웃었다.

“뭐, 이 이야기는 나중에 하고…… 내가 뭐 하나만 물어봐도 되려나?”

만만치 않은 상대가 한발 물러났다. 여기서 더 물어뜯었다가는 되레 낭패만 볼 뿐이다. 이풍은 묵묵히 고개를 끄덕였다.

“하문하십시오.”

“이 첨사가 전에 화산파에 있었다고 했죠?”

이풍이 멈칫했다. 그에게 있어 화산파는 그리우면서도 아픈 기억이다.

화산을 떠난 지 이제 어언 십 년이지만 그곳에서의 기억은 여전히 몸과 마음 깊숙이 남아 있었다.

“예. 속가제자였습니다.”

“화산파는 섬서에 있고?”

그와 홍 내관은 이른바 정적(政敵)이라 할 수 있는 관계였다. 그만큼 오히려 속속들이 잘 알았다.

홍 내관은 이런 기본적인 사실을 몰라서 물어볼 만큼 허술하지도, 멍청하지도 않았다.

오히려 속에 구렁이가 백 마리는 득실거리는 교활한 놈이다.

그렇기에 이풍은 더욱 의아함을 느꼈다.

“맞습니다. 그런데 갑자기 그건 왜 물어보시는지?”

“내가 이번에 알게 된 지인이 몇 분 있는데, 혹시 이 첨사도 알까 싶어서.”

“무림인입니까?”

“맞아요. 그것도 섬서 출신.”

“설마 화산……?”

“에이, 그럼 내가 미리 말을 했겠지.”

이풍은 안도의 한숨을 내쉬었다.

결국, 스스로 떠나오긴 했지만 평생을 자랑스러워할 사문(師門)이다. 홍 내관 같은 간신배와 엮이지 않았다는 사실이 천만다행이었다.

“섬서에 문파가 한둘도 아니고, 저도 본산에서 수련하는 중에는 바깥출입을 하지 않았기 때문에 이름을 들어도 잘 모릅니다.”

“그런가? 그럼 얼굴을 보면 알 수도 있겠네?”

“……?”

이풍의 표정을 본 홍 내관이 탁자에 놓인 젓가락을 집어 들었다.

“아까 이 첨사가 물어봤었죠? 내가 왜 이런 자리에 있냐고.”

아름답게 세공된 은 젓가락이 술잔을 두드렸다.

팅. 맑은 소리가 멀리 퍼져 나갔다. 어리둥절한 이풍에게 홍 내관이 눈웃음을 지어 보였다.

“지인을 몇 분 초대했거든. 전하께서 좋아하실 만큼 명성 높고 강한 무인들로.”

동시에 철문 밖에서 힘찬 외침이 들려왔다.

“섬서의 종남삼수(終南三手)가 뵙기를 청합니다!”

“종남삼수…… 종남파!”

이풍의 안색이 급변했다.

화산파와 종남파는 장장 백 년간 섬서의 패권을 다퉈 온 앙숙 관계.

홍 내관의 의도는 지금 짓고 있는 웃음만큼이나 환하기 그지없었다.

“같은 섬서 사람이라 자리를 마련해 봤어요. 괜찮죠?”

이풍이 주먹을 불끈 움켜쥔 그때, 거대한 철문이 열리고 대전 안으로 장대한 체구의 세 사람이 성큼 들어왔다.

그중에 낯익은 얼굴 하나가 끼어 있었다.

“이게 누구야. 화산파의 이풍 아닌가?”

이풍은 몸을 부르르 떨었다. 놈의 얼굴을 본 순간 십 년 전의 그 치욕스러운 기억이 떠올랐기 때문이었다.

“네가 여길 어떻게!”

날카로운 눈매의 사내가 천연덕스럽게 대답했다.

“어떻게 오긴. 산서성의 도지휘동지께서 불러 주시는데 천 리라도 한달음에 달려와야지. 안 그렇습니까?”

“별말씀을. 오히려 초대에 응해 주셔서 감사할 따름이에요.”

으드득, 이를 가는 이풍을 향해 종남삼수의 셋째, 공일혁이 씩 웃어 보였다.

“그나저나 출세했네. 자네 주제에 도지휘첨사라…… 화산에서 은자깨나 뿌렸겠어. 응?”

“네놈이 감히 화산파를 모욕해?”

“응? 화산파를 모욕한 건 자네지. 십 년 전, 그 대단한 화산 무공으로 백여 초 만에 무릎을 꿇은 게 누구였나?”

“이놈-!”

이풍의 입에서 벼락같은 외침이 터져 나왔다.

그가 화염이 줄기줄기 쏟아지는 눈동자로 공일혁을 노려보던 그 순간. 철문 밖에서 세 번째 외침이 들려왔다.

“산서 무림의 후기지수들이 뵙기를 청합니다!”
```

## Current accepted English baseline

```markdown
# Chapter 138

The luxurious six-horse carriage raced onward without slowing.

Soldiers who looked like elite troops cleared the road ahead, while the people who had been swarming around like ants split neatly to either side and watched the carriage dash past like the wind.

“So this is how Moses felt.”

Cheongpung reacted to my mutter.

“Moses? Who is that?”

“Someone.”

“Oh, I see.”

If it had been Hyuk Mujin, he would have complained for ages about me saying something strange, but Cheongpung was different.

He had the excited expression of a child at an amusement park as he pressed and tapped every part of the carriage.

“This is my first time riding in a six-horse carriage!”

“…What about a four-horse carriage?”

“I’ve never ridden in one of those, either!”

“What about an ordinary carriage…?”

“I’d like to ride in one of those, too!”

“…”

If I put him on a subway, he would probably faint.

At this point, it would be much faster to count the things he had done than the things he had never done.

I stared at Cheongpung, who had entered a state of total excitement.

*What the hell is this guy?*

Was he innocent or stupid?

Then again, he had said he had lived his entire life in the mountains. Maybe this was only natural.

*At least he’s easy to handle.*

I still couldn’t forget the expression he had just made. His eyes had lit up like high beams at the mere mention of the imperial family.

*“Have you ever seen a member of the imperial family?”*

*“I want to! I’ll see one! Please let me see one!”*

What filled his eyes wasn’t the sort of admiration ordinary commoners felt toward the imperial family. If I had to compare it to something, it was more like the excitement of going to see an elephant at the zoo.

*He really is a strange one.*

Apparently, I wasn’t the only one who thought so.

The young prodigies of the Five Gates of Shanxi, excluding the severely injured Woo Jintae, were staring at Cheongpung as if they were looking at something bizarre.

“Is he really all right…?”

“Can we really go like this?”

“If he says something inappropriate in front of His Highness, we might get dragged into it, too.”

“It’ll be lucky if it ends with him saying something inappropriate. If he gets excited about seeing an imperial family member for the first time and pulls on his ear, we’re finished. Completely finished.”

…That was a surprisingly plausible prediction.

Hearing the young prodigies whispering, the official riding in the carriage with us leaned over and spoke in an anxious voice.

“Um, Young Master Jin.”

“Yes?”

“That person… Is he really all right?”

“Believe me. He’s a master I can vouch for.”

“To hell with whether he’s a master. I’m asking whether he’s right in the head.”

“Oh.”

“Wouldn’t it be better to bring along the martial artist who was with you instead?”

“Who? Ah, Hyuk Mujin?”

“I believe that was his name. I hear he’s also quite skilled in martial arts.”

If Mujin had heard that, he would have jumped for joy.

The problem was that he had a dark blue bruise on his face from getting beaten by me that morning, so there was no way he could come along.

*And Hyuk Mujin wouldn’t be enough.*

To avoid offending the young prince, I needed to bring a more impressive gift.

I firmly shook my head at the worried official.

“Don’t worry. I’ll take responsibility for making sure nothing happens.”

Who was I? A direct descendant of the prestigious Jin Family of Taiyuan, a rising star, and Shanxi Murim’s newest sensation.

My bold assurance brightened the official’s expression a little.

“Then I’ll trust Young Master Jin—”

*Crack.*

“…?”

“…?”

Wait a second. What was that sound?

As though we had made a pact, we all turned our heads at the same time.

There was Cheongpung, clutching something in his hands.

“Huh? Why did this fall off?”

The official stared at me in silence for a long moment as Cheongpung grinned foolishly while holding an exquisitely crafted golden dragon.

“Young Master Jin.”

“Yes?”

“Is he really all right?”

After thinking it over, I opened my mouth.

“Probably.”

* * *

The space was so vast that it could have been called a castle rather than a residence. A man strode through it without hesitation.

Everyone who saw his tightly pressed lips and resolute gaze respectfully paid their respects.

“Greetings, Assistant Military Commissioner.”

He acknowledged them with a nod and quickened his pace.

After passing through a corridor lined with endless pillars, how long had he been walking? The man finally stopped when a massive iron gate engraved with a dragon appeared before him.

“Announce me.”

“Yes, sir.”

A commander from the palace guard saluted him and called out in a powerful voice.

“His Excellency Li Feng, Assistant Military Commissioner of Shanxi Province, entering!”

Before long, a voice answered from within.

“Let him enter.”

“…”

The voice was neither as high and childish as a little boy’s nor as deep as a grown man’s.

At the moment the man—Li Feng—seemed to realize something and his eyebrows shot up, the iron gate opened with a heavy groan.

*Grrrnnng.*

Beyond it was an extravagantly decorated grand hall. Gold and silver treasures glittered in every direction, and a table large enough for dozens of people was covered with every delicacy from land and sea.

It was a sight that would have left anyone else gaping. But Li Feng’s gaze remained fixed on a single point.

*How is he here?*

At the end of Li Feng’s gaze, a man seated at the head of the table smiled faintly.

Wrapped in dazzling red silk, the man spoke in a coy, lilting voice.

“Well, well. If it isn’t our Assistant Commissioner Li.”

*Our Assistant Commissioner Li?*

Li Feng bit down on his lips and performed a military salute.

“…Greetings, Deputy Military Commissioner.”

The Deputy Military Commissioner was a second-rank official, with only two such posts in each province.

Aside from the Military Commissioner, who was the commander-in-chief, and the City Lord, Prince Shangshan, it was the highest position there was. As the deputy commander, he also wielded tremendous authority.

That was what people knew publicly. In truth, the man before him possessed even greater power.

*That bastard deserves to be beaten to death.*

A sycophant and corrupt official who used his glib tongue and petty tricks to blind the young prince’s eyes and ears while lining his own pockets. That was Li Feng’s assessment of him.

But even beneath Li Feng’s openly hostile gaze, the man continued smiling.

“Assistant Commissioner Li, it’s been a while. Isn’t the atmosphere a little too tense? Did I perhaps do something to offend you?”

“…Of course not. I was merely surprised to find you in a place like this, Deputy Military Commissioner.”

“A place like this?”

“It is a gathering of martial artists from the martial world. They are rather rough people, so I was concerned that you might be uncomfortable, Deputy Military Commissioner.”

His words sounded considerate, but their true meaning was different. Neither man was unaware of that.

“What’s the problem? I like places like this. Besides, you’ve been so stiff with your title since a while ago. Just call me whatever you like. We’re close enough, aren’t we?”

“Close enough for what, exactly?”

“We’re the kind of people who would split a bean between us. True loyal subjects who serve His Highness with all our hearts.”

*Split a bean between us? True loyal subjects?*

Li Feng asked bluntly,

“Then may I call you Eunuch Hong?”

The smile on Eunuch Hong’s face stiffened for a moment.

With a single word, Li Feng had touched his sore spot.

“That’s… a little too familiar, don’t you think?”

“I only followed your instructions.”

“Well, this is something. I didn’t realize Assistant Commissioner Li considered me that close.”

“I’m overwhelmed that you understand my feelings at last.”

“Assistant Commissioner Li.”

“Did you call, Eunuch Hong? Or should I go back to calling you Deputy Military Commissioner?”

A heavy silence settled over the hall.

It was a long while before Eunuch Hong opened his mouth again.

“Our Assistant Commissioner Li has improved quite a bit, hasn’t he?”

“Have I?”

“Yes. Compared to a few years ago, you’ve made remarkable progress.”

“I’ve learned many things thanks to you.”

“I thought you were only good with a sword, but now I see you’re good with your tongue, too. I’ll have to look at you differently.”

“I’m still nowhere near as skilled as someone else.”

Their gazes collided in midair. Within the tightly stretched silence, Eunuch Hong smiled gently.

“Well, we can talk about that later… May I ask you one thing?”

His opponent was no pushover, but he had taken a step back. If he kept biting at him, he would only end up at a disadvantage. Li Feng silently nodded.

“Ask.”

“You said you used to belong to Huashan, didn’t you?”

Li Feng paused. Huashan was a place he both missed and remembered with pain.

It had been nearly ten years since he had left Mount Hua, but the memories of that time still remained deep in his body and heart.

“Yes. I was a lay disciple.”

“And Huashan is in Shaanxi?”

He and Eunuch Hong were what one might call political enemies. For that very reason, they knew one another inside and out.

Eunuch Hong was neither careless nor stupid enough to ask about such a basic fact without a reason.

If anything, he was a crafty man with a hundred snakes writhing inside him.

That was why Li Feng was even more puzzled.

“That’s right. But why are you suddenly asking?”

“I’ve come to know a few people recently, and I wondered if you might know them, too.”

“Are they martial artists?”

“Yes. And they’re from Shaanxi.”

“Don’t tell me they’re from Huashan…?”

“Oh, come on. If they were, I would have told you already.”

Li Feng let out a sigh of relief.

In the end, he had left of his own accord, but Huashan was still the sect he would be proud of for the rest of his life. It was a tremendous relief that he had not been entangled with a sycophant like Eunuch Hong.

“There are more than one or two sects in Shaanxi. And I didn’t go outside while training at the main sect, so even if I heard their names, I might not recognize them.”

“Is that so? Then perhaps you would recognize them if you saw their faces?”

“…?”

Seeing Li Feng’s expression, Eunuch Hong picked up the chopsticks lying on the table.

“You asked earlier why I was here, didn’t you?”

The beautifully crafted silver chopsticks tapped against a wine cup.

*Ping.*

The clear sound spread through the hall.

Eunuch Hong gave the bewildered Li Feng a knowing smile.

“I invited a few acquaintances. Famous and powerful martial artists whom His Highness would enjoy meeting.”

At that moment, a powerful shout rang out from beyond the iron gate.

“The Three Hands of Zhongnan request an audience!”

“The Three Hands of Zhongnan… The Zhongnan Sect!”

Li Feng’s complexion changed drastically.

Huashan and the Zhongnan Sect had been bitter rivals fighting for supremacy in Shaanxi for a full hundred years.

Eunuch Hong’s intentions were every bit as clear as the smile on his face.

“They’re from Shaanxi, so I thought I’d arrange a gathering. Isn’t that nice?”

Just as Li Feng clenched his fists, the massive iron gate opened and three imposing men strode into the hall.

One of them had a familiar face.

“Well, well. If it isn’t Li Feng of Huashan?”

Li Feng’s body trembled. The moment he saw that man’s face, the humiliating memory from ten years ago came rushing back.

“How did you get here?”

The sharp-eyed man answered casually.

“How did I get here? When the Deputy Military Commissioner of Shanxi Province invites you, you have to come running even if it’s a thousand li away. Isn’t that right?”

“There’s no need to thank me. I’m the one grateful that you accepted the invitation.”

*Grind.*

Gong Ilhyuk, the third of the Three Hands of Zhongnan, grinned at Li Feng as he ground his teeth.

“Anyway, you’ve done well for yourself. Assistant Military Commissioner, someone like you… Huashan must have spread around quite a bit of silver for you. Hmm?”

“How dare you insult Huashan?”

“Insult Huashan? You’re the one who insulted it. Ten years ago, who was it that knelt after a little over a hundred exchanges against that magnificent Huashan martial arts?”

“You bastard!”

A thunderous shout burst from Li Feng’s mouth.

At the moment he glared at Gong Ilhyuk with eyes that seemed to pour out streams of flame, a third shout rang out from beyond the iron gate.

“The young prodigies of Shanxi Murim request an audience!”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 138`.

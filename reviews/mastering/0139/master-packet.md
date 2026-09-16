# Master Edit Task — Chapter 139

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
| 위팽     | **Wipeng**         |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 산서오문   | **Five Gates of Shanxi**         |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 레벨               | **Level**                      |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 이풍 | 진태경 | senior_official_to_respected_young_martial_artist | Young Hero Jin | formal and respectful | Addresses Taekyung as 진 소협 after praising his reputation. |
| 이풍 | 청풍 | Huashan lay disciple to martial uncle | Young Hero; Martial Uncle Cheongpung | formal and reverent | Li Feng initially addresses Cheongpung as 소협 while testing his knowledge, then recognizes him as 사숙 after witnessing his Huashan sword technique. |
| 청풍 | 이풍 | Martial Uncle to Martial Nephew | Martial Nephew Li Feng | exuberant and deferential | Cheongpung adopts the address to obtain royal-guard armor and weapons. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 진태경 | 이풍 | junior_to_respected_official_and_martial_ally | Great Hero Li | polite and respectful | Agrees with Li Feng's proposal that Zhu Bao visit the Jin Family's banquet. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 진위경 | 홍진 | political_host_to_deputy_military_commissioner | Comrade Hong | formal-polite and playful | Jin Wikyung adopts Hong Jin's requested casual address, 홍 동지. |
| 홍진 | 진위경 | deputy_military_commissioner_to_lesser_family_head | Lesser Family Head Jin | formal and teasing | Hong Jin addresses Jin Wikyung as 진 소가주님 while flattering and joking with him. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 위팽 | 진태경 | retainer_to_third_young_master | Third Young Master | formal-polite and admonishing | Uses 삼공자 while warning Taekyung to return by noon and behave respectfully toward Jang Taebo. |
| 위팽 | 청풍 | Jin Family retainer to visiting Huashan martial artist | Young Hero Cheongpung | formal-polite and worried | Uses 청 소협 while warning that Cheongpung's refusal of the Sect Leader's order could strain relations between the Jin Family and Huashan. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |

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

#### Chapter 137 tail (verified mastered)

…
prodigies of Murim, receive this royal command! I, the younger brother of the sacred Son of Heaven…” “Eek!” *Thud!* This time, the one who collapsed was a woman. The unexpected accident made the official’s breathing turn ragged for a moment. But he was the bearer of a royal command. He couldn’t let something so trivial throw him off. The official composed himself and took another breath. “I-I…” “Gasp!” *Thud!* “The command I bestow upon you…” “Eek!” *Thud!* This time, even the official couldn’t escape the disaster. Perhaps he had bitten his tongue, because a crunch came from his mouth, followed by blood streaming down his lips. The crowd fell silent, though for a different reason than before. As the official stood there in despair, one man strode confidently up to him and whispered, “Do we really have to do this outside? Why don’t we just do it inside?” The official considered Taekyung’s words for a moment before answering. “Let’sh do that.” “…Just nod. You’re getting blood on your clothes.” * * * The official spoke with a grave expression. “How on earth did this happen?” Everyone was watching me for a response. In the end, I had no choice but to explain the situation as briefly and clearly as possible. “The kids aren’t feeling well.” “Not feeling well? What do you mean?” “They’re the fresh young pillars of Murim, aren’t they? They trained so hard to become stronger that they wore themselves down. That’s why they keep collapsing.” “Is that really what happened?” “…” “…” It was quiet enough to hear a mouse breathe. I turned slightly and asked, “He’s asking whether that’s true. Did you not hear him?” The four young prodigies of the Five Gates of Shanxi jolted as though they had seen a ghost. “O-oh, no. We heard him. We were just thinking of an answer…” “Th-that’s right. I thought someone else would answer…” “What is there to think about? Just tell him the truth. Isn’t that right? Hahaha.” Of course, if they told the truth, they would get some private one-on-one time with me. The law was far away, and fists were close at hand. If the four of them wanted to keep living peacefully in Shanxi Murim, they had no choice but to stay on the Jin Family of Taiyuan’s good side. They forced the corners of their mouths upward. “Well, that’s what happened.” The official looked dubious as he asked another question. “But why is one person missing? As I understand it, there should be six of you, including Young Hero Jin.” “Ah, you mean the Young Bureau Head of the Seongun Escort Bureau.” “That must be him. His name was…” “Jintae. Woo Jintae.” “That’s right. Why hasn’t he come out?” *Because that one is in no condition to look human.* If I had known from the start that the Five Gates of Shanxi’s young prodigies had been invited to this luncheon with me, I wouldn’t have beaten him quite so badly. *Well, what’s done is done.* All I could do was clean up the mess as best I could. I shook my head with the most sympathetic expression I could manage. “Last night, he was injured in a minor altercation and still hasn’t regained consciousness.” “An altercation? Are you saying he got into a fistfight?” “Something like that. In any case, his face is in such a state that he simply can’t appear in front of people.” “Good heavens. What kind of fiend would do that to a guest invited by His Highness?” “…” This felt really strange. With the culprit standing right in front of him, the official muttered something about treason, then lamented. “This is a serious matter. Whatever the reason, the fact remains that he can’t attend the invitation. How furious will His Highness be when he learns of this?” “Could I perhaps explain things to him properly?” “Young Master, you don’t understand. Once His Highness takes offense, no one can stop him. The surrounding area will be turned into a wasteland for the time being.” “Turned into a wasteland? What do you mean by that?” “What else could I mean? First, they’ll arrest and severely punish the man who injured the Young Bureau Head of the Seongun Escort Bureau. Then, citing the terrible state of public order, dozens of officials will be forced to resign. I’ll probably be one of them.” “…” Why would they take it that far? The official, who looked like he was about to be laid off in the prime of his life, added the finishing touch with a tragic expression. “I have more than ten family members to feed… Sigh. I can only blame the heavens.” *He has a big family, too.* I was squirming in my seat and desperately racking my brain when— “Yaaawn.” A carefree yawn, completely at odds with the mood. My eyes lit up when I saw someone coming downstairs with a long stretch. “Hey, how about this?” “Hm? What do you mean?” “If we bring along an even more impressive young prodigy, there won’t be a problem. Right?” “I can’t be certain, but that’s probably true. His Highness wouldn’t complain if you found someone even more outstanding.” Perfect. With a triumphant smile, I waved at Cheongpung. He was a young prodigy who was no less than a Peak master. “Have you ever seen a member of the imperial family?”

#### Chapter 138 tail (verified mastered)

…
His Highness with all our hearts.” *Split a bean? True and loyal subjects?* Li Feng asked bluntly, “Then may I call you Eunuch Hong?” Eunuch Hong’s smile stiffened for a moment. With that single word, Li Feng had touched his sore spot. “That’s… a little too familiar, don’t you think?” “I only followed your instructions.” “Well, this is a surprise. I had no idea Assistant Commissioner Li considered me that close.” “I’m overwhelmed that you finally understand how I feel.” “Assistant Commissioner Li.” “Did you call, Eunuch Hong? Or would you prefer that I go back to calling you Deputy Military Commissioner?” A heavy silence settled over the hall. It was a long while before Eunuch Hong spoke again. “Our Assistant Commissioner Li has improved quite a bit, hasn’t he?” “Have I?” “Yes. Compared to a few years ago, you’ve made remarkable progress.” “I’ve learned many things thanks to you.” “I thought you were only good with a sword, but now I see you’re good with your tongue, too. I’ll have to look at you differently.” “I’m still nowhere near as skilled as a certain someone.” Their gazes collided in midair. Amid the taut silence, Eunuch Hong smiled gently. “Well, we can talk about that later… May I ask you one thing?” His opponent was no pushover, but he had taken a step back. If Li Feng kept biting at him, he would only put himself at a disadvantage. He silently nodded. “Ask.” “You said you used to belong to Huashan, didn’t you?” Li Feng paused. Huashan was a place he both missed and remembered with pain. It had been nearly ten years since he had left Mount Hua, but the memories of that time still remained deep in his body and heart. “Yes. I was a lay disciple.” “And Huashan is in Shaanxi?” He and Eunuch Hong were what one might call political enemies. For that very reason, they knew one another inside and out. Eunuch Hong was neither careless nor stupid enough to ask about such a basic fact without a reason. If anything, he was a crafty bastard with a hundred snakes writhing inside him. That only made Li Feng more puzzled. “That’s right. But why are you suddenly asking?” “I’ve come to know a few people recently, and I wondered if you might know them, too.” “Are they martial artists?” “Yes. From Shaanxi, no less.” “Don’t tell me they’re from Huashan…?” “Oh, come on. If they were, I would have told you already.” Li Feng sighed in relief. In the end, he had left of his own accord, but Huashan was still the sect he would be proud of for the rest of his life. It was a tremendous relief that Huashan had not become entangled with a sycophant like Eunuch Hong. “There are more than one or two sects in Shaanxi. And I didn’t go outside while training at the main sect, so even if I heard their names, I might not recognize them.” “Is that so? Then perhaps you would recognize them if you saw their faces?” “…?” At the sight of Li Feng’s expression, Eunuch Hong picked up the chopsticks lying on the table. “You asked earlier why I was here, didn’t you?” The beautifully crafted silver chopsticks tapped against a wine cup. *Ping.* The clear sound spread through the hall. Eunuch Hong smiled with his eyes at the bewildered Li Feng. “I invited a few acquaintances. Famous and powerful martial artists whom His Highness would enjoy meeting.” At that moment, a powerful shout rang out from beyond the iron gate. “The Three Hands of Zhongnan request an audience!” “The Three Hands of Zhongnan… The Zhongnan Sect!” Li Feng’s complexion changed drastically. Huashan and the Zhongnan Sect had been bitter rivals fighting for supremacy in Shaanxi for a full hundred years. Eunuch Hong’s intentions were every bit as clear as the smile on his face. “They’re fellow Shaanxi men, so I thought I’d arrange a gathering. You don’t mind, do you?” Just as Li Feng clenched his fists, the massive iron gate opened and three imposing men strode into the hall. One of them had a familiar face. “Well, well. If it isn’t Li Feng of Huashan?” Li Feng shuddered. The moment he saw that man’s face, the humiliating memory from ten years ago came rushing back. “How did you get here?” The sharp-eyed man answered casually. “How else? When the Deputy Military Commissioner of Shanxi Province invites you, you have to come running even if it’s a thousand li away. Isn’t that right?” “You’re too kind. I’m the one grateful that you accepted the invitation.” Li Feng ground his teeth. Gong Ilhyuk, the third of the Three Hands of Zhongnan, grinned at him. “Anyway, you’ve done well for yourself. Assistant Military Commissioner, someone like you… Huashan must have spread around quite a few silver nyang for you. Hmm?” “How dare you insult Huashan?” “Insult Huashan? You’re the one who insulted it. Ten years ago, who was it that fell to his knees after only a hundred or so exchanges with that magnificent Huashan martial arts?” “You bastard!” A thunderous shout burst from Li Feng’s mouth. At the moment he glared at Gong Ilhyuk with eyes that seemed to pour out streams of flame, a third shout rang out from beyond the iron gate. “The young prodigies of Shanxi Murim request an audience!”

## Korean source

```text
＃139화



진태경 일행을 태운 육두마차가 출발하고 채 한 시진도 되지 않아 태원 거리는 다시 한번 뜨겁게 달아올랐다.

사두마차를 둘러싼 오십 기의 기마, 그리고 형형한 눈빛을 뿜어내는 무인들 때문이었다.

“저건…….”

“태원진가다!”

“와아아아!”

“아까는 산서잠룡이고 이제는 태원진가야? 오늘 눈 호강 제대로 하는구먼.”

마차 안, 사방에서 쏟아지는 환호를 듣고 있던 진위경의 귀가 쫑긋 섰다.

“무경아, 방금 들었느냐?”

진무경이 하품을 하며 고개를 끄덕였다.

“예. 들었습니다.”

“위팽, 자네도?”

위팽 역시 지긋지긋하다는 표정으로 대답했다.

“제가 들었건 말건 신경 안 쓰시잖습니까. 그냥 말씀하십쇼.”

“자넨 말을 왜 그렇게 하나? 그러면 속이 시원해?”

“속이 시원하긴요, 지금도 화병 나게 생겼는데요. 그래서 하고 싶으신 말이 뭡니까?”

“방금 사람들이 그러는데 태경이가…….”

“와, 미치겠네.”

진위경은 위팽의 중얼거림을 못 들은 척하며 말을 이었다.

“성주와의 오찬에 참석하러 간 모양일세. 지금쯤이면 도착했을지도 모르고.”

“도착했겠죠. 엎어지면 코 닿을 거린데.”

“혹시 무슨 일이라도 생기는 건 아니겠지?”

“삼공자가 무슨 물가에 내놓은 어린아이도 아니고. 상다리가 부러지도록 극진한 대접을 받고 있을 테니 걱정일랑 접어 두십시오.”

“글쎄, 워낙 자유분방한 아이라.”

위팽이 그게 무슨 개소리냐는 듯 눈을 동그랗게 떴다.

“자유분방이라뇨. 이 경우는 천방지축 아닙니까?”

“크흠.”

“그냥 사고 칠 것 같아서 걱정된다고 말씀하시면 되지, 뭘 또 그렇게…….”

“그 입 다물게.”

“예. 그럼 아무 말도 안 할 테니까 정 걱정되시면 저기 있는 이공자한테 물어보십쇼.”

심드렁한 대답에 진위경의 시선이 슬쩍 옆으로 옮겨 갔다.

사실 위팽의 조언은 적절했다. 이 중에서 현 산서 성주와 한 번이라도 대면해 본 적이 있는 사람은 진무경뿐이니까.

‘더 말을 안 해 줘서 문제지.’

산서 성주와의 오찬을 그냥 ‘개 같았다’는 한마디로 일축한 진무경은 그 후로 입을 굳게 다물고 있었다.

“무경아, 혹시…….”

말이 채 이어지기도 전에 대답이 돌아왔다.

“아무 문제 없을 겁니다.”

단칼 같은 대답에 진위경이 안도의 한숨을 내쉴 때, 진무경이 한마디를 덧붙였다.

“비위가 좋다면요.”

“……비위라니? 갑자기 그게 무슨 소리냐?”

황족이며 성주가 주최하는 식사 자리다. 성대한 연회에 구더기가 들끓는 음식이라도 나온단 말인가?

순간 어리둥절해진 그의 시선에 서서히 일그러지는 진무경의 얼굴이 보였다.

“있습니다. 벌레만큼 징그러운 놈이.”



* * *



성주가 머무른다는 이곳, 산서성부(山西城府)는 저택의 형태를 벗어난 지 오래였다.

태원진가도, 얼마 전에 다녀왔던 항산검문도 상당한 규모였지만 이곳에 비하면 우스울 정도다.

‘이걸 뭐라고 불러야 하나. 요새? 아니면 성?’

대륙 스케일이 큰 건 진작 알고 있었지만, 상상 이상이다.

나는 물론이고 청풍과 후기지수들도 입을 쩍 벌리고 주위를 둘러보았다. 그러자 관리가 슬며시 웃는다.

“어떻소?”

“넓네요. 엄청나게.”

“능히 수천 명을 수용하고도 남으니 그럴 수밖에. 전시에 수성하게 된다면 십 년을 버틸 만한 곡식도 있다오.”

관리는 거대한 창고 몇 개를 차례대로 가리켰다. 저 안에 식량이 가득 채워져 있다는 말도 덧붙였다.

“저 많은 곳에 전부 다요?”

“물론이오.”

강남 아파트 입주민처럼 자부심 넘치는 미소를 띤 관리가 말을 이었다.

“성부라는 곳은 전시를 대비하여 크고 단단하게 짓기 마련이지만, 본래 이 정도 크기는 아니라오.”

“그럼……?”

“이곳에 어떤 분이 사시는지 벌써 잊었소?”

“아.”

그랬지. 그냥 성주도 아니고 황족. 거기에 더해 정식으로 왕 작위도 가진 어엿한 임금님이 살고 있댔다.

“그럼 여기가 왕궁?”

“그런 셈이오.”

우리는 촌놈처럼 주위를 두리번거리며 계속 이동했다.

시선이 닿는 곳마다 하인과 시비들이 바쁘게 움직였고, 군기가 바짝 든 정예군들은 경계를 서거나 연무장에서 대련을 벌이고 있었다.

‘수준이 제법인데?’

가장 의외였던 점은 군사들의 질이 상당히 높다는 사실이었다.

경계를 서는 인원 중 대부분이 레벨 20 전후였고, 제법 그럴싸한 갑주를 차려입은 장수들의 경우에는 일류를 가뿐히 넘겼다.

‘하긴, 버젓이 있는 무공을 굳이 익히지 말라는 법은 없으니까.’

오히려 군대가 강성해지는 거니 장려해야 할 일이다.

나는 걸음을 옮기면서 계속 연무장을 곁눈질했다.

둥! 둥! 둥!

“찔러!”

“악!”

이미 해가 중천에 걸린 정오.

북소리에 맞춰 수백의 창날이 빛나고, 군사들이 한 몸처럼 일사불란하게 모이고 흩어진다.

전법과 전술, 대형을 훈련받는 그들을 보고 있자니 문득 한 단어가 떠올랐다.

‘레이드 팀.’

통일된 무기 종류. 체계적인 훈련을 통해 맞춘 합(合)은 대규모 집단전에서 무시무시한 위력을 발휘할 것이다.

‘개개인의 실력은 무림인들보다 떨어지겠지만.’

수십 대 수십의 싸움이라면 몰라도 수백 대 수백, 수천 대 수천의 전투가 벌어진다면 어지간한 절정 고수로는 전세를 뒤엎을 수 없다.

그게 바로 훈련된 집단의 무서움이다.

‘떨어지는 질은 물량과 훈련으로 메운다, 이건가.’

지난 수백 년간 광활한 영토를 지배해 왔다는 통일 제국답다.

그 자존심 강한 무림인들이 대국의 백성임을 인정하는 데에는 지금 같은 이유도 한몫하지 않았을까.

그런데…….

‘이거 뒀다가 어따 써. 엿 바꿔 먹나?’

당장 눈에 보이는 군사들만 수백이 넘어간다. 저 중에 일부만이라도 산서 북부로 보냈으면 적풍단은 진작 빤쓰런 했을 거다.

‘시벌, 누구는 죽을 고비 넘겨 가면서 그 고생을 했는데.’

무능한 공권력의 실체를 보자 갑자기 현자 타임이 찾아온다.

천하제일의 명검을 갖고 있으면 뭐 해. 검갑에서 뽑지 않으면 몽둥이나 다름없는데.

내심 욕을 퍼붓고 있을 때 관리가 입을 열었다.

“자, 이제 거의 다 도착했소.”

그의 말대로였다. 수십여 개의 기둥이 늘어선 긴 회랑의 끝, 거대한 철문이 모습을 드러내자 양옆으로 긴장된 한숨이 흘러나온다.

“휴우우.”

“후우. 어떡해요, 정 소협? 나 너무 떨려요.”

“걱정 마시오. 내가 있잖소.”

“……지랄 염병하네.”

될 놈은 된다더니 그 와중에 어떻게 눈이 맞은 건지 모르겠다.

함께 빠따를 맞으면서 애정이 싹튼 건가?

‘이게 나라냐.’

솔로부대 투 스타로서 불편한 심기를 숨기지 못하는 내게 경쾌한 발걸음으로 걷고 있던 청풍이 밝은 목소리로 물었다.

“저 안에 왕이 있는 건가요?”

왕. 그 한 글자에 산서오문의 후기지수들이 입을 딱 벌렸고, 앞서 걷던 관리는 벌에라도 쏘인 것처럼 펄쩍 뛰었다.

“와, 왕이라니! 무엄하오!”

“어? 왕 아니에요?”

“왕이 아니긴! 당연히 왕이지!”

“그럼 왕 맞지 않아요?”

“아니, 그게 아니고……!”

이러다가는 둘 중 하나다. 관리가 고혈압으로 쓰러지거나, 역모죄를 들먹이면서 당장 연무장에서 훈련 중인 수백 명의 군사를 부르거나.

둘 중 어느 것도 원하지 않는 내가 중재에 나섰다.

“일단 좀 진정하시고, 그리고 청 공자.”

“예, 은인.”

“왕이라고 하면 안 됩니다. 전하라고 해야 돼요. 맞죠?”

마지막 질문은 관리를 향한 거다. 그가 청풍을 노려보며 맹렬하게 고개를 끄덕였다.

“반드시! 무조건 그래야 하오!”

“아, 정말요?”

“휴, 그렇소.”

청풍이 맑은 눈동자를 깜빡였다.

“왜요?”

“……진 공자. 정말 이놈, 아니 이자를 데려가야겠소?”

“전 빼도 상관없긴 한데. 괜찮으시겠어요?”

관리는 잠깐 침묵했다.

청풍을 빼고 다섯 명을 데려가면 상부의 문책과 함께 직장이 날아갈 것이고, 청풍이 혓바닥 한 번 잘못 놀렸다가는 목이 날아갈 것이다.

잠시 후, 다시 입을 연 그의 얼굴은 십 년은 늙어 있었다.

“……그냥 갑시다.”

청풍이 활짝 웃었다.

“감사합니다. 혹시 시간 되면 왕, 아니 전하한테 잘 말씀드려 볼게요.”

“그쪽 양반은 제발 입만 다물고 있어 주시오.”

관리가 간곡한 부탁과 함께 주의해야 할 점을 줄줄이 읊는 동안 우리는 마침내 철문 앞에 도착했다.

척 봐도 엄청나게 크고 두꺼운 철문 뒤에서 두런두런 목소리가 흘러나오고 있었다.

‘도지휘첨사, 화산파, 모욕?’

단편적인 단어들만 들어서는 도저히 무슨 대화를 나누고 있는 건지 알 도리가 없다. 다만…….

‘분위기는 영 아닌 것 같은데?’

마주 보며 밥 먹기에는 썩 좋은 자리가 아닌 것 같다는 직감이 든 그때, 철문 앞에 시립해 있던 이가 크게 외쳤다.

“산서 무림의 후기지수들이 뵙기를 청합니다!”

그그긍.

외침과 동시에 철문이 열리기 시작했다.

관리가 걱정스러운 얼굴로 마지막 당부를 건넸다. 슬쩍 청풍을 곁눈질하면서.

“저 인간 주둥이만 막아 주시오.”

“……아, 예.”

정말 어지간히 걱정되나 보다.



* * *



들어가자마자 눈앞이 환해지는 기분이었다.

호화롭게 꾸며진 대전은 마법 학교를 배경으로 한 영화에서나 보던 넓은 탁자와 온갖 음식으로 가득했다.

그리고 미리 와 있던 다섯 사람을 본 순간, 딱 한 가지 생각이 머릿속을 스쳤다.

‘조졌군.’

눈치 빠르기로는 둘째가라면 서러운 나다. F급 헌터로 눈칫밥을 하도 처먹다 보니 0.1초면 분위기 파악이 끝난다.

바로 지금처럼.

‘분위기 끝내주는데.’

다섯 사람을 중심으로 팽팽하게 조여든 공기가 느껴진다. 밖에서부터 심상치 않음을 느끼긴 했지만 생각 이상이다.

자리가 자리인지라 모두 빈손이기에 망정이지, 허리춤에 뭐라도 있었으면 당장 칼부림이 일어났을 거다.

“이거…… 손님이 오셨으니 해후는 이쯤에서 마칠까요?”

팽팽한 분위기를 흩어 놓은 것은 가냘픈 목소리의 사내였다.

아니, 사내가 맞나? 여인이라고 생각될 정도로 가냘픈 체구에 얼굴은 희었고 입술은 염료라도 바른 듯 붉다.



[Lv.22 홍진]



그가 나를 향해 미소를 지어 보였다.

“강호의 후기지수답게 훤칠한 미남이시네. 내 듣기로는 오늘 태원진가에서 젊은 영웅이 온다고 들었는데, 혹시……?”

지금이 인사를 할 타이밍이다. 나는 다섯 사람을 향해 포권을 취했다.

“태원진가의 진태경이라고 합니다.”

순간 안 좋았던 분위기가 한결 누그러진다. 불쾌와 비웃음의 흔적이 남아 있던 네 사람의 얼굴 위로 놀라움이 덧칠해졌다.

“태원진가의 진태경이라면…….”

흑색 무복을 걸친 거한이 중얼거렸다.

처음 봤을 때부터 상남자 냄새가 물씬 풍기던 그의 이름은 이풍, 머리 위에는 68레벨이라는 숫자가 떠다녔다.

‘군문(軍門)에 소속된 사람인가?’

첫 만남에서 모든 걸 판단할 수는 없지만 풍기는 냄새가 그렇다. 자존심 강하고 강직한 군인. 그것이 그의 첫인상이었다.

‘이풍, 이풍이라. 68레벨이면…… 초일류 정도?’

그의 이름과 레벨을 다시 한번 머릿속에 새겼을 때쯤 나머지 세 사람의 반응이 이어졌다.

“흠. 저 친구가 산서잠룡이라고?”

“젊은데? 아니, 어려.”

“딱히 소문만큼 실력이 대단해 보이지는 않는데…….”

신기한 듯 나를 바라보는 눈빛에는 놀라움과 약간의 질투, 그리고 미묘한 우월함이 담겨 있었다.

대개 이런 경우에는 굳이 상대의 정체를 물어볼 필요가 없다. 자신을 자랑하기 위해 안달이 난 사람들이기 때문이다.

“인사가 늦었군. 후배.”

날카로운 눈매의 남자가 씩 웃으며 말을 걸어온다. 다른 두 명은 귀여운 병아리 보듯이 팔짱을 끼고 날 바라보는 중이었다.

‘이거 묘하게 기분 나쁘네.’

뭐 하는 놈들이기에 다짜고짜 선배 노릇일까?

의문은 얼마 가지 않아 곧 풀렸다.

“아, 아직 모르겠군. 우린 섬서에서 왔다네. 섬서 종남파(終南派), 들어 봤나?”

나도 모르게 입이 벌어졌다.

“조, 종남파? 그 종남파요?”

세 사람의 얼굴에 한껏 웃음꽃이 피었다.

“하하, 이 친구 너무 놀라는데?”

“그러게 말이야.”

“혹 우리 문파를 잘 아는가?”

나는 잔뜩 흥분해서 외쳤다.

“알죠! 잘 알죠! 얼마나 재밌게 봤는데!”

“잘 안다니 기쁘…… 잠깐, 재밌게 보다니?”

“뭐긴요. 그야 당연히 군림…….”

대답하려다가 문득 깨달았다.

아, 여긴 소설이 아니었지.
```

## Current accepted English baseline

```markdown
# Chapter 139

The six-horse carriage carrying Jin Taekyung and his group had been on the road for less than a shichen when the streets of Taiyuan heated up once again.

This time, it was because of the fifty mounted soldiers surrounding the four-horse carriage, as well as the martial artists radiating sharp, piercing gazes.

“That’s…”

“It’s the Jin Family of Taiyuan!”

“Woooooah!”

“First the Sleeping Dragon of Shanxi, and now the Jin Family of Taiyuan? My eyes are getting spoiled today.”

Inside the carriage, Jin Wikyung’s ears pricked up at the cheers pouring in from every direction.

“Mukyung, did you hear that just now?”

Jin Mukyung yawned and nodded.

“Yes. I heard it.”

“Wipeng, you too?”

Wipeng answered with an exasperated expression.

“You don’t care whether I heard it or not. Just say what you wanted to say.”

“Why do you always speak like that? Does it make you feel better?”

“Feel better? I’m about to give myself an ulcer as it is. So what did you want to say?”

“People were saying that Taekyung…”

“Wow. This is driving me insane.”

Jin Wikyung pretended not to hear Wipeng’s muttering and continued.

“It seems he’s on his way to attend a luncheon with the City Lord. He might even have arrived by now.”

“He probably has. It’s close enough to touch if you fall over.”

“I hope nothing happens.”

“The Third Young Master isn’t some little child you’ve left beside a pond. He’s probably being treated to such an extravagant meal that the table legs are breaking. Stop worrying.”

“I don’t know. He’s such a free-spirited child.”

Wipeng’s eyes went round as though he were asking what the hell that was supposed to mean.

“Free-spirited? Isn’t this more a case of him being reckless and out of control?”

“Ahem.”

“You could just say you’re worried he’ll cause trouble. Why do you have to dress it up like that…?”

“Shut your mouth.”

“Yes, my lord. Then I won’t say anything. If you’re really that worried, ask the Second Young Master over there.”

At Wipeng’s indifferent reply, Jin Wikyung’s gaze shifted slightly to the side.

In truth, Wipeng’s advice was appropriate. Jin Mukyung was the only person among them who had ever met Shanxi’s current City Lord, even once.

*The problem is that he won’t tell us anything else.*

Jin Mukyung had dismissed his luncheon with the Shanxi City Lord with a single phrase—*It was fucking awful*—and had firmly kept his mouth shut ever since.

“Mukyung, by any chance…”

Before he could finish, an answer came flying back.

“There shouldn’t be any problems.”

Jin Wikyung let out a relieved sigh at the decisive answer, but Jin Mukyung added one more thing.

“If his stomach can handle it.”

“…His stomach? What are you talking about all of a sudden?”

It was a meal hosted by royalty and the City Lord. Was he saying they might serve food crawling with maggots at such a grand banquet?

As confusion filled Jin Wikyung’s gaze, he saw Jin Mukyung’s face slowly twist.

“There’s someone here as disgusting as a bug.”

* * *

The Shanxi Provincial Office, where the City Lord resided, had long since outgrown the shape of an ordinary estate.

The Jin Family of Taiyuan and the Mount Heng Sword Sect, which I had visited not long ago, were both enormous, but compared to this place, they seemed laughably small.

*What should I call this? A fortress? No, a castle?*

I had known for a long time that the continent operated on a massive scale, but this was beyond anything I had imagined.

Cheongpung and the other young prodigies gaped as they looked around. The official gave a small smile.

“What do you think?”

“It’s big. Extremely big.”

“It can easily accommodate several thousand people, so it has to be. If we had to defend it during wartime, we even have enough grain to last ten years.”

The official pointed to several enormous warehouses one after another. He added that they were filled with food.

“All of those?”

“Of course.”

The official continued with a proud smile, like a resident of a Gangnam apartment showing off his building.

“Provincial offices are generally built large and sturdy in preparation for wartime, but they aren’t normally this large.”

“Then…?”

“Have you already forgotten who lives here?”

“Oh.”

Right. He wasn’t merely the City Lord. He was a member of the imperial family. On top of that, he possessed an official royal title—a proper prince in his own right.

“Then is this the royal palace?”

“In a manner of speaking.”

We continued moving, looking around like country bumpkins.

Everywhere we looked, servants and maidservants hurried about their business, while elite soldiers with razor-sharp discipline stood guard or sparred in the training grounds.

*They’re pretty good.*

The most surprising thing was the remarkably high quality of the soldiers.

Most of the soldiers standing guard were around Level 20, while the commanders wearing fairly impressive armor were comfortably above First Rate.

*Well, it’s not as if there’s any reason they shouldn’t learn martial arts when they’re readily available.*

If anything, it would make the army stronger. It was something that ought to be encouraged.

I kept walking while glancing toward the training grounds.

*Boom! Boom! Boom!*

“Thrust!”

“Argh!”

It was noon, with the sun already high overhead.

Hundreds of spearheads flashed in time with the drums, and the soldiers gathered and scattered in perfect unison, moving as one body.

Watching them train in formations, tactics, and battle strategies, one word suddenly came to mind.

*Raid team.*

Uniform weapons. Coordination drilled into them through systematic training. In a large-scale battle, that kind of teamwork would display terrifying power.

*Their individual skills might be inferior to those of Murim martial artists.*

A battle of dozens against dozens might be another story, but if hundreds fought hundreds, or thousands fought thousands, even an ordinary Peak master couldn’t turn the tide by himself.

That was the terrifying strength of a trained group.

*Make up for inferior quality with numbers and training. Is that it?*

It was just as one would expect from a unified empire that had ruled a vast territory for hundreds of years.

Wasn’t that part of the reason those proud Murim martial artists acknowledged that they were subjects of a great nation?

And yet…

*What the hell are they keeping all this for? To trade it in for candy?*

There were already more than several hundred soldiers in sight. If even a portion of them had been sent to northern Shanxi, the Red Wind Band would have made a run for it long ago.

*Fuck. Some of us nearly died going through all that trouble.*

Seeing the true face of incompetent public authority suddenly plunged me into a spell of hollow enlightenment.

What good was owning the finest sword under heaven? If you didn’t draw it from its scabbard, it was no different from a club.

Just as I was cursing them inwardly, the official spoke.

“Well, we’re almost there.”

He was right. At the end of a long corridor lined with dozens of pillars, a massive iron gate came into view, and anxious sighs escaped from both sides.

“Phew…”

“Whew. What do I do, Young Hero Jeong? I’m so nervous.”

“Don’t worry. You have me.”

“…What a fucking load of bullshit.”

They say people destined to succeed will succeed, but I had no idea how those two had managed to hit it off in the middle of all this.

*Maybe getting beaten together made them fall for each other?*

*What kind of country is this?*

Unable to hide my discomfort as a two-star general of the Singles Brigade, I heard Cheongpung ask brightly as he walked along with a light step.

“Is the king inside?”

King.

At that single word, the young prodigies of the Five Gates of Shanxi gaped, while the official leading us leaped as though he had been stung by a bee.

“A king? How impudent!”

“Huh? Isn’t he a king?”

“Of course he’s a king!”

“Then wasn’t I right?”

“No, that’s not what I mean…!”

At this rate, one of two things would happen. The official would collapse from high blood pressure, or he would invoke treason and immediately summon the hundreds of soldiers training in the grounds.

I wanted neither, so I stepped in to mediate.

“First, calm down. And, Young Master Cheongpung.”

“Yes, Benefactor.”

“You can’t call him a king. You have to say ‘His Highness.’ Right?”

The final question was directed at the official. He glared at Cheongpung and nodded furiously.

“Absolutely! You must!”

“Oh, really?”

“Phew. Yes.”

Cheongpung blinked his clear eyes.

“Why?”

“…Young Master Jin. Do we really have to take this fellow—or rather, this person—with us?”

“I don’t mind leaving him out. But are you sure you’ll be all right?”

The official fell silent for a moment.

If he took five people without Cheongpung, he would be reprimanded by his superiors and lose his job. But if Cheongpung let his tongue slip just once, he might lose his head.

A moment later, when he spoke again, his face looked ten years older.

“…Let’s just go.”

Cheongpung beamed.

“Thank you. If we have time, I’ll put in a good word with the king—or rather, His Highness.”

“Please, just keep that gentleman’s mouth shut.”

The official proceeded to list every precaution we needed to take, along with his earnest pleas, and we finally reached the iron gate.

The gate was so enormous and thick that it was almost absurd. From behind it came the sound of quiet voices.

*Assistant Military Commissioner, Huashan, insult?*

Those fragmentary words alone gave me no clue what kind of conversation was taking place. Still…

*The atmosphere doesn’t seem very good.*

I had a feeling this wasn’t the best place for people to sit across from one another over a meal.

At that moment, a man standing at attention before the gate shouted loudly,

“The young prodigies of Shanxi Murim request an audience!”

*Groooan.*

The iron gate began to open at the same time.

The official gave me one final warning with a worried expression, stealing a sidelong glance at Cheongpung.

“Please just keep that man’s mouth shut.”

“…Ah. Yes.”

He must have been extremely worried.

* * *

The moment we entered, it felt as though my eyes had brightened.

The lavishly decorated grand hall was filled with a long table like the ones I had only seen in movies set in magic schools, along with every kind of dish imaginable.

And the moment I saw the five people who had arrived ahead of us, only one thought crossed my mind.

*We’re screwed.*

When it came to reading the room, I was second to none. After spending so long scraping by as an F-rank Hunter, always watching everyone’s mood, I could read the room in 0.1 seconds.

Just like now.

*What a wonderful atmosphere.*

The air around the five people was pulled taut.

I had sensed that something was wrong from outside, but the reality was worse than I had expected.

It was fortunate that everyone had come empty-handed because of the occasion. If anyone had been carrying so much as a weapon at their waist, someone would have drawn steel on the spot.

“Well… Since we have guests, shall we end this reunion here?”

The tense atmosphere was dispersed by a man’s delicate voice.

Though was he really a man? His slender build was delicate enough to make him seem like a woman. His face was pale, and his lips were red as though they had been painted with dye.

> **System**
>
> Level 22: Hong Jin

He smiled at me.

“You’re a strikingly handsome young prodigy, just as one would expect from the martial world. I heard a young hero from the Jin Family of Taiyuan was coming today. Might that be you…?”

Now was the time for introductions. I performed a fist-and-palm salute toward the five men.

“My name is Jin Taekyung of the Jin Family of Taiyuan.”

The unpleasant atmosphere immediately eased somewhat. Surprise painted over the traces of displeasure and ridicule lingering on the other four faces.

“If you’re Jin Taekyung of the Jin Family of Taiyuan…”

A huge man dressed in black martial robes muttered.

From the moment I first saw him, he had radiated tough-guy energy. His name was Li Feng, and the number 68 hovered above his head.

*Is he affiliated with the military?*

I couldn’t judge everything from a first meeting, but that was the impression he gave. A proud and upright soldier. That was my first impression of him.

*Li Feng, Li Feng… At Level 68, he’s probably an advanced First Rate?*

Just as I was engraving his name and Level into my mind, the other three men reacted.

“Hm. That’s the Sleeping Dragon of Shanxi?”

“He’s young. No, he’s a child.”

“He doesn’t look particularly as incredible as the rumors claim…”

The gazes fixed on me with apparent curiosity contained surprise, a hint of jealousy, and a subtle sense of superiority.

In situations like this, there was usually no need to ask about the other person’s identity. They were the sort of people desperate to show off.

“Apologies for the late introduction, Junior.”

A sharp-eyed man grinned as he spoke to me. The other two had their arms folded as they looked at me like a cute little chick.

*This is weirdly irritating.*

What kind of people acted like my Seniors right off the bat?

My question was answered soon enough.

“Oh, you don’t know yet, do you? We came from Shaanxi. The Zhongnan Sect of Shaanxi—have you heard of it?”

My mouth fell open before I knew it.

“The Zhongnan Sect? *That* Zhongnan Sect?”

The three men’s faces blossomed with smiles.

“Haha! Look how surprised he is.”

“Exactly.”

“Perhaps you know our sect well?”

I shouted, suddenly brimming with excitement.

“I do! I know it very well! I had so much fun reading about it!”

“We’re glad to hear you know us… Wait. What do you mean, ‘reading about it’?”

“What else? Obviously, *The Reign…*”

I stopped halfway through my answer.

*Ah. This wasn’t a novel.*
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 139`.

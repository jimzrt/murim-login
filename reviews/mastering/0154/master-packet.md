# Master Edit Task — Chapter 154

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
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 마교     | **Demonic Cult**                                 |                                                       |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 스킬               | **Skill**                      |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 습득               | **Acquired**                   |
| 헌터      | **Hunter**            |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |
| 혈교 | **Blood Cult** | Demonic organization named as a possible source of the intruder. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 낙안봉 | **Falling Goose Peak** | Huashan peak exceeding five hundred jang; Cheongpung climbed it as a child. |
| 인피면구 | **human-skin mask** | Disguise made from peeled human facial skin. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 장칠득 | 진태경 | servant_to_third_young_master | Third Young Master | formal-deferential | Jang Childeuk addresses Taekyung as 삼공자님 while asking permission to report the dangerous training. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 고생하셨습니다 | register | Subordinate courtesy (“thank you for your hard work”), not a superior’s “Good work.” | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 145–149

## Plot

Jin Taekyung pressures the four heirs of the Five Gates of Shanxi other than the Seongun Escort Bureau to support the Jin Family of Taiyuan, Huashan, and the government, threatening to absorb Gopyeong Sect as a Jin Family branch if necessary. He invites ten-year-old Prince Shangshan Zhu Bao to the Jin Family’s grand banquet in fifteen days and promises to obtain Jin Mukyung’s autograph, though Zhu Bao refuses Cheongpung’s autograph until Cheongpung earns a martial title.

At the luncheon’s conclusion, Zhu Bao gives Taekyung Prince Shangshan’s Token as the Quest Reward. Hong Jin then joins Taekyung’s journey to the Jin Family, sending Jin Wikyung a thousand silver nyang and arranging a large escort and delegation. Cheongpung receives the Royal Guard Armor Set and decides to stay with the Jin Family temporarily. The Five Gates’ young prodigies remain at Honghwa Inn until New Year’s Day to support the Seongun Escort Bureau. During the journey, Cheongpung reveals that he came to Huashan at age three or four and was not born there; Hong Jin discloses that he is a eunuch, formerly served the late Emperor, was assigned to Prince Shangshan, and reached the frontier in something like exile.

Wikyung prepares an extravagant, bribe-influenced welcome for Hong Jin. He and Hong Jin immediately establish a playful rapport, while Cheongpung reveals that Mae Jonghak is his grandfather and that he secretly left Huashan to defeat all the Ten Dragons and Phoenixes. He chooses Jin Mukyung as his first opponent. Cheongpung activates the Zaha Divine Technique, and his light-flames collide with Mukyung’s Sword Energy as their duel begins; the outcome is unresolved.

Meanwhile, Huashan’s Lone Crane, Baek Museong, travels with fellow Three Plum Blossom Elites Chulwoo and Eunhyang toward the Jin Family. After Chulwoo and Eunhyang cause trouble with the Black Serpent Sect in Xi’an, Baek makes them return the stolen money and jade hairpin and apologizes to the innkeeper. Huashan has been sealed since Mae Jonghak entered the sleeping Sect Leader’s quarters, left a dagger and handwritten note, and disappeared. A messenger from Shanxi prompted Huashan to dispatch the Three Elites, and Baek looks forward to seeing how Cheongpung has grown since their meeting ten years earlier.

## Continuity

- Prince Shangshan’s Token has been obtained as the completed luncheon Quest Reward; Zhu Bao is expected at the Jin Family’s grand banquet in roughly fifteen days, around New Year’s Day.
- Zhu Bao is ten years old, an exceptionally skilled young swordsman, and an admirer of Jin Taekyung. Jin Mukyung refused Zhu Bao’s autograph three years earlier; Taekyung has promised to obtain it.
- Cheongpung is a twenty-year-old Peak master, grandson and disciple of Sword Saint Mae Jonghak. He secretly left Huashan without Mae Jonghak’s knowledge and is undertaking a dueling tour against the Ten Dragons and Phoenixes.
- Cheongpung’s duel with Jin Mukyung has begun, but its outcome is unknown. Cheongpung still lacks a martial title, which Zhu Bao requires before accepting his autograph.
- Cheongpung came to Huashan at about age three or four rather than being born there. His parentage and Mae Jonghak’s statement that a crane delivered him remain unexplained.
- Mae Jonghak disappeared after entering the sleeping Huashan Sect Leader’s quarters, leaving a dagger and handwritten note. Huashan is sealed, and the search for Mae Jonghak’s hidden residence remains unresolved.
- Baek Museong is Huashan’s Lone Crane and the first of the Three Plum Blossom Elites. Chulwoo and Eunhyang are his junior disciples and fellow Elites; both are notorious troublemakers.
- Hong Jin is a eunuch who formerly served the late Emperor and has served Prince Shangshan since infancy. His circumstances of castration, exile-like transfer to the frontier, and political role remain unclear.
- Hong Jin and Jin Wikyung have formed a joking rapport. Hong Jin bribed Wikyung with one thousand silver nyang, prompting the Jin Family’s extravagant pro-imperial welcome.
- Hong Jin and Li Feng continue pursuing the Shaanxi–Shanxi trade project through Huashan, with the Seongun Escort Bureau as the proposed base. Taekyung is to relay the proposal to Jin Wikyung.
- The four non-Seongun heirs of the Five Gates will remain at Honghwa Inn until New Year’s Day while supporting Taekyung’s side.
- Gong Ilhyuk remains humiliated and vengeful; the identities of the other two members of the Three Hands of Zhongnan are unknown.
- Taekyung remains below the Peak realm and cannot use Sword Energy despite his victories over Peak masters.

## Translation Decisions

- Render **주표** as “Zhu Bao,” **상산왕** as “Prince Shangshan,” and **상산왕의 패** as “Prince Shangshan’s Token.”
- Render **고평문** as “Gopyeong Sect” and **고평지부** as “Gopyeong Branch of the Jin Family of Taiyuan.”
- Render **비무행** as “dueling tour,” **청강검** as “blue-steel sword,” and **광염** as “light-flames.”
- Render **화산일학** as “Huashan’s Lone Crane,” **매화삼절** as “Three Plum Blossom Elites,” and **매화검수** as “Plum Blossom Swordsmen.”
- Use “Senior Brother” for **대사형** and “Big Brother” for **큰 오라버니** when Eunhyang deliberately uses the familiar alternative.
- Preserve the crude eunuch misunderstanding and Cheongpung’s innocent “ball friend” joke.
- Render **금성전장** as “Golden Star Exchange,” **전표** as “bank draft,” **은자** as “silver nyang,” **철전** as “iron coins,” **은원보** as “silver yuanbao,” and **사서삼경** as “Four Books and Three Classics.”
- Continue rendering **전하** as “His Highness” formally and **왕** as “king” when used literally.

### Prior accepted reading-copy tails

#### Chapter 152 tail (verified mastered)

…
“What are those?” “Birds, probably.” As Childeuk stared blankly at the sky, his gaze drifted toward the dizzyingly high cliff. Suddenly, his eyes narrowed. “What about that thing clinging to the cliff?” “The cliff? What’s on the cliff?” “Yes. It’s pretty big.” “Dunno. Must be a pretty big bird. Hold on, I brought a bottle of liquor somewhere…” Without even looking where Childeuk was pointing, Hong pulled a small porcelain bottle from his robes. “It looks a little too big to be a bird.” “It could be a Heavenly Eagle. Those things are as big as people. They aren’t ordinary hawks.” “Wow. It really is as big as a person.” “They’re even called spirit creatures. I heard their wingspan alone is more than a jang. I’ve only seen one from a distance, myself.” “But, hyung.” “What? Why do you keep calling me?” “Do Heavenly Eagles fall, too?” “What the hell are you talking about?” Hong, who had been tipping the bottle toward his mouth, hurriedly looked at the cliff. At that dizzying height, a massive dot was plummeting rapidly. “Aaaaaaah!” Childeuk marveled. “It really is a spirit creature. Its scream sounds exactly like a person.” “That’s a person, you lunatic!” “Whaaa!” “Move! Move!” The instant Hong screamed, a person crashed into the ground amid a shower of stone fragments. *Boom! Rumble, rumble!* Rocks and dust burst in every direction. The two men swallowed at the same time. “D-do you think he’s dead?” “Try falling from that height. Even the Jade Emperor would die.” How had such a horrific calamity intruded upon their peaceful routine? The middle-aged martial artist clutched his trembling chest and stared at the body lying facedown. “What kind of madman falls from a cliff…” “He looks young.” “Does it matter whether he’s young or old? The important thing is that he’s dead.” “That’s true, but…” “Go turn him over.” “M-me?” “Who else is here besides you and me? Hurry!” At the middle-aged martial artist’s shout, Jang Childeuk hesitantly began approaching the body. He had only been a martial artist for a month. This was the first time he had ever witnessed someone die right in front of him. “Huff, huff.” The closer he got, the more clearly he could see the body. Its limbs lay limp, and blood streamed from the back of its head as it lay facedown on the ground. Considering the height of the fall, the corpse looked surprisingly intact. “M-may you be reborn in paradise.” He squeezed his eyes shut and reached out to touch the body. That was when it suddenly shot upright. *Crack!* The world flashed before Childeuk’s eyes, followed by a wave of excruciating pain. He landed hard on his backside, his mouth hanging open, unaware that blood was streaming from both nostrils. “Uh… uhhhh.” “What in the… Ugh, ughhh!” Hong’s legs gave out, and he collapsed. “The corpse—the corpse is alive!” “Ugh! It’s a jiangshi! A jiangshi[^1] has appeared!” The dirt-covered stranger who had suddenly been written off as dead staggered to his feet. His hair was wild, and blood vessels had burst in his eyes. He looked around, then ground his teeth. “Fuck, Taecho Village[^2] again?” * * * Damn, that hurts. Head, shoulders, knees, feet, knees, feet… There wasn’t a single part of me that didn’t ache. Luckily, I’d driven a dagger into the cliff and slowed my fall. Otherwise, I might have kicked the bucket. Of course, the physique and toughness stats I had steadily raised had helped, too. “Ow, the back of my head is throbbing.” I touched the tender spot and found it wet with blood. I tore off a strip of my sleeve and was wiping away the blood when— “W-who are you?!” “Reveal your identity, you scoundrel!” Oh, right. These two guys were here too. One of the two men pointing swords at me looked familiar. What was his name again… “Jang Childeuk?” Mr. Jang Childeuk, who had been working hard to manipulate public opinion at Honghwa Inn until just a few days ago, recoiled in terror. “Gasp! How do you know my name?!” “The jiangshi is talking! It’s bewitching people with its words!” “…Who are you calling a jiangshi? Can’t you see I’m breathing just fine?” The middle-aged man with the patchy beard glared at me and shouted. “You evil creature! You can’t fool my eyes. If you were human, you couldn’t possibly be fine after falling from that height. Who sent you? The Demonic Cult? The Blood Cult? Or perhaps…” “Taecho Village! Hyung, that jiangshi definitely said ‘Taecho Village.’” “That’s right! You’re a jiangshi sent by Taecho Village!” The middle-aged man shouted as if he had finally figured it out, then suddenly stopped and asked Childeuk, “But where is Taecho Village?” “I don’t know either.” “…” It would have been strange if he did. I gave up on the conversation and wiped the dirt from my face with my sleeve. The middle-aged man might not know me, but Childeuk knew my face well. This would be faster. “Gasp! Third Young Master!” “Yes. Long time no see.” “Little brother, the Third Young Master? What in the world are you talking about?” “The Third Young Master has become a jiangshi!” “…” How the hell did he reach that conclusion? [^1]: A jiangshi is a reanimated corpse from Chinese folklore, often depicted as a hopping vampire. [^2]: *Taecho* means “primordial” or “the beginning.”

#### Chapter 153 tail (verified mastered)

…
climbed, the more treacherous the slope became and the smoother the surface grew. The cliff was already slippery enough. On top of that, the scattered snow flurries that came almost every day and the wind blowing in from the northern Gaoyuan had turned it into one enormous sheet of ice. *Dead end. I can’t see a way forward.* As I worried at my lip, something suddenly caught my eye. A crack in the rock blocked by a snowball that had not yet frozen. It was a tiny space, barely wide enough for one finger. It would be difficult, but I had no other choice. “Hup!” I launched myself forward with a shout, simultaneously jamming my smallest finger—the little finger—precisely into the crack. *Thud.* My prediction had been only half right. I could break through the unfrozen snowball, but the crack was much shallower than I had expected. It was barely one finger joint deep. And I had to support a body weighing 0.1 tons with my little finger. “Ungh.” Even for me, this was asking a bit much. To make matters worse, my finger was slowly slipping because of the moisture pooled inside the crack. *If I waste any more time, I’ll fall.* There was not much farther to go. I steadied my breathing and calmed the tension in my body. Using my little finger as a support, I lifted my entire body. Physical ability truly worthy of the word superhuman. > **System** > > - **Strength** increased by 1. > > - **Agility** increased by 1. > > - **Stamina** increased by 1. Even my stats rose at just the right moment. Just as I smiled triumphantly and reached toward the next crack— *Hup!* “Captain!” Damn it. My breathing faltered at the worst possible moment. As I steadied it again, Hyuk Mujin kept shouting. “Th-this! This!” “What are you saying? I can’t hear you!” The fierce snowstorm scattered sound and obscured my vision. I was about to open my mouth again when a clear shout struck my ears. “Above! Above!” “Above?” The fact that I could hear Hyuk Mujin’s voice meant the savage wind had paused. Only then did my obstructed vision clear and my ears open. Following Hyuk Mujin’s gesture, I raised my head and finally saw it. A massive boulder falling straight toward my face. *Whoooosh!* “Ah, shit.” *Boom!* * * * “Wow. I can’t believe you broke such a huge boulder with your bare fist.” I let Cheongpung’s admiration go in one ear and out the other as I collapsed onto my back. Only a moment ago, I had wanted nothing more than to beat that bastard senseless. Now I was completely drained. *I made it up. It’s over!* Just as I lay there, unable to move even a hand and cheering inwardly, a bluish, frozen hand reached the summit. “Huff. Haaah.” “You succeeded in only one day! You’re both incredible!” If it weren’t for you, I would’ve made it in one shichen, you idiot. I wanted to lay into him, but I was too exhausted to speak. As Hyuk Mujin and I panted with exhaustion and accomplishment, Cheongpung bowed deeply. “Thank you both for your hard work! Now that you’ve succeeded once, you should be able to climb the remaining nine times much faster.” “…” “…” The words were so shocking that Hyuk Mujin and I forgot even to pant as we stared at him. *What is he talking about?* Could he possibly mean what I thought he meant? No, surely not. As an intellectual of modern society, I spoke with a calm demeanor. “The remaining nine times? What kind of bullshit is that?” “My grandfather…” Was this bastard a wild man or a boy detective? At that moment, Sword Saint or whatever be damned—I couldn’t help seeing red. “So you’re telling us to do this nine more times?” “Yes!” “And you’ll throw rocks at us from up here just the same?” “Yes!” “No.” “What?” Hyuk Mujin and I dropped flat at the same time. “I’m not doing it. I don’t even have the strength to go back down. Go ahead and gut me.” “Gut me too, you vicious bastard!” “Puhahaha.” “…Are you laughing?” Cheongpung smiled brightly. “Sorry. You looked just like I did when I first started training, so I couldn’t help it.” “See? You didn’t want to do it either!” “No. I thought it was fun and wanted to keep going, but my body wouldn’t keep up.” Hyuk Mujin muttered quietly enough that only I could hear. “…Is he insane?” “So I told my grandfather. I asked whether I could continue the next day because my legs wouldn’t listen to me.” As he reminisced about his happy past, Cheongpung suddenly drew his sword. At the same time, purple Sword Energy shot forth. *Shhk.* Ice, dirt, rock—Cheongpung cut through all of it without distinction, then continued speaking. “My grandfather said climbing up was hard, but going down was easy. He said if I endured it for just a moment, I’d be back down in no time.” *Rumble, rumble, rumble.* The edge of the cliff ledge where Hyuk Mujin and I were lying—barely ten square meters in size—began to shake. *Is this for real?* As we lay there in a daze, Cheongpung waved at us. “Nine more to go.” > **System** > > - The Quest **Sword Saint Training: A Secondhand Experience** has been generated.

## Korean source

```text
＃154화



중년 무인과 장칠득은 오늘도 하늘을, 아니 절벽을 바라보고 있었다.

“이보게, 장 아우. 혹시 벽호공 익혀 본 적 있나?”

“벽호공이요? 어휴, 저처럼 담이 작은 놈은 엄두도 못 냅니다. 형님은요?”

“오 년 전쯤에 한 번.”

“왜 그만두셨습니까?”

“벽호공 수련을 시작한 지 석 달쯤 됐나? 발을 헛디뎌서 떨어지는 바람에 발목이 부러졌었지.”

“아이고, 높은 곳에서 떨어지셨나 봅니다.”

“겨우 오 장 남짓이었어. 하루도 빠지지 않고 석 달을 수련했는데 발목이 부러진 거야.”

“저런. 아쉽습니다.”

“아쉽다니?”

“혹시 압니까, 계속 익히셨으면 벽호공의 고수가 되셨을지도…….”

“벽호공의 고수? 평생 익힌 검공으로도 이류를 못 벗어나는 내가?”

중년 무인이 피식 웃으며 절벽을 가리켰다.

“무슨 무공이든 무재(武才)가 있어야 고수 소리 듣는 거야. 저 두 사람을 보면서 느끼는 게 없나?”

“확실히 그건 그렇습니다.”

두 사람은 절벽 위를 빠르게 올라가는 두 신형을 응시했다.

볼 것도 없이 오늘도 벽호공 수련에 매진하는 진태경과 혁무진이다.

파파파파팍!

까마득한 위에서 굴러떨어지는 돌멩이과 눈덩이.

지금 이 순간, 두 사람은 같은 생각을 떠올리는 중이었다.

‘저게 사람이야, 도마뱀이야.’

거의 수직으로 이어진 절벽을 오르는 손발에 거침이 없다.

비록 속도의 차이는 꽤 크지만 수련 기간을 생각해 본다면 실로 괄목할 만한 성과였다.

“지금이 며칠째지?”

“어디 보자, 이번이 세 번째 교대니까…… 딱 사흘째입니다.”

“고작 사흘이라. 내가 석 달이 아니라 일 년을 수련했다면 저 정도로 벽호공을 익힐 수 있었을까?”

“…….”

그 질문에 대한 답은 중년 무인도 알고 장칠득도 안다.

잠깐 말이 없던 장칠득이 입을 열었다.

“형님.”

“응?”

“무재가 없는 우린 뭘 할 수 있죠?”

“우린 쓸모가 없어. 육포나 꺼내.”

“옙.”

장칠득은 냉큼 품에서 육포와 술병을 꺼냈다. 태원진가 최고의 꿀 보직이라는 수련동 근무에 빠르게 적응해 나가는 그였다.



* * *



후우웅!

무서운 속도로 떨어지는 바위를, 절벽에 바짝 달라붙어 피했다. 한참 위에서 아쉬운 얼굴로 입맛을 다시는 청풍이 보인다.

‘이럴 줄 알았다, 인마.’

이 짓 한두 번 당하나?

어릴 때부터 공부 머리는 나빠도 몸으로 익히는 거 하나만큼은 타의 추종을 불허하던 나다.

“흐어어억!”

그에 비해 혁무진 저놈은 좀 느린 편이다. 아무래도 지금의 나와는 확실히 수준 차이가 있으니 당연할지도 모르겠다.

나는 한참 밑에서 기어 올라오는 혁무진을 향해 외쳤다.

“무진아, 괜찮냐?”

“아니요!”

“……어, 그래?”

칼답 봐라. 당연히 안 괜찮겠지만 보통은 빈말이라도 괜찮다고 하는데, 혁무진 이놈은 그런 게 없다.

“엄살 부리지 말고 빨리 올라와!”

“온몸에 쥐가 나서 죽겠다고요! 방금도 간신히 피했어요!”

말은 저렇게 해도 제법 잘 따라온다. 이번 수련을 통해 다시 한번 확인했다. 혁무진은 제법 끈기와 무재가 있는 놈이라는 사실을.

“이제 거의 다 왔다. 이 악물고 올라와!”

나는 절벽의 오목한 곳에 몸을 집어넣고 잠시 숨 고르기에 들어갔다.

‘퀘스트 창 오픈.’

띠링.



퀘스트



[검성 수련 간접 체험기]

고수는 수많은 담금질과 망치질 끝에 만들어지는 법.

검성으로부터 혹독한 수련을 받은 청풍은 어린 시절의 기억을 되살려 당신들을 교육시킬 겁니다!



등급 : 절정

제한 : 청풍의 허락을 받은 자

임무 : 절벽 10회 등반 (9/10)

보상 : [벽호공] 습득

 [청풍]이 매우 기뻐합니다

 ???

실패 : 부상 또는 사망

 [청풍]이 매우 슬퍼합니다





이 빌어먹을 절벽을 타기 시작한 지 오늘로 딱 사흘째.

퀘스트 완료까지는 딱 한 번이 남았지만 아직 방심해서는 안 된다.

왜냐하면…….

“은인! 어디 계세요! 고개 좀 내밀어 보세요!”

“싫어! 꺼져!”

“아, 거기 계셨구나! 근처에 던질 만한 게 다 떨어져서 구해 오느라 좀 늦었어요!”

당장이라도 내 얼굴에 바위를 떨구고 싶어 하는 저 사이코패스 때문이지.

첫 번째 절벽 등반도 충분히 힘들었는데, 청풍의 훼방은 회차를 거듭할수록 점점 강도를 더해 가는 중이다.

나는 몸을 바짝 웅크리고 외쳤다.

“그걸 왜 구해 와! 돌 떨어졌으면 그냥 던지질 마!”

“그치만…… 이렇게 하지 않으면, 은인께서 벽호공을 제대로 익히실 수 없는걸요!”

“…….”

미친놈인가. 세상천지에 바위 처맞아 가면서 벽호공 익히는 사람이 몇 명이나 된다고.

기가 차서 말도 안 나오던 와중에 상처투성이 손 하나가 내가 있는 공간으로 쑥 솟구쳤다.

오래전 이곳에서 벽호공을 익히다가 죽은 귀신……은 당연히 아니고 혁무진이다.

“흐어억. 죽겠다.”

진짜 힘들면 말도 안 나온다. 숨이 턱 끝까지 차서 머리는 띵하고 호흡하는 것만으로도 가슴이 뻐근해진다.

그래도 아직 충분히 살 만해 보이는 녀석이 옆자리로 엉금엉금 기어 오더니 다리를 쩍 벌렸다.

“야, 좁잖아.”

“조장님만 좁습니까? 저도 좁습니다.”

“다리를 오므리든가, 옆으로 좀 더 가라. 여긴 기본적으로 일 인석이야.”

“아, 힘들어요. 조장님이 옆으로 가세요. 힘겹게 여기까지 올라온 오른팔한테 너무 야박한 거 아닙니까?”

“오른팔한테는 잘해 주지. 근데 넌 새끼발가락이라 좀 야박하게 굴어도 돼.”

“와, 진짜 이러시깁니까? 그나마 바위 피할 곳이라고는 여기밖에 없는데. 제가 그냥 확 뛰쳐나가서 면상에 바위라도 맞아야 속이 시원하시겠어요?”

나는 정색하고 대답했다.

“말을 왜 그렇게 하냐? 당연히 아니지.”

“오, 조장님이 웬일로…….”

“한동안 속이 갑갑하고 죄책감에 시달릴 거야. 하지만 일 년쯤 지나면 괜찮아지겠지. 십 년쯤 지나면 얼굴도 까먹을 거고.”

“……거, 되게 현실적이시네.”

“원래 인생이 그런 거야, 인마. 그러니까 당장 다리 오므려. 아니면 내가 죄책감 느낄 일이 생길 것 같으니까.”

“넵.”

쩍벌충은 바위에 뚝배기가 깨져도 상관없다. 쩍벌충이니까.

다리를 바짝 오므린 채 숨을 고른 혁무진이 한숨을 내쉬었다.

“아무리 생각해도 미친 것 같습니다.”

“뭐가?”

“이딴 걸 시키는 청풍 저놈도 미친 것 같고, 시킨다고 하는 저도 미친놈 같아요.”

“그런 것치곤 잘하고 있는데?”

“그냥 죽자 살자 하는 거죠.”

“그게 답이지.”

“예?”

“죽자 살자 하는 거. 그게 답이라고. 나중에 정말 죽음이 코앞에 닥치면 지금 이 순간을 후회하게 될걸?”

나는 흐트러진 머리를 질끈 묶으며 말을 이었다.

“아, 그때 좀 더 열심히 했어야 했는데. 뭐 그런 후회 있잖아.”

헌터로 살면서 피똥 쌀 정도로 노력했다고 자부한다. 하지만 그렇게 했어도 남는 게 후회더라. 후회는 늘 늦는다. 그리고 소중한 뭔가를 잃은 후에야 뼈아프게 다가온다.

“네 목숨, 재물, 아니면 사람. 소중한 걸 잃기 싫다면 지금 목숨 걸고 해. 살아 있을 때 죽도록 노력하는 게 죽는 것보다는 낫잖아?”

“어…….”

혁무진이 눈을 동그랗게 뜨고 나를 바라봤다.

“뭔가 경험자처럼 말씀하시네요.”

“왜, 이상하냐?”

“누구 입에서 나온 말이냐에 따라 느낌이 다르잖아요. 제가 보는 조장님은, 으음…….”

“남부럽지 않게 자란 도련님이 할 말은 아니다?”

“굳이 따지면 뭐 그렇죠. 분명히 살면서 소중한 뭔가를 잃어 본 적 없을 것 같은 사람인데, 산전수전 다 겪은 백전노장 같다고 해야 하나?”

이 녀석, 제법 촉이 좋다.

아니, 어쩌면 다른 사람들의 시선에도 그렇게 보이려나?

별다른 말 없이 피식 웃는 나를 혁무진이 미심쩍은 눈빛으로 바라봤다.

“뭡니까, 그 웃음은?”

“그냥 제법이다 싶어서.”

“혹시 조장님, 가짜 아니죠?”

“뭐?”

“이제 와서 꺼내기에는 좀 새삼스러운 이야기긴 한데……. 달라져도 너무 달라졌잖아요. 성격도 그렇고, 무공도 그렇고. 완전 딴사람이 된 것 같다니까요.”

“소문 못 들었어? 태원진가에서 비밀리에 길러 낸 비밀 병기.”

“소문은 소문이죠. 확인 안 된 소문. 조장님이 흥청망청 노는 거 본 사람이 어디 한두 명입니까?”

“너도 그중 하나고?”

“네. 처음에는 인피면구(人皮面具)라도 쓰고 있나 했는데 그건 아닌 것 같고.”

“인피면구? 사람 얼굴 가죽 벗겨서 쓰는 그거?”

“보세요. 이런 것도 처음 듣는 양 되물으시고. 가끔 뜻 모를 말도 자주 하시잖아요.”

“흠.”

그러고 보니 어느 순간부터 의심을 피하는 것에 많이 신경 쓰지 않았다. 주위의 모두가 나를 태원진가의 진태경으로 생각하고 있었으니까. 나도 무림에서의 모습을 내 일부로 받아들인 지 오래였다.

“혹시 조장님이 소설에서나 보던 암중 세력이 내세운 대역, 뭐 그런 거면 지금 말씀해 주세요. 조용히 넘어가 드릴 테니까.”

“이거 어이없는 놈일세. 그럼 당장 보고해야지.”

“저야 뭐 예전 모습보다는 지금이 훨씬 나으니까요. 조장님한테는 목숨 빚도 있고. 헤헤.”

입은 웃고 있지만 농담은 아니다. 은연중에 넘어가는 목울대, 살짝 흔들리는 눈빛이 그 증거다.

나는 잠시 고민하다가 입을 열었다.

“솔직하게 말해 줘?”

“소, 솔직하게?”

“안 그래도 말하고 싶어서 입 근질거렸는데 잘됐지. 장소도 딱 적당하고.”

혁무진이 불안한 표정으로 주위를 살폈다. 딱 두 사람이 엉덩이 붙일 만큼 움푹 들어간 절벽. 때마침 밖으로 얼굴만 내밀면 바위를 떨궈 줄 미친놈도 기다리고 있다.

그야말로 둘이 앉아 있다가 하나가 죽어도 모를 명당이다.

“너 머리 되게 나쁘구나?”

혁무진이 마른침을 꿀꺽 삼켰다.

“조, 조, 조장님. 전 조장님이 어떤 사람이어도 상관없습니다.”

“이미 늦었어.”

“헉! 말 안 할게요! 아까 했던 말 진심이었어요!”

“내가 마교 소속이라고 해도?”

“마교!”

“딱 한 번 말한다. 잘 들어라.”

“못 들은 걸로 하겠습니다. 아니, 안 들을게요!”

새파랗게 질린 혁무진이 귀를 막으려 했지만 내 말이 한발 빨랐다.

“나, 사실 다른 세상에서 왔다.”

“……?”

“만 리를 떨어져 있어도 서로 대화할 수 있고, 뿔이나 날개가 달린 괴물들이 우글거려. 무림으로 치자면 악귀라고 하나?”

“……예?”

“아무튼 그런 세상에서 어쩌다가 여기까지 오게 됐는데, 눈앞에 막 이상한 게 보이더니 레벨 업을 팍! 포인트가 펑! 머릿속에서 띠링띠링띠링!”

“……”

“아무튼 그렇게 무공에 입문한 지는 두세 달쯤 됐지. 일류 고수 수십 명을 발랐고 절정 고수 셋을 잡았고. 자, 그럼 여기서 질문?”

혁무진이 귀를 반쯤 막고 있던 양손을 스르륵 내렸다.

빡침과 안도가 뒤섞인 복잡한 표정이다.

“후우, 그냥 제가 잘못한 걸로 합시다. 됐어요?”

“왜, 사실인데. 안 믿겨?”

“지나가던 개도 안 믿습니다. 내가 진짜 무공만 더 강했어도…….”

따악!

투덜거리는 녀석의 뒤통수를 후려갈겨 준 다음, 자리에서 일어났다. 진실이지만 진실 같지 않은 이야기다.

물론 나 스스로도 혁무진의 이런 반응을 예상하고 있었기에 말한 것이다.

다른 세상에서 왔다니, 누가 들어도 황당한 이야기 아닌가?

“뇌반업? 포인두? 내참, 말을 말아야지. 제가 조장님한테 뭘 기대했는지 모르겠습니다.”

“뭘 기대했는데? 마교? 혈교?”

“아, 쫌! 그만 좀 하세요!”

자리에서 일어나는 혁무진의 어깨를 잡아챘다. 다음 순간 살벌한 파공음과 함께 성인 남성 키만 한 바위가 스쳐 지나갔다.

“조심해라. 아직 갈 길 멀다.”

나는 녀석을 등을 툭툭 두드려 주고 다시 절벽을 오르기 시작했다. 남은 정상까지는 이제 고작 절반이었다.



* * *



나와 혁무진이 마침내 정상에 오른 순간, 축포처럼 시스템 알림이 터져 나왔다.

띠링. 띠링. 띠링!



- 절벽 10회 등반(10/10)

- 퀘스트를 성공적으로 완료했습니다!

- 새로운 무공, [벽호공]이 활성화됩니다!

- 예상을 뛰어넘는 훌륭한 성과를 거두었으므로 추가 보상이 주어집니다!

- 레벨 업!

- 스탯, 스킬 포인트를 각각 10포인트씩 획득합니다!

- 칭호, [초보 수련자]가 [중급 수련자]로 강화됩니다!

- 변경된 사항은 해당 시스템 창을 열어 확인, 적용시켜 주시기 바랍니다.



청풍이 우리를 향해 활짝 웃었다.

“와아, 이걸 진짜 해냈네요!”

“……그게 무슨 뜻입니까?”

“혹시.”

이 새끼 설마? 우리 둘의 날카로운 눈빛에 청풍이 고개를 저었다.

“별건 아니에요. 전 보름이나 걸렸거든요. 이렇게 빨리 끝내실 줄은 몰라서.”

“보름 말입니까?”

되물은 혁무진이 얼떨떨한 기색으로 나를 바라봤다.

청풍이 누구인가, 검성의 후인이자 진무경을 꺾은 절정 고수다. 그보다 빠른 성취를 이뤘다는 사실이 믿기지 않겠지.

하지만…….

“뭘 좋아해, 인마. 나이대가 다른데. 그렇죠?”

“별로 어리지도 않았어요. 열 살이나 먹었을 때니까!”

“……보통은 열 살밖에 아닌가?”

청풍은 해맑게 웃으며 그때 그 시절을 회상했다.

“그때는 낙안봉(落雁峰)에서 올라갔다가 떨어지는 게 일상이었죠. 참 재밌었는데.”

“낙안봉이요?”

“화산에 있는 봉우리예요. 높이는 오백 장을 가뿐히 넘기는 정도? 아, 물론 저도 끝까지 올라갈 수 있었던 건 열여덟부터였어요.”

“…….”

“…….”

15세 관람 등급 영화도 못 보는 나이 아니냐?

초등학교 3학년이면 급식충이라고 하기에도 뭣하다.

‘난 저 나이 때 학교 운동장에 있는 정글짐 타고 놀았는데…….’

청풍 저놈은 화산 산봉우리를 타고 놀았구나.

역시 대륙, 스케일이 다르다.

“어쨌든 두 분 다 너무너무 고생하셨습니다. 대단한 성과를 거두셨어요!”

혼자 신나게 박수를 친 청풍이 말을 이었다.

“그래서 말인데요…….”

뭔가 불길함을 느낀 혁무진이 황급히 나섰다.

“아냐, 잠깐만. 잠깐만 기다려 봐요.”

“제가 더 재밌는 수련을 많이 알고 있거든요.”

“야! 잠깐만 기다려 보라고!”

혁무진이 고함과 함께 달려들었지만 이미 늦었다. 금나수로 가볍게 녀석을 제압한 청풍이 씩씩하게 외쳤다.

“우리 다 같이 힘내 봐요!”

띠링.



- [청풍]은 당신의 뛰어난 성과에 기분이 한껏 고양되었습니다!

- 특별 보상으로 연계 퀘스트, [검성 수련 간접 체험기-2]가 생성되었습니다!



“야, 이 새끼야! 당장 팔 안 놔!”

혁무진의 고함을 들으면서 문득 드는 의문이 있었다.

‘이거, 연계 퀘스트가 몇 개나 있는 거지?’

하나는 확실하다.

저 청풍이 고작 2에서 멈출 리는 없다는 것.

‘오지게 굴리겠군.’

나는 꽥꽥 소리를 질러 대는 혁무진의 목소리를 뒤로하고 하늘을 바라봤다. 드넓은 하늘이 푸르기 그지없다. 공기는 서늘하고, 거대한 날개를 활짝 펼친 매 몇 마리가 하늘을 부유한다.

원단이 열흘 앞으로 다가온 시점이었다.
```

## Current accepted English baseline

```markdown
# Chapter 154

The middle-aged martial artist and Jang Childeuk were staring at the sky again today—or rather, at the cliff.

“Say, Brother Jang. Have you ever learned the Wall Lizard Technique?”

“The Wall Lizard Technique? Good heavens, someone as timid as me would never even dare try it. What about you, hyung?”

“Once, about five years ago.”

“Why did you quit?”

“Had it been about three months since I started training in it? I misstepped and fell, and broke my ankle.”

“Oof. You must have fallen from somewhere pretty high.”

“Barely five jang or so. I trained for three months without missing a single day, and still broke my ankle.”

“That’s a shame.”

“A shame?”

“Who knows? If you’d kept learning, you might have become a master of the Wall Lizard Technique…”

“A master of the Wall Lizard Technique? Me? I can’t even break out of Second Rate with the sword techniques I’ve practiced all my life.”

The middle-aged martial artist let out a quiet laugh and pointed at the cliff.

“Whatever the martial art, you need talent to be called a master. Don’t you feel anything when you look at those two?”

“That’s certainly true.”

The two men watched the two figures swiftly climbing the cliff.

There was no mistaking them. Jin Taekyung and Hyuk Mujin were dedicating themselves to Wall Lizard Technique training again today.

*Thud-thud-thud-thud!*

Stones and snowballs came tumbling down from far above.

At that very moment, both men were thinking the same thing.

*Are those people or lizards?*

Their hands and feet moved without hesitation as they climbed the nearly vertical cliff.

The difference in speed between them was considerable, but considering how long they had been training, their progress was truly remarkable.

“How many days has it been now?”

“Let’s see. This is our third shift, so… exactly our third day.”

“Only three days. If I had trained for a year instead of three months, could I have learned the Wall Lizard Technique to that extent?”

“…”

The answer to that question was known to both the middle-aged martial artist and Jang Childeuk.

After a brief silence, Childeuk spoke.

“Hyung.”

“Hmm?”

“What can people without martial talent do?”

“We’re useless. Get out the jerky.”

“Yes, sir.”

Jang Childeuk quickly pulled out some jerky and a bottle of liquor from inside his robes. He was adapting rapidly to his post guarding the training hall—the Jin Family of Taiyuan’s cushiest assignment.

* * *

*Whoooosh!*

I pressed myself tightly against the cliff and dodged the boulder plummeting downward at terrifying speed. Far above, I could see Cheongpung looking disappointed as he smacked his lips.

*I knew this would happen, you bastard.*

As if this were the first or second time I’d been subjected to this.

I might have been bad at book learning when I was young, but when it came to learning through my body, I had been unrivaled.

“Haaaargh!”

Hyuk Mujin, on the other hand, was a little slower. Compared to me as I was now, there was a clear difference in level, so perhaps it was only natural.

I shouted toward Hyuk Mujin, who was crawling up from far below.

“Mujin, you okay?”

“No!”

“...Oh. Right.”

What a brutally quick answer.

Of course he wasn’t okay, but most people would say they were fine even as empty courtesy. Hyuk Mujin had no such habit.

“Quit whining and get up here!”

“My entire body is cramping! I barely dodged that one just now!”

For all his complaining, he was keeping up fairly well. This training had confirmed it once again: Hyuk Mujin had a decent amount of persistence and martial talent.

“We’re almost there. Grit your teeth and climb!”

I wedged myself into a hollow in the cliff and took a moment to catch my breath.

*Open the Quest window.*

*Ding.*

> **System**
>
> **Quest**
>
> **Sword Saint Training: A Secondhand Experience**
>
> A master is forged through countless rounds of tempering and hammering.
>
> Cheongpung, who received harsh training from the Sword Saint, will revive his childhood memories and put you through training!
>
> **Grade:** Peak
>
> **Restriction:** Those who have Cheongpung’s permission
>
> **Mission:** Climb the cliff 10 times (9/10)
>
> **Reward:** Acquire **Wall Lizard Technique**
>
> **Cheongpung** is extremely pleased.
>
> **???**
>
> **Failure:** Injury or death
>
> **Cheongpung** is extremely saddened.

Today marked exactly three days since we started climbing this damned cliff.

Only one climb remained before the Quest was complete, but I still couldn’t let my guard down.

Because of this psychopath who looked like he wanted to drop a boulder straight onto my face at any moment.

The first climb had been hard enough, but Cheongpung’s interference had grown more intense with every round.

I curled up as tightly as I could and shouted.

“Benefactor! Where are you? Show me your head!”

“No! Get lost!”

“Oh, there you are! I ran out of things nearby that were good for throwing, so I was delayed while I went to find more!”

“What do you mean, find more? If you ran out of rocks, just don’t throw anything!”

“But… if I don’t do this, you won’t be able to properly learn the Wall Lizard Technique, Benefactor!”

“…”

Was this guy insane?

How many people in the world learned the Wall Lizard Technique while getting pelted with rocks?

Just as I was rendered speechless by the sheer absurdity of it, a battered hand shot up into the hollow where I was hiding.

It wasn’t the hand of some ghost that had died here long ago while learning the Wall Lizard Technique.

Naturally, it was Hyuk Mujin.

“Haaaargh. I’m dying.”

When you were truly exhausted, you couldn’t even speak. You got so out of breath that your head rang, and even breathing made your chest ache.

Even so, Mujin still looked like he had plenty of life left in him. He crawled over beside me, then spread his legs wide.

“Hey, it’s cramped.”

“Am I the only one cramped, Captain? I’m cramped too.”

“Pull your legs in or move over. This is basically a one-person seat.”

“Ah, I’m too tired. You move over, Captain. Aren’t you being a little too harsh on your right-hand man after he worked so hard to get up here?”

“I’m nice to my right arm. But you’re my little toe, so I can afford to be a little harsh.”

“Wow, you’re really going to be like this? This is the only place where we can avoid the rocks. Would it make you feel better if I just jumped out and got one straight to the face?”

I answered with a perfectly serious expression.

“Why would you say that? Of course not.”

“Oh, wow. What’s gotten into you all of a sudden, Captain…”

“I’d feel stifled and guilty for a while. But after a year, I’d be fine. After ten years, I’d have forgotten your face.”

“...You’re awfully realistic.”

“That’s life, punk. Now pull your legs in. Otherwise, you might give me something to feel guilty about.”

“Yes, sir.”

Manspreaders could get their skulls cracked by a rock for all I cared. That was what they got for manspreading.

Hyuk Mujin pulled his legs tightly together, caught his breath, and sighed.

“No matter how I think about it, this is insane.”

“What is?”

“Cheongpung is insane for making us do this, and I’m insane for agreeing to do it.”

“You’re doing pretty well for someone who thinks it’s insane.”

“I’m just fighting like my life depends on it.”

“That’s the answer.”

“What?”

“Going at it like it’s do or die. That’s the answer. Later, when death really is staring you in the face, you’ll regret this moment.”

I tied back my disheveled hair and continued.

“Ah, I should’ve worked harder back then. You know, that kind of regret.”

I prided myself on having worked so hard as a Hunter that I had practically shit blood. But even after doing all that, regret was what remained.

Regret always came too late. It only struck with bone-deep pain after you had lost something precious.

“Your life, your wealth, or someone you care about. If you don’t want to lose something precious, put your life on the line now. Working yourself to death while you’re alive is still better than actually dying, isn’t it?”

“Uh…”

Hyuk Mujin stared at me with round eyes.

“You’re talking like someone who’s been through it.”

“Why? Is that strange?”

“Words feel different depending on whose mouth they come from. The Captain I know is, um…”

“Not exactly someone who should be saying that, having grown up as a young master with nothing to envy?”

“If I had to put it that way, then yes. You look like someone who’s never lost anything precious in his life, but you talk like a battle-hardened veteran who’s been through every possible hardship.”

This guy had pretty good instincts.

Or maybe that was how I looked to everyone else, too.

I simply let out a quiet laugh without answering. Hyuk Mujin studied me suspiciously.

“What’s with that laugh?”

“I was just thinking you’re pretty perceptive.”

“Captain, you’re not a fake, are you?”

“What?”

“It’s a little late to bring this up, but… you’ve changed too much. Your personality, your martial arts—everything. You’re like a completely different person.”

“Haven’t you heard the rumors? I’m a secret weapon secretly raised by the Jin Family of Taiyuan.”

“Rumors are just rumors—unverified ones. Plenty of people saw you carousing and wasting your time, Captain.”

“You were one of them?”

“Yes. At first, I thought you might be wearing a human-skin mask, but that doesn’t seem to be it.”

“A human-skin mask? The kind where you peel the skin off someone’s face and wear it?”

“See? You ask again as if you’re hearing about it for the first time. You also say things that make no sense all the time.”

“Hmm.”

Come to think of it, at some point I had stopped worrying so much about avoiding suspicion. Everyone around me thought I was Jin Taekyung of the Jin Family of Taiyuan. I had also long since accepted my Murim self as part of who I was.

“If I’m right, and you’re some kind of double put forward by a shadowy organization like the ones in wuxia novels, tell me now. I’ll let it slide quietly.”

“What an absurd thing to say. Then you should report me immediately.”

“Well, I like you much better now than I did before. And I owe you my life. Hehe.”

His lips were smiling, but it wasn’t a joke. The subtle movement of his throat as he swallowed and the slight tremor in his eyes were proof.

I thought for a moment, then opened my mouth.

“Want me to tell you honestly?”

“H-honestly?”

“I’ve been itching to tell someone anyway, so this works out. And the location is perfect.”

Hyuk Mujin glanced around anxiously.

The hollow in the cliff was just large enough for two people to plant their backsides. As luck would have it, the lunatic who would drop a rock on us the moment we stuck our faces outside was waiting nearby, too.

It was the perfect place for two people to sit until one of them died without anyone ever knowing.

“You really are stupid, aren’t you?”

Hyuk Mujin swallowed hard.

“C-C-Captain. I don’t care who you are.”

“Too late.”

“Gasp! I won’t say anything! I meant what I said earlier!”

“What if I told you I belonged to the Demonic Cult?”

“The Demonic Cult!”

“I’m only going to say this once. Listen carefully.”

“I’ll pretend I didn’t hear it. No, I won’t listen!”

Hyuk Mujin’s face turned deathly pale as he tried to cover his ears, but my words came a moment faster.

“I’m actually from another world.”

“...?”

“People can talk to each other even when they’re ten thousand li apart, and monsters with horns or wings roam everywhere. If you put it in Murim terms, I suppose you’d call them evil spirits.”

“...What?”

“Anyway, somehow I ended up here from that kind of world. Then strange things started appearing before my eyes, and suddenly—Level Up! Bam! Points! Boom! Ding-ding-ding-ding inside my head!”

“…”

“Anyway, I only entered the world of martial arts two or three months ago. I’ve wiped the floor with dozens of First Rate masters and taken down three Peak masters. So, any questions?”

Hyuk Mujin slowly lowered the hands that had been half-covering his ears.

His expression was complicated, a mixture of irritation and relief.

“Whew. Let’s just say I was wrong. Happy now?”

“Why? It’s the truth. You don’t believe me?”

“Not even a stray dog would believe that. If only my martial arts were stronger…”

*Smack!*

After smacking him on the back of the head, I stood up.

It was a true story, but it didn’t sound true.

Of course, I had expected Hyuk Mujin to react this way. That was precisely why I had told him.

Someone coming from another world? Anyone would think that was ridiculous.

“Nevel-up? Poin-two? Good grief, I should just stop talking. I don’t know what I expected from you, Captain.”

“What did you expect? The Demonic Cult? The Blood Cult?”

“Oh, come on! Just stop!”

I grabbed Hyuk Mujin by the shoulder as he stood up. The next instant, a murderous shriek of displaced air filled the space, and a boulder as tall as a grown man shot past us.

“Watch yourself. We still have a long way to go.”

I patted him on the back and started climbing the cliff again.

We were only halfway to the summit.

* * *

The moment Hyuk Mujin and I finally reached the summit, System notifications burst forth like celebratory cannon fire.

*Ding. Ding. Ding.*

> **System**
>
> - **Cliff climb:** 10 times (10/10)
>
> - Quest successfully completed!
>
> - New martial art, **Wall Lizard Technique**, is now activated!
>
> - Because you achieved outstanding results that exceeded expectations, you will receive an additional reward!
>
> - Level Up!
>
> - You have acquired 10 Stat Points and 10 Skill Points!
>
> - The Title **Beginner Trainee** has been upgraded to **Intermediate Trainee**!
>
> - Open the relevant System window to check and apply the changes.

Cheongpung beamed at us.

“Wow! You really did it!”

“...What’s that supposed to mean?”

“By any chance—”

*This bastard. Don’t tell me…*

At the sharp look the two of us gave him, Cheongpung shook his head.

“It’s nothing. It took me fifteen days, you see. I didn’t expect you to finish so quickly.”

“Fifteen days?”

Hyuk Mujin repeated the number, then stared at me in disbelief.

Who was Cheongpung? The Sword Saint’s successor, a Peak master who had defeated Jin Mukyung. It was only natural that Mujin couldn’t believe we had achieved this faster than he had.

But…

“What are you so happy about, punk? We’re not the same age. Right?”

“I wasn’t even that young! I was already ten years old!”

“...Isn’t ten usually considered young?”

Cheongpung smiled brightly as he reminisced about those days.

“Back then, climbing up Falling Goose Peak and falling back down was part of my daily routine. It was so much fun.”

“Falling Goose Peak?”

“It’s a peak on Huashan. It’s comfortably more than five hundred jang high. Oh, of course, I couldn’t climb all the way to the top until I was eighteen.”

“…”

“…”

Wasn’t he too young even to watch a movie rated fifteen-plus?

At that age, he would’ve only been in third grade—barely old enough to count as a snot-nosed schoolkid.

*When I was that age, I was playing on the jungle gym in the school playground…*

That bastard Cheongpung had been playing on the mountain peaks of Huashan.

As expected of the continent. The scale was completely different.

“Anyway, you both worked incredibly hard. You achieved something amazing!”

Cheongpung clapped excitedly all by himself, then continued.

“So, about that…”

Sensing something ominous, Hyuk Mujin hurriedly cut in.

“No. Hold on. Wait just a second.”

“I know lots of other fun training exercises.”

“Hey! I said wait a second!”

Hyuk Mujin lunged at him with a shout, but it was already too late. Cheongpung effortlessly subdued him with a grappling technique and called out energetically,

“Let’s all give it our best!”

*Ding.*

> **System**
>
> - **Cheongpung** is in extremely high spirits over your outstanding achievement!
>
> - As a special reward, the linked Quest **Sword Saint Training: A Secondhand Experience—2** has been generated!

“You bastard! Let go of my arm right now!”

As I listened to Hyuk Mujin shout, a question suddenly occurred to me.

*How many of these linked Quests are there?*

One thing was certain.

There was no way Cheongpung would stop at a measly two.

*He’s going to work us into the ground.*

I left Hyuk Mujin’s shrill shouting behind and looked up at the sky.

The vast sky was an intense blue. The air was cool, and several hawks floated overhead with their enormous wings spread wide.

New Year’s Day was ten days away.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 154`.

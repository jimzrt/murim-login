# Master Edit Task — Chapter 155

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
| 진위경    | **Jin Wikyung**    |
| 위팽     | **Wipeng**         |
| 백무성    | **Baek Museong**   |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 무신     | **Martial God**               | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 화산파    | **Huashan**                      |
| 산서오문   | **Five Gates of Shanxi**         |
| 삼류     | **Third Rate**    |
| 이류     | **Second Rate**   |
| 무인     | **martial artist**                               | Default term                                          |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장문인    | **Sect Leader**                              |
| 표국     | **Escort Bureau**                            |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 청해     | **Qinghai**            |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 정마대전   | **Great Faction War**         |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 태사부 | **Grandmaster** | Huashan title referring to Mae Jonghak. |
| 화산일학 | **Huashan’s Lone Crane** | Epithet of Baek Museong. |
| 매화삼절 | **Three Plum Blossom Elites** | Collective title for the current Sect Leader’s three exceptional disciples. |
| 매화검수 | **Plum Blossom Swordsmen** | Huashan appointment held by its three elite disciples. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 황하방 | **Yellow River Gang** | Organization involved in a dispute with the Sogong Sect. |
| 소공문 | **Sogong Sect** | Sect involved in a dispute with the Yellow River Gang. |
| 남부상회 | **Southern Merchant Guild** | Merchant organization whose matter is reported to Jin Wikyung. |
| 내당주 | **Inner Hall Master** | Title for the head of the Jin Family's Inner Hall. |
| 내외당 | **Inner and Outer Halls** | The Jin Family's two internal administrative divisions. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 진위경 | 홍진 | political_host_to_deputy_military_commissioner | Comrade Hong | formal-polite and playful | Jin Wikyung adopts Hong Jin's requested casual address, 홍 동지. |
| 홍진 | 진위경 | deputy_military_commissioner_to_lesser_family_head | Lesser Family Head Jin | formal and teasing | Hong Jin addresses Jin Wikyung as 진 소가주님 while flattering and joking with him. |
| 유생 | 진위경 | scholar_to_lesser_family_head | Lesser Family Head | formal-deferential | The scholar reports matters to Jin Wikyung and apologizes for his inadequate proposal. |
| 진위경 | 유생 | lesser_family_head_to_scholar | you | formal-but-familiar | Jin Wikyung uses 자네 while correcting and instructing the inexperienced scholar. |
| 위팽 | 유생 | senior_retainer_to_scholar | you | familiar and probing | Wipeng uses 자네 while asking the scholar for his assessment. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 진위경 | 백무성 | host_to_visiting_martial_artist | Young Hero Baek | formal-polite | Uses 백 소협 when asking whether anything is wrong. |
| 백무성 | 청풍 | Martial_Nephew_to_Martial_Uncle | Martial Uncle | formal-deferential | Baek formally identifies himself as Cheongpung's Martial Nephew. |
| 위팽 | 청풍 | Jin Family retainer to visiting Huashan martial artist | Young Hero Cheongpung | formal-polite and worried | Uses 청 소협 while warning that Cheongpung's refusal of the Sect Leader's order could strain relations between the Jin Family and Huashan. |
| 청풍 | 백무성 | Martial_Uncle_to_Martial_Nephew | Martial Nephew | affectionate-casual | Cheongpung accepts Baek Museong's apology by calling him 사질. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 백무성 | 진위경 | visiting_martial_artist_to_lesser_family_head | Great Hero Jin | formal-polite | Baek Museong uses 진 대협 while urging Jin Wikyung to stop the duel. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 150–154

## Plot

Four days after losing to Cheongpung, Jin Mukyung isolates himself and trains, realizing that his reputation as the Heaven Shaking Sword and one of the Ten Dragons and Phoenixes had made him a frog in a well. The defeat sharpens his ambition, and his Sword Energy becomes denser and more refined.

Jin Taekyung attempts to force open his Conception and Governor Vessels using his accumulated internal energy and the Scorching Yang Qi from the Blazing Flame Divine Pill. The attempt fails, slightly damages his acupoints, reduces his Sinews and Meridians by one, and leaves him severely injured. Cheongpung explains that Mae Jonghak forbade forcing the vessels open and agrees to train Taekyung after revealing that his own Governor Vessel opened naturally through enlightenment. Taekyung also persuades Hyuk Mujin to join the training.

Cheongpung makes them run to the training hall and climb a sheer cliff using the Wall Lizard Technique, without internal energy or weapons. He throws rocks at them throughout the exercise, rescues Mujin from a fall with the Zaha Divine Technique, and demands ten total ascents. Taekyung and Mujin complete the climbs over three days. Taekyung gains Strength, Agility, and Stamina during the training, acquires Wall Lizard Technique, levels up with 10 Stat Points and 10 Skill Points, and advances from Beginner Trainee to Intermediate Trainee. Cheongpung’s satisfaction generates the linked quest *Sword Saint Training: A Secondhand Experience—2*. Taekyung jokingly claims to have come from another world with a System, but Mujin does not believe him.

Meanwhile, Jang Childeuk begins guarding the Jin Family’s mostly unused training hall. The post is maintained as a symbol because Founder Jin Muryang allegedly trained beneath its cliff and opened the base with One Strike. Taekyung later falls from the cliff, slowing himself with a dagger and surviving through his physique and toughness. Childeuk and the other guard mistake him for a jiangshi until Childeuk recognizes him; Taekyung’s first words after waking mention Taecho Village again.

## Continuity

- Jin Mukyung lost to Cheongpung after roughly three hundred exchanges and has secluded himself to train. His ambition and Sword Energy have strengthened.
- Taekyung failed to force open the Conception and Governor Vessels, suffering slight acupoint damage and a one-point reduction in Sinews and Meridians.
- Cheongpung’s Governor Vessel opened naturally through enlightenment two years earlier; Mae Jonghak warned him never to force either vessel open.
- Cheongpung is training Taekyung and Hyuk Mujin with Mae Jonghak’s cliff-climbing method. The ten climbs are complete.
- Taekyung now has Wall Lizard Technique, 10 additional Stat Points, 10 additional Skill Points, and the Intermediate Trainee rank.
- *Sword Saint Training: A Secondhand Experience—2* has begun or been generated; the number of linked quests in the sequence remains unknown.
- Hyuk Mujin has accepted Taekyung’s training invitation and demonstrated persistence and martial talent. He does not believe Taekyung’s story about another world and a System.
- Jang Childeuk is now a martial artist directly under Jin Wikyung and guards the Jin Family training hall. He remains intensely loyal to the family.
- Taekyung survived his fall at the training hall but again mentioned Taecho Village after regaining consciousness. What Taecho Village is, and why he says “again,” remain unresolved.
- New Year’s Day is ten days away; Prince Shangshan Zhu Bao is expected at the Jin Family’s grand banquet around then.
- Cheongpung still lacks a martial title, which Zhu Bao requires before accepting his autograph.
- Mae Jonghak’s disappearance, Cheongpung’s unexplained origin, and the meaning of the crane that supposedly delivered him remain unresolved.

## Translation Decisions

- Render **임독양맥** as “Conception and Governor Vessels,” **근맥** as “Sinews and Meridians,” **기해** as “qi sea,” and **환골탈태** as “Bone Transformation.”
- Render **벽호공** as “Wall Lizard Technique,” **연무장** as “training ground,” **수련동** as “training hall,” and **청석** as “bluestone.”
- Render **진무량 조사** as “Founder Jin Muryang,” **천응** as “Heavenly Eagle,” **강시** as “jiangshi,” and **태초 마을** as “Taecho Village.”
- Render **초보 수련자** and **중급 수련자** as “Beginner Trainee” and “Intermediate Trainee.”
- Render **검성 수련 간접 체험기** and **검성 수련 간접 체험기-2** as “Sword Saint Training: A Secondhand Experience” and “Sword Saint Training: A Secondhand Experience—2.”
- Retain “His Highness” for formal **전하**, “king” for literal **왕**, “Sword God” for **검신**, “Sword Saint” for **검성**, and “Zaha Divine Technique” for **자하신공**.

### Prior accepted reading-copy tails

#### Chapter 153 tail (verified mastered)

…
climbed, the more treacherous the slope became and the smoother the surface grew. The cliff was already slippery enough. On top of that, the scattered snow flurries that came almost every day and the wind blowing in from the northern Gaoyuan had turned it into one enormous sheet of ice. *Dead end. I can’t see a way forward.* As I worried at my lip, something suddenly caught my eye. A crack in the rock blocked by a snowball that had not yet frozen. It was a tiny space, barely wide enough for one finger. It would be difficult, but I had no other choice. “Hup!” I launched myself forward with a shout, simultaneously jamming my smallest finger—the little finger—precisely into the crack. *Thud.* My prediction had been only half right. I could break through the unfrozen snowball, but the crack was much shallower than I had expected. It was barely one finger joint deep. And I had to support a body weighing 0.1 tons with my little finger. “Ungh.” Even for me, this was asking a bit much. To make matters worse, my finger was slowly slipping because of the moisture pooled inside the crack. *If I waste any more time, I’ll fall.* There was not much farther to go. I steadied my breathing and calmed the tension in my body. Using my little finger as a support, I lifted my entire body. Physical ability truly worthy of the word superhuman. > **System** > > - **Strength** increased by 1. > > - **Agility** increased by 1. > > - **Stamina** increased by 1. Even my stats rose at just the right moment. Just as I smiled triumphantly and reached toward the next crack— *Hup!* “Captain!” Damn it. My breathing faltered at the worst possible moment. As I steadied it again, Hyuk Mujin kept shouting. “Th-this! This!” “What are you saying? I can’t hear you!” The fierce snowstorm scattered sound and obscured my vision. I was about to open my mouth again when a clear shout struck my ears. “Above! Above!” “Above?” The fact that I could hear Hyuk Mujin’s voice meant the savage wind had paused. Only then did my obstructed vision clear and my ears open. Following Hyuk Mujin’s gesture, I raised my head and finally saw it. A massive boulder falling straight toward my face. *Whoooosh!* “Ah, shit.” *Boom!* * * * “Wow. I can’t believe you broke such a huge boulder with your bare fist.” I let Cheongpung’s admiration go in one ear and out the other as I collapsed onto my back. Only a moment ago, I had wanted nothing more than to beat that bastard senseless. Now I was completely drained. *I made it up. It’s over!* Just as I lay there, unable to move even a hand and cheering inwardly, a bluish, frozen hand reached the summit. “Huff. Haaah.” “You succeeded in only one day! You’re both incredible!” If it weren’t for you, I would’ve made it in one shichen, you idiot. I wanted to lay into him, but I was too exhausted to speak. As Hyuk Mujin and I panted with exhaustion and accomplishment, Cheongpung bowed deeply. “Thank you both for your hard work! Now that you’ve succeeded once, you should be able to climb the remaining nine times much faster.” “…” “…” The words were so shocking that Hyuk Mujin and I forgot even to pant as we stared at him. *What is he talking about?* Could he possibly mean what I thought he meant? No, surely not. As an intellectual of modern society, I spoke with a calm demeanor. “The remaining nine times? What kind of bullshit is that?” “My grandfather…” Was this bastard a wild man or a boy detective? At that moment, Sword Saint or whatever be damned—I couldn’t help seeing red. “So you’re telling us to do this nine more times?” “Yes!” “And you’ll throw rocks at us from up here just the same?” “Yes!” “No.” “What?” Hyuk Mujin and I dropped flat at the same time. “I’m not doing it. I don’t even have the strength to go back down. Go ahead and gut me.” “Gut me too, you vicious bastard!” “Puhahaha.” “…Are you laughing?” Cheongpung smiled brightly. “Sorry. You looked just like I did when I first started training, so I couldn’t help it.” “See? You didn’t want to do it either!” “No. I thought it was fun and wanted to keep going, but my body wouldn’t keep up.” Hyuk Mujin muttered quietly enough that only I could hear. “…Is he insane?” “So I told my grandfather. I asked whether I could continue the next day because my legs wouldn’t listen to me.” As he reminisced about his happy past, Cheongpung suddenly drew his sword. At the same time, purple Sword Energy shot forth. *Shhk.* Ice, dirt, rock—Cheongpung cut through all of it without distinction, then continued speaking. “My grandfather said climbing up was hard, but going down was easy. He said if I endured it for just a moment, I’d be back down in no time.” *Rumble, rumble, rumble.* The edge of the cliff ledge where Hyuk Mujin and I were lying—barely ten square meters in size—began to shake. *Is this for real?* As we lay there in a daze, Cheongpung waved at us. “Nine more to go.” > **System** > > - The Quest **Sword Saint Training: A Secondhand Experience** has been generated.

#### Chapter 154 tail (verified mastered)

…
as he tried to cover his ears, but my words came a moment faster. “I’m actually from another world.” “…?” “People can talk to each other even when they’re ten thousand li apart, and monsters with horns or wings roam everywhere. If you put it in Murim terms, I suppose you’d call them evil spirits.” “…What?” “Anyway, somehow I ended up here from that kind of world. Then strange things started appearing before my eyes, and suddenly—Level Up! Bam! Points! Boom! Ding-ding-ding inside my head!” “…” “Anyway, I only entered the world of martial arts two or three months ago. I’ve wiped the floor with dozens of First Rate masters and taken down three Peak masters. So, any questions?” Hyuk Mujin slowly lowered the hands that had been half-covering his ears. His expression was a complicated mixture of irritation and relief. “Whew. Let’s just say I was wrong. Happy now?” “Why? It’s true. You don’t believe me?” “Not even a stray dog would believe that. If only my martial arts were stronger…” *Smack!* I smacked him on the back of the head, then stood up. It was a true story, but it didn’t sound true. Of course, I had expected Hyuk Mujin to react this way. That was precisely why I had told him. Someone coming from another world? Anyone would think it was ridiculous. “Nevel-up? Poin-two? Good grief. I should’ve kept my mouth shut. I don’t know what I expected from you, Captain.” “What did you expect? The Demonic Cult? The Blood Cult?” “Oh, come on! Just stop!” I grabbed Hyuk Mujin by the shoulder as he stood up. The next instant, a boulder as tall as a grown man shot past us with a murderous shriek of displaced air. “Watch yourself. We still have a long way to go.” I patted him on the back and resumed climbing. We were only halfway to the summit. * * * The moment Hyuk Mujin and I finally reached the summit, System notifications erupted like celebratory cannon fire. *Ding. Ding. Ding.* > **System** > > - **Cliff climb:** 10 times (10/10) > > - Quest successfully completed! > > - New martial art, **Wall Lizard Technique**, is now activated! > > - You have achieved outstanding results beyond expectations. An additional Reward will be granted! > > - Level Up! > > - You have acquired 10 Stat Points and 10 Skill Points! > > - The Title **Beginner Trainee** has been upgraded to **Intermediate Trainee**! > > - Open the relevant System window to check and apply the changes. Cheongpung beamed at us. “Wow! You really did it!” “…What’s that supposed to mean?” “By any chance—” *This bastard. Don’t tell me…* At the sharp looks we gave him, Cheongpung shook his head. “It’s nothing. It took me fifteen days, you see. I didn’t expect you to finish so quickly.” “Fifteen days?” Hyuk Mujin repeated the number, then stared at me in disbelief. Who was Cheongpung? The Sword Saint’s successor and a Peak master who had defeated Jin Mukyung. Mujin must have found it hard to believe that we had achieved this faster than he had. But… “What are you so happy about, punk? We’re not the same age. Right?” “I wasn’t even that young! I was already ten years old!” “…Isn’t ten usually considered young?” Cheongpung smiled brightly as he reminisced about those days. “Back then, climbing up Falling Goose Peak and falling back down was part of my daily routine. It was so much fun.” “Falling Goose Peak?” “It’s a peak on Huashan. It’s easily more than five hundred jang high. Oh, of course, I couldn’t make it all the way to the top until I was eighteen.” “…” “…” Wasn’t ten too young even to watch a movie rated fifteen-plus? At that age, he would’ve only been in third grade—barely old enough to count as a snot-nosed schoolkid. *When I was that age, I played on the jungle gym in the schoolyard…* That bastard Cheongpung had played on the peaks of Huashan. As expected of the continent. Everything was on a different scale. “Anyway, thank you both so, so much for your hard work. You achieved something amazing!” Cheongpung clapped excitedly all by himself, then continued. “So, about that…” Sensing something ominous, Hyuk Mujin hurriedly cut in. “No. Hold on. Wait just a second.” “I know lots of even more fun training exercises.” “Hey! I said wait a second!” Hyuk Mujin lunged at him with a shout, but it was already too late. Cheongpung effortlessly subdued him with a grappling technique and called out energetically, “Let’s all give it our best!” *Ding.* > **System** > > - **Cheongpung** is in extremely high spirits over your outstanding achievement! > > - As a special Reward, the linked Quest **Sword Saint Training: A Secondhand Experience—2** has been generated! “You bastard! Let go of my arm right now!” As I listened to Hyuk Mujin shout, a question suddenly occurred to me. *How many linked Quests are there?* One thing was certain. There was no way Cheongpung would stop at a measly two. *He’s going to work us into the ground.* Leaving Hyuk Mujin’s squawking behind me, I looked up at the sky. The vast sky was a brilliant blue. The air was cool, and several hawks drifted overhead with their enormous wings spread wide. New Year’s Day was ten days away.

## Korean source

```text
＃155화



적막한 공간. 예닐곱 명의 유생들이 정신없이 업무에 몰두하고 있었다.

그들은 초췌한 얼굴로 산처럼 쌓인 죽간을 하나씩 처리해 나가는 한편, 여러 사안을 집무실의 주인에게 보고했다.

“황하방과 소공문 사이에 분쟁이 일어났습니다. 본가에 중재를 청해 왔는데…….”

“원단에 자리를 마련할 테니 그때 이야기하자 전하게. 내당주에게 미리 일러 놓고.”

“산서오문에 관한 사안은 어떻게 하는 게 좋겠습니까?”

“아, 셋째와 관련된 일인가?”

“예. 산서오문의 당주들이 사죄의 말씀을 전하기 위해 기다리고 있습니다.”

“돌려보내게. 정말 아쉬웠다면 손발을 보낼 게 아니라 머리가 직접 왔어야지. 그것도 내당주에게 일러 놓고.”

“다음은 남부상회(商會)에서…….”

사안을 보고받는 와중에도 집무실의 주인, 진위경은 죽간에서 눈을 떼지 않았다.

그러나 이어지는 보고에는 그도 고개를 들 수밖에 없었다.

“소가주님. 대동(大同) 부근에서 북부 고원의 마적단들이 수상한 움직임을 보이고 있습니다.”

“마적? 하오문에서 보낸 소식인가?”

“예. 이대로 내버려 둔다면 양민들을 대상으로 대대적인 노략질이 있을 겁니다.”

“규모는?”

“다섯 개의 마적단이 연합, 약 오백에 달하는 인원이 속속 집결 중입니다.”

“마적들이라. 두고두고 말썽이로군.”

진위경은 피곤한 얼굴로 미간을 문질렀다.

태원진가의 세력이 막강한 것은 사실이지만 아직 산서 전역을 아우르기에는 역부족이다.

적풍단의 궤멸을 알고 있음에도 마적들이 호시탐탐 기회를 엿보는 이유이기도 했다.

“무인들을 차출할까요?”

유생의 말에 진위경이 곧장 고개를 가로저었다.

“불가.”

“근래 본가에 입문한 무인들은 헤아릴 수도 없습니다. 충분한 여력이 있습니다.”

“그러기에는 이미 너무 많은 피를 흘렸네. 게다가 이번에 받아들인 이들은 아직 경험이 부족해. 수백을 충원해도 수백이 죽어 나가겠지.”

항산검문.

산서성이라는 세발솥을 지탱하던 다리 하나가 부러지니 담겨 있던 물이 흘러넘치기 시작했다.

펄펄 끓는 물에 화상을 입기 전에 대책을 강구해야 했다.

잠시 고민하던 진위경이 입을 열었다.

“당분간은 각 군현에 지부를 설립하고 안정화하는 것에 집중하게. 그게 최우선일세.”

“소가주님!”

유생이 깜짝 놀라 외쳤다. 각자 맡은 일에 집중하고 있던 다른 이들도 고개를 들었다.

수백의 마적단이 쳐들어온다는데 지부 설립이 최우선이라니. 양민들이 죽건 말건 신경 쓰지 않겠다는 것인가?

유생들의 얼굴에 실망이 번질 때, 진위경의 말이 이어졌다.

“대신 산서오문에 지원을 요청하게. 이백 정도면 적당할 것 같은데…… 어떻게 생각하나?”

“그 정도로는 턱도 없습니다.”

태원진가의 소가주에게 이렇게 직설적으로 말할 수 있는 사람은 적어도 이 집무실 안에 없다.

진위경이 막 문을 열고 들어오는 위팽을 보며 씩 웃었다.

“그런가? 난 충분할 것 같은데.”

“지금의 산서오문이 어떤 자들입니까? 이전투구에 혈안이 된 자들입니다. 공들여 기른 정예는 담장 안에 꽁꽁 숨겨 두고 어리바리한 이류, 삼류들로 꽉꽉 채워서 보내겠죠.”

“그럴듯하군.”

“그럴듯한 정도가 아니라 십중팔구입니다. 솜털 보송보송한 어린놈들을 보고 마적 놈들만 좋아서 입이 찢어지겠군요.”

“하하, 그래서 우리가 나서야 한다?”

“별수 있겠습니까? 쓸 만한 놈들로 붙여 주시면 제가 직접 다녀오겠습니다. 그럼 산서오문 쪽에서도 얌생이 짓은 못 할 테니까요.”

“그렇지. 귀신보다 무서운 게 귀검(鬼劍) 아닌가?”

놀리듯이 말하는 진위경의 목소리에 위팽이 고개를 절레절레 흔들었다.

“이제 그만하시고 알려 주십시오.”

“뭘?”

“이미 생각해 둔 방도가 있으시지 않습니까?”

“방도는 무슨. 자네 의견 좋던데?”

“거참. 언제부터 제 말을 그렇게 귀 기울여 들으셨다고.”

“자네 입에서 나오는 말은 내게 금과옥조지.”

한숨을 푹 내쉰 위팽이 멀거니 서 있는 유생을 향해 고개를 돌렸다.

“자네는 어떻게 생각하나?”

“예, 예?”

마른 체구에 희멀건 얼굴. 방구석에서 서책이나 들여다보던 백면서생의 표본이다.

위팽의 갑작스러운 질문에 그가 더듬더듬 대답했다.

“여, 역부족이라고 생각합니다.”

“그게 끝인가?”

“인원을 더 차출해야…….”

그 모습을 지켜보던 진위경이 웃으며 끼어들었다.

“거기까지 하게. 그리고 자네.”

위팽의 날카로운 기세에 위축되어 있던 유생이 몸을 움찔 떨었다.

“예.”

“산서오문. 그리고 산서성부에 연통을 넣게. 대동 근방에 마적들이 들끓으니 도움을 바란다고 말이야.”

“산서성부 말입니까?”

“백성이 위험에 처했는데 나라가 발 벗고 나서야지. 아, 산서오문 쪽에도 슬쩍 그에 대해 언질 하고.”

“근 몇 년간 보여 준 관의 소극적인 태도를 보아 성사될 가능성은 희박합니다.”

“성사시켜야지.”

진위경이 웃음기가 사라진 얼굴로 한마디를 덧붙였다.

“그게 자네 할 일 아닌가?”

“아.”

유생은 정신이 번쩍 들었다. 며칠 밤을 새는 바람에 지쳐 있었다고는 하나 너무 쉽게 생각하고 있었다.

산서성에 도움을 요청하라니. 차라리 뼛속까지 무인인 위팽이 내놓은 의견이 훨씬 그럴듯한 대책이다.

“송구합니다.”

“아직 서투를 테니 이해하네. 하지만 본가에 필요한 건 유생이 아니라 본가를 위해 최선의 대책을 내놓을 지자(智者)야. 내 말을 잘 기억하길 바라네.”

유구무언이다. 눈앞의 유생뿐만 아니라 모두의 얼굴이 붉어진 걸 확인한 진위경이 재차 입을 열었다.

“다들 피곤할 테니 오늘은 이만 들어가 쉬게.”

쉬라는데 거부할 사람은 없다. 사흘째 죽간을 베개 삼아 쪽잠으로 버티던 이들이라면 더더욱.

유생들이 지친 몸을 이끌고 빠져나가자 위팽이 빈 의자를 끌어당겼다.

“새로 뽑은 자들입니까?”

“역시 혼자서는 역부족이더군. 그래도 없는 것보다는 나아.”

“글쎄요. 어째 다들 밍밍합니다만.”

“저들 중 본가에 들어오려고 학문을 익힌 이들이 몇이나 되겠나? 어쩌면 당연한 거지.”

진위경이 기지개를 쭉 켰다. 우두둑, 뼈 어긋나는 소리가 요란하게 울려 퍼졌다.

“아직 며칠밖에 안 됐어. 옥석을 가려내고 떠날 자는 떠나보내야지.”

“굳이 산서성부와의 밀약을 알리지 않으신 이유도 그 때문입니까?”

“밀약(密約)이 왜 밀약인가? 아는 사람은 적을수록 좋아.”

사실 산서성부의 도움을 이끌어 내는 것은 그리 어려운 일이 아니다. 이미 닷새 전 방문한 도지휘동지 홍진과의 대화를 통해 많은 것을 주고받지 않았던가?

“본가는 아직 완전히 자리를 잡지 못했네. 이런 상황에서 관과 밀약을 맺었다는 식의 소문이 떠돌면 곤란하지.”

“그건 그렇지요. 소문이 아니라 사실일 경우에는 더더욱.”

홍진과 주고받은 대화에는 산서성의 중소 문파들, 그중에서도 산서오문이 달가워하지 않을 만한 주제들이 여럿 끼어 있다.

특히 성운표국 측에서 진위경과 홍진의 대화를 듣게 된다면 입에 거품을 물고 쓰러질지도 모르는 일이다.

“그래, 다른 준비는 잘되어 가고?”

“예. 분부하신 대로 인사 조치를 끝냈습니다. 내외당의 당주들은 그대로 두었고, 세 개의 대(隊)를 신설했으며…….”

위팽의 입에서 흘러나오는 보고는 진위경이 종전 직후 가장 먼저 처리한 부분이다.

현재의 태원진가는 떠오르는 태양과 같다. 한창 피 끓는 산서성의 젊은이들에게는 최고의 선택지.

끊임없이 몰려드는 이들을 모두 포용하기 위해서는 품이 더욱 넓어져야 했다.

“……이렇게 처리했습니다만, 계속해서 규모가 늘어날 예정이니만큼 추후 재정비가 필요해 보입니다.”

“그러길 바라야지.”

위팽의 보고를 들은 진위경은 담담한 척하려 애썼다.

정마대전 이후 조금씩, 그리고 꾸준히 쇠락해 가던 태원진가다. 그러나 지금의 태원진가는 빠르게 과거의 성세를 회복해 가고 있었다.

‘아니, 어쩌면 정마대전이 일어나기 이전보다 더욱 강성해질지도 모른다.’

만약 그렇게 된다면…….

그때야말로 세가(世家)의 자격을 갖추게 된다.

변방의 무가를 벗어나, 천하의 거목들과 어깨를 나란히 하게 되는 것이다.

‘세가, 세가라는 말이지.’

생각만 해도 가슴이 뛰는 단어다.

모든 무인이 무신을 꿈꾸는 것처럼, 진위경은 가문을 세가의 반석에 올리기를 오랫동안 소원해 왔으니까.

‘이제 곧 원단이다.’

그 날, 산서 무림의 모든 문파가 보는 앞에서 태원진가는 명실상부한 산서성의 패자로 인정받는다.

곧 다가올 새해 첫날이 태원진가가 세가로 나아가는 첫 발판이자 효시가 될 것이라 진위경은 믿어 의심치 않았다.

그리고 그가 남몰래 주먹을 꽉 움켜쥔 그 순간이었다.

“저어, 들어가도 되겠습니까?”

“응? 물론일세.”

곧이어 등장한 목소리의 주인공은 방금 떠났던 유생이었다.

“무슨 일인가? 놓고 간 물건이라도 있나?”

“그것이 아니라…….”

진위경과 위팽의 의아한 시선을 받은 그가 조심스럽게 말을 이었다.

“미처 보고드리지 못한 소식이 있습니다.”

“사람도 참 고지식하기는. 며칠 동안 잠도 제대로 못 자고 고생했는데 괘념치 말고 들어가서 푹 쉬시게.”

“아닙니다. 제가 진작 말씀드렸어야 했는데 깜빡하는 바람에…….”

“어허, 괜찮네. 그만 쉬라니까.”

위팽도 한마디 거들었다.

“소가주님 말씀이 맞네. 사람이 강시도 아니고, 충분한 휴식을 취해야 다음 날도 힘내서…….”

“화산파에서 매화삼절(梅花三晣)을 보냈답니다.”

진위경과 위팽이 동시에 자리에서 벌떡 일어났다.

“뭣이!”

“뭐라!”

매화삼절이 누군가.

화산파의 최정예로 불리는 매화검수. 그중에서도 두각을 드러낸 걸출한 기재들이다.

특히 화산일학 백무성은 화산파의 미래를 짊어질 차기 장문인으로 꼽히는 거물.

그런 얘길 들었으니 두 사람의 눈이 튀어나올 수밖에 없었다.

“그게 정말인가?”

“예, 마지막에 말씀드리려다가 그만. 그리고 하나 더 있습니다.”

“하나 더?”

“또? 어서 말해 보게!”

매화삼절의 방문만 해도 놀라운데, 하나가 더 있단다.

유생이 눈살을 찌푸리며 말을 이었다.

“태사부께서 사라지셨다고. 본가로 가신 것 같으니 뵙게 되면 꼭 좀 연통을 넣어 달라 하는데…… 태사부가 누굽니까?”

아직 무림 실정에 어두운 유생은 이게 뭔가 싶었지만, 진위경과 위팽은 입을 딱 벌렸다.

“화산파의 태사부면…….”

“거, 거, 거…….”

검성 매종학. 차마 입 밖에 내지 못하고 입만 벙긋거린 두 사람이 침을 꿀꺽 삼켰다.

화산파는 아직까지 검성의 행방을 불문에 부쳐 두고 싶어 한다. 이럴 때일수록 말은 아끼는 게 좋다.

“거, 뭐라고 하셨습니까?”

“거, 거시기, 그런 게 있네.”

“예?”

“자네는 이만 나가 보게. 지금 있었던 일은 머릿속에서 지우고. 알겠나?”

유생이 어리둥절한 얼굴로 고개를 숙이고 나가자 비로소 참았던 말이 튀어나왔다.

“검성이 온다!”

“쉿, 목소리 낮추십시오. 아직 확실하지도 않잖습니까.”

말과는 달리 위팽의 얼굴도 홍조로 붉게 달아올라 있었다. 그와 같은 검수(劍手)에게 있어 검성 매종학은 옥황상제 그 이상이었으니까.

그런 분을 직접 만날 수 있다니! 아니, 어쩌면 한 수 가르침까지 받을 수 있을지 모른다.

“그, 그런데 검성이 왜 본가에.”

“뭣 때문이겠나?”

“아.”

너무 흥분한 나머지 깜빡하고 있었다. 지금 태원진가에 누가 와 있는지를.

“그 검성이 애제자를 찾으러 은거를 깼군요.”

“아직은 짐작이지만 그럴 가능성이 농후하지. 친손자처럼 길렀다는데 그 정이야 오죽할까.”

진위경은 싱글벙글 웃었다.

이유야 어찌 되었건 검성의 방문은 한 사람의 무인으로서도, 태원진가의 소가주로서도 쌍수를 들고 환영할만한 일이다.

“청풍이라고 했지, 그 친구는 지금 어디 있나? 막내에게 벽호공 수련시킨다는 이야기를 한참 전에 들은 것 같네만.”

“벽호공 수련은 이틀 전에 끝났고 지금은…….”

“지금은?”

“삼 공자를 줘 패고 있습니다.”

“뭣이이이!”
```

## Current accepted English baseline

```markdown
# Chapter 155

A silent room. Six or seven scholars were frantically immersed in their work.

With haggard faces, they processed the bamboo slips piled up like mountains one by one while reporting various matters to the master of the office.

“There’s been a dispute between the Yellow River Gang and the Sogong Sect. They’ve asked our family to mediate, but…”

“Tell them we’ll arrange a place on New Year’s Day and discuss it then. Inform the Inner Hall Master in advance.”

“What should we do about the matter concerning the Five Gates of Shanxi?”

“Ah, is this related to the third one?”

“Yes. The heads of the Five Gates of Shanxi are waiting to convey their apologies.”

“Send them back. If they were truly sorry, the heads themselves should have come in person instead of sending their hands and feet. Inform the Inner Hall Master of that, too.”

“Next, there’s a matter from the Southern Merchant Guild…”

Even while receiving reports, the master of the office, Jin Wikyung, never looked up from the bamboo slips.

But at the next report, even he had no choice but to raise his head.

“Lesser Family Head, the mounted bandits from the northern plateau are showing suspicious movements near Datong.”

“Mounted bandits? Is this information from the Lower District Sect?”

“Yes. If we leave them alone, they’ll launch a large-scale raid against the common people.”

“How large is their force?”

“Five mounted-bandit groups have formed an alliance. Around five hundred men are gradually gathering.”

“Mounted bandits, huh? They’ve been a constant nuisance.”

Jin Wikyung rubbed the space between his brows with a tired expression.

It was true that the Jin Family of Taiyuan possessed formidable power, but it still lacked the strength to cover all of Shanxi Province.

That was also why the mounted bandits kept watching for an opportunity despite knowing that the Red Wind Band had been annihilated.

“Should we draft some martial artists?”

At the scholar’s question, Jin Wikyung immediately shook his head.

“No.”

“We have more martial artists joining our family than we can count. We have enough manpower.”

“We’ve already shed too much blood for that. Besides, those we accepted this time still lack experience. Even if we recruit several hundred, several hundred will die.”

The Mount Heng Sword Sect.

One of the legs supporting the tripod of Shanxi Province had broken, and the water inside was beginning to spill over.

They had to devise a countermeasure before they were scalded by the boiling water.

After thinking for a moment, Jin Wikyung spoke.

“For the time being, focus on establishing and stabilizing branches in each prefecture and county. That is our top priority.”

“Lesser Family Head!”

The scholar cried out in surprise. The others, who had been focused on their own tasks, also raised their heads.

Hundreds of mounted bandits were supposedly invading, and yet establishing branches was the top priority. Did that mean they did not care whether the common people died?

As disappointment spread across the scholars’ faces, Jin Wikyung continued.

“Instead, request assistance from the Five Gates of Shanxi. Two hundred should be about right… What do you think?”

“That won’t come close to being enough.”

There was no one in this office, at least, who could speak so bluntly to the Lesser Family Head of the Jin Family of Taiyuan.

Jin Wikyung grinned as he looked at Wipeng, who had just entered through the door.

“Is that so? I thought it would be enough.”

“What sort of people are the Five Gates of Shanxi now? They’re obsessed with clawing at one another for scraps. They’ll hide their carefully trained elites inside their walls and send us a force packed with clueless Second Rate and Third Rate martial artists.”

“That sounds plausible.”

“It’s not just plausible. That’s what will happen nine times out of ten. The mounted bandits will see all those peach-fuzzed little punks and be so delighted their mouths will split open.”

“Haha. So we have to step in?”

“What else can we do? If you attach some useful men to the force, I’ll go there myself. Then the Five Gates of Shanxi won’t be able to pull any sneaky tricks.”

“Exactly. Isn’t the Ghost Sword more frightening than a ghost?”

At Jin Wikyung’s teasing tone, Wipeng shook his head from side to side.

“Enough of that. Tell me what you have in mind.”

“What do you mean?”

“You already have a plan, don’t you?”

“What plan? I thought your idea was pretty good.”

“Good grief. Since when have you listened to my words so attentively?”

“Every word that comes out of your mouth is a golden rule to me.”

Wipeng let out a deep sigh and turned toward the scholar standing blankly nearby.

“What do you think?”

“Y-yes?”

A thin frame and a pale, washed-out face. He was the very picture of a pale-faced scholar who did nothing but pore over books in his room.

Startled by Wipeng’s sudden question, he stammered out an answer.

“I-I think it’s insufficient.”

“Is that all?”

“We should draft more men…”

Watching him, Jin Wikyung cut in with a laugh.

“That’s enough. And you.”

The scholar, already cowed by Wipeng’s sharp aura, flinched.

“Yes.”

“Send word to the Five Gates of Shanxi and the Shanxi Provincial Office. Tell them mounted bandits are swarming around Datong and that we request their assistance.”

“The Shanxi Provincial Office?”

“The people are in danger. The government ought to step forward. Ah, casually give the Five Gates of Shanxi a hint about it, too.”

“Judging by the government’s passive attitude over the past several years, the chances of that succeeding are slim.”

“Then make it succeed.”

Jin Wikyung’s face lost its smile as he added one more thing.

“Isn’t that your job?”

“Ah.”

The scholar’s mind snapped awake. He was exhausted from staying up several nights, but he had been thinking far too simply.

Request help from Shanxi Province? The countermeasure proposed by Wipeng, a man who was a martial artist down to his bones, was much more plausible.

“I apologize.”

“You’re still inexperienced, so I understand. But what our family needs isn’t scholars. We need wise men who can offer the best possible measures for the sake of our family. I hope you’ll remember that.”

There was nothing the scholar could say. Seeing that not only the man before him but everyone else had reddened faces, Jin Wikyung spoke again.

“You’re all tired, so go in and rest for today.”

No one would refuse an order to rest. Especially not those who had been surviving on brief naps with bamboo slips for pillows for three straight days.

Once the scholars dragged their exhausted bodies out, Wipeng pulled over an empty chair.

“Are they newly recruited?”

“Being on my own was too much. Still, they’re better than nothing.”

“I’m not sure. They all seem rather bland.”

“How many of them studied in order to join our family? It’s only natural.”

Jin Wikyung stretched his arms high. The loud cracking of bones echoed through the room.

“It’s only been a few days. We need to separate the jade from the stones and send away those who need to go.”

“Is that why you didn’t inform them of the secret agreement with the Shanxi Provincial Office?”

“Why is a secret agreement called a secret agreement? The fewer people who know about it, the better.”

In truth, securing the assistance of the Shanxi Provincial Office was not particularly difficult. Hadn’t he and Deputy Military Commissioner Hong Jin already exchanged plenty through their conversation five days earlier?

“Our family hasn’t fully established itself yet. It would be troublesome if rumors spread that we had entered into a secret agreement with the government under these circumstances.”

“That’s true. Even more so if they weren’t rumors but facts.”

The conversation Jin Wikyung had exchanged with Hong Jin had included several topics that the small and medium-sized sects of Shanxi Province—and especially the Five Gates of Shanxi—would not welcome.

If the Seongun Escort Bureau heard what Jin Wikyung and Hong Jin had discussed, they might collapse frothing at the mouth.

“So, are the other preparations going well?”

“Yes. I’ve completed the personnel changes as you ordered. The heads of the Inner and Outer Halls have been left in place, and we’ve established three new squads…”

The report flowing from Wipeng’s mouth concerned the first matter Jin Wikyung had handled immediately after the war ended.

The Jin Family of Taiyuan was like a rising sun. To the hot-blooded young people of Shanxi Province, it was the finest choice available.

To embrace the endless stream of people coming to them, the family had to widen its arms even further.

“…That’s how I handled it, but since our numbers are expected to continue growing, we’ll likely need to reorganize again later.”

“That’s what we should hope for.”

Jin Wikyung tried to appear calm as he listened to Wipeng’s report.

The Jin Family of Taiyuan had been slowly but steadily declining since the Great Faction War. Yet the Jin Family of Taiyuan now was rapidly recovering its former glory.

*No. Perhaps it will become even stronger than it was before the Great Faction War.*

If that happened…

That would be when they truly earned the right to be called a great family.

They would break free of their status as a frontier martial family and stand shoulder to shoulder with the great powers of the realm.

*A great family. A great family, huh.*

Just thinking about it made his heart race.

Just as every martial artist dreamed of becoming the Martial God, Jin Wikyung had long dreamed of raising his family onto the foundation of a great family.

*New Year’s Day is almost here.*

On that day, before all the sects of Shanxi Murim, the Jin Family of Taiyuan would be recognized as the undisputed hegemon of Shanxi Province.

Jin Wikyung had no doubt that the first day of the coming year would become the Jin Family of Taiyuan’s first stepping-stone—and the harbinger of its rise—as a great family.

And it was at the very moment he secretly clenched his fists that—

“Um, may I come in?”

“Hm? Of course.”

The owner of the voice that appeared next was the scholar who had just left.

“What is it? Did you leave something behind?”

“It’s not that…”

Under the puzzled gazes of Jin Wikyung and Wipeng, the scholar carefully continued.

“There’s some news I failed to report.”

“You’re a stubborn one. You’ve been working hard for days without even getting proper sleep. Don’t worry about it. Go in and get some rest.”

“No. I should have told you earlier, but I forgot…”

“Now, now, it’s all right. I said go rest.”

Wipeng added his voice.

“My lord is right. You aren’t a jiangshi. You need to get enough rest so you can have the strength to work again tomorrow…”

“Huashan has sent the Three Plum Blossom Elites.”

Jin Wikyung and Wipeng shot to their feet at the same time.

“What!”

“What did you say?”

Who were the Three Plum Blossom Elites?

They were Plum Blossom Swordsmen, known as Huashan’s finest. Among them were three outstanding prodigies who stood above the rest.

In particular, Baek Museong, Huashan’s Lone Crane, was a major figure regarded as the future Sect Leader who would carry Huashan’s future on his shoulders.

Having heard that, there was no way the two men’s eyes would not bulge.

“Is that really true?”

“Yes. I meant to tell you at the end, but I forgot. And there’s one more thing.”

“One more?”

“Another? Tell us quickly!”

The visit of the Three Plum Blossom Elites was shocking enough, and now he was saying there was something else.

The scholar continued with a frown.

“They say the Grandmaster has disappeared. He seems to have gone to our family, so they asked us to send word if we happen to meet him… But who is the Grandmaster?”

The scholar was still unfamiliar with the realities of Murim and wondered what this was all about. Jin Wikyung and Wipeng, however, stood with their mouths hanging open.

“If Huashan’s Grandmaster is…”

“Th-the, th-the…”

Sword Saint Mae Jonghak.

The two men could not bring themselves to say the name aloud. They merely moved their lips and swallowed hard.

Huashan still wanted to keep the Sword Saint’s whereabouts secret. At times like this, it was best to keep one’s mouth shut.

“Th-the… What did you say?”

“Th-that thing. You know, that sort of thing.”

“Yes?”

“You can leave now. Erase everything that just happened from your mind. Understood?”

The scholar bowed with a bewildered expression and left. Only then did the words they had been holding back burst out.

“The Sword Saint is coming!”

“Shh! Lower your voice. We don’t even know for certain yet.”

Despite his words, Wipeng’s face had also flushed bright red. To a swordsman like him, Sword Saint Mae Jonghak was greater than even the Jade Emperor.

To think they might be able to meet such a person in the flesh! No, perhaps he might even receive instruction from him.

“B-but why would the Sword Saint come to our family?”

“What else could it be?”

“Ah.”

He had been so excited that he had momentarily forgotten who was currently staying at the Jin Family of Taiyuan.

“That Sword Saint broke his seclusion to look for his beloved disciple.”

“It’s only a guess for now, but that’s highly likely. I hear he raised him like his own grandson. How deep must his affection be?”

Jin Wikyung grinned broadly.

Whatever the reason, the Sword Saint’s visit was something to welcome with open arms—not only as a martial artist, but also as the Lesser Family Head of the Jin Family of Taiyuan.

“You said his name was Cheongpung, right? Where is he now? I seem to remember hearing a while ago that he was training the youngest in the Wall Lizard Technique.”

“The Wall Lizard Technique training ended two days ago, and now he’s…”

“And now?”

“He’s beating the crap out of the Third Young Master.”

“What!”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 155`.

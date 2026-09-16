# Master Edit Task — Chapter 150

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
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 천무학관   | **Heaven's Gate Temple**         |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 임맥     | **Conception Vessel**                            |                                                       |
| 독맥     | **Governor Vessel**                              |                                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 상태               | **Status**                     |
| 보상               | **Reward**                     |
| 청해     | **Qinghai**            |
| 소협      | **Young Hero**                                                  |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 청강검 | **blue-steel sword** | Cheongpung's sword. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 임독양맥 | **Conception and Governor Vessels** | The paired vessels Taekyung attempts to open. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 사해오호 | **Four Seas and Five Lakes** | Traditional geographic phrase used with the Nine Provinces and Eight Wastes. |
| 환골탈태 | **Bone Transformation** | Advanced transformation described as optional in martial-arts novels. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 호승심 | polysemy | Competitive pride or fighting spirit; not merely a desire to test oneself. | test myself |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

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

#### Chapter 148 tail (verified mastered)

…
place to start.” “A first? What does that mean?” “A dueling tour.” Cheongpung smiled softly. It was completely different from the bright, innocent smile I had seen from him until now. “I decided it while coming down the mountain. I won’t return until I’ve defeated all the Ten Dragons and Phoenixes.” “……!” “My grandfather told me this: A martial artist has no need for conversation. We contend through martial arts alone.” Sssss. At that moment, I felt a wave of heat. Violet light-flames had risen around Cheongpung’s entire body, surging upward. I had already seen this once before. *The Zaha Divine Technique.* The Extreme Yang qi burned the cold away. The earth melted, and the soil scorched. Cheongpung opened his mouth with all traces of his smile gone. “Shall we move somewhere else?” “Is there any need?” Jin Mukyung continued. “Draw your sword.” * * * Jin Mukyung let out a long breath. His rapidly beating heart slowly began to settle. Breathing was important in battle. Only now was he finally ready to draw his sword. As he placed a hand on the hilt, he thought of one man’s name. *Sword Saint Mae Jonghak.* Not once had he forgotten that name since the day he first held a sword. A legendary swordsman said to have reached the ultimate realm of the sword—or perhaps a realm beyond it. Everyone revered the Sword Saint, but Jin Mukyung was different. *Someday, I will defeat him.* If anyone had heard him say that, they would have snorted. They would have pointed at him and called him crazy. No matter how much of a genius Jin Mukyung was, he could never reach the Sword Saint’s name. Ever since Mae Jonghak had begun to be called the Sword Saint, no one had surpassed him. Decades ago, Sword Saint Mae Jonghak had already written a new chapter in the history of the orthodox Murim and become the protagonist of a legend. *It doesn’t matter. This is my goal.* It was not reckless arrogance. It was a goal. A goal he had etched into his bones and heart every day as he trained with his sword. And at this very moment, someone who had inherited everything from Sword Saint Mae Jonghak stood before him. “My grandfather used to tell me, ‘Compared to the Ten Dragons and Phoenixes, you are nothing. Don’t become arrogant.’” Cheongpung slowly stepped forward. A single blue-steel sword dangled from his waist, tied on haphazardly, and his footsteps were as light as though he had come out for a stroll. But… *There are no openings.* He looked utterly careless, but Jin Mukyung had no idea when or how he could attack. Jin Mukyung licked his parched lips. “I’ve never even met him… He praised me too highly.” “No. Honestly, you surprised me a little. I mean that.” Jin Mukyung knew that Cheongpung meant every word. That only made him feel stranger. *Only a little?* It had been more than twenty years since he began training with the sword. Talent and effort had brought him this far. People called him a genius, gave him the martial title Heaven Shaking Sword, and counted him among the Ten Dragons and Phoenixes. He had believed he had never once become drunk on such empty fame, but… *I still have a long way to go.* At some point, he must have grown accustomed to the gazes of people who looked up to him. The wound Pung Yang had inflicted on him not long ago seemed to throb again. “Do you know something?” “What?” “That you’re strong.” “Until recently, I wasn’t certain. But now I know.” “Because you met me?” “Yes. Because I met you, Young Hero Jin. Now I know what the Ten Dragons and Phoenixes are capable of.” “Is that so?” Jin Mukyung let out a quiet laugh. What an interesting guy. He possessed martial arts that rivaled—or even surpassed—those of an Elder of the Nine Sects and One Gang, yet he remained untainted by the world. He was pure. Honest. He was a martial artist, but he didn’t fit in the Murim. *He’s the exact opposite of someone I know.* One person suddenly came to mind. A guy who seemed like he could somehow survive no matter where he was thrown in the Murim, and who fought in the least martial-artist-like way imaginable. “How old are you?” “I turned twenty this year.” “We’re even the same age. Coincidence? Or fate?” “What?” Instead of answering, Jin Mukyung shook his head. In truth, he already knew the outcome of this duel. The qi of the Zaha Divine Technique surging through Cheongpung’s entire body was that overwhelming. His only regret was that he couldn’t display the full extent of his skill against an opponent of this caliber. *What would that troublemaker do in a situation like this?* Jin Mukyung glanced at his troublesome younger brother. With a grin like a little devil’s, Taekyung was mouthing something. *You. Are. Fucked.* *What a goddamn bastard.* Laughing hollowly, Jin Mukyung placed a hand on his sword hilt. The internal energy boiling up from his dantian coursed through every part of his body. Cheongpung looked at Jin Mukyung’s sword and spoke. “My grandfather told me something else, too. A duel doesn’t need an opening stance or anything like that.” “I agree.” The next moment— With a tremendous boom, violet light-flames and silver Sword Energy collided.

#### Chapter 149 tail (verified mastered)

…
Since it’s already happened, we could eat something delicious while we travel to our destination…” The young man cut them off in a stern voice. “Since when was running a gambling den an evil deed? Or have you seen them commit any evil with your own eyes?” “We don’t need to see it. It’s obvious. They’re dark-path figures.” “How could this vast Murim contain only one color? And if the Black Serpent Sect were truly a group of villains, the main sect would have taken action long ago.” “But…” “Enough. We’re in a hurry, so we’ll leave the valuables here. Is that all right, Innkeeper?” By now, everyone in the inn knew that these people were martial artists—and that they had made enemies of one of Xi’an’s dark-path factions. The innkeeper, who desperately wanted to avoid entanglement with martial artists, looked as though he had stepped in filth. “G-Great Hero, forgive me, but this is more than an old man like me can handle.” Chulwoo, about to lose the fruits of his hard work, spoke gruffly. “Don’t worry. Nothing will happen.” “Nothing may happen right now, but once you leave, I’ll be in serious trouble.” “Come now, I said that won’t happen. Even after we leave, they won’t be able to touch a hair on your head.” “No, that’s not something you can say so easily…” *Is his brain made of muscle too? He’s damn short-sighted.* The innkeeper couldn’t bring himself to say that aloud and could only suffer in silence. At that moment, the young man smiled calmly. “When they come, just tell them one thing along with this pouch.” “Great Heroes, I don’t think you understand what I’m saying…” The innkeeper’s words were cut short by the young man’s voice. “Tell them that Baek Museong, a first-generation disciple of Huashan, apologizes for his junior disciples’ mistake.” The inn fell silent. The name *Huashan* was intimidating enough, but the young man’s name also sounded familiar, as though they had heard it somewhere before. “Baek Museong of Huashan?” “Baek Museong… Baek Museong… Wait. Could it be?” Xi’an was practically Huashan’s front yard. It didn’t take long for a few martial arts aficionados to realize the young man’s identity. “Baek Museong, Huashan’s Lone Crane!” The title had been given to him because of his lofty bearing, like that of a solitary crane. Renowned as an outstanding prodigy from the moment he entered Huashan, he also held another title. “If he’s Huashan’s Lone Crane, isn’t he the first of the Three Plum Blossom Elites?” The current Sect Leader of Huashan had three disciples, every one of whom had grown into an outstanding master. Naturally, they had been appointed Plum Blossom Swordsmen—the pride of Huashan—and soon distinguished themselves. “I heard one of them was a woman… Then are those two—?” “Why even ask? Didn’t you hear her call Huashan’s Lone Crane her Senior Brother?” “Good heavens. I never thought I’d live to see all of the Three Plum Blossom Elites in a place like this.” Ignoring the exclamations erupting throughout the inn, Baek Museong spoke. “Would it really be impossible?” The innkeeper answered with a solemn expression. “I’ll return this property to the Black Serpent Sect at the risk of my life. At your command!” “…” * * * “Ah, that’s right.” At Baek Museong’s mutter, his two junior disciples turned toward him. “What is it, Senior Brother?” “Did you leave something behind?” Baek Museong shook his head. “I forgot to tell him that Huashan has been sealed off.” “Tell who?” “I don’t know his name. That man is going to drag his aching legs all the way there for nothing.” Eunhyang clicked her tongue sympathetically. “What a shame. He won’t have a chance for the next few months.” “Indeed.” They recalled the incident that had thrown all of Huashan into an uproar several days earlier. While the Sect Leader—in other words, their Master—was asleep, an intruder had entered and left without anyone noticing. The intruder had committed the audacious act of leaving a dagger and a handwritten letter beside the Sect Leader’s head. > “I’m going out to get some air. Don’t slack off just because you’ve become Sect Leader. Train your martial arts when you should be sleeping.” Under ordinary circumstances, they would have immediately cast a dragnet across the entire mountain. But if the intruder’s identity was Sword Saint Mae Jonghak, the matter was different. The Sect Leader had immediately sealed Huashan tight and ordered a search for the Sword Saint’s place of seclusion. The search had continued ever since. “Grandmaster really is something. He’s an amazing person.” “I’d only heard about him. I didn’t know he was this extraordinary either.” “If that messenger pigeon hadn’t arrived, we would have been stuck searching Huashan too.” In the midst of all that, the messenger pigeon that flew in from Shanxi Province had been a light of salvation. After much deliberation, Huashan’s leaders had decided to dispatch the exceptional talents known as the Three Plum Blossom Elites. “But what about that person named Cheongpung? Have you ever met him, Senior Brother?” “Yes. Once, ten years ago.” A disciple whom Sword Saint Mae Jonghak had raised like a son—like a grandson. Baek Museong had been there that day ten years ago as well. The eyes of Huashan’s Lone Crane, Baek Museong, gleamed. “I’m looking forward to it. I wonder how much he’s grown.”

## Korean source

```text
＃150화



을씨년스러워 보일 정도로 넓고 휑한 연무장. 가부좌를 틀고 앉아 있는 한 청년의 이마에 땀방울이 흘러내렸다.

‘어찌했어야 했나.’

눈을 감고 생각에 잠긴다. 그리고 한 사람을 떠올린다.

그의 조잡한 청강검과 발걸음. 무공을 펼치기 시작하면서 사라진 웃음을 기억해 냈다.

비로소 칠흑 같은 어둠 속에서 자줏빛 광염을 두른 한 사람이 튀어나왔다.

‘청풍.’

검신 매종학의 손자, 제자. 뭐라 부르든 상관은 없다.

중요한 것은 나흘 전 그와 무공을 겨뤘고, 패했다는 사실이다.

진무경은 그날부터 연무장과 처소에 틀어박혀 두문불출했다. 허기는 벽곡단으로 채웠고 졸음은 수련으로 쫓았다.

지금 그에게 따뜻한 음식과 꿀 같은 휴식 따위는 필요하지 않았다.

‘졌다. 철저하게.’

불과 삼백여 초. 몸 상태가 정상이 아니었음을 감안해도 너무 쉽게 무너졌다.

자신이 누군가. 고작 약관에 절정의 경지에 올라 중원을 떠들썩하게 만들었던 천재다.

‘진천검, 십봉룡…… 우습군. 겨우 이 정도였나?’

고작 이 정도인 자신에게 붙은 거창한 별호들이 우습고, 허명이라 생각하면서도 은근히 스스로를 높게 여기던 자신의 모습이 허탈했다. 이거야말로 위선자 아닌가.

‘누가 그랬지. 천하는 넓다고.’

구주팔황(九州八荒), 사해오호(四海五湖).

이 광활한 대륙에 얼마나 많은 고수가 숨어 있단 말인가.

진무경은 청풍을 만나고서야 그 말의 진짜 의미를 깨달았다.

‘난 우물 안 개구리였어.’

천무학관(天武學館)은 분명 정파 무림 최고의 교육 기관이지만 천하의 모든 기재가 천무학관의 관도가 되는 것은 아니다.

천하 오대세가의 직계와 구파일방의 적전 제자들은 사문의 비전 절기를 이어받기에도 바쁘니까.

청풍도 그중 한 명이다. 그들은…… 우물 밖에서 태어났고 오래전부터 거기서 살아왔다.

‘기다려라, 청풍. 그리고 다른 놈들도 모두.’

눈이 반개한 순간, 진무경의 신형이 번개처럼 솟구침과 동시에 허리춤에서 빛이 뿜어져 나왔다.

쏴아아악!

검기(劍氣). 사방을 쉼 없이 난도질하는 은빛 검기는 나흘 전보다, 아니 지금까지의 그 어떤 때보다 짙고 선명했다.

청풍과의 비무는 그에게 깨달음과 투지를 주었다. 그저 강해지겠다는 막연했던 목표가 초점을 잡은 것이다.

쉬쉬쉬쉬슁!

그 후로도 진무경의 검은 쉬지 않았다. 지쳐 녹초가 되어 쓰러질 때까지…….



* * *



무림에서는 단전을 기해라고 부른다.

기해(氣海). 기의 바다. 몸 안의 모든 공력이 시작되고 모이는 곳. 누가 만들었는지 참 적절한 단어다.

띠링.



- [운기조식]을 시작합니다.

- [진가심법]의 구결을 따라 공력을 운용하십시오.



어느덧 팔 성에 오른 진가심법이다. 이미 수백, 수천 번도 넘게 반복했던 그 길을 따라 45년의 공력을 흘려보냈다.

‘뜨겁다.’

열화신단을 복용함으로써 얻은 열양지기(熱陽之氣)는 자그마치 반 갑자.

용암처럼 끓어오르는 강대한 기운이 전신의 혈맥을 휩쓸었다. 그 거침없는 기세를 보아하니 사뭇 기대감이 든다.

‘지금이라면 가능할지도…….’

운기조식을 할 때마다 항상 막히는 부분이 있었다. 철문처럼 굳게 잠긴 채 공력의 출입을 허락하지 않는 두 개의 혈도.

그곳을 임독양맥(任督兩脈)이라 부른다는 사실을 알게 된 건 최근의 일이다.

‘임독양맥. 소설에서 많이 봤지.’

무협 소설의 주인공이라면 한 번쯤 거치는 단계 아닌가?

무협 소설에선 임독양맥 뚫는 건 기본이요, 환골탈태는 옵션이다. 물론 난 주인공은커녕 조연도 안 되는 놈이라 번번이 물러나야 했다.

‘그랬었지. 지금까지는.’

고작 15년의 공력으로는 역부족이었다. 에어백도 안 터지는 소형차를 바위에 돌진시키는 꼴이니까.

하지만 이제는 다르다. 반 갑자의 열양지기가 더해진다면 소형차는 군용 전차로 탈바꿈한다.

‘이 정도면 해 볼 만하지.’

아니, 해내야 한다.

더 높은 경지로 나아가기 위해서는 반드시 넘어야 할 산이었다.

나는 기세가 최고조에 달한 공력을 끌어 올려 임맥과 독맥, 두 갈래로 쏘아 보냈다.

쿵!

혈도와 공력의 충돌음이 천둥처럼 들렸다. 동시에 찌르르한 고통이 척추와 아랫배를 울린다.

충돌하는 힘이 강해진 만큼 반발력도 장난이 아니다. 그러나 여기서 포기할 수는 없는 노릇. 나는 이를 악물고 연이어 부딪쳐 갔다.

쿵! 쿵! 쿵!

‘와, 씨. 뭐냐 이거.’

나도 나름대로 몸뚱이 험하게 굴린 놈이다. 칼 맞는 건 예사고 내장까지 망가진 적도 있다.

하지만 이건 고통의 종류가 다르다.

‘허리 아픈 건 그렇다 치고, 거기는 왜 아픈 건데!’

남자에게 목숨만큼이나 중요한 부위가 욱신거린다. 마치 누군가가 힘껏 움켜쥐었다가 놓기를 반복하는 것처럼.

임독양맥만 뚫으면 엄청난 보상을 받을 수 있을 것 같은데, 이것만 견디면 절정 고수가 될 수 있을 것 같은데…… 공력을 부딪쳐 갈수록 눈앞이 노래진다.

“으헉!”

삐빅!



- [운기조식]에 실패했습니다.

- 공력이 흐트러지며 혈도가 미세한 손상을 입었습니다.

- [근맥]이 1 하락합니다.



불알 아픈 것도 서러워 죽겠는데 근맥까지 떨어졌다. 나는 아직도 욱신거리는 그 부위를 붙잡고 침상 위에 엎드렸다.

“억! 어어억!”

벼는 익을수록 고개를 숙이고, 남자는 급소가 아플수록 허리를 숙이는 법.

기도드리는 심정으로 한참을 엎드려 있자 점차 통증이 사그라든다.

“훅, 후욱.”

하마터면 홍진 될 뻔.

땀범벅이 된 채로 침상에 드러누워 있는 그때, 다급한 발소리와 함께 불청객들이 들이닥쳤다.

“조장!”

“은인!”

문을 박차고 뛰어 들어온 혁무진과 청풍이 나를 보고 멈칫했다.

“무슨 일…… 헐.”

“은인, 뭐 하시는 거예요?”

“응? 뭐가?”

되묻고 나서 깨달았다.

내가 지금 어떤 꼴인지를.

“아.”

밀폐된 방. 한겨울임에도 어쩐지 땀으로 흠뻑 젖어 침상 위에 누운 채 손은 그곳을 붙잡고 있는 혈기왕성한 20대 청년.

음. 확실히 오해의 소지가 있군.

나는 침착하게 입을 열었다.

“오해야.”

잠깐의 침묵 끝에 혁무진이 눈웃음을 쳤다.

“압니다. 다 알아요.”

“아니라니까.”

“어허, 왜 이러십니까, 선수들끼리.”

“선수는 무슨 선수야, 이 미친놈아.”

“끝까지 모르는 척하시네. 제가 그리 속 좁은 놈으로 보이십니까?”

“아, 진짜 아니라고!”

“좋으셨어요? 어떻게, 아직 안 끝나셨으면 자리 비켜 드려요?”

“시작도 안 했어!”

“아, 그럼 이제 슬슬 시작하려고 하셨구나. 끝나면 다시 올까요?”

“안 해! 할 생각 없어!”

“괜찮습니다. 부끄러운 거 아니에요. 저도 상태 좋은 날에는 하루 다섯 번도 하는데요, 뭘.”

“그거 진짜냐…… 아니, 근데 이 새끼가.”

혼돈. 파괴. 망가.

시간이 지날수록 오해만 깊어져 가는 대화를 듣던 청풍이 고개를 갸우뚱했다.

“뭐가 오해예요? 뭘 알아요?”

“청 소협, 진짜 몰라요? 조장님이 저러고 계신 이유를?”

“몰라요. 소피가 마려우셔서 그런 건가?”

“허어, 어찌 이럴 수가. 딱 한 번만 알려 드릴 테니 마음에 새기십쇼. 이게 다 피와 살이 되는 거예요. 인생이 달라진다니까요.”

“네!”

“지금 조장님의 손이 어디에 있습니까? 대답해 보세요.”

“아랫도리요.”

“그렇죠. 그럼 아랫도리에는 뭐가 있을까요?”

“속곳이요.”

“속곳! 좋습니다. 거의 다 왔어요. 그럼 속곳에는 뭐가 있을까요?”

“어? 그런데 지금은 아랫도리에 없어요.”

“예?”

“은인의 손이 이쪽으로 오고 있어요.”

“헉.”

쫙! 털썩.

정확히 아래턱을 조준한 귀싸대기다. 편안한 표정으로 스르륵 무너지는 혁무진을 청풍이 받아 들었다.

“아직 다 못 들었는데.”

“……그거 들어서 뭐 하시게?”

“한 번 들으면 피와 살이 되고 인생이 달라진다고 하셨잖아요. 그럼 좋은 거 아니에요?”

“…….”

생각해 보니 아주 틀린 말은 아니네.

이미 기절한 성교육 선생님을 시무룩한 얼굴로 바라보던 청풍이 물었다.

“그런데 아랫도리 붙잡고 뭐 하고 계셨어요?”

“…….”

남들이 들으면 진짜 오해하겠다.



* * *



“……이렇게 된 겁니다.”

팩트로 꽉꽉 채운 설명이 끝나자 어느새 깨어난 혁무진이 불퉁한 표정으로 중얼거렸다.

“그럼 처음부터 그렇다고 말씀을 하시지.”

“후우, 너 진짜 오늘 죽도록 맞아 볼래?”

“아, 그건 사양하겠습니다. 지금도 골이 울려요.”

혁무진이 눈을 찡그리며 고개를 흔들었다.

“그런데 갑자기 임독양맥은 왜 건드리신 겁니까? 조장님이 절정 내가고수도 아니고, 그렇다고 위험을 감수할 만큼 간 큰 분도 아니시잖아요.”

“……그냥 한 번 건드려 봤다.”

“예?”

“됐어. 시끄러우니까 입이나 다물어라.”

나는 눈을 동그랗게 뜬 혁무진을 향해 손을 휘휘 저었다.

나흘 전 진무경과 청풍의 비무를 보고 지금보다 훨씬 강해지고 싶다는 생각이 들었다고 털어놓기에는 너무 낯부끄럽다.

“아무튼, 보기 좋게 실패했다는 것만 알아 둬. 거기가 아파서 제대로 못 하겠더라. 이거 왜 이러는 거야?”

“그거야 저도 모르죠. 의원도 아니고, 또 누구 같은 절정 고수도 아니니까.”

나와 혁무진의 시선이 자연스럽게 옆으로 옮겨 갔다. 앞서 말한 ‘누구 같은 절정 고수’가 눈을 깜빡이더니 입을 열었다.

“음, 할아버지한테 들은 적이 있어요.”

이제는 혁무진도 청풍의 신분을 안다. 우리는 동시에 기대감 어린 탄성을 토해 냈다.

“오오.”

“오오오.”

검성 매종학은 천하에서도 손에 꼽히는 고수. 무공에 관한 한, 그가 한 말이라면 팥으로 메주를 쑨다고 해도 믿을 수 있다.

“뭐라고 하셨는데요?”

“임맥은 자칫하다가는 사내구실 못 하게 되고, 독맥도 마찬가지라고. 그리고 또 뭐라고 하셨더라? 아, 맞다!”

곰곰이 생각에 잠겨 있던 청풍이 이마를 탁 쳤다.

“시간 지나면 알아서 뚫리니까 얌전히 놔두라고 하셨어요. 두 개 다 잘못 건드리면 병신 된다고.”

“……?”

“……?”

저게 뭔 소리야.

나와 혁무진의 시선이 거의 동시에 부딪쳤다.

“원래 임독양맥이 시간 지나면 뚫리는 거였냐?”

“글쎄요, 저도 처음 듣는 말인데.”

“그렇다고 허튼소리일 리는 없잖아. 검성씩이나 되는 양반인데.”

“그렇죠. 혹시 시간이 아주 많이 필요한 것 아닐까요?”

“얼마나 필요한데?”

“저야 모르죠. 저희 아버지가 내일모레 환갑이신데 한번 여쭤볼까요?”

“아, 임독양맥 뚫리셨냐고?”

“네.”

“무인이셔?”

“혁가 포목점 주인이신데요.”

“너는 될 수 있으면 말하지 마라. 듣는 사람 속 터지니까.”

“네.”

이런 놈을 수하라고 데리고 다니는 내가 불쌍하다.

나는 한숨을 푹 내쉬고 청풍에게 말했다.

“좀 더 자세히 설명해 주실 수 있나요? 설마 조부님께서 그것만 딱 말씀하시진 않았을…….”

“딱 그것만 말씀하셨어요.”

“……진짜요? 토씨 한 글자 안 틀리고?”

“저는 은인께 거짓말을 하지 않아요.”

하긴, 청풍은 거짓말 칠 정도로 약은 놈이 아니다.

천성인지, 아니면 성장 환경 때문인지 나쁘게 말하면 멍청해 보일 정도로 솔직하고 해맑다.

청풍이 억울한 표정으로 덧붙였다.

“그리고 저희 할아버지도 거짓말을 하시는 분이 아니세요. 저도 기다리니까 뚫렸는걸요. 임독양맥 전부는 아니고 독맥 하나뿐이지만.”

“검성 어르신께서 거짓말을 하셨다는 게 아니라…… 잠깐만요, 지금 뭐라고요?”

“청 소협. 방금 뭐라 하셨습니까? 임독양맥을 뚫으셨다고요?”

“어, 일단은 독맥 하나만요. 아직 제가 어려서 그런가 봐요.”

나는 더듬더듬 물었다.

“어, 어떻게 뚫으셨는데요?”

“재작년에 그냥 수련하다가 기분이 묘해지고, 꽝!”

“꽝?”

“그렇게 뚫었어요.”

“…….”

“…….”

“신기해서 할아버지께 여쭤봤더니 그게 깨달음이란 거래요. 헤헤.”

안 되겠다. 달라도 너무 달라.

시간이 흐르면 자연히 임독양맥을 타통 할 거라는 검성의 말은 정확했다.

문제는 오직 청풍에게만 적용된다는 것이다.

눈앞에서 해맑게 웃고 있는 이놈은, 애초에 나 같은 놈과는 종(種)이 다른 신인류나 다름없다.

‘천재. 하늘이 내린 재능이다, 이거지.’

청풍도, 진무경도. 애시당초 나와는 타고난 재능이 다르니 답이 없다.

말문이 막혀 한동안 가만히 있자 청풍이 슬금슬금 내 눈치를 살폈다.

“은인, 제가 뭐 잘못한 거예요?”

“아뇨. 잘못한 거 없어요.”

“그래요? 다행이다.”

안도의 한숨을 쉬는 청풍을 보며 바짝 마른 입술을 핥았다.

“그런데 저기…….”

“네?”

“부탁 하나만 해도 될까요?”

“뭐든지 말씀하세요.”

젠장, 이거 막상 말하려니 입이 잘 안 떨어지네.

나는 철판이 두껍다. 뻔뻔하다는 소리도 들어 봤고, 염치없다는 소리도 들어 봤다.

하지만 이 한마디가 왜 이렇게 힘들까.

“은인?”

나는 어렵게, 정말 어렵게 한마디를 내뱉었다.

“제 수련 좀 도와주실 수 있나요?”

“그럼요. 물론이죠.”

“네?”

“도와드릴게요. 수련.”

녀석의 투명한 눈동자를 바라본 순간, 비로소 깨달았다. 내가 왜 망설였는지.

그건 호승심이었다.

이 녀석에게만큼은 도움을 받고 싶지 않다는 호승심.

싫어서가 아니라 오롯이 내 힘으로 꺾고 싶은 상대라서 생기는 감정이었다.

“……너무 쉽게 승낙하시는 것 아니에요?”

“은인한테는 빚을 많이 졌는걸요. 제가 좋은 거 여러 가지 많이 가르쳐 드릴게요. 아, 물론 할아버지한테 주의받은 무공은 빼고!”

가르쳐 준다고?

내 좁쌀 같은 마음 한구석이 불편해진다. 그리고 확실해졌다.

나는 이 녀석을 꺾고 싶다. 동등한 위치에 서고 싶다.

하지만 그러기 위해선…….

“그럼 잘 부탁드릴게요.”

배워야지, 뭐.

나, 생각보다 낯짝 두꺼운 놈이다.
```

## Current accepted English baseline

```markdown
# Chapter 150

The training ground was so wide and empty that it looked bleak. Sweat trickled down the forehead of a young man sitting cross-legged.

*What should I have done?*

He closed his eyes and sank into thought. Then he recalled one person.

He remembered Cheongpung’s crude blue-steel sword and clumsy footwork. He remembered the smile that vanished when the young man began to display his martial arts.

At last, from the pitch-black darkness, a figure wrapped in violet light-flames burst forth.

*Cheongpung.*

Grandson and disciple of the Sword God Mae Jonghak. It made no difference what he called him.

What mattered was the fact that four days ago, he had exchanged martial arts with Cheongpung—and lost.

Jin Mukyung had shut himself away in the training ground and his quarters ever since that day. He staved off hunger with fasting pills and chased away sleep through training.

Warm food and honey-sweet rest were of no use to him now.

*I lost. Completely.*

It had taken barely three hundred exchanges. Even taking into account the fact that his condition had not been normal, he had fallen far too easily.

*Who am I?* He was a genius who had reached the Peak realm at barely twenty and caused the Central Plains to tremble.

*Heaven Shaking Sword. Ten Dragons and Phoenixes… How laughable. Was that all I amounted to?*

The grand titles attached to someone as mediocre as himself seemed laughable, nothing more than empty reputations. And yet the way he had secretly held himself in high regard left him feeling hollow.

*Isn’t that the very definition of hypocrisy?*

*Who was it that said the world was vast?*

The Nine Provinces and Eight Wastes. The Four Seas and Five Lakes.

How many masters were hidden across this enormous continent?

Only after meeting Cheongpung did Jin Mukyung understand the true meaning of those words.

*I was a frog in a well.*

Heaven’s Gate Temple was certainly the greatest educational institution in the orthodox Murim, but not every genius under heaven became a student at Heaven’s Gate Temple.

The direct descendants of the Five Great Families and the direct disciples of the Nine Sects and One Gang were too busy inheriting their sects’ secret ultimate techniques.

Cheongpung was one of them. They had been born outside the well and had lived there for a long time.

*Wait for me, Cheongpung. And all the others, too.*

The moment his eyes opened halfway, Jin Mukyung’s body shot upward like lightning, and light burst from his waist.

Whoosh!

Sword Energy. The silver Sword Energy slashed incessantly in every direction. It was denser and clearer than it had been four days ago—no, than it had ever been before.

His duel with Cheongpung had given him insight and fighting spirit. His vague goal of simply becoming stronger had finally gained focus.

Swish, swish, swish, swish!

Jin Mukyung’s sword did not stop after that, either.

Not until he was exhausted, utterly spent, and collapsed…

* * *

In Murim, the dantian is called the qi sea.

The qi sea. The sea of qi. The place where all the internal energy in the body begins and gathers. Whoever coined the term had chosen very well.

Ding!

> **System**
>
> Qi circulation has begun.
>
> Follow the formula of the Jin Family’s Cultivation Technique to circulate your internal energy.

The Jin Family’s Cultivation Technique had reached the eighth stage. Following the path I had already repeated hundreds, even thousands, of times, I sent forty-five years of internal energy flowing through it.

*Hot.*

The Scorching Yang Qi I had gained by taking the Blazing Flame Divine Pill amounted to half a jiazi.

The powerful energy boiling like lava swept through every blood vessel in my body. Seeing its unstoppable momentum, I began to feel a little hopeful.

*Maybe it’s possible now…*

There was always one part that blocked me whenever I circulated my qi. Two acupoints locked as firmly as iron gates, refusing to let internal energy pass through.

I had only recently learned that they were called the Conception and Governor Vessels.

*The Conception and Governor Vessels. I’ve seen them a lot in novels.*

Wasn’t this a stage every protagonist in a martial arts novel passed through at least once?

In martial arts novels, opening the Conception and Governor Vessels was the bare minimum, while Bone Transformation was optional. Of course, I was neither a protagonist nor even a supporting character, so I had been forced to retreat every time.

*That was then. Until now.*

Fifteen years of internal energy had been insufficient. It was like driving a compact car whose airbags did not even work straight into a boulder.

But things were different now. If half a jiazi of Scorching Yang Qi were added to the mix, the compact car would be transformed into a military tank.

*This should be worth a try.*

No. I had to do it.

It was a mountain I absolutely had to cross if I wanted to advance to a higher realm.

I drew up the internal energy that had reached its peak and shot it down two paths, toward the Conception Vessel and the Governor Vessel.

Boom!

The collision between my internal energy and the acupoints sounded like thunder. At the same time, a sharp pain rang through my spine and lower abdomen.

The stronger the collision became, the more vicious the recoil was. But I could not give up here. I clenched my teeth and kept crashing into them.

Boom! Boom! Boom!

*What the hell is this?*

I had put my body through hell in my own way. Being stabbed was nothing unusual, and I had even suffered damage to my internal organs before.

But this was a completely different kind of pain.

*I can accept my lower back hurting, but why does it hurt there?*

A part of a man as important as his life throbbed painfully. It felt as though someone were squeezing it as hard as they could, releasing it, and then repeating the process.

It felt as though I would receive an incredible reward if I opened the Conception and Governor Vessels. It felt as though I would become a Peak master if I could only endure this…

But the more I slammed my internal energy against them, the more the world before my eyes turned yellow.

“Ugh!”

Beep! Beep!

> **System**
>
> Qi circulation failed.
>
> Your internal energy became disordered, causing slight damage to your acupoints.
>
> **Sinews and Meridians** decreased by 1.

My balls were already aching badly enough to make me miserable, and now my Meridians had dropped, too.

I grabbed the still-throbbing area and collapsed face-first onto the bed.

“Ugh! Uuugh!”

As rice bows its head more deeply the riper it becomes, a man bows at the waist more deeply the more his vital points hurt.

I stayed hunched over for a long while as though praying, and the pain gradually subsided.

“Huff, huff.”

I had almost ended up like Hong Jin.

Just as I sprawled out on the bed, drenched in sweat, hurried footsteps approached, and unwelcome guests burst in.

“Captain!”

“Benefactor!”

Hyuk Mujin and Cheongpung rushed through the door, then stopped short when they saw me.

“What happened… Whoa.”

“Benefactor, what are you doing?”

“Huh? What about it?”

I asked the question, then realized it.

I realized what I looked like right now.

“Oh.”

A twenty-something young man in a sealed room, soaked in sweat despite the middle of winter, lying on a bed with one hand clutching that particular spot.

Hmm. There was definitely room for misunderstanding.

I calmly opened my mouth.

“You’ve got it wrong.”

After a brief silence, Hyuk Mujin smiled with his eyes.

“I know. I know everything.”

“No, you don’t.”

“Oh, come on. Why are you acting like this? We’re both professionals.”

“What do you mean, professionals, you lunatic?”

“You’re still pretending not to know. Do I look like such a narrow-minded man to you?”

“I’m telling you, that’s not what it is!”

“Did you enjoy yourself? If you haven’t finished yet, should I step outside?”

“I haven’t even started!”

“Oh, then you were just about to start. Should I come back when you’re done?”

“I’m not doing it! I have no intention of doing it!”

“It’s all right. There’s nothing to be embarrassed about. I do it five times a day when I’m in good shape.”

“Is that actually true…? No, wait. You little—”

Chaos. Destruction. A complete mess.

As the conversation only grew more suspicious with every passing moment, Cheongpung tilted his head.

“What’s the misunderstanding? What does he know?”

“Young Hero Cheongpung, you really don’t know why the Captain is like that?”

“I don’t. Does he need to pee?”

“What? How can this be? I’ll only explain it once, so remember this well. All of this becomes flesh and blood. I’m telling you, it changes your life.”

“Yes!”

“Where is the Captain’s hand right now? Answer me.”

“On his lower half.”

“That’s right. And what’s on the lower half?”

“Underclothes.”

“Underclothes! Good. You’re almost there. And what’s inside the underclothes?”

“Huh? But right now it isn’t on his lower half.”

“What?”

“Benefactor’s hand is coming this way.”

“Gasp.”

Smack!

Thud.

It was a slap aimed precisely at his lower jaw. Hyuk Mujin crumpled with a peaceful expression, and Cheongpung caught him.

“I haven’t heard the whole thing yet.”

“…What are you going to do with the rest of it?”

“You said that hearing it would make it flesh and blood and change my life. Isn’t that a good thing?”

“…”

Come to think of it, that wasn’t entirely wrong.

Cheongpung looked dejectedly at the sex-education teacher who had already passed out.

“But what were you doing while holding your lower half?”

“…”

If anyone else heard this, they would definitely misunderstand.

* * *

“…And that’s what happened.”

By the time I finished an explanation packed full of facts, Hyuk Mujin had woken up and was muttering with a sullen expression.

“Then you should have said that from the beginning.”

“Whew. Do you really want me to beat you to death today?”

“Ah, I’ll pass. My head is still ringing.”

Hyuk Mujin winced and shook his head.

“But why did you suddenly try to open the Conception and Governor Vessels? You’re not a Peak internal-energy master, and you don’t have the guts to risk something like that.”

“…I just tried it once.”

“What?”

“Forget it. You’re noisy, so shut your mouth.”

I waved my hand at Hyuk Mujin, who had opened his eyes wide.

It was too embarrassing to admit that seeing the duel between Jin Mukyung and Cheongpung four days ago had made me want to become much stronger than I was now.

“Anyway, just know that I failed spectacularly. I couldn’t do it properly because it hurt there. Why is this happening?”

“I wouldn’t know. I’m not a physician, and I’m not some Peak master either.”

Hyuk Mujin and I naturally turned our gazes to the side. The aforementioned “Peak master” blinked and opened his mouth.

“Hmm. I’ve heard something about it from my grandfather.”

Hyuk Mujin knew Cheongpung’s identity now, too. We both let out exclamations full of anticipation.

“Ohhh.”

“Ooooooh.”

The Sword Saint Mae Jonghak was one of the most highly regarded masters under heaven. When it came to martial arts, if he had said it, we could believe him even if he told us that red beans could be made into soybean blocks.

“What did he say?”

“He said that if you mess up the Conception Vessel, you might not be able to perform as a man, and that the same goes for the Governor Vessel. And what else did he say? Oh, right!”

Cheongpung, who had been thinking hard, smacked his forehead.

“He said they would open on their own with time, so I should leave them alone. He said touching either of them incorrectly would turn me into a cripple.”

“…”

“…”

*What the hell is he talking about?*

Hyuk Mujin and I exchanged glances almost simultaneously.

“Do the Conception and Governor Vessels normally open with time?”

“I don’t know. That’s the first I’ve heard of it, too.”

“But it couldn’t be nonsense. He’s the Sword Saint, after all.”

“Right. Perhaps it takes a very long time?”

“How long?”

“How would I know? My father is almost sixty. Should I ask him?”

“Oh, ask him whether his Conception and Governor Vessels have opened?”

“Yes.”

“Is he a martial artist?”

“He owns the Hyuk Family Textile Shop.”

“Try not to talk if you can help it. You’ll drive the listener insane.”

“Yes.”

I pitied myself for taking someone like this around as my subordinate.

I let out a deep sigh and spoke to Cheongpung.

“Could you explain in a little more detail? Surely your grandfather didn’t say only that…”

“He said exactly that.”

“…Really? Word for word?”

“I don’t lie to my Benefactor.”

That was true. Cheongpung was not clever enough to lie.

Whether it was in his nature or the result of his upbringing, he was so honest and guileless that, put unkindly, he looked stupid.

Cheongpung added with an indignant expression,

“And my grandfather isn’t someone who lies, either. I waited, too, and mine opened. Not both of them—just the Governor Vessel.”

“The Sword Saint didn’t lie… Wait. What did you just say?”

“Young Hero Cheongpung, what did you say? You opened the Conception and Governor Vessels?”

“Oh, only the Governor Vessel for now. Maybe it’s because I’m still young.”

I asked haltingly,

“How did you open it?”

“Two years ago, I was training when I suddenly felt strange, and then—bang!”

“Bang?”

“That’s how it opened.”

“…”

“…”

“I thought it was strange, so I asked my grandfather about it. He said it was enlightenment. Hehe.”

This was hopeless. We were far too different.

The Sword Saint had been right that the Conception and Governor Vessels would open naturally with time.

The problem was that it only applied to Cheongpung.

The young man smiling brightly in front of me was practically a new species of humanity, fundamentally different from someone like me.

*Genius. Talent bestowed by heaven. That’s what this is.*

Cheongpung and Jin Mukyung. Their innate talent was different from mine from the very beginning. There was no answer for me.

When I remained silent for a while, Cheongpung cautiously watched my expression.

“Benefactor, did I do something wrong?”

“No. You didn’t do anything wrong.”

“Really? That’s a relief.”

As Cheongpung sighed in relief, I licked my dry lips.

“But, um…”

“Yes?”

“Can I ask you for a favor?”

“Tell me whatever it is.”

Damn it. Why was it so hard to say now that the moment had come?

I had thick skin. I had been called shameless, and I had been called without shame.

But why was this one sentence so difficult?

“Benefactor?”

With great difficulty—truly, great difficulty—I forced out the words.

“Could you help me with my training?”

“Of course. Certainly.”

“What?”

“I’ll help you. With your training.”

As I looked into his clear eyes, I finally understood why I had hesitated.

It was competitive pride.

The competitive pride that made me unwilling to accept help from this young man of all people.

It was not because I disliked him. It was because he was an opponent I wanted to bring down solely through my own strength.

I wanted to stand on equal footing with him.

But to do that…

“Then I’ll be counting on you.”

I had to learn. What else could I do?

Turns out I had a thicker hide than I thought.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 150`.

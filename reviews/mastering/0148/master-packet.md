# Master Edit Task — Chapter 148

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
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 천무학관   | **Heaven's Gate Temple**         |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 정파     | **orthodox faction**                             |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장로     | **Elder**                                    |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 극양                        | **Extreme Yang**      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 평양 | **Pyongyang** | City invoked in Taekyung's communist-atmosphere joke. |
| 천하제일인 | **greatest under heaven** | Superlative martial distinction used in Hong Jin and Jin Wikyung's banter. |
| 고금제일인 | **greatest of all time** | Superlative martial distinction used in Hong Jin's exaggerated praise. |
| 비무행 | **dueling tour** | Cheongpung's planned journey to challenge the Ten Dragons and Phoenixes. |
| 청강검 | **blue-steel sword** | Cheongpung's sword. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 진위경 | 홍진 | political_host_to_deputy_military_commissioner | Comrade Hong | formal-polite and playful | Jin Wikyung adopts Hong Jin's requested casual address, 홍 동지. |
| 홍진 | 진위경 | deputy_military_commissioner_to_lesser_family_head | Lesser Family Head Jin | formal and teasing | Hong Jin addresses Jin Wikyung as 진 소가주님 while flattering and joking with him. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 위팽 | 청풍 | Jin Family retainer to visiting Huashan martial artist | Young Hero Cheongpung | formal-polite and worried | Uses 청 소협 while warning that Cheongpung's refusal of the Sect Leader's order could strain relations between the Jin Family and Huashan. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 140–144

## Plot

At the City Lord’s luncheon, Jin Taekyung humiliates Gong Ilhyuk by exposing his tenuous relationship with Zhongnan Sect Leader Gong Iljung. When Ilhyuk attacks Cheongpung, Cheongpung effortlessly destroys his arm with the Taeeul Miri Palm. Revealing that Mae Jonghak, the Sword Saint, taught him the technique, Cheongpung prompts Li Feng to recognize him as his Martial Uncle. Cheongpung then demonstrates the Zaha Divine Technique, confirming his inheritance of Mae Jonghak’s legacy and further humiliating Zhongnan.

Hong Jin dismisses the Zhongnan delegation and abandons their expected partnership, choosing to pursue the Shaanxi–Shanxi trade route through Huashan instead. Li Feng agrees to contact Huashan and act as intermediary. Gong Ilhyuk leaves vowing revenge.

Hong Jin and Li Feng escort Taekyung and Cheongpung through the Provincial Office to meet ten-year-old Prince Shangshan, Zhu Bao. Zhu Bao recognizes Taekyung as the Sleeping Dragon of Shanxi, requests his autograph, and eagerly questions Cheongpung after learning he is Mae Jonghak’s disciple. Taekyung carves an encouraging signature for Zhu Bao, who plans to display it publicly.

The luncheon attendance condition is fulfilled, with the associated quest reward deferred until the luncheon ends. Hong Jin and Li Feng ask the Jin Family of Taiyuan to support an Escort Bureau expanding from Shaanxi toward the Central Plains, offering half the funding and official assistance. Taekyung agrees only to relay the proposal to Jin Wikyung and suggests using the Seongun Escort Bureau as the base.

## Continuity

- Cheongpung is Mae Jonghak’s twenty-year-old grandson and martial heir, a Peak master raised in seclusion. Li Feng formally recognizes him as his Martial Uncle.
- Mae Jonghak remained hidden at a Huashan residence protected by ten formations. Li Feng saw Cheongpung there as a child and left Huashan after being overwhelmed by his talent, not because of his defeat by Gong Ilhyuk.
- Cheongpung knows the Taeeul Miri Palm, Zaha Divine Technique, and several other Huashan techniques. His Extreme Yang internal energy and martial ability vastly exceed his apparent age.
- Cheongpung’s exact parentage and the meaning of Mae Jonghak’s claim that a crane delivered him remain unresolved.
- Hong Jin is Shanxi’s eunuch Deputy Military Commissioner and has served Prince Shangshan since infancy. Li Feng is the Assistant Military Commissioner and commands the Provincial Office’s soldiers.
- The trade and Escort Bureau project has shifted from Zhongnan to Huashan, with Li Feng serving as Hong Jin’s intermediary. Taekyung has not endorsed the proposal; he will present it to Jin Wikyung.
- Gong Ilhyuk leaves humiliated and vengeful. The names and identities of the other two members of the Three Hands of Zhongnan remain unknown.
- Zhu Bao is an exceptionally skilled ten-year-old swordsman who has trained daily for three years. He admires Taekyung and wants to emulate him.
- Taekyung remains below the Peak realm and cannot use Sword Energy, despite defeating the Peak masters Jopil, Jin Baekyang, and Pung Yang.
- Cheongpung wants royal-guard armor because he admires its black appearance and has agreed to call Li Feng Martial Nephew in exchange for royal-guard equipment.
- The full title of the wuxia novel beginning with “The Reign…” remains unknown. The Emperor’s reported suspicion of his younger brother and the political danger surrounding Zhu Bao also remain unresolved.

## Translation Decisions

- Render **태을미리장** as **Taeeul Miri Palm**, **자하신공** as **Zaha Divine Technique**, **태사부** as **Grandmaster**, and **사숙** as **Martial Uncle**.
- Render **풍운검군** as **Wind-and-Cloud Sword Lord** and **오촌 당숙** as **father’s cousin**.
- Render **근위대** as **royal guard** and **근위대 갑옷 세트** as **Royal Guard Armor Set**.
- Use **His Highness** for formal royal address and **king** when Cheongpung uses the literal term.
- Render **주표** as **Zhu Bao**, Prince Shangshan’s personal name.

### Prior accepted reading-copy tails

#### Chapter 146 tail (verified mastered)

…
He passed the military examination, of course. After that, it was smooth sailing all the way.” “As expected of a Huashan lay disciple.” “I can’t say that had no influence, but that wasn’t the only reason. Becoming a Third-Rank Assistant Military Commissioner in only ten years is extremely difficult.” “Third-Rank means…?” “What’s Third-Rank? Is it something you eat?” I vaguely understood that it was a high position, but that was about it. Seeing that Cheongpung and I had no idea what he was talking about, Hong Jin explained patiently. “It’s a high office. There are only four such positions in each province, and Assistant Military Commissioner Li is among the top three in the military hierarchy.” Hong Jin counted them off on his fingers. “First is the Military Commissioner, the commander in chief. Then me, directly beneath him. And third is Assistant Military Commissioner Li. Of course, His Highness Prince Shangshan stands above us all.” “The Military Commissioner?” “He’ll be retiring soon. He was born the son of a Grand General, accomplished a little, and has a tremendous fondness for bribes.” *A corrupt military official. The kind whose petty corruption had become a way of life.* With the commander in chief being that kind of man, it was easy to understand why security in Shanxi Province had been such a mess lately. “The current Military Commissioner is incompetent. You only need to look at the mounted bandits roaming freely the moment the Mount Heng Sword Sect collapsed.” “If he’s that incompetent, why not just…” I swallowed the rest of the sentence before it left my mouth. *Who was I to meddle in someone else’s workplace? Especially when they were all high-ranking government officials.* Seeing my reaction, Hong Jin kindly added an explanation. “The Military Commissioner is appointed directly by the Emperor. The same goes for dismissing him.” “Oh.” “Well, at least he has no ambitions beyond that. I like bribes too, so I’m hardly in a position to criticize him.” *What kind of person was this?* I’d seen plenty of politicians on television proclaiming their innocence against accusations of accepting bribes, but Hong Jin was the first person I’d met who openly admitted to liking them. “Why? Did I look that upright?” “No. You did look like someone who would enjoy bribes, but…” “But you didn’t expect me to say it so openly?” “Well, yes. Honestly, I’m a little flustered.” “Young Master Jin. Do you know what?” Hong Jin continued with a serious expression. “I don’t have a thing.” “What?” “I’m a eunuch.” “……” *What the hell was I supposed to say to that?* I’d suspected as much, but I hadn’t expected him to drop a bomb like that out of nowhere. Cheongpung, who had been looking out the window, abruptly joined in with a curious expression. “What’s a eunuch?” “……Please, please shut your mouth.” *He’s saying he doesn’t have his thing—his thing!* Every second dragged by. Sweating coldly, I forced myself to speak. “I’m sorry to hear that.” “There’s no need to be sorry. Some people live without one, and some live with one. Right?” “Th—that’s right.” His admirable attitude made me solemn for no reason. Meanwhile, the mountain-dwelling primitive who didn’t know what a eunuch was kept chattering without the slightest hint of tact. “Benefactor, could you please tell me what a eunuch is?” *Even if I die, I’m not telling him. Never.* Even if I explained it, there was a 99.99 percent chance he would say something like, *Wow, I’ve never met anyone without a dick before!* But Hong Jin remained composed. “A eunuch doesn’t have a dick.” “Wow, I’ve never met anyone without—” “Oh, shut up already!” Cheongpung sucked in a startled breath. “B-Benefactor.” “Calm down, Young Master Jin. If he grew up in the mountains, it’s understandable. And besides, it’s not as if I’ve only been living as a eunuch for a day or two.” “Still, that was too harsh.” “Was I in the wrong? I’m truly sorry.” “It’s fine. Chin up. Yours is still attached.” *Decades of experience as a eunuch hadn’t gone anywhere.* Hong Jin waved a hand as if to calm us down, then continued as though nothing important had happened. “I’ve never regretted my decision. When your own family is starving to death, what wouldn’t you do? Am I wrong?” “Of course not.” “I—I would have done the same!” Whatever Hong Jin said now, we had to agree with him. Cheongpung and I could only nod, feeling like condemned criminals. “I’m not an upright man, but I’m not cowardly enough to betray a trust. If I were, I wouldn’t have continued serving His Highness all this time.” Hong Jin gazed out the window with hazy eyes. “Long ago, I served at the late Emperor’s side. He ordered me to assist His Highness Prince Shangshan.” “The late Emperor?” If the previous Emperor had entrusted Hong Jin with such a request, Hong Jin must have held a considerably high position among the palace attendants even back then. Hong Jin nodded and continued. “I came to the frontier in what was practically exile, but… I’m satisfied with things as they are now. Truly, this is enough.” Despite his words, an unmistakable light shone in his eyes. Ambition? Hope? Before I could understand what that light meant, it disappeared, and the coachman’s quiet voice reached my ears. “The Jin Family of Taiyuan is in sight.”

#### Chapter 147 tail (verified mastered)

…
cloth banner displayed enormous letters that read: **The Day the Deputy Military Commissioner Came to the Jin Family of Taiyuan** *This isn’t even Buddha’s Birthday. What the hell is this?* I was too embarrassed to lift my head when Hong Jin climbed down behind me and burst out laughing, clutching his stomach. “Wow. This is even more than I expected.” “Are you and my eldest brother old ball buddies or something? How else did you get such an enthusiastic welcome…?” “Young Master Jin, I don’t have balls.” “Ah—oh. I’m sorry. I’m really sorry.” That was a tremendous blunder. Without a stick, there was no way any fertilized eggs would be left behind. As I writhed under the weight of my guilt, Cheongpung approached and comforted me. “Benefactor, my grandfather used to say that people who don’t know how to read the room have no friends around them. But don’t worry. I’ll be your ball buddy.” “……” *I don’t need one, you bastard.* As I struggled to swallow the curse, Hong Jin spoke. “Young Master Jin, do you know what binds people together? Wealth. They say gold and silver can make even ghosts work for you. Living people should be even easier, don’t you think?” “So?” “I told you I’d give him a present. It’s basically a bribe.” *Money can make even ghosts work for you.* I agreed with that to some extent, but I didn’t like the fact that the person in question was Jin Wikyung. I already thought of him as my older brother deep down. I didn’t appreciate Hong Jin making him out to be some materialistic opportunist who could be bought with a bribe. Perhaps that displeasure showed on my face, because Hong Jin smiled and said, “Was that too harsh? But it’s only natural. Who doesn’t like wealth?” “He’s still my eldest brother. Don’t think you’ve won over the Lesser Family Head of the Jin Family of Taiyuan with a measly few silver nyang.” “Young Master Jin…” Hong Jin’s eyes widened at my low voice. “A few silver nyang? I gave him a thousand.” “A measly… How much?” “A thousand silver nyang. One hundred thousand nyang in iron coins.” By now, I had a rough grasp of Murim prices and currency. The private suite at the Phoenix Inn, which could be considered a luxury hotel, cost fifty silver nyang per night. That was said to be close to twice the annual living expenses of a family of four commoners. *In modern money, that would be tens of millions of won.* A thousand silver nyang was twenty times that. In other words, Hong Jin had casually tossed several hundred million won at them in one go. “That’s… a lot, isn’t it?” “A lot, yes. I put in some effort this time.” “Still, that’s far too much.” “It’s for the sake of our future relationship. And right now, the Jin Family of Taiyuan is probably losing money faster than it’s bringing money in. Winning a war and occupying the enemy’s territory isn’t the end of it.” “Ah, yes.” “The assistance you give at times like this feels much greater. I learned that after giving and receiving so many bribes myself. Ah, of course…” Hong Jin continued with a wink. “I also spent a little extra because I’ve taken quite a liking to you, Young Master Jin. You know how I feel, don’t you?” The moment he finished speaking, I felt a hard foreign object against my butt. The repeated poking sensation jolted me wide awake. *No way. Is this bastard seriously…?* I swear, it was the most spine-chilling moment of my entire life. *Fine. You die, I die. Let’s have another war!* I spun around at lightning speed. What met my eyes was a silver lump about half the size of my palm. What did they call those again? A silver yuanbao? “Here. Pocket money from me.” *Oh, right. He’s a eunuch.* I calmed my pounding heart and answered. “Th-thank you.” “Sure. Go buy some candied hawthorn skewers.[^1]” “Benefactor, could you take me with you when you buy them?” Cheongpung smacked his lips as he joined in. Just then, a familiar voice rang out from behind us. “Heh heh. I’ll tell the cooks separately, so ask for as many as you like. Isn’t that right, Wipeng?” “We’ll build a mountain of candied hawthorn skewers.” “Who is that fellow? Candied hawthorn skewers? He isn’t even a child, so what’s this about?” I didn’t need to look to know who it was. I turned around with a happy smile, only to find a scene that left me speechless. *Flutter. Flutter.* Jin Wikyung was smiling broadly. So was Wipeng. Jin Mukyung’s face was bright red. In the hands of all three men, tiny scraps of cloth fluttered in the wind. I had no idea when they had made them. > **Long live the Great Nation! Long live His Imperial Majesty the Emperor!** > > **His Highness Prince Shangshan, may you become a sage king!** “……” “……” *What had I said to Hong Jin earlier?* *Had I told him not to think he’d won over the Lesser Family Head of the mighty Jin Family of Taiyuan with a measly few silver nyang?* *Fuck, “won him over” my ass.* At this point, he was burned—burned to a crisp. [^1]: Candied hawthorn skewers are a traditional snack made by coating fruit in hardened sugar.

## Korean source

```text
＃148화



십만 냥이라는 거금이 따뜻하게 덥혀 놓은 분위기 속, 진위경과 홍진이 인사를 주고받았다.

“태원진가의 진위경이라 합니다. 말로만 듣던 도지휘동지를 뵙게 되어 기쁘기 한량없습니다.”

“대태원진가의 소가주께서 이리 환대해 주시니 몸 둘 바를 모르겠네요. 앞으로는 편하게 홍 동지라고 불러 주세요.”

“그래도 벼슬하시는 분께 그럴 수야 있습니까.”

“아이, 너무 딱딱하시다. 편하게 부르시라니까.”

“하하, 그럼 그럴까요, 홍 동지?”

갑자기 분위기 공산주의 뭔데.

여기가 평양인지 무림인지 고민하고 있을 때, 통성명을 끝마친 진위경의 시선이 이쪽을 향했다.

“음. 태경이 왔느냐?”

“예.”

평소와는 다른 묵직한 목소리에 눈치껏 공손히 대답했다.

아무래도 외부인이 보는 앞에서 평소처럼 굴었다가는 진위경 개인의 위신은 물론이고 가문 전체가 망신임을 알고 있는 것 같다.

“그래, 전하께 인사는 잘 드렸고?”

인사 정도가 아니라 단독 팬 사인회도 하고 왔지.

홍진이 웃으며 내 어깨를 톡톡 두드렸다.

“전하께서 아주 기뻐하셨어요. 평소에 여기 진 공자를 너무 보고 싶어 하셨거든요.”

“아, 그렇습니까?”

“네. 얼마나 좋아하시던지 도무지 놔줄 생각을 안 하시더라니까요.”

“으허허, 우리 막내…… 아니. 제 아우가 마음에 쏙 드신 모양이군요.”

“그럴 만도 하죠. 얼굴 잘생겼지, 키 크고 몸 좋지. 무공도 강한 데다 성격도 아주 서글서글하니 싫어할 사람이 어디 있겠어요?”

“으흠, 제 입으로 이런 말 하긴 뭐 하지만, 사실 태경이가 대단한 인재이긴 합니다. 본가가 아니라 오대세가 같은 곳에서 태어났으면 천하제일인이 되었어도 이상하지 않아요.”

무게 잡는 것도 잊고 신이 나서 떠들어 대는 진위경의 모습에 홍진이 얼굴을 굳혔다.

“천하제일이요? 진 소가주님. 농담이 너무 심하시다.”

“네? 그게 무슨.”

“진 공자가 천하제일인이 될 재목이라니요. 아무리 제가 무림과 연이 없다고 해도 그렇지, 너무 우습게 보시는 거 아녜요?”

“……커흠.”

순간 싸해진 분위기 속에 진위경이 불편한 헛기침을 내뱉었다. 그때 홍진이 재깍 말을 이었다.

“진 공자 정도라면 고금제일인도 될 수 있죠.”

“……!”

“미리 축하드려요, 소가주님. 태원진가에서 고금제일인이 나오다니, 산서성의 홍복이네요.”

진위경이 감격에 찬 얼굴로 외쳤다.

“홍 동지!”

“진 소가주님!”

“…….”

황궁에서 20년을 살았다더니, 과연 혓바닥 놀리는 솜씨가 보통이 아니다.

나는 영혼의 단짝을 만나기라도 한 것처럼 기뻐하는 진위경을 보며 혀를 내둘렀다.

“안 되겠습니다. 여기서 이럴 게 아니라 제가 자리를 마련해 뒀으니 술이라도 한잔…….”

“어쩌죠? 제가 술은 잘 못 먹어서.”

“아, 이리 안타까울 수가.”

“없어서 못 먹어요.”

“홍 동지!”

“진 소가주님!”

“…….”

“…….”

쿵짝 잘 맞는 거 봐라.

두 사람이 껄껄 웃으며 어깨동무를 하고 사라지자 위팽이 황당하다는 얼굴로 나를 바라봤다.

“저자가 정말 도지휘동지가 맞습니까?”

“안타깝지만 사실이에요.”

“내관 출신이라고는 들었지만 저렇게 경박스러울 줄은.”

글쎄, 그럼 거기에 맞장구까지 다 쳐 준 무인 출신인 진위경은 뭐가 되나.

아까부터 썩은 표정이던 진무경이 입을 열었다.

“원래 저런 작자입니다. 지난번에는 은근슬쩍 제 어깨를 쓰다듬더군요. 팔을 부러트리려다가 간신히 참았습니다.”

손에 들고 있던 천을 쫙쫙 찢어 땅바닥에 내팽개친 그가 한결 후련해진 표정으로 말했다.

“그럼 전 중요한 볼일이 있어서 이만.”

“볼일은 무슨. 또 수련이겠지 뭐.”

“무인에게 있어 수련보다 중요한 일이 있나?”

“……없지.”

할 말 없게 만드는군.

말문이 막혀 입맛만 다시던 그때, 또랑또랑하고 맑은 목소리가 울려 퍼졌다.

“우와, 저희 할아버지가 항상 하시는 말씀이랑 똑같아요.”

순간 위팽과 진무경의 시선이 청풍을 송곳처럼 찔렀다.

양민들이 볼 때야 조금 독특한 분위기의 청년, 딱 그 정도지만 고수들에겐 다르다.

두 사람의 눈썹이 위로 솟구치자 청풍이 당황한 얼굴로 나를 돌아봤다.

“어, 은인. 제가 무슨 잘못이라도 했나요?”

“잘못은 무슨. 그냥 신기해서 그런 거예요. 그렇죠, 두 분?”

두 사람은 청풍에게 시선을 고정시킨 채 고개만 끄덕였다.

새파랗게 젊은 절정 고수. 그들로서는 난데없이 튀어나온 청풍의 정체가 궁금할 법도 했다.

“이참에 서로 통성명이라도 하시죠. 이쪽은 청풍.”

내 말이 끝나기가 무섭게 청풍이 고개를 꾸벅 숙였다.

“안녕하세요, 청풍입니다! 산서에 온 지는 며칠밖에 안 됐고요. 그전에는 하남에 있었고 또…….”

이거 어디서 굴러먹다 온 놈이야? 두 사람의 얼굴엔 딱 저렇게 쓰여 있다.

예상했던 바다. 나는 청풍의 정체를 간단명료하게 설명했다.

“검성의 제잡니다.”

“……!”

“……!”

검성 매종학의 이름은 무림인들에게 있어 확실히 치트키나 다름없다.

두 사람이 경악에 찬 얼굴로 입을 딱 벌리고 말을 잇지 못하자 청풍이 조심스럽게 물었다.

“저어, 그런데 두 분 중 누가 진천검이시죠?”

아직 충격에서 빠져나오지 못한 진무경이 더듬더듬 대답했다.

“내, 내가 진천검이오. 한데 정말 검성 매종학 대협의……?”

“네. 저희 할아버지세요.”

“헉!”

화염신장의 비급을 봤을 때보다 몇 배는 놀란 표정이다.

이미 수십 년 전 은거한 것으로 알려진 초절정 고수의 제자, 그것도 손자라고 하는 젊은이가 툭 튀어나왔으니 그럴 만도 했다.

“이럴 수가…….”

“검성의 후인이라니.”

놀라움을 금치 못하는 두 사람을 번갈아 보던 청풍이 해맑게 웃었다.

“저도 하산하기 전까지는 몰랐네요.”

“소, 소협. 혹시 매 대협께서도 하산을……?”

물어보는 목소리에는 기대와 흥분이 한껏 담겨 있었다.

두 사람 모두 일평생 검을 수련해 온 검객. 매종학은 검성이라는 별호를 얻을 정도로 검도(劍道)의 경지를 이룩한 사람이니 그들에게 있어 신이나 다름없는 존재였다.

그러나 청풍은 대답은 두 사람의 기대를 산산조각 냈다.

“아뇨, 저만 몰래 도망쳐 나왔어요. 만나고 싶은 분들이 있어서.”

“아아.”

“그럴 수가…….”

“근데 그건 그렇고…….”

안타까워하는 두 사람을 바라보던 청풍이 재차 입을 열었다.

그의 반짝거리는 눈빛은 아까 전부터 진무경에게 고정되어 있었다.

“정말 진천검 진무경 소협이신가요? 십봉룡(十鳳龍)의 그분?”

“맞소, 내가 진무경이오.”

“와, 드디어 찾았다!”

“……음?”

“제가 그쪽을 엄청 찾아 헤맸거든요. 하남의 천무학관에서부터 여기까지.”

뭐야, 저 녀석이 찾고 있던 사람이 진무경이었어?

위팽은 물론이고 당사자인 진무경도 어리둥절한 표정으로 물었다.

“날 말이오?”

“네. 마침 가깝기도 하고, 첫 번째 시작으로 나쁘지 않겠다 싶어서요.”

“첫 번째라니. 그게 무슨 말이오?”

“비무행(比武行).”

청풍이 잔잔하게 웃었다. 그건 지금까지 보아 왔던 해맑고 순수한 웃음과는 전혀 다른 종류의 것이었다.

“하산하면서 결심했지요. 십봉룡을 모두 꺾기 전에는 돌아가지 않겠다고.”

“……!”

“할아버지께서 그러셨어요. 무인에게는 대화가 필요 없다. 오직 무(武)로 겨룰 뿐이다.”

스으으.

그 순간, 나는 뜨거운 열기를 느꼈다. 어느새 솟구친 자줏빛 광염(光焰)이 청풍의 전신에서 피어오르고 있었다.

이미 한 번 본 적 있는 광경이다.

‘자하신공.’

극양의 기운이 냉기를 불살랐다. 땅이 녹고 흙이 그을렸다. 청풍이 웃음이 사라진 얼굴로 입을 열었다.

“자리를 옮길까요?”

“그럴 필요 있나?”

진무경의 말이 이어졌다.

“검을 뽑아.”



* * *



진무경은 길게 숨을 내뱉었다. 빠르게 뛰던 심장이 천천히 속도를 늦춘다. 전투에서 중요한 것은 호흡이다. 이제야 비로소 검을 뽑을 준비를 갖췄다.

그는 검파에 손을 올리며 한 사람의 이름을 떠올렸다.

‘검성 매종학.’

검을 처음 쥔 날부터 단 하루도 그 이름을 잊은 적이 없었다.

검의 궁극에 다다랐다는, 혹은 그 너머의 경지에 이르렀다는 전설적인 검객.

모두가 검성을 추앙했지만 진무경은 달랐다.

‘언젠가 그를 꺾고 말겠다.’

누군가 들었다면 코웃음을 쳤을 일이다. 미친놈이라며 손가락질했을 것이다.

진무경이 제아무리 천재라 한들 검성이라는 이름에는 닿을 수 없다. 매종학이 검성이라 불리기 시작한 이래, 그 누구도 그를 넘어서지 못했으니까.

검성 매종학은 이미 수십 년 전 정파 무림의 새로운 역사를 썼고, 신화의 주인공이 되었다.

‘상관없어. 이건 내 목표니까.’

만용이 아니라 목표다.

지금껏 검을 수련하며 매일같이 뼈와 가슴에 새겨 온 목표.

그리고 이 순간, 검성 매종학의 모든 것을 물려받은 한 사람이 눈앞에 있다.

“할아버지께서 그러셨죠. 너는 십봉룡에 비하면 아무것도 아니다. 자만하지 말아라.”

청풍이 천천히 발을 내디뎠다. 허리춤에는 아무렇게나 매인 청강검 한 자루가 대롱거렸고, 발걸음은 산책이라도 나온 것처럼 가벼웠다.

그러나…….

‘빈틈이 없다.’

허술하기 짝이 없는데 도무지 언제, 어떻게 상대를 공격해야 할지 모르겠다.

진무경은 바짝 마른 입술을 핥았다.

“난 그분을 만나 본 적도 없는데…… 과찬을 하셨군.”

“아니에요. 솔직히 살짝 놀랐는걸요. 이건 진심이에요.”

진무경 역시 지금 청풍이 하는 말들이 모두 진심이라는 사실을 안다. 그래서 더 기분이 묘했다.

‘살짝, 이라고.’

검을 수련한 지 어느덧 이십여 년이 지났다. 재능과 노력을 바탕으로 이 자리에 올랐다.

세인들은 자신을 천재라고 불렀고, 진천검이라는 별호를 붙여 주었으며 십봉룡이라 칭했다.

단 한 번도 그런 허명(虛名)에 취한 적이 없다고 생각했는데…….

‘나도 아직 한참 멀었군.’

어느새 자신을 우러러보는 사람들의 시선에 익숙해져 있었던 모양이다.

얼마 전 풍양에게 당한 상처가 다시 욱신거리는 듯했다.

“그거 아시오?”

“뭘요?”

“당신이 강하다는 것.”

“사실 얼마 전까지 확신하지 못했어요. 하지만 이제는 알겠네요.”

“나를 만나서?”

“네. 진 소협을 만나서. 십봉룡이 어느 정도인지 알게 됐으니까요.”

“그렇소?”

진무경이 피식 웃었다.

재미있는 놈이다. 이미 구파일방의 장로에 버금가는 무공, 혹은 그 이상이면서도 때 묻지 않은 순수함. 솔직함.

무인이지만 무림에는 어울리지 않는 놈이다.

‘내가 아는 누구랑은 정반대로군.’

문득 한 사람이 떠오른다.

무림 어디에 던져 놔도 어떻게든 살아남을 것 같은 놈, 동시에 가장 무인답지 않게 싸우는 놈이.

“나이가 어떻게 되시오?”

“올해로 약관입니다.”

“마침 나이도 같군. 우연인가? 아니면 인연?”

“네?”

진무경은 대답 대신에 고개를 저었다.

사실 이 비무의 결과는 이미 알고 있다. 청풍의 전신에서 넘실거리는 자하신공의 기운이 그만큼 압도적이었으니까.

이 정도의 고수를 상대로 모든 기량을 펼치지 못하는 것이 아쉬울 뿐이다.

‘이럴 때 저 녀석이라면 어떻게 했을까?’

진무경은 자신의 사고뭉치 동생을 흘끗 바라봤다. 놈은 악동 같은 웃음과 함께 입을 벙긋거리고 있었다.

넌. 좆. 됐. 다.

이런 쳐 죽일 놈을 봤나. 허탈하게 웃은 진무경이 검파에 손을 올렸다. 단전에서 끓어오른 공력이 사지백해로 뻗어 나간다.

청풍이 진무경의 검을 바라보며 입을 열었다.

“할아버지께서 그런 말씀도 해 주셨어요. 비무에는 기수식 따위 필요 없다.”

“동감이오.”

다음 순간.

거대한 굉음과 함께 자줏빛 광염과 은빛 검기가 격돌했다.
```

## Current accepted English baseline

```markdown
# Chapter 148

In the atmosphere warmed by the enormous sum of a hundred thousand nyang, Jin Wikyung and Hong Jin exchanged greetings.

“I am Jin Wikyung of the Jin Family of Taiyuan. It is an immense pleasure to meet the Deputy Military Commissioner I’ve heard so much about.”

“Being so warmly welcomed by the Lesser Family Head of the great Jin Family of Taiyuan leaves me at a loss. From now on, please just call me Comrade Hong.”

“Even so, how could I address an official that casually?”

“Come now, you’re being too stiff. I said to call me casually.”

“Ha-ha. Then shall I, Comrade Hong?”

What was with the sudden communist atmosphere?

As I wondered whether I was in Pyongyang or the Murim, Jin Wikyung finished exchanging introductions and turned his gaze toward me.

“Hmm. Taekyung, you’re here?”

“Yes.”

His voice was heavier than usual, so I answered politely and read the room.

Apparently, he understood that acting as he normally did in front of outsiders would not only damage his personal dignity but also humiliate the entire family.

“So, did you greet His Highness properly?”

*Properly? I didn’t just greet him. I even held a private autograph session.*

Hong Jin smiled and patted my shoulder.

“His Highness was delighted. He’d always wanted to meet Young Master Jin here.”

“Oh, is that so?”

“Yes. He was so happy that he had no intention of letting him go.”

“Uhehehe. It seems our youngest—no. It seems His Highness has taken quite a liking to my younger brother.”

“I can see why. He’s handsome, tall, and well-built. He’s strong in martial arts, and he has such an easygoing personality. Who could dislike him?”

“Ehem. It feels strange to say this myself, but Taekyung really is an extraordinary talent. If he had been born somewhere like the Five Great Families instead of our family, it wouldn’t be strange if he became the greatest under heaven.”

Hong Jin’s expression hardened as Jin Wikyung got carried away, chattering excitedly and forgetting all about maintaining his dignity.

“The greatest under heaven? Lesser Family Head Jin, that’s too much of a joke.”

“Pardon? What do you mean?”

“You’re saying Young Master Jin has what it takes to become the greatest under heaven? Even if I have no connection to the Murim, surely you aren’t making light of me.”

“……Ahem.”

As the atmosphere instantly turned cold, Jin Wikyung gave an uncomfortable cough. Hong Jin immediately continued.

“Someone like Young Master Jin could become the greatest of all time.”

“……!”

“Allow me to congratulate you in advance, Lesser Family Head. For the greatest of all time to come from the Jin Family of Taiyuan—what a blessing for Shanxi Province.”

Jin Wikyung cried out with a deeply moved expression.

“Comrade Hong!”

“Lesser Family Head Jin!”

“……”

They say Hong Jin lived in the imperial palace for twenty years. His skill with his tongue certainly wasn’t ordinary.

I clicked my tongue as I watched Jin Wikyung rejoice as though he had found his soulmate.

“This won’t do. There’s no point staying here. I’ve already arranged a place, so why don’t we have a drink?”

“What should I do? I’m not very good with alcohol.”

“Ah, what a shame.”

“The only time I can’t drink is when there’s none to be had.”

“Comrade Hong!”

“Lesser Family Head Jin!”

“……”

“……”

Look at how perfectly they clicked together.

When the two men disappeared, laughing loudly with their arms around each other’s shoulders, Wipeng stared at me with an utterly dumbfounded expression.

“Is that man really the Deputy Military Commissioner?”

“Unfortunately, yes.”

“I heard he was a former palace attendant, but I didn’t know he’d be so frivolous.”

Well, then what did that make Jin Wikyung, a martial artist who had played along with every bit of it?

Jin Mukyung, who had been wearing a sour expression for some time, finally spoke.

“That’s just the kind of man he is. Last time, he subtly stroked my shoulder. I barely stopped myself from breaking his arm.”

He ripped the cloth in his hands into strips and threw them onto the ground, then spoke with a much more relieved expression.

“Then I have important business, so I’ll be leaving.”

“What business? Training again, I assume.”

“Is there anything more important to a martial artist than training?”

“……No.”

That left me with nothing to say.

As I stood there at a loss, merely smacking my lips, a clear, ringing voice rang out.

“Wow, that’s exactly what my grandfather always says.”

Wipeng and Jin Mukyung’s gazes pierced Cheongpung like awls.

To ordinary people, Cheongpung was merely a young man with a slightly unusual air about him. To masters, however, he was something else entirely.

When both men’s eyebrows shot upward, Cheongpung turned to me with a flustered expression.

“Uh, Benefactor. Did I do something wrong?”

“What do you mean, wrong? They just found it interesting. Right, gentlemen?”

Neither man took his eyes off Cheongpung. They merely nodded.

An extraordinarily young Peak master. It was only natural that they would be curious about the identity of this Cheongpung who had suddenly appeared out of nowhere.

“Since we’re here, why don’t you introduce yourselves? This is Cheongpung.”

Before I had even finished speaking, Cheongpung gave a deep bow.

“Hello, I’m Cheongpung! I’ve only been in Shanxi for a few days. Before that, I was in Henan, and before that…”

*Where did this guy crawl out of?*

The question was written plainly across both men’s faces.

Just as I expected. I explained Cheongpung’s identity simply and clearly.

“He’s the Sword Saint’s disciple.”

“……!”

“……!”

The name of Sword Saint Mae Jonghak was practically an instant cheat code among martial artists.

When the two men stared at Cheongpung in shock, mouths hanging open and unable to speak, he asked cautiously,

“Um, which of you is the Heaven Shaking Sword?”

Jin Mukyung, who still hadn’t recovered from the shock, stammered out a reply.

“I-I’m the Heaven Shaking Sword. But are you really the Sword Saint Mae Jonghak’s…?”

“Yes. He’s my grandfather.”

“Gasp!”

He looked several times more shocked than when he had seen the Flame Divine Palm martial arts manual.

A young man claiming to be the disciple—and grandson—of a Supreme Peak master who was known to have gone into seclusion decades ago had suddenly appeared before them. Their reaction was understandable.

“This can’t be…”

“He’s the Sword Saint’s successor…”

Cheongpung looked back and forth between the two astonished men, then smiled brightly.

“I didn’t know either until I came down the mountain.”

“Y-Young Hero. Did Great Hero Mae also descend the mountain…?”

His voice was filled with expectation and excitement.

Both men had trained in swordsmanship their entire lives. To them, Mae Jonghak was practically a god—a man who had reached such a level in the Way of the Sword that he had earned the martial title of Sword Saint.

But Cheongpung’s answer shattered their expectations.

“No. I just snuck out by myself. There were people I wanted to meet.”

“Ah…”

“How unfortunate…”

“But putting that aside…”

Cheongpung looked at the two crestfallen men before speaking again.

His bright eyes had been fixed on Jin Mukyung for some time.

“Are you really Young Hero Jin Mukyung, the one from the Ten Dragons and Phoenixes?”

“That’s right. I’m Jin Mukyung.”

“Wow, I finally found you!”

“……Hmm?”

“I searched everywhere for you. From Heaven’s Gate Temple in Henan all the way here.”

*What? The person that guy had been looking for was Jin Mukyung?*

Wipeng, as well as Jin Mukyung himself, asked with bewildered expressions,

“You were looking for me?”

“Yes. Since you were nearby, I thought you’d be a decent place to start.”

“A first? What does that mean?”

“A dueling tour.”

Cheongpung smiled softly. It was completely different from the bright, innocent smile I had seen from him until now.

“I decided it while coming down the mountain. I won’t return until I’ve defeated all the Ten Dragons and Phoenixes.”

“……!”

“My grandfather told me this: A martial artist has no need for conversation. We settle things through martial arts alone.”

Sssss.

At that moment, I felt a wave of heat. Violet light-flames had risen around Cheongpung’s entire body, surging upward.

I had already seen this once before.

*The Zaha Divine Technique.*

The Extreme Yang qi burned the cold away. The earth melted, and the soil scorched. Cheongpung opened his mouth with all traces of his smile gone.

“Shall we move somewhere else?”

“Is there any need?”

Jin Mukyung continued,

“Draw your sword.”

* * *

Jin Mukyung let out a long breath. His rapidly beating heart slowly began to settle. Breathing was important in battle. Only now was he finally ready to draw his sword.

As he placed a hand on the hilt, he thought of one man’s name.

*Sword Saint Mae Jonghak.*

Not once had he forgotten that name since the day he first held a sword.

A legendary swordsman who was said to have reached the ultimate realm of the sword—or perhaps a realm beyond it.

Everyone revered the Sword Saint, but Jin Mukyung was different.

*Someday, I’ll defeat him.*

If anyone had heard him say that, they would have snorted. They would have pointed at him and called him crazy.

No matter how talented Jin Mukyung was, he could never touch the Sword Saint’s level. Ever since Mae Jonghak had begun to be called the Sword Saint, no one had surpassed him.

Sword Saint Mae Jonghak had written a new chapter in the history of the orthodox Murim decades ago and become the protagonist of a legend.

*It doesn’t matter. This is my goal.*

It wasn’t reckless arrogance. It was a goal.

A goal he had etched into his bones and heart every day as he trained with his sword.

And at this very moment, someone who had inherited everything from Sword Saint Mae Jonghak stood before him.

“My grandfather used to tell me this. ‘Compared to the Ten Dragons and Phoenixes, you are nothing. Don’t become arrogant.’”

Cheongpung slowly stepped forward. A single blue-steel sword dangled from his waist, tied on haphazardly, and his footsteps were as light as though he had come out for a stroll.

But…

*There are no openings.*

He looked utterly careless, yet Jin Mukyung couldn’t figure out when or how he was supposed to attack him.

Jin Mukyung licked his parched lips.

“I’ve never even met him… He praised me too highly.”

“No, honestly, you surprised me a little. I mean that.”

Jin Mukyung knew that everything Cheongpung was saying was sincere. That only made it feel stranger.

*Just a little?*

More than twenty years had passed since he began training with the sword. He had reached this point through talent and effort.

People had called him a genius, given him the martial title Heaven Shaking Sword, and counted him among the Ten Dragons and Phoenixes.

He had believed that he had never once been intoxicated by such hollow fame, but…

*I still have a long way to go.*

At some point, he must have grown accustomed to the gazes of people who looked up to him.

The wound Pung Yang had inflicted on him not long ago seemed to throb again.

“Do you know something?”

“What?”

“That you’re strong.”

“Until recently, I wasn’t certain. But now I know.”

“Because you met me?”

“Yes. Because I met Young Hero Jin. Now I know what the Ten Dragons and Phoenixes are capable of.”

“Is that so?”

Jin Mukyung let out a quiet laugh.

What an interesting guy. He possessed martial arts that rivaled—or even surpassed—those of an Elder of the Nine Sects and One Gang, yet he remained untainted by the world. He was pure. Honest.

He was a martial artist, but he didn’t fit in the Murim.

*He’s the exact opposite of someone I know.*

One person suddenly came to mind.

A guy who seemed like he could somehow survive no matter where he was thrown in the Murim, and who fought in the least martial-artist-like way imaginable.

“How old are you?”

“I’m twenty this year.”

“We’re the same age. Is it coincidence? Or fate?”

“What?”

Jin Mukyung shook his head instead of answering.

In truth, he already knew the outcome of this duel. The qi of the Zaha Divine Technique surging through Cheongpung’s entire body was that overwhelming.

It was merely regrettable that he couldn’t display all his abilities against an opponent of this caliber.

*How would that troublemaker handle a situation like this?*

Jin Mukyung glanced at his troublesome younger brother. With a grin like a little devil’s, Taekyung was mouthing something.

*You. Are. Fucked.*

*What a goddamn bastard.*

Laughing hollowly, Jin Mukyung placed a hand on his sword hilt. The internal energy boiling up from his dantian coursed through every part of his body.

Cheongpung looked at Jin Mukyung’s sword and spoke.

“My grandfather told me something else, too. A duel doesn’t need an opening stance or anything like that.”

“I agree.”

The next moment—

With a tremendous boom, violet light-flames and silver Sword Energy collided.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 148`.

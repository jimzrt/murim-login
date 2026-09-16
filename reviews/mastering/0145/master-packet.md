# Master Edit Task — Chapter 145

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
| 청풍     | **Cheongpung**     |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 산서오문   | **Five Gates of Shanxi**         |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 표국     | **Escort Bureau**                            |
| 소국주    | **Young Bureau Head**                        |
| 제자     | **Disciple**                                 |
| 사숙     | **Martial Uncle**                            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 고평문 | **Gopyeong Sect** | Minor sect whose young sect leader is pressured by Taekyung. |
| 고평지부 | **Gopyeong Branch** | Proposed branch designation under the Jin Family of Taiyuan. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 이풍 | 청풍 | Huashan lay disciple to martial uncle | Young Hero; Martial Uncle Cheongpung | formal and reverent | Li Feng initially addresses Cheongpung as 소협 while testing his knowledge, then recognizes him as 사숙 after witnessing his Huashan sword technique. |
| 청풍 | 이풍 | Martial Uncle to Martial Nephew | Martial Nephew Li Feng | exuberant and deferential | Cheongpung adopts the address to obtain royal-guard armor and weapons. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 이풍 | 주표 | official_to_prince | Your Highness | formal-deferential | Suggests that Zhu Bao visit the Jin Family's grand banquet in fifteen days. |
| 주표 | 청풍 | prince_to_young_martial_artist | you | formal and gatekeeping | Refuses Cheongpung's autograph until he acquires a martial title. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 진위경 | 홍진 | political_host_to_deputy_military_commissioner | Comrade Hong | formal-polite and playful | Jin Wikyung adopts Hong Jin's requested casual address, 홍 동지. |
| 홍진 | 진위경 | deputy_military_commissioner_to_lesser_family_head | Lesser Family Head Jin | formal and teasing | Hong Jin addresses Jin Wikyung as 진 소가주님 while flattering and joking with him. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |

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

#### Chapter 143 tail (verified mastered)

…
over. Merchandise wasn’t complete without the full set. On the verge of obtaining the Royal Guard Armor Set, Cheongpung spread his arms, his face glowing with joy. “Martial Nephew Li Feng!” Li Feng answered awkwardly. “M-Martial Uncle Cheongpung.” “I like Martial Nephew Li Feng best in the whole world!” “……Thank you, Martial Uncle.” I felt sorry for the Sword Saint, who had spent twenty years raising that bastard as his grandson. While even the royal guards were distracted by this unexpected farce, Hong Jin let out a deep sigh. “What are you doing? Why haven’t you opened the gate?” * * * The young prince barely came up to my chest, if that. Prince Shangshan, Zhu Bao,[^1] was much smaller than I had expected—and much stronger. *Ssshhk, ssshhk, ssshhk!* That was not a sound a mere ten-year-old child should have been able to make with a sword. His sword paths were sharp, and his footwork technique carried him busily across the training ground. Even I, who wasn’t particularly well versed in sword techniques, could tell that his skill was more than enough to make me nod in approval. *So there was a reason he invited us.* When I first received Prince Shangshan’s invitation, I’d had only one thought. *I’ll go tell him a few heroic tales he wants to hear.* That was about it. But this child was different. Instead of telling him stories about my exploits, I might have to teach him about martial arts. “What do you think of His Highness?” Hong Jin asked after dismissing all the attendants waiting outside the training ground with a single gesture. Even then, the young prince was so absorbed in his martial arts that he didn’t notice who had arrived or who had left. “Exactly what sort of impression are you asking for?” “Well, for starters, his martial arts?” I answered honestly. “He’s better than I expected. No, he’s outstanding. When did he begin learning?” “He began showing an interest in martial arts three years ago.” “Three years…” “Yes. Ever since the day he first held a sword, he hasn’t missed a single day of martial arts training unless something unusual happened.” Li Feng smiled proudly and added, “He is unlike an ordinary child in many ways. His determination is remarkable. Much like yours, Young Hero Jin.” “Mine?” “That’s right. I heard Young Hero Jin worked himself to the bone from a young age. You’ve been making quite a name for yourself, just as one would expect from a master the Jin Family of Taiyuan secretly raised with such painstaking care.” “Uh… yes, I suppose.” That was a bogus rumor the Jin Family of Taiyuan had spread for public consumption. In reality, I couldn’t even remember what I’d been doing at the age of ten. *Probably going to elementary school or something.* Li Feng continued. “You have no idea how delighted His Highness was when he heard the story of the Sleeping Dragon of Shanxi. He must have been eagerly awaiting the chance to meet Young Hero Jin today.” “……For someone who was looking forward to it, hasn’t he kept us waiting rather a long time?” It felt like we’d been waiting for almost an hour. Was it because he was a prince? The little brat already had no basic manners. Li Feng smiled faintly at my timid complaint. “His Highness has a habit of immersing himself in martial arts whenever he is nervous. If he has offended you, please accept my apologies.” There was no need to apologize over something like that. Just as I waved my hands dismissively, Hong Jin cupped both hands around his mouth and shouted, “Your Hiiiighness—!” The small figure practicing his sword technique stopped dead at the shrill call. A moment later, he noticed us and crooked a finger. “What is that supposed to be?” “What do you think? His Highness is calling us.” “What are we, neighborhood mutts?” “Wow, I’ve never been a neighborhood mutt before!” “……Please shut your mouth. No one here has ever been a neighborhood mutt.” Suppressing my frustration, I walked toward the training ground. Prince Shangshan Zhu Bao. With every step, his face drew closer. *The rude ones always seem to be handsome.* Even at such a young age, his already fully formed features were sharp and distinct. His black eyes stared directly at me. When I reached him, a voice that was still unmistakably childish drifted out. “Do you know who I am?” I had at least learned the basics of etiquette by now. I lowered myself onto one knee so that our eyes were level. “Yes. His Highness, Prince Shangshan.” “I do not yet know your name.” “My name is Jin Taekyung of the Jin Family of Taiyuan.” A faint trace of surprise appeared in his previously dignified eyes. “T-The Sleeping Dragon of Shanxi, Jin Taekyung?” “That’s right.” I wondered how he would react. The young prince remained silent for a long moment. Then he suddenly pulled something from his robes. A wooden tablet about the size of an adult’s palm and a dagger. “This…” “……?” He had handed them to me, so I accepted them. But what was I supposed to do with them? As I stood there in bewilderment, Zhu Bao delivered a single dignified word. “I would like your signature.” “……” *Oh. He wants an autograph?* [^1]: Zhu Bao (朱豹) is Prince Shangshan’s personal name.

#### Chapter 144 tail (verified mastered)

…
Beside Li Feng, of course. I’ll say it again: my ass is precious. “Let’s hear what this is about. I’m not very knowledgeable in this area, so I may not be much help.” Hong Jin had been pouting in feigned disappointment. Now he spoke. “It doesn’t matter if Young Hero Jin doesn’t make a decision here. You only need to pass the matter along to the Lesser Family Head. Now, Assistant Commissioner Li?” Li Feng took over. “We would like to borrow the strength of the Jin Family of Taiyuan for this matter.” “This matter being…?” “I believe you’re aware of our plan to focus on connecting Shaanxi and Shanxi.” “The thing you originally intended to do with the Zhongnan Sect?” Hong Jin, who had been watching us, nodded. “To be honest, the Zhongnan Sect isn’t a bad partner. It’s a massive sect belonging to the Nine Sects and One Gang, and its leadership, including the Sect Leader, the Wind-and-Cloud Sword Lord, has a practical nature. They’re different from the other, relatively closed-off Murim sects.” “Then was there really any need to switch partners? If you hadn’t intended to work with Huashan from the start, leaving things as they were might have been better.” “It was a decision I reached after giving it a great deal of thought. Although we overturned it today.” Hong Jin smiled faintly and continued. “I’m not a martial artist, but I’m well aware of the Sword Saint’s standing in Murim.” “…” “But it has been more than thirty years since the Sword Saint disappeared. If we had known sooner that he had remained at Huashan and was raising successors, we wouldn’t have chosen the Zhongnan Sect.” When he finished speaking, Hong Jin shot Li Feng a reproachful look. Apparently, Li Feng had known about the Sword Saint and Cheongpung for the past ten years without breathing a word of it. “Deputy Military Commissioner, I’ll say it again: that was classified information belonging to our sect. There was simply no longer any reason to conceal it once Martial Uncle Cheongpung descended the mountain.” Li Feng replied calmly, then turned to me. “I’ll get straight to the point. We need an Escort Bureau capable of expanding into the Central Plains, starting with Shaanxi.” *Ah.* I had a rough idea of what was going on. They were asking the Jin Family of Taiyuan to provide material or human resources. “Are you planning to create an Escort Bureau?” “Something similar. However, we would like to borrow the name of the Jin Family of Taiyuan. In return, we’ll provide half the funding and every possible convenience.” They were openly offering to back us. Wouldn’t it be better for them to create an Escort Bureau themselves at this point? As I wondered about that, I suddenly remembered what Jin Mukyung had told me a few days ago. *He said that the current Emperor also assassinated his older brother, the Crown Prince, and ascended the throne. I’m sure of it.* It was only an unconfirmed rumor, but judging by how cautiously these two were acting, it didn’t seem entirely baseless. Could the Emperor’s wariness have been the reason he sent his only younger brother to Shanxi Province, a region treated as a frontier? *Hmm. Something about this smells fishy too.* As I wondered whether I had gotten myself entangled in something dangerous, the two men spoke to me. “We’ll arrange a meeting regarding this matter in the coming days. Please put in a good word with the Lesser Family Head.” “Young Master Jin, you know this is a good offer, right?” “I know. I do, but…” Looked at one way, this was someone else’s family feud. Ordinary brothers might fight over who got an extra ice cream, give each other bloody noses, and call it a day. But this wasn’t ice cream. It was the imperial throne. A bloody nose wouldn’t be the end of it. “I’ll make sure to pass it along to my eldest brother.” I deliberately kept my answer noncommittal. Jin Wikyung would be the one making the decision anyway, so there was no reason for me to worry about it—unless he asked for my opinion first. “That will be enough. He won’t simply dismiss something Young Master Jin tells him. We’ve heard plenty about how much the Lesser Family Head cherishes his younger brothers.” *So the whole neighborhood knows.* I drained my cup of liquor with an embarrassed look, only to meet the eyes of the four of them sitting at the far end of a table some distance away. They all looked as though they were about to get indigestion. Oh, right. I’d almost forgotten something. “Excuse me. Comrade Chairman—no, Deputy Military Commissioner.” “Yes?” “That Escort Bureau business. Wouldn’t it be enough to simply change the sign?” Unlike the bewildered Li Feng, Hong Jin grinned. “You have a place in mind?” “The one the two of you were talking about earlier.” “The Seongun Escort Bureau? Don’t take them too lightly. It’s the foremost Escort Bureau in Shanxi, after all. They’ll be difficult to swallow in one bite.” “That’s why we have to chew thoroughly.” One look at their Young Bureau Head had told me exactly what we were dealing with. With Hong Jin and Li Feng backing the Jin Family of Taiyuan as it now stood, we could chew them up bones and all—and still digest them.

## Korean source

```text
＃145화



홍진이 피식 웃으며 술잔을 기울였다.

“우리 진 공자, 생각보다 욕심이 많으시구나?”

“남들만큼은 있는 편이죠. 그리고 부탁인데, 그냥 진 공자라고 불러 주시면 안 될까요.”

“어머, 좋으면서 싫은 척하기는.”

“족 같네…….”

“응? 방금 뭐라고 했어요?”

“아, 가족 같아서 좋다고요.”

“가족이라, 듣기 좋네. 벌써부터 진 소가주님과의 만남이 기다려지는데요?”

맞다. 이 자리에 입 아프게 떠들어 봤자 결국 결정하는 건 진위경과 홍진이다.

둘 다 이 방면에서는 프로나 다름없으니 아마추어는 빠져 줘야 하는 게 도리겠지.

“그나저나 성운표국에는 무슨 악감정이 있어서 이러는 거예요?”

“악감정이랄 것까진 없고…… 미운 놈 뺨 한 대 더 때려 주는 거죠. 떡고물도 챙길 수 있으니 좋고.”

“아하, 원래 오기로 했던 성운표국의 소국주와 관련된 일?”

이 인간, 눈치가 보통이 아니다.

대강 눈치챈 마당에 괜히 미주알고주알 설명할 필요도 없을 것 같아서 어깨를 으쓱해 보였다.

“뭐, 비슷합니다. 어떻게 아셨어요?”

“진 공자. 난 이십 년을 넘게 황궁(皇宮)에서 살았어요.”

“네?”

“눈치 하나로 살아남았다는 뜻이에요. 어린애들 표정 읽는 것 정도야 쉽지.”

홍진이 산서오문의 후기지수들을 턱짓으로 가리켰다.

멀찍이 떨어진 탁자 끄트머리, 바짝 얼어붙은 표정으로 이쪽을 힐끔거리던 녀석들이 화들짝 놀라며 움츠러든다.

“처음 들어올 때부터 저러더라고. 진 공자 눈치만 살살 살피면서.”

“그랬어요?”

“응. 보는 내가 다 애처로울 정도였다니까. 도대체 무슨 짓을 한 거예요?”

“아까 나가신 분들이랑 비슷한 일이 있었죠.”

“종남삼수? 쯧쯧. 사람을 못 알아봤구나?”

역시 척 하면 착이다. 홍진은 안타깝다는 듯이 혀를 찼고, 이풍은 고개를 홱 돌려 후기지수들을 응시했다.

마치 ‘청풍 사숙’을 건드린 놈들이 누군지 똑똑히 기억해 두겠다는 듯한 눈빛이었다.

“헉.”

“도, 도지휘첨사. 아니, 이 대협. 그게 아니옵고…….”

산서성 군부의 실력자인 데다 화산파 속가제자인 이풍이다.

제아무리 관과 무림이 불가침의 관계라지만 잘못 얽히면 산서오문의 미래가 아주 재미없어질 게 뻔하다.

황급히 변명을 늘어놓는 녀석들을 뒤로하고 이풍이 내게 물었다.

“그 얘기, 자세히 들려줄 수 있겠소?”

“다 끝난 얘기예요. 당사자가 직접 빠따도 쳤는데요, 뭘.”

“빠따?”

“아, 두들겨 팼다는 뜻입니다. 물론 그 전에 사과도 했고요.”

“사숙이 직접 말이오? 흠.”

정확히는 한 명만 조졌지만 때리긴 때린 거다.

이풍이 한결 누그러진 눈빛으로 후기지수들을 바라봤다.

“네놈들의 잘못을 알고 있느냐?”

“예, 옛!”

“뼈저리게 느끼고 있습니다!”

곧장 터져 나오는 우렁찬 외침. 이풍도 이풍이지만 청풍의 신분을 알았으니 똥줄이 탈 만하다.

절정 고수인 건 둘째치고, 무려 검성의 제자에 화산파의 적전제자 아닌가.

‘아주 제대로 엿 된 거지.’

산서오문이라고 해 봤자 결국 중소 문파. 구파일방인 화산파가 열받으면 일가친척까지 빠따를 맞을 수도 있다.

아니, 고작 그걸로 끝나면 다행이지.

“오늘 이곳에서 나눴던 대화와 일들은…….”

이풍의 묵직한 음성이 이어지기도 전에 대답이 튀어나왔다.

“함구하겠습니다!”

“무덤까지 갖고 가겠습니다!”

“전 이미 잊었어요!”

“여기가 어디죠? 제가 누구죠?”

……아주 지랄들을 하는구나.

기억상실증 환자가 속출하는 광경을 바라보고 있던 나는 한마디를 보탰다.

“그걸로 되겠어?”

“예, 예?”

“그게 무슨 말씀이신지…….”

“무슨 말씀이긴. 한 식구 되고 싶으면 너희도 숟가락 얹으라는 얘기지. 거기 너, 식구 뜻이 뭐야?”

지목당한 후기지수가 더듬더듬 대답했다.

“같이 밥 먹는…… 아니라면 죄송합니다.”

“맞았어. 자, 그럼 식구가 되려면 어떻게 해야 할까?”

“아!”

후기지수가 탄성과 함께 이마를 탁 쳤다.

그나마 눈치는 좀 있는 놈이군.

“그럼 다음에 제가 좋은 자리를 마련하겠습니다. 홍화루 어떠십니까?”

“…….”

돌대가리가 따로 없네.

후계자라는 것들이 이 모양이니 산서오문 꼬라지는 안 봐도 뻔하다. 나는 한숨을 푹 내쉬고 간단명료하게 설명해 주었다.

“홍화루는 집어치우고 우리 쪽에서 시키는 거 잘하란 말이야. 가령 성운표국에 관련된 문제라든가, 응?”

“아아.”

태원진가는 분명 산서 제일의 세력을 갖추게 됐지만 중소 문파가 똘똘 뭉쳐 반발한다면 피곤한 일이 생길 게 뻔했다.

명색이 정파 무림 소속인데, 마적 떼처럼 닥치는 대로 뺏고 책임을 물었다가는 손가락질을 받을 테니까.

무림에서 무공만큼이나 중요한 것이 바로 명분 아닌가?

‘하지만 손가락질할 놈들만 없다면 문제 될 것도 없지.’

나는 네 명의 남녀를 천천히 눈에 담았다. 산서오문 중 성운표국을 제외한 네 문파의 후계자들.

이들이 앞장서서 태원진가의 손을 들어 준다면 일이 한층 쉬워질 거다.

“밥 먹을 때 어디에 앉아야 할지 잘 봐. 그래야 한 입씩이라도 얻어먹지.”

비록 변방이라지만 명색이 한 성에서 첫손가락에 꼽는다는 성운표국. 이만하면 조금씩 나눠 먹어도 충분한 진수성찬이다.

내 말에 눈치 빠른 놈은 조용히 눈을 반짝였고, 눈치 없는 놈은 조심스럽게 입을 열었다.

“그래도 그건 좀…….”

나는 어벙해 보이는 놈의 말을 칼같이 잘라 냈다.

“너, 어디 문파 소속이냐?”

“저, 저 말씀이십니까?”

“그래, 너.”

한참을 머뭇거린 끝에 고평문이라는 이름이 튀어나왔다.

얼핏 들어 본 이름 같긴 한데, 기억이 가물가물한 듣보잡 문파. 고평문의 위치는 딱 그 정도다.

아니, 신(新) 산서오문의 위치가 전부 마찬가지였다.

“고평문. 고평문…… 어감이 별로네. 내가 새로 하나 추천해 줘?”

“예?”

아직도 감을 못 잡는 놈의 눈동자를 들여다보며 말을 이었다.

“다음 달부터는 새 이름으로 다시 시작하자. 태원진가 고평지부로. 어때?”

“……!”

“……!”

“마음에 안 드나 보네. 그냥 한번 해 본 소리야, 인마.”

물론 그냥 해 본 소리는 아니지.

나는 새파랗게 질린 고평문 소문주의 어깨를 탁탁 두드리며 좌중을 쓸어 봤다.

“여기 우진태랑 의형제, 의남매 맺은 사람 있냐?”

“어, 없습니다.”

“아니면 어릴 때부터 십 년 넘게 봐 온 끈끈한 사이라든지. 태중 혼약이라든지. 뭐 많잖아?”

“절대! 절대 아닙니다. 몇 번 어울린 게 전부예요.”

“저, 저도 비단 몇 필 선물 받고 보석 조금…….”

“그럼 됐네.”

짝!

날카로운 박수 소리에 네 남녀의 몸이 흠칫 떨렸다.

“선택해. 태원진가와 화산파, 그리고 관까지 적으로 돌릴 건지, 아니면…….”

나는 씩 웃으며 또박또박, 마지막 말을 읊었다.

“별로 안 친한 놈 버리고 우리랑 같이 나눠 먹을 건지.”

짝짝짝짝.

이번에는 내가 아니다. 홍진이 깔깔 웃으며 박수를 치고 있었다.

“우리 진 공자, 보면 볼수록 마음에 든다니까?”

“…….”

그런 위험 발언은 자제해 주십시오, 형님.



* * *



“벌써 가는 것이냐?”

여전히 오만한 말투였지만 목소리와 눈빛에는 아쉬움이 한가득이다.

‘자식, 볼수록 귀엽네.’

나는 꼬마 팬, 아니 상산왕 주표의 머리를 쓰다듬어…… 주려다가 이풍의 눈빛에 손을 내렸다.

아, 맞다. 얘 왕이었지. 그것도 황족.

“커흠. 저도 급한 볼일이 있는지라.”

“나중으로 미루면 안 되겠느냐?”

“죄송합니다. 한시를 다투는 일이라서.”

“그런가…….”

시무룩한 꼬맹이의 얼굴을 보니 살짝 죄책감이 들기는 개뿔, 얼른 본가로 돌아가서 푹 쉬고 싶다.

때맞춰 홍진이 간드러진 목소리로 끼어들었다.

“전하, 제가 있으니 여기 진 공자는 그만 보내 주세요. 네?”

그러나 주표는 고집스러운 얼굴로 날 바라볼 뿐이었다.

“하면 언제쯤 그대를 다시 볼 수 있지?”

“어, 글쎄요. 천 밤쯤 지나면?”

“천 밤!”

주표가 충격받은 얼굴로 외쳤다.

약 3년. 이제 고작 열 살인 어린아이에겐 어마어마한 시간일 것이다.

“그, 그렇게 바쁘단 말이냐?”

“어른의 사정이란 것이 있습니다. 전하.”

“허어어, 돌아가신 아바마마께서도 그 정도는 아니셨는데…….”

상심이 매우 큰 모양이다. 고개를 푹 떨군 주표를 일으켜 세운 건 다음 순간 들려온 이풍의 한마디였다.

“전하, 이렇게 하시는 것은 어떻겠습니까?”

“뭘 말인가?”

“보름 후 태원진가에서 성대한 연회가 열린다고 하니 전하께서 직접 태원진가를 방문하시는 겁니다.”

“태원진가를?”

“예. 산서에서 난다 긴다 하는 고수들이 모두 모일 테니 분명 흡족하실 겁니다.”

주표의 눈동자가 반짝반짝 빛났다.

“옳거니, 그런 방법이 있었구나!”

“예, 전하.”

“…….”

아니, 이것들이 지금 무슨 얘기를 하고 있는 거야.

초대도 안 했는데 아주 상상의 나래를 펼치고 있다. 그렇다고 오지 말라고 하면 일이 터질 기세라 그냥 고개를 끄덕이는 수밖에 없었다.

“이 대협 말이 맞습니다. 그때 한번 놀러 오세요.”

“그래도 될까?”

참 일찍도 물어본다.

나는 영업용 미소를 띠고 대답했다.

“당연하죠. 제 형님들도 반가워할 겁니다.”

“그, 그게 정말인가?”

“네, 제 형님들이 누군지 아시죠? 둘째 형은 구면이실 거고.”

“진천검?”

해맑던 주표의 얼굴에 순간 먹구름이 꼈다.

“그대의 둘째 형은 과인을 싫어한다. 삼 년 전에도 아무 말 없이 밥만 먹고 갔지. 무례하기까지 했어.”

“……아무 말도 안 했다고요?”

“그날에 대한 얘기는 더 이상하기 싫다.”

홍진이 조그마한 목소리로 속삭였다.

“전하께서 서명을 부탁하셨는데 단칼에 거절하더군요.”

진무경이 초청을 받았던 게 3년 전이라고 했으니까…… 주표가 일곱 살 때다.

세상에. 어떻게 일곱 살 어린애, 그것도 왕이 사인을 부탁하는데 딱 잘라 거절할 수 있지?

‘그 인간도 어지간하네.’

어떤 의미에서는 참 진무경답다.

팬심이 무참히 짓밟힌 과거의 기억을 떠올린 주표는 말없이 손가락을 꼬물거렸다.

가만히 보고 있자니 어쩐지 마음 한구석이 짠하다.

“이번에 오시면 제가 부탁해서 서명 받아 드릴게요.”

“헛. 정말?”

“약속. 도장 꽝.”

어리둥절해하는 녀석과 새끼손가락도 걸고 도장까지 찍었다.

“이게 무엇이지?”

“천지신명께 맹세한다. 뭐 그런 뜻입니다.”

“오오!”

주위에서는 황족이니, 왕이니 난리지만 역시 애는 애다.

좋아서 어쩔 줄을 모르는 주표의 모습에 사람들도 흐뭇하게 웃었다.

“전하께서 저렇게 기뻐하시는 모습은 오랜만에 봅니다.”

“그러게요. 매일 재미없는 이 첨사만 상대하다가 오랜만에 활짝 웃으시네요.”

“전 최선을 다한 것밖에 없습니다.”

“최선이 꼭 최고의 결과를 만드는 건 아니죠. 그럴 수 있어요.”

“도지휘동지!”

“왜요, 도지휘첨사?”

이풍과 홍진.

사이가 좋은 건지, 나쁜 건지 도무지 종잡을 수 없는 두 사람이 티격태격할 때 청풍이 잔뜩 기대하는 얼굴로 주표에게 다가갔다.

“저도, 저도 서명해 드릴까요?”

“……당신 서명 처음 해 보지?”

“헛. 어떻게 아셨어요? 오는 길에 쟁자수로 수결(手決)은 해 봤어도 서명은 처음인데.”

“모르는 게 이상한 거 아냐?”

저 기대하는 표정 봐라. 누군가에게 난생처음 서명을 해 주고 싶어서 안달이 난 표정이다.

“저, 전 서명하면 안 되나요?”

“아니. 맘대로 해. 서명해 드리면 전하께서 좋아하실걸.”

하지만 주표의 반응은 예상 밖이었다.

“서명? 그대가?”

“네! 꼭 서명해 드리고 싶습니다!”

“안 된다.”

“왜, 왜요? 저희 할아버지 되게 유명한 분이시래요. 검성 못 들어 보셨어요?”

“알지. 당연히 알지. 하지만…….”

주표가 짐짓 단호한 얼굴로 고개를 저었다.

“그대는 아직 별호가 없지 않나.”

“네?”

“나중에 멋있는 별호가 생기면 다시 오도록. 그땐 내 반드시 서명을 받도록 하지.”

“…….”

“…….”

저거 네임드만 할 수 있는 거였구나.
```

## Current accepted English baseline

```markdown
# Chapter 145

Hong Jin let out a quiet laugh and tilted his cup.

“Our Young Master Jin, you’re greedier than I thought.”

“I’m about as greedy as anyone else. And I have a favor to ask. Could you just call me Young Master Jin?”

“Oh my, pretending you don’t like it when you do.”

“Fucking hell…”

“Hm? What did you say just now?”

“Ah, I said it’s nice. It feels like family.”

“Family, huh? That’s nice to hear. I’m already looking forward to meeting the Lesser Family Head Jin.”

Right. No matter how much I talked in this room, the final decision would be made by Jin Wikyung and Hong Jin.

Both of them were practically professionals in this area, so it was only proper for an amateur to step aside.

“By the way, what grudge do you have against the Seongun Escort Bureau?”

“It’s not quite a grudge… I’m just giving an extra slap to someone I dislike. And it doesn’t hurt that I can pick up a few crumbs along the way.”

“Ah. Is this related to the Young Bureau Head of the Seongun Escort Bureau who was originally supposed to come?”

This man’s instincts were anything but ordinary.

Since he had already figured it out, there seemed to be no need to explain every little detail. I simply shrugged.

“Something like that. How did you know?”

“Young Master Jin, I’ve lived in the imperial palace for more than twenty years.”

“Excuse me?”

“I survived on my ability to read the room. Reading the expressions of children is easy enough.”

Hong Jin gestured with his chin toward the young prodigies of the Five Gates of Shanxi.

At the far end of a distant table, the young men and women had been sneaking glances our way with frozen expressions. They flinched and shrank back when they realized they had been noticed.

“They’ve been like that since they first came in. Carefully watching Young Master Jin’s every move.”

“Really?”

“Yes. I almost felt sorry for them just watching. What on earth did you do?”

“They had something similar happen with the people who left earlier.”

“The Three Hands of Zhongnan? Tsk, tsk. They failed to recognize who they were dealing with, didn’t they?”

As expected, Hong Jin understood everything with the slightest hint. He clicked his tongue sympathetically, while Li Feng abruptly turned his head and stared at the young prodigies.

His eyes seemed to say he would remember exactly who had provoked Martial Uncle Cheongpung.

“Gasp.”

“Assistant Military Commissioner! No, Great Hero Li! It’s not like that…”

Li Feng was not only a powerful figure in the Shanxi Province military but also a lay disciple of Huashan.

Even though the government and Murim were supposed to remain separate, getting entangled with him in the wrong way would make the future of the Five Gates of Shanxi very unpleasant.

Ignoring the young men as they hurriedly offered excuses, Li Feng asked me,

“Could you tell me more about what happened?”

“It’s all over now. The person involved even beat them himself. What more is there to say?”

“Beat them himself?”

“Ah, I mean he beat them up. Of course, they apologized before that.”

“Martial Uncle did it himself? Hmm.”

Strictly speaking, Cheongpung had only dealt with one of them, but he had beaten him all the same.

Li Feng looked at the young prodigies with a much gentler gaze.

“Do you understand what you did wrong?”

“Yes, sir!”

“We feel it in our bones!”

Their booming replies erupted immediately. It wasn’t only Li Feng’s position that had them sweating bullets. They now knew Cheongpung’s identity as well.

Putting aside the fact that he was a Peak master, he was the Disciple of the Sword Saint and Huashan’s direct Disciple.

*They’re completely screwed.*

The Five Gates of Shanxi were ultimately nothing more than a collection of minor sects. If Huashan, one of the Nine Sects and One Gang, got angry, even their extended families might get beaten with a bat.

No, they would be lucky if it ended there.

“The conversations and events that took place here today…”

Li Feng’s heavy voice had barely begun when the answers came flying out.

“We’ll keep silent!”

“We’ll take it to our graves!”

“I’ve already forgotten everything!”

“Where are we? Who am I?”

*They’re really putting on a fucking show.*

As I watched an epidemic of amnesia break out before my eyes, I added one more thing.

“Is that enough?”

“Ex-Excuse me?”

“What do you mean?”

“What do I mean? If you want to become part of the family, you need to put your spoon in too. You there. What does ‘family’ mean?”

The young prodigy I had pointed at stammered out an answer.

“People who eat together… Unless that’s not it, in which case, I’m sorry.”

“That’s right. Now, how do you become family?”

“Ah!”

The young prodigy slapped his forehead with a cry of realization.

At least that one had some sense.

“Then I’ll arrange a fine place for our next meeting. How about Honghwaru?”

“……”

What a complete idiot.

With heirs like these, the state of the Five Gates of Shanxi was obvious without even looking. I let out a deep sigh and explained it simply.

“Forget Honghwaru. I’m telling you to do whatever our side tells you to do. For example, anything involving the Seongun Escort Bureau. Understand?”

“Ohhh.”

The Jin Family of Taiyuan had certainly become the greatest power in Shanxi, but if the minor sects united and resisted, it would inevitably become a nuisance.

We belonged to the orthodox faction, after all. If we seized whatever we wanted and held people accountable like a band of mounted bandits, everyone would point fingers at us.

Wasn’t legitimacy just as important as martial arts in Murim?

*But if there’s no one left to point fingers, it won’t be a problem.*

I slowly took in the four men and women before me—the heirs of the four sects among the Five Gates of Shanxi, excluding the Seongun Escort Bureau.

If they stepped forward and sided with the Jin Family of Taiyuan, things would become much easier.

“When you’re eating, pay close attention to where you sit. That way, you can at least get a bite or two.”

The Seongun Escort Bureau was supposedly one of the most prominent powers in the province, despite being located in a frontier region. It was more than enough of a feast to share around.

At my words, the quick-witted one’s eyes quietly gleamed, while the clueless one cautiously opened his mouth.

“Even so, that might be a little…”

I cut off the dense-looking young man before he could finish.

“What sect are you from?”

“M-Me?”

“Yes, you.”

After a long hesitation, the name Gopyeong Sect finally came out.

It was a name I vaguely recognized—a minor sect so obscure that I could barely remember hearing it. That was about the extent of Gopyeong Sect’s standing.

No, that was true of all the sects in the new Five Gates of Shanxi.

“Gopyeong Sect. Gopyeong Sect… It doesn’t have a very pleasant ring to it. Should I recommend a new name?”

“Excuse me?”

I stared into his eyes as he continued to fail to understand.

“Starting next month, let’s begin again under a new name. The Gopyeong Branch of the Jin Family of Taiyuan. How does that sound?”

“……!”

“……!”

“You don’t seem to like it. I was only saying it for fun, you idiot.”

Of course, I hadn’t been saying it for fun.

I patted the deathly pale Young Sect Leader of Gopyeong Sect on the shoulder and swept my gaze across the room.

“Is anyone here sworn brothers or sisters with Woo Jintae?”

“N-No, sir.”

“Or perhaps you’ve been close friends since childhood, watching each other for more than ten years? Maybe you were betrothed before birth? There are plenty of possibilities.”

“Absolutely not! Absolutely not. We’ve only spent time together a few times.”

“I-I only received a few bolts of silk and a little jewelry…”

“Then that settles it.”

Clap!

The sharp sound of my hands coming together made the four men and women flinch.

“Choose. Are you going to make enemies of the Jin Family of Taiyuan, Huashan, and the government, or…”

I grinned and enunciated the final words clearly.

“Are you going to abandon someone you aren’t even close to and share the feast with us?”

Clap, clap, clap, clap.

This time, it wasn’t me. Hong Jin was laughing loudly and applauding.

“Our Young Master Jin, I like you more and more every time I see you.”

“……”

*Brother, please refrain from making dangerous remarks.*

* * *

“Are you leaving already?”

His tone was still arrogant, but his voice and eyes were filled with regret.

*The more I see him, the cuter he gets.*

I was about to pat the head of my little fanboy—no, Prince Shangshan Zhu Bao—when I lowered my hand under Li Feng’s gaze.

*Oh, right. He was a king. And a member of the imperial family, at that.*

“Ahem. I have some urgent business to attend to.”

“Can you not put it off until later?”

“I’m sorry, but it’s a matter where every moment counts.”

“I see…”

Looking at the dejected kid’s face made me feel a little guilty—like hell it did. I wanted to hurry back home to my family and get some proper rest.

Right then, Hong Jin cut in with his delicate voice.

“His Highness, I’m here, so please let Young Master Jin go now. All right?”

But Zhu Bao only stared at me stubbornly.

“Then when shall I be able to see you again?”

“Hmm, I don’t know. After a thousand nights?”

“A thousand nights!”

Zhu Bao cried out with a shocked expression.

That was approximately three years. For a child who was only ten years old, it must have seemed like an enormous amount of time.

“Are you truly that busy?”

“There are such things as adult matters, Your Highness.”

“Good heavens. Even my late father was never that busy…”

He seemed deeply disheartened. Zhu Bao’s head drooped, but Li Feng’s next words made him straighten up again.

“Your Highness, what do you think of this?”

“What do you mean?”

“I hear the Jin Family of Taiyuan will be holding a grand banquet in fifteen days. Why don’t you pay the Jin Family of Taiyuan a personal visit?”

“The Jin Family of Taiyuan?”

“Yes. All the masters who are famous throughout Shanxi will be gathered there, so I’m sure you’ll be pleased.”

Zhu Bao’s eyes began to sparkle.

“Of course! Why didn’t I think of that?”

“Yes, Your Highness.”

“……”

What the hell were these two talking about?

They hadn’t even been invited, yet they were spreading their wings and soaring through the realm of imagination. But if I told him not to come, it felt as though something would explode, so all I could do was nod.

“Great Hero Li is right. Come visit us then.”

“Would that really be all right?”

He was asking rather late.

I answered with a professional smile.

“Of course. My brothers will be happy to see you too.”

“Is that really true?”

“You know who my brothers are, don’t you? You should already be acquainted with my second brother.”

“Heaven Shaking Sword?”

A dark cloud suddenly fell over Zhu Bao’s bright, innocent face.

“Your second brother dislikes me. Three years ago, he only ate and left without saying a word. He was even rude.”

“He didn’t say a single word?”

“I do not wish to speak of that day anymore.”

Hong Jin whispered in a tiny voice,

“His Highness asked him for an autograph, but he flatly refused.”

Jin Mukyung had said he was invited three years ago, so…

Zhu Bao must have been seven at the time.

Good grief. How could anyone flatly refuse when a seven-year-old child—an actual king, no less—asked for his autograph?

*That man really is something.*

In a way, it was very much like Jin Mukyung.

Recalling how his fanboy enthusiasm had been so brutally crushed, Zhu Bao silently fidgeted with his fingers.

Watching him, I felt a pang of sympathy.

“If you come this time, I’ll ask him to give you his autograph.”

“Really?”

“Pinky promise. Seal it.”

I even hooked pinkies with the bewildered boy and sealed our promise.

“What is this?”

“It means I swear before the gods of heaven and earth.”

“Oh!”

Everyone around us was making a fuss because he was royalty, because he was a king, and so on. But a child was still a child.

Seeing Zhu Bao so happy that he didn’t know what to do, everyone smiled fondly.

“It’s been a long time since I’ve seen His Highness this happy.”

“I know. After dealing with that boring Assistant Military Commissioner every day, he’s smiling brightly for the first time in ages.”

“I’ve only been doing my best.”

“Doing your best doesn’t always produce the best result. It happens.”

“Deputy Military Commissioner!”

“What is it, Assistant Military Commissioner?”

Hong Jin and Li Feng.

I could never tell whether the two of them got along or hated each other as they bickered back and forth.

Meanwhile, Cheongpung approached Zhu Bao with an expectant expression.

“Can I sign something for you too?”

“……”

“You’ve never signed your name before, have you?”

“Gasp. How did you know? I’ve left my hand mark as a luggage porter before, but this is my first autograph.”

“Wouldn’t it be strange if I didn’t know?”

Just look at that eager expression. He looked desperate to give someone his very first autograph.

“C-Can I not sign one?”

“No. Do whatever you want. His Highness will be happy if you give him your autograph.”

But Zhu Bao’s reaction was unexpected.

“An autograph? Yours?”

“Yes! I really want to give you my autograph!”

“No.”

“W-Why not? They say my grandfather is a very famous man. Haven’t you heard of the Sword Saint?”

“I know. Of course I know. But…”

Zhu Bao put on a deliberately stern expression and shook his head.

“You don’t have a martial title yet, do you?”

“Excuse me?”

“Come back after you’ve acquired a cool martial title. Then I shall certainly get your autograph.”

“……”

“……”

*So this was something only named characters could do.*
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 145`.

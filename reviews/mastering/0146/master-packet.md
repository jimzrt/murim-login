# Master Edit Task — Chapter 146

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
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 화산파    | **Huashan**                      |
| 산서오문   | **Five Gates of Shanxi**         |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 영약     | **elixir**                                       |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 표국     | **Escort Bureau**                            |
| 제자     | **Disciple**                                 |
| 사숙     | **Martial Uncle**                            |
| 사질     | **Martial Nephew**                           |
| 은인     | **Benefactor**                               |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 정삼품 | **Third-Rank** | Official rank of the unnamed Assistant Military Commissioner. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 도지휘사 | **Military Commissioner** | Provincial military commander's office |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 근위대 | **royal guard** | Guard unit protecting Prince Shangshan. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 이풍 | 청풍 | Huashan lay disciple to martial uncle | Young Hero; Martial Uncle Cheongpung | formal and reverent | Li Feng initially addresses Cheongpung as 소협 while testing his knowledge, then recognizes him as 사숙 after witnessing his Huashan sword technique. |
| 청풍 | 이풍 | Martial Uncle to Martial Nephew | Martial Nephew Li Feng | exuberant and deferential | Cheongpung adopts the address to obtain royal-guard armor and weapons. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 이풍 | 주표 | official_to_prince | Your Highness | formal-deferential | Suggests that Zhu Bao visit the Jin Family's grand banquet in fifteen days. |
| 주표 | 청풍 | prince_to_young_martial_artist | you | formal and gatekeeping | Refuses Cheongpung's autograph until he acquires a martial title. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
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

#### Chapter 144 tail (verified mastered)

…
Beside Li Feng, of course. I’ll say it again: my ass is precious. “Let’s hear what this is about. I’m not very knowledgeable in this area, so I may not be much help.” Hong Jin had been pouting in feigned disappointment. Now he spoke. “It doesn’t matter if Young Hero Jin doesn’t make a decision here. You only need to pass the matter along to the Lesser Family Head. Now, Assistant Commissioner Li?” Li Feng took over. “We would like to borrow the strength of the Jin Family of Taiyuan for this matter.” “This matter being…?” “I believe you’re aware of our plan to focus on connecting Shaanxi and Shanxi.” “The thing you originally intended to do with the Zhongnan Sect?” Hong Jin, who had been watching us, nodded. “To be honest, the Zhongnan Sect isn’t a bad partner. It’s a massive sect belonging to the Nine Sects and One Gang, and its leadership, including the Sect Leader, the Wind-and-Cloud Sword Lord, has a practical nature. They’re different from the other, relatively closed-off Murim sects.” “Then was there really any need to switch partners? If you hadn’t intended to work with Huashan from the start, leaving things as they were might have been better.” “It was a decision I reached after giving it a great deal of thought. Although we overturned it today.” Hong Jin smiled faintly and continued. “I’m not a martial artist, but I’m well aware of the Sword Saint’s standing in Murim.” “…” “But it has been more than thirty years since the Sword Saint disappeared. If we had known sooner that he had remained at Huashan and was raising successors, we wouldn’t have chosen the Zhongnan Sect.” When he finished speaking, Hong Jin shot Li Feng a reproachful look. Apparently, Li Feng had known about the Sword Saint and Cheongpung for the past ten years without breathing a word of it. “Deputy Military Commissioner, I’ll say it again: that was classified information belonging to our sect. There was simply no longer any reason to conceal it once Martial Uncle Cheongpung descended the mountain.” Li Feng replied calmly, then turned to me. “I’ll get straight to the point. We need an Escort Bureau capable of expanding into the Central Plains, starting with Shaanxi.” *Ah.* I had a rough idea of what was going on. They were asking the Jin Family of Taiyuan to provide material or human resources. “Are you planning to create an Escort Bureau?” “Something similar. However, we would like to borrow the name of the Jin Family of Taiyuan. In return, we’ll provide half the funding and every possible convenience.” They were openly offering to back us. Wouldn’t it be better for them to create an Escort Bureau themselves at this point? As I wondered about that, I suddenly remembered what Jin Mukyung had told me a few days ago. *He said that the current Emperor also assassinated his older brother, the Crown Prince, and ascended the throne. I’m sure of it.* It was only an unconfirmed rumor, but judging by how cautiously these two were acting, it didn’t seem entirely baseless. Could the Emperor’s wariness have been the reason he sent his only younger brother to Shanxi Province, a region treated as a frontier? *Hmm. Something about this smells fishy too.* As I wondered whether I had gotten myself entangled in something dangerous, the two men spoke to me. “We’ll arrange a meeting regarding this matter in the coming days. Please put in a good word with the Lesser Family Head.” “Young Master Jin, you know this is a good offer, right?” “I know. I do, but…” Looked at one way, this was someone else’s family feud. Ordinary brothers might fight over who got an extra ice cream, give each other bloody noses, and call it a day. But this wasn’t ice cream. It was the imperial throne. A bloody nose wouldn’t be the end of it. “I’ll make sure to pass it along to my eldest brother.” I deliberately kept my answer noncommittal. Jin Wikyung would be the one making the decision anyway, so there was no reason for me to worry about it—unless he asked for my opinion first. “That will be enough. He won’t simply dismiss something Young Master Jin tells him. We’ve heard plenty about how much the Lesser Family Head cherishes his younger brothers.” *So the whole neighborhood knows.* I drained my cup of liquor with an embarrassed look, only to meet the eyes of the four of them sitting at the far end of a table some distance away. They all looked as though they were about to get indigestion. Oh, right. I’d almost forgotten something. “Excuse me. Comrade Chairman—no, Deputy Military Commissioner.” “Yes?” “That Escort Bureau business. Wouldn’t it be enough to simply change the sign?” Unlike the bewildered Li Feng, Hong Jin grinned. “You have a place in mind?” “The one the two of you were talking about earlier.” “The Seongun Escort Bureau? Don’t take them too lightly. It’s the foremost Escort Bureau in Shanxi, after all. They’ll be difficult to swallow in one bite.” “That’s why we have to chew thoroughly.” One look at their Young Bureau Head had told me exactly what we were dealing with. With Hong Jin and Li Feng backing the Jin Family of Taiyuan as it now stood, we could chew them up bones and all—and still digest them.

#### Chapter 145 tail (verified mastered)

…
cuter he gets.* I reached out to pat my little fanboy—no, Prince Shangshan Zhu Bao—on the head, only to lower my hand when I saw Li Feng’s expression. *Oh, right. He’s a king. And a member of the imperial family, at that.* “Ahem. I have urgent business to attend to.” “Can you not put it off?” “I’m sorry, but every moment counts.” “I see…” Looking at the dejected kid’s face made me feel a little guilty—like hell it did. I wanted to hurry back home to my family and get some proper rest. Right on cue, Hong Jin cut in with his delicate voice. “Your Highness, you have me, so please let Young Master Jin go now. All right?” But Zhu Bao merely stared at me, his expression stubborn. “Then when shall I be able to see you again?” “Hmm, I don’t know. After a thousand nights?” “A thousand nights!” Zhu Bao cried out in shock. That was approximately three years. For a child who was only ten years old, it must have seemed like an enormous amount of time. “A-Are you truly that busy?” “There are such things as adult matters, Your Highness.” “Good heavens. Even my late father was never that busy…” He looked utterly crushed. Zhu Bao’s head drooped, only to shoot back up at Li Feng’s next words. “Your Highness, how about this?” “What do you mean?” “I hear the Jin Family of Taiyuan will be holding a grand banquet in fifteen days. Why not visit the Jin Family of Taiyuan in person?” “The Jin Family of Taiyuan?” “Yes. All the renowned masters of Shanxi will be gathered there, so I’m sure you’ll be pleased.” Zhu Bao’s eyes sparkled. “Of course! Why didn’t I think of that?” “Yes, Your Highness.” “……” What the hell were these two talking about? They hadn’t even been invited, yet here they were letting their imaginations run wild. But if I told him not to come, it felt as though something would explode, so all I could do was nod. “Great Hero Li is right. Come visit us then.” “Would that really be all right?” A little late to ask, wasn’t it? I put on my best customer-service smile. “Of course. My brothers will be happy to see you too.” “I-Is that really true?” “You know who my brothers are, don’t you? You’ve already met my second brother.” “The Heaven Shaking Sword?” A dark cloud suddenly fell over Zhu Bao’s bright, innocent face. “Your second brother dislikes me. Three years ago, he only ate and left without saying a word. He was even rude.” “He didn’t say a single word?” “I do not wish to speak of that day anymore.” Hong Jin whispered in a tiny voice, “His Highness asked him for an autograph, but he flatly refused.” Jin Mukyung had been invited three years ago, which meant… Zhu Bao had been seven at the time. Good grief. How could anyone flatly refuse a seven-year-old asking for an autograph—especially when that seven-year-old was a king? *That man really is something else.* In a way, it was very Jin Mukyung. Recalling how his fanboy enthusiasm had been so brutally crushed, Zhu Bao silently fidgeted with his fingers. Watching him, I felt a pang of sympathy. “If you come this time, I’ll ask him to give you his autograph.” “Really?” “Pinky promise. Seal it.” I hooked pinkies with the bewildered boy and even stamped our thumbs together. “What is this?” “It means I swear before the gods of heaven and earth. Something like that.” “Oh!” Everyone around us was making a fuss because he was royalty, because he was a king, and so on. But a child was still a child. Everyone smiled fondly at the sight of Zhu Bao beside himself with delight. “It’s been a long time since I’ve seen His Highness this happy.” “I know. After dealing with this boring Assistant Military Commissioner every day, he’s smiling brightly for the first time in ages.” “I’ve done nothing but my best.” “Doing your best doesn’t always produce the best results. It happens.” “Deputy Military Commissioner!” “What is it, Assistant Military Commissioner?” Li Feng and Hong Jin. I could never tell whether the two of them got along or hated each other as they bickered back and forth. Meanwhile, Cheongpung approached Zhu Bao with anticipation written all over his face. “I-I could give you an autograph too?” “……” “You’ve never given anyone an autograph before, have you?” “Gasp. How did you know? I’ve left my hand mark as a porter on the way here, but this is my first autograph.” “Wouldn’t it be strange if I didn’t know?” Just look at that expectant face. He was dying to give someone his first-ever autograph. “C-Can’t I give him one?” “Sure. Do whatever you want. His Highness will probably be pleased.” But Zhu Bao’s reaction was unexpected. “An autograph? From you?” “Yes! I really want to give you my autograph!” “No.” “W-Why not? They say my grandfather is very famous. Haven’t you heard of the Sword Saint?” “I know. Of course I know. But…” Zhu Bao put on a deliberately stern expression and shook his head. “You don’t have a martial title yet, do you?” “Excuse me?” “Come back after you’ve acquired a cool martial title. Then I shall certainly get your autograph.” “……” “……” *So this was something only named characters could do.*

## Korean source

```text
＃146화



모든 만남에는 헤어짐이 있는 법.

눈에 익은 육두마차가 가까이 다가오자 주표가 손바닥만 한 뭔가를 내게 내밀었다.

“이게 뭡니까?”

“오늘 만남에 대한 과인의 보답이다.”

“어이쿠, 뭐 이런 걸 다…….”

건네받아 자세히 살펴보니 일종의 황금 메달이다.

표면에 구름과 용이 섬세하게 음각된 그것은 햇빛을 받아 번쩍 빛났다.

띠링.



- 퀘스트 대상이 오늘의 만남을 매우 흡족해합니다!

- 퀘스트 보상으로 [상산왕의 증표]를 얻었습니다!



“과인의 증표다. 혹시 따로 원하는 물건이나 소원이 있다면 증표를 들고 찾아오너라. 내 힘이 닿는 데까지 들어줄 터이니.”

“오.”

교환 쿠폰이네.

중국집 쿠폰은 스무 장에 탕수육 대짜인데, 이건 무려 상산왕의 교환 쿠폰이니까 각종 영약이나 보물로 바꿀 수 있을지도 모르겠다.

‘안 그래도 무기가 하나 필요하긴 한데.’

열화신단을 흡수한 덕분에 공력은 충분한 상황.

다만 쓸 만한 창이 없다는 게 아쉽던 차다. 다른 무기들은 처음부터 거의 일회용 젓가락처럼 쓰고 버리는 수준이었으니까.

‘아예 지금 확 바꿔 버려?’

순간 고민했지만 이내 고개를 저었다.

이미 큰 위기는 넘겼다. 급할 것 없는 상황에 왕의 증표를 무기 하나와 교환하기에는 너무 아깝다.

“감사합니다. 저 이거 되게 갖고 싶었던 건데.”

허리를 꾸벅 숙이자 주표가 까치발을 들고 내 머리를 쓱쓱 쓰다듬었다.

“그대가 좋아하니 나도 기쁘다.”

“…….”

이거 되게 기분 묘하네. 귀여우니까 봐준다.

그사이 우리를 데려다줄 마차가 멈춰 섰다. 마차에 오르려는 내게 주표가 손을 흔든다.

“조심히 가게! 다음에 또 와!”

다음에는 네가 와야지, 인마.

새해 첫날, 그러니까 원단(元旦)까지는 고작 보름 남짓 남았다. 아마 그때쯤 어린 왕을 다시 만날 수 있을 것이다.

“그럼 이만.”

“다녀오겠습니다, 전하.”

마차가 워낙 크다 보니 입구도 넓다. 나와 홍진은 나란히 마차에 올랐다.

“……응?”

아니, 잠깐만. 너무 자연스러워서 넘어갈 뻔했네.

나는 황당한 마음을 담아 홍진을 바라봤다.

“뭡니까?”

“응? 왜요?”

“이거 태원진가 가는 마차인데요.”

“알아요. 그래서 탄 거지.”

“예?”

“쇠뿔도 단김에 빼라고. 이참에 진 소가주님과 이야기를 한번 나눠 봐야 하지 않겠어요?”

빙긋 웃은 홍진이 손가락을 튕기자 관리 한 명이 바람처럼 달려왔다.

“도지휘동지. 분부하실 일이라도?”

“선약도 없이 방문하는데 선물이라도 듬뿍 가져가야지. 미리 전령을 보내서 정중히 인사드리는 것도 잊지 말고.”

“명을 받들겠습니다!”

이풍도 휘하의 장수에게 지시를 내렸다.

“귀빈이시다. 태원진가까지 모셔다드려라.”

“충!”

두 사람의 명령에 자그마치 백 명에 달하는 병력과 급하게 꾸려진 사절단이 일사불란하게 움직이기 시작한다.

그 광경에 뒤따라 오르려던 청풍이 작게 박수를 쳤다.

“우와.”

그토록 염원하던 근위대 굿즈 세트를 손에 넣은 그는 당분간 태원진가에 머무르기로 했다.

이풍이 나를 향해 고개를 까딱 숙였다.

“사숙을 부탁드리겠소.”

“별말씀을.”

그런 말을 굳이 듣지 않아도 이쪽에서 먼저 친하게 지내고 싶은 상대다.

청풍을 징검다리 삼아 화산파와의 관계를 돈독히 한다면 태원진가의 앞날도 화창할 게 분명하니까.

‘재밌는 놈이기도 하고.’

청풍이 해맑게 웃으며 손을 흔들었다.

“이풍 사질, 난 걱정하지 말아요! 진 공자랑 같이 있으면 재미있는 일이 자꾸자꾸 생기거든요!”

“……혹시 싶어서 말해 두는데, 사고만 치지 마십쇼.”

“네!”

대답은 잘한다.

나는 남아 있는 사람들을 향해 고개를 돌렸다.

“너희는 어떻게 하기로 했어?”

산서오문의 후기지수들이 우물쭈물 대답했다.

“원단이 다가올 때까지 홍화객잔에 묵을 계획입니다.”

“본가에 다녀오기에는 워낙 시간이 빡빡하기도 하고…….”

“사실 돌아갈 엄두도 안 납니다.”

“지금 돌아가면 아버지께서 절 죽이실지도 몰라요.”

우울하기 짝이 없는 대답이다.

하긴, 지금쯤이면 전날 있었던 일에 대한 소문이 날개 달린 말처럼 퍼져 나가고 있을 테니 그럴 만도 하다.

나는 녀석들을 보며 혀를 찼다.

“원단까지는 얌전하게 있어라. 문주님들께는 나중에 말 잘해 놓을 테니까.”

“저, 정말이십니까?”

“그 대신 너희도 각자 잘하고. 무슨 얘긴지 알지?”

“성운표국…… 예, 알겠습니다.”

이미 대세는 거스를 수 없다. 이제는 이 녀석들도, 산서오문의 문주들도 그 사실을 알 것이다.

앞으로는 그저 태원진가의 밑에서 최대한 몸집을 불리는 수밖에.

“그래, 그럼 수고들 하고 원단에 보자.”

“네?”

“왜, 뭐.”

“저, 저희도 가는 길인데요.”

“어디. 홍화객잔?”

“예.”

나는 황당해하는 녀석들에게 한마디를 날렸다.

“이거 태원진가 급행이야.”

쾅!

문이 닫히기 무섭게 마차가 움직이기 시작했다.



* * *



여섯 명이 앉아도 넓었던 내부다. 나와 청풍, 그리고 홍진 세 사람은 각자 몇 자리씩을 차지하고 푹신한 좌석에 몸을 기댔다.

“여기서 살아도 될 것 같아요.”

행복한 웃음을 띤 청풍이 말을 이었다.

“할아버지와 살 때는 풀이나 돌 위에서 잤거든요. 이제는 그렇게 못 살 것 같아요.”

문명을 접한 원시인이 따로 없네.

그 말에 홍진이 호기심 어린 눈빛으로 물었다.

“그럼 공자께서는 줄곧 화산에 살았던 건가요?”

“네. 엄청 어릴 때부터요. 하지만 화산에서 태어난 건 아니래요. 예전에 할아버지께 여쭤본 적이 있는데, 화산에 온 건 제가 서너 살 때라고 들었어요.”

그렇겠지. 검성이 아무리 엄청난 고수라지만 육아에는 한계가 있기 마련이다.

초절정 고수가 된다고 남자 가슴에서 젖이 나오지는 않을 테니까.

“…….”

아냐, 초절정 고수라면 혹시 몰라.

검기, 검강도 쓰는 괴물들인데 젖 정도야 나올 수 있지.

나는 호호백발 할아버지가 갓난아기에게 젖을 물리는 장면을 상상해 보았다.

“우웩.”

“은인, 괜찮으세요?”

“진 공자. 괜찮아요?”

“괜찮습니다. 잠깐 속이 메슥거린 것뿐이에요.”

“어머, 그러면 안 되지. 자, 내 무릎에 누워요.”

“…….”

확 그냥 무릎을 부숴 버릴까 보다.

내가 눈으로 쌍욕을 퍼붓자 홍진이 입을 가리며 웃었다.

“호호, 역시 진 공자는 놀리는 재미가 있다니까.”

미인이 저런 말을 했다면 나도 따라서 헤헤 웃었을 텐데, 홍진은 명백한 남자다. 얼굴에 하얗게 분을 칠하고 입술에 뭘 발라도 그 사실은 달라지지 않는다.

‘내관 출신이라고 했지.’

내관이면 내시 아닌가?

예전에 듣기로는 내시라고 해서 꼭 고자는 아니라던데. 하지만 홍진이 달린 놈인지 안 달린 놈인지 구분할 방법이 없다.

“진 공자.”

“예, 예?”

“지금 어디 보고 있어요?”

“아, 뭐가 묻은 것 같아서 그만.”

젠장, 걸렸네.

무림인은 아닌데 눈치가 절정 고수 급이다. 홍진의 하체에서 시선을 뗀 나는 황급히 화제를 돌렸다.

“그런데 이풍 대협은 어쩌다가 군문에 들어가게 된 겁니까?”

“이 첨사? 당연히 무과에 급제해서 들어온 거죠. 그 후로는 쭉 탄탄대로였고.”

“역시 화산파 속가제자라 다르긴 하군요.”

“영향이 없다고는 말 못 하겠지만 꼭 그런 것만은 아니에요. 고작 십 년 만에 정삼품 도지휘첨사가 된다는 건 정말 어려운 일이거든.”

“정삼품이라면……?”

“정삼품이 뭐예요? 먹는 건가?”

높은 직책인 건 대충 알겠는데 딱 거기까지다.

영 감을 못 잡는 나와 청풍에게 홍진이 차근차근 설명해 주었다.

“고위직이죠. 각 성에 겨우 넷밖에 없는 데다가 이 첨사 같은 경우는 품계로 군부에서 세 손가락 안에 들어요.”

홍진이 손가락을 하나씩 꼽았다.

“총사령관인 도지휘사, 그 아래가 나. 그리고 세 번째가 이 첨사. 물론 모두의 위에 계신 분이 상산왕 전하시고.”

“도지휘사요?”

“곧 은퇴를 앞둔 분이죠. 대장군의 아들로 태어나 약간의 공을 세웠고 뇌물을 엄청나게 좋아하시는.”

부패한 군인이군. 생계형 비리가 일상이 되어 버린.

총사령관이라는 인간이 그 모양이니 근래 산서성 치안이 엉망이었던 것도 충분히 설명이 된다.

“지금의 도지휘사는 무능해요. 항산검문이 무너지자마자 마적 떼가 활보하는 것만 봐도 알 수 있죠.”

“그렇게 무능하면 차라리…….”

잘라 버리지 그러십니까, 라는 말을 내뱉기 전에 꿀꺽 삼켰다. 내가 뭐라고 남의 직장 일에 관여를 하나. 그것도 고위 공무원들인데.

이런 내 반응에 홍진이 친절한 설명을 덧붙였다.

“도지휘사는 황상께서 직접 임명하세요. 해임도 마찬가지고.”

“아.”

“뭐, 그래도 그 이상의 욕심은 없으니 다행이죠. 나도 뇌물 좋아하니까 욕할 처지는 아니고.”

뭐 이런 놈이 다 있어.

각종 뇌물 수수 혐의에 결백을 주장하는 정치인들은 TV에서 많이 봤지만 홍진 같은 경우는 처음이다.

“왜요, 내가 그렇게 청렴해 보였나?”

“아뇨. 뇌물 좋아하실 것 같긴 했는데…….”

“이렇게 대놓고 말할 줄 몰랐다?”

“뭐, 그렇죠. 솔직히 지금 살짝 당황했습니다.”

“진 공자. 그거 알아요?”

홍진이 진지한 표정으로 말을 이었다.

“나, 물건이 없어.”

“예?”

“고자라고.”

“…….”

이거 뭐 어떻게 대답해야 하냐. 짐작은 했지만 이런 폭탄 발언을 갑자기 던질 줄이야.

창밖을 구경 중이던 청풍이 궁금한 듯한 얼굴로 대뜸 끼어들었다.

“고자가 뭐예요?”

“……제발, 제발 입 좀 다물어.”

고추가 없다잖아, 고추가!

일분일초가 느릿하다. 나는 식은땀을 흘리며 입을 열었다.

“유감입니다.”

“유감일 것까지야. 살다 보면 없는 사람도 있고, 있는 사람도 있지. 안 그래요?”

“그……렇죠.”

존경스러운 마인드에 괜히 나까지 숙연해진다.

그 와중에 고자의 뜻을 모르는 원시인 놈은 눈치도 없이 자꾸 떠들어 댔다.

“은인, 고자가 뭔지 알려 주시면 안 돼요?”

죽어도 안 알려 줄 거다. 절대.

알려 줘 봤자 ‘와, 저 고추 없는 사람 처음 봐요!’ 이딴 소리 지껄일 확률이 99.99%니까.

하지만 홍진은 의연했다.

“고자는 고추가 없어요.”

“와, 저 고추 없는 사람 처음…….”

“아, 닥치라고!”

헉, 깜짝 놀란 청풍이 헛숨을 들이켰다.

“으, 은인.”

“진정해요. 진 공자. 산에서 살다 왔으면 그럴 수도 있죠. 그리고 뭐, 내가 하루 이틀 고자로 살고 있는 것도 아니고.”

“그래도 말이 너무 심하잖아요.”

“제가 잘못한 거예요? 정말 죄송합니다.”

“괜찮아요. 어깨 펴. 아직 달려 있잖아.”

고자 수십 년 짬밥이 어디 가는 게 아니구나.

진정하라는 듯 손을 내저은 홍진은 대수롭지 않게 말을 이어 갔다.

“내가 내린 결정에 대해서는 후회한 적 없어요. 일가 피붙이가 굶어 죽어 가는 마당에 뭐든 못 하겠어. 안 그래요?”

“암요. 그렇죠.”

“저도, 저도 그랬을 거예요!”

지금은 홍진이 무슨 말을 하든 맞장구쳐 줘야 한다. 나와 청풍은 대역 죄인이 된 기분으로 고개만 끄덕였다.

“난 청렴하진 않지만 신의를 저버릴 만큼 비겁한 놈은 아니에요. 그랬다면 지금까지 전하를 모시지도 않았겠지.”

홍진이 흐릿한 시선으로 창밖을 응시했다.

“오래전 선황(先皇)을 곁에서 모셨었죠. 제게 상산왕 전하를 보필하라는 명을 내리셨어요.”

“선황께서요?”

죽은 전대 황제가 그런 부탁을 했을 정도라면 그때 역시 내관 중에서도 상당한 고위직이었다는 뜻이다.

고개를 끄덕인 홍진이 말을 이었다.

“변방으로 귀양 아닌 귀양을 왔지만…… 지금은 이 정도로 만족해요. 충분히.”

말과는 달리 눈동자에는 숨길 수 없는 빛이 스며들어 있다.

야망? 희망? 그것이 품은 의미를 알아차리기도 전에 빛은 사라졌고, 마부의 조용한 음성이 귓가를 파고들었다.

“태원진가가 보입니다.”
```

## Current accepted English baseline

```markdown
# Chapter 146

Every meeting must eventually end in a parting.

As the familiar six-horse carriage drew near, Zhu Bao held out something about the size of my palm.

“What is this?”

“My reward for today’s meeting.”

“Oh, you really didn’t have to…”

When I accepted it and examined it closely, I saw that it was a kind of golden medallion.

Clouds and a dragon had been delicately engraved into its surface, which flashed brilliantly in the sunlight.

*Ding.*

> **System**
>
> - The Quest target is extremely pleased with today’s meeting!
>
> - As a Quest Reward, obtained **Prince Shangshan’s Token**!

“It is my token. If there is anything else you desire or a wish you would like granted, bring this token and come find me. I shall fulfill it to the best of my ability.”

“Oh.”

A coupon for an exchange.

At a Chinese restaurant, twenty coupons would get you a large serving of sweet-and-sour pork. Since this was a coupon from Prince Shangshan, I might be able to exchange it for all kinds of elixirs or treasures.

*I do need a weapon, too.*

Thanks to absorbing the Blazing Flame Divine Pill, I had more than enough internal energy.

It was just a shame that I didn’t have a decent spear to use. As for the other weapons, I had used and discarded them from the start like disposable chopsticks.

*Should I just trade it in right now?*

I considered it for a moment, then shook my head.

The greatest dangers had already passed. Exchanging the prince’s token for a single weapon when there was no immediate need would be a waste.

“Thank you. I really wanted something like this.”

When I bowed deeply from the waist, Zhu Bao rose onto his tiptoes and gently ruffled my hair.

“I am happy that you like it.”

“……”

This felt really strange. I’d let it slide because he was cute.

In the meantime, the carriage that would take us home came to a stop. As I was about to climb aboard, Zhu Bao waved at me.

“Take care! Come again!”

*Next time, you should come to me, you little punk.*

There were only a little over two weeks left until New Year’s Day. I would probably be able to see the young prince again around then.

“Then, I shall take my leave.”

“I’ll return, Your Highness.”

The carriage was so large that its entrance was wide as well. Hong Jin and I climbed aboard side by side.

“……Hm?”

Wait a minute. That had been so natural that I’d almost let it pass.

I stared at Hong Jin in disbelief.

“What is it?”

“Hm? Why?”

“This carriage is going to the Jin Family of Taiyuan.”

“I know. That’s why I got on.”

“What?”

“You know what they say—strike while the iron is hot. Shouldn’t I take this opportunity to have a conversation with the Lesser Family Head Jin?”

Hong Jin smiled pleasantly and snapped his fingers. An official came running over like the wind.

“Deputy Military Commissioner. Do you have an order for me?”

“We’re visiting without an appointment, so we should bring plenty of gifts. Don’t forget to send a messenger ahead to offer them our respects.”

“I shall carry out your orders!”

Li Feng also issued an order to one of the officers under his command.

“He is an honored guest. Escort him to the Jin Family of Taiyuan.”

“Yes, sir!”

At the two men’s commands, nearly a hundred soldiers and a hastily assembled delegation began moving in perfect order.

Cheongpung, who had been about to climb aboard after us, gave a small round of applause at the sight.

“Wow.”

Having obtained the royal guard gear set he had longed for so desperately, he decided to stay at the Jin Family of Taiyuan for the time being.

Li Feng dipped his head toward me.

“I entrust Martial Uncle to you.”

“Of course.”

Even without hearing him say that, Cheongpung was someone I wanted to become friends with first.

If I used him as a bridge to strengthen the Jin Family of Taiyuan’s relationship with Huashan, our family’s future would surely be bright.

*He’s an interesting guy, too.*

Cheongpung waved with a sunny smile.

“Martial Nephew Li Feng, don’t worry about me! Interesting things keep happening whenever I’m with Young Master Jin!”

“Just in case, I’ll say this now. Don’t cause any trouble.”

“Yes!”

At least he was good at answering.

I turned toward the people who remained behind.

“What have you decided to do?”

The young prodigies of the Five Gates of Shanxi answered hesitantly.

“We plan to stay at Honghwa Inn until New Year’s Day.”

“It would be difficult to visit our families. There isn’t much time…”

“To be honest, we don’t even dare go back.”

“If I return now, my father might kill me.”

Their answers were as gloomy as could be.

Then again, rumors about what had happened the day before had probably already spread like wildfire, so their fear was understandable.

I clicked my tongue as I looked at them.

“Behave yourselves until New Year’s Day. I’ll smooth things over with the Sect Leaders later.”

“Are you really going to do that?”

“But in return, each of you needs to do your part. You know what I mean, right?”

“The Seongun Escort Bureau… Yes, sir. We understand.”

The tide could no longer be turned. By now, both these young men and the Sect Leaders of the Five Gates of Shanxi would know that.

All that remained was to grow as large as possible under the Jin Family of Taiyuan.

“All right, then. Do your best, and I’ll see you at New Year’s.”

“What?”

“Why? What is it?”

“W-we’re going the same way.”

“Where? To Honghwa Inn?”

“Yes.”

I tossed one final remark at the bewildered young men.

“This is an express carriage to the Jin Family of Taiyuan.”

*Bang!*

The carriage began moving almost as soon as the door slammed shut.

* * *

The inside had been spacious even with six people seated in it. Cheongpung, Hong Jin, and I each claimed several seats and leaned back against the soft cushions.

“I think I could live here.”

Cheongpung continued with a blissful smile.

“When I lived with Grandfather, I slept on grass or rocks. I don’t think I could live like that anymore.”

*He’s a primitive man discovering civilization.*

At his words, Hong Jin asked with curious eyes,

“Then have you always lived on Huashan, Young Master?”

“Yes. Ever since I was very young. But apparently I wasn’t born on Huashan. I asked Grandfather about it once, and he said I came to Huashan when I was three or four years old.”

That figured. No matter how great a master the Sword Saint was, even he had limits when it came to raising a child.

Reaching the Supreme Peak realm wouldn’t make milk come out of a man’s chest, after all.

“……”

*Actually, a Supreme Peak master might be able to do it.*

They were monsters who could use Sword Energy and Sword Force. Producing a little milk couldn’t be beyond them.

I imagined a white-haired old man nursing a newborn baby.

“Ugh.”

“Benefactor, are you all right?”

“Young Master Jin, are you all right?”

“I’m fine. I just felt a little nauseated.”

“Oh my, that won’t do. Here, lie down on my lap.”

“……”

*Maybe I should just smash his knee.*

When I hurled a silent double curse at him with my eyes, Hong Jin covered his mouth and laughed.

“Hoho. As expected, Young Master Jin is so much fun to tease.”

If a beautiful woman had said that, I would have laughed along with her. But Hong Jin was unmistakably a man. No amount of white powder on his face or lipstick on his lips could change that fact.

*He said he used to be a palace attendant.*

Didn’t that make him a eunuch?

I had heard once that not every eunuch was necessarily castrated. But there was no way to tell whether Hong Jin was equipped or not.

“Young Master Jin.”

“Yes, yes?”

“What are you looking at right now?”

“Ah, I thought there was something stuck there.”

*Damn it. He caught me.*

He wasn’t a Murim martial artist, but his ability to read the situation was on the level of a Supreme Peak master. I quickly pulled my gaze away from Hong Jin’s lower body and changed the subject.

“By the way, how did Great Hero Li Feng end up joining the military?”

“Assistant Military Commissioner Li? He passed the military examination, of course. After that, it was smooth sailing all the way.”

“As expected of a Huashan lay disciple.”

“I can’t say that had no influence, but it wasn’t only because of that. Becoming a Third-Rank Assistant Military Commissioner in only ten years is extremely difficult.”

“Third-Rank means…?”

“What is Third-Rank? Is it something you eat?”

I vaguely understood that it was a high position, but that was about it.

Seeing that Cheongpung and I had no idea what he was talking about, Hong Jin explained patiently.

“It’s a high office. There are only four such positions in each province, and in terms of rank, Assistant Military Commissioner Li is one of the top three in the military.”

Hong Jin counted them off on his fingers.

“The Military Commissioner, who is the commander in chief. Then me, directly beneath him. And third is Assistant Military Commissioner Li. Of course, His Highness Prince Shangshan stands above all of us.”

“The Military Commissioner?”

“He’s about to retire. He was born the son of a Grand General, accomplished a little, and has a tremendous fondness for bribes.”

*A corrupt military official. The kind whose petty corruption had become a way of life.*

With the commander in chief being that kind of person, it was easy to understand why security in Shanxi Province had been such a mess lately.

“The current Military Commissioner is incompetent. You only need to look at the mounted bandits roaming freely the moment the Mount Heng Sword Sect collapsed.”

“If he’s that incompetent, then why not just…”

I swallowed the rest of the sentence before it left my mouth.

*Why should I meddle in someone else’s workplace? Especially when they’re all high-ranking government officials.*

Seeing my reaction, Hong Jin kindly added an explanation.

“The Military Commissioner is appointed directly by the Emperor. His dismissal works the same way.”

“Oh.”

“Well, at least he has no ambitions beyond that. I like bribes too, so I’m hardly in a position to criticize him.”

*What kind of person was this?*

I had seen plenty of politicians on television who claimed to be innocent of all charges of accepting bribes, but Hong Jin was the first person I had met who admitted to liking them so openly.

“Why? Did I look that upright?”

“No. You did look like someone who would enjoy bribes, but…”

“But you didn’t expect me to say it so openly?”

“Something like that. To be honest, I’m a little flustered.”

“Young Master Jin. Do you know what?”

Hong Jin continued with a serious expression.

“I don’t have a thing.”

“What?”

“I’ve been castrated.”

“……”

*What the hell was I supposed to say to that?*

I had suspected as much, but I hadn’t expected him to suddenly drop a bomb like that.

Cheongpung, who had been looking out the window, abruptly joined in with a curious expression.

“What does ‘castrated’ mean?”

“……Please, please shut your mouth.”

*He said he doesn’t have his thing—his thing!*

Every second dragged by. Sweating coldly, I forced myself to speak.

“I’m sorry to hear that.”

“There’s no need to be sorry. Some people live without it, and some people live with it. Right?”

“Th—that’s right.”

His admirable attitude made me solemn for no reason.

Meanwhile, the mountain-dwelling primitive who didn’t know what a eunuch was kept chattering without the slightest sense of danger.

“Benefactor, could you please tell me what a eunuch is?”

*Even if I die, I’m not telling him. Never.*

Even if I explained it, there was a 99.99 percent chance he would say something like, *Wow, I’ve never met anyone without one before!*

But Hong Jin remained composed.

“It means a man doesn’t have his thing.”

“Wow, I’ve never met anyone who didn’t have—”

“Oh, shut up already!”

Cheongpung sucked in a startled breath.

“B-Benefactor.”

“Calm down, Young Master Jin. If he grew up in the mountains, it’s understandable. And besides, it’s not as if I’ve only been living as a eunuch for a day or two.”

“Still, that was too harsh.”

“Was I in the wrong? My sincerest apologies.”

“It’s fine. Chin up. It’s still attached.”

*Decades of experience as a eunuch hadn’t gone anywhere.*

Hong Jin waved his hand as if telling us to calm down, then continued as though nothing important had happened.

“I have never regretted the decision I made. When your own family is starving to death, what wouldn’t you do? Am I wrong?”

“Of course not.”

“I—I would have done the same!”

Whatever Hong Jin said now, we had to agree with him. Cheongpung and I could only nod, feeling like condemned criminals.

“I’m not an upright man, but I’m not cowardly enough to betray my loyalty. If I were, I wouldn’t have continued serving His Highness all this time.”

Hong Jin gazed out the window with hazy eyes.

“I served the late Emperor at his side long ago. He ordered me to assist His Highness Prince Shangshan.”

“The late Emperor?”

If the previous Emperor had entrusted Hong Jin with such a request, it meant he must have held a considerably high position among the palace eunuchs even back then.

Hong Jin nodded and continued.

“I came to the frontier in something like exile, but… I’m satisfied with things as they are now. More than satisfied.”

Despite his words, an unmistakable light shone in his eyes.

Ambition? Hope?

Before I could understand what that light meant, it disappeared, and the coachman’s quiet voice reached my ears.

“We can see the Jin Family of Taiyuan.”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 146`.

# Master Edit Task — Chapter 147

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
| 청풍     | **Cheongpung**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 큰형     | **eldest brother**                           |
| 은인     | **Benefactor**                               |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 사서삼경 | **Four Books and Three Classics** | Confucian texts used to describe conventional scholarly learning. |
| 금성전장 | **Golden Star Exchange** | Financial institution that issued the thousand-nyang bank draft. |
| 전표 | **bank draft** | Negotiable draft used for the thousand-silver-nyang payment. |
| 은자 | **silver nyang** | Silver currency unit. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 은원보 | **silver yuanbao** | Small silver ingot given to Taekyung as pocket money. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 성군 | **sage king** | Desired form of rulership proclaimed for Prince Shangshan. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 전령 | 진위경 | military messenger to Lesser Family Head | Lesser Family Head | formal-polite and deferential | Uses 소가주님 when confirming Wikyung's identity. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 진위경 | 홍진 | political_host_to_deputy_military_commissioner | Comrade Hong | formal-polite and playful | Jin Wikyung adopts Hong Jin's requested casual address, 홍 동지. |
| 홍진 | 진위경 | deputy_military_commissioner_to_lesser_family_head | Lesser Family Head Jin | formal and teasing | Hong Jin addresses Jin Wikyung as 진 소가주님 while flattering and joking with him. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 유생 | 진위경 | scholar_to_lesser_family_head | Lesser Family Head | formal-deferential | The scholar reports matters to Jin Wikyung and apologizes for his inadequate proposal. |
| 진위경 | 유생 | lesser_family_head_to_scholar | you | formal-but-familiar | Jin Wikyung uses 자네 while correcting and instructing the inexperienced scholar. |
| 위팽 | 유생 | senior_retainer_to_scholar | you | familiar and probing | Wipeng uses 자네 while asking the scholar for his assessment. |
| 위팽 | 청풍 | Jin Family retainer to visiting Huashan martial artist | Young Hero Cheongpung | formal-polite and worried | Uses 청 소협 while warning that Cheongpung's refusal of the Sect Leader's order could strain relations between the Jin Family and Huashan. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 큰형 | kinship | Eldest older brother, not a generic older brother. | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
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

#### Chapter 145 tail (verified mastered)

…
cuter he gets.* I reached out to pat my little fanboy—no, Prince Shangshan Zhu Bao—on the head, only to lower my hand when I saw Li Feng’s expression. *Oh, right. He’s a king. And a member of the imperial family, at that.* “Ahem. I have urgent business to attend to.” “Can you not put it off?” “I’m sorry, but every moment counts.” “I see…” Looking at the dejected kid’s face made me feel a little guilty—like hell it did. I wanted to hurry back home to my family and get some proper rest. Right on cue, Hong Jin cut in with his delicate voice. “Your Highness, you have me, so please let Young Master Jin go now. All right?” But Zhu Bao merely stared at me, his expression stubborn. “Then when shall I be able to see you again?” “Hmm, I don’t know. After a thousand nights?” “A thousand nights!” Zhu Bao cried out in shock. That was approximately three years. For a child who was only ten years old, it must have seemed like an enormous amount of time. “A-Are you truly that busy?” “There are such things as adult matters, Your Highness.” “Good heavens. Even my late father was never that busy…” He looked utterly crushed. Zhu Bao’s head drooped, only to shoot back up at Li Feng’s next words. “Your Highness, how about this?” “What do you mean?” “I hear the Jin Family of Taiyuan will be holding a grand banquet in fifteen days. Why not visit the Jin Family of Taiyuan in person?” “The Jin Family of Taiyuan?” “Yes. All the renowned masters of Shanxi will be gathered there, so I’m sure you’ll be pleased.” Zhu Bao’s eyes sparkled. “Of course! Why didn’t I think of that?” “Yes, Your Highness.” “……” What the hell were these two talking about? They hadn’t even been invited, yet here they were letting their imaginations run wild. But if I told him not to come, it felt as though something would explode, so all I could do was nod. “Great Hero Li is right. Come visit us then.” “Would that really be all right?” A little late to ask, wasn’t it? I put on my best customer-service smile. “Of course. My brothers will be happy to see you too.” “I-Is that really true?” “You know who my brothers are, don’t you? You’ve already met my second brother.” “The Heaven Shaking Sword?” A dark cloud suddenly fell over Zhu Bao’s bright, innocent face. “Your second brother dislikes me. Three years ago, he only ate and left without saying a word. He was even rude.” “He didn’t say a single word?” “I do not wish to speak of that day anymore.” Hong Jin whispered in a tiny voice, “His Highness asked him for an autograph, but he flatly refused.” Jin Mukyung had been invited three years ago, which meant… Zhu Bao had been seven at the time. Good grief. How could anyone flatly refuse a seven-year-old asking for an autograph—especially when that seven-year-old was a king? *That man really is something else.* In a way, it was very Jin Mukyung. Recalling how his fanboy enthusiasm had been so brutally crushed, Zhu Bao silently fidgeted with his fingers. Watching him, I felt a pang of sympathy. “If you come this time, I’ll ask him to give you his autograph.” “Really?” “Pinky promise. Seal it.” I hooked pinkies with the bewildered boy and even stamped our thumbs together. “What is this?” “It means I swear before the gods of heaven and earth. Something like that.” “Oh!” Everyone around us was making a fuss because he was royalty, because he was a king, and so on. But a child was still a child. Everyone smiled fondly at the sight of Zhu Bao beside himself with delight. “It’s been a long time since I’ve seen His Highness this happy.” “I know. After dealing with this boring Assistant Military Commissioner every day, he’s smiling brightly for the first time in ages.” “I’ve done nothing but my best.” “Doing your best doesn’t always produce the best results. It happens.” “Deputy Military Commissioner!” “What is it, Assistant Military Commissioner?” Li Feng and Hong Jin. I could never tell whether the two of them got along or hated each other as they bickered back and forth. Meanwhile, Cheongpung approached Zhu Bao with anticipation written all over his face. “I-I could give you an autograph too?” “……” “You’ve never given anyone an autograph before, have you?” “Gasp. How did you know? I’ve left my hand mark as a porter on the way here, but this is my first autograph.” “Wouldn’t it be strange if I didn’t know?” Just look at that expectant face. He was dying to give someone his first-ever autograph. “C-Can’t I give him one?” “Sure. Do whatever you want. His Highness will probably be pleased.” But Zhu Bao’s reaction was unexpected. “An autograph? From you?” “Yes! I really want to give you my autograph!” “No.” “W-Why not? They say my grandfather is very famous. Haven’t you heard of the Sword Saint?” “I know. Of course I know. But…” Zhu Bao put on a deliberately stern expression and shook his head. “You don’t have a martial title yet, do you?” “Excuse me?” “Come back after you’ve acquired a cool martial title. Then I shall certainly get your autograph.” “……” “……” *So this was something only named characters could do.*

#### Chapter 146 tail (verified mastered)

…
He passed the military examination, of course. After that, it was smooth sailing all the way.” “As expected of a Huashan lay disciple.” “I can’t say that had no influence, but that wasn’t the only reason. Becoming a Third-Rank Assistant Military Commissioner in only ten years is extremely difficult.” “Third-Rank means…?” “What’s Third-Rank? Is it something you eat?” I vaguely understood that it was a high position, but that was about it. Seeing that Cheongpung and I had no idea what he was talking about, Hong Jin explained patiently. “It’s a high office. There are only four such positions in each province, and Assistant Military Commissioner Li is among the top three in the military hierarchy.” Hong Jin counted them off on his fingers. “First is the Military Commissioner, the commander in chief. Then me, directly beneath him. And third is Assistant Military Commissioner Li. Of course, His Highness Prince Shangshan stands above us all.” “The Military Commissioner?” “He’ll be retiring soon. He was born the son of a Grand General, accomplished a little, and has a tremendous fondness for bribes.” *A corrupt military official. The kind whose petty corruption had become a way of life.* With the commander in chief being that kind of man, it was easy to understand why security in Shanxi Province had been such a mess lately. “The current Military Commissioner is incompetent. You only need to look at the mounted bandits roaming freely the moment the Mount Heng Sword Sect collapsed.” “If he’s that incompetent, why not just…” I swallowed the rest of the sentence before it left my mouth. *Who was I to meddle in someone else’s workplace? Especially when they were all high-ranking government officials.* Seeing my reaction, Hong Jin kindly added an explanation. “The Military Commissioner is appointed directly by the Emperor. The same goes for dismissing him.” “Oh.” “Well, at least he has no ambitions beyond that. I like bribes too, so I’m hardly in a position to criticize him.” *What kind of person was this?* I’d seen plenty of politicians on television proclaiming their innocence against accusations of accepting bribes, but Hong Jin was the first person I’d met who openly admitted to liking them. “Why? Did I look that upright?” “No. You did look like someone who would enjoy bribes, but…” “But you didn’t expect me to say it so openly?” “Well, yes. Honestly, I’m a little flustered.” “Young Master Jin. Do you know what?” Hong Jin continued with a serious expression. “I don’t have a thing.” “What?” “I’m a eunuch.” “……” *What the hell was I supposed to say to that?* I’d suspected as much, but I hadn’t expected him to drop a bomb like that out of nowhere. Cheongpung, who had been looking out the window, abruptly joined in with a curious expression. “What’s a eunuch?” “……Please, please shut your mouth.” *He’s saying he doesn’t have his thing—his thing!* Every second dragged by. Sweating coldly, I forced myself to speak. “I’m sorry to hear that.” “There’s no need to be sorry. Some people live without one, and some live with one. Right?” “Th—that’s right.” His admirable attitude made me solemn for no reason. Meanwhile, the mountain-dwelling primitive who didn’t know what a eunuch was kept chattering without the slightest hint of tact. “Benefactor, could you please tell me what a eunuch is?” *Even if I die, I’m not telling him. Never.* Even if I explained it, there was a 99.99 percent chance he would say something like, *Wow, I’ve never met anyone without a dick before!* But Hong Jin remained composed. “A eunuch doesn’t have a dick.” “Wow, I’ve never met anyone without—” “Oh, shut up already!” Cheongpung sucked in a startled breath. “B-Benefactor.” “Calm down, Young Master Jin. If he grew up in the mountains, it’s understandable. And besides, it’s not as if I’ve only been living as a eunuch for a day or two.” “Still, that was too harsh.” “Was I in the wrong? I’m truly sorry.” “It’s fine. Chin up. Yours is still attached.” *Decades of experience as a eunuch hadn’t gone anywhere.* Hong Jin waved a hand as if to calm us down, then continued as though nothing important had happened. “I’ve never regretted my decision. When your own family is starving to death, what wouldn’t you do? Am I wrong?” “Of course not.” “I—I would have done the same!” Whatever Hong Jin said now, we had to agree with him. Cheongpung and I could only nod, feeling like condemned criminals. “I’m not an upright man, but I’m not cowardly enough to betray a trust. If I were, I wouldn’t have continued serving His Highness all this time.” Hong Jin gazed out the window with hazy eyes. “Long ago, I served at the late Emperor’s side. He ordered me to assist His Highness Prince Shangshan.” “The late Emperor?” If the previous Emperor had entrusted Hong Jin with such a request, Hong Jin must have held a considerably high position among the palace attendants even back then. Hong Jin nodded and continued. “I came to the frontier in what was practically exile, but… I’m satisfied with things as they are now. Truly, this is enough.” Despite his words, an unmistakable light shone in his eyes. Ambition? Hope? Before I could understand what that light meant, it disappeared, and the coachman’s quiet voice reached my ears. “The Jin Family of Taiyuan is in sight.”

## Korean source

```text
＃147화



진위경은 깊은 탄식을 내뱉었다.

“가문에 돌아오자마자 일을 해야 한다니.”

“며칠 동안 자리를 비우지 않으셨습니까.”

“그거야 피치 못할 사정 때문이지!”

“지금처럼 화내신다고 일이 줄어들지는 않죠.”

“위팽, 나 좀 살려 주게. 이러다가는 정말 과로로 죽고 말걸세.”

간절하고 애처로운 간청에도 위팽은 냉정하게 대답했다.

“일은 끝내고 죽으십쇼. 장례는 성대하게 치러 드리겠습니다.”

“……악귀가 따로 없군. 자네 정말 사람 맞나?”

이미 반나절 앞서 태원진가로 복귀한 진위경을 기다리는 건 산더미처럼 쌓인 일거리였다.

장장 열흘가량이나 자리를 비운 탓에 서탁 위는 물론이고 바닥까지 수백 개의 죽간이 늘어져 있었다.

“이걸 혼자 어떻게 해!”

“하실 수 있습니다. 지금까지 잘하셔 놓고 뭘 새삼스럽게.”

“본가에 이 정도로 사람이 없나? 아니지, 산서성에 기재가 이 정도로 없어?”

“사람 보는 눈을 좀 낮춰야겠다는 생각은 안 하십니까?”

“내 문제라는 말인가?”

“벌써 십여 명이 다녀갔습니다. 제 눈에는 다들 괜찮은 유생(儒生)들이었는데 고작 두 명만 뽑으신 게 실수하신 겁니다.”

“괜찮은 유생은 무슨. 자넨 눈도 없나?”

학문을 익혔다고 무조건 받아들일 수는 없었다.

태원진가는 엄연한 무림 문파. 사서삼경(四書三經)을 얼마나 많이 외웠느냐, 어느 석학의 문하에서 뭘 배웠느냐는 중요하지 않다.

진위경이 원한 인재는 유연한 사고방식을 지닌 실용주의자지 공자 왈, 맹자 왈을 입에 달고 사는 뻣뻣한 유생이 아니다.

“그들 중 두 사람이 유일하게 쓸 만한 자들이었네.”

지금도 그 선택을 후회하지 않는다. 그의 단호한 대답에 위팽이 귀를 후볐다.

“아, 그렇습니까? 그래서 그 두 사람, 지금 어디서 뭘 하고 있습니까?”

“……그, 그건.”

순간 말문이 막힌 진위경을 대신해 위팽이 말을 이었다.

“나흘 동안 꼬박 철야 근무하고 도망쳤잖습니까.”

“도, 도망치긴 누가 도망쳤다고 그러는 건가! 한 명은 어머니가 위독하셔서…….”

“제가 그 친구 사라지고 나서 한번 알아봤습니다. 어머니는 십 년 전에 돌아가셨던데요.”

“……그래?”

“다른 한 명은 잠시 측간에 간다더니 그 길로 내뺐고요. 제 말이 틀립니까?”

“크험, 크허험!”

“주군께서야 무공을 익히셨으니 며칠 밤을 새워도 멀쩡하시겠지만, 그 친구들은 아닙니다. 평생 심법 구결 한 줄 읽어 본 적 없는 양민들이라고요.”

“아, 알고 있네. 그래서 보수를 후하게 챙겨 주잖나.”

“보름만 더 있었으면 그 은자가 유족에게 갔겠죠.”

“…….”

“더 할 말 있으십니까?”

“……없네.”

“없으시면 이제 일 시작하십시오. 다음부터 찾아오는 유생들은 쓸 만하다 싶으면 다 받아들이시고요.”

우울한 얼굴로 고개를 끄덕인 진위경이 죽간 하나를 집어 든 그 순간이었다.

집무실 밖에서 대기 중이던 호위대의 무인 하나가 조심스럽게 들어와 예상치 못한 소식 하나를 전했다.

“누구라고?”

진위경의 물음에 위팽이 대답했다.

“산서성 도지휘동지가 보낸 전령이랍니다.”

“그건 나도 들었네. 한데 도지휘동지라면…… 상산왕의 최측근이자 실세라는 그자?”

“예. 내관 주제에 군부 고위직을 꿰찼다고 말이 많았었죠.”

“그래, 그랬었지.”

진위경 역시 들어 본 기억이 있다. 군부의 꼭대기에 앉아 혼자서 어린 왕을 쥐락펴락한다는 내관에 관한 소문을.

“일면식도 없는데 갑자기 무슨 일일까요?”

“무슨 일이겠나?”

“설마 삼공자 때문에?”

“정황상 그럴 가능성이 매우 농후하지. 우선 전령을 안으로 들이게.”

“예.”

“아, 혹시 모르니 무경이도 부르고.”

“알겠습니다.”

위팽이 수하를 향해 고개를 끄덕인 지 얼마 되지 않아 한 사람이 집무실 안으로 들어섰다.

각을 잰 듯 절도 있는 행동에 가벼운 갑옷 차림.

척 봐도 군 소속으로 짐작되는 그가 바로 홍진이 보낸 전령이었다.

“태원진가의 소가주님 되십니까?”

진위경이 고개를 끄덕였다.

“내가 진 모요. 피차 번잡스러운 서론은 접어 둡시다, 어쩐 일로 오셨소?”

“도지휘동지의 말씀을 전하러 왔습니다.”

“혹, 내 아우와 연관된 일이오?”

“예. 지금 함께 이곳으로 오고 계십니다.”

“함께?”

“그렇습니다. 반 시진 후면 도착하실 겁니다.”

진위경은 그 말을 들으며 가만히 턱을 쓰다듬었다.

사실상 산서성의 이인자 격인 홍진이다. 아무런 이유 없이 움직일 인물은 아니었다.

지금까지 아무런 접점도 없었던 그가 달랑 서신만 보낸 것이라 해도 뜻밖일 터인데, 심지어 직접 오고 있다고 하니 당혹스러울 수밖에.

“선약을 잡은 기억은 없소만.”

위팽이 냉기가 뚝뚝 흐르는 표정으로 한마디를 보탰다.

“도지휘동지가 제아무리 나랏일을 하는 고관(高官)이라고는 하나, 이건 명백히 본가를 무시하는 처사요. 알고 있소?”

“그, 그것이…….”

전령의 이마에 땀방울이 맺혔다.

그도 미약하게나마 군문의 무공을 익힌 몸. 귀검이라 불리는 절정 고수의 눈빛에 가슴이 철렁 내려앉을 수밖에 없었다.

“어떤 용무로 오는 것이오?”

“저, 저는 그저 말씀을 전하라는 명을…….”

“아주 상전이 따로 없군.”

좌불안석이 된 전령을 구원해 준 것은 진위경이었다.

“위팽, 그만하게. 그래서 도지휘동지께서 정확히 뭐라 하시었소?”

“도지휘동지께선 갑작스러운 무례에 미리 사죄의 말씀을 전하라 하셨습니다. 그리고…….”

전령이 품에서 원통 하나를 꺼내 진위경에게 건넸다. 어른 손바닥만 한 원통 안에는 돌돌 말린 하얀 종이가 들어 있었다.

“이게 뭐요?”

“소인도 들은 바가 없습니다. 그저 전해 드리면 알 거라고 하시더군요.”

“흠.”

짐짓 눈살을 찌푸린 진위경이 종이를 펼친 그때, 집무실 문이 열리고 두 번째 손님이 들어왔다.

“부르셨습니까?”

“…….”

“형님?”

한동안 말없이 손에 들린 종이를 바라보던 진위경이 고개를 들었다.

“왔느냐?”

“예. 수련 중에 저를 찾으신다는 말을 듣고…… 한데 어쩐 일로 부르신 겁니까?”

“귀빈이 오기로 해서 말이다. 마중 나갈 채비를 해야겠구나.”

“귀빈, 말입니까?”

“주군. 귀빈이라니요? 마중까지 나갈 필요 있습니까?”

위팽이 인상을 찡그리며 반박했다.

“언질도 없이 오는데 무슨 귀빈입니까? 불청객이지.”

코앞에 전령이 있음에도 거침이 없다. 지금의 태원진가가 산서성에서 차지하는 위치를 생각해 보면 결코 틀린 말은 아니다.

그러나 진위경은 조용히 종이를 건넸다.

“이거 보고 다시 얘기하게.”

“이게 뭡니까?”

“백문이 불여일견.”

“그냥 시원하게 말씀해 주시면 되지 꼭…….”

위팽의 목소리가 점점 줄어들더니 이내 뚝 끊겼다. 눈동자가 쉴 새 없이 움직이며 떨렸다.

종이를 뚫어져라 바라보던 그의 입술이 열린 것은 잠시 후였다.

“귀빈께서 오시는군요.”

“그렇지?”

“예. 맞습니다.”

두 사람의 시선이 아직도 영문을 모르고 멀거니 서 있는 진무경에게로 향했다.

“무경아.”

“이공자.”

“예?”

“너 수련하다가 왔다고 했지.”

“땀 냄새 납니다.”

“수련할 때 땀나는 거야 당연한 거 아닙니까.”

“씻고 와라.”

“당장 씻으십쇼.”

이유를 알 수 없는 두 사람의 반응에 진무경이 답답한 얼굴로 물었다.

“도대체 누가 오기에 이러시는 겁니까?”

진위경과 위팽이 동시에 대답했다.

“큰손.”

“그것도 아주 큰손이죠.”

위팽이 손에 들린 종이를 흔들었다. 그건 천하 어디에서나 사용할 수 있다는 금성전장에서 발행한 천 냥짜리 전표였다.

“이거, 그냥 천 냥 아니다. 은자 천 냥이야.”

은자 천 냥이면 철전으로는 십만 냥이다. 안 그래도 사방에 돈을 퍼붓고 있는 태원진가에게는 가뭄의 단비 같은 거금이었다.

진위경은 실로 오랜만에 둘째 동생에게 정색했다.

“무경아, 이제 씻자.”

“…….”



* * *



마차에서 내리자마자 저절로 한마디가 튀어나왔다.

“와, 시벌…….”

욕을 안 하려야 안 할 수가 없다. 높이 솟은 담벼락 위, 펄럭거리는 천에는 대문짝만한 글씨로 이렇게 쓰여 있었다.



도지휘동지 태원진가 오신 날



부처님 오신 날도 아니고 이게 뭐야.

쪽팔림에 차마 고개를 들지 못하고 있는데, 뒤따라 내린 홍진이 배를 잡고 깔깔 웃었다.

“이야, 생각 이상이네.”

“혹시 저희 큰형님이랑 불알친구라도 됩니까? 도대체 어떻게 하면 이렇게까지 극진한 환대를…….”

“진 공자, 난 불알이 없어요.”

“앗, 아아. 죄송합니다. 정말 죄송합니다.”

엄청난 실수다. 스틱도 없는데 유정란이 남아 있을 리가 있나.

죄책감에 몸부림치는 나를 청풍이 다가와 위로해 주었다.

“은인, 저희 할아버지가 그러셨는데, 눈치 없는 사람은 주위에 친구가 없대요. 하지만 걱정 말아요. 내가 은인의 불알친구가 되어 줄 테니.”

“…….”

필요 없어, 이 새끼야.

애써 욕을 삼키는 내게 홍진이 말했다.

“진 공자, 사람 사이의 관계를 끈끈하게 만들어 주는 게 뭔지 알아요? 바로 재물이야. 금은보화면 귀신도 부린다는데, 산 사람은 오죽하겠어, 안 그래?”

“그럼?”

“선물 준다고 했잖아요. 일종의 뇌물이지 뭐.”

돈이면 귀신도 부린다, 라.

나 역시 어느 정도 동의하는 말이긴 한데 그 대상이 진위경이라는 게 거슬린다.

이미 마음속 깊숙한 곳에서 형이라고 생각하는 그를 뇌물에 넘어간 속물처럼 표현하는 홍진이 곱게 보이지 않는 것이다.

그런 기색이 내 표정에서도 드러나 버렸는지 홍진이 웃음 띤 얼굴로 말했다.

“내 말이 너무 심했나? 하지만 그건 당연한 거예요. 재물 싫어하는 사람이 어디 있겠어?”

“그래도 우리 큰형님입니다. 고작 은자 몇 푼으로 태원진가의 소가주를 구워삶았다고 생각하진 마세요.”

“진 공자…….”

낮은 목소리에 홍진이 눈을 크게 떴다.

“은자 몇 푼이라니. 천 냥이나 줬어.”

“그깟 은자…… 얼마요?”

“은자 천 냥. 철전으로는 십만 냥.”

이제 나도 대충 무림의 물가와 화폐에 대해 감을 잡았다.

특급 호텔이라 할 수 있는 봉황객잔의 별채는 하룻밤에 은자 오십 냥, 양민 네 식구의 일 년 생활비 두 배에 가깝다고 했다.

‘현대 금액으로 따지면 수천만 원.’

은자 천 냥이면 거기서도 20배다. 그러니까 홍진은 수억 원의 돈을 한 번에 툭 던져 준 거다.

“많……네요?”

“많이 줬지. 이번엔 나도 힘 좀 쓴 거야.”

“아니, 그래도 너무 많이 주셨는데.”

“앞으로의 관계를 위해서지. 그리고 지금 태원진가, 지금은 재물이 모이는 것보다 빠지는 게 더 많을걸? 전쟁에서 이기고 적의 영토를 점령한다고 끝나는 게 아니거든.”

“아, 예.”

“이럴 때 주는 도움이 진짜 크게 느껴지는 거지. 나도 뇌물 많이 주고받다 보니까 알게 되더라고. 아, 물론…….”

홍진이 눈을 찡긋하며 말을 이었다.

“진 공자가 아주 마음에 들어서 좀 더 쓴 것도 있고. 내 마음 알지?”

말이 끝나기가 무섭게 엉덩이에서 느껴지는 딱딱한 이물감.

쿡쿡 찔러 오는 감촉에 정신이 번쩍 든다.

‘아니, 이 새끼가 설마?’

맹세컨대 지금까지의 모든 인생을 통틀어 가장 소름 돋는 순간이다.

‘그래, 너 죽고 나 죽자. 전쟁 한 번 더 하자!’

번개 같은 속도로 돌아선 내 눈에 들어온 건 손바닥 절반만 한 크기의 은덩이였다. 저걸 뭐라고 하더라? 은원보?

“자, 이건 내가 주는 용돈.”

아, 맞다. 얘 고자였지.

나는 펄떡거리는 가슴을 진정시키며 대답했다.

“가, 감사합니다.”

“응. 빙당호로 사 먹어요.”

“은인, 사 먹을 때 저도 같이 데려가 주면 안 돼요?”

청풍이 입맛을 다시며 끼어든 그때, 등 뒤에서 익숙한 목소리가 울렸다.

“허허, 숙수들에게 따로 말해 놓을 테니 얼마든지 말만 하시오. 안 그런가, 위팽?”

“빙당호로의 산을 쌓아 놓겠습니다.”

“저놈은 누굽니까? 빙당호로라니, 어린 애도 아니고 무슨.”

누구인지 보지 않아도 알 수 있다. 반가운 웃음과 함께 돌아선 나는 말문이 막히는 장면을 발견했다.

펄럭, 펄럭.

활짝 웃고 있는 진위경과 위팽. 그리고 얼굴이 벌겋게 달아오른 진무경.

세 사람의 손에는 언제 만들었는지 모를 자그마한 천 쪼가리가 바람에 펄럭이고 있었다.



대국 만세! 황상 폐하 만세!

상산왕 전하, 성군이 되시옵소서!



“…….”

“…….”

내가 아까 홍진에게 뭐라고 했더라?

고작 은자 몇 푼으로 대 태원진가의 소가주를 구워삶았다고 생각하지 말라고 했나?

‘시벌, 구워삶기는 개뿔.’

이 정도면 탔다, 탔어.
```

## Current accepted English baseline

```markdown
# Chapter 147

Jin Wikyung let out a deep sigh.

“I have to start working the moment I return to the family.”

“Were you not away for several days?”

“That was due to circumstances beyond my control!”

“Getting angry like this won’t make the work disappear.”

“Wipeng, save me. At this rate, I’m really going to die of overwork.”

Despite his desperate, pitiful plea, Wipeng answered coldly.

“Finish your work before you die. I’ll give you a grand funeral.”

“……You’re a demon. Are you really human?”

What awaited Jin Wikyung, who had returned to the Jin Family of Taiyuan half a day earlier, was a mountain of work.

Because he had been away for nearly ten days, hundreds of bamboo slips were scattered across not only the writing desk but also the floor.

“How am I supposed to do all this alone?”

“You can do it. You’ve done fine until now, so why are you making such a fuss?”

“Does our family really have so few people? No—are there really so few capable people in all of Shanxi Province?”

“Have you ever considered lowering your standards when it comes to people?”

“Are you saying this is my fault?”

“More than ten people have come and gone already. They all looked like decent scholars to me, but you made the mistake of choosing only two.”

“Decent scholars? Please. Do you have no eye for people?”

They couldn’t simply accept anyone who had studied.

The Jin Family of Taiyuan was, after all, a Murim sect. How much of the Four Books and Three Classics someone had memorized, or what they had learned from which great scholar, wasn’t important.

The kind of talent Jin Wikyung wanted was a practical-minded person with flexible thinking—not a rigid scholar who went around constantly quoting Confucius and Mencius.

“Those two were the only ones among them who were worth using.”

He still didn’t regret that choice. At his firm answer, Wipeng picked at his ear.

“Oh, really? And where are those two now? What are they doing?”

“……Well, that’s…”

When Jin Wikyung was momentarily at a loss for words, Wipeng continued in his place.

“They worked through four straight nights and then ran away.”

“W-who ran away? What are you talking about? One of them had a mother who was gravely ill…”

“I looked into it after that fellow disappeared. His mother died ten years ago.”

“……Really?”

“The other one said he was going to the latrine, then slipped away and never came back. Am I wrong?”

“Cough. Cough-cough!”

“My lord, you’ve trained in martial arts, so you can stay up for several nights and remain perfectly fine. But those men are different. They’re commoners who have never read a single line of a cultivation technique formula in their entire lives.”

“Ah, I know that. That’s why I’m paying them generously.”

“If they had stayed another fifteen days, that silver would have gone to their survivors.”

“……”

“Do you have anything else to say?”

“……No.”

“If you have nothing else to say, start working. From now on, accept any scholars who seem useful when they come looking for work.”

Jin Wikyung nodded gloomily and reached for a bamboo slip.

That was when one of the martial artists from the guard detail waiting outside the office cautiously entered and delivered an unexpected report.

“Who did you say?”

In response to Jin Wikyung’s question, Wipeng answered.

“A messenger sent by the Deputy Military Commissioner of Shanxi Province.”

“I heard that much. But the Deputy Military Commissioner is… that man who’s supposedly Prince Shangshan’s closest aide and the real power behind him?”

“Yes. There used to be plenty of talk about how a palace attendant had managed to secure a high-ranking military post.”

“Right. I remember hearing that.”

Jin Wikyung had heard the rumors about the palace attendant who sat at the top of the military hierarchy and single-handedly kept the young prince under his thumb.

“We’ve never even met him. What could he want all of a sudden?”

“What do you think?”

“Could it be because of the Third Young Master?”

“Given the circumstances, that’s highly likely. Bring the messenger inside first.”

“Yes.”

“Ah, and just in case, call Mukyung as well.”

“Understood.”

Not long after Wipeng nodded to one of his subordinates, a man entered the office.

He moved with measured precision and wore light armor.

Anyone could tell at a glance that he belonged to the military. He was the messenger Hong Jin had sent.

“Are you the Lesser Family Head of the Jin Family of Taiyuan?”

Jin Wikyung nodded.

“I am Jin Wikyung. Let’s skip the tedious formalities between us. What brings you here?”

“I have come to convey the Deputy Military Commissioner’s words.”

“Is this related to my younger brother?”

“Yes. He is on his way here now, together with the Deputy Military Commissioner.”

“Together?”

“Yes. They should arrive in half a shichen.”

Jin Wikyung silently stroked his chin as he listened.

Hong Jin was effectively the second-most powerful man in Shanxi Province. He wasn’t the sort of person who moved without a reason.

It would have been surprising enough if someone who had never had any connection with them sent nothing but a letter. The fact that he was coming in person made the situation all the more bewildering.

“I don’t recall making an appointment.”

Wipeng added a remark with a face dripping with frost.

“No matter how high-ranking an official the Deputy Military Commissioner is, this is clearly an insult to our family. Are you aware of that?”

“Th-that…”

Sweat gathered on the messenger’s forehead.

He had trained in military martial arts, however slightly. When faced with the gaze of the Peak master known as the Ghost Sword, his heart couldn’t help but sink.

“What business does he have here?”

“I-I was only ordered to deliver his message…”

“He certainly knows how to pull rank.”

The messenger, who had become so nervous he could hardly sit still, was rescued by Jin Wikyung.

“Wipeng, that’s enough. So what exactly did the Deputy Military Commissioner say?”

“He told me to convey his apologies in advance for his sudden rudeness. And…”

The messenger pulled a small cylinder from inside his robes and handed it to Jin Wikyung. Inside the cylinder, which was about the size of an adult’s palm, was a rolled-up sheet of white paper.

“What is this?”

“I haven’t heard anything myself. He merely said that you would understand once it was delivered.”

“Hmm.”

Jin Wikyung deliberately furrowed his brow and unfolded the paper.

At that moment, the office door opened, and a second guest entered.

“Did you call for me?”

“……”

“Older brother?”

Jin Wikyung stared silently at the paper in his hand for a while before raising his head.

“You’re here.”

“Yes. I heard you were looking for me while I was training… What did you call me for?”

“We have an honored guest coming. We need to prepare to go out and greet him.”

“An honored guest?”

“My lord, what do you mean, an honored guest? Do we really need to go out and greet him?”

Wipeng frowned and objected.

“He’s coming without even giving us notice. What kind of honored guest is that? He’s an uninvited guest.”

He showed no restraint despite the messenger standing right in front of him. Considering the position the Jin Family of Taiyuan currently held in Shanxi, it wasn’t an entirely wrong thing to say.

Jin Wikyung quietly handed him the paper.

“Look at this, then we’ll talk again.”

“What is it?”

“Seeing is believing.”

“You could simply tell me instead of making such a fuss…”

Wipeng’s voice gradually grew quieter before cutting off completely. His eyes trembled as they darted back and forth.

A moment later, his lips parted.

“An honored guest is coming.”

“Right?”

“Yes. Exactly.”

The two men turned their gazes toward Jin Mukyung, who was still standing there with no idea what was going on.

“Mukyung.”

“Second Young Master.”

“Yes?”

“You said you came straight from training, right?”

“You smell like sweat.”

“It’s only natural to sweat when you train.”

“Go wash.”

“Wash immediately.”

Unable to understand the reason for their reactions, Jin Mukyung asked with a frustrated expression,

“Who on earth is coming to make you act like this?”

Jin Wikyung and Wipeng answered at the same time.

“A big spender.”

“And an extremely big one at that.”

Wipeng waved the paper in his hand. It was a thousand-nyang bank draft issued by the Golden Star Exchange, valid anywhere under heaven.

“This isn’t just a thousand nyang. It’s a thousand nyang of silver.”

A thousand silver nyang was worth one hundred thousand nyang in iron coins. To the Jin Family of Taiyuan, which was already pouring money out in every direction, it was a fortune like rain after a drought.

For the first time in a long while, Jin Wikyung gave his younger brother a stern look.

“Mukyung, let’s go wash up.”

“……”

* * *

The moment I got out of the carriage, a word slipped out on its own.

“Wow, fuck…”

There was no way I could stop myself from swearing. Atop the towering wall, a fluttering cloth banner displayed enormous letters that read:

**The Day the Deputy Military Commissioner Came to the Jin Family of Taiyuan**

*This isn’t even Buddha’s Birthday. What the hell is this?*

I was too embarrassed to lift my head when Hong Jin climbed down behind me and burst out laughing, clutching his stomach.

“Wow. This is beyond what I expected.”

“Are you perhaps childhood friends with my eldest brother? How else could he give you such an enthusiastic welcome…?”

“Young Master Jin, I don’t have balls.”

“Ah—oh. I’m sorry. I’m really sorry.”

That was a tremendous blunder. Without a stick, there was no way any fertilized eggs would be left behind.

As I writhed under the weight of my guilt, Cheongpung approached and comforted me.

“Benefactor, my grandfather used to say that people who don’t know how to read the room have no friends around them. But don’t worry. I’ll be your ball friend.”

“……”

*I don’t need one, you bastard.*

As I desperately swallowed my curses, Hong Jin spoke to me.

“Young Master Jin, do you know what makes relationships between people strong? Wealth. They say gold and silver can make even ghosts work for you. Living people should be even easier, don’t you think?”

“And?”

“I told you I’d give him a present. It’s basically a bribe.”

*Money can make even ghosts work for you.*

I agreed with that to some extent, but I didn’t like the fact that the person in question was Jin Wikyung.

I already thought of him as my older brother deep down. I didn’t appreciate Hong Jin making him out to be some materialistic opportunist who could be bought with a bribe.

Perhaps that displeasure showed on my face, because Hong Jin smiled and said,

“Was that too harsh? But it’s only natural. Who doesn’t like wealth?”

“He’s still my eldest brother. Don’t think you’ve won over the Lesser Family Head of the Jin Family of Taiyuan with a measly few silver nyang.”

“Young Master Jin…”

Hong Jin’s eyes widened at my low voice.

“A few silver nyang? I gave him a thousand nyang.”

“Just a few silver… How much?”

“A thousand silver nyang. That’s one hundred thousand nyang in iron coins.”

I had finally gotten a rough sense of prices and currency in the Murim.

The private suite at the Phoenix Inn, which could be considered a luxury hotel, cost fifty silver nyang per night. That was said to be close to twice the annual living expenses of a family of four commoners.

*In modern currency, that would be tens of millions of won.*

A thousand silver nyang was twenty times that. In other words, Hong Jin had casually tossed around several hundred million won in one go.

“That’s… a lot, isn’t it?”

“A lot, yes. I put in some effort this time.”

“Still, that’s far too much.”

“It’s for the sake of our future relationship. And right now, the Jin Family of Taiyuan is probably losing money faster than it’s bringing money in. Winning a war and occupying the enemy’s territory isn’t the end of it.”

“Ah, yes.”

“The assistance you give at times like this feels much greater. I learned that after giving and receiving so many bribes myself. Ah, of course…”

Hong Jin continued with a wink.

“I did spend a little extra because I took a particular liking to Young Master Jin. You understand my feelings, right?”

The moment he finished speaking, I felt a hard foreign object against my butt.

The sensation poking me repeatedly snapped me fully awake.

*No way. Is this bastard seriously…?*

I swear, in my entire life, this was the most spine-chilling moment I had ever experienced.

*Fine, if you’re going down, I’m going down too. Let’s have another war!*

I spun around at lightning speed.

What met my eyes was a silver lump about half the size of my palm. What did they call those again? A silver yuanbao?

“Here. Pocket money from me.”

*Oh, right. He was a eunuch.*

I calmed my pounding heart and answered.

“Th-thank you.”

“Sure. Go buy some candied hawthorn skewers.[^1]”

“Benefactor, could you take me with you when you go buy them?”

Cheongpung joined in, smacking his lips.

Just then, a familiar voice rang out from behind us.

“Heh heh. I’ll tell the cooks separately, so order as much as you like. Right, Wipeng?”

“We’ll build a mountain of candied hawthorn skewers.”

“Who is that fellow? Candied hawthorn skewers? He isn’t even a child, so what’s this about?”

I didn’t need to look to know who it was.

I turned around with a happy smile, only to find a scene that left me speechless.

*Flutter. Flutter.*

Jin Wikyung was smiling broadly. So was Wipeng. Jin Mukyung’s face was bright red.

In the hands of all three men, tiny scraps of cloth fluttered in the wind. I had no idea when they had made them.

> **Long live the Great Nation! Long live His Imperial Majesty the Emperor!**
>
> **His Highness Prince Shangshan, may you become a sage king!**

“……”

“……”

*What had I said to Hong Jin earlier?*

*Had I told him not to think he’d won over the Lesser Family Head of the mighty Jin Family of Taiyuan with a mere few silver nyang?*

*Fuck, “won him over” my ass.*

At this point, he was burned—burned to a crisp.

[^1]: Candied hawthorn skewers are a traditional snack of fruit coated in hardened sugar.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 147`.

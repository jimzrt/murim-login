# Master Edit Task — Chapter 375

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

## Chapter 374 Expedition

- This branch intentionally starts at Chapter 374. Chapters 65–370 have no accepted local English translation here; Chapters 371–373 are source-only bridge summaries.
- Treat `docs/EXPEDITION_SEED.md` and `summaries/0369-0373.md` as bounded orientation, not as a substitute for missing translations.
- When the current Korean source conflicts with bridge context, the current source wins. Preserve uncertainty instead of inventing skipped-range backstory.
- From Chapter 374 onward, the ordinary workflow update, names ledger, profiles, summaries, QA, hashes, and mastering artifacts are authoritative for this branch.

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

| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 아이템              | **Item**                       |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 노부      | **this old man / I**                                            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 당호룡 | **Tang Horyong** | Acting Family Head of the Sichuan Tang Clan |
| 사천당문 | **Sichuan Tang Clan** | The Tang family and clan of Sichuan |
| 당사독 | **Tang Sadok** | Poison King and Family Head of the Sichuan Tang Clan |
| 서천마군 | **Western Heaven Demon Lord** | Major obstacle recently overcome by Taekyung |
| 만독지환 | **Myriad Poison Ring** | Item Taekyung considers taking before departure |
| 미미 | **Mimi** | Tang Sadok's snake and longtime companion; temporarily entrusted to Cheongpung. |
| 동봉 | **Dongbong** | Name or designation associated with the Divine Physician. |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 백염 | **White Flame** | Previously bound item listed by the System. |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 370–374

## Plot

Chapter 370 is intentionally skipped; no accepted English translation or plot details are asserted.

In Chapter 371, Taekyung is celebrated as the Flame Divine Dragon after reaching the Supreme Peak realm. The Qingcheng and Emei Sect Leaders ask him and Jeok Cheongang to investigate a strange Dark Heaven-related formation identified by Samgoe. Taekyung encounters Mungyeong and learns that the physician is secretly the Slaughter Saint.

The group enters a cave hidden by a phantom formation in Chapter 372. It contains supplies, weapons, and a huge inactive transport formation apparently capable of moving people over great distances. Its patterns are not writing, and its origin and purpose remain unclear. Slaughter Saint suggests Dark Heaven succeeded the Demonic Cult, while Taekyung senses something familiar about the formation.

Slaughter Saint decides to resume living as Mungyeong. Back at the Sichuan Tang Clan, Taekyung processes accumulated System messages, reaches Level 120, and discovers that the previously unnamed Inventory item is bound to him and summonable in either world. An investigative party from Henan arrives.

In Chapter 374, Jin Wikyung urges acting Family Head Tang Horyong to relocate the devastated Sichuan Tang Clan to Henan, Shaanxi, or Shanxi, promising orthodox Murim support as a larger war approaches. Horyong does not decide. Wikyung prepares to escort Samgoe to Henan, but Tang Sadok awakens after his long coma, delaying their departure. Taekyung identifies the bound item as the Myriad Poison Ring and expects to return to his original world soon.

## Continuity

- Chapter 370 remains a source-only gap; later references across it must be checked against the current Korean source.
- Taekyung is at the Supreme Peak realm and Level 120. His exact Fame, titles, martial-art stages, and unassigned points after the skipped range are not established here.
- Slaughter Saint is secretly living as Mungyeong and intends to leave Murim after intervening in the crisis.
- The inactive Dark Heaven-associated transport formation remains unexplained. Its origin, destination, mechanism, and connection to Dark Heaven are unresolved.
- Dark Heaven’s agents, larger purpose, and connection to the Demonic Cult remain unresolved.
- The Sichuan Tang Clan, Qingcheng Sect, and Emei Sect were devastated by Dark Heaven. Tang Horyong remains acting Family Head; Tang Sadok, the Poison King, has awakened.
- Jin Wikyung is the Lesser Family Head of the Jin Family of Taiyuan, leader of unified Shanxi Murim, and the assigned escort for Samgoe. He has offered the Tang Clan relocation and orthodox support.
- Orthodox Murim is preparing a new Murim Alliance after Mae Jonghak’s warning of a war greater than the Great Faction War.
- Samgoe remains under guard and is being taken toward Henan; the escort’s outcome and timing are unresolved.
- The Sichuan Tang Clan’s relocation decision and destination are unresolved.
- Taekyung’s return to his original world is imminent; roughly six hours have passed there while about two months passed in Murim.
- The previously unnamed bound Inventory item is the Myriad Poison Ring.
- The outcome of Taekyung’s spar with Jin Mukyung remains unresolved in the accepted earlier anchor.

## Translation Decisions

- Preserve **Flame Divine Dragon**, **Supreme Peak**, **Dark Heaven**, **Slaughter Saint**, **Mungyeong**, **Myriad Poison Ring**, **Sichuan Tang Clan**, **Qingcheng Sect**, **Emei Sect**, **Henan**, **Shaanxi**, and **Shanxi**.
- Preserve uncertainty around the transport formation; do not treat its patterns as writing or assert an origin, destination, or confirmed mechanism beyond its apparent transport function.
- Render **반 시진** and **한 시진** as **half a shichen** and **one shichen**, with a footnote explaining that a shichen is a traditional two-hour period.
- Render **종형** as **older cousin** in the Tang family context.
- Treat Chapters 371–373 as source-only bridge summaries, not complete accepted English translations.

### Prior accepted reading-copy tails

#### Chapter 374 tail (verified mastered)

…
sort of thing time and again, I’d expected a reaction this dramatic. Crack! …But I hadn’t expected this. What the hell was that? Why could I hear my bones going out of alignment? I sighed as his embrace tightened around my entire body like an anaconda from the Amazon jungle. In any case, I let him hug me because I was glad to see him. But his reaction was more violent than ever before. “Hold on, hyungnim. Let go so we can talk. Let go.” “Hyungnim?! Didn’t I tell you to call me hyung instead of using such a stiff formality? You’ve changed, you’ve changed!” “Ah, fine, I get it. Now let me go.” “You used to speak informally when you were little, so why are you using polite speech now? You’ve changed, you’ve changed!” “Let go, fuck.” “Gasp! Even during your rebellious phase, you never swore! You’ve chang—!” “Wow. That running commentary is driving me insane.” *Is his day job a Murim martial artist and his side job a Dementor?* Feeling as though my soul were being sucked out, I shuddered in revulsion and reached out. Whirl—crash! Jin Wikyung’s huge body slammed headfirst into the ground, upside down, and a heavy impact rang out. A middle-aged man from the Sichuan Tang Clan who had been watching let out a startled groan. “It’s okay, it’s okay. We’re just playing around.” “Ah, but still…” “Look. He’s getting up just fine.” Just as I’d said, Jin Wikyung sprang to his feet as though nothing had happened, tears of emotion glimmering in his eyes. “You’ve gotten even stronger in the meantime. That’s our youngest.” His complete lack of change made me snort. “You’re still the same.” “Still the same? Do you know how worried I’ve been these past two months? I couldn’t sleep at night, and I had no appetite. I was reduced to skin and bones.” I looked over his massive, muscular frame and muttered, “Your bones look pretty well padded.” In any case, two months. So much time had already passed. It struck me anew that it was almost time to return. Given that spending ten days in one world meant only about an hour passed in the other… *About six hours must have passed. The plane might be landing soon.* The timing was perfect. I had accumulated quite a bit of fatigue after overcoming the massive obstacle that was the Western Heaven Demon Lord. Rather than drag out the conversation, I got straight to the point. “When are we leaving?” “Our youngest, you must have suffered so much… Hm?” Jin Wikyung, who had been anxiously looking me over, froze. “What did you say?” “You came to take me with you, didn’t you? Oh, and Samgoe too.” Jin Wikyung’s eyes widened. “How did you know that?” The middle-aged man, who appeared to be an important figure in the Sichuan Tang Clan, also spoke with a startled expression. “Sir Jin, did you not come to investigate the full circumstances of the incident?” “I did. However, several members of the investigative party, myself included, will be returning to Henan. Just before we reached Sichuan, I received a mission to escort Samgoe, one of the principal culprits behind the Three-Sect Bloodbath.” “Then what about the matter concerning our family…” “It still stands, of course. It would simply be difficult for the Tang Clan to act on it immediately.” “That’s true. The Family Head is still unable to travel a long distance. We must also seek the consent of the other members of the family.” “Yes. And…” After quietly conversing with the middle-aged man for a moment, Jin Wikyung sent me a discreet Sound Transmission. *But how did you know?* *I can take a hint. It just seemed likely from the circumstances.* *Ah, our youngest. What enormous ordeal did you have to overcome to make you clever, too?* *…* *That somehow rubs me the wrong way.* In truth, I hadn’t figured it out from the circumstances. I knew because a Quest related to escorting Samgoe had popped up. “So when are we leaving?” Having just finished his conversation, Jin Wikyung answered me. “You already knew? That makes things easier. The sooner, the better. Are you ready?” “The only things I brought with me are my two balls. I just need to bring my body.” On top of that, I had two bundles of luggage wrapped tightly in bandages. Jin Wikyung nodded. “Sir Tang, where is Samgoe?” The middle-aged man he had addressed as Sir Tang replied, “We bound all four of his limbs and imprisoned him under strict guard. Ever since his balls were crushed, he has tried to kill himself whenever he gets the chance. You’ll need to be careful.” “Oh dear…” *Even I would want to die if I were him.* In any case, everything was in place for a swift departure. Jin Wikyung considered it for a moment, then gave a decisive answer. “Then half a shichen.[^1] We’ll leave within half a shichen. Is that all right?” “No problem.” The moment I answered without hesitation, hurried footsteps sounded outside the pavilion, followed by someone shouting. “The Family Head! The Family Head has awakened!” Jin Wikyung corrected himself in a lukewarm voice. “One shichen. Let’s make it one shichen.” “…Yes. That sounds better.” What a shame. I could’ve taken the Myriad Poison Ring and bolted. [^1]: A shichen is a traditional two-hour period.

## Korean source

```text
＃375화



병문안에도 순서가 있는 법.

가주이자 가문의 웃어른인 당사독이 깨어났다는 소식에, 당문의 식솔들은 만사를 제치고 달려왔다.

그러나 백여 명이나 되는 인원 모두가 당사독을 볼 수 있는 것은 아니었다.

“은인, 우린 언제쯤 당 할아버지를 뵐 수 있어요?”

“글쎄. 앞에 사람들이 들어간 지 꽤 됐으니까 슬슬 나오지 않을까.”

“아, 그렇구나.”

내 대답에 청풍이 고개를 끄덕인다.

아니, 잠깐만. 청풍?

“뭐야, 언제 왔어?”

“방금요.”

너무 자연스럽게 끼어들어서 있는 줄도 몰랐다. 그런데 이놈이 여길 왜 찾아왔지?

내 의문을 읽기라도 한 것처럼 청풍이 자신의 가슴팍을 가리키며 대답했다.

“미미가 보고 싶다고 해서요.”

“……?”

내가 지금 도대체 뭘 들은 거지.

이제는 하다 하다 의사소통까지 하다니. 이 자식 혹시 화산파가 아니라 슬리데린 출신인가.

심상치 않은 내 시선에 청풍이 고개를 갸웃했다.

“제 이마는 갑자기 왜 쳐다보세요? 뭐 묻었어요?”

“그냥. 이마에 번개 모양 흉터라도 있나 확인해 봤어.”

“네?”

“그런 게 있다.”

말이 끝난 그 순간.

덜컥.

굳게 닫혀 있던 의방의 문이 열리고 십여 명의 사람들이 모습을 드러냈다.

그들은 몇 남지 않은 사천당문의 직계들로, 그중에는 일면식이 있는 당호룡 역시 포함되어 있었다.

“후우…….”

붉게 충혈된 눈으로 하늘을 올려다본 그가 이쪽을 향해 걸어왔다.

“가주께서 뵙고자 하시오.”

“기다리고 있었습니다.”

고개를 끄덕인 진위경이 앞장서고, 나와 청풍이 그 뒤를 따라 의방으로 들어갔다.

사방에서 진동하는 탕약 냄새를 맡으며 얼마나 걸었을까. 하얀 천으로 코와 입을 가린 의원이 안내해 준 의실로 들어서자, 마침내 낯익은 얼굴들과 마주할 수 있었다.

“쿨럭, 왔는가.”

힘겹게 잔기침을 내뱉는 당사독의 상태는 한눈에 보기에도 심각했다.

부러진 팔다리와 내상으로 인해 불안정한 기운.

상반신을 일으키려는 그를, 우리와 눈인사를 주고받은 신의(神醫)가 만류했다.

“가주, 제가 움직이지 말라 하지 않았습니까.”

“노부는 죄인일세. 죽어 마땅한 죄를 지었으니 벌을 청하는 것이 이치지.”

창백한 얼굴로 고개를 저은 당사독이 나를 똑바로 응시하며 말을 이었다.

“구차한 변명은 하지 않겠네. 서천마군이 지하 뇌옥으로 향한 것은, 노부가 알려 주었기 때문일세.”

나는 비스듬히 팔짱을 꼈다.

“아, 어쩐지.”

“……?”

“왜요.”

당사독이 당황한 얼굴로 물었다.

“아, 알고 있었나?”

“당연히 처음에는 몰랐죠. 그때는 워낙 정신이 없기도 했고. 그런데 나중에 곰곰이 생각해 보니까 서천마군. 그 새끼가 어떻게 만독지환의 위치를 알았나 싶더라고요.”

애당초 만독지환의 위치를 아는 사람은 극소수.

청풍은 겉보기에는 꽃잎처럼 가벼워 보여도 나무뿌리처럼 단단한 놈이니, 발설할 만한 사람은 당사독 한 명밖에 없었다.

“왜 그랬습니까?”

“……만독지환의 위치를 알려 주면 가문의 명맥을 보존해 주겠다 하더군.”

“그걸 믿었어요?”

“노부가 어리석었네. 잠시 판단력이 흐려져, 해서는 안 될 일을 저질렀지.”

“알고는 계시네요.”

나를 바라보는 당사독의 눈빛이 파르르 떨렸다.

“이 늙은이가 목숨을 건사할 수 있었던 것은, 자네들에게 사죄하고 벌을 받으라는 하늘의 뜻이겠지.”

“그럼 가주께서는 어떤 벌을 원하십니까.”

불쑥 들려온 차가운 목소리의 주인은 아무 말 없이 대화를 듣고 있던 진위경이었다.

“태원진가의 소가주 되시는가.”

“예. 두 아우를 자식처럼 키운 형이기도 하지요.”

깊게 가라앉은 진위경의 눈동자에서 숨길 수 없는 분노가 진득하게 묻어나왔다.

“정도(正道)를 걷는 이라면 해서는 안 될 짓이었습니다.”

“알고 있네. 아니, 알고 있소. 그렇기에 죄를 청하는 것이오.”

“자결하라 한다면 어쩌시겠습니까.”

“……!”

나를 포함한 모두가 놀란 눈빛으로 진위경을 바라봤다.

그러나 한 사람, 당사독만은 예외였다.

그는 담담하기 그지없는 표정으로 입을 열었다.

“나는 도의(道義)를 저버렸으나, 그대들이 목숨을 내놓고 싸워 준 덕분에 본가의 명맥을 이을 수 있게 되었소. 이 보잘것없는 늙은이의 목숨으로 사죄를 대신할 수 있다면, 흔쾌히 그리하리다.”

짧은 침묵 뒤에 이어진 것은 진위경의 한숨이었다.

“후우…….”

복잡한 눈빛으로 당사독을 바라보던 그가 나를 향해 고개를 돌렸다.

“어찌하겠느냐?”

“……뭘요. 자결?”

“그 무엇이든.”

갑자기 손에 칼자루가 쥐어지니 심장이 쫀득해지는 기분이다.

더군다나 그 칼자루 끝에 달린 것이 사천당문 가주의 목숨이라고 하니 더더욱 그랬다.

‘갑자기 분위기 싸해진 것 보소.’

물론 허허 웃고 넘어갈 일은 아니다. 내가 무슨 공명정대하고 속 넓은 인의대협도 아니고, 솔직히 사건의 전말을 깨달았을 때는 슬그머니 분노가 솟구치기도 했다.

당시에는 나뿐만 아니라 모두의 목숨이 걸려 있는 상황이었으니까.

하지만…….

“됐습니다. 그렇게까지 하고 싶지는 않네요.”

그래, 한편으로는 당사독의 입장을 이해한다.

얼굴 몇 번 본 것이 고작인 외부인과 일가의 가주로서 목숨 걸고 지켜야 할 혈육을 저울에 올려 둔다면 나 역시 그와 같은 선택을 했을 것 같았다.

‘그전에 빚도 있었고.’

적천강이 깨어날 수 있었던 것에는 당사독의 도움도 크게 한몫했다.

비록 모종의 거래가 있었다고는 하나, 한 핏줄에게도 알리지 않은 신물을 빌려준 사람 역시 당사독이었다.

“그러니까 이걸로 쌤쌤. 퉁 치죠. 아니, 그건 너무 나갔고 이번 일로 사천당문이 저희에게 큰 빚을 진 것으로 하자고요.”

내 말이 끝나자 청풍과 신의가 입을 열었다.

“은인이 위험해졌던 건 분명히 당 할아버지의 잘못이지만…… 저도 은인의 뜻에 따를래요.”

“전 이미 잊었습니다. 다만 의원으로서 바라는 것이 있다면 가주께서 하루빨리 쾌차하는 것이지요. 아직 살아남은 식솔들이 있지 않습니다.”

마지막으로 입을 연 것은 진위경이었다. 처음과 달리 그에게서는 더 이상 어떤 분노도 느껴지지 않았다.

아니, 어쩌면 진위경은 처음부터 내 대답을 알고 있었을지도 모르겠다.

“그렇다는군요. 가주의 생각은 어떠하십니까.”

“……!”

우리를 바라보는 당사독의 눈동자가 격동으로 떨렸다.

짧은 침묵이 흐른 뒤, 갈라진 목소리가 그의 입술 사이로 흘러나왔다.

“노부가, 사천당문이 그대들에게 큰 은혜를 입었구려.”

당사독이 진심을 담아 고개를 숙인 바로 그 순간이었다.

띠링. 띠링. 띠링.



- 자신의 죄를 고백하는 것은 어렵지만, 그보다 더 큰 용기를 필요로 하는 것이 있습니다. 바로 용서입니다.

- 히든 퀘스트, [사죄와 용서]를 성공적으로 완료했습니다!

- [Lv.115 당사독]이 당신들의 호의에 깊은 감사를 표합니다. 그와 [사천당문]은 결코 오늘의 호의와 도움을 잊지 않을 것이며, [사천당문]의 사람들은 당신을 은인으로 기억할 것입니다!

- 칭호, [당문의 은인]을 획득했습니다!

- 히든 퀘스트 완료 보상으로 막대한 경험치와 명성을 얻었습니다!

- 레벨 업!



뭐야, 이거. 갑자기 히든 퀘스트라니.

내가 뜬금없이 울려 퍼진 시스템 알림에 얼떨떨해하던 그때, 차가운 무언가가 다리 사이를 스치며 지나갔다.

취릭, 취리리릭.

“미미, 이 녀석.”

오랜만에 해후하는 미미와 당사독의 모습에, 잠시 깜빡하고 있던 물건 하나가 떠올랐다.

“아, 그러고 보니 만독지환 말인데요. 다행히 제가 지금까지 잘 갖고 있었…….”

“그런가?”

내가 미처 말을 끝맺기도 전에, 불쑥 입을 연 당사독이 말을 이었다.

“그럼 계속 갖고 있으시게.”

“예, 그럼 제가 계속…… 예?”

“자네에게 본가의 신물을 맡기겠네. 은인에 대한 증표이니 부디 거절하지 말아 주게.”

띠링.



- 소유자의 뜻에 따라 [만독지환]이 당신에게 양도되었습니다!

- 새로운 아이템이 당신에게 종속됩니다!

- 현재 보유 중인 종속 아이템 : [백염], [만독지환], [???].

- 아직 이름이 정해지지 않은 종속 아이템이 있습니다. 새로운 이름을 부여해 주십시오.



아니, 오늘 무슨 날이야?

도대체 앞으로 어떤 개 같은 일들이 벌어지려고 이렇게 퍼 주나 싶어 불안하기까지 할 지경이다.

금붕어처럼 입만 벙긋거리는 내 모습에, 당사독이 희미한 미소를 머금었다.

“다들 원하는 것들이 있다면 말씀하시구려. 본가의 역량이 닿는 한 무엇이든 들어드리리다.”

신의가 따라 웃으며 대답했다.

“원하는 것이라면, 그저 병자들이 하루빨리 낫길 바랄 뿐입니다.”

“허어.”

과연 신의다운 대답이다. 아니, 이제는 동봉이라고 해야 하나.

하지만 한 가지 확실한 것은, 그 역시 또 다른 한 사람의 신의(神醫)라는 사실이었다.

“자네는 무엇을 원하는가?”

갑작스러운 질문에 청풍이 화들짝 놀랐다.

“저, 저요?”

당사독이 고개를 끄덕이자 청풍이 손발을 배배 꼬며 대답했다.

“저어는…… 그러니까요. 으음. 없어요.”

“정말인가?”

“네에. 없는 것 같아요.”

“…….”

“…….”

야, 이 자식아. 미미쨩한테서 눈이나 떼고 얘기해.

거울을 가져와서 보여 주고 싶다. 지금 청풍의 눈동자에는 미미쨩을 향한 애절함과 갈망이 떠올라 있었다.

저러다가 뱀 가죽이 뚫리겠다 싶던 그때, 당사독이 입을 열었다.

“이 녀석은 내 오랜 친우일세. 지난 수십 년 동안, 노부가 아무에게도 드러내지 못했던 희로애락(喜怒哀樂)을 나눌 수 있었던 유일한 존재였지.”

청풍이 측은해진 눈빛으로 당사독을 바라봤다.

“당 할아버지께서는 다른 친구가 없으시군요.”

“만들지 않았다네. 노부에게 당문의 가주란 그런 자리였으니까.”

“그래서 친구가 없으시군요.”

“없던 게 아니라. 만들 수 있었는데…….”

“친구 하나 없었군요. 불쌍해라.”

“…….”

신의가 다급하게 당사독의 어깨를 붙잡았다.

“가주. 진정하십시오. 호흡이 너무 가파릅니다!”

“후욱, 후우욱.”

“크고 천천히 호흡하십시오. 자, 저를 따라서 하나, 둘…….”

“후우우우욱…….”

잠시 후, 간신히 고혈압의 위기에서 벗어난 당사독이 청풍을 바라보며 입을 열었다.

“하지만 자네에게 미미를…….”

청풍이 두 손으로 입을 틀어막았다.

“아니에요. 당 할아버지. 할아버지의 유일한 친구를 데려갈 수는 없어요.”

“……아직 맡기겠다고 하지 않았는데.”

“앗. 아앗.”

당사독이 한숨을 푹 내쉬었다. 잠깐이었지만 저런 놈한테 미미쨩을 맡겨도 되나, 하는 생각을 했음이 틀림없었다.

“그래, 자네의 짐작대로일세. 향후 본가의 향방이 어떻게 될지 모르는바, 노부는 자네에게 미미를 맡기고자 하네. 물론 임시로.”

“와아!”

“마지막에 했던 말 들었나? 임시일세.”

“와아아!”

못 들었다에 혁무진 오른손 손목을 건다.

미미의 임시보호자가 된 청풍은 기뻐서 어쩔 줄을 몰라 했다.

“걱정 마세요. 잘 돌볼게요!”

“지난번에 본 바에 의하면 미미가 자네를 잘 따르는 것 같긴 하지만, 녀석은 본래 성정이 까다롭고 낯을 많이 가리니…….”

“미미. 회오리치기 후 뱅글뱅글 돌고 인사하기!”

취리리릭!

“오메, 시벌.”

여기서 신기술을 써 버리네.

생전 처음 보는 광경에 반쯤 넋이 나가 있던 진위경이 얼빠진 목소리로 중얼거렸다.

“가주께서 걱정하시는 일은 없을 것 같군요.”

당사독의 눈동자에 지진이 일어났다.

당사독은 진위경과 긴히 나눌 말이 있다며 따로 자리를 청했고, 나와 청풍은 먼저 방을 빠져나왔다.

아니, 지금 막 한 사람이 추가되었다.

“진 소협. 잠시 이 늙은이에게 시간을 내어줄 수 있겠소?”

“저요?”

신의가 잔잔한 웃음과 함께 고개를 끄덕였다.

“떠나기 전에 꼭 부탁하고 싶은 것이 있소.”
```

## Current accepted English baseline

```markdown
# Chapter 375

Even hospital visits had a proper order.

When word spread that Tang Sadok—the Family Head and elder of the clan—had awakened, the members of the Tang household dropped everything and came running.

However, not all of the more than one hundred people could see Tang Sadok.

“Benefactor, when can we see Grandpa Tang?”

“I don’t know. It’s been quite a while since the people in front of us went in, so they should be coming out soon.”

“Oh, I see.”

Cheongpung nodded at my answer.

Wait. Cheongpung?

“What are you doing here? When did you get here?”

“Just now.”

He had joined the conversation so naturally that I hadn’t even noticed he was there. But why had this guy come here?

As though he had read my thoughts, Cheongpung pointed to his chest and answered.

“Because Mimi said she wanted to visit.”

“……?”

*What did I just hear?*

Now Mimi was communicating with him, too. Was this bastard from Slytherin instead of Huashan?

At my suspicious gaze, Cheongpung tilted his head.

“Why are you suddenly staring at my forehead? Is there something on it?”

“I was just checking whether you had a lightning-shaped scar on your forehead.”

“What?”

“Never mind.”

The moment the words left my mouth—

Clunk.

The tightly closed door of the medical ward opened, and more than ten people emerged.

They were among the few remaining direct-line members of the Sichuan Tang Clan. Tang Horyong was among them, and I had met him before.

“Hoo……”

After looking up at the sky with bloodshot eyes, he walked toward us.

“The Family Head wishes to see you.”

“We’ve been waiting.”

Jin Wikyung nodded and led the way. Cheongpung and I followed him into the medical ward.

Who knew how long we walked through the pervasive smell of medicinal decoctions? At last, the physician whose nose and mouth were covered with white cloth led us into a treatment room, where we came face-to-face with several familiar faces.

“Cough, cough. You’ve come.”

Tang Sadok’s condition was visibly serious. His limbs were broken, and his internal injuries had left his qi unstable.

As he tried to raise his upper body, the Divine Physician who had exchanged a nod with us stopped him.

“Family Head, didn’t I tell you not to move?”

“This old man is a sinner. I committed a crime deserving of death, so it is only right that I ask for punishment.”

Pale-faced, Tang Sadok shook his head, stared straight at me, and continued.

“I will not make any pathetic excuses. The reason the Western Heaven Demon Lord headed for the underground prison was because I told him about it.”

I folded my arms at an angle.

“Ah. That explains it.”

“……?”

“Why are you looking at me like that?”

“Ah, you knew?”

“Of course I didn’t know at first. There was too much going on at the time. But later, when I thought about it carefully, I started wondering how that bastard, the Western Heaven Demon Lord, had known the location of the Myriad Poison Ring.”

Only a handful of people knew where the Myriad Poison Ring was in the first place.

Cheongpung might look as light as a flower petal, but he was as sturdy as a tree root. That left Tang Sadok as the only person who could have revealed it.

“Why did you do it?”

“He said that if I revealed the location of the Myriad Poison Ring, he would preserve the family line.”

“And you believed him?”

“This old man was foolish. My judgment was clouded for a moment, and I committed an act I should never have committed.”

“At least you know that.”

Tang Sadok’s eyes trembled as he looked at me.

“The reason this old man was able to keep his life is surely heaven’s will. I must apologize to you all and accept my punishment.”

“What punishment do you want, then?”

The owner of the cold voice was Jin Wikyung, who had been listening to the conversation in silence.

“Are you the Lesser Family Head of the Jin Family of Taiyuan?”

“Yes. I am also an older brother who raised my two younger brothers as though they were my own children.”

Unconcealed anger clung heavily to Jin Wikyung’s deeply sunken eyes.

“It was something no one walking the righteous path should have done.”

“I know. No—I understand. That is why I ask to be punished.”

“What will you do if I tell you to take your own life?”

“……!”

Everyone, myself included, looked at Jin Wikyung in surprise.

Everyone except Tang Sadok.

He opened his mouth with an expression of utter calm.

“I abandoned righteousness, but thanks to the fact that all of you fought while putting your lives on the line, my family will be able to continue. If this insignificant old man’s life can serve as an apology, I will gladly give it.”

After a brief silence, Jin Wikyung sighed.

“Hoo……”

He stared at Tang Sadok with complicated emotions before turning to me.

“What will you do?”

“……About what? His suicide?”

“Whatever you wish.”

Having the hilt of a knife suddenly thrust into my hand made my heart feel strangely taut.

Even more so when I was told that the life attached to the end of that hilt was the life of the Family Head of the Sichuan Tang Clan.

*Look at how suddenly the mood turned cold.*

Of course, this wasn’t something to laugh off. I wasn’t some impartial, broad-minded Great Hero. To be honest, when I realized the whole truth of what had happened, a quiet anger had risen inside me.

After all, everyone’s lives had been on the line at the time—not just mine.

But……

“That’s enough. I don’t want to take things that far.”

That was right. On the other hand, I could understand Tang Sadok’s position.

If, as the head of a family, I had to weigh blood relatives I was duty-bound to protect with my life against outsiders I’d met only a few times, I probably would’ve made the same choice.

*I had a debt to him, too.*

Tang Sadok’s help had played a major role in Jeok Cheongang’s recovery.

There may have been a transaction involved, but Tang Sadok had still lent us a sacred artifact without even telling his own blood relatives.

“So let’s call it even. We’ll let it slide. No, that’s going too far—let’s say the Sichuan Tang Clan owes us a huge debt over this.”

When I finished speaking, Cheongpung and the Divine Physician spoke up.

“It was definitely Grandpa Tang’s fault that the Benefactor was put in danger, but… I’ll follow the Benefactor’s wishes, too.”

“I’ve already forgotten about it. But if there is one thing I wish for as a physician, it is that the Family Head recovers as soon as possible. There are still surviving members of the household, after all.”

The last person to speak was Jin Wikyung. Unlike before, there was no anger to be felt from him anymore.

No—perhaps Jin Wikyung had known my answer from the very beginning.

“So that is their decision. What do you think, Family Head?”

“……!”

Tang Sadok’s eyes trembled with emotion as he looked at us.

After a short silence, a hoarse voice slipped between his lips.

“This old man—and the Sichuan Tang Clan—have received a great kindness from you.”

The instant Tang Sadok bowed his head with genuine sincerity—

> **System**
>
> Confessing one's sins is difficult, but there is something that requires even greater courage. That is forgiveness.
>
> **Hidden Quest:** **Atonement and Forgiveness** successfully completed!
>
> **Level 115 Tang Sadok** expresses his deep gratitude for your kindness. He and the **Sichuan Tang Clan** will never forget the favor and assistance you showed them today, and the people of the **Sichuan Tang Clan** will remember you as their **Benefactor**!
>
> **Title Acquired:** **Benefactor of the Tang Clan**
>
> You have gained a tremendous amount of EXP and Fame as a reward for completing the Hidden Quest!
>
> **Level Up!**

*What was this? A Hidden Quest, all of a sudden?*

As I stood there dumbfounded by the System notification that had suddenly rung out, something cold brushed between my legs.

Ssssk. Ssssss.

“Mimi, you little……”

At the sight of Mimi and Tang Sadok reunited after so long, I remembered something I had momentarily forgotten.

“Ah, now that I think about it, the Myriad Poison Ring. Thankfully, I’ve been keeping it safe all this time……”

“Is that so?”

Before I could finish speaking, Tang Sadok interrupted.

“Then continue to keep it.”

“Yes, then I’ll keep—what?”

“I am entrusting the sacred artifact of our family to you. It is a token of our gratitude to our Benefactor, so please do not refuse.”

> **System**
>
> According to the owner's wishes, **Myriad Poison Ring** has been transferred to you!
>
> A new item is now bound to you!
>
> **Currently bound items:** **White Flame**, **Myriad Poison Ring**, **???**
>
> You have a bound item that has not yet been named. Please give it a new name.

*What kind of day was today?*

I was getting downright nervous, wondering what kind of shitty things were about to happen for them to be giving so much away like this.

At the sight of me opening and closing my mouth like a goldfish, Tang Sadok smiled faintly.

“If any of you have something you want, speak up. I will grant you anything within the limits of our family’s abilities.”

The Divine Physician smiled along with him and answered.

“If there is something I want, it is simply for the patients to recover as soon as possible.”

“Good heavens.”

That was certainly an answer worthy of the Divine Physician. No, should I be calling him Dongbong now?

But one thing was certain: he, too, was another Divine Physician.

“What do you want?”

Cheongpung jumped at the sudden question.

“M-Me?”

Tang Sadok nodded, and Cheongpung answered while fidgeting with his hands and feet.

“Well, I…… Let me think. Um. Nothing.”

“Are you sure?”

“Yeees. I don’t think there’s anything.”

“……”

“……”

*Hey, you idiot. Take your eyes off Mimi-chan and talk.*

I wanted to bring him a mirror and show him his face. Cheongpung’s eyes were filled with aching longing and desire for Mimi-chan.

*At this rate, he’s going to stare a hole through the snake’s hide.*

Just then, Tang Sadok spoke.

“This creature is an old friend of mine. For the past several decades, it has been the only one with whom this old man could share the joys and sorrows he could reveal to no one else.”

Cheongpung looked at Tang Sadok with pity.

“So you don’t have any other friends, Grandpa Tang.”

“I never made any. Being the Family Head of the Tang Clan was that kind of position.”

“So you have no friends.”

“It wasn’t that I had none. I could have made them, but……”

“You didn’t have a single friend. How pitiful.”

“……”

The Divine Physician hurriedly grabbed Tang Sadok by the shoulders.

“Family Head, please calm down. Your breathing is too rapid!”

“Huuk, hoo-oo.”

“Take deep, slow breaths. Come on, follow me. One, two……”

“Huooooo……”

A little while later, Tang Sadok barely managed to escape a hypertensive crisis before opening his mouth again.

“But I could entrust Mimi to you……”

Cheongpung covered his mouth with both hands.

“No, Grandpa Tang. I can’t take away your only friend.”

“……I haven’t even said I was going to entrust her to you yet.”

“Oh. Oh!”

Tang Sadok let out a deep sigh. It had only been for a moment, but he had undoubtedly wondered whether he could entrust Mimi-chan to someone like that.

“Yes, just as you guessed. Since we do not know what path our family will take from here on, I wish to entrust Mimi to you. Temporarily, of course.”

“Yaaay!”

“Did you hear what I said at the end? Temporarily.”

“Yaaay!”

*I’ll bet Hyuk Mujin’s right wrist that he didn’t hear that.*

Cheongpung, now Mimi’s temporary guardian, didn’t know what to do with his happiness.

“Don’t worry. I’ll take good care of her!”

“From what I saw last time, Mimi does seem to like you, but she has a rather difficult temperament and is very wary of strangers, so……”

“Mimi. Do Whirlwind, then spin round and round and say hello!”

Sssriririk!

“Oh, for fuck’s sake.”

*He’s using a new trick here.*

Jin Wikyung had been half out of his mind at the sight he was seeing for the first time in his life. He muttered in a dazed voice.

“It seems you have nothing to worry about, Family Head.”

An earthquake struck Tang Sadok’s eyes.

Tang Sadok asked Jin Wikyung to stay behind for a private conversation, while Cheongpung and I left the room first.

No, one person had just been added.

“Young Hero Jin. Could you spare this old man a little of your time?”

“Me?”

The Divine Physician nodded with a gentle smile.

“There is something I would like to ask you before you leave.”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 375`.

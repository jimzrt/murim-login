# Master Edit Task — Chapter 377

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

- This branch backfills Chapters 370–373 against the Chapter 65 anchor. Chapters 66–369 have no accepted local English translation here.
- Treat `docs/EXPEDITION_SEED.md` as bounded orientation, not as a substitute for missing translations. Do not read parked Chapters 374–375 while drafting 370–373.
- When the current Korean source conflicts with bridge context, the current source wins. Preserve uncertainty instead of inventing skipped-range backstory.
- After Chapter 373 is committed, run `python tools/expedition.py resume-parked` so the existing 374–375 translations remain the accepted line.

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
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 장강수로맹  | **Yangtze River Channel League** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 로그아웃             | **Logout**                     |
| 사천     | **Sichuan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 애향 | **Ae-hyang** | The Sichuan Governor's favorite concubine; covertly manipulative. |
| 궁기방 | **Gung Gibang** | Young beggar and Future Beggar Chief. |
| 문경 | **Mungyeong** | Young Disciple of the Divine Physician overseeing Jin Taekyung's care. |
| 서천마군 | **Western Heaven Demon Lord** | Major obstacle recently overcome by Taekyung |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 성도 | **Chengdu** | City whose western port is the departure point. |
| 상산왕 | **King of Shangshan** | Noble whose token was carried by Taekyung's group. |
| 수룡채 | **Water Dragon Stronghold** | Stronghold whose flag flies from the ships carrying Taekyung's group. |
| 흑룡갑 | **Black Dragon Armor** | The armor's former name; only a fragment survives. |
| 화룡갑 | **Flame Dragon Armor** | New name Taekyung gives the bound armor fragment. |
| 열화신공 | **Blazing Flame Divine Art** | Art whose formula Taekyung uses to infuse the armor. |
| 삼공 | **Grand Councilor** | High office referenced in the Sichuan Governor's ambitions. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 궁기방 | orthodox_ally_to_orthodox_ally | Young Hero Gung | blunt-but-formal | Uses 궁 소협 while teasing Gung Gibang about his injuries. |
| 혁무진 | 청풍 | junior_ally_to_younger_ally | Young Hero Cheong | formal-but-bewildered | Uses 청 소협 when reacting to Cheongpung's warning. |
| 혁무진 | 진태경 | subordinate_to_squad_leader | Squad Leader | deferential | Calls Taekyung 조장님 when announcing his awakening. |
| 궁기방 | 진태경 | squadmate_to_squad_leader | Jin Taekyung | familiar-but-direct | Calls Taekyung by name when he wakes. |
| 진태경 | 문경 | ally_to_secret_identity_holder | Mungyeong | casual-but-teasing | Taekyung accepts the requested name and deliberately uses it in a familiar vocative. |
| 사천성주 | 애향 | lover_to_favorite_concubine | Ae-hyang | intimate-affectionate | The Sichuan Governor repeatedly calls his favorite concubine by name and speaks to her in an indulgent intimate manner. |
| 애향 | 사천성주 | favorite_concubine_to_lover | my dear | intimate-coquettish | Ae-hyang addresses the Sichuan Governor as 가가 while flattering and manipulating him. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

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

#### Chapter 375 tail (verified mastered)

…
even greater courage. That is forgiveness. > > **Hidden Quest:** **Apology and Forgiveness** successfully completed! > > **Level 115 Tang Sadok** expresses his deep gratitude for your kindness. He and the **Sichuan Tang Clan** will never forget the kindness and assistance you showed them today, and the people of the **Sichuan Tang Clan** will remember you as their **Benefactor**! > > **Title Acquired:** **Benefactor of the Tang Clan** > > You have gained a tremendous amount of EXP and Fame as a reward for completing the Hidden Quest! > > **Level Up!** *What was this? A Hidden Quest, all of a sudden?* As I stood there dumbfounded by the System notification that had suddenly rung out, something cold brushed between my legs. Sssrik. Sssriririk. “Mimi, you little……” At the sight of Mimi and Tang Sadok reunited after so long, I remembered something I had momentarily forgotten. “Ah, now that I think about it, the Myriad Poison Ring. Thankfully, I’ve been keeping it safe all this time……” “Is that so?” Tang Sadok cut in before I could finish. “Then continue to keep it.” “Yes, then I’ll keep—what?” “I am entrusting our family’s sacred artifact to you. It is a token of gratitude for our Benefactor, so please do not refuse.” > **System** > > According to the owner’s wishes, **Myriad Poison Ring** has been transferred to you! > > A new item is now bound to you! > > **Currently bound items:** **White Flame**, **Myriad Poison Ring**, **???** > > You have a bound item that has not yet been named. Please give it a new name. *What kind of day was today?* I was getting downright nervous, wondering what kind of shitty things were about to happen for them to be giving so much away like this. At the sight of me opening and closing my mouth like a goldfish, Tang Sadok smiled faintly. “If any of you desire something, speak. I will grant anything within our family’s power.” The Divine Physician smiled along with him. “If there is something I desire, it is simply for the patients to recover as soon as possible.” “Good heavens.” That was certainly an answer worthy of the Divine Physician. No, should I be calling him Dongbong now? But one thing was certain: he, too, was another Divine Physician. “What do you want?” Cheongpung jumped at the sudden question. “M-Me?” Tang Sadok nodded, and Cheongpung answered while fidgeting with his hands and feet. “Well, I… Let me think. Um. Nothing.” “Are you sure?” “Yeees. I don’t think there’s anything.” “……” “……” *Hey, you idiot. Take your eyes off Mimi-chan and talk.* I wanted to bring him a mirror and show him his own face. His eyes brimmed with aching longing and desire for Mimi-chan. *At this rate, he’s going to stare a hole through the snake’s hide.* Just then, Tang Sadok spoke. “This creature is an old friend of mine. For the past several decades, she has been the only one with whom this old man could share the joy, anger, sorrow, and pleasure he could reveal to no one else.” Cheongpung looked at Tang Sadok with pity. “So you don’t have any other friends, Grandpa Tang.” “I never made any. Being the Family Head of the Tang Clan was that kind of position.” “So you have no friends.” “It wasn’t that I had none. I could have made them, but……” “You didn’t have a single friend. How pitiful.” “……” The Divine Physician hurriedly grabbed Tang Sadok by the shoulders. “Family Head, calm down. You’re breathing too quickly!” “Huuk, hoo-oo.” “Take deep, slow breaths. Come on, follow me. One, two……” “Huooooo……” A little while later, after narrowly escaping a hypertensive crisis, Tang Sadok looked at Cheongpung and spoke again. “But as for Mimi, perhaps you……” Cheongpung covered his mouth with both hands. “No, Grandpa Tang. I can’t take away your only friend.” “……I haven’t said I’m entrusting her to you yet.” “Oh. Oh!” Tang Sadok let out a deep sigh. It had only been for a moment, but he had undoubtedly wondered whether he could entrust Mimi-chan to someone like that. “Yes, just as you guessed. Since we do not know what path our family will take from here on, I wish to entrust Mimi to you. Temporarily, of course.” “Yaaay!” “Did you hear the last part? Temporarily.” “Yaaay!” *I’ll bet Hyuk Mujin’s right wrist that he didn’t.* Now Mimi’s temporary guardian, Cheongpung was beside himself with joy. “Don’t worry. I’ll take good care of her!” “From what I saw last time, Mimi does seem fond of you, but she is temperamental by nature and extremely wary of strangers, so……” “Mimi. Do Whirlwind, then spin round and round and say hello!” Sssriririk! “Holy shit.” *He busted out a new trick right here.* Jin Wikyung, half stunned by the sight he was seeing for the first time in his life, muttered in a dazed voice. “It seems you have nothing to worry about, Family Head.” An earthquake shook Tang Sadok’s eyes. Tang Sadok asked Jin Wikyung to stay behind for a private conversation, while Cheongpung and I left the room first. No, one person had just been added. “Young Hero Jin. Could you spare this old man a little of your time?” “Me?” The Divine Physician nodded with a gentle smile. “There is something I very much wish to ask of you before you leave.”

#### Chapter 376 tail (verified mastered)

…
because he hated killing, then it should have been right for him to abandon martial arts as well—the means by which he killed. Yet his martial arts had advanced even further. It was proof that he had been unable to let go of his attachment to them. *Why was that?* The old disciple’s voice broke through his brief reverie. “You can treat hundreds, even thousands, of patients, Master. At the same time, you are capable of saving tens of thousands of lives.” “…” “Please prevent the coming war—not as the Slaughter Saint, but as the Divine Physician. This disciple will care for the patients here.” Mungyeong suddenly lifted his head and looked at the sky. It was clear and blue. Seven days and nights earlier, when the Sichuan Tang Clan had been dyed in blood, the sky had been filled with dark clouds. “The sky is clear.” In his blunt voice, he resumed his halted steps. “I should go check on the patients. Take your time coming down.” As he descended the hill, Dongbong’s voice scattered behind him. “The Hour of the Dog. They said they would depart from Chengdu’s western port then.[^1]” “Pointless. The Murim is not where I belong.” Yet as the old disciple watched his master’s back recede into the distance, a faint smile formed on his lips. “Please… be well.” Whoooosh. A wind blew from somewhere, sweeping between the two men. * * * “What are you looking at so intently?” At Hyuk Mujin’s question, I turned away from the crowd surrounding the port. “Nothing. Just in case.” “Then what are you looking at?” “You little pest. Why are you interrogating me like this? If I say it’s nothing, take it as nothing.” Hyuk Mujin gave me a knowing smile. “I actually know why you’re acting that way, Squad Leader.” “…?” I froze for a moment. How the hell did he know? Even Cheongpung hadn’t heard the conversation between the Divine Physician and me. *Since when was this guy so perceptive?* As I wondered about it, he whispered, “Weren’t you looking at the young lady standing fourth from the right in the front row?” “…” “She is pretty, that’s for sure. She looks like the daughter of a fairly wealthy family. If you give me permission, Squad Leader, I could quietly go over there as your right-hand man and arrange a separate—” “Mujin.” “Yes? Ah, do you prefer meeting women naturally? If so…” “Do you want to sink to the bottom of the Yangtze?” “…!” “Stop talking nonsense and keep lying there. And don’t puke later because you get seasick.” “…Yes, sir.” As Hyuk Mujin quietly shrank in on himself, Gung Gibang snickered. “What a fool. It’s not the fourth woman on the right, but the third on the left. Anyone can see she’s much prettier. Your eyes must be crooked.” “Want me to make them crooked for real?” “…Sorry.” “Let’s live like human beings. Like human beings.” With a sigh, I shook my head and gave the crowd gathered like clouds one last sweeping look. They were both definitely pretty, but the third woman from the left was more my type— *No. That’s not what this is about.* *Damn it. Those idiots wouldn’t shut up about them, and now I can’t stop looking.* Just then, a towering, bronze-skinned man approached me. “Hey there, junior. No, not junior. Young Hero Jin. No, Great Hero.” *What is this, buffering?* I offered a solution to the boatman Mu Song, who was switching forms of address at lightning speed. “Just call me junior.” “Ahem. Th-That would be all right?” “Why wouldn’t it be? You used to do it just fine.” “Even so, you’ve accomplished such a great thing.” He had a point. I had gone from a local rising martial artist known as the Sleeping Dragon of Shanxi to a nationwide celebrity. “And Great Hero Jeok doesn’t seem to like me very much, either…” “It’s fine. He never liked water much in the first place.” Where Mu Song kept glancing, Jeok Cheongang stood with a face twisted in fury. Right beside him, Jin Wikyung was examining some bamboo slips whose contents I could not identify, while Cheongpung was teaching Mimi a new trick. “Mimi, ride the waves!” Sssrik—splaash! …Was that thing a water snake? Mu Song, whose attention had been stolen for a moment by the rare spectacle, finally spoke with a sour expression. “In any case, preparations for departure are complete. When should we set sail?” “What time is it now?” “The Hour of the Dog you mentioned has passed. It would be best to leave before it gets any darker.” “…Hmm.” “Is someone else coming?” I considered Mu Song’s question for a moment, then shook my head. “No. No one.” “Then we can depart.” “Let’s do that.” “Very well.” Mu Song raised one hand high, and the water bandits, who had already finished all their preparations, moved in perfect unison. The people gathered to see us off were waving in our direction when— “Wait! Just a moment!” “Stop! Stop!” The bow of the fast ship rocked as it was about to pull away from the port. Far in the distance, I spotted a boy pushing his way through the crowd and let out a quiet laugh. “Let’s take one more passenger.” [^1]: The Hour of the Dog was a traditional two-hour period, roughly corresponding to 7–9 p.m.

## Korean source

```text
＃377화



“그들은, 떠났나?”

살이 토실토실하게 오른 중년인, 사천성주의 긴장 어린 물음에 호위장이 대답했다.

“예. 한 식경 전에 그들이 탄 장강수로맹의 쾌조선이 출항했습니다.”

“휴우우.”

뱃살이 출렁일 만큼 깊은 안도의 한숨을 내쉰 사천성주가 손을 내저었다.

“알겠으니 이만 물러가게. 혹시 무림인들에 관련된 소식이 있다면 바로바로 보고하고.”

“알겠습니다. 한데 성도 인근에 주둔시켜 놓은 병력은…….”

사천성주가 눈살을 찌푸렸다.

“이봐, 호위장.”

“예?”

“내가 그런 시시콜콜한 부분까지 신경 써야 하나? 그 정도 뒤처리는 자네들끼리 처리하라고. 도지휘사(都指揮使), 그 꼬장꼬장한 작자와 잘 상의를 하든가 해서. 응?”

“…….”

호위장은 내심 어이가 없었다.

이게 말인가 방귀인가. 성주의 무능함과 아랫사람에게 일 떠넘기는 버릇이야 하루 이틀 일이 아니지만 이건 해도 해도 너무했다.

‘아무리 그래도 이 정도는 아니었던 것 같은데.’

어느 날부터 애첩 하나를 들이더니 벌써 수년째 여색에 빠져 공무는 뒷전이다.

내심 한숨을 푹 내쉰 호위장이 힘없이 군례를 취했다.

“……성주님의 명을 받들겠습니다.”

“당연히 그래야지. 그럼 수고하라고. 난 바쁜 용무가 있어서 이만.”

그제야 만족스럽게 고개를 끄덕인 사천성주가 자리에서 일어났다.

과도한 체중 탓에 가쁜 숨을 내쉬며 멀어지는 그의 뒷모습을 바라보던 호위장이 개미만 한 목소리로 중얼거렸다.

“바쁜 용무는 무슨. 또 애첩이나 안으러 가겠지.”

호위장의 예상은 적중했다. 대전을 떠난 사천성주가 가장 먼저 찾은 곳은 바로 화려하게 치장된 침소였다.

“애향아! 애향아!”

어지간한 방보다 큰 비단 침상 위, 반나체로 누워 있던 미녀가 몸을 일으켰다.

“가가(哥哥). 왜 이제야 오셨어요? 애향이가 얼마나 기다렸는데.”

“그, 그랬느냐?”

새치름한 눈매에 한 번, 이불 사이로 슬쩍슬쩍 보이는 새하얀 살결에 두 번 넋이 나간 사천성주의 입이 헤벌쭉 벌어졌다.

“미안하구나. 호위장이 귀찮게 구는 바람에.”

“또 그 사람이에요? 안 그래도 가가께서 얼마나 바쁘신데 왜 그리 못살게 군대요?”

“그러게나 말이다.”

“이래서 무능력한 아랫것들이 문제예요. 가가께서 없으시면 다들 아무것도 못 하잖아요?”

“역시, 이 가가를 생각해 주는 건 우리 애향이밖에 없다!”

호위장이 들었으면 눈을 까뒤집었을 대화였다.

감동으로 볼살을 부르르 떠는 사천성주를 향해 애첩이 두 팔을 벌렸다.

“이리 오세요, 가가. 고생하셨으니까 이 애향이가 꼭 안아 드릴게요.”

“애향아……!”

사랑하는 애첩의 끈적하고도 고혹적인 눈웃음에, 사천성주의 눈동자가 몽롱하게 풀어졌다.

“세상 천하에 너처럼 아름다운 여인이 있을 수 있단 말이냐!”

삼공(三公)을 배출한 세도가의 핏줄로 태어나 탄탄대로를 걸어온 사천성주다.

마르지 않는 재물을 바탕으로 숱하게 기방을 들락거리며 온갖 미녀들을 품에 안았다.

마음이 혹하면 첩으로 들인 것도 수차례, 그러나 워낙 많은 여인을 만난 탓에 한 해를 버티지 못하고 시들해지고는 했다.

‘하지만 이 아이는 달라!’

맹세코 이런 여인은 처음 보았다. 목소리와 눈빛, 손끝 하나의 움직임까지. 사천성주의 눈에는 애향이의 모든 것이 매혹적이고 사랑스러웠다.

벌써 수년째 보아 온 모습이지만 도무지 질리지 않는다. 아니, 오히려 무서울 만큼 깊숙이 빠져들고 있었다.

“사랑한다. 사랑한다, 애향아!”

막 오십 줄에 접어든 사천성주의 외침은 사랑에 빠진 젊은이의 그것처럼 절절했다.

홀린 듯이 다가가 애첩의 품에 안긴 그는 언제나 그래 왔듯 오늘 하루 있었던 일을 말하기 시작했다. 사천성주에게 있어 애첩은 가장 은밀한 비밀까지 털어놓을 수 있는 유일한 사람이었다.

“……해서, 드디어 그 골칫덩이 무뢰배들이 떠났다.”

“무뢰배들이라면, 그들을 말씀하시는 거죠? 지난번에 찾아왔던 무림인들.”

“그래. 상산왕 전하의 증표를 가져왔던 그자들 말이다.”

“흐음.”

“왜 그러느냐?”

“아니에요, 아무것도. 그나저나 이번 일로 가가께서 고생 많으셨겠다. 들어 보니 무림인들끼리 시비가 붙어서 많은 사람이 죽고 다쳤다면서요?”

사천성주가 질린 얼굴로 고개를 내저었다.

“말도 말거라. 어디서 구했는지 감히 관군의 복식까지 훔쳐 입고 대국의 질서를 어지럽히다니.”

“어머, 정말요?”

“믿기지 않겠지만 사실이다. 내 다른 건 몰라도 그에 관해서는 반드시 조정에 장계를…….”

“어쩜 이리 대장부 같으실까. 그런데 가가.”

싱긋 웃은 애첩이 무릎에 얹힌 사천성주의 머리를 쓰다듬었다.

“황실에서 알게 된다면 일이 커지지 않을까요?”

“으, 응?”

“그렇잖아요. 언젠가는 가가께서도 삼공(三公)의 지위에 올라 문무백관을 거느리며 황상을 보필하실 텐데…… 소첩은 가가를 시기하는 무리가 이번 일을 문제 삼지는 않을까 걱정이 되어요.”

“허허. 역시 날 이만큼 생각해 주는 것은 애향이, 너밖에 없구나.”

사천성주는 애정이 뚝뚝 묻어나는 눈빛으로 자신의 애첩을 바라보았다.

그러나 그 역시 아주 얼간이는 아니었다.

비록 관과 무림이 서로를 소 닭 보듯 하는 상호 불가침의 영역이라고는 하지만, 지난 칠 주야 동안 천 명이 훌쩍 넘는 사람들이 사천 땅 곳곳에서 죽어 나갔다.

자질구레한 뒤처리는 아랫놈들에게 떠넘기더라도 최소한 이것만큼은 직접 나서야 한다.

“네 마음씨가 갸륵하나, 지금처럼 큰 사안은 오히려 숨길수록 문제가 되기 마련이다.”

“가가도 참. 제가 그걸 모를 것 같아요?”

“음? 그럼 어쩌자는 것이냐?”

“숨길 건 숨기고, 공은 부풀려야죠.”

교태 가득한 목소리가 사천성주의 귓가를 간지럽혔다.

“무림인들 간에 큰 분쟁이 있었고, 가가께서 휘하의 관군을 움직여 이 사태를 진정시킨 것으로.”

“으음.”

“가가께서는 무뢰배들의 손에 어지럽혀진 대국의 질서를 바로 세우고, 민초들을 보살핀 어진 성주가 되시는 거예요. 물론 관의 무기와 의복에 관한 이야기는 빼놓는 게 좋겠죠? 오해를 살 수도 있으니까.”

“애향이 네 말대로만 된다면 좋겠지만. 아무리 그래도 장계를 거짓으로 꾸며 올리기에는 좀…….”

“가가, 절 보세요.”

머뭇거리던 사천성주는 흑요석처럼 아름답게 반짝거리는 눈동자를 보고 외마디 탄성을 흘렸다.

“아.”

“이 애향이를, 가가를 사모하는 제 뜻을 모르시나요?”

“그것이, 그러니까…….”

사천성주는 말을 잇지 못했다.

애첩과 눈이 마주친 순간, 이미 머릿속은 텅 비워진 지 오래였다.

고혹적인 자태에 가슴이 떨리고 꽃향기 같은 채취에 정신이 아득해진다.

어디에선가 불쑥 솟구친 무한한 신뢰와 애정, 그리고 참을 수 없는 욕망이 그를 지배했다.

“애향아, 애향아!”

간절한 목소리. 하지만 애첩은 자신의 몸을 더듬어 오는 사천성주의 손길을 붙잡았다.

“가가, 대답은요?”

“다, 당연히 네 뜻에 따르마. 너를 위해서라면 내 무엇이든 하겠다!”

애첩의 입가에 맺힌 웃음이 짙어졌다.

“잘하셨어요. 지금까지 그랬던 것처럼, 앞으로도 그렇게 하시면 되는 거예요. 아셨지요?”

“응, 응!”

강렬한 욕망에 사로잡힌 사천성주는 미처 볼 수 없었다.

자신이 그토록 사랑하는 애첩의 눈동자에 요사스러운 붉은빛이 스며드는 불길한 광경을.

“아이, 착해라. 우리 성주님. 말도 잘 듣네.”

애첩은 소리 내어 깔깔 웃었다.

모든 것은 그녀가, 아니 그분이 원하는 방향으로 흘러가고 있었다.



* * *



“음?”

“왜 그러세요?”

“아니, 방금 무슨 미친년 웃는 소리를 들은 것 같아서.”

“미친년이요? 여기서요?”

“응. 쎄하더라고.”

나와 혁무진은 주위를 둘러봤다. 드넓은 장강의 지류, 수룡채의 깃발을 내건 세 척의 쾌조선은 막힘없이 나아가고 있었고 당연하지만 그중 어디에도 여인은 없었다.

“잘못 들었나? 이상하네.”

요새 온갖 일을 다 겪었더니 이제 환청이 다 들리나.

고민하는 내게 혁무진이 심각한 얼굴로 입을 열었다.

“혹시 그…….”

“그, 뭐?”

“앞줄 우측 네 번째에 서 있던 소저를 잊지 못하신 것 아닙니까?”

궁기방이 고개를 저었다.

“헛소리. 좌측 세 번째야. 그 정도면 잊지 못할 미모지.”

“아, 뭔가 했더니 그 이야기였어?”

나는 인자하게 웃으며 두 녀석을 바라보았다.

“내 생각에는, 오늘이 너희 둘한테 잊지 못할 하루가 될 것 같은데.”

환히 웃는 얼굴로 손짓하자 그걸 보고 달려온 건장한 수적 여럿이 굽신굽신 고개를 조아렸다.

“부르셨습니까요, 진 대협.”

“혹시 쇤네들에게 뭐 시키실 일이라도.”

“저 새끼들 붙잡아서 장강에 찍먹 해 주세요.”

수적들이 어리둥절한 얼굴로 되물었다.

“어, 찍먹이라 하셨습니까?”

“죄송하지만 저희가 원체 무식한 놈들이라. 당최 찍먹이 무엇입니까?”

“찍먹은 올바른 문화……가 아니라, 그냥 제가 멈추라고 할 때까지 계속 머리통만 담갔다가 빼 주시면 됩니다.”

“아아, 예.”

“쉽구먼요.”

“자, 잠깐만!”

“조장님!”

궁기방과 혁무진은 저항하려 했지만 턱도 없는 일이었다.

한 놈은 다리 한 짝만 멀쩡하고, 다른 한 놈은 전신이 붕대로 감겨 있었으니까.

무공을 익힌 건장한 떡대들이 우르르 몰려와 사지를 붙들고 찍먹쇼를 시작하는 사이, 나는 앞서 허공에 띄워 둔 시스템창을 바라봤다.



- 아직 이름을 정하지 않은 종속 아이템이 있습니다. 확인하시겠습니까?



‘당연히 예스.’

띠링.



아이템창



[???]

종류 : 방어구

등급 : 신병이기

제한 : 진태경

설명 : 이름 모를 고대 야장의 혼이 깃든 갑옷. 실로 가공할 만한 방어력을 지녔으며, 현재는 전 주인이 사망함으로써 새로운 주인에게 소유권이 종속되었다. 이름을 지어 주면 어디에서나 자유롭게 사용할 수 있다.





‘전 주인이 사망해서 소유권이 종속되었다고?’

설마 했는데, 내가 생각하는 그 물건이 맞는 것 같다.

나는 인벤토리를 탈탈 털어 본 끝에 새로운 종속 아이템을 확인할 수 있었다. 그리고 저절로 흘러나오는 김빠진 소리.

“……에게?”

손바닥 위에 올려진 그것은 자그마한 파편에 불과했다. 본래는 흑룡갑(黑龍鉀)이라 불리던 물건이기도 했다.

‘분명히 마지막에 일섬으로 서천마군, 그놈과 함께 날려 버렸는데. 종속 아이템이라 인벤토리에 자동으로 들어온 건가.’

흑룡갑이 산산조각 나던 광경이 아직도 눈앞에 선하다.

그런데 겨우 이만한 파편으로 뭘 어떻게 하라는 건지 모르겠네.

‘팬티 앞부분에 넣어 두면 세상 든든하긴 할 것 같은데.’

아, 혹시 이래서 방어구인 건가.

슬쩍 바지 앞섬을 잡아당겨 적절한 위치를 살피던 그때였다.

“거기서 뭐 하…….”

“……아.”

순간 내려앉은 싸늘한 침묵.

풀어진 바지춤과 그 안에 쑥 들어간 내 손을 본 소년의 얼굴이 딱딱하게 굳는다.

주위에 아무도 없는 것을 확인한 쌀성, 아니 문경이 입을 열었다.

“이걸 하필, 여기서?”

“아니, 잠깐만. 이거 오해가 좀 있는 것 같은데요.”

내가 황급히 변명하려던 찰나, 문경의 눈빛이 착 가라앉았다.

“출발할 때 말했을 텐데. 화왕과 청풍을 제외한 다른 사람 앞에서는 문경으로 대하라고.”

나는 억울한 얼굴로 대답했다.

“너도 지금 반말하고 있잖아, 새꺄.”

“……!”

“아, 죄송.”

만감이 교차하는 표정을 짓던 문경이 근처로 다가온 수적들을 곁눈질하며 혀를 찼다.

무시무시한 살성이 신의의 제자이자 밝은 소년 의생의 모습으로 변하는 것은 순식간이었다.

“뭐 하고 계셨어요?”

“네가 알아서 뭐 하게.”

“……!”

이거 은근히 재밌네. 그런데 세 번은 못 하겠다.

나는 말문이 막힌 문경을 향해 얼른 손을 내밀었다.

“이게 바지춤에 들어가서.”

물론 사실과는 살짝 괴리감이 있지만, 문경은 그런 것 따위는 신경 쓰지 않았다. 정확히 말하자면, 흑룡갑의 파편에 시선이 고정되어 있었다.

“이건…….”

“혹시 아시는 물건. 아니, 아는 물건이냐?”

“어디서 얻었습니까?”

“그놈에게서.”

서천마군을 뜻한다는 것을 알아들은 문경이 고개를 끄덕였다.

“신병이기(神兵利器)를 얻으셨군요. 어쩌다가 파편만 남았는지는 모르겠지만.”

“놈은 이걸 흑룡갑이라고 부르던데.”

“흑룡갑?”

“왜, 알고 있던 이름이랑 달라?”

“오래된 비사(祕史)에서 읽은 적이 있습니다. 정해진 이름이 없으며, 소유자에 따라 형태와 성질이 바뀐다는 신비한 갑옷에 대한 이야기를.”

“형태와 성질이 바뀐다고? 어떻게?”

문경은 한심하다는 눈빛으로 대답을 대신했다. 그리고 나는 그제야 지금부터 무엇을 해야 할지 깨달았다.

‘공력.’

공력이야말로 소유자가 지닌 형태와 성질, 그 자체다.

스아아아.

팔 성에 오른 열화신공의 구결에 따라 용암 같은 기운을 흑룡갑의 파편을 향해 흘려보냈다.

파편의 표면에 감돌던 묵색 기운이 사라지고, 빈자리를 청백색의 열양지기가 채웠다.

불꽃이 이글거리는 듯한 문양이 새겨진 그것은, 더 이상 흑룡갑이라 부를 수 없는 물건이었다.

‘화룡갑(火龍鉀).’

단순하지만 이보다 적절한 이름은 존재하지 않을 것이다.

내가 만족스러운 미소를 머금음과 동시에 경쾌한 종소리가 울려 퍼졌다.

띠링.



- 당신은 종속 아이템, [???]에게 새로운 이름을 부여했습니다!

- 지금부터 [화룡갑]을 어디에서나 자유롭게 사용할 수 있습니다!

- [화룡갑]이 당신의 기운과 공명합니다! 스스로 파손 부위를 복구하기 위해 소유자의 힘을 원합니다!



쏴아악.

느껴진다. 체내로부터 빠져나간 막대한 공력이 화룡갑을 향해 몰려드는 것이.

나는 스펀지처럼 공력을 빨아들인 그것을 품에 넣는 척, 인벤토리에 수납했다.

‘자동 복구라, 끝내주는데.’

확실히 쓸모있는 물건을 얻었다.

다행이다. 이번 여정에서 얻은 마지막 선물이 화룡갑이라서.

돌아서려는 나를, 문경이 눈을 크게 뜨고 바라봤다.

“어딜 가느, 가십니까?”

“네가 알아서 뭐 하게.”

“……!”

아, 이거 어쩐지 중독 될 것 같아.

나는 속으로 ‘참을 인’ 자를 되새기고 있을 문경에게 손을 흔들어 주었다.

“한숨 자러 간다. 깨우지마라.”

“……?”

그래, 이제는 오랜 잠에서 깨어날 때다.

그런데…….

‘왜 이렇게 찝찝하지? 뭘 잊었나?’

갸웃거리며 쾌조선의 선실에 자리를 잡고 누운 나는 눈을 감았다. 깊이 심호흡하며 명령어를 외쳤다.

‘로그아웃.’

띠링.



- 10초 후 로그아웃합니다. 십, 구, 팔, 칠…….



마지막 카운트와 함께, 어디선가 물장구 소리와 누군가의 외침이 아련하게 귓가를 파고들었다.

첨벙, 푸하! 조장님, 살려, 푸하!
```

## Current accepted English baseline

```markdown
# Chapter 377

“They’ve left?”

The guard captain answered the tense question from the plump middle-aged Sichuan Governor.

“Yes. The fast ship belonging to the Yangtze River Channel League departed one sikgyeong ago.[^1]”

“Pheeeeew.”

The Sichuan Governor let out a deep sigh of relief, his belly wobbling, and waved a hand.

“All right, you may withdraw. If you hear anything related to the martial artists, report it to me immediately.”

“Understood. But the troops stationed near Chengdu…”

The Sichuan Governor frowned.

“Listen, Guard Captain.”

“Yes?”

“Do I have to concern myself with every little detail? Handle that kind of cleanup among yourselves. Consult the Provincial Military Commissioner—that stubborn bastard—if you have to. Hmm?”

“…”

The Guard Captain was speechless inside.

*Was that supposed to be an order or a fart?*

The governor’s incompetence and habit of dumping work on his subordinates were nothing new, but this was too much even for him.

*Even so, I don’t remember him being this bad.*

Several years ago, he had taken a favorite concubine, and ever since then, he had been so consumed by women that official duties had become an afterthought.

The Guard Captain sighed inwardly and weakly performed a military salute.

“…I will carry out Your Excellency’s order.”

“Of course you will. Then get to work. I have an urgent matter to attend to, so I’ll be going.”

Only then did the Sichuan Governor nod with satisfaction and rise from his seat.

The Guard Captain watched his back recede as he walked away, panting from his excessive weight. Then he muttered in a voice as tiny as an ant.

“Urgent matter, my ass. He’s just going to embrace his favorite concubine again.”

The Guard Captain’s prediction was accurate. The first place the Sichuan Governor visited after leaving the main hall was an extravagantly decorated bedroom.

“Ae-hyang! Ae-hyang!”

A beautiful woman lying half-naked on a silk bed larger than most rooms sat up.

“My dear. Why did you take so long? Ae-hyang has been waiting for you.”

“Y-You have?”

The Sichuan Governor was dazed once by her coy eyes and twice by the dazzling white skin that peeked out from between the blankets. His mouth fell open in a foolish grin.

“I’m sorry. The Guard Captain was bothering me.”

“That man again? You’re already so busy, my dear. Why does he keep giving you such a hard time?”

“Exactly.”

“That’s the problem with incompetent underlings. They can’t do anything without you, can they?”

“As expected, you’re the only one who truly cares about me, Ae-hyang!”

The Guard Captain would have rolled his eyes if he had heard the conversation.

The favorite concubine opened both arms toward the Sichuan Governor, whose cheeks trembled with emotion.

“Come here, my dear. You’ve worked so hard. Let Ae-hyang hold you.”

“Ae-hyang…”

At the sight of his beloved concubine’s sultry, alluring smile, the Sichuan Governor’s eyes grew hazy.

“Could there truly be a woman in all the world as beautiful as you?”

The Sichuan Governor had been born into a powerful family that had produced Grand Councilors, and his path through life had always been smooth.

Backed by inexhaustible wealth, he had frequented pleasure quarters and held countless beautiful women in his arms.

He had taken several of them as concubines whenever they caught his fancy. But because he had met so many women, he always lost interest before a year had passed.

*But this girl is different!*

He swore he had never seen a woman like her. Her voice, her eyes, even the smallest movement of her fingertips—everything about Ae-hyang was captivating and lovable in his eyes.

He had been seeing her for years, yet he had never grown tired of her. No—if anything, he was sinking deeper into her grasp, to a frightening degree.

“I love you. I love you, Ae-hyang!”

The Sichuan Governor was just entering his fifties, but his cry was as heartfelt as that of a young man who had fallen in love.

He approached her as if possessed and nestled into her arms. As he always did, he began telling her about everything that had happened that day. To the Sichuan Governor, his favorite concubine was the only person to whom he could reveal even his most private secrets.

“…And so, those troublesome rogue bastards finally left.”

“By rogues, you mean them, right? The martial artists who came here last time.”

“That’s right. The ones carrying His Highness the King of Shangshan’s token.”

“Hmm.”

“What is it?”

“Nothing. Anyway, you must have had a hard time because of this. I heard that the martial artists got into a dispute and many people were killed or injured.”

The Sichuan Governor shook his head with a disgusted expression.

“Don’t remind me. They dared to steal government uniforms and wear them, throwing the order of the empire into chaos.”

“Oh my, really?”

“It may be hard to believe, but it’s true. Whatever else I may overlook, I will certainly submit a memorial to the court about that…”

“How gallant of you. But, my dear…”

The concubine smiled sweetly and stroked the Sichuan Governor’s head where it rested on her lap.

“Wouldn’t it become a serious matter if the imperial court found out?”

“Huh?”

“Think about it. One day, you will rise to the position of a Grand Councilor, command all the civil and military officials, and assist His Majesty… I’m worried that the factions jealous of you might use this incident against you.”

“Ha ha. As expected, you’re the only one who cares about me this much.”

The Sichuan Governor gazed at his concubine with overflowing affection.

But he was not a complete fool.

Though the government and the Murim treated each other as they would a cow and a chicken, maintaining mutually inviolable spheres, more than a thousand people had died throughout Sichuan over the past seven days and nights.

He could dump the minor cleanup on his subordinates, but he needed to handle at least this much himself.

“Your concern is touching, but the more one tries to hide an important matter like this, the worse the problem becomes.”

“Oh, my dear. Do you think I don’t know that?”

“Hmm? Then what do you suggest?”

“Hide what needs to be hidden and exaggerate your achievements.”

Her coquettish voice tickled the Sichuan Governor’s ear.

“There was a major conflict among the martial artists, and you mobilized the government troops under your command to calm the situation.”

“Hmm…”

“You’ll become a wise governor who restored the empire’s order after it was thrown into chaos by a group of rogues and cared for the common people. Of course, it would be best to leave out anything about the government weapons and uniforms, don’t you think? They might cause a misunderstanding.”

“It would be nice if everything went as you said, Ae-hyang. But even so, submitting a false memorial feels a little…”

“My dear, look at me.”

The hesitating Sichuan Governor let out a short exclamation when he saw her eyes glittering beautifully like obsidian.

“Ah.”

“Don’t you understand Ae-hyang’s feelings? Don’t you understand how much I adore you?”

“I… I mean…”

The Sichuan Governor could not continue.

The moment his eyes met hers, his mind had already been emptied.

His heart trembled at her bewitching figure, and the floral scent of her body made his thoughts swim.

Boundless trust and affection that had surged up from somewhere, along with unbearable desire, seized control of him.

“Ae-hyang, Ae-hyang!”

His voice was desperate, but the concubine caught the Sichuan Governor’s hand as it wandered over her body.

“My dear, what is your answer?”

“O-Of course I’ll do as you wish. I would do anything for you!”

The smile at the corner of the concubine’s mouth deepened.

“Good. Just keep doing that, as you have until now. Understood?”

“Yes, yes!”

The Sichuan Governor, consumed by fierce desire, failed to notice.

A sinister red light had begun to seep into the eyes of the concubine he loved so dearly.

“Oh, what a good boy. Our governor listens so well.”

The concubine burst into loud laughter.

Everything was proceeding exactly as she—or rather, the one above her—desired.

* * *

“Hmm?”

“What’s wrong?”

“I thought I just heard some crazy bitch laughing.”

“A crazy bitch? Here?”

“Yeah. It gave me the creeps.”

Hyuk Mujin and I looked around. Three fast ships flying the flag of the Water Dragon Stronghold were gliding smoothly along the broad tributary of the Yangtze, and naturally, there wasn’t a woman anywhere among them.

“Did I hear wrong? That’s strange.”

*After everything I’ve been through lately, am I hallucinating now?*

As I pondered the matter, Hyuk Mujin spoke with a serious expression.

“Could it be that…”

“That what?”

“Perhaps you still cannot forget the young lady standing fourth from the right in the front row?”

Gung Gibang shook his head.

“Nonsense. It was the third from the left. Anyone would be unable to forget a beauty like that.”

“Oh, that’s what this was about?”

I smiled benevolently at the two of them.

“I think today is going to be an unforgettable day for you two.”

I waved them over with a bright smile. Several burly river bandits came running over and bowed repeatedly.

“Did you call for us, Great Hero Jin?”

“Is there something you want us humble men to do?”

“Grab those two bastards and give them a dip in the Yangtze.”

The river bandits looked bewildered.

“Uh, did you say a dip?”

“We’re ignorant fellows, you see. What exactly is ‘dip’?”

“Dipping is the civilized way… No, forget that. Just keep dunking their heads in and pulling them out until I tell you to stop.”

“Oh, yes.”

“Easy enough.”

“W-Wait!”

“Squad Leader!”

Gung Gibang and Hyuk Mujin tried to resist, but it was utterly futile.

One of them had only one good leg, while the other was wrapped in bandages from head to toe.

As a group of burly martial artists swarmed over, seized their limbs, and began the great dunking show, I looked at the System window I had already left floating in the air.

> **System**
>
> You have an unnamed bound item. Would you like to inspect it?

*Obviously, yes.*

A cheerful chime rang out.

> **System**
>
> **Item Window**
>
> **???**
>
> **Type:** Armor  
> **Grade:** Divine Weapon  
> **Restriction:** Jin Taekyung  
> **Description:** Armor imbued with the spirit of an unknown ancient blacksmith. It possesses truly formidable defensive power. With the death of its previous owner, ownership has become bound to a new owner. Once given a name, it can be used freely anywhere.

*Its ownership became bound because the previous owner died?*

I had suspected as much, but it seemed that this really was the object I thought it was.

After turning my inventory upside down, I finally found the new bound item. A flat, deflated sound escaped my lips.

“…Huh?”

The object resting on my palm was nothing more than a tiny fragment. It had originally been called Black Dragon Armor.

*I definitely blew it away with that bastard, the Western Heaven Demon Lord, in the final slash. Did it automatically enter my inventory because it was a bound item?*

The sight of the Black Dragon Armor shattering into pieces was still vivid before my eyes.

But I had no idea what I was supposed to do with a fragment this small.

*It would certainly make me feel secure if I tucked it into the front of my underwear.*

Ah. Maybe that was why it was classified as armor.

I was tugging at the front of my pants and inspecting a suitable position when—

“What are you doing th—”

“…Ah.”

A chilly silence descended in an instant.

The boy’s face stiffened when he saw my loosened waistband and the hand thrust inside it.

After making sure there was no one nearby, the Slaughter Saint—no, Mungyeong—spoke.

“Why here, of all places?”

“Wait a second. I think there’s been a misunderstanding.”

Just as I hurriedly began to make excuses, Mungyeong’s gaze turned cold.

“I told you when we departed. In front of anyone other than the Fire King and Cheongpung, you are to address me as Mungyeong.”

I answered with an aggrieved expression.

“You’re speaking casually to me right now too, you bastard.”

“…!”

“Oh. Sorry.”

Mungyeong wore an expression of conflicting emotions as he glanced sideways at the river bandits approaching nearby and clicked his tongue.

The terrifying Slaughter Saint transformed into the Divine Physician’s Disciple—a cheerful young physician-in-training—in an instant.

“What were you doing?”

“What business is it of yours?”

“…!”

*This is surprisingly fun. But I don’t think I can do it three times.*

I quickly held out my hand toward the speechless Mungyeong.

“This got into the front of my pants.”

That was slightly at odds with the truth, of course, but Mungyeong did not care about such details. More precisely, his eyes were fixed on the fragment of the Black Dragon Armor.

“This is…”

“Do you happen to know this? No—do you know it?”

“Where did you get it?”

“From that bastard.”

Mungyeong understood that I meant the Western Heaven Demon Lord and nodded.

“You obtained a divine weapon. Though I do not know how only a fragment remained.”

“He called it Black Dragon Armor.”

“Black Dragon Armor?”

“Why? Is that different from the name you knew?”

“I read about it in an old secret history. It was a mysterious armor with no fixed name, said to change its form and properties according to its owner.”

“It changes its form and properties? How?”

Mungyeong answered with a look that said I was hopeless. Only then did I realize what I needed to do next.

*Internal energy.*

Internal energy was the very form and nature possessed by its owner.

Whoooosh.

Following the formula of the Blazing Flame Divine Art, which had reached its eighth stage, I sent magma-like energy toward the fragment of the Black Dragon Armor.

The ink-dark energy swirling across the fragment’s surface disappeared, and bluish-white Scorching Yang Qi filled the empty space.

Engraved with patterns that seemed to writhe with blazing flames, it was no longer something that could be called Black Dragon Armor.

*Flame Dragon Armor.*

It was a simple name, but there could be no more suitable one.

At the same moment that I smiled with satisfaction, a bright chime rang out.

> **System**
>
> You have given the bound item ??? a new name!
>
> From now on, you can freely use Flame Dragon Armor anywhere!
>
> Flame Dragon Armor is resonating with your qi! It requires its owner’s power to repair its damaged sections by itself!

Whoosh.

I could feel it. A massive amount of internal energy was leaving my body and rushing toward the Flame Dragon Armor.

I pretended to tuck it into my robes and stored it in my inventory instead.

*Automatic repairs? That’s incredible.*

I had certainly obtained something useful.

*Thank goodness the final gift of this journey was the Flame Dragon Armor.*

As I turned away, Mungyeong stared at me with wide eyes.

“Where are you go—going?”

“What business is it of yours?”

“…!”

This was strangely addictive.

I waved at Mungyeong, who I knew was silently repeating the character for patience.

“I’m going to get some sleep. Don’t wake me.”

“…?”

Yes. It was time to wake from a long sleep.

But…

*Why do I feel so uneasy? Did I forget something?*

I tilted my head, then found a place in the cabin of the fast ship and lay down. I closed my eyes, took a deep breath, and called out the command.

*Logout.*

A chime rang out.

> **System**
>
> Logging out in 10 seconds. Ten, nine, eight, seven…

With the final count, the sound of splashing and someone’s cries faintly pierced my ears from somewhere.

Splash, gasp! Squad Leader, save me! Gasp!

[^1]: A sikgyeong was the time required to eat a meal, conventionally treated as roughly thirty minutes.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 377`.

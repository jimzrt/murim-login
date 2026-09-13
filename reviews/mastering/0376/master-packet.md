# Master Edit Task — Chapter 376

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
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 소저      | **Young Lady**                                                  |
| 궁기방 | **Gung Gibang** | Young beggar and Future Beggar Chief. |
| 문경 | **Mungyeong** | Young Disciple of the Divine Physician overseeing Jin Taekyung's care. |
| 사천당문 | **Sichuan Tang Clan** | The Tang family and clan of Sichuan |
| 미미 | **Mimi** | Tang Sadok's snake and longtime companion; temporarily entrusted to Cheongpung. |
| 동봉 | **Dongbong** | Name or designation associated with the Divine Physician. |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 화산신룡 | **Huashan Divine Dragon** | Epithet used for Jin Taekyung. |
| 열화신룡 | **Blazing Fire Divine Dragon** | New epithet acquired by Jin Taekyung. |
| 홍무 | **Hongwu** | Era name beginning when the civil war ends and a new emperor ascends. |
| 성도 | **Chengdu** | City whose western port is the departure point. |
| 선화아 | **boatman** | Nautical title used for Mu Song. |
| 무송 | **Mu Song** | Bronze-skinned boatman associated with the water bandits. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 혁무진 | 궁기방 | orthodox_ally_to_orthodox_ally | Young Hero Gung | blunt-but-formal | Uses 궁 소협 while teasing Gung Gibang about his injuries. |
| 혁무진 | 청풍 | junior_ally_to_younger_ally | Young Hero Cheong | formal-but-bewildered | Uses 청 소협 when reacting to Cheongpung's warning. |
| 혁무진 | 진태경 | subordinate_to_squad_leader | Squad Leader | deferential | Calls Taekyung 조장님 when announcing his awakening. |
| 궁기방 | 진태경 | squadmate_to_squad_leader | Jin Taekyung | familiar-but-direct | Calls Taekyung by name when he wakes. |
| 진태경 | 적천강 | disciple_to_elder_master | Old Man | casual-but-affectionate | Uses 노야 while thanking Jeok Cheongang. |
| 적천강 | 문경 | orthodox_elder_to_younger_orthodox_elder | Wen | hostile-but-blunt | Jeok Cheongang addresses Mungyeong as 문가 while intervening on Taekyung's behalf. |
| 진태경 | 문경 | ally_to_secret_identity_holder | Mungyeong | casual-but-teasing | Taekyung accepts the requested name and deliberately uses it in a familiar vocative. |
| 동봉 | 문경 | disciple_to_master | Master | deferential | Dongbong repeatedly addresses Mungyeong as 스승님 after affirming his identity as the Divine Physician. |
| 무송 | 진태경 | older_ally_to_junior_ally | junior | deferential-but-uncertain | Mu Song switches from junior to Young Hero Jin and Great Hero before Taekyung tells him to use junior. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |

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

#### Chapter 375 tail (verified mastered)

…
even greater courage. That is forgiveness. > > **Hidden Quest:** **Apology and Forgiveness** successfully completed! > > **Level 115 Tang Sadok** expresses his deep gratitude for your kindness. He and the **Sichuan Tang Clan** will never forget the kindness and assistance you showed them today, and the people of the **Sichuan Tang Clan** will remember you as their **Benefactor**! > > **Title Acquired:** **Benefactor of the Tang Clan** > > You have gained a tremendous amount of EXP and Fame as a reward for completing the Hidden Quest! > > **Level Up!** *What was this? A Hidden Quest, all of a sudden?* As I stood there dumbfounded by the System notification that had suddenly rung out, something cold brushed between my legs. Sssrik. Sssriririk. “Mimi, you little……” At the sight of Mimi and Tang Sadok reunited after so long, I remembered something I had momentarily forgotten. “Ah, now that I think about it, the Myriad Poison Ring. Thankfully, I’ve been keeping it safe all this time……” “Is that so?” Tang Sadok cut in before I could finish. “Then continue to keep it.” “Yes, then I’ll keep—what?” “I am entrusting our family’s sacred artifact to you. It is a token of gratitude for our Benefactor, so please do not refuse.” > **System** > > According to the owner’s wishes, **Myriad Poison Ring** has been transferred to you! > > A new item is now bound to you! > > **Currently bound items:** **White Flame**, **Myriad Poison Ring**, **???** > > You have a bound item that has not yet been named. Please give it a new name. *What kind of day was today?* I was getting downright nervous, wondering what kind of shitty things were about to happen for them to be giving so much away like this. At the sight of me opening and closing my mouth like a goldfish, Tang Sadok smiled faintly. “If any of you desire something, speak. I will grant anything within our family’s power.” The Divine Physician smiled along with him. “If there is something I desire, it is simply for the patients to recover as soon as possible.” “Good heavens.” That was certainly an answer worthy of the Divine Physician. No, should I be calling him Dongbong now? But one thing was certain: he, too, was another Divine Physician. “What do you want?” Cheongpung jumped at the sudden question. “M-Me?” Tang Sadok nodded, and Cheongpung answered while fidgeting with his hands and feet. “Well, I… Let me think. Um. Nothing.” “Are you sure?” “Yeees. I don’t think there’s anything.” “……” “……” *Hey, you idiot. Take your eyes off Mimi-chan and talk.* I wanted to bring him a mirror and show him his own face. His eyes brimmed with aching longing and desire for Mimi-chan. *At this rate, he’s going to stare a hole through the snake’s hide.* Just then, Tang Sadok spoke. “This creature is an old friend of mine. For the past several decades, she has been the only one with whom this old man could share the joy, anger, sorrow, and pleasure he could reveal to no one else.” Cheongpung looked at Tang Sadok with pity. “So you don’t have any other friends, Grandpa Tang.” “I never made any. Being the Family Head of the Tang Clan was that kind of position.” “So you have no friends.” “It wasn’t that I had none. I could have made them, but……” “You didn’t have a single friend. How pitiful.” “……” The Divine Physician hurriedly grabbed Tang Sadok by the shoulders. “Family Head, calm down. You’re breathing too quickly!” “Huuk, hoo-oo.” “Take deep, slow breaths. Come on, follow me. One, two……” “Huooooo……” A little while later, after narrowly escaping a hypertensive crisis, Tang Sadok looked at Cheongpung and spoke again. “But as for Mimi, perhaps you……” Cheongpung covered his mouth with both hands. “No, Grandpa Tang. I can’t take away your only friend.” “……I haven’t said I’m entrusting her to you yet.” “Oh. Oh!” Tang Sadok let out a deep sigh. It had only been for a moment, but he had undoubtedly wondered whether he could entrust Mimi-chan to someone like that. “Yes, just as you guessed. Since we do not know what path our family will take from here on, I wish to entrust Mimi to you. Temporarily, of course.” “Yaaay!” “Did you hear the last part? Temporarily.” “Yaaay!” *I’ll bet Hyuk Mujin’s right wrist that he didn’t.* Now Mimi’s temporary guardian, Cheongpung was beside himself with joy. “Don’t worry. I’ll take good care of her!” “From what I saw last time, Mimi does seem fond of you, but she is temperamental by nature and extremely wary of strangers, so……” “Mimi. Do Whirlwind, then spin round and round and say hello!” Sssriririk! “Holy shit.” *He busted out a new trick right here.* Jin Wikyung, half stunned by the sight he was seeing for the first time in his life, muttered in a dazed voice. “It seems you have nothing to worry about, Family Head.” An earthquake shook Tang Sadok’s eyes. Tang Sadok asked Jin Wikyung to stay behind for a private conversation, while Cheongpung and I left the room first. No, one person had just been added. “Young Hero Jin. Could you spare this old man a little of your time?” “Me?” The Divine Physician nodded with a gentle smile. “There is something I very much wish to ask of you before you leave.”

## Korean source

```text
＃376화



인산인해(人山人海).

그렇게밖에 표현할 수 없는 광경이었다.

산서잠룡, 아니 열화신룡 진태경과 화산신룡 청풍이 떠난다는 소식을 들은 사람들이 구름처럼 모여들었기 때문이었다.

비단 무림인뿐만 아니라 겁 없는 양민들까지 더해지니, 배웅에 나선 인파는 꼬리에 꼬리를 물고 늘어져 셀 수가 없었다.

“잘 가시오! 열화신룡!”

“사천 무림은 그대들을 잊지 않을 거요!”

“뿔 달린 뱀이다! 화산신룡이 뿔 달린 뱀을 갖고 있다!”

“헉, 뱀이 공중제비를 돌았다!”

“화왕! 화왕이 뱀을 붙잡아서 태우려고 하고 있다!”

웅성거리는 소음이 행렬을 따라 서서히 멀어져 간다.

그리고 아무도 찾지 않는 언덕 위, 나무 그루터기에 앉아 모든 광경을 지켜보고 있던 소년이 문득 입을 열었다.

“멀리도 왔구나.”

“그러게 말입니다. 힘이 드는군요.”

거친 숨소리와 함께 풀밭에 털썩 주저앉는 늙은 제자의 모습에 소년, 문경은 중얼거렸다.

“……참으로 멀리도 왔어.”

거리를 말하는 것이 아니다. 지금 문경은 지나온 세월을 이야기하고 있었다.

“우리가 처음 만났던 때를 기억하느냐?”

“어찌 잊을 수 있겠습니까.”

늙은 제자는 이마에 맺힌 땀을 훔쳤다. 마치 그날의 따가운 햇볕이 자신에게 내리쬐고 있는 것처럼.

“홍무(洪武) 일 년. 유난히도 무더웠던 그해 여름을.”

황위를 둘러싼 내전이 끝나고 새로운 천자가 즉위한 해였다.

젊고 야심만만한 황제는 연호(年號)를 바꾸고 개혁을 꾀했으나, 기나긴 내전으로 피폐해진 백성들은 천자의 뜻을 받들어 개혁에 동참하기에는 너무나 지쳐 있었다.

“천하 각지에서 반란이 일어나고, 도적이 들끓었지.”

“가뭄이 들고 메뚜기 떼가 평야를 휩쓸었습니다. 관군과 반란군의 시신이 도처에 가득하니 역병이 창궐했지요.”

“그래, 실로 난세(亂世)였다.”

죽음은 또 다른 죽음을 낳았고 이내 대륙을 집어삼켰다.

동씨 성을 쓰는 젊은 목수 역시 천하에 드리워진 어두운 그림자를 피할 수는 없었다.

“지금도 가끔 그때를 생각하고는 합니다.”

수십 년의 세월이 바꿔 놓은 것은 강산뿐만이 아니다. 사랑하는 두 아이와 아내를 역병으로 잃어야 했던 젊은 목수는 어느덧 늙은 의원이 되어 있었다.

“제가 조금만 빨랐더라면, 더 빨리 스승님을 찾았다면 가족들을 살릴 수 있지 않았을까 하는 생각 말입니다.”

“후회하느냐?”

“예.”

하늘과 가까운 언덕에 앉아, 떠다니는 조각구름을 바라보는 늙은 의원의 눈동자는 어느새 젊은 목수의 그것으로 돌아가 있었다.

“이 숨이 붙어 있는 한 평생토록.”

고작 하루 차이였다.

목수가 역병에 걸린 몸을 이끌고 화전민촌에 머무르던 이름 모를 노의원을 데려왔을 때는 모든 것이 늦은 후였다.

그는 꼬박 하루를 울었고 가족들을 묻기 위한 구덩이를 팠다. 그리고 자신이 데려온 의원에게 한 가지 부탁을 했다.

“함께 묻어 주십시오. 제가 그리 청했지요.”

문경이 무뚝뚝한 목소리로 말을 받았다.

“그래서 나는 네 뺨을 때려 주었지.”

“많이 아팠습니다. 죽고 싶을 정도로.”

아팠다. 목숨을 좌지우지하는 고통보다는 사랑하는 아내와 아이들을 더 이상 볼 수 없다는 사실 때문에.

“그런 저를 스승님께서 일으켜 세워 주셨습니다.”

문경은 고개를 저었다.

“손을 내밀었을 뿐이다. 그 손을 붙잡고 일어난 것은 네 의지였어.”

“살아야 했습니다. 해야 할 일이 생겼으니까요.”

본래대로라면 목수 역시 역병으로 죽었어야 할 몸이었다.

그러나 의원은 지금껏 본 적 없는 의술로 그를 완치시켰고, 목수는 처음으로 하늘이 정한 생로병사(生老病死)를 한낱 인간 역시 바꿀 수 있음을 깨달았다.

“아직도 눈앞에 선하구나. 제자로 받아 달라며 무릎을 꿇던 네 모습이.”

“이 제자가 기억하는 것과는 다르군요. 저는 따라오라며 손짓하시던 스승님의 모습이 떠오릅니다.”

그렇게 가족을 잃은 젊은 목수는 새로운 목표를 찾았고, 천하를 주유하며 힘없고 가난한 병자를 보살피던 늙은 의원은 새로운 제자를 얻었다.

이제는 의원이 된 목수, 동봉(童奉)이 스승의 진정한 정체를 알게 된 것은 그로부터 오랜 시간이 흐른 뒤였다.

“살성(殺星)…… 실로 무시무시한 별호입니다. 그때 처음으로 스승님이 낯설게 느껴졌지요.”

문경은 무감각한 시선으로 저 너머를 바라봤다.

지금부터 하려는 말은 그가 자신의 제자에게 단 한 번도 묻지 않았던 내용이었다.

“왜 떠나지 않았느냐?”

“제가 스승님을 떠날 것이라 생각하셨습니까?”

“나는 지금까지 헤아릴 수 없이 많은 목숨을 해쳤다. 과거를 숨긴 추악한 살귀(殺鬼)에 불과했지. 네가 떠난다 해도 이해했을 것이다.”

“정말 그랬을지도 모르지요. 하지만 저는 스승님이 어떤 사람인지 너무나도 잘 알고 있었습니다.”

다음 순간, 나지막한 목소리가 이어졌다.

“신의(神醫). 제 스승님은 신의라 불리는 분입니다. 이유 없는 살생을 저지르실 분이 아닙니다.”

“……!”

문경의 눈동자가 파르르 떨렸다. 그건 지금껏 아무에게도 말하지 않았고, 아무도 인정하지 않으려 했던 사실이었다.

그는 살수로 살아오며 정(正), 사(邪), 마(魔)를 가리지 않고 숱한 목숨을 직접 거둬들였다. 그리고 그들은 하나같이 죽어야 할 이유가 있는 자들이었다.

공명정대함으로 이름 높은 정파의 대협은 여인을 간살하는 취미가 있었고, 어느 사파의 고수는 재미 삼아 촌락 하나를 몰살시켰다.

중원을 침공한 마교의 군세가 닥치는 대로 사람들을 죽이고 파괴를 일삼지 않았다면, 보다 못한 천하제일의 살수가 나서서 악명 높은 마두들을 죽이지 않았다면 그는 살성(殺星)이라 불릴 수 없었을 것이다.

“내가 마교와 싸우지 않았다면, 온 천하가 나를 손가락질했을 것이다. 지금껏 그래 왔던 것처럼.”

살성이라는 별호는 천하 무림의 주인이 된 정파가 그에게 내리는 면죄부이자 강자에 대한 찬사일 뿐이었다.

문경은 늘 문경이었음에도, 사람들은 그 이면에 숨겨진 진실을 알지 못했고 알려고도 하지 않았다.

“어째서 알리지 않으셨습니까?”

“모두 지난 일이다. 나는 무림을 떠나고자 했고, 뜻한 바에 따라 의원이 되었지. 그리고 앞으로도 그럴 것이다.”

문경은 천천히 몸을 일으켰다. 어느새 사천당문을 빠져나간 기나긴 행렬은 저 너머로 사라진 후였다.

“이만 내려가자. 우리를 기다리는 병자들이 있다.”

건조한 목소리와 함께 걸음을 뗀 그 순간이었다.

“곧 거대한 전란(戰亂)이 일어날 것입니다.”

문경의 발걸음이 우뚝 멈췄다. 그의 등 뒤로 늙수그레한 제자의 목소리가 이어졌다.

“그때와 같은 일이 반복될 것입니다. 수많은 이들이 죽고 다치겠지요. 부모와 자식을 잃은 자들이 넘쳐나고, 비명과 죽음이 끊이지 않을 겁니다.”

“……많이 바빠지겠군. 준비를 해 둬야겠어.”

“제가 무슨 말을 하려 하는지, 스승님께서는 알고 계시지 않습니까.”

“알고 싶지 않다.”

“스승님.”

“나는 의원이다. 비록 스스로 약속한 바를 깨고 어쩔 수 없이 살생을 저질렀으나, 두 번 다시 그런 실수는 없을 것이다.”

문경은 천천히 말을 이었다.

“싸우는 것은 저들의 몫이고, 병자를 치료하는 것은 우리의 몫이다. 내 뜻은 이미 무림을 떠난 지 오래다.”

“그렇다면 어찌하여 무공을 놓지 않으셨습니까.”

“……!”

문경은 말문이 막혔다.

그건 스스로가 오랫동안 품고 있던 의문이었다. 살생이 싫어 무림을 떠나고자 했다면, 살생을 위한 수단인 무공 역시 전폐해야 맞았다.

그러나 오히려 그의 무공은 한층 진일보했다. 무공에 대한 끈과 미련을 놓지 못했다는 증거다.

‘그것은 어째서인가.’

짧은 상념을 깨트린 것은 늙은 제자의 목소리였다.

“스승님께서는 수백, 수천의 병자를 치료하실 수 있으십니다. 동시에 수만의 인명을 구할 수 있는 분이기도 하지요.”

“…….”

“살성(殺星)이 아닌 신의(神醫)로서 전란을 막아 주십시오. 이 제자는 이곳에서 병자들을 보살피겠습니다.”

문경은 문득 고개를 들어 하늘을 바라봤다.

맑고 푸르르다. 사천당문이 피로 물들었던 칠 주야 전의 하늘은 먹구름으로 가득했었다.

“하늘이 맑구나.”

무뚝뚝한 목소리와 함께 멈춰 있던 발걸음이 앞으로 나아갔다.

“이만 병자들을 살피러 가 보아야겠다. 천천히 내려오너라.”

언덕을 내려가는 그의 등 뒤로 동봉의 목소리가 흩어졌다.

“술시(戌時). 성도의 서쪽 항구에서 출발한다고 했습니다.”

“부질없는 짓. 내가 있어야 할 곳은 무림이 아니다.”

그러나 서서히 멀어지는 스승의 뒷모습을 바라보는 늙은 제자의 입가에는 희미한 웃음이 맺혀 있었다.

“부디…… 강녕하십시오.”

휘이이잉.

어디선가 불어온 바람이 두 사람의 사이를 스쳐 지나갔다.



* * *



“뭘 그렇게 보고 계세요?”

혁무진의 물음에, 항구를 에워싼 인파를 바라보고 있던 나는 고개를 돌렸다.

“별거 아니다. 그냥 혹시나 해서.”

“그러니까 뭘요?”

“이 자식이, 왜 이렇게 꼬치꼬치 캐물어? 그렇다면 그런 줄 알지.”

내 대답에 혁무진이 의미심장하게 웃었다.

“사실 다 알고 있습니다. 조장님께서 왜 그러시는지.”

“……?”

순간 멈칫했다. 이 자식이 어떻게 그걸 알지? 나와 신의가 나눈 대화는 청풍도 듣지 못했는데.

‘이 녀석 눈치가 이렇게 빨랐나.’

의아해하던 그때, 녀석이 작게 속삭였다.

“저기 앞줄 우측 네 번째에 서 있는 소저를 보고 계셨던 거 아닙니까?”

“…….”

“확실히 예쁘긴 하네요. 제법 있는 집 규수 같아 보이는데. 조장님께서 허락하신다면 오른팔인 제가 슬쩍 가서 따로 자리를…….”

“무진아.”

“예? 아, 혹시 자연스러운 만남을 추구하시는 쪽입니까? 그렇다면…….”

“장강 밑바닥에 가라앉고 싶니?”

“……!”

“개소리하지 말고 계속 거기 누워 있어. 나중에 멀미 난다고 토하지나 말고.”

“……옙.”

조용히 찌그러지는 혁무진의 모습에 궁기방이 킬킬거렸다.

“멍청한 작자 같으니. 우측 네 번째가 아니라 좌측 세 번째 여인이다. 누가 봐도 훨씬 미인인데 눈깔이 삐었군.”

“눈깔 삐꾸 만들어 줘?”

“……미안하다.”

“사람답게 살자. 사람답게.”

한숨과 함께 고개를 내저은 나는 마지막으로 구름처럼 모여 있는 사람들을 쭉 훑었다.

확실히 둘 다 예쁘긴 하지만 궁기방이 말한 좌측 세 번째가 내 스타일…… 아, 이게 아니지.

‘아 씨, 저 자식들이 떠들어 댄 것 때문에 괜히 자꾸 보게 되네.’

그런 생각을 하고 있을 때, 구릿빛 체구의 거한이 내게 다가와 말을 건넸다.

“이보게, 후배. 아니 후배가 아니라 진 소협, 아니 대협.”

뭐야, 버퍼링이야?

나는 번개에 콩 볶듯 호칭을 바꿔 대는 선화아(船火兒) 무송에게 해결책을 제시해 주었다.

“그냥 후배라고 하시죠.”

“커흠. 그, 그래도 되겠나?”

“안 될 건 뭡니까. 전에는 잘만 하시더니.”

“그래도 그, 자네가 워낙 큰일을 해내지 않았나.”

그렇긴 하다. 산서잠룡이라는 지역구 후기지수에서 이제는 전국구 유명인사가 되었으니까.

“그리고 적 대협께서도 나를 좀 별로 마음에 안 들어 하시는 것 같길래…….”

“괜찮아요. 애초에 물을 별로 안 좋아하셔서.”

무송이 힐끔거리는 곳에는 잔뜩 성난 얼굴의 적천강이 있었다.

바로 옆에는 진위경이 뭔지 모를 죽간을 들여다보고 있고, 청풍은 미미에게 새로운 기술을 연습시키고 있었다.

“미미, 파도타기!”

취릭, 촤아아악!

……저거 물뱀이었나.

좀처럼 보기 힘든 진귀한 광경에 잠시 시선을 뺏겼던 무송이 떨떠름하게 입을 열었다.

“어쨌든, 출항 준비는 이미 끝마쳤는데 언제쯤 출발하면 되겠나?”

“혹시 지금 시간이?”

“자네가 말했던 술시가 지났네. 더 어두워지기 전에 출발하는 것이 좋아.”

“……음.”

“혹시 더 올 사람이라도 있는 건가?”

무송의 질문에 잠시 고민하던 나는 고개를 저었다.

“아뇨. 없어요.”

“그럼 출발해도 되겠군.”

“그렇게 하시죠.”

“알겠네.”

무송이 손을 번쩍 치켜올리자 이미 모든 준비를 끝마친 수적들이 일사불란하게 움직였다.

환송을 위해 모여 있던 사람들이 우리를 향해 손을 흔들던 바로 그 순간이었다.

“잠깐, 잠깐만요!”

“정지, 정지!”

항구에서 떨어지려던 쾌조선의 뱃머리가 흔들렸다.

나는 저 멀리, 사람들 사이를 해치며 다가오는 한 소년을 발견하고 피식 웃었다.

“한 사람만 더 태우고 가죠.”
```

## Current accepted English baseline

```markdown
# Chapter 376

A sea of people.

There was no other way to describe the scene.

Word had spread that the Sleeping Dragon of Shanxi—or rather, the Blazing Fire Divine Dragon, Jin Taekyung—and the Huashan Divine Dragon, Cheongpung, were leaving, and people had gathered in clouds.

Not only martial artists, but fearless commoners as well, had come out to see them off. The crowd stretched farther and farther, an endless tail that could not be counted.

“Safe travels, Blazing Fire Divine Dragon!”

“The martial world of Sichuan will never forget you!”

“It’s a snake with horns! The Huashan Divine Dragon has a snake with horns!”

“Whoa! The snake just did a somersault in midair!”

“The Fire King! The Fire King is holding the snake and trying to set it on fire!”

The murmuring noise gradually faded as the procession moved farther away.

And on a deserted hilltop, a boy sitting on a tree stump and watching the entire scene suddenly spoke.

“We’ve come a long way.”

“We certainly have. It’s tiring.”

At the sight of the old disciple plopping down on the grass with ragged breaths, the boy, Mungyeong, muttered,

“…We really have come a long way.”

He was not talking about distance. Mungyeong was talking about the years they had traveled through.

“Do you remember when we first met?”

“How could I forget?”

The old disciple wiped the sweat from his brow. It was as though the scorching sunlight from that day were beating down on him again.

“The first year of Hongwu. That exceptionally hot summer.”

It was the year the civil war over the imperial throne ended and a new emperor ascended.

The young and ambitious emperor changed the era name and attempted reforms, but the people, exhausted by the long civil war, were far too weary to heed the emperor’s will and take part in those reforms.

“Rebellions broke out across the land, and bandits ran rampant.”

“There was a drought, and swarms of locusts swept across the plains. The corpses of government soldiers and rebels filled the roads, and epidemics spread everywhere.”

“Yes. It was truly an age of turmoil.”

Death gave birth to more death, and soon it devoured the entire continent.

A young carpenter with the surname Dong could not escape the dark shadow that hung over the land, either.

“I still think about that time from time to time.”

The decades had changed more than just the landscape. The young carpenter who had lost his beloved wife and two children to the epidemic had since become an old physician.

“I wonder if I could have saved my family if I had been just a little faster. If I had found you sooner.”

“Do you regret it?”

“Yes.”

Sitting on a hill close to the heavens and gazing at the drifting scraps of cloud, the old physician’s eyes had returned to those of the young carpenter.

“For as long as I have breath in my body.”

It had been only a single day.

By the time the carpenter, dragging along his plague-stricken body, brought back the nameless old physician who had been staying in the slash-and-burn settlers’ village, everything was already too late.

He cried for an entire day, then dug a pit to bury his family. And he made one request of the physician he had brought.

“Bury me with them. That was what I asked.”

Mungyeong answered in his blunt voice.

“And so I slapped you across the face.”

“It hurt. Enough to make me want to die.”

It had hurt. Not because of pain that threatened his life, but because he could no longer see his beloved wife and children.

“You were the one who made me stand again, Master.”

Mungyeong shook his head.

“I merely held out my hand. You were the one who took it and stood.”

“I had to live. I had something to do.”

The carpenter’s body should have died from the epidemic.

But the physician cured him with medical knowledge unlike anything he had ever seen, and for the first time, the carpenter realized that even a human being could alter the birth, aging, sickness, and death ordained by heaven.

“I can still see it clearly. You kneeling before me and asking me to accept you as my disciple.”

“I remember it differently. I remember you beckoning me to follow you, Master.”

Thus, the young carpenter who had lost his family found a new goal, while the old physician who traveled the world caring for the sick and poor gained a new disciple.

It was only much later that the carpenter, who had now become a physician himself, learned his master’s true identity.

“Slaughter Saint… It is a truly terrifying sobriquet. That was the first time you felt like a stranger to me, Master.”

Mungyeong gazed into the distance with an emotionless expression.

What he was about to ask was something he had never once asked his disciple.

“Why didn’t you leave?”

“Did you think I would leave you?”

“I have taken countless lives over the years. I was nothing more than an ugly slaughter demon hiding my past. I would have understood if you had left.”

“Perhaps I really would have. But I knew all too well what kind of person you were, Master.”

A moment later, his low voice continued.

“The Divine Physician. My master is known as the Divine Physician. You are not someone who would kill without reason.”

“…”

Mungyeong’s eyes trembled.

It was a truth he had never told anyone, and one that no one had ever been willing to acknowledge.

He had lived as an assassin, taking countless lives with his own hands, whether they belonged to the orthodox faction, the unorthodox faction, or the Demonic Cult. And every one of those people had had a reason they deserved to die.

A Great Hero of the orthodox faction, renowned for his fairness and integrity, had made a hobby of raping and murdering women. A master of an unorthodox faction had slaughtered an entire village for fun.

If the army of the Demonic Cult invading the Central Plains had not killed and destroyed indiscriminately, and if the greatest assassin under heaven had not stepped forward to kill those infamous demon heads because he could no longer stand by and watch, he could never have been called the Slaughter Saint.

“If I had not fought the Demonic Cult, the entire world would have pointed fingers at me. Just as it had always done.”

The title of Slaughter Saint was merely an absolution granted by the orthodox faction that ruled the Murim—and praise for a powerful man.

Mungyeong had always been Mungyeong, but people neither knew nor wanted to know the truth hidden beneath the surface.

“Why didn’t you tell them?”

“It is all in the past. I wanted to leave the Murim, and I became a physician as I had intended. I will continue to do so.”

Mungyeong slowly rose to his feet. By then, the long procession that had left the Sichuan Tang Clan had disappeared into the distance.

“Let’s go down. There are patients waiting for us.”

He had just started walking, his voice dry, when—

“A great war will break out soon.”

Mungyeong came to an abrupt stop. Behind him, the old disciple’s voice continued.

“The same thing that happened back then will happen again. Countless people will die or be injured. There will be countless people who have lost their parents or children, and the screams and deaths will never end.”

“…I suppose I’ll be very busy. I should make preparations.”

“You know what I am trying to say, Master.”

“I do not want to know.”

“Master.”

“I am a physician. Though I broke the promise I made to myself and killed when I had no other choice, I will never make that mistake again.”

Mungyeong continued slowly.

“Fighting is their responsibility, and treating the sick is ours. My heart left the Murim long ago.”

“Then why did you never abandon your martial arts?”

“…”

Mungyeong was at a loss for words.

It was a question he himself had carried for a long time. If he had wanted to leave the Murim because he hated killing, then it should have been right for him to abandon martial arts as well—the means by which he killed.

Yet his martial arts had advanced even further. It was proof that he had been unable to let go of his attachment to them.

*Why was that?*

The old disciple’s voice broke through his brief reverie.

“You can treat hundreds, even thousands, of patients, Master. At the same time, you are capable of saving tens of thousands of lives.”

“…”

“Please prevent the coming war—not as the Slaughter Saint, but as the Divine Physician. This disciple will care for the patients here.”

Mungyeong suddenly lifted his head and looked at the sky.

It was clear and blue. Seven days and nights earlier, when the Sichuan Tang Clan had been dyed in blood, the sky had been filled with dark clouds.

“The sky is clear.”

With his blunt voice, he resumed his halted steps.

“I should go check on the patients. Come down slowly.”

Behind him as he descended the hill, Dongbong’s voice scattered into the wind.

“The Hour of the Dog. They said they would depart from the western port of Chengdu then.[^1]”

“Pointless. The Murim is not where I belong.”

Yet as the old disciple watched his master’s back gradually disappear into the distance, a faint smile formed around his lips.

“Please… stay well.”

Whoooosh.

A wind that had come from somewhere swept between the two men.

* * *

“What are you looking at so intently?”

At Hyuk Mujin’s question, I turned away from the crowd surrounding the port.

“Nothing. Just in case.”

“Then what are you looking at?”

“You little pest. Why are you interrogating me like this? If I say it’s nothing, take it as nothing.”

Hyuk Mujin gave me a meaningful smile.

“I actually know why you’re acting that way, Squad Leader.”

“…?”

I froze for a moment. How the hell did he know? Even Cheongpung hadn’t heard the conversation between the Divine Physician and me.

*Since when was this guy so perceptive?*

As I wondered about it, he whispered,

“Weren’t you looking at the young lady standing fourth from the right in the front row?”

“…”

“She is pretty, that’s for sure. She looks like the daughter of a fairly wealthy family. If you give me permission, Squad Leader, I could quietly go over there as your right-hand man and arrange a separate—”

“Mujin.”

“Yes? Ah, do you prefer natural encounters? If so…”

“Do you want to sink to the bottom of the Yangtze?”

“…”

“Stop talking nonsense and keep lying there. And don’t puke later because you get seasick.”

“…Yes, sir.”

As Hyuk Mujin quietly shrank in on himself, Gung Gibang snickered.

“What a fool. It’s not the fourth woman on the right, but the third on the left. Anyone can see she’s much prettier. Your eyes must be crooked.”

“Want me to make them crooked for real?”

“…Sorry.”

“Let’s live like human beings. Like human beings.”

With a sigh, I shook my head and gave the crowd gathered like clouds one last sweeping look.

The women on both sides were definitely pretty, but the third from the left was more my type—

*No. That’s not what this is about.*

*Damn it. Those idiots keep talking about it, so now I can’t stop looking.*

That was when a towering, bronze-skinned man approached me and spoke.

“Hey there, junior. No, not junior. Young Hero Jin. No, Great Hero.”

*What is this, buffering?*

I offered a solution to the boatman Mu Song, who was switching forms of address at lightning speed.

“Just call me junior.”

“Ahem. Th-That would be all right?”

“Why wouldn’t it be? You used to do it just fine.”

“Even so, you’ve accomplished such a great thing.”

He had a point. I had gone from being a local rising martial artist known as the Sleeping Dragon of Shanxi to a nationwide celebrity.

“And Great Hero Jeok seems not to like me very much, either…”

“It’s fine. He never liked water much in the first place.”

Where Mu Song kept glancing, Jeok Cheongang stood with a face twisted in fury.

Right beside him, Jin Wikyung was examining some bamboo slips whose contents I could not identify, while Cheongpung was teaching Mimi a new trick.

“Mimi, ride the waves!”

Sssrik—splash!

…Was that a water snake?

Mu Song, whose attention had been stolen for a moment by the rare spectacle, finally spoke with a sour expression.

“In any case, we have finished preparing for departure. When should we leave?”

“Has the time come already?”

“The Hour of the Dog you mentioned has passed. It would be best to leave before it gets any darker.”

“…Hmm.”

“Is someone else coming?”

I considered Mu Song’s question for a moment, then shook my head.

“No. No one.”

“Then we can depart.”

“Let’s do that.”

“Very well.”

Mu Song raised one hand high, and the water bandits, who had already finished preparing everything, began moving in perfect unison.

The people gathered to see us off were waving in our direction when—

“Wait! Just a moment!”

“Stop! Stop!”

The bow of the fast ship, which was about to pull away from the port, rocked.

Far in the distance, I spotted a boy making his way through the crowd and let out a quiet laugh.

“Let’s take one more passenger.”

[^1]: The Hour of the Dog was a traditional two-hour period, roughly corresponding to 7–9 p.m.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 376`.

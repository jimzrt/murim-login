# Master Edit Task — Chapter 157

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
| 혁무진    | **Hyuk Mujin**     |
| 조필     | **Jopil**          |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 화산파    | **Huashan**                      |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 검법     | **sword technique**                              |                                                       |
| 권법     | **fist technique**                               |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 소협      | **Young Hero**                                                  |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 매화검법 | **Plum Blossom Sword Technique** | Huashan sword technique Cheongpung performed at age ten. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 천응 | **Heavenly Eagle** | Huge bird regarded as a spirit creature, said to have a wingspan exceeding one jang. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 복호권 | **Crouching Tiger Fist** | Huashan martial art Cheongpung uses during the spar. |
| 일권복호 | **One Fist Subdues the Tiger** | Named form of the Crouching Tiger Fist. |
| 매화권 | **Plum Blossom Fist** | Huashan fist technique Cheongpung uses in sparring. |
| 천응조 | **Heavenly Eagle Claw** | Huashan claw technique used by Cheongpung. |
| 봉미혈 | **Fengwei acupoint** | Acupoint around the ribs targeted by Cheongpung. |
| 태권도 | **Taekwondo** | Martial art Taekyung practiced as a child. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

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

#### Chapter 155 tail (verified mastered)

…
coming to them, the family had to widen its arms even further. “…That’s how I handled it, but with our numbers expected to keep growing, we’ll likely need to reorganize again later.” “That’s what we should hope for.” Jin Wikyung tried to appear calm as he listened to Wipeng’s report. The Jin Family of Taiyuan had declined slowly but steadily since the Great Faction War. Now, however, it was rapidly regaining its former glory. *No. Perhaps it will become even stronger than it was before the Great Faction War.* If that happened… Only then would they truly earn the right to be called a great family. They would break free of their status as a frontier martial family and stand shoulder to shoulder with the towering powers of the realm. *A great family. A great family, huh.* It was a word that made his heart race just to think about it. Just as every martial artist dreamed of becoming the Martial God, Jin Wikyung had long dreamed of raising his family onto the foundation of a great family. *New Year’s Day is almost here.* On that day, before all the sects of Shanxi Murim, the Jin Family of Taiyuan would be recognized as the undisputed hegemon of Shanxi Province. Jin Wikyung had no doubt that the first day of the coming year would become the Jin Family of Taiyuan’s first stepping-stone—and the harbinger of its rise—as a great family. And it was at the very moment he secretly clenched his fists that— “Um… May I come in?” “Hm? Of course.” The voice belonged to the scholar who had just left. “What is it? Did you leave something behind?” “It’s not that…” Under Jin Wikyung and Wipeng’s puzzled gazes, the scholar continued cautiously. “There’s some news I failed to report.” “You’re too conscientious for your own good. You’ve been working hard for days without even getting proper sleep. Don’t worry about it. Go in and get some rest.” “No. I should have told you earlier, but it slipped my mind…” “Now, now. It’s fine. I told you to rest.” Wipeng chimed in. “My lord is right. You aren’t a jiangshi. You need to get enough rest so you can have the strength to work again tomorrow…” “Huashan has sent the Three Plum Blossom Elites.” Jin Wikyung and Wipeng shot to their feet at the same time. “What!” “What did you say?” Who were the Three Plum Blossom Elites? They were the most exceptional talents among the Plum Blossom Swordsmen, Huashan’s finest. In particular, Huashan’s Lone Crane, Baek Museong, was a major figure expected to become the next Sect Leader and carry Huashan’s future upon his shoulders. After hearing such news, how could the two men’s eyes not nearly pop from their sockets? “Is that really true?” “Yes. I meant to tell you at the end, but I forgot. And there’s one more thing.” “One more?” “Another? Tell us quickly!” The visit of the Three Plum Blossom Elites was shocking enough, and now he was saying there was something else. Frowning, the scholar continued. “They say the Grandmaster has disappeared. He seems to have gone to our family, so they asked us to send word if we happen to meet him… But who is the Grandmaster?” The scholar was still unfamiliar with the realities of Murim and wondered what this was all about. Jin Wikyung and Wipeng, however, stood with their mouths hanging open. “If Huashan’s Grandmaster is…” “Th-th-that…” Sword Saint Mae Jonghak. Unable to bring themselves to say the name aloud, the two men merely mouthed the words and swallowed hard. Huashan still wanted to keep the Sword Saint’s whereabouts secret. At times like this, it was best to keep one’s mouth shut. “Th-that… What did you say?” “Th-that thing. You know, that sort of thing.” “Pardon?” “You can leave now. Erase everything that just happened from your mind. Understood?” The scholar bowed with a bewildered expression and left. Only then did the words they had been holding back burst out. “The Sword Saint is coming!” “Shh! Lower your voice. We don’t even know for certain yet.” Despite his words, Wipeng’s face had also flushed bright red. To a swordsman like him, Sword Saint Mae Jonghak was greater than even the Jade Emperor. To think they might be able to meet such a person in the flesh! No, perhaps he might even receive instruction from him. “B-but why would the Sword Saint come to our family?” “What else could it be?” “Ah.” He had been so excited that he had momentarily forgotten who was currently staying at the Jin Family of Taiyuan. “That Sword Saint broke his seclusion to look for his beloved disciple.” “It’s only a guess for now, but that’s highly likely. I hear he raised him like his own grandson. How deep must his affection be?” Jin Wikyung grinned broadly. Whatever the reason, the Sword Saint’s visit was something to welcome with open arms—not only as a martial artist, but also as the Lesser Family Head of the Jin Family of Taiyuan. “You said his name was Cheongpung, right? Where is he now? I seem to remember hearing a while ago that he was training my youngest brother in the Wall Lizard Technique.” “The Wall Lizard Technique training ended two days ago, and now he’s…” “And now?” “He’s beating the crap out of the Third Young Master.” “Whaaat!”

#### Chapter 156 tail (verified mastered)

…
get back up anyway!” I wasn’t so sure. I had a feeling I wouldn’t be getting back up this time. I silently stared at the undulating energy of the Zaha Divine Technique and the blazing Sword Energy before finally managing to speak. “L-let’s put away the Sword Energy.” Let me live too, you bastard. * * * *Whoosh!* The spearhead tore through the air. A fast, razor-sharp strike. Cheongpung rolled his shoulder aside, and the second and third attacks followed like a storm. “Hah!” With a shout, spearheads rained down. The martial art itself was simple and heavy. But the movements of the man wielding the spear were light and fast. Hidden between his efficient movements were unpredictable attacks. *Swish! Swish-swish-swish!* A smile tugged at Cheongpung’s lips as he narrowly evaded the spearhead. *Wow, this is fun. Was Benefactor always this good?* He beamed as he watched the young man pressing him relentlessly. Jin Taekyung. They hadn’t known each other long, but he was the Benefactor who had helped Cheongpung in many ways. When Jin Taekyung had given him every last candied hawthorn skewer[^1] at their first meeting, Cheongpung had nearly cried. [^1]: Traditional fruit skewers coated in hardened sugar. *He’s a good person. He gave me something so precious.* Grandfather had been wrong. He had said Murim was crawling with frightening people who were vicious and utterly ruthless, but everyone Cheongpung had met was gentle and kind-hearted. He didn’t even dislike the Senior from the Zhongnan Sect whom he’d injured through his own mistake not long ago. *He’s my Senior, so he can’t be a bad person.* As far as Cheongpung knew, the bond between Seniors and Juniors was no ordinary relationship. It was a close tie forged by something thicker than blood. And Grandfather had always told him to protect the weak. The Senior from the Zhongnan Sect had been weak in martial arts. Cheongpung had felt terrible for hurting him. *But…* It was nice that there was no reason to feel bad about Jin Mukyung and Jin Taekyung. They were the strongest people Cheongpung had met since leaving Huashan. Even now, as he exchanged blows with Jin Taekyung, he was enjoying himself immensely. *Whoosh!* Cheongpung easily dodged the spear thrusting toward his shoulder, then burst out laughing despite himself. “Hehe.” “You laughing?” “Because I’m happy.” “You really need to watch what you say. That’s a dangerous thing to say.” *Swish-swish-swish!* Six killing attacks and twice as many feints came raining down from every direction. But Cheongpung was no longer where he had been. Jin Taekyung pierced the faint afterimage and shouted with the expression of someone who had seen a ghost. “What the hell was that?” “Dark Fragrance Drift. Hehe.” “That’s cheating!” “Would you like me to teach you?” “Great Hero Cheongpung, as for me, I’ve been barely scraping by in this harsh world with the paltry Jin Family’s Manoeuvre Technique…” “Oh, right. Grandfather told me not to teach it to anyone.” “This little bastard?” *Whoosh!* Jin Taekyung changed direction and thrust low. Just before the fiercely spinning spearhead pierced his instep, Cheongpung raised his foot with dazzling speed and pressed the spearhead down toward the ground instead. *Scrape!* “Wow, that was a little dangerous.” But Jin Taekyung wasn’t listening to him. With a short shout, he lifted the spear shaft beneath Cheongpung’s foot. “Hah!” “Benefactor, it’s no use. This is the Thousand-Catty Drop[^2]—” [^2]: A catty is a traditional East Asian unit of weight; the technique’s name evokes immense downward force. *Whoosh!* The next moment, Cheongpung felt himself floating. Jin Taekyung’s tremendous strength whipped the spear shaft skyward, flinging Cheongpung’s feet clear and leaving them treading empty air. He lost his balance for an instant and hurriedly drew up his internal energy. *Boom! Boom! Swish-swish!* The force of the Falling Flower Chasing Shadow Palm struck the air and shoved his body backward. A split second later, Jin Taekyung’s spear stabbed and slashed through the space where Cheongpung had been. *Wow.* Jin Taekyung’s strength was beyond Cheongpung’s imagination, even if it was still inferior to his grandfather’s. No. It wasn’t just his strength. He had incredible stamina, enough to fall countless times and keep getting back up. Agility that shouldn’t have been possible for someone with his build. And tremendous Toughness. *Even the way he uses martial arts is different from everyone else.* Cheongpung was a Peak master. He had been raised by the Sword Saint and had grown up watching the Sword Saint’s martial arts. He could gauge an opponent’s level from a single move and half a form of the martial arts they displayed. *Young Hero Jin Mukyung was sharp.* Jin Mukyung, whom he’d dueled a few days earlier, possessed an aura that seemed sharp enough to cut anyone who touched it. His martial arts were the same. But despite sharing the same blood, Jin Taekyung’s disposition and martial arts were the exact opposite of his brother’s. *What should I call this?* Though his martial arts were rough, still unrefined, and otherwise unremarkable, his movements created a strange tension. His aura seeped out naturally… “Whew. You coming? If not, I’m coming to you.” At the sight of the man striding toward him, Cheongpung finally thought of a word. *Wildness.* A beast hell-bent on biting through its prey’s throat. Jin Taekyung’s claws had not yet been honed, and that was precisely why they seemed even larger.

## Korean source

```text
＃157화



예로부터 명산(名山)의 주인은 영물(靈物)이라고 했다. 중원 오악으로 불리는 화산도 예외는 아니었다.

사람의 발이 닿기 전, 드높고 광활한 산림을 지배하던 것은 호랑이였다.

왕의 위엄과 짐승의 흉성을 지닌 이 영물은 자신들의 영역이 침범당하자 분노했고, 이내 허락받지 않은 불청객들을 공격하기 시작했다.



‘와아, 그래서요?’

‘인명 피해가 극심해지자 화산파에서도 나서지 않을 수 없었지. 복호권(伏虎拳)은 그렇게 탄생했다.’



호랑이를 굴복시키는 권법. 복호권.

청풍은 오래전 복호권을 배울 당시 할아버지가 해 주었던 말을 똑똑히 기억하고 있었다.



‘풍아, 복호권은 산중제왕을 굴복시킬 만큼 강맹한 무공이다. 이것 하나만 잘 익혀도 네 또래에 널 대적할 녀석은 없을 것이다. 알겠느냐?’

‘네!’



어린 시절의 청풍은 할아버지의 말을 철석같이 믿었다.

그러나 십 년이 흐른 지금 이 순간.

퍽!

“어우, 아파라.”

“……어라?”

그는 처음으로 할아버지도 틀릴 수 있다는 사실을 깨달았다.



* * *



청풍과의 비무를 시작한 지 사흘째. 나는 마흔다섯 번째 비무에서 처음으로 말을 더듬는 녀석을 목격할 수 있었다.

“으, 은인. 괜찮으세요?”

“알아요. 복호권 맞죠?”

눈으로 보고, 직접 맞으면서 겪어 보기까지 했다.

명치에 복호권을 얻어맞고 뻗었던 것이 어제의 일이다.

복호권을 시전 할 때의 청풍이 어떻게 움직이는지, 밟는 보법과 어깨의 위치, 이어지는 투로까지 눈에 담고 머릿속에 새겼다.

하지만 그러고도 공격을 허용했으니 확실히 청풍은 나보다 한 수 위다.

“방금 그거, 초식 이름이 뭡니까?”

내 물음에 청풍이 얼떨떨한 얼굴로 대답했다.

“일권복호(一拳伏虎)요.”

한 주먹에 호랑이를 쓰러트린다? 확실히 그럴 만한 파괴력을 지닌 초식이다. 비무를 겪을 때마다 쭉쭉 상승하는 맷집이 아니었다면 어제처럼 무릎을 꿇었을 것이다.

‘그래도 어제보단 많이 나아진 걸 위안 삼아야 하나?’

올라간 것은 맷집뿐만이 아니다. 청풍의 무공을 직접 몸으로 겪으면서 점점 익숙해지고 있었다.

“자, 다시 갑시다.”

하지만 청풍은 그럴 생각이 없어 보였다.

“어떻게 피하신 거예요?”

“예?”

“정확히 봉미혈(鳳尾穴) 부근을 노렸는데…….”

봉미혈이라면 늑골 어림이다. 나름 피한다고 몸을 틀었다가 복부 한가운데를 정통으로 얻어맞은 거다.

상대의 목적에서 벗어났으니 이것도 어떻게 보면 피하긴 한 셈인가? 나는 어깨를 으쓱했다.

“한 대라도 안 맞아 보려고 몸부림쳐 본 거죠, 뭐. 결국은 얻어맞았지만.”

“투로가 보였나요?”

며칠 동안 두들겨 맞다 보니 어렴풋이 보이긴 한다. 어디서 어떻게 공격이 들어올지. 또 다음 초식이 어떻게 이어질지.

‘아직 서툴러서 문제지.’

나는 욱신거리는 복부를 문지르며 대답했다.

“지금까지 맞은 짬이 있는데 그 정도는 읽어야죠. 일부러 맞을 때마다 눈 부릅뜨고 봤습니다.”

얻어맞으면서도 눈을 감지 않는 것, 상대의 투로를 파악하는 것의 기본 아닌가?

“어어, 이상하다. 복호권은 몇 번 안 썼는데.”

“그래서 다른 것보다는 좀 더 걸리더라고요.”

“다른 거요?”

“네. 매화권 같은 건 나름 쉽던데? 비무에서 가장 많이 썼던 거라 그런지 대충 알겠더라고요.”

청풍이 감탄성과 함께 박수를 쳤다.

“와아, 보여 주실 수 있어요?”

“뭐 어려운 건 아니니까.”

나는 어설픈 자세로 짝퉁 매화권을 펼쳤다. 보법도, 동작도 영 엉성하지만 모두 청풍이 비무 때마다 펼치던 매화권의 초식들이다.

‘이 정도쯤이야, 뭘.’

무공을 익히다 보니 어느 순간부터 깨달았다.

식(式)에는 무공에 대한 이해와 그에 걸맞은 공력 운용이 필요하지만, 형(形)을 따라 하는 건 쉽다는 사실을.

‘여기서는 이렇게 움직였지, 아마?’

일 초식부터 칠 초식까지. 간혹 버벅거리긴 했지만, 무리 없이 최대한 자연스럽게 펼쳐 보인 뒤 고개를 돌렸다.

“일단 이 정도인데…… 저기 청 소협?”

“아, 네. 은인.”

“무슨 문제라도 있습니까? 표정이 왜 그래요?”

“아뇨, 그게…….”

어쩐지 복잡 미묘한 표정으로 나를 바라보던 청풍이 머뭇거리며 입을 열었다.

“갑자기 할아버지가 하셨던 말씀이 생각나서요.”

“검성 할배, 아니 조부님이요?”

“네. 저를 도둑놈이라고 부르셨거든요.”

“괜찮아요. 저도 어릴 때 엄마 지갑에서 몰래 천 원 빼 갔다가 뒤지게 맞았어요.”

“그게 아니라…….”

청풍이 한숨을 푹 내쉬었다.

“무공을 가르쳐 주시면서 늘 그러셨어요. 저보고 무공 빼먹는 도둑놈이라고.”

“아.”

이거 칭찬 맞지? 청풍 같은 재능충에게 칭찬을 받다니.

얼떨떨해하는 내게 청풍이 말했다.

“은인은 무공의 천재가 분명해요.”

“천재요? 제가?”

“네.”

천재는 무슨……이 아니고, 맞긴 맞다.

따져 보면 고작 두세 달 만에 일류 무공인 진무보법과 창법을 대성했으니까.

물론 전부 시스템 빨이지만.

“그냥 편법이에요. 제가 몸 쓰는 건 잘하는 편이라. 눈도 좋은 편이고. 흐흐.”

“할아버지께서 그러셨어요. 무공은 눈이 칠, 발이 삼이라고.”

“그 말은 맞는 것 같은데, 아무튼 전 아니에요.”

“잘 생각해 보세요. 분명히 전에도 비슷한 일이 있었을걸요?”

그런가?

문득 어린 시절이 떠올랐다. 원체 운동신경이 좋아서 무슨 스포츠건 잘하는 편이긴 했는데. 굳이 무공이라고 할 만한 건…….

‘어, 하나 있네.’

내 표정이 변하자 청풍이 그거 보란 듯이 고개를 끄덕였다.

“그런 적 있죠?”

“있긴 있네요. 태권도라고.”

“태권도요?”

“무술 비슷한 겁니다.”

초딩 시절에 휴대용 게임기를 준다는 감언이설에 속아 등록한 태권도 도장.

고등부 형들의 태권도 시범이 있었고, 정확히 두 번 만에 태극 1장부터 8장까지 따라 할 수 있게 됐다.

물론 일주일도 지나지 않아 두 살 많은 중학생 형을 때리고 잘렸지만.

‘설마 그게?’

그러고 보니 F급 헌터 시절에도 뭐든 곧잘 따라 하긴 했었다.

다만 허접한 신체 능력이 발목을 잡았을 뿐.

나 같은 최하급 헌터가 중급 헌터의 움직임을 따라 하다가는 파괴력도 안 나올뿐더러 가랑이만 찢어지기 때문이었다.

‘하지만 이제는 다르지.’

넘치는 공력. 뛰어난 신체 능력. 그리고 무림에서 익힌 무공.

이제 보니 무공의 천재까지는 아니어도, 내게 제법 재능이 있긴 한 모양이다.

“청 소협은 매화권 익히기까지 얼마나 걸렸어요?”

“한 달이요.”

“한 달?”

직접 해 본 바로는 매화권이 화산파의 무학이긴 하나 그 정도로 복잡한 무공은 아니다.

그런데 저 녀석이 한 달 걸려서 익힌 걸 사흘 만에 얼추 따라 하게 됐다고?

‘미쳤다.’

입이 찢어질 정도로 환히 웃는 내게 청풍이 덧붙였다.

“대성(大成)하는 데 한 달이나 걸렸다고 할아버지한테 호되게 혼이 났죠.”

“…….”

그럼 그렇지.

어이없어하는 나를 보며 청풍이 중얼거렸다.

“그래도…… 썩 좋은 기분은 아니네요. 누가 내 무공을 따라 한다는 거.”

심상치 않은 기세가 피어올랐다.



* * *



혼절에서 깨어난 혁무진은 멍하니 연무장을 바라봤다.

‘끝내주네.’

연무장은 이미 반쯤 초토화된 상태였다.

산서성에서 방귀깨나 뀐다는 석공들이 정성 들여 깔아 놓은 청석은 절반 이상이 박살 났고, 지금도 빠르게 망가지는 중이었다.

캉! 카카카캉!

계절이 무색하게도 연무장 중앙은 열기로 후끈 달아올랐다. 불꽃을 터트리며 격돌하는 창과 검.

병장기를 쥔 주인들이 눈부신 속도로 움직이며 주고받는 합은 일류 고수인 혁무진의 눈으로도 따라가기 버거웠다.

‘어떻게 저렇게 빠를 수 있지?’

흰 무복을 입은 청풍과 검은 무복을 걸친 진태경.

한눈에도 극도로 대비되는 그들이 자신과 비슷한 또래라는 사실이 그저 놀라울 따름이었다.

‘청풍 저 인간은 괴물 수준이군.’

적당한 체구에 선한 인상. 당장 태원 거리에 반나절만 있어도 또래의 비슷한 젊은이를 서너 명은 만날 수 있을 것 같다.

그러나 저 평범한 청년에게는 아무도 쉽게 예상하지 못하는 신분이 감춰져 있다.

‘검성 매종학의 모든 것을 물려받은 후인.’

쐐애애애액! 쉭!

높이 솟은 태양 아래 진태경의 창날이 번득인다.

무겁고 간결한 초식, 그러나 힘과 속도가 더해지니 보는 것만으로도 아찔해지는 극쾌의 창술로 변모했다.

‘만약 저 창이 나를 노린다면?’

혁무진은 고개를 절레절레 저었다.

부끄럽지만 일다경 이상 버틸 자신이 없다. 아니, 어쩌면 그 생각마저도 스스로의 자존심을 지키기 위한 위안일지 모른다.

하지만 청풍은 달랐다.

쉬익, 쉬쉬쉬쉭!

사방을 점하고 달려들던 창날이 허무하게 허공을 갈랐다. 손쉽게 모든 공격을 피해 내는 청풍의 얼굴은 평온했다.

이어 그의 손이 흐릿해진다 싶더니 한 줄기 빛이 공기를 갈랐다.

쐐애애애액! 쾅!

“흡!”

굉음과 함께 진태경이 신음을 토해 냈다. 가까스로 검을 막아 낸 그를 향해 장대비 같은 검격이 쏟아졌다.

그 광경을 지켜보던 혁무진은 자신도 모르게 입을 벌렸다. 지금 이 순간, 한 가지 생각이 그의 머릿속을 꽉 채웠다.

‘유려하다.’

그렇게밖에 표현할 수 없다.

청풍의 움직임은 경지에 오른 화공의 붓놀림처럼 섬세하고 부드러웠고, 계절의 끝에서 너울너울 떨어지는 꽃잎을 닮았다.

넋을 놓고 바라보던 혁무진이 문득 중얼거렸다.

“매화검법…….”

그는 지금까지 화산파의 무공을 본 적이 없다.

그러나 한 가지는 확신할 수 있었다. 청풍의 몸놀림 하나하나에 화산파 무학의 정수(淨水)가 스며들어 있음을.

‘괴물이군. 말 그대로 괴물이야.’

그러나 괴물은 청풍 한 명만을 가리키는 단어가 아니었다.

쉬쉬쉬쉬쉭!

카가가강!

검성의 제자가 펼치는 매화검법을 모조리 막아 내는 또 다른 한 사람.

장대한 체구와 선 굵은 잘생긴 외모의 청년이 빠득, 이를 갈았다.

“씨이벌, 화산파 무공 진짜 개같이 만들었네!”

화산파가 들었다면 뒤집혔을 만한 걸쭉한 욕설을 내뱉은 진태경의 몸에서 거친 기세가 뿜어져 나왔다.

청풍의 유려함을 순간적으로 억누를 만큼 패도적인 기세는 곧 반격으로 이어졌다.

후우우웅! 쾅!

강맹한 일격.

굉음과 함께 창을 막아 낸 청풍의 신형이 훨훨 날았다. 단 한 수로 청풍의 공세를 떨쳐 낸 진태경이 인상을 찡그렸다.

“으, 따가워.”

스스슥. 말이 끝나기가 무섭게 그가 입고 있던 검은 무복이 길게 갈라졌다.

살이 드러난 가슴팍에는 몇 줄기의 상흔과 핏물이 흥건하게 배어 나왔다.

“이건 무슨 무공입니까?”

“천응조(天鷹爪)요.”

“없는 게 없네.”

“알려 드릴까요?”

“알려 줘도 됩니까?”

“어, 지금 생각났는데 할아버지께서 외인한테는 알려 주지 말라고 하셨어요.”

“또? 내 그럴 줄 알았지.”

“화산파에 입문하실래요?”

“안 해!”

고함을 내지른 진태경이 지면을 박차고 달려들었다.

아슬아슬하게 무공의 형태를 지키면서도 맹수와도 같은 본능적인 움직임. 혁무진은 몸을 부르르 떨었다.

‘저 인간은 어째 갈수록 더 무서워지네.’

사람에게는 저마다 기세라는 것이 있다.

진태경의 기세는 끈질기고 치열하다. 보는 사람으로 하여금 두려워지게 하는 무언가가 있다.

‘무공의 문제가 아니야.’

현재의 진태경도 물론 충분히 뛰어난 고수지만 검성의 제자이자 당당한 절정 고수인 청풍만큼은 아니다.

그러나 최근 몇 달간 그를 가까이서 지켜본 혁무진은 확신할 수 있었다.

‘하늘이 무너져도 살아날 인간이지.’

어떤 지옥에 던져 놔도 진태경은 살아 돌아올 것 같다는 확신.

지금까지 세 명의 절정 고수가 그를 죽이려고 했지만 결국 쓰러진 것은 그들이었다. 무림에서는 살아남는 자가 강자이며, 진태경은 거기서 끝끝내 살아남았다.

게다가…….

‘조장의 성장 속도는 상상을 초월한다.’

가장 가까이서 지켜봐 왔기에 알 수 있는 사실이었다.

일문일살 조필을 처절한 혈투 끝에 쓰러트린 그때부터 청풍과 맞서 싸우고 있는 지금까지.

진태경은 나날이 강해지고 있다.

‘그건 지금 이 순간도 마찬가지.’

바로 며칠 전만 하더라도 청풍이 쏟아 내는 화산파의 절기들 앞에 불과 백여 초를 버티지 못했다.

그러나 지금은?

혁무진이 직접 지켜본 것만 삼백여 초가 훌쩍 넘어갔다. 화산파의 본산 제자들만 익힐 수 있다는 천응조에 당해 놓고도 ‘앗, 따가워.’가 고작이다.

‘괴물이지. 괴물.’

비슷한 또래에 다들 절정, 초일류. 이건 해도 해도 너무한 것 아닌가. 어째 주위에 하나같이 괴물들만 득실거리는 것 같다.

한숨을 푹 내쉬던 혁무진은 며칠 전 벽호공을 수련할 당시 진태경이 했던 말을 되새겼다.



‘소중한 걸 잃기 싫다면 지금 목숨 걸고 해. 숨이 붙어 있을 때 죽도록 노력하는 게 죽는 것보다는 낫잖아?’



그 말이 맞다. 그렇게 죽도록 노력해야 살아남아 강자가 된다. 무림이라는 파도에 휩쓸리지 않기 위해 선 촌각이 아쉽다.

가만히 두 사람의 비무를 지켜보던 혁무진이 자리를 털고 일어났다.

‘새끼발가락으로 끝낼 순 없지.’

강해져야 한다. 진태경의 오른팔, 혹은 심장으로 인정받을 정도로. 그리고…….

‘모든 사람에게 혁무진이라는 이름으로 기억될 정도로.’

그는 검갑을 꽉 움켜쥐었다.
```

## Current accepted English baseline

```markdown
# Chapter 157

Since ancient times, people had said that the masters of famous mountains were spirit creatures. Huashan, one of the Central Plains’ Five Great Mountains, was no exception.

Before human feet ever touched it, tigers had ruled over its lofty, sprawling forests.

These spirit creatures possessed the majesty of kings and the ferocity of beasts. When their territory was invaded, they grew furious and soon began attacking the unwelcome trespassers who had entered without permission.

“Wow, and then?”

“When the loss of human life became severe, the Huashan Sect had no choice but to step in. That was how the Crouching Tiger Fist was born.”

*A fist technique that subdues tigers. The Crouching Tiger Fist.*

Cheongpung remembered clearly what his grandfather had told him when he learned the Crouching Tiger Fist long ago.

“Pung, the Crouching Tiger Fist is a powerful martial art capable of subduing the king of the mountains. If you master this one technique, no one your age will be able to stand against you. Do you understand?”

“Yes!”

As a child, Cheongpung had believed his grandfather’s words without question.

But now, ten years later—

*Whack!*

“Ow, that hurt.”

“…Huh?”

For the first time, he realized that even his grandfather could be wrong.

* * *

It was the third day since I had begun sparring with Cheongpung. During my forty-fifth duel, I witnessed him stumble over his words for the first time.

“B-Benefactor, are you all right?”

“I know. That was the Crouching Tiger Fist, right?”

I had watched it with my own eyes, and I had even experienced it firsthand by getting hit.

Getting knocked out after taking the Crouching Tiger Fist to the solar plexus had happened yesterday.

I had committed the way Cheongpung moved when he used the Crouching Tiger Fist to memory—the footwork he used, the position of his shoulders, and even the sequence of forms that followed.

And yet I had still allowed myself to be hit.

There was no doubt about it. Cheongpung was one step ahead of me.

“What was the name of that form just now?”

At my question, Cheongpung answered with a dazed expression.

“One Fist Subdues the Tiger.”

A single fist that knocked down a tiger? It certainly possessed enough destructive power to justify the name. If I hadn’t been getting so much better at taking hits with every duel, I would have dropped to my knees just like yesterday.

*Should I take comfort in the fact that I’m doing much better than yesterday?*

My ability to take a hit wasn’t the only thing that had improved. By experiencing Cheongpung’s martial arts with my own body, I was gradually getting used to them.

“All right, let’s go again.”

But Cheongpung didn’t seem to have any intention of doing that.

“How did you dodge it?”

“Huh?”

“I was aiming precisely around your Fengwei acupoint…”

The Fengwei acupoint was located around the ribs. I had twisted my body in an attempt to dodge, only to take the blow squarely in the middle of my abdomen.

Since I had avoided his intended target, could this technically count as dodging? I shrugged.

“I just struggled to avoid getting hit even once. I got hit in the end, though.”

“Did you see the sequence of forms?”

After being beaten up for several days, I could make out the forms vaguely. Where and how an attack would come from. How the next form would follow.

*The problem is that I’m still clumsy at it.*

I rubbed my aching abdomen and answered.

“After taking this many hits, I should be able to read at least that much. Every time you hit me, I kept my eyes wide open and watched.”

Wasn’t keeping your eyes open even while getting hit and figuring out your opponent’s sequence of forms the most basic thing?

“Hmm, that’s strange. I’ve only used the Crouching Tiger Fist a few times.”

“That’s why it took me a little longer to figure out than the others.”

“The others?”

“Yes. The Plum Blossom Fist was pretty easy. Maybe because you used it the most during our duels, but I could more or less figure it out.”

Cheongpung clapped with an exclamation of admiration.

“Wow, can you show me?”

“It’s nothing difficult.”

I performed a poor imitation of the Plum Blossom Fist. My footwork and movements were both terribly awkward, but every form came from the Plum Blossom Fist Cheongpung had used in our duels.

*This much is easy.*

At some point after I began learning martial arts, I realized something.

A technique required an understanding of martial arts and the internal-energy control to match it. But copying the form itself was easy.

*I moved like this here, didn’t I? Probably?*

From the first form to the seventh. I occasionally stumbled, but I managed to perform them as naturally as possible without much difficulty. Then I turned my head.

“That’s about it for now… Young Hero Cheongpung?”

“Ah, yes, Benefactor.”

“Is something wrong? Why do you look like that?”

“No, it’s just…”

Cheongpung stared at me with an oddly complicated expression before hesitantly opening his mouth.

“I suddenly remembered something my grandfather once said.”

“The Sword Saint old man—I mean, your grandfather?”

“Yes. He used to call me a thief.”

“It’s all right. When I was young, I secretly took a thousand won from my mother’s wallet and got beaten half to death.”

“That’s not what I mean…”

Cheongpung let out a deep sigh.

“He always said that while teaching me martial arts. He called me a thief who stole martial arts.”

“Oh.”

That was a compliment, right? To think a talent freak like Cheongpung was praising me.

As I stood there dumbfounded, Cheongpung said,

“Benefactor, you’re definitely a genius of martial arts.”

“A genius? Me?”

“Yes.”

*A genius, my ass…*

No, wait. He was right.

When I thought about it, I had mastered the Jin Family’s Manoeuvre Technique and spear technique—both First Rate martial arts—in barely two or three months.

Of course, the System had carried me through all of it.

“It’s just a shortcut. I’m pretty good at using my body, that’s all. My eyes are good, too. Heh heh.”

“My grandfather used to say that martial arts are seventy percent eyes and thirty percent feet.”

“I think he was right about that, but either way, I’m not a genius.”

“Think about it carefully. I’m sure something similar happened before.”

Was that true?

I suddenly remembered my childhood. I had always been good at sports because of my natural athletic ability, but martial arts specifically…

*Oh. There was one.*

When my expression changed, Cheongpung nodded as though to say he had been right.

“See? Something like that happened, didn’t it?”

“There was one. Taekwondo.”

“Taekwondo?”

“It’s something like a martial art.”

Back in elementary school, I had been tricked into enrolling at a taekwondo academy by the promise of receiving a portable game console.

The older high school students had put on a taekwondo demonstration, and after watching it exactly twice, I could follow all eight Taegeuk forms.[^1]

[^1]: Taegeuk forms are a standardized sequence of eight color-belt patterns in taekwondo.

Of course, I beat up a middle-school student two years older than me and got kicked out less than a week later.

*Could that have been it?*

Come to think of it, even back when I had been an F-rank Hunter, I had been pretty good at copying almost anything.

My poor physical abilities had simply held me back.

If someone at the bottom of the Hunter ranks tried to imitate the movements of a mid-rank Hunter, he wouldn’t be able to generate any destructive power. He would only end up tearing his groin apart.

*But things are different now.*

Overflowing internal energy. Excellent physical abilities. And martial arts learned in Murim.

Now that I thought about it, I might not be a genius of martial arts, but I did seem to have a fair amount of talent.

“How long did it take you to learn the Plum Blossom Fist, Young Hero Cheongpung?”

“One month.”

“One month?”

From my own experience, the Plum Blossom Fist was a Huashan martial art, but it wasn’t complicated enough to take that long.

And this guy had taken a month to learn it, while I had managed to roughly copy it after three days?

*That’s insane.*

As I grinned so broadly that the corners of my mouth nearly split, Cheongpung added,

“It took me a whole month to achieve Great Attainment, so my grandfather scolded me terribly.”

“…”

Right. Of course.

As I stared at him in disbelief, Cheongpung muttered,

“Still… it doesn’t feel very good. Having someone copy my martial arts.”

A dangerous aura rose from him.

* * *

After regaining consciousness, Hyuk Mujin stared blankly at the training ground.

*This is incredible.*

The training ground had already been half reduced to rubble.

More than half of the bluestone carefully laid by stonemasons famous throughout Shanxi Province had been smashed apart, and the destruction was continuing at a rapid pace.

*Clang! Ka-ka-ka-clang!*

Despite the season, the center of the training ground was scorching hot. Spear and sword clashed amid bursts of flame.

The owners of the weapons moved at dazzling speed, exchanging blows so quickly that even Hyuk Mujin, a First Rate master, struggled to follow them.

*How can they be that fast?*

Cheongpung wore white martial robes, while Jin Taekyung wore black. The two young men were starkly different at a glance, yet the fact that they were around the same age was simply astonishing.

*That Cheongpung fellow is a monster.*

He had an ordinary build and a gentle appearance. If he spent half a day walking around Taiyuan, he would probably encounter three or four young men his age who looked much like him.

But that ordinary-looking young man concealed an identity no one could easily have guessed.

*The heir who inherited everything from the Sword Saint Mae Jonghak.*

*Whoosh! Whoosh!*

Beneath the high-riding sun, Jin Taekyung’s spearhead flashed.

His forms were heavy and concise, but with power and speed added to them, they transformed into an extremely fast spear technique that made Hyuk Mujin dizzy just watching it.

*What if that spear were aimed at me?*

Hyuk Mujin shook his head from side to side.

It was embarrassing, but he had no confidence that he could last even a full quarter hour. No, perhaps even that thought was nothing more than consolation meant to preserve his pride.

But Cheongpung was different.

*Swish, swish-swish-swish!*

The spearhead came at him from every direction, only to slice uselessly through empty air. Cheongpung’s face remained calm as he effortlessly dodged every attack.

Then his hand blurred.

A streak of light split the air.

*Whoosh! Boom!*

“Hng!”

Jin Taekyung let out a groan amid the thunderous impact. He had barely blocked the sword, but sword strikes poured toward him like a torrential downpour.

Hyuk Mujin watched the scene with his mouth falling open.

At that moment, one thought filled his mind.

*Graceful.*

That was the only way to describe it.

Cheongpung’s movements were delicate and fluid, like the brushstrokes of a master painter. They resembled flower petals drifting and fluttering down at the end of the season.

Hyuk Mujin watched in a daze before suddenly muttering,

“Plum Blossom Sword Technique…”

He had never seen Huashan martial arts before.

But he could be certain of one thing. The very essence of Huashan martial arts had seeped into every one of Cheongpung’s movements.

*He’s a monster. He really is a monster.*

But “monster” was not a word that applied only to Cheongpung.

*Swish-swish-swish-swish!*

*Ka-ga-gang!*

Another man was blocking every strike of the Plum Blossom Sword Technique unleashed by the Sword Saint’s disciple.

The young man with a powerful build and striking, ruggedly handsome features ground his teeth.

“Fuck, Huashan made its martial arts a fucking nightmare!”

If Huashan had heard the thick profanity Jin Taekyung spat out, the entire sect would have turned upside down.

A rough aura poured from his body.

The domineering force of it momentarily suppressed Cheongpung’s graceful movements, and then flowed straight into a counterattack.

*Whoooosh! Boom!*

A powerful strike.

Cheongpung’s body flew through the air after blocking the spear amid the thunderous impact. Jin Taekyung had knocked aside Cheongpung’s offensive with a single move, but he immediately frowned.

“Ow, that stings.”

*Slice.*

Before his words had even ended, the black martial robes he wore split open in a long tear.

Several long wounds scored his exposed chest, blood welling freely from them.

“What martial art was that?”

“The Heavenly Eagle Claw.”

“You really have everything.”

“Would you like me to teach you?”

“You’re allowed to teach me?”

“Oh, I just remembered. My grandfather told me not to teach it to outsiders.”

“Again? I knew you’d say that.”

“Would you like to join Huashan?”

“No!”

Jin Taekyung shouted and kicked off the ground, charging forward.

His movements were instinctive, like those of a wild beast, yet they barely retained the form of martial arts. Hyuk Mujin shuddered.

*Why does that man get scarier the longer I watch him?*

Every person possessed something called an aura.

Jin Taekyung’s aura was tenacious and fierce. There was something about it that made anyone watching him feel afraid.

*It isn’t about his martial arts.*

Jin Taekyung was certainly a highly skilled master, but he was not yet the equal of Cheongpung, the Sword Saint’s disciple and a true Peak master.

Yet Hyuk Mujin had watched him from close by for the past several months, and he could say this with certainty.

*Even if the sky fell, that man would survive.*

Hyuk Mujin was certain Jin Taekyung would somehow return alive no matter what kind of hell he was thrown into.

Three Peak masters had tried to kill him so far, but in the end, they had been the ones to fall. In Murim, the one who survived was the strong one.

And Jin Taekyung had survived to the bitter end.

Besides…

*Captain’s growth is beyond imagination.*

It was something Hyuk Mujin knew because he had watched him from closer than anyone else.

From the moment Jin Taekyung had defeated Jopil, One Question, One Kill, after a desperate battle to the present, when he was fighting Cheongpung.

Jin Taekyung was growing stronger every day.

*And that’s true even now.*

Just a few days ago, he hadn’t been able to last even a hundred moves against the supreme techniques of Huashan that Cheongpung unleashed.

But now?

Hyuk Mujin alone had watched the exchange go well beyond three hundred moves. Even after being struck by the Heavenly Eagle Claw, a martial art that could be learned only by disciples of Huashan’s main sect, all Jin Taekyung said was, “Ow, that stings.”

*He’s a monster. A monster.*

Everyone around them was around the same age, and they were all Peak or advanced First Rate. Wasn’t that taking things too far? It seemed as though nothing but monsters surrounded him.

With a deep sigh, Hyuk Mujin remembered what Jin Taekyung had said a few days earlier while training the Wall Lizard Technique.

*If you don’t want to lose something precious, then risk your life and do it now. Working yourself to death while you’re still breathing is better than dying, isn’t it?*

Those words were true.

You had to work yourself to death to survive and become strong. Every moment was precious if you wanted to avoid being swept away by the waves of Murim.

Hyuk Mujin watched the two men spar for a while longer, then got to his feet.

*I can’t finish this with just my little toe.*

He had to become stronger. Strong enough to be acknowledged as Jin Taekyung’s right arm—or perhaps his heart.

And…

*Strong enough for everyone to remember the name Hyuk Mujin.*

He gripped his sword case tightly.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 157`.

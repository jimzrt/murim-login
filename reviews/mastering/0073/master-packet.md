# Master Edit Task — Chapter 73

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
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 큰형     | **eldest brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 시스템              | **System**                     |
| 스킬               | **Skill**                      |
| 스킬창              | **Skill Window**               |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 장칠득 | 진태경 | servant_to_third_young_master | Third Young Master | formal-deferential | Jang Childeuk addresses Taekyung as 삼공자님 while asking permission to report the dangerous training. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 호승심 | polysemy | Competitive pride or fighting spirit; not merely a desire to test oneself. | test myself |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 큰형 | kinship | Eldest older brother, not a generic older brother. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 65–69

## Plot

Jin Mukyung is astonished that Jin Taekyung has become a First Rate martial artist approaching the Peak realm. When Mukyung uses internal energy, he defeats Taekyung and destroys the pavilion. Taekyung and the badly injured Hyuk Mujin are taken to the Medicine King Hall, while the Jin Family mistakes the incident for an assassin’s attack and begins a pursuit for the Head Elder’s possible hidden disciple. Mujin receives public credit for protecting Taekyung, leading to speculation that he may become the next Master of the Gatekeeper Pavilion.

Mukyung reunites with Jin Wikyung after three years but remains detached and focused on training. Wikyung sends Wipeng and thirty elites south under the cover of pursuing the nonexistent assassin, while secretly preparing to summon every sect in Shanxi Province on New Year’s Day and potentially seek the Alliance Leader position. Wikyung finds no mention of Dark Heaven in the family records. Gong Yacheong continues recovering and will oversee the rebuilt Sakju Branch, with Socheon and Soyul planning to join him in six months.

While Taekyung’s residence is rebuilt, Wikyung places him and Mukyung together temporarily. Mukyung imposes rules of polite speech, silence, and obedience regarding the training hall. After Mukyung harshly beats Taekyung with his scabbard, Taekyung sincerely asks to become stronger. Mukyung agrees to rebuild his martial arts from the fundamentals through practical, real-combat training.

The System grants Taekyung the Return achievement and Returnee title, activating Login and Logout and increasing all stats by ten. It then creates the Peak-Grade Quest “[Trial? Training?],” requiring Mukyung’s recognition before the remaining cohabitation period ends. Logout is restricted, and Mukyung orders Taekyung to bring his spear for training.

## Continuity

- Jin Mukyung defeated Taekyung in their spar, destroying Taekyung’s pavilion. Taekyung survived; Hyuk Mujin remains badly injured and under treatment.
- The Jin Family is pursuing an unidentified assassin believed possibly to be the Head Elder’s hidden disciple. The assassin’s identity, sponsor, and possible connection to Song Sword Sect remain unknown.
- Jin Mukyung has begun training Taekyung harshly and intends to reconstruct his inadequate martial arts from the basics.
- The Peak-Grade Quest “[Trial? Training?]” requires Jin Mukyung’s recognition. Its reward and failure conditions remain unknown, and Logout is restricted for its duration.
- Taekyung is Level 50 with fifty unspent points and fifteen years of Internal Energy after investing fifty points in Agility. The Returnee title grants All Stats +10 and activates Login and Logout.
- Jin Wikyung plans a New Year’s Day summons for all Shanxi sects and may pursue the Alliance Leader position; whether the sects will attend and whether he will become Alliance Leader remain unresolved.
- Wipeng is traveling south with thirty Jin Family elites under the pretext of pursuing the assassin.
- Gong Yacheong will lead the rebuilt Sakju Branch; Socheon and Soyul intend to accompany him in six months. Soyul still does not know that her parents are dead.
- Mukyung has spent three years attempting to open the Ren and Du meridians.
- Hyuk Mujin’s possible promotion to Master of the Gatekeeper Pavilion remains unresolved.

## Translation Decisions

- Use **First Rate**, **Peak**, **Internal Energy**, **Medicine King Hall**, **Master of the Gatekeeper Pavilion**, and **Alliance Leader** consistently.
- Render **삼재검법** as **Three Calamities Sword Technique**.
- Use **gongcheong seokyu** for 공청석유, with a footnote explaining the rare-elixir and petroleum wordplay.
- Use **junzi** for 군자, with a footnote explaining the Confucian ideal of a morally upright gentleman.
- Retain **Hyung-nim** for Taekyung’s deferential 형님, distinct from casual **hyung**.
- Use **Sleep Mode**, **Return**, **Returnee**, **Login**, **Logout**, **Ren and Du meridians**, **Heart Demon**, and **Quest** for established System and cultivation terminology.
- Render **두 시진** as **two hours**, **권각술** as **fist-and-kicking technique**, and **인정** in the Quest mission as **recognition**.
- Retain **Asmodeus** for 아스모데우스 and **Demon King Asmodeus** for 마왕 아스모데우스.

### Prior accepted reading-copy tails

#### Chapter 71 tail (verified mastered)

…
martial art I had learned. *I’ll show you what a real fight looks like.* With all my strength, I kicked Jin Mukyung in the shin as he grinned triumphantly. It was a decisive technique known as a soccer kick, or simply a shin-kick. I had never seen anyone stay fine after taking one of these. Clang! Add one more to the list. “You fucking—” “You idiot.” Jin Mukyung looked down at me as I collapsed, clutching my foot. His expression seemed to say that I was the most pathetic person alive. “Fifth… Never mind. I’m getting tired of talking.” He pulled a flat metal plate from beneath his pant leg and strode toward me. I tried to limp to my feet, but he kicked my ankle out from under me and sent me back down. *Damn it.* It was over. If I used Inventory, I might have a chance to turn things around, but I did not want to do something so blatantly suspicious right in front of him. I lowered my head with a sigh. “Let’s stop.” “You want to stop?” I lifted my head at his hard voice. Jin Mukyung’s face had gone cold. “After only this much?” The man who had been grinning as he gleefully beat me only moments ago was nowhere to be seen. His emotionless gaze made my skin prickle. My Adam’s apple bobbed. Gulp. Almost simultaneously with the sound of me swallowing, the wooden sword slammed into my right shoulder. My arm buckled with a thud, throwing me off balance. “Guh. What the hell are you doing…?” Jin Mukyung ignored me and swung the wooden sword again. The Jin Mukyung standing before me now seemed unable to hear the voice of the defeated. Thud. Thud. Thud. He struck my left arm, then both legs. Only then did his hand stop. “You just had all four limbs cut off. By a vicious Peak master of the dark path who is several times stronger than you.” “…” “If he were even nastier, he’d have other methods.” Tap-tap-tap. The instant Jin Mukyung’s hand blurred, my entire body went rigid and my tongue curled back. The System immediately alerted me to the abnormal conditions. Beep! > **System** > > - The **Paralysis Acupoint** has been subdued. You will be paralyzed for two hours! > > - The **Mute Acupoint** has been subdued. You will be unable to make a sound for two hours! I could not move so much as a hair or make a single sound. A breathing corpse. In my current state, even a child could kill me. *Jin Mukyung. You insane bastard!* The curses could only circle inside my head, unable to escape my lips. All I could do was glare at him. Jin Mukyung calmly met my furious gaze. “Tendon-Splitting and Bone-Twisting is a cruel technique. Within an hour at most, your qi and blood will twist and every bone in your body will be crushed. Even if you miraculously survive, you’ll either go insane or spend the rest of your life crippled.” “…” “Do you think you could endure that pain? You’d probably forget who you are within fifteen minutes.” My stomach churned. Not because of his explanation of Tendon-Splitting and Bone-Twisting. It was Jin Mukyung’s eyes. There was no emotion in them. Those black eyes were unfamiliar and frightening. *Could Jin Mukyung really be about to kill me?* No. That was impossible. I was Jin Taekyung. A direct descendant of the Jin Family of Taiyuan, and Jin Mukyung’s only younger brother. But what he did next went far beyond anything I had expected. “Don’t worry. I’ll send you off without pain.” Something cold touched my throat as he spoke in a low voice. It was the metal plate Jin Mukyung had pulled out earlier. Its thin, sharp edge slowly dug into my flesh. *I’m going to die? Like this?* I had survived dozens of brushes with death. In Gates, and in Murim. I had struggled all this time to survive somehow… And now I was about to die without even being able to blink. To that bastard who was supposed to be my biological older brother, even though we did not share a single drop of blood! *What the fuck kind of situation is this?* My body rigid, I could only stare at the ceiling as the voice of the Reaper reached my ears. “Die.” Slice. The strength drained from my entire body. I felt hot blood trickling down my neck. Jin Taekyung. Aged twenty-seven. Gone to sleep in Murim. I slowly closed my eyes. “…” No, wait. Something was wrong. *My acupoints were sealed, but I just closed my eyes?* At that moment— Ding. > **System** > > - The **Paralysis Acupoint** has been released. The paralysis has ended! > > - The **Mute Acupoint** has been released. You can speak freely! “Get up.” “…” At Jin Mukyung’s voice, I slowly opened my eyes. All five of my senses were sharp and clear, proving that I was alive. *How?* I hurriedly felt the back of my neck. The cut stung, and blood came away on my fingers, but there were only a few drops of it. Everything else had been an illusion brought on by the fear and tension of death. “Remember.” His cold voice continued—the same voice that had pronounced my death only seconds earlier. “You died once today.”

#### Chapter 72 tail (verified mastered)

…
vision went dark. “No. Don’t do it! Don’t offer it!” “Lesser Family Head!” Huff, huff. Childeuk panted heavily, and Jin Wikyung gathered his internal energy. *I never imagined something like this would happen.* No matter how open-minded he was, this was too much. Personal sexual preferences were one thing, but he had no desire to become their object. Jin Wikyung swallowed hard. “Then… are you really into men?”[^2] Childeuk’s eyes flashed. His heart pounded at the thought of wearing the navy-blue uniform of the Jin Family’s martial artists. “Yes! Just give the order!” “How dare you set your sights on me? Not a chance, you bastard!” Smack! A slap from a Peak master was powerful. Childeuk collapsed like a puppet with its strings cut. Jin Wikyung stared down at him, breathing hard, then hurriedly rang the bell. Ding. Ding. “Lesser Family Head, did you call—? Gasp! Childeuk!” Jin Wikyung spoke to the horrified servant. “Drag him out immediately!” “W-What happened?” “That bastard tried to… No. Never mind.” He could not possibly say such a thing to a member of his household. For the first time in his life, anger and wounded sorrow brought him close to tears. “I-I’ll take care of it.” Just as the quick-witted servant hoisted Childeuk onto his back, Jin Wikyung added the most important part. “And that man.” “Yes?” “Remove him from his post.” “Ah.” The servant suddenly remembered Childeuk’s assignment. *Delivering meals.* The most important duty given to Childeuk, an exceptional servant possessing all four virtues, was to bring every meal to Jin Mukyung and Jin Taekyung. “Don’t let him anywhere near my younger brothers. Understood?” “Yes, sir!” * * * ### Training Day 1 I decided to start keeping a diary today. So I won’t forget what I learn during this training. Under Jin Mukyung’s guidance, I did nothing but swing a spear all day. Every day begins and ends with a spar. I got beaten half to death, but it’s bearable. This is my first time grinding ink, and it’s surprisingly fun. ### Training Day 2 I swung my spear to the point of death again today. Maybe that’s why my Strength and Stamina stats increased, and the Jin Family’s Spear Technique reached the ninth stage. I’m progressing much faster than when I trained alone, but I can’t help thinking I’d be better off spending this time learning another Peak martial art. Still, Jin Mukyung must have his reasons. Grinding ink is getting a little annoying. I’m tired. ### Training Day 3 The Jin Family’s Spear Technique again. I asked him to teach me another martial art and got beaten half to death. He said my mind was rotten. While desperately dodging his attacks, the Jin Family’s Manoeuvre Technique rose to the eighth stage. Damn it. This is surprisingly effective. ### Training Day 4 I haven’t slept more than two hours a day since training began. Most of my time is spent repeating the same cycle with Jin Mukyung: training, sparring, training, sparring. Starting yesterday, I began using fasting pills instead of wasting time eating. Even with the System, I’m starting to reach my physical limit. ### Training Day 5 My arms hurt, so I only ground a little ink. The sky is yellow. Going to sleep. ### Training Day 6 I don’t understand why the System doesn’t have a notepad function. I got pissed off while grinding ink and broke the inkstone. Jin Mukyung beat me. ### Training Day 7 The Jin Family’s Manoeuvre Technique reached the ninth stage. My Level also increased by one. I’ve practiced it so relentlessly that these days, I even use the footwork when I’m just walking around. I got goose bumps. ### Training Day 8 My hands and feet keep getting tangled today. It feels like these aren’t the martial arts I know anymore. The martial arts I’ve performed thousands—even tens of thousands—of times feel unfamiliar. Jin Mukyung said it was a natural phenomenon. *What the hell is he talking about?* I got beaten because my expression was disrespectful. ### Training Day 9 I think I get it. * * * Bang! Compressed air erupted from the tip of the wooden spear. Jin Mukyung skidded backward and clicked his tongue as he looked at his broken sword. “That was a narrow success.” I did not answer. I stood there blankly, gripping my spear. *So this is what it was.* I had thought I knew the martial arts I’d learned inside and out. But I was wrong. I had merely mistaken the middle of the mountain for the summit. Whenever my martial arts rose to a new level, a new landscape came into view. *Just like now.* Ding. Ding. Ding. > **System** > > - You have achieved mastery of **Jin Family’s Spear Technique**! > > - You have achieved mastery of **Jin Family’s Manoeuvre Technique**! > > - Achievement **Master a First Rate Martial Art** completed! > > - As a reward, a new Skill, **Martial Arts Manual Creation**, has been generated! > > - All Stats have increased significantly! > > - Level Up! > > - Level Up! A wave of System notifications swept over me. [^1]: *Junzi* is a Confucian ideal referring to a morally upright and cultivated gentleman. [^2]: In Korean, *nam-saek* can refer both to male homosexuality and to the color navy blue, creating the misunderstanding between Jin Wikyung and Childeuk.

## Korean source

```text
＃73화



띠링. 띠링. 띠링.

밀려드는 시스템 알림에 귀가 아플 정도다. 나는 입을 딱 벌리고 눈앞을 가득 채운 메시지창을 지워 나갔다.

‘뭔 보상이 이렇게 많아?’

두 번의 레벨 업과 모든 능력치 상승, 거기에 더해 업적 달성으로 새로운 스킬이 주어졌다.

‘비급 제작?’

띠링.



스킬창



[비급 제작]

등급 : 無

경지 : 일 성

설명 : 대성한 무공에 한해 비급을 제작할 수 있다.

제작 가능한 비급 : 진가창법, 진가보법





설명을 읽어 보니 내가 짐작한 그대로다.

‘일단 스킬이니까 없는 것보다는 낫긴 한데…….’

지금으로써는 딱히 큰 효용이 없어 보인다. 이런 생산직 스킬도 주는구나, 하는 생각에 신기한 정도?

‘이럴 때는 확실히 게임 같단 말이지.’

이 세상에는 아직도 내가 겪어 보지 못한 것들이 너무 많다.

모든 것들이 생소하고 비현실적이다. 지금까지도 무림이 게임인지, 또 다른 현실인지 헷갈릴 정도로.

딱!

“아.”

얼얼한 뒤통수를 붙잡고 돌아섰다. 반 토막 난 목검을 든 진무경이 한심하다는 얼굴로 나를 바라보는 중이었다.

“집중 안 하지?”

“거, 진짜. 기분 나쁘게 자꾸 머리만 때리고 그래.”

“이 자식 또 자연스럽게 말 놓네.”

진무경은 눈을 가늘게 떴지만 이제는 별로 무섭지도 않다.

‘한두 번 맞아 보나.’

지옥 훈련이 시작된 지 오늘로 열흘째.

나는 시작과 동시에 중요한 사실 하나를 깨달았다.

‘존댓말 써도 맞는다!’

정말 오지게 맞았다. 겨우 이틀 차에 [맷집] 능력치가 생겼을 정도니 말 다 했다. 어차피 어떻게 하든 결과는 두들겨 맞을 텐데, 기왕이면 반말 쓰고 맞는 게 정신 승리에 도움이 된다.

따닥!

“이 정도야 간지럽지.”

괜히 맷집 능력치가 생긴 게 아니다.

꽃이 햇빛과 물을 받으며 자라는 것처럼, 내 능력치는 가혹한 폭력과 지옥 훈련으로 쑥쑥 성장했다.

빡!

“아, 잠깐만. 뼈 맞았어, 뼈.”

“비무 아직 안 끝났다.”

퍼버벅!

요령 있게 급소를 타격해 오는 목검을 맞아 가며, 나도 창을 휘둘렀다.

쉬쉬쉭! 타닥!

열흘간의 지옥 훈련.

마침내 대성에 이른 진가창법과 진가보법이 호흡처럼 자연스럽게 흘러나왔다.

띠링.



제한 시간 : 2시간 22분



띠링.



제한 시간 : 2시간 22분



“……?”

뭐야, 왜 두 번 울려.



* * *



쉬쉬쉭!

캉!

압박해 들어오는 창을 막아 내며 진무경은 새어 나오려는 헛웃음을 삼켰다.

‘이놈 봐라.’

열흘. 짧다면 짧고, 길다면 긴 시간이다. 그러나 그게 일류 무공을 대성하기까지 걸린 시간이라면 이야기가 달라진다.

‘뭐 이런 놈이 다 있지?’

지난 열흘간 수십 번도 넘게 든 생각이다. 진태경의 성장 속도는 문일지십(聞一知十)이라는 말로도 부족했다.

‘아는 것과 체득하는 것은 다르니까.’

무공을 대성(大成)했다는 말은 그 무공을 완벽히 이해하고 펼칠 수 있게 되었다는 말이다. 진태경은 일류 무공 두 개를 단 열흘 만에 고스란히 자신의 것으로 만들었다.

이미 어느 정도 경지에 올라 있었다는 사실을 감안해도 이건 엄청난 성과다.

‘이게 되네.’

진무경은 어이가 없었다. 처음 예상치가 어느 정도였더라?

확실한 건 처음 목표를 훨씬 초월했다는 것 정도다.

‘시도 때도 없이 손발 나가는 버릇 고치고, 기본기나 확실히 잡아 주려고 한 건데…….’

막상 시작해 보니 이야기가 달라졌다.

기본기? 진무경은 알 길이 없는 일이지만 진태경은 칠 년간 끊임없이 수련해 왔다. 강해지기 위한 수련, 살기 위한 발버둥이었다.

손바닥 가죽이 수십 번 찢어지고 아물수록 그의 창도 빠르고 강해졌다. 그 때문에 진태경의 기본기는 약간의 자세 교정을 제외하면 흠잡을 곳이 없다.

‘다른 부분들도 마찬가지고.’

마보(馬步) 수련 역시 시간 낭비에 불과했다.

근력, 체력, 민첩. 그의 모든 신체 능력은 동급의 무인들을 훌쩍 상회하고, 매우 균형감 있게 발달해 있었다.

‘지금까지 살아남은 게 마냥 운 때문만은 아니었군.’

껑충하게 큰 키와 길쭉한 팔다리. 날렵하고 옹골찬 근육을 보라. 삼 년 전, 기녀들한테 잘 보이겠다고 복근을 만들던 말라깽이가 맞나 싶을 정도다.

‘염병, 무슨 천무지체(天武肢體)도 아니고.’

진무경이 다시 한번 황당함을 느낀 그때였다.

쐐애애액!

강맹한 기세로 찔러 들어오는 창.

진무경은 보법을 밟으며 물러났지만 진태경은 끈질기게 따라붙으며 공격을 이어 나갔다.

쉭! 쉬쉬쉭!

같은 무공이라도 누가, 어떻게 펼치느냐에 따라 달라진다. 한 수, 한 수에 그가 가진 기질과 성향이 고스란히 묻어 나오는 것이다.

지금 펼쳐지는 진무경의 진가창법도 마찬가지였다.

‘진가창법이 이런 무공이었나?’

무인과 낭인. 어딘지 모르게 삐걱대고 불안하던 움직임이 서서히 조화를 이루기 시작했다.

‘벌써 제 것으로 만들었다, 이거지.’

열흘 전의 진태경은 반쪽짜리였지만…… 이미 변화는 시작됐다. 진무경은 아우의 성취가 기특하면서도 한편으로는 뱃속이 뜨거워졌다.

‘이건.’

과거, 다른 누군가를 상대로 한 번 느꼈던 감정이다. 그 대상이 진태경이 될 줄은 꿈에도 몰랐지만.

‘질투. 그리고 호승심.’

진무경은 그 자리에 우뚝 굳어 버렸다. 그 찰나의 빈틈을 향해 진가창법의 마지막 초식, 천관일이 쏘아졌다.

“합!”

콰아아아-!

창을 중심으로 휘몰아친 바람이 진태경의 기합을 집어삼켰다. 금방이라도 가슴이 꿰뚫릴 것 같은 그 순간, 진무경의 손이 검자루를 잡았다.

푸화악!

허리춤에서 솟구친 섬광이 바람을 갈랐다. 그 끝에, 진태경이 있었다.



* * *



쉭!

짧은 바람 소리와 함께 상반신이 시원해진다. 오른쪽 허리춤부터 시작해서 왼쪽 어깨까지. 깔끔하게 잘려 나간 무복 사이로 지하 연무장의 싸늘한 공기가 스며들었다.

상처가 없다는 걸 확인한 후에야 안도의 한숨이 흘러나왔다.

“후.”

그나저나 갑자기 검기라니. 심장이 목구멍 밖으로 튀어나올 뻔했다.

“미친. 검기는 안 쓴다더니.”

“……그걸 곧이곧대로 믿은 놈이 멍청한 거지.”

영 석연치 않은 얼굴로 대답한 진무경이 검을 집어넣었다.

“수련은 여기서 마친다.”

띠링.



- [진무경]이 수련 종료를 선언했습니다.

- 남아 있는 [제한 시간]이 소멸합니다.

- [진무경]의 평가에 따라 퀘스트 성공 여부가 결정됩니다.



성공? 아니면 실패?

내 기대감 어린 눈빛을 받으며, 그가 입을 열었다.

“한참 멀었어.”

“아.”

“열흘 동안 고작 이 정도밖에 못 따라오다니. 내 시간이 아깝…….”

진무경이 말하다 말고 떫은 표정을 지었다.

“그 표정은 뭐지?”

“응? 뭐가.”

“지금 짓고 있는 해괴망측한 표정 말이다!”

“아닌데? 무슨 말 하는 건지 모르겠는데?”

하지만 진무경의 말이 맞았다.

나는 자꾸만 솟구치는 입꼬리를 감추느라 무진 애를 써야 했다. 허공에 떠오른 시스템 메시지 때문이었다.

띠링.



- 퀘스트 성공 조건을 충족했습니다!

- [수련? 시련!] 퀘스트를 완료했습니다!

- 레벨 업!

- 퀘스트 완료 보상이 인벤토리로 이동합니다!

- 훌륭한 성과입니다. 추가 보상이 주어집니다!



“음. 부끄러움이 많은 아이로구나.”

정직한 청년. 진무경.

“이놈! 그게 무슨 소리냐!”

“아냐, 넘어가. 스물셋이면 한창 수줍을 때지.”

“이 새끼가?”

눈깔이 뒤집힌 진무경이 내게 달려들려던 그 순간이었다.

끼이익.

지상으로 통하는 문이 열림과 동시에 웬 하인 하나가 빼꼼 고개를 내밀었다.



[Lv.12 장칠득]



“저어, 공자님들?”

한 사흘인가? 그쯤 전에 꼬박꼬박 식사를 가져다주던 하인이다. 못 본 사이에 무슨 일이 있었는지 얼굴은 멍투성이고 이빨이 네댓 개 부러졌다.

그가 새어 나가는 발음으로 말을 이었다.

“소가주님께서 찾으십니다.”

“……젠장.”

나와 칠득이를 번갈아 보던 진무경이 아쉬운 얼굴로 주먹을 내렸다.



* * *



우리는 안내를 따라 이동했다. 진무경은 뭐가 그렇게 못마땅한지 뚱한 얼굴로 땅만 쳐다보며 걸었고, 칠득이는 걸을 때마다 통증이 올라오는지 자꾸 앓는 소리를 냈다.

“아야, 어이쿠. 으헉.”

“…….”

거 더럽게 신경 쓰이네.

“어쩌다가 다쳤어요?”

“그, 사소한 오해가 있었습니다.”

사소한 오해치고는 제법 중한 부상을 당한 것 같은데.

현실에서야 포션이 있으니 못 고칠 병이 없다지만 무림은 다르다. 나는 칠득이의 부러진 이빨을 보며 혀를 찼다.

“많이 아프시겠네.”

“괜찮습니다.”

칠득이가 의연하게 가슴을 쭉 폈다.

“태원진가의 무인이라면 이 정도는 견뎌야죠.”

“…….”

방금까지만 해도 아파 죽으려고 하더니.

그런데 이 사람, 하인 아니었나?

‘그러고 보니 옷이 바뀌었네.’

그는 태원진가 소속 무인들이 입는 짙은 남색의 무복을 입고 있었다. 이전에는 하인들이 입는 옷을 입었던 것 같은데.

내 시선을 알아차린 그가 수줍게 웃었다.

“아. 며칠 전에 정식으로 무인이 됐습니다.”

“무인?”

뒤에서 말없이 걷고 있던 진무경이 불쑥 입을 열었다.

“어디 소속인가?”

내가 근래 들어서 아무리 유명세를 떨치고 있다지만 진무경만큼은 아니다. 칠득이가 황송하다는 얼굴로 대답했다.

“소가주님 직속입니다.”

“큰형님 직속은 본가 내에서도 선별된 무인들만 들어갈 수 있는 곳인데.”

진무경이 칠득이를 위아래로 훑었다. 깔보는 눈빛이라기보다는 상대의 경지를 가늠하는 관찰에 가까웠다.

“근골은 제법이지만 딱히 무공을 배운 것 같지는 않은데?”

“예에. 사실 저도 얼떨떨합니다. 무공이라고는 일초 반식도 제대로 펼쳐 본 적이 없어서요.”

[기감]으로 파악한 칠득이의 레벨은 12. 음식이나 나르던 하인치고는 높지만 무인으로 치면 삼류다.

‘진위경 직속 일류 고수들은 최소 40레벨이 넘던데.’

뭐지? 배경이 빵빵한가?

진무경도 나와 비슷한 생각을 했는지 눈살을 찌푸렸다.

“뒷배가 좋나 보군. 춘부장께서 무슨 일을 하시나?”

칠득이가 송아지처럼 커다란 눈망울을 깜빡였다.

“십 년 전에 돌아가셨는데요.”

“…….”

“…….”

“유명한 약초꾼이셨는데, 호환(虎患)을 당하셔서 그만.”

순간 눈앞이 아득해졌다. 절정 고수답게 가장 먼저 평정심을 되찾은 진무경이 황급히 수습에 나섰다.

“후, 훌륭한 분이셨군.”

“지금 생각해도 참 순박한 분이셨습니다. 어머니와 금슬도 좋으셨고요.”

“그럼 어머니께서는, 혹시? 아니지?”

“잘 계십니다.”

우리가 안도의 한숨을 내쉬던 그때, 칠득이가 아련한 눈빛으로 먼 산을 응시했다.

“아버지 곁에 묻어 드렸으니 두 분 모두 잘 계실 겁니다.”

“…….”

“…….”

그 후는 죽음의 행진이었다. 당장 전력을 다해 도망치고 싶었지만 칠득이의 혼잣말을 듣고 포기했다.

“아, 저 꽃 오랜만에 보네요. 아버지를 따라 산에 가면 참 많이 보였는데.”

“…….”

“…….”

일각만 더 함께 걸었다면 진무경은 자살했을지도 모른다. 그러나 다섯 시간 같은 5분이 흐른 뒤, 우리는 다행히 목적지에 도착할 수 있었다.

“오, 왔느냐!”

전각 앞에서 기다리고 있던 진위경을 보자 눈물이 날 것 같다. 우리는 물기 어린 목소리로 부르짖었다.

“혀엉!”

“형님!”

칠득이는 어색하게 포권을 취했다.

“분부대로 공자님들을 모셔 왔습니다.”

나와 진무경을 향해 한걸음에 달려오던 진위경이 멈칫하더니 칠득이를 껴안았다.

“인의예지를 갖춘 장칠득! 우리 장 무인 왔는가!”

“옛! 소가주님.”

“아주 큰 임무를 완수했네! 이만 가서 쉬도록 하게.”

이게 도대체 무슨 상황이야. 나와 진무경이 얼빠진 얼굴로 그 광경을 지켜보던 그때, 귓가를 파고드는 전음이 있었다.

- 그, 내가 이 친구랑 사소한 오해가 좀 있어서…….

“…….”

어쩐지 칠득이의 뒷배를 알 것 같다.
```

## Current accepted English baseline

```markdown
# Chapter 73

Ding. Ding. Ding.

The flood of System notifications was enough to make my ears hurt. I opened my mouth wide and dismissed the message windows filling my vision one by one.

*Why are there so many rewards?*

Two Level Ups, an increase to all my Stats, and a new Skill for completing an achievement.

*Martial Arts Manual Creation?*

Ding.

> **System**
>
> **Skill Window**
>
> **Martial Arts Manual Creation**
>
> **Grade:** None
>
> **Realm:** First Stage
>
> **Description:** Can create martial arts manuals for martial arts that have reached mastery.
>
> **Martial Arts Manuals Available:** Jin Family’s Spear Technique, Jin Family’s Manoeuvre Technique

After reading the description, I realized it was exactly what I had guessed.

*It’s a Skill, so it’s better than nothing, I suppose…*

For now, though, it did not seem particularly useful. I was mostly fascinated that the System would give me a Skill for some kind of production job.

*This really does feel like a game sometimes.*

There were still far too many things in this world that I had never experienced.

Everything was unfamiliar and unreal. Even now, I was still unsure whether Murim was a game or another reality altogether.

Smack!

“Ah.”

I turned around, clutching the back of my stinging head. Jin Mukyung was looking at me with a contemptuous expression, a wooden sword broken in half in his hand.

“Not concentrating?”

“Seriously. Why do you keep hitting me in the head? It’s annoying.”

“This bastard is slipping back into informal speech again.”

Jin Mukyung narrowed his eyes, but he was not very frightening anymore.

*It’s not like this is the first or second time I’ve been hit.*

Today marked the tenth day since the hellish training began.

I had realized one important fact right from the start.

*I get hit even when I use polite speech!*

I had been beaten black and blue. I had even gained the **Toughness** Stat on only the second day, which said everything that needed to be said. No matter what I did, I was going to get beaten anyway. If so, using informal speech while getting beaten at least let me claim a moral victory.

Smack!

“This much is just a tickle.”

The Toughness Stat had not appeared for no reason.

Just as flowers grew with sunlight and water, my Stats had flourished under merciless violence and hellish training.

Whack!

“Hey, wait. You hit bone. Bone.”

“The spar isn’t over.”

Thud-thud-thud!

While taking hits from the wooden sword as it struck my vital points with practiced precision, I swung my spear as well.

Sshh-shh-shhk! Crack!

Ten days of hellish training.

At last, the Jin Family’s Spear Technique and Jin Family’s Manoeuvre Technique flowed out as naturally as breathing, having reached mastery.

Ding.

> **System**
>
> **Time Limit:** 2 hours 22 minutes

Ding.

> **System**
>
> **Time Limit:** 2 hours 22 minutes

“…?”

What the hell? Why did it ring twice?

* * *

Sshh-shh-shhk!

Clang!

Blocking the spear pressing in on him, Jin Mukyung swallowed a laugh that was about to escape.

*Look at this bastard.*

Ten days. It was a short time if you thought of it one way, and a long time if you thought of it another. But if that was how long it took to achieve mastery of a First Rate martial art, the matter was entirely different.

*What kind of person is this?*

He had thought the same thing dozens of times over the past ten days. Jin Taekyung’s rate of growth was beyond even the saying “hear one, know ten.”

*Knowing something and making it your own are different.*

To achieve mastery of a martial art meant that one understood it perfectly and could wield it as such. Jin Taekyung had made two First Rate martial arts completely his own in only ten days.

Even taking into account the fact that he had already reached a certain level, this was an astonishing achievement.

*So it really is possible.*

Jin Mukyung was dumbfounded. What had his initial estimate been again?

One thing was certain: Taekyung had far surpassed his original goal.

*I was only trying to cure his habit of throwing out his hands and feet whenever he felt like it and make sure his fundamentals were solid…*

But once training began, things had changed.

Fundamentals? Jin Mukyung could not have known it, but Jin Taekyung had trained relentlessly for seven years. Training to become stronger. Struggling desperately to survive.

His palms split open and healed dozens of times, and with each cycle, his spear became faster and stronger. Because of that, there was nothing to criticize in Jin Taekyung’s fundamentals except for a few issues with his posture.

*The same goes for everything else.*

Horse-stance training would have been nothing more than a waste of time.

Strength, Stamina, Agility—every one of his physical abilities far surpassed those of martial artists at the same level, and they had developed with remarkable balance.

*So surviving until now wasn’t simply a matter of luck.*

Look at his tall, lanky frame and long limbs. At his lean, solid muscles. Was this really the same skinny brat who had built abdominal muscles three years ago to impress courtesans?

*Damn, was he some kind of heavenly martial physique?*

Jin Mukyung was feeling dumbfounded all over again when it happened.

Swoooosh!

A spear thrust forward with powerful momentum.

Jin Mukyung stepped back using his footwork, but Jin Taekyung tenaciously followed and continued his attack.

Sshk! Sshh-shh-shhk!

Even the same martial art changed depending on who wielded it and how they wielded it. Every move carried the wielder’s temperament and disposition.

The Jin Family’s Spear Technique Jin Mukyung was using now was no different.

*Was this what the Jin Family’s Spear Technique was supposed to be?*

Martial artist and wandering martial artist. Movements that had been awkward and uneasy in some indefinable way were gradually beginning to harmonize.

*He’s already made it his own.*

Ten days ago, Jin Taekyung had been half-finished, but the change had already begun. Jin Mukyung was proud of his younger brother’s achievement. At the same time, heat began to build in his stomach.

*This feeling…*

It was an emotion he had felt once before, toward someone else. He had never imagined that Jin Taekyung would become its object.

*Jealousy. And fighting spirit.*

Jin Mukyung froze in place.

Toward that momentary opening, the final form of the Jin Family’s Spear Technique, Sky-Piercing Strike, shot forward.

“Haap!”

Whoooosh!

The wind spiraling around the spear swallowed Jin Taekyung’s shout. At the moment when it seemed the spear was about to pierce straight through his chest, Jin Mukyung’s hand seized his sword hilt.

Fwoosh!

A flash erupted from his waist and cleaved through the wind.

At its end stood Jin Taekyung.

* * *

Sshk!

With a short rush of wind, my upper body suddenly felt breezy. Starting from my right waist and ending at my left shoulder, my martial arts uniform had been sliced cleanly apart, and the chilly air of the underground training hall seeped through the gap.

Only after confirming that I had not been injured did I let out a relieved sigh.

“Whew.”

A Sword Energy attack out of nowhere? My heart had nearly jumped out of my throat.

“Crazy. You said you weren’t going to use Sword Energy.”

“……Only an idiot would take that at face value.”

Jin Mukyung answered with a distinctly uneasy expression and sheathed his sword.

“Training ends here.”

Ding.

> **System**
>
> - **Jin Mukyung** has declared the training complete.
>
> - The remaining **Time Limit** has vanished.
>
> - Quest success will be determined according to **Jin Mukyung’s** evaluation.

Success? Or failure?

With my eyes shining expectantly, he opened his mouth.

“You’re nowhere near good enough.”

“Ah.”

“To think this is all you managed to keep up with me after ten days. What a waste of my ti—”

Jin Mukyung stopped speaking and made a sour face.

“What’s with that expression?”

“Huh? What expression?”

“That bizarre expression you’re making right now!”

“I’m not making one. I have no idea what you’re talking about.”

But Jin Mukyung was right.

I had to make a tremendous effort to hide the corners of my mouth, which kept trying to rise. The reason was the System message floating in the air.

Ding.

> **System**
>
> - You have fulfilled the conditions for quest success!
>
> - Quest **Training? Trial!** has been completed!
>
> - Level Up!
>
> - The Quest completion Reward has been moved to your Inventory!
>
> - Excellent work. An additional Reward will be granted!

“Hm. You’re a shy child, aren’t you?”

Jin Mukyung. An honest young man.

“You bastard! What the hell is that supposed to mean?”

“No, forget it. At twenty-three, you’re still at the age when you get embarrassed easily.”

“You little—”

Jin Mukyung’s eyes went wild, and he was just about to charge at me.

At that moment—

Creak.

The door leading to the surface opened, and a servant cautiously poked his head inside.

> **System**
>
> **Level 12: Jang Childeuk**

“Um, Young Masters?”

He was the servant who had brought us meals regularly until about three days ago. Something had clearly happened while we had not seen him. His face was covered in bruises, and four or five of his teeth were broken.

He continued speaking through his damaged mouth.

“The Lesser Family Head is looking for you.”

“……Damn it.”

Jin Mukyung looked back and forth between Childeuk and me, then reluctantly lowered his fist.

* * *

We moved according to Childeuk’s directions. Jin Mukyung walked along with a sour expression, staring only at the ground as if everything offended him. Childeuk kept groaning whenever pain shot through him with each step.

“Ow. Good grief. Urgh.”

“……”

What a pain in the ass.

“How did you get hurt?”

“There was a small misunderstanding.”

That seemed like a fairly serious injury for a small misunderstanding.

In the modern world, there were potions, so there was no ailment they couldn’t cure. Murim was different. I clicked my tongue as I looked at Childeuk’s broken teeth.

“That must hurt.”

“It’s all right.”

Childeuk puffed out his chest with stoic resolve.

“A martial artist of the Jin Family of Taiyuan must be able to endure this much.”

“……”

He had been acting like he was about to die from the pain just moments ago.

But wasn’t this man a servant?

*Come to think of it, his clothes have changed.*

He was wearing the dark navy martial arts uniform worn by martial artists of the Jin Family. I thought he had been wearing a servant’s clothes before.

Noticing my gaze, he smiled shyly.

“Oh. I officially became a martial artist a few days ago.”

“A martial artist?”

Jin Mukyung, who had been walking silently behind us, suddenly spoke.

“Under whose command?”

I might have made a name for myself lately, but I was still nowhere near as famous as Jin Mukyung. Childeuk answered with an awestruck expression.

“I’m directly under the Lesser Family Head.”

“Only specially selected martial artists within our family can serve directly under our eldest brother.”

Jin Mukyung looked Childeuk up and down. His gaze was not contemptuous so much as observant, as though he were estimating Childeuk’s level.

“Your physique is decent, but you don’t seem to have learned any martial arts.”

“Yes. I’m still bewildered myself. I’ve never properly performed even a single form of martial arts.”

Childeuk’s Level, as determined through **Sense**, was twelve. That was high for a servant who had done nothing but carry food, but he was Third Rate by martial-artist standards.

*The First Rate masters directly under Jin Wikyung are at least Level 40.*

What was going on? Did he have powerful backing?

Jin Mukyung seemed to have reached the same conclusion. His brow furrowed.

“You must have good connections. What does your father do?”

Childeuk blinked his large, calf-like eyes.

“He died ten years ago.”

“……”

“……”

“He was a famous herbalist, but he was killed by a tiger.”

For a moment, my vision went hazy. As befitted a Peak master, Jin Mukyung was the first to regain his composure and hurriedly tried to smooth things over.

“Whew. He sounds like he was an excellent man.”

“Even now, I remember him as such an innocent man. He and my mother were very loving, too.”

“Then your mother, perhaps? No, never mind.”

“She’s doing well.”

Just as we let out sighs of relief, Childeuk gazed wistfully at a distant mountain.

“I buried her beside my father, so I’m sure they’re both doing well.”

“……”

“……”

What followed was a march of death. I wanted to run away at full speed, but I gave up after hearing Childeuk muttering to himself.

“Oh, I haven’t seen those flowers in a long time. I used to see them everywhere when I went into the mountains with my father.”

“……”

“……”

If we had walked together for another fifteen minutes, Jin Mukyung might have killed himself. Fortunately, after five minutes that felt like five hours, we reached our destination.

“Oh, you’re here!”

Seeing Jin Wikyung waiting in front of the pavilion nearly brought tears to my eyes. We cried out in voices thick with emotion.

“Hyuung!”

“Hyung-nim!”

Childeuk awkwardly clasped his hands in a formal salute.

“As ordered, I have escorted the Young Masters here.”

Jin Wikyung, who had been hurrying toward Jin Mukyung and me, suddenly stopped and embraced Childeuk.

“Jang Childeuk, a man of benevolence, righteousness, propriety, and wisdom! Is that you, Martial Artist Jang?”

“Yes, sir, Lesser Family Head!”

“You’ve completed a very important mission! Go and rest now.”

What on earth was happening? Jin Mukyung and I stared blankly at the scene.

Then a voice reached my ear through Sound Transmission.

*There was, uh, a minor misunderstanding between me and this fellow…*

“……”

Somehow, I thought I knew who was backing Childeuk.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 73`.

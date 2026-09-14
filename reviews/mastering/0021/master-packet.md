# Master Edit Task — Chapter 21

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

| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 이천백    | **Lee Cheonbaek**  |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 낭인     | **wandering martial artist**                     |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 지부장    | **Branch Leader**                            |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 스킬창              | **Skill Window**               |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 지능               | **Intelligence**               |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |
| 염라편 | **Yama Whip** |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |

## Matched risk notes

(No matching risk notes.)

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 15–19

## Plot

Taekyung defeats Lee Seogeun in the duel, completing the Duel Quest and gaining three levels, the Gambler title, Fame, Fourth-Stage Cultivation, and Third-Stage Qi Sense. Lee is later killed in the departing Jin Family carriage by an unidentified masked assassin using Sound Transmission, paralysis or toxin, and a blue-black needle; “going to Mount Beimang” foreshadows his death.

The Jin Family’s belief that Taekyung is the Sleeping Dragon of Shanxi earns him additional Fame. While cultivating, he discovers a powerful unidentified energy in his dantian that rejects his contact and nearly consumes the internal energy he sends toward it. His cultivation raises his Sinews and Bones, but his Status Window still shows ten years of internal energy.

The Elder Council interrogates Taekyung over Lee’s poisoning and blames him for provoking Mount Heng. Jin Wikyung rejects the proposal to hand him over and calls for war. The Head Elder unexpectedly supports Wikyung and condemns the faction that framed Taekyung, though his political motives remain unclear. Mount Heng declares war, creating a System War relationship, designating Taekyung a public enemy, and triggering the Main Quest — War. Wikyung seals the family grounds and assumes operational control.

The Jin Family is badly outmatched: roughly 200 martial artists and three Peak masters against Mount Heng’s 300 or more martial artists and five Peak masters. With Shanxi sects refusing to answer the family’s requests for aid, Wikyung accepts assistance from Wolhwa, revealed to be Eun Sowol, the Level 50 Branch Leader of the Lower District Sect’s Shanxi branch. In exchange, she demands half of Mount Heng’s shops and exclusive rights to the pleasure district.

## Continuity

- Taekyung is Lv. 17. His Cultivation, Spear, and Manoeuvre Techniques are Fourth Stage; Qi Sense is Third Stage and detects targets through Lv. 50.
- The Main Quest still requires First Rate, Lv. 30, and Fame 500 for the reward of Logout. Taekyung has 17/30 levels and approximately 70/500 Fame.
- Taekyung’s ten years of internal energy remain insufficient for advancement despite his strong physical stats. An unidentified, much stronger energy occupies his dantian and resists control.
- The Sleeping Dragon of Shanxi rumor is spreading through the Jin Family. Taekyung deliberately confirms it, gaining 10 Fame, with later belief producing periodic Fame increases.
- Lee Seogeun is dead. His masked killer remains unidentified; the assassin used Sound Transmission, paralysis or poison, and a large blue-black needle.
- Jin Wikyung is Taekyung’s protective eldest brother and acting Family Head during the war. Wipeng remains his trusted Peak-level ally.
- The Head Elder is Taekyung’s great-uncle and the Jin Family’s highest-ranking elder. He supports Wikyung publicly, but his true plan is unresolved.
- Mount Heng Sword Sect and the Jin Family of Taiyuan are at war. Taekyung is a public enemy, and fleeing incurs severe System penalties. The family grounds are sealed without Wikyung’s authorization.
- Wolhwa is Eun Sowol, a Level 50 martial artist and Lower District Sect Branch Leader. Honghwaru is that sect’s Shanxi branch. Wikyung accepted her demand for half of Mount Heng’s shops and exclusive pleasure-district rights.
- The capsule’s purpose, the route home, and the limits of Murim’s death and resurrection rules remain unresolved.

## Translation Decisions

- Preserve **Mount Heng Sword Sect**, **Mount Beimang**, **Sleeping Dragon of Shanxi**, **Lower District Sect**, **Branch Leader**, **War relationship**, **Main Quest — War**, **First Rate**, **Peak**, **Fame**, and **Logout**.
- Keep **Sound Transmission**, **Elder Council**, **Head Elder**, **acting Family Head**, and the Jin Family’s **Cultivation**, **Spear**, and **Manoeuvre Techniques** consistent.
- Render the System’s war clause as: “Those who survive are strong, and only the strong will survive.”
- Preserve the brisk dark action-comedy and Taekyung’s dry, self-mocking profanity.
- Retain the gold-spoon/**God-Spoon** wordplay with a brief footnote where needed.
- Keep the assassination cues explicit: burning throat pain or loss of voice where applicable, paralysis or toxin effects, the Mount Beimang death idiom, and the masked assassin’s blue-black needle.

### Prior accepted reading-copy tails

#### Chapter 19 tail (verified mastered)

…
you trying to pull, barging in like this? We’re expecting an important guest, too.” The timing was damn awful, too. I was in the Lesser Family Head’s office waiting for a guest from a sect called the Lower District Sect. Naturally, Jin Wikyung and Wipeng were there with me. “Taekyung.” Jin Wikyung called my name. Without even turning around, I hurriedly waved my hands. “Ah, it’s not what you think. I didn’t call her. She says she’s leaving now, too. Right?” Wolhwa’s laughter rose in pitch. “Our Young Master Jin is still so adorable. But you guessed wrong. I’m here on business.” “Don’t call me ‘our Young Master Jin.’ I’m going to live chastely from today onward. I don’t have any business with you anymore, so hurry up and leave.” “Hmm. I don’t want to.” Then there was no helping it. I would have to move her by force. In desperation, I grabbed Wolhwa around the waist and hoisted her up— “Huh?” What the hell? Why won’t she lift? Wolhwa looked slender, but was she so big-boned that she weighed a lot? *That’s bullshit.* Just how high was my Strength stat? With raw physical strength alone, I could grind a rock into powder. And yet I couldn’t lift a single female NPC, which meant— “Taekyung?” I ignored Jin Wikyung’s second call and furtively let go. Then I heightened my Qi Sense. “Ahahahahaha! This is driving me insane!” As Wolhwa laughed herself to death, a Level Window appeared above her head. At the same time, I heard Jin Wikyung call my name for the third time. > **System** > > **Lv. 50 Eun Sowol** “Taekyung, greet her. She is the Branch Leader of the Lower District Sect’s Shanxi branch…” Ah. Ahhh. *I want to die.* * * * “Greetings. I am Wolhwa, Branch Leader of the Lower District Sect’s Shanxi branch.” Eun Sowol. No, for now, let’s just call her Wolhwa. She was different from how she had acted until now. Every movement carried the grace and elegance of a noblewoman. “I am Jin Wikyung of the Jin Family of Taiyuan.” “I’m Wipeng.” I kept my mouth shut like Mute Samryong,[^1] and Wolhwa flashed me a grin. It was an ominous grin. *Don’t. Don’t smile.* *Don’t talk to me. Please don’t.* “It seems there’s one person I haven’t been introduced to.” I felt eyes boring into me. Someone stepped on my foot beneath the table. Feeling as though I were coughing up blood, I forced myself to speak. “…I’m Jin Taekyung.” “Yeees. I hope we get along too, Young Master Jin.” “Ahem.” With a cough, Jin Wikyung glanced at me. “I didn’t realize you were acquainted with my younger brother.” “He’s a regular at our establishment—the Honghwaru in Taiyuan. It also serves as our sect’s Shanxi branch.” “Ah. A regular…” I avoided everyone’s gaze. Wolhwa snorted with laughter, then got down to business. “Shall we talk business now?” I had felt it several times before, but she really was a refreshingly direct woman. Jin Wikyung and Wipeng also turned their attention away from me and joined the conversation. “First, allow me to offer my sincere thanks for the Lower District Sect’s assistance.” “Think nothing of it.” “But may I ask why you wish to help our family?” Wolhwa smiled sweetly at Jin Wikyung’s question. “The reason… I will tell you if necessary. First, we are doing this for our sect’s benefit.” “Benefit. What specific compensation do you want?” “Half of the shops and assets owned by the Mount Heng Sword Sect.” “Good.” “My lord!” Wipeng hurriedly stepped forward, but Jin Wikyung paid him no heed. Wolhwa also looked slightly surprised. “You decide quickly.” “Because I have staked everything the family has.” “Has this already been agreed upon?” “I am the Lesser Family Head, and with my father absent, I possess the authority of the acting Family Head.” “I hear the internal opposition is quite fierce. The Elder Council, for example?” “As expected of the Lower District Sect. You certainly get your information fast.” “It can’t be helped. Information is essential if you want to survive in this bleak Murim. We need at least that much resourcefulness to make a living, don’t we?” Watching Wolhwa smile, I suddenly had a thought. *That information. Did I—or rather, did Jin Taekyung—let it slip?* I had wondered where I had heard the name Lower District Sect before. It was an information-gathering sect that appeared regularly in martial-arts novels. In other words, Wolhwa, its Branch Leader, was a veteran information merchant. On top of that, she was an outstanding martial artist at Level 50. A woman like that had disguised herself as a courtesan to meet a guy like Jin Taekyung? *Even a dog would laugh at that.* I stared at Wolhwa. Her beauty was dazzling enough to make me wonder if a goddess had descended. Whenever she smiled, roses came to mind. Only now could I see the sharp thorns hidden beneath all that splendor. Jin Wikyung spoke with a stiff expression. “Then tell us the second reason.” Wolhwa answered with her usual radiant smile. “Because I like Young Master Jin.” “Excuse me?” “He’s young, handsome, well-built, and has such a cute personality.” “…” “…” *How much of that was sincere, and how much was a joke?* [^1]: Mute Samryong is the protagonist of a well-known Korean short story; his name literally means “Three Dragons.”

#### Chapter 20 tail (verified mastered)

…
carried the air of a master. He was the coachman who had brought me to the Jin Family of Taiyuan a few days ago. I never expected to see that face here. I was momentarily speechless, and Wolhwa spoke up. “I hear you two are acquainted. Last time, you crossed the boundary between life and death together and forged a deep friendship that transcended age and status…” *No. That isn’t what happened. Please stop.* I tugged at Wolhwa’s sleeve, but it was already too late. The coachman smiled gently and opened his mouth. “Even now, whenever I close my eyes, the memories of that day remain vivid. The Heavenly Axe… He was a truly strong bastard.” The gate guards, who had been listening intently, exclaimed in amazement. “Oh!” “The Heavenly Axe… Surely he means that Heavenly Axe of the Eighteen Strongholds of Green Forest?” “Wasn’t he the infamous Peak master of Green Forest? To kill a man like that, as expected, this gentleman must be…” “…” They seemed to have gotten something seriously wrong. I didn’t even know where to begin correcting them—or where to stop. While I stood there blankly, the coachman grabbed me in a hug. “If it hadn’t been for you, Young Master, I would have been in serious trouble.” This man certainly had a strange way of putting things. Without me, he would have been drinking a cup of makgeolli atop Mount Beimang by now.[^1] “Please let go of me first, then we can talk…” I was just about to pry him off when someone muttered, “Yama Whip. The master of the whip arts who vanished without a trace more than ten years ago. It’s him. It has to be.” A ripple passed through the gate guards. “Yama Whip? You mean that Peak master who roamed the realm beating down remnants of the Demonic path?” “I’ve heard that name, too. A master who stood between the orthodox and unorthodox paths, with neither his sect nor his past known… Come to think of it, didn’t his trail vanish somewhere near Shanxi?” “Then the Third Young Master—no, our Young Master—is acquainted with Great Hero Yama Whip.” “And not only that. He must have played a major role in taking down the Heavenly Axe.” “Oh! Ohhh!” Fervent gazes poured in from every direction. Perhaps sensing that something was wrong, the coachman tried to pull away, but my hand was gripping his shoulder tightly. “Young Master?” I gave him the brightest smile in the world. “To meet you again like this—Yama. Whip. Great Hero!” My words were like oil thrown onto a fire. “Woooah!” The overheated gate guards stomped their feet, while Wolhwa bent over, desperately trying to hold back her laughter. Ding. > **System** > > - Rumors about the **Poisoner** are dying down! > > - Rumors about the **Sleeping Dragon of Shanxi** are gaining credibility! > > - **Fame** increases by 20! > > - Passionate supporters have appeared! As the beautiful System notifications rang out, a famous saying came to mind. *The perfect lie… is a true story.* * * * The young man stared at the ceiling with his eyes wide open. The light had gone out of his once-bright black eyes, and his face was twisted with fear and pain. “Seogeun. My son.” A large, rough hand caressed the young man’s face. Intense poisonous energy seeped through the man’s skin, only to be stopped by the internal energy that instinctively surged within him. “How did this happen to you?” The middle-aged man lamented. He had grown up a complete orphan and spent decades in Murim. He had met countless people and watched countless people leave. From the days when he was a green twenty-year-old wandering martial artist to the moment he became the master of a sect, his memories were beyond counting. “Did it hurt? Were you so wronged that you couldn’t even close your eyes?” He quietly looked down at his son’s wide-open eyes. Every tiny blood vessel had burst, staining his eyes red. His son was barely twenty. Blood tears flowed from the eyes of a father who stood before his poisoned son. “My son.” The poisonous energy that had entered through his hand was spreading throughout his body. Within only a few breaths, his head began to spin and his limbs went numb. Such a deadly poison. He could vividly picture his son’s final moments—his entire body stiffening until he couldn’t even struggle. “I will remember this pain.” The next moment, powerful internal energy rose like a wildfire and drove the poisonous energy away. The poison that had been consuming his insides vanished in an instant, as if it had been torn apart by a pack of hundreds of wolves. “I’ll pay those bastards back a hundredfold. A thousandfold.” The Sect Leader of the Mount Heng Sword Sect, Blood Wolf Sword Lee Cheonbaek, left his son’s corpse behind and walked away. When he opened the pavilion door, he saw the black night sky and the flickering torches beneath it. A group of about two hundred fully armed men stood outside. The man at the front bowed his head. “Father.” Lee Cheonbaek nodded to his eldest son. “Go. Tonight… our revenge begins.” That night, about two hundred martial artists left the Mount Heng Sword Sect. [^1]: A reference to Mount Beimang, a famous burial ground traditionally used as a symbol of death.

## Korean source

```text
＃21화



띠링.



- [진가심법]을 수련했습니다.

- 반복 수련의 결과로 근맥과 근골이 1씩 상승합니다.



“후우.”

심호흡과 함께 눈을 떴다. 어스름한 새벽, 촛불로 밝힌 방 안은 호박빛으로 출렁이고 있었다.

‘이번에도 실패.’

고요 속에서 주먹이 불끈 쥐어진다.

몇 번째 시도였을까. 스무 번? 서른 번? 중요한 건 결과다. 이번에도 굳은 공력을 끌어내는 것에 실패했다.

‘그나마 나아지고 있다는 걸 위안 삼아야 하나?’

공력을 다루는 것에 점점 익숙해지고 있다. 내가 F급 헌터가 아니라 C급. 아니 최소 D급만 되었어도 훨씬 빨리 적응했겠지만, 현실은 냉혹한 법이다.

‘근골, 근맥이 꾸준히 향상되는 덕분인 것도 있겠지.’

공력은 인체의 혈을 타고 흐른다. 심법을 수련하면 할수록, 근골과 근맥이 향상되면 될수록 혈이 넓어지고 튼튼해진다. 처음과 비교하면 보다 더 많은 공력을, 훨씬 빠른 속도로 순환시킬 수 있었다.

‘스킬 포인트 덕분이지.’

레벨 업 한 번에 10씩 주어지는 스킬 포인트는 그 역할을 톡톡히 하고 있었다. 근골과 근맥을 향상시키는 데에는 그만한 양분이 없다.

‘스킬창 오픈.’



스킬창



[LV.17 진태경]

심법 : 진가심법 (사 성)

무공 : 진가창법 (오 성) / 진가보법 (오 성)

근골 : 105

잔여 포인트 :  0





‘가능성이 보인다.’

난공불락의 요새가 점점 작고 허술해지고 있다. 계속해서 두드리다 보면 곧 문을 열 수 있을 것 같은 느낌이다.

다행히 내가 재능은 없어도 끈기는 있는 놈이지.

‘계속 시도한다. 될 때까지.’

다시 가부좌를 틀고 운기조식을 시작하려던 찰나였다.

앞서 수차례의 운기조식 덕분에 잔뜩 곤두선 감각들 사이로, 심상치 않은 소리가 들려왔다.

‘이건…….’

웅웅웅. 언뜻 들으면 벌 떼 우는 소리처럼 들리는 그것은 사람들의 웅성거림이었다.

‘무슨 일이지?’

귓가로 공력을 흘려보냈다. 거리가 멀어서 그런지 완전히 알아듣기에는 턱없이 부족했다. 하지만 그것으로도 충분했다.

웅얼거리는 목소리들 사이에서 한 단어를 들었으니까.

‘전투!’

항산검문이다. 드디어 전투가 벌어진 것이다.

나는 황급히 가부좌를 풀고 일어섰다. 그리고 반쯤 열린 창문 너머로 뛰어내렸다.

고양이처럼 착지한 내 시야에, 차례차례 불이 밝혀지는 전각들이 들어왔다.

‘결국…….’

시작됐구나.



* * *



스물다섯. 가지런히 눕힌 시신의 숫자였다.

모든 생기를 잃은 채 고목처럼 누워 있는 그들을 확인했을 때, 할 말을 잃고 말았다.

“이건.”

나는 헌터다. 무수한 전투를 겪었고 죽음을 지켜봤다.

중독되고, 베이고, 으스러지고, 터지고…….

상대하는 몬스터에 따라 죽음의 종류도 천차만별이다. 하지만 그들에게는 한 가지 공통점이 있었다.

바로 ‘성인’이라는 것.

그건 각성의 기본 조건이었다. 어떤 기준인지, 왜인지는 아무도 몰랐다. 게이트의 존재만큼이나 자연스럽게 자리 잡은 법칙이었다.

그래서 내가 목격한 그 숱한 죽음들 중에는 어린아이의 죽음이 포함되어 있지 않았다.

‘이건 게임이다. 고작 게임이라고.’

마음속으로 계속해서 중얼거렸다. 그러나 단순히 그렇게 치부하기에는 눈앞의 광경이 너무나도 참혹했다.



혈血



이마에 아로새겨진 글자. 말라붙은 핏물 위로 횃불이 비친다. 열 명이 넘는 어린아이들이 그렇게 싸늘하게 식어 있었다.

기껏해야 중학생. 혹은 그 밑으로 보이는 아이들까지 하나도 빠짐없이. 그렇게 죽어 있었다.

“우웁!”

떨리는 손으로 횃불을 들고 있던 무사 하나가 허리를 숙이는 것을 시작으로 곳곳에서 토악질 소리가 울려 퍼졌다.

그때 무사가 떨어트린 횃불을 집어 드는 손이 있었다.

“소미. 분명 그런 이름이었지. 내가 가주 대행이 되던 날, 응현 지부장이 자신의 보물이라며 침이 마르게 자랑했었다.”

진위경이다. 그는 꺼질 듯한 눈동자로 횃불을 들어 아이들의 얼굴을 비췄다. 한 사람. 한 사람. 얼굴이 드러날 때마다 어김없이 각자의 이름이 흘러나왔다.

마지막 아이의 이름을 부른 진위경이 나를 바라봤다.

“이 아이들이 누군지 아느냐?”

“……모릅니다.”

“응현(應現), 산음(山陰), 삭주(朔州) 지부에 파견된 본가의 식솔들이다.”

그곳이 어디인지 나는 모른다. 하지만 이 아이들의 부모들이 어떤 최후를 맞았을지는 짐작할 수 있었다.

더불어 항산검문의 의도에 구역질이 났다.

‘미친 사이코패스 새끼들.’

봐라, 우리는 이런 어린아이까지도 참혹하게 죽일 수 있다. 곧 너희도 이처럼 될 것이다.

얼굴도 모르는 항산검문주의 목소리가 들리는 듯했다.

“모든 게 내 탓이다. 무공을 모르는 아이들까지 이리 참혹하게…….”

진위경이 떨리는 목소리로 자책하던 그때였다.

“그것이 전쟁의 본질이오. 소가주.”

대장로가 은빛 수염을 매만지며 나타났다. 시신들을 바라보는 그의 눈동자는 담담하게 가라앉아 있었다.

“승리와 패배. 둘 중 어디에도 죽음은 빠지지 않는 법. 항산검문주. 혈랑검 이천백이라고 했나? 그는 낭인 출신답게 전쟁을 잘 알고 있소. 이 아이들만 봐도 알 수 있지.”

그 대수롭지 않다는 말투에 나는 소름이 돋았다.

‘어떻게 돼먹은 인공지능이야.’

이 NPC는 어딘가 결여되어 있다. 그래서 더욱 위험하게 느껴진다.

나는 입을 다물었고, 진위경은 일그러진 얼굴로 입을 열었다.

“……말을 삼가시지요. 본가의 식솔들입니다.”

“아니, 저 아이들은 전사자요. 앞으로도 무수한 이들이 죽어 나가겠지. 어쩌면 지금 이 순간에도.”

“대장로. 말을 삼가라 했습니다.”

진위경이 으르렁거렸다. 사람들의 눈만 없었다면 진작 일을 냈을 기세였다. 하지만 대장로는 여전히 담담했다.

“예상하지 못했느냐?”

갑작스러운 하대였다. 하지만 나도, 진위경도 인식하지 못할 정도로 자연스러웠다.

“산음, 응현, 삭주. 모두 항산검문의 손이 닿는 곳이었다. 전날 각 지부에 전서구를 보내면서 이런 일이 벌어질 수 있음을 전혀 염두에 두지 않았단 말이냐?”

“그건…….”

“너는 알고 있었다. 그들에게 화가 미치리라는 사실을 말이다. 전서구를 보냈던 건 단순한 양심의 가책이었을 뿐이지.”

“그만. 그만하십시오.”

“훌륭한 판단이었다. 만약 지부를 구원하고자 했다면 쉬지 않고 칠 주야를 달려야 했을 것이고, 극도로 지친 상태에서 적과 싸워야 했을 테니까. 그렇지 않으냐?”

진위경은 하얗게 질린 얼굴로 대장로를 바라봤다. 꽉 쥔 주먹 사이로 선혈이 흘렀다.

“난, 나는…….”

“모든 것에는 희생이 따르는 법. 대국을 직시해라. 너는 태원진가의 수백 식솔을 책임질 소가주다.”

진위경의 몸이 부르르 떨렸다. 분노와 슬픔이 빠져나간 표정에는 왠지 모를 허탈함이 가득했다.

“희생…….”

“전쟁은 이제 막 시작되었을 뿐이오. 안 그렇소? 소가주.”

포권을 취해 보이는 대장로의 모습에, 나는 입술을 질끈 깨물었다.

‘종잡을 수 없는 노인네.’

대장로는 분명 위험한 인물이다. 가문에서의 위치, 도무지 짐작할 수 없는 속내, 어린아이들을 시체를 보고도 눈썹 하나 깜짝하지 않는 사이코패스적인 면모까지.

하지만…….

‘그의 말이 맞아.’

내 시선에서 진위경은 좋은 소가주다. 인간미도 넘치고 머리도 영특하다.

하지만 시신들을 보는 순간, 누구보다 크게 흔들렸다. 대장로의 싸늘한 일침이 아니었다면 평정심을 되찾기까지 상당한 시간이 걸렸을 것이다.

‘도움을 줬다. 다른 누구도 아닌, 바로 그 대장로가…….’

평화로울 때는 적대 관계지만 전쟁 시에는 뭉친다는 건가?

‘그럼 다행인데.’

의심과 안도가 섞인 눈초리로 대장로를 바라보던 그때였다.

“삼공자도 있었군.”

노회한 잿빛 눈동자에 가슴이 덜컥 내려앉았다. 처음으로 대장로가 내게 말을 걸어온 것이다.

“대장로를 뵙습니다.”

애써 당황을 숨기는 나를 대장로가 묘한 미소를 띠고 바라봤다.

“요새 가문 내에 재미있는 소문이 들리던데, 그게 아마…… 산서잠룡이라던가?”

저 웃기지도 않는 별명을 대장로에게서 들을 줄이야.

“일설에 의하면 염라편과 친분이 있다고도 하더군. 그와 힘을 합쳐 천력부를 쓰러트렸다던데.”

“쿨럭. 쿨럭.”

“어디 아픈가?”

“아, 아닙니다. 그냥 몸이 으슬으슬해서요.”

“저런. 곧 큰 공을 세울 사람이 그래서야 쓰나.”

어색하게 웃던 내 얼굴이 천천히 굳어졌다.

“그게 무슨 말씀이신지.”

“천력부라는 걸출한 마두를 제거하는 데 일조한 실력자라면 귀중한 전력이지. 설마 그 소문이 거짓은 아닐 테고.”

“…….”

“해서, 본가의 직계로서 앞장서서 싸우는 건 당연한 의무라고 생각되는데. 소가주의 생각은 어떠시오?”

빙긋. 대장로의 웃음을 물끄러미 바라보던 진위경이 내게 물었다.

“네 생각은 어떠하냐?”

외통수. 한 단어를 떠올린 순간, 익숙한 알림이 울렸다.

띠링.



* * *



퀘스트



[임무 수행]

당신은 백호당 정찰조장으로 임명되었습니다.

지금부터 휘하에 배속된 부하들을 이끌고 임무를 수행, 공적을 쌓으십시오!



등급 : 반복 퀘스트

제한 : 진태경

임무 : 공적치 100 달성 (0 / 100)

보상 : 성공 정도에 따라 변화합니다.

실패 : 실패 정도에 따라 변화합니다.





퀘스트창을 껐다. 이미 몇 번이나 봤을뿐더러, 잠시 자리를 비웠던 백호당 소속 무사가 지금 막 돌아왔기 때문이었다.

“조장들에게 기본으로 지급되는 물품들입니다.”

검, 그리고 백호가 조잡하게 수놓아진 흑색 무복과 나무 냄새가 물씬 나는 반들반들한 목패(木牌).

그게 전부였다.

“새로 휘하에 배속된 이들은 정찰조 숙소에서 대기 중입니다. 위치는…….”

다행히 내가 아는 곳이었다. 몇 번 오가면서 봤던 전각이 바로 정찰조에 배정된 숙소였다.

백호당을 빠져나온 후 우선 인적이 없는 골목으로 숨었다.

‘인벤토리 오픈.’

모든 복장을 갖추는 데는 10초면 충분했다. 옷을 갈아입고, 검은 인벤토리 깊숙이 처박은 다음 [예리한 창]을 꺼냈다.

지금까지야 으리으리한 개인 전각에서 삼공자의 신분을 톡톡히 누렸지만 지금부터는 다르다.

‘공동 생활이랬지.’

먹는 것도, 자는 것도 함께다. 필요할 때마다 허공에서 2m짜리 철창이 튀어나오는 마술을 보여 줄 수는 없는 법이다.

조장이라고 음각된 목패를 허리춤에 차자 태원진가의 평범한 무사1이 된 것 같았다.

‘그냥 무사는 아니지. 정찰조장이니까.’

백호당 정찰조장. 생각지도 못한 직책을 받게 됐다.

물론 여기에는 나름 치열한 의견 대립이 있었다. 대장로는 나를 장로원 계열의 전투 부대에 넣고 싶어 했고, 진위경은 극렬하게 반대했다.

‘결국 타협을 봤지.’

임무 자체는 어렵지 않은 정찰조장. 하지만 장로원 일파인 백호당주의 휘하로. 결국 어어, 하는 사이에 이런 직책을 받게 됐다.

‘이런 식으로 전쟁에 끼게 될 줄은 몰랐는데.’

배 째라 식으로 나갈 수도 있었지만 참았다. 염라편을 언급할 때마다 번뜩이는 대장로의 눈빛이 첫 번째 이유였고, 두 번째 이유는…… 어린아이들 때문이다.

‘게임이다. 전부 그래픽이고 허상일 뿐이야.’

수없이 되뇌어도 그 시신들이, 이마에 칼로 새겨진 글자가 눈앞에 어른거렸다. 맞다. 이 결정에는 감성적인 부분도 있었다.

이대로라면 좋지 않다.

‘몰입하지 말자. 현실과 게임을 혼동해서는 안 돼.’

언젠가부터 부쩍 그런 일들이 많아졌다. 처음에는 재미 삼아 NPC들을 사람처럼 대했던 것이, 요즘 들어서는 정말 사람이라고 생각하고 관계를 맺고 있었다.

그럴 때마다 깜짝깜짝 놀라곤 한다. 이것도 게임을 오래 하다 보니 생긴 부작용일지도 모르지.

“여긴가?”

어느새 정찰조의 숙소에 도착한 나는 입을 벌렸다.

갈라진 목재와 쾌쾌한 냄새. 세상에, 처마 밑에는 벌집까지 있다. 저렇게 큰 건 또 처음 본다.

‘역시 가족 같은 기업…….’

복지 수준 봐라. 아니, 어쩌면 날 싫어하는 백호당주의 심술일 수도 있겠다. 대놓고 갈구는 건 아직 못 하겠고, 엿 좀 먹어 보라 이건가.

‘그래, 일단 해 보자.’

크게 심호흡한 나는 문을 열고 한 발을 내딛었다.

끼이이익. 오래된 바닥이 울부짖는 소리가 유난히 불길했다.
```

## Current accepted English baseline

```markdown
# Chapter 21

Ding.

> **System**
>
> - Practiced the **Jin Family’s Cultivation Technique**.
>
> - As a result of repeated practice, **Sinews** and **Bones** each increase by 1.

“Whew.”

I opened my eyes, exhaling deeply. Before dawn, the candlelit room glowed amber in the darkness.

*Failed again.*

I clenched my fist.

How many times had I tried? Twenty? Thirty? The result was what mattered. Once again, I had failed to draw out the condensed internal energy.

*Should I take comfort in the fact that I’m getting better?*

I was gradually getting used to handling internal energy. If I had been a C-rank Hunter instead of an F-rank—or at least a D-rank—I would have adapted much faster. But reality was cold and unforgiving.

*My Sinews and Bones improving steadily must be helping, too.*

Internal energy flowed through the body’s meridians. The more I practiced a cultivation technique, and the more my Sinews and Bones improved, the wider and sturdier those pathways became. Compared to when I had started, I could circulate more internal energy at a much faster speed.

*It’s all thanks to the Skill Points.*

The ten Skill Points awarded with every level-up were doing their job well. Nothing could nourish my Sinews and Bones better.

*Open Skill Window.*

> **Skill Window**
>
> **Lv. 17 Jin Taekyung**
>
> **Cultivation Technique:** Jin Family’s Cultivation Technique (Fourth Stage)
>
> **Martial Arts:** Jin Family’s Spear Technique (Fifth Stage) / Jin Family’s Manoeuvre Technique (Fifth Stage)
>
> **Sinews and Bones:** 105
>
> **Remaining Points:** 0

*I can see the possibility.*

The impregnable fortress was cracking and crumbling. If I kept pounding away at it, I felt as if I could open the gate soon.

Fortunately, I might lack talent, but I had persistence.

*I’ll keep trying. Until it works.*

I was just about to sit cross-legged and begin circulating my qi again when it happened.

My senses, sharpened by the earlier rounds of circulating my qi, picked up an unusual sound.

*This is…*

A low, droning hum. At first, it sounded like a swarm of bees, but it was actually the murmur of many people.

*What’s going on?*

I let internal energy flow to my ears. Perhaps because of the distance, I couldn’t make out everything clearly. But I heard enough.

One word stood out among the indistinct voices.

*Battle!*

The Mount Heng Sword Sect. The battle had finally begun.

I hurriedly uncrossed my legs and stood. Then I leaped through the half-open window.

I landed like a cat. Before me, the pavilions lit up one by one.

*In the end…*

It had begun.

* * *

Twenty-five.

That was the number of corpses laid out in orderly rows.

When I saw them lying like dead trees, every trace of vitality gone, I was left speechless.

“This is…”

I was a Hunter. I had fought countless battles and witnessed death countless times.

Poisoned, cut apart, crushed, blown apart…

The kinds of death varied wildly depending on the monster involved. But all those deaths had one thing in common.

They were all adults.

That was one of the basic conditions for awakening. No one knew what the standard was or why it existed. It was a law as naturally established as the existence of Gates.

That was why none of the countless deaths I had witnessed had involved a child.

*This is a game. It’s just a game.*

I kept repeating the words to myself. But the sight before me was too horrific to dismiss so simply.

**BLOOD**

The character had been carved into their foreheads. Torchlight reflected off the dried blood.

More than ten children had gone cold like that.

They were middle-school age at most. Some looked even younger. Every single one of them was dead.

“Urgh!”

One of the martial artists, holding a torch in a shaking hand, doubled over, and soon the sound of retching rang out from all around us.

Then a hand reached down and picked up the torch he had dropped.

“Somi. That was definitely her name. On the day I became acting Family Head, the Branch Leader of Eung-hyeon bragged about her endlessly, calling her his treasure.”

It was Jin Wikyung. With eyes that seemed ready to go out, he lifted the torch and illuminated the children’s faces.

One by one.

As each face was revealed, he unfailingly spoke its name.

After naming the last child, Jin Wikyung looked at me.

“Do you know who these children are?”

“…No.”

“They were members of our family sent to the branches in Eung-hyeon, Saneum, and Sakju.”

I didn’t know where those places were. But I could guess what end the children’s parents had met.

And I was sickened by the Mount Heng Sword Sect’s intentions.

*Those lunatics. Those fucking psychopaths.*

*Look. We can slaughter even children this young. Soon, you’ll end up the same way.*

I could almost hear the voice of the Mount Heng Sword Sect’s Sect Leader, whose face I had never seen.

“This is all my fault. To slaughter even children who don’t know martial arts so cruelly…”

Jin Wikyung was blaming himself in a trembling voice when—

“That is the essence of war, Lesser Family Head.”

The Head Elder appeared, stroking his silver beard. His gaze was calm as he looked over the corpses.

“Victory and defeat—neither comes without death. The Mount Heng Sword Sect’s Leader—Blood Wolf Sword Lee Cheonbaek, was it? As one would expect of a former wandering martial artist, he understands war well. These children alone make that clear.”

The casual way he said it sent a chill through me.

*What the hell is wrong with this AI?*

This NPC was missing something. That made him feel even more dangerous.

I kept my mouth shut, while Jin Wikyung spoke with a twisted expression.

“…Please choose your words carefully. They are members of our family.”

“No. Those children are casualties of war. Countless more will die from now on. Perhaps even at this very moment.”

“Head Elder. I told you to watch your words.”

Jin Wikyung growled. Had we been alone, he would have been ready to start something right then and there.

But the Head Elder remained calm.

“Did you not anticipate this?”

He had suddenly switched to informal speech, yet it was so natural that neither Jin Wikyung nor I even registered it.

“Saneum, Eung-hyeon, Sakju. All of them were places within the Mount Heng Sword Sect’s reach. When you sent messenger pigeons to the branches the day before, did you truly not consider that something like this might happen?”

“That…”

“You knew harm would come to them. Sending those pigeons was nothing more than a way to ease your conscience.”

“Enough. Please, enough.”

“It was an excellent decision. If you had wanted to save the branches, you would have had to run for seven days and nights without rest, then fight the enemy in a state of extreme exhaustion. Isn’t that right?”

Jin Wikyung stared at the Head Elder with a pale face. Fresh blood flowed between his tightly clenched fingers.

“I—I…”

“Everything comes with a sacrifice. Look at the bigger picture. You are the Lesser Family Head responsible for the hundreds of family members of the Jin Family of Taiyuan.”

Jin Wikyung’s body trembled. The anger and sorrow had drained from his face, leaving it filled with a strange emptiness.

“Sacrifice…”

“The war has only just begun. Isn’t that so, Lesser Family Head?”

The Head Elder made a respectful fist-and-palm salute. I bit down hard on my lip.

*What an impossible old man to figure out.*

The Head Elder was clearly dangerous. His position in the family, his utterly unreadable motives, and even his psychopathic side—he didn’t so much as twitch an eyebrow while looking at the corpses of children.

But…

*He was right.*

From my perspective, Jin Wikyung was a good Lesser Family Head. He was deeply humane and sharp-minded.

But the moment he saw the corpses, he had been shaken more than anyone. Without the Head Elder’s cold rebuke, it would have taken him a long time to regain his composure.

*He helped. The Head Elder, of all people…*

*Were they enemies in peacetime but united during war?*

*Then that’s fortunate.*

I was looking at the Head Elder with a mixture of suspicion and relief when he spoke.

“So the Third Young Master is here as well.”

My heart dropped at the sight of those shrewd gray eyes. It was the first time the Head Elder had spoken to me.

“Greetings, Head Elder.”

The Head Elder looked at me with a strange smile as I did my best to hide my surprise.

“I’ve been hearing an interesting rumor within the family lately. Something about… the Sleeping Dragon of Shanxi?”

I never expected to hear that ridiculous nickname from the Head Elder.

“I’ve also heard that you are acquainted with Yama Whip. They say you joined forces with him to defeat the Heavenly Axe.”

“Cough. Cough.”

“Are you ill?”

“N-no. I’m just feeling a little chilly.”

“Oh dear. That won’t do for someone who is about to accomplish great things.”

My awkward smile slowly froze.

“What do you mean?”

“Someone capable of helping eliminate an exceptional demon like the Heavenly Axe is a valuable asset in battle. Surely that rumor isn’t false.”

“…”

“Therefore, as a direct-line member of our family, I believe it is only natural that you take the lead in battle. What do you think, Lesser Family Head?”

The Head Elder smiled faintly. Jin Wikyung, who had been gazing at that smile, asked me,

“What do you think?”

I was cornered.

The moment the word came to mind, a familiar notification rang out.

Ding.

* * *

> **System**
>
> **Quest**
>
> **Mission**
>
> You have been appointed reconnaissance squad leader of White Tiger Hall.
>
> From now on, lead the subordinates assigned under you on missions and build merit!
>
> **Grade:** Repeating Quest  
> **Restriction:** Jin Taekyung  
> **Mission:** Achieve 100 Merit (0 / 100)  
> **Reward:** Changes according to the degree of success.  
> **Failure:** Changes according to the degree of failure.

I closed the Quest Window. I had already seen it several times, and besides, the White Tiger Hall martial artist who had been away for a while had just returned.

“These are the supplies issued to squad leaders.”

A sword.

A black martial uniform with a crude white tiger embroidered on it.

And a smooth wooden plaque that smelled strongly of fresh wood.

That was everything.

“The newly assigned members are waiting at the reconnaissance squad’s quarters. The location is…”

Fortunately, I knew the place. The pavilion I had passed several times was the quarters assigned to the reconnaissance squad.

After leaving White Tiger Hall, I first ducked into an empty alley.

*Open Inventory.*

Ten seconds was enough to put on the full uniform. I changed clothes, shoved the sword deep into my Inventory, then pulled out the *Sharp Spear*.

Until now, I had thoroughly enjoyed the privileges of being the Third Young Master in a lavish private pavilion.

But things were different from here on out.

*It’s communal living, right?*

We would eat together and sleep together. I couldn’t have a two-meter iron spear pop out of thin air whenever I needed one.

Once I hung the wooden plaque engraved with *Squad Leader* at my waist, I felt like I’d become Ordinary Martial Artist #1 of the Jin Family of Taiyuan.

*Not just an ordinary martial artist. I’m a reconnaissance squad leader.*

White Tiger Hall reconnaissance squad leader.

I had never expected to receive a position like this.

Of course, there had been some fierce disagreement over it. The Head Elder wanted to place me in a combat unit under the Elder Council faction, while Jin Wikyung had vehemently opposed him.

*In the end, we reached a compromise.*

The mission itself was easy enough, but I would be serving under the command of White Tiger Hall’s Leader, who belonged to the Elder Council faction.

Before I knew it, I had received this position.

*I never imagined this was how I’d get dragged into the war.*

I could have just told them to do whatever the hell they wanted, but I held back. The first reason was the Head Elder’s eyes, which flashed every time Yama Whip was mentioned.

The second reason was…

The children.

*It’s a game. It’s all graphics and nothing more than an illusion.*

No matter how many times I repeated that to myself, the corpses and the character carved into their foreheads kept flickering before my eyes.

Part of this decision had been emotional.

This wasn’t good.

*Don’t get immersed. I can’t confuse reality with the game.*

Things like this had been happening more and more often lately. At first, I had treated the NPCs like people for fun. But these days, I was actually thinking of them as real people and forming relationships with them.

Every time it happened, I was startled.

Maybe this was a side effect of playing the game for too long.

“Is this it?”

Before I knew it, I had arrived at the reconnaissance squad’s quarters, and my mouth fell open.

Cracked wood and a musty smell.

Good lord, there was even a beehive under the eaves. I had never seen one that big before.

*Just like a company that treats you like family…*

Look at those benefits.

Or maybe it was a mean-spirited prank by the White Tiger Hall Leader, who disliked me. Perhaps he couldn’t openly give me grief yet, so this was his way of telling me to eat shit.

*All right. Let’s give it a shot.*

I took a deep breath, opened the door, and stepped inside.

Creeeak.

The old floor let out a wailing sound that felt especially ominous.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 21`.

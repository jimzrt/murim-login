# Master Edit Task — Chapter 105

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
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 낭인     | **wandering martial artist**                     |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 지부장    | **Branch Leader**                            |
| 산서지부장  | **Shanxi Branch Leader**                     |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 매력               | **Charm**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 100–104

## Plot

Im Chunsoo learns that Sangdong Guild’s investigation of the Peace Guild failed, Hong Woojin disappeared, and the Security Team was defeated by Jin Taekyung. Taekyung interrogates the captured Hunters, confirms that Woojin was hired by Team Leader 1 and that Im Chunsoo directed the operation, then faces Chunsoo in person. Chunsoo tests him with ice spikes, but Taekyung counters with Fire Wall before Level 80 mage Kim Hwajong arrives. Hwajong’s former-instructor relationship with Chunsoo is revealed, along with Chunsoo’s deep fear and obedience toward him. Team Leader 1 conceals the encounter and formally warns the Security Team over its unauthorized escalation.

Taekyung buys a two-story house in Goyang for his family and plans to live there alone until Hayeon finishes her entrance exam. After moving out of Hope Goshiwon and logging into Murim, he discovers Seong Jinho emerging from the capsule inside the new house.

In Murim, Taekyung, Jin Mukyung, and Hyuk Mujin travel through a blizzard to Honju. They stay at the Phoenix Inn, where Mujin’s travel funds rapidly dwindle under Taekyung’s appetite. When martial artists ruin Taekyung’s chicken-and-corn soup and provoke him, he punches the first aggressor. The inn’s proprietress hears that the Sleeping Dragon of Shanxi subdued six men, recognizes the name, and goes to meet him.

## Continuity

- Im Chunsoo is Sangdong Guild’s Level 75 A-rank ice-mage Guild Master; the failed Security Team operation against Taekyung was conducted under his special order.
- The Security Team’s six Hunters were defeated and captured, then released by Team Leader 1. Choi Byungil’s team faces formal discipline; the final punishment remains unknown.
- Team Leader 1 assesses Taekyung as a top-tier B-rank or possibly A-rank Hunter.
- Hong Woojin is a B-rank Familiar mage hired by Team Leader 1. The relationship between Woojin’s investigation and Sangdong’s operation remains unresolved.
- Kim Hwajong is a Level 80 mage, former Hunter Training Center instructor, and the trainer who traumatized Class 25 trainee Im Chunsoo. Why he arrived at the confrontation—and why he now works as a butler—remains unknown.
- Taekyung owns a two-story detached house in Goyang and intends it as his family’s home. Logout remains active, so he no longer needs the capsule for travel between worlds.
- Seong Jinho unexpectedly emerged from Taekyung’s capsule inside the new house. How and why he entered remains unknown.
- Taekyung’s current Quest requires him to deliver the Jin Family of Taiyuan’s Lunar New Year invitation to the Mount Heng Sword Sect, now led by Lee Seowol, his former accuser.
- Taekyung, Mukyung, and Hyuk Mujin are staying at the Phoenix Inn’s private residence in Honju. Wikyung gave Mujin fifty silver nyang for the journey; Mujin has five silver nyang left after paying half the lodging fee.
- Mukyung is a Peak master who uses a superficially learned heat-yang technique to warm Hyuk Mujin and considers enduring hunger martial training.
- The unnamed Phoenix Inn proprietress knows the name Sleeping Dragon of Shanxi and has gone to meet Taekyung after hearing about the fight.
- The three possible surveillance properties near Taekyung’s former home remain unidentified, as do the black Familiar’s immediate instructions and the final consequences of the Phoenix Inn fight.

## Translation Decisions

- Retain **Familiar**, **Logout**, **Inventory**, **Qi Sense**, and **Fire Wall**.
- Render **아가리 봉인술** as **mouth-sealing technique**.
- Render **교관님** as **Instructor**, **1번 훈련생** as **Trainee Number One**, and **춘수** as **Chunsoo** when used familiarly by Hwajong.
- Render Im Chunsoo’s **자네** as **you** while preserving his blunt senior voice.
- Render **열양공** as **heat-yang technique** and related **화기** as **fire qi**.
- Render **원단** as **Lunar New Year**.
- Render **항산검문주** as **Sect Leader of the Mount Heng Sword Sect**.
- Render **별채** as **private residence**, **냥** as **nyang**, and **봉황객잔** as **Phoenix Inn**.
- Render **계용옥미갱/계용옥미앵** as **chicken-and-corn soup**, preserving the latter as a spelling variant.
- Render **형장** as **Brother** in the martial artists’ address to Taekyung.

### Prior accepted reading-copy tails

#### Chapter 103 tail (verified mastered)

…
do while I was asleep?” “While you were sleeping? Didn’t you say you were circulating your qi before that?” “…I did?” It had been so long that I couldn’t even remember. But that wasn’t important right now. “You hit someone while they were sleeping?” “You looked so pathetic that I did. A martial artist like you sprawled out asleep instead of training.” “You call yourself a martial artist, yet you underhandedly attack a defenseless opponent?” “Then shall we get off right now and have a bout? Like true martial artists?” We both sprang to our feet and glared at each other without waiting for the other to move first. Jin Mukyung spoke in an ominous tone. “Hyung Mujin.” “It’s Hyuk Mujin. Second Young Master, please.” “Stop the carriage.” “…Yes, sir.” The carriage slowly began to decelerate. Now it was my turn. I met his gaze and spoke. “Hyuk Mujin.” “Ah, why me this time, Captain?” “Keep going.” “Haah, this is driving me crazy.” The carriage began to speed up again. As I slowly sat back down, Jin Mukyung asked incredulously, “Didn’t I suggest that we have a bout like martial artists?” “How pathetic. The mission comes first, and fighting comes after. And…” “And?” “I never said we should fight. I only said you were underhanded.” “…” I said it as confidently as possible, but there was no hiding how lame it looked. I snuck a look at Jin Mukyung’s Level window. > **System** > > **Lv. ??? Jin Mukyung** *Right. Come on, fighting him the moment I got back would be a bit much.* * * * *Check the Quest window.* Ding. > **System** > > **Quest** > > **Yesterday’s Enemy, Today’s Ally** > > Now that all the truth has been revealed, the Mount Heng Sword Sect is no longer an enemy but an ally you must join forces with. Invite them to the Jin Family of Taiyuan for the upcoming New Year’s Day. > > **Grade:** First Rate > > **Restriction:** Jin Taekyung > > **Mission:** Deliver the invitation (Incomplete) > > **Reward:** ??? > > **Failure:** None I took another look at the last Quest I had received. It was an easy mission. The Quest’s Grade wasn’t particularly high, and there was no penalty for failure. All I had to do was deliver the invitation to the Mount Heng Sword Sect. *The Mount Heng Sword Sect…* The current Mount Heng Sword Sect had been reduced to its bare bones. Once Lee Seogeun was poisoned and the pillar known as Lee Cheonbaek fell, its collapse had been swift. *The battle at Eight Spring Gorge was the fatal blow.* They say words without feet can travel a thousand li. That day’s battle, watched by countless eyes and ears, spread rapidly through messenger pigeons and word of mouth. With nearly all its main forces gone, the Mount Heng Sword Sect became easy prey for someone. *Wandering martial artists. And mounted bandits.* They said as many as two hundred attackers had suddenly raided the Mount Heng Sword Sect. After two days and nights of fighting, the attackers were driven off. Lee Seogwang, who had remained at the sect after being placed under disciplinary confinement, ultimately fell in battle. The Mount Heng Sword Sect needed a new rallying point, and one person emerged. *Lee Seowol.* Lee Cheonbaek’s last surviving descendant and the current Sect Leader of the Mount Heng Sword Sect. We had to deliver this invitation to her. The problem was… *Things between us were seriously awkward.* Actually, “awkward” was putting it mildly, at least from my perspective. In a way, the two of us had been at the starting point of all this. *I think it was right after I came out of the training hall.* I remembered Wipeng’s words exactly, down to the last syllable. “Is it true that you tried to force yourself on the daughter of the Mount Heng Sword Sect?” These days, everyone knew I was innocent. But back then, I had been treated like the worst bastard under heaven. Lee Seogeun, who had come to pressure the Jin Family of Taiyuan with fabricated evidence, was poisoned on his way home, and that was the beginning of everything. *It’s only been a month or two.* The Third Rate wastrel despised by his own family had become the Sleeping Dragon of Shanxi, while the woman whose name I hadn’t even known was now the new Sect Leader of the Mount Heng Sword Sect. We had both gone through so many changes in that time that, in a sense, we had something in common. *Our positions are very different, though.* The Jin Family of Taiyuan was now, by everyone’s admission, the foremost family in Shanxi. The Mount Heng Sword Sect, on the other hand, was nothing more than an empty shell. In truth, this invitation was practically an offer to surrender and come under the Jin Family of Taiyuan. I would have to experience it firsthand to know how Lee Seowol would react. *I just hope she doesn’t suddenly stab me.* Just as I closed the Quest window, sunlight streamed in and the sound of a boisterous crowd drew closer. Hyuk Mujin looked at me, his face flushed with excitement. “We’re at Honju.” The distance between her and me had narrowed to two days. [^1]: The Jade Emperor and Primordial Heavenly Venerable are major figures in Daoist cosmology.

#### Chapter 104 tail (verified mastered)

…
hadn’t laughed at me…* Regret always comes too late. Hyuk Mujin hurriedly began working the abacus in his head. *The expense money is gone. But I brought some emergency savings just in case, so maybe I can somehow manage.* Five silver nyang. Every coin he had saved until now. He had brought it in case of an emergency, never expecting to actually spend it. *If I don’t indulge too much, I should be able to hold out until we return.* But there was one thing Hyuk Mujin had failed to consider. Jin Taekyung’s appetite. Slurp. Gulp. Munch, munch. “Wow, this really melts in your mouth.” “……” Beggar’s Chicken, Fish-Fragrant Shredded Pork, Maechae Guyuk,[^1] scallion tofu, Kung Pao chicken… Every time one of those dishes—or any of the dozen others—arrived at the table, Jin Taekyung’s hand moved like lightning. “Wow, this is really good. So juicy.” “……” “You’re not eating? Then I’ll finish the rest too.” “……” “Wow, this broth is incredible.” “…Please, eat as much as you like.” At some point, a single tear rolled down Hyuk Mujin’s cheek. *The dishes served so far already cost five silver nyang.* His last hope was gone. Judging by the way things were going, that pig looked ready to devour another twenty plates. Hyuk Mujin wanted to smash a plate over the pig-like bastard’s head, but he restrained himself. He didn’t want to lose his life on top of his entire fortune. *Jade Emperor, Primordial Heavenly Venerable. Please, stop that bastard.* Just as he cursed the heavens— Crash! * * * The hardest parts of life in Murim were, first, survival and, second, the food. For some reason, everything was spicy, salty, and greasy, leaving me craving soup at every meal. In that sense, the dish just placed on the table held special significance. *Chicken-and-corn soup.* It was a kind of corn soup with egg whisked through it until silky smooth. I lowered my head slightly and smelled it. The distinctive savory scent of corn lingered at the tip of my nose. *Yes, this is it.* A smile rose naturally to my face. My stomach had already started feeling greasy. Once I settled it with the chicken-and-corn soup, I could probably clear another ten plates. *All right, then, now…* Just as I grasped the hot ceramic bowl with pleasant anticipation— Crash! Clatter, clatter! “…Huh?” It happened in an instant. A liquor bottle shattered in the middle of the table, exploding into hundreds of ceramic shards that flew in every direction. Along with them came the little liquor left inside. Pitter-patter. Drenched by the sudden shower, I was left speechless. *How could this happen?* The chicken-and-corn soup I had been eagerly awaiting—the warm, savory broth that would gently soothe my stomach—was no longer there. What now filled the ceramic bowl was nothing more than food waste mixed with liquor and pieces of pottery. Across from me, Hyuk Mujin stared with his mouth hanging open. “Oh, Jade Emperor. Primordial Heavenly Venerable.” Ignoring his nonsense, I slowly turned toward the direction the bottle had come from. Five men were looking our way and snickering. “Oh, Brother. Sorry about that.” “Who can you blame when your hand slips? We can just order him another one.” “Hey, don’t say anything crazy. Didn’t you see how much that bastard’s been eating?” I watched them snicker among themselves, then crooked a finger. The one who had apologized first. That bastard was the culprit who had ruined my chicken-and-corn thoup. “What, you want me to come over?” He gave a short laugh, rose from his seat, and strode toward us. His martial robes reeked of sweat and blood, and a curved saber hung from his left hip. That was the source of his confidence. *All right. Let’s handle this rationally.* I spoke calmly. “The ancient sages said that even a dog shouldn’t be disturbed while it’s eating. Apologize properly and order the food again. Starting with the chicken-and-corn thoup.” “Well, listen to the little brat lisp.” “What about the apology?” “Come on, kid. Stick out your tongue. I’ll pull it out for you.” He grinned, revealing teeth rotted black. The horrific stench of his breath wiped away my appetite as if it had been washed clean. I supposed I would have to eat the thoup later. “Open your mouth. My fist is going in.” As the words left my mouth, I drove my fist into his face. Crack! * * * There were three reasons the Phoenix Inn was famous. But the third was why so many people—men in particular—flocked there. The beautiful proprietress, whom one could only meet on a lucky day. And today was that day. “It’s noisy.” The proprietress’s clear yet languid voice was not directed at herself. The presence outside her door vanishing proved it. A moment later, a quiet voice came from beyond the door. “A fight has broken out between martial artists.” The proprietress clicked her tongue softly before speaking. “Did anyone die?” “One man subdued the other six.” “Who is he? Where is he from?” “He’s the Sleeping Dragon of Shanxi.” The proprietress laughed soundlessly. “What a welcome name. I should go see his face after all this time.” She rose from where she had been reclining. Moonlight filtering through the window gleamed upon her slender, long-stemmed tobacco pipe. [^1]: *Maechae Guyuk* is an abbreviated name for pork belly steamed with preserved mustard greens.

## Korean source

```text
＃105화



콰직!

악취 나는 주둥이에 주먹을 꽂는 순간 직감했다. 저놈이 앞으로 먹을 수 있는 건 계용옥미갱뿐이라는 걸.

쿠당탕! 쾅!

일직선으로 튕겨 나간 첫 번째 놈은 몸이 땅에 닿기도 전에 정신을 잃었다.

31레벨. 일류 초입에 든 무인이지만 내 주먹을 피할 수는 없었다.

“시발놈이 어디서 입 냄새를 풍겨, 밥맛 떨어지게.”

순간 객잔의 모든 소리가 멎었다. 그러나 그건 아주 잠깐에 불과했다.

“광수가 당했다!”

“이 애새끼가!”

“죽여!”

차차창!

일제히 뽑혀 나온 다섯 개의 곡도. 살기로 번들거리는 다섯 쌍의 눈동자. 비명과 함께 객잔의 손님들이 흩어진다.

문득 방금 쓰러진 놈에게서 나던 피비린내가 생각났다.

‘허, 이놈들 봐라?’

살인에 익숙한 놈들이다. 먼저 시비를 건 주제에 병장기를 꺼내는 걸 주저하지 않는 모습만 봐도 알 수 있다.

“너네 뭐 하는 놈들이냐?”

“저승사자.”

대답과 동시에 놈들이 달려들었다. 네 개의 곡도가 사지를, 남은 하나는 가슴을 정확히 노리고 찔러 들어온다.

쉬쉬쉭!

느리다. 다섯 놈 중 일류가 하나, 이류가 넷.

날 어떻게 해 보겠다는 생각은 야무졌지만 발은 느리고 정면에서 펼친 도의 그물은 허술하다.

“다음부터는 최소한 포위라도 해라.”

친절한 조언과 함께 놈들을 향해 양손을 떨쳤다. 아주 짧은 순간, 인벤토리에서 소환된 단검 두 자루가 허공을 갈랐다.

쉬쉭!

단검 투척. 무림에서는 비도술이라고 하나?

실전용으로 배운 적은 없지만 괜찮다. 날이건, 자루건 우선 맞기만 하면 되니까.

빡! 털썩.

그래, 저렇게.

검 자루에 이마가 깨진 한 놈이 비명도 못 지르고 그대로 고꾸라졌다. 그럼 다른 하나는?

캉!

“어디서 얕은수를!”

운이 좋은 건지, 생각보다 눈이 좋은 건지 용케 막았다.

나는 놈을 향해 활짝 웃어 주었다.

“그 단검이 네 단검이냐?”

“네놈이 던져 놓고 무슨 개소리냐!”

“정직한 아이로구나. 상으로 둘 다 주마.”

뻑, 뻑!

“꺼흑. 분명 손이 비었…….”

털썩.

“내 단검은 무한 증식이란다.”

태원진가에서 출발하기 전에 무기 창고에 먼저 들르길 잘했다.

빈손으로 들어가서 빈손으로 나왔지만 지금 인벤토리에는 전리품으로 노획한 병장기 수십 개가 쌓여 있다.

“이, 이게 무슨.”

눈 깜짝할 사이에 벌어진 일. 남은 세 놈이 달려들다 말고 주춤거리며 물러났다.

“안 와? 그럼 내가 간다?”

“자, 잠깐, 소협! 저희가 무례를 저질렀습니다. 정중하게 사과드리고 변상을…….”

태세 전환 하는 속도 봐라.

방금만 해도 애새끼 운운하던 놈들이 소협은 무슨.

“사과?”

“예, 예!”

“필요 없어!”

나는 주먹을 불끈 쥐고 놈들을 향해 달려들었다. 이런 놈들을 처리하는 데에는 무공도 필요 없다.

“제기랄, 쳐!”

쉬이익!

옆으로 한 걸음.

정수리를 향해 일직선으로 내리 찍히는 곡도를 피했다. 이어 비어 있는 옆구리에 일권(一拳)을 내지른다.

우드득.

헉, 억눌린 신음과 함께 쓰러지는 놈을 뒤로하고 다음 상대를 향해 달려들었다. 머리 위로 35레벨이라 적힌 시스템창이 보인다.

“놈!”

쐐애액!

일류 고수답게 제법 무공을 익힌 티가 난다. 군더더기 없는 동작과 정확히 급소를 노리고 휘둘러지는 곡도.

하지만…….

‘압도적인 힘과 속도 앞에서는 무용지물이지.’

레벨과 공력이 낮을 뿐, 능력치로 따지자면 일류를 아득하게 뛰어넘은 나다. 거기다 더해 무림에서 쌓은 전투 경험까지. 이놈은 결코 내 상대가 될 수 없다.

콰직!

초점이 사라진 눈동자. 미처 끝까지 휘두르지 못한 곡도가 손아귀에서 미끄러진다.

철그렁.

이 모든 광경을 지켜본 마지막 한 놈은 반쯤 넋이 나갔다.

“조, 조장이 고작 일 합 만에…… 넌 누구냐?”

“통성명은 내 주먹이랑 해야지. 자, 얘는 오른손이라고 해. 너는?”

불끈 쥔 오른 주먹을 들고 다가서자 놈이 허공에 곡도를 붕붕 휘둘러 댔다.

“오, 오지 마!”

“부탁은 공손히 해야지.”

“오지 마십시오!”

“이걸 진짜 하네.”

그래도 저렇게까지 공손하게 부탁하는데 들어줘야지.

내가 걸음을 멈추자 놈의 얼굴에 화색이 돈다.

“가, 감사합니다! 앞으로 착하게 살겠습니다!”

“뭘 감사까지. 그리고 착하게 안 살아도 돼.”

“예?”

“개과천선이라는 게 그렇게 쉽게 되는 게 아니거든. 안 그러냐, 무진아?”

어느새 놈의 뒤에 서 있던 혁무진이 대답했다.

“그럼요.”

“헉!”

헛숨을 들이켜며 돌아봤지만 이미 늦었다. 혁무진이 손에 든 나무 의자를 녀석의 정수리로 있는 힘껏 내리찍는 중이니까.

빡!

둔중한 소리와 함께 마지막 한 놈이 쓰러진다. 혁무진이 의자를 내려놓으며 중얼거렸다.

“고맙고, 미안하다.”

“저런 놈들한테 뭐가 고마워?”

“그런 게 있습니다.”

어째 상당히 건방진 눈빛인데, 저거.

오랜만에 한 대 쥐어박을까 고민하고 있던 그때 쓰러진 놈들의 품을 뒤지던 혁무진이 고개를 갸웃거렸다.

“어라? 조장님, 이놈들 좀 수상한데요?”

“뭐가?”

“이것 좀 보세요.”

혁무진이 한 놈의 소매를 쓱 걷어 올리자 마치 인두로 지진 듯한 흉터가 드러난다. 아니, 단순한 흉터가 아니다.

이건 마치…….

“문신?”

조잡하고 야만적이지만 분명 그건 일종의 문신이었다. 달리는 말의 형태를 한.

“이놈 하나만 그런 거 아냐?”

“모르겠습니다. 아직 다 확인해 본 게 아니라서.”

“다른 놈들도 확인해 봐.”

“옙.”

혁무진이 기절한 놈들을 한곳에 모아 상의를 벗겼다. 팔뚝, 가슴, 목. 위치는 조금씩 달라도 하나같이 말 문신을 새겼다.

‘어떤 단체에 소속되어 있다는 건데…….’

단순한 불량배가 아니라는 사실은 알고 있었다. 일류 고수가 둘이나 포함되어 있는 데다가 마지막 한 놈이 무심코 흘렸던 단어가 마음에 걸렸기 때문이다.

‘분명히 조장, 이라고 했었지.’

다른 문파에 소속된 무인들? 아니다. 그런 것치고는 풍기는 기세가 거칠고 복장도 통일되어 있지 않았다.

차라리 제법 규모가 있는 낭인 집단일 가능성이 크다.

‘말 문신, 말 문신이라.’

그때 문득, 어떤 단어가 뇌리를 스쳤다. 항산검문과의 전쟁 당시 처음으로 들었던 이름이다.

“마적(馬賊)?”

내 중얼거림에 어디선가 대답이 들려왔다.

“북쪽 고원(高原)에는 수십 개의 마적단이 있답니다. 이천백이 그들을 고용한 건 큰 실수였어요.”

나른하면서도 고혹적인 목소리의 주인을 찾아 고개를 돌렸다. 2층으로 통하는 계단 위, 얼굴에 면사를 드리운 한 여인이 서 있었다.

“오랜만이네, 우리 공자님.”

우리 공자님?

그 한마디를 듣는 순간, 여인의 정체를 알 수 있었다.

‘월화.’

바로 그녀다.



* * *



나와 혁무진이 안내된 곳은 봉황객잔의 최상층에 있는 객실이었다. 말이 객실이지, 층 전체를 쓰는 거라 일종의 펜트하우스라고 해야 맞겠다.

“이곳에 사내를 들이는 건 처음이네요. 그것도 둘씩이나.”

은은한 불빛에 물든 월화의 미소는 눈부셨다. 첫 만남 때부터 느꼈지만 진짜 팜므파탈이 따로 없다.

이미 몇 번 만난 적이 있는 나도 속이 울렁거릴 정도인데, 혁무진은 말할 것도 없었다.

“사, 삼생의 영광입니다.”

“…….”

이 새끼 눈 풀린 것 보소. 아주 제대로 뻑이 간 모양인데.

혁무진을 향해 싱긋 웃어 보인 그녀가 내게로 시선을 던졌다.

“진 공자는 잘 지냈어요? 아, 이제는 예전처럼 공자님이라고 부를 수도 없으려나?”

월화의 짓궂은 표정을 보니 무슨 말이 나올지 충분히 예상이 간다. 나는 황급히 손을 내저었다.

“그냥 편하게 부르세요. 예전처럼.”

“음, 그럼 잠룡 공자 어때요?”

“……끔찍한데요.”

“어머, 왜? 산서잠룡, 멋있잖아요. 약관에 그 정도 무명(武名)을 얻었으면 좀 더 자랑스러워해도 될 텐데.”

산서잠룡이나, 불꽃 카리스마 태경이나 오십보백보다. 내 표정을 본 월화가 키득거리며 곰방대를 물었다.

“농담이에요. 하여간 진 공자는 놀리는 재미가 있어서 좋다니까.”

“저어, 끼어들어서 죄송합니다만.”

약간 정신이 돌아온 혁무진이 나와 월화를 번갈아 본다.

“혹시 두 분이 어떤 사이신지?”

“알 거 없어.”

구구절절 설명하기에는 좀 쪽팔린 관계다. 칼같이 잘라 내며 월화를 향해 눈짓했다. 대충 장단 맞춰 달라는 신호.

그녀도 눈치 빠르게 알아듣고 고개를 끄덕였다.

“우리 가게 단골손님이었어요. 지금은 아니지만.”

“…….”

알아듣긴 개뿔이.

하긴, 진위경과 위팽 앞에서도 스스럼없던 그녀가 이제 와서 감추는 것도 웃기긴 하다.

한편 월화의 대답에 혁무진은 제대로 이해하지 못했는지 반신반의하는 얼굴이었다.

“그 가게라는 게 봉황객잔을 말씀하시는 겁니까?”

“아니? 이건 부업이고. 본업은 따로 있죠. 나처럼 아름답고 매력 있는 여인만이 할 수 있는 일.”

“그럼 혹시…….”

“젊은 무사님이 생각하는 그게 맞을걸?”

“기루?”

“정답.”

혁무진의 눈이 커졌다.

“소문으로만 듣던 봉황객잔의 여주인이 기녀였다니.”

“무사님, 말조심하셔야겠어요. 듣는 입장에서는 기분이 별로거든.”

“기분 나빴다면 사과하겠소. 허나 지금 소저의 언행도 그리 좋게 보이지만은 않는구려.”

갑자기 정색하는 녀석의 모습에 내가 더 당황했다.

“야, 너 왜 그래?”

“조장, 아니 공자님은 태원진가의 직계이십니다. 설령 천하제일미(天下第一美)라 해도 공자님께 이리 소홀히 대할 수는 없는 법. 본가의 식솔로서 좌시할 수 없어 나선 것입니다.”

“아까는 삼생의 영광이라며.”

“……아무튼, 한낱 기녀가 어찌 공자님께. 억!”

시원하게 뒤통수를 후려갈긴 내가 입을 열었다.

“하오문 산서지부장이셔.”

“하오문 산서지부장이건 뭐건, 예? 뭐요?”

“귀 막혔냐? 하오문 산서지부장님이시라고. 이번 항산검문과의 전쟁에서 아주, 매우, 결정적인 도움을 주신.”

“난 괜찮아요, 진 공자.”

월화가 슬픈 듯이 눈을 내리깔았다.

“어차피 한낱 기녀일 뿐이니까.”

잠시 침묵하던 혁무진이 고개를 숙였다.

“소저, 아니 지부장님. 사죄드리겠…….”

“그럼 입 다물고 있어요.”

“옙.”

월화가 실소를 흘렸다.

“재밌는 수하를 뒀네요.”

어물전 망신은 꼴뚜기가 시킨다더니, 태원진가 망신은 혁무진 저 자식이 다 시키는구나. 쪽팔려서 얼굴도 제대로 못 쳐다보겠다.

“……제가 다 죄송하네요.”

“공자가 사과할 건 아니죠. 뭐, 아주 틀린 말도 아니고.”

시원시원하게 넘어가 주니 다행이다.

담배 연기를 내뿜은 월화가 입을 열었다.

“항산검문에 가는 길이죠?”

“네.”

“목적이 뭔지 물어봐도 될까요?”

“이미 알고 있지 않습니까?”

산서성 제일의 정보통이 바로 그녀다. 어떻게 알았는지 물어볼 필요조차 없었다.

“나는 진 공자가 직접 말해 주길 바랐는데…… 섭섭하네요.”

“공과 사는 뚜렷해야죠.”

“야박하긴. 그럼 제의 하나만 해도 될까요? 거래라고 해도 좋고.”

“들어 보고 결정하겠습니다.”

월화가 곰방대를 툭툭 털었다.

“같이 가요. 항산검문.”

“네?”

이게 뭔 소리야.
```

## Current accepted English baseline

```markdown
# Chapter 105

Crack!

The instant my fist sank into that foul-smelling snout, I knew.

The only thing that bastard would be able to eat from now on was chicken-and-corn soup.

Crash! Bang!

The first man shot backward in a straight line and lost consciousness before his body even hit the ground.

Level 31. He was a martial artist at the entry level of First Rate, but he still couldn’t dodge my punch.

“Where the hell do you get off stinking up the place with your breath and ruining my appetite?”

Every sound in the inn stopped.

But only for a moment.

“Gwangsu’s down!”

“You little brat!”

“Kill him!”

Shing, shing, shing!

Five curved sabers were drawn at once. Five pairs of eyes gleamed with killing intent. The inn’s guests scattered with screams.

I suddenly remembered the smell of blood coming from the man who had just fallen.

*Huh. Look at these bastards.*

They were used to killing. I could tell just from the fact that they had started the fight and still hadn’t hesitated to draw their weapons.

“What kind of people are you?”

“The Grim Reaper.”

The answer came at the same time as their attack.

Four curved sabers stabbed straight at my limbs, while the remaining one aimed precisely for my chest.

Whoosh, whoosh, whoosh!

Too slow.

One of the five was First Rate. The other four were Second Rate.

Their confidence in taking me down was impressive, but their feet were slow, and the net of sabers they spread from the front was full of gaps.

“Next time, at least try surrounding someone.”

Along with that friendly advice, I flicked both hands toward them.

For a very brief moment, two daggers summoned from my Inventory cut through the air.

Whoosh!

*Throwing daggers. Is that what they call it in Murim—flying-dagger arts?*

I had never learned it for actual combat, but it didn’t matter. Whether they were hit by the blade or the hilt, a hit was a hit.

Crack! Thud.

Yes, just like that.

One man’s forehead split open against the hilt of a dagger, and he crumpled without even managing to scream.

What about the other one?

Clang!

“What a cheap trick!”

Whether he was lucky or had better eyes than I expected, he had somehow blocked it.

I gave him a wide smile.

“Is that dagger yours?”

“You threw it at me, so what kind of bullshit are you talking about?”

“What an honest child. As a reward, I’ll give you both of them.”

Thud, thud!

“Ghk. But your hands were clearly empty—”

Thud.

“My daggers multiply infinitely.”

It had been a good idea to stop by the armory before leaving the Jin Family of Taiyuan.

I had gone in empty-handed and come out empty-handed, but my Inventory was now filled with dozens of weapons looted as spoils.

“What… what is this?”

It had all happened in the blink of an eye. The remaining three stopped in the middle of their charge, hesitated, and backed away.

“Not coming? Then I’ll go to you.”

“W-Wait, Young Hero! We were rude. We sincerely apologize and will compensate you—”

Look at how quickly they changed tactics.

Just a moment ago, they had been calling me a brat. Now they were calling me Young Hero.

“An apology?”

“Yes, yes!”

“Don’t need it!”

I clenched my fist and charged at them. I didn’t need martial arts to deal with trash like this.

“Damn it, attack!”

Whoosh!

One step to the side.

I dodged the curved saber that came crashing straight down toward the top of my head, then drove a single punch into the exposed side of his body.

Crunch.

Leaving the man who collapsed with a strangled groan behind me, I charged at the next opponent.

Above his head, I saw a System window displaying Level 35.

“You bastard!”

Whoosh!

As befitted a First Rate expert, he had clearly learned a fair amount of martial arts. His movements were clean, and the curved saber was swung with precision toward my vital points.

But…

*All of that is useless before overwhelming strength and speed.*

My level and internal energy were low, but in terms of stats, I far surpassed First Rate. On top of that, I had all the combat experience I had built up in Murim.

This man could never be my opponent.

Crack!

The focus vanished from his eyes. The curved saber slipped from his grip before he could finish his swing.

Clang.

The last man, who had watched everything unfold, was half out of his mind.

“T-The squad leader fell in a single exchange… Who are you?”

“You should exchange names with my fist. Here, this one’s called Right Hand. And you?”

I approached with my right fist clenched. The man swung his curved saber wildly through the air.

“D-Don’t come any closer!”

“You should make a request more politely.”

“Please, don’t come any closer!”

“You really did it.”

Since he had asked so politely, I supposed I had to honor his request.

When I stopped walking, color returned to the man’s face.

“T-Thank you! I’ll live a good life from now on!”

“No need to thank me. And you don’t have to live a good life.”

“Huh?”

“Turning over a new leaf isn’t something that happens so easily. Isn’t that right, Mujin?”

Hyuk Mujin was standing behind the man before I knew it.

“Of course.”

“Hic!”

The man sucked in a startled breath and turned around, but it was already too late.

Hyuk Mujin was in the middle of bringing the wooden chair in his hands down on the top of the man’s head with all his strength.

Crack!

With a heavy thud, the last man collapsed. Hyuk Mujin set the chair down and muttered,

“Thank you, and I’m sorry.”

“What are you thanking those bastards for?”

“There are things.”

That look in his eyes was awfully cocky.

I was wondering whether I should give him a smack after such a long time when Hyuk Mujin, who had been searching through the fallen men’s clothes, tilted his head.

“Huh? Squad Leader, these men are suspicious.”

“What about them?”

“Look at this.”

Hyuk Mujin rolled up one man’s sleeve, revealing a scar that looked as though it had been branded into the flesh.

No, it wasn’t simply a scar.

It looked like…

“A tattoo?”

It was crude and savage, but it was definitely a kind of tattoo.

A running horse.

“Is this the only one with it?”

“I don’t know. I haven’t checked all of them yet.”

“Check the others.”

“Yes, sir.”

Hyuk Mujin gathered the unconscious men in one place and stripped off their shirts.

Their arms, chests, and necks. The locations differed slightly, but every one of them had a tattoo of a horse.

*So they belong to some kind of organization…*

I already knew they weren’t simple thugs. Two of them were First Rate masters, and I couldn’t stop thinking about the word the last man had let slip without meaning to.

*He definitely said captain, didn’t he?*

Martial artists belonging to another sect?

No. Their aura was too rough for that, and their clothing wasn’t uniform.

It was more likely that they belonged to a fairly large group of wandering martial artists.

*A horse tattoo. A horse tattoo…*

Then a word suddenly flashed through my mind.

It was a name I had first heard during the war with the Mount Heng Sword Sect.

“Mounted bandits?”

Someone answered my mutter from somewhere nearby.

“There are dozens of mounted-bandit groups on the northern plateau. It was a great mistake for Lee Cheonbaek to hire them.”

I turned toward the owner of the languid yet alluring voice.

A woman stood on the stairs leading to the second floor, a veil draped across her face.

“Long time no see, our Young Master.”

*Our Young Master?*

The moment I heard those words, I knew who she was.

*Wolhwa.*

It was her.

* * *

Hyuk Mujin and I were led to a guest room on the top floor of the Phoenix Inn.

Calling it a guest room didn’t really do it justice. We had the entire floor to ourselves, so it was more accurate to call it a penthouse.

“It’s my first time bringing a man here. And two of them, no less.”

Wolhwa’s smile, bathed in the soft light, was dazzling.

I had felt it from the moment we first met, but there really was no better example of a femme fatale.

Even though I had met her several times already, my stomach still churned whenever I looked at her.

Hyuk Mujin was beyond saving.

“It’s an honor beyond three lifetimes.”

“……”

Look at that bastard’s unfocused eyes.

He was completely smitten.

Wolhwa gave him a bright smile before turning her gaze toward me.

“Have you been well, Young Master Jin? Ah, I suppose I can’t call you Young Master the way I used to anymore?”

Judging from Wolhwa’s mischievous expression, I could easily guess what she was about to say.

I hurriedly waved my hands.

“Just call me whatever you like. Like before.”

“Hmm. Then how about Young Master Sleeping Dragon?”

“……That’s horrible.”

“Why? Sleeping Dragon of Shanxi sounds wonderful. If you’ve earned that much martial fame at such a young age, you could stand to be a little prouder.”

Sleeping Dragon of Shanxi or Flaming Charisma Taekyung—they were equally terrible.

Seeing my expression, Wolhwa chuckled and put her long-stemmed tobacco pipe to her lips.

“I’m only joking. Anyway, teasing Young Master Jin is so much fun.”

“Excuse me for interrupting.”

Hyuk Mujin had finally regained some of his senses. He looked back and forth between Wolhwa and me.

“May I ask what kind of relationship the two of you have?”

“None of your business.”

It was too embarrassing to explain our relationship in detail.

I cut him off sharply, then glanced at Wolhwa. It was a signal asking her to play along.

She immediately understood and nodded.

“He used to be a regular at my establishment. Not anymore, though.”

“……”

Like hell she did.

Still, it was a little ridiculous for her to hide it now. She had been completely open about it in front of Jin Wikyung and Wipeng.

Hyuk Mujin, meanwhile, seemed only half-convinced by Wolhwa’s answer.

“By ‘establishment,’ do you mean the Phoenix Inn?”

“No. This is just a side business. My real profession is something only a beautiful and charming woman like me can do.”

“Then perhaps…”

“It’s probably what you’re thinking, Young Martial Artist.”

“A pleasure house?”

“Correct.”

Hyuk Mujin’s eyes widened.

“So the proprietress of the Phoenix Inn, whom I had only heard about in rumors, was a courtesan.”

“Young Martial Artist, you should watch your words. It’s unpleasant to hear that from the other side.”

“If I offended you, I apologize. However, your words and behavior don’t exactly appear in a favorable light either.”

The sudden change in his expression caught me even more off guard.

“Hey, what’s with you?”

“Squad Leader—no, Young Master—is a direct descendant of the Jin Family of Taiyuan. Even the most beautiful woman under heaven cannot treat the Young Master so casually. As a retainer of our family, I could not stand by and let it happen.”

“A moment ago, you said it was an honor beyond three lifetimes.”

“……In any case, how could a mere courtesan treat Young Master—”

Smack!

I gave him a satisfying whack on the back of the head and opened my mouth.

“She’s the Shanxi Branch Leader of the Lower District Sect.”

“Whether she’s the Shanxi Branch Leader or not, huh? What?”

“Are your ears clogged? I said she’s the Shanxi Branch Leader of the Lower District Sect. She gave us extremely—very, very—decisive help in the recent war with the Mount Heng Sword Sect.”

“I’m fine, Young Master Jin.”

Wolhwa lowered her eyes sadly.

“I’m only a mere courtesan, after all.”

Hyuk Mujin was silent for a moment before bowing his head.

“Young Lady—no, Branch Leader. I apologize—”

“Then keep your mouth shut.”

“Yes, ma’am.”

Wolhwa let out a quiet laugh.

“You have an interesting subordinate.”

They say the squid is what disgraces the fish market. In the same way, that bastard Mujin was doing all the disgracing for the Jin Family of Taiyuan.

I was too embarrassed to look Wolhwa in the eye.

“……I apologize for all of this.”

“You’re not the one who needs to apologize, Young Master. And he wasn’t entirely wrong.”

Thankfully, she let it slide without a fuss.

After exhaling a stream of smoke, Wolhwa spoke.

“You’re on your way to the Mount Heng Sword Sect, aren’t you?”

“Yes.”

“May I ask what your purpose is?”

“You already know, don’t you?”

She was the greatest source of information in all of Shanxi. There was no need to ask how she knew.

“I wanted Young Master Jin to tell me himself, though. I’m disappointed.”

“Business and personal matters should be kept separate.”

“How cold. Then may I make you a proposal? You can call it a deal, if you prefer.”

“I’ll decide after I hear it.”

Wolhwa tapped the ash from her pipe.

“Let’s go together. To the Mount Heng Sword Sect.”

“What?”

What the hell was she talking about?
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 105`.

# Master Edit Task — Chapter 106

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
| 혁무진    | **Hyuk Mujin**     |
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 지부장    | **Branch Leader**                            |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 청해     | **Qinghai**            |
| 항산     | **Mount Heng**         |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 은자 | **silver nyang** | Silver currency unit. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 하오문도 | 진위경 | informant_to_lesser_family_head | Lesser Family Head | deferential | Uses 소가주님 while correcting Wikyung's misunderstanding about Mukyung's condition. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |

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

#### Chapter 104 tail (verified mastered)

…
hadn’t laughed at me…* Regret always comes too late. Hyuk Mujin hurriedly began working the abacus in his head. *The expense money is gone. But I brought some emergency savings just in case, so maybe I can somehow manage.* Five silver nyang. Every coin he had saved until now. He had brought it in case of an emergency, never expecting to actually spend it. *If I don’t indulge too much, I should be able to hold out until we return.* But there was one thing Hyuk Mujin had failed to consider. Jin Taekyung’s appetite. Slurp. Gulp. Munch, munch. “Wow, this really melts in your mouth.” “……” Beggar’s Chicken, Fish-Fragrant Shredded Pork, Maechae Guyuk,[^1] scallion tofu, Kung Pao chicken… Every time one of those dishes—or any of the dozen others—arrived at the table, Jin Taekyung’s hand moved like lightning. “Wow, this is really good. So juicy.” “……” “You’re not eating? Then I’ll finish the rest too.” “……” “Wow, this broth is incredible.” “…Please, eat as much as you like.” At some point, a single tear rolled down Hyuk Mujin’s cheek. *The dishes served so far already cost five silver nyang.* His last hope was gone. Judging by the way things were going, that pig looked ready to devour another twenty plates. Hyuk Mujin wanted to smash a plate over the pig-like bastard’s head, but he restrained himself. He didn’t want to lose his life on top of his entire fortune. *Jade Emperor, Primordial Heavenly Venerable. Please, stop that bastard.* Just as he cursed the heavens— Crash! * * * The hardest parts of life in Murim were, first, survival and, second, the food. For some reason, everything was spicy, salty, and greasy, leaving me craving soup at every meal. In that sense, the dish just placed on the table held special significance. *Chicken-and-corn soup.* It was a kind of corn soup with egg whisked through it until silky smooth. I lowered my head slightly and smelled it. The distinctive savory scent of corn lingered at the tip of my nose. *Yes, this is it.* A smile rose naturally to my face. My stomach had already started feeling greasy. Once I settled it with the chicken-and-corn soup, I could probably clear another ten plates. *All right, then, now…* Just as I grasped the hot ceramic bowl with pleasant anticipation— Crash! Clatter, clatter! “…Huh?” It happened in an instant. A liquor bottle shattered in the middle of the table, exploding into hundreds of ceramic shards that flew in every direction. Along with them came the little liquor left inside. Pitter-patter. Drenched by the sudden shower, I was left speechless. *How could this happen?* The chicken-and-corn soup I had been eagerly awaiting—the warm, savory broth that would gently soothe my stomach—was no longer there. What now filled the ceramic bowl was nothing more than food waste mixed with liquor and pieces of pottery. Across from me, Hyuk Mujin stared with his mouth hanging open. “Oh, Jade Emperor. Primordial Heavenly Venerable.” Ignoring his nonsense, I slowly turned toward the direction the bottle had come from. Five men were looking our way and snickering. “Oh, Brother. Sorry about that.” “Who can you blame when your hand slips? We can just order him another one.” “Hey, don’t say anything crazy. Didn’t you see how much that bastard’s been eating?” I watched them snicker among themselves, then crooked a finger. The one who had apologized first. That bastard was the culprit who had ruined my chicken-and-corn thoup. “What, you want me to come over?” He gave a short laugh, rose from his seat, and strode toward us. His martial robes reeked of sweat and blood, and a curved saber hung from his left hip. That was the source of his confidence. *All right. Let’s handle this rationally.* I spoke calmly. “The ancient sages said that even a dog shouldn’t be disturbed while it’s eating. Apologize properly and order the food again. Starting with the chicken-and-corn thoup.” “Well, listen to the little brat lisp.” “What about the apology?” “Come on, kid. Stick out your tongue. I’ll pull it out for you.” He grinned, revealing teeth rotted black. The horrific stench of his breath wiped away my appetite as if it had been washed clean. I supposed I would have to eat the thoup later. “Open your mouth. My fist is going in.” As the words left my mouth, I drove my fist into his face. Crack! * * * There were three reasons the Phoenix Inn was famous. But the third was why so many people—men in particular—flocked there. The beautiful proprietress, whom one could only meet on a lucky day. And today was that day. “It’s noisy.” The proprietress’s clear yet languid voice was not directed at herself. The presence outside her door vanishing proved it. A moment later, a quiet voice came from beyond the door. “A fight has broken out between martial artists.” The proprietress clicked her tongue softly before speaking. “Did anyone die?” “One man subdued the other six.” “Who is he? Where is he from?” “He’s the Sleeping Dragon of Shanxi.” The proprietress laughed soundlessly. “What a welcome name. I should go see his face after all this time.” She rose from where she had been reclining. Moonlight filtering through the window gleamed upon her slender, long-stemmed tobacco pipe. [^1]: *Maechae Guyuk* is an abbreviated name for pork belly steamed with preserved mustard greens.

#### Chapter 105 tail (verified mastered)

…
woman stood on the stairs leading to the second floor, a veil draped across her face. “Long time no see, our Young Master.” *Our Young Master?* The moment I heard those words, I knew who she was. *Wolhwa.* It was her. * * * Hyuk Mujin and I were led to a guest room on the top floor of the Phoenix Inn. Calling it a guest room hardly did it justice. It occupied the entire floor, so penthouse would have been more accurate. “It’s my first time bringing a man here. And two of them, no less.” Bathed in the soft light, Wolhwa’s smile was dazzling. I had felt it from the moment we first met, but she was the very definition of a femme fatale. Even after meeting her several times, the sight of her was enough to make my stomach churn. Hyuk Mujin was beyond saving. “I-It is the honor of three lifetimes.” “……” Look at that bastard’s glazed eyes. He was completely smitten. Wolhwa gave him a smile, then turned her gaze toward me. “Have you been well, Young Master Jin? Ah, perhaps I can’t call you Young Master the way I used to anymore?” The mischief in her expression made it obvious what was coming. I hurriedly waved my hands. “Just call me whatever you like. Like before.” “Hmm. Then how about Young Master Sleeping Dragon?” “……That’s horrible.” “Oh my, why? Sleeping Dragon of Shanxi sounds wonderful. If you’ve earned that much martial fame at such a young age, you could stand to be a little prouder.” Sleeping Dragon of Shanxi, Flaming Charisma Taekyung—six of one, half a dozen of the other. Seeing my expression, Wolhwa chuckled and put her long-stemmed tobacco pipe to her lips. “I’m only joking. Anyway, teasing Young Master Jin is so much fun.” “Excuse me for interrupting.” Hyuk Mujin had regained some of his senses. He looked back and forth between Wolhwa and me. “May I ask what kind of relationship the two of you have?” “None of your business.” Our relationship was too embarrassing to explain in detail. I cut him off sharply and glanced at Wolhwa, signaling for her to play along. Quick on the uptake, she nodded. “He used to be a regular at my establishment. Not anymore, though.” “……” Like hell she understood. Then again, after how openly she had acted in front of Jin Wikyung and Wipeng, it would have been ridiculous for her to hide it now. Hyuk Mujin, meanwhile, seemed only half-convinced by Wolhwa’s answer. “By ‘establishment,’ do you mean the Phoenix Inn?” “No. This is just a side business. My real profession is something only a beautiful and charming woman like me can do.” “Then perhaps…” “It’s probably exactly what you’re imagining, Young Martial Artist.” “A pleasure house?” “Correct.” Hyuk Mujin’s eyes widened. “So the proprietress of the Phoenix Inn, whom I had only heard about in rumors, was a courtesan.” “Young Martial Artist, you should watch your words. That isn’t very pleasant to hear.” “If I offended you, I apologize. However, your words and behavior don’t exactly appear in a favorable light either.” His sudden seriousness caught me even more off guard. “Hey, what’s with you?” “Captain—no, Young Master—is a direct descendant of the Jin Family of Taiyuan. Even the most beautiful woman under heaven has no right to treat him so casually. As a retainer of our family, I could not simply stand by and watch.” “A moment ago, you said this was the honor of three lifetimes.” “……In any case, how dare a mere courtesan treat the Young Master—agh!” Smack! I gave him a satisfying whack on the back of the head. “She’s the Shanxi Branch Leader of the Lower District Sect.” “Shanxi Branch Leader or not—what? What did you say?” “Are your ears clogged? I said she’s the Shanxi Branch Leader of the Lower District Sect. She gave us extremely—very, very—decisive help in the recent war with the Mount Heng Sword Sect.” “I’m fine, Young Master Jin.” Wolhwa lowered her eyes sadly. “I’m only a mere courtesan, after all.” Hyuk Mujin fell silent for a moment, then bowed his head. “Young Lady—no, Branch Leader. I apologize…” “Then keep your mouth shut.” “Yes, ma’am.” Wolhwa let out a quiet laugh. “You have an interesting subordinate.” As the saying went, it was the squid that disgraced the fish market. That bastard Hyuk Mujin was disgracing the entire Jin Family of Taiyuan all by himself. I was too embarrassed to even look Wolhwa in the eye. “……I apologize for all of this.” “You’re not the one who needs to apologize, Young Master. And he wasn’t entirely wrong.” Thankfully, she let it slide without a fuss. After exhaling a stream of smoke, Wolhwa spoke. “You’re on your way to the Mount Heng Sword Sect, aren’t you?” “Yes.” “May I ask what your purpose is?” “You already know, don’t you?” She was the greatest source of information in all of Shanxi Province. There was no need to ask how she knew. “I wanted Young Master Jin to tell me himself… I’m disappointed.” “Business and personal matters should be kept separate.” “How cold. Then may I make a proposal? Or a deal, if you prefer.” “I’ll decide after I hear it.” Wolhwa tapped the ash from her pipe. “Let’s go together. To the Mount Heng Sword Sect.” “What?” What the hell was she talking about?

## Korean source

```text
＃106화



“같이 가요. 항산검문.”

“네?”

“진 공자가 들은 그대로예요. 나도 항산검문에 볼일이 있거든.”

“무슨 일로요?”

“그건 말 못 할 것 같은데? 나도 공과 사가 뚜렷한 편이라서.”

되로 주고 말로 받았군.

방금 내 입으로 한 말이 고스란히 돌아온다. 머쓱해하는 나를 보는 월화의 미소가 짙어졌다.

“장난이에요. 마침 항산검문 쪽에 받을 게 있거든요. 정확히는 태원진가에서 받기로 한 거지만.”

“무슨…… 아.”

문득 떠오르는 기억이 있다. 항산검문과의 전쟁이 한창 진행되고 있을 무렵, 태원진가와 하오문이 맺었던 밀약.

‘정보를 제공하는 대신 항산검문이 소유한 부지 등에 대한 소유권을 받기로 약속했던가?’

하오문은, 아니 월화는 약속을 지켰다. 개전 초기 항산검문의 선봉대를 궤멸시킬 수 있었던 것도 그녀의 도움이 있었기 때문이다.

태원진가는 그 후에도 하오문에게 여러 도움을 받았고 마침내 전쟁에서 승리했지만, 문제는 그 후였다.

“진 공자도 알다시피 우리 입장이 좀 묘하게 됐어요. 전쟁에선 이겼는데 전리품에 손을 못 대고 있는 상황이라.”

약육강식. 강자가 약자를 집어삼키는 건 무림의 법칙이다.

그러나 대장로의 등장이 모든 걸 망쳤다. 태원진가와 항산검문이 그의 농간에 놀아났다는 사실이 밝혀진 순간부터 전리품을 취할 명분이 희미해진 거다.

‘그래서 합병을 진행하는 거고.’

지금은 검을 거두고 붓으로 대화를 나눠야 할 때다. 세상 사람들이 욕하지 않는 범위 안에서 조용히, 원만하게 흡수하는 것이 진위경이 그리는 그림이다.

월화는 그 전에 보상을 받기를 원하는 거고.

“항산검문 측이 우리의 제안을 받아들인다면 그때 보상을 요구해도 될 텐데요.”

“그건 태원진가가 산서성의 맹주(盟主)가 아닌 패자(霸者)일 때나 가능한 이야기예요. 지금 상황에서 섣불리 뺏으려 하다가는 다른 중소 문파들도 발을 빼겠죠. 더군다나…….”

순간 나를 의미심장한 눈빛으로 바라본 그녀가 고개를 저었다.

도대체 뭐지?

“더군다나, 뭐요?”

“아니에요. 뭐, 아무튼 소가주님께도 제안을 받긴 했어요.”

월화가 곰방대를 뻐끔거리며 말을 이었다.

“약속했던 것에 상응하는 재물, 혹은 태원진가가 관리하는 구역을 양도해 주시겠다고 하더군요.”

그 정도면 괜찮은 거 아닌가 싶지만 개인이 아닌, 한 단체를 이끄는 수장의 입장에서 생각해 보면 다르다.

‘활동 영역을 확대하고 싶은 거겠지.’

월화의 본질은 기녀도, 객잔의 주인도 아닌 정보 상인.

이번 기회에 항산검문의 차단으로 비교적 약세였던 산서성 북부까지 하오문의 영향력을 넓히고 싶어 하는 게 분명했다.

‘진위경이야 당연히 태원진가가 산서성 전역을 아울렀으면 하는 마음일 거고.’

이미 오래전부터 산서성 중남부에 막대한 영향력을 행사해 왔던 태원진가다. 알짜배기 구역을 몇 개 넘겨준다고 해서 지금까지 쌓아 올린 영향력이 줄어들지는 않는다.

‘이거 딱 그거네. 재개발 구역.’

북부를 꽉 잡고 외부 세력의 유입을 막던 항산검문이 무너지고 있다. 그린벨트가 해제되고 재개발 구역이 되니 진위경과 월화 간의 밀고 당기기가 시작된 거다.

‘둘 다 장난 아니네.’

어제의 동맹이 오늘의 경쟁자가 됐다.

사람은 보이는 게 전부가 아니라는 사실을 오늘 다시 한번 느낀다.

“그래서 우리 귀여운 신임 문주님도 뵙고, 빚 독촉도 할 겸 항산검문까지 동행하려고 하는데…… 어때요?”

더 생각할 것도 없이 대답했다.

“거절하겠습니다.”

“와, 너무 단호한 거 아니에요? 거래 조건도 듣기 전에 칼같이 잘라 버리네.”

“아우가 돼서 형님 앞길에 똥물 뿌릴 순 없죠.”

피 한 방울 안 섞인 형제지만 이미 마음 한구석에서는 그의 존재를, 이 무림을 받아들인 지 오래다.

“흐음.”

나를 지그시 바라보던 월화가 곰방대를 탁 내려놨다.

“그렇게 해요, 그럼.”

“아, 예.”

몇 번 더 꼬드길 줄 알았는데 바로 포기하네.

뭐, 나로서는 이야기가 빨리 끝나서 마음 편하다.

“그럼 이만.”

아직도 입을 봉인한 채 앉아 있는 혁무진을 툭 치며 자리에서 일어났다. 그때 월화가 묘한 웃음을 짓곤 말했다.

“아, 진 소협한테 전해 줄래요? 후원에 있는 노송(老松), 그거 비싼 거니까 수련 좀 조심히 해 달라고.”

산서성 제일의 정보 상인이 운영하는 객잔이다. 이곳에 들어온 후부터 내부 장기까지 훤히 읽히고 있는 거나 마찬가지겠지.

“그러죠.”

“필요한 거 있으면 말씀하시고. 우리 진 공자님 부탁인데 뭐든 다 구해 드려야지.”

눈을 찡긋거리는 그녀를 일별하고 방을 나오자마자 잠시 잊고 있던 일이 생각났다.

“무진아, 넌 왜 그렇게 주둥이를 함부로 놀리니?”

빡! 빡! 빡!

“악, 악, 악!”

한 명은 때리고, 한 명은 맞고.

그렇게 돌아온 별채에서는 반듯하게 잘려 나간 노송 몇 그루와 흡족한 얼굴의 진무경이 기다리고 있었다.

“베는 맛이 있군.”

“…….”

“…….”

언젠가 저놈을 베어 버리고 싶다.



* * *



고요해진 객실. 한동안 곰방대만 피워 물던 월화가 입을 연 것은 진태경이 떠나고 한참 후였다.

“내가 일전에 지시한 거, 알아봤어?”

객실 밖에서 대기하고 있던 하오문도가 낮은 목소리로 대답했다.

“나흘 전에 확인하신 것이 전부입니다. 추가 정보를 수집하고는 있습니다만…….”

“더 나올 게 없다?”

“예, 희박합니다.”

“희박? 그럼 가능성이 없진 않네? 계속 파. 시간 넉넉하게 줄 테니까 서두르지 말고. 지금 태원진가 건드렸다가는 우리도 좋은 꼴 못 보는 거 알지?”

“존명.”

물러가려는 하오문도를 붙잡은 건 이어지는 월화의 한마디였다.

“삼류 망나니가 불과 두 달도 안 돼서 산서잠룡이 됐어. 네 생각은 어때?”

“가능합니다. 소문대로라면.”

“아, 그거.”

월화가 피식 실소를 터트렸다. 진태경이 일문일살 조필을 쓰러트린 후부터 퍼지기 시작한 소문이다.

지금까지 진태경이 보인 모습은 모두 위장이었고, 사실은 그가 어린 시절부터 전폭적인 지원 아래 무공을 익혔다는 소문.

이제는 산서성 전역에 모르는 사람이 없을 정도로 퍼진 이야기다.

“그걸 믿니?”

“황당무계한 헛소문이죠. 하지만…….”

“사람들은 믿지. 멍청해서가 아니라, 믿을 수밖에 없으니까. 하지만 우리는 아니야.”

산서는 이미 중원에서 취급도 안 해 주는 변방이지만 하오문은 끊임없이 정보를 모아 왔다.

산서성의 유력가인 태원진가의 직계에 대해서는 말할 것도 없다. 유일한 실수라고는 혼란스러웠던 전란(戰亂)의 시기에 활동했던 대장로를 정확히 파악하지 못했다는 것뿐.

그러나 진태경에 관한 정보는 완벽에 가깝다.

“술, 여자, 도박. 어린 시절부터 나태했고 노는 것에만 정신이 팔려 있었지. 태원진가 역사에 저런 자가 있었나 싶을 정도로.”

“이 년 전, 지부장님께서 부임하시자마자 내린 첫 지시도 그것이었죠.”

“맞아. 산서 전체 동향 파악. 그리고 진태경 집중 조사.”

본디 재능은 대물림되는 법이다. 태원진가의 직계는 대대로 뛰어난 무재(武才)의 소유자들이었고 기인이라 평가받는 현 가주와 두 아들도 예외는 아니었다.

그 사이에서 진태경의 존재는 이질적일 만큼 눈에 띄었고, 그래서 하오문은 조사에 착수했다.

“결과는 허무했지.”

“정말 보이는 그대로 나왔습니다.”

가문의 핏줄 덕분인지 근골과 근맥이 약간 뛰어나다는 것 빼고는 특별할 것도 없었다.

“그때 뭔가 놓쳤던 걸까?”

“이틀에 한 번꼴로 기루에서 자고 가던 놈입니다. 잠을 줄여 가며 익혀도 부족한 것이 무공이지 않습니까?”

“알지, 잘 알지.”

월화는 일류 중에서도 제법 완숙한 경지까지 무공을 익힌 사람이다. 그에 대해 모를 리 없었다.

답답함에 연신 곰방대만 빨아들이던 그녀가 긴 숨을 토했다.

“결국 답은 하나뿐이네.”

“그렇습니다.”

진태경이 두 달 남짓한 시간 동안 삼류에서 초일류의 고수가 되었다는 것. 월화는 스스로 내린 결론에 기가 찼지만 어쩔 도리가 없었다.

“아까 내린 지시는 없던 걸로 해. 그에 대해서는 더 이상 묻지도, 알려고 하지도 마. 혹여나 입에 올리는 일 없도록 함구령 내리고.”

“존명. 단단히 일러두겠습니다.”

“아, 그리고 하나 더. 내일 일찍 떠날 테니까 준비해 둬.”

“누구를 데려가실 생각인지.”

“나 혼자.”

“지부장님, 그건…….”

“명령이야.”

“……존명.”

수하가 물러나자 객실에는 적막이 내리깔렸다. 월화는 까맣게 타 버린 담뱃잎을 털며 생각했다.

‘진태경이라.’

지금까지의 행보가 모두 사실이라면, 항산검문에게서 얻어 내야 할 북부 이권 따위는 아무것도 아니다.

‘고금을 통틀어 이 정도로 빠르게 성장한 이가 있었을까?’

진태경이 앉아 있던 자리를 바라보는 그녀의 눈빛이 깊게 가라앉았다.



* * *



다음 날 아침.

문제가 터졌다고 느낀 건 별채를 담당하는 책임자를 만난 후부터였다.

“숙박비 스물다섯 냥, 음식값 다섯 냥, 그리고 기물 파손비로 오십 냥. 총합 은자 여든 냥입니다.”

어제 마적 놈들을 주머니를 털었다며 희희낙락하던 혁무진이 입을 딱 벌렸다.

“기물 파손? 은자 오십 냥?”

“후원에 가 보니 노송 다섯 그루가 쓰러져 있더군요.”

월화가 비싸다고 했던 그 나무다.

나와 혁무진이 동시에 고개를 돌렸다. 시선이 마주친 진무경이 움찔하더니 입을 열었다.

“검을 펼치다 보니 흥에 취했다.”

“……아니, 시바. 흥에 취하면 걸리는 거 다 잘라도 되는 거야? 어?”

“후우우.”

혁무진은 뭐라 말은 못 하고 분노의 한숨만 푹푹 내쉬었다.

척 보아하니 내야 할 돈이 경비를 초과한 게 분명하다. 그래도 약간 정도라면 잘 말해서 협의점을 찾을 수도…….

“무진아, 지금 얼마 있냐?”

“사십 냥이요.”

협의점은 염병. 턱도 없네.

“혹시 외상 됩니까?”

별채 책임자의 입가에 맺혀 있던 상냥한 미소가 사라진 그 순간이었다.

“진 공자, 여기서 뭐 해요?”

이쪽을 향해 다가오는 하늘하늘한 궁장 차림의 미녀.

지금의 우리에게 있어 월화의 등장은 구명줄이나 다름없었다.

어젯밤 그녀의 제안을 단호하게 제안한 게 마음에 걸리지만, 이것저것 가릴 때가 아니다.

“아니, 그게요…….”

사정을 설명하자 월화가 눈을 동그랗게 떴다.

“여든 냥? 그럴 리가 없는데.”

“그렇죠? 좀 잘못된 것 같다니까요.”

“그거 이리 줘 봐.”

책임자가 들고 있던 죽간을 건네받아 읽기 시작하는 그녀.

점점 눈살을 찌푸리는 걸 보니 계산이 단단히 틀어진 것이 분명했다.

‘그럼 그렇지.’

이윽고 죽간을 모두 읽은 월화의 입술 사이로 싸늘한 목소리가 흘러나왔다.

“일 똑바로 안 해?”

“죄, 죄송합니다.”

“이분들이 어떤 분들이신데 감히 이따위 짓거리를…… 가격 똑바로 적어.”

혁무진이 작은 목소리로 소곤거렸다.

“천만다행이네요.”

“그러게. 접시 닦고 갈 뻔했네.”

“이공자님 때문에 뭔 고생입니까, 이게.”

“저 인간 얘기는 꺼내지도 마. 듣기만 해도 암 걸려.”

“암이 뭔데요?”

“……있어, 안 좋은 거.”

그사이 진땀을 흘려 가며 가격을 고친 책임자가 허리를 푹 숙이며 우리에게 사과했다.

“죄송합니다. 제가 생각이 짧아서 결례를 저질렀습니다.”

혁무진이 거만한 태도로 인사를 받았다.

“다음부턴 그러지 마쇼. 상대를 봐 가면서 장난을 쳐야지. 그래서 얼마요?”

“은자 백오 냥 하고도 철전 이십삼 냥입니다.”

“……?”

“……?”

뭐야, 이거. 꿈인가?

고개가 저절로 월화를 향해 돌아간다.

“무슨 소리예요, 저게?”

“내 지인이라고 멋대로 가격을 깎았더라고요. 감히 대태원진가의 자제분들을 뭘로 보고. 다시 한번 사과드려.”

“몰라뵈어서 죄송합니다!”

“그…….”

나는 잔뜩 목멘 목소리로 물었다.

“외상은 되죠? 당연히.”

“안 되죠. 당연히. 이 년 동안 단 한 번도 없었어요.”

“이번 기회에 선례를 남기는 건 어떨까요?”

“아직은 그럴 생각이 없어서. 다음 기회를 노려 봐야죠.”

월화가 화사한 웃음과 함께 덧붙였다.

“더 하실 말씀이라도?”

“……하, 항산.”

“뭐라고요?”

나는 눈을 질끈 감고 말을 이었다.

“항산검문까지 같이 가실래요?”

“와아, 저야 좋죠.”

저 가증스러운 웃음이라니. 월화의 손짓에 책임자가 죽간을 들고 빛의 속도로 사라진다.

“앞으로 여비 걱정은 없겠네요.”

혁무진처럼 현실을 받아들이는 사람이 있는 반면에, 결사반대를 외치는 사람도 있었다.

“헛소리! 가문의 임무를 수행하는 길에 어찌 여인을 데려간단 말이냐!”

“그럼 여기서 그릇 닦고 오든가.”

“…….”

“이 중에서 노송 자른 사람 손?”

진무경은 손을 들지 않았고, 월화는 그에게 치맛자락을 살짝 들어 올리며 인사했다.

“잘 부탁드려요. 진 소협.”
```

## Current accepted English baseline

```markdown
# Chapter 106

“Let’s go together. To the Mount Heng Sword Sect.”

“What?”

“You heard me, Young Master Jin. I have business at the Mount Heng Sword Sect too.”

“What kind of business?”

“I don’t think I can tell you that. I’m rather clear about keeping business and personal matters separate.”

*Talk about getting paid back tenfold.*

What I had just said had come back to bite me. Wolhwa’s smile deepened as she watched me grow awkward.

“I’m only joking. I happen to have something to collect from the Mount Heng Sword Sect. More precisely, something I’m supposed to receive from the Jin Family of Taiyuan.”

“What… Oh.”

A memory suddenly came to me. Back when the war with the Mount Heng Sword Sect was in full swing, the Jin Family of Taiyuan and the Lower District Sect had made a secret pact.

*Hadn’t we promised to give them ownership of the Mount Heng Sword Sect’s properties and such in exchange for information?*

The Lower District Sect—or rather, Wolhwa—had kept her promise. It was thanks to her help that we had been able to annihilate the Mount Heng Sword Sect’s vanguard in the early days of the war.

The Jin Family of Taiyuan had continued receiving help from the Lower District Sect afterward and had eventually won the war, but that was when the trouble began.

“As you know, Young Master Jin, our position has become rather awkward. We won the war, but we can’t lay our hands on the spoils.”

The strong devouring the weak. That was the law of Murim.

But the appearance of the Head Elder had ruined everything. The moment it came to light that the Jin Family of Taiyuan and the Mount Heng Sword Sect had both been manipulated by him, the justification for claiming the spoils had grown faint.

*So that’s why we’re pursuing a merger.*

Now was the time to put away our swords and negotiate with a brush. Jin Wikyung’s vision was to quietly and amicably absorb the Mount Heng Sword Sect within limits that would keep the world from condemning us.

Wolhwa wanted to receive her reward before that happened.

“If the Mount Heng Sword Sect accepts our proposal, couldn’t you demand your reward then?”

“That would only be possible if the Jin Family of Taiyuan were Shanxi’s hegemon rather than its Alliance Leader. If we tried to snatch things away carelessly in the current situation, the other mid-sized and small sects would withdraw too. And on top of that…”

For a moment, she looked at me with meaningful eyes before shaking her head.

*What was that supposed to mean?*

“And on top of that, what?”

“No, it’s nothing. Anyway, I did receive a proposal from the Lesser Family Head.”

Wolhwa took a puff from her long-stemmed tobacco pipe before continuing.

“He said he would transfer wealth equivalent to what he had promised, or hand over some of the areas managed by the Jin Family of Taiyuan.”

That sounded like a reasonable offer, but it looked different when viewed from the perspective of someone leading an organization rather than acting as an individual.

*She wants to expand her territory.*

Wolhwa’s true nature was neither that of a courtesan nor an innkeeper. She was an information merchant.

There was no doubt that she wanted to use this opportunity to expand the Lower District Sect’s influence into northern Shanxi, where it had been relatively weak because of the Mount Heng Sword Sect’s blockade.

*Jin Wikyung, naturally, wants the Jin Family of Taiyuan to encompass all of Shanxi.*

The Jin Family of Taiyuan had already wielded enormous influence over central and southern Shanxi for a long time. Handing over a few prime areas wouldn’t diminish the influence they had built up until now.

*This is exactly like a redevelopment district.*

The Mount Heng Sword Sect, which had held a firm grip on the north and blocked outside forces from entering, was collapsing. The greenbelt had been lifted and the area had become open for redevelopment, so the tug-of-war between Jin Wikyung and Wolhwa had begun.

*They’re both something else.*

Yesterday’s ally had become today’s competitor.

Once again, I felt that people were never everything they appeared to be.

“So I thought I’d meet our adorable new Sect Leader and collect what I’m owed while I was at it. How about we travel to the Mount Heng Sword Sect together?”

I answered without needing to think any further.

“I’ll have to decline.”

“Wow, aren’t you being a little too decisive? You cut me off without even hearing the terms.”

“As his younger brother, I can’t go around splashing filth on my hyung’s path.”

We weren’t related by blood, but I had long since accepted his existence—and this Murim—as my own.

“Hmm.”

Wolhwa stared at me for a moment before setting her pipe down with a sharp tap.

“All right, then.”

“Ah. Yes.”

I had expected her to tempt me a few more times, but she gave up right away.

Well, at least the conversation had ended quickly. That made things easier for me.

“Then we’ll be going.”

I gave Hyuk Mujin, who was still sitting there with his mouth sealed shut, a light tap and rose from my seat. That was when Wolhwa smiled strangely and spoke.

“Oh, could you tell Young Hero Jin something for me? The old pine in the rear courtyard is expensive, so please be careful with your training.”

This was an inn run by the greatest information merchant in Shanxi. Ever since we entered this place, she had probably seen right through us, down to our innards.

“Sure.”

“And tell me if you need anything. It’s a request from our Young Master Jin, so I have to procure anything you might need.”

She gave me a wink. I merely glanced at her and left the room, only to remember something I had momentarily forgotten.

“Mujin, why do you run your mouth so carelessly?”

Whack! Whack! Whack!

“Argh! Argh! Argh!”

One of us hit, and the other took the hits.

When we returned to the private residence, we found several old pine trees neatly cut down and Jin Mukyung waiting with a satisfied expression.

“There’s a certain satisfaction to cutting.”

“……”

“……”

*One day, I really want to cut that bastard down.*

* * *

The guest room had grown quiet. Wolhwa smoked her long-stemmed tobacco pipe for a long while before finally speaking, long after Jin Taekyung had left.

“Did you look into what I instructed you to investigate?”

A member of the Lower District Sect, who had been waiting outside the guest room, answered in a low voice.

“What you confirmed four days ago is all we have. We’re still gathering additional information, but…”

“Nothing else is going to turn up?”

“It’s unlikely.”

“Unlikely? Then there’s still a chance. Keep digging. I’ll give you plenty of time, so don’t rush. You know that if we provoke the Jin Family of Taiyuan right now, we won’t fare well either.”

“Yes, Branch Leader.”

The Lower District Sect member was about to withdraw when Wolhwa stopped him with one more question.

“A Third Rate wastrel became the Sleeping Dragon of Shanxi in less than two months. What do you think?”

“It’s possible, if the rumors are true.”

“Ah, that.”

Wolhwa let out a short laugh. It was a rumor that had begun spreading after Jin Taekyung defeated Jopil, One Question, One Kill.

According to the rumor, everything Jin Taekyung had shown until now had been an act. In truth, he had learned martial arts since childhood under the full support of the family.

By now, the story had spread throughout Shanxi to the point that there was hardly anyone who hadn’t heard it.

“Do you believe it?”

“It’s ridiculous nonsense. But…”

“People believe it. Not because they’re stupid, but because they have no choice but to believe it. But we’re different.”

Shanxi was already a frontier region that the Central Plains hardly even acknowledged, but the Lower District Sect had continued gathering information there without pause.

When it came to the direct descendants of the Jin Family of Taiyuan, one of Shanxi’s most powerful families, there was no need to mention it. Their only mistake had been failing to accurately assess the Head Elder, who had been active during the chaotic period of war.

But their information on Jin Taekyung was nearly perfect.

“Alcohol, women, gambling. He had been lazy since childhood and obsessed with nothing but having fun. He was so out of place that you would have wondered whether someone like him had ever existed in the history of the Jin Family of Taiyuan.”

“That was the first order you gave after taking office as Branch Leader two years ago.”

“That’s right. Monitor the entire situation in Shanxi. And investigate Jin Taekyung in depth.”

Talent was normally passed down through the generations. The direct descendants of the Jin Family of Taiyuan had possessed exceptional martial talent for generations, and the current Family Head and his two sons, all regarded as eccentrics, were no exception.

Jin Taekyung’s existence stood out so sharply among them that he seemed almost alien. That was why the Lower District Sect had begun its investigation.

“The result was anticlimactic.”

“He was exactly what he appeared to be.”

Other than having slightly superior bones and meridians, perhaps thanks to his family bloodline, there had been nothing special about him.

“Did we miss something back then?”

“He was the kind of bastard who spent the night at a pleasure house every other day. Martial arts already demands more time than a person has, even if they cut back on sleep.”

“I know. I know very well.”

Wolhwa had cultivated her martial arts to a fairly mature stage of the First Rate realm. There was no way she didn’t understand that.

She continued drawing on her pipe, exhaling long breaths in frustration before finally letting out a deep sigh.

“In the end, there’s only one answer.”

“That’s right.”

Jin Taekyung had gone from Third Rate to a master beyond First Rate in a little over two months. Wolhwa was dumbfounded by the conclusion she had reached herself, but there was nothing she could do about it.

“Cancel the order I gave earlier. Don’t ask about him anymore, and don’t try to find out anything else. Issue a gag order so that no one even mentions him.”

“Yes, Branch Leader. I’ll make sure they understand.”

“Oh, and one more thing. I’ll be leaving early tomorrow, so prepare everything.”

“Who are you planning to take with you?”

“No one. I’ll go alone.”

“Branch Leader, that…”

“It’s an order.”

“Understood.”

Once her subordinate withdrew, silence settled over the guest room. Wolhwa shook the completely burned tobacco leaves from her pipe and thought.

*Jin Taekyung.*

If everything he had done until now was true, then the northern interests she was supposed to extract from the Mount Heng Sword Sect were nothing.

*Has anyone in all history ever grown this quickly?*

Her gaze, fixed on the place where Jin Taekyung had been sitting, sank into deep contemplation.

* * *

The next morning.

I began to feel that something had gone wrong after meeting the person in charge of the private residence.

“The lodging fee is twenty-five nyang, the food comes to five nyang, and the property damage fee is fifty nyang. The total is eighty silver nyang.”

Hyuk Mujin, who had been rejoicing yesterday over emptying the pockets of those mounted bandits, gaped.

“Property damage? Fifty silver nyang?”

“When I went to the rear courtyard, I found that five old pine trees had fallen.”

They were the trees Wolhwa had said were expensive.

Hyuk Mujin and I turned our heads at the same time. Jin Mukyung, whose eyes met ours, flinched before opening his mouth.

“I got carried away while practicing my swordsmanship.”

“……No, fuck. If you get carried away, does that mean you can cut down anything in your way? Huh?”

“Hoooo.”

Hyuk Mujin couldn’t say anything. He merely kept letting out furious sighs.

At a glance, it was obvious that the bill exceeded the amount we had on hand. If it had only been a little over, we might have been able to talk things out and find a compromise…

“Mujin, how much money do you have right now?”

“Forty nyang.”

*To hell with a compromise. We’re nowhere close.*

“Could we put it on credit?”

That was the exact moment the kind smile around the private-residence manager’s lips disappeared.

“Young Master Jin, what are you doing here?”

A beautiful woman in a light, flowing palace-style dress was approaching us.

Wolhwa’s appearance was nothing short of a lifeline.

I felt bad about turning down her proposal so decisively the night before, but this was no time to be picky.

“Well, you see…”

When I explained the situation, Wolhwa’s eyes grew round.

“Eighty nyang? That can’t be right.”

“Exactly. I knew something was wrong.”

“Give me that.”

She took the bamboo slip from the manager and began to read.

The deeper her frown grew, the clearer it seemed that the arithmetic had been badly botched.

*Knew it.*

At last, Wolhwa finished reading the bamboo slip. A chill entered her voice.

“Are you not doing your job properly?”

“I-I’m sorry.”

“Who do you think these gentlemen are, to dare pull this kind of stunt? Write the prices correctly.”

Hyuk Mujin whispered in a small voice.

“What a relief.”

“Yeah. We almost had to wash dishes before leaving.”

“What kind of hardship is this because of the Second Young Master?”

“Don’t even mention that man. Just hearing about him gives me cancer.”

“What’s cancer?”

“……It’s something bad.”

Meanwhile, the manager revised the prices while sweating profusely. Then he bent deeply at the waist and apologized to us.

“I’m sorry. I was thoughtless and committed a grave discourtesy.”

Hyuk Mujin accepted the apology with an arrogant air.

“Don’t do that again. You have to know who you’re dealing with before pulling a prank. So how much is it?”

“One hundred and five nyang, along with twenty-three iron coins.”

“……”

“……”

*What the hell? Is this a dream?*

My head turned toward Wolhwa of its own accord.

“What is that supposed to mean?”

“He arbitrarily lowered the price because you were my acquaintances. How dare he take the young masters of the Jin Family of Taiyuan for fools? Apologize to them again.”

“I’m sorry for failing to recognize your identities!”

“But…”

I asked in a thoroughly choked voice.

“We can put it on credit, right? Of course.”

“No, you can’t. Of course not. We haven’t allowed that even once in the past two years.”

“How about making an exception and setting a precedent this time?”

“I don’t have any plans to do that yet. You’ll have to aim for the next opportunity.”

Wolhwa added with a bright smile,

“Was there something else you wanted to say?”

“……M-Mount Heng.”

“What was that?”

I squeezed my eyes shut and continued.

“Would you like to come with us to the Mount Heng Sword Sect?”

“Wow, I’d love to.”

*That hateful smile.*

At Wolhwa’s gesture, the manager snatched up the bamboo slip and vanished at the speed of light.

“We won’t have to worry about travel expenses anymore.”

While Hyuk Mujin was the sort of person who simply accepted reality, someone else was shouting vehement opposition.

“Nonsense! How can you bring a woman along while carrying out a family mission?”

“Then stay here and wash dishes.”

“……”

“Who here cut down the old pine trees? Raise your hand.”

Jin Mukyung didn’t raise his hand. Wolhwa slightly lifted the hem of her skirt and greeted him.

“Please take good care of me, Young Hero Jin.”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 106`.

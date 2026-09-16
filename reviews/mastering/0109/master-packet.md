# Master Edit Task — Chapter 109

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
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 월화     | **Wolhwa**         |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 대주     | **Squad Leader** / **Commander**             |
| 지부장    | **Branch Leader**                            |
| 일격     | **One Strike**                         |
| 퀘스트              | **Quest**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본문      | **our sect / this sect**                                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 삭주 | **Sakju** | Jin Family branch location |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 토호단 | **Earth Tiger Band** | Mounted-bandit group formerly led by Pung Yang's subordinate. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 월화 | 춘삼 | Lower District Sect branch leader to subordinate | Chunsam | commanding-familiar | Uses 춘삼아 while directing him to execute the interrogation order. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |

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

#### Chapter 107 tail (verified mastered)

…
At the words of the coachman and bodyguard, whom I assumed to be a member of the Lower District Sect, we headed outside. More precisely, one of us was dragged out by someone. “Follow me.” “Gah! Captain! Captain!” I ignored Hyuk Mujin as Jin Mukyung dragged him away by the collar and looked up at the sky. *Hmm. The moon sure is bright tonight.* “What are you doing?” “As you can see.” Wolhwa smiled faintly. “You seem to enjoy looking at the scenery.” “I’ve been getting into it lately.” The only scenery to be found in the modern world was the nightscape seen from some high vantage point. Even that consisted of sad lights created by office workers working overtime. *Now this is real scenery.* There were no dense forests of skyscrapers, apartment complexes, or industrial sites. In place of asphalt roads, damp dirt paths and crisp air filled the entire world. *Living in a place like this would be genuinely healing.* The problem was that it was also an easy place to get killed. Somehow, people were more frightening here than monsters. I didn’t even need to go as far as the Head Elder or Jopil. What had happened at the Phoenix Inn just yesterday was enough. “Oh, right. What happened to those guys?” “If you mean the mounted bandits from the Red Wind Band, they’ve been detained. Of course, we had to call a physician first.” I’d beaten the shit out of them, so of course they’d needed treatment. But there was another word that caught my attention more than that. “The Red Wind Band?” They’re a rising power from Gaoyuan. They’re fairly large, and more than anything, the Red Wind Band Leader is said to possess formidable martial arts. Northern Gaoyuan. I had first learned of that place from a map during the war with the Mount Heng Sword Sect. One thing puzzled me. Gaoyuan was a considerable distance from Honju, where the Phoenix Inn was located. As far as I knew, the journey took more than a week even if you rode day and night. “How did people like that end up all the way here?” “Toward the end of the war, Lee Cheonbaek hired countless wandering martial artists and mounted-bandit groups. Many of them met their end at Eight Spring Gorge, but some survived and fled.” “So the Red Wind Band was among them?” Wolhwa shook her head. “The Red Wind Band Leader… He was quicker-witted than I expected.” “Then what happened?” “He watched the situation until the very end. He kept a close eye on Eight Spring Gorge from only two shichen away, then turned his horse around the moment he heard how the battle had ended—along with the two hundred men under his command.” Two hundred people. What would have happened if the Red Wind Band had joined the battle at Eight Spring Gorge that day? There would have been an enormous number of casualties, and it might even have affected the outcome of the battle. “We were lucky.” “We were. For the Mount Heng Sword Sect, it was incredibly unlucky.” Wolhwa continued as she firmly packed tobacco leaves into her long-stemmed pipe. “The Red Wind Band headed north immediately. They targeted the Mount Heng Sword Sect’s main base after most of its forces had withdrawn.” “……Huh.” They were natural-born plunderers. The moment the tide of the war turned, they headed north and sank their teeth into the Mount Heng Sword Sect’s throat while most of its main force was away. They had preserved their forces by staying out of the battle, and they must have been well-rested too. They would have been in peak condition. “Young Master Jin, you heard how it ended, didn’t you?” “Yes.” After two days of fierce fighting, the Mount Heng Sword Sect ultimately emerged victorious—but at the cost of the Young Sect Leader, who was supposed to succeed his father. “But the rumors I heard said that wandering martial artists and mounted bandits were mixed together.” “A tiger doesn’t become a dog just because it has lost its teeth. The Red Wind Band Leader had recruited quite a few wandering martial artists as well. They would have made excellent shields.” *Tap, tap.* Wolhwa took out a fire starter, lit it, and drew on her long-stemmed pipe. “The mounted bandits Young Master Jin defeated were probably the ones who fled at that time. Even if the Red Wind Band is unusually disciplined for a mounted-bandit group, it doesn’t mean they have no deserters at all. I’m not sure what they were doing in Honju, though.” “Deserters…” “That’s why the surrounding area has been so unsettled lately. Wandering martial artists, bandits, mounted bandits, even dark-path figures—they’re all starting to rear their heads now that the Mount Heng Sword Sect’s strength has been so badly diminished.” “They’ll have no choice but to accept our proposal.” Wolhwa gave me a prim smile. “Strictly speaking, it isn’t *our* proposal. It’s the Jin Family of Taiyuan’s, isn’t it? Still, from my perspective, this is certainly a good time to pressure the new Sect Leader.” “By the way…” “Yes?” “Do commoners really visit this shrine in weather like this?” “Of course not. Hunters, perhaps. Why do you ask all of a sudden?” I pointed toward the mountain path. Through the light snowstorm that had begun to swirl, I could see torches climbing toward us.

#### Chapter 108 tail (verified mastered)

…
A deathly silence fell. Hyuk Mujin, one eye bruised deep blue, whispered to me, “Am I actually alive right now?” “Yeah. Your breath against my ear is giving me goose bumps, so move away.” “Just a moment ago, I was wondering how anyone could get beaten like a dog that badly, but now…” *Gulp.* Hyuk Mujin swallowed dryly, his gaze fixed on the fallen leader. “Hng… Hng…” With all four limbs broken and his dantian destroyed, the man struggled for breath. If he received proper care, he might be able to walk again, but his life as a martial artist was over. The Level window I sensed through Qi Sense was proof. > **System** > > **Level 2 — Lee Sam** *The dung flies those watchers used as Familiars were Level 1, if I remember right.* The culprit who had reduced a Level 25 martial artist—one who had once been close to First Rate—to a living corpse kept stealing glances in our direction. “Captain, please save me. I think the Second Young Master is still short on blood.” “Stop talking nonsense and move that guy somewhere suitable. He’ll die if you leave him like that.” “Doesn’t he deserve to die? They were selling perfectly innocent commoners.” “Move him anyway. He’s still alive.” One of the greatest sources of dissonance I had felt while moving between Murim and the modern world was the issue of killing people. For twenty-seven years, I had lived in a society governed by law and order. I had trained to kill enemies with bladed weapons, but my targets had been monsters, not living humans. *I was sure that was the case…* Now I couldn’t even remember how many people I had killed. Even after realizing that the enemies who had died by my hand might have been real people rather than NPCs, I hadn’t felt much guilt. *They were enemies. They were trying to kill me too.* I didn’t know whether it was because I had lived as a Hunter or because I had grown accustomed to Murim’s ways. I was only surprised by my own numbness and the simplicity of my self-justification. *For now, this much should be fine.* I was living in two completely different worlds. I couldn’t afford to play at being some half-baked Buddhist disciple. I shook off the thoughts clinging to me and approached the men cowering on the ground. “Eek!” “Uaaagh! Save me, Boss!” “You bastards make a fuss even when I’m trying to save you. Hold still.” I untied the ropes, and the Five-Colored Ghosts were free. They stood on trembling legs. “Th-thank you.” “We’ll serve you as our Benefactor for the rest of our lives!” “Like hell you will. Anyway, how did you end up getting caught by men like these? All five of you at once?” The Five-Colored Ghosts were small, but they were grown men, at least in name. They had been strong enough to commit banditry alongside the Heavenly Axe. “Um, well…” “…?” What was wrong with these guys? Sensing something off in their hesitation, I grabbed the nearest human trafficker by the collar and hauled him up. “How did you catch them?” “We caught them trying to steal our money pouches in the marketplace.” “…” What the hell, these Ten-Colored Ghosts. I thought they had quit being bandits and might have taken up farming, but they had only changed occupations? “Explain yourselves.” Under my piercing stare, the five men’s eyes darted around. “W-well…” “Boss, this is the only kind of thing people like us ever learned to do.” “E-even so, we only started recently!” “We tried to work honestly, but nothing went right… We said we’d pull just one job and get out, but then…” “If we’d known they were mounted bandits, we never would’ve touched them. We’re victims too. Boss, please forgive us just this once!” As I wondered what to do with these men, a familiar word made me pause. “What did you say?” “We’ll live honestly if you forgive us just one more time!” “No, not that. What did they say?” “Ah, do you mean the mounted-bandit group?” “Yeah. That.” “We only found out after they caught us. Some ruffians were throwing silver around at a pleasure house, so we followed them… Turns out they were from the Red Wind Band, infamous for their viciousness even among mounted bandits.” “The Red Wind Band? Are you sure?” “Yes. I heard it clearly with my own ears. Right?” The others began eagerly adding their own pieces. “They also said they were leaving at first light tomorrow.” “They said they’d have to ride without stopping to reach Saneum. They were even worried they might lose their heads if they arrived late.” “So that’s how it is.” Yesterday, and now today. Running into mounted bandits from the Red Wind Band two days in a row was already an uncanny coincidence. On top of that, Saneum was close to Eung-hyeon, where the Mount Heng Sword Sect’s headquarters stood. “Are these men telling the truth?” The human trafficker whose collar I held in my right hand—or rather, the mounted bandit from the Red Wind Band—nodded, trembling. At that moment— *Shriek!* A hawk landed in front of the shrine with a sharp cry. A small cylinder tied to its ankle caught my eye. *A messenger eagle.* Things were taking a strange turn. [^1]: A nickname meaning “Five-Colored Ghosts.”

## Korean source

```text
＃109화



전서응(全書鷹).

태원진가에도 두 마리밖에 없다는 연락용 매다.

훈련시키기 어렵다 보니 중요한 정보를 전달하는 데에만 쓰인다고 들었는데…….

‘누가 보낸 거지?’

전서응을 향해 다가가려는 나를 붙잡은 건 월화의 목소리였다.

“물러서는 게 좋을걸요? 경계심이 심한 녀석이라 진 공자가 잡으려고 들면 도망칠 테니까.”

“아, 혹시?”

“본문에서 보낸 전서응이에요. 특정한 추종향(追從香)을 쫓아오도록 훈련되어 있죠.”

월화가 품에서 자그마한 주머니를 꺼내 흔들자, 전서응이 슬금슬금 다가와 부리를 비빈다.

그 틈에 어느새 밖으로 나온 하오문도가 전서응의 발목에 묶인 원통을 풀었다.

“어디야?”

“하루 전 삭주지부에서 지부장님 앞으로 보낸 전서입니다.”

“이리 줘.”

전서를 건네받아 읽는 월화의 표정이 오묘했다.

굳게 다물어져 있던 입술이 열린 것은 잠시 후였다.

“적풍단주…… 생각 이상인데.”

“또 적풍단에 관련된 겁니까?”

작게 고개를 끄덕인 월화가 내게 전서를 내밀었다.

읽어 보라는데 굳이 마다할 필요가 있나, 쭈뼛거리던 진무경과 혁무진도 슬쩍 고개를 들이밀었다.



적풍단, 고원을 넘어 남하 중. 숫자는 대략 이백으로 추정.



짤막한 한 줄이 의미하는 바는 명백했다.

“다시 한번 항산검문을 치려는 거군요.”

“틀림없어요. 하루 전 소식이니 그만큼, 아니 그 이상으로 거리가 좁혀졌을 거고요.”

현재 항산검문까지 남은 거리는 하루하고도 반나절.

마적단인 만큼 뛰어난 기동력으로 목적지를 향해 진군하고 있을 것이다.

“안타깝게도 저희 지부는 북부에 제대로 된 정보망을 갖추지 못했어요. 그나마 다행인 건…….”

월화의 시선이 적풍단의 마적들을 향했다. 이미 오래전 전의를 상실한 그들은 움찔하며 고개를 숙였다.

“여기 소중한 정보원들이 있다는 거죠. 쓸 만한 정보를 갖고 있을지는 모르겠지만.”

마적들을 훑어보던 그녀가 돌연 한 사람을 지목했다.

“너, 일어나.”

“……저, 저 말입니까?”

잔뜩 겁먹은 얼굴로 일어난 그는 생각 이상으로 젊은 청년이었다. 마적 중 가장 어리고 약한 그 녀석은 월화의 시선을 정면으로 쳐다보지도 못했다.

“나이가?”

“오, 올해 약관을 넘겼습니다.”

“약관? 어리네. 하긴, 어리다고 마적이 될 수 없는 건 아니니까.”

“전 마적이 아닙니다! 얼마 전에 낭인이 되었는데 한몫 단단히 챙겨 준다는 말에 그만…….”

“아, 지난번 습격 때 적풍단주가 끌어모은 낭인 중 하나구나?”

“예, 예! 제가 아는 사실은 모두 말씀드리겠습니다!”

“아냐, 괜찮아.”

“예?”

“별로 아는 것도 없어 보이는데 뭘. 안 그러니, 춘삼아?”

지금까지 묵묵히 마부를 자처하던 하오문도.

그가 대답 대신 품에서 꺼낸 소도(小刀)를 청년의 가슴에 박아 넣었다.

푹-

일류 무인의 빠르고 정확한 일격이 심장을 갈랐다. 비명도 지르지 못한 채 입을 벙긋거리던 청년이 실 끊어진 인형처럼 쓰러졌다.

쿵.

싸늘한 적막이 장내를 짓눌렀다. 경악과 공포로 물든 마적들의 시선 속에서, 월화의 가느다란 손가락이 다시 한번 움직였다.

“너.”

“마, 말하겠소! 전부 다 말하겠소! 나는 적풍단에 일 년째 몸담고 있는…….”

“춘삼아.”

쐐애애액! 서걱!

“크륵, 그르륵.”

마적이 피가래 끓는 소리와 함께 뒷걸음질 쳤다. 쩍 벌어진 목을 막아 보지만 손가락 사이로 뿜어져 나오는 피분수를 막을 수는 없다.

“단 두 가지만 명심하면 돼.”

머리부터 발끝까지.

선홍빛 핏물을 뒤집어쓴 월화가 건조한 어조로 말을 이었다.

“대답은 묻는 말에만, 있는 사실 그대로.”

“……!”

우리는 불과 촌각(寸刻) 만에 적풍단에 관한 모든 정보를 얻을 수 있었다.



* * *



한시가 급하다는 걸 알게 된 우리는 마차를 버리고 말을 한 마리씩 골라잡았다. 나, 진무경, 혁무진, 그리고 월화.

하오문도는 오색귀와 생존한 마적들을 데리고 가까운 하오문 지부에서 상황을 전달할 것이다.

“너무 잔인했나요?”

월화가 말안장을 올리며 건넨 물음에 나는 턱을 긁적였다.

“솔직히, 조금 놀라긴 했어요.”

항상 여유롭고 장난기 넘치는 모습만 봐서 잠시 잊고 있었다. 그녀도 무림인이라는 사실을.

‘그것도 경륜 있는 무림인이지.’

월화의 나이가 어떻게 되더라?

물어본 적이 없어 잘은 모르지만 서른은 넘지 않을 것이다.

그런 젊은 나이에 산서성 전체를 총괄하는 지부장이 되었다는 것은 그에 걸맞은 결단력을 갖췄다는 뜻이다.

‘잔인하지만 효과적인 방법이었어.’

망설임 없이 두 명을 죽였다. 그것도 파리 잡듯 간단하게.

진무경이 우두머리를 상대로 보여 준 모습도 마적들에겐 두려웠겠지만 죽음에 대한 공포는 그 이상이다.

벼랑 끝으로 내몰린 그들은 필사적으로 정보를 쏟아 내는 수밖에 없었다.

“저라도 술술 불었을 것 같은데요.”

“진 공자가 오해할까 봐 말해 두는데, 살생에는 취미 없어요. 상대가 선량한 양민들도 아니었고…… 아, 이놈의 피는 닦아도 끝이 없네.”

주르륵 흘러내리는 피는 두 번째로 죽은 마적의 것이다.

콧잔등을 찡그리는 그녀를 향해 천 조각을 내미는 한 사람이 있었다.

“이, 이걸로 닦으시오.”

“어머.”

“엥?”

“흐음.”

월화와 나, 그리고 혁무진의 반응에 진무경이 헛기침을 연발했다.

“그, 필요할 것 같아서.”

“고마워요, 진 소협. 마침 딱 필요했는데.”

“별것 아니오.”

말과는 달리 표정은 상당히 뿌듯해 보이는데?

저놈 저거 설마…….

‘여자한테만 잘해 주는 타입이구나.’

어딜 가나 저런 놈이 꼭 하나씩 있지. 천하의 진천검도 별다른 것 없던 모양이다. 그때 피를 닦아 낸 월화가 품에서 돌돌 만 가죽을 꺼내어 펼쳤다.

“산서성 전역을 대략으로 표기한 지도에요. 우리 위치는 지금 여기. 적풍단은 아마…… 쉬지 않고 이동했다면 이미 대동(大同)을 돌파했을지도 모르겠네요.”

“저희보다 빠르군요.”

“지금으로선 반나절. 하지만 우리가 가는 길에는 관도가 잘 정비되어 있으니 밤낮없이 달린다면 충분히 격차를 좁힐 수 있을 거예요.”

요컨대 쉴 생각은 하지 말라는 뜻이다. 나는 사람들을 따라 말안장 위로 훌쩍 뛰어올랐다.

‘어째 오자마자 일이 터지냐.’

내심 한숨이 나왔지만, 별수 있나. 한두 번 고생하는 것도 아니고 이젠 그러려니 해야지.

‘이거 되게 간단한 퀘스트였던 것 같은데.’

띠링.



- 퀘스트 난이도가 [절정]으로 변경되었습니다.



“…….”

어, 그래. 이젠 아니구나.



* * *



여우를 닮은 사내였다. 뾰족한 턱과 귀, 날카롭게 찢어진 눈동자는 주위의 모든 것들을 감시하는 동시에 관찰했다.

“크아아악!”

“죽여라, 싸그리 다 죽여!”

“꺄아아아아!”

커다란 장원에서 솟구치는 연기, 그리고 비명.

말에 올라 언덕 아래를 응시하던 사내, 적풍단주 풍양(風陽)의 입이 열린 것은 장원이 잠잠해진 후였다.

“끝났나?”

보고를 위해 막 언덕을 올라온 마적이 대답했다.

“사내놈들은 전부 죽였고, 아이와 여자들은 한데 모아 뒀습니다.”

“왜?”

“예? 그야 당연히 고원의 전통대로…….”

마차 바퀴보다 큰 사내는 아이라도 가차 없이 죽이고, 여인은 취하거나 노예로 팔아 버린다. 그것이 유목민들로부터 전해져 내려오는 전통 아닌 전통이었다.

마적의 말에 풍양은 조용히 손가락을 까딱였다.

“이리 가까이 와 보게.”

주춤주춤 다가온 마적이 조심스럽게 물었다.

“단주, 제가 혹시 큰 실수라도…….”

“원래 어디 소속이었나?”

“얼마 전까지 토호단에 부단주로 있었습니다.”

“토호단? 아, 기억나. 거기 부단주가 자네였군.”

“예, 옛! 단주의 고강한 무공과 훌륭한 인품에 반해 충성스러운 수하가 되기로 맹세했습니다!”

풍양은 미묘한 얼굴로 코를 긁적였다.

그랬던가? 그가 기억하는 건 서른 명쯤 되는 부하를 데리고 단주랍시고 거들먹거리는 쓰레기를 일 합에 죽인 것뿐이었다.

“내 기억과는 좀 다르지만 어쨌든 고맙네.”

“아닙니다, 영광입니다!”

“그런데 말이야. 토호단은 어땠을지 모르지만, 이곳 적풍단은 좀 달라. 고원의 전통이라든지 하는 자질구레한 것들 말일세.”

“아, 미처 몰랐습니다.”

“단주인 내 명령이 최우선이야. 알겠나?”

“앞으로 명심, 또 명심하겠습니다!”

“아마 저 친구들도 몰라서 고원의 전통을 지킨 모양이야. 다들 자네처럼 새로 합류한 이들이거든. 그러니 가서 내 뜻을 전해 줄 수 있겠나?”

“존명. 한 놈도 살려 두지 않겠습니다.”

마적답지 않게 어설픈 군례까지 갖추는 그를 향해 풍양은 손을 내저었다.

“그래, 어서 가 보게.”

“옛!”

말을 몰아 떠나는 그의 뒷모습을 응시하던 풍양이 돌연 소매를 떨쳤다.

쉭, 바람이 갈라지는 소리와 함께 뻗어 나간 빛줄기가 십 장(약 30m) 밖에서 목표를 관통했다.

푹! 털썩.

말은 계속해서 내달렸다.

이미 숨이 끊긴 주인이 등자에 발이 걸려 지금 이 순간에도 너덜너덜해지고 있다는 사실을 모른 채.

“가서 전해. 포로는 없다고. 다 죽이고 불태우라고.”

“예, 단주님.”

풍양의 수하가 떠나고 얼마 지나지 않아 장원 전체가 화염에 휩싸였다. 금세 타들어 가는 현판(懸板)을 확인한 그의 입가에 슬쩍 웃음이 맺혔다.

항산검문 대동지부.

적풍단이 다시 한번 고원을 넘은 순간이었다.



* * *



넓은 대전.

갑론을박을 벌이던 사람들은 전령의 보고에 숨이 턱 막혔다.

“놈들이 대동을 돌파했습니다!”

“버, 벌써?”

“대동지부는? 경계를 위해 나가 있던 인원들은 어찌 되었나?”

“전멸, 전멸입니다. 대동지부는 잿더미가 되었고 생존자는 한 명도 없습니다.”

“뭣이?”

“혹 소식이 잘못 전해진 건 아닌가? 놈들도 지난번에 큰 타격을 입었을 터인데 어찌 이리 빨리……!”

“다른 마적단을 흡수한 듯합니다. 최소 이백 명, 혹은 그 이상입니다.”

“그 말이 사실인가?”

“예, 틀림없습니다.”

“그, 그럼 도대체 언제쯤 여기까지……?”

“빠르면 하루, 늦어도 이틀 안에 놈들의 공격이 시작될 것으로 예상됩니다.”

“끝장이군.”

누군가의 중얼거림은 이 자리에 모인 대부분의 마음과 크게 다르지 않았다.

열 명 남짓한 그들은 모두 항산검문의 주요 직책을 맡은 중진. 그러나 누구 하나 빠지지 않고 마음속으로는 이미 패배라는 단어를 만지작거리는 중이었다.

“철검대주, 이 싸움 자신 있어?”

“각주씩이나 되는 양반이 왜 나한테 물어? 여기서 무인이 나밖에 없나.”

대항산검문의 대주. 당주, 혹은 각주.

한때는 분명 그 위치에 오르길 간절하게 소망한 적이 있었다. 한때는, 말이다.

‘대항산검문은 얼어 죽을. 이제 와서 승진시켜 주면 뭐 하나, 문파가 이 꼴인데.’

‘가만히 둬도 망할 판국에 마적단까지 와서 난장을 피우는군. 어디 보자, 남아 있는 놈들을 박박 긁어모으면 한 백 명 되려나?’

태원진가와의 전쟁으로 팔 할에 가까운 전력을 상실했다.

공들여 키운 정예 무인들과 풍진강호를 헤쳐 온 노련한 중진들, 무엇보다 문파가 가진 힘을 상징하는 절정 고수들과 금력(金力)의 상실이 가장 뼈아프다.

“제기랄, 문주라도 살아 있었다면.”

일개 낭인으로 시작하여 지금의 항산검문을 키워 낸 이천백. 그의 무공과 수완이라면 이 사태를 뒤집을 수 있을 것이다.

그러나 혈랑검 이천백은 이미 죽고 없다. 그의 핏줄 중 살아남은 이는 오직 한 사람뿐이다.

“이런 상황에 약관도 안 된 어린 계집을 문주라고 모셔야 하다니.”

누군가 홧김에 말을 내뱉은 그 순간.

쾅!

굳게 닫혀 있던 대전의 문이 폭발했다.
```

## Current accepted English baseline

```markdown
# Chapter 109

A messenger hawk.

I’d heard the Jin Family of Taiyuan had only two of them. They were messenger birds, but difficult to train, so they were used only to deliver important information…

*Who sent it?*

Just as I was about to approach the messenger hawk, Wolhwa called out to me.

“You’d better keep your distance. It’s a very wary bird. If Young Master Jin tries to catch it, it’ll fly away.”

“Ah, could it be?”

“It’s a messenger hawk sent from our sect. It was trained to follow a specific tracking scent.”

Wolhwa pulled a small pouch from her robes and shook it. The messenger hawk cautiously approached and rubbed its beak against it.

In that moment, a Lower District Sect member who had somehow already slipped outside untied the cylinder from the hawk’s ankle.

“Where’s it from?”

“A letter sent yesterday from the Sakju Branch to the Branch Leader.”

“Give it to me.”

Wolhwa accepted the letter and read it. Her expression turned complicated.

It took a while before her tightly closed lips finally parted.

“The Red Wind Band Leader… He’s more than I expected.”

“Is this about the Red Wind Band again?”

Wolhwa gave a small nod and handed me the letter.

There was no reason to refuse when she was telling me to read it. Jin Mukyung and Hyuk Mujin, who had been hesitating nearby, cautiously leaned in as well.

The Red Wind Band is moving south across the plateau. Their numbers are estimated at approximately two hundred.

The short line made its meaning clear.

“They’re planning to attack the Mount Heng Sword Sect again.”

“There’s no doubt about it. This news is already a day old, so they must have narrowed the distance by that much—or more.”

We were currently a day and a half away from the Mount Heng Sword Sect.

As a mounted-bandit group, they would be advancing toward their destination with exceptional mobility.

“Unfortunately, our branch doesn’t have a proper intelligence network in the northern region. The one fortunate thing is…”

Wolhwa’s gaze shifted toward the mounted bandits of the Red Wind Band. They had lost the will to fight long ago, and flinched as they lowered their heads.

“We have valuable sources of information right here. I don’t know whether they have any useful information, though.”

After looking over the mounted bandits, she suddenly pointed at one of them.

“You. Stand up.”

“……M-me?”

The man rose with a thoroughly terrified expression. He was younger than I expected. The youngest and weakest of the mounted bandits, he couldn’t even meet Wolhwa’s gaze.

“How old are you?”

“I-I passed twenty this year.”

“Twenty? You’re young. Then again, being young doesn’t stop someone from becoming a mounted bandit.”

“I’m not a mounted bandit! I only became a wandering martial artist recently, but then they said they’d give me a big cut, so I…”

“Ah, so you’re one of the wandering martial artists the Red Wind Band Leader gathered for the last attack?”

“Y-yes! I’ll tell you everything I know!”

“No, it’s all right.”

“Pardon?”

“You don’t look like you know much anyway. What would be the point? Isn’t that right, Chunsam?”

The Lower District Sect member who had silently played the part of our carriage driver until now.

Instead of answering, he pulled a small knife from his robes and drove it into the young man’s chest.

*Thunk—*

A First Rate martial artist’s fast, precise One Strike split the young man’s heart. He opened and closed his mouth soundlessly before collapsing like a puppet with its strings cut.

*Thud.*

A frigid silence pressed down on the scene. While the mounted bandits stared in horror and fear, Wolhwa’s slender finger moved once more.

“You.”

“I-I’ll talk! I’ll tell you everything! I’ve been with the Red Wind Band for a year…”

“Chunsam.”

*Whoosh! Slash!*

“Grrk… Gurg…”

The mounted bandit staggered backward, making a wet, blood-choked sound. He tried to cover his gaping throat, but couldn’t stop the fountain of blood spraying between his fingers.

“You only need to remember two things.”

From head to toe, Wolhwa was covered in crimson blood. She continued in a dry tone.

“Answer only what you’re asked, and tell the truth exactly as it is.”

“……!”

In mere moments, we learned everything there was to know about the Red Wind Band.

* * *

Once we learned that every second mattered, we abandoned the carriage and each chose a horse. Me, Jin Mukyung, Hyuk Mujin, and Wolhwa.

The Lower District Sect member would take the Five-Colored Ghosts and the surviving mounted bandits to a nearby Lower District Sect branch and report what had happened.

“Was that too cruel?”

Wolhwa asked as she lifted a saddle onto her horse. I scratched my chin.

“To be honest, I was a little surprised.”

I had temporarily forgotten because I had only ever seen her relaxed and playful. She was a martial artist too.

*And an experienced one at that.*

How old was Wolhwa, anyway?

I’d never asked, so I didn’t know for sure, but she couldn’t have been over thirty.

To become the Branch Leader overseeing all of Shanxi at such a young age, she had to possess the decisiveness to match the position.

*Cruel, but effective.*

She had killed two people without hesitation. Just as casually as swatting flies.

Jin Mukyung’s display against the leader must have terrified the mounted bandits, but the fear of death was even greater.

Driven to the edge of a cliff, they had no choice but to pour out information desperately.

“I think I would’ve spilled everything too.”

“I’m saying this in case Young Master Jin gets the wrong idea, but I don’t enjoy killing people. They weren’t innocent commoners, either… Ah, this bastard’s blood just won’t stop, even when I wipe it.”

The blood streaming down her belonged to the second mounted bandit she had killed.

As she wrinkled her nose, someone held out a piece of cloth to her.

“U-use this to wipe it off.”

“Oh my.”

“Huh?”

“Hmm.”

At the reactions from Wolhwa, me, and Hyuk Mujin, Jin Mukyung cleared his throat repeatedly.

“I thought you might need it.”

“Thank you, Young Hero Jin. I needed it.”

“It’s nothing.”

His expression, however, looked quite pleased.

*No way. Is he…*

*The type who’s only nice to women?*

There was always at least one guy like that wherever you went. Even the Heaven Shaking Sword wasn’t any different, apparently.

After wiping away the blood, Wolhwa pulled a rolled-up piece of leather from her robes and spread it out.

“This is a rough map of the entire Shanxi region. Our location is here. The Red Wind Band has probably… If they’ve been moving without rest, they may have already broken through Datong.”

“They’re faster than us.”

“By half a day for now. But the roads along our route are well maintained, so if we ride day and night, we can narrow the gap enough.”

In short, she was telling us not to expect any rest.

I followed the others and leaped onto my saddle.

*Why does something always happen the moment I arrive?*

I wanted to sigh, but what could I do? It wasn’t as though this was my first hardship—or my second. I’d just have to accept it.

*Wasn’t this supposed to be a really simple Quest?*

*Ding.*

> **System**
>
> Quest difficulty has changed to **Peak**.

“……”

Right. I guess it wasn’t simple anymore.

* * *

He was a man who resembled a fox. His pointed chin and ears, along with his sharp, slanted eyes, watched and observed everything around him at once.

“Graaah!”

“Kill them! Kill every last one of them!”

“Aaaah!”

Smoke billowed from a large manor, accompanied by screams.

The man sitting on horseback and gazing down from the hill was Pung Yang, the Red Wind Band Leader. He didn’t speak until the manor had fallen silent.

“Is it over?”

A mounted bandit who had just climbed the hill to deliver his report answered.

“We killed all the men and gathered the women and children together.”

“Why?”

“Pardon? Why, because it’s the plateau’s tradition, of course…”

Any male taller than a cartwheel—even a child—was killed without mercy, while the women were taken or sold as slaves. It was a tradition—or something close to one—passed down from the nomads.

At the mounted bandit’s words, Pung Yang quietly crooked one finger.

“Come closer.”

The mounted bandit approached hesitantly and asked carefully,

“Leader, did I perhaps make some serious mistake…”

“Where did you belong before?”

“Until recently, I was the deputy leader of the Toho Band.”

“The Toho Band? Ah, I remember. You were their deputy leader.”

“Y-yes! I was so impressed by your formidable martial arts and noble character that I swore to become your loyal subordinate!”

Pung Yang scratched his nose with an ambiguous expression.

*Was that so?*

All he remembered was killing a piece of trash in a single strike—the man who had swaggered around calling himself a bandit leader while commanding some thirty subordinates.

“My memory differs a little, but thank you anyway.”

“Not at all! It’s an honor!”

“However, the Earth Tiger Band may have been different. The Red Wind Band has its own way. Those petty matters about plateau traditions, for example.”

“Ah, I didn’t realize.”

“My orders as leader take priority. Do you understand?”

“I’ll keep that in mind—over and over again!”

“Those fellows probably followed the plateau’s traditions because they didn’t know any better. They all joined recently, just like you. So go and convey my wishes to them, will you?”

“Understood. I won’t leave a single one alive.”

The mounted bandit even gave an awkward military salute, though there was nothing military about a mounted bandit. Pung Yang waved him away.

“Yes, go on.”

“Yes, Leader!”

Pung Yang watched him ride away, then suddenly flicked his sleeve.

With a sharp sound as the air split, a streak of light shot out and pierced its target ten jang away—about thirty meters.

*Thud!*

*Clatter.*

The horse continued racing forward.

Its rider was already dead, but his foot remained caught in the stirrup. Unaware that his body was being dragged and battered to shreds, the horse galloped on.

“Go and tell them. There are no prisoners. Kill them all and burn the place.”

“Yes, Leader.”

Not long after Pung Yang’s subordinate departed, the entire manor was engulfed in flames. As he watched the signboard burn away in an instant, a faint smile touched the corners of his mouth.

The Datong Branch of the Mount Heng Sword Sect.

The moment the Red Wind Band crossed the plateau once more.

* * *

The people gathered in the spacious main hall had been arguing back and forth when the messenger’s report left them speechless.

“They’ve broken through Datong!”

“A-already?”

“What about the Datong Branch? What happened to the men who went out to stand guard?”

“Everyone was wiped out. Everyone. The Datong Branch was reduced to ashes, and there were no survivors.”

“What?”

“Could the report be wrong? They must have suffered heavy losses last time, so how could they have come this far so quickly…?”

“They appear to have absorbed another mounted-bandit group. At least two hundred men—possibly more.”

“Is that certain?”

“Yes, without a doubt.”

“Th-then when will they reach us…?”

“If they’re fast, the attack will begin within a day. At the latest, we expect it within two days.”

“We’re finished.”

The muttered words were not much different from what most of the people gathered there were thinking.

There were a little over ten of them, all senior figures holding important positions in the Mount Heng Sword Sect. Yet every one of them was already turning the word *defeat* over in their minds.

“Iron Sword Squad Leader, are you confident in this fight?”

“Why are you asking me, when you’re a Pavilion Leader? Am I the only martial artist here?”

They were squad leaders, hall leaders, and pavilion leaders of the great Mount Heng Sword Sect.

There had been a time when he had desperately wanted to rise to that position. Once upon a time, that was.

*To hell with being a commander of the Mount Heng Sword Sect. What good is a promotion now, with the sect in this state?*

*We were already doomed if left alone, and now a mounted-bandit group has come to make a mess of everything. Let’s see… If we scrape together every man we have left, there might be a hundred of them.*

The war with the Jin Family of Taiyuan had cost them nearly eighty percent of their strength.

The loss of the elite martial artists they had painstakingly trained and the seasoned senior figures who had weathered the martial world was painful enough. Most devastating of all was the loss of the Peak masters who represented the sect’s power—and its financial resources.

“Damn it. If only the Sect Leader were still alive.”

Lee Cheonbaek had started as a mere wandering martial artist and built the Mount Heng Sword Sect into what it was now. With his martial arts and resourcefulness, he could have turned this situation around.

But the Blood Wolf Sword, Lee Cheonbaek, was already dead. Of his bloodline, only one person remained alive.

“To think we have to serve some little girl who isn’t even twenty as Sect Leader at a time like this.”

At that moment, someone spat out the words in a fit of anger.

*Boom!*

The tightly closed doors of the main hall exploded.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 109`.

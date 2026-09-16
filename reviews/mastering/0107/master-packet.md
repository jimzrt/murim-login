# Master Edit Task — Chapter 107

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

| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 천무학관   | **Heaven's Gate Temple**         |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 살기     | **killing intent**                               |                                                       |
| 낭인     | **wandering martial artist**                     |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 지부장    | **Branch Leader**                            |
| 산서지부장  | **Shanxi Branch Leader**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 보상               | **Reward**                     |
| 몬스터     | **monster**           |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 팔천협    | **Eight Spring Gorge** |
| 본가      | **our family / this family**                                    |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 혼주 | **Honju** | Shanxi location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 관제묘 | **Guandi Temple** | Shrine type mentioned in martial-arts novels. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
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

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

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

#### Chapter 105 tail (verified mastered)

…
woman stood on the stairs leading to the second floor, a veil draped across her face. “Long time no see, our Young Master.” *Our Young Master?* The moment I heard those words, I knew who she was. *Wolhwa.* It was her. * * * Hyuk Mujin and I were led to a guest room on the top floor of the Phoenix Inn. Calling it a guest room hardly did it justice. It occupied the entire floor, so penthouse would have been more accurate. “It’s my first time bringing a man here. And two of them, no less.” Bathed in the soft light, Wolhwa’s smile was dazzling. I had felt it from the moment we first met, but she was the very definition of a femme fatale. Even after meeting her several times, the sight of her was enough to make my stomach churn. Hyuk Mujin was beyond saving. “I-It is the honor of three lifetimes.” “……” Look at that bastard’s glazed eyes. He was completely smitten. Wolhwa gave him a smile, then turned her gaze toward me. “Have you been well, Young Master Jin? Ah, perhaps I can’t call you Young Master the way I used to anymore?” The mischief in her expression made it obvious what was coming. I hurriedly waved my hands. “Just call me whatever you like. Like before.” “Hmm. Then how about Young Master Sleeping Dragon?” “……That’s horrible.” “Oh my, why? Sleeping Dragon of Shanxi sounds wonderful. If you’ve earned that much martial fame at such a young age, you could stand to be a little prouder.” Sleeping Dragon of Shanxi, Flaming Charisma Taekyung—six of one, half a dozen of the other. Seeing my expression, Wolhwa chuckled and put her long-stemmed tobacco pipe to her lips. “I’m only joking. Anyway, teasing Young Master Jin is so much fun.” “Excuse me for interrupting.” Hyuk Mujin had regained some of his senses. He looked back and forth between Wolhwa and me. “May I ask what kind of relationship the two of you have?” “None of your business.” Our relationship was too embarrassing to explain in detail. I cut him off sharply and glanced at Wolhwa, signaling for her to play along. Quick on the uptake, she nodded. “He used to be a regular at my establishment. Not anymore, though.” “……” Like hell she understood. Then again, after how openly she had acted in front of Jin Wikyung and Wipeng, it would have been ridiculous for her to hide it now. Hyuk Mujin, meanwhile, seemed only half-convinced by Wolhwa’s answer. “By ‘establishment,’ do you mean the Phoenix Inn?” “No. This is just a side business. My real profession is something only a beautiful and charming woman like me can do.” “Then perhaps…” “It’s probably exactly what you’re imagining, Young Martial Artist.” “A pleasure house?” “Correct.” Hyuk Mujin’s eyes widened. “So the proprietress of the Phoenix Inn, whom I had only heard about in rumors, was a courtesan.” “Young Martial Artist, you should watch your words. That isn’t very pleasant to hear.” “If I offended you, I apologize. However, your words and behavior don’t exactly appear in a favorable light either.” His sudden seriousness caught me even more off guard. “Hey, what’s with you?” “Captain—no, Young Master—is a direct descendant of the Jin Family of Taiyuan. Even the most beautiful woman under heaven has no right to treat him so casually. As a retainer of our family, I could not simply stand by and watch.” “A moment ago, you said this was the honor of three lifetimes.” “……In any case, how dare a mere courtesan treat the Young Master—agh!” Smack! I gave him a satisfying whack on the back of the head. “She’s the Shanxi Branch Leader of the Lower District Sect.” “Shanxi Branch Leader or not—what? What did you say?” “Are your ears clogged? I said she’s the Shanxi Branch Leader of the Lower District Sect. She gave us extremely—very, very—decisive help in the recent war with the Mount Heng Sword Sect.” “I’m fine, Young Master Jin.” Wolhwa lowered her eyes sadly. “I’m only a mere courtesan, after all.” Hyuk Mujin fell silent for a moment, then bowed his head. “Young Lady—no, Branch Leader. I apologize…” “Then keep your mouth shut.” “Yes, ma’am.” Wolhwa let out a quiet laugh. “You have an interesting subordinate.” As the saying went, it was the squid that disgraced the fish market. That bastard Hyuk Mujin was disgracing the entire Jin Family of Taiyuan all by himself. I was too embarrassed to even look Wolhwa in the eye. “……I apologize for all of this.” “You’re not the one who needs to apologize, Young Master. And he wasn’t entirely wrong.” Thankfully, she let it slide without a fuss. After exhaling a stream of smoke, Wolhwa spoke. “You’re on your way to the Mount Heng Sword Sect, aren’t you?” “Yes.” “May I ask what your purpose is?” “You already know, don’t you?” She was the greatest source of information in all of Shanxi Province. There was no need to ask how she knew. “I wanted Young Master Jin to tell me himself… I’m disappointed.” “Business and personal matters should be kept separate.” “How cold. Then may I make a proposal? Or a deal, if you prefer.” “I’ll decide after I hear it.” Wolhwa tapped the ash from her pipe. “Let’s go together. To the Mount Heng Sword Sect.” “What?” What the hell was she talking about?

#### Chapter 106 tail (verified mastered)

…
earlier. Don’t ask about him anymore, and don’t try to learn anything else. Issue a gag order and make sure no one even mentions this.” “Yes, Branch Leader. I’ll make sure they understand.” “Oh, and one more thing. I’ll be leaving early tomorrow, so make the preparations.” “Who are you planning to take with you?” “No one. I’ll go alone.” “Branch Leader, that…” “It’s an order.” “Understood.” Once her subordinate withdrew, silence settled over the guest room. Wolhwa tapped the blackened tobacco leaves from her pipe and thought. *Jin Taekyung.* If everything he had done until now was true, then the northern interests she needed to extract from the Mount Heng Sword Sect were nothing. *Has anyone in all history ever grown this quickly?* Her gaze darkened as she stared at the place where Jin Taekyung had been sitting. * * * The next morning. I began to feel that something had gone wrong after meeting the person in charge of the private residence. “The lodging fee is twenty-five nyang, the food comes to five nyang, and the property damage fee is fifty nyang. The total is eighty silver nyang.” Hyuk Mujin, who had been celebrating yesterday after emptying those mounted bandits’ pockets, gaped. “Property damage? Fifty silver nyang?” “When I went to the rear courtyard, I found that five old pine trees had fallen.” They were the trees Wolhwa had said were expensive. Hyuk Mujin and I turned our heads at the same time. Jin Mukyung, whose eyes met ours, flinched before opening his mouth. “I got carried away while practicing my swordsmanship.” “……No, fuck. If you get carried away, does that mean you can cut down anything in your way? Huh?” “Hoooo.” Hyuk Mujin couldn’t say anything. He merely let out one furious sigh after another. One look told me the bill exceeded the money we had left. If it had only been a little over, maybe we could have talked it out and found some middle ground… “Mujin, how much do you have right now?” “Forty nyang.” *Middle ground, my ass. We’re nowhere close.* “Could we put it on credit?” That was the exact moment the kind smile around the private-residence manager’s lips disappeared. “Young Master Jin, what are you doing here?” A beautiful woman in a light, flowing palace-style dress was approaching us. Right now, Wolhwa’s appearance was nothing short of a lifeline. I felt bad about turning down her proposal so decisively the night before, but this was no time to be picky. “Well, you see…” When I explained the situation, Wolhwa’s eyes grew round. “Eighty nyang? That can’t be right.” “Exactly. I knew something was wrong.” “Give me that.” She took the bamboo slip from the manager and began to read. The deeper her frown grew, the clearer it seemed that the arithmetic had been badly botched. *Knew it.* At last, Wolhwa finished reading the bamboo slip. A chill entered her voice. “Are you not doing your job properly?” “I-I’m sorry.” “Do you have any idea who these gentlemen are? How dare you pull this kind of stunt? Write down the correct prices.” Hyuk Mujin whispered to me. “What a relief.” “Yeah. We almost had to wash dishes before leaving.” “Why do we have to suffer because of the Second Young Master?” “Don’t even mention that man. Just hearing about him gives me cancer.” “What’s cancer?” “……Something bad.” Meanwhile, the manager revised the prices, sweating profusely. Then he bowed deeply and apologized to us. “I’m sorry. I acted thoughtlessly and committed a grave discourtesy.” Hyuk Mujin accepted the apology with an arrogant air. “Don’t do that again. You have to know who you’re dealing with before pulling a prank. So how much is it?” “One hundred and five silver nyang and twenty-three iron coins.” “……?” “……?” *What the hell? Is this a dream?* My head turned toward Wolhwa of its own accord. “What is that supposed to mean?” “He arbitrarily lowered the prices because you were my acquaintances. How dare he look down on the young masters of the great Jin Family of Taiyuan? Apologize again.” “I’m sorry for failing to recognize your identities!” “But…” I asked in a thoroughly choked voice. “We can put it on credit, right? Of course.” “No, you can’t. Of course not. We haven’t allowed that even once in the past two years.” “How about making an exception and setting a precedent this time?” “I don’t have any plans to do that yet. You’ll have to aim for the next opportunity.” Wolhwa added with a radiant smile, “Was there something else you wanted to say?” “……M-Mount Heng.” “What was that?” I squeezed my eyes shut and continued. “Would you like to come with us to the Mount Heng Sword Sect?” “Wow, I’d love to.” *That hateful smile.* At Wolhwa’s gesture, the manager snatched up the bamboo slip and vanished at the speed of light. “We won’t have to worry about travel expenses anymore.” While Hyuk Mujin was the sort of person who simply accepted reality, someone else was shouting vehement opposition. “Nonsense! How can you bring a woman along while carrying out a family mission?” “Then stay here and wash dishes.” “……” “Who here cut down the old pine trees? Raise your hand.” Jin Mukyung didn’t raise his hand. Wolhwa slightly lifted the hem of her skirt and greeted him. “Please take good care of me, Young Hero Jin.”

## Korean source

```text
＃107화



사두마차는 목적지를 향해 부드럽게 이동했다. 어제와 같은 말, 같은 마차임에도 승차감은 차원이 달랐다. 마부가 교체되었기 때문이다.

겨우 마부석을 벗어나 내 옆자리에 앉은 혁무진이 속 편한 얼굴로 말했다.

“역시 사람은 각자 타고나는 게 있나 봐요. 전 마차 모는 건 영 젬병이라.”

젬병 같은 소리 하네.

하오문 산서지부장인 월화가 데려온 사람이다. 당연히 평범한 마부일 리가 없다.

묵묵하게 말고삐를 잡고 있는 그는 50레벨의 일류 무인이었다. 마부 겸 호위무사, 딱 그림이 나온다.

“무진아.”

“네?”

“제발 조용히 좀 가자. 그럼 중간이라도 간다.”

“……맨날 나만 갖고 뭐라 하셔.”

“네가 맨날 헛소리만 하니까 그렇지, 인마.”

맞은편에 앉아 우리를 지켜보던 월화가 실소를 흘렸다.

“두 사람, 격의 없는 모습이 보기 좋네요.”

“저놈이 싸가지가 없는 겁니다.”

“싸가지라뇨. 이런 말까지는 안 하려고 했는데, 제가 조장보다 두 살이나 더 많습니다. 제 친구들은 애도 있어요.”

“넌 없잖아.”

“아니, 뭐. 그렇긴 한데요.”

“그리고 네가 스물둘이어도 나보다 어려. 아무튼, 어려.”

“그게 무슨 소립니까. 조장님이 이제 겨우 약관인 건 산서성 똥개들도 다 아는 사실인데.”

“못 믿겠으면 한판 붙든가.”

“……다른 분들도 계시니까 여기까지만 하겠습니다.”

혁무진의 추한 변명에 월화가 활짝 웃었다.

“어머, 난 괜찮은데? 여기 진 소협은 어떨지 모르겠지만.”

자연스럽게 모두의 시선이 한 사람을 향해 쏠린다.

아까부터 입을 꾹 다물고 있던 진무경이 움찔하더니 입을 열었다.

“나, 난 상관없소.”

“……?”

뭐야, 저놈 지금 말 더듬은 거야?

예상치 못한 반응에 눈을 동그랗게 뜨고 바라보자 진무경이 슬쩍 시선을 회피했다.

‘어어, 점점.’

원래 저런 캐릭터가 아닌데. 평소 같았으면 뭘 쳐다보냐고 눈을 부라릴 녀석인데.

나는 진심을 담아 물었다.

“어디 아파?”

“……전혀.”

“대화할 때는 사람 눈을 보고 해야지.”

“……시끄럽다. 말 걸지 마.”

오늘따라 참 요상하네, 진짜.

절정 고수씩이나 되는 인간이 마차 멀미에 걸렸을 리는 없고.

아침까지만 해도 팔팔하더니 어째 상태가 영 아니다.

‘그러고 보니까 마차 타고 나서부터 저렇게 된 것 같은데.’

눈을 가늘게 뜨고 진무경을 바라보던 그때.

쿡쿡.

슬쩍 옆구리를 찌른 혁무진이 내게만 들릴 정도로 작은 목소리로 속삭였다.

“이공자님 좀 보세요.”

“뭐가…… 아.”

혁무진의 말을 들은 후에야 이상한 광경이 눈에 띄었다.

어떻게 지금까지 눈치채지 못했나 싶을 정도다.

‘뭐지?’

태원진가에서 가져온 사두마차는 상당히 호화롭다. 어지간한 방 하나 크기라 좌석도 넓었다. 지금 인원의 두 배를 태워도 무리가 없을 정도다.

그런데…….

‘쟤는 왜 저러고 있어.’

현재 진무경은 넓은 좌석을 두고 마차 끄트머리 구석에 몸을 구겨 넣고 있었다. 아니, 저 정도면 거의 압축 수준이다.

‘9와 4분의 3 승강장이야, 뭐야.’

천무학관이 아니라 마법 학교를 다니고 있는 건가.

한편 저 괴상한 짓거리를 지켜보고 있는 것은 나와 혁무진만이 아니었다.

“진 소협. 많이 불편해 보이는데 이쪽으로 좀 오세요. 자리 많이 남아요.”

월화의 고혹적인 목소리에 덜컥 굳는 진무경의 신형.

삐걱거리는 대답이 흘러나온 건 잠시 후였다.

“괘, 괜찮소.”

“…….”

하나도 안 괜찮아 보이는데. 나와 비슷한 표정을 짓고 있는 혁무진에게 조용히 속삭였다.

“네가 봐도 이상하지?”

“이상한 정도가 아닌데요.”

“그래, 나도 비슷한 생각이야.”

우리는 의미심장한 눈빛을 주고받았다.

“세상에, 누가 상상이나 했겠습니까.”

“그러게. 천하의 진천검이 저렇게 낯가림이 심할 줄이야.”

“제 말이 그 말…… 예?”

“반응이 왜 그래? 사람 성격 가지고 뭐라 하면 안 돼. 나처럼 낯짝 두꺼운 놈이 있으면 소심한 사람도 있는 거야.”

“아니, 잠시만. 잠시만요.”

혁무진이 더듬거리며 말을 이었다.

“지금 무슨 말씀을 하시는 거예요?”

“그야 당연히 진무경…….”

으스스한 목소리가 불쑥 끼어들었다.

“입 다물어.”

아무리 넓어 봤자 마차 안이니 다 들린다. 진무경의 찢어 죽일 듯한 눈빛에 나와 혁무진이 동시에 입을 다물었다.

살벌한 분위기를 환기시킨 건 월화였다.

“내 정신 좀 봐, 아직 정식으로 인사드린 적이 없네요. 하오문 산서지부장 월화라고 합니다.”

“……태원진가의 진무경이오.”

“반응이 영 심심하네요. 저기 진 공자는 처음 제 신분을 듣고 엄청나게 놀랐는데.”

“저 녀석에게 대충 들어서 알고는 있었소. 본가를 위해 큰일을 해 주셨다는 이야기도.”

진무경이 정중하게 포권을 취했다.

“늦었지만 감사를 표하오.”

“별말씀을. 정당한 거래였어요.”

월화가 매끄럽게 한 마디를 덧붙였다.

“아직 적절한 보상은 못 받았지만요.”

“본가는 하오문의 호의를 잊지 않을 거요.”

아직도 어색하기 짝이 없는 행동과 말투지만 그래도 처음보다는 썩 나아진 모습이다.

미남과 미녀의 그림 같은 투샷에 혁무진이 감탄사를 토했다.

“촉망받는 젊은 고수와 절세의 미녀라…… 크으, 보기만 해도 가슴이 뛰는군요. 안 그렇습니까?”

나는 못 들은 척 고개를 돌렸다.

피부가 따끔거릴 정도로 살기 어린 시선을 보아하니, 혁무진의 가슴이 뛸 시간은 얼마 남지 않은 게 분명했다.



* * *



겨울의 낮은 성미가 급하다.

산길을 따라 얼마나 이동했을까, 금세 해가 지고 어둠이 찾아왔다. 마차가 멈춘 것은 그로부터 두 시진이 지난 후, 자정 무렵이었다.

“도착했습니다.”

마차에서 내리자마자 보이는 것은 적당한 크기의 목제 건물이었다.

안으로 발을 내딛자마자 느껴지는 싸늘한 공기. 사람을 본뜬 동상은 위엄 있게 우리를 내려다보고 있었다. 이런 곳을 뭐라고 하더라?

‘아, 그래. 사당(祠堂).’

죽은 이의 위패를 모시고 제사를 지내는 장소라고 들었다.

무협 소설에서 심심하면 등장하는 관제묘(關帝廟)가 떠올라 동상을 살펴봤지만 누군지는 알 수 없었다.

“수년 전 기근 이후로 버려진 사당인데, 지금도 간혹 인근 양민들이 오는 모양이에요.”

월화의 말처럼 사당 내부는 휑했지만 아직 사람의 흔적이 남아 있었다. 이를테면 먼지 쌓인 바닥 위로 찍혀 있는 사람의 발자국이라든가.

“자리를 준비하겠습니다.”

하오문도로 짐작되는 마부 겸 호위무사의 말에 우리는 사당 밖으로 나왔다. 아니, 정확히 말하면 한 명은 누군가에 의해 끌려 나왔다고 해야 맞겠다.

“따라와라.”

“으헉, 조장님, 조장님!”

진무경에게 멱살을 잡힌 채 질질 끌려가는 혁무진을 외면하고 하늘을 바라봤다. 음, 오늘은 달이 참 밝구나.

“뭐 해요?”

“뭐, 보시는 대로죠.”

월화가 싱긋 웃었다.

“경치 구경하는 거 좋아하나 봐요?”

“요즘 들어서 좋아지고 있어요.”

현대에서 볼 수 있는 경치라고 해 봐야 높은 곳에서 내려다보이는 야경이다. 그마저도 직장인들의 야근이 만들어 낸 슬픈 불빛들이고.

‘이런 게 진짜 경치지.’

빽빽한 빌딩 숲도, 아파트 단지와 공장 부지도 없다.

아스팔트 도로 대신 축축한 흙길과 청량한 공기가 온 세상에 가득하다.

‘이런 곳에서 살면 힐링 제대로 될 텐데.’

문제는 킬링 당하기도 쉬운 동네라는 거다. 어떻게 된 게 여기는 몬스터보다 사람이 더 무섭다.

굳이 대장로나 조필까지 갈 필요도 없이, 바로 어제 봉황객잔에서 있었던 일만 해도 그렇다.

“아, 맞다. 그놈들은 어떻게 됐어요?”

“적풍단(赤風團)의 마적들을 말하는 거라면 구금해 뒀어요. 물론 그 전에 의원을 불러야 했죠.”

그 정도로 개박살을 내 줬으니 치료가 필요하긴 했을 거다.

그러나 그보다 관심을 끄는 단어가 있었다.

“적풍단이요?”

“고원에서 떠오르는 신흥 강자예요. 규모도 제법 크고, 무엇보다 우두머리인 적풍단주의 무공이 고강하다고 알려져 있어요.”

북부 고원. 항산검문과의 전쟁 당시 지도를 통해 처음으로 알게 된 지명이다.

한 가지 의아한 점은, 봉황객잔이 있는 혼주와 고원의 거리가 상당하다는 것이었다. 밤낮으로 말을 달려도 일주일 이상이 소요되는 걸로 알고 있는데…….

“그런 놈들이 어떻게 여기까지 흘러들어온 겁니까?”

“이천백은 전쟁 말미에 수많은 낭인과 마적단들을 고용했어요. 그중 상당수는 팔천협에서 뼈를 묻었지만, 일부는 살아남아 도망쳤죠.”

“그중에 적풍단이 있었다?”

월화가 고개를 저었다.

“적풍단주…… 생각 이상으로 머리 회전이 빠른 자더군요.”

“그럼?”

“그는 마지막까지 사태를 지켜봤어요. 불과 두 시진 떨어진 거리에서 팔천협을 예의 주시하다가 전투 결과를 듣고 말 머리를 돌렸죠. 자신을 따르는 이백 명의 수하와 함께.”

자그마치 이백 명.

만약 그날 팔천협에서 적풍단이 가세했다면 어떻게 되었을까? 엄청난 사상자가 나오는 건 물론이고 전투의 승패에도 영향을 끼쳤을지도 모른다.

“우리로서는 행운이었네요.”

“그렇죠. 항산검문 입장에서는 엄청난 불운이었고.”

월화가 곰방대에 담뱃잎을 꾹꾹 눌러 담으며 말을 이었다.

“적풍단은 그 길로 북상했어요. 대부분의 병력이 빠져나간 항산검문의 본진을 노린 거죠.”

“……허.”

그야말로 타고난 약탈자다.

전쟁의 승기가 한쪽으로 기울자마자 북상, 대부분의 주력이 빠져나간 항산검문의 목덜미를 물어뜯은 것이다.

전투에 참여하지 않은 덕분에 병력을 보존한 건 물론이고 충분한 휴식도 취했을 테니, 컨디션은 최상이었겠지.

“결과는 진 공자도 들어서 알죠?”

“네.”

이틀 동안 이어진 치열한 전투는 결국 항산검문의 승리로 막을 내렸다. 아버지를 뒤를 이어야 할 소문주의 죽음을 남기고.

“그런데 제가 들은 소문으로는 낭인과 마적들이 섞여 있었다고 하던데요.”

“호랑이가 이빨이 빠졌다고 해서 개라고 부르진 않는 법. 적풍단주가 끌어들인 낭인들도 제법 되죠. 방패막이로 사용하기에는 딱 좋았을 테니까.”

탁, 탁.

화섭자를 꺼내 불을 붙인 그녀가 곰방대를 빨아들였다.

“진 공자가 쓰러트린 마적들은 아마도 그때 도망친 자들일 거예요. 적풍단이 마적단치고 제법 규율이 강하긴 해도 탈영병이 아예 없진 않으니까. 혼주에서 뭘 하고 있었는지는 잘 모르겠지만요.”

“탈영병이라…….”

“그것 때문에 근래 들어 이 근방이 어수선해요. 낭인, 산적, 마적, 심지어는 흑도들까지 슬쩍 고개를 들고 있는데 항산검문의 힘은 형편없이 줄어들었으니까.”

“우리의 제안을 받아들일 수밖에 없겠네요.”

월화가 새치름하게 웃어 보였다.

“정확히 말하면 우리, 가 아니라 태원진가겠죠? 뭐, 내 입장에서도 신임 문주를 핍박하기 좋은 때라는 건 맞지만.”

“저기, 그런데요.”

“응?”

“이런 날씨에도 사당에 오는 양민들이 있습니까?”

“그럴 리가요. 사냥꾼들이라면 몰라도. 그런데 갑자기 그건 왜?”

나는 산길을 가리켰다. 어느새 휘날리기 시작한 엷은 눈보라 사이로, 이쪽을 향해 올라오는 횃불들이 보였다.
```

## Current accepted English baseline

```markdown
# Chapter 107

The four-horse carriage moved smoothly toward its destination. Even though it was the same carriage pulled by the same horses as yesterday, the ride was on an entirely different level.

The driver had been replaced.

Hyuk Mujin, who had finally escaped the driver’s seat and settled beside me, said with a relaxed expression,

“People really must be born with different talents. I’m hopeless at driving a carriage.”

*What a load of crap.*

He was someone Wolhwa, the Lower District Sect’s Shanxi Branch Leader, had brought with her. Naturally, there was no way he was an ordinary coachman.

The man quietly holding the reins was a Level 50 First Rate martial artist. A coachman and a bodyguard. The picture fit perfectly.

“Mujin.”

“Yes?”

“Please just travel quietly. Then you’ll at least do okay.”

“……Why am I always the one you pick on?”

“Because you’re always spouting nonsense, you idiot.”

Wolhwa, who was sitting across from us and watching, let out a quiet laugh.

“You two seem very comfortable with each other.”

“He’s just rude.”

“Rude? I wasn’t going to say this, but I’m two years older than the squad leader. My friends have children.”

“You don’t.”

“Well, no. That’s true.”

“And even if you were twenty-two, you’d still be younger than me. Anyway, you’re younger.”

“What are you talking about? Even the stray dogs of Shanxi Province know that the squad leader is barely twenty.”

“If you don’t believe me, then let’s have a match.”

“……Since there are other people here, I’ll stop at this point.”

Wolhwa smiled brightly at Hyuk Mujin’s ugly excuse.

“Oh, I don’t mind. Though I can’t speak for Young Hero Jin.”

Everyone’s eyes naturally turned toward one person.

Jin Mukyung, who had kept his mouth tightly shut until then, flinched and opened it.

“I—I don’t mind.”

“……?”

*What the hell? Did he just stutter?*

I stared at him with my eyes wide open at the unexpected response. Jin Mukyung subtly looked away.

*Oh, this is getting worse.*

He wasn’t usually like this. Normally, he would have glared and asked what I was staring at.

I asked him sincerely,

“Are you sick?”

“……Not at all.”

“When you’re talking to someone, you should look them in the eye.”

“……Be quiet. Don’t talk to me.”

He was acting really strange today.

There was no way a Peak master like him had gotten motion sickness.

He had been full of energy until this morning, but now he was clearly not himself.

*Come to think of it, he seems to have been like this ever since we got into the carriage.*

Just as I was narrowing my eyes and watching Jin Mukyung—

*Poke, poke.*

Hyuk Mujin nudged me in the side and whispered so quietly that only I could hear him.

“Look at the Second Young Master.”

“Look at what…… Ah.”

Only after hearing Hyuk Mujin did I notice the bizarre sight.

I couldn’t believe I hadn’t noticed it until now.

*What is he doing?*

The four-horse carriage brought from the Jin Family of Taiyuan was quite luxurious. The inside was about the size of an ordinary room, and the seats were spacious too. It could have carried twice as many people as we had without any trouble.

And yet…

*Why is he sitting like that?*

Jin Mukyung had ignored the spacious seats and folded himself into the corner at the very end of the carriage.

No, “folded” didn’t quite cover it. He was practically compressed.

*What is this, Platform Nine and Three-Quarters?*

Was he attending a magic school instead of Heaven’s Gate Temple?

I wasn’t the only one watching this strange behavior.

“Young Hero Jin, you look very uncomfortable. Why don’t you come over here? There’s plenty of room.”

Jin Mukyung’s body went rigid at the sound of Wolhwa’s alluring voice.

A creaking reply came a moment later.

“I—I’m fine.”

“……”

He didn’t look fine at all.

I whispered quietly to Hyuk Mujin, whose expression was similar to mine.

“You think he’s acting strange too, right?”

“It’s more than strange.”

“Yeah. I thought so too.”

We exchanged meaningful glances.

“My goodness. Who could have imagined this?”

“Exactly. Who knew the Heaven Shaking Sword was so shy around people?”

“That’s exactly what I mean…… Huh?”

“Why are you reacting like that? You shouldn’t criticize someone’s personality. If there are thick-skinned guys like me, then there can be timid people too.”

“No, wait. Just wait a moment.”

Hyuk Mujin stumbled over his words.

“What exactly are you talking about?”

“Obviously, Jin Mukyung……”

An eerie voice suddenly cut in.

“Shut up.”

No matter how spacious the carriage was, everyone inside could hear everything.

Under Jin Mukyung’s murderous glare, Hyuk Mujin and I shut our mouths at the same time.

Wolhwa was the one who changed the grim atmosphere.

“Where are my manners? I haven’t even properly introduced myself yet. I’m Wolhwa, Shanxi Branch Leader of the Lower District Sect.”

“……I am Jin Mukyung of the Jin Family of Taiyuan.”

“What a dull reaction. That Young Master Jin over there was extremely surprised when he first heard about my identity.”

“I heard the general details from him. I also heard that you did a great deal for our family.”

Jin Mukyung politely clasped his hands.

“I realize this is late, but allow me to express my thanks.”

“Not at all. It was a fair trade.”

Wolhwa smoothly added,

“Though I haven’t received the proper compensation yet.”

“Our family will not forget the Lower District Sect’s goodwill.”

His behavior and speech were still awkward beyond belief, but he was doing much better than when they had first met.

Looking at the handsome man and beautiful woman sitting together like a picture, Hyuk Mujin exclaimed,

“A promising young martial arts master and a peerless beauty… Whew, just looking at them makes my heart race. Don’t you agree?”

I turned my head away and pretended not to hear him.

Judging by the killing intent prickling my skin, Hyuk Mujin’s heart wouldn’t be racing for much longer.

* * *

Winter days were short-tempered.

How long had we traveled along the mountain road? The sun quickly set, and darkness descended. The carriage stopped four hours later, around midnight.

“We’ve arrived.”

The first thing I saw after stepping out of the carriage was a moderately sized wooden building.

The moment I stepped inside, I felt a chill in the air. A statue shaped in the likeness of a person looked down at us with solemn dignity.

*What did they call places like this again?*

*Oh, right. A shrine.*

I had heard that it was a place where the spirit tablets of the dead were kept and memorial rites were performed.

The Guandi Temples that appeared so often in martial arts novels came to mind. I looked closely at the statue, but I couldn’t tell who it represented.

“It’s a shrine that was abandoned after a famine several years ago, though it seems local commoners still come here from time to time.”

Just as Wolhwa had said, the inside of the shrine was empty, but traces of human presence remained. For example, there were footprints pressed into the dust-covered floor.

“I’ll prepare the place.”

At the words of the coachman and bodyguard, whom I assumed was a member of the Lower District Sect, we went outside the shrine.

More precisely, one of us was dragged out by someone.

“Follow me.”

“Gah! Squad Leader! Squad Leader!”

I ignored Hyuk Mujin as Jin Mukyung dragged him away by the collar and looked up at the sky.

*The moon is awfully bright tonight.*

“What are you doing?”

“As you can see.”

Wolhwa smiled faintly.

“You seem to enjoy looking at the scenery.”

“I’ve been starting to enjoy it lately.”

The only scenery available in the modern world was a night view seen from some high place. Even that consisted of sad lights created by office workers working overtime.

*This is real scenery.*

There were no dense forests of skyscrapers, no apartment complexes, and no factories.

In place of asphalt roads, damp dirt paths and crisp air filled the entire world.

*Living in a place like this would be genuinely healing.*

The problem was that it was also an easy place to get killed.

Somehow, people were more frightening here than monsters.

I didn’t even need to go as far as the Head Elder or Jopil. What had happened at the Phoenix Inn just yesterday was enough.

“Oh, right. What happened to those guys?”

“If you mean the mounted bandits from the Red Wind Band, they’ve been detained. Of course, we had to call a physician first.”

I’d beaten the shit out of them, so of course they’d needed treatment.

But there was another word that caught my attention more than that.

“The Red Wind Band?”

“They’re a rising power from the plateau. They’re fairly large, and more than anything, the leader of the Red Wind Band is said to possess formidable martial arts.”

The Northern Plateau.

I had first learned of that place through the map during the war with the Mount Heng Sword Sect.

One thing struck me as strange: the plateau was a considerable distance from Honju, where the Phoenix Inn was located. As far as I knew, it took more than a week even if one rode day and night.

“How did people like that end up all the way here?”

“Toward the end of the war, Lee Cheonbaek hired countless wandering martial artists and mounted-bandit groups. Many of them met their end at Eight Spring Gorge, but some survived and fled.”

“So the Red Wind Band was among them?”

Wolhwa shook her head.

“The leader of the Red Wind Band…… He was quicker-witted than I expected.”

“What do you mean?”

“He watched the situation until the very end. He kept a close eye on Eight Spring Gorge from only four hours away, then turned his horse around when he heard the outcome of the battle.”

“With the two hundred subordinates who followed him.”

Two hundred people.

What would have happened if the Red Wind Band had joined the battle at Eight Spring Gorge that day? There would have been an enormous number of casualties, and it might even have affected the outcome of the battle.

“We were lucky.”

“We were. For the Mount Heng Sword Sect, it was incredibly unlucky.”

Wolhwa continued as she packed tobacco into her long-stemmed pipe.

“The Red Wind Band headed north immediately. They targeted the Mount Heng Sword Sect’s main base after most of its forces had withdrawn.”

“……Huh.”

They were natural-born plunderers.

The moment the tide of the war turned, they headed north and bit into the throat of the Mount Heng Sword Sect, whose main forces had already withdrawn.

They had preserved their forces by not participating in the battle, and they must have gotten plenty of rest as well. Their condition would have been at its peak.

“Young Master Jin, you heard what happened, didn’t you?”

“Yes.”

The fierce battle that continued for two days ended with the Mount Heng Sword Sect’s victory.

It also left behind the death of the Young Sect Leader, who was supposed to succeed his father.

“But the rumors I heard said that wandering martial artists and mounted bandits were mixed together.”

“A tiger doesn’t become a dog just because it has lost its teeth. The wandering martial artists the leader of the Red Wind Band drew in were fairly numerous as well. They would have been perfect for use as shields.”

*Tap, tap.*

Wolhwa took out a fire starter, lit it, and drew on her long-stemmed pipe.

“The mounted bandits Young Master Jin defeated were probably the ones who fled at that time. Even if the Red Wind Band is unusually disciplined for a mounted-bandit group, it doesn’t mean they have no deserters at all. I’m not sure what they were doing in Honju, though.”

“Deserters……”

“That’s why things have been chaotic around here lately. Wandering martial artists, bandits, mounted bandits, and even dark-path figures are starting to raise their heads, while the Mount Heng Sword Sect’s strength has been reduced to almost nothing.”

“They’ll have no choice but to accept our proposal.”

Wolhwa smiled demurely.

“To be precise, it isn’t *our* proposal. It’s the Jin Family of Taiyuan’s, isn’t it? Still, from my perspective, this is indeed a good time to pressure the new Sect Leader.”

“By the way……”

“Yes?”

“Do commoners really come to this shrine in weather like this?”

“Of course not. Hunters, perhaps. Why do you ask all of a sudden?”

I pointed toward the mountain path.

Through the thin snowstorm that had begun to swirl, I could see torches climbing toward us.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 107`.

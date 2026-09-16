# Master Edit Task — Chapter 108

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
| 월화     | **Wolhwa**         |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 마적     | **mounted bandits**                              |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 은인     | **Benefactor**                               |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 은자 | **silver nyang** | Silver currency unit. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
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

#### Chapter 106 tail (verified mastered)

…
earlier. Don’t ask about him anymore, and don’t try to learn anything else. Issue a gag order and make sure no one even mentions this.” “Yes, Branch Leader. I’ll make sure they understand.” “Oh, and one more thing. I’ll be leaving early tomorrow, so make the preparations.” “Who are you planning to take with you?” “No one. I’ll go alone.” “Branch Leader, that…” “It’s an order.” “Understood.” Once her subordinate withdrew, silence settled over the guest room. Wolhwa tapped the blackened tobacco leaves from her pipe and thought. *Jin Taekyung.* If everything he had done until now was true, then the northern interests she needed to extract from the Mount Heng Sword Sect were nothing. *Has anyone in all history ever grown this quickly?* Her gaze darkened as she stared at the place where Jin Taekyung had been sitting. * * * The next morning. I began to feel that something had gone wrong after meeting the person in charge of the private residence. “The lodging fee is twenty-five nyang, the food comes to five nyang, and the property damage fee is fifty nyang. The total is eighty silver nyang.” Hyuk Mujin, who had been celebrating yesterday after emptying those mounted bandits’ pockets, gaped. “Property damage? Fifty silver nyang?” “When I went to the rear courtyard, I found that five old pine trees had fallen.” They were the trees Wolhwa had said were expensive. Hyuk Mujin and I turned our heads at the same time. Jin Mukyung, whose eyes met ours, flinched before opening his mouth. “I got carried away while practicing my swordsmanship.” “……No, fuck. If you get carried away, does that mean you can cut down anything in your way? Huh?” “Hoooo.” Hyuk Mujin couldn’t say anything. He merely let out one furious sigh after another. One look told me the bill exceeded the money we had left. If it had only been a little over, maybe we could have talked it out and found some middle ground… “Mujin, how much do you have right now?” “Forty nyang.” *Middle ground, my ass. We’re nowhere close.* “Could we put it on credit?” That was the exact moment the kind smile around the private-residence manager’s lips disappeared. “Young Master Jin, what are you doing here?” A beautiful woman in a light, flowing palace-style dress was approaching us. Right now, Wolhwa’s appearance was nothing short of a lifeline. I felt bad about turning down her proposal so decisively the night before, but this was no time to be picky. “Well, you see…” When I explained the situation, Wolhwa’s eyes grew round. “Eighty nyang? That can’t be right.” “Exactly. I knew something was wrong.” “Give me that.” She took the bamboo slip from the manager and began to read. The deeper her frown grew, the clearer it seemed that the arithmetic had been badly botched. *Knew it.* At last, Wolhwa finished reading the bamboo slip. A chill entered her voice. “Are you not doing your job properly?” “I-I’m sorry.” “Do you have any idea who these gentlemen are? How dare you pull this kind of stunt? Write down the correct prices.” Hyuk Mujin whispered to me. “What a relief.” “Yeah. We almost had to wash dishes before leaving.” “Why do we have to suffer because of the Second Young Master?” “Don’t even mention that man. Just hearing about him gives me cancer.” “What’s cancer?” “……Something bad.” Meanwhile, the manager revised the prices, sweating profusely. Then he bowed deeply and apologized to us. “I’m sorry. I acted thoughtlessly and committed a grave discourtesy.” Hyuk Mujin accepted the apology with an arrogant air. “Don’t do that again. You have to know who you’re dealing with before pulling a prank. So how much is it?” “One hundred and five silver nyang and twenty-three iron coins.” “……?” “……?” *What the hell? Is this a dream?* My head turned toward Wolhwa of its own accord. “What is that supposed to mean?” “He arbitrarily lowered the prices because you were my acquaintances. How dare he look down on the young masters of the great Jin Family of Taiyuan? Apologize again.” “I’m sorry for failing to recognize your identities!” “But…” I asked in a thoroughly choked voice. “We can put it on credit, right? Of course.” “No, you can’t. Of course not. We haven’t allowed that even once in the past two years.” “How about making an exception and setting a precedent this time?” “I don’t have any plans to do that yet. You’ll have to aim for the next opportunity.” Wolhwa added with a radiant smile, “Was there something else you wanted to say?” “……M-Mount Heng.” “What was that?” I squeezed my eyes shut and continued. “Would you like to come with us to the Mount Heng Sword Sect?” “Wow, I’d love to.” *That hateful smile.* At Wolhwa’s gesture, the manager snatched up the bamboo slip and vanished at the speed of light. “We won’t have to worry about travel expenses anymore.” While Hyuk Mujin was the sort of person who simply accepted reality, someone else was shouting vehement opposition. “Nonsense! How can you bring a woman along while carrying out a family mission?” “Then stay here and wash dishes.” “……” “Who here cut down the old pine trees? Raise your hand.” Jin Mukyung didn’t raise his hand. Wolhwa slightly lifted the hem of her skirt and greeted him. “Please take good care of me, Young Hero Jin.”

#### Chapter 107 tail (verified mastered)

…
At the words of the coachman and bodyguard, whom I assumed to be a member of the Lower District Sect, we headed outside. More precisely, one of us was dragged out by someone. “Follow me.” “Gah! Captain! Captain!” I ignored Hyuk Mujin as Jin Mukyung dragged him away by the collar and looked up at the sky. *Hmm. The moon sure is bright tonight.* “What are you doing?” “As you can see.” Wolhwa smiled faintly. “You seem to enjoy looking at the scenery.” “I’ve been getting into it lately.” The only scenery to be found in the modern world was the nightscape seen from some high vantage point. Even that consisted of sad lights created by office workers working overtime. *Now this is real scenery.* There were no dense forests of skyscrapers, apartment complexes, or industrial sites. In place of asphalt roads, damp dirt paths and crisp air filled the entire world. *Living in a place like this would be genuinely healing.* The problem was that it was also an easy place to get killed. Somehow, people were more frightening here than monsters. I didn’t even need to go as far as the Head Elder or Jopil. What had happened at the Phoenix Inn just yesterday was enough. “Oh, right. What happened to those guys?” “If you mean the mounted bandits from the Red Wind Band, they’ve been detained. Of course, we had to call a physician first.” I’d beaten the shit out of them, so of course they’d needed treatment. But there was another word that caught my attention more than that. “The Red Wind Band?” They’re a rising power from Gaoyuan. They’re fairly large, and more than anything, the Red Wind Band Leader is said to possess formidable martial arts. Northern Gaoyuan. I had first learned of that place from a map during the war with the Mount Heng Sword Sect. One thing puzzled me. Gaoyuan was a considerable distance from Honju, where the Phoenix Inn was located. As far as I knew, the journey took more than a week even if you rode day and night. “How did people like that end up all the way here?” “Toward the end of the war, Lee Cheonbaek hired countless wandering martial artists and mounted-bandit groups. Many of them met their end at Eight Spring Gorge, but some survived and fled.” “So the Red Wind Band was among them?” Wolhwa shook her head. “The Red Wind Band Leader… He was quicker-witted than I expected.” “Then what happened?” “He watched the situation until the very end. He kept a close eye on Eight Spring Gorge from only two shichen away, then turned his horse around the moment he heard how the battle had ended—along with the two hundred men under his command.” Two hundred people. What would have happened if the Red Wind Band had joined the battle at Eight Spring Gorge that day? There would have been an enormous number of casualties, and it might even have affected the outcome of the battle. “We were lucky.” “We were. For the Mount Heng Sword Sect, it was incredibly unlucky.” Wolhwa continued as she firmly packed tobacco leaves into her long-stemmed pipe. “The Red Wind Band headed north immediately. They targeted the Mount Heng Sword Sect’s main base after most of its forces had withdrawn.” “……Huh.” They were natural-born plunderers. The moment the tide of the war turned, they headed north and sank their teeth into the Mount Heng Sword Sect’s throat while most of its main force was away. They had preserved their forces by staying out of the battle, and they must have been well-rested too. They would have been in peak condition. “Young Master Jin, you heard how it ended, didn’t you?” “Yes.” After two days of fierce fighting, the Mount Heng Sword Sect ultimately emerged victorious—but at the cost of the Young Sect Leader, who was supposed to succeed his father. “But the rumors I heard said that wandering martial artists and mounted bandits were mixed together.” “A tiger doesn’t become a dog just because it has lost its teeth. The Red Wind Band Leader had recruited quite a few wandering martial artists as well. They would have made excellent shields.” *Tap, tap.* Wolhwa took out a fire starter, lit it, and drew on her long-stemmed pipe. “The mounted bandits Young Master Jin defeated were probably the ones who fled at that time. Even if the Red Wind Band is unusually disciplined for a mounted-bandit group, it doesn’t mean they have no deserters at all. I’m not sure what they were doing in Honju, though.” “Deserters…” “That’s why the surrounding area has been so unsettled lately. Wandering martial artists, bandits, mounted bandits, even dark-path figures—they’re all starting to rear their heads now that the Mount Heng Sword Sect’s strength has been so badly diminished.” “They’ll have no choice but to accept our proposal.” Wolhwa gave me a prim smile. “Strictly speaking, it isn’t *our* proposal. It’s the Jin Family of Taiyuan’s, isn’t it? Still, from my perspective, this is certainly a good time to pressure the new Sect Leader.” “By the way…” “Yes?” “Do commoners really visit this shrine in weather like this?” “Of course not. Hunters, perhaps. Why do you ask all of a sudden?” I pointed toward the mountain path. Through the light snowstorm that had begun to swirl, I could see torches climbing toward us.

## Korean source

```text
＃108화



‘사냥꾼?’

월화의 짐작은 절반만 맞았다. 사냥꾼은 사냥꾼인데, 불청객들의 정체는 조금 더 특별하고 훨씬 더 악랄했다.

“빨리빨리 걸어라, 이놈들아.”

“사내라는 것들이 이렇게 비리비리해서 어디다 써?”

머릿수는 총 열 명. 하나같이 험상궂은 얼굴에, 병장기로 무장까지 했다. 그들의 선두에선 굴비처럼 밧줄로 묶인 포로들이 비틀거리고 있었다.

퍽, 퍽퍽!

“아이고, 대혀업!”

“갑니다, 가고 있으니까 제발 그만 좀…….”

“허, 그만? 이놈들이 아직도 정신이 덜 들었구나.”

“어허, 적당히 때려. 어디 한 군데 부러지기라도 하면 값 떨어진다. 가뜩이나 조그마한 놈들이라 제값도 못 받게 생겼구먼.”

“곡마단(曲馬團)에 팔아먹으면 그럭저럭 받겠지. 후딱 들어가서 화주나 한잔하자고.”

“아따, 생각만 해도 침이…… 근데 저건 뭐여?”

인간 사냥꾼들의 발걸음이 우뚝 멈췄다. 사당 앞에 세워져 있는 사두마차를 응시하던 눈동자들이 스르륵 옆으로 옮겨 간다.

그들의 시선 끝에 나와 월화가 있었다.

“……누구쇼?”

우두머리로 보이는 놈의 질문에 내가 나섰다.

“지나가던 과객.”

“과객이라. 요즘 같은 시기에 돌아다니면 위험한데.”

번들거리는 눈빛이 스스로가 위험한 놈이란 걸 말해 준다.

물론 그래 봤자 겨우 25레벨이라 내게는 위험 축에도 못 끼지만.

“이야, 사두마차에 기막힌 미녀까지. 있는 집 공자님이신가 봐?”

가까이 다가가서 확인했다면 마차에 새겨진 태원진가의 문장을 확인할 수 있었겠지만, 지금은 시커먼 밤이었고 놈은 뛰어난 안력(眼力)의 소유자가 아니었다.

“없는 집 자식은 아니지.”

“거참. 아까부터 말씀이 짧으시네.”

우두머리가 갈라진 입술을 핥았다. 슬슬 열이 오르는 모양이지만 아직은 나에 대한 경계를 풀지 않고 있다.

“뭐, 됐고. 이곳은 우리가 며칠 전부터 머무르던 곳인데…… 어쩌겠소?”

“뭘?”

“뭐긴, 약간의 성의를 보여 주면 자리를 내어 드릴 수 있다는 거지.”

“누가 들으면 이 사당이 그쪽 건 줄 알겠네.”

“버려진 곳이니 먼저 차지하는 사람이 임자 아닌가?”

“그럼 부동산 내용 증명서 떼 와.”

“뭐?”

우두머리가 어리둥절한 얼굴로 수하들을 돌아봤다. 생전 처음 듣는 용어일 테니 당연한 일이다. 하지만 아는 놈이 있을 리가 있나.

부동산 내용 증명서에 관해 수군거리는 놈들을 향해 쯧쯧 혀를 찼다.

“증명 못 하겠으면 곱게 돌아가라. 거기 잡아 둔 사람들은 풀어 주고.”

“……선을 넘는군. 호위무사라도 기다리나?”

“그런 거 없어.”

“그럼 뭘 믿고?”

“나.”

우두머리의 시선이 내 텅 빈 두 손을 향한다.

“병장기도 없이?”

“너희 정도야 주먹으로 충분하니까.”

“도련님이 어디서 한 수 배우긴 했나 본데…… 무림을 너무 우습게 보는 거 아닌가?”

“무림은 안 우습지. 그냥 너희가 우스운 거야.”

말과 함께 환하게 밝혀진 횃불을 향해 발을 내디딘 그 순간, 얌전히 잡혀 있던 포로들이 괴성을 내질렀다.

“어, 어어어?”

“으어어어! 대형! 대형!”

“이 자식들이 미쳤나. 다들 입 안 닥쳐!”

포로들의 격한 반응에 뒤에 선 놈들이 단검을 뽑아 목에 가져다 댔다. 우두머리가 경계심 어린 눈빛으로 나를 응시했다.

“아는 놈들인가?”

“아니, 태어나서 처음 보는데.”

반응이 너무 갑작스러워서 나까지 당황할 정도다. 그리고 갑자기 대형이라니?

“대혀어엉! 접니다! 저흽니다!”

“이놈들은 그쪽을 아는 것 같은데?”

“그거야 그냥 구해 달라고…… 어라?”

나는 포로들을 유심히 바라봤다. 어린애처럼 작은 키에 하나같이 못생긴 얼굴. 어디서 본 것 같기도 하다.

‘체형이 고블린을 닮아서 낯이 익은 건가?’

잠깐만. 고블린?

문득 오래전의 기억이 떠오른다. 아니, 사실 그리 오래된 기억도 아니다. 불과 몇 달 전 튜토리얼 퀘스트에서 있었던 일이니까.

“설마 그, 천력부랑 같이 있었던?”

포로들, 아니 천력부 장삼의 부하였던 오색귀(五色鬼)가 미친 듯이 고개를 끄덕였다.

“맞습니다, 저흽니다!”

“대형! 살려 주십시오!”

이놈들을 여기서 보게 될 줄이야. 황당해하는 내게 뒤에서 상황을 지켜보던 월화가 물었다.

“진 공자가 아는 사람들이에요?”

“일단은 구면이네요.”

인신매매범과 산적이라. 우열을 가릴 수 없는 조합이다.

방금까지는 구해 줄 생각이었는데 지금은 살짝 고민되네.

“대혀어어엉!”

“저흴 버리실 생각이십니까!”

“그날 이후 산적질도 그만두고 착하게 살았습니다!”

“…….”

눈치 하나는 귀신이다. 하긴, 천력부가 죽었을 때도 바로 항복해 버린 놈들이니 오죽할까.

“구해 줄 건가요?”

“쓰읍. 일단 구하긴 해야 할 것 같아요.”

그날 이후 새사람이 됐다는데 이대로 보내기에는 영 찝찝하다. 무엇보다 현직 인신매매범보다는 전직 산적이 훨씬 낫지.

그러자 우리의 대화를 들은 우두머리가 으르렁거리는 목소리로 끼어들었다.

“구해? 네놈이?”

“다 들어 놓고 뭘 또 물어봐. 너 인생 피곤하게 사는구나?”

“이 애새끼가 보자 보자 하니까…….”

차차창!

우두머리가 창을 겨누자 수하들도 무기를 빼 들었다. 월화가 짐짓 겁먹은 얼굴로 내 옆구리에 달라붙는다.

“어머, 무서워. 나 꼭 지켜 줘야 해요?”

보호 본능을 불러일으키는 촉촉한 눈망울. 간절한 표정.

월화의 실체를 아는 나로서는 기가 차는 광경이지만 놈들은 침을 꿀꺽 삼켰다.

“널 죽여야 하는 이유가 하나 더 늘었군.”

우두머리의 끈적끈적한 눈빛에 월화가 꺅, 비명을 질렀다.

“어떡해, 어떡해! 소녀, 너무 무서워요!”

“허허, 너무 겁먹지 말거라. 내 비록 일평생 거칠게 살았어도 마음만은 비단결처럼 고운 사내라는 걸 알게 될 테니. 잠시 후에 몸으로 대화를 나눠 보자꾸나.”

“어, 그전에 나 좀 보자.”

더러운 주둥이를 찢어 놔야 다시는 저딴 소리를 못 하지.

놈을 향해 성큼성큼 걸어가다가 문득 발걸음을 멈췄다. 그런 내 모습을 본 우두머리가 껄껄 웃었다.

“왜, 막상 싸우려니까 겁이 나나? 하지만 이미 늦었어.”

“그러게. 너, 진짜 큰일 났다.”

“……뭐?”

나는 어리둥절해하는 놈을 향해 활짝 웃어 주었다.

“좆 됐다고. 인마.”

말이 끝난 그 순간, 땅이 울림과 동시에 강력한 바람이 휘몰아쳤다.

쿵, 쐐애애액!

말 그대로 찰나에 불과한 시간.

무서운 속도로 나와 월화를 스쳐 간 그것은 어느새 우두머리의 앞에 서 있었다.

“다시 한번 말해 봐라.”

진무경. 그의 전신에서 뿜어져 나온 어마어마한 기파(氣波)가 장내를 짓눌렀다. 우두머리가 파랗게 질린 얼굴로 손을 덜덜 떨었다.

“요, 용서. 제발…….”

차가운 목소리가 대답했다.

“한참 늦었어.”



* * *



어쩌면 진무경은 우리 중 최고의 비폭력주의자일지도 모른다. 불과 십여 초 만에 이어질 모든 불필요한 싸움을 종결지었으니까.

“하, 항복, 항복하겠습니다.”

“제발 살려 주십시오. 제발 목숨만은…….”

공포에 질린 얼굴. 모두 다리가 풀려 자리에 주저앉았고, 누군가가 지린 소변은 언덕 아래로 흘렀다.

그건 오색귀도 마찬가지였다.

“시끄럽다.”

진무경이 얼굴에 묻은 피를 닦아 내며 툭 던진 한마디에 죽음 같은 침묵이 내리깔린다. 눈 한쪽이 시퍼렇게 멍든 혁무진이 내게 속삭였다.

“저 지금 살아 있는 거 맞습니까?”

“어, 귓가에 숨결 닿는 거 소름 돋으니까 좀 떨어져.”

“아까 전만 해도 이렇게 개처럼 맞을 수가 있나, 하는 생각이었는데 지금은…….”

꿀꺽, 마른침을 삼키는 혁무진의 시선은 쓰러진 우두머리를 향해 고정되어 있었다.

“흐윽, 흐으윽.”

사지가 부러지고 단전(丹田)이 파괴당한 그는 힘겹게 숨을 몰아쉬는 중이었다. 잘만 요양하면 다시 걸어 다닐 수는 있겠지만 무인으로서의 생명은 끝장이다.

기감으로 파악한 레벨창이 그 증거였다.



[Lv.2 이삼]



감시자들이 패밀리어로 쓰던 똥파리가 1레벨이었지, 아마.

한때 일류에 근접했던 25레벨의 무인을 산송장으로 만들어 버린 범인은 아까부터 계속 이쪽을 힐끗거리고 있다.

“조장님, 저 좀 살려 주세요. 이공자님께서 피가 부족하신가 봐요.”

“헛소리하지 말고 쟤나 좀 적당한 곳에 옮겨 놔. 저러다가 죽겠다.”

“죽어도 싼 놈 아닙니까? 멀쩡한 양민들 팔아먹던 놈들이잖아요.”

“그래도 옮겨. 아직 살아 있잖아.”

내가 무림과 현대를 오가며 느낀 가장 큰 괴리감 중 하나가 바로 살인(殺人)에 관한 문제였다.

27년간, 법과 질서가 존재하는 사회에서 살았던 나다.

날붙이로 적을 죽이는 법을 단련해 왔지만 그 대상은 몬스터였지, 살아 있는 인간이 아니었다.

‘분명히 그랬는데…….’

이제는 몇 명을 죽였는지 기억도 안 난다. 지금까지 내 손에 죽어 나간 적들이 NPC가 아닌 진짜 사람일지도 모른다는 걸 깨달았을 때도 큰 죄책감은 들지 않았다.

‘적이었으니까. 저들도 날 죽이려고 했으니까.’

헌터로 살아왔기 때문인지, 무림의 방식에 익숙해진 건지는 잘 모르겠다. 다만 무덤덤한 마음과 단순한 자기 합리화에 스스로 놀랐을 뿐.

‘지금은 이 정도로도 괜찮겠지.’

나는 전혀 다른 두 세계를 살아가는 중이다. 어설픈 불자(佛子) 흉내를 낼 정도로 여유로운 상황이 아니다.

들러붙는 생각을 떨쳐 내며 주저앉아 있는 놈들을 향해 다가갔다.

“히익!”

“흐아악, 살려 주십쇼, 대형!”

“이 자식들은 구해 주려고 해도 난리네. 가만히 있어 봐.”

밧줄을 풀어 주자 자유의 몸이 된 오색귀가 후들거리는 다리로 일어났다.

“가, 감사합니다.”

“평생 은인으로 모시겠습니다!”

“은인으로 모시긴 개뿔이. 그나저나 어쩌다가 이런 놈들한테 잡힌 거냐? 그것도 다섯 명이 한꺼번에.”

오색귀 놈들이 체구가 작긴 해도 명색이 성인 남자다. 천력부를 따라 산적질 할 정도의 수준은 된다.

“아니, 저 그게.”

“……?”

뭐지, 이놈들.

머뭇거리는 태도에 이상함을 감지한 나는 가장 가까이 있는 인신매매범의 멱살을 붙잡고 끌어올렸다.

“이놈들 어떻게 붙잡았어?”

“저, 저잣거리에서 저희 전낭을 슬쩍 하려던 걸 붙잡았습니다.”

“…….”

이런 십색귀들을 봤나. 산적 관두고 농사라도 짓나 했더니 직종을 바꾼 거였어?

“변명해 봐.”

날카로운 내 시선에 다섯 놈이 눈알을 뒤룩뒤룩 굴렸다.

“그, 그러니까.”

“대형, 저희 같은 놈들은 배운 게 그런 것뿐이라.”

“그, 그래도 시작한 지 얼마 안 됐습니다!”

“착실하게 일하려고 했는데 영 신통치가 않아서…… 딱 한탕만 치고 빠지자 했던 게 그만.”

“마적단 놈들인 줄 알았으면 건드리지도 않았죠. 저희도 피해잡니다. 대형, 제발 한 번만 용서해 주십쇼!”

이놈들을 어떻게 처리해야 하나 고민하던 나는 익숙한 단어에 잠시 멈칫했다.

“뭐라고?”

“진짜 딱 한 번만 더 용서해 주시면 착실하게 살겠습니다!”

“아니, 그거 말고. 저놈들이 뭐라고?”

“아, 마적단 말씀이십니까요?”

“그래, 그거.”

“저희도 잡힌 후에야 들었습니다. 웬 왈패 무리가 기루에서 은자를 뿌리며 다니기에 따라붙었는데…… 마적들 사이에서도 흉악하기로 소문난 적풍단(赤風團) 놈들이었지 뭡니까.”

“적풍단? 확실해?”

“예. 제 귀로 똑똑히 들었습니다. 맞지?”

다른 놈들도 앞다퉈 한 마디씩 보태기 시작했다.

“내일 날이 밝자마자 떠날 거라고도 했습니다.”

“산음(山陰)까지 가려면 쉬지 않고 달려야 한다고. 괜히 늦었다가 목 달아나는 거 아니냐고 걱정까지 하던데요.”

“그렇단 말이지.”

어제, 그리고 오늘. 이틀 연속으로 만난 마적이 하필이면 적풍단 소속인 것도 공교로운데, 산음은 항산검문의 본거지가 있는 응현(應現)과 가까운 곳이다.

“이 녀석들 말이 모두 사실이냐?”

내 오른손에 멱살이 붙잡혀 있던 인신매매범, 아니 적풍단의 마적이 덜덜 떨며 고개를 끄덕인 그 순간이었다.

삐이익!

날카로운 울음소리와 함께 한 마리의 매가 사당 앞에 내려앉았다. 발목에 묶인 자그마한 원통이 눈에 들어온다.

‘전서응.’

이거 어째 분위기가 묘하게 돌아가는데.
```

## Current accepted English baseline

```markdown
# Chapter 108

*Hunters?*

Wolhwa’s guess was only half right. They were hunters, all right—but the uninvited guests were something more special and far more vicious.

“Move it, you bastards.”

“Who can do anything with men as scrawny as you?”

There were ten of them in all. Every one had a rough-looking face and was armed with a weapon. At the front of their group, prisoners tied together with rope like a string of dried fish staggered along.

*Thud! Thud-thud!*

“Ugh, Boss!”

“We’re coming, we’re coming, so please stop already…”

“Huh, stop? These bastards still haven’t come to their senses.”

“Hey, take it easy. If you break something, their price drops. They’re small to begin with, so it looks like we won’t get full value for them.”

“We should get a decent price if we sell them to a circus troupe. Let’s hurry inside and have a drink.”

“Ah, my mouth waters just thinking about it… But what’s that?”

The human hunters came to an abrupt stop. Their eyes, which had been fixed on the four-horse carriage parked in front of the shrine, slowly shifted to the side.

At the end of their gazes stood Wolhwa and me.

“…Who are you?”

I stepped forward at the question from the man who appeared to be their leader.

“Just a traveler passing through.”

“A traveler. It’s dangerous to be wandering around at a time like this.”

The gleam in his eyes told me he was a dangerous man.

Of course, at Level 25, he didn’t even qualify as a threat to me.

“Wow, a four-horse carriage and a gorgeous woman. You must be a Young Master from a wealthy family, huh?”

If he had come closer to inspect it, he could have seen the crest of the Jin Family of Taiyuan carved into the carriage. But it was pitch-black outside, and he didn’t possess particularly sharp eyesight.

“I’m not from a poor family.”

“Well now. You’ve been awfully informal with me from the start.”

The leader licked his split lips. He seemed to be getting irritated, but he still hadn’t let down his guard around me.

“Whatever. This is a place we’ve been staying in for several days… What are you going to do?”

“Do about what?”

“What do you think? If you show us a little sincerity, we might let you have the place.”

“Anyone listening would think you owned this shrine.”

“It’s abandoned. Doesn’t that mean whoever claims it first owns it?”

“Then go get a certified property document.”

“What?”

The leader turned toward his men with a bewildered expression. Naturally. They had probably never heard the term in their lives. But it wasn’t as though any of them would know what it meant.

I clicked my tongue at the men whispering among themselves about the certified property document.

“If you can’t prove it, then leave quietly. And release the people you’ve tied up.”

“…You’re crossing the line. Are you waiting for bodyguards?”

“I don’t have any.”

“Then what are you relying on?”

“Me.”

The leader’s gaze shifted to my two empty hands.

“Without even a weapon?”

“People at your level? My fists are enough.”

“Looks like the Young Master learned a move or two somewhere… But aren’t you taking Murim a little too lightly?”

“Murim isn’t something to laugh at. You are.”

The moment I stepped toward the brightly burning torch, the prisoners who had been quietly restrained began screaming.

“Wh-what?”

“Boss! Boss!”

“You bastards gone crazy? Shut your mouths!”

The men in the rear drew daggers and held them to the prisoners’ throats in response to their violent reaction. The leader stared at me with wary eyes.

“Do you know them?”

“No. I’m seeing them for the first time in my life.”

Their sudden reaction had even caught me off guard. And why were they suddenly calling me Boss?

“Bosss! It’s me! It’s us!”

“These men seem to know you.”

“They’re just asking me to save them… Huh?”

I looked closely at the prisoners. They were all short as children and had uniformly ugly faces. They looked vaguely familiar.

*Is it because their body shapes resemble goblins?*

Wait. Goblins?

A memory from long ago suddenly came to mind. No, it wasn’t actually that long ago. It had happened only a few months earlier, during the tutorial Quest.

“Don’t tell me… You were with the Heavenly Axe?”

The prisoners—or rather, the Five-Colored Ghosts[^1] who had once been Jang Sam the Heavenly Axe’s subordinates—nodded frantically.

“That’s us!”

“Boss! Please save us!”

I never expected to run into these bastards here. As I stood there dumbfounded, Wolhwa, who had been watching the situation from behind, asked,

“Are these people acquaintances of Young Master Jin?”

“We’ve met before, at least.”

Human traffickers and bandits. It was hard to say which was worse.

Until a moment ago, I had been thinking of saving them. Now I was having second thoughts.

“Bosssss!”

“Are you planning to abandon us?”

“We quit being bandits after that day and have lived good lives ever since!”

“…”

Their ability to read the situation was almost supernatural. No wonder. They had surrendered immediately when the Heavenly Axe died, after all.

“Are you going to save them?”

“Tsk. I think we have to, at least.”

They said they had become new men after that day, and it felt wrong to leave them like this. More importantly, former bandits were far better than active human traffickers.

The leader, who had overheard our conversation, interrupted with a growl.

“Save them? You?”

“You heard the whole thing. Why ask again? You must live a tiring life.”

“You little shit, I’ve been letting you run your mouth, but…”

*Clang!*

The leader leveled his spear at me, and his men drew their weapons as well. Wolhwa clung to my side with a deliberately frightened expression.

“Oh my, I’m scared. You have to protect me, don’t you?”

Her moist eyes stirred a man’s protective instinct. Her expression was pleading.

To someone who knew Wolhwa’s true nature, it was an absurd sight. But the men swallowed hard.

“There’s one more reason I have to kill you.”

At the leader’s lecherous gaze, Wolhwa let out a shriek.

“Oh no, oh no! This maiden is so scared!”

“Ho ho, don’t be so frightened. Though I may have lived a rough life, you’ll soon learn that I’m a man with a heart as soft as silk. In a little while, we can have a conversation with our bodies.”

“Before that, deal with me.”

I needed to rip that filthy mouth open so he would never say anything like that again.

I strode toward him, then suddenly stopped. Seeing that, the leader burst out laughing.

“What’s wrong? Are you scared now that we’re actually going to fight? But it’s already too late.”

“Yeah. You’re really screwed.”

“…What?”

I gave the bewildered man a broad smile.

“I said you’re fucked, asshole.”

The moment I finished speaking, the ground shook, and a powerful wind whipped through the area.

*Boom—whoosh!*

It lasted no more than an instant.

The figure that swept past Wolhwa and me at terrifying speed was already standing in front of the leader.

“Say that again.”

Jin Mukyung.

An overwhelming wave of qi poured from his entire body and crushed the entire scene. The leader’s face turned deathly pale, and his hands began to tremble.

“F-forgive me. Please…”

The cold voice answered.

“You’re far too late.”

* * *

Perhaps Jin Mukyung was the greatest pacifist among us. In just over ten seconds, he had put an end to all the unnecessary fighting that would have followed.

“S-surrender! We surrender!”

“Please spare us! Please, just spare our lives…”

Their faces were frozen with terror. Everyone’s legs gave out, and they collapsed where they stood. Someone’s urine trickled down the hill.

The Five-Colored Ghosts were no different.

“Quiet.”

Jin Mukyung wiped the blood from his face and tossed out a single word. A deathly silence descended.

Hyuk Mujin, one eye bruised deep blue, whispered to me,

“Am I actually alive right now?”

“Yeah. Your breath against my ear is giving me goose bumps, so move away.”

“Just a moment ago, I was thinking, *How can someone get beaten like a dog this badly?* But now…”

*Gulp.*

Hyuk Mujin swallowed dryly, his gaze fixed on the fallen leader.

“Hng… Hng…”

With all four limbs broken and his dantian destroyed, the man struggled for breath. If he received proper care, he might be able to walk again, but his life as a martial artist was over.

The Level window I sensed through Qi Sense was proof.

> **System**
>
> **Level 2 — Lee Sam**

*The dung flies the watchers used as Familiars were Level 1, if I remember correctly.*

The culprit who had turned a Level 25 martial artist who had once been close to First Rate into a living corpse had been sneaking glances in our direction for a while.

“Captain, please save me. I think the Second Young Master is still short on blood.”

“Stop talking nonsense and move that guy somewhere suitable. He’ll die if you leave him like that.”

“Isn’t he a bastard who deserves to die? They were selling perfectly innocent commoners.”

“Even so, move him. He’s still alive.”

One of the greatest sources of dissonance I had felt while moving between Murim and the modern world was the issue of killing people.

For twenty-seven years, I had lived in a society where law and order existed.

I had trained to kill enemies with bladed weapons, but my targets had been monsters, not living humans.

*I was sure that was the case…*

Now I couldn’t even remember how many people I had killed. Even when I realized that the enemies who had died by my hand might have been real people rather than NPCs, I hadn’t felt particularly guilty.

*They were enemies. They were trying to kill me too.*

I didn’t know whether it was because I had lived as a Hunter or because I had grown accustomed to Murim’s ways. I was only surprised by my own numbness and the simplicity of my self-justification.

*For now, maybe this much is okay.*

I was living in two entirely different worlds. This wasn’t a situation where I had the leisure to put on an awkward act as a Buddhist.

Shaking off the thoughts clinging to me, I approached the men cowering on the ground.

“Eek!”

“Uaaagh! Save me, Boss!”

“These guys cause a commotion even when I’m trying to save them. Hold still.”

I untied the ropes, and the Five-Colored Ghosts were free. They stood on trembling legs.

“Th-thank you.”

“We’ll regard you as our Benefactor for the rest of our lives!”

“Like hell you will. Anyway, how did you end up getting caught by men like these? All five of you at once?”

The Five-Colored Ghosts were small, but they were grown men, at least in name. They had been strong enough to commit banditry alongside the Heavenly Axe.

“Um, well…”

“…?”

What was wrong with these guys?

Sensing something strange in their hesitation, I grabbed the nearest human trafficker by the collar and hauled him up.

“How did you catch these men?”

“We caught them trying to steal our money pouches in the marketplace.”

“…”

What the hell, these Ten-Colored Ghosts. I thought they had quit being bandits and might have taken up farming, but they had only changed occupations?

“Explain yourselves.”

Under my sharp gaze, the five men rolled their eyes back and forth.

“W-well…”

“Boss, people like us only know how to do this.”

“Even so, we only started recently!”

“We tried to work honestly, but things didn’t go very well… We said we’d pull just one job and get out, but then…”

“If we’d known they were mounted bandits, we wouldn’t have touched them. We’re victims too. Boss, please forgive us just this once!”

As I wondered what to do with these men, a familiar word made me pause.

“What did you say?”

“We’ll live honestly if you forgive us just one more time!”

“No, not that. What did they say?”

“Ah, do you mean the mounted-bandit group?”

“Yes. That.”

“We only heard after we were captured. Some bunch of ruffians were throwing silver around at a pleasure house, so we followed them… But they turned out to be members of the Red Wind Band, infamous for their viciousness even among mounted bandits.”

“The Red Wind Band? Are you sure?”

“Yes. I heard it clearly with my own ears. Didn’t I?”

The others began eagerly adding their own pieces.

“They said they were leaving as soon as dawn broke tomorrow.”

“They said they’d have to travel nonstop to reach Saneum. They were even worried that they might lose their heads if they arrived late.”

“So that’s how it is.”

Yesterday and today.

It was already an uncanny coincidence that the mounted bandits I had encountered two days in a row happened to belong to the Red Wind Band. On top of that, Saneum was close to Eung-hyeon, where the Mount Heng Sword Sect’s headquarters was located.

“Are these men telling the truth?”

The human trafficker held by the collar in my right hand—or rather, the mounted bandit from the Red Wind Band—nodded with a trembling head.

That was when it happened.

*Shriek!*

A hawk landed in front of the shrine with a sharp cry. A small cylinder tied to its ankle caught my eye.

*A messenger hawk.*

This was getting strange.

[^1]: A nickname meaning “Five-Colored Ghosts.”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 108`.

# Master Edit Task — Chapter 103

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
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소광    | **Lee Seogwang**   |
| 이소군    | **Lee Seogeun**    |
| 이소월    | **Lee Seowol**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 절정고수                | **Peak master** / **Peak martial artist** |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 내공     | **internal energy**                              |                                                       |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 낭인     | **wandering martial artist**                     |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 팔천협    | **Eight Spring Gorge** |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 혼주 | **Honju** | Shanxi location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 열양공 | **heat-yang technique** | Mukyung's heat-based internal-energy technique. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 산서제일미 | **Shanxi's foremost beauty** | Former reputation of Taekyung's mother. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 위팽 | 진태경 | retainer_to_third_young_master | Third Young Master | formal-polite and admonishing | Uses 삼공자 while warning Taekyung to return by noon and behave respectfully toward Jang Taebo. |
| 진태경 | 이소월 | young_martial_artist_to_allied_sect_leader | Young Lady Lee | formal-polite | Taekyung uses 이 소저 while greeting Seowol at the banquet. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 95–99

## Plot

Hong Woojin uses a kitten Familiar to infiltrate and surveil Jin Taekyung’s household, but Hayeon’s affection traps him in her room until he engineers a filthy escape. Taekyung recognizes Woojin when he returns home and later uses the two kitten Familiars and a staged phone call about a USB to bait the surveillance teams.

Sangdong Guild’s six-person Security Team, operating under Guild Master Im Chunsoo’s special order, identifies the three recently traded apartments near Taekyung’s home as possible surveillance bases. Convinced that Taekyung possesses valuable intelligence, Security Team Leader Choi Byungil authorizes an illegal attempt to seize the USB. Taekyung leads the team to a deserted mountain clearing, exposes their identities and affiliation, and reveals that the USB contains only his porn collection. After Choi orders the attack, Taekyung shatters an attacker’s dagger and begins the fight.

Hong Woojin observes the Sangdong team preparing to use violence and quits his assignment, reporting the decision to the Team 1 Leader.

## Continuity

- Sangdong Guild’s Security Team is conducting surveillance under a special order from Guild Master Im Chunsoo.
- Choi Byungil is the B-rank Security Team leader, with a Level in the mid-sixties. The other five field watchers are C-rank Hunters around Levels 30–40: Kim Gwondong, Park Hyungjin, Oh Gyuhyeon, Lee Mincheol, and Kim Junsu.
- Kim Junsu is Sangdong’s sole Familiar mage, a Level 41 C-rank mental mage suffering exhaustion and anxiety about his hair loss.
- The team uses black and white kitten Familiars and eavesdropping-magic Equipment installed in nearby real-estate offices.
- Taekyung identified three possible surveillance bases within five hundred meters of his home: Building 5, Unit 901; Building 4, Unit 302; and Building 3, Unit 202. Which one is occupied remains unknown.
- Taekyung scanned the apartment complex and parking lot with Qi Sense and found no suspicious vehicles.
- Taekyung deliberately baited the team with a phone call and a USB stored in his Inventory. The USB contains his porn collection, not intelligence.
- Taekyung has identified all six Sangdong watchers and confirmed their affiliation. The confrontation is underway in a deserted mountain clearing.
- Hong Woojin was recognized by Taekyung while infiltrating the home as a kitten Familiar. He maintains a rooftop supply-closet hideout at Taekyung’s apartment building and has quit the assignment after witnessing the planned violence.
- Hayeon is at the library; the two kitten Familiars were left with Taekyung before the bait operation.
- Unresolved: why Im Chunsoo issued the special warning about Taekyung; who Taekyung called; which apartment is the surveillance base; whether the black Familiar and Kim Gwondong share immediate instructions; and whether Woojin’s investigation and Sangdong’s operation have the same commissioning chain.

## Translation Decisions

- Retain **Familiar**, **Link**, **Qi Sense**, **Inventory**, **Lock**, and **third-awakening Hunter**.
- Use **mental mage** for 정신계 마법사 and **Security Team** for 보안팀.
- Use **Yeoreum** for 여름이 and **Midsummer** for the rejected naming pun.
- Render **도청 마법** as **wiretapping magic** and **도청 마법 Equipment** as **eavesdropping-magic Equipment**, according to context.
- Render **개냥이** as **dog-cat** with an explanatory footnote.
- Render **역마살** as **yeokmasal**, with a footnote explaining its wandering-fate meaning and age-related pun.
- Render **공(公)만 뺏기다** as **merely taking the credit** and **쇠뿔도 단김에 빼라** with the idiom about pulling the ox’s horn while it is hot.
- Preserve Hong Woojin’s profane, self-deprecating, deadpan comic voice; render **현자 타임** as **post-nut clarity**.

### Prior accepted reading-copy tails

#### Chapter 101 tail (verified mastered)

…
couldn’t bring himself to finish. *Exactly like yours, Guild Master.* Im Chunsoo glared at him. “Exactly like what?” “Oh, it was nothing.” “How bland. Some greenhorns were playing army down there, so I chased them away. Do colleges still have hazing culture these days?” “Ah, I see.” “What was it? I made them do some PT exercises for a while, and they looked ready to die.” Team Leader 1 felt the suspicions he had been harboring vanish completely. *I must have been out of my mind. How dare I even think such a thing?* While he reflected deeply on his mistake, Im Chunsoo laid into the Security Team. “Security Team Leader.” “Y-yes, sir!” “Well, look at that. You certainly know how to answer. After causing this mess, are you still a Team Leader just because you’re technically still a Team Leader?” “I’m sorry, Guild Master!” “Are the others keeping their mouths shut because they did such a good job? Do you want me to make my sword dance today?” “We’re sorry, Guild Master!” Team Leader 1 watched the scene with a pleased smile. Every so often, there were people who spread the rumor that Im Chunsoo had a godawful personality. But after watching him up close, Team Leader 1 knew better. He was a charismatic superior and an outstanding Senior in life. *Guild Master. I’ll follow you forever.* As he gazed at Im Chunsoo’s back with boundless respect, Team Leader 1 suddenly cocked his head. *…But why is there dirt on the Guild Master’s back?* He must have scolded those kids rather intensely. * * * “We’ve arrived.” At Butler Kim’s words, sitting in the passenger seat, I came to my senses with a start and looked around. Through the window, I could see the entrance to an apartment complex. *When did we get here?* “Th-thank you.” “Don’t mention it.” A smile appeared on his handsomely lined face. He looked like a middle-aged actor who had once ruled an era. *No, this man really did rule an era, too.* Until now, I had thought of him as nothing more than a Senior Hunter from a distant generation. But that meant I hadn’t understood Butler Kim at all. *He worked an A-rank mage like a dog—and Im Chunsoo, no less.* He had made a former war hero do a hundred sets of PT Exercise No. 8, then later kicked him in the shin with his dress shoe. Even now, the way he had calmly berated Im Chunsoo in that gentle voice sent chills down my spine. *Trainee, who uses mana during PT exercises?* *Whack!* *Trainee Number One Im Chunsoo. S-sorry, sir.* *Does it hurt? Now that you’ve gotten older, has your voice gotten quieter, too?* *No, sirrrrr!* *Attention. At ease. Attention. At ease.* *Snap-snap-snap-snap!* *On your backs. On your fronts. On your backs. On your backs.* *Gasp.* *Trainee, didn’t you hear this Instructor say on your backs? Get your head straight.* *I’ll correct it, sirrrr!* *And why are you bullying an innocent junior? Hasn’t this Instructor told you time and again that Seniors and juniors should help each other?* *S-sorry, sir.* *Repeat after me. Cherish your junior on the way down. Cherish your junior on the way up. One. Two.* *Cherish my junior!* *Trainee, I remember you’re Class 25. Am I right?* *Trainee Number One Im Chunsoo. Yes, sir.* *This Instructor is Class 3. If what happened today gets out or happens again, Classes 4 through 24 will assemble without exception.* *…* *Why aren’t you answering? Prepare for squat jumps.* *P-prepare, sir…* He worked him over, and over, and over again. It was the kind of sight you couldn’t see even if you paid for it. If the Sangdong Guild members had witnessed it, the Guild might have had to close its doors that very day. *Who the hell is Butler Kim, really?* Being Class 3 at the Hunter Training Center meant he could line up every Guild Master in the country on a parade ground and beat every last one of them with a bat. And he had been an Instructor, no less. It wouldn’t be an exaggeration to say that nearly every mage from the early days of the Great Cataclysm had passed through his hands. *He’s at least A-rank as a mage, too.* I could tell just by watching Im Chunsoo take his punishment without daring to make a peep. Butler Kim surpassed him in both seniority and skill. There was probably also an elemental advantage between ice and fire. You could say Butler Kim was the one who taught Im Chunsoo and raised him to his current position. *But…* Why was someone that accomplished working as a butler? I stole a sidelong glance at Butler Kim, only for our eyes to meet. “You seem to have a lot you want to ask.” “To be honest, I do.” My curiosity was killing me. Seeing my thoughts written plainly across my face, Butler Kim curled up the corners of his mouth. “It’s a long story.” “That’s fine. I’m on vacation, so I have plenty of time.” “Ah, then this is a good opportunity to hear your story as well, Mr. Jin. I already have more than one or two questions myself.” “Now that I think about it, it’s already dinnertime. Tomorrow is the last day of my vacation, so I have to sign a real-estate contract, too. Hahaha.” “……”

#### Chapter 102 tail (verified mastered)

…
accident as he climbed into the truck bed to move the capsule. “That thing must weigh quite a bit.” “It’s fine. I’ve moved plenty of them, so I know. Game capsules all weigh about the same.” “No, it’s seriously heavy.” I knew because I had lifted it myself earlier. It had felt reasonably hefty even to me, with my Strength stat in the triple digits. For the driver, it would be a different story entirely. “Boss, I’ll move it myself.” The driver wrapped his arms around the capsule and grinned. “Come on. You’re underestimating me. I was a Hunter back in the day. Something like this is—nnngh!” “Oh, wow.” As expected of a former Hunter, he did manage to lift it in one go. The only change was that the smile had vanished from his face. “Go ahead and open the doors. Quickly!” At the urgency in his voice, I dashed ahead and threw open the front gate and the front door. I had no idea why I was getting nervous too. “I can carry it—” “Move!” “Ah, yes.” He barreled into the living room at a speed fit for an alarm and screamed, “Which room?!” “I was going to put the capsule upstairs…” “What?!” “…but just leave it in the nearest room.” Fortunately, the door to one of the rooms was already open. The driver set the capsule down with a thud and began panting. “Why… is this… huff… so heavy?” “……” Hadn’t I told him it was heavy? * * * As soon as the moving driver left, I dropped onto the living room sofa. It was one of the pieces of furniture the previous owner had transferred to me on the condition that I pay the remaining balance all at once. *I’ll have to live alone for a few months.* I had told my family that I was going back to Bucheon. Until Hayeon finished her college entrance exam, I planned to eat and sleep here while commuting to work. *I need to remodel the house and buy a car too. Ah, the Guild said they’d provide me with a car anyway, so I need to get my license first.* There was a mountain of other things to do. But instead of feeling tired, I felt energized. These were all things I hadn’t been able to do before, no matter how much I wanted to. It had only been a few months since I had done nothing but suffer while going back and forth between Gates and the goshiwon, yet so much had changed. *You’ve come a long way, Jin Taekyung.* One person suddenly came to mind. A man who had always smiled like a boy despite his age. A man who had done his best for his wife and children and approached them like a friend. *Dad, I bought a house. The place we used to live in was already gone. But I did well enough, right?* I wanted to brag about it like a child, but the person who would have praised me had passed away long ago. All I could do was repeat words in my heart that would never reach him. How much time passed like that? When I came to my senses, it was already eight in the evening. The summer sun was slowly setting. *So this is how my last day of vacation ends.* An entire week of vacation. It had been hectic because of everything involving the Sangdong Guild, but it was still the best rest I had enjoyed since becoming a Hunter. Now it was time to return to my daily life. *In exactly twelve hours.* I lay flat on the sofa where I had been sitting. I briefly considered entering the capsule, but soon dismissed the thought. After eleven years, I finally had a home again. Just this once, I wanted to wake up in our living room instead of inside that stuffy capsule. *Login.* The System responded to my call. Ding. > **System** > > Would you like to connect to Murim? > > Y / N Of course, my answer was yes. * * * Long after Jin Taekyung lost consciousness, something no one could have expected was happening in the room beside the front door. Hissssss. The door of the metal object that looked like a gigantic egg—the capsule—slowly began to open. The first thing to emerge was a pair of feet. Red letters were printed across a pair of long athletic socks that reached up to the calves. **Hope Goshiwon Early-Morning Soccer Club** Next came sweatpants rolled up halfway, followed by a pair of pale, skinny hands. The cover of the book he clutched tightly, as though it were scripture, gleamed in the sunset pouring through the window. **Complete Mastery of the Civil Service Exam** And finally, his face emerged. After enduring several long hours of agony, he looked as haggard as Crown Prince Sado[^1] yet as relieved as Park Hyeokgeose emerging from an egg.[^2] A parched voice slipped between his bone-dry lips. “Is this my new nest…?” As Seong Jinho gazed around the spacious room, a satisfied smile spread across his lips. [^1]: Crown Prince Sado was an eighteenth-century Joseon royal who died after being confined in a wooden rice chest. [^2]: Park Hyeokgeose is the legendary founder of the ancient Korean kingdom of Silla, said to have been born from an egg.

## Korean source

```text
＃103화



덜컹덜컹.

미숙한 마부가 모는 마차는 위태로웠다.

나름대로 정비가 잘된 가도(假道)라고는 하나 며칠째 계속되는 폭설에 채찍은 고드름이 되었고 말들의 엉덩이를 찌르기 일쑤였다.

그리고 드디어 사달이 났다.

푹!

히히잉!

미끄러운 눈길에도 제법 빠르게 발을 놀리던 준마 네 마리가 갑자기 걸음을 멈춘 것이다.

“으헉!”

앞으로 고꾸라질 뻔한 마부가 가까스로 중심을 잡았다. 그러나 낙마를 면했다는 안도감보다 앞으로 닥쳐올 일에 대한 두려움이 앞섰다.

‘제발, 옥황상제님, 원시천존님.’

간절한 바람이 통한 걸까? 슬쩍 마차 안을 들여다보았지만 두 청년은 아무 일도 없었다는 듯이 앉아 있었다.

‘뭐, 정확히 말하면 한 명은 자고 있는 거지만.’

털가죽에 파묻혀 이마만 빠끔히 보이는 한 청년은 수혈이라도 짚였는지 도무지 깰 생각을 안 하고, 다른 한 청년은 가부좌를 튼 채 운기조식에 여념이 없다.

스으으읍. 후우우우.

만약 누군가가 그 광경을 봤다면 두 번 놀랐을 것이다.

청년의 수려한 용모에 한 번, 그의 몸에서 뿜어져 나오는 절정고수의 무형지기(無形地氣)에 또 한 번.

어느 정도 그에게 익숙해졌다고 생각한 마부, 혁무진도 크게 다르지 않았다.

‘이런 개 같은 경우를 봤나.’

이제는 부러운 걸 넘어서 화가 날 지경이다.

뛰어난 외모와 천재적인 무재(武才). 둘 중 하나만 가져도 소원이 없겠는데 저 청년, 진무경은 둘 다 가졌다.

‘심지어 한 명 더 있지.’

운기조식을 할 거라더니 죽은 듯이 자고 있는 또 다른 청년, 진태경도 마찬가지다.

아니, 어쩌면 형인 진무경보다 더한 괴물일지도 모르겠다.

불과 몇 달 전까지만 하더라도 기루나 돌아다니던 삼류 망나니가 산서 제일의 잠룡이 됐으니까.

‘아무리 형제라지만 이렇게까지 닮을 수가 있나.’

과거 산서제일미였다는 모친의 핏줄을 고스란히 물려받은 용모. 질투심이 날 정도로 천재적인 재능.

그리고 마지막으로…….

‘둘 다 성격이 더럽지.’

혁무진은 두 형제를 번갈아 가며 노려봤다.

한 놈은 수하가 마부석에서 얼어 죽든 말든 제 한 몸 덥히겠다고 털가죽을 죄다 가져갔고, 다른 한 놈은 마차도 제대로 못 몬다며 장장 한 시진을 구박하더니 이젠 속 편하게 운기조식 중이다.

‘난형난제가 따로 없군.’

좋은 쪽으로 우열을 가리기 힘들어야 하는데 이 형제는 그 반대다.

혁무진이 둘 중 누구의 인성이 더 개차반인가 곰곰이 생각하던 그때였다.

“야.”

서늘한 목소리. 막 운기를 끝마친 눈동자에서 항거할 수 없는 무형의 기운이 뿜어져 나와 혁무진을 옭아맸다.

“뭐 해, 마차 안 몰고.”

“자, 잠깐 문제가 생겨서 말입니다.”

“무슨 문제.”

“그게……”

얼어붙은 채찍에 엉덩이를 찔린 말들이 화났습니다, 라고 하면 무슨 일이 벌어질까? 혁무진은 현명한 선택을 했다.

“몸이 얼어서 마차를 못 몰겠습니다.”

이참에 좀 쉬고 싶기도 했다. 아까부터 마부석에서 고생한 엉덩이에게도 휴식을 줘야 하지 않겠는가.

하지만 진무경의 대응은 간단했다.

“손.”

“예?”

“손 내밀어 보라고.”

혁무진은 엉겁결에 똥개처럼 손을 내밀었다. 그러자 그걸 붙잡은 진무경이 한마디를 툭 내뱉었다.

“뜨거워도 참아라.”

말뜻을 파악하기도 전에 손끝을 타고 어마어마한 기운이 솟구쳤다. 순간 숨이 턱 막힐 정도의 화기(火氣)에 온몸이 불타는 듯했다.

‘허억!’

충격이 너무 크면 비명도 안 나오는 법이다. 찰나에 지나지 않는 짧은 순간이었지만 혁무진은 입을 딱 벌리고 몸을 부르르 떨었다. 어느새 진무경이 자신의 손을 놓았다는 사실조차 알지 못했다.

“어때, 좀 낫나?”

그제야 정신을 차린 혁무진이 간신히 입을 열었다.

“바, 방금 그게 뭡니까?”

“간단한 열양공의 일종이다.”

“……그렇게 간단해 보이진 않던데요. 타 죽는 줄 알았습니다.”

“그래? 역시, 겉핥기식으로 익힌 거라 미숙했나 보군.”

진무경의 대수롭지 않은 말투에 혁무진은 어이가 없었다.

‘겉핥기식으로 배운 걸 왜 나한테 써…….’

난형난제? 인성 싸움은 형의 압승이다.

진태경은 쥐어팬 적은 있어도 열양공으로 태워 죽이려고 하진 않았으니까.

“몸도 녹았으니 이제 가서 마차를 몰아라. 갈 길이 구만리다.”

“…….”

녹은 게 아니라 불태운 수준이지만 효과는 확실했다.

“그럼 다시 출발하겠습니다.”

혁무진이 후끈후끈해진 몸으로 마부석으로 돌아가자 진무경의 시선이 정면을 향했다.

털가죽에 파묻혀서 이게 곰인지, 사람인지 헷갈리는 진태경이 보였다.

‘운기를 한다더니 퍼질러 자고 있군.’

헛소리일 거라고 생각했지만 이렇게 당당하게 숙면을 할 줄은 몰랐다. 무인이라면 항상 무공에 대해 고민하고, 수련을 거듭해야 하는 법이거늘.

진무경이 굳은 얼굴로 호통쳤다.

“이놈, 당장 일어나지 못하겠느냐!”

“으헉!”

마부석의 혁무진은 물론이고 말들까지 움찔할 정도로 쩌렁쩌렁한 외침이다. 그러나 정작 진태경은 요지부동이었다.

쌔액. 쌔액.

“이노옴!”

자리에서 벌떡 일어난 진무경이 손바닥으로 아우의 이마를 후려갈겼다. 쫙, 하는 소리와 함께 피부가 벌겋게 달아오른다.

‘이래도 안 일어나는지 보자.’

쫙, 쫙, 쫙.

쌔액. 쌔액.

“……!”

이마가 붉어지다 못해 혹까지 생겨 터질 듯한데도 미동 하나 없다.

진무경은 크나큰 충격에 휩싸였다. 이 정도면 내공 한 톨 없는 양민도 비명을 지르며 일어나야 하는데, 명색이 초일류의 무인에 산서잠룡이라는 놈이 꿈쩍도 안 한다.

살다 살다 이렇게 무방비한 놈은 처음 봤다.

‘그리고 그놈이 내 동생이라니.’

지난 며칠간 단련시켰던 것이 마치 헛수고처럼 느껴지던 그때.

“으음.”

영원히 감겨 있을 것만 같던 진태경의 눈이 스르륵 뜨였다.



* * *



눈을 뜨기도 전에 무림으로 돌아왔다는 사실을 깨달았다.

볼에 닿는 서늘한 공기. 덜컹거리는 마차 내부.

그리고 통증.

“……?”

잠깐. 웬 통증?

눈을 떠 보니 제법 익숙한 얼굴이 나를 내려다보고 있었다.

‘진무경.’

뭐 이런 놈이 있나, 하는 표정의 그를 무시하고 기울어져 있던 몸을 바로 했다. 그리고 그 후에야 통증의 원인을 알 수 있었다.

“아야.”

이마다. 조심스럽게 만져 보니 혹과 함께 주위 피부가 화끈거리는 것이 느껴졌다.

‘뭐여, 이건.’

도대체 여기서 뭘 했다고 이마에 혹이 나 있어?

순간 벽에 머리라도 박았나 싶었지만, 근골과 맷집을 꾸준히 올려놓은 터라 그 정도로는 생채기도 안 난다.

‘이건 딱 작정하고 때린 건데.’

마침 용의자 두 명이 보인다.

진무경과 혁무진. 누가 범인인지는 세 살배기 어린애도 알겠다.

“나 자는 사이에 뭔 짓 했지.”

“자는 사이? 그전에는 운기조식이라고 하지 않았나?”

“……내가?”

한참 된 일이라 기억도 안 나는데. 어쨌든 지금 그게 중요한 게 아니다.

“자는 사람을 때려?”

“네 꼴이 하도 한심해 보여 그런 것이다. 무인이라는 놈이 수련할 생각은 안 하고 잘도 퍼질러 자더군.”

“넌 무인이라는 놈이 비열하게 무방비인 상대를 공격하냐?”

“그럼 당장 내려서 한 판 붙을까? 무인답게.”

우리는 누가 먼저랄 것도 없이 벌떡 일어나 서로를 노려봤다. 진무경이 스산한 어조로 말했다.

“형무진.”

“혁무진입니다. 이공자님, 제발.”

“당장 마차 세워.”

“……옙.”

마차의 속도가 천천히 줄어들기 시작했다. 이번에는 내 차례다. 나는 놈의 시선을 맞받아치며 입을 열었다.

“혁무진.”

“아, 조장님은 또 왜요.”

“계속 가.”

“하, 미치겠네.”

마차의 속도가 다시 빨라지기 시작했다. 천천히 자리에 앉는 나를 보며 진무경이 기가 차다는 표정으로 물었다.

“무인답게 한 판 붙자고 하지 않았나?”

“한심하긴. 임무가 먼저고 붙는 건 그다음이야. 그리고…….”

“그리고?”

“난 붙자고 한 적 없다. 비열하다고 했을 뿐.”

“…….”

최대한 당당하게 말했지만 모양이 빠지는 건 어쩔 수 없다.

나는 흘끗 진무경의 레벨창을 확인했다.



[Lv.??? 진무경]



그래, 인간적으로 오자마자 싸우는 건 좀 아니지.



* * *



‘퀘스트창 확인.’

띠링.



퀘스트



[어제의 적, 오늘의 동지]

모든 진실이 밝혀진 지금, 항산검문은 적이 아니라 손을 잡아야 할 동지입니다. 곧 다가오는 원단에 그들을 태원진가로 초대하십시오.



등급 : 일류

제한 : 진태경

임무 : 초대장 전달 (미완료)

보상 : ???

실패 : 없음





마지막으로 받았던 퀘스트를 다시 한번 확인했다.

쉬운 임무다. 퀘스트 등급도 그리 높지 않고, 실패 시 패널티도 없다. 그저 항산검문 측에 초대장만 전달하면 그만이다.

‘항산검문이라…….’

지금의 항산검문은 뼈대만 남았다. 이소군이 독살당하고 이천백이라는 기둥이 무너지자 붕괴는 순식간이었다.

‘팔천협 전투가 치명타였지.’

발 없는 말이 천 리를 간다고 했다.

수많은 눈과 귀가 집중됐던 그 날의 전투는 전서구와 사람들의 입을 통해 빠르게 퍼져 나갔고, 거의 모든 주력이 빠져나간 항산검문은 누군가에겐 좋은 먹잇감이었다.

‘낭인, 그리고 마적 떼.’

물경 이백에 달하는 습격자들이 항산검문을 급습했다고 했다. 이틀 밤낮의 전투 끝에 습격자들은 패퇴, 일찍이 근신 처분을 받고 문파에 남아 있던 이소광은 끝내 전사했다.

항산검문은 새로운 구심점이 필요했고, 그렇게 한 사람이 등장했다.

‘이소월.’

이천백의 마지막 남은 핏줄이자 현(現) 항산검문주.

우리는 그녀에게 이 초대장을 전달해야 한다.

문제는…….

‘나랑 영 껄끄러운 관계라는 거지.’

사실 껄끄럽다는 표현도 내 입장에서 순화한 거다.

어떻게 보면 이 모든 일의 시작점에 나와 이소월이 있었으니까.

‘그때가 수련동에서 막 나왔을 때였지, 아마.’

당시 위팽이 했던 말은 토씨 한 글자 안 틀리고 기억한다.



‘항산검문의 여식을 범하려 한 것이 사실입니까?’



지금이야 내가 결백하다는 걸 모르는 사람이 없지만, 그때만 해도 천하의 죽일 놈 취급받았었다.

조작한 증거로 태원진가를 압박하러 왔던 이소군은 돌아가던 길에 독살당했고, 그게 모든 일의 시작이었다.

‘겨우 한두 달이 흘렀을 뿐인데.’

가문에서도 멸시받던 삼류 망나니는 산서잠룡이 되고, 이름도 몰랐던 그녀는 이제 항산검문의 새로운 주인이다.

우리 둘 다 그사이 참 많은 변화를 겪었으니 어떤 의미로는 공통점이 있다고 할 수도 있겠다.

‘처지는 많이 달라졌지만.’

태원진가는 이제 자타가 공인하는 산서제일가(山西第一家).

반면 항산검문은 속 빈 강정에 불과하다. 이 초대장은 사실 이제 태원진가의 밑으로 들어오라는 항복 권유에 가깝다.

과연 이소월이 어떤 반응을 보일지는 직접 겪어 봐야 알 수 있을 것 같다.

‘다짜고짜 칼침만 안 놨으면 좋겠네.’

그런 생각과 함께 퀘스트창을 닫은 그때, 햇빛이 쏟아지고 왁자지껄한 소리가 가까워졌다. 혁무진이 잔뜩 상기된 얼굴로 나를 바라봤다.

“혼주(昏住)입니다.”

그녀와의 거리가 이틀까지 좁혀진 순간이었다.
```

## Current accepted English baseline

```markdown
# Chapter 103

Clatter, clatter.

The carriage lurched dangerously under the hands of an inexperienced coachman.

Though it was a fairly well-maintained makeshift road, the blizzard that had continued for several days had frozen the whip into an icicle, and it kept jabbing the horses in the rump.

And then, at last, trouble struck.

Thud!

Neigh!

The four fine horses, which had been moving their hooves surprisingly quickly despite the slippery snow, suddenly stopped.

“Gah!”

The coachman nearly pitched forward but somehow managed to regain his balance. Yet more than the relief of avoiding a fall, he was consumed by fear of what was about to happen.

*Please, Jade Emperor, Primordial Heavenly Venerable.*[^1]

Had his desperate prayer been answered? He cautiously peeked into the carriage, but the two young men were sitting there as though nothing had happened.

*Well, technically, one of them is sleeping.*

One young man was buried in fur until only his forehead showed. Perhaps someone had pressed a sleep-inducing pressure point, because he showed no sign of waking. The other sat cross-legged, utterly absorbed in circulating his qi.

Sssssip. Hooooo.

If anyone had witnessed the scene, they would have been surprised twice.

Once by the young man’s handsome features, and once again by the formless qi of a Peak master pouring from his body.

Hyuk Mujin, the coachman, thought he had grown somewhat accustomed to him by now. But he was no different.

*What kind of bullshit is this?*

His envy had gone beyond envy and reached the point of anger.

A handsome face and genius-level martial talent. If he possessed even one of those things, he would have no other wish in the world. But that young man, Jin Mukyung, had both.

*And there’s even another one.*

The same went for the other young man, Jin Taekyung, who had said he would circulate his qi only to fall into a deathlike sleep.

No, he might even be a greater monster than his older brother, Jin Mukyung.

After all, only a few months ago, he had been a Third Rate wastrel who did nothing but visit pleasure houses. Now, he was the Sleeping Dragon of Shanxi.

*How can two brothers be this alike?*

Their handsome features had been inherited in full from their mother, who had once been known as Shanxi’s foremost beauty. Their talent was so extraordinary it inspired jealousy.

And lastly…

*They were both assholes.*

Hyuk Mujin glared at the two brothers in turn.

One had taken all the fur for himself to keep warm, whether his subordinate froze to death on the driver’s bench or not. The other had given him hell for a full two hours because he couldn’t even drive a carriage properly, and now he was comfortably circulating his qi.

*They’re perfectly matched.*

They should have been difficult to rank because of their excellence, but these brothers were the opposite.

Hyuk Mujin was carefully considering which brother had the worse personality when it happened.

“Hey.”

A chilly voice. Formless qi poured from the eyes of the man who had just finished circulating his qi, binding Hyuk Mujin in place.

“What are you doing? Why aren’t you driving?”

“A problem, ahem, came up for a moment.”

“What problem?”

“Well…”

What would happen if he told him that the horses had gotten angry because the frozen whip kept stabbing them in the rump? Hyuk Mujin made the wise choice.

“My body is frozen, so I can’t drive.”

He also wanted to take a break. Didn’t the backside that had been suffering on the driver’s bench deserve some rest?

But Jin Mukyung’s response was simple.

“Hand.”

“Pardon?”

“Give me your hand.”

Hyuk Mujin reflexively held out his hand like a mutt. Jin Mukyung grabbed it and casually said,

“Bear with the heat.”

Before Hyuk Mujin could understand what he meant, an enormous surge of qi traveled through his fingertips. The fire qi was so intense that his entire body seemed to catch fire, and his breath caught in his throat.

*Gah!*

The shock was too great for a scream to come out. It lasted no more than an instant, but Hyuk Mujin stood there with his mouth hanging open, his body trembling violently. He did not even realize that Jin Mukyung had already let go of his hand.

“How is it? Better?”

Only then did Hyuk Mujin come to his senses. He barely managed to open his mouth.

“What, what was that just now?”

“A simple type of heat-yang technique.”

“That didn’t look simple… I thought I was going to burn to death.”

“Really? I suppose I’m still unskilled at it, since I only learned it superficially.”

Jin Mukyung’s offhand tone left Hyuk Mujin dumbfounded.

*Why would you use something you only learned superficially on me…?*

Hard to tell the brothers apart? The older brother won the contest by a mile.

Jin Taekyung had beaten him up before, but he had never tried to burn him to death with heat-yang qi.

“Now go drive the carriage. We still have a long way to go.”

“…”

He hadn’t merely warmed up. He had been roasted. But the effect was undeniable.

“Then I’ll get us moving again.”

When Hyuk Mujin returned to the driver’s bench with his body blazing hot, Jin Mukyung turned his gaze forward.

Jin Taekyung was buried in fur so thoroughly that it was difficult to tell whether he was a bear or a person.

*He said he was going to circulate his qi, but he’s sleeping like a log.*

Mukyung had thought he was talking nonsense, but he hadn’t expected him to sleep so openly. A martial artist was supposed to constantly ponder martial arts and train without rest.

Jin Mukyung shouted with a stern expression.

“You rascal! Will you not get up this instant?”

His voice reverberated so loudly that Hyuk Mujin on the driver’s bench and even the horses flinched. Yet Jin Taekyung himself did not stir.

Snnn. Snnn.

“You rascal!”

Jin Mukyung sprang to his feet and struck his younger brother’s forehead with his palm. With a sharp smack, the skin turned bright red.

*Let’s see if this wakes you up.*

Smack, smack, smack.

Snnn. Snnn.

“…”

His forehead had turned red enough for a lump to rise and look ready to burst, yet he did not twitch.

Jin Mukyung was overwhelmed by shock. Even a commoner without a shred of internal energy should have screamed awake from this. Yet this guy, supposedly a top-tier First Rate martial artist and the Sleeping Dragon of Shanxi, did not move an inch.

Jin Mukyung had never seen anyone so defenseless in all his life.

*And that guy is my younger brother.*

Just as the training he had put Taekyung through over the past several days was beginning to feel like a complete waste of time—

“Hmm.”

The eyes that had seemed destined to remain closed forever slowly opened.

* * *

Before I even opened my eyes, I realized that I had returned to Murim.

The cool air against my cheek. The rattling interior of the carriage.

And pain.

“…”

Wait. Why was I in pain?

When I opened my eyes, a fairly familiar face was looking down at me.

*Jin Mukyung.*

I ignored his expression, which seemed to say *What kind of person is this?*, and straightened my slumped body. Only then did I identify the source of the pain.

“Ow.”

My forehead. When I carefully touched it, I felt a lump and the heat radiating from the surrounding skin.

*What the hell?*

How had I gotten a lump on my forehead?

For a moment, I wondered if I had slammed my head against the wall. But with the bones, muscles, and toughness I had steadily built up, that wouldn’t even leave a scratch.

*This was a deliberate hit, plain and simple.*

Fortunately, there were two suspects right in front of me.

Jin Mukyung and Hyuk Mujin. Even a three-year-old could tell who the culprit was.

“What did you do while I was asleep?”

“While you were sleeping? Didn’t you say you were circulating your qi before that?”

“…”

*I did?*

It had happened long enough ago that I couldn’t even remember it. But that wasn’t important right now.

“You hit someone while they were sleeping?”

“You looked so pathetic that I did. A martial artist like you was sleeping away instead of training.”

“You call yourself a martial artist and attack someone who’s defenseless?”

“Then shall we get off right now and have a bout? Like true martial artists?”

We both sprang to our feet and glared at each other without waiting for the other to move first. Jin Mukyung spoke in an ominous tone.

“Hyung Mujin.”

“It’s Hyuk Mujin. Second Young Master, please.”

“Stop the carriage.”

“…”

“Yes, sir.”

The carriage slowly began to decelerate. Now it was my turn. I met his gaze and opened my mouth.

“Hyuk Mujin.”

“Ah, why me this time, Squad Leader?”

“Keep going.”

“Haah, this is driving me crazy.”

The carriage began to speed up again. As I slowly sat back down, Jin Mukyung asked with an incredulous expression,

“Didn’t you just suggest that we have a bout like martial artists?”

“What a joke. The mission comes first, and fighting comes after. And…”

“And?”

“I never said we should fight. I only said you were underhanded.”

“…”

I had said it as confidently as possible, but there was no hiding how lame it looked.

I snuck a look at Jin Mukyung’s Level window.

> **System**
>
> **Lv. ??? Jin Mukyung**

*Right. Come on, fighting him the moment I got back would be a bit much.*

* * *

*Check the Quest window.*

Ding.

> **System**
>
> **Quest**
>
> **Yesterday’s Enemy, Today’s Ally**
>
> Now that all the truth has been revealed, the Mount Heng Sword Sect is no longer an enemy but an ally you must join forces with. Invite them to the Jin Family of Taiyuan for the upcoming Lunar New Year.
>
> **Grade:** First Rate
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Deliver the invitation (Incomplete)
>
> **Reward:** ???
>
> **Failure:** None

I took one more look at the last Quest I had received.

It was an easy mission. The Quest’s Grade wasn’t particularly high, and there was no penalty for failure. I simply had to deliver the invitation to the Mount Heng Sword Sect.

*The Mount Heng Sword Sect…*

The current Mount Heng Sword Sect had been reduced to its bare bones. Once Lee Seogeun was poisoned and the pillar known as Lee Cheonbaek fell, its collapse had been swift.

*The battle at Eight Spring Gorge had been the fatal blow.*

They say words without feet can travel a thousand li.

That day’s battle, watched by countless eyes and ears, spread rapidly through messenger pigeons and word of mouth. With nearly all its main forces gone, the Mount Heng Sword Sect became easy prey for someone.

*Wandering martial artists. And mounted bandits.*

They said as many as two hundred attackers had suddenly raided the Mount Heng Sword Sect. After two days and nights of fighting, the attackers were driven off. Lee Seogwang, who had remained at the sect after being placed under disciplinary confinement, ultimately fell in battle.

The Mount Heng Sword Sect needed a new rallying point, and one person emerged.

*Lee Seowol.*

Lee Cheonbaek’s last surviving descendant, and the current Sect Leader of the Mount Heng Sword Sect.

We had to deliver this invitation to her.

The problem was…

*We had a thoroughly uncomfortable relationship.*

Actually, “uncomfortable” was a softened description from my perspective.

In a way, the two of us had been at the very starting point of all this.

*I think it was right after I came out of the training cave.*

I remembered Wipeng’s words exactly, down to the last syllable.

“Is it true that you tried to force yourself on the daughter of the Mount Heng Sword Sect?”

These days, no one was unaware of my innocence. But back then, I had been treated like the worst bastard under heaven.

Lee Seogeun, who had come to pressure the Jin Family of Taiyuan with fabricated evidence, was poisoned on his way home, and that was the beginning of everything.

*Only a month or two has passed.*

The Third Rate wastrel despised by his own family had become the Sleeping Dragon of Shanxi, while the woman whose name I hadn’t even known was now the new Sect Leader of the Mount Heng Sword Sect.

We had both gone through so many changes in the meantime that, in a sense, we had something in common.

*Our positions, however, were very different.*

The Jin Family of Taiyuan was now, by everyone’s admission, the foremost family in Shanxi.

The Mount Heng Sword Sect, on the other hand, was nothing more than an empty shell. This invitation was, in truth, almost a proposal that they surrender and come under the Jin Family of Taiyuan.

I would have to experience it firsthand to know how Lee Seowol would react.

*I just hope she doesn’t suddenly stab me.*

Just as I closed the Quest window, sunlight streamed in and the sound of a boisterous crowd drew closer. Hyuk Mujin looked at me, his face flushed with excitement.

“We’re at Honju.”

We were now only two days away from her.

[^1]: The Jade Emperor and Primordial Heavenly Venerable are major figures in Daoist cosmology.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 103`.

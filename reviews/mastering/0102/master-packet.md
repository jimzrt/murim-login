# Master Edit Task — Chapter 102

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
| 생도     | **cadet**                                    |
| 선배     | **Senior**                                   |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 로그인              | **Login**                      |
| 로그아웃             | **Logout**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 성진호 | **Seong Jinho** |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 사도세자 | **Crown Prince Sado** | Joseon crown prince used in the comparison for Jinho's haggard appearance; footnoted. |
| 박혁거세 | **Park Hyeokgeose** | Legendary founder of Silla, used in the comparison to Jinho emerging from the capsule; footnoted. |
| 꼰대 | **boomer** | Modern slang for a hidebound older person; used by Cheongpung. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 진태경 | 기사님 | customer_to_moving_driver | Driver | polite | Taekyung addresses the private moving-truck driver by his occupational title on the phone. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |
| 고생하셨습니다 | register | Subordinate courtesy (“thank you for your hard work”), not a superior’s “Good work.” | |

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

#### Chapter 100 tail (verified mastered)

…
“Jin Taekyung. That’s you, isn’t it?” “Well, yes, but… who are you?” “My name is Im Chunsoo. I heard you have a few of my people with you.” “…” “Are you listening?” I was listening. I just couldn’t speak. The Guild Master of a mid-sized Guild had come all the way here himself to meet me. And it was Im Chunsoo, of all people—the man notorious for his temper. “Come down. We can clear up any misunderstandings over a meal.” There was no misunderstanding to clear up, but I had no idea what would happen if I said, *No.* Hadn’t the man already found out my location? In the end, I had only one option. “I’ll come down now.” * * * Im Chunsoo made a powerful first impression. He was younger than I had expected, and although his eyes seemed gentle, they burned with heat. *Fiery.* Ironically, that was my first thought upon meeting a master of ice magic. “Hello. I’m Jin Taekyung.” “I’m Im Chunsoo.” Unlike his burning gaze, his voice was cold. At last, he seemed like someone who deserved the nickname Frozen. “It’s strange seeing in person a face I’ve only seen in report photos.” There were actually people who could admit so bluntly and without embarrassment that they had dug into my background. “What about my people?” “They’re upstairs.” “Any fatalities?” “Of course not. I’d hate to become a criminal.” “I appreciate that.” Im Chunsoo gave me a slight nod. “My people got impatient and made a mistake. Can you let it slide?” “If there’s reasonable compensation.” Im Chunsoo gave a short laugh, while the man beside him, who looked like a Team Leader, frowned. “Young man, you have no manners.” “I can be like that… but it feels a little strange hearing it from the people who put me under surveillance.” “Even so—” The man couldn’t continue. Im Chunsoo raised a hand to stop him. “Team Leader 1, go upstairs and release my people.” “…Yes, Guild Master.” If Kim Butler possessed a gentle charisma, this man possessed a rough one. Maybe it was because they were both mages. Somehow, the two men overlapped in my mind. “Come take a walk with me.” Im Chunsoo went ahead, and I followed behind him. “Do you know something?” After walking briskly for a while, Im Chunsoo suddenly spoke. “Once I have a grudge against someone, I have to see it through to the end. I don’t know about you, but that’s the kind of person I am.” *Very Murim of him.* The strong devour the weak. Survival of the fittest. It seemed this man had the blood of a Murim tough guy running through his veins, too. “That’s how I built the Sangdong Guild. I climbed higher by stepping on what I had brought down and salvaging whatever I could.” “I see.” “What about the Peace Guild?” “…What do you mean?” “The past decade has been dull. We’re allies with every nearby Guild, and we haven’t had a rival for a long time. Then you people appeared.” I looked into his eyes, where curiosity and passion seemed to boil, and had only one thought. *This is dangerous.* Im Chunsoo continued, regardless. “Your Guild Master and Team Leader are people even I can’t easily access information on… But more than anything, your existence has stirred me up.” We were climbing a hill now. Despite his considerable age, Im Chunsoo didn’t seem short of breath. “Do you know why I came all the way here?” “To see me.” “You’re only half right.” Im Chunsoo’s footsteps stopped. Slowly turning around, he released a frigid chill from his entire body. > **System** > > Level 75 Im Chunsoo “At my age, time is money. I’m not so extravagant that I’d come all the way here just to see your face.” Frozen. The seasoned A-rank mage who had fought his way through the Great Cataclysm himself. The moment he extended his hand toward me— Hissssss. A dozen or so ice spikes formed in the empty air above my head. The midsummer air froze, and frost settled over the scorching dirt path. *I’d been well and truly caught.* I had thought he was an old man with some sense of propriety. I never imagined he would launch straight into something like this. “Do you really have to go this far?” “I’m going this far because it’s you.” “I’m only a C-rank.” “Exactly. Let’s see what that C-rank Hunter can do.” The moment he finished speaking, Im Chunsoo clenched his fist. The ice spikes, streaming with biting cold, shot toward me. Whoosh! But they couldn’t even touch the hem of my clothes. “Rise up. Fire Wall.” At the sound of a clear voice, the mana permeating the air began to churn. The ground, which had been frosted over by Im Chunsoo’s magic, melted as flames surged upward. Fwoosh! Roar! It was a wall of fire in the most literal sense. Blue flames swallowed the ice spikes and split the space between Im Chunsoo and me. Beyond the wavering flames, Im Chunsoo cried out in shock. “This is…!” But I wasn’t looking at Im Chunsoo. A man standing behind him at the entrance to the hiking trail greeted us in a gentle voice. “I’m glad I’m not late. You too, Chunsoo.” > **System** > > Level 80 Kim Hwajong Kim Hwajong. Kim Butler had arrived.

#### Chapter 101 tail (verified mastered)

…
couldn’t bring himself to finish. *Exactly like yours, Guild Master.* Im Chunsoo glared at him. “Exactly like what?” “Oh, it was nothing.” “How bland. Some greenhorns were playing army down there, so I chased them away. Do colleges still have hazing culture these days?” “Ah, I see.” “What was it? I made them do some PT exercises for a while, and they looked ready to die.” Team Leader 1 felt the suspicions he had been harboring vanish completely. *I must have been out of my mind. How dare I even think such a thing?* While he reflected deeply on his mistake, Im Chunsoo laid into the Security Team. “Security Team Leader.” “Y-yes, sir!” “Well, look at that. You certainly know how to answer. After causing this mess, are you still a Team Leader just because you’re technically still a Team Leader?” “I’m sorry, Guild Master!” “Are the others keeping their mouths shut because they did such a good job? Do you want me to make my sword dance today?” “We’re sorry, Guild Master!” Team Leader 1 watched the scene with a pleased smile. Every so often, there were people who spread the rumor that Im Chunsoo had a godawful personality. But after watching him up close, Team Leader 1 knew better. He was a charismatic superior and an outstanding Senior in life. *Guild Master. I’ll follow you forever.* As he gazed at Im Chunsoo’s back with boundless respect, Team Leader 1 suddenly cocked his head. *…But why is there dirt on the Guild Master’s back?* He must have scolded those kids rather intensely. * * * “We’ve arrived.” At Butler Kim’s words, sitting in the passenger seat, I came to my senses with a start and looked around. Through the window, I could see the entrance to an apartment complex. *When did we get here?* “Th-thank you.” “Don’t mention it.” A smile appeared on his handsomely lined face. He looked like a middle-aged actor who had once ruled an era. *No, this man really did rule an era, too.* Until now, I had thought of him as nothing more than a Senior Hunter from a distant generation. But that meant I hadn’t understood Butler Kim at all. *He worked an A-rank mage like a dog—and Im Chunsoo, no less.* He had made a former war hero do a hundred sets of PT Exercise No. 8, then later kicked him in the shin with his dress shoe. Even now, the way he had calmly berated Im Chunsoo in that gentle voice sent chills down my spine. *Trainee, who uses mana during PT exercises?* *Whack!* *Trainee Number One Im Chunsoo. S-sorry, sir.* *Does it hurt? Now that you’ve gotten older, has your voice gotten quieter, too?* *No, sirrrrr!* *Attention. At ease. Attention. At ease.* *Snap-snap-snap-snap!* *On your backs. On your fronts. On your backs. On your backs.* *Gasp.* *Trainee, didn’t you hear this Instructor say on your backs? Get your head straight.* *I’ll correct it, sirrrr!* *And why are you bullying an innocent junior? Hasn’t this Instructor told you time and again that Seniors and juniors should help each other?* *S-sorry, sir.* *Repeat after me. Cherish your junior on the way down. Cherish your junior on the way up. One. Two.* *Cherish my junior!* *Trainee, I remember you’re Class 25. Am I right?* *Trainee Number One Im Chunsoo. Yes, sir.* *This Instructor is Class 3. If what happened today gets out or happens again, Classes 4 through 24 will assemble without exception.* *…* *Why aren’t you answering? Prepare for squat jumps.* *P-prepare, sir…* He worked him over, and over, and over again. It was the kind of sight you couldn’t see even if you paid for it. If the Sangdong Guild members had witnessed it, the Guild might have had to close its doors that very day. *Who the hell is Butler Kim, really?* Being Class 3 at the Hunter Training Center meant he could line up every Guild Master in the country on a parade ground and beat every last one of them with a bat. And he had been an Instructor, no less. It wouldn’t be an exaggeration to say that nearly every mage from the early days of the Great Cataclysm had passed through his hands. *He’s at least A-rank as a mage, too.* I could tell just by watching Im Chunsoo take his punishment without daring to make a peep. Butler Kim surpassed him in both seniority and skill. There was probably also an elemental advantage between ice and fire. You could say Butler Kim was the one who taught Im Chunsoo and raised him to his current position. *But…* Why was someone that accomplished working as a butler? I stole a sidelong glance at Butler Kim, only for our eyes to meet. “You seem to have a lot you want to ask.” “To be honest, I do.” My curiosity was killing me. Seeing my thoughts written plainly across my face, Butler Kim curled up the corners of his mouth. “It’s a long story.” “That’s fine. I’m on vacation, so I have plenty of time.” “Ah, then this is a good opportunity to hear your story as well, Mr. Jin. I already have more than one or two questions myself.” “Now that I think about it, it’s already dinnertime. Tomorrow is the last day of my vacation, so I have to sign a real-estate contract, too. Hahaha.” “……”

## Korean source

```text
＃102화



사람마다 전문 분야가 다르기 마련이다.

게이트에서의 포메이션과 위기 상황이 닥쳤을 때 취해야 할 행동, 몬스터들의 약점 등을 달달 꿰고 있는 내가 법 관련 사항에서는 문외한인 것도 같은 맥락이었다.

“고생하셨습니다.”

“법무사님도요.”

각진 뿔테 안경을 쓴 이 남자는 내게 부동산 매매를 위임받은 법무사다. 맞은편에선 집주인과 공인중개사 아저씨가 인사를 나누며 막 자리에서 일어나고 있었다.

“계약 축하해요. 젊은 분이 성공하셨네.”

“아, 네. 감사합니다.”

집주인과 악수를 나누며 그제야 새로운 사실을 깨달았다.

‘이젠 내 집이구나.’

그리고 우리 가족의 집이다. 자그마치 11년 만에 되찾은.



* * *



좁은 방 안을 돌아봤다.

오래전 스프링이 나간 침대. 몇 벌 들어가지도 않는 작은 옷장과 군데군데 칠이 벗겨진 책상 하나. 그 위에 놓인 소형 TV.

두고 가야 할 것을 제외하고 옷이며 자질구레한 물건들을 주워 담으니 종이 박스 하나를 꽉 채웠다.

‘겨우 박스 하나.’

지난 7년이 그 안에 담겨 있다. 어쩐지 먹먹한 심정이 되어 하염없이 방을 둘러보고 있던 그때였다.

“가냐?”

굳이 돌아보지 않아도 알 수 있다.

내 7년에서 빼놓을 수 없는 사람이니까.

“응.”

“집은?”

“구했으니까 나가지.”

“새끼, 빠르네. 가족들은 이미 새집으로 이사했고?”

“아니. 아직까지는 비밀이야. 내가 먼저 들어가서 살다가 동생 수능 끝나면 알려 주려고.”

“하긴, 한창 중요한 시기니까.”

“응. 그 전에 리모델링도 해야 하고.”

잠깐 침묵이 흘렀다. 우리 둘은 굳이 대화를 나누지 않아도 편안한 사이, 눈빛만으로도 서로의 마음을 읽을 수 있는 사이지만 지금은 무슨 말을 해야 할지 모르겠다.

“형.”

“야, 야. 됐어. 분위기 잡지 마.”

진호 형이 내 등을 세게 두드렸다.

“무슨 전학 가는 초등학생도 아니고. 너 이사 가면 내 얼굴 안 볼 거냐?”

“봐야지. 꼭 봐야지.”

“그럼 됐어. 어차피 나도 오늘 중으로 짐 뺀다.”

“형도?”

“지난번에 말했잖아. 기억 안 나냐?”

“아, 그랬었지.”

몇 년씩이나 동고동락한 진호 형만 고시원에 두고 가는 게 마음에 걸렸는데, 이제야 한결 편해진다.

“형은 어디로 이사 가는데?”

“그냥 뭐 아는 사람 집에 얹혀살게 됐어. 너 이번에 산 집이 어디 있다고 했지?”

“고양시. 여기서 30분 거리라 그렇게 멀진 않아.”

“고양시?”

진호 형이 눈을 크게 떴다.

“나도 그 근처야, 인마!”

“어? 진짜?”

뜻밖의 이야기에 내심 반가웠다. 이제는 하루라도 안 보면 섭섭한 얼굴이다. 사는 곳이 가까우면 앞으로도 자주 만날 수 있겠지.

“형, 그럼 정확한 주소가 어디…….”

막 주소를 물어보려던 찰나, 주머니에 넣어 둔 스마트폰이 울렸다. 전화를 받으니 수화기 너머로 걸걸한 목소리가 흘러나온다.

- 어, 진태경 씨 맞죠? 지금 고시원 앞이에요.

“아, 예. 기사님.”

미리 불러 둔 개인 이삿짐 기사다. 흘끗 창문 밖을 바라보니 고시원 앞에서 기다리고 있는 파란색 용달차 한 대가 보였다.

- 짐 많아요? 무거운 거면 제가 도와드리고.

“아닙니다. 제가 들고 갈게요.”

짐이라고 해 봤자 두 개뿐이다.

소소한 물건들을 챙겨 넣은 종이 박스, 그리고…….

‘캡슐.’

로그아웃 기능이 활성화된 지금은 굳이 캡슐을 사용하지 않아도 무림과 현대를 넘나들 수 있다.

이제는 공간만 차지하는 애물단지가 됐지만 내게는 그 어떤 것보다 특별한 의미가 있었다. 짐이 별로 없는데도 용달차를 부른 것 역시 다 이거 때문이다.

‘이 캡슐이 아니었다면 어떻게 됐을까.’

천천히 캡슐 표면을 쓰다듬었다. 손을 통해 전해지는 금속의 차가움과 거칠거칠한 촉감.

이 낡은 캡슐 하나가 내 인생을 송두리째 바꿨다.

아, 맞다. 거기에 큰 역할을 해 준 사람도 있었지.

“진호 형.”

“응?”

어리둥절한 표정을 보고 있자니 실소가 절로 나온다.

그날, 진호 형이 술에 떡이 되지 않았더라면 내가 캡슐에 들어갈 일도 없었을 것이다.

“아냐, 아무것도.”

“싱겁기는. 그나저나 너 이제 가 봐야 하는 거 아니냐? 밖에 트럭 서 있던데.”

“어. 그런 김에 거기 박스 좀 들어 주라. 난 캡슐 들어야 해서 손이 부족해.”

“으, 응?”

“뭐야, 그 반응은? 이사 가는 동생을 위해서 박스 하나 못 들어 줘?”

“그게 아니고…… 어우, 생각해 보니까 나도 짐 싸야 되네. 귀찮아도 그냥 한 번 왔다 갔다 해라. 그럼 수고!”

“…….”

미꾸라지처럼 빠져나가는 것 보소. 나는 슬금슬금 멀어지는 진호 형의 뒷모습을 바라보다 결국 박스를 집어 들었다.

기다림에 지친 이삿짐 아저씨의 클랙슨 소리가 귀를 때린다.

빵빵!

“예, 지금 내려가요!”



* * *



“헌터신가 봐요?”

계속 나를 흘끗거리던 이삿짐 아저씨가 말을 던졌다. 박스와 캡슐을 실은 용달차는 내비게이션의 안내에 따라 새로운 집을 향해 달리고 있었다.

“어떻게 아셨어요?”

“그거야 보면 딱 알죠. 나도 예전에는 헌터였거든. F급.”

“어, 정말요?”

“아마 내가 손님보다 훈련소 기수로는 선배일걸? 아, 꼰대짓 하려는 건 아니에요. 딱 한 달 만에 때려치우고 자격증 반납한 놈이 그러는 것도 우습잖아.”

아저씨가 넋두리처럼 말을 이었다.

“헌터 훈련소 때는 할 만했어요. F급이지만 헌터가 된다는 자부심도 있었고. 그런데 수료 후에 길드 들어가자마자 사고가 터진 거지.”

게이트에서 사고가 터졌다는 말은 사망과 동의어다.

설령 팔다리가 날아가도 돈만 있다면 회복할 수 있는 세상이니까. 헌터들끼리는 그 정도를 사고라고 말하진 않는다.

“같이 입사한 훈련소 동기 녀석이었는데…… 어어, 하는 사이에 끌려가더니 그렇게 죽었어. 무슨 수를 써서라도 쫓아가서 구했어야 했는데 차마 발이 안 떨어지더라고. 그 녀석 장례식 마치고 은퇴 신청했지. 나 같은 놈은 레이드 뛰면 안 되니까.”

그는 애써 덤덤한 척하려 했지만 잘게 떨리는 목소리까지 감추지는 못했다.

“이거 헌터 손님 앞에서 너무 재수 없는 소리를 했네. 이게 뭐 좋은 얘기라고. 미안합니다.”

“별말씀을요.”

아저씨의 심정이 충분히 이해가 갔다.

나도 비슷한 경험이 있었으니까. 가족에 대한 책임감이 없었다면, 옆에서 위로해 준 진호 형이 없었다면 2년 전 그때 은퇴했을지도 모른다.

‘그럼 내 인생도 크게 달라졌겠지.’

헌터는 치열한 직업이다. 언론에서는 인류의 수호자요, 방패라며 치켜세워 주지만 늘 죽음을 옆에 끼고 살아간다.

- 50m 앞에서 우회전입니다.

내비게이션의 안내 음성에 아저씨가 멈칫하더니 중얼거렸다.

“어, 그러고 보니까 여기 안전 구역이네.”

“맞으니까 쭉 가 주세요.”

“아, 예.”

용달차는 얼마 지나지 않아 목적지에 도착했다.

푸른색 지붕의 2층짜리 단독주택. 너무 높지 않은 돌담과 잔디가 깔린 마당이 보인다. 이 집을 처음 봤던 며칠 전과는 또 느낌이 달랐다.

‘우리 집이라 그런 거겠지.’

우리 집.

곱씹을수록 기분 좋은 말이다. 물론 집이 워낙 예뻐서 그런 것도 있겠지만.

“이야…… 집 좋네.”

운전석에서 내린 아저씨가 혀를 내둘렀다. 다른 사람의 입에서 나오는 소리는 더 달콤하게 들리는 법. 참으려고 해도 자꾸 입꼬리가 올라간다.

“잘나가는 헌터인가 봐요. 내 꿈이 이런 집에서 사는 거였는데.”

“저도요.”

“소원 성취 하셨네. 좋으시겠어.”

당연히 좋아 죽지.

연신 감탄사를 터트리며 돌담도 만져 보고, 잔디밭도 바라보던 그가 물었다.

“잠깐 들어가서 구경해 봐도 될까요? 캡슐도 옮겨 드릴 겸.”

“네, 그러세요.”

의도치 않게 새집의 첫 손님이 된 이삿짐 아저씨가 짐칸으로 올라갔다. 캡슐을 옮기기 위해서다.

“그런데 그거 무게가 꽤 나갈 텐데.”

“괜찮아요. 저도 많이 옮겨 봐서 알아요. 게임 캡슐 무게야 거기서 거긴데요 뭘.”

“아니, 진짜 무거울 건데.”

아까 직접 들어 봐서 안다. 근력 스탯이 세 자리가 넘어가는 나한테도 적당히 묵직한 정도였는데 저 아저씨라면 더더욱 얘기가 다르다.

“사장님, 그냥 제가 옮길게요.”

캡슐을 끌어안은 그가 씩 웃었다.

“에헤이. 너무 무시하신다. 내가 그래도 왕년에 헌터였는데 겨우 이 정도로…… 끄응!”

“오오.”

역시 전직 헌터. 한 번에 들긴 들었다.

약간 변한 게 있다면 아저씨의 얼굴에서 웃음이 사라졌다는 것 정도?

“먼저 가서 문 열어요. 빨리!”

긴박한 목소리에 후다닥 달려가 대문과 현관문을 열어젖혔다. 이게 뭐라고 나까지 긴장되는지 모르겠다.

“그냥 제가 들…….”

“비켯!”

“아, 네.”

경보에 버금가는 속도로 거실에 들어간 그가 비명처럼 외쳤다.

“어느 방!”

“캡슐은 2층…….”

“뭣이?”

“……에 놓으려고 했는데 그냥 가까운 방에 놔 주세요.”

다행히 방문은 열려 있었다. 쿵, 소리와 함께 캡슐을 내려놓은 아저씨가 숨을 헐떡였다.

“이거, 왜, 이렇게, 허억. 무거워요?”

“…….”

내가 무겁다고 말해 주지 않았나?



* * *



이삿짐 아저씨가 떠나자마자 거실 소파에 털썩 걸터앉았다.

한 번에 잔금을 지급하는 조건으로 전 주인에게 양도받은 가구 중 하나다.

‘몇 달 동안은 혼자 살아야 하니까.’

가족들에게는 다시 부천으로 돌아간다고 말해 둔 상태.

하연이의 수능 전까지는 이곳에서 먹고 자며 출퇴근을 할 작정이다.

‘집 리모델링도 하고, 차도 사고. 아, 어차피 차는 길드에서 지원해 준다고 했으니 면허부터 따야겠구나.’

그밖에도 할 일이 태산이다. 그러나 지치기는커녕 힘이 솟았다. 전에는 하고 싶어도 못 했던 일들이니까.

게이트와 고시원을 오가며 고생만 하던 게 불과 몇 달 전인데, 참 많은 게 바뀌었다.

‘많이 컸다, 진태경.’

문득 생각나는 한 사람이 있다.

적지 않은 나이에도 늘 소년처럼 웃던 사람. 아내에게, 자식들에게 최선을 다하며 친구처럼 다가와 주었던 그가 떠오른다.

‘아버지, 나 집 샀어요. 예전에 우리가 살던 곳은 이미 없더라고. 그래도 이 정도면 잘한 거 맞죠?’

아이처럼 자랑하고 싶어도 칭찬해 줄 사람은 이미 오래전에 떠났다. 내가 할 수 있는 거라곤 마음속으로 닿지 않을 말을 되뇌는 것뿐이었다.

그렇게 시간이 얼마나 흘렀을까?

정신을 차려 보니 벌써 오후 여덟 시. 여름철의 해가 서서히 저물고 있었다.

‘휴가 마지막 날이 이렇게 끝나네.’

장장 일주일의 휴가. 상동 길드와 엮여 소란스럽기도 했지만 헌터 생활을 시작한 이래 처음으로 누리는 최고의 휴식이었다.

이제는 다시 일상으로 돌아가야 할 시간이다.

‘정확히 열두 시간 후에 말이지.’

앉아 있던 소파에 반듯이 누웠다. 캡슐에 들어갈까 하는 생각도 들었지만 이내 지워 버렸다.

11년 만에 돌아온 집이다. 이번만큼은 후덥지근한 캡슐 안이 아니라 우리 집 거실에서 깨어나고 싶었다.

‘로그인(Login).’

내 부름에 시스템이 응답한다.

띠링.



[무림]에 접속하시겠습니까?

Y   /   N



물론 내 대답은 예스다.



* * *



진태경이 의식을 잃은 지 한참 후, 현관문 옆 방 안에서는 누구도 예상 못 한 일이 벌어지고 있었다.

치이이익.

마치 거대한 알처럼 보이는 금속 물체, 캡슐의 문이 천천히 열리기 시작한 것이다.

가장 먼저 드러난 것은 두 발이었다.

종아리까지 덮는 긴 스포츠 양말에 프린팅된 붉은 글씨.



희망 고시원 조기축구회



이어 반쯤 말아 올린 추리닝 바지를 지나 희고 마른 양손까지 드러났다. 성서라도 되는 것처럼 꼭 붙잡고 있는 책 표지가 창밖으로 흘러들어온 노을빛을 받아 번쩍 빛난다.



행정고시 완전 정복



그리고 마침내 드러나는 그의 얼굴.

장장 몇 시간의 고통을 인내한 그는 사도세자처럼 초췌했으나 알을 깨고 태어난 박혁거세처럼 후련해 보였다.

바짝 마른 입술 사이로 메마른 음성이 새어 나온다.

“이곳이 나의 새로운 보금자리인가…….”

넓은 방을 바라보는 성진호의 입가에 흐뭇한 웃음이 맺혔다.
```

## Current accepted English baseline

```markdown
# Chapter 102

Everyone has their own area of expertise.

I knew the formations used at Gates, what to do when a crisis struck, and the weaknesses of various monsters like the back of my hand. My being clueless about legal matters was simply another example of everyone having their own specialty.

“Thank you for your hard work.”

“You too.”

The man in the angular horn-rimmed glasses was the legal scrivener I had hired to handle the real-estate transaction. Across from me, the homeowner and the licensed realtor were exchanging farewells and getting to their feet.

“Congratulations on the contract. A young man making it big.”

“Ah, yes. Thank you.”

As I shook hands with the homeowner, I realized something for the first time.

*This is my house now.*

And it was my family’s house.

A home we had reclaimed after no less than eleven years.

* * *

I looked around the cramped room.

The bed, whose springs had broken long ago. A small wardrobe that could barely hold a few outfits. A desk with its paint peeling off in places. A small TV sitting on top of it.

After packing up my clothes and assorted belongings, excluding the things I had to leave behind, I filled one cardboard box.

*Just one box.*

The past seven years were contained inside it. I was staring around the room with a strange tightness in my chest when a voice came from behind me.

“You leaving?”

I knew who it was without turning around.

He was someone I couldn’t leave out of my seven years.

“Yeah.”

“What about the house?”

“I found one, so I’m moving out.”

“Bastard, that was fast. Has your family already moved into the new place?”

“No. It’s still a secret. I’m planning to move in first and tell them after my sister finishes her college entrance exam.”

“Fair enough. She’s at an important stage.”

“Yeah. I need to remodel the place first, too.”

A brief silence followed. We were comfortable enough not to need conversation, the kind of people who could read each other’s thoughts from a look alone. But right now, neither of us seemed to know what to say.

“Hyung.”

“Hey, hey. Don’t set the mood.”

Jinho hyung slapped me hard on the back.

“It’s not like you’re an elementary school kid transferring schools. Just because you’re moving, you’re not going to stop seeing me, are you?”

“Of course I’ll see you. I definitely will.”

“Then it’s fine. Besides, I’m moving my stuff out by the end of today, too.”

“You are?”

“I told you last time. Don’t you remember?”

“Oh, right. You did.”

I had felt bad about leaving Jinho hyung alone in the goshiwon after all the years we had spent living together. Now I finally felt a little more at ease.

“Where are you moving?”

“Well, I ended up crashing at someone I know’s place. Where did you say the house you bought was?”

“Goyang. It’s only thirty minutes from here, so it’s not that far.”

“Goyang?”

Jinho hyung’s eyes widened.

“I’m in that area too, you punk!”

“Huh? Really?”

I was secretly pleased by the unexpected news. By now, his was a face I felt lonely not seeing for even a single day. If we lived close by, we could keep meeting often.

“Hyung, then where exactly is your address—”

Just as I was about to ask, the smartphone in my pocket rang. When I answered, a gravelly voice came from the other end.

—Hello, is this Mr. Jin Taekyung? I’m in front of the goshiwon right now.

“Ah, yes. Driver.”

It was the private moving-truck driver I had called in advance. I glanced out the window and saw a blue light truck waiting in front of the goshiwon.

—Do you have a lot of luggage? If anything’s heavy, I can help you carry it.

“No, it’s fine. I’ll carry it myself.”

I only had two things to move.

A cardboard box filled with small belongings, and…

*The capsule.*

Now that the Logout function had been activated, I no longer needed to use the capsule to travel between the Murim and modern worlds.

It had become nothing more than a bulky nuisance, but it held a more special meaning for me than anything else. That was the entire reason I had called a moving truck despite having so little luggage.

*What would have happened if I hadn’t had this capsule?*

I slowly ran my hand over its surface. The coldness of the metal and its rough texture traveled through my fingers.

This one old capsule had completely changed my life.

*Oh, right. There was also someone who played a major role in that.*

“Jinho hyung.”

“Yeah?”

I couldn’t help letting out a quiet laugh at his puzzled expression.

If Jinho hyung hadn’t gotten dead drunk that day, I never would have had a reason to enter the capsule.

“Never mind. It’s nothing.”

“You’re no fun. Anyway, shouldn’t you get going? There’s a truck waiting outside.”

“Yeah. Since you’re here, carry that box down for me. I have to carry the capsule, so I’m short on hands.”

“Uh, what?”

“What’s with that reaction? Can’t you carry one box for your little brother who’s moving away?”

“That’s not it… Ah, now that I think about it, I need to pack my own stuff too. Even if it’s a hassle, just make one trip back and forth. Well, good luck!”

“……”

Look at him slither away like a loach.

I watched Jinho hyung’s back as it slowly disappeared into the distance, then eventually picked up the box myself.

The moving driver, tired of waiting, honked the truck’s horn. The sound struck my ears.

Honk, honk!

“Yes, I’m coming down!”

* * *

“Are you a Hunter?”

The moving driver, who had been sneaking glances at me, finally spoke. The light truck, carrying the box and capsule, was heading toward my new home according to the navigation.

“How did you know?”

“You can tell at a glance. I used to be a Hunter, too. F-rank.”

“Oh, really?”

“I’m probably your Senior by training-center class. Ah, I’m not trying to pull rank. It would be ridiculous for a guy who quit after exactly one month and handed back his license to act like some old-timer.”

The driver continued, sounding as though he were simply airing a long-held grievance.

“Being a Hunter at the training center was manageable. Even though I was only F-rank, I took pride in becoming a Hunter. But the moment I joined a Guild after graduating, an accident happened.”

An accident at a Gate was synonymous with death.

Even if someone lost an arm or a leg, they could recover as long as they had enough money. Hunters didn’t call something that minor an accident.

“He was one of my training-center classmates, and he joined the Guild at the same time as me… Before I knew what was happening, he was dragged away and died just like that. I should have chased after him and saved him, no matter what it took, but I just couldn’t make myself move. After his funeral, I applied for retirement. Someone like me shouldn’t be going on raids.”

He tried to sound calm, but he couldn’t hide the tremor in his voice.

“I said something awfully ominous in front of a Hunter customer. It’s not exactly a pleasant story. Sorry about that.”

“Don’t worry about it.”

I understood how he felt.

I had experienced something similar. If I hadn’t felt responsible for my family, and if Jinho hyung hadn’t been there to comfort me, I might have retired two years ago.

*Then my life would have turned out completely differently.*

Being a Hunter was a brutal profession. The media praised them as humanity’s guardians and shields, but they lived with death always at their side.

—Turn right in fifty meters.

The driver flinched at the navigation’s voice, then muttered,

“Oh, come to think of it, this is a safe zone.”

“That’s right. Just keep going.”

“Ah, yes.”

The light truck arrived at its destination soon afterward.

It was a two-story detached house with a blue roof. A low stone wall surrounded a yard covered in grass. The house felt different from when I had first seen it a few days ago.

*It must be because it’s ours now.*

Our house.

The more I repeated those words in my head, the better they sounded. Of course, the fact that the house itself was beautiful probably helped.

“Wow… It’s a nice house.”

The driver climbed out of the cab and clicked his tongue in admiration. Praise sounded sweeter coming from someone else. No matter how hard I tried to suppress it, the corners of my mouth kept rising.

“You must be a successful Hunter. My dream was to live in a house like this.”

“Mine too.”

“Your wish came true. You must be happy.”

*Of course I was ecstatic.*

The driver continued exclaiming over the place, touching the stone wall and looking over the lawn, before asking,

“Would it be all right if I took a quick look inside? I can help move the capsule while I’m at it.”

“Sure. Go ahead.”

The moving driver became the new house’s first guest by accident as he climbed into the truck’s cargo bed.

He was going to move the capsule.

“That thing must weigh quite a bit.”

“It’s fine. I’ve moved plenty of them, so I know. Game capsules are all roughly the same weight.”

“No, it’s seriously heavy.”

I knew because I had lifted it myself earlier. It had been moderately heavy even for me, with my Strength stat in the triple digits. For the driver, it would be a different story entirely.

“Boss, I’ll move it myself.”

The driver hugged the capsule and grinned.

“Come on. You’re underestimating me. I may be an ex-Hunter, but something like this shouldn’t—nnngh!”

“Oh, wow.”

As expected of a former Hunter, he did manage to lift it in one go.

The only thing that had changed was that the smile had disappeared from his face.

“Go ahead and open the doors. Quickly!”

His voice suddenly urgent, I hurried over and threw open the front gate and the house’s entrance door. I had no idea why this had me feeling tense, too.

“I can carry it—”

“Move!”

“Ah, yes.”

He charged into the living room with the urgency of an alarm and shouted like he was screaming for his life.

“Which room?!”

“I was going to put the capsule upstairs…”

“What?!”

“…but just leave it in the nearest room.”

Fortunately, the door to one of the rooms was already open. With a heavy thud, the driver set down the capsule and began panting.

“Why… why is this… huff… so heavy?”

“……”

Hadn’t I told him it was heavy?

* * *

As soon as the moving driver left, I dropped onto the living room sofa.

It was one of the pieces of furniture the previous owner had transferred to me on the condition that I pay the remaining balance all at once.

*I’ll have to live alone for a few months.*

I had told my family that I was going back to Bucheon.

Until Hayeon finished her college entrance exam, I planned to eat and sleep here and commute to work.

*I need to remodel the house and buy a car, too. Ah, the Guild said they’d provide the car anyway, so I need to get my license first.*

There was a mountain of other things to do. But instead of feeling tired, I felt energized. These were all things I hadn’t been able to do before, no matter how much I wanted to.

It had only been a few months since I had done nothing but suffer while going back and forth between Gates and the goshiwon, yet so much had changed.

*You’ve come a long way, Jin Taekyung.*

One person suddenly came to mind.

A man who had always smiled like a boy despite his age. A man who had done his best for his wife and children and approached them like a friend.

*Dad, I bought a house. The place we used to live in was already gone. But I did well enough, right?*

I wanted to brag about it like a child, but the person who would have praised me had passed away long ago. All I could do was repeat, in my heart, words that could no longer reach him.

How much time passed like that?

When I came to my senses, it was already eight in the evening. The summer sun was slowly sinking.

*So this is how my last day of vacation ends.*

An entire week of vacation. It had been hectic because of everything involving the Sangdong Guild, but it was still the best rest I had enjoyed since becoming a Hunter.

Now it was time to return to my daily life.

*Precisely twelve hours from now.*

I lay flat on the sofa where I had been sitting. I briefly considered entering the capsule, but soon dismissed the thought.

After eleven years, I finally had a home of my own again. Just this once, I wanted to wake up in our living room instead of inside the stuffy capsule.

*Login.*

The System responded to my call.

Ding.

> **System**
>
> Would you like to connect to Murim?
>
> Y / N

Of course, my answer was yes.

* * *

A long time after Jin Taekyung lost consciousness, something no one could have expected was taking place in the room beside the front door.

Hissssss.

The door of the metal object that looked like a gigantic egg—the capsule—slowly began to open.

The first thing to emerge was a pair of feet.

Red letters were printed across a pair of long athletic socks that reached up to the calves.

**Hope Goshiwon Early-Morning Soccer Club**

Next came sweatpants rolled up halfway to the knees, followed by a pair of pale, skinny hands. The cover of the book he clutched tightly, as though it were scripture, gleamed in the sunset pouring through the window.

**Complete Mastery of the Civil Service Exam**

And finally, his face emerged.

After enduring several long hours of agony, he looked as haggard as Crown Prince Sado[^1] yet as relieved as Park Hyeokgeose emerging from an egg.[^2]

A parched voice slipped between his bone-dry lips.

“Is this my new nest…?”

As Seong Jinho gazed around the spacious room, a satisfied smile spread across his lips.

[^1]: Crown Prince Sado was an eighteenth-century Joseon royal who died after being confined in a wooden rice chest.

[^2]: Park Hyeokgeose is the legendary founder of the ancient Korean kingdom of Silla, said to have been born from an egg.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 102`.

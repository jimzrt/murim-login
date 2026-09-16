# Master Edit Task — Chapter 101

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
| 김화종    | **Kim Hwajong**   |
| 임춘수    | **Im Chunsoo**    |
| 살기     | **killing intent**                               |                                                       |
| 창기     | **Spear Energy**                                 | Explicit system skill for Taekyung                    |
| 선배     | **Senior**                                   |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |
| 임춘수 | 김화종 | former_trainee_to_former_instructor | Instructor | deferential and fearful | Im Chunsoo addresses Hwajong as 교관님 after recognizing his former instructor. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

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

#### Chapter 99 tail (verified mastered)

…
he shouldn’t get involved any further. *Sangdong Guild, you goddamn thugs.* Clicking his tongue, Hong Woojin pulled out his smartphone and sent a text. The recipient was the Team 1 Leader. The message was short and simple. > **Team 1 Leader** > > I’m dropping the job. Before leaving the rooftop, he didn’t forget to pray for the already-vanished Jin Taekyung’s soul. *Well, that was filthy. Let’s never see each other again.* In every possible way, the job had brought him nothing but bad luck. * * * I climbed the mountain path in silence. I had left the hiking trail behind long ago. But I didn’t stop. I kept walking deeper and deeper into the mountain. At some point, a broad clearing came into view. Weeds had grown thick there, reaching up to my knees. I slowly turned around. “Looks like you’re still out for a walk?” Kim Gwondong, the middle-aged man I had run into twice before, said nothing. His face hardened. “No answer? Who’s the man beside you?” “A friend.” If Kim Gwondong had the sort of ordinary face you could see anywhere, the man who answered was his complete opposite. He was huge, with a vicious face fierce enough to make gangsters cry. A gravelly voice rumbled from between his lips. “You already know everything, so why did you come all the way here?” “You kept trailing me from behind, so I wanted to see how far you’d follow. Think of it as training a mutt.” The man burst into a hearty laugh. “Young punk’s got nerve. How old are you?” “*Yeokmasal*.”[^2] “You’ve got a real talent for asking for a beating.” “Thanks for the compliment, Mr. Choi Byungil.” The man, Choi Byungil, closed his mouth. His eyes wavered. “…How did you know?” “That’s a trade secret. But are you and Mr. Kim Gwondong really friends? Judging by appearances, you two don’t exactly look like a matching pair.” This time, it was Kim Gwondong’s turn to panic. But I wasn’t finished. “Is that hard to answer because you’re not friends? Then I’ll ask the other four. Mr. Park Hyungjin, Mr. Oh Gyuhyeon, Mr. Lee Mincheol, and Mr. Kim Junsu, I’d appreciate an honest answer.” Bzzzzzz. The air rippled, and four people dropped straight down. Each had a Level window floating above his head, and all four looked like they’d seen a ghost. “Why is everyone so surprised? I was just being considerate so you could breathe easy.” Choi Byungil gritted his teeth. All traces of his earlier composure had vanished, leaving his face colored by anxiety and bewilderment. “What the fuck… What kind of bastard are you?” He had cursed first, so that was the end of respecting my elders. I gave a quiet laugh as I looked at Choi Byungil. “You still don’t know? You must have dug up every scrap of information about me. If you went so far as to attach Familiars, that says everything.” “…!” “I could’ve let it go if I’d been alone at home. But the thought of my family being watched too pissed me off. So I threw out some bait, and you snapped it right up.” The six watchers trembled. “Th-then the USB…” “Oh, that? It’s the porn collection I’ve spent my whole life assembling.” A treasure of humanity, carefully preserved in my Inventory. “No way! I definitely had a feeling!” “Well, there are plenty of works in there that defy belief. And any man would get a gut feeling about it.” I addressed the six of them as they stood there looking utterly crushed. “You answered honestly, so let me ask you one thing, too.” One by one, they flinched whenever their eyes met mine. At last, my gaze settled on a painfully skinny man in his twenties. He was probably the Familiar mage. > **System** > > Level 41 Kim Junsu “Junsu. Sangdong Guild sent you, didn’t they?” “Shut your mouth!” Choi Byungil shouted, but Kim Junsu had already answered. His bloodless, ashen face was answer enough. “Okay, Sangdong Guild. I figured as much.” Choi Byungil’s face stiffened at my words. “You shouldn’t have said that name out loud.” “Why? You going to kill me?” “…I’ll capture you first. Then I’ll think about it.” “That’s going to be pretty hard.” Choi Byungil’s Level was in the mid-sixties. His aura was comparable to Im Changsoo’s, while the rest were unremarkable C-ranks around Levels 30 or 40. The odds of a group that wasn’t even a professional raid team managing to capture me were extremely low. “Come at me prepared to die. That’s the only way you’ll manage to tie so much as a butterfly knot around my wrist.” “Get him!” At Choi Byungil’s shout, the Sangdong Guild watchers began charging at me from all directions. Whoosh! The opening move was a dagger dropping toward my shoulder. I reached toward the trajectory that looked slow to me. At the same time… *Inventory open. Equip.* Crunch! The blade, brimming with internal energy, shattered the enemy’s dagger. Shards of metal and someone’s blood spilled across the nameless weeds. “Come on, you stalker bastards!” Ssshhhhh! [^1]: *Pyeong* is a traditional Korean unit of floor area; five pyeong is roughly 16.5 square meters. [^2]: *Yeokmasal* is a traditional Korean notion of a fate that compels someone to wander. Here it also puns on *sal*, the Korean word used when asking someone’s age.

#### Chapter 100 tail (verified mastered)

…
“Jin Taekyung. That’s you, isn’t it?” “Well, yes, but… who are you?” “My name is Im Chunsoo. I heard you have a few of my people with you.” “…” “Are you listening?” I was listening. I just couldn’t speak. The Guild Master of a mid-sized Guild had come all the way here himself to meet me. And it was Im Chunsoo, of all people—the man notorious for his temper. “Come down. We can clear up any misunderstandings over a meal.” There was no misunderstanding to clear up, but I had no idea what would happen if I said, *No.* Hadn’t the man already found out my location? In the end, I had only one option. “I’ll come down now.” * * * Im Chunsoo made a powerful first impression. He was younger than I had expected, and although his eyes seemed gentle, they burned with heat. *Fiery.* Ironically, that was my first thought upon meeting a master of ice magic. “Hello. I’m Jin Taekyung.” “I’m Im Chunsoo.” Unlike his burning gaze, his voice was cold. At last, he seemed like someone who deserved the nickname Frozen. “It’s strange seeing in person a face I’ve only seen in report photos.” There were actually people who could admit so bluntly and without embarrassment that they had dug into my background. “What about my people?” “They’re upstairs.” “Any fatalities?” “Of course not. I’d hate to become a criminal.” “I appreciate that.” Im Chunsoo gave me a slight nod. “My people got impatient and made a mistake. Can you let it slide?” “If there’s reasonable compensation.” Im Chunsoo gave a short laugh, while the man beside him, who looked like a Team Leader, frowned. “Young man, you have no manners.” “I can be like that… but it feels a little strange hearing it from the people who put me under surveillance.” “Even so—” The man couldn’t continue. Im Chunsoo raised a hand to stop him. “Team Leader 1, go upstairs and release my people.” “…Yes, Guild Master.” If Kim Butler possessed a gentle charisma, this man possessed a rough one. Maybe it was because they were both mages. Somehow, the two men overlapped in my mind. “Come take a walk with me.” Im Chunsoo went ahead, and I followed behind him. “Do you know something?” After walking briskly for a while, Im Chunsoo suddenly spoke. “Once I have a grudge against someone, I have to see it through to the end. I don’t know about you, but that’s the kind of person I am.” *Very Murim of him.* The strong devour the weak. Survival of the fittest. It seemed this man had the blood of a Murim tough guy running through his veins, too. “That’s how I built the Sangdong Guild. I climbed higher by stepping on what I had brought down and salvaging whatever I could.” “I see.” “What about the Peace Guild?” “…What do you mean?” “The past decade has been dull. We’re allies with every nearby Guild, and we haven’t had a rival for a long time. Then you people appeared.” I looked into his eyes, where curiosity and passion seemed to boil, and had only one thought. *This is dangerous.* Im Chunsoo continued, regardless. “Your Guild Master and Team Leader are people even I can’t easily access information on… But more than anything, your existence has stirred me up.” We were climbing a hill now. Despite his considerable age, Im Chunsoo didn’t seem short of breath. “Do you know why I came all the way here?” “To see me.” “You’re only half right.” Im Chunsoo’s footsteps stopped. Slowly turning around, he released a frigid chill from his entire body. > **System** > > Level 75 Im Chunsoo “At my age, time is money. I’m not so extravagant that I’d come all the way here just to see your face.” Frozen. The seasoned A-rank mage who had fought his way through the Great Cataclysm himself. The moment he extended his hand toward me— Hissssss. A dozen or so ice spikes formed in the empty air above my head. The midsummer air froze, and frost settled over the scorching dirt path. *I’d been well and truly caught.* I had thought he was an old man with some sense of propriety. I never imagined he would launch straight into something like this. “Do you really have to go this far?” “I’m going this far because it’s you.” “I’m only a C-rank.” “Exactly. Let’s see what that C-rank Hunter can do.” The moment he finished speaking, Im Chunsoo clenched his fist. The ice spikes, streaming with biting cold, shot toward me. Whoosh! But they couldn’t even touch the hem of my clothes. “Rise up. Fire Wall.” At the sound of a clear voice, the mana permeating the air began to churn. The ground, which had been frosted over by Im Chunsoo’s magic, melted as flames surged upward. Fwoosh! Roar! It was a wall of fire in the most literal sense. Blue flames swallowed the ice spikes and split the space between Im Chunsoo and me. Beyond the wavering flames, Im Chunsoo cried out in shock. “This is…!” But I wasn’t looking at Im Chunsoo. A man standing behind him at the entrance to the hiking trail greeted us in a gentle voice. “I’m glad I’m not late. You too, Chunsoo.” > **System** > > Level 80 Kim Hwajong Kim Hwajong. Kim Butler had arrived.

## Korean source

```text
＃101화



‘뭐야, 이거.’

어안이 벙벙했다. 김 집사의 등장도 뜻밖이지만 그가 임춘수를 향해 건넨 말에 비하면 아무것도 아니다.

‘춘수? 자네?’

두 사람 아는 사이였어?

생각해 보면 김 집사와 임춘수는 공통점이 많았다. 나이도 엇비슷하고 헌터 경력도 오래됐다.

‘그러고 보니 김 집사도 대격변 때 헌터로 활동했지.’

당사자의 입으로 직접 들은 건 아니지만 내심 짐작하고 있었던 사실이다. 두 사람을 번갈아 쳐다보던 나는 조심스럽게 물었다.

“두 분, 친하세요?”

임춘수의 눈동자가 파르르 떨렸다.



* * *



처음 평화 길드에 관한 보고서를 받았을 때, 임춘수는 자신의 눈을 의심했다.

흐릿한 기억 속에 남아 있는 얼굴, 다시는 볼 수 없을 거라 확신했던 얼굴이 보고서 속 사진에 있었기 때문이었다.



‘이, 이 자가 누구라고?’

‘평화 길드 마스터 김화종. 나이는 55세. B급 헌터입니다.’

‘김화종? B급 헌터?’

‘예. 혹시 무슨 문제라도?’

‘아, 아니야. 전에 알던 사람이랑 닮아서 착각했어.’



그럼 그렇지. 임춘수는 안도의 한숨을 내쉬었다.

얼굴이 약간 닮긴 했지만 그것뿐이다. 무엇보다 그자는 이미 30여 년 전 죽지 않았나.

아무리 세상이 요지경이 됐다지만 죽은 자가 살아 돌아올 수는 없다.

‘설령 그 인간이 살아 돌아왔어도 이런 곳에서 썩고 있진 않겠지. 늙다리 B급 헌터랑 착각한 것뿐이야.’

그날, 임춘수는 오랜만에 소주를 한 잔 걸치며 찜찜한 마음을 털어 냈다. 50이 넘도록 그의 발목을 붙잡고 있는 끔찍한 기억들을 떨치려는 시도였다.

‘어후, 이 나이 먹고도 아직 이러고 있다니.’

이후 김화종의 정보에 철통같은 보안이 걸려 있다는 얘길 들었을 때는 등줄기가 서늘하기까지 했었다.

‘설마? 아냐. 그럴 리가 없지.’

하지만…… 왜 불길한 예감은 틀리는 법이 없을까?

“솟구쳐라. 파이어 월.”

주문을 영창하는 나직한 목소리가 들림과 동시에 솟아오른 불의 장벽.

화륵, 화아악!

초고온의 청염(靑炎)이 강철보다 단단한 얼음송곳을 흔적도 없이 증발시켰다.

그리고…….

“늦지 않아서 다행입니다. 춘수, 자네도.”

꿈에서도 잊을 수 없던 목소리를 듣는 순간, 임춘수는 떠올렸다. 놈에게 지배당했던 공포를. 살기 위해 굴렀던 굴욕을.

‘시발…… 좆 됐다.’

돌처럼 굳은 그에게 진태경이 묻는다.

“두 분, 친하세요?”

뭐? 친하냐고?

임춘수는 폐부 깊숙한 곳에서 올라오려는 쌍욕을 꿀꺽 삼키고 돌아섰다. 오래전 죽었다고 생각했던 한 사람이 그곳에 있었다.

“교, 교관님.”

김 집사가 부드럽게 웃었다. 시간이 흐른 지금까지도 임춘수의 뇌리 깊숙이 새겨진 악마의 웃음.

“28연대 1대대 2중대. 임춘수. 그래, 처음 보자마자 알았지.”

그것은 영혼의 울림이었다.

임춘수의 구부정했던 허리가 펴지고 바짝 붙인 발은 45도. 시선은 전방 15도 위를 향한다.

번개처럼 빠른 동작 끝에 천둥 같은 외침이 터져 나왔다.

“1번 훈련생! 이임! 추운! 수우!”

30년 만에 외치는 관등성명에 산이 들썩였다.



* * *



산 위로 올라간 1팀장이 발견한 것은 핏물이 군데군데 튄 풀숲과 마법 밧줄로 꽁꽁 묶인 보안팀이었다.

‘정말 가관이군, 가관이야.’

내심 혀를 찬 그가 검을 꺼내 밧줄을 끊었다.

다들 피는 좀 흘렸어도 심각한 부상을 입은 것 같아 보이지는 않는다. 진태경이라는 놈이 최소한의 신경은 써 준 모양이었다.

‘이 정도면 B급 최상위. 혹은 A급 헌터.’

1팀장의 판단으로 진태경의 실력은 그 정도 되는 듯했다.

그 후 산에서 내려오는 길은 누군가에게는 지옥 같은 시간이었다.

“왜 그랬습니까? 감시 정도야 어떻게 넘기겠지만 오늘 일은 살인미수까지 갈 수도 있어요. 뒷일은 생각하고 일을 벌인 겁니까?”

“……죄송합니다.”

1팀장의 말에 보안팀장이 고개를 푹 숙였다.

무리수까지 둬 가며 무력행사에 나섰는데 도리어 진태경에게 탈탈 털렸다. 입이 열 개라도 할 말이 없는 상황이다.

“길드장님께서 단단히 실망하셨습니다.”

“그, 그럼?”

“시말서에 감봉은 당연한 거고 그 이상까지 각오해 두세요.”

“사직, 입니까?”

“그거야 길드장님 뜻에 달린 거죠.”

“……저, 팀장님. 혹시.”

“미리 말해 두는데, 괜한 청탁 같은 건 하지 않길 바랍니다. 내가 다니는 직장 이름에 똥칠한 사람을 편드는 취미는 없어서요. 길드장님 뜻에 반대할 생각도 없고.”

“…….”

“후우.”

1팀장이 짜증 섞인 한숨을 내쉰 그때였다.

저 멀리서 울려 퍼지는 쩌렁쩌렁한 외침.

- 1번 훈련생! 이임! 추운! 수우!

“……?”

“……?”

뭐지? 환청인가?

1팀장은 물론이고 죽을상을 하고 있던 보안팀원들까지 화들짝 놀랐다. 가장 먼저 정신을 수습한 건 보안팀장이었다.

“저기, 1팀장님. 이런 분위기에서 죄송합니다만, 방금 길드장님 목소리를 들은 것 같은데요.”

귀를 후비고 있던 1팀장이 눈을 동그랗게 떴다.

“……보안팀장도 들었어요?”

“저희도 들었는데요.”

“근데 길드장님 목소리인지는 잘 구분을 못 하겠고…… 성함은 들은 것 같습니다.”

“그게 사람 이름이었어? 난 그냥 악쓰는 소리 같던데.”

“그런가? 나는 관등성명 대는 것처럼 들렸는데.”

보안팀의 쑥덕거림을 듣던 1팀장이 정색했다.

“방금 말한 사람 누굽니까? 뭐, 관등성명?”

그에게 있어 임춘수는 존경하는 선배이자 상관이었다.

대격변 때부터 활동한 불세출의 헌터이자 전쟁 영웅이 난데없이 관등성명이라니?

상상한 적도 없고 상상할 수도 없다.

“아직도 그런 헛소리를 할 여유가 있습니까? 이게 도대체 정신이 똑바로 박힌 사람들이 할 얘기냔 말이야!”

“죄, 죄송합니다.”

“저희가 잘못 들은 것 같습니다.”

“다들 정신 똑바로 차려요. 알겠습니까?”

으름장을 놓은 1팀장이 다시 걸음을 뗀 그 순간이었다.

- 아닙니다아아악!

“…….”

- 시정하겠습니다아악!

“…….”

그것은 영혼이 실린 이등병의 외침.

꾹 닫혀 있던 1팀장의 입이 열린 것은 잠시 후였다.

“지금부터 전속력으로 뛰어간다. 실시.”

“시, 실시!”

이 자리에 모인 이들은 최소 C급 헌터. 이미 일반인의 한계를 훌쩍 뛰어넘은 초인들이다.

폭주 기관차처럼 내달린 그들은 5분이 채 지나기도 전에 등산로 입구에 도착했다.

“느려 터졌군. 이제야 왔나?”

“길드장님!”

“목소리 줄여, 귀청 떨어져.”

여느 때와 다름없는 임춘수의 모습에 1팀장이 안도의 한숨을 내쉬었다.

“전 또 혹시 무슨 일이 난 줄 알고…….”

“일이라니? 뭐 이상한 일 있었나?”

“아, 아닙니다. 그런데 진태경 그놈은 어디 갔습니까?”

“적당히 타일러서 보냈어. 이야기를 나눠 보니 생각보다 괜찮은 놈이더군. 그런데 왜?”

“놈이 무슨 소란을 피웠나 해서요.”

“아, 혹시 아까 어떤 놈이 소리 지른 거 말하는 거야?”

“네, 맞습니다. 그런데 목소리가 꼭…….”

길드장님 같아서요. 차마 뒷말을 잇지 못하는 1팀장을 향해 임춘수가 눈을 부라렸다.

“목소리가 뭐?”

“아, 아무것도 아닙니다.”

“싱겁기는. 새파란 놈들이 저 아래서 군대놀이 하길래 쫓아내고 왔다. 아니, 요즘도 대학에 군기 문화가 있어?”

“아, 그렇군요.”

“거 뭐야. PT 체조로 잠깐 굴렸더니 아주 죽으려고 하데?”

1팀장은 마음에 품고 있던 의혹이 말끔하게 사라지는 것을 느꼈다.

‘내가 미쳤던 거지. 감히 무슨 생각을.’

그가 한쪽에서 마음 깊이 반성하고 있을 때 임춘수는 보안팀을 탈탈 털고 있었다.

“보안팀장.”

“예, 옛!”

“어쭈. 대답은 잘하네. 이런 일을 벌이고도 아직 팀장은 팀장이라 이건가?”

“죄, 죄송합니다!”

“다른 놈들은 잘해서 입 다물고 있나? 오늘 칼춤 한번 춰?”

“죄송합니다, 길드장님!”

1팀장은 흐뭇하게 웃으며 그 광경을 지켜봤다.

간혹 임춘수의 성격이 지랄 맞다는 유언비어를 퍼트리는 놈들이 있다. 그러나 직접 옆에서 지켜본 그는 카리스마가 뛰어난 상관이며 훌륭한 인생의 선배였다.

‘길드장님. 영원히 따르겠습니다.’

무한한 존경의 눈빛으로 임춘수의 뒷모습을 바라보던 1팀장이 문득 고개를 갸웃했다.

‘……그런데 왜 길드장님 등에 흙이 묻어 있지?’

애들을 좀, 격하게 혼내셨나 보다.



* * *



“도착했습니다.”

김 집사의 말에 조수석에 앉아 있던 나는 화들짝 정신을 차리며 주변을 두리번거렸다. 창밖으로 아파트 입구가 보였다. 언제 여기까지 왔지?

“가, 감사합니다.”

“별말씀을요.”

멋있게 주름진 얼굴에 미소가 떠오른다. 왕년에 한 시대를 주름잡던 중년 배우가 생각나는 모습이다.

‘아니, 이 사람도 한 시대를 주름잡긴 했구나.’

지금까지는 그저 까마득한 선배 헌터 정도로 생각했는데, 그건 김 집사를 몰라도 한참 몰랐던 거다.

‘A급 마법사를, 그것도 임춘수를 개처럼 굴리다니.’

옛 전쟁 영웅한테 PT 8번 100세트를 시키더니, 나중에는 구둣발로 쪼인트를 깠다. 나긋나긋한 목소리로 임춘수를 갈구던 모습은 지금 생각해도 소름 그 자체다.



‘훈련생, 누가 PT 체조에 마나를 씁니까?’

빡!

‘1번 훈련생 임춘수. 죄, 죄송합니다.’

‘아픕니까? 나이 먹더니 목소리도 작아진 겁니까?’

‘아닙니다아아악!’

‘차렷. 열중쉬어. 차렷. 열중쉬어.’

파바바바박!

‘뒤로 취침. 앞으로 취침. 뒤로 취침. 뒤로 취침.’

‘헉.’

‘훈련생, 본 교관이 뒤로 취침이라고 하는 말 못 들었습니까? 정신 똑바로 차립니다.’

‘시정하겠습니다아악!’

‘그리고 왜 선량한 후배를 괴롭힙니까? 본 교관이 누누이 강조하지 않았습니까. 선후배끼리 서로 도우며 살라고.’

‘죄, 죄송합니다.’

‘복명복창합니다. 앉으면서 후배를, 일어나면서 아끼자. 하나. 둘.’

‘후배를, 아끼자!’

‘훈련생, 25기로 기억하는데 맞습니까?’

‘1번 훈련생 임춘수. 예, 그렇습니다.’

‘본 교관은 3기입니다. 만약 오늘 있었던 일이 밖으로 새어 나가거나 다시 반복된다면 4기부터 24기까지 열외 없이 집합입니다.’

‘…….’

‘왜 대답이 없습니까. 쪼그려 뛰기 준비.’

‘주, 준비…….’



굴리고, 굴리고, 또 굴리고.

그야말로 돈 주고도 못 보는 광경. 만약 상동 길드원들이 봤다면 오늘 부로 길드 문 닫을 뻔했다.

‘김 집사, 이 양반 도대체 정체가 뭐야?’

헌터 훈련소 3기면 전국 길드장들을 연병장에 모아 놓고 줄 빠따를 쳐도 된다. 게다가 무려 교관 출신이라니.

어지간한 대격변 초창기 마법사들은 전부 그의 손을 거쳤다고 해도 과언이 아니다.

‘마법사로서의 역량도 최소 A급.’

임춘수가 찍소리도 못하고 얼차려를 당하는 것만 봐도 알 수 있다. 김 집사가 짬으로도, 실력으로도 앞선다.

얼음과 화염. 마법의 상성도 있겠지만 임춘수를 가르쳐서 지금의 위치까지 오르게 한 것도 김 집사라고 볼 수 있다.

‘그런데…….’

그 정도씩이나 되는 사람이 왜 집사 노릇을 하고 있냐 이거지. 슬쩍 김 집사를 곁눈질하다가 시선이 딱 부딪쳤다.

“묻고 싶은 게 많아 보이는군요.”

“솔직히 말씀드리면 그렇습니다.”

궁금해서 도저히 못 참겠다.

생각이 고스란히 드러나는 내 표정에 김 집사가 입꼬리를 말아 올렸다.

“말하자면 깁니다.”

“괜찮습니다. 휴가 중이라 시간 넉넉해요.”

“아, 그럼 이참에 진태경 씨 얘기도 들을 수 있겠군요. 안 그래도 궁금한 점이 한두 가지가 아닌데.”

“생각해 보니까 벌써 저녁 시간이네요. 내일은 휴가 마지막 날이라 부동산 계약도 해야 하고. 허허허.”

“…….”
```

## Current accepted English baseline

```markdown
# Chapter 101

*What the hell is this?*

I was dumbfounded. Butler Kim’s appearance was unexpected, but that was nothing compared to the words he had directed at Im Chunsoo.

*Chunsoo? You?*

*Were the two of them acquainted?*

Come to think of it, Butler Kim and Im Chunsoo had a lot in common. They were around the same age, and both had been Hunters for a long time.

*Come to think of it, Butler Kim was active as a Hunter during the Great Cataclysm, too.*

I had never heard it directly from him, but I had suspected as much. Looking back and forth between the two men, I carefully asked,

“Are you two close?”

Im Chunsoo’s pupils trembled.

* * *

When Im Chunsoo first received the report on the Peace Guild, he had doubted his own eyes.

The face in the photograph was one that remained in his hazy memories—a face he had been certain he would never see again.

*Who did you say this man was?*

*Peace Guild Master Kim Hwajong. He’s fifty-five years old and a B-rank Hunter.*

*Kim Hwajong? A B-rank Hunter?*

*Yes. Is there some problem?*

*No, no. He resembles someone I used to know, so I mistook him for that person.*

That figures. Im Chunsoo let out a sigh of relief.

The face did resemble him a little, but that was all. More importantly, hadn’t that man died over thirty years ago?

No matter how bizarre the world had become, the dead could not come back to life.

*Even if that bastard had come back to life, he wouldn’t be rotting away in a place like this. I simply mistook him for an old B-rank Hunter.*

That day, Im Chunsoo drank a glass of soju for the first time in a long while and tried to shake off his uneasy feelings. It was an attempt to cast off the terrible memories that had clung to his ankles even after he turned fifty.

*Damn. I’m this old, and I’m still like this.*

Later, when he heard that Kim Hwajong’s information was protected by airtight security, he had even felt a chill run down his spine.

*Could it be? No. There’s no way.*

But then… why did ominous premonitions never turn out to be wrong?

“Rise up. Fire Wall.”

A quiet voice chanting a spell rang out, and a wall of fire surged upward.

*Fwoosh! Fwoosh!*

Blue flames burning at an extreme temperature vaporized the ice spikes, which were harder than steel, without leaving a trace.

And then—

“I’m glad I’m not too late. You too, Chunsoo.”

The moment he heard the voice he could never forget, not even in his dreams, Im Chunsoo remembered.

The terror of being controlled by that man.

The humiliation of rolling around on the ground to survive.

*Fuck… I’m screwed.*

As he stood frozen like a stone, Jin Taekyung asked him,

“Are you two close?”

What? Close?

Im Chunsoo swallowed the stream of curses rising from the depths of his lungs and turned around.

A man he had believed had died long ago was standing there.

“I-Instructor.”

Butler Kim smiled gently. It was the smile of a demon still deeply engraved in Im Chunsoo’s mind, even after all these years.

“Twenty-eighth Regiment, First Battalion, Second Company. Im Chunsoo. Yes, I knew the moment I saw you.”

It was the resonance of the soul.

Im Chunsoo’s hunched back straightened. His feet snapped together at a forty-five-degree angle, and his gaze turned fifteen degrees upward toward the front.

After a series of movements as fast as lightning, a thunderous shout burst from his throat.

“Trainee Number One! Im! Chun! Soo!”

The mountain shook as he bellowed out his military identification for the first time in thirty years.

* * *

What Team Leader 1 found after climbing up the mountain was grass splattered with blood in several places and the Security Team bound tightly with magical ropes.

*What a sight.*

Clicking his tongue inwardly, he drew his sword and cut through the ropes.

Everyone had lost some blood, but none of them appeared to have suffered serious injuries. Jin Taekyung seemed to have shown them at least the bare minimum of consideration.

*At this level, he’s either a top-tier B-rank… or an A-rank Hunter.*

That was how strong Jin Taekyung appeared to Team Leader 1.

For one person, the walk back down the mountain was a hellish experience.

“Why did you do that? We might have been able to overlook the surveillance, but what happened today could amount to attempted murder. Did you start this after thinking about what would happen afterward?”

“I’m… sorry.”

At Team Leader 1’s words, the Security Team Leader hung his head.

They had gone so far as to use force, only to be thoroughly trounced by Jin Taekyung. Even if he had ten mouths, he would have had nothing to say.

“The Guild Master is deeply disappointed.”

“Th-then?”

“A written report and a pay cut are a given. Prepare yourself for anything beyond that, too.”

“Are you talking about resignation?”

“That depends on the Guild Master.”

“Team Leader, perhaps…”

“Let me tell you up front: don’t ask me for any favors. I don’t have any interest in taking the side of someone who smeared the name of the company I work for. And I have no intention of going against the Guild Master’s wishes.”

“…”

“Whew.”

It was then that Team Leader 1 let out an irritated sigh.

A booming shout echoed from far away.

—Trainee Number One! Im! Chun! Soo!

“……”

“……”

What was that? Were they hearing things?

Team Leader 1 and even the Security Team members, who had all looked ready to die, jumped in surprise. The first to recover his composure was the Security Team Leader.

“Team Leader 1, I’m sorry to bring this up in this kind of atmosphere, but I think I just heard the Guild Master’s voice.”

Team Leader 1, who had been cleaning out his ears, opened his eyes wide.

“Did you hear it too?”

“We heard it, too.”

“But we couldn’t really tell whether it was the Guild Master’s voice… We think we heard a name, though.”

“That was a person’s name? I thought it was just someone screaming.”

“Really? I thought it sounded like someone giving their name and rank.”

Team Leader 1’s face hardened as he listened to the Security Team whispering among themselves.

“Who just said that? What was that about giving a name and rank?”

To him, Im Chunsoo was a respected senior and superior.

Im Chunsoo was an unrivaled Hunter who had been active since the Great Cataclysm and a war hero—and they were saying he had suddenly given his name and rank?

Team Leader 1 had never imagined such a thing. He couldn’t even imagine it.

“Do you still have the leisure to spout this kind of nonsense? Do you think this is something people in their right minds would say?”

“S-sorry.”

“We must have heard it wrong.”

“Everyone, get a hold of yourselves. Understood?”

After issuing his warning, Team Leader 1 started walking again.

That was when it happened.

—No, sirrrrr!

“……”

—I’ll correct it, sirrrr!

“……”

Those were the shouts of a private second class filled with the very essence of his soul.

It took a while before Team Leader 1’s tightly sealed mouth finally opened.

“From now on, we’re running at full speed. Move.”

“M-Move!”

Everyone gathered there was at least a C-rank Hunter. They were superhuman beings who had already far surpassed the limits of ordinary people.

They raced forward like runaway locomotives and reached the entrance to the hiking trail in less than five minutes.

“You’re slow as hell. Took you long enough?”

“Guild Master!”

“Keep your voice down. You’ll burst my eardrums.”

Seeing Im Chunsoo looking the same as always, Team Leader 1 let out a sigh of relief.

“I was worried something might have happened…”

“Something happened? Was there anything strange?”

“N-no, sir. But where did that Jin Taekyung bastard go?”

“I gave him a talking-to and sent him on his way. After speaking with him, I found out he was a better fellow than I expected. Why?”

“I was wondering if he had caused some kind of disturbance.”

“Ah, are you talking about the man shouting earlier?”

“Yes, that’s right. But his voice sounded just like…”

He couldn’t bring himself to finish the sentence.

Just like the Guild Master’s.

Im Chunsoo glared at him.

“Just like what?”

“Oh, it was nothing.”

“What a bland bunch. Some greenhorns were playing army down there, so I chased them away. Do colleges still have hazing culture these days?”

“Ah, I see.”

“What was it? I made them do some PT exercises for a while, and they looked ready to die.”

Team Leader 1 felt the suspicions he had been harboring vanish completely.

*I must have been out of my mind. How dare I even think such a thing?*

While he was deeply repenting to himself, Im Chunsoo was tearing into the Security Team.

“Security Team Leader.”

“Y-yes, sir!”

“Oh, you can answer properly. After causing this mess, are you still a Team Leader just because you’re technically still a Team Leader?”

“I’m sorry, Guild Master!”

“Are the others keeping their mouths shut because they did such a good job? Do I need to make my sword dance today?”

“We’re sorry, Guild Master!”

Team Leader 1 watched the scene with a pleased smile.

Every so often, there were people who spread the rumor that Im Chunsoo had a godawful personality. But after watching him up close, Team Leader 1 knew better. He was a charismatic superior and an outstanding senior in life.

*Guild Master. I’ll follow you forever.*

As Team Leader 1 gazed at Im Chunsoo’s back with boundless respect, he suddenly tilted his head.

*…But why is there dirt on the Guild Master’s back?*

He must have scolded those kids rather intensely.

* * *

“We’ve arrived.”

At Butler Kim’s words, I came to my senses with a start and looked around. Through the window, I could see the entrance to an apartment complex.

*When did we get here?*

“Th-thank you.”

“Don’t mention it.”

A smile appeared on his handsomely lined face. He looked like a middle-aged actor who had once ruled an entire era.

*No, this man really did rule an era, too.*

Until now, I had thought of him as nothing more than a senior Hunter from a distant generation. But that meant I hadn’t understood Butler Kim at all.

*He made an A-rank mage—and Im Chunsoo, no less—run around like a dog.*

He had made a former war hero do a hundred sets of PT Exercise No. 8, then later kicked him in the shin with his dress shoe. Even now, the way he had calmly berated Im Chunsoo in that gentle voice sent chills down my spine.

*Trainee, who uses mana during PT exercises?*

*Whack!*

*Trainee Number One Im Chunsoo. S-sorry, sir.*

*Does it hurt? Now that you’ve gotten older, has your voice gotten quieter, too?*

*No, sirrrrr!*

*Attention. At ease. Attention. At ease.*

*Snap-snap-snap-snap!*

*On your backs. On your fronts. On your backs. On your backs.*

*Gasp.*

*Trainee, didn’t you hear me say on your backs? Get your head straight.*

*I’ll correct it, sirrrr!*

*And why are you bullying an innocent junior? Haven’t I repeatedly emphasized that seniors and juniors should help each other?*

*S-sorry, sir.*

*Repeat after me. Sitting down, cherish your junior; standing up, cherish him. One. Two.*

*Cherish my junior!*

*Trainee, I remember you’re Class 25. Am I right?*

*Trainee Number One Im Chunsoo. Yes, sir.*

*I’m Class 3. If what happened today gets out or happens again, Classes 4 through 24 will assemble without exception.*

*…*

*Why aren’t you answering? Prepare for squat jumps.*

*P-prepare, sir…*

He kept working him over, then working him over some more.

It was the kind of sight you couldn’t see even if you paid for it. If the Sangdong Guild members had witnessed it, the Guild might have had to close its doors that very day.

*What on earth is Butler Kim’s real identity?*

If someone was Class 3 at the Hunter Training Center, they could line up every Guild Master in the country on a parade ground and beat every last one of them with a bat.

And he had been an instructor, no less.

It would not be an exaggeration to say that every mage from the early days of the Great Cataclysm had passed through his hands.

*His ability as a mage is at least A-rank, too.*

I could tell just by watching Im Chunsoo take his punishment without daring to make a peep. Butler Kim surpassed him in both seniority and skill.

There was probably also an elemental advantage between ice and fire. You could say Butler Kim was the one who taught Im Chunsoo and raised him to his current position.

*But…*

Why was someone that accomplished working as a butler?

I was sneaking a sidelong glance at Butler Kim when our eyes met.

“You seem to have a lot you want to ask.”

“To be honest, I do.”

I was too curious to stand it any longer.

Seeing my thoughts written plainly across my face, Butler Kim curled up the corners of his mouth.

“It’s a long story.”

“That’s fine. I’m on vacation, so I have plenty of time.”

“Ah, then this is a good opportunity to hear your story as well, Mr. Jin. I already have more than one or two questions myself.”

“Now that I think about it, it’s already dinnertime. Tomorrow is the last day of my vacation, so I have to sign a real-estate contract, too. Hahaha.”

“……”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 101`.

# Master Edit Task — Chapter 100

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
| 김화종    | **Kim Hwajong**   |
| 임춘수    | **Im Chunsoo**    |
| 임창수    | **Im Changsoo**   |
| 홍우진    | **Hong Woojin**   |
| 상태               | **Status**                     |
| 보상               | **Reward**                     |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 사천     | **Sichuan**            |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 성진호 | **Seong Jinho** |
| 평화 | **Peace Guild** | Guild name. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |
| 임춘수 | 김화종 | former_trainee_to_former_instructor | Instructor | deferential and fearful | Im Chunsoo addresses Hwajong as 교관님 after recognizing his former instructor. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
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

#### Chapter 98 tail (verified mastered)

…
she would jump whenever I suddenly spoke to her. Something had definitely changed around Mom. *She’ll tell me when the time is right.* My mother was the person I loved and trusted most in this world. As always, all I could do was trust her and wait. Of course, listening to her and talking things over at the right time was also a child’s duty. “What are you thinking about so hard?” “It’s nothing. By the way, aren’t you going out?” “What? You sound like you want me to leave.” “Not exactly.” “Hmm. Suspicious. You’re not planning to bring a girlfriend over, are you?” “…” *I wish I had a girlfriend to bring over.* My expression must have revealed my thoughts, because Hayeon hesitated. “Ah, I’m sorry.” “Don’t apologize. It makes me twice as pathetic.” “I’m really sorry.” “You’re doing this on purpose, aren’t you?” “Come to think of it, I have some books to return to the library.” She sprinted into her room, threw on her backpack, and came back out at the speed of light. The front door slammed shut, and the house fell silent. *She really went and gouged out a single man’s heart.* A corner of my chest felt hollow, but the stage I had been waiting for had finally been set. This was a problem I needed to deal with while my family was out of the house, if possible. *Myaow.* *Meow.* The two cats, one black and one white, crept toward me and began circling. Bright eyes. Perked-up ears. I left the Familiars, who were dying to learn more about me, behind and stepped onto the balcony. The first thing I saw was the parking lot, where hundreds of cars were lined up. *The parking lot is clear.* Before returning home, I had carried the Familiar in my arms and taken a lap around the apartment complex. To everyone else, I probably looked like an idler out for a walk on a pleasant day. My real purpose had been to check the vehicles. The result was nothing suspicious. *Then it has to be one of those apartments.* That confirmed the watchers had made one of the recently sold or leased apartments their base. I recalled the information I had obtained from the real-estate office once more. *Building 5, Unit 901. Building 4, Unit 302. Building 3, Unit 202.* Coincidentally, all three were positioned around our apartment, forming a ring. Their windows also overlooked the building entrances, making them ideal for surveillance. The watchers could have been in any one of them. *The question is which one they’re hiding in…* They were cautious enough to use a Familiar instead of magical Equipment to avoid being discovered. If I approached recklessly, I would lose them. To make a definite capture, I had no choice but to throw out equally substantial bait. *Time to get started.* Swish. Rustle. First, I drew every curtain in the house. Though it was the middle of the day, the living room grew dim. Standing in its center, I reached into my pocket. *Inventory open. Mana-detection Equipment.* At the same time, my hand closed around a lump of metal half the size of my palm. As its name suggested, it was Equipment that could detect mana. I had paid twenty million won for it at the Store. *Next step: search.* I carefully swept through the house with the detection Equipment. After confirming that no mana was being detected inside, I took out my smartphone and called someone. Beep. Beep. Click. The call connected, and the other person answered. —Hello? I replied, “It’s me, Jin Taekyung.” The two Familiars watched me without even seeming to breathe. * * * The moment Kim Junsu opened his eyes, he shouted. “He’s here! He’s here!” The Security Team members, who had been huddled together writing their assessments, jumped in surprise. “What?” “Who’s here? Our Team Leader?” “Or could it be…” Kim Junsu nodded at the team member who had trailed off. “The target. This bastard reeks of something rotten.” “Seriously?” “Yes. I got a bad feeling when he drew all the curtains as soon as the house was empty, and then he even used detection Equipment to inspect the inside.” That wasn’t something an ordinary C-rank Hunter would do, especially while on vacation. Everyone in the room swallowed hard. “Th-then what?” “He pulled out his phone and made a call.” “A call? To whom?” “I don’t know.” Kim Junsu furrowed his brow. “The call was so short that it didn’t even last three minutes. But more than that, I could tell he was being extremely careful about how he addressed the other person.” “That’s enough. We’ll report it up the chain and have them pull that bastard’s call records.” “Right. Was there anything else?” “Of course there was. Do you know what he said?” Ahem. After clearing his throat, he lowered his voice. “‘The plan is proceeding without a hitch. Yes, yes. The Sangdong Guild hasn’t noticed anything yet. I have the item with me.’” The team members listening slapped their knees. “This is it!” “We finally got something!” “Wow, I just got chills. What is he, some kind of secret agent?” At that moment, Kim Gwondong, who had been listening quietly, suddenly spoke. “Junsu, didn’t that bastard say he had some kind of item?” “Good observation.” Kim Junsu smiled meaningfully. “That guy has a USB.”

#### Chapter 99 tail (verified mastered)

…
he shouldn’t get involved any further. *Sangdong Guild, you goddamn thugs.* Clicking his tongue, Hong Woojin pulled out his smartphone and sent a text. The recipient was the Team 1 Leader. The message was short and simple. > **Team 1 Leader** > > I’m dropping the job. Before leaving the rooftop, he didn’t forget to pray for the already-vanished Jin Taekyung’s soul. *Well, that was filthy. Let’s never see each other again.* In every possible way, the job had brought him nothing but bad luck. * * * I climbed the mountain path in silence. I had left the hiking trail behind long ago. But I didn’t stop. I kept walking deeper and deeper into the mountain. At some point, a broad clearing came into view. Weeds had grown thick there, reaching up to my knees. I slowly turned around. “Looks like you’re still out for a walk?” Kim Gwondong, the middle-aged man I had run into twice before, said nothing. His face hardened. “No answer? Who’s the man beside you?” “A friend.” If Kim Gwondong had the sort of ordinary face you could see anywhere, the man who answered was his complete opposite. He was huge, with a vicious face fierce enough to make gangsters cry. A gravelly voice rumbled from between his lips. “You already know everything, so why did you come all the way here?” “You kept trailing me from behind, so I wanted to see how far you’d follow. Think of it as training a mutt.” The man burst into a hearty laugh. “Young punk’s got nerve. How old are you?” “*Yeokmasal*.”[^2] “You’ve got a real talent for asking for a beating.” “Thanks for the compliment, Mr. Choi Byungil.” The man, Choi Byungil, closed his mouth. His eyes wavered. “…How did you know?” “That’s a trade secret. But are you and Mr. Kim Gwondong really friends? Judging by appearances, you two don’t exactly look like a matching pair.” This time, it was Kim Gwondong’s turn to panic. But I wasn’t finished. “Is that hard to answer because you’re not friends? Then I’ll ask the other four. Mr. Park Hyungjin, Mr. Oh Gyuhyeon, Mr. Lee Mincheol, and Mr. Kim Junsu, I’d appreciate an honest answer.” Bzzzzzz. The air rippled, and four people dropped straight down. Each had a Level window floating above his head, and all four looked like they’d seen a ghost. “Why is everyone so surprised? I was just being considerate so you could breathe easy.” Choi Byungil gritted his teeth. All traces of his earlier composure had vanished, leaving his face colored by anxiety and bewilderment. “What the fuck… What kind of bastard are you?” He had cursed first, so that was the end of respecting my elders. I gave a quiet laugh as I looked at Choi Byungil. “You still don’t know? You must have dug up every scrap of information about me. If you went so far as to attach Familiars, that says everything.” “…!” “I could’ve let it go if I’d been alone at home. But the thought of my family being watched too pissed me off. So I threw out some bait, and you snapped it right up.” The six watchers trembled. “Th-then the USB…” “Oh, that? It’s the porn collection I’ve spent my whole life assembling.” A treasure of humanity, carefully preserved in my Inventory. “No way! I definitely had a feeling!” “Well, there are plenty of works in there that defy belief. And any man would get a gut feeling about it.” I addressed the six of them as they stood there looking utterly crushed. “You answered honestly, so let me ask you one thing, too.” One by one, they flinched whenever their eyes met mine. At last, my gaze settled on a painfully skinny man in his twenties. He was probably the Familiar mage. > **System** > > Level 41 Kim Junsu “Junsu. Sangdong Guild sent you, didn’t they?” “Shut your mouth!” Choi Byungil shouted, but Kim Junsu had already answered. His bloodless, ashen face was answer enough. “Okay, Sangdong Guild. I figured as much.” Choi Byungil’s face stiffened at my words. “You shouldn’t have said that name out loud.” “Why? You going to kill me?” “…I’ll capture you first. Then I’ll think about it.” “That’s going to be pretty hard.” Choi Byungil’s Level was in the mid-sixties. His aura was comparable to Im Changsoo’s, while the rest were unremarkable C-ranks around Levels 30 or 40. The odds of a group that wasn’t even a professional raid team managing to capture me were extremely low. “Come at me prepared to die. That’s the only way you’ll manage to tie so much as a butterfly knot around my wrist.” “Get him!” At Choi Byungil’s shout, the Sangdong Guild watchers began charging at me from all directions. Whoosh! The opening move was a dagger dropping toward my shoulder. I reached toward the trajectory that looked slow to me. At the same time… *Inventory open. Equip.* Crunch! The blade, brimming with internal energy, shattered the enemy’s dagger. Shards of metal and someone’s blood spilled across the nameless weeds. “Come on, you stalker bastards!” Ssshhhhh! [^1]: *Pyeong* is a traditional Korean unit of floor area; five pyeong is roughly 16.5 square meters. [^2]: *Yeokmasal* is a traditional Korean notion of a fate that compels someone to wander. Here it also puns on *sal*, the Korean word used when asking someone’s age.

## Korean source

```text
＃100화



사람은 저마다의 취미를 하나씩 갖고 있기 마련이다. 임춘수도 크게 다르지 않았다.

1팀장이 길드장실에 들어섰을 때 처음으로 목격한 것은 문을 향해 굴러오는 골프공이었다.

데구르르. 툭.

홀(Hole)을 한참이나 벗어난 공은 1팀장의 신발에 부딪힌 후에야 멈췄다. 허리를 숙여 공을 주우려는 그에게 임춘수가 손짓했다.

“됐어. 와서 차나 한잔해.”

“네.”

두 사람 사이에 잠깐 침묵이 흘렀다. 차를 음미하던 임춘수가 문득 입을 열었다.

“향 좋지?”

“아, 예. 좋은 차인가 봅니다.”

“이게 용정차라는 건데, 선물로 받았는데 사실 뭔지 잘 모르겠어. 가격만 더럽게 비싸고.”

“예?”

“뭘 그렇게 놀라?”

“차를 좋아하시는 줄 알았는데요.”

“전혀. 그냥 있어 보이고 싶어서 음미하는 흉내만 내는 거야. 집에서는 믹스 커피 마셔.”

1팀장은 실소를 흘렸다. 길드 간부들 사이에서 임춘수의 차(茶) 사랑은 유명했다. 누가 더 좋은 차를 길드장에게 선물하는지 경쟁이 붙을 정도다.

“놀랄 사람들이 몇 있겠군요.”

“예를 들자면?”

“3팀장이죠. 이번에 중국 출장 가서 명차를 구해 오겠다고 호언장담을 하고 다닙니다.”

“그놈 잘라. 일은 안 하고 풀떼기 구할 생각에 넋이 나갔구먼.”

“진심이십니까?”

“당연히 농담이지. 나는 농담도 못 하나?”

두 사람 사이로 가벼운 웃음이 흘렀다. 남은 찻물을 냉수처럼 쭉 들이켠 임춘수가 입맛을 다셨다.

“그래서, 언제 말할 건가?”

“예?”

“새로 가져온 소식 있잖아. 말하기 힘들어서 우물쭈물하는 놈한테 큰맘 먹고 비밀까지 얘기해 줬는데…….”

“그렇게 티가 났습니까?”

“앞으로는 들어오기 전에 거울 보고 와. 그렇게 죽상을 하고 있는데 누가 모르나.”

1팀장이 힘겹게 말문을 연 것은 얼마 지나지 않아서였다.

“일전에 내리신 평화 길드 조사…… 실패했습니다.”

“둘 다?”

“예. 죄송합니다.”

“더 자세히 설명해 봐.”

“신중하게 접근해 봤지만 평화 길드장과 팀장은 건드리지 않는 편이 좋을 것 같답니다.”

“그건 어느 정도 예상했어. 내가 직접 청탁을 넣었어야 했는데. 뭐, 결국 쓸데없는 체면 때문에 안 나선 거니까 내 탓도 있는 거지.”

“아닙니다. 제가 부족한 탓입니다.”

“그것도 맞는 말이고. 락 걸린 놈들은 몰라도 진태경인가 하는 C급 헌터는 성공했어야지.”

임춘수가 냉엄한 눈빛으로 그를 쏘아봤다.

“도대체 왜 실패한 건가? 외부에서 고용한 패밀리어 마법사에 길드 보안팀도 붙여 줬잖아.”

“저, 그게…….”

머뭇거리던 1팀장이 차마 하지 못했던 말을 어렵사리 토해 냈다.

“연락이 끊겼습니다.”

“응? 홍우진 그놈?”

“홍우진은 문자 한 통 남기고 잠적했고 연락이 끊긴 건 보안팀입니다.”

“보안팀이 왜? 주기적으로 상황 보고하지 않나?”

“네. 두 시간에 한 번씩 보고가 들어오는데…… 네 시간 전이 마지막입니다.”

“지금 보안팀이 단체 이탈이라도 했다는 소리야?”

“아닙니다. 정황상 진태경에게 당했을 확률이 높습니다.”

“뭐?”

이게 무슨 말인가.

황당해하는 임춘수에게 1팀장이 프린트해 온 종이를 내밀었다.

“오늘 자 보고입니다.”

특정 부분만 붉은 글씨로 칠해진 걸 보니 정기 보고서가 아니라 긴급 보고서다.

임춘수의 눈동자가 빠르게 활자 위를 누볐다.

표적이 정체를 알 수 없는 누군가와 통화를 했으며 대화 내용과 취한 행동 모두 수상하다. 보고를 빠짐없이 읽은 그가 한숨을 토해 냈다.

“허, 이거 생각보다 재밌는 놈이네. 그래서 이다음은?”

“보안팀장이 개인적으로 연락을 취했습니다. 급하게 표적을 쫓아야 하니 선 조치 후 보고 하겠다고요.”

“그리고 연락이 끊겼다…….”

임춘수는 골똘히 생각에 잠긴 채 탁자를 두드렸다.

톡. 톡. 톡. 고개를 들었을 때는 고급 원목 탁자가 꽁꽁 언 상태였다.

“진태경이랑 통화한 놈은 누구야? 이름 석 자 정도는 알아 왔으니까 이걸 보여 준 거겠지.”

“성진호. 부천 사는 30세 고시생입니다.”

“……1팀장아. 내가 잘못 들은 거냐? 헌터가 아니라 고시생?”

“저도 재차 확인해 봤지만 틀림없습니다. 진태경이 사는 고시원 총무더군요. 의형제 같은 사이랍니다.”

“허, 참. 오늘 여러 번 놀라게 만드는군.”

최소 A급 헌터는 될 줄 알았는데, 뭐? 민간인 고시생?

고개를 절레절레 내저은 임춘수가 자리에서 일어났다.

“끙, 이거 아주 제대로 당했네. 달랑 다섯 명 있는 길드가 뭐 이리 숨기는 게 많아?”

“어찌 하는 게 좋겠습니까?”

“어쩌긴 뭘 어째. 슬슬 밥시간인데 저녁이나 한 끼 하러 가야지.”

“……네?”

어리둥절한 1팀장을 본 임춘수가 혀를 찼다.

“잔말 말고 따라오기나 해.”

오늘 저녁은 일산에서 먹을 생각이다.



* * *



6대1의 싸움은 순식간에 끝났다.

애초에 나와 손을 섞을 수 있는 사람은 최병일 한 명뿐인데다가, 그마저도 오래 버티지 못하고 무릎을 꿇었다.

‘뭐, 당연한 거지.’

그러나 누군가에게는 커다란 충격이었던 것 같다.

양 발목이 부러진 최병일은 새하얗게 질린 얼굴로 계속해서 내게 말을 걸었다.

“A급 헌터? 정체를 숨긴 건가?”

“아닌데. 정체 숨긴 적 없는데.”

“진짜 소속을 밝혀라! 혹시 아레스 길드에서 우리 상동 길드를…….”

“나 평화 길드야. 그리고 아레스 길드는 당신네 길드에 관심도 없을걸. 체급부터가 완전히 다른데.”

“그럼 전화를 한 상대는 누구지?”

“고시원 총무 형이라고 몇 번을 말하냐. 성진호라고 하면 당신이 알아?”

“이럴 리가, 이럴 리가 없는데.”

결국 아가리 봉인술을 쓰는 수밖에 없었다. 그의 옷을 찢어 입을 틀어막은 뒤 그를 포함해 남은 부상자들을 모두 치료했다.

아, 물론 내가 스토어에서 샀던 포션은 아니다.

“이야, 상동 길드 지원 빵빵하네.”

당장 놈들이 들고 온 것만 털었는데도 장비며 소모품의 질과 양이 제법이다. 그중 일부를 치료에 쓰고 나머지는…….

“이건 일단 내가 압수. 혹시 불만 있는 사람?”

당연하게도 누구 하나 손을 들지 않았다.

다들 압도적인 내 무력에 질렸는지 상처가 치료됐음에도 감히 다시 덤빌 생각을 하지 못했다. 상당히 똑똑한 놈들이다.

“자, 이제 나한테 너희들의 임무에 대해서 상세히 알려 줄 사람?”

이번 역시 아무도 손을 들지 않아서 직접 고르는 수밖에 없었다.

선택은 아주 쉬웠다.

“너.”

“저, 저요?”

“응, 너.”

패밀리어 마법사, 김준수는 움찔하더니 이내 결연한 표정으로 선언했다.

“저는 보안팀 소속입니다. 길드의 기밀 사항을 외부인에게 함부로 유출할 수 없습니다.”

“오.”

나는 감탄했고, 그것과 동시에 녀석의 머리끄덩이를 잡아당겼다.

어디선가 테이프 뜯어지는 작은 소리가 들리고 가발이 훌렁 벗겨졌다. 그러자 그 아래 감춰져 있던 빛나는 정수리가 드러난다.

“이게 무슨!”

“자, 지금부터 하는 질문에 거짓말이나 모르쇠로 일관할 시 머리털을 한 움큼씩 뽑도록 하겠다.”

“……!”

그 후부터는 일사천리였다. 어떻게 해서든 머리를 지키고 싶은 탈모인의 입에서 온갖 정보가 흘러나왔다.

“홍우진?”

“네, 1팀장님이 외부에서 고용한 B급 마법사입니다. 저처럼 패밀리어 마법이 주특기고요.”

“그래?”

아깝다. 그놈도 잡아서 족쳤어야 했는데.

‘언젠가 만날 일이 오겠지. 오래 걸리면 내가 찾아내도 되고.’

나는 입맛을 다시며 계속해서 정보를 뽑아냈다. 김준수가 멈칫한다 싶으면 얼마 남지 않은 머리카락을 만지작거리며 용기를 북돋아 주었다.

“끝입니다, 진짜 끝. 아무리 제가 보안팀이라지만 더 이상은 몰라요. 그러니 제발 머리카락만큼은…….”

억울함과 진심이 묻어 나오는 말투다. 특히 마지막 말이 내 심금을 울렸다.

‘이 정도면 얼추 마무리됐겠지.’

배후는 예상대로 상동 길드, 정확히 말하면 임춘수였다.

가뜩이나 흥청망청 사는 아들내미가 수입 억을 삥 뜯긴 걸 보고 그 직후부터 우리 길드를 털기 시작한 거다.

뭐, 결국 나한테 역으로 털렸지만.

“길드장님께서 가만히 있지 않을 거다.”

“약한 놈들 전용 멘트, 뭐 그런 거라도 있나? 길드장 운운하지 말고 본인이 싼 똥이나 치울 생각해.”

“……큭.”

내 일침에 최병일은 분한 듯 고개를 떨궜지만 저 인간의 말이 아주 틀린 건 아니다.

‘상동 길드장이 알면 열 좀 받겠네.’

감시하라고 부하들을 보냈더니 오히려 역으로 털리고 붙잡히는 신세까지 됐다. 길드장은 물론이고 길드 전체 입장에서 봐도 이런 개망신이 또 없다.

사안이 사안이니만큼 그쪽에서도 조용히 덮고 넘어가 주길 바랄 뿐이다.

‘최 팀장한테 전화를 해야 하나.’

스마트폰을 들고 고민하던 찰나였다.



[010-xxxx-xxxx]



처음 보는 번호로 걸려 온 한 통의 전화. 뭐지?

왠지 모르게 드는 묘한 긴장감 속에 전화를 받았다.

“여보세요?”

- 내려오게. 밑에서 기다리고 있네.

“네? 전화 잘못 거신 것 같은데요.”

- 진태경. 맞지?

“아니, 맞긴 한데…… 누구세요?”

- 나 임춘수라고 하는 사람인데, 그쪽이 우리 애들을 몇 명 데리고 있다고 해서.

“…….”

- 듣고 있나?

듣고는 있다. 말을 못 할 뿐이지.

중견 길드의 길드장이 나를 만나기 위해 여기까지 직접 행차하실 줄이야. 그것도 성질 더럽다는 임춘수가.

- 내려와, 오해도 풀 겸 밥이나 한 끼 하게.

굳이 오해를 풀 만한 일은 없지만 ‘싫어요.’라고 했을 경우 무슨 일이 벌어질지 모르겠다.

이미 위치까지 파악하고 온 양반 아닌가?

결국 내 선택지는 하나밖에 없었다.

“지금 내려가겠습니다.”



* * *



임춘수의 첫인상은 강렬했다. 생각보다 젊었고 눈빛은 온화한 듯하면서도 뜨거웠다.

‘불같다.’

아이러니하게도 저것이 얼음 마법의 대가를 만나서 처음으로 한 생각이었다.

“안녕하십니까. 진태경이라고 합니다.”

“임춘수라고 하네.”

뜨거운 눈빛과는 달리 목소리는 차갑다. 이제야 프로즌(frozen)이라는 별명과 어울리는 사람이 된 것 같았다.

“보고서 사진으로만 보던 얼굴을 이렇게 보니까 좀 신기하군.”

뒤를 캤다는 걸 이렇게 직설적으로, 부끄러워하지 않고 말할 수 있는 사람도 존재하는구나.

“우리 애들은?”

“위에 있습니다.”

“사망자가 있나?”

“설마요. 범죄자 되는 건 딱 질색입니다.”

“그거 고맙군.”

임춘수가 나를 향해 고개를 까딱였다.

“우리 애들이 조급함에 실수를 저질렀네. 이해해 줄 텐가?”

“적당한 보상이 있다면요.”

내 대답에 임춘수는 피식 웃었고, 팀장처럼 보이는 옆의 남자는 눈살을 찌푸렸다.

“젊은 친구가 예의가 없군.”

“제가 좀 그런 편이긴 한데…… 감시까지 붙인 분들한테 들으니까 기분이 좀 묘하네요.”

“아무리 그래도.”

남자의 말은 이어지지 못했다. 임창수가 손을 들어 그를 제지했기 때문이었다.

“1팀장은 위에 가서 애들이나 풀어 줘.”

“……예. 길드장님.”

김 집사가 부드러운 카리스마라면 그는 거친 카리스마의 소유자였다. 같은 마법사라 그런 걸까? 어쩐지 모르게 두 사람의 모습이 겹쳐 보였다.

“자네는 나랑 좀 걷지.”

임창수가 앞장섰고 내가 그 뒤를 따랐다.

“혹시 그거 알고 있나?”

한동안 거침없이 걸어가던 임춘수가 불쑥 말문을 열었다.

“난 일단 원한 관계가 맺어지면 무조건 끝을 봐야 해. 자네는 어떨지 모르지만 난 그런 성격이지.”

무림 스타일인데?

약육강식. 적자생존. 이 아저씨의 혈관에도 무림 터프가이의 피가 흐르는 모양이다.

“지금의 상동 길드는 그렇게 쌓아 올린 거야. 무너트린 걸 밟고 건져 내서 더 높게.”

“그렇군요.”

“평화 길드는 어떤가?”

“……그게 무슨 뜻입니까?”

“근 10년은 무료했지. 인근 길드와는 전부 동맹 관계고 우리에게 더 이상 적수가 없었어. 그런데 자네들이 나타난 거야.”

호기심과 열정이 끓어오르고 있는 듯한 그의 눈을 보며 드는 생각은 딱 하나였다.

‘이거 위험한데.’

그러거나 말거나 임춘수의 말은 이어졌다.

“길드장과 팀장은 나로서도 정보를 쉽게 열람할 수 없는 인물들이고…… 무엇보다 자네의 존재가 날 자극시켰어.”

우리는 이제 언덕길을 오르고 있었다. 적지 않은 나이임에도 불구하고 임춘수는 숨이 차는 것 같지 않았다.

“자네는 내가 왜 여기까지 왔는지 알고 있나?”

“절 보기 위해서겠죠.”

“절반만 맞췄어.”

임춘수의 발걸음이 멎었다. 천천히 돌아서는 그의 전신에서 서늘한 냉기가 흘러나왔다.



[Lv.75 임춘수]



“내 나이에는 시간이 금이야. 얼굴만 보려고 여기까지 올 만큼 사치스러운 사람이 아닐세.”

프로즌. 대격변을 온몸으로 헤쳐 나간 노련한 A급 마법사가 나를 향해 손을 펼친 순간.

츠츠츠.

아무것도 없던 머리 위 허공에서 십여 개의 얼음송곳이 생겨났다. 한여름의 공기가 얼어붙고 뜨겁게 달궈진 흙길에 서리가 내려앉는다.

‘된통 걸렸군.’

제법 경우를 아는 노인네라고 생각했는데, 설마 다짜고짜 이런 식으로 나올 줄은 몰랐다.

“이렇게까지 해야 됩니까?”

“자네라서 이렇게까지 하는 거야.”

“저는 고작 C급인데요.”

“그래, 그 C급 헌터 실력 좀 보자고.”

말이 끝남과 동시에 임춘수가 주먹을 움켜쥐었다. 시린 냉기를 뿜어내는 얼음송곳들이 나를 향해 쏘아졌다.

쐐애애애액!

그러나 얼음송곳은 내 옷자락 하나 건드리지 못했다.

“솟구쳐라. 파이어 월(Fire Wall).”

또렷한 음성과 함께 대기에 스며든 마나가 요동친다. 임춘수의 마법으로 서리가 끼어 있던 바닥이 녹고 불꽃이 솟구쳤다.

화륵, 화아악!

그건 말 그대로 불의 장벽이었다. 푸른 화염은 얼음송곳을 집어삼키고 나와 임춘수의 사이를 갈랐다.

일렁이는 불꽃 너머, 임춘수가 경악에 찬 음성을 토해 냈다.

“이건……!”

그러나 내가 보고 있는 것은 임춘수가 아니었다. 그의 등 뒤, 등산로 입구에 서 있던 한 사람이 부드러운 목소리로 인사를 건넸다.

“늦지 않아서 다행입니다. 춘수, 자네도.”



[Lv.80 김화종]



김화종. 김 집사의 등장이었다.
```

## Current accepted English baseline

```markdown
# Chapter 100

Everyone had at least one hobby. Im Chunsoo was no different.

The first thing Team Leader 1 saw when he entered the Guild Master’s office was a golf ball rolling toward the door.

Roll, roll. Thunk.

The ball had rolled far wide of the hole and only stopped after striking Team Leader 1’s shoe. As he bent down to pick it up, Im Chunsoo waved him off.

“Forget it. Come over here and have some tea.”

“Yes, sir.”

A brief silence passed between them. After savoring his tea, Im Chunsoo suddenly spoke.

“Smells good, doesn’t it?”

“Ah, yes. I suppose it must be good tea.”

“This is Longjing tea. I received it as a gift, but to be honest, I don’t really know what it is. It’s just filthy expensive.”

“What?”

“Why are you so surprised?”

“I thought you liked tea.”

“Not at all. I only pretend to savor it because I want to look sophisticated. At home, I drink instant coffee.”

Team Leader 1 let out a quiet laugh. Im Chunsoo’s love of tea was famous among the Guild executives. They had even begun competing to see who could give the Guild Master the better tea.

“A few people are going to be surprised.”

“For example?”

“Team Leader 3. He’s been bragging that he’ll bring back some famous tea from his upcoming business trip to China.”

“Fire that bastard. He’s lost his mind thinking about gathering weeds instead of doing his job.”

“You’re serious?”

“Of course I’m joking. Am I not allowed to joke?”

Light laughter passed between them. Im Chunsoo gulped down the remaining tea as if it were cold water, then smacked his lips.

“So, when are you going to tell me?”

“Tell you what?”

“You have some new information. I went out of my way to tell you a secret because you were having trouble speaking up…”

“Was it that obvious?”

“Look in a mirror before you come in next time. With a long face like that, anyone could tell.”

It wasn’t long before Team Leader 1 finally managed to speak.

“The investigation into the Peace Guild that you ordered previously… has failed.”

“Both of them?”

“Yes. I’m sorry.”

“Explain in more detail.”

“They approached carefully, but they say it would be better not to provoke the Peace Guild Master or Team Leader.”

“I expected as much. I should have made the request personally. In the end, I didn’t step in because of my useless pride, so some of the blame is mine.”

“No, it was because I was inadequate.”

“That’s true, too. Even if those locked-down bastards were out of reach, this C-rank Hunter named Jin Taekyung should have been a success.”

Im Chunsoo shot him a cold glare.

“Why exactly did you fail? I gave you a Familiar mage hired from outside and even assigned the Guild’s Security Team to him.”

“Well, that…”

Team Leader 1 hesitated, then finally forced out the words he had been unable to say.

“We lost contact.”

“Hm? That bastard Hong Woojin?”

“Hong Woojin disappeared after leaving a single text message. The ones we lost contact with were the Security Team.”

“Why the Security Team? Don’t they report the situation regularly?”

“Yes. Reports come in every two hours, but… the last one was four hours ago.”

“Are you saying the entire Security Team walked out on us?”

“No. Judging by the circumstances, it’s highly likely Jin Taekyung got to them.”

“What?”

What was that supposed to mean?

As Im Chunsoo stared at him in disbelief, Team Leader 1 handed him the pages he had printed out.

“Today’s report.”

The fact that only certain sections had been highlighted in red showed that this was an emergency report, not a regular one.

Im Chunsoo’s eyes raced across the words.

The target had spoken on the phone with someone whose identity was unknown, and both the contents of the conversation and the target’s actions were suspicious. After reading the report from beginning to end, Im Chunsoo let out a sigh.

“Hah. He’s more interesting than I expected. What happened next?”

“The Security Team Leader contacted me directly. He said they needed to pursue the target immediately, so he would take action first and report afterward.”

“And then they lost contact…”

Im Chunsoo fell deep into thought as he tapped the table.

Tap. Tap. Tap.

When he raised his head, the high-quality wooden table had frozen solid.

“Who did Jin Taekyung call? You found out at least the person’s full name, or you wouldn’t have shown me this.”

“Seong Jinho. A thirty-year-old exam candidate living in Bucheon.”

“……Team Leader 1. Did I hear you wrong? An exam candidate, not a Hunter?”

“I checked again myself, but there’s no mistake. He’s the manager of the goshiwon where Jin Taekyung lives. They’re supposedly like sworn brothers.”

“Hah. Today keeps surprising me.”

Im Chunsoo had expected him to be at least an A-rank Hunter. But what was this? A civilian exam candidate?

Shaking his head, Im Chunsoo rose from his seat.

“Ugh, we really got played. How does a Guild with only five people have so much to hide?”

“What should we do?”

“What do you mean, what should we do? It’s almost dinnertime. We should go have a meal.”

“……What?”

Im Chunsoo clicked his tongue at the bewildered Team Leader 1.

“Stop talking and follow me.”

He was thinking of having dinner in Ilsan that evening.

* * *

The six-on-one fight ended in an instant.

To begin with, Choi Byungil was the only one who could exchange blows with me. Even he didn’t last long before dropping to his knees.

*Obviously.*

But it seemed to have been a tremendous shock to someone.

With both ankles broken, Choi Byungil continued talking to me with a face as white as a sheet.

“An A-rank Hunter? Were you hiding your identity?”

“No. I never hid my identity.”

“Tell me your real affiliation! Is Ares Guild making a move against our Sangdong Guild…?”

“I’m with the Peace Guild. And Ares Guild wouldn’t be interested in your Guild. You’re in completely different weight classes.”

“Then who was the person you called?”

“How many times do I have to tell you? He’s my goshiwon manager hyung. Would you know him if I said his name was Seong Jinho?”

“This can’t be. This can’t be happening.”

In the end, there was nothing for it but to use the mouth-sealing technique. I tore his clothes into strips and gagged him, then treated all the remaining wounded, including him.

Of course, I didn’t use the potions I had bought from the Store.

“Wow, Sangdong Guild gives you guys some serious support.”

Even after looting only what they had brought with them, the quality and quantity of their Equipment and consumables were nothing to sneeze at. I used some of them for treatment, and the rest…

“I’m confiscating this for now. Anyone have a problem with that?”

Naturally, no one raised a hand.

They must have been so intimidated by my overwhelming strength that, even after their injuries had been healed, they didn’t dare attack me again. They were fairly smart men.

“Now, who wants to tell me all about your mission?”

Once again, nobody raised a hand, so I had to choose someone myself.

The choice was easy.

“You.”

“M-me?”

“Yeah, you.”

The Familiar mage, Kim Junsu, flinched. Then he declared with a resolute expression,

“I’m with the Security Team. I cannot carelessly disclose the Guild’s confidential information to an outsider.”

“Oh.”

I was impressed. At the same time, I grabbed him by the hair and yanked.

A small sound like tape being ripped came from somewhere, and his wig came clean off. The gleaming bald crown hidden beneath it was exposed.

“What is this?!”

“From now on, if you lie or keep claiming ignorance in response to my questions, I’ll pluck your hair out by the handful.”

“……!”

After that, everything proceeded smoothly. All kinds of information poured from the mouth of a balding man desperate to protect his hair by any means necessary.

“Hong Woojin?”

“Yes. He’s a B-rank mage hired from outside by Team Leader 1. Like me, his specialty is Familiar magic.”

“Really?”

What a waste. I should have caught that bastard and beaten the information out of him, too.

*I’ll run into him someday. If it takes too long, I can always track him down myself.*

Smacking my lips, I continued extracting information. Whenever Kim Junsu seemed to hesitate, I encouraged him by fiddling with his remaining hair.

“That’s everything. I really mean it, that’s all. Even though I’m in the Security Team, I truly don’t know anything else. So please, just leave my hair alone…”

His tone was full of both resentment and sincerity. The final words in particular struck a chord with me.

*This should be more or less everything.*

The mastermind behind it was the Sangdong Guild—or, more precisely, Im Chunsoo.

After seeing that his spendthrift son had been shaken down for a hundred million won in income, he had started digging into our Guild.

Well, in the end, I was the one who robbed him instead.

“The Guild Master won’t let this go.”

“Is that some line reserved for weaklings? Forget invoking the Guild Master and clean up the shit you made yourself.”

“……Tch.”

At my sharp retort, Choi Byungil lowered his head in frustration. But the man wasn’t entirely wrong.

*The Sangdong Guild Master is going to be pretty pissed when he finds out.*

He had sent his subordinates to watch me, only for them to get robbed and captured instead. For the Guild Master—and the Guild as a whole—this was about as fucking humiliating as it got.

Given the seriousness of the matter, I could only hope they would quietly bury it and move on.

*Should I call Team Leader Choi?*

That was when it happened.

010-xxxx-xxxx

A call from a number I didn’t recognize.

What was this?

A strange tension rose within me for no apparent reason as I answered.

“Hello?”

“Come downstairs. I’m waiting below.”

“Huh? I think you have the wrong number.”

“Jin Taekyung. That’s right, isn’t it?”

“Well, yes, but… who are you?”

“My name is Im Chunsoo. I heard you have a few of my people with you.”

“……”

“Are you listening?”

I was listening. I just couldn’t speak.

The Guild Master of a mid-sized Guild had come all the way here himself to meet me. And it was Im Chunsoo, of all people—the man with the terrible temper.

“Come down. We can clear up any misunderstandings over a meal.”

There was no misunderstanding that needed clearing up, but I had no idea what would happen if I said, *No.*

Hadn’t the man already found out my location?

In the end, I had only one option.

“I’ll be down shortly.”

* * *

Im Chunsoo’s first impression was intense. He was younger than I expected, and although his eyes seemed gentle, they burned with heat.

*Fiery.*

Ironically, that was my first thought upon meeting a master of ice magic.

“Hello. My name is Jin Taekyung.”

“I’m Im Chunsoo.”

His voice was cold, unlike his burning gaze. At last, he seemed like someone who deserved the nickname Frozen.

“It’s interesting to see in person the face I’d only seen in report photos.”

There were actually people who could admit so bluntly and without embarrassment that they had dug into my background.

“What about my people?”

“They’re upstairs.”

“Are there any fatalities?”

“Of course not. I have no desire to become a criminal.”

“I appreciate that.”

Im Chunsoo gave me a slight nod.

“My people got impatient and made a mistake. Can you let it slide?”

“If there’s reasonable compensation.”

Im Chunsoo let out a quiet laugh, and the man beside him, who looked like a Team Leader, frowned.

“Young man, you’re rude.”

“I am, somewhat… but hearing that from someone who even put me under surveillance feels a little strange.”

“Even so—”

The man couldn’t continue. Im Changsoo raised a hand to stop him.

“Team Leader 1, go upstairs and release my people.”

“……Yes, Guild Master.”

If Kim Butler possessed a gentle charisma, this man possessed a rough one. Maybe it was because they were both mages. Somehow, the two men overlapped in my mind.

“Come take a walk with me.”

Im Changsoo went ahead, and I followed behind him.

“Do you know something?”

After walking briskly for a while, Im Chunsoo suddenly spoke.

“Once I have a grudge against someone, I have to see it through to the end. I don’t know about you, but that’s the kind of person I am.”

*Very Murim of him.*

The strong devour the weak. Survival of the fittest. It seemed the blood of a Murim tough guy flowed through this man’s veins, too.

“That’s how I built the Sangdong Guild. I climbed higher by stepping on what I had brought down and salvaging whatever I could.”

“I see.”

“What about the Peace Guild?”

“……What do you mean?”

“The past decade has been dull. We’re allies with every nearby Guild, and we haven’t had a rival for a long time. Then you people appeared.”

As I looked into his eyes, where curiosity and passion seemed to be boiling, I had only one thought.

*This is dangerous.*

Whether I cared or not, Im Chunsoo continued speaking.

“Your Guild Master and Team Leader are people whose information I can’t easily access myself… But more than anything, your existence has stirred me up.”

We were climbing a hill now. Despite his considerable age, Im Chunsoo didn’t seem short of breath.

“Do you know why I came all the way here?”

“To see me.”

“You’re only half right.”

Im Chunsoo’s footsteps stopped. Slowly turning around, he released a frigid chill from his entire body.

> **System**
>
> Level 75 Im Chunsoo

“At my age, time is money. I’m not so indulgent that I’d come all the way here just to see your face.”

Frozen. The seasoned A-rank mage who had fought his way through the Great Cataclysm himself.

The moment he extended his hand toward me—

Hissssss.

Around a dozen ice spikes formed in the empty air above my head. The midsummer air froze, and frost settled over the scorching dirt path.

*I’d been well and truly caught.*

I had thought he was an old man with some sense of propriety. I never imagined he would launch straight into something like this.

“Do you really have to go this far?”

“I’m going this far because it’s you.”

“I’m only a C-rank.”

“Exactly. I want to see what that C-rank Hunter can do.”

The moment he finished speaking, Im Chunsoo clenched his fist. The ice spikes, streaming with biting cold, shot toward me.

Whoosh!

But they couldn’t even touch the hem of my clothes.

“Rise up. Fire Wall.”

At the sound of a clear voice, the mana permeating the air began to churn. The ground, which had been frosted over by Im Chunsoo’s magic, melted as flames surged upward.

Fwoosh! Fwoosh!

It was exactly what its name suggested: a wall of fire. Blue flames swallowed the ice spikes and split the space between Im Chunsoo and me.

Beyond the wavering flames, Im Chunsoo cried out in shock.

“What is this…!”

But I wasn’t looking at Im Chunsoo.

Behind him, a man standing at the entrance to the hiking trail greeted me in a gentle voice.

“I’m glad I’m not late. Chunsoo, you’re here too.”

> **System**
>
> Level 80 Kim Hwajong

Kim Hwajong.

Kim Butler had arrived.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 100`.

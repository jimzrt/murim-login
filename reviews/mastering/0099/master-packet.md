# Master Edit Task — Chapter 99

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
| 임춘수    | **Im Chunsoo**    |
| 임창수    | **Im Changsoo**   |
| 홍우진    | **Hong Woojin**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 레벨               | **Level**                      |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 평화 | **Peace Guild** | Guild name. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 당장은 | polysemy | Right away / for now / at the moment; not the broader “anytime soon.” | anytime soon |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 90–94

## Plot

During a week of paid vacation, Jin Taekyung begins arranging to buy and remodel his family’s former home. He reunites with former classmate Park Jihwang, now Park Jihoon, a Hunter in Myeongdong Guild whose strength appears comparable to or greater than Im Changsoo’s.

Sangdong Guild investigates Taekyung after Im Chunsoo receives reports of his impossible recent feats. Chunsoo orders expanded surveillance while Sangdong’s Team 1 Leader remains skeptical. Hong Woojin, a B-rank mage and information broker, monitors Taekyung through tiny Familiars. Taekyung detects and drives away the Familiars around his home, concludes the controllers must have been nearby, and decides to catch them himself.

Taekyung purchases and stores 350 million won worth of low-rank weapons at the Ilsan Store. On returning home, he learns that Hayeon has found an abandoned kitten and received permission to foster it. Taekyung identifies the kitten through the System as a level-two Cat—Familiar, raising the possibility that it is connected to the surveillance.

## Continuity

- Peace Guild’s Guild house will finish remodeling in one week; Taekyung is on paid vacation until then.
- Choi Minwoo and Butler Kim suspect Taekyung may be a third-awakening Hunter, but this remains unconfirmed.
- Taekyung agreed to buy his former family home for 3.38 billion won, paid the ten-percent deposit, and plans to remodel it and move after Hayeon’s college entrance examination.
- Park Jihwang changed his name to Park Jihoon and works in Team 1 of Myeongdong Guild.
- Im Chunsoo ordered Sangdong Guild’s Audit Team to expand surveillance of Taekyung. Sangdong’s Team 1 Leader, Chunsoo’s loyal right hand and the Guild’s only other A-rank Hunter, doubts the reports of Taekyung’s feats.
- Peace Guild’s Guild Master and Team Leader remain protected by an unexplained security Lock that hides their personal and account information.
- Hong Woojin is investigating Taekyung with Familiar magic. He severed the Link to his rice-weevil Familiar and intends to continue with more conspicuous surveillance.
- Taekyung’s Qi Sense reaches seventy meters and detected the Familiars in his home, but tiny Familiars generally evade ordinary detection magic.
- A B-rank mage’s Familiar connection reaches up to 500 meters, with approximately 300 meters considered a safe operating distance. Forced Link severance causes physical distress and may cause mana backflow.
- Taekyung spent 350 million won at the Ilsan Store and stored the weapons in his Inventory.
- Hayeon is temporarily fostering an abandoned level-two Cat Familiar with Kim Jeonghee’s permission. Its owner and connection to the surveillance are unknown.
- Retaliation by Im Chunsoo or Sangdong Guild, Woojin’s motive, Hayeon’s schooling, and the existence of third-awakening Hunters remain unresolved.

## Translation Decisions

- Use **third-awakening Hunter**, **third awakening**, **Frozen**, **Qi Sense**, **Familiar**, **Link**, and **Lock** as established.
- Render **Park Jihwang** and **Park Jihoon** for the former and current names.
- Use **Myeongdong Guild**, **Team 1 Leader**, **Audit Team**, **Ilsan Store**, **Assistant Manager**, and **Cat—Familiar**.
- Retain **jeonse** with its explanatory gloss, **goshiwon** with its established footnote, and **samgyetang** with its explanatory footnote.
- Preserve the established explanatory footnote for **백조** and the forum author’s exaggerated comic voice.

### Prior accepted reading-copy tails

#### Chapter 97 tail (verified mastered)

…
in the last few moments. “What do we do about the transcript and the statements?” “What do you think? If you don’t want to watch the Team Leader throw a fit, you have to write them. Want to go to the hospital and get a medical statement?” “…” “Just slap something together. I’ll cover for you and say you couldn’t write yours because you were using Familiar magic.” After heaving deep sighs, the two men began cursing the Team Leader in earnest. All the while, the conversation continued through the transmitter. —It’s nice. It faces south, so it gets plenty of sunlight. What about the building next to it? Don’t tell me that one’s gone, too? —Huh? No, it’s still available. Business has been slow lately, so the places that went recently were… Wait, young man. —Yes? —Your arm is really firm. Goodness, just look at those muscles and veins. —… * * * “Young man, come again! Come twice!” I left the real-estate office with the ajumma’s regretful farewell behind me. Goose bumps had risen all over the arm her hand had just brushed. *Whether it’s an ajumma or an ajusshi, people who grow old without growing up are all alike when it comes to hitting on younger people.* I left as if fleeing her sticky gaze, but I had already accomplished what I’d gone there to do, so I had no regrets about leaving. *Confirm the listings that were recently sold or leased.* Today was exactly five days after the raid with Im Changsoo. In other words, the surveillance team couldn’t have been assigned to me more than five days ago. *I tried to act and ask about it indirectly without making it obvious, but…* Knowing that eavesdropping magic was in place, every word and action had been deliberate. I wanted to come across as an unremarkable C-rank Hunter packed full of arrogance and extravagance. *Whether they fell for it or not was another matter.* My conversation with the real-estate ajumma had given me an important clue. I silently muttered the addresses I had memorized in advance. *Building 5, Unit 901. Building 4, Unit 302. Building 3, Unit 202.* These were the three listings that had changed hands in the past five days. I had used our house as the center point and set the range at a maximum of five hundred meters—the distance Familiar magic could reach. The watchers were definitely somewhere within that range. *The problem is how to find them.* My goal wasn’t to drive them away. I wanted to catch them, beat the hell out of them, and find out who was behind them. If I went after the wrong place too soon, they might catch on and run. *They could be hiding in a car, so I should check the parking lot too.* Searching the nearby homes would tip them off, but I could search the parking lot without looking suspicious. All I had to do was pretend to take a walk while sweeping the area with Qi Sense. Game over. > **System** > > **Lv. 42 Kim Gwondong** “Oh, we meet again.” Just like this guy. I greeted Kim Gwondong when he called out to me. “Indeed. We meet again.” “You said you were going to the real-estate office. Finished already?” “I just asked a few questions. But when I actually went there and looked into it, the house prices weren’t exactly cheap. I ran right back out.” “That’s this neighborhood for you. Still, you’re doing well for yourself, young man. At your age, all I did was sit at home and eat my parents’ food.” “Doing well? Ha-ha.” If he knew what real ability looked like, he’d faint. Kim Gwondong laughed along, unaware of my thoughts, then spoke. “Well, I should get going. I need to walk to the park over there and back.” “You must like taking walks.” “Huh? It’s not that I do it because I like it. I do it because I need to. You’ll have a hard time too once you reach my age.” He conspicuously waved his thin arms and legs. To all appearances, he was just a scrawny, potbellied middle-aged man. *He certainly looks like a civilian.* Anyone else would have fallen for it completely. But there was no such thing as a Level 42 civilian. *Probably a C-rank Hunter. Judging by his build, he likely specializes in stealth and pursuit.* Once you knew someone was a Hunter, there was plenty you could infer. I said goodbye to Kim Gwondong. “Then I’ll see you next time.” “Maybe you will, maybe you won’t. Ha-ha.” Well, I definitely wanted to see him. Of course, when that happened, I wouldn’t be parting from him with a smile and a laugh like I was now. I wanted to knock him flat right then and there, but it wasn’t time yet. I gave him a slight bow and turned to leave when his voice came from behind me. “Oh, right. That cat seemed awfully smart. I saw it on my way over, and it was still there.” He had even given me a friendly reminder not to forget to pick up my Familiar. And just as he said, the cat was waiting for me in the same spot as before. “Meow.” Right. Hyung’s here, you punk. [^1]: Yulmu tea is a sweet Korean grain beverage made from roasted Job’s tears.

#### Chapter 98 tail (verified mastered)

…
she would jump whenever I suddenly spoke to her. Something had definitely changed around Mom. *She’ll tell me when the time is right.* My mother was the person I loved and trusted most in this world. As always, all I could do was trust her and wait. Of course, listening to her and talking things over at the right time was also a child’s duty. “What are you thinking about so hard?” “It’s nothing. By the way, aren’t you going out?” “What? You sound like you want me to leave.” “Not exactly.” “Hmm. Suspicious. You’re not planning to bring a girlfriend over, are you?” “…” *I wish I had a girlfriend to bring over.* My expression must have revealed my thoughts, because Hayeon hesitated. “Ah, I’m sorry.” “Don’t apologize. It makes me twice as pathetic.” “I’m really sorry.” “You’re doing this on purpose, aren’t you?” “Come to think of it, I have some books to return to the library.” She sprinted into her room, threw on her backpack, and came back out at the speed of light. The front door slammed shut, and the house fell silent. *She really went and gouged out a single man’s heart.* A corner of my chest felt hollow, but the stage I had been waiting for had finally been set. This was a problem I needed to deal with while my family was out of the house, if possible. *Myaow.* *Meow.* The two cats, one black and one white, crept toward me and began circling. Bright eyes. Perked-up ears. I left the Familiars, who were dying to learn more about me, behind and stepped onto the balcony. The first thing I saw was the parking lot, where hundreds of cars were lined up. *The parking lot is clear.* Before returning home, I had carried the Familiar in my arms and taken a lap around the apartment complex. To everyone else, I probably looked like an idler out for a walk on a pleasant day. My real purpose had been to check the vehicles. The result was nothing suspicious. *Then it has to be one of those apartments.* That confirmed the watchers had made one of the recently sold or leased apartments their base. I recalled the information I had obtained from the real-estate office once more. *Building 5, Unit 901. Building 4, Unit 302. Building 3, Unit 202.* Coincidentally, all three were positioned around our apartment, forming a ring. Their windows also overlooked the building entrances, making them ideal for surveillance. The watchers could have been in any one of them. *The question is which one they’re hiding in…* They were cautious enough to use a Familiar instead of magical Equipment to avoid being discovered. If I approached recklessly, I would lose them. To make a definite capture, I had no choice but to throw out equally substantial bait. *Time to get started.* Swish. Rustle. First, I drew every curtain in the house. Though it was the middle of the day, the living room grew dim. Standing in its center, I reached into my pocket. *Inventory open. Mana-detection Equipment.* At the same time, my hand closed around a lump of metal half the size of my palm. As its name suggested, it was Equipment that could detect mana. I had paid twenty million won for it at the Store. *Next step: search.* I carefully swept through the house with the detection Equipment. After confirming that no mana was being detected inside, I took out my smartphone and called someone. Beep. Beep. Click. The call connected, and the other person answered. —Hello? I replied, “It’s me, Jin Taekyung.” The two Familiars watched me without even seeming to breathe. * * * The moment Kim Junsu opened his eyes, he shouted. “He’s here! He’s here!” The Security Team members, who had been huddled together writing their assessments, jumped in surprise. “What?” “Who’s here? Our Team Leader?” “Or could it be…” Kim Junsu nodded at the team member who had trailed off. “The target. This bastard reeks of something rotten.” “Seriously?” “Yes. I got a bad feeling when he drew all the curtains as soon as the house was empty, and then he even used detection Equipment to inspect the inside.” That wasn’t something an ordinary C-rank Hunter would do, especially while on vacation. Everyone in the room swallowed hard. “Th-then what?” “He pulled out his phone and made a call.” “A call? To whom?” “I don’t know.” Kim Junsu furrowed his brow. “The call was so short that it didn’t even last three minutes. But more than that, I could tell he was being extremely careful about how he addressed the other person.” “That’s enough. We’ll report it up the chain and have them pull that bastard’s call records.” “Right. Was there anything else?” “Of course there was. Do you know what he said?” Ahem. After clearing his throat, he lowered his voice. “‘The plan is proceeding without a hitch. Yes, yes. The Sangdong Guild hasn’t noticed anything yet. I have the item with me.’” The team members listening slapped their knees. “This is it!” “We finally got something!” “Wow, I just got chills. What is he, some kind of secret agent?” At that moment, Kim Gwondong, who had been listening quietly, suddenly spoke. “Junsu, didn’t that bastard say he had some kind of item?” “Good observation.” Kim Junsu smiled meaningfully. “That guy has a USB.”

## Korean source

```text
＃99화



보안팀장이 한 통의 전화를 받은 것은 사우나를 막 끝마친 직후였다.

- 팀장님. 접니다, 김권동.

“어, 녹취록이랑 소견서 다 썼냐?”

- 아뇨. 그게 아니라…….

“이 자식이 진짜. 최고참이라고 편의 봐줬더니 정신 못 차리지? 당장 10분 안에 소견서 작성해서 보내.”

- 아이 참, 그게 아니고요. 특이 사항 때문에 보고드리려고 전화한 겁니다.

잠시 후, 보안팀장은 들고 있던 맥반석 계란을 툭 떨궜다.

“USB를 갖고 있었다고?”

- 네. 통화 상대가 누군지는 모르지만 물건 잘 갖고 있다면서, 본인도 슬쩍 꺼내서 확인했다고 합니다. 준수가 직접 봤다니까 확실합니다.

“그, 그래서?”

- 표적이 직접 보관 중이라는데…… 당장은 준수도 어떻게 할 방법이 없어서 보고드립니다.

“준수, 준수는? 당장 바꿔 봐.”

- 지금 패밀리어로 표적 감시 중이라 곤란할 것 같은데요.

보안팀장은 입술을 질끈 깨물었다. 방금 보고받은 내용으로 머릿속은 뒤죽박죽이었다.

‘전화 상대는 누구지? 표적의 정체는? USB 안에는 대체 뭐가 들어 있을까?’

보안팀장의 본능이 꿈틀거리기 시작했다.

“김권동이. 이거 길드장님께서 특별 지시 하신 거야. 알지? 내가 몇 번이나 말했잖아.”

- 그거야 다들 알죠.

“뭐 하나라도 건지면 다 같이 대박 나는 거라고. 나도 위로 올라가고, 너도 짬 먹을 만큼 먹었으니까 팀장 달아야 할 거 아냐.”

- ……그게 제 맘처럼 되나요. 적어도 B급은 되어야 팀장 달아 주는 거 모르는 처지도 아니고.

“내 생각에 이거 충분히 건수 된다. 진태경 그놈이 어디에서 굴러먹다 온 놈인지는 모르겠는데 그림 딱 나와. 우리 상동 길드 언급하면서 대화하는 내용만 들어 봐도 알잖아. 그치?”

- 저도 좀 그렇게 생각하긴 했습니다.

계획은 차질 없이 진행되는 중이며, 상동 길드는 아직 눈치채지 못했다. 그리고 물건은 잘 간수하고 있다.

정체를 알 수 없는 상대와 진태경의 대화는 제삼자가 듣기에도 충분히 의미심장한 내용이었다.

하물며 상동 길드의 보안팀이라면 말할 것도 없다.

“그 USB가 핵심이야. 막말로 진태경이 소속된 평화 길드건, 어느 경쟁 길드건 간에 우리 길드 한번 엎으려고 수 쓰는 거면…….”

- 그런 거면 진짜 특급 정보죠.

보너스는 기본이고 승진은 옵션이다. 길드장의 눈에 든다면 무난하게 길드 임원까지 노려 볼 수 있다.

지금 이 순간, 보안팀장은 길드장의 오른팔이 된 자신의 모습을 상상했고 김권동은 상동 길드 최초의 C급 팀장이 되는 꿈에 젖었다.

“계속 주시해. 난 일단 윗선에 보고하고 진태경 통화 내역부터 조회할 테니까.”

- 넵!

“나 옷만 갈아입고 바로 간다. 아무리 늦어도 저녁 먹기 전에 표적이 어떤 놈이랑 통화했는지 뜰 테니까 그전까지 대책을 세워 보자고.”

보안팀장이 탈의실로 달려가려던 그때였다.

- 아, 팀장님. 그런데 한 가지 걱정되는 부분이…….

“뭔데.”

김권동의 목소리에서 불안함이 읽힌다. 그리고 불길한 예감은 빗나가지 않고 적중했다.

- 홍우진이 있잖습니까.

“아, 젠장.”

실수다. 너무 흥분한 나머지 홍우진의 존재를 잠시 잊고 있었다. 보안팀장은 마음이 조급해졌다.

‘그놈이 먼저 움직이면 곤란한데.’

그가 아는 길드장, 임춘수는 상벌이 명확한 인물이었다.

신입이어도 실력을 입증한다면 출셋길에 아스팔트를 깔아 주고, 아니다 싶으면 10년을 근무한 길드원이라도 망설임 없이 쳐 내는 성격.

‘한두 번 본 게 아니지.’

단순히 홍우진에게 공(公)만 뺏기고 끝날 리가 없다. 보안팀장 자신의 밥그릇이 달려 있다.

돈? 그따위 문제가 아니다. 반평생을 몸담은 길드, 올라갈 수 있는 데까지는 가 보고 싶었다.

“권동아.”

- 예.

“그놈, 지금 집에 혼자랬지?”

- 팀장님, 설마? 안 됩니다!

“아직 말 안 끝났다.”

목소리가 커진 김권동과는 달리 보안팀장은 침착했다.

“이 일, 표적 제압하고 물건 챙겨서 가면 깔끔하게 끝난다. 어차피 C급이야, 쫄 거 없어.”

- 구린내가 풀풀 나는 C급이죠. 잘못 건드렸다가 저희가 역으로 당할 수도 있습니다.

“당해? 이제 겨우 C급으로 각성한 풋내기한테 B급 베테랑인 내가? 이거 자존심 상하네.”

- …….

“너, 설마 임창수가 했던 말 믿는 건 아니지? 그게 사실이면 진태경이 사실은 A급 헌터라는 소린데…… 그럴 거면 차라리 길드장님이 첩자라고 해라. 응?”

- 아니, 무슨 말씀을 그렇게까지 하세요.

“됐고. 할 거야, 말 거야?”

- 하, 씨. 미치겠네.

깊은 한숨을 푹푹 내쉬던 김권동이 마음의 결정을 내린 것은 잠시 후였다.

- 우리 이거 걸리면 범죄자 되는 겁니다. 아시죠?

“알지. 안 걸리면 무죄라는 것도.”

- 팀장님, 진짜 간도 크시네요.

“그러니까 팀장이지. 애들은?”

- 지금 다 모여 있습니다. CCTV 파악은 투입된 첫날에 끝냈고 간단한 변장 장비도 있어요.

“좋아.”

- 언제 시작합니까?

보안팀장은 마른 입술을 핥았다.

“내가 도착하는 즉시.”

옛말에 이르기를 쇠뿔도 단김에 빼라고 했다. 그에게 있어 C급 헌터는 한 손으로도 뽑을 수 있을 만큼 물렁한 뿔이다.



* * *



낚시가 성공했다고 느낀 것은 얼마 지나지 않아서였다.

야옹.

미야옹.

내 환심을 사기 위한 두 패밀리어의 애교 세례. 그러나 이번에는 좀 다르다.

짧은 다리로 버둥버둥 소파에 올라오더니 다른 곳도 아닌 허벅지 위에 자리 잡는 모습을 보니 확신이 들었다.

‘미끼를 물었구나.’

주머니에 들어 있는 USB가 미끼다. 감시자들은 지금쯤 궁금해서 미칠 지경일 거다.

내가 통화에서 말한 계획과 전화를 받은 상대방은 누군지, 이 USB에는 도대체 뭐가 들어 있는지.

‘생각보다 과감한 놈들이었으면 좋겠는데.’

그들이나 나나, 오래 끌어서 좋을 게 없다. 평일 오후, 아파트 단지는 한적했고 TV에서는 재미없는 귀농 다큐멘터리가 방영되고 있었다.

“아, 오랜만에 뒷산이나 갈까…….”

혼잣말을 중얼거리고 현관문을 나서려던 그때, 기다리던 변화가 일어났다.



[Lv.2 고양이]

[Lv.2 고양이]



패밀리어 마법의 해제. 이 현상이 뜻하는 바는 명백했다.

‘이제야 본격적으로 움직이는구나.’

새끼 고양이의 몸으로는 내게서 USB를 훔칠 수 없다. 하지만 표적인 내가 직접 인적이 드문 곳으로 이동한다면 이야기가 달라진다.

‘누가 봐도 고만고만한 C급 헌터, 마음 놓고 뺏을 수 있다고 생각하겠지.’

물론 그 과정에 적당한 폭력과 협박도 포함되어 있을 거라는 건 충분히 예상할 수 있었다.

단, 감시자들은 가장 중요한 한 가지를 착각했다.

바로 나라는 존재다. 항상 가해자였던 그들은 자신들이 피해자가 될 수도 있을 거라는 생각을 하지 못한다.

‘기대되네. 어떤 놈들일지.’

허락 없이 불법 스토킹을 하면 어떻게 되는지 똑똑히 보여 줄 생각이다.



* * *



진태경이 부동산에서 얻은 정보는 절반만 맞았다. 상동 길드의 보안팀과는 달리 홍우진의 아지트는 그가 전혀 예상치 못한 곳에 있었다.

바로 진태경이 사는 아파트 옥상이었다.

“후우.”

패밀리어와의 링크를 해제한 홍우진은 옥상에 딸린 자그마한 비품 창고에서 눈을 떴다.

그는 경비원에게 약간의 돈을 찔러 주는 것으로 5평 남짓한 최적의 공간을 며칠간 마련할 수 있었다.

“이거 일이 더럽게 꼬였네.”

심상치 않은 진태경의 통화, 뭐가 담겼는지 모를 USB.

드디어 정보라고 할 만한 걸 알아냈지만 그건 상동 길드 쪽도 마찬가지다.

비품 창고에서 나온 그는 옥상 밑을 내려다봤다. 까마득한 저 아래, 막 아파트 입구를 나서는 진태경이 보였다.

‘따라가야 하나, 말아야 하나.’

의뢰를 생각한다면 따라가는 게 맞는데, 어쩐지 꺼림칙하다. 홍우진이 갈등하는 눈빛으로 멀어져 가는 진태경을 지켜보던 그때였다.

“허, 이것 보게?”

한 명, 그리고 다시 한 명. 슬금슬금 기어 나오는 꼴이 딱 먹이를 노리는 뱀의 그것과 다르지 않다.

그 숫자가 도합 여섯.

각자 복장도 다르고 행동거지도 일반인과 다름없지만 업계 동업자인 홍우진의 눈에는 똑똑히 보였다.

“상동 길드 놈들이군.”

한두 명도 아니고 자그마치 여섯이 몰려나왔다.

더군다나 표적의 목적지는 인적이 드문 야산. 곧 벌어질 일을 짐작한 그가 미간을 찡그렸다.

“가지가지 한다. 아주.”

무력행사는 홍우진의 기준에서 벗어나는 일이다. 처음 의뢰를 맡을 당시 신신당부를 했음에도 보안팀을 투입시켰을 때 관뒀어야 했는데……. 이건 도를 지나쳤다.

‘진태경, 저놈은 내 손으로 털고 싶었는데.’

정체가 궁금해지는 놈이지만 딱 여기까지다. 더 이상 얽히면 안 될 것 같다는 예감이 들었다.

‘상동 길드, 이 양아치 새끼들.’

혀를 찬 홍우진이 스마트폰을 꺼내 문자를 발송했다.

수신인은 1팀장. 문자 내용은 짧고 간략했다.



〈 1팀장



일 접습니다.



옥상을 떠나기 전, 이미 사라진 진태경의 명복을 빌어 주는 것도 잊지 않았다.

‘거, 더러웠고 다신 보지 말자.’

그로서는 여러모로 재수 옴 붙은 의뢰였다.



* * *



묵묵히 산길을 올랐다. 이미 등산로를 벗어난 지 오래다.

하지만 멈추지 않는다. 깊숙이, 더 깊숙이 계속해서 걸음을 옮길 뿐.

그러던 어느 순간 너른 평지가 모습을 드러냈다. 무릎에 닿을 정도로 높이 자란 잡초가 무성한 그곳에서, 나는 천천히 돌아섰다.

“아직도 산책 중이신가 봐요?”

앞서 두 차례 마주친 바가 있는 중년인, 김권동은 말없이 얼굴을 굳혔다.

“대답이 없으시네. 옆에 계신 분은 누구?”

“친구.”

김권동이 어디서나 찾아볼 수 있는 흔한 인상이라면 지금 대답한 이 남자는 정반대였다.

조폭도 울고 갈 만큼 험악한 인상에 거구의 소유자. 그의 입술 사이로 걸걸한 음성이 흘러나왔다.

“다 알면서 왜 여기까지 왔지?”

“뒤에서 졸졸 따라오시길래. 어디까지 따라오나 본 거죠. 똥개 훈련이라고 생각하시면 편해요.”

남자가 너털웃음을 터트렸다.

“어린놈이 당돌하네. 몇 살이냐?”

“역마살이요.”

“매를 버는 재주가 있구나.”

“칭찬 감사합니다, 최병일 씨.”

남자, 최병일이 입을 다물었다. 그의 눈동자가 흔들렸다.

“……어떻게 알았지?”

“그거야 영업 비밀이죠. 그런데 김권동 씨랑 친구 맞아요? 외관상으로 봤을 때는 투샷이 영 아닌데.”

이번에는 김권동이 당황할 차례다. 하지만 내 말은 아직 끝나지 않았다.

“친구가 아니라 대답하기 곤란한가? 그럼 다른 네 분한테 물어볼게요. 박형진, 오규현, 이민철, 김준수 씨는 솔직하게 대답해 주셨으면 좋겠네요.”

우우웅.

허공이 일렁이더니 네 사람이 뚝 떨어져 내린다. 머리 위로 레벨창을 각자 달고 있는 그들은 귀신이라도 본 듯한 얼굴이었다.

“다들 뭘 그렇게 놀라시나. 숨이라도 편하게 쉬시라고 배려해 드린 건데.”

최병일이 이를 악물었다. 처음의 여유는 온데간데없고 초조함과 당황에 물든 얼굴이다.

“이런 씨팔…… 너 뭐 하는 새끼야?”

먼저 욕 박았으니까 어른 공경은 여기서 끝이다. 나는 최병일을 보며 피식 웃었다.

“아직도 몰라? 내 정보 싹 긁었을 텐데. 패밀리어까지 붙여 놓을 정도면 말 다 한 거지.”

“……!”

“집에 나 혼자였으면 그러려니 했겠는데, 가족들까지 감시당할 거 생각하니까 좀 열받더라고. 그래서 미끼 한번 던져 봤더니 덥석 물데?”

여섯 명의 감시자들이 몸을 부르르 떨었다.

“그, 그럼 USB도?”

“아, 그거? 내가 평생을 바쳐 모은 야동 컬렉션.”

인벤토리에 소중히 보관해 놨던 인류의 보물이다.

“말도 안 돼! 분명히 촉이 왔는데.”

“음. 말도 안 되는 작품들이 수두룩하긴 하지. 남자라면 촉이 오는 것도 당연한 거고.”

하나같이 망연자실한 얼굴로 서 있는 그들을 향해 말했다.

“성실하게 대답해 줬으니까 나도 하나만 물어보자.”

한 명, 한 명. 나와 눈이 마주칠 때마다 몸을 움찔거린다.

마침내 내 시선이 멈춘 곳에는 빼빼 마른 20대 남성이 서 있었다. 아마도 이놈이 패밀리어 마법사겠지.



[Lv.41 김준수]



“준수야. 너희 상동 길드에서 보내서 왔지?”

“입 닥쳐!”

최병일이 외쳤지만 김준수는 이미 대답을 끝낸 후였다.

핏기 하나 없이 창백해진 얼굴이 바로 그의 대답이다.

“오케이, 상동 길드. 그럴 줄 알았다.”

내 말을 들은 최병일의 얼굴이 딱딱하게 굳었다.

“그 이름은 입에 담지 말았어야지.”

“왜, 죽이게?”

“……널 사로잡고 생각해 보지.”

“그거 되게 힘들 텐데.”

최병일의 레벨은 60대 중반. 느껴지는 기세는 임창수와 비등하고 나머지는 그저 그런 3, 40레벨 정도의 C급이었다.

전문적인 레이드 팀도 아닌 이들이 나를 사로잡을 확률은 매우 희박하다.

“죽을 각오로 덤벼. 그래야 내 손목에 나비매듭이라도 묶을 수 있지.”

“쳐!”

최병일의 외침과 함께 상동 길드의 감시자들이 사방에서 달려들기 시작한다.

쉬이이익!

어깨 위로 떨어지는 단검 한 자루가 시작이다.

나는 느릿느릿하게만 보이는 그 궤적을 향해 손을 뻗었다.

그와 동시에…….

‘인벤토리 오픈. 장착.’

콰직!

공력을 한껏 머금은 검날이 적의 단검을 부쉈다. 이름 모를 잡초 위로 조각난 날붙이와 누군가의 핏물이 쏟아진다.

“들어와, 이 스토커 새끼들아!”

쐐애애액!
```

## Current accepted English baseline

```markdown
# Chapter 99

The Security Team Leader received a phone call just after finishing up at the sauna.

“Team Leader. It’s me, Kim Gwondong.”

“Oh, did you finish writing the transcript and assessment?”

“No, sir. That’s not it…”

“You little shit. I went easy on you because you’re the most senior one here, and now you’re getting careless? Write up your assessment and send it to me within ten minutes.”

“Come on, that’s not it. I’m calling to report something unusual.”

A moment later, the Security Team Leader dropped the roasted egg he was holding.

“He had a USB?”

“Yes. We don’t know who he was talking to, but he said he was keeping the item safe, and he even slipped it out to check it himself. Junsu saw it directly, so it’s certain.”

“Th-then?”

“The target is keeping it on him, apparently… Junsu has no way to do anything about it for now, so I’m reporting it.”

“Junsu? Put Junsu on right now.”

“He’s watching the target with his Familiar, so that might be difficult.”

The Security Team Leader bit down hard on his lip. His head was a complete mess after hearing the report.

*Who was the person on the phone? What was the target’s true identity? And what on earth is inside that USB?*

The Security Team Leader’s instincts began to stir.

“Gwondong. This was a special order from the Guild Master. You know that, right? I’ve told you so many times.”

“Everyone knows that.”

“If we manage to get even one thing out of this, we all hit the jackpot. I’ll move up, and you’ve been around long enough that you ought to become a Team Leader, too.”

“…It’s not as simple as wishing for it. You know perfectly well they won’t make someone a Team Leader unless they’re at least B-rank.”

“I think this is more than enough to make a real score. I don’t know where that Jin Taekyung bastard came from, but the picture is obvious. You can tell just by listening to him talk about our Sangdong Guild. Right?”

“I did think it looked that way.”

The plan was proceeding without a hitch. Sangdong Guild still hadn’t noticed anything. And he was keeping the item safe.

The conversation between Jin Taekyung and the unknown person on the other end of the line was suspicious enough to sound meaningful even to a third party.

For Sangdong Guild’s Security Team, there was no question.

“That USB is the key. To put it bluntly, whether it’s the Peace Guild Jin Taekyung belongs to or some rival Guild, if they’re making a move to bring down our Guild…”

“Then that’s seriously high-value intel.”

The bonus was a given, and promotion was an option. If he caught the Guild Master’s eye, he might even be able to aim for a position among the Guild executives.

At that very moment, the Security Team Leader imagined himself as the Guild Master’s right-hand man, while Kim Gwondong became lost in a dream of becoming Sangdong Guild’s first C-rank Team Leader.

“Keep watching him. I’ll report this up the chain and start by checking Jin Taekyung’s call records.”

“Yes, sir!”

“I’ll change clothes and head over immediately. No matter how late it is, we’ll know who the target spoke with before dinner. Let’s come up with a plan before then.”

Just as the Security Team Leader was about to hurry to the changing room, Kim Gwondong spoke again.

“Ah, Team Leader. There’s one thing I’m worried about…”

“What is it?”

Anxiety could be heard in Kim Gwondong’s voice. And his ominous premonition proved accurate.

“You know Hong Woojin, right?”

“Ah, damn it.”

It was a mistake. He had been so excited that he had briefly forgotten about Hong Woojin’s existence. The Security Team Leader grew impatient.

*It’ll be a problem if that bastard makes the first move.*

The Guild Master he knew, Im Chunsoo, was a man who made rewards and punishments absolutely clear.

If a newcomer proved their ability, he would pave the road to advancement for them. But if he decided someone was no good, he would cut them loose without hesitation—even if they had been a Guild member for ten years.

*I’ve seen it more than once or twice.*

This wouldn’t simply end with Hong Woojin taking the credit. The Security Team Leader’s own livelihood was on the line.

Money? That wasn’t the issue. He had devoted half his life to this Guild and wanted to climb as high as he possibly could.

“Gwondong.”

“Yes.”

“That bastard is alone at home right now, isn’t he?”

“Team Leader, surely not? You can’t!”

“I’m not finished talking.”

Unlike Kim Gwondong, whose voice had grown loud, the Security Team Leader remained calm.

“If we subdue the target, take the item, and leave, this ends cleanly. He’s only C-rank, after all. There’s nothing to be afraid of.”

“He’s a C-rank who reeks to high heaven. If we make the wrong move, we could be the ones getting taken down.”

“Taken down? By a rookie who only just awakened as a C-rank? Me, a B-rank veteran? That’s insulting.”

“…”

“You don’t actually believe what Im Changsoo said, do you? If that were true, it would mean Jin Taekyung was really an A-rank Hunter… If that’s the case, you might as well say the Guild Master is a spy. Huh?”

“Come on, why are you taking it that far?”

“Enough. Are you doing it or not?”

“Fuck, this is driving me crazy.”

Kim Gwondong let out several deep sighs before finally making up his mind.

“If we get caught, we become criminals. You know that, right?”

“I know. I also know that if we don’t get caught, we’re innocent.”

“Team Leader, you really have some nerve.”

“That’s why I’m the Team Leader. What about the others?”

“They’re all gathered right now. We finished checking the CCTV on the first day we were deployed, and we have some simple disguise Equipment, too.”

“Good.”

“When do we start?”

The Security Team Leader licked his dry lips.

“The moment I arrive.”

As the old saying went, you had to pull the ox’s horn while it was hot. To him, a C-rank Hunter was a soft horn he could yank out one-handed.

* * *

It didn’t take long for me to realize that the bait had worked.

*Meow.*

*Myaow.*

The two Familiars showered me with affection, trying to win my favor. But this time, something was different.

They had struggled up onto the sofa with their short legs, then settled down—not just anywhere, but on my thighs.

*They took the bait.*

The USB in my pocket was the bait. By now, the watchers must have been going crazy with curiosity.

What plan I had mentioned during the call, who I had been speaking to, and what on earth was inside the USB.

*I hope they’re more daring than I expect.*

Neither they nor I had anything to gain by dragging this out. It was a weekday afternoon, the apartment complex was quiet, and the TV was showing a boring documentary about returning to farming.

“Ah, should I go to the hill behind the apartment for the first time in a while…?”

I muttered to myself and was about to leave through the front door when the change I had been waiting for occurred.

> **System**
>
> Level 2 Cat
>
> Level 2 Cat

The Familiar magic had been dispelled. The meaning of this phenomenon was obvious.

*They’re finally making their move.*

In the body of a kitten, they couldn’t steal the USB from me. But if I, the target, moved somewhere sparsely populated on my own, that would change things.

*Anyone looking at me would see an ordinary C-rank Hunter. They’d think they could take it from me without worry.*

Of course, it wasn’t hard to predict that a suitable amount of violence and threats would be part of the process.

But the watchers had made one crucial mistake.

What they had misjudged was me. They had always been the perpetrators, and had never imagined that they could become the victims.

*I’m looking forward to this. What kind of bastards are they?*

I intended to show them exactly what happened when someone illegally stalked another person without permission.

* * *

The information Jin Taekyung had obtained from the real-estate office was only half right. Unlike Sangdong Guild’s Security Team, Hong Woojin’s hideout was in a place Taekyung had never expected.

The rooftop of the apartment building where Jin Taekyung lived.

“Whew.”

After severing his Link with the Familiar, Hong Woojin opened his eyes inside the tiny supply closet attached to the rooftop.

By slipping the security guard a little money, he had secured this optimal space of roughly five pyeong[^1] for several days.

“This job got horribly tangled up.”

Jin Taekyung’s suspicious phone call. A USB whose contents were unknown.

He had finally discovered something that could be called information, but Sangdong Guild had discovered the same thing.

Hong Woojin stepped out of the supply closet and looked down over the edge of the roof. Far below, he could see Jin Taekyung just leaving the apartment entrance.

*Should I follow him or not?*

If he thought about the job, following him was the right choice. But something about it felt wrong. Hong Woojin was watching Jin Taekyung grow smaller in the distance with a conflicted look in his eyes when—

“Huh. What do we have here?”

One person, then another. The way they slowly crawled out was no different from snakes stalking their prey.

There were six of them in total.

Their clothes were all different, and their behavior was no different from ordinary people’s. But to Hong Woojin, a fellow professional in the industry, it was obvious.

“They’re from Sangdong Guild.”

Not one or two of them—six had emerged.

What was more, the target’s destination was a deserted hillside. Realizing what was about to happen, Hong Woojin furrowed his brow.

“They really pull every dirty trick in the book.”

Using force crossed Hong Woojin’s line. He should have quit when they deployed the Security Team, despite his repeated warnings when he first accepted the job. But this had gone too far.

*I wanted to uncover Jin Taekyung’s secrets myself.*

He was a man whose identity had made Hong Woojin curious, but this was where it ended. He had a feeling that he shouldn’t get involved any further.

*Sangdong Guild, you goddamn thugs.*

Clicking his tongue, Hong Woojin took out his smartphone and sent a text.

The recipient was the Team 1 Leader. The message was short and simple.

> **Team 1 Leader**
>
> I’m dropping the job.

Before leaving the rooftop, he also remembered to wish the already-vanished Jin Taekyung a peaceful rest.

*Well, that was filthy. Let’s never see each other again.*

In every respect, it had been a cursed job.

* * *

I climbed the mountain path in silence. It had been a long time since I’d left the hiking trail behind.

But I didn’t stop. I kept walking deeper and deeper into the mountain.

At some point, a broad clearing came into view. Weeds had grown thick there, reaching up to my knees. I slowly turned around.

“Looks like you’re still out for a walk?”

Kim Gwondong, the middle-aged man I had run into twice before, said nothing. His face hardened.

“No answer? Who’s the person with you?”

“My friend.”

If Kim Gwondong had an ordinary, forgettable face, the man who answered me was the complete opposite.

He was huge, with a vicious expression fierce enough to make gangsters cry. A rough voice rumbled from between his lips.

“You already know everything, so why did you come all the way here?”

“You kept trailing me from behind, so I wanted to see how far you’d follow. Think of it as training a mutt.”

The man let out a hearty laugh.

“Young punk’s got nerve. How old are you?”

“*Yeokmasal*.”[^2]

“You’ve got a real talent for earning a beating.”

“Thanks for the compliment, Mr. Choi Byungil.”

The man, Choi Byungil, closed his mouth. His eyes shook.

“…How did you know?”

“That’s a trade secret. But are you and Mr. Kim Gwondong really friends? Judging by appearances, you two don’t exactly look like a matching pair.”

This time, it was Kim Gwondong’s turn to panic. But I wasn’t finished.

“Is it difficult to answer because you’re not friends? Then I’ll ask the other four. Mr. Park Hyungjin, Mr. Oh Gyuhyeon, Mr. Lee Mincheol, and Mr. Kim Junsu, I’d appreciate an honest answer.”

Bzzzzzz.

The air rippled, and four people dropped straight down.

Each of them had a Level window floating over their head, and their faces looked as if they had seen a ghost.

“Why is everyone so surprised? I was just being considerate so you could breathe comfortably.”

Choi Byungil gritted his teeth. All traces of his earlier composure had vanished, leaving his face colored by anxiety and bewilderment.

“What the fuck… What kind of bastard are you?”

Since he had started with profanity, my respect for my elders ended there. I let out a quiet laugh as I looked at Choi Byungil.

“You still don’t know? You must have dug up every scrap of information about me. If you went so far as to attach Familiars, that says everything.”

“…”

“I could’ve let it go if I’d been alone at home. But the thought of my family being watched pissed me off. So I threw out some bait, and you snapped it up.”

The six watchers trembled.

“Th-then what about the USB?”

“Oh, that? It’s my collection of porn I’ve spent my whole life putting together.”

It was a treasure of humanity that I had carefully stored in my Inventory.

“No way! I definitely had a feeling!”

“Well, there are plenty of works in there that defy belief. And any man would get a gut feeling about it.”

I looked at them, standing there with faces full of despair.

“You answered honestly, so let me ask you one thing, too.”

One by one, they flinched whenever their eyes met mine.

At last, my gaze stopped on a painfully thin man in his twenties. He was probably the Familiar mage.

> **System**
>
> Level 41 Kim Junsu

“Junsu. You were sent here by Sangdong Guild, weren’t you?”

“Shut your mouth!”

Choi Byungil shouted, but Kim Junsu had already answered.

His face had gone completely pale. That was answer enough.

“Okay, Sangdong Guild. I figured as much.”

Choi Byungil’s face stiffened at my words.

“You shouldn’t have said that name out loud.”

“What, you’re going to kill me?”

“…I’ll capture you first and think about it.”

“That’ll be pretty hard.”

Choi Byungil’s Level was in the mid-sixties. His aura was comparable to Im Changsoo’s, while the others were ordinary C-ranks around Levels 30 or 40.

The odds of a group that wasn’t even a professional raid team managing to capture me were extremely low.

“Come at me prepared to die. That’s the only way you’ll manage to tie even a butterfly knot around my wrist.”

“Get him!”

At Choi Byungil’s shout, the Sangdong Guild watchers began charging at me from all directions.

Whoosh!

A dagger dropping toward my shoulder was the opening move.

I reached toward the trajectory that looked slow to me.

At the same time…

*Inventory open. Equip.*

Crunch!

A blade brimming with internal energy shattered the enemy’s dagger. Broken metal and someone’s blood spilled across the nameless weeds.

“Come on, you stalker bastards!”

Ssshhhhh!

[^1]: *Pyeong* is a traditional Korean unit of floor area; five pyeong is roughly 16.5 square meters.

[^2]: *Yeokmasal* is a traditional Korean notion of a fate that compels someone to wander. Here it also puns on *sal*, the Korean word used when asking someone’s age.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 99`.

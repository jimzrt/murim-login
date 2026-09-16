# Master Edit Task — Chapter 98

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
| 진하연    | **Jin Hayeon**    |
| 홍우진    | **Hong Woojin**   |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 귀가      | **your family**                                                 |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

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

#### Chapter 96 tail (verified mastered)

…
he moved away with a loose, swinging gait. *He’s a good actor.* “Meow.” Right. You’re here, too. The moment I left the house, I met two actors. Actors wearing the guises of a stray cat and a neighbor. “I’ll be back soon, so wait here quietly, okay?” The cat tilted its head as if it had no idea what I was talking about. But I knew. It had understood me, and it would still be sitting here even if several hours passed. And there was one more thing. > **System** > > Lv. 42 Kim Gwondong There weren’t any Hunters living in the building next to ours. *Just as I thought. They aren’t working together.* The appearance of the two actors was enough to turn my guess into certainty. My steps grew even lighter as I headed toward the real-estate office in front of the house. * * * Late that morning, a middle-aged man in shabby clothes dragged his slippers along while humming to himself. He looked like someone you could see anywhere. The moment he rounded the corner, he pulled out a cigarette and stuck it between his lips. “Let’s see. Where’s my lighter…” His hand rummaged slowly through his pocket, but his eyes darted around. Once he had confirmed that no one was nearby, he pulled out something other than a lighter: a miniature radio. “How was my acting? Maybe I should’ve become an actor instead of a Hunter. Seems like I’m better at acting than fighting.” —It’s me, the Team Leader. Plop. The cigarette fell from his mouth. His now-free lips moved soundlessly. *Fuck. I’m screwed.* Kim Gwondong, a C-rank Hunter in the Security Team, hurriedly collected himself and answered. “Ah, yes, Team Leader.” —Kim Gwondong’s pretty good at acting, huh? You could quit the Guild and go to Hollywood. “I-I’m sorry.” —Don’t get scared. That was a compliment. Anyway, how’s the target? He didn’t catch on, did he? “I don’t think so.” The Team Leader had already heard the conversation through Kim Junsu, but there was a simple reason he was asking again. A cat’s eyes could not capture everything about the target clearly. —Are you sure? One hundred percent? “Ninety percent.” —You little shit, is ninety percent certain? At times like this, you’re supposed to say it confidently and go for it. “It’s dangerous to jump to conclusions.” Kim Gwondong cursed the Team Leader inwardly. *What good would that do? If something goes wrong later, you’ll be the first one to rip me a new asshole.* He had to leave himself an escape route. Kim Gwondong’s ninety percent would only be complete once the Team Leader supplied the remaining ten. —That’s exactly the attitude I like to see. You know what to do next, right? The pleasure in the Team Leader’s voice signaled that they had finally reached one hundred percent. Kim Gwondong subtly changed direction to avoid a resident approaching in the distance. “Yes. I’ll circle the area naturally and keep watch.” —Right. Report immediately if anything unusual happens. “Yes.” —Keep up the good work, then. No one overheard the conversation, which lasted just over a minute. This time, Kim Gwondong took out a real lighter and lit his cigarette. He inhaled deeply. “Fuck. Lung cancer’s going to kill me before a monster does.” * * * The Security Team Leader got busy. There were three external surveillance personnel in total. He had to give instructions to the other two and make sure every precaution was taken. “Number One.” —Number One here. “You were listening on the all-team channel, right? What’s the situation with the real-estate office the target is heading to?” —There are two in the nearby shopping district. We’ve installed magical eavesdropping Equipment in both. “Good. Where’s the target?” —We haven’t seen him yet… Ah, there he is. He’s approaching from about 300 meters away. “Leave your position. We already installed the Equipment, so there’s no need to make contact for no reason.” —Yes. I’ll report immediately if anything unusual happens. “Okay. Number Two?” —Standing by at my current position. A deep voice came over the radio. The Security Team Leader nodded at the reply from another team member concealed in a nearby shop. “That bastard might veer off and take another route, so keep a close eye on him.” —Yes. Four C-rank Hunters specializing in stealth and tracking, plus a Familiar mage. They lacked combat power, but every one of them was a veteran with extensive experience in this field. *It’s overkill for one C-rank Hunter.* At first, he had been somewhat wary. The Guild Master had given them a special warning about the target. *They said he cleared a B-rank Gate alone, I think.* But the more information he gathered about the man, the more he watched him, the more he felt that was not the case at all. The fact that the information had come from Im Changsoo finally put an end to his doubts. *That good-for-nothing bastard made it all up because he didn’t want to get beaten to death.* An ordinary C-rank Hunter you could find anywhere. In his eyes, that was all Jin Taekyung was. Beep. —Target entering the real-estate office. A report came over the radio from the team member keeping watch. Sangdong Guild’s Security Team went on full alert. [^1]: A Korean term for a cat that acts like a dog—friendly and affectionate.

#### Chapter 97 tail (verified mastered)

…
in the last few moments. “What do we do about the transcript and the statements?” “What do you think? If you don’t want to watch the Team Leader throw a fit, you have to write them. Want to go to the hospital and get a medical statement?” “…” “Just slap something together. I’ll cover for you and say you couldn’t write yours because you were using Familiar magic.” After heaving deep sighs, the two men began cursing the Team Leader in earnest. All the while, the conversation continued through the transmitter. —It’s nice. It faces south, so it gets plenty of sunlight. What about the building next to it? Don’t tell me that one’s gone, too? —Huh? No, it’s still available. Business has been slow lately, so the places that went recently were… Wait, young man. —Yes? —Your arm is really firm. Goodness, just look at those muscles and veins. —… * * * “Young man, come again! Come twice!” I left the real-estate office with the ajumma’s regretful farewell behind me. Goose bumps had risen all over the arm her hand had just brushed. *Whether it’s an ajumma or an ajusshi, people who grow old without growing up are all alike when it comes to hitting on younger people.* I left as if fleeing her sticky gaze, but I had already accomplished what I’d gone there to do, so I had no regrets about leaving. *Confirm the listings that were recently sold or leased.* Today was exactly five days after the raid with Im Changsoo. In other words, the surveillance team couldn’t have been assigned to me more than five days ago. *I tried to act and ask about it indirectly without making it obvious, but…* Knowing that eavesdropping magic was in place, every word and action had been deliberate. I wanted to come across as an unremarkable C-rank Hunter packed full of arrogance and extravagance. *Whether they fell for it or not was another matter.* My conversation with the real-estate ajumma had given me an important clue. I silently muttered the addresses I had memorized in advance. *Building 5, Unit 901. Building 4, Unit 302. Building 3, Unit 202.* These were the three listings that had changed hands in the past five days. I had used our house as the center point and set the range at a maximum of five hundred meters—the distance Familiar magic could reach. The watchers were definitely somewhere within that range. *The problem is how to find them.* My goal wasn’t to drive them away. I wanted to catch them, beat the hell out of them, and find out who was behind them. If I went after the wrong place too soon, they might catch on and run. *They could be hiding in a car, so I should check the parking lot too.* Searching the nearby homes would tip them off, but I could search the parking lot without looking suspicious. All I had to do was pretend to take a walk while sweeping the area with Qi Sense. Game over. > **System** > > **Lv. 42 Kim Gwondong** “Oh, we meet again.” Just like this guy. I greeted Kim Gwondong when he called out to me. “Indeed. We meet again.” “You said you were going to the real-estate office. Finished already?” “I just asked a few questions. But when I actually went there and looked into it, the house prices weren’t exactly cheap. I ran right back out.” “That’s this neighborhood for you. Still, you’re doing well for yourself, young man. At your age, all I did was sit at home and eat my parents’ food.” “Doing well? Ha-ha.” If he knew what real ability looked like, he’d faint. Kim Gwondong laughed along, unaware of my thoughts, then spoke. “Well, I should get going. I need to walk to the park over there and back.” “You must like taking walks.” “Huh? It’s not that I do it because I like it. I do it because I need to. You’ll have a hard time too once you reach my age.” He conspicuously waved his thin arms and legs. To all appearances, he was just a scrawny, potbellied middle-aged man. *He certainly looks like a civilian.* Anyone else would have fallen for it completely. But there was no such thing as a Level 42 civilian. *Probably a C-rank Hunter. Judging by his build, he likely specializes in stealth and pursuit.* Once you knew someone was a Hunter, there was plenty you could infer. I said goodbye to Kim Gwondong. “Then I’ll see you next time.” “Maybe you will, maybe you won’t. Ha-ha.” Well, I definitely wanted to see him. Of course, when that happened, I wouldn’t be parting from him with a smile and a laugh like I was now. I wanted to knock him flat right then and there, but it wasn’t time yet. I gave him a slight bow and turned to leave when his voice came from behind me. “Oh, right. That cat seemed awfully smart. I saw it on my way over, and it was still there.” He had even given me a friendly reminder not to forget to pick up my Familiar. And just as he said, the cat was waiting for me in the same spot as before. “Meow.” Right. Hyung’s here, you punk. [^1]: Yulmu tea is a sweet Korean grain beverage made from roasted Job’s tears.

## Korean source

```text
＃98화



홍우진은 후회했다.

‘내 생각이 짧았구나.’

침입은 성공적이었다. 고양이 덕후인 표적의 여동생에게 접근, 애처로우면서도 반짝이는 눈망울로 마음을 사로잡았으니까. 다만 문제는…….

“우리 여름이는 뭘 먹고 이렇게 귀여워요? 응? 응응?”

미야옹.

“여름아, 왜 자꾸 문밖으로 나가려고 해. 여기서 언니랑 놀자.”

야옹.

“꺅, 너무 귀여워!”

하악! 하아아악!

“헉, 여름이 화났어? 미안해. 언니가 너무 만졌지? 알았어, 가만히 있을 테니까 침대 위에서 놀고 있어. 응?”

이 망할 여동생이라는 녀석이 도무지 밖으로 내보내 줄 생각을 안 한다는 거다. 덕분에 하루 반나절 이상을 진하연의 방에 갇혀 지내는 신세가 됐다.

‘차라리 개로 할걸.’

개였다면 지금처럼 쉽게 들어올 수는 없었겠지만 들어온 이후에 반 감금되어 있지는 않았을 것이다. 적어도 산책 정도는 시켜 줬을 테니까.

‘이대로는 죽도 밥도 안 된다.’

위기감에 휩싸인 홍우진은 탈출을 시도했다.

‘네가 이기나, 내가 이기나 보자!’

그렇게 독한 마음으로 시작했는데…….

벅, 벅벅벅벅.

“…….”

야옹. 야오오오옹.

“…….”

첫 번째 시도는 실패다. 괜히 방문도 박박 긁어 보고, 큰 소리로도 울어도 봤지만 진하연은 책상에 앉아 단 한 번도 반응하지 않았다.

이어폰도 끼지 않은 채 그저 매서운 눈빛과 손놀림으로 문제집을 풀어 가고 있을 뿐.

‘전국 상위 0.01%라더니.’

1차 조사 자료에서 봤다. 중학교 때부터 전교 1, 2등은 예사고 각종 경시 대회에서 입상한 경력이 수두룩했으니 잊기도 힘든 내역이다.

홍우진은 오늘에서야 그 이유를 알았다. 책상 앞에 앉은 그녀는 정말이지, 어마 무시한 집중력의 소유자였다.

‘이런 애가 마법사 하면 딱인데……가 아니고.’

그는 그 후로도 어떻게든 공부를 방해하려고 애썼다. 쉴 새 없이 발을 건드리고 애교를 부려 댔다.

하지만 진하연의 대응은 간단했다.

“언니 지금 공부 중이야. 방해하면 안 돼.”

의자에 발을 올려 책상다리로 앉아 버리고 나니 이 조그마한 몸으로는 결코 닿을 수 없게 되었다. 아기 고양이의 한계였다.

‘이번 작전은 실패다.’

공부 방해 작전이 실패로 돌아갔으니 별수 없이 최후의 카드를 꺼내야 한다. 인간의 존엄성에 큰 손상을 입겠지만 지금은 이것저것 가릴 때가 아니었다.

‘이것도 무시하나 보자.’

쉬이이이이.

새하얀 이불보가 노랗게 물든다. 본래 큰일과 작은 일은 한 번에 해결해야 하는 법. 두 가지 일을 동시에 끝마친 홍우진은 굳게 결심했다.

‘그래, 기왕 이렇게 된 거 확실하게 처리하자. 프로답게.’

데굴데굴.

패밀리어 마법을 시작한 지 5년. 이렇게까지 망가진 적은 이번이 처음이었다. 그는 끊임없이 자기 세뇌를 걸었다.

‘나는 프로다, 나는 프로다, 나는 프로다…….’

잠시 후, 뭔가 이상한 냄새를 맡은 진하연이 고개를 돌렸을 때는 모든 게 끝난 후였다.

미야옹.

대소변으로 물든 이불, 마찬가지로 오물로 범벅이 된 아기 고양이 한 마리.

“꺅, 여름아!”

깜짝 놀란 진하연이 신속하게 움직였다. 더러워진 이불을 걷고, 조심스럽게 고양이의 뒷덜미를 잡아 들어 올렸다.

“화장실 두고 여기서 싸면 어떡해. 우리 여름이 씻어야겠다.”

‘그래, 문으로 가라! 문!’

고대하던 순간이다. 비록 오물로 범벅이 된 채 스무 살도 안 된 여자애의 손에 대롱대롱 매달려 있지만 홍우진은 희열에 가득 찼다.

달칵.

열린다, 문이!

어제 이후로 보지 못했던 거실이 보인다!

미야옹! 미야오옹!

“이상하네. 얘가 왜 이렇게 좋아하는 것 같지?”

진하연이 갸우뚱하던 그때였다.

비밀번호를 입력하는 익숙한 기계음과 함께 현관문이 열렸다.

“다녀왔습니…… 뭐냐, 그건?”

“어디 다녀왔…… 그건 뭐야?”

남매는 서로를 황당한 시선으로 바라봤다. 정확히 말하면 각자의 손에 들린 생물체를.

야옹.

미야옹.

황당한 시선을 교환하는 것은 이쪽도 마찬가지였다.

‘저게 홍우진?’

‘저놈은 상동 길드의 아마추어?’

그리고 이어지는 생각.

‘쟤는 왜 온몸에 똥칠을 하고 있어?’

‘아, 시바.’

홍우진이 갖고 있던 마지막 인간의 존엄성이 와르르 무너지는 순간이었다.



* * *



“이불에다가 똥칠을 해 놨다고?”

“어. 잠깐 공부하는 사이에 실수했나 봐.”

실수는 개뿔, 다분히 의도적이다.

하연이가 방에만 두고 물고 빠니까 어떻게든 나오려고 머리 굴린 거지, 뭐.

미야옹…….

고양이, 아니 이제 두 마리니까 이름을 불러 줘야겠구나.

어쨌건 여름이의 힘없는 울음소리에 하연이가 걱정스러운 얼굴로 물었다.

“애가 아까부터 힘이 없어.”

“음, 그럴 수 있지.”

모르긴 몰라도 자괴감이 장난 아닐 거다.

몸에 똥칠한 채로 업계 동업자와 감시 표적을 동시에 맞닥트렸으니까.

“너무 걱정하지 마. 원래 고양이들은 몸에 물 닿는 거 싫어하잖아.”

“그래서 그런 건가? 아냐, 아까 씻길 땐 반항도 안 하고 얌전하던데.”

“아, 그래?”

“기분 탓인지는 모르겠는데…… 애가 좀 넋이 나간 느낌이야. 자기도 사고 친 걸 알아서 미안해하는 건가?”

우리 여름이, 현자 타임이 제대로 왔구나.

나는 웃음을 삼키며 말했다.

“그거야 모르지. 아무튼 너 이불 어쩌냐? 시트도 새로 갈아야 되겠네.”

“괜찮아. 사람이 한 것도 아니고 동물인데, 뭘.”

별생각 없이 던진 돌에 개구리가 맞아 죽는다더니.

지금이 딱 그 상황이다. 하연이의 한마디는 비수로 변해 누군가의 가슴에 꽂혔다.

움찔.

울음소리도 못 내고 작은 몸을 부르르 떠는 아기 고양이 한 마리. 반면 다른 한쪽은 신이 났다.

그릉, 그르릉.

기분 좋은 소리를 내며 내 다리에 연신 얼굴을 비벼 대는 검은 고양이를 하연이가 귀여워 죽겠다는 얼굴로 바라봤다.

“얘는 어디서 데려왔어?”

“아파트 단지 입구에서.”

“길고양이야?”

“그렇겠지. 혼자 있었으니까.”

“뭐? 그럼 엄마가 있을지도 모르잖아. 그래서 새끼 고양이는 하루 정도는 지켜보고 데려와야 해.”

“어떤 아저씨한테 들었는데, 어제부터 혼자 울고 있었다는데?”

“아, 그럼 엄마 없네.”

움찔!

골골거리던 애교가 딱 멎는다. 자신도 모르는 사이에 2킬을 달성한 하연이가 해맑게 웃었다.

“우쭈쭈. 너도 엄마가 없구나. 괜찮아, 오늘부터 언니가 엄마 해 줄게.”

“…….”

내 동생이지만 웃는 얼굴로 엿 먹이는 재주가 제법인데.

검은 고양이는 직업 정신과 패드립 사이에서 갈등하는 듯했지만 이내 현실을 받아들였다.

야옹.

어머니의 원수에게 애교를 부리는 모습이 처량하기까지 하다. 저런 게 바로 직장인의 애환이지.

지켜보고 있자니 문득 엄마에게 생각이 미쳤다.

“엄마는?”

“몰라, 중요한 약속 있다고 나가셨어.”

“약속?”

“응, 요즘 자주 나가셔.”

무슨 일이지?

근래 들어 엄마의 외출이 잦아졌다. 일을 관둔 후 어느 정도 여유가 생기니 스스로의 삶을 찾으시는 걸까?

‘그러고 보니 분위기가 이상하긴 했지.’

뭔가 할 말이 있는 듯한 얼굴로 앉아 계신다거나, 갑자기 말을 걸면 화들짝 놀란다거나. 확실히 엄마의 주변에 어떤 변화가 일어나고 있는 것은 분명해 보인다.

‘때가 되면 말씀해 주시겠지.’

내가 세상에서 가장 사랑하고 믿는 분이 바로 우리 엄마다. 언제나 그렇듯이 믿고 기다리는 수밖에.

물론 적절한 시기에 함께 대화를 나누고 이야기를 들어 드리는 것도 자식의 도리다.

“무슨 생각을 그렇게 해?”

“별것 아냐. 그나저나 너는 어디 안 나가냐?”

“뭐야, 꼭 어디 나가기를 바라는 말투네.”

“꼭 그런 건 아니고.”

“흠, 수상해. 여자 친구 데려오려는 건 아니지?”

“…….”

제발 데려올 여자 친구라도 있었으면 좋겠다.

생각이 고스란히 드러나는 내 표정에 하연이가 주춤했다.

“아, 미안.”

“……사과하지 마. 두 배로 비참해져.”

“진짜 미안해.”

“너 일부러 이러는 거지?”

“생각해 보니까 도서관에 책 반납해야 할 게 있네.”

방 안으로 뛰어가더니 가방을 들쳐 메고 나오는 속도가 광속이다. 쾅 소리와 함께 현관문이 닫히자 집 안이 조용해졌다.

‘솔로의 마음을 후벼 놓다니.’

가슴 한구석이 휑해졌지만 내가 원하던 무대가 드디어 만들어졌다.

가급적이면 가족이 없을 때 해결해야 될 문제니까.

미야옹.

야옹.

각기 검고 흰 두 마리의 고양이가 슬금슬금 다가와 주위를 맴돌기 시작했다. 초롱초롱한 눈망울, 쫑긋 선 귀.

나에 대한 정보를 건지고 싶어 안달이 난 패밀리어들을 뒤로하고 베란다로 나갔다.

가장 먼저 보이는 건 수백 대의 차량이 늘어선 주차장이다.

‘주차장은 클리어.’

귀가하기 전, 패밀리어를 품에 안고 아파트 단지를 한 바퀴 돌아 보았다. 남들 눈에는 날씨 좋은 날 산책하는 한량으로 보였겠지만 목적은 차량 확인이었다.

결과는 이상 무.

‘그럼 역시 집밖에 없지.’

이로써 감시자들이 최근 거래된 아파트를 아지트로 삼았음이 확인됐다. 나는 부동산에서 얻은 정보를 다시 한번 떠올렸다.

‘5동 901호. 4동 302호. 3동 202호.’

공교롭게도 세 곳 전부 우리 아파트를 중심으로 감싸는 형태로 자리해 있다. 창문으로도 동 입구를 내려다볼 수 있어 감시에 용이한 위치.

감시자들이 어느 곳에 있어도 이상하지 않다.

‘문제는 저 중 어디에 숨었냐는 건데…….’

발각을 우려해 마법 장비가 아닌 패밀리어를 붙일 정도로 조심성을 갖춘 놈들이다.

섣부르게 다가갔다가는 놓친다. 확실한 검거를 위해서는 그만큼 큼지막한 미끼를 던지는 수밖에 없다.

‘슬슬 시작해 볼까.’

촥, 촤르륵.

우선 집 안의 모든 커튼을 쳤다. 한낮임에도 불구하고 어둑해진 거실 중앙에서 주머니를 뒤적였다.

‘인벤토리 오픈. 마나 탐지 장비.’

동시에 손바닥의 절반만 한 쇳덩이가 손에 잡혔다.

이름 그대로 마나를 탐지할 수 있는 장비, 스토어에서 2천만 원이나 주고 산 물건이다.

‘다음 단계, 수색.’

탐지 장비를 들고 집 안을 꼼꼼히 훑었다. 내부에 아무런 마나가 감지되지 않는 걸 확인하고 스마트폰을 꺼내어 누군가에게 통화를 걸었다.

뚜, 뚜. 달칵.

통화 연결음과 함께 상대방이 전화를 받았다.

- 여보세요?

내가 대답했다.

“접니다, 진태경.”

그런 내 모습을 두 마리의 패밀리어가 숨도 쉬지 않고 지켜보고 있었다.



* * *



김준수는 눈을 뜸과 동시에 외쳤다.

“왔어요, 왔어!”

옹기종기 모여 앉아 소견서를 쓰고 있던 보안팀원들이 화들짝 놀랐다.

“뭐?”

“누가 와? 우리 팀장?”

“아니면 설마…….”

말꼬리를 흐린 팀원을 향해 김준수가 고개를 끄덕였다.

“표적이요. 이 자식 이거 구린내 장난 아닙니다.”

“진짜로?”

“네. 집 비자마자 커튼 칠 때부터 뭔가 쎄 했는데, 탐지 장비까지 사용해서 집 안 점검하더라고요.”

평범한 C급 헌터, 그것도 휴가 중인 놈이 할 만한 일이 아니다. 방 안의 모두가 침을 꿀꺽 삼켰다.

“그, 그래서?”

“폰 꺼내더니 전화부터 걸던데요.”

“전화? 누구한테?”

“그걸 모르겠어요.”

김준수가 미간을 찡그렸다.

“통화가 3분도 안 될 만큼 짧았던 것도 있지만, 호칭에 굉장히 주의한다는 게 느껴질 정도?”

“그 정도면 충분해. 일단 윗선에 보고해서 저놈 통화 기록 털어 보면 되니까.”

“그래, 더 나온 건 없고?”

“왜 없겠습니까. 그놈이 뭐라고 한 줄 아세요?”

크흠. 한차례 목을 가다듬은 그의 입에서 낮은 목소리가 흘러나왔다.

“계획은 차질 없이 진행 중입니다. 네, 네. 상동 길드 쪽에서는 아직 눈치 못 챘습니다. 물건은 잘 갖고 있습니다.”

듣고 있던 팀원들이 무릎을 탁 쳤다.

“이거네!”

“드디어 하나 건졌다.”

“와, 방금 살짝 소름 돋았어. 이거 무슨 비밀 요원이야?”

그때, 가만히 듣고 있던 김권동이 불쑥 입을 열었다.

“진수야, 방금 그 자식이 무슨 물건 갖고 있다고 하지 않았냐?”

“좋은 지적입니다.”

김진수가 의미심장하게 웃었다.

“그놈, USB를 갖고 있어요.”
```

## Current accepted English baseline

```markdown
# Chapter 98

Hong Woojin regretted it.

*I didn't think this through.*

The intrusion itself had gone perfectly. He had approached the target’s cat-loving younger sister and won her heart with a pair of pitiful yet sparkling eyes.

The problem was…

“What does our Yeoreum eat to be this cute? Hmm? Hmm-hmm?”

*Meow.*

“Yeoreum, why do you keep trying to get out the door? Stay here and play with your big sis.”

*Meow.*

“Eek, you’re so cute!”

*Hiss! Hissssss!*

“Oh no, is Yeoreum mad? I’m sorry. Did Sis touch you too much? Okay, I’ll stay still, so play on the bed, all right?”

This damn younger sister had absolutely no intention of letting him outside. Thanks to her, he had spent more than a day and a half trapped in Jin Hayeon’s room.

*I should’ve gone with a dog.*

If he had been a dog, getting inside wouldn’t have been this easy. But once he was in, he wouldn’t have been practically held captive, either. At the very least, they would have taken him out for walks.

*This gets me nowhere.*

Swept up by a sense of crisis, Hong Woojin attempted to escape.

*Let’s see who wins—you or me!*

He had begun with that fierce resolve, but then…

Scritch, scritch-scritch-scritch.

“…”

*Meow. Myaaaaaow.*

“…”

His first attempt was a failure. He scratched desperately at the door and even tried crying as loudly as he could, but Jin Hayeon didn’t react even once.

Without even putting on earphones, she simply continued solving problems with a fierce look in her eyes and swift movements of her hands.

*So this is what it means to be in the top 0.01 percent nationwide.*

He had seen it in the initial investigation report. Ever since middle school, she had routinely ranked first or second in her entire school and had earned countless awards in various academic competitions. It was hard to forget a record like that.

Only today did Hong Woojin understand why.

Sitting in front of her desk, she possessed truly terrifying powers of concentration.

*Someone like this would make the perfect mage… No, that’s not the point.*

He continued trying to disrupt her studies somehow. He pawed at her feet without pause and kept acting cute.

But Jin Hayeon’s response was simple.

“Big sis is studying right now. Don’t bother me.”

She pulled her feet up onto the chair and sat cross-legged, putting them completely out of reach of his tiny body.

That was the limit of being a kitten.

*This operation has failed.*

Since his plan to disrupt her studies had gone up in smoke, he had no choice but to bring out his final card. It would deal a serious blow to his human dignity, but this was no time to be picky.

*Let’s see if you ignore this, too.*

Sssssssss.

The pristine white duvet turned yellow.

When nature called, it was best to take care of both kinds of business at once. Having finished both simultaneously, Hong Woojin made a solemn decision.

*Fine. Since things have come to this, I might as well take care of it properly. Like a professional.*

He rolled over and over.

It had been five years since he started using Familiar magic. This was the first time he had ever fallen this far.

He kept hypnotizing himself.

*I’m a professional. I’m a professional. I’m a professional…*

A little while later, Jin Hayeon noticed a strange smell and turned around.

By then, everything was over.

*Meow.*

A duvet stained with urine and feces, and a kitten covered in filth.

“Eek, Yeoreum!”

Jin Hayeon was startled and moved quickly. She pulled off the dirty duvet, then carefully grabbed the kitten by the scruff of its neck and lifted it up.

“What are you doing going to the bathroom here when your litter box is right there? We need to wash our Yeoreum.”

*Yes, go to the door! The door!*

This was the moment he had been waiting for.

Even though he was covered in filth and dangling from the hand of a girl who wasn’t even twenty, Hong Woojin was filled with joy.

Click.

The door was opening!

The living room he hadn’t seen since yesterday came into view!

*Meow! Myaaaow!*

“That’s strange. Why does it look so happy?”

Jin Hayeon tilted her head.

That was when the front door opened with the familiar electronic tones of someone entering the passcode.

“I’m ho—… What is that?”

“Where have you been—… What’s that?”

The siblings stared at each other in bewilderment.

More precisely, they stared at the creatures in each other’s hands.

*Meow.*

*Myaow.*

The two cats exchanged equally bewildered looks.

*That’s Hong Woojin?*

*That guy is the Sangdong Guild’s amateur?*

And then came the next thought.

*Why is he covered in shit from head to toe?*

*Ah, fuck.*

It was the moment the last shred of Hong Woojin’s human dignity collapsed.

* * *

“You smeared poop all over the duvet?”

“Yeah. I guess he had an accident while I was studying for a bit.”

*An accident, my ass.*

Since Hayeon had kept him in her room, petting and cuddling him nonstop, he had wracked his brain for a way to get out.

*Myaow…*

A cat.

No, there were two of them now, so I supposed I should call them by their names.

Whatever the case, Hayeon asked worriedly at the sound of Yeoreum’s feeble cry.

“He’s been looking weak for a while.”

“Hmm. That can happen.”

I couldn’t say for sure, but his self-loathing had to be something else.

He had run into both a fellow professional and his surveillance target while covered in shit.

“Don’t worry too much. Cats normally hate getting water on their bodies.”

“Is that why? No, he didn’t even resist when I washed him earlier. He was completely docile.”

“Oh, really?”

“I don’t know if it’s just my imagination, but he seems kind of out of it. Maybe he knows he made a mess and feels sorry?”

*Our Yeoreum had a serious case of post-nut clarity.*

I swallowed my laughter and said, “Who knows? Anyway, what are you going to do about the duvet? You’ll have to change the sheets, too.”

“It’s fine. It was an animal, not a person. What’s the big deal?”

They say a frog can die from a stone thrown without a second thought.

That was exactly what had happened here. Hayeon’s offhand remark turned into a blade and lodged itself in someone’s chest.

The kitten trembled violently in silence, unable to even cry out.

Meanwhile, the other one was having a wonderful time.

*Purr. Prrrr.*

Hayeon gazed at the black cat with a face full of adoration as it repeatedly rubbed its face against my leg, making happy noises.

“Where did you bring him from?”

“The entrance to the apartment complex.”

“Is he a stray?”

“I guess so. He was alone.”

“What? Then he might have a mother. You’re supposed to watch a kitten for about a day before bringing it home.”

“Some man told me he’d been crying alone since yesterday.”

“Oh, then he doesn’t have a mother.”

The black cat flinched.

Its purring and attempts to act cute stopped dead. Without realizing it, Hayeon had scored two kills, and she smiled brightly.

“There, there. You don’t have a mother, either. It’s okay. From today onward, Sis will be your mommy.”

“…”

For my little sister, she certainly had a talent for screwing people over with a smile.

The black cat seemed torn between professional duty and the cheap shot at his mom, but soon accepted reality.

*Meow.*

The sight of it acting cute for its mother’s enemy was downright pitiful.

*That’s the hardship of being a working stiff.*

Watching them, I suddenly thought of Mom.

“Where’s Mom?”

“I don’t know. She went out because she had an important appointment.”

“An appointment?”

“Yeah. She’s been going out a lot lately.”

*What’s going on?*

Mom had been leaving the house frequently these days. Now that she had some free time after quitting her job, was she finally looking for a life of her own?

*Come to think of it, she had been acting strange.*

Sometimes she would sit there with an expression that looked as though she had something to say. Other times, she would jump whenever I suddenly spoke to her.

Something had definitely changed around Mom.

*She’ll tell me when the time is right.*

The person I loved and trusted most in this world was my mother. Just as always, all I could do was trust her and wait.

Of course, listening to her and talking things over at the right time was also a child’s duty.

“What are you thinking about so hard?”

“It’s nothing. By the way, aren’t you going out?”

“What, you sound like you want me to leave.”

“Not exactly.”

“Hmm. Suspicious. You’re not planning to bring a girlfriend over, are you?”

“…”

*I wish I had a girlfriend to bring over.*

My expression must have revealed my thoughts, because Hayeon hesitated.

“Ah, I’m sorry.”

“Don’t apologize. It makes me twice as pathetic.”

“I’m really sorry.”

“You’re doing this on purpose, aren’t you?”

“Come to think of it, I have some books to return to the library.”

She sprinted into her room, threw on her backpack, and came back out at the speed of light.

The front door slammed shut, and the house fell silent.

*She really went and gouged out a single man’s heart.*

A corner of my chest felt hollow, but the stage I had been waiting for had finally been set.

This was a problem I needed to deal with while my family was out of the house, if possible.

*Myaow.*

*Meow.*

Two cats, one black and one white, began creeping toward me and circling around.

Bright eyes. Perked-up ears.

I left the Familiars, who were dying to learn more about me, behind and stepped onto the balcony.

The first thing I saw was the parking lot, where hundreds of cars were lined up.

*The parking lot is clear.*

Before returning home, I had carried the Familiar in my arms and taken a lap around the apartment complex. To everyone else, I probably looked like an idler out for a walk on a pleasant day.

My real purpose had been to check the vehicles.

The result was nothing suspicious.

*Then it has to be one of those houses.*

That confirmed the watchers had made one of the recently traded apartments their base. I recalled the information I had obtained from the real-estate office once more.

*Building 5, Unit 901. Building 4, Unit 302. Building 3, Unit 202.*

Coincidentally, all three were positioned around our apartment, forming a sort of ring. They were ideal for surveillance, since their windows offered a view of the entrances to the buildings.

It wouldn’t be strange for the watchers to be in any one of them.

*The question is which one they’re hiding in…*

They were cautious enough to use a Familiar instead of magical Equipment to avoid being discovered.

If I approached recklessly, I would lose them. To make a definite capture, I had no choice but to throw out equally substantial bait.

*I think it’s time to begin.*

Swish. Rustle.

First, I drew all the curtains in the house. Even though it was the middle of the day, the living room had grown dim. I reached into my pocket.

*Inventory open. Mana-detection Equipment.*

At the same time, my hand closed around a lump of metal about half the size of my palm.

As its name suggested, it was Equipment that could detect mana. I had paid twenty million won for it at the Store.

*Next step: search.*

I carefully swept through the house with the detection Equipment. After confirming that no mana was being detected inside, I took out my smartphone and called someone.

Beep. Beep. Click.

The other person answered as the call connected.

—Hello?

I replied.

“It’s me, Jin Taekyung.”

The two Familiars watched me without even seeming to breathe.

* * *

The moment Kim Junsu opened his eyes, he shouted.

“He’s here! He’s here!”

The Security Team members, who had been sitting close together and writing their assessments, jumped in surprise.

“What?”

“Who’s here? Our Team Leader?”

“Or could it be…”

Kim Junsu nodded at the team member who had let his voice trail off.

“The target. This guy reeks to high heaven.”

“Seriously?”

“Yes. I got a bad feeling when he drew all the curtains as soon as the house was empty, and then he even used detection Equipment to inspect the inside.”

That wasn’t something an ordinary C-rank Hunter, especially one on vacation, would do.

Everyone in the room swallowed hard.

“Th-then?”

“He pulled out his phone and made a call.”

“A call? To whom?”

“I don’t know.”

Kim Junsu furrowed his brow.

“The call was so short that it didn’t even last three minutes. But more than that, I could tell he was being extremely careful about how he addressed the other person.”

“That’s enough. We’ll report it up the chain and pull that bastard’s call records.”

“Right. And there was nothing else?”

“How could there be nothing else? Do you know what he said?”

He cleared his throat once. Then a low voice came from his mouth.

“‘The plan is proceeding without a hitch. Yes, yes. The Sangdong Guild hasn’t noticed anything yet. I have the item with me.’”

The team members listening slapped their knees.

“This is it!”

“We finally got something!”

“Wow, I just got chills. What is he, some kind of secret agent?”

At that moment, Kim Gwondong, who had been listening quietly, suddenly spoke.

“Junsu, didn’t that bastard say he had an item?”

“Good observation.”

Kim Junsu smiled meaningfully.

“That guy has a USB.”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 98`.

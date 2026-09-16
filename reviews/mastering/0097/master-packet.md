# Master Edit Task — Chapter 97

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
| 임창수    | **Im Changsoo**   |
| 홍우진    | **Hong Woojin**   |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 꼰대 | **boomer** | Modern slang for a hidebound older person; used by Cheongpung. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |
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

#### Chapter 95 tail (verified mastered)

…
over 300 million won. In every respect, this was a losing proposition. I was watching TV with my face twisted into a scowl when Hayeon cautiously studied my expression and spoke. “Oppa, are you mad?” “No. What would I be mad about?” “I’m sorry.” “…What’s gotten into you? You’re starting to scare me.” I wasn’t joking. I was more startled than when I had first discovered the Familiar. Since when could she say something like that? I asked seriously. “Are you sick?” “No, it’s just…” “Then are you hungry?” “That’s not it…” Just as Hayeon hesitated, about to say something, a stomach growled from somewhere. It wasn’t mine. Mom had stepped out to run an errand. “You’re hungry.” “Mm, a little?” “Right. You’re so hungry you’re starting to spout nonsense. You know where my wallet is, right? Order anything you want to eat.” “Really?” “Yeah. Up to a hundred thousand won.” “Wow, now that you’re making money, you’ve gotten generous. Our Oppa.” I never thought I’d live to hear her call me “our Oppa.” It was the first time I’d heard it since Hayeon had been in middle school, and it gave me goose bumps. “You’re the Familiar, you little bastard!” “What are you talking about? Anyway, I can order whatever I want as long as it’s under a hundred thousand won?” “Yeah. No, wait. Fine. Order everything you want.” “What about the money left over?” “…Did you leave your money with me?” “The more, the better.” Her shamelessness left me dumbfounded, but at the same time, I was happy. She had never once asked me for spending money. Judging by the clothes she wore and how she usually looked, she was far more modest than the kids her age I occasionally saw on the street. *What an old soul.* Come to think of it, Hayeon had been like that since she was little. She rarely cried, and she didn’t often express her feelings honestly. Her current personality had only developed after she entered high school. *She ought to be allowed to act spoiled once in a while… She grew up too soon.* *Maybe even far sooner than I did.* Was that why? None of her actions or words annoyed me in the slightest. If anything, I found her admirable, and I was happy. “Fine. Take it all. Take everything.” “Really?” “Yeah.” Hayeon beamed at my words. “That’s a relief. I almost felt bad for nothing.” “What’s there to feel bad about?” “I took three hundred thousand won from your wallet earlier.” “…Huh?” “But when you said I could have whatever was left after eating within the 100,000-won limit, I felt better.” “Hold on. Didn’t I tell you to take two hundred thousand won?” “It was an impulsive accident.” “…Don’t you mean an impulsive crime?” I take back what I said earlier. The sight of her back as she hummed her way into her room couldn’t have been more irritating. * * * The head of Sangdong Guild’s Security Team frowned. “A Cat Familiar?” “Yes, I’m certain.” The person who answered in a firm voice was a member of the Security Team and the Guild’s only Familiar mage. He was only a C-rank Hunter, but as a rare mental mage, he was also a core member of the Security Team. “The target’s younger sister is a cat fanatic. Hong Woojin took advantage of that opening perfectly.” “Can’t you read the room? You’re praising that bastard to my face?” “I-I’m sorry.” “Team 1 Leader said Hong Woojin called and went ballistic, saying he nearly got exposed because of us.” “…” “Come to think of it, that bastard is technically on our side, too. But can we afford to be outdone by a freelancer? Don’t you know the Guild Master is taking a special interest in this?” Six people had been assigned to the operation, including the Security Team Leader. One was the Familiar mage. Four were close-combat Hunters specializing in tracking and stealth. The last was the Security Team Leader himself, a B-rank Hunter. “You seem to be misunderstanding something… We didn’t come here just to dig up dirt on one C-rank Hunter.” The Security Team Leader glared menacingly at his team. The Guild Master had personally ordered this operation. They had to produce results that went beyond the direct order, no matter what. “Let’s do this properly. This came straight from the Guild Master. Are you going to end here? You should get bonuses and promotions too.” The team members silently lowered their heads. The person most desperate for a bonus and promotion was the Security Team Leader himself. The hysteria of a middle-aged family man whose retirement was slowly approaching was nothing new by this point. “And you.” The Security Team Leader pointed at the Familiar mage. “You do the cat, too.” “The cat? They already did that over there.” “What, then? Are you going to put on another pathetic act with a tiny Familiar you can’t even control and die like last time?” “…” “Do as you’re told. The girl’s a cat fanatic, isn’t she?” If he was told to use a cat, then he had to use a cat. What choice did he have? After the Security Team Leader stormed out, the Familiar mage immediately turned on his smartphone and began searching. Tap. Tap. Tap. > **Cats for Adoption in Ilsan** “…Will they let me expense this?”

#### Chapter 96 tail (verified mastered)

…
he moved away with a loose, swinging gait. *He’s a good actor.* “Meow.” Right. You’re here, too. The moment I left the house, I met two actors. Actors wearing the guises of a stray cat and a neighbor. “I’ll be back soon, so wait here quietly, okay?” The cat tilted its head as if it had no idea what I was talking about. But I knew. It had understood me, and it would still be sitting here even if several hours passed. And there was one more thing. > **System** > > Lv. 42 Kim Gwondong There weren’t any Hunters living in the building next to ours. *Just as I thought. They aren’t working together.* The appearance of the two actors was enough to turn my guess into certainty. My steps grew even lighter as I headed toward the real-estate office in front of the house. * * * Late that morning, a middle-aged man in shabby clothes dragged his slippers along while humming to himself. He looked like someone you could see anywhere. The moment he rounded the corner, he pulled out a cigarette and stuck it between his lips. “Let’s see. Where’s my lighter…” His hand rummaged slowly through his pocket, but his eyes darted around. Once he had confirmed that no one was nearby, he pulled out something other than a lighter: a miniature radio. “How was my acting? Maybe I should’ve become an actor instead of a Hunter. Seems like I’m better at acting than fighting.” —It’s me, the Team Leader. Plop. The cigarette fell from his mouth. His now-free lips moved soundlessly. *Fuck. I’m screwed.* Kim Gwondong, a C-rank Hunter in the Security Team, hurriedly collected himself and answered. “Ah, yes, Team Leader.” —Kim Gwondong’s pretty good at acting, huh? You could quit the Guild and go to Hollywood. “I-I’m sorry.” —Don’t get scared. That was a compliment. Anyway, how’s the target? He didn’t catch on, did he? “I don’t think so.” The Team Leader had already heard the conversation through Kim Junsu, but there was a simple reason he was asking again. A cat’s eyes could not capture everything about the target clearly. —Are you sure? One hundred percent? “Ninety percent.” —You little shit, is ninety percent certain? At times like this, you’re supposed to say it confidently and go for it. “It’s dangerous to jump to conclusions.” Kim Gwondong cursed the Team Leader inwardly. *What good would that do? If something goes wrong later, you’ll be the first one to rip me a new asshole.* He had to leave himself an escape route. Kim Gwondong’s ninety percent would only be complete once the Team Leader supplied the remaining ten. —That’s exactly the attitude I like to see. You know what to do next, right? The pleasure in the Team Leader’s voice signaled that they had finally reached one hundred percent. Kim Gwondong subtly changed direction to avoid a resident approaching in the distance. “Yes. I’ll circle the area naturally and keep watch.” —Right. Report immediately if anything unusual happens. “Yes.” —Keep up the good work, then. No one overheard the conversation, which lasted just over a minute. This time, Kim Gwondong took out a real lighter and lit his cigarette. He inhaled deeply. “Fuck. Lung cancer’s going to kill me before a monster does.” * * * The Security Team Leader got busy. There were three external surveillance personnel in total. He had to give instructions to the other two and make sure every precaution was taken. “Number One.” —Number One here. “You were listening on the all-team channel, right? What’s the situation with the real-estate office the target is heading to?” —There are two in the nearby shopping district. We’ve installed magical eavesdropping Equipment in both. “Good. Where’s the target?” —We haven’t seen him yet… Ah, there he is. He’s approaching from about 300 meters away. “Leave your position. We already installed the Equipment, so there’s no need to make contact for no reason.” —Yes. I’ll report immediately if anything unusual happens. “Okay. Number Two?” —Standing by at my current position. A deep voice came over the radio. The Security Team Leader nodded at the reply from another team member concealed in a nearby shop. “That bastard might veer off and take another route, so keep a close eye on him.” —Yes. Four C-rank Hunters specializing in stealth and tracking, plus a Familiar mage. They lacked combat power, but every one of them was a veteran with extensive experience in this field. *It’s overkill for one C-rank Hunter.* At first, he had been somewhat wary. The Guild Master had given them a special warning about the target. *They said he cleared a B-rank Gate alone, I think.* But the more information he gathered about the man, the more he watched him, the more he felt that was not the case at all. The fact that the information had come from Im Changsoo finally put an end to his doubts. *That good-for-nothing bastard made it all up because he didn’t want to get beaten to death.* An ordinary C-rank Hunter you could find anywhere. In his eyes, that was all Jin Taekyung was. Beep. —Target entering the real-estate office. A report came over the radio from the team member keeping watch. Sangdong Guild’s Security Team went on full alert. [^1]: A Korean term for a cat that acts like a dog—friendly and affectionate.

## Korean source

```text
＃97화



“어머, 어서 오세용.”

40대로 보이는 아주머니가 콧소리와 함께 나를 맞이했다.

집에서 가까운 부동산이라 그런가? 가끔 집에 올 때 얼핏 스쳐 갔던 얼굴 같기도 하다.

“젊은 분이 오셨네. 뭐 마실래요? 커피? 율무차? 콜라?”

“커피로 주세요.”

“블랙, 프림, 아니면…….”

“블랙이요.”

“총각이 커피 마실 줄 아네.”

쉴 새 없이 다다다 쏘아 대는 말을 한 귀로 흘리며 자리에 앉았다. 수다스러운 부동산 아줌마보다 더 신경 써야 할 곳이 있었기 때문이다.

‘이건…….’

부동산 내부에 흐르고 있는 익숙한 기운.

바로 마나(Mana)다.

‘도청 마법인가?’

사장이 설치해 놓은 보안 마법일 확률은 거의 없다. 집도 아니고 부동산에 비싼 마법 제품을 둘 리는 없으니까.

나를 감시하는 놈들이 미리 손을 쓴 게 분명했다.

‘뭐, 충분히 예상했던 일이지.’

패밀리어까지 쓰는 놈들이니 도청 마법 정도야 애교다.

문제는 도대체 놈들이 몇 명이며 어디 있냐는 건데…….

“자아, 커피 나왔습니다.”

나는 예의 바른 웃음을 지으며 커피잔을 받았다.

“아, 감사합니다.”

감사하다는 말은 진심이다.

지금부터 놈들의 근거지를 알려 줄 사람이니까.



* * *



- 그래서, 우리 잘생긴 사장님은 어떻게 오셨을까?

- 집 좀 알아보려고요.

도청 마법이 전달해 주는 음성은 또렷했다. 잠시 패밀리어 마법을 해제한 김준수와 또 다른 팀원, 보안팀장은 약속이나 한 듯이 서로를 바라봤다.

“저놈 얼마 전에도 부동산 가지 않았냐?”

“네, 고양시 쪽으로 갔었죠. 그때는 저희가 투입되기 전이라 1팀장님이 홍우진한테 정보 받아서 넘겨주셨고.”

“준수 말이 맞습니다. 나중에 저희가 부동산 찾아가서 캐 보니까 계약금까지 걸고 왔더라고요.”

“쟤 계좌에 지금 얼마 들어 있지?”

진태경의 계좌 현황은 이미 훤히 알고 있는 보안팀이다.

보안팀장의 말에 팀원이 재빨리 태블릿을 꺼내 보고서를 띄웠다.

“약 37억 정도 됩니다. 이 중에 30억 원은 새로운 집 매입 비용으로 나갈 거고요.”

“그거, 구입하는 거 확실해?”

“조만간 집주인이랑 날 잡아서 계약한다는 말까지 들었으니까 구입할 생각인 건 확실합니다. 조사해 보니 표적이 어릴 때 살던 동네라서 좀 각별한 의미가 있는 것 같더군요.”

“그렇단 말이지…….”

보안팀장은 눈살을 찌푸렸다.

곧 새로운 집에 전 재산의 대부분을 쏟아부을 놈이다. 그런데 이제 와서 이 동네에 무슨 집을 또 알아본단 말인가?

‘심지어 길드도 부천에 있고.’

무슨 생각인지는 몰라도 어쩐지 찝찝한 기분이다.

“야, 소리 좀만 더 키워 봐.”

“옙.”

세 사람의 귀에 이어지는 대화가 흘러 들어온다.

- 원하는 조건이 어떻게 되시는데?

- 월세 아니면 전세요.

- 몇 개 있긴 한데…… 알다시피 이 동네가 안전 구역에 걸쳐져 있어서 좀 비싸.

- 괜찮아요. 저 헌터거든요.

- 어머, 헌터였어? 어쩐지 몸 좋더라니. 등급이 어떻게 돼? 아, 이런 거 물어보면 좀 주책인가?

- 뭐 그럭저럭? 별로 안 높아요. C급.

- 어머, 어머. 돈 잘 벌겠네. 팔뚝 한 번 만져 봐도 돼? 오호호!

- 하하, 매물 좋은 거 보여 주시면 생각해 볼게요. 아니, 아예 싹 다 보여 주세요. 전세고 매매고 마음에 드는 거 있으면 사 버려야지.

듣고 있던 세 사람은 기가 찼다.

“이 새끼 아주 신났네. 신났어.”

“오죽하겠습니까. F급으로 살다가 재각성 후 목돈 턱턱 들어오니까 가오가 확 살겠죠.”

“음, 그렇지. 한창 그럴 때지.”

다들 경험해 봐서 안다. 새로운 세계에 발을 디딘 저 기분.

비싸서 쳐다보지도 못하던 명품이 우습게 느껴지고 사람들의 보는 눈이 달라진다.

“저 자식이 딱 그 상태네, 지금.”

“마음에 드는 게 있으면 사긴 개뿔이. 계약한 집 잔금 치르면 네 잔고로는 전세가 고작이다, 이놈아.”

“그래도 부럽네요. 쟤는 뭐 먹고 머리털이 저렇게 풍성하지?”

진태경의 치기 어린 언행들을 지켜보고 있자니 한심하면서도 피식 실소가 새어 나온다.

어느새 세 사람의 마음이 느슨하게 풀어졌다. 귀는 열려 있지만 라디오 방송을 듣는 기분이다.

- 여기 어때요? 전세로 하면 5억 정도? 안전 구역인 거 감안하면 시세보다 훨씬 저렴하게 내놓은 거야.

- 괜찮네요. 다른 곳은 없어요?

- 왜 없겠어, 당연히 있지. 방금 보여 준 곳 바로 옆옆 동에 매물 있는데…… 아, 여긴 얼마 전에 나갔었네. 월세였는데 조건이 워낙 좋아서.

- 아, 그래요?

- 응. 총각이 며칠만 더 일찍 왔어도 건지는 건데. 관리가 잘 안 되어 있는 대신에 월세가 쌌거든. 뭐 그거야 돈 있으면 리모델링으로 해결할 수 있는 문제니까.

- 그거 아쉽네요.

- 나도 아쉬워. 웬 무섭게 생긴 아저씨가 와서 무슨 명령조로 얘기하더라니까? 지가 나한테 집을 맡겨 놨나…… 나도 기왕이면 젊고 잘생긴 총각한테 넘기는 게 기분 좋잖아. 그치?

- 어휴, 완전 꼰대였나 보네요.

- 조폭인가 싶어서 찍소리 못 했지. 몸에서도 홀아비 냄새가 진동을 해서 아주 죽는 줄 알았어. 호호호.

빠드득.

옆에서 들려오는 이 가는 소리. 김준수와 팀원은 터져 나오려는 웃음을 꾹 억눌렀다.

‘팀장이네.’

‘팀장이야.’

조폭 같은 인상에 홀아비 냄새. 여기까지만 들어도 보안팀장이란 사실을 알 수 있다.

인상이 어찌나 험악한지, 그가 처음 상동 길드에 입사했을 당시 면접관이 무서워서 더 볼 것도 없이 뽑았다는 소문도 있을 정도다.

“저 아줌마가 미쳤나…….”

이를 바득바득 갈던 팀장이 고개를 홱 돌렸다. 웃음을 참느라 얼굴이 벌겋게 달아오른 두 사람이 황급히 고개를 숙였다.

“참느라 힘들어 보인다?”

“아, 아닙니다.”

“그런 사실 없습니다.”

애써 부정해 보지만 이미 빈정이 상할 대로 상한 팀장은 자리에서 일어났다. 40대 중반의 솔로인 그에게 있어 홀아비라는 말은 결코 건드려서는 안 되는 부분이었다.

“홀아비 냄새 씻으러 사우나 다녀올 테니까 오는 즉시 볼 수 있도록 녹취록 작성해 놔.”

“예?”

김준수와 다른 팀원은 어이가 없었다.

부동산에서 허세 부리는 C급 헌터와 푼수 아줌마. 두 사람의 별것 없는 대화에 무슨 녹취록까지 작성한단 말인가.

“팀장님. 이거 다 자동으로 저장되고 있는…….”

“각자 소견서도 A4 용지 한 장 꽉 채워서 준비해. 중요한 표적이니까 팀원들 의견도 수렴해 봐야지.”

“…….”

“…….”

도대체 언제부터 팀원들 의견을 물어봤다고? 그리고 그 중요한 표적을 두고 팀장이란 양반이 사우나를 간다는 게 말이 되나.

속 좁은 상관의 화풀이에 두 사람의 표정이 일그러졌다.

“내 말 못 들었어? 복명복창한다, 실시!”

“……네.”

“……실시.”

“자식들이 빠져 가지고 말이야. 팀장 알기를 아주 개똥으로 알아요.”

부하들을 노려본 보안팀장이 씩씩거리며 방을 빠져나갔다.

쾅! 아파트 현관문 닫히는 소리에 남아 있던 두 사람이 동시에 참았던 말을 토해 낸다.

“아니, 시바.”

“이건 해도 해도 너무한 거 아니에요?”

“지 인상 더럽고 결혼 못 한 걸 왜 우리한테 화풀이하냐고.”

“인상만 더럽습니까? 아줌마 얘기 들어 보니까 명령조로 얘기했다잖아요. 인성까지 글러 먹은 거지.”

“나 참, 진짜 더러워서 못 해 먹겠네.”

“아, 진짜 스트레스받으면 안 되는데. 머리 더 빠지는데.”

물기 어린 목소리로 중얼거린 김준수가 정수리를 더듬었다. 모르긴 몰라도 잠깐 사이에 열 가닥은 빠진 것 같다.

“녹취록이랑 소견서, 어떡해요?”

“어떡하긴, 팀장 지랄하는 거 보기 싫으면 써야지. 병원 가서 진단 소견서 떼어 올래?”

“…….”

“대충 써, 대충. 패밀리어 마법 쓰느라 못 썼다고 옆에서 커버 쳐 줄 테니까.”

한숨을 푹 내쉰 두 사람은 본격적으로 팀장을 욕하기 시작했다. 그 와중에도 송신기 너머에서는 대화가 이어졌다.

- 괜찮네요. 남향이라 햇빛도 잘 들어오고. 그 옆 동은 어때요? 설마 여기도 나간 건 아니죠?

- 응? 아냐. 요즘 경기가 안 좋아서 최근에 나간 곳은…… 그런데 총각.

- 예?

- 팔뚝 진짜 단단하다. 세상에, 이 근육이랑 핏줄 도드라진 것 좀 봐.

- …….



* * *



“총각, 또 와. 두 번 와!”

아줌마의 아쉬움 섞인 배웅을 뒤로하고 부동산을 나섰다. 방금 그녀의 손길이 스친 팔뚝에는 닭살이 오소소 돋아 있다.

‘아줌마나 아저씨나, 철없이 나이 먹으면 젊은 애한테 치근덕거리는 건 비슷하다니까.’

끈적끈적한 눈빛에 도망치듯 자리를 떴지만 이미 부동산을 찾은 목적은 달성한 후라 별 미련은 없었다.

‘최근에 거래된 매물 확인.’

오늘은 임창수와의 레이드로부터 정확히 5일째 되는 날이다.

그 말인즉슨, 감시자들이 붙은 것은 아무리 빨라도 5일 안이라는 뜻이 된다.

‘나름 연기랍시고 티 나지 않게 돌려서 묻긴 했는데…….’

도청 마법의 존재를 아는 나로서는 다분히 의도적인 언행이었다. 허세와 사치로 똘똘 뭉친, 별거 없는 C급 헌터로 비치길 바랐으니까.

‘속아 넘어갔을지는 미지수지만.’

부동산 아줌마와의 대화는 중요한 단서였다. 나는 미리 외워 두었던 주소를 마음속으로 중얼거렸다.

‘5동 901호. 4동 302호. 3동 202호.’

이 세 곳이 최근 5일간 거래된 매물이다.

기준은 우리 집. 패밀리어 마법이 닿는 범위인 최대 500m로 잡았다. 감시자들은 분명 이 안에 있다.

‘문제는 어떻게 찾아내냐는 거지.’

내 목적은 놈들을 쫓아내는 게 아니라, 잡아서 족친 후에 배후를 알아내는 거다. 섣부르게 헛다리 짚었다가는 도주할 가능성이 있다.

‘자동차에 숨어 있을 가능성도 있으니까 주차장도 한번 살펴보고.’

근방의 집을 뒤지기 시작하면 낌새를 눈치채겠지만 주차장은 자연스럽게 수색할 수 있다.

산책하는 척 [기감]으로 훑어보면 게임 끝이지, 뭐.



[Lv.42 김권동]



“어, 또 만났네?”

그래, 이 아저씨처럼.

나는 알은체를 해 오는 김권동에게 인사를 건넸다.

“그러게요. 또 뵙네요.”

“부동산 가신다면서? 벌써 볼일 끝난 거야?”

“그냥 문의만 했어요. 그런데 막상 가서 알아보니까 집값이 만만치가 않더라고요. 바로 도망쳐 나왔죠.”

“이 동네가 다 그렇지, 뭐. 그래도 젊은 친구가 능력이 있네. 난 그 나이에 집에서 밥만 축냈는데.”

“능력이요? 하하.”

진짜 능력이 뭔지 알면 까무러칠걸.

내 속마음도 모른 채 따라 웃던 김권동이 입을 열었다.

“그럼 난 이만 갑니다. 저쪽 공원까지 돌고 와야 해서.”

“산책을 좋아하시나 봐요?”

“응? 그거야 좋아서 하는 게 아니라 필요해서 하는 거지. 그쪽도 내 나이 되면 힘들걸?”

보란 듯이 얇은 팔다리를 흔들어 보인다. 겉모습만 보면 마르고 배만 나온 중년 아저씨가 따로 없다.

‘민간인처럼 보이기는 하네.’

다른 사람이면 깜빡 속아 넘어갔을 모습이다.

하지만 42레벨이나 되는 민간인이 있을 리가 있나.

‘아마도 C급 헌터. 체형으로 봐서는 은신, 추격 계열.’

상대가 헌터라는 것만 알면 유추해 낼 수 있는 정보는 많다.

나는 김권동에게 인사했다.

“그럼 다음에 또 뵙죠.”

“그거야 볼 수도 있고, 못 볼 수도 있고. 하하.”

글쎄, 나는 꼭 보고 싶은데.

물론 그때는 지금처럼 하하 호호 웃으면서 헤어지진 않을 거다. 지금 당장이라도 때려눕히고 싶지만, 아직은 때가 아니었다.

꾸벅.

살짝 고개 숙여 인사하고 자리를 뜨려는데 등 뒤에서 그의 목소리가 들렸다.

“아, 맞다. 그 고양이 진짜 똑똑한 놈 같던데? 오는 길에 보니까 아직도 거기 있더라고.”

패밀리어를 잊지 말고 주워 가라는 친절한 안내 방송까지 해 준다.

그리고 그의 말처럼 고양이는 아까와 같은 곳에서 날 기다리고 있었다.

야옹.

그래. 형 왔다, 인마.
```

## Current accepted English baseline

```markdown
# Chapter 97

“Oh my, welcome!”

An ajumma who looked to be in her forties greeted me with a nasal sing-song.

Maybe it was because this real-estate office was close to home. Her face looked vaguely familiar, as though I had passed her by on my way home once or twice.

“Young man, what would you like to drink? Coffee? Yulmu tea?[^1] Cola?”

“Coffee, please.”

“Black, creamer, or…”

“Black.”

“Well, look at you. A young bachelor who knows how to drink coffee.”

I let her rapid-fire chatter go in one ear and out the other as I took a seat. There was another place I needed to pay more attention to than the talkative real-estate ajumma.

*This is…*

The familiar energy flowing through the real-estate office.

It was mana.

*Wiretapping magic?*

There was almost no chance it was security magic installed by the owner. Who would put an expensive magic product in a real-estate office instead of their home?

The people watching me had clearly made preparations in advance.

*Well, it was something I expected.*

They were using Familiars, after all. Wiretapping magic was the least of it.

The question was how many of them there were and where they were hiding…

“Here you go. One coffee.”

I accepted the cup with a polite smile.

“Ah, thank you.”

I meant that sincerely.

She was about to tell me where their base was.

* * *

—So, what brings our handsome boss here?

—I’m looking for a house.

The voice transmitted by the eavesdropping magic was perfectly clear. Kim Junsu, who had briefly deactivated his Familiar magic, exchanged a look with another team member and the Security Team Leader.

“Didn’t that bastard go to a real-estate office recently, too?”

“Yes. He went to Goyang. At the time, we hadn’t been assigned to him yet, so the Team 1 Leader got the information from Hong Woojin and passed it along.”

“Junsu’s right. We went to the real-estate office afterward and dug around a little. Apparently, he even put down a deposit.”

“How much money does he have in his account right now?”

The Security Team already knew Jin Taekyung’s account balance inside and out.

At the Security Team Leader’s question, a team member quickly pulled out a tablet and brought up the report.

“About 3.7 billion won. Three billion of that will go toward buying the new house.”

“Are you sure he’s going to buy it?”

“We even heard that he’s planning to set a date with the owner and sign the contract soon, so he definitely intends to purchase it. We looked into it, and apparently it’s the neighborhood where the target lived as a child. It seems to have some special meaning to him.”

“I see…”

The Security Team Leader frowned.

The man was about to pour most of his fortune into a new house. So why was he looking into another house in this neighborhood now?

*Even though his Guild is in Bucheon.*

Whatever he was thinking, the whole thing left an unpleasant feeling in the Security Team Leader’s gut.

“Hey, turn up the volume a little.”

“Yes, sir.”

The conversation continued to flow into the three men’s ears.

—What kind of conditions are you looking for?

—Either monthly rent or a jeonse lease.

—I do have a few, but… as you know, this neighborhood straddles a safety zone, so it’s a little expensive.

—That’s fine. I’m a Hunter.

—Oh my, you’re a Hunter? I knew you looked fit. What rank are you? Ah, is it rude of me to ask something like that?

—Somewhere around there. It’s not very high. C-rank.

—Oh my, oh my. You must make good money. Can I feel that arm? Oh-ho-ho!

—Ha-ha. Show me some good listings and I’ll think about it. No, show me everything. Jeonse, purchases, whatever. If I find something I like, I’ll just buy it.

The three men listening were dumbfounded.

“That bastard’s really enjoying himself.”

“Can you blame him? He lived as an F-rank Hunter, then after his reawakening, big chunks of money started rolling in. Of course his ego would swell.”

“Hmm, true. That’s the age for it.”

They all knew from experience. The feeling of stepping into a new world.

Luxury goods they had once been unable to look at because they were too expensive suddenly seemed laughable, and other people started looking at them differently.

“That bastard’s exactly like that right now.”

“‘If I find something I like, I’ll buy it,’ my ass. Once you pay the balance on the house you already contracted for, your account will barely cover a jeonse deposit, you idiot.”

“Still, I’m jealous. What does he eat to have such thick hair?”

Watching Jin Taekyung’s childish, cocky behavior was pathetic, but a quiet laugh escaped them anyway.

Before they knew it, the three men had relaxed. Their ears were still open, but they felt as if they were listening to a radio broadcast.

—How about this place? Around five hundred million won for a jeonse lease? Considering that it’s in a safety zone, it’s much cheaper than market price.

—Not bad. Are there any others?

—Of course there are. There’s another listing in the building two over from the one I just showed you… Oh, this one already went off the market. It was monthly rent, but the terms were exceptionally good.

—Oh, really?

—Yeah. If you’d come a few days earlier, young man, you could’ve snagged it. The place wasn’t well maintained, but the rent was cheap. Of course, if you have money, remodeling can solve that problem.

—That’s a shame.

—Tell me about it. Some scary-looking man came by and spoke to me in this commanding tone. Did he think I’d been entrusted with his house or something? I’d much rather hand it over to a young, handsome bachelor, you know. Right?

—Ugh, I guess he was a total old-fashioned jerk.

—I thought he might be a gangster, so I couldn’t so much as squeak. The smell of an old bachelor was practically pouring off him. I thought I was going to die. Ho-ho-ho.

Grrrind.

The sound of teeth grinding came from beside them. Kim Junsu and the other team member suppressed the laughter threatening to burst out.

*It’s the Team Leader.*

*It really is the Team Leader.*

A gangster-like impression and the smell of an old bachelor. Just hearing that much was enough to identify the Security Team Leader.

His expression was so frightening that there was even a rumor that when he first joined Sangdong Guild, the interviewer had been too scared to look any further and hired him on the spot.

“Has that ajumma lost her mind…?”

The Team Leader ground his teeth and whipped his head around. The two men, whose faces had flushed red from holding back their laughter, hurriedly lowered their heads.

“You two look like you’re having a hard time holding it in.”

“Oh, no, sir.”

“There’s no such thing.”

They tried desperately to deny it, but the Team Leader was already thoroughly offended. He stood up.

For a single man in his mid-forties, the words *old bachelor* touched on a subject that absolutely should not be touched.

“I’m going to the sauna to wash off this old-bachelor smell, so have the transcript ready for me to read as soon as I get back.”

“What?”

Kim Junsu and the other team member were dumbfounded.

A C-rank Hunter showing off at a real-estate office and a scatterbrained ajumma. Why would anyone write up a transcript of their completely unremarkable conversation?

“Team Leader, it’s all being saved automatically…”

“Prepare a full-page A4 statement of your individual opinions, too. He’s an important target, so we should gather the team’s input.”

“…”

“…”

Since when had he ever asked for their opinions? And how could it make sense for the Team Leader to go to a sauna while they were dealing with such an important target?

Their expressions twisted at the narrow-minded superior’s petty retaliation.

“Didn’t you hear me? Repeat the order back. Execute!”

“…Yes.”

“…Execute.”

“You bastards have gotten way too lax. You treat your Team Leader like dog shit.”

The Security Team Leader glared at his subordinates, snorted angrily, and left the room.

Bang!

The apartment’s front door slammed shut. The two men left behind immediately let out everything they had been holding in.

“Man, fuck this.”

“Isn’t this taking things way too far?”

“Why is he taking out the fact that he has an ugly face and can’t get married on us?”

“Is his face the only problem? That ajumma said he spoke in a commanding tone. His personality’s rotten, too.”

“This is so damn unpleasant. I can’t keep doing this.”

“Ah, I really can’t afford to get stressed out. It’ll make even more of my hair fall out.”

Kim Junsu muttered in a voice thick with tears and felt the top of his head.

He couldn’t be sure, but it seemed like at least ten hairs had fallen out in the last few moments.

“Then what do we do about the transcript and the statements?”

“What do you think? If you don’t want to watch the Team Leader throw a fit, you have to write them. Want to go to the hospital and get a medical statement?”

“…”

“Just write something rough. I’ll cover for you and say you couldn’t write because you were using Familiar magic.”

After letting out a deep sigh, the two men began cursing the Team Leader in earnest.

Even then, the conversation continued through the transmitter.

—It’s nice. Since it faces south, it gets plenty of sunlight. What about the building next to it? Don’t tell me that one’s gone, too?

—Huh? No, it’s still available. Business has been slow lately, so the places that went recently were… Wait, young man.

—Yes?

—That arm of yours is really solid. Goodness, look at those muscles and veins.

—…

* * *

“Young man, come again. Come twice!”

I left the real-estate office with the ajumma’s regretful farewell behind me.

Goose bumps had risen all over the arm her hand had just brushed.

*Whether it’s an ajumma or an ajusshi, people who grow old without growing up are all alike when it comes to hitting on younger people.*

I had escaped as if fleeing from her sticky gaze, but I had already accomplished my purpose in visiting the real-estate office, so I had no reason to linger.

*Confirm the listings that were recently sold or leased.*

Today was exactly five days after the raid with Im Changsoo.

That meant the surveillance team had been assigned to me no more than five days ago.

*I tried to act and ask about it indirectly without making it obvious, but…*

Knowing that eavesdropping magic was in place, I had deliberately behaved that way. I wanted to come across as an unremarkable C-rank Hunter packed full of arrogance and extravagance.

*Whether they fell for it or not was another matter.*

My conversation with the real-estate ajumma had given me an important clue. I repeated the addresses I had memorized in advance in my head.

*Building 5, Unit 901. Building 4, Unit 302. Building 3, Unit 202.*

These were the listings that had changed hands in the past five days.

I had used our house as the center point and set the range at a maximum of five hundred meters—the distance Familiar magic could reach.

The watchers were definitely somewhere within that range.

*The problem is how to find them.*

My goal wasn’t to drive them away. I wanted to catch them, beat the hell out of them, and find out who was behind them.

If I jumped at the wrong lead, they might realize what was happening and run.

*They could be hiding in a car, too, so I should check the parking lot.*

If I started searching the nearby houses, they would notice something was wrong. But I could search the parking lot naturally.

All I had to do was scan the area with Qi Sense while pretending to take a walk.

Game over.

> **System**
>
> **Lv. 42 Kim Gwondong**

“Oh, we meet again.”

Just like this man.

I returned Kim Gwondong’s familiar greeting.

“Indeed. We meet again.”

“You said you were going to the real-estate office. Are you done already?”

“I just asked a few questions. But when I actually went there and looked into it, the house prices weren’t exactly cheap. I ran right back out.”

“That’s how this neighborhood is. Still, you’re doing well for yourself, young man. At your age, I was just sitting at home eating my parents’ food.”

“Doing well? Ha-ha.”

If he knew what real ability looked like, he’d faint.

Kim Gwondong laughed along, unaware of my thoughts, then spoke.

“Well, I should be going. I need to walk as far as the park over there.”

“You must like taking walks.”

“Huh? It’s not that I do it because I like it. I do it because I need to. You’ll have a hard time too once you reach my age.”

He deliberately waved his thin arms and legs.

From the outside, he looked exactly like an ordinary middle-aged man who was skinny everywhere except for his protruding belly.

*He certainly looks like a civilian.*

Anyone else would have been fooled.

But there was no way a civilian could be Level 42.

*Probably a C-rank Hunter. Judging by his build, he’s probably specialized in stealth and pursuit.*

Once you knew someone was a Hunter, there was a lot you could infer.

I said goodbye to Kim Gwondong.

“Then I’ll see you next time.”

“That depends. We might run into each other, or we might not. Ha-ha.”

Well, I definitely wanted to see him.

Of course, when that happened, I wouldn’t be parting from him with a smile and a laugh like I was now. I wanted to knock him flat right then and there, but it wasn’t time yet.

I gave him a slight bow and turned to leave.

“Oh, right. That cat seemed awfully smart. I saw it on my way over, and it was still there.”

He had even given me a friendly reminder not to forget to pick up my Familiar.

And just as he said, the cat was waiting for me in the same spot as before.

“Meow.”

Right. Hyung’s here, you punk.

[^1]: Yulmu tea is a sweet Korean grain beverage made from roasted Job’s tears.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 97`.

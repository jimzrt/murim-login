# Master Edit Task — Chapter 96

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
| 철수     | **Cheol Soo**      |
| 임창수    | **Im Changsoo**   |
| 홍우진    | **Hong Woojin**   |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 평화 | **Peace Guild** | Guild name. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
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

#### Chapter 94 tail (verified mastered)

…
a Familiar connection. I’ve been increasing it little by little, but it’s hard. If the Link gets forcibly severed, my stomach churns and I feel like I’m going to puke. There’s also a risk of mana backflow. └ Anonymous#9882: So you have to stay within five hundred meters no matter what. └ Author: Yeah. To work safely, maybe three hundred meters? You have to prepare for anything that might happen. Most people probably do the same. I was scrolling through the comments when I suddenly stopped. Had I just stumbled across something important? *The connection to a Familiar breaks beyond five hundred meters?* The maximum distance was that much, and the safe working distance was three hundred meters. In other words, if the author’s comments were true, then the people who had controlled the Familiars yesterday had been somewhere not far from my house. *And they’d be going bald, too. Maybe completely bald.* There was a strong possibility they were wearing wigs, but knowing that couldn’t hurt. I kept searching for information about Familiar magic and managed to put together a few facts. *For a B-rank mage, the maximum Familiar connection distance is five hundred meters. The safe distance is three hundred meters. If a Familiar dies, the Link is forcibly severed, and the caster also takes a slight hit.* And I realized one more thing: why they had gone out of their way to use an expensive Familiar mage to watch me. *What the hell? Tiny Familiars can slip past most detection magic?* It was like this: detection magic was a net, while tiny Familiars like flies and rice weevils were too small to get caught in it. Of course, there were products with built-in top-of-the-line detection magic capable of catching even those. But when I looked them up, they cost five hundred fifty million won—and that was the summer special price. “…” What part of that was supposed to be a summer special? I already had plenty of expenses coming my way. Five hundred million won, my ass. *One more reason to catch them myself.* My thoughts suddenly turned to the other Guild members, too. Had Familiars been attached only to my family? I still didn’t know the exact identity of the person who had commissioned this. Sangdong Guild was only the prime suspect. “That’ll be 8,400 won.” “Ah, yes. Here you go.” I paid the taxi fare and got out. The entrance to the apartment complex, which had always looked exactly the same, seemed a little unfamiliar today. The watcher’s presence bothered me like a thorn caught in my throat. *Should I contact Team Leader Choi?* I was looking at his number saved on my smartphone when— “Oppa!” A familiar swan[^1] in a green tracksuit and round glasses waved at me, her greasy hair tied tightly back. “Oh, y-yeah.” “What’s with that reaction?” “I guess I’d rather not acknowledge knowing you in public. You could say I’m embarrassed…” “You’re embarrassed by your one and only little sister? Huh?” “Go buy some clothes. What are you doing wearing a tracksuit again when you left the clothes you bought at the department store last time at home?” “You should worry about yourself. You’re one to talk, when you go around wearing the same kinds of clothes every day.” Hayeon’s pointed remark left me speechless for a moment. I had paid three hundred million won only an hour or two ago, but I was still wearing nothing but jeans and a T-shirt. Apparently, the old grime of being an ordinary little citizen, caked on over twenty-seven years, had not yet completely washed off. “A-Anyway. Where are you going?” “Where am I going? The convenience store!” Hayeon, who had been sulking until just now, began grinning foolishly. *What’s gotten into her?* I asked in a bemused voice. “Why are you so excited? Is your heart already pounding at the thought of raiding the convenience store?” “Raiding, my ass. I’m going to buy canned tuna.” “Canned tuna? Are we having tuna kimchi stew for lunch today?” “No! We’re not!” “…What’s with you today, seriously? Have you been drinking?” “You’ll be like this, too, when you see this little one.” Despite my reaction, Hayeon only continued to grin strangely, unlike her usual self. Then she lowered the zipper of her tracksuit and pulled something out from inside her clothes. A tiny ball of white-and-yellow fur wriggled in her palm. “Meeoow.” “…A kitten?” “Cute, right? I went out to sort the recycling earlier, and someone had abandoned it in a box. It had been left there for anyone who wanted to raise it.” “…” “I don’t know what kind of bastard abandoned it, but it’s pitiful, isn’t it? What did it ever do wrong? Right, Oppa?” “…Yeah. It’s not the animal’s fault.” “I got Mom’s permission to foster it, even if it’s only for a little while. You’re okay with it, too, right?” “Me?” “Yeah. You know how our Mrs. Kim melts for her eldest son. She told me to get your permission, too, so put in a good word for me when we go inside later.” “We’ll see.” “What? You liked animals when you were little.” I did. I still do, in fact. But this little thing sitting quietly in Hayeon’s palm was… > **System** > > Lv. 2 Cat—Familiar A little different. [^1]: In Korean slang, a “swan” is an unemployed woman.

#### Chapter 95 tail (verified mastered)

…
over 300 million won. In every respect, this was a losing proposition. I was watching TV with my face twisted into a scowl when Hayeon cautiously studied my expression and spoke. “Oppa, are you mad?” “No. What would I be mad about?” “I’m sorry.” “…What’s gotten into you? You’re starting to scare me.” I wasn’t joking. I was more startled than when I had first discovered the Familiar. Since when could she say something like that? I asked seriously. “Are you sick?” “No, it’s just…” “Then are you hungry?” “That’s not it…” Just as Hayeon hesitated, about to say something, a stomach growled from somewhere. It wasn’t mine. Mom had stepped out to run an errand. “You’re hungry.” “Mm, a little?” “Right. You’re so hungry you’re starting to spout nonsense. You know where my wallet is, right? Order anything you want to eat.” “Really?” “Yeah. Up to a hundred thousand won.” “Wow, now that you’re making money, you’ve gotten generous. Our Oppa.” I never thought I’d live to hear her call me “our Oppa.” It was the first time I’d heard it since Hayeon had been in middle school, and it gave me goose bumps. “You’re the Familiar, you little bastard!” “What are you talking about? Anyway, I can order whatever I want as long as it’s under a hundred thousand won?” “Yeah. No, wait. Fine. Order everything you want.” “What about the money left over?” “…Did you leave your money with me?” “The more, the better.” Her shamelessness left me dumbfounded, but at the same time, I was happy. She had never once asked me for spending money. Judging by the clothes she wore and how she usually looked, she was far more modest than the kids her age I occasionally saw on the street. *What an old soul.* Come to think of it, Hayeon had been like that since she was little. She rarely cried, and she didn’t often express her feelings honestly. Her current personality had only developed after she entered high school. *She ought to be allowed to act spoiled once in a while… She grew up too soon.* *Maybe even far sooner than I did.* Was that why? None of her actions or words annoyed me in the slightest. If anything, I found her admirable, and I was happy. “Fine. Take it all. Take everything.” “Really?” “Yeah.” Hayeon beamed at my words. “That’s a relief. I almost felt bad for nothing.” “What’s there to feel bad about?” “I took three hundred thousand won from your wallet earlier.” “…Huh?” “But when you said I could have whatever was left after eating within the 100,000-won limit, I felt better.” “Hold on. Didn’t I tell you to take two hundred thousand won?” “It was an impulsive accident.” “…Don’t you mean an impulsive crime?” I take back what I said earlier. The sight of her back as she hummed her way into her room couldn’t have been more irritating. * * * The head of Sangdong Guild’s Security Team frowned. “A Cat Familiar?” “Yes, I’m certain.” The person who answered in a firm voice was a member of the Security Team and the Guild’s only Familiar mage. He was only a C-rank Hunter, but as a rare mental mage, he was also a core member of the Security Team. “The target’s younger sister is a cat fanatic. Hong Woojin took advantage of that opening perfectly.” “Can’t you read the room? You’re praising that bastard to my face?” “I-I’m sorry.” “Team 1 Leader said Hong Woojin called and went ballistic, saying he nearly got exposed because of us.” “…” “Come to think of it, that bastard is technically on our side, too. But can we afford to be outdone by a freelancer? Don’t you know the Guild Master is taking a special interest in this?” Six people had been assigned to the operation, including the Security Team Leader. One was the Familiar mage. Four were close-combat Hunters specializing in tracking and stealth. The last was the Security Team Leader himself, a B-rank Hunter. “You seem to be misunderstanding something… We didn’t come here just to dig up dirt on one C-rank Hunter.” The Security Team Leader glared menacingly at his team. The Guild Master had personally ordered this operation. They had to produce results that went beyond the direct order, no matter what. “Let’s do this properly. This came straight from the Guild Master. Are you going to end here? You should get bonuses and promotions too.” The team members silently lowered their heads. The person most desperate for a bonus and promotion was the Security Team Leader himself. The hysteria of a middle-aged family man whose retirement was slowly approaching was nothing new by this point. “And you.” The Security Team Leader pointed at the Familiar mage. “You do the cat, too.” “The cat? They already did that over there.” “What, then? Are you going to put on another pathetic act with a tiny Familiar you can’t even control and die like last time?” “…” “Do as you’re told. The girl’s a cat fanatic, isn’t she?” If he was told to use a cat, then he had to use a cat. What choice did he have? After the Security Team Leader stormed out, the Familiar mage immediately turned on his smartphone and began searching. Tap. Tap. Tap. > **Cats for Adoption in Ilsan** “…Will they let me expense this?”

## Korean source

```text
＃96화



김준수는 상동 길드 보안팀 소속의 C급 헌터다.

원소 마법에는 재능이 쥐뿔도 없었지만 다행히 희귀하다는 정신계 마법사로 각성한 덕에 나름 잘나가는 인생을 살고 있었다.

‘집에 못 들어가는 것만 빼면.’

100평이 넘는 집을 갖고 있으면 뭐 하나. 상동 길드 유일의 패밀리어 마법사인 그는 일거리가 끊이질 않았다.

레이드 팀은 게이트 돌고 나면 퇴근이라도 하지, 보안팀은 그딴 거 없이 매번 달라지는 아지트에서 밤을 새야 한다.

“준수야, 밤샜냐?”

“네.”

김준수의 퀭한 얼굴을 본 보안팀의 동료가 혀를 찼다. 귀중한 패밀리어 마법사를 경호하기 위해 남아 있던 한 사람이다.

“고생 많다. 저 새끼는 어떻게 집 밖으로 한 발자국을 안 나오냐?”

“그러니까요. 며칠째 감시 중인데 지금까지 딱 두 번 나왔어요, 두 번. 고양시 쪽 부동산 한 번이랑 일산 스토어.”

“이래서 표적 대상은 흡연자인 게 좋은데. 걔들은 담배 피우러 나오기라도 하잖아.”

새로 구한 고양이를 패밀리어 삼아 밤새 아파트 동 입구에서 기다렸지만 표적은 꿈쩍도 하지 않았다.

유일한 사건이라면 기다림에 지쳐 야옹거리며 울다가 경비 아저씨한테 쫓겨날 뻔했던 것뿐이다.

“평화 길드? 보니까 규모도 작던데 레이드도 안 뛰나.”

“쟤들 지금 휴가래.”

“휴가요?”

“어. 2조에 있는 내 동기가 평화 길드 다른 애들 감시 중인데 다 쉬고 있다던데?”

“아…… 그쪽 상황은 어떻대요?”

“어제부로 철수. 여자 하나랑 아저씨 하난데 금방 끝났다더라. 팀장 반응 봐서는 그쪽에서 뭐 하나 건진 거 같긴 한데 잘은 모르겠고.”

“후우. 이쪽도 그냥 적당히 하고 철수하지.”

깊은 한숨을 내쉬는 김준수를 동료가 안쓰러운 표정으로 바라봤다.

“길드에 딱 한 명 있는 패밀리어 마법사를 특별히 붙인 이유가 있지 않겠어?”

“그래 봤자 C급 헌터인데, 이렇게까지 공들이는 건 좀 아니지 않아요?”

“어쩌겠냐. 까라면 까야 하는걸. 팀장이 어제처럼 쪼아 대도 그러려니 해.”

“적당히 쪼아 대야죠. 애초에 홍우진인가 하는 그 사람이랑 얘기해서 잘 협력했으면 진작 끝났을 문젠데.”

“길드장님께 보여 주고 싶은 거지. 우리 보안팀이 홍우진보다 훨씬 낫다. 내 리더십이 이렇게 뛰어나다. 안 그래도 슬슬 하반기 인사이동 시즌인데 팀장도 똥줄 탈 만하잖아.”

“……환장하겠네요.”

“환장하지.”

김준수는 머리라도 쥐어뜯고 싶은 마음이었지만 꾹 참았다. 그랬다가는 이제 겨우 봄철 새순처럼 돋아난 머리카락이 뽑혀 나갈지 모른다.

‘아, 의사가 스트레스받으면 탈모 악화된다고 했는데.’

그 쉬운 라이트 마법도 못 쓰는 민간인 의사지만 머리만 풍성하게 만들어 준다면 예수님으로 모실 수 있다.

‘그러고 보니 오늘은 머리가 별로 안 빠진 것 같기도 하고.’

김준수가 조심스럽게 정수리를 더듬으려던 그때였다.

- 표적 확인. 표적 확인. 이동 중!

무전기 너머로 들려오는 낮지만 긴박한 동료의 목소리.

방 안의 두 사람은 물론이고 옆방에서 코를 골고 있던 보안팀장까지 벌떡 일어났다.

추르릅. 입가의 침을 훔친 그가 외친다.

“야! 김준수!”

젠장. 아직 아침도 못 먹었는데.

패밀리어 마법 쓰면 머리 또 빠지는데!

‘씨바, 계약 끝나면 바로 길드 때려치운다.’

눈물을 삼킨 김준수가 마나를 끌어 올렸다. 머리가 뜨거워지며 의식이 빨려 들어간다.

‘충실한 종이여, 내 부름에 답하라. 링크!’

화악!

그리고 다음 순간, 차 밑에 엎드려 있던 새끼 고양이가 번쩍 눈을 떴다.

미야옹.



* * *



나는 걸음을 멈췄다. 울음소리와 함께 갑자기 불쑥 튀어나온 검은 털 뭉치 때문이다.



[Lv.2 고양이 - 패밀리어]



“…….”

또 고양이네. 이 자식들은 창의력이 이렇게 없나?

아, 하나 달라지긴 했다. 이놈은 털 색이 새까맣다.

미앙. 미야앙.

새끼치고는 제법 당찬 걸음으로 다가온 고양이가 내 슬리퍼에 온몸을 비비적거렸다. 시전자가 누군지는 몰라도 클럽에서 좀 놀아 본 솜씨다.

‘거참. 이런 식으로 관심받는 건 별론데.’

하지만 새로운 패밀리어의 등장 덕분에 새로운 사실을 짐작할 수 있었다.

‘이놈들, 한패가 아닌가?’

하루 간격으로 고양이처럼 눈에 띄는 패밀리어를 두 마리나? 결코 좋은 접근 방식이 아니다. 오히려 황급히 따라 한다는 느낌이 강했다.

냥!

관심을 가져 달라는 듯이 울어 대는 고양이의 모습에 나는 피식 웃었다.

“짜식, 귀엽네.”

이놈을 데려가야 하나, 말아야 하나…….

머리가 바쁘게 돌아가던 그때였다.

“고양이가 애교가 많네. 아저씨가 기르는 거예요?”

슬리퍼를 질질 끌며 다가온 한 남자. 40대 초반 정도로 보이는 얼굴은 지극히 평범했고 목 늘어난 티셔츠와 라면 국물이 묻은 축구 반바지는 친근하다.

“아뇨. 길고양이인 것 같은데 갑자기 애교를 부리네요.”

“이야, 이거 완전히 그거잖아. 개냥이.”

“그러게요. 어제도 그렇고, 이 동네 고양이들은 애교가 많나 봐요.”

“어제요?”

“네, 어제도 한 마리 주웠거든요. 개냥이로.”

“거 신기하네.”

남자가 반쯤 타들어 간 담배를 한 모금 빨았다.

“이렇게 보면 짐승들도 다 인연이 있는 것 같어. 좋은 주인이 될 것 같으니까 고양이가 애교도 부리고 하지.”

“에이, 좋은 주인은 무슨. 그냥 원래 이런 성격인 것 같은데요?”

“그런가? 야, 야, 이리 와 봐.”

아저씨의 손짓에도 고양이는 꿈쩍도 하지 않는다.

아니, 오히려 내 다리 사이로 파고들었다.

“허허. 이놈 봐라. 어린 게 벌써부터 사람을 가릴 줄 아네.”

내가 말없이 웃고만 있자 아저씨가 묻는다.

“그래서, 키우시려고?”

“글쎄요. 지금 급한 볼일이 있어서. 끝내고 왔을 때도 있으면 며칠 데리고 있어 보죠, 뭐.”

“그때까지 이놈이 여기 있을까 모르겠네. 그치, 나비야?”

에옹.

“얼마 안 걸려요. 요 앞에 부동산 가는 거라.”

“그래요? 참, 그쪽 젊은 양반은 처음 보는 분이시네. 나 여기 오래 살아서 어지간한 사람은 다 아는데. 부동산 가신다는 거 보니 새로 이사 오시는 분인가?”

“저는 따로 살아서요. 가족들 보러 어쩌다 한 번씩만 옵니다. 부동산은 잠깐 뭐, 일이 있어서요.”

“아아…….”

후우. 마지막 연기가 바람에 흩어진다. 담배꽁초를 바닥으로 튕긴 아저씨가 입을 열었다.

“이거 참, 내가 바쁜 사람 붙잡고 있었네. 마음 상한 건 아니죠?”

“전혀요.”

“그럼 다행이고. 다음에 만나면 알은체나 합시다. 이웃사촌끼리.”

내가 대답했다.

“네, 이웃사촌끼리.”

“그럼 먼저 갑니다. 날씨도 좋은데 동네나 한 바퀴 돌아야지.”

사람 좋은 웃음을 지은 아저씨가 걸음을 옮긴다. 휘적거리는 걸음으로 멀어지는 그의 뒷모습을 잠시 바라보며 생각했다.

‘연기 잘하네.’

야옹.

그래, 너도 있었지.

집을 나서자마자 연기자를 두 명이나 만났다. 길고양이와 이웃사촌이라는 탈을 쓴 연기자를.

“금방 올 테니까 여기서 얌전히 기다리고 있어라, 응?”

고양이가 무슨 소리냐는 듯 고개를 갸우뚱한다.

하지만 나는 알고 있다. 저 녀석이 내 말을 알아들었고, 몇 시간이 흘러도 이 자리에 있을 거라는 사실을.

그리고 하나 더.



[Lv.42 김권동]



우리 집 옆 동에는 헌터가 살지 않는다는 사실을.

‘역시 한패가 아니야.’

두 연기자의 등장은 짐작을 확신으로 바꾸기에 충분했다.

집 앞 부동산을 향하는 내 발걸음은 한층 더 가벼워져 있었다.



* * *



늦은 아침, 슬리퍼를 질질 끌며 콧노래를 부르는 후줄근한 차림의 중년인. 어디에서나 흔하게 찾아볼 수 있는 모습인 그는 코너를 돌자마자 담배 한 개비를 빼 물었다.

“어디 보자, 라이터가…….”

손은 느릿느릿 주머니를 뒤지지만 눈은 바쁘게 움직인다.

주위에 아무도 없는 것을 확인한 그가 라이터 대신 꺼낸 것은 초소형 무전기였다.

“연기 괜찮았어? 나 헌터 말고 배우나 할 걸 그랬나 봐. 어째 전투보다 연기를 더 잘해.”

- 나 팀장이다.

툭. 입에 물고 있던 담배가 떨어졌다. 덕분에 자유로워진 입이 벙긋거린다.

시바, 좆 됐네.

황급히 정신을 수습한 보안팀 소속 C급 헌터, 김권동이 대답했다.

“아, 예. 팀장님.”

- 이야, 김권동이 연기 잘하데? 길드 관두고 할리우드 가도 되겠더라.

“죄, 죄송합니다.”

- 쫄기는, 칭찬이야. 그건 그렇고 표적은 어때? 냄새 못 맡았겠지?

“제 생각으로는 그렇습니다.”

패밀리어 마법을 사용 중인 김준수를 통해 대화를 이미 들었을 텐데도 재확인하는 이유는 간단하다.

고양이의 시선으로는 표적의 모든 것을 명확하게 담을 수 없기 때문이다.

- 확실해? 100%?

“90%입니다.”

- 자식이, 90%가 확실한 거냐? 이럴 때는 자신감 있게 질러야지.

“섣부른 판단은 금물이니까요.”

김권동은 속으로 팀장을 욕했다.

‘자신 있게 지르면 뭐 해. 나중에 일 잘못되면 나한테 제일 먼저 지랄할 거면서.’

이런 식으로 빠져나갈 구멍은 만들어 둬야 한다. 김권동의 90%는 팀장의 10%가 더해져야 비로소 완성된다.

- 그런 모습 아주 보기 좋아. 다음 행동은 알지?

팀장의 기분 좋은 목소리는 이제야 100%가 됐다는 신호다.

김권동은 저 멀리서 걸어오는 주민을 피해 슬그머니 발길을 틀었다.

“예. 자연스럽게 주위 맴돌면서 관찰하겠습니다.”

- 그래, 특이 사항 생기면 바로바로 보고하고.

“예.”

- 그럼 수고.

1분 남짓 이루어진 둘의 대화는 아무도 듣지 못했다.

이번에는 진짜 라이터를 꺼내 담배에 불을 붙인 김권동이 연기를 깊이 들이마셨다.

“시발, 몬스터한테 죽는 것보다 폐암 걸려 죽는 게 더 빠르겠네.”



* * *



보안팀장이 바빠졌다. 외부 감시 인원은 총 셋. 남은 두 명에게 지시를 하달하고 만전을 기해야 한다.

“1번.”

- 1번 등장했습니다.

“전체 채널로 듣고 있었지? 표적이 가는 부동산은 어떻게 됐어?”

- 인근 상가에 두 개 있고, 두 곳 모두 도청 마법 장비 깔았습니다.

“잘했어. 표적 위치는?”

- 아직 안 보이는…… 아, 등장했습니다. 약 300m 밖에서 접근 중.

“자리 떠. 어차피 장비 깔았으니까 괜히 접촉할 필요 없어.”

- 예. 특이 사항 있으면 바로 보고하겠습니다.

“오케이. 2번은?”

- 현 위치에서 대기 중입니다.

무전기 너머로 들려오는 굵은 목소리.

근처 상가에 은신해 있던 또 다른 팀원의 대답에 보안팀장이 고개를 끄덕였다.

“이 자식 다른 길로 샐 수도 있으니까 잘 감시해.”

- 네.

은신, 추적 계열의 C급 헌터 넷과 패밀리어 마법사.

전투력은 떨어지지만 이 분야에서는 하나같이 풍부한 경험이 있는 베테랑들이다.

‘C급 헌터 하나한테 붙기에는 과분한 정도지.’

처음에는 약간의 경계심이 있었다. 표적에 관하여 길드장이 특별히 언질한 부분이 있었기 때문이다.

‘B급 게이트를 혼자 클리어했다고 했지, 아마.’

하지만 놈에 관한 정보를 모을수록, 지켜보면 지켜볼수록 전혀 아니라는 생각이 들었다. 의심에 종지부를 찍은 건 정보의 출처가 임창수라는 사실이다.

‘망나니 새끼가 맞아 죽기 싫어서 이빨 깐 거지.’

어디서나 볼 수 있는 평범한 C급 헌터.

그의 눈에 비친 진태경은 딱 그 정도였다.

삑.

- 표적, 부동산으로 들어갑니다.

감시하고 있던 팀원의 무전.

상동 길드 보안팀은 촉각을 곤두세웠다.
```

## Current accepted English baseline

```markdown
# Chapter 96

Kim Junsu was a C-rank Hunter belonging to Sangdong Guild’s Security Team.

He had not an ounce of talent for elemental magic, but fortunately, he had awakened as a rare type of mage—a mental mage—and was living a fairly successful life.

*Except for the fact that I can’t go home.*

What good was owning a house larger than 330 square meters? As the only Familiar mage in Sangdong Guild, he never ran out of work.

Raid teams at least got to go home after running a Gate, but the Security Team had no such luxury. They had to spend every night in a different hideout.

“Junsu, did you pull an all-nighter?”

“Yes.”

A colleague on the Security Team clicked his tongue when he saw Kim Junsu’s hollowed-out face. He was the one person who had stayed behind to protect their valuable Familiar mage.

“You’re working hard. How does that bastard manage not to step outside even once?”

“I know. We’ve been watching him for days, and he’s only gone out twice. Twice. Once to a real-estate office in Goyang and once to the Ilsan Store.”

“This is why it’s better when the target smokes. At least smokers come outside to have a cigarette.”

They had obtained a new cat to use as a Familiar and waited all night at the entrance of the apartment building, but the target had not budged.

The only incident was when the cat, exhausted from waiting, started meowing and was nearly chased away by a security guard.

“Peace Guild? It looked pretty small. Do they even go on raids?”

“They’re on vacation right now.”

“Vacation?”

“Yeah. A guy from Team 2 is watching the other members of Peace Guild, and apparently they’re all taking time off.”

“Ah… How’s that situation going?”

“They pulled out yesterday. There was one woman and one middle-aged man, but it ended quickly. Judging by the Team Leader’s reaction, it seems like they turned up something over there, but I don’t know the details.”

“Phew. We should just do enough to get by and pull out, too.”

His colleague looked at Kim Junsu with pity as he let out a deep sigh.

“There has to be a reason they specially assigned the Guild’s only Familiar mage, right?”

“He’s still only a C-rank Hunter. Don’t you think this is going a little overboard?”

“What can we do? When we’re told to do something, we have to do it. Even if the Team Leader hounds us like he did yesterday, we just have to put up with it.”

“He should hound us in moderation. This would’ve been over ages ago if he had just talked to that Hong Woojin guy and cooperated properly.”

“He wants to show the Guild Master. ‘Our Security Team is much better than Hong Woojin. My leadership is this outstanding.’ Besides, it’s almost time for the second-half personnel reshuffle. No wonder the Team Leader is sweating bullets.”

“…This is driving me insane.”

“It is.”

Kim Junsu wanted to tear his hair out, but he held himself back. If he did, the hair that had only just begun sprouting like fresh spring shoots might come right out.

*Ah, the doctor said stress makes hair loss worse.*

The doctor was a civilian who couldn’t even use the simple Light magic, but if he could give Kim Junsu a full head of hair, Junsu would worship him as Jesus.

*Come to think of it, maybe I haven’t lost much hair today.*

That was when Kim Junsu cautiously reached up to feel the crown of his head.

—Target confirmed. Target confirmed. Moving!

A low but urgent voice came through the radio.

The two men in the room—and even the Security Team Leader, who had been snoring in the next room—bolted upright.

Slurp. After wiping the drool from his mouth, the Team Leader shouted.

“Hey! Kim Junsu!”

*Damn it. I haven’t even eaten breakfast yet.*

*Using Familiar magic makes my hair fall out again!*

*Fuck this. I’m quitting the Guild the moment my contract ends.*

Swallowing back his tears, Kim Junsu drew up his mana. His head grew hot, and his consciousness was pulled inward.

*Faithful servant, answer my call. Link!*

Whoosh!

The next moment, a kitten lying beneath a car opened its eyes wide.

“Myaowww.”

* * *

I stopped walking.

A black ball of fur had suddenly popped out with a cry.

> **System**
>
> **Lv. 2 Cat—Familiar**

“…”

Another cat. Did these bastards have no creativity at all?

Well, one thing was different. This one’s fur was pitch-black.

“Miaow. Miaowww.”

The kitten approached with surprisingly confident steps for such a young creature, then rubbed its entire body against my slipper. Whoever had cast the spell clearly knew its way around a club.

*Man. I don’t like getting attention this way.*

But the appearance of this new Familiar allowed me to make a new guess.

*Could they be working together?*

Two conspicuous Familiars, both in the form of cats, appearing a day apart? It was hardly a good approach. If anything, it felt like someone had hurriedly copied the first attempt.

“Meow!”

The cat cried as if demanding my attention, and I let out a quiet laugh.

“You little thing. You’re cute.”

Should I take it with me or not…?

My mind was racing when—

“That cat’s pretty affectionate. Is it yours, sir?”

A man approached, dragging his slippers. He looked to be in his early forties, with an utterly ordinary face. His stretched-out T-shirt and soccer shorts stained with ramen broth gave him a friendly, familiar air.

“No. I think it’s a stray, but it suddenly started acting affectionate.”

“Wow, this is totally one of those. A dog-cat.”[^1]

“Exactly. Just like yesterday. I guess the cats in this neighborhood are pretty affectionate.”

“Yesterday?”

“Yeah, I picked up another one yesterday. It was a dog-cat, too.”

“That’s strange.”

The man took a drag from a half-burned cigarette.

“When you look at things like this, even animals seem to have connections with people. The cat’s acting affectionate because you look like you’d make a good owner.”

“Come on, what do you mean, a good owner? I think it just has this kind of personality.”

“Is that so? Hey, hey, come here.”

The cat did not move at the man’s beckoning.

No, it burrowed between my legs instead.

“Well, look at this one. Young as it is, it already knows how to pick its people.”

I only smiled without saying anything, so the man asked,

“So, are you planning to raise it?”

“I’m not sure. I have somewhere urgent to be right now. If it’s still here when I get back, I’ll keep it for a few days.”

“Who knows if it’ll still be here by then. Right, Nabi?”

“Mrow.”

“It won’t take long. I’m just going to the real-estate office right over there.”

“Really? Oh, come to think of it, I’ve never seen you before, young man. I’ve lived here a long time, so I know just about everyone. Since you’re going to a real-estate office, are you moving into the neighborhood?”

“I live somewhere else, so I only come by to see my family once in a while. I just have something to take care of at the real-estate office.”

“Ah…”

Phew. His final breath of smoke scattered in the wind. The man flicked his cigarette butt onto the ground and spoke.

“Well, look at me, holding up a busy man. You’re not offended, are you?”

“Not at all.”

“Then that’s good. If we meet again, let’s say hello. We’re neighbors, after all.”

I answered,

“Yes. We’re neighbors.”

“Then I’ll be off. The weather’s nice, so I should take a lap around the neighborhood.”

The man gave me a good-natured smile and started walking. I watched his retreating back for a moment as he moved away with a loose, swinging gait.

*He’s good at acting.*

“Meow.”

Right. You’re here, too.

The moment I left the house, I met two actors. Actors wearing the guises of a stray cat and a neighbor.

“I’ll be back soon, so wait here quietly, okay?”

The cat tilted its head as if it had no idea what I was talking about.

But I knew. I knew that it understood me—and that it would still be sitting here even after several hours had passed.

And there was one more thing.

> **System**
>
> **Lv. 42 Kim Gwondong**

There wasn’t a Hunter living in the building next to ours.

*So they aren’t working together.*

The appearance of the two actors was enough to turn my suspicion into certainty.

My steps grew lighter as I headed toward the real-estate office in front of the house.

* * *

Late in the morning, a middle-aged man in shabby clothes dragged his slippers along while humming. He was such an ordinary sight that he could be found anywhere. The moment he turned the corner, he pulled out a cigarette and placed it between his lips.

“Let’s see. Where’s my lighter…”

His hand moved slowly as it rummaged through his pocket, but his eyes were moving busily.

After confirming that no one was nearby, he pulled out something else instead of a lighter: a miniature radio.

“Was the acting okay? Maybe I should’ve become an actor instead of a Hunter. I’m better at acting than fighting.”

—It’s me, the Team Leader.

Plop.

The cigarette fell from his mouth. His now-free lips moved soundlessly.

*Shit. I’m screwed.*

The C-rank Hunter Kim Gwondong, a member of the Security Team, hurriedly pulled himself together and answered.

“Ah, yes, Team Leader.”

—Kim Gwondong’s pretty good at acting, huh? You could quit the Guild and go to Hollywood.

“I-I’m sorry.”

—Don’t get scared. It’s a compliment. Anyway, how’s the target? He didn’t smell anything, right?

“I don’t think so.”

The reason the Team Leader asked again, despite having already heard the conversation through Kim Junsu, was simple.

A cat’s eyes could not capture everything about the target clearly.

—Are you sure? One hundred percent?

“Ninety percent.”

—You little shit, is ninety percent certain? At times like this, you’re supposed to say it confidently and go for it.

“Jumping to conclusions is dangerous.”

Kim Gwondong cursed the Team Leader inwardly.

*What good does it do me to say it confidently? If something goes wrong later, you’ll be the first one to chew me out.*

He had to leave himself an escape route like this. Kim Gwondong’s ninety percent would only be complete once the Team Leader added his ten percent.

—That attitude of yours is exactly what I like to see. You know what to do next, right?

The Team Leader’s pleasant voice was a sign that he had finally reached one hundred percent.

Kim Gwondong subtly changed direction to avoid a resident approaching from far away.

“Yes. I’ll naturally circle around the area and keep watch.”

—Right. Report immediately if anything unusual happens.

“Yes.”

—Then keep up the good work.

The conversation between the two men lasted a little over a minute, and no one heard it.

This time, Kim Gwondong took out a real lighter and lit his cigarette. He inhaled deeply.

“Fuck. Looks like lung cancer’s going to kill me faster than a monster.”

* * *

The Security Team Leader got busy. There were three external surveillance personnel in total. He had to give instructions to the other two and make sure everything was in place.

“Number One.”

—Number One here.

“You were listening on the all-team channel, right? What about the real-estate office the target is heading to?”

—There are two in the nearby shopping district, and we’ve installed eavesdropping-magic Equipment in both.

“Good. Where’s the target?”

—We haven’t seen him yet… Ah, there he is. He’s approaching from about 300 meters away.

“Leave your position. We already installed the Equipment, so there’s no need to make contact for no reason.”

—Yes. I’ll report immediately if anything unusual happens.

“Okay. Number Two?”

—Waiting at my current position.

A deep voice came through the radio.

The Security Team Leader nodded at the reply from another team member hiding in a nearby shop.

“That bastard might take another route, so keep a close eye on him.”

—Yes.

Four C-rank Hunters specializing in stealth and tracking, along with a Familiar mage.

Their combat power was low, but every one of them was a veteran with extensive experience in this field.

*It’s overkill for one C-rank Hunter.*

At first, he had been somewhat wary. The Guild Master had given them a special warning about the target.

*They said he cleared a B-rank Gate alone, I think.*

But the more information he gathered about the man, the more he watched him, the more he felt that was not the case at all. The fact that the information had come from Im Changsoo finally put an end to his doubts.

*That good-for-nothing bastard made it all up because he didn’t want to get beaten to death.*

An ordinary C-rank Hunter whom one could find anywhere.

That was all Jin Taekyung was in his eyes.

Beep.

—Target entering the real-estate office.

A report came over the radio from the team member keeping watch.

Sangdong Guild’s Security Team went on full alert.

[^1]: A Korean term for a cat that acts like a dog—friendly and affectionate.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 96`.

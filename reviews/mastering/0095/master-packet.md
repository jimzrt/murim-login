# Master Edit Task — Chapter 95

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
| 상태               | **Status**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
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

#### Chapter 93 tail (verified mastered)

…
a Store filled with all kinds of goods ordinary people could never access. “…Hey, hey. Let’s go.” Only after the kids loitering out front had left did the guard notice me. He addressed me politely. “What brings you here?” “I’d like to purchase something.” “Please present your membership card or Hunter certification.” “Here.” “I’ll need to complete the verification process.” Only after my certification had been checked and my fingerprints scanned was I given an admission pass. “As a C-rank Hunter, you may access up to the third floor.” The Store stocked different items on each floor. I had visited once when I was an F-rank Hunter, but the second floor had been the highest I could access at the time. I had never even gotten to look around above it. “Have a pleasant time.” “Thanks. Take care.” Once I passed through the doors, I saw endless rows of glass display cases. The space was incomparably larger than an ordinary shop, yet there were only a handful of customers in sight. *Well, it would be strange if this place were crowded.* Only a tiny minority could shop here: Hunters, who made up just 0.1 percent of Korea’s population, and civilians with enough social influence to be issued membership cards. They were the Store’s main customers. “This item was manufactured by domestic S Company and has a built-in alarm spell, making it useful for security…” “This brooch was made by overseas M Company. With its beautiful, tasteful design and built-in shield spell, it’s perfect for your wife’s personal protection…” The employees were busy explaining their products to customers. That was right. The Store was a kind of luxury department store where people could buy expensive magical goods that were difficult to obtain through ordinary channels. “Then I’ll take that one and this one. Bring me that, too.” “Don’t you have anything with better performance? Don’t worry about the price. Bring me some options.” There might not have been many customers, but their purchasing power was unmatched. I was staring blankly at people buying goods that cost at least several million won when a pretty female employee approached and bowed. “Hello. I’m Assistant Manager Kim Seonhee from the Ilsan Store. I’ll be assisting you today.” “Ah, yes.” They had treated me politely the last time I visited, too, but not to this extent. Now that I was a C-rank Hunter, the customer service was considerably more attentive. “Is there a particular product you’re looking for?” “I’d like to buy some raid equipment.” The employee’s expression brightened. The Store carried countless magical goods, but Hunter equipment was among the most expensive of them all. And I was a C-rank Hunter. Even a mid-level Hunter could spend hundreds of millions of won on a single piece of equipment. Naturally, a sales employee would be delighted at the thought of adding that kind of sale to her record. “I’ll show you to the third floor.” As she turned toward the escalators, I spoke. “No, please take me to the second floor.” “Pardon? But to purchase C-rank Hunter equipment, you’ll need to go to the third floor…” “It’s fine. I’m looking for weapons for low-rank Hunters.” I pretended not to notice her expression darkening and stepped onto the escalator first. *I wonder if they have anything useful for killing rats.* The time had come to fill my Inventory. * * * “It’s fine. I’m looking for weapons for low-rank Hunters.” Assistant Manager Kim Seonhee secretly sighed at the customer’s words. As someone unusually concerned about her sales numbers, this was far from welcome news. *I need a good sales record this month if I want to get promoted.* The colleague who had joined the company at the same time as her and worked at the Seoul branch was already a Team Leader. Whether it was luck or business savvy, every customer she encountered was apparently a big spender. Compared to her… “This one looks good.” “Ah, yes. This product was manufactured using an F-rank Magic Gem…” Kim Seonhee quickly pulled herself together and began her explanation. The customer had picked up a dagger with a black-painted blade. Compared to the other weapons, it was nothing special. It did not even have magic embedded in it. It was just an ordinary consumable. “How much is it?” “It’s currently on sale as part of our summer promotion, so we’re offering it at the low price of 520,000 won.” “Hmm. That’s expensive.” “…” How much did a C-rank Hunter make a year again? Didn’t their basic allowances alone amount to several hundred million won? Kim Seonhee found it ridiculous, but silently waited for the customer to make his choice. “Ah, well, I guess it can’t be helped. I’ll buy it. Give me one.” “…Yes.” The look on his face, as if parting with the money were killing him, was utterly obnoxious. Kim Seonhee swallowed a curse as she picked up the dagger when— “No. Not that one.” “Excuse me?” “The one next to it.” Her gaze shifted to the side. One hundred daggers were neatly arranged inside a storage box. “They’re the same product, sir.” “I know. Give me one of those.” “…Are you referring to that storage box?” “Yes. Give me one box of those. And one box of that, too. And that one…” That was the moment Assistant Manager Kim Seonhee’s worries about her sales numbers disappeared.

#### Chapter 94 tail (verified mastered)

…
a Familiar connection. I’ve been increasing it little by little, but it’s hard. If the Link gets forcibly severed, my stomach churns and I feel like I’m going to puke. There’s also a risk of mana backflow. └ Anonymous#9882: So you have to stay within five hundred meters no matter what. └ Author: Yeah. To work safely, maybe three hundred meters? You have to prepare for anything that might happen. Most people probably do the same. I was scrolling through the comments when I suddenly stopped. Had I just stumbled across something important? *The connection to a Familiar breaks beyond five hundred meters?* The maximum distance was that much, and the safe working distance was three hundred meters. In other words, if the author’s comments were true, then the people who had controlled the Familiars yesterday had been somewhere not far from my house. *And they’d be going bald, too. Maybe completely bald.* There was a strong possibility they were wearing wigs, but knowing that couldn’t hurt. I kept searching for information about Familiar magic and managed to put together a few facts. *For a B-rank mage, the maximum Familiar connection distance is five hundred meters. The safe distance is three hundred meters. If a Familiar dies, the Link is forcibly severed, and the caster also takes a slight hit.* And I realized one more thing: why they had gone out of their way to use an expensive Familiar mage to watch me. *What the hell? Tiny Familiars can slip past most detection magic?* It was like this: detection magic was a net, while tiny Familiars like flies and rice weevils were too small to get caught in it. Of course, there were products with built-in top-of-the-line detection magic capable of catching even those. But when I looked them up, they cost five hundred fifty million won—and that was the summer special price. “…” What part of that was supposed to be a summer special? I already had plenty of expenses coming my way. Five hundred million won, my ass. *One more reason to catch them myself.* My thoughts suddenly turned to the other Guild members, too. Had Familiars been attached only to my family? I still didn’t know the exact identity of the person who had commissioned this. Sangdong Guild was only the prime suspect. “That’ll be 8,400 won.” “Ah, yes. Here you go.” I paid the taxi fare and got out. The entrance to the apartment complex, which had always looked exactly the same, seemed a little unfamiliar today. The watcher’s presence bothered me like a thorn caught in my throat. *Should I contact Team Leader Choi?* I was looking at his number saved on my smartphone when— “Oppa!” A familiar swan[^1] in a green tracksuit and round glasses waved at me, her greasy hair tied tightly back. “Oh, y-yeah.” “What’s with that reaction?” “I guess I’d rather not acknowledge knowing you in public. You could say I’m embarrassed…” “You’re embarrassed by your one and only little sister? Huh?” “Go buy some clothes. What are you doing wearing a tracksuit again when you left the clothes you bought at the department store last time at home?” “You should worry about yourself. You’re one to talk, when you go around wearing the same kinds of clothes every day.” Hayeon’s pointed remark left me speechless for a moment. I had paid three hundred million won only an hour or two ago, but I was still wearing nothing but jeans and a T-shirt. Apparently, the old grime of being an ordinary little citizen, caked on over twenty-seven years, had not yet completely washed off. “A-Anyway. Where are you going?” “Where am I going? The convenience store!” Hayeon, who had been sulking until just now, began grinning foolishly. *What’s gotten into her?* I asked in a bemused voice. “Why are you so excited? Is your heart already pounding at the thought of raiding the convenience store?” “Raiding, my ass. I’m going to buy canned tuna.” “Canned tuna? Are we having tuna kimchi stew for lunch today?” “No! We’re not!” “…What’s with you today, seriously? Have you been drinking?” “You’ll be like this, too, when you see this little one.” Despite my reaction, Hayeon only continued to grin strangely, unlike her usual self. Then she lowered the zipper of her tracksuit and pulled something out from inside her clothes. A tiny ball of white-and-yellow fur wriggled in her palm. “Meeoow.” “…A kitten?” “Cute, right? I went out to sort the recycling earlier, and someone had abandoned it in a box. It had been left there for anyone who wanted to raise it.” “…” “I don’t know what kind of bastard abandoned it, but it’s pitiful, isn’t it? What did it ever do wrong? Right, Oppa?” “…Yeah. It’s not the animal’s fault.” “I got Mom’s permission to foster it, even if it’s only for a little while. You’re okay with it, too, right?” “Me?” “Yeah. You know how our Mrs. Kim melts for her eldest son. She told me to get your permission, too, so put in a good word for me when we go inside later.” “We’ll see.” “What? You liked animals when you were little.” I did. I still do, in fact. But this little thing sitting quietly in Hayeon’s palm was… > **System** > > Lv. 2 Cat—Familiar A little different. [^1]: In Korean slang, a “swan” is an unemployed woman.

## Korean source

```text
＃95화



‘후후후. 성공이다.’

홍우진은 득의양양하게 웃었다. 그는 표적 대상의 일거수일투족을 감시하며 모든 정보를 읽어 내는 베테랑이다.

진태경의 여동생이 동물, 그중에서도 특히 고양이에 환장한다는 정보는 특히 유용했다.

“야옹아, 대답해 봐. 집 들어오니까 좋지?”

침투는 자연스러웠고, 성공적이었다. 새끼 고양이의 몸 안에 들어간 홍우진이 기쁨의 포효를 내질렀다.

미야오옹.

“꺄, 귀여워! 오빠, 방금 들었어? 들었어?”

“응. 들었다.”

“이런 귀여운 생물체를 두고 어떻게 그렇게 무심할 수가 있어? 사람이야?”

“그럼 내가 짐승이냐?”

문제는 진태경, 저놈이다.

아무리 감정이 메마른 사람이라고 해도 귀여운 동물, 특히 조그마한 새끼 앞에서는 마음이 말랑말랑해지기 마련인데…….

“옆으로 좀 비켜 봐. TV 화면 가리고 있잖아.”

이놈은 그딴 거 없다. 사하라 사막보다 건조한 감수성에 여동생, 진하연이 구시렁거렸다.

“어휴, 사람이 삭막해도 정도가 있지. 안 그래, 여름아?”

“여름이?”

“응. 여름에 태어났으니까 한여름. 이름 예쁘지?”

“한여름은 무슨. 덩치 보니까 3개월은 되어 보이는데 늦봄에 태어났으니까 늦봄이라고 하든가.”

“……그게 말이야, 방구야? 아무튼 얘 이름은 오늘부터 여름이야. 그치, 여름아?”

야오옹.

홍우진 입장에서는 진하연이 일등 공신이다. 덕분에 일이 술술 풀리고 있었다.

“꺄악! 대답했어! 여름이 방금 언니한테 대답한 거 맞죠? 그렇죠?”

미야옹.

“으헉, 내 심장!”

후후, 다루기 쉬운 녀석 같으니라고. 몇 번 울어 주기만 해도 아주 자지러진다.

‘이래서 여고생들이란…… 아니지, 내 패밀리어 선택이 탁월했던 거지.’

홍우진이 흐뭇하게 웃고 있던 그때.

멀뚱히 TV만 보고 있던 진태경이 한마디를 툭 던졌다.

“걔 수컷 아냐?”

“응? 그거야…….”

“아직 모르지?”

“그러고 보니 확인을 안 했어.”

“까 봐. 확인해 보자.”

어라?

일이 요상하게 돌아간다. 비록 몸은 고양이지만 홍우진은 혈기왕성한 청년. 진태경의 커다란 손이 다가오자 문득 수치심이 몰려왔다.

‘더러운 사내놈이 내 거기를 본다고?’

정확히 말하자면 홍우진의 몸은 아니다. 종(種)이 다른 만큼 신체 구조도 다르다.

그러나 패밀리어 마법은 시전자와 패밀리어가 모든 것을 공유한다. 그렇다 보니 기분이 더러워지는 건 어쩔 수 없었다.

‘절대 안 돼!’

홍우진은 황급히 진하연의 품속으로 파고들었다.

야오오옹.

“어머, 얘가 싫어하는 거 같은데?”

“원래 세상이 그래. 하고 싶은 거만 하면서 사는 사람이 어디 있어?”

“여름이는 고양이잖아.”

“고양이도 마찬가지야. 뜨신 사료에 간식으로 통조림 하나라도 얻어먹으려면 이 정도는 감수해야지.”

저런 미친놈. 고양이 성별 한번 확인해 보겠다고 말도 안 되는 소리를 지껄이네. 홍우진은 이를 갈며 유일한 희망인 진하연에게 매달렸다.

그녀의 팔에 온몸을 비비며 애처로운 눈빛을 발사하자 진하연의 눈동자가 스르륵 풀린다.

“어떡해. 귀여워서 미칠 것 같아.”

“그래, 귀여우니까 한번 까 보자.”

“다음에 해. 애가 무서워하잖아.”

“기분 탓이야.”

“여름이가 오빠 싫어하는 것 같다니까.”

타이밍에 맞춰 신음 한번 흘려 주는 게 포인트다.

끼양. 끼으응.

“봐 봐. 맞지?”

“……그럼 어쩔 수 없지.”

“괜히 애 억지로 만지고 그랬단 봐라. 새끼 고양이들은 예민해서 신경 써 줘야 한단 말이야.”

됐다. 당장 위기는 넘겼다. 진태경 이 녀석, 세상 혼자 사는 또라이 같아도 가족에게는 약한 놈이었다.

이미 상동 길드 측에서 건네준 사전 정보를 모두 숙지한 홍우진은 자신이 한 수 앞을 내다보고 있다고 생각했다.

‘이래서 정보가 중요하지. 넌 나한테 이미 걸려들었어.’

그러나 홍우진이 차마 몰랐던 사실이 있었다.

“동생아.”

“응?”

“용돈 더 안 필요하니?”

“……지금 나를 돈으로 매수해서 우리 여름이를 막, 농락하겠다 이거야?”

“어. 10만 원.”

“콜. 그 대신 너무 싫어하지 않게 살살 해야 돼?”

“내 방 책상에 지갑 있으니까 가져가.”

“꺅!”

미야옹?

총알처럼 사라지는 진하연의 뒷모습에 홍우진은 어이없는 마음을 담아 울음을 토해 냈다.

귀여워서 미칠 것 같다며? 우리 여름이라며?

‘저런 되바라진 것을 봤나.’

언제는 간이고 쓸개고 다 빼 줄 것처럼 굴더니 고작 10만 원에 우리 여름이를 버려?

그러나 자본주의 사회의 현실에 한탄하고 있을 틈 따위는 더 이상 주어지지 않았다.

“자, 이제 나랑 놀자.”

덥석.

번개 같은 속도로 사지를 결박한 진태경의 징글맞은 웃음.

홍우진은 절박한 심정으로 비명을 내질렀다.

‘놔! 놔, 이 새끼야!’

하악! 하아아악!

털을 바짝 세운 하악질 소리에 진태경의 지갑을 뒤지던 유일한 희망이 반응했다.

“오빠!”

“어, 10만 원 더 빼 가라.”

“고마워!”

야, 야!

유일한 희망이 자본주의의 노예로 타락했다!

충격이 채 가시기도 전에 진태경의 뜨거운 숨결이 훅 밀려왔다.

“우리 여름이, 고추 좀 볼까?”

절체절명의 순간.

‘링크(Link) 해제!’

미야오오옹!

구슬픈 울음소리와 함께 새끼 고양이의 몸에서 힘이 쭉 빠져나갔다.

그리고 어두컴컴한 어딘가에서 눈을 뜬 홍우진이 숨을 토해 냈다.

“푸하악!”

헌터 일을 시작하고 크고 작은 백여 건의 의뢰를 처리했지만 지금처럼 생명의 위협을 느낀 적은 처음이다.

소름이 오소소 돋은 팔뚝을 내려다본 그가 헛구역질을 시작했다.

“우욱.”

속이 울렁거리고 머리가 지끈지끈했다.

갑작스러운 링크 해제의 부작용이다. 미리 준비해 놓은 포션을 냉수처럼 들이켜고 나서야 홍우진은 한숨 돌릴 수 있었다.

“진태경, 이 개새끼 진짜…….”

처음으로 의뢰를 받은 게 후회되는 순간이었다.



* * *



[Lv.2 고양이]



“갔네, 갔어.”

나는 혀를 쯧쯧 차며 새끼 고양이를 놔주었다. 3개월이나 됐을까. 손바닥 두 개를 합친 것보다 작은 녀석이 어리둥절한 얼굴로 뒷걸음질 쳤다.

미야옹.

내 방을 나오던 하연이가 그 광경을 발견했다.

“우리 여름이한테 못된 짓 한 거 아니지?”

“그 여름이를 20만 원에 팔아넘긴 게 너고?”

“……흠. 흠.”

“됐다. 어휴, 주워 와도 꼭 저런 걸 주워 와서.”

“뭐래, 얘가 얼마나 귀여운데.”

“그게 아니라…… 아니다. 말을 말자.”

일일이 설명하기에는 길고 복잡한 얘기다. 설명해 줄 생각도 없고.

어떤 음흉한 놈이 고양이 몸 안에 들어가 우리를 관찰하고 있다고 말해 봐라. 얼마나 불안해할지 안 봐도 뻔한데. 지금 벌어지고 있는 일들을 가족들이 알아서는 안 된다.

‘어차피 나도 허락한 일이고.’

패밀리어를 집에 들인 이유는 하연이가 부탁해서, 엄마가 허락해서가 아니다.

‘내가 원해서지.’

누구의 의뢰인지는 몰라도 놈들은 당장 쫓아낸다 해도 계속해서 시도할 것이다.

패밀리어의 형태가 지난번처럼 벌레든, 오늘처럼 고양이든 그건 상관없다.

내가 패밀리어의 정체를 이미 알고 있으며, 언제든지 쳐 낼 수 있다는 사실이 중요하다.

‘분명 이 근방이야.’

집으로부터 최대 500m. 그 안에 패밀리어를 조종하는 마법사가 있다. 그놈을 털면 분명히 연결 고리가 나올 거다.

‘일단 아구창에 주먹 한 대 꽂고 물어봐야지.’

어차피 불법으로 민간인 사찰을 한 놈이니 때려도 신고 못 할 게 뻔하다. 제대로 손봐 줄 생각에 벌써 주먹이 근질거렸다.

‘감히 누구 집에서 깔짝대?’

오랜만의 휴가까지 방해받고 심지어 이 자식들 덕분에 쓴 돈도 3억이 훌쩍 넘어간다. 여러모로 손해 보는 장사가 아닐 수 없다.

잔뜩 구겨진 얼굴로 TV를 보고 있는데, 하연이가 슬금슬금 눈치를 살피며 입을 열었다.

“오빠, 화났어?”

“아니. 화날 게 뭐가 있어.”

“내가 미안해.”

“……왜 이러냐? 무서워지려고 하네.”

농담이 아니라 진짜다. 패밀리어를 처음 발견했을 때보다 더 놀랐다. 얘가 이런 말도 할 줄 알았나?

나는 진지하게 물었다.

“어디 아파?”

“아니 뭐, 그냥.”

“그럼 배고파?”

“그게 아니고…….”

뭔가 말하려던 하연이가 멈칫한 순간, 어디선가 꼬르륵 소리가 들려왔다.

나는 아니고. 엄마는 잠깐 볼일 보러 나가셨고.

“너 배고프지.”

“음, 살짝?”

“그래, 배고파서 헛소리까지 나오는구나. 내 지갑 어디 있는지 알지? 너 먹고 싶은 거 다 시켜.”

“진짜?”

“응. 10만 원 한도 내에서.”

“와, 돈 벌더니 통 커졌네. 우리 오빠.”

살다 살다 우리 오빠 소리도 들어 보는구나. 하연이가 중학생일 때 이후로 처음 듣는 말이라 소름이 돋았다.

“너 패밀리어지, 이 새끼야!”

“무슨 헛소리야. 암튼 그럼 10만 원 선에서 막 시킨다?”

“어, 아니네. 그래. 다 시켜.”

“남은 돈은?”

“……너 나한테 돈 맡겨 놨니?”

“다다익선.”

당당한 하연이의 모습에 기가 찼지만 한편으로는 기뻤다.

지금까지 용돈 달라는 소리 한번 없던 녀석이다. 입고 다니는 옷이나 평소 상태만 봐도 길거리에서 종종 마주치는 또래 애들에 비하면 한참 수수했다.

‘애늙은이 같은 녀석.’

생각해 보면 하연이는 어릴 때부터 그랬다. 쉽게 울지도 않았고 솔직하게 감정을 표현하는 일도 적었다. 지금 같은 성격이 된 것은 오히려 고등학교에 입학한 이후다.

가끔은 어리광을 피워도 될 텐데…… 너무 일찍 철이 들었다.

‘어쩌면 나보다도 훨씬.’

그래서 그런가? 녀석의 행동과 말이 하나도 얄밉지 않다. 오히려 기특하고 기뻤다.

“그래, 다 가져라, 다 가져.”

“진짜?”

“어.”

내 말에 하연이가 방긋 웃었다.

“다행이다. 괜히 미안할 뻔했네.”

“미안할 게 뭐가 있어.”

“아까 오빠 지갑에서 30만 원 빼 갔거든.”

“……어?”

“그런데 오빠가 10만 원 선에서 먹고 남은 거 다 가지라고 하니까 마음이 편해지네.”

“잠깐만, 내가 20만 원 가져가라고 하지 않았냐?”

“우발적 사고였어.”

“……우발적 범죄 아니냐?

아까 했던 말 취소.

콧노래를 부르며 방으로 들어가는 뒷모습이 얄밉기 짝이 없다.



* * *



상동 길드 보안팀장은 눈살을 찌푸렸다.

“고양이 패밀리어?”

“네, 확실합니다.”

단호한 목소리로 대답한 사람은 보안팀 소속이자 길드 유일의 패밀리어 마법사다. 헌터 등급은 C급에 불과하지만 희귀한 정신계 마법사라 보안팀의 핵심 멤버이기도 했다.

“표적의 여동생이 고양이 덕후랍니다. 빈틈을 잘 노렸어요.”

“분위기 파악 안 되냐? 지금 내 앞에서 그 새끼 칭찬이 나와?”

“죄, 죄송합니다.”

“1팀장님이 그러더라. 홍우진이가 전화해서 우리 때문에 바로 들킬 뻔했다고 지랄했대.”

“…….”

“뭐 따지고 보면 그 새끼도 우리 편이긴 하지. 근데 프리랜서한테 밀리면 되겠냐? 길드장님이 각별하게 신경 쓰고 계신 거 몰라?”

이번 일에 투입된 인원은 그를 포함해 총 여섯. 그중 하나는 패밀리어 마법사고 나머지 넷은 추적과 은신에 특화된 근접 헌터들, 마지막으로 팀장 본인은 B급 헌터였다.

“너희가 뭘 착각하나 본데…… 우리 C급 헌터 하나 털어 보자고 온 거 아니다.”

보안팀장은 험악한 얼굴로 팀원들을 응시했다.

이번 건은 길드장이 직접 지시한 일이다. 무조건 지시한 것 그 이상의 성과를 내야만 했다.

“잘하자. 이거 길드장님 직통이야. 너희 여기서 끝날 거야? 보너스도 받고 승진도 해야지.”

팀원들은 말없이 고개를 숙였다.

보너스와 승진이 가장 간절한 사람이 바로 보안팀장이다. 은퇴 시기가 슬슬 다가오는 중년 가장의 히스테리는 이제 와선 하루 이틀 일이 아니었다.

“그리고 너.”

보안팀장이 패밀리어 마법사를 지목했다.

“너도 고양이 해.”

“고양이요? 그건 이미 저쪽에서 했는데.”

“그럼? 괜히 컨트롤도 안 되는 초소형 패밀리어로 발연기 하다가 지난번처럼 뒤질래?”

“…….”

“시키는 대로 해. 여자애가 고양이 덕후라며?”

까면 까야지, 별수 있나. 한바탕 성질을 부린 보안팀장이 나간 뒤 패밀리어 마법사는 곧장 스마트폰을 켜서 검색을 시작했다.

틱. 틱. 틱.

[일산 고양이 분양]

“……이것도 영수증 처리해 주려나?”
```

## Current accepted English baseline

```markdown
# Chapter 95

*Heh heh heh. Success.*

Hong Woojin smiled smugly. He was a veteran at monitoring his targets’ every move and extracting every bit of information from them.

The information that Jin Taekyung’s younger sister was crazy about animals—cats in particular—had been especially useful.

“Meow-meow, answer me. You like being inside the house, don’t you?”

The infiltration had been natural and successful. Inside the kitten’s body, Hong Woojin let out a roar of joy.

“Miaowww.”

“Ahh, so cute! Oppa, did you hear that just now? You heard it, right?”

“Yeah. I heard it.”

“How can you be so indifferent to such a cute little creature? Are you even human?”

“Then what am I, a beast?”

The problem was Jin Taekyung.

Even the most emotionally dried-up person tended to soften in front of a cute animal, especially a tiny one, but…

“Move over a little. You’re blocking the TV.”

This guy had none of that. His sensitivity was drier than the Sahara Desert, and his younger sister, Jin Hayeon, grumbled.

“Good grief, there’s a limit to how bleak a person can be. Right, Yeoreum?”

“Yeoreum?”

“Yeah. Born in summer, so Midsummer. Pretty, right?”

“What do you mean, Midsummer? Judging by the size, the kitten looks about three months old. That would mean it was born in late spring, so call it Late Spring or something.”

“…Is that supposed to be a joke or what? Anyway, this kitten’s name is Yeoreum from today onward. Right, Yeoreum?”

“Mrowww.”

From Hong Woojin’s perspective, Jin Hayeon was his greatest asset. Thanks to her, everything was going smoothly.

“Ahh! Yeoreum answered! You just answered your big sister, didn’t you? Didn’t you?”

“Miaow.”

“Eek, my heart!”

*Heh. What an easy one to handle.* All it took was a few meows, and she practically melted.

*This is why high-school girls are… No, wait. It’s because my choice of Familiar was excellent.*

Hong Woojin was grinning contentedly when—

Jin Taekyung, who had been staring blankly at the TV, casually tossed out a remark.

“Isn’t that one male?”

“Huh? Well, that…”

“We don’t know yet, do we?”

“Come to think of it, I haven’t checked.”

“Let’s take a look. We can find out.”

Huh?

Things were taking a strange turn. His body might have been a cat’s, but Hong Woojin was a vigorous young man. When Jin Taekyung’s large hand approached, a sense of shame suddenly washed over him.

*That filthy bastard is going to look at my junk?*

Strictly speaking, it wasn’t Hong Woojin’s body. Since the species were different, the physical structures were different, too.

However, Familiar magic made the caster and the Familiar share everything. There was no helping the disgust he felt.

*Absolutely not!*

Hong Woojin hurriedly burrowed into Jin Hayeon’s arms.

“Mrowww.”

“Oh my, I don’t think the kitten likes that.”

“That’s how the world works. Who gets to live doing only what they want?”

“But Yeoreum’s a cat.”

“Cats are the same. If you want warm feed and even a can of treats, you have to put up with this much.”

What a lunatic. He was spouting ridiculous nonsense just because he wanted to check a cat’s sex. Grinding his teeth, Hong Woojin clung to his only hope, Jin Hayeon.

He rubbed his entire body against her arm and gave her a pitiful look. Her eyes slowly softened.

“What am I going to do? Yeoreum’s so cute I could die.”

“Yeah, very cute. So let’s take a look.”

“Do it next time. You’re scaring the kitten.”

“That’s just your imagination.”

“I told you, Yeoreum doesn’t like you, Oppa.”

The key was to let out a groan at exactly the right moment.

“Mnyaa. Mngh.”

“See? I’m right, aren’t I?”

“…Then I can’t help it.”

“Don’t you dare force the kitten to let you handle it. Kittens are sensitive, so you have to be careful with them.”

Good. He had gotten past the immediate crisis. Jin Taekyung seemed like a lunatic who lived in his own world, but he was weak when it came to his family.

Having fully absorbed all the background information Sangdong Guild had given him, Hong Woojin thought he was one step ahead.

*This is why information matters. You’ve already fallen right into my trap.*

But there was one fact Hong Woojin had never imagined.

“Hey, Sis.”

“Yeah?”

“Do you need more spending money?”

“…Are you trying to bribe me so you can mess with our Yeoreum?”

“Yeah. A hundred thousand won.”

“Deal. But you have to be gentle so she doesn’t hate you too much, okay?”

“My wallet’s on the desk in my room. Go get it.”

“Eek!”

“Miaow?”

Jin Hayeon disappeared like a bullet. Hong Woojin let out a cry filled with disbelief.

*You said she was so cute you could die. You called her our Yeoreum!*

*What a shameless little brat.*

One minute she had acted ready to give Yeoreum anything, and now she was abandoning “our Yeoreum” for a mere hundred thousand won?

But he was given no time to lament the realities of a capitalist society.

“Come on. Let’s play.”

He grabbed him.

Jin Taekyung restrained all four of his limbs with lightning speed and smiled horribly.

Hong Woojin screamed desperately.

*Let go! Let go, you son of a bitch!*

“Hiss! Hissss!”

The kitten’s fur stood on end as Hong Woojin hissed, catching the attention of his only hope as she rummaged through Jin Taekyung’s wallet.

“Oppa!”

“Yeah, take another hundred thousand won.”

“Thanks!”

*Hey! Hey!*

His only hope had become a slave to capitalism!

Before the shock had even worn off, Jin Taekyung’s hot breath swept over him.

“Our Yeoreum, shall we take a look at your little peepee?”

At that desperate, life-or-death moment—

*Sever Link!*

“Miaowww!”

With a sorrowful cry, all the strength drained out of the kitten’s body.

Then Hong Woojin opened his eyes somewhere dark and let out a breath.

“Puhack!”

Since starting work as a Hunter, he had handled more than a hundred large and small assignments, but this was the first time he had ever felt his life was in danger.

He looked down at his forearms, which were covered in goose bumps, and began to gag.

“Urgh.”

His stomach churned, and his head throbbed.

It was a side effect of the sudden Link severance. Only after he gulped down the potion he had prepared in advance like cold water could Hong Woojin finally catch his breath.

“Jin Taekyung, you fucking bastard…”

It was the moment he first regretted ever accepting the assignment.

* * *

> **System**
>
> **Lv. 2 Cat**

“There he goes.”

Clicking my tongue, I let the kitten go. Was it three months old? The little thing, smaller than my two joined palms, backed away with a bewildered expression.

“Miaow.”

Hayeon was leaving my room when she spotted what had happened.

“You didn’t do anything mean to our Yeoreum, did you?”

“And you’re the one who sold Yeoreum for 200,000 won?”

“…Ahem. Ahem.”

“Whatever. Good grief. Whenever you pick something up, it has to be something like that.”

“What are you talking about? Look how cute Yeoreum is.”

“That’s not what I meant… Never mind. Forget it.”

It was a long and complicated story to explain one detail at a time. Besides, I had no intention of explaining it.

If I told her that some sinister bastard had entered the body of a cat and was watching us, it was obvious how anxious she would become. My family couldn’t find out about what was happening.

*Besides, I was the one who had allowed it.*

The reason I had let a Familiar into the house wasn’t because Hayeon had asked or because Mom had given her permission.

*It was because I wanted it.*

I didn’t know who had hired them, but even if I drove them off now, they would keep trying.

It didn’t matter whether the Familiar took the form of an insect like last time or a cat like today.

What mattered was that I already knew what the Familiar was and could swat it away whenever I wanted.

*They’re definitely somewhere around here.*

Within 500 meters of the house. Somewhere inside that radius was a mage controlling the Familiar. If I roughed him up, I was sure I’d find the connection.

*First, I’ll punch him in the mouth, then ask some questions.*

He had illegally surveilled a civilian, so there was no way he could report me even if I beat him. Just thinking about teaching him a proper lesson made my fists itch.

*How dare they snoop around someone’s house?*

They had interrupted my first vacation in a long time, and thanks to these bastards, I had already spent well over 300 million won. In every respect, this was a losing proposition.

I was watching TV with my face twisted into a scowl when Hayeon cautiously watched my reaction and spoke.

“Oppa, are you mad?”

“No. What is there to be mad about?”

“I’m sorry.”

“…What’s gotten into you? You’re starting to scare me.”

I wasn’t joking. I was more startled than when I had first discovered the Familiar. Since when could she say something like that?

I asked seriously.

“Are you sick?”

“No, it’s just…”

“Then are you hungry?”

“That’s not it…”

Just as Hayeon hesitated, apparently about to say something, a stomach growled from somewhere.

It wasn’t mine. Mom had stepped out to run an errand.

“You’re hungry.”

“Mm, a little?”

“Right. You’re so hungry you’re starting to spout nonsense. You know where my wallet is, right? Order anything you want to eat.”

“Really?”

“Yeah. Up to 100,000 won.”

“Wow, now that you’re making money, you’ve gotten generous, Oppa.”

In all my life, I never thought I’d hear her call me “our Oppa.” It was the first time I’d heard it since Hayeon had been in middle school, and it gave me goose bumps.

“You’re the Familiar, you little bastard!”

“What are you talking about? Anyway, can I order whatever I want as long as it’s under 100,000 won?”

“Yeah. No, wait. Fine. Order everything you want.”

“What about the money left over?”

“…Did you leave your money with me?”

“More is better.”

I was dumbfounded by Hayeon’s shamelessness, but at the same time, I was happy.

She had never once asked me for spending money. Even judging by the clothes she wore and her usual appearance, she was far more modest than the kids her age I occasionally saw on the street.

*What an old soul.*

Come to think of it, Hayeon had been like that since she was little. She rarely cried, and she didn’t often express her feelings honestly. Her current personality had only developed after she entered high school.

*She ought to be allowed to act spoiled once in a while… She grew up too soon.*

*Maybe even much sooner than I did.*

Maybe that was why. None of her actions or words annoyed me in the slightest. If anything, I found her admirable, and I was happy.

“Fine. Take it all. Take everything.”

“Really?”

“Yeah.”

Hayeon beamed at my words.

“That’s a relief. I almost felt bad for nothing.”

“What’s there to feel bad about?”

“I took 300,000 won from your wallet earlier.”

“…Huh?”

“But when you said I could have whatever was left after eating within the 100,000-won limit, I felt better.”

“Hold on. Didn’t I tell you to take 200,000 won?”

“It was an accident.”

“…Don’t you mean a crime of opportunity?”

I take back what I said earlier.

The sight of her back as she hummed her way into her room couldn’t have been more irritating.

* * *

The head of Sangdong Guild’s Security Team frowned.

“A Cat Familiar?”

“Yes, I’m certain.”

The person who answered in a firm voice was a member of the Security Team and the Guild’s only Familiar mage. He was only a C-rank Hunter, but he was also a core member of the Security Team because mental mages were rare.

“The target’s younger sister is a cat fanatic. Hong Woojin took advantage of that opening perfectly.”

“Can’t you read the room? You’re praising that bastard in front of me?”

“I-I’m sorry.”

“Team 1 Leader said Hong Woojin called and went ballistic, saying he nearly got exposed because of us.”

“…”

“Come to think of it, that bastard is technically on our side, too. But can we afford to be outdone by a freelancer? Don’t you know the Guild Master is taking a special interest in this?”

Six people had been assigned to this operation, including the Security Team Leader. One was the Familiar mage, four were close-combat Hunters specializing in tracking and stealth, and the Team Leader himself was a B-rank Hunter.

“I think you’re under a misconception… We didn’t come here just to dig up dirt on one C-rank Hunter.”

The Security Team Leader glared at his team with a menacing expression.

The Guild Master had personally ordered this operation. They had to produce results that went beyond the direct order, no matter what.

“Let’s do this properly. This came straight from the Guild Master. Are you going to let your careers end here? You want bonuses and promotions, don’t you?”

The team members silently lowered their heads.

The person most desperate for a bonus and promotion was the Security Team Leader himself. The hysteria of a middle-aged family man whose retirement was slowly approaching was nothing new by this point.

“And you.”

The Security Team Leader pointed at the Familiar mage.

“You do the cat, too.”

“The cat? They already did that over there.”

“What, then? Are you going to put on another pathetic performance with a tiny Familiar you can’t even control and die like last time?”

“…”

“Do as you’re told. The girl’s a cat fanatic, isn’t she?”

If they wanted a cat, he had to use a cat. What else could he do?

After the Security Team Leader stormed out, the Familiar mage immediately turned on his smartphone and began searching.

Tap. Tap. Tap.

> **Ilsan Cat Adoption**

“…Do you think this will count as a business expense?”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 95`.

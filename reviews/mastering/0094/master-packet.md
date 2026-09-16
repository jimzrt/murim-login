# Master Edit Task — Chapter 94

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

| 시스템              | **System**                     |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 85–89

## Plot

In the Boss Zone of The Minotaur’s Labyrinth, Im Changsoo plans to exploit Taekyung’s apparent interest in Song Song and use the Level 70 Minotaur Warrior to humiliate him. Taekyung instead kills the boss with a single spear technique, completes the B-rank Gate Clear Quest, and receives a Level Up and its undisclosed reward. Song Song declines his attempts to invite her to dinner.

After the raid, Changsoo transfers the wagered four billion won to Taekyung. His father, Im Chunsoo—the A-rank Guild Master of Sangdong Guild, known as Frozen—learns that Changsoo transferred eight billion won in total, fires him, and begins beating him with an ice club.

Taekyung visits his sick sister Hayeon and discovers that their mother, Kim Jeonghee, has been secretly working in a restaurant. When the restaurant owner insults Jeonghee and attacks Taekyung, he reveals his C-rank Hunter status and has Changsoo confirm both his identity and payment. Jeonghee quits and leaves with him.

At home, Taekyung uses Circulate Qi for Healing on Hayeon and Jeonghee, curing Hayeon’s fever and headache and greatly improving his mother’s condition. He gives each of them a Lesser Potion from his reality Inventory. After learning that Taekyung earned four billion won, Hayeon asks whether she can drop out of school.

## Continuity

- Taekyung killed the Level 70 Minotaur Warrior in one blow, completed the B-rank Gate Clear Quest, leveled up, and received its reward in his reality Inventory.
- Im Changsoo paid Taekyung the promised four billion won.
- Im Chunsoo is Sangdong Guild’s founder and A-rank Guild Master, known as Frozen and for his exceptional ice magic. He fired Changsoo and violently confronted him after discovering Changsoo’s eight-billion-won transfer.
- Kim Jeonghee quit her restaurant job after the owner insulted and attacked Taekyung.
- Kim Minsu is the owner’s son, a D-rank Hunter in Sangdong Guild, but Changsoo does not know him personally.
- Taekyung can safely use the Jin Family’s Cultivation Technique to perform Circulate Qi for Healing on others.
- Hayeon and Jeonghee recovered substantially after receiving the treatment; Taekyung also gave each a Lesser Potion.
- Taekyung’s reality and Murim Inventories remain separate.
- Hayeon has asked about dropping out of school, but no decision has been made.
- Retaliation by Im Chunsoo or Sangdong Guild, Jeonghee’s next circumstances, and Hayeon’s schooling remain unresolved.

## Translation Decisions

- Render 일섬 as **One Annihilation** and 미노타우로스 대전사 as **Minotaur Warrior**.
- Render 관심법 as **mind-reading technique** and preserve the **barbarian against barbarian** wording for 이이제이.
- Retain **Frozen**, **C-rank**, **D-rank**, **Circulate Qi for Healing**, **Lesser Potion**, and **Third Rate**.
- Retain **ajumma** and **goshiwon** with their established explanatory footnotes.
- Use **Minsu** as Kim Minsu’s short form.
- Preserve the established family addresses **Mom** and **Son**.

### Prior accepted reading-copy tails

#### Chapter 92 tail (verified mastered)

…
after leaving the Guild Master’s office, the Team 1 Leader could not shake his unease. * * * Home. Vacation. Just thinking about those two words made me happy. The reality was every bit as wonderful. Except… Bzzzz. Bzzzzzz. “Ah, this is driving me crazy.” I swatted a fly with lightning speed. Not with an ordinary palm, either, but one charged with internal energy. I tossed the fly, dead in one strike, into the trash and returned to the sofa. “Why the hell are there so many fucking flies?” Hayeon, who had briefly come out into the living room to get a drink of water, let out a deep sigh. “It’s summer, you idiot, Oppa.” “I’m telling you, this is more than that.” “How many could there possibly be? There was only one just now.” “That’s the problem. They keep coming in one at a time. Every time I kill one, another shows up from somewhere.” “How many have you killed?” “I swear to heaven, I’ve killed at least a hundred since this morning.” “Look at you exaggerating. This is why men are…” “I’m serious!” “Okay, okay.” Wow. This was driving me insane. I tore at my hair and swatted another fly. A hundred? That was no exaggeration. What the hell was wrong with this neighborhood that one house could be overrun with so many flies? *Did someone smear honey on the windows?* At first, they had merely been annoying. Like Hayeon said, I assumed they were only around because it was summer. But the more time passed, the more I realized that something was strange. *It was after I’d killed about thirty of them.* These damn things kept coming in without a break! I would kill one, then another would come in. I would kill that one, and a different fly would take its place. Even after I closed every window and searched the whole house with Qi Sense, the nightmare of the fly army continued. Bzzzzzz. “See? Another one came in before we could even turn around. Where the hell are these things coming from?” I carefully searched for some tiny gap I had failed to notice, but I could not figure it out. They seemed to be coming through spaces barely large enough for a single ant to pass through. “Stop swatting them and leave them alone. Then they’ll quiet down.” “What kind of creative bullshit is that? You think they’ll sit still just because you leave them alone? We obviously won’t be able to sleep with them buzzing all night.” “The flies in my room stay still.” “What?” “There are about three in my room, too. They bothered me at first, so I thought about killing them, but when I left them alone, they stopped flying around and just sat on my desk.” “That’s only temporary. They probably fly around like crazy when you’re not looking.” “I think they’re just lazy flies. They haven’t moved even once.” “Say something that makes sense.” “I’m serious. Want to bet a hundred thousand won?” “You even have a hundred thousand won? You’re supposed to be studying for exams.” “Of course I do. It’s the money you gave me last time.” “You’re going to bet against me with the allowance I gave you?” “If you’re scared, you can just die.” “…Deal.” Shit. So this was how money went around in circles. We went straight to Hayeon’s room. She pointed at a fly sitting quietly on her desk and grinned triumphantly. “See? I was right, wasn’t I? Hurry up and hand over the hundred thousand won.” “Hand over what? We need to run an experiment first.” I brought my palm down over the fly. I struck at an ordinary person’s speed, slow enough for the fly to dodge easily. But then… Flinch. Scramble. The fly jumped in alarm and scurried away as fast as its legs could carry it. I was dumbfounded. Hayeon looked just as baffled. “Sis.” “Y-Yeah?” “Are all flies these days like that?” “M-Maybe they do? Anyway, give me the hundred thousand won.” “I’ll give it to you. I will. But isn’t that fly strange?” “A fly is a fly. That one’s just a little strange.” “What kind of fly acts like that? I’ve seen goblins and Minotaurs in my life, but I’ve never seen a fly that flies around so little.” The instant I finished speaking— Bzzzzzz— “……” “……” Suspicious. Way too suspicious. The timing was questionable enough, but the way its wings moved—as if it were trying hard to look ordinary—was even stranger. Even its flight was awkward and unsteady. *Never mind that. It gives me the creeps. This feeling is weirdly familiar.* Where had I felt something like this before? Oh, right. That alley I had walked through two days ago, on my way home from viewing the house. That strange sense of déjà vu, as though someone were watching me. *Am I really just being oversensitive?* I glared at the fly and raised my Qi Sense. Its activation range now extended to a radius of seventy meters, spreading into every corner of the house. And then something no one could have expected happened. Ding. Ding. Ding. > **System** > > Lv. 1 Housefly—Familiar > > Lv. 1 Black Blow Fly—Familiar > > Lv. 1 Green Bottle Fly—Familiar “…?” *What the hell is this?* [^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.

#### Chapter 93 tail (verified mastered)

…
a Store filled with all kinds of goods ordinary people could never access. “…Hey, hey. Let’s go.” Only after the kids loitering out front had left did the guard notice me. He addressed me politely. “What brings you here?” “I’d like to purchase something.” “Please present your membership card or Hunter certification.” “Here.” “I’ll need to complete the verification process.” Only after my certification had been checked and my fingerprints scanned was I given an admission pass. “As a C-rank Hunter, you may access up to the third floor.” The Store stocked different items on each floor. I had visited once when I was an F-rank Hunter, but the second floor had been the highest I could access at the time. I had never even gotten to look around above it. “Have a pleasant time.” “Thanks. Take care.” Once I passed through the doors, I saw endless rows of glass display cases. The space was incomparably larger than an ordinary shop, yet there were only a handful of customers in sight. *Well, it would be strange if this place were crowded.* Only a tiny minority could shop here: Hunters, who made up just 0.1 percent of Korea’s population, and civilians with enough social influence to be issued membership cards. They were the Store’s main customers. “This item was manufactured by domestic S Company and has a built-in alarm spell, making it useful for security…” “This brooch was made by overseas M Company. With its beautiful, tasteful design and built-in shield spell, it’s perfect for your wife’s personal protection…” The employees were busy explaining their products to customers. That was right. The Store was a kind of luxury department store where people could buy expensive magical goods that were difficult to obtain through ordinary channels. “Then I’ll take that one and this one. Bring me that, too.” “Don’t you have anything with better performance? Don’t worry about the price. Bring me some options.” There might not have been many customers, but their purchasing power was unmatched. I was staring blankly at people buying goods that cost at least several million won when a pretty female employee approached and bowed. “Hello. I’m Assistant Manager Kim Seonhee from the Ilsan Store. I’ll be assisting you today.” “Ah, yes.” They had treated me politely the last time I visited, too, but not to this extent. Now that I was a C-rank Hunter, the customer service was considerably more attentive. “Is there a particular product you’re looking for?” “I’d like to buy some raid equipment.” The employee’s expression brightened. The Store carried countless magical goods, but Hunter equipment was among the most expensive of them all. And I was a C-rank Hunter. Even a mid-level Hunter could spend hundreds of millions of won on a single piece of equipment. Naturally, a sales employee would be delighted at the thought of adding that kind of sale to her record. “I’ll show you to the third floor.” As she turned toward the escalators, I spoke. “No, please take me to the second floor.” “Pardon? But to purchase C-rank Hunter equipment, you’ll need to go to the third floor…” “It’s fine. I’m looking for weapons for low-rank Hunters.” I pretended not to notice her expression darkening and stepped onto the escalator first. *I wonder if they have anything useful for killing rats.* The time had come to fill my Inventory. * * * “It’s fine. I’m looking for weapons for low-rank Hunters.” Assistant Manager Kim Seonhee secretly sighed at the customer’s words. As someone unusually concerned about her sales numbers, this was far from welcome news. *I need a good sales record this month if I want to get promoted.* The colleague who had joined the company at the same time as her and worked at the Seoul branch was already a Team Leader. Whether it was luck or business savvy, every customer she encountered was apparently a big spender. Compared to her… “This one looks good.” “Ah, yes. This product was manufactured using an F-rank Magic Gem…” Kim Seonhee quickly pulled herself together and began her explanation. The customer had picked up a dagger with a black-painted blade. Compared to the other weapons, it was nothing special. It did not even have magic embedded in it. It was just an ordinary consumable. “How much is it?” “It’s currently on sale as part of our summer promotion, so we’re offering it at the low price of 520,000 won.” “Hmm. That’s expensive.” “…” How much did a C-rank Hunter make a year again? Didn’t their basic allowances alone amount to several hundred million won? Kim Seonhee found it ridiculous, but silently waited for the customer to make his choice. “Ah, well, I guess it can’t be helped. I’ll buy it. Give me one.” “…Yes.” The look on his face, as if parting with the money were killing him, was utterly obnoxious. Kim Seonhee swallowed a curse as she picked up the dagger when— “No. Not that one.” “Excuse me?” “The one next to it.” Her gaze shifted to the side. One hundred daggers were neatly arranged inside a storage box. “They’re the same product, sir.” “I know. Give me one of those.” “…Are you referring to that storage box?” “Yes. Give me one box of those. And one box of that, too. And that one…” That was the moment Assistant Manager Kim Seonhee’s worries about her sales numbers disappeared.

## Korean source

```text
＃94화



“3억 5천만 원입니다.”

계산하는 직원의 목소리도 떨리고, 카드를 건네는 내 손도 떨린다.

세상에, 3억 5천만 원이라니. 개처럼 일하던 시절의 3년 치 연봉을 불과 한 시간 만에 다 써 버렸다.

‘아냐. 좋게 생각하자.’

감시자들로부터 가족을 지키기 위해 쓰는 돈이다.

어차피 돈은 앞으로 계속 벌면 되고, 오늘 산 물건들은 두고두고 쓸 수 있다.

삑.

- 승인이 완료되었습니다.

“결제 완료했습니다.”

덕분에 이 아가씨만 로또 맞았군. 입이 귀에 걸린 김희선 대리에게 카드를 돌려받았다.

“그럼 끝난 거죠?”

“아, 주소를 알려 주시면 저희가 배송해 드립니다.”

“괜찮아요. 바로 가 볼 데가 있어서.”

배송은 무슨. 사람들의 시선에서 벗어나는 즉시 인벤토리에 보관하면 끝이다.

‘시스템이 이럴 때 편리하단 말이야.’

그런 생각을 하며 쇼핑백을 양손 가득 받아 들었다. 물론 그냥 종이 쇼핑백이 아니다. 오우거 가죽으로 만들었다는 질기고 튼튼한 가죽 쇼핑백이다. 사은품으로 받은 건데 기쁘기는커녕 속이 쓰리다.

“그럼 수고하세요.”

“다음에 꼭! 다시 찾아 주십시오.”

“……아, 네.”

허리를 직각으로 푹 숙이며 내미는 그녀의 명함을 건네받았다.

실적에 미친 자, 그의 이름은 판매 사원.



* * *



근처 화장실에 들러 스토어에서 산 물건들을 인벤토리에 수납한 뒤 택시를 잡았다. 운전면허를 못 딴 게 후회되는 요즘이다.

“일산 A아파트로 가 주세요.”

조수석에 앉자마자 스마트폰을 꺼내 정보를 검색했다.

검색어는…….

‘패밀리어.’

검색 버튼을 누르기가 무섭게 관련 정보가 촤르륵 떴다.

일반인들은 보지 못하는, 헌터 인증을 해야만 열람 가능한 정보도 상당수였는데, 그중 제법 시선을 끄는 제목이 하나 있었다.



유머X 패밀리어 마법 쓰지 마라. 탈모 왔다.



그야말로 영혼을 울리는 제목이다. 클릭 안 할 수가 없지.

‘아, 여기 올라온 글이었네.’

글이 게시된 사이트는 유명한 국내 헌터 커뮤니티였다.

해당 게시글은 월간 베스트에 조회수가 10만, 댓글이 2천 개가 넘어가는 위엄을 보였다.

‘어디 한 번 읽어 볼까.’

클릭!



유머X 패밀리어 마법 쓰지 마라. 탈모 왔다.



현직 B급 마법사다.

나름 짬밥 좀 먹었고 프리랜서 헌터로 짭짤하게 돈 벌고 있다. 정확한 스펙을 밝히지 못하는 건 양해 바람.

아무튼 이 글을 쓰게 된 이유는 제목 그대로다.

나 패밀리어 마법 때문에 탈모빔 맞았다…….

아직 20대인데 정수리는 2천 년 된 미라랑 동기 동창이다, 시발 거.

태클 거는 새끼들 있을까 봐 미리 말해 두는데 우리 집안은 대대로 풍성충이다. 일제 강점기 때 찍은 증조할아버지 사진도 봤는데 조선의 라푼젤임.

각설하고, 패밀리어 마법. 이거 진짜 양날의 검이다.

나처럼 법사 하는 애들은 알 건데 정신계 마법이 흔한 게 아니거든. 민간인들도 기술 하나 배우면 먹고는 살잖아.

법사한테는 정신계가 딱 그래. 이거 하나 있으면 어떻게든 잘 먹고 잘 산다.

근데 시발, 머리가 빠져. 계속 빠져.

여기 상급 포션으로 머리 감아 본 놈 있냐? 난 해 봤다.

머리 한 번 감는데 몇천만 원을 썼다고 미친 놈들아. 그 정도로 별 지랄을 다 해 봤는데 그것도 잠깐이야.

하다 하다 안 돼서 민간 의사 찾아갔더니 이 새끼가 한숨 푹 내쉬면서 그러더라.

정신계 마법사시죠?

진짜 토씨 한 글자 안 틀리고 저랬음. 깜짝 놀라서 어떻게 알았냐고 물었더니 리얼 소름 돋는 얘기 해 주더라.

정신계 법사 중 90퍼 이상이 탈모고, 특히 그중에서도 난이도가 있는 패밀리어 마법 쓰는 놈들은 100퍼센트래.

머리를 존나 혹사시키니까 어느 순간부터 풍성충도 탈모충이 된다는 거지.

처음에는 무슨 헛소리를 하는 거지 싶었는데 알아보니까 사실이더라고.

부랴부랴 정신계 법사 카페 가입해서 나 같은 놈 있는지 찾아봤는데 뭔 카페 회원 100명 중에 98명이 탈모야.

내 상황 듣더니 이미 늦었다고, 포션 그거 일시적으로 세포 회복시켜 주는 거라 자주 쓰면 모발 세포만 죽는대.

카페 게시판에 진료 후기 써 주면 등업 시켜 준다는 거 쌩 까고 탈퇴 후 나만의 치료법을 찾고 있다…….

세줄 요약.

1. 정신계 마법사 좋다. 근데 그 대신 머리 빠짐.

2. 포션 써 봤자 헛수고다. 차라리 탈모 방지 샴푸에 민간 병원을 가라. 모발은 마음과 간절함으로 치료해야지, 마법으로 치료하려고 하면 안 됨.

3. 난 포기하지 않는다.

그럼 이만.



“…….”

다 읽고 나니 눈앞이 뿌옇게 흐려진다. 항상 부러워했던 마법사들, 다 가졌을 것 같던 그들에게도 이런 고충이 있었다니.

“손님, 괜찮으세요?”

“전 괜찮…… 으흡.”

“왜 그러세요?”

“아, 아닙니다. 괜찮아요.”

이 상황에 하필이면 택시 아저씨도 대머리다. 나는 죄인의 심정으로 스마트폰을 향해 고개를 떨궜다.

게시글 아래 2천 개가 넘어가는 댓글이 보인다.



익명#232 : 한 줄 요약해 주라.

└ 작성자 : [심한 욕설로 블라인드 처리된 댓글입니다.]



익명#112 : 첫 댓글 사람 새끼 맞냐? 난 울었다. 응원할게 힘내.

└ 작성자 : 고맙다...



익명#1512 : 다른 건 모르겠고 두 번째 댓글도 탈모인인 듯. 근데 쭉 읽어 보니까 돈 많이 버는 것 같던데 모발 좀 없어도 되지 않냐. 가발 좋은 거 쓰면 되잖아.

└ 작성자 : [심한 욕설로 블라인드 처리된 댓글입니다.]



익명#4885 : 와, 패밀리어 법사를 여기서 보네. 너희가 몰라서 그렇지 작성자 리얼 귀족임. 같은 B급이어도 수입 면으로는 비교가 안 된다. 대우도 그렇고.

└ 작성자 : 돈 많으면 뭐 하냐. 머리가 없는데.

└ 익명#4885 : 생각해 보니까 그러네.

└ 작성자 : 위로해 줄 거면 끝까지 해, 이 새끼야.

.

.

.

운영자 : 축하드립니다! 인기 게시글로 선정되셨습니다!

└ 익명#5252 : ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

└ 익명#8984 : ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

└ 작성자 : 이걸 웃어야 되냐 말아야 되냐.

└ 익명#2652 : 지금 모발이 없는데 웃음이 나와?

└ 작성자 : [심한 욕설로 블라인드 처리 된 댓글입니다.]



작성자 : 열화와 같은 성원 고맙다. 월간 베스트 찍고 명예의 전당 가게 생겼네. 혹시 궁금한 점 있으면 아래로 댓글 달아라. 지금 일 중이긴 한데 틈틈이 들어와서 대답해 줌.

└ 익명#9665 : 프리랜서라고 했는데 주로 어떤 일 함?

└ 작성자 : 말이 좋아서 프리랜서지 하는 일은 흥신소랑 비슷해. 일급 범죄자(물론 헌터) 추적도 해 봤고 졸부 집 불륜 사건도 맡아 봤다.

└ 익명#915 : 오... 많이 벌겠네. 수입 얼마나 되냐.

└ 작성자 : 그거야 어떤 의뢰냐에 따라 다르지. 그래도 몇 년 일해서 서울에 건물 하나 올렸다. 지금 사는 집도 내 명의로 된 거고.

└ 익명#5252 : 집 인증해 봐.

└ 작성자 : 일 중이라 밖에 나와 있어. 나중에 제대로 인증할 테니까 그때 봐라.

└ 익명#9882 : 일 중인 거랑 뭔 상관이냐. 패밀리어 어차피 원격 조종 아님?

└ 작성자 : 아무리 원격 조종이어도 거리 제한이 있지 병신아. 넌 미국 여행 가서도 너희 집 와이파이 쓰냐?

└ 익명#9882 : ㅈㅅ

└ 작성자 : 패밀리어 연결 거리는 최대 500미터가 한계야. 조금씩 거리 늘리고는 있는데 힘들더라. 강제로 링크 해제되면 속 울렁거리고 토할 것 같음. 마나 역류 위험도 있고.

└ 익명#9882 : 그럼 500미터 안에는 무조건 있어야겠네.

└ 작성자 : ㅇㅇ 안전하게 작업하려면 한 300미터? 혹시 모를 사태를 대비해야 되니까. 아마 대부분이 그럴 거야.



댓글들을 쭉 읽어 내리다가 멈칫했다.

지금 뜻하지 않게 중요한 정보를 발견한 것 같은데?

‘500m를 벗어나면 패밀리어와의 연결이 끊긴다고?’

최대 거리가 그 정도고 안전한 작업을 위해서는 300m라니.

즉, 작성자의 댓글이 사실이라면 어제 패밀리어를 부린 놈들은 우리 집에서 얼마 떨어지지 않은 곳에 있었다는 뜻이다.

‘그리고 머리가 벗겨져 있겠지. 완전히 대머리거나.’

가발을 쓰고 있을 가능성이 농후하지만 알고 있어서 나쁠 건 없다.

나는 그 후로도 계속 패밀리어 마법에 관한 정보를 검색했고, 몇 가지 사실을 정리할 수 있었다.

‘B급 마법사 기준 패밀리어 연결 거리는 최대 500m. 안전 거리 300m. 패밀리어가 죽을 경우 강제로 링크가 해제되며 시전자도 약간의 타격을 입는다.’

그리고 하나 더, 왜 굳이 몸값 비싼 패밀리어 마법사로 나를 감시하는지도 깨달았다.

‘뭐야, 이거. 초소형 패밀리어는 어지간한 탐지 마법에도 안 걸린다고?’

예를 들자면 그런 거다. 탐지 마법은 그물이고, 파리나 쌀벌레 같은 소형 패밀리어는 그물에 걸리지 않을 만큼 작으니 걸릴 리가 없다.

물론 그것까지 잡아내는 최상급 탐지 마법이 내장된 제품도 있긴 한데 찾아보니 여름 특가로 5억 5천이란다.

“…….”

도대체 어느 부분에서 여름 특가인지 모르겠다. 가뜩이나 앞으로 돈 나갈 구석도 많은데 5억은 얼어 죽을.

‘직접 잡아야 할 이유가 하나 더 늘었군.’

문득 다른 길드원들에게도 생각이 미쳤다. 과연 패밀리어가 우리 가족에게만 붙었을까?

사주한 범인의 정확한 정체도 아직 모른다. 상동 길드는 유력한 용의자일 뿐이다.

“8천 4백 원이요.”

“아, 네. 여기요.”

택시비를 지불하고 차에서 내렸다. 항상 똑같았던 아파트 단지 입구가 오늘은 좀 낯설다.

목구멍에 걸린 가시처럼, 감시자의 존재가 거슬렸다.

‘최 팀장한테 연락을 해 봐야 되나.’

스마트폰에 저장된 그의 번호를 보며 고민하던 그때였다.

“오빠!”

낯익은 초록색 추리닝에 동그란 안경. 떡 진 머리를 뒤로 질끈 묶은 백조 한 마리가 날 보며 손을 흔든다.

“어, 으응.”

“뭐야, 그 반응은?”

“왠지 밖에서는 알은척하고 싶지 않다고 해야 할까. 부끄럽다고나 할까…….”

“하나뿐인 여동생이 부끄러워? 어?”

“옷이나 사 입어라. 지난번에 백화점에서 산 옷은 놔뒀다 뭐 하고 또 추리닝이야?”

“오빠나 잘해. 맨날 비슷한 옷만 입고 다니는 주제에.”

하연이의 일침에 순간 할 말을 잃었다. 불과 한두 시간 전에 3억을 결제했는데 입고 있는 옷은 아직도 청바지와 티셔츠뿐이다. 27년 동안 박혀 있던 소시민의 묵은 때가 덜 벗겨진 모양이다.

“아, 아무튼. 어디 가는 길이야?”

“어디 가냐고? 편의점!”

방금까지만 하더라도 뚱해 있던 하연이가 이번엔 실실 웃기 시작한다.

얘가 왜 이래? 난 떨떠름한 목소리로 물었다.

“왜 이렇게 신났냐? 편의점 털어 올 생각에 벌써부터 가슴이 두근거려?”

“털어 오긴 무슨. 참치 통조림 사 올 건데.”

“참치 통조림? 오늘 점심 참치 김치찌개야?”

“아니! 아닌데!”

“……오늘 왜 이래, 진짜? 술 마셨어?”

“오빠도 얘 보면 그렇게 될걸.”

내 반응에도 평소와 달리 히죽거리기만 하던 하연이가 추리닝 지퍼를 내리고 품 안에서 뭔가를 꺼내 들었다. 하얗고 노란, 조그마한 털 뭉치 하나가 손바닥 안에서 꼬물거린다.

야오옹.

“……새끼 고양이?”

“귀엽지? 아까 분리수거 하러 갔는데 누가 박스에 버려 놨더라고. 기르고 싶은 사람 기르라고.”

“…….”

“어떤 놈이 버렸는지 몰라도 불쌍하잖아. 얘는 뭔 죄야? 안 그래, 오빠?”

“……그래. 동물이 무슨 죄냐.”

“엄마한테 허락받아서 잠깐이라도 임시 보호 하기로 했어. 오빠도 괜찮지?”

“나?”

“응, 우리 김 여사가 장남한테 껌뻑 죽잖아. 오빠 허락도 받으라는데 이따 들어가서 말 좀 잘 해 주라.”

“글쎄.”

“뭐야. 어릴 땐 동물 좋아했잖아.”

좋아했지. 아니, 지금도 좋아한다. 하지만 하연이의 손바닥에 얌전히 안겨 있는 이 녀석은…….



[Lv.2 고양이 – 패밀리어]



좀, 다르다.
```

## Current accepted English baseline

```markdown
# Chapter 94

“Three hundred fifty million won.”

The employee’s voice trembled as she ran the payment, and so did my hand as I handed over the card.

*Good lord. Three hundred fifty million won?* I had just spent three years’ worth of salary from back when I worked like a dog in barely an hour.

*No. Let’s look on the bright side.*

This was money spent to protect my family from the people watching us.

I could keep earning money from now on, anyway, and I could use the things I bought today for a long time.

Beep.

- Approval complete.

“Your payment has gone through.”

Thanks to me, this young lady was the only one who had hit the lottery. I took my card back from Assistant Manager Kim Seonhee, whose smile stretched from ear to ear.

“So that’s everything, right?”

“Ah, if you give us your address, we can have everything delivered.”

“That’s all right. I have somewhere to go right now.”

Delivery, my ass. The moment I got out of everyone’s sight, I could just store everything in my Inventory.

*The System sure is convenient at times like this.*

Thinking that, I accepted the shopping bags until both my hands were full. Of course, they weren’t ordinary paper bags. They were tough, sturdy leather shopping bags supposedly made from ogre hide. They had been free gifts, but instead of feeling happy, they just made my stomach hurt.

“Take care.”

“Please come back next time! We look forward to seeing you again.”

“…Ah, yes.”

I accepted the business card she held out while she bent at the waist at a perfect right angle.

*One obsessed with sales figures. Their name: salesperson.*

* * *

I stopped by a nearby restroom and stored the things I had bought at the Store in my Inventory before hailing a taxi. These days, I regretted never getting my driver’s license.

“Please take me to Apartment A in Ilsan.”

The moment I sat in the passenger seat, I pulled out my smartphone and started searching for information.

The search term was…

*Familiar.*

The moment I pressed the search button, related information came streaming onto the screen.

There was quite a bit of information that ordinary people couldn’t see and that required Hunter certification to access. One title in particular caught my eye.

No Joke: Don’t Use Familiar Magic. It Made My Hair Fall Out.

It was a title that resonated with my soul. There was no way I could not click it.

*Ah, so this was where it was posted.*

The post was on a famous domestic Hunter community site.

It had been selected as a monthly best post, with over one hundred thousand views and more than two thousand comments.

*Let’s see what it says.*

Click!

No Joke: Don’t Use Familiar Magic. It Made My Hair Fall Out.

I’m a currently active B-rank mage.

I’ve been in the business for a while and make decent money as a freelance Hunter. Please understand that I can’t reveal my exact specifications.

Anyway, the reason I’m writing this post is exactly what the title says.

I got hit by a hair-loss beam because of Familiar magic…

I’m still in my twenties, but the top of my head is classmates with a two-thousand-year-old mummy. Goddamn it.

Before anyone starts nitpicking, let me say this in advance: My family has always been blessed with thick hair. I even saw a photograph of my great-grandfather taken during the Japanese occupation, and he looked like Rapunzel of Joseon.

Anyway, back to Familiar magic. This stuff is a real double-edged sword.

Any of you guys who are mages will know this, but mental magic isn’t exactly common. Even civilians can make a living once they learn a skill.

For a mage, mental magic is exactly like that. If you have this one thing, you can live well no matter what.

But fuck, your hair starts falling out. It keeps falling out.

Anyone here ever tried washing their hair with a Superior Potion? I have.

You crazy bastards, I spent tens of millions of won washing my hair just once. I tried every kind of crazy shit imaginable, but even that only worked for a little while.

When none of it worked, I went to a regular doctor, and the bastard let out a long sigh and said:

“You’re a mental-magic mage, aren’t you?”

He said it exactly like that, without getting a single word wrong. I was shocked and asked how he knew, and then he told me something genuinely horrifying.

More than ninety percent of mental-magic mages suffer from hair loss, and the rate is one hundred percent among those who use the more difficult Familiar magic.

Apparently, because we overwork our brains like crazy, even people with thick hair turn into bald people at some point.

At first, I thought, *What the hell is he talking about?* But I looked into it, and it turned out to be true.

I hurriedly joined a mental-magic mage café and searched for people like me, only to find that ninety-eight of its one hundred members suffered from hair loss.

After hearing about my situation, they told me it was already too late. Potions only restore cells temporarily, so using them too often just ends up killing your hair-follicle cells.

I ignored the café’s promise to upgrade my membership if I wrote a review of my medical consultation, quit, and am searching for my own treatment method…

Three-line summary.

1. Mental-magic mage is great. But you lose your hair instead.

2. Potions are useless. Use hair-loss-prevention shampoo and go to a regular hospital instead. Hair must be treated with heart and desperation, not magic.

3. I will not give up.

That’s all.

“…”

After reading the entire thing, my vision grew blurry. So even the mages I had always envied, the people who seemed to have everything, had their own hardships.

“Are you all right, sir?”

“I’m fine… Hngh.”

“What’s wrong?”

“Ah, it’s nothing. I’m fine.”

Of all things, the taxi driver happened to be bald, too. Feeling like a sinner, I lowered my head toward my smartphone.

Below the post, I found more than two thousand comments.

Anonymous#232: Give us the one-line summary.

└ Author: [Comment hidden due to severe profanity.]

Anonymous#112: Is the person who made the first comment even human? I cried. I’ll be rooting for you. Hang in there.

└ Author: Thanks…

Anonymous#1512: I don’t know about the rest, but the second commenter seems to be suffering from hair loss, too. But after reading the whole thing, it sounds like you make a lot of money. Can’t you live without some hair? Just wear a good wig.

└ Author: [Comment hidden due to severe profanity.]

Anonymous#4885: Wow, I’m seeing a Familiar mage here. You guys don’t know this, but the author is a real aristocrat. Even among B-ranks, your income is incomparable. So is the way you’re treated.

└ Author: What good is having money when you don’t have any hair?

└ Anonymous#4885: Now that you mention it, you’re right.

└ Author: If you’re going to comfort me, see it through, you son of a bitch.

.

.

.

Moderator: Congratulations! You’ve been selected as a popular post!

└ Anonymous#5252: LMAOOOOOOOOOO

└ Anonymous#8984: LMAOOOOOOOOOOOOOOOOOOOOOOOOOO

└ Author: Am I supposed to laugh at this or not?

└ Anonymous#2652: You don’t have any hair and you still feel like laughing?

└ Author: [Comment hidden due to severe profanity.]

Author: Thanks for the overwhelming support. Looks like I’m about to make the monthly best list and enter the Hall of Fame. If you have any questions, leave them below. I’m working right now, but I’ll drop in and answer them whenever I get a chance.

└ Anonymous#9665: You said you’re a freelancer. What kind of work do you mainly do?

└ Author: Freelancer is a nice way of putting it. What I do is similar to running a private detective agency. I’ve tracked high-level criminals—Hunters, of course—and I’ve also taken on an affair case at a nouveau riche family’s house.

└ Anonymous#915: Oh… You must make a lot. How much do you earn?

└ Author: That depends on the job, obviously. Still, after working for a few years, I put up a building in Seoul. The house I live in now is also under my name.

└ Anonymous#5252: Show us proof of your house.

└ Author: I’m outside working right now. I’ll properly verify it later, so wait until then.

└ Anonymous#9882: What does working have to do with it? Familiars are remote-controlled anyway, aren’t they?

└ Author: Even remote control has a range limit, you idiot. Do you use the Wi-Fi at your house while traveling in the United States?

└ Anonymous#9882: Sorry.

└ Author: The maximum distance for a Familiar connection is five hundred meters. I’m increasing the distance little by little, but it’s difficult. If the Link is forcibly severed, my stomach starts churning and I feel like I’m going to throw up. There’s also a risk of mana backflow.

└ Anonymous#9882: So you always have to stay within five hundred meters.

└ Author: Yeah. To work safely, maybe three hundred meters? You have to prepare for anything that might happen. Most people probably do the same.

I was scrolling through the comments when I suddenly stopped.

It seemed I had unintentionally discovered some important information.

*The connection with a Familiar is severed if it goes beyond five hundred meters?*

The maximum distance was that much, and the safe working distance was three hundred meters.

In other words, if the author’s comments were true, then the people who had controlled the Familiars yesterday had been somewhere not far from my house.

*And they’d be going bald, too. Maybe completely bald.*

There was a strong possibility they were wearing wigs, but knowing that couldn’t hurt.

I continued searching for information about Familiar magic and was able to organize a few facts.

*For a B-rank mage, the maximum Familiar connection distance is five hundred meters. The safe distance is three hundred meters. If a Familiar dies, the Link is forcibly severed, and the caster also takes a slight hit.*

And I realized one more thing: why they had gone out of their way to use an expensive Familiar mage to watch me.

*What? Tiny Familiars don’t get caught by most detection magic?*

It was like this: detection magic was a net, while tiny Familiars like flies and rice weevils were too small to get caught in it.

Of course, there were products with built-in top-of-the-line detection magic capable of detecting even those, but when I looked them up, they cost five hundred fifty million won as part of a summer special.

“…”

I had no idea which part of that was supposed to be a summer special. I already had plenty of places where money would be going from now on. Five hundred million won, my ass.

*That’s one more reason I have to catch them myself.*

My thoughts suddenly turned to the other Guild members, too. Had Familiars been attached only to my family?

I still didn’t know the exact identity of the person who had commissioned this. Sangdong Guild was only the prime suspect.

“That’ll be 8,400 won.”

“Ah, yes. Here you go.”

I paid the taxi fare and got out. The entrance to the apartment complex, which had always looked exactly the same, seemed a little unfamiliar today.

The presence of the watcher bothered me like a thorn lodged in my throat.

*Should I contact Team Leader Choi?*

I was looking at his number saved on my smartphone when—

“Oppa!”

A familiar “swan”[^1] in a green tracksuit and round glasses, her greasy hair tied tightly back, waved at me.

[^1]: In Korean slang, a “swan” is an unemployed woman.

“Oh, y-yeah.”

“What’s with that reaction?”

“I guess I’d rather not acknowledge knowing you in public. You could say I’m embarrassed…”

“Are you embarrassed by your one and only little sister? Huh?”

“Go buy some clothes. What are you doing wearing a tracksuit again when you left the clothes you bought at the department store last time at home?”

“You should worry about yourself. You’re one to talk, when you go around wearing the same kinds of clothes every day.”

Hayeon’s pointed remark left me speechless for a moment. I had paid three hundred million won only an hour or two ago, but I was still wearing nothing but jeans and a T-shirt. Apparently, the old grime of being an ordinary little citizen, caked on over twenty-seven years, had not yet completely washed off.

“W-Well, anyway. Where are you headed?”

“Where am I going? The convenience store!”

Hayeon, who had been sulking until just now, began grinning foolishly.

*What’s gotten into her?*

I asked in a bemused voice.

“Why are you so excited? Is your heart already pounding at the thought of raiding the convenience store?”

“Who’s raiding anything? I’m going to buy canned tuna.”

“Canned tuna? Are we having tuna kimchi stew for lunch today?”

“No! We’re not!”

“…What’s with you today, seriously? Did you drink?”

“You’ll be like this, too, when you see this little one.”

Despite my reaction, Hayeon only continued to grin strangely, unlike her usual self. Then she lowered the zipper of her tracksuit and pulled something out from inside her clothes.

A tiny ball of white and yellow fur wriggled in her palm.

“Meeoow.”

“…Is that a kitten?”

“Cute, right? I went out to sort the recycling earlier, and someone had abandoned it in a box. It had been left there for anyone who wanted to raise it.”

“…”

“I don’t know what kind of bastard abandoned her, but she’s pitiful, isn’t she? What did it ever do to deserve that? Right, Oppa?”

“…Yeah. Animals haven’t done anything wrong.”

“I got Mom’s permission to foster it, even if it’s only for a little while. You’re okay with it, too, right?”

“Me?”

“Yeah. Our Mom melts for her eldest son, you know. She told me to get your permission, too, so put in a good word for me when we go inside later.”

“We’ll see.”

“What? You liked animals when you were little.”

I did. I still did, in fact. But this little thing sitting quietly in Hayeon’s palm was…

> **System**
>
> Lv. 2 Cat—Familiar

A little different.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 94`.

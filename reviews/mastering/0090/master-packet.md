# Master Edit Task — Chapter 90

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
| 최민우    | **Choi Minwoo**   |
| 임창수    | **Im Changsoo**   |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
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

#### Chapter 88 tail (verified mastered)

…
the owner examined the thin silver card I handed her, her mouth fell open. “…C-rank Hunter?” “Personally, I think rank is everything for Hunters. What do you think, Boss?” “N-no way. I heard you were F-rank…” “I was F-rank. I’m C-rank now. You’re pretty slow about updating your information.” “I-isn’t this fake? The color is completely different from my Minsu’s license!” “His license is brass-colored, right?” “…” “I used one of those myself in the past. Lower-rank Hunters have brass-colored licenses, while mid-rank Hunters have silver ones. You didn’t know that?” Suppressed laughter erupted from all around us. The atmosphere had flipped in an instant. My mother slipped her arm through mine with a proud smile, while the owner’s face turned bright red and she began making excuses. “D-does a Hunter’s rank really matter? C-rank and D-rank are only one step apart. They’re practically the same.” *Was that supposed to be an argument or a fart?* All I could do was laugh hollowly at her absurd struggle. “That’s not something a person who looked down on someone for their Hunter rank should be saying.” “Is a person’s title all that matters? The company they work for matters more. People respect an Assistant Manager at a major corporation more than a section manager at a small company. Am I wrong?” “I don’t know about that, but the customers here don’t seem to agree with you.” I gestured toward the customers filling the dining area. Dozens of office workers from small and midsize companies were glaring at the owner without bothering to hide their displeasure. “What’s with that ajumma?” “My appetite’s completely gone.” “The food hasn’t even come out yet. Should we just leave?” “Yeah. Let’s go.” “Everyone, let’s eat somewhere else. There’s a decent set-meal place right up ahead. I may not be an Assistant Manager at a major corporation, but I’m a section manager at a small company, so lunch is on me.” Scrape. At the middle-aged man’s words, five or six of his subordinates stood and followed him. Similar scenes began unfolding throughout the dining area. “Customers, that’s not what I meant. Customers!” “What do you mean, it’s not? Just watch me never come back here.” “But your orders have already gone in. If you leave like this…” “Looking at that kitchen, it’ll take an hour anyway. Forget it. We’re leaving too.” Despite the dining staff’s attempts to stop them, the customers streamed out like the receding tide. Barely a minute later, fewer than ten customers remained in the dining area. *Damn. I can already hear the sound of this place going under.* The owner was trembling with anger and bewilderment. “You… You people…” “So which Guild did you say your son was with?” “Our Minsu is a real hotshot Hunter in Sangdong Guild! Someone like you…” “What? Which Guild?” “Sangdong Guild! They even gave him a house and a car.” “Oh, Sangdong Guild. Could you wait just a moment?” What an incredible coincidence. Holding back my laughter, I pulled out my smartphone and made a call. Beep. Beep. Beep. Click. “Uh, what is it?” “What do you mean, what is it? Are we only supposed to call each other when we have business?” “…I sent you the promised four billion won, though.” “Ah, I checked that. It came through fine.” The conversation continued over speakerphone, loud enough for everyone to hear. Four billion won. The moment it became clear that what I had said earlier was true, everyone’s eyes nearly popped out of their heads. I ignored all the stares and got to the point. “Do you happen to know a Kim Minsu?” “Kim Minsu? That’s the first I’ve heard of him.” “You’re a Team Leader in Sangdong Guild, and you don’t even know him? Apparently, he’s a D-rank Hunter in your Guild.” “D-rank Hunters are a dime a dozen. How am I supposed to know all of them? Is that why you called?” “Yeah. Bye.” Getting Im Changsoo’s business card in case he tried to stiff me had been a stroke of genius. Click. As soon as I hung up, the owner asked in a faltering voice. “W-who was that?” “Didn’t you hear? He’s a Team Leader in Sangdong Guild. Put simply, he’s Mr. Minsu’s boss.” “…Team Leader? His boss?” “Oh, and one more thing. He’s also a future employer Mr. Minsu will want to impress. His father is the Guild Master of Sangdong Guild.” “…” Her face went white as a sheet. There was no longer any reason or need to exchange another word with her. I turned toward my mother. “Let’s go now.” “Shall we, son?” My mother, Kim Jeonghee, flashed a broad smile and shoved her work clothes into the sink. Of course, she didn’t forget to leave the owner with one final remark. “If you’re a parent, act like one and live right, you ajumma. Where do you get off casually running your mouth about someone else’s precious child?” The final blow. The owner lowered her head without answering, and we left the restaurant with light steps. “Son, have you eaten? There’s cheonggukjang and kimchi pancakes at home.” “Wow. What a feast.” The weather was beautiful. [^1]: *Ajumma* is a familiar Korean term for a married or middle-aged woman, commonly used by customers or employers to address service workers. [^2]: A *goshiwon* is a tiny, inexpensive room-for-rent housing arrangement, often with shared facilities.

#### Chapter 89 tail (verified mastered)

…
me. You can do it right now, if you want.” “Should I? Come to think of it, I’ve been having trouble digesting lately…” Mom smiled brightly and held out her hand. That was when— *Bwaaaang. Frrt. Frrt.* “…….” “…….” Mom quietly withdrew her hand. “……Should we start when Hayeon comes out?” “……Yes.” Our house had only one bathroom. * * * *Whooosh.* Some time after the sound of the toilet flushing, Mom emerged with the most refreshed expression in the world. “How do you feel?” “I feel ten years younger.” That was no exaggeration. Even nineteen-year-old Hayeon had taken more than an hour to expel all the waste from her body. Mom was middle-aged, and the amount of waste she had accumulated matched the years she had lived. After more than two hours of Circulate Qi for Healing, her condition must have improved beyond comparison. “See? Until a little while ago, I had a headache and felt dizzy, but now I’m completely better. I checked my temperature as soon as I came out of the bathroom, and it was normal.” Hayeon stared at me in wonder. As soon as she had emerged from the bathroom, she had polished off two bowls of rice as though she had never complained about having no appetite. “Where did you learn something like this? Were you a healer, Oppa?” “A healer? No. I just happened to learn it.” “Which traditional medicine clinic did you learn it at? If it’s nearby, I’ll go there too.” “……You’d be in big trouble if you went there.” “Why?” “You don’t need to know. Just know that there are lots of scary men there.” “Do they stick the needles in painfully?” “……They do tend to.” *What kind of face would she make if she knew those “needles” were actually knife stabs?* I pushed Hayeon away as she kept peppering me with questions and slipped a hand into my pocket. *Open Inventory.* A translucent inventory window appeared along with the familiar System notification. If I had been in the Murim, it would have been packed with the spoils I had obtained after defeating Jopil and various weapons. But this was reality. *It would be nice if the inventories were integrated.* The more I thought about them being separate, the more disappointing it seemed. Taking just a few high-grade potions to the Murim would be no different from bringing along a few extra lives. *Well, I guess I should be satisfied that leveling up restores me to some extent.* I clicked my tongue inwardly and pulled my hand from my pocket. Two small bottles filled with sloshing red liquid rested in my palm. > **System** > > **Item Window** > > **Lesser Potion** > > - **Type:** Medicine > - **Grade:** Third Rate > - **Description:** A liquid infused with weak healing magic. Readily available on the market. > - **Effect:** Restores the body when consumed. The effect is minimal. They had been issued as raid supplies yesterday. Since I had no particular use for them, I had put them in my Inventory and left them untouched. *Technically, I’m supposed to return them.* Even lesser potions cost more than 200,000 won apiece. Employers generous enough to hand them out as freely as Team Leader Choi were hard to find. “Take one each.” “Huh? It’s a potion.” “Why go as far as using a potion? I’m perfectly fine now.” “I’m worried there might be side effects. If you don’t drink it now, it’ll cost you more later.” In truth, I was only offering them as a tonic. Circulate Qi for Healing had no side effects. “Drink up. You too, Hayeon.” Mom hesitated, then took hers first. Hayeon cautiously took her cue from Mom and followed suit. *Gulp. Gulp.* “How do you feel?” Hayeon downed hers in one shot and tilted her head. “Maybe I feel a little stronger. Or maybe not. How should I know? It’s not like I’ve ever had a potion before.” “I guess I don’t really know either.” “You’ll definitely notice the effect when you’re tired or sick. I’ll buy a box and keep it here, so drink one whenever that happens.” “A box? How many come in a box?” “Fifty, if you buy the large one?” “They’re about 200,000 won each, so fifty would be… ten million won? Oppa, are you insane?” Hayeon smacked my forearm. “Just because you made some money this time, are you really going to spend it so recklessly? If you keep overspending like that, that 300 million won will disappear in no time.” “It’s fine. I’ve been making good money lately.” “I looked it up online. Once you become a C-rank Hunter, you have to replace your equipment and everything, right? They said you can blow through hundreds of millions like it’s nothing.” “I told you, it’s fine. I made four billion won yesterday, too.” “If you have four billion won, then spending like this… Wait. How much did you say?” “Four billion won.” “…….” Hayeon went completely rigid. She stared blankly at me, then turned toward Mom. “Mom, Oppa says he made four billion won.” Mom gave an awkward smile and nodded. Only then did Hayeon ask in a trembling voice, “Is that true?” “Yeah.” “Four billion won?” “I told you.” Determination filled Hayeon’s eyes. “Oppa. Can I drop out of school?” “…….” *Didn’t you say there was no end to learning?*

## Korean source

```text
＃90화



“일주일 동안 휴가요?”

- 네. 들으신 그대롭니다.

그날 저녁에 걸려 온 최 팀장의 전화는 뜻밖이었다.

일주일이나 휴가라니. 길드에 무슨 문제라도 생겼나?

생각이 거기까지 미치자 문득 걸리는 사실이 있었다.

“저, 혹시 상동 길드랑 트러블이 생긴 건 아니죠?”

- 상동 길드요?

“아니 왜, 임창수 문제 때문에…….”

- 아, 그 문제는 신경 쓰지 않으셔도 됩니다. 길드 하우스 리모델링이 일주일 뒤에 끝난다고 해서요.

아무 일 없다니 다행이긴 한데. 길드 하우스 리모델링 때문에 레이드를 쉬는 경우도 있나?

‘일주일이나 쉰다니까 좋긴 한데.’

지난 7년간 앞만 보고 달려온 인생. 요즘 들어서는 무림과 현실까지 오가며 쉴 틈 없는 나날을 보내왔다.

솔직히 쉬고 싶…… 아니다. 이럴 때일수록 더욱 힘내서 일을 해야 한다. 나는 의지에 찬 목소리로 말했다.

“팀장님. 전 일하고 싶습니다.”

- 아, 휴가지만 급여는 정상적으로 나갈 겁니다.

“그럼 일주일 뒤에 뵙죠.”

- …….

“끊을게요. 저녁 먹으러 가야 해서.”

- ……네.

전화를 끊자 하연이가 종종걸음으로 다가와 공손히 고개를 숙였다.

“오라버니. 저녁 식사가 준비되었사옵니다.”

“……그 말투 소름 돋으니까 그만해 줄래?”

“반말 모드로 전환하려면 유료 결제가 필요하옵니다.”

“용돈 달라는 소리를 어렵게도 한다.”

신사임당 두 장을 내밀자 하연이가 씩 웃는다.

“엄마가 저녁 먹으래.”

“오, 메뉴 뭔데.”

“소불고기. 그리고 내가 끓인 콩나물국.”

“소불고기 맛있겠다.”

“콩나물국 맛있대. 엄마한테 칭찬받았어.”

“엄마표 소불고기는 배신하는 법이 없지. 늘 새로워, 최고야, 짜릿해.”

“…….”

잔뜩 열받은 여동생과 한 상 가득 차려진 엄마표 요리.

휴가가 별거냐. 집에서 실컷 먹고 자야겠다.



* * *



탁.

최민우는 전화가 끊긴 스마트폰을 내려놨다. 테이블을 가운데에 두고 앉아 있던 김 집사가 묻는다.

“뭐라고 하던가요?”

“안 그래도 걱정하고 있더군요. 상동 길드에 대해서.”

“보면 볼수록 재미있는 청년입니다. 생각 없이 행동하는 것 같으면서도 상황 파악이 빨라요.”

최민우는 길쭉한 손가락으로 테이블을 두드렸다.

갑자기 등장한 진태경의 존재는 시간이 좀 지난 지금도 여전히 수수께끼다.

처음 만났을 때는 성실한 F급 헌터 그 이상도 이하도 아니었던 그가, 어제는 혼자서 B급 게이트를 쓸어 버렸다.

‘점점 강해지고 있어.’

어제부로 의심이 확신으로 바뀌었다.

진태경은 점점 강해지고 있다. 그것도 매우 빠르게!

“진태경 씨 관련해서는 추가 정보가 없습니까?”

“예, 재확인을 거듭했지만 아무것도 나오지 않습니다.”

김 집사는 일 처리가 확실한 인물이다. 하지만 이번만큼은 경우가 다르다. 최민우는 신중하게 입을 뗐다.

“김 집사님.”

“예, 도련님.”

“혹시…… 3차 각성자의 사례를 찾아볼 수 있겠습니까?”

“네?”

김 집사의 눈썹이 움찔했다.

3차 각성자라니. 일평생 듣도 보도 못한 명칭이다. 만약 그런 헌터가 있었다면 아무도 ‘재각성’이라는 단어를 사용하지 않았을 것이다.

재각성은 그다음이 없기 때문에 재각성인 것이니까.

“도련님, 그건.”

난색을 표하려던 그때, 김 집사의 뇌리에 한 사람의 이름이 스쳤다.

‘진태경. 그 청년이라면 모르겠군.’

김 집사는 대격변을 온몸으로 겪은 산증인이다. 눈부신 전공을 세웠고 수많은 전투에 참전했다.

그러나 그의 시선에도 진태경은 특별했다.

‘그 움직임들…… 실로 대단했지.’

때로는 강하게, 혹은 유려하게, 효율적인 공수 전환과 나아갈 때와 물러설 때를 아는 타고난 전투 감각.

진태경의 싸움을 보고 있자면 압도적이라는 표현밖에 떠오르지 않았다.

‘3차 각성자라.’

시간은 걸리겠지만 충분히 알아볼 가치가 있다.

김 집사가 고개를 숙였다.

“알아보겠습니다.”

“고맙습니다. 아, 상동 길드 쪽 동향은 어떤가요?”

“감시원들을 풀었습니다. 아마 며칠 안에 대부분의 정보를 입수할 겁니다.”

임창수가 길드장실로 불려 가 개처럼 맞았다는 정보를 입수한 지 반나절도 되지 않았는데, 벌써 감시원들이 달라붙기 시작했다. 예상보다 빠른 움직임이다.

“목표는 진태경 씨겠군요.”

“주요 인물로 찍어 뒀을 겁니다. 일단은 길드 전체를 샅샅이 분석하겠지만요.”

“다른 길드원들은 어떻습니까?”

“혹시 미행이 붙을 수도 있으니 언질 정도는 해 두었습니다. 그런데…….”

김 집사가 멈칫하더니 덧붙였다.

“진태경 씨한테도 알려 줘야 하지 않겠습니까?”

“괜찮습니다. 전 오히려 상동 길드의 정보력이 우리보다 훨씬 뛰어났으면 하는 바람입니다.”

가장 알 수 없는 인물, 그리고 가장 많은 것이 드러나 있는 인물.

맑은 샘물을 보면서도 그 안에 무엇이 들어 있는지 볼 수가 없는 것과 같다.

최민우는 상동 길드의 힘을 빌려서라도 진태경의 정체에 근접하고 싶은 마음이었다.

“그보다, 상동 길드장이 화가 단단히 났나 봅니다.”

“그래도 많이 신중해진 것 같더군요. 예전 같았으면 진작 쳐들어와 난동을 피웠을 텐데.”

“아, 혹시?”

최민우의 반응에 김 집사가 웃으며 고개를 끄덕였다.

“상동 길드장과는 안면이 있습니다.”

“악연인가요?”

“글쎄요.”

김 집사의 웃음이 진해졌다.



* * *



“무슨 일로?”

이마가 번쩍번쩍 빛나는 부동산 아저씨의 물음에 내가 대답했다.

“집 좀 보려고요.”

“찾으시는 집이 월세? 전세? 아니면…….”

“매매요.”

“어이쿠, 젊은 사장님이셨네. 미안한데 잠시만 기다려 봐요. 내 이것만 처리하고 후딱 올게. 너무 급해서 참을 수가 있어야지.”

뭘 처리하나 했더니, 손에 화장지를 들고 있다.

다른 것도 아니고 그거면 빨리 처리하셔야지. 내가 고개를 끄덕이자 부동산 아저씨가 화장실로 후다닥 뛰어 들어갔다.

“소파에서 뭐라도 드시면서 기다리고 계세요. 탁자에 모카빵. 끄으으으읍.”

푸드득. 푸드드득.

“…….”

앞으로 모카빵은 못 먹겠군.

내심 한탄하며 소파에 몸을 기댔다. 이미 틀어져 있던 TV 화면에서는 대격변 관련 다큐멘터리가 흘러나오고 있었다.



- 꺄아아악!

- 콰과광! 펑!

- 긴급 속보입니다. 현재 전국 곳곳에서 정체불명의 현상들이 벌어지고 있습니다. 이에 정부는 현 시간부로 계엄령을 선포하였으며…….



비명을 지르며 흩어지는 사람들, 무너지는 건물과 솟구치는 화염, 대격변의 시작을 알리는 뉴스가 차례차례 스쳐 지나가고 미국 대통령의 초췌한 얼굴이 화면을 꽉 채웠다.



- 아직 저들의 정체를 파악하지 못했으나 한 가지는 확실합니다. 그들은 우리의 적입니다. 미합중국뿐만이 아닌 전 세계, 전 인류의 적입니다. 지금도 수많은 몬스터가 게이트를 통과해 지구를 침략하고 있습니다.



게이트(Gate).

게이트는 말 그대로 문을 뜻한다. 마왕 아스모데우스는 차원 저 너머에서 이 문을 열고 지구에 강림했다. 헤아릴 수 없이 많은 몬스터 군단과 함께.

‘그 후로는 교과서에 적힌 대로고.’

인류는 속수무책이었다. 도심지, 농촌, 산과 바다, 밀림……. 때와 장소를 가리지 않고 생성되는 게이트와 쏟아지는 괴물들이 살인과 파괴를 일삼았다.

게이트가 열린 후 ‘피의 일주일’이라 불리는 지옥 같은 시간이 끝났을 때, 사상자는 수천만에 달했고 재산 피해는 정확한 집계조차 내지 못할 정도였다.



- 대격변, 인류 역사상 가장 끔찍했던 10년의 역사.



자막과 함께 다큐멘터리가 중반에 접어들 때쯤 화장실 문이 벌컥 열렸다.

“휴, 이제 좀 살겠네.”

부동산 아저씨가 땀으로 번들거리는 이마를 닦으며 털썩 주저앉았다.

“오래 기다리게 해서 미안합니다. 매매 알아보신다고 했죠?”

“네.”

“혹시 다른 곳 들렀다가 오시는 길인가? 오는 길에 부동산 많았을 텐데.”

“아뇨, 여기가 처음이에요.”

“그으래요?”

눈동자를 굴리는 걸 보아하니 호구 잡을까 말까 고민 중인 모양이다. 나는 모른 척하며 쪽지를 내밀었다.

쪽지에는 미리 적어 온 주소지가 적혀 있었다.

“가급적이면 이쪽 매물로 보고 싶은데요.”

“이 주소지면…… 안전 구역인데?”

“네.”

“매매 맞죠? 아까 똥이 급해서 잘못 들었나?”

고개를 끄덕이자 아저씨의 눈이 슬쩍 위아래로 움직인다.

청바지에 흰 티셔츠. 시장에서 인터넷에서 주고 산 2만 원짜리 운동화. 누가 보더라도 결코 있어 보이는 차림은 아니다.

“혹시 직업이 어떻게 되시나?”

“게이트 뜁니다.”

“아, 헌터? 어쩐지. 젊은 분이 성공하셨네.”

아저씨의 얼굴에 웃음꽃이 활짝 피었다. 헌터는 대표적인 고수입 직종 중 하나다. 젊고 잘나가는 헌터들이 고가의 집과 차를 구매하는 것은 그리 드문 일이 아니다.

그가 한결 친절해진 말투로 물었다.

“시세는 대충 알아보셨어요?”

“오면서 인터넷으로 검색해 봤어요.”

“운 좋으시네. 안 그래도 매물이 좀 있긴 하거든요. 어디 보자…….”

아저씨가 몸이 달았는지 바쁘게 여기저기 전화를 걸기 시작한다.

끊고 다시 걸기를 반복하고 5분쯤 지났을까? 그가 스마트폰을 집어넣으며 내 쪽으로 돌아섰다.

“사장님한테 딱 맞는 매물을 찾았는데. 어떻게, 바쁘지 않으면 지금 가서 한번 보실래요?”

“그러죠, 뭐.”

휴가 중인 나로서는 거절할 이유가 없다. 내가 자리에서 일어나자 아저씨가 함박웃음을 지었다.



* * *



부우웅.

승용차 조수석에 앉아 스쳐 가는 풍경을 바라봤다. 줄지어 서 있는 단독 주택과 군데군데 자리한 상가, 놀이터와 학교.

“많이 변했네…….”

내 중얼거림에 아저씨가 슬쩍 곁눈질했다.

“여기 사시던 분이에요?”

“어릴 때요.”

중학교 3학년. 열여섯 살 때니까 지금으로부터 딱 11년 전이다. 이곳에서 태어나고 자랐으니 내게는 고향인 셈이다.

“여기가 10년 전쯤 재개발돼서 많이 바뀌었을 거예요. 원래 낡은 아파트 단지였는데 30분 거리에 협회 지부 세워진다니까 엎어 버린 거지.”

“그렇군요.”

이미 알고 있는 사실이다. 재개발 소식이 들리기가 무섭게 집값이 폭등했고, 몇억씩이나 오른 전세금을 감당할 수 없었던 우리는 이사를 결심했다.

‘아버지가 돌아가신 지 얼마 안 됐을 때였어.’

이사 전날 밤, 숨죽여 우시는 엄마의 모습을 봤다.

그곳이 부모님의 신혼집이었다는 이야기를 들은 건 그로부터 몇 년이나 지난 후였다.

“도착했어요.”

아저씨의 말에 정신을 차렸다. 문을 열고 나오자 마당이 깔린 단독 주택 한 채가 보인다.

“사장님이 말했던 주소가 여기예요. 마침 집주인도 없으니까 후딱 보고 나오자고.”

“아, 잠시만요.”

과거의 향수 때문일까? 낡은 아파트 단지는 이미 허물어지고 없지만 어딘지 모르게 친숙하다.

‘그래도…… 아주 바뀌진 않아서 다행이네.’

재개발을 거친 후에도 남아 있는 옛 풍경들이 있다. 감회에 젖어 주위를 둘러보는 내 모습에 아저씨가 입맛을 다셨다.

“오랜만에 오셔서 좋으신가 보네. 이참에 그냥 동네 한 바퀴 돌고 오실래요?”

“그래도 됩니까?”

“계약하실 거잖아. 아니에요?”

“아뇨. 맞습니다.”

이 집은 어떻게든 사야 한다.

피식 웃은 아저씨가 담배를 꺼내 들었다.

“그럼 편의 봐 드려야지, 동네 한 바퀴 도는 데 얼마나 걸린다고. 여기서 담배 한 대 피우고 있을 테니까 신경 쓰지 말고 다녀와요.”

가볍게 감사를 표한 후 천천히 걷기 시작했다.

‘이 길이 맞나?’

골목을 지나 어린 시절 자주 가던 슈퍼를 발견한 그 순간이었다.

“오빠 어릴 때 여기가 아지트였거든. 중학교 때 담배 막 피울 때 여기 할머니가 나이가 많아서…….”

슈퍼 앞에 주차된 번쩍거리는 외제 차. 대화를 나누던 한 쌍의 남녀가 나를 보고 멈칫했다.

아니, 정확히는 남자 쪽이 그랬다. 고개를 갸웃거리던 그가 내게 다가와 말했다.

“혹시 저 아세요?”
```

## Current accepted English baseline

```markdown
# Chapter 90

“A week off?”

“Yes. Exactly as you heard.”

Team Leader Choi’s call that evening had been unexpected.

A whole week off? Had something happened to the Guild?

When my thoughts reached that point, I suddenly remembered something.

“Uh, you didn’t have a problem with Sangdong Guild, did you?”

“Sangdong Guild?”

“I mean, because of the Im Changsoo situation…”

“Ah, you don’t need to worry about that. The Guild house remodeling is supposed to be finished in a week.”

It was a relief to hear that nothing had happened. But did people really stop raiding because of Guild house remodeling?

*It’s nice to hear I’m getting a whole week off.*

For the past seven years, I had lived with my eyes fixed straight ahead, running without rest. Lately, I had been going back and forth between the Murim and reality, spending my days without a moment to breathe.

Honestly, I wanted to re—no. This was precisely when I needed to work harder. I spoke in a voice filled with determination.

“Team Leader. I want to work.”

“Ah, but you’ll still receive your full salary during your vacation.”

“Then I’ll see you in a week.”

“……”

“I’m hanging up. I need to eat dinner.”

“…Yes.”

As soon as I ended the call, Hayeon came hurrying over and bowed politely.

“Oppa. The evening meal has been prepared.”

“……Could you stop speaking like that? It’s giving me goose bumps.”

“Switching to casual mode requires a paid purchase.”

“You make asking for allowance sound so complicated.”

When I held out two 50,000-won bills, Hayeon flashed a wide grin.

“Mom says dinner’s ready.”

“Oh, what’s on the menu?”

“Beef bulgogi. And bean sprout soup that I made.”

“Beef bulgogi sounds good.”

“Mom says my bean sprout soup is good. She praised me.”

“Mom’s homemade beef bulgogi never lets you down. It’s always fresh, the best, thrilling.”

“……”

My younger sister was thoroughly pissed off, and the table was covered with Mom’s cooking.

What was so special about vacation? I would eat and sleep to my heart’s content at home.

* * *

Tap.

Choi Minwoo set down his smartphone after ending the call. Butler Kim, seated across the table from him, asked,

“What did he say?”

“He was worried too. About Sangdong Guild.”

“The more I see of him, the more interesting that young man becomes. He seems to act without thinking, yet he’s quick to grasp the situation.”

Choi Minwoo tapped the table with his long fingers.

Even after some time had passed, the sudden appearance of Jin Taekyung remained a mystery.

When they had first met, Taekyung had seemed like nothing more or less than a diligent F-rank Hunter. Yet yesterday, he had single-handedly swept through a B-rank Gate.

*He’s getting stronger.*

As of yesterday, his suspicions had turned into certainty.

Jin Taekyung was getting stronger. And he was doing so incredibly fast.

“Is there no additional information about Jin Taekyung?”

“No. I’ve repeatedly reconfirmed everything, but nothing has turned up.”

Butler Kim was a man who handled his work thoroughly. But this time was different. Choi Minwoo carefully opened his mouth.

“Butler Kim.”

“Yes, Young Master.”

“Could you perhaps look for cases of Hunters who awakened a third time?”

“What?”

Butler Kim’s eyebrows twitched.

A third awakening? It was a term he had never heard or seen in his entire life. If a Hunter like that had existed, no one would have used the word *reawakening*.

A reawakening was called a reawakening because there was nothing after it.

“Young Master, that…”

Just as Butler Kim was about to express his difficulty, a name flashed through his mind.

*Jin Taekyung. If it’s that young man, who knows?*

Butler Kim was a living witness who had experienced the Great Cataclysm firsthand. He had accomplished brilliant feats and participated in countless battles.

Yet even to his eyes, Jin Taekyung was special.

*Those movements… They were truly remarkable.*

Sometimes forceful, sometimes fluid. His transitions between offense and defense were efficient, and he possessed an innate combat sense that told him when to advance and when to retreat.

When Butler Kim watched Jin Taekyung fight, the only word that came to mind was *overwhelming*.

*A third awakening, huh.*

It would take time, but it was worth investigating.

Butler Kim lowered his head.

“I’ll look into it.”

“Thank you. Ah, what are Sangdong Guild’s movements like?”

“They’ve deployed surveillance agents. They’ll probably obtain most of the information within a few days.”

It had not even been half a day since word came that Im Changsoo had been summoned to the Guild Master’s office and beaten like a dog, yet Sangdong Guild’s watchers had already latched on. They were moving faster than expected.

“The target is Jin Taekyung, then.”

“They must have marked him as a major figure. For now, they’ll analyze the entire Guild, though.”

“What about the other Guild members?”

“I’ve warned them in case someone follows them. But…”

Butler Kim hesitated before adding,

“Shouldn’t we tell Jin Taekyung as well?”

“It’s fine. In fact, I hope Sangdong Guild’s intelligence network is far better than ours.”

The person who was hardest to understand—and the person about whom the most had already been revealed.

It was like looking into a clear spring and still being unable to see what lay inside.

Choi Minwoo wanted to use Sangdong Guild’s power, if necessary, to get closer to Jin Taekyung’s true identity.

“More importantly, it seems Sangdong Guild’s Master is extremely angry.”

“He does seem much more cautious than before. If this were the past, he would have barged in and caused a scene by now.”

“Ah. Could it be?”

At Choi Minwoo’s reaction, Butler Kim smiled and nodded.

“I’m acquainted with Sangdong Guild’s Master.”

“An ill-fated relationship?”

“Who knows?”

Butler Kim’s smile deepened.

* * *

“What can I do for you?”

I answered the real estate agent, a man whose forehead shone brightly.

“I’d like to look at some houses.”

“Are you looking for a monthly rental? A jeonse lease? Or perhaps…”

“A house to buy.”

“Well, well. So you’re a young Boss. Sorry, but wait just a moment. Let me take care of this and I’ll be right back. It’s so urgent I can barely hold it.”

I wondered what he needed to take care of, then noticed the toilet paper in his hand.

If that was what he needed to take care of, he should hurry. When I nodded, the real estate agent dashed into the bathroom.

“Have something to eat while you wait on the sofa. There’s some mocha bread on the table. Gnnngh…”

Pfft. Pffft.

“……”

I wouldn’t be able to eat mocha bread ever again.

I lamented inwardly and leaned back against the sofa. On the television, which had already been turned on, a documentary about the Great Cataclysm was playing.

> “Aaaah!”
>
> “Crash! Boom!”
>
> “This is an emergency bulletin. Mysterious phenomena are currently occurring across the country. In response, the government has declared martial law effective immediately…”

People scattered while screaming, buildings collapsed, and flames shot into the sky. News reports announcing the beginning of the Great Cataclysm flashed by one after another, until the exhausted face of the American president filled the screen.

> “We have yet to determine their identity, but one thing is certain. They are our enemies. Not merely the enemies of the United States, but the enemies of the entire world and all of humanity. Even now, countless monsters are passing through Gates and invading Earth.”

Gate.

A Gate meant a door, quite literally. The Demon King Asmodeus had opened that door from beyond another dimension and descended upon Earth with an innumerable army of monsters.

*After that, it went exactly as written in the textbooks.*

Humanity had been helpless. Downtown areas, rural villages, mountains and seas, jungles… Gates appeared regardless of time or place, and the monsters pouring through them committed murder and destruction.

When the hellish period known as the Bloody Week ended after the Gates first opened, the casualties numbered in the tens of millions, while the property damage was so immense that it could not even be calculated accurately.

> The Great Cataclysm: The Ten Most Horrific Years in Human History.

By the time the documentary reached its midpoint alongside the caption, the bathroom door flew open.

“Whew. I feel alive again.”

The real estate agent plopped down after wiping his sweat-slick forehead.

“Sorry to keep you waiting. You said you were looking to buy, right?”

“Yes.”

“Did you happen to visit somewhere else before coming here? There must’ve been plenty of real estate offices on the way.”

“No, this is my first stop.”

“Really?”

Judging by the way his eyes rolled around, he seemed to be deciding whether or not to take me for a fool. I pretended not to notice and held out the note I had prepared.

It had the address written on it.

“I’d prefer to see the property at this address, if possible.”

“With this address… that’s a safe zone.”

“Yes.”

“You really said you wanted to buy, right? Did I hear you wrong because I had to take a dump so badly?”

When I nodded, the man’s eyes traveled subtly up and down.

Jeans and a white T-shirt. A pair of 20,000-won sneakers bought at a market or online. No matter how you looked at it, I was not dressed like someone wealthy.

“What do you do for a living?”

“I run Gates.”

“Oh, a Hunter? I thought so. You’re young and already successful.”

A bright smile blossomed across the man’s face. Hunters were one of the most prominent high-income professions. It was hardly unusual for young, successful Hunters to buy expensive houses and cars.

He asked in a much friendlier tone,

“Have you checked the market prices?”

“I searched online on the way here.”

“Then you’re in luck. There actually happen to be a few listings available. Let’s see…”

Perhaps he was excited by the prospect of a sale, because the man began making calls to one person after another.

He hung up and called again, repeating the process. About five minutes later, he put away his smartphone and turned toward me.

“I found a listing that’s perfect for you, Boss. If you’re not busy, would you like to go take a look right now?”

“Sure. Why not?”

Since I was on vacation, I had no reason to refuse. When I stood up, the man broke into a huge smile.

* * *

Vroom.

I sat in the passenger seat of the sedan and watched the scenery pass by. Detached houses stood in rows, shops dotted the streets here and there, and playgrounds and schools appeared along the way.

“It’s changed a lot…”

The man glanced at me.

“Did you used to live around here?”

“When I was young.”

I had been in my third year of middle school—sixteen years old—so it had been exactly eleven years since then. I had been born and raised here, so in a way, this was my hometown.

“This area was redeveloped about ten years ago, so it must look pretty different. It used to be an old apartment complex, but when they heard an Association branch was going to be built within thirty minutes of here, they tore the whole thing down.”

“I see.”

I already knew that. As soon as news of the redevelopment spread, housing prices skyrocketed. We could not afford the jeonse deposit, which had risen by hundreds of millions of won, so we decided to move.

*It was not long after my father died.*

On the night before we moved, I saw Mom crying silently.

It was several years later that I learned the place had been my parents’ newlywed home.

“We’re here.”

The man’s voice brought me back to myself. When I opened the door and stepped outside, I saw a detached house with a yard.

“This is the address you gave me, Boss. The owner happens to be out, so let’s take a quick look around and get going.”

“Ah, just a moment.”

Maybe it was because of the memories. The old apartment complex had already been demolished, but the area still felt strangely familiar.

*Still… I’m glad it hasn’t changed completely.*

Some traces of the old scenery remained even after the redevelopment. The real estate agent smacked his lips as he watched me look around, lost in nostalgia.

“You must be happy to be back after all this time. Why don’t you take a lap around the neighborhood while you’re at it?”

“Is that okay?”

“You’re going to sign the contract, right?”

“No. I mean, yes.”

This house was something I had to buy, no matter what.

The man let out a quiet laugh and took out a cigarette.

“Then I should accommodate you. It won’t take long to walk around the neighborhood. I’ll stay here and smoke while I wait, so don’t worry about me.”

After offering him a brief word of thanks, I began walking slowly.

*Is this the right way?*

I passed through an alley and found the supermarket I had often visited as a child.

“When I was a kid, this place was my hangout. Back when I smoked like crazy in middle school, the old lady here was so old that…”

A gleaming foreign car was parked in front of the supermarket. A man and woman who had been talking together stopped when they saw me.

No—the man was the one who stopped.

He tilted his head, then approached me and asked,

“Do you know me?”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 90`.

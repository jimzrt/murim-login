# Master Edit Task — Chapter 42

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
| 일류     | **First Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 지능               | **Intelligence**               |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 임꺽정 | **Im Kkeokjeong** |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |
| 고생하셨습니다 | register | Subordinate courtesy (“thank you for your hard work”), not a superior’s “Good work.” | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 35–39

## Plot

Taekyung visits Hyuk Mujin, Han Yeop, Gong Yacheong, Socheon, Soyul, and the injured reconnaissance squad before the Jin Family’s march. Hyuk and Han, both alive but seriously injured, vow to surpass Jopil and catch up to Taekyung. Gong returns Jopil’s possessions: the Supreme Peak **Flame Divine Palm** manual, the dangerous **Fire Divine Elixir**, and a mysterious **Nameless Sword** forged from ten-thousand-year cold iron.

Taekyung’s Fame reaches 475/500, then stalls. He commands the rear guard as the Jin Family and its allies march north. Jin Wikyung predicts victory within three days but privately tells Taekyung to survive and flee if the family loses, so Taekyung and Jin Mukyung can preserve its future. The exhausted Mount Heng reinforcements cross Mount Otae, and Wikyung plans to force the enemy through narrow Eight Spring Gorge, where the Jin Family has hidden roughly one hundred horn bows.

At Honju, Gwak Jun, the supposedly allied Level 40 leader of the Three Paths Sect, reveals that he and twenty black-clad fighters are First Rate assassins. A herd of water deer disrupts their ambush, triggering Taekyung’s solo **Slay the Assassins** Quest. Taekyung and the reconnaissance squad defeat the assassins through formation tactics and Taekyung’s use of Inventory weapons and **One Flash**. Gwak is captured but dies after severing his own heart meridian. He reveals that the Three Paths Sect was founded thirty years earlier according to an unidentified person’s will.

The System grants Taekyung 50 Fame and a level-up, raising him to 547/500 Fame and starting the three-second Logout countdown. He loses consciousness but successfully logs out. Thirty days in Murim correspond to only three hours in reality. Taekyung wakes in the unplugged Ark - 2020 capsule with Seong Jinho, who dismisses his account as insanity. The manual identifies H Soft as the manufacturer and states that the registered user is permanently bound until death, that reality and game time can pass at an adjustable slow ratio, and that **Character Synchronization** is a key feature. The capsule’s origin and connection to Murim remain unexplained.

## Continuity

- Taekyung is First Rate, Lv. 33 after the assassin Quest, with 547 Fame; Logout has succeeded, but the System is unavailable in reality.
- Taekyung possesses Jopil’s **Flame Divine Palm** manual, **Fire Divine Elixir**, and **Nameless Sword** in his Inventory. The manual requires Scorching Yang Qi; the elixir contains dangerous fire qi and grants thirty years of internal energy; the sword’s special power is unknown.
- Hyuk Mujin and Han Yeop survived Jopil’s attack. Han remains hospitalized with unhealed internal injuries; Hyuk’s internal injuries heal, but he joins the march despite serious external injuries.
- Taekyung commands the Jin Family rear guard. The broader war is expected to involve roughly fifteen hundred martial artists, with the Jin Family and allies moving to Eight Spring Gorge and Mount Heng’s forces approaching Jeongyang.
- Gwak Jun and the twenty infiltrators were assassins impersonating the Three Paths Sect. The real sect was established thirty years ago according to an unidentified conspirator’s will. More than one hundred suspected allied fighters came from the Three Paths Sect and Gunggwimun.
- Taekyung suspects the Head Elder has betrayed the Jin Family and assembled its strength to seize Shanxi. The Head Elder’s Sound Transmission accomplice, the infiltrators’ full chain of command, and the wider plan remain unresolved.
- Taekyung remembers Murim and its inhabitants as real. The capsule’s purpose, Character Synchronization, permanent user binding, route back to Murim, and the limits of death and resurrection remain unresolved.
- Seong Jinho currently believes Taekyung is mentally ill. The capsule was unplugged when Taekyung returned, despite the completed Murim experience.
- The manual’s observed time ratio is thirty days in Murim to three hours in reality; it describes the ratio only as adjustable and reversible.

## Translation Decisions

- Preserve **Flame Divine Palm**, **Fire Divine Elixir**, **Nameless Sword**, **One Flash**, **Slay the Assassins**, **Fame**, **Logout**, **Inventory**, **First Rate**, **Peak**, and **Character Synchronization** as established terminology.
- Keep **Three Paths Sect**, **Gunggwimun**, **Eight Spring Gorge**, **Mount Otae**, **Honju**, **Sound Transmission**, and **rear guard** consistent with prior chapters.
- Preserve the abrupt water-deer interruption, the reconnaissance squad’s drilled teamwork, Taekyung’s violent dark comedy, and the cliffhanger transition between Murim and reality.
- Render the capsule’s displayed forms exactly as **Ark - 2020** and **H Soft**.
- Retain Taekyung’s dry, self-mocking first-person voice and the blunt informal exchange with Seong Jinho.

### Prior accepted reading-copy tails

#### Chapter 40 tail (verified mastered)

…
Goshiwon. I sat beneath the old, rusted sign and pulled out my smartphone. The other end picked up almost before it could ring. Click. “Yeah. Why?” My one and only nemesis—no, my younger sister, Hayeon. The moment I heard that uniquely bratty voice of hers, my throat closed up. “Hello?” “…Yeah.” “Why’d you call?” “Just. I wanted to hear your voice.” A deathly silence followed. “I’m hanging up.” “No, wait. Wait!” “Three seconds. What’s your business.” *That damn girl…* Right. This was Jin Hayeon. Thanks to her, the tear ducts that had gotten a little moist dried out like sand around the pyramids. “What’s Mom doing?” “She went out. Said she had an errand. Call her if you’re curious.” I deliberately didn’t. Even this brat’s voice was enough to choke me up. If I heard Mom’s, I’d probably bawl like a little kid. I quickly changed the subject. “What about you?” “What’s a high-school senior with a hundred and twenty days left until the college entrance exam supposed to do? Study.” Her tone was sharper than usual. Exam stress must have been hitting her hard. “How’s studying going?” “I bombed the July mock exam. I failed to manage my condition and missed even the easy questions. God, the more I think about it, the more annoyed I get.” “It’s fine. Just do well on the real thing. How many did you miss?” “Two.” “That’s still Grade 1.[^1] What about the other subjects?” “Two across all subjects.” “Huh?” “One in Korean history and one in math.” “…Two in total, across every subject? Are you serious?” “Obviously that’s what I meant.” *Smart little brat…* I knew she was good at studying, but I hadn’t realized she was this good. Thinking back on my own school grades, it really seemed like there was such a thing as dumping all the genes into one kid. “You study pretty well, huh?” “From your perspective, isn’t that really good?” “W-what kind of nonsense is that? I studied pretty well too, you know? You just don’t remember because you were in elementary school…” “Last week during a deep clean, I found your report card. There were so many Grade 7s I thought it was a slot machine that had hit the jackpot.” “You need some allowance, right? How much does makeup cost these days?” “That’s pathetic. Seriously.” *Cruel girl…* The call lasted more than ten minutes. I mostly listened. Hayeon rattled on about studying, school, and a boy she was interested in, her voice much brighter than it had been at first. I found myself getting oddly sentimental. *I really did come back.* Had I been dreaming? Or lost in a delusion? Only a day had passed in reality, yet utterly incomprehensible, inexplicable things had happened. But I decided to stop trying to understand them. *I’m back in reality now.* And I had to live in reality. My family was here. I was here. That was enough. I had simply dreamed a strange dream for a little while. The kind of dream that would fade on its own with time. “So I…” “Yeah.” Listening to my little sister chatter, I stood up. It was time to step out from beneath the old, rusted sign and go back to my room. * * * Bzzzt. Bzzzt. Seong Jinho cracked his bleary eyes open. The smartphone beside his pillow was vibrating. Six in the morning. The signal that started the day. “Oh, I’m dying.” It had been five years since he left home. The moldy smell that crept into his nose every morning had gotten pretty familiar. Eyes half shut, Seong Jinho shoved his cigarettes and lighter into his pocket and left the room. *Nothing wakes you up like a cigarette.* He shuffled up to the rooftop in his slippers. He’d just put a cigarette between his lips when— Thud. “Huh?” What was that? Wondering, he leaned over the railing, and a hunk of metal sitting in the recycling area right in front of him caught his eye. So did the well-built young man gazing at it. “Hey! Jin Taekyung!” At Seong Jinho’s shout, Jin Taekyung looked up. “What?” “You throwing that away?” The hunk of metal was the junk capsule Taekyung had picked up the day before. After using it for some ridiculous prank, he seemed to be taking it back out to throw away. *He’d been awfully serious for a prank like that… Ah, whatever. It was nonsense.* Seong Jinho gave a short laugh. “Why throw it away? Not going back to Murim?” “You believed that?” Jin Taekyung smiled back. But to Seong Jinho, who had watched him for a long time, the smile looked somehow awkward. *What’s with him?* Something felt off. As Seong Jinho stood there uneasily, Jin Taekyung waved and started down the hill. “Where are you going, you punk? Aren’t we eating breakfast together later?” “I have to work!” Jin Taekyung left without looking back. Seong Jinho took a drag from his half-burned cigarette. “That bastard’s really working hard…” Soon, Jin Taekyung disappeared from sight. Seong Jinho stubbed out his cigarette in a flowerpot and was about to leave when the junk capsule caught his eye. *He said the manufacturer was H Soft, right?* It was probably just some half-assed prank, but there was no harm in looking into it. [^1]: Korean mock exams use a 1–9 scale; Grade 1 is the highest.

#### Chapter 41 tail (verified mastered)

…
shirt was waiting in the lobby. Without preamble, he held out a contract with a blank face. “I’m from the Peace Guild. Read it and sign.” *This guy’s way of talking is seriously irritating.* I glared from the contract to the man’s face and back. “The settlement split is eight to two.” “After the raid, the proceeds are distributed fairly according to contribution. We take twenty percent of the amount you receive.” “And the base pay?” “Thirty.” “Thir…ty?” *Did this guy’s tongue get cut in half?* “Gate rank.” “E-rank.” “Rejected.” “The positions are full. You’ll be a porter.” The corner of my eye twitched. *What the hell did this guy just say?* “Por-ter?” “Is there a problem?” “Obviously.” The shirt guy glared down his nose at me. “What is it?” “I don’t have a pen.” “…” After a brief silence, I took the pen he handed me and scrawled my signature. The base pay was 300,000 won, and the settlement split was generous too. I’d flinched at the mention of an E-rank Gate, but I was only going as a porter, so it didn’t matter. I’d skin a few monsters, carry a pack for a while, and then we’d part ways in a good mood. *Peace Guild. I like the name already.* I’d been itching to sign so badly my fingers had almost cramped. “All signed.” “…” “So where are we going now? We taking a van?” “There’s a van waiting outside.” “Oh, that one? Looks nice. Bet the AC’s blasting too.” “…” “Guess I was last? There are already a few people here… Huh? Kkeokjeong hyung!” “Huh? Taekyung!” Im Kkeokjeong was waiting to load his bags into the bus’s trunk. He grinned wide. “You’re coming too. Great!” “Right? I guess I really do have a connection with you, hyung.” “Hahahaha!” “Ahahaha!” “…Let’s get going.” Maybe it was the heat, but the shirt guy’s face looked years older. * * * The bus pulled out. From the passenger seat, the shirt guy said we’d arrive within twenty minutes, then closed his eyes. Im Kkeokjeong introduced me to the others who’d been hired with us. “All right, everyone, say hello. This is a younger brother I know.” Now that I looked, they all knew each other. I dipped my head. “Hello. I’m Jin Taekyung.” “Oh, nice to meet you.” “Tall young fellow. Looks like he can fight.” There were three new people in all, men in their late thirties or early forties. In that warm atmosphere, Im Kkeokjeong explained. “These guys are all E-rank. I’ve known them a long time. Over ten years now.” “Yeah, about that long. Time sure flies.” Meaning they all had at least ten years in. I had enough experience that nobody was going to call me a rookie wherever I went, but these guys were on another level entirely. *Old-timer party.* People like them pulled their weight wherever they went. In a pinch, they were much better than a middling D-rank. “So what’s the young guy’s rank?” Here it came. The rank check. I answered carefully. “F-rank.” “Ah. That so? How many years?” “Seven.” “Hmm. That so?” The mood went lukewarm. If my first raid started like this, that would be a problem. I ran my mouth before it could settle. “I won’t be taking part in combat at all. I’m joining as a porter, so you don’t have to worry…” The three men stared at me blankly. “Why the extra explanation? We gonna eat you?” “Drop it. If he’s been knocking around for seven years, he knows enough.” “If Kkeokjeong hyung recommended him, that’s enough. Team Leader Choi must’ve thought he was all right too, or he wouldn’t have said yes.” *Recommended? Team Leader Choi?* I didn’t know the exact details, but I could more or less see how this had gone. Im Kkeokjeong had recommended me. To the shirt guy—Team Leader Choi. “W-what are you talking about?” Im Kkeokjeong waved his hands, his face bright red. The three men snickered. “It’s written all over him. How did that hyung ever get married?” “Good deeds are supposed to come to light. Why go through life hiding them?” “Right. You think so too, don’t you?” I nodded at once. “Of course. Thank you for looking out for me.” “Ahem. I just put in a word. Team Leader Choi made the decision.” Well, then… I’d thought of Im Kkeokjeong as one of the many people I’d crossed paths with for a moment and moved on from. Meeting him again, he was more guileless and warmhearted than I’d expected. *So that’s why the terms were so generous.* The way they kept saying Team Leader Choi, Team Leader Choi, I figured their friendship had played a part in my contract too. “I’ll work hard.” “I told you, Team Leader Choi made the decision!” The man in question answered Im Kkeokjeong’s awkward excuse. “Then let’s say I made the decision.” The shirt guy had opened his eyes at some point. No—Team Leader Choi. He spoke to us. “We’re almost there.” I turned my head. A four-meter-high Gate was drawing closer. At its center, a vortex of mana churned, ready to suck us in. *An E-rank Gate.* My first raid since coming back. [^1]: A famous Joseon-era bandit and folk hero; the nickname comes from his looks. [^2]: Yulmu tea is a sweet Korean grain drink, commonly served hot or cold.

## Korean source

```text
＃42화



게이트(Gate).

대격변이 남긴 가장 큰 흔적.

삼십여 년 전 마왕 아스모데우스가 침략 루트로 사용했던 그곳은, 헌터들의 생계 수단이자 마정석이라는 고차원 에너지 자원의 발굴 현장으로 전락한 지 오래였다.

“평화 길드 분들이시죠?”

입구에 나와 있던 작업복 차림의 중년인이 다가왔다.

게이트마다 배치된 게이트 관리청 소속의 공무원이다.

“네.”

최 팀장의 무뚝뚝한 대답에 공무원이 고개를 끄덕였다.

“딱 맞춰 오셨네요. 언제 진입하실 겁니까?”

“장비 갖추고 바로 들어가겠습니다.”

“2층에 대기실 있으니까 준비 마치고 내려오시면 됩니다. 그럼.”

우리는 최 팀장을 따라 이동했다. 관리청 공무원이 상주하는 2층짜리 건물은 낡을 대로 낡았는데, 대기실 역시 비슷한 상황이었다.

‘와 씨. 냄새 봐라.’

문을 열자마자 땀 냄새가 코를 찌른다. 녹슨 캐비닛과 꽉 찬 휴지통도 눈에 띄었다.

“여긴 좀 심하네. 환기도 안 시키나?”

“게이트 담당 공무원들이 그렇지 뭐. 괜히 꿀 보직이 아니여.”

나는 투덜거리는 소리를 뒤로하고 레이드 장비로 환복하기 시작했다. 가죽 갑옷에 가벼운 소재의 전투화. 마지막으로 길쭉한 케이스에서 창을 꺼내 쥐었다.

‘오랜만이네.’

손아귀에 딱 들어오는 이 감촉. 익숙하면서도 낯설다.

지난 한 달 동안 썼던 무기와는 확실히 차이가…… 아, 아니다. 더는 생각하지 말자.

‘이젠 다 잊어야지.’

괜히 멀쩡한 전투화 끈을 조이는 내게 임꺽정이 다가왔다.

그는 전신 갑옷과 거대한 타워 실드를 갖춘 메인 탱커의 모습이었다.

“준비 끝났어?”

“예. 뭐.”

나를 위아래로 훑어본 임꺽정이 혀를 내둘렀다.

“이 녀석 보게. 도대체 언제 적 장비야?”

“글쎄요. 처음 시작할 때 샀으니까 적어도 7년?”

초짜 시절, 동대문 지하 매장에서 큰맘 먹고 질렀더랬다. 가격도 정확히 기억한다. 198만 원.

‘지르고 나서 며칠 동안 잠도 제대로 못 잤지.’

헌터는 수입만큼 지출도 큰 직업이다. 그 지출의 대부분을 차지하는 게 장비 관련이고. 이게 다 게이트의 특수성 때문이다.

‘마나, 혹은 마력이 깃들지 않은 장비는 금방 망가지니까.’

그래서 가장 흔하게 쓰이는 방법이 게이트 몬스터에게 얻은 마정석을 재료로 장비를 제작하는 거다.

사용된 마정석의 등급이 높을수록 가격은 천정부지로 솟는다.

“7년? 세상에. 아무리 돈이 좋아도 쓸 때는 써야지. 목숨에 돈 아낄래?”

“음. 사정이 있었어요.”

굳이 말하고 싶지 않은 사정이다. 임꺽정은 걱정스러운 목소리로 말했다.

“오늘은 비전투 포지션이니 괜찮겠지만…… 조심해라.”

“네.”

대답하면서도 기분이 묘하다. 얼마 전까지 조심하라는 말을 입에 달고 살던 누군가가 떠올라서.

하지만 감상에 젖는 것도 잠시.

“다들 준비 끝나셨습니까?”

최 팀장의 등장에 나는 입을 딱 벌렸다.

저거 설마.

“붉은 드레이크 가죽 세트?”

“음.”

최 팀장의 얼굴이 굳었다. 명품관 카탈로그에서나 보던 거라 나도 모르게 그만 실수했다.

“아, 죄송합…….”

“별거 아닙니다. 다섯 종류의 마법과 B급 마정석을 재료로 만들었을 뿐이죠.”

“……?”

“강조하는 건 아니지만 다섯 종류의 마법과 B급 마정석이 재료입니다.”

“아, 네.”

“붉은 드레이크의 가죽이 인기가 좋은 건 특유의 윤기 때문인데, 보기에만 그럴듯하고 별 쓸모는 없습니다.”

최 팀장이 굳은 얼굴로 몸을 움직였다. 은은한 붉은 빛이 번뜩였다.

“하지만 매우 아름답죠.”

“…….”

“이만 내려갑시다.”

최 팀장이 먼저 대기실을 나가자 임꺽정이 다가와 말했다.

“저 친구 장비 알아봐 주는 거 엄청 좋아해.”

“아니 뭐, 이해는 가는데…… 왜 저래요?”

“몰라. 장비 덕후야. 전 재산 털어서 저거 사고 밤마다 입고 잔다는 소문도 있어.”

저 자식도 또라이구나.

나는 내심 한탄하며 오늘 레이드가 무사히 끝나길 빌었다.



* * *



“신청하신 인원이랑 다르군요.”

공무원은 불편한 표정이었다. 그럴 만도 하지. 이제 진입해야 하는데 인원이 전부 안 모였으니까.

‘도대체 얼마나 기다려야 하나.’

현재 게이트 앞에 집결한 인원은 여섯 명. 짐꾼으로 온 나를 제외하면 전투 인원은 다섯밖에 안 된다.

E급 게이트니까 최소한 동급의 헌터 다섯이 더 필요한데…… 평화 길드 놈들이 코빼기도 보이지 않으니 공무원 입장에서는 짜증이 날 수밖에.

“추가된 인원이 있으면 미리 말씀을 해 주셔야죠.”

응? 방금 뭐라고 한 거냐.

추가된 인원이라니?

“죄송합니다.”

최 팀장의 무뚝뚝한 사과에 공무원이 펜을 들어 서류에 좍좍 줄을 그었다.

“뭐 수정하면 되니까 큰 문제는 없는데…… 다음부턴 조심해 주십쇼.”

“예.”

큰 문제가 없기는 시발. 사람이 없잖아, 사람이!

나는 임꺽정의 옆구리를 쿡 찔렀다.

“형님. 다른 사람들은 언제 와요?”

“무슨 사람들?”

“평화 길드요.”

“최 팀장 있잖아.”

“네?”

“아, 말 안 했었나? 평화 길드, 신생이라 인원이 없어. 길드장 포함 세 명이 전부지. 으하하.”

……웃어?

“아니, 형님.”

“알아, 인마. 근데 걱정 안 해도 돼.”

내 어깨를 툭 친 임꺽정이 서류에 사인 중인 최 팀장을 가리켰다.

“저 양반, C급 헌터거든.”

“아. C급…….”

나는 입을 다물었다. 최 팀장이 C급 헌터라면 문제없다. 아니, E급 헌터 열 명보다 훨씬 낫다. 그는 나 같은 하급 헌터와 격이 다른 ‘중급 헌터’니까.

‘명품 장비 걸쳤을 때부터 알아차렸어야 했는데.’

고급 아파트를 몸에 두르고 다니는 인간이다. 어지간한 하급 헌터들은 전 재산을 열 번 털어도 못 사는 가격.

최 팀장의 뒷모습에서 은은한 후광이 비쳤다.

“서명 확인 바랍니다.”

공무원에게 펜을 넘겨주는 모습도 어쩜 저렇게 우아하냐.

작은 움직임조차 부티가 좔좔 흐르는 것 같다.

저게 바로 C급 헌터의 품격인가.

‘존나 멋있어.’

의형제 맺고 싶다. 게이트 아래에서 게이결의, 아니 게이트결의 맺고 싶다.

“자, 그럼 이제 들어갈…… 뭡니까?”

최 팀장이 흠칫한 얼굴로 나를 바라봤다.

“아뇨. 그냥 멋있어서요.”

“네?”

“장비. 멋있다고요.”

그 순간, 최 팀장의 입꼬리가 꿈틀거렸다.

“별거 아닙니다. 다섯 종류의 마법과 B급 마정석을 재료로…….”

친해지고 싶은 또라이다.



* * *



게이트를 향해 한 걸음을 내디뎠다.

쏴아악-

익숙한 느낌이 전신을 감싼다. 서늘하면서 끈적거리는 마력 특유의 기운. 그리고 뒤바뀐 풍경.

“동굴이군요.”

최 팀장의 말처럼 이번 레이드 장소는 동굴이었다. 습기를 머금은 벽면은 축축했고 사방은 옅은 어둠에 잠겨 있었다.

“태경 씨. 손전등 꺼내세요.”

“넵.”

나는 재빨리 배낭을 내려놨다. 게이트 진입 직전, 최 팀장에게 건네받은 짐꾼용 가방이다. 겉보기에는 평범하지만 무려 공간 확장에 경량화 마법까지 걸려 있는 고가의 물품.

“여기 있습니다. 손전등.”

달라니까 주긴 하는데, 내 경험상 그리 좋은 방법은 아니다. 간편한 대신 빛이 사라질 경우 갑작스러운 어둠에 적응하지 못하기 때문이다.

차라리 잠깐 대기하면서 눈에 어둠이 익기를 기다리는 게 훨씬…….

딸깍.

“빛이 있으라. 라이트(Light).”

슈웅. 손전등으로부터 축구공만 한 빛 덩어리가 튀어나와 동굴 천장에 철썩 달라붙는다.

“……마법?”

“주문만 영창하면 바로 발동되는 내장 마법입니다. 지속력이 꽤 길어서 앞으로 서너 시간은 문제없어요. M사에서 한정판으로 구매한 물건인데…….”

지켜보던 임꺽정이 한마디로 축약했다.

“엄청 비싸.”

최 팀장의 얼굴이 살짝 어두워지는 건 기분 탓인가, 아니면 그림자 때문인가. 어쨌건 덕분에 레이드가 한결 쉬워졌다.

‘역시 돈이 최고야.’

세상은 자본이 지배하고 게이트도 마찬가지다. 돈 있는 놈은 마법 장비로 편하게 싸우고 없는 놈은 횃불 들어야 한다.

“각자 위치로.”

최 팀장의 지시에 사람들은 즉각 반응했다. 탱커 포지션인 임꺽정, 그리고 다른 E급 헌터가 선두에 섰고 최 팀장이 그다음. 짐꾼인 나와 원거리 딜러 둘이 가장 뒤에 섰다.

“이동.”

우리는 천천히 앞을 향해 나아가기 시작했다.

환한 마법의 불빛이 길을 밝혀 주었다.

“…….”

하나 갖고 싶다.



* * *



“키이이잇!”

어둠 속에 웅크리고 있던 녀석들이 괴성과 함께 모습을 드러냈다. 녹색 피부에 짧은 몸통. 흉측해 보이는 팔다리.

일반 고블린의 상위종인 홉 고블린(Hob goblin)이다.

‘머릿수는 대략 서른.’

고작 다섯 명으로는 힘든 싸움이 될 것이다.

‘하지만 C급 헌터가 있으면 이야기가 달라지지.’

거기에 다른 네 명은 최소 십수 년 경력의 E급 베테랑.

나는 멀찍이 물러서서 전투를 구경했다.

“원거리!”

최 팀장의 말이 떨어짐과 동시에 화살이 쏘아졌다. 한 발에 한 놈씩. 급소를 파고드는 화살에 방패가 없는 홉 고블린들이 우수수 쓰러진다.

“키잇!”

“어이고, 방패병 나왔다. 어쩔까요?”

“대기.”

최 팀장이 이어 말했다.

“탱커 전진.”

두꺼운 전신 갑옷에 타워 실드를 든 탱커들이 움직였다. 임꺽정도 그렇고, 다른 한 사람도 190센티가 넘는 거구들이라 위압감이 장난이 아니다.

“키이이잇!”

하지만 몬스터는 괜히 몬스터가 아니다. 머릿수만 믿은 홉 고블린들이 벌 떼처럼 달려들었다.

하지만…….

“어쭈.”

뻐버벙!

크고 아름다운 타워 실드에 피떡이 되어 날아갔다. 기세를 탄 임꺽정이 철퇴를 파리채처럼 휘두를 때마다 팔다리가 아작 나고 머리통이 박살 난다.

“요놈! 요놈!”

……무슨 두더지 게임이야?

‘역시 고인물.’

네 명 모두 과하지 않은 선에서 자신의 포지션을 지키면서 적들의 숫자를 착실하게 줄이고 있다.

물러설 때와 나아갈 때를 아는 건 풍부한 경험에서 우러나온 전투 지능이다.

“전원 위치 고수.”

그리고 한 사람.

지금껏 전투의 흐름을 조율하던 그가 움직였다.

“나머진 제가 맡겠습니다.”

동시에 갑옷을 타고 번뜩이는 붉은 선이 스무 마리의 홉 고블린 사이로 파고들었다.

서걱-

깔끔한 궤적과 함께 목이 솟구친다. 순식간에 벌어진 일에 놈들은 제대로 반응하지 못했다.

“키이이?”

서걱. 서걱. 서걱.

칼날은 멈추지 않았다. 무자비하고 효율적으로 적들의 급소를 꿰뚫고 베어 냈다. 그것은 더 이상 전투가 아니었다.

학살. 단 한 명의 인간이 이십여 마리의 몬스터를 상대로 벌이는 학살이다.

‘이게 C급 헌터.’

그의 속도, 근력. 모두 보인다. 그리고 느꼈다.

‘역시 강해.’

F급에 불과한 나로서는 감히 넘볼 수 없다. 무려 세 단계 높은 중급 헌터니까. 그건 노력으로는 결코 메울 수 없는, 넓은 강이자 높은 벽이다.

하지만 동시에 어떤 의문이 고개를 들었다.

‘만약 무림이라면 어땠을까.’

최 팀장은 분명 강하다. C급 헌터에 어울리는 능력과 풍부한 경험을 갖췄다. 그러나 이곳이 무림이라면. 또 그가 무림인이라면…….

‘내가 더 강해.’

빠르고 힘 있는 동작이지만 그뿐이다. 그는 무공도 익히지 않았고, 마나를 효율적으로 사용하지도 못한다.

고작해야 일류. 무림에서의 그는 딱 그 정도다.

‘하지만 이게 현실이지.’

나도 모르게 입술을 깨물었다.

중급 헌터와 최하급 헌터. 중급 헌터가 값비싼 장비를 입고 몬스터들을 학살할 때 최하급 헌터는 멍하니 바라볼 뿐이다.

짐꾼이라는 역할로.

“끼이이잇…….”

마지막 홉 고블린이 쓰러졌다. 놈의 가슴에서 검을 빼낸 최 팀장과 시선이 부딪쳤다.

“태경 씨. 부산물 처리 부탁합니다.”

“…….”

“태경 씨?”

그에게 말하고 싶었다. 내가 당신보다 강하다고.

하지만 끝내 말하지 못한 것은 이게 내 현실이기 때문이다.

“……고생하셨습니다.”

나는 당신보다 강‘했었’다.
```

## Current accepted English baseline

```markdown
# Chapter 42

A Gate.

The greatest scar left behind by the Great Cataclysm.

More than thirty years ago, Demon King Asmodeus had used them as an invasion route. These days, they had long since been reduced to a livelihood for Hunters and excavation sites for a higher-dimensional energy resource called Magic Gems.

“Are you with the Peace Guild?”

A middle-aged man in work clothes came over from the entrance.

He was a civil servant from the Gate Management Office, posted at every Gate.

“Yes.”

At Team Leader Choi’s curt reply, the civil servant nodded.

“You’re right on time. When will you be entering?”

“We’ll gear up and go in right away.”

“There’s a waiting room on the second floor. Come down when you’re ready. Right, then.”

We followed Team Leader Choi. The two-story building where the Management Office civil servant was stationed was as run-down as a building could get, and the waiting room wasn’t much better.

*Damn. Get a load of that smell.*

The moment we opened the door, the stench of sweat hit me. Rusty cabinets and an overflowing trash can jumped out at me too.

“This place is pretty bad. Don’t they even air it out?”

“That’s how Gate officials are. It’s not called a cushy post for nothing.”

I left the grumbling behind and started changing into my raid gear. Leather armor and lightweight combat boots. Last, I drew a spear from its long case and gripped it.

*It’s been a while.*

That snug fit in my hand felt familiar and strange at the same time.

It was definitely different from the weapon I’d used over the past month… Ah, no. I shouldn’t think about that anymore.

*I have to forget all of it now.*

I was tightening the perfectly fine laces on my combat boots for no reason when Im Kkeokjeong came over.

He looked every bit the main tank, in full-body armor with a massive tower shield.

“Are you ready?”

“Yes. Pretty much.”

Im Kkeokjeong looked me up and down, then clicked his tongue.

“Look at this guy. How old is that equipment, even?”

“Who knows? I bought it when I first started, so at least seven years?”

Back when I was a rookie, I’d splurged on it at an underground shop in Dongdaemun.[^1] I still remembered the exact price.

1.98 million won.

*I couldn’t sleep properly for days after buying it.*

Hunting was a job where the expenses ran about as high as the pay. Most of that spending went to equipment. All because of how Gates worked.

*Gear that isn’t imbued with mana falls apart in no time.*

So the most common method was to craft equipment from Magic Gems taken from Gate monsters.

The higher the Grade of Magic Gem used, the more the price shot through the roof.

“Seven years? Good grief. No matter how much you like money, you have to spend it when you need to. You going to pinch pennies with your life on the line?”

“Hmm. I had my reasons.”

Reasons I didn’t particularly want to talk about. Im Kkeokjeong’s voice was worried.

“You’ll be in a noncombat position today, so you should be fine… but be careful.”

“Yes.”

Even as I answered, I felt strange. Someone who’d had “be careful” on their lips constantly until just recently came to mind.

But the sentimentality didn’t last.

“Is everyone ready?”

When Team Leader Choi appeared, my jaw dropped.

*No way.*

“Is that a Red Drake leather set?”

“Hmm.”

Team Leader Choi’s face hardened. I’d only ever seen gear like that in luxury-store catalogs, so the words slipped out before I could stop them.

“Ah, sorry…”

“It’s nothing. It’s only made with five types of magic and B-grade Magic Gems.”

“…”

“I’m not emphasizing it, but the materials are five types of magic and B-grade Magic Gems.”

“Ah. Right.”

“Red Drake leather is popular because of its distinctive sheen, but that’s all for show. It isn’t actually that useful.”

Team Leader Choi moved, his face still stiff. A faint red glow flashed across him.

“But it is very beautiful.”

“…”

“Let’s head downstairs.”

Team Leader Choi left the waiting room first. Im Kkeokjeong came over.

“That guy really loves it when people recognize his equipment.”

“I mean, I get it, but… why is he like that?”

“No idea. He’s an equipment nut. There’s even a rumor he blew his entire fortune on that set and sleeps in it every night.”

*So this guy’s a nutjob too.*

I sighed inwardly and hoped today’s raid would end in one piece.

* * *

“This isn’t the number of people you registered.”

The civil servant looked uncomfortable. Fair enough. We were supposed to enter soon, and the party still wasn’t all there.

*How long are we going to have to wait?*

Six people had gathered in front of the Gate. Barring me, the porter, there were only five combatants.

It was an E-rank Gate, so you needed at least five more Hunters of the same rank… and with those Peace Guild bastards nowhere in sight, of course the civil servant was pissed.

“If additional personnel have been added, you need to inform us in advance.”

*Huh? What did he just say?*

Additional personnel?

“I’m sorry.”

At Team Leader Choi’s curt apology, the civil servant picked up his pen and struck several lines through the paperwork.

“We can just amend it, so it’s not a major problem… but please be careful next time.”

“Yes.”

*Not a major problem, my ass. There aren’t any people!*

I poked Im Kkeokjeong in the ribs.

“Hyung. When are the others getting here?”

“What others?”

“The Peace Guild.”

“Team Leader Choi is here.”

“What?”

“Oh, did I not tell you? The Peace Guild is new, so it’s short on people. There are only three of us, including the Guild Master. Hahaha.”

…You’re laughing?

“Come on, hyung.”

“I know, punk. But you don’t have to worry.”

Im Kkeokjeong patted my shoulder and pointed at Team Leader Choi, who was signing the paperwork.

“That man’s a C-rank Hunter.”

“Oh. C-rank…”

I shut my mouth.

If Team Leader Choi was a C-rank Hunter, there was no problem. No—he was far better than ten E-rank Hunters. He was a mid-rank Hunter, in a completely different league from a low-rank Hunter like me.

*I should’ve realized the moment I saw him in that luxury gear.*

This was a man walking around with a high-end apartment wrapped around his body. A price most low-rank Hunters couldn’t afford even if they drained their entire fortunes ten times over.

A faint halo seemed to shine from Team Leader Choi’s back.

“Please verify the signature.”

Even the way he handed the pen back to the civil servant was elegant.

Even his smallest movements seemed to drip with class.

*So this is the dignity of a C-rank Hunter.*

*That’s fucking cool.*

I wanted to become sworn brothers with him. To swear a gay oath beneath the Gate—no, a Gate oath.

“All right, then. Let’s go in… What is it?”

Team Leader Choi looked at me, startled.

“No. I just thought you looked cool.”

“Excuse me?”

“The equipment. I said it looks cool.”

At that moment, the corner of Team Leader Choi’s mouth twitched.

“It’s nothing. It’s only made with five types of magic and B-grade Magic Gems…”

*A nutjob I wanted to get along with.*

* * *

I took a step toward the Gate.

Whoosh—

A familiar sensation wrapped around me. The cool, sticky energy unique to mana. Then the scenery flipped.

“It’s a cave.”

As Team Leader Choi said, this raid’s location was a cave. The walls were damp with moisture, and faint darkness lay over everything around us.

“Mr. Taekyung. Take out a flashlight.”

“Yes.”

I quickly set down my backpack. It was a porter’s bag Team Leader Choi had handed me just before we entered the Gate. It looked ordinary on the outside, but it was an expensive item enchanted with both space expansion and weight-reduction magic.

“Here. A flashlight.”

I handed it over since he’d asked, but in my experience it wasn’t the best method. Convenient, sure, but if the light vanished, you couldn’t adapt to the sudden dark.

It was much better to wait a little and let your eyes get used to the darkness…

Click.

“Let there be light. Light.”

Whoosh. A ball of light the size of a soccer ball shot out of the flashlight and slapped itself against the cave ceiling.

“…Magic?”

“It’s built-in magic that activates as soon as you chant the spell. It lasts quite a long time, so three or four hours shouldn’t be a problem. It’s a limited edition I bought from Company M, but…”

Im Kkeokjeong, who had been watching, boiled it down to one line.

“It’s crazy expensive.”

Was Team Leader Choi’s face darkening a little just my imagination, or was it the shadows? Either way, the raid had gotten a lot easier thanks to it.

*Money really is the best.*

The world was ruled by capital, and Gates were no different. People with money fought easy with magic equipment; people without it had to carry torches.

“Take your positions.”

At Team Leader Choi’s command, everyone moved at once. Im Kkeokjeong and another E-rank Hunter took the lead as tanks, with Team Leader Choi behind them. I, the porter, and the two ranged dealers stood at the very back.

“Move.”

We started advancing slowly.

The bright magic light lit the path ahead.

“…”

*I want one.*

* * *

“Kiiiieet!”

The creatures that had been crouched in the darkness showed themselves with shrill cries. Green skin. Short torsos. Limbs that looked grotesque.

They were Hobgoblins, a higher species of ordinary goblin.

*About thirty of them.*

With only five people, this would be a hard fight.

*But a C-rank Hunter changes the story.*

On top of that, the other four were veteran E-rank Hunters with at least ten-odd years of experience each.

I hung back and watched the fight.

“Ranged!”

The moment Team Leader Choi gave the order, arrows flew. One shot, one kill. The arrows punched into vital points, and the unshielded Hobgoblins dropped in heaps.

“Kiit!”

“Oof, shield-bearers. What should we do?”

“Hold.”

Team Leader Choi went on.

“Tanks, advance.”

The tanks in thick full-body armor moved forward with their tower shields. Im Kkeokjeong and the other man were both huge, over 190 centimeters, so the intimidation factor was no joke.

“Kiiiieet!”

But monsters were monsters for a reason. Trusting in their numbers, the Hobgoblins charged like a swarm of bees.

But then—

“Well now.”

Bam!

They turned to bloody pulp against those big, beautiful tower shields and went flying. Riding that momentum, Im Kkeokjeong swung his mace like a flyswatter, wrecking limbs and smashing heads.

“You punk! You punk!”

…What was this, whack-a-mole?

*Old-timers, as expected.*

All four of them kept to their roles without overdoing it, steadily cutting the enemy numbers down.

Knowing when to fall back and when to push in was combat intelligence born of plenty of experience.

“Everyone, hold your positions.”

And then one man.

The man who had been directing the flow of battle until now moved.

“I’ll handle the rest.”

At the same time, a red line flashing along his armor plunged through the twenty Hobgoblins.

Slash—

A head sprang into the air along a clean arc. The monsters couldn’t react in time to something that happened so fast.

“Kiiie?”

Slash. Slash. Slash.

The blade did not stop. Merciless and efficient, it pierced and cut through vital points. This was no longer a battle.

It was a massacre. A massacre of some twenty monsters by a single human.

*This is a C-rank Hunter.*

I could see his speed, his strength. All of it. And I felt it.

*He really is strong.*

As a mere F-rank, I couldn’t even dream of matching him. He was a mid-rank Hunter three full stages above me. A wide river and a high wall that effort alone could never bridge.

But at the same time, a question surfaced.

*What if this were Murim?*

Team Leader Choi was definitely strong. He had the ability befitting a C-rank Hunter, and plenty of experience.

But if this were Murim… if he were a man of Murim…

*I’d be stronger.*

His movements were fast and powerful, but that was all. He hadn’t learned martial arts, and he didn’t use mana efficiently either.

At best, he was first-rate. In Murim, that was exactly where he would stand.

*But this is reality.*

I bit my lip without realizing it.

A mid-rank Hunter and the lowest-rank Hunter.

While the mid-rank Hunter wore expensive equipment and slaughtered monsters, the lowest-rank Hunter could only stare blankly.

In the role of a porter.

“Kiiieet…”

The last Hobgoblin fell. Team Leader Choi pulled his sword from its chest, and our eyes met.

“Mr. Taekyung. Please handle the byproducts.”

“…”

“Mr. Taekyung?”

I wanted to tell him I was stronger than he was.

But in the end I couldn’t. This was my reality.

“…Thank you for your hard work.”

I *used to be* stronger than you.

[^1]: Dongdaemun is Seoul’s major wholesale-market district.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 42`.

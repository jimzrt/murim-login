# Master Edit Task — Chapter 41

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
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 임꺽정 | **Im Kkeokjeong** |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |

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

#### Chapter 39 tail (verified mastered)

…
he get out?* Jinho hyung sighed when he saw me standing there flustered. “What are you doing?” “Uh, uh?” “The power isn’t even on. What game were you playing?” What was that supposed to mean? “The power isn’t on?” “Move.” While I was still stammering, Jinho hyung came out the door, bent down under the capsule, and picked something up. “What does this look like to you?” A cord. An unplugged power cord. *Was I seeing things?* I scrubbed at my eyes furiously, but nothing changed. “Why is this…” “Taekyung. Jin Taekyung. You poor, pathetic soul.” Jinho hyung spoke with a distant look on his face. “Go to a mental hospital as soon as the sun comes up. I’m going back to my room.” He tossed the power cord aside and walked off. I stared blankly at his back. The power cord hadn’t even been plugged in. *Then what was the game I played?* I felt like I’d been bewitched by a ghost. Goose bumps rose all over my body. * * * I lay on the bed and thought. *Am I crazy?* I’d played a game for thirty days in a capsule that hadn’t even been plugged in. I could understand Jinho hyung’s reaction. But everything that had happened there… *It was all real.* Jin Wikyung, Wolhwa, Hyuk Mujin, and the Head Elder. I remembered every NPC’s face, the way they spoke, and how they acted. It hadn’t been a delusion I’d cooked up on my own. *Then what’s the problem?* There was only one answer. The problem was the game capsule built twenty-seven years ago—a piece of junk that should have been retired long ago and put in a museum. The date of manufacture was suspicious, too. January 1, 2020. The day the Demon King Asmodeus fell at humanity’s hands. *Who the hell would’ve been making capsules back then?* It was an era when hundreds of millions of people had died in the five-year Great War, and monsters had roamed downtown. In my opinion, the bastards who heard the breaking news that the Demon King had fallen and fired up a factory going, *All right, let’s make game capsules now!* belonged in court. *Back then, I thought it was a misprint.* I froze. *A misprint?* *The product manual!* How could I have forgotten something so important? What an idiot. I shot to my feet and started turning the room upside down. At last, I found a familiar little booklet under the bed. > **Product User Manual** > > **Product name:** Virtual Reality Access Device > **Model name:** Ark - 2020 > **Manufacturer:** H Soft > **Date of manufacture:** January 1, 2020 Then the next page. > **Precautions** > > - The player cannot log out at will. > > - If the player dies during play, resurrection is impossible. A month ago—no, three hours ago—I had thrown the booklet aside at this point. This time was different. With trembling hands, I turned to the final page. > **Key Features** > > - A custom capsule made for one person only! Once a user is registered, the capsule is permanently bound to that user until death. > > - Time-ratio adjustment for comfortable play! Upon login, time in reality passes very slowly. The reverse is also true. > > - Character Synchronization System! By synchronizing with their character, the user experiences a greater sense of unity. “What the hell is this?” My eyes could read the words, but my brain refused to process them. I started again from the beginning. *First, permanent binding.* It meant exactly what it said: it was mine until I died. Once I got some answers, I decided, I was going to smash that goddamn capsule to pieces. *Next, the time ratio.* That was the part I’d been most curious about. But instead of an exact figure, all it had was the vague phrase *passes very slowly*. It said the reverse was true as well, so time in the game had to be passing now too, however slowly. *Then is the war still going on?* Jin Wikyung came to mind. The Head Elder’s betrayal was already a given, and he would try to stab Wikyung in the back at the critical moment. Had Hyuk Mujin and the reconnaissance squad gotten that news to him? *Ah, that’s still a long way off. The time ratio has reversed.* More than that, I had my own crisis staring me in the face. I checked the last key feature. Unlike the ones before it, I couldn’t understand this no matter how many times I read it. *Synchronize with a character?* Just in case, I even looked it up in a Korean dictionary. It meant exactly what I thought it did. That only made it sound crazier. *How the hell do you synchronize with a game character?* I couldn’t make any sense of it. In the end, all I’d done was add another question. One thing was certain: I wasn’t crazy. I flopped onto the bed and read the front of the booklet again. “Manufacturer. H Soft.” In the end, every road led to the same place. If I investigated these bastards, something was bound to turn up. I searched the internet for H Soft, but aside from a porn studio with the same name, I couldn’t find a thing. “…” First, I needed to lock the door and think.

#### Chapter 40 tail (verified mastered)

…
Goshiwon. I sat beneath the old, rusted sign and pulled out my smartphone. The other end picked up almost before it could ring. Click. “Yeah. Why?” My one and only nemesis—no, my younger sister, Hayeon. The moment I heard that uniquely bratty voice of hers, my throat closed up. “Hello?” “…Yeah.” “Why’d you call?” “Just. I wanted to hear your voice.” A deathly silence followed. “I’m hanging up.” “No, wait. Wait!” “Three seconds. What’s your business.” *That damn girl…* Right. This was Jin Hayeon. Thanks to her, the tear ducts that had gotten a little moist dried out like sand around the pyramids. “What’s Mom doing?” “She went out. Said she had an errand. Call her if you’re curious.” I deliberately didn’t. Even this brat’s voice was enough to choke me up. If I heard Mom’s, I’d probably bawl like a little kid. I quickly changed the subject. “What about you?” “What’s a high-school senior with a hundred and twenty days left until the college entrance exam supposed to do? Study.” Her tone was sharper than usual. Exam stress must have been hitting her hard. “How’s studying going?” “I bombed the July mock exam. I failed to manage my condition and missed even the easy questions. God, the more I think about it, the more annoyed I get.” “It’s fine. Just do well on the real thing. How many did you miss?” “Two.” “That’s still Grade 1.[^1] What about the other subjects?” “Two across all subjects.” “Huh?” “One in Korean history and one in math.” “…Two in total, across every subject? Are you serious?” “Obviously that’s what I meant.” *Smart little brat…* I knew she was good at studying, but I hadn’t realized she was this good. Thinking back on my own school grades, it really seemed like there was such a thing as dumping all the genes into one kid. “You study pretty well, huh?” “From your perspective, isn’t that really good?” “W-what kind of nonsense is that? I studied pretty well too, you know? You just don’t remember because you were in elementary school…” “Last week during a deep clean, I found your report card. There were so many Grade 7s I thought it was a slot machine that had hit the jackpot.” “You need some allowance, right? How much does makeup cost these days?” “That’s pathetic. Seriously.” *Cruel girl…* The call lasted more than ten minutes. I mostly listened. Hayeon rattled on about studying, school, and a boy she was interested in, her voice much brighter than it had been at first. I found myself getting oddly sentimental. *I really did come back.* Had I been dreaming? Or lost in a delusion? Only a day had passed in reality, yet utterly incomprehensible, inexplicable things had happened. But I decided to stop trying to understand them. *I’m back in reality now.* And I had to live in reality. My family was here. I was here. That was enough. I had simply dreamed a strange dream for a little while. The kind of dream that would fade on its own with time. “So I…” “Yeah.” Listening to my little sister chatter, I stood up. It was time to step out from beneath the old, rusted sign and go back to my room. * * * Bzzzt. Bzzzt. Seong Jinho cracked his bleary eyes open. The smartphone beside his pillow was vibrating. Six in the morning. The signal that started the day. “Oh, I’m dying.” It had been five years since he left home. The moldy smell that crept into his nose every morning had gotten pretty familiar. Eyes half shut, Seong Jinho shoved his cigarettes and lighter into his pocket and left the room. *Nothing wakes you up like a cigarette.* He shuffled up to the rooftop in his slippers. He’d just put a cigarette between his lips when— Thud. “Huh?” What was that? Wondering, he leaned over the railing, and a hunk of metal sitting in the recycling area right in front of him caught his eye. So did the well-built young man gazing at it. “Hey! Jin Taekyung!” At Seong Jinho’s shout, Jin Taekyung looked up. “What?” “You throwing that away?” The hunk of metal was the junk capsule Taekyung had picked up the day before. After using it for some ridiculous prank, he seemed to be taking it back out to throw away. *He’d been awfully serious for a prank like that… Ah, whatever. It was nonsense.* Seong Jinho gave a short laugh. “Why throw it away? Not going back to Murim?” “You believed that?” Jin Taekyung smiled back. But to Seong Jinho, who had watched him for a long time, the smile looked somehow awkward. *What’s with him?* Something felt off. As Seong Jinho stood there uneasily, Jin Taekyung waved and started down the hill. “Where are you going, you punk? Aren’t we eating breakfast together later?” “I have to work!” Jin Taekyung left without looking back. Seong Jinho took a drag from his half-burned cigarette. “That bastard’s really working hard…” Soon, Jin Taekyung disappeared from sight. Seong Jinho stubbed out his cigarette in a flowerpot and was about to leave when the junk capsule caught his eye. *He said the manufacturer was H Soft, right?* It was probably just some half-assed prank, but there was no harm in looking into it. [^1]: Korean mock exams use a 1–9 scale; Grade 1 is the highest.

## Korean source

```text
＃41화



헌터 인력 사무소.

말이 사무소지 빌딩이다. 역세권 노른자위 땅에 세운 이 6층 빌딩에는 하루에도 수백 명의 헌터들이 드나들었다.

‘오랜만이네.’

새벽인데도 불구하고 로비는 인산인해였다.

긴 줄을 거쳐 창구에 도착하자 여직원이 사무적인 태도로 물었다.

“인력 사무소는 처음이신가요?”

“아뇨, 등록되어 있습니다.”

“성함이?”

“진태경입니다.”

초짜 시절이었다. 헌터 훈련소를 우수한 성적으로 수료했지만 나 같은 F급 헌터를 필요로 하는 곳은 거의 없었고, 몇몇 중소 길드가 적선하듯 내민 계약서는 날강도 수준이었다.

그래서 찾은 곳이 이곳이었다. 지역은 달랐지만.

“일산 지점에 기록이 남아 있네요. 명단에 올렸으니 1층 강당에서 대기해 주세요.”

“네.”

이 6층 빌딩은 그 자체로 피라미드다. 1층은 E급과 F급을 수용하고, 2층은 최소 D급부터 발을 들일 수 있다.

너무 대놓고 차별하는 것 아니냐며 분노하는 사람도 있지만, 차별하는 거 맞다.

‘한두 번도 아니고.’

이 바닥에서 7년을 버티면서 온갖 더러운 꼴을 다 겪었다. 찬밥 더운밥 가릴 시기는 오래전에 지났지.

그런 생각과 함께 걸음을 뗀 순간이었다.

“어, 이게 누구야!”

걸걸한 목소리에 돌아보니 웬 털북숭이가 나를 보며 활짝 웃고 있었다.

“태경이. 진태경 맞지?”

“꺽정 아저씨?

이 아저씨, 아직 살아 있었어?



* * *



성은 임. 이름은 까먹었다. 7년 전 딱 한 번, 자기소개할 때 들은 것 같은데 기억이 나지 않는다.

다만 산적을 연상시키는 외모라 모두 그를 임꺽정이라고 불렀다.

“그동안 어떻게 지냈냐?”

“F급 헌터 사는 게 거기서 거기죠. 아저씨는요?”

“아저씨는 무슨.”

임꺽정이 넉넉한 웃음을 지어 보였다.

“형님이라고 불러라. 나이 차이도 얼마나 안 나는데.”

몇 살 차이였더라. 가물가물하다.

“형님, 혹시 나이가?”

“마흔다섯.”

“…….”

저 당당함 뭔데.

하지만 그동안 갈고 닦은 처세술이 빛을 발했다. 나는 가까스로 억지 미소를 지을 수 있었다.

“그러네요. 그냥 형님이라고 부를게요.”

“그래, 동생. 으하하하!”

강당 안에 호탕한 웃음이 울려 퍼졌다. 백 명에 가까운 사람들의 시선이 붙었다가 떨어진다.

‘그냥 못 들은 척하고 갈걸.’

어떻게 보면 얕은 인연이다. 반년 남짓 일산 사무소에서 매일같이 마주치고, 가끔 같이 일도 하고. 딱 그 정도 인연.

‘사람은 좋은데…….’

가끔 옆에 있으면 부끄러울 때가 있다. 지금처럼.

“여기 율무차가 끝내줘. 강당 의자도 푹신하고.”

율무차를 한입에 털어 넣은 임꺽정이 의자를 한껏 젖혔다.

보아하니 한두 번 들락거린 솜씨가 아니다.

“자주 오시나 봐요?”

“매일은 아니고 가끔 들르는 정도지. 결혼하고 자식도 생기니까 몸을 사리게 되더라고. 흐흐.”

못 본 사이에 가정을 꾸린 모양이다. 내가 축하 인사를 건네자 임꺽정이 머리를 긁적였다.

“그게 뭐 대단한 일이라고.”

겸양을 떨지만 대단한 건 대단한 거다. 헌터, 그것도 F급 헌터로 20년 넘게 활동하면서 가정까지 일구다니.

어쩌면 눈앞의 임꺽정이 미래의 내 모습일지도 모른다는 생각이 들었다.

‘물론 저 나이까지 살아 있어야 가능한 거지만.’

헌터는 오래 할 직업이 못 된다. 그래서 연금 지급 대상인 10년을 채우자마자 은퇴하는 이들도 부지기수다.

“그나저나 너도 이제 제법 티가 난다? 처음 봤을 때는 완전히 얼어서 말도 잘 못하더니.”

“당연하죠. 나름 7년 찬데.”

“그럼 그때 이후로 계속 사무소만 돈 거야? 그럭저럭 괜찮은 조건으로 중소 길드랑 계약하지 않았나? 소, 소…… 거기 이름이 뭐더라.”

“소풍 길드요. 그저께 잘렸어요.”

임꺽정이 애써 웃었다.

“으하하! 잘했어. 길드 이름도 구리네. 소풍이 뭐냐 소풍이. 게이트에 소풍 가는 것도 아니고.”

“아뇨, 그 소풍이 아니라 지역명인데요. 부천 소풍터미널 근처라 소풍 길드.”

“아…….”

그 후로 이어지는 임꺽정과의 대화는 제법 유익했다. 어쨌건 그는 인력 사무소의 단골이었고 괜찮은 정보와 자신만의 노하우를 가진 베테랑 헌터였으니까.

“사무소 수수료 10%. 뭐 이거야 기본이고, 여기 꽤 타율이 좋아.”

타율. 고용될 확률을 이르는 이 바닥 속어다. 당장 일당 치기가 목적인 나로서는 희소식이었다.

“저희 같은 F급 헌터도요?”

“어? 응. 그렇지.”

뭐야, 저 어색한 표정은?

하지만 뭔가를 더 물어보기도 전에 강당에 설치된 스피커에서 음성이 흘러나왔다.



- E급 헌터 임혁준. 임혁준 님께서는 로비로 나와 주시기 바랍니다.



오전 여섯 시 반.

드디어 첫 타자가 나왔다. 그리고 E급 헌터들이 다 빠져나간 후에야 내 차례가 돌아올 것이다.

“역시 E급 먼저 나가는…… 형님 어디 가세요?”

“먼저 갈게.”

방어구와 무기가 든 커다란 가방을 둘러맨 임꺽정, 아니 임혁준이 허허 웃었다.

‘어쩐지 표정이 이상하더라니.’

저 양반, 못 본 사이 정말 피나는 노력을 한 모양이다.

고작 한 단계지만 F급의 잠재력으로 승급하는 건 정말 쉬운 일이 아니니까.

“또 보자.”

“네. 또 봬요.”

그가 강당을 빠져나간 것이 시작이었다. 스피커는 작정한 듯 사람들의 이름을 쏟아 내기 시작했다.

E급 누구누구, E급 누구, E급…… 염병, 여긴 나만 F급이냐?

슬슬 초조해지려던 그 순간이었다.



- F급 헌터 진태경. 진태경 님께서는 로비로 나와 주시기 바랍니다.



떴다!



* * *



“진태경 씨?”

로비에는 흰색 린넨 셔츠를 입은 남자가 기다리고 있었다. 그는 다짜고짜 덤덤한 얼굴로 계약서를 내밀었다.

“평화 길드에서 나왔습니다. 읽고 사인하십시오.”

이 자식 말투가 상당히 거슬리는데?

나는 계약서와 남자의 얼굴을 번갈아 노려보았다.

“정산 비율이 8:2로 되어 있는데요.”

“레이드 후 기여도에 따라 공정한 금액 분배 후. 진태경 씨가 받게 될 금액의 2할을 저희가 가져갑니다.”

“기본 수당은요?”

“삼십.”

“삼시입?”

이 자식은 혀가 반 토막이 났나.

“게이트 등급.”

“E급.”

“거절.”

“포지션 다 찼습니다. 진태경 씨는 짐꾼 역할입니다.”

나도 모르게 눈가가 파르르 떨렸다.

이 자식이 방금 뭐라고 한 거야?

“짐꾸운?”

“문제가 있습니까?”

“당연히.”

셔츠남이 고압적인 시선으로 쏘아봤다.

“뭡니까?”

“펜이 없어요.”

“…….”

잠깐의 침묵이 흐른 후, 셔츠남이 건네주는 펜을 받아 사인을 휘갈겼다. 기본급 30만 원에 정산 비율도 후하다.

E급 게이트라는 말에 흠칫했지만 짐꾼이니까 상관없지. 몬스터 가죽 좀 벗기고, 배낭 좀 메고 있다가 기분 좋게 헤어지는 거다.

‘평화 길드. 이름부터 마음에 드네.’

아까부터 사인하고 싶어서 손가락에 쥐 날 뻔했다.

“잘 썼습니다.”

“…….”

“이제 어디로 가요? 봉고차 타고 가나?”

“밖에 승합차 대 놨습니다.”

“오, 저거죠? 좋아 보이네. 에어컨도 빵빵할 것 같고.”

“…….”

“제가 마지막이었나 봐요? 이미 몇 분 계시네…… 어? 꺽정 형님!”

“어? 태경아!”

버스 트렁크에 짐을 넣기 위해 대기 중이던 임꺽정이 활짝 웃었다.

“너도 같이 가는구나. 잘됐다!”

“그러게요. 제가 형님이랑 제법 인연이 있나 본데?”

“으하하하!”

“아하하하!”

“……출발하시죠.”

더위 때문인가, 셔츠남의 얼굴이 부쩍 늙어 보였다.



* * *



버스가 출발했다. 조수석에 앉은 셔츠남은 20분 안에 도착한다는 말을 남기고 눈을 감았다.

임꺽정이 함께 고용된 이들에게 나를 소개했다.

“자, 다들 인사해. 여긴 내 아는 동생.”

이제 보니 다들 아는 사이였다. 나는 꾸벅 고개를 숙였다.

“안녕하십니까. 진태경입니다.”

“어어, 반가워요.”

“젊은 친구가 훤칠하네. 잘 싸울 것 같어.”

새로운 사람들은 총 세 명이었는데, 최소 30대 후반에서 40대 초반의 아저씨들이었다. 훈훈한 분위기 속에서 임꺽정이 설명했다.

“이 친구들은 다 E급이야. 오래전부터 알았지. 10년도 넘었으니까.”

“뭐, 그쯤 됐죠. 세월 참 빨라.”

다들 최소 10년 차라는 말이다. 나도 어디 가서 풋내기 소리 들을 정도의 경력은 아닌데, 이 사람들은 완전히…….

‘고인물 파티.’

이런 사람들은 어딜 가든 제 몫은 한다. 급박한 상황에서는 오히려 어중간한 D급보다 훨씬 낫다.

“그런데 젊은 친구는 등급이 어떻게 돼?”

올 게 왔다. 등급 조사.

나는 조심스럽게 대답했다.

“F급입니다.”

“아. 그래? 경력은?”

“7년 찹니다.”

“흠. 그래?”

미적지근한 분위기. 첫 레이드부터 이런 식이면 곤란한데.

나는 재빨리 입을 털었다.

“전투 참여는 일절 안 하고 짐꾼으로 참여할 겁니다. 걱정 안 하셔도…….”

세 사람이 멀뚱멀뚱 나를 바라본다.

“뭘 부연 설명까지 해. 우리가 잡아먹나?”

“됐어. 7년 굴렀으면 알 만큼 알겠지.”

“꺽정 형님 추천이면 된 거지. 최 팀장도 괜찮다 싶으니까 오케이 했을 거고.”

추천? 최 팀장?

정확히는 몰라도 대충 돌아가는 그림은 알겠다.

임꺽정이 나를 추천한 거다. 셔츠남, 최 팀장에게.

“무, 무슨 소리를!”

손사래 치는 임꺽정의 얼굴이 빨갛게 달아올라 있었다.

그 모습에 아저씨 셋이 낄낄거렸다.

“다 티 나, 아주. 저 형님 장가는 어떻게 갔대?”

“원래 선행은 밝혀져야 좋은 거야. 뭘 그렇게 숨기고 살아.”

“그럼. 그쪽도 그렇게 생각하지?”

나는 냉큼 고개를 끄덕였다.

“그럼요. 마음 써 주셔서 감사합니다.”

“흠흠. 뭐 나야 그냥 한 번 찔러 본 거지. 결정은 최 팀장이 다 했어.”

이거 참…….

잠깐 들렀다 스쳐 지나간 수많은 인연 중 하나라고 생각했는데, 다시 만난 임꺽정은 생각보다 순박하고 정이 깊은 사람이었다.

‘그래서 조건도 후했던 건가.’

최 팀장, 최 팀장 하는 걸 보니 그들 사이의 친분도 내 계약조건에 한몫했을 거라는 생각이 든다.

“열심히 하겠습니다.”

“아니, 결정은 최 팀장이 했다니까!”

임꺽정의 어색한 변명에 당사자가 대답했다.

“그럼 제가 결정한 걸로 하죠.”

어느새 눈을 뜬 셔츠남. 아니, 최 팀장이 우리에게 말했다.

“이제 다 도착했으니까요.”

고개를 돌리니 점점 가까워지는 4m 높이의 문(Gate)이 보였다. 그 중심에는 우리를 빨아들일 마력의 소용돌이가 휘몰아치고 있었다.

‘E급 게이트.’

복귀 후 첫 레이드다.
```

## Current accepted English baseline

```markdown
# Chapter 41

The Hunter Manpower Office.

They called it an office, but it was a building. This six-story building sat on prime real estate right by the station, and hundreds of Hunters came through it every day.

*It’s been a while.*

Even at dawn, the lobby was packed.

After working through the long line, I reached the counter. The woman there asked in a businesslike tone,

“Is this your first time at the manpower office?”

“No. I’m already registered.”

“Your name?”

“Jin Taekyung.”

Back when I was a rookie, I’d graduated from the Hunter Training Center with excellent scores. But almost nowhere needed an F-rank Hunter like me, and the contracts a few small and midsize Guilds offered like they were doing me a favor were highway robbery.

So I’d found this place. The region had been different, though.

“There’s a record at the Ilsan branch. I’ve put you on the list, so please wait in the hall on the first floor.”

“Yes.”

This six-story building was a pyramid all by itself. The first floor took E- and F-ranks. You needed at least D-rank to set foot on the second.

Some people got angry, asking if this wasn’t just open discrimination.

It was.

*Not like this was the first or second time.*

I’d lasted seven years in this business and taken every kind of dirty treatment there was. I’d long since passed the point of being picky.

I started walking with that thought when—

“Hey, look who it is!”

I turned at the gravelly voice. Some hairy guy was grinning at me.

“Taekyung. You’re Jin Taekyung, right?”

“Uncle Kkeokjeong?”

*This guy’s still alive?*

* * *

His surname was Im. I’d forgotten his given name. I was pretty sure I’d heard it once, when he introduced himself seven years ago, but I couldn’t remember it.

He just looked so much like a bandit that everyone called him Im Kkeokjeong[^1].

“How’ve you been all this time?”

“Life as an F-rank Hunter is always the same. How about you?”

“Don’t call me uncle.”

Im Kkeokjeong gave me an easy smile.

“Call me hyung. We’re not even that far apart in age.”

How many years apart were we again? It was hazy.

“Hyung, how old are you?”

“Forty-five.”

“…”

*What’s with that confidence?*

But the people skills I’d honed over the years paid off. I somehow managed to force a smile.

“Right. I’ll just call you hyung.”

“That’s it, little brother. Hahahaha!”

His hearty laugh rolled through the hall. Nearly a hundred people looked over, then looked away.

*I should’ve just pretended I didn’t hear him and kept walking.*

In a way, it was a shallow connection. We’d run into each other every day for about half a year at the Ilsan office, and sometimes worked together. That was about it.

*He’s a good guy, but…*

Sometimes having him next to me was embarrassing.

Like now.

“The yulmu tea here is incredible. And the chairs in the hall are nice and soft.”

Im Kkeokjeong knocked back a mouthful of yulmu tea[^2] and tipped his chair as far as it would go.

From the way he did it, this clearly wasn’t his first or second visit.

“You come here often?”

“Not every day. I drop by now and then. Once I got married and had kids, I started watching myself. Heh heh.”

It seemed he’d started a family while we were out of touch. When I congratulated him, Im Kkeokjeong scratched his head.

“What’s so great about that.”

He was being modest, but a big deal was a big deal. He’d worked as a Hunter—an F-rank Hunter—for more than twenty years and still managed to build a family.

I wondered if the Im Kkeokjeong in front of me might be my future self.

*Assuming I lived to that age first.*

Being a Hunter wasn’t a career you could keep up for long. Plenty of people retired the moment they finished the ten years that qualified them for a pension.

“Anyway, you’re starting to look the part. When I first saw you, you were completely frozen. Could barely even talk.”

“Of course. I’ve got seven years in.”

“So you’ve just been bouncing around offices ever since? Didn’t you sign with a small or midsize Guild on fairly decent terms? So, So… what was the name again?”

“Sopung Guild. They fired me the day before yesterday.”

Im Kkeokjeong forced a laugh.

“Hahaha! Good for you. The Guild’s name was lousy, too. What the hell is Sopung? It’s not like you’re going on a picnic to a Gate.”

“No, not that sopung. It’s a place name. They’re near Bucheon Sopung Terminal, so Sopung Guild.”

“Oh…”

The conversation that followed was pretty useful. Im Kkeokjeong was a regular at the manpower office, after all, and a veteran Hunter with decent information and his own hard-earned know-how.

“The office takes a ten percent commission. That’s standard. But the batting average here is pretty good.”

*Batting average* was slang in this business for the odds of getting hired. For someone whose immediate goal was a day’s pay, that was good news.

“Even for F-rank Hunters like us?”

“Huh? Yeah. That’s right.”

*What’s with that awkward look?*

Before I could ask anything else, a voice came through the speakers in the hall.

—E-rank Hunter Im Hyeokjun. Im Hyeokjun, please come to the lobby.

Six thirty in the morning.

At last, the first batter was up. And it would only be my turn after all the E-rank Hunters had left.

“E-ranks first, as expected… Hyung, where are you going?”

“I’ll go ahead.”

Im Kkeokjeong—or rather, Im Hyeokjun—slung a large bag of armor and weapons over his shoulder and gave a sheepish laugh.

*No wonder his expression looked off.*

The man had clearly worked himself to the bone while I wasn’t looking.

It was only one step, but ranking up on an F-rank’s potential was no easy feat.

“See you again.”

“Yes. See you.”

Him walking out of the hall was the start. The speakers began pouring out names like they meant it.

E-rank this person, E-rank that person, E-rank…

*Goddamn it, am I the only F-rank here?*

Just as I was starting to get anxious—

—F-rank Hunter Jin Taekyung. Jin Taekyung, please come to the lobby.

*There it is!*

* * *

“Mr. Jin Taekyung?”

A man in a white linen shirt was waiting in the lobby. Without preamble, he held out a contract with a blank face.

“I’m from the Peace Guild. Read it and sign.”

*This guy’s way of talking is seriously irritating.*

I glared from the contract to the man’s face and back.

“The settlement split is eight to two.”

“After the raid, we divide the proceeds fairly by contribution. Then we take twenty percent of the amount you receive.”

“And the base pay?”

“Thirty.”

“Thir…ty?”

*Did this guy’s tongue get cut in half?*

“Gate rank.”

“E-rank.”

“Rejected.”

“The positions are full. You’ll be a porter.”

The corner of my eye twitched.

*What the hell did this guy just say?*

“Por-ter?”

“Is there a problem?”

“Obviously.”

The shirt guy glared at me, looking down his nose.

“What is it?”

“I don’t have a pen.”

“…”

After a brief silence, I took the pen he handed me and scrawled my signature. The base pay was 300,000 won, and the settlement split was generous too.

I’d flinched at E-rank Gate, but I was only going as a porter, so it didn’t matter. Skin a few monsters, haul a pack for a while, and part ways in a good mood.

*Peace Guild. I like the name already.*

I’d been itching to sign so badly my fingers had almost cramped.

“All signed.”

“…”

“So where are we going now? We taking a van?”

“There’s a van waiting outside.”

“Oh, that one? Looks nice. Bet the AC’s blasting too.”

“…”

“Guess I was last? There are already a few people here… Huh? Kkeokjeong hyung!”

“Huh? Taekyung!”

Im Kkeokjeong was waiting to load his bags into the bus’s trunk. He grinned wide.

“You’re coming too. Great!”

“Right? I must really have a connection with you, hyung.”

“Hahahaha!”

“Ahahaha!”

“…Let’s get going.”

Maybe it was the heat, but the shirt guy’s face looked years older.

* * *

The bus pulled out. From the passenger seat, the shirt guy said we’d arrive within twenty minutes, then closed his eyes.

Im Kkeokjeong introduced me to the others who’d been hired with us.

“All right, everyone, say hello. This is a younger brother I know.”

Now that I looked, they all knew each other. I dipped my head.

“Hello. I’m Jin Taekyung.”

“Oh, nice to meet you.”

“Tall young fellow. Looks like he can fight.”

There were three new people in all, men in their late thirties or early forties. In that warm atmosphere, Im Kkeokjeong explained.

“These guys are all E-rank. I’ve known them a long time. Over ten years now.”

“Yeah, about that long. Time sure flies.”

Meaning they all had at least ten years in. I had enough experience that nobody was going to call me a rookie wherever I went, but these guys were on another level entirely.

*Old-timer party.*

People like them pulled their weight wherever they went. In a pinch, they were much better than a middling D-rank.

“So what’s the young guy’s rank?”

Here it came. The rank check.

I answered carefully.

“F-rank.”

“Ah. That so? How many years?”

“Seven.”

“Hmm. That so?”

The mood went lukewarm. If my first raid started like this, that would be a problem.

I ran my mouth before it could settle.

“I won’t be in combat at all. I’m joining as a porter, so you don’t have to worry…”

The three men stared at me blankly.

“Why the extra explanation? We gonna eat you?”

“Drop it. If he’s been knocking around for seven years, he knows enough.”

“If Kkeokjeong hyung recommended him, that’s enough. Team Leader Choi must’ve thought he was all right too, or he wouldn’t have said yes.”

*Recommended? Team Leader Choi?*

I didn’t know the exact details, but I could more or less see how this had gone.

Im Kkeokjeong had recommended me. To the shirt guy—Team Leader Choi.

“W-what are you talking about?”

Im Kkeokjeong waved his hands, his face bright red.

The three men snickered.

“It’s written all over him. How did that hyung ever get married?”

“Good deeds are supposed to come to light. Why live hiding them?”

“Right. You think so too, don’t you?”

I nodded at once.

“Of course. Thank you for looking out for me.”

“Ahem. I just put in a word. Team Leader Choi made the decision.”

Well, then…

I’d thought of Im Kkeokjeong as one of the many people I’d crossed paths with for a moment and moved on from. Meeting him again, he was more simple and warmhearted than I’d expected.

*So that’s why the terms were so generous.*

The way they kept saying Team Leader Choi, Team Leader Choi, I figured their friendship had played a part in my contract too.

“I’ll work hard.”

“I told you, Team Leader Choi made the decision!”

The man in question answered Im Kkeokjeong’s awkward excuse.

“Then let’s say I made the decision.”

The shirt guy had opened his eyes at some point. No—Team Leader Choi. He spoke to us.

“We’ve arrived.”

I looked over. A four-meter-high Gate was drawing closer. At its center, a vortex of mana churned, ready to suck us in.

*An E-rank Gate.*

My first raid since coming back.

[^1]: Famous Joseon-era folk-hero bandit; the nickname comes from his looks.
[^2]: Yulmu tea is a sweet Korean grain drink, commonly served hot or cold.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 41`.

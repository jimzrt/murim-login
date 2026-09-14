# Master Edit Task — Chapter 56

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
| 진위경    | **Jin Wikyung**    |
| 위팽     | **Wipeng**         |
| 이천백    | **Lee Cheonbaek**  |
| 이소군    | **Lee Seogeun**    |
| 화양검    | **Blade of Flowers**          | Jin Baekyang   |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 초식     | **form**                                         | Numbered technique movement                           |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 일격     | **One Strike**                         |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 호승심 | polysemy | Competitive pride or fighting spirit; not merely a desire to test oneself. | test myself |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 50–54

## Plot

Taekyung enters Choi Minwoo’s exclusive D-rank Gate and clears a colony of about twenty Level 40 swamp Lizardmen alone. Choi reveals the encounter was a test, then releases female-Lizardman pheromones that summon a much stronger horde. Taekyung spends all 100 Remaining Points—30 Strength, 30 Stamina, and 40 Agility—and uses One Flash to kill the Level 52 Lizardman Great Chieftain and dozens of monsters. He and Choi clear three C-rank Gates in one day, earning Taekyung 300 million won, while Choi privately recognizes that Taekyung may be stronger than himself.

Sopung Guild’s Guild Master learns that Kim Sangshik dismissed Taekyung and filed a false report. He expels Kim and orders the resignation of Kim’s son, Kim Sangho, provoking Guild-wide gossip about Taekyung’s reawakening.

Taekyung returns home with his C-rank Hunter license and cash, gives his mother and younger sister Hayeon an edited account of his reawakening, and spends the day treating them to clothes and an expensive meal. Back in the goshiwon, increasingly vivid Murim nightmares destabilize him despite Sleep Mode and qi circulation. His injuries worsen during raids, so Choi orders him home. Taekyung lies to Jinho that Jin Wikyung is his Chinese girlfriend, then concludes that Murim may be another reality and the Ark - 2020 capsule a dimensional Gate.

A dream of the Mount Heng Sword Sect–Jin Family battle convinces Taekyung that Murim’s people are real and that he must return. Choi and Butler Kim investigate him, find no evidence that he is an illegal Awakener or deliberately infiltrated Choi’s orbit, and offer an exceptionally generous contract. Taekyung refuses because he cannot abandon Murim, promises to return the next day, enters the capsule, and accepts the prompt to connect to Murim.

## Continuity

- Taekyung clears the Lizardman Gate without injury, then kills the Level 52 Lizardman Great Chieftain and the summoned horde with One Flash.
- He spends all 100 Remaining Points: 30 Strength, 30 Stamina, and 40 Agility. His equipment remains the First Rate Lizardman Hunter’s Leather Set and Lizardman Slayer’s Harpoon.
- Taekyung completes three C-rank Gates in one day and receives 300 million won, including a 270-million-won bonus. His seven-day provisional Peace Guild contract requires weekends off.
- Choi Minwoo suspects Taekyung may be stronger than him; Choi’s exact current rank remains unknown. Choi continues observing Taekyung and wants to recruit him.
- Sopung Guild expels Kim Sangshik after confirming his misconduct; Kim Sangho also leaves. Sopung’s recruitment of Taekyung remains unresolved.
- Taekyung now holds a C-rank Hunter license. His family knows only the edited explanation that he reawakened and earned money; Murim, the System, and the capsule remain concealed from them and from Seong Jinho.
- Hayeon is nineteen and still a high-school senior. Taekyung’s mother and Hayeon secretly give him additional cash and side dishes.
- Taekyung suffers recurring Murim nightmares and increasing injuries during raids. Sleep Mode repairs his body but does not resolve the mental disturbance.
- The Mount Heng–Jin Family battle is underway. The Head Elder’s third force is waiting for both sides to weaken; the traitor’s identity, betrayal, and the battle’s outcome remain unresolved.
- Taekyung has reconnected to Murim through the Ark - 2020 capsule. Whether the capsule can transport him safely and reliably, its ultimate purpose, and the consequences of his return remain unresolved.
- Choi’s offered contract includes a 500-million-won signing bonus, 50-million-won monthly salary, seventy-percent settlement split, officetel, sedan, and social insurance. Taekyung rejects it while intending to return from Murim.

## Translation Decisions

- Use **Lizardman Great Chieftain** for 대족장 and **One Flash** for 일섬.
- Preserve **swamp Lizardmen**, **Lizardman Hunter’s Leather Set**, **Lizardman Slayer’s Harpoon**, and the female-Lizardman pheromone lure.
- Keep **C-rank Hunter** distinct from System **Grade** terminology.
- Preserve **Sleep Mode**, **Remaining Points**, **Internal Energy**, **System**, and the exact prompt: **“Would you like to connect to Murim?”**
- Use **logged in** only for Taekyung’s action after accepting the prompt.
- Keep **Peace Guild**, **Sopung Guild**, **Hunter license**, **goshiwon**, and **officetel**.
- Preserve the distinction between Hayeon’s gender-neutral question about Jin Wikyung and Taekyung’s false claim that Wikyung is his girlfriend.
- Retain the dry, self-mocking narration; affectionate, profane family banter; Choi’s measured testing and recruitment; and the Guild Master’s “raise hell” callback.
- Keep *Bulgeum* as “Burning Friday,” with a concise Korean-slang footnote, and retain concise first-use footnotes for *gukbap* and *goshiwon*.

### Prior accepted reading-copy tails

#### Chapter 54 tail (verified mastered)

…
valued that highly. And it was proof I had found an employer with the insight not to judge a Hunter by rank alone. *And he has the money, too.* I stared across the table at Team Leader Choi. As always, his expression gave nothing away, and his eyes were deep. Team Leader Choi spoke without warning. “This makes three.” He had already offered me a contract twice before. I had turned him down both times. This was his roundabout way of telling me not to refuse him again. “I’m sorry about that. There was a minor issue.” “Have you resolved it?” “Yes. For now, I think so.” “Then there shouldn’t be any problem now.” “…Of course.” Even as I answered, I still had doubts. Was there really no problem now? Was it okay to leave it like this? *What the hell am I thinking?* I had to knock this out before my mind wandered. “I’ll sign.” I started signing with the fountain pen Team Leader Choi had handed me. One page, two pages, three… The contract was five pages long. All I had to do was write the three characters of my name on the last page, and it would be done. At that moment, the question came back. *Is this really okay?* The fountain pen that had been moving without hesitation slowed. One thought caught on the next. *What if it isn’t? Isn’t this what I wanted?* It was. This was exactly what I had dreamed of so desperately for seven years. A massive salary and high social standing. Becoming a son and older brother my family could be proud of, and treating them to an easy life. Becoming someone others envied and admired instead of ignored and scorned. *I can have it all now.* I could live enjoying every bit of it. Goodbye to my grimy life. Goodbye to that shitty Murim. Crack. And goodbye to the fountain pen, too. I relaxed my grip. Ink spilled from the shattered pen and soaked into the contract. “Mr. Jin Taekyung. Let me ask you again.” Team Leader Choi pulled out a white handkerchief and wiped the ink that had splattered onto his chin. For all the sudden mess, he looked calm. “That problem from last time. Have you really resolved it?” “No.” The moment I answered, a weight lifted from my chest. “If it’s something I can help you with…” “I appreciate it, but I have to handle this myself.” Team Leader Choi studied me with an odd look, then gave a small laugh. “I didn’t know a contract could be this hard. I didn’t expect to get turned down three times, either.” He sounded more amused by the situation than angry. “When would be a good time to make my fourth offer?” He probably meant it half as a joke, but my answer was serious. “Tomorrow. Same time, same place.” “Tomorrow?” “Yes. Tomorrow.” Just one day. But for me, it would be a month. Maybe several. Team Leader Choi had no way of knowing that, and he furrowed his brow. “I don’t much care for jokes like that.” “Neither do I. Not jokes like this.” He didn’t know what my words meant. “I’ll be sure to see you.” It was a vow to myself. A vow that I would make it back alive. And… “Tomorrow, you’ll have to raise the terms even higher.” I walked out of the café, leaving a wide-eyed Team Leader Choi behind. * * * “Phew.” I drew a deep breath and opened the capsule. The sight of the sunken seat and VR headset made my heart hammer. Even after coming this far, temptation kept raising its head and whispering. *Don’t go back.* *Just forget everything and live content with your reality.* *Everyone you met in Murim is an NPC, and Murim is nothing more than a game.* Right. There had been a time when I thought that way. But after wrestling with it, I realized I was going back, one way or another. *I’d already reached my conclusion a long time ago.* On the night of the blizzard, I had gone back for Gong Yacheong. I had brought along two young siblings who were nothing but baggage, and instead of using the reconnaissance squad as human shields, I had fought Jopil and barely made it through. *It probably started then.* That was when the three letters *NPC*, lodged in my mind, began to fade. That was when the two-character word *family* came to mind at the sight of Jin Wikyung’s back as he told me to survive and turned away.[^3] “Fuck, my life really is a variety show.” With a hollow, complaining laugh, I climbed into the capsule. The moment I put on the VR headset, a single line of text appeared in front of me. Ding. > **System** > > Would you like to connect to Murim? > > **Accept** / **Decline** “Yes.” My consciousness faded. My vision darkened. I logged in. [^1]: “Paying three personal visits” alludes to Liu Bei’s repeated visits to Zhuge Liang in *Romance of the Three Kingdoms* to recruit him as an adviser. [^2]: An officetel is a Korean mixed-use unit designed for both office and residential use. [^3]: In Korean writing, each syllable is written as a single character block; the word for “family” consists of two such blocks, contrasting with the three Roman letters in “NPC.”

#### Chapter 55 tail (verified mastered)

…
sudden? Seriously.” “No time. Answer quickly.” “You were breathing, that’s why you woke up. Otherwise you’d be dead.” Fair enough. Apparently, logging in or logging out put the other side into a deathlike state. *If I’d logged out before dealing with the assassins, there wouldn’t have been a body to come back to.* I’d think about that later. There was a more urgent problem. “The main force?” “We were already heading that way. We split two men off and sent them back to the family.” “Good. How much farther?” “At least another two hours.” “Two hours…” “Uh, Squad Leader. I’m sorry to say this, but… I think we have to consider the worst case.” Hyuk Mujin and every member of the reconnaissance squad clamped their mouths shut. Nobody had to ask what the worst case meant. *I’ve thought about it too.* From what Gwak Jun had said right before he died, this betrayal had been planned down to the last detail for a long time. But the plan had exactly one error. *Me.* The Head Elder had underestimated me. No—maybe, in another way, he’d overestimated me. He’d sent dozens of First Rate masters just to kill me. Even that hadn’t been enough. I had survived. *He made a mistake.* On top of that, when Gwak Jun first revealed his true colors, he’d said they needed to start moving soon if they wanted to make it on time. Which meant… “It’s not too late.” I met each squad member’s eyes and spoke firmly. “Don’t think about the worst case. No matter what it takes, I’ll change that outcome.” “Squad Leader…” “So, Mujin.” I gave Hyuk’s choked-up face a good-natured smile. “Get up. Now.” “I’m dying here.” “Want to get beaten to death instead?” “…” “Run even one more step in the time we’ve got. Don’t you know marathon spirit?” “I don’t.” Ah. Right. This was Murim. “Anyway, get up. Another hour will do it.” Hyuk grabbed his trembling legs and pushed himself up, then cocked his head. “An hour?” “Yeah. An hour.” “I already told you. Even at full speed, it’ll take two.” “Exactly. An hour.” “What are you even saying…” “Mujin.” “Yes?” Hyuk blinked at me, as simple as an ox. I smiled even brighter. “Ever heard of grit?” Two hours or four, I didn’t care. We were getting there in an hour. Period. “Run like hell. That’ll do it.” “Huk.” Every face in the reconnaissance squad went deathly pale. * * * “We’ve been blocked.” “Casualties are heavy. Sect Leader, please take action.” Despite the continuing reports, Blood Wolf Sword Lee Cheonbaek, Sect Leader of the Mount Heng Sword Sect, kept his eyes closed. *I was too hasty.* The war had begun in a rush, and their preparations had been equally inadequate. Their provisions were rapidly dwindling, morale was falling, and men were deserting one after another. *They read us completely.* Rage at losing his son and impatience with the situation had clouded his judgment. He had ignored his subordinates’ advice and taken the fastest route he could find. And that was how he had run into the Jin Family of Taiyuan in a narrow gorge whose very name was unfamiliar: Eight Spring Gorge. “Sect Leader!” At his subordinate’s shout, Lee Cheonbaek slowly opened his eyes. The fearsome vision of a Peak master pierced the battlefield. “Gaaah!” “Wipe them out! They’re nothing but rabble!” Well over a thousand of his own men were jammed at the narrow mouth and couldn’t advance. The wandering martial artists and mounted bandits he’d put at the front had numbers, but man for man they were worse than even the Jin Family’s rank-and-file. *Sword fodder, at best.* Just as he was clicking his tongue inwardly, several dozen wandering martial artists suddenly started peeling off the front line. The middle-aged wanderer at their head bellowed until his throat tore. “We’ll die like dogs at this rate! Brothers of the Blood Rain Group, fall back!” Those became the middle-aged wandering martial artist’s last words. Whoosh— A light breeze. The wandering martial artist felt nothing else. He did not know that Blood Wolf Sword Lee Cheonbaek had already brushed past him. He did not know that the wandering martial artists under him had frozen in terror. He only thought, suddenly, that his neck was hot. “Uh…” His cleanly severed head dropped with a dull thud. The headless body staggered a few more steps, then collapsed like a rotten old tree. “The Blood Rain Group, was it?” Lee Cheonbaek pointed his sword at the petrified wanderers. Not a single drop of blood stained its blade. “Go back.” A Peak master’s killing intent shot into them like a blade. The wandering martial artists charged toward the front even faster than they had come. They had decided that fighting on the front line was better than throwing themselves at the Peak master before them. “Rat bastards.” Lee Cheonbaek went after them. His burning gaze was aimed somewhere ahead, where the Jin Family of Taiyuan’s command had to be. “The Sect Leader is taking the lead!” “Everyone, charge! Wipe out the Jin Family of Taiyuan!” As Lee Cheonbaek stepped forward, the Mount Heng Sword Sect’s core forces followed. Three Peak masters and dozens of First Rate masters crashed toward the front. [^1]: A riff on the Korean pop song “My Ear’s Candy”; Taekyung follows it with a parody of the lyrics.

## Korean source

```text
＃56화



이천백의 등장을 가장 먼저 알아차린 사람은 대장로였다.

‘머리가 직접 나섰군.’

협곡을 가로지르며 뿜어내는 강맹한 기파와 넘실거리는 살기. 눈으로 보지 않아도 알 수 있었다.

아니나 다를까.

“이놈들!”

천둥 같은 고함과 함께 이천백이 나타났다. 반백의 머리는 갈기처럼 휘날렸고 눈은 붉게 달아올라 있었다.

잇따라 항산검문의 핵심 전력이 도착했다. 일류 무인들과 세 명의 절정 고수!

“태원진가 놈들을 쓸어 버려라!”

“문주님이다! 문주님께서 오셨다!”

“우와아아!”

함성과 함께 식어 가던 전의가 타올랐다. 순식간에 트인 길을 따라 이천백이 쇄도했다.

“간악한 태원진가 놈들을 죽여라!”

그 모습을 가만히 지켜보고 있을 진위경이 아니었다.

“때가 되었습니다.”

대장로가 대답했다.

“동의하오.”

사실 그는 이천백의 등장이 달갑지 않았다. 어느 정도 소모전이 진행되어야 뒤처리가 편해진다.

하지만 현재 태원진가와 항산검문. 양 세력의 피해는 그리 크다고 할 수 없었다.

‘상관없겠지. 어차피 그들이 나설 테니.’

산서성의 패자를 자처하는 양대 세력이지만 ‘그들’의 힘에 비하면 하찮다.

과거 강성했던 시절에도 변방의 무가(武家) 취급밖에 받지 못하던 태원진가가 어찌 그들을 당해 낼 수 있을까.

‘일개 무가라…….’

씁쓸한 웃음을 삼킨 대장로가 검을 뽑아 들었다.

스르릉.

오랜 세월 두 자루의 검을 품었다. 하나는 가슴에, 하나는 허리춤에. 이제 더는 말이 필요 없었다.

“이천백은 내가 맡겠소.”

“그리하시지요.”

혈랑검 이천백이 누군가, 오로지 검 한 자루로 항산검문을 세우고 이제는 일성(一城)의 패자를 노리는 자다. 비록 적이지만 인정할 수밖에 없는 절정의 무인.

‘그와 겨뤄 보고 싶다.’

그러나 진위경은 끓는 피를 억눌렀다. 가문의 명운이 걸린 전투. 호승심은 접어야 한다.

“위팽.”

“예.”

어느새 예리한 협봉검을 빼 든 위팽이 진위경의 곁에 섰다.

“너와 내가 나머지를 맡는다.”

“받들겠습니다.”

한 치의 망설임도 없는 대답이다. 희미하게 웃은 진위경이 검을 뽑았다. 태원진가 대대로 내려져 오는 가문의 보검.

어느 날 홀연히 사라진 아버지가 남긴 유일한 물건이다.



중원 유람 좀 하고 오마.

그동안 너 써.



검집에 대충 끼워 넣어져 있던 서신의 내용을 떠올린 진위경은 새삼 피가 거꾸로 솟구쳤다.

‘중원 유람 같은 소리하네. 평생 실컷 놀아 놓고.’

가주라는 인간은 지금 어디서 뭘 하는지도 모르겠고, 수천 리 밖에 있는 둘째는 이제야 겨우 서신을 받았을 것이다.

‘내가 지켜야 한다.’

무인, 시비, 하인, 아이들.

지금은 다른 누구도 아닌 진위경이 태원진가의 가주다. 그들의 죽음도, 생존도 오롯이 그가 짊어져야만 했다.

‘반드시 승리한다.’

진위경이 눈을 부릅떴다. 검을 치켜든 그의 입에서 창룡후가 터져 나왔다.

“한 놈도 살려 보내지 마라!”

쉬쉬쉭!

태원진가의 고수들이 땅을 박차고 날아올랐다. 그것을 신호로 등 뒤에서 불화살 하나가 높게 솟구쳤다.

절벽 위에서 수십의 인영이 몸을 일으킨 것도 그때였다.

“쏴라!”

소낙비처럼 쏟아지는 화살 아래, 이 전투의 향방을 가를 고수들의 싸움이 시작되었다.



* * *



혈랑검 이천백은 타고난 무인이다.

무공에 대한 천부적인 재능과 야수 같은 감각으로 적들을 해치웠고, 자신의 야망을 차례차례 실현시켰다.

항산검문을 세우고, 인근 방파를 차례차례 흡수하며 힘을 길렀다. 장차 중원에서도 인정받는 세가(世家)의 초석을 다지고자 했다.



‘문주! 이 공자가…….’



그러던 어느 날, 둘째 아들이 주검으로 돌아왔다. 정당한 비무로 인한 것도 아니었다. 극독에 당해 칠공에서 피를 쏟아내며 죽었다.

이천백은 맹세했다. 태원진가와 연관된 것들은 모조리 죽이고 불태우기로.

그런 그의 눈앞에 진위경이 나타났다. 이천백의 눈에서 불길이 쏟아졌다.

“이노옴-!”

이천백이 야수처럼 뛰어들었다. 일 갑자에 달하는 공력을 머금은 검신이 우윳빛으로 빛났다.

이 힘이라면 어떤 갑옷도, 신병이기도 잘라 낼 수 있으리라.

‘놈은 반드시 죽는다!’

확신에 찬 이천백이 검을 휘두르려던 그 순간이었다.

“오호, 검기(劍氣)?”

뒤에서 들려온 나직한 목소리. 이천백의 가슴이 덜컥 내려앉았다.

‘어떻게?’

이토록 허무하게 뒤를 내주다니. 이천백의 반응은 섬전 같았다. 역수로 틀어쥔 검을 뒤로 찔러 넣었다.

쉭.

검신은 허공을 찔렀고, 이천백은 시간을 벌었다. 그제야 적의 얼굴을 확인할 수 있었다.

가슴께까지 늘어트린 수염, 입가에 맺힌 여유로운 미소.

백발의 노인이었다. 이천백은 단숨에 노인의 정체를 알아차렸다.

“화양검?”

대장로가 고개를 끄덕였다.

“오랜만에 듣는군. 그러는 자네는 이천백이겠지?”

“그렇소.”

이천백은 대답하는 지금도 등골이 서늘하다 느꼈다.

진위경이 어디 있는지, 전투가 어떻게 돌아가고 있는지 확인할 엄두도 나지 않았다. 눈을 떼면 금방이라도 목이 떨어질 것 같았다.

‘우연? 아니다.’

진위경을 보고 과하게 흥분한 건 맞다. 마음이 조급했던 것도 맞다. 하지만 이천백은 절정 고수였다.

그중에서도 검기상인의 경지에 오른 절정 고수.

이미 답은 나와 있었다.

‘고수!’

일 초식이건, 반 초식이건 눈앞의 노인은 이천백보다 윗줄의 고수였다. 이천백은 애검을 꽉 움켜잡았다.

“위명은 익히 들었소.”

“위명은 무슨. 뒷방 늙은이에 불과하네.”

“그럼 계속 뒷방에 있지, 뭣 하러 나온 거요?”

“아직 젊은 친구라 뭘 모르는군. 늙을수록 가끔 움직여 줘야 해.”

대장로의 능글맞은 태도에 이천백은 이를 갈았다.

‘망할 늙은이.’

그는 이미 오래전부터 태원진가의 동향을 살피고 있었다.

대장로를 중심으로 가주에게 맞서는 파벌이 있다는 것도 안다. 그래서 내심 태원진가의 내부 분열을 기대하기도 했다.

하지만 기대했던 상황은 정반대로 흘러갔다.

‘외적이 침입하면 한마음으로 뭉친다 이건가?’

무거운 눈으로 대장로를 응시하던 이천백의 입이 열렸다.

“당신은 얼마나 강하오?”

“자네가 믿는 만큼.”

“말장난이군.”

“화양검이라 불리던 시절 내 나이가 이립이었네.”

나이 서른에 대장로는 이미 절정의 무인이었다. 칠순의 노인이 된 지금, 그의 무공은 어떻게 변화했을까. 잠시 생각하던 이천백은 문득 실소를 머금었다.

‘나도 늙었군.’

혈랑검.

젊은 시절의 이천백은 거침없었다. 뛰어난 신공, 번듯한 스승 하나 없이 오로지 홀로 모든 것을 헤쳐 나갔다.

한 수 위의 상대를 만나도 그는 물러서지 않았다. 늑대처럼 달려들어 목을 물어뜯었다.

‘반평생을 그렇게 살았는데…….’

어느 순간부터 그는 혈랑검 대신 문주라고 불리기 시작했다.

혈육, 수하, 재물. 지켜야 할 것들이 산더미처럼 쌓여 갔다.

수련 대신 집무 시간이 늘었고, 행동해야 할 때 머리를 굴렸다. 지금처럼.

“왜 웃나?”

대장로의 물음에 이천백이 대답했다.

“나 자신이 한심해서 웃었소.”

“자네, 나를 무서워하는군.”

이천백이 묵묵히 고개를 끄덕였다.

“죽음이 두려웠나?”

“아주 잠깐은.”

“지금은 어떤가?”

“당신을 죽일 거요.”

“자네 정도로는 무리야.”

“길고 짧은 건 대봐야 하지 않겠소?”

“짧은 자들이 늘 하는 말이지. 막상 대봐도 결과는 변함없다는 사실을 몰라.”

“혀가 맵구려.”

“혀만 매울까.”

대장로는 검을 늘어트렸다. 별반 특별할 것 없어 보이는 청강검이었지만 그의 손에 들린 순간 지독한 예기를 뿜어내기 시작했다.

“먼저 오시게.”

이천백은 거절하지 않았다. 일 갑자의 공력을 빨아들인 검신이 빛의 아지랑이를 피워 올렸다.

수많은 무인들이 꿈꾸는 검기상인(劍氣霜刃)의 경지.

츠츠츠.

검기가 세 치(10cm)까지 솟구친 순간, 이천백의 신형이 쏘아졌다. 수많은 실전 끝에 완성한 독문 무공이 그의 손끝에서 펼쳐지고 있었다.

쉭, 쉬쉬쉬쉭!

콰아앙!

검기가 사방을 난도질했다. 순간적으로 솟아오른 흙더미 사이로 비명이 터져 나왔다.

“크아아악!”

간격에 휘말린 무인들이 내는 소리였다. 하나같이 젊은이의 목소리들. 이천백의 머릿속에 붉은 신호가 켜졌다.

‘뒤!’

이천백은 돌아섬과 동시에 검을 휘둘렀다. 바람에 나부끼는 흰 수염이 보였다. 그의 손에 들린 검도.

쾅!

‘큭.’

굉음과 함께 이천백이 정신없이 물러났다. 그에게는 손목의 통증을 느낄 틈도 주어지지 않았다.

쾅! 쾅! 쾅!

두 개의 검이 부딪칠 때마다 뇌성벽력이 울려 퍼진다.

줄줄이 뿜어져 나오는 검기가 땅을 부수고 바람을 찢었다.

쉬쉬슁!

“저게 도대체…….”

양 세력의 무인들은 싸우던 것도 잊었다. 그저 넋이 나간 얼굴로 이 엄청난 생사결을 바라봤다.

지금 이 순간만큼은 모두가 같은 생각을 하고 있었다.

‘저들이 우리와 같은 사람이란 말인가?’

쉴 새 없이 터지는 굉음과 보는 것만으로도 황홀해지는 검기의 향연. 그 중심에 선 두 사람의 움직임은 이제껏 본 그 누구보다 빠르고, 강했다.

누군가가 신음처럼 중얼거렸다.

“이게 절정 고수…….”

그들의 눈에는 누가 이겨도 이상하지 않은 싸움.

그러나 힘의 우위는 명백했다. 삼백여 합을 주고받았을 때, 대장로의 검이 변화를 보였다.

쉭, 서걱!

“크윽.”

이천백은 입술을 깨물었다. 대장로의 검이 훑고 지나간 팔뚝에서 피가 철철 흐르고 있었다.

검을 쥔 손에 힘이 스르륵 풀렸다.

‘하필이면.’

재빨리 검을 바꿔 잡았지만 그는 본래 우수검(右手劍)이다.

십 할의 전력을 쏟아부어도 모자랄 판에 검을 쓰는 팔을 다쳤으니 승부는 정해진 것이나 다름없었다.

쾅!

우드득.

단 일격에 손목이 꺾였다. 심각한 공력 소모로 약해진 검기로는 대장로를 당해 낼 수 없었다.

하지만 이천백은 포기하지 않았다.

‘아직, 아직 끝나지 않았다.’

이보다 더한 부상도 숱하게 겪었다. 이천백은 팔과 허리, 다리 힘을 이용해 검을 휘둘렀다.

아니, 휘두르려고 했다.

촤아악.

이번에는 무릎이다. 힘줄이 잘려 나간 무릎이 이천백의 의지와는 상관없이 스르륵 무너졌다.

그의 검이 허망하게 허공을 갈랐다.

푹. 푹푹푹.

옆구리, 어깨, 가슴.

번갯불이 전신을 쑤시고 베어 냈다. 강맹한 검기는 살과 뼈를 자르는 걸로도 모자라 내부를 진탕시켰다.

“우웨엑!”

내장 조각이 섞인 핏물을 토해 낸 이천백이 흐린 눈빛으로 대장로를 올려다봤다.

노인의 안색은 무덤덤했다. 상대를 쓰러트렸다는 희열도, 전쟁이 끝났다는 기쁨도 엿볼 수 없었다.

그에게는 이 모든 것들이 당연한 결과였다.

“쿨럭, 산서제일인이 눈앞에 있었구려.”

“천하제일이 아니라면 변방의 무부(武夫)에 불과하지. 나도, 자네도 그 정도 그릇은 아니야.”

“원하는 걸 말하시오. 내 목을 주겠소. 수하들을 항복시키고, 십 년이고 백 년이고 봉문 하겠소. 그러니…….”

“불가. 내가 원하는 건 멸문일세. 풀 한 포기 남겨 두지 않는 완전한 멸문.”

“어째서……!”

“그렇게 묻지 말게. 자네가 승리했다면 멸문하는 것은 본가가 되었을 테니.”

이천백은 핏발 선 눈동자로 대장로를 노려봤다.

당장이라도 저 주름진 목을 꺾어 버리고 싶다. 그러나 중상을 입은 그가 할 수 있는 일이라고는 목소리를 쥐어짜 내는 게 전부였다.

“태원진가. 네놈들이 시작하지 않았나. 그 어린 녀석을, 내 아들을 죽였어!”

“아, 이소군. 그렇지. 그 아이가 시작이었지.”

대장로는 고소를 머금었다.

산서성을 양분하는 항산검문의 주인조차 ‘그들’의 개입을 알아채지 못했다. 죽음이 목전에 다다른 지금까지도.

- 염라대왕을 만나면 물어보게. 이소군을 죽인 자가 누구인지.

귓가를 파고드는 전음(傳音)에 이천백이 눈을 부릅떴다.

“그게 무슨……!”

그건 다분히 충동적인 행동이었다. 아무것도 모른 채 죽게 될 이천백에 대한 연민일 수도 있고, 늙은이의 단순한 변덕일 수도 있다.

- 저승길 노잣돈일세. 먼 길 가는 동안 생각해 보게.

대장로는 검을 치켜세웠다. 겨울 산등성이 너머로 비춘 노을이 검신을 따라 산산이 부서졌다.

‘이것으로…….’

이천백이라는 거인의 죽음으로 항산검문은 무너진다.

저항하는 자는 죽고 항복하는 자는 사로잡힌다. 그렇게 하나의 전쟁이 끝나고…… 새로운 전쟁이 시작될 것이다.

모두가 승리에 취해 있는 그 순간에.

‘끝이다.’

마침내 대장로의 검이 움직였다.

쐐애애액-!

날카로운 파공성.

최후를 직감한 이천백은 눈을 감았다. 푸른 검기에 휩싸인 검신이 아름다운 선을 그었다.

서걱.

그러나 앞서 들린 파공성도, 검의 방향도 이천백의 예상을 벗어났다.

난데없이 등을 향해 날아온 창 한 자루를 검기로 갈라 낸 대장로의 입에서 창노한 음성이 터졌다.

“웬 놈이냐!”

다음 순간, 대답이 들려왔다.

“나다, 이 십새끼야!”

야트막한 언덕 위, 우뚝 서 있는 한 청년의 얼굴을 확인한 대장로가 신음했다.

“진태경?”
```

## Current accepted English baseline

```markdown
# Chapter 56

The Head Elder was the first to notice Lee Cheonbaek’s arrival.

*The head himself has entered the fray.*

The fierce wave of qi blasting across the gorge, and the killing intent rolling with it, made that obvious even without seeing him.

Sure enough—

“You bastards!”

Lee Cheonbaek appeared with a thunderous roar. His half-gray hair whipped around like a mane, and his eyes burned red.

The Mount Heng Sword Sect’s core forces arrived on his heels. First Rate martial artists, and three Peak masters!

“Wipe out those Jin Family of Taiyuan bastards!”

“The Sect Leader is here! The Sect Leader has come!”

“Waaaah!”

The cheers rekindled the fighting spirit that had begun to fade. Lee Cheonbaek surged forward along the path that had opened in an instant.

“Kill those treacherous Jin Family of Taiyuan bastards!”

Jin Wikyung was not the kind of man to stand by and watch.

“The time has come.”

The Head Elder answered.

“I agree.”

In truth, he had not welcomed Lee Cheonbaek’s arrival. A certain amount of attrition would have made the cleanup easier.

But the losses on both sides—the Jin Family of Taiyuan and the Mount Heng Sword Sect—were still nothing to speak of.

*It doesn’t matter. They’ll be making their move anyway.*

The two great powers claimed to be the rulers of Shanxi, but compared to *them*, they were insignificant.

Even in its former heyday, the Jin Family of Taiyuan had been treated as nothing more than a martial family from the frontier. How could it possibly stand against them?

*A mere martial family…*

The Head Elder swallowed a bitter smile and drew his sword.

Shing.

For many years he had carried two swords. One at his chest, the other at his waist.

There was no need for more words.

“I’ll handle Lee Cheonbaek.”

“Please do.”

Who was Blood Wolf Sword Lee Cheonbaek? The man who had founded the Mount Heng Sword Sect with nothing but a single sword, and who now meant to become the ruler of an entire city. Enemy or not, there was no denying he was a Peak martial artist of the highest caliber.

*I want to fight him.*

But Jin Wikyung forced down the heat in his blood.

This was a battle with the family’s fate at stake. Competitive spirit had no place here.

“Wipeng.”

“Yes.”

Wipeng had already drawn his sharp, narrow blade and taken his place at Jin Wikyung’s side.

“You and I will handle the rest.”

“As you command.”

There was not a trace of hesitation in the answer. Jin Wikyung smiled faintly and drew his own sword—the family’s treasured blade, passed down through generations of the Jin Family of Taiyuan.

It was the only thing left behind by the father who had vanished one day without a trace.

*I’m going to travel around the Central Plains for a while.*

*Use this in the meantime.*

Remembering the letter that had been stuffed carelessly into the scabbard, Jin Wikyung felt his blood boil all over again.

*Travel around the Central Plains, my ass. You spent your whole life having fun.*

He didn’t even know where that so-called Family Head was, or what he was doing. And his second brother, thousands of li away, had probably only just received the letter.

*I have to protect them.*

Martial artists, maids, servants, children.

Jin Wikyung was the Family Head of the Jin Family of Taiyuan now. No one else.

Their deaths and their survival were his to carry, and his alone.

*We will win.*

Jin Wikyung’s eyes flared wide. Sword raised, an Azure Dragon’s Roar burst from his mouth.

“Don’t let a single one of them live!”

Whoosh, whoosh, whoosh!

The Jin Family’s masters kicked off the ground and leaped into the air. Taking that as the signal, a single fire arrow rose high behind them.

That was when dozens of figures stood up along the cliffs.

“Fire!”

Beneath arrows pouring down like a sudden rain, the fight between the masters who would decide the course of the battle began.

* * *

Blood Wolf Sword Lee Cheonbaek was a born martial artist.

With innate talent for martial arts and beastlike instincts, he had cut down his enemies and realized his ambitions one after another.

He had founded the Mount Heng Sword Sect and grown its strength by absorbing the surrounding factions one by one. His aim was to lay the foundation for a prestigious house that would one day be recognized even in the Central Plains.

*Sect Leader! The Young Master…*

Then, one day, his second son came home a corpse.

It had not been a fair duel. Deadly poison had taken him, and he had died with blood pouring from all seven orifices.

Lee Cheonbaek swore an oath.

He would kill and burn everything connected to the Jin Family of Taiyuan.

And then Jin Wikyung appeared before his eyes.

Lee Cheonbaek’s eyes blazed.

“You bastard—!”

He charged like a beast. The blade, holding sixty years of internal energy, shone milky white.

With this much power, it could cut through any armor, any divine weapon.

*That bastard dies here!*

Just as Lee Cheonbaek, sure of it, was about to swing—

“Oho. Sword Energy?”

A low voice, from behind him.

Lee Cheonbaek’s heart sank.

*How?*

To give up his back so cheaply. His reaction was lightning-fast. He drove the sword backward in a reverse grip.

Whoosh.

The blade stabbed empty air, and that bought him time. Only then could he see his opponent’s face.

A beard hanging down to his chest. A relaxed smile at the corners of his mouth.

A white-haired old man.

Lee Cheonbaek knew him at once.

“Blade of Flowers?”

The Head Elder nodded.

“I haven’t heard that name in a long time. Then you must be Lee Cheonbaek.”

“That’s right.”

Even as he answered, a chill ran down Lee Cheonbaek’s spine.

He didn’t dare look for Jin Wikyung, or check how the battle was going. Take his eyes off the old man, and he felt his head would come off on the spot.

*Coincidence? No.*

It was true that seeing Jin Wikyung had agitated him past reason. It was true that he had been impatient.

But Lee Cheonbaek was a Peak master.

A Peak master who had reached the realm of Sword Energy Frost Blade.

The answer was already clear.

*A master!*

Whether in one form or half a form, the old man in front of him was a master a league above Lee Cheonbaek.

Lee Cheonbaek tightened his grip on his beloved sword.

“I’ve heard much of your reputation.”

“Reputation? I’m nothing more than an old man in the back room.”

“Then why leave the back room?”

“You’re still a young fellow, so there’s a lot you don’t know. The older you get, the more you have to get moving now and then.”

Lee Cheonbaek ground his teeth at the Head Elder’s sly manner.

*Damn old man.*

He had been watching the Jin Family of Taiyuan for a long time.

He knew there was a faction centered on the Head Elder that opposed the Family Head. He had even privately hoped the family would split from within.

But things had gone the opposite of what he had expected.

*So when an outside enemy invades, they unite as one?*

Lee Cheonbaek stared at the Head Elder with heavy eyes, then opened his mouth.

“How strong are you?”

“As strong as you believe me to be.”

“Word games.”

“When I was called Blade of Flowers, I was thirty.”

At thirty, the Head Elder had already been a Peak martial artist.

Now he was a man of seventy. How had his martial arts changed since then?

After a moment’s thought, Lee Cheonbaek let out a wry laugh.

*I’m getting old, too.*

Blood Wolf Sword.

In his youth, Lee Cheonbaek had been unstoppable. Without an exceptional martial art or a respectable master, he had carved his way through everything on his own.

Even against an opponent a level above him, he never backed down. He charged like a wolf and tore out their throats.

*I lived half my life that way…*

At some point, people had started calling him Sect Leader instead of Blood Wolf Sword.

Blood relatives, subordinates, wealth.

The things he had to protect had piled up like a mountain.

Time spent training shrank; time spent on affairs grew. When it was time to act, he started thinking instead.

Just as he was now.

“Why are you laughing?”

Lee Cheonbaek answered the Head Elder’s question.

“I’m laughing because I find myself pathetic.”

“You’re afraid of me.”

Lee Cheonbaek nodded in silence.

“Were you afraid of death?”

“For a very brief moment.”

“And now?”

“I’m going to kill you.”

“Someone of your level won’t manage it.”

“You have to measure them to know which is longer, don’t you?”

“That’s what the short ones always say. They never realize that even after you measure, the result doesn’t change.”

“Your tongue is sharp.”

“Is it only my tongue?”

The Head Elder lowered his sword.

It looked like an ordinary blue-steel sword, but the moment it entered his hand, it began to give off a vicious killing edge.

“Come at me first.”

Lee Cheonbaek did not refuse.

The blade, having drawn in sixty years of internal energy, raised a shimmering haze of light.

The realm of Sword Energy Frost Blade—a realm countless martial artists dreamed of reaching.

Tssss.

The moment the Sword Energy rose three inches—about ten centimeters—Lee Cheonbaek’s body shot forward.

A unique martial art, perfected through countless real battles, unfolded from his fingertips.

Whoosh! Whoosh-whoosh-whoosh!

Boom!

Sword Energy hacked wildly in every direction. Screams burst from between the mounds of earth that erupted in an instant.

“Graaagh!”

They were the cries of martial artists caught in the gap.

Every voice was a young man’s.

A red warning light went on in Lee Cheonbaek’s mind.

*Behind!*

He spun and swung at the same time.

He saw the white beard fluttering in the wind.

And the sword in the old man’s hand.

Boom!

*Kh.*

Lee Cheonbaek fell back in a daze amid the thunderous crash. He was not even given time to feel the pain in his wrist.

Boom! Boom! Boom!

Every time the two swords met, thunder and lightning rolled.

Sword Energy poured out in a continuous stream, smashing the ground and tearing the wind.

Whoosh!

“What in the world is that…?”

The martial artists of both sides forgot they were fighting. They could only stare, slack-faced, at this staggering life-and-death duel.

In that moment, every one of them was thinking the same thing.

*Are those two really human beings like us?*

The ceaseless thunder. A feast of Sword Energy so dazzling it left them spellbound just to watch.

The movements of the two men at its center were faster and stronger than anyone they had ever seen.

Someone muttered, almost a groan.

“So this is a Peak master…”

To their eyes, it was a fight where either outcome would have made sense.

But the superiority in strength was obvious.

After some three hundred exchanges, the Head Elder’s sword changed.

Whoosh—slice!

“Ghk.”

Lee Cheonbaek bit down on his lip.

Blood streamed from the forearm the Head Elder’s sword had raked.

The strength drained from the hand on his sword.

*Of all things.*

He shifted the sword to his other hand at once, but he was a right-handed swordsman by nature.

Even at full power he would have been hard-pressed. Now that the arm he used to wield a sword was injured, the outcome was all but decided.

Boom!

Crack.

A single blow snapped his wrist.

His Sword Energy, weakened by the severe drain on his internal energy, could no longer stand against the Head Elder.

But Lee Cheonbaek did not give up.

*Not yet. It isn’t over yet.*

He had taken worse injuries than this, plenty of times.

Using the strength in his arm, his waist, his legs, Lee Cheonbaek swung his sword.

No—he tried to.

Slash!

This time, it was the knee.

The tendons had been cut, and the knee buckled slowly, with no regard for Lee Cheonbaek’s will.

His sword carved uselessly through empty air.

Shhk. Shhk-shhk-shhk.

His side. His shoulder. His chest.

Lightning stabbed and sliced through his whole body. The fierce Sword Energy did more than cut flesh and bone—it churned his insides.

“Bleeegh!”

Lee Cheonbaek vomited blood mixed with pieces of organ and looked up at the Head Elder through clouded eyes.

The old man’s face was impassive.

No joy at having put his opponent down. No delight that the war was ending.

To him, all of this was simply the natural result.

“Cough… So Shanxi’s Number One was standing right in front of me.”

“If you’re not Number One Under Heaven, you’re nothing more than a martial brute from the frontier. Neither you nor I have that kind of capacity.”

“Tell me what you want. I’ll give you my neck. I’ll make my men surrender, and I’ll seal the sect for ten years—or a hundred. So…”

“Impossible. What I want is annihilation. Complete annihilation, without a single blade of grass left standing.”

“Why…!”

“Don’t ask me that. If you had won, it would have been this family facing annihilation.”

Lee Cheonbaek glared at the Head Elder with bloodshot eyes.

He wanted to snap that wrinkled neck then and there.

But in his condition, all a man with wounds like his could do was wring out a voice.

“Jin Family of Taiyuan. You started this, didn’t you? You killed that boy—my son!”

“Ah, Lee Seogeun. That’s right. That child was where it began.”

The Head Elder wore a sardonic smile.

Even the master of the Mount Heng Sword Sect, one of the two powers splitting Shanxi between them, had failed to notice *their* intervention.

Not even with death at his doorstep.

—When you meet King Yama, ask him. Ask who killed Lee Seogeun.

The Sound Transmission burrowing into his ear made Lee Cheonbaek’s eyes flare wide.

“What does that mean…?”

It had been a thoroughly impulsive act.

Perhaps pity for Lee Cheonbaek, who was about to die knowing nothing.

Or perhaps nothing more than an old man’s whim.

—Fare for the road to the afterlife. Think it over on the long journey.

The Head Elder raised his sword.

The sunset beyond the winter ridge shattered into fragments along the blade.

*With this…*

With the death of the giant called Lee Cheonbaek, the Mount Heng Sword Sect would collapse.

Those who resisted would die. Those who surrendered would be taken.

One war would end like that…

And a new war would begin, at the very moment everyone was drunk on victory.

*It’s over.*

At last, the Head Elder’s sword moved.

Screeeech—!

A sharp sound tore the air.

Sensing the end, Lee Cheonbaek closed his eyes.

The blade, wrapped in blue Sword Energy, traced a beautiful line.

Slice.

But the tearing sound that had come first, and the direction of the sword, were both beyond Lee Cheonbaek’s expectations.

The Head Elder split a spear that came flying at his back out of nowhere, cutting it apart with Sword Energy.

An enraged roar burst from his mouth.

“Who the hell are you!”

The answer came the next instant.

“It’s me, you fucking bastard!”

The Head Elder saw the face of a young man standing tall on a low hill, and groaned.

“Jin Taekyung?”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 56`.

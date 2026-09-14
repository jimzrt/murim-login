# Master Edit Task — Chapter 29

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
| 혁무진    | **Hyuk Mujin**     |
| 이소군    | **Lee Seogeun**    |
| 조필     | **Jopil**          |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 창법     | **spear technique**                              |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 낭인     | **wandering martial artist**                     |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 진가창법   | **Jin Family's Spear Technique**       |
| 일격     | **One Strike**                         |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 칭호               | **Title**                      |
| 민첩               | **Agility**                    |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 흑산도 | **Black Mountain Blade** |
| 한엽 | **Han Yeop** |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 나발이고 | slang | Dismissive rejection of the preceding concern (to hell with X), not a neutral “or not.” | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 20–24

## Plot

The Jin Family and the Lower District Sect formalize a wartime alliance. In exchange for half of Mount Heng’s shops and exclusive rights to its pleasure district, the Lower District Sect stops selling Shanxi intelligence to other sects and devotes its resources to war intelligence. Wolhwa disguises the agreement by publicly claiming that she and Taekyung spent a passionate night together, presenting it as an unpaid Honghwaru tab. Her investigation has found neither evidence clearing Taekyung nor Lee Seogeun’s killer; she supports the Jin Family because either Taekyung is legitimate or the family is powerful enough to conceal the truth.

Taekyung recognizes Wolhwa’s coachman as Yama Whip, a Peak master. When the gate guards mistake Taekyung for the hero who helped Yama Whip defeat the Heavenly Axe, he encourages the story. The System reports that Poisoner rumors are fading, the Sleeping Dragon of Shanxi rumor is strengthening, and Taekyung gains 20 Fame. Meanwhile, Lee Cheonbaek, Mount Heng’s Sect Leader and Lee Seogeun’s father, expels the poison from his son’s body, vows revenge, and sends about two hundred armed martial artists toward the Jin Family.

Mount Heng’s attack begins with the murder of twenty-five children from the Jin Family’s Saneum, Eung-hyeon, and Sakju branches. The Head Elder calls the deaths necessary sacrifices and uses the Sleeping Dragon rumor and Taekyung’s supposed alliance with Yama Whip to force him into wartime service. Taekyung becomes leader of White Tiger Hall’s reconnaissance squad under the Head Elder’s faction and receives a repeating quest to earn 100 Merit.

The squad consists mostly of inexperienced second-rate martial artists. Taekyung appoints Level 22 Hyuk Mujin, who has killed five bandits, as deputy squad leader and assigns everyone numbers. He imposes a practical Hunter-style schedule, equips three members with wooden shields, and drills formations, dispersal, and all-out retreat. Hyuk mocks the retreat strategy and accuses Taekyung of causing the war. Taekyung knocks him unconscious with a sequence of slaps, then does so again when Hyuk attacks after waking in a hunter’s shelter during a blizzard. The rest of the squad accepts Taekyung’s methods and asks him to train them.

The squad is ordered to scout near Jeongyang and return within five days. A Lower District Sect messenger hawk reports that Jopil, One Question, One Kill, and a special detachment have appeared there. Jopil leads about fifty wandering martial artists in massacring survivors from the Sakju Branch, killing the defending martial artist and several women and children. He orders his First Rate subordinate Black Mountain Blade to pursue one escaping martial artist and two children toward Honju.

Fourteen-year-old Socheon flees with his younger sister, Soyul. Their mother led other survivors away earlier, while their father and the branch families were killed. Gong Yacheong, an old friend of Socheon’s father, guides the children and stays behind to delay the pursuers; his fate is unknown. The siblings reach the reconnaissance squad’s hunter’s shelter as more than twenty Mount Heng pursuers arrive. The System creates the Sudden Quest **Survivors of the Sakju Branch**.

Taekyung first orders an attack formation, then changes to a defensive formation so the squad can hold the enemy back while he claims the kills, EXP, and Merit. He charges alone through the low-level pursuers, using the Jin Family’s Manoeuvre and Spear Techniques and cycling through their forms. He finishes Level 32 Black Mountain Blade with Sky-Piercing Strike, completes the Survivors of the Sakju Branch Quest, receives substantial EXP and Merit, reaches at least Level 20, and triggers a Chain Quest.

## Continuity

- The Jin Family–Lower District Sect alliance lasts for the war. Its terms are half of Mount Heng’s shops, exclusive pleasure-district rights, and exclusive Lower District Sect intelligence support.
- Wolhwa is Eun Sowol, the Level 50 Branch Leader of the Lower District Sect’s Shanxi branch. Yama Whip is her Peak-level coachman.
- Lee Cheonbaek is Mount Heng’s Sect Leader, the Blood Wolf Sword, and Lee Seogeun’s father. He has committed Mount Heng to revenge.
- Taekyung leads ten reconnaissance-squad members in White Tiger Hall. The deployed group has eleven people including Taekyung. The group has nine sword users, one spear user—Level 13 Han Yeop—and no experienced shield user before Taekyung assigns three wooden shields.
- Hyuk Mujin is Level 22, has killed five bandits, and is Taekyung’s deputy squad leader. Han Yeop enthusiastically follows Taekyung’s orders.
- The squad is scouting near Jeongyang under a five-day return deadline. Taekyung’s standard movement cycle is two hours of travel followed by fifteen minutes of rest.
- Jopil, One Question, One Kill, commands about fifty wandering martial artists. Black Mountain Blade, his First Rate right-hand man, is dead.
- Socheon and Soyul survived the Sakju Branch massacre. Their mother’s fate and Gong Yacheong’s fate remain unresolved.
- Taekyung completed the Sudden Quest **Survivors of the Sakju Branch**, gained large EXP and Merit, levelled up repeatedly, and activated a Chain Quest. Its requirements and outcome remain unresolved.
- The war, the unidentified assassin who killed Lee Seogeun, the capsule’s purpose, the route home, and Murim’s death and resurrection rules remain unresolved.

## Translation Decisions

- Preserve **Lower District Sect**, **Branch Leader**, **Honghwaru**, **Yama Whip**, **White Tiger Hall**, **One Question, One Kill**, **Black Mountain Blade**, **Sakju Branch**, **Honju**, and **Jeongyang**.
- Keep the alliance terms precise: half of Mount Heng’s shops, exclusive pleasure-district rights, and exclusive wartime intelligence support.
- Render Taekyung’s staged introduction as: “Yama. Whip. Great Hero!”
- Preserve the repeating 100-Merit quest, the Sudden Quest **Survivors of the Sakju Branch**, and the Chain Quest as distinct System events.
- Retain Taekyung’s practical Hunter-style command, the numbered-squad joke, the formation commands “Form up,” and his EXP-driven decision to claim the enemies himself.
- Preserve the dark comedy and violence of the five-blow sequence, including Hyuk’s accusation and Taekyung’s grip holding him upright.
- Keep **Sky-Piercing Strike** as the final form of the Jin Family’s Spear Technique and retain “Splurt!” for the finishing impact.
- Render `반 시진` as “more than half a shichen,” with a brief factual footnote if used in the chapter translation.

### Prior accepted reading-copy tails

#### Chapter 27 tail (verified mastered)

…
since we started moving?* A sikyeong? Half a shichen? I couldn’t tell. In the dead of night, with darkness swallowing everything around us, even the passage of time was impossible to feel. With every step, one thought refused to leave my mind. *He must have left by now.* It was only natural. Gong Yacheong and I both knew it, and every member of the reconnaissance squad except Han Yeop had accepted it. Most importantly… I had a family waiting for me. There was a reality I would face once I got out. *Then why does this feel so damn awful?* My feet felt heavy. Not just because snow had piled up to my calves. Not because grass and branches blocked the path ahead. A mere NPC named Gong Yacheong kept weighing on my mind. I thought of his final smile. The cheap Quest without a single reward. I thought of Han Yeop defying my order, and Hyuk Mujin’s calm gaze pricked at my chest like a thorn. *It’s only natural. So why?* Because it was a game. Because it was only a game. *If I didn’t leave him behind, everyone would die. I’d die, too! You fucking bastards!* “Fuuuck…” The profanity that had been caught in my throat spilled out. Soyul stirred from her light sleep and mumbled something as she wrapped her arms around my neck. Her adorably tiny hands were cold. The sensation was so vivid it raised goose bumps across my skin. Too real to believe this was a game. Real enough to make me feel guilty for abandoning a single NPC. “…What a fucked-up game.” I turned around. “Where are you going?” I strode back the way we had come. Neither Socheon nor the faces of the reconnaissance squad members registered. That was why I didn’t notice the fleeting smile that crossed Hyuk Mujin’s face when he asked where I was going. Or that Han Yeop, who should have been at the very rear, was nowhere to be seen. “Huff. Huuuff.” I raced across the snow like the wind. And then I found him. Below the hill, Han Yeop was gritting his teeth and forcing one foot in front of the other even as he gasped for breath. Gong Yacheong, unconscious, was on his back. “You…” I didn’t know what to say. With a sigh, I grabbed Han Yeop’s hand and pulled him up. “Th-thank you.” *Shit…* *I don’t know anymore, either.* * * * This was a hidden retreat reserved for one person. Since becoming its owner thirty years ago, he had barred everyone else from entering. Over time, that had hardened into an unbreakable rule, and the others thought of it the same way. “How are things going?” The air trembled faintly as the two shadows conversed through Sound Transmission. “Smoothly. And on your end?” “Do you even need to ask?” “I wouldn’t expect otherwise.” “The Blood Wolf Sword. For a man with such an epithet, he’s surprisingly fond of his family.” “A wolf can still love its own blood. So?” “The vanguard alone numbers two hundred. A madman named Jopil is running wild as he pleases, but… it should be fine.” “Jopil, One Question, One Kill? The Blood Wolf Sword chose well.” “The wastrel young master is being chased all over the place. It wasn’t part of the plan, but this isn’t bad either.” “Hahahaha.” “Could it be…?” “That’s right. I sent him. Once the Lesser Family Head sees the severed head of the youngest brother he cherishes so dearly, he’ll change his mind.” “Whew. A heart as cold as poison, without blood or tears. You have my respect.” “Are you one to talk?” “I merely took one hopeless life.” “And thanks to that, a bloody storm will sweep across Shanxi?” “Isn’t that what you wanted?” “I can’t deny it. Yes. I’ve waited far too long.” “The fruit will be all the sweeter.” “I hope so.” “Ah, one more thing. The Lower District Sect has gotten involved.” “The Lower District Sect? How did they?” “The new Branch Leader has a sharp nose. Once this matter is settled, I plan to get rid of him.” “Be careful. No matter how formidable Heaven may be, you must never let your guard down…” At that moment, the wind stopped. The air quivered. “…I misspoke.” A long while passed before another Sound Transmission arrived. “You would do well to watch your words and actions.” The voice was as soft as a cat’s paw. But the listener could feel the razor-sharp blade hidden beneath it. “Let me apologize once more.” “Let’s end here for today. If any problems arise, I’ll visit you again in a few days.” The conversation ended there. The other person vanished without a sound or trace. *They’re like ghosts.* Sometimes, he wondered what their true identities were. How strong were they? Who were their members? But he soon shook his head. *That would only shorten my life.* He had endured years of hardship to reap the fruit. He couldn’t let mere curiosity ruin his great undertaking. *It truly has been a long time.* The shadow reached a hand toward the moon. Faint moonlight slipping between his fingers illuminated a silver beard. *Soon… everything will return to its proper place.* The Head Elder smiled with pleasure. [^1]: A shichen is a traditional time period of roughly two hours; a sikyeong is a shorter traditional interval.

#### Chapter 28 tail (verified mastered)

…
happen. Those bastards are painfully slow. It’ll take them half a shichen to catch up.[^2] By then, everything will be over.” One thing was certain. In the ending Jopil envisioned, his own death had no place. “Well?” “And if I refuse?” Jopil smiled softly. “I’ll be disappointed in you. Very disappointed.” I could more or less picture what would happen if he became disappointed. “Young friend, I have no grudge against you. No—if anything, I’m rather fond of you. Answer a few things truthfully, and I might even let you go.” “Wait. Let me go?” “Yes. I won’t harm you in any way. I’ll send you back in one piece.” “…Really?” “I’ll stake my neck on it. Is that enough?” The sincerity showed on Jopil’s face. Unpredictable psychopath or not, maybe everyone could walk out of this alive. “All right.” Even if the worst happened, what else could I do but fight? For now, I planned to buy some time and search for a weakness. “Good. A friend who listens to reason, haha.” Jopil clapped and laughed. The scabbard at his left hip swayed. *Right-handed. Swordsman.* I kept inputting the data in my head. “First, I’d like to ask your age.” “Twenty.” Jopil’s eyes went round. “My. To have reached that realm at twenty. Impressive.” I’d spent seven years as a Hunter without ever escaping F-rank, yet in this game, people treated me like a martial arts genius. It was a strange feeling. “Judging by your clothes, you seem to be from the Jin Family of Taiyuan.” I nodded readily. “Super First Rate at twenty. You wouldn’t be that famous Heaven Shaking Sword, so… your name?” “Jin Taekyung.” “Jin Taekyung. Jin Taekyung. I’ve heard that name somewhere. Ah!” Jopil had been turning it over. Then he exclaimed. “The wastrel Third Young Master! That’s you?” “I’m not a wastrel. These days, they call me the Sleeping Dragon.” “Puhahaha! I knew it. The Jin Family of Taiyuan, those rigid fools, poisoning someone? Please. I don’t know who set this board, but things are getting interesting.” Jopil looked at me, satisfied. “I’ve heard plenty of rumors about you. Was all of that a disguise?” “…Something like that.” “Good. A hidden blade, then. I like it. When did you start learning martial arts?” “Seven years.” Not entirely a lie. By Murim standards, Hunter combat methods were a kind of martial art too. “Seven years. And your master?” “Don’t have one.” “No master?” He studied me for a while, then said, “Doesn’t seem like a lie.” “You promised to spare me if I answered honestly. That was your promise, wasn’t it?” “Yes, it was. What an absurd yet entertaining story. A direct descendant of the Jin Family of Taiyuan, without a master, reaching that realm at twenty… My, my.” My mouth was bone-dry. I gripped the spear and scanned Jopil’s body. He was unbelievably riddled with openings. But was what I was seeing really all there was? *He could be baiting me into attacking first.* The thought went no further. Jopil suddenly burst out laughing. “Hahaha! Good. I like it. I’ll keep my promise.” He’d keep his promise? The thing I’d thought impossible was actually happening. I stared at Jopil in a daze. “No need to look at me like that. Truth is, at first I really wanted to kill you… But now that we’ve met, I find I want to watch you a little longer.” Jopil continued, his voice brimming with goodwill. “It’d be a waste to kill outstanding talent like this. Especially in a situation like this.” “A situation like this?” “Ah. You might not know. You’ll find out when you return. Go on, then. I hope you’ll have grown a little more by the next time we meet.” I could leave? He meant it? I backed away without dropping my guard. Jopil merely watched me with a smile. He looked like a fisherman letting a minnow go. *They say even if you walk into a tiger’s den, you live if you keep your head.* Who’d have thought Jopil’s wild-card personality would turn into an exit. Once I had a safe distance, the breath I’d been holding burst out. But there was no time to catch it. I had to leave this place a second sooner, if I could. “We’re moving. Hurry!” Then— “Hold on, young friend.” Jopil looked at me, puzzled. “What are you doing?” “What do you mean? Going back, like you promised…” “I only gave permission for you to leave. Alone.” “…What?” “I may not look it, but I’m in someone’s employ. I have to finish the mission I took on.” The mission. Don’t tell me. “The three survivors of the Sakju Branch. And those pieces of trash you call your subordinates. Leave them behind. I ought to be paid for two days’ work, don’t you think?” Eyes that had been clear as a child’s flashed. The next instant, they were a predator’s. “I’ll say this now. If you refuse, I’ll be very disappointed.” I stared blankly at Jopil, the reconnaissance squad, the young siblings, and the dying Gong Yacheong. Time was short, but after dozens of rounds of doubt and conflict, one line burst out. “Then be disappointed, you fucking bastard.” Jopil laughed savagely. [^1]: A zhang is a traditional Chinese unit of distance, roughly 3.3 meters. [^2]: A shichen is a traditional time period of roughly two hours.

## Korean source

```text
＃29화



한번 결정을 내리면 망설이지 않는 사람이 있다. 조필이 바로 그런 부류였다.

“솜씨 좀 볼까.”

한 마디를 툭 내뱉은 조필이 지면을 박찼다. 십여 장의 거리가 두 걸음 만에 사라진다. 놈의 허리춤에서 섬광이 뿜어졌다.

쉭!

‘이게 뭐…….’

생각보다 몸이 먼저 움직였다. 쭉 뻗은 창대가 섬광과 맞닿은 순간.

쾅!

굉음과 함께 몸이 뒤로 쏠렸다. 포탄처럼 날아가던 내 몸은 정찰조원들을 향해 날아갔다. 방패고 나발이고, 선두의 서너 명이 우르르 쓰러진다.

“으악!”

“조장! 괜찮으십니까!”

……괜찮겠냐.

‘와, 씨.’

진동이 가라앉지 않은 창대를 꽉 움켜잡았다.

섬광의 정체는 조필의 검이었다. 그리고 내 27년 인생을 통틀어 가장 빠르고, 강한 공격이었다.

‘막았는데도 이 정도라고?’

잠깐이라도 반응이 늦었다면 지금쯤 북망산을 등산하고 있었을 거다. 쿵쿵 뛰는 가슴을 진정시키며 일어났다.

조필은 웃고 있었다.

“실망인데. 이 정도밖에 안 되나?”

그나마 ‘이 정도’라서 막아 낼 수 있었던 공격이다. 앞서 스무 명을 쓸어버리고 레벨 업을 하지 않았다면 이미 죽었을지도 몰랐다.

‘시발, 잘못 걸렸네.’

내 경지는 이류다. 그럼에도 불구하고 지금까지 두 명의 일류 고수를 손쉽게 이겼다. 시스템으로 얻은 무공과 능력치로, 그리고 내가 쌓아 온 전투 경험으로.

하지만 단 한 번의 공격으로 알 수 있었다.

‘이놈은 달라.’

모든 면에서 압도당하는 기분이다. 조필은 이소군이나 흑산도와는 격이 다른 존재다. 죽음이라는 단어가 떠오를 정도로.

“겁먹었군.”

겁먹었다고? 내가?

나는 손을 바라보았다. 창의 진동은 멎었지만 창을 움켜쥔 손이 사시나무처럼 떨리고 있었다. 심장 소리는 너무 커서 모두에게 들릴 듯했다.

“그런 새가슴으로 어찌 풍진강호에서 살아남겠나.”

조필이 혀를 찼다.

“안 되겠군. 내가 힘을 좀 북돋아 주지.”

“뭐?”

“분노는 언제나 두려움을 이기거든.”

그 말을 이해하기도 전에 조필이 소매를 떨쳤다. 동시에 여러 개의 빛줄기가 튀어나왔다.

‘위험!’

머릿속 적색경보가 울리자마자 창을 휘둘렀다. 캉! 날카로운 소리와 함께 몇 개의 비수가 튕겨 나갔다.

하지만 모든 공격을 막을 수는 없었다.

“컥.”

정찰조원 중 하나가 목을 움켜잡았다. 손가락 너머로 펑펑 솟구치는 핏물과 비수 한 자루가 보였다.

“크륵. 조……장. 크르륵.”

피가래 끓는 소리와 함께 그가 무릎을 꿇었다. 아직 앳된 얼굴은 죽음에 대한 공포로 잔뜩 일그러져 있었다.

“사, 살려 주…….”

쉭, 퍽!

목과 미간에 비수가 박히고도 살아남은 사람은 없다. 그도 마찬가지였다.

철퍽. 이제 막 녹기 시작한 땅에 그가 얼굴을 박았다. 그리고 다시는 일어나지 못했다.

한순간에 벌어진 일이었다.

“가장 어려 보이기에 골랐는데…… 아끼던 수하였나?”

조필이 물음에 고개를 내저었다.

“아니.”

“그거 안타깝군.”

“사실 이름도 몰라.”

“수하라면서?”

“NPC니까. 이름도, 나이도 알 필요 없는.”

“뭐?”

나는 시신을 뒤집어 눕혔다. 얼굴에 묻어 있는 흙과 눈을 털어 준 다음 부릅뜬 눈도 감겨 주었다.

그리고 아직도 어리둥절한 얼굴의 조필에게 고백처럼 털어놨다.

“사실 만난 지 사흘밖에 안 됐어.”

“그런가?”

“그렇지.”

“그런데 자네…….”

조필이 웃으며 말을 이었다.

“왜 화가 나 있나?”

놈의 말이 맞았다. 뱃속에서부터 뭔가가 부글부글 끓어올랐다. 머리고 가슴이고 뜨겁게 달궈져서 무슨 말이라도 해야 했다.

‘저 녀석 이름이 뭐더라.’

정찰조에서 칠 호로 불리던 놈이다. 싫다는 녀석에게 억지로 방패를 들게 하고 틈틈이 수련시켰다. 어린 녀석이라 몇 번 칭찬해 주니 좋아서 헤벌쭉 웃곤 했었다.

‘이름이 뭐였지.’

나는 끝내 기억해 내지 못했다.

같은 고시원 주민들 이름도 다 모르는데 고작 며칠 본 NPC 따위. 기억할 이유도, 필요도 없었다.

‘그런데…….’

짜증이 난다. 화가 난다. 게임에서는 다를 줄 알았는데, 여기서도 내 팀원을 지키지 못했다는 사실이.

애써 훈련시킨 이유도, 지난 며칠간의 노력도 물거품처럼 사라졌다. 나는 입을 벌려 뜨거운 숨을 토해 냈다.

“개새끼. 넌 뒈졌어.”

마지막 하나 남은 벽곡단을 씹어 삼켰다. 기력이 회복되었다는 시스템 메시지와 함께.

쿵-

나는 땅을 박차고 날았다.



* * *



조필은 사각(死角)에서 솟구친 창날을 튕겨 냈다.

캉! 카가각.

빠르고, 힘 있다. 기본기가 튼튼하고 전투 감각도 제법이다.

항산검문의 애새끼나 흑산도처럼 근본 없는 낭인이 당해 낼 수 있는 놈이 아니다.

‘태원진가…… 썩어도 준치라 이건가?’

조필은 여유롭게 창날을 피해 내며 생각했다.

태원진가의 몰락은 어제오늘의 일이 아니다. 한때 산서성을 아우르던 위엄은 이미 사라졌고 남은 건 빛바랜 과거의 영광과 가물에 콩 나듯 출현하는 인재뿐이다.

눈앞의 진태경 같은.

‘재미있는 놈을 길렀어.’

약관에 이 정도 솜씨라. 이미 산서성 제일의 고수 소리를 듣는 진천검만큼은 못하지만 흥미로운 녀석이다.

나이를 떠나 보면 공력도, 무공도 어중간한데…… 싸울 줄 안다. 물러설 때, 나아갈 때를 정확히 알고 기회가 오면 투귀처럼 달려든다.

바로 지금처럼.

“핫!”

쉭- 팡!

얼굴을 노리고 번뜩이는 창날이 허공을 관통했다. 터지는 소리와 함께 조필의 머리카락이 흩날렸다.

‘허, 이것 보게.’

창을 들고 찌르는 일련의 동작이 간결하고 물 흐르듯이 이어진다. 그뿐인가, 부드럽게 전신을 비틀어 힘을 폭발시키는 저 움직임은 전사경(纏紗勁)이다. 아직은 서툴지만 틀림없다.

‘약관에 전사경을?’

타고난 감각에 노강호를 연상시키는 전투 경험. 그리고 재능.

무서운 잠재력이다. 조필이 그렇게 생각했을 때였다.

진태경이 굳은 얼굴로 중얼거렸다.

“시발, 뭐야 이거.”

“…….”

조필의 발이 꼬였다. 아차, 하는 순간 진태경의 창이 뱀처럼 파고들었다. 훌쩍 뒤로 거리를 벌렸지만 창에 실린 공력은 보통이 아니었다.

찌이이익!

처음으로 허용한 공격이다. 상의가 길게 갈라지며 가슴팍이 훤히 드러났다.

“아, 아깝다. 끝낼 수 있었는데.”

“…….”

아까워? 끝내? 다름 아닌 나, 일문일살 조필을 상대로?

입맛을 다시는 진태경을 보며 조필은 극렬한 분노를 느꼈다.

“이노오오옴!”

공력이 실린 고함에 숲속이 진동했다. 눈깔이 홱 뒤집힌 조필이 진태경을 향해 돌진했다.



* * *



조필의 옷을 길게 잘라 낸 순간, 시스템 알림이 울렸다.

띠링.



- [Lv.??? 조필]이 [광분]합니다!

- 지속 시간 동안 힘과 민첩이 상승합니다!



젠장. 여기서 더?

“크아아아!”

쾅- 콰광!

일격, 일격이 굉음과 함께 내리꽂힌다. 지면이 뒤집히고 나무가 뿌리째 뽑혀 나갔다. 눈깔이 허옇게 뒤집힌 조필은 말 그대로 미친놈처럼 날뛰었다.

‘보통 미친놈이 아니니까 문제지.’

자그마치 절정 고수씩이나 되는 미친놈이다. 일대일 대결 시 전투 능력치를 10% 향상시켜 주는 칭호, [승부사]가 아니었다면 지금까지 버티지도 못했을 것이다.

콰아앙!

저건 무공이 아니다. 폭격이지.

그러나 지금의 조필에게 정교함은 찾아볼 수 없다. 간결하고 빠른 동작에 [광분]으로 인해 과한 힘이 들어가다 보니 동작이 크고 허점이 많아진 것이다.

‘단 한 번의 틈만 보이면 되는데…….’

문제는 그 틈이 안 보인다. 꼭지가 돌아서 주변을 초토화시키는데, 피하는 게 고작이고 막을 엄두도 나지 않는다.

사정권에 들어가면 갈가리 찢겨 나갈 게 뻔했다.

“조장!”

“저희가 가겠습니다!”

달려오는 정찰조원들을 향해 황급히 손을 내저었다.

“야, 오지 마! 오지 마! 물러나라고!”

저놈들이 미쳤나. 여기가 어디라고 와? 이미 허무하게 한 명을 잃었다. 정찰조의 전멸은 내가 바라는 결과가 아니다.

그리고…….

‘저놈들 오면 승부사 칭호 효과가 사라지잖아!’

[승부사]는 일대일 대결 시에만 효과가 적용된다.

지금도 근근이 버티는 형국인데 칭호 효과까지 사라지면 얼마나 더 견딜지 모르겠다.

“돌아가라고 이 새끼들아!”

고함과 함께 잽싸게 옆으로 몸을 날렸다. 어김없이 조필의 검이 지면을 박살 냈다.

콰직!

“조장!”

한 박자 늦게 혁무진의 외침이 들렸다. 내 만류가 무색하게도 녀석은 이미 달려오고 있었다. 그 뒤로 결연한 얼굴의 한엽도 보였다.

“야, 오지……!”

“조필, 이 악독한 놈!”

“조장에게서 물러나라!”

그러나 한발 늦었다. 온 힘을 다해 달려온 혁무진과 한엽이 내게 정신이 팔린 조필을 향해 각자의 병장기를 찔러 넣었다.

“죽어라!”

검과 창. 창과 검. 미리 연습이라도 한 것처럼 좋은 타이밍에 좋은 공격이다. 하지만 딱 하나, 상대가 나빴다.

“감히! 이 쥐새끼들이!”

조필의 대응은 신속했다. 검을 그 자리에 꽂고 돌아섬과 동시에 양손으로 두 개의 무기를 후려친 것이다.

검과 창에 맨손으로 맞서는 건 자살행위다. 그러나 이곳 무림에서는 달랐다. 정확히는 절정 고수인 조필은 달랐다.

쩌적- 콰직!

고작 옆면에 손바닥이 닿았을 뿐인데, 조필에게 닿기도 전에 혁무진의 검이 조각나서 흩어졌다. 한엽은 창두가 싹둑 잘려 나간 창을 보고 경악한 얼굴로 변했다.

조필의 곧게 핀 수도(手刀)가 불러온 결과였다.

“이게 무슨.”

“말도 안…….”

말이 끝나기도 전에 조필의 양손이 두 사람의 가슴팍을 후려쳤다. 그들은 피 분수를 뿜으며 나무에 처박혔다.

“죽여 주마.”

스산하게 웃는 놈의 얼굴에선 더 이상 흰자위가 보이지 않았다. 광분이 풀리고 제정신으로 돌아온 것이다.

“씨발…….”

점입가경. 첩첩산중. 사면초가. 조필 개새끼.

상황은 점점 최악으로 치닫고 있었다. 막으려면 내가 나서야 했다.

“조필-!”

전력으로 끌어 올린 공력이 빠르게 전신으로 뻗어 나간다. 땅을 박차고 놈을 향해 쏘아졌다. 조필이 활짝 웃으며 입을 열었다.

“그래, 네놈부터 죽여 주마.”

하지만 나도 믿는 구석이 있었다.

‘지금 놈은 맨손이다.’

광분 상태에서 저지른 패착이다. 그리고 나는 놈이 등 뒤의 검을 뽑아 휘두르기 전에 모든 걸 끝낼 자신이 있었다.

다음 순간, 있는 힘을 다해 단전 안의 공력을 끌어 올렸다. 모든 힘을 오로지 창끝. 일점(一點)에 집중하고 뻗어 냈다.

“죽엇!”

진가창법의 마지막 초식, 천관일. 하늘을 뚫는데 조필의 심장이라고 못 뚫을까. 나는 확신했다.

‘이걸로…… 끝이다.’

느려진 세상 속에서 조필의 얼굴이 보였다. 놈은 웃고 있었다. 그 미소를 본 순간 깨달았다.

뭔가 잘못됐다.

카가가각.

내 창보다 조필의 검이 더 빨랐다. 피를 머금은 붉은 칼날이 창대를 밀어 내며 안쪽으로 파고든다. 공력이 실린 창날이 허공을 찌른 순간.

서걱.

섬뜩한 소리와 함께 가슴이 시원해졌다. 이내 격통과 함께 뿜어지는 핏물. 다행히 마지막 순간 몸을 뺀 덕분에 치명상은 피했다.

‘빌어먹을.’

뭐가 어떻게 된 거지? 비틀거리며 물러나는 내게 조필이 달려들었다.

쉬쉬쉭!

붉은 검광이 쏟아진다. 하나같이 제대로 보이지도 않을 만큼 빠르고 강력하다. 나는 이를 악물고 창을 휘둘렀지만 기세와 무공, 모두 조필이 앞섰다.

서걱. 푹. 촤악.

번갯불이 전신을 가로질렀다. 어깨와 무릎, 옆구리를 쑤시고 베고 꿰뚫은 검신은 핏물과 함께 빠져나왔다.

“커헉.”

“무기를 놓치지 않았군. 칭찬해 주지.”

조필이 덧붙였다.

“이것도 버티면.”

다음 순간, 놈의 손이 내 가슴을 때렸다.
```

## Current accepted English baseline

```markdown
# Chapter 29

Some people don’t hesitate once they’ve made a decision. Jopil was one of them.

“Let’s see what you’ve got.”

Jopil tossed the line out and kicked off the ground. Ten-odd zhang of distance vanished in two steps.[^1] A flash burst from his waist.

*Whoosh!*

*What the…?*

My body moved before I could think. The moment my outstretched spear shaft met the flash—

*Boom!*

A thunderous impact threw me backward. I shot toward the reconnaissance squad like a cannonball. Forget the shields—the three or four men in front went down in a heap.

“Argh!”

“Squad Leader! Are you all right?”

…Would I be all right?

*Wow, shit.*

I clenched the spear shaft. It still hadn’t stopped shaking.

The flash was Jopil’s sword. And in all twenty-seven years of my life, it was the fastest, strongest attack I had ever taken.

*It hit that hard even though I blocked it?*

If my reaction had been even a moment slower, I would have been hiking up Mount Beimang by now.[^2] I calmed my pounding heart and got back on my feet.

Jopil was smiling.

“I’m disappointed. Is that all you’ve got?”

The only reason I had been able to block it was because it was merely “that much.” If I hadn’t leveled up after mowing down those twenty men, I might already have been dead.

*Fuck. Wrong opponent.*

My realm was Second Rate. Even so, I had easily beaten two First Rate masters so far—with the martial arts and stats I’d gained through the System, and with the combat experience I had built up.

But I could tell from that one attack.

*This guy is different.*

I felt outmatched in every way. Jopil was on a completely different level from Lee Seogeun or Black Mountain Blade.

Different enough that the word *death* came to mind.

“You’re afraid.”

Afraid? Me?

I looked at my hand. The spear had stopped vibrating, but the hand gripping it was shaking like an aspen leaf. My heartbeat was so loud it felt as though everyone could hear it.

“How will you survive in the martial world with a chicken heart like that?”

Jopil clicked his tongue.

“This won’t do. I’ll give you a little boost.”

“What?”

“Anger always beats fear.”

Before I could even understand what he meant, Jopil flicked his sleeve. Several streaks of light shot out at once.

*Danger!*

The instant a red alert went off in my head, I swung my spear. *Clang!* A few throwing knives bounced away with a sharp ring.

But I couldn’t stop every attack.

“Guh.”

One of the reconnaissance squad clutched his throat. Blood fountained between his fingers, and I saw a throwing knife buried there.

“Grrk. Squ… Squad Leader. Grrk.”

He dropped to his knees, gurgling on blood. His still-boyish face was twisted with the terror of dying.

“P-please, save me…”

*Whoosh. Thunk!*

No one survived throwing knives to the throat and between the eyes. He was no exception.

*Splat.*

He planted his face in the ground, which had only just begun to thaw.

He never got up again.

It had all happened in an instant.

“I picked him because he looked the youngest… Was he a subordinate you cherished?”

I shook my head at Jopil’s question.

“No.”

“That’s a shame.”

“I don’t even know his name.”

“You called him a subordinate.”

“He was an NPC. No need to know his name or his age.”

“What?”

I turned the corpse onto his back. After brushing the dirt and snow from his face, I closed his staring eyes.

Then I spilled it to Jopil, who still looked bewildered, like a confession.

“We’ve only known each other three days.”

“Is that so?”

“That’s right.”

“Then…”

Jopil smiled and went on.

“Why are you angry?”

He was right. Something was bubbling up from the pit of my stomach. My head and chest were burning, and I had to say something.

*What was that kid’s name again?*

He was the one they called Number Seven in the reconnaissance squad. I had forced a shield on him when he didn’t want one and trained him whenever I had the chance. He was young, so a few words of praise had him breaking into a goofy grin.

*What was his name?*

In the end, I couldn’t remember.

I didn’t even know all my goshiwon neighbors’ names.[^3] Why would I remember some NPC I had only known for a few days? There was no reason to, and no need.

*But…*

I was annoyed. I was angry. I had thought it would be different in a game, but even here I hadn’t protected my teammate.

The reason I had gone out of my way to train him, the work of the past few days—gone like foam. I opened my mouth and let out a hot breath.

“You son of a bitch. You’re dead.”

I chewed and swallowed the last fasting pill I had.

Together with the System message that my energy had recovered—

*Boom.*

I kicked off the ground and launched.

* * *

Jopil knocked away the spearhead that had surged up from his blind spot.

*Clang! Skrrratch.*

Fast, and strong. His fundamentals were solid, and his combat sense was quite good.

He was not someone a rootless wandering martial artist like that Mount Heng Sword Sect brat or Black Mountain Blade could handle.

*The Jin Family of Taiyuan… even rotten, still a junichi, is that it?*[^4]

Jopil slipped the spearhead aside at his leisure and thought.

The fall of the Jin Family of Taiyuan was nothing new. The prestige that had once covered Shanxi was already gone. All that remained was faded glory from the past, and talent that turned up once in a blue moon.

Someone like the Jin Taekyung in front of him.

*They’ve raised an interesting one.*

This much skill at twenty. He still couldn’t match the Heaven Shaking Sword, already called Shanxi’s greatest master, but he was an interesting kid.

Leave age out of it, and his internal energy and martial arts were both middling… but he knew how to fight. He knew exactly when to back off and when to press, and when a chance came, he charged like a fighting demon.

Just like now.

“Ha!”

*Whoosh—Boom!*

The spearhead flashed at his face and punched through empty air. With a bursting crack, Jopil’s hair flew.

*Well, look at this.*

The sequence of gripping the spear and thrusting was compact, flowing like water. And that movement—smoothly twisting his whole body before exploding the force—was silk-reeling force.[^5] He was still clumsy with it, but there was no mistaking it.

*Silk-reeling force at twenty?*

Innate sense, combat experience that called to mind an old martial-world veteran, and talent.

Frightening potential.

That was what Jopil was thinking when Jin Taekyung muttered with a stiff face,

“Fuck, what is this?”

“…”

Jopil’s feet tangled.

The instant he thought *ah, shit*, Jin Taekyung’s spear slid in like a snake. He hopped back and opened the distance, but the internal energy on that spear was no joke.

*Riiip!*

It was the first attack Jopil had allowed through. His upper robe split in a long gash, baring his chest.

“Ah, so close. I could’ve finished it.”

“…”

*So close? Finished it? Against me—Jopil, One Question, One Kill?*

Watching Jin Taekyung smack his lips, Jopil felt a violent surge of rage.

“Youuu bastard!”

His shout, loaded with internal energy, shook the forest. His eyes rolled back as he charged at Jin Taekyung.

* * *

The moment I cut a long gash through Jopil’s clothes, the System notification rang.

*Ding.*

> **System**
>
> **Lv.??? Jopil** enters **Berserk**!
>
> Strength and Agility increase for the duration!

*Damn it. Even more?*

“Graaaaah!”

*Boom! Boom!*

Blow after blow crashed down with a roar. The ground overturned, and trees were ripped out by the roots.

With his eyes rolled completely white, Jopil rampaged like a madman.

*The problem is, he’s no ordinary madman.*

A madman who happened to be a Peak master, no less. If I hadn’t had the **Gambler** Title, which increased my combat stats by 10% in a one-on-one, I wouldn’t have lasted this long.

*Boom!*

That wasn’t martial arts.

It was a bombardment.

But there was no precision in Jopil now. His movements were simple and fast, but the extra strength from **Berserk** had made them big and left him full of openings.

*I just need him to show me one opening…*

The problem was, I couldn’t see one.

He had completely lost it and was turning the area around us into a wasteland. All I could do was dodge. I didn’t even dare to block.

Step into range and I would be shredded. That much was obvious.

“Squad Leader!”

“We’ll go!”

I hurriedly waved off the reconnaissance squad members running toward me.

“Hey, don’t come! Don’t come! Fall back!”

Had they lost their minds? Coming *here*?

We had already lost one man for nothing. Wiping out the reconnaissance squad was not the result I wanted.

And besides—

*If those guys come over here, the Gambler Title’s effect disappears!*

**Gambler** only applied in a one-on-one.

I was barely hanging on as it was. If the Title’s effect vanished too, I had no idea how much longer I could last.

“Get back, you bastards!”

I shouted and flung myself sideways. Sure enough, Jopil’s sword smashed the ground to pieces.

*Crack!*

“Squad Leader!”

Hyuk Mujin’s shout came a beat late. For all I had tried to stop him, he was already charging. Behind him, I saw Han Yeop with a set, determined face.

“Hey, don’t—”

“Jopil, you vile bastard!”

“Get away from the Squad Leader!”

But it was a step too late. Hyuk Mujin and Han Yeop, who had come running with everything they had, drove their weapons at Jopil, who was preoccupied with me.

“Die!”

Sword and spear. Spear and sword.

Good timing, good attacks, like they had practiced it beforehand. There was just one problem.

They had the wrong opponent.

“How dare you, you rats!”

Jopil’s response was instant. He drove his sword into the ground where he stood and, in the same turn, smashed both weapons with his bare hands.

Going at a sword and a spear empty-handed was suicide.

But this was Murim.

More precisely, Jopil was different because he was a Peak master.

*Crack—Crunch!*

His palm had only brushed the side of the blade, and Hyuk Mujin’s sword still shattered into pieces before it reached him. Han Yeop stared in horror at his spear, the head sliced clean off.

That was Jopil’s straightened knife-hand.

“What is this?”

“That’s impossible…”

Before they could finish, Jopil’s hands slammed into both their chests.

They smashed into trees, spraying fountains of blood.

“I’ll kill you.”

On that chilling smile, the whites of his eyes were gone.

Berserk had worn off. He was back in his right mind.

“Fuck…”

From bad to worse. Mountains on mountains. Surrounded on all sides. Jopil, you son of a bitch.

The situation was sliding toward the worst possible outcome. If anyone was going to stop him, it had to be me.

“Jopil—!”

The internal energy I had pulled up at full strength raced through my whole body. I kicked off the ground and shot toward him.

Jopil grinned wide.

“Right. I’ll kill you first.”

But I had something to count on.

*He’s empty-handed right now.*

*A mistake he had made while Berserk. And I was sure I could finish everything before he retrieved the sword from the ground and swung it.*

The next instant, I hauled up every bit of internal energy in my dantian. I focused all of it on a single point—the spear tip—and thrust.

“Die!”

The final form of the Jin Family’s Spear Technique, Sky-Piercing Strike.

If it could pierce the heavens, why couldn’t it pierce Jopil’s heart?

I was sure of it.

*This is it… the end.*

The world slowed, and I saw Jopil’s face.

He was smiling.

The moment I saw that smile, I knew.

Something was wrong.

*Skrrrng.*

Jopil’s sword was faster than my spear.

The blood-wet crimson blade shoved my spear shaft aside and drove inward. The instant my internal-energy-charged spearhead stabbed empty air—

*Slash.*

A chilling sound, and my chest felt cool. Then came the searing pain, and the blood bursting out.

Fortunately, I had jerked back at the last moment and avoided a fatal wound.

*Damn it.*

What the hell had just happened?

As I staggered back, Jopil charged.

*Whoosh-whoosh-whoosh!*

Crimson sword-light poured down. Every flash was so fast and strong I could barely see it.

I gritted my teeth and swung my spear, but Jopil had the edge in both momentum and martial arts.

*Slash. Thunk. Splurt.*

Lightning cut across my whole body. The blade stabbed my shoulder, slashed my knee, and punched through my side before coming back out with a spray of blood.

“Guh.”

“You didn’t drop your weapon. I’ll give you that.”

Jopil added,

“If you can take this, too.”

The next instant, his hand slammed into my chest.

[^1]: A zhang is a traditional Chinese unit of distance, roughly 3.3 meters.

[^2]: Mount Beimang is a burial mountain; hiking it means being dead.

[^3]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.

[^4]: A junichi is a quality fish; even rotten, it is still a quality fish.

[^5]: Silk-reeling force is a method of twisting the entire body in a continuous, coiling motion to release power.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 29`.

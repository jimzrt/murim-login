# Master Edit Task — Chapter 39

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
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 월화     | **Wolhwa**         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 로그인              | **Login**                      |
| 로그아웃             | **Logout**                     |
| 동기화              | **Synchronization** / **Sync** |
| 몬스터     | **monster**           |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 30–34

## Plot

Taekyung survives Jopil’s Flame Divine Palm and uses Inventory daggers to sever Jopil’s Achilles tendons and pierce his dantian, causing qi deviation. When Jopil burns his life for one final attack, Taekyung awakens the hardened third energy in his dantian, channels it through the broken Sharp Spear, and uses **Thrust with All My Might** to kill him. The skill’s destructive power exceeds Taekyung’s body’s limits, leaving him critically injured.

Taekyung remains unconscious for five days and confronts, in a nightmare, the guilt surrounding a disastrous modern-world Gate raid where his team died after he insisted on entering the boss zone. Wipeng reports that the reconnaissance squad and the Sakju Branch survivors returned safely. The squad member killed by Jopil was an orphan who dreamed of becoming Number One of All Time; Wipeng urges Taekyung to remember him and live his share as well.

The Jin Family wins a major battle at Honju, where one hundred elites defeat two hundred Mount Heng vanguard troops. Wipeng and Jin Wikyung each kill one of the Mount Heng Twin Devils, while the Mount Heng Lesser Family Head escapes. Jin Wikyung publicly celebrates Taekyung as the Sleeping Dragon of Shanxi, though the family’s rumor greatly exaggerates his victory.

Taekyung recovers rapidly after consuming a hundred-year snow ginseng. He reaches Level 30, has fifteen years of internal energy, and remains Second Rate until Wikyung explains that martial arts begin with belief. Realizing he has trusted the System’s label instead of his own achievements, Taekyung reaches First Rate. His martial arts advance by one stage, his body and meridians improve, his dantian expands, and he gains two levels. **Thrust with All My Might** evolves into the Peak, Second-Stage Skill **One Flash**, whose cost can be adjusted but whose overuse can leave him helpless.

Mount Heng gathers roughly five hundred fighters and plans to march on Taiyuan. The Jin Family will march north in two days, aided by the Five Gates of Shanxi, and strike before Mount Heng’s reinforcements join its main force. Taekyung accepts the **Rear Guard Defense** Quest, deliberately cultivates public awe to gain Fame, and goes to Medicine King Hall while still short of the Fame required for Logout.

## Continuity

- Jopil, One Question, One Kill, is dead. He was the nineteenth-generation successor of the Fire Gate Clan.
- Taekyung survived the fight but suffered severe damage to his qi and blood channels. The awakened hardened third dantian energy remains a major but dangerous power source.
- **Thrust with All My Might** evolved into **One Flash**, a Peak, Second-Stage Skill with adjustable stamina and internal-energy costs.
- Taekyung is now First Rate, has reached Level 30 and gained two additional level-ups, and possesses fifteen years of internal energy. His Fame remains below 500, so Logout is still unavailable.
- The reconnaissance squad and Gong Yacheong, Socheon, and Soyul returned safely. Hyuk Mujin and Han Yeop survived with serious but nonfatal injuries.
- The unnamed squad member killed by Jopil was an orphan; his body was recovered and buried, and his dream was to become Number One of All Time. Wipeng’s dream is Number One Under Heaven.
- Taekyung’s modern-world team died during a Gate raid after he insisted on entering the boss zone; he alone survived.
- The Jin Family defeated Mount Heng’s vanguard at Honju. Fewer than thirty Mount Heng fighters escaped, Jin Family casualties were similar in number, and Mount Heng lost three Peak masters. The Lesser Family Head escaped.
- Wipeng and Jin Wikyung killed the Mount Heng Twin Devils, both Peak masters.
- Mount Heng now has about five hundred assembled fighters, including hired wandering martial artists, black-market fighters, and mounted bandits. Lee Cheonbaek intends to march on Taiyuan and suppress rumors of Taekyung’s victory over Jopil.
- The Jin Family will march north in two days. The Five Gates of Shanxi has pledged support, including the Three Paths Sect. The enemy force could reach about one thousand after reinforcements join the Blood Wolf Sword’s main force.
- Taekyung accepted the **Rear Guard Defense** short-term Quest and is expected to command the rear guard.
- The capsule’s purpose, route home, and the limits of Murim’s death and resurrection rules remain unresolved.
- The Head Elder’s Sound Transmission accomplice and the full purpose of their plan remain unidentified.
- Medicine King Hall entry is restricted to authorized personnel; Taekyung has gone there seeking additional Fame.

## Translation Decisions

- Preserve **Flame Divine Palm**, **Fire Gate Clan**, **qi deviation**, **Inventory**, **Sharp Spear**, **Thrust with All My Might**, and **One Flash**.
- Keep **First Rate**, **Second Rate**, **Peak**, **Grade**, **Level**, **Fame**, and **Logout** distinct according to established System terminology.
- Preserve Wipeng’s “live his share as well” counsel and the contrast between Taekyung’s guilt, dark humor, and growing responsibility toward Murim’s people.
- Retain **Sleeping Dragon of Shanxi**, **Mount Heng Twin Devils**, **Five Gates of Shanxi**, and **Three Paths Sect**.
- Preserve the exaggerated public rumor, Wikyung’s destructive affection, and Taekyung’s deliberate Fame-seeking as dark action-comedy.
- Keep the modern Hunter terms **Gate**, **Demon Realm**, **Magic Gems**, **boss zone**, and Hunter grades distinct from Murim terminology.
- Preserve the goshiwon footnote and the established gold-spoon/God-Spoon wordplay where relevant.

### Prior accepted reading-copy tails

#### Chapter 37 tail (verified mastered)

…
nose. > **System** > > Achieve Fame 500 (497/500) I never thought the number 1 could feel this precious. In a voice that had aged all of a sudden, I muttered, “I’m going, I’m going, going home now…” “Now you’re even talking to yourself. Have you lost your mind?” Hyuk Mujin clicked his tongue, then his eyes went round. “What’s that? I’ve never seen those before.” “This?” I pointed in turn at the old book and the small case sitting on the rock. “One’s a martial arts manual. The other’s an elixir.” “Whoa. Really?” I explained in a drained voice to the guy whose eyes were halfway out of his head. “The manual’s a Supreme Peak martial art, and if you absorb the elixir properly, it’ll give you thirty years of internal energy.” “What?” “But they say if you take the elixir wrong, you’ll burn to death. You want it?” “Uh, right…” Judging by that unimpressed face and the snout sticking out a good five feet, he didn’t believe a damn word I was saying. *Well, if someone suddenly came at me with a Supreme Peak martial art and a thirty-year Fireball elixir, I’d figure it was a joke too.* “You really won’t eat it? It’s good stuff.” “Oh, I’m fine. Learn plenty of that Supreme Peak martial art, and be sure to chew your elixir thoroughly.” “I don’t need this kind of thing anymore.” “Of course. You’re the Sleeping Dragon.” Normally I would have smacked him in the back of the head. Right now I didn’t feel much of anything. *Is this how a short-timer sergeant feels?[^1]* At the same time, I felt strange. Was it the aftereffect of everything I’d been through? It had only been a little over a month, but it felt hazy and distant, as if I’d been here a year. I started tracing back through old memories. *I first opened my eyes at Honghwaru.* That was where I met Wolhwa for the first time and realized I was trapped in this game. Even now, thinking about that moment gave me goose bumps. *I really thought I was going to lose my mind.* It had taken me three days just to decide to go to the Jin Family of Taiyuan. And the guy I met there was this one—Hyuk Mujin. Smack! “Argh! Why did you hit me?” “Hmm. Just thought of the old days.” “What old days?” “Nope. Not telling. Get back already.” “What are you, some back-alley thug? Just because your martial arts are a bit strong, you think you can oppress people like this?” As Hyuk Mujin threw a fit, everyone’s eyes turned toward us. Even the reconnaissance-squad members who had been watching like it was none of their business jumped in. “What are you two talking about?” “Dunno. The deputy squad leader must have done something wrong.” “Hey, I didn’t do anything!” “This is Murim. Being weak is a crime.” “But should we even be doing this?” At someone’s words, silence fell for a moment. “True. Waiting here is our mission, but…” The tension and fear they had been suppressing with forced smiles hung in the air. Even I, who would soon be returning to the real world, felt uneasy with Jin Wikyung’s face flickering through my mind. How much worse must it be for these guys? There was only one thing I could say. “I trust my big brother.” *Big brother.* This time, I put my heart into the word. Jin Wikyung had been the greatest source of strength I’d had in this place. Maybe I simply wanted to shake off that unease, even if only like this. The faces that had stiffened for a moment relaxed. “We feel the same.” Hyuk Mujin slipped in as well. “I trust the squad leader more.” “Wow. Deputy squad leader, that side-switching of yours is really something.” “You little bastards. Is there anyone here who doesn’t owe the squad leader their life?” “Well, when you put it that way, what can we say?” “I trust the squad leader too. Honestly, I knew all along, even when you were playing the thug. I thought, *Ah, that man is the Sleeping Dragon.* I could tell right away.” I felt strange. *They say even dried squid gives water if you squeeze it. Who knew I’d feel something like this toward NPCs in a game?* *Well, honestly… it doesn’t feel bad.* Suddenly I wondered about Jin Wikyung, somewhere beyond those mountains. Had the battle started? If so, which side was winning? And I wasn’t the only one thinking that. “By now, the battle must have started.” It was Gwak Jun of the Three Paths Sect. Unlike before, he was wearing black martial robes. *Was that what this guy originally wore?* At my look, Gwak Jun shrugged. “I like this sort of thing. Easy to move in, and even if a little blood splatters, it doesn’t show. You fellows feel the same, right?” That last question wasn’t aimed at us. It was for the martial artists of the Three Paths Sect under his command. Every last one of them had changed into black, and they nodded without a word. “Apparently so.” Gwak Jun smiled, satisfied, then turned to me. “Well, shall we set out too?” *What the fuck is this bastard talking about right now?* [^1]: A conscript sergeant in the last stretch of mandatory service, coasting toward discharge.

#### Chapter 38 tail (verified mastered)

…
away, somewhere no one can find me.* But Gwak Jun couldn’t set out in search of a second life. Just as he was about to turn, a savage voice cut in. “Stop right there. If you don’t want to die very painfully.” Jin Taekyung added, his voice a little milder, “If you answer well, I’ll kill you gently.” Gwak Jun’s face went white. * * * Crunch! “Ghk.” I knew that feeling. Two or three ribs had to have broken, and the wind would have been knocked clean out of him. He held up pretty well for a Level 40, but that was his limit. “I told you not to run.” “If I were him, I would’ve run too.” Covered in blood and dust, Hyuk Mujin stared at me like I was some kind of beast. “If you’re going to kill him gently, you might as well say you’ll coat your spearhead with Golden Sore Medicine[^1] and stab him.” “Want me to stab you?” “Now that I think about it, that’s true. A blade hurts less if it hits you gently, doesn’t it? You could die gently. Heh heh, heh heh heh.” I smacked him once on the back of the head, then hauled Gwak Jun to his feet. “Let’s try this again. Who are you?” Ptooey. I easily dodged the bloody phlegm. With a high Agility stat, you could even avoid spit flying at you from point-blank range. That was a useful life hack. Of course, I had a fitting life hack for Gwak Jun, too. For example: “If you get hit in the solar plexus while your ribs are broken, it hurts a lot.” Thump. “Gaaaaah!” “So? Your answer?” “T-Three Paths Sect.” As I raised my fist again, Gwak Jun shouted, “The Three Paths Sect! We really are the Three Paths Sect! I’m telling you the truth!” Hyuk Mujin frowned. “He’s lying. The Three Paths Sect was founded thirty years ago. In truth, it’s closer to a martial arts school than a sect. They’re highly respected for taking in wandering orphans and teaching them.” “So?” “Couldn’t these bastards have killed all the Three Paths Sect’s disciples and impersonated them?” “Fake? Puh-huh.” A deflating sound escaped Gwak Jun’s mouth. He was laughing. “You still don’t understand? The Three Paths Sect was established according to that person’s will. As if you could have guessed at a thirty-year grand plan. Heh heh.” “Thirty years?” It was an unimaginably long time. Only a handful of people could have lain low for that many years while plotting to seize Shanxi Province. Only one person came to mind. *The Head Elder?* What possible reason could he have? The Head Elder was the one who had pulled Jin Wikyung to his feet while he blamed himself in front of the children’s bodies. He was also the one who had halted every political maneuver and actively cooperated. Thanks to him, the Jin Family of Taiyuan had united and made it this far… *Wait.* My head spun. *Could it be?* “Hyuk Mujin. How many martial artists from the newly joined small and mid-sized sects are there?” “If you add the Three Paths Sect and Gunggwimun together, well over a hundred.”[^2] “And under the Head Elder?” “If you mean the Head Elder’s faction, probably close to half the main force… Ah!” Hyuk Mujin and the reconnaissance-squad members gaped as they grasped the situation. If my guess was right and the Head Elder was a traitor, everything fit. Helping Jin Wikyung had been nothing more than laying the groundwork for today. *To take everything in a single battle.* He had helped Jin Wikyung and united the family’s strength for this very day. Suddenly I remembered what Gwak Jun had said before the fight. That one line about Shanxi’s master changing. It no longer sounded like nonsense. *The main force is in danger.* I had to tell Jin Wikyung. “We’re moving out. Right now!” I shouted and was about to turn. “Already too late.” Gwak Jun grinned, baring his bloodstained teeth. “Too late for me, too late for you bastards, and too late for the Jin Family of Taiyuan and the Mount Heng Sword Sect. The grand plan has already begun.” At the same time, blood gushed out. From his eyes, nose, and mouth—from every opening. Gwak Jun’s head slowly drooped. Hyuk Mujin spoke with a sickened look on his face. “He severed his own heart meridian.” Gwak Jun’s death meant one thing. Ding. Ding. Ding. > **System** > > — Defeated **Lv.40 Gwak Jun**! > > — **Slay the Assassins** (20/20) > > — Quest **Slay the Assassins** complete! > > — Level up! > > — Fame increases by 50! Quest complete, a level-up, and a Fame increase. After all those notifications, a single message appeared. > **System** > > — All conditions for **Logout** have been met. > > — Logging out in 3 seconds. 3, 2… Strength drained from my whole body. It felt as if I were floating. Hyuk Mujin, startled, caught me. “Squad Leader!” His voice crackled with static. My vision blurred, and my body slipped beyond my control. *Not now. Not like this…* *Of all times.* And then— > **System** > > — 1. Darkness crashed over me. [^1]: Golden Sore Medicine is a salve for blade wounds. [^2]: Gunggwimun is the name of another small sect newly allied with the Jin Family.

## Korean source

```text
＃39화



“아.”

눈을 깜빡였다. 덥고 습하다. 숨을 내뱉자 시야가 뿌옇게 흐려진다. 머리를 더듬자 딱딱한 뭔가가 만져졌다.

‘VR 헬멧.’

그대로 벗겨 내자 먼지 낀 캡슐 내부가 눈앞에 있었다.

쿠션이 꺼진 낡은 캡슐 의자에 앉아 쿵쾅거리는 가슴을 진정시켰다.

‘현실이라고? 정말?’

꼭 30일 만의 로그아웃. 문득 두려움이 솟구쳤다.

여기가 정말 현실일까? 저 버튼을 누르고 캡슐이 열렸을 때, 너무 많은 게 변해 있지는 않을까? 나는 떨리는 마음으로 입을 열었다.

“상태창 오픈.”

적막이 찾아왔다.

익숙한 알림도, 시스템창도 응답하지 않는다.

그제야 비로소 깨달았다. 로그아웃에 성공했다는 사실을.

“후웁.”

크게 숨을 들이마신 뒤 버튼을 눌렀다. 딸깍, 소리와 함께 캡슐 문이 열렸다. 텁텁한 공기가 나를 반긴다.

“……허.”

어둡고 좁은 방 안. 책상 위에 올려 둔 소형 TV와 침대 하나. 그리고 술 냄새를 풀풀 풍기며 잠들어 있는 한 사람.

“크허어. 크허어어.”

저 괴상한 코골이가 이렇게 반가울 줄이야.

‘돌아왔어. 현실로.’

기억 속 그대로다. 지난 30일간의 기억이 꿈인 것처럼.

한동안 멍하니 방 안을 둘러보던 나는 진호 형에게 다가갔다. 그리고 목젖을 손날로 후려쳤다.

빡!

“크허어…… 컥!”

이 인간 코골이만 아니었어도 캡슐로 기어들어 갈 일은 없었다. 나는 발버둥 치는 진호 형을 꽉 붙잡았다.

“한 대만 더 맞자. 아니, 두 대만.”

빡! 빡!

“컥! 커허억!”



* * *



“다 알 만한 사람들이 그래. 그것도 고시원 총무라는 양반이.”

“……죄송합니다.”

“얼굴 붉힐 일 없게 합시다. 응?”

쾅.

문이 닫히자 진호 형이 한숨을 내쉬며 돌아섰다.

“미쳤냐?”

더 험한 말이 나오기 전에 선수를 쳤다.

“미리 말해 두는데, 정당방위였다.”

“뭔 개소리야. 너 돌았어?”

“지극히 정상이지.”

“근데 왜 잘 자는 사람 목을 치고 지랄……!”

쿵쿵쿵.

옆방 아저씨가 벽을 두드렸다. 박자와 강도로 보아 ‘널 죽이고 싶다’는 의미가 담겨 있었다. 진호 형이 목소리를 낮췄다.

“왜 지랄이야? 그것도 이 새벽에.”

“새벽?”

“그래, 이 미친놈아. 이제 겨우 세 시야.”

진호 형이 기가 차다는 표정으로 핸드폰을 내밀었다.

7월 25일. AM 3:02. 날짜와 시간을 확인한 나는 입을 떡 벌렸다.

‘겨우 세 시간밖에 안 지났다고?’

무림에서 한 달. 딱 30일을 지냈는데 현실에서는 고작 세 시간이 흘렀다니.

“……형.”

“말 시키지 마. 목 아파.”

“보통 게임 캡슐 시간 배율이 어느 정도지?”

“홍길동 같은 놈이네, 이거. 대화 주제가 동에 번쩍, 서에 번쩍해. 아주.”

“어느 정도냐고.”

“어?”

굳은 얼굴로 묻자 잠깐 당황하던 진호 형이 대답했다.

“지난달에 나온 최신형 캡슐이 오 대 일? 아마 그럴걸.”

“그 오 대 일이 정확히 뭔데?”

“뭐긴. 게임 체감 시간이 다섯 시간이면 현실에서는 한 시간 흐른 거지.”

미치겠네.

“그 이상은?”

“없어. 지금 기술력으로는 거기까지가 한계…… 근데 이런 건 왜 물어보냐.”

말도 안 되는 일이 일어났으니까.

‘이걸 어떻게 받아들여야 하나.’

다시 봐도 낡아 빠진 캡슐. 만들어진 지 20년도 넘은 저 고물은 현재의 기술력을 아득히 뛰어넘었다.

30일 동안 겨우 세 시간이라니. 시간 배율로 따지면 도대체 어느 정도냐. 정신이 없어서 계산도 안 된다.

“골 때리네.”

“뭐가?”

내 머리로는 도저히 이해할 수 없는 일이다. 진호 형이라면 뭐라도 답이 나오지 않을까. 나는 잠시 망설이다가 입을 뗐다.

“한 달 전에, 아니 세 시간 전에 저 캡슐로 들어갔는데…….”

워낙 많은 일을 겪어서 그런지 할 말도 많다. 모든 이야기를 들은 후에도 진호 형은 한동안 침묵을 지켰다.

그리고 한마디를 던졌다.

“골 때리네.”

“그러니까. 이게 말이 되냐고. 저거 불법 개조 캡슐, 뭐 그런 거 아냐?”

“아니, 캡슐 말고. 너.”

“응?”

진호 형이 심각한 얼굴로 말했다.

“깔끔하게 사과해, 그냥. 미안하다. 코 고는 소리가 너무 시끄러워서 때렸다. 쿨하게, 이 자식아.”

“…….”

“뭐, 로그아웃이 안 돼서 한 달 동안 목숨 걸고 버텨? 소설을 써라, 아주.”

그래, 왠지 잘 풀린다 했다. 나는 한숨을 내쉬었다.

“진짜라니까.”

“자, 태경아. 우리 이성적으로 생각해 보자.”

진호 형이 진지한 말투로 말했다.

“어떤 놈이 잘 자는 사람 목젖 때려서 깨우더니, 한 달 동안 게임 속에 갇혀 있었대. 근데 시계 보니까 세 시간 지났네? 캡슐은 박물관에 들어가도 되는 고물이네?”

“미친 소리로 들리겠지. 알아, 이해해. 근데…….”

“어, 그럼 나 좀 이해해 주라. 숙취 때문에 머리도 아프고 목젖도 아프고 널 보는 내 마음도 아프다.”

“아니, 내 얘기를 좀 들어 보라고!”

쿵쿵쿵쿵.

옆방 아저씨가 벽을 때려 부수기 전에 목소리를 낮췄다.

“그럼 형이 직접 해 봐.”

“뭐?”

“형이 해 보면 믿을 거 아냐.”

직접 겪어 보는 것만큼 빠른 게 없다. 10분쯤 후에 꺼내 주면 내 말을 믿을 수밖에 없을 거다.

진호 형은 나를 뚫어져라 응시하다가 입을 열었다.

“그래, 한번 해 보자, 그럼.”

그러더니 캡슐로 몸을 집어넣고 VR 헬멧까지 썼다. 헬멧 안에서 쉰내가 난다고 투덜거리는 진호 형에게 말했다.

“금방 꺼내 줄게. 홍화루에 처박혀 있어.”

“홍화루 같은 소리 하네. 캡슐 문이나 닫아.”

잠시 후 마주할 진호 형의 표정이 궁금하다. 나는 캡슐 문을 닫고 핸드폰을 꺼내 스톱워치 기능을 켰다.

시작 버튼을 누르자마자 숫자가 빠르게 솟구친다.

‘1초, 2초…… 10초.’

현실에서 10초면 게임 속에서는 분, 시간 단위일 거다.

지금쯤이면 홍화루에서 사태 파악하느라 정신이 없을…….

덜컹.

“어?”

문이 열렸다. 뭐야, 왜 벌써 나와? 아니, 어떻게 나와?

당황한 나를 보며 진호 형이 한숨을 내쉬었다.

“너 지금 뭐 하냐?”

“어, 어?”

“전원도 안 들어오는데 뭔 게임을 해.”

이건 또 무슨 소리야.

“전원이 안 들어온다고?”

“비켜 봐.”

어어, 하는 사이에 문을 열고 나온 진호 형이 캡슐 아래로 허리를 숙였다. 그리고 뭔가를 집어 올렸다.

“넌 이게 뭐로 보이냐?”

코드다. 뽑혀 있는 전기 코드.

헛것을 봤나, 맹렬한 기세로 눈을 비볐지만 달라지는 건 없었다.

“이게 왜…….”

“태경아. 진태경아. 이 가엾고 딱한 자야.”

진호 형이 아련한 얼굴로 말했다.

“날 밝는 대로 정신병원 가라. 난 내 방 간다.”

전기 코드를 툭 던져 놓고 떠나는 진호 형의 뒷모습을, 나는 멍하니 바라봤다. 전기 코드도 안 꽂혀 있었다니.

‘그럼 내가 했던 게임은 뭐야.’

귀신에 홀린 기분이다. 온몸에 소름이 돋았다.



* * *



침대에 누워 생각했다.

‘내가 미친 건가?’

전기 코드도 안 꽂혀 있던 캡슐로 30일간 게임을 했다니.

진호 형의 반응도 이해가 된다. 하지만 그곳에서 일어난 모든 일은…….

‘전부 사실이야.’

진위경, 월화, 혁무진과 대장로. NPC들의 얼굴 하나하나, 그들의 말투와 행동들을 기억한다. 결코 나 혼자만의 망상이 아니었다.

‘그럼 뭐가 문제일까.’

답은 하나다. 27년 전 만들어진 게임 캡슐. 오래전에 현역 은퇴하고 박물관에 있어야 하는 저 고물이 문제다.

게다가 만들어진 시기도 수상쩍다. 2020년 1월 1일.

마왕 아스모데우스가 인류의 손에 쓰러진 날.

‘그때 캡슐 만드는 놈들이 어디 있냐고.’

5년의 대전쟁으로 인해 억 단위의 사람이 죽어 나가고 몬스터가 도심을 활보하던 시대다.

마왕이 쓰러졌다는 뉴스 속보에 ‘자, 이제 게임 캡슐 만듭시다!’ 하고 공장 돌리는 새끼들은 법정에 세워야 한다는 게 내 생각이다.

‘그때는 인쇄가 잘못됐다고 생각했는데.’

순간 몸이 굳었다. 인쇄?

‘제품 사용 설명서!’

그 중요한 걸 잊고 있었다니, 이런 멍청한 놈.

나는 벌떡 일어나 방 안을 뒤엎기 시작했다. 그리고 마침내 침대 밑에서 낯익은 소형 책자를 발견할 수 있었다.



[제품 사용 설명서]

제품명 : 가상현실 접속기

모델명 : Ark - 2020

제조사 : H 소프트

제조일 : 2020년 1월 1일



그리고 다음 페이지.



[주의사항]

- 플레이어 임의로 로그아웃할 수 없습니다.

- 플레이 도중 사망 시, 부활할 수 없습니다.



한 달 전, 아니 세 시간 전에는 여기서 책자를 집어 던졌다.

하지만 이번에는 다르다. 떨리는 손으로 마지막 페이지를 넘겼다.



[주요 기능]

- 한 사람만을 위한 맞춤형 캡슐! 사용자 등록 시 캡슐이 영구 귀속되며, 이는 사망 전까지 유효합니다.

- 쾌적한 플레이를 위한 시간 배율 조정! 로그인 시 현실의 시간이 매우 느리게 흐릅니다. 반대의 경우도 마찬가지입니다.

- 캐릭터와의 동기화 시스템! 사용자는 캐릭터와 동기화됨으로써 더 큰 일체감을 느낍니다.



“뭐야, 이게.”

눈을 글자를 읽었는데, 뇌가 받아들이질 못한다. 나는 처음부터 다시 읽기 시작했다.

‘우선 첫 번째. 영구 귀속.’

말 그대로 죽을 때까지 내 거란 뜻이다. 나는 의문만 해결되면 저 개 같은 캡슐을 박살 내리라 마음먹었다.

‘그다음. 시간 배율.’

가장 궁금했던 부분이다. 하지만 정확한 수치 대신 ‘매우 느리게 흐른다’는 두루뭉술한 표현만 적혀 있을 뿐이었다.

반대의 경우도 마찬가지라고 했으니 현재 게임 속 시간도 매우 느리게나마 흐르고 있을 것이다.

‘그럼 전쟁도 계속되나?’

문득 진위경이 생각났다. 대장로의 배신은 이미 기정사실, 그는 중요한 순간 뒤통수를 치려고 들 것이다. 혁무진과 정찰조가 진위경에게 그 소식을 전했을까?

‘아, 한참 멀었구나. 시간 배율이 거꾸로 바뀌었으니까.’

뭣보다 지금 당장 내 코가 석 자다. 나는 마지막 주요 기능을 살폈다. 하지만 앞에 쓰인 것과는 달리 이건 여러 번 읽어도 이해가 되지 않았다.

‘캐릭터와 동기화한다고?’

혹시나 싶어 국어사전 검색까지 해 봤다. 내가 아는 그 뜻이 맞다. 그래서 더 미친 소리로 들린다.

‘게임 캐릭터랑 뭘 어떻게 동기화를 해.’

이건 도저히 모르겠다. 결국 의문만 하나 더 늘어난 셈이다.

확실한 건 내가 미친 게 아니라는 거다. 나는 침대 위에 풀썩 드러누워 책자의 앞장을 읽었다.

“제작사. H소프트.”

결국 길은 하나로 통한다. 이놈들을 조사하면 뭐라도 나오겠지. 나는 H소프트를 찾아 인터넷을 뒤졌지만 동명의 포르노 제작사가 있다는 사실 말고는 아무것도 알아낼 수 없었다.

“…….”

일단 문부터 잠그고 생각을 해 봐야겠다.
```

## Current accepted English baseline

```markdown
# Chapter 39

“Ah.”

I blinked. It was hot and humid. When I exhaled, my vision went hazy. I felt around my head and found something hard.

*The VR helmet.*

I pulled it off, and the dusty interior of the capsule came into view.

Sitting in the old capsule chair with its collapsed cushions, I calmed my pounding heart.

*Reality? Really?*

Logout after exactly thirty days. Fear surged through me.

Was this really reality? When I pressed that button and the capsule opened, would too much have changed? I opened my mouth, my heart pounding.

“Open Status Window.”

Silence.

Neither the familiar notification nor the System Window answered.

Only then did it sink in. I had successfully logged out.

“Huuup.”

I drew a deep breath and pressed the button. With a click, the capsule door opened. Stale air greeted me.

“…Huh.”

A dark, cramped room. A small TV on the desk. A single bed. And one person asleep, reeking of alcohol.

“Khrrr. Khrrrrooo.”

Who would’ve thought those bizarre snores could sound so welcome?

*I’m back. Back to reality.*

Everything was just as I remembered it. The last thirty days felt like a dream.

After staring blankly around the room for a while, I walked over to Jinho hyung. Then I slammed the edge of my hand into his uvula.

Whack!

“Khrrr… gack!”

If it hadn’t been for this guy’s snoring, I never would have crawled into that capsule. I grabbed Jinho hyung as he thrashed around.

“Take one more. No, two.”

Whack! Whack!

“Gack! Grrrgh!”

* * *

“People who should know better, acting like this. And you’re supposed to be the goshiwon manager, no less.”

“…Sorry.”

“Let’s not make this something to be embarrassed about, all right?”

Bang.

Once the door closed, Jinho hyung turned around with a sigh.

“Are you insane?”

Before he could say anything worse, I beat him to the punch.

“For the record, it was self-defense.”

“What the fuck are you talking about? Have you lost your mind?”

“I’m perfectly normal.”

“Then why the hell did you hit a sleeping person in the neck and—!”

Thump, thump, thump.

The man next door pounded on the wall. Judging by the rhythm and force, the meaning was clear: *I want to kill you.*

Jinho hyung lowered his voice.

“Why the hell are you throwing a fit? In the middle of the night, too.”

“The middle of the night?”

“Yeah, you lunatic. It’s only three in the morning.”

With an incredulous look, Jinho hyung held out his phone.

July 25. 3:02 a.m.

I checked the date and time, and my mouth fell open.

*Only three hours have passed?*

I’d spent a whole month in Murim. Exactly thirty days. And in reality, only three hours had gone by.

“…Hyung.”

“Don’t talk to me. My throat hurts.”

“What’s the usual time ratio for a game capsule?”

“You’re like Hong Gil-dong, you bastard. Your conversation keeps flashing east, then west. All over the place.”

“How much is it?”

“Huh?”

When I asked with a stiff face, Jinho hyung looked briefly flustered, then answered.

“The latest capsule that came out last month? Five to one, I think.”

“What exactly does five to one mean?”

“What do you think? If five hours pass in the game, one hour passes in reality.”

This was driving me crazy.

“What about anything beyond that?”

“There isn’t any. With current technology, that’s the limit… Why are you asking about this?”

Because something impossible had happened.

*How am I supposed to make sense of this?*

Even looking at it again, the capsule was ancient. That piece of junk, made more than twenty years ago, had left current technology in the dust.

Thirty days in only three hours. What kind of time ratio was that? My head was too scrambled to calculate.

“Unbelievable.”

“What is?”

There was no way I could understand it on my own. Maybe Jinho hyung could come up with some kind of answer. After a moment’s hesitation, I spoke.

“A month ago—no, three hours ago—I went into that capsule…”

I’d been through so much that I had plenty to say. Even after hearing the whole story, Jinho hyung stayed silent for a long time.

Then he said one thing.

“Unbelievable.”

“Exactly. Does this make any sense? Isn’t that some illegally modified capsule or something?”

“No. Not the capsule. You.”

“Huh?”

Jinho hyung spoke with a serious face.

“Just apologize cleanly. Sorry. I hit you because your snoring was too loud. Be cool about it, you bastard.”

“…”

“What, you couldn’t log out and spent a month risking your life in a game? Go write a novel.”

*Right. I knew it was going too well.*

I sighed.

“I’m telling you, it’s true.”

“Come on, Taekyung. Let’s think about this rationally.”

Jinho hyung put on a solemn tone.

“Some guy smacks a sleeping person in the uvula to wake him up, then says he was trapped in a game for a month. But he checks the clock, and only three hours have passed? And the capsule is an antique that belongs in a museum?”

“I know it sounds insane. I get it. But…”

“Then try to get me, too. My head hurts from the hangover, my uvula hurts, and looking at you hurts.”

“Just listen to me!”

Thump, thump, thump, thump.

Before the man next door could smash through the wall, I lowered my voice.

“Then try it yourself.”

“What?”

“If you try it, you’ll believe me.”

Nothing was faster than experiencing it firsthand. If I pulled him out after about ten minutes, he’d have no choice but to believe me.

Jinho hyung stared through me, then spoke.

“Fine. Let’s try it, then.”

He climbed into the capsule and even put on the VR helmet. As he grumbled that it smelled sour inside the helmet, I said,

“I’ll pull you out soon. Stay holed up at Honghwaru.”

“Honghwaru, my ass. Just close the capsule door.”

I was curious what face he’d make when I saw him again. I closed the capsule door, took out my phone, and turned on the stopwatch.

The instant I pressed start, the numbers shot up.

*One second, two seconds… ten seconds.*

Ten seconds in reality had to mean minutes, maybe hours, in the game.

*By now he had to be losing his mind at Honghwaru trying to figure out what was going on…*

Clunk.

“Huh?”

The door opened.

*What? Why is he already out? No, how did he get out?*

Looking at me standing there flustered, Jinho hyung sighed.

“What are you doing?”

“Uh, uh?”

“The power isn’t even on. What game were you playing?”

What was that supposed to mean?

“The power isn’t on?”

“Move.”

While I was still stammering, Jinho hyung came out the door, bent down under the capsule, and picked something up.

“What does this look like to you?”

A cord. An unplugged power cord.

I scrubbed at my eyes furiously, but nothing changed.

*Was I seeing things?*

“Why is this…”

“Taekyung. Jin Taekyung. You poor, pathetic soul.”

Jinho hyung spoke with a distant look on his face.

“Go to a mental hospital as soon as it gets light. I’m going back to my room.”

He tossed the power cord aside and walked off. I stared blankly at his back.

The power cord hadn’t even been plugged in.

*Then what was the game I played?*

I felt like I’d been possessed by a ghost. Goose bumps rose all over my body.

* * *

I lay on the bed and thought.

*Am I crazy?*

I’d played a game for thirty days in a capsule that hadn’t even been plugged in.

I could understand Jinho hyung’s reaction. But everything that had happened there…

*It was all real.*

Jin Wikyung, Wolhwa, Hyuk Mujin, and the Head Elder. I remembered every NPC’s face, their way of speaking, their mannerisms. It hadn’t been a delusion I’d cooked up on my own.

*Then what was the problem?*

There was only one answer.

The problem was that game capsule made twenty-seven years ago—a piece of junk that should have retired from service long ago and been sitting in a museum.

The date of manufacture was suspicious, too.

January 1, 2020.

The day the Demon King Asmodeus fell at humanity’s hands.

*Where the hell were people making capsules back then?*

It was an era when hundreds of millions of people had died in the five-year Great War, and monsters had roamed downtown.

In my opinion, the bastards who heard the breaking news that the Demon King had fallen and fired up a factory going, *All right, let’s make game capsules now!* belonged in court.

*Back then, I thought it was a misprint.*

I froze.

*A misprint?*

*The product manual!*

How could I have forgotten something that important? What an idiot.

I shot to my feet and started turning the room upside down. At last, I found a familiar little booklet under the bed.

> **Product User Manual**
>
> **Product name:** Virtual Reality Access Device  
> **Model name:** Ark - 2020  
> **Manufacturer:** H Soft  
> **Date of manufacture:** January 1, 2020

And the next page.

> **Precautions**
>
> - The player cannot log out at will.
>
> - If the player dies during play, resurrection is impossible.

A month ago—no, three hours ago—I had thrown the booklet aside right there.

This time was different.

With trembling hands, I turned to the last page.

> **Key Features**
>
> - A custom capsule for one person only! Once a user is registered, the capsule is permanently bound, and this remains in effect until death.
>
> - Time-ratio adjustment for comfortable play! Upon login, time in reality passes very slowly. The reverse is also true.
>
> - Character Synchronization system! By synchronizing with their character, the user experiences a greater sense of unity.

“What the hell is this?”

I could read the words, but my brain refused to take them in. I started over from the beginning.

*First, permanent binding.*

It meant exactly what it said: it was mine until I died. Once I got some answers, I decided, I was going to smash that goddamn capsule to pieces.

*Next, the time ratio.*

That was the part I’d been most curious about. But instead of an exact figure, all it had was the vague phrase *passes very slowly*.

It said the reverse was true as well, so time in the game had to be passing too, however slowly.

*Then is the war still going on?*

Jin Wikyung came to mind. The Head Elder’s betrayal was already a given, and he would try to stab Wikyung in the back at the critical moment. Had Hyuk Mujin and the reconnaissance squad gotten that news to him?

*Ah. It’s still a long way off. The time ratio flipped.*

More than that, I had my own crisis staring me in the face. I checked the last key feature. Unlike the ones before it, I couldn’t understand this no matter how many times I read it.

*Synchronize with a character?*

Just in case, I even looked it up in a Korean dictionary. It meant exactly what I thought it meant. That only made it sound crazier.

*How do you even synchronize with a game character?*

I couldn’t make any sense of it. In the end, all I’d done was add another question.

One thing was certain: I wasn’t crazy.

I flopped onto the bed and read the front of the booklet again.

“Manufacturer. H Soft.”

In the end, every road led to the same place. If I looked into these bastards, something was bound to turn up.

I searched the internet for H Soft, but aside from a porn studio with the same name, I didn’t find a thing.

“…”

First I needed to lock the door and think.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 39`.

# Master Edit Task — Chapter 38

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
| 이소군    | **Lee Seogeun**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 로그아웃             | **Logout**                     |
| 민첩               | **Agility**                    |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 청해     | **Qinghai**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 귀문      | **your sect**                                                   |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 곽준 | **Gwak Jun** |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |

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

#### Chapter 36 tail (verified mastered)

…
order to make camp finally came once we entered a wide basin. “Ugh, every bone in my body hurts.” Hyuk Mujin groaned. Since he clearly wasn’t fully recovered, the march seemed to be too much for him. “It’s not too late. Want to turn back even now?” “Are you saying that again?” “I’m saying it because you look like you’re struggling.” “You’re mistaken. Does Hyuk Mujin, a man among men, look like someone who’d get tired after walking for a mere half day?” I nodded without the slightest hesitation. “Yep.” “Absolutely not!” “Hmm. You’re really not tired? You’re fine?” “Yes.” “Then go help the others set up camp.” At that moment, Hyuk Mujin, man among men, snapped his eyes wide and sank to the ground. “Ugh, the internal injuries Jopil gave me…” “…” *You said your internal injuries had healed, you bastard.* I was wondering whether I ought to hit him when a voice cut in. “Is he injured?” A massive shadow stretched under the moonlight. Hyuk Mujin cautiously lifted his head to see who it was, then his eyes flew open. “Gasp! Lesser Family Head!” If Jin Wikyung was a division commander, Hyuk Mujin was a private. The next moment, Hyuk Mujin sprang to his feet like lightning and stood at attention. Jin Wikyung burst out laughing. “You still don’t look fully recovered. Lie back down. Ah, the internal injuries do seem fully healed. I’ll vouch for that.” “Ah, I, that isn’t…” Jin Wikyung lightly patted the flustered Hyuk Mujin on the shoulder, then turned to me. “Shall we walk for a bit?” I followed him to a secluded corner. He spoke first. “How’s your condition?” “Good.” I’d reaped the full benefits of leveling up. My body had recovered at a terrifying speed, and allocating my points had made it even stronger. The problem was something else. *My Fame isn’t going up.* No, it was going up. Really, by about a rat dropping’s worth. Little by little. Very, very little. At this rate, there was no guarantee I’d be able to log out before the fighting began. *At least, not if things kept going like this.* Jin Wikyung’s arrival was perfect timing. I brought up the idea I’d been mulling over. “I want to take on a mission.” His eyes went round at how bluntly I’d come out with it. “Hm? A mission?” “Now that I’ve recovered, I want to distinguish myself for our family.” I was proud of myself. To think I could deliver a line like that—a lie like that—with a straight face. “I-is that truly what you think?” “Yes.” The corners of Jin Wikyung’s eyes trembled. He looked like a wave of emotion was running through his whole body. *This is actually making me feel kind of guilty.* The reason I was putting on this unconvincing act was Fame. If I went out on even a reconnaissance mission and distinguished myself, Fame would come in. It would be even better if I ran into a reconnaissance unit from the Mount Heng Sword Sect. Not only would that be excellent EXP, I’d be able to fill all the Fame I had left. *Once the real battle starts, it’s over.* I had to log out, and fast, before then. I spoke in a voice full of resolve. “Just leave it to me.” “How did you come to have such an admirable thought? Thank you, my youngest brother.” Jin Wikyung wiped the damp corners of his eyes with his sleeve and went on. “But no.” “Then please give me a reconnaissance mission—what?” “I appreciate the thought. Keep guarding the rear as you are now.” *What is he talking about?* I barely suppressed the urge to grab him by the collar and shake him. “I-I really want to distinguish myself.” “You’ve already done more than enough.” “No, that’s not what I mean.” “The merits you’ve earned so far have already been a great help to our family. So don’t trouble yourself over it.” “I’d like you to give me even one reconnaissance mission. There could be enemies lying in ambush ahead…” Jin Wikyung laughed softly. “This is a battle with our family’s fate at stake. Do you think I wouldn’t have accounted for something like that?” “Couldn’t there be a one-in-ten-thousand chance we missed something?” “That is, quite literally, one in ten thousand.” *Damn it.* Nothing was going my way. What if I really failed to fill my Fame at this rate? Then I’d have to fight a large-scale battle with fifteen hundred people committed. *I’m fucked.* Something large and warm settled on my dejected shoulder. Jin Wikyung’s hand. “Youngest.” His voice was heavy and lonely. At the sudden change in mood, I fell silent and listened. “Your mission is graver than anyone else’s among us.” “What’s my mission?” After letting it hang for a long time, he forced out a single word. “Survive.” “Huh?” “Survive however you can. If our family loses, run without looking back.” “…” “If the roots live, the tree will grow again. Second Brother and you could become better roots than I.” I was speechless. For a long while, I could only stare at his face. Survive. Become roots. His voice and eyes hit home with more seriousness than ever before. “That is your mission.” The palm resting on my shoulder slid slowly down. I stared after Jin Wikyung’s departing back, unable to look away.

#### Chapter 37 tail (verified mastered)

…
nose. > **System** > > Achieve Fame 500 (497/500) I never thought the number 1 could feel this precious. In a voice that had aged all of a sudden, I muttered, “I’m going, I’m going, going home now…” “Now you’re even talking to yourself. Have you lost your mind?” Hyuk Mujin clicked his tongue, then his eyes went round. “What’s that? I’ve never seen those before.” “This?” I pointed in turn at the old book and the small case sitting on the rock. “One’s a martial arts manual. The other’s an elixir.” “Whoa. Really?” I explained in a drained voice to the guy whose eyes were halfway out of his head. “The manual’s a Supreme Peak martial art, and if you absorb the elixir properly, it’ll give you thirty years of internal energy.” “What?” “But they say if you take the elixir wrong, you’ll burn to death. You want it?” “Uh, right…” Judging by that unimpressed face and the snout sticking out a good five feet, he didn’t believe a damn word I was saying. *Well, if someone suddenly came at me with a Supreme Peak martial art and a thirty-year Fireball elixir, I’d figure it was a joke too.* “You really won’t eat it? It’s good stuff.” “Oh, I’m fine. Learn plenty of that Supreme Peak martial art, and be sure to chew your elixir thoroughly.” “I don’t need this kind of thing anymore.” “Of course. You’re the Sleeping Dragon.” Normally I would have smacked him in the back of the head. Right now I didn’t feel much of anything. *Is this how a short-timer sergeant feels?[^1]* At the same time, I felt strange. Was it the aftereffect of everything I’d been through? It had only been a little over a month, but it felt hazy and distant, as if I’d been here a year. I started tracing back through old memories. *I first opened my eyes at Honghwaru.* That was where I met Wolhwa for the first time and realized I was trapped in this game. Even now, thinking about that moment gave me goose bumps. *I really thought I was going to lose my mind.* It had taken me three days just to decide to go to the Jin Family of Taiyuan. And the guy I met there was this one—Hyuk Mujin. Smack! “Argh! Why did you hit me?” “Hmm. Just thought of the old days.” “What old days?” “Nope. Not telling. Get back already.” “What are you, some back-alley thug? Just because your martial arts are a bit strong, you think you can oppress people like this?” As Hyuk Mujin threw a fit, everyone’s eyes turned toward us. Even the reconnaissance-squad members who had been watching like it was none of their business jumped in. “What are you two talking about?” “Dunno. The deputy squad leader must have done something wrong.” “Hey, I didn’t do anything!” “This is Murim. Being weak is a crime.” “But should we even be doing this?” At someone’s words, silence fell for a moment. “True. Waiting here is our mission, but…” The tension and fear they had been suppressing with forced smiles hung in the air. Even I, who would soon be returning to the real world, felt uneasy with Jin Wikyung’s face flickering through my mind. How much worse must it be for these guys? There was only one thing I could say. “I trust my big brother.” *Big brother.* This time, I put my heart into the word. Jin Wikyung had been the greatest source of strength I’d had in this place. Maybe I simply wanted to shake off that unease, even if only like this. The faces that had stiffened for a moment relaxed. “We feel the same.” Hyuk Mujin slipped in as well. “I trust the squad leader more.” “Wow. Deputy squad leader, that side-switching of yours is really something.” “You little bastards. Is there anyone here who doesn’t owe the squad leader their life?” “Well, when you put it that way, what can we say?” “I trust the squad leader too. Honestly, I knew all along, even when you were playing the thug. I thought, *Ah, that man is the Sleeping Dragon.* I could tell right away.” I felt strange. *They say even dried squid gives water if you squeeze it. Who knew I’d feel something like this toward NPCs in a game?* *Well, honestly… it doesn’t feel bad.* Suddenly I wondered about Jin Wikyung, somewhere beyond those mountains. Had the battle started? If so, which side was winning? And I wasn’t the only one thinking that. “By now, the battle must have started.” It was Gwak Jun of the Three Paths Sect. Unlike before, he was wearing black martial robes. *Was that what this guy originally wore?* At my look, Gwak Jun shrugged. “I like this sort of thing. Easy to move in, and even if a little blood splatters, it doesn’t show. You fellows feel the same, right?” That last question wasn’t aimed at us. It was for the martial artists of the Three Paths Sect under his command. Every last one of them had changed into black, and they nodded without a word. “Apparently so.” Gwak Jun smiled, satisfied, then turned to me. “Well, shall we set out too?” *What the fuck is this bastard talking about right now?* [^1]: A conscript sergeant in the last stretch of mandatory service, coasting toward discharge.

## Korean source

```text
＃38화



처음에 드는 감정은 의아함이었다.

“출발?”

곽준이 대답했다.

“예. 이쪽에서도 슬슬 움직여 줘야 시간에 맞출 수 있거든요.”

종잡을 수 없는 그의 말에 혁무진이 나섰다.

“거기, 삼도문 양반. 뭘 잘못 알고 있나 본데, 우리 임무는 여기 계신 공자님과 함께 후미에서 대기하는 거요.”

“아, 정말입니까?”

곽준이 눈을 동그랗게 떴다. 그 반응에 정찰조원들이 그럼 그렇지, 하는 얼굴로 고개를 끄덕였다.

“잘못 알고 있었나 보군.”

“그럴 수 있지. 암. 그럴 수 있어.”

하지만 내 생각은 달랐다.

‘그럴 수 있긴 뭘 그럴 수 있어.’

현재 후미에 남아 있는 삼도문의 무사는 스물. 그중 우두머리 격인 인물이 바로 곽준이다.

‘그런 놈이 명령을 헷갈려?’

분명 기분 나쁜 놈이지만 그 정도로 멍청해 보이진 않는다.

불길함이 스멀스멀 올라와 온몸을 휘감는다.

“곤란하군요. 제가 받은 임무는 좀 달라서요.”

“어떻게 다르지?”

말과 동시에 혁무진의 발을 지그시 밟았다. 하루에도 수십 번씩 까불거리는 녀석이지만 바보는 아니다. 내 신호를 알아들은 혁무진의 눈이 커졌다.

“조장. 발 좀 치워 주세요. 아파요.”

“…….”

이런 시벌.

어이없어하는 나를 보며 곽준이 입꼬리를 말아 올렸다.

“눈치가 빠르시군. 아니면 수하들이 멍청한 건가? 뭐, 아무튼. 그분께서 하신 말씀을 그대로 들려주지.”

다음 순간, 곽준의 얼굴에서 웃음기가 사라졌다. 냉정하고 무감각한 눈빛의 살인자가 말을 이었다.

“모두 제거하고 본대에 합류하라.”

차차창!

말이 떨어짐과 동시에 수십 개의 검광이 치솟았다. 곽준이 이끄는 삼도문의 무사 스무 명. 그리고 반 박자 늦게 검을 뽑아 든 정찰조원들 사이로 살기와 긴장감이 감돌았다.

“이 자식들이 미쳤나…….”

빠드득, 혁무진이 이를 갈며 놈들을 노려봤다.

“네놈들이 감히 본가를 배신해? 죽고 싶어 환장한 것이냐!”

“배신? 죽어? 단단히 착각하고 있군.”

곽준의 입가에 비웃음이 떠올랐다.

“배신한 적도, 죽을 일도 없다. 네놈들 따위한테는 더더욱.”

“이 새끼가!”

눈이 뒤집힌 혁무진이 곽준을 향해 몸을 날렸다. 아니, 날리려고 했다.

“가만히 있어.”

“조장?”

혁무진이 눈을 부릅떴다.

“삼도문입니다. 이류 문파 쭉정이들이라고요! 당장 저놈들을 아작 내고…….”

“아니야.”

“예?”

“쭉정이가 아니라고.”

예리한 기세와 살기등등한 눈빛. 지금까지 봐 왔던 일개 중소 문파의 무사들이 아니다. 시스템은 그 의심을 확신으로 바꿔 주었다.



[Lv.30]



기감을 통해 읽어 낸 놈들의 평균 레벨이다.

하나하나가 일류의 무인들. 젠장, 이런 놈들과 사흘을 함께 있었는데 까맣게 몰랐다.

‘로그아웃에만 너무 정신이 팔려 있었어.’

방심한 결과다. 나는 입술을 깨물며 놈들을 바라봤다. 정확히 말하면 놈들의 등 뒤로 우거진 풀숲을.

아주 미세한 움직임이었지만 내 눈을 피해 갈 수는 없다.

‘숨어 있군.’

[기감]의 범위 밖이라 확인할 수 없지만, 직감상 확실하다. 첩자에 매복까지. 철저한 놈들이다.

“너희, 정체가 뭐냐?”

“무슨 말이지?”

“진짜 삼도문은 어디 있어?”

삼도문은 일개 중소 문파. 앞서 혁무진의 말처럼 이류 문파 쭉정이다. 이런 놈들이 하루아침에 뚝딱 생겨났을 리 없다.

설마?

“항산검문에서 왔나?”

곽준이 피식 웃었다.

“항산검문? 뭐, 그렇게 생각할 수도 있겠군.”

빌어먹을, 제삼의 세력이다.

로그아웃이 코앞인데 이런 일이 생기다니…….

‘시바, 운도 더럽게 없지.’

똥줄이 활활 탄다. 내가 위축될수록 곽준은 기세등등해졌다.

“이제 와서 후회해 봤자 늦었다. 대계(大計)는 오래전부터 시작되었으니까.”

“크윽.”

곽준은 희열에 찬 목소리로 선언했다.

“오늘…… 산서 무림은 새로운 주인을 맞이한다.”

띠링.



- 퀘스트가 생성되었습니다.



퀘스트



[암살자 처단]

오랫동안 때를 기다려 온 누군가가 움직였습니다. 우선 배신자가 보낸 암살자들을 처치하십시오!



등급 : 절정

제한 : 진태경

임무 : 암살자 처단 (0/20)

보상 : 경험치와 명성

 연계 퀘스트

실패 : 사망





눈을 깜빡였다. 내가 퀘스트창을 잘못 봤나?

‘스무 명?’

왜 이십이야? 저기 매복한 놈들도 있는데?

의문이 떠오른 그때, 풀숲이 들썩이고 매복한 적들이 함성과 함께 우리를 향해 돌격했다.

- 꾸에에에엑!

함성치곤 독특한데. 아니, 저건 울음소리 아닌가.

멍하니 서 있는 내 귓가로 [기감]이 발동됐다는 알림이 울렸다.



[Lv.1 고라니]



뭐여, 시벌.

“고라니여?”

고라니 무리가 우리를 스쳐 저 언덕 너머로 사라졌다. 갑작스러운 등장. 빠른 퇴장.

곽준이 묘하게 힘 빠진 얼굴로 검을 뽑아 들었다.

“쳐라!”

스무 명의 적들이 천천히 접근해 왔다. 나는 고라니의 충격이 가시지 않은 얼굴로 혁무진을 불렀다.

“야.”

“왜요.”

“쟤들 다 일류거든?”

“헉, 진짜요?”

혁무진이 화들짝 놀랐다.

“어. 너 이소군 알지. 항산검문 둘째. 걔가 한 스무 명 있다고 생각하면 돼.”

“이소군이, 스무 명이요?”

이번 반응은 묘하다. 잠깐 곰곰이 생각에 잠겨 있던 혁무진이 한마디를 툭, 던졌다.

“쟤들, 다 죽겠는데요?”



* * *



곽준은 생각했다.

‘이게 아닌데.’

그의 시선은 한 사람에게 고정되어 있다. 진태경. 초일류라고 알려진 태원진가의 삼공자. 놈의 창이 움직일 때마다 피가 솟구치고 수하들이 쓰러진다.

일격을 버텨도 이 격, 삼 격에 반드시 숨통이 끊어졌다. 그 한 명, 한 명이 최소 십 년을 수련시킨 일류 무인들이다.

‘뭐 저런 놈이 다 있지?’

창을 쓰니 창수(槍手)인 건 분명해 보이는데, 간격이 좁혀지건 말건 신경도 안 쓴다. 창을 휘두를 거리조차 없다 싶으면 어디선가 비수며 도끼가 툭툭 튀어나와 닥치는 대로 찌르고 쑤신다. 곡예단(曲藝團)의 묘기보다 더하다.

‘저 많은 무기가 도대체 어디서 튀어나오는 거지?’

보지도 못했다. 무슨 수법인지도 모르겠다. 무공과 공력의 문제가 아니다. 진태경이라는 인간 자체가 강해 보였다.

‘정보가 잘못됐다.’

스물로는 턱도 없다. 두 배는 데려와야 했다. 그가 받은 정보에 의하면 진태경은 운 좋은 애송이 그 이상도, 이하도 아니었다.

‘게다가, 저놈들은 도대체 뭐야.’

진태경의 부하라는 아홉 명은 대장이 앞에서 뭘 하건 말건 서로 등을 맞대고 느릿느릿 전진했다. 분명 개개인으로 보면 한참 부족한 실력인데, 한데 뭉치니 철벽이 따로 없다.

퍽. 콰직!

“크아악!”

“찔러, 찔러!”

“들어와, 들어와!”

곽준의 입술이 파르르 떨렸다. 무인으로서의 명예도 없는 놈들이다. 이런 난전에 서너 명씩 달라붙어 칼질을 해 대니 일류 고수인 수하들도 꼬치구이 신세를 면치 못했다.

“이놈들……!”

진태경에 대한 두려움을, 분노가 밀어냈다. 분기탱천한 그가 전장을 향해 몸을 날리려던 그때였다.

콰아아아-

전장의 중심에서 광풍이 휘몰아쳤다.

진태경의 창은 바람을 찢고 검을 조각 냈다. 수백 개의 검편(劍片)이 바람을 타고 전방을 휩쓸었다. 검의 주인들, 그리고 미처 반응하지 못한 자들을 향해.

푸푸푸푸푹!

“……끄윽.”

털썩.

전신에 검편이 박힌 무사가 그대로 고꾸라졌다. 일섬에 휘말린 십여 명의 부하 중 목소리라도 남긴 이는 그가 유일했다.

“……!”

꿀꺽. 누군가의 목울대가 크게 일렁였다. 이 순간만큼은 적아를 떠나 모두가 침묵을 지켰다. 어느 누구도 감히 검을 들어 싸울 생각을 하지 못했다. 물론 한 사람은 예외였다.

“일섬, 이거 끝내주네.”

진태경의 중얼거림을 듣는 순간, 곽준은 모든 걸 포기했다.

‘다 끝났어.’

대계가 성공해도 그는 실패했다. 진태경에게 죽느냐, 그분께 죽느냐 하는 무의미한 선택만이 남아 있을 뿐.

‘도망쳐야 한다. 아무도 찾을 수 없는 곳으로 멀리.’

하지만 곽준은 두 번째 인생을 찾아 떠날 수 없었다. 막 돌아서려는 찰나 들려온 살벌한 목소리 때문이었다.

“거기 딱 서. 매우 아프게 죽기 싫으면.”

진태경은 조금 누그러진 목소리로 덧붙였다.

“대답만 잘하면 살살 죽여 줄게.”

곽준의 얼굴이 하얗게 질렸다.



* * *



우직-!

“헙.”

느낌이 왔다.

갈비뼈가 두세 대쯤 부러지고 숨이 턱 막혔을 거다.

그래도 40레벨이라고 제법 버텼지만, 딱 거기까지가 한계다.

“도망치지 말라니까.”

“저 같아도 튀었습니다.”

피와 먼지를 뒤집어쓴 혁무진이 나를 짐승 보듯 바라본다.

“살살 죽인다니, 차라리 창날에 금창약을 바르고 찌른다고 하십쇼.”

“찔러 줘?”

“생각해 보니까 맞는 말이네요. 칼도 살살 맞으면 덜 아프잖습니까. 살살 죽을 수도 있죠. 허허, 허허허.”

뒤통수를 한 대 갈겨 주고 곽준을 일으켜 세웠다.

“다시 물어보자. 너희, 누구야?”

퉤. 피가래를 가볍게 피했다. 민첩 스탯이 높으면 코앞에서 날아오는 침도 피할 수 있다. 이건 좋은 리빙 포인트다.

물론 곽준에게 적당한 리빙 포인트도 있지. 예를 들자면.

“갈비뼈가 나간 상태에서 명치를 맞으면 많이 아프다.”

뻑.

“크아아아악!”

“그래서 대답은?”

“사, 삼도문.”

다시 주먹을 치켜드는 내게 곽준이 외쳤다.

“삼도문, 삼도문이 맞소. 사실이란 말이오!”

혁무진이 눈살을 찌푸렸다.

“거짓말입니다. 삼도문은 삼십 년 전에 개파한 문파인데, 사실 문파보단 무관에 가깝습니다. 주로 떠돌이 고아들을 받아들여 가르쳐서 명망이 높죠.”

“그래서?”

“이놈들이 삼도문의 제자들을 모두 죽이고 가짜 행세를 한 게 아닐까요?”

“가짜? 푸흐흐.”

곽준의 입에서 바람 빠지는 소리가 흘러나왔다. 놈은 웃고 있었다.

“아직도 모르겠느냐? 삼도문은 그분의 뜻에 따라 세워진 것이다. 삼십 년 대계를 짐작이나 했겠냐마는. 크흐흐.”

“삼십 년?”

까마득한 시간이다. 그 긴 세월 동안 웅크린 채 산서성을 차지할 계획을 꾸밀 수 있는 사람은 몇 되지 않는다.

당장 생각나는 건 한 사람뿐.

‘대장로?’

그가 도대체, 무슨 이유로?

아이들의 시신 앞에서 자책하던 진위경을 일으킨 것도, 모든 정치적 행위를 중단한 채 적극적으로 협력한 것도 대장로다.

덕분에 태원진가는 하나로 뭉쳐 오늘날에 이를 수 있었…….

‘잠깐.’

머릿속이 어지럽다. 설마?

“혁무진. 새로 합류한 중소 문파의 무사들이 몇이나 되지?”

“삼도문, 궁귀문을 합치면 백 명이 훌쩍 넘을 겁니다.”

“대장로 휘하는?”

“대장로님 계파라면 아마 본대의 절반 가까이…… 아!”

사태를 파악한 혁무진과 정찰조원들이 입을 벌렸다. 만약 내 짐작대로 대장로가 배신자라면 아귀가 맞아떨어진다.

진위경을 도운 건 오늘을 위한 포석에 지나지 않는다.

‘한 번의 전투로, 모든 걸 얻기 위해서.’

바로 오늘을 위해 진위경을 돕고, 가문의 힘을 합친 거다.

문득 전투 전, 곽준이 했던 말이 생각났다.

산서성의 주인이 바뀐다던 그 한마디. 결코 헛소리로 들리지 않는다.

‘본대가 위험해.’

이 사실을 진위경에게 알려야 한다.

“출발한다. 당장!”

버럭 외치며 돌아서려던 순간이었다.

“이미 늦었어.”

곽준이 피에 젖은 이를 드러내며 웃었다.

“나도, 네놈들도. 그리고 태원진가와 항산검문도. 대계는 이미 시작됐거든.”

동시에 핏물이 쏟아졌다. 눈, 코, 입. 구멍이란 구멍에서 피를 쏟아 낸 곽준의 고개가 스르륵 내려갔다.

혁무진이 질린 얼굴로 말했다.

“스스로 심맥을 끊었습니다.”

곽준의 죽음. 그건 한 가지 사실을 의미했다.

띠링. 띠링. 띠링.



- [Lv.40 곽준]을 처치했습니다!

- 암살자 처단 (20 / 20)

- 퀘스트, [암살자 처단]을 완료했습니다!

- 레벨 업!

- 명성이 50 상승합니다!



퀘스트 완료, 레벨 업과 명성 상승. 그 수많은 알림 끝에 나타난 하나의 메시지.



- [로그아웃]에 대한 모든 조건을 충족했습니다.

- 3초 후 로그아웃합니다. 3, 2…….



전신에서 힘이 쭉 빠져나간다. 몸이 붕 뜨는 감각.

혁무진이 화들짝 놀란 얼굴로 나를 부축했다.

“조장!”

노이즈 낀 목소리, 흐려지는 시야와 통제를 벗어난 몸.

지금은 안 되는데, 이런 식으로는 아닌데…….

‘하필 이럴 때.’

그리고 다음 순간.



- 1.



암흑이 들이닥쳤다.
```

## Current accepted English baseline

```markdown
# Chapter 38

The first thing I felt was puzzlement.

“Set out?”

Gwak Jun answered.

“Yes. Our side needs to get moving too, or we won’t make it in time.”

At those inscrutable words, Hyuk Mujin stepped forward.

“You there, Three Paths Sect man. You seem to have the wrong idea. Our mission is to wait here in the rear with the Young Master.”

“Oh, is that so?”

Gwak Jun’s eyes went round. At that reaction, the reconnaissance-squad members nodded with looks that said, *That figures.*

“Looks like I had it wrong.”

“It happens. Sure it does.”

But I thought differently.

*What do you mean, it happens?*

There were twenty Three Paths Sect martial artists left in the rear. The one who amounted to their leader was Gwak Jun.

*Would a guy like that mix up his orders?*

He was unpleasant, no question, but he didn’t look that stupid.

A creeping dread rose and wound around my whole body.

“That’s a problem. The mission I received is a little different.”

“How is it different?”

As I spoke, I pressed down firmly on Hyuk Mujin’s foot. He horsed around dozens of times a day, but he wasn’t an idiot. His eyes widened as he caught my signal.

“Squad Leader, please move your foot. It hurts.”

“…”

*For fuck’s sake.*

Gwak Jun’s mouth curled as he watched me stare in disbelief.

“You catch on fast. Or are your subordinates just idiots? Well, anyway. I’ll tell you exactly what that person said.”

The next moment, the smile vanished from Gwak Jun’s face. A killer with cold, vacant eyes went on.

“Eliminate everyone and join the main force.”

Clang-clang-clang!

The instant the words left his mouth, dozens of sword flashes shot into the air. Killing intent and tension hung between the twenty martial artists Gwak Jun led and the reconnaissance-squad members, who drew their swords half a beat later.

“Have you bastards lost your minds…?”

Hyuk Mujin ground his teeth and glared at them.

“You dare betray our family? Are you itching to die?”

“Betray? Die? You’re badly mistaken.”

A sneer tugged at Gwak Jun’s mouth.

“There has been no betrayal, and we aren’t going to die. Least of all to trash like you.”

“You son of a—!”

Hyuk Mujin’s eyes went wild as he threw himself at Gwak Jun.

Or tried to.

“Don’t move.”

“Squad Leader?”

Hyuk Mujin’s eyes flew wide.

“They’re the Three Paths Sect! They’re nothing but Second Rate sect husks! Let us smash them right now and—”

“No.”

“What?”

“They’re not husks.”

Their sharp aura and murderous eyes were nothing like the ordinary martial artists of a small or mid-sized sect I had seen until now. The System turned that suspicion into certainty.

> **System**
>
> **Lv.30**

That was the average Level I read through my **Qi Sense**.

Every last one of them was a First Rate martial artist. Damn it. I’d spent three days with these people and hadn’t noticed a thing.

*I’d been too fixated on Logout.*

That was what I got for letting my guard down. I bit my lip and looked at them—or, more precisely, at the thick grass behind them.

The movement had been extremely faint, but it couldn’t get past my eyes.

*Someone’s hiding.*

They were outside the range of my **Qi Sense**, so I couldn’t confirm it. My instincts were certain, though. Spies, and an ambush on top of it. Thorough bastards.

“You lot. What are you really?”

“What is that supposed to mean?”

“Where is the real Three Paths Sect?”

The Three Paths Sect was only a small or mid-sized sect. As Hyuk Mujin had said, they were Second Rate husks. People like these couldn’t have been whipped up overnight.

*Don’t tell me.*

“Did you come from the Mount Heng Sword Sect?”

Gwak Jun gave a short laugh.

“The Mount Heng Sword Sect? Well, you could think that.”

*Damn it. A third faction.*

Logout was right in front of me, and this had to happen now…

*Shit. My luck is rotten.*

I was scared shitless. The more I shrank back, the more triumphant Gwak Jun looked.

“It’s too late for regret now. The grand plan began long ago.”

“Kh.”

Gwak Jun declared it in a voice brimming with delight.

“Today… Shanxi Murim will welcome a new master.”

Ding.

> **System**
>
> — A Quest has been created.
>
> **Quest**
>
> **Slay the Assassins**
>
> Someone who has waited a long time for the right moment has made their move. First, defeat the assassins sent by the traitor!
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Slay the Assassins (0/20)
>
> **Reward:** EXP and Fame
>
> **Chain Quest**
>
> **Failure:** Death

I blinked. Had I misread the Quest Window?

*Twenty?*

Why twenty? There were enemies lying in ambush back there too.

Just as the question formed, the grass shook. The ambushers charged us with a battle cry.

“Kweeeek!”

Strange, for a battle cry. No, wait. Wasn’t that an animal?

As I stood there blankly, an alert rang in my ears that **Qi Sense** had activated.

> **System**
>
> **Lv.1 Water Deer**

What the hell?

“A water deer?”

A herd of water deer brushed past us and vanished beyond the hill. A sudden appearance. A quick exit.

Gwak Jun drew his sword with an oddly deflated look on his face.

“Attack!”

The twenty enemies came on slowly. Still wearing the shock of the water deer, I called to Hyuk Mujin.

“Hey.”

“What.”

“They’re all First Rate, you know?”

“What? Really?”

Hyuk Mujin jumped.

“Yeah. You know Lee Seogeun, the second son of the Mount Heng Sword Sect? Imagine there are twenty of him.”

“Twenty Lee Seogeuns?”

This reaction was odd. Hyuk Mujin thought it over for a moment, then tossed out a single remark.

“They’re all going to die, aren’t they?”

* * *

Gwak Jun thought,

*This isn’t how it was supposed to go.*

His gaze was locked on one man. Jin Taekyung, the third Young Master of the Jin Family of Taiyuan, known as a Super First Rate.

Every time that spear moved, blood spurted and Gwak’s men went down.

Even if they weathered one blow, the second or third always finished them. Every one of them was a First Rate martial artist trained for at least ten years.

*How is there a man like that?*

He was clearly a spearman, but he didn’t care whether the gap closed or not. Whenever it looked like there wasn’t even room to swing the spear, daggers and axes popped out from somewhere and stabbed and jabbed at anything in reach.

It put an acrobat troupe’s stunts to shame.

*Where the hell are all those weapons coming from?*

He hadn’t even seen them appear. He had no idea what kind of technique it was. This wasn’t a matter of martial arts or internal energy. Jin Taekyung himself just looked strong.

*The information was wrong.*

Twenty men weren’t nearly enough. They should have brought twice that. According to what he had been told, Jin Taekyung was nothing more or less than a lucky greenhorn.

*And what the hell are those people?*

The eight said to be Jin Taekyung’s subordinates advanced slowly with their backs together, whether their leader was doing anything up ahead or not. Individually, their skill was far from enough, but once they bunched up, they were an iron wall.

Thud. Crack!

“Gaaah!”

“Stab them! Stab them!”

“Come in! Come in!”

Gwak Jun’s lips trembled.

They had no honor as martial artists. In the middle of this melee they piled on three or four at a time and hacked away, and even his First Rate subordinates couldn’t avoid ending up as meat on a skewer.

“You bastards…!”

Anger shoved aside the fear of Jin Taekyung. Just as Gwak Jun, livid, was about to hurl himself into the fight—

Whoooosh—

A violent gale whipped up at the center of the battle.

Jin Taekyung’s spear tore through the wind and shattered the swords. Hundreds of sword fragments rode the gale and swept forward, toward the owners of those swords and the men who hadn’t reacted in time.

Pupupupupup!

“…Urk.”

Thud.

A martial artist with sword fragments buried all over his body crumpled forward. Of the ten or so subordinates caught in One Flash, he was the only one who even left a sound.

“…!”

Someone swallowed hard. Their throat bobbed.

For that moment, friend and foe alike kept silent. No one even dared think of raising a sword to fight.

Of course, one person was the exception.

“One Flash. This thing is awesome.”

The instant Gwak Jun heard that mutter, he gave up on everything.

*It’s all over.*

Even if the grand plan succeeded, he had failed. All that remained was the meaningless choice of dying to Jin Taekyung or dying to that person.

*I have to run. Far away, somewhere no one can find me.*

But Gwak Jun couldn’t leave to find a second life. Just as he was turning, a savage voice cut in.

“Stop right there. If you don’t want to die very painfully.”

Jin Taekyung added, his voice a little milder,

“If you answer well, I’ll kill you gently.”

Gwak Jun’s face went white.

* * *

Crunch!

“Ghk.”

I knew that feeling.

Two or three ribs had to have broken, and the wind would have been knocked clean out of him.

He held up pretty well for a Level 40, but that was as far as he could go.

“I told you not to run.”

“If I were him, I would’ve run too.”

Hyuk Mujin, covered in blood and dust, stared at me like I was some kind of beast.

“If you’re going to kill him gently, you might as well say you’ll coat your spearhead with Golden Sore Medicine[^1] and stab him.”

“Want me to stab you?”

“Now that I think about it, that’s true. A blade hurts less if it hits you gently, doesn’t it? You could die gently. Heh heh, heh heh heh.”

I smacked him once on the back of the head, then hauled Gwak Jun to his feet.

“Let’s try this again. Who are you?”

Ptooey.

I easily dodged the bloody phlegm. With a high Agility stat, you could even avoid spit flying at you from point-blank range.

That was a useful life hack.

Of course, I had a fitting life hack for Gwak Jun, too. For example:

“If you get hit in the solar plexus while your ribs are broken, it hurts a lot.”

Thump.

“Gaaaaah!”

“So? Your answer?”

“T-Three Paths Sect.”

As I raised my fist again, Gwak Jun shouted,

“The Three Paths Sect! It really is the Three Paths Sect! I’m telling you the truth!”

Hyuk Mujin frowned.

“He’s lying. The Three Paths Sect was founded thirty years ago. In truth, it’s closer to a martial arts school than a sect. They’re highly respected for taking in wandering orphans and teaching them.”

“So?”

“Couldn’t these bastards have killed all the Three Paths Sect’s disciples and impersonated them?”

“Impersonated? Pfft.”

A deflating sound escaped Gwak Jun’s mouth. He was laughing.

“You still don’t understand? The Three Paths Sect was established according to that person’s will. As if you could have guessed at a thirty-year grand plan. Heh heh.”

“Thirty years?”

It was an unimaginably long time. There were only a handful of people who could lie low for that many years and plot to seize Shanxi Province.

Only one person came to mind.

*The Head Elder?*

What possible reason could he have?

The Head Elder was the one who had pulled Jin Wikyung to his feet while he blamed himself in front of the children’s bodies. He was also the one who had halted every political maneuver and actively cooperated.

Thanks to that, the Jin Family of Taiyuan had united and made it this far…

*Wait.*

My head spun.

*Could it be?*

“Hyuk Mujin. How many martial artists from the newly joined small and mid-sized sects are there?”

“If you add the Three Paths Sect and Gunggwimun together, well over a hundred.”[^2]

“And under the Head Elder?”

“If you mean the Head Elder’s faction, probably close to half the main force… Ah!”

Hyuk Mujin and the reconnaissance-squad members opened their mouths as they grasped the situation.

If my guess was right and the Head Elder was a traitor, everything fit.

Helping Jin Wikyung had been nothing more than a setup for today.

*To take everything in a single battle.*

He had helped Jin Wikyung and united the family’s strength for this very day.

Suddenly I remembered what Gwak Jun had said before the fight.

That one line about Shanxi’s master changing. It no longer sounded like nonsense.

*The main force is in danger.*

I had to tell Jin Wikyung.

“We’re moving out. Right now!”

I shouted and was about to turn.

“Already too late.”

Gwak Jun grinned, baring bloodstained teeth.

“Too late for me, too late for you bastards, and too late for the Jin Family of Taiyuan and the Mount Heng Sword Sect. The grand plan has already begun.”

At the same time, blood gushed out. From his eyes, nose, and mouth—from every opening.

Gwak Jun’s head slowly drooped.

Hyuk Mujin spoke with a sickened look on his face.

“He severed his own heart meridian.”

Gwak Jun’s death meant one thing.

Ding. Ding. Ding.

> **System**
>
> — Defeated **Lv.40 Gwak Jun**!
>
> — **Slay the Assassins** (20/20)
>
> — Quest **Slay the Assassins** complete!
>
> — Level up!
>
> — Fame increases by 50!

Quest complete, a level-up, and a Fame increase.

After all those notifications, a single message appeared.

> **System**
>
> — All conditions for **Logout** have been met.
>
> — Logging out in 3 seconds. 3, 2…

Strength drained from my whole body. It felt as if I were floating.

Hyuk Mujin, startled, caught me.

“Squad Leader!”

His voice came through full of static. My vision blurred, and my body slipped out of my control.

*Not now. Not like this…*

*Of all times.*

And then—

> **System**
>
> — 1.

Darkness crashed in.

[^1]: Golden Sore Medicine is a salve for blade wounds.
[^2]: Gunggwimun is the name of another small sect newly allied with the Jin Family.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 38`.

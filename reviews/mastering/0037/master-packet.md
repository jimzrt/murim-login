# Master Edit Task — Chapter 37

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
| 진위경    | **Jin Wikyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 월화     | **Wolhwa**         |
| 화양검    | **Blade of Flowers**          | Jin Baekyang   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 팔천협    | **Eight Spring Gorge** |
| 정마대전   | **Great Faction War**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 곽준 | **Gwak Jun** |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
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

#### Chapter 35 tail (verified mastered)

…
“You were in no state to collect it at the time. Now that its owner is here, returning it is only right.” *What is it?* Still bewildered, I took the bundle. It was fairly heavy. Just as I was about to check what was inside, Gong Yacheong spoke. “Unwrap it in your quarters. Don’t let anyone else see.” *Did he put a golden calf in here?* * * * I unwrapped the bundle the moment I reached my quarters. Then I understood what Gong Yacheong’s last words had meant. *These really are the kind of things people would covet if they saw them.* An old booklet. A small box. And a familiar sword. To someone in Murim, these were worth far more than any golden calf. And I had the ability to judge their value more accurately than anyone. *Check Item.* Ding. > **System** > > **Item Window** > > **Flame Divine Palm** > > **Type:** Martial Arts Manual > > **Grade:** Supreme Peak > > **Restriction:** Holder of Scorching Yang Qi > > **Description:** One of the Fire Gate Clan’s secret techniques. A martial art based on powerful fire qi. > > **Effect:** Learn Flame Divine Palm > > **Item Window** > > **Fire Divine Elixir** > > **Type:** Spiritual Elixir > > **Grade:** Peak > > **Restriction:** None > > **Description:** A spiritual elixir made according to the Fire Gate Clan’s secret formula. > > **Effect:** Grants thirty years of internal energy when consumed. However, if the user cannot control the powerful fire qi contained within the elixir, they may meet a horrific end. > > **Item Window** > > **Nameless Sword** > > **Type:** Sword > > **Grade:** None > > **Restriction:** None > > **Description:** Made of ten-thousand-year cold iron, this sword is exceptionally sharp and hard. After drinking countless amounts of blood over a long time, it changed on its own. Special conditions are required to draw out the sword’s power. > > **Effect:** Unknown “This is insane.” It really was insane. A Supreme Peak martial arts manual. A spiritual elixir that granted thirty years of internal energy. And a sword I didn’t fully understand but that looked ridiculously good. They said a tiger left its pelt behind when it died, but Jopil had left three things like these. *Shit. It always gives me the good stuff after everything’s over.* Goddamn trash game. If it was going to give me something, it should’ve done it sooner. Playing catch-up after everything was finished just spiked my blood pressure. *Still, these items are seriously good.* Reading the descriptions, I caught myself getting tempted. What if I absorbed the elixir and learned Flame Divine Palm? Fire shooting from my hands like Jopil… *That would be fucking cool.* But the thought lasted only a moment. They said that in your last stretch before discharge, you had to watch out even for falling leaves. I didn’t want to swallow the elixir wrong and hold a self-immolation ceremony. *Remember this. Safety first. Safety first.* Talking about safety at this point was pretty funny, but I wasn’t stupid enough to just gulp it down. *It’s almost over.* One slip and I’d be gone. I stuffed all the items into my Inventory. Somewhere in the dead of night, someone must have been talking about me over drinks, because a System alert rang out. Ding. > **System** > > — Fame has increased by 1. * * * At that hour, the Head Elder was walking through the garden. This was the appointed date and place. The man in the darkness was never late. “The moon is very bright.” “So it is.” As he had said, tonight’s full moon was exceptionally bright. “When I was young, I really loved the moon… but the older I got, the more I found myself thinking.” “Thinking what?” “That I wished there were no moon. Something like that.” “A world without charm.” “What’s wrong with a little less charm? I make my living at night, so I’d be delighted if the moon disappeared.” *Night life, huh.* He ran his mouth in a flippant, cheerful tone like a kept man, but the Head Elder knew the truth. He possessed formidable martial arts, and he was a superb assassin. The wind seemed to carry the smell of blood. “Ah, right. How is the work progressing?” “Smoothly. Even the troop deployments are finished.” “Don’t overdo it. If the clever Lesser Family Head catches a whiff of it, everything will go wrong.” “Don’t worry. I didn’t even need to make a move.” “Heaven is helping us.” “And your side?” “You’re asking the obvious.” The light reproach in his words made the Head Elder fall silent. *As if it would be otherwise.* They were like sea fog. Their identities lay hidden under the mist, and even if you reached out and stirred it with your hand, there was no substance to grasp. All that remained was a damp palm and an unpleasant feeling. *But they have power.* The power to make him Family Head of the Jin Family of Taiyuan and the sole hegemon of Shanxi. It was an ambition he had harbored for half his life. The Head Elder was prepared to do anything. “All preparations are complete.” “Mine as well.” On the day the two great sects that divided Shanxi between them clashed… Everything would end, and everything would begin anew.

#### Chapter 36 tail (verified mastered)

…
order to make camp finally came once we entered a wide basin. “Ugh, every bone in my body hurts.” Hyuk Mujin groaned. Since he clearly wasn’t fully recovered, the march seemed to be too much for him. “It’s not too late. Want to turn back even now?” “Are you saying that again?” “I’m saying it because you look like you’re struggling.” “You’re mistaken. Does Hyuk Mujin, a man among men, look like someone who’d get tired after walking for a mere half day?” I nodded without the slightest hesitation. “Yep.” “Absolutely not!” “Hmm. You’re really not tired? You’re fine?” “Yes.” “Then go help the others set up camp.” At that moment, Hyuk Mujin, man among men, snapped his eyes wide and sank to the ground. “Ugh, the internal injuries Jopil gave me…” “…” *You said your internal injuries had healed, you bastard.* I was wondering whether I ought to hit him when a voice cut in. “Is he injured?” A massive shadow stretched under the moonlight. Hyuk Mujin cautiously lifted his head to see who it was, then his eyes flew open. “Gasp! Lesser Family Head!” If Jin Wikyung was a division commander, Hyuk Mujin was a private. The next moment, Hyuk Mujin sprang to his feet like lightning and stood at attention. Jin Wikyung burst out laughing. “You still don’t look fully recovered. Lie back down. Ah, the internal injuries do seem fully healed. I’ll vouch for that.” “Ah, I, that isn’t…” Jin Wikyung lightly patted the flustered Hyuk Mujin on the shoulder, then turned to me. “Shall we walk for a bit?” I followed him to a secluded corner. He spoke first. “How’s your condition?” “Good.” I’d reaped the full benefits of leveling up. My body had recovered at a terrifying speed, and allocating my points had made it even stronger. The problem was something else. *My Fame isn’t going up.* No, it was going up. Really, by about a rat dropping’s worth. Little by little. Very, very little. At this rate, there was no guarantee I’d be able to log out before the fighting began. *At least, not if things kept going like this.* Jin Wikyung’s arrival was perfect timing. I brought up the idea I’d been mulling over. “I want to take on a mission.” His eyes went round at how bluntly I’d come out with it. “Hm? A mission?” “Now that I’ve recovered, I want to distinguish myself for our family.” I was proud of myself. To think I could deliver a line like that—a lie like that—with a straight face. “I-is that truly what you think?” “Yes.” The corners of Jin Wikyung’s eyes trembled. He looked like a wave of emotion was running through his whole body. *This is actually making me feel kind of guilty.* The reason I was putting on this unconvincing act was Fame. If I went out on even a reconnaissance mission and distinguished myself, Fame would come in. It would be even better if I ran into a reconnaissance unit from the Mount Heng Sword Sect. Not only would that be excellent EXP, I’d be able to fill all the Fame I had left. *Once the real battle starts, it’s over.* I had to log out, and fast, before then. I spoke in a voice full of resolve. “Just leave it to me.” “How did you come to have such an admirable thought? Thank you, my youngest brother.” Jin Wikyung wiped the damp corners of his eyes with his sleeve and went on. “But no.” “Then please give me a reconnaissance mission—what?” “I appreciate the thought. Keep guarding the rear as you are now.” *What is he talking about?* I barely suppressed the urge to grab him by the collar and shake him. “I-I really want to distinguish myself.” “You’ve already done more than enough.” “No, that’s not what I mean.” “The merits you’ve earned so far have already been a great help to our family. So don’t trouble yourself over it.” “I’d like you to give me even one reconnaissance mission. There could be enemies lying in ambush ahead…” Jin Wikyung laughed softly. “This is a battle with our family’s fate at stake. Do you think I wouldn’t have accounted for something like that?” “Couldn’t there be a one-in-ten-thousand chance we missed something?” “That is, quite literally, one in ten thousand.” *Damn it.* Nothing was going my way. What if I really failed to fill my Fame at this rate? Then I’d have to fight a large-scale battle with fifteen hundred people committed. *I’m fucked.* Something large and warm settled on my dejected shoulder. Jin Wikyung’s hand. “Youngest.” His voice was heavy and lonely. At the sudden change in mood, I fell silent and listened. “Your mission is graver than anyone else’s among us.” “What’s my mission?” After letting it hang for a long time, he forced out a single word. “Survive.” “Huh?” “Survive however you can. If our family loses, run without looking back.” “…” “If the roots live, the tree will grow again. Second Brother and you could become better roots than I.” I was speechless. For a long while, I could only stare at his face. Survive. Become roots. His voice and eyes hit home with more seriousness than ever before. “That is your mission.” The palm resting on my shoulder slid slowly down. I stared after Jin Wikyung’s departing back, unable to look away.

## Korean source

```text
＃37화



이동은 순조로웠다. 지난번 정찰 임무 때 내린 폭설은 녹아 없어진 지 오래였고 지휘부는 병력의 힘을 최대한 비축시키며 이동했다.

“지금 속도라면 늦어도 내일 정양(定壤)에 도착하겠군요.”

어쩐지 낯익은 남자의 말에 나는 눈을 껌뻑거렸다.

“누구신지?”

복색을 보아하니 태원진가 쪽 사람은 아니다. 내가 있는 후미에는 정찰조원들을 제외하면 새로 합류한 중소 문파의 무사들이 대다수였으니 당연했다.

“삼도문의 곽준이라 합니다. 일전에 한 번 인사를 드렸었는데…… 손도 잡았었죠.”

삼도문의 곽준? 기억이 날 듯 말 듯 한데.

명성치 올리려고 잡은 손이 한 둘이냐. 아마 그들 중 하나였겠지.

“죄송합니다. 제가 기억력이 좀 안 좋아서.”

“사실 기대도 안 했습니다. 하하.”

친근한 웃음을 지어 보인 곽준이 재차 입을 열었다

“사실 처음에는 후미에 배치되었다는 사실에 실망했습니다.”

“왜요?”

“공을 세울 기회가 적어지니까요. 저 같은 무명 소졸이 이름을 알릴 기회 아니겠습니까?”

“아, 예.”

이런 경우는 둘 중 하나다. 정말 많은 전투를 겪어서 강심장이 됐거나, 겁이 없는 놈이거나. 나는 [기감]을 끌어올렸다.

띠링.



[Lv.40 곽준]



오, 한가락 하는데?

40레벨이면 최소 일류다. 나 고수라고 큰소리 뻥뻥 치지는 못해도 후미에만 처박혀 있는 게 억울할 정도는 된다.

“적들의 병력 중 절반은 급하게 충원된 자들입니다. 별의별 쭉정이들까지 끌어들인 데다 본대에 합류하기 위해 강행군을 했을 테니 태원진가와 삼도문의 정예들에게는 상대도 안 되겠지요.”

말은 제법 그럴듯하다. 삼도문이 정예라는 걸 빼면.

나는 건성으로 고개를 끄덕였다.

“그렇군요.”

“적들보다 뛰어난 절정 고수들도 있지요. 소가주님과 위 대협도 계시지만 화양검(火魎檢)의 무명은 중원 전체에 퍼져 있지 않습니까.”

화양검. 처음 듣는 별호였지만 누군지 짐작할 수 있었다.

태원진가의 절정 고수는 셋이고 진위경과 위팽을 제외한다면 남는 건 한 사람뿐이니까.

‘대장로.’

그 노인네가 그 정도였나?

이어지는 곽준의 말은 찬양 일색이었다. 수십 년 전, 젊은 시절의 대장로가 베어 넘긴 고수들의 별호와 이름이 수도 없이 흘러나왔다.

“정마대전이 낳은 영웅이셨죠.”

과거의 전쟁 영웅이라. 곽준의 말만 들어 보면 정의를 사랑하고 불의를 보면 못 참는 협객 중의 협객인데…….

‘난 왜 볼 때마다 찝찝할까.’

첫인상 때문인지 몰라도 나는 대장로가 싫었다.

특유의 분위기와 상대방을 뚫어 보는 묘한 눈빛. 진위경에 맞서 정치적 파벌을 이루고 있다는 것까지.

하지만 그 후로 대장로는 진위경을 전폭적으로 지지해 주었고, 태원진가는 안팎으로 똘똘 뭉칠 수 있었다.

‘하긴, 외적이 침입하면 집안싸움도 멈춰야지.’

현재 대장로는 진위경과 함께 선두를 이끌고 있다. 그가 소문만큼의 고수라면 내일의 전투가 한층 수월해질 것이다.

“내일 화양검 대협께서 전장을 휩쓸 모습을 생각하니 벌써부터 가슴이 뛰는군요.”

곽준은 사흘 만에 소변본 사람처럼 몸을 부르르 떨었다.

이 자식은 긴장감이란 걸 모르나? 더군다나 우리가 이길 거라는 자신감은 어디서 나온 건지 모르겠다.

“승리를 확신하시는군요.”

“지면 큰일이죠.”

“예?”

큰일이 아니라 끝장나는 거 아니냐. 항산검문이 지금까지 해 왔던 짓을 보면 태원진가는 물론이고 우리 쪽에 가담한 중소 문파들까지 쑥대밭으로 만들 것 같은데.

“그게 무슨…….”

“농담입니다.”

이 자식도 또라이네. 어이없어하는 내게 곽준이 씩 웃어 보였다.

“이깁니다. 우리가.”

확신에 찬 한마디였다.

곽준이 그 말을 끝으로 멀어지자 혁무진이 다가와 물었다.

“누굽니까?”

“40레벨.”

“예?”

“있어. 자신감 넘치는 놈이.”

여러모로 마음에 안 드는 놈이다. 뭐, 이제 대화를 나눌 일도 없겠지만.



* * *



시간은 빠르게 흘렀다. 진군을 시작한 지 이틀째 되는 밤, 우리는 혼주에 도착했고 진위경은 지휘부를 모아 회의를 열었다. 그의 손에는 작은 종이가 쥐어져 있었다.

“하오문에서 보낸 전서요. 이틀 전 적들의 원군이 오태산을 넘었다는군.”

“그렇다면…….”

“지금쯤, 혹은 내일 중에 본대와 합류할 가능성이 높소.”

뭐지? 이해할 수가 없다. 원군이 합류하기 전에 본대를 쳤다면 훨씬 수월한 싸움이 됐을 텐데.

‘생각해 둔 게 있겠지.’

아니나 다를까, 이어지는 진위경의 말이 있었다.

“새로 합류한 적들의 원군은 지쳐 있고 식량은 바닥을 드러내고 있소. 내일 우리가 앞서 정양의 유리한 고지를 점하면 항산검문주는 고민할 거요. 물러서느냐. 부딪치느냐.”

다음 순간 진위경의 시선이 나를 향했다.

“그가 어떤 선택을 할까?”

순간 당황했지만 답은 나와 있다. 이제 와서 물러설 위인이었다면 이미 한참 전에 물러났겠지.

“부딪칠 것 같은데요.”

두 배에 달하는 병력, 절정 고수의 숫자도 밀리지 않는다. 적으로서는 속전속결로 이 싸움을 끝내려 할 것이다.

“바로 보았다.”

흐뭇하게 웃은 진위경이 탁자에 놓인 지형도를 짚어 나갔다.

“적들이 정양으로 진입할 수 있는 길은 네 곳. 허나 식량 사정이 여의찮은 그들은 가장 빠른 길을 선택하겠지.”

손가락이 멈춘 곳에는 팔천협(八天峽)이라는 지명이 적혀 있었다. 그때, 조용히 자리를 지키고 있던 대장로가 처음으로 말문을 열었다.

“팔천협이라. 항아리 모양에 입구가 좁고 가파른 곳이지. 마적 떼들은 애마를 버려야겠구려.”

“목숨도 버리고 가야지요.”

“적들도 목숨을 불사하고 싸울 터, 이 정도로는 부족하오.”

“협곡 위 절벽에 각궁 백여 자루를 숨겨 두었습니다.”

“허어.”

막사 안이 술렁였다. 나도 입을 벌리고 진위경을 바라봤다.

아니, 도대체 그건 언제 숨겨 뒀대?

“혼주에서의 승리 직후였습니다. 수완 좋은 조력자 덕분이지요.”

진위경이 나를 똑바로 바라보며 말했다.

‘하오문. 월화구나.’

보이지 않는 곳에서 끊임없이 도움을 주고 있다. 물론 이 정도까지 큰 그림을 그린 진위경도 대단하다.

‘존나 멋있어.’

저 인간 분쇄기 같은 덩치에 명석한 두뇌라니. 갑자기 형이라고 부르고 싶어진다.

“오오.”

“소가주……!”

시커먼 사내놈들의 뜨거운 시선에 막사가 후끈 달아오른다.

진위경이 묵직한 눈빛으로 좌중을 훑었다.

“이제 결착을 냅시다.”

이견은 없었다. 가장 먼저 자리에서 일어난 대장로가 진위경을 향해 포권을 취했다.

“존명.”

그렇게 회의가 끝났다. 막사를 나오는 내 귓가로 익숙한 목소리가 파고들었다.

- 어제 했던 말, 잊지 말거라.

순간 몸이 굳는다. 하지만 이내 작게 고개를 끄덕여 보였다.

그리고 그날 새벽, 태원진가의 무사 삼백과 중소 문파의 지원군 백오십. 도합 사백오십의 병력이 협곡을 향해 떠났다.

‘그래도 마지막인데, 인사도 제대로 못 했네.’

나는 언덕에 올라 굽이치는 횃불을 하염없이 바라보았다.



* * *



다음 날 아침, 나를 본 혁무진이 흠칫 놀라며 물러났다.

“깜짝이야. 무슨 일이에요?”

“뭐가?”

“뭐긴요. 얼굴이 산송장 같아요. 안 주무셨어요?”

“아냐. 조금 잤어.”

거짓말이다. 사실 한숨도 못 잤다. 바위에 틀어 앉아 밤이 새도록 시스템창만 들여다보고 있었다.

마침내 코앞으로 다가온 그 순간을 손꼽아 기다리며.



명성 500 달성 (497 / 500)



숫자 1이 이렇게 소중하게 느껴질 줄이야.

나는 부쩍 늙어 버린 목소리로 중얼거렸다.

“간다, 간다, 이제 집 간다…….”

“이제는 혼잣말까지 하네. 실성했어요?”

쯧쯧. 혀를 차던 혁무진이 눈을 동그랗게 떴다.

“그건 뭐예요? 못 보던 물건인데.”

“이거?”

나는 바위에 올려 둔 낡은 서책과 조그마한 함을 차례대로 가리켰다.

“하나는 비급. 하나는 영단.”

“헉. 진짜요?”

반쯤 눈이 튀어나온 녀석에게 힘없이 설명해 주었다.

“비급은 초절정 무공이고, 영단은 잘만 흡수하면 반 갑자.”

“예?”

“그런데 영단 잘못 먹으면 타 죽는다더라. 너 먹을래?”

“아, 예에…….”

시큰둥한 얼굴과 댓 발 튀어나온 주둥이를 보아하니 내 말을 쥐뿔도 안 믿는 것 같다.

하긴, 난데없이 초절정 무공에 반 갑자짜리 파이어볼 영단이라고 하니 장난으로 생각할 만도 하지.

“진짜 안 먹어? 좋은 건데.”

“어이구, 됐습니다. 초절정 무공 많이 익히시고 영단 꼭꼭 씹어 드십쇼.”

“난 이제 이런 거 필요 없어.”

“그럼요. 잠룡이신데.”

평소 같았으면 뒤통수라도 한 대 후려쳐 줬을 텐데. 지금은 별 느낌 없다.

‘이게 말년 병장의 기분인가?’

동시에 기분이 이상해졌다. 워낙 많은 일을 겪은 후유증인가? 한 달 남짓인데 일 년은 있었던 것처럼 아련하다.

나는 과거의 기억을 더듬어 나갔다.

‘처음 홍화루에서 눈을 떴지.’

그곳에서 월화를 처음 만났고 이 게임에 갇혔다는 사실을 깨달았다. 그때만 생각하면 지금도 소름이 끼친다.

‘진짜 미쳐 버리는 줄 알았는데.’

태원진가에 오기로 결심하는 데만 사흘이 걸렸다. 거기서 만난 게 이 녀석, 혁무진이다.

빡!

“억! 왜 때려요?”

“음. 그냥 옛날 생각이 나서.”

“옛날 언제요?”

“안 돼. 안 알려 줘. 빨리 돌아가.”

“무슨 뒷골목 파락호예요? 무공 좀 세다고 이렇게 사람을 핍박해도 되는 겁니까?”

혁무진이 길길이 날뛰자 사람들의 시선이 우리를 향해 쏠렸다. 강 건너 불구경하던 정찰조원들까지 끼어들었다.

“두 분이서 무슨 얘기 중이에요?”

“몰라. 부조장이 잘못했겠지.”

“야, 난 아무것도 안 했어!”

“무림이잖아. 약한 게 죄야.”

“그런데 우리 이러고 있어도 되는 겁니까?”

누군가의 말에 순간 침묵이 흘렀다.

“그러게. 여기서 대기하는 게 우리 임무긴 한데…….”

억지웃음으로 억누르고 있던 긴장과 두려움이 감돈다. 곧 현실로 돌아갈 나조차 진위경의 모습이 어른거려 찝찝한 마당에 이 녀석들이야 오죽하겠나. 내가 해 줄 말은 하나밖에 없다.

“난 형님을 믿는다.”

형님. 이번만큼은 그 단어에 진심을 실었다. 이곳에서 내게 가장 큰 힘이 되어 주었던 진위경이다. 이렇게라도 찝찝함을 털어 내고 싶었던 것일지도 모르겠다.

잠깐 굳어 있던 사람들의 얼굴이 풀렸다.

“저희도 마찬가집니다.”

혁무진도 슬쩍 끼어들었다.

“전 조장을 더 믿습니다.”

“와, 부조장 줄 갈아타는 솜씨가 아주.”

“이 자식들이. 여기 조장한테 목숨 빚지지 않은 놈 있어?”

“에이, 그렇게 말씀하시면 또 할 말이 없죠.”

“저도 조장 믿습니다. 사실 전 조장이 망나니 행세할 때도 다 알고 있었어요. 아, 저 사람은 잠룡이구나. 딱 감이 왔죠.”

기분이 묘했다. 마른오징어도 짜면 물이 나온다더니, 게임에서 NPC들을 상대로 이런 감정을 느낄 줄이야.

‘뭐, 솔직히…… 기분이 나쁘진 않네.’

문득 저 산 너머에 있을 진위경이 궁금했다. 전투가 시작됐는지, 시작됐다면 어느 쪽이 이기고 있는지.

그리고 그런 생각을 한 것은 나 혼자만이 아니었다.

“지금쯤이면 전투가 시작됐겠군요.”

삼도문의 곽준이다. 지금까지와는 달리 그는 흑색 무복을 걸치고 있었다.

‘저 녀석이 원래 저 옷이었던가?’

내 시선에 곽준이 어깨를 으쓱했다.

“전 이런 게 좋더라고요. 움직이기에도 편하고, 피 좀 튀어도 티도 안 나고. 자네들도 그렇지?”

마지막 질문은 우리를 향한 것이 아니었다. 곽준이 이끄는 삼도문의 무사들. 빠짐없이 흑의로 갈아입은 그들이 과묵하게 고개를 끄덕였다.

“그렇다는군요.”

만족스럽게 웃은 곽준이 내게 고개를 돌렸다.

“자, 이제 저희도 출발해 볼까요?”

이 새끼가 지금 뭐라는 거지?
```

## Current accepted English baseline

```markdown
# Chapter 37

The march went smoothly. The heavy snow that had fallen during our last reconnaissance mission had melted away long ago, and command moved us while conserving as much of the troops’ strength as possible.

“At this rate, we’ll arrive in Jeongyang by tomorrow at the latest.”

I blinked at the oddly familiar man’s words.

“Who are you?”

Judging by his clothes, he wasn’t from the Jin Family of Taiyuan. Aside from the reconnaissance squad, most of the people in the rear guard were martial artists from the newly allied small and mid-sized sects, so that made sense.

“I’m Gwak Jun of the Three Paths Sect. We met once before… We even shook hands.”

Gwak Jun of the Three Paths Sect? It was on the tip of my tongue.

*It wasn’t as if I’d shaken only one or two hands trying to raise my Fame.*

He was probably one of them.

“Sorry. My memory isn’t very good.”

“I wasn’t expecting you to remember, honestly. Haha.”

Gwak Jun gave me a friendly smile and went on.

“To be honest, I was disappointed at first when I found out we’d been assigned to the rear guard.”

“Why?”

“Because there’d be fewer chances to distinguish ourselves. Isn’t this the chance for an unknown grunt like me to make a name for himself?”

“Ah. Right.”

There were two possibilities in cases like this. Either he’d been through so many battles that he’d grown nerves of steel, or he was simply fearless.

I raised my **Qi Sense**.

Ding.

> **System**
>
> **Lv.40 Gwak Jun**

*Oh. He’s got some skill.*

At Level 40, he was at least First Rate. He couldn’t exactly go around bragging he was a master, but it was more than enough to feel wronged about being stuck in the rear.

“Half of the enemy troops were recruited in a hurry. They’ve dragged in every kind of deadweight, and they must have force-marched to join the main force. They won’t stand a chance against the elites of the Jin Family of Taiyuan and the Three Paths Sect.”

His words sounded plausible enough.

*If you leave out the part about the Three Paths Sect being elite.*

I nodded half-heartedly.

“I see.”

“And we have Peak masters superior to the enemy’s as well. There’s the Lesser Family Head and Great Hero Wipeng, of course, but the reputation of the Blade of Flowers has spread throughout the Central Plains, hasn’t it?”

The Blade of Flowers. It was the first time I’d heard the title, but I could guess who he meant.

The Jin Family of Taiyuan had three Peak masters. Exclude Jin Wikyung and Wipeng, and only one person was left.

*The Head Elder.*

*Was that old man really that strong?*

Gwak Jun’s next words were nothing but praise. Title after title, name after name of masters the Head Elder had cut down in his youth, decades ago, came spilling out.

“He was a hero born of the Great Faction War.”

A war hero from the past. Listening to Gwak Jun, he sounded like a chivalrous hero among chivalrous heroes—a man who loved justice and couldn’t stand to see injustice go unpunished…

*Then why do I feel so uneasy every time I see him?*

Maybe it was the first impression, but I disliked the Head Elder.

That peculiar air of his. The strange gaze that bored straight through people. The fact that he had formed a political faction against Jin Wikyung.

And yet after that, the Head Elder had thrown his full support behind Jin Wikyung, and the Jin Family of Taiyuan had been able to pull tight together, inside and out.

*Well, when an outside enemy invades, even family feuds have to stop.*

The Head Elder was currently leading the vanguard alongside Jin Wikyung. If he really was as skilled as the rumors claimed, tomorrow’s battle would be that much easier.

“Just thinking of Great Hero Blade of Flowers sweeping the battlefield tomorrow already has my heart racing.”

Gwak Jun shuddered like a man taking a piss after three days.

*Does this bastard not know what tension is?*

And where was he getting the confidence that we were going to win?

“You’re certain of victory.”

“If we lose, we’re in big trouble.”

“Excuse me?”

*Not big trouble. We’d be finished.*

Judging by everything the Mount Heng Sword Sect had done so far, they would turn not only the Jin Family of Taiyuan but the small and mid-sized sects allied with us into a wasteland.

“What do you mean by—”

“I’m joking.”

*This bastard’s a lunatic too.*

As I stared at him, speechless, Gwak Jun flashed me a grin.

“We’ll win. We will.”

One sentence, packed with conviction.

When Gwak Jun left it at that and moved away, Hyuk Mujin came up and asked,

“Who was that?”

“Level 40.”

“What?”

“There’s this guy. Overflowing with confidence.”

I didn’t like him, in more ways than one.

*Well, it wasn’t as though I’d have to talk to him again.*

* * *

Time passed quickly. On the second night after we began the march, we reached Honju, and Jin Wikyung gathered the command staff for a meeting. He was holding a small slip of paper.

“A letter from the Lower District Sect. The enemy reinforcements crossed Mount Otae two days ago.”

“Then…”

“They’re likely to join the main force around now, or sometime tomorrow.”

*What?*

I couldn’t understand it. If we had attacked the main force before the reinforcements joined them, the fight would have been much easier.

*He must have something in mind.*

Sure enough, Jin Wikyung went on.

“The enemy reinforcements that just joined them are exhausted, and their food is running out. If we take Jeongyang’s high ground first tomorrow, the Mount Heng Sword Sect Leader will have a choice to make. Fall back, or clash.”

The next moment, Jin Wikyung’s gaze shifted to me.

“What choice do you think he’ll make?”

I was caught off guard, but the answer was already there. If he were the kind of man to fall back at this point, he would have done so long ago.

“I think he’ll clash.”

Twice our numbers, and they weren’t behind us in Peak masters either. From the enemy’s side, they would want to end this fight as fast as possible.

“Exactly.”

Jin Wikyung smiled, pleased, and traced a finger across the topographic map on the table.

“There are four routes the enemy can take into Jeongyang. But with their food situation as it is, they’ll choose the fastest one.”

His finger stopped on a place labeled Eight Spring Gorge. The Head Elder, who had been sitting quietly until then, spoke for the first time.

“Eight Spring Gorge. Jar-shaped, with a narrow, steep mouth. The mounted bandits will have to abandon their prized horses.”

“They’ll have to abandon their lives too.”

“The enemy will fight with their lives on the line as well. This much won’t be enough.”

“I’ve hidden some hundred horn bows on the cliffs above the gorge.”

“Hoh.”

A stir ran through the tent. I stared at Jin Wikyung with my mouth open.

*When the hell did he hide those?*

“Right after our victory at Honju. Thanks to a resourceful ally.”

Jin Wikyung looked straight at me as he said it.

*The Lower District Sect. Wolhwa.*

She had been helping us constantly from places we couldn’t see. Of course, Jin Wikyung was impressive too, for drawing a picture this big.

*That’s fucking cool.*

A build like a human meat grinder, and a sharp mind to go with it. Suddenly I wanted to call him big brother.

“Oh!”

“The Lesser Family Head…!”

The tent went hot under the burning gazes of those dark, burly men.

Jin Wikyung swept a heavy look over everyone assembled.

“Let’s settle this.”

No one objected. The Head Elder was the first to rise, then gave Jin Wikyung a fist-in-palm salute.

“By your command.”

That was the end of the meeting. As I left the tent, a familiar voice bored into my ear.

—Don’t forget what I told you yesterday.

I stiffened for a moment. Then I gave a small nod.

And at dawn that day, three hundred martial artists from the Jin Family of Taiyuan and one hundred fifty reinforcements from the small and mid-sized sects—four hundred fifty in all—set out for the gorge.

*Still, this was the end, and I hadn’t even said a proper goodbye.*

I climbed a hill and stared endlessly at the winding line of torches.

* * *

The next morning, Hyuk Mujin flinched when he saw me and stepped back.

“You startled me. What’s going on?”

“What?”

“What do you mean, what? You look like a living corpse. Did you not sleep?”

“Nah. I slept a little.”

That was a lie. I hadn’t slept a wink. I had planted myself on a rock and stared at the System Window all night.

Counting down to the moment that had finally come right up to my nose.

> **System**
>
> Achieve Fame 500 (497/500)

I never thought the number 1 could feel this precious.

In a voice that had aged all of a sudden, I muttered,

“I’m going, I’m going, going home now…”

“Now you’re even talking to yourself. Have you lost your mind?”

Hyuk Mujin clicked his tongue, then his eyes went round.

“What’s that? I’ve never seen those before.”

“This?”

I pointed in turn at the old book and the small case sitting on the rock.

“One’s a martial arts manual. The other’s an elixir.”

“Hah. Really?”

I explained it weakly to the guy whose eyes were halfway out of his head.

“The manual’s a Supreme Peak martial art, and if you absorb the elixir right, it’s thirty years.”

“What?”

“But they say if you take the elixir wrong, you’ll burn to death. You want it?”

“Ah. Sure…”

Judging by that unimpressed face and the snout sticking out a good few feet, he didn’t believe a damn word I was saying.

*Well, if someone suddenly came at me with a Supreme Peak martial art and a thirty-year Fireball elixir, I’d figure it was a joke too.*

“You really won’t eat it? It’s good stuff.”

“Oh, I’m fine. Learn plenty of that Supreme Peak martial art, and be sure to chew your elixir thoroughly.”

“I don’t need this kind of thing anymore.”

“Of course. You’re the Sleeping Dragon.”

Normally I would have smacked him in the back of the head. Right now I didn’t feel much of anything.

*Is this how a short-timer sergeant feels?[^1]*

At the same time, I felt strange. Was it the aftereffect of everything I’d been through? It had only been a little over a month, but it felt distant, as if I’d been here a year.

I started tracing back through old memories.

*I first opened my eyes at Honghwaru.*

That was where I met Wolhwa for the first time and realized I was trapped in this game. Even now, thinking about that moment gave me goose bumps.

*I really thought I was going to lose my mind.*

It had taken me three days just to decide to go to the Jin Family of Taiyuan. And the guy I met there was this one—Hyuk Mujin.

Smack!

“Argh! Why did you hit me?”

“Hmm. Just thought of the old days.”

“What old days?”

“Nope. Not telling. Get back already.”

“What am I, some back-alley punk? Just because your martial arts are a bit strong, you think you can oppress people like this?”

As Hyuk Mujin threw a fit, everyone’s eyes turned toward us. Even the reconnaissance-squad members who had been watching like it was none of their business jumped in.

“What are you two talking about?”

“Dunno. The deputy squad leader must have done something wrong.”

“Hey, I didn’t do anything!”

“This is Murim. Being weak is a crime.”

“But should we even be doing this?”

At someone’s words, silence fell for a moment.

“True. Waiting here is our mission, but…”

The tension and fear they had been holding down with forced smiles hung in the air. Even I, who would soon be going back to the real world, felt uneasy with Jin Wikyung’s face flickering through my mind. How much worse must it be for these guys?

There was only one thing I could say.

“I trust my big brother.”

*Big brother.* This time, I put my heart into the word.

Jin Wikyung had been the greatest source of strength I’d had in this place. Maybe I simply wanted to shake off that unease, even if only like this.

The faces that had stiffened for a moment eased.

“We feel the same.”

Hyuk Mujin slipped in as well.

“I trust the squad leader more.”

“Wow. Deputy squad leader, that side-switching of yours is really something.”

“You little bastards. Is there anyone here who doesn’t owe the squad leader their life?”

“Well, when you put it that way, what can we say?”

“I trust the squad leader too. Honestly, I knew all along, even when you were playing the thug. I thought, *Ah, that man is the Sleeping Dragon.* I could tell right away.”

I felt strange.

*They say even dried squid gives water if you squeeze it. Who knew I’d feel something like this toward NPCs in a game?*

*Well, honestly… it doesn’t feel bad.*

Suddenly I wondered about Jin Wikyung, somewhere beyond those mountains. Had the battle started? If it had, which side was winning?

And I wasn’t the only one thinking that.

“By now, the battle must have started.”

It was Gwak Jun of the Three Paths Sect. Unlike before, he was wearing black martial robes.

*Was that what this guy originally wore?*

At my look, Gwak Jun shrugged.

“I like this sort of thing. Easy to move in, and even if a little blood splatters, it doesn’t show. You all feel the same, right?”

That last question wasn’t aimed at us. It was for the martial artists of the Three Paths Sect whom he led. Every last one of them had changed into black, and they nodded without a word.

“Apparently so.”

Gwak Jun smiled, satisfied, then turned to me.

“Well, shall we set out too?”

*What the fuck is this bastard talking about right now?*

[^1]: A conscript sergeant in the last stretch of mandatory service, coasting toward discharge.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 37`.

# Master Edit Task — Chapter 36

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
| 조필     | **Jopil**          |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 낭인     | **wandering martial artist**                     |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 로그아웃             | **Logout**                     |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 대사      | **Master** for a senior Buddhist monk                           |
| 한엽 | **Han Yeop** |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

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

#### Chapter 34 tail (verified mastered)

…
begin with belief.” *They begin with belief.* It sounded like pie in the sky. But from the moment I heard those words, my heart was pounding. *They begin with belief…* Strangely, that one sentence kept circling through my mind, spinning round and round until I was dizzy. *What had I been believing in all this time?* The first word that came to mind—and the only one—was the System. The thing that had helped me more than anything else in this game and had always told me nothing but absolute facts. I had thought of myself as Second Rate because the System had told me I was Second Rate. *Because I believed in the System.* I had already overwhelmed Lee Seogeun, a First Rate master. I had taken down more than twenty wandering martial artists by myself, and I had even defeated Jopil, a Peak master. Everyone praised me as a First Rate master and a hero, but I was still Second Rate. Because I had believed in the System instead of myself. But now I understood. *I’m already First Rate.* Already. Maybe I had been for a long time. I was First Rate. “You look like you’ve just been slapped.” This time, Jin Wikyung was right. I slumped against the back of my chair, looking completely out of it. *What a dumbass.* If I couldn’t even believe in myself, I was Second Rate. No. I *had been* Second Rate. Ding. > **System** > > — You have reached the **First Rate** realm! > > — The realm of all martial arts increases by one stage! > > — Your Sinews and Bones and your Meridians improve greatly! > > — The size of your dantian expands! > > — Level Up! > > — Level Up! From Third Rate to Second Rate. Then from Second Rate to First Rate. I felt power surge from deep within my body, and Jin Wikyung burst out laughing. “What happened?” Wipeng showed up late and asked, looking bewildered. * * * It felt like a blocked nose had blown clear. Reaching First Rate had brought a tremendous leap in every way—senses, martial arts, everything. I left the main hall and started walking. The wind felt refreshing. “It’s the Third Young Master.” “Has he fully recovered?” Sure enough, people’s eyes gathered. I changed direction toward a place with even more people. *Anyone watching would take me for an attention hog.* But everything happens for a reason. Ding. > **System** > > — Someone gazes at you with awe. > > — Fame increases by 1. > > — Someone is impressed after hearing your rumors. > > — Fame increases by 1. As I walked, the crowd gathered like clouds. Plenty of NPCs dressed in unfamiliar clothing were mixed in among them. *Who are they?* My eyes met one of them. The young man looked a little over twenty. He flinched in surprise, then quickly approached and made a fist-and-palm salute. “Guo of the Three Paths Sect presents his respects.”[^1] “Ah, yes.” My own fist-and-palm salute now came out on reflex and looked fairly convincing. But where was the Three Paths Sect? *Oh. Could it be…?* “Are you with the Five Gates of Shanxi?” Guo Whatsisname nodded enthusiastically. “That is correct. Our Three Paths Sect has agreed to lend its strength to the Jin Family of Taiyuan. I, Guo, could not be more delighted to offer even the smallest assistance.” In a situation like this, he was a reinforcement worth his weight in gold. I grabbed Guo Whatsisname’s hand, hoping he would fight hard enough for my share as well. “Thank you for coming.” “Don’t mention it. It is merely an honor to be included in the Young Master’s tales of martial prowess.” > **System** > > — Someone is impressed after hearing your rumors. > > — Fame increases by 1. A complete stranger had come all this way to fight for us, and he was even helping my Fame climb. I offered my warm thanks to the freely giving Guo Whatsisname. “God bless you.” “Pardon?” “It means I hope the Jade Emperor’s blessing will be with you.” “Ahh. Thank you. Gapburaesuyu.” “Ah. Yes.” I put on a fake smile and kept walking. Maybe because everyone who needed to know already did, the Jin Family of Taiyuan’s people no longer raised my Fame. *Still, I’ve piled up quite a bit.* I opened the Status Window and saw that I was about fifty points short of the target. If I spent the next two days grinding hard, maybe I could Logout. “Um, Young Hero Jin.” I turned around. It was the fellow from the Three Paths Sect. He looked ready to follow me to the ends of the earth. “If you aren’t busy, perhaps we could have some tea together…” “I’m sorry. I have something to take care of.” It sounded like a lie, but it was the truth. My destination had been decided from the start. I pointed out a building to him as he looked disappointed. A faded signboard hung there, and the smell of medicinal decoctions rolled out thick. Medicine King Hall. And beneath it hung a small wooden plaque. **No Entry Except for Authorized Personnel.** The people surrounding me let out pitying sighs. [^1]: The sect’s name is written 三道問, using 問 (“question”) rather than the usual 門 (“gate” or “sect”).

#### Chapter 35 tail (verified mastered)

…
“You were in no state to collect it at the time. Now that its owner is here, returning it is only right.” *What is it?* Still bewildered, I took the bundle. It was fairly heavy. Just as I was about to check what was inside, Gong Yacheong spoke. “Unwrap it in your quarters. Don’t let anyone else see.” *Did he put a golden calf in here?* * * * I unwrapped the bundle the moment I reached my quarters. Then I understood what Gong Yacheong’s last words had meant. *These really are the kind of things people would covet if they saw them.* An old booklet. A small box. And a familiar sword. To someone in Murim, these were worth far more than any golden calf. And I had the ability to judge their value more accurately than anyone. *Check Item.* Ding. > **System** > > **Item Window** > > **Flame Divine Palm** > > **Type:** Martial Arts Manual > > **Grade:** Supreme Peak > > **Restriction:** Holder of Scorching Yang Qi > > **Description:** One of the Fire Gate Clan’s secret techniques. A martial art based on powerful fire qi. > > **Effect:** Learn Flame Divine Palm > > **Item Window** > > **Fire Divine Elixir** > > **Type:** Spiritual Elixir > > **Grade:** Peak > > **Restriction:** None > > **Description:** A spiritual elixir made according to the Fire Gate Clan’s secret formula. > > **Effect:** Grants thirty years of internal energy when consumed. However, if the user cannot control the powerful fire qi contained within the elixir, they may meet a horrific end. > > **Item Window** > > **Nameless Sword** > > **Type:** Sword > > **Grade:** None > > **Restriction:** None > > **Description:** Made of ten-thousand-year cold iron, this sword is exceptionally sharp and hard. After drinking countless amounts of blood over a long time, it changed on its own. Special conditions are required to draw out the sword’s power. > > **Effect:** Unknown “This is insane.” It really was insane. A Supreme Peak martial arts manual. A spiritual elixir that granted thirty years of internal energy. And a sword I didn’t fully understand but that looked ridiculously good. They said a tiger left its pelt behind when it died, but Jopil had left three things like these. *Shit. It always gives me the good stuff after everything’s over.* Goddamn trash game. If it was going to give me something, it should’ve done it sooner. Playing catch-up after everything was finished just spiked my blood pressure. *Still, these items are seriously good.* Reading the descriptions, I caught myself getting tempted. What if I absorbed the elixir and learned Flame Divine Palm? Fire shooting from my hands like Jopil… *That would be fucking cool.* But the thought lasted only a moment. They said that in your last stretch before discharge, you had to watch out even for falling leaves. I didn’t want to swallow the elixir wrong and hold a self-immolation ceremony. *Remember this. Safety first. Safety first.* Talking about safety at this point was pretty funny, but I wasn’t stupid enough to just gulp it down. *It’s almost over.* One slip and I’d be gone. I stuffed all the items into my Inventory. Somewhere in the dead of night, someone must have been talking about me over drinks, because a System alert rang out. Ding. > **System** > > — Fame has increased by 1. * * * At that hour, the Head Elder was walking through the garden. This was the appointed date and place. The man in the darkness was never late. “The moon is very bright.” “So it is.” As he had said, tonight’s full moon was exceptionally bright. “When I was young, I really loved the moon… but the older I got, the more I found myself thinking.” “Thinking what?” “That I wished there were no moon. Something like that.” “A world without charm.” “What’s wrong with a little less charm? I make my living at night, so I’d be delighted if the moon disappeared.” *Night life, huh.* He ran his mouth in a flippant, cheerful tone like a kept man, but the Head Elder knew the truth. He possessed formidable martial arts, and he was a superb assassin. The wind seemed to carry the smell of blood. “Ah, right. How is the work progressing?” “Smoothly. Even the troop deployments are finished.” “Don’t overdo it. If the clever Lesser Family Head catches a whiff of it, everything will go wrong.” “Don’t worry. I didn’t even need to make a move.” “Heaven is helping us.” “And your side?” “You’re asking the obvious.” The light reproach in his words made the Head Elder fall silent. *As if it would be otherwise.* They were like sea fog. Their identities lay hidden under the mist, and even if you reached out and stirred it with your hand, there was no substance to grasp. All that remained was a damp palm and an unpleasant feeling. *But they have power.* The power to make him Family Head of the Jin Family of Taiyuan and the sole hegemon of Shanxi. It was an ambition he had harbored for half his life. The Head Elder was prepared to do anything. “All preparations are complete.” “Mine as well.” On the day the two great sects that divided Shanxi between them clashed… Everything would end, and everything would begin anew.

## Korean source

```text
＃36화



퀘스트



[로그아웃]

이제 당신은 이 험난한 무림을 헤쳐 나가야 합니다.

더욱더 강해지고, 유명해지십시오.

언젠가 다가올 그 날을 위해…….



등급 : 메인 퀘스트

제한 : 진태경

임무 : [일류] 경지 달성 (완료)

         Lv.30 달성 (완료)

         명성 500 달성 (475/500)

보상 : [로그아웃]





퀘스트창을 껐다. 한겨울인데 식은땀이 날 것 같다.

‘이렇게 되면 완전 나가린데.’

조금씩 오르던 명성치가 어느 순간 뚝 멈췄다. 그게 반나절 전의 일이다. 처소를 뛰쳐나가 대선 후보처럼 손이 발이 되도록 악수를 하고 다녔지만 기다리던 알림은 울리지 않았다.

‘아니, 알림이 울리긴 했지.’

삐빅!



- [태원진가]에 당신의 명성을 모르는 사람은 없습니다.



이미 한계치까지 명성을 뽑아 먹었으니 적당히 하란 소리였다. 시스템이 보기에도 내 모습이 애잔했던 모양이다.

그렇게 하루가 속절없이 흘렀다. 그리고 오늘은 대망의 출정식이다.

“시파…….”

내가 작게 욕설을 내뱉을 때 진위경은 단상에 오르고 있었다.

수백 쌍의 눈동자가 그를 따라 움직인다. 태원진가의 무사와 새로 합류한 중소 문파의 무사들까지. 대연무장에 도열한 무사들의 숫자는 오백이 넘어갔다.

쿵. 쿵. 쿵.

어느 순간, 거대한 울림이 퍼져 나갔다. 누군가는 발을 구르고 누군가는 병장기를 두드린다. 공력을 지닌 무림인 오백 명이 한뜻으로 움직이자 땅이 흔들리고 굉음이 천지를 메웠다.

‘이게 무슨…….’

지금껏 본 적 없는 광경. 개인에서 하나의 군세(軍勢)가 된 그들은 이제 한 사람의 명령을 기다리고 있었다.

그리고 마침내 진위경의 입이 열렸다.

“부정하지 않겠다. 적들은 병력도, 절정 고수의 숫자도 우리보다 앞선다.”

순식간에 침묵이 내리깔렸다. 하지만 시작부터 사기를 깎아 먹을 정도로 진위경은 멍청한 사람이 아니다. 전신에서 뿜어져 나오는 기백이 바로 그 증거였다.

“그러나.”

평소의 사람 좋은 웃음은 온데간데없다. 지금의 진위경은 절정의 무인인 동시에 태원진가의 수장이었다.

“머릿수만 많은 승냥이에 불과하다. 저자의 무뢰배, 황금에 눈이 먼 낭인과 양민을 약탈하던 마적 떼!”

불길을 토해 내는 외침에 공기가 찌르르 울린다. 이 순간만큼은 나도 피가 끓어오르는 듯했다.

“놈들에게는 명분도, 정의도 없다.”

명분. 정의.

항산검문은 전쟁에 있어 가장 중요한 두 가지를 잃었다.

두 강자의 전쟁에 눈치만 살피던 산서성의 중소 문파들이 지원군을 보낸 이유이기도 했다.

“사흘 안에 이 전쟁은 끝난다.”

천오백의 무인들이 한날한시에 부딪힌다.

서로를 죽고 죽이는 지옥 같은 싸움이 될 것이다.

“이 중 어느 누구도 생사를 장담하지 못한다. 그러나…….”

진위경의 번뜩이는 눈동자가 모두를 담았다.

“우리는 반드시 승리할 것이다.”

다음 순간.

귀가 먹먹할 정도의 함성이 터져 나왔다. 최고조에 달한 분위기 속, 진위경은 거인처럼 우뚝 서 있었다.

“적자생존(適者生存)! 목숨을 걸고 싸워 살아남아라!”

함성은 그 후로도 오랫동안 이어졌다.



* * *



오백의 병력은 선두, 중앙, 후미로 나뉘었다. 핵심이 되는 전력은 대부분 선두와 중앙에 배치되었기 때문에 내가 맡은 후미에는 수십 명의 무사가 전부였다.

그중에는 제법 낯익은 얼굴들도 있었다.

“조장님!”

정찰조원들이다. 나는 반가움 반, 의아함 반으로 물었다.

“너희가 왜 여기 있냐? 약왕당에 있는 거 아니었어?”

“본가의 명운이 걸린 싸움 아닙니까. 조금 다쳤다고 빠질 수야 없죠.”

지난번에 몰래 들렀을 때는 팔다리에 금 간 놈도 있던데. 무림인들 터프한 거 보소.

“조장 밑에 넣어 달라고 요청했더니 상부에서도 흔쾌히 허락하더군요. 그날 이후로 저희도 어깨에 힘 좀 주고 다닙니다, 하하.”

“어쭈.”

피식 웃음이 나왔다. 정찰조 임무를 맡아 며칠을 함께했지만 이 중 몇몇은 이름도 모른다. 그럼에도 친근한 마음이 드는 것은 함께 생사를 함께했다는 동질감 때문이다.

‘하긴, 레이드 세 번이면 의형제도 맺는다는데.’

나는 오래된 헌터 격언을 떠올리며 여덟 명의 정찰조원들을 향해 웃어 보였다. 그리고 문득 생각했다.

‘아니, 잠깐만.’

여덟이라고? 내가 잘못 셌나?

나는 끝에서부터 한 명씩 다시 세기 시작했다. 일단 나를 제외하고 아홉 명. 거기에 혁무진과 한엽은 중상이니까 당연히 오지 못했을 테니 일곱이 되어야 하는데…….

“……너 여기서 뭐 하냐?”

보면서도 이놈이 그놈인가 싶다. 찐빵처럼 부푼 얼굴, 옷 밖으로 드러난 살은 울긋불긋하다.

“보면 모릅니까?”

맞다. 정찰조원 중 이런 싸가지 없는 놈은 하나밖에 없다.

“혁무진?”

“예. 왜요. 뭐요.”

“너 진짜 혁무진 맞아?”

“이젠 제 얼굴도 못 알아봅니까?”

지금 꼴이면 너희 부모님도 못 알아볼걸…….

아니, 그전에 이 자식이 왜 여기 있는 걸까.

“너도 자원했냐?”

“했죠.”

이어 덧붙인다.

“안 받아 줬지만.”

“응?”

“의원한테 말했는데 죽고 싶어서 환장했냐고 화를 내더군요. 그래서 그냥 몰래 빠져나왔습니다.”

나는 진지하게 말했다.

“죽고 싶어서 환장했냐?”

“살고 싶은데요.”

혁무진이 썩은 표정으로 대꾸했다.

“그럼 여길 왜 와?”

“제 몸 상태는 제가 압니다. 충분히 싸울 수 있어요.”

“얼굴은 터지기 직전인데.”

“부기 빠지는 과정입니다. 내상은 전부 나았으니 문제없습니다.”

“외상은?”

“가면서 낫겠죠.”

“…….”

“뼈 몇 군데에 금이 가긴 했는데 버틸 만합니, 컥!”

혁무진이 갑자기 허리를 숙였다. 나는 깜짝 놀라 외쳤다.

“야! 왜 이래?”

“가끔 숨 쉴 때마다 가슴이 아파서…… 아, 이제 괜찮아졌네요.”

“…….”

이거 완전히 미친놈 아냐.

말문이 막힌 내게 혁무진이 말했다.

“아, 한엽 그 녀석은 못 왔습니다. 내상도 안 나아서 짐만 되겠더라고요. 조장? 조장, 지금 제 말 듣고 있는 거 맞죠?”

머릿속에는 한 가지 생각밖에 없었다.

로그아웃, 로그아웃이 시급하다.



* * *



겨울의 밤은 빨리 찾아왔다. 그렇게 해가 저물고 얼마나 걸었을까, 너른 분지(盆地)에 진입한 후에야 야영 준비를 하라는 명령이 떨어졌다.

“어이구, 삭신이야.”

혁무진이 앓는 소리를 냈다. 아무래도 완쾌된 몸이 아니다 보니 힘에 부치는 모양이었다.

“아직 안 늦었는데, 지금이라도 돌아갈래?”

“또 그 소립니까?”

“힘들어 보여서 하는 소리지.”

“착각입니다. 사나이 혁무진이 고작 반나절 걸었다고 지칠 놈으로 보이십니까?”

나는 한 치의 망설임도 없이 고개를 끄덕였다.

“응.”

“절대 아닙니다!”

“음. 정말 안 힘들어? 멀쩡해?”

“예.”

“그럼 가서 애들 야영 준비하는 거나 도와.”

그 순간, 사나이 혁무진이 눈을 부릅뜨며 주저앉았다.

“큭, 조필에게 당한 내상이.”

“…….”

내상 다 나았다며, 이 새끼야.

이놈을 한 대 때려 줘야 하나 고민하던 찰나였다.

“부상자인가?”

달빛 아래 드리워진 거대한 그림자. 슬그머니 고개를 들어 상대를 확인한 혁무진이 눈을 부릅떴다.

“헉, 소가주님!”

진위경이 사단장이면 혁무진은 이등병이다.

다음 순간, 번개처럼 일어나 차렷 자세를 취하는 혁무진의 모습에 진위경이 껄껄 웃었다.

“아직 몸이 성치 않아 보이는데 누워 있게. 아, 내상은 확실히 나은 것 같군. 내가 보증하지.”

“아, 저, 그것이 아니옵고.”

진위경은 쩔쩔매는 혁무진의 어깨를 가볍게 두드려 준 후 나를 향해 돌아섰다.

“잠시 걸을까?”

나는 진위경을 따라 후미진 구석으로 이동했다. 그가 먼저 입을 뗐다.

“몸 상태는 어떠냐?”

“좋습니다.”

레벨 업의 효과를 톡톡히 누렸다. 무시무시한 속도로 완쾌된 육체는 포인트 분배를 통해 더욱 강해졌다.

문제는 따로 있다.

‘명성치가 안 올라.’

아니, 오르긴 오른다. 정말 쥐똥만큼. 조금씩, 아주 조금씩.

지금 속도라면 전투가 벌어지기 전에 로그아웃할 수 있을지 장담하기 어렵다.

‘이대로라면, 말이지.’

마침 진위경이 왔으니 잘됐다. 아까 전부터 생각해 두었던 말을 꺼냈다.

“임무를 맡고 싶습니다.”

다짜고짜 들어온 직진에 진위경의 눈이 동그랗게 떠진다.

“응? 임무?”

“몸도 나았으니 본가를 위해 공을 세우고 싶습니다.”

내 자신이 자랑스럽다. 이런 대사, 이런 거짓말을 당당하게 할 수 있다니.

“지, 진정 그게 네 생각이냐?”

“예.”

진위경의 눈초리가 파르르 떨렸다. 감동의 물결을 온몸으로 느끼고 있는 모양이었다.

‘이거 은근히 죄책감 드네.’

내가 되지도 않는 연기를 한 건 명성치를 위해서다. 정찰 임무라도 나가서 공을 세우면 들어오는 명성치.

항산검문의 정찰대와 맞닥트리면 더욱 좋다. 훌륭한 경험치일 뿐만 아니라 남은 명성치를 모두 채울 수 있을 테니까.

‘본격적인 전투가 일어나면 끝장이다.’

그전에 후딱 로그아웃을 해야 한다. 나는 결의 어린 목소리로 말했다.

“맡겨만 주십시오.”

“어찌 이런 기특한 생각을 했을꼬. 고맙구나, 막내야.”

진위경이 촉촉해진 눈가를 소매로 닦으며 말을 이었다.

“하지만 안 된다.”

“그럼 제게 정찰 임무를, 예?”

“마음만 받으마. 너는 지금처럼 후미를 지켜라.”

이게 뭔 소리야.

멱살이라도 잡고 흔들고 싶은 마음을 간신히 억눌렀다.

“그, 꼭 공을 세우고 싶습니다.”

“이미 차고 넘친다.”

“아뇨, 그게 아니라.”

“지금껏 세운 전공으로도 본가에 큰 힘이 됐다. 그러니 너무 마음 쓰지 말거라.”

“정찰 임무라도 하나 맡겨 주셨으면 좋겠는데요. 앞에 적들이 매복하고 있을 수도 있고…….”

진위경이 허허 웃었다.

“본가의 명운이 걸린 싸움이다. 내가 그런 것 하나 염두에 두지 않았을까.”

“만에 하나 놓치고 간 부분이 있지 않을까요.”

“말 그대로 만에 하나일 뿐이다.”

염병.

되는 일이 하나도 없다. 이러다가 정말 명성치를 못 채우게 되면? 그때는 천오백 명이 투입된 대규모 전투를 치러야 한다.

‘좆 됐다.’

낙담한 내 어깨 위에 크고 따뜻한 뭔가가 닿았다. 진위경의 손이다.

“막내야.”

무거우면서도 쓸쓸한 목소리다. 갑자기 바뀐 분위기에 나는 잠자코 귀를 기울였다.

“네 임무는 우리 중 누구보다 막중하다.”

“제 임무가 뭔데요?”

한참 뜸을 들인 끝에 한마디를 토해 낸다.

“살아남아라.”

“예?”

“어떻게든 살아남아. 본가가 패배한다면 뒤도 돌아보지 말고 도망치란 말이다.”

“…….”

“뿌리가 살아 있다면 나무는 다시 자란다. 둘째와 너는 나보다 훌륭한 뿌리가 될 수 있을 것이다.”

나는 말문이 막혀 한동안 가만히 그의 얼굴을 바라보고만 있었다.

살아남아라. 뿌리가 되어라. 그 어느 때보다 진지하게 와닿는 목소리와 눈빛이었다.

“그게 네 임무다.”

어깨에 얹혀 있던 손바닥이 스르륵 내려갔다. 나는 떠나는 진위경의 뒷모습을 하염없이 바라보았다.
```

## Current accepted English baseline

```markdown
# Chapter 36

> **System**
>
> **Quest**
>
> **Logout**
>
> You must now make your way through this harsh Murim.
>
> Become even stronger, and become famous.
>
> For the day that will one day come…
>
> **Grade:** Main Quest
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Reach the **First Rate** realm (Complete)
>
> Reach Lv. 30 (Complete)
>
> Reach Fame 500 (475/500)
>
> **Reward:** Logout

I closed the Quest Window. It was midwinter, and I still felt like I was about to break into a cold sweat.

*If this keeps up, I’m completely screwed.*

The Fame that had been climbing little by little had suddenly stopped dead. That had been half a day ago. I’d bolted from my quarters and shaken hands like a presidential candidate until I was worn to the bone, but the notification I’d been waiting for never came.

*No, I did get a notification.*

> **System**
>
> — There is no one in the Jin Family of Taiyuan who does not know your Fame.

It was the System’s way of telling me I’d already milked Fame to the limit and should knock it off. Even the System seemed to find me pitiful.

And so the day slipped away, and there was nothing I could do about it. Today was the long-awaited departure ceremony.

“Fuck…”

As I muttered the curse under my breath, Jin Wikyung was climbing onto the platform.

Hundreds of pairs of eyes followed him. Martial artists of the Jin Family of Taiyuan, and martial artists from the small and mid-sized sects that had newly joined us. More than five hundred martial artists stood in formation across the main training ground.

Boom. Boom. Boom.

At some point, a tremendous rumble spread through the air. Some stamped their feet; others struck their weapons. When five hundred martial artists with internal energy moved as one, the earth shook and a roar filled heaven and earth.

*What is this…?*

I had never seen anything like it. They had gone from individuals to a single military force, and now they were waiting for one man’s command.

At last, Jin Wikyung spoke.

“I will not deny it. The enemy is ahead of us in troop numbers and in the number of Peak masters.”

Silence dropped over them in an instant. But Jin Wikyung wasn’t foolish enough to kill morale from the opening. The presence pouring off his entire body was proof of that.

“However.”

His usual good-natured smile was gone without a trace. The Jin Wikyung standing before us was both a Peak martial artist and the head of the Jin Family of Taiyuan.

“They are nothing but jackals with numbers on their side. That man’s rabble—wandering martial artists blinded by gold, and a pack of mounted bandits who have plundered the common people!”

The air crackled under a shout that spat fire. Even I felt my blood boil, if only for that moment.

“They have neither cause nor justice.”

Cause. Justice.

The Mount Heng Sword Sect had lost the two most important things in a war.

That was also why the small and mid-sized sects of Shanxi Province, which had only been watching which way the wind blew in the war between two powers, had sent reinforcements.

“This war will be over within three days.”

Fifteen hundred martial artists would clash at the same hour on the same day.

It would be a hellish fight in which they killed and were killed.

“No one here can guarantee whether they will live or die. However…”

Jin Wikyung’s flashing eyes took them all in.

“We will surely win.”

The next moment.

A roar burst out, loud enough to leave my ears ringing. With the mood at its height, Jin Wikyung stood towering like a giant.

“Survival of the fittest! Fight with your lives on the line, and survive!”

The cheering went on for a long time afterward.

* * *

The five hundred troops were divided into vanguard, center, and rear guard. Most of the core fighting strength had been placed in the vanguard and the center, so the rear I’d been given had only a few dozen martial artists.

Some of the faces were fairly familiar.

“Squad Leader!”

They were members of the reconnaissance squad. Half pleased and half puzzled, I asked,

“Why are you guys here? Weren’t you at Medicine King Hall?”

“This is a battle with the fate of our family at stake. We can’t sit it out just because we’re a little injured.”

Last time I’d snuck over to visit, some of them had still had cracked bones in their arms and legs. Murim people really were tough as hell.

“When we asked to be placed under your command, the higher-ups readily approved it. We’ve been walking around with our chests puffed out ever since that day, haha.”

“Well, look at you.”

I let out a short laugh.

I’d spent several days with them on the reconnaissance mission, but I didn’t even know some of their names. Even so, I felt close to them—we’d been through life and death together.

*They say three raids are enough to make sworn brothers.*

I smiled at the eight reconnaissance-squad members. Then a thought suddenly struck me.

*No, wait.*

Eight? Had I counted wrong?

I started counting again from the end, one person at a time. Not counting me, there were eight. Han Yeop had serious injuries, so he obviously couldn’t have come—but Hyuk Mujin had snuck out to join us.

“…What are you doing here?”

Even looking at him, I wasn’t sure it was the same guy. His face was puffed up like a steamed bun, and the skin showing past his clothes was red and blotchy.

“Can’t you tell by looking?”

He was right. There was only one rude bastard on the reconnaissance squad.

“Hyuk Mujin?”

“Yes. Why? What?”

“Are you really Hyuk Mujin?”

“Can’t you recognize my face anymore?”

*Looking like that, even your parents wouldn’t recognize you…*

No. Before that—why was this bastard here?

“Did you volunteer too?”

“I did.”

He added,

“They didn’t take me, though.”

“Huh?”

“I told the physician, and he got angry and asked if I’d gone insane, wanting to die. So I just snuck out.”

I spoke seriously.

“Have you gone insane, wanting to die?”

“I want to live.”

Hyuk Mujin answered with a look like something had gone sour.

“Then why did you come here?”

“I know my own condition. I can fight well enough.”

“Your face looks like it’s about to burst.”

“The swelling is going down. My internal injuries have all healed, so there’s no problem.”

“What about the external injuries?”

“They’ll heal on the way.”

“…”

“A few bones are cracked, but I can handle i—kh!”

Hyuk Mujin suddenly bent forward at the waist. Startled, I shouted,

“Hey! What’s wrong?”

“Sometimes my chest hurts whenever I breathe… Ah, it’s fine now.”

“…”

Was this guy completely insane?

As I stood there speechless, Hyuk Mujin said,

“Ah, Han Yeop couldn’t come. His internal injuries haven’t healed, so he’d only be a burden. Squad Leader? Squad Leader, you are listening to me, right?”

There was only one thought in my head.

*Logout. Logout is urgent.*

* * *

Winter night came early. After the sun went down, we walked for who knew how long, and only after we entered a wide basin did the order come to prepare camp.

“Ugh, every bone in my body hurts.”

Hyuk Mujin groaned. Since he clearly wasn’t fully recovered, the march seemed to be too much for him.

“It’s not too late. Want to turn back even now?”

“Are you saying that again?”

“I’m saying it because you look like you’re struggling.”

“You’re mistaken. Does Hyuk Mujin the man look like someone who’d get tired from walking a mere half day?”

I nodded without the slightest hesitation.

“Yep.”

“Absolutely not!”

“Hmm. You’re really not tired? You’re fine?”

“Yes.”

“Then go help the others prepare camp.”

At that moment, Hyuk Mujin the man snapped his eyes wide and sank to the ground.

“Ugh, the internal injuries I took from Jopil…”

“…”

*You said your internal injuries had healed, you bastard.*

I was wondering whether I ought to hit him when a voice cut in.

“Is he injured?”

A massive shadow stretched under the moonlight. Hyuk Mujin cautiously lifted his head to see who it was, then his eyes flew open.

“Gasp, Lesser Family Head!”

If Jin Wikyung was a division commander, Hyuk Mujin was a private.

The next moment, Hyuk Mujin sprang to his feet like lightning and stood at attention. Jin Wikyung burst out laughing.

“You still don’t look fully recovered. Lie back down. Ah, the internal injuries do seem fully healed. I’ll vouch for that.”

“Ah, I, that isn’t…”

Jin Wikyung gave the flustered Hyuk Mujin’s shoulder a light pat, then turned to me.

“Shall we walk for a bit?”

I followed Jin Wikyung to a secluded corner. He spoke first.

“How’s your condition?”

“It’s good.”

I’d gotten full use out of the level-up. My body had recovered at a terrifying speed, and distributing my points had made it even stronger.

The problem was something else.

*My Fame isn’t going up.*

No, it was going up. Really, by about a rat dropping. Little by little. Very, very little.

At this rate, I couldn’t guarantee I’d be able to log out before the fighting started.

*If it stayed like this, I mean.*

Jin Wikyung showing up now was convenient. I brought up what I’d been thinking for a while.

“I want to take on a mission.”

His eyes went round at how bluntly I’d come out with it.

“Hm? A mission?”

“Now that I’ve recovered, I want to distinguish myself for our family.”

I was proud of myself. To think I could deliver a line like that—a lie like that—with a straight face.

“I-is that truly what you think?”

“Yes.”

The corners of Jin Wikyung’s eyes trembled. He looked like a wave of emotion was running through his whole body.

*This is actually making me feel kind of guilty.*

The reason I was putting on this unconvincing act was Fame. If I went out on even a reconnaissance mission and distinguished myself, Fame would come in.

It would be even better if I ran into a reconnaissance unit from the Mount Heng Sword Sect. Not only would that be excellent EXP, I’d be able to fill all the Fame I had left.

*Once the real battle starts, it’s over.*

I had to log out, and fast, before then. I spoke in a voice full of resolve.

“Just leave it to me.”

“How could you have thought of something so admirable? Thank you, my youngest brother.”

Jin Wikyung wiped the damp corners of his eyes with his sleeve and went on.

“But no.”

“Then a reconnaissance mission for me, please?”

“I’ll take the sentiment. You guard the rear as you are now.”

*What is he talking about?*

I barely held down the urge to grab him by the collar and shake him.

“I-I really want to distinguish myself.”

“You’ve already done more than enough.”

“No, that’s not what I mean.”

“The merits you’ve earned so far have already been a great help to our family. So don’t trouble yourself over it.”

“I’d like you to give me even one reconnaissance mission. There could be enemies lying in ambush ahead…”

Jin Wikyung laughed softly.

“This is a battle with our family’s fate at stake. Do you think I wouldn’t have accounted for something like that?”

“Might there not be a one-in-ten-thousand chance we missed something?”

“That is, quite literally, one in ten thousand.”

*Damn it.*

Nothing was going my way. If I really failed to fill my Fame at this rate? Then I’d have to fight a large-scale battle with fifteen hundred people committed.

*I’m fucked.*

Something large and warm settled on my dejected shoulder. Jin Wikyung’s hand.

“Youngest.”

His voice was heavy and lonely. At the sudden change in mood, I kept quiet and listened.

“Your mission is graver than anyone else’s among us.”

“What’s my mission?”

After letting it hang for a long time, he forced out a single word.

“Survive.”

“Huh?”

“Survive however you can. If our family loses, run without looking back.”

“…”

“If the roots live, the tree will grow again. Second Brother and you could become better roots than I.”

I was speechless. For a long while, I could only stare at his face.

Survive. Become roots.

His voice and eyes hit home with more seriousness than ever before.

“That is your mission.”

The palm resting on my shoulder slid slowly down. I stared after Jin Wikyung’s departing back, unable to look away.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 36`.

# Master Edit Task — Chapter 44

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
| 이소군    | **Lee Seogeun**    |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 동기화              | **Synchronization** / **Sync** |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
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
| 나발이고 | slang | Dismissive rejection of the preceding concern (to hell with X), not a neutral “or not.” | |
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

#### Chapter 42 tail (verified mastered)

…
a flashlight.” “Yes.” I quickly set down my backpack. It was a porter’s bag Team Leader Choi had handed me just before we entered the Gate. It looked ordinary on the outside, but it was an expensive item enchanted with both space expansion and weight-reduction magic. “Here. A flashlight.” I handed it over since he’d asked, but in my experience it wasn’t the best method. Convenient, sure, but if the light vanished, you couldn’t adapt to the sudden dark. It was much better to wait a little and let your eyes get used to the darkness… Click. “Let there be light. Light.” Whoosh. A ball of light the size of a soccer ball shot out of the flashlight and slapped itself onto the cave ceiling. “…Magic?” “It’s built-in magic that activates as soon as you chant the spell. It lasts quite a long time, so three or four hours shouldn’t be a problem. It’s a limited edition I bought from Company M, but…” Im Kkeokjeong, who had been watching, boiled it down to one line. “It’s crazy expensive.” Was Team Leader Choi’s face darkening a little just my imagination, or was it the shadows? Either way, the raid had gotten a lot easier thanks to it. *Money really is the best.* The world was ruled by capital, and Gates were no different. People with money fought comfortably with magic equipment; people without it had to carry torches. “Take your positions.” Everyone responded immediately to Team Leader Choi’s command. Im Kkeokjeong and another E-rank Hunter took the lead as tanks, with Team Leader Choi behind them. I, the porter, and the two ranged dealers stood at the very back. “Move.” We started advancing slowly. The bright magic light lit the path ahead. “…” *I want one.* * * * “Kiiiieet!” The creatures crouching in the darkness emerged with shrill cries. Green skin. Short torsos. Hideous limbs. They were Hobgoblins, a higher species of ordinary goblin. *About thirty of them.* With only five people, this would be a hard fight. *But a C-rank Hunter changes the story.* On top of that, the other four were veteran E-rank Hunters with at least ten-odd years of experience each. I hung well back and watched the battle. “Ranged!” The moment Team Leader Choi gave the order, arrows flew. One shot, one kill. The arrows punched into vital points, and the unshielded Hobgoblins dropped in heaps. “Kiit!” “Oof, shield-bearers. What should we do?” “Hold.” Team Leader Choi went on. “Tanks, advance.” The tanks in thick full-body armor moved forward with their tower shields. Im Kkeokjeong and the other man were both huge, over 190 centimeters, so the intimidation factor was no joke. “Kiiiieet!” But monsters were called monsters for a reason. Trusting in their numbers, the Hobgoblins charged like a swarm of bees. But… “Well now.” Bam! Bam! Bam! They turned to bloody pulp against those big, beautiful tower shields and went flying. Riding that momentum, Im Kkeokjeong swung his mace like a flyswatter, wrecking limbs and smashing heads. “You punk! You punk!” …What was this, whack-a-mole? *Old-timers, as expected.* All four of them kept to their roles without overdoing it, steadily cutting the enemy numbers down. Knowing when to fall back and when to advance was combat intelligence born of plenty of experience. “Everyone, hold your positions.” And then one man. The man who had been directing the flow of battle until now moved. “I’ll handle the rest.” At the same time, a red line flashing along his armor plunged through the twenty Hobgoblins. Slash— A head soared into the air along a clean arc. It happened so quickly that the monsters couldn’t react. “Kiiie?” Slash. Slash. Slash. The blade never stopped. Merciless and efficient, it pierced and sliced through the monsters’ vital points. This was no longer a battle. It was a massacre. A massacre of some twenty monsters by a single human. *This is a C-rank Hunter.* I could see his speed, his strength. All of it. And I felt it. *He really is strong.* As a mere F-rank, I couldn’t even dream of matching him. He was a mid-rank Hunter three full stages above me. A wide river and a high wall that effort alone could never bridge. But at the same time, a question surfaced. *What if this were Murim?* Team Leader Choi was definitely strong. He had the ability befitting a C-rank Hunter, and plenty of experience. But if this were Murim… if he were a man of Murim… *I’d be stronger.* His movements were fast and powerful, but that was all. He hadn’t learned martial arts, and he couldn’t use mana efficiently either. At best, he was First Rate. In Murim, that was as far as he would go. *But this is reality.* I bit my lip without realizing it. A mid-rank Hunter and the lowest-rank Hunter. While the mid-rank Hunter wore expensive equipment and slaughtered monsters, the lowest-rank Hunter could only stare blankly. In the role of a porter. “Kiiieet…” The last Hobgoblin fell. Team Leader Choi pulled his sword from its chest, and our eyes met. “Mr. Taekyung. Please handle the byproducts.” “…” “Mr. Taekyung?” I wanted to tell him I was stronger than he was. But in the end, I couldn’t. Because this was my reality. “…Thank you for your hard work.” I *used to be* stronger than you. [^1]: Dongdaemun is Seoul’s major wholesale-market district.

#### Chapter 43 tail (verified mastered)

…
planning to order sushi by himself. *Is it really okay to be this relaxed?* Of course, I had no right to say that. Just portering and butchering in between had already earned me a day’s pay. Until I landed a job at a new Guild, if Team Leader Choi kept calling me, I wouldn’t have anything left to wish for. A sweet gig like this? I could do it a hundred times over. “Well, shall we head in?” “Yes.” At Team Leader Choi’s answer, Im Kkeokjeong slammed his tower shield into the stone gate. Boom! The gate blew apart, and powdered stone and dust poured down. I followed the others into the Boss Zone. And there… —Keuruk. It was there. *A shaman?* That was the first word that came to mind when I saw it. An old Hobgoblin in robes marked with unreadable patterns. A withered staff in one hand, a sharp dagger in the other. —Karruk. Chwi. Akto. Despite the loud crash when the stone gate broke, it went on muttering, unfazed. Each time a syllable ended, black energy rose from the corpses scattered around it. *Wait. Corpses?* I’d seen it right. Nearly a hundred Hobgoblins lay dead on the altar. Looking closer, they were the ones we were supposed to fight in the Boss Zone. *What the hell is this?* While all of us froze at a situation none of us had ever seen, Team Leader Choi shouted like a thunderclap. “Get outside. Now!” That was when the unknown old Hobgoblin turned its head. Clink. Its staff shook lightly. —Mita. Allo. The air shuddered. Magic was taking form. “Behind the shields!” The tanks hurriedly raised their tower shields. But that was the wrong call. What it had cast wasn’t an attack spell. Boom. Boom. Boom! “Behind us! The passage is being blocked!” “Run! Hurry!” *Damn it. Too late.* As if the clock had been turned back, the shattered stone gate stood intact again. And the changes didn’t stop there. The rubble on the floor stacked itself into double and triple walls, and vines from the cave walls bound them tight. “Everyone, out of the way!” It was Im Kkeokjeong. His muscles had swollen like they were about to burst—probably a Strength Enhancement Skill. Tower shield in hand, he charged the stone gate. “Haaah!” Bang! Crack! “…Goddamn it.” Im Kkeokjeong dropped the tower shield, his face blank with disbelief. An E-rank Hunter had even used a Skill and still hadn’t broken through. All he’d managed to do was wreck his shield. *Enhancement magic?* Whatever it was, one thing was certain. If it could wield magic like this, that old Hobgoblin had to be a monster at least one or two tiers higher. And… Swish! There was someone among us who could face it. *When did he—?* Team Leader Choi was already charging the thing, as if he’d been sure the passage wouldn’t break. “The wind takes hold. Haste.” His body slid forward. More than a hundred meters vanished in an instant. With five paces left, the sword came free from Team Leader Choi’s waist. Whoosh! A C-rank Hunter’s full-power attack. But the old Hobgoblin gave a nasty grin. —Karruk. Chwi. Akto. The change happened in an instant. Whoosh— The hundred-odd corpses scattered across the altar shriveled, then dispersed like sand. The black energy, fully pulled out of them, gathered into one mass and smashed into Team Leader Choi’s side. Thud! “Ghk.” Team Leader Choi bounced back fast. His face contorted as he said, “We have to stop it. Right now.” “…That?” It was already too late. Only a few seconds ago, it had been nothing more than energy given form. Now it was rapidly taking shape. A hulking frame nearly three meters tall. A monster with muscles ready to burst, holding a greatsword of terrifying size. “What the hell is that…?” Someone muttered in a dazed voice. Just like me, this had to be the first time they were seeing anything like it. Only Team Leader Choi knew what they were. “Hobgoblin Great Warrior. A C-rank Rare Monster.” The fact that something that size was a Hobgoblin was shocking enough, but it was nothing compared to what came next. *C-rank Rare Monster?* *Fuck, why is that thing showing up here?* Rare Monsters were uncommon monsters that appeared in a given Gate only at a low rate. And that Great Warrior was C-rank—something neither I nor the other team members would ever have run into in our lives. …Of course, not anymore. “You want us to fight that thing?” “Those things.” Team Leader Choi pointed at the old Hobgoblin. “Hobgoblin Priest. Also a C-rank Rare Monster.” “Ah, fuck…” The curse slipped out before I could stop it. Im Kkeokjeong asked with a grim expression, “What are our chances? Give it to me straight.” “If we take out the Priest first, there’s hope. In exchange…” Boom. Boom. Team Leader Choi’s words cut off. The Great Warrior was coming toward us. One step. Then another. The cave floor shook. “We need to hold that thing down for a little while.” *Who?* “Us?” “No. All of you.” “Kuwooooh!” The Great Warrior’s roar sent a stalactite falling from the cave ceiling. Team Leader Choi turned with a resolute look I’d never seen on him before. “The wind takes hold. Haste.” *Hey, you bastard.* [^1]: Gukbap is a Korean dish of soup served with rice.

## Korean source

```text
＃44화



“5분만 버티세요.”

한마디를 남긴 최 팀장은 바람처럼 달려 나갔다. 불행인지 다행인지, 홉 고블린 대전사는 최 팀장을 개미 눈곱만큼도 신경 쓰지 않았다.

“이쪽으로 오는데요.”

내 말에 사람들이 멍하니 고개를 끄덕였다.

“그러네.”

쿵쿵쿵!

“뛰어오는데요.”

“수비 대혀엉-!”

팀원들이 순식간에 대형을 갖춘다. 나도 창을 움켜쥐고 지시에 따라 움직였다. 탱커와 원거리 딜러들 사이. 딱 중앙이 내 위치다.

‘아니 시발, 난 짐꾼인데…….’

인생이 꼬여도 이따위로 꼬이나.

재수 없는 놈은 뒤로 넘어져도 코가 깨진다더니, 30만 원에 중급 레어 몬스터를 둘씩이나 만났다. 이건 코도 깨지고 뒤통수도 깨진 거다.

- 쿠워어어어!

홉 고블린 대전사는 포효와 함께 돌진했다. 3m에 달하는 신장, 근육질의 녹색 괴물은 그 자체만으로도 압도적이다.

‘대검은 왜 저렇게 커?’

저게 날 향해 휘둘러진다고 생각하니 저절로 침이 넘어간다.

“막을 수 있을까요?”

“버텨 봐야지.”

타워 실드를 바닥에 고정한 임꺽정이 소리쳤다.

“궁수! 마나 아끼지 말고 퍼부어!”

쉬쉬쉭!

동시에 마나를 머금은 화살들이 직사(直射)로 쏘아졌다. 어지간한 방패도 뚫어 버릴 만한 힘이었지만…….

투두둑.

홉 고블린 대전사가 가볍게 휘두른 대검에 죄다 반 토막이 나 버렸다. 설령 명중했어도 저 두꺼운 가죽을 뚫을 수 있을지 의문이다.

“급소 노려! 계속 쏘면서 속도 늦춰!”

그때 대전사의 눈이 붉게 달아올랐다. 마력을 끌어 올린 놈의 힘과 속도는 조금 전에 비할 바가 아니었다.

“쿠오오오오!”

쩌렁쩌렁한 고함과 함께 녹색 거구가 도약했다.

임꺽정이 비명처럼 외쳤다.

“산개!”

모두가 생각할 틈도 없이 몸을 날린 다음 순간.

쾅!

거대한 대검이 지면을 박살 냈다. 풍압과 함께 먼지가 토네이도처럼 주위를 휩쓸었다.

“크으.”

“콜록, 콜록.”

먼지의 장막 너머, 신음과 기침 소리가 터져 나왔다. 나는 몸을 바짝 수그린 채 생각했다.

‘뭐 저런 괴물이 다 있어.’

2년 전 ‘그놈’과 비교할 수는 없지만 등골이 오싹해지는 기분이다. 이런 싸움에 나 같은 F급 헌터는 짐짝밖에 안 된다.

‘이 틈에 최대한 멀리 떨어져야 해.’

온통 뿌옇게 물든 시야. 적아를 분간 못 하는 지금이 기회다.

나는 한껏 몸을 낮추고 천천히 움직였다. 한 손에는 창을, 다른 한 손으로는 허공을 더듬거리던 그때였다.

턱.

단단한 뭔가가 손끝에 닿았다. 매우 딱딱하고, 축축하다.

아마 동굴 벽인 듯싶었다.

‘벌써?’

꽤 멀리 떨어져 있었는데 의외로 가까웠던 모양이다.

아무튼 잘됐다. 이제 벽을 잡고 이동하면…….

물컹.

“……?”

이건 또 뭐야. 뭔가 기분 나쁘게 물컹거리는 물체를 조심스럽게 더듬어 갔다.

‘털도 있네. 사람인가?’

정신을 잃고 쓰러진 누군가의 머리일지도 모르겠다. 나는 한껏 숨죽여 속삭였다.

“꺽정 형님?”

대답은 없었다.

“누구세요?”

이번에는 대답이 들려왔다.

바로 위에서.

“크르르.”

때마침 어디선가 불어온 바람이 먼지를 걷어 냈다. 천천히 고개를 들자 번뜩이는 붉은 안광이 보인다.

“크륵.”

“…….”

다시 고개를 내렸다. 기둥처럼 굵고 돌처럼 단단한 놈의 허벅지 사이, 내 섬섬옥수가 뭔가를 움켜쥐고 있었다. 나는 나직이 신음했다.

“아, 시발…….”

그건 수컷의 본능이었다. 참을 수 없는 메스꺼움과 내 자신에 대한 혐오. 다음 순간 자연스럽게 손아귀에서 힘이 빠졌다.

스르륵.

힘없이 내려가는 내 손과 힘 있게 올라가는 대검이 보였다.

“크륵.”

“놨잖아! 놨는데 왜 그래!”

“쿠오오오오!”

이런 젠장.

나는 젖 먹던 힘까지 쥐어짜 뛰기 시작했다.



* * *



쾅! 쾅! 쾅!

홉 고블린 대전사는 완전히 돌아 버렸다. 그야말로 미친 듯이 나를 쫓아왔고, 대검으로 사방을 난도질했다.

스아악-

“으아아아!”

방금 건 진짜 위험했다. 순간적으로 바짝 숙인 머리 위로 스쳐 간 대검이 벽면을 작살냈다.

“태경아!”

“쏴!”

팀원들은 열심히 화살이며 투척 무기를 날렸지만…….

“크와아아악!”

이미 눈이 뒤집힌 대전사의 주의를 끌기에는 역부족이다.

나는 구르고, 또 구르며 한탄했다.

‘그냥 터트릴걸.’

이성보다 본능이 앞선 결과다. 1초라도 빨리 ‘그것’에서 손을 떼고 싶었던 남자의 마음.

쐐애액!

대검은 아슬아슬하게 빗겨 나갔다. 분명 위기의 연속이었지만 나는 C급 레어 몬스터를 상대로 한 번의 유효타도 허용하지 않고 있었다.

‘무림에서 워낙 험한 꼴을 많이 봐서 그런가.’

미친 소리일 수도 있지만 사실이다. 놈의 공격이 눈에 보인다. 반 박자 빠른 움직임이 내 목숨을 살리고 있었다.

쾅!

물론 저거 한 방 맞으면 골로 가겠지만.

“태경아, 이쪽으로!”

나는 소리가 들리는 곳으로 방향을 틀었다. 그곳에는 다시 수비 대형을 갖춘 팀원들이 기다리고 있었다.

“뒤로 빠져!”

임꺽정이 나를 쫓아오는 대전사를 향해 차징(Charging)을 시도했다. 타워 실드에 덧씌워진 푸른 마나에는 어지간한 하급 몬스터는 박살 내 버릴 파괴력이 깃들었다.

“하압!”

짧은 기합성과 함께 임꺽정이 나를 스치듯 지나간다. 그리고 다음 순간.

우직. 쿵-

뭔가 부서지는 소리와 함께 빠른 속도로 튕겨 나왔다.

십여 미터를 날아가 벽면에 처박힌 임꺽정이 왈칵 피를 토한다.

“쿠웨엑.”

“…….”

이거 실화냐.

황당해하는 나와는 달리 다른 팀원들은 비장했다.

“안 돼! 꺽정 형님!”

“우리가 시간 끌 테니까 형님 데리고 피해!”

그때 대검이 또 다른 탱커를 타워 실드 채로 날려 버렸다.

쿵!

“으악!”

“종민아!”

“우리가 시간 끌 테니까 종민이랑 형님 데리고 피해!”

퍽!

“으아아!”

“석호야!”

“…….”

빡!

팀원들의 전멸을 알리는 소리였다. 단검을 들고 덤벼들었다가 꿀밤을 맞고 날아간 마지막 팀원은 꿈틀거리다가 혼절했다.

그나마 모두 숨은 붙어 있으니 천만다행이다.

- 크르르…….

방금 했던 말 취소. 나는 놈에게 시선을 고정한 채 외쳤다.

“팀장님!”

저 멀리 제단에서도 치열한 싸움이 계속되고 있었다.

폭음 너머로 지친 목소리가 들려왔다.

“왜요!”

“아직 멀었습니까? 5분 넘은 것 같은데요!”

콰콰쾅! 화르륵!

벼락이 치고 화염이 치솟는다. 최 팀장이 비명처럼 외쳤다.

“3분 더!”

모르는 사람이 보면 축구 심판인 줄 알겠네. 최 팀장의 당당한 추가 시간 선언에 나는 할 말을 잃었다.

- 카륵, 카르륵.

홉 고블린 대전사가 천천히 다가온다. 쭉 찢어진 입에는 잔혹한 미소가 걸려 있었다. 나는 놈의 걸음에 맞춰 슬금슬금 물러났다.

“그래, 들어와. 들어와.”

어쩔 수 없다. 지금까지 했던 것처럼 죽어라 뛰어다니며 시간을 끄는 수밖에.

- 크륵.

하지만 대전사는 내 생각대로 움직이지 않았다.

“어?”

툭 튀어나온 눈동자가 정신을 잃고 널브러진 팀원들을 향해 뒤룩뒤룩 굴러간다. 이거 어째 느낌이 안 좋은데.

“저거 설마.”

그 설마가 맞았다.

임꺽정을 향해 걸어가는 놈의 뒷모습에 가슴이 철렁 내려앉는다.

“야, 야 인마!”

돌아오는 건 완전한 무시뿐.

이렇게 되자 마음이 다급해진 건 내 쪽이었다.

‘이대로 두면 다 죽는다.’

어떻게든 시선을 끌어야 했다. 나는 주위에 널려 있는 돌 중 하나를 주워 놈의 머리를 향해 날렸다.

딱!

명중이다.

홉 고블린 대전사가 고개를 돌려 나를 노려본다.

“그래, 이리 오라고.”

- 크르르.

가느다랗게 뜬 눈이 나와 임꺽정을 번갈아 본다. 그러더니 이내 임꺽정을 향해 뛰기 시작했다.

쿵쿵쿵.

“이런 미친!”

이대로라면 임꺽정은 물론이고 다른 팀원들까지 전멸이다. 놈을 막을 수 있는 건 오직 나뿐이었다.

‘저놈을 막는다고? 내가?’

C급 레어 몬스터와의 일대일 승부라니.

절대 이길 수 없는 싸움이다. 하지만…….

‘아, 시발.’

나는 이미 놈을 향해 쇄도하고 있었다. 가망 없는 싸움일지라도 싸워야 할 때가 있다. 지금이 바로 그때다.

“야, 이 개새끼야!”

쐐애액-!

넓은 등을 향해 창을 내지른 그 순간.

- 쿠루룩.

기다렸다는 녹색 거체가 돌아섰다. 놈의 입가에 걸린 득의양양한 웃음. 수평으로 휘둘러진 대검이 빛살이 되어 옆구리를 향해 쏘아졌다.

‘이걸 노렸구나.’

머릿속이 하얗게 물든다. 저걸 내가 막을 수 있을까? 괜히 같잖은 죄책감과 영웅심에 잘못된 판단을 내린 건 아닐까?

그러나 주사위는 이미 던져졌다.

‘버텨야 해.’

목숨을 걸고 싸워야 할 때가 있다. 지금이 바로 그랬다.

‘제발!’

나는 이를 악물고 철창의 진로를 틀었다. 그와 동시에 대검이 철창을 후려쳤다.

구그긍-

굉음. 그리고 거대한 압력이 있었다. 대검은 철창과 함께 내 허리를 그대로 갈라 버렸…….

“……어?”

철창도, 허리도 멀쩡하다. 대검에 실린 힘에 의해 발이 살짝, 아주 살짝 밀린 게 전부였다.

“……?”

뭐야, 이거.

- 크, 크륵?

홉 고블린 대전사의 얼굴이 시뻘겋게 달아올랐다. 뒤로 당겨진 대검이 재차 철창 위를 후려친다. 나는 정신이 없는 와중에도 철창을 쥔 손에 힘을 주어 막았다.

쾅!

몸이 밀렸다.

한, 30cm 정도?

“……엥.”

- ……크륵.

홉 고블린 대전사와 내 시선이 공중에서 마주쳤다. 이거 어디선가 한 번 겪었던 일 같은데.

‘맞아. 이소군과의 비무. 그때 딱 이랬었지.’

레벨만 보고 쫄아서 죽는 줄 알았는데, 알고 보니 허접이었던 그 황당한 순간을 어떻게 잊을까.

‘근데 거긴 시스템 빨이 있었잖아.’

반면 여긴 현실이다. 나는 시스템이고 나발이고 아무것도 없는 F급 헌터고.

‘이게 도대체 어떻게 된 일…….’

띠링.

“어?”

나는 그대로 굳어 버렸다. 이 순간만큼은 아무것도 보이지도, 들리지도 않았다.

‘이럴 리가 없는데. 이건 진짜 말도 안 되는 건데.’

띠링.



- 동기화가 완료되었습니다.

- 모든 시스템이 전승(傳承)됩니다.



그런데 그것이 실제로 일어났습니다.

“허, 허허.”

실성한 사람처럼 웃음이 새어 나온다. 홉 고블린 대전사가 미친놈 보듯이 나를 쳐다봤다.



[Lv.45 홉 고블린 대전사]



그래, 그렇단 말이지.

“뭐가 어떻게 된 건진 모르겠지만.”

나는 놈을 향해 씩 웃어 주었다.

“넌 뒈졌어.”



* * *



그르륵.

주름진 손이 목을 움켜쥐었다. 하지만 폭포수처럼 흘러나오는 피를 막을 힘도, 혀끝에만 맴도는 주문을 뱉어 낼 시간도 늙은 고블린에게는 주어지지 않았다.

“애먹이는군.”

최 팀장의 한마디와 함께 홉 고블린 제사장의 눈동자에서 빛이 꺼졌다.

‘피곤하다.’

하지만 곧장 몸을 돌렸다. 아직 그에게는 할 일이 남아 있었다. C급 레어 몬스터를 상대하려면 얼마나 악전고투를 치러야 할지…….

서걱-

“크와아악!”

최 팀장은 헛것을 봤다고 생각했다. 바로 그 홉 고블린 대전사가 비명을 지르고 있다. 한쪽 팔이 잘려 나간 채 주춤주춤 물러나고 있었다.

‘도대체 누가?’

최 팀장은 도와야 한다는 사실도 잊은 채 싸움을 바라봤다. 귀신같은 몸놀림, 물 흐르듯 쏟아지는 창날이 녹색 거체를 난도질했다.

잠깐. 창이라고?

오늘 모인 이들 중 창을 쓰는 사람은 한 명밖에 없다.

‘짐꾼, 아니 진태경?’

맞다. 바로 그였다.

배낭을 메고 가죽을 벗기던 F급 헌터!

“지금 도대체…….”

최 팀장의 입이 천천히 벌어졌다.

“무슨 일이 벌어지고 있는 거야?”
```

## Current accepted English baseline

```markdown
# Chapter 44

“Just hold out for five minutes.”

With that, Team Leader Choi shot off like the wind. For better or worse, the Hobgoblin Great Warrior didn’t give him so much as a glance.

“He’s coming this way.”

At my words, everyone nodded blankly.

“He is.”

Boom, boom, boom!

“He’s running this way.”

“Defensive formation—!”

The team snapped into formation. I gripped my spear and moved as ordered. Between the tank and the ranged dealers. Dead center—that was my spot.

*No, for fuck’s sake. I’m a porter…*

Even if my life was going to go sideways, did it have to go this sideways?

They say an unlucky bastard can fall over backward and still break his nose. For 300,000 won, I’d run into two mid-grade Rare Monsters. This wasn’t just a broken nose. This was a broken nose and a cracked skull.

—Kuwaaaaah!

The Hobgoblin Great Warrior charged with a roar. Nearly three meters of muscle and green hide—overwhelming all by itself.

*Why is that greatsword so damn huge?*

The thought of that thing swinging at me made me swallow hard.

“Can we stop it?”

“We’ll have to try.”

Im Kkeokjeong planted his tower shield in the ground and shouted,

“Archers! Don’t hold back on mana! Pour it on!”

Swish, swish, swish!

Mana-charged arrows flew in a straight line. They had enough force to punch through most shields, but…

Thunk, thunk.

The Hobgoblin Great Warrior flicked its greatsword and chopped every one of them in half. Even if they’d hit, I doubted they could have pierced that hide.

“Aim for the vitals! Keep shooting and slow it down!”

Then the Great Warrior’s eyes burned red. Once it drew up its mana, its strength and speed were on a whole different level.

“Kuwooooooh!”

With a booming roar, the green giant launched into the air.

Im Kkeokjeong screamed,

“Scatter!”

Before anyone had time to think, they threw themselves aside.

Boom!

The greatsword smashed the ground to pieces. A blast of air sent dust whipping around us like a tornado.

“Ghh.”

“Cough, cough.”

Groans and coughing broke out beyond the curtain of dust. I crouched as low as I could and thought,

*What kind of monster is that?*

It couldn’t compare to *that guy* from two years ago, but a chill still ran down my spine. In a fight like this, an F-rank Hunter like me was nothing but baggage.

*I have to get as far away as I can while I have the chance.*

Everything was a wash of haze. Nobody could tell friend from foe. This was my opening.

I stayed low and moved slowly. Spear in one hand, the other feeling through empty air.

Then—

Tap.

My fingertips hit something solid. Very hard, and wet.

It had to be the cave wall.

*Already?*

I’d thought I was farther out, but I must have been closer than I expected.

Fine by me. If I followed the wall, I could—

Squish.

“…?”

What was this now? I carefully probed the unpleasantly squishy thing.

*There’s fur, too. A person?*

Maybe it was the head of someone who’d passed out. I held my breath and whispered,

“Kkeokjeong hyung?”

No answer.

“Who is it?”

This time, I got a reply.

Right above me.

“Grrr.”

A gust of wind swept through from somewhere and cleared the dust. I slowly looked up and saw a pair of gleaming red eyes.

“Grrk.”

“…”

I looked back down. Between thighs as thick as pillars and hard as stone, my dainty little hand was clamped around something.

I groaned under my breath.

“Ah, fuck…”

That was a male’s instinct. Unbearable nausea. Disgust at myself. The next moment, my grip went slack on its own.

Slide.

My hand dropped, limp—and the greatsword rose with force.

“Grrk.”

“I let go! I let go, so why are you doing this?!”

“Kuwooooooh!”

Goddammit.

I wrung out every last bit of strength I had and ran.

* * *

Boom! Boom! Boom!

The Hobgoblin Great Warrior had completely lost it. It chased me like a lunatic, hacking in every direction with its greatsword.

Whoosh—

“Aaaaah!”

That one was actually close. I ducked at the last second; the greatsword skimmed over my head and wrecked the cave wall.

“Taekyung!”

“Shoot!”

The team poured on arrows and throwing weapons, but…

“Kuwaaaaargh!”

It wasn’t enough to pull the Great Warrior’s attention. Its eyes had already rolled back.

I rolled, then rolled again, and cursed my luck.

*I should’ve just popped it.*

Instinct had beaten reason. A man’s need to get his hand off *that* even one second sooner.

Whoosh!

The greatsword barely missed. Crisis after crisis, and I still hadn’t let the C-rank Rare Monster land a single clean hit.

*Maybe it’s because I’ve seen so much hell in Murim.*

It sounded insane, but it was true. I could see the attacks. Moving half a beat ahead was what was keeping me alive.

Boom!

Of course, one hit from that thing and I’d be a goner.

“Taekyung, this way!”

I cut toward the voice. The team was waiting there in a defensive formation again.

“Fall back!”

Im Kkeokjeong charged the Great Warrior chasing me. Blue mana sheathed the tower shield, packed with enough force to smash most low-grade monsters to pieces.

“Hah!”

With a short shout, Im Kkeokjeong brushed past me. And then—

Crunch. Thud.

Something broke, and he shot backward at a vicious speed.

He flew a good ten meters, slammed into the wall, and vomited a gush of blood.

“Gweeehk.”

“…”

Was this for real?

I was stunned. The rest of the team, on the other hand, looked grimly determined.

“No! Kkeokjeong hyung!”

“We’ll buy time! Take hyung and get out!”

Then the greatsword sent another tank flying, tower shield and all.

Boom!

“Agh!”

“Jongmin!”

“We’ll buy time! Take Jongmin and hyung and get out!”

Thud!

“Aaargh!”

“Seokho!”

“…”

Smack!

That was the sound of the team wiping. The last member had charged in with a dagger, taken a knuckle to the skull, and gone flying. He twitched, then passed out.

At least they were all still breathing. Small mercies.

—Grrr…

Scratch that.

I kept my eyes on the monster and shouted,

“Team Leader!”

A brutal fight was still going on at the altar in the distance.

A tired voice came through the explosions.

“What?!”

“Are you still not done? It feels like it’s been more than five minutes!”

Boom! Boom! Fwoosh!

Lightning struck, and flames surged. Team Leader Choi screamed,

“Three more minutes!”

Anyone who didn’t know better might have taken him for a soccer referee. His bold call for extra time left me speechless.

—Karruk, karruk.

The Hobgoblin Great Warrior came on slowly. A cruel smile hung on its wide-slit mouth. I eased back in time with its steps.

“That’s right. Come on. Come on.”

No choice. Same as before: run like hell and stall.

—Grrk.

But the Great Warrior didn’t play along.

“Huh?”

Its bulging eyes rolled toward the teammates sprawled unconscious on the ground. I had a very bad feeling about this.

“Don’t tell me…”

That was exactly it.

My heart dropped as I watched its back heading for Im Kkeokjeong.

“Hey! Hey, you!”

All I got was being ignored completely.

Now I was the one in a panic.

*If I leave it like this, they’re all dead.*

I had to pull its eyes somehow. I grabbed a rock off the ground and threw it at the monster’s head.

Thwack!

Direct hit.

The Hobgoblin Great Warrior turned and glared at me.

“Yeah. Come here.”

—Grrr.

Its narrowed eyes flicked between me and Im Kkeokjeong. Then it started running at Im Kkeokjeong.

Boom, boom, boom!

“You crazy bastard!”

At this rate, Im Kkeokjeong and the rest of the team would all be wiped out. I was the only one who could stop it.

*Stop that thing? Me?*

A one-on-one against a C-rank Rare Monster.

A fight I could never win. But…

*Ah, fuck.*

I was already charging at it. Sometimes you have to fight even when there’s no chance.

This was one of those times.

“You son of a bitch!”

Whoosh—!

The instant I thrust my spear at its broad back—

—Kururuk.

The green giant turned like it had been waiting. A smug smile sat on its mouth. The greatsword swept in horizontally, a streak of light shooting for my side.

*That’s what you were after.*

My mind went white. Could I even block that? Had I made the wrong call out of some cheap guilt and heroics?

But the die was already cast.

*I have to hold.*

There are times you fight with your life on the line. This was one of them.

*Please!*

I clenched my teeth and turned the iron spear into its path. At the same time, the greatsword smashed into it.

Rrrrk—

A roar of impact. Then enormous pressure. The greatsword, iron spear and all, split straight through my waist—

“…Huh?”

The iron spear was fine. So was my waist. All that had happened was my feet had been pushed back a little. A very, very little.

“…?”

What was this?

—G-Grrk?

The Hobgoblin Great Warrior’s face flushed bright red. It pulled the greatsword back and smashed it down on the iron spear again. Even through the confusion, I tightened my grip and blocked.

Boom!

My body slid back.

Maybe thirty centimeters?

“…Uhh.”

—…Grrk.

The Hobgoblin Great Warrior’s eyes met mine in the air between us. I’d been through this somewhere before.

*That’s right. The duel with Lee Seogeun. It was exactly like this.*

I’d freaked out at his Level and thought I was dead, only to find out he was a total pushover. How was I supposed to forget a moment that absurd?

*But I had the System backing me there.*

This was reality. I was an F-rank Hunter with nothing. No System, not a damn thing.

*How is this even…*

Ding.

“Huh?”

I froze. For that instant, I couldn’t see or hear a thing.

*This can’t be. This is actually insane.*

Ding.

> **System**
>
> Synchronization complete.
>
> All systems are inherited.

And yet, it actually happened.

“Ha… hahaha.”

A laugh slipped out of me like I’d lost my mind. The Hobgoblin Great Warrior stared at me like I was the crazy one.

> **System**
>
> Lv. 45 Hobgoblin Great Warrior

Right. So that was how it was.

“I don’t know what the hell just happened…”

I grinned at the monster.

“But you’re fucking dead.”

* * *

Gurgle.

A wrinkled hand clutched at a throat. But the old goblin had neither the strength to stop the blood pouring out like a waterfall nor the time to spit out the spell still sitting on the tip of its tongue.

“What a nuisance.”

With that from Team Leader Choi, the light went out of the Hobgoblin Priest’s eyes.

*I’m tired.*

But he turned around at once. He still had work to do. A C-rank Rare Monster was going to be a brutal fight, so—

Slash—

“Kwaaaaargh!”

Team Leader Choi thought he was seeing things. That same Hobgoblin Great Warrior was screaming. One arm gone, it was staggering back.

*Who did that?*

He watched the fight, even forgetting he was supposed to help. Ghostlike movement. A spear-point pouring like water, carving the green giant to pieces.

Wait. A spear?

Of everyone here today, only one person used a spear.

*The porter—no, Jin Taekyung?*

That was him.

The F-rank Hunter who’d been hauling a backpack and skinning hides!

“What on earth…”

Team Leader Choi’s mouth slowly fell open.

“What’s going on?”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 44`.

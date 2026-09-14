# Master Edit Task — Chapter 40

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
| 진하연    | **Jin Hayeon**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무인     | **martial artist**                               | Default term                                          |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 게이트     | **Gate**              |
| 태원     | **Taiyuan**            |
| 성진호 | **Seong Jinho** |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
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

#### Chapter 38 tail (verified mastered)

…
away, somewhere no one can find me.* But Gwak Jun couldn’t set out in search of a second life. Just as he was about to turn, a savage voice cut in. “Stop right there. If you don’t want to die very painfully.” Jin Taekyung added, his voice a little milder, “If you answer well, I’ll kill you gently.” Gwak Jun’s face went white. * * * Crunch! “Ghk.” I knew that feeling. Two or three ribs had to have broken, and the wind would have been knocked clean out of him. He held up pretty well for a Level 40, but that was his limit. “I told you not to run.” “If I were him, I would’ve run too.” Covered in blood and dust, Hyuk Mujin stared at me like I was some kind of beast. “If you’re going to kill him gently, you might as well say you’ll coat your spearhead with Golden Sore Medicine[^1] and stab him.” “Want me to stab you?” “Now that I think about it, that’s true. A blade hurts less if it hits you gently, doesn’t it? You could die gently. Heh heh, heh heh heh.” I smacked him once on the back of the head, then hauled Gwak Jun to his feet. “Let’s try this again. Who are you?” Ptooey. I easily dodged the bloody phlegm. With a high Agility stat, you could even avoid spit flying at you from point-blank range. That was a useful life hack. Of course, I had a fitting life hack for Gwak Jun, too. For example: “If you get hit in the solar plexus while your ribs are broken, it hurts a lot.” Thump. “Gaaaaah!” “So? Your answer?” “T-Three Paths Sect.” As I raised my fist again, Gwak Jun shouted, “The Three Paths Sect! We really are the Three Paths Sect! I’m telling you the truth!” Hyuk Mujin frowned. “He’s lying. The Three Paths Sect was founded thirty years ago. In truth, it’s closer to a martial arts school than a sect. They’re highly respected for taking in wandering orphans and teaching them.” “So?” “Couldn’t these bastards have killed all the Three Paths Sect’s disciples and impersonated them?” “Fake? Puh-huh.” A deflating sound escaped Gwak Jun’s mouth. He was laughing. “You still don’t understand? The Three Paths Sect was established according to that person’s will. As if you could have guessed at a thirty-year grand plan. Heh heh.” “Thirty years?” It was an unimaginably long time. Only a handful of people could have lain low for that many years while plotting to seize Shanxi Province. Only one person came to mind. *The Head Elder?* What possible reason could he have? The Head Elder was the one who had pulled Jin Wikyung to his feet while he blamed himself in front of the children’s bodies. He was also the one who had halted every political maneuver and actively cooperated. Thanks to him, the Jin Family of Taiyuan had united and made it this far… *Wait.* My head spun. *Could it be?* “Hyuk Mujin. How many martial artists from the newly joined small and mid-sized sects are there?” “If you add the Three Paths Sect and Gunggwimun together, well over a hundred.”[^2] “And under the Head Elder?” “If you mean the Head Elder’s faction, probably close to half the main force… Ah!” Hyuk Mujin and the reconnaissance-squad members gaped as they grasped the situation. If my guess was right and the Head Elder was a traitor, everything fit. Helping Jin Wikyung had been nothing more than laying the groundwork for today. *To take everything in a single battle.* He had helped Jin Wikyung and united the family’s strength for this very day. Suddenly I remembered what Gwak Jun had said before the fight. That one line about Shanxi’s master changing. It no longer sounded like nonsense. *The main force is in danger.* I had to tell Jin Wikyung. “We’re moving out. Right now!” I shouted and was about to turn. “Already too late.” Gwak Jun grinned, baring his bloodstained teeth. “Too late for me, too late for you bastards, and too late for the Jin Family of Taiyuan and the Mount Heng Sword Sect. The grand plan has already begun.” At the same time, blood gushed out. From his eyes, nose, and mouth—from every opening. Gwak Jun’s head slowly drooped. Hyuk Mujin spoke with a sickened look on his face. “He severed his own heart meridian.” Gwak Jun’s death meant one thing. Ding. Ding. Ding. > **System** > > — Defeated **Lv.40 Gwak Jun**! > > — **Slay the Assassins** (20/20) > > — Quest **Slay the Assassins** complete! > > — Level up! > > — Fame increases by 50! Quest complete, a level-up, and a Fame increase. After all those notifications, a single message appeared. > **System** > > — All conditions for **Logout** have been met. > > — Logging out in 3 seconds. 3, 2… Strength drained from my whole body. It felt as if I were floating. Hyuk Mujin, startled, caught me. “Squad Leader!” His voice crackled with static. My vision blurred, and my body slipped beyond my control. *Not now. Not like this…* *Of all times.* And then— > **System** > > — 1. Darkness crashed over me. [^1]: Golden Sore Medicine is a salve for blade wounds. [^2]: Gunggwimun is the name of another small sect newly allied with the Jin Family.

#### Chapter 39 tail (verified mastered)

…
he get out?* Jinho hyung sighed when he saw me standing there flustered. “What are you doing?” “Uh, uh?” “The power isn’t even on. What game were you playing?” What was that supposed to mean? “The power isn’t on?” “Move.” While I was still stammering, Jinho hyung came out the door, bent down under the capsule, and picked something up. “What does this look like to you?” A cord. An unplugged power cord. *Was I seeing things?* I scrubbed at my eyes furiously, but nothing changed. “Why is this…” “Taekyung. Jin Taekyung. You poor, pathetic soul.” Jinho hyung spoke with a distant look on his face. “Go to a mental hospital as soon as the sun comes up. I’m going back to my room.” He tossed the power cord aside and walked off. I stared blankly at his back. The power cord hadn’t even been plugged in. *Then what was the game I played?* I felt like I’d been bewitched by a ghost. Goose bumps rose all over my body. * * * I lay on the bed and thought. *Am I crazy?* I’d played a game for thirty days in a capsule that hadn’t even been plugged in. I could understand Jinho hyung’s reaction. But everything that had happened there… *It was all real.* Jin Wikyung, Wolhwa, Hyuk Mujin, and the Head Elder. I remembered every NPC’s face, the way they spoke, and how they acted. It hadn’t been a delusion I’d cooked up on my own. *Then what’s the problem?* There was only one answer. The problem was the game capsule built twenty-seven years ago—a piece of junk that should have been retired long ago and put in a museum. The date of manufacture was suspicious, too. January 1, 2020. The day the Demon King Asmodeus fell at humanity’s hands. *Who the hell would’ve been making capsules back then?* It was an era when hundreds of millions of people had died in the five-year Great War, and monsters had roamed downtown. In my opinion, the bastards who heard the breaking news that the Demon King had fallen and fired up a factory going, *All right, let’s make game capsules now!* belonged in court. *Back then, I thought it was a misprint.* I froze. *A misprint?* *The product manual!* How could I have forgotten something so important? What an idiot. I shot to my feet and started turning the room upside down. At last, I found a familiar little booklet under the bed. > **Product User Manual** > > **Product name:** Virtual Reality Access Device > **Model name:** Ark - 2020 > **Manufacturer:** H Soft > **Date of manufacture:** January 1, 2020 Then the next page. > **Precautions** > > - The player cannot log out at will. > > - If the player dies during play, resurrection is impossible. A month ago—no, three hours ago—I had thrown the booklet aside at this point. This time was different. With trembling hands, I turned to the final page. > **Key Features** > > - A custom capsule made for one person only! Once a user is registered, the capsule is permanently bound to that user until death. > > - Time-ratio adjustment for comfortable play! Upon login, time in reality passes very slowly. The reverse is also true. > > - Character Synchronization System! By synchronizing with their character, the user experiences a greater sense of unity. “What the hell is this?” My eyes could read the words, but my brain refused to process them. I started again from the beginning. *First, permanent binding.* It meant exactly what it said: it was mine until I died. Once I got some answers, I decided, I was going to smash that goddamn capsule to pieces. *Next, the time ratio.* That was the part I’d been most curious about. But instead of an exact figure, all it had was the vague phrase *passes very slowly*. It said the reverse was true as well, so time in the game had to be passing now too, however slowly. *Then is the war still going on?* Jin Wikyung came to mind. The Head Elder’s betrayal was already a given, and he would try to stab Wikyung in the back at the critical moment. Had Hyuk Mujin and the reconnaissance squad gotten that news to him? *Ah, that’s still a long way off. The time ratio has reversed.* More than that, I had my own crisis staring me in the face. I checked the last key feature. Unlike the ones before it, I couldn’t understand this no matter how many times I read it. *Synchronize with a character?* Just in case, I even looked it up in a Korean dictionary. It meant exactly what I thought it did. That only made it sound crazier. *How the hell do you synchronize with a game character?* I couldn’t make any sense of it. In the end, all I’d done was add another question. One thing was certain: I wasn’t crazy. I flopped onto the bed and read the front of the booklet again. “Manufacturer. H Soft.” In the end, every road led to the same place. If I investigated these bastards, something was bound to turn up. I searched the internet for H Soft, but aside from a porn studio with the same name, I couldn’t find a thing. “…” First, I needed to lock the door and think.

## Korean source

```text
＃40화



나는 하늘을 날고 있다. 거대한 날개를 펴고 바람을 갈랐다.

저 아래 보이는 높고 가파른 협곡. 호리병 형상을 띤 그곳에 인간들이 있었다. 그 수가 어림잡아 수백.

중심에 선 남자가 목청껏 외쳤다.

“태원진가를 위해 싸우지 마라!”

그때 땅이 진동했다. 나무가 흔들리고 산새가 날아오른다.

흘끗 뒤를 돌아보자 거대한 먼지구름이 협곡을 휩쓸며 다가오고 있었다.

“너희를 위해 싸워라! 적들에게 짓밟힐 혈육과 사랑하는 이를 위해 싸워라!”

검을 뽑아 든 그가 포효한다.

“무인답게 맞서라! 나도 그러할 것이다!”

수백 개의 병장기가 나란히 뽑혔다. 성큼성큼 걸어 나간 남자가 선두에 섰다. 협곡을 가로지르던 먼지구름이 흩어지고 무수한 인간들이 모습을 드러낸다.

- 와아아!

- 태원진가 놈들을 쓸어 버려라!

문득 남자가 고개를 들었다. 나를 발견한 그가 씩 웃었다.

“느낌이 좋군.”

남자의 얼굴을 본 순간, 날개에 힘이 스르륵 빠졌다. 나는 의식 깊은 곳으로 추락했다.



* * *



“어푸, 어푸어푸!”

필사적으로 날개를, 아니 팔을 퍼덕거리다가 깨달았다.

‘꿈이었구나.’

천만다행이다. 죽는 줄 알았네. 한숨 돌린 후에야 방 안의 상황이 눈에 들어왔다.



- 뉴스 속보입니다. 합정역 3번 출구에서 새로운 게이트가 출몰했습니다. 마력 측정 결과 C급 게이트로 판명 났으며…….



책상 위, 아나운서의 모습을 비추고 있는 소형 TV. 그리고.

“방금 뭐냐?”

진호 형이 있었다. 한 손에는 냄비 뚜껑. 다른 한 손에는 젓가락을 든 그가 어처구니가 없다는 표정으로 나를 바라본다.

“행위 예술 같은 건가.”

“닥쳐. 꿈꿨어.”

“헤엄치는 꿈?”

“떨어지는 꿈.”

“좋겠네. 키 크겠다.”

영혼 없는 말을 던지고 후루룩 면발을 빨아들이는 모습이 자연스럽다. 순간 여기가 내 방이 맞나, 헷갈릴 정도로.

“여기 내 방 맞지?”

“그럴걸.”

“근데 형이 왜 여기 있어?”

“하루 이틀이야?”

그럴듯한데? 순간 설득당할 뻔했다.

“TV나 좀 끄든가. 사람 자는데.”

“어떤 몰상식한 새끼는 목젖도 때리더라. 사람 자는데.”

“…….”

하여간 저 인간, 말빨 하나는 끝내준다.

“할 말 없으면 라면이나 먹어. 너 깰 것 같아서 다섯 개 끓였어.”

선견지명 보소. 젓가락을 받아 든 나는 감회에 젖었다.

이게 보통 라면인가. 한 달 만에 먹는 라면이다. 식욕을 당기는 냄새, 딱 알맞게 익은 면발과 따로 썰어 넣은 청양고추로 매콤하게 끓여진 국물.

‘미쳤다, 미쳤어.’

후루루룩.

정신이 들었을 때는 모든 게 끝난 후였다. 냄비 바닥까지 싹싹 핥아 먹고 있는 나를 진호 형이 멍하니 바라봤다.

“광고 찍는 줄 알았네. 태어나서 라면 처음 먹어 보냐?”

“돌아와서 처음 먹는 라면이니까.”

“또 그 소리냐?”

“한 달 동안 중국 음식만 먹다가 라면 먹어 봐. 미슐랭이 따로 없다.”

“그만해. 이제 재미없으니까.”

질렸다는 표정. 하지만 이번에는 나도 믿는 구석이 있다.

“이거나 보고 다시 얘기합시다.”

“뭔데 이게.”

“뭐긴. 제품 사용 설명서지.”

“……이거 설마.”

“어, 저 캡슐에 들어 있더라고. 읽어 봐.”

“20년도 더 지난 고물을 버리면서 이런 걸 넣어 둔다고?”

진호 형은 고개를 갸웃하더니 설명서를 읽기 시작했다. 그리고 몇 초 지나지 않아 고개를 들었다.

“이거 인쇄가 잘못됐네. 제조일이 2020년 1월 1일이야.”

나도 처음에는 그렇게 생각했다. 처음에는.

“그거, 인쇄 오류 아닐지도 몰라.”

“응?”

“아니, 이건 아직 짐작이니까 넘어가자. 다른 부분은 어때? 거기 적혀 있는 모델명이나 제조사, 형은 들어 봤어?”

전자 기기, 그중에서도 캡슐이라면 사족을 못 쓰는 그다.

관련 사이트에서도 이름만 대면 아는 네임드 유저에 IT 전문 블로그도 운영했었다고 했다.

하지만 즉각 튀어나온 대답은 기대를 와르르 무너트렸다.

“아니.”

하긴, 인터넷 검색으로도 나오지 않았으니 어떻게 보면 당연한 결과다. 하지만 약간의 실망감은 어쩔 수 없다.

“전혀 몰라? 형 이쪽 계통은 완전 빠삭하잖아.”

“그렇지. 근데 이건 모르겠다.”

진호 형이 머리를 긁적였다.

“불법 개조 캡슐? 아니면 커스텀인가? 솔직히 저런 디자인은 처음 보네.”

들을수록 암담하다.

“그래, 디자인은 뭐 그렇다 쳐. 근데, 내가 최초 모델부터 최신형까지 다 꿰고 있는 사람이거든? 국내에 한 번이라도 풀린 물건은 싹 다.”

“그런데?”

“여기 적힌 모델명. 제조사. 완전히 쌩 초면이야.”

“해외 쪽 제조사일 수도 있지 않나?”

“어이고. 이 화상아, 등신아, 머저리 같은 놈아.”

진호 형이 속 터진다는 얼굴로 설명서를 내밀었다.

“첫 줄 읽어 봐라.”

“제품 사용 설명서?”

“그래. 한글이라고, 한글!”

“아.”

“H 소프트가 국내 제조 업체건, 해외 제조 업체건 사용 설명서까지 한글로 만들 정도면 모를 수가 없지. 그 바닥에 캡슐 제조사가 수백, 수천 개도 아닌데.”

완전 바보가 된 기분이다. 내가 캡슐 관해서 뭐 아는 게 있어야지. 그때 진호 형이 말했다.

“잠깐 기다려 봐.”

스마트폰을 꺼내 화면을 두드리는 걸 보니 검색 중인 모양이다. 하지만 결과는 뻔했다.

“시발, 야동 사이트밖에 안 뜨네.”

어, 거기 괜찮더라.

“유령 회사도 아니고. 왜 아무것도 안 떠?”

“일단 뒷장도 읽어 봐.”

마지막 장까지 읽으면 정말 유령에 홀린 기분이 될걸. 진호 형은 심각한 얼굴로 설명서를 넘겼다.

한 번. 그리고 다시 한번.

“기가 막히지?”

“그러네. 기가 막히네.”

허탈한 음성이었다.

“백지를 보라고 하니까 기가 막히네.”

“어?”

“어쩐지 뭔 설명서가 이렇게 허술하나 했다. 캡슐 부품 설명도 없고, 실행 방법도 없고, 그나마 있는 모델명, 제조사, 제조일도 개판이고.”

“아니, 백지? 그게 무슨 소리야!”

“얼씨구. 문과충 자식 천연덕스러운 거 보소.”

황급히 설명서를 뺏어 읽었다. 잠들기 전 봤던 그 내용이 그대로 있다. 두 번째 페이지에는 주의 사항. 마지막 페이지에는 주요 기능.

“이게 안 보여?”

“그만해라. 무서워지려고 한다.”

저 표정. 말투. 진심이다. 내게 보이는 이 글씨가, 진호 형에게는 보이지 않는다.

아니, 어쩌면…….

‘이 내용은 나한테만 보인다.’

나는 한동안 그렇게 굳어 있었다.



* * *



푸쉭-

후들거리는 다리로 캡슐을 빠져나왔다. 반질거리는 외관, 흡사 거대한 달걀처럼 보이는 이 물건은 지난달에 출시된 최신형 캡슐이다.

“어, 금방 나오셨네. 제가 추천해 드린 게임 해 보셨어요?”

카운터에 앉아 있던 캡슐방 사장의 물음에 나는 반쯤 혼이 나간 채로 대답했다.

“네.”

사장이 권유한 가상현실 게임은 동시 접속자만 천만 명에 달한다는 메가 히트작. 엄청난 그래픽과 뛰어난 자유도로 시장 점유율 70%가 넘는다고 했다.

“그래픽 미쳤죠?”

게임에 접속. 그래픽을 보고 생각했다. 내가 미쳤나?

‘이게 가장 잘나가는 가상현실 게임이라고?’

그래픽 좋은 건 알겠다. 하지만 딱 거기까지였다.

NPC들의 외모와 움직임, 대화 패턴과 내 캐릭터로 느껴지는 오감(五感). 모두 부자연스럽다. ‘게임’이지만 결코 ‘현실’처럼 느껴지진 않는다.

“혹시 무협 배경 게임도 있나요?”

“아하, 무협 쪽 취향이시구나? 꽤 있긴 하죠. 찾으시는 게임 제목이 뭔데요?”

“무림이요.”

“무림 온라인?”

“아뇨. 오픈 월드 식 게임이에요. 혼자 플레이하는.”

“무협 게임 중에 그런 게 있어요?”

그럼 그렇지. 더 들어 볼 것도 없다. 비틀비틀 문을 나서는 내게 사장이 인사했다.

“또 오세요!”

안 올 거다. 두 번 다시.



* * *



희망 고시원.

낡고 녹슨 간판 아래에 앉아 스마트폰을 꺼냈다. 신호음이 가기 무섭게 상대방이 전화를 받았다.

딸깍.

- 어, 왜.

하나뿐인 웬수, 아니 여동생인 하연이다. 특유의 싸가지 없는 목소리를 듣는 순간 목이 꽉 막혔다.

- 여보세요?

“……어.”

- 왜 전화했어?

“그냥. 목소리 듣고 싶어서.”

순간, 죽음 같은 침묵이 흘렀다.

- 끊는다.

“아니, 잠깐만. 잠깐만!”

- 3초 준다. 용건.

망할 년…….

그래, 이래야 진하연이지. 덕분에 잠시나마 촉촉해졌던 눈물샘이 피라미드 인근 모래처럼 건조해졌다.

“엄마는 뭐 하셔?”

- 잠깐 볼일 있다고 외출. 궁금하면 전화해 봐.

일부러 하지 않았다. 이 녀석 목소리에도 울컥하는데 엄마 목소리를 들으면 어린아이처럼 엉엉 울 것 같아서.

나는 재빨리 말을 돌렸다.

“너는?”

- 수능 120일 남은 고삼이 뭐 하겠어. 공부하지.

평소보다 까칠한 말투. 수험생 스트레스가 상당한 모양이다.

“공부는 잘되고?”

- 이번에 7월 모의고사 망쳤어. 컨디션 조절 실패해서 쉬운 문제도 다 틀리고. 아, 생각할수록 짜증 나.

“괜찮아. 실전에서만 잘하면 되지. 몇 개나 틀렸는데?”

- 두 개.

“그 정도면 1등급이잖아. 다른 과목은?”

- 전 과목 두 개.

“응?”

- 한국사에서 하나. 수학에서 하나.

“……전 과목 통틀어서 두 개? 진심이냐?”

- 당연히 그거 말한 거지.

똑똑한 년…….

공부 잘하는 건 알고 있었는데 이 정도일 줄이야. 과거 내 학창 시절 성적을 생각해 보면 유전자 몰빵이라는 게 정말 존재하는 모양이다.

“공부 좀 한다?”

- 오빠 입장에서 보면 엄청 잘하는 거 아냐?

“무, 무슨 헛소리를! 나도 공부 꽤 했거든? 네가 초등학생 때라 기억을 못 하는 거…….”

- 지난주에 대청소하다가 오빠 성적표 나왔어. 7등급이 하도 많아서 무슨 잭팟 터진 슬롯머신인 줄.

“용돈 필요하지? 요즘 화장품은 얼마나 하냐?”

- 애잔하다. 진짜.

잔인한 년…….

통화는 10분이 넘도록 이어졌다. 나는 주로 듣는 쪽이었다. 공부, 학교, 관심 있는 남학생 이야기를 떠들어 대는 하연이의 목소리는 처음보다 한결 밝아져 있었다.

문득 묘한 감상에 젖어 들었다.

‘정말 돌아왔구나.’

나는 꿈을 꿨던 걸까, 아니면 망상에 빠져 있던 걸까.

현실에서는 고작 하루가 지났을 뿐인데 도저히 이해할 수 없는 불가사의한 일들이 일어났다.

하지만 이제는 이해하지 않기로 했다.

‘이제 현실로 돌아왔으니까.’

그리고 현실에서 살아야 하니까.

이곳에 가족이 있고 내가 있다. 그럼 그걸로 된 거다. 나는 아주 잠깐 이상한 꿈을 꾼 거다. 시간이 흐르면 자연스럽게 잊혀질, 그런 꿈.

- 그래서 내가…….

“응.”

조잘거리는 여동생의 목소리를 들으며, 나는 자리에서 일어났다. 낡고 녹슨 간판 아래를 벗어나 내 방으로 돌아가야 할 시간이었다.



* * *



지잉. 지이잉.

성진호는 부스스 눈을 떴다. 머리맡에 놓아둔 스마트폰이 울리고 있었다. 새벽 여섯 시. 오늘 하루를 시작하는 신호였다.

“어이고, 죽겠다.”

집을 나온 지 5년째. 아침마다 코끝을 파고드는 곰팡내가 퍽 익숙해졌다. 성진호는 반쯤 감긴 눈으로 담배와 라이터를 주머니에 쑤셔 넣고 방을 나섰다.

‘잠 깨는 데는 담배가 최고지.’

슬리퍼를 질질 끌며 옥상으로 올라간 그가 담배를 입에 물었을 때였다.

쿵.

“응?”

무슨 소리지? 의문과 함께 난간으로 고개를 내밀자 바로 앞 분리수거장에 놓인 쇳덩어리가 눈에 띄었다.

그리고 그걸 물끄러미 바라보는 덩치 좋은 청년도.

“야! 진태경!”

성진호의 외침에 진태경이 고개를 들었다.

“왜?”

“그거 버리게?”

쇳덩어리의 정체는 전날 주워 온 고물 캡슐이었다. 저걸로 되지 않는 장난이나 치더니 도로 갖다 버리려는 모양이었다.

‘그런 것치곤 너무 진지하긴 했는데…… 뭐, 헛소리지.’

성진호가 피식 웃었다.

“왜 버려. 무림 다시 안 가?”

“그걸 믿었어?”

진태경이 마주 웃었다. 하지만 오랫동안 그를 지켜봐 온 성진호가 보기에는 어쩐지 어색한 웃음이었다.

‘뭐지?’

묘한 느낌이다. 찝찝해하는 성진호에게 손을 흔들어 보인 진태경이 언덕을 내려가기 시작했다.

“어디 가, 인마! 이따 같이 아침 안 먹어?”

“일해야 돼!”

진태경은 뒤도 돌아보지 않고 떠났다. 성진호는 반쯤 타들어 간 담배를 한 모금 빨았다.

“새끼, 열심히 사네…….”

이윽고 진태경의 모습이 시야에서 사라졌다. 화분에 담배를 비벼 끄고 떠나려던 성진호의 눈에 고물 캡슐이 눈에 띈 것도 그때였다.

‘제조사가 H 소프트라고 했나?’

허접한 장난이겠지만, 알아봐서 나쁠 건 없겠지.
```

## Current accepted English baseline

```markdown
# Chapter 40

I was flying through the sky. Enormous wings spread, I cut through the wind.

Far below, a high, steep gorge came into view. Shaped like a bottle gourd, it held people—hundreds of them, at a rough count.

A man standing at the center shouted at the top of his lungs.

“Don’t fight for the Jin Family of Taiyuan!”

Then the ground shook. Trees trembled, and mountain birds took flight.

I glanced over my shoulder. A huge cloud of dust was sweeping through the gorge toward us.

“Fight for yourselves! Fight for the flesh and blood and loved ones who will be trampled by the enemy!”

He drew his sword and roared.

“Stand and face them like martial artists! I will do the same!”

Hundreds of weapons were drawn in unison. The man strode forward and took the lead. The cloud of dust crossing the gorge scattered, revealing countless people.

— Waaaaah!

— Wipe out those Jin Family bastards!

The man suddenly looked up. When he spotted me, he grinned.

“I’ve got a good feeling about this.”

The moment I saw his face, the strength drained from my wings. I plunged into the depths of consciousness.

* * *

“Pwah, pwah-pwah!”

I flailed desperately with my wings—or rather, my arms—before it hit me.

*It was a dream.*

Thank god. I thought I was a goner. Only after catching my breath did the situation in the room come into focus.

— This is a breaking news report. A new Gate has appeared at Exit 3 of Hapjeong Station. Mana measurements have confirmed it as a C-rank Gate, and…

A small TV sat on the desk, showing an announcer. And then there was—

“What the hell was that?”

Jinho hyung. He held a pot lid in one hand and chopsticks in the other, staring at me like I was out of my mind.

“Some kind of performance art?”

“Shut up. I was dreaming.”

“About swimming?”

“About falling.”

“Good for you. You’ll grow taller.”

He tossed out the line with zero soul and slurped up his noodles, looking completely at home. For a moment I wondered if this was even my room.

“This is my room, right?”

“Probably.”

“Then why are you here?”

“What, has it only been a day or two?”

That actually sounded plausible. I almost bought it.

“Turn the TV off or something. People are sleeping.”

“Some inconsiderate bastard even hits people in the uvula while they’re sleeping.”

“…”

Anyway, that bastard had one hell of a mouth on him.

“If you’ve got nothing to say, eat some ramen. I boiled five packs because I thought you might wake up.”

Talk about foresight. I took the chopsticks from him, a wave of feeling hitting me.

Was this ordinary ramen? This was ramen I was eating for the first time in a month.

The smell that pulled at my appetite. Noodles cooked just right. Broth boiled spicy with separately sliced Cheongyang peppers.

*Insane. This is insane.*

Slurp.

By the time I came to, it was all over. Jinho hyung stared blankly at me as I licked the pot clean.

“I thought you were filming a commercial. Have you never eaten ramen in your life?”

“It’s my first ramen since I came back.”

“Are you still on that?”

“Try eating nothing but Chinese food for a month, then have some ramen. Michelin’s got nothing on this.”

“Stop. It’s not funny anymore.”

He looked thoroughly fed up. But this time, I had something to back me up.

“Look this over, then we’ll talk again.”

“What is this?”

“What do you think? A product user manual.”

“…”

“Don’t tell me…”

“Yeah. It was inside that capsule. Read it.”

“You stuck this in a piece of junk more than twenty years old before throwing it away?”

Jinho hyung tilted his head, then started reading. A few seconds later, he looked up.

“This is a misprint. The date of manufacture is January 1, 2020.”

I’d thought the same thing at first. At first.

“That might not be a printing error.”

“Huh?”

“No, never mind—that’s still just a guess. What about the rest? The model name and manufacturer listed there. Have you heard of them?”

Jinho hyung was crazy about electronics, especially capsules.

On the related sites, he was a named user people recognized on sight. He’d even run an IT blog.

But the answer that came out immediately sent my expectations crashing down.

“No.”

Well, that was only natural. Even an internet search hadn’t turned anything up. Still, I couldn’t help feeling a little disappointed.

“You really don’t know? You know this field inside out.”

“Yeah. But I don’t know this.”

Jinho hyung scratched his head.

“An illegally modded capsule? Or a custom job? Honestly, I’ve never seen a design like that.”

The more he talked, the bleaker it got.

“Fine, I’ll grant you the design. But I know every model from the earliest ones to the latest. Everything that’s ever been released in Korea.”

“And?”

“The model name written here. The manufacturer. Complete strangers.”

“Couldn’t it be an overseas manufacturer?”

“Oh, you hopeless idiot. You dumbass. You moron.”

Jinho hyung thrust the manual at me, looking thoroughly exasperated.

“Read the first line.”

“Product User Manual?”

“Exactly. It’s in Korean. Korean!”

“Oh.”

“Whether H Soft is a domestic manufacturer or an overseas one, if they went as far as making the user manual in Korean, there’s no way I wouldn’t know them. It’s not like there are hundreds or thousands of capsule manufacturers in this business.”

I felt like a complete idiot. Not that I knew anything about capsules. That was when Jinho hyung spoke up.

“Wait a second.”

He pulled out his smartphone and started tapping the screen. Searching, from the looks of it. But the result was obvious.

“Fuck. All that comes up is porn sites.”

*Yeah, that one was pretty good.*

“It’s not even a ghost company. Why isn’t anything coming up?”

“Read the rest of it, too.”

By the time he reached the last page, he’d really feel like he’d been haunted. Jinho hyung turned the pages with a serious expression.

Once.

Then once more.

“Isn’t it incredible?”

“Yeah. Incredible.”

His voice was hollow.

“You told me to look at blank pages. That’s incredible.”

“Huh?”

“No wonder I thought this manual was so slapdash. No explanation of the capsule’s parts, no operating instructions, and even the model name, manufacturer, and date of manufacture are a mess.”

“Blank pages? What are you talking about?”

“Well, well. Look at this humanities-major bastard, acting all innocent.”

I snatched the manual and read it in a hurry. The contents I’d seen before falling asleep were still there. Precautions on the second page. Key features on the last.

“You can’t see this?”

“Cut it out. This is starting to get scary.”

That look. That tone. He meant it. The writing I could see was invisible to Jinho hyung.

Or maybe…

*Only I can see this.*

I stayed frozen like that for a long while.

* * *

Pshhh—

I climbed out of the capsule on shaky legs. Glossy exterior, shaped like a giant egg—this was the latest model, released only last month.

“Oh, you’re out already. Did you try the game I recommended?”

Still half out of my mind, I answered the capsule café owner at the counter.

“Yes.”

The virtual-reality game he’d recommended was a megahit with ten million concurrent users. Incredible graphics, outstanding freedom, over seventy percent of the market, he’d said.

“The graphics are insane, right?”

I logged in. I looked at the graphics and thought:

*Am I the one who’s insane?*

*This is the most popular virtual-reality game there is?*

The graphics were good. I could give it that. But that was as far as it went.

The NPCs’ faces and movements, their dialogue patterns, the five senses I felt through my character—all of it was unnatural. It was a *game*, but it never felt like *reality*.

“Do you have any games set in wuxia?”

“Ah, so you’re into wuxia? There are quite a few. What’s the title you’re looking for?”

“Murim.”

“Murim Online?”

“No. It’s an open-world game. One you play alone.”

“Are there games like that in the wuxia genre?”

Figures. There was nothing more to hear. I staggered out the door, and the owner called after me.

“Come again!”

I wouldn’t.

Not ever again.

* * *

Hope Goshiwon.

I sat beneath the old, rusted sign and pulled out my smartphone. The other end picked up almost before it could ring.

Click.

“Yeah. Why?”

My one and only nemesis—no, my younger sister, Hayeon. The moment I heard that uniquely bratty voice of hers, my throat closed up.

“Hello?”

“…Yeah.”

“Why’d you call?”

“Just. I wanted to hear your voice.”

A deathly silence followed.

“I’m hanging up.”

“No, wait. Wait!”

“Three seconds. What’s your business.”

*That damn girl…*

Right. This was Jin Hayeon. Thanks to her, the tear ducts that had gotten a little moist dried out like sand around the pyramids.

“What’s Mom doing?”

“She went out. Said she had an errand. Call her if you’re curious.”

I didn’t. On purpose. Even this brat’s voice was enough to choke me up. If I heard Mom’s, I’d bawl like a little kid.

I quickly changed the subject.

“What about you?”

“What’s a high-school senior with a hundred and twenty days left until the college entrance exam supposed to do? Study.”

Her tone was sharper than usual. Exam stress must have been hitting her hard.

“How’s studying going?”

“I bombed the July mock exam. I didn’t manage my condition right and missed even the easy questions. God, the more I think about it, the more annoyed I get.”

“It’s fine. Just do well on the real thing. How many did you miss?”

“Two.”

“That’s still Grade 1.[^1] What about the other subjects?”

“Two across all subjects.”

“Huh?”

“One in Korean history and one in math.”

“…Two in total, across every subject? Are you serious?”

“Obviously that’s what I meant.”

*Smart little brat…*

I knew she was good at studying, but I hadn’t realized she was this good. Thinking back on my own school grades, it really seemed like there was such a thing as dumping all the genes into one kid.

“You study pretty well, huh?”

“From an older brother’s standpoint, isn’t it amazing?”

“W-what kind of nonsense is that? I studied pretty well too, you know? You just don’t remember because you were in elementary school…”

“Last week during a deep clean, I found your report card. There were so many Grade 7s I thought it was a slot machine that had hit the jackpot.”

“You need some allowance, right? How much do cosmetics cost these days?”

“That’s pathetic. Seriously.”

*Cruel girl…*

The call lasted more than ten minutes. I did most of the listening. Hayeon rattled on about studying, school, and a boy she was interested in, and her voice was much brighter than it had been at first.

I found myself getting oddly sentimental.

*I really did come back.*

Had I been dreaming? Or lost in a delusion?

Only a day had passed in reality, yet utterly incomprehensible, inexplicable things had happened.

But I decided not to try to understand them anymore.

*I’m back in reality now.*

And I had to live in reality.

My family was here. I was here. That was enough. I had simply dreamed a strange dream for a little while. The kind of dream that would fade on its own with time.

“So I…”

“Yeah.”

Listening to my little sister chatter, I stood up. It was time to leave the old, rusted sign behind and go back to my room.

* * *

Bzzzt. Bzzzt.

Seong Jinho cracked his bleary eyes open. The smartphone by his pillow was ringing.

Six in the morning. The signal that started the day.

“Oh, I’m dying.”

It had been five years since he left home. The moldy smell that crept into his nose every morning had gotten pretty familiar. Eyes half shut, Seong Jinho shoved his cigarettes and lighter into his pocket and left the room.

*Nothing wakes you up like a cigarette.*

He shuffled up to the rooftop in his slippers. He’d just put a cigarette between his lips when—

Thud.

“Huh?”

What was that? Wondering, he leaned over the railing, and a hunk of metal sitting in the recycling area right in front of him caught his eye.

So did the well-built young man gazing at it.

“Hey! Jin Taekyung!”

At Seong Jinho’s shout, Jin Taekyung looked up.

“What?”

“You throwing that away?”

The hunk of metal was the junk capsule Taekyung had picked up the day before. After pulling some failed prank with it, he seemed to be taking it back out to throw away.

*He’d been awfully serious for a prank like that… Ah, whatever. It was nonsense.*

Seong Jinho gave a short laugh.

“Why throw it away? Not going back to Murim?”

“You believed that?”

Jin Taekyung smiled back. But to Seong Jinho, who had watched him for a long time, the smile looked somehow awkward.

*What’s with him?*

Something felt off. As Seong Jinho stood there uneasily, Jin Taekyung waved and started down the hill.

“Where are you going, you punk? Aren’t we eating breakfast together later?”

“I have to work!”

Jin Taekyung left without looking back. Seong Jinho took a drag from his half-burned cigarette.

“That bastard’s really working hard…”

Soon, Jin Taekyung disappeared from sight. Seong Jinho stubbed out his cigarette in a flowerpot and was about to leave when the junk capsule caught his eye.

*He said the manufacturer was H Soft, right?*

It was probably just some half-assed prank, but there was no harm in looking into it.

[^1]: Korean mock exams use a 1–9 scale; Grade 1 is the highest.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 40`.

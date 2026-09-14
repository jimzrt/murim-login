# Master Edit Task — Chapter 379

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

## Chapter 374 Expedition

- This branch backfills Chapters 370–373 against the Chapter 65 anchor. Chapters 66–369 have no accepted local English translation here.
- Treat `docs/EXPEDITION_SEED.md` as bounded orientation, not as a substitute for missing translations. Do not read parked Chapters 374–375 while drafting 370–373.
- When the current Korean source conflicts with bridge context, the current source wins. Preserve uncertainty instead of inventing skipped-range backstory.
- After Chapter 373 is committed, run `python tools/expedition.py resume-parked` so the existing 374–375 translations remain the accepted line.

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

| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 귀가      | **your family**                                                 |
| 류인친 | **Ryu Inchin** | Named combatant of the Public Security Armed Forces; exact relationship to the person calling him hyung is unresolved. |
| 야오위 | **Yao Wei** | A-rank Hunter, Shao Shen's friend and comrade. |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 중화인민공화국 | **People's Republic of China** | Country whose flag appears on Shao Shen's armor. |
| 중화 | **Zhonghua** | Term used in Shao Shen's rallying cry for China. |
| 오성홍기 | **Five-Star Red Flag** | National flag of the People's Republic of China. |
| 듀라한 | **Dullahan** | Higher undead monster form taken by Yao Wei. |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 호승심 | polysemy | Competitive pride or fighting spirit; not merely a desire to test oneself. | test myself |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 370–374

## Plot

Chapter 370 is intentionally skipped; no accepted English translation or plot details are asserted.

In Chapter 371, Taekyung is celebrated as the Flame Divine Dragon after reaching the Supreme Peak realm. The Qingcheng and Emei Sect Leaders ask him and Jeok Cheongang to investigate a strange Dark Heaven-related formation identified by Samgoe. Taekyung encounters Mungyeong and learns that the physician is secretly the Slaughter Saint.

The group enters a cave hidden by a phantom formation in Chapter 372. It contains supplies, weapons, and a huge inactive transport formation apparently capable of moving people over great distances. Its patterns are not writing, and its origin and purpose remain unclear. Slaughter Saint suggests Dark Heaven succeeded the Demonic Cult, while Taekyung senses something familiar about the formation.

Slaughter Saint decides to resume living as Mungyeong. Back at the Sichuan Tang Clan, Taekyung processes accumulated System messages, reaches Level 120, and discovers that the previously unnamed Inventory item is bound to him and summonable in either world. An investigative party from Henan arrives.

In Chapter 374, Jin Wikyung urges acting Family Head Tang Horyong to relocate the devastated Sichuan Tang Clan to Henan, Shaanxi, or Shanxi, promising orthodox Murim support as a larger war approaches. Horyong does not decide. Wikyung prepares to escort Samgoe to Henan, but Tang Sadok awakens after his long coma, delaying their departure. Taekyung identifies the bound item as the Myriad Poison Ring and expects to return to his original world soon.

## Continuity

- Chapter 370 remains a source-only gap; later references across it must be checked against the current Korean source.
- Taekyung is at the Supreme Peak realm and Level 120. His exact Fame, titles, martial-art stages, and unassigned points after the skipped range are not established here.
- Slaughter Saint is secretly living as Mungyeong and intends to leave Murim after intervening in the crisis.
- The inactive Dark Heaven-associated transport formation remains unexplained. Its origin, destination, mechanism, and connection to Dark Heaven are unresolved.
- Dark Heaven’s agents, larger purpose, and connection to the Demonic Cult remain unresolved.
- The Sichuan Tang Clan, Qingcheng Sect, and Emei Sect were devastated by Dark Heaven. Tang Horyong remains acting Family Head; Tang Sadok, the Poison King, has awakened.
- Jin Wikyung is the Lesser Family Head of the Jin Family of Taiyuan, leader of unified Shanxi Murim, and the assigned escort for Samgoe. He has offered the Tang Clan relocation and orthodox support.
- Orthodox Murim is preparing a new Murim Alliance after Mae Jonghak’s warning of a war greater than the Great Faction War.
- Samgoe remains under guard and is being taken toward Henan; the escort’s outcome and timing are unresolved.
- The Sichuan Tang Clan’s relocation decision and destination are unresolved.
- Taekyung’s return to his original world is imminent; roughly six hours have passed there while about two months passed in Murim.
- The previously unnamed bound Inventory item is the Myriad Poison Ring.
- The outcome of Taekyung’s spar with Jin Mukyung remains unresolved in the accepted earlier anchor.

## Translation Decisions

- Preserve **Flame Divine Dragon**, **Supreme Peak**, **Dark Heaven**, **Slaughter Saint**, **Mungyeong**, **Myriad Poison Ring**, **Sichuan Tang Clan**, **Qingcheng Sect**, **Emei Sect**, **Henan**, **Shaanxi**, and **Shanxi**.
- Preserve uncertainty around the transport formation; do not treat its patterns as writing or assert an origin, destination, or confirmed mechanism beyond its apparent transport function.
- Render **반 시진** and **한 시진** as **half a shichen** and **one shichen**, with a footnote explaining that a shichen is a traditional two-hour period.
- Render **종형** as **older cousin** in the Tang family context.
- Treat Chapters 371–373 as source-only bridge summaries, not complete accepted English translations.

### Prior accepted reading-copy tails

#### Chapter 377 tail (verified mastered)

…
ownership became bound to a new owner. Once given a name, it can be used freely anywhere. *Its ownership became bound because the previous owner died?* I had suspected as much, but it seemed this really was what I thought it was. After turning my inventory upside down, I finally found the new bound item. A flat, deflated sound escaped my lips. “…Eh?” The object resting on my palm was nothing more than a tiny fragment. It had originally been called Black Dragon Armor. *I definitely blew it away along with that bastard, the Western Heaven Demon Lord, in the final slash. Did it automatically enter my inventory because it was a bound item?* The sight of the Black Dragon Armor shattering into pieces was still vivid before my eyes. But what was I supposed to do with a fragment this small? *I guess I’d feel incredibly secure if I tucked it into the front of my underwear.* Ah. Maybe that was why it was classified as armor. I was tugging at the front of my pants and inspecting a suitable position when— “What are you doing th—” “…Ah.” A chilly silence descended in an instant. The boy’s face stiffened at the sight of my loosened waistband and the hand thrust inside it. After making sure no one else was nearby, the Slaughter Saint—no, Mungyeong—spoke. “Why here, of all places?” “Wait a second. I think there’s been a misunderstanding.” Just as I hurriedly began to make excuses, Mungyeong’s gaze turned cold. “I told you when we departed. In front of anyone other than the Fire King and Cheongpung, you are to treat me as Mungyeong.” I answered with an aggrieved expression. “You’re speaking casually to me right now too, you bastard.” “…!” “Oh. Sorry.” A multitude of emotions crossed Mungyeong’s face. He glanced sideways at the approaching river bandits and clicked his tongue. The terrifying Slaughter Saint transformed into the Divine Physician’s Disciple—a cheerful young physician-in-training—in an instant. “What were you doing, sir?” “What business is it of yours?” “…!” *This is surprisingly fun. But I can’t do it a third time.* I quickly held out my hand toward the speechless Mungyeong. “This got into the front of my pants.” That was slightly at odds with the truth, of course, but Mungyeong did not care about such details. More precisely, his eyes were fixed on the fragment of the Black Dragon Armor. “This is…” “Do you happen to know this? No—do you know it?” “Where did you get it?” “From that bastard.” Mungyeong understood that I meant the Western Heaven Demon Lord and nodded. “You obtained a divine weapon. Though I do not know how only a fragment remained.” “He called it Black Dragon Armor.” “Black Dragon Armor?” “Why? Is that different from the name you knew?” “I once read about it in an old secret history. A mysterious suit of armor with no fixed name, said to change its form and properties according to its owner.” “It changes its form and properties? How?” Mungyeong answered with a look that said I was hopeless. Only then did I realize what I needed to do next. *Internal energy.* Internal energy was the very form and nature possessed by its owner. Sssaaaaah. Following the formula of the Blazing Flame Divine Art, which had reached its eighth stage, I poured magma-like qi into the fragment of Black Dragon Armor. The ink-dark energy swirling over its surface vanished, and bluish-white Scorching Yang Qi filled the void. Engraved with patterns that seemed to blaze like flames, it was no longer something that could be called Black Dragon Armor. *Flame Dragon Armor.* The name was simple, but nothing could have suited it better. The instant I smiled in satisfaction, a bright chime rang out. > **System** > > You have given the bound item ??? a new name! > > From now on, you can freely use Flame Dragon Armor anywhere! > > Flame Dragon Armor is resonating with your qi! It requires its owner’s power to repair its damaged sections by itself! Whoooosh. I could feel it—a massive amount of internal energy rushing out of my body and into the Flame Dragon Armor. The fragment absorbed it like a sponge. Pretending to tuck it into my robes, I stored it in my inventory instead. *Automatic repairs? That’s incredible.* I had certainly obtained something useful. Thank goodness the final gift of this journey was the Flame Dragon Armor. As I turned away, Mungyeong stared at me with wide eyes. “Where are you go—going, sir?” “What business is it of yours?” “…!” This was strangely addictive. I waved to Mungyeong, who was probably repeating the character for *patience* to himself. “I’m going to get some sleep. Don’t wake me.” “…?” Yes. It was time to wake from a long sleep. But… *Why do I feel so uneasy? Did I forget something?* Tilting my head, I found a place in the fast ship’s cabin and lay down. I closed my eyes, took a deep breath, and called out the command. *Logout.* A chime rang out. > **System** > > Logging out in 10 seconds. Ten, nine, eight, seven… With the final count, the sound of splashing and someone’s cries faintly pierced my ears from somewhere. Splash! Gasp! Squad Leader, save me—gasp! [^1]: A sikgyeong was the time required to eat a meal, conventionally treated as roughly thirty minutes.

#### Chapter 378 tail (verified mastered)

…
was so shocked that he poked his head out and stared at me as if I were insane. “Of course not! The pressure-sealing system won’t even let you open it, and the aircraft will be damaged because it can’t withstand the pressure difference! We won’t be able to breathe properly, either!” Team Leader Choi, fiddling with the ring on his finger, cut in. “I think I can block the pressure. I don’t know what you have in mind, but go ahead and try.” “Okay.” “Don’t! You *bangzi* bastards![^1] Are you trying to kill us all?” “…What did you just call us?” The nerve of him, insulting Koreans right in front of a proud Korean kimchi man like me! The captain realized what had slipped out, and his face turned white. “No, that’s not what I meant.” “You fucking Chink bastard. Damn it.” “…!” “Hey, Captain!” “Y-Yes?” “I’m opening it.” “Ah! Ahhh!” Before the captain could stop me, I opened the door. No—I cut it open. Shhk! Sword qi—the force called an Aura Blade in the modern world—sliced through the sturdy alloy and created a small door. It was the tremendous power wielded by Supreme Peak masters in Murim and, in this world, only by S-rank Hunters. Team Leader Choi’s eyes widened in shock. “Mr. Jin Taekyung, this is—” “Team Leader!” Whoooosh! This was no time to be surprised. The tremendous wind and pressure were making the aircraft lurch, turning the cabin into a complete mess. The screams and my shout snapped Team Leader Choi back to his senses. He rubbed his ring. “An airtight barrier surrounds us. Barrier!” “Oh.” With the incantation, a transparent membrane of energy sealed the new opening without leaving the slightest gap. So there was a way to do this. With a brief exclamation of admiration, I stuck my upper body out of the cabin. Team Leader Choi’s barrier recognized me as an ally and let me pass through without resistance. Rrrrrumble! The wind pressure slammed into my upper body as if trying to crush me to death. I grinned. *This is no joke.* But it wasn’t unbearable. Actually, it would have been strange if I couldn’t withstand it. Compared to the waves of qi the Western Heaven Demon Lord had emitted, this was no more than a gentle spring breeze. - Kyaaaauuu! The monster’s sharp cry mixed into that spring breeze. The flock of wyverns had already drawn close enough for me to judge the distance. *About a hundred meters. I’ve never tried this before, but… at this distance, it should be enough.* *Open Inventory. Equip.* Ssswish. A spear I had bought at a discount from the Hunter Market appeared in my hand. Like a javelin thrower, I drew my shoulder all the way back. From my waist to my wrist, every muscle and tendon I needed pulled taut like a bowstring. - Kyaau! The lead wyvern—their chief—sensed something was wrong and threw back its head with a shriek. I could see a pure-white current of air being sucked toward its snout. *That’s…* - Breath! It’s Breath! Dodge it, you vile human! The Skeleton Warlord was right. Of all the countless monsters, Breath was a power granted only to the dragonkin. I could clearly see it taking shape inside the wyvern’s gaping maw. Whooooom. A massive sphere of wind. The Air Breath, powerful enough to shred metal like paper, finished taking shape. “Hey, wyvern!” - Kya? “I’m putting it in!” I shouted like a thunderbolt and whipped my drawn-back shoulder forward. Fwoom—whooosh! Fiery concentrated qi sheathed the spearhead, burning through the air and cleaving the wind. The wyvern’s bright yellow eyes widened at the blue-white streak of light shooting straight toward it. - Kiiiiiik! Whoooom! Compressed air burst from the tip of the spear. A cloud of white. And then— Thwack! Boom-boom! A massive body plummeted toward the ground like a kite with its string cut. * * * - Kyaau? - Kiiit? Around a dozen pairs of bright yellow eyes stared at one another. Wyverns were ferocious creatures from the moment they were born, but at this moment, they were utterly bewildered and had no idea what to do. - Kikikit? - Kiiik… *What? Is the boss dead?* *Looks that way…* After exchanging words in their own language, the wyverns were dumbfounded. Their leader was exceptionally powerful even among their own kind—so powerful that he was known as the “Black Star.” And now, the Black Star had become a black speck falling toward the impossibly distant ground. - Kiririk? - Grrrrr. None of them had even properly seen how he died. They could only guess that the tiny human had thrown a spear and hit him. But that was impossible. How could a mere human dare lay a hand on a descendant of the great dragons… “Hey, green wyvern over there!” - Kiiik? “I’m putting it in!” Thwack! This time, they saw it clearly: their companion’s head bursting apart in the beam of light. - Kiiik! - Kyaaaauuu! *Another of our bloodline has died after the boss!* Furious beyond measure, the wyverns vowed revenge against that damned human. - Kiiit! Of course, not today. They would get their revenge later. A little later. “Hey, blue wyvern over there!” Thwack! *…Would they ever get their revenge?* Around a dozen pairs of wings began flapping desperately. [^1]: *Bangzi* (棒子) is a derogatory Chinese slur for Koreans.

## Korean source

```text
＃379화



드드드득!

거대한 울림과 지면을 통해 전해지는 진동.

지평선을 바라본 스무 살의 청년. 샤오 쉔(Shao Shen)은 도무지 지금의 상황을 믿을 수 없었다.

‘수천 킬로 밖에 있어야 할 몬스터들이 어떻게……!’

이것은 샤오 쉔 혼자만이 떠올린 의문이 아니었다.

천여 명의 공안 무력부 소속의 헌터와 치안 유지를 위해 파견된 오천 명의 중국 인민 해방군. 청두 국제공항에 주둔해 있던 모두가 같은 의문을 떠올렸고, 눈앞에 닥쳐 온 현실에 경악했다.

- 취이익!

- 그워어어!

하급 몬스터인 고블린, 오크부터 트롤, 오우거와 라이칸슬로프 같은 상위 몬스터까지.

지평선을 가득 메운 몬스터 대군이 괴성과 함께 돌진하고 있었다.

1km의 거리가 시시각각 빠르게 좁혀지는 광경에 비명 같은 외침이 터져 나왔다.

“각 제대 별로 대열 갖춰! 집합! 집하압-!”

“쏴, 쏴라! 쏘란 말이다!”

타다다당! 꽈앙!

황급히 대열을 갖춘 인민해방군이 상관의 명령에 따라 화력을 퍼부었지만, 효과는 미비하기 짝이 없었다.

예상치 못한 몬스터 대군의 습격.

아무 능력도 없는 일반인에 불과한 군인들은 공포로 몸이 굳었고, 그들이 발사한 화기는 고작해야 하급 몬스터들에게만 통하는 수준이었다.

“몬스터들이, 몬스터들이 너무 많습니다!”

“파일럿!”

“어서 전투기를 띄워라! 놈들의 머리 위로 폭격을……!”

다급한 지휘관들의 외침은, 다음 순간 하늘 위에서 울려 퍼진 흉포한 괴성에 파묻혔다.

- 캬우우우우!

“저, 저건!”

“와이번! 와이번이다!”

석양을 등지고 날아오는 거대한 동체.

창공의 공포라 불리는 와이번을 선두로 수십 마리의 그리폰(Griffon), 가고일(Gargoyle)이 뒤따른다.

수 미터의 날개를 비스듬히 꺾으며 하강한 A급 몬스터들이 아직 미처 이륙하지 못한 전투기들을 덮쳤다.

콰드드득! 콰광!

위력적인 날갯짓에 수 톤의 쇳덩이가 들썩였고, 마력이 실린 발톱에 전투기의 기체가 종잇장처럼 찢겨 나갔다.

폭발과 함께 엄청난 힘으로 튕겨 나간 금속 파편이 황급히 뛰어가던 파일럿들을 덮쳤다.

퍼버벙! 콰직!

비명조차 남기지 못한 즉사.

정신을 차린 지휘관의 명령에 따라 총기가 불을 뿜었지만, 강력한 마력을 머금은 피부와 가죽은 수백, 수천 발의 탄환으로도 생채기만 내는 것이 고작이었다.

- 키키키킷.

무력한 인간을 비웃는 몬스터의 웃음소리에, 사람들은 전신의 털이 곤두서는 듯한 충격과 공포를 느꼈다.

“이, 이럴 수가.”

지상과 상공을 가득 메운 몬스터 대군. 화기조차 제대로 통하지 않는 놈들은 그야말로 괴물이었다.

“괴, 괴물…….”

“나, 난 살아야겠어. 이런 곳에서 개죽음당하기는 싫다고!”

죽음에 대한 공포는 그 어떤 전염병보다 빠르게 퍼져 나갔다.

인민 해방군이 하나둘씩 뒷걸음질 치던 그때, 오히려 앞을 향해 나아가는 한 사람이 있었다.

“물러서지 마라!”

아직 앳된 기가 가시지 않은 청년, 샤오 쉔이 타오르는 눈빛으로 외쳤다.

그가 착용한 갑옷의 가슴팍에는 중화인민공화국의 국기인 오성홍기(五星紅旗)가 새겨져 있었다.

“우리가 누구인가!”

젊은 청년의 물음에 도망치려던 이들이 발걸음을 멈췄다.

샤오 쉔은 수백 미터 밖에서 돌격해 오는 몬스터 군단을 노려보았다. 깊게 눌러쓴 투구 사이로 다시 한번 천둥 같은 목소리가 터져 나왔다.

“우리가 누구인가!”

피가 끓어오르는 듯한 외침.

모두의 시선 속에 샤오 쉔은 창날을 곧추세웠다.

“우리는 중화의 후예이고, 인민 해방군과 공안 무력부(公安武力部)의 형제들이다!”

하늘을 찌를 듯 높이 솟구친 창날에서 석양빛을 닮은 오라가 솟구쳤다.

츠츠츠츠!

“가자! 저 괴물들을 모조리 쓸어 버리자!”

“와아아아아!”

귀가 먹먹해지는 거대한 함성이 지축을 뒤흔들었다.

샤오 쉔을 필두로, 공안 무력부 소속의 헌터들이 각자의 무기를 손에 쥔 채 몬스터 대군을 향해 맹호처럼 짓쳐 들었다.

“물러서지 마라! 중화의 힘을 보여 줘라!”

“으아아아!”

- 구워어어어!

- 아우우우!

죽음을 각오한 결의가 담긴 인간의 외침과 몬스터들의 괴성이 뒤섞인다. 한 덩어리가 된 두 집단이 서로를 향해 얽혀들었다.

콰과과과광!

하늘과 땅을 울리는 격돌. 그리고 사방에서 빗발치는 죽음.

“크아아악!”

- 쿠에엑!

푸푸푹! 퍼걱!!

지상 곳곳에서 비명과 굉음이 울려 퍼졌다.

오라가 서린 A급 헌터의 검신이 라이칸스로프의 목을 갈랐고, 오우거가 휘두른 쇠몽둥이에 서너 명의 헌터들이 피곤죽이 되어 날아간다.

힘을 합쳐 몬스터 하나를 쓰러트리고 다음 적을 향해 무기를 휘두르려던 두 헌터의 머리 위에 거대한 그림자가 드리웠다.

- 키이이잇!

서걱!

급강하한 그리폰의 발톱이 헌터들의 육신을 갑옷과 함께 갈기갈기 찢었다.

다음 사냥감을 찾아 헤매는 그리폰을 향해 커다란 불의 구(球)가 날아왔다.

“파이어 볼(Fire Ball)!”

퍼버벙!

매캐한 연기와 함께 상공을 유영하던 그리폰의 동체가 휘청였다. 지상에서 호시탐탐 때를 노리고 있던 원거리 부대는 그 틈을 놓치지 않았다.

“지금!”

펑! 퍼버버벅!

가지각색의 마법과 마나를 한껏 머금은 화살이 그리폰을 꿰뚫었다.

단말마와 함께 추락하는 그리폰의 모습에 비행 몬스터들이 흉포한 괴성을 토해 냈다.

- 캬우우우우!

원거리 부대를 향해 내리꽂히는 비행 몬스터들을 가로막은 것은, 납과 철로 이루어진 현대식 무기였다.

“일제 사격, 실시!”

타타타타탕! 콰앙!

무수히 많은 소총과 중화기. 수십여 대의 전차가 일시에 불을 토해냈다.

비록 몬스터들의 마력과 상극이라 할 수 있는 마나(Mana)의 힘에 비할 바는 아니지만, 일거에 화력을 집중시키니 비행 몬스터들도 주춤할 수밖에 없었다.

- 키잇!

“통한다!”

“다른 곳은 소용없다! 눈을 노려!”

날 때부터 마력을 머금은 몬스터들의 피륙은 대부분의 물리력을 가뿐히 무시한다. 그러나 단 한 곳, 눈만은 예외였다.

얕은 피막에 싸여 있는 안구는 중화기를 동원한다면 충분히 피해를 입힐 수 있는 수준.

멈칫거리는 몬스터들의 모습에, 모든 광경을 지켜보고 있던 사단장이 신나게 지휘봉을 휘둘렀다.

“더! 더 퍼부어라! 저 괴물들이 꼼짝도 못 하게…….”

콰아아아아!

음성은 이어지지 못했다.

그린 와이번이 쏘아 보낸 포이즌 브레스(Poison Breath)가 반경 백여 미터를 뒤덮었고, 사단장을 포함한 참모 지휘부는 강력한 산성 독을 뒤집어쓴 채 녹아내렸다.

“사, 사단장님!”

“지휘부가……!”

눈 깜짝할 사이에 수백의 병사와 고급 지휘관을 잃은 인민 해방군은 패닉 상태에 빠졌다.

장교와 부사관, 병사. 가릴 것 없이 모두가 경악에 찬 외침과 함께 눈 앞에 펼쳐진 끔찍한 광경을 바라봤다.

“이럴 수가…….”

“이, 이건 아니야. 이럴 수는 없어! 이런 건 내 임무가 아니라고!”

누군가의 비명은 모두의 심정을 대변하는 것이었다.

만일을 대비해 전력을 끌고 오긴 했지만, 그들의 주 임무는 곧 청두 국제공항에 도착할 외국의 헌터들과 합류, 호위하며 상부의 명령에 따라 움직이는 것이었다.

수천 킬로미터 밖에 있을 몬스터 군단이 쳐들어올 거라는 내용은 어디에서도 들은 바 없었다.

“이게 도대체…….”

“죽는다. 우리 모두 죽을 거야.”

잠시 잊었던 공포감이 인민 해방군의 머리 위에 내려앉았다.

그들은 전장의 선두에서 싸우고 있는 공안 무력부의 헌터들이 아니라, 현대식 화기를 든 평범한 일반인에 불과했으니까.

그리고 불길한 짐작은 곧 현실이 되었다. 그들이 생각했던 것보다 더한 악몽으로.

- 옴. 느. 하. 소. 유.

뚝뚝 끊어지는 목소리. 수신이 불안정한 라디오의 노이즈를 닮은 스산한 소음이 전장에 울려 퍼진다.

어디선가 몰려온 검은 안개가 사람들의 머리 위를 뒤덮었다.

- 옌. 위. 가. 지. 케!

그때였다. 끔찍한 변화가 일어난 것은.

쏴아아아악!

먹구름처럼 어두운 마력이 피와 시체를 타고 거미줄처럼 뻗어 나갔다.

싸늘하게 식어 가는 시신에 새로운 힘과 영혼을 불어넣고, 사슬로 묶어 종속시킨다.

투둑, 투두두둑.

새로운 생명을 얻고 죽음의 웅덩이에서 서서히 몸을 일으키는 백골(白骨)의 군단.

무수한 망자들을 보이지 않는 사슬로 엮어 종으로 삼은 ‘그 존재들’은 만족스럽게 웃었다.

- 킥, 키키킥.

- 그극. 키히히.



* * *



- 그르르륵.

끓어오르는 소리와 함께 사내가 몸을 일으킨다.

오성홍기가 새겨진 갑옷과 거대한 도끼를 든 그는 샤오 쉔이 기억하는 A급 헌터의 모습 그대로였다.

‘……야오위 씨.’

그러나 샤오 쉔은 사내의 이름을 소리 내어 부를 수 없었고, 부르지도 못했다.

눈앞의 그가, 더이상 자신이 알던 사람이 아니라는 사실을 알기 때문이다.

‘아, 아아.’

만약 십여 분 전 그가 목이 잘리는 광경을 목격하지 않았다면, 지금 이 순간 자신의 잘려 나간 목을 옆구리에 낀 채 일어나지 않았다면 샤오 쉔은 그를 동료이자 친구로 생각했을 것이다.

하지만 이제 야오위는 존재하지 않는다. 샤오 쉔의 입술 사이에서 그의 새로운 이름이 흘러나왔다.

“듀라한(Dullahan)…….”

목 없는 기사. 듀라한.

샤오 쉔은 상위 언데드 몬스터로 거듭난 동료의 모습에 입술을 깨물었다. 뜨거운 무언가가 볼을 타고 흘러내렸다.

“미안합니다. 정말로.”

- 그어어어!

괴성과 함께 달려드는 듀라한을 향해, 샤오 쉔은 바람처럼 쏘아졌다.

과거 두 사람은 종종 이렇게 대련을 벌이고는 했다. 단순한 호승심으로 시작한 대련은 매일마다 계속되었고, 대련이 끝나면 야오위의 투정을 받아 주어야 했다.



‘어린놈이 예의가 없어요, 예의가. 한 번 져 주면 덧나냐?’

‘하하. 밥이나 먹으러 가죠. 대련에 진 사람이 계산하기로 했으니까, 오늘도 야오위 씨가 사겠네요.’

‘집에 돈도 많은 놈이 밝히기는. 내가 언젠가 네 녀석한테 밥 얻어먹고 만다.’



하지만 그런 일은 과거에도, 앞으로도 없을 것이다. 승자는 늘 샤오 쉔이었다.

‘잘 가요. 그동안 고마웠습니다.’

후웅! 서걱!

휘둘러진 도끼는 허공을 갈랐고, 샤오 쉔의 창날에서 솟구친 오러는 듀라한의 상반신을 갈랐다.

허리춤으로부터 그어진 선. 목 없는 기사의 신형이 천천히 허물어진다.

쿵, 털썩.

쓰러진 듀라한, 아니 야오위의 얼굴을 물끄러미 내려다보던 샤오 쉔의 눈동자가 뜨겁게 달아올랐다.

“감히, 감히 이런 짓을…….”

반나절 전만 해도 함께 웃고 떠들던 친구와 동료들이 언데드 몬스터가 되었다.

공안 무력부의 헌터들은 군기가 엄정하기로 이름 높지만 피 한 방울 없는 냉혈한들은 아니었다.

죽을 각오로 전투에 임하던 헌터들은 처음으로 인정(人情)이라는 두려움에 직면했다.

“정신 차려! 나 류인친이야! 류인친!”

“혀, 형……!”

- 크르르륵!

퍼걱! 콰과광!

사방에서 비명과 죽음이 빗발쳤다. 절반에 가까운 피해를 입은 공안 무력부와 달리, 오히려 숫자를 불린 몬스터 군단은 끊임없이 밀려들었다.

‘이곳에서, 이렇게 죽는 건가?’

샤오 쉔은 난생처음으로 죽음을 떠올렸다. 늘 밝고 쾌활하던 그가 이렇게 생각할 만큼 상황은 절망적이었다.

‘위험 신호를 받지 못했으니 아마도 통신은 불통, 지원도 없을 테니…… 정말 끝장이구나.’

서걱!

달려드는 언데드 몬스터를 연달아 베어 넘긴 샤오 쉔은 허탈하게 웃으며 하늘을 바라봤다.

노을빛이 퍽 아름답다. 곧 해가 지고 어둠이 찾아오면, 이런 광경도 두 번 다시 보지 못할 것이다.

‘다행이야. 마지막으로 보는 하늘치고는 썩 괜찮…….’

어?

샤오 쉔은 생각을 잇지 못하고 눈을 깜빡였다.

하늘 위, 엄청나게 거대한 무언가가 빠른 속도로 전장을 향해 가까워지고 있었다.

‘비행기?’

콰아아아아아!

불길이 타오르는 거대한 기체. 그리고 드넓은 창공에 울려퍼지는 누군가의 외침.

“야아! 몬스터어!”

“……?”

- ……?

지금 헛것을 들은 건가.

샤오 쉔뿐만 아니라 전장의 모두가 하늘을 올려다보았다.

광기마저 느껴지는 누군가의 목소리가 천둥처럼 울려 퍼졌다.

“박는다!”

박아? 뭘?

샤오 쉔은 곧 그 말의 뜻을 깨달을 수 있었다.

쿠구구구궁!

비행기의 거대한 동체가, 그대로 전장을 휩쓸었다.
```

## Current accepted English baseline

```markdown
# Chapter 379

Rrrrrumble!

A tremendous roar, followed by vibrations traveling through the ground.

Shao Shen, a twenty-year-old young man staring toward the horizon, simply could not believe what he was seeing.

*How can monsters that should be thousands of kilometers away be here…?*

He was not the only one asking that question.

More than a thousand Hunters from the Public Security Armed Forces, along with five thousand soldiers of the Chinese People’s Liberation Army dispatched to maintain public order—all of them stationed at Chengdu International Airport—were asking themselves the same thing as they stared in horror at the reality bearing down on them.

- Ssssss!

- Grrrrr!

From low-level monsters like goblins and orcs to higher monsters like trolls, ogres, and lycanthropes—

A monster army filling the horizon was charging forward with hideous roars.

The distance of one kilometer was shrinking by the second. Shouts like screams erupted across the airport.

“Form ranks by unit! Assemble! Assembllllle—!”

“Fire! Fire! I said fire!”

Rat-a-tat-tat! Boom!

The People’s Liberation Army hurriedly formed ranks and poured out firepower at their commanders’ orders, but the effect was pitifully small.

They had been ambushed by an unexpected monster army.

The soldiers, who were merely ordinary people without any abilities, froze in fear. Their firearms were barely effective against the low-level monsters at best.

“There are too many monsters! There are too many!”

“Pilots!”

“Get the fighter jets into the air! Bomb them from above—!”

The desperate shouts of the commanders were drowned out the next moment by a savage roar that rang across the sky.

- Kyaaaauuu!

“W-What is that?”

“Wyverns! They’re wyverns!”

A massive body came flying with the setting sun behind it.

Leading the charge were wyverns, known as the terror of the skies, followed by dozens of griffons and gargoyles.

The A-rank monsters descended with their wings angled sharply, swooping down upon the fighter jets that had not yet managed to take off.

Krrrunch! Boom!

The powerful beat of their wings made several-ton blocks of metal jolt, while claws infused with magic tore through the fighter jets like sheets of paper.

The metal fragments hurled away by the explosions crashed into the pilots running frantically across the tarmac.

Bang-bang! Crunch!

Instant death. They did not even have time to scream.

The guns began spitting fire at the commanders’ orders once they regained their senses, but the flesh and hide saturated with powerful magic could do little more than suffer scratches from hundreds or even thousands of bullets.

- Kikikikit.

The monsters laughed at the helpless humans.

Everyone felt a shock and terror that made the hair all over their bodies stand on end.

“H-How can this be?”

A monster army filled the ground and the sky. The creatures that could barely be harmed by firearms were monsters in the truest sense.

“M-Monsters…”

“I-I have to live. I don’t want to die like a dog in a place like this!”

Fear of death spread faster than any epidemic.

And just as the soldiers of the People’s Liberation Army began taking a step backward one by one, one person instead moved forward.

“Don’t retreat!”

Shao Shen, a young man whose boyishness had not yet faded, shouted with blazing eyes.

The five-star red flag of the People’s Republic of China was embroidered across the chest of his armor.

“Who are we?”

At the young man’s question, those who had been about to flee stopped in their tracks.

Shao Shen glared at the monster army charging from several hundred meters away. His thunderous voice erupted again from beneath his tightly pulled helmet.

“Who are we?”

His shout made their blood seem to boil.

With everyone watching him, Shao Shen raised his spear point straight into the air.

“We are the descendants of Zhonghua, and we are brothers of the People’s Liberation Army and the Public Security Armed Forces!”

An aura resembling the colors of the setting sun surged from the spear point, which rose high enough to pierce the sky.

Ssssss!

“Let’s go! Let’s sweep away every last one of those monsters!”

“Waaaaah!”

A colossal roar that made their ears ring shook the earth.

Led by Shao Shen, the Hunters of the Public Security Armed Forces gripped their weapons and charged into the monster army like fierce tigers.

“Don’t retreat! Show them the power of Zhonghua!”

“Uraaaaaah!”

- Grrrrr!

- Awooooo!

Human cries filled with the resolve to face death mingled with the monsters’ roars.

The two groups became one mass as they crashed into each other.

Kra-kra-kra-boom!

A clash that shook the heavens and earth.

And death raining down from every direction.

“Gaaaaah!”

- Kweeeek!

Thud! Crunch!

Screams and thunderous impacts rang out across the battlefield.

The aura-coated blade of an A-rank Hunter cleaved through a lycanthrope’s neck, while an ogre’s iron club sent three or four Hunters flying as bloody pulp.

Two Hunters worked together to bring down a monster, then raised their weapons toward the next enemy.

A massive shadow fell over their heads.

- Kiiiiit!

Slash!

The claws of a griffon diving from the sky shredded the Hunters’ bodies along with their armor.

A large ball of fire flew toward the griffon as it searched for its next prey.

“Fireball!”

Bang!

The griffon’s body, gliding through the sky, staggered amid a cloud of acrid smoke.

The ranged units waiting on the ground for their chance did not miss the opening.

“Now!”

Boom! Bang-bang-bang!

Spells of every kind and arrows saturated with mana tore into the griffon.

The flying monsters let out savage cries at the sight of the griffon plummeting with a final scream.

- Kyaaaauuu!

The modern weapons made of lead and iron blocked the flying monsters diving toward the ranged units.

“Commence mass fire!”

Rat-a-tat-tat-tat! Boom!

Countless rifles and heavy weapons fired at once. Dozens of tanks spewed fire simultaneously.

Though modern weapons were no match for mana—the natural counter to monsters’ magic—concentrating all that firepower at once still forced even the flying monsters to falter.

- Kiiit!

“It works!”

“It’s useless anywhere else! Aim for their eyes!”

Monsters were born with magic running through their bodies, and their flesh could casually ignore most physical force.

But their eyes were the one exception.

Their eyeballs, covered only by a thin membrane, could be damaged if heavy weapons were brought to bear.

At the sight of the monsters hesitating, the division commander watching everything unfold excitedly waved his baton.

“More! Pour more fire into them! Don’t let those monsters move an inch—”

Whoooooom!

His voice never finished.

Poison Breath fired by a green wyvern covered a radius of more than a hundred meters. The division commander and the command staff were drenched in potent acidic poison and melted away.

“D-Division Commander!”

“The command staff…!”

The People’s Liberation Army fell into a state of panic after losing hundreds of soldiers and senior commanders in the blink of an eye.

Officers, noncommissioned officers, and soldiers alike stared at the horrific scene unfolding before them, crying out in shock.

“This can’t be happening…”

“N-No. This isn’t right. This can’t be happening! This isn’t what I signed up for!”

Someone’s scream spoke for everyone.

They had brought their forces as a precaution, but their primary mission was to join up with and escort the foreign Hunters who would soon arrive at Chengdu International Airport, then follow orders from above.

They had never heard anything about a monster army that should have been thousands of kilometers away invading the airport.

“What the hell is going on…?”

“We’re going to die. We’re all going to die.”

The fear they had briefly forgotten settled over the heads of the People’s Liberation Army once more.

Unlike the Hunters of the Public Security Armed Forces fighting on the front lines, they were merely ordinary people carrying modern firearms.

And their ominous premonition soon became reality.

A nightmare far worse than they had imagined.

- Om. Ne. Ha. So. Yu.

A voice broken into disconnected syllables.

An eerie noise resembling the static of a radio with an unstable signal echoed across the battlefield.

Black fog that had come from somewhere spread over the heads of the people.

- Yen. Wi. Ga. Ji. Ke!

That was when the horrifying change occurred.

Swoooooosh!

Dark magic as black as storm clouds spread like a web through the blood and corpses.

It breathed new strength and souls into bodies that were growing cold, then bound them in chains and enslaved them.

Snap. Snap-snap.

Given new life, an army of skeletons slowly rose from the pools of death.

*Those beings* had woven countless dead together with invisible chains and made them their slaves.

They laughed in satisfaction.

- Kik, kikikik.

- Grrk. Kihihihi.

* * *

- Grrrrr.

With a bubbling sound, a man rose to his feet.

He wore armor bearing the five-star red flag and carried a massive ax. He looked exactly like the A-rank Hunter Shao Shen remembered.

*…Mr. Yao Wei.*

But Shao Shen could not call the man’s name aloud.

No—he could not bring himself to call it.

He knew that the person standing before him was no longer the man he had known.

*Ah… ahhh.*

If Shao Shen had not witnessed the man’s decapitation ten minutes earlier, if he had not seen him rise with his severed head tucked beneath his arm, Shao Shen would have thought of him as a comrade and friend.

But Yao Wei no longer existed.

A new name slipped between Shao Shen’s lips.

“Dullahan…”

A headless knight.

A dullahan.

Shao Shen bit his lip at the sight of his comrade transformed into a higher undead monster.

Something hot ran down his cheek.

“I’m sorry. I really am.”

- Grrrrraaaah!

As the dullahan charged at him with a roar, Shao Shen shot forward like the wind.

In the past, the two of them had often sparred like this.

Their bouts had begun with nothing more than competitive pride and continued day after day. Once each spar ended, Shao Shen had to put up with Yao Wei’s complaints.

*You little brat have no manners, I tell you. Would it kill you to let me win once?*

*Ha-ha. Let’s go get something to eat. The loser was supposed to pay, so I guess you’re buying again today, Mr. Yao Wei.*

*You’ve got plenty of money at home, and you’re still so cheap. One day, I’ll make you buy me a meal.*

But that had never happened before, and now it never would. Shao Shen had always been the winner.

*Goodbye. Thank you for everything.*

Whoosh! Slash!

The ax swept through empty air, while the aura surging from Shao Shen’s spear point cleaved through the dullahan’s upper body.

A cut line appeared, starting at his waist. The headless knight’s body slowly crumpled.

Thud. Collapse.

Shao Shen stared blankly down at the face of the fallen dullahan—no, Yao Wei.

His eyes burned.

“How dare you… How dare you do this…”

His friends and comrades, who had been laughing and joking with him only half a day earlier, had become undead monsters.

The Hunters of the Public Security Armed Forces were famous for their strict discipline, but they were not cold-blooded people without a drop of human feeling.

The Hunters who had entered the battle prepared to die now faced something frightening for the first time—the fear of human attachment.

“Wake up! It’s me, Ryu Inchin! Ryu Inchin!”

“H-Hyung…!”

- Grrrrr!

Crunch! Boom!

Screams and death rained down from every direction.

Unlike the Public Security Armed Forces, which had suffered casualties approaching half its strength, the monster army had increased its numbers and continued to surge forward without end.

*Am I going to die here, like this?*

For the first time in his life, Shao Shen thought about death.

The situation was so desperate that even someone as bright and cheerful as him had begun to think that way.

*We didn’t receive any warning signal, so communications must be down. There won’t be any reinforcements either… This really is the end.*

Slash!

After cutting down one undead monster after another, Shao Shen laughed hollowly and looked up at the sky.

The sunset was surprisingly beautiful.

When the sun went down and darkness arrived, he would never see a sight like this again.

*It’s not so bad for the last sky I’ll ever see…*

Huh?

Shao Shen blinked, unable to finish the thought.

Something unimaginably enormous was rapidly approaching the battlefield from high above.

*An airplane?*

Whoooooom!

A massive aircraft engulfed in flames.

And someone’s shout rang across the vast sky.

“Hey! Monsters!”

“…?”

- …?

*Am I hearing things?*

Shao Shen was not the only one to look up.

Everyone on the battlefield raised their eyes toward the sky.

A voice that seemed to hold even a hint of madness thundered across the battlefield.

“I’m going to ram it!”

*Ram what?*

Shao Shen soon understood what the voice meant.

Rrrrrumble!

The massive fuselage of the airplane swept across the battlefield.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 379`.

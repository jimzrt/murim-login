# Master Edit Task — Chapter 380

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

| 진태경    | **Jin Taekyung**   |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 살기     | **killing intent**                               |                                                       |
| 대주     | **Squad Leader** / **Commander**             |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 퀘스트              | **Quest**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 백염 | **White Flame** | Previously bound item listed by the System. |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 중화 | **Zhonghua** | Term used in Shao Shen's rallying cry for China. |
| 듀라한 | **Dullahan** | Higher undead monster form taken by Yao Wei. |
| 시벌좌 | **Sibeol-jwa** | Taekyung's profane nickname, recognized by Shao Shen. |
| 화염신장 | **Flame Divine Palm** | Named fire-based palm technique used by Taekyung. |
| 멸염신권 | **Flame-Annihilating Divine Fist** | Named fire-based fist technique used by Taekyung. |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 375–379

## Plot

Tang Sadok awakens and confesses that he revealed the Myriad Poison Ring’s location to the Western Heaven Demon Lord to protect the Sichuan Tang Clan. Taekyung forgives him, completing the Hidden Quest **Atonement and Forgiveness** and earning the **Benefactor of the Tang Clan** Title, EXP, Fame, and a level up. Tang Sadok transfers the Myriad Poison Ring to Taekyung, making it bound. The Divine Physician asks Taekyung for time before his departure, while Cheongpung becomes Mimi’s temporary guardian.

Taekyung and his companions leave the Sichuan Tang Clan amid a massive farewell. Mungyeong’s disciple Dongbong recalls how Mungyeong cured him after an epidemic killed his wife and children. Dongbong asks Mungyeong to prevent the great war he expects to come, but Mungyeong insists that his place is outside the Murim. At Chengdu’s western port, Taekyung accepts an unidentified boy as a last-minute passenger aboard the Water Dragon Stronghold’s ship.

The Sichuan Governor’s concubine Ae-hyang manipulates him into concealing the government’s involvement in the recent conflict and submitting an inflated report. A sinister red light appears in her eyes, implying an unidentified superior’s influence. During the voyage, Taekyung identifies the surviving Black Dragon Armor fragment, renames it **Flame Dragon Armor** after infusing it with Scorching Yang Qi, and learns that it repairs itself by consuming his internal energy. He then completes Logout.

Taekyung awakens aboard a private jet returning to the modern world, with Chengdu International Airport under monster attack. Around a dozen A-rank wyverns pursue the aircraft. With Team Leader Choi maintaining a pressure-sealing barrier, Taekyung cuts open the hull using an Aura Blade and kills Black Star and several wyverns with a spear. The survivors retreat, promising revenge.

At the airport, twenty-year-old Hunter Shao Shen leads Chinese Hunters and soldiers against a monster army. A green wyvern’s Poison Breath kills the command staff, after which dark magic spreads through blood and corpses, resurrecting the dead as bound undead. Shao Shen kills his friend Yao Wei after Yao is transformed into a headless Dullahan. As the defenders near defeat, Taekyung’s burning airplane sweeps toward the battlefield.

## Continuity

- Taekyung forgave Tang Sadok, completed **Atonement and Forgiveness**, gained the **Benefactor of the Tang Clan** Title, and received EXP, Fame, and a level up.
- The Myriad Poison Ring is now bound to Taekyung. His bound items include White Flame, Myriad Poison Ring, and Flame Dragon Armor.
- Tang Sadok is awake and again serving as Family Head of the Sichuan Tang Clan; the clan owes Taekyung’s group a significant debt.
- Cheongpung is temporarily responsible for Mimi while the Tang Clan’s future remains uncertain.
- The Divine Physician has asked Taekyung for time, but the matter remains undisclosed.
- Mungyeong is both the Divine Physician and the Slaughter Saint; Dongbong is his longtime disciple. Mungyeong verbally refuses to intervene in the coming war, though his ultimate choice remains unresolved.
- An unidentified boy boarded Taekyung’s departing ship at Chengdu’s western port.
- Ae-hyang is secretly influenced by an unidentified superior; the Governor’s false memorial and its consequences remain unresolved.
- Logout succeeded. Taekyung has returned to the modern world aboard a Central Committee of China jet bound for Chengdu International Airport.
- Team Leader Choi can maintain a pressure-blocking barrier. Taekyung’s sword qi is called an Aura Blade in the modern world.
- The Lich is suspected of extending its reach to Chengdu, but its exact role in the attack is unconfirmed.
- Black Star and several pursuing wyverns were killed; surviving wyverns escaped and seek revenge.
- Shao Shen is a twenty-year-old spear-wielding Hunter of the Public Security Armed Forces. Yao Wei was his A-rank friend and comrade before becoming a Dullahan.
- The airport’s undead army is created and controlled through dark magic, but the controlling beings’ identities remain unknown.
- The burning aircraft’s passengers, its impact on the monster army, and Taekyung’s immediate fate remain unresolved.

## Translation Decisions

- Preserve **Atonement and Forgiveness**, **Benefactor of the Tang Clan**, **Myriad Poison Ring**, **Flame Dragon Armor**, **Divine Physician**, **Slaughter Saint**, **Dongbong**, **Water Dragon Stronghold**, **Aura Blade**, **Black Star**, **Shao Shen**, **Yao Wei**, **Dullahan**, **Public Security Armed Forces**, and **Chengdu International Airport**.
- Render **술시** as **the Hour of the Dog**, with a footnote identifying it as approximately 7–9 p.m.
- Render **식경** as **sikgyeong**, approximately thirty minutes, with a footnote.
- Render **강기** as **sword qi**, **오라 블레이드** as **Aura Blade**, **흑룡갑** as **Black Dragon Armor**, and **화룡갑** as **Flame Dragon Armor**.
- Render **수룡채** as **Water Dragon Stronghold**, **열화신공** as **Blazing Flame Divine Art**, **선화아** as **boatman**, and **무송** as **Mu Song**.
- Retain Mungyeong’s distinction between his physician identity and his slaughter-demon past; preserve the chapter’s casual banter and Taekyung’s self-mocking narration.

### Prior accepted reading-copy tails

#### Chapter 378 tail (verified mastered)

…
was so shocked that he poked his head out and stared at me as if I were insane. “Of course not! The pressure-sealing system won’t even let you open it, and the aircraft will be damaged because it can’t withstand the pressure difference! We won’t be able to breathe properly, either!” Team Leader Choi, fiddling with the ring on his finger, cut in. “I think I can block the pressure. I don’t know what you have in mind, but go ahead and try.” “Okay.” “Don’t! You *bangzi* bastards![^1] Are you trying to kill us all?” “…What did you just call us?” The nerve of him, insulting Koreans right in front of a proud Korean kimchi man like me! The captain realized what had slipped out, and his face turned white. “No, that’s not what I meant.” “You fucking Chink bastard. Damn it.” “…!” “Hey, Captain!” “Y-Yes?” “I’m opening it.” “Ah! Ahhh!” Before the captain could stop me, I opened the door. No—I cut it open. Shhk! Sword qi—the force called an Aura Blade in the modern world—sliced through the sturdy alloy and created a small door. It was the tremendous power wielded by Supreme Peak masters in Murim and, in this world, only by S-rank Hunters. Team Leader Choi’s eyes widened in shock. “Mr. Jin Taekyung, this is—” “Team Leader!” Whoooosh! This was no time to be surprised. The tremendous wind and pressure were making the aircraft lurch, turning the cabin into a complete mess. The screams and my shout snapped Team Leader Choi back to his senses. He rubbed his ring. “An airtight barrier surrounds us. Barrier!” “Oh.” With the incantation, a transparent membrane of energy sealed the new opening without leaving the slightest gap. So there was a way to do this. With a brief exclamation of admiration, I stuck my upper body out of the cabin. Team Leader Choi’s barrier recognized me as an ally and let me pass through without resistance. Rrrrrumble! The wind pressure slammed into my upper body as if trying to crush me to death. I grinned. *This is no joke.* But it wasn’t unbearable. Actually, it would have been strange if I couldn’t withstand it. Compared to the waves of qi the Western Heaven Demon Lord had emitted, this was no more than a gentle spring breeze. - Kyaaaauuu! The monster’s sharp cry mixed into that spring breeze. The flock of wyverns had already drawn close enough for me to judge the distance. *About a hundred meters. I’ve never tried this before, but… at this distance, it should be enough.* *Open Inventory. Equip.* Ssswish. A spear I had bought at a discount from the Hunter Market appeared in my hand. Like a javelin thrower, I drew my shoulder all the way back. From my waist to my wrist, every muscle and tendon I needed pulled taut like a bowstring. - Kyaau! The lead wyvern—their chief—sensed something was wrong and threw back its head with a shriek. I could see a pure-white current of air being sucked toward its snout. *That’s…* - Breath! It’s Breath! Dodge it, you vile human! The Skeleton Warlord was right. Of all the countless monsters, Breath was a power granted only to the dragonkin. I could clearly see it taking shape inside the wyvern’s gaping maw. Whooooom. A massive sphere of wind. The Air Breath, powerful enough to shred metal like paper, finished taking shape. “Hey, wyvern!” - Kya? “I’m putting it in!” I shouted like a thunderbolt and whipped my drawn-back shoulder forward. Fwoom—whooosh! Fiery concentrated qi sheathed the spearhead, burning through the air and cleaving the wind. The wyvern’s bright yellow eyes widened at the blue-white streak of light shooting straight toward it. - Kiiiiiik! Whoooom! Compressed air burst from the tip of the spear. A cloud of white. And then— Thwack! Boom-boom! A massive body plummeted toward the ground like a kite with its string cut. * * * - Kyaau? - Kiiit? Around a dozen pairs of bright yellow eyes stared at one another. Wyverns were ferocious creatures from the moment they were born, but at this moment, they were utterly bewildered and had no idea what to do. - Kikikit? - Kiiik… *What? Is the boss dead?* *Looks that way…* After exchanging words in their own language, the wyverns were dumbfounded. Their leader was exceptionally powerful even among their own kind—so powerful that he was known as the “Black Star.” And now, the Black Star had become a black speck falling toward the impossibly distant ground. - Kiririk? - Grrrrr. None of them had even properly seen how he died. They could only guess that the tiny human had thrown a spear and hit him. But that was impossible. How could a mere human dare lay a hand on a descendant of the great dragons… “Hey, green wyvern over there!” - Kiiik? “I’m putting it in!” Thwack! This time, they saw it clearly: their companion’s head bursting apart in the beam of light. - Kiiik! - Kyaaaauuu! *Another of our bloodline has died after the boss!* Furious beyond measure, the wyverns vowed revenge against that damned human. - Kiiit! Of course, not today. They would get their revenge later. A little later. “Hey, blue wyvern over there!” Thwack! *…Would they ever get their revenge?* Around a dozen pairs of wings began flapping desperately. [^1]: *Bangzi* (棒子) is a derogatory Chinese slur for Koreans.

#### Chapter 379 tail (verified mastered)

…
been thousands of kilometers away invading the airport. “What the hell is going on…?” “We’re going to die. We’re all going to die.” The fear they had briefly forgotten settled over the heads of the People’s Liberation Army once more. Unlike the Hunters of the Public Security Armed Forces fighting on the front lines, they were merely ordinary people carrying modern firearms. And their ominous premonition soon became reality. A nightmare far worse than they had imagined. - Om. Ne. Ha. So. Yu. A voice broken into disconnected syllables. An eerie noise resembling the static of a radio with an unstable signal echoed across the battlefield. Black fog that had rolled in from somewhere spread over the people’s heads. - Yen. Wi. Ga. Ji. Ke! That was when the horrifying change occurred. Swoooooosh! Dark magic as black as storm clouds spread like a web through the blood and corpses. It breathed new strength and souls into bodies that were growing cold, then bound them in chains and enslaved them. Snap. Snap-snap. An army of skeletons rose slowly from the pools of death, granted new life. *Those beings* had woven countless dead together with invisible chains and made them their slaves. They laughed in satisfaction. - Kik, kikikik. - Grrk. Kihihihi. * * * - Grrrrr. With a bubbling sound, a man rose to his feet. Clad in armor bearing the Five-Star Red Flag and carrying a massive ax, he looked exactly like the A-rank Hunter Shao Shen remembered. *…Mr. Yao Wei.* But Shao Shen could not call the man’s name aloud. He could not bring himself to. He knew the figure before him was no longer the person he had known. *Ah… ahhh.* If Shao Shen had not witnessed the man’s decapitation a little over ten minutes earlier, if he had not seen him rise with his severed head tucked beneath his arm, Shao Shen would have thought of him as a comrade and friend. But Yao Wei no longer existed. His new name slipped from Shao Shen’s lips. “Dullahan…” A headless knight. A Dullahan. Shao Shen bit his lip at the sight of his comrade reborn as a higher undead monster. Something hot ran down his cheek. “I’m sorry. I really am.” - Grrrrraaaah! The Dullahan charged with a roar, and Shao Shen shot forward like the wind. In the past, the two of them had often sparred like this. Their bouts had begun with nothing more than competitive pride and continued day after day. Once each spar ended, Shao Shen had to put up with Yao Wei’s complaints. *You little brat. No manners, none at all. Would it kill you to let me win once?* *Ha-ha. Let’s go get something to eat. The loser pays, so I guess you’re buying again today, Mr. Yao Wei.* *Your family’s loaded, and you’re still so cheap. One day, I’ll make you buy me a meal.* But that had never happened before, and now it never would. Shao Shen had always won. *Goodbye. Thank you for everything.* Whoosh! Slash! The ax cut through empty air. Aura surged from Shao Shen’s spear point and cleaved through the Dullahan’s upper body. A cut line appeared, starting at his waist. The headless knight’s body slowly crumpled. Thud. Slump. Shao Shen stared blankly down at the face of the fallen Dullahan—no, Yao Wei. His eyes burned. “How dare you… How dare you do this…” Friends and comrades who had been laughing and joking with him only half a day ago had become undead monsters. The Hunters of the Public Security Armed Forces were famous for their strict discipline, but they were not cold-blooded people without a drop of human feeling. The Hunters who had entered the battle prepared to die now faced the fear of human attachment for the first time. “Wake up! It’s me, Ryu Inchin! Ryu Inchin!” “H-Hyung…!” - Grrrrr! Crunch! Boom! Screams and death rained down from every direction. Unlike the Public Security Armed Forces, which had suffered casualties approaching half its strength, the monster army had increased its numbers and continued to surge forward without end. *Am I going to die here, like this?* For the first time in his life, Shao Shen thought about death. The situation was desperate enough to make even someone as bright and cheerful as him think that way. *We didn’t receive any warning signal, so communications must be down. There won’t be any reinforcements either… This really is the end.* Slash! Shao Shen cut down one charging undead monster after another, then laughed hollowly and looked up at the sky. The sunset was surprisingly beautiful. When the sun went down and darkness arrived, he would never see a sight like this again. *Thankfully, it's not so bad for the last sky I'll ever see…* Huh? Shao Shen blinked, unable to finish the thought. Something unimaginably enormous was rapidly approaching the battlefield from high above. *An airplane?* Whoooooom! A massive aircraft engulfed in flames. And someone’s shout rang across the vast sky. “Hey! Monsters!” “…?” - …? *Am I hearing things?* Shao Shen was not the only one looking up. Everyone on the battlefield raised their eyes toward the sky. A voice that seemed even to carry madness thundered across the battlefield. “I’m going to ram it!” *Ram what?* Shao Shen soon realized what the voice meant. Rrrrrumble! The airplane’s massive fuselage swept straight across the battlefield.

## Korean source

```text
＃380화



샤오 쉔은 처음으로 깨달았다.

콰아아아아!

두 날개가 불에 휩싸인 채 지상으로 돌진하는 비행기를 목격한다면, 종(種)을 넘어선 공포에 사로잡힌다는 것을.

- 으어어어어!

그토록 흉포하다는 오우거가, 트롤이 비명을 내질렀고.

- 구워어어어!

언데드 몬스터 중에서도 가장 느려터졌다는 구울(Ghoul)도 발바닥에 땀이 나도록 뛰었다.

- 취이이익!

「어, 어어, 어어어…….」

비명이라도 지를 수 있는 몬스터들은 양반이었다.

샤오 쉔을 비롯한 대부분은 석상처럼 굳은 채 지상을 향해 돌진하는 비행기를 바라볼 수밖에 없었다.

‘도망쳐야 하는데…….’

발이, 손이 움직이지 않는다.

무엇보다 전장의 한가운데에 포위되어 있던 샤오 쉔과 공안 무력부의 헌터들에게는 도망칠 기회조차 주어지지 않았다.

‘이대로 끝장인가?’

모두의 머릿속에 같은 생각이 떠오른 그 순간.

쿠구구구구궁!

귀가 먹먹해지는 굉음과 함께, 비행기의 거대한 동체가 전장을 휩쓸었다.

그리고 그 경천동지할 충돌은 개미 떼처럼 흩어지던 몬스터 군단의 최후방으로부터 시작되었다.

콰지지지직! 우두둑!

수십 톤의 무게를 지닌 거대한 강철의 덩어리는 앞을 막아서는 모든 것을 부수고 터트렸다.

몬스터들의 녹색 핏물이 분수처럼 뿜어졌고 크고 작은 사지가 사방으로 솟구친다.

‘이, 이게 도대체…….’

몬스터들의 물리 방어력이 아무리 뛰어나다지만, 그것도 정도가 있는 법. 몬스터 믹서기로 변모한 비행기를 멈출 수 있는 것은 아무것도 없었다.

- 구워……!

- 키이이익!

콰드드드득!

섬뜩한 파육음에 몬스터들의 비명이 파묻힌다. 지금껏 본 적도, 들은 적도 없는 아비규환(阿鼻叫喚).

상상치도 못한 광경을 넋 놓고 바라보던 샤오 쉔과 헌터들의 귓가에, 광기에 찬 누군가의 외침이 파고들었다.

“몬스터! 박는다! 죽인다!”

“……!”

이런 와중에도 똑똑히 들리는 모국의 언어에 공안 무력부의 헌터들은 지원군이라는 세 글자를 떠올렸고, 샤오 쉔은 경악했다.

‘엄청난 강자!’

목소리에 실린 강대한 마나(Mana). 필시 S급 헌터가 틀림없었다.

“가 버렷! 비행기이이잇!”

“…….”

그것도 살짝 미친 S급 헌터가 확실하다.

섬나라 놈들이 세계 2차 대전 때나 쓰던 방법을 가져오다니. 아군이 죽을 것까지는 생각 못 했단 말인가.

‘중앙 군사 위원회에서 파견된 것 같은데…… 우리나라에 저런 S급 헌터가 있었나?’

문득 든 의문. 그러나 이제 샤오 쉔과는 그다지 상관없는 일이 될 것이다.

몬스터들을 갈아 버리며 전장의 절반을 가로지른 거대한 강철 덩어리가 그와 헌터들을 향해 돌진하고 있었으니까.

- 취, 취익!

「도망쳐!」

살기 위한 몸부림에 적아(敵我)의 구분은 없었다.

샤오 쉔은 코앞에 인간이 있는 것도 잊은 채 몸을 부딪혀 오는 몬스터를 향해 단검을 내질렀다.

푸푹!

- 크르륵.

숨이 끊긴 몬스터의 육체가 샤오 쉔을 향해 허물어진다.

사방에서 밀려드는 몬스터들로 인해 한 걸음도 움직일 수 없는 상황. 샤오 쉔은 자신을 덮쳐 오는 육중한 무게를 느끼며 외쳤다.

「전투는 끝나지 않았다! 마지막까지 싸워라!」

맞다. 아직 전투는 끝나지 않았다. 헌터는 숨이 끊기는 마지막 순간까지 몬스터를 죽여야 하는 존재다.

샤오 쉔의 외침을 들은 헌터들이 이를 악물고 무기를 휘둘렀다.

‘이걸로 됐어.’

번개 같은 솜씨로 도망치는 오우거의 뒤통수에 단검을 박아 넣은 샤오 쉔은 크게 심호흡했다.

어느새 이십여 미터 앞까지 들이닥친 비행기의 거체가 보였다.

처음보다 속도가 훨씬 줄긴 했지만, 옴짝달싹하지 못하는 상황에서 저것을 피하기란 요원해 보였다.

‘미련은 없다.’

자랑스러운 중화의 헌터로 인민을 위해 싸우다가 죽는다면, 그것으로 족했다.

샤오 쉔이 사방에서 빗발치는 비명을 들으며 눈을 감은 그 순간이었다.

“읏차.”

콰드드드득! 촤아악!

핏물로 짐작되는 끈적한 액체를 뒤집어쓴 샤오 쉔은 생각했다.

‘……읏차?’

보통은 으악, 아닌가?

단말마치고는 기묘한 소리에 샤오 쉔은 슬그머니 눈꺼풀을 들어 올렸다.

그리고 마침내 볼 수 있었다. 몇 걸음 앞에서 우뚝 멈춘 비행기와 두런두런 이야기를 나누고 있는 두 사내를.

“자, 도착했습니다. 혹시 폭발할지도 모르니까 사람들 데리고 얼른 내리세요.”

“……진태경 씨. 전부 다 기절했습니다.”

“그래요? 나약하네.”

“……배리어 마법이 아니었으면 죽었을 겁니다.”

“그럼 최 팀장님이 옮겨 주세요. 아, 맞다. 아까 우리한테 빵즈라고 했던 그 새끼도 살았어요?”

“예. 그, 살아는 있긴 한데.”

“그럼 그 새끼 잘 지켜 주세요. 나중에 돌아갈 때 두고두고 갈굴 거니까.”

“……노력해 보죠.”

샤오 쉔은 도무지 이 상황을 이해할 수 없었다.

누가, 언제, 어디서, 무엇을, 어떻게. 왜. 이건 육하원칙으로도 정리할 수 없을 만큼 괴상한 광경이었다.

‘비행기는 갑자기 어떻게 멈춘 거고, 저 사람들은 뭐지? 중앙 군사 위원회에서 보낸 헌터가 아니었단 말인가?’

심지어 두 사람은 다른 언어로 이야기를 나누고 있었다.

둘 중 귀공자처럼 멀끔하게 생긴 사내의 말은 알아들을 수 없었지만, 어느 나라의 언어인지는 안다.

오랜 시간 동안 이웃한 옆 나라, 바로 한국이다.

‘잠깐. 한국인이라면……!’

샤오 쉔은 핏물로 끈적이는 눈가를 황급히 비볐다. 그제야 한 사람을 알아볼 수 있었다.

남들보다 머리 하나는 큰 근육질의 청년.

TV에서나 보던 그가, 자신의 우상이 눈앞에 있었다.

「호, 혹시 한국에서 오신 진 선생님 되십니까?」

“엥?”

청년, 진태경이 샤오 쉔을 보며 고개를 갸웃거렸다.

“저 선생님 아닌데요.”

「그럼 시벌좌…….」

“……시벌. 뭐여.”

맞구나!

샤오 쉔은 전신을 감싸는 안도감과 희망에 몸을 부르르 떨었다.



* * *



‘도대체 중국인이 시벌좌를 어떻게 아는 거지.’

나에 관한 기사가 잠깐 외신에서 떠들썩하긴 했는데, 시벌좌라는 별명까지 알려져 있을 줄은 몰랐다.

오대양 육대주를 떨어 울리는 시벌좌라니.

미국에 가게 되면 떡대 끝내주는 양키 형님들이 맥주병을 들고 다가와 알은척을 할지도 모르겠다.

‘헤이, 유. 씨뻘쫘?’

아임 파인 땡큐다. 시벌. 도대체 어느 정신 나간 놈들이 이따위 별명을 지은 거야.

그나저나…….

“개판이네.”

주위를 둘러본 내 짤막한 감상평이다.

기절한 승무원들을 굴비처럼 엮은 최 팀장과 인벤토리 안에 처박아 둔 스켈레톤 워로드가 대답했다.

“끔찍한 광경입니다.”

- 간악한 인간이여, 본 사령관은 이곳이 마음에 드는구나. 익숙하고도 정겨운 기분이다.

“…….”

죽음, 그 자체라고 할 수 있는 네임드 언데드 몬스터가 흡족해할 정도니 두말해 봐야 입 아픈 수준이다.

“오자마자 실전 투입이라니.”

내 푸념에 응답하는 것처럼, 시스템 알림이 울렸다.

띠링.



- 돌발 퀘스트, [예상치 못한 습격]이 생성되었습니다.



이래서 돈을 많이 준다고 했던 건가. 나는 내심 혀를 차며 입을 열었다.

“최 팀장님, 우선 민간인들부터 보호하고 그 후에는 알아서 싸우세요. 너무 무리하지는 마시고.”

“예. 안 그래도 그럴 생각입니다.”

최 팀장은 똑똑한 사람이다. 진가심법을 익히면서 예전과는 비교할 수 없을 만큼 강해졌지만, 결코 과시하려 하지 않을 것이다.

“그리고 거기 계신 젊은 분.”

「예, 옛. 진 선생님.」

선생님은 무슨. 나는 빠릿빠릿하게 대답하는 젊은 청년을 위아래로 훑었다.

얼굴은 어리지만 척 봐도 헌터다. 그것도 A급 정도로 보이는 강자. 마치 공장에서 찍어 낸 것처럼 똑같은 갑옷을 입은 주위의 헌터들과는 달리, 어깨에는 붉은 휘장도 달려 있었다.

“보니까 직급깨나 있어 보이시는데, 부하들 잘 간수해요. 한 사람이라도 더 살리자고.”

「예, 예?」

“이제부터 시작이니까.”

나는 대답과 동시에 주먹을 뻗었다.

콰아아앙!

줄기줄기 쏟아진 열양지기(熱陽之氣)가 멍하니 서 있던 몬스터들을 향해 쏘아진다.

후끈한 열기가 한바탕 휩쓴 곳에는 수십여 구의 몬스터 사체만이 남았다.

“뭘 그렇게 쳐다보고 있냐. 누가 정지 버튼이라도 눌렀어?”

“……!”

- ……!

내 한 마디를 신호로.

전장을 짓누르고 있던 침묵이 산산 조각나며 깨어졌다.

- 쿠워어어어!

「주, 죽여라! 몬스터 놈들을 막아!」

인간과 몬스터, 몬스터와 인간.

죽고 죽이는 전투가 시작된다. 나는 지면 깊숙이 박혀 있는 백염을 뽑아 휘둘렀다.

스걱!

물 반, 고기 반이 아니라 사방이 몬스터로 득실거리는 상황.

창날에서 뻗어 나간 반월의 강기가 한데 뭉친 몬스터 무리를 스쳤다.

띠링.



- [Lv.15 언데드 고블린]를 처치했습니다!

- [Lv.78 언데드 라이칸스로프]를 처치했습니다!

- [Lv.93 듀라한]을 처치했습니다!

- [Lv.30 스켈레톤]을 처치했습니다!

.

.

.

- 레벨의 격차가 큽니다. 미비한 경험치를 획득했습니다!



몬스터 처치와 경험치 획득을 알리는 시스템 알림이 끊임없이 울려 퍼진다.

평소였다면 한 귀로 흘려듣거나 무시했을 알림.

그러나 이번만큼은 중요한 힌트가 되어 주었다.

“이놈들 이거 설마…….”

- 아아, 맞다. 간악한 인간이여! 이토록 강한 언데드 군단이라니!

환희에 가득 찬 스켈레톤 워로드의 외침은 내 짐작을 확신으로 바꿔 주기에 충분했다.

‘어쩐지, 뭔가 이상하더라니.’

안 그래도 놈들에게서 생기(生氣)가 느껴지지 않아 의아하던 차였다.

아직 살아 있는 몬스터의 숫자도 상당했지만, 거의 절반 이상의 몬스터가 언데드 상태였다. 모두 합하면 이천 마리에 달하는 대군이다.

“그리고 언데드 몬스터는…….”

스켈레톤 워로드가 잔뜩 신이 나서 외쳤다.

- 아름답고! 멋있고! 용맹하다!

퍼걱!

다섯 마리의 몬스터를 베어 버린 내가 중얼거렸다.

“방금 저놈처럼 소멸하고 싶냐? 아름답고, 멋있고, 용맹하게?”

- ……실언을 했군. 사과한다. 간악한 인간이여.

잠시 자신의 처지를 망각했던 스켈레톤 워로드가 황급히 덧붙였다.

- 잠깐. 그렇다면 누군가의 조종을 받는 것이 틀림없다!

내 생각도 마찬가지다.

다만 한 가지 확신이 서지 않는 것은…….

“리치(Lich). 그놈이 직접 나선 걸까?”

- 으음. 지난번에 네가 보여 준 그 홀로그램 영상이라는 것에 나오는 그 리치를 말하는 것이라면, 아마 아닐 거다.

스켈레톤 워로드의 대답을 들으며 반걸음을 내디뎠다.

쾅!

거대한 쇠몽둥이가 어깨를 아슬아슬하게 지나쳐 지면을 부순다. 아직 생기가 느껴지는, 평범한 오우거다.

- 구워어어!

“어, 구워 줄게.”

퍼벙!

화염신장을 가슴에 얻어맞은 오우거의 칠공에서 검녹색의 핏물이 터져 나왔다.

허물어지는 거체를 지나치며 백염을 비스듬히 내리그었다.

쉬이이이익! 서걱!

공간이 잘려 나가고 그 사이에 있던 몬스터들의 몸뚱어리가 조각 난다.

핏물과 체액을 뒤집어쓴 채로 날 멍하니 바라보는 중국인 헌터를 뒤로하며, 주먹을 말아쥐었다.

고오오옹.

초고온의 열기가 주먹을 향해 내달리고, 이내 전방을 향해 쏘아졌다.

꽈앙!

멸염신권(滅炎神拳).

거대한 불의 기둥이 몬스터들을 집어삼켰다.

살이 타들어 가는 고약한 냄새와 함께 용케 살아남은 놈들이 고통에 찬 괴성을 내지른다.

몬스터도, 헌터도 순간 싸우는 것을 잊을 정도의 파괴력.

스켈레톤 워로드가 더듬거리는 목소리로 말했다.

- 가, 간악한 인간이여. 더욱 더 괴물이 되었구나.

“괴물한테 괴물 소리 들으니까 기분 묘한데. 그나저나 리치가 아니면 도대체 어떤 놈이 이 난리를 피우는 건데?”

- 그야 본 사령관도 모르지. 하지만 한 가지는 장담할 수 있다.

“장담? 뭘?”

- 놈의 언데드 통제는 이 몸에 비해 한 수 아래라는 것. 으하하! 군단이여! 본 사령관은 너희가 그립구나!

“…….”

이 자식을 죽여, 살려.

고민하던 나는 문득 뇌리를 스치는 어떤 생각에 우뚝 멈췄다.

“야, 방금 뭐라고?”

- 으하하핫! 본 사령관의 위엄을 느꼈는가. 간악한 인간이여!

“소멸할래, 말할래.”

- ……말하겠다. 그런데 뭘 묻는 거지?

“언데드 통제 어쩌구 했던 거.”

- 그거야 당연하지 않나. 본 사령관은 스켈레톤 워로드다. 놈들에 비교하면 당연히…… 어?

짧은 침묵.

나와 같은 생각을 했음이 틀림없다. 마른침을 꿀꺽 삼킨 나는 넌지시 말을 꺼냈다.

“해 봐. 그거.”

- …….

“할래, 소멸할래.”

스켈레톤 워로드가 입을 열었다.

- 자, 자라나라 해골해골…….

그 순간, 치열한 전투를 벌이던 언데드 몬스터들의 신형이 우뚝 멈췄다.

‘……이게 되네.’
```

## Current accepted English baseline

```markdown
# Chapter 380

Shao Shen realized something for the first time.

Krrrrrrrummble!

If you ever witnessed an airplane with both wings engulfed in flames hurtling toward the ground, you would be seized by a terror that transcended species.

- Gaaaaaaaah!

The ogres reputed to be so fearsome screamed. The trolls screamed, too.

- Roooooar!

Even the notoriously sluggish ghouls ran until the soles of their feet sweated.

- Sssssss!

“U-Urgh, uhhh, uhhhhh…”

The monsters that could scream were the lucky ones.

Most of them—including Shao Shen—could only stare at the airplane charging toward the ground, frozen like statues.

*I need to run…*

But his feet and hands would not move.

More importantly, Shao Shen and the Hunters of the Public Security Armed Forces had been surrounded in the middle of the battlefield. They had not even been given a chance to escape.

*Is this really the end?*

The same thought appeared in everyone’s mind at that very moment.

Rrrrrrrumble!

Along with an earsplitting roar, the airplane’s enormous fuselage swept across the battlefield.

That earth-shaking collision began at the very rear of the monster army, which was scattering like a swarm of ants.

Krrrrrunch! Crack!

The massive steel object, weighing dozens of tons, smashed and burst through everything in its path.

The monsters’ green blood spurted like fountains, and limbs of every size flew in all directions.

*W-What the hell is this…?*

No matter how powerful a monster’s physical defenses were, there was a limit. Nothing could stop the airplane now transformed into a monster blender.

- Roooo…

- Kiiiiiiik!

Krrrrrunch!

The eerie sounds of flesh being torn apart swallowed the monsters’ screams. It was a scene of carnage such as Shao Shen had never seen or heard before.

As Shao Shen and the other Hunters stared blankly at the unimaginable sight, someone’s crazed shout pierced their ears.

“Monsters! Ram! Kill!”

“……!”

The Hunters of the Public Security Armed Forces heard their native language loud and clear despite everything happening around them. The word *reinforcements* flashed through their minds, and Shao Shen was stunned.

*An incredible powerhouse!*

The powerful mana carried in that voice. It had to be an S-rank Hunter.

“Go! Go, airplane!”

“……”

And definitely a slightly insane S-rank Hunter.

*To think they’d use a method those island bastards employed back in World War II. Had they not considered that their own allies might die too?*

*He looks like someone dispatched by the Central Military Commission… But did our country even have an S-rank Hunter like that?*

The question suddenly occurred to Shao Shen. But it would soon have nothing to do with him.

The massive steel object that had ground its way through half the battlefield was charging straight toward him and the Hunters.

- S-Sssss!

“Run!”

When it came to struggling for survival, there was no distinction between friend and foe.

Forgetting that there was a human right in front of him, Shao Shen thrust his dagger at the monster crashing into him.

Thud!

- Grrrk.

The dead monster’s body collapsed toward Shao Shen.

Monsters were surging in from every direction, leaving him unable to move even one step. Feeling the immense weight bearing down on him, Shao Shen shouted.

“The battle isn’t over! Fight until the very end!”

He was right. The battle was not over yet. A Hunter was someone who had to kill monsters until the last moment before his own breath ran out.

The Hunters who heard Shao Shen’s shout gritted their teeth and swung their weapons.

*This is enough.*

With lightning-fast skill, Shao Shen drove his dagger into the back of a fleeing ogre’s head, then drew a deep breath.

The enormous airplane was already less than twenty meters away.

Its speed had decreased considerably since the beginning, but with everyone trapped in place, evading it seemed impossible.

*I have no regrets.*

If he died fighting for the people as a proud Hunter of Zhonghua, that was enough.

Shao Shen closed his eyes as screams rained down from every direction.

“Hup.”

Krrrrrunch! Ssssh!

Covered in a sticky liquid that he assumed was blood, Shao Shen thought:

*…Hup?*

*Wouldn’t it normally be “Aagh”?*

The strange sound was hardly an appropriate death cry. Shao Shen cautiously lifted his eyelids.

At last, he saw it.

The airplane had stopped a few steps away, and two men were chatting beside it.

“All right, we’ve arrived. It might explode, so get everyone off quickly.”

“…Mr. Jin Taekyung. Everyone has passed out.”

“Really? How pathetic.”

“…They would have died if not for the barrier magic.”

“Then carry them out, Team Leader Choi. Oh, right. Is that bastard who called us Bangzi[^2] earlier alive, too?”

“Yes. He’s, uh, alive, at least.”

“Then keep a close eye on him. I’m going to give him hell for a long time when we get back.”

“…I’ll do my best.”

Shao Shen could not make sense of the situation at all.

Who, when, where, what, how, and why. Even the five Ws and one H could not organize a scene this bizarre.

*How did the airplane suddenly stop, and who are those people? Were they not Hunters sent by the Central Military Commission?*

The two men were even speaking to each other in a different language.

Shao Shen could not understand the words of the refined-looking man who resembled a young master, but he knew what country the language belonged to.

Their longtime neighbor.

Korea.

*Wait. If he’s Korean…!*

Shao Shen hurriedly wiped the sticky blood from around his eyes. Only then did he recognize one of the men.

A muscular young man a full head taller than everyone else.

The man he had only seen on television—his idol—was standing right in front of him.

“E-Excuse me. Are you Teacher Jin from Korea?”

“Huh?”

The young man, Jin Taekyung, tilted his head as he looked at Shao Shen.

“I’m not a teacher.”

“Then… Sibeol-jwa…”

“…Sibeol. What?”

That was him!

A wave of relief and hope ran through Shao Shen’s entire body, making him tremble.

[^1]: *Sibeol* is a Korean profanity, while *-jwa* is a playful suffix used in a nickname.

[^2]: *Bangzi* is a derogatory Chinese slur for Koreans.

* * *

*How does a Chinese person even know about Sibeol-jwa?*

Articles about me had briefly made a splash in the foreign press, but I had never expected my nickname to spread along with them.

*Sibeol-jwa, whose name makes the five oceans and six continents tremble.*

If I ever went to the United States, maybe some huge Yankee bros would approach me with beer bottles in hand and pretend they knew me.

*Hey, you. Sibeol-jwa?*

*I’m fine, thank you. Sibeol. What kind of deranged bastards came up with a nickname like this?*

Anyway…

“It’s a complete mess.”

That was my brief assessment as I looked around.

Team Leader Choi, who had strung the unconscious flight attendants together like dried fish, and the Skeleton Warlord I had shoved into my inventory both answered.

“It is a horrifying sight.”

- Vile human, I like this place. It feels familiar and strangely pleasant.

“……”

There was no need to say more. A named undead monster who could be called death itself found the scene satisfying.

“We just got here, and we’re already being thrown into actual combat.”

As if responding to my complaint, a System notification rang out.

Ding.

> **System**
>
> - An unexpected Quest, **Unexpected Assault**, has been generated.

*So this is why they said they were paying me so much.*

I clicked my tongue inwardly and spoke.

“Team Leader Choi, protect the civilians first. After that, fight as you see fit. Don’t overdo it.”

“Yes. That was already my intention.”

Team Leader Choi was a smart man. Learning the Jin Family’s Cultivation Technique had made him incomparably stronger than before, but he was not the sort of person who would ever show off.

“And you, young man over there.”

“Y-Yes, Teacher Jin.”

*Teacher, my ass.*

I looked the young man up and down as he answered so promptly.

His face was young, but he was obviously a Hunter. And a powerful one, at that—around A-rank, judging by appearances. Unlike the Hunters around him, who wore identical armor as if they had been stamped out in a factory, he also had a red insignia on his shoulder.

“You look like you hold a decent rank, so keep your men in line. Let’s save as many people as we can.”

“Y-Yes?”

“This is only the beginning.”

As I answered, I thrust out my fist.

KABOOM!

Streams of Scorching Yang Qi shot toward the monsters standing there in a daze.

When the wave of searing heat had passed, dozens of monster corpses were all that remained.

“What are you all staring at? Did someone press the pause button?”

“……!”

- ……!

My words served as the signal.

The silence pressing down on the battlefield shattered.

- Grrrrrrrr!

“K-Kill them! Hold back those monsters!”

Humans and monsters. Monsters and humans.

A battle of killing and being killed began. I pulled White Flame from where it was buried deep in the ground and swung it.

Swish!

This was not a situation of half water and half meat—monsters swarmed in every direction.

A crescent of sword qi extended from the spearhead and grazed a tightly packed mob of monsters.

Ding.

> **System**
>
> - Defeated **Lv. 15 Undead Goblin**!
>
> - Defeated **Lv. 78 Undead Lycanthrope**!
>
> - Defeated **Lv. 93 Dullahan**!
>
> - Defeated **Lv. 30 Skeleton**!
>
> - …
>
> - The Level gap is significant. Gained negligible EXP!

System notifications announcing monster kills and EXP gains rang out without end.

Normally, I would have let such notifications go in one ear and out the other, or simply ignored them.

But this time, they gave me an important clue.

“These guys couldn’t possibly be…”

- Ah, that’s right, vile human! What a powerful undead army!

The Skeleton Warlord’s delighted shout was enough to turn my suspicion into certainty.

*No wonder something felt off.*

I had already been puzzled because I could not sense any life force from them.

A sizeable number of monsters were still alive, but roughly half or more of them were undead. All told, it was an army of close to two thousand monsters.

“And undead monsters are…”

The Skeleton Warlord shouted excitedly.

- Beautiful! Magnificent! Valiant!

Crash!

I cut down five monsters and muttered.

“Do you want to disappear like that guy just now? Beautiful, magnificent, and valiant?”

- ……I misspoke. My apologies, vile human.

The Skeleton Warlord had briefly forgotten his own situation, then hurriedly added:

- Wait. Then they must be under someone’s control!

I thought so, too.

But there was one thing I still could not be certain about…

“The Lich. Did that bastard come out personally?”

- Hmm. If you mean the Lich from that holographic video you showed me last time, then probably not.

As I listened to the Skeleton Warlord’s answer, I took half a step forward.

Boom!

A massive iron club passed dangerously close to my shoulder and smashed into the ground. This was an ordinary ogre, and I could still sense its life force.

- Grrrrrr!

“Sure. I’ll cook you.”

Boom!

The ogre was struck in the chest by a Flame Divine Palm, and black-green blood burst from its seven orifices.

As I passed its collapsing bulk, I slashed White Flame diagonally downward.

Whoooosh! Slash!

Space itself seemed to split apart, and the bodies of the monsters caught between the two halves were sliced to pieces.

Leaving behind a Chinese Hunter staring blankly at me, drenched in blood and bodily fluids, I clenched my fist.

Whoooooom.

A surge of extreme heat raced toward my fist, then shot forward.

KABOOM!

Flame-Annihilating Divine Fist.

A massive pillar of fire swallowed the monsters.

Along with the foul smell of burning flesh, the few monsters that had somehow survived shrieked in agony.

The attack had enough destructive power to make both monsters and Hunters forget to fight for a moment.

The Skeleton Warlord spoke in a stammering voice.

- V-Vile human. You have become even more of a monster.

“It feels weird being called a monster by a monster. But if it’s not the Lich, then what bastard is causing all this chaos?”

- This commander does not know, either. But I can guarantee one thing.

“A guarantee? What?”

- That bastard’s control of the undead is a notch below this commander’s. Hahaha! My army! This commander misses you!

“……”

*Should I kill this bastard or let him live?*

As I was wondering, a thought suddenly flashed through my mind, and I stopped dead.

“Hey. What did you just say?”

- Hahahaha! Did you feel this commander’s majesty, vile human?

“Disappear or talk.”

- ……I will talk. But what are you asking?

“The thing you said about controlling the undead.”

- Isn’t it obvious? This commander is a Skeleton Warlord. Compared to them, naturally… Huh?

A brief silence followed.

He must have had the same thought I did. After swallowing hard, I casually broached the subject.

“Try it. That thing.”

- ……

“Are you going to do it, or do you want to disappear?”

The Skeleton Warlord opened his mouth.

- Grow, grow, skeletons, skeletons…

At that moment, the undead monsters locked in fierce combat abruptly stopped moving.

*…So it works.*
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 380`.

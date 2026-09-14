# Master Edit Task — Chapter 381

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
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 듀라한 | **Dullahan** | Higher undead monster form taken by Yao Wei. |
| 염화일로 | **Flamefire Path** | Named fire-based movement technique used by Jin Taekyung. |
| 데스나이트 | **Death Knight** | Powerful undead being the three beings plan but fail to create. |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 당장은 | polysemy | Right away / for now / at the moment; not the broader “anytime soon.” | anytime soon |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |

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

#### Chapter 379 tail (verified mastered)

…
been thousands of kilometers away invading the airport. “What the hell is going on…?” “We’re going to die. We’re all going to die.” The fear they had briefly forgotten settled over the heads of the People’s Liberation Army once more. Unlike the Hunters of the Public Security Armed Forces fighting on the front lines, they were merely ordinary people carrying modern firearms. And their ominous premonition soon became reality. A nightmare far worse than they had imagined. - Om. Ne. Ha. So. Yu. A voice broken into disconnected syllables. An eerie noise resembling the static of a radio with an unstable signal echoed across the battlefield. Black fog that had rolled in from somewhere spread over the people’s heads. - Yen. Wi. Ga. Ji. Ke! That was when the horrifying change occurred. Swoooooosh! Dark magic as black as storm clouds spread like a web through the blood and corpses. It breathed new strength and souls into bodies that were growing cold, then bound them in chains and enslaved them. Snap. Snap-snap. An army of skeletons rose slowly from the pools of death, granted new life. *Those beings* had woven countless dead together with invisible chains and made them their slaves. They laughed in satisfaction. - Kik, kikikik. - Grrk. Kihihihi. * * * - Grrrrr. With a bubbling sound, a man rose to his feet. Clad in armor bearing the Five-Star Red Flag and carrying a massive ax, he looked exactly like the A-rank Hunter Shao Shen remembered. *…Mr. Yao Wei.* But Shao Shen could not call the man’s name aloud. He could not bring himself to. He knew the figure before him was no longer the person he had known. *Ah… ahhh.* If Shao Shen had not witnessed the man’s decapitation a little over ten minutes earlier, if he had not seen him rise with his severed head tucked beneath his arm, Shao Shen would have thought of him as a comrade and friend. But Yao Wei no longer existed. His new name slipped from Shao Shen’s lips. “Dullahan…” A headless knight. A Dullahan. Shao Shen bit his lip at the sight of his comrade reborn as a higher undead monster. Something hot ran down his cheek. “I’m sorry. I really am.” - Grrrrraaaah! The Dullahan charged with a roar, and Shao Shen shot forward like the wind. In the past, the two of them had often sparred like this. Their bouts had begun with nothing more than competitive pride and continued day after day. Once each spar ended, Shao Shen had to put up with Yao Wei’s complaints. *You little brat. No manners, none at all. Would it kill you to let me win once?* *Ha-ha. Let’s go get something to eat. The loser pays, so I guess you’re buying again today, Mr. Yao Wei.* *Your family’s loaded, and you’re still so cheap. One day, I’ll make you buy me a meal.* But that had never happened before, and now it never would. Shao Shen had always won. *Goodbye. Thank you for everything.* Whoosh! Slash! The ax cut through empty air. Aura surged from Shao Shen’s spear point and cleaved through the Dullahan’s upper body. A cut line appeared, starting at his waist. The headless knight’s body slowly crumpled. Thud. Slump. Shao Shen stared blankly down at the face of the fallen Dullahan—no, Yao Wei. His eyes burned. “How dare you… How dare you do this…” Friends and comrades who had been laughing and joking with him only half a day ago had become undead monsters. The Hunters of the Public Security Armed Forces were famous for their strict discipline, but they were not cold-blooded people without a drop of human feeling. The Hunters who had entered the battle prepared to die now faced the fear of human attachment for the first time. “Wake up! It’s me, Ryu Inchin! Ryu Inchin!” “H-Hyung…!” - Grrrrr! Crunch! Boom! Screams and death rained down from every direction. Unlike the Public Security Armed Forces, which had suffered casualties approaching half its strength, the monster army had increased its numbers and continued to surge forward without end. *Am I going to die here, like this?* For the first time in his life, Shao Shen thought about death. The situation was desperate enough to make even someone as bright and cheerful as him think that way. *We didn’t receive any warning signal, so communications must be down. There won’t be any reinforcements either… This really is the end.* Slash! Shao Shen cut down one charging undead monster after another, then laughed hollowly and looked up at the sky. The sunset was surprisingly beautiful. When the sun went down and darkness arrived, he would never see a sight like this again. *Thankfully, it's not so bad for the last sky I'll ever see…* Huh? Shao Shen blinked, unable to finish the thought. Something unimaginably enormous was rapidly approaching the battlefield from high above. *An airplane?* Whoooooom! A massive aircraft engulfed in flames. And someone’s shout rang across the vast sky. “Hey! Monsters!” “…?” - …? *Am I hearing things?* Shao Shen was not the only one looking up. Everyone on the battlefield raised their eyes toward the sky. A voice that seemed even to carry madness thundered across the battlefield. “I’m going to ram it!” *Ram what?* Shao Shen soon realized what the voice meant. Rrrrrumble! The airplane’s massive fuselage swept straight across the battlefield.

#### Chapter 380 tail (verified mastered)

…
as he answered so promptly. His face was young, but he was obviously a Hunter. And a powerful one, at that—around A-rank, judging by appearances. Unlike the Hunters around him, who wore identical armor as if they had been stamped out in a factory, he also had a red insignia on his shoulder. “You look like you hold a decent rank, so take care of your men. Let’s save as many people as we can.” “Y-Yes?” “This is only the beginning.” As I answered, I thrust out my fist. KABOOM! Streams of Scorching Yang Qi shot toward the monsters standing there in a daze. Once the wave of searing heat had swept past, only dozens of monster corpses remained. “What are you all staring at? Did someone press the pause button?” “……!” - ……! My words served as the signal. The silence pressing down on the battlefield shattered. - Grrrrrrrr! “K-Kill them! Hold back those monsters!” Humans and monsters. Monsters and humans. A battle of killing and being killed began. I pulled White Flame from where it was embedded deep in the ground and swung it. Swish! Forget waters so crowded they were half water and half fish—monsters were swarming everywhere. A crescent of sword qi extended from the spearhead and grazed a tightly packed mob of monsters. Ding. > **System** > > - Defeated **Lv. 15 Undead Goblin**! > > - Defeated **Lv. 78 Undead Lycanthrope**! > > - Defeated **Lv. 93 Dullahan**! > > - Defeated **Lv. 30 Skeleton**! > > - … > > - The Level gap is significant. Gained negligible EXP! System notifications announcing monster kills and EXP gains rang out without end. Normally, I would have let them go in one ear and out the other, or simply ignored them. But this time, they gave me an important clue. “Don’t tell me these guys are…” - Ah, that’s right, vile human! What a powerful undead army! The Skeleton Warlord’s delighted shout was enough to turn my suspicion into certainty. *No wonder something felt off.* I had already been wondering why I could not sense any life force from them. A sizeable number of monsters were still alive, but roughly half or more of them were undead. All told, it was an army of close to two thousand monsters. “And undead monsters are…” The Skeleton Warlord shouted excitedly. - Beautiful! Magnificent! Valiant! Crash! I cut down five monsters and muttered. “Do you want to disappear like that guy just did? Beautifully, magnificently, and valiantly?” - ……I misspoke. My apologies, vile human. The Skeleton Warlord had briefly forgotten his own situation. He hurriedly added: - Wait. Then they must be under someone’s control! I thought so, too. But there was one thing I still could not be certain about… “The Lich. Did that bastard come out personally?” - Hmm. If you mean the Lich from that holographic video you showed me last time, then probably not. As I listened to the Skeleton Warlord’s answer, I took half a step forward. Boom! A massive iron club passed dangerously close to my shoulder and smashed into the ground. This was an ordinary ogre, and I could still sense its life force. - Guwooooo![^3] “Yeah, I’ll roast you.” [^3]: The ogre’s roar, *guwo*, is also Korean for “roast it.” Boom! The Flame Divine Palm struck the ogre in the chest, and black-green blood erupted from all seven of its orifices. As I passed its collapsing bulk, I slashed White Flame diagonally downward. Whoooosh! Slash! Space split apart, and the bodies of the monsters caught between the two halves were sliced to pieces. Leaving behind a Chinese Hunter who stared blankly at me, drenched in blood and bodily fluids, I clenched my fist. Whoooooom. A surge of extreme heat raced toward my fist, then shot forward. KABOOM! Flame-Annihilating Divine Fist. A massive pillar of fire swallowed the monsters. Along with the foul smell of burning flesh, the few monsters that had somehow survived shrieked in agony. The attack had enough destructive power to make both monsters and Hunters forget to fight for a moment. The Skeleton Warlord stammered. - V-Vile human. You have become even more of a monster. “It feels weird being called a monster by a monster. But if it’s not the Lich, then what bastard is causing all this chaos?” - This commander does not know, either. But I can guarantee one thing. “Guarantee? What?” - That bastard’s control of the undead is a notch below this commander’s. Hahaha! My army! This commander misses you! “……” *Should I kill this bastard or let him live?* As I was wondering, a thought suddenly flashed through my mind, and I stopped dead. “Hey. What did you just say?” - Hahahaha! Did you feel this commander’s majesty, vile human? “Disappear or talk.” - ……I will talk. But what are you asking? “That thing you said about controlling the undead.” - Isn’t it obvious? This commander is a Skeleton Warlord. Compared to them, naturally… Huh? A brief silence followed. He must have had the same thought I did. I swallowed hard, then casually broached the subject. “Try it. That thing.” - …… “Are you going to do it, or do you want to disappear?” The Skeleton Warlord opened his mouth. - Grow, grow, skeletons, skeletons… At that moment, the undead monsters locked in fierce combat abruptly stopped moving. *…So it works.*

## Korean source

```text
＃381화



솨아아아.

보이지 않는다. 그러나 느껴진다. 나를 중심으로, 아니 인벤토리라는 아공간에 존재하는 스켈레톤 워로드로부터 흘러나온 끈적한 기운이 사방으로 뻗어 나가는 것이.

변화는 순식간에 일어났다.

- 키릭?

- 구워?

흉포하기 그지없던 몬스터들의 움직임이 우뚝 멈췄다.

오크, 트롤, 고블린, 라이칸스로프와 몬스터 백과사전에서나 보던 온갖 종류의 몬스터와 전사한 헌터들까지.

놈들의 공통점은 단 하나, 이미 한 번 죽어 언데드로 부활했다는 점이었다.

꿀꺽.

마른침을 삼킨 내가 중얼거렸다.

“이게 되네.”

- 와, 이게 진짜 되네.

“……?”

- ……?

아니, 지금 뭐라고?

순간 뇌정지가 온 나는 작게 속삭였다.

“무슨 개뼈다귀 같은 소리야. 당연히 되니까 한 거 아니었어?”

스켈레톤 워로드가 우물쭈물 대답했다.

- 그게 사실…… 본 사령관도 이렇게 쉽게 될 줄 몰랐다.

“네 통제력이 훨씬 높다면서?”

- 아, 그건 홧김에 그냥 해 본 말인데.

“뭐?”

- 가만히 있기에는 자존심이 상해서…….

“…….”

이거 완전 미친놈 아냐.

어이가 없었지만, 그것과는 별개로 결과는 확실했다.

반경 수십 미터에 존재하던 언데드 몬스터들이 일시에 움직임을 멈추자 주위에서 벌어지던 치열한 전투도 잠시 소강상태에 빠진 것이다.

「모, 몬스터들이 움직임을 멈췄다!」

「이게 도대체 무슨 상황이지?」

「방심하지마! 아직 움직이는 놈들이 있다!」

누군가의 외침대로, 방심하기에는 아직 일렀다.

스켈레톤 워로드의 통제에 들어온 것은 근처의 일부 언데드 몬스터일 뿐, 멀리 떨어져 있거나 언데드 상태가 아닌 일반 몬스터의 경우는 예외였으니까.

- 우워어어어!

- 취이익!

“흐아아압!”

카가가강! 푸푹!

갑작스러운 동족의 변화에 어리둥절하던 것도 잠시, 통제가 되지 않는 몬스터들이 재차 날뛰기 시작하자 다시금 전투가 시작되었다.

머릿수에서부터 비교가 되지 않는 싸움. 그러나 지금 이 순간부터는 달라질 것이다.

나는 한껏 숨죽인 목소리로 외쳤다.

“가라, 워로드몬!”

발끈한 워로드몬, 아니 스켈레톤 워로드가 외쳤다.

- 간악한 인간이여! 본 사령관을 그렇게 부르지 말라!

“그럼 소멸하고 싶어서 환장한 워로드몬?”

- ……빌어먹을.

숨도 못 쉬는 해골 주제에 한숨을 푹 내쉬더니 이내 마법의 주문을 외운다.

- 싸워라, 해골해골.

저놈도 해골해골에 재미가 들린 게 틀림없다. 별 우습지도 않은 주문이었지만 효과는 확실했다.

- 구워?

스켈레톤 워로드의 명령에, 멍하니 풀려 있던 언데드 몬스터들의 눈동자에 흉포함이 서린다. 그리고 다음 순간.

콰직!

언데드 오우거의 쇠몽둥이가 어느 트롤의 머리통을 부수는 것을 시작으로, 새로운 주인을 섬기게 된 언데드 몬스터들이 동족을 향해 달려들었다.

- 쿠워어어어!

- 취, 취릭?

빠각! 서걱! 푸푸푹!

등 뒤에서 벌어진 예상치 못한 아군의 기습. 중국 헌터들을 포위하고 있던 몬스터 군단의 한 축이 속절없이 허물어졌다.

- 취이이익!

「뭐, 뭐야!」

「갑자기 저놈들이 왜……?」

당황한 것은 동족에게 배신당한 몬스터들 뿐만이 아니었다.

갑작스러운 상황에 얼떨떨해하는 중국 헌터들. 나는 그들의 선두에서 줄곧 종횡무진 창을 휘두르던 청년 헌터를 향해 외쳤다.

“샤오 쉔!”

「지, 진 선생님?」

동그래진 눈동자가 나를 바라봤다.

「어, 어떻게 제 이름을?」

방금 [기감]으로 레벨 창을 확인해서 알게 된 거지만, 지금은 그게 중요한 게 아니다.

“뭐 합니까! 적극 공세로 전환하지 않고.”

「그런데 이 상황은 도대체…….」

“지금 그게 그렇게 궁금해요? 언데드 몬스터 하나 붙잡고 육하원칙에 따라 왜 우리를 돕는지 설명을 듣고 싶어?”

「아, 아닙니다!」

“그럼 이제 어떻게 해야 될까?”

정신이 번쩍 든 샤오 쉔이 창을 번쩍 치켜들었다.

「공격 대형! 공안 무력부 전원, 지금부터 언데드 몬스터들을 제외한 나머지를 친다!」

「옛!」

훌륭한 판단의 표본이로군.

하나가 된 외침과 함께 궁지에 몰려 있던 오백여 명의 헌터들의 기세가 바뀌었다.

「죽여!」

「동지들의 원한를 갚아라!」

쉬쉬쉬쉭, 서걱!

- 아우우우!

막 오크의 목을 잘라낸 헌터를 향해 달려드는 라이칸스로프.

누런 송곳니로 목줄기를 물어뜯으려는 놈의 아가리를 거대한 주먹이 후려쳤다.

콰직!

- 그워어어어!

라이칸스로프의 두개골을 박살 낸 오우거가 흉포한 함성을 내질렀다. 그런 오우거의 머리 위로 급강하한 그리폰의 날카로운 발톱이 번쩍 빛을 발했다.

- 끼이이이익!

날카로운 괴성. A급 몬스터의 마력이 실린 발톱이 오우거의 안구를 할퀴려던 그 순간.

「아이스 볼!」

「라이트닝 볼트!」

대기하고 있던 원거리 헌터들의 마법에, 감전된 그리폰이 허공에서 몸을 부르르 떨었다.

바로 그때, 트롤의 어깨를 밟고 솟구친 한 인영이 그리폰을 향해 무기를 휘둘렀다.

“독일 최고의 무기 공방으로 손꼽히는 J사에서 특별 제작한……!”

서걱!

군더더기 없이 깔끔한 일격이 그리폰의 머리를 가른다.

우아하게 착지한 최 팀장이 피 한 방울 묻지 않은 투명한 검신을 바라보며 흡족하게 웃었다.

“경매가 52억에 낙찰받은 롱소드. 역시 제값을 하는군.”

“…….”

병신 같은데 멋있어. 멋있긴 한데 병신 같아.

그 광경을 지켜보던 스켈레톤 워로드가 떨떠름한 목소리로 물었다.

- 간악한 인간이여, 저 인간이 네 상관이라고 했나?

“아니, 그. 길드 내부 직책상으로 따지면 그렇긴 한데…….”

- 인간치고는 제법 똑똑해 보였는데, 별 괴상한 인간을 다 보겠군. 과연 네 녀석의 상관답다.

“혓바닥 잘못 놀려서 소멸하고 싶은 스켈레톤 워로드 손?”

짧게 침묵한 스켈레톤 워로드는 주문을 외는 것으로 대답을 대신했다.

- 자라나라, 해골해골!

서당 개 삼 년이면 풍월을 읊는다고, 이제는 시키지 않아도 알아서 잘한다.

투둑, 투두두둑.

최 팀장에게 죽은 그리폰이, 헌터와 언데드의 합공에 의해 쓰러진 몬스터들이 새로운 생명을 얻으며 죽은 육신을 일으켜 세운다.

그 숫자가 무려 이백. 처음 시도했던 것에 비해 범위도 더욱 넓어졌는지, 저 멀리에 있는 언데드 몬스터들도 스켈레톤 워로드의 통제에 들어와 아군을 공격하기 시작했다.

“와. 너 이 정도였냐?”

- 와. 본 사령관이 이 정도였나?

“…….”

- ……사실 이 정도까지는 아니었다. 하지만 어째서인지는 몰라도, 이곳에 오니 엄청난 마력이 솟구치는구나!

“어, 그래.”

나는 이 괴상한 네임드 몬스터를 이해하기를 포기했다.

하긴 결과만 좋으면 됐지, 지금 당장은 따져 봤자 머리만 아플 것 같다.

- 많은, 더 많은 군단을 내게 다오!

인벤토리에 넣어 둔 터라 보이지는 않지만, 뼈 밖에 안 남은 두개골을 부르르 떨고 있을 것이 분명했다.

나는 한숨을 내쉬며 창을 말아쥐었다.

“안 그래도 그럴 생각이야.”

- 방법이 있나?

“있지.”

더 많은 언데드를 늘리는 방법? 간단하다.

“싹 다 죽이면 돼.”

- 크하하하! 너는 실로 간악하고도 무식한 인간이로구나!

건방진 녀석. 하지만 이번만큼의 놈의 말에 일부분 동의할 수밖에 없다.

머릿속에 울려 퍼지는 스켈레톤 워로드의 광소를 들으며, 나는 걸음을 내디뎠다.

‘염화일로(炎火一路)’

화아아악!

발걸음을 따라, 불꽃의 길이 열렸다.



* * *



새카만 로브와 해골이 주렁주렁 매달린 지팡이. 동공이 있어야 할 그곳은 텅 비어 있었고 몸에는 아직 썩지 않은 살점이 붙어 있었다.

악몽에나 나올 법한 모습을 한 세 존재는 서로를 향해 의념(疑念)을 전달했다.

- 문제가 생겼군.

- 언데드 몬스터들이 통제를 벗어나고 있다. 인간을 도와 군단을 공격하고 있어.

- 어째서?

통제를 벗어나게 한 방법을 묻는 것이 아니다. 그들 세 존재는 이미 그 물음에 대한 답을 알고 있었으니까.

- 상위 언데드다. 우리보다 강력한.

모든 몬스터는 우열이 있지만, 그중에서도 특히 언데드는 철저한 힘의 지배를 받는다.

지금처럼 통제력을 빼앗겼다면 그것은 필시 상위의 존재가 벌인 소행이었다.

- 하지만…….

- 어떻게 그럴 수 있지?

세 존재 중 그 물음에 답할 수 있는 자는 아무도 없었다.

도대체 어찌 자신들보다 강력한 존재가 이곳에 있으며, 언데드의 통제권을 빼앗아 인간을 돕는단 말인가.

- 설마 ‘그분’께서?

- 말도 안 되는 소리. 그분께서 우리를 보내며 내리신 명령을 잊었는가?

- 인간을 죽여라. 더 많은 언데드와 군단을 만들어 더, 더 많은 인간을 죽여라.

명령을 다시금 떠올린 세 존재는 작은 혼란에 빠졌다.

그분, 아크 리치(Arch Lich)가 아니라면 그 누가 자신들의 통제력을 뛰어넘을 수 있단 말인가.

- 인간들 중 네크로맨서가 있었나?

- 아무것도 느끼지 못했다.

- 인간은 죽음을 배척하고 혐오하지. 그럴 리 없어. 설령 있더라도 우리에 비할 바는 아니다.

의념에서 숨길 수 없는 적의(敵意)가 느껴지는 까닭은, 그들 역시 한때 인간의 배척과 멸시를 한 몸에 받았던 네크로맨서였기 때문이었다.

하지만 그것은 이미 아득한 과거이며 또 다른 차원에서 있었던 일.

죽음이라는 망망대해를 표류하던 그들은 아크 리치라는 뱃사공을 만났고, 새로운 힘을 얻어 그토록 염원하던 리치(Lich)로 발돋움하려 하고 있었다.

그러나…….

- 아쉽군.

- 변화가 완전히 끝났더라면. 이 땅에 더 많은 죽음이 있었다면.

- 그럼 통제력을 빼앗기는 일 역시 없었겠지.

세 존재는 안타까움을 금치 못했다.

살아생전 위대한 네크로맨서였던 그들은 아직 완전한 리치로 거듭나지 못한 상태였다.

죽은 마법사의 몸을 빌려 새롭게 태어나기는 했으나, 일주일이라는 시간은 리치로 변화하기 위한 사기(死氣)를 흡수하기에는 너무나도 짧았다.

- 그렇기에 그분께서 우리 셋을 보낸 것인데.

- 이 일이 실패로 돌아간다면 실망하실 거다.

- 우리에게 주신 힘을 도로 빼앗으실지도 몰라.

그건 세 존재가 가장 두려워하는 일이었다.

아크 리치의 신임을 얻기 위해서라면 어떻게든 이 난관을 헤쳐나가야 했다. 설령 극심한 힘을 소모하더라도.

- 어쩔 수 없지.

- 힘을 합치자는 말인가?

- 그렇다. 우리 셋이 힘을 합친다면, 정체를 알 수 없는 상위 언데드도 더는 통제력을 빼앗을 수 없을 것이다.

- 으음. 좋다.

- 동의하는가?

- 동의한다.

아크 리치의 총애를 얻기 위해 경쟁하던 세 존재는 마침내 합의점을 찾았다.

그들은 망설임 없이 사령의 주문을 외우기 시작했다.

- 바렌시아. 마드릿.

- 바이엘른. 뮌헨.

- 스토흐. 시리.

세 존재로부터 흘러나온 죽음의 기운이 대기를 타고 뻗어 나갔다.

푸른 잔디가 까맣게 물들고, 범위에 들어와 있던 인민 해방군 소속의 병사들이 목을 움켜쥐고 쓰러졌다.

“컥!”

“크허억!”

쏴아아악.

단말마와 함께 숨이 끊긴 인간들의 몸에서 흘러나온 사기는 몬스터들의 전신에 스며들었다.

- 캬우우우우!

- 그워어어!

흉포한 외침에 실린 강력한 마력에 주위의 공기가 요동쳤다. 그 힘은 일반적인 몬스터와는 비교도 할 수 없을 정도였다.

강화된 통제력과 휘하 몬스터들의 힘을 느낀 세 존재는 그제야 주문을 멈추었다.

- 키키키키킥.

- 성공이다.

- 엄청난 힘을 소비하긴 했지만…… 이 정도면 차고 넘치는 수준이지.

세 존재가 더욱 강력해진 자신들의 군단을 바라보며 만족스럽게 웃던 그때.

꽈앙!

저 멀리, 굉음과 함께 몬스터의 사지가 날아올랐다.

세 존재는 솟구치는 불꽃을 바라보며 대화를 나누었다.

- 화염 마법사가 있나 보군. 제법인데?

- 그래 봤자 인간이다. 스켈레톤 메이지들을 대거 투입하도록 하지.

- 좋은 생각이야.

그리고 잠시 후, 다시금 솟구치는 화염에 세 존재는 서로를 바라보았다.

- 방금. 뭐였지?

- 통제력이 끊겼다. 빼앗긴 건 아니야.

- 소멸시켰다고? 제법이군.

- 그런데 정말 마법사가 맞나? 움직임이 너무 빠른 것 같은데…….

- 음. 오우거 부대를 투입 시키자.

- 오우거 받고, 듀라한 더.

- 듀라한까지? 그럼 우리들의 호위는 누가 맡지?

- 그의 말이 맞다. 듀라한은 너무 과해. 강화된 오우거로 충분하다.

- 그렇긴 하지.

그리고 삼 분 후.

세 존재의 두개골 위로는 심각한 공기가 어렸다.

- 끊겼다.

- 또?

- 그러게 듀라한 보내자니까.

- 저거 도대체 뭐지. 마법사 아닌 것 같은데.

- 아, 일단 듀라한부터 보내자고!

- 그, 그러도록 하지.

호위부대로 삼은 듀라한 이십여 마리가 우르르 사라지는 모습을 보며, 세 존재는 슬그머니 또 다른 합의점을 찾기 시작했다.

- 음. 그런 일이 벌어지지는 않겠지만 혹시…….

- 나도 비슷한 생각을 했다.

- 데스나이트(Death Knight)…… 만들까?

- 이미 너무 많은 힘을 소비했는데 데스나이트까지? 재료도 마땅치 않고, 시간도 오래 걸릴 텐데.

- 급한 대로 가장 쓸 만한 놈을 골라서 만들면 된다. 우리 셋이 힘을 합친다면 가능해.

- 그, 그럼 시도는 해 볼까.

그러나 세 존재의 데스나이트 제작 계획은 채 십 분도 지나지 않아 산산조각 나고 말았다.

화륵, 콰아아앙!

뼈밖에 남지 않은 몸으로도 느낄 수 있는 초고온의 열기.

“시벌 놈들. 더럽게 많네.”

콰드드득!

겁화(劫火)에 휩싸인 창을 휘두르며 몬스터 군단을 박살 내는 존재를 목격한 세 존재는 황급히 주문을 외웠다.

느릿느릿하던 목소리는 랩처럼 빨라져 있었다.

- 옴느하소유!

- 옌위가지케!

그러나 주문이 완성되기도 전에, 화염 마법사인지 전사인지 분간이 되지 않는 젊은 인간은 그들의 코앞에 도착해 있었다.

“어, 반갑다.”

- 오, 옴느하소유!

- 예, 옌위가지케!

청년, 진태경이 삐딱하게 고개를 꺾었다.

“안녕하세요. 연예가중계? 병신들인가.”
```

## Current accepted English baseline

```markdown
# Chapter 381

Swoooosh.

I couldn’t see it. But I could feel it. Centered on me—or rather, flowing from the Skeleton Warlord inside the subspace called my inventory—a sticky energy spread in every direction.

The change happened in an instant.

- Krrik?

- Guwo?

The movements of the utterly savage monsters abruptly stopped.

Orcs, trolls, goblins, lycanthropes, every kind of monster I had only ever seen in monster encyclopedias, and even the fallen Hunters.

They had just one thing in common: they had already died once and been resurrected as undead.

Gulp.

I swallowed dryly and muttered.

“This actually works.”

- Wow. It really works.

“……?”

- ……?

*Wait, what did you just say?*

My brain froze for a moment. Then I whispered:

“What kind of boneheaded nonsense was that? Didn’t you do it because you knew it would work?”

The Skeleton Warlord answered sheepishly.

- The truth is… this commander didn’t know it would be this easy.

“You said your control was much stronger.”

- Ah, that? I only said it because I was angry.

“What?”

- I was too proud to just sit there doing nothing…

“……”

*Is this guy completely insane?*

It was absurd, but the result was undeniable.

The undead monsters within a radius of several dozen meters all stopped moving at once, and the fierce battle raging around us briefly fell into a lull.

“Th-The monsters have stopped moving!”

“What on earth is happening?”

“Don’t let your guard down! Some of them are still moving!”

As someone shouted, it was still too soon to relax.

The Skeleton Warlord had only taken control of some of the nearby undead monsters. Those farther away, as well as the ordinary monsters that were not undead, were exceptions.

- Roooooar!

- Kreeeek!

“Haaaaah!”

Clang! Stab!

The uncontrolled monsters were bewildered for only a moment by the sudden change in their own kind before they began rampaging again.

The battle resumed.

It was a fight where the two sides could not even be compared in terms of numbers. But from this moment on, things would be different.

I shouted in a hushed voice.

“Go, Warlordmon!”

The Warlordmon—no, the Skeleton Warlord—shouted angrily.

- You vile human! Do not call this commander that!

“Then what about Warlordmon, who’s dying to disappear?”

- ……Damn it.

Despite being a skeleton that couldn’t even breathe, he let out a deep sigh before beginning to chant a spell.

- Fight, skeleton skeleton.

That bastard had clearly gotten hooked on “skeleton skeleton.” It was an absurdly stupid incantation, but its effect was undeniable.

- Guwo?

At the Skeleton Warlord’s command, ferocity filled the eyes of the undead monsters that had been staring blankly into space.

Then, in the next moment—

Crunch!

An undead ogre’s iron club crushed a troll’s skull.

That was the beginning.

The undead monsters who now served a new master charged toward their former allies.

- Guwoooooo!

- K-Kreeek?

Crack! Slash! Stab-stab-stab!

It was an unexpected ambush from behind.

One flank of the monster army surrounding the Chinese Hunters collapsed helplessly.

- Kreeeeeeek!

“What the hell?!”

“Why are they suddenly…?”

The monsters betrayed by their own kind were not the only ones thrown into confusion.

The Chinese Hunters were bewildered by the sudden turn of events, too. From the front of their formation, I shouted at the young Hunter who had been swinging his spear all over the battlefield.

“Shao Shen!”

“T-Teacher Jin?”

His widened eyes turned toward me.

“How do you know my name?”

I had just checked his Level window using Qi Sense, but that was not important right now.

“What are you doing? Why haven’t you switched to an all-out attack?”

“But what exactly is happening…?”

“Are you really that curious right now? Do you want to grab an undead monster and make it explain why it’s helping us according to the five Ws and one H?”

“No, sir!”

“Then what should we do now?”

Shao Shen suddenly came to his senses and raised his spear high.

“Attack formation! Everyone in the Public Security Armed Forces, attack everything except the undead monsters from this moment onward!”

“Yes, sir!”

*An excellent example of sound judgment.*

With one unified shout, the momentum of the five hundred or so Hunters who had been cornered changed.

“Kill them!”

“Avenge our fallen comrades!”

Swish-swish-swish! Slash!

A lycanthrope charged toward a Hunter who had just cut through an orc’s neck.

The monster opened its jaws, yellow fangs aiming to tear out the Hunter’s throat—but a huge fist slammed into its mouth.

Crunch!

- Grrrrrrr!

The ogre that had crushed the lycanthrope’s skull let out a savage roar.

At that moment, the sharp claws of a griffin diving toward the ogre flashed above its head.

- Screeeeeech!

The griffin let out a piercing cry. Its claws, charged with the mana of an A-rank monster, were just about to rake across the ogre’s eyes when—

“Ice Ball!”

“Lightning Bolt!”

The griffin convulsed in midair after being struck by the spells of the ranged Hunters waiting nearby.

Right then, a figure launched himself upward after stepping on a troll’s shoulder and swung his weapon at the griffin.

“Specially made by J Company, widely regarded as one of Germany’s finest weapon workshops…!”

Slash!

The clean, no-frills strike split the griffin’s head in two.

Team Leader Choi landed gracefully and gazed at the transparent blade, which did not have a single drop of blood on it. He smiled with satisfaction.

“The longsword I won for 5.2 billion won at auction. It really was worth the price.”

“……”

*He looks like an idiot, but he’s cool.*

*He’s cool, but he looks like an idiot.*

The Skeleton Warlord, who had watched the scene, asked in a dubious voice:

- Vile human, you said that man was your superior?

“Technically, yes, in terms of internal Guild positions, but…”

- He looked fairly intelligent for a human. I’ve seen all kinds of strange humans, but this one truly suits you as a superior.

“Raise your hand if you’re a Skeleton Warlord who wants to be annihilated for running his mouth.”

After a brief silence, the Skeleton Warlord answered by chanting another spell.

- Grow, skeleton skeleton!

After three years at a village school, even a dog can recite poetry. By now, he could do it without being told.

Tuk. Tuk-tuk-tuk.

The griffin killed by Team Leader Choi, along with the monsters brought down by the combined attacks of the Hunters and the undead, gained new life and hauled their dead bodies back to their feet.

There were two hundred of them.

The range seemed to have grown even wider compared to his first attempt. Even the undead monsters far away had come under the Skeleton Warlord’s control and begun attacking their former allies.

“Wow. You were this strong?”

- Wow. Was this commander really this strong?

“……”

- ……Actually, this commander was not this strong before. But for some reason, an incredible amount of mana is surging through this place!

“Uh-huh. Good for you.”

I gave up on trying to understand this bizarre named monster.

The important thing was the result. Trying to figure it out right now would only give me a headache.

- Give me a larger legion. A larger one!

I couldn’t see him because he was inside my inventory, but I was certain his skull—which had nothing left but bones—was trembling with excitement.

I sighed and tightened my grip on my spear.

“I was already planning to.”

- Is there a way?

“There is.”

The method for increasing the number of undead was simple.

“You just have to kill every last one of them.”

- Hahahaha! You truly are a vile and brainless human!

*What an arrogant bastard.*

Still, this time, I couldn’t help agreeing with part of what he said.

As the Skeleton Warlord’s mad laughter echoed through my head, I took a step forward.

*Flamefire Path.*

Whoooooosh!

A path of flame opened beneath my footsteps.

* * *

Black robes. A staff with skulls hanging from it.

The places where their pupils should have been were empty, and pieces of flesh that had not yet rotted still clung to their bodies.

The three beings looked as though they had stepped out of a nightmare. They exchanged thoughts with one another.

- A problem has arisen.

- The undead monsters are breaking free of our control. They are helping the humans and attacking the legion.

- Why?

They were not asking how the undead had escaped their control.

The three beings already knew the answer to that question.

- A higher undead. One more powerful than us.

All monsters had a hierarchy of strength, but the undead in particular were ruled completely by power.

If control had been taken away as it had now, it was undoubtedly the work of a superior being.

- But…

- How is that possible?

None of the three beings could answer.

How could an existence more powerful than them be here? How could it steal control of the undead and use them to help the humans?

- Could it be *Him*?

- Don’t be ridiculous. Have you forgotten the order He gave us when He sent us here?

- Kill the humans. Create more undead and a larger legion, then kill more and more humans.

Remembering the order, the three beings fell into a brief state of confusion.

If it was not Him—the Arch Lich—who could possibly surpass their control?

- Was there a necromancer among the humans?

- I sensed nothing.

- Humans reject and hate death. It is impossible. Even if there were one, they would be no match for us.

The reason unmistakable hostility could be felt in their thoughts was that they, too, had once been necromancers who had borne the full weight of human rejection and contempt.

But that had been an unimaginably long time ago, in another dimension.

They had drifted across the boundless sea of death until they encountered a ferryman named the Arch Lich. They gained new power and were now trying to become the Liches they had long yearned to be.

However…

- What a shame.

- If only the transformation had been completed. If only there had been more death in this land.

- Then we would not have lost control, either.

The three beings could not hide their regret.

They had been great necromancers in life, but they had not yet fully transformed into Liches.

They had been reborn by borrowing the bodies of dead mages, but one week was far too short to absorb the death energy needed to transform into Liches.

- That is why He sent the three of us.

- He will be disappointed if this fails.

- He may even take back the power He gave us.

That was what the three beings feared most.

They had to overcome this crisis somehow if they wanted to earn the Arch Lich’s trust—even if it meant expending a tremendous amount of power.

- It cannot be helped.

- Are you suggesting that we join forces?

- Yes. If the three of us combine our power, even this unidentified higher undead will no longer be able to take control from us.

- Hmm. Very well.

- Do you agree?

- I agree.

The three beings had been competing to earn the Arch Lich’s favor, but at last they found common ground.

Without hesitation, they began chanting a necromantic spell.

- Barensia. Madrit.[^1]

- Baielrn. Munich.

- Stoh. Siri.

[^1]: The pseudo-incantation mangles the names Valencia, Madrid, Bayern Munich, and Stoke City.

The energy of death flowing from the three beings spread through the air.

The green grass turned black, and the soldiers of the People’s Liberation Army caught within its range clutched their throats and collapsed.

“Urk!”

“Ghhurk!”

Ssshhhhhh.

The death energy flowing from the bodies of the humans who had died with those final cries seeped into every inch of the monsters.

- Kyaaaaaaa!

- Grrrrrrr!

The air shook beneath the powerful mana contained in their savage cries. Their strength was beyond comparison with ordinary monsters.

Only after sensing the enhanced control and the increased strength of the monsters under their command did the three beings stop chanting.

- Kikikikikik.

- It worked.

- We expended an enormous amount of power, but… this is more than enough.

The three beings were gazing with satisfaction at their strengthened legion when—

BOOM!

Far away, a monster’s limbs flew through the air with a thunderous explosion.

The three beings looked toward the flames surging into the sky.

- There appears to be a fire mage. Not bad.

- It is still only a human. Deploy a large number of Skeleton Mages.

- A good idea.

A short while later, flames surged into the sky again.

The three beings looked at one another.

- Just now. What was that?

- The control was cut off. It was not stolen.

- Did it annihilate them? Impressive.

- But is that really a mage? Its movements seem too fast…

- Let’s deploy the ogre unit.

- I’ll see your ogres and raise you Dullahans.

- More Dullahans? Then who will guard us?

- He has a point. Dullahans are excessive. Strengthened ogres will be enough.

- That is true.

Three minutes later, a grim atmosphere hung over the three beings’ skulls.

- It was cut off.

- Again?

- That is what I said. We should send Dullahans.

- What the hell is that? It does not seem to be a mage.

- I said we should send Dullahans first!

- Th-Then let us do that.

Watching the twenty or so Dullahans they had selected as an escort troop disappear in a group, the three beings cautiously began searching for another point of agreement.

- Hmm. It will not happen, but just in case…

- I had a similar thought.

- A Death Knight… should we make one?

- We have already expended too much power. A Death Knight, too? We do not have suitable materials, and it would take a long time.

- We can choose the most useful one and make it in a hurry. If the three of us combine our power, it is possible.

- Th-Then should we at least try?

But the three beings’ plan to create a Death Knight was shattered into pieces before ten minutes had passed.

Fwoosh! Kaaaa-boom!

Even their bodies made of nothing but bones could feel the heat of the searing flames.

“Fuck, there are a shitload of them.”

Crack-crack-crack!

The three beings saw the figure tearing through the monster legion with a spear engulfed in hellfire and hurriedly began chanting.

Their slow voices had become as fast as rap lyrics.

- Omnehasoyu!

- Yenwigajike!

But before the spell could be completed, the young human—whose identity as either a fire mage or a warrior was impossible to determine—had already arrived right in front of them.

“Uh, nice to meet you.”

- O-Omnehasoyu!

- Ye-Yenwigajike!

The young man, Jin Taekyung, cocked his head to one side.

“Hello. *Entertainment Weekly*?[^2] Are you idiots?”

[^2]: The two incantations sound like mangled versions of *annyeonghaseyo* (“hello”) and *Yeonye-ga Junggye*, the Korean title of the TV program *Entertainment Weekly*.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 381`.

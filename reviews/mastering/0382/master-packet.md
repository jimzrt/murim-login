# Master Edit Task — Chapter 382

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
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 극양                        | **Extreme Yang**      |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 귀가      | **your family**                                                 |
| 웨이펑후 | **Wei Penghu** | Senior General and Minister of Defense at the Central Military Commission. |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 중화 | **Zhonghua** | Term used in Shao Shen's rallying cry for China. |
| 시벌좌 | **Sibeol-jwa** | Taekyung's profane nickname, recognized by Shao Shen. |
| 국방부장 | **Minister of Defense** | Wei Penghu's office at the Central Military Commission. |
| 상장 | **Senior General** | Wei Penghu's military rank, explained as four-star. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 웨이펑후 | 진태경 | senior_military_official_to_foreign_hero | Teacher Jin | respectful-formal | Wei Penghu uses 진 선생 when introducing himself and inviting Taekyung to the operations headquarters. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |
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

#### Chapter 380 tail (verified mastered)

…
as he answered so promptly. His face was young, but he was obviously a Hunter. And a powerful one, at that—around A-rank, judging by appearances. Unlike the Hunters around him, who wore identical armor as if they had been stamped out in a factory, he also had a red insignia on his shoulder. “You look like you hold a decent rank, so take care of your men. Let’s save as many people as we can.” “Y-Yes?” “This is only the beginning.” As I answered, I thrust out my fist. KABOOM! Streams of Scorching Yang Qi shot toward the monsters standing there in a daze. Once the wave of searing heat had swept past, only dozens of monster corpses remained. “What are you all staring at? Did someone press the pause button?” “……!” - ……! My words served as the signal. The silence pressing down on the battlefield shattered. - Grrrrrrrr! “K-Kill them! Hold back those monsters!” Humans and monsters. Monsters and humans. A battle of killing and being killed began. I pulled White Flame from where it was embedded deep in the ground and swung it. Swish! Forget waters so crowded they were half water and half fish—monsters were swarming everywhere. A crescent of sword qi extended from the spearhead and grazed a tightly packed mob of monsters. Ding. > **System** > > - Defeated **Lv. 15 Undead Goblin**! > > - Defeated **Lv. 78 Undead Lycanthrope**! > > - Defeated **Lv. 93 Dullahan**! > > - Defeated **Lv. 30 Skeleton**! > > - … > > - The Level gap is significant. Gained negligible EXP! System notifications announcing monster kills and EXP gains rang out without end. Normally, I would have let them go in one ear and out the other, or simply ignored them. But this time, they gave me an important clue. “Don’t tell me these guys are…” - Ah, that’s right, vile human! What a powerful undead army! The Skeleton Warlord’s delighted shout was enough to turn my suspicion into certainty. *No wonder something felt off.* I had already been wondering why I could not sense any life force from them. A sizeable number of monsters were still alive, but roughly half or more of them were undead. All told, it was an army of close to two thousand monsters. “And undead monsters are…” The Skeleton Warlord shouted excitedly. - Beautiful! Magnificent! Valiant! Crash! I cut down five monsters and muttered. “Do you want to disappear like that guy just did? Beautifully, magnificently, and valiantly?” - ……I misspoke. My apologies, vile human. The Skeleton Warlord had briefly forgotten his own situation. He hurriedly added: - Wait. Then they must be under someone’s control! I thought so, too. But there was one thing I still could not be certain about… “The Lich. Did that bastard come out personally?” - Hmm. If you mean the Lich from that holographic video you showed me last time, then probably not. As I listened to the Skeleton Warlord’s answer, I took half a step forward. Boom! A massive iron club passed dangerously close to my shoulder and smashed into the ground. This was an ordinary ogre, and I could still sense its life force. - Guwooooo![^3] “Yeah, I’ll roast you.” [^3]: The ogre’s roar, *guwo*, is also Korean for “roast it.” Boom! The Flame Divine Palm struck the ogre in the chest, and black-green blood erupted from all seven of its orifices. As I passed its collapsing bulk, I slashed White Flame diagonally downward. Whoooosh! Slash! Space split apart, and the bodies of the monsters caught between the two halves were sliced to pieces. Leaving behind a Chinese Hunter who stared blankly at me, drenched in blood and bodily fluids, I clenched my fist. Whoooooom. A surge of extreme heat raced toward my fist, then shot forward. KABOOM! Flame-Annihilating Divine Fist. A massive pillar of fire swallowed the monsters. Along with the foul smell of burning flesh, the few monsters that had somehow survived shrieked in agony. The attack had enough destructive power to make both monsters and Hunters forget to fight for a moment. The Skeleton Warlord stammered. - V-Vile human. You have become even more of a monster. “It feels weird being called a monster by a monster. But if it’s not the Lich, then what bastard is causing all this chaos?” - This commander does not know, either. But I can guarantee one thing. “Guarantee? What?” - That bastard’s control of the undead is a notch below this commander’s. Hahaha! My army! This commander misses you! “……” *Should I kill this bastard or let him live?* As I was wondering, a thought suddenly flashed through my mind, and I stopped dead. “Hey. What did you just say?” - Hahahaha! Did you feel this commander’s majesty, vile human? “Disappear or talk.” - ……I will talk. But what are you asking? “That thing you said about controlling the undead.” - Isn’t it obvious? This commander is a Skeleton Warlord. Compared to them, naturally… Huh? A brief silence followed. He must have had the same thought I did. I swallowed hard, then casually broached the subject. “Try it. That thing.” - …… “Are you going to do it, or do you want to disappear?” The Skeleton Warlord opened his mouth. - Grow, grow, skeletons, skeletons… At that moment, the undead monsters locked in fierce combat abruptly stopped moving. *…So it works.*

#### Chapter 381 tail (verified mastered)

…
human rejection and contempt. But that had been in the distant past, in another dimension. They had drifted across the boundless sea of death until they encountered a ferryman named the Arch Lich. They gained new power and were now trying to become the Liches they had long yearned to be. However… - What a shame. - If only the transformation had been completed. If only there had been more death in this land. - Then we would not have lost control, either. The three beings could not hide their regret. They had been great necromancers in life, but they had not yet fully transformed into Liches. They had been reborn by borrowing the bodies of dead mages, but one week was far too short to absorb the death energy needed to transform into Liches. - That is why He sent the three of us. - He will be disappointed if this fails. - He may even take back the power He gave us. That was what the three beings feared most. They had to overcome this crisis somehow if they wanted to earn the Arch Lich’s trust—even if it meant expending a tremendous amount of power. - It cannot be helped. - Are you suggesting we join forces? - Yes. If the three of us combine our power, even this unidentified higher undead will no longer be able to wrest control from us. - Hmm. Very well. - Do you agree? - I agree. The three beings, who had been competing for the Arch Lich’s favor, finally found common ground. Without hesitation, they began chanting a necromantic spell. - Barensia. Madrit.[^1] - Baielrn. Munich. - Stoh. Siri. [^1]: The pseudo-incantation mangles the names Valencia, Madrid, Bayern Munich, and Stoke City. The energy of death flowed from the three beings and spread through the air. Green grass turned black. Soldiers of the People’s Liberation Army caught within its range clutched their throats and collapsed. “Urk!” “Ghhurk!” Ssshhhhhh. The death energy flowing from the bodies of the humans who had died with those final cries seeped into every inch of the monsters. - Kyaaaaaaa! - Grrrrrrr! The air shook beneath the powerful mana carried in their savage cries. Their strength was beyond comparison with that of ordinary monsters. Only after sensing their strengthened control and the increased power of the monsters under their command did the three beings stop chanting. - Kikikikikik. - It worked. - We expended an enormous amount of power, but… this is more than enough. The three beings were smiling with satisfaction at their strengthened legion when— BOOM! In the distance, a monster’s limbs went flying with a thunderous explosion. The three beings looked toward the flames surging into the sky. - There appears to be a fire mage. Not bad. - It is still only a human. Deploy a large number of Skeleton Mages. - A good idea. A short while later, flames surged into the sky once again. The three beings looked at one another. - Just now. What was that? - Our control was severed. It was not stolen. - It annihilated them? Impressive. - But is that really a mage? Its movements seem too fast… - Let’s deploy the ogre unit. - I’ll see your ogres and raise you Dullahans. - Dullahans as well? Then who will guard us? - He has a point. Dullahans are excessive. Strengthened ogres will be enough. - That is true. Three minutes later, a grim atmosphere hung over the three beings’ skulls. - It was severed. - Again? - I told you we should send the Dullahans. - What the hell is that thing? It does not seem to be a mage. - I said we should send the Dullahans first! - Th-Then let us do that. Watching the twenty or so Dullahans they had selected as an escort troop rush off as a group, the three beings furtively began searching for another point of agreement. - Hmm. It will not happen, but just in case… - I had a similar thought. - A Death Knight… should we make one? - We have already expended too much power. A Death Knight, too? We do not have suitable materials, and it would take a long time. - For now, we can pick the most useful one and make a Death Knight out of it. If the three of us combine our power, it is possible. - Th-Then should we at least try? But the three beings’ plan to create a Death Knight was shattered into pieces before even ten minutes had passed. Fwoosh! Kaaaa-boom! Even their bodies made of nothing but bones could feel the scorching heat. “Fucking bastards. There are a shitload of them.” Crack-crack-crack! The three beings saw the figure tearing through the monster legion with a spear engulfed in hellfire and hurriedly began chanting. Their slow voices had become as fast as rap. - Omnehasoyu! - Yenwigajike! But before the spell could be completed, the young human—whose identity as either a fire mage or a warrior was impossible to determine—had already arrived right in front of them. “Uh, nice to meet you.” - O-Omnehasoyu! - Ye-Yenwigajike! The young man, Jin Taekyung, cocked his head to one side. “Hello. *Entertainment Weekly*?[^2] Are you idiots?” [^2]: The incantations sound like mangled versions of *annyeonghaseyo* (“hello”) and *Yeonye-ga Junggye*, the Korean title of the TV program *Entertainment Weekly*.

## Korean source

```text
＃382화



머리를 치면 몸통은 쓰러지는 법.

우두머리로 보이던 세 놈을 붙잡자 놈들이 통제하고 있던 언데드는 태엽 인형처럼 움직임을 멈췄고, 지휘력을 상실한 몬스터 군단은 뿔뿔이 와해되어 죽거나 도망쳤다.

“아크 리치(Arch Lich)?”

내 물음에 무릎을 꿇고 앉아 있던 세 놈이 고개를 끄덕였다.

이미 죽어서 뼈만 남은 이것들을 ‘놈’이라고 부를 수 있는지는 모르겠지만 어쨌든.

나는 세 개의 두개골을 차례차례 쓰다듬으며 말을 이었다.

“사람이 말을 하면 대답을 해야지. 너희 지금 죽었다고 유세 부리니?”

말이 끝나기가 무섭게 대답이 튀어나왔다.

- 예. 예. 아크 리치가 맞습니다.

- 인간님께서 들으신 것이 정확합니다.

- 그렇다.

“음. 아크 리치라. 처음 들어 보는 몬스터인데…… 그런데 마지막에 반말로 대답한 놈 누구냐.”

- 저놈입니다!

- 감히 위대하신 인간님께!

휙, 휙!

뼈만 남은 손가락들이 한 놈을 가리켰다.

전광석화와도 같은 동료들의 배신에, 지목당한 놈이 두개골을 바르르 떨었다.

- 아니다! 이건 비열한 모함이다!

“……내 생각에는 모함이 아닌 것 같은데.”

거짓말을 할 거면 말투라도 좀 고치든가.

슬쩍 주위를 확인한 나는 인벤토리에서 ‘그것’을 꺼내 들었다.

“골골아. 간식 먹자.”

기묘한 검은 광택이 흐르는 두개골 하나. 그것의 텅 빈 동공에서 불꽃이 일렁인다.

- ……골골이라니. 그럴 바에야 차라리 전처럼 워로드몬이라고 불러라.

“왜, 해골이니까 골골이. 찰떡인데.”

- 본 사령관을 이렇게 모욕하다니!

“뭐 싫으면 말든가.”

다시 인벤토리에 집어넣으려던 그때, 스켈레톤 워로드가 분노한 목소리로 외쳤다.

- 잘 먹겠습니다!

“솔직한 아이로구나.”

솔직한 아이에게는 상을 줘야지. 거짓말이나 치는 나쁜 놈에게는 벌을 주고.

“자, 이제 시식해.”

- 고맙구나. 조금 덜 간악한 인간이여. 그런데 얼마나 먹어야……?

“아까처럼 조금만.”

- 으음. 좀 더 먹고 싶은데. 하지만 알겠다.

간식도 너무 자주 주면 과한 법. 살짝 아쉬움을 표한 스켈레톤 워로드가 벌벌 떨고 있는 놈을 향해 입을 쩍 벌렸다.

- 자, 이리 오너라.

- 히, 히이익! 안 돼!

- 돼!

스켈레톤 워로드의 단호한 외침과 동시에 변화가 시작되었다.

쏴아아악!

저건 다시 봐도 신기하네.

마치 진공청소기로 빨아들이는 것처럼, 무릎을 꿇고 있는 놈의 몸뚱어리에서 흘러나온 검은 안개가 스켈레톤 워로드에게 흡수되기 시작한다.

- 흐어어어억!

변화는 거기에서 끝나지 않았다.

검은 안개, 스켈레톤 워로드가 사기(死氣)라고 부르는 그것이 흘러나올수록 놈의 안색, 아니 뼈다귀가 점점 새하얗게 변해 갔다.

반면 스켈레톤 워로드는 검은 광택이 더욱더 깊고 진해졌다.

- 그, 그만!

- 후후후. 이토록 맛 좋은 사기라니.

- 안 돼애!

- 본 사령관이 전부 가져가 주마. 사기이잇!

빡!

- 흡!

“사기잇 같은 소리 하네. 어디서 이상한 것만 배워서는.”

- ……네가 할 소린가?

“아무튼 이제 그만 먹어라.”

- 어째서!

“살쪄.”

순간 할 말을 잃은 스켈레톤 워로드를 품 안에 집어넣고 놈을 바라봤다.

처음 봤을 때만 해도 거무튀튀하던 뼈다귀는 어느새 반쯤 백골이 된 상태. 상당한 사기를 흡수당한 탓인지, 동공 안의 녹색 불빛이 위태롭게 휘청거린다.

- 크흡, 크흐흑.

뼛속까지 쪽쪽 빨린 동료의 약해진 모습에, 나머지 두 녀석은 초조하게 이빨을 딱딱 부딪쳤다.

- 무엇이든 하문하십시오. 위대하신 화염의 지배자시여.

- 부디 바라옵건대. 이 하찮은 존재, 오르페우스 폰 막시무스 발렌시아 바이엘른의 충성을 받아 주시옵소서.

“……언데드가 아니라 비데인가.”

어지간히 힘을 잃기 싫은 모양이다. 뭐 이렇게 협조적으로 나와주면 나야 고맙긴 하지만.

“자, 아직 말 안 한 게 있으면 밑바닥까지 싹싹 긁어서 털어놔 봐. 만약 거짓부렁을 늘어 놨다가는…….”

- 전부 말하겠습니다!

- 부디 바라옵건대, 이 거짓되고 하찮은 존재가 진실을 말씀드리도록 허락해 주소서!

- 마, 말하겠습니다.

이대로 사골국물이 되기는 싫은지 세 뼈다귀는 열정적으로 질의응답에 참여했다.

일주일 전, 아크 리치의 첫 등장부터 지금까지 벌어진 모든 일 들을 빠짐없이 들은 나는 짐짓 눈살을 찌푸렸다.

“확실해?”

- 그렇사옵니다!

- 죽음의 강에 맹세합니다!

- 하, 한 치의 거짓도 없습니다.

격렬하게 두개골을 끄덕이는 세 놈의 모습에, 스켈레톤 워로드가 불쑥 끼어들었다.

- 사실이다.

“얘네한테 뒷돈 받았냐? 그걸 네가 어떻게 장담해?”

- 죽음의 강에 맹세했으니까. 그건 우리 같은 존재에게는 절대적인 약속이다. 결코 거스를 수 없는.

“흠.”

평소에는 먼지처럼 가볍던 녀석이 저렇게 무게를 잡고 말하는 걸 보면 거짓말은 아닌 것 같다.

사실 지금 같은 상황에 놈들이 수작을 부릴 이유도 없고.

“오케이. 믿어 주지.”

- 감사합니다! 정말 감사합니다!

- 크흐흐흑! 충심을 다하겠나이다. 나의 왕이시여!

- 나, 아니 저도 인간님께 충성하겠습니다. 앞으로는 두 번 다시 오늘과 같은 일을 저지르지 않을 것을 죽음의 강에 맹세…….

콰직!

마지막 놈은 말을 잇지 못하고 머뭇거렸다.

파르르 떨리는 녹색 안광이 자신의 가슴팍에 틀어박힌 주먹과 나를 번갈아 바라본다.

- 어, 어째서?

“어째서긴 뭘 어째서야.”

- 나, 나는, 충성을, 맹세, 죽음의 강…….

“늦었어.”

남의 것처럼 차가운 목소리가 입술을 비집고 흘러나왔다.

“너희가 한 짓을 되돌리기에는.”

바로 오늘, 이 자리에서 수많은 사람이 죽었다.

화기를 갖춘 정규군과 헌터들로도 놈들을 막을 수 없었으니, 지난 일주일 동안 몬스터 군단의 손에 죽은 민간인들은 헤아릴 수조차 없을 것이다.

“충성은 필요 없어. 너희 같은 새끼들이 바치는 거라면 더더욱.”

단전에서 끌어 올린 열양지기를 흘려 보낸 순간.

화륵!

놈의 갈비뼈를 부수고 박혀 있던 주먹에서 극양의 기운이 피어올랐다. 초고온의 열기를 띤 청백색의 강기가 놈의 전신을 휘감았다.

콰아아아!

보였다. 바람 앞의 촛불처럼 휘청이던 놈의 녹색 안광이 꺼지는 광경이.

그리고 튕기듯이 몸을 일으키며 주문을 영창하는 두 놈의 모습도.

- 자즈차와 엄바도……!

- 바르간 마흐라……!

후우웅.

놈들을 중심으로 흩날리는 마력의 바람. 사악한 마법의 주문이 완성되려던 그때, 나는 한마디를 툭 내뱉었다.

“먹어 치워. 전부.”

마치 그 말만을 기다리고 있었다는 듯, 품 안에 넣어 둔 스켈레톤 워로드가 옷자락 사이로 뛰쳐나오며 입을 쩍 벌렸다.

- 얼마든지.

- 바르사바…… 히이익!

- 아, 안 돼!

살고자 하는, 아니 계속 언데드로 남아 있고자 하는 몬스터들의 마지막 단말마.

그러나 놈들의 염원과는 달리 스켈레톤 워로드의 흡입력은 그 어느 때보다 강했고, 신속했다.

쏴아아악! 꿀꺽!

엄청난 양의 사기를 한입에 집어삼킨 스켈레톤 워로드가 두개골을 부르르 떤 다음 순간, 모든 기운을 빼앗긴 두 개의 해골이 와르르 허물어졌다.

띠링. 띠링. 띠링.



- 돌발 퀘스트, [예상치 못한 습격]을 성공적으로 완료했습니다!

- 당신은 몬스터 군단을 와해시켰습니다! 이는 실로 뛰어난 업적입니다!

- 퀘스트 보상으로 칭호, [언데드 헌터]를 획득했습니다!

- 상당량의 경험치와 명성을 획득했습니다!

- 레벨 업!



고작 한 번?

예전 같았으면 레벨 업 몇 번은 거뜬했을 텐데, 120레벨이 되고 나니 필요한 경험치가 많아진 모양이다.

‘경험치 얻자고 한 일은 아니긴 한데.’

마땅히 해야 할 일을 했을 뿐이지만, 약간의 아쉬움이 드는 건 어쩔 수 없다.

강해지면 강해질수록, 앞으로의 전투에 더 큰 도움이 될 테니까.

‘저놈도 마찬가지고.’

나는 내심 중얼거리며 스켈레톤 워로드를 바라봤다.

엄청난 양의 사기를 흡수한 덕분인지, 녀석에게서 느껴지는 힘은 처음 만났던 그때와 비교할 바가 아니었다.

- 으음. 후우우우…….

두개골에 뚫린 코와 귀, 눈 등의 구멍 사이로 검은 안개가 뭉게뭉게 피어오른다.

횃불처럼 타오르는 보랏빛 안광과 매끈한 묵광을 자랑하는 표면. 이내 내 머릿속에 녀석의 광소가 쩌렁쩌렁 울려 퍼졌다.

- 크하, 크하하하하!

“볼륨 좀 줄여라. 시끄럽다.”

- 너, 간악한 인간이여. 이번만큼은 본 사령관이 네게 큰 감사를 표하마.

“당연히 그래야지. 누가 먹이를 줬는데.”

내 시큰둥한 대답에 스켈레톤 워로드가 발끈했다.

- 먹이라니! 이 몸이 애완동물이라도 된다는 건가!

“비슷하지. 아냐?”

- 헛소리하지 마라!

“그래? 골골이, 돌아와.”

내가 손을 내밀자 튕기듯 폴짝 뛰어올라 손바닥 위에 안착하는 두개골.

나는 상으로 녀석의 미간을 살살 긁어 주었다.

“잘했어, 골골이. 어유 예뻐.”

- ……!

두개골이 부들부들 떨렸다.

- 이, 이럴 수가! 본 사령관이 어찌 인간 따위에게!

“입은 아니라고 하지만, 몸은 솔직한 거지.”

- 나는 검은 숲의 주인이자, 위대한 언데드 군단의 사령관이다. 이 몸을 능멸하지 말라!

“머리통만 남은 사령관?”

- 뭣이! 이깟 신체 따위. 사기를 소모한다면 얼마든지 복구할 수 있다!

“그래? 그런데 왜 지금까지 복구 안 했어?”

- ……복구해 봤자 어차피 웬 미친 인간이 박살 낼 테니까.

“오, 정답.”

까드득. 이빨도 없어서 뼈마디를 간 스켈레톤 워로드의 안광이 가늘어졌다.

- 어째서냐, 간악한 인간.

“뭐가?”

- 내게 먹이를, 아니 이토록 큰 힘을 준 꿍꿍이가 있을 것 아닌가. 시커먼 속내가 있는 것이 분명할 터. 진실을 고하라!

잠깐 생각하던 나는 대답했다.

“음. 네가 좆밥이라서.”

- 어?

“어차피 넌 나 못 이겨. 그럴 거면 좀 더 강하고 쓸모있는 좆밥을 데리고 다니는 게 써먹기도 편하잖아. 안 그래?”

- ……!

“자, 이제 안에 들어가 있어라. 사람들 온다.”

나는 충격으로 굳어 버린 녀석을 인벤토리에 집어넣고 자리에서 일어났다.

본래는 공항 직원과 승객들로 붐볐을 공항 면세점 복도. 텅 비고 어두컴컴한 그곳에서 이쪽을 향해 걸어오는 세 사람이 있었다.

그리고 그중 두 사람은 낯익은 얼굴이었다.

“진태경 씨.”

「진 선생님.」

비교적 멀끔한 상태인 최 팀장과 중국 공안 무력부 소속의 A급 헌터인 샤오 쉔이다.

전투가 끝난 지 상당한 시간이 흘렀음에도 여전히 피와 먼지를 뒤집어쓴 채인 샤오 쉔의 얼굴은 피곤에 찌들어 있었다.

「여기 계셨군요.」

나는 최 팀장을 향해 눈인사를 건네며 둘러댔다.

“네. 잠시 할 일이 있어서요.”

「말씀 낮춰 주십시오. 시벌, 아니 진 선생님께서는 저와 제 동지들. 나아가 중화의 인민을 구한 영웅이십니다.」

“…….”

착각인가. 저놈 방금 시벌좌라고 하려고 했던 것 같은데.

내 생각을 아는지 모르는지, 샤오 쉔은 지극히 공손한 태도로 말을 이었다.

「다행히 평화 길드에서 오신 두 선생님의 도움으로 몬스터들을 격퇴할 수 있었습니다. 이 자리를 빌려 다시 한번 감사를 표합니다.」

“아, 예. 뭘 이 정도 가지고. 마땅히 해야 할 일이었는데요.”

나는 손사래를 치며 힐끗 최 팀장의 눈치를 살폈다.

혹시나 [통합 언어팩]이 잘못 작동해서 이상함을 눈치채면 어쩌나 했는데, 지금은 대화를 나누는 상대가 샤오 쉔인 만큼 내가 하는 말도 최 팀장의 귀에는 중국어로 들리는 것 같았다.

“그런데 옆에 계신 분은……?”

이들 중 유일하게 낯선 사람.

묵묵히 우리의 대화를 듣고 있던 반백의 장년인이 손을 내밀어 악수를 청했다.

「중앙 군사위원회에서 국방부장을 맡고 있는 웨이펑후라고 하오. 반갑소, 진 선생.」

“국방부장이라면…….”

「계급은 상장이오.」

“아아.”

대단한 사람인 건 알겠는데, 상장이 뭔진 모르겠다.

내 생각을 읽었는지, 옆에서 최 팀장이 개미만 한 목소리로 속삭였다.

“포 스타요. 포 스타.”

“아아, 아아아! 대장님이셨구나! 만나서 반갑습니다!”

나도 한때 별이 네 개였다. 어릴 때 했던 그 게임 참 재밌었지. 차기작은 쪽박도 그런 쪽박이 없었지만.

내 반응에 장년인, 웨이펑후가 희미한 미소를 띠며 손을 맞잡았다.

「젊은 분이라 그런지, 혈기왕성하시구려. 진 선생께 물어볼 것이 많은데…… 우선 가면서 얘기하시겠소?」

“그러죠, 뭐.”

웨이펑후를 따라 발걸음을 옮기려던 내가 멈칫했다.

“그런데 어디로 갑니까?”

「작전 본부요. 제트기를 대기시켜 두었소.」

“예? 본부? 제트기요?”

「그렇소. 모두 그곳에서 진 선생을 기다리고 있지.」

모두라니. 누구?
```

## Current accepted English baseline

```markdown
# Chapter 382

Strike the head, and the body falls.

Once I got hold of the three who looked like leaders, the undead they had been controlling stopped moving like clockwork dolls. The monster army, deprived of its command, scattered and collapsed, with some dying and others fleeing.

“Arch Lich?”

At my question, the three creatures sitting on their knees nodded.

I wasn’t sure whether I could still call things that had already died and been reduced to bones “creatures,” but whatever.

I stroked each of the three skulls in turn and continued.

“When someone speaks to you, you’re supposed to answer. Are you throwing your weight around just because you’re dead?”

The answer came flying out before I had even finished speaking.

- Yes. Yes. It is indeed the Arch Lich.

- What the great human heard is accurate.

- That is so.

“Hmm. Arch Liches. That’s a monster I’ve never heard of before… But which one of you just answered me informally?”

- That one!

- How dare he speak to the great human like that!

Whoosh! Whoosh!

The skeletal fingers pointed at one of them.

Betrayed by his comrades with lightning speed, the accused skull began to tremble.

- No! This is a vile slander!

“…I don’t think it’s slander.”

If you’re going to lie, at least put on a respectful tone.

I casually checked my surroundings, then pulled *it* out of my inventory.

“Boney. Time for a snack.”

A skull with a strange black sheen. Flames flickered inside its empty eye sockets.

- …Boney? You might as well call me Warlordmon like before.

“Why? You’re a skeleton, so Boney. Perfect fit.”

- To think you would insult this commander like this!

“What? If you don’t like it, forget it.”

I was about to put him back in my inventory when the Skeleton Warlord shouted furiously.

- I will gladly eat it!

“You’re an honest little thing.”

An honest little thing deserved a reward. A bad one that lied deserved punishment.

“Here. Try it.”

- Thank you. You are a slightly less wicked human. But how much should I eat…?

“Just a little, like before.”

- Hmm. I want to eat more. But I understand.

Too many snacks would be overdoing it. Showing a hint of disappointment, the Skeleton Warlord opened his mouth wide at the trembling creature.

- Come here.

- Eek! No!

- Yes!

The change began with the Skeleton Warlord’s firm declaration.

Whoooooosh!

That was still amazing, no matter how many times I saw it.

Like something being sucked up by a vacuum cleaner, black mist began flowing out of the kneeling creature’s body and being absorbed by the Skeleton Warlord.

- Gaaaaaah!

The change didn’t end there.

The black mist—the substance the Skeleton Warlord called death energy—continued to flow out. The creature’s complexion, or rather its bones, gradually turned whiter and whiter.

Meanwhile, the Skeleton Warlord’s black sheen grew deeper and darker.

- S-Stop!

- Hehehe. Such delicious death energy.

- Noooo!

- This commander shall take it all. Death energyyyy!

Crack!

- Hk!

“Don’t go saying things like ‘death energyyyy.’ Where did you even learn that weird crap?”

- …Is that really something you can say?

“Anyway, stop eating now.”

- Why?!

“You’ll get fat.”

The Skeleton Warlord fell silent for a moment. I tucked him against my chest and looked at the creature.

When I had first seen it, its bones had been dark and grimy. Now, it was halfway to becoming a bleached skeleton. Perhaps because it had lost so much death energy, the green light in its eye sockets wavered dangerously.

- Sob… sob…

At the weakened state of their comrade, who had been drained to the bone, the other two creatures anxiously clacked their teeth together.

- Ask anything of us, great ruler of flame.

- I humbly beseech you. Please accept the loyalty of this lowly being, Orpheus von Maximus Valencia Bayern.

“…Are you undead, or are you bidets?”

They really didn’t want to lose their strength. I appreciated their cooperation, though.

“All right. If there’s anything you haven’t told me, scrape the bottom clean and spill every last detail. But if you start spewing lies…”

- We will tell you everything!

- I humbly beseech you. Please permit this false and lowly being to speak the truth!

- W-We will tell you.

Perhaps they didn’t want to become bone broth. The three skeletons participated enthusiastically in the interrogation.

After hearing every detail of what had happened over the past week, from the Arch Lich’s first appearance until now, I deliberately furrowed my brow.

“Are you sure?”

- Yes, we are!

- We swear upon the River of Death!

- Th-There is not a single lie.

As the three creatures vigorously nodded their skulls, the Skeleton Warlord suddenly interrupted.

- It is true.

“Did they pay you off? How can you guarantee that?”

- Because they swore upon the River of Death. It is an absolute promise to beings like us. One that can never be broken.

“Hmm.”

The Skeleton Warlord was usually as light as dust, so the fact that he was speaking with such gravity made me think he wasn’t lying.

Besides, there was no reason for them to scheme in a situation like this.

“Okay. I’ll believe you.”

- Thank you! Thank you so much!

- Sob, sob! I shall devote my entire heart to your service, my king!

- I-I will serve the human, too. I swear upon the River of Death that I will never again commit an act like today’s—

Crack!

The last creature couldn’t finish speaking and faltered. The trembling green light in its eyes shifted between the fist buried in its chest and me.

- Wh-Why?

“Why do you think?”

- I-I will swear my loyalty. I swear upon the River of Death—

“Too late.”

A voice so cold it seemed to belong to someone else slipped through my lips.

“You can’t undo what you did.”

A great many people had died here, today.

Even regular troops equipped with firearms and Hunters had been unable to stop them. There was no way to count all the civilians who had died at the hands of the monster army over the past week.

“I don’t need your loyalty. Especially not from pieces of shit like you.”

The moment I released the Scorching Yang Qi I had drawn up from my dantian—

Fwoosh!

Extreme Yang qi surged from the fist embedded in the creature’s shattered ribs. Blue-white sword qi, carrying ultra-high heat, coiled around its entire body.

Kaaaa-boom!

I saw it.

The green light in its eyes, wavering like a candle in the wind, went out.

I also saw the other two creatures spring to their feet and begin chanting spells.

- Jajeuchawa Eumbado…!

- Bareugan Mahra…!

Whoooong.

A magical wind swirled around them. Just as the evil spell was about to be completed, I casually spoke one word.

“Devour them. All of them.”

As though it had been waiting for those words, the Skeleton Warlord leaped out from among my clothes and opened its mouth wide.

- Gladly.

- Barsaba… Eeeek!

- N-No!

The monsters’ final cries were filled with the desire to live—or rather, the desire to remain undead.

But contrary to their wishes, the Skeleton Warlord’s suction was stronger and faster than ever.

Whoooooosh! Gulp!

After swallowing an enormous amount of death energy in one bite, the Skeleton Warlord’s skull trembled.

The next moment, the two skeletons, drained of every last trace of energy, crumbled to the ground.

Ding. Ding. Ding.

> **System**
>
> - The unexpected Quest, **Unexpected Assault**, has been successfully completed!
>
> - You have routed the monster army! This is truly an outstanding achievement!
>
> - As a Quest Reward, you have acquired the Title **Undead Hunter**!
>
> - You have acquired a considerable amount of EXP and Fame!
>
> - Level Up!

Only once?

In the past, I would have leveled up several times without a problem. But now that I had reached Level 120, it seemed the EXP requirement had increased.

*It’s not like I did this for the EXP.*

I had only done what needed to be done, but I couldn’t help feeling a little disappointed.

The stronger I became, the more useful I would be in future battles.

*That one is the same.*

I looked at the Skeleton Warlord.

Perhaps because he had absorbed such a massive amount of death energy, the power I felt from him was incomparable to what I had sensed when we first met.

- Hmm. Hoooooo…

Black mist billowed from the holes in his skull where his nose, ears, eyes, and other features should have been.

Purple light blazed in his eyes like torches, and the surface of his skull gleamed with a smooth, dark luster. Then his booming laughter echoed through my head.

- Krah, hahahahaha!

“Turn down the volume. You’re loud.”

- You vile human. This time, this commander shall express his great gratitude to you.

“You should. Who was it that fed you?”

At my indifferent reply, the Skeleton Warlord flared up.

- Food?! Are you saying this body has become a pet?!

“Something like that. Isn’t it?”

- Do not spout nonsense!

“Really? Boney, come back.”

I held out my hand.

The skull leaped up as though spring-loaded and landed neatly on my palm.

As a reward, I gently scratched the spot between his eyes.

“Good job, Boney. Who’s a pretty boy?”

- …!

The skull trembled violently.

- H-How can this be?! How can this commander possibly… to a mere human?!

“Your mouth says no, but your body is honest.”

- I am the master of the Black Forest and commander of the great undead legion. Do not humiliate this body!

“A commander with only a head left?”

- What?! This paltry body is nothing! If I expend death energy, I can restore it as many times as I wish!

“Really? Then why haven’t you restored it yet?”

- …Because some crazy human would just smash it again anyway.

“Oh, correct.”

Grind.

The Skeleton Warlord had no teeth, so he ground his bones together instead. His eye sockets narrowed.

- Why, you vile human?

“What?”

- You must have an ulterior motive for giving me food—or rather, granting me such great power. You clearly have some sinister intention. Tell me the truth!

I thought for a moment before answering.

“Hmm. Because you’re a fucking weakling.”

- Huh?

“You can’t beat me anyway. If I’m going to drag you around, it’s easier to make use of a stronger, more useful fucking weakling, isn’t it?”

- …!

“Now get back inside. People are coming.”

I put the creature, frozen with shock, back into my inventory and stood up.

The airport duty-free corridor would normally have been packed with airport employees and passengers. Now, three people were walking toward me through the empty, gloomy passage.

Two of them were familiar faces.

“Mr. Jin Taekyung.”

“Teacher Jin.”

They were Team Leader Choi, who was in relatively decent condition, and Shao Shen, an A-rank Hunter belonging to the Public Security Armed Forces of China.

A considerable amount of time had passed since the battle ended, but Shao Shen’s face was still covered in blood and dust, and exhaustion had sunk deep into his features.

“So you were here.”

I greeted Team Leader Choi with a glance and made an excuse.

“Yes. I had something to take care of.”

“Please speak casually. Sibeol—no, Teacher Jin, you are a hero who saved me and my comrades. More than that, you saved the people of Zhonghua.”

“……”

Was it my imagination, or had he just been about to call me Sibeol-jwa?

Whether he knew what I was thinking or not, Shao Shen continued in an extremely polite tone.

“Fortunately, with the help of the two gentlemen from Peace Guild, we were able to repel the monsters. I would like to take this opportunity to thank you once again.”

“Ah, yes. It was nothing. It was simply what needed to be done.”

I waved my hands modestly, then glanced at Team Leader Choi.

I had been worried that the Integrated Language Pack might malfunction and he would notice something strange. But since Shao Shen was the person I was speaking with, it seemed that even my words sounded like Chinese to Team Leader Choi.

“But who is the gentleman beside you…?”

The only unfamiliar person among them was a middle-aged man with half-gray hair.

He had been listening silently to our conversation. Now he extended a hand for a handshake.

“I am Wei Penghu, the Minister of Defense at the Central Military Commission. It is a pleasure to meet you, Teacher Jin.”

“The Minister of Defense…?”

“My rank is Senior General.”

“Oh.”

I understood that he was an important person, but I had no idea what a Senior General was.

Perhaps he read my thoughts, because Team Leader Choi whispered from beside me in a voice as tiny as an ant.

“Four-star. Four-star.”

“Oh, ohhh! So you’re a four-star general! Nice to meet you!”

I had been a four-star once, too. The game I played as a kid had been a lot of fun. The sequel had flopped so hard it was practically in a league of its own.

At my reaction, Wei Penghu gave a faint smile and clasped my hand.

“Perhaps because you are young, you are full of youthful vigor. I have much to ask Teacher Jin, but… shall we talk while we make our way there?”

“Sure, why not?”

I started following Wei Penghu, then stopped.

“But where are we going?”

“To the operations headquarters. I have a jet standing by.”

“What? Headquarters? A jet?”

“That is correct. Everyone is waiting for Teacher Jin there.”

Everyone?

Who?
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 382`.

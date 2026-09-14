# Master Edit Task — Chapter 383

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

| 무림     | **Murim**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 레이페이 | **Lei Fei** | Previously undisclosed Chinese S-rank Hunter and commander of the Sichuan Public Security Armed Forces; missing with his Hunters. |
| 웨이펑후 | **Wei Penghu** | Senior General and Minister of Defense at the Central Military Commission. |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 쓰촨성 | **Sichuan Province** | Province containing Chengdu International Airport. |
| 중화인민공화국 | **People's Republic of China** | Country whose flag appears on Shao Shen's armor. |
| 중화 | **Zhonghua** | Term used in Shao Shen's rallying cry for China. |
| 국방부장 | **Minister of Defense** | Wei Penghu's office at the Central Military Commission. |
| 난충시 | **Nanchong City** | City containing Gaoping District, where the monster wave began. |
| 가오핑구 | **Gaoping District** | District in Nanchong City where the first monster-wave signs appeared. |
| 청성산 | **Mount Qingcheng** | Mountain containing the temporary operations headquarters. |
| 핑핑이 | **Pingping** | Taekyung's joking guess at the name of the deceased former chairman; not established as the actual name. |
| 팽팽이 | **Pengpeng** | Taekyung's joking alternative guess at the name of the deceased former chairman; not established as the actual name. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 조종사 | 웨이펑후 | pilot_to_senior_military_official | Comrade Minister of Defense | deferential-formal | Pilot's formal greeting on Wei Penghu's arrival. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 뭐랄까 | comedy | Keep the hesitation beat; do not delete the hedge before the realization. | |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
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

#### Chapter 381 tail (verified mastered)

…
human rejection and contempt. But that had been in the distant past, in another dimension. They had drifted across the boundless sea of death until they encountered a ferryman named the Arch Lich. They gained new power and were now trying to become the Liches they had long yearned to be. However… - What a shame. - If only the transformation had been completed. If only there had been more death in this land. - Then we would not have lost control, either. The three beings could not hide their regret. They had been great necromancers in life, but they had not yet fully transformed into Liches. They had been reborn by borrowing the bodies of dead mages, but one week was far too short to absorb the death energy needed to transform into Liches. - That is why He sent the three of us. - He will be disappointed if this fails. - He may even take back the power He gave us. That was what the three beings feared most. They had to overcome this crisis somehow if they wanted to earn the Arch Lich’s trust—even if it meant expending a tremendous amount of power. - It cannot be helped. - Are you suggesting we join forces? - Yes. If the three of us combine our power, even this unidentified higher undead will no longer be able to wrest control from us. - Hmm. Very well. - Do you agree? - I agree. The three beings, who had been competing for the Arch Lich’s favor, finally found common ground. Without hesitation, they began chanting a necromantic spell. - Barensia. Madrit.[^1] - Baielrn. Munich. - Stoh. Siri. [^1]: The pseudo-incantation mangles the names Valencia, Madrid, Bayern Munich, and Stoke City. The energy of death flowed from the three beings and spread through the air. Green grass turned black. Soldiers of the People’s Liberation Army caught within its range clutched their throats and collapsed. “Urk!” “Ghhurk!” Ssshhhhhh. The death energy flowing from the bodies of the humans who had died with those final cries seeped into every inch of the monsters. - Kyaaaaaaa! - Grrrrrrr! The air shook beneath the powerful mana carried in their savage cries. Their strength was beyond comparison with that of ordinary monsters. Only after sensing their strengthened control and the increased power of the monsters under their command did the three beings stop chanting. - Kikikikikik. - It worked. - We expended an enormous amount of power, but… this is more than enough. The three beings were smiling with satisfaction at their strengthened legion when— BOOM! In the distance, a monster’s limbs went flying with a thunderous explosion. The three beings looked toward the flames surging into the sky. - There appears to be a fire mage. Not bad. - It is still only a human. Deploy a large number of Skeleton Mages. - A good idea. A short while later, flames surged into the sky once again. The three beings looked at one another. - Just now. What was that? - Our control was severed. It was not stolen. - It annihilated them? Impressive. - But is that really a mage? Its movements seem too fast… - Let’s deploy the ogre unit. - I’ll see your ogres and raise you Dullahans. - Dullahans as well? Then who will guard us? - He has a point. Dullahans are excessive. Strengthened ogres will be enough. - That is true. Three minutes later, a grim atmosphere hung over the three beings’ skulls. - It was severed. - Again? - I told you we should send the Dullahans. - What the hell is that thing? It does not seem to be a mage. - I said we should send the Dullahans first! - Th-Then let us do that. Watching the twenty or so Dullahans they had selected as an escort troop rush off as a group, the three beings furtively began searching for another point of agreement. - Hmm. It will not happen, but just in case… - I had a similar thought. - A Death Knight… should we make one? - We have already expended too much power. A Death Knight, too? We do not have suitable materials, and it would take a long time. - For now, we can pick the most useful one and make a Death Knight out of it. If the three of us combine our power, it is possible. - Th-Then should we at least try? But the three beings’ plan to create a Death Knight was shattered into pieces before even ten minutes had passed. Fwoosh! Kaaaa-boom! Even their bodies made of nothing but bones could feel the scorching heat. “Fucking bastards. There are a shitload of them.” Crack-crack-crack! The three beings saw the figure tearing through the monster legion with a spear engulfed in hellfire and hurriedly began chanting. Their slow voices had become as fast as rap. - Omnehasoyu! - Yenwigajike! But before the spell could be completed, the young human—whose identity as either a fire mage or a warrior was impossible to determine—had already arrived right in front of them. “Uh, nice to meet you.” - O-Omnehasoyu! - Ye-Yenwigajike! The young man, Jin Taekyung, cocked his head to one side. “Hello. *Entertainment Weekly*?[^2] Are you idiots?” [^2]: The incantations sound like mangled versions of *annyeonghaseyo* (“hello”) and *Yeonye-ga Junggye*, the Korean title of the TV program *Entertainment Weekly*.

#### Chapter 382 tail (verified mastered)

…
*The same goes for him.* I looked at the Skeleton Warlord. Perhaps because he had absorbed such a massive amount of death energy, the power I felt from him was incomparable to what I had sensed when we first met. - Hmm. Hoooooo… Black mist billowed from the holes in his skull—his nose, ears, eyes, and more. Purple light blazed in his eyes like torches, and the surface of his skull gleamed with a smooth, inky luster. Then his booming, maniacal laughter rang through my head. - Krah, hahahahaha! “Turn down the volume. You’re loud.” - You vile human. This time, this commander shall express his great gratitude to you. “You should. Who fed you?” At my indifferent reply, the Skeleton Warlord flared up. - Food?! Are you saying this body has become a pet?! “Something like that. Isn’t it?” - Do not spout nonsense! “Really? Boney, come back.” I held out my hand. The skull leaped up as though spring-loaded and landed neatly on my palm. As a reward, I gently scratched the spot between his eyes. “Good job, Boney. Who’s a pretty boy?” - …! The skull trembled violently. - H-How can this be?! How can this commander possibly… to a mere human?! “Your mouth says no, but your body is honest.” - I am the master of the Black Forest and commander of the great undead legion. Do not humiliate this body! “A commander who’s only a head?” - What?! This paltry body is nothing! If I expend death energy, I can restore it as many times as I wish! “Really? Then why haven’t you restored it yet?” - …Because some crazy human would just smash it again anyway. “Oh, correct.” Grind. The Skeleton Warlord had no teeth, so he ground his bone joints instead. The light in his eye sockets narrowed. - Why, vile human? “What?” - You must have an ulterior motive for giving me food—or rather, granting me such great power. You clearly have some sinister intention. Tell me the truth! I thought for a moment before answering. “Hmm. Because you’re a fucking weakling.” - Huh? “You can’t beat me anyway. If I’m going to drag you around, it’s easier to make use of a stronger, more useful fucking weakling, isn’t it?” - …! “Now get back inside. People are coming.” I put the creature, frozen with shock, back into my inventory and stood up. The airport duty-free corridor would normally have been packed with employees and passengers. Now it was empty and dark, and three people were walking toward me through the gloom. Two of them were familiar faces. “Mr. Jin Taekyung.” “Teacher Jin.” They were Team Leader Choi, who looked relatively presentable, and Shao Shen, the A-rank Hunter from China’s Public Security Armed Forces. A considerable amount of time had passed since the battle ended, but Shao Shen’s face was still covered in blood and dust, and exhaustion had sunk deep into his features. “So you were here.” I greeted Team Leader Choi with a glance and made an excuse. “Yes. I had something to take care of.” “Please, speak casually to me. Sibeol—no, Teacher Jin, you are a hero who saved me and my comrades. More than that, you saved the people of Zhonghua.” “……” Was it my imagination, or had he just been about to call me Sibeol-jwa? Whether he knew what I was thinking or not, Shao Shen continued in an extremely polite tone. “Fortunately, with the help of the two gentlemen from Peace Guild, we were able to repel the monsters. I would like to take this opportunity to thank you once again.” “Ah, yes. It was nothing. It was simply what needed to be done.” I waved my hands modestly, then glanced at Team Leader Choi. I had been worried that the Integrated Language Pack might malfunction and he would notice something strange. But since Shao Shen was the person I was speaking with, it seemed that even my words sounded like Chinese to Team Leader Choi. “But who is the gentleman beside you…?” The only unfamiliar person among them was a middle-aged man with half-gray hair. He had been listening silently to our conversation. Now he extended a hand for a handshake. “I am Wei Penghu, Minister of Defense at the Central Military Commission. It is a pleasure to meet you, Teacher Jin.” “The Minister of Defense…?” “My rank is Senior General.” “Oh.” I could tell he was an important man, but I had no idea what a Senior General was. Perhaps he read my thoughts, because Team Leader Choi whispered from beside me in a voice as tiny as an ant. “Four-star. Four-star.” “Oh, ohhh! So you’re a four-star general! Nice to meet you!” I had been a four-star once, too. The game I played as a kid had been a lot of fun. The sequel had flopped so hard it was practically in a league of its own. Wei Penghu smiled faintly at my reaction and clasped my hand. “Perhaps because you are young, you are full of vigor. I have much to ask Teacher Jin, but… shall we talk on the way?” “Sure, why not?” I started following Wei Penghu, then stopped. “But where are we going?” “To the operations headquarters. I have a jet standing by.” “What? Headquarters? A jet?” “That is correct. Everyone is waiting for Teacher Jin there.” Everyone? Who?

## Korean source

```text
＃383화



웨이펑후가 준비해 두었다는 제트기는 생각했던 모습과는 상당한 차이가 있었다.

‘넓네. 화려하고.’

살짝 열린 출입문 너머로 고급스러운 테이블과 소위 말하는 회장님 의자가 보였다.

곁에 있던 최 팀장이 우리가 보고 있는 이게 한 대당 천억에 육박하는 비즈니스 제트기라는 걸 알려 주며 덧붙였다.

「국빈용으로나 쓰이는 기체를 여기서 볼 줄은 몰랐군요.」

웨이펑후가 담담하게 대꾸했다.

「당연한 일이오. 두 선생께서는 본국의 국빈이시니.」

“아.”

「덕분에 수많은 병사와 헌터들을 살릴 수 있었소. 나를 포함한 모두는 오늘의 도움을 절대 잊지 않을 거요.」

“……아, 예.”

그 전에 미세먼지와 역사 왜곡부터 좀 처리해 줬으면 좋겠는데.

내심 중국이 내가 알고 있는 것보다 더 양심적인 국가이길 바라며 기체에 몸을 실었다.

대기하던 조종사가 우리를 향해, 정확히는 웨이펑후를 향해 절도있는 동작으로 경례를 올렸다.

「오셨습니까, 국방부장 동지.」

「준비는?」

「본 기체를 포함한 호위기 모두 준비를 끝마쳤습니다. 명령만 내려 주시면 됩니다.」

호위라기에 뭔 소린가 했더니, 창밖 활주로에 날렵한 곡선을 자랑하는 전투기 다섯 대가 신호를 보내듯 불을 깜빡이는 것이 보였다.

‘뭐여, 저게.’

전쟁 영화에서나 보던 걸 여기서 보네. 당장 한판 뜨러 가기라도 하는 건가?

눈을 동그랗게 뜬 내 모습에 웨이펑후가 입을 열었다.

「아직 외부에는 정확히 알려지지 않았지만…… 알다시피 현재 쓰촨성은 전시 상황이오. 마법으로 인한 통신 방해와 비행 몬스터들의 습격까지 빈번하게 이루어지는 실정이니, 안전을 위해 호위는 필수지.」

“정말입니까?”

생각했던 것보다 상황이 심각하다.

우리야 청두 국제공항을 습격하러 온 와이번에게 겸사겸사 느낌으로 습격을 당한 거지만, 이게 쓰촨성 전역에서 벌어지는 일이라면 이야기가 달라진다.

「차라리 내가 거짓말을 하는 거라면 얼마나 좋겠소.」

현재 상황을 떠올리는 것만으로 지치는지, 부쩍 늙어 버린 웨이펑후가 푹신한 좌석 시트에 몸을 기댔다.

「자네와는 여기에서 작별해야 할 듯싶군. 조만간 다시 만나세. 샤오 쉔 대교(大校).」

우리와 달리 기체에 오르지 않은 한 사람, 샤오 쉔이 부동자세로 경례를 취했다.

「예. 조속히 임무를 마친 후 합류하겠습니다, 국방부장 동지. 그리고 두 선생님.」

「그래, 기대가 크네.」

상당한 전공을 세웠기 때문인지 전도유망한 젊은 헌터를 바라보는 웨이펑후의 입가에 흐뭇한 미소가 스쳤다.

최 팀장은 정중한 묵례로 인사를 대신했고, 나는 손을 흔들어 주었다.

“다음에 또 봐요. 오늘 아주 잘 싸웠어.”

단지 한 마디였을 뿐이었다.

하지만 내 말을 들은 샤오 쉔의 눈동자가 쟁반만큼 커졌다. 전기에 감전된 것처럼 몸을 부르르 떨던 그가 쩌렁쩌렁하게 외쳤다.

「가, 감사합니다! 진 선생님께서 실망하시는 일 없도록 모든 일에 견마지로(犬馬之勞)를 다하겠습니다!」

“……아니, 뭘 견마지로씩이나.”

「옥체 무사하시길 기원하겠습니다! 추웅! 성!」

“옥체라니. 그게 무슨…….”

빡!

「흡!」

“…….”

저건 잘못된 판단의 표본 같은데.

경례를 얼마나 세게 했는지 손날로 본인의 눈썹 부분을 때린 수준이다.

이를 악물고 아픔을 참는 샤오 쉔의 모습을 황당하게 바라보던 그때, 입구가 닫히고 우리가 탄 비즈니스 제트기가 천천히 이륙을 시작했다.

“저 친구도 뭐랄까, 그……. 캐릭터가 독특하네요.”

내 떨떠름한 말에 웨이펑후가 피식 웃었다.

「우상에게 칭찬을 들었으니 그럴 만도 하지 않겠소?」

“예?”

「본국에는 진 선생을 동경하는 젊은 헌터들이 많소. 저 친구도 예외는 아니지.」

뭐야, 나 한류 스타였어?

그나저나 이 양반, 나는 새도 떨어트린다는 포 스타치고 아랫사람에게 관심이 많은 것 같다.

아니면 샤오 쉔이 그만큼 기대받는 청년이거나.

아, 그런데…….

- 팀장님. 중앙군사위원회 국방부장이면 정확히 어느 정도예요? 제가 이쪽 편제를 잘 몰라서.

내 전음에 움찔한 최 팀장이 메시지 마법으로 대답했다.

- 우리나라로 치자면 국방부 장관입니다. 물론 이곳은 중국이고, 웨이펑후는 현 주석의 오른팔이니 그 권력이 훨씬 막대하죠.

- 아.

나랑 비슷하네. 난 국밥부 장관인데.

순대국 특 하나면 공깃밥 세 그릇 정도는 거뜬하다.

물론 웨이펑후는 손가락질 하나로 도시 세 개를 지워 버릴 수도 있겠지만.

그리고 지금, 막대한 권한을 지닌 중화인민공화국의 권력자가 우리를 향해 상반신을 기울이며 묻고 있다.

「가는 동안 나눠야 할 대화가 많은 것 같소만. 안 그렇소?」

최 팀장과 내가 진지하게 고개를 끄덕이며 입을 열었다.

「물론입니다. 우선 현재 쓰촨성의 상황이 정확히 어찌 돌아가는지부터 여쭤…….」

“그런데 혹시 삶은 달걀이랑 사이다 없나요. 열심히 싸웠더니 허기가 져서.”

“…….”

“…….”

없는 모양이다.

「있소.」

“……?”

“……?”

이게 있네.



* * *



중화인민공화국.

중국의 정식 명칭에서 알 수 있듯이 이 위엄 넘치는 대륙인들은 아직도 사회주의를 국가 이념으로 삼고 있었다.

지금으로부터 약 이십여 년 전, 종신 집권으로 독재의 기틀을 공고히 다졌던 당시 주석이 대격변 도중 사망하면서 훨씬 온건한 정권으로 권력이 이양되기는 했지만, 아직도 알맹이는 여전하다.

- 죽은 주석 이름이 뭐였죠? 핑핑이? 팽팽이?

웨이펑후의 말에 맞장구치던 최 팀장이 입술을 달싹였다. 경이로울 정도의 포커페이스다.

- ……혹시나 해서 드리는 말씀인데, 이곳에서 그런 말 꺼냈다가는 정말 큰일 납니다.

- 그래서 전음, 아니 메시지 마법으로 하잖아요.

- 주의하라는 말입니다. A급 이상의 뛰어난 마법사 중에는 메시지 마법을 도청할 수 있는 사람도 있어요.

- 어쨌건 이름이 뭐였죠? 핑핑이, 아니면 팽팽이? 저 이거 못 들으면 오늘 잠 못 자요.

- ……핑핑이.

결국은 대답해 줄 거면서 뭘.

비로소 후련해진 나는 들려오는 웨이펑후의 말에 귀를 기울였다.

「그 누구도 예상치 못한 일이었소.」

쓰촨성은 광활한 면적과 수천만의 인구를 보유한 거대한 성.

그리고 이 모든 일은 쓰촨성에 존재하는 20여 개 행정 구역 중 하나, 난충시의 가오핑구에서 시작되었다.

「알다시피 본국에 존재하는 게이트의 숫자는 타국과 비교하면 열 배 이상 많소. 때문에 대격변 당시 가장 큰 피해를 입었던 국가 중 하나였고, 그만큼 철저하게 관리하고 있었지.」

하지만 사람의 힘으로 천재지변까지 제어할 수는 없었고, 몬스터 웨이브는 천재지변보다 더한 재앙이었다.

「가오핑구에서 마력 수치가 급등했다는 연락을 받은 건, 첫 징후가 나타난 지 정확히 13분이 지난 후였소. 그리고 쓰촨성에 주둔 중이던 공안무력부장 레이페이가 휘하 헌터들을 이끌고 현장에 도착했을 때는…… 모든 것이 늦은 후였지.」

“레이페이?”

낯선 이름. 그러나 어째서일까, 문득 떠오르는 기억이 있었다.

‘출발하기 전, 길드 하우스에서 최 팀장이 보여 줬던 그 영상.’

아직도 생생하다. 홀로그램이 비춘 아비규환의 도시와 헌터들의 선두에서 몬스터들을 베어 가던 한 남자의 모습이.

그의 무기에는 눈이 부실 만큼 찬란한 오라가 맺혀 있었다.

“본 적이 있는 것 같습니다. 혹시 보내 주신 영상에 나왔던 그……?”

「그렇소.」

잠시 머뭇거리던 웨이펑후가 옅은 한숨과 함께 입을 열었다.

「본국이 보유한 S급 헌터 중 한 명이었소. 물론 두 선생께서는 모르시겠지만.」

모를 거라고?

S급 헌터는 전 세계를 통틀어도 스무 명밖에 되지 않는 절대 강자들.

그들이 누리는 유명세와 지위는 무림의 초절정 고수가 가지는 그것보다 훨씬 크고 강하다.

인터넷, 뉴스, SNS가 그들의 발판이고 마이크와 카메라는 그림자처럼 따라붙는다.

무림인을 향한 양민들의 시선이 경계심 반, 호기심 반이라면 현대인들에게 헌터는 그저 선망의 대상이다. 그야말로 세계의 유명인인 것이다.

‘그런데 그런 S급 헌터를 우리가 모른다고?’

웨이펑후는 에둘러 말했지만, 그 말에 담긴 뜻을 알아듣기에는 충분했다.

나와 최 팀장의 시선이 허공에서 부딪쳤다. 이 순간, 우리는 같은 생각을 떠올리고 있었다.

‘드러나지 않은 S급 헌터.’

아니, 정확히 말하자면 중국 정부가 의도적으로 감춘 S급 헌터라고 하는 게 맞겠다.

‘이런 건 소문으로만 들었는데. 사실이었나?’

S급 헌터는 한 국가의 얼굴이나 다름없는 존재.

그러나 얕보이지 않기 위해 안간힘을 쓰는 약자와는 달리, 강자는 오히려 발톱을 감춘다.

이미 두 명의 S급 헌터를 보유하고 있다고 알려진 중국은 모든 힘을 드러내고 싶지 않았던 게 분명했다.

어쩌면 중국뿐만 아니라, 세계 유수의 강대국들도 마찬가지일 것이다.

‘거 참. 대격변을 겪고서도 이런 눈치싸움이라니.’

한심하기도 했고, 한편으로는 이해가 될 것 같기도 하다. 외교, 정치. 내가 알 수 없었던 세상의 진실을 조금이나마 엿본 것 같아 기분이 묘했다.

그리고 그런 나와 달리, 최 팀장은 보다 더 예리한 사람이었다.

「귀국이 보유한 S급 헌터 중 한 명‘이었다’는 건, 과거형으로 들리는군요.」

웨이펑후가 참담한 얼굴로 대답했다.

「……처음 몬스터 웨이브가 일어났던 일주일 전, 레이페이는 실종되었소. 그가 지휘하던 공안무력부의 헌터들과 함께.」

「실종이 확실합니까? 혹시…….」

「죽음은 확인하지 못했소. 그 영상을 마지막으로 리치. 아니지, 아크 리치라 불린 그 몬스터가 마력으로 모든 통신과 감시를 차단했으니까.」

나와 최 팀장은 동시에 침음성을 흘렸다. 우리의 반응에 웨이펑후가 갈라진 목소리로 물었다.

「선생들도 레이페이가 죽었다고 생각하시오?」

“음.”

“어…….”

실종. 그것도 일주일 전에 그 아비규환 속에서 실종되었다면 이미 결말은 정해져 있는 것이나 다름없다.

최 팀장의 눈짓에 나는 조심스럽게 입을 열었다.

“그, 뭐냐. 사람 일은 어떻게 될지 모르는 것이지만…….”

「다른 전문가들은 백 퍼센트 죽었을 거라 하더군. 천하에 쓸모없는 허풍선이들 같으니.」

왜 그래. 진짜 전문가 맞는 것 같은데.

저 상황에서 살아 있다고 장담하는 놈이 있으면 당장 잘라야 한다. 그게 엄연한 사실이니까.

「하지만 내 생각은 다르오. 레이페이, 그 아이는 반드시 살아 있을 거요.」

“저도 그러길 바랍니다만, 아무래도 현실적으로 봤을 때…….”

「하나뿐인 외조카요. 어릴 적부터 병약했던 내 누이는 산고를 이기지 못하고 세상을 떠났고, 젖도 못 뗀 핏덩이를 내가 지금까지 친자식처럼 키웠지.」

“예?”

아니, 외조카라니. 친자식처럼 키웠다니. 이게 뭔 소리야.

석상처럼 굳어 버린 내게 웨이펑후가 축축해진 눈동자로 물었다.

「그런데 뭐라 하려고 했소? 현실적으로 봤을 때, 그 뒤에 말이오.」

시벌, 이건 역대급 위기다.

순간 말문이 턱 막혔던 나는 간신히 목소리를 쥐어짜 냈다.

“그, 현실적으로 봤을 때. 살아 있을 확률도 아주 없진 않다고 말씀을 드리려고 한 건데요.”

「그렇소? 그게 사실이오?」

“아, 예. 하지만 그 확률이라는 게 매우 희박…….”

「고맙소, 진 선생!」

“아니, 장군님. 대장님. 수령님. 잠시만 고정하시고 제 말을 좀 더…….”

덥석!

틀렸다. 웨이펑후는 이미 내 말을 듣고 있지 않았다. 그 대신 눈물이 그렁그렁 맺힌 눈동자로 내 손을 감싸 쥐었다.

「한 가지 부탁해도 되겠소?」

그 부탁, 안 했으면 좋겠는데.

간절한 내 바람과는 달리, 결국 몇 초 후 예상했던 한 마디가 가슴을 파고들었다.

「혹시 나중에 진 선생께서 그 아이를 만난다면 데려와 주실 수 있소?」

“…….”

「내 이리 부탁하리다.」

간절하게 부탁하는 그의 어깨너머로 최 팀장이 고개를 젓는 것이 보인다.

차라리 처음부터 단호하게 대답했다면 어땠을까. 후회했지만 이미 늦었다.

결국 내가 할 수 있는 대답은 하나뿐이었다.

“그렇게 하겠습니다. 하지만…….”

「진 선생.」

“네?”

「굳이 말하지 않아도 되오. 이미 각오하고 있는 일이니.」

“……!”

소매로 눈가를 훔친 웨이펑후는 혈육의 안위를 걱정하는 장년인이 아닌, 중앙군사위원회 국방부장으로 돌아와 있었다.

「이것으로 충분하오. 누구도 선뜻 나서 주질 않았는데, 진 선생이 약속해 주었으니 안심이오.」

“저도 장담할 수는 없습니다.”

「내게 필요한 건 누군가의 호언장담이 아니었소. 실낱같은 희망이었지.」

웨이펑후가 작게 읊조린 그때, 붕 뜨는 부유감과 함께 기체가 지상을 향해 미끄러졌다.

창밖, 짙은 어둠에 휩싸인 그곳에 험악한 산세와 쉴 새 없이 움직이는 불빛, 그리고 군용차량이 보인다.

「도착한 것 같군.」

뭔가에 사로잡힌 사람처럼, 창밖의 풍경을 뚫어져라 바라보던 내가 물었다.

“여기가 어딥니까?”

「임시 작전 본부요.」

“아뇨. 그걸 물어본 게 아닙니다.”

「음?」

“산. 저 산이 왠지 모르게 낯익은 기분이라서요.”

「그럴 리가. 진 선생께선 본국에 입국한 적이 없는 것으로 아는데…… 아, 혹시 사진으로 본 것 아니오?」

“사진이요?”

「유네스코에서 지정한 세계문화유산이니 충분히 가능한 일이지.」

웨이펑후가 옅은 웃음과 함께 말을 이었다.

「임시 작전 본부. 청성산(靑城山)에 온 것을 환영하오.」
```

## Current accepted English baseline

```markdown
# Chapter 383

The jet Wei Penghu had prepared looked nothing like what I had expected.

*It’s spacious. And fancy.*

Through the slightly open door, I could see a luxurious table and the kind of chair people called a chairman’s chair.

Team Leader Choi, who was standing beside me, informed me that this was a business jet costing close to one hundred billion won per aircraft, then added,

“I never thought I’d see an aircraft normally reserved for state guests here.”

Wei Penghu replied calmly.

“Of course. The two of you are state guests of our country.”

“Oh.”

“Thanks to you, we were able to save countless soldiers and Hunters. No one—including me—will ever forget the help you gave us today.”

“…Ah, yes.”

*I’d appreciate it if you dealt with the fine dust and historical distortions first.*

Hoping inwardly that China was a more conscientious country than I knew it to be, I boarded the aircraft.

The waiting pilot gave us a crisp salute—or, more precisely, gave Wei Penghu a crisp salute.

“Have you arrived, Comrade Minister of Defense?”

“Are we ready?”

“All escort aircraft, including this one, have completed preparations. We are awaiting your orders.”

I wondered what he meant by “escort,” then looked out the window and saw five fighter jets with sleek, elegant curves blinking their lights as if signaling us.

*What the hell?*

I had only ever seen things like that in war movies. Were we heading straight into a fight?

Seeing my eyes widen, Wei Penghu spoke.

“The exact situation has not yet been made public, but as you know, Sichuan Province is currently in a state of war. Magical interference with communications and attacks by flying monsters are occurring frequently. Escorts are essential for our safety.”

“Are you serious?”

The situation was worse than I had imagined.

The wyverns had come to attack Chengdu International Airport and only attacked us while they were at it, but if the same thing was happening throughout Sichuan Province, that was an entirely different story.

“If only I were lying. How wonderful that would be.”

Perhaps merely recalling the current situation was exhausting him. Wei Penghu, who seemed to have aged considerably, leaned back into the soft seat.

“It seems we must part ways here. I hope we meet again soon, Senior Colonel Shao Shen.”

Unlike us, one man had not boarded the aircraft. Shao Shen stood rigidly at attention and saluted.

“Yes. I will complete my mission as quickly as possible and rejoin you, Comrade Minister of Defense. And you as well, Teachers.”

“Yes. I have high hopes for you.”

Perhaps because he had achieved so much, a pleased smile briefly touched Wei Penghu’s lips as he looked at the promising young Hunter.

Team Leader Choi substituted a polite bow for a farewell, while I waved.

“See you next time. You fought really well today.”

It was only one sentence.

But Shao Shen’s eyes grew as large as serving trays when he heard me. His body trembled as though he had been electrocuted, and he shouted in a booming voice,

“Th-Thank you! I will devote every ounce of my humble strength to every task so that Teacher Jin is never disappointed!”

“…No need to go that far.”

“I pray that your august person remains safe! Loya-alty!”

“Your august person? What does that even—”

Smack!

“Ngh!”

“…”

*That looked like a textbook example of a bad decision.*

He had saluted so forcefully that the edge of his hand had struck his own eyebrow.

I was staring dumbfounded at Shao Shen as he clenched his teeth and endured the pain when the entrance closed and our business jet slowly began to take off.

“That friend of yours is, well… What should I say? His character is pretty unique.”

At my dubious comment, Wei Penghu let out a quiet laugh.

“He heard praise from his idol. Can you blame him?”

“Pardon?”

“There are many young Hunters in our country who admire Teacher Jin. He is no exception.”

*What? Was I a Korean Wave star now?*

Come to think of it, this man seemed unusually interested in those beneath him for a four-star general who was powerful enough to make birds fall from the sky.

Or perhaps Shao Shen was simply a young man who inspired that much expectation.

*Ah, but…*

- Team Leader, where exactly does the Minister of Defense at the Central Military Commission sit in the hierarchy? I’m not familiar with how things are structured here.

Team Leader Choi flinched at my Sound Transmission, then answered through message magic.

- In our country, he would be the Minister of Defense. Of course, this is China, and Wei Penghu is the current chairman’s right-hand man, so his power is far greater.

- Ah.

*We’re similar. I’m the Minister of Soup and Rice, myself.*

*One extra-large bowl of sundae-guk[^1] is enough for me to polish off three bowls of rice.*

*Of course, Wei Penghu could probably erase three cities with a single point of his finger.*

And now, that powerful official of the People's Republic of China leaned his upper body toward us and asked,

“We have quite a lot to discuss on the way. Wouldn’t you agree?”

Team Leader Choi and I solemnly nodded and began to speak.

“Of course. First, we would like to ask exactly what is happening in Sichuan Province—”

“By the way, do you happen to have any boiled eggs and soda? I’m hungry after fighting so hard.”

“…”

“…”

Apparently, they didn’t.

“We do.”

“...?”

“...?”

They did.

* * *

The People's Republic of China.

As its official name suggested, the grand people of this vast continent still embraced socialism as their national ideology.

About twenty years ago, the chairman of the time—who had solidified the foundations of a dictatorship by securing lifelong rule—died during the Great Cataclysm, and power was transferred to a much more moderate regime.

But the core of the system remained unchanged.

- What was the dead chairman’s name again? Pingping? Pengpeng?

Team Leader Choi, who had been responding to Wei Penghu, silently moved his lips. His composure was astonishing.

- …I’m only saying this in case you didn’t know, but you’ll be in serious trouble if you bring up something like that here.

- That’s why I’m using Sound Transmission—or rather, message magic.

- I’m telling you to be careful. Among the outstanding mages of A-rank and above, there are people who can eavesdrop on message magic.

- Anyway, what was his name? Pingping or Pengpeng? I won’t be able to sleep tonight if I don’t find out.

- …Pingping.

*He was going to answer anyway. Why make such a fuss?*

Finally relieved, I listened to Wei Penghu’s words.

“No one could have anticipated it.”

Sichuan Province was a massive province with a vast area and a population of tens of millions.

And all of this had begun in Gaoping District, Nanchong City—one of the more than twenty administrative districts in Sichuan Province.

“As you know, our country has more than ten times as many Gates as other nations. Because of that, we were one of the countries hit hardest during the Great Cataclysm, and we have managed them with corresponding rigor ever since.”

But humans could not control even natural disasters, and the monster wave was a calamity worse than any natural disaster.

“Exactly thirteen minutes after the first sign appeared, we received word that the mana levels in Gaoping District had skyrocketed. And by the time Lei Fei, commander of the Public Security Armed Forces stationed in Sichuan Province, arrived at the scene with the Hunters under his command… everything was already too late.”

“Lei Fei?”

An unfamiliar name. And yet, for some reason, a memory suddenly surfaced.

*The video Team Leader Choi showed me at the Guild house before we left.*

It was still vivid: the city plunged into chaos beneath the hologram’s light, and a man at the head of the Hunters, cutting down monsters one after another.

An aura so brilliant it hurt the eyes had gathered around his weapon.

“I think I’ve seen him before. Is he the man who appeared in the video you sent us…?”

“That’s right.”

Wei Penghu hesitated briefly before continuing with a faint sigh.

“He was one of the S-rank Hunters possessed by our country. Of course, the two of you would not have known that.”

*We wouldn’t have known?*

There were only twenty S-rank Hunters in the entire world. They were absolute powerhouses.

The fame and status they enjoyed were far greater and more formidable than those of even a Supreme Peak master in the Murim.

The internet, the news, and social media were their platforms, while microphones and cameras followed them like shadows.

If ordinary people looked at martial artists with half wariness and half curiosity, modern people looked at Hunters with nothing but admiration.

They were celebrities known throughout the world.

*But we didn’t know about an S-rank Hunter like that?*

Wei Penghu had spoken indirectly, but I understood the meaning behind his words well enough.

Team Leader Choi and I met eyes in midair. At that moment, we were thinking the same thing.

*An undisclosed S-rank Hunter.*

No. More precisely, an S-rank Hunter deliberately concealed by the Chinese government.

*I’d only heard about things like that in rumors. So it was true?*

An S-rank Hunter was practically the face of a nation.

But unlike the weak, who struggled desperately not to be looked down on, the strong hid their claws.

China was already known to possess two S-rank Hunters. Clearly, it had not wanted to reveal all its strength.

Perhaps the world’s other great powers were the same.

*What a thing. Even after going through the Great Cataclysm, they’re still playing this game of one-upmanship.*

It was pathetic. At the same time, I could almost understand it.

Diplomacy. Politics.

I felt as though I had caught a glimpse of the truth of a world I had never understood, and the feeling was strange.

Unlike me, however, Team Leader Choi was much sharper.

“When you say that Lei Fei ‘was’ one of the S-rank Hunters your country possessed, that sounds like the past tense.”

Wei Penghu answered with a grim expression.

“…A week ago, when the first monster wave occurred, Lei Fei disappeared. Along with the Hunters from the Public Security Armed Forces under his command.”

“Are you certain he disappeared? Could it be that…”

“We have not confirmed his death. After that video, the monster called the Lich—no, the Arch Lich—used mana to cut off all communications and surveillance.”

Team Leader Choi and I groaned at the same time.

Hearing our reaction, Wei Penghu asked in a hoarse voice,

“Do you two also think Lei Fei is dead?”

“Hmm.”

“Uh…”

*If someone disappeared in that chaos a week ago, the ending was practically a foregone conclusion.*

At Team Leader Choi’s signal, I cautiously opened my mouth.

“Well, you never know how things will turn out, but…”

“Other experts said he was one hundred percent dead. Useless blowhards, every last one of them.”

*What’s wrong with you? They sound like real experts.*

If anyone claimed he was alive under those circumstances, they should be fired immediately.

That was simply a fact.

“But I think differently. Lei Fei—that boy must still be alive.”

“I hope so too, but realistically speaking…”

“He is my only nephew. My sister, who had been sickly since childhood, died in childbirth. I raised that tiny, unweaned infant as if he were my own son.”

“What?”

*A nephew? You raised him as your own son? What the hell is this?*

As I froze like a statue, Wei Penghu looked at me with tear-filled eyes.

“But what were you going to say? When you said, ‘Realistically speaking,’ I mean.”

*Fuck. This is a crisis of unprecedented proportions.*

My words caught in my throat. I barely managed to squeeze out a voice.

“Well, realistically speaking, I was going to say that there’s still a chance he might be alive.”

“Is that so? Is that true?”

“Yes. But that chance is extremely slim…”

“Thank you, Teacher Jin!”

“No, General. Commander. Great Leader. Just hold on a second and let me finish—”

Grab!

It was too late. Wei Penghu was no longer listening to me.

Instead, he clasped my hand in both of his, his eyes brimming with tears.

“May I ask you for one favor?”

*I wish he wouldn’t.*

Contrary to my desperate hopes, a few seconds later, the words I had been dreading pierced my heart.

“If you happen to meet that boy someday, would you bring him to me?”

“…”

“I beg you.”

Over his desperately pleading shoulders, I saw Team Leader Choi shaking his head.

*What if I had just answered him firmly from the beginning?*

I regretted it, but it was already too late.

In the end, there was only one answer I could give.

“I will. But…”

“Teacher Jin.”

“Yes?”

“You don’t have to say it. I’m already prepared for that.”

“...!”

Wei Penghu wiped the corners of his eyes with his sleeve.

He was no longer a middle-aged man worrying about the safety of his blood relative. He had returned to being the Minister of Defense at the Central Military Commission.

“This is enough. No one was willing to step forward, but you promised me. I can rest easy now.”

“I can’t guarantee anything.”

“What I needed was not someone’s bombastic guarantee. It was a thread of hope.”

Just as Wei Penghu murmured those words, the aircraft descended with a weightless sensation and glided toward the ground.

Outside the window, amid the darkness, I could see rugged mountain terrain, lights moving ceaselessly, and military vehicles.

“It looks like we’ve arrived.”

I had been staring fixedly out the window as though possessed by something. Now I asked,

“Where are we?”

“The temporary operations headquarters.”

“No. That’s not what I asked.”

“Hmm?”

“The mountain. That mountain feels strangely familiar.”

“That’s impossible. As far as I know, you have never entered our country before… Ah, perhaps you saw it in a photograph?”

“A photograph?”

“It is a UNESCO-designated World Cultural Heritage Site, so that would certainly be possible.”

With a faint smile, Wei Penghu continued,

“This is where we established our temporary operations headquarters. Welcome to Mount Qingcheng.”

[^1]: *Sundae-guk* is a Korean soup made with sundae, a type of Korean blood sausage, and is commonly served with rice.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 383`.

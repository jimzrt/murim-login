# Master Edit Task — Chapter 384

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
| 진태경    | **Jin Taekyung**   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 대주     | **Squad Leader** / **Commander**             |
| 생도     | **cadet**                                    |
| 칭호               | **Title**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 사천     | **Sichuan**            |
| 웨이펑후 | **Wei Penghu** | Senior General and Minister of Defense at the Central Military Commission. |
| 삼문혈사 | **Three-Sect Bloodbath** | Recent attack on three major orthodox sects |
| 쓰촨성 | **Sichuan Province** | Province containing Chengdu International Airport. |
| 중화인민공화국 | **People's Republic of China** | Country whose flag appears on Shao Shen's armor. |
| 중화 | **Zhonghua** | Term used in Shao Shen's rallying cry for China. |
| 시벌좌 | **Sibeol-jwa** | Taekyung's profane nickname, recognized by Shao Shen. |
| 국방부장 | **Minister of Defense** | Wei Penghu's office at the Central Military Commission. |
| 청성산 | **Mount Qingcheng** | Mountain containing the temporary operations headquarters. |
| 대마법사 | **Archmage** | Title held by only three people worldwide. |
| 총서기 | **General Secretary** | One of Xiao Yang's offices. |
| 중앙군사위원회 | **Central Military Commission** | Commission chaired by Xiao Yang. |
| 종석이 | **Jongseok** | Taekyung's mistaken personal-name joke for the General Secretary; not the chairman's actual name. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 웨이펑후 | 진태경 | senior_military_official_to_foreign_hero | Teacher Jin | respectful-formal | Wei Penghu uses 진 선생 when introducing himself and inviting Taekyung to the operations headquarters. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
| 나발이고 | slang | Dismissive rejection of the preceding concern (to hell with X), not a neutral “or not.” | |
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

#### Chapter 382 tail (verified mastered)

…
*The same goes for him.* I looked at the Skeleton Warlord. Perhaps because he had absorbed such a massive amount of death energy, the power I felt from him was incomparable to what I had sensed when we first met. - Hmm. Hoooooo… Black mist billowed from the holes in his skull—his nose, ears, eyes, and more. Purple light blazed in his eyes like torches, and the surface of his skull gleamed with a smooth, inky luster. Then his booming, maniacal laughter rang through my head. - Krah, hahahahaha! “Turn down the volume. You’re loud.” - You vile human. This time, this commander shall express his great gratitude to you. “You should. Who fed you?” At my indifferent reply, the Skeleton Warlord flared up. - Food?! Are you saying this body has become a pet?! “Something like that. Isn’t it?” - Do not spout nonsense! “Really? Boney, come back.” I held out my hand. The skull leaped up as though spring-loaded and landed neatly on my palm. As a reward, I gently scratched the spot between his eyes. “Good job, Boney. Who’s a pretty boy?” - …! The skull trembled violently. - H-How can this be?! How can this commander possibly… to a mere human?! “Your mouth says no, but your body is honest.” - I am the master of the Black Forest and commander of the great undead legion. Do not humiliate this body! “A commander who’s only a head?” - What?! This paltry body is nothing! If I expend death energy, I can restore it as many times as I wish! “Really? Then why haven’t you restored it yet?” - …Because some crazy human would just smash it again anyway. “Oh, correct.” Grind. The Skeleton Warlord had no teeth, so he ground his bone joints instead. The light in his eye sockets narrowed. - Why, vile human? “What?” - You must have an ulterior motive for giving me food—or rather, granting me such great power. You clearly have some sinister intention. Tell me the truth! I thought for a moment before answering. “Hmm. Because you’re a fucking weakling.” - Huh? “You can’t beat me anyway. If I’m going to drag you around, it’s easier to make use of a stronger, more useful fucking weakling, isn’t it?” - …! “Now get back inside. People are coming.” I put the creature, frozen with shock, back into my inventory and stood up. The airport duty-free corridor would normally have been packed with employees and passengers. Now it was empty and dark, and three people were walking toward me through the gloom. Two of them were familiar faces. “Mr. Jin Taekyung.” “Teacher Jin.” They were Team Leader Choi, who looked relatively presentable, and Shao Shen, the A-rank Hunter from China’s Public Security Armed Forces. A considerable amount of time had passed since the battle ended, but Shao Shen’s face was still covered in blood and dust, and exhaustion had sunk deep into his features. “So you were here.” I greeted Team Leader Choi with a glance and made an excuse. “Yes. I had something to take care of.” “Please, speak casually to me. Sibeol—no, Teacher Jin, you are a hero who saved me and my comrades. More than that, you saved the people of Zhonghua.” “……” Was it my imagination, or had he just been about to call me Sibeol-jwa? Whether he knew what I was thinking or not, Shao Shen continued in an extremely polite tone. “Fortunately, with the help of the two gentlemen from Peace Guild, we were able to repel the monsters. I would like to take this opportunity to thank you once again.” “Ah, yes. It was nothing. It was simply what needed to be done.” I waved my hands modestly, then glanced at Team Leader Choi. I had been worried that the Integrated Language Pack might malfunction and he would notice something strange. But since Shao Shen was the person I was speaking with, it seemed that even my words sounded like Chinese to Team Leader Choi. “But who is the gentleman beside you…?” The only unfamiliar person among them was a middle-aged man with half-gray hair. He had been listening silently to our conversation. Now he extended a hand for a handshake. “I am Wei Penghu, Minister of Defense at the Central Military Commission. It is a pleasure to meet you, Teacher Jin.” “The Minister of Defense…?” “My rank is Senior General.” “Oh.” I could tell he was an important man, but I had no idea what a Senior General was. Perhaps he read my thoughts, because Team Leader Choi whispered from beside me in a voice as tiny as an ant. “Four-star. Four-star.” “Oh, ohhh! So you’re a four-star general! Nice to meet you!” I had been a four-star once, too. The game I played as a kid had been a lot of fun. The sequel had flopped so hard it was practically in a league of its own. Wei Penghu smiled faintly at my reaction and clasped my hand. “Perhaps because you are young, you are full of vigor. I have much to ask Teacher Jin, but… shall we talk on the way?” “Sure, why not?” I started following Wei Penghu, then stopped. “But where are we going?” “To the operations headquarters. I have a jet standing by.” “What? Headquarters? A jet?” “That is correct. Everyone is waiting for Teacher Jin there.” Everyone? Who?

#### Chapter 383 tail (verified mastered)

…
Hunter like that?* Wei Penghu had spoken indirectly, but the meaning behind his words was clear enough. Team Leader Choi and I locked eyes in midair. At that moment, we were thinking the same thing. *An undisclosed S-rank Hunter.* No. More precisely, an S-rank Hunter deliberately concealed by the Chinese government. *I’d only heard rumors about things like this. So it was true?* An S-rank Hunter was practically the face of a nation. But unlike the weak, who struggled desperately not to be looked down on, the strong hid their claws. China was already known to possess two S-rank Hunters. Clearly, it had not wanted to reveal all its strength. Perhaps the same was true of the world’s other great powers. *Seriously. Even after going through the Great Cataclysm, they’re still jockeying for advantage like this.* It was pathetic. At the same time, I could almost understand it. Diplomacy. Politics. I felt as though I’d caught a glimpse of the truth of a world I’d never understood, and it left me with a strange feeling. Unlike me, however, Team Leader Choi was much sharper. “When you say Lei Fei ‘was’ one of your country’s S-rank Hunters, that sounds like the past tense.” Wei Penghu answered with a grim expression. “…A week ago, when the first monster wave occurred, Lei Fei disappeared. Along with the Hunters from the Public Security Armed Forces under his command.” “Are you certain he’s missing? Could he perhaps…” “We have not confirmed his death. After that video, the monster called the Lich—no, the Arch Lich—used mana to cut off all communications and surveillance.” Team Leader Choi and I groaned at the same time. Hearing our reaction, Wei Penghu asked in a hoarse voice, “Do you two also think Lei Fei is dead?” “Hmm.” “Uh…” *Missing. And if someone had gone missing in that hell a week ago, the ending was practically a foregone conclusion.* At Team Leader Choi’s signal, I cautiously opened my mouth. “Well, you never know how things will turn out, but…” “Other experts said he was one hundred percent dead. Useless blowhards, every last one of them.” *What’s wrong with you? They sound like real experts.* If anyone guaranteed he was alive under those circumstances, they should be fired immediately. That was simply a fact. “But I disagree. Lei Fei—that boy must still be alive.” “I hope so too, but realistically speaking…” “He is my only nephew. My sister was sickly from childhood and died in childbirth. I raised that tiny, unweaned infant as if he were my own son.” “What?” *A nephew? You raised him as your own son? What the hell is this?* I froze like a statue. Wei Penghu looked at me with tear-filled eyes. “But what were you going to say? After ‘realistically speaking,’ I mean.” *Fuck. This is the biggest crisis I’ve ever faced.* The words caught in my throat. I barely managed to squeeze out a reply. “Well, realistically speaking, I was going to say that there’s still some chance he might be alive.” “Is that so? Is that true?” “Yes. But that chance is extremely slim…” “Thank you, Teacher Jin!” “No, General. Commander. Great Leader. Just hold on a second and let me finish—” Grab! It was too late. Wei Penghu was no longer listening. Instead, he clasped my hand in both of his, his eyes brimming with tears. “May I ask you for one favor?” *I wish you wouldn’t.* Despite my desperate hopes, the words I’d been dreading pierced my heart a few seconds later. “If you happen to meet that boy someday, would you bring him back to me?” “…” “I beg you.” Over his desperately pleading shoulder, I saw Team Leader Choi shaking his head. *What if I’d just given him a firm answer from the beginning?* I regretted it, but it was already too late. In the end, there was only one answer I could give. “I will. But…” “Teacher Jin.” “Yes?” “You don’t have to say it. I’m already prepared for that.” “…!” Wei Penghu wiped the corners of his eyes with his sleeve. He was no longer a middle-aged man worrying about the safety of his blood relative. He had returned to being the Minister of Defense at the Central Military Commission. “This is enough. No one was willing to step forward, but you promised me. I can rest easy now.” “I can’t guarantee anything.” “What I needed was not someone’s bombastic guarantee. It was a thread of hope.” Just as Wei Penghu murmured those words, the aircraft glided toward the ground with a weightless sensation. Outside the window, amid the deep darkness, I could see rugged mountain terrain, lights moving ceaselessly, and military vehicles. “It looks like we’ve arrived.” I had been staring fixedly out the window as though possessed by something. Now I asked, “Where are we?” “The temporary operations headquarters.” “No. That’s not what I asked.” “Hmm?” “The mountain. That mountain feels strangely familiar.” “That’s impossible. As far as I know, you have never entered our country before… Ah, perhaps you saw it in a photograph?” “A photograph?” “It is a UNESCO-designated World Cultural Heritage Site, so that is entirely possible.” With a faint smile, Wei Penghu continued, “The temporary operations headquarters. Welcome to Mount Qingcheng.” [^1]: *Sundae-guk* is a Korean soup made with sundae, a type of Korean blood sausage, and is commonly served with rice.

## Korean source

```text
＃384화



청성산(靑城山).

아득한 세월을 간직한 도교의 성지.

그 준엄하고도 압도적인 산세를 마주한다면, 그 누구라 해도 순간 할 말을 잃고 바라보게 된다.

그러나 나는 전혀 다른 의미에서 놀라움을 느끼고 있었다.

‘분명 다르지만…… 닮았어.’

무림의 청성산. 그리고 21세기 현대의 청성산.

지금껏 내가 경험해 온 두 세상은 많은 부분을 닮았다. 무림에서의 지형, 언어, 사람들의 용모와 생활 양식까지.

한때는 어쩌면 무림은 현대의 머나먼 과거가 아닐까, 고민한 적이 있을 정도였다.

‘하지만 아니었지.’

나비효과? 영화에서나 보던 일이 일어났을 리가.

두 세상은 분명 닮았지만, 미묘한 차이가 있었고 역사도 달랐다.

또한 무림의 세상은 현대의 그것보다 좁고 오대양 육대주로 갈라져 있지도 않다.

이역만리의 이국땅에 색목인들이 살기는 하나 그뿐. 거대한 대국의 통치 아래 존재하는 대륙이 저쪽 세상의 중심이다.

중국 사람들이 지겹도록 주장하는 중화(中和)가 곧 무림일지도 모르겠다.

‘그런데 하필이면 이런 것까지 닮았냐.’

사천성을 무자비하게 피로 물들였던 삼문혈사(三門血史)를 겪고 돌아오자마자 쓰촨성의 청성산에 오다니.

단순한 우연인지, 지독한 악연인지 모르겠다.

부디 그런 것까지 닮진 않았으면 좋겠는데…….

「진 선생?」

“진태경 씨.”

“아.”

나는 잠에서 깨어난 사람처럼 고개를 쳐들었다.

어느새 비즈니스 제트기에서 내린 웨이펑후와 최 팀장이 나를 묘한 눈빛으로 바라보고 있었다.

“죄송합니다. 경치에 잠깐 한눈팔려서.”

「이토록 어두운데 청성산의 절경을 볼 수 있다니. 진 선생께서는 대단한 마나의 소유자시군.」

그것도 틀린 말은 아니지만, 초절정의 경지에 오른 지금은 굳이 공력 없이도 어지간하면 안력(眼力)으로 꿰뚫어 볼 수 있다.

내가 미묘한 얼굴로 고개를 끄덕이자 웨이펑후가 감탄했다.

「과연, 한국이 진 선생을 왜 그리 꼭꼭 숨겨 두었는지 이제야 알 것 같구려. 나라의 얼굴이라 할 만한 S급 헌터답소이다.」

“예? 저 아직 자격증으로는 A급인데요.”

「굳이 숨길 필요 없소. 본국에서도 어느 정도는 파악하고 있으니.」

뭐라 말하기도 전에 웨이펑후가 청산유수처럼 말을 이었다.

「S급 헌터가 되기 위해서는 끊임없는 정신 수양과 고된 수련을 통해 깨달음을 얻어야 하는 법. 본국도 수많은 시행착오를 겪어 가며 지금의 헌터들을 육성했는데…… 진 선생처럼 젊은 나이에 그런 경지에 올랐다는 것은 한국 정부의 전폭적인 지원이 있었다는 뜻이겠지.」

“……?”

“……?”

「아, 물론 옆에 계신 최 선생도 훌륭한 헌터요. 이런 분들이 함께하니 나로서는 든든할 뿐이오.」

이게 무슨 든든하게 국밥 말아먹는 소리냐.

짧은 순간 시선을 교환한 나와 최 팀장은 무언의 합의를 보았다.

‘입 다물자.’

‘그냥 갑시다.’

내가 너무 비현실적으로 이 자리까지 올라왔기 때문에 벌어진 해프닝인 듯싶은데, 이미 저쪽에서 붙인 딱지를 굳이 우리 손을 떼 줄 필요는 없다.

당장 이 자리에서 웨이펑후를 납득시키기도 귀찮고.

“음, 약간 오해가 있으신 것 같은데, 때가 되면 제가 차차 말씀드릴게요.”

「오해랄 것 있겠소. 서로 다 사정 아는 처지에.」

“…….”

“…….”

「주석께서도 이미 알고 계신 사안이니, 뵙게 되면 구태여 부정하지 말고 그러려니 하시오.」

알긴 뭘 알아. 나는 피식 웃었다.

‘그나저나 주석이라.’

중화 인민공화국에 존재하는 10억여 명의 인구와 경제, 군사를 한 손에 틀어쥔 왕 같은 존재.

초절정의 경지에 오른 지금에도 현대의 상식이 뿌리박힌 내게 그는 가까우면서도 한없이 먼 존재다.

이번 일이 끝나면 얼굴이나 한 번 볼 수 있으려나?

뭐, 무슨 상관이겠나. 이건 한참 나중에 생각해야 할 문제다.

레이드 수당을 제외하더라도 주급이 무려 백억. 지금의 내게는 손 큰 고용주일 뿐이다. 사람도 구하고, 돈도 버니 일석이조다.

“그렇게 하겠습니다. 뵙게 되면요.”

「좋소. 그럼 뵈러 갑시다.」

“예?”

「내가 말하지 않았나? 지금 지하 벙커에서 기다리고 계시오.」

아니, 이게 도대체 뭔 상황이야.

앞서가는 웨이펑후의 뒷모습을 멍하니 바라보던 나는 최 팀장에게 다가가 빠르게 속삭였다.

“바, 방금 들으셨어요?”

“예, 들었습니다. 하지만 저로서도 좀 의외로군요. 국가 주석이 안전한 베이징을 놔두고 여기까지 오다니. 세간의 평가가 어느 정도 사실인 모양입니다.”

“세간의 평가고 나발이고. 중국 종석이, 종석이가!”

“종석이가 아니라 총서기! 국가 주석이라고!”

「음? 방금 뭐라 하셨소?」

「아무것도 아닙니다. 국방부장님.」

문득 뒤돌아본 웨이펑후를 향해 정중하게 둘러댄 최 팀장이 지금껏 본 적 없는 아주 진지하고 간절한 표정으로 말했다.

“진태경 씨. 주석 앞에서 지금 같은 말실수는 하면 안 됩니다. 아시겠죠? 특히 종석이 얘기는 말도 꺼내지 마세요. 무슨 고등학교 동창 이름도 아니고.”

“어? 어떻게 아셨어요?”

“…….”

방금 최 팀장이 시발이라고 한 것 같은데. 기분 탓이겠지.

나는 깊게 심호흡하며 속으로 중얼거렸다.

‘종석이 아냐. 총서기야. 중국 주석이야.’

태생부터 성골 귀족이었던 최 팀장과 달리 나는 뼛속까지 소시민이다.

평소 중국에 어떤 감정을 품고 있었건 간에, 세계에서 열 손가락 안에 꼽히는 강대국의 지도자를 만난다는 사실에 가슴이 쿵쿵 뛰었다.

‘실수만 하지 말자. 특히 종석이.’

그리고 십 분 후, 나는 깊숙한 지하 벙커에 모인 주요 인물들의 시선을 받으며 중화인민공화국의 지도자와 악수를 나누었다.

「반갑소, 진 선생. 이 늙은이는 중화인민공화국의 국가 주석을 맡고 있는 샤오 양이라 하오.」

좋아, 종석이의 종자도 꺼낼 일은 없다. 한고비를 넘긴 나는 편안한 마음으로 입을 열었다.

“어서 오세요.”

「……?」

“……?”

아, 시벌.



* * *



중국 공산당 중앙군사위원회 주석이자 총서기. 그리고 10억 명이 넘는 인민들의 정점에 선 국가 주석.

샤오 양(Shao Yang).

사람들을 향한 그의 목소리는 부드럽고, 눈빛에는 힘이 실려 있었다.

「여러분도 알다시피, 안타깝게도 나는 군사 전문가도, 뛰어난 장군도 아니오. 일찍이 정치에 몸담아 나이 일흔이 되어서야 작은 뜻을 이룬 협잡꾼일 뿐이지.」

스스로를 협잡꾼이라 지칭하는 말은, 지구에서 네 번째로 거대한 국토와 제일의 인구수를 지닌 국가 수장의 입에서 나온 말이라곤 믿기지 않을 정도로 파격적이었다.

‘이런 뜻이었나? 최 팀장이 말했던 세간의 평가라는 게.’

대충 어떤 사람인지 알 것 같은 느낌이다.

어쩌면 그저 사람들 앞에서 꺼내 든 가면이나 위선일 수도 있다.

하지만 적어도 지금 나를 포함한 모두의 앞에서 말을 이어 가는 노인, 샤오 양 중국 주석에게는 그런 것과는 전혀 다른 종류의 기(氣)가 느껴졌다.

「최선을 다해 주시오. 부디 한 명이라도 더 많은 인민을 구하고, 하루빨리 이 끔찍한 참사를 막아 주시오. 만약 그리 해 주신다면 나는 여러분과 여러분의 나라에 합당한 고마움을 표시하고 이번에 준 도움을 오래도록 기억할 거요.」

사실 저 노인이 어떤 인생을 살아왔고 어떤 정책을 펼치는지 나는 모른다.

다만 자국의 사람들을 구하기 위해 세계 각국에 도움의 손길을 뻗었다는 것에는 큰 점수를 주고 싶다.

「이 늙은이의 말은 여기까지요. 여러분들은 부디 정치와 같은 복잡한 문제는 신경 쓰지 말고, 최소의 희생으로 이 사태를 막을 수 있는 최선의 방도를 찾아 주시길 간곡히 부탁하겠소.」

정치에 일평생을 바친 늙은 정객(政客)은 고개를 돌려 한 사람을 바라보았다.

「웨이펑후 국방부장. 내 오랜 벗이여.」

「예. 존경하는 주석 동지.」

「중앙군사위원회의 전권을 원하나?」

잠시 망설이던 웨이펑후가 무겁게 고개를 끄덕였다.

「그렇습니다.」

「자네라면 그 힘을 잘 사용할 수 있겠지. 하지만 거절하겠네.」

「……주석 동지?」

「회의가 끝나면 명령서를 가져오게. 모든 일의 전권도, 책임도 내가 질 테니.」

순간 중국 종석이가 왜 저러나 싶었는데, 이제 보니 모두 자신이 안고 가겠다는 의지의 표명이었다.

그 광경을 지켜보던 최 팀장이 옆에서 중얼거렸다.

“좋은 리더군요.”

나는 작게 고개를 저었다.

“아뇨. 저한테는 최 팀장님이 최곱니다.”

“진태경 씨…….”

“그러니까 길드 정산 비율 좀 올려 주세요.”

“진태경 씨…….”

같은 말, 다른 느낌.

니 새끼가 그럼 그렇지, 하는 눈빛으로 나를 바라본 최 팀장이 고개를 젓던 그때였다.

「주석께서 퇴장하십니다.」

서기관의 말에 앉아 있던 모두가 자리에서 일어났다. 국가 원수에 대한 최소한의 예우다.

「모쪼록 무운을 비오.」

주석은 이 자리에 있는 한 사람, 한 사람과 눈을 맞추며 말을 건넸다. 물론 나 역시 예외는 아니었다.

그것도 하필이면 맨 마지막에 걸렸다.

「진 선생.」

“……예.”

나를 바라보는 주석의 입가에 희미한 미소가 스쳤다.

「내 진 선생에게 거는 기대가 아주 크오. 비록 서로가 필요로 하는 것을 주고받는 계약이라지만, 어떤 상황에서도 인명을 우선해 주었으면 좋겠소.」

기분 탓인가, 다른 사람들에 비해 유난히 긴 인사말이다. 나는 사람들의 시선을 느끼며 고개를 끄덕였다.

“알겠습니다.”

「부디 꼭 큰 힘이 되어 주시구려.」

그 말을 끝으로 돌아서려던 주석이 멈칫 발걸음을 멈췄다. 그리고 한 마디를 툭 던졌다.

「어서 오시오.」

“…….”

「그럼 이만.」

주석을 배웅하기 위해 동석하고 있던 중국 고위 관계자들이 사라지고, 나는 의자에 털썩 주저앉았다.

‘시벌.’

만약 내가 죽는다면 사인은 수치사다. 설령 몬스터한테 죽는다고 해도 사인은 수치사로 하기로 했다.

‘으아, 으아아아아!’

마음속으로 온 사방을 향해 울부짖는 내 발을 무언가가 지그시 밟았다. 보나 마나 옆에 앉은 최 팀장이 분명했다.

“왜요.”

최 팀장이 작게 헛기침을 내뱉었다.

“크흠.”

“뭐요.”

“크흐흠. 사람들, 사람들.”

“아.”

주위를 둘러본 나는 그제야 깨달았다. 지하 벙커 안, 남녀와 인종이 뒤섞인 십여 명의 사람들이 나를 주시하고 있었다는 것을.

그리고 그중에서도 특히 눈에 띄는 네 사람이 있었다.

‘저들은…….’

중국인 남녀 한 쌍. 그리고 각각 초록빛과 푸른빛을 띤 서양인 사내 둘.

시선을 마주한 것만으로도 느껴진다. 그들의 몸 안에 웅크린 거대한 기운이.

놀랍다기보다는 당연하다는 생각이 앞섰다. 저 네 사람의 정체를 아는 이들이라면 누구나 나와 같을 것이다.

‘S급 헌터.’

존재 자체가 이슈인 사람들. 전 세계에 존재하는 수많은 헌터 중에서도 정점에 선 이들.

TV와 광고에서 지긋지긋하게 보던 얼굴들이 내 눈앞에 있었다.

그리고 지금, 그중 한 사람이 일어나 내게 손을 내밀었다.

「만나서 반가워. 나는……. 아, 혹시 영어를 잘 모르나? 통역 마법을 써 줄 수도 있는데.」

먼저 말을 걸어 줄 거라고는 생각지도 못했다. 나는 얼떨떨한 얼굴로 그가 내민 손을 맞잡으며 대답했다.

“아닙니다. 괜찮아요.”

「오, 이 친구 발음 보게. 미국인이라고 해도 믿겠는데.」

중년의 흑인. 2미터를 훌쩍 넘기는 거구의 그가 푸른 눈을 빛내며 물었다.

「내가 누군지 아는 것 같은데. 안 그래?」

모를 리가 있나. 나는 샤오 양 주석을 마주했을 때보다 더한 떨림을 느끼며 대답했다.

“물론입니다, 매직 존슨(Magic Johnson).”

전 세계에서 오직 세 명만이 부여받은 대마법사의 칭호.

눈앞의 흑인, 매직 존슨은 그 대마법사 중에서도 가장 전투에 특화되어 있다는 워 메이지(War Mage)다.

‘매직 존슨이랑 이야기를 하다니. 살다 보니 이런 날도 다 오네.’

여러모로 오길 잘했다고 생각하는 내게, 세계 최고의 워 메이지가 활짝 웃으며 말을 건넸다.

「하하. 알아봐 주니 고맙군. 사실 나도 전부터 널 알고 있었어.」

“저, 절요?”

「당연하지. 올해 초등학교에 입학한 내 막내딸도 시벌좌를 아는걸.」

“…….”

아니, 저 염병할 별명은 도대체 어디까지 알려진 거야.

시벌좌라는 별명이 영미권에서는 뭐라고 불리려나. 퍽 가이? 퍽 맨?

매직 존슨의 어린 막내딸이 나를 그런 이름으로 알고 있다고 생각하니 하나도 기쁘지 않다.

그리고 기분이 좋지 않은 것은 나뿐만이 아니었던 모양이었다.

「천박하기 짝이 없는 별명이군. 뭐, A급 헌터 나부랭이에게 딱 어울리긴 하지만.」

이제 막 서른쯤 되었을까. 비교적 젊어 보이는 중국인 사내가 비스듬히 팔짱을 끼며 나를 응시했다.

「안 그래, 반도의 빵즈?」

최 팀장이 말릴 틈도 없었다. 이미 내 목소리는 자동 응답기처럼 흘러나온 후였으니까.

“뭐래, 대륙 짱깨 새끼가.”
```

## Current accepted English baseline

```markdown
# Chapter 384

Mount Qingcheng.

A sacred Taoist site that had preserved the passage of countless ages.

Anyone who faced its stern, overwhelming mountain terrain would find themselves momentarily speechless, staring in awe.

But I was feeling a completely different kind of surprise.

*They’re definitely different… but they look alike.*

Mount Qingcheng in the Murim. And Mount Qingcheng in the modern world of the twenty-first century.

The two worlds I had experienced so far were similar in many ways—the terrain, the language, and even the appearance and lifestyles of their people.

At one point, I had even wondered whether the Murim might be the modern world’s distant past.

*But it wasn’t.*

The butterfly effect? There was no way something I’d only seen in movies had actually happened.

The two worlds were certainly similar, but they had subtle differences, and their histories were different as well.

The world of the Murim was also smaller than the modern world. It wasn’t divided into five oceans and six continents.

People with colored eyes did live in foreign lands thousands of miles away, but that was all. The center of that world was a continent ruled by a vast and powerful nation.

Perhaps the Zhonghua that the Chinese people insisted on so tirelessly was the Murim itself.

*But why did even this have to look alike?*

I had just returned from the Three-Sect Bloodbath, which had mercilessly dyed Sichuan Province in blood, only to come to Mount Qingcheng in Sichuan Province.

I didn’t know whether it was a simple coincidence or a cursed connection.

I just hoped even that wasn’t similar…

“Teacher Jin?”

“Mr. Jin Taekyung.”

“Huh?”

I lifted my head like someone waking from sleep.

Wei Penghu and Team Leader Choi had already gotten off the business jet and were looking at me with strange expressions.

“Sorry. I got distracted by the scenery for a moment.”

“You can see Mount Qingcheng’s beauty in this darkness. You must possess tremendous mana, Teacher Jin.”

That wasn’t entirely wrong, but now that I had reached the Supreme Peak realm, I could see through most things with my eyesight alone, without even using internal energy.

When I nodded with a subtle expression, Wei Penghu exclaimed in admiration.

“Now I understand why Korea has hidden you away so carefully. You truly are worthy of being called an S-rank Hunter—the face of your nation.”

“What? I’m still A-rank according to my license.”

“There’s no need to hide it. Our country has figured it out to some extent as well.”

Before I could say anything, Wei Penghu continued as smoothly as flowing water.

“To become an S-rank Hunter, one must gain enlightenment through constant mental cultivation and arduous training. Our country has also raised its current Hunters through countless trials and errors… Reaching such a realm at your young age means you must have received the full support of the Korean government.”

“…”

“…”

“Ah, of course, Teacher Choi beside you is also an excellent Hunter. Having people like the two of you with us is reassuring.”

*What was this nonsense about feeling reassured? Was he talking about a hearty bowl of gukbap or something?*

Team Leader Choi and I exchanged glances for a brief moment and reached a silent agreement.

*Keep your mouths shut.*

*Let’s just go.*

This seemed to have happened because I had reached this position in such an utterly unrealistic way. But there was no reason to remove the label they had already stuck on us.

Besides, convincing Wei Penghu right here and now sounded exhausting.

“Well, I think there’s been a slight misunderstanding. I’ll explain everything little by little when the time comes.”

“What misunderstanding? We’re both in a position to know the circumstances.”

“…”

“…”

“The Chairman already knows about the matter, so when you meet him, don’t bother denying it. Just accept it.”

*What does he know?*

I let out a quiet laugh.

*Speaking of the Chairman…*

A kinglike figure who held the population, economy, and military of the People’s Republic of China’s billion-plus people in one hand.

Even now that I had reached the Supreme Peak realm, to me—with modern common sense still rooted deep in my bones—he felt both close and infinitely distant.

*I wonder if I’ll get to see his face once this is over.*

Well, what did it matter? That was a problem for much later.

Even without my raid pay, my weekly salary was a whopping ten billion won. To me, he was merely a generous employer.

I could save people and make money at the same time. Two birds with one stone.

“That’s what I’ll do. If I meet him.”

“Good. Then let’s go meet him.”

“What?”

“Didn’t I tell you? He’s waiting in the underground bunker right now.”

*What the hell was going on?*

I stared blankly at Wei Penghu’s back as he walked ahead, then approached Team Leader Choi and whispered quickly.

“D-Did you hear that?”

“Yes, I did. But it’s somewhat unexpected to me as well. For the Chairman of China to leave the safety of Beijing and come all the way here… The public perception of him must be at least somewhat accurate.”

“To hell with public perception. China’s Jongseok—Jongseok!”

“Not Jongseok! The General Secretary! The state chairman!”

“Hmm? What did you just say?”

“Nothing, Comrade Minister of Defense.”

Team Leader Choi politely covered for us when Wei Penghu suddenly glanced back. Then, wearing an extremely serious and earnest expression I had never seen before, he spoke to me.

“Mr. Jin Taekyung. You must not make a slip like that in front of the Chairman. You understand? Especially the Jongseok thing. Don’t even bring it up. It’s not as though you’re talking about the name of some high school classmate.”

“Huh? How did you know?”

“…”

I could have sworn Team Leader Choi had just said *fuck*.

It was probably just my imagination.

I took a deep breath and muttered inwardly.

*Not Jongseok. The General Secretary. China’s Chairman.*

Unlike Team Leader Choi, who had been born into aristocracy, I was a commoner down to my bones.

Whatever feelings I usually had toward China, the thought of meeting the leader of one of the world’s ten greatest powers made my heart pound.

*Let’s just not make any mistakes. Especially not about Jongseok.*

Ten minutes later, I stood amid the gazes of the important figures gathered in a deep underground bunker and shook hands with the leader of the People’s Republic of China.

“Nice to meet you, Teacher Jin. This old man is Xiao Yang, the state chairman of the People’s Republic of China.”

*Good. I won’t even have to utter the first syllable of Jongseok.*

Having cleared the first hurdle, I opened my mouth with a relaxed mind.

“Welcome.”

“…”

“…”

*Oh, fuck.*

* * *

Chairman of the Central Military Commission of the Chinese Communist Party and General Secretary.

And the state chairman standing at the pinnacle of more than a billion people.

Xiao Yang.

His voice was gentle as he spoke to the people gathered there, but his eyes held power.

“As you all know, unfortunately, I am neither a military expert nor an outstanding general. I am merely a political schemer who entered politics early and achieved one small ambition only after reaching the age of seventy.”

The fact that he referred to himself as a schemer was so audacious that it was difficult to believe the words had come from the leader of a nation with the fourth-largest territory and the largest population on Earth.

*Was this what Team Leader Choi meant by the public perception of him?*

I felt as though I had a rough idea of what kind of person he was.

Perhaps it was merely a mask or hypocrisy he had put on before the people.

But at least from the old man continuing to speak before all of us—including me—Chairman Xiao Yang of China, I sensed a kind of qi entirely different from either of those things.

“Please do your utmost. Save as many of our people as possible, and stop this terrible disaster as soon as you can. If you do so, I will express my gratitude to you and your country in a manner befitting your efforts, and I will remember the help you have given us for a long time.”

I knew nothing about the life that old man had lived or the policies he had pursued.

But I wanted to give him considerable credit for reaching out to countries around the world for help in order to save his own people.

“That is all this old man has to say. I earnestly ask you not to concern yourselves with complicated matters like politics. Please find the best way to stop this situation with the fewest possible sacrifices.”

The old politician, who had devoted his entire life to politics, turned his head and looked at one man.

“Minister of Defense Wei Penghu. My old friend.”

“Yes, Comrade Chairman.”

“Do you want full authority over the Central Military Commission?”

Wei Penghu hesitated for a moment, then gave a heavy nod.

“Yes.”

“You would use that power well. But I will refuse.”

“…Comrade Chairman?”

“When this meeting is over, bring me the written order. I will take full authority over every matter and bear all the responsibility myself.”

For a moment, I wondered why China’s Jongseok was acting that way.

But now I understood. It was his declaration that he would shoulder everything himself.

Team Leader Choi muttered beside me as he watched the scene.

“He’s a good leader.”

I shook my head slightly.

“No. To me, Team Leader Choi, you’re the best.”

“Mr. Jin Taekyung…”

“So please raise my Guild settlement percentage.”

“Mr. Jin Taekyung…”

Same words. Different feeling.

Team Leader Choi looked at me as if to say, *Of course you’d say that, you bastard,* and shook his head.

That was when it happened.

“The Chairman is leaving.”

At the secretary’s words, everyone who had been seated rose from their places.

It was the minimum courtesy owed to a head of state.

“I wish you all good fortune.”

The Chairman looked each person in the eyes as he spoke to them.

Of course, I was no exception.

As luck would have it, I was the last one.

“Teacher Jin.”

“…Yes.”

A faint smile touched the corners of the Chairman’s mouth as he looked at me.

“I have very high hopes for you, Teacher Jin. Though this is a contract in which we exchange what we each need, I hope that you will put human lives first in every situation.”

Was it my imagination, or was his farewell unusually long compared to everyone else’s?

Feeling everyone’s eyes on me, I nodded.

“I understand.”

“Please be a great source of strength to us.”

The Chairman finished speaking and was about to turn away when he abruptly stopped.

Then he tossed out one more word.

“Welcome.”

“…”

“Well, that will be all.”

After the high-ranking Chinese officials who had been present to see the Chairman off disappeared, I dropped heavily into a chair.

*Fuck.*

If I died, the cause of death would be humiliation.

Even if a monster killed me, I would insist that the cause of death be recorded as humiliation.

*No! Nooooooo!*

As I screamed inwardly in every direction, something pressed down firmly on my foot.

It was obviously Team Leader Choi, who was sitting beside me.

“What?”

Team Leader Choi gave a small cough.

“Ahem.”

“What?”

“Ahem. People. People.”

“Oh.”

I looked around and finally realized that more than a dozen men and women of different races were watching me inside the underground bunker.

Four of them stood out in particular.

*Those people are…*

A Chinese man and woman.

And two Western men, one tinged with green and the other with blue.

I could feel it just from meeting their eyes—the immense power coiled inside their bodies.

My first thought wasn’t that it was surprising, but that it was only natural. Anyone who knew the identities of those four would have thought the same thing.

*S-rank Hunters.*

People whose very existence was news. Those who stood at the pinnacle of the countless Hunters in the world.

The faces I had seen to death on television and in advertisements were right in front of me.

And now, one of them stood up and extended a hand toward me.

“Nice to meet you. I’m… Ah, do you perhaps not speak English? I can use translation magic if you’d like.”

I hadn’t expected him to speak to me first. Looking flustered, I took his hand and answered.

“No, it’s fine.”

“Oh, listen to this fellow’s pronunciation. I’d believe you if you told me you were American.”

The middle-aged Black man was a giant well over two meters tall. His blue eyes gleamed as he asked,

“You seem to know who I am. Don’t you?”

As if I wouldn’t.

I felt even more nervous than I had when facing Chairman Shao Yang.

“Of course, Magic Johnson.”

The title of Archmage had been bestowed upon only three people in the entire world.

The Black man standing before me, Magic Johnson, was a War Mage—the most combat-oriented of those three Archmages.

*I’m talking to Magic Johnson. I guess days like this really do come along.*

As I thought that I had made the right choice in coming here, the world’s greatest War Mage smiled broadly and spoke to me.

“Haha. I’m glad you recognized me. Actually, I’ve known about you for a while too.”

“M-Me?”

“Of course. Even my youngest daughter, who started elementary school this year, knows Sibeol-jwa.”

“…”

*How far has that damn nickname spread?*

What would they call the nickname Sibeol-jwa in the English-speaking world?

*Fuck Guy? Fuck Man?*

The thought of Magic Johnson’s little youngest daughter knowing me by that name was not flattering in the slightest.

And apparently, I wasn’t the only one who disliked it.

“That is an obscenely vulgar nickname. Though I suppose it suits a mere A-rank Hunter like you.”

A Chinese man who looked to be around thirty, relatively young, stared at me with his arms folded at an angle.

“Isn’t that right, you peninsula bangzi?”[^1]

Team Leader Choi didn’t even have time to stop him.

My voice had already come out like an automatic response.

“What are you saying, you mainland chink bastard?”

[^1]: *Bangzi* is a derogatory Chinese slur for Koreans.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 384`.

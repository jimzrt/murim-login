# Master Edit Task — Chapter 387

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
| 이정룡    | **Lee Jungryong** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 내공     | **internal energy**                              |                                                       |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 검법     | **sword technique**                              |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 장비               | **Equipment**                  |
| 습득               | **Acquired**                   |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 사천     | **Sichuan**            |
| 공자      | **Young Master**                                                |
| 우헤이싱 | **Wu Heixing** | S-rank Hunter antagonistic toward Taekyung. |
| 대마법사 | **Archmage** | Title held by only three people worldwide. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 우헤이싱 | 이정룡 | junior_s_rank_hunter_to_top_s_rank_hunter | Mr. Lee | intimidated-deferential | Uses 이 선생님 and suppresses his usual hostility in Lee's presence. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 380–384

## Plot

At Chengdu International Airport, Jin Taekyung and Team Leader Choi survive their burning jet’s crash into the monster army and join Shao Shen’s defense. Taekyung discovers that nearly half the army consists of undead controlled by an unidentified force. The Skeleton Warlord seizes control of roughly two hundred nearby undead, turning them against the living monsters while the Chinese Hunters counterattack.

Three incomplete Liches, former human necromancers serving an Arch Lich, command the assault. They strengthen their army by harvesting death energy from soldiers and attempt to create increasingly powerful undead, but Taekyung reaches them before they can complete a Death Knight. He destroys all three, using Scorching Yang Qi against one and ordering the Skeleton Warlord to consume the other two. The Unexpected Assault Quest is completed, granting Taekyung the **Undead Hunter** Title, EXP, Fame, and a level up; the Skeleton Warlord becomes substantially stronger.

Taekyung is taken to Mount Qingcheng, where Senior General Wei Penghu explains that the monster wave began in Gaoping District, Nanchong City, after a sudden mana surge. Lei Fei, China’s previously undisclosed S-rank Hunter and commander of the Sichuan Public Security Armed Forces, disappeared with his Hunters while investigating the incident. Wei, who raised Lei Fei as his own son, asks Taekyung to bring him back if he is found. Taekyung agrees without promising that Lei Fei is alive.

At the underground operations headquarters, state chairman Xiao Yang personally asks Taekyung and the assembled international Hunters to save as many people as possible. He retains overall authority rather than granting Wei Penghu unrestricted control. The bunker contains several S-rank Hunters, including the Archmage and War Mage Magic Johnson, who recognizes Taekyung’s Sibeol-jwa nickname. A young Chinese Hunter insults Taekyung as a peninsula bangzi; Taekyung answers with an equally offensive insult.

## Continuity

- Taekyung and Team Leader Choi are cooperating with China to stop the Sichuan disaster and locate Lei Fei and the missing Sichuan Hunters.
- Chengdu International Airport’s monster army was controlled by three incomplete Arch Liches, all destroyed by Taekyung and the Skeleton Warlord.
- The three Arch Liches served an Arch Lich and swore upon the River of Death that their account of their origins and orders was truthful; the relationship between them and the earlier Lich remains unresolved.
- The Skeleton Warlord absorbed substantial death energy and is much stronger, but the full extent and persistence of the increase remain unknown.
- The monster wave began in Gaoping District, Nanchong City, following a sudden mana surge. Magical interference disrupts communications throughout wartime Sichuan.
- Lei Fei is Wei Penghu’s only nephew and was raised by Wei as his son. Lei Fei’s fate and the fate of his missing unit remain unresolved.
- Wei Penghu is a Senior General and Minister of Defense at the Central Military Commission. Xiao Yang is its Chairman, the Communist Party’s General Secretary, and the state chairman of the People’s Republic of China.
- Xiao Yang has personally tasked the Hunters with minimizing casualties while retaining full responsibility and authority.
- Magic Johnson is an S-rank Hunter, one of the world’s three Archmages, and a combat-specialized War Mage. At least four other unnamed international S-rank Hunters are present.
- Taekyung’s exact post-level-up Level, Fame, Titles, martial-art stages, and unassigned points remain unstated.
- Dark Heaven, the hidden transport formation, the Sichuan Tang Clan’s relocation, Mungyeong’s response to the coming war, the port boy’s identity, and Ae-hyang’s superior remain unresolved.
- The monster wave’s larger plan, the Arch Lich’s identity, and the reason for the mana surge remain unresolved.
- The insult exchange between Taekyung and the young Chinese Hunter remains an immediate interpersonal tension.

## Translation Decisions

- Preserve **Undead Hunter**, **Sibeol-jwa**, **Teacher Jin**, **Lei Fei**, **Wei Penghu**, **Gaoping District**, **Nanchong City**, **Mount Qingcheng**, **Magic Johnson**, **Archmage**, and **War Mage**.
- Render **중앙군사위원회** as **Central Military Commission**, **국가 주석** as **state chairman**, and **총서기** as **General Secretary**.
- Preserve the **Jongseok** mishearing joke for General Secretary and the official forms **Comrade Minister of Defense** and **Comrade Chairman**.
- Render **반도의 빵즈** as **peninsula bangzi**, retaining a footnote identifying *bangzi* as a derogatory Chinese slur for Koreans.
- Preserve Taekyung’s Sibeol-jwa nickname, self-mocking voice, death-by-humiliation joke, and the deliberately offensive insult exchange.

### Prior accepted reading-copy tails

#### Chapter 385 tail (verified mastered)

…
damage to the back of his hand. Or even just one finger. - I said no! I hadn’t known Message Magic could carry this much emotion. Team Leader Choi must have been desperate in his own way. *Fine. He’s a British prince. It can’t be helped.* I was trying to swallow my anger when— “Hey, Sibeol-jwa.” *What now?* I looked warily at Magic Johnson, who had suddenly approached me. I hadn’t expected much from Wu Heixing, who was infamous for his anti-Korean sentiment and various scandals in the first place. But the joy of seeing in person the S-rank Hunters I had only watched on television was gradually running out. “…No, please. Call me by my name instead of Sibeol-jwa. Would you like it if I called you Fuckson instead of Johnson?” “Hmm. Now that you mention it, I see your point. Jin, then?” “That’s much better. But why?” “It’s nothing special. You’re not thinking of kissing the prince’s hand, are you?” *That sounds pretty special to me.* Taken aback, I immediately asked, “Of course not. What is this, the Middle Ages? Would you want to if you were me, Johnson?” “I would.” “What?” A flash of enlightenment struck my mind. I had completely forgotten. Magic Johnson was an American national hero—and the nation’s gay icon. *Time* magazine’s choice for “the world’s most influential LGBT person” looked at me with a perfectly serious expression and made a proposal. “So I’d like to express your gratitude to the prince on your behalf.” “…” What a way to package it. But unlike Magic Johnson, Prince Felix quietly withdrew his hand. “We are all equal human beings beneath God. This antiquated etiquette must disappear. Magic Johnson, I will accept your kind offer at a later time.” “…” *Was that really something the bastard who had just held out his hand to me could say?* Pai Chen had been listening too. Apparently just as dumbfounded, she muttered, “Oh my. He’s shameless. He may not be a criminal, but he might be even worse than Wu Heixing.” “Even so, he’s better than Wu Heixing. That bastard should have been executed under the law.” “That’s true.” Wu Heixing had shriveled in the presence of one heavyweight after another, but now sparks flew from his eyes. “Th-this, this, this bangzi bastard!” “Enough with the bangzi routine. Even the national anthem gets hard to get through from the second verse onward. The same goes for me going easy on you.” “……Going easy on me? You? On me?” His tone made it clear that he genuinely couldn’t understand. I nodded. “Yeah. It just became obvious.” I had a pretty good idea what level Wu Heixing was at, but he hadn’t realized in the slightest who I was. A fight starts with sizing up your opponent. This one was over before it even began. “So stop picking fights for no reason and leave while I’m still asking nicely. Let’s each focus on doing our own jobs.” “You’re a mere A-rank Hunter, yet because Comrade Chairman expects great things from you, you’ve forgotten your place and started running wild—!” “Ah.” I’d been wondering why he had acted like an asshole from the moment we met. So that was it. The reason was so obvious and childish that a dry laugh escaped me. “Still, calling it cute would be a stretch. You’re too damn old.” “…!” “What are you going to do? You want all of the Chairman’s expectations and attention for yourself, but some Korean guy has edged you out.” “You…” Wu Heixing’s face flushed with shame and fury as he realized I had seen through his thoughts. By now, everyone’s attention was fixed on us. He must have felt their contemptuous stares all the way to his bones. And when people like him found themselves in situations like this… *They always cross the line.* My prediction was dead on. A faint movement. His fingertips slid almost imperceptibly toward the hilt of his sword. The magnanimous Chairman Xiao Yang hadn’t asked anyone present to disarm as a sign of trust, but that consideration would be poison to Wu Heixing. *Draw it. Don’t hesitate.* No matter how reckless I might seem, I did at least consider the circumstances. I had held back until now only because I had come to help China at the Chairman’s request. If Wu Heixing drew a weapon, I would have grounds to rough him up within reason. *That’s it. More. More.* As if he were being controlled by me, Wu Heixing’s hand reached for the hilt. Just as he was about to seize it— Step. Step. Several sets of footsteps echoed through the hallway outside the quiet underground bunker. Wu Heixing’s hand stopped, and the tightly shut door opened at almost the exact same moment. The moment I saw the man who entered alongside Minister of Defense Wei Penghu, Wu Heixing’s existence vanished from my mind. “I’m too late. Have you all been waiting long?” Bold features that looked as though they had been painted with a brush, and a solid build that even his clothes couldn’t conceal. He looked like a middle-aged man barely into his forties, but beneath that skin lurked an old tiger and a cunning snake. *Lee Jungryong.* When Lee Jungryong’s eyes met mine, a deep smile formed at the corners of his mouth. [^1]: *Bangzi* is a derogatory Chinese slur for Koreans.

#### Chapter 386 tail (verified mastered)

…
Stroking his beard, he began to speak. “Listening to the Minister of Defense, I find myself so frustrated that I have to speak. At this rate, how long will it take us to deal with those monsters?” *Wow…* His tone was unbelievably obnoxious. He was talking that way to Wei Penghu—the Chairman’s right-hand man and the military’s highest-ranking power broker. As if he had read my question, Team Leader Choi sent me a Message Spell. - The Communist Party has factions too. Senior General Liao is a pure-blooded member of the Princelings, the Communist Party’s largest faction, going back to his grandfather’s generation. They’re rivals of the Shanghai clique, which Chairman Xiao and Minister of Defense Wei Penghu belong to. - The Princelings and Shang… what? - …If we’re being precise, it means the Princelings are number one and the Shanghai clique is number two. - Ah. Until now, I had assumed that the Communist Party operated under a strict one-party system. Apparently, they fought each other tooth and nail too. - But is that allowed? If Chairman Xiao simply points at someone and says, “That man is dangerous,” wouldn’t that person be beheaded in Tiananmen Square? - They do it because they’re allowed to. - …Right. When you put it that way, I’ve got nothing to say. - The factions reached an agreement. During the Great Cataclysm, the Chairman from the Princelings made so many mistakes that they felt awkward about continuing to hold power. - Ah. Pingping? - Yes. Pingping. That damn Great Cataclysm really had changed all kinds of things. While I was listening to Team Leader Choi’s explanation, Senior General Liao—who apparently came from the Princelings’ pure-blooded younger generation—made an absolutely brilliant proposal. “Let’s use nuclear weapons.” “…” “…” “Let’s formally request it from Chairman Xiao and fire dozens of nuclear weapons across all of Sichuan. Wouldn’t that solve everything cleanly?” “…” “…” What a lunatic nuclear-happy bastard. Everyone, myself included, stared at each other in disbelief. Wei Penghu’s expression was especially spectacular. He answered with the face of a man who desperately wanted a pistol. “Rejected.” “Why? Are you dismissing me because I’m not part of the Shanghai clique?” “Say something that makes sense. Something that makes sense! If we do that, what happens to the people who are still alive or haven’t been harmed? What about the land we leave barren?” “Sacrificing the few for the sake of the many is unavoidable!” Forget the rest—he just sounded like an ox head to me.[^1] Magic Johnson, who had been listening quietly, suddenly spoke in his deep voice. “The damage from a successful nuclear attack is bad enough, but what are you going to do if someone uses spatial teleportation magic to move the nuclear warheads? To Beijing, for example.” “That’s why we have an Archmage like you…” “Me? Our opponent isn’t an ordinary Lich. If this Arch Lich is more skilled in magic than I am, then it will cause an irreversible catastrophe. Something similar already happened several times during the early days of the Great Cataclysm, remember?” “B-But even so… sacrifices on this scale…” “Hey. Motherfucker.” Bang! I nearly jumped out of my skin. Magic Johnson shot to his feet, his bronze muscles rippling. “Knock it off. I like Asian men too, you know. I might punish you.” “…!” “…!” That was the scariest threat I had ever heard. Senior General Liao’s face turned deathly pale as he looked around for help. But the officials who appeared to belong to his faction avoided his gaze. Even Wu Heixing, the last line of defense, looked away. *So this is how it gets resolved.* The opponent was an American national hero and a national gay icon. Everyone seemed desperate not to become the Asian man Magic Johnson liked. Of course, the ridiculous bullshit Senior General Liao had been spouting also played a major role. “Enough, both of you. And especially Senior General Liao—stop talking such utter nonsense.” Under Wei Penghu’s leadership—a Chinese man who had just subdued the chink—the meeting moved forward quickly. After gathering the opinions that had been raised and exchanging heated arguments, Wei Penghu finally won everyone’s agreement. He spoke with a tired expression. “We will divide the six S-rank Hunters present here among six fronts. According to the official organization, each front will receive three Army and Air Force divisions, along with Hunters from the Public Security Armed Forces.” Three Chinese divisions, along with the Public Security Armed Forces. I had no idea exactly how many that meant, but their sheer numbers would be enormous. When it came to the number of Hunters it possessed, China was always competing for first or second place. *Of course, the other side is no pushover either.* The casualty estimates alone were in the hundreds of thousands. If the Arch Lich had resurrected the dead as undead… Then an unimaginable number of enemies would be waiting for us. “This concludes the meeting. Please move out as soon as possible.” Just as everyone rose from their seats after Wei Penghu said he would provide the exact numbers and unit composition in writing, a voice pierced my ear. - Come see me for a moment. It was not a Message Spell, but unmistakably Sound Transmission. [^1]: The Korean word *so* can mean both “the few” in the general’s maxim and “ox,” turning his solemn justification into an insult.

## Korean source

```text
＃387화



지하 벙커를 빠져나왔을 때는 이미 깊은 밤이었다.

크게 숨을 들이쉬자 차가운 공기가 폐부로 스며든다. 저 어딘가에 있을 무림의 사천을 떠올리며 별이 총총히 박힌 밤하늘을 바라보고 있는데, 자그마한 손이 어깨를 톡 건드렸다.

「따라올래? 가볍게 한잔할 생각인데.」

“지금요?”

「응. 우리끼리.」

파이 첸이다. 그녀의 등 뒤에는 ‘우리’에 속한 두 사람이 서 있었다.

그중 하나가 기품이 넘쳐흐르는 말투로 입을 열었다.

「동양의 귀부인이여, 혹 함께 마실 술 중에 로마네콩티가 있는가?」

「귀부인은 아닌데, 당연히 있지. 술 좋아해, 왕자?」

필릭스 왕자가 못마땅한 얼굴로 대답했다.

「왕자가 아니라 필릭스 전하라고 부르라니까. 그리고 술은 적당히 즐기는 편이다. 특히 로마네콩티 45년 산을.」

「45년 산은 없는데.」

「그럼 거절하지. 난 이만.」

저거 진짜 미친놈인가.

필릭스 왕자가 수행원들을 이끌고 사라지자 파이 첸이 남은 한 사람을 향해 고개를 돌렸다.

「당신은 갈 거지. 존슨?」

매직 존슨이 새하얀 이빨을 드러내며 웃었다.

「미안하군. 아쉽지만 다음으로 미뤄야 할 것 같아.」

「왜?」

「당장 내일 전선에 투입될지도 모르는데, 메모라이즈(Memorize) 정도는 해 둬야 마음이 편할 것 같아서.」

역시 대마법사. 대격변의 영웅은 괜히 되는 게 아니구나.

매직 존슨의 마음가짐에 깊은 감명을 받은 내가 입술을 뗐다.

“저도 지금은 안 될 것 같은데요.”

「안 돼.」

“왜요?”

「넌 왕자도 아니고, 대마법사도 아니잖아.」

“……아니, 그런 게 어딨어요.”

어이가 없네. 말도 안 되는 강짜를 놓는 건 둘째치고 이런 판국에 술을 마시자는 저 아줌마도 정말 어지간하다.

「너, 방금 속으로 내 욕했지? 이런 상황에서 술이나 마시는 생각 없는 아줌마라고.」

“……어떻게 알았어요?”

「어머, 얘 쓸데없이 솔직한 것 좀 봐라?」

파이 첸이 긴 손가락으로 내 코끝을 쿡 찔렀다. 외관만 보면 20대 초반의 미인인데, 실상은 어머니보다 나이 많은 사람이라 그런지 기분이 묘하다.

“다른 사람 찾아보시는 게 어때요? 이정룡 씨라거나…….”

「리(Lee)?」

파이 첸의 고개가 살짝 기울어졌다. 이정룡은 이미 자신이 데려온 아레스 길드원들과 사라진 지 오래였다.

「흠. 뭔가 어려운 사람이라서. 대격변 때만 해도 저 정도는 아니었는데 능구렁이가 다 됐어. 무슨 생각을 하는지 알 수가 없다니까.」

사람 보는 눈이 상당히 정확한데.

파이 첸은 저 멀리 사라지는 또 다른 후보를 힐끗 곁눈질하며 말을 이었다.

「우헤이싱. 쟤는 너무 예의가 없고. 같이 마시면 술맛 떨어져.」

나는 인적 드문 숲속으로 향하는 우헤이싱의 뒷모습을 물끄러미 바라보며 대답했다.

“어쩔 수 없네요. 다음에 드시는 수밖에.”

「아니. 술은 이런 날에 마시는 거란다.」

“……?”

「마지막이 될지도 모르잖니.」

“아.”

파이 첸이 왜 술을 찾는지, 어느 정도 알 것 같았다.

전쟁은 사람을 지치게 만든다. 동시에 죽음이라는 방식으로 예측하지 못한 이별이 찾아오기도 한다.

대격변을 통해 수많은 동료를 잃었던 그녀만의 전야제(前夜祭)인 셈이다.

당장 이번 사태가 마무리되었을 때, 우리 중 누군가는 영영 돌아올 수 없는 강을 건넜을 수도 있으니까.

「뭐, 어쨌건 이렇게 된 이상 표적을 바꾸는 수밖에 없네. 안 그래, 거기 잘생긴 총각?」

“저 안 간다니까요.”

파이 첸이 어처구니없는 표정으로 나를 바라봤다.

「양심이 없니? 너 말고 저 청년 말이야.」

파이 첸에게 지목당한 잘생긴 총각, 최 팀장은 내 예상과 다르게 흔쾌히 고개를 끄덕였다.

“불러 주신다면 저야 영광입니다.”

“어, 팀장님. 진짜 가시게요?”

“가야죠. 파이 첸과 함께 술자리를 가질 기회가 언제 또 오겠습니까. 궁금한 것도 많고요.”

파이 첸이 까르르 웃었다.

「잘생긴 줄만 알았는데 말도 예쁘게 하네. 그래, 뭐가 그렇게 궁금하니?」

“혹시 지금 착용하고 계신 장비. 어디서 구매하신 겁니까?”

「……그게 질문이야?」

“예.”

「얘도 만만치 않네.」

한숨을 푹 내쉬는 파이 첸을 보며 매직 존슨이 호탕한 웃음을 터트렸다.

「하하. 미스 첸, 그럼 이제 다 같이 한잔하러 갈까?」

「다 같이? 존슨 당신 안 간다고 하지 않았어?」

「그랬지. 여자랑 단둘이 술 마시는 취미는 없거든. 하지만 여기 있는 미스터 최처럼 매력적인 남자가 동석한다면 이야기는 달라지지.」

「…….」

「난 남자가 좋아. 특히 동양인 남자.」

「그, 그래. 가자.」

역시 타임지가 선정한 세상에서 가장 영향력 있는 성소수자 1위답다.

나는 바짝 굳은 채 끌려가는 최 팀장에게 전음을 날렸다.

- 무슨 일 생기면 연락해요.

도살장에 끌려가는 소처럼 슬픈 눈으로 나를 바라본 최 팀장이 두 S급 헌터와 함께 사라지고, 주위를 둘러본 나는 발걸음을 옮겼다.

‘이 방향이었지.’

사람들의 눈을 피해 어두컴컴한 오솔길을 얼마나 걸었을까. 컴컴한 어둠 속에 멈추어 서서 입을 열었다.

“나와.”

잠깐의 침묵 후, 누군가의 목소리가 흘러나왔다.

「……제법이군.」

부스럭.

인기척과 함께 나타난 한 사람, 우헤이싱이 나를 위아래로 훑었다.

「어떻게 알았지?」

저걸 말이라고. 나는 심드렁하게 대꾸했다.

“차라리 일 더 하기 일이 뭐냐고 물어봐라. 그게 더 어렵겠다.”

「음. 생각보다 실력 있는 놈이었군.」

“이제 와서 칭찬하는 척하지마. 개수작 부리려는 거 뻔히 보이니까.”

「……!」

정곡을 찔린 우헤이싱의 얼굴이 붉게 달아올랐다.

어떤 의미에서는 참 다루기 쉬운 놈이다. 서른 중반이 넘은 나이로 알고 있는데 저렇게 단순하기도 힘들다.

「그, 그게 아니라 나는 진심으로…….」

“진심으로 빵즈라고 생각하겠지. 아직 정식 S급 헌터도 아닌 웬 한국놈이 너 대신 주목받으니까 짜증 났을 거고. 특유의 일차원적인 행동으로 시비부터 걸고 봤는데, 이게 영 반응도 안 좋고 저 빵즈 놈도 생각 외로 만만치가 않네?”

나는 대꾸할 틈도 주지 않고 속사포처럼 말을 이었다.

“그래서 괜히 마음에도 없는 칭찬 몇 번 날려 주고, 우호적인 제스처 취하면서 뭔가 수작을 부리려는 것 같은데…… 아, 혹시 지금까지 내가 말한 것 중에 틀린 부분 있냐?”

「…….」

“그래, 너 같은 놈 많이 봤다. 뒤통수를 하도 처맞았더니 안 돌아가던 머리가 휙휙 돌아가더라.”

한심한 눈빛으로 바라보자, 얼굴이 벌겋게 달아올라 있던 우헤이싱이 더듬더듬 입을 열었다.

「다른 수작을 부리려던 건 아니었다.」

“아니면? 혹시 나랑 친해질 생각이면 곱게 접어서 넣어 둬라. 똥 옆에 있으면 나한테까지 냄새 배니까.”

「……!」

“그런데 너 지금 뭐 하냐?”

내 나직한 한마디에, 검파를 향해 움직이던 놈의 손이 우뚝 멈췄다.

“뽑지 마라. 다친다.”

갈등 어린 눈빛으로 날 바라보던 우헤이싱이 불쑥 입을 열었다.

「어차피 다 알고 있었으면서…… 왜 순순히 따라온 거지?」

“물어볼 게 있어서.”

「뭐?」

난 우헤이싱의 눈동자를 똑바로 직시하며 입을 열었다.

“전음(傳音). 맞지?”

「……!」

딱딱하게 굳은 얼굴이 곧 대답이다. 설마 했는데, 나는 뒷머리를 긁적이며 중얼거렸다.

“맞나 보네. 하긴, 본토니까 여러 가지 무공이 남아 있을 수도 있겠지. 내공심법이라던가.”

「무, 무슨 소리! 그건 메시지 마법…….」

“얼씨구.”

황급히 변명을 늘어놓는 녀석의 모습에 실소가 흘러나왔다.

무공을 접하지 못한 다른 사람들은 차이점을 구분할 수 없겠지만, 나까지 속일 수는 없다.



‘잠깐 나 좀 보지.’



회의가 끝날 무렵 귓가에 닿은 것은 분명 전음이었다.

무시할 수도 있었던 제의에 응했던 이유는, 전음을 보낸 장본인이 바로 우헤이싱이었기 때문이다.

「네, 네놈이 그걸 어떻게.」

“왜, 아무도 모르는 비밀이었어?”

나는 당황하는 우헤이싱을 물끄러미 바라보며 입을 열었다.

“어느 정도 가능성은 있다고 생각하긴 했는데, 확실히 신기하긴 하네. 너희 문화 대혁명이다, 뭐다 해서 무술인들 싹 다 조져 놓지 않았었냐? 그 와중에도 용케 무공이 남아 있었네.”

「주둥이 닥쳐!」

“아, 너 집안 빵빵하다고 했었지. 그럼 공산당 최고위층이 직위를 이용해서 슬쩍 빼돌린 건가?”

「…….」

순식간에 착 가라앉은 표정을 보니 맞는 것 같다.

엄연한 외국인인 나로서는 이게 얼마나 큰 문제인지는 잘 모르겠지만, 내공심법. 즉 현대에 이르러 마나 연공법이라 불리는 이것의 가치가 어느 정도인지 알고 있다.

‘이곳이 무림이었다면, 한바탕 피바람이 일었겠지.’

그렇게 몰래 빼돌린 금송아지를 들켰으니, 놈의 반응이 좋지 않은 것은 당연했다.

「방금 했던 말, 두 번 다시 발설하지 않는 것이 좋을 거다.」

“딱히 할 생각은 없었는데, 말투가 상당히 띠껍네.”

우헤이싱이 표독스러운 눈빛으로 나를 노려보았다.

「내 아버지가 누군지 안 후에도 네놈이 이런 식으로 나올 수 있을까?」

“네 아버지가 누군진 모르겠고, 홍위병 출신이었을 것 같긴 한데.”

「……!」

“소싯적에 오함마 들고 공자 묘 때려 부순 게 너희 아버지 아니냐?”

「이 빵즈 새끼가-!」

파팟!

분기탱천한 고함과 함께 놈의 신형이 쏘아졌다.

어느새 검집에서 뽑혀 나온 직검(直劍)에서 솟구친 오러 블레이드, 아니 검강이 내 목을 노리고 날아든다.

쉬이이이잉!

시원한 바람에 머리카락이 흩날렸다. 바닥에 닿을 만큼 허리를 젖혀 검강을 피해 낸 나는, 몸을 튕기듯 일어나며 무릎으로 놈의 턱을 쳐올렸다.

콰직!

허공으로 솟구치는 치아와 핏물. 순간 비틀거리는 놈의 두 팔을 움켜잡고 귓가에 속삭였다.

“그 검. 뽑지 말랬지.”

치이이익, 우두둑!

「크아아아악!」

양손에 실린 강대한 열양지기가 갑옷을 부수고 살을 태운다.

우헤이싱의 입술 사이로 뛰쳐나온 비명은 내가 펼쳐 놓은 기막(氣幕)에 가로막혀 나아가지 못했다.

「노옴!」

후우우웅!

이놈, 권각술(拳脚術)까지 익혔다. 허접한 검법과는 달리 이건 제법 예리하다.

물론…….

‘무림이랑 비교하면 무공의 질이 훨씬 떨어져.’

나는 약간의 실망을 느끼며 손을 뻗었다.

꽈앙!

공력과 공력의 격돌.

내 허리를 향해 채찍처럼 휘둘러진 놈의 다리는 더 이상 나아가지 못했다.

우헤이싱의 눈동자가 충격과 경악으로 파르르 떨렸다.

「어, 어떻게?」

“잘.”

발목을 덥석 붙잡은 나는 땅을 향해 있는 힘껏 놈을 패대기쳤다.

후우웅, 콰앙!

한 번 더.

후우우웅, 쾅!

더, 더, 더.

쾅! 쾅! 콰과광!

땅이 뒤집히고 바위와 나무가 뽑혀 나간다.

잠시 후 생체 곡괭이질이 멈췄을 때는, 혼이 빠져나간 듯한 우헤이싱이 커다란 크레이터 안에 대자로 뻗어 있었다.

“그래도 몸은 튼튼해서 별로 안 다쳤네.”

「흐, 흐어…….」

“야, 우냐?”

「흐어어어…….」

아주 정신이 나갔군.

혀를 차며 허리를 굽힌 나는 놈의 주머니를 뒤졌다.

공간 확장 마법이 걸린 주머니를 얼마나 헤집었을까, 마침내 원하던 물건을 찾을 수 있었다.

“아, 여기 있네. 상급 포션.”

띠링.



- [최상급 포션]을 습득하셨습니다!



“……이 아니라. 최상급 포션? 뭐야, 이 새끼.”

나는 놀란 눈으로 뻗어 있는 우헤이싱을 바라봤다. 아무리 S급 헌터라지만 이런 물건을 들고 다니다니.

상급 포션도 희귀하지만, 최상급 포션은 일 년에 한두 개 나올까 말까 하는 물건이다.

현실감조차 들지 않는 가격은 둘째치고, 희소성이 너무 높은 탓에 돈이 있어도 못 구한다.

‘인터넷에서나 보던 걸 여기서 보네.’

잠시 고민하던 나는 최상급 포션을 슬쩍 인벤토리에 집어넣었다. 그리고 놈의 주머니를 뒤져 상급 포션 하나를 찾아내 부어 주었다.

“합의금 챙겼으니까 이쯤에서 봐준다. 너도 켕기는 거 많으니까 오늘 일 어디 가서 떠들면…… 알지?”

「흐으, 흐으으으…….」

“오케이. 우리 합의 본 거야.”

깔끔하게 사태를 마무리한 그때, 주머니에 넣어 둔 휴대폰이 부르르 몸을 떨었다.

최 팀장으로부터 짤막한 문자 한 통이 와 있었다.



〈 최 팀장님



최 팀장님

지ㄴ태경시제발빠ㄹ리 와주세요



“…….”

안 돼, 존슨.
```

## Current accepted English baseline

```markdown
# Chapter 387

By the time we left the underground bunker, it was already deep into the night.

I drew in a deep breath, and the cold air seeped into my lungs. As I gazed up at the star-filled night sky, thinking of the Sichuan of the Murim somewhere out there, a small hand tapped me on the shoulder.

“Want to come along? I was thinking of having a light drink.”

“Now?”

“Yeah. Just us.”

It was Pai Chen. Two people who belonged to her “us” stood behind her.

One of them spoke in a voice overflowing with dignity.

“O noblewoman of the East, might there be a bottle of Romanée-Conti among the wine we shall drink together?”

“I’m not a noblewoman, but of course there is. Do you like wine, Prince?”

Prince Felix answered with an displeased expression.

“I told you to call me His Highness Felix, not Prince. And I enjoy wine in moderation. Especially forty-five-year-old Romanée-Conti.”

“We don’t have any forty-five-year-old.”

“Then I must decline. I’ll be going.”

*Is he actually insane?*

As Prince Felix disappeared with his attendants, Pai Chen turned toward the one person left.

“You’re coming, right, Johnson?”

Magic Johnson smiled, baring his perfectly white teeth.

“I’m sorry. Unfortunately, I think I’ll have to take a rain check.”

“Why?”

“I might be deployed to the front tomorrow. I should at least use *Memorize* so I can put my mind at ease.”

As expected of an Archmage. You didn’t become a hero of the Great Cataclysm for nothing.

Deeply impressed by Magic Johnson’s attitude, I opened my mouth.

“I don’t think I can go right now either.”

“No.”

“Why not?”

“You’re neither a prince nor an Archmage.”

“…”

“What kind of logic is that?”

Unbelievable. Setting aside the ridiculous stubbornness she was displaying, that middle-aged woman was really something for suggesting drinks in a situation like this.

“You just insulted me in your head, didn’t you? You called me a clueless middle-aged woman for thinking about drinking in a situation like this.”

“...How did you know?”

“Oh my, look how pointlessly honest you are.”

Pai Chen poked the tip of my nose with one long finger. She looked like a beautiful woman in her early twenties, but in reality, she was older than my mother. It gave me a strange feeling.

“How about finding someone else? Mr. Lee, maybe…”

“Lee?”

Pai Chen tilted her head slightly. Lee Jungryong had disappeared a long time ago with the Ares Guild members he had brought along.

“Hmm. He’s a difficult man. He wasn’t like that during the Great Cataclysm, but he’s become a slippery old fox. You can’t tell what he’s thinking.”

*She’s a pretty accurate judge of character.*

Pai Chen continued, casting a sidelong glance at another candidate disappearing in the distance.

“Wu Heixing. He’s too rude. Drinking with him would ruin the taste.”

I stared at Wu Heixing’s back as he headed toward a deserted forest and answered.

“Nothing we can do. You’ll have to drink next time.”

“No. This is exactly when you’re supposed to drink.”

“...?”

“It might be the last chance we get.”

“Ah.”

I thought I understood, at least to some extent, why Pai Chen wanted a drink.

War exhausted people. At the same time, it brought unexpected farewells in the form of death.

It was her own sort of prewar celebration after losing countless companions during the Great Cataclysm.

Once this crisis was over, one of us might have crossed the river from which no one returned.

“Well, now that things have turned out this way, I have no choice but to change targets. Don’t you agree, handsome bachelor over there?”

“I told you I’m not going.”

Pai Chen stared at me in disbelief.

“Do you have no conscience? I’m talking about that young man, not you.”

The handsome bachelor Pai Chen had singled out, Team Leader Choi, nodded readily—contrary to my expectations.

“If you’ll have me, I’d be honored.”

“Wait, Team Leader. You’re really going?”

“I should. When will I get another chance to have a drink with Pai Chen? And I have a lot of questions.”

Pai Chen burst into laughter.

“I thought you were only handsome, but you say such pretty things, too. All right, then. What are you so curious about?”

“For the Equipment you’re wearing right now. Where did you buy it?”

“...That’s your question?”

“Yes.”

“This one’s quite a handful too.”

As Pai Chen let out a deep sigh, Magic Johnson broke into a hearty laugh.

“Haha. Miss Chen, shall we all go have a drink now?”

“All of us? Johnson, didn’t you say you weren’t coming?”

“I did. I don’t make a habit of drinking alone with women. But if a charming man like Mr. Choi joins us, that changes things.”

“…”

“I like men. Especially East Asian men.”

“Y-yes. Let’s go.”

No wonder Time had named him the world’s most influential LGBTQ person.

I sent Sound Transmission to Team Leader Choi as he was dragged away, stiff as a board.

—If anything happens, contact me.

Team Leader Choi looked at me with the sad eyes of an ox being led to slaughter, then disappeared with the two S-rank Hunters. I looked around before setting off.

*This was the direction.*

How long had I walked along the dark path to avoid people’s eyes? I stopped in the pitch-black darkness and spoke.

“Come out.”

After a brief silence, someone’s voice drifted out.

“...Not bad.”

Rustle.

A figure emerged with the sound of someone approaching. Wu Heixing looked me up and down.

“How did you know?”

*What kind of question was that?*

I answered listlessly.

“You might as well ask me what one plus one is. That’d be harder.”

“Hmm. You’re more capable than I expected.”

“Don’t pretend to compliment me now. It’s obvious you’re trying to pull some kind of cheap trick.”

“...!”

I had hit the mark. Wu Heixing’s face flushed red.

In a way, he was incredibly easy to handle. I believed he was already in his mid-thirties, yet it was hard to imagine anyone being this simple.

“N-no, that’s not it. I sincerely—”

“You probably do sincerely think I’m a *bangzi*.[^1] You were annoyed because some Korean guy who isn’t even an official S-rank Hunter yet was getting attention instead of you. You picked a fight with your usual one-dimensional behavior, but it didn’t go over well, and that *bangzi* bastard turned out to be tougher than you expected, huh?”

I continued speaking like a machine gun without giving him a chance to respond.

“So you threw out a few compliments you didn’t mean and started acting friendly while looking for an angle… Am I wrong about anything I’ve said so far?”

“…”

“Yeah, I’ve seen plenty of people like you. After getting hit in the back of the head so many times, even my brain—which had stopped working—started spinning again.”

I looked at him with pity. His face already bright red, Wu Heixing stammered.

“I wasn’t trying to pull any other kind of trick.”

“Then what? If you’re thinking of becoming friends with me, fold that thought up neatly and tuck it away. If I stand next to shit, the stink rubs off on me too.”

“...!”

“By the way, what are you doing right now?”

At my quiet question, the hand moving toward his sword hilt stopped dead.

“Don’t draw it. You’ll get hurt.”

Wu Heixing looked at me with hesitation in his eyes before blurting out,

“You knew all along… so why did you follow me so readily?”

“Because I had something to ask.”

“What?”

I looked directly into Wu Heixing’s eyes and spoke.

“Sound Transmission. Right?”

“...!”

His face stiffened. That was answer enough. I had suspected as much, but I scratched the back of my head and muttered,

“So it was. Well, this is the mainland, after all. There could still be all kinds of martial arts here. An internal-energy cultivation technique, for example.”

“W-what are you talking about? That was Message Spell…”

“Oh, please.”

A quiet laugh escaped me at his frantic excuses.

People who had never encountered martial arts might not be able to tell the difference, but he couldn’t fool me.

*Come see me for a moment.*

The thing that had reached my ear near the end of the meeting had unmistakably been Sound Transmission.

The reason I had accepted an offer I could have ignored was because Wu Heixing himself had been the one to send it.

“H-how did you know that?”

“What, was it a secret no one else knew?”

I stared at the flustered Wu Heixing and continued.

“I did think it was somewhat possible, but it’s still fascinating. Didn’t you wipe out all the martial artists during your Cultural Revolution and whatnot? Martial arts somehow survived even through that.”

“Shut your mouth!”

“Ah, you said your family was powerful. Did the highest levels of the Communist Party use their positions to quietly spirit it away?”

“…”

His expression instantly sank.

*Looks like I was right.*

As a foreigner, I didn’t know exactly how serious a problem this was. But I knew how valuable an internal-energy cultivation technique was—the thing now called a mana cultivation method in the modern era.

*If this were the Murim, a bloody storm would have erupted.*

Now that he’d been caught with the golden calf that had been secretly spirited away, it was only natural that he’d react badly.

“It would be best if you never uttered what you just said again.”

“I wasn’t planning to, but your tone is pretty damn irritating.”

Wu Heixing glared at me viciously.

“Even after you find out who my father is, do you think you can keep acting like this?”

“I don’t know who your father is, but I have a feeling he used to be a Red Guard.”

“...!”

“Wasn’t your father the one who smashed Confucius’s tomb with a sledgehammer in his youth?”

“You fucking bangzi bastard—!”

Fwish!

With an enraged roar, his body shot forward.

A straight sword had already been drawn from its scabbard. The Aura Blade rising from it—no, the Sword Force—flew toward my neck.

Shiiiiing!

The rush of wind scattered my hair. I bent backward until my back nearly touched the ground, avoiding the Sword Force, then sprang upright and drove my knee into his chin.

Crack!

Teeth and blood shot into the air. As he staggered, I seized both his arms and whispered into his ear.

“I told you not to draw that sword.”

Hiss, crack!

“Gaaaaaaaaah!”

The powerful Scorching Yang Qi surging through both my hands shattered his armor and seared his flesh.

His scream could not travel beyond the Qi Curtain I had spread.

“You bastard!”

Whooom!

That bastard had learned fist-and-foot techniques too. Unlike his shoddy sword technique, this one had some bite.

Of course…

*Compared with the Murim, the quality of his martial arts was far lower.*

Slightly disappointed, I reached out.

Boom!

Internal energy collided with internal energy.

The leg he had whipped toward my waist like a lash could go no farther.

Wu Heixing’s eyes trembled with shock and disbelief.

“H-how?”

“Well.”

I grabbed his ankle and slammed him into the ground with all my strength.

Whoom! Boom!

Once more.

Whoooom! Crash!

More. More, more, more.

Crash! Crash! KRA-KOOM!

The ground turned over, and rocks and trees were ripped from the earth.

A little while later, when I finally stopped using him as a living pickaxe, Wu Heixing lay spread-eagled in a huge crater, looking as if his soul had left his body.

“Still, you’ve got a sturdy body. You’re not hurt that badly.”

“Hh… hhaa…”

“Hey, are you crying?”

“Hhaa…”

He was completely out of it.

Clicking my tongue, I bent over and searched through his pockets.

After rummaging through the pouch with spatial expansion magic for a while, I finally found what I wanted.

“Ah, here it is. An Advanced Potion.”

Ding.

> **System**
> **Acquired:** Supreme Potion!

“...No, wait. Supreme Potion? What the hell, you bastard?”

I stared at the sprawled-out Wu Heixing in shock. Even if he was an S-rank Hunter, who carried something like this around?

Advanced Potions were rare, but Supreme Potions were items of which only one or two appeared in an entire year, if that.

Putting aside the price, which didn’t even feel real, they were so scarce that they couldn’t be obtained even with money.

*I’d only ever seen one online. And now here it is.*

After a moment of thought, I quietly slipped the Supreme Potion into my inventory. Then I searched through his pouch again, found an Advanced Potion, and poured it over him.

“I’ve taken my settlement payment, so I’ll let you off here. You’ve got plenty to hide, so if you go blabbing about what happened today… you know what happens, right?”

“Hh… hhh…”

“Okay. We’ve reached a settlement.”

Just as I had neatly wrapped things up, the phone in my pocket began to vibrate.

I had received one short text message from Team Leader Choi.

> 〈 Team Leader Choi
>
> Team Leader Choi
>
> Ji[n] Taekyung, please come qui[c]kly.

“…”

*No, Johnson.*

[^1]: *Bangzi* is a derogatory Chinese slur for Koreans.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 387`.

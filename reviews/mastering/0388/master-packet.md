# Master Edit Task — Chapter 388

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
| 이정룡    | **Lee Jungryong** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 레이페이 | **Lei Fei** | Previously undisclosed Chinese S-rank Hunter and commander of the Sichuan Public Security Armed Forces; missing with his Hunters. |
| 웨이펑후 | **Wei Penghu** | Senior General and Minister of Defense at the Central Military Commission. |
| 우헤이싱 | **Wu Heixing** | S-rank Hunter antagonistic toward Taekyung. |
| 열화신공 | **Blazing Flame Divine Art** | Art whose formula Taekyung uses to infuse the armor. |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 중화 | **Zhonghua** | Term used in Shao Shen's rallying cry for China. |
| 국방부장 | **Minister of Defense** | Wei Penghu's office at the Central Military Commission. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 웨이펑후 | 진태경 | senior_military_official_to_foreign_hero | Teacher Jin | respectful-formal | Wei Penghu uses 진 선생 when introducing himself and inviting Taekyung to the operations headquarters. |
| 우헤이싱 | 진태경 | hostile_peer | peninsula bangzi | abusive-hostile | Wu Heixing repeatedly addresses Taekyung with an anti-Korean slur. |
| 진태경 | 우헤이싱 | hostile_peer | mainland chink | abusive-hostile | Taekyung answers Wu Heixing's slur with an explicit anti-mainland insult. |
| 우헤이싱 | 이정룡 | junior_s_rank_hunter_to_top_s_rank_hunter | Mr. Lee | intimidated-deferential | Uses 이 선생님 and suppresses his usual hostility in Lee's presence. |
| 웨이펑후 | 이정룡 | senior_military_official_to_top_s_rank_hunter | Mr. Lee | respectful-formal | Addresses Lee as 이 선생 during the meeting. |
| 진태경 | 아저씨 | passenger_to_pilot | Sir | casual-urgent | Taekyung addresses the pilot informally while demanding full throttle. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |
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

#### Chapter 386 tail (verified mastered)

…
Stroking his beard, he began to speak. “Listening to the Minister of Defense, I find myself so frustrated that I have to speak. At this rate, how long will it take us to deal with those monsters?” *Wow…* His tone was unbelievably obnoxious. He was talking that way to Wei Penghu—the Chairman’s right-hand man and the military’s highest-ranking power broker. As if he had read my question, Team Leader Choi sent me a Message Spell. - The Communist Party has factions too. Senior General Liao is a pure-blooded member of the Princelings, the Communist Party’s largest faction, going back to his grandfather’s generation. They’re rivals of the Shanghai clique, which Chairman Xiao and Minister of Defense Wei Penghu belong to. - The Princelings and Shang… what? - …If we’re being precise, it means the Princelings are number one and the Shanghai clique is number two. - Ah. Until now, I had assumed that the Communist Party operated under a strict one-party system. Apparently, they fought each other tooth and nail too. - But is that allowed? If Chairman Xiao simply points at someone and says, “That man is dangerous,” wouldn’t that person be beheaded in Tiananmen Square? - They do it because they’re allowed to. - …Right. When you put it that way, I’ve got nothing to say. - The factions reached an agreement. During the Great Cataclysm, the Chairman from the Princelings made so many mistakes that they felt awkward about continuing to hold power. - Ah. Pingping? - Yes. Pingping. That damn Great Cataclysm really had changed all kinds of things. While I was listening to Team Leader Choi’s explanation, Senior General Liao—who apparently came from the Princelings’ pure-blooded younger generation—made an absolutely brilliant proposal. “Let’s use nuclear weapons.” “…” “…” “Let’s formally request it from Chairman Xiao and fire dozens of nuclear weapons across all of Sichuan. Wouldn’t that solve everything cleanly?” “…” “…” What a lunatic nuclear-happy bastard. Everyone, myself included, stared at each other in disbelief. Wei Penghu’s expression was especially spectacular. He answered with the face of a man who desperately wanted a pistol. “Rejected.” “Why? Are you dismissing me because I’m not part of the Shanghai clique?” “Say something that makes sense. Something that makes sense! If we do that, what happens to the people who are still alive or haven’t been harmed? What about the land we leave barren?” “Sacrificing the few for the sake of the many is unavoidable!” Forget the rest—he just sounded like an ox head to me.[^1] Magic Johnson, who had been listening quietly, suddenly spoke in his deep voice. “The damage from a successful nuclear attack is bad enough, but what are you going to do if someone uses spatial teleportation magic to move the nuclear warheads? To Beijing, for example.” “That’s why we have an Archmage like you…” “Me? Our opponent isn’t an ordinary Lich. If this Arch Lich is more skilled in magic than I am, then it will cause an irreversible catastrophe. Something similar already happened several times during the early days of the Great Cataclysm, remember?” “B-But even so… sacrifices on this scale…” “Hey. Motherfucker.” Bang! I nearly jumped out of my skin. Magic Johnson shot to his feet, his bronze muscles rippling. “Knock it off. I like Asian men too, you know. I might punish you.” “…!” “…!” That was the scariest threat I had ever heard. Senior General Liao’s face turned deathly pale as he looked around for help. But the officials who appeared to belong to his faction avoided his gaze. Even Wu Heixing, the last line of defense, looked away. *So this is how it gets resolved.* The opponent was an American national hero and a national gay icon. Everyone seemed desperate not to become the Asian man Magic Johnson liked. Of course, the ridiculous bullshit Senior General Liao had been spouting also played a major role. “Enough, both of you. And especially Senior General Liao—stop talking such utter nonsense.” Under Wei Penghu’s leadership—a Chinese man who had just subdued the chink—the meeting moved forward quickly. After gathering the opinions that had been raised and exchanging heated arguments, Wei Penghu finally won everyone’s agreement. He spoke with a tired expression. “We will divide the six S-rank Hunters present here among six fronts. According to the official organization, each front will receive three Army and Air Force divisions, along with Hunters from the Public Security Armed Forces.” Three Chinese divisions, along with the Public Security Armed Forces. I had no idea exactly how many that meant, but their sheer numbers would be enormous. When it came to the number of Hunters it possessed, China was always competing for first or second place. *Of course, the other side is no pushover either.* The casualty estimates alone were in the hundreds of thousands. If the Arch Lich had resurrected the dead as undead… Then an unimaginable number of enemies would be waiting for us. “This concludes the meeting. Please move out as soon as possible.” Just as everyone rose from their seats after Wei Penghu said he would provide the exact numbers and unit composition in writing, a voice pierced my ear. - Come see me for a moment. It was not a Message Spell, but unmistakably Sound Transmission. [^1]: The Korean word *so* can mean both “the few” in the general’s maxim and “ox,” turning his solemn justification into an insult.

#### Chapter 387 tail (verified mastered)

…
Well, this is the mainland, after all. There could still be all kinds of martial arts here. An internal-energy cultivation technique, for example.” “W-what are you talking about? That was a Message Spell…” “Oh, please.” A dry laugh escaped me at the sight of his frantic excuses. People who had never encountered martial arts might not be able to tell the difference, but he couldn’t fool me. *Come see me for a moment.* What had reached my ear near the end of the meeting had unmistakably been Sound Transmission. The reason I had accepted an offer I could have ignored was that Wu Heixing himself had sent it. “H-how did you know that?” “What, was it a secret no one else knew?” I stared at the flustered Wu Heixing and continued. “I did think it was somewhat possible, but it’s still fascinating. Didn’t you wipe out all the martial artists during your Cultural Revolution and whatnot? Martial arts somehow survived even through that.” “Shut your mouth!” “Ah, you said your family was powerful. Did the highest levels of the Communist Party use their positions to quietly spirit it away?” “…” His expression instantly sank. *Looks like I was right.* As a foreigner, I didn’t know exactly how serious a problem this was. But I knew how valuable an internal-energy cultivation technique was—the thing now called a mana cultivation method in the modern era. *If this were the Murim, a bloody storm would have erupted.* Now that he’d been caught with the golden calf that had been secretly spirited away, no wonder he wasn’t taking it well. “It would be best if you never uttered what you just said again.” “I wasn’t planning to, but that tone of yours is pretty damn irritating.” Wu Heixing glared at me viciously. “Do you think you’ll still be able to act this way once you learn who my father is?” “I don’t know who your father is, but I have a feeling he used to be a Red Guard.” “…!” “Wasn’t your father the one who smashed Confucius’s tomb with a sledgehammer in his youth?” “You fucking *bangzi* bastard—!” Fwish! With a furious roar, he shot forward. A straight sword had already been drawn from its scabbard. The Aura Blade rising from it—no, the Sword Force—flew toward my neck. Shiiiiing! The cool wind scattered my hair. I bent backward until my back nearly touched the ground, letting the Sword Force pass overhead, then sprang upright and drove my knee into his chin. Crack! Teeth and blood shot into the air. As he staggered, I seized both his arms and whispered into his ear. “I told you not to draw that sword.” Hiss! Crack! “Gaaaaaaaaah!” The powerful Scorching Yang Qi surging through both my hands shattered his armor and seared his flesh. The scream that tore from Wu Heixing’s lips struck the Qi Curtain I had spread and went no farther. “You bastard!” Whooom! That bastard had learned fist-and-foot techniques too. Unlike his shoddy sword technique, this one was reasonably sharp. Of course… *Compared with the Murim, the quality of his martial arts was far lower.* Slightly disappointed, I reached out. Boom! Internal energy collided with internal energy. The leg he had whipped toward my waist like a lash stopped dead. Wu Heixing’s eyes trembled with shock and disbelief. “H-how?” “Well.” I grabbed his ankle and slammed him into the ground with all my strength. Whoom! Boom! Once more. Whoooom! Crash! More, more, more. Crash! Crash! KRA-KOOM! The ground turned over, and rocks and trees were ripped from the earth. A little while later, when I finally stopped using him as a living pickaxe, Wu Heixing lay spread-eagled in a huge crater, looking as if his soul had left his body. “Still, you’ve got a sturdy body. You’re not hurt that badly.” “Hh… hhaa…” “Hey, are you crying?” “Hhaaa…” He was completely out of it. Clicking my tongue, I bent over and searched through his pockets. After rummaging through the pouch enchanted with spatial expansion magic for some time, I finally found what I wanted. “Ah, here it is. An Advanced Potion.” Ding. > **System** > > **Acquired:** Supreme Potion! “…No, wait. Supreme Potion? What the hell, you bastard?” I stared in shock at the sprawled-out Wu Heixing. Even for an S-rank Hunter, who carried something like this around? Advanced Potions were rare enough, but only one or two Supreme Potions appeared in an entire year, if that. Never mind the price, which was so high it hardly felt real. They were so scarce that even having the money wasn’t enough to get one. *I’d only ever seen one online. And now here it is.* After a moment’s thought, I quietly slipped the Supreme Potion into my inventory. Then I searched his pouch again, found an Advanced Potion, and poured it over him. “I’ve taken my settlement payment, so I’ll let you off here. You’ve got plenty to hide yourself, so if you go around blabbing about what happened today… you know what’ll happen, right?” “Hh… hhh…” “Okay. We’ve reached a settlement.” Just as I neatly wrapped things up, the phone in my pocket shuddered. A short text message had arrived from Team Leader Choi. > 〈 Team Leader Choi > > Team Leader Choi > > Ji nTaekyung please come quic kly “…” *No, Johnson.* [^1]: *Bangzi* is a derogatory Chinese slur for Koreans.

## Korean source

```text
＃388화



“야, 야.”

툭, 툭툭.

옆구리를 건드리는 누군가의 발끝. 간신히 눈을 뜬 우헤이싱의 시야에, 자신을 내려다보는 커다란 형체가 어른거렸다.

「흐으…….」

“나 급한 일이 생겨서 이만 가 봐야 하거든? 혹시 누구 오거나 그러면 알아서 잘 둘러대라.”

「흐으, 흐으으…….」

“포션 부어 줬으니까 엄살 그만 피우고, 인마. 계속 그러면 매직 존슨 불러서 진짜 신음 흘리게 하는 수가 있어. 그럼 간다!”

파팟!

듣는 것만으로도 엉덩이가 욱신거리는 한마디를 남긴 채, 순식간에 멀어져 가는 한 사람의 인기척.

대 자로 뻗어 있던 우헤이싱이 끓어오르는 음성을 내뱉은 것은 그로부터 십여 분이 흐른 뒤였다.

「진태경……!」

부러진 뼈와 살은 상급 포션의 효능으로 회복되었지만, 뼛속 깊이 각인된 고통과 금이 간 자존심까지 치유할 수는 없었다.

‘도대체 어떻게?’

믿을 수 없었다. 제아무리 흥분한 상태였다고는 해도 S급 헌터인 자신이 이렇게까지 철저하게 농락당하다니.

진태경에게 무공을 간파당했다는 것도 충격이지만, 스스로가 지니고 있는 힘에 대단한 자부심을 가진 그로서는 패배에 대한 충격이 더 컸다.

‘내가, 다른 사람도 아닌 이 내가?’

우헤이싱은 태어남과 동시에 헌터의 운명을 타고났다.

그는 유아기 시절 막대한 금액을 들인 마나 적응도 검사를 통해 잠재력을 인정받았고, 중국 공산당 최고위층인 집안은 온갖 지원을 아끼지 않았다.

부패로 축적한 막대한 재산과 권력. 최고의 환경과 지원 아래 성장한 우헤이싱은 스무 살이 되던 해에 A급 헌터로 각성했고, 십 년이 흐른 뒤에는 S급 헌터가 되는 기염을 토했다.

그런데…….

‘그런데 어째서. 내가 저런 소국의 빵즈 놈에게!’

캄캄한 밤하늘을 노려보는 우헤이싱의 눈동자에 기광이 번뜩였다.

그의 눈빛에 서린 것은 분노인 동시에 질투였으며 진태경이 보여 준 힘에 대한 일말의 두려움이었다.

그리고 이러한 감정들은 우헤이싱이 지난 십수 년 동안 지긋지긋하게 느껴 온 것이기도 했다.

이제는 찾을 수 없는 한 사람을 향해, 우헤이싱이 외쳤다.

「네놈의 짓이냐? 죽어서도 날 괴롭히려는 거냐!」

대중과 미디어는 그를 구제 불능 탕아라 욕하는 동시에 중화가 낳은 천재라며 칭송했지만, 우헤이싱을 포함한 극소수의 사람들은 알고 있었다.

진정한 천재는 따로 있음을. 그렇기에 드러내지 않고 감춰 놓았다는 것을.

「대답해라, 레이페이!」

막강한 실력은 물론이고 고결한 심성을 지닌 레이페이는 우헤이싱에게 있어 넘을 수 없는 벽이었다.

처음 그가 실종되었다는 소식을 듣고 얼마나 당황하고 기뻐했던가.

하지만 불과 일주일 만에 또 다른 벽이 나타났다. 진태경이라는 이름으로.

「으아아아아!」

쩌렁쩌렁한 외침에 수풀이 몸을 부르르 떨던 그때였다.

“그 마음, 나도 잘 알지.”

기척도 없이 다가온 누군가의 나직한 목소리에, 우헤이싱은 번개처럼 몸을 일으켜 세웠다.

「누구냐!」

“섭섭하군. 구면이라고 생각했는데.”

저벅.

어둠 속에서 불쑥 걸음을 내디딘 한 사람. 우헤이싱의 눈동자가 크게 뜨였다.

「당신은……?」

희미하게 비치는 달빛 아래, 이정룡이 미소 띤 얼굴로 말을 이었다.

“우리가 긴히 나눌 이야기가 있을 것 같은데. 어찌 생각하나?”

「……!」



* * *



띠링.



- [운기조식]을 완료했습니다!

- [열화신공]의 경지가 미약하게 상승합니다!



기운을 갈무리하고 눈을 떴을 때는 밖이 환하게 밝아 오고 있었다.

마치 이때만을 기다리고 있었다는 듯 스켈레톤 워로드가 냉큼 입을 연다.

- 간악한 인간. 드디어 일어났나?

“안 잤어, 인마.”

- 전투를 앞두고 술을 마시다니. 쯧쯧.

“어차피 술병 날 일 없으니까 조용히 해라.”

술을 많이 마시면 주독(酒毒)이 쌓이는데, 어지간한 내가 고수라면 손쉽게 주독을 몰아낼 수 있다.

강대한 열양지기를 지닌 나는 말할 것도 없지.

‘그러고 보니 엄청나게 마시긴 했지. 파이 첸이 전용기로 실어 온 술을 몽땅 거덜 냈을 정도니까.’

분명히 매직 존슨을 말리러 간 거였는데, 어쩌다가 그렇게 됐는지 나도 잘 모르겠다.

- 그런데 인간. 언제까지 이런 갑갑한 곳에 있을 생각인가?

“안 그래도 갈 생각이야.”

시계를 보니 오전 다섯 시 반. 슬슬 준비해야 할 때다.

임시 숙소로 배정받은 호텔 룸에서 짐을 챙긴 뒤 로비로 내려가자, 커피를 마시고 있는 최 팀장이 보였다.

“어, 팀장님.”

“……나오셨군요.”

슬쩍 보니 눈 밑이 퀭하다. 평소 철저한 자기 관리로 잡티 하나 없던 피부가 까슬까슬해 보인다.

“혹시 안 주무셨어요?”

“진태경 씨 같으면 잠이 오겠습니까?”

“…….”

그건 그래.

어젯밤, 세상에서 가장 다급한 호출 문자를 받고 달려간 내가 목격한 광경은 참혹하기 그지없었다.



‘헤이, 최. 이건 술 게임이잖아. 쿨하게 한 번 하자고. 안 그래?’

‘파이 첸! 도와주십시오, 파이 첸!’

‘으음……. 미안한데 이건 술 게임인걸. 왕의 명령은 절대적이다. 이게 룰 아냐?’

‘아무리 그래도 뽀뽀라니! 저는 술 게임 자체도 처음이란 말입니다! 룰도 제대로 설명 안 해 주셨잖아요!’

‘아. 몰라, 몰라. 2번은 3번의 볼에 입 맞출 것. 이게 내 명령이야.’

‘최. 가만히 있어. 난 네게 속박 마법을 걸고 싶지 않아.’

‘이건 말도 안…… 진태경 씨! 여깁니다, 진태경 씨!’

‘진. 방해하지마. 난 네게 공격 마법을 쓰고 싶지 않아.’



정말이지, 일 분만 늦었어도 대참사가 벌어질 뻔했다.

최 팀장을 구제해 주는 대가로 엄청난 양의 술을 원샷 해야 했지만, 일말의 후회도 없다. 그에 걸맞은 합당한 보상을 약속받았으니.

“혹시 어제 했던 약속, 기억하시죠? 제 정산 비율 조정하기로 한 거.”

“……알고 있습니다. 9대1.”

최 팀장이 싸늘한 눈빛으로 나를 노려보았다.

“어떻게 그런 급한 상황에서 그러실 수가 있습니까? 사람입니까?”

“그럼 지금이라도 찐하게 뽀뽀 한번 하시든가. 마침 저기 오시네, 2번님.”

번호는 2번이지만 게이력은 세계 제일이지.

지금 막 로비에 들어선 거구의 흑인, 매직 존슨을 발견한 최 팀장이 마시고 있던 커피를 뿜었다.

“푸웁! 저 좀, 저 좀 숨겨 주십시오.”

“이미 늦은 것 같은데.”

내 말이 끝나기가 무섭게, 우리를 발견한 매직 존슨이 솥뚜껑만 한 손바닥을 흔들었다.

“헤이, 게이즈!”

보통은 가이즈 아닌가. 잘못 말한 거겠지……?

순간 귀를 의심하는 나와 최 팀장에게 다가온 매직 존슨이 껄껄 웃었다.

「너무 그런 표정 짓지 마. 어제는 내가 너무 흥분해서 아주 약간 장난친 거니까.」

“……진짜 흥분하셨어요?”

「아, 그게 그렇게 되네.」

“말조심해 주세요. 깜짝 놀랐네.”

「하하. 어쨌든 어제는 좀 사정이 있었어.」

“……뭐가 있었다고요?”

「어? 아니, 사정이 그 사정이 아니라.」

“말조심 좀 해 주세요. 진짜 깜짝 놀랐네.”

“제발 두 분 다 그만하시죠. 누가 들을까 봐 겁납니다.”

해탈한 얼굴로 남아 있던 커피를 원샷한 최 팀장이 고개를 돌렸다.

어느새 호텔 정문을 통과한 한 무리의 사람들이 우리를 향해 걸어오고 있었다.

「이제 떠날 시간이오. 선생들.」

그중 선두에 있던 국방부장 웨이펑후의 목소리는 긴장으로 딱딱하게 굳어 있었다.

그의 눈짓에 나이 지긋해 보이는 군 장성 하나가 서류철을 하나씩 나눠 주었다.

“이게 뭡니까?”

「선생들이 배치된 지역과 주둔 병력에 대한 정보요. 물론 저쪽에도 미리 필요한 정보와 연락은 취해 두었소. 지금부터는 지정된 제트기를 타고 이동할 거요.」

아무래도 최첨단 기술이 발달한 현대이다 보니, 이런 것만큼은 편리하다.

잠시 후 웨이펑후의 뒤를 따라 도착한 임시 이륙장에는 삼엄한 경호에 둘러싸인 익숙한 얼굴들이 있었다.

「잘 잤니, 젊은이들?」

「…….」

“늦었군.”

기지개를 쭉 켜며 인사를 건네는 파이 첸. 어제 있었던 일 때문인지 말없이 시선을 내리까는 우헤이싱과 묘한 미소를 짓고 있는 이정룡까지.

인벤토리 안에 고이 넣어 둔 스켈레톤 워로드가 떨떠름한 목소리로 말했다.

- 왠지 모르게 기분 나쁜 인간이로군. 본 사령관은 저자가 썩 마음에 들지 않는다.

“동감이야.”

작게 중얼거린 소리를 들은 파이 첸이 눈썹을 치켜올렸다.

「응? 뭐라고?」

“아닙니다. 그나저나 필릭스 왕자는요?”

「동트기 직전에 떠났어. 왕자가 맡게 된 지역에서 교전 신호가 왔다던데.」

“……그렇군요.”

도착한 지 24시간도 되지 않아 또다시 전투가 벌어지다니.

새삼 전쟁이라는 두 글자에 문득 가슴 한구석이 꾸욱, 하고 조여 온다.

국적도, 자라난 환경도 다르지만 나와 같은 인간이 어딘가에서 무참히 살육당하고 있다고 생각하니 마음이 무거워졌다.

「거기 젊은이.」

“예?”

나를 물끄러미 바라보던 파이 첸이 어깨를 툭 쳤다.

「어깨에 힘 풀어. 무거워서 창이나 제대로 휘두르겠어?」

“…….”

「자책하지도 말고 조급해할 필요도 없어. 모든 죽음에 책임을 지려 하지 말라고.」

책임이라. 잠깐 고민하던 나는 솔직히 대답했다.

“……글쎄요. 그다지 자신은 없네요.”

「뭐, 그런 것치고는 어제 술을 진탕 퍼마시긴 하던데.」

“그건…….”

「알아, 농담이야. 우리 같은 사람들은 그렇게라도 잠시 부담감을 잊는 거지. 당장 내일, 아니 오늘 죽을지도 모르는 목숨이니까.」

밝은 목소리에 어울리지 않는 내용. 대격변이라는 소용돌이를 온몸으로 헤쳐나온 영웅은 고개를 들어 하늘을 바라보았다.

「아, 싸우기 딱 좋은 날씨다.」

그러고는 몸을 돌려 이륙 준비를 끝마친 제트기를 향해 사뿐사뿐 걸음을 옮긴다.

나직한 한마디를 남긴 채.

「모두…… 살아서 보자.」

그녀의 뒷모습이 기체 내부 안으로 사라졌다.

잠시 감회에 찬 눈빛으로 하늘을 올려다보던 매직 존슨이 불쑥 입을 열었다.

「헤이, 최.」

“네?”

「너도 엉덩이에 힘 풀어.」

“…….”

「아니, 어깨에 힘 풀어. 살아서 다시 보자고.」

저거 아무래도 진심이 나온 것 같은데.

최 팀장의 경계 어린 눈빛에 껄껄 웃은 매직 존슨이 파이 첸의 뒤를 이어 기체에 몸을 실었다.

이어 우헤이싱이 도망치듯 발걸음을 옮겼고, 마지막으로 남은 이정룡이 묘한 눈빛으로 나와 최 팀장을 훝었다.

“둘 다 몸조심하게. 이런 곳에서 요절할 수야 없지 않나. 젊은 나이에.”

노인네 말본새 하고는. 정말이지, 의미심장한 한마디다.

얼굴을 굳힌 최 팀장을 대신해, 내가 웃으며 입을 열었다.

“그래야죠. 우린 누구와 다르게 지금 죽어도 호상(好喪)은 아니니까.”

“……!”

“혹시 골로 가시면 부조 넉넉하게 하겠습니다.”

“기대하지.”

짧은 침묵 끝에 한마디를 툭 내뱉은 이정룡이 아레스 길드원들을 이끌고 멀어져 간다. 이제 남은 것은 우리뿐.

있는 힘껏 기지개를 켠 나는 최 팀장의 어깨를 두드렸다.

“가시죠. 팀장님.”

“예. 그래야죠.”

“긴장할 것 없습니다. 엉덩이에 힘 푸세요.”

“…….”

“……농담이었는데. 죄송합니다.”

농담 두 번 하면 사람 죽일 기세다.

슬금슬금 최 팀장의 눈치를 살피며 기체에 오르던 그때였다.

「부대- 차렷!」

등 뒤에서 터져 나온 우렁찬 외침.

국방부장 웨이펑후가 반백의 머리를 흩날리며 우리를 향해 거수경례를 올리고 있었다.

그러자 이륙장을 가득 메운 사람들이 웨이펑후를 따라 경례 자세를 취했다.

자신들의 가족과 친구들을 위해 싸우러 가는 영웅들을 향한 경의.

그들의 경례는 제트기의 문이 닫히고, 까마득한 점이 되어 시야에서 사라질 때까지 끝나지 않았다.

‘거, 참.’

이렇게까지 해 주니 어깨가 무거워질 수밖에.

문득 피로를 느끼며 시트에 몸을 기댄 다음 순간이었다.

치직. 치지직.

- ……답. 응답하라. 여기는…….

갑자기 조종석에서 들려오는 노이즈 낀 무전과 함께 귓속을 파고드는 알림.

띠링.



- 돌발 퀘스트, [다급해진 전황]이 생성되었습니다.

- 당신은 퀘스트를 거절할 수 없습니다. 한시라도 빠르게 도착하여 적들을 물리치십시오!



“…….”

빌어먹을, 내 인생이 이렇지 뭐.

푹 한숨을 내쉰 나는 조종석을 향해 힘차게 외쳤다.

“아저씨, 풀 악셀 땡겨요!”



* * *



「그들은?」

입을 연 것은 팔십 대의 노인이었다. 주름과 검버섯이 가득한 얼굴. 늙은 육신은 소싯적만 못했지만, 그의 눈동자에는 젊었을 적보다 더한 힘이 있었다.

홀로그램 화면으로도 느껴지는 노인의 힘 있는 눈빛에, 마른침을 삼킨 웨이펑후가 대답했다.

「모두 출발했습니다. 주석 동지.」

「전황은 어떤가?」

「마법으로 인한 통신 교란과 결계로 적들의 동태를 쉽게 파악할 수 없습니다만, 최선을 다해 이동을 감지 중입니다.」

「S급 헌터들이 도착한다면…….」

「그들의 힘이라면 충분히 전황을 뒤집을 수 있습니다.」

「속단은 금물이야. 한순간도 방심하지 말게. 수많은 이들의 목숨이 우리의 결정에 달렸네.」

「예. 명심하겠습니다.」

웨이펑후 국방부장과의 짧은 통신이 끝난 후, 샤오 양 중국 주석은 드넓은 회의실에 앉아 생각에 잠겼다.

‘어쩌다 이리되었는지.’

대격변 이후 유례없는 대참사다. 수많은 인력과 자금을 투입했지만 아크 리치를 중심으로 한 몬스터 군단을 막을 수는 없었다.

가급적이면 혼란을 막고 싶었지만…… 더 이상 늦으면 기회는 영영 사라질지도 모른다.

그렇기에 샤오 양은 공산당 내부의 숱한 반대를 무릅쓰고 오늘, 이 자리에 왔다.

「준비되었습니다.」

「……즉시 연결하게.」

비서관의 말에 샤오 양은 감았던 눈을 떴다.

넓은 회의실, 비어 있던 자리 위로 홀로그램으로 이루어진 형체들이 하나둘씩 떠오르기 시작했다.

인종도, 성별도 모두 다른 열넷. 아니 샤오 양을 포함한 열다섯 명의 사람들.

그들 한 사람, 한 사람은 일국의 지도자들이었고 하나의 기구에 속해 있었다.

‘유엔 안전보장이사회(The Security Council).’

늙은 주석은, 무거운 목소리로 긴급회의의 시작을 알렸다.
```

## Current accepted English baseline

```markdown
# Chapter 388

“Hey. Hey.”

Tap. Tap-tap.

The tip of someone’s foot nudged Wu Heixing in the side. He barely opened his eyes, and a huge shape loomed over him.

“Hngh…”

“I’ve got something urgent to take care of, so I have to leave. If anyone comes by, make up some excuse for me.”

“Hngh… hngh…”

“I poured an Advanced Potion over you, so quit pretending, punk. Keep it up, and I might call Magic Johnson over and make you moan for real. See you!”

Fwish!

After leaving behind a parting remark that made his butt ache just from hearing it, the person’s presence rapidly faded into the distance.

It was a little over ten minutes later that Wu Heixing, still sprawled spread-eagled, finally growled in a seething voice.

“Jin Taekyung…!”

His broken bones and flesh had recovered thanks to the Advanced Potion, but it could not heal the pain etched deep into his bones or his cracked pride.

*How?*

It was impossible to believe. No matter how excited he had been, how could an S-rank Hunter like him have been toyed with so thoroughly?

The fact that Jin Taekyung had seen through his martial arts was shocking enough, but for someone who took such immense pride in his own power, the shock of defeat struck even harder.

*Me? Me, of all people?*

Wu Heixing had been born with a Hunter’s fate.

Even as an infant, his potential had been recognized through an enormously expensive mana aptitude test, and his family—part of the highest echelons of the Chinese Communist Party—had spared no expense supporting him.

Vast wealth and power accumulated through corruption. Raised in the finest environment with every possible advantage, Wu Heixing awakened as an A-rank Hunter at the age of twenty. Ten years later, he achieved the remarkable feat of becoming an S-rank Hunter.

And yet…

*But why? Why was I defeated by that bangzi bastard from such a small country?*[^1]

A fierce light flashed in Wu Heixing’s eyes as he glared at the pitch-black night sky.

His gaze held anger, but also jealousy—and a trace of fear toward the power Jin Taekyung had displayed.

And those emotions were ones Wu Heixing had been sickeningly familiar with for more than a decade.

Toward the one person he could no longer find, Wu Heixing shouted.

“Was this your doing? Are you trying to torment me even after death?”

The public and the media cursed him as an incorrigible degenerate while praising him as a genius born of Zhonghua, but a tiny handful of people, Wu Heixing among them, knew the truth.

The true genius was someone else. That was why they had kept him hidden instead of letting him come to light.

“Answer me, Lei Fei!”

Lei Fei possessed not only overwhelming skill but also a noble character. To Wu Heixing, he had been an insurmountable wall.

How flustered—and delighted—had Wu Heixing been when he first heard that Lei Fei had disappeared?

But in just one week, another wall had appeared.

His name was Jin Taekyung.

“Gaaaaaaaaah!”

His roar echoed across the night, making the bushes tremble.

“That feeling… I know it well, too.”

At the quiet voice of someone who had approached without making a sound, Wu Heixing sprang to his feet like a bolt of lightning.

“Who are you?”

“I’m hurt. I thought we knew each other.”

Step.

A figure suddenly stepped out of the darkness. Wu Heixing’s eyes widened.

“You’re…?”

Beneath the faint moonlight, Lee Jungryong continued with a smile.

“It seems we have something important to discuss. What do you think?”

“...!”

* * *

Ding.

> **System**
>
> - You have finished circulating your qi!
>
> - Your realm in the Blazing Flame Divine Art has risen slightly!

By the time I gathered my qi and opened my eyes, the world outside had brightened.

As though it had been waiting for this exact moment, the Skeleton Warlord promptly opened its mouth.

- Vile human. You have finally awakened?

“I wasn’t asleep, punk.”

- You drank alcohol before a battle. Tsk, tsk.

“I’m not going to get a hangover, so shut up.”

Drinking too much caused alcohol toxins to build up, but any halfway decent internal arts master could easily purge them.

With my powerful Scorching Yang Qi, I had even less to worry about.

*Come to think of it, I really did drink a lot. I drank every last bottle of alcohol Pai Chen had flown in on her private jet.*

I had definitely gone there to stop Magic Johnson, but I had no idea how things had ended up like that.

- Human, how much longer do you intend to stay in this cramped place?

“I was planning to leave anyway.”

The clock showed five-thirty in the morning. It was about time to get ready.

After packing my things in the hotel room assigned to me as temporary lodging, I went down to the lobby and found Team Leader Choi drinking coffee.

“Oh, Team Leader.”

“...You’re out.”

A quick glance told me his eyes were hollow with exhaustion. His skin, usually flawless thanks to his meticulous self-care, looked rough.

“Did you not sleep?”

“If you were in my position, Mr. Jin, would you be able to sleep?”

“...”

Fair point.

Last night, I had received the most desperate emergency message in the world and rushed over. What I witnessed there had been nothing short of horrifying.

*“Hey, Choi. This is a drinking game. Come on, just do it once. Be cool. Right?”*

*“Pai Chen! Please, help me, Pai Chen!”*

*“Hmm… Sorry, but this is a drinking game. The king’s command is absolute. Isn’t that the rule?”*

*“Even so, a kiss? This is my first drinking game! You didn’t even explain the rules properly!”*

*“Ah, whatever, whatever. Number Two will kiss Number Three on the cheek. That’s my command.”*

*“Choi. Stay still. I don’t want to cast a binding spell on you.”*

*“This is absurd… Jin Taekyung! Jin Taekyung, over here!”*

*“Jin. Don’t interfere. I don’t want to use an attack spell on you.”*

Honestly, if I had been one minute late, it would have ended in a catastrophe.

I had been forced to chug an enormous amount of alcohol in exchange for rescuing Team Leader Choi, but I had not regretted it for a second. I had been promised a fair reward in return.

“You remember the promise you made yesterday, right? You said you’d adjust my share of the settlement.”

“...I remember. Nine to one.”

Team Leader Choi glared at me coldly.

“How could you do that in such an emergency? Are you even human?”

“Then give him one good, passionate kiss right now. Number Two is coming over.”

He might have been Number Two, but his gay stat was the highest in the world.

Team Leader Choi spotted the huge Black man just entering the lobby—Magic Johnson—and spat out the coffee he had been drinking.

“Ptooey! Please, please hide me!”

“I think it’s already too late.”

The moment I finished speaking, Magic Johnson spotted us and waved a palm the size of a pot lid.

“Hey, gays!”

Wasn’t it usually *guys*? He must have misspoken… right?

Magic Johnson approached us as Team Leader Choi and I stood there, wondering if we had heard correctly, then laughed heartily.

“Don’t make such expressions. I was just a little excited yesterday and playing around.”

“...You were really excited?”

“Ah. I suppose that’s how it sounded.”

“Watch what you say. You startled me.”

“Haha. Anyway, something came up yesterday.”

“...What came?”

“Huh? No, not that kind of coming.”

“Watch what you say. You really startled me.”

“Please, both of you, stop. I’m afraid someone will hear you.”

Team Leader Choi, wearing an utterly enlightened expression, drained the coffee that remained in his cup and turned his head.

A group of people had passed through the hotel’s main entrance and were walking toward us.

“It is time to depart, gentlemen.”

The voice of Minister of Defense Wei Penghu, who led the group, was stiff with tension.

At his signal, a military general who looked well into his later years began handing out folders one by one.

“What is this?”

“Information on the areas to which you have been assigned and the forces stationed there. Of course, we have already sent the necessary information and established communications with the people on that side. From now on, you will travel aboard the designated jets.”

Modern technology did have its conveniences.

A short while later, at the temporary airfield where we arrived behind Wei Penghu, I saw several familiar faces surrounded by tight security.

“Did you sleep well, youngsters?”

“...”

“You’re late.”

Pai Chen greeted us while stretching her arms high. Wu Heixing silently lowered his gaze, perhaps because of what had happened yesterday, while Lee Jungryong wore a strange smile.

The Skeleton Warlord, safely stored inside my Inventory, spoke in a displeased voice.

- There is something unpleasant about that human. This commander does not like him one bit.

“I agree.”

Pai Chen raised an eyebrow after hearing my mutter.

“Hm? What did you say?”

“Nothing. By the way, where is Prince Felix?”

“He left just before dawn. Apparently, a battle signal came from the area assigned to him.”

“...I see.”

Another battle had broken out less than twenty-four hours after our arrival.

At the thought of the word *war*, something suddenly clenched in one corner of my chest.

Our nationalities and upbringings were different, but the thought of people just like me being brutally slaughtered somewhere weighed heavily on my heart.

“Hey, young man.”

“Yes?”

Pai Chen stared at me for a moment, then gave my shoulder a light tap.

“Relax your shoulders. They’re so tense you won’t be able to swing your spear properly.”

“...”

“Don’t blame yourself, and don’t rush. Don’t try to take responsibility for every death.”

Responsibility.

I thought about it for a moment before answering honestly.

“...I’m not sure. I can’t say I’m very confident.”

“Well, you certainly drank yourself senseless yesterday, for someone who feels that way.”

“That was…”

“I know. I’m joking. People like us forget the burden for a little while that way. We’re lives that might die tomorrow—or even today.”

The content did not suit her bright voice at all.

The hero who had fought her way through the Great Cataclysm with her entire body raised her head and looked at the sky.

“Ah. Perfect weather for a fight.”

Then she turned and began walking lightly toward the jet, which had finished preparing for takeoff.

She left us with one quiet remark.

“Let’s all see each other alive.”

Her back disappeared inside the aircraft.

Magic Johnson gazed up at the sky for a moment with an unusually solemn expression, then abruptly opened his mouth.

“Hey, Choi.”

“Yes?”

“Relax your ass, too.”

“...”

“No, I mean relax your shoulders. Let’s see each other alive again.”

*I had a feeling his true feelings had just slipped out.*

Magic Johnson laughed heartily at Team Leader Choi’s wary gaze and boarded the aircraft after Pai Chen.

Wu Heixing followed, walking as though he were trying to escape. Finally, Lee Jungryong was left behind. He looked us both over with strange eyes.

“Both of you, take care. You can’t go dying young in a place like this—not at your age.”

*What an old man’s way of putting it. What a meaningful thing to say.*

I smiled and spoke in place of Team Leader Choi, whose face had gone rigid.

“We should. Unlike some people, dying now wouldn’t exactly be a good death for us.[^2]”

“...!”

“If you kick the bucket, I’ll make a generous condolence contribution.”

“I’ll look forward to it.”

After a brief silence, Lee Jungryong tossed out that one remark and led the Ares Guild members away.

Now only the two of us remained.

I stretched as hard as I could, then patted Team Leader Choi on the shoulder.

“Let’s go, Team Leader.”

“Yes. We should.”

“There’s nothing to be nervous about. Relax your ass.”

“...”

“...I was joking. Sorry.”

*At this rate, two jokes would be enough to kill a man.*

I was cautiously watching Team Leader Choi’s expression as I climbed aboard the aircraft when—

“Troops—attention!”

A thunderous shout erupted behind us.

Minister of Defense Wei Penghu was saluting us, his half-gray hair whipping in the wind.

The people filling the airfield followed Wei Penghu and assumed the same salute.

It was a display of respect for the heroes going off to fight for their families and friends.

Their salutes did not end until the jet door closed and the aircraft disappeared from sight as a distant speck.

*Good grief.*

After all that, there was no way my shoulders wouldn’t feel heavy.

I suddenly felt tired and leaned back against my seat.

Static crackled.

- …respond. Respond. This is…

Along with the distorted radio transmission coming from the cockpit, an alert pierced my ears.

Ding.

> **System**
>
> - Unexpected Quest generated: The Battle Situation Has Become Critical.
>
> - You cannot refuse the Quest. Arrive as quickly as possible and defeat the enemies!

“...”

*Damn it. That’s just how my life is.*

I let out a deep sigh, then shouted toward the cockpit.

“Sir, give it full throttle!”

* * *

“What about them?”

The person who spoke was an old man in his eighties. His face was covered in wrinkles and age spots. His aged body was no longer what it had been in his youth, but his eyes held even greater power than they had back then.

Even through the holographic screen, the force in the old man’s gaze could be felt. Wei Penghu swallowed hard before answering.

“They have all departed, Comrade Chairman.”

“How is the battle situation?”

“We cannot easily determine the enemy’s movements because of communication interference caused by magic and the barriers, but we are doing our best to detect their movements.”

“If the S-rank Hunters arrive…”

“With their power, they should be more than capable of turning the tide.”

“Do not jump to conclusions. Do not let your guard down for even a moment. The lives of countless people depend on our decisions.”

“Yes. I will keep that in mind.”

After the brief communication with Minister of Defense Wei Penghu ended, state chairman Xiao Yang sat alone in the vast conference room, lost in thought.

*How did things come to this?*

This was an unprecedented catastrophe since the Great Cataclysm.

Despite pouring in vast amounts of personnel and funding, they had been unable to stop the monster army centered around an Arch Lich.

He had wanted to prevent panic as much as possible, but if they delayed any longer, the opportunity might disappear forever.

That was why Xiao Yang had come here today, despite the countless objections from within the Communist Party.

“We’re ready.”

“...Connect me immediately.”

At the secretary’s words, Xiao Yang opened his closed eyes.

One by one, holographic figures began to appear above the empty seats in the vast conference room.

Fourteen people of different races and genders.

No—fifteen, including Xiao Yang.

Every one of them was the leader of a country, and they belonged to a single institution.

*The United Nations Security Council.*

The old chairman announced the beginning of the emergency meeting in a heavy voice.

[^1]: *Bangzi* is a derogatory Chinese slur for Koreans.

[^2]: A *ho-sang* is a death considered fortunate because it comes after a long, full life, usually at an advanced age.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 388`.

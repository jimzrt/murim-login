# Master Edit Task — Chapter 389

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
| 철수     | **Cheol Soo**      |
| 이정룡    | **Lee Jungryong** |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 살기     | **killing intent**                               |                                                       |
| 가주     | **Family Head**                              |
| 극양                        | **Extreme Yang**      |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 사천     | **Sichuan**            |
| 귀가      | **your family**                                                 |
| 우헤이싱 | **Wu Heixing** | S-rank Hunter antagonistic toward Taekyung. |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 백염 | **White Flame** | Previously bound item listed by the System. |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 쓰촨성 | **Sichuan Province** | Province containing Chengdu International Airport. |
| 중화인민공화국 | **People's Republic of China** | Country whose flag appears on Shao Shen's armor. |
| 중화 | **Zhonghua** | Term used in Shao Shen's rallying cry for China. |
| 시벌좌 | **Sibeol-jwa** | Taekyung's profane nickname, recognized by Shao Shen. |
| 염화일로 | **Flamefire Path** | Named fire-based movement technique used by Jin Taekyung. |
| 김철수 | **Kim Cheol Soo** | Generic Korean name used in a forum joke. |
| 제임스 | **James** | Generic English name used in a forum joke. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 우헤이싱 | 진태경 | hostile_peer | peninsula bangzi | abusive-hostile | Wu Heixing repeatedly addresses Taekyung with an anti-Korean slur. |
| 진태경 | 우헤이싱 | hostile_peer | mainland chink | abusive-hostile | Taekyung answers Wu Heixing's slur with an explicit anti-mainland insult. |
| 우헤이싱 | 이정룡 | junior_s_rank_hunter_to_top_s_rank_hunter | Mr. Lee | intimidated-deferential | Uses 이 선생님 and suppresses his usual hostility in Lee's presence. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
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

#### Chapter 387 tail (verified mastered)

…
Well, this is the mainland, after all. There could still be all kinds of martial arts here. An internal-energy cultivation technique, for example.” “W-what are you talking about? That was a Message Spell…” “Oh, please.” A dry laugh escaped me at the sight of his frantic excuses. People who had never encountered martial arts might not be able to tell the difference, but he couldn’t fool me. *Come see me for a moment.* What had reached my ear near the end of the meeting had unmistakably been Sound Transmission. The reason I had accepted an offer I could have ignored was that Wu Heixing himself had sent it. “H-how did you know that?” “What, was it a secret no one else knew?” I stared at the flustered Wu Heixing and continued. “I did think it was somewhat possible, but it’s still fascinating. Didn’t you wipe out all the martial artists during your Cultural Revolution and whatnot? Martial arts somehow survived even through that.” “Shut your mouth!” “Ah, you said your family was powerful. Did the highest levels of the Communist Party use their positions to quietly spirit it away?” “…” His expression instantly sank. *Looks like I was right.* As a foreigner, I didn’t know exactly how serious a problem this was. But I knew how valuable an internal-energy cultivation technique was—the thing now called a mana cultivation method in the modern era. *If this were the Murim, a bloody storm would have erupted.* Now that he’d been caught with the golden calf that had been secretly spirited away, no wonder he wasn’t taking it well. “It would be best if you never uttered what you just said again.” “I wasn’t planning to, but that tone of yours is pretty damn irritating.” Wu Heixing glared at me viciously. “Do you think you’ll still be able to act this way once you learn who my father is?” “I don’t know who your father is, but I have a feeling he used to be a Red Guard.” “…!” “Wasn’t your father the one who smashed Confucius’s tomb with a sledgehammer in his youth?” “You fucking *bangzi* bastard—!” Fwish! With a furious roar, he shot forward. A straight sword had already been drawn from its scabbard. The Aura Blade rising from it—no, the Sword Force—flew toward my neck. Shiiiiing! The cool wind scattered my hair. I bent backward until my back nearly touched the ground, letting the Sword Force pass overhead, then sprang upright and drove my knee into his chin. Crack! Teeth and blood shot into the air. As he staggered, I seized both his arms and whispered into his ear. “I told you not to draw that sword.” Hiss! Crack! “Gaaaaaaaaah!” The powerful Scorching Yang Qi surging through both my hands shattered his armor and seared his flesh. The scream that tore from Wu Heixing’s lips struck the Qi Curtain I had spread and went no farther. “You bastard!” Whooom! That bastard had learned fist-and-foot techniques too. Unlike his shoddy sword technique, this one was reasonably sharp. Of course… *Compared with the Murim, the quality of his martial arts was far lower.* Slightly disappointed, I reached out. Boom! Internal energy collided with internal energy. The leg he had whipped toward my waist like a lash stopped dead. Wu Heixing’s eyes trembled with shock and disbelief. “H-how?” “Well.” I grabbed his ankle and slammed him into the ground with all my strength. Whoom! Boom! Once more. Whoooom! Crash! More, more, more. Crash! Crash! KRA-KOOM! The ground turned over, and rocks and trees were ripped from the earth. A little while later, when I finally stopped using him as a living pickaxe, Wu Heixing lay spread-eagled in a huge crater, looking as if his soul had left his body. “Still, you’ve got a sturdy body. You’re not hurt that badly.” “Hh… hhaa…” “Hey, are you crying?” “Hhaaa…” He was completely out of it. Clicking my tongue, I bent over and searched through his pockets. After rummaging through the pouch enchanted with spatial expansion magic for some time, I finally found what I wanted. “Ah, here it is. An Advanced Potion.” Ding. > **System** > > **Acquired:** Supreme Potion! “…No, wait. Supreme Potion? What the hell, you bastard?” I stared in shock at the sprawled-out Wu Heixing. Even for an S-rank Hunter, who carried something like this around? Advanced Potions were rare enough, but only one or two Supreme Potions appeared in an entire year, if that. Never mind the price, which was so high it hardly felt real. They were so scarce that even having the money wasn’t enough to get one. *I’d only ever seen one online. And now here it is.* After a moment’s thought, I quietly slipped the Supreme Potion into my inventory. Then I searched his pouch again, found an Advanced Potion, and poured it over him. “I’ve taken my settlement payment, so I’ll let you off here. You’ve got plenty to hide yourself, so if you go around blabbing about what happened today… you know what’ll happen, right?” “Hh… hhh…” “Okay. We’ve reached a settlement.” Just as I neatly wrapped things up, the phone in my pocket shuddered. A short text message had arrived from Team Leader Choi. > 〈 Team Leader Choi > > Team Leader Choi > > Ji nTaekyung please come quic kly “…” *No, Johnson.* [^1]: *Bangzi* is a derogatory Chinese slur for Koreans.

#### Chapter 388 tail (verified mastered)

…
that way, you certainly drank yourself senseless yesterday.” “That was…” “I know. I’m joking. This is how people like us forget the burden for a little while. We might die tomorrow—or even today.” The words didn’t match her bright voice at all. The hero who had fought her way through the maelstrom of the Great Cataclysm with her entire body raised her head and gazed at the sky. “Ah. Perfect weather for a fight.” Then she turned and walked lightly toward the jet, which was ready for takeoff. She left us with one quiet remark. “Let’s all see each other alive.” Her back disappeared into the aircraft. Magic Johnson gazed up at the sky for a moment with emotion in his eyes, then abruptly spoke. “Hey, Choi.” “Yes?” “Relax your ass, too.” “…” “No, I mean relax your shoulders. Let’s see each other alive again.” *I had a feeling his true feelings had just slipped out.* Magic Johnson laughed heartily at Team Leader Choi’s wary gaze and boarded the jet after Pai Chen. Wu Heixing then walked off as though fleeing. Lee Jungryong, the last one left, looked Team Leader Choi and me over with a strange gaze. “Both of you, take care. You can’t go dying in a place like this when you’re still so young.” *What an old man’s way of putting it. What a loaded remark.* I smiled and spoke in place of Team Leader Choi, whose face had gone rigid. “We should. Unlike some people, dying now wouldn’t exactly count as a good death for us.[^2]” “…!” “If you kick the bucket, I’ll make a generous condolence contribution.” “I’ll look forward to it.” After a brief silence, Lee Jungryong tossed out that one remark and led the Ares Guild members away. Now only the two of us remained. I stretched with all my might, then patted Team Leader Choi on the shoulder. “Let’s go, Team Leader.” “Yes. We should.” “There’s no need to be nervous. Relax your ass.” “…” “…It was a joke. Sorry.” *At this rate, two jokes would be enough to kill a man.* I was cautiously watching Team Leader Choi’s expression as I climbed aboard the jet when— “Troops—attention!” A thunderous shout erupted behind us. Minister of Defense Wei Penghu was saluting us, his half-gray hair whipping in the wind. The people filling the airfield followed his example and saluted. It was a gesture of respect toward the heroes going to fight for the gathered crowd’s families and friends. They held their salutes until the jet’s door closed and the aircraft dwindled to a distant speck, then vanished from sight. *Good grief.* After a send-off like that, how could my shoulders not feel heavy? I suddenly felt tired and leaned back against my seat. Static crackled. - …respond. Respond. This is… Along with the distorted radio transmission coming from the cockpit, an alert pierced my ears. Ding. > **System** > > - Unexpected Quest generated: The Battle Situation Has Become Critical. > > - You cannot refuse the Quest. Arrive as quickly as possible and defeat the enemies! “…” *Damn it. That’s just how my life goes.* I let out a deep sigh, then shouted toward the cockpit. “Sir, give it full throttle!” * * * “What about them?” The speaker was an old man in his eighties. Wrinkles and age spots covered his face. His aged body was no longer what it had been in his youth, but his eyes held even greater strength than they had back then. Even through the holographic screen, the force of the old man’s gaze was palpable. Wei Penghu swallowed hard before answering. “They have all departed, Comrade Chairman.” “How is the battle situation?” “We cannot easily determine the enemy’s movements because of communication interference caused by magic and the barriers, but we are doing our best to detect their movements.” “If the S-rank Hunters arrive…” “With their power, they should be more than capable of turning the tide.” “Do not jump to conclusions. Do not let your guard down for even a moment. Countless lives depend on our decisions.” “Yes. I will keep that in mind.” After ending his brief communication with Minister of Defense Wei Penghu, state chairman Xiao Yang sat alone in the vast conference room, lost in thought. *How did it come to this?* This was an unprecedented catastrophe since the Great Cataclysm. They had committed vast amounts of manpower and funding, yet still failed to stop the monster army centered around the Arch Lich. He had wanted to prevent panic if at all possible, but if they delayed any longer, the opportunity might disappear forever. That was why Xiao Yang had come here today, despite the countless objections from within the Communist Party. “We are ready.” “…Connect me immediately.” At the secretary’s words, Xiao Yang opened his closed eyes. One by one, holographic figures began to appear above the empty seats throughout the vast conference room. Fourteen people of different races and genders. No—fifteen, including Xiao Yang. Each one was the leader of a nation, and all belonged to a single organization. *The United Nations Security Council.* The old chairman announced the beginning of the emergency meeting in a grave voice. [^1]: *Bangzi* is a derogatory Chinese slur for Koreans. [^2]: A *ho-sang* is a death considered fortunate because it comes after a long, full life, usually at an advanced age.

## Korean source

```text
＃389화



한파가 주춤한 어느 날이었다.

비로소 수능에서 해방된 수험생들은 재수를 준비하거나 놀기 바빴고, 직장인들은 눈 밑에 짙은 다크서클을 드리운 채 대중교통에 몸을 실었다.

그렇게 여느 때와 같은 평화로운 일상 속에서, 그 누구도 예상치 못한 폭탄이 떨어졌다.



[긴급 속보 - 유엔 안전보장이사회 중대 발표]



30분 남짓 길이의 영상은 무거운 눈빛으로 카메라를 응시하던 샤오 양 주석의 한 마디로 시작되었다.

「저는 중화인민공화국의 9대 국가주석이자 유엔 안전보장이사회의 일원으로서, 쓰촨성에서 벌어진 대규모 몬스터 웨이브를 말씀드리고자 이 자리에 섰습니다.」

전 세계의 이목을 집중시키고, 아시아 전체를 뒤흔들 폭탄이었다.



* * *



하루, 이틀, 사흘. 나흘이 지난 후에도 사태는 진정되지 않았다.

대격변 이후 수많은 사건 사고가 있었지만, 이번에 쓰촨성에서 벌어진 몬스터 웨이브는 유례를 찾아볼 수 없을 정도의 규모였다.

샤오 양 중국 주석은 공식 계엄령을 선포했고, 유엔 안전보장이사회의 승인하에 평화 유지군이 전선에 투입되었다.

전 세계의 이목이 집중된 상황.

그중에서도 특히 촉각을 곤두세우는 것은 중국과 인접한 아시아의 국가들이었다.

대한민국 역시 예외는 아니었다. 오늘도 국내 최대 포럼 사이트의 헌터 이슈란은 숯불 위 가마솥처럼 들끓고 있었다.



지금까지의 상황 요약해 준다.



이 중에서 안보리 중대 발표 영상 안 본 놈은 없겠지? 혹시 있으면 나가 뒤져야 됨. 이거 진짜 비상 상황임. 북쪽 수령 놈도 이미 아이튜브로 다 보고 여기 게시판도 눈팅 하고 있을 듯.

아무튼 지들 목숨 걸린 일까지 요약해 달라는 벌레 새1끼들 하도 많길래 참다 참다 쓴다.

1. 쓰촨성에서 원인 불명의 대규모 웨이브 발생. 현재 추정 사상자만 최소 30만.

물론 일주일 전 이야기고 지금은 비교할 수도 없겠지. 사실상 통계가 불가능하다고 봄.

2. 중국 정부가 나섰지만 생각했던 것보다 규모가 미쳤음.

아크 리치라는 놈을 중심으로 최소 수만에 달하는 몬스터 군단 결집.

인민해방군, 공군 개 털리고 공안 무력부 헌터들도 2천 명 넘게 실종(마법 방해로 통신 두절, 인공위성 감시 무력화돼서 생존 여부도 확인 못 함.)

3. 중국 정부가 비밀리에 몇몇 국가에 연락, 사태를 조속히 진압하기 위해 몇몇 S급 헌터들 고용. 이틀 전에 UN 평화 유지군까지 전선 투입해서 분전하는 중.

전투 현황은 안보리에서 업데이트하고 있으니까 관심 있는 놈은 여기 들어가 봐라.

(주소 첨부.)

아래부터는 내 개인적인 생각이니까 읽지 않아도 별 상관없음.

4. 정신머리 똑바로 박힌 사람들은 알겠지만, 지금 보통 심각한 상황이 아니다. 특히 중국 본토는 생지옥임.

쓸 만한 헌터들 끌어다가 전선에 투입하는 통에 관리가 소홀해진 다른 게이트 마력 수치도 불안하고, 모든 방면에서 초인플레이션 현상 일어나고 있음.

이게 진짜 무서운 게, 만약 전선 무너지고 몬스터 군단이 사천 밖으로 진격하게 되면…… 그 뒤는 상상에 맡긴다.

5. 그러니까 다들 ㅈ 되기 전에 마트 가서 비상식량 사 놔라. 물론 사재기로 부당이익 취하란 소리는 아님.

6. 이대로 끝내기에는 아쉬워서 국뽕 추가함.

우리의 시벌좌랑 아레스 길드 정 드래곤이 전선에서 활약 중이란다. 지금까지 빨던 대로 열심히 빨아라.

진짜 끗.



올라온 지 몇 시간 만에 조회수 10만을 돌파한 해당 게시글은 현 상황을 예의주시하고 있던 네티즌들의 댓글로 불타올랐다.



(Best댓글) 글 내용대로 심각한 상황은 맞는데, 글 작성자가 너무 분위기 쎄게 잡은 것도 있음ㅋㅋ S급 헌터들에 일반 헌터만 10만 명 참전했다는데 뭐가 그리 걱정임. 그리고 군대는 놀고 있냐?

└ ㅇㅇ걔들 지금 정비대에서 놀고 있음.

└ ……?

└ 뉴스 못 봤냐. 이번에 중국군 장비 죄다 고장 나서 최대 규모 군납 비리 드러난 거. 최소 수십조 원 규모라고 함. 발 묶인 사단이 한두 개가 아니라더라.

└ 어, 이거 어디서 많이 들어 본 얘기 같은데.

└ 제발 수통 좀 바꿔 줘라. 이 시팔 샛기들아. 작년에 전역했는데 왜 수통에서 아직도 노르망디 물맛이 나냐. 한 모금 마시면 내 이름이 김철수인지 제임스인지 헷갈리더라.

└ 김 상병님. 오늘 석식 명태 순살 조림입니다.

└ 안 먹어 ㅅㅂ

└ 그나저나 장비 고장 때문에 군대 발 묶인 것도 문제긴 한데, 걔들이야 뭐 남아도는 게 병력이라 ㄱㅊ. 어차피 몬스터한테 실질적인 타격을 줄 수 있는 건 헌터들이니까. 사실 그거 말고 더 큰 문제는 따로 있음.

└ 뭔데?

└ 몬스터 개체 수 10만 뚫음.

└ ??

└ ?????

└ 무슨 10만이야 ㅅㅂ; 개소리하지마.

└ 개소리가 아니라 유엔 안보리에서 발표한 오피셜임. 게시글 링크 타고 가서 확인해 봐라. 5분 전에 떴다.

└ 와…… 시발.

└ 윗 댓글 반응 보니까 진짠가 보네 ㅁㅊ;

└ 아니. 그냥 죄다 영어라 뭔 소린지 몰라서 그런 건데. 지금 가글 번역기 돌리고 있음.

└ 미친놈인가.

└ 야 근데 진짜 몬스터 10만 뚫었으면 큰일 난 거 아니냐. 지금까지 일어난 몬스터 웨이브 최대 규모라고 해 봐야 천 마리 안 넘었던 것 같은데;

└ 당연히 이번 웨이브도 초기에는 이 정도 규모 아니었지. 근데 저쪽에 아크 리치가 있는 게 문제야. 그냥 리치만 나타나도 큰 사건인데, 쟤는 학계에도 알려지지 않은 최상위 네임드 몬스터임. 사실상 현재 싸우는 몬스터들 대부분은 아크 리치가 부활시킨 언데드라고 해야 맞다.

└ 아크 리치 : “계왕권 100배.”

└ 그럼 아크 리치만 죽이면 되는 거 아님? 몬스터 대부분이 언데드면 조종자만 죽이면 끝나잖아.

└ ???????

└ 아크 리치를 누가 어떻게 죽이는데, 시벌 놈아. 키보드로 오러 블레이드 쓰는 새끼가 입만 살아 가지고.



치열한 갑론을박.

댓글을 다는 사람 중에는 강 건너 불구경하듯 바라보는 이들도 있었고, 이번 사태를 심각하게 받아들이는 이들도 있었다.

그렇게 종말론과 낙관론이 판을 치는 와중에도 새로운 소식은 끊임없이 업데이트되고 있었다.



(Best댓글) 안보리 오피셜, 한 시간 전 동서부 쪽 전선 뚫림. 다행히 파이 첸이 지원군으로 와서 피해 확산은 막았다고 함.

└ ㄷㄷ진짜네.

└ 동서부 전선이면 우헤이싱 있는 곳 아님?

└ 맞음. 중국 약쟁이 걔.

└ 근데 왜 뚫려. S급 헌터잖아.

└ 중국산 S급 헌터라 그럼.

└ 아…….

└ 파이 첸 없었으면 진짜 큰일 날 뻔했네. 파이 첸은 대격변 출신 웰메이드 헌터라 그런가.

└ 파이 첸은 부모님이 홍콩 국적이라 홍콩산임.

└ 윗 댓글 품질 관리 위원회에서 일하냐? ㅈㄴ 명쾌하네.

└ 그런 김에 한국산 헌터들 소식은 없냐.

└ 정 드래곤은 북부 전선 맡아서 우세 점하는 중이고, 시벌좌는 서부 전선에서 두세 번 승리했다고는 들었는데 그 후로 소식 없는 거 보니까 현상 유지 중인 듯.

└ 음…… 이정룡 실력이야 뭐 다 아니까 걱정은 안 하는데, 시벌좌는 무사하려나. 아직 A급 헌터잖아.

└ ??ㅋㅋㅋㅋ

└ ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

└ 아직도 시벌좌를 A급 취급하는 순진한 놈이 있눜ㅋㅋㅋㅋㅋㅋㅋㅋ현직 A급 헌터로서 웃음밖에 안 나온다. 진태경 쟤는 그냥 괴물임ㅋㅋ



야야ㅇ야야야!! 지금 안ㄴ보리에서 서ㅂ 전선 현황 발표함!

└ 오, 시벌좌 소식 오랜만이다.

└ 엄청 다급하네. 서부 전선? 뭐라는데?

└ 뚫렸다는데?

└ 어?

└ 어?

└ 뭔 소리야. 설마 시벌좌 죽었음……?

└ 잠깐만. 이게 뭔 내용이지. 얘들아 나 다시 보고 온다. 메인에 떴으니까 너희도 직접 가서 보셈.

└ 아. 갑자기 개후달리네; 당장 들어가 본다.

└ ㄱㄱㄱㄱㄱ



신나게 댓글을 작성하던 네티즌들은 황급히 유엔 안보리 홈페이지에 접속했다.

일시적으로 과도한 접속자가 몰린 탓에 트래픽 초과로 기다리길 한참. 마침내 메인 화면에 뜬 발표 자료을 본 그들은, 자신의 눈과 귀를 의심할 수밖에 없었다.

“……저게 뭐야.”

몬스터 군단과의 대치 상황을 표시해 놓은 지도. 타원형의 전선을 형성한 그곳에는, 송곳처럼 움푹 파고든 서부 전선의 모습이 그려져 있었다.



……방금 확인하고 왔다. 진짜 뚫렸네.

└ 진태경 죽음? 피해 얼마나 됨?

└ 아니, 몬스터 쪽이 뚫렸다고.

└ ??

└ ???

└ 돌파 속도가 너무 빨라서 업데이트가 못 따라간 거였음.

└ ……말이 되냐?

└ 입 다물고 셔터 내려라. 오늘 주모 제삿날이다…….



* * *



곧 치열한 전투가 벌어질 전장은 혼잡했다. 끝없이 펼쳐진 황무지. 무수히 많은 몬스터가 시야에 들어온다.

어디선가 불어온 바람에 놈들이 뿜어내는 짙은 살기와 악취가 묻어 나왔다.

“시부럴 거. 많이도 모였네.”

내 중얼거림에 곁에 서 있던 최 팀장이 대답했다.

“죽여도, 죽여도 끝이 없군요.”

서부 전선에 투입되어 본격적인 전투가 시작된 지 나흘째. 항상 말끔하던 최 팀장의 모습은 더 이상 찾아볼 수 없다.

핏물과 먼지로 뒤덮인 그는 침착하면서도 깊게 가라앉은 눈동자로 날 바라보았다.

“언제 시작합니까?”

“글쎄요, 그건 우리 꼬마 사령관님 의견을 들어 봐야지. 안 그래?”

마지막 물음표는 최 팀장을 향한 것이 아니다.

줄곧 내 곁에서 떨어지지 않고 있던 스물한 살의 ‘꼬마 사령관’. 샤오 쉔이 대답했다.

「저는 진 선생님의 명령에 따르겠습니다!」

녀석의 반짝거리는 눈빛에 실소가 터져 나왔다.

“아직도 그놈의 선생님 타령은. 나한테는 먼저 말 놓으라고 하던 녀석이. 차라리 형님이라고 부르라니까.”

「저, 정말 그래도 됩니까?」

“너만 괜찮으면 된다고 했잖아. 그런데 부하들 보는 앞에서 이래도 되는 거냐? 너 이제 소장 진급 한다며?”

샤오 쉔이 번개 같은 속도로 고개를 저었다.

「아무 문제 없습니다! 혀, 혀, 형님!」

싸울 때는 무서울 정도로 침착한데, 평소에는 왜 이렇게 말을 더듬는지 모르겠다.

나는 뒤에 정렬한 공안무력부 소속의 헌터들을 바라봤다. 자그마치 천여 명에 달하는 숫자.

뜨겁게 달아오른 눈동자에는 강자를 바라보는 선망과 경이로움이 깃들어 있었다.

물론 그중에서도 독보적인 건 샤오 쉔이지만.

「명령을 내려 주십시오. 혀, 형님.」

“명령이라.”

나는 문득 하늘을 올려다봤다.

거대한 날개를 펼친 독수리가 우리의 머리 위를 맴돌고 있었다. 오늘도 느낌이 좋다.

“따라와. 지금껏 해 왔던 것처럼.”

「……!」

“지금 당장.”

나는 대답과 함께 발을 내디뎠다.

쩌저적.

발끝에 실린 만근의 힘에 지면이 거미줄처럼 갈라지며 움푹 꺼진다.

그리고 다음 순간.

쾅!

귀가 먹먹해지는 굉음과 함께, 나는 빛줄기가 되어 쏘아졌다.

‘염화일로(炎火一路).’

추위를 머금은 바람이 달아오르며 열풍으로 변한다.

땅, 바람, 풍경이 빠르게 스쳐 지나가던 그때, 등 뒤에서 거대한 함성이 터져 나왔다.

「돌격! 돌격하라!」

「중화의 후예여! 인민이여! 놈들을 모조리 쓸어버려라!」

「와아아아아!」

두두두두!

캬우우우우!

천지에 울려 퍼지는 인간의 함성과 몬스터의 괴성. 거대한 진동이 지축을 떨어 울린다.

그 혼란의 입구 속에서, 나는 손에 쥔 백염(白炎)을 힘차게 휘둘렀다.

콰아아아!

창날에서 솟아 나온 극양의 강기가, 막아서는 모든 것을 베었다.
```

## Current accepted English baseline

```markdown
# Chapter 389

It was a day when the cold snap had finally eased.

Students finally freed from the college entrance exam were busy either preparing to retake it or having fun, while office workers boarded public transportation with dark circles hanging beneath their eyes.

And in the midst of that peaceful, ordinary routine, a bombshell no one had expected dropped.

**[Breaking News—United Nations Security Council Makes Major Announcement]**

The roughly thirty-minute video began with Chairman Xiao Yang staring gravely into the camera.

“I stand before you as the ninth state chairman of the People’s Republic of China and a member of the United Nations Security Council to speak about the massive monster wave that has occurred in Sichuan Province.”

It was a bombshell that seized the attention of the entire world and sent all of Asia into upheaval.

* * *

One day passed. Then two. Then three. Even after four days, the situation had not calmed down.

There had been countless incidents and accidents since the Great Cataclysm, but the monster wave that had erupted in Sichuan Province was unprecedented in scale.

Chinese state chairman Xiao Yang declared official martial law, and peacekeeping forces were deployed to the front with the approval of the United Nations Security Council.

The entire world was watching.

The Asian countries bordering China were especially on edge.

South Korea was no exception. Even today, the Hunter Issues section of the country’s largest forum site was boiling like a cauldron over a charcoal brazier.

Here’s a summary of the situation so far.

Nobody here hasn’t watched the Security Council’s major announcement video, right? If there is, go outside and die. This is a genuine emergency. Even that northern supreme leader bastard has probably watched the whole thing on iTube and is lurking on this forum too.

Anyway, there were so many fucking vermin demanding a summary of something that could literally cost them their lives that I finally got fed up and wrote one.

**1. An unexplained massive wave occurred in Sichuan Province. The current estimated casualties are at least 300,000.**

Of course, that estimate is already a week old, and the current figure probably can’t even be compared to it. Realistically, I think it’s impossible to calculate the numbers.

**2. The Chinese government intervened, but the scale was completely insane.**

A monster army numbering at least tens of thousands has gathered around a creature called an Arch Lich.

The People’s Liberation Army and Air Force were thoroughly wrecked, and more than two thousand Hunters from the Public Security Armed Forces have gone missing. Communications were cut off because of magical interference, and satellite surveillance was neutralized, so they can’t even confirm whether anyone survived.

**3. The Chinese government secretly contacted several countries and hired several S-rank Hunters to suppress the situation as quickly as possible. The UN peacekeeping forces were deployed to the front two days ago, and they’re fighting desperately.**

The Security Council is updating the battle situation, so anyone interested can check here.

*(Link attached.)*

Everything below this is just my personal opinion, so you can skip it if you want.

**4. Anyone with a functioning brain knows this, but the current situation is not merely serious. Mainland China is basically hell on earth.**

They’re dragging every usable Hunter to the front, so the mana levels of other Gates, which are being neglected, are unstable too. Hyperinflation is happening everywhere.

The truly frightening part is this: if the front collapses and the monster army advances beyond Sichuan…

I’ll leave the rest to your imagination.

**5. So go to the supermarket and buy emergency rations before everyone gets completely fucked. Of course, I’m not telling you to hoard supplies and make an unfair profit.**

**6. It felt like a shame to end things here, so I’m adding some patriotic hype.**

Our Sibeol-jwa and Ares Guild’s Jung Dragon are both doing great work at the front. Keep stanning them as hard as you have been.

The end.

Within a few hours of being posted, the thread surpassed 100,000 views and caught fire with comments from netizens watching the situation closely.

**(Best Comment)** The situation really is as serious as the post says, but the author is laying it on a little thick lol. There are S-rank Hunters in the fight, plus a hundred thousand regular Hunters. What’s there to worry about? And is the military just sitting around?

└ Yeah, they’re fooling around in the maintenance units right now.

└ …………?

└ Didn’t you watch the news? All the Chinese military equipment broke down this time, exposing the largest military-procurement corruption scandal ever. They say it’s worth at least tens of trillions of won. Apparently more than one or two divisions are stuck.

└ Huh. This sounds really familiar.

└ Please replace the canteens already, you fucking assholes. I got discharged last year, so why does mine still taste like Normandy water? Every time I take a sip, I can’t tell whether my name is Kim Cheol Soo or James.

└ Corporal Kim. Tonight’s dinner is braised boneless pollock.

└ Not eating that shit.

└ Anyway, the military being stuck because of broken equipment is a problem, but they have manpower to spare, so they’ll be fine. Hunters are the only ones who can actually hurt the monsters anyway. There’s a bigger problem than that.

└ What?

└ The number of monsters has broken through 100,000.

└ ??

└ ?????

└ What do you mean, 100,000? Fuck off; don’t talk nonsense.

└ It’s not nonsense. It’s official from the UN Security Council. Follow the link in the post and check it yourself. It was posted five minutes ago.

└ Wow… fuck.

└ Judging by the reaction above, I guess it’s true. Holy shit.

└ No. I only reacted like that because it’s all in English and I have no idea what it says. I’m running it through Goggle Translate right now.

└ Is this guy insane?

└ But seriously, if the monster count has really passed 100,000, isn’t this a disaster? The largest monster wave so far didn’t even exceed a thousand, did it?

└ Obviously, the wave wasn’t this big in the beginning. The problem is that there’s an Arch Lich over there. Even the appearance of an ordinary Lich would be a major incident, but that thing is a top-tier named monster unknown even to the academic world. Realistically, most of the monsters currently fighting are undead revived by the Arch Lich.

└ Arch Lich: “Kaioken times one hundred.”

└ Then can’t we just kill the Arch Lich? If most of the monsters are undead, killing the controller should end it, right?

└ ???????

└ Who the hell is going to kill the Arch Lich, you bastard? You can only use Aura Blade on a keyboard, and your mouth’s still the only thing that works.

A fierce argument broke out.

Some commenters watched from a safe distance, as though observing a fire across a river, while others took the situation extremely seriously.

And even as doomsday theories and optimism battled for control, new updates continued to pour in.

**(Best Comment)** Security Council official: The front in the east-west sector was breached an hour ago. Fortunately, Pai Chen arrived as reinforcement and prevented the damage from spreading.

└ Damn, it’s true.

└ If it’s the east-west front, isn’t that where Wu Heixing is?

└ Yeah. That Chinese junkie guy.

└ But how did it break through? He’s an S-rank Hunter.

└ Because he’s a Chinese-made S-rank Hunter.

└ Ah…

└ It could’ve been a real disaster if Pai Chen hadn’t been there. Maybe it’s because Pai Chen is a well-made Hunter from the Great Cataclysm.

└ Pai Chen’s parents have Hong Kong citizenship, so she’s Hong Kong-made.

└ Does the commenter above work in quality control or something? That was fucking clear.

└ While you’re at it, does anyone have news about the Korean Hunters?

└ Jung Dragon is in charge of the northern front and gaining the upper hand. I heard Sibeol-jwa won two or three times on the western front, but there’s been no news since, so I guess they’re holding the line.

└ Hmm… Nobody needs to worry about Lee Jungryong’s skills, but is Sibeol-jwa safe? He’s still an A-rank Hunter.

└ ?? LOL

└ LMAOOOOOOOOOO

└ There’s still an innocent idiot who treats Sibeol-jwa like an A-rank Hunter? As a current A-rank Hunter, all I can do is laugh. That Jin Taekyung guy is just a monster lol

Hey heyheyhey!! The U—N Security Council just announced the w—estern front situation!

└ Oh, Sibeol-jwa news. Been a while.

└ That sounds incredibly urgent. The western front? What are they saying?

└ They say it broke through?

└ Huh?

└ Huh?

└ What the hell does that mean? Don’t tell me Sibeol-jwa died…?

└ Wait. What is this actually saying? Guys, I’m going back to check it again. It’s on the main page, so go look for yourselves.

└ Ah. I’m suddenly fucking terrified. I’m checking it right now.

└ Go go go go go

The netizens who had been enthusiastically writing comments hurriedly accessed the United Nations Security Council website.

Because too many visitors had flooded the site at once, they had to wait for quite some time after hitting the traffic limit. At last, when they saw the announcement that had appeared on the main page, they could do nothing but doubt their own eyes and ears.

“…What the hell is that?”

The map displayed the standoff with the monster army. The front line formed an oval, but the western front had been gouged inward like an awl.

…I just checked. It really broke through.

└ Is Jin Taekyung dead? How bad are the casualties?

└ No, the monsters’ line was breached.

└ ??

└ ???

└ The breakthrough happened so fast that the updates couldn’t keep up.

└ …Does that even make sense?

└ Shut up and pull down the shutters. Today is the tavern lady’s death anniversary…[^1]

[^1]: Korean internet slang calls for a tavern lady to pour celebratory drinks when national pride surges; the joke is that today’s celebration will work her to death.

* * *

The battlefield where a fierce battle was about to erupt was chaotic. An endless wasteland stretched out before us, and countless monsters filled my field of vision.

A wind that blew in from somewhere carried the thick killing intent and stench pouring off the creatures.

“Fuck. They really gathered a lot.”

Team Leader Choi, standing beside me, answered my mutter.

“No matter how many we kill, they never end.”

It was the fourth day since we had been deployed to the western front and the full-scale battle had begun. The Team Leader Choi who had always looked immaculate was nowhere to be found.

Covered in blood and dust, he looked at me with a calm, somber gaze.

“When do we begin?”

“Who knows? We should hear what our little commander thinks first. Right?”

That last question was not directed at Team Leader Choi.

The twenty-one-year-old “little commander” who had not left my side the entire time answered. It was Shao Shen.

“I will follow Teacher Jin’s orders!”

A snort of laughter escaped me at the sparkle in his eyes.

“You’re still going on about calling me Teacher. You were the one who first told me to drop the formal speech. I told you to call me hyung instead.”

“Is it… Is it really all right if I do that?”

“I told you it was fine as long as you were okay with it. But can you really do this in front of your men? I heard you’re getting promoted to major general now.”

Shao Shen shook his head at lightning speed.

“There’s no problem at all! H-hyung-nim!”

He was frighteningly calm when fighting, so I had no idea why he stammered so much in ordinary situations.

I looked at the Hunters from the Public Security Armed Forces lined up behind him. There were more than a thousand of them.

Their heated eyes held admiration and awe for the strong.

Of course, Shao Shen stood out even among them.

“Give us your orders. H-hyung-nim.”

“An order.”

I suddenly looked up at the sky.

A huge eagle with its wings spread wide circled above our heads. I had a good feeling about today, too.

“Follow me. Just like you’ve done until now.”

“……!”

“Right now.”

I stepped forward as I answered.

Crack.

The force of ten thousand geun packed into my toe made the ground split like a spiderweb and cave inward.

And then, in the next moment—

Boom!

Accompanied by a deafening roar that left my ears ringing, I shot forward as a streak of light.

*Flamefire Path.*

The wind carrying the cold heated up and transformed into a blast of hot air.

As the ground, wind, and scenery streaked past, a tremendous roar erupted behind me.

“Charge! Charge!”

“Descendants of Zhonghua! People! Sweep every last one of them away!”

“Waaaaaaah!”

Thud-thud-thud-thud!

Kyaaaauuuuu!

Human battle cries and monster shrieks rang across heaven and earth. The immense vibrations shook the very ground.

At the threshold of that chaos, I swung the White Flame in my hand with all my strength.

Whoooosh!

The Extreme Yang force that surged from the spearhead sliced through everything standing in its way.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 389`.

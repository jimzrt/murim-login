# Master Edit Task — Chapter 385

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
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 사형     | **Senior Brother**                           |
| 선배     | **Senior**                                   |
| 칭호               | **Title**                      |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 대사      | **Master** for a senior Buddhist monk                           |
| 웨이펑후 | **Wei Penghu** | Senior General and Minister of Defense at the Central Military Commission. |
| 윌리엄 | **William** | Prince Felix's formal attendant. |
| 우헤이싱 | **Wu Heixing** | S-rank Hunter antagonistic toward Taekyung. |
| 시벌좌 | **Sibeol-jwa** | Taekyung's profane nickname, recognized by Shao Shen. |
| 국방부장 | **Minister of Defense** | Wei Penghu's office at the Central Military Commission. |
| 대마법사 | **Archmage** | Title held by only three people worldwide. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 웨이펑후 | 진태경 | senior_military_official_to_foreign_hero | Teacher Jin | respectful-formal | Wei Penghu uses 진 선생 when introducing himself and inviting Taekyung to the operations headquarters. |
| 우헤이싱 | 진태경 | hostile_peer | peninsula bangzi | abusive-hostile | Wu Heixing repeatedly addresses Taekyung with an anti-Korean slur. |
| 진태경 | 우헤이싱 | hostile_peer | mainland chink | abusive-hostile | Taekyung answers Wu Heixing's slur with an explicit anti-mainland insult. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |

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

#### Chapter 383 tail (verified mastered)

…
Hunter like that?* Wei Penghu had spoken indirectly, but the meaning behind his words was clear enough. Team Leader Choi and I locked eyes in midair. At that moment, we were thinking the same thing. *An undisclosed S-rank Hunter.* No. More precisely, an S-rank Hunter deliberately concealed by the Chinese government. *I’d only heard rumors about things like this. So it was true?* An S-rank Hunter was practically the face of a nation. But unlike the weak, who struggled desperately not to be looked down on, the strong hid their claws. China was already known to possess two S-rank Hunters. Clearly, it had not wanted to reveal all its strength. Perhaps the same was true of the world’s other great powers. *Seriously. Even after going through the Great Cataclysm, they’re still jockeying for advantage like this.* It was pathetic. At the same time, I could almost understand it. Diplomacy. Politics. I felt as though I’d caught a glimpse of the truth of a world I’d never understood, and it left me with a strange feeling. Unlike me, however, Team Leader Choi was much sharper. “When you say Lei Fei ‘was’ one of your country’s S-rank Hunters, that sounds like the past tense.” Wei Penghu answered with a grim expression. “…A week ago, when the first monster wave occurred, Lei Fei disappeared. Along with the Hunters from the Public Security Armed Forces under his command.” “Are you certain he’s missing? Could he perhaps…” “We have not confirmed his death. After that video, the monster called the Lich—no, the Arch Lich—used mana to cut off all communications and surveillance.” Team Leader Choi and I groaned at the same time. Hearing our reaction, Wei Penghu asked in a hoarse voice, “Do you two also think Lei Fei is dead?” “Hmm.” “Uh…” *Missing. And if someone had gone missing in that hell a week ago, the ending was practically a foregone conclusion.* At Team Leader Choi’s signal, I cautiously opened my mouth. “Well, you never know how things will turn out, but…” “Other experts said he was one hundred percent dead. Useless blowhards, every last one of them.” *What’s wrong with you? They sound like real experts.* If anyone guaranteed he was alive under those circumstances, they should be fired immediately. That was simply a fact. “But I disagree. Lei Fei—that boy must still be alive.” “I hope so too, but realistically speaking…” “He is my only nephew. My sister was sickly from childhood and died in childbirth. I raised that tiny, unweaned infant as if he were my own son.” “What?” *A nephew? You raised him as your own son? What the hell is this?* I froze like a statue. Wei Penghu looked at me with tear-filled eyes. “But what were you going to say? After ‘realistically speaking,’ I mean.” *Fuck. This is the biggest crisis I’ve ever faced.* The words caught in my throat. I barely managed to squeeze out a reply. “Well, realistically speaking, I was going to say that there’s still some chance he might be alive.” “Is that so? Is that true?” “Yes. But that chance is extremely slim…” “Thank you, Teacher Jin!” “No, General. Commander. Great Leader. Just hold on a second and let me finish—” Grab! It was too late. Wei Penghu was no longer listening. Instead, he clasped my hand in both of his, his eyes brimming with tears. “May I ask you for one favor?” *I wish you wouldn’t.* Despite my desperate hopes, the words I’d been dreading pierced my heart a few seconds later. “If you happen to meet that boy someday, would you bring him back to me?” “…” “I beg you.” Over his desperately pleading shoulder, I saw Team Leader Choi shaking his head. *What if I’d just given him a firm answer from the beginning?* I regretted it, but it was already too late. In the end, there was only one answer I could give. “I will. But…” “Teacher Jin.” “Yes?” “You don’t have to say it. I’m already prepared for that.” “…!” Wei Penghu wiped the corners of his eyes with his sleeve. He was no longer a middle-aged man worrying about the safety of his blood relative. He had returned to being the Minister of Defense at the Central Military Commission. “This is enough. No one was willing to step forward, but you promised me. I can rest easy now.” “I can’t guarantee anything.” “What I needed was not someone’s bombastic guarantee. It was a thread of hope.” Just as Wei Penghu murmured those words, the aircraft glided toward the ground with a weightless sensation. Outside the window, amid the deep darkness, I could see rugged mountain terrain, lights moving ceaselessly, and military vehicles. “It looks like we’ve arrived.” I had been staring fixedly out the window as though possessed by something. Now I asked, “Where are we?” “The temporary operations headquarters.” “No. That’s not what I asked.” “Hmm?” “The mountain. That mountain feels strangely familiar.” “That’s impossible. As far as I know, you have never entered our country before… Ah, perhaps you saw it in a photograph?” “A photograph?” “It is a UNESCO-designated World Cultural Heritage Site, so that is entirely possible.” With a faint smile, Wei Penghu continued, “The temporary operations headquarters. Welcome to Mount Qingcheng.” [^1]: *Sundae-guk* is a Korean soup made with sundae, a type of Korean blood sausage, and is commonly served with rice.

#### Chapter 384 tail (verified mastered)

…
full authority over the Central Military Commission?” Wei Penghu hesitated for a moment, then gave a heavy nod. “Yes.” “You would use that power well. But I will refuse.” “…Comrade Chairman?” “Bring me the written order once this meeting ends. I will assume full authority over everything—and bear all the responsibility myself.” For a moment, I wondered what had gotten into China’s Jongseok. Then I understood. He was declaring his intention to shoulder everything himself. Team Leader Choi muttered beside me as he watched the scene. “He’s a good leader.” I shook my head slightly. “No. To me, Team Leader Choi, you’re the best.” “Mr. Jin Taekyung…” “So please raise my Guild settlement percentage.” “Mr. Jin Taekyung…” Same words. Different feeling. Team Leader Choi looked at me as if to say, *Of course you’d say that, you bastard,* and shook his head. That was when it happened. “The Chairman is leaving.” At the secretary’s words, everyone who had been seated rose from their places. It was the minimum courtesy owed to a head of state. “I wish you all good fortune.” The Chairman met each person’s eyes and addressed them in turn. Of course, I was no exception. And as luck would have it, I was last. “Teacher Jin.” “…Yes.” A faint smile touched the corners of the Chairman’s mouth as he looked at me. “I have very high hopes for you, Teacher Jin. Though this is a contract in which we exchange what we each need, I hope that you will put human lives first in every situation.” Was it my imagination, or was his farewell unusually long compared to everyone else’s? Feeling everyone’s eyes on me, I nodded. “I understand.” “Please be a great source of strength to us.” The Chairman finished speaking and was about to turn away when he abruptly stopped. Then he tossed out one last remark. “Welcome.” “…” “Well, that will be all.” After the high-ranking Chinese officials who had been present to see the Chairman off disappeared, I dropped heavily into a chair. *Fuck.* If I died, the cause of death would be humiliation. Even if a monster killed me, I would make sure the official cause of death was listed as humiliation. *No! Nooooooo!* As I screamed inwardly in every direction, something pressed down firmly on my foot. Obviously, it was Team Leader Choi, seated beside me. “What?” Team Leader Choi gave a small cough. “Ahem.” “What?” “Ahem. People. People.” “Oh.” I looked around and finally realized that around a dozen men and women of different races were watching me inside the underground bunker. Four of them stood out in particular. *Those people are…* A Chinese man and woman. And two Western men, one tinged with green and the other with blue. I could feel it just from meeting their eyes—the immense power coiled inside their bodies. My first thought wasn’t that it was surprising, but that it was only natural. Anyone who knew the identities of those four would have thought the same thing. *S-rank Hunters.* People whose very existence was news. Those who stood at the pinnacle of the countless Hunters in the world. Faces I had seen until I was sick of them on television and in advertisements were now right in front of me. And now, one of them stood up and extended a hand toward me. “Nice to meet you. I’m… Ah, do you perhaps not speak English? I can cast translation magic if you’d like.” I hadn’t expected him to speak to me first. Still dazed, I took his hand and answered. “No, it’s fine.” “Oh, listen to this fellow’s pronunciation. I’d believe you if you told me you were American.” The middle-aged Black man was a giant well over two meters tall. His blue eyes gleamed as he asked, “You seem to know who I am. Don’t you?” As if I wouldn’t. I felt an even greater tremor than I had when facing Chairman Xiao Yang. “Of course, Magic Johnson.” Only three people in the entire world had been granted the Title of Archmage. The Black man standing before me, Magic Johnson, was a War Mage—the most combat-oriented of those three Archmages. *I’m actually talking to Magic Johnson. I guess you really do live to see all kinds of things.* As I thought that I had made the right choice in coming here, the world’s greatest War Mage smiled broadly and spoke to me. “Haha. I’m glad you recognized me. Actually, I’ve known about you for a while too.” “M-Me?” “Of course. Even my youngest daughter, who started elementary school this year, knows Sibeol-jwa.” “…” *Just how far has that damn nickname spread?* What would they call the nickname Sibeol-jwa in the English-speaking world? *Fuck Guy? Fuck Man?* The thought of Magic Johnson’s little youngest daughter knowing me by that name didn’t make me happy in the slightest. And apparently, I wasn’t the only one who disliked it. “What an utterly vulgar nickname. Though I suppose it suits a mere A-rank Hunter like you.” A relatively young Chinese man, perhaps around thirty, stared at me with his arms folded at an angle. “Isn’t that right, you peninsula bangzi?”[^1] Team Leader Choi didn’t even have time to stop me. My voice had already come out like an automatic response. “What are you saying, you mainland chink bastard?” [^1]: *Bangzi* is a derogatory Chinese slur for Koreans.

## Korean source

```text
＃385화



「안 그래, 반도의 빵즈?」

“뭐래, 대륙 짱개 새끼가.”

그 순간, 무거운 적막이 내려앉았다.

매직 존슨과 같은 외국인들은 통역 마법을 사용하면서도 빵즈와 짱깨가 정확히 무슨 의미인지 알아듣지 못해 어리둥절했고, 최 팀장은 작게 혀를 찼으며 한 사람의 얼굴은 돌처럼 딱딱하게 굳었다.

「뭐?」

“뭐, 인마.”

「다시 한번 지껄여 봐라, 빵즈.」

“응. 짱깨.”

「이런 개…….」

“좋아. 정리하자. 나는 개. 너는 짱깨.”

「……!」

놈의 얼굴이 와락 일그러지는 것이 보인다. 자리를 박차고 벌떡 일어나려는 놈을, 옆자리에 앉아 있던 여인이 손을 들어 제지했다.

「그만.」

청량음료처럼 깨끗한 분위기를 지닌 20대 초반의 미녀. 그녀의 입술 사이로 침착한 목소리가 이어졌다.

「부탁이니 적당히 해 줬으면 좋겠는데. 두 사람 모두.」

적당히라…….

잠시 여자를 바라보던 나는 어깨를 으쓱해 보였다.

“뭐, 원하신다면.”

뜻밖의 대답이었는지 그녀의 눈썹이 살짝 휘었다.

「언뜻 듣기로는 만만치 않은 성격이라던데, 생각보다 순순하게 받아들이네?」

“받아들여야죠. 다른 사람도 아니고 당신 부탁인데.”

「미인계에 걸려들었구나? 아, 이래서 예쁘면 피곤하다니까.」

능청스럽게 긴 머리를 쓸어올리는 그녀를 보자 피식 웃음이 나왔다.

“너, 지금 웃었니?”

「생각했던 것보다 재미있는 분 같네요. 파이 첸 씨는.」

파이 첸. 그녀의 이름이다.

대학교 표지 모델 같은 저 용모와 분위기에 속으면 안 된다. 결혼만 하지 않았을 뿐, 쉰 살을 훌쩍 넘긴 장년의 나이니까.

동시에 내게는 까마득한 대선배이자, 대격변의 영웅 중 한 사람이기도 했다.

「처음부터 알고 있었다 이거지. 흠, 요즘 애들은 나 모를 줄 알았는데.」

틀린 말은 아니다. 확실히 파이 첸은 다른 S급 헌터들에 비해 미디어에 노출되는 빈도가 매우 낮았다.

수면 아래에서는 신분을 세탁한 뒤 새로운 삶을 살고 있다는 소식도 심심찮게 들려올 정도였다.

하지만 나는 아주 어릴 때부터 그녀를 알고 있었다.

“저희 어머니가 오랜 팬이시거든요. 그 왜, 이십 년 전쯤에 개봉했던 로맨스 영화에 주연으로 나오셨었잖아요.”

「어머? 그게 도대체 언제 적 이야기니. 그래도 그걸 기억해 주는 사람을 만나니까 반갑네.」

“혹시 나중에 사인받으러 가도 됩니까? 어머니께 파이 첸 씨 사인 가져다드리면 좋아하실 것 같아서요.”

「물론이지. 그리고 앞으로는 그냥 첸 씨라고 해. 풀 네임은 너무 딱딱해 보이잖아. 더 편하게 누님이라고 불러도 되고.」

“예? 무슨 소리세요. 인터넷 검색해 보니까 첸 씨가 저희 어머니보다 다섯 살 많으시던데.”

「……만만치 않네. 듣던 대로.」

하지만 정말 만만치 않은 놈은 따로 있었다.

「이런 자라 좆 같은……!」

끓어오르는 목소리. 우리의 대화로 잠시 잊혔던 놈이 분노에 가득 찬 눈으로 나를 노려보았다.

「이 약소국 빵즈 놈이 감히 누구를 무시하는 거냐. 내가 어떤 사람인 줄 알고!」

“……와, 대사 존나 구려.”

우리를 번갈아 보던 파이 첸이 흥미로운 눈빛으로 턱을 괴었다.

「그러게. 아까부터 궁금했는데 너, 이 애가 누군지는 알고 이러는 거니?」

내 대답을 듣고 싶어 하는 사람은 파이 첸 뿐만 아니었다.

이제 반쯤 해탈한 표정의 최 팀장을 제외한 모두가 내 입만을 바라보고 있었다.

말싸움에서 진 일곱 살 어린애처럼 씨근덕거리는 놈과 미국의 대마법사 매직 존슨. 그리고 영국에서 온 청년까지. 그들을 따라온 수행원들도 예외는 아니었다.

모두의 시선 속에, 나는 고개를 끄덕였다.

「알긴 알죠. 우헤이싱.」

잦은 미디어 노출로는 S급 헌터 중에서도 1, 2위를 다투는 놈이니 모를 수가 없다.

내 대답에 아까부터 빵즈 운운하며 시비를 걸어온 놈, 우헤이싱이 눈을 부릅떴다.

「내가 누구인지 알면서도 그랬단 말이냐?」

“지나가던 개도 알걸? S급 헌터 중에 웬 인간 말종 새끼가 하나 있다는 것 정도는.”

「뭐, 뭐라고?」

“왜? 네 취미가 관심받기. 특기가 범죄 저지른 다음 언론 플레이 하기인 거 모르는 사람이 어디 있다고.”

「……!」

“그러고 보니까 너 이 새끼, 작년쯤에 사고 치지 않았냐? 나라가 내게 허락한 유일한 마약. 뭐 이 지랄 떨면서 공식 SNS에 레이드 한 사진 올리고 한 달 후에 진짜 마약 한 거 걸렸었잖아. 아마 대마초였나?”

“진태경 씨.”

“최 팀장님, 말리지 마세요.”

“대마초가 아닙니다.”

“예?”

불쑥 끼어든 최 팀장이 침착한 목소리로 태경 위키를 수정해 주었다.

“대마초가 아니라 코카인과 필로폰입니다.”

“아, 그랬구나. 알려 주셔서 감사합니다.”

“뭘요. 기왕 이렇게 된 거, 못 할 말이 뭐가 있겠습니까.”

해탈한 표정 보소.

이제는 모든 것을 내려놓고 우화등선(羽化登仙)을 준비 중인 최 팀장을 뒤로한 나는, 우헤이싱을 향해 활짝 웃으며 말을 이었다.

“크으, 어떻게 그런 복선을 깔 생각을 했냐. 이 새끼 최소 우헤이순원. 보랏빛 레이드.”

「뭐, 뭐라고?」

“생각해 보니까 또 있네. 5년 전에 버닝문인가 뭔가 하는 클럽에서 약 타서 성폭행 저지르다가 걸렸던 거. 그거 어떻게 무죄 받았냐? 중국 법으로 이 정도면 두세 번쯤 사형당했어도 이상하지 않은데.”

「……!」

“공산당 최고위층 아들이라는 소문은 들었는데. 돈이랑 권력으로 빠져나온 거야? 이 똑똑한 새끼 보게 이거.”

「주, 주둥이 닥치지 못해! 이 천민 출신 빵즈가 감히!」

얼굴이 시뻘겋게 달아오른 채 고함을 내지르는 우헤이싱의 모습에, 가만히 이 사태를 지켜보던 한 사람이 입을 열었다.

「시끄럽군.」

오만한 목소리가 물 흐르듯 이어졌다.

「경박스럽고 천박해. 듣자 하니 중국 귀족 집안의 핏줄 같은데, 가문의 어른들에게 예법 교육을 받지 못했나?」

목소리의 주인을 확인한 우헤이싱이 입술을 깨물었다.

「다, 당신은…….」

「당신?」

잘 정돈된 갈색 머리카락 아래, 은은한 초록빛 눈동자가 우헤이싱을 천천히 훑더니 떨어진다.

「윌리엄.」

청년의 부름에 뒤에 서 있던 반백의 장년인이 앞으로 나섰다.

먼지 한 톨 묻어 있지 않은 구두와 칼처럼 예리하게 다려진 정장. 우뚝 선 채 좌중을 둘러본 장년인의 입술 사이로 듣기 좋은 중저음이 흘러나왔다.

「케임브리지 공작, 스트래선 백작, 캐릭퍼거스 남작, 가터 훈장의 기사, 시슬 훈장의 기사이신 왕자 필릭스 알렉산더 루이 전하께 모두 일어나 예를 갖추십시오.」

케임브리지 공작이자 스트래선의 백…… 시벌, 뭔 칭호가 저렇게 길어.

어쨌건 필릭스 뭐시기 왕자가 준엄하게 한마디를 덧붙였다.

「다들 편하게 필릭스 왕자 전하라고 부르게.」

“…….”

“…….”

사람들 표정 좀 봐라. 세상에서 제일 불편해 보인다.

물론 그중에서도 가장 압권인 사람은 앞서 내게 천민 운운했던 우헤이싱이었다.

그도 그럴 게, 막상 신분으로 따지면 영국 왕족을 어떻게 이기겠나.

「그, 그러니까 이게…….」

「아하.」

당황하는 우헤이싱을 바라보던 필릭스 왕자가 이제 알았다는 듯 고개를 끄덕였다.

「그렇군. 말 더듬이인가?」

「마, 말더듬이?」

「아니라면 왜 말을 제대로 하지 못하는 거지? 가문에서 스피치 훈련을 받지 못했나?」

왕자 전하 만세.

굳이 직접 나설 필요도 없었다. 영국 왕위 계승 서열 3위가 주사기로 꽂아 주는 탄산에 십이지장까지 톡톡 튀는 기분이다.

입이 찢어질 듯이 웃고 있던 그때, 필릭스 왕자의 시선이 문득 나를 향했다.

「자네.」

“응? 나 말하는 겁니까?”

내 반문에 필릭스 왕자의 뒤에 서 있던 장년인이 입을 열었다.

「케임브리지 공작, 스트래선 백작, 캐릭퍼거스 남작, 가터 훈장의 기사, 시슬 훈장의 기사이신 왕자 필릭스 알렉산더 루이 전하께서 하문하실 때에는…….」

「그만하게. 윌리엄.」

손을 들어 앵무새의 입을 틀어막은 필릭스 왕자가 자애로운 눈빛으로 나를 응시했다.

「본인이 품위를 버리고 이렇게 직접 나선 것은, 평소 신분 격차를 타파해야 한다는 신념을 갖고 있기 때문이라네.」

“……?”

「천민이면 어떻고, 귀족이면 어떤가. 우리는 그저 신 아래 평등한 사람일 뿐인 것을. 그러니 저자의 말에 너무 상처받지 말게.」

아니, 이게 뭔 개소리야.

순간 할 말을 잃은 내게 최 팀장이 넌지시 속삭였다.

“진태경 씨를 천민이라고 생각하는 것 같습니다.”

“……!”

저 왕자 새끼가 미쳤나.

어이없는 표정으로 필릭스 왕자를 바라보는 내게, 천천히 자리에서 일어난 그가 당연하다는 듯한 얼굴로 손등을 내밀었다.

「자, 어서.」

“……어서라니. 이번에는 또 뭔데.”

비서인지 앵무새인지 모를 장년인이 흐뭇한 미소를 띤 채 입을 열었다.

「손등에 입을 맞춰, 필릭스 알렉산더 루이 전하께서 보여 주신 자애로움에 감사를 표하시면 됩니다.」

“…….”

이거 완전 또라이들 아냐.

‘단체로 타입 캡슐 타고 18세기에서 건너왔나, 이 18새기들이.’

잠시 머리가 띵해진 내 귓가에, 최 팀장이 보낸 메시지 마법이 닿았다.

- 안 됩니다.

나는 전음으로 응답했다.

- 뭐가 안 돼요.

- 어쨌든 안 됩니다. 그냥 웃으면서 넘어가십시오. 필릭스 왕자는 원래 좀 별종으로 유명하잖습니까.

- 지금 쟤 손등 부러트리면 더 유명해지지 않을까?

- 안 됩니다. 절대 안 됩니다!

- 손등 조금. 아니면 손가락 하나만이라도.

- 안 된다고!

메시지 마법에 이 정도의 감정이 담길 수 있다니. 최 팀장도 나름대로 절박한 모양이다.

그래, 영국 왕자니까 어쩔 수 없지. 내가 내심 화를 삭이던 그때였다.

「헤이, 시벌좌.」

이건 또 뭐야. 나는 불쑥 다가온 매직 존슨을 경계 어린 눈빛으로 바라봤다.

혐한, 각종 트러블로 유명한 우헤이싱은 애초에 기대부터 안 했지만, TV에서나 보던 S급 헌터들을 실물로 봤다는 기쁨은 서서히 바닥을 드러내고 있었다.

“……아니 제발. 시벌좌 말고 이름으로 부르세요. 제가 존슨을 좆슨이라고 부르면 좋겠어요?”

「음, 듣고 보니 그렇군. 그럼, 진(Jin)?」

“훨씬 낫네요. 그런데 왜요?”

「별건 아니고. 혹시 왕자의 손등에 키스할 생각이 없는 거야?」

충분히 별거 같은데.

어이가 없어진 나는 즉각 되물었다.

“당연하죠. 무슨 중세시대도 아니고. 존슨 같으면 하고 싶겠습니까?”

「난 하고 싶지.」

“예?”

순간 뇌리를 스치는 섬광 같은 깨달음.

깜빡 잊고 있었다. 매직 존슨은 미국의 국민 영웅이자 국민 게이라는 사실을.

타임지가 선정한 ‘세계에서 가장 영향력 있는 성소수자 1위’가 나를 향해 진지한 얼굴로 제안한다.

「그래서 말인데, 내가 진을 대신해서 왕자에게 감사를 표하고 싶어.」

“…….”

이걸 이렇게 포장해 버리네. 하지만 매직 존슨과는 달리 필릭스 왕자는 슬그머니 손등을 회수했다.

「신 아래 우리는 평등한 한 사람의 인간일 뿐. 이런 구닥다리 예법은 없어져야 해. 매직 존슨, 그대의 호의는 나중에 받기로 하지.」

“…….”

저게 조금 전까지만 해도 나한테 손등 내밀던 새끼가 할 말인가? 듣고 있던 파이 첸도 어처구니가 없는지 중얼거렸다.

「어머, 되게 뻔뻔하다. 범죄만 안 저질렀지, 우헤이싱 저 녀석보다 한 수 위일지도 몰라.」

“아무리 그래도 우헤이싱보다는 낫죠. 쟤는 법대로면 사형당했어야 할 놈인데.”

「그것도 그래.」

뒤이은 거물들의 등장에 쭈구리가 되어 있던 우헤이싱의 눈동자에서 불똥이 튀었다.

「이, 이, 이 빵즈 새끼가!」

“그놈의 빵즈 타령 그만하지. 애국가도 2절부터는 힘들다. 내가 너 봐주는 것도 마찬가지고.”

「……봐줘? 네놈 따위가 나를?」

도무지 이해가 가지 않는다는 말투에 내가 고개를 끄덕였다.

“어. 방금 확실해졌네.”

나는 우헤이싱이 어느 수준인지 짐작하고 있지만, 놈은 내가 어떤 사람인지 조금도 알아차리지 못했다.

싸움은 상대를 가늠하는 것부터 시작이다. 이 싸움은 시작하기도 전에 끝났다.

“그러니까 괜히 시비 걸지 말고 좋게 말할 때 가라. 각자 할 일이나 열심히 하자고.”

「A급 헌터 주제에 주석 동지의 기대를 받는다고 하늘 높은 줄 모르고 나대……!」

“아하.”

왜 초면부터 지랄을 떠나 싶었는데, 이거 때문이었구만. 너무 뻔하고 유치한 이유라 실소가 흘러나왔다.

“거 참. 이걸 귀엽다고 하기에는 나이를 너무 처먹었고.”

「……!」

“어떡하냐? 주석님의 기대와 주목을 한몸에 받고 싶은데, 웬 한국 놈한테 밀려서.”

「너…….」

속마음을 들켰다는 걸 깨달은 우헤이싱의 얼굴이 수치심과 분노로 달아올랐다.

어느새 모두의 이목이 쏠린 상황. 자신을 향한 사람들의 한심한 시선을 놈도 뼈저리게 느끼고 있을 것이다.

그리고 저런 부류의 놈들은 지금 같은 상황이 오면…….

‘꼭, 선을 넘기 마련이지.’

내 예상은 정확히 들어맞았다.

스윽.

검파를 향해 아주 미세하게 미끄러지는 녀석의 손끝.

대범한 샤오 양 주석은 신뢰의 증거로 이 자리의 누구에게도 무장 해제를 부탁하지 않았지만, 그의 배려는 우헤이싱에게 독이 될 것이다.

‘뽑아. 망설이지 말고.’

내가 아무리 막 나가는 것 같아도 최소한의 경우는 따진다.

지금까지는 주석의 요청으로 중국을 돕기 위해 왔으니 참았던 것뿐, 놈이 무기라도 뽑아 들면 적당한 선에서 조질 명분을 얻을 수 있다.

‘그래, 더. 더.’

마치 내게 조종이라도 당하는 것처럼, 우헤이싱의 손길이 검파를 잡아채려던 바로 그때.

저벅. 저벅.

조용하던 지하 벙커의 문밖, 복도에 울려 퍼지는 여러 명의 발걸음 소리.

우헤이싱의 손이 멈추고 굳게 닫혀 있던 문이 열린 것은, 거의 동시에 벌어진 일이었다.

그리고 국방부장 웨이펑후와 함께 등장한 한 사람을 발견한 순간, 내 뇌리에서 우헤이싱의 존재를 깨끗하게 잊혔다.

“내가 너무 늦었군. 많이들 기다렸나?”

붓으로 그린 듯한 굵은 이목구비와 옷으로도 숨길 수 없는 단단한 체구.

이제 고작 40대 초반인 중년인의 모습을 하고 있지만, 가죽 안에 숨은 것은 늙은 호랑이요, 교활한 뱀이다.

‘이정룡.’

나와 눈이 마주친 이정룡의 입가에, 진한 웃음이 맺혔다.
```

## Current accepted English baseline

```markdown
# Chapter 385

“Isn’t that right, you peninsula bangzi?”[^1]

“What are you saying, you mainland chink bastard?”

A heavy silence descended.

Even while using translation magic, the foreigners like Magic Johnson looked bewildered because they didn’t understand exactly what *bangzi* and *chink* meant. Team Leader Choi clicked his tongue softly, while one man’s face hardened like stone.

“What?”

“What, asshole?”

“Say that again, bangzi.”

“Yeah. Chink.”

“You fucking—”

“Fine. Let’s get this straight. I’m a dog. You’re a chink.”

“……!”

I watched his face twist violently. Just as he was about to shove back his chair and leap to his feet, the woman sitting beside him raised a hand to stop him.

“Enough.”

She was a beautiful woman in her early twenties, with an atmosphere as clean and refreshing as a soft drink. A calm voice continued from between her lips.

“I’d appreciate it if you both toned it down.”

*Stop, huh…*

I stared at her for a moment, then shrugged.

“Sure, if you insist.”

Perhaps my unexpected answer had caught her off guard. Her eyebrows curved slightly.

“I heard you weren’t the sort of person who was easy to deal with, but you’re accepting it more readily than I expected.”

“I have to accept it. It’s your request, after all.”

“You fell for the beauty trap? Ah, this is why being pretty is such a hassle.”

When she nonchalantly swept back her long hair, I let out a quiet laugh.

“Did you just laugh?”

“You seem more interesting than I expected, Ms. Pai Chen.”

Pai Chen. That was her name.

I couldn’t let myself be fooled by the looks and atmosphere of someone who could have been a university cover model. She might not have married, but she was well past fifty.

At the same time, she was an impossibly senior Senior to me—and one of the heroes of the Great Cataclysm.

“So you knew from the beginning. Hmm. I thought kids these days might not know me.”

That wasn’t wrong. Compared to other S-rank Hunters, Pai Chen had definitely appeared in the media far less often.

Behind the scenes, it wasn’t uncommon to hear that she had assumed a new identity and begun a new life.

But I had known about her since I was very young.

“My mother’s been a fan of yours for years. You starred in that romance movie that came out about twenty years ago, didn’t you?”

“Oh my? When was that? Still, it’s nice to meet someone who remembers.”

“Would it be all right if I came to get your autograph sometime? I think my mother would love it if I brought her one from you.”

“Of course. And from now on, just call me Chen. Your full name sounds too stiff. You can call me *older sister* if you want to be more casual.”

“Excuse me? What are you talking about? I searched online, and it says you’re five years older than my mother.”

“……You really aren’t easy to deal with. Just as I heard.”

But there was someone else who was truly not easy to deal with.

“You fucking turtle-dick…!”

His voice boiled over. The man who had briefly been forgotten amid our conversation glared at me with furious eyes.

“How dare a weak-country bangzi look down on me? Do you even know who I am?”

“……Wow. That’s a really shitty line.”

Pai Chen rested her chin on her hand, looking back and forth between us with interest.

“Indeed. I’ve been wondering since earlier—do you even know who this young man is?”

Pai Chen wasn’t the only one who wanted to hear my answer.

Everyone except Team Leader Choi, whose face had taken on an expression of near enlightenment, was staring at my mouth.

The man huffing and puffing like a seven-year-old who had lost an argument, Magic Johnson, America’s Archmage, and even the young man from Britain. Their attendants were no exception.

Under everyone’s gaze, I nodded.

“Of course I know. Wu Heixing.”

He ranked first or second even among S-rank Hunters when it came to media exposure, so there was no way I wouldn’t know him.

At my answer, the man who had been picking a fight with me about bangzi since earlier—Wu Heixing—widened his eyes.

“You knew who I was, and you still acted that way?”

“Even a stray dog passing by would know there’s one complete piece of human trash among the S-rank Hunters.”

“W-What did you say?”

“Why? You didn’t know that your hobby is getting attention and your specialty is committing crimes, then working the media afterward?”

“……!”

“Come to think of it, didn’t you cause trouble last year? You uploaded a raid photo on your official social media with some bullshit about ‘the only drug my country allows me.’ Then a month later, you got caught taking actual drugs. Was it marijuana?”

“Mr. Jin Taekyung.”

“Team Leader Choi, don’t stop me.”

“It wasn’t marijuana.”

“Huh?”

Team Leader Choi cut in abruptly and calmly corrected the Taekyung Wiki.

“It was cocaine and methamphetamine.”

“Oh. I see. Thank you for letting me know.”

“You’re welcome. Now that things have come this far, is there anything left that can’t be said?”

Look at that expression of enlightenment.

Leaving Team Leader Choi behind as he seemed to be giving up on everything and preparing to ascend to immortality, I continued speaking to Wu Heixing with a broad smile.

“Damn, how did you think of setting up foreshadowing like that? This bastard is Wu Heisunwon at minimum. *Purple Raid.*”

“W-What did you say?”

“Come to think of it, there’s another one. Five years ago, you got caught sexually assaulting someone after drugging them at some club called Burning Moon. How did you get acquitted? Under Chinese law, for something like that, it wouldn’t have been strange if you’d been executed two or three times.”

“……!”

“I heard rumors that you’re the son of someone in the Communist Party’s highest ranks. Did you buy your way out with money and power? What a clever little bastard.”

“Sh-Shut your mouth! How dare a bangzi from a lowly background speak to me like that!”

Wu Heixing’s face flushed bright red as he shouted. Then someone who had been quietly watching the entire situation opened his mouth.

“You’re being loud.”

An arrogant voice flowed smoothly through the room.

“You’re frivolous and vulgar. I hear you’re descended from a Chinese aristocratic family, but did the elders of your household never teach you proper etiquette?”

Wu Heixing bit his lip when he recognized the owner of the voice.

“Y-You’re……”

“You’re?”

Beneath neatly groomed brown hair, faintly green eyes slowly swept over Wu Heixing before moving away.

“William.”

At the young man’s call, a middle-aged man with half-gray hair stepped forward from behind him.

His shoes were spotless, and his suit had been pressed as sharply as a blade. Standing tall as he surveyed the room, the middle-aged man spoke in a pleasingly deep voice.

“Everyone, rise and pay your respects to His Royal Highness Prince Felix Alexander Louis, Duke of Cambridge, Earl of Strathearn, Baron Carrickfergus, Knight of the Garter, and Knight of the Thistle.”

*The Duke of Cambridge and the Earl of Strathearn… Fuck, why does he have so many titles?*

Whatever the case, Prince Felix-whatever added one stern remark.

“Everyone, just call me His Royal Highness Prince Felix.”

“……”

“……”

Look at everyone’s faces. They looked more uncomfortable than anyone else in the world.

Of course, the most spectacular reaction belonged to Wu Heixing, who had just called me a lowborn commoner.

And that was only natural. When it came to social status, how could he possibly beat a member of the British royal family?

“S-So, this is…”

“Ah.”

Prince Felix looked at the flustered Wu Heixing and nodded as if he had just understood.

“I see. Are you a stutterer?”

“A st-stutterer?”

“If not, why can’t you speak properly? Did your family fail to provide you with speech training?”

Long live His Royal Highness the Prince.

I didn’t even have to step in myself. The third in line to the British throne was injecting carbonation straight into me, and I could feel it fizzing all the way down to my duodenum.

I was grinning so hard my mouth felt ready to split open when Prince Felix’s gaze suddenly turned toward me.

“You.”

“Hm? Are you talking to me?”

At my question, the middle-aged man standing behind Prince Felix opened his mouth.

“When His Royal Highness Prince Felix Alexander Louis, Duke of Cambridge, Earl of Strathearn, Baron Carrickfergus, Knight of the Garter, and Knight of the Thistle, addresses you—”

“That will do, William.”

Prince Felix raised a hand and cut off the parrot. Then he gazed at me with benevolent eyes.

“I have personally stepped forward like this, abandoning my dignity, because I have always believed that we must overcome the divisions between social classes.”

“……?”

“What does it matter whether one is a commoner or a noble? We are all simply equal people beneath God. So don’t take that man’s words too much to heart.”

*What the fuck was this supposed to mean?*

I was momentarily at a loss for words when Team Leader Choi whispered discreetly.

“I believe he thinks you’re a commoner.”

“……!”

*Is that prince bastard insane?*

As I stared at Prince Felix with an incredulous expression, he slowly rose from his seat and extended the back of his hand toward me as if it were the most natural thing in the world.

“Well, come along.”

“……Come along? What is it this time?”

The middle-aged man—whether he was a secretary or a parrot, I couldn’t tell—spoke with a pleased smile.

“Kiss the back of his hand and express your gratitude for the benevolence His Royal Highness Prince Felix Alexander Louis has shown you.”

“……”

*Are these people complete lunatics?*

*Did these eighteenth-century fuckers all arrive here in a time capsule?*

Just as my head began to throb, a message spell from Team Leader Choi reached my ear.

- No.

I replied through Sound Transmission.

- What do you mean, no?

- In any case, no. Just smile and let it pass. Prince Felix is famous for being a bit of an oddball.

- If I break the back of his hand right now, wouldn’t he become even more famous?

- No. Absolutely not!

- Just the back of his hand. Or maybe one finger.

- I said no!

I hadn’t known Message Magic could carry this much emotion. Team Leader Choi must have been desperate in his own way.

*Fine. He’s a British prince. It can’t be helped.*

I was trying to swallow my anger when—

“Hey, Sibeol-jwa.”

*What now?*

I looked warily at Magic Johnson, who had suddenly approached me.

I hadn’t expected much from Wu Heixing, who was famous for his anti-Korean sentiment and various scandals in the first place. But the joy of seeing the S-rank Hunters I had only watched on television was gradually running out.

“……No, please. Call me by my name instead of Sibeol-jwa. Would you like it if I called you Fuckson instead of Johnson?”

“Hmm. Now that you mention it, I see your point. Then, Jin?”

“That’s much better. But why?”

“It’s nothing special. You’re not thinking of kissing the prince’s hand, are you?”

*That sounds pretty special to me.*

Taken aback, I immediately asked,

“Of course not. What is this, the Middle Ages? Would you want to if you were me, Johnson?”

“I would.”

“What?”

A flash of enlightenment struck my mind.

I had completely forgotten. Magic Johnson was an American national hero—and the nation’s gay icon.

Time magazine’s pick for *the world’s most influential LGBT person* was now making a serious proposition to me.

“So, I was thinking I’d like to thank the prince on your behalf.”

“……”

What a way to dress it up.

But unlike Magic Johnson, Prince Felix quietly withdrew his hand.

“We are all equal human beings beneath God. This antiquated etiquette must disappear. Magic Johnson, I will accept your kind offer at a later time.”

“……”

*Was that really something the bastard who had just held out his hand to me could say?*

Pai Chen had been listening too. Apparently unable to believe it, she muttered,

“Oh my. He’s shameless. He may be one step above Wu Heixing, despite not having committed any crimes.”

“Even so, he’s still better than Wu Heixing. That one should have been executed under the law.”

“That’s true.”

Spark flew from Wu Heixing’s eyes as he shrank beneath the arrival of one powerful figure after another.

“Th-this, this, this bangzi bastard!”

“Enough with the bangzi routine. Even the national anthem gets hard to get through after the second verse. Me going easy on you is the same.”

“……Going easy on me? You? On me?”

His tone made it clear that he genuinely couldn’t understand. I nodded.

“Yeah. It just became obvious.”

I had a pretty good idea what level Wu Heixing was at, but he hadn’t realized in the slightest who I was.

A fight began with gauging one’s opponent. This fight had ended before it even began.

“So stop picking fights for no reason and leave while I’m still asking nicely. Let’s each focus on doing our own jobs.”

“You’re just an A-rank Hunter, but because Comrade Chairman expects great things from you, you’ve forgotten your place and started running wild—!”

“Ah.”

I’d wondered why he had been acting like an asshole from the moment we met. So that was what this was about.

The reason was so obvious and childish that a dry laugh escaped me.

“Still, calling it cute would be a stretch. You’re too damn old.”

“……!”

“What are you going to do? You want all of the Chairman’s expectations and attention for yourself, but some Korean guy has edged you out.”

“You……”

Wu Heixing’s face flushed with shame and fury as he realized I had seen through his thoughts.

By then, everyone’s attention had gathered on us. He must have been keenly feeling the contemptuous looks everyone was giving him.

And people like him always crossed the line when put in a situation like this.

*They always do.*

My prediction was exactly right.

A faint movement.

His fingertips slid almost imperceptibly toward the hilt of his sword.

The magnanimous Chairman Xiao Yang hadn’t asked anyone present to disarm as a sign of trust, but that consideration would be poison to Wu Heixing.

*Draw it. Don’t hesitate.*

No matter how reckless I might seem, I still weighed the circumstances at least a little.

I had held back until now only because I had come to help China at the Chairman’s request. If Wu Heixing drew a weapon, I would have grounds to rough him up within reason.

*That’s it. A little more.*

As if he were being controlled by me, Wu Heixing’s hand reached for the hilt. Just as he was about to seize it—

Thud. Thud.

Several sets of footsteps echoed through the hallway outside the quiet underground bunker.

Wu Heixing’s hand stopped, and the tightly shut door opened at almost the exact same moment.

The instant I saw the person who entered alongside Minister of Defense Wei Penghu, I completely forgot that Wu Heixing even existed.

“I’m too late. Have you all been waiting long?”

Bold features that looked as though they had been painted with a brush, and a solid build that even his clothes couldn’t conceal.

He looked like a middle-aged man barely into his forties, but hidden beneath that skin were an old tiger and a cunning snake.

*Lee Jungryong.*

When Lee Jungryong’s eyes met mine, a deep smile formed at the corners of his mouth.

[^1]: *Bangzi* is a derogatory Chinese slur for Koreans.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 385`.

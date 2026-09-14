# Master Edit Task — Chapter 391

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
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 탱커      | **tank**              |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 쓰촨성 | **Sichuan Province** | Province containing Chengdu International Airport. |
| 중화 | **Zhonghua** | Term used in Shao Shen's rallying cry for China. |
| 데스나이트 | **Death Knight** | Powerful undead being the three beings plan but fail to create. |
| 상장 | **Senior General** | Wei Penghu's military rank, explained as four-star. |
| 태자당 | **Princelings** | The Communist Party's largest faction; Liao belongs to it. |
| 쑤이닝시 | **Suining City** | City near the devastated town attacked by the Death Knights. |
| 사르 | **Sar** | First component of the black knight's demon-realm command. |
| 가로쉬 | **Garosh** | Second component of the black knight's demon-realm command. |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 당장은 | polysemy | Right away / for now / at the moment; not the broader “anytime soon.” | anytime soon |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 385–389

## Plot

Jin Taekyung clashes verbally with Wu Heixing, an arrogant S-rank Hunter whose anti-Korean slurs and jealousy escalate the tension. Pai Chen intervenes, while Taekyung publicly mocks Wu’s drug and sexual-assault scandals. Prince Felix Alexander Louis further irritates the group with his elaborate royal etiquette and condescending treatment of commoners. Wei Penghu then arrives with Lee Jungryong, whose presence immediately draws Taekyung’s attention.

Lee recognizes that Choi Minwoo has grown dramatically and that Taekyung has crossed the wall. During the ensuing strategy meeting, Senior General Liao proposes using nuclear weapons against the Sichuan monster wave, but Wei Penghu rejects the plan because of the danger to survivors, the land, and possible magical teleportation. Six S-rank Hunters are assigned to separate fronts, each supported by military divisions and Public Security Armed Forces Hunters. An unidentified person contacts Taekyung through Sound Transmission.

The sender is Wu Heixing, who lures Taekyung into a forest and attacks him with a sword and martial-arts techniques. Taekyung decisively defeats him, takes his Supreme Potion as compensation, and gives him an Advanced Potion. Meanwhile, Team Leader Choi, Pai Chen, and Magic Johnson prepare to deploy; Choi agrees to a nine-to-one settlement split after Taekyung rescued him from their drinking-game predicament. Lee later approaches Wu in the darkness to request a private discussion, but its subject is not revealed.

An Unexpected Quest, **The Battle Situation Has Become Critical**, orders Taekyung to reach the battlefield quickly and defeat the enemies. Felix departs before dawn after receiving a battle signal. Chairman Xiao Yang announces the disaster to the United Nations Security Council, and China remains under martial law as UN-approved peacekeeping forces join the fighting.

Four days into the full-scale battle, the monster army has exceeded 100,000, communications and satellite surveillance remain disrupted, and the western front is breached by a rapid monster advance. Taekyung, Choi, and Shao Shen remain deployed there. Shao Shen commands more than a thousand Public Security Armed Forces Hunters and, after receiving permission, addresses Taekyung as hyung-nim. Taekyung leads the countercharge with Flamefire Path, White Flame, and Extreme Yang force.

## Continuity

- Jin Taekyung is a Supreme Peak martial artist who has crossed the wall. His exact Level, Fame, complete Titles, martial-art stages, and unassigned points remain unstated.
- Taekyung is cooperating with China to stop the Sichuan disaster and locate Lei Fei and the missing Sichuan Hunters.
- The six S-rank Hunters were assigned to six fronts, with three Army and Air Force divisions and Public Security Armed Forces Hunters attached to each.
- China is under martial law, and UN-approved peacekeeping forces are fighting on the front.
- The monster army exceeds 100,000, is centered around an Arch Lich, and is supported by magical interference that disrupts communications and satellite surveillance.
- The east-west front was breached, but Pai Chen prevented the damage from spreading. The western-front breach is a monster advance through the enemy line, not the collapse of Taekyung’s position.
- Taekyung and Team Leader Choi have fought on the western front for four days of full-scale battle.
- Shao Shen is twenty-one, commands more than a thousand Public Security Armed Forces Hunters, follows Taekyung’s battlefield orders, and now calls him hyung-nim.
- Wei Penghu remains Senior General and Minister of Defense at the Central Military Commission. He raised his missing nephew Lei Fei as his son.
- Xiao Yang remains Chairman of the Central Military Commission, General Secretary, and state chairman of China, retaining overall authority over the crisis.
- Lee Jungryong leads Ares Guild in practice and is one of the world’s three strongest S-rank Hunters. He recognizes Choi Minwoo’s growth and Taekyung’s breakthrough.
- Wu Heixing is an S-rank Hunter from a powerful Communist Party family. He is arrogant, volatile, status-conscious, and considers the missing Lei Fei an insurmountable rival.
- Wu knows Sound Transmission and martial arts. Taekyung defeated him after Wu initiated the attack, taking his Supreme Potion and leaving him with an Advanced Potion.
- Pai Chen is an S-rank Hunter, Great Cataclysm hero, and former romance-film actress who appears far younger than her actual age.
- Magic Johnson is an S-rank Hunter, one of the world’s three Archmages, and a combat-specialized War Mage.
- Prince Felix Alexander Louis is third in line to the British throne and holds multiple senior British titles; William is his formal attendant.
- The subject and consequences of Lee Jungryong’s private discussion with Wu Heixing remain unresolved.
- Lei Fei’s fate, the missing Sichuan Hunters’ fate, the western-front battle’s outcome, Wu’s reason for contacting Taekyung, and the monster wave’s larger plan remain unresolved.
- The Arch Lich’s identity, its relationship to the earlier Lich, the reason for the mana surge, and the full extent of the Skeleton Warlord’s increased power remain unresolved.
- Dark Heaven, the hidden transport formation, the Sichuan Tang Clan’s relocation, Mungyeong’s response, Dongbong’s request, Ae-hyang’s superior, and the Chengdu port boy remain unresolved.

## Translation Decisions

- Preserve **Jin Taekyung**, **Team Leader Choi**, **Lee Jungryong**, **Lei Fei**, **Wei Penghu**, **Pai Chen**, **Wu Heixing**, **Shao Shen**, **Magic Johnson**, **Prince Felix Alexander Louis**, and **William**.
- Render **전음** as **Sound Transmission**, **검강** as **Sword Force**, **상급 포션** as **Advanced Potion**, and **최상급 포션** as **Supreme Potion**.
- Render **다급해진 전황** as **The Battle Situation Has Become Critical** and **유엔 안전보장이사회** as **United Nations Security Council**.
- Render **대마법사** as **Archmage** and **워 메이지** as **War Mage**.
- Retain **hyung-nim** for Shao Shen’s address to Taekyung, **Sibeol-jwa**, **Flamefire Path**, **White Flame**, and **Extreme Yang**.
- Preserve the established **bangzi** footnote and the source’s offensive insult exchange, conversational self-mockery, drinking-game wordplay, and Felix’s ceremonial satire.

### Prior accepted reading-copy tails

#### Chapter 389 tail (verified mastered)

…
three times on the western front, but there’s been no news since, so I guess they’re holding the line. └ Hmm… Everyone knows how strong Lee Jungryong is, so I’m not worried about him. But is Sibeol-jwa going to be all right? He’s still an A-rank Hunter. └ ?? LOL └ LMAOOOOOOOOOO └ There’s still an innocent idiot who treats Sibeol-jwa like an A-rank Hunter? As an active A-rank Hunter myself, all I can do is laugh. That Jin Taekyung guy is just a monster lol Hey heyheyhey!! The S—Security Council just posted an update on the w—western front! └ Oh, Sibeol-jwa news. Been a while. └ That sounds incredibly urgent. The western front? What are they saying? └ They say it was breached? └ Huh? └ Huh? └ What the hell does that mean? Don’t tell me Sibeol-jwa died…? └ Wait. What is this actually saying? Guys, I’m going back to check it again. It’s on the main page, so go look for yourselves. └ Ah. I’m suddenly fucking terrified. I’m checking it right now. └ Go go go go go The netizens who had been excitedly writing comments rushed to the United Nations Security Council website. So many users flooded the site at once that it exceeded its traffic limit, forcing them to wait for quite some time. When they finally saw the announcement on the main page, they could only doubt their own eyes and ears. “…What the hell is that?” The map displayed the standoff with the monster army. The front line formed an oval, but the western front had been gouged inward like an awl. …I just checked. It really was breached. └ Is Jin Taekyung dead? How bad are the casualties? └ No, the monsters’ line was breached. └ ?? └ ??? └ The breakthrough was so fast that the updates couldn’t keep up. └ …Does that even make sense? └ Shut up and pull down the shutters. Today is the tavern lady’s death anniversary…[^1] * * * The battlefield where a fierce battle was about to erupt was crowded. An endless wasteland stretched out before us, and countless monsters filled my field of vision. A wind that blew in from somewhere carried the thick killing intent and stench pouring off the creatures. “Fucking hell. There sure are a lot of them.” Team Leader Choi, standing beside me, answered my mutter. “No matter how many we kill, there’s no end to them.” It was the fourth day since we had been deployed to the western front and the fighting had begun in earnest. There was no trace left of the Team Leader Choi who had always looked immaculate. Covered in blood and dust, he looked at me with a calm, somber gaze. “When do we begin?” “Who knows? We should hear what our little commander thinks first. Right?” That last question wasn’t directed at Team Leader Choi. The twenty-one-year-old “little commander” who had not left my side the entire time answered. It was Shao Shen. “I will follow Teacher Jin’s orders!” A snort of laughter escaped me at the sparkle in his eyes. “You’re still going on about calling me Teacher. You were the one who told me to speak casually to you first. I said you might as well call me hyung.” “Is it… Is it really all right if I do that?” “I told you it was fine as long as you were okay with it. But can you really act like this in front of your men? I heard you’re about to be promoted to major general.” Shao Shen shook his head at lightning speed. “There’s no problem at all! H-h-hyung-nim!” He was frighteningly calm in battle, so I had no idea why he stammered so much the rest of the time. I looked at the Hunters from the Public Security Armed Forces lined up behind him. There were more than a thousand of them. Their heated eyes held admiration and awe for the strong. Of course, Shao Shen stood out even among them. “Give us your orders. H-hyung-nim.” “Orders, huh?” I suddenly looked up at the sky. A huge eagle with its wings spread wide circled above our heads. I had a good feeling about today, too. “Follow me. Just like you’ve done until now.” “…!” “Right now.” With that answer, I stepped forward. Crack. The force of ten thousand geun concentrated in the tip of my foot split the ground like a spiderweb and drove it inward. And then, in the next moment— Boom! With a deafening roar that left my ears ringing, I shot forward as a streak of light. *Flamefire Path.* The wind carrying the cold heated up and transformed into a blast of hot air. As the ground, wind, and scenery streaked past, a tremendous roar erupted behind me. “Charge! Charge!” “Descendants of Zhonghua! People! Sweep every last one of them away!” “Waaaaaaah!” Thud-thud-thud-thud! Kyaaaauuuuu! Human battle cries and monster shrieks rang across heaven and earth. The immense vibrations shook the very ground. At the threshold of that chaos, I swung the White Flame in my hand with all my strength. Whoooosh! The Extreme Yang force that surged from the spearhead sliced through everything standing in its way. [^1]: Korean internet slang calls for a tavern lady to pour celebratory drinks whenever national pride surges; the joke is that today’s celebration will work her to death.

#### Chapter 390 tail (verified mastered)

…
vehicle bounced up and down as it raced along the ruined road. Through the window of the military vehicle I was sitting in, I began to see ruined rice paddies and fields, along with collapsed houses scattered here and there. After the cleanup was finished, I—or rather, *we*—were heading toward a nearby small city. “Ha-ha! You’ve really worked hard, Teacher Jin!” A belly even a tightly cinched belt couldn’t hide. A bald crown gleaming beneath the sun. If not for the military uniform he wore and the three stars on his shoulder strap, I would never have had any reason to meet the middle-aged man in front of me. “I contacted the higher-ups this morning, as it happens. The entire world, not to mention the United Nations Security Council, is in an uproar over Teacher Jin’s victory report! I don’t know what they mean, but apparently people in Korea are calling today Jumo’s death anniversary…”[^1] I had reached my limit for listening to his nonstop stream of nonsense. Unable to hold back any longer, I cut in. “I don’t care whether Jumo is dead or alive. Can I ask you one thing?” “Te-Teacher Jin?” Under China’s official military structure, this was the Chengdu Military Region. More specifically, the man before me was Senior General Liao, commander-in-chief of the Thirteenth Group Army, which included seven divisions and brigades. He looked at me anxiously. “Why, why are you acting like this? Did something happen?” “I heard something strange today, so I’m a little on edge.” “Who dared upset Teacher Jin? Ask me anything.” “Ah, yes. What I wanted to ask was…” I stared at Senior General Liao’s greasy, glistening face and continued. “I heard that some officers are extremely dissatisfied because they want to earn merit. Did you know about that?” “Ahem.” So he knew. He had known and done nothing. It was so absurd that I had gone beyond anger and come out numb on the other side. Still, he was technically an ally and a three-star general from another country. I kept my tone as calm and polite as possible. “Could I see the faces of those fucking bastards?” “Ahem!” “What kind of lunatics throw a fit about earning merit at a time like this? It’s not like they’ll be fighting themselves. They’ll put ordinary soldiers out front and wave their command batons from the rear, won’t they?” “Ahem! Ahem!” “What the fuck do they mean, they’re tired of cleaning up monster corpses? What, have they seen so many that they’ve grown fond of them and want to become corpses too? Do they need to actually die before they come to their senses? Fucking assholes.” “Ahem! Ahem! Ahem!” “If there are any bastards like that, tell them to come see me. I’ll gear them up and put them in the vanguard. They’d make perfect meat shields—” I suddenly shut my mouth. Cold sweat was pouring from Senior General Liao’s forehead like water from a sprinkler. “…” “…” This man was one of those lunatics too. I’d suspected he was no ordinary madman ever since he’d kicked up that whole goddamn fuss in an underground bunker over whether or not to launch a nuke. But he was clearly insane on an entirely different level. “General, are you out of your mind?” “Well, that is… We also have to show them something. We have to prove that we can do something too…” “We haven’t lost anyone, and everything’s moving forward smoothly—what more do you want to show them? The Hunters are breaking through the path ahead, while the army is cleaning up behind them and rescuing civilians. We’re doing a good job. What else do you want to show?” Crack. I cracked my knuckles. Senior General Liao hurriedly waved his hands. “Now, now! Let’s not speak informally to each other. Whether you consider my age or my rank, I’m not someone who should be treated this way by Teacher Jin.” “How about I give your skull the serving-bowl treatment and crack it wide open?” “Wh-What?” “Nothing. You misheard me. Anyway, I understand. Don’t get any foolish ideas. From now on, let’s advance slowly, minimize casualties, and rescue civilians. Understood?” “…” What was wrong with this man’s reaction? The moment I saw Senior General Liao’s eyes darting about instead of answering, a chill ran down my spine. *No way…* “Have you already issued an order?” “Well, I’m also implicated in a military procurement corruption case, and it’s time for me to accomplish something independently…” “You fucking bastard!” Bang! My kick tore the armored door off its hinges. The driver sitting in the front seat hurriedly slammed on the brakes. Screech! “Eek!” Senior General Liao curled into himself, trembling as he stammered out an answer. “I-I thought there might be monsters in the small city we’re heading toward, so I deployed some of the Public Security Armed Forces Hunters we were holding in reserve…” I didn’t need to hear any more. Before I could press him further, a roar rang out from the city that had suddenly drawn close. Boom! A massive explosion. Flames and smoke surged into the sky. And then— Ding. A System notification announced an Unexpected Quest. [^1]: *Jumo* is a traditional tavern keeper. Koreans jokingly call for her to serve drinks online when celebrating a national triumph; calling it her death anniversary means the celebration has worked her to death.

## Korean source

```text
＃391화



후위에 남아 있던 쓰촨성 공안 무력부 2중대장, 장 웨이는 처음부터 이 작전이 꺼림칙했다.

‘군대와 함께 먼저 가서 도시를 점령하라니? 샤오 연대장이 내린 명령과는 다른데.’

장 웨이가 품고 있던 한 줄기 의문이 더욱 커진 것은, 굳이 앞에서 교전 중인 아군을 우회하여 진격했을 때부터였다.

「왕 상교(上校)님. 이 작전, 저희 연대장님께서 동의하신 게 확실합니까?」

장 웨이의 물음에 중년의 고위 장교가 눈살을 찌푸리며 대답했다.

「왜 그런 게 궁금하지?」

「아무리 생각해도 이상해서 말입니다. 분명히 저희 연대장님께서는 후위에서 체력을 비축하며 본부를 호위하라고 하셨는데…….」

「아, 그 꼬마 연대장 말이지.」

샤오 쉔을 향한 고위 장교의 비웃음에 장 웨이가 얼굴을 굳혔다.

「샤오 쉔 연대장은 왕 상교님과 같은 계급입니다. 그것도 곧 소장 진급을 앞두고 계신.」

「세상 물정 모르는 어린 애가 운이 좋았던 게지. A급 헌터로 각성한 것으로도 모자라, 한국 놈이 활약해 준 덕분에 덩달아 이번 진급 명단에도 올랐으니. 이렇게 초고속 승진을 하는 걸 보니까 정계에 괜찮은 꽌시(关系)라도 있는 건가?」

「……나이는 어리지만 그만큼 뛰어난 분입니다. 저희와도 형제처럼 지내실 만큼 신망도 두텁고요.」

고위 장교가 손에 든 지휘봉을 쓸어내렸다.

「헌터들 위아래 없는 거야 본관도 잘 알고 있네. 하지만 지금은 전시 상황이야. 이 명령은 사령관이신 랴오 상장께서 내리신 거고.」

「사령관님께서 직접…… 말씀이십니까?」

「그래. 그러니 명령에 따르기 싫다면 지금이라도 돌아가게. 단, 지금 자네의 행동이 명령 불복종이라는 사실을 알고 있기를 바라지.」

「……!」

「진격 속도를 좀 더 단축하고자 할 뿐이야. 정황상 그럴 리는 없겠지만 몬스터 잔당이 남아 있다면 쓸어 버리고, 위험에 빠진 민간인들을 구출하는 게 전부라고. 알아들었나?」

한참이나 말이 없던 장 웨이는 고개를 끄덕이고 물러났다.

일반적으로 공안 무력부는 군부에 속하지 않은 별개의 단체로 취급받지만, 현재는 전시 상황이었다. 서부 전선 사령관인 랴오 상장의 명령을 거스르는 건 결코 좋은 선택이 아니었다.

「뭐랍니까?」

한껏 목소리를 낮춘 부하의 물음에 장 웨이가 대답했다.

「쉬운 작전이니 닥치고 따라오라는군. 거절하면 명령 불복종이고.」

「그 말을 믿으십니까?」

「전자를 묻는 거라면 당연히 아니지. 하지만 후자는 사실일 거야. 자네는 어떻게 생각하나?」

「당연히 못 믿죠. 왕 상교 저놈, 능력도 없는 주제에 태자당 쪽 꽌시 하나로 여기까지 올라온 놈입니다. 랴오 상장이 기르는 충견이라고 소문이 자자해요.」

「바로 그 랴오 상장의 명령이야. 당장은 구린내가 나더라도 참을 수밖에.」

「……빌어먹을.」

「하지만 왕 상교의 말이 사실일지도 몰라. 인근에 존재하는 대부분의 몬스터는 전부 아군과 교전 중일 테니까. 현재 우리 전력이라면 몬스터 잔당 정도는 충분해.」

장 웨이는 주위를 둘러보았다. 그를 포함한 백 명의 헌터 외에도 이십여 대의 전차와 오백의 보병. 상공에는 전투 헬기 세 대가 시야를 확보하며 나아가는 중이었다.

‘부디 별다른 피해가 없기를.’

장 웨이의 바램이 하늘에 닿았는지, 그가 우려하던 일은 발생하지 않았다.

촉각을 곤두세우며 진입한 쑤이닝시 인근의 작은 소도시는 몬스터에 의해 초토화된 상태였을 뿐, 폐허가 된 도심은 적막하기 그지없었다.

고블린, 오크 따위의 몬스터가 간간이 튀어 나왔지만, 그들에게는 아무런 위협도 되지 못했다.

- 키이이익!

서걱!

가장 선두에서 십여 마리의 몬스터들을 처치한 장 웨이는 약간 이나마 마음이 풀어졌다.

「종도 다른 몬스터가 따로따로 나타나는 걸 보니 무리에서 이탈한 놈들 같군요.」

「예상대로군. 그러게 내가 뭐라고 했나?」

거만하게 대답하는 꼴이 썩 마음에 들지 않았지만, 차라리 이게 낫다.

그렇게 생각하고 잠자코 고개를 끄덕이던 장 웨이는 이어지는 고위 장교의 말에 멈칫하고 말았다.

「병력을 나누라고 하셨습니까?」

「그래. 이런 상황이라면 최대한 빨리 생존자부터 찾아야지.」

「하지만 왕 상교님. 진입한 지 아직 한 시간도 채 되지 않았습니다. 조금 더 중심부로 나아간 후에…….」

「건방진 소리.」

「예?」

「전투 실력은 헌터인 자네들이 나을지 몰라도, 전술은 내가 몇 수 위야. 현재 지휘권은 내게 있으니 그만 입 다물고 명령을 따르라고.」

「……!」

「못 들었나? 그럼 본관이 직접 자네 수하들에게 명령을 내릴까?」

「……제가 하지요.」

「세부 지도는 갖고 있겠지. 그럼 두 시간 후에 중앙 광장에서 보도록 하지.」

장 웨이를 향해 밉살맞게 웃어 보인 장교가 장갑차에 몸을 실으려던 그 순간이었다.

쐐애애액, 펑!

장 웨이는 멍하니 눈을 깜빡였다. 손바닥으로 얼굴을 쓸어내리자 끈적한 핏물이 한가득 묻어 나왔다.

한없이 붉은색을 띤 그것은 분명 인간의 것이었고, 이미 상반신이 흔적도 없이 사라진 장교의 몸뚱어리는 장갑차에서 굴러떨어지고 있었다.

쿵.

숨 막히는 정적. 가장 먼저 정신을 차린 장 웨이가 외쳤다.

「전원 전투 준비-!」

「몬스터! 몬스터가 나타났다!」

「탱커!」

「여, 연대장님께서 전사하셨다!」

그 외침에 가장 먼저 반응한 것은 공안 무력부의 헌터들이었고, 군인들은 한차례 늦게 상황을 파악했다.

그리고 갑작스러운 지휘관의 사망으로 극심에 혼란에 빠진 그들을 기다리고 있던 것은 더욱 처절한 죽음이었다.

쐐애애액!

단 한 번의 파공성.

보이지도 않는 속도로 쏘아진 빛줄기가 오와 열을 맞춘 채 진군 중이던 군인들을 휩쓸었다.

퍼버버벙!

수십의 사람들을 풍선처럼 터트리며 나아간 빛줄기가 마지막으로 꿰뚫은 것은 보병들의 호위를 받으며 이동하던 장갑차였다.

단단한 외피를 뚫고 내부 깊숙이 파고든 빛줄기. 그 광경을 목격한 장 웨이가 벼락처럼 외쳤다.

「모두 피해!」

그러나 그의 외침이 닿기도 전에, 다음 순간 터져 나온 굉음이 모든 것을 집어삼켰다.

꽈아앙!

붉은 섬광, 검은 연기와 함께 터져 나간 장갑차의 파편이 수백, 수천 개의 칼날이 되어 사방을 난자한다.

군인은 물론이고 미처 반응하지 못한 하급 헌터까지. 셀 수도 없는 이들이 짚단처럼 쓰러졌다.

이미 숨이 끊긴 그들의 몸뚱어리는 미동조차 하지 않았다.

「……!」

「이, 이게 도대체…….」

석상처럼 굳어 버린 사람들을 향해 장 웨이가 고함을 내질렀다.

「산개! 모두 산개해라! 전차와 장갑차에서 최대한 멀리 떨어져!」

하지만 난생처음으로 실전을 겪는 병사들의 몸은 굳어 있었고, 아직 모습을 드러내지 않은 상대는 적들의 혼란을 결코 놓치는 법이 없었다.

쐐애애애액!

다시 한번 들려오는 죽음의 소리. 그러나 지금까지와는 달리 쏘아진 빛줄기는 하나가 아니었다.

콰앙! 퍼버버벙!

「크아아아악!」

불꽃이 솟구치고 비명이 넘쳐흐른다.

이십여 대의 장갑차와 전차가 무력화되기까지 걸린 시간은 그야말로 찰나.

상공을 배회하던 세 대의 전투 헬기 역시 수많은 파편으로 화해 지상으로 추락했다.

콰앙! 투두두둑.

시산혈해라고 부를 만한 참혹한 현장에, 장 웨이는 등골을 타고 흐르는 오싹한 기운을 느꼈다.

‘최소 A급 몬스터. 그것도 한둘이 아니다.’

아이러니하게도, 그것이 오늘 장 웨이가 내린 판단 중 가장 정확한 것이었다.

스아아아아.

어두컴컴한 골목과 무너진 건물 사이. 아직도 타오르는 빌딩의 옥상.

검은 안개처럼 나타난 열 개의 형체들은 타오르는 보랏빛 안광으로 살아남은 수백의 인간들을 응시했다.

뼈밖에 남지 않은 전마(戰馬)에 올라탄 형체들을 발견한 장 웨이의 입술 사이로 신음 같은 한 마디가 새어 나왔다.

「……데스나이트(Death Knight).」

한때는 고결했으나 흑마법에 의해 타락한 죽음의 기사들.

리치와 함께 대격변 이후 모습을 감춘 바로 그 데스나이트가 나타났다. 그것도 자그마치 열 기나 되는 숫자.

순간 장 웨이의 머릿속에 가장 먼저 떠오른 단어는 죽음이었다.

‘여기까지인가.’

데스나이트는 A급 몬스터를 벗어난 존재들이다.

아직 백 명의 헌터와 군병력이 남았지만, 장 웨이는 이미 알고 있었다.

놈들이 펼쳐 놓은 그물을 피할 수 없다는 사실을.

하지만…….

「곱게 죽어 줄 생각 따위는 없다.」

그것은 비단 장 웨이만의 생각이 아니었다.

두려움으로 총기조차 제대로 잡지 못하는 군인들과 달리, 공안 무력부의 헌터들은 결의에 찬 눈빛으로 각자의 병장기를 치켜세웠다.

「너희까지 이럴 필요는 없어.」

장 웨이의 나지막한 한마디에, 소대장 중 하나가 퉁명스럽게 대답했다.

「중대장님은 이래도 되고요?」

「미안하다. 너희를 데려오는 게 아니었는데.」

「누가 데려온 게 아니라, 저희가 따라온 겁니다. 중대장님 덕분에 열 번도 넘게 살아남았으니 한 번쯤 이럴 때도 됐죠.」

아무렇지 않게 말하지만, 목소리에 묻어 나오는 떨림마저 감출 수는 없었다.

미동도 하지 않는 열 기의 데스나이트를 바라보며, 장 웨이는 바짝 마른 입술을 핥았다.

「최선을 다해 싸우고, 한 사람이라도 살아남아라. 너희에게 해 줄 말은 그게 전부다.」

대답 대신 우렁찬 함성이 터져 나왔다. 두려움을 몰아낸 헌터들의 눈동자가 샛별처럼 빛났다.

안전하고 풍요로운 삶을 원했다면 다른 길도 있었다.

그러나 그들이 부유한 기업가의 경호원이나, 용병 대신 공안 무력부를 택한 것은 헌터로서의 명예와 책임감 때문이었다.

이건 결코 물러설 수 없는 싸움이다.

「가자! 인민의 아들딸, 중화의 후예들이여!」

온 힘을 다해 부르짖은 장 웨이가 가장 가까운 데스나이트를 향해 쇄도하려던 바로 그 순간.

구구구구궁!

그건 본능에 가까웠다.

거센 진동과 함께 느껴지는 거대한 기운. 살아남은 인간들은 전신의 털이 쭈뼛 곤두서는 공포와 함께 고개를 돌렸다.

여러 눈동자가 향하는 곳에, 폐허가 된 도심지를 천천히 가로지르는 검은 기사가 있었다.

깊게 눌러쓴 투구 아래, 붉은 안광이 번쩍인다. 핏기없는 입술 사이로 죽음의 숨결이 뿜어져 나왔다.

- 사르, 가로쉬.

누구도 알아들을 수 없는 마계의 언어.

그러나 다음 순간, 장 웨이는 곧 그 말이 무엇을 뜻하는지 깨달을 수 있었다.

‘모두 죽여라.’

부릅떠진 장 웨이의 눈동자에, 사방에서 쇄도해 오는 열 기의 데스나이트가 비쳤다.

서걱!

도륙의 시작이었다.



* * *



철벅.

뼈밖에 남지 않은 말발굽이 피 웅덩이를 밟았다.

마지막까지 저항하던 중년의 헌터, 장 웨이의 시신을 물끄러미 내려다보는 검은 기사를 향해 다가온 데스나이트들이 한쪽 무릎을 꿇었다.

- 로드. 다음 명령을.

다음 명령이라.

잠시 말이 없던 검은 기사가 문득 손을 뻗었다.

쉬익, 서걱!

채찍처럼 휘둘러진 흑색 빛줄기가 콘크리트와 철근을 갈랐다.

비스듬히 허물어지는 건물. 드러난 내부 공간에는 한껏 입을 막은 채 웅크려 있는 인간들이 있었다.

「진진. 여보. 괜찮아, 괜찮아…….」

「흑, 흐흐흑!」

「압빠빠?」

인간 수컷과 암컷. 그리고…… 아직 암수 구분이 되지 않을 만큼 한없이 작고 가벼워 보이는 존재.

아마 저걸 아이라고 하던가.

‘아이, 아이?’

이 단어를 어디서 들어 봤던가.

검은 기사는 문득 드는 의문을 뒤로하고 손을 뻗었다. 눈에 보이는 인간은 말살시켜야 한다. 그것이 그가 받은 명령이었다.

하지만.

- ……?

어째서인지 손이 나아가지 않았다.

손가락만 튕겨도 한 줌 핏물로 화해 사라질 나약한 존재들이 분명한데, 마치 보이지 않는 방어막이 인간들을 감싸고 있는 듯했다.

- 너희는. 뭐지?

검은 기사의 음산한 목소리에 부모의 품 안에서 꼬물거리던 아이가 으앙, 하고 소리 내어 울음을 터트린 그때였다.

- 이건.

문득 고개를 들어 저 너머를 바라보던 검은 기사가 말머리를 돌렸다.

갑작스러운 우두머리의 행동에 데스나이트들이 의문을 표했다.

- 로드?

- 돌아간다. 지금. 당장.

- 그럼 인간들은 저희가.

- 돌아간다. 지금. 당장.

그것이 전부였다. 무릎을 꿇어 예를 표한 열 기의 데스나이트는 우두머리의 뒤를 따라 말을 달렸다.

그들의 모습이 안개처럼 사라지기 직전, 검은 기사의 붉은 안광이 기적처럼 살아남은 세 인간에 닿았다가 떨어졌다.

휘이이이잉.

피비린내를 머금은 바람이 시체로 가득한 폐허를 휩쓸었다.
```

## Current accepted English baseline

```markdown
# Chapter 391

Zhang Wei, commander of the 2nd Company of the Sichuan Province Public Security Armed Forces, had felt uneasy about this operation from the very beginning.

*Advance ahead with the army and seize the city? That’s different from the order Regimental Commander Shao gave me.*

The doubt Zhang Wei had been harboring only grew when they deliberately bypassed the allied forces engaged in combat ahead of them and continued their advance.

“Senior Colonel Wang. Are you certain our regimental commander approved this operation?”

The middle-aged senior officer frowned at Zhang Wei’s question.

“Why are you curious about that?”

“No matter how I look at it, something seems wrong. Our regimental commander clearly told us to conserve our strength in the rear and guard headquarters…”

“Ah, you mean that little regimental commander.”

Zhang Wei’s expression hardened at the senior officer’s mocking tone toward Shao Shen.

“Regimental Commander Shao Shen holds the same rank as you, Senior Colonel Wang. And he’s about to be promoted to major general.”

“That ignorant child was simply lucky. Awakening as an A-rank Hunter wasn’t enough—thanks to that Korean bastard’s performance, he even ended up on this promotion list. Considering how quickly he’s risen through the ranks, I wonder if he has some decent guanxi in political circles.”[^1]

“He may be young, but he’s just as capable. He’s also well respected enough that he treats us like brothers.”

The senior officer stroked the baton in his hand.

“I know Hunters don’t recognize rank and seniority the way ordinary soldiers do. But this is wartime. This order came from Senior General Liao, the commander.”

“From the commander himself…?”

“That’s right. So if you don’t want to follow the order, turn back now. But I hope you understand that what you’re doing constitutes disobeying orders.”

“……!”

“I merely want to shorten our advance time. The circumstances make it unlikely, but if any monsters remain, we’ll wipe them out and rescue any civilians in danger. That’s all. Understood?”

Zhang Wei remained silent for a long while before nodding and stepping away.

The Public Security Armed Forces were generally treated as a separate organization outside the military, but this was wartime. Defying Senior General Liao, the commander of the western front, was by no means a wise choice.

“What did he say?”

A subordinate asked in a lowered voice. Zhang Wei answered.

“He says it’s an easy operation, so we should shut up and follow him. Refusing would constitute disobedience.”

“Do you believe him?”

“If you’re asking about the first part, of course not. But the second part is probably true. What do you think?”

“Of course I don’t believe him. That bastard Senior Colonel Wang has risen this far on a single connection to the Princelings despite having no ability. Everyone says he’s Senior General Liao’s lapdog.”

“And this is an order from that very Senior General Liao. We’ll have to endure it for now, even if it smells rotten.”

“Damn it.”

“But Senior Colonel Wang might be telling the truth. Most of the monsters in the area are probably engaged with our forces. With our current strength, we should be more than capable of handling a few stragglers.”

Zhang Wei looked around him. In addition to the hundred Hunters, including himself, there were around twenty tanks and five hundred infantrymen. Three combat helicopters were advancing overhead, securing their field of vision.

*Please, let there be no casualties.*

Perhaps Zhang Wei’s wish had reached the heavens. The thing he had feared did not happen.

The small town near Suining City, which they entered with every sense alert, had been utterly devastated by monsters. Apart from that, the ruined downtown area was deathly silent.

Monsters such as goblins and orcs occasionally sprang out, but they posed no threat whatsoever.

—Kieeeek!

Slice!

After killing a dozen or so monsters at the very front, Zhang Wei felt slightly more at ease.

“Seeing how monsters of different species are appearing separately, they must be stragglers that broke away from the main group.”

“Just as expected. What did I tell you?”

The officer’s arrogant manner was irritating, but this was still preferable.

Thinking so, Zhang Wei silently nodded. Then he froze at the senior officer’s next words.

“You want us to split up our forces?”

“That’s right. In a situation like this, we need to find survivors as quickly as possible.”

“But Senior Colonel Wang, we haven’t even been inside for an hour yet. We should advance a little farther toward the center first…”

“Impertinent.”

“Pardon?”

“You Hunters may be better at combat, but I’m several moves ahead of you when it comes to tactics. I hold command authority at present, so stop talking and follow my orders.”

“……!”

“Didn’t you hear me? Should I issue the order directly to your subordinates?”

“…I’ll do it.”

“You have a detailed map, I assume. Then we’ll meet at the central square in two hours.”

The officer gave Zhang Wei a hateful smile and was about to climb into an armored vehicle when—

Whoooosh—boom!

Zhang Wei blinked blankly. When he wiped his face with his palm, it came away covered in sticky blood.

The substance was unmistakably human blood, bright red without end. The officer’s body, already missing its entire upper half, rolled out of the armored vehicle.

Thud.

A suffocating silence descended. Zhang Wei was the first to regain his senses.

“Everyone, prepare for battle!”

“Monsters! Monsters have appeared!”

“Tank!”

“T-The regimental commander has been killed!”

The Hunters of the Public Security Armed Forces were the first to react to the shouts. The soldiers understood what was happening a moment later.

And waiting for them, already thrown into utter chaos by their commander’s sudden death, was an even more horrific death.

Whoooosh!

A single sound of air being split.

A streak of light fired at an invisible speed swept across the soldiers marching in orderly ranks.

Boom-boom-boom!

The streak of light burst dozens of people like balloons as it advanced, then finally pierced the armored vehicle moving under the protection of the infantry.

It broke through the vehicle’s hard outer shell and burrowed deep inside. The sight made Zhang Wei shout like a thunderclap.

“Everyone, get clear!”

But before his voice could reach them, the thunderous roar that erupted the next moment swallowed everything.

KABOOM!

The armored vehicle exploded in a red flash and black smoke. Its fragments became hundreds, thousands of blades, tearing into everything around them.

Soldiers and lower-ranking Hunters who failed to react in time alike fell like sheaves of straw. Countless bodies collapsed.

Those who were already dead did not move even an inch.

“……!”

“W-What the hell is this…?”

Zhang Wei shouted at the people frozen like statues.

“Spread out! Everyone, spread out! Get as far away from the tanks and armored vehicles as possible!”

But the soldiers, experiencing real combat for the first time in their lives, were frozen in place. And their opponent, who had yet to reveal itself, never failed to take advantage of the enemy’s confusion.

Whoooosh!

The sound of death rang out once again. But unlike before, there was more than one streak of light.

Boom! Boom-boom-boom!

“Aaaaargh!”

Flames erupted, and screams flooded the air.

The roughly twenty armored vehicles and tanks were disabled in the blink of an eye.

The three combat helicopters circling overhead also shattered into countless fragments and crashed to the ground.

Boom! Clatter, clatter.

Amid the horrific scene that could only be called a mountain of corpses and sea of blood, Zhang Wei felt a chill run down his spine.

*At least an A-rank monster. And not just one or two.*

Ironically, it was the most accurate judgment Zhang Wei would make that day.

Ssssss.

Between dark alleys and collapsed buildings, atop a still-burning building—

Ten figures appeared like black mist, staring down at the hundreds of surviving humans with blazing violet eyes.

A groan escaped Zhang Wei’s lips when he spotted the figures mounted on warhorses stripped down to their bones.

“…Death Knights.”

Once noble, they were knights of death corrupted by dark magic.

The very Death Knights that had vanished from sight after the Great Cataclysm along with the Lich had appeared. And there were no fewer than ten of them.

The first word that came to Zhang Wei’s mind was death.

*Is this where it ends?*

Death Knights were beings that had surpassed A-rank monsters.

A hundred Hunters and the military forces still remained, but Zhang Wei already knew.

They could not escape the net that had been spread around them.

But…

“I have no intention of dying quietly.”

That thought did not belong to Zhang Wei alone.

Unlike the soldiers, who were so terrified they could barely hold their guns properly, the Hunters of the Public Security Armed Forces raised their weapons with eyes full of resolve.

“You don’t have to do this.”

One of the platoon commanders answered Zhang Wei’s quiet words bluntly.

“And you do?”

“I’m sorry. I shouldn’t have brought you here.”

“No one brought us. We followed you. We’ve survived more than ten times thanks to you, Company Commander. It was about time we faced something like this at least once.”

He spoke as though it were nothing, but he could not hide the tremor in his voice.

Zhang Wei licked his parched lips as he stared at the ten Death Knights that remained perfectly still.

“Fight with everything you have, and make sure at least one of you survives. That’s all I have to say.”

A thunderous cheer erupted in place of an answer. The Hunters’ eyes, their fear driven away, shone like morning stars.

If they had wanted safe and prosperous lives, they could have chosen another path.

But they had chosen the Public Security Armed Forces over becoming bodyguards for wealthy entrepreneurs or mercenaries because of their honor and sense of responsibility as Hunters.

This was a battle they could never retreat from.

“Forward! Sons and daughters of the people, descendants of Zhonghua!”

Just as Zhang Wei roared with all his strength and was about to charge toward the nearest Death Knight—

Rumble-rumble-rumble!

It was almost instinctive.

A tremendous force accompanied the violent tremors. The surviving humans turned their heads, terror making every hair on their bodies stand on end.

Where countless eyes turned, a black knight was slowly crossing the ruined downtown area.

Red eyes flashed beneath a helmet pulled low. The breath of death poured from between its bloodless lips.

—Sar, Garosh.

A language of the demon realm that no one could understand.

But the next moment, Zhang Wei realized what the words meant.

*Kill them all.*

The ten Death Knights charging from every direction were reflected in Zhang Wei’s wide-open eyes.

Slice!

The massacre began.

* * *

Splash.

A horse’s bony hoof stepped into a pool of blood.

The Death Knights approached the black knight, who was gazing down at the corpse of Zhang Wei, the middle-aged Hunter who had resisted until the very end, and dropped to one knee.

—Lord. Awaiting your next command.

The next command.

After remaining silent for a moment, the black knight suddenly extended a hand.

Whoosh—slice!

A black streak of light, swung like a whip, cut through concrete and rebar.

The building collapsed at an angle. Inside the exposed space, humans were crouched together with their hands clamped tightly over their mouths.

“Jinjin. Honey. It’s okay, it’s okay…”

“Sniff… sob…”

“Dada?”

A human male and female. And…

A being so small and light that it was impossible to tell whether it was male or female.

Perhaps that was what they called a child.

*Child. Child?*

Where had he heard that word before?

The black knight pushed the question aside and extended his hand. The humans within sight had to be annihilated. That was the order he had received.

But—

—……?

For some reason, his hand would not move forward.

The creatures were clearly so weak that the snap of a finger would turn them into a handful of blood and make them disappear. And yet it was as if an invisible barrier surrounded them.

—What are you?

At the black knight’s eerie voice, the child wriggling in its parents’ arms suddenly burst into a wailing cry.

—This is…

The black knight abruptly lifted its head and looked into the distance before turning its horse around.

The Death Knights questioned their leader’s sudden movement.

—Lord?

—We’re leaving. Now. At once.

—Then we’ll take care of the humans—

—We’re leaving. Now. At once.

That was all.

The ten Death Knights knelt in salute, then spurred their horses after their leader.

Just before they vanished like mist, the black knight’s red eyes touched the three humans who had survived by a miracle, then moved away.

Whoooooosh.

A wind carrying the smell of blood swept through the ruins filled with corpses.

[^1]: *Guanxi* refers to a network of personal connections and favors, especially one useful in politics or business.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 391`.

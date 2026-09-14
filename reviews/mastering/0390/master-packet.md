# Master Edit Task — Chapter 390

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
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 시스템              | **System**                     |
| 경험치              | **EXP**                        |
| 퀘스트              | **Quest**                      |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 귀가      | **your family**                                                 |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 상장 | **Senior General** | Wei Penghu's military rank, explained as four-star. |
| 천격 | **Heavenly Strike** | Named spear technique used by Taekyung. |
| 주모 | **Jumo** | Traditional tavern keeper in the Korean victory-day joke. |
| 청두군구 | **Chengdu Military Region** | Chinese military region commanded by Senior General Liao. |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |

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

#### Chapter 388 tail (verified mastered)

…
that way, you certainly drank yourself senseless yesterday.” “That was…” “I know. I’m joking. This is how people like us forget the burden for a little while. We might die tomorrow—or even today.” The words didn’t match her bright voice at all. The hero who had fought her way through the maelstrom of the Great Cataclysm with her entire body raised her head and gazed at the sky. “Ah. Perfect weather for a fight.” Then she turned and walked lightly toward the jet, which was ready for takeoff. She left us with one quiet remark. “Let’s all see each other alive.” Her back disappeared into the aircraft. Magic Johnson gazed up at the sky for a moment with emotion in his eyes, then abruptly spoke. “Hey, Choi.” “Yes?” “Relax your ass, too.” “…” “No, I mean relax your shoulders. Let’s see each other alive again.” *I had a feeling his true feelings had just slipped out.* Magic Johnson laughed heartily at Team Leader Choi’s wary gaze and boarded the jet after Pai Chen. Wu Heixing then walked off as though fleeing. Lee Jungryong, the last one left, looked Team Leader Choi and me over with a strange gaze. “Both of you, take care. You can’t go dying in a place like this when you’re still so young.” *What an old man’s way of putting it. What a loaded remark.* I smiled and spoke in place of Team Leader Choi, whose face had gone rigid. “We should. Unlike some people, dying now wouldn’t exactly count as a good death for us.[^2]” “…!” “If you kick the bucket, I’ll make a generous condolence contribution.” “I’ll look forward to it.” After a brief silence, Lee Jungryong tossed out that one remark and led the Ares Guild members away. Now only the two of us remained. I stretched with all my might, then patted Team Leader Choi on the shoulder. “Let’s go, Team Leader.” “Yes. We should.” “There’s no need to be nervous. Relax your ass.” “…” “…It was a joke. Sorry.” *At this rate, two jokes would be enough to kill a man.* I was cautiously watching Team Leader Choi’s expression as I climbed aboard the jet when— “Troops—attention!” A thunderous shout erupted behind us. Minister of Defense Wei Penghu was saluting us, his half-gray hair whipping in the wind. The people filling the airfield followed his example and saluted. It was a gesture of respect toward the heroes going to fight for the gathered crowd’s families and friends. They held their salutes until the jet’s door closed and the aircraft dwindled to a distant speck, then vanished from sight. *Good grief.* After a send-off like that, how could my shoulders not feel heavy? I suddenly felt tired and leaned back against my seat. Static crackled. - …respond. Respond. This is… Along with the distorted radio transmission coming from the cockpit, an alert pierced my ears. Ding. > **System** > > - Unexpected Quest generated: The Battle Situation Has Become Critical. > > - You cannot refuse the Quest. Arrive as quickly as possible and defeat the enemies! “…” *Damn it. That’s just how my life goes.* I let out a deep sigh, then shouted toward the cockpit. “Sir, give it full throttle!” * * * “What about them?” The speaker was an old man in his eighties. Wrinkles and age spots covered his face. His aged body was no longer what it had been in his youth, but his eyes held even greater strength than they had back then. Even through the holographic screen, the force of the old man’s gaze was palpable. Wei Penghu swallowed hard before answering. “They have all departed, Comrade Chairman.” “How is the battle situation?” “We cannot easily determine the enemy’s movements because of communication interference caused by magic and the barriers, but we are doing our best to detect their movements.” “If the S-rank Hunters arrive…” “With their power, they should be more than capable of turning the tide.” “Do not jump to conclusions. Do not let your guard down for even a moment. Countless lives depend on our decisions.” “Yes. I will keep that in mind.” After ending his brief communication with Minister of Defense Wei Penghu, state chairman Xiao Yang sat alone in the vast conference room, lost in thought. *How did it come to this?* This was an unprecedented catastrophe since the Great Cataclysm. They had committed vast amounts of manpower and funding, yet still failed to stop the monster army centered around the Arch Lich. He had wanted to prevent panic if at all possible, but if they delayed any longer, the opportunity might disappear forever. That was why Xiao Yang had come here today, despite the countless objections from within the Communist Party. “We are ready.” “…Connect me immediately.” At the secretary’s words, Xiao Yang opened his closed eyes. One by one, holographic figures began to appear above the empty seats throughout the vast conference room. Fourteen people of different races and genders. No—fifteen, including Xiao Yang. Each one was the leader of a nation, and all belonged to a single organization. *The United Nations Security Council.* The old chairman announced the beginning of the emergency meeting in a grave voice. [^1]: *Bangzi* is a derogatory Chinese slur for Koreans. [^2]: A *ho-sang* is a death considered fortunate because it comes after a long, full life, usually at an advanced age.

#### Chapter 389 tail (verified mastered)

…
three times on the western front, but there’s been no news since, so I guess they’re holding the line. └ Hmm… Everyone knows how strong Lee Jungryong is, so I’m not worried about him. But is Sibeol-jwa going to be all right? He’s still an A-rank Hunter. └ ?? LOL └ LMAOOOOOOOOOO └ There’s still an innocent idiot who treats Sibeol-jwa like an A-rank Hunter? As an active A-rank Hunter myself, all I can do is laugh. That Jin Taekyung guy is just a monster lol Hey heyheyhey!! The S—Security Council just posted an update on the w—western front! └ Oh, Sibeol-jwa news. Been a while. └ That sounds incredibly urgent. The western front? What are they saying? └ They say it was breached? └ Huh? └ Huh? └ What the hell does that mean? Don’t tell me Sibeol-jwa died…? └ Wait. What is this actually saying? Guys, I’m going back to check it again. It’s on the main page, so go look for yourselves. └ Ah. I’m suddenly fucking terrified. I’m checking it right now. └ Go go go go go The netizens who had been excitedly writing comments rushed to the United Nations Security Council website. So many users flooded the site at once that it exceeded its traffic limit, forcing them to wait for quite some time. When they finally saw the announcement on the main page, they could only doubt their own eyes and ears. “…What the hell is that?” The map displayed the standoff with the monster army. The front line formed an oval, but the western front had been gouged inward like an awl. …I just checked. It really was breached. └ Is Jin Taekyung dead? How bad are the casualties? └ No, the monsters’ line was breached. └ ?? └ ??? └ The breakthrough was so fast that the updates couldn’t keep up. └ …Does that even make sense? └ Shut up and pull down the shutters. Today is the tavern lady’s death anniversary…[^1] * * * The battlefield where a fierce battle was about to erupt was crowded. An endless wasteland stretched out before us, and countless monsters filled my field of vision. A wind that blew in from somewhere carried the thick killing intent and stench pouring off the creatures. “Fucking hell. There sure are a lot of them.” Team Leader Choi, standing beside me, answered my mutter. “No matter how many we kill, there’s no end to them.” It was the fourth day since we had been deployed to the western front and the fighting had begun in earnest. There was no trace left of the Team Leader Choi who had always looked immaculate. Covered in blood and dust, he looked at me with a calm, somber gaze. “When do we begin?” “Who knows? We should hear what our little commander thinks first. Right?” That last question wasn’t directed at Team Leader Choi. The twenty-one-year-old “little commander” who had not left my side the entire time answered. It was Shao Shen. “I will follow Teacher Jin’s orders!” A snort of laughter escaped me at the sparkle in his eyes. “You’re still going on about calling me Teacher. You were the one who told me to speak casually to you first. I said you might as well call me hyung.” “Is it… Is it really all right if I do that?” “I told you it was fine as long as you were okay with it. But can you really act like this in front of your men? I heard you’re about to be promoted to major general.” Shao Shen shook his head at lightning speed. “There’s no problem at all! H-h-hyung-nim!” He was frighteningly calm in battle, so I had no idea why he stammered so much the rest of the time. I looked at the Hunters from the Public Security Armed Forces lined up behind him. There were more than a thousand of them. Their heated eyes held admiration and awe for the strong. Of course, Shao Shen stood out even among them. “Give us your orders. H-hyung-nim.” “Orders, huh?” I suddenly looked up at the sky. A huge eagle with its wings spread wide circled above our heads. I had a good feeling about today, too. “Follow me. Just like you’ve done until now.” “…!” “Right now.” With that answer, I stepped forward. Crack. The force of ten thousand geun concentrated in the tip of my foot split the ground like a spiderweb and drove it inward. And then, in the next moment— Boom! With a deafening roar that left my ears ringing, I shot forward as a streak of light. *Flamefire Path.* The wind carrying the cold heated up and transformed into a blast of hot air. As the ground, wind, and scenery streaked past, a tremendous roar erupted behind me. “Charge! Charge!” “Descendants of Zhonghua! People! Sweep every last one of them away!” “Waaaaaaah!” Thud-thud-thud-thud! Kyaaaauuuuu! Human battle cries and monster shrieks rang across heaven and earth. The immense vibrations shook the very ground. At the threshold of that chaos, I swung the White Flame in my hand with all my strength. Whoooosh! The Extreme Yang force that surged from the spearhead sliced through everything standing in its way. [^1]: Korean internet slang calls for a tavern lady to pour celebratory drinks whenever national pride surges; the joke is that today’s celebration will work her to death.

## Korean source

```text
＃390화



촤아아악!

강기가 스쳐 지나간 자리, 솟구치는 목들과 함께 뜨거운 핏물이 뿜어져 나온다.

나는 볏짚처럼 쓰러지는 오우거의 몸뚱이를 밟고 높이 솟아올랐다. 목덜미에 닿는 햇볕이 따스하다.

‘거, 싸우기 딱 좋은 날씨네.’

때는 정오. 장소는 나무 한 그루 없는 황무지.

운집해 있는 천여 마리의 몬스터들 한가운데에 태양을 등진 내 그림자가 비친다.

급강하와 동시에 내리그어지는 창날의 움직임까지도.

‘천격(天格).’

콰아아아앙!

화룡의 발톱이 지상을 할퀴었다.

하늘이 쪼개지는 듯한 굉음. 지면이 수 미터 깊이로 주저앉고 흙과 돌 부스러기가 사방으로 비산한다.

전장의 중심에서 일어난 열풍(熱風)의 회오리가 칼날이 되어 몬스터들을 휩쓸었다.

콰아아아!

띠링. 띠링. 띠링…….

흙먼지로 인해 뿌옇게 물든 시야 속, 몬스터 처치를 알리는 시스템 알림과 함께 녹색 핏물이 투두둑 쏟아진다.

가볍게 손을 내젓자 먼지구름이 흩어지고 멍한 얼굴로 나를 응시하는 몬스터들이 보였다.

- 취릭?

- 크륵?

도대체 이게 무슨 상황인지 모르겠다는 듯한 눈빛들. 깊게 숨을 들이쉰 나는 공력을 실은 외침을 토해 냈다.

“쓸어-!”

그리고 다음 순간.

「와아아아아아!」

귀가 먹먹해지는 함성과 함께, 어느새 들이닥친 천여 명의 헌터들이 파도처럼 몬스터 군단을 덮쳤다.

콰드드드득!

퍼버벅!

속수무책으로 허물어지는 몬스터들을 보며 한 가지 확신이 들었다.

‘이 전투, 이겼다.’

농사가 끝났으니 이제 추수를 해야 할 때.

나는 보스 몬스터로 보이는 트윈 헤드 오우거를 향해 걸음을 옮겼다.

내 금쪽같은 경험치. 아니, 아군의 피해를 최소화하기 위해서였다.

「저놈이 우두머리다! 원거리 부대!」

“야, 야! 손 떼! 내가 처리할 테니까 털끝 하나 건드리지 마!”

하늘에 맹세컨대, 정말 요만큼의 사심도 없다.

“…….”

음, 곰곰이 생각해 보니까 맹세할 필요까지는 없을 것 같다.

- 간악한 인간이여. 부산물을 차지하려는 네 속셈이 뻔히 들여다보인다. 내 군단을 학살할 때도 탐욕을 숨기지 않았지!

“닥치고 네 할 일이나 하지? 빨리 언데드로 동족상잔 시작해.”

- 안 그래도 그러려고 했다. 자라나라 해골해…… 어?

“왜 그래?”

- 왜 내 힘이 통하지 않는 거지? 혹시 버그인가?

“……그런 단어는 또 어디서 주워들은 거야.”

점점 현대화가 진행 중인 스켈레톤 워로드가 낙담한 목소리로 말했다.

- 안으로 들어올수록 아크 리치의 지배력이 강해지는 것 같다. 아아, 군단 없는 사령관이라니. 실로 통탄을 금치 못하겠구나. 이래서야 죽은 것이나 다름없어!

“…….”

이 새끼는 본인을 뭐라고 생각하는 거지.

이제는 이미 죽어 있다고 말해 주는 것도 지겹다. 나는 내심 한숨을 내쉬며 우두머리를 향해 달려들었다.



* * *



「대승입니다! 이번에도 대승이에요!」

샤오 쉔이 발갛게 달아오른 얼굴로 외쳤다. 지금까지 열 번도 넘게 본 광경이라 이제는 나와 최 팀장도 그러려니 하고 넘기는 분위기다.

‘뭐, 신날 만도 하지.’

자그마치 천여 마리의 몬스터 대군을 전멸시키기까지 겨우 두 시간 남짓.

그것도 단 한 사람의 사망자도 없이 마무리 지었으니 기념비적인 승리인 것은 맞다. 이런 상황에서는 오히려 덤덤한 것이 이상한 거지.

「저희 쪽 피해는 중상자 스물셋, 경상자 서른 명이 전부입니다. 아, 이건 정말……!」

오줌 마려운 강아지처럼 몸을 부르르 떤 샤오 쉔이 반짝거리는 눈동자로 나를 바라봤다.

「어떻게 매번 이럴 수 있는 겁니까?」

“음. 그건 내가 강하기 때문이 아닐까.”

내 대답에 최 팀장이 살짝 어이없다는 눈빛을 보냈다.

“왜요?”

“아니. 보통 이럴 때는 운이 좋다거나, 뭐 그런 겸양의 말을 하지 않습니까?”

“보통은 그렇죠. 근데 운이 좋은 게 아니라 정말 강해서 이런 걸 어떡합니까. 안 그러냐, 쉔?”

샤오 쉔이 엄청난 속도로 고개를 끄덕였다.

「맞습니다! 형님은 최고십니다!」

“녀석. 훌륭한 아부의 표본이로구나.”

“…….”

주거니 받거니 하는 우리의 모습에 최 팀장이 고개를 절레절레 저었다.

“뭐요.”

“아닙니다. 하긴, 이래야 진태경 씨답긴 하죠.”

뭐지, 묘하게 기분 나쁘게 들리는데.

어깨를 으쓱한 나는 샤오 쉔을 향해 물었다.

“그보다 본부 쪽은?”

「아, 그렇지 않아도 전투 시작 전에 연락을 취했습니다.」

연락을 취했다는 건, 휘하에 있는 헌터 몇 명을 미리 보내 놨다는 뜻이다.

요즘 같은 세상에 전령(傳令)이 웬 말이냐 싶겠지만, 어쩔 수 없다. 마법으로 통신과 위성 감시가 불가능한 상황이니 죽어라 뛰거나 차량을 이용하는 수밖에.

그래도 조명탄을 포함한 여러 문물이 있으니 다행이다.

“또 한참 걸리겠군.”

「뒤따라오는 중이었으니 그리 오래 걸리지는 않을 겁니다.」

“피곤하겠지만 천막이라도 쳐서 애들 쉬게 해. 금방 끝나긴 했어도 전투 끝나면 진이 쏙 빠진다.”

「대형 몬스터 정도는 우리 쪽에서 처리해 놔야 하지 않을까요? 아무래도 본부가 옮기기에는 힘들 것 같아서…….」

“그것도 맞는 말이긴 하지.”

본부란 우리와 함께 움직이는 군 병력을 말한다.

나를 포함한 공안 무력부 소속 헌터들이 선봉에서 몬스터를 무찌르면, 뒤따라온 군 병력이 해당 지역과 몬스터 사체들을 ‘청소’하는 방식이었다.

굳이 청소라고 표현하는 이유는 그 목적이 부산물 노획이 아니기 때문이다.

이건 말 그대로 청소다. 내가 맡은 서부 전선의 군대는 죽은 몬스터들이 언데드로 부활할 수 없도록 사체를 토막 내고, 후방으로 옮기는 역할을 가장 많이 했다.

「저어, 형님.」

“응, 왜?”

「그간 부끄러워서 말씀드리지 못했었는데…… 현재 몇몇 고위 장교들 사이에서 이런저런 말이 나오고 있는 것 같습니다.」

“말? 무슨 말?”

샤오 쉔이 내 눈치를 살피며 조심스럽게 속삭였다.

「그, 본인들이 맡은 역할에 불만이 조금…….」

“……?”

저게 도대체 무슨 소리지.

샤오 쉔의 말을 이해하기까지는 제법 긴 시간이 필요했다. 무거운 침묵이 흐른 뒤, 나는 설마 하는 마음으로 입술을 뗐다.

“혹시 자기들도 몬스터 사체 그만 치우고 공을 세우고 싶다. 뭐 그런 거야?”

「……예.」

“아니, 이런 미친 새끼들을 봤나.”

쌍욕이 절로 튀어나오는 상황이다. 다른 전선에서는 군인들이 하루가 멀다고 죽어 나가는데, 몬스터 사체 치우기가 지겹다니.

가만히 듣고 있던 최 팀장이 침착하게 입을 열었다.

“당황하지 마십시오. 짱깨가 짱깨 했을 뿐입니다.”

저게 천 명에 가까운 중국인들 앞에서 할 소린가 싶지만, 중국인과 짱깨는 엄연히 다른 인종이다.

착한 중국인의 대표인 샤오 쉔의 얼굴은 어느새 부끄러움으로 붉어져 있었다.

「죄, 죄송합니다. 다만 장교들 전부는 아니고, 일부 인원들이 그런 불만을 품은 것으로 알고 있습니다.」

“일부 인원들이라. 그렇겠지. 그런데 한 가지 궁금한 게 있는데…….”

나는 눈살을 찌푸리며 샤오 쉔의 어깨너머를 가리켰다.

“그 일부 인원에, 저기 오는 저 인간도 포함되어 있냐?”

저 멀리, 백여 대의 장갑차와 전차가 먼지구름을 일으키며 이곳을 향해 다가오고 있었다.



* * *



드르륵, 덜컹!

황폐해진 도로를 달리는 차량이 위아래로 들썩인다. 앉아 있는 군용 차량의 창밖으로 엉망이 된 논과 밭, 무너진 민가가 드문드문 보이기 시작했다.

뒷정리가 끝난 후 나는, 아니 ‘우리’는 인근 소도시로 향하는 중이었다.

「하하, 정말 고생 많았소이다. 진 선생!」

꽉 조인 벨트로도 감출 수 없는 뱃살. 태양 아래 번쩍이는 정수리.

입고 있는 군복과 견장에 박힌 별 세 개가 아니었다면, 내가 눈앞의 장년인과 만날 일은 없었을 것이다.

「안 그래도 오늘 아침 상부에 연락이 닿았소. 진 선생의 승전보에 유엔 안보리는 물론이고 전 세계가 난리가 났어요! 내 무슨 소리인지는 모르겠지만, 한국에서는 오늘을 주모 기일이라 부른다던데…….」

시종일관 떠들어 대는 헛소리를 듣는 건 여기까지다. 나는 참지 못하고 불쑥 입을 열었다.

“주모가 뒤졌는지 살았는지, 그런 건 관심 없고요. 하나만 물어봐도 됩니까?”

「지, 진 선생?」

중국 정식 편제로는 청두군구(成都軍球). 그중에서도 일곱 개의 사단, 여단이 속한 제 13집단군 총사령관인 랴오 상장은 불안한 눈빛으로 날 바라봤다.

「왜, 왜 이러시오? 무슨 일이라도 있었소?」

“오늘 제가 이상한 이야기를 들어서요. 지금 좀 예민해졌네요.”

「누가 감히 진 선생의 심기를! 뭐든 물어보시오.」

“아, 예. 제가 여쭤볼 건 다름이 아니고…….”

나는 기름기로 번들거리는 랴오 상장의 얼굴을 빤히 바라보며 말을 이었다.

“공을 세우고 싶은 몇몇 장교들의 불만이 상당하다던데…… 혹시 알고 계셨나 해서요.”

「크흠.」

알고 있었군. 그걸 알면서도 가만히 놔뒀다니. 하도 어이가 없으려니 이제는 오히려 덤덤해진다.

그래도 명색이 아군이자 타국의 쓰리스타. 나는 최대한 침착하고 공손한 어조로 물었다.

“그 씨팔 새끼들 면상 좀 볼 수 있습니까?”

「크흐흠!」

“아니 시부럴 거, 어떤 정신 나간 놈들이 이 시국에 공을 세우고 싶다고 지랄을 해요. 막말로 지들이 나가서 싸울 것도 아니고, 일반 병사들 앞에 세우고 뒤에서 지휘봉이나 휘두를 거 아닙니까.”

「크흐흐흠!」

“몬스터 사체 치우기 귀찮다는 게 무슨 개소립니까. 왜요, 하도 보니까 정겹고 친근해져서 본인들도 사체가 되고 싶대요? 진짜 뒈져 봐야 정신을 차리지. 개 같은 거.”

「크흐흐흐흠!」

“그런 새끼들 있으면 그냥 와서 말하라고 해요. 장비 입혀서 선봉에 세워 줄 테니까. 고기 방패로 쓰면 딱이겠…….”

열변을 토하던 나는 문득 입을 닫았다. 랴오 상장의 이마에서 식은땀이 스프링클러처럼 쏟아지는 중이었다.

「…….」

“…….”

이 인간도 그 정신 나간 놈 중에 하나구만.

지하 벙커에서 핵을 쏘니 마니, 염병을 할 때부터 보통 미친놈은 아니구나 싶었는데. 정말 상당한 수준으로 미쳐 있는 게 분명하다.

“……장군님. 제정신입니까?”

「그, 그러니까 이게. 우리도 뭔가를 보여 줘야 한다. 뭐 그런 게 조금은…….」

“아니, 피해 없이 쭉쭉 잘 가고 있는데 여기서 뭘 더 보여 줘요. 헌터들이 앞에서 길 뚫고, 군대는 뒤에서 뒷수습하면서 민간인들 구하고. 잘하고 있는데 뭘 더 보여 주냐고.”

우두둑.

손가락 관절을 꺾는 내 모습에 랴오 상장이 황급히 손을 내저었다.

「어, 어허! 우리 서로 간에 반말은 하지 맙시다. 내 연배로 보나 계급으로 보나, 진 선생에게 이런 대접을 받을 사람이 아니오.」

“아주 그냥, 대접으로 대가리를 깨 버릴까.”

「뭐, 뭣이?」

“아닙니다. 잘못 들으신 거예요. 어쨌든 알겠고, 허튼 생각하지 마십시오. 지금부터는 사상자는 최소로, 민간인들 구출하면서 천천히 진격하자고요. 아시겠습니까?”

「…….」

이 인간 반응이 왜 이래?

대답 대신 눈깔을 뒤룩뒤룩 굴리는 랴오 상장을 보는 순간, 등골이 서늘해졌다.

설마…….

“이미 명령을 내린 겁니까?”

「그, 그게. 내가 지금 군납 비리 건에 연루되어 있기도 하고. 독자적으로 뭔가를 해내야 하는 시점이라…….」

“야 이 개새끼야!”

쾅!

내 발길질에 방탄 처리 되어 있는 문짝이 뜯겨 나갔다. 앞 좌석에 앉아 있던 운전병이 황급히 브레이크를 밟았다.

끼이이익!

“히익!”

잔뜩 몸을 웅크린 채 벌벌 떨던 랴오 상장이 더듬거리는 목소리로 대답했다.

「우, 우리가 지금 가고 있는 소도시에 몬스터가 있을 것 같아서 예비대로 운용 중이던 공안 무력부 헌터들을 조금 투입시켰…….」

더 들을 필요도 없었다. 내가 뭐라 다그치기도 전에, 어느새 가까워진 도시로부터 굉음이 울려 퍼졌으니까.

콰아아앙!

거대한 폭발. 솟구치는 불꽃과 연기.

그리고…….

띠링.

돌발 퀘스트를 알리는 시스템 알림이 있었다.
```

## Current accepted English baseline

```markdown
# Chapter 390

Whoosh!

Where the blade force swept past, hot blood spurted as heads sprang into the air.

I stepped on the ogre’s body as it collapsed like a bundle of straw and sprang high into the air. The sunlight touching the back of my neck was warm.

*Perfect weather for a fight.*

It was noon. The location was a wasteland without a single tree.

With the sun at my back, my shadow fell across the midst of the thousand or so monsters gathered below—even the spearhead in it slashing downward as I dove.

*Heavenly Strike.*

Boom!

The Flame Dragon’s Claw raked across the earth.

The roar sounded as if the sky itself had split apart. The ground sank several meters, sending dirt and fragments of stone flying in every direction.

A vortex of hot air that erupted at the center of the battlefield became a blade and swept through the monsters.

Boom!

Ding. Ding. Ding…

Through my dust-clouded vision, green blood poured down in rapid splatters as System notifications announced the monsters’ deaths.

I waved my hand lightly, scattering the dust cloud. The monsters staring at me with blank faces came into view.

“Chirrik?”

“Krrk?”

Their eyes seemed to ask what the hell had just happened. I drew in a deep breath, then shouted with my internal energy behind my voice.

“Wipe them out—!”

And then—

“Waaaaaaah!”

With an earsplitting roar, more than a thousand Hunters who had rushed in by then descended on the monster army like a wave.

Crack-crack-crack!

Wham!

Watching the monsters crumble helplessly, I became certain of one thing.

*We’ve won this battle.*

The farming was over. Now it was time to harvest.

I headed toward the Twin-Headed Ogre that looked like the boss monster.

For the sake of my precious EXP. No—for the sake of minimizing our casualties.

“That one’s the leader! Ranged units!”

“Hey, hey! Hands off! I’ll take care of it, so don’t touch a single hair on its head!”

I swear to heaven, I had not a shred of ulterior motive.

…

Well, after thinking about it, I didn’t need to swear.

“Insidious human. Your intention to claim the byproducts is painfully obvious. You didn’t conceal your greed even while slaughtering my legion!”

“Shut up and do your job. Hurry up and start making your kind kill each other as undead.”

“I was going to do that anyway. Grow, my sea of skeletons… Huh?”

“What’s wrong?”

“Why isn’t my power working? Is this perhaps a bug?”

“…”

“Where did you even pick up a word like that?”

The Skeleton Warlord, whose modernization was progressing by the day, spoke in a dejected voice.

“The farther inside I go, the stronger the Arch Lich’s control seems to become. Ah, a commander without a legion. Truly, I cannot contain my grief. At this rate, I might as well be dead!”

“…”

What the hell did this guy think he was?

I was tired of telling him that he was already dead. Sighing inwardly, I charged at the leader.

* * *

“It’s a crushing victory! Another crushing victory!”

Shao Shen shouted with a flushed face. We had seen this scene more than ten times by now, so Team Leader Choi and I had reached the point where we simply took it in stride.

*Well, I can understand why he’s excited.*

It had taken barely two hours to annihilate an army of more than a thousand monsters.

And we had finished without a single death. It really was a victory worth commemorating. In a situation like this, acting calm would be stranger.

“Our casualties are only twenty-three seriously wounded and thirty lightly wounded. Ah, this is really…!”

Shao Shen trembled like a dog desperate to pee and stared at me with shining eyes.

“How can this happen every time?”

“Hmm. Maybe it’s because I’m strong.”

Team Leader Choi gave me a slightly incredulous look.

“Why?”

“Usually, this is when people say something modest, like that they were lucky.”

“Usually, yes. But it’s not that I’m lucky. I’m genuinely strong. What else can I do? Isn’t that right, Shen?”

Shao Shen nodded at tremendous speed.

“That’s right! Hyung-nim is the best!”

“Good lad. You’re a fine specimen of flattery.”

“…”

Team Leader Choi shook his head as he watched us trade lines back and forth.

“What?”

“Nothing. Though I suppose this is very much like you, Mr. Jin Taekyung.”

Somehow, that sounded vaguely insulting.

I shrugged and turned to Shao Shen.

“More importantly, what about headquarters?”

“Ah, yes. I contacted them before the battle began.”

Contacting them meant that he had sent several Hunters under his command ahead of us.

In this day and age, sending messengers seemed ridiculous, but there was no choice. Magic had made communication and satellite surveillance impossible, so we either had to run ourselves or use vehicles.

At least we still had things like signal flares.

“It’ll take a while.”

“They were already following us, so it shouldn’t take too long.”

“You’re tired, but put up some tents and let the men rest. The battle ended quickly, but fighting drains you completely.”

“Shouldn’t we take care of the large monsters ourselves? It might be difficult for headquarters to move otherwise…”

“That’s a fair point.”

Headquarters referred to the military forces moving with us.

When Hunters from the Public Security Armed Forces, myself included, defeated the monsters at the front, the military forces following behind would “clean up” the area and the monster corpses.

The reason I called it cleaning was that the purpose wasn’t to collect the byproducts.

It was literally cleanup. The army assigned to my western front spent most of its time chopping up the dead monsters so they couldn’t be resurrected as undead, then transporting the remains to the rear.

“Hyung-nim.”

“Yeah? What is it?”

“I was too embarrassed to mention this before, but… it seems that some of the senior officers have been making various complaints.”

“Complaints? What kind?”

Shao Shen glanced at me and lowered his voice cautiously.

“They’re… somewhat dissatisfied with the roles they’ve been assigned.”

“…”

What the hell was he talking about?

It took me a while to understand Shao Shen’s words. After a heavy silence passed, I finally parted my lips, half expecting the worst.

“Do they want to stop cleaning up monster corpses and earn some merit themselves?”

“…Yes.”

“Are you fucking kidding me?”

The profanity came out on its own. Soldiers were dying every day on the other fronts, and these people were complaining that cleaning up monster corpses was boring.

Team Leader Choi, who had been listening quietly, spoke in a calm voice.

“Don’t be alarmed. The chinks are just being chinks.”

I wondered if that was really something he should say in front of nearly a thousand Chinese people. But Chinese and chinks were, strictly speaking, two entirely different races.

Shao Shen, the model Chinese man, had gone red with embarrassment.

“I-I’m sorry. But I understand that not all the officers are like that. Only some of them have those complaints.”

“Some of them, huh. I’m sure that’s the case. But there’s something I’m curious about…”

I frowned and pointed over Shao Shen’s shoulder.

“Does that include the guy coming over there?”

In the distance, more than a hundred armored vehicles and tanks approached us, raising a cloud of dust.

* * *

Rattle, clunk!

The vehicle bounced up and down as it raced along the ruined road. Through the window of the military vehicle I was sitting in, I began to see ruined rice paddies and fields, along with collapsed houses scattered here and there.

After the cleanup was finished, I—or rather, *we*—were heading toward a nearby small city.

“Ha-ha! You’ve really worked hard, Teacher Jin!”

A belly that even a tightly fastened belt couldn’t conceal. A bald crown gleaming beneath the sun.

If not for the military uniform he wore and the three stars on his shoulder strap, I would never have had any reason to meet the middle-aged man in front of me.

“I contacted the higher-ups this morning, as it happens. The entire world, not to mention the United Nations Security Council, is in an uproar over Teacher Jin’s victory report! I don’t know what they mean, but apparently people in Korea are calling today Jumo’s death anniversary…[^1]

[^1]: *Jumo* is a traditional tavern keeper. Koreans jokingly call for her to serve drinks online when celebrating a national triumph.”

I had reached my limit for listening to his nonstop stream of nonsense. Unable to hold back any longer, I cut in.

“I don’t care whether the tavern lady is dead or alive. Can I ask you one thing?”

“Te-Teacher Jin?”

Under China’s official military structure, this was the Chengdu Military Region. More specifically, the man before me was Senior General Liao, commander-in-chief of the Thirteenth Group Army, which included seven divisions and brigades.

He looked at me anxiously.

“Why, why are you acting like this? Did something happen?”

“I heard something strange today, so I’m a little sensitive right now.”

“Who dared upset Teacher Jin? Ask me anything.”

“Yes. What I wanted to ask is…”

I stared at Senior General Liao’s greasy, glistening face and continued.

“I heard that some officers are extremely dissatisfied because they want to earn merit. Did you know about that?”

“Ahem.”

So he knew.

He had known about it and still done nothing. It was so absurd that I had passed beyond anger and reached a state of numbness.

Still, he was technically an ally and a three-star general from another country, so I asked as calmly and politely as I could.

“Could I see the faces of those fucking bastards?”

“Ahem!”

“What kind of lunatics are throwing a fit about wanting to earn merit at a time like this? To put it bluntly, they aren’t going to fight themselves. They’ll just put ordinary soldiers in front and wave their command batons from behind, won’t they?”

“Ahem! Ahem!”

“What the fuck does it mean that they’re tired of cleaning up monster corpses? What, have they seen so many of them that they’ve grown fond of them and want to become corpses themselves? They’ll have to actually die before they come to their senses. Goddamn it.”

“Ahem! Ahem! Ahem!”

“If there are any of those bastards, tell them to come see me. I’ll equip them and put them in the vanguard. They’d make perfect meat shields—”

I suddenly shut my mouth.

Cold sweat was pouring from Senior General Liao’s forehead like water from a sprinkler.

…

“…”

This man was one of those lunatics too.

I’d suspected he was no ordinary madman ever since he’d kicked up that whole goddamn fuss in an underground bunker over whether or not to launch a nuke. But he was clearly insane on an entirely different level.

“General, are you in your right mind?”

“Well, that is… We also have to show them something. We have to prove that we can do something too…”

“No casualties, everything moving forward smoothly—what more do you want to show them? The Hunters are breaking through the path ahead, while the army is cleaning up behind them and rescuing civilians. We’re doing a good job. What else do you want to show?”

Crack.

I cracked my knuckles. Senior General Liao hurriedly waved his hands.

“Now, now! Let’s not speak informally to each other. Whether you consider my age or my rank, I’m not someone who should be treated this way by Teacher Jin.”

“How about I crack your skull open with a serving bowl?”

“Wh-What?”

“Nothing. You heard me wrong. Anyway, I understand. Don’t entertain any foolish ideas. From now on, let’s advance slowly, minimize casualties, and rescue civilians. Understood?”

“…”

What was wrong with this man’s reaction?

The moment I saw Senior General Liao’s eyes rolling around instead of answering, a chill ran down my spine.

*No way…*

“Have you already issued an order?”

“Well, I’m currently involved in the military procurement corruption scandal too. It’s time for me to accomplish something independently…”

“You fucking bastard!”

Bang!

My kick tore the armored door off its hinges. The driver sitting in the front seat hurriedly slammed on the brakes.

Screech!

“Eek!”

Senior General Liao huddled up and trembled as he answered in a stammering voice.

“I-I thought there might be monsters in the small city we’re heading toward, so I deployed some of the Public Security Armed Forces Hunters who had been held in reserve…”

I didn’t need to hear any more. Before I could press him further, a roar rang out from the city that had suddenly drawn close.

Boom!

A massive explosion. Flames and smoke surged into the sky.

And then—

Ding.

A System notification announced an Unexpected Quest.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 390`.

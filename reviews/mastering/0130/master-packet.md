# Master Edit Task — Chapter 130

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
| 청풍     | **Cheongpung**     |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 마적     | **mounted bandits**                              |                                                       |
| 표국     | **Escort Bureau**                            |
| 표사     | **escort**                                   |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 석칠 | **Seokchil** | Middle-aged porter with nearly twenty years of experience. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 사서삼경 | **Four Books and Three Classics** | Confucian texts used to describe conventional scholarly learning. |
| 은자 | **silver nyang** | Silver currency unit. |
| 은원보 | **silver yuanbao** | Small silver ingot given to Taekyung as pocket money. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

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

# Chapters 125–129

## Plot

The surviving Mount Heng Sword Sect members thank Jin Taekyung, Jin Mukyung, and Hyuk Mujin for saving Lee Seowol and preserving the sect, while formally apologizing for Lee Cheonbaek’s crimes. Taekyung refuses their apology, saying the Jin Family of Taiyuan is the party entitled to receive it. Seowol will visit the Jin Family on New Year’s Day and still awaits Taekyung’s answer to her marriage proposal.

On the journey home, Taekyung examines Pung Yang’s Temporary Strength Pill. It grants enormous temporary power, fifteen years of internal energy, Body-Protecting Qi, and +100 combat-related stats, but its maker, Grade, and price are initially unknown. After Wipeng unconsciously names Dark Heaven, the System identifies it as the pill’s manufacturer. Wikyung and Wipeng refuse to explain Dark Heaven’s identity or connection to the Jin Family.

Wikyung and fifty elite guards arrive at Sakju to retrieve the Jin group. The family celebrates Taekyung, Mukyung, and Hyuk Mujin’s survival, while Mukyung learns that Taekyung possesses the dangerous pill. The group drinks for three days; Wipeng becomes known as the God of Drinking, while Taekyung gains the rumor-based title Night King and additional Fame.

As the Jin group travels onward, Taekyung’s Sleeping Dragon of Shanxi Title strengthens, raising its effects to all stats +15 and Fame +200. He reaches Level 61 with Fame 2,100 (+250) and sixty unspent stat points. Taekyung and Hyuk Mujin deliberately exaggerate their victory over the Red Wind Band, earning public awe and prompting a county magistrate to deliver an invitation from Shanxi’s City Lord.

The ten-year-old City Lord, a Prince and the Emperor’s youngest brother, invites Taekyung to a luncheon with young prodigies. Taekyung intends to refuse, but Hyuk Mujin accepts on his behalf, causing the System to create and lock in The City Lord’s Invitation Quest. Jin Mukyung reveals that he met the City Lord three years earlier and remembers the encounter as a nightmare.

## Continuity

- Pung Yang is dead, the Red Wind Band has been annihilated, and the wider Murim’s response remains unresolved.
- Jin Mukyung survived his battle with Pung Yang but remains incompletely recovered; his chest wound reopened during the drinking gathering.
- Lee Seowol remains the seventeen-year-old Sect Leader of the Mount Heng Sword Sect. Only a small group survived, and the sect’s reconstruction remains uncertain.
- Seowol apologized to the Jin Family through Taekyung, accepted the New Year invitation, offered the sect’s territorial rights, and proposed marriage to Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist. Taekyung intends to reject the proposal because he loves Song Song.
- The Temporary Strength Pill is in Taekyung’s Inventory and is known to Jin Wikyung, Jin Mukyung, and Wipeng. It is a Dark Heaven product restricted to Peak martial artists or higher; it temporarily grants +100 combat-related stats, fifteen years of internal energy, and Body-Protecting Qi at an unspecified price. Its Grade and long-term aftereffects remain unknown.
- Dark Heaven’s identity, purpose, relationship to the Jin Family, and possible connection to the Demonic Cult’s Blood-Exploding Pill remain undisclosed.
- Taekyung fully absorbed the Blazing Flame Divine Pill and possesses forty-five years of internal energy with the Scorching Yang Qi attribute.
- Taekyung is Level 61 with Fame 2,100 (+250), sixty unspent stat points, and a strengthened Sleeping Dragon of Shanxi Title granting all stats +15 and Fame +200.
- Wipeng is called the God of Drinking, and Taekyung is rumored to be the Night King.
- The City Lord’s Invitation Quest has been accepted on Taekyung’s behalf and requires attendance at the City Lord’s luncheon with young prodigies the following day. Its reward depends on the City Lord’s reaction, and rejection may cause him to sulk.
- Shanxi’s City Lord is a ten-year-old Prince, the Emperor’s youngest brother, and a direct member of the Zhu imperial family. He has held the office since age five.
- The current Emperor is rumored to have assassinated his older brother, the Crown Prince, to seize the throne.
- The government and Murim recognize each other’s authority and generally avoid interference; the Jin Family is not yet one of the Nine Sects and One Gang or the Five Great Families and must avoid provoking the government.
- The Fire King’s status remains unknown, and the truth of Jopil’s claim to be the nineteenth-generation successor of the Flame Divine Palm remains unresolved.

## Translation Decisions

- Retain **Peak**, **Supreme Peak**, **Internal Injury**, **Body-Protecting Qi**, **Scorching Yang Qi**, **Red Wind Band**, **Sect Leader**, **Benefactor**, **Taiyuan Jin Family**, **Dark Heaven**, **God of Drinking**, and **Night King**.
- Render 잠력단 as **Temporary Strength Pill**, 폭혈단 as **Blood-Exploding Pill**, 열화신단 as **Blazing Flame Divine Pill**, 만년한철 as **Ten-Thousand-Year Cold Iron**, and 이름 없는 검 as **Unnamed Sword**.
- Render 혈랑검법 as **Blood Wolf Sword Technique**, 혈랑보법 as **Blood Wolf Footwork**, 파천신권 as **Shura Annihilating Fist**, and 절정 무공 as **Peak martial arts**.
- Render 현령 as **county magistrate**, 성주 as **City Lord**, 성주의 초청 as **The City Lord’s Invitation**, 친왕 as **Prince**, 주씨 as **Zhu**, and 태자 as **Crown Prince**.
- Render 구파일방 as **Nine Sects and One Gang** and 오대세가 as **Five Great Families**.
- Render 전서응 as **messenger eagle**, 원단 as **New Year’s Day**, 갑자 as **jiazi**, and 시진 as **shichen**.
- Preserve the Samsung/Samseong pun with a clarifying footnote and retain **Jaringobi** with its explanatory footnote.

### Prior accepted reading-copy tails

#### Chapter 128 tail (verified mastered)

…
at most. And by the time Jin Mukyung and I arrived, fewer than a hundred of them remained. *In reality, there was Pung Yang and maybe seventy mounted bandits who were already exhausted. Something like that.* Well, rumors were usually exaggerated. “Come on, that’s too—” Just as I was about to tell him the truth, murmurs spread through the people who had been listening to my conversation with the county magistrate. “Five hundred? Didn’t the Sleeping Dragon of Shanxi and the Heaven Shaking Sword go there alone?” “Good heavens. The two of them defeated more than five hundred mounted bandits?” “How can human beings be that strong?” Ding. > **System** > > People are looking at you with awe. > > **Fame** rises by 40! “Too what, did you say?” I continued speaking to the bewildered county magistrate. “That’s far too low. In reality, there were nearly six hundred.” “Six hundred!” “My second brother and I took half each.” “Then three hundred each!” “Hmm. More precisely, about 285?” The county magistrate—and even the government troops—gaped at me. “Ooh!” “Two hundred and eighty-five! He even knows the exact number!” Ding. > **System** > > People are looking at you with awe. > > **Fame** rises by 40! This time, Hyuk Mujin whispered to me with an expression usually reserved for looking at a bug. “Do you really want to take it this far?” “Yep.” “What are you going to do if you inflate your achievements for no reason and get caught lying?” “You, Wolhwa, and the Mount Heng Sword Sect just have to keep your mouths shut. So hurry up and back me up.” “I refuse. Hyuk Mujin may not look it, but I’ve lived a truthful life without a single shameful moment before the heavens.” I stared at him in disbelief. “When Jin Mukyung destroyed my pavilion, weren’t you the one who fought assassins that didn’t even exist?” “…” “If you have nothing to say, shut up and watch your expression. My two hundred and eighty… How many was it?” “Two hundred and eighty-five.” “Right. I’ll say you took care of about thirty of them. If you were born with balls, you ought to become Master of the Gatekeeper Pavilion in the Jin Family of Taiyuan at least once in your life. Don’t you think?” “…!” Hyuk Mujin, who had lived a truthful life without a single shameful moment before the heavens, used dazzling verbal footwork to completely win over the county magistrate. The mounted bandits, most of whom had been Second Rate or Third Rate, became First Rate masters to a man—each a Lü Bu astride Red Hare. Pung Yang became an invincible master who could cleave mountains and seas with a single sword strike. *From now on, I’m filtering anything that comes out of this bastard’s mouth.* He was such a skilled liar that even I found myself wondering whether it was true. If even I, the person involved, was confused, there was no hope for anyone else. “…and that was how Pung Yang, the absolute ruler of Gaoyuan, and the vicious Red Wind Band came to meet their end at the Mount Heng Sword Sect.” The moment Hyuk Mujin finished his bullshit—his story, I mean—sighs of disappointment rose from all around us. The county magistrate’s reaction was the most enthusiastic of all. “Whaaaat? How could such a thing happen? The Murim is truly a wondrous yet terrifying place.” Hyuk Mujin swept his gaze over the crowd with melancholy eyes. “A martial brute like me has no fear. Ever since I took up the sword, I’ve lived with death as my companion. But if I have one wish…” “One wish?” “To die by the sword of someone strong. That is all I could ask for.” “…” What a bumper crop of bullshit. Suppressing the urge to smack Hyuk Mujin in the back of the head, I stepped forward. I had already milked the Fame for all it was worth, and there was no reason to keep talking to a potbellied middle-aged man. “Sorry to interrupt, but we’re in a hurry.” The county magistrate, who had been gazing at Hyuk Mujin with dazed eyes as if hypnotized, suddenly came to his senses. “Ah, my apologies. I didn’t mean for this to happen.” “Then did you have some other business?” “Could I meet Great Hero Jin? The Lesser Family Head, I mean.” The county magistrate’s gaze shifted toward the carriage behind me. They couldn’t be seen from outside, but Jin Wikyung, Jin Mukyung, and Wipeng were inside. *Because they were drunk out of their minds.* They were the losers who had been utterly crushed by me in our drinking contest over the past three days. But how could I tell him the truth? Without so much as changing my expression, I lied. “I’m sorry, but he’s currently circulating his qi, so I don’t think he can see you. As you know, County Magistrate, it’s quite dangerous.” “Ah, I see. Then it can’t be helped.” The county magistrate clicked his tongue, then pulled a tightly rolled piece of paper from his sleeve and handed it to me. “What is this?” “An invitation from the City Lord. After hearing about your recent exploits, Young Hero Jin, he seems to have been deeply impressed, so he arranged a gathering with several young prodigies.” Ding. > **System** > > A **Quest** has been created.

#### Chapter 129 tail (verified mastered)

…
on the way to the Mount Heng Sword Sect, yet I hadn’t even seen a government soldier. “That’s…” Jin Wikyung let his voice trail off. Jin Mukyung, who had been silently inhaling his food until then, suddenly blurted, “Because the City Lord is incompetent. No, in this case, is the Emperor incompetent?” The moment he finished speaking, Hyuk Mujin had a fit, while Jin Wikyung and Wipeng deliberately hardened their expressions. “Hey, Mukyung.” “It’s just us here. No one can overhear us. Besides, I didn’t say anything untrue.” “Second Young Master, our family does not yet stand alongside the Nine Sects and One Gang or the Five Great Families. Please refrain from saying anything that could cause trouble.” I asked Jin Mukyung, who reluctantly nodded. “What do you mean, the City Lord is incompetent?” “Do you not know what the word *incompetent* means?” “Should I report you to the authorities for insulting the Emperor?” “Treason gets at least three clans punished. Congratulations, little brother.” *This bastard Jin Mukyung has gotten pretty good with words.* “Do you know who the current City Lord is?” “Kim Chunbae?” “…If you don’t know, just say you don’t know.” He looked at me as if I were a bug, then continued. “The current City Lord of Shanxi has the surname Zhu.” “So?” “What do you mean, *so*? He’s a member of the imperial family. The imperial family!” “Oh, really?” Apparently, this was a Zhu dynasty. In the span of a moment, I had been branded an ignorant fool who didn’t even know the Emperor’s surname. Still, it wasn’t as if this sort of thing had only happened once or twice. I wasn’t even embarrassed anymore. “Fine, I get it. Keep going.” Jin Mukyung let out a deep sigh and continued. “The current City Lord is the Emperor’s youngest brother, and his imperial title is Prince. As a direct member of the imperial family, he stands on a different level from the other City Lords. He’s someone whose invitation we must accept, even if we have to force ourselves, if only to preserve his dignity.” “Oh.” He really was on a different level. Not just an ordinary City Lord, but the Emperor’s brother. An actual king, no less. Born the son of the Son of Heaven and then becoming the younger brother of the Son of Heaven, he hadn’t merely been born with a silver spoon in his mouth. His spoon was made of vibranium. He was the modern North Korean nuclear spoon—and then some. “Then how can someone who’s practically a king be so incompetent? One letter to his brother should get him all the support he needs from above. Are they on bad terms?” “Who knows? I don’t know the details of that family’s affairs, but I doubt they’re particularly close. There are rumors that the current Emperor assassinated the Crown Prince, his immediately older brother, before ascending the throne.” “Talk about a hunger for power.” “People kill over a single dumpling. Imagine what they’d do for the imperial throne.” Jin Wikyung and Wipeng’s mouths fell open, while Hyuk Mujin had another fit. “Your Honor, I didn’t hear anything. I truly know nothing. In fact, I haven’t been able to hear for a long time…” As Hyuk Mujin muttered like a madman, Jin Mukyung smacked him across the back of the head. I asked, “Does he not get any support because he’s on bad terms with the Emperor? Or is he simply lost in wine and women?” “Wine? Women?” Jin Mukyung gave another short laugh. “He’s only ten years old. It’s too early for him to lose himself in wine and women.” “What, ten? You mean a ten-year-old is the City Lord?” “He’s a direct member of the imperial family. With his bloodline, he could become far more than a City Lord.” The System message I’d seen earlier suddenly came to mind. > If you reject the Quest, the City Lord may sulk. I had thought it was ridiculous for a middle-aged man to act so childish, but now that I knew he was a ten-year-old boy, it finally made sense. Wasn’t that the age when even a falling leaf could make you sulk? “What’s even more amusing is that he was first appointed City Lord five years ago.” “…Five years old? That’s insane.” What could a five-year-old possibly know? I could roughly guess why the public order in Shanxi Province had become such a mess. I also understood why Jin Mukyung had said that the Emperor, rather than the City Lord, was more incompetent. This wasn’t some neighborhood corner store. They had put a child in a position that demanded ability and responsibility. There was no way things could run properly. “How do you know all this?” I asked because it was surprising that Jin Mukyung, who had been obsessed with martial arts and nothing else, was so well-informed about current affairs. His answer was unexpected. “Because I’ve met him before. More accurately, I was summoned.” “Oh, really?” “Three years ago.” Well, if I was the rising super rookie of the moment, Jin Mukyung was already an established Peak master. It made sense that he would have been invited before me. “What was he like?” Jin Mukyung looked at me with a strange glint in his eyes. Then, wearing an ominous expression that mixed laughter with irritation, he spoke. “It was fucking awful.”

## Korean source

```text
＃130화



변방의 겨울은 혹독하다. 옷깃을 파고드는 칼바람에 중년 사내가 몸을 부르르 떨었다.

“어흐으, 더럽게 춥네.”

사내, 석칠은 산서성 남부에 있는 성운표국(盛運鏢局)의 쟁자수다.

하루 반나절이 넘게 백 근(斤)이 넘어가는 짐수레를 끌어 온몸이 땀으로 흠뻑 젖었고, 지금처럼 잠시 휴식을 취할 때는 엄청난 한기와 싸워야 했다.

“형님, 짐수레 얼른 놓고 빨리 와서 불이나 좀 쬐시오. 그러다가 얼어 죽겠네.”

어느새 모닥불 앞에 쭈그려 앉은 동료 쟁자수가 말했다. 석칠은 퉁명스럽게 대답하며 걸음을 옮겼다.

“이놈아, 내가 먹여 살려야 할 입이 다섯이다. 죽으려면 한참 멀었어.”

“그렇지. 여우 같은 마누라와 토끼 같은 자식들 생각하면 못 죽지.”

“여우는 무슨. 곰이야, 곰.”

“방금 그거 유언이오? 형수님이 들으면 모가지를 꺾어 버릴 텐데.”

“없는 데서는 나라님 욕도 하는 법이야. 몰라?”

석칠은 모닥불 앞으로 바짝 다가갔다.

말똥을 장작으로 쓰다 보니 고약한 냄새가 사방으로 풍겼지만 이십 년 가까이 쟁자수 일을 해 온 그에게는 밥 짓는 냄새만큼이나 익숙했다.

“어따, 이제야 좀 살겠다.”

“그런데 형님, 너무 야박한 거 아니오?”

“응? 이건 또 무슨 헛소리야?”

동료 쟁자수가 실실 웃으며 턱짓했다.

“신참도 데려오셔야지. 혼자만 살겠다고 냅다 오는 법이 어디 있소?”

꽁꽁 언 손을 녹이던 석칠이 고개를 돌렸다. 그의 시선 끝에 멀뚱멀뚱한 얼굴로 눈 덮인 바위 위에 앉아 있는 한 청년이 보였다.

‘저놈 저거, 또 저러고 있네.’

청년은 하남(下南)에서 새로 구한 쟁자수다. 이번 표행의 책임자인 송 표두에게 듣기로는 그럭저럭 밥값은 할 것 같아 받아 줬다고 한다.

‘뭐, 사람이야 늘 부족하니까.’

문제는 젊은 놈이 대체 무슨 생각을 하는지, 지금처럼 넋 놓고 있을 때가 많다는 거다.

쯧쯧 혀를 차는 석칠에게 동료 쟁자수가 물었다.

“왜요, 좀 이상한 놈입니까?”

“일은 잘해. 보기보다 힘이 장사더라고.”

“그럼 됐지, 뭘.”

“되긴 뭐가 돼. 젊은 놈이 허구한 날 저러고 있으니 답답해서 그렇지. 나 때는 말이야…….”

“풍운의 꿈을 품고 하루하루 열심히 살았다고 말하고 싶은 거요?”

“그럼, 사내라면 원대한 목표를 세우고 나아갈 줄 알아야지.”

“그 원대한 목표라는 게 천하제일의 쟁자수는 아니었을 테고.”

“이 자식이 아까부터.”

발끈하는 석칠의 반응에 동료 쟁자수가 화제를 돌렸다.

“그런데 저 친구, 이름이 뭐요?”

“청풍(淸風).”

“아따, 이름 한번 멋있네. 잘 어울리기도 하고.”

“그건 그래.”

청년, 청풍을 내심 못마땅하게 생각하던 석칠이지만 그 말에는 십분 공감했다.

서글서글한 인상과 맑은 눈동자를 보고 있노라면 이상하게 마음이 편안해지고 화도 가라앉았다.

“이보게, 신참!”

동료 쟁자수의 말에 청풍이 고개를 돌렸다.

“저요?”

“그럼 여기 신참이 자네 말고 누가 있나? 이쪽으로 와서 불이나 좀 쬐게. 거기 앉아 있다가는 궁둥이가 뜯어져 나갈걸.”

“그런 경험도 나쁘지 않죠.”

“경험? 무슨 경험?”

“엉덩이가 뜯겨 나가는 경험이요. 제가 한 번도 그래 본 적이 없어서.”

잠깐 말이 없던 동료 쟁자수가 석칠에게 속삭였다.

“저거 뭐 하는 놈입니까?”

“몰라, 애가 좀 이상해. 뭘 잘못 먹었나 봐.”

청풍이 고개를 갸웃했다.

“아침에 만두 두 개 먹었는데요.”

“……귀가 밝구먼. 알았으니까 와서 앉기나 하게.”

“그럴까요?”

터벅터벅 걸어온 청풍이 모닥불 앞에 앉자 으레 하는 질문들이 날아들었다.

“어디서 왔나?”

“하남에서요.”

“하남 사람이었군.”

“한 달 전에는 호북에 있었고요.”

“음. 호북도 좋지.”

“그전에는…….”

쟁자수가 석칠에게 말했다.

“골 때리네.”

“그렇지? 이야기하다 보면 나까지 이상해지는 기분이라니까.”

“어떻게 이런 놈을 옆에 끼고 달포씩이나 버티셨소?”

“그래서 요즘 말 안 걸어. 마지막으로 대화한 게 사흘쯤 됐나?”

청풍이 진지한 얼굴로 대답했다.

“나흘 하고도 세 시진이요.”

“…….”

“…….”

두 사람은 청풍의 머리통을 한 대 쥐어박고 싶은 마음을 간신히 억눌렀다.

“그래서 어디 사람인가?”

“산에서 살았어요.”

“내 말은 그게 아니고…… 아닐세, 그거라도 대답해 줘서 고맙네.”

“별말씀을요.”

해맑게 웃는 청풍의 모습을 보니 신기하게도 화가 수그러든다.

종잡을 수 없는 엉뚱한 언행에 아이처럼 순수한 웃음. 난생처음 보는 별종에 관한 호기심이 이어졌다.

“한데, 산에서 살았다니?”

“말 그대로예요. 어릴 때부터 산에서 농사도 짓고, 약초도 캐고. 그 외에도 이것저것 하면서 살았거든요.”

두 사람은 청풍이 화전민 출신임을 지레짐작했다.

화전민 중 대부분은 악질 지주의 횡포를 못 견뎌서, 혹은 크고 작은 죄를 지어서 관의 눈을 피해 산으로 들어갔다.

“고생이 많았겠군.”

“전 재밌었는데요?”

“아, 그래?”

화전민 생활이 재미있을 수가 있나? 순간 석칠의 머릿속에 그런 생각이 스쳤지만, 굳이 물어볼 필요를 느끼진 못했다.

“그럼 하산(下山)하게 된 계기는 뭔가?”

“산속 생활이 심심해져서요. 세상 구경도 하고 싶고, 만나고 싶은 사람도 있었거든요.”

“그래서 하남에 온 거로군.”

“네. 어쩌다 보니 헛걸음을 하게 됐는데…… 지금도 나쁘지 않아요. 표행이란 것도 상당히 재밌어요.”

“표행이 재미있다고?”

청풍이 활짝 웃으며 대답했다.

“사람 구경하는 것도 재밌고, 땅도 보고, 하늘도 보고. 생각하는 것도 재밌어요.”

오랜 세월 쟁자수 일을 해 온 석칠에게는 이젠 지긋지긋한 광경이다.

피곤과 생계에 대한 고민으로 찌들어 있는 사람들, 축축한 땅과 미친 듯이 불어오는 칼바람. 머릿속엔 그저 이번 표행으로 얼마의 수당을 받을지만 꽉 차 있다.

‘하긴, 아직 젊으니까 할 수 있는 소리지.’

더군다나 평생 산에서 살아온 화전민 출신이니 그럴 법도 하다.

곧 냉정한 현실을 알게 되고 점차 나이를 먹으면 자신과 같은 모습이 되어 가지 않을까?

‘나도 저럴 때가 있었는데.’

석칠은 부러움과 안타까움이 섞인 눈빛으로 청풍을 바라보다가 입을 열었다.

“그냥 헛소리라고 생각하고 듣게.”

괜한 오지랖인 건 알지만, 이 순박한 청년에게 현실을 알려 주고 싶었다.

쟁자수로 시작해서 쟁자수로 늙어 죽기에는 너무 창창한 인생 아닌가.

“할 만한 것도 잠깐이야. 십 년, 이십 년쯤 되면 미래가 잘 보이지 않는다 이 말일세. 쟁자수는 아무리 날고 기어 봐야 쟁자수거든. 차라리 동네 무관(武關)에서 삼류 무공이라도 배워서 표사로 시작하게. 그편이 훨씬 나아.”

청풍은 눈을 깜빡였다.

“아, 그래요?”

“그래요, 가 아니고 그렇게 하란 소리야. 무공을 익히기에는 늦은 나이지만 혹시 아나? 의외로 무재가 뛰어나서 잘나가는 일류 고수가 될지.”

“일류 고수…….”

가만히 듣고 있던 동료 쟁자수가 혀를 찼다.

“거, 너무 헛바람 불어넣는 거 아니오? 일류 고수가 뉘 집 개 이름도 아니고.”

“말이 그렇다는 거야, 말이. 저 나이에 쟁자수로 만족한다는 게 말이 돼?”

“뭐, 그건 그렇죠. 나도 십 년만 젊었으면 여기서 안 이러고 있지.”

“거봐.”

석칠이 청풍의 어깨를 두드렸다.

“들었지? 일이 년만 알뜰하게 모아서 무관 등록 하는 게 훨씬 나아. 그때까진 내가 옆에서 잘 알려 줌세.”

청풍이 고개를 갸웃했다.

“일이 년이요?”

“왜, 너무 긴가? 자네가 세상 물정을 몰라서 그런가 본데, 무관비가 한두 푼 하는 게 아니야. 아무리 적게 잡아도 일 년은…….”

“아뇨, 제가 그 전에 관둘 거라서.”

“관둔다고? 언제?”

“지금이요.”

“응?”

“엥?”

청풍이 해맑게 웃었다.

“제가 산서성까지 가는 길을 몰라서요. 마침 산서로 가는 표행이 있길래 끼워 달라고 한 건데요.”

“……그래서?”

“이제 하루만 더 가면 태원(太元)이니까 이쯤에서 헤어지려고요.”

석칠과 동료 쟁자수는 이게 뭔가 싶은 얼굴로 서로를 마주 보았다.

“저놈 뭐야? 송 표두 말로는 일 년짜리 계약서에 수결(手決)했다고 하지 않았나?”

“나도 그렇게 알고 있소. 그러니까 최고참인 형님한테 배우라고 붙여 놓은 거였고.”

석칠이 혼란스러운 표정으로 청풍에게 물었다.

“자네, 하남에서 합류할 때 뭔가에 수결했었지?”

“앗, 네.”

“그거 갖고 있으면 줘 봐.”

청풍이 품에서 누리끼리한 죽간 하나를 꺼내어 보여 줬다.

앞으로 일 년간 성운표국에서 쟁자수로 일할 것이며, 도중 이탈 시 위약금을 문다는 내용의 계약서였다.

“글은 읽을 줄 알지?”

“네 살 때 사서삼경을 땠지요.”

“그딴 헛소리는 하지 말고. 거기 읽어 봐. 그래, 그 부분. 소리 내서 크게.”

청풍이 또랑또랑한 목소리로 석칠이 알려 준 부분을 읽어 내려갔다.

“수결 시 번복할 수 없으며, 무단이탈 시 은자 오십 냥의 위약금 혹은 그에 상응하는 대가를 치르게 될 것.”

“은자 오십 냥이 얼마인지는 알 테고. 그에 상응하는 대가라는 게 무슨 뜻인지 아나?”

곰곰이 생각에 잠겨 있던 청풍이 이마를 탁 쳤다.

“혹시 몸으로 때우라는?”

“그래, 이 멍청한 친구야. 표국이 무슨 무골호인들만 모여 있는 곳인 줄 알았어?”

석칠은 혈압이 올라 뒷덜미가 당겼다. 이놈의 머릿속에 뭐가 들어 있는지 정수리를 쪼개 보고 싶을 정도였다.

‘어떻게 이런 놈이 다 있지? 산에서만 살아서 그런가?’

천하를 가로지르며 물건을 운송할 때 겪는 위험은 상상을 초월한다. 마적, 수적, 산적, 온갖 도적 떼와 경쟁 표국의 견제까지.

행여 그 모든 장애물을 넘어도 자연재해 한 번 잘못 만나면 표행은 실패로 돌아간다.

어지간한 무림 문파만큼, 아니 그 이상으로 철저하고 거친 것이 표국이었다.

‘그런데 수결까지 찍어 놓고 뭐? 이쯤에서 헤어지겠습니다?’

눈앞의 이 젊은 놈은 세상을 몰라도 너무 모른다.

석칠은 애먼 목숨 구한다는 마음으로 입을 열었다.

“혹시나 해서 말해 두는데, 도망칠 생각은 일찌감치 접게. 그냥 일 년 동안 돈 번다 생각하고 일하란 말이야. 알겠나?”

“일 년은 너무 긴데요. 내일 하루까지는 일할 수 있을 것 같은데.”

“야, 이 새끼야!”

“형님, 형님 진정하십쇼! 괜히 송 표두가 보기라도 하면 피곤해져요.”

“놔! 안 놔?”

석칠의 눈이 뒤집힌 그때였다.

“어, 이 정도면 위약금으로 충분하지 않나요?”

쩔그럭.

청풍이 내민 손을 확인한 두 사람이 눈을 부릅떴다.

말발굽 모양의 그것은 눈보다 새하얀 은빛으로 번쩍거리고 있었다.

“은, 은원보(銀元寶)?”

“그것도 두 개나!”

은자 오십 냥에 해당하는 은원보가 무려 두 개.

은자 백 냥은 일개 쟁자수가 십 년간 뼈 빠지게 일해도 벌기 힘든 엄청난 거금이다.

그런 거금이 화전민 청년의 품에서 나올 줄이야.

“어, 어, 어, 어떻게.”

“집 나오면서 노잣돈을 좀 받았거든요.”

청풍의 천진난만한 대답에 두 사람은 입을 딱 벌렸다.

도대체 어느 집 자제길래 은자 백 냥을 노잣돈으로 준단 말인가. 심지어 소불알처럼 축 늘어진 전낭을 보니 저게 끝이 아닌 듯했다.

“일단 위약금은 이걸로 해결할 수 있을 것 같은데…….”

두 사람은 미친 듯이 고개를 끄덕였다.

“됩니다. 되고 말고요.”

“왜 갑자기 존댓말을 쓰세요?”

“그냥 이게 편해서 그럽니다.”

“맞습니다. 세상에서 제일 편합니다.”

“아, 그러시다면야 뭐.”

신기하다는 듯 두 사람을 바라본 청풍이 은원보 두 개를 건넸다.

“전 이만 가 볼게요. 이건 위약금이라고 전해 주세요.”

“이, 이걸 다 말입니까?”

“너무 많은데…….”

“남으면 두 분이 나눠 쓰세요. 제가 돈 쓰는 법을 잘 몰라서. 따뜻한 옷이라도 하나씩 사 입으세요. 비싼 털가죽 달린 걸로.”

“……!”

주섬주섬 봇짐 하나를 둘러메고 떠나려는 청풍의 모습에 석칠이 황급히 입을 열었다.

“호, 혹시 성함이?”

“청풍이요. 보름 전까지는 하남 사람이었고, 지난달에는 호북, 그전에는 섬서에 살았죠.”

대답을 마친 청풍은 태원을 향해 성큼성큼 걷기 시작했다.

하늘을 푸르렀고, 축축한 땅 위로는 때 이른 새싹이 돋아나고 있었다.

“이번 봄은 좀 일찍 오려나?”

그는 활짝 웃으며 생각했다. 이번 봄에도 매화가 흐드러지게 피었으면 좋겠다고.

문득 얼마 전 몰래 뛰쳐나온 화산(華山)의 연화봉(蓮花峰)이 생각났다.
```

## Current accepted English baseline

```markdown
# Chapter 130

Winter in the borderlands was harsh. A middle-aged man shivered violently as the knife-sharp wind cut through his collar.

“Ugh, it’s cold as hell.”

The man, Seokchil, was a porter for the Seongun Escort Bureau in southern Shanxi Province.

He had spent more than a day and a half hauling a cart loaded with over a hundred geun of cargo, soaking his entire body in sweat. Whenever he took a brief rest, as he was now, he had to fight against the brutal cold.

“Hyung, hurry up and leave the cart. Come warm yourself by the fire before you freeze to death.”

A fellow porter, already crouched in front of the campfire, called out. Seokchil answered gruffly as he walked over.

“Brat, I have five mouths to feed. I’ve got a long way to go before I’m ready to die.”

“True. You can’t die when you’ve got a fox of a wife and rabbit-like children waiting for you.”

“What do you mean, fox? She’s a bear. A bear.”

“Was that a deathbed confession? If your wife hears you, she’ll wring your neck.”

“You can curse the king behind his back. What, you didn’t know that?”

Seokchil moved closer to the campfire.

They used horse manure for firewood, so a foul smell spread in every direction. But after nearly twenty years as a porter, Seokchil was as used to it as he was to the smell of cooking rice.

“Ah, now I feel like I can live again.”

“But Hyung, aren’t you being a little stingy?”

“Huh? What kind of nonsense is this?”

His fellow porter grinned and jerked his chin toward something.

“You should bring the rookie over, too. Where’s the sense in rushing over here to save yourself alone?”

Seokchil, who had been warming his frozen hands, turned his head. At the end of his gaze sat a young man on a snow-covered rock, staring blankly into space.

*That kid’s doing it again.*

The young man was a new porter they had picked up in Henan. Escort Chief Song, the person in charge of this escort run, had said that the young man seemed capable enough to earn his keep, so they had taken him on.

*Well, people are always in short supply.*

The problem was that the young man often sat around like this, completely lost in thought, and no one had the slightest idea what was going on inside his head.

As Seokchil clicked his tongue, his fellow porter asked,

“Why? Is he a little strange?”

“He does his work well. He’s surprisingly strong for someone who doesn’t look like much.”

“Then what’s the problem?”

“What do you mean, what’s the problem? It’s frustrating seeing a young fellow sit around like that every day. Back when I was his age…”

“You want to say you had dreams of making your mark on the world and worked hard every day?”

“Of course. A man should know how to set a grand goal and move toward it.”

“I assume that grand goal wasn’t becoming the greatest porter under heaven.”

“You little—”

At Seokchil’s furious reaction, his fellow porter quickly changed the subject.

“By the way, what’s that fellow’s name?”

“Cheongpung.”

“Wow, what a great name. It suits him, too.”

“That’s true.”

Seokchil secretly disliked the young man, Cheongpung, but he had to agree completely.

There was something about the young man’s open, gentle features and clear eyes that made people feel strangely at ease and calmed their anger.

“Hey, rookie!”

At his fellow porter’s shout, Cheongpung turned his head.

“Me?”

“Who else would I be talking to? Come over here and warm yourself by the fire. If you keep sitting there, your butt will get ripped right off.”

“An experience like that wouldn’t be bad.”

“An experience? What experience?”

“The experience of having my butt ripped off. I’ve never had that happen before.”

His fellow porter was silent for a moment before whispering to Seokchil,

“What kind of guy is he?”

“I don’t know. The kid’s a little strange. Maybe he ate something bad.”

Cheongpung tilted his head.

“I ate two dumplings this morning.”

“……You’ve got sharp ears. Fine, just come sit down.”

“Should I?”

Cheongpung trudged over and sat down in front of the fire. The usual questions immediately began flying at him.

“Where are you from?”

“Henan.”

“So you’re from Henan.”

“I was in Hubei a month ago.”

“Hmm. Hubei’s nice, too.”

“Before that…”

The porter turned to Seokchil.

“This guy’s unbelievable.”

“Right? I feel like I’m becoming strange myself whenever I talk to him.”

“How have you lasted over a month with someone like him beside you?”

“That’s why I stopped talking to him lately. Has it been about three days since our last conversation?”

Cheongpung answered with a serious expression.

“Four days and three shichen.”

“……”

“……”

The two men barely managed to suppress their urge to smack Cheongpung over the head.

“So where are you from?”

“I lived in the mountains.”

“That’s not what I meant… No, never mind. Thank you for answering that, at least.”

“You’re welcome.”

Strangely, Cheongpung’s bright smile made their anger subside.

His unpredictable, bizarre remarks were paired with an innocent smile like a child’s. Their curiosity about this strange young man, unlike anyone they had ever seen, continued to grow.

“But you said you lived in the mountains?”

“I mean exactly what I said. I farmed and gathered medicinal herbs in the mountains from the time I was young. I did various other things, too.”

The two men jumped to the conclusion that Cheongpung was from a slash-and-burn farming community.

Most slash-and-burn farmers went into the mountains to escape the cruelty of vicious landlords or to avoid the authorities after committing one crime or another.

“You must have had a hard life.”

“But I had fun.”

“Oh, really?”

Could life as a slash-and-burn farmer really be fun? The thought briefly crossed Seokchil’s mind, but he saw no reason to ask.

“Then what made you come down from the mountain?”

“Life in the mountains got boring. I wanted to see the world, and there were people I wanted to meet.”

“So that’s why you came to Henan.”

“Yes. It turned out to be a wasted trip, but… things aren’t bad now, either. This escort work is pretty interesting, too.”

“You find escort work interesting?”

Cheongpung answered with a broad smile.

“Watching people is interesting. Looking at the land and the sky is interesting, too. Thinking is fun.”

To Seokchil, who had worked as a porter for so many years, these were all sights he was sick to death of seeing.

People worn down by exhaustion and worries about making a living. Damp earth and knife-sharp winds that blew like mad. His mind was filled with only one thought: how much pay he would receive for this escort run.

*Well, he’s still young. That’s the only reason he can say something like that.*

Besides, he had lived in the mountains his entire life and came from a slash-and-burn farming community. It made sense that he would feel this way.

Wouldn’t he learn about the harsh realities of life soon enough and gradually become just like Seokchil as he grew older?

*I used to be like that, too.*

Seokchil looked at Cheongpung with a mixture of envy and pity before opening his mouth.

“Just listen to this as the ramblings of an old man.”

He knew he was meddling where he wasn’t wanted, but he wanted to show this innocent young man the realities of life.

Wasn’t his life too promising to begin and end as a porter?

“Anything seems worthwhile for a while. But after ten or twenty years, you stop seeing much of a future ahead of you. No matter how hard a porter works or how talented he is, he’s still a porter. You should learn even Third Rate martial arts at a local martial arts academy and start working as an escort. You’d be much better off.”

Cheongpung blinked.

“Oh, really?”

“Not ‘oh, really?’ I’m telling you to do it. You’re a little old to start learning martial arts, but who knows? Maybe you have exceptional talent and could become a successful First Rate master.”

“A First Rate master…”

His fellow porter, who had been listening quietly, clicked his tongue.

“Isn’t that giving him too much false hope? A First Rate master isn’t some dog’s name.”

“I’m speaking hypothetically. What kind of sense does it make for someone his age to be satisfied with being a porter?”

“Well, you’re right about that. If I were ten years younger, I wouldn’t be sitting here either.”

“See?”

Seokchil patted Cheongpung on the shoulder.

“You heard him, right? Save carefully for a year or two and enroll in a martial arts academy. It’ll be much better for you. Until then, I’ll teach you everything I know.”

Cheongpung tilted his head.

“A year or two?”

“What? Is that too long? You don’t know how the world works, so I suppose you don’t realize that martial arts academy fees aren’t cheap. Even if you take the lowest estimate, it’ll take a year to…”

“No, because I’m going to quit before then.”

“You’re quitting? When?”

“Now.”

“Huh?”

“What?”

Cheongpung smiled brightly.

“I don’t know the way to Shanxi Province. There happened to be an escort run heading to Shanxi, so I asked them to let me tag along.”

“……And?”

“We’ll reach Taiyuan after one more day, so I was planning to part ways around then.”

Seokchil and his fellow porter looked at each other with expressions that seemed to ask whether this was some kind of joke.

“What the hell? Didn’t Escort Chief Song say he signed a one-year contract?”

“That’s what I heard, too. That’s why they assigned him to the most experienced porter, so he could learn from him.”

With a confused expression, Seokchil asked Cheongpung,

“When you joined us in Henan, you signed something, didn’t you?”

“Oh, yes.”

“If you have it, show it to me.”

Cheongpung pulled a yellowish bamboo slip from inside his clothes and showed it to them.

It was a contract stating that he would work as a porter for the Seongun Escort Bureau for one year and pay a penalty if he left before then.

“You can read, right?”

“I finished studying the Four Books and Three Classics when I was four.[^1]”

“Don’t say stupid things like that. Read this part. Yes, that section. Read it aloud, and make sure I can hear you.”

In a clear voice, Cheongpung read the section Seokchil pointed out.

“Once signed, this contract cannot be revoked. In the event of unauthorized departure, the signer shall pay a penalty of fifty nyang of silver or provide compensation of equivalent value.”

“You know how much fifty nyang of silver is, right? Do you know what ‘compensation of equivalent value’ means?”

Cheongpung thought deeply for a moment, then slapped his forehead.

“Does it mean I’d have to work it off?”

“That’s right, you idiot. Did you think the Escort Bureau was full of nothing but kindhearted saints?”

Seokchil’s blood pressure rose, and the back of his neck began to ache. He wanted to split the top of this kid’s skull open and see what was inside.

*How can someone like this even exist? Is it because he only ever lived in the mountains?*

The dangers of transporting goods across the land were beyond imagination. Mounted bandits, river bandits, mountain bandits, every kind of bandit gang imaginable, not to mention interference from competing Escort Bureaus.

Even if they overcame all those obstacles, one encounter with a natural disaster could bring an escort run to failure.

An Escort Bureau was every bit as thorough and hard-edged as most Murim sects, if not more so.

*And this kid signed the contract, then says what? “I’m leaving around here”?*

The young fool in front of him knew far too little about the world.

Seokchil spoke, determined to keep the boy from throwing his life away.

“I’m telling you this just in case, so give up on running away right now. Work for a year and think of it as earning money. Understand?”

“A year is too long. I think I can work until tomorrow, though.”

“You little bastard!”

“Hyung, Hyung, calm down! If Escort Chief Song happens to see this, we’ll all be in trouble.”

“Let go! I said let go!”

It was just then, as Seokchil was about to snap.

“Uh, wouldn’t this be enough to cover the penalty?”

Clink.

The two men’s eyes widened when they saw what Cheongpung held out.

The object was shaped like a horse’s hoof and gleamed with a silver light whiter than the snow.

“Is that a silver ingot?”

“And there are two of them!”

There were two silver ingots, each worth fifty nyang of silver.

A hundred nyang of silver was an enormous sum that an ordinary porter would struggle to earn even after working himself to the bone for ten years.

And yet such a fortune had come from the clothes of a young man from a slash-and-burn farming community.

“H-how?”

“I was given some traveling money when I left home.”

At Cheongpung’s innocent answer, both men’s mouths fell open.

What kind of family gave their son a hundred nyang of silver as traveling money? And judging from the money pouch hanging limp like a bull’s testicles, this didn’t seem to be all he had.

“At least it looks like the penalty can be settled with this…”

The two men nodded frantically.

“It can. Of course it can.”

“Why did you suddenly start speaking formally?”

“It’s just more comfortable this way.”

“Exactly. It’s the most comfortable thing in the world.”

“Oh. If that’s what you prefer.”

Cheongpung looked at the two men as if they were strange and handed over the two silver ingots.

“I’ll be going, then. Please tell them this is the penalty.”

“A-are you really giving us both?”

“It’s too much…”

“If there’s any left over, you two can split it. I don’t really know how to spend money. Buy yourselves some warm clothes. Something with expensive fur on it.”

“……!”

As Cheongpung slung a bundle over his shoulder and prepared to leave, Seokchil hurriedly spoke.

“C-could I ask your name?”

“Cheongpung. Until half a month ago, I was from Henan. Last month, I lived in Hubei, and before that, I was in Shaanxi.”

After answering, Cheongpung began walking steadily toward Taiyuan.

The sky was blue, and early shoots were already sprouting from the damp earth.

“Maybe spring will come a little early this year.”

He smiled brightly as he thought about it. He hoped the plum blossoms would bloom in profusion again this spring.

Then, without warning, he thought of Lotus Peak on Huashan, from which he had secretly run away not long ago.

[^1]: The Four Books and Three Classics are foundational Confucian texts.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 130`.

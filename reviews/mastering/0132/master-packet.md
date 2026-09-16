# Master Edit Task — Chapter 132

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
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 은인     | **Benefactor**                               |
| 레벨               | **Level**                      |
| 산서     | **Shanxi**             |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 메구미 | **Megumi** | Japanese name used in Taekyung's joke about the abbreviated dish name. |
| 산니백육 | **Garlic Pork** | Boiled pork sliced thin and served with garlic sauce. |
| 어향육사 | **Fish-Fragrant Shredded Pork** | Shredded pork dish. |
| 경장육사 | **Beijing Sauce Shredded Pork** | Shredded pork dish. |
| 규화계 | **Beggar's Chicken** | Named inn dish. |
| 매구 | **Maegu** | Waiter's shortened name for Maechae Guyuk. |
| 매채구육 | **Maechae Guyuk** | Pork belly with preserved mustard greens; the abbreviation is explained in a footnote. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 호승심 | polysemy | Competitive pride or fighting spirit; not merely a desire to test oneself. | test myself |
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

#### Chapter 130 tail (verified mastered)

…
to be an escort run heading to Shanxi, so I asked them to let me tag along.” “…And?” “We’ll reach Taiyuan after one more day, so I was planning to part ways around then.” Seokchil and the other porter exchanged baffled looks. “What the hell? Didn’t Escort Chief Song say he signed a one-year contract?” “That’s what I heard, too. That’s why they assigned him to you, the most experienced porter, so he could learn from you.” With a confused expression, Seokchil asked Cheongpung, “When you joined us in Henan, you signed something, didn’t you?” “Oh, yes.” “If you have it, show it to me.” Cheongpung pulled a yellowish bamboo slip from inside his clothes and showed it to them. It was a contract stating that he would work as a porter for the Seongun Escort Bureau for one year and pay a penalty if he left before then. “You can read, right?” “I finished the Four Books and Three Classics when I was four.[^1]” “Don’t say stupid things like that. Read this part. Yes, that section. Read it aloud, and make sure I can hear you.” Cheongpung read the section Seokchil indicated in a crisp voice. “Once signed, this contract cannot be revoked. In the event of unauthorized departure, the signer shall pay a penalty of fifty silver nyang or provide compensation of equivalent value.” “You know how much fifty silver nyang is, right? Do you know what ‘compensation of equivalent value’ means?” Cheongpung thought deeply for a moment, then slapped his forehead. “Does it mean I’d have to work it off?” “That’s right, you idiot. Did you think the Escort Bureau was full of nothing but kindhearted saints?” Seokchil’s blood pressure shot up, making the back of his neck throb. He wanted to crack open the top of the kid’s skull and see what was inside. *How can someone like this even exist? Is it because he only ever lived in the mountains?* The dangers of transporting goods across the land were beyond imagination. Mounted bandits, river bandits, mountain bandits, every kind of bandit gang imaginable, not to mention interference from competing Escort Bureaus. Even if they overcame every one of those obstacles, a single natural disaster could doom an escort run. An Escort Bureau was every bit as thorough and hard-edged as most Murim sects, if not more so. *And this kid signed the contract, then says what? “I’m leaving around here”?* The young fool in front of him knew far too little about the world. Seokchil spoke, determined to keep the boy from throwing his life away. “I’m telling you this just in case, so give up any thoughts of running away. Work for a year and think of it as earning money. Understand?” “A year is too long. I think I can work through tomorrow, though.” “You little bastard!” “Hyung, Hyung, calm down! If Escort Chief Song happens to see this, we’ll all be in trouble.” “Let go! I said let go!” It was just then, as Seokchil was about to snap. “Uh, wouldn’t this be enough to cover the penalty?” Clink. The two men’s eyes widened at what Cheongpung held out. The object was shaped like a horse’s hoof and gleamed with a silver light whiter than the snow. “S-silver yuanbao?” “And there are two of them!” Two silver yuanbao, each worth fifty silver nyang. A hundred silver nyang was an enormous sum that an ordinary porter would struggle to earn even after working himself to the bone for ten years. And yet such a fortune had come from the clothes of a young man from a slash-and-burn farming community. “H-how…?” “I was given some traveling money when I left home.” Both men’s mouths fell open at Cheongpung’s innocent reply. What kind of family gave their son a hundred silver nyang as traveling money? And judging from the money pouch hanging limp like a bull’s testicles, this didn’t seem to be all he had. “At least it looks like this should cover the penalty…” The two men nodded frantically. “It can. Of course it can.” “Why did you suddenly start speaking formally?” “It’s just more comfortable this way.” “Exactly. It’s the most comfortable thing in the world.” “Oh. If that’s what you prefer.” Cheongpung looked at the two men as if they were strange and handed over the two silver yuanbao. “I’ll be going, then. Please tell them this is the penalty.” “A-are you giving us both?” “It’s too much…” “If there’s anything left over, you two can split it. I don’t really know how to spend money. Buy yourselves some warm clothes. Something with expensive fur.” “…!” As Cheongpung slung a bundle over his shoulder and prepared to leave, Seokchil hurriedly called after him. “C-could I ask your name?” “Cheongpung. Until half a month ago, I was from Henan. Last month, I lived in Hubei, and before that, I was in Shaanxi.” With that, Cheongpung strode off toward Taiyuan. The sky was blue, and early shoots were already sprouting from the damp earth. “Maybe spring will come a little early this year.” He smiled brightly as he thought about it. He hoped the plum blossoms would bloom in profusion again this spring. Then, without warning, he thought of Lotus Peak on Huashan, from which he had secretly run away not long ago. [^1]: The Four Books and Three Classics are foundational Confucian texts.

#### Chapter 131 tail (verified mastered)

…
who lingered around her stall. After a childhood of hardship and years of grueling effort, the boy finally found success and returned as a strapping young man. It was a story I had heard somewhere before, but that didn’t make it any less moving. “Ahem. What is this? Did something get in my eye?” Was it yellow dust or fine dust? They couldn’t have built any factories yet, so it must have been yellow dust. That was when the rims of my eyes reddened slightly despite myself. “So, have you gone to see your parents?” “Not yet. I was thinking of stopping by today or tomorrow.” “Go see them soon. Didn’t your family move?” “Moved? Where?” “To a large estate along the main road over there. They even released koi into the pond and raised them.” “Oh, really?” “…?” Parents? Moving? A huge estate with koi? Wait. Something wasn’t right. I stared dumbfoundedly at Hyuk Mujin as he returned carrying the candied hawthorn skewers. “What was that about?” “Huh? About what?” “Your parents are alive?” Hyuk Mujin stared at me as though I were insane. “Why are you killing off my perfectly healthy parents?” “No, that’s not what I meant… Then what was all that stuff you said earlier?” “What stuff?” “The candied hawthorn. You said you couldn’t have any and spent every day sucking on your fingers.” “I couldn’t have any. My parents wouldn’t let me eat it because they said it would rot my teeth. Every merchant around here knew how overbearing my parents were, so they made a point of refusing to sell any to me. That lady was the only one who secretly slipped me some.” “…” “And what about being jealous of the children holding their parents’ hands?” “My family’s business was so successful that they never had any free time. I played by myself.” “Th-then you had family in Taiyuan, but you didn’t come back once in five years?” “I left home. I didn’t want to inherit the family business, so I left a single letter behind and ran away. The Master of the Gatekeeper Pavilion in our family is my father’s childhood best friend, so he probably knew everything about how I was doing.” “…” “For about two years, they gave me hell over it. Then my youngest sibling was suddenly born, so I no longer needed to inherit the family business. After that, they stopped saying much.” Hyuk Mujin craned his neck and looked around, then raised a hand and pointed. “Ah, there it is. See it? That building belongs to my parents… It got even bigger while I was away.” I followed Hyuk Mujin’s finger and turned my head. A huge, towering five-story pavilion and a signboard bearing enormous characters came into view. **Hyuk Family Textile Shop** Hyuk Mujin smiled proudly. “It’s the largest textile shop in Taiyuan. We have branches in Henan and Hebei, too.” *This bastard was born with a silver spoon, too…* You had to be pretty damn wealthy to open chain stores in a place this rough. *What the hell have I been doing?* A young boy who used to suck on his fingers because he wanted to eat candied hawthorn so badly? The truth was that his successful business-owner parents had forbidden him from eating it because they were worried about his teeth. *What the fuck is this?* As I stood there with my mouth hanging open, Hyuk Mujin held out one of the candied hawthorn skewers. “Here, have one. I specially chose the biggest and shiniest one. The ones that lady sells are the best in this area.” “You son of a…” I swallowed the curse that had surged up to my throat and bit down on the candied hawthorn with a loud crunch. “Let’s hurry up and find a room.” “Already? We’ve only spent a few iron coins…” “Hey! Is it your money? Those are travel expenses we were given to spend when necessary. Expenses!” “Didn’t you just say we should spend it all and have fun?” “We’ve had enough fun. You said the rooms would fill up after sunset. If we get a bad night’s sleep and end up late to tomorrow’s luncheon, are you going to take responsibility?” “…” * * * Honghwa Inn. As its signboard suggested, this was one of the establishments under the Lower District Sect’s influence. *Honghwaru at night. Honghwa Inn for lodging.* Whoever had come up with that arrangement was clearly determined to wring every last coin out of the drunks. “Let’s go in.” I was about to lead Hyuk Mujin, whose lower lip had been jutting out for some time, toward the inn’s entrance when someone spoke. “Excuse me. I’m sorry to bother you.” The voice strangely tugged at my nerves. Its owner was a young man with an affable expression and a dreamy, hazy voice as innocent as a child’s. *This feeling…* The moment I turned around and met his clear eyes, my breath caught despite myself. This was an aura different from Jin Mukyung’s. > **System** > > **Level:** ??? > **Name:** Cheongpung Another Peak master had appeared. Amid the tension, the young man named Cheongpung opened his lips. “If you don’t mind, may I eat just one candied hawthorn skewer?” “…?” *What the hell is this guy?* [^1]: Candied hawthorn skewers are a traditional snack made by coating skewered fruit in hardened sugar.

## Korean source

```text
＃132화



“실례가 안 된다면 빙당호로 하나만 먹어도 되겠습니까?”

예상을 뛰어넘는 멘트에 순간 뇌정지가 왔다.

‘이게 뭔 소리야.’

도를 아십니까도 아니고, 빙당호로 하나만 먹어도 되겠냐니.

처음 만난 절정 고수가 세상에서 가장 정중한 말투로 빙당호로를 구걸하는 상황은 내 계획에 없었는데.

꼬르륵.

이제는 배꼽시계로 측은지심까지 자극한다. 나는 엉겁결에 아직 들고 있던 빙당호로를 내밀었다.

“여, 여기요.”

“감사합니다, 은인.”

빙당호로 가성비 보소, 만난 지 10초 만에 절정 고수의 은인이 됐다.

애들이나 먹을 법한 사탕 과자를 맹렬하게 물고 빠는 청년, 청풍의 모습을 나와 혁무진이 멍하니 지켜봤다.

“조장님, 아는 사람이에요?”

“아니.”

빙당호로 하나를 게 눈 감추듯 먹어 치운 청풍은 아직 모자란지 굶주린 맹수의 눈빛으로 혁무진을 바라봤다.

정확히는 녀석의 양손에 들린 빙당호로 두 개를.

“……무진아.”

“네?”

“드려라.”

혁무진이 재빨리 손을 뒤로 감췄다.

“싫습니다.”

“싫어?”

“예, 저 이거 오 년 만에 처음으로 먹는 겁니다. 아직 입도 안 댔어요.”

“그렇구나. 우리 무진이가 예상 수명보다 오십 년 정도 일찍 죽고 싶구나.”

“…….”

한숨을 푹 내쉰 녀석이 빙당호로를 내밀자 청풍의 눈이 번쩍 빛났다.

“감사합니다, 은인!”

다음 순간, 휙 하는 바람 소리와 함께 빙당호로가 청풍의 손으로 옮겨 갔다.

“으헉.”

실로 엄청난 속도다. 헛숨을 들이킨 혁무진이 내게 떨리는 목소리로 속삭였다.

“보, 보통 거지가 아닌데요?”

눈앞의 꾀죄죄한 청년이 절정 고수라는 사실을 알면 무슨 표정을 지을까?

나는 정신없이 빙당호로를 흡입 중인 청풍을 유심히 살폈다.

‘절정 고수라기에는 너무 젊어 보이는데.’

나도 지금까지 주워들은 풍문이 있다. 명문 대파에서 온갖 영재 교육과 지원을 쏟아부어도 가물에 콩 나듯 탄생하는 것이 절정 고수라는 사실도 이제는 안다.

천하에서도 변방 촌구석 취급받는 산서성 출신인 진무경이 유명해진 이유도 그 때문이다.

남들보다 10년, 20년을 앞서 절정의 경지에 올랐으니까.

‘그런데…….’

기껏해야 내 또래로 보이는 녀석이 기감으로도 레벨을 파악하지 못하는 절정 고수라니.

산서성에 저렇게 젊은 절정 고수가 있다는 말은 들어 본 적이 없다.

‘이런 놈이 어디서 튀어나온 거지?’

때마침 청풍이 고개를 들었다. 허겁지겁 먹은 터라 입가에는 끈적끈적한 설탕이 한가득 묻어 있었다.

“휴우, 잘 먹었습니다.”

“배가 좀…… 많이 고프셨나 보네.”

“네. 하루 종일 굶었거든요.”

“저런, 어쩌다가?”

“여비를 잃어버리는 바람에 그만. 그래도 재미있는 경험을 했네요.”

“…….”

돈 없어서 온종일 쫄쫄 굶은 게 재밌는 경험이 될 수 있나?

처음 만난 그 순간부터 느낀 거지만 확실히 사고방식이 특이한 놈이다.

청풍이 해맑게 웃으며 꾸벅 포권을 취했다.

“아, 제 소개가 늦었네요. 은인들께 청풍이 인사 올립니다.”

“진태경이라고 합니다.”

“전 이분의 오른팔이자 심장, 혁무진입니다.”

혁무진의 헛소리를 깔끔하게 무시하고 청풍을 주시했다.

내가 이래 봬도 나름 산서성에서는 유명 인사다.

몇 달 전까지만 해도 나쁜 쪽으로, 지금은 정반대의 이유로 산서성에서 내 이름을 모르는 사람이 없다.

‘알아보려나?’

은근히 기대감을 품은 그때, 청풍의 얼굴이 딱딱하게 굳었다.

“저, 혹시…….”

“네, 맞습니다. 제가 바로 그.”

“실례가 안 된다면 좀 더 신세 져도 될까요?”

“예?”

“제가 좀 오래 굶어서.”

때맞춰 청풍의 배에서 천둥 같은 소리가 흘러나왔다.

꼬르륵.

“……그럼 같이 식사라도.”

“감사합니다, 은인!”

이게 은인인지 호구인지 모르겠다.



* * *



홍화객잔의 내부는 이른 저녁 식사를 하러 온 사람들로 바글거렸다.

발 빠르게 달려온 점소이가 몇 안 되는 빈자리로 우리를 안내해 주었다.

“음식은 뭘로 드릴깝쇼?”

나는 나무로 제작된 무림식 메뉴판을 청풍에게 건네줬다.

“드시고 싶은 거 시키세요.”

“아앗, 아닙니다. 제가 은혜도 모르는 금수(禽獸)도 아니고 어찌…….”

“괜찮으니까 드시고 싶은 거 시키세요.”

“그럼 여기 있는 거 전부 주세요.”

“…….”

이런 금수 같은 놈을 봤나.

대형 호구의 등장에 주방만 바빠졌다. 얼마 지나지 않아 주문한 음식들이 쉬지 않고 줄줄이 쏟아져 나왔다.

“산니백육(䔉泥白肉) 나왔습니다. 이 음식은 삶은 돼지고기를 얇게 포를 떠서…….”

“오.”

“어향육사(魚香肉絲) 나왔습니다. 돼지고기를 죽순, 목이버섯 등과 함께…….”

“오오.”

“경장육사(京醬肉絲)입니다.”

“오오오!”

“규화계(叫花鷄).”

“오오오오!”

처음에는 열심히 설명해 주던 점소이의 말이 점점 짧아지는 것과 달리, 청풍의 리액션은 갈수록 풍부해졌다.

끊임없이 탁자를 채워 가는 요리. 슬슬 음식을 놓을 자리가 없어질 때쯤 점소이가 현자 타임이 온 듯한 얼굴로 새로 나온 접시를 슥 내밀었다.

“매구.”

“매구?”

옆 동네 섬나라 사는 메구미는 알아도 매구는 처음 들어 본다. 내 시선에 점소이가 귀찮다는 듯이 대답했다.

“매채구육(梅采拘肉)이요.”

“…….”

이제는 하다 하다 줄임말까지 쓰는구나.

내가 어이없어하는 사이 청풍은 빠르게 음식 접시를 비워 나가고 있었다.

“우걱, 우걱.”

“천천히 드세요. 천천히.”

“아히헤호. 하후이흡히하.”

“……대답하지 말고 그냥 드세요.”

“캉사합히하!”

혁무진이 입맛이 뚝 떨어진 얼굴로 속삭였다.

“진짜 거지 아닙니까?”

“아까 빙당호로 낚아채는 거 못 봤어? 절대 아니야.”

“쿰척, 쿰척!”

“……아마도 아닐 거야.”

“혹시 압니까, 개방(丐幫)의 고수일지도.”

“개방이라.”

무협 소설에서 질리도록 많이 봤다. 실제로 현 무림에도 구파일방(九派一幇) 중 하나로 버젓이 존재한다.

아직 만나 보지는 못했지만, 당장 저기 객잔 입구에서 어슬렁거리는 거지 중 하나가 개방도일 수도 있다.

“제가 매듭 있나 살짝 확인해 볼까요?”

개방의 고수들은 허리의 매듭으로 신분을 구별한다던가?

나는 고개를 저었다.

‘아니, 일단 개방 소속은 아니야.’

그렇다면 내 이름을 들었을 때 어떻게든 반응이 왔을 거다. 같은 정파 소속이니 일부러 모른 척할 이유도 없고.

‘그럼 어느 문파 출신이지?’

이렇게 젊은 절정 고수가 하늘에서 뚝 떨어졌을 리는 없다.

최소한 이름난 문파 출신일 텐데……. 갈수록 이 수수께끼의 청년에 대한 호기심이 샘솟는다.

“꺼윽, 잘 먹었습니다.”

마침내 식사를 끝마친 청풍이 올챙이배를 두드리다가 나와 혁무진을 보고 멈칫했다.

“다 처음 먹어 보는 음식이라 은인들 앞에서 추태를 보였습니다. 제가 너무 과하진 않았는지…….”

이미 충분히 과했어, 인마.

그래도 최소한의 자각이라도 있어서 다행이다.

“괜찮습니다. 저도 가끔 그러는데요 뭘.”

“저랑 통하는 구석이 있으시네요. 하하.”

나는 청풍을 따라 웃으며 입을 열었다. 이제 슬슬 호구 조사를 시작할 타이밍이다.

“그런데 다 처음 먹어 보는 음식이라니, 평소에 기름진 음식을 잘 안 드시는 모양이네요.”

청풍이 침울하게 고개를 내저었다.

“안 먹는 게 아니라 못 먹었어요. 이렇게 맛있는 음식들이 있는 걸 알았다면 좀 더 일찍 하산했을 텐데.”

“아아, 산에 사셨구나. 많이 힘드셨겠네.”

“산 생활이요? 재밌어요. 경치도 좋고, 여기저기 먹을 것도 많고요. 저희 할아버지도 산에서 평생 혼자 사셨는걸요.”

“할아버님이요?”

“예. 그런데 저어…….”

“말씀하세요.”

“술 좀 시켜도 될까요? 제가 아직 술을 못 먹어 봐서.”

“……얼마든지 시키세요.”

이 자식은 못 먹어 본 것도 많네.

그래도 한 줄기 양심은 남아 있는지 가장 값싼 화주 한 병을 시킨다.

잠시 후, 화주를 거침없이 들이킨 청풍이 약간 붉어진 얼굴로 중얼거렸다.

“으아, 이게 취한다는 거구나. 그런데 우리가 무슨 얘기를 하고 있었죠?”

“할아버님께서 산에서 평생 혼자 사셨다는 것까지.”

“아, 맞다. 아무튼, 저도 어릴 때부터 할아버지랑 같이 살았어요. 그게 다섯 살 때부터니까, 벌써 십오 년이나 됐네요.”

“그래요? 진짜 오래됐네.”

나는 놀란 티를 내지 않으려고 애썼다.

불과 약관에 절정 고수라니. 최소한 진무경에 버금가거나 그 이상 가는 천재란 소리다. 이야기를 나눌수록 그의 정체가 점점 궁금해졌다.

“거기가 어디예요? 그렇게 살기 좋은 곳이면 나중에 한번 놀러 가 볼까 하는데.”

뭔가 말하려던 청풍이 순간 멈칫했다.

“어어, 그건 말씀 못 드릴 것 같은데.”

“에이, 그 정도도 말 못 해 줘요?”

“왜냐하면, 할아버지가 엄청나게 싫어하셔서…… 안 그래도 그것 때문에 일 년에 한두 번씩은 거처를 옮기시거든요.”

“거처를 옮겨요?”

“네. 자꾸 이상한 사람들이 찾아와서요.”

이상한 사람들이라니. 진상 등산객인가?

하긴, 산에 사는 사람한테는 불편할 만도 하겠다.

그가 추억에 잠긴 눈으로 말을 이었다.

“제가 열 살 때였는데, 어느 날 수십 명이 우르르 찾아와서 행패를 부리는 거예요. 할아버지께서 산에 불 질러 버리기 전에 꺼지라고 소리치시던 기억이 나요.”

“아, 그래서 계속 거처를 옮기시는……?”

“네, 다행히 산이 넓어서 십 년째 잘 피해 다니고 계세요.”

“…….”

십 년씩이나? 그 할아버지도 대단한 양반이다.

그때 청풍의 이야기를 흥미진진하게 듣고 있던 혁무진이 물었다.

“그럼 공자께서는 왜 하산하신 겁니까?”

아쉬운 듯이 술병 주둥이를 쪽쪽 빨던 청풍이 대답했다.

“십봉룡(十鳳龍) 때문에요.”

“십봉룡? 그건 또 뭐야?”

내 물음에 혁무진이 별 이상한 놈 다 본다는 눈빛으로 대답했다.

“조장님이 십봉룡을 왜 몰라요?”

“모를 수도 있지, 인마.”

“엥? 작년에 기루에서 술 푸지게 먹고 십봉룡이 될 거라고 떠들었다가 개망신당했으면서.”

“그건 내가 아니라…… 됐다. 그래서 십봉룡이 뭔데?”

“진심으로 몰라서 물어보시는 겁니까?”

“모르면 안 되냐?”

“당연히 안 되죠. 당장 이공자님이 십봉룡인데.”

어, 진짜?

눈을 깜빡거리는 내게 혁무진이 열변을 토했다.

“정파 무림 최고의 후기지수들! 차기 무림을 이끌어갈 용과 봉황들! 십봉룡을 모른다는 게 말이나 됩니까?”

“야, 야. 목소리나 줄여. 사람들 쳐다보잖아.”

그냥 하는 말이 아니라 혁무진의 쩌렁쩌렁한 외침 때문에 주위 손님들이 우리를 힐끗거리는 중이다.

“쳐다보면 뭐 어때요. 이건 조장님이 해도 너무하잖아요! 사람 놀립니까, 예?”

“사람 놀리는 건 모르겠고, 때리는 건 잘해.”

“제가 너무 흥분한 것 같네요. 죄송합니다.”

순식간에 이성을 되찾은 혁무진을 뒤로하고 청풍을 향해 사람 좋은 미소를 지어 보였다.

“말씀 계속하시죠.”

“별건 아니에요. 순간적으로 치기 어린 생각이 들었던 거죠.”

청풍이 살짝 풀린 눈으로 나를 응시했다. 굳이 공력으로 취기를 몰아내지 않을 생각인지 여전히 살짝 알딸딸한 모습이다.

“나와 저들 중에 누가 더 강할까? 저는 그 의문에 대한 답을 확인하고 싶었어요.”

결국은 무인의 호승심(好勝心) 때문이라는 거다.

새로운 세상으로 나아가고픈 마음, 강자를 꺾어 자신의 무공을 입증하고픈 마음이 그의 발걸음을 산 아래로 이끌었음을 짐작할 수 있었다.

‘저런 생각을 해도 될 만큼의 실력도 있는 것 같고.’

진무경은 약관에 절정의 경지에 올라 중원을 떠들썩하게 만들었다고 했다. 그랬던 그는 지금 십봉룡, 정파 최고의 후기지수 중 한 사람으로 꼽힌다.

눈앞의 청풍은 최소 진무경에 비견할 만한 무재(武才)의 소유자다.

‘그럴 만한 자격이 있어.’

내심 고개를 끄덕이던 그 순간이었다.

“푸하하하!”

“큭, 크큭. 아, 웃음 참느라 혼났네.”

소리의 근원지를 향해 고개를 들었다.

2층. 비단옷을 걸친 다섯 명의 남녀가 얼굴 가득 비웃음을 띤 채 우리를 내려다보고 있었다.
```

## Current accepted English baseline

```markdown
# Chapter 132

“If it wouldn’t be too much trouble, may I have just one candied hawthorn skewer?[^1]”

[^1]: Candied hawthorn skewers are a traditional Chinese snack made by coating skewered fruit in hardened sugar.

The unexpected comment caused my brain to freeze for a moment.

*What the hell is he talking about?*

It wasn’t one of those *Do you know the Way?* pitches. He was asking if he could have just one candied hawthorn skewer.

I hadn’t planned for a Peak master I’d just met to beg for candied hawthorn in the most polite tone in the world.

*Grrrrrrowl.*

Now he was even tugging at my pity with his stomach clock. Without thinking, I held out the candied hawthorn skewer I was still holding.

“H-here.”

“Thank you, Benefactor.”

Talk about value for money. Ten seconds after meeting him, I had become a Peak master’s Benefactor.

Hyuk Mujin and I stared blankly at Cheongpung as he ferociously bit and sucked on the candy-coated snack children usually ate.

“Captain, do you know him?”

“No.”

Cheongpung devoured the candied hawthorn skewer as though it had vanished in the blink of an eye. Apparently, it hadn’t been enough, because he turned toward Hyuk Mujin with the eyes of a starving beast.

More precisely, he stared at the two candied hawthorn skewers in Mujin’s hands.

“…Mujin.”

“Yes?”

“Give them to him.”

Hyuk Mujin quickly hid his hands behind his back.

“No.”

“You don’t want to?”

“Yes. This is the first time I’ve eaten these in five years. I haven’t even taken a bite yet.”

“I see. Our Mujin wants to die fifty years ahead of schedule.”

“…”

With a deep sigh, he held out the candied hawthorn skewers. Cheongpung’s eyes flashed.

“Thank you, Benefactor!”

The next moment, accompanied by a sharp *whoosh*, the candied hawthorn skewers had transferred into Cheongpung’s hands.

“Gah!”

That was an incredible speed. Hyuk Mujin sucked in a startled breath and whispered to me in a trembling voice.

“He’s not an ordinary beggar, is he?”

What kind of expression would Mujin make if he learned that the filthy young man in front of us was a Peak master?

I studied Cheongpung as he inhaled the candied hawthorn with single-minded focus.

*He looks far too young to be a Peak master.*

I had heard a few rumors by now. I also knew that even famous, powerful sects with every kind of genius training and support only produced a Peak master once in a blue moon.

That was why Jin Mukyung, who had come from Shanxi Province—a remote backwater even by the standards of the Central Plains—had become so famous.

*He reached the Peak realm ten or twenty years ahead of everyone else.*

*But…*

The young man in front of me looked barely my age, yet he was a Peak master whose Level I couldn’t even determine through Qi Sense.

I had never heard of a Peak master this young living in Shanxi Province.

*Where the hell did this guy come from?*

As if on cue, Cheongpung raised his head. Since he had eaten so hurriedly, his mouth was covered in sticky sugar.

“Whew. That was delicious.”

“You must’ve been a little… very hungry.”

“Yes. I haven’t eaten all day.”

“Oh dear. How did that happen?”

“I lost my travel expenses. Still, it was an interesting experience.”

“…”

Could being forced to starve all day because you had no money really count as an interesting experience?

I had felt it from the moment we met, but this guy definitely had a peculiar way of thinking.

Cheongpung smiled brightly and gave us a respectful fist-and-palm salute.

“Ah, I’m late introducing myself. Cheongpung offers his greetings to his Benefactors.”

“My name is Jin Taekyung.”

“I’m this man’s right arm and heart, Hyuk Mujin.”

I completely ignored Hyuk Mujin’s nonsense and kept my eyes on Cheongpung.

I might not look it, but I was fairly famous in Shanxi Province.

Until a few months ago, I had been famous for all the wrong reasons. Now, for the exact opposite reasons, there wasn’t a single person in Shanxi Province who didn’t know my name.

*I wonder if he’ll recognize me.*

Just as I was secretly getting my hopes up, Cheongpung’s face went stiff.

“Excuse me, are you perhaps…”

“Yes, that’s right. I’m the very—”

“Would it be all right if I imposed on you a little longer?”

“What?”

“I’ve been hungry for quite a long time.”

Right on cue, a thunderous sound came from Cheongpung’s stomach.

*Grrrrrrowl.*

“…Then why don’t we have a meal together?”

“Thank you, Benefactor!”

I couldn’t tell whether I was his Benefactor or just a sucker.

* * *

The inside of Honghwa Inn was packed with people who had come for an early dinner.

A quick-footed waiter led us to one of the few remaining empty tables.

“What’ll it be?”

I handed the wooden menu board to Cheongpung.

“Order whatever you want.”

“Oh, no, I couldn’t. I’m not some ungrateful beast who doesn’t know how to repay a kindness. How could I…”

“It’s fine. Order whatever you want.”

“Then I’ll have everything on here.”

“…”

What an ungrateful beast.

The appearance of a colossal sucker kept the kitchen busy. Before long, the dishes we had ordered began pouring out without pause.

“Garlic Pork is here. This dish is made by slicing boiled pork thin and…”

“Oh.”

“Fish-Fragrant Shredded Pork is here. It’s pork served with bamboo shoots, wood ear mushrooms, and…”

“Ohhh.”

“Beijing Sauce Shredded Pork.”

“Ohhhh!”

“Beggar’s Chicken.”

“Ohhhhh!”

Unlike the waiter, whose explanations had grown shorter and shorter, Cheongpung’s reactions were becoming more and more elaborate.

Dish after dish continued filling the table. Just as there was barely any room left, the waiter pushed out another plate with the expression of a man who had reached enlightenment.

“Maegu.”

“Maegu?”

I’d heard of Megumi from the island country next door, but Maegu was a new one to me. Catching my look, the waiter answered as if explaining it was a chore.

“Maechae Guyuk.”[^2]

“…”

Now he was even abbreviating dish names.

While I stared at him in disbelief, Cheongpung rapidly emptied the plates.

[^2]: *Maechae Guyuk* is pork belly with preserved mustard greens. The waiter shortens its Korean name to *Maegu*, which sounds like the beginning of the Japanese name Megumi.

“Nom, nom.”

“Slow down. Eat slowly.”

“Mmph, mmph. Ah hih he ho. Ha hu i heup hi ha.”

“Don’t answer. Just keep eating.”

“Khanks hah!”

Hyuk Mujin whispered with a thoroughly disgusted expression.

“Isn’t he really a beggar?”

“Didn’t you see him snatch the candied hawthorn earlier? He definitely isn’t.”

*Chomp, chomp.*

“…Probably.”

“What if he’s a master of the Beggars’ Sect?”

“The Beggars’ Sect, huh?”

I had seen it countless times in martial arts novels. It also existed openly in the actual Murim as one of the Nine Sects and One Gang.

I had never met one of its members, but any of the beggars loitering near the inn’s entrance could be a Beggars’ Sect disciple.

“Should I take a quick look to see whether he has any knots?”

The masters of the Beggars’ Sect supposedly distinguished their status by the knots around their waists.

I shook my head.

*No. He isn’t with the Beggars’ Sect.*

If he were, he would have reacted somehow when he heard my name. We belonged to the same orthodox faction, so he had no reason to pretend he didn’t recognize me.

*Then what sect is he from?*

There was no way a Peak master this young had simply dropped out of the sky.

He had to come from a famous sect at the very least… The more I thought about it, the more curious I became about this mysterious young man.

“Burp. That was delicious.”

Cheongpung finally finished eating. After patting his tadpole-like belly, he looked at Hyuk Mujin and me, then stopped short.

“It was my first time trying any of these dishes, so I made a spectacle of myself in front of my Benefactors. I hope I didn’t overdo it…”

*You were more than excessive, you idiot.*

Still, it was good that he had at least a little self-awareness.

“It’s fine. I do that sometimes, too.”

“We have something in common. Ha-ha.”

I laughed along with Cheongpung and opened my mouth. It was time to start questioning him.

“You said everything was your first time eating it. You don’t usually eat rich food, do you?”

Cheongpung shook his head gloomily.

“It’s not that I don’t eat it. I couldn’t eat it. If I’d known food this delicious existed, I would have come down from the mountain sooner.”

“Oh, so you lived in the mountains. That must have been difficult.”

“Life in the mountains? It was fun. The scenery was beautiful, and there was plenty to eat here and there. My grandfather has lived alone in the mountains his entire life, too.”

“Your grandfather?”

“Yes. But, um…”

“Go ahead.”

“May I order some alcohol? I’ve never had any before.”

“…Order as much as you like.”

This kid had a lot of things he had never tried.

At least he still had a sliver of conscience left. He ordered the cheapest bottle of fire liquor.

A short while later, Cheongpung downed the fire liquor without hesitation and muttered with a slightly flushed face,

“Ahh, so this is what it means to get drunk. But what were we talking about?”

“That your grandfather had lived alone in the mountains his entire life.”

“Oh, right. Anyway, I lived with my grandfather from a young age. That started when I was five, so it’s already been fifteen years.”

“Really? That’s a long time.”

I did my best not to show my surprise.

*A Peak master at barely twenty.*

That meant he was a genius at least comparable to Jin Mukyung, if not greater. The more I talked with him, the more curious I became about his identity.

“Where was it? If it’s such a nice place to live, maybe I could visit sometime.”

Cheongpung hesitated just as he was about to say something.

“Um, I don’t think I can tell you that.”

“Come on. You can’t even tell me that much?”

“Because my grandfather hates it when people visit. He moves to a different place once or twice a year because of that.”

“He moves?”

“Yes. Strange people keep coming to see him.”

*Strange people? Obnoxious hikers?*

Well, I suppose it would be annoying for someone living in the mountains.

He continued speaking with a nostalgic look in his eyes.

“When I was ten, dozens of people suddenly came rushing over and started causing trouble. I remember my grandfather shouting at them to get lost before he set the mountain on fire.”

“Oh, so that’s why he keeps moving?”

“Yes. Fortunately, the mountains are huge, so he’s been avoiding them successfully for ten years.”

“…”

Ten years? His grandfather was quite a man.

Hyuk Mujin, who had been listening to Cheongpung’s story with great interest, asked,

“Then why did Young Master come down from the mountain?”

Cheongpung, who had been sucking on the mouth of the liquor bottle regretfully, answered,

“Because of the Ten Dragons and Phoenixes.”

“The Ten Dragons and Phoenixes? What’s that supposed to be?”

At my question, Hyuk Mujin looked at me as though I were the strangest person he had ever seen.

“Why don’t you know about the Ten Dragons and Phoenixes, Captain?”

“I’m allowed not to know, damn it.”

“Huh? You made a complete fool of yourself last year after getting plastered at a pleasure house and bragging that you were going to become one of them.”

“That wasn’t me… Never mind. What are the Ten Dragons and Phoenixes?”

“Are you seriously asking because you don’t know?”

“Can’t I just not know?”

“Of course you can’t. The Second Young Master is one of them, after all.”

Wait, really?

As I blinked at him, Hyuk Mujin launched into an impassioned explanation.

“They’re the greatest young prodigies of the orthodox Murim! The dragons and phoenixes who will lead the Murim of the future! How can you not know about the Ten Dragons and Phoenixes?”

“Hey, hey. Keep your voice down. People are staring.”

He wasn’t exaggerating. Hyuk Mujin’s booming voice had drawn glances from the other customers.

“Who cares if they stare? This is too much even for you, Captain! Are you making fun of me?”

“I don’t know about making fun of people, but I’m good at hitting them.”

“I think I got too worked up. I’m sorry.”

Hyuk Mujin regained his composure in an instant. I turned away from him and gave Cheongpung a friendly smile.

“Please continue.”

“It’s nothing important. I just had a childish thought for a moment.”

Cheongpung looked at me through slightly unfocused eyes. Apparently, he had no intention of using his internal energy to dispel the drunkenness, because he was still a little tipsy.

“Who would be stronger, me or them? I wanted to find the answer to that question.”

In the end, it was because of a martial artist’s competitive pride.

The desire to step into a new world. The desire to defeat a strong opponent and prove his martial arts. I could tell that those feelings had led him down the mountain.

*He seems to have the skill to justify thinking that way, too.*

Jin Mukyung had supposedly reached the Peak realm when he was barely twenty and caused an uproar throughout the Central Plains. Now, he was counted as one of the Ten Dragons and Phoenixes, one of the greatest young prodigies of the orthodox faction.

The Cheongpung in front of me possessed martial talent at least comparable to Jin Mukyung’s.

*He has every right to think so.*

I was nodding inwardly when—

“Puhahaha!”

“Pfft, hahahaha. Ah, holding back my laughter was torture.”

I raised my head toward the source of the sound.

On the second floor, five men and women in silk clothes were looking down at us with faces full of mockery.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 132`.

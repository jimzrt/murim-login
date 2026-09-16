# Master Edit Task — Chapter 133

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
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 산서오문   | **Five Gates of Shanxi**         |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 기루     | **pleasure house**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 표국     | **Escort Bureau**                            |
| 레벨               | **Level**                      |
| 매력               | **Charm**                      |
| 산서     | **Shanxi**             |
| 사천     | **Sichuan**            |
| 팔천협    | **Eight Spring Gorge** |
| 귀문      | **your sect**                                                   |
| 귀가      | **your family**                                                 |
| 소협      | **Young Hero**                                                  |
| 소저      | **Young Lady**                                                  |
| 대사      | **Master** for a senior Buddhist monk                           |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 명화 | **Myeonghwa** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 성룡이 | **Seongryong** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 소혜 | **Sohye** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 국주님 | **Chief** | Honorific title for the head of an Escort Bureau. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |
| 삼도문 | **Samdo Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 궁귀문 | **Gunggui Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

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

#### Chapter 131 tail (verified mastered)

…
who lingered around her stall. After a childhood of hardship and years of grueling effort, the boy finally found success and returned as a strapping young man. It was a story I had heard somewhere before, but that didn’t make it any less moving. “Ahem. What is this? Did something get in my eye?” Was it yellow dust or fine dust? They couldn’t have built any factories yet, so it must have been yellow dust. That was when the rims of my eyes reddened slightly despite myself. “So, have you gone to see your parents?” “Not yet. I was thinking of stopping by today or tomorrow.” “Go see them soon. Didn’t your family move?” “Moved? Where?” “To a large estate along the main road over there. They even released koi into the pond and raised them.” “Oh, really?” “…?” Parents? Moving? A huge estate with koi? Wait. Something wasn’t right. I stared dumbfoundedly at Hyuk Mujin as he returned carrying the candied hawthorn skewers. “What was that about?” “Huh? About what?” “Your parents are alive?” Hyuk Mujin stared at me as though I were insane. “Why are you killing off my perfectly healthy parents?” “No, that’s not what I meant… Then what was all that stuff you said earlier?” “What stuff?” “The candied hawthorn. You said you couldn’t have any and spent every day sucking on your fingers.” “I couldn’t have any. My parents wouldn’t let me eat it because they said it would rot my teeth. Every merchant around here knew how overbearing my parents were, so they made a point of refusing to sell any to me. That lady was the only one who secretly slipped me some.” “…” “And what about being jealous of the children holding their parents’ hands?” “My family’s business was so successful that they never had any free time. I played by myself.” “Th-then you had family in Taiyuan, but you didn’t come back once in five years?” “I left home. I didn’t want to inherit the family business, so I left a single letter behind and ran away. The Master of the Gatekeeper Pavilion in our family is my father’s childhood best friend, so he probably knew everything about how I was doing.” “…” “For about two years, they gave me hell over it. Then my youngest sibling was suddenly born, so I no longer needed to inherit the family business. After that, they stopped saying much.” Hyuk Mujin craned his neck and looked around, then raised a hand and pointed. “Ah, there it is. See it? That building belongs to my parents… It got even bigger while I was away.” I followed Hyuk Mujin’s finger and turned my head. A huge, towering five-story pavilion and a signboard bearing enormous characters came into view. **Hyuk Family Textile Shop** Hyuk Mujin smiled proudly. “It’s the largest textile shop in Taiyuan. We have branches in Henan and Hebei, too.” *This bastard was born with a silver spoon, too…* You had to be pretty damn wealthy to open chain stores in a place this rough. *What the hell have I been doing?* A young boy who used to suck on his fingers because he wanted to eat candied hawthorn so badly? The truth was that his successful business-owner parents had forbidden him from eating it because they were worried about his teeth. *What the fuck is this?* As I stood there with my mouth hanging open, Hyuk Mujin held out one of the candied hawthorn skewers. “Here, have one. I specially chose the biggest and shiniest one. The ones that lady sells are the best in this area.” “You son of a…” I swallowed the curse that had surged up to my throat and bit down on the candied hawthorn with a loud crunch. “Let’s hurry up and find a room.” “Already? We’ve only spent a few iron coins…” “Hey! Is it your money? Those are travel expenses we were given to spend when necessary. Expenses!” “Didn’t you just say we should spend it all and have fun?” “We’ve had enough fun. You said the rooms would fill up after sunset. If we get a bad night’s sleep and end up late to tomorrow’s luncheon, are you going to take responsibility?” “…” * * * Honghwa Inn. As its signboard suggested, this was one of the establishments under the Lower District Sect’s influence. *Honghwaru at night. Honghwa Inn for lodging.* Whoever had come up with that arrangement was clearly determined to wring every last coin out of the drunks. “Let’s go in.” I was about to lead Hyuk Mujin, whose lower lip had been jutting out for some time, toward the inn’s entrance when someone spoke. “Excuse me. I’m sorry to bother you.” The voice strangely tugged at my nerves. Its owner was a young man with an affable expression and a dreamy, hazy voice as innocent as a child’s. *This feeling…* The moment I turned around and met his clear eyes, my breath caught despite myself. This was an aura different from Jin Mukyung’s. > **System** > > **Level:** ??? > **Name:** Cheongpung Another Peak master had appeared. Amid the tension, the young man named Cheongpung opened his lips. “If you don’t mind, may I eat just one candied hawthorn skewer?” “…?” *What the hell is this guy?* [^1]: Candied hawthorn skewers are a traditional snack made by coating skewered fruit in hardened sugar.

#### Chapter 132 tail (verified mastered)

…
all over the place. My grandfather has lived alone in the mountains his entire life, too.” “Your grandfather?” “Yes. But, um…” “Go ahead.” “May I order some alcohol? I’ve never tried it before.” “…Order as much as you like.” This kid had a lot of things he’d never tried. At least he still had a sliver of conscience left. He ordered the cheapest bottle of fire liquor. A short while later, Cheongpung downed the fire liquor without hesitation and muttered, his face slightly flushed. “Ahh, so this is what it means to get drunk. But what were we talking about?” “Your grandfather living alone in the mountains his entire life.” “Oh, right. Anyway, I’ve lived with my grandfather since I was little. I was five when we started living together, so it’s already been fifteen years.” “Really? That’s a long time.” I did my best not to show my surprise. *A Peak master at barely twenty.* That meant he was a genius at least comparable to Jin Mukyung, if not greater. The more I talked with him, the more curious I became about his identity. “Where is it? If it’s such a nice place to live, maybe I could visit sometime.” Cheongpung hesitated just as he was about to say something. “Um, I don’t think I can tell you that.” “Come on. You can’t even tell me that much?” “Because my grandfather hates it so much… He already moves to a different place once or twice a year because of that.” “He moves?” “Yes. Strange people keep coming to see him.” *Strange people? Obnoxious hikers?* Well, I suppose it would be annoying for someone living in the mountains. He continued with a nostalgic look in his eyes. “When I was ten, dozens of people suddenly came rushing over and started causing trouble. I remember my grandfather shouting at them to get lost before he set the mountain on fire.” “Oh, so that’s why he keeps moving?” “Yes. Fortunately, the mountains are huge, so he’s managed to avoid them for ten years.” “…” Ten years? His grandfather was quite a man. Hyuk Mujin, who had been listening to Cheongpung’s story with great interest, asked, “Then why did you come down from the mountain, Young Master?” Cheongpung, who had been sucking on the mouth of the liquor bottle regretfully, answered, “Because of the Ten Dragons and Phoenixes.” “The Ten Dragons and Phoenixes? What’s that supposed to be?” At my question, Hyuk Mujin looked at me as though I were the strangest person he had ever seen. “Why don’t you know about the Ten Dragons and Phoenixes, Captain?” “I’m allowed not to know, damn it.” “Huh? Last year, you got plastered at a pleasure house and made a complete fool of yourself bragging that you were going to become one of them.” “That wasn’t me… Never mind. What are the Ten Dragons and Phoenixes?” “Are you seriously asking because you don’t know?” “Can’t I just not know?” “Of course you can’t. The Second Young Master is one of them, after all.” Wait, really? As I blinked at him, Hyuk Mujin launched into an impassioned explanation. “They’re the greatest young prodigies of the orthodox Murim! The dragons and phoenixes who will lead the Murim of the future! How can you not know about the Ten Dragons and Phoenixes?” “Hey, hey. Keep your voice down. People are staring.” I wasn’t exaggerating. Hyuk Mujin’s booming voice had drawn glances from the other customers. “Who cares if they stare? This is too much even for you, Captain! Are you making fun of me?” “I don’t know about making fun of people, but I’m good at hitting them.” “I think I got too worked up. I’m sorry.” Hyuk Mujin regained his composure in an instant. I turned away from him and gave Cheongpung a friendly smile. “Please continue.” “It’s nothing important. I just had a childish thought for a moment.” Cheongpung gazed at me through slightly unfocused eyes. Apparently, he had no intention of using his internal energy to dispel the drunkenness, because he still looked a little tipsy. “Who would be stronger, me or them? I wanted to find the answer to that question.” In the end, it came down to a martial artist’s competitive pride. The desire to venture into a new world. The desire to defeat the strong and prove his martial arts. I could tell those feelings had led him down the mountain. *He seems to have the skill to justify thinking that way, too.* Jin Mukyung had supposedly reached the Peak realm at barely twenty, causing an uproar throughout the Central Plains. Now he was counted among the Ten Dragons and Phoenixes, the greatest young prodigies of the orthodox faction. The Cheongpung in front of me possessed martial talent at least comparable to Jin Mukyung’s. *He has every right to think so.* I was nodding inwardly when— “Puhahaha!” “Pfft, hahahaha. Ah, holding back my laughter was torture.” I raised my head toward the source of the sound. On the second floor, five men and women dressed in silk were looking down at us, their faces full of mockery. [^1]: Candied hawthorn skewers are a traditional Chinese snack made by coating skewered fruit in hardened sugar. [^2]: *Maechae Guyuk* is pork belly with preserved mustard greens. The waiter shortens its Korean name to *Maegu*, which sounds like the beginning of the Japanese name Megumi.

## Korean source

```text
＃133화



우진태(優進泰)는 황금빛 술잔을 치켜들었다. 온갖 진미와 명주로 가득 채워진 탁자에는 그를 포함하여 총 다섯 명의 남녀가 앉아 있었다.

“자, 산서오문(山西五門)의 무궁한 발전을 위하여!”

“위하여!”

“위하여!”

한 순배씩 술이 돌자 다섯 사람의 얼굴에 웃음이 번졌다.

“역시 홍화객잔이군요. 숙수가 누군지는 몰라도 음식 맛이 대단합니다.”

“그러게요. 혀에 닿자마자 살살 녹아요.”

우진태가 호탕한 웃음을 터트렸다.

“하하, 허리띠 풀고 마음껏 드시오. 오늘도 내가 모두 살 테니.”

“이야, 역시 형님! 이러다가 성운표국 기둥뿌리 하나 뽑는 거 아닙니까?”

“어머, 감당되시겠어요?”

우진태는 피식 웃으며 눈앞의 이남이녀(二男二女)를 바라보았다.

스무 개의 중소 문파 연합. 그중에서도 대표 격인 산서오문의 자제들이지만 자신에게는 한 수 접어 줘야 한다.

“어허, 나 우진태요. 성운표국의 우진태! 이 객잔을 통째로 사도 문제없으니 걱정 말고 마음껏 드시오.”

약간의 허세가 섞이긴 했지만 아주 틀린 말도 아니다.

삼문협(三門峽) 일대를 주름잡고 있는 성운표국은 운수와 경비 등, 각종 사업으로 매해 엄청난 재물을 벌어들이고 있으니까.

우진태는 바로 그 성운표국을 물려받을 후계자였다.

‘역시 돈이 최고지.’

산서오문이라고 해 봤자 어차피 하나같이 고만고만한 중소 문파의 자제들. 성운표국의 금력(金力)을 등에 업은 그는 거칠 것이 없었다.

“이 자리에 있는 분들 덕분에 우리 성운표국이 한 계단 올라섰으니 그만한 대접을 해야 하지 않겠소?”

우진태의 말에 사람들이 황급히 손사래를 쳤다.

“어휴, 그게 어떻게 저희 덕분입니까? 다 국주님과 형님께서 표국의 발전을 위해 불철주야 애쓰신 덕분이지요.”

“맞아요. 우 소협의 말씀은 저희가 감당하기 어려워요.”

금이면 귀신도 부린다는데 산 사람은 오죽할까.

‘불철주야 애썼다라. 뭐, 틀린 말은 아니군.’

뼈대 있는 무가(武家)도, 그렇다고 뚜렷한 무림 문파도 아닌 성운표국이 산서오문에 들어갈 수 있었던 이유는 재물을 풀었기 때문이다.

이십여 개 중소 문파의 문주들과 중진들, 자제들…… 그들 모두에게 밤낮 가리지 않고 술과 재물을 퍼먹였고, 결과는 확실했다.

‘산서오문.’

남부에 위치한 중소 문파 연합의 대표라 할 수 있는 자리다.

평범한 무림 문파였다면 허울만 좋은 명예직이었겠지만. 각종 사업을 통해서 이익을 창출하는 성운표국으로서는 날개를 단 것이나 다름없었다.

우진태는 짐짓 진중한 얼굴로 고개를 숙였다.

“아닙니다. 여러분들이 있기에 지금의 성운표국이 있는 거요. 몇 달 전만 하더라도 그 간악한 노괴(老怪)들 때문에 통 기를 못 펴고 살았는데…… 다시 한번 고맙소.”

“노괴들이라면, 그 배반자들 말입니까?”

“어이쿠, 그자들 이야기는 꺼내지도 마십시오. 이번 일이 아니었다면 우리 모두 꼼짝없이 이용만 당할 뻔했습니다.”

이 자리에 모인 이들은 모두 산서오문의 자제들이지만 불과 몇 달 전까지만 해도 아니었다.

삼도문, 궁귀문을 비롯한 다섯 개 문파, 그들이 바로 전(前) 산서오문이다. 그러나 대장로의 수족임이 밝혀진 팔천협 전투에서 빠짐없이 멸문당했다.

“이제 와서 하는 말인데, 그 작자들이 유난히 성운표국을 견제하긴 했습니다.”

“국주님과 우 소협의 혜안(慧眼)에 정체가 발각될까 봐 그런 것이 분명해요.”

우진태는 터져 나오려는 웃음을 억눌렀다. 전 산서오문의 문주들이 성운표국을 견제했던 이유는 간단하다.

‘바로 지금 같은 상황을 우려해서지.’

당시의 산서오문은 지금보다 훨씬 강했고 유대도 끈끈했다.

하지만 이제는 아니다. 이 자리의 모두는 이미 성운표국의 돈맛을 봤다. 이걸 빌미로 야금야금 각종 이권을 뺏어 먹는 건 시간문제다.

“자, 이번에는 우리의 우정을 위해 건배합시다.”

“우정을 위하여!”

흥겨운 분위기의 술자리가 이어졌다. 우진태는 틈틈이 선물이라는 이름의 뇌물을 건네기도 했다.

“이번에 사천에서 들여온 촉금(蜀錦)인데, 황 소저께 잘 어울릴 것 같아 따로 빼 두었지요.”

“어머, 제가 아는 그 촉금이요?”

“예. 그중에서도 최상급이라 그런지 빛깔이 아주 곱더군요. 하인에게 일러 마차에 미리 실어 두었으니 가져가십시오.”

“세상에, 우 소협. 너무 감사해요.”

“감사할 것까지 있겠습니까? 그냥 소저를 생각하는 제 마음이다, 생각하시고 넣어 두십시오.”

“네, 네?”

“하하, 제가 말실수를 했군요. 못 들은 셈 치십시오.”

우진태의 매력적인 미소에 소속된 무인만 일백이 넘어가는 문파의 무남독녀가 볼을 붉혔다.

마음의 빚을 지게 해 두면 언제고 써먹을 날이 있을 것이다.

“형님, 이거 서운합니다. 소저들만 챙기시는 게 어디 있습니까?”

그는 어느새 호형호제하게 된 무가의 자제를 향해 이번엔 눈을 찡긋했다.

“내가 혁 아우를 잊었을 리가. 기대하고 있게. 아주 끝내주는 선물을 준비해 뒀으니.”

“크, 역시 형님.”

“하하, 우 소협, 날 잊은 건 아니겠지요?”

“무슨 그런 섭섭한 말씀을 하십니까. 사람마다 어울리는 선물이 있어서 따로 말씀드리려고 한 것뿐입니다.”

쉬운 일이다. 여인들에게는 값비싼 비단과 보석, 사내들에게는 절색의 여인과 재물을 안겨 주면 된다.

마침 근처에 산서성 제일의 기루라는 홍화루가 있으니 안성맞춤이다.

우진태는 기뻐하는 사람들을 보며 빙긋 웃었다.

“기분도 적당히 풀렸겠다, 오늘 술자리는 이쯤에서 파할까 하는데…… 다들 어찌 생각하십니까?”

선물을 받기 전이라면 아쉬웠겠지만 지금은 다르다.

여인들은 마차에 실어 둔 비단과 보석을 확인하고 싶어 고개를 끄덕였고, 사내들은 기루로 자리를 옮길 거라는 확신에 가슴이 뛰었다.

“그럼 마지막으로 몇 잔씩들 하고 일어납시다. 내일 있을 오찬(午餐)도 잊지 마시고요.”

우진태의 말에 사람들이 피식피식 웃었다.

“아무리 취해도 그걸 잊겠습니까.”

“우 소협도 참, 저희를 너무 무시하는 것 아니에요?”

“혹시나 하는 마음에 말한 겁니다. 하하하.”

산서 성주와의 오찬.

그것이 산서에서 방귀 좀 뀐다는 문파의 자제들이 한자리에 모인 이유였다. 우진태는 술잔을 비우며 생각했다.

‘내일이 기대되는군.’

고작 열 살밖에 되지 않은 어린 성주.

사람 비위 맞추는 데에는 도가 튼 그다. 이미 성주를 구워삶을 만반의 준비를 끝내 두었다.

‘듣기로는 제법 잔망스러운 녀석이라던데…… 황족이라, 과연 어떨까?’

우진태가 곰곰이 생각에 잠겨 있던 그때. 아래층에서 쩌렁쩌렁한 외침이 터져 나왔다.

“정파 무림 최고의 후기지수들! 차기 무림을 이끌어 갈 용과 봉황들! 십봉룡을 모른다는 게 말이나 됩니까?”

“야, 야. 목소리나 줄여. 사람들 쳐다보잖아.”

십봉룡? 그 단어에 다섯 쌍의 귀가 쫑긋 섰다.

십봉룡이 누구인가, 이미 전설의 첫 장을 쓰고 있는 천재들이자 정파 무림의 미래다.

십봉룡은 강호의 후기지수들에게는 선망의 대상이었고, 이 자리에 모인 이들에게도 크게 다르지 않았다.

“누구지? 무림인인가?”

난간 가장 가까이에 앉아 있던 사람이 목을 빼고 아래층을 내려다보며 말했다.

“세 명입니다. 한 명은 도련님, 한 명은 그럭저럭 무인 같고…… 다른 하나는 거지로 보이는데요.”

“그게 도대체 무슨 조합이야?”

“쉿, 계속 들어나 봅시다.”

우진태의 말에 사람들이 입을 다물고 다시 귀를 기울였다.

다들 무가의 자제라고 할 만큼 무공을 익힌 몸이라 대화를 듣는 것은 그리 어렵지 않았다.

“말씀 계속하시죠.”

“별건 아니에요. 순간적으로 치기 어린 생각이 들었던 거죠.”

잠깐의 침묵. 그리고 이어지는 한마디.

“나와 저들 중에 누가 더 강할까? 저는 그 의문에 대한 답을 확인하고 싶었어요.”

산서오문의 후기지수들이 서로를 바라보았다.

“방금 저 말, 다들 들으셨습니까?”

“네, 누가 한 말이에요?”

“아까 말했던 그 거집니다. 요즘 별 미친놈을 다 보겠네요.”

그때 우진태가 고개를 저었다.

“거지가 아니라 무인일 겁니다.”

“무인……이라고 하셨습니까?”

“십봉룡을 입에 올릴 정도면 그게 맞겠죠. 어떻게 거지꼴이 됐는지는 뭐, 안 봐도 대충 알겠고요.”

우진태의 입가에서 실소가 흘러나왔다.

“뻔하지 않습니까. 어쩌다 익힌 삼류 무공 몇 수를 믿고 하염없이 강호를 떠돌다가 죽는 인생.”

“아하, 생각해 보니 그렇네요. 역시 우 소협이십니다.”

“곱씹을수록 웃기네. 어떻게 저 주제에 십봉룡을 입에 올렸지?”

서로를 바라보며 피식거리던 후기지수들의 웃음이 점점 진해졌다.

“그런 정신 나간 놈이랑 어울리는 것들 수준도 알 만하군. 아니, 미친놈이라고 따귀를 한 대 올려붙이고 나가려나?”

“그, 같이 앉은 도련님이랑 무인은 뭐 하고 있대요?”

아래를 힐끗 내려다본 후기지수가 웃음을 참으며 말했다.

“무인은 모르겠고, 도련님은 혼자서 고개 끄덕끄덕하고 있습니다.”

“허어.”

“정말요?”

“이야, 다들 저 표정을 봐야 되는데. 진심으로 저 거지 말을 믿는 것 같은데요?”

후기지수들이 자리에서 일어나 난간으로 다가갔다. 그중에는 호기심을 참지 못한 우진태도 포함되어 있었다.

‘어떤 놈들인지 얼굴이나 보자.’

그리고 심각한 표정으로 고개를 끄덕이는 도련님의 얼굴을 본 순간, 그의 입에서 커다란 웃음이 터져 나왔다.

“푸하하핫!”

동시에 다른 후기지수들도 큰 소리로 웃기 시작했다.

“큭, 크크큭! 아, 웃음 참느라 혼났네.”

“크하하! 무공이라고는 쥐뿔도 모르는 놈들이, 뭐? 십봉룡이 어쩌고 저째?”

얼마나 웃었을까. 간신히 웃음을 그쳤을 때 그들이 목격한 것은, 물끄러미 자신들을 바라보는 한 사람의 시선이었다.

“다 웃었냐?”

‘도련님’의 한마디에 후기지수들은 멍해졌다.

다들 애지중지 자란 몸이다. 도대체 이게 얼마 만에 들어 보는 반말인가.

순간 싸하게 내려앉은 침묵을 깨트린 것은 우진태의 메마른 목소리였다.

“그렇다면?”

‘도련님’이 활짝 웃었다.

“당장 내려와, 이 호로 쌍노무 새끼들아. 목 아파.”



* * *



혁무진이 기대 어린 눈빛으로 물었다.

“한판 하시게요?”

“저놈들 하는 거 봐서.”

“호로 쌍노무 새끼 소리 나왔으면 싸우자는 거 아니에요?”

“그것도 좋고. 내 얼굴에 저놈들 침 다 튄 거 보여?”

“흥건하네요.”

혁무진이 옷소매로 내 얼굴을 슥슥 문질러 주었다.

“사과 안 하면 어떡해요?”

“해야 될걸?”

“쟤들 표정 보세요. 절대 사과 안 해요.”

“그럼 뒤지게 맞아야지.”

“여인들도 있는데…….”

“나 남녀평등주의자야.”

“예?”

“공평하게 다 때린다고.”

멍하니 구경만 하고 있던 청풍이 반짝거리는 시선으로 날 바라봤다.

“오, 잘은 모르지만 뭔가 멋있어 보여요.”

“별걸 다…… 일단 감사합니다.”

뭔가 더 얘기하고 싶어도 더 이상 시간이 주어지지 않았다.

다섯 놈, 아니 다섯 연놈들이 2층에서 훌쩍 뛰어내렸기 때문이다.

타닥.

일류 고수다운 사뿐하게 착지. 이쪽을 노려보는 그들 사이로 한 사람이 나섰다.

45레벨. 키 크고 훈훈하게 생긴 놈. 아까 처음으로 웃었던 그놈이다.

“나는…….”

“네가 대가리야?”

“대가리?”

“거기 다섯 명 중에 두목이냐고.”

놈이 피식 웃었다.

“입조심하는 게 좋을 거다. 나를 포함해서 여기 있는 분들이 누군지 알면…….”

나는 마주 웃으며 연놈들의 레벨창을 쭉 읽었다.

“성룡이, 천우, 명화, 소혜, 마지막으로 넌 진태. 성까지 말해 줘?”

“……!”

“……!”

놀라움에 찬 다섯 쌍의 눈동자. 아니, 혁무진과 청풍까지 일곱 쌍의 눈동자가 내게 쏠렸다.

“아, 그리고 이건 개인적인 부탁인데, 제발 어떻게 알았냐고 물어보지 마라. 그 대사 이제 지겨워. 말하면 때릴 거야.”

“어떻게……!”

“귀에 무 박았냐?”

다음 순간, 내 손바닥이 놈의 뺨에 닿았다.

쫙!
```

## Current accepted English baseline

```markdown
# Chapter 133

Woo Jintae raised a golden wine cup. Five men and women, including him, sat around a table laden with every kind of delicacy and fine liquor.

“Now, to the limitless prosperity of the Five Gates of Shanxi!”

“To prosperity!”

“To prosperity!”

After the wine made its way around once, smiles spread across everyone’s faces.

“As expected of Honghwa Inn. I don’t know who the chef is, but the food is incredible.”

“Right? It practically melts the moment it touches your tongue.”

Woo Jintae let out a hearty laugh.

“Ha-ha! Loosen your belts and eat to your hearts’ content. I’m paying for everyone today, too.”

“Wow, as expected of you, hyung! At this rate, aren’t you going to pull up one of the foundation pillars of the Seongun Escort Bureau?”

“Oh my, can you afford all this?”

Woo Jintae chuckled as he looked at the two men and two women in front of him.

They were the scions of the Five Gates of Shanxi, the representatives of an alliance of twenty small and medium-sized sects. Even so, they had to yield to him.

“Hey, I’m Woo Jintae. Woo Jintae of the Seongun Escort Bureau! I could buy this entire inn and it wouldn’t be a problem, so don’t worry and eat as much as you like.”

There was a little bit of boasting mixed in, but it wasn’t entirely untrue.

The Seongun Escort Bureau dominated the area around Three Questions Gorge and earned an enormous amount of money every year through various businesses, including transportation and security.

Woo Jintae was the heir who would inherit that very Seongun Escort Bureau.

*Money really is the best.*

The Five Gates of Shanxi were nothing more than the scions of a bunch of small and medium-sized sects that were all roughly the same. With the financial power of the Seongun Escort Bureau behind him, there was nothing Woo Jintae had to fear.

“Thanks to everyone here, our Seongun Escort Bureau has climbed another step higher, so it’s only right that I treat you accordingly, isn’t it?”

At Woo Jintae’s words, everyone hurriedly waved their hands.

“Oh, no. How could that be thanks to us? It’s all thanks to the Chief and Young Hero Woo working tirelessly day and night for the growth of the Escort Bureau.”

“That’s right. We could never accept such praise from Young Hero Woo.”

They said that money could make even ghosts do your bidding. Living people were even easier.

*Working tirelessly day and night, huh? Well, that isn’t entirely wrong.*

The Seongun Escort Bureau was neither a prestigious martial family nor a distinct Murim sect. The reason it had been able to join the Five Gates of Shanxi was because it had opened its purse.

The Sect Leaders, senior members, and scions of more than twenty small and medium-sized sects…

Woo Jintae had stuffed all of them with liquor and money day and night, and the results had been undeniable.

*The Five Gates of Shanxi.*

It was a position that could be called the representative of the alliance of small and medium-sized sects in the south.

For an ordinary Murim sect, it would have been nothing more than a hollow honorary position. But for the Seongun Escort Bureau, which generated profits through all kinds of businesses, it was like growing wings.

Woo Jintae lowered his head with an appropriately solemn expression.

“No. The Seongun Escort Bureau of today exists because of all of you. Just a few months ago, those vile old monsters had us living without being able to hold our heads up… Thank you once again.”

“Those old monsters? You mean the traitors?”

“Ugh, don’t even mention them. If this hadn’t happened, all of us would have been helplessly used by them.”

Everyone gathered here was a scion of the Five Gates of Shanxi, but that had not been the case until only a few months ago.

The Samdo Sect, the Gunggui Sect, and three other sects had been the former Five Gates of Shanxi. But during the Battle of Eight Spring Gorge, it was revealed that they were all agents of the Head Elder, and every one of them had been annihilated.

“Now that I think about it, those bastards were especially wary of the Seongun Escort Bureau.”

“They must have been afraid that their identities would be exposed by the keen insight of the Chief and Young Hero Woo.”

Woo Jintae suppressed the laugh that was threatening to escape.

The reason the former Five Gates of Shanxi had been wary of the Seongun Escort Bureau was simple.

*They were worried about exactly this situation.*

The Five Gates of Shanxi had been much stronger back then, and their bonds had been far tighter.

But that was no longer the case. Everyone here had already tasted the money of the Seongun Escort Bureau. Using that as leverage to slowly siphon away all kinds of business interests was only a matter of time.

“Now, let’s raise a toast to our friendship.”

“To friendship!”

The lively drinking continued. From time to time, Woo Jintae also handed out bribes disguised as gifts.

“This is Shu brocade I brought in from Sichuan. I thought it would suit Young Lady Hwang, so I had it set aside separately.”

“Oh my! You mean the Shu brocade I know?”

“Yes. It’s the finest grade, and perhaps that’s why the color is so exceptionally beautiful. I told a servant to load it into the carriage beforehand, so please take it with you.”

“My goodness, Young Hero Woo. Thank you so much.”

“Is there any need to thank me? Just think of it as the feelings I have for you and put it away.”

“Wh-what?”

“Ha-ha, I misspoke. Pretend you didn’t hear that.”

At Woo Jintae’s charming smile, the only daughter of a martial sect with more than a hundred affiliated martial artists blushed.

*Once I make her indebted to me, there will be a day when I can put that debt to use.*

“Hyung, this is unfair. How can you only take care of the young ladies?”

He winked at the scion of a martial family who had become close enough with him to call each other hyung and little brother.

“Did you think I could forget Little Brother Hyuk? Just wait. I’ve prepared an absolutely incredible gift for you.”

“Damn, as expected of you, hyung.”

“Ha-ha, Young Hero Woo, you haven’t forgotten me, have you?”

“What a hurtful thing to say. I only wanted to tell you separately because I have a gift suited to each person.”

It was easy. Expensive silk and jewelry for the women, and peerless beauties and wealth for the men.

There happened to be Honghwaru, supposedly the finest pleasure house in Shanxi Province, nearby. It was perfect.

Woo Jintae smiled as he watched everyone’s delight.

“Now that everyone’s had a chance to unwind, how about we end tonight’s drinking here… What do you all think?”

If they had not received their gifts yet, they might have been disappointed. But things were different now.

The women nodded because they wanted to check the silk and jewelry loaded into the carriage, while the men’s hearts pounded at the certainty that they would be moving to the pleasure house.

“Then let’s have a few final cups before we leave. And don’t forget tomorrow’s luncheon.”

Everyone chuckled at Woo Jintae’s words.

“How could we forget that, no matter how drunk we get?”

“You really underestimate us, Young Hero Woo.”

“I only mentioned it just in case. Ha-ha-ha.”

A luncheon with the City Lord of Shanxi.

That was why the scions of the sects with some clout in Shanxi had gathered in one place. Woo Jintae emptied his wine cup and thought,

*Tomorrow should be interesting.*

The City Lord was only ten years old.

He was already an expert at catering to people’s whims. Woo Jintae had finished making every possible preparation to win the City Lord over.

*I hear he’s quite a mischievous little fellow… He’s a member of the imperial family, so I wonder what he’ll be like.*

Just as Woo Jintae was sinking into thought, a booming shout erupted from downstairs.

“The greatest young prodigies of the Murim’s orthodox faction! The dragons and phoenixes who will lead the Murim of the future! How can you say you don’t know the Ten Dragons and Phoenixes?”

“Hey, hey. Keep your voice down. People are staring.”

At the words *Ten Dragons and Phoenixes*, five pairs of ears perked up.

Who were the Ten Dragons and Phoenixes? They were geniuses already writing the first pages of their legends and the future of the Murim’s orthodox faction.

The Ten Dragons and Phoenixes were objects of admiration for the young martial artists of the martial world, and the people gathered here were no different.

“Who are they? Are they martial artists?”

The person seated closest to the railing craned his neck and looked down at the first floor.

“There are three of them. One is a young master, one looks more or less like a martial artist… and the other one looks like a beggar.”

“What kind of combination is that?”

“Shh. Let’s keep listening.”

At Woo Jintae’s urging, everyone fell silent and pricked up their ears again.

They had all trained in martial arts as befitted scions of martial families, so overhearing the conversation was not difficult.

“Please continue.”

“It’s nothing important. I just had a childish thought for a moment.”

There was a brief silence. Then another statement followed.

“Who would be stronger, me or them? I wanted to find the answer to that question.”

The young prodigies of the Five Gates of Shanxi looked at one another.

“Did you all hear what he just said?”

“Yes. Who said it?”

“That beggar I mentioned earlier. You really do see all kinds of lunatics these days.”

Woo Jintae shook his head.

“He’s a martial artist.”

“A martial artist…?”

“If he’s talking about the Ten Dragons and Phoenixes, he must be. As for how he ended up looking like a beggar, I can more or less guess without even seeing it.”

A mocking laugh escaped Woo Jintae’s lips.

“Isn’t it obvious? He’s the type who picks up a few Third Rate martial arts moves by chance, puts his faith in them, wanders aimlessly through the martial world, and winds up dead.”

“Ah, now that you mention it, you’re right. As expected of Young Hero Woo.”

“The more I think about it, the funnier it gets. How did someone like that dare mention the Ten Dragons and Phoenixes?”

The young prodigies snickered at one another, and their laughter gradually grew louder.

“You can tell what kind of people associate with a lunatic like that. Or maybe they’ll slap him once, call him crazy, and leave?”

“What are the young master and the martial artist sitting with him doing?”

The young prodigy who had glanced down again spoke while trying to hold back his laughter.

“I don’t know what the martial artist is doing, but the young master is nodding to himself.”

“Huh.”

“Really?”

“Wow, you should all see his expression. He genuinely seems to believe that beggar.”

The young prodigies stood up and moved toward the railing. Woo Jintae, who could not resist his curiosity, was among them.

*Let’s see what these people look like.*

The moment he saw the young master’s face, which was nodding with a serious expression, a loud laugh burst from Woo Jintae’s mouth.

“Puhahaha!”

At the same time, the other young prodigies began laughing loudly as well.

“Pfft, ha-ha-ha! I almost died trying to hold that in.”

“Ha-ha-ha! They don’t know the first thing about martial arts, and they’re talking about the Ten Dragons and Phoenixes?”

How long did they laugh?

When they finally managed to stop, what they saw was one person staring quietly up at them.

“Finished laughing?”

At the ‘young master’s’ words, the young prodigies froze.

They had all been raised precious and pampered. How long had it been since anyone had spoken down to them like that?

The chilly silence was broken by Woo Jintae’s dry voice.

“And if we have?”

The ‘young master’ smiled brightly.

“Get down here right now, you fucking sons of bitches. My neck hurts.”

* * *

Hyuk Mujin asked with an expectant look in his eyes,

“Are you going to fight them?”

“Depends on what they do.”

“Once you’ve called them fucking sons of bitches, isn’t that asking for a fight?”

“That would be fine, too. Also, can you see all the spit those bastards sprayed on my face?”

“You’re completely drenched.”

Hyuk Mujin briskly wiped my face with his sleeve.

“What if they don’t apologize?”

“They ought to.”

“Look at their faces. They’re never going to apologize.”

“Then they can get the shit beaten out of them.”

“There are women among them, too…”

“I believe in gender equality.”

“What?”

“I beat everyone equally.”

Cheongpung, who had been watching blankly, looked at me with sparkling eyes.

“Oh. I don’t really understand, but it sounds cool.”

“It’s nothing special… Anyway, thanks.”

Even if I wanted to say more, I was no longer given the time.

The five bastards—or rather, the five sons and daughters of bitches—had jumped down from the second floor.

*Tap.*

They landed lightly, as befitted First Rate masters. One person stepped forward from among the five as they glared at us.

Level 45. He was tall and good-looking. He was also the one who had laughed first.

“I…”

“Are you the head?”

“The head?”

“Are you the boss of the five of you?”

The man gave a short laugh.

“You’d better watch your mouth. If you knew who the people here were, including me…”

I smiled back and scanned through their Level windows.

“Seongryong, Cheonwoo, Myeonghwa, Sohye, and finally, you—Jintae. Want me to tell you your family names, too?”

“…”

“…”

Five pairs of astonished eyes turned toward me. No—along with Hyuk Mujin and Cheongpung, there were seven pairs of eyes fixed on me.

“Oh, and this is a personal request, but please don’t ask how I knew. I’m sick of that line. If you ask, I’ll hit you.”

“How did you…?”

“Did you stick radishes in your ears?”

The next moment, my palm struck the man’s cheek.

*Smack!*
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 133`.

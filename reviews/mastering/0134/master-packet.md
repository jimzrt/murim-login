# Master Edit Task — Chapter 134

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
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 산서오문   | **Five Gates of Shanxi**         |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 영약     | **elixir**                                       |                                                       |
| 살기     | **killing intent**                               |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 중원     | **Central Plains**                               |                                                       |
| 표국     | **Escort Bureau**                            |
| 소국주    | **Young Bureau Head**                        |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 귀가      | **your family**                                                 |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |
| 도동파 | **Dodong Sect** | Fabricated sect claimed by Taekyung when Woo Jintae demands his affiliation. |
| 천진반 | **Tien Shinhan** | Fabricated personal identity claimed by Taekyung. |
| 왕가장 | **Wang Family Estate** | Family estate whose heir is one of the Five Gates scions; he uses sabers rather than sword arts. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 우진태 | enemy_to_enemy | you / you bastard | insulting-casual | Taekyung repeatedly addresses Woo Jintae with hostile informal forms while demanding an apology and slapping him. |
| 우진태 | 진태경 | enemy_to_enemy | you / little bastard | condescending and enraged | Woo Jintae uses hostile forms such as 네놈, 애새끼, and 어린놈 while trying to intimidate Taekyung. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |

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

#### Chapter 132 tail (verified mastered)

…
all over the place. My grandfather has lived alone in the mountains his entire life, too.” “Your grandfather?” “Yes. But, um…” “Go ahead.” “May I order some alcohol? I’ve never tried it before.” “…Order as much as you like.” This kid had a lot of things he’d never tried. At least he still had a sliver of conscience left. He ordered the cheapest bottle of fire liquor. A short while later, Cheongpung downed the fire liquor without hesitation and muttered, his face slightly flushed. “Ahh, so this is what it means to get drunk. But what were we talking about?” “Your grandfather living alone in the mountains his entire life.” “Oh, right. Anyway, I’ve lived with my grandfather since I was little. I was five when we started living together, so it’s already been fifteen years.” “Really? That’s a long time.” I did my best not to show my surprise. *A Peak master at barely twenty.* That meant he was a genius at least comparable to Jin Mukyung, if not greater. The more I talked with him, the more curious I became about his identity. “Where is it? If it’s such a nice place to live, maybe I could visit sometime.” Cheongpung hesitated just as he was about to say something. “Um, I don’t think I can tell you that.” “Come on. You can’t even tell me that much?” “Because my grandfather hates it so much… He already moves to a different place once or twice a year because of that.” “He moves?” “Yes. Strange people keep coming to see him.” *Strange people? Obnoxious hikers?* Well, I suppose it would be annoying for someone living in the mountains. He continued with a nostalgic look in his eyes. “When I was ten, dozens of people suddenly came rushing over and started causing trouble. I remember my grandfather shouting at them to get lost before he set the mountain on fire.” “Oh, so that’s why he keeps moving?” “Yes. Fortunately, the mountains are huge, so he’s managed to avoid them for ten years.” “…” Ten years? His grandfather was quite a man. Hyuk Mujin, who had been listening to Cheongpung’s story with great interest, asked, “Then why did you come down from the mountain, Young Master?” Cheongpung, who had been sucking on the mouth of the liquor bottle regretfully, answered, “Because of the Ten Dragons and Phoenixes.” “The Ten Dragons and Phoenixes? What’s that supposed to be?” At my question, Hyuk Mujin looked at me as though I were the strangest person he had ever seen. “Why don’t you know about the Ten Dragons and Phoenixes, Captain?” “I’m allowed not to know, damn it.” “Huh? Last year, you got plastered at a pleasure house and made a complete fool of yourself bragging that you were going to become one of them.” “That wasn’t me… Never mind. What are the Ten Dragons and Phoenixes?” “Are you seriously asking because you don’t know?” “Can’t I just not know?” “Of course you can’t. The Second Young Master is one of them, after all.” Wait, really? As I blinked at him, Hyuk Mujin launched into an impassioned explanation. “They’re the greatest young prodigies of the orthodox Murim! The dragons and phoenixes who will lead the Murim of the future! How can you not know about the Ten Dragons and Phoenixes?” “Hey, hey. Keep your voice down. People are staring.” I wasn’t exaggerating. Hyuk Mujin’s booming voice had drawn glances from the other customers. “Who cares if they stare? This is too much even for you, Captain! Are you making fun of me?” “I don’t know about making fun of people, but I’m good at hitting them.” “I think I got too worked up. I’m sorry.” Hyuk Mujin regained his composure in an instant. I turned away from him and gave Cheongpung a friendly smile. “Please continue.” “It’s nothing important. I just had a childish thought for a moment.” Cheongpung gazed at me through slightly unfocused eyes. Apparently, he had no intention of using his internal energy to dispel the drunkenness, because he still looked a little tipsy. “Who would be stronger, me or them? I wanted to find the answer to that question.” In the end, it came down to a martial artist’s competitive pride. The desire to venture into a new world. The desire to defeat the strong and prove his martial arts. I could tell those feelings had led him down the mountain. *He seems to have the skill to justify thinking that way, too.* Jin Mukyung had supposedly reached the Peak realm at barely twenty, causing an uproar throughout the Central Plains. Now he was counted among the Ten Dragons and Phoenixes, the greatest young prodigies of the orthodox faction. The Cheongpung in front of me possessed martial talent at least comparable to Jin Mukyung’s. *He has every right to think so.* I was nodding inwardly when— “Puhahaha!” “Pfft, hahahaha. Ah, holding back my laughter was torture.” I raised my head toward the source of the sound. On the second floor, five men and women dressed in silk were looking down at us, their faces full of mockery. [^1]: Candied hawthorn skewers are a traditional Chinese snack made by coating skewered fruit in hardened sugar. [^2]: *Maechae Guyuk* is pork belly with preserved mustard greens. The waiter shortens its Korean name to *Maegu*, which sounds like the beginning of the Japanese name Megumi.

#### Chapter 133 tail (verified mastered)

…
their legends—the future of the Murim’s orthodox faction. They were the objects of every rising martial artist’s admiration, and those gathered here were no exception. “Who are they? Martial artists?” The person seated closest to the railing craned his neck and looked down at the first floor. “There are three of them. One’s a young master, another looks somewhat like a martial artist… and the last looks like a beggar.” “What kind of combination is that?” “Shh. Let’s keep listening.” At Woo Jintae’s urging, everyone fell silent and pricked up their ears again. They had all trained in martial arts as befitted scions of martial families, so overhearing the conversation was not difficult. “Please continue.” “It’s nothing important. I just had a childish thought for a moment.” There was a brief silence. Then another statement followed. “Who would be stronger, me or them? I wanted to find the answer to that question.” The young prodigies of the Five Gates of Shanxi looked at one another. “Did you all hear that?” “Yes. Who said it?” “That beggar I mentioned. You really do see all kinds of lunatics these days.” Woo Jintae shook his head. “He’s probably a martial artist, not a beggar.” “A martial artist…?” “If he’s talking about the Ten Dragons and Phoenixes, that must be it. As for how he ended up looking like a beggar, well, I can guess without even seeing him.” A mocking laugh escaped Woo Jintae’s lips. “Isn’t it obvious? He’s the type who picks up a few Third Rate martial arts moves by chance, puts his faith in them, wanders aimlessly through the martial world, and winds up dead.” “Ah, now that you mention it, you’re right. As expected of Young Hero Woo.” “The more I think about it, the funnier it gets. How did someone like that dare mention the Ten Dragons and Phoenixes?” The young prodigies snickered at one another, and their laughter gradually grew louder. “That tells you all you need to know about the people who associate with a lunatic like him. Or maybe they’ll slap him across the face, call him crazy, and walk out.” “What are the young master and the martial artist sitting with him doing?” The young prodigy who glanced downstairs again answered while stifling his laughter. “I don’t know about the martial artist, but the young master is nodding to himself.” “Well, now.” “Really?” “Wow, you should all see his expression. He genuinely seems to believe that beggar.” The young prodigies rose and approached the railing. Woo Jintae, unable to contain his curiosity, went with them. *Let’s at least see what these fools look like.* The moment he saw the young master nodding with a serious expression, a loud laugh burst from his mouth. “Puhahaha!” At the same time, the other young prodigies began laughing loudly as well. “Pfft, ha-ha-ha! I almost died trying to hold that in.” “Ha-ha-ha! They don’t know the first thing about martial arts, yet they’re talking about the Ten Dragons and Phoenixes?” How long did they laugh? When they finally managed to stop, what they saw was one person staring quietly up at them. “Finished laughing?” At the ‘young master’s’ words, the young prodigies froze. They had all been raised precious and pampered. How long had it been since anyone had spoken down to them like that? Woo Jintae’s dry voice broke the sudden, icy silence. “And if we have?” The ‘young master’ smiled brightly. “Get down here right now, you fucking sons of bitches. My neck hurts.” * * * Hyuk Mujin asked with an expectant look in his eyes, “Are you going to fight them?” “Depends on what they do.” “Once you’ve called them fucking sons of bitches, isn’t that asking for a fight?” “That works, too. See all the spit those bastards sprayed on my face?” “You’re completely drenched.” Hyuk Mujin briskly wiped my face with his sleeve. “What if they don’t apologize?” “They’d better.” “Look at their faces. They’re never going to apologize.” “Then they’ll get the shit beaten out of them.” “There are women among them, too…” “I believe in gender equality.” “What?” “I beat everyone equally.” Cheongpung, who had been watching blankly, looked at me with sparkling eyes. “Oh. I don’t really understand, but it sounds cool.” “It’s nothing special… Anyway, thanks.” I might have said more, but there was no time. The five bastards—or rather, the five sons and daughters of bitches—had jumped down from the second floor. *Tap.* They landed lightly, as befitted First Rate masters. One of them stepped out from the group as they glared at us. Level 45. Tall and good-looking. The same bastard who had laughed first. “I am—” “You the head?” “The head?” “Are you the boss of these five?” He let out a short laugh. “You’d better watch your mouth. If you knew who the people here were, including me…” I smiled back and scanned through their Level windows. “Seongryong, Cheonwoo, Myeonghwa, Sohye, and finally, you—Jintae. Want me to tell you your family names, too?” “…!” “…!” Five pairs of astonished eyes turned toward me. No, seven, counting Hyuk Mujin and Cheongpung. “Oh, and this is a personal request, but please don’t ask how I knew. I’m sick of that line. If you ask, I’ll hit you.” “How did you…?” “Did you stuff radishes in your ears?” The next moment, my palm met his cheek. *Smack!*

## Korean source

```text
＃134화



쫙!

찰진 소리와 함께 우진태의 고개가 옆으로 돌아갔다. 그는 멍하니 자신의 뺨을 쓰다듬었다.

‘지금 무슨 일이 벌어진 거지?’

어안이 벙벙하다. 따귀를 맞아? 내가 고작 이런 놈한테?

내일모레면 이립(而立)인 그는 일찍 혼사를 치른 덕분에 이미 가정도 있었다.

그런데 약관이나 됐을까 싶은 어린놈한테 이런 치욕을 당하다니.

“꺄악! 우 소협!”

“혀, 형님, 괜찮으십니까?”

“저거, 저거 성운표국의 소국주 아녀?”

“맞네. 세상에, 어떤 간 큰 놈이…… 가만, 어디서 본 얼굴 같은데?”

뒤늦은 후기지수들의 반응과 객잔 손님들의 시선이 우진태의 수치심을 배로 키웠다.

그는 살기 어린 눈빛으로 눈앞의 애새끼를 노려봤다.

“네놈이 감히…….”

“그게 아니지.”

“뭐?”

“감히, 가 아니라 어떻게, 가 나와야 하는 거야. 네가 무인이라면.”

우진태가 순간 멈칫했다. 어릴 적부터 성운표국의 전폭적인 지원 아래 각종 영약과 일류 무공을 흡수한 그다.

그러니 뛰어난 무재를 타고나진 않았어도 여타 후기지수에 비해 일초반식은 앞선다고 자부하는 것도 당연했다.

‘그런 내가 이렇게 쉽게 당해?’

놈이 언제, 어떻게 다가왔는지 제대로 보지도 못했다. 사람들 앞에서 개망신을 당했다는 사실에 치욕감이 앞섰을 뿐이다.

우진태는 그제야 경계심이 가득한 눈으로 상대방을 훑었다.

“이 자식 눈깔 굴리는 것 보게. 왜, 쓰리 사이즈 알려 줘?”

“어느 문파의 누구냐?”

“도동파의 천진반이다, 이 새끼야.”

어린놈의 욕설을 참을 수 있었던 것은 이성이 돌아왔기 때문이었다.

무림에서는 무슨 일이 일어날지 모르는 법. 만약 상대가 대문파의 제자라면 깔끔하게 물러나야 한다.

‘도동파, 도동파의 천진반이라고?’

문파도, 놈의 이름도 생소하기 짝이 없다. 슬쩍 뒤를 돌아보니 다른 후기지수들의 얼굴에도 어리둥절한 기색이 역력하다.

우진태의 머리가 팽팽 돌아갔다.

‘내가 알기로 산서성에 도동파라는 문파는 없다.’

이미 각 문파들이 확고히 자리를 잡은 산서성에서 개파(開派)를 한다는 건 불가능에 가깝다.

다른 문파들의 견제는 둘째 치더라도 금세 소문이 날 수밖에 없는 구조다.

‘저 나이에 이만한 경지의 후기지수를 키워 냈다면 상당한 역량의 문파라는 건데……. 어디지? 섬서 쪽인가? 아니면 하남?’

우진태가 쉽게 입을 열지 못하고 눈만 뒤룩뒤룩 굴리던 그 순간이었다.

멀뚱멀뚱, 강 건너 불구경만 하고 있던 젊은 무인이 불쑥 물었다.

“도동파는 또 뭡니까? 진짜 있는 문파예요?”

“있겠냐? 원래 거짓말도 그럴듯하게 치면 실화가 되는 법이란다.”

“아하. 금과옥조 같은 말씀, 가슴에 새기겠습니다.”

“짜식, 오랜만에 말 예쁘게 하네.”

거지처럼 남루한 옷차림의 청년도 한마디 보탰다.

“거짓말도 잘 치면 실화다…… 좋은 말씀입니다. 현기(玄機)가 느껴져요.”

“……아, 예. 일단 칭찬은 고맙네요.”

세 사람의 대화를 들은 우진태의 눈에서 불똥이 튀었다.

“놈! 정체를 밝혀라!”

“왜, 어디의 누구인지 들어 본 다음 만만하면 한판 붙고 급이 좀 높다 싶으면 꼬리 말고 사과하게?”

“…….”

적나라하지만 정곡을 찌르는 한마디다. 쉽게 입을 떼지 못하는 우진태를 보며 어린놈이 끌끌 혀를 찼다.

“인마, 넌 질문부터가 글러 먹었어. 방귀 뀐 놈이 성낸다더니, 내 대답을 듣고 싶었으면 먼저 사과부터 했어야지.”

우진태는 지그시 입술을 깨물었다.

사과?

성운표국의 삼대독자로 태어나 평생을 떠받들어져 살아온 그다. 어디 출신인지도 모를 상대에게 머리를 숙일 만큼 유연한 사고방식의 소유자가 아니었다.

마침내 결심한 우진태는 산서오문의 후기지수들을 향해 은밀히 눈짓했다.

‘저놈이 아무리 강해 봤자지.’

상대는 고작 셋. 반면 이쪽은 산서성에서 손꼽히는 후기지수들로 이루어진 일류 고수 다섯이다.

자신의 신호에 슬쩍 병장기를 움켜잡는 네 남녀를 보니 마음이 든든해진다.

“내가, 아니 우리가 누군지는 알고 있나?”

“어쩌다 보니 이름 석 자 정도는. 그런데 그게 사과냐?”

“사과? 간도 크군.”

우진태가 비릿하게 웃었다.

“우리는 산서오문의 후계자들이다. 산서오문을 모른다고 하지는 않겠지.”

“안다고 해 줄게. 근데 진짜 사과 안 해? 이거 마지막 경고야.”

“나도 경고하지. 어디에서 온 놈인지는 몰라도 사람 잘못 건드렸…….”

쫙!

우진태의 눈앞이 번쩍했다. 저도 모르게 뒷걸음질 치는 그에게 번개 같은 싸대기가 연이어 작렬했다.

쫙! 쫙! 쫘좍!

한 걸음에 한 대씩. 도합 다섯 대를 맞은 우진태가 비틀거렸다.

집요할 정도로 한쪽만 때린 탓에 뺨은 퉁퉁 부어올랐고, 터져 나간 입 안엔 핏물이 고였다.

‘아버지에게도 맞아 본 적이 없는데.’

난생처음 겪는 수모. 그것도 만인이 보는 앞에서 벌어진 일이다.

그의 눈이 희번덕거렸다.

“이런 개……!”

“말했지, 마지막 경고라고. 혹시 마지막이라는 뜻을 모르는 거냐, 아니면 경고의 뜻을 모르는 거냐? 아니면 둘 다?”

“감히 날 쳐?”

“널 함부로 대한 남자는 내가 처음이겠지만 제발 사랑하진 말아라. 난 송이 씨 한 명 사랑하는 것도 바빠.”

“죽인다!”

“때린다!”

쫙쫙쫙!

“커헉!”

우진태는 정신을 차릴 수 없었다.

공력이 실린 것도 아니요, 그렇다고 신묘한 보법을 밟는 것 같지도 않다. 그런데도 한쪽도 아니고 두 뺨을 향해 쏟아지는 따귀 세례를 도저히 막을 방법이 없었다.

‘이게 어떻게 된 일이란 말이냐!’

속수무책으로 당하고 있는 그의 귓가에 광기 어린 외침이 파고들었다.

“왼손으로 때리고, 오른손으로 때리고!”

쫙쫙!

“한치 두치 세치 네치 뿌꾸 뺨! 뿌꾸 뺨!”

쫙쫙쫙!

끊임없이 알아들을 수 없는 말을 외치면서 따귀를 날리는데, 그 모습이 꼭 따귀를 때리기 위해 태어난 미친놈 같았다.

바로 지금처럼.

“왼손 올리고 오른손 내려. 오른손 내리고 왼손 내려. 왼손 내리고 오른손 올리지 마.”

“허억!”

“옳지. 잘했어요. 선생님이 상으로 우리 우진태 어린이의 뺨을 호되게 때려 줄 거예요.”

쫙쫙쫙쫙!

불과 촌각도 되지 않는 시간 동안 얼마나 맞았을까. 삼십 대? 오십 대?

하도 정신없이 맞았더니 머리가 띵하고, 눈에는 눈물이 핑 돈다.

결국, 우진태가 할 수 있는 것은 구조 요청뿐이었다.

“나, 나 좀 도와주시오!”



* * *



성운표국. 재력으로만 따지면 산서 제일의 태원진가에도 비견할 만하다는 바로 그 성운표국의 소국주가 간절한 목소리로 외친다.

“제, 제발 도와주시오!”

자존심이고 뭐고 전부 내팽개친 절박한 음성에도 산서오문의 후기지수들은 쉽사리 병장기를 뽑지 못했다.

“저걸 어떻게 이겨…….”

누군가가 신음처럼 흘린 말은 모두의 마음을 대변하는 것이었다.

맞다. 직접 겪어 볼 필요도 없다.

옆에서 보는 것만으로도 오금이 저리고 다리가 풀릴 정도였다. 상대는 자신들과 나이만 엇비슷할 뿐, 상상을 뛰어넘는 고수임이 틀림없었다.

“저 나이에 이 정도 경지라니.”

“저건 완전 괴물이잖아.”

쫙쫙!

“사, 살려 주시오!”

한층 더 절박해진 목소리. 구조 요청도 미묘하게 변했다.

이대로 조금만 더 지난다면 차라리 죽여 달라는 말이 나올지도 모르겠다.

“도, 도와야겠죠?”

“최소한 말리기라도 해야…… 왕 공자가 어떻게 좀 해 봐요.”

“저요? 갑자기 저는 왜요?”

“왜긴요. 모일 때마다 가전무공 자랑했잖아요. 중원 어디에 내놔도 부끄럽지 않은 검공(劍功)이라면서요?”

평소 틈만 나면 가전무공의 위대함을 자랑했던 왕가장의 후계자가 정색하고 대답했다.

“저는 도객이라 검공 안 익혔습니다.”

“네?”

“그리고 그걸 왜 나한테 떠넘깁니까? 정 말리고 싶으면 신 소저께서 나서시면 될 것 아닙니까?”

“어머. 별꼴이네, 진짜.”

산서오문의 후기지수들이 서로에게 차례를 미루던 그때, 가만히 상황을 지켜보던 혁무진이 불쑥 끼어들었다.

“쓸데없는 고민들 하시네. 나 같았으면 얼른 가서 한 손이라도 보탰소.”

“네놈, 아니 당신은 뭐요?”

워낙 무서운 광경이 눈앞에서 펼쳐지고 있으니 별것 아닌 무인 하나에게도 반존대를 써야 했다.

불과 일각 전 우진태에게 촉금을 선물로 받았던 황 소저도 재빨리 나섰다.

“미리 말해 두는데, 우리는 당신들한테 아무런 악감정이 없어요. 알죠?”

“그래요? 정 그렇다면 뭐, 그렇다고 칩시다.”

“그렇다고 치는 게 아니라 사실이 그렇다는 말이에요.”

“그걸 나한테 말해 봤자 무슨 소용이겠습니까?”

혁무진이 실실 웃으며 우진태를 신명 나게 두들겨 패고 있는 진태경의 뒷모습을 턱짓으로 가리켰다.

“우리 조장님이 한 성깔 하시거든요. 저기 신명 나게 맞고 있는 분이 쓰러지면 다음 차례는 누가 될까…… 거기 공자님? 아니면 옆에 계신 소저?”

“…….”

“아, 혹시나 해서 말해 두는데 저 양반은 남녀 구분 없이 다 때립니다.”

“나, 난 안 웃었소!”

“저도 마찬가지예요!”

“똑같은 말 두 번 해야 합니까? 나한테 말해도 소용없다니까요. 아, 그나마 가능성이 있는 방법이 하나 있긴 하네.”

“방법?”

후기지수들의 귀가 번쩍 뜨였다.

다들 그동안 무공을 아주 공으로 익힌 것은 아닌지라, 저 괴물 같은 청년을 상대로는 승산이 없음을 깨닫고 있었다.

“사, 사람 살려…….”

때마침 귓가로 흘러 들어온 우진태의 죽어 가는 목소리는 생존 본능에 더욱 불을 지폈다.

“그, 그 방법이란 게 도대체 뭐요?”

혁무진이 짐짓 심각한 얼굴로 턱을 쓸었다.

“글쎄, 이거 하나같이 방귀깨나 뀌는 집 자제분들이라 할 수 있으실지 모르겠는데.”

“하겠소!”

“할게요! 무조건 할게요!”

“음. 기본이 됐군요.”

흡족한 얼굴로 고개를 끄덕인 혁무진이 입을 헤 벌린 채 일방적인 구타를 구경하던 청풍을 가리켰다.

“우선 여기 계신 이분께 정중히 사과할 것.”

말이 끝나기가 무섭게 산서오문의 자제들이 허리를 접었다.

“진심으로 사과드리겠소.”

“겉모습만 보고 섣부른 판단을 했던 점. 정말 죄송스럽게 생각해요.”

청풍이 뒤통수를 긁적였다.

“전 괜찮으니 다들 일어나세요.”

앞서 많은 사람 앞에서 비웃음을 당한 것 치고는 너무 흔쾌히 용서해 주어 되레 혁무진이 당황했다.

심지어 불쾌함에 응당 붉어져 있어야 할 안색은 해맑기까지 했다.

“이렇게 쉽게 말입니까?”

“네. 무슨 문제라도 있나요?”

“그건 아니지만…… 아까 화나시지 않았습니까? 이렇게 공공연한 장소에서 모욕을 당하셨는데.”

“화가 왜 나요? 그냥 좀 신기한데.”

“예? 그게 무슨.”

“아까처럼 많은 사람이 저를 주목한 건 처음이었거든요. 절 무시한 사람한테 사과받는 것도 처음이라 신기하고 재밌던데요.”

“…….”

“아, 역시 하산하길 잘한 것 같아요.”

이놈도 살짝 맛이 갔구나.

해괴한 사람을 보는 듯한 눈빛으로 청풍을 바라보던 혁무진이 고개를 절레절레 저으며 후기지수들을 바라봤다.

“들으셨죠? 여기 계신 소협께서 사과를 받으셨으니 이 문제는 여기서 마무리 짓겠습니다.”

“오오!”

“오오오, 살았다!”

그러나 혁무진의 말은 거기서 끝나지 않았다.

“자, 그럼 마지막 두 번째가 남았습니다.”

“……두 번째라니?”

“더 있어요?”

“네, 이게 가장 중요합니다.”

이윽고, 그가 자신을 바라보는 네 남녀를 향해 엄숙하게 선언했다.

“다들 대가리 박으십쇼.”

“……!”

“……!”
```

## Current accepted English baseline

```markdown
# Chapter 134

*Smack!*

Woo Jintae’s head snapped to the side with a satisfyingly solid sound. He blankly stroked his cheek.

*What just happened?*

He was dumbfounded.

Had he just been slapped? By a punk like this?

Woo Jintae was nearing thirty. Thanks to marrying young, he already had a family of his own.

And now he had suffered this humiliation at the hands of some kid who couldn’t have been more than twenty.

“Eek! Young Hero Woo!”

“H-Hyung, are you all right?”

“Isn’t that the Young Bureau Head of the Seongun Escort Bureau?”

“That’s him. My goodness, what kind of reckless bastard would… Wait. Doesn’t that face look familiar?”

The belated reactions of the young prodigies and the stares of the inn’s guests doubled Woo Jintae’s shame.

He glared at the little bastard in front of him with eyes full of killing intent.

“How dare you…”

“That’s not the right way to put it.”

“What?”

“Not *how dare you*. You should be asking *how did you do that?* If you’re a martial artist.”

Woo Jintae froze for a moment.

Since childhood, he had received the full support of the Seongun Escort Bureau, taking in all kinds of elixirs and First Rate martial arts. Even if he hadn’t been born with extraordinary talent, it was only natural that he took pride in being a move and a half ahead of the other young prodigies.

*How did I get beaten so easily?*

He hadn’t even seen when or how the bastard approached him. All he had felt was the humiliation of being utterly disgraced in front of everyone.

Only then did Woo Jintae study his opponent with eyes full of caution.

“Look at those eyes darting around. What, do you want me to tell you my three measurements?”

“Which sect are you from, and who are you?”

“I’m Tien Shinhan of the Dodong Sect, you son of a bitch.”

The only reason Woo Jintae managed to endure the young bastard’s profanity was that his reason had finally returned.

In the Murim, you never knew what might happen. If the other man was a disciple of a great sect, Woo Jintae would have to withdraw cleanly.

*The Dodong Sect? The Dodong Sect’s Tien Shinhan?*

Both the sect and the man’s name were utterly unfamiliar. Woo Jintae glanced back. The other young prodigies wore equally bewildered expressions.

His mind began racing.

*As far as I know, there’s no such sect as the Dodong Sect in Shanxi Province.*

Opening a new sect in Shanxi Province, where all the established sects had already secured their positions, was nearly impossible.

Even without interference from the other sects, word would spread immediately.

*If they raised a young prodigy of this level at that age, they must be a sect with considerable power… Where are they from? Shaanxi? Henan?*

That was when the young martial artist who had been standing idly by as though none of this concerned him suddenly asked,

“What’s the Dodong Sect? Is it a real sect?”

“Would it be? A well-told lie becomes fact before you know it.”

“Ah. I’ll engrave those golden words in my heart.”

“You little punk. You’re speaking nicely for once.”

A young man dressed in rags like a beggar added his own comment.

“A well-told lie becomes fact… Those are wise words. I can sense profound wisdom in them.”

“Ah… yes. Thank you for the compliment, at least.”

Sparks flew from Woo Jintae’s eyes as he listened to the three of them.

“You bastard! Reveal your identity!”

“What, you want to hear who I am and where I’m from, then pick a fight if I seem easy and tuck your tail between your legs and apologize if I turn out to be too high-status?”

“…”

It was a crude statement, but it struck the bull’s-eye. Seeing Woo Jintae unable to answer, the young bastard clicked his tongue.

“Punk, you started with the wrong question. They say the one who farted gets angry. If you wanted an answer from me, you should’ve apologized first.”

Woo Jintae bit down on his lip.

An apology?

Born the sole male heir the Seongun Escort Bureau’s family had produced in three generations, he had been pampered and revered his entire life. He wasn’t flexible enough to bow his head to some nobody whose origins he didn’t even know.

At last, Woo Jintae made up his mind and gave the young prodigies of the Five Gates of Shanxi a subtle signal with his eyes.

*No matter how strong he is, he can’t be that strong.*

There were only three opponents. On their side were five First Rate masters, all among Shanxi Province’s foremost young prodigies.

Seeing the four men and women discreetly gripping their weapons in response to his signal, Woo Jintae felt reassured.

“Do you know who I am—or rather, who we are?”

“I happen to know your names, at least. But is that an apology?”

“An apology? You’ve got some nerve.”

Woo Jintae gave a thin smile.

“We are the heirs of the Five Gates of Shanxi. Surely you can’t claim not to know the Five Gates of Shanxi.”

“I’ll say I know. But are you really not going to apologize? This is your final warning.”

“I’ll give you a warning, too. I don’t know where you came from, but you picked the wrong person to mess with—”

*Smack!*

Woo Jintae’s vision flashed white.

As he instinctively stumbled backward, lightning-fast slaps struck him one after another.

*Smack! Smack! Smack-smack!*

One slap with every step.

After taking five slaps in all, Woo Jintae staggered unsteadily.

Because the blows had relentlessly targeted one side, his cheek had swollen grotesquely. Blood pooled inside his split mouth.

*Even my father never hit me.*

It was the first humiliation of his life—and it had happened in front of everyone.

His eyes rolled wildly.

“You fucking—!”

“I told you, final warning. Do you not know what *final* means, or what *warning* means? Or both?”

“How dare you hit me?”

“I may be the first man ever to treat you so casually, but please don’t fall in love with me. I’m busy enough loving one Song-i.”

“I’ll kill you!”

“I’ll beat you!”

*Smack-smack-smack!*

“Guh!”

Woo Jintae couldn’t regain his senses.

There was no internal energy behind the blows, nor did his opponent seem to be using any mystical manoeuvre technique. And yet Woo Jintae had no way to block the storm of slaps raining down on both his cheeks.

*How is this happening?*

As he was beaten helplessly, a crazed shout rang in his ears.

“Slap with the left hand, slap with the right hand!”

*Smack-smack!*

“One chi, two chi, three chi, four chi—Ppukku cheek! Ppukku cheek!”

*Smack-smack-smack!*

He kept shouting words that made no sense while flinging slap after slap. He looked like a madman born for the sole purpose of smacking people across the face.

Just like right now.

“Raise your left hand and lower your right. Lower your right and lower your left. Lower your left, and don’t raise your right.”

“Hurk!”

“That’s right. Good job. As a reward, your teacher will give little Woo Jintae’s cheeks a thorough beating.”

*Smack-smack-smack-smack!*

How many times had he been struck in the space of less than a moment?

Thirty? Fifty?

He had been hit so frantically that his head rang and tears swam in his eyes.

In the end, all Woo Jintae could do was call for help.

“P-please! Somebody help me!”

* * *

The Young Bureau Head of the Seongun Escort Bureau—the very Seongun Escort Bureau whose wealth alone was said to rival that of the Jin Family of Taiyuan, the richest family in Shanxi—cried out in desperation.

“P-please help me!”

Having thrown away his pride and everything else, Woo Jintae’s desperate plea still failed to make the young prodigies of the Five Gates of Shanxi draw their weapons.

“How are we supposed to beat that…?”

Someone’s groan spoke for everyone.

They were right. There was no need to experience it firsthand.

Just watching from the side was enough to make their knees go weak and their legs tremble. Their opponent was roughly the same age as them, but there was no question that he was a master far beyond their imagination.

“To reach that realm at his age…”

“That thing’s a complete monster.”

*Smack-smack!*

“P-please spare my life!”

Woo Jintae’s voice grew even more desperate. Even his plea for help had subtly changed.

If this continued much longer, he might start begging them to kill him instead.

“We, we should help him, right?”

“At the very least, we should try to stop him… Young Master Wang, do something.”

“Me? Why am I suddenly involved?”

“Why do you think? Every time we got together, you bragged about your family’s martial arts. You said it was sword arts you could display anywhere in the Central Plains without shame.”

The heir of the Wang Family Estate, who had boasted endlessly about the greatness of his family’s martial arts, answered with a stern expression.

“I’m a saber user. I never learned sword arts.”

“What?”

“And why are you trying to dump this on me? If Young Lady Shin wants to stop him so badly, she can step in herself.”

“My goodness. What a ridiculous thing to say.”

That was when the young prodigies of the Five Gates began shoving the responsibility onto one another.

Hyuk Mujin, who had been quietly watching the situation, suddenly cut in.

“You’re all worrying over nothing. If it were me, I’d hurry over and lend a hand, at least.”

“You—no, you. Who are you?”

With such a terrifying scene unfolding before them, they had to speak with even an ordinary martial artist using half-polite language.

Young Lady Hwang, who had received Shu brocade as a gift from Woo Jintae only moments earlier, quickly stepped forward.

“Let me make this clear in advance. We have no ill feelings toward you people. You know that, right?”

“Do you? If that’s how it is, then fine. Let’s say that’s how it is.”

“I’m not saying we should just say that. I’m saying it’s the truth.”

“What good does telling me do?”

Hyuk Mujin smiled thinly and jerked his chin toward Jin Taekyung’s back, where he was enthusiastically beating Woo Jintae.

“Our Captain has quite a temper. Once the gentleman getting beaten over there collapses, who do you think will be next? You, Young Master? Or the Young Lady beside you?”

“…”

“Oh, and just in case you’re wondering, that man hits men and women alike.”

“I-I didn’t laugh!”

“Neither did I!”

“Do I have to say the same thing twice? Telling me won’t do you any good. Though, there is one way that might work.”

“A way?”

The young prodigies’ ears perked up.

They hadn’t trained in martial arts for nothing. They understood that they had no chance against that monstrous young man.

“P-please… somebody save me…”

Woo Jintae’s dying voice happened to drift into their ears, fanning their survival instincts even further.

“W-what exactly is this way?”

Hyuk Mujin stroked his chin with a deliberately serious expression.

“Well, you’re all children of families that can fart with the best of them, so I don’t know whether you’ll be able to do it.”

“I will!”

“I’ll do it! I’ll definitely do it!”

“Good. You know the basics.”

Hyuk Mujin nodded with satisfaction and pointed to Cheongpung, who was watching the one-sided beating with his mouth hanging open.

“First, apologize politely to this gentleman.”

Before he had even finished speaking, the young men and women of the Five Gates bent at the waist.

“We sincerely apologize.”

“We’re truly sorry for judging you rashly based on your appearance.”

Cheongpung scratched the back of his head.

“I’m fine, so everyone can stand up.”

Hyuk Mujin was taken aback by how readily Cheongpung forgave them, especially after they had mocked him in front of so many people.

Even the expression on his face, which should have been flushed with anger, was sunny and bright.

“You’re saying that so easily?”

“Yes. Is there a problem?”

“It’s not that, but… Weren’t you angry earlier? You were insulted so publicly.”

“Why would I be angry? I just thought it was fascinating.”

“What?”

“It was the first time so many people had focused on me like that. It was also the first time someone who had looked down on me apologized. I thought it was fascinating and fun.”

“…”

“Ah. I think coming down from the mountain was a good decision.”

*This guy’s a little nuts, too.*

Hyuk Mujin looked at Cheongpung as though he were some strange creature, then shook his head and turned to the young prodigies.

“You heard him, right? Since the Young Hero here has accepted your apology, we’ll consider the matter settled.”

“Oh!”

“We’re saved!”

But Hyuk Mujin wasn’t finished.

“All right, then. There’s one final thing left—the second.”

“…The second?”

“There’s more?”

“Yes. This is the most important one.”

Then, with a solemn expression, he declared to the four men and women looking at him,

“All of you, bend over and plant your heads on the floor.”

“……!”

“……”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 134`.

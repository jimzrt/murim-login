# Master Edit Task — Chapter 127

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

| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 무신     | **Martial God**               | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 마교     | **Demonic Cult**                                 |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 대주     | **Squad Leader** / **Commander**             |
| 큰형     | **eldest brother**                           |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 화북 | **North China** | Regional designation used when discussing Shanxi drinking culture. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 큰형 | kinship | Eldest older brother, not a generic older brother. | |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 120–124

## Plot

Jin Taekyung kills Pung Yang with the Unnamed Sword after its Ten-Thousand-Year Cold Iron destroys Pung Yang’s Body-Protecting Qi. The victory completes the Temporary Strength Pill Quest, restoring Taekyung’s health and granting five level-ups, substantial EXP and Fame, and medicines that save many wounded Mount Heng Sword Sect survivors. Taekyung also fully absorbs the Blazing Flame Divine Pill, reaching forty-five years of internal energy with the Scorching Yang Qi attribute.

The Mount Heng Sword Sect is devastated, but Lee Seowol remains Sect Leader and vows to rebuild it. She accepts Jin Wikyung’s invitation to the Jin Family of Taiyuan’s New Year gathering and offers the Jin Family the sect’s territorial rights as an apology. She also offers the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist in exchange for marrying Taekyung. Taekyung initially rejects the proposal because Seowol is seventeen and because he loves Song Song, while Jin Mukyung insists that the three Peak martial arts make the marriage worthwhile.

Taekyung reveals that Jopil left behind the Flame Divine Palm, a Supreme Peak secret art of the Fire Gate Clan restricted to practitioners with Scorching Yang Qi. Mukyung warns that possessing another sect’s secret technique could make the Jin Family thieves in the eyes of the Murim. The art belonged to the Fire King, one of the world’s twenty greatest experts, whose survival after a legendary battle at Mount Jiuhua remains unknown. Mukyung returns to the Jin Family while still recovering, accompanied by Hyuk Mujin. Wolhwa departs to tour northern Shanxi and promises to maintain close ties with the Jin Family. After the carriage leaves, Lee Seowol appears and addresses Taekyung as Benefactor.

## Continuity

- Pung Yang is dead, and the Red Wind Band’s remaining forces and wider response to his death remain unresolved.
- Taekyung has fully absorbed the Blazing Flame Divine Pill and possesses forty-five years of internal energy with the Scorching Yang Qi attribute.
- The Temporary Strength Pill Quest granted Taekyung five level-ups, major EXP and Fame, and Full Recovery; the pill’s origin and long-term effects remain unknown.
- Jin Mukyung survived his Internal Injuries and can travel, but he is not fully recovered.
- Cheol Mubaek has broken limbs and serious Internal Injuries and requires at least four months of recuperation.
- Twenty-five Mount Heng survivors remain, including Lee Seowol; five were initially unlikely to survive. The sect’s reconstruction remains uncertain.
- Lee Seowol is seventeen, remains Sect Leader, accepted the New Year invitation, and has proposed marriage to Taekyung in exchange for three Peak martial arts.
- Taekyung intends to reject Seowol’s political marriage because he loves Song Song, but the proposal and territorial transaction have not been resolved.
- Cheol Mubaek gave Lee Seowol the Shura Annihilating Fist manual despite its single-successor, transmission-only-to-the-worthy tradition.
- Taekyung possesses Jopil’s Flame Divine Palm manual. Jopil claimed to be its nineteenth-generation successor, but how he obtained it and whether the claim is true remain uncertain.
- The Flame Divine Palm is a Fire Gate Clan secret art restricted to owners of Scorching Yang Qi. The Fire Gate Clan follows a single-successor tradition.
- The Fire King, the art’s legendary master, may still be alive.
- Wolhwa is Eun Sowol, the Lower District Sect’s Shanxi Branch Leader, and plans to tour northern Shanxi while preserving the alliance with the Jin Family.

## Translation Decisions

- Retain **Peak**, **Supreme Peak**, **Internal Injury**, **Severe Injury**, **Body-Protecting Qi**, **Scorching Yang Qi**, **Red Wind Band**, **Sect Leader**, **Benefactor**, and **Taiyuan Jin Family**.
- Render **잠력단** as **Temporary Strength Pill**, **열화신단** as **Blazing Flame Divine Pill**, **완전 회복** as **Full Recovery**, **만년한철** as **Ten-Thousand-Year Cold Iron**, and **이름 없는 검** as **Unnamed Sword**.
- Render **혈랑검법** as **Blood Wolf Sword Technique**, **혈랑보법** as **Blood Wolf Footwork**, **절정 무공** as **Peak martial arts**, **파천신권** as **Shura Annihilating Fist**, and **열화문** as **Fire Gate Clan**.
- Render **화왕** as **Fire King**, **구화산** as **Mount Jiuhua**, **진무보법** as **Jin Family’s Manoeuvre Technique**, **일인전승** as **single successor**, and **비인부전** as **transmission only to the worthy**.
- Preserve the Samsung/Samseong pun with a clarifying footnote; retain **Jaringobi** with its explanatory footnote.

### Prior accepted reading-copy tails

#### Chapter 125 tail (verified mastered)

…
that the wounds were beginning to close. *Because everyone who caused them is dead.* The Head Elder and Lee Cheonbaek, each of whom had dreamed of revenge, had already met their ends. Wasn’t that why we had raced here day and night to save the Mount Heng Sword Sect? With a sincere apology and forgiveness… wounds could heal, even if the scars remained. Just as they were now. “I won’t accept your apology.” The words came out only after considerable thought. Without waiting for anyone else to react, I continued. “I’m not someone with the right to receive your apology or forgive you.” No one here had that right. The people they needed to apologize to were back at the Jin Family of Taiyuan. Lee Seowol and Cheol Mubaek seemed to understand. Both nodded. “I’ll see you on New Year’s Day.” “Taiyuan, is it? It will be my first journey away from home in thirty years.” The Mount Heng Sword Sect would hardly be a welcome guest. Especially now, diminished to such a pitiful state, they might have to endure all manner of humiliation and disgrace. But that was something they would have to bear themselves. There was nothing I could do, nor any reason for me to interfere. *Well done.* With Jin Mukyung’s brief Sound Transmission in my ear, I offered one last farewell. “Then we’ll be going.” I had just turned toward the carriage when Lee Seowol called out. “Benefactor.” “Yes?” “Did you know there are fewer than fifteen days left until New Year’s Day?” Her voice babbled on like a little stream. “I’m looking forward to hearing the answer I didn’t get last time.” I could only open and close my mouth in confusion as Jin Mukyung grabbed me and dragged me away. With Cheol Mubaek’s distinctly displeased cough sounding behind us, the carriage set off at full speed. * * * The journey back to the Jin Family of Taiyuan was quick and smooth. The coachman’s skill played a part, but with the impatience gone from my heart, everything seemed that way. “Phew.” Jin Mukyung had just finished circulating his qi when he suddenly muttered, “Now that I think about it, I didn’t even get to see a Peak martial art.” He had joined us after Jin Wikyung lured him in with the promise that he could see Peak martial arts at Mount Heng. I answered him calmly. “It’s fine. Thanks to Pung Yang, you got to see Mount Beimang.” “You call that consolation?” “No. I was making fun of you.” Bones cracked in Jin Mukyung’s hand. “You’ve grown a lot.” “Want to spar once your injuries are fully healed?” “I could do it right now… Urgh.” Jin Mukyung tried to spring to his feet, then immediately frowned. No matter how quickly he recovered, it had only been four days. That was nowhere near enough time for his injuries to heal completely. He collapsed back into his seat and glared at me. “Consider yourself lucky.” “I don’t know about lucky, but my lifeline sure is damn thick.” Considering how I kept surviving every brush with death, I must have been born with an unusually sturdy lifeline. Either that, or I had been blessed with heaven’s fortune. “Anyway, you did well.” “Huh?” “Eeeh?” Hyuk Mujin and I both widened our eyes at the unexpected praise sticker. Jin Mukyung looked at us as if he couldn’t understand what was wrong. “Why are you looking at me like that? You look as if you’ve heard something you weren’t supposed to.” “You’re practically a ghost.” “Wait, could Pung Yang have already killed you? Are you sitting here as a vengeful spirit?” It was a fairly plausible theory, but around Jin Mukyung, you had to watch your mouth at all times. As I watched Hyuk Mujin get beaten until dust flew, I felt around inside my robes. *Inventory open. Summon.* The next moment, my fingertips touched something round and hard. It was the only thing Pung Yang had left behind. No—the only thing I had taken from him. *Check Item.* *Ding.* > **System** > > **Item Window** > > **Temporary Strength Pill** > > **Type:** Elixir > **Grade:** ??? > **Restriction:** Peak martial artist or higher > **Description:** A pill manufactured by an unknown person. It greatly raises the user’s latent power for about one shichen, but a price must be paid in return. Do not take it except in the worst-case scenario. > **Effect:** Combat-related stats +100 > > **Internal energy:** +15 years > > **Body-Protecting Qi:** Available Even accounting for the short time limit, its effects were monstrous. I could understand why Pung Yang had been so confident. I had no idea how severe the aftereffects were, but if my life were in danger, I’d swallow twenty of them, not two. Obviously. But something else bothered me. *An elixir manufactured by an unknown person.* The Item’s Grade was marked with question marks, its exact aftereffects weren’t listed, and even its maker was shrouded in mystery. What kind of bastard had created something this bizarre? *This thing reeks of something shady.* I was rolling the Temporary Strength Pill around in my palm, lost in thought, when a distant cry drifted toward us. “Mukyuuung! Taekyuuung!” Jin Mukyung froze in the middle of enthusiastically hammering Hyuk Mujin’s forehead. “Was that a hallucination?” Yeah, no. [^1]: A jiazi is a traditional sixty-year cycle.

#### Chapter 126 tail (verified mastered)

…
“He was the strongest opponent I’ve ever fought. No—to be precise, I should say he *became* that strong.” “Became?” “What do you mean by that...?” “The instant he swallowed a blood-red pill, he became terrifyingly powerful.” At last, the conversation had reached the Temporary Strength Pill. I tried to act as naturally as possible. *I can’t let them find out I have it.* The Temporary Strength Pill was a poisoned chalice. It was undeniably ominous and suspicious, but its tremendous effects couldn’t be ignored. I had already decided to use it as a second-worst contingency for the worst possible moment—when I was facing death. “It was only for a brief moment, but when he was about to take the pill, I clearly saw that one pill remained inside the wooden case...” Jin Mukyung trailed off and looked at me. “Did you happen to find anything on Pung Yang’s person afterward?” “Hm? Like what?” “A wooden case. Or the red pill I mentioned.” I deliberately furrowed my brow. “I’m not sure. I searched him afterward to see if he had anything, but a bunch of wooden splinters spilled out. Maybe those were pieces of the case?” “Then the pill? The pill?” “No idea. I was half-dead myself. How was I supposed to search through everything?” It was a fairly convincing excuse. It wasn’t as though only one or two people had died, and the battle had been brutally fierce. It was only natural that I’d been too exhausted to search properly. What more could he say? “Is that so?” “The people from the Mount Heng Sword Sect might have found it. Or it could have dissolved into one of the countless pools of blood scattered across the ground.” “Hmm.” Jin Mukyung stared at me with faint suspicion, but I merely shrugged. *You won’t find it even if you search, idiot.* I had tucked it safely into a corner of the greatest vault in existence—my Inventory, which only I could open and close. Neither Jin Mukyung nor the greatest thief under heaven could touch a hair of the Temporary Strength Pill. *It really is convenient.* While I marveled once more at the convenience of the System, Jin Wikyung and Wipeng began speculating about the pill’s origins. “It must be a relic of demonic, heterodox arts. I remember hearing that quite a few pills with similar effects were used during the Great Faction War.” “Northern Shanxi, including Gaoyuan, once fell into the hands of the Demonic Cult. If Pung Yang discovered some remnant they left behind, it would make sense.” I had been listening with my ears perked up when I suddenly froze. *Wait. The Demonic Cult?* The Demonic Cult was a regular fixture you could never leave out of a Murim novel, the licorice in every medicine shop, and Geum Jandi’s honorary firefighter.[^2] Of course, it wasn’t a religious organization devoted to world peace and helping the poor. It was more like IS—the Islamic terrorist group. In short, they were a bunch of fanatics you had absolutely nothing to gain from getting involved with. *What if the Demonic Cult made the Temporary Strength Pill?* Pung Yang’s eyes had been stained red, like a demon that had just climbed out of hell. The pill had granted him unimaginable power, even if only temporarily. *I’m starting to see the picture.* This felt wrong. Really fucking wrong! But nothing could be gained without suffering. The side effects should be something I could endure... “The best-known pill used by the Demonic Cult at the time was the Blood-Exploding Pill, if memory serves.” “I’ve only heard stories about it. Don’t all the blood vessels in the user’s body burst after two shichen, killing them?” “That was the price of trying to gain power through dark arts.” “If the Blood-Exploding Pill was that terrible, just how severe would the side effects of Pung Yang’s pill be?” “I don’t know, but they must be beyond imagination. It wouldn’t just damage his innate qi. Once the time limit ended, his body would suffer tremendous strain. In the end, the pill uses the body itself as kindling and burns it for a brief period.” I swallowed dryly. Before I knew it, my voice had jumped out. “And after that?” “It was made by the Demonic Cult. What else would you expect? Once the demonic qi surges into your very marrow… you’d become a murderous fiend who knows nothing but blood.” “...A murderous fiend? The demonic qi surges into his marrow?” “If an item like that fell into the hands of a villain, it would be a true disaster… Taekyung, what’s wrong?” Jin Wikyung looked at me with concern. I rubbed my forehead and found it covered in beads of sweat. “Nothing. I’m just a little hot.” “What are you talking about? It’s snowing outside.” “What would a Soeumin know? I’m a Taeyangin. That’s why…”[^3] Damn it. I didn’t even know what I was saying anymore. I gave the three of them an awkward smile. “There’s something I forgot earlier.” “…?” “…?” “…?” “That pill. Now that I think about it, I have it. Heh-heh. Heh-heh-heh.” “…!” “…!” “…!” [^1]: A jang is a traditional Korean unit of length measuring roughly three meters. [^2]: Geum Jandi is the heroine of the Korean drama *Boys Over Flowers*. [^3]: Soeumin and Taeyangin are two of the four constitutional types in traditional Korean Sasang medicine.

## Korean source

```text
＃127화



물음표가 느낌표로, 느낌표가 황당함과 분노로 바뀌는 데까지는 그리 오랜 시간이 걸리지 않았다.

가장 먼저 정적을 깬 것은 진무경이었다.

“너…….”

벌겋게 달아오른 얼굴, 거친 숨소리. 당장이라도 내 주둥이에 한 방 먹이고 싶은지 주먹이 움찔거린다.

‘음, 제대로 열받았군.’

싸늘하다. 가슴에 비수가 날아와 꽂힌다. 하지만 걱정하지 마라. 내게는 든든한 방패가 있으니까.

“어허, 무경아.”

나직하게 들리는 목소리에 진무경의 얼굴이 와락 일그러졌다.

“형님!”

“태경이도 다 생각이 있었겠지. 안 그러느냐?”

나는 짐짓 눈을 내리깔았다.

“아닙니다. 소제(小弟)의 생각이 짧았습니다.”

“응?”

“호기심에 그만…… 하지만 큰형님의 이야기를 듣고 깨달았습니다. 그것은 결코 갖고 있어서도, 숨겨서도 안 되는 물건이라는 사실을 말입니다.”

생각만 해도 치가 떨린다는 듯이 주먹을 부르르 떠는 연출도 잊지 않았다.

“마교! 그 악독한 놈들의 이름만 들어도 치가 떨립니다!”

이건 진심이다. 기왕 만드는 거 잘 좀 만들지, 광기에 젖은 살인귀가 되는 심각한 결함이 있다니!

“허어.”

나를 바라보는 진위경의 눈빛에 애정이 듬뿍 담겨 있었다.

“나중에 커서 협의지사가 되겠다던 작고 귀여운 꼬마 아이가 생각나는구나. 그때 네 나이가 여섯 살이었다. 기억나느냐?”

당연히 안 나지.

재작년 일도 가물가물한데 이 몸의 원주인이 여섯 살 때 뭘 했는지 알 턱이 있나. 그러나 나는 비장하게 고개를 끄덕였다.

“똑똑히 기억합니다. 제 유일한 꿈이었으니까요.”

협의지사건 경기도지사건, 오늘 이 시간부로 그게 내 여섯 살 때 장래 희망이다.

“허허, 그 어린 녀석이 이렇게 훌륭히 장성하다니.”

흐뭇하게 웃은 진위경이 이번엔 다른 두 사람을 향해 고개를 돌렸다.

“그 자리에 자네도 있었지. 위팽, 기억나는가?”

위팽이 숨도 쉬지 않고 대답했다.

“그건 모르겠고, 그러고서 딱 십 년 후부터 계집질 시작한 건 기억납니다. 커서 뭐가 될 거냐고 물었더니 그때는 천하제일의 풍류남아라고 하던데요.”

“영웅이라면 모름지기 풍류를 알아야지.”

“무공은 쥐뿔도 모르는데 풍류만 알아서 뭐 합니까? 말씀하시는 영웅이 밤의 영웅, 기녀들의 영웅. 뭐 그런 겁니까?”

“조용히 하게. 우리 막내는 어릴 때부터 싹수가 남달랐어.”

“그러니까 그 싹수가…… 어후, 됐습니다. 내가 말을 말아야지.”

벌컥벌컥.

술을 병째로 들이붓는 위팽을 깔끔하게 무시한 진위경의 시선이 다음 주자를 향했다.

“무경아. 이제 막내의 진심을 알았으니 화 풀거라.”

오만상을 쓰고 있던 진무경이 입을 뗐다.

“저 자식 한 대만 때리면 안 됩니까?”

“어허.”

“딱 한 대만. 제발.”

싸늘한 목소리에 내가 재빨리 고개를 숙였다.

“이 못난 아우를 용서하십시오, 둘째 형님.”

“지금까지 반말 찍찍 하던 놈이 형님 같은 소리 하네.”

“예? 제가요?”

“그만해라. 마지막 경고다.”

“아닙니다. 차라리 절 때리십시오. 그렇게라도 형님의 분이 풀리신다면 이 아우, 기꺼이 감내하겠습니다.”

“야, 이 새끼야!”

벌떡 일어난 진무경이 헉, 하는 신음과 함께 도로 주저앉았다. 가슴팍에 동여맨 붕대가 붉게 젖어 드는 걸 보니 상처가 벌어진 모양이다.

“아이고 형님, 괜찮으십니까!”

“이 자식이 또…… 커헉!”

“의원, 의원!”

순식간에 난장판이 되어 버린 술자리.

묵묵히 두 번째 술병을 집어 든 위팽이 중얼거렸다.

“가문 꼴 잘 돌아간다…….”

얼마나 잘 돌아가는지, 무려 산서제일가다.



* * *



결국, 의원이 다녀가고 나서야 분위기가 수습됐다.

나를 찢어 죽일 듯한 진무경의 시선을 외면하고 잠력단을 품에서 꺼냈다.

“바로 이겁니다.”

마치 피를 응축시킨 것처럼 온통 붉은 단환.

진위경과 위팽이 잠력단을 유심히 살폈다.

“위팽, 어떻게 생각하나?”

“보기만 해도 피비린내가 나는군요. 흉악한 물건입니다.”

“정말 마교 쪽에서 만든 걸까?”

“글쎄요. 그렇다면 마기가 느껴져야 하는데…… 저로서는 확신하기 어렵습니다.”

“그렇지? 뭔가 달라.”

두 사람의 표정은 몹시 심각했다. 잠력단을 어디서, 누가 만들었는지 궁금한 건 나도 매한가지라 힌트를 던져 주기로 했다.

“잠력단이라고 하던데요.”

“잠력단?”

“네, 풍양의 입으로 직접 들었어요.”

진무경이 불쑥 끼어들었다.

“풍양이? 도대체 언제?”

“너 기절해 있을 때요.”

“……후욱. 후우욱.”

누가 뭐라고 하든 내가 유일한 목격자고 증인이다. 본전도 못 찾은 진무경이 화를 가라앉히려 호흡을 가다듬을 때, 다른 두 사람은 미간의 골만 깊어지고 있었다.

“잠력단이라, 위팽?”

“저도 처음 들어 봅니다. 이 정도 효력에 마교의 물건이라면 분명 정마대전 때 쓰였을 터인데…….”

“마교가 아닐 수도 있지 않아요?”

두 사람의 시선이 날 향했다.

“마교가 아니다?”

“어찌 그렇게 생각하십니까?”

“처음부터 단정 지을 필요는 없다 이거죠.”

사실 마교가 만든 단환이 아니라면 다시 가져갈 수 있을까 하는 희망 사항에서 나온 말이다.

물론 내 나름대로 달리 떠오른 생각도 있었고.

‘대장로.’

지난번 전쟁에서 표면적으로 드러난 적은 분명 항산검문이었지만 진정한 적은 대장로, 바로 그였다.

이분법적인 추측보다는 제3의 세력이 있을지도 모른다는 가능성을 늘 염두에 둬야 한다는 것이 내 생각이다.

“뭐, 그냥 갑자기 그런 생각이 들었다는 거죠.”

내 말을 모두 들은 두 사람의 표정이 심상치 않다. 그리고 다음 순간, 위팽의 입에서 아주 작은 목소리가 흘러나왔다.

그것은 무의식중에 신음처럼 흘러나온 한 단어였다.

“암천…….”

“위팽.”

진위경의 날카로운 눈빛이 이어지는 말을 틀어막았다.

“아, 죄송합니다. 제가 실언을.”

황급히 얼버무리는 위팽. 하지만 이미 늦었다.

암천이라는 두 글자가 내 뇌리에 깊게 박힌 후였으니까.

‘암천? 그게 뭐지?’

그때, 예상치 못한 일이 일어났다.

띠링.



- [암천]에 관한 미약한 정보를 얻었습니다.

- [잠력단]에 관한 아이템 설명이 변경됩니다.



느닷없는 시스템 알림. 나는 잠력단을 들고 있는 위팽에게 손을 내밀었다.

“제가 잠깐 확인해 봐도 될까요?”

“아, 물론입니다.”

아이템 확인. 마음속으로 중얼거리자 곧장 잠력단에 관한 정보가 떴다.

변경된 정보를 찾는 것은 쉬운 일이었다.



아이템창



[잠력단]

종류 : 영단

등급 : ???

제한 : [절정 무인] 이상

설명 : [암천]이 제조한 단환. 약 한 시진 동안 복용자의 잠재된 힘을 대폭 끌어 올리는 대신, 그에 대한 대가가 뒤따른다. 최악의 경우가 아니고서는 복용하지 말 것.

효과 : 전투 관련 능력치 +100

[공력] +15년

[호신강기] 사용 가능





[알 수 없는 누군가]가 사라지고 [암천]이라는 생소한 단어가 그 자리를 채웠다.

‘문맥으로 봐서 어떤 모종의 단체인 건 확실한데…….’

뭐, 잠력단 같은 물건을 만드는 놈들이니 마교와 비교해도 그 나물에 그 밥일 게 뻔하다.

‘암천.’

누가 지었는지 작명 센스 하나는 끝내준다. 두 글자만으로 자신들이 수상쩍은 놈들이라는 걸 알려 주니까.

이 새끼들 분명히 뒤가 구린 놈들이다. 99퍼센트 확신한다.

‘진위경과 위팽은 뭔가 알고 있는 것 같은데.’

문제는 앞서 두 사람이 보인 반응으로 봤을 때 암천에 관한 정보 노출을 극도로 꺼릴 거라는 사실이다.

‘그래도 한 번 찔러 볼까?’

하지만 정작 내가 입을 열기도 전에, 진무경이 한발 빨리 물었다.

“암천? 그게 뭡니까?”

“그게…….”

진위경의 얼굴 위로 곤란한 빛이 스쳤다.

“미안하구나. 아직은 말해 줄 수 없다.”

동생들을 끔찍이 생각하는 그의 입에서 나온 말이다.

진위경이 이러는데 위팽에게는 물어볼 필요도 없다.

“두 공자님께는 죄송합니다만, 보다 명확해지기 전까지는 알려 드릴 수 없습니다.”

지금까지 보지 못했던 확고한 태도다. 나도, 진무경도 오늘은 이쯤에서 물러나야 한다는 사실을 깨달았다.

다만 그럴수록 암천에 대한 호기심은 더더욱 커져 갔다.

‘우리한테까지 감춰야 할 비밀이라 이거지.’

가문의 직계라는 혈통은 둘째치더라도, 나와 진무경은 태원진가의 핵심 고수다. 진위경의 오른팔이 위팽이라면 각자 왼팔, 한쪽 다리 역할 정도는 하고도 남는다.

‘그럼 가문 내에서도 두 사람만 아는 특급 기밀이라는 건데.’

나도 사람인지라 궁금해지는 건 어쩔 수 없다. 게다가 항산검문 때는 잠잠하던 시스템이 반응했다는 사실도 한몫했다.

‘암천, 잠력단, 진위경과 위팽만 아는 특급 기밀.’

몇 가지 키워드가 머릿속을 휙휙 스쳐 지나간다.

좋아, 결심했다.

‘신경 끄고 살아야지.’

과한 호기심은 명줄을 짧게 만드는 법이다. 항산검문에 우편 배달하러 갔다가 죽을 고비를 넘긴 지 며칠 되지도 않았다.

이름부터가 불길하기 짝이 없는 수수께끼의 단체? 엮였다가는 좋은 꼴 못 볼 게 뻔하다.

“자자, 이 얘기는 그만하고 술이나 한 잔씩들 할까?”

진위경이 억지로 분위기를 환기시킨다.

이미 혼자서 두 병을 아작 낸 위팽도, 부상당한 진무경도 잔을 채우는데 나라고 뺄 수 있나. 진위경이 따라 주는 술을 받아 쭉 들이켰다.

꿀꺽, 꿀꺽.

도수 높기로 악명이 자자한 화주(火酒)가 후끈한 열기와 함께 목을 타고 넘어갔다.

“크으으.”

이야, 이거 장난 아닌데?

도수 높은 거야 알고는 있었지만 직접 마셔 보니 생각 이상이다. 이 정도면 소주, 맥주는 명함도 못 내밀 것 같다.

몸을 부르르 떠는 나와는 달리 나머지 셋은 곧장 빈 술잔을 꽉꽉 채웠다.

“마셔!”

“들이부어!”

“죽을 때까지 달려!”

“…….”

산서성이 화북(華北) 지방에 속하며, 화북 사내들은 하나같이 엄청난 주당이라는 사실을 안 것은 술로 밤을 꼬박 지새우고 난 후였다.



* * *



다음 날 정오. 상쾌한 기분으로 말에 오르는 나를 혁무진이 괴물 보듯 바라봤다.

“속 괜찮으세요?”

“어, 괜찮은데?”

“혹시 어제 혼자 술 안 드신 건 아니죠? 아니면 중간에 주무셨다거나.”

“응, 넷이서 계속 마셨어.”

“……그걸 전부 다요?”

녀석이 입을 딱 벌렸다.

“그게 말이 됩니까? 사람이에요?”

“다 들어가더라.”

“세상에, 도대체 밤새 몇 병을 드신 겁니까?”

단위가 잘못됐다. ‘병’이 아니라 ‘통’이다.

무슨 해적 나오는 영화에서나 보던 거대한 술통을 끊임없이 비우고, 또 비웠다.

“글쎄, 한 스무 통 가까이 마신 것 같은데. 열 통 넘은 후로는 안 세어 봐서 모르겠다.”

“허, 정말 대단하십니다.”

혁무진이 감탄하며 엄지를 추켜세우는데 갑자기 객잔의 문이 열렸다.

그리고 세 마리의 좀비, 아니 세 명의 절정 고수가 모습을 드러낸다.

“흐어어.”

“우욱.”

“허억, 허억.”

창백한 안색, 바짝 마른 입술과 퀭한 눈동자.

한 명의 예외도 없이 발을 질질 끌며 마차로 쏙 들어가는 모습에 호위대의 무인들이 눈을 휘둥그레 떴다.

“갑자기 왜 마차를…….”

“상태가 많이 안 좋으신 것 같은데?”

“그럴 리가. 자네들 우리 대주님이랑 술 안 마셔 봤어? 주신(酒神) 위팽. 몰라?”

“대주님 별호는 귀검 아니었습니까?”

“모르긴 몰라도 주량으로 따지면 무신(武神)도 이길걸. 그냥 지금까지의 피로가 쌓여서 저러시는 거겠지.”

무인들이 쑥덕거리던 그때, 마차 문이 벌컥 열리더니 한 사람이 후다닥 뛰쳐나와 허리를 숙였다.

“꺼억, 끄우웨에에엑!”

촤르르르륵.

희멀건 액체만 한참 쏟아 내고 비틀비틀 마차로 복귀하는 위팽의 뒷모습에 한창 떠들던 무인이 얼떨떨한 목소리로 중얼거렸다.

“……이럴 리가 없는데.”

“이럴 리가 없긴. 저건 누가 봐도 숙취지. 잠도 안 주무시고 그렇게 마셔 댔으니 저러실 만도 해.”

“그럼 삼공자님은 왜 저렇게 멀쩡하신데?”

호위대의 시선이 내게로 쏠렸다. 전신에서 섬뜩할 정도로 풍기는 술 냄새. 하지만 그와는 반대로 상쾌하기 짝이 없는 얼굴과 편안한 호흡.

“설마?”

“삼공자님이 대주님을 이겼다고? 그 주신을?”

술렁이는 장내.

이제 혁무진은 감탄을 넘어 존경의 눈빛을 보내고 있었다.

“아아, 역시! 허구한 날 기녀들 끼고 술 마시던 조장님 수준!”

“…….”

“조장님이 삼 년만 더 술을 마셨으면 본가 기둥뿌리가 뽑혔을 거라는 총관님 말씀이 생각납니다. 이래서 항상 공금을 훔칠 수밖에 없었던 거였군요!”

“……야, 인마.”

단둘이 있는 것도 아니고, 그딴 식으로 말하면 내 이미지가 뭐가 되냐.

안 그래도 아까부터 사방에서 우수수 꽂혀 드는 시선에 얼굴이 따가울 지경이다.

“커흠. 커흐흠!”

헛기침하며 슬쩍 주위를 둘러봤는데 이게 웬걸. 시커먼 사내놈들 눈동자가 밤하늘 샛별보다 반짝거리는 중이다.

“진정한 주신, 주신이다.”

“태원 홍등가에서는 유명하시지. 야왕이라고 못 들어 봤나?”

“야왕? 별호만 들어도 알겠다. 원래 술 잘 드시는 걸로 정평이 나 있으셨구먼.”

“그게 아니라…… 그거. 그거.”

“허억. 정말인가?”

“나야 모르지. 본 적이 없으니까.”

“알고 보니 진정한 사내셨구먼.”

띠링.



- 이 자리에 모인 이들이 당신의 주량과 위용에 감탄합니다!

- 명성이 20 상승합니다!

- 명성이 22 상승합니다!

- 명성이 25 상승합니다!

- 특정 소문이 퍼질 시, 관련된 칭호를 얻을 수 있습니다.



“…….”

아니 시발, 명성 쭉쭉 오르는 거 뭔데.

그리고 관련된 칭호라니. 괜찮아, 넣어 둬. 제발 산서잠룡으로 만족하게 해 줘.

‘그만해. 이 미친놈들아…….’

이유 모를 수치심과 함께 고개를 돌린 나는, 내 특정 부위를 뚫어져라 바라보는 혁무진과 마주할 수 있었다.

“……뭐 하냐, 지금?”

“아, 잠깐 눈대중으로 재 보고 있었습니다.”

너무 당당하게 대답해서 당황스러울 정도다. 혁무진이 해맑게 웃으며 팔뚝을 내밀었다.

“이야, 역시 대단하십니다. 헤헤.”

나는 팔뚝에 대한 답례로 주먹을 내밀었다.

뻑!
```

## Current accepted English baseline

```markdown
# Chapter 127

It didn’t take long for the question marks to turn into exclamation points, and the exclamation points to turn into bewilderment and rage.

Jin Mukyung was the first to break the silence.

“You…”

His face was flushed red, and his breathing was rough. His fist twitched as if he wanted to plant one right in my mouth.

*Well, he’s really pissed.*

It was chilling. A dagger had flown straight into my chest.

But don’t worry. I had a sturdy shield.

“Now, now, Mukyung.”

At the quiet voice, Jin Mukyung’s face twisted violently.

“Eldest brother!”

“Taekyung must have had his reasons. Isn’t that right?”

I deliberately lowered my eyes.

“No, eldest brother. I was short-sighted.”

“Hm?”

“I let my curiosity get the better of me… But after hearing what Eldest Brother said, I realized something. It’s an object that should never be kept—or hidden.”

I didn’t forget to make a show of trembling my fist, as if merely thinking about it made my teeth chatter with rage.

“The Demonic Cult! Just hearing the name of those vile bastards makes me tremble with fury!”

This part was sincere. If you’re going to make something, make it properly. Why did it have such a serious defect that it turned people into deranged murderers?

“Good heavens.”

Jin Wikyung looked at me with eyes full of affection.

“I remember a small, adorable little boy who said he would grow up to become a chivalrous hero. You were six years old then. Do you remember?”

Of course I didn’t.

The events of the year before last were already hazy. How was I supposed to know what the original owner of this body had done at age six?

Still, I nodded solemnly.

“I remember it clearly. It was my only dream.”

Whether it was a chivalrous hero or the governor of Gyeonggi Province, as of this moment, that was my career aspiration at age six.

“Ha-ha. To think that little boy would grow up so splendidly.”

After laughing with satisfaction, Jin Wikyung turned toward the other two people.

“You were there too, Wipeng. Do you remember?”

Wipeng answered without even taking a breath.

“I don’t remember that, but I do remember him starting to womanize exactly ten years later. When I asked what he wanted to be when he grew up, he said he’d become the greatest ladies’ man under heaven.”

“A hero ought to know how to enjoy romance.”

“He doesn’t know squat about martial arts, so what good is knowing about romance? Is the hero you’re talking about a hero of the night, a hero to courtesans, or something?”

“Be quiet. Our youngest showed unusual promise from an early age.”

“So that promise… Ah, never mind. I should just stop talking.”

Glug, glug.

Jin Wikyung completely ignored Wipeng, who was pouring liquor straight from the bottle, and turned his attention to the next man in line.

“Mukyung. Now that you understand your little brother’s sincerity, let go of your anger.”

Jin Mukyung, who had been making a face like he’d swallowed something foul, finally spoke.

“Can’t I hit that bastard just once?”

“Now, now.”

“Just once. Please.”

At the icy voice, I quickly lowered my head.

“Please forgive this foolish little brother, Second Brother.”

“The bastard who’s been speaking casually to me this whole time is suddenly calling me ‘brother.’”

“Pardon? I am?”

“That’s enough. This is your final warning.”

“No. Hit me instead. If that would ease your anger, this little brother will gladly endure it.”

“You little shit!”

Jin Mukyung shot to his feet, then sank back down with a gasp. The bandages tied around his chest were turning red. It seemed his wound had reopened.

“Oh, no! Second Brother, are you all right?”

“This bastard, again… Guh!”

“Doctor! Doctor!”

The drinking party became a complete disaster in an instant.

Wipeng quietly picked up his second bottle and muttered,

“This family is really something…”

And how something it was—the foremost family in Shanxi.

* * *

The atmosphere finally settled down after the physician had come and gone.

I ignored Jin Mukyung’s murderous glare and took the Temporary Strength Pill from inside my robes.

“This is it.”

The pill was entirely red, as if blood had been condensed into a single sphere.

Jin Wikyung and Wipeng examined it closely.

“Wipeng, what do you think?”

“Just looking at it makes me smell blood. It’s a vicious object.”

“Could it really have been made by the Demonic Cult?”

“I couldn’t say. If it were, we should be able to sense demonic qi… but I can’t be certain.”

“Right? There’s something different about it.”

Both of them looked extremely serious. I was just as curious about where the Temporary Strength Pill had come from and who had made it, so I decided to give them a hint.

“They called it a Temporary Strength Pill.”

“A Temporary Strength Pill?”

“Yes. I heard it directly from Pung Yang.”

Jin Mukyung suddenly cut in.

“Pung Yang? When did you hear that?”

“While you were unconscious.”

“…Hoo. Hoo…”

I was the only eyewitness and witness, no matter what anyone said. As Jin Mukyung, who had gotten nowhere with his interruption, steadied his breathing to calm himself, the furrows between the other two men’s brows only deepened.

“A Temporary Strength Pill, Wipeng?”

“I’ve never heard of it either. If an object with this level of efficacy belonged to the Demonic Cult, it must have been used during the Great Faction War…”

“Could it not be the Demonic Cult?”

Their gazes turned toward me.

“Not the Demonic Cult?”

“What makes you think that?”

“I’m saying there’s no need to decide that from the start.”

In truth, I had said it out of hope that I might be able to take the pill back if it hadn’t been made by the Demonic Cult.

Of course, I had another thought as well.

*The Head Elder.*

The Mount Heng Sword Sect had certainly been the enemy that appeared on the surface during the last battle, but the true enemy had been the Head Elder himself.

Rather than making a simple either-or assumption, I believed we always had to keep open the possibility that there might be a third faction involved.

“Well, it just suddenly occurred to me.”

After hearing me out, the other two men’s expressions grew strange. Then, in the next moment, a very quiet voice escaped Wipeng’s lips.

It was a single word that slipped out unconsciously, like a groan.

“Dark Heaven…”

“Wipeng.”

Jin Wikyung’s sharp gaze cut off whatever he had been about to say.

“Ah, I apologize. I misspoke.”

Wipeng hurriedly tried to cover it up.

But it was already too late.

The two words *Dark Heaven* had been deeply etched into my mind.

*Dark Heaven? What is that?*

Then something unexpected happened.

> **System**
>
> You have obtained a small amount of information about **Dark Heaven**.
>
> The item description for the **Temporary Strength Pill** will be updated.

It was a completely sudden System notification. I held out my hand toward Wipeng, who was holding the Temporary Strength Pill.

“May I take a quick look?”

“Of course.”

*Item check.*

As soon as I muttered the words in my mind, information about the Temporary Strength Pill appeared.

Finding the changed information was easy.

> **System**
>
> **Item Window**
>
> **Temporary Strength Pill**
>
> **Type:** Elixir  
> **Grade:** ???  
> **Restriction:** Peak martial artist or higher  
> **Description:** A pill manufactured by **Dark Heaven**. For approximately one shichen, it dramatically raises the user’s latent power, but a price follows. Do not take it except in the worst circumstances.  
> **Effects:** Combat-related stats +100  
> Internal energy +15 years  
> Body-Protecting Qi available

The phrase *Someone Unknown* had disappeared, replaced by the unfamiliar term *Dark Heaven*.

*Judging by the context, it’s definitely some kind of organization…*

Well, anyone capable of making something like the Temporary Strength Pill was bound to be no better than the Demonic Cult. Same rotten lot, different name.

*Dark Heaven.*

Whoever came up with the name had incredible instincts. Two words were enough to tell everyone they were suspicious bastards.

*These guys definitely have something rotten going on behind the scenes. Ninety-nine percent sure.*

*Jin Wikyung and Wipeng seem to know something.*

The problem was that, judging by their reactions, they were extremely reluctant to reveal anything about Dark Heaven.

*Should I poke at them once?*

But before I could open my mouth, Jin Mukyung beat me to it.

“Dark Heaven? What is that?”

“Well…”

A troubled look crossed Jin Wikyung’s face.

“I’m sorry. I can’t tell you yet.”

Those words came from a man who cared deeply for his younger brothers.

If Jin Wikyung was unwilling to speak, there was no need to ask Wipeng.

“I apologize, Young Masters, but I cannot tell you until the matter becomes clearer.”

His attitude was firmer than anything I had seen from him before. Both Jin Mukyung and I realized that we had to withdraw for today.

But the more they tried to hide it, the more curious I became about Dark Heaven.

*So it’s a secret they have to keep hidden even from us.*

Even putting aside the fact that Mukyung and I were direct descendants of the family, we were core masters of the Jin Family of Taiyuan. If Wipeng was Jin Wikyung’s right arm, the two of us were each more than qualified to serve as his left arm or one of his legs.

*Then it must be a top-secret matter known only to those two, even within the family.*

I was only human, so I couldn’t help being curious. The fact that the System had reacted this time, despite remaining silent during the Mount Heng Sword Sect incident, also played a part.

*Dark Heaven. The Temporary Strength Pill. A top-secret matter known only to Jin Wikyung and Wipeng.*

Several keywords flashed through my mind.

All right. I’d made up my mind.

*I’ll ignore it and go on living.*

Excessive curiosity had a way of shortening one’s life. It had only been a few days since I’d gone to deliver the mail to the Mount Heng Sword Sect and nearly died.

A mysterious organization whose very name was ominous? If I got involved with them, it was obvious things wouldn’t end well.

“Well, let’s stop talking about this and have another drink.”

Jin Wikyung forced the mood back to normal.

Wipeng, who had already demolished two bottles by himself, was filling his glass, and so was the injured Mukyung. How could I be the only one to sit out? I accepted the liquor Jin Wikyung poured and downed it in one gulp.

Gulp, gulp.

The notorious fire liquor burned its way down my throat with a fierce heat.

“Guhhh.”

Wow. This was no joke.

I knew it was strong, but drinking it myself, it was far more potent than I’d expected. At this strength, soju and beer couldn’t even hold a candle to it.

Unlike me, who shuddered from head to toe, the other three immediately filled their empty glasses to the brim.

“Drink!”

“Down it!”

“Let’s keep going until we drop!”

“….”

I didn’t learn that Shanxi Province belonged to North China, or that every man from North China was an incredible drinker, until after we spent the entire night drinking.

* * *

The next day at noon, Hyuk Mujin stared at me as if I were a monster when I mounted my horse in a perfectly refreshed mood.

“Is your stomach all right?”

“Yeah. Why wouldn’t it be?”

“Don’t tell me you were the only one who didn’t drink yesterday. Or did you fall asleep halfway through?”

“No. The four of us kept drinking.”

“…All of it?”

His mouth fell open.

“Is that even possible? Are you human?”

“It all fit.”

“My goodness. How many bottles did you drink through the night?”

He had the wrong unit.

It wasn’t bottles. It was barrels.

We kept emptying massive casks of liquor—the kind I’d only ever seen in pirate movies—and then emptying more.

“I think it was close to twenty barrels. I stopped counting after ten, so I’m not sure.”

“Wow. That’s incredible.”

Hyuk Mujin raised his thumb in admiration when the inn door suddenly opened.

And three zombies—or rather, three Peak masters—appeared.

“Uuugh.”

“Urk.”

“Huff, huff.”

Their faces were pale, their lips parched, and their eyes sunken.

Without a single exception, they dragged their feet and climbed straight into the carriage. The martial artists of the escort force stared at them with their eyes wide.

“Why are they suddenly getting into the carriage…?”

“They look really unwell.”

“That can’t be. Haven’t you ever drunk with our Commander? Wipeng, the God of Drinking? You don’t know?”

“Wasn’t the Commander’s epithet Ghost Sword?”

“Whatever else you might say, when it comes to drinking, he could probably beat even the Martial God. They’re probably just like this because all the fatigue they’ve accumulated finally caught up with them.”

As the martial artists whispered among themselves, the carriage door suddenly flew open, and one person hurriedly dashed out and bent over.

“Urrp, buuurrgh!”

Splaaarsh.

After pouring out a pale liquid for quite some time, Wipeng staggered back into the carriage. One of the martial artists who had been talking animatedly muttered in a dazed voice,

“…This can’t be.”

“It absolutely can. Anyone can see that’s a hangover. They drank all night without sleeping. Of course they’d end up like that.”

“Then why is the Third Young Master so perfectly fine?”

The escort force’s gazes all turned toward me.

The smell of liquor radiating from my entire body was strong enough to send chills down the spine. But in complete contrast, my face looked unbelievably refreshed, and my breathing was calm.

“No way…”

“The Third Young Master beat the Commander? That God of Drinking?”

The courtyard buzzed with excitement.

Hyuk Mujin’s look of admiration had gone beyond admiration and become outright reverence.

“Ah, I knew it! That’s our Captain—the man who used to drink with courtesans every damn day!”

“….”

“I remember what the Chief Steward said. If Captain had kept drinking for three more years, he would have uprooted the family’s entire foundation. So this is why you always had to steal from the family coffers!”

“…Hey, you punk.”

It wasn’t as if we were alone. If he talked like that, what would happen to my image?

As if the stares pouring in from every direction hadn’t already made my face feel hot enough.

“Ahem. Ahem!”

I cleared my throat and glanced around. And what do you know? The eyes of all those rough-looking men were sparkling brighter than stars in the night sky.

“A true God of Drinking. He really is.”

“He’s famous in Taiyuan’s red-light district. Haven’t you heard of the Night King?”

“The Night King? I can tell just from the epithet. So he was already renowned for his drinking.”

“No, not that… The other thing. That.”

“Gasp. Is it true?”

“How would I know? I’ve never seen it.”

“Turns out he really is a man among men.”

> **System**
>
> Everyone gathered here is impressed by your drinking capacity and imposing presence!
>
> **Fame** rises by 20!
>
> **Fame** rises by 22!
>
> **Fame** rises by 25!
>
> If a particular rumor spreads, you may obtain a related **Title**.

“….”

What the fuck was with my Fame shooting up like that?

And what did it mean, a related Title? No, it was fine. Put that away. Please, just let me be satisfied with the Sleeping Dragon of Shanxi.

*Stop it, you lunatics…*

With a mysterious sense of shame, I turned my head—and came face-to-face with Hyuk Mujin, who was staring intently at a certain part of me.

“…What are you doing?”

“Oh, I was just taking a rough measurement with my eyes.”

His answer was so straightforward that I was almost thrown off. Hyuk Mujin cheerfully extended his forearm.

“Wow. As expected, you’re amazing. Hehe.”

In return for the forearm, I offered him my fist.

Thwack!
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 127`.

# Master Edit Task — Chapter 135

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
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 산서오문   | **Five Gates of Shanxi**         |
| 일류     | **First Rate**    |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 표국     | **Escort Bureau**                            |
| 소국주    | **Young Bureau Head**                        |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 형장      | **Brother** / **Brother [Name]**                                |
| 공자      | **Young Master**                                                |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 130–134

## Plot

Cheongpung, an eccentric young Peak master who recently fled Huashan’s Lotus Peak, travels toward Taiyuan after briefly joining a Seongun Escort Bureau escort run. At Honghwa Inn, he meets Jin Taekyung and Hyuk Mujin and begs for candied hawthorn skewers because he has not eaten all day. Taekyung feeds him, learning that Cheongpung was raised in the mountains by his grandfather and came down to test himself against the Ten Dragons and Phoenixes. Taekyung cannot identify Cheongpung’s Level through Qi Sense; his System Window displays `???`.

Five First Rate heirs of the current Five Gates of Shanxi mock Cheongpung, Taekyung, and Mujin from the inn’s second floor, then refuse to apologize. Their spokesman, Woo Jintae, heir to the Seongun Escort Bureau, is publicly slapped and humiliated by Taekyung, who fabricates the identity Tien Shinhan of the Dodong Sect when challenged about his affiliation. The other heirs—Seongryong, Cheonwoo, Myeonghwa, and Sohye—refuse to fight Taekyung. Mujin warns them that they will be next, secures their apology to Cheongpung, and orders them to prostrate themselves.

Woo Jintae had been using the Seongun Escort Bureau’s wealth, gifts, and hospitality to control the current Five Gates scions before their scheduled luncheon with Shanxi’s ten-year-old Prince City Lord. The luncheon, already locked in as The City Lord’s Invitation Quest, is due to take place the following day.

## Continuity

- Cheongpung is an exceptionally young Peak master with an undetectable Level, an innocent and eccentric personality, and a strong appetite. He was raised by his grandfather in the mountains from age five, and his grandfather repeatedly relocates because people keep finding him.
- Cheongpung recently left Huashan’s Lotus Peak and descended from the mountains to determine whether he or the Ten Dragons and Phoenixes are stronger. His status at Huashan, his grandfather’s identity, and his precise affiliation remain unresolved.
- Hyuk Mujin has returned to Taiyuan after five years. His parents are healthy textile merchants who own the city’s largest textile shop, with branches in Henan and Hebei.
- Woo Jintae is the married, nearly thirty-year-old heir and sole male heir in three generations of the Seongun Escort Bureau. He cultivated the current Five Gates scions through lavish hospitality, gifts, and bribes.
- The current Five Gates of Shanxi are an alliance of more than twenty small and medium-sized sects formed after the former Five Gates—including the Samdo Sect and Gunggui Sect—were annihilated at the Battle of Eight Spring Gorge for serving the Head Elder.
- The five scions are Seongryong, Cheonwoo, Myeonghwa, Sohye, and Woo Jintae. They are pampered First Rate martial artists; Jintae is Level 45 and served as spokesman.
- Taekyung has publicly humiliated Jintae and claimed the fabricated identity Tien Shinhan of the Dodong Sect. The other four scions apologized to Cheongpung and were ordered by Mujin to plant their heads on the floor; whether they obey and what consequences follow remain unresolved.
- The City Lord’s Invitation Quest requires Taekyung’s attendance at the next day’s luncheon with young prodigies. The City Lord is a ten-year-old Zhu Prince and the Emperor’s youngest brother; Woo Jintae and the Five Gates scions are also expected to attend.
- Taekyung still intends to reject Lee Seowol’s marriage proposal because he loves Song Song. The Mount Heng Sword Sect’s reconstruction, the Temporary Strength Pill and Dark Heaven, Pung Yang’s wider consequences, and the Fire King’s status remain unresolved.

## Translation Decisions

- Render 성운표국 as **Seongun Escort Bureau**, 표행 as **escort run**, 쟁자수 as **porter**, 표두 as **Escort Chief**, 은원보 as **silver ingot**, 은자 as **nyang of silver**, 사서삼경 as **the Four Books and Three Classics**, and 연화봉 as **Lotus Peak**.
- Render 빙당호로 as **candied hawthorn skewers**, with an explanatory footnote.
- Render 개방 as **Beggars’ Sect**, 삼도문 as **Samdo Sect**, 궁귀문 as **Gunggui Sect**, 산서오문 as **Five Gates of Shanxi**, and 십봉룡 as **Ten Dragons and Phoenixes**.
- Render 우진태 as **Woo Jintae**, 우 소협 as **Young Hero Woo**, 황 소저 as **Young Lady Hwang**, and 혁 아우 as **Little Brother Hyuk**.
- Render 도동파 as **Dodong Sect** and 천진반 as **Tien Shinhan**, preserving Taekyung’s fabricated identity joke.
- Render 대가리 박으십쇼 as **“bend over and plant your heads on the floor,”** retaining Mujin’s blunt comic coercion.
- Render 촉금 as **Shu brocade**, and retain **First Rate**, **Peak**, **City Lord**, **Prince**, and **The City Lord’s Invitation**.

### Prior accepted reading-copy tails

#### Chapter 133 tail (verified mastered)

…
their legends—the future of the Murim’s orthodox faction. They were the objects of every rising martial artist’s admiration, and those gathered here were no exception. “Who are they? Martial artists?” The person seated closest to the railing craned his neck and looked down at the first floor. “There are three of them. One’s a young master, another looks somewhat like a martial artist… and the last looks like a beggar.” “What kind of combination is that?” “Shh. Let’s keep listening.” At Woo Jintae’s urging, everyone fell silent and pricked up their ears again. They had all trained in martial arts as befitted scions of martial families, so overhearing the conversation was not difficult. “Please continue.” “It’s nothing important. I just had a childish thought for a moment.” There was a brief silence. Then another statement followed. “Who would be stronger, me or them? I wanted to find the answer to that question.” The young prodigies of the Five Gates of Shanxi looked at one another. “Did you all hear that?” “Yes. Who said it?” “That beggar I mentioned. You really do see all kinds of lunatics these days.” Woo Jintae shook his head. “He’s probably a martial artist, not a beggar.” “A martial artist…?” “If he’s talking about the Ten Dragons and Phoenixes, that must be it. As for how he ended up looking like a beggar, well, I can guess without even seeing him.” A mocking laugh escaped Woo Jintae’s lips. “Isn’t it obvious? He’s the type who picks up a few Third Rate martial arts moves by chance, puts his faith in them, wanders aimlessly through the martial world, and winds up dead.” “Ah, now that you mention it, you’re right. As expected of Young Hero Woo.” “The more I think about it, the funnier it gets. How did someone like that dare mention the Ten Dragons and Phoenixes?” The young prodigies snickered at one another, and their laughter gradually grew louder. “That tells you all you need to know about the people who associate with a lunatic like him. Or maybe they’ll slap him across the face, call him crazy, and walk out.” “What are the young master and the martial artist sitting with him doing?” The young prodigy who glanced downstairs again answered while stifling his laughter. “I don’t know about the martial artist, but the young master is nodding to himself.” “Well, now.” “Really?” “Wow, you should all see his expression. He genuinely seems to believe that beggar.” The young prodigies rose and approached the railing. Woo Jintae, unable to contain his curiosity, went with them. *Let’s at least see what these fools look like.* The moment he saw the young master nodding with a serious expression, a loud laugh burst from his mouth. “Puhahaha!” At the same time, the other young prodigies began laughing loudly as well. “Pfft, ha-ha-ha! I almost died trying to hold that in.” “Ha-ha-ha! They don’t know the first thing about martial arts, yet they’re talking about the Ten Dragons and Phoenixes?” How long did they laugh? When they finally managed to stop, what they saw was one person staring quietly up at them. “Finished laughing?” At the ‘young master’s’ words, the young prodigies froze. They had all been raised precious and pampered. How long had it been since anyone had spoken down to them like that? Woo Jintae’s dry voice broke the sudden, icy silence. “And if we have?” The ‘young master’ smiled brightly. “Get down here right now, you fucking sons of bitches. My neck hurts.” * * * Hyuk Mujin asked with an expectant look in his eyes, “Are you going to fight them?” “Depends on what they do.” “Once you’ve called them fucking sons of bitches, isn’t that asking for a fight?” “That works, too. See all the spit those bastards sprayed on my face?” “You’re completely drenched.” Hyuk Mujin briskly wiped my face with his sleeve. “What if they don’t apologize?” “They’d better.” “Look at their faces. They’re never going to apologize.” “Then they’ll get the shit beaten out of them.” “There are women among them, too…” “I believe in gender equality.” “What?” “I beat everyone equally.” Cheongpung, who had been watching blankly, looked at me with sparkling eyes. “Oh. I don’t really understand, but it sounds cool.” “It’s nothing special… Anyway, thanks.” I might have said more, but there was no time. The five bastards—or rather, the five sons and daughters of bitches—had jumped down from the second floor. *Tap.* They landed lightly, as befitted First Rate masters. One of them stepped out from the group as they glared at us. Level 45. Tall and good-looking. The same bastard who had laughed first. “I am—” “You the head?” “The head?” “Are you the boss of these five?” He let out a short laugh. “You’d better watch your mouth. If you knew who the people here were, including me…” I smiled back and scanned through their Level windows. “Seongryong, Cheonwoo, Myeonghwa, Sohye, and finally, you—Jintae. Want me to tell you your family names, too?” “…!” “…!” Five pairs of astonished eyes turned toward me. No, seven, counting Hyuk Mujin and Cheongpung. “Oh, and this is a personal request, but please don’t ask how I knew. I’m sick of that line. If you ask, I’ll hit you.” “How did you…?” “Did you stuff radishes in your ears?” The next moment, my palm met his cheek. *Smack!*

#### Chapter 134 tail (verified mastered)

…
Jintae cast aside his pride and everything else, the young prodigies of the Five Gates of Shanxi couldn’t bring themselves to draw their weapons. “How are we supposed to beat that…?” The words slipped from someone like a groan, speaking for them all. They were right. There was no need to experience it firsthand. Just watching from the side was enough to make their knees go weak and their legs give out. Their opponent was roughly the same age as them, but there was no question that he was a master far beyond their imagination. “To reach that realm at his age…” “That thing’s a complete monster.” *Smack-smack!* “P-please spare my life!” Woo Jintae’s voice grew even more desperate. Even his plea for help had subtly changed. If this continued much longer, he might start begging to be killed instead. “W-we should help him, right?” “At the very least, we should try to stop him… Young Master Wang, do something.” “Me? Why me all of a sudden?” “Why do you think? Every time we got together, you bragged about your family’s martial arts. You said it was sword arts you could display anywhere in the Central Plains without shame.” The heir of the Wang Family Estate, who never missed an opportunity to boast about the greatness of his family’s martial arts, answered with a solemn expression. “I’m a saber user. I never learned sword arts.” “What?” “And why are you trying to dump this on me? If Young Lady Shin wants to stop him so badly, she can step in herself.” “My goodness. What a spectacle.” As the young prodigies of the Five Gates passed the responsibility around, Hyuk Mujin, who had been quietly watching the situation, suddenly cut in. “You’re all worrying over nothing. If it were me, I’d hurry over and lend a hand, at least.” “You—no, sir. Who are you?” With such a terrifying scene unfolding before them, they had to speak with even an ordinary martial artist using half-polite language. Young Lady Hwang, who had received Shu brocade as a gift from Woo Jintae only a quarter of an hour earlier, quickly stepped forward. “Let me make this clear in advance. We have no ill feelings toward you people. You know that, right?” “Do you? If that’s how it is, then fine. Let’s say that’s how it is.” “I’m not saying we should just say that. I’m saying it’s the truth.” “What good will telling me do?” Hyuk Mujin grinned and jerked his chin toward Jin Taekyung’s back, where he was enthusiastically beating Woo Jintae. “Our Captain has quite a temper. Once the gentleman getting beaten over there collapses, who do you think will be next? You, Young Master? Or the Young Lady beside you?” “…” “Oh, and just in case you’re wondering, that man hits men and women alike.” “I-I didn’t laugh!” “Neither did I!” “Do I have to say the same thing twice? Telling me won’t do you any good. Though, there is one way that might work.” “A way?” The young prodigies’ ears perked up. They hadn’t trained in martial arts for nothing. They understood that they had no chance against that monstrous young man. “S-somebody save me…” Woo Jintae’s dying voice happened to drift into their ears, fanning their survival instincts even further. “W-what exactly is this way?” Hyuk Mujin stroked his chin with a deliberately serious expression. “Well, you’re all scions of influential families, so I don’t know whether you can bring yourselves to do it.” “I will!” “I’ll do it! I’ll definitely do it!” “Good. At least you’ve got the right attitude.” Hyuk Mujin nodded in satisfaction and pointed at Cheongpung, who was watching the one-sided beating with his mouth hanging open. “First, apologize politely to this gentleman.” Before he had even finished speaking, the young men and women of the Five Gates bent deeply at the waist. “We sincerely apologize.” “We’re truly sorry for judging you rashly based on your appearance.” Cheongpung scratched the back of his head. “I’m fine, so everyone, please stand up.” Considering how they had mocked him in front of so many people, Cheongpung forgave them so readily that even Hyuk Mujin was taken aback. Even his face, which should rightfully have been flushed with anger, was sunny and bright. “You’re saying that so easily?” “Yes. Is there a problem?” “It’s not that, but… Weren’t you angry earlier? You were insulted so publicly.” “Why would I be angry? I just found it fascinating.” “What? What do you mean?” “That was the first time so many people had paid attention to me. It was also the first time someone who looked down on me apologized afterward. I found it fascinating and fun.” “…” “Ah. I think coming down from the mountain was a good decision.” *This guy’s a little nuts, too.* Hyuk Mujin looked at Cheongpung as though he were some strange creature, then shook his head and turned to the young prodigies. “You heard him, right? Since the Young Hero here has accepted your apology, we’ll consider the matter settled.” “Oh!” “We’re saved!” But Hyuk Mujin wasn’t finished. “All right, then. There’s one final thing left—the second.” “…The second?” “There’s more?” “Yes. This is the most important one.” Then he solemnly declared to the four men and women looking at him, “All of you, get down and plant your heads on the floor.” “…!” “…!”

## Korean source

```text
＃135화



쫙!

“도, 도와주시오!”

“너 도와줄 사람 없다.”

쫙쫙!

“사, 살려 주시오!”

“싫어, 안 돼. 돌아가.”

쫙쫙쫙!

“차, 차라리 죽여…….”

“아냐, 너 아직 괜찮아. 주둥이에서 말이 나오고 있잖아.”

쫙쫙쫙쫙!

“흐윽, 흐그으윽.”

“그래, 바로 이 반응이지.”

나는 그제야 비로소 손을 멈췄다.

그럭저럭 봐줄 만했던 귀공자의 얼굴은 찐빵처럼 부풀었고, 양 뺨에는 발그레한 홍조 대신 검푸른 멍이 새겨져 있었다.

“우리 진태. 잘못했어, 안 했어.”

“흐그윽.”

엉망이 된 몰골로 흐느끼는 녀석을 보니 문득 안쓰럽다는 생각이 들었다.

그래, 얘도 남의 집 귀한 아들인데…….

“잘못했지?”

“흐극, 흐그그극!”

“그러니까 왜 사람 말을 무시해. 사과하라고 했을 때 바로 사과했으면 얼마나 좋아. 안 그래?”

“흐으으.”

“앞으로 착하게 살자. 알겠지?”

“흐그극.”

나는 맹렬하게 고개를 끄덕이는 우진태를 가만히 바라보다가 입을 열었다.

“그런데 너…….”

“흐으?”

“아까부터 대답이 왜 그따위야? 사람 말 못 해?”

순간 녀석의 흐느낌이 뚝 멎었다.

“죄, 죄송합니다.”

“할 수 있네? 할 수 있는데 안 한 거네? 왜 운 거야? 내가 이 정도로 아프고 힘들다. 뭐 그런 거 티 내는 거야?”

“아닙니다!”

“이젠 목소리도 커지네? 성량 좋다, 너. 복식 호흡 연습해? 내 고막을 터트려서 이 위기를 모면해 보겠다, 이거야?”

“아닙니다. 정말 아닙니다. 제발 이제 그만해 주십시오, 흐흐흑…….”

“어? 또 우네? 지금 울음이 나와? 네가 뭐 잘했다고 울어. 울면 인생이 끝나? 그리고 그만해 달라니. 누가 보면 내가 가해자인 줄 알겠다?”

“죄송합니다. 안 울겠습니다.”

“와, 바로 울음 그치는 것 봐. 소름 돋는 놈이네, 이거. 내가 너였으면 죄 없는 사람 건드렸다는 죄책감에 울다 지쳐서 실신했을 텐데. 너 정말 미안하긴 해?”

“자, 잠시만. 잠시만 제 얘기를 들어 주시면…….”

“듣긴 뭘 들어. 네가 말할 자격이나 있어? 여기가 무슨 연예 대상 시상식이야? 너 말하는 동안 나는 잠자코 기다리다가 훈훈하게 웃으면서 박수 쳐 주면 돼?”

“…….”

“이제는 대답도 안 하네. 넌 밥 안 먹어도 배부르겠다. 그치? 지금처럼 남의 말 아작아작 씹어 먹으면 기분 좋…….”

말을 이어 가려던 그 순간, 우진태가 번개 같은 속도로 자신의 뒤통수를 바닥에 내리찍었다.

쿵! 털썩.

안타깝다. 최소한 한 시진은 더 갈굴 수 있었는데.

혼절한 우진태를 두고 돌아서는 나에게 수많은 시선이 우수수 날아와 꽂힌다.

“성운표국의 소국주가 저렇게 간단하게…….”

“저 젊은 놈, 도대체 정체가 뭐야?”

“손속도 손속이지만, 혓바닥이 독사가 따로 없구먼.”

놀람과 두려움이 섞인 웅성거림이 일파만파 퍼져 나갔다.

1층에 자리한 손님만 자그마치 백여 명. 내 얼굴을 알아보는 이들이 나타난 것도 사실 결코 놀라운 일은 아니었다.

“사, 산서잠룡이다!”

“뭐? 태원진가의?”

“그럼 산서잠룡이 둘이겠나! 어쩐지 아까부터 눈에 익더라니.”

산서잠룡의 명성이 아주 하늘을 떨어 울리는구나.

내가 흐뭇한 미소와 함께 사람들에게 손을 흔들어 주려던 그때였다.

“확실한가? 산서잠룡이라면 작년 이맘때쯤에 홍화루에서 한 번 본 적이 있는데, 내가 기억하는 모습과는 좀…….”

“이 사람아, 그때 우리 둘이 같이 있었던 건 기억 안 나나?”

“어, 그랬던가?”

“그래, 체격이나 분위기가 많이 달라져서 그렇지, 산서잠룡이 확실하네. 태원진가의 자제라는 놈이 가문에 기녀를 데려가겠다고 온갖 진상을 부리던 모습이 아직도 눈앞에 선해.”

“…….”

젠장. 별걸 다 기억하네.

내가 머쓱한 얼굴로 손을 내리자 자기들끼리 수군거리던 손님 중 몇 명이 손을 번쩍 치켜들었다.

“그때 나도 있었소!”

“형장도?”

“똑똑히 기억하오. 저놈, 아니 저분이 계단에서 넘어지면서 내 아래 물건을 쭉 잡아당겼…… 후우, 그때만 생각하면 지금도 아찔하구려.”

“허어어, 망측한지고. 지금은 괜찮소?”

“다행히도 멀쩡하오. 뿐만 아니라 그 후로 살짝 길어진 느낌이오.”

“…….”

그게 가능해?

나는 방금 입을 연 사람에게 얼마나 커졌는지 물어보고 싶은 마음을 간신히 억눌렀다. 산서오문인지 나발인지 하는 찌꺼기들의 처리가 아직 남아 있었기 때문이다.

그런데…….

“어라?”

내 시선에 들어온 것은 나란히 대가리를 박고 있는 네 명의 후기지수와 어쩐지 목이 빳빳하게 선 혁무진이었다.

“준비 끝났습니다.”

“네가 이러라고 시킨 거냐?”

“서당 개 삼 년이면 풍월을 읊는다 했습니다. 이제 척 하면 착 아닙니까?”

“너 이 녀석……!”

나는 형용할 수 없는 감정에 사로잡혔다.

처음에는 멍청한 놈인 줄 알았는데, 갈수록 똑똑해지는 것 같다.

나 대신 지력 스탯을 찍는 게 아닌지 의심될 정도다.

“성장했구나. 매우 칭찬한다.”

“과찬의 말씀이십니다. 그보다 이들은 어찌할까요?”

“검갑 줘 봐.”

“존명.”

대하 사극의 한 장면이 따로 없다. 나는 혁무진이 내민 검갑을 받아 들고 손바닥을 내리쳤다. 그립감 좋고, 타격감도 좋다.

“다들 기상.”

말이 떨어지기가 무섭게 후기지수 네 사람이 벌떡 일어났다.

두려움 가득한 시선을 무시하며 다시 레벨창을 쭉 훑어보니 역시나 이제 간신히 일류가 될까 말까 한 녀석들이다.

“뭘 잘못했는지는 이미 알 테고…… 너희가 산서오문의 후계자들이라고?”

“예, 옛!”

“셋째 아들, 막내딸. 뭐 그런 거 아냐?”

“아닙니다!”

“확실해?”

“예, 그렇습니다!”

기합이 제대로 들어간 목소리가 객잔 내부를 쩌렁쩌렁하게 울린다. 나는 검갑을 탁탁 두드리며 중얼거렸다.

“그래? 그럼 산서오문도 별거 아니네?”

“…….”

“…….”

하나같이 수치심으로 얼굴이 붉게 달아올랐지만 아무 말도 하지 못한다.

이제는 놈들도 내 신분을 아니까.

당장 나와의 무력 차이는 둘째치고서라도, 산서오문 정도로는 태원진가의 이름 앞에서 고개를 빳빳하게 들 수 없다.

“그동안 세월 좋았다. 그치?”

“……아닙니다.”

“아니긴 뭐가 아니야. 돈 걱정 없고, 뒷배 든든하고. 그거 믿고 지금까지 짱짱하게 잘나갔을 거 아냐. 응? 여기저기 시비도 걸고 다니고.”

“…….”

“그런데 태원진가랑 항산검문 사이에 전쟁이 일어났네? 평소에 잘해 준 건 태원진가인데, 항산검문이 이기면 돌아올 보복이 무서워서 눈치 살살 보다가 여기까지 왔고. 맞지?”

“그, 그게 저희는 잘…….”

“너희 후계자라면서? 각자 소문주, 소가주. 뭐 그런 거 아니냐? 아, 저기 저놈은 소국주였지.”

엉겁결에 내가 가리키는 방향을 바라본 네 사람이 몸을 부르르 떨었다.

모진 따귀 세례와 트래쉬 토크를 견디지 못하고 스스로 기절을 택한 우진태가 죽은 것처럼 바닥에 누워 있었다.

“아무튼, 상황이 이러면 적당히 쭈그려 있지 뭐 잘났다고 여기까지 와서 기고만장하게 굴어. 태원진가가 우스워? 내가 이마에 산서잠룡이라고 문신 새기고 다녀야 해?”

“죄, 죄송합니다.”

“죄송하면 다 끝나? 내가 너희 죽사발 낸 다음에 사과해 줘?”

“히익!”

저 공포에 찬 눈빛들을 보라. 걸어 다니는 재앙이 된 기분이다.

더 이상 말이 필요 없는 상황. 나는 검갑을 들어 올렸다.

“역사적으로도 이게 약이었다. 다들 엎드려뻗쳐.”

그리고 오들오들 떨면서 엎드린 네 명의 후기지수에게 스산한 목소리로 물었다.

“몇 대 맞아야 반성할래? 각자 말해 봐.”

“예, 예?”

“말해 보라고. 우진태 저놈은 너무 나대서 저렇게 팬 거지, 너희는 자진 납세 했으니까 정상참작 해 준다.”

무거운 침묵이 흘렀다. 빠르게 시선을 교환한 네 사람이 한입으로 외쳤다.

“하, 한 대만 맞겠습니다!”

“한 대? 그걸로 되겠어?”

“옛!”

“한 대 맞으면 다시는 이런 일 없게 할 거야?”

“천지신명께 맹세하겠습니다!”

나는 검갑을 단단히 말아 쥐었다.

“좋아. 그럼 각자 열 대씩.”

“……!”

“……!”

“방금 천지신명한테 물어봤는데, 너희는 한 대로 어림도 없대. 그러니까 열 대.”

내가 살면서 이런 상황을 겪게 될 줄이야. 학창 시절, 틈만 나면 빠따를 휘두르던 체대 입시 선생이 된 기분이다.

나는 묘한 향수에 젖은 채 빠따, 아니 검갑을 휘둘렀다.

빡! 빡! 빡! 딱!

“크헉!”

“움직이지 마. 뼈 다친다. 자, 다시.”

빡! 빡! 빡!

홍화 객잔을 가득 메운 사람들에게는 진귀한 광경일 것이다. 산서오문의 후계자라는 자들이 굼벵이처럼 바닥을 기어 다니고 있었으니까. 심지어 그중에는 여자도 둘이나 끼어 있었다.

우리를 빙 둘러싼 사람들이 수군거리는 소리가 귓가를 파고들었다.

“저거, 저래도 되는 거여?”

“그러게 말이여. 아무리 그래도 산서오문인데…… 이러다가 또 무림의 은원이니 뭐니 하면서 큰 싸움 일어나는 거 아닌가 모르겄네.”

“거, 답답하기는. 요즘 상황을 몰라도 너무 모르는 거 아니오? 항산검문이 건재했다면 모를까, 지금 태원진가를 막으려면 산서 땅에 있는 중소 문파가 죄다 뭉쳐도 될까 말까요.”

“그 정도여?”

“다 끌어모으면 머릿수야 앞설지 몰라도 수준이 다르지. 저기 산서잠룡만 봐도 알 수 있는 사실 아니오?”

“그렇긴 하네. 산서오문의 후계자니, 후기지수니 뭐니 하면서 거들먹거리더니 산서잠룡한테는 쥐뿔도 안 되는 거 보면.”

“따지고 보면 먼저 시비 건 것도 저쪽 아니오?”

“그것도 맞는 말이지.”

“그리고 기왕 말이 나왔으니 말인데, 지금 산서오문이라고 하고 다니는 것들 보면 죄다 냄새가 구려.”

“구리다니?”

“말이 정파지 알게 모르게 양민 등골이나 빨아먹는다, 이 말이오. 당장 성운표국만 봐도 상인들 사이에서 얼마나 말이 많은데?”

“그 소문들이 사실이었나?”

“반면에 태원진가는 어떻소? 십 년 전에 기근(飢饉)이 들었을 때는 구휼미도 풀고, 그보다 훨씬 전에는 마교 놈들도 막아 냈지. 그놈들은 우리 같은 양민들도 죽이고 다니는 흉악한 살귀(殺鬼)들이니 만약 태원진가가 아니었다면…… 으, 생각하기도 싫소.”

“맞다, 이번에 고원에서 넘어온 마적들을 쫓아 보낸 것도 태원진가라고 들었는데.”

“그 소문 아직 못 들은 사람도 있소? 진천검과 산서잠룡이 싹 다 몰살을 시켜 버렸다고 합디다.”

“허어어.”

“그러니 만에 하나 다시 전쟁이 일어난들 문제 될 것이 무에 있겠소? 내 맹세컨대, 산서오문이 이 문제를 걸고넘어지면 당장 태원진가에 입문(入門)하여 싸우겠소!”

“오오!”

“아직 젊은 친구가 협기(俠氣)가 대단하군. 내 듣고 보니 자네 말이 맞는 것 같네. 여기 내 술 한 잔 받게!”

빡! 빡! 빡!

후기지수 넷 중 세 명을 굼벵이로 만든 나는 말소리가 들려오는 쪽으로 고개를 돌렸다.

얼마나 힘써서 태원진가를 변호해 주는지, 이야기를 듣다 보니 내가 술을 사 주고 싶어질 정도다.

‘마인드만 보면 이미 우리 태원진가 사람인데?’

레벨만 좀 받쳐 준다면 영입 1순위다. 나는 흐뭇하게 웃으며 저 위대한 웅변가의 레벨창을 확인했다.



[Lv.15 장칠득]



“……뭐여, 시벌.”

장칠득? 내가 아는 그 장칠득?

다시 잘 보니 분명 아는 얼굴이다. 진무경에게 일대일 집중 수련을 받던 시절, 우리한테 꼬박꼬박 식사를 가져다주던 하인.

바로 그 장칠득이 위대한 웅변가의 정체였다.

‘와 씨, 소름.’

어쩐지 너무 태원진가 편만 들더라.

물론 틀린 말은 없었지만 이런 식으로 여론 조작을 하다니.

뭔가 정치계의 엄청난 음모를 발견한 것 같은 기분에 몸이 부르르 떨리던 그때였다.

“저기…….”

잠시 잊고 있던 한 사람, 청풍이 맑은 눈으로 입을 열었다.

“아직 한 분 남았는데요.”

“헉.”

엎드려 있던 마지막 한 놈이 움찔했다. 청풍 이놈도 은근히 순진한 것 같으면서 무서운 놈이다.

어차피 마지막이라고 봐줄 생각 따위는 없었지만.

“안 그래도 지금 때리려고요.”

검갑을 휘두르려던 그때, 청풍이 재차 입을 열었다.

“저기. 어려운 부탁 하나만 말씀드려도 되겠습니까?”

“빙당호로 이제 없어요.”

“그게 아니고, 저어.”

머뭇거리던 청풍이 조용히 검갑을 가리켰다.

“마지막 분은 제가 한번 때려 보고 싶어서요.”

“예?”

“제가 아직 이런 걸 한 번도 안 해 봐서…….”

“…….”

살면서 별의별 또라이를 다 봤지만, 첫 경험 빌런은 처음이다.
```

## Current accepted English baseline

```markdown
# Chapter 135

*Smack!*

“P-please, help me!”

“No one’s coming to help you.”

*Smack-smack!*

“P-please, spare me!”

“No. Not happening. Go back.”

*Smack-smack-smack!*

“Th-then just kill me…”

“No, you’re still fine. Words are still coming out of your mouth.”

*Smack-smack-smack-smack!*

“Hhk… Hhrrgh…”

“Yes. That’s the reaction I was looking for.”

Only then did I finally stop my hand.

The young master’s face, which had been reasonably presentable until now, had puffed up like a steamed bun. Instead of a healthy flush, both cheeks were covered in dark blue bruises.

“Our Jintae. Did you do something wrong or not?”

“Hhrrgh.”

Seeing him sob with his face in such a mess, I suddenly felt a little sorry for him.

*Right. He’s someone else’s precious son, too…*

“You did something wrong, didn’t you?”

“Hhk! Hhrrgh!”

“Then why did you ignore what I was saying? You should’ve apologized the moment I told you to. Wouldn’t that have been better? Don’t you think?”

“Hhrrr.”

“Let’s live properly from now on. Understand?”

“Hhrrgh.”

I quietly watched Woo Jintae nod furiously before opening my mouth.

“But you…”

“Hh?”

“Why have you been answering like that this whole time? Can’t you speak like a normal person?”

His sobbing stopped dead.

“I-I’m sorry.”

“You could do it? You could speak, but you chose not to? Why were you crying? Were you trying to show everyone how much pain and hardship you were in?”

“No!”

“Your voice is getting louder, too. You’ve got some volume. Have you been practicing diaphragmatic breathing? Were you planning to blow out my eardrums and escape this crisis?”

“No. Absolutely not. Please, stop now. Hh-hhng…”

“Oh? You’re crying again? You can still cry? What have you done to deserve tears? Is your life over because you’re crying? And ‘please stop’? Anyone watching would think I was the one attacking you.”

“I’m sorry. I won’t cry.”

“Wow, look at him stop crying right away. You’re a creepy one, aren’t you? If I were you, I’d feel so guilty for picking on an innocent person that I’d cry until I passed out from exhaustion. Are you really sorry?”

“P-please, just listen to me for a moment…”

“Listen to what? Do you even have the right to speak? Is this some kind of entertainment awards ceremony? Am I supposed to sit quietly while you talk, then smile warmly and applaud when you’re finished?”

“…”

“Now you’re not even answering. You must feel full even without eating. Right? If you keep crunching through other people’s words like that, it must feel good…”

Just as I was about to continue, Woo Jintae slammed the back of his head into the floor with lightning speed.

*Thud! Plop.*

What a shame. I could have kept chewing him out for at least another shichen.[^1]

[^1]: A shichen is a traditional time unit equal to approximately two hours.

As I turned away from the unconscious Woo Jintae, countless gazes came flying toward me and stuck fast.

“The Young Bureau Head of the Seongun Escort Bureau went down that easily…”

“Who the hell is that young man?”

“His hands are vicious enough, but his tongue is a venomous snake all on its own.”

A murmur mixed with shock and fear spread through the room like a wave.

There were more than a hundred guests on the first floor alone. It was hardly surprising that some of them recognized my face.

“It’s the Sleeping Dragon of Shanxi!”

“What? The one from the Jin Family of Taiyuan?”

“Do you think there are two Sleeping Dragons of Shanxi? I knew his face looked familiar.”

*My reputation as the Sleeping Dragon of Shanxi really does reach the heavens.*

I was just about to give the crowd a pleased smile and wave when someone spoke up.

“Are you sure? I saw the Sleeping Dragon of Shanxi at Honghwaru around this time last year, but he looks a little…”

“You don’t remember that the two of us were there together?”

“Oh. Were we?”

“Yes. His build and overall impression have changed quite a bit, but it’s definitely him. I can still see him causing a scene because he wanted to bring a courtesan back to the Jin Family.”

“…”

*Damn. Why do people remember such useless things?*

As I awkwardly lowered my hand, several of the guests who had been whispering among themselves suddenly raised their hands.

“I was there, too!”

“You were, Brother?”

“I remember it clearly. That guy—no, that gentleman—fell down the stairs, grabbed the thing between my legs, and gave it a long yank… Whew. Just thinking about it still makes me dizzy.”

“My goodness, how indecent. Are you all right now?”

“Fortunately, I’m perfectly fine. Not only that, I think it’s gotten a little longer since then.”

“…”

*Can that happen?*

I barely managed to suppress my urge to ask the man who had just spoken exactly how much longer it had gotten. There was still the trash from the so-called Five Gates of Shanxi to deal with.

But then…

“Huh?”

What came into view were four young prodigies with their heads planted on the floor in a row—and Hyuk Mujin standing there with his head held oddly high.

“We’re ready.”

“Did you order them to do this?”

“They say that even a village-school dog can recite poetry after three years. Now, if you give me a hint, I know exactly what to do.”

“You little…”

I was seized by an indescribable emotion.

At first, I had thought he was an idiot, but he seemed to be getting smarter by the day.

I was almost suspicious that he was putting points into Intelligence for me.

“You’ve grown. I’m very proud of you.”

“You’re too kind. More importantly, what should we do with them?”

“Give me the sword case.”

“At your command.”

It was straight out of a historical drama. I took the sword case Hyuk Mujin held out and brought it down against my palm.

The grip was good, and the impact felt good, too.

“Everyone, get up.”

The four young prodigies sprang to their feet the moment I spoke.

Ignoring their terrified gazes, I scanned their Level Windows again. Just as I thought, they were barely First Rate, if that.

“You already know what you did wrong… You’re the heirs of the Five Gates of Shanxi?”

“Y-yes, sir!”

“The third son, the youngest daughter, that sort of thing?”

“No!”

“Are you sure?”

“Yes, we are!”

Their voices, filled with proper martial spirit, rang through the inn. I tapped the sword case against my palm and muttered,

“Really? Then the Five Gates of Shanxi aren’t anything special, are they?”

“…”

“…”

Every one of their faces flushed with shame, but none of them dared to answer.

They knew who I was now.

Their difference in martial power was only the second issue. Even putting that aside, people from the Five Gates of Shanxi couldn’t hold their heads high in front of the Jin Family of Taiyuan.

“You’ve had it good all this time, haven’t you?”

“…No.”

“What do you mean, no? You never had to worry about money, and you had powerful backing. You relied on that and lived large all this time, didn’t you? Picking fights wherever you went.”

“…”

“But then a war broke out between the Jin Family of Taiyuan and the Mount Heng Sword Sect. The Jin Family was the one that had always treated you well, but you were afraid of the retaliation that would come if Mount Heng won, so you kept watching the situation and ended up here. Right?”

“Th-that’s… We…”

“You’re the heirs, aren’t you? A Young Sect Leader, a Lesser Family Head—something like that, right? Ah, that fellow over there was the Young Bureau Head.”

The four people I pointed toward reflexively glanced in that direction and shuddered.

Unable to endure the merciless barrage of slaps and trash talk, Woo Jintae had chosen to pass out. He lay on the floor as though he were dead.

“Anyway, given the situation, you should’ve kept your heads down. What did you come all the way here for, acting so high and mighty? Do you think the Jin Family of Taiyuan is a joke? Do I need to tattoo ‘Sleeping Dragon of Shanxi’ on my forehead and walk around with it?”

“I-I’m sorry.”

“Does apologizing make everything go away? Should I beat you into a bloody mess and then apologize to you?”

“Eek!”

Just look at those terrified eyes. I felt like a walking disaster.

This was a situation that no longer required words. I raised the sword case.

“Historically, this has always been an effective remedy. Everyone, get down.”

Then I asked the four trembling young prodigies who lay face down in a chilling voice,

“How many blows will it take for you to reflect? Each of you, give me a number.”

“W-what?”

“Give me a number. I beat that Woo Jintae so badly because he was acting too high and mighty. Since you paid up voluntarily, I’ll take that into consideration.”

A heavy silence descended.

The four of them exchanged hurried glances before shouting as one.

“J-just one!”

“One? Will that really be enough?”

“Yes, sir!”

“If you take one hit, will you swear never to do anything like this again?”

“We swear it before Heaven and Earth and all the divine spirits!”

I gripped the sword case tightly.

“Good. Then ten each.”

“……!”

“……!”

“I just asked Heaven and Earth, and they said one wouldn’t come close to being enough for you. So ten it is.”

I never thought I’d find myself in a situation like this.

Back in school, I felt like one of those physical-education entrance-exam teachers who swung a bat whenever he got the chance.

Wallowing in a strange sense of nostalgia, I swung the bat—or rather, the sword case.

*Whack! Whack! Whack! Crack!*

“Guh!”

“Don’t move. You’ll hurt your bones. All right, again.”

*Whack! Whack! Whack!*

It must have been a rare sight for everyone filling Honghwa Inn. The heirs of the Five Gates of Shanxi were crawling across the floor like grubs.

There were even two women among them.

The whispers of the people surrounding us cut into my ears.

“Is that really okay?”

“I know, right? Even if they are the Five Gates of Shanxi… Couldn’t this turn into one of those big fights over Murim gratitude and grudges?”

“Don’t be so clueless. Are you really that out of touch with what’s happening these days? Maybe things would be different if the Mount Heng Sword Sect were still standing, but to stop the Jin Family of Taiyuan now, every small and medium-sized sect in Shanxi would have to join forces—and even then, they might not manage it.”

“It’s that bad?”

“They might have the numbers if they gathered everyone, but the caliber is completely different. You only have to look at the Sleeping Dragon of Shanxi over there to know that.”

“That’s true. Those Five Gates heirs swaggered around acting so important, but they’re completely worthless in front of the Sleeping Dragon of Shanxi.”

“If you think about it, they were the ones who picked the fight first.”

“That’s true, too.”

“And since we’re on the subject, there’s something rotten about all those people who call themselves the Five Gates of Shanxi these days.”

“Rotten?”

“They call themselves an orthodox faction, but they’re really just sucking the marrow out of ordinary people without anyone noticing. Just look at the Seongun Escort Bureau. How many complaints have merchants made about them?”

“Were all those rumors true?”

“What about the Jin Family of Taiyuan? When there was a famine ten years ago, they released relief grain. Long before that, they even held off the Demonic Cult. Those bastards were vicious murderers who went around killing ordinary people like us. If not for the Jin Family of Taiyuan…”

“Ugh. I don’t even want to think about it.”

“That’s right. I also heard it was the Jin Family of Taiyuan that drove off the mounted bandits who came over from Gaoyuan this time.”

“Is there anyone who hasn’t heard that rumor yet? They say the Heaven Shaking Sword and the Sleeping Dragon of Shanxi slaughtered every last one of them.”

“My goodness.”

“So even if another war breaks out, what’s there to worry about? I swear, if the Five Gates of Shanxi try to make an issue of this, I’ll join the Jin Family of Taiyuan and fight alongside them!”

“Oh!”

“That’s some impressive chivalrous spirit for such a young man. Now that I’ve heard you out, I think you’re right. Here, have a drink on me!”

*Whack! Whack! Whack!*

I had turned three of the four young prodigies into grubs when I turned my head toward the voices.

They were defending the Jin Family of Taiyuan with such passion that, by the time I finished listening, I almost wanted to buy them a drink.

*In terms of mindset, he’s already one of our Jin Family.*

If his Level were high enough, he’d be my first pick for recruitment. Smiling with satisfaction, I checked the Level Window of the great orator.

> **System**
>
> **Level 15: Jang Childeuk**

“…What the fuck?”

*Jang Childeuk? The Jang Childeuk I know?*

Looking again, I realized that I definitely knew the face.

He was the servant who had brought us meals every day while I was receiving one-on-one intensive training from Jin Mukyung.

That Jang Childeuk was the great orator’s true identity.

*Holy shit. Goose bumps.*

No wonder he had been taking the Jin Family’s side so aggressively.

He hadn’t said anything incorrect, of course, but manipulating public opinion like this…

Just as I trembled at the feeling that I had uncovered some enormous conspiracy in the political world, someone spoke up.

“Um…”

It was Cheongpung, the one person I had momentarily forgotten. He opened his mouth with his clear eyes shining.

“There’s still one person left.”

“Ah.”

The last man lying face down flinched. Cheongpung seemed innocent in his own way, but he was also strangely frightening.

Not that I had any intention of going easy on him just because he was last.

“I was just about to hit him.”

I was about to swing the sword case when Cheongpung spoke again.

“Excuse me. May I ask you one difficult favor?”

“We’re out of candied hawthorn skewers[^2] now.”

[^2]: Candied hawthorn skewers are a traditional snack of fruit skewers coated in hardened sugar.

“That’s not it. I, uh…”

Cheongpung hesitated, then quietly pointed at the sword case.

“I’d like to try hitting the last gentleman once.”

“What?”

“I’ve never done anything like this before…”

“…”

I had seen every kind of nutcase in my life, but this was my first time seeing a first-experience villain.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 135`.

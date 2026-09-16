# Master Edit Task — Chapter 153

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
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 화산파    | **Huashan**                      |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 사자후 | **lion's roar** | Taekyung's term for Song Il's crowd-shattering roar. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 나발이고 | slang | Dismissive rejection of the preceding concern (to hell with X), not a neutral “or not.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |
| 고생하셨습니다 | register | Subordinate courtesy (“thank you for your hard work”), not a superior’s “Good work.” | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 145–149

## Plot

Jin Taekyung pressures the four heirs of the Five Gates of Shanxi other than the Seongun Escort Bureau to support the Jin Family of Taiyuan, Huashan, and the government, threatening to absorb Gopyeong Sect as a Jin Family branch if necessary. He invites ten-year-old Prince Shangshan Zhu Bao to the Jin Family’s grand banquet in fifteen days and promises to obtain Jin Mukyung’s autograph, though Zhu Bao refuses Cheongpung’s autograph until Cheongpung earns a martial title.

At the luncheon’s conclusion, Zhu Bao gives Taekyung Prince Shangshan’s Token as the Quest Reward. Hong Jin then joins Taekyung’s journey to the Jin Family, sending Jin Wikyung a thousand silver nyang and arranging a large escort and delegation. Cheongpung receives the Royal Guard Armor Set and decides to stay with the Jin Family temporarily. The Five Gates’ young prodigies remain at Honghwa Inn until New Year’s Day to support the Seongun Escort Bureau. During the journey, Cheongpung reveals that he came to Huashan at age three or four and was not born there; Hong Jin discloses that he is a eunuch, formerly served the late Emperor, was assigned to Prince Shangshan, and reached the frontier in something like exile.

Wikyung prepares an extravagant, bribe-influenced welcome for Hong Jin. He and Hong Jin immediately establish a playful rapport, while Cheongpung reveals that Mae Jonghak is his grandfather and that he secretly left Huashan to defeat all the Ten Dragons and Phoenixes. He chooses Jin Mukyung as his first opponent. Cheongpung activates the Zaha Divine Technique, and his light-flames collide with Mukyung’s Sword Energy as their duel begins; the outcome is unresolved.

Meanwhile, Huashan’s Lone Crane, Baek Museong, travels with fellow Three Plum Blossom Elites Chulwoo and Eunhyang toward the Jin Family. After Chulwoo and Eunhyang cause trouble with the Black Serpent Sect in Xi’an, Baek makes them return the stolen money and jade hairpin and apologizes to the innkeeper. Huashan has been sealed since Mae Jonghak entered the sleeping Sect Leader’s quarters, left a dagger and handwritten note, and disappeared. A messenger from Shanxi prompted Huashan to dispatch the Three Elites, and Baek looks forward to seeing how Cheongpung has grown since their meeting ten years earlier.

## Continuity

- Prince Shangshan’s Token has been obtained as the completed luncheon Quest Reward; Zhu Bao is expected at the Jin Family’s grand banquet in roughly fifteen days, around New Year’s Day.
- Zhu Bao is ten years old, an exceptionally skilled young swordsman, and an admirer of Jin Taekyung. Jin Mukyung refused Zhu Bao’s autograph three years earlier; Taekyung has promised to obtain it.
- Cheongpung is a twenty-year-old Peak master, grandson and disciple of Sword Saint Mae Jonghak. He secretly left Huashan without Mae Jonghak’s knowledge and is undertaking a dueling tour against the Ten Dragons and Phoenixes.
- Cheongpung’s duel with Jin Mukyung has begun, but its outcome is unknown. Cheongpung still lacks a martial title, which Zhu Bao requires before accepting his autograph.
- Cheongpung came to Huashan at about age three or four rather than being born there. His parentage and Mae Jonghak’s statement that a crane delivered him remain unexplained.
- Mae Jonghak disappeared after entering the sleeping Huashan Sect Leader’s quarters, leaving a dagger and handwritten note. Huashan is sealed, and the search for Mae Jonghak’s hidden residence remains unresolved.
- Baek Museong is Huashan’s Lone Crane and the first of the Three Plum Blossom Elites. Chulwoo and Eunhyang are his junior disciples and fellow Elites; both are notorious troublemakers.
- Hong Jin is a eunuch who formerly served the late Emperor and has served Prince Shangshan since infancy. His circumstances of castration, exile-like transfer to the frontier, and political role remain unclear.
- Hong Jin and Jin Wikyung have formed a joking rapport. Hong Jin bribed Wikyung with one thousand silver nyang, prompting the Jin Family’s extravagant pro-imperial welcome.
- Hong Jin and Li Feng continue pursuing the Shaanxi–Shanxi trade project through Huashan, with the Seongun Escort Bureau as the proposed base. Taekyung is to relay the proposal to Jin Wikyung.
- The four non-Seongun heirs of the Five Gates will remain at Honghwa Inn until New Year’s Day while supporting Taekyung’s side.
- Gong Ilhyuk remains humiliated and vengeful; the identities of the other two members of the Three Hands of Zhongnan are unknown.
- Taekyung remains below the Peak realm and cannot use Sword Energy despite his victories over Peak masters.

## Translation Decisions

- Render **주표** as “Zhu Bao,” **상산왕** as “Prince Shangshan,” and **상산왕의 패** as “Prince Shangshan’s Token.”
- Render **고평문** as “Gopyeong Sect” and **고평지부** as “Gopyeong Branch of the Jin Family of Taiyuan.”
- Render **비무행** as “dueling tour,” **청강검** as “blue-steel sword,” and **광염** as “light-flames.”
- Render **화산일학** as “Huashan’s Lone Crane,” **매화삼절** as “Three Plum Blossom Elites,” and **매화검수** as “Plum Blossom Swordsmen.”
- Use “Senior Brother” for **대사형** and “Big Brother” for **큰 오라버니** when Eunhyang deliberately uses the familiar alternative.
- Preserve the crude eunuch misunderstanding and Cheongpung’s innocent “ball friend” joke.
- Render **금성전장** as “Golden Star Exchange,” **전표** as “bank draft,” **은자** as “silver nyang,” **철전** as “iron coins,” **은원보** as “silver yuanbao,” and **사서삼경** as “Four Books and Three Classics.”
- Continue rendering **전하** as “His Highness” formally and **왕** as “king” when used literally.

### Prior accepted reading-copy tails

#### Chapter 151 tail (verified mastered)

…
talking nonsense.” “That was just something I said. If I disliked you, would I have kept you around all this time?” “Wasn’t it because you were bored? Sometimes you seemed to enjoy hitting me when your hands got restless.” “…” Just how much of a piece of trash did this bastard think I was? When I glared at him, Hyuk Mujin hurriedly pretended nothing had happened. “Ahem. Ahem, ahem…” “Listen, if I hadn’t planned to raise you up, I would have gone around alone a long time ago. Why would I lug around deadweight like you?” “Deadweight? Can you really change your story that easily? A moment ago, I was your right arm or your heart.” “Right arm, my ass. At your current level, I’ll let you be my little toe.” “Wow. That’s harsh. Really.” He sounded hurt, but he couldn’t hide the corners of his mouth, which kept rising. Right arm or little toe, they were both important parts of the body. That fact didn’t change. Feeling strangely embarrassed, I shouted, “Enough! Are you doing this or not?” “I’m actually a martial arts genius, you know. I might copy everything you do. Are you sure that’s okay?” “Bullshit. Copy it if you can.” “Really?” “Ask one more time and I’ll hit you so it really hurts.” Hyuk Mujin broke into a broad smile. “I’ll do it.” His voice sounded lighter, as though he had shed an old skin. * * * Hyuk Mujin and I sat on the floor of the training ground and looked at Cheongpung. Taking a seat was the basic requirement before the real lecture began. “All right. Let’s begin.” “I look forward to learning from you, Young Hero Cheongpung.” “Yes, yes! Hoo, hoo…” Every time Cheongpung took a heavy breath, white steam puffed from his nose into the cold winter air. What was wrong with him all of a sudden? “Are you all right?” “I’m fine!” “You startled me. Why are you suddenly acting like this?” “Oh. Um, well…” Cheongpung hesitated, then spoke with a face flushed bright red. “This is my first time teaching anyone, so I’m too excited and worked up... Whew, give me a moment.” “…” “…” I knew this would happen. Perhaps he was still nervous, because Cheongpung spoke in a trembling voice. “Th-then I’ll begin.” “Don’t make it so stiff. Just relax.” “R-relax?” “Yes. Relax. Just teach us in whatever way you’re comfortable with, Young Hero Cheongpung.” “The way I’m most comfortable…” “The way your grandfather taught you.” “Oh. What an easy solution!” Hyuk Mujin and I looked at Cheongpung with a mixture of anticipation and curiosity. This was the teaching method of the Sword Saint himself. How had that great martial artist raised this genius? *It must be something completely different.* As Cheongpung sank into thought, a smile appeared on his lips. Apparently, merely thinking about the method put him in a good mood. “Oh, I thought of something. This training will probably help both of you a great deal, too.” “Ohhh.” “Ooooooh. What is it?” “Do you see that?” We turned in the direction Cheongpung was pointing. Hyuk Mujin spoke first, and I finished the thought. “That’s…” “The training hall.” It stood roughly two hundred jang from the training ground. I had a pretty good idea what kind of training he meant, and a quiet laugh escaped me. It was the classic touch-and-go method: repeatedly running like hell to touch the destination and come back. *I expected something special from the Sword Saint, but I guess he wasn’t that different.* It was certainly a classic, but it was an effective exercise for building endurance and strengthening the lower body. I stood and began stretching leisurely. “Do we just go there and come back?” Cheongpung tilted his head. “Huh? You’ve done this before?” “Until I was sick of it.” “Oh, I see. That’s a relief.” Cheongpung smiled brightly and pointed to me, then Hyuk Mujin. “Then I’ll give you half a shichen and one shichen, respectively.” “…?” “…?” “What?” I asked in confusion. “Half a shichen? What do you mean?” “Didn’t you say you’d done it until you were sick of it? That should be plenty of time for you.” “That’s true, but... Ah, I get it. Do we have to make nonstop round trips for half a shichen?” “No. Once will be enough for now. I’ll wait for you at the summit.” “What? The summit?” “Yes. There.” This time, I saw it clearly. Cheongpung’s raised fingertip was pointing at the cliff behind the training hall. Hyuk Mujin and I dropped our jaws at the same time. *Holy shit. What the hell is that?* The height was impossibly vast. Even judging by eye, it was a steep cliff hundreds of jang high. My vision went dark, and my hands and feet began to tremble. If it affected me this badly, Hyuk Mujin had to be even worse. “Are you saying… we have to climb that?” “Yes! I picked it because it’s about the same height as the place I climbed every day when I was little.” “…” “…” “Ah, that brings back memories. I fell halfway down and nearly died twice. It really hurt back then.” “…!” “…!” He was insane. The Sword Saint was insane, and this bastard was insane too. [^1]: Candied hawthorn skewers are a traditional snack made by coating fruit on skewers in hardened sugar.

#### Chapter 152 tail (verified mastered)

…
“What are those?” “Birds, probably.” As Childeuk stared blankly at the sky, his gaze drifted toward the dizzyingly high cliff. Suddenly, his eyes narrowed. “What about that thing clinging to the cliff?” “The cliff? What’s on the cliff?” “Yes. It’s pretty big.” “Dunno. Must be a pretty big bird. Hold on, I brought a bottle of liquor somewhere…” Without even looking where Childeuk was pointing, Hong pulled a small porcelain bottle from his robes. “It looks a little too big to be a bird.” “It could be a Heavenly Eagle. Those things are as big as people. They aren’t ordinary hawks.” “Wow. It really is as big as a person.” “They’re even called spirit creatures. I heard their wingspan alone is more than a jang. I’ve only seen one from a distance, myself.” “But, hyung.” “What? Why do you keep calling me?” “Do Heavenly Eagles fall, too?” “What the hell are you talking about?” Hong, who had been tipping the bottle toward his mouth, hurriedly looked at the cliff. At that dizzying height, a massive dot was plummeting rapidly. “Aaaaaaah!” Childeuk marveled. “It really is a spirit creature. Its scream sounds exactly like a person.” “That’s a person, you lunatic!” “Whaaa!” “Move! Move!” The instant Hong screamed, a person crashed into the ground amid a shower of stone fragments. *Boom! Rumble, rumble!* Rocks and dust burst in every direction. The two men swallowed at the same time. “D-do you think he’s dead?” “Try falling from that height. Even the Jade Emperor would die.” How had such a horrific calamity intruded upon their peaceful routine? The middle-aged martial artist clutched his trembling chest and stared at the body lying facedown. “What kind of madman falls from a cliff…” “He looks young.” “Does it matter whether he’s young or old? The important thing is that he’s dead.” “That’s true, but…” “Go turn him over.” “M-me?” “Who else is here besides you and me? Hurry!” At the middle-aged martial artist’s shout, Jang Childeuk hesitantly began approaching the body. He had only been a martial artist for a month. This was the first time he had ever witnessed someone die right in front of him. “Huff, huff.” The closer he got, the more clearly he could see the body. Its limbs lay limp, and blood streamed from the back of its head as it lay facedown on the ground. Considering the height of the fall, the corpse looked surprisingly intact. “M-may you be reborn in paradise.” He squeezed his eyes shut and reached out to touch the body. That was when it suddenly shot upright. *Crack!* The world flashed before Childeuk’s eyes, followed by a wave of excruciating pain. He landed hard on his backside, his mouth hanging open, unaware that blood was streaming from both nostrils. “Uh… uhhhh.” “What in the… Ugh, ughhh!” Hong’s legs gave out, and he collapsed. “The corpse—the corpse is alive!” “Ugh! It’s a jiangshi! A jiangshi[^1] has appeared!” The dirt-covered stranger who had suddenly been written off as dead staggered to his feet. His hair was wild, and blood vessels had burst in his eyes. He looked around, then ground his teeth. “Fuck, Taecho Village[^2] again?” * * * Damn, that hurts. Head, shoulders, knees, feet, knees, feet… There wasn’t a single part of me that didn’t ache. Luckily, I’d driven a dagger into the cliff and slowed my fall. Otherwise, I might have kicked the bucket. Of course, the physique and toughness stats I had steadily raised had helped, too. “Ow, the back of my head is throbbing.” I touched the tender spot and found it wet with blood. I tore off a strip of my sleeve and was wiping away the blood when— “W-who are you?!” “Reveal your identity, you scoundrel!” Oh, right. These two guys were here too. One of the two men pointing swords at me looked familiar. What was his name again… “Jang Childeuk?” Mr. Jang Childeuk, who had been working hard to manipulate public opinion at Honghwa Inn until just a few days ago, recoiled in terror. “Gasp! How do you know my name?!” “The jiangshi is talking! It’s bewitching people with its words!” “…Who are you calling a jiangshi? Can’t you see I’m breathing just fine?” The middle-aged man with the patchy beard glared at me and shouted. “You evil creature! You can’t fool my eyes. If you were human, you couldn’t possibly be fine after falling from that height. Who sent you? The Demonic Cult? The Blood Cult? Or perhaps…” “Taecho Village! Hyung, that jiangshi definitely said ‘Taecho Village.’” “That’s right! You’re a jiangshi sent by Taecho Village!” The middle-aged man shouted as if he had finally figured it out, then suddenly stopped and asked Childeuk, “But where is Taecho Village?” “I don’t know either.” “…” It would have been strange if he did. I gave up on the conversation and wiped the dirt from my face with my sleeve. The middle-aged man might not know me, but Childeuk knew my face well. This would be faster. “Gasp! Third Young Master!” “Yes. Long time no see.” “Little brother, the Third Young Master? What in the world are you talking about?” “The Third Young Master has become a jiangshi!” “…” How the hell did he reach that conclusion? [^1]: A jiangshi is a reanimated corpse from Chinese folklore, often depicted as a hopping vampire. [^2]: *Taecho* means “primordial” or “the beginning.”

## Korean source

```text
＃153화



“그러니까…….”

장칠득이 힘겹게 말을 이었다.

“수련 중이셨다고요?”

“네.”

“혹시 벽호공(壁虎功)을 익히고 계셨던 겁니까?”

“저도 잘은 모르겠는데 일단 그런 것 같아요.”

벽호공. 무협 소설에서 많이 봤다.

도마뱀이 벽을 타는 모습에서 창안된 무공이라던가?

현실에 존재하는 스포츠인 클라이밍(Climbing)과 비슷하지만 다른 점이 딱 두 가지가 있다.

첫째, 클라이밍과는 달리 공력을 사용한다.

둘째, 안전장치가 없다.

‘역시 무림이야, 빠꾸가 없지.’

떨어지면 골로 가는, 그야말로 상남자의 무공이다.

내가 고개를 끄덕이자 두 사람이 귀신 바라보듯 나를 쳐다봤다.

“이 높이에서요?”

“그게 됩니까?”

“되던데요.”

처음 청풍의 말을 들었을 때는 나도 무슨 미친 소린가 했다. 그런데 하니까 되더라.

지금까지 시도해 보지 않아서 비현실적으로 느껴졌을 뿐, 내 육신은 이미 초인의 영역에 들었다고 해도 과언이 아니다.

“아이고, 삼공자님. 이러다가 큰일이라도 나면 어쩌려고 그러십니까!”

중년 아재가 호들갑을 떨며 내 몸에 묻은 먼지를 툭툭 털어 주었다.

한 3분 전까지만 하더라도 태초 마을에서 온 강시 취급 하더니, 지금은 삼대독자 아들 대하듯 조심스럽다.

“자자, 수련은 이쯤 하시고 처소로 돌아가시는 게 좋을 것 같습니다.”

“왜요?”

“왜라니요! 이번에는 운이 좋았기에 망정이지, 한 번 더 떨어지셨다가는 정말 돌아가실지도 모릅니다.”

나는 손을 내저었다.

“괜찮아요. 한두 번도 아니고.”

“예?”

“지금이 벌써 다섯 번짼데요. 뭘 새삼스럽게.”

“다섯…… 번이요?”

“네. 다섯 번.”

떨리는 눈빛이 나와 가파른 절벽을 번갈아 바라본다.

“도, 도대체 어떻게 아직 살아 계신 겁니까?”

“괜찮아요. 열 번도 넘게 떨어진 놈도 있으니까.”

“……?”

“……?”

“슬슬 한 번 더 떨어질 때가 됐는데…… 아, 저기 온다.”

나는 높이 솟은 절벽 한군데를 가리켰다. 점점 커져 가는 검은 점 하나와 찢어지는 비명이 뒤를 이었다.

“끼아아아아악! 조오오자아앙!”

두 사람이 입을 딱 벌렸다.

“세상에. 정말 한 명 더 있었네.”

“저건 누굽니까?”

“제 오른팔, 아니 새끼발가락이요.”

“예? 그게 무슨.”

“아니, 그 전에 당장 구해 줘야 하는 것 아닙니까?”

“구해요? 저걸?”

나는 고개를 가로저었다.

혁무진도 신체 건장한 성인 남성이다. 저 높이에서 추락하는 녀석을 받아 들었다가는 어디 한군데 부러지는 정도로 안 끝난다.

“그냥 내버려 두세요. 괜히 끼어들었다가 다치지 마시고.”

두 사람이 비명을 내질렀다.

“떨어진다! 떨어진다!”

“이대로 두면 죽을 겁니다!”

“쟤 안 죽어요.”

그랬으면 이미 열 번도 더 죽었지.

하지만 혁무진에게는 동아줄이 있다. 언제나 한 끗 차이로 그를 구해 주는 튼튼한 동아줄이.

“끼아아아악!”

추락하는 혁무진의 비명이 시시각각 가까워져 마침내 경악한 표정조차 생생하게 보인 그 순간, 저 위에서 빛줄기가 번쩍였다.

유성(流星)처럼 빠르게 급강하하는 그것은 은은한 자줏빛으로 빛나고 있었다.

“저, 저게…….”

“뭡니까?”

내가 짤막하게 대답했다.

“자하신공.”

정확히는 자하신공을 끌어 올린 누군가지.

두 사람에게는 보이지 않겠지만, 내 눈에는 자하신공 특유의 자색 기운에 휩싸인 청풍이 똑똑히 보였다.

녀석은 입이 찢어져라 웃고 있다.

“우와아아아아!”

“…….”

저놈 저거 신난 거 봐라.

그러나 살짝 맛이 간 성격과는 별개로 능력 하나만큼은 넘사벽이다. 나는 이어지는 광경에 혀를 내둘렀다.

‘어떻게 저게 가능하지?’

화살처럼 쏘아진 청풍은 눈 깜짝할 시간 만에 혁무진의 허리를 낚아챘다.

그리고 급속도로 가까워진 지면을 향해 손바닥을 내밀었다.

팡! 퍼버벙!

한 번, 두 번, 세 번…….

압축된 공기가 터져 나가는 소리와 함께 바닥이 푹푹 파인다.

보이지 않는 거인이 주먹으로 내리친다면 이렇게 될까?

청풍이 일장(一掌)을 내지를 때마다 얼어붙은 땅이 뒤집히고 그 반발력으로 추락하던 신형이 허공에 멈춘다. 이내 청풍의 발이 사뿐히 땅을 밟았다.

“휴, 이번에도 재밌었다. 그렇죠?”

이미 혼절한 혁무진이 신음을 내뱉었다.

“흐어, 흐어어어.”

“역시, 좋아하실 줄 알았어요.”

“…….”

도대체 어딜 봐서?

즐겁게 웃으며 혁무진을 내려놓은 청풍이 내게 알은체를 해 왔다.

“엇, 은인! 아직 여기 계셨네요?”

“떨어졌거든요. 누구 덕분에.”

나는 청풍을 지그시 노려봤다.

사실 지금까지 정상에 오를 기회가 몇 번이나 있었다. 문제는 청풍이라는 놈이 보통 정신 상태의 소유자가 아니라는 것이지.

“헤헤, 제 덕분이라고 해 주시니 기분이 좋아지네요.”

“닥쳐! 당신이 위에서 훼방만 안 놨어도 진작 올라왔어!”

“헉! 진정하세요, 은인!”

“진정? 그런 말은 돌 굴리기 전에 했어야지!”

생각해 봐라.

맨손으로 백여 장이 훌쩍 넘는 절벽을 기어오르는 것도 만만치 않은데, 어느 정도 왔다 싶으면 위에서 어린애만 한 돌덩이가 와르르 쏟아진다.

청풍의 천진난만한 외침은 덤이다.



‘은인, 돌 굴러가요!’



이건 당해 본 사람만 안다. 석가모니가 내 입장이었어도 염주로 저놈 목 졸라 죽였다.

‘다시 생각하니까 열받네.’

그냥 확 들이받아 버릴까.

주먹을 움켜쥔 그때, 바닥에 누워 손가락만 움찔거리던 혁무진이 비명과 함께 벌떡 일어났다.

“끼아아아아아!”

“야, 야. 숨 쉬어, 숨. 여기 땅이야.”

“허억, 허어어억. 저 살아 있는 거 맞습니까?”

“그래, 인마. 아직 살아 있어.”

“무, 물 좀.”

청풍이 허리춤에 찬 죽통을 내밀었다.

“여기요.”

“고맙…….”

무심코 죽통을 받아 들던 혁무진의 신형이 우뚝 굳었다.

그리고 곧이어 터져 나오는 사자후.

“야, 이 개새끼야!”

눈이 뒤집혀 날뛰는 혁무진의 모습에 청풍이 기겁했다.

“저, 저한테 갑자기 왜 이러세요!”

“지금 몰라서 묻냐? 조장, 저 새끼 잡아요!”

“저는 할아버지께 배운 그대로 해 드리고 있는 건데.”

“당장 이리 안 와!”

“은인, 이따 위에서 뵐게요!”

혁무진을 피해 후다닥 물러난 청풍이 땅을 박찼다.

쾅! 단번에 십여 미터를 날아오른 녀석은 절벽에 철썩 달라붙더니 벽호공을 펼쳐 절벽을 올라가기 시작했다.

파파파파팍!

역시 고인물.

태어날 때부터 사족보행이었던 것처럼 빠르게 사라지는 청풍의 모습에 혁무진이 주저앉았다.

“저, 저 자식이 저한테 돌을, 돌을…….”

내가 숙연하게 대답했다.

“알아. 아까 너 떨어지는 거 봤어. 눈에 맞았더라.”

“저거 완전히 미친놈이에요. 어린애 머리통만 한 걸 던져요.”

“내 것보다는 작네. 나한텐 흙도 뿌리던데.”

“조장. 저 결심했습니다.”

“뭘?”

“저놈 잡아서 족치기 전까지는 포기 안 합니다. 사나이 혁무진의 이름을 걸고 맹세하는 거예요.”

혁무진의 눈동자가 이글이글 타올랐다.

지금처럼 열의에 불타는 모습은 처음 본다. 속마음은 어떨지 몰라도 표면적으로는 늘 유쾌하고 설렁설렁한 녀석이었으니까.

‘설마 이걸 노리고?’

이 모든 게 혁무진의 분노를 끌어 올려 최선을 다하게 만들려는 청풍의…….

아니다. 저 화산파 출신 자연인에게는 그런 머리가 없다.

‘뭐, 좋은 게 좋은 거지.’

씩씩거리는 혁무진에게 보퉁이 하나를 던졌다.

“품에 잘 챙겨 놔.”

“이게 뭡니까?”

“벽곡단. 수련 시작 전에 챙겨 놨었지.”

허기와 기력을 보충하는 것에는 저만한 게 없다. 크기가 작고 무게가 가벼우니 휴대도 간편하고.

“올라가다가 힘 딸린다 싶으면 먹어라.”

“사방이 낭떠러지인데 벽곡단을 어디서 먹습니까. 전 당장 올라가서 저놈을 단칼에…….”

“단칼에 죽을걸.”

새로 배운 벽호공으로 북망산을 타고 싶은 모양이다. 나는 혁무진의 뒤통수를 갈겼다.

“악!”

“그리고 절벽이 일직선이냐? 중간중간 깎여 있는 곳도 있으니까 알아서 자리 잡고 먹어. 조급해하다가 떨어지지 말고 천천히, 한 번에 성공하겠다는 생각으로 해.”

“후우.”

“그럼 가자.”

“옛!”

나와 혁무진이 결연한 표정으로 절벽 앞에 섰을 때였다.

“저기…….”

“사, 삼공자님.”

맞다. 이 사람들도 있었지.

장칠득과 중년 아재가 머뭇거리며 입을 열었다.

“소가주님께 보고를 해도 괜찮겠습니까?”

“아무래도 사안이 사안인지라. 공자님께서 부상이라도 입으시면 저희가…….”

손을 들어 그들의 말을 막았다.

뒷말은 듣지 않아도 충분히 짐작할 수 있었다. 직장인들 입장은 내가 더 잘 안다.

“보고하세요, 단.”

“단?”

“근무 끝나고 난 후에. 지금 얼마나 남았죠?”

“이제 세 시진 정도 남았습니다.”

“그 정도면 충분해요.”

벌써 절벽을 오르기 시작한 지 반나절.

남은 세 시진 안에 이 지긋지긋한 절벽을 정복할 생각이었다.



* * *



높고 가파른 이 이름 모를 절벽은 세월을 고스란히 맞아 어느 부분은 울퉁불퉁하고, 또 어떤 부분은 매끄럽다.

두꺼운 뿌리나 암석이 튀어나와 있어 잡기 쉬운 구간이 있는가 하면 조그마한 틈에 손가락 하나를 끼워 넣어 버텨야 할 때도 있었다.

‘하다못해 공력이나 병장기를 쓰면 편해질 텐데.’

공력을 사용하면 단단한 암석도 두부처럼 으스러진다.

인벤토리에 있는 병장기를 꺼낸다면 단검을 계단처럼 박아가며 올라갈 수 있다.

굳이 손쉬운 방법을 놔두고 이 고생을 하는 이유는 수련이기 때문……인 것도 있지만 그렇게 하려고 할 때마다 청풍이 귀신같이 알아차리고 돌을 떨구기 때문이다.

투두두둑.

갑자기 위에서 돌가루가 쏟아진다는 건 불길한 징조다.

나와 혁무진은 황급히 팔로 머리를 가리고 외쳤다.

“안 했어요! 진짜 아무것도 안 했어! 돌 굴리지 마!”

“으어어어!”

저 위에서 희멀건 얼굴이 빼꼼 튀어나왔다.

“진짜요?”

우리는 미친 듯이 고개를 끄덕였다.

아직 절반도 못 왔다. 여기서 스톤 샤워를 맞고 떨어지면 올라오기 전 호언장담했던 것이 흑역사가 될 거다.

“믿어 주세요!”

“청풍 소협! 아니, 청풍 대협!”

“할아버지께서 그러셨어요. 수련에는 결코 꼼수가 있어서는 안 된다. 무공은 피와 땀으로 얻어지는 것이다.”

일장 연설을 늘어놓은 청풍이 선심 쓴다는 듯이 한마디를 덧붙였다.

“이번 한 번만 봐드릴게요.”

“…….”

“…….”

아주 상전이 따로 없다. 나와 혁무진은 분통을 참으며 다시 절벽을 오르기 시작했다.

아주 사소한 실수 하나만 해도 다시 저 아래로 곤두박질치는 상황.

이렇다 보니 감각이 날카로워지고 손가락, 발가락 하나하나에 엄청난 신경을 기울이게 된다.

‘겨울만 아니었어도 진작 올라갔을 텐데…….’

올라가면 갈수록 경사는 험난했고, 표면은 밋밋해졌다.

가뜩이나 미끄러운 절벽이다. 그런데 심지어 하루가 멀다고 산발적으로 흩날리는 눈발과 북쪽 고원에서 불어온 바람이 절벽을 거대한 얼음으로 만들어 버렸다.

‘막혔다. 도무지 길이 안 보여.’

입술을 잘근잘근 깨무는 내 시선에 문득 뭔가가 눈에 들어왔다. 아직 얼지 않은 눈덩이로 막혀 있는 바위 틈새.

손가락 하나 들어갈까 말까 한 작은 공간이다. 힘들겠지만 지금으로써는 별수 없다.

“흡!”

나는 기합과 함께 몸을 날렸다. 동시에 가장 작은 새끼손가락을 정확히 틈새에 꽂아 넣었다.

푹, 내 예상은 절반만 맞았다. 아직 얼지 않은 눈덩이는 뚫어 낼 수 있었지만, 틈새의 깊이가 생각보다 너무 짧다.

고작 손가락 한 마디. 그것도 새끼손가락으로 0.1t에 달하는 몸무게를 지탱해야 한다.

“끄응.”

아무리 나라고 해도 이건 좀 빡센데?

설상가상으로 틈새에 고인 물기 때문에 손가락이 서서히 미끄러지는 중이다.

‘시간을 지체하면 추락한다.’

이제 얼마 남지 않았다. 나는 호흡을 가다듬고 몸의 긴장을 가라앉혔다. 새끼손가락을 지지대 삼아 전신을 들어 올렸다.

그야말로 초인(超人)이라 불릴 만한 신체 능력.

띠링.



- [근력]이 1 상승했습니다.

- [민첩]이 1 상승했습니다.

- [체력]이 1 상승했습니다.



때마침 스탯 상승까지. 회심의 미소를 지으며 다음 틈새를 향해 손을 뻗으려던 그때였다.

‘흡!’

“조장!”

이런, 중요한 순간에 호흡이 흐트러졌다. 다시 호흡을 가다듬는데 혁무진의 외침이 이어졌다.

“이! 이!”

“뭐라는 거야! 잘 안 들려!”

세차게 불어오는 눈바람은 시야와 소리를 흩어 놓았다.

내가 다시 입을 떼려는데, 또렷한 고함이 귓가를 후려쳤다.

“위! 위요!”

“위?”

혁무진의 목소리가 들렸다는 것은 맹렬한 바람이 주춤했다는 뜻. 그제야 막혔던 시야가 트이고 귀가 뚫렸다.

나는 혁무진의 손짓을 따라 고개를 들어 마침내 목격했다.

얼굴을 향해 떨어지는 거대한 바위를.

후우우웅!

“아, 시바.”

쾅!



* * *



“와, 그 큰 바위를 맨주먹으로 깨트리실 줄이야.”

청풍의 감탄을 한 귀로 흘리고 털썩 드러누웠다.

아까만 해도 저 자식을 두들겨 패고 싶은 마음뿐이었는데, 지금은 진이 다 빠졌다.

‘올라왔다. 끝났다!’

손 하나 까딱하지 못하고 속으로만 환호를 지르고 있을 때, 푸르딩딩하게 얼어붙은 손이 정상을 짚었다.

“허억. 흐어억.”

“겨우 하루 만에 성공하시다니! 두 분 다 너무 대단해요!”

너만 아니었어도 한 시진 안에 성공했어, 인마.

한바탕 쏘아 주고 싶은데 힘들어서 말이 안 나온다. 성취감과 피로로 헉헉거리는 우리를 보며 청풍이 허리를 꾸벅 숙였다.

“정말 고생하셨습니다! 한 번 성공한 경험이 있으니 남은 아홉 번은 더 빨리 오르실 수 있을 거예요.”

“……?”

“……?”

얼마나 충격적인 말이었던지, 나와 혁무진은 숨을 몰아쉬는 것도 잊고 청풍을 바라봤다.

‘저게 무슨 말이야.’

설마 지금 내가 생각한 그건가? 아니겠지?

나는 현대 사회의 지식인답게 침착한 태도로 입을 열었다.

“아홉 번이라니. 그게 무슨 개소리십니까?”

“저희 할아버지께서…….”

이 자식은 자연인이야, 소년 탐정이야.

이 순간만큼은 검성이고 나발이고 눈이 뒤집힐 수밖에 없었다.

“그러니까 이걸 아홉 번을 더 하라고요?”

“네!”

“당신은 똑같이 여기서 바위 던지고?”

“네!”

“안 해.”

“네?”

나와 혁무진이 동시에 자리에 드러누웠다.

“안 한다고. 내려갈 힘도 없어. 배 째.”

“내 배도 째라. 이 악랄한 놈아!”

“푸헤헤.”

“……웃어?”

청풍이 싱글벙글 웃으며 말했다.

“죄송해요. 제가 처음 수련 시작했을 때 모습을 보는 것 같아서 그만.”

“거봐! 당신도 하기 싫었잖아!”

“아뇨. 전 재밌어서 계속하고 싶었는데 몸이 안 따라 주더라고요.”

혁무진이 내게만 들릴 정도로 작은 목소리로 중얼거렸다.

“……미친놈인가.”

“그래서 할아버지께 말씀드렸죠. 다리가 말을 안 들으니 내일 이어서 하면 안 되겠냐고.”

행복한 과거를 회상하던 청풍이 돌연 검을 뽑아 들었다. 동시에 자줏빛 검기가 발출됐다.

서걱.

얼음, 흙, 바위. 가릴 것 없이 모두 베어 버린 청풍이 말을 이었다.

“그랬더니 할아버지께서 대답하셨어요. 올라오는 게 어렵지. 내려가는 건 쉽다고. 잠깐만 참으면 금방 내려간다고요.”

쿠구구궁.

딱 나와 혁무진이 누워 있는 3평 남짓한 절벽의 끄트머리가 진동했다.

‘실화냐.’

멍해 있는 우리에게 청풍이 손을 흔들었다.

“아홉 번 남았어요.”

띠링.



- 퀘스트, [검성 수련 간접체험기]가 생성되었습니다.
```

## Current accepted English baseline

```markdown
# Chapter 153

“So…”

Jang Childeuk continued haltingly.

“You were training?”

“Yes.”

“Were you perhaps practicing the Wall Lizard Technique?”

“I’m not entirely sure myself, but I think so.”

The Wall Lizard Technique. I’d seen it plenty of times in wuxia novels.

Apparently, it had been created by observing lizards climbing walls.

It was similar to the real-world sport of climbing, but there were two key differences.

First, unlike climbing, it used internal energy.

Second, there were no safety devices.

*This really is the Murim. No holding back.*

If you fell, you were as good as dead. It was the ultimate macho martial art.

When I nodded, the two men stared at me as though I were a ghost.

“From this height?”

“Is that even possible?”

“It worked.”

When I first heard Cheongpung suggest it, I had wondered what kind of insane nonsense he was talking about, too. But once I tried it, it worked.

It had only seemed unrealistic because I had never attempted it before. My body had already entered the realm of the superhuman—it would not be an exaggeration to say so.

“Oh, my. Third Young Master, what will you do if something serious happens to you?”

The middle-aged guy fussed as he brushed the dust off my clothes.

Only three minutes ago, he had treated me like a jiangshi from Taecho Village. Now he was handling me as carefully as though I were his family’s precious only son, three generations in the making.

“Well, why don’t you stop training for now and return to your quarters?”

“Why?”

“What do you mean, why? You were lucky this time, but if you fall one more time, you could really die.”

I waved a hand dismissively.

“It’s fine. It’s not like this was my first or second time.”

“What?”

“This is already the fifth time. Why are you acting surprised now?”

“The fifth… time?”

“Yes. Five times.”

His trembling eyes moved back and forth between me and the steep cliff.

“H-how are you still alive?”

“It’s fine. There’s someone who’s fallen more than ten times.”

“…”

“…”

“Looks like it’s about time for him to fall again… Oh, there he comes.”

I pointed toward a spot high up on the cliff. A black dot that grew larger by the second was followed by a piercing scream.

“Aaaaaaah! Caaaaaptain!”

The two men’s mouths fell open.

“My goodness. There really was someone else.”

“Who is that?”

“My right arm—no, my little toe.”

“What? What does that mean?”

“No, wait. Shouldn’t we save him right now?”

“Save him? Him?”

I shook my head.

Hyuk Mujin was a healthy adult man. If I tried to catch him as he fell from that height, it would end with more than just a broken bone somewhere.

“Just leave him alone. Don’t get involved and hurt yourselves.”

The two men screamed.

“He’s falling! He’s falling!”

“He’ll die if you leave him like this!”

“He won’t die.”

If he could die from this, he would have died ten times over by now.

But Hyuk Mujin had a lifeline—a sturdy rope that always saved him at the very last moment.

“Aaaaaaah!”

Hyuk Mujin’s scream drew closer by the second. At last, even his horrified expression became clearly visible.

That was when a streak of light flashed above us.

The thing plunging downward at meteor-like speed was glowing with a soft purple light.

“W-what is that…?”

“What is it?”

I answered briefly.

“The Zaha Divine Technique.”

More precisely, it was someone channeling the Zaha Divine Technique.

The two men could not see him, but I could clearly make out Cheongpung, wrapped in the distinctive purple qi of the Zaha Divine Technique.

He was grinning from ear to ear.

“Whoooooa!”

“…”

Look at that bastard having the time of his life.

His personality might have been a little unhinged, but when it came to ability, he was in a league of his own. I could only marvel at what happened next.

*How is that even possible?*

Shot forward like an arrow, Cheongpung snatched Hyuk Mujin by the waist in the blink of an eye.

Then he extended his palm toward the ground rushing up beneath them.

*Bang! Boom-boom!*

Once. Twice. Three times…

With each explosion of compressed air, the ground caved in.

Would this be what happened if an invisible giant pounded the earth with its fists?

Every time Cheongpung struck out with a palm, the frozen ground flipped over. The resulting recoil stopped the falling figure in midair.

A moment later, Cheongpung’s feet landed lightly on the ground.

“Whew, that was fun again. Right?”

Hyuk Mujin, already unconscious, groaned.

“Uhh… uhhh.”

“I knew you’d like it.”

“…”

How exactly did it look like he was enjoying himself?

Cheongpung cheerfully set Hyuk Mujin down, then acknowledged my presence.

“Oh, Benefactor! You’re still here?”

“I fell, remember? Thanks to someone.”

I glared steadily at Cheongpung.

In fact, I had already had several chances to reach the summit. The problem was that Cheongpung was not exactly a man in possession of an ordinary state of mind.

“Hehe. It makes me happy that you say it was thanks to me.”

“Shut up! I would’ve reached the top ages ago if you hadn’t done anything but interfere from up there!”

“Gasp! Please calm down, Benefactor!”

“Calm down? You should have said that before rolling rocks down at me!”

Think about it.

Climbing a cliff more than a hundred jang high with your bare hands was no easy feat to begin with. But every time I thought I had made decent progress, rocks the size of children came tumbling down from above.

Cheongpung’s innocent cries were an added bonus.

*Benefactor, rocks are rolling!*

Only someone who had experienced it could understand. Even if Shakyamuni himself had been in my position, he would have strangled that bastard to death with his prayer beads.

*Now that I think about it, I’m getting pissed off again.*

Should I just go at him?

Just as I clenched my fist, Hyuk Mujin, who had been lying on the ground and twitching only his fingers, suddenly sprang upright with a scream.

“Aaaaaaaah!”

“Hey, hey. Breathe. Take a breath. You’re on the ground.”

“Huff, huff. Am I really alive?”

“Yeah, you idiot. You’re still alive.”

“W-water, please.”

Cheongpung held out the bamboo tube hanging from his waist.

“Here.”

“Thank you…”

Hyuk Mujin absentmindedly accepted the bamboo tube, then froze stiff.

A moment later, a roar burst from him.

“You fucking bastard!”

Cheongpung recoiled in alarm at the sight of Hyuk Mujin running wild with his eyes rolling back.

“W-why are you suddenly acting like this toward me?”

“You’re asking because you don’t know? Captain, catch that bastard!”

“I’m only doing exactly what my grandfather taught me.”

“Get over here right now!”

“See you up there later, Benefactor!”

Cheongpung hurriedly backed away from Hyuk Mujin, then kicked off the ground.

*Boom!*

He shot more than ten meters into the air in a single bound, slapped onto the cliff, and began climbing with the Wall Lizard Technique.

*Papapapapak!*

Now that was a true veteran.

Cheongpung vanished so quickly that he looked as though he had been born walking on all fours. Hyuk Mujin sank to the ground.

“That bastard threw rocks at me. Rocks…”

I answered solemnly.

“I know. I saw you fall earlier. One hit you right in the eye.”

“He’s completely insane. He throws rocks as big as a child’s head.”

“That’s smaller than what he threw at me. He even threw dirt at me.”

“Captain. I’ve made up my mind.”

“About what?”

“I won’t give up until I catch that bastard and beat the shit out of him. I swear it on the name of Hyuk Mujin, a true man.”

Hyuk Mujin’s eyes burned fiercely.

I had never seen him so fired up. No matter what he was like inside, on the surface he had always been cheerful and carefree.

*Could this have been what he was aiming for?*

Was all of this Cheongpung’s way of drawing out Hyuk Mujin’s anger so that he would give it his all?

No. That nature-loving Huashan guy did not have the brains for that.

*Well, as long as it works out.*

I threw a bundle at the huffing Hyuk Mujin.

“Keep it secure inside your clothes.”

“What is this?”

“Fasting pills. I packed them before we started training.”

There was nothing better for replenishing hunger and energy. They were small and light, making them easy to carry, too.

“Eat them if you start running out of strength on the way up.”

“We’re surrounded by cliffs. Where am I supposed to eat fasting pills? I’m going up there right now and cutting that bastard down in one stroke…”

“You’ll be the one who dies in one stroke.”

Apparently, he wanted his newly learned Wall Lizard Technique to take him straight to Mount Beimang. I smacked Hyuk Mujin on the back of the head.

“Ow!”

“And it’s not like the cliff is sheer all the way up. There are ledges here and there, so find a place to stop and eat. Don’t fall because you’re in a hurry. Take it slowly, thinking only about succeeding in one attempt.”

“Hoo.”

“Then let’s go.”

“Yes, Captain!”

Hyuk Mujin and I were standing before the cliff with determined expressions when—

“Um…”

“T-Third Young Master.”

Right. These two were here, too.

Jang Childeuk and the middle-aged guy hesitantly opened their mouths.

“Would it be all right if we reported this to the Lesser Family Head?”

“Considering the circumstances… If you suffer even an injury, Young Master, then we…”

I raised a hand to stop them.

I could easily guess what they were going to say next. I knew the perspective of ordinary employees better than anyone.

“Report it, but…”

“But?”

“After your shift ends. How much time is left?”

“About three shichen.”

“That’s enough.”

It had already been half a day since I started climbing the cliff.

I intended to conquer this maddening cliff within the remaining three shichen.

* * *

This tall, steep, nameless cliff had endured the passage of time. Some sections were uneven, while others were smooth.

In some places, thick roots or rocks jutted out, making them easy to grab. In others, I had to wedge a single finger into a tiny crack and hang on.

*It would be much easier if I could use internal energy or a weapon, at least.*

With internal energy, even solid rock would crumble like tofu.

If I took a weapon from my inventory, I could drive daggers into the cliff like steps and climb that way.

The reason I was going through all this trouble instead of taking the easy route was because this was training…

Well, that was part of it. But every time I tried to use an easier method, Cheongpung would somehow sense it and drop rocks on me.

*Thud-thud-thud.*

A sudden shower of rock dust from above was an ominous sign.

Hyuk Mujin and I hurriedly covered our heads with our arms and shouted.

“We didn’t do anything! Seriously, we didn’t do anything! Don’t roll any rocks!”

“Uuughhh!”

A pale face cautiously poked out from above.

“Really?”

We nodded frantically.

We had not even made it halfway. If we were hit by a stone shower and fell now, all the bold claims we had made before climbing would become a humiliating memory.

“Please believe us!”

“Young Hero Cheongpung! No, Great Hero Cheongpung!”

“My grandfather always said that there must never be any tricks in training. Martial arts are gained through blood and sweat.”

After delivering a full speech, Cheongpung added one more sentence as though he were showing us mercy.

“I’ll let it go just this once.”

“…”

“…”

He was acting like an absolute tyrant.

Suppressing our outrage, Hyuk Mujin and I started climbing the cliff again.

We were in a situation where even the slightest mistake would send us hurtling back down below.

As a result, our senses grew sharper, and we had to pay tremendous attention to every single finger and toe.

*If it weren’t winter, I would have reached the top long ago…*

The higher we climbed, the more treacherous the slope became and the smoother the surface grew.

The cliff was already slippery enough. On top of that, the scattered snow flurries that came almost every day and the wind blowing in from the northern Gaoyuan had turned it into one enormous sheet of ice.

*I’m blocked. I can’t see a path at all.*

As I bit down on my lip, something suddenly caught my eye.

A crack in the rock blocked by a snowball that had not yet frozen.

It was a tiny space, barely wide enough for one finger. It would be difficult, but I had no other choice.

*Hup!*

I launched myself forward with a shout, simultaneously jamming my smallest finger—the little finger—precisely into the crack.

*Thud.*

My prediction had been only half right. I could break through the unfrozen snowball, but the crack was much shallower than I had expected.

It was barely one finger joint deep. And I had to support a body weighing 0.1 tons with my little finger.

“Ungh.”

Even for me, this was a bit much.

To make matters worse, my finger was slowly slipping because of the moisture pooled inside the crack.

*If I waste any more time, I’ll fall.*

There was not much farther to go. I steadied my breathing and calmed the tension in my body. Using my little finger as a support, I lifted my entire body.

Physical ability worthy of being called superhuman.

> **System**
>
> - **Strength** increased by 1.
>
> - **Agility** increased by 1.
>
> - **Stamina** increased by 1.

The stat increase came at exactly the right moment.

Just as I smiled triumphantly and reached toward the next crack—

*Hup!*

“Captain!”

Damn it. My breathing had faltered at the worst possible moment. I steadied my breathing again, but Hyuk Mujin continued shouting.

“Th-this! This!”

“What are you saying? I can’t hear you!”

The fierce snowstorm scattered both sound and visibility.

I was about to open my mouth again when a clear shout struck my ears.

“Above! Above!”

“Above?”

The fact that I could hear Hyuk Mujin’s voice meant the savage wind had paused. Only then did my obstructed vision clear and my ears open.

Following Hyuk Mujin’s gesture, I raised my head and finally saw it.

A massive boulder falling straight toward my face.

*Whoooosh!*

“Ah, shit.”

*Boom!*

* * *

“Wow. I can’t believe you broke such a huge boulder with your bare fist.”

I let Cheongpung’s admiration go in one ear and collapsed onto my back.

Only a moment ago, I had wanted nothing more than to beat that bastard senseless. Now I was completely drained.

*I made it up. It’s over!*

Just as I lay there, unable to move even a hand and cheering inwardly, a bluish, frozen hand reached the summit.

“Huff. Haaah.”

“You succeeded in only one day! You’re both incredible!”

If it weren’t for you, I would have done it in one shichen, you idiot.

I wanted to lay into him, but I was too exhausted to speak. As Hyuk Mujin and I panted from a mixture of accomplishment and fatigue, Cheongpung bowed deeply at the waist.

“You’ve both worked so hard! Now that you’ve succeeded once, you should be able to climb the remaining nine times much faster.”

“…”

“…”

The statement was so shocking that Hyuk Mujin and I stared at Cheongpung without even remembering to breathe.

*What is he talking about?*

Could he possibly mean what I thought he meant?

No, surely not.

As an intellectual of modern society, I opened my mouth with a calm demeanor.

“The remaining nine times? What kind of bullshit is that?”

“My grandfather…”

This guy was either a mountain hermit or a boy detective.

At that moment, Sword Saint be damned—I couldn’t help but see red.

“So you’re telling us to do this nine more times?”

“Yes!”

“You’re going to keep throwing rocks at us from up here?”

“Yes!”

“No.”

“What?”

Hyuk Mujin and I simultaneously collapsed onto the ground.

“I’m not doing it. I don’t even have the strength to go back down. Go ahead and gut me.”

“Gut me too, you vicious bastard!”

“Puhahaha.”

“Are you laughing?”

Cheongpung smiled brightly.

“Sorry. You looked just like me when I first started training, so I couldn’t help it.”

“See? You didn’t want to do it either!”

“No. I thought it was fun and wanted to keep going, but my body wouldn’t keep up.”

Hyuk Mujin muttered in a voice so quiet that only I could hear.

“…Is he insane?”

“So I told my grandfather. I asked whether I could continue the next day because my legs wouldn’t listen to me.”

As he reminisced about his happy past, Cheongpung suddenly drew his sword.

At the same time, purple Sword Energy shot forth.

*Shhk.*

Ice, dirt, rock—Cheongpung cut through all of it without distinction, then continued speaking.

“My grandfather answered that climbing up was difficult, but going down was easy. He said that if I endured it for just a little while, I would be back down in no time.”

*Rumble, rumble, rumble.*

The edge of the cliff ledge where Hyuk Mujin and I were lying—barely ten square meters in size—began to shake.

*Is this for real?*

As we lay there in a daze, Cheongpung waved at us.

“Nine more to go.”

> **System**
>
> - The Quest **Sword Saint Training: A Secondhand Experience** has been generated.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 153`.

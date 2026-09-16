# Master Edit Task — Chapter 152

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

| 태원진가   | **Jin Family of Taiyuan**        |
| 하북팽가   | **Hebei Peng Family**            |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 마교     | **Demonic Cult**                                 |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 대주     | **Squad Leader** / **Commander**             |
| 선배     | **Senior**                                   |
| 일격     | **One Strike**                         |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |
| 홍가 | **Hong** | Unnamed middle-aged Jin Family martial artist who identifies himself by surname. |
| 진무량 | **Jin Muryang** | Founder of the Jin Family; legendary martial artist from roughly three hundred years earlier. |
| 천응 | **Heavenly Eagle** | Huge bird regarded as a spirit creature, said to have a wingspan exceeding one jang. |
| 혈교 | **Blood Cult** | Demonic organization named as a possible source of the intruder. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 홍가 | 장칠득 | older_martial_artist_to_junior_martial_artist | Little Brother Jang | familiar and casual | Hong calls Childeuk 장 아우 after inviting him to address Hong as hyung. |
| 장칠득 | 홍가 | junior_martial_artist_to_older_martial_artist | hyung | deferential, then familiar | Childeuk initially uses Senior and then adopts Hong's requested 형님 address. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

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

#### Chapter 150 tail (verified mastered)

…
He muttered sullenly, “Then you should’ve just said so from the start.” “Whew. Do you really want me to beat you to death today?” “Ah, I’ll pass. My head is still ringing.” Hyuk Mujin winced and shook his head. “But why did you suddenly try to open the Conception and Governor Vessels? You’re not a Peak internal-energy master, and you don’t have the guts to risk something like that.” “…I just tried it once.” “What?” “Forget it. You’re annoying, so shut up.” I waved dismissively at the wide-eyed Hyuk Mujin. It was too embarrassing to admit that watching Jin Mukyung and Cheongpung’s duel four days ago had made me want to become far stronger than I was now. “Anyway, just know that I failed spectacularly. I couldn’t do it properly because it hurt down there. Why is this happening?” “How would I know? I’m not a physician, or a Peak master like a certain someone.” Hyuk Mujin and I naturally turned our gazes to the side. The aforementioned “Peak master” blinked and opened his mouth. “Hmm. I’ve heard something about it from my grandfather.” Hyuk Mujin now knew Cheongpung’s identity too. We both exclaimed in anticipation. “Ohhh.” “Ooooooh.” Sword Saint Mae Jonghak was one of the greatest masters under heaven. When it came to martial arts, we would believe him even if he claimed he could make fermented soybean blocks out of red beans. “What did he say?” “He said that if I mishandled the Conception Vessel, I might not be able to perform as a man, and that the same was true of the Governor Vessel. What else did he say? Oh, right!” Cheongpung, who had been thinking hard, smacked his forehead. “He told me to leave them alone because they’d open on their own with time. He said I’d become a cripple if I mishandled both of them.” “…?” “…?” *What the hell is he talking about?* Hyuk Mujin and I exchanged glances almost simultaneously. “Do the Conception and Governor Vessels normally open with time?” “I don’t know. That’s the first I’ve heard of it, too.” “But it can’t be nonsense. The man’s the Sword Saint.” “Right. Maybe it takes a very long time?” “How long?” “How would I know? My father is almost sixty. Should I ask him?” “Oh, ask him whether his Conception and Governor Vessels have opened?” “Yes.” “Is he a martial artist?” “He owns the Hyuk Family Textile Shop.” “Try not to speak unless you have to. Listening to you is infuriating.” “Yes.” I pitied myself for taking someone like this around as my subordinate. I heaved a deep sigh and spoke to Cheongpung. “Could you explain in a little more detail? Surely your grandfather didn’t say only that…” “He said exactly that.” “…Really? Word for word?” “I don’t lie to my Benefactor.” That was true. Cheongpung wasn’t sly enough to lie. Whether it was his nature or the environment in which he’d grown up, he was so honest and guileless that, to put it unkindly, he seemed stupid. Cheongpung added with an aggrieved expression, “And my grandfather isn’t a liar either. I waited, too, and mine opened. Not both of them—only the Governor Vessel.” “I’m not saying the Sword Saint lied… Wait. What did you just say?” “Young Hero Cheongpung, what was that? You opened the Conception and Governor Vessels?” “Oh, only the Governor Vessel for now. Maybe it’s because I’m still young.” I stammered, “H-How did you open it?” “Two years ago, I was just training when I suddenly felt strange, and then—bang!” “Bang?” “That’s how it opened.” “…” “…” “I thought it was strange, so I asked my grandfather. He said it was enlightenment. Hehe.” This was hopeless. We were far too different. The Sword Saint had been right that the Conception and Governor Vessels would open naturally with time. The problem was that it only applied to Cheongpung. The guy smiling innocently in front of me was practically a new breed of human, fundamentally different from someone like me. *Genius. Talent bestowed by heaven. That’s what this is.* Cheongpung and Jin Mukyung had both been born with talent entirely unlike mine. There was nothing I could do about that. When I remained silent for a while, Cheongpung cautiously watched my expression. “Benefactor, did I do something wrong?” “No. You didn’t do anything wrong.” “Really? That’s a relief.” Watching Cheongpung sigh with relief, I licked my dry lips. “But, um…” “Yes?” “Could I ask you for a favor?” “Anything.” Damn it. Now that I had to say it, the words wouldn’t come out. I had thick skin. I’d been called brazen and shameless before. But why was this one sentence so difficult? “Benefactor?” With great difficulty—truly, great difficulty—I forced out the words. “Could you help me with my training?” “Of course. Certainly.” “What?” “I’ll help you. With your training.” The moment I looked into his clear eyes, I finally understood why I had hesitated. It was competitive pride. Competitive pride that made me unwilling to accept help from this guy, of all people. Not because I disliked him, but because he was an opponent I wanted to defeat solely through my own strength. I wanted to stand on equal footing with him. But to do that… “Then I’ll be counting on you.” I had to learn. What else could I do? Turns out I had a thicker hide than I thought.

#### Chapter 151 tail (verified mastered)

…
talking nonsense.” “That was just something I said. If I disliked you, would I have kept you around all this time?” “Wasn’t it because you were bored? Sometimes you seemed to enjoy hitting me when your hands got restless.” “…” Just how much of a piece of trash did this bastard think I was? When I glared at him, Hyuk Mujin hurriedly pretended nothing had happened. “Ahem. Ahem, ahem…” “Listen, if I hadn’t planned to raise you up, I would have gone around alone a long time ago. Why would I lug around deadweight like you?” “Deadweight? Can you really change your story that easily? A moment ago, I was your right arm or your heart.” “Right arm, my ass. At your current level, I’ll let you be my little toe.” “Wow. That’s harsh. Really.” He sounded hurt, but he couldn’t hide the corners of his mouth, which kept rising. Right arm or little toe, they were both important parts of the body. That fact didn’t change. Feeling strangely embarrassed, I shouted, “Enough! Are you doing this or not?” “I’m actually a martial arts genius, you know. I might copy everything you do. Are you sure that’s okay?” “Bullshit. Copy it if you can.” “Really?” “Ask one more time and I’ll hit you so it really hurts.” Hyuk Mujin broke into a broad smile. “I’ll do it.” His voice sounded lighter, as though he had shed an old skin. * * * Hyuk Mujin and I sat on the floor of the training ground and looked at Cheongpung. Taking a seat was the basic requirement before the real lecture began. “All right. Let’s begin.” “I look forward to learning from you, Young Hero Cheongpung.” “Yes, yes! Hoo, hoo…” Every time Cheongpung took a heavy breath, white steam puffed from his nose into the cold winter air. What was wrong with him all of a sudden? “Are you all right?” “I’m fine!” “You startled me. Why are you suddenly acting like this?” “Oh. Um, well…” Cheongpung hesitated, then spoke with a face flushed bright red. “This is my first time teaching anyone, so I’m too excited and worked up... Whew, give me a moment.” “…” “…” I knew this would happen. Perhaps he was still nervous, because Cheongpung spoke in a trembling voice. “Th-then I’ll begin.” “Don’t make it so stiff. Just relax.” “R-relax?” “Yes. Relax. Just teach us in whatever way you’re comfortable with, Young Hero Cheongpung.” “The way I’m most comfortable…” “The way your grandfather taught you.” “Oh. What an easy solution!” Hyuk Mujin and I looked at Cheongpung with a mixture of anticipation and curiosity. This was the teaching method of the Sword Saint himself. How had that great martial artist raised this genius? *It must be something completely different.* As Cheongpung sank into thought, a smile appeared on his lips. Apparently, merely thinking about the method put him in a good mood. “Oh, I thought of something. This training will probably help both of you a great deal, too.” “Ohhh.” “Ooooooh. What is it?” “Do you see that?” We turned in the direction Cheongpung was pointing. Hyuk Mujin spoke first, and I finished the thought. “That’s…” “The training hall.” It stood roughly two hundred jang from the training ground. I had a pretty good idea what kind of training he meant, and a quiet laugh escaped me. It was the classic touch-and-go method: repeatedly running like hell to touch the destination and come back. *I expected something special from the Sword Saint, but I guess he wasn’t that different.* It was certainly a classic, but it was an effective exercise for building endurance and strengthening the lower body. I stood and began stretching leisurely. “Do we just go there and come back?” Cheongpung tilted his head. “Huh? You’ve done this before?” “Until I was sick of it.” “Oh, I see. That’s a relief.” Cheongpung smiled brightly and pointed to me, then Hyuk Mujin. “Then I’ll give you half a shichen and one shichen, respectively.” “…?” “…?” “What?” I asked in confusion. “Half a shichen? What do you mean?” “Didn’t you say you’d done it until you were sick of it? That should be plenty of time for you.” “That’s true, but... Ah, I get it. Do we have to make nonstop round trips for half a shichen?” “No. Once will be enough for now. I’ll wait for you at the summit.” “What? The summit?” “Yes. There.” This time, I saw it clearly. Cheongpung’s raised fingertip was pointing at the cliff behind the training hall. Hyuk Mujin and I dropped our jaws at the same time. *Holy shit. What the hell is that?* The height was impossibly vast. Even judging by eye, it was a steep cliff hundreds of jang high. My vision went dark, and my hands and feet began to tremble. If it affected me this badly, Hyuk Mujin had to be even worse. “Are you saying… we have to climb that?” “Yes! I picked it because it’s about the same height as the place I climbed every day when I was little.” “…” “…” “Ah, that brings back memories. I fell halfway down and nearly died twice. It really hurt back then.” “…!” “…!” He was insane. The Sword Saint was insane, and this bastard was insane too. [^1]: Candied hawthorn skewers are a traditional snack made by coating fruit on skewers in hardened sugar.

## Korean source

```text
＃152화



“흐아아아암.”

늘어져라 하품을 한 중년 무인이 옆을 흘끗 바라봤다.

몇 걸음 떨어지지 않은 곳에 오늘 새로 발령받은 신참이 뻣뻣한 자세로 정면을 주시하는 중이었다.

‘그놈 참. 떡대 하나는 끝내주네.’

절굿공이 같은 팔다리 하며, 딱 벌어진 어깨 하며.

덩치만 보면 근골 좋기로 유명한 하북팽가(河北彭家) 출신은 아닌지 의심이 들 정도였다.

‘그러고 보니 아직 이름도 모르는군.’

날은 춥고, 근무 시간은 앞으로 세 시진도 더 남았다.

이런 날에는 주둥이라도 털어야 시간도 금방 가고 몸도 따뜻해지는 법. 중년 무인이 슬그머니 입을 열었다.

“여보게.”

“예, 옛!”

“어허, 벽력탄을 삶아 먹었나. 왜 이리 목청이 커?”

“죄송합니다!”

“그렇다고 사과할 것까진 없고. 신입이라 그런가? 패기 넘치는 모습이 보기 좋구먼.”

“헛, 감사합니다.”

“응. 그려, 그려.”

중년 무인은 흐뭇하게 웃었다. 몇 마디 안 나눠 봤지만 괜찮은 놈 같다. 행동거지가 우직하고, 요즘 젊은것들답지 않게 예의도 바르다.

슬슬 뒷방 늙은이 취급받는 처지인 그로서는 꽤 괜찮은 말동무가 생긴 셈이었다.

“혹시 자네 성이 팽가인가?”

“아닙니다. 장가입니다.”

“혹시나 해서 물어봤네. 자네 근골이 좀 좋아야지. 난 또 하북팽가의 먼 방계라도 되나 싶었지 뭔가.”

신참 무인이 뒤통수를 긁적였다.

“제가 코흘리개 때부터 힘깨나 쓰긴 했지요.”

“어쩐지. 팔다리에 아주 근육이 옹골차네그려. 내 젊을 때를 보는 것 같아.”

물론 턱도 없는 소리다. 하지만 생긴 것답지 않게 제법 눈치가 있는 신참 무인은 넙죽 허리를 숙였다.

“선배님께서 젊으셨을 적에 비하면 저는 아무것도 아닙니다.”

“어허. 선배가 뭔가, 앞으로는 형님이라고 부르게. 아, 나는 홍가일세.”

“예, 형님!”

“허허. 좋은 아우가 생겼구먼. 그래, 우리 장 아우는 본가에 언제 입문(入門)했는가?”

“벌써 수년 되었습니다.”

“으잉? 그럴 리가, 아우 같은 장군감이 들어왔으면 내가 진작 알았을 터인데…….”

어언 이십 년을 태원진가에 몸담은 그다. 나름 터줏대감이라 무인 중 누가 들어오는지, 누가 나가는지는 정확히 알았다.

“아, 무인이 된 건 한 달도 안 됐습니다. 그전에는 하인으로 잡일이나 이것저것 했었죠. 눈에 잘 안 띄는 곳이라 모르셨을 수도 있습니다.”

“아아, 그랬구먼.”

중년 무인은 새삼스러운 눈빛으로 신참을 바라봤다.

하인에서 무인이라. 아주 없는 일은 아니지만 그렇다고 흔한 일도 아니다.

“뒷배가 좋나 보군.”

“예?”

“예끼, 알 만한 사람이 시치미 떼기는. 신참이 이 자리에 들어오는 게 쉬운 일인 줄 알아?”

중년 무인이 씩 웃으며 신참의 옆구리를 쿡쿡 찔렀다.

“누군가? 내총관이야 워낙 깐깐한 위인이니 아닐 테고, 수뇌부에 튼튼한 줄이라도 하나 잡았나?”

“저, 그게…….”

“나만 알고 있을 테니 살짝 말해 보게. 외당주인가? 아니면 철검대주?”

아뇨, 소가주님께서 보내셨는데요.

신참 무인, 장칠득은 튀어나오려던 말을 꿀꺽 삼켰다.

사람의 입이 얼마나 가벼운가, 곧이곧대로 말했다가는 내일 해가 뜨기 전에 소문이 퍼질 것이 뻔했다.

‘소가주님께 누를 끼칠 수는 없다!’

태원진가에 대한 충성심 하나만큼은 여느 열사(烈士) 못지않은 칠득이다.

그는 궁금함이 잔뜩 담겨 있는 중년 무인의 눈빛을 외면하며 입을 열었다.

“그런데 여기가 그렇게 들어오기 힘든 곳이었습니까?”

칠득의 화제 전환에 중년 무인이 실망한 표정으로 입맛을 다셨다. 굳이 말하기 싫다는데 더 찔러 보기도 뭐하다.

“쩝. 자네, 본가에 몇 년 동안 있었다고 했지?”

“그렇죠. 하인이었지만.”

“그럼 그 몇 년간 수련동에 몇 번이나 와 봤나?”

“딱 두 번 와 봤습니다.”

“그렇지? 자, 그 자리에서 한 바퀴 쓱 둘러보게.”

“지금요?”

“그럼 내년에 할래?”

장칠득은 시키는 대로 주위를 둘러봤다. 태원진가의 뒤를 빈틈없이 감싼 가파른 절벽 아래, 뻥 뚫려 있는 동공(洞空).

그곳이 수련동의 입구였고, 그와 중년 무인 외에는 아무도 없었다.

“어떤가?”

“휑하네요.”

“그렇지? 여기 하루에 몇 명이나 올 것 같나?”

“몇 명이나 옵니까?”

중년 무인이 심드렁하게 대답했다.

“안 와.”

“예?”

“네 시진마다 교대하러 오는 인원 제외하면 아무도 안 온다고. 아, 식사 전해 주는 하인도 있었군.”

“하지만…… 수련동이잖습니까?”

“수련동이지. 그런데 여기서 수련하는 사람? 없어. 예전에 삼공자가 사고 치고 몇 번 들락거리긴 했지만.”

이 무슨 황당무계한 말인가. 그러고 보니 말만 수련동이지, 막상 이곳에서 수련했다는 사람은 못 본 것 같다.

반면 연무장은 사시사철 무인들로 득실거렸다.

“그럼 여길 왜 지키는 겁니까?”

“상징이지.”

“상징이요?”

“먼 옛날, 본가를 세우신 진무량 조사(祖師)께서 수련하시던 곳이거든. 전해지기로는 이 절벽에서 수련하시던 도중 문득 깨달음을 얻어 무공을 펼쳤는데, 일격에 절벽 밑이 뻥 뚫렸다는군.”

장칠득은 입을 딱 벌렸다.

진무량 조사에 대한 전설은 그도 들어 본 기억이 있다. 삼백 년 전에는 천하에서 손꼽히는 고수였다던가?

하지만 어찌 인간의 몸으로 그것이 가능하단 말인가.

“그, 그게 사실입니까?”

“자그마치 수백 년 전의 일일세. 사실이면 어떻고, 거짓이면 어떤가? 정작 중요한 사실은 따로 있는 것을.”

“……예?”

“이 수련동 앞에서 하루 몇 시진만 죽치고 앉아 있으면 월봉이 따박따박 나온다는 것. 그게 중요한 걸세. 시간이 더럽게 안 가는 게 흠이긴 하지만.”

씩 웃은 중년 무인이 장칠득의 어깨를 두드렸다.

“축하하네. 자네는 본가의 무인들이 꿈꾸는 최고의 보직에 임명된 걸세. 일명 꿀보직이라고 하지.”

“…….”

장칠득의 얼굴이 일그러졌다. 곧 은퇴해도 이상하지 않을 나이라면 모를까, 지금처럼 한창때에 할 일 없이 수련동에서 시간이나 죽이고 있을 생각은 없다.

그의 생각을 알 리 없는 중년 무인은 품에서 육포 하나를 꺼내어 씹었다.

“자네도 하나 줘?”

“전 괜찮습니다.”

“왜? 짭조름하니 괜찮은데. 육포 씹으면서 하늘 보면 시간도 금방 가고 좋아.”

수련동 입구에 비스듬히 기댄 중년 무인이 고개를 꺾어 하늘을 바라봤다.

“아따, 하늘 한번 맑다. 보고만 있어도 가슴이 탁 트이네.”

장칠득도 마지못해 위를 흘끗 바라봤다.

중년 무인의 말처럼 날씨는 맑았다. 푸른 하늘 위, 천천히 흘러가는 조각구름과 검은 점 몇 개가 떠다녔다.

“저건 뭡니까?”

“새겠지, 뭐.”

멍하니 하늘을 바라보던 장칠득의 시선이 까마득한 높이의 절벽을 향했다. 문득 그의 눈이 가늘어졌다.

“절벽에 붙어 있는 저건요?”

“절벽? 절벽에 뭐가 있나?”

“예. 꽤 큰데요?”

“몰러. 꽤 큰 새인가 보지. 가만있자, 술을 한 병 가져왔는데…….”

중년 무인은 칠득이 가리키는 곳을 쳐다보지도 않고 품에서 조그마한 자기 병 하나를 꺼내 들었다.

“새치고는 좀 너무 큰 것 같은데요.”

“천응(天鷹)이라는 놈일 수도 있지. 그놈들은 덩치가 사람만 하거든. 보통 매가 아니여.”

“허어, 진짜 사람만 하네요.”

“영물 소리도 듣는 놈이니까. 날개 길이만 일장이 넘는다고 하던데, 나도 멀리서 딱 한 번 봤네.”

“그런데 형님.”

“아, 왜 자꾸 부르나?”

“천응도 떨어집니까?”

“그게 뭔 개소리여?”

술병을 기울이던 중년 무인이 황급히 절벽을 쳐다봤다. 까마득한 높이, 거대한 점이 빠르게 추락하고 있었다.

“으아아아아악!”

장칠득이 감탄했다.

“영물은 영물이네요. 비명이 꼭 사람 같습니다.”

“저거 사람이야, 이 미친놈아!”

“뜨아아!”

“피해, 피해!”

중년 무인이 비명을 내지른 다음 순간, 비처럼 쏟아지는 돌조각과 함께 한 사람이 지면에 추락했다.

쾅! 후두두둑!

돌과 먼지가 사방으로 비산했다. 두 사람이 동시에 침을 꼴깍 삼켰다.

“주, 죽은 걸까요?”

“저 높이에서 떨어져 봐. 옥황상제도 죽는다.”

평온하던 일상에 이 무슨 참담한 사태란 말인가.

중년 무인은 떨리는 가슴을 부여잡고 엎어진 시신을 바라봤다.

“도대체 어떤 미친놈이 절벽에서…….”

“젊은 놈 같은데요?”

“지금 젊은 놈이건 늙은 놈이건 그게 중요한가? 죽었다는 게 중요하지.”

“그건 그렇지만…….”

“가서 한 번 뒤집어 보게.”

“제, 제가 말입니까?”

“여기 자네랑 나 말고 누가 있나? 어서!”

중년 무인의 호통에 장칠득이 머뭇거리며 시신을 향해 다가가기 시작했다.

무인이 된 지 고작 한 달. 눈앞에서 사람의 죽음을 목도한 것은 이번이 처음이다.

“후욱, 후욱.”

가까워질수록 시신의 모습이 명확하게 보이기 시작한다.

축 늘어진 사지, 엎어진 뒤통수에서는 핏물이 줄줄 흘러내렸다. 저 높이에서 떨어진 것치고는 곱게 죽은 모습.

“그, 극락왕생하시오.”

눈을 질끈 감고 시신의 몸에 손을 댄 그 순간이었다.

벌떡, 빡!

눈앞이 번쩍하더니 격통이 밀려들었다.

그대로 엉덩방아를 찧은 장칠득은 자신이 쌍코피를 흘리는 것도 모르고 입을 딱 벌렸다.

“어어, 어어어.”

“갑자기 뭔…… 으어어, 으어어어!”

중년 무인도 다리에 힘이 풀려 털썩 쓰러졌다.

“시체가, 시체가 살아 있다!

“으어어, 강시다! 강시가 나타났다!”

시체, 강시.

졸지에 죽은 놈이 되어 버린 흙투성이의 괴인이 비틀거리며 일어났다.

산발이 된 머리, 실핏줄이 터진 눈동자로 주위를 둘러보던 그가 빠드득, 이를 갈았다.

“씨벌, 또 태초 마을이야?”



* * *



더럽게 아프네.

머리, 어깨, 무릎, 발, 무릎, 발…… 안 쑤시는 곳이 없다. 그나마 절벽에 단검을 박아서 추락 속도를 늦춰 망정이지, 하마터면 골로 갈 뻔했다.

물론 꾸준하게 올려놓은 근골, 맷집 스탯도 한몫했고.

“어우, 뒷골 땡겨.”

따끔한 뒤통수를 만져 보니 핏물이 축축하게 묻어 나온다.

소매를 북 찢어 피를 닦아 내던 그때였다.

“누, 누구냐!”

“정체, 정체를 밝혀라, 이노옴!”

아, 이 아저씨들도 있었지.

대뜸 칼을 들이대는 두 사람 중 한 명의 얼굴이 낯이 익다. 그러니까 이름이…….

“장칠득?”

며칠 전까지만 해도 홍화객잔에서 여론 조작에 힘쓰시던 장칠득 씨가 기겁하며 물러났다.

“허억! 어떻게 내 이름을?!”

“강시가 말을 한다! 말로 사람을 홀린다!”

“……누가 강시야. 숨 잘만 쉬고 있는 거 안 보여요?”

수염이 듬성듬성한 중년 아재가 눈을 부릅뜨며 외쳤다.

“이 사악한 것! 내 눈을 속일 수는 없다. 네가 사람이라면 저 높이에서 떨어지고도 멀쩡할 리 없을 터, 어디서 보냈느냐! 마교(魔敎)? 혈교(血敎)? 그것도 아니면…….”

“태초 마을! 형님, 저 강시가 분명 태초 마을이라고 했습니다.”

“그렇지! 태초 마을에서 보낸 강시구나!”

감 잡았다는 듯이 버럭 소리친 중년인이 순간 멈칫하더니 장칠득에게 물었다.

“그런데 태초 마을이 어디야?”

“저도 모르죠.”

“…….”

알면 이상하지.

나는 대화를 포기하고 흙투성이가 된 얼굴을 옷소매로 문질렀다.

중년인은 몰라도 장칠득은 내 얼굴을 잘 아니까 이게 더 빠르겠지.

“헉, 삼공자님!”

“네, 오랜만이에요.”

“아우, 삼공자님이라니. 그게 대체 무슨 소린가?”

“삼공자님이 강시가 됐습니다!”

“…….”

결론이 왜 그따위냐.
```

## Current accepted English baseline

```markdown
# Chapter 152

“Yaaawn.”

A middle-aged martial artist glanced to the side after letting out a long yawn.

Only a few paces away, the new recruit who had been assigned here today was standing stiffly and staring straight ahead.

*What a guy. He’s got one hell of a build.*

Limbs like pestles. Shoulders spread wide.

Judging by his size alone, one might have suspected he came from the Hebei Peng Family, famous for producing martial artists with strong bones and muscles.

*Come to think of it, I don’t even know his name yet.*

The weather was cold, and there were still more than three shichen left in his shift.

On days like this, chatting was the best way to make time pass faster and keep warm. The middle-aged martial artist slowly opened his mouth.

“Hey there.”

“Yes, sir!”

“Good heavens, did you swallow a thunderbolt? Why are you shouting so loudly?”

“I’m sorry!”

“You don’t have to apologize for that. Is it because you’re new? It’s nice to see someone so full of spirit.”

“Ah, thank you.”

“Yeah, yeah. That’s right.”

The middle-aged martial artist smiled, pleased. They had only exchanged a few words, but the kid seemed decent. His manner was straightforward, and unlike young people these days, he was polite too.

For a man who was slowly being treated like an old-timer fit only for the back rooms, he had found himself a pretty good conversational partner.

“Is your surname perhaps Peng?”

“No. It’s Jang.”

“I only asked because I was curious. Your physique is quite impressive. I wondered whether you might be from some distant collateral branch of the Hebei Peng Family.”

The new martial artist scratched the back of his head.

“I was pretty strong even when I was a little kid.”

“I thought so. Your limbs are packed with muscle. You remind me of myself when I was young.”

Of course, that was utter nonsense. But despite his appearance, the new martial artist was perceptive enough to immediately bow deeply.

“Compared to what you were like in your youth, Senior, I’m nothing.”

“Hey, none of this ‘Senior’ business. Call me hyung from now on. Ah, I’m Hong.”

“Yes, hyung!”

“Heh heh. Looks like I’ve got myself a good little brother. So, Jang, when did you join this family?”

“It’s already been several years.”

“Huh? That can’t be right. If a fine candidate for a general like you had joined, I would have heard about it long ago…”

He had been with the Jin Family of Taiyuan for nearly twenty years. He considered himself something of an old hand and knew exactly which martial artists came and went.

“Ah, I haven’t even been a martial artist for a month. Before that, I was a servant who handled odd jobs here and there. I worked in places where I didn’t stand out much, so you might not have noticed me.”

“Ahh, I see.”

The middle-aged martial artist looked at the new recruit with fresh interest.

A servant who became a martial artist. It wasn’t unheard of, but it wasn’t common either.

“You must have a powerful backer.”

“Pardon?”

“Oh, come on. Don’t play dumb. Do you think it’s easy for a new recruit to get assigned to this position?”

The middle-aged martial artist grinned and poked the new recruit in the side.

“Who is it? The Chief Steward is far too strict to be behind it, so did you manage to secure a solid connection somewhere in the leadership?”

“Well, I…”

“Just tell me quietly. I’ll keep it to myself. Is it the Outer Hall Master? Or the Iron Sword Squad Leader?”

*The Lesser Family Head sent me here.*

The new martial artist, Jang Childeuk, swallowed the words that had nearly slipped out.

People’s tongues were terribly light. If he told the truth, the rumor would spread before the sun rose tomorrow.

*I can’t cause trouble for the Lesser Family Head!*

When it came to loyalty toward the Jin Family of Taiyuan, Childeuk was no less devoted than any martyr.

He avoided the middle-aged martial artist’s intensely curious gaze and opened his mouth.

“By the way, was this really such a difficult place to get into?”

The middle-aged martial artist looked disappointed at the change of subject and clicked his tongue. Since Childeuk clearly didn’t want to talk about it, there was no point in pressing him further.

“Tsk. You said you’d been with the family for several years, right?”

“That’s right. Although I was a servant.”

“Then how many times did you come to the training hall during those years?”

“Exactly twice.”

“Right? Now, take a good look around.”

“Right now?”

“Or would you rather do it next year?”

Jang Childeuk looked around as instructed.

Beneath the steep cliffs that enclosed the rear of the Jin Family without a single gap, there was a wide-open cavern.

That was the entrance to the training hall, and other than Childeuk and the middle-aged martial artist, there was no one there.

“What do you think?”

“It’s deserted.”

“Right? How many people do you think come here in a day?”

“How many?”

The middle-aged martial artist answered indifferently.

“No one.”

“Pardon?”

“Other than the people who come to change shifts every four shichen, nobody comes here. Ah, there is a servant who delivers meals.”

“But… this is the training hall, isn’t it?”

“It is. But does anyone train here? No. The Third Young Master came in and out a few times after causing trouble, but that’s about it.”

What an absurd thing to say.

Come to think of it, it was called a training hall, but Childeuk had never seen anyone actually training there.

The training ground, on the other hand, was always crawling with martial artists, no matter the season.

“Then why are we guarding this place?”

“It’s a symbol.”

“A symbol?”

“Long ago, Founder Jin Muryang trained here. According to the story, he suddenly attained enlightenment while training on this cliff and unleashed his martial arts, blasting open the base of the cliff with One Strike.”

Jang Childeuk’s mouth fell open.

He remembered hearing the legend of Founder Jin Muryang. Hadn’t he been one of the most renowned masters in the world three hundred years ago?

But how could such a thing be possible with a human body?

“Is, is that really true?”

“It happened hundreds of years ago. What does it matter whether it’s true or false? There’s another fact that’s actually important.”

“…Yes?”

“If you sit around in front of this training hall for a few shichen a day, your monthly pay comes like clockwork. That’s what matters. The only downside is that time passes unbelievably slowly.”

The middle-aged martial artist grinned and patted Childeuk on the shoulder.

“Congratulations. You’ve been assigned to the finest post the martial artists of this family dream of. They call it a cushy post.”

“…”

Childeuk’s face twisted.

It would be one thing if he were old enough to retire at any moment, but he was still in his prime. He had no intention of wasting his time in the training hall with nothing to do.

The middle-aged martial artist, unaware of his thoughts, pulled out a strip of dried meat and began chewing.

“Want one?”

“I’m fine.”

“Why? It’s salty and pretty good. Looking at the sky while chewing jerky makes time pass quickly.”

The middle-aged martial artist leaned against the entrance to the training hall and tilted his head back to look at the sky.

“Well, would you look at that. The sky is so clear. Just looking at it makes my chest feel wide open.”

Jang Childeuk reluctantly glanced upward.

Just as the middle-aged martial artist had said, the weather was clear. A few wispy clouds drifted slowly across the blue sky, along with several black specks.

“What are those?”

“Birds, probably.”

Childeuk’s gaze, which had been fixed blankly on the sky, shifted toward the cliff towering into the heavens. His eyes narrowed.

“What about that thing clinging to the cliff?”

“The cliff? What’s on the cliff?”

“Yes. It’s pretty big.”

“Dunno. Must be a pretty big bird. Hold on, I brought a bottle of liquor somewhere…”

Without even looking toward the place Childeuk was pointing, the middle-aged martial artist pulled a small porcelain bottle from his robes.

“It seems too big for a bird.”

“It could be a Heavenly Eagle. Those things are as big as people. They aren’t ordinary hawks.”

“Wow. It really is as big as a person.”

“They’re even called spirit creatures. I heard their wingspan alone is more than a jang. I’ve only seen one from a distance, myself.”

“But, hyung.”

“What? Why do you keep calling me?”

“Do Heavenly Eagles fall, too?”

“What the hell are you talking about?”

The middle-aged martial artist, who had been tilting the bottle toward his mouth, hurriedly looked at the cliff.

At that dizzying height, a massive dot was plummeting rapidly.

“Aaaaaaah!”

Childeuk sounded impressed.

“It really is a spirit creature. Its scream sounds exactly like a person.”

“That’s a person, you lunatic!”

“Whaaa!”

“Move! Move!”

The instant the middle-aged martial artist screamed, a person crashed into the ground amid a shower of stones.

*Boom! Rumble, rumble!*

Rocks and dust burst in every direction. The two men swallowed at the same time.

“D-do you think he’s dead?”

“Try falling from that height. Even the Jade Emperor would die.”

What a calamity to interrupt their peaceful daily routine.

The middle-aged martial artist clutched his trembling chest and stared at the body lying facedown.

“What kind of madman falls from a cliff…”

“He looks young.”

“Does it matter whether he’s young or old? The important thing is that he’s dead.”

“That’s true, but…”

“Go turn him over.”

“M-me?”

“Who else is here besides you and me? Hurry!”

At the middle-aged martial artist’s shout, Jang Childeuk hesitantly began approaching the body.

He had only been a martial artist for a month. This was the first time he had ever witnessed someone die right in front of him.

“Huff, huff.”

The closer he got, the more clearly he could see the body.

Its limbs lay limp, and blood streamed from the back of its head as it lay facedown on the ground. Considering the height of the fall, the corpse looked surprisingly intact.

“May you be reborn in paradise.”

He squeezed his eyes shut and reached out to touch the body.

That was when—

The body sprang upright.

*Crack!*

The world flashed before Childeuk’s eyes, followed by a wave of blinding pain.

He landed hard on his backside, mouth hanging open, unaware that blood was pouring from both nostrils.

“Uh… uhhhh.”

“What the hell just… ugh, ughhh!”

The middle-aged martial artist’s legs gave out, and he collapsed.

“The corpse—the corpse is alive!”

“Ugh! It’s a jiangshi! A jiangshi[^1] has appeared!”

The dirt-covered stranger who had suddenly been written off as dead staggered to his feet.

He looked around with his hair in disarray and blood vessels burst in his eyes, then ground his teeth.

“Fuck, Taecho Village[^2] again?”

* * *

Damn, that hurts.

My head, shoulders, knees, feet, knees, feet… There wasn’t a single place that didn’t ache. Luckily, I had slowed my fall by driving a dagger into the cliff. Otherwise, I might have ended up dead.

Of course, the physique and toughness stats I had steadily raised had helped, too.

“Ow, the back of my head is throbbing.”

When I touched the tender spot on the back of my head, blood came away damply on my fingers.

I tore off a strip of my sleeve and was wiping away the blood when—

“Who are you?!”

“Reveal your identity, you scoundrel!”

Oh, right. Those two older guys were here, too.

One of the two men pointing swords at me looked familiar. What was his name again…

“Jang Childeuk?”

Mr. Jang Childeuk, who had been working hard to manipulate public opinion at Honghwa Inn until just a few days ago, recoiled in terror.

“Gasp! How do you know my name?!”

“The jiangshi is talking! It’s bewitching people with its words!”

“…Who are you calling a jiangshi? Can’t you see I’m breathing just fine?”

The middle-aged man with the patchy beard glared at me and shouted.

“You evil creature! You can’t fool my eyes. If you were human, you couldn’t possibly be fine after falling from that height. Who sent you? The Demonic Cult? The Blood Cult? Or perhaps…”

“Taecho Village! Hyung, that jiangshi definitely said ‘Taecho Village.’”

“That’s right! You’re a jiangshi sent by Taecho Village!”

The middle-aged man shouted as if he had finally figured it out, then suddenly stopped and asked Childeuk,

“But where is Taecho Village?”

“I don’t know either.”

“…”

It would have been strange if he did.

I gave up on the conversation and wiped the dirt from my face with my sleeve.

The middle-aged man might not know me, but Childeuk knew my face well. This would be faster.

“Gasp! Third Young Master!”

“Yes. Long time no see.”

“Little brother, the Third Young Master? What in the world are you talking about?”

“The Third Young Master has become a jiangshi!”

“…”

Why was that the conclusion?

[^1]: A jiangshi is a reanimated corpse from Chinese folklore, often depicted as a hopping vampire.

[^2]: *Taecho* means “primordial” or “the beginning.”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 152`.

# Master Edit Task — Chapter 124

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
| 이소월    | **Lee Seowol**     |
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 일신     | **One God**         |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 열화문    | **Fire Gate Clan**               |
| 남궁세가   | **Nangong Family**               |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 검법     | **sword technique**                              |                                                       |
| 권법     | **fist technique**                               |                                                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 낭인     | **wandering martial artist**                     |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 지부장    | **Branch Leader**                            |
| 진가창법   | **Jin Family's Spear Technique**       |
| 상태               | **Status**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 습득               | **Acquired**                   |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 안휘     | **Anhui**              |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 본가      | **our family / this family**                                    |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |

## Matched risk notes

(No matching risk notes.)

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 115–119

## Plot

Jin Taekyung and Jin Mukyung enter the Mount Heng fortress after finding Cheol Mubaek critically wounded by Pung Yang’s Temporary Strength Pill. Wolhwa and Hyuk Mujin remain behind to protect Cheol while the Jin brothers attack the Red Wind Band. Although Mukyung initially dominates, Pung Yang consumes another pill, gains enough power to produce imperfect Sword Force and Body-Protecting Qi, and reverses the fight. He reveals that he obtained the Crimson Blood Twelve Swords, the Crimson Blood Cultivation Technique, and five Temporary Strength Pills from a hidden plateau tomb, killing his companions to keep the legacy.

Mukyung appears to break Pung Yang’s defensive qi, but concealed throwing knives leave him unconscious. Taekyung consumes Jopil’s Blazing Flame Divine Pill, gaining thirty years of Scorching Yang Qi and temporarily raising his internal energy to forty-five years. He outmaneuvers Pung Yang and wounds him with a dagger before his Body-Protecting Qi fully forms, but the divine pill’s energy runs wild and severely damages Taekyung. As Pung Yang’s Temporary Strength Pill begins to wear off, Lee Seowol and nine surviving Mount Heng martial artists make a last stand so Taekyung can escape with Mukyung.

Taekyung refuses to flee and attacks with One Annihilation, but Pung Yang destroys it, severely injures him, and captures him. When Pung Yang attempts to mutilate him, Taekyung summons the Unnamed Sword. Its Ten-Thousand-Year Cold Iron destroys Pung Yang’s Body-Protecting Qi, leaving the confrontation unresolved.

## Continuity

- Cheol Mubaek is alive but critically injured, with broken limbs and severe internal injuries; Wolhwa’s medicine provides only temporary support.
- Jin Mukyung is unconscious after Pung Yang’s five concealed throwing knives; his recovery is unresolved.
- Pung Yang reached the Peak realm through the Crimson Blood martial arts and heterodox cultivation in two years.
- Pung Yang has approximately seventy percent mastery of the Crimson Blood Twelve Sabers and can temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi with a Temporary Strength Pill.
- Pung Yang’s Temporary Strength Pill began losing effect after roughly half a shichen. He retained one final pill but refused to take it because using three consecutively could endanger his life.
- Pung Yang still intends to capture both Jin brothers and obtain the Taiyuan Jin Family’s martial arts formulas.
- Taekyung consumed the Blazing Flame Divine Pill and gained the Scorching Yang Qi attribute, but its uncontrolled energy caused severe internal injury and a major drop in his stats. The Divine Pill Absorption Quest remains active, and his survival is uncertain.
- Taekyung’s iron spear was cut to less than half its length; he learned Pung Yang’s attack pattern before the final exchange.
- Lee Seowol and nine other surviving Mount Heng Sword Sect martial artists began a sacrificial last stand to protect Taekyung and Mukyung; their fate is unresolved.
- Taekyung’s Unnamed Sword destroyed Pung Yang’s Body-Protecting Qi at the endpoint. Taekyung’s and Pung Yang’s final conditions, and whether either survives, remain unresolved.
- The Peak Quest’s Lunar New Year invitation to the Jin Family remains the governing objective.

## Translation Decisions

- Retain **Peak**, **early Peak**, **First Rate**, **Red Wind Band**, **Sect Leader**, **Taiyuan Jin Family**, **Scorching Yang Qi**, and **Body-Protecting Qi**.
- Render **잠력단** as **Temporary Strength Pill**.
- Render **적혈십이도** as **Crimson Blood Twelve Sabers**, distinct from **Crimson Blood Twelve Swords**.
- Render **열화신단** as **Blazing Flame Divine Pill** and **영단 흡수** as **Divine Pill Absorption**.
- Render **만년한철** as **Ten-Thousand-Year Cold Iron** and **이름 없는 검** as **Unnamed Sword**.
- Render **내상** as **Internal Injury** and **중상** as **Severe Injury** in System notifications.
- Render **일 식경** as **one meal’s time** in this passage.
- Retain **Narye tagon** with a footnote explaining its lazy-donkey imagery; render **격산타우** as **Striking the Ox Across the Mountain** with a footnote explaining force through an obstacle.

### Prior accepted reading-copy tails

#### Chapter 122 tail (verified mastered)

…
as I spent most of my time learning to control my newly acquired Scorching Yang Qi, her final words kept returning to me. *Marriage is one of life’s great human obligations, so take your time thinking it over.* I had been so flustered at the time that I could only open and close my mouth. Who would have thought a woman would propose to me first—and a girl who looked so much younger than me, at that? Although it was a cold political marriage proposal—cold enough that calling it a transaction wasn’t an exaggeration—a proposal was still a proposal. The greater shock, however, was still to come. *Seventeen years old? Is this for real?* A first-year high school student was right in the prime school-lunch-eating years. She was two years younger than my late-born little sister, Hayeon, and a full ten years younger than me. *That’s the Murim for you…* This was a world where getting married in middle school and becoming a parent in high school wouldn’t even be strange. If anything, the three brothers of the Jin Family of Taiyuan looked like the oddballs for remaining unmarried at our age. No, wait a second. “What are you staring at?” Jin Mukyung noticed my gaze and asked irritably. He had suffered considerable injuries at Pung Yang’s hands, but he had now recovered enough to move around on his own. *Come to think of it…* I had never heard whether Jin Mukyung was married. I opened my mouth, half expecting the worst. “Just asking in case.” “What?” “Are you married?” Pffft! Jin Mukyung spat tea into my face and hurriedly shouted. “W-What kind of nonsense is that?” “If you’re not, then you’re not. Why are you so flustered?” After receiving that unexpected facial wash, I wiped my face with my sleeve and continued asking questions. “Why haven’t you married?” Jin Mukyung seemed flustered for a moment, then answered readily. “I’m too busy training in martial arts. Women are a luxury to me.” “You make it sound downright frugal.” “Don’t lump me in with a lecherous idler like you. That’s an insult to me.” “…” Lecherous, my ass. I had spent all twenty-seven years of my life single. If dating was a luxury, then I was the very definition of a miser. The only slight difference was that while Jaringobi ate rice while staring at a strip of dried fish, I had a USB drive.[^2] “What’s with that expression? You look incredibly sad.” “Call it regret over the life I’ve lived.” “At last, you’re becoming human.” He seemed to have a different interpretation of my past life, but fine. He could interpret it however he wanted. “But why did you suddenly ask about marriage? It’s something you already know perfectly well.” “Oh, because the Sect Leader of the Mount Heng Sword Sect asked me to marry her.” Pffft! “…For fuck’s sake. Stop spitting.” As I wiped away the second mouthful of tea, Jin Mukyung regained his composure. “The Sect Leader of the Mount Heng Sword Sect?” “Yeah. She said it two days ago.” “Why on earth would she marry someone like you… Ah, of course. It must be a political marriage.” “…” He wasn’t wrong, but it was still pretty damn irritating. At this point, wasn’t I prime husband material both in the Murim and in the real world? “So, are you thinking of doing it?” “Of course not. How could I marry a girl so much younger than me?” “You’re barely twenty, and you say things like that.” *My body is twenty, but my mind is twenty-seven, you bastard.* Besides, I had decided on my answer to Lee Seowol’s proposal long ago. You can’t set up two households when there’s someone you love. There was only one person in my heart right now. *What could Song-i be doing right now?* Just imagining it made me happy. I tilted my teacup with a blissful smile, and Jin Mukyung stared at me with a bizarre expression. “What a disgusting look.” “Anyway, I’m turning down the marriage for various reasons.” “You made the right decision. At the very least, a political marriage has to offer us something in return. If you marry someone you have no feelings for and gain nothing from it, there’s no reason to enter into a political marriage.” I had thought he was a fool who knew nothing but martial arts, but every now and then, he became a surprisingly sharp realist. “And no matter what they offer, it’s out of the question as long as our eldest brother is around. He isn’t the sort of man who would bind you through a political marriage.” “They did make a pretty substantial offer, though.” “Hm. What did they say they would give you?” Jin Mukyung tilted his teacup with an uninterested expression. “The Blood Wolf Sword Technique, the Blood Wolf Footwork, and the Shura Annihilating Fist.” Pffft! “…Ah, fuck.” This time, I didn’t even have time to wipe my face. Jin Mukyung grabbed me by the collar and shook me hard. “Marry her right now!” [^1]: “School lunch” is Korean slang for a school-age kid, while “clank, clank” evokes handcuffs or prison bars—the joke is that sexual interest in a high schooler could land someone in jail. [^2]: Jaringobi is a traditional Korean image of a miser who stares at dried fish while eating rice rather than eat the fish.

#### Chapter 123 tail (verified mastered)

…
me by the collar and shook me violently, his eyes half rolled back in his head. “Marry her right now!” “Cough! Cough!” Tea had already gone up my nose and left me choking. With Mukyung shaking me nonstop by the collar on top of that, I couldn’t think straight. “Let go! Are you going to let go or not?” “The Shura Annihilating Fist! The Blood Wolf Sword Technique! The Blood Wolf Footwork!” “I get it, so let go first!” “You stupid bastard! Do you even know what kind of martial art the Shura Annihilating Fist is?” “Let go and then we’ll talk!” “A single successor! Transmission only to the worthy!” “Enough, you crazy bastard!” A short while later, by the time I finally pried Mukyung’s hand away, the inside of the pavilion looked as though a storm had passed through it. “Huff… huff…” I caught my breath and looked around. The table had collapsed, the chairs had been smashed to pieces, and shards of broken teaware rolled across the floor. Mukyung calmly straightened his clothes and spoke. “Hmm. I’ve calmed down.” “…” This guy was even crazier than I’d thought. I scrubbed my face with the less-soaked sleeve. “Is the Shura Annihilating Fist the greatest martial art under heaven or something? Why are you so obsessed with it?” “It ranks among the ten greatest fist techniques under heaven. No—it did.” “It did?” “Two hundred years ago. Even in the library of Heaven’s Gate Temple, which holds tens of thousands of books, that martial art survives only in written records. And to think that the Great Hero Tiger of Mount Heng was the current successor to the Shura Annihilating Fist!” His cheeks flushed red from excitement at the mere thought. I blew the tea out of my nose and asked, “So?” “What? What do you mean, ‘so’?” Mukyung stared at me in disbelief. “This is the Shura Annihilating Fist we’re talking about! A Peak martial art whose lineage was believed to have died out long ago!” “And it was one of the ten greatest fist techniques under heaven two hundred years ago?” “Exactly!” “Wait a second.” I picked up a thick wooden stick lying on the floor. Until five minutes ago, it had been known as a table leg. “Know what this is?” “A club?” “You know your stuff.” “What does that have to do with anything?” “About two thousand years ago, wouldn’t this have been one of the ten greatest weapons under heaven or something?” He wasn’t stupid enough to miss my point. Mukyung glared at me. “How dare you compare the Shura Annihilating Fist to something like that.” “Then what’s the difference?” “That’s…” “Sure, it’s worth far more than a wooden club. But does it still hold the same value now?” In the past, mankind had fought with stones and clubs. But when bronze and iron appeared, the march of time left them behind. The Shura Annihilating Fist was no different. “Of course, it’s still an outstanding Peak martial art that everyone would want.” Cheol Mubaek himself had proven that. With the Shura Annihilating Fist, he had become a renowned Peak master in Shanxi Province. “But it’s not still one of the ten greatest fist techniques under heaven, is it?” Just as stone and wooden clubs had given way to steel, martial arts had also advanced. I had no idea what the ten greatest fist techniques under heaven were now, but Mukyung’s expression proved my point. “To put it bluntly, if the Shura Annihilating Fist were really that powerful, Cheol Mubaek wouldn’t have lost to Pung Yang. And here’s the most important part…” I tossed the table leg into a corner and drove the final nail home. “I have no intention of getting married.” “…!” “What can you do when the person involved refuses? Right?” “Well… That’s true.” Mukyung heaved one sigh after another. I’d been ready to fight him if he kept insisting, but he accepted it surprisingly easily. Still, the wistful look in his eyes suggested that he couldn’t stop thinking about the Shura Annihilating Fist manual. *This guy is a martial arts nut too.* Then again, he had gone to Heaven’s Gate Temple because he wanted to learn more martial arts. Now he had discovered a centuries-old martial art that survived only in the records of that very temple. No wonder he was beside himself. “Hoo…” Mukyung let out a sigh deep enough to make the earth cave in and muttered, “What a shame. What a shame.” “It’s not that big a deal. If fate brings it around, we can get it another time.” “You idiot. Do you think Peak martial arts just drop out of the sky?” “Really? Mine did.” “Even at Heaven’s Gate Temple, where all the martial arts under heaven are gathered, Peak martial arts are strictly controlled… What did you say?” “I said mine fell out of the sky.” I pulled an old book from inside my robes. The four characters on its cover had faded under the ravages of time, but they remained clear enough to read. **Flame Divine Palm.** A tiger leaves its hide when it dies, and Jopil left behind a Supreme Peak martial art. “Fl-Fl-Flame…” Today was probably the most astonishing day of Jin Mukyung’s entire life. I grinned as his eyes bulged and darted between me and the martial arts manual. “From now on, call me hyung.”

## Korean source

```text
＃124화



나도 사람인지라 이틀 전 밤 이소월이 내민 세 권의 무공 비급 앞에선 마음이 흔들릴 수밖에 없었다.

자그마치 초절정 무공이다. 진가창법과 진무보법을 대성한 지금, 안 그래도 새로운 무공의 필요성을 느끼고 있던 차에 눈앞에 들이밀어진 달콤한 유혹.

‘이대로는 안 돼.’

풍양과의 싸움은 처절했다. 조필에게서 얻은 [이름 없는 검]이 아니었다면 목숨이 두 개라 해도 살아남지 못했을 것이다.

이젠 더 많은 무공을 익혀서 새로운 경지에 들어야 할 때다.

‘절정 고수.’

혈랑검법과 혈랑보법, 그리고 수라멸권은 이미 검증된 절정 무공이다. 그 높다는 절정의 벽을 허물어트릴 수 있을 만큼 단단한 망치인 것이다. 하지만…….

‘저게 망치면, 이건 포클레인이지.’

나는 손에 들린 낡은 서책을 뿌듯하게 바라봤다.

이 한 권의 무공 비급이 바로 별 미련 없이 이소월의 제안을 거절할 수 있는 이유다.

“화, 화, 화, 화…….”

한참 동안 버퍼링이 걸려 있던 진무경이 마침내 한 단어를 토해 냈다.

“화염신장!”

“오, 아네? 정답.”

200년 전의 천하십대권법도 꿰고 있는 진무경이니 화염신장을 알고 있는 건 어쩜 당연했다. 이건 그보다 훨씬 더 대단한 무공이니까.

‘아이템 확인.’

띠링.



아이템창



[화염신장]

종류 : 무공 비급

등급 : 초절정

제한 : 열양지기의 소유자

설명 : 열화문(熱火門)의 비전절기 중 하나. 강력한 화기를 바탕으로 한 무공이다.

효과 : [화염신장]의 습득





진무경이 믿기지 않는다는 얼굴로 물었다.

“네가 이걸 어떻게…….”

“어떤 고마우신 분이 주고 가셨지.”

“주고 갔다고?”

“응.”

이걸 주고 하늘나라로 훨훨 날아가셨다.

호신강기도 파괴하는 만년한철로 만들어진 [이름 없는 검], 30년의 열양지기를 얻을 수 있는 [열화신단].

마지막으로 초절정 무공인 [화염신장]까지.

나는 아낌없이 주고 떠난 조필을 생각하며 창 너머 푸른 하늘을 바라보았다.

‘잘 지내니.’

그때 진무경이 불쑥 끼어들었다.

“이제 헛소리 그만하고 사실대로 말해라. 열화문(熱火門)의 비전절기가 어떻게 네 손에 있는 거지?”

“말했잖아. 누가 주고 갔다니까.”

“지금 네가 뭘 착각하는 모양인데…….”

진무경이 심각한 얼굴로 말을 이었다.

“농으로 얼버무릴 상황이 아니다.”

“왜?”

“네가 타 문파의 무공을 훔친 도둑놈이 될 수도 있으니까. 자칫하면 본가가 천하 무림의 질타를 받게 된다.”

미처 생각지 못한 문제다.

무공은 곧 문파의 근간이자 역사다. 초절정 무공인 동시에 열화문의 비전절기라는 화염신장이야 말할 것도 없다.

“아, 젠장.”

“다시 한번 물어보마. 화염신장의 비급을 어디서, 어떻게 얻었느냐?”

나는 한숨을 푹 내쉬며 대답했다.

“조필한테서.”

“조필? 내가 알고 있는 일문일살 조필?”

“맞아. 조필을 쓰러트리고 전리품으로 얻은 거지.”

“그놈이 어떻게 화염신장의 비급을 갖고 있었는지 알고 있느냐?”

“글쎄…….”

곰곰이 생각한 끝에 그때 조필이 했던 말을 기억해 낼 수 있었다.

“자기 입으로는 본인이 화염신장의 십구 대 계승자라던데.”

“조필 같은 놈이 어찌…… 잘못 들은 건 아니냐?”

“아냐, 확실해. 거짓말하는 것 같아 보이지도 않았고.”

당시 조필은 선천지기를 끌어 올린 상태였고, 이미 빠르게 죽어 가고 있었다. 죽음을 목전에 둔 사람의 입에서 나오는 말은 대부분 진실에 가깝다.

‘물론 조필이 거짓말을 쳤을 가능성도 염두에 둬야겠지.’

그때 골똘히 생각에 잠겨 있던 진무경이 이해가 안 간다는 얼굴로 입을 열었다.

“화염신장의 계승자라는 놈이 왜 너 같은 놈한테 져?”

“…….”

음, 기분은 더럽지만 일리가 있군.

초절정 무공을 익힌 조필이 낭인 짓을 하고 있다는 것부터가 수상하긴 하다.

‘그러고 보니 검기도 제대로 못 쓰는 놈이었고.’

만나는 놈들마다 검기는 기본이요, 옵션으로 호신강기까지 달고 나오는 요즘이다. 일문일살 조필은 지금까지 내가 상대한 절정 고수 중 가장 약한 축에 속했다.

“화염신장, 이거 생각보다 약한 무공인가?”

“뭐? 화염신장이 약해?”

진무경이 별 미친놈 다 보겠다는 눈빛으로 말했다.

“정신 나간 놈. 화왕(火王)의 독문무공을 약하다고 하는 놈은 천하에 너 하나뿐일 거다.”

“화왕이 누군데.”

“장난칠 기분 아니다.”

“나돈데?”

“그만해라. 재미없으니까.”

“응. 그래서 화왕이 누구냐고.”

이번 침묵은 좀 길었다. 금붕어처럼 입만 벙긋거리던 진무경이 깊은 한숨을 뱉어 냈다.

“네 손, 발가락을 합해 봐라. 모두 몇 개냐?”

“스무 개.”

“그래, 화왕은 천하를 거꾸로 들어서 탈탈 털어도 그 안에 들어가는 고수다.”

“……오우야.”

“일신(一神), 삼성(三星), 십왕(十王). 몰라? 정말 이걸 모른다고?”

이거 아주 못 들어 봤다고 하면 모가지를 비틀어 버릴 기세다.

진무경의 고리눈에 나는 조심스럽게 입을 열었다.

“삼성은 들어 봤는데…….”

“그나마 다행이군.”

이 삼성이 그 삼성이 아니지만 어쨌든.

지금 중요한 건 그게 아니다.

“그럼 내가 화염신장을 갖고 있다는 사실을 화왕이 알게 된다면…….”

“별로 상상하고 싶지 않은 상황이 벌어지겠지.”

젠장, 천하를 통틀어 스무 손가락 안에 든다는 초절정 고수라니. 화왕이 이 사실을 알고 찾아온다면 태원진가 전체가 덤벼도 이길 수 없을 거다.

‘어떻게 얻은 무공인데…….’

익히지도 못하고 넘겨줘야 한다는 사실에 속이 쓰리던 그때였다.

나와 마찬가지로 화염신장의 비급을 안타까운 얼굴로 바라보던 진무경이 한마디를 보탰다.

“화왕이 아직까지 살아 있다면 말이다.”

“뭐?”

“화왕이 마지막으로 모습을 드러낸 것은 사십 년 전이 마지막이다.”

“사십 년 전?”

“처음 무림에 모습을 나타냈을 당시에도 화왕은 이미 노인이었다. 정마대전이 아니었다면 평생 은거기인으로 살았을지도 모르지.”

진무경의 말이 이어졌다.

“남궁세가를 패퇴시키고 안휘성(安徽城)을 점령한 마교의 사기는 하늘을 찔렀다. 수많은 약탈과 살인, 방화가 이뤄졌는데 그 과정에서 구화산(九華山)에 불을 지른 것이 화왕의 심기를 건드렸다더군.”

“그래서?”

“나흘 밤낮 동안 천 명이 죽었고, 구화산 깊숙한 곳에 은거해 있던 노인은 화왕이라는 이름을 얻었다.”

“……천 명?”

“그래. 구화산에서 입은 피해가 너무 컸던 탓에 마교는 얼마 버티지 못하고 안휘성에서 물러나야 했다.”

천 명이란 말이지…….

나는 신중한 고민 끝에 입을 열었다.

“이거, 돌려주자.”

오래 살고 싶다. 내 인생에 단신으로 천 명을 죽였다는 미친 노인네를 만나는 이벤트는 끼워 넣고 싶지 않다.

“당장 출발해야겠네. 안휘성? 아직도 거기 사신대?”

“아무도 모른다. 화왕은 그것으로 분이 안 풀렸는지 일 년 동안 눈에 보이는 마교도들을 전부 박살 내고 다시 은거했으니까.”

“열화문! 열화문에 가면 볼 수 있겠네.”

“열화문은 일인전승(一人傳承)이다. 철 대협과 비슷한 경우지.”

“…….”

돌려주고 싶어도 줄 수가 없네.

그나마 화왕과 가장 가까웠던 인물이라면 조필인데, 이미 죽고 없으니 찾을 방법이 없다.

‘가장 좋은 상황은 화왕이 이미 죽고 없는 건데…….’

사십 년 전 이미 노인이었다고 하니 충분히 가능성이 있다.

반대로 초절정 고수인 만큼 엄청나게 장수하고 있을 수도 있고.

“쓰읍.”

엄청난 보물인지, 아니면 계륵인지. 갈등 어린 눈빛으로 화염신장을 바라보는 내게 진무경이 말했다.

“만약 화왕이 죽었다면…… 네가 바로 열화문의 주인이다.”



* * *



진무경은 빠르게 회복했다. 풍양으로부터 상당한 내상을 입은 탓에 완전히 회복하기까지는 어느 정도 시간이 필요하겠지만, 태원진가로 복귀할 수 있을 만한 기력은 충분했다.

“드디어 돌아가네요.”

혁무진이 감회 어린 얼굴로 중얼거렸다.

“집 나오면 고생이라더니. 앞으로는 절대, 무조건! 본가 밖으로는 나오지 않을 겁니다.”

“……누가 보면 네가 제일 고생한 줄 알겠다, 인마.”

“왜 이러세요? 저도 나름의 고충이 있는 법입니다.”

“너 뒤에 있는 사람한테 똑같이 말해 봐.”

아직도 붕대를 풀지 못한 진무경이 나는 듯이 달려와 혁무진의 뒤통수를 갈겼다.

빡!

“컥!”

“헛소리 그만하고 말이나 몰아.”

“마부가 있는데 왜 제가…….”

혁무진의 말마따나 마부는 따로 있었다. 월화가 따로 붙여 준 하오문 소속의 문도.

그녀는 우리를 배웅하기 위해 먼저 나와 있었다.

“잘 가요. 막상 헤어지려니까 아쉽네?”

“그럼 지금이라도 같이 가실래요?”

나를 향해 눈을 찡긋하는 그녀에게 농담처럼 말을 건넸다. 아직 경계심은 남아 있지만 지난 여정으로 농담 정도는 건넬 수 있는 사이가 됐다.

“어머, 나야 그러고 싶긴 한데…… 이참에 산서 북부를 한번 쭉 돌아볼 생각이라.”

지금까지 항산검문이 철저히 통제하고 있던 산서 북부는 열린 시장이 됐다. 산서성의 총지부장인 월화가 바빠지는 것은 당연한 결과다.

“항산검문과의 일이 잘 풀렸나 보죠?”

“비밀. 명색이 총지부장인데, 제가 본문의 대외비를 외인에게 떠들고 다닐 수는 없죠.”

말은 저렇게 해도 시원시원하게 웃는 모습이 대답을 대신해 주었다.

꼬리 아홉 개가 달려 있어도 이상하지 않은 여인이니 충분히 만족스러운 결과를 얻어 냈을 것이다.

“다음에는 태원진가에서 만나겠네요.”

“아, 혹시?”

“그래도 전(前) 동맹인데, 앞으로도 계속 돈독한 관계를 유지해야 서로 좋지 않겠어요?”

새치름하게 웃은 월화가 치맛자락을 살짝 들어 올렸다.

“그때 꼭 다시 봐요. 그럼 이만.”

그녀가 미리 대기하고 있던 마차에 오르자 곧장 마부가 채찍을 휘둘렀다. 빠르게 멀어져 가는 마차를 하염없이 바라보는 두 쌍의 시선이 있었다.

“쩝. 조금만 더 있다 가시지.”

“음, 으으음.”

혁무진이야 그렇다 치고, 진무경은 도대체 왜?

아쉬움이 듬뿍 묻어 나오는 녀석의 눈빛을 바라보던 내게 문득 떠오르는 생각이 있었다.

‘저 자식, 설마…….’

월화한테 관심이 있나?

세상에, 이럴 수가. 저 무공밖에 모르는 놈이 여자한테 관심을 보이다니.

이 어마어마한 빅뉴스를 혼자만 알고 있을 수는 없다. 나는 개미만 한 목소리로 혁무진에게 바싹 가까이 다가가 아주 작게 속삭였다.

“야, 무진아.”

“아, 깜짝아. 왜요?”

“쉿. 놀라지 말고 들어라. 티 하나도 내지 마. 이건 무덤까지 안고 가야 할 비밀이야.”

혁무진이 바짝 굳은 목소리로 대답했다.

“헙, 네. 말씀하세요.”

“저 인간…… 월화 소저한테 관심 있는 것 같아.”

“…….”

“아무한테도 말하지 마라. 이거 진짜 나만 아는 비밀인데, 너한테만 알려 주는 거야.”

나의 진지한 속삭임에도 혁무진은 썩은 얼굴로 대꾸했다.

“아, 네. 감사합니다. 정말 너무 감사해서 몸 둘 바를 모르겠네요.”

아니, 이 새끼가?

저 싸가지 없는 말투를 어떻게 교정시켜 줘야 할까 고민하던 그때였다.

“은공.”

나는 천천히 돌아섰다. 눈처럼 흰 궁장을 차려입은 이소월이 그곳에 있었다.
```

## Current accepted English baseline

```markdown
# Chapter 124

I was only human, so I couldn’t help wavering when Lee Seowol presented me with three martial arts manuals two nights ago.

They were Supreme Peak martial arts, no less. Now that I had mastered the Jin Family’s Spear Technique and Jin Family’s Manoeuvre Technique, I had already been feeling the need to learn something new. And then, right in front of me, someone had dangled such a tempting offer.

*This won’t do.*

My fight with Pung Yang had been brutal. If I hadn’t had the Unnamed Sword I’d obtained from Jopil, I wouldn’t have survived even if I’d had two lives.

It was time to learn more martial arts and enter a new realm.

*Peak master.*

The Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist were all proven Peak martial arts. They were sturdy hammers, strong enough to break through that supposedly insurmountable wall of the Peak realm. But…

*If those are hammers, then this is an excavator.*

I gazed proudly at the old book in my hand.

This one martial arts manual was the reason I could reject Lee Seowol’s proposal without much regret.

“Fl, fl, fl, fl…”

After buffering for quite some time, Jin Mukyung finally managed to spit out a single word.

“Flame Divine Palm!”

“Oh, you know it? Correct.”

Jin Mukyung knew even the ten greatest fist techniques in the world from two hundred years ago, so perhaps it was only natural that he knew about the Flame Divine Palm. This martial art was even more incredible than those.

*Check item.*

*Ding.*

> **System**
>
> **Item Window**
>
> **Flame Divine Palm**
>
> **Type:** Martial arts manual  
> **Grade:** Supreme Peak  
> **Restriction:** Owner of Scorching Yang Qi  
> **Description:** One of the secret techniques of the Fire Gate Clan. A martial art based on powerful fire energy.  
> **Effect:** Acquisition of Flame Divine Palm.

Jin Mukyung asked with an expression of utter disbelief.

“How did you get this…?”

“Some generous soul gave it to me before he left.”

“He gave it to you?”

“Yeah.”

He gave it to me and then flew away to heaven.

The Unnamed Sword, made of Ten-Thousand-Year Cold Iron capable of destroying even Body-Protecting Qi. The Blazing Flame Divine Pill, which could grant me thirty years of Scorching Yang Qi.

And finally, the Flame Divine Palm, a Supreme Peak martial art.

Thinking of Jopil, who had given me so much before leaving this world, I gazed at the blue sky beyond the window.

*I hope you’re doing well.*

That was when Jin Mukyung abruptly cut in.

“Stop spouting nonsense and tell me the truth. How did a secret technique of the Fire Gate Clan end up in your hands?”

“I told you. Someone gave it to me before he left.”

“It seems you’re under some kind of misunderstanding…”

Jin Mukyung continued with a serious expression.

“This isn’t a situation you can gloss over with a joke.”

“Why not?”

“Because you could end up branded a thief who stole another sect’s martial arts. If things go badly, the Jin Family could be condemned by the entire Murim.”

That was a problem I hadn’t considered.

Martial arts were the foundation and history of a sect. The Flame Divine Palm was not only a Supreme Peak martial art but also a secret technique of the Fire Gate Clan. That went without saying.

“Damn it.”

“I’ll ask you one more time. Where and how did you acquire the manual for the Flame Divine Palm?”

I let out a deep sigh before answering.

“From Jopil.”

“Jopil? The One Question, One Kill Jopil I know?”

“That’s right. I defeated Jopil and obtained it as spoils.”

“Do you know how that bastard came to possess the Flame Divine Palm manual?”

“Not really…”

After thinking carefully, I remembered what Jopil had said at the time.

“He claimed he was the nineteenth-generation successor of the Flame Divine Palm.”

“How could someone like Jopil be… Are you sure you didn’t hear him wrong?”

“No, I’m sure. He didn’t look like he was lying, either.”

At the time, Jopil had been drawing on his innate qi, and he had already been dying rapidly. Words spoken by someone standing on the brink of death were usually close to the truth.

*Of course, I have to consider the possibility that Jopil was lying.*

Jin Mukyung had been lost in thought. Then he spoke with an expression of confusion.

“If he was a successor of the Flame Divine Palm, how did he lose to someone like you?”

“…”

Well, that pissed me off, but he had a point.

It was suspicious enough that Jopil had been living as a wandering martial artist despite having learned a Supreme Peak martial art.

*Now that I think about it, he couldn’t even use Sword Energy properly.*

These days, every martial artist I met came with Sword Energy as standard and Body-Protecting Qi as an optional extra. One Question, One Kill Jopil had been among the weakest Peak masters I had fought so far.

“Is the Flame Divine Palm weaker than I thought?”

“What? The Flame Divine Palm is weak?”

Jin Mukyung looked at me as if I were the craziest person he had ever seen.

“You lunatic. You’re probably the only person in the world who would call the Fire King’s signature martial art weak.”

“Who’s the Fire King?”

“I’m not in the mood for jokes.”

“Neither am I.”

“Stop it. You’re not funny.”

“Okay. So who’s the Fire King?”

This silence lasted a little longer. Jin Mukyung opened and closed his mouth like a goldfish before letting out a deep sigh.

“Count your fingers and toes. How many are there altogether?”

“Twenty.”

“Right. Even if you turned the entire world upside down and shook it out, the Fire King would still be among the twenty greatest masters in it.”

“…Whoa.”

“One God, Three Saints, Ten Kings. You’ve never heard of them? You really don’t know?”

He looked ready to twist my neck if I said I had never heard of any of them.

Under Jin Mukyung’s ringed eyes, I cautiously opened my mouth.

“I’ve heard of the Three Saints, at least…”

“That’s something.”

I meant Samsung,[^1] not the Three Saints, but whatever.

[^1]: The Korean name “Samsung” is pronounced *Samseong*, the same as the Korean term rendered here as “Three Saints.”

That wasn’t important right now.

“Then if the Fire King finds out that I have the Flame Divine Palm…”

“Something you won’t particularly want to imagine will happen.”

Damn it. A Supreme Peak master ranked among the twenty greatest experts in the entire world. If the Fire King learned about this and came looking for me, the entire Jin Family of Taiyuan could attack him together and still lose.

*After everything it took to obtain this martial art…*

My gut twisted at the thought that I might have to hand it over without even learning it.

At that moment, Jin Mukyung, who had been gazing sorrowfully at the Flame Divine Palm manual just as I was, added one more thing.

“If the Fire King is still alive.”

“What?”

“The last time the Fire King appeared was forty years ago.”

“Forty years ago?”

“When he first appeared in the Murim, the Fire King was already an old man. If not for the Great Faction War, he might have lived his entire life as a secluded eccentric.”

Jin Mukyung continued.

“The Demonic Cult’s morale soared after it defeated the Nangong Family and occupied Anhui Province. They carried out countless acts of looting, murder, and arson, and apparently, setting fire to Mount Jiuhua was what finally provoked the Fire King.”

“And then?”

“A thousand people died over four days and nights, and the old man who had been living in seclusion deep within Mount Jiuhua gained the name Fire King.”

“…A thousand people?”

“Yes. The Demonic Cult suffered such heavy losses at Mount Jiuhua that it could not hold out for long and had to withdraw from Anhui Province.”

A thousand people, huh…

After careful consideration, I opened my mouth.

“Let’s give it back.”

I wanted to live a long life. I didn’t want an event involving some insane old man who had killed a thousand people by himself added to my life.

“We should leave right away. Anhui Province? Do people still say he lives there?”

“No one knows. Perhaps that still hadn’t been enough to quell the Fire King’s anger. He spent an entire year crushing every Demonic Cult member he could find before disappearing into seclusion again.”

“The Fire Gate Clan! We can find him if we go to the Fire Gate Clan.”

“The Fire Gate Clan has a single successor. It’s a situation similar to Great Hero Cheol’s.”

“…”

Even if I wanted to return it, I had no one to give it to.

And the person who had probably been closest to the Fire King was Jopil, but he was already dead. There was no way to find him.

*The best-case scenario would be that the Fire King is already dead…*

He had already been an old man forty years ago, so it was certainly possible.

On the other hand, as a Supreme Peak master, he might have lived an extraordinarily long life.

“Hmm.”

Was this a priceless treasure or a useless burden? As I stared at the Flame Divine Palm with a conflicted expression, Jin Mukyung said,

“If the Fire King is dead… then you’re the master of the Fire Gate Clan now.”

* * *

Jin Mukyung recovered quickly. His Internal Injuries from Pung Yang had been considerable, so it would still take some time for him to recover completely, but he had enough strength to return to the Jin Family of Taiyuan.

“We’re finally going home.”

Hyuk Mujin muttered with deep emotion.

“They say leaving home means hardship. From now on, I will never, ever leave the family grounds again!”

“…Anyone listening to you would think you were the one who suffered the most, you punk.”

“What are you talking about? I have my own hardships, you know.”

“Try saying that to the person behind you.”

Jin Mukyung, who still hadn’t been able to remove his bandages, came flying over and smacked Hyuk Mujin on the back of the head.

*Whack!*

“Urk!”

“Stop spouting nonsense and drive the carriage.”

“There’s a coachman. Why do I have to…?”

Just as Hyuk Mujin said, we had a separate coachman—a member of the Lower District Sect whom Wolhwa had assigned to us.

Wolhwa had come out ahead of time to see us off.

“Goodbye. It’s a shame to part now that the time has come, isn’t it?”

“Then would you like to come with us now?”

I spoke jokingly to her as she winked at me. I was still wary of her, but after traveling together, we were close enough to exchange jokes.

“Oh, I would like that, but… I’m planning to take this opportunity to make a full tour of northern Shanxi.”

Northern Shanxi, which had been under the strict control of the Mount Heng Sword Sect until now, had become an open market. It was only natural that Wolhwa, the Lower District Sect’s Chief Branch Leader in Shanxi Province, would be busy.

“Things must have gone well with the Mount Heng Sword Sect?”

“Secret. I may be the Chief Branch Leader, but I can’t go around telling outsiders the sect’s confidential information.”

Her words said one thing, but her bright, carefree smile was answer enough.

She was the sort of woman who could have nine tails and no one would find it strange, so she had probably obtained a more than satisfactory result.

“We’ll meet again at the Jin Family of Taiyuan next time.”

“Oh, really?”

“We were allies once. Wouldn’t it be better for both of us if we continued to maintain a close relationship?”

Wolhwa gave a coy smile and lifted the hem of her skirt slightly.

“Make sure you come see me again then. Well, I’ll be off.”

As soon as she climbed into the carriage waiting nearby, the coachman cracked his whip. Two pairs of eyes gazed blankly at the carriage as it quickly disappeared into the distance.

“Tsk. She could’ve stayed a little longer.”

“Hmm. Mmm…”

Hyuk Mujin was one thing, but why was Jin Mukyung doing that?

As I watched his wistful gaze, a thought suddenly occurred to me.

*Could that bastard possibly…?*

Was he interested in Wolhwa?

Good heavens. I couldn’t believe it. The man who knew nothing but martial arts was showing an interest in a woman.

I couldn’t keep this earth-shattering news to myself. I moved close to Hyuk Mujin and whispered in a voice as small as an ant.

“Hey, Mujin.”

“Ah! You startled me. What is it?”

“Shh. Listen, but don’t be surprised. Don’t show even the slightest reaction. This is a secret we have to take to our graves.”

Hyuk Mujin answered in a stiff voice.

“Gasp. Yes. Go ahead.”

“I think that guy is interested in Young Lady Wolhwa.”

“…”

“Don’t tell anyone. This is a secret only I know, and I’m telling you alone.”

Despite my serious whisper, Hyuk Mujin replied with a sour expression.

“Oh, yes. Thank you. I’m so grateful I don’t know what to do with myself.”

*Why, this little shit…*

I was wondering how to correct that rude tone when—

“Benefactor.”

I slowly turned around.

Lee Seowol stood there, dressed in a snow-white formal robe.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 124`.

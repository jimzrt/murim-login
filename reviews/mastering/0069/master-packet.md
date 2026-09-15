# Master Edit Task — Chapter 69

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
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 권법     | **fist technique**                               |                                                       |
| 신법     | **movement technique**                           |                                                       |
| 주화입마   | **qi deviation**                                 |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 로그아웃             | **Logout**                     |
| 체력               | **Stamina**                    |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 임독양맥 | **Conception and Governor Vessels** | The paired vessels Taekyung attempts to open. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 60–64

## Plot

At Eight Spring Gorge, Taekyung and the reconnaissance squad surround the Head Elder, but his Finger-Flicking Technique kills numerous allied martial artists. Jin Wikyung arrives and joins the assault. Taekyung uses One Flash to destroy the Head Elder’s arm, while the elder cuts apart Wikyung’s ancestral sword and reveals that his betrayal grew from revenge for an old Great Faction War disaster.

The wounded Head Elder forms Sword Force for a final attack. Lee Cheonbaek ambushes him with a dagger, giving Taekyung the opening to finish him with One Flash. Lee dies from the effort. The System records the defeats of Lee Cheonbaek and Jin Baekyang, completes the Traitor Chain Quest, grants Taekyung multiple level-ups and increased Fame, and awards him the Sleeping Dragon of Shanxi title. The First Elder dies after warning Wipeng about Dark Heaven, and the surviving black-clad forces surrender.

Dark Heaven then appears on the cliff. Its agent kills Jin Chung and the Gunggwimun disciples who stayed behind, explaining that Dark Heaven rescued the conspirators from the Demonic Cult decades earlier and implanted gu in their heads. The agent deliberately spares Taekyung.

Five days later, rumors credit the Sleeping Dragon of Shanxi with the Jin Family’s victory. Mount Heng Sword Sect is collapsing after Lee Seogeun and Lee Cheonbaek’s deaths, and its First Young Master is killed by bandits. Jin Mukyung, the Heaven Shaking Sword and Taekyung’s lookalike second older brother, returns after three years at Heaven’s Gate Temple. Taekyung reaches Level 50, advances the Jin Family’s Cultivation Technique to the Eighth Stage, and gains 100 unassigned points.

Mukyung immediately tests Taekyung with the Reformation Fist and grappling techniques. Despite using no internal energy, Mukyung overwhelms him. Taekyung spends ten of his points on Agility, briefly reads Mukyung’s movements, and is struck again. Their spar remains unresolved.

## Continuity

- Jin Baekyang, the former Head Elder, is dead. Lee Cheonbaek died helping Taekyung defeat him.
- The Eight Spring Gorge battle is over; the black-clad conspirators surrendered after the Head Elder’s death.
- The First Elder is dead after naming Dark Heaven. The Second and Third Elders are dead. Wipeng and the surviving senior members’ subsequent fate is unresolved.
- Dark Heaven rescued the conspirators from the Demonic Cult, implanted gu in them, and is pursuing a larger plan. Its agents, purpose, and reason for sparing Taekyung remain unresolved.
- Jin Chung and the Gunggwimun disciples who stayed with him were killed by Dark Heaven.
- Taekyung is Level 50 with Fame 1,180, fifteen years of Internal Energy, and 90 unassigned points after spending 10 on Agility. His four Titles include Sleeping Dragon of Shanxi, Scion of a Prestigious Family, Novice Trainee, and Gambler.
- Sleeping Dragon of Shanxi is a Peak-grade Title granting All Stats +10 and Fame +100.
- Taekyung’s Jin Family’s Cultivation Technique is at the Eighth Stage, but his Internal Energy remains fifteen years because accumulation is slow.
- Jin Mukyung is twenty-three, the Heaven Shaking Sword, a Peak-level martial genius, and Taekyung’s second older brother. He studied at Heaven’s Gate Temple in Henan for three years and is far stronger than Taekyung.
- Taekyung’s spar with Mukyung remains unresolved.
- Mount Heng Sword Sect is near collapse; Lee Seogeun and Lee Cheonbaek are dead, and the First Young Master was killed by mounted bandits.

## Translation Decisions

- Preserve **Dark Heaven**, **Sleeping Dragon of Shanxi**, **Heaven Shaking Sword**, **Sword Force**, **One Flash**, **Reformation Fist**, **Peak**, **Eighth Stage**, **Qi Circulation**, and **Internal Energy**.
- Use **gu** in italics at first use with the established footnote explaining its venomous-creature origin.
- Retain **hyung** for Taekyung’s address to Mukyung.
- Render 금나수 as **grappling technique** rather than assigning an unsupported proper name.
- Keep **Captain of the Gatekeepers**, **Gunggwimun**, **Heaven’s Gate Temple**, and **Mount Heng Sword Sect** consistent with prior chapters.

### Prior accepted reading-copy tails

#### Chapter 67 tail (verified mastered)

…
the circumstances are, you don’t care as long as it’s spacious?” The premise sounded slightly ominous, but I nodded anyway. Jin Wikyung’s face brightened. “That’s a relief. I was worried you might dislike it.” “Where exactly is this place?” “We’re here. This is the building.” “Oh.” We stopped in front of a large three-story pavilion. Compared to the other buildings we had passed, it was much cleaner and had a distinctly elegant, old-fashioned charm. I also liked the tall stone wall surrounding it. “It’s nice.” There was no reason at all to dislike a place like this. Jin Wikyung smiled brightly, looking pleased by my reaction. “Do you like it?” “Yes. It’s much cleaner than I expected. And it looks incredibly spacious.” “That’s right. I had the training ground built large.” “A training hall!” “I had another one built underground in case the weather was bad.” “Oh. Two training halls!” “If we divide them up, there shouldn’t be any problem.” “Whoa. If we divide them up, that’d be perfect… Huh?” Wait. What had he just said? “I’m not supposed to use it alone?” “Oh, well…” Jin Wikyung gave an awkward smile. “It’s spacious enough for two people to use it together, isn’t it? You might grow closer while you’re at it.” “Who is it?” Unease began to creep up my spine. And bad premonitions were never wrong. Instead of answering, Jin Wikyung strode into the pavilion. “Mukyung! Your big brother’s here!” *Oh, damn it.* * * * “So, I’d like you two to live together until his residence is rebuilt.” After hearing the situation, Jin Mukyung readily nodded. “Very well.” I hadn’t expected him to accept so readily. His unexpected response surprised both me and Jin Wikyung. “Wait, are you serious?” “Yes. But please send me one person tomorrow.” “Of course. I was worried about you shutting yourself away in the training ground all alone anyway, so this works out well. I’ll find you a capable servant who’s quick on the uptake. Or should I bring in a cook while I’m at it?” “A servant or a cook is unnecessary.” “Then what?” Jin Mukyung gave me a long, meaningful look. “Please call a physician.” “……” “……” The scenery I had seen on the way here suddenly rose before my eyes. An empty street with no people around. An underground training ground where not even a scream could escape. The perfect conditions for committing a crime. *He’s really made up his mind to beat me senseless.* As I shivered with a chill, Jin Wikyung stammered, “M-Mukyung. No, that’s not it, right? It’s not what I’m thinking, right?” “It’s exactly what you’re thinking. It might be worse.” “If it’s worse…” “Then you’ll need to call an undertaker instead of a physician.” I threw myself toward the exit without delay. Whoosh! Grab! *Goddammit.* Jin Wikyung caught me by the nape and hauled me back. Jin Mukyung let out a short laugh as he watched. “What a pathetic movement technique. Even a back-alley dog would be faster than you.” This time I fired back without backing down. “If something’s faster than me, is it really a dog? It’s Red Hare, isn’t it?”[^3] “Even after taking that beating, you still haven’t come to your senses.” “Hit me! Come on, hit me!” Of course, I had no intention of actually being hit. I had a dependable protector on my side. “Enough!” The booming shout shook the underground training ground. Unlike before, Jin Wikyung’s face had hardened. “What do you two think you’re doing?” I had never seen him like this. They said it was frightening when a kind person got angry, and Jin Wikyung now showed me exactly what that meant. “Instead of getting along as brothers, you’re trying to start a fight in front of me?” Under his fierce glare, Jin Mukyung and I both fell silent. “It isn’t half a year or a year. It’s only fifteen days. I’m asking you to live together just until the pavilion is finished. Was that such a difficult request?” Jin Mukyung flinched. As the one responsible for demolishing the pavilion, he couldn’t help feeling guilty. “That was because that brat was being rude…” “And that gives you the right to demolish a pavilion and beat up your little brother? You call that an excuse?” Jin Mukyung lowered his head. “I’m sorry.” This time, the arrow turned toward me. “Taekyung, what about you?” I wanted to whip out my ID card, but I held myself back. This body was only twenty now, and Jin Mukyung was my blood brother, three years older than me. “Answer!” “……I’m sorry.” Jin Wikyung glared sternly at both of us. “This is a decision I reached after careful consideration. If you dislike each other that much, say so now. I’ll respect your wishes.” Jin Mukyung and I locked eyes in midair. Our answers burst out at the same time. “I don’t want to.” “Nor do I.” “……” After a heavy silence, Jin Wikyung finally managed to speak. “I’m glad you two are willing to follow your big brother’s wishes.” *Why ask when he’d already decided on the answer?* [^1]: Go-stop is a Korean card game commonly played with hwatu cards. [^2]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement; three pyeong is roughly ten square meters. [^3]: Red Hare is the legendary swift horse associated with the historical warlord Lü Bu.

#### Chapter 68 tail (verified mastered)

…
you know they’re from the Jin Family of Taiyuan?” “The gate guards came running and said people from the Jin Family of Taiyuan were outside. And, uh, what was his name? They said some fellow called Wi… Wi-something asked if he could meet you.” Wi-something? The Sect Leader swallowed. “His name wasn’t Wipeng, was it?” “Ah, yes. Wipeng.” The Sect Leader nearly smashed the steward’s head with his wooden pillow. *Ghost Sword Wipeng came here in person?* He was the right hand of the Lesser Family Head, Jin Wikyung, and one of the core masters of the Jin Family of Taiyuan. The thought of a Peak master who had distinguished himself in the recent war paying them a visit nearly scared the soul out of him. “Wake everyone up! Right now!” This was an emergency. Even as the Sect Leader rushed outside, a thousand thoughts raced through his mind. *Is this retaliation?* Song Sword Sect was a small- to medium-sized sect in central Shanxi Province. It had fewer than fifty disciples, most of whom were only Second or Third Rate. They had received various forms of assistance because of their close relationship with the Jin Family of Taiyuan, but when war had actually broken out, they had quietly withdrawn. Perhaps this visit was only to be expected. *Even so, why did Ghost Sword come in person? And at this hour?* The Jin Family of Taiyuan was renowned for its fairness and integrity, so they were unlikely to do such a thing. But if they had come to annihilate Song Sword Sect, there was nothing he could do to stop them. Even he, the strongest martial artist in the sect, might not last three moves against Wipeng. “Sect Leader!” The gate guards, who had been whimpering like puppies desperate to poop, brightened at the sight of their leader. But the Sect Leader could not share their joy. His face stiff, he politely clasped his hands toward the uninvited guests. “I am Huang, the leader of Song Sword Sect.” At the same time, the thirty uninvited guests in bamboo hats parted to either side. Beneath the hazy moonlight, one man stepped forward. “Good to meet you. I’m Wipeng.” He was young, just as the Sect Leader had heard, and ruder than expected. Song Sword Sect might have been an insignificant sect, but how could he treat its Sect Leader like that? Still, the Sect Leader did not dare show his displeasure. The rude young man was Ghost Sword, and behind him stood the name of the Jin Family of Taiyuan. If this was the price of turning a blind eye to an ally’s crisis, then he was getting off cheap. The Sect Leader licked his parched lips. “I have long heard of Ghost Sword’s great reputation. If you had sent word in advance, I would have gone out to welcome you…” “Please do not trouble yourself, Sect Leader. I only intended to deliver a letter from the Lesser Family Head and leave.” “A letter?” Wipeng nodded and handed him a sealed letter. The seal of the Jin Family of Taiyuan was clearly visible in the torchlight held by one of the gate guards. “This is…” “An invitation. The Lesser Family Head requests that you visit our family on New Year’s Day.” The Sect Leader of Song Sword Sect had lived in Murim for many years. He immediately understood the hidden meaning. *What invitation?* This was both a summons and a warning. It was a warning that if they failed to answer the summons, they would be pushed out of the future course of Shanxi Murim. New Year’s Day would be the day the victorious lord accepted new vassals. *The Jin Family of Taiyuan has drawn its sword.* After a brief silence, the Sect Leader spoke. “I have wanted to meet the Lesser Family Head for some time… This will be an excellent opportunity.” “It is an honor that you are willing to visit.” Wipeng politely clasped his hands. The abrupt change in his attitude made the Sect Leader bite his lip. “You must be tired from your journey. Rather than standing out here, why don’t you come inside and rest?” “Thank you for the kind offer, but I think we should be leaving. There is someone we need to catch.” “The man Great Hero Wipeng is pursuing? He must be quite the villain.” “A vicious assassin. He dared to try to harm the Third Young Master.” “T-The Third Young Master? Who would dare attack the Sleeping Dragon of Shanxi?” “Well, we assume the assassin was sent by someone hostile to our family.” “Good heavens.” “But…” Wipeng’s eyes flashed. His sharp gaze swept through the interior of Song Sword Sect. “Wouldn’t you know it, our pursuit led us all the way to Song Sword Sect.” “T-That’s impossible. Surely there has been some misunderstanding?” The Sect Leader’s heart dropped. He was about to start making hurried excuses when Wipeng smiled and waved his hand. “Haha. Of course it must be a mistake. The whole world knows of the deep friendship between the Jin Family of Taiyuan and Song Sword Sect. How could such a thing be true?” “…!” “Thank you for your hospitality. I’ll see you again on New Year’s Day. Hyah!” Wipeng and his subordinates disappeared into the darkness. The Sect Leader of Song Sword Sect remained standing there for a long time.

## Korean source

```text
＃69화



모두가 잠든 깊은 밤. 진위경은 비명과 함께 눈을 떴다.

“크허업!”

맹렬한 기세로 양팔을 허우적거리던 그는 얼마 지나지 않아 자신이 현실로 돌아왔음을 깨달았다.

일렁이는 등잔불과 탁자를 가득 채운 서류. 익숙한 집무실의 풍경이다.

“휴우.”

안도의 한숨을 내쉰 진위경이 목덜미를 주물렀다. 악몽을 꾼 탓인지 목덜미는 식은땀으로 축축했다.

‘죽는 줄 알았네.’

땅이 갈라지고 하늘이 무너지는 꿈이었다. 천지를 진동하는 굉음을 피해 턱에 숨이 차도록 도망치다가 넘어진 것이 마지막 기억이다.

‘너무 무리해서 그런가.’

처리해야 할 일은 넘쳐나는데 인력은 턱없이 부족하다. 피 말리는 하루하루의 연속이다 보니 피로는 쌓여만 갔다.

“끙. 빨리 사람을 뽑든가 해야지. 이러다가는 제 명에 못 살겠어.”

천하는 넓고 인재는 많다. 그런데도 아직 변변한 책사 하나 없는 것은 태원진가의 역량이 부족했기 때문이다.

두 팔 벌려 환영하는 중원의 거대 문파나 이름난 세가(世家)를 놔두고 뭣 하러 산서의 태원진가에 몸을 담겠는가?

그들로서는 당연한 선택일지도 모른다.

‘지금까지는, 말이지.’

이제는 모든 게 바뀔 것이다. 다가오는 원단에 산서 무림을 일통하고 계속해서 영향력을 확장한다면…… 머지않아 태원진가의 깃발 아래로 천하의 인재들이 몰려드는 날이 올 것이다.

‘……그전에 과로로 죽겠지만.’

진위경이 살벌한 양의 서류 더미를 보며 깊은 한숨을 내쉬던 그때였다.

쿠르릉.

아주 미세한 소리. 절정 고수인 진위경이기에 알아차릴 수 있을 만큼 작은 소음이 울렸다.

‘뭐지?’

그는 감각을 곤두세웠다. 공력을 귀에 집중시키자 소리가 또렷해졌다.

쿠르릉. 캉.

작지만 분명히 들었다. 강철이 부딪치는 소리.

누군가 싸우고 있는 것이다. 그것도 이 야심한 시각에.

진위경의 얼굴이 굳은 이유는 그 사실 때문만은 아니었다.

‘저 방향은…….’

진무경의 처소가 있는 곳이다. 그리고 어제부로 한 사람이 더 들어가게 된 곳.

‘설마 무경이가 막내를……. 에이, 아니겠지.’

사이좋게 지내라고 그렇게 신신당부했는데 벌써 치고받고 싸우겠는가. 그는 사랑하는 아우들을 굳게 믿었다.

캉. 캉!

“…….”

진위경이 슬그머니 자리에서 일어났다.



* * *



작정하고 경신법을 펼치자 진무경의 처소까지는 금방이었다.

문제는 목적지가 가까워질수록 들려오는 소리가 심상치 않다는 것에 있었다.

‘……연무장에서 혼자 수련하는 거겠지?’

전각 안으로 들어가야 하나, 말아야 하나. 잠시 고민하던 진위경은 담벼락 위로 고개를 빼꼼 내밀었다.

그리고 충격적인 광경을 목격했다.

“내가, 말했지. 두 번째 규칙. 어?”

쾅! 콰광!

쉬지 않고 검집을 휘두르는 진무경. 그리고 그런 그를 피해 정신없이 도망치는 한 사람.

“로, 로그아웃!”

진태경의 필사적인 외침이 끝나기도 전에 검집이 날아들었다. 아슬아슬하게 비껴간 검집이 연무장의 청석(靑石)을 박살 냈다.

콰앙!

“내가, 이 새끼야, 주화입마, 임독양맥!”

“로그아우우웃!”

“…….”

노구아욱은 뭐고 주화입마에 임독양맥은 왜 튀어나오는가.

당최 알 수 없는 대화의 흐름이었지만 한 가지는 확실했다.

‘저러다가 일 나겠군.’

이대로라면 정말 의원이든 장의사든 둘 중 하나는 불러야 할지도 모르는 판이다.

‘막내는 내가 지킨다!’

진위경이 결의에 찬 얼굴로 난입하려던 그때.

“옆구리는 왜 또 비어? 맞고 싶어서 안달 났냐?”

뻑!

“커흑!”

옆구리에 일격을 얻어맞은 진태경이 비틀거렸다. 진무경이 때를 놓치지 않고 따라붙으며 검집을 휘둘렀다.

퍼버벅!

“악, 악, 악!”

“맞았다고 움츠러들지 마라. 특히 하체!”

퍽!

“이익!”

“어쭈.”

이를 악물고 달려드는 아우의 모습에 진무경이 가소롭다는 듯이 웃었다.

“넌 기본도 안 된 놈이야. 본능대로 손 뻗고 발 나가는 습관부터 고쳐. 무공은 사람이 익히는 거지 짐승이 익히는 게 아니니까.”

“닥쳐!”

“기억력도 안 좋은 놈이군. 푹 자라. 일어나면 규칙을 다시 한번 설명해 주마.”

쉭! 털썩.

정통으로 턱을 얻어맞은 진태경의 신형이 허물어졌다. 대자로 뻗은 그를 말없이 내려다보던 진무경이 천천히 입을 열었다.

“나오십시오.”

누구에게 한 말인지는 명백하다. 머쓱한 얼굴의 진위경이 담벼락 뒤에서 모습을 드러냈다.

“알고 있었느냐?”

“모르는 게 이상하죠. 이 녀석 맞을 때마다 형님 침 삼키는 소리가 천둥처럼 들리던데요.”

진위경이 걱정스러운 눈빛으로 쓰러진 진태경의 상태를 살폈다.

“그렇게 심한 상처는 아니구나. 다행이다.”

“설마 죽기야 하겠습니까?”

“무경아!”

“걱정 마십시오. 근골 하나는 기가 막히게 튼튼한 녀석이니까요.”

“그래?”

“그렇게 두들겨 맞으면서도 두 시진이나 버티더군요. 이 정도 체력과 독기면 금방…… 왜 웃으십니까?”

묘한 미소를 머금은 채로 동생의 얼굴을 들여다보던 진위경이 흔쾌히 대답했다.

“신기해서. 네가 막내 칭찬하는 건 처음 아니냐?”

그 말에 진무경이 멈칫했다.

‘칭찬? 내가 저 녀석을?’

있을 수 없는 일이다. 장점이라고는 눈곱만큼도 없는 동생 아닌가. 가문이 어떻게 돌아가든 말든 술독에 빠져 계집질이나 일삼던 놈을 자신이 칭찬했다니.

진무경은 애써 고개를 저었다.

“……그런 적 없습니다.”

“그렇구나.”

“정말입니다.”

“알았다. 누가 뭐라던?”

“아니, 지금도 웃고 계시잖습니까!”

“그런 적 없다.”

“형님!”

진위경은 터져 나오려는 웃음을 참으려 애썼다. 눈에 넣어도 아프지 않을 막내가 다친 건 마음 아픈 일이지만…… 언젠가는 겪어야 할 일이었다.

‘언제까지 품 안에 둘 수는 없어.’

산서잠룡. 태원진가가 배출한 또 한 명의 천재.

그는 훌쩍 커 버린 아우를 보며 기쁨과 불안감을 동시에 느꼈다. 아니, 그건 어쩌면 두려움이었다.

‘이게 가능한 일인가?’

빨라도 너무 빠르다. 진무경이라는 천재를 가장 가까이서 지켜본 그의 눈에도 진태경의 성장 속도는 불가해(不可解)의 영역이다.

‘나로서는 도저히 가늠이 안 돼.’

어린 시절, 진위경은 촉망받는 기재였지만 결코 천재는 아니었다. 자신 같은 범인(凡人)이 어찌 천재를 이해하고, 가르칠 수 있단 말인가?

그렇게 고민이 깊어 가던 찰나에 진무경이 돌아온 것이다.

진위경은 이때구나, 하고 두 사람을 붙여 놨다.

‘워낙 사이가 좋지 않아 걱정이 많았었는데…….’

오늘 와 보니 괜한 걱정을 했다. 방법이 거칠긴 하지만 그건 분명 일방적인 구타가 아니라 단련이었다. 성장은 빠르지만 아직 미숙한 진태경을 더욱 단단하고 날카롭게 만들어 줄 단련.

비록 몸은 고달프겠지만 말이다.

‘다 널 위해서다.’

쓰러진 막내를 하염없이 다정한 시선으로 바라보던 진위경이 입을 열었다.

“이만 가마.”

하지만 그걸 그냥 보고만 있을 진무경이 아니었다.

“혼자 가긴 어딜 갑니까? 저 녀석도 데려가십시오. 같이 못 살겠습니다.”

“열흘이다. 고작 그 정도도 못 참겠느냐?”

“오늘은 형님을 봐서 이 정도로 끝낸 겁니다. 정 그러면 내일은 장의사 부르시든가요.”

“진심이냐?”

“예. 그러니 당장 데려가는 게 저 녀석한테도 좋을 겁니다.”

“네 뜻이 정 그렇다면…….”

고개를 끄덕인 진위경이 말을 이었다.

“그렇게 하거라.”

“예, 예?”

“원하는 대로 하라고.”

한마디를 툭 던진 진위경이 뒤돌아 걷기 시작했다.

진무경이 어떤 표정을 짓고 있을지 상상하니 피식 실소가 새어 나왔다.

‘네게도 좋은 경험이 될 게다.’

이 불편한 동거는 비단 막내만을 위한 것이 아니다.

천재는 언제나 외로운 법. 두 천재가 서로에게 큰 자극이 될 것임을, 그는 믿어 의심치 않았다.

“일어나, 이 새끼야!”

빡!

“…….”

진위경은 돌아가는 길 내내 뒤돌아보고 싶은 충동을 억눌러야 했다.



* * *



“일어났냐?”

“…….”

“일어난 거 다 안다. 대답해라.”

“…….”

“마지막 기회 준다. 셋 셀 동안 안 일어나면 연무장이 네 무덤이 될 줄 알아라.”

“…….”

“하나, 둘.”

개새끼. 숫자 한번 더럽게 빨리 센다.

나는 슬그머니 일어나 기지개를 켰다.

“어우, 잘 잤다.”

슬쩍 고개를 돌리니 고리눈을 뜬 진무경이 보였다.

저 얼굴을 보니까 어제의 기억이 새록새록 되살아난다. 피도 눈물도 없는 놈. 쳐 죽일 놈.

나는 천연덕스러운 목소리로 말을 걸었다.

“어? 형님. 언제 오셨어요?”

“……방금.”

아쉬운 얼굴로 입맛을 다시는 진무경을 보니 존댓말을 쓴 게 신의 한 수라는 생각이 들었다. 뭐 하나 트집 잡히기라도 하면 복날 개 잡듯이 두들겨 팰 놈이니까.

‘시바…… 약한 게 죄다. 죄.’

나도 오기가 있는 놈이다. 하지만 맨주먹으로 하는 싸움에서는 죽었다 깨어나도 진무경을 당할 수 없었다.

저놈이 체계적인 권법, 각법을 익힐 때 나는 UFC 경기를 봤다. 애초에 오기로 어떻게 해볼 수 있는 상대가 아니다.

그래서 마지막으로 선택한 게 로그아웃이었다.

물론 보기 좋게 실패했지만.

‘전투 시에는 로그아웃이 불가능하다니. 그딴 게 어디 있어.’

미리 말이나 해 주든가. 그것도 모르고 덤볐다가 인생에서 로그아웃 당할 뻔했다. 나는 힐끔 진무경을 곁눈질했다.

“야.”

“예?”

“너 왜 눈을 그렇게 떠?”

“제가요?”

싸늘한 목소리에 최대한 눈을 초롱초롱하게 떴다. 이제는 눈도 착하게 떠야 한 대라도 덜 맞는다.

“너…… 후. 조심해라.”

“네, 형님.”

갑자기 공손해진 내 태도에 진무경은 기분 나쁘다는 듯한 표정을 지었다. 하지만 예의 바르다고 때릴 수도 없는 노릇이겠지.

“어제 일 말인데…….”

잽싸게 고개를 숙였다.

“제 잘못입니다. 수련 중이신데 큰 소리를 내다니. 맞아도 싸죠.”

“아니, 야.”

“어떡해, 어제 저 때리시느라 손 아프셨겠다. 제가 호 불어 드릴까요?”

“이거 완전히 미친놈이네.”

진무경은 나를 때릴까 말까 고민하는 눈치였지만 결국 포기하고 주먹을 내려놨다.

“됐다. 따라 나와.”

“……어디로요?”

“연무장.”

앞에 했던 말 정정. 연무장에서 때릴 모양이다. 그래, 또 내 방을 초토화시킬 순 없을 테니까.

바짝 굳은 내 표정을 본 진무경이 혀를 찼다.

“그런 거 아니니까 따라와. 오늘부터 수련이다.”

“수련이요?”

“그래. 네 녀석의 끔찍한 무공을 처음부터 뜯어고쳐 주마.”

볼 때마다 두들겨 패던 인간이 갑자기 수련을 도와준다고? 그것도 자기 시간까지 쪼개 가면서?

‘차라리 마왕 아스모데우스가 회개했다는 말을 믿지.’

의심 가득한 눈초리를 스스로도 느꼈는지 진무경이 깊은 한숨을 내쉬었다.

“어제 형님께서 다녀가셨다.”

“아.”

성격은 지랄맞아도 위아래가 확실한 놈이다. 진위경이 직접 부탁했다면 지금 상황이 이해된다.

“비어 있는 건물이 몇 채인데 너를 왜 내게 보냈겠느냐? 젠장. 아예 처음부터 거절했어야 했는데.”

……어지간히 가르쳐 주기 싫은 모양이군.

하지만 나로서는 그의 도움이 꼭 필요하다. 하다못해 괜찮은 권각술 하나라도 전수받는다면 분명히 써먹을 데가 있을 테니까.

“부탁드립니다.”

진무경이 고개를 저었다.

“생각하고 말해. 내 기준에 맞추려면 벅찰 테니까. 힘들다고 포기할 바에야 지금 깨끗하게 접어라.”

힘들 때마다 포기했다면, 여기까지 오지도 못했다.

“강해지고 싶습니다.”

목소리에 담긴 진심을 읽은 걸까? 한동안 물끄러미 나를 응시하던 그가 결국 입을 열었다.

“연무장으로 나와라.”

띠링.



- 퀘스트가 생성되었습니다.



퀘스트



[시련? 수련?]

정해진 기간 동안 진무경의 지도를 받으며 수련하십시오. 당신이 얼마나 강해지건, 진무경이 만족하지 않는다면 퀘스트는 실패합니다!



등급 : 절정

제한 : 진태경

임무 : 진무경의 인정 (미완료)

보상 : ???

실패 : ???

남은 시간 : 9일 23시간 51분 10초





‘진무경의 인정이라.’

추상적인 임무지만 충분히 자신 있다. 시스템의 사기성과 내 노력이 합쳐진다면 진무경의 눈이 튀어나올 만큼 빠르게 성장할 수 있을 테니까.

‘할 수 있어.’

내가 결의를 다지던 그 순간이었다.

“참. 너 창 쓰지?”

“아, 네.”

“그것도 챙겨서 나와.”

진무경은 검사다. 그러니 당연히 권법 위주로 가르쳐 줄 거라 생각했는데. 어리둥절한 일이라 일단 조심스럽게 물어봤다.

“갑자기 창은 왜……?”

“수련도 실전처럼. 그런 말 못 들어 봤어?”

진무경이 환하게 웃으며 덧붙였다.

“형님한테도 허락 맡아 뒀다. 장의사 불러도 상관없대.”

경쾌한 발걸음으로 사라지는 그의 뒷모습을 멍하니 쳐다보던 나는 간신히 입을 열었다.

“……로그아웃.”

삑.



- 해당 퀘스트 중에는 로그아웃이 제한됩니다.



이런 시발.
```

## Current accepted English baseline

```markdown
# Chapter 69

In the dead of night, while everyone else slept, Jin Wikyung awoke with a scream.

“Graaah!”

He flailed both arms with startling force, then soon realized that he had returned to reality.

The flickering lamplight and the documents covering his desk. The familiar sight of his study.

“Phew.”

After letting out a sigh of relief, Jin Wikyung rubbed the back of his neck. It was damp with cold sweat, probably because of the nightmare.

*I thought I was going to die.*

It had been a dream in which the earth split apart and the sky collapsed. He had run from a deafening roar that shook heaven and earth until he was gasping for breath, and his last memory was of falling.

*Maybe I’ve been pushing myself too hard.*

There was more work than he could handle, but nowhere near enough people to do it. Each day was a nerve-racking struggle, and the fatigue kept piling up.

“Ugh. I need to hire more people soon. At this rate, I’ll die before my time.”

The world was vast, and there were plenty of talented people in it. And yet the Jin Family of Taiyuan still did not have a single decent strategist. That was because the family’s capabilities were lacking.

Why would any talented person choose to join the Jin Family of Taiyuan in Shanxi when they could go to one of the great sects or renowned clans of the Central Plains, where people would welcome them with open arms?

From their perspective, it was an obvious choice.

*Until now, that is.*

Everything was about to change. If the Jin Family united Shanxi Murim on New Year’s Day and continued expanding its influence…

Before long, talented people from across the land would come flocking beneath the Jin Family of Taiyuan’s banner.

*Although I’ll probably die of overwork before then.*

Jin Wikyung let out a deep sigh as he stared at the terrifying mountain of paperwork.

That was when it happened.

Rumble.

It was an extremely faint sound, so quiet that only a Peak master like Jin Wikyung could have noticed it.

*What was that?*

He sharpened his senses. When he focused his internal energy on his ears, the sound became clearer.

Rumble. Clang.

Small, but unmistakable.

The sound of steel striking steel.

Someone was fighting. At this hour of the night, no less.

That was not the only reason Jin Wikyung’s face hardened.

*That direction is…*

It was where Jin Mukyung’s residence was located. And, as of yesterday, there was one more person living there.

*Surely Mukyung isn’t beating up the youngest… No, of course not.*

He had repeatedly urged them to get along. Surely they would not already be beating each other senseless.

He trusted his beloved younger brothers.

Clang. Clang!

“…”

Jin Wikyung quietly rose from his seat.

* * *

Once he fully unleashed his movement technique, Jin Wikyung reached Jin Mukyung’s residence in no time.

The problem was that the closer he got, the more ominous the sounds became.

*…He’s probably training alone in the training hall, right?*

Jin Wikyung hesitated over whether he should enter the pavilion. In the end, he cautiously poked his head over the wall.

And witnessed a shocking sight.

“I told you. Rule number two. Huh?”

Boom! Crash!

Jin Mukyung swung his scabbard without pause. One person fled desperately, trying to escape him.

“Lo, Logout!”

Before Jin Taekyung could even finish his desperate cry, the scabbard flew toward him. It narrowly missed him and smashed into the bluestone floor of the training hall.

Bang!

“I told you, you bastard—qi deviation! Ren and Du meridians!”

“Logouuuut!”

“…”

What was “Loguawk,” and why were qi deviation and the Ren and Du meridians suddenly coming up?

The flow of the conversation made absolutely no sense, but one thing was certain.

*Something bad is going to happen if this keeps up.*

At this rate, they might really need to call either a physician or an undertaker.

*I’ll protect the youngest!*

Jin Wikyung was just about to charge in with determination on his face when—

“Why is your side open again? Are you that desperate to get hit?”

Whack!

“Guh!”

Jin Taekyung staggered after taking a blow to the ribs. Jin Mukyung did not miss the opportunity and followed up with another swing of his scabbard.

Thwack-thwack-thwack!

“Argh! Argh! Argh!”

“Don’t shrink back just because you got hit. Especially with your lower body!”

Thwack!

“Grrr!”

“Oh, look at you.”

Jin Mukyung smiled disdainfully at the sight of his younger brother charging at him with his teeth clenched.

“You’re an idiot who doesn’t even have the basics down. Fix that habit of throwing out your hands and feet on instinct first. Martial arts are learned by people, not beasts.”

“Shut up!”

“You have a terrible memory, too. Sleep well. When you wake up, I’ll explain the rules again.”

Whoosh! Thud.

Jin Taekyung took a direct hit to the chin, and his body crumpled. Jin Mukyung silently looked down at him lying spread-eagled on the floor, then slowly spoke.

“Please come out.”

There was no question who he was speaking to. Jin Wikyung emerged from behind the wall with an awkward expression.

“You knew I was here?”

“It would be strange if I didn’t. Every time that kid got hit, I could hear you swallowing from here like thunder.”

Jin Wikyung examined Jin Taekyung’s fallen body with worried eyes.

“The injuries aren’t too severe. That’s a relief.”

“It’s not like he’s going to die.”

“Mukyung!”

“Don’t worry. His bones and sinews are unbelievably sturdy.”

“Really?”

“He lasted four hours while taking a beating like that. With that kind of stamina and grit, he’ll soon… Why are you laughing?”

Jin Wikyung gazed at his younger brother’s face with a strange smile and answered cheerfully.

“It’s fascinating. Isn’t this the first time you’ve ever praised the youngest?”

Jin Mukyung stiffened.

*Praise? I praised that bastard?*

It was impossible. Wasn’t he a younger brother without a single redeeming quality? Jin Mukyung had praised the man who had spent his days drowning in alcohol and chasing women, heedless of what happened to the family?

Jin Mukyung forced himself to shake his head.

“…I have never done such a thing.”

“I see.”

“I really haven’t.”

“All right. Who said otherwise?”

“No, you’re still laughing!”

“I have never done that.”

“Hyung!”

Jin Wikyung tried to suppress the laughter welling up inside him. It pained him to see his beloved youngest brother hurt, but this was something he would have to experience someday.

*I can’t keep him under my wing forever.*

Sleeping Dragon of Shanxi.

Another genius produced by the Jin Family of Taiyuan.

Jin Wikyung felt both joy and unease as he looked at his younger brother, who had grown so much in such a short time.

No. Perhaps it was fear.

*Is this even possible?*

It was far too fast. Even to someone who had watched the genius Jin Mukyung from closer than anyone else, Jin Taekyung’s rate of growth was beyond comprehension.

*I can’t even begin to gauge it.*

As a child, Jin Wikyung had been a promising talent, but he had never been a genius. How could an ordinary man like him understand a genius, let alone teach one?

His thoughts were growing deeper when Jin Mukyung returned.

Jin Wikyung had known at once that this was the moment, and put the two of them together.

*I was so worried because they got along so poorly…*

Now that he had seen them together, those worries had been pointless. The method was rough, but this was clearly not one-sided beating. It was training.

Training that would make the fast-growing but still inexperienced Jin Taekyung stronger and sharper.

His body would suffer, though.

*It’s all for your sake.*

Jin Wikyung looked down at the fallen youngest with boundless tenderness and spoke.

“I’ll be going now.”

But Jin Mukyung was not about to let him leave like that.

“Where are you going alone? Take that kid with you. I can’t live with him.”

“It’s ten days. Can’t you endure that much?”

“I stopped at this much today out of respect for you. If you insist, call an undertaker tomorrow.”

“Are you serious?”

“Yes. So taking him with you right now would be better for him, too.”

“If that is truly what you want…”

Jin Wikyung nodded and continued.

“Then do so.”

“Yes, yes?”

“Do as you wish.”

After tossing out that one sentence, Jin Wikyung turned and began walking away.

Imagining what expression Jin Mukyung must be wearing, he let out a quiet laugh.

*This will be good experience for you, too.*

This uncomfortable arrangement was not only for the youngest.

Geniuses were always lonely. Jin Wikyung had no doubt that the two geniuses would greatly spur each other on.

“Get up, you bastard!”

Whack!

“…”

Jin Wikyung had to suppress the urge to look back the entire way home.

* * *

“Are you awake?”

“…”

“I know you’re awake. Answer me.”

“…”

“I’ll give you one last chance. If you’re not up by the time I count to three, this training hall will be your grave.”

“…”

“One, two.”

*Bastard. He counts ridiculously fast.*

I quietly got up and stretched.

“Whew, I slept well.”

I casually turned my head and found Jin Mukyung glaring at me.

The moment I saw that face, yesterday’s memories came flooding back.

A man without blood or tears. A bastard who deserved to be beaten to death.

I addressed him in a nonchalant voice.

“Oh? Hyung-nim. When did you get here?”

“…Just now.”

Seeing Jin Mukyung smack his lips with disappointment, I decided that switching to formal speech had been a stroke of genius. If he found even one thing to nitpick, he was the type to beat me like a dog.

*Fuck… Being weak is a sin. A sin.*

I had my pride, too. But in an unarmed fight, I could not beat Jin Mukyung even if I died and came back to life.

While that bastard had been learning systematic fist and kicking techniques, I had been watching UFC matches. He was not someone I could overcome through sheer stubbornness.

That was why I had chosen Logout as a last resort.

Of course, it had failed spectacularly.

*You can’t Logout during combat? What kind of ridiculous rule is that?*

They could have told me beforehand. I had charged in without knowing and nearly logged out of life.

I cast a sidelong glance at Jin Mukyung.

“Hey.”

“Yes?”

“Why are you looking at me like that?”

“Me?”

At his icy tone, I made my eyes look as bright and innocent as possible.

Now I even had to watch how I looked at him if I wanted one less beating.

“You… Hah. Be careful.”

“Yes, Hyung-nim.”

Jin Mukyung looked displeased by my sudden politeness. But he could hardly hit me just for having good manners.

“About yesterday…”

I quickly bowed my head.

“It was my fault. I was making so much noise while you were training. I deserved to get hit.”

“No, hey.”

“Oh, no. Your hand must hurt from hitting me yesterday. Would you like me to blow on it?”

“You’re completely insane.”

Jin Mukyung looked as though he was debating whether to hit me, but eventually gave up and lowered his fist.

“Enough. Follow me.”

“…Where?”

“The training hall.”

Retract what I said earlier. He planned to beat me in the training hall.

There was no way he could turn my room into a wasteland again, after all.

Seeing my expression stiffen, Jin Mukyung clicked his tongue.

“It’s not that. Follow me. Training starts today.”

“Training?”

“Yes. I’ll tear apart your horrible martial arts and rebuild them from the beginning.”

The man who had beaten me senseless every time he saw me was suddenly offering to help me train? And he was even carving out time from his own schedule?

*I’d sooner believe that the Demon King Asmodeus had repented.*

Perhaps he noticed the suspicion in my eyes, because Jin Mukyung let out a deep sigh.

“Hyung came by yesterday.”

“Ah.”

His personality might have been foul, but he had a clear sense of rank and propriety. If Jin Wikyung had personally asked him, the current situation made sense.

“There are several empty buildings. Why do you think he sent you to me? Damn it. I should have refused from the beginning.”

…I suppose he really did not want to teach me.

But I desperately needed his help. If nothing else, there had to be some use for learning even one decent fist-and-kicking technique from him.

“Please teach me.”

Jin Mukyung shook his head.

“Think before you speak. Meeting my standards will be difficult. If you’re going to give up as soon as things become hard, quit now.”

If I had given up every time things became difficult, I would never have made it this far.

“I want to become stronger.”

Perhaps he sensed the sincerity in my voice. After staring at me for a long time, he finally opened his mouth.

“Come out to the training hall.”

Ding.

> **System**
>
> **Quest**
>
> **Trial? Training?**
>
> Train under Jin Mukyung’s guidance for the designated period. No matter how strong you become, the Quest will fail if Jin Mukyung is not satisfied!
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Jin Mukyung’s recognition (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???
>
> **Time Remaining:** 9 days 23 hours 51 minutes 10 seconds

*Jin Mukyung’s recognition.*

It was an abstract mission, but I was confident enough. If I combined the System’s cheat-like advantages with my own effort, I could grow so quickly that Jin Mukyung’s eyes would pop out.

*I can do this.*

That was when I was steeling my resolve.

“Oh, right. You use a spear, don’t you?”

“Ah, yes.”

“Bring that with you, too.”

Jin Mukyung was a swordsman. Naturally, I had assumed he would primarily teach me fist techniques. Puzzled, I cautiously asked:

“Why the spear all of a sudden…?”

“Train as if it were real combat. Haven’t you heard that saying?”

Jin Mukyung smiled brightly and added:

“I even got Hyung’s permission. He said he doesn’t mind if we have to call an undertaker.”

I stared blankly at his back as he walked away with light, cheerful steps. At last, I managed to open my mouth.

“…Logout.”

Beep.

> **System**
>
> - Logout is restricted during this Quest.

*Fuck.*
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 69`.

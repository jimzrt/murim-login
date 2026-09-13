# Master Edit Task — Chapter 372

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

## Chapter 374 Expedition

- This branch backfills Chapters 370–373 against the Chapter 65 anchor. Chapters 66–369 have no accepted local English translation here.
- Treat `docs/EXPEDITION_SEED.md` as bounded orientation, not as a substitute for missing translations. Do not read parked Chapters 374–375 while drafting 370–373.
- When the current Korean source conflicts with bridge context, the current source wins. Preserve uncertainty instead of inventing skipped-range backstory.
- After Chapter 373 is committed, run `python tools/expedition.py resume-parked` so the existing 374–375 translations remain the accepted line.

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
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 하오문    | **Lower District Sect**          |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 마교     | **Demonic Cult**                                 |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 시스템              | **System**                     |
| 스킬               | **Skill**                      |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 문경 | **Mungyeong** | Young Disciple of the Divine Physician overseeing Jin Taekyung's care. |
| 사천당문 | **Sichuan Tang Clan** | The Tang family and clan of Sichuan |
| 삼괴 | **Samgoe** | Principal culprit being escorted to Henan |
| 서천마군 | **Western Heaven Demon Lord** | Major obstacle recently overcome by Taekyung |
| 청성파 | **Qingcheng Sect** | Orthodox sect represented among the assisting martial artists. |
| 개방 | **Beggars' Sect** | Organization represented by the attending beggars. |
| 청풍고검 | **Clear Wind Ancient Sword** | Sect Leader of the Qingcheng Sect; epithet of the old Daoist. |
| 멸절신니 | **Extinction Divine Nun** | New Sect Leader of the Emei Sect after the death of the Heaven-Shaking Divine Nun. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 멸절신니 | 적천강 | orthodox_elder_to_orthodox_elder | Benefactor Jeok | respectful-but-familiar | Uses 시주 when responding to Jeok Cheongang. |
| 적천강 | 문경 | orthodox_elder_to_younger_orthodox_elder | Wen | hostile-but-blunt | Jeok Cheongang addresses Mungyeong as 문가 while intervening on Taekyung's behalf. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |
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

#### Chapter 370 tail (verified mastered)

…
said—don’t say it in front of Grandfa—no, especially not in front of Mungyeong.” “What? Why are you suddenly saying—” “No. Really, don’t.” “…” Hyuk Mujin and Gung Gibang exchanged bewildered looks. Then Cheongpung suddenly gasped. “Mimi! Where did you go, Mimi?” At that moment, just as Cheongpung began desperately searching for the thousand-year one-horned snake that had disappeared during the brief time he looked away, a muffled shout burst from beyond the firmly closed door. “Gack! Hey, you snake bastard!” The three men’s gazes collided in midair. At the same time, several different names for one person rang through the pavilion and echoed outside. “Benefactor!” “Squad Leader!” “Jin Taekyung!” The shouts caused a commotion among the people outside, who had been busy with their respective tasks. “Did you hear that?” “Could he have woken up?” “Report this to the Sect Leader! Quickly!” * * * I had a nightmare. A snake was slowly tightening around my neck in an abyss of pitch-black darkness where I couldn’t see an inch ahead. I couldn’t breathe, and my vision washed white. Then, in the next moment, I opened my eyes and exhaled the breath I had been holding. “Guh-ack!” Ssssk. “…?” *Ssssk? What the fuck is this?* Three seconds of complete mental shutdown. At last, I realized what my nightmare had been. I grabbed the horn of the snake coiled tightly around my neck. “Hey, you snake bastard!” I didn’t care whether its name was Thousand-Year One-Horned Snake, Mimi-chan, or whatever else. From today onward, this bastard’s name was Snake Wine. “You’re living on nothing but dew from now on. Cham Isul.[^2]” I swung it around, preparing to slam it forcefully onto the floor, when the firmly closed door exploded inward and someone charged through. “Benefactor!” Cheongpung’s thunderous shout made my skull ring. Behind him, I saw Hyuk Mujin wriggling like an earthworm and Gung Gibang hopping along on one leg. “Squad Leader!” “Jin Taekyung!” “…Why do you all look like that?” Hyuk Mujin answered while vigorously bouncing his body. “Samgoe. That insane old monster did this to me.” Gung Gibang helpfully elaborated. “It’s sheer luck he survived. That lunatic Hyuk Mujin mixed rocks into some dirt and threw it at Samgoe. If Chilseonja hadn’t stepped in and blocked him at just the right moment, Hyuk Mujin would have been torn limb from limb.” “…?” *Who the hell are Samgoe and Chilseonja? Kim Sunja was the name of my high-school dean of students…* *These fucking lunatics.* My relief at surviving the underground prison lasted only a moment. A headache came on, and I pressed a hand to my forehead. I had specifically told them to hole up at the Divine Physician’s residence, but apparently they couldn’t sit still for even that long and had crawled out to fight to the death. Thank God they had survived. What would I have done if they had died? “Were you idiots desperate to die? What kind of trouble did you cause this time?” “…?” “…?” “What? Why?” Why did they look like that? The three of us—everyone except Cheongpung—exchanged bewildered glances. “Is there a problem?” “Of course there is.” “You told us to go save the Emei Sect, Squad Leader.” The first answer came from Gung Gibang, the second from Hyuk Mujin. They were both talking nonsense, so I deliberately frowned. “What are you talking about? I did?” “Yes. That’s definitely what I heard from Mungyeong. Did you hit your head?” No way. I could feel it the moment I opened my eyes: a powerful qi boiling throughout my entire body. The world spread out before me and the qi of nature surrounding me both felt clear and vivid. *So this is the Supreme Peak realm…* I wanted to test this power right away—and check the mountain of System messages that must have piled up by now. But before either of those, I needed to stop listening to this nonsense and ask one thing. “Is everyone safe?” They all knew who I meant by *everyone*. Smiling brightly, Cheongpung threw open the enormous window instead of answering. “See for yourself, Benefactor.” As if possessed, I slowly walked toward the window. A warm spring breeze brushed my face. An oddly quiet atmosphere greeted me as I leaned out and looked beyond the window. “Ah.” I looked down and was rendered speechless. There were people gathered below. Nuns, Daoists, and people who appeared to be craftsmen, such as carpenters. Physicians wearing brilliant white garments. Countless gazes were fixed on me, all carrying the same emotion. *Awe.* The next moment, as though by some prior agreement, they all paid their respects. Some gave a fist-and-palm salute. Some bowed their heads slightly. Others prostrated themselves deeply. At the same time, one enormous voice rose as though from a single throat. “We pay our respects to the Blazing Fire Divine Dragon!” A shiver pierced me from the crown of my head to the tips of my toes. Ding. > **System** > > - Your achievements and Fame will resound throughout the Central Plains. > - You have acquired a new epithet! Along with the System notification ringing in my ears, I spotted someone in the distance. “Well done.” I smiled back at Jeok Cheongang. [^1]: An *imugi* is a serpent from Korean legend said to become a dragon. [^2]: *Cham Isul* is a Korean soju brand whose name literally means “true dew.”

#### Chapter 371 tail (verified mastered)

…
“I’ll go.” My body felt light, and going with them would give me a chance to hear everything that had happened. I had no particular reason to refuse. At my ready answer, the two Sect Leaders turned and began leading the way. Then Jeok Cheongang suddenly spoke. “But why don’t I see one of them?” “He is waiting downstairs.” “He said he did not want the others to notice him.” *One of them? If he’s important enough to be part of this group, could it be Tang Sadok, the Family Head of the Tang Clan?* *Well, whoever it is, I’ll be seeing him soon enough.* But my curiosity vanished without a trace the moment I stepped out of the pavilion and encountered one person. At the sight of that familiar face, a delighted shout burst from me. “Hey, you bastard! Mungyeong!” Mungyeong looked exactly as he had before leaving the Sichuan Tang Clan. Dark Heaven had invaded soon after he left, so I had been worried. Maybe he and Dark Heaven had simply missed each other on the road—somehow, he’d escaped unhurt. “When did you get here? Damn, you look even taller than before. Are you going through a growth spurt?” “……” “Why are you so quiet? In a bad mood? Or maybe…” I mussed Mungyeong’s hair, then whispered, “Did you have a wet dream this morning?” “……!” “You did. You definitely did.” Look at the brat, too embarrassed to say anything. I smiled in satisfaction. It was something that happened from time to time at that age. Maybe I should use this opportunity to spread proper sex education through this stale old Murim. “This hyung of yours will show you a whole new world. From now on, call me Teacher Jin Seong-ae.” Teacher Gu Seong-ae, are you watching? Your knowledge is crossing space and time. I was patting Mungyeong’s shoulder, swelling with pride, when it happened. “Uh…” “Well…” “Good grief… We forgot to tell him that.” Forgot to tell me what? Three long sighs came from behind me. At the same time, a dry voice slipped between Mungyeong’s lips. “Take your hand off.” “…Huh?” “And my wet dreams ended a long time ago.” “That’s a little concerning, because you still haven’t completely finished your secondary sexual development—no, that’s not what I mean.” I swallowed hard. A horrifying thought suddenly flashed through my mind. “Who… are you?” *Mom, I’m scared.* * * * “…and that is how things came to be.” “A truly bizarre affair.” Even as they raced along at tremendous speed using their movement techniques, the two Sect Leaders’ voices did not waver. When they looked at me as though demanding an answer, I managed to part my lips. “Ah, yes. So the place we’re heading to has some kind of strange formation, right?” “According to what we learned by capturing and interrogating Samgoe, that is the case. But the formation itself is so strange…” Jeok Cheongang answered gruffly. “This old man and this brat are both hopeless when it comes to formations. Even if we look at it, we won’t understand a thing.” I agreed. Mount Jiuhua’s Blazing Fire Cave had an impressive arcane formation installed, but that did not mean we were experts in such things. *We’d be better off calling in someone like the Zhuge Clan.* But it would take the Zhuge Clan a considerable amount of time to arrive. For some reason, the two Sect Leaders seemed to have high expectations of us. Especially me. “Fellow Daoist Jin, did you notice anything else strange about that man? Anything he said or did?” “That’s everything I told you. And from what I could tell… there wasn’t much room for him to get any stranger.” Dark Heaven’s people were weird by their very existence. They were fanatics who practically—or rather, simply—worshiped a being called the Heavenly Lord as a god. The powers and bizarre abilities displayed by the Blood Lord and the Western Heaven Demon Lord were no different. *Regenerating like a human troll, detaching and reattaching an arm as if it had double-sided tape on it—and to top it all off, even possession.* The more I thought about it, the more miraculous it seemed. That we had fought those bastards and won. “Hm. Before you awoke, I heard a rough account of the situation from Benefactor Jeok. Once the message hawk we sent to Henan returns with a reply, we should know how to proceed.” “Just in case, if you notice anything strange when you see the formation, let us know.” “Yes.” As I answered, I glanced at the figure far ahead of us. Mungyeong. No, the man known by the epithet Slaughter Saint. *Fuck. Why is the Slaughter Saint here?* Honestly, I nearly pissed myself. Even if I had spent half a day splashing around and grilling meat in the Valley of the Sanzu River,[^2] it would not have been this bad. *Mungyeong was the Slaughter Saint. And I’d asked the Slaughter Saint if he’d had a wet dream!* Teacher Gu Seong-ae. I nearly fucking died because of you. Just as I secretly breathed a sigh of relief, the dense brush around us vanished, and towering cliffs began to come into view. [^1]: *Bossam* is boiled pork commonly served with napa cabbage or other greens for wrapping. [^2]: The Sanzu River is a Buddhist river said to separate the living world from the afterlife.

## Korean source

```text
＃372화



“이곳일세.”

“절벽이네요? 평범한.”

다른 사람들과 함께 가파른 절벽 앞에 멈춰선 나는 주위를 둘러봤다.

백여 장에 달하는 높이와 온통 단단한 암석으로 이루어진 절벽의 풍경은 그리 특별해 보일 것도 없었다.

‘여기에 무슨 진법이 있다고?’

하지만 의문이 해결되는 데까지는 그리 오랜 시간이 필요하지 않았다.

문득 느껴지는 기시감을 따라 천천히 걸어간 나는 황갈색의 암벽 앞에서 걸음을 멈췄다.

“이건…….”

모든 것에는 흐름과 결이 있다. 보이지도, 만질 수도 없는 기운이라고 해도 그 범주를 벗어날 수 없다.

그리고 초절정의 경지에 오르며 진일보한 감각은, 부자연스러운 기의 흐름을 감지해 내기에 충분했다.

“진법(陳法)?”

내 중얼거림에 대답하는 목소리가 있었다.

“정확히는 환영진(幻影陳)이다.”

건조한 눈빛으로 내 얼굴을 훑어본 문경, 아니 살성이 앞으로 나서며 손을 뻗었다.

막대한 기의 움직임과 함께 단단하던 암벽이 안개처럼 사라지고 시커먼 동혈의 입구가 모습을 드러낸다.

“아주 개눈깔은 아니로군.”

“어, 예?”

“되묻지 마라.”

한마디를 툭 흘린 살성은 대꾸할 시간도 주지 않고 동혈을 향해 걸음을 옮겼다.

‘저게 욕이야, 칭찬이야.’

이거 묘하게 기분 나쁘네.

그렇다고 막상 화를 내는 것도 뭐한 것이, 살성의 말과 행동에서는 나에 대한 어떤 악감정도 느껴지지 않았다. 그저 다른 사람들을 대하는 것처럼 무미건조한 딱딱함만이 느껴질 뿐이다.

이러니 듣는 사람으로서는 화가 나기보다 머쓱해질 수밖에.

“…….”

물론 상대가 상대인지라 좋게좋게 넘어가려는 것도 있다.

살성이 그렇다는데 뭐 어쩔 거야. 좀 기분 나쁘더라도 참아야지.

몽정 얘기를 꺼내놓고도 멀쩡히 서 있는 것만으로도 감지덕지다.

‘살성을 쌀성으로 만들어 버릴 뻔했는데, 이 정도면 양반이지.’

그런 생각을 하고 있을 때, 옆에서 낮은 웃음소리가 들려왔다. 고개를 돌려보니 입꼬리를 씰룩거리는 적천강이 보였다.

“갑자기 왜 웃으세요?”

“그냥. 살성 저놈도 어지간히 솔직하지 못한 놈이구나, 하는 생각이 들어서.”

“예?”

“되묻지 마라.”

“……?”

뭐지. 최신 유행어인가.

그 말을 끝으로 휘적휘적 걸어가는 적천강의 뒷모습을 바라보던 나와 두 장문인은 시커먼 동혈을 향해 걸음을 내디뎠다.

‘그나저나…….’

이런 곳이 숨겨져 있었다니.

심지어 사천의 중심인 성도에서 한나절이면 올 수 있는 거리다. 평범한 양민의 걸음으로 한나절이니, 무공을 익힌 이들이라면 말할 것도 없다.

나는 끝없이 이어지는 동굴을 걸으며 주위를 둘러봤다.

‘입구부터 엄청 넓네. 사천당문의 지하 뇌옥보다 몇 배는 더.’

오면서 간략히 들었다. 바로 이 동굴에서 암천의 흉수들이 머물렀다고.

그렇게 많은 숫자가 어디에서 튀어나왔나 했더니, 여기에 숨어서 때를 기다리고 있었던 모양이다.

‘그런데 여기까지는 어떻게 들어온 거지?’

서천마군의 지휘 아래, 당문에 쳐들어온 적들의 숫자만 삼백여 명이다.

거기에 더해 청성과 아미로 향한 놈들까지 합친다면 결코 무시할 수 없는 머릿수가 된다.

‘사천성 치안이 그 정도로 개판인가. 아니, 아무리 그래도 개방과 하오문이라면 알아차렸을 것 같은데.’

한 줄기 의문을 품은 채 얼마나 걸었을까.

장정 열 명이 나란히 걸어도 될 만한 넓은 길이 끝나고 마침내 새로운 공간이 모습을 드러냈다.

그 순간, 나도 모르게 혼잣말이 흘러나왔다.

“……허. 이것 봐라.”

족히 천여 명은 수용하고도 남을 것 같은 면적. 천장에 박힌 수십 개의 야명주(夜明珠)가 은은한 빛을 뿌리고, 한구석에는 건량과 벽곡단이 가득 쌓인 항아리와 병장기 등이 놓였다.

그러나 내가 가장 놀란 것은 따로 있었다.

‘저게 뭐야.’

동굴 바닥 전체를 뒤덮고 있는 기이한 문양들.

마치 정교한 톱니바퀴처럼, 일정한 배치로 새겨진 그것들은 마치 오래전 잊힌 고대 왕국의 유적지 같았다.

“혹시 저게 아까 말씀하신 그……?”

내 물음에 청성파의 장문인인 청풍고검이 무거운 얼굴로 고개를 끄덕였다.

“맞네. 저것이 빈도가 말했던 기이한 진법일세.”

설마 했는데, 진짜 진법이었다니.

성라대연에서 진법을 포함한 각종 기관진식을 겪어 본 적이 있었지만 저만큼 크고, 이상한 건 처음 봤다.

‘이 정도면 기이한 걸 넘어서 기형적인데.’

어쩌면 신비로우면서도 위험해 보이는 문양 때문일지도 모른다.

나와 비슷한 생각을 했는지 적천강이 입을 열었다.

“그런데 저 괴상한 문양은 도대체 뭐지?”

“그것이…… 저희 쪽에서도 아직 알아낸 바가 없습니다.”

청풍고검에 이어 멸절신니가 말을 보탰다.

“지금으로서는 속단할 수 없소. 진법의 일부를 본떠 여러 석학과 명사들에게 보여 주었으나 아는 이가 없더구려. 아무도 모르는 서역(西域)의 문자일 가능성도 완전히 배제할 수 없겠소.”

그런데 그때, 나도 모르게 입술 사이로 한마디가 튀어나왔다.

“어, 이거 문자 아닌데?”

“……?”

“……?”

“……?”

모두의 시선이 나를 향해 쏠렸다. 동굴에 들어온 이래 시종일관 침묵을 지키던 살성이 불쑥 입을 열었다.

“근거는?”

“그, 근거요?”

“그렇게 주장하는 데에는 합당한 근거가 있을 터. 되묻지 말고 대답해라.”

당연히 있다. 수만 권의 책을 독파하며 지식을 쌓은 유명한 학자도, 일평생 무림을 종횡하며 수많은 경험을 한 무림의 명사도 반박할 수 없는 확실한 근거가.

‘통합 언어 팩.’

시스템의 힘으로 모든 언어를 자동으로 통역해 주는 [통합 언어 팩].

이것만 있으면 의사소통은 물론이고 글자를 읽고 쓰는 것까지 아무 문제가 없다.

현대에서 스켈레톤 워로드와 대화를 할 수 있었던 이유도 [통합 언어 팩] 덕분이었다.

그러나 패시브 스킬처럼 상시 적용되는 해석 기능에도 진법을 이루는 문양은 처음 모습 그대로였다. 이건 저 문양이 문자가 아니라는 확실한 근거다.

문제는…….

‘이걸 어떻게 설명하냐.’

괜히 말했다. 그냥 가만히 있을걸.

하지만 이미 너무 늦어 버렸다. 점점 깊어지는 살성의 눈빛에, 나는 더듬더듬 입을 열었다.

“찌, 찌.”

“찌찌?”

쌀성의 눈썹이 꿈틀거렸다. 처음으로 보이는 감정 표현. 몽정 사건을 떠올렸음이 분명하다.

“아, 아니, 찌찌가 아니고요.”

“그럼. 젖인가?”

“…….”

제발. 감정이라고는 한 톨도 느껴지지 않는 얼굴로 그런 말 하지 마.

“아니, 그게 아니고요.”

내가 황급히 손을 내젓던 그때, 적천강이 불쑥 끼어들었다.

“지금 내 제자를 겁박하는 건가? 감히 이 화왕의 후인이자 열화문의 소문주를?”

“겁박이라. 할 필요도 없지만 못 할 것도 없지.”

“우연찮게 구명의 은을 입어 참으려고 했는데, 문가(文家), 네놈이 이리 나온다면 노부도 가만히 있을 수 없지.”

점점 험악해지는 분위기 속. 나는 두 눈을 질끈 감으며 외쳤다.

“찌, 찍었는데요!”

“……!”

“……!”

“……!”

“예전에 책에서 본 것 같기도 하고…… 제 느낌상 글자가 아닌 것 같아서, 찍었습니다.”

순간 내려앉은 고요한 침묵. 들릴락 말락 하게 한숨을 내쉰 살성이 적천강에게 물었다.

“그래서, 저놈이 화왕의 후인이자 열화문의 소문주라고?”

잠시 말이 없던 적천강이 대답했다.

“생각해 보니 정식으로 입문식을 치르진 않았군.”

“…….”

“그러니까 엄연히 따지자면 본문의 정식 제자는 아닌 게지. 즉, 아직까지 이 녀석은 태원진가 소속이라고 봐야…….”

나와 시선이 마주친 적천강이 슬그머니 시선을 회피했다.

“여기까지 하겠네.”

“…….”

뭘 여기까지 해. 이미 할 말 다 해 놓고.

스승과 제자 간의 신뢰가 박살 나는 현장을 눈앞에서 목격한 멸절신니와 청풍고검이 떨떠름한 얼굴로 화제를 돌렸다.

“크흠. 어찌 되었건 이 기이한 진법에 관한 문제는 계속해서 알아봐야 할 것 같소.”

“지, 진 도우와 적 선배님의 고견이 큰 도움이 되었습니다.”

하나도 도움이 안 됐다는 건 하늘도 알고 땅도 알고 여기 있는 모두가 안다.

뒷골목 똥개도 안 믿을 소리로 상황을 일단락한 청풍고검이 그늘진 얼굴로 멸절신니에게 말했다.

“그나저나 참으로 믿을 수 없는 일입니다. 고작 진법으로 그 많은 숫자를 불러오다니. 허, 참.”

“그러게 말이오. 이런 일이 가능하다는 건 천하 각지 어디에서도 놈들이 나타날 수 있다는 것 아니겠소?”

잠깐, 지금 뭐라고?

설명하지 못하는 답답함과 찌찌의 후유증에 땅만 쳐다보고 있던 나는 고개를 번쩍 쳐들었다.

“왜 그러시는가, 진 시주?”

“아니. 방금 두 분께서 진법에 관해 나누신 이야기를 저는 처음 듣는 것 같아서요.”

“음? 이동진(移動陳) 말인가?”

“……이동진이요?”

“그렇다네. 삼괴의 말에 의하면 저 기이한 진법은 이동진이라고 불린다더군. 어디까지 믿어야 할지 알 수 없는 허무맹랑한 소리지만…… 암천은 저 진법을 통해 수백 리 거리를 뛰어넘어 이동했다고 하네.”

이동진. 이동진이라니.

갑자기 각진 뿔테 안경을 쓴 평론가가 걸어 나와서 이 진법의 별점은 네 개 반입니다, 라고 해도 지금만큼 당황스럽진 않을 거다.

‘이거, 어디서 많이 듣던 건데.’

거리를 뛰어넘어 수백 명을 이동시키는 진법이라니.

다시 떠올릴수록 가슴이 거세게 뛰고 입술이 바싹 마른다.

만약, 이동진이라 불리는 이 진법이 지금 내가 생각하고 있는 ‘그것’이라면?

‘아니, 그럴 리가.’

그러나 애써 부정하는 속마음과는 달리, 나도 모르게 목울대가 크게 일렁였다.

“혹시, 이 진법. 지금도 가동되는 겁니까?”

두 장문인을 향한 물음이었지만, 대답이 흘러나온 것은 살성의 입이었다.

“삼괴. 놈을 이곳에서 직접 잡았지.”

“……이동진을 통해 도주하려 했군요.”

“그래. 하지만 그건 놈의 생각일 뿐이었다.”

“그 말씀은…….”

“후에 놈이 실토한 대로 진법을 가동하려 했지만, 아무런 일도 일어나지 않았다.”

“아.”

“한 가지는 확실하지. 저 진법에서는 아무런 기의 흐름도 느껴지지 않는다. 이제는 힘을 완전히 상실한 껍데기에 지나지 않아.”

고저 없는 목소리로 설명을 끝마친 살성이 한 마디를 덧붙였다.

“지금까지 드러난 정황을 보건대, 암천은 틀림없는 마교의 후신(後身)이다. 마교가 보유한 괴공절학(怪功絶學)은 셀 수도 없이 많으니 어떤 기이한 술법이 있다고 한들 이상하지 않지.”

마교가 어떤 곳인지는 오래전부터 귀에 못이 박이도록 들어 왔다.

사마외도(邪魔外道) 그 자체라 할 수 있는 강대한 종교 집단.

비록 최종적으로는 정마대전에서 패배했지만, 상당한 기간 천하 무림을 상대로 압도할 수 있었던 것은 마교가 보유한 괴공절학 덕택이었다.

‘그럼 이 진법도 마교로부터 전해진 수많은 괴공절학 중 하나라고?’

생각해 봐도 도저히 모르겠다. 예전에 봤던 퓨전 판타지 소설에서 자주 나오던 소재라 그런가. 괜히 더 헷갈리는 기분이다.

‘묵형에서는 잘만 넘어가던데. 후, 완결도 안 나는 걸 괜히 봐 가지고.’

그래도 혹시 모르니 진법의 배치와 문양 정도는 외워 두기로 했다.

내가 뚫어져라 이동진을 보며 머릿속에 새겨 나가던 그때, 살성이 문득 입을 열었다.

“네 태도를 보아하니 뭔가 아는 것 같은데. 혹 짚이는 것이라도 있느냐?”

“…….”

이건 뭐라고 변명을 해야 하나.
```

## Current accepted English baseline

```markdown
# Chapter 372

“This is the place.”

“It’s a cliff. A perfectly ordinary one.”

I stopped in front of the steep cliff with the others and looked around.

There was nothing particularly remarkable about it. The cliff rose more than a hundred jang[^1] into the air, and its entire surface was made of solid rock.

*There’s a formation here?*

But it did not take long for my question to be answered.

Following a strange sense of déjà vu, I slowly walked forward and stopped in front of a yellow-brown rock wall.

“This is…”

Everything has a flow and a grain. Even qi, which cannot be seen or touched, cannot escape that principle.

And the senses I had honed by advancing into the Supreme Peak realm were more than enough to detect an unnatural flow of qi.

“A formation?”

A voice answered my mutter.

“More precisely, an Illusion Formation.”

Mungyeong—no, the Slaughter Saint—studied my face with dry eyes, then stepped forward and extended a hand.

With a massive surge of qi, the solid rock wall vanished like mist, revealing the entrance to a pitch-black cavern.

“So your eyes aren’t completely useless after all.”

“Huh?”

“Don’t ask.”

The Slaughter Saint tossed out that one remark, then walked toward the cavern without giving me time to respond.

*Was that an insult or a compliment?*

It left me feeling oddly irritated.

Still, it would have been awkward to get angry when neither the Slaughter Saint’s words nor his actions showed any particular hostility toward me. He was merely as dry and rigid with me as he was with everyone else.

As a result, it was impossible to feel angry. All I could do was feel awkward.

“…”

Of course, the fact that I was trying to let it slide had something to do with who I was dealing with.

If that was how the Slaughter Saint was, what could I do about it? Even if it bothered me, I had to endure it.

The mere fact that I was still standing after bringing up wet dreams was already something to be grateful for.

*I nearly turned the Slaughter Saint into the Spurt Saint. Compared to that, this is downright civilized.*

While I was thinking that, a low chuckle came from beside me. I turned my head and saw Jeok Cheongang’s lips twitching.

“Why are you suddenly laughing?”

“Nothing. I was just thinking that the Slaughter Saint is remarkably bad at being honest about his feelings.”

“Huh?”

“Don’t ask.”

“…”

What was this? Was it some kind of new catchphrase?

After Jeok Cheongang sauntered away, the two Sect Leaders and I walked toward the black cavern.

*More importantly…*

Who would have thought a place like this was hidden here?

It was only half a day’s journey from Chengdu, the heart of Sichuan. That was by the pace of an ordinary commoner, so for martial artists, it would take even less time.

I looked around as I walked through the endless cave.

*The entrance alone is enormous. It’s several times larger than the underground prison beneath the Sichuan Tang Clan.*

I had heard a brief explanation on the way. Dark Heaven’s villains had been staying in this very cavern.

So that was where all those people had come from. They must have been hiding here, waiting for the right moment.

*But how did they get here in the first place?*

Under the command of the Western Heaven Demon Lord, more than three hundred enemies had invaded the Tang Clan alone.

If I added the men who had headed toward Qingcheng and Emei, the number became impossible to ignore.

*Is Sichuan’s security really that terrible? No, even if it was, surely the Beggars’ Sect and the Lower District Sect would have noticed.*

I had been walking with that question in mind for some time when the broad passage—wide enough for ten sturdy men to walk side by side—finally came to an end, and a new space opened before us.

Without meaning to, I muttered,

“…Well, look at this.”

The area was large enough to comfortably accommodate more than a thousand people. Dozens of night-shining pearls embedded in the ceiling cast a soft light, while jars and containers filled with dried provisions and grain-avoiding pills were stacked in one corner alongside weapons and other supplies.

But something else caught my attention far more than any of that.

*What is that?*

Strange patterns covered the entire floor of the cavern.

Engraved in a regular arrangement like elaborate gears, they looked like the ruins of an ancient kingdom forgotten long ago.

“Is that the thing you mentioned earlier…?”

At my question, Clear Wind Ancient Sword, the Sect Leader of the Qingcheng Sect, nodded gravely.

“Yes. That is the strange formation I mentioned.”

I had suspected as much, but it was still astonishing to see that it really was a formation.

I had encountered all kinds of mechanisms and formations at the Star-Netted Grand Banquet, but I had never seen anything so large or so strange.

*At this point, it’s gone beyond strange and become downright malformed.*

Perhaps it was because of the mysterious, dangerous-looking patterns.

Jeok Cheongang seemed to have had the same thought.

“But what in the world are those bizarre patterns?”

“We have not yet determined that ourselves.”

Then Extinction Divine Nun added,

“We cannot jump to conclusions at this point. We copied a portion of the formation and showed it to several renowned scholars and eminent figures, but none of them recognized it. We cannot completely rule out the possibility that it is writing from some unknown region of the Western Territories.”

Then, without meaning to, I blurted out,

“Uh, these aren’t letters.”

“…”

“…”

“…”

Everyone’s eyes turned toward me.

The Slaughter Saint, who had remained silent ever since entering the cavern, suddenly spoke.

“Your basis?”

“M-my basis?”

“If you claim that, you must have a reasonable basis. Answer without asking another question.”

Of course I did. I had a firm basis that neither a renowned scholar who had built up knowledge by reading tens of thousands of books nor an eminent martial artist who had spent a lifetime roaming the Murim and gathering countless experiences could refute.

*The Integrated Language Pack.*

The Integrated Language Pack automatically translated every language through the power of the System.

With it, I could communicate without difficulty, and I could also read and write.

It was thanks to the Integrated Language Pack that I had been able to converse with the Skeleton Warlord in the modern world.

Yet even though its translation function was always active like a passive Skill, the patterns making up the formation remained exactly as they were.

That was conclusive proof that the patterns were not writing.

The problem was…

*How am I supposed to explain that?*

I shouldn’t have said anything. I should have just kept my mouth shut.

But it was already too late. As the Slaughter Saint’s gaze grew more intense, I stammered,

“J-j…”

“Jugs?”

The Spurt Saint’s eyebrow twitched. It was the first emotion I had seen from him. He had clearly remembered the wet-dream incident.

“N-no, not jugs.”

“Then what? Breasts?”

“…”

Please. Don’t say things like that with a face that doesn’t show a single hint of emotion.

“No, that’s not what I meant.”

Just as I frantically waved my hands, Jeok Cheongang suddenly cut in.

“Are you threatening my disciple? How dare you threaten the heir of the Fire King and the Young Sect Leader of the Fire Gate Clan?”

“Threatening him? There is no need for that. But it is not beyond my ability.”

“I was trying to hold back because I owe you my life, but if you, Wen, are going to act like this, this old man cannot sit back and do nothing.”

The atmosphere grew increasingly hostile.

I squeezed my eyes shut and shouted,

“I—I guessed!”

“…”

“…”

“…”

“I think I saw it in a book once… It just felt like it wasn’t writing, so I took a guess.”

A deep silence descended.

The Slaughter Saint let out a nearly inaudible sigh, then asked Jeok Cheongang,

“So that man is the Fire King’s heir and the Young Sect Leader of the Fire Gate Clan?”

Jeok Cheongang was silent for a moment before answering.

“Now that I think about it, he never went through a formal initiation ceremony.”

“…”

“So, strictly speaking, he isn’t an official disciple of our sect. That means he still belongs to the Jin Family of Taiyuan—”

Jeok Cheongang’s eyes met mine. He quietly looked away.

“We’ll stop here.”

“…”

What did he mean, stop here? He had already said everything there was to say.

Extinction Divine Nun and Clear Wind Ancient Sword, who had just witnessed the trust between master and disciple being utterly destroyed, awkwardly changed the subject.

“Ahem. In any case, it seems we will have to continue investigating this strange formation.”

“Y-yes. Fellow Daoist Jin and Senior Jeok’s insights were a great help.”

Everyone here, along with heaven and earth, knew that they had not helped at all.

Even a stray dog in a back alley would not have believed that, but Clear Wind Ancient Sword used it to bring the situation to an end before speaking to Extinction Divine Nun with a troubled expression.

“More importantly, this is truly unbelievable. To bring that many people here with nothing but a formation… My goodness.”

“Indeed. If such a thing is possible, does that not mean they could appear anywhere across the land?”

Wait. What did he just say?

I had been staring at the ground, frustrated by my inability to explain myself and still suffering the aftereffects of the boob incident. I suddenly jerked my head up.

“What’s the matter, Benefactor Jin?”

“No. I think this is the first time I’ve heard what you two just said about the formation.”

“Hm? You mean the Transportation Formation?”

“…The Transportation Formation?”

“That is what Samgoe called it. According to him, that strange formation is a Transportation Formation. It is an absurd claim, and we have no way of knowing how much of it to believe, but he said Dark Heaven used it to cross hundreds of li.”

A Transportation Formation. He said a Transportation Formation.

Even if a critic wearing angular horn-rimmed glasses had suddenly walked over and said, “I give this formation four and a half stars,” I would not have been any more bewildered than I was now.

*This sounds familiar.*

A formation capable of moving hundreds of people across hundreds of li.

The more I thought about it, the harder my heart pounded and the drier my lips became.

*What if this formation called the Transportation Formation was that thing I was thinking of?*

*No. That couldn’t be.*

But despite my desperate attempts to deny it, my throat bobbed heavily.

“Is this formation still operational?”

I had directed the question at the two Sect Leaders, but the answer came from the Slaughter Saint.

“Samgoe. I caught him here myself.”

“…He tried to escape through the Transportation Formation.”

“Yes. But that was only what he intended to do.”

“What do you mean?”

“As he later confessed, he tried to activate the formation. Nothing happened.”

“Ah.”

“One thing is certain. There is no flow of qi coming from that formation. It has completely lost its power. Now it is nothing more than an empty shell.”

After explaining that in his level voice, the Slaughter Saint added,

“Judging by the circumstances revealed so far, Dark Heaven is unquestionably a successor of the Demonic Cult. The Demonic Cult possesses countless bizarre and supreme arts. It would not be strange for them to have any number of strange techniques.”

I had heard what kind of place the Demonic Cult was so many times that the words had practically been hammered into my ears.

A powerful religious organization that was the very embodiment of evil, demonic, and heretical ways.

Although it had ultimately lost the Great Faction War, the Demonic Cult had been able to overwhelm the Murim for a considerable period thanks to its bizarre and supreme arts.

*Then this formation is one of the countless strange arts passed down from the Demonic Cult?*

No matter how much I thought about it, I could not figure it out. Maybe it was because this was such a common device in the fusion-fantasy novels I had read before. It only made me more confused.

*It worked just fine in Muk-hyeong.[^2] Sigh. I shouldn’t have bothered reading something that never even got an ending.*

Still, just in case, I decided to memorize the formation’s layout and patterns.

As I stared intently at the Transportation Formation and carved every detail into my memory, the Slaughter Saint suddenly spoke.

“Judging by your attitude, you seem to know something. Does anything come to mind?”

“…”

What excuse was I supposed to make now?

[^1]: A *jang* is a traditional East Asian unit of length, roughly ten feet.

[^2]: *Muk-hyeong* is the title of a fusion-fantasy novel Jin Taekyung has read.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 372`.

# Master Edit Task — Chapter 371

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
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 살성     | **Slaughter Saint**           | —              |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 신법     | **movement technique**                           |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 가주     | **Family Head**                              |
| 장문인    | **Sect Leader**                              |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 스킬               | **Skill**                      |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 도사      | **Daoist**                                                      |
| 궁기방 | **Gung Gibang** | Young beggar and Future Beggar Chief. |
| 문경 | **Mungyeong** | Young Disciple of the Divine Physician overseeing Jin Taekyung's care. |
| 사천당문 | **Sichuan Tang Clan** | The Tang family and clan of Sichuan |
| 당사독 | **Tang Sadok** | Poison King and Family Head of the Sichuan Tang Clan |
| 경천신니 | **Heaven-Shaking Divine Nun** | Murder victim named alongside Tang Sadok |
| 삼괴 | **Samgoe** | Principal culprit being escorted to Henan |
| 구파일방 | **Nine Sects and One Gang** | Major orthodox organizations |
| 서천마군 | **Western Heaven Demon Lord** | Major obstacle recently overcome by Taekyung |
| 미미 | **Mimi** | Tang Sadok's snake and longtime companion; temporarily entrusted to Cheongpung. |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 아미파 | **Emei Sect** | Orthodox sect whose nuns conduct the funeral rites. |
| 청성파 | **Qingcheng Sect** | Orthodox sect represented among the assisting martial artists. |
| 열화신룡 | **Blazing Fire Divine Dragon** | New epithet acquired by Jin Taekyung. |
| 청풍고검 | **Clear Wind Ancient Sword** | Sect Leader of the Qingcheng Sect; epithet of the old Daoist. |
| 멸절신니 | **Extinction Divine Nun** | New Sect Leader of the Emei Sect after the death of the Heaven-Shaking Divine Nun. |
| 천주 | **Heavenly Lord** | Being worshiped as a god by Dark Heaven's fanatics. |
| 혈주 | **Blood Lord** | Dark Heaven figure whose power and abilities are recalled by Jin Taekyung. |
| 열화동 | **Blazing Fire Cave** | Cave at Mount Jiuhua containing an advanced arcane formation. |
| 진성애 | **Jin Seong-ae** | Jin Taekyung's joking title for himself as a sex-education teacher. |
| 구성애 | **Gu Seong-ae** | Real-world sex-education teacher referenced in Jin Taekyung's joke. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 궁기방 | orthodox_ally_to_orthodox_ally | Young Hero Gung | blunt-but-formal | Uses 궁 소협 while teasing Gung Gibang about his injuries. |
| 혁무진 | 청풍 | junior_ally_to_younger_ally | Young Hero Cheong | formal-but-bewildered | Uses 청 소협 when reacting to Cheongpung's warning. |
| 혁무진 | 진태경 | subordinate_to_squad_leader | Squad Leader | deferential | Calls Taekyung 조장님 when announcing his awakening. |
| 궁기방 | 진태경 | squadmate_to_squad_leader | Jin Taekyung | familiar-but-direct | Calls Taekyung by name when he wakes. |
| 진태경 | 청풍고검 | junior_to_elder_sect_leader | Perfected One | respectful-formal | Uses 진인 when greeting the Qingcheng Sect Leader. |
| 청풍고검 | 진태경 | elder_sect_leader_to_junior_ally | Fellow Daoist Jin | respectful-but-familiar | Uses 진 도우 when greeting Taekyung. |
| 멸절신니 | 진태경 | elder_sect_leader_to_benefactor | Benefactor Jin | respectful-formal | Uses 진 시주 when greeting Taekyung. |
| 멸절신니 | 적천강 | orthodox_elder_to_orthodox_elder | Benefactor Jeok | respectful-but-familiar | Uses 시주 when responding to Jeok Cheongang. |
| 진태경 | 적천강 | disciple_to_elder_master | Old Man | casual-but-affectionate | Uses 노야 while thanking Jeok Cheongang. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |

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

## Korean source

```text
＃371화



“열화신룡(烈火神龍) 진태경 대협을 뵙습니다!”

경외를 담은 외침이 사천당문의 경내에 울려 퍼진 그 순간, 전율을 느낀 것은 진태경 한 사람뿐만이 아니었다.

멀리서 모든 광경을 지켜보던 늙은 스승은 벅차오르는 감정을 숨기기 위해 안간힘을 써야 했다.

‘녀석…….’

적천강은 진태경을 처음 만난 날을 또렷이 기억하고 있었다.

변방 무가의 삼공자. 이제 갓 산서 땅에서 이름을 알리기 시작했던 어린 청년은 잠룡이 되었고, 마침내 날개를 활짝 펴고 푸른 하늘로 비상하고 있었다.

‘그래, 네 녀석이야말로 신룡(神龍)이요, 대협(大俠)이다.’

눈이 마주치자 씩 웃는 진태경의 얼굴이 보인다. 창밖으로 상반신을 내민 그가 두 손을 미친 듯이 휘저었다.

“내 이름이 뭐라고?”

“진태경!”

“별호는 뭐라고!”

“열화신룡!”

“더 크게 소리 질러-!”

“와아아아아!”

엄숙하던 장내가 한 번에 뒤집어지며 광란의 도가니로 변하는 광경에, 적천강은 참았던 웃음을 터트렸다.

“으하, 으하하하!”

시원한 웃음소리와 함성이 뒤섞인다. 바람은 시원했고 하늘은 맑았다.

바야흐로 난세(亂世)의 시작이었으나, 새로운 영웅이 태동하던 그 날은 따스한 봄이었다.



* * *



적천강이 나타난 것은 광란의 도가니가 가라앉은 직후였다.

“좁쌀만 한 방에 많이도 모여 있구나.”

“어? 하나도 안 좁은데요?”

“적 대협, 저쪽에 빈자리가 있습니다.”

눈치라고는 죽었다가 깨어나도 없는 청풍이나 혁무진과는 달리, 뼛속까지 성골 거지인 궁기방은 즉각 움직였다.

“어이구, 그러고 보니까 좁아서 미어터질 것 같네요. 저는 나가 있겠습니다.”

청풍과 혁무진이 손을 흔들어 주었다.

“잘 가요, 궁 소협.”

“저 양반 드디어 가네. 조장, 아까부터 어디서 똥개 궁둥이 냄새 나지 않았습니까?”

나는 조심스럽게 고개를 끄덕였다.

“어, 조금 심하게 나긴 하더라…….”

“개소리 그만하고 둘 다 나와!”

“아니, 진짜 났다니까…….”

“알겠어요. 그렇게 화내지 마세요, 궁 소협.”

벌컥 성을 내는 궁기방의 모습에 청풍이 시무룩한 얼굴로 고개를 숙였다.

“미미. 회오리 치기 하면서 인사.”

취릭. 취리리릭!

“……뭐여, 시벌.”

그사이 스킬이 늘었네. 화려한 퍼포먼스를 보여 준 청풍이 마지막으로 방을 나서자 적천강이 입을 열었다.

“천둥벌거숭이 같으니. 아주 한바탕 난리를 치더구나.”

굳은 얼굴과 착 가라앉은 목소리. 참 여전하다. 평소의 적천강 같아서 왠지 웃음이 나왔다.

“웃어?”

“그럼 웃지, 웁니까?”

“허, 이놈 보게나. 사람들 앞에서 추태를 부려 본문의 명성에 먹칠을 해 놓고도 그런 말이 나오느냐?”

“그렇게 생각하신 것치고는 엄청 크게 웃으시던데.”

“……!”

“다 봤어요.”

애써 유지하던 굳은 표정이 와르르 무너졌다. 적천강의 고개가 슬그머니 창밖을 향해 돌아갔다.

“크흠. 보긴 뭘 봤단 말이더냐.”

“저 말고도 오십 명쯤은 봤을걸요. 입꼬리에서 피 나시는 줄.”

거의 차이나 조커 수준이었지.

도무지 빠져나올 틈을 주지 않는 내 확인 사살에, 한참이나 머뭇거리며 말을 잇지 못하던 적천강이 한마디를 툭 내뱉었다.

“……했다.”

“예?”

“아, 잘했다고!”

벌겋게 달아오른 얼굴로 외친 적천강이 작게 툴툴거린다.

그 모습에 내 입가에 맺힌 웃음이 더욱 짙어졌다. 그래, 그 한마디면 충분하다.

“감사합니다. 전부 노야 덕분이에요.”

“…….”

뭐지? 어째 표정이 심상치 않다.

섭섭함마저 느껴지는 눈빛에 황당해진 내가 물었다.

“이번엔 또 왜요?”

“아니다. 아무것도.”

“그런 것치곤 표정이 어째 좀…….”

“아니라니까!”

“아니, 왜 소리를 지르고 그러세요? 오랜만에 분위기 훈훈하고 좋았는데.”

“거, 아니라면 아닌 줄 알 것이지. 네 녀석이 자꾸 꼬치꼬치 캐물으니까 이러는 것 아니냐!”

“어어, 점점?”

이 양반 갑자기 왜 이래. 내가 무슨 실수라도 했나?

어리둥절해서 고개를 갸웃거리던 그때였다.

스슥.

계단을 올라오는 두 개의 인기척.

벽을 넘어서며 한층 더 예민해진 감각이 아니었다면 쉽게 알아차리지 못했을 만큼, 그들의 걸음은 가볍고 표횰했다.

‘둘 다 엄청난 고수들이다.’

갑자기 초절정의 고수가 둘씩이나?

최근 들어 많은 위기를 겪은 탓에 이제는 몸이 저절로 움직였다.

그런데 적천강이 주먹을 말아쥐는 나를 눈짓으로 만류하더니 손을 내저었다. 한 줄기의 열풍이 닫혀 있던 문을 부드럽게 열어젖혔다.

“다들 성질도 급하군. 일각도 못 기다리고 우르르 몰려와?”

적천강의 불퉁한 목소리에 늙은 여승과 도사가 차례대로 대답했다.

“성질이 급하다니. 시주에게 들으니 기분이 참 묘해지는구려.”

“후배가 결례를 저질렀습니다. 다만 사안이 사안인지라.”

쪼글쪼글한 주름이 가득한 늙은 여승은 초면이었지만, 도사가 누군지는 금방 알아볼 수 있었다.

나는 노고사를 향해 포권을 취했다.

“안녕하십니까. 진인(眞人).”

“다시 보니 반갑네. 진 도우.”

노도사의 정체는 일전에 신의를 찾기 위해 도움을 청하러 간 청성파의 장문인인 청풍고검(淸風高劍)이었다.

‘그럼 이 여승이 아미파의 장문인일 텐데…… 누구지?’

나도 이제 무림 짬밥이 좀 되다 보니 유명한 고수에 관한 것들은 어느 정도 알고 있는데, 남의 문파 사정까지 속속들이 꿰고 있을 정도는 아니었다.

경천신니의 죽음 이후 새로 취임한 장문인의 경우에는 더더욱.

내 생각을 읽은 듯, 적천강이 넌지시 전음을 보냈다.

- 그 할망구는 아미파의 멸절신니(滅絶神尼)다. 보기에는 인자해 보여도 한 번 눈이 뒤집히면 나찰이 따로 없으니 언행에 특별히 신경 써라. 특히 나이에 관해서는 입도 벙긋하지 말고.

나도 조심스럽게 전음으로 응수했다.

- 춘추가 어떻게 되시길래.

- 노부보다 많다. 경천신니의 사고이기도 하지.

- 아.

적천강의 정확한 나이는 모르지만, 백 세를 넘겼다는 것만은 안다. 거기에 더해 별호에서 느껴지는 포스까지.

나는 보쌈집 회장님 같아 보이는 왕 할머니에게 넙죽 허리를 숙였다.

“안녕하십니까! 진태경이라고 합니다!”

“반갑네, 진 시주.”

묘한 눈빛으로 나를 응시하던 멸절신니가 고개를 끄덕였다.

“소문대로군. 아니, 그 이상이야.”

청풍고검이 희미하게 웃으며 말을 받았다.

“실로 놀랍지 않습니까.”

“장강후랑추전랑(長江後浪推前浪). 장강의 뒷물결이 이 늙은이들까지 밀어내려 하는구려. 이토록 어린 나이에 벽을 넘어서다니…….”

“그뿐만이 아닙니다, 신니. 청풍이라는 젊은이도 있지요.”

“아, 그 검성의 후인이라는?”

“예. 빈도가 부족한 탓에 우열을 가릴 수는 없겠으나, 두 젊은이 모두 하늘이 내린 인물들이 확실합니다. 무림의 큰 흥복이지요.”

“호오…….”

피곤함이 묻어나던 두 사람의 얼굴 위로 흥미와 놀라움이 스친다.

어쩐지 민망해져서 눈동자만 굴리고 있던 그때, 적천강이 내 앞을 슥 가로막았다.

그래 봤자 키 차이가 워낙 나서 달라질 것도 없었지만.

“애 얼굴 닳겠소. 할 말이나 후딱 하고 가.”

퉁명스러운 말에 머쓱해진 두 장문인이 본론을 꺼내 들었다.

“문제가 생겼네. 두 사람 모두 잠시 동행해 줄 수 있겠나?”

“오래 걸리지 않을 겁니다. 약속드리지요.”

“동행? 지금 당장?”

탐탁지 않은 목소리로 되물은 적천강이 돌아서며 내게 물었다.

“어찌하겠느냐?”

“…….”

구파일방의 두 장문인이 부탁하는데 나보고 뭘 어쩌라고.

“가겠습니다.”

어차피 몸도 가뿐하겠다, 동행하면서 지금까지의 전후 사정을 들을 수 있을 테니 딱히 거절할 이유가 없었다.

내 흔쾌한 대답에 두 장문인이 앞장서서 걸음을 떼는데, 적천강이 불쑥 입을 열었다.

“그런데, 한 놈은 왜 안 보여?”

“아래에서 기다리고 있다네.”

“다른 사람들 눈에 띄기 싫다 하시더군요.”

한 놈? 이 멤버에 낄 정도면 당문의 가주인 당사독인가?

‘뭐, 누구건 곧 보게 되겠지.’

하지만 내 궁금증은 전각을 나서자마자 마주친 한 사람에 의해 씻은 듯이 사라졌다.

낯익은 얼굴을 보자 절로 반가움이 담긴 외침이 터져 나왔다.

“야, 인마! 문경!”

문경은 사천당문을 떠나기 전의 모습 그대로였다.

안 그래도 녀석이 떠난 지 얼마 되지 않아 암천이 쳐들어온 탓에 걱정이 들었는데, 길이 엇갈렸는지 용케도 다치지 않았다.

“언제부터 와 있었어? 이 자식 이거, 못 본 사이에 키가 더 커진 것 같네. 요즘 성장기냐?”

“…….”

“왜 이렇게 말이 없어. 기분 안 좋아? 혹시…….”

문경의 머리를 쓱쓱 헤집던 나는 숨죽여 속삭였다.

“아침에 몽정했냐?”

“……!”

“했네. 했어.”

짜식, 부끄러워서 아무 말도 안 하는 것 봐라.

나는 흐뭇하게 웃었다.

원래 저 나이대에는 종종 있는 일이다. 이참에 이 케케묵은 무림에 올바른 성 지식을 전파하는 것도 좋겠지.

“이 형님이 신세계를 알려 주마. 앞으로 진성애 선생님이라고 불러라.”

구성애 선생님. 보고 계십니까. 당신의 지식이 시공을 넘어 전해지고 있습니다.

뿌듯한 감정을 느끼며 문경의 어깨를 탁탁 두드리던 그 순간이었다.

“어…….”

“그…….”

“허어…… 저걸 말 안 해 줬네.”

말 안 해 주다니. 뭘?

등 뒤에서 들려오는 세 사람의 장탄식. 동시에 문경의 입술 사이로 무미건조한 음성이 흘러나왔다.

“손. 치워라.”

“……어?”

“그리고 몽정은 오래전에 끝났다.”

“그건 좀 문제가 있는데, 왜냐하면 네가 아직 이차 성징이 완전히 안 끝났……이 아니라.”

나는 침을 꼴깍 삼켰다.

문득, 어떤 무서운 상상이 뇌리를 스쳤기 때문이었다.

“누구……세요?”

엄마, 나 무서워.



* * *



“……해서, 이렇게 된 걸세.”

“참으로 해괴한 일이지.”

엄청난 속도로 신법을 발휘하는 와중에도 두 장문인의 목소리는 흔들리지 않았다.

대답을 요구하는 눈빛에, 나는 힘겹게 입술을 뗐다.

“아, 예. 그래서 지금 가는 곳에 그 뭐냐. 요상한 진법이 있다는 거죠?”

“삼괴(三怪)를 붙잡아 심문한 바에 의하면 그렇다네. 한데 그 진법이라는 것이 워낙 기이해서 말이지.”

적천강이 퉁명스러운 목소리로 대꾸했다.

“노부나 이놈이나, 진법에는 영 젬병이라 봐 봤자 몰라.”

동감이다. 구화산의 열화동은 대단한 기문진식이 설치되어 있지만, 그렇다고 해서 우리가 능통한 것은 아니니까.

‘차라리 제갈세가 같은 곳을 불러야지.’

하지만 제갈세가가 오려면 상당한 시일이 소요될 것이다.

왜인진 몰라도 두 장문인은 우리에게 상당한 기대를 하고 있는 모양이었다. 그중에서도 특히 내게.

“진 도우. 그자에게서 더 이상한 점을 느끼지 못했나? 어떤 언행이라든지.”

“말씀드린 게 전붑니다. 그리고 제가 느끼기에…… 거기서 더 이상해질 것도 없어요.”

암천은 존재 자체가 이상한 놈들이다. 천주라는 존재를 거의, 아니 그냥 신으로 떠받드는 광신도들.

혈주나 서천마군이 보여 준 힘과 기이한 능력들 역시 마찬가지다.

‘인간 트롤마냥 재생하지를 않나, 팔에 양면테이프라도 붙였는지 뗐다 붙이고. 마지막에는 빙의까지 했지.’

생각할수록 기적이다. 그런 놈들을 상대로 싸워서 이겼다는 게.

“으음. 우선 자네가 깨어나기 전 적 시주에게 대략적인 상황은 모두 들었네. 하남으로 보낸 전서응이 답신을 갖고 돌아오면 방향이 잡히겠지.”

“혹시 모르니 진법을 보고 이상한 점이 있다면 알려 주게.”

“예.”

나는 대답하면서 힐끔 저 멀리 앞서나가는 신형을 바라보았다.

문경, 아니 살성(殺聖)이라는 별호를 가진 그를.

‘시벌, 살성이 여기서 왜 나와.’

솔직히 말해서 오줌 쌀 뻔했다.

삼도천 계곡에서 반나절쯤 물놀이 하다가 고기까지 구워 먹고 와도 이 정도는 아닐 거다.

‘문경이 살성이었다니. 내가 살성한테 몽정했냐고 물어봤다니!’

구성애 선생님. 선생님 때문에 뒤질 뻔했습니다.

남몰래 안도의 한숨을 내쉬던 바로 그때, 울창하던 주위의 풀숲이 사라지고 높이 솟은 절벽이 보이기 시작했다.
```

## Current accepted English baseline

```markdown
# Chapter 371

“We pay our respects to Great Hero Jin Taekyung, the Blazing Fire Divine Dragon!”

At the moment that cry, filled with awe, rang throughout the grounds of the Sichuan Tang Clan, Jin Taekyung was not the only one who felt a shiver.

The old master watching everything from far away had to struggle with all his might to hide the emotions welling up inside him.

*You rascal…*

Jeok Cheongang remembered the day he had first met Jin Taekyung as clearly as yesterday.

The Third Young Master of a frontier martial family. The young man who had only just begun making a name for himself in Shanxi had become a hidden dragon, and at last he was spreading his wings wide and soaring into the blue sky.

*Yes. You are the Divine Dragon and the Great Hero.*

Their eyes met, and Jeok Cheongang saw Jin Taekyung grinning at him. Leaning his upper body out through the window, he waved both hands like a madman.

“What’s my name?”

“Jin Taekyung!”

“What’s my epithet?”

“Blazing Fire Divine Dragon!”

“Shout it louder—!”

“Waaaaaaah!”

The solemn courtyard was overturned in an instant, transforming into a cauldron of madness. Jeok Cheongang finally let out the laughter he had been holding back.

“Ha! Hahaha!”

His hearty laughter mingled with the cheers. The breeze was cool, and the sky was clear.

It was the beginning of an age of chaos, but the day a new hero began to emerge was warm with spring.

* * *

Jeok Cheongang appeared just after the cauldron of madness had settled down.

“So many millet grains gathered in a room this small.”

“Huh? It isn’t cramped at all.”

“Great Hero Jeok, there’s an empty seat over there.”

Unlike Cheongpung and Hyuk Mujin, who wouldn’t know how to read the room even if they died and came back to life, Gung Gibang—a blue-blooded beggar to the bone—moved at once.

“Oh, now that you mention it, it is so cramped that we’re about to burst. I’ll step outside.”

Cheongpung and Hyuk Mujin waved him off.

“Goodbye, Young Hero Gung.”

“That guy’s finally leaving. Squad Leader, haven’t you smelled a stray dog’s ass around here since earlier?”

I cautiously nodded.

“Yeah, it did smell pretty bad…”

“Stop talking shit and both of you get out!”

“No, I’m telling you, it really did smell…”

“All right. Don’t get so angry, Young Hero Gung.”

At Gung Gibang’s sudden outburst, Cheongpung lowered his head with a sullen expression.

“Mimi. Say hello while doing a whirlwind spin.”

Sssrik. Sssrrrikkk!

“…What the fuck?”

His Skill repertoire had grown while I wasn’t looking.

After Cheongpung finally left the room following that flashy performance, Jeok Cheongang spoke.

“You reckless brat. You really caused quite a scene.”

His face was stern, and his voice had sunk low. Just like always. He seemed so much like his usual self that I felt like laughing.

“You’re laughing?”

“Why wouldn’t I laugh? Should I cry?”

“Look at this rascal. You made a spectacle of yourself in front of all those people and tarnished our sect’s reputation, yet you still have the nerve to say that?”

“You were laughing awfully loudly for someone who thought that.”

“……!”

“I saw everything.”

The stern expression he had desperately maintained collapsed all at once. Jeok Cheongang’s head slowly turned toward the window.

“Ahem. What do you mean, you saw something?”

“About fifty people besides me probably saw it too. I thought your mouth was bleeding from how far the corners of it had risen.”

You looked practically like the China Joker.

My confirmation kill left him no room to escape. Jeok Cheongang hesitated for a long while before finally tossing out a single word.

“…You did well.”

“Pardon?”

“Ah, I said you did well!”

Jeok Cheongang shouted with a face flushed bright red, then grumbled under his breath.

The smile around my lips deepened. Yes, those few words were enough.

“Thank you. It was all thanks to you, Old Man.”

“……”

What was this? His expression seemed rather strange.

His eyes even looked hurt. Dumbfounded, I asked,

“What is it this time?”

“It’s nothing. Nothing at all.”

“For something that’s nothing, your expression looks a little…”

“I said it’s nothing!”

“Why are you shouting? It was nice having such a warm, friendly atmosphere for once.”

“If I say it’s nothing, then take it as nothing. You’re the one making me act this way by interrogating me over every little thing!”

“Whoa. It’s getting worse.”

What was wrong with him all of a sudden? Had I made some kind of mistake?

It was just then, while I was tilting my head in confusion, that I sensed it.

Swish.

Two presences were coming up the stairs.

Their footsteps were so light and elusive that I would never have noticed them if my senses had not become even keener after crossing the wall.

*They’re both incredible masters.*

Two Supreme Peak masters all of a sudden?

After enduring so many dangers recently, my body now moved on its own.

But just as I clenched my fists, Jeok Cheongang restrained me with a glance and waved his hand. A strand of scorching wind gently pushed open the closed door.

“You’re all so impatient. Couldn’t you wait even a quarter of an hour before swarming over here?”

In response to Jeok Cheongang’s gruff voice, an old nun and a Daoist answered in turn.

“Impatient, you say? Hearing that from a benefactor gives me a rather strange feeling.”

“This junior has been discourteous. However, given the matter at hand…”

The old nun, whose face was covered in countless wrinkles, was a stranger to me. The identity of the Daoist, however, was easy enough to recognize.

I raised my hands in a fist-and-palm salute toward the old Daoist.

“Greetings, Perfected One.”

“Good to see you again, Fellow Daoist Jin.”

The old Daoist was the Sect Leader of the Qingcheng Sect, the Clear Wind Ancient Sword, whom I had once visited to ask for help finding the Divine Physician.

*Then this nun must be the Sect Leader of the Emei Sect… but who is she?*

I had been in the Murim long enough to know a fair amount about famous masters, but I was nowhere near familiar enough with every detail of other sects’ affairs.

Especially not the identity of the Sect Leader who had taken office after the death of the Heaven-Shaking Divine Nun.

As if he had read my thoughts, Jeok Cheongang sent me a quiet Sound Transmission.

—That old hag is the Emei Sect’s Extinction Divine Nun. She looks kind enough, but once she sees red, there’s no difference between her and a rakshasa, so watch your words and actions carefully. And especially don’t say a word about her age.

I cautiously replied through Sound Transmission.

—How old is she, exactly?

—Older than this old man. She was also the Heaven-Shaking Divine Nun’s martial aunt.

—Ah.

I did not know Jeok Cheongang’s exact age, but I knew he was over a hundred. And then there was the force suggested by her epithet.

I bowed deeply to the ancient granny who looked like the chairwoman of a bossam restaurant.[^1]

“Greetings! My name is Jin Taekyung!”

“Good to meet you, Benefactor Jin.”

The Extinction Divine Nun studied me with an odd look, then nodded.

“Just as the rumors say. No—you’re even more impressive.”

The Clear Wind Ancient Sword answered with a faint smile.

“Isn’t it truly astonishing?”

“The waves behind the Yangtze push the waves ahead. It seems the younger generation means to push even us old people aside. To cross the wall at such a young age…”

“That is not all, Divine Nun. There is also a young man named Cheongpung.”

“Ah, the one said to be the Sword Saint’s heir?”

“Yes. This poor Daoist is too inadequate to judge which of them is superior, but both young men are unquestionably people blessed by Heaven. They are a great blessing to the Murim.”

“Oh…”

Interest and astonishment passed over the two leaders’ weary faces.

I was rolling only my eyes, growing increasingly embarrassed, when Jeok Cheongang stepped in front of me.

It did not make much difference, considering the enormous difference in our heights.

“You’ll wear the boy’s face out. Say what you came to say and be off.”

Embarrassed by his brusque words, the two Sect Leaders brought up the matter at hand.

“A problem has arisen. Could you both accompany us for a while?”

“It will not take long. I promise you.”

“Accompany you? Right now?”

Jeok Cheongang turned away with an unhappy expression and asked me,

“What will you do?”

“……”

Two Sect Leaders of the Nine Sects and One Gang were asking me for a favor. What exactly did they expect me to do?

“I’ll go.”

I felt perfectly fine, and accompanying them would let me hear what had happened, so I had no particular reason to refuse.

The two Sect Leaders readily turned and began walking ahead. Then Jeok Cheongang suddenly spoke.

“But why can’t I see one of them?”

“He is waiting downstairs.”

“He said he did not want to attract the attention of the others.”

*One of them? If someone important enough to join this group is here, could it be Tang Sadok, the Family Head of the Tang Clan?*

*Well, whoever it is, I’ll be seeing him soon enough.*

But my curiosity vanished without a trace the moment I stepped out of the pavilion and encountered one person.

The familiar face drew a delighted shout from me.

“Hey, you bastard! Mungyeong!”

Mungyeong looked exactly as he had before leaving the Sichuan Tang Clan.

Dark Heaven had invaded soon after he left, so I had been worried. By some stroke of luck, our paths must have missed each other, and he had not been hurt.

“When did you get here? Damn, you look even taller than before. Are you going through a growth spurt?”

“……”

“Why are you so quiet? In a bad mood? Or maybe…”

I mussed Mungyeong’s hair, then whispered,

“Did you have a wet dream this morning?”

“……!”

“You did. You definitely did.”

Look at the brat, staying silent because he was embarrassed.

I smiled in satisfaction.

It was something that happened from time to time at that age. Maybe I should use this opportunity to spread proper sex education through this stale old Murim.

“This hyung of yours will show you a whole new world. From now on, call me Teacher Jin Seong-ae.”

Teacher Gu Seong-ae, are you watching? Your knowledge is crossing space and time.

I was patting Mungyeong’s shoulder with a swell of pride when it happened.

“Uh…”

“The…”

“Good grief… We forgot to tell him that.”

Forgot to tell me what?

Three long sighs came from behind me. At the same time, a dry voice slipped between Mungyeong’s lips.

“Take your hand off.”

“…Huh?”

“And the wet dreams ended a long time ago.”

“That’s a little concerning, because you still haven’t completely finished your secondary sexual development—no, that’s not what I mean.”

I swallowed hard.

A horrifying thought suddenly flashed through my mind.

“Who… are you?”

*Mom, I’m scared.*

* * *

“…and that is how things came to be.”

“A truly bizarre affair.”

Even while using their movement techniques at tremendous speed, the voices of the two Sect Leaders did not waver.

When they looked at me as though demanding an answer, I managed to part my lips.

“Ah, yes. So the place we’re heading to has some kind of strange formation, right?”

“According to what we learned by capturing and interrogating Samgoe, that is the case. But the formation itself is so strange…”

Jeok Cheongang answered in a gruff voice.

“This old man and this brat are both hopeless with formations. Even if we look at it, we won’t know anything.”

I agreed. Mount Jiuhua’s Blazing Fire Cave had an impressive arcane formation installed, but that did not mean we were experts in such things.

*We should call in someone like the Zhuge Clan instead.*

But it would take a considerable amount of time for the Zhuge Clan to arrive.

For some reason, the two Sect Leaders seemed to be placing considerable expectations on us. Especially on me.

“Fellow Daoist Jin. Did you notice anything stranger about that man? Something in his words or actions?”

“That’s everything I told you. And from what I could tell… there wasn’t much room for him to get any stranger.”

Dark Heaven’s people were weird by their very existence. They were fanatics who practically—or rather, simply—worshiped a being called the Heavenly Lord as a god.

The powers and bizarre abilities displayed by the Blood Lord and the Western Heaven Demon Lord had been just as strange.

*Regenerating like a human troll, detaching and reattaching an arm as if it had double-sided tape on it—and to top it all off, even possession.*

The more I thought about it, the more miraculous it seemed. That we had fought those bastards and won.

“Hm. Before you awoke, I heard a rough account of the situation from Benefactor Jeok. Once the message hawk we sent to Henan returns with a reply, we should know how to proceed.”

“Just in case, if you notice anything strange when you examine the formation, let us know.”

“Yes.”

As I answered, I glanced at the figure far ahead of us.

Mungyeong. No, the man known by the epithet Slaughter Saint.

*Fuck. Why is the Slaughter Saint here?*

Honestly, I nearly pissed myself.

Even if I had spent half a day splashing around and grilling meat in the Valley of the Sanzu River,[^2] it would not have been this bad.

*Mungyeong had been the Slaughter Saint. And I’d asked the Slaughter Saint if he’d had a wet dream!*

Teacher Gu Seong-ae. I nearly fucking died because of you.

Just as I secretly breathed a sigh of relief, the dense brush around us vanished, and towering cliffs began to come into view.

[^1]: *Bossam* is boiled pork commonly served with napa cabbage or other greens for wrapping.

[^2]: The Sanzu River is a Buddhist river said to separate the living world from the afterlife.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 371`.

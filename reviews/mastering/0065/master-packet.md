# Master Edit Task — Chapter 65

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
| 혁무진    | **Hyuk Mujin**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 검법     | **sword technique**                              |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 수문조장   | **Captain of the Gatekeepers**               |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 큰형     | **eldest brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 은인     | **Benefactor**                               |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 소천 | **Socheon** |
| 소율 | **Soyul** |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 큰형 | kinship | Eldest older brother, not a generic older brother. | |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
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

#### Chapter 63 tail (verified mastered)

…
old man was incredible.* Even after five days, I still couldn’t forget it. No. Forget five days. Even fifty years from now, I would never forget that sight. The Sword Energy and Sword Force that had swept across the battlefield. And that absurd number—Level 95. *How long could I have lasted against him one-on-one?* Even if I had wrung out every last ounce of strength, I doubted I could have held on for a minute. But unexpected variables had overturned the result, and I had been able to drive my spear through his chest. And the System hadn’t forgotten my reward. “Open Status Window.” Ding! > **System** > > **Status Window** > > **Lv. 50 Jin Taekyung** > > **Class:** First Rate Martial Artist > **Fame:** 1,180 (+150) > **Titles:** 4 (Title effects active) > > - **Sleeping Dragon of Shanxi** — All Stats +10, Fame +100 > - **Scion of a Prestigious Family** — All Stats +5, Fame +50 > - **Novice Trainee** — Training Speed +10% > - **Gambler** — Combat-related Stats +10% in one-on-one combat > > **Strength:** 135 (+15) > **Stamina:** 142 (+15) > **Agility:** 130 (+15) > **Intelligence:** 25 (+15) > **Charm:** 25 (+15) > **Internal Energy:** 15 years > > **Remaining Points:** 100 > > - Distribute your Remaining Points. “Ohhh.” I had checked that Status Window dozens of times over the past few days, but I never got tired of it. It felt like carbonation popping in my veins. *Fighting the Head Elder was worth it.* It had been a gamble with my life on the line, so the reward was stacked. I had jumped thirteen levels in one stroke, my Fame had entered the triple digits, and my Titles had changed. “Check Titles.” Ding! > **System** > > **Status Window** > > **Sleeping Dragon of Shanxi** > > **Grade:** Peak > **Effect:** All Stats +10, Fame +100 > **Description:** Your fame has now spread throughout Shanxi. But the world is vast and masters are many. Never become complacent! I wasn’t a nationwide name yet, but in Shanxi—my local district—I apparently had some real clout… *So that’s why it’s called the Sleeping Dragon of Shanxi?* Goyang’s Honey Fist. Incheon’s Sea of Blood. That kind of thing. Either way, it was good for me. I had a solid new Title, and Family Shame, the tag that had clung to me until recently, was gone. It felt as good as having an aching tooth pulled. *I’ve gotten stronger again.* I suddenly remembered the conversation I’d had with Team Leader Choi before returning to Murim. I’d told him that the next time he saw me, he would have to revise my contract. He had probably taken it as a bluff, but I had made it a reality. *I’ll get as strong as I can, then go back.* I would return with every scrap of power I could obtain. Internal energy, martial arts, stats. Whatever it was, all of it. On my next Logout, I’d be a B-rank Hunter—no, an A-rank Hunter—and return home in glory… “Huh?” No, wait. I felt like I was forgetting something incredibly important. *What is it?* I stopped everything I was doing and tried to pin down that sense of déjà vu. That was when— “Is this the place?” “Yessir. No mistake.” Two voices murmured outside the door. The instant I recognized one of them as Hyuk Mujin’s— Boom! The door was ripped off its hinges with a thunderous crash. * * * I take basic common sense seriously. Tissues go in the trash. Cigarettes belong in the smoking area. Porn comes from Japan. And when you enter someone else’s room, you knock. I especially believe that anyone who barges into a room a man uses alone, without knocking, deserves life in prison. By that standard, the bastard in front of me got the death penalty. Smashing the door earned him life. Speaking down to me on our first meeting was an aggravating offense. I answered him politely. “Yeah. I’m here.” The bastard’s eyes went round. His face was black with grime, as if he had spent twenty years working in the Aoji Coal Mine.[^1] Young. Shabbily dressed. The story practically wrote itself. *Wandering Martial Artist #1.* An extra who had come running after hearing of the Sleeping Dragon of Shanxi’s fame. I turned to Hyuk Mujin, who was wearing a similar expression. “What’s with this guy?” Hyuk Mujin froze solid. He looked like he had seen a ghost. “You don’t know him?” “How would I know, idiot? You have to introduce people.” Grumbling, I raised my Qi Sense. A blue circle stretched toward the two of them. > **System** > > **Lv. ??? Jin Mukyung** *Jin Mukyung. Guess he’s pretty high-level.* “Huh? Jin Mukyung?” I looked at the Level window once. Then at his face. I repeated that three or four times before approaching him with a trembling heart. “Uh, hold on a second.” “…” Rub, rub. My clean sleeve turned black. Beneath the grime, a handsome face emerged. I thought it looked familiar, then realized it was the same face I saw every morning when I washed up. *Carbon copies.* Heh. I gave him an awkward smile. Wandering Martial Artist #1 glared back at me with icy eyes. “Long time no see, hyung.” [^1]: Aoji Coal Mine was a notorious coal mine in North Korea, associated with harsh working conditions.

#### Chapter 64 tail (verified mastered)

…
the wall and landed on the ground. Jin Mukyung watched me and gave a quiet snort. “Well, well.” I didn’t like where this was going. I scratched the back of my head. “Weren’t we close?” “We were. My fist and your body.” “Ah.” I was insane to believe Jin Wikyung. The man doted on his younger brothers like his life depended on it. *Shit. He should’ve explained that properly.* Jin Mukyung held out his fist. “This is your oldest friend. Say hello.” “Hello.” Ominously, his smile widened. “Our youngest has grown a lot. Acting cocky in front of your big brother.” Whoooosh! Jin Mukyung charged like lightning and threw a punch. The air tore before his fist. *He’s serious?* The blow carried no internal energy, but the raw force behind it was immense. I jerked my head aside in alarm. Bang! The wooden wall exploded. Fists rained down through the splinters scattering in the air. Bababang! Face, chest, shoulder, stomach. The punches seemed wild and random, but his movements flowed smoothly, and the area they covered was as tightly woven as a net. “A fist technique?” “Been a while since you had a taste of the Reformation Fist, hasn’t it?” *Fuck, what kind of name is that for a fist technique?* As I cursed inwardly, a move from the Reformation Fist slammed into my abdomen. Whump! “Hup.” “It’s not over yet.” I fought through the breath-stealing pain and blocked the incoming punch with my forearm. The dull impact made my bones throb. “You blocked?” Babababam! It hurt. It hurt like hell. Jin Mukyung outclassed me in every way—strength, speed, everything. But how should I put it… *This is more manageable than I expected.* Was it because he wasn’t using internal energy? At first, all I could do was take a one-sided beating. But after a while, his attacks slowly began to come into focus. Whoosh! Jin Mukyung’s fist sliced through empty air. A precise read. A clean dodge. He looked at me in surprise. “You’ve improved quite a bit.” I steadied my breathing and grinned. Since things had come to this, I figured we might as well have a satisfying fight. “Not quite a bit. A lot. Haven’t you heard the rumors?” “I have. Until I’m sick of them.” Jin Mukyung gave a quiet laugh. “Then prove how much of them is true.” Shwaaak! With a sharp sound of air being split, his hand shot toward my wrist. *Like hell!* I widened my eyes and slapped the incoming hand away. Or tried to. Tap, tat-tat-tat! Five attacks and defenses passed between us in less than a second. Then the match was decided in an instant. Clamp! “What the hell is this pathetic grappling technique?” Jin Mukyung finally twisted my wrist into a lock with a strange movement, then spoke as though I were hopeless. Being caught so helplessly already had me seething, but his next words set my chest on fire. “Again.” “…What are you trying to do?” “I already knew the rumors were nonsense. Now I need to correct the habits of a little brother who doesn’t know his place.” Jin Mukyung released my wrist and crooked a finger. “Come at me. I won’t go easy on you this time.” I stared at him in silence. Jin Mukyung was unquestionably a master far beyond me. The wall of the Peak realm was too high for my current abilities to overcome. I knew that. I knew all of it. *This is pissing me off.* And suddenly, I was curious. How far could I go? Just how strong was Jin Mukyung, the genius whose reputation had spread so far? This was competitive pride—not as a Hunter, but as a martial artist of Murim. *Let’s do this.* Jin Mukyung was the first to notice the change in me. “I didn’t know you could make a face like that.” “This is my normal face.” He laughed as though he found it amusing. “Fine. That’s all well and good… but are you still talking so casually?” At that moment, Jin Mukyung’s fist blurred. Whoosh! Whump! My vision flashed. Even though I had been concentrating to the extreme, I hadn't managed to avoid the attack completely. Jin Mukyung looked from his fist to me and back again. “That shouldn’t have happened.” The punch had been aimed at my temple. If it had landed cleanly, that would have been the last blow. Even though he hadn't used internal energy, I had managed to partially evade a Peak master's full-powered One Strike. “See? I’ve improved a lot.” “I admit it. But you’re not even a quarter as good as the rumors claim.” “Don’t worry. I’ll catch up little by little from here on.” “You’ll catch up to me? How long do you think that’ll take?” I answered. “Starting this very moment.” “Hold out for a quarter of an hour. Then you’re my big brother.” Jin Mukyung's form blurred once again. But this time, I was a step faster. *Assign ten points to Agility.* Ten level-ups gained through the war. A hundred points lying dormant in my Status Window. Some of them answered my command. Shwaaaak! The change was instantaneous. At the same time, certainty filled me. I could perfectly evade Jin Mukyung’s fist as it flew toward my face. Whoosh! *Too slow.* Without hesitation, I turned my head. Whump! *…Damn it. I should’ve used ten more points.*

## Korean source

```text
＃65화



진무경은 생각했다.

‘지난 삼 년 동안 무슨 일이 있었던 거지?’

그건 오랜만에 느껴 보는 당혹감이었다. 그리고 이 순간에도 당혹감은 눈덩이처럼 불어나고 있었다.

쉬쉬쉭!

펑! 콰광!

공기가 터져 나가고 침실 안의 가구는 물론 벽까지 산산조각 난다.

하지만 그뿐이다. 진태경은 아슬아슬하게 자신의 공격을 피해 내고 있었다.

‘이걸 피한다고? 저놈이?’

보면서도 믿을 수 없는 광경.

그는 진태경이라는 인간을 잘 알았다. 명색이 무가의 자제면서 정신도, 육체도 나약하기 짝이 없는 놈.

코흘리개 시절에야 그러려니 하고 넘어갔지만 진태경의 행보는 해가 지날수록 점입가경이었다.

‘어떻게 저런 놈이 내 동생인가 싶었지.’

열다섯 살 때였나? 저놈이 수련장에 의자를 가져온 그 날은 아직도 또렷하게 기억난다.



‘동생아, 그건 뭐니?’

‘의자.’

‘뒤에 한 글자 빼먹었다.’

‘의자요…….’

‘왜 가져 왔어.’

‘마보(馬步) 수련할 때 쓰려고요.’

‘아하, 마보 수련할 때 힘들어서?’



그 획기적인 발상에 진무경은 이마를 탁 쳤더랬다.

동시에 깨달음을 얻었다. 아, 이놈은 말로 하면 안 되는 놈이구나.



‘엎드려.’



갱생권의 탄생이었다.

‘그랬던 놈이, 뭐? 산서잠룡?’

처음 객잔에서 그 얘기를 들었을 때, 어이가 없어서 코웃음조차 나오지 않았다. 매담자가 이십 년만 젊었어도 늘씬하게 두들겨 패 주었을 것이다.

가문에 도착하자마자 태경의 방을 찾은 이유도 그 때문이었다.

‘이제 하다 하다 소문까지 조작해?’

안 봐도 삼재검법이다. 대충 그림이 그려졌다.

할 줄 아는 거라고는 계집질밖에 없는 놈이 유명세 좀 타 보겠답시고 절정 고수 행세를 하는 거겠지.

너 오늘 잘 걸렸다. 딱 그런 마음으로 쳐들어왔다.

그런데…….

‘달라.’

처음 본 순간 알아차렸다. 크고 단단해진 근골. 삼류 파락호 같은 눈빛 깊숙이 숨어 있는 날카로운 기도.

이어 맞잡은 손은 거칠었고 힘이 있었다.

‘절정? 아니, 아니다. 아직은 초일류야.’

자신도 한 번 지나온 길이기에 알 수 있었다. 진태경은 아직 정제되지 않았다. 절정의 벽 앞에 서 있을 뿐이다.

그래서 더 놀라웠다.

‘도대체 어떻게?’

물과 햇빛이 있다고 모두가 자라는 건 아니다. 봄이 와야 싹이 트는 것처럼, 무공을 익히는 것에도 때가 있다.

진태경은 태원진가의 핏줄답게 괜찮은 근골을 타고났지만, 허송세월로 그 시기를 놓쳤다.

그랬던 놈이 삼 년 만에 이렇게까지 성장하다니.

‘환골탈태가 아니고서야…….’

쐐애액!

날카로운 파공성이 진무경의 상념을 깨트렸다. 아슬아슬하게 진태경의 주먹을 피해 낸 그의 얼굴은 딱딱하게 굳었다.

‘갈수록 빨라지고 있다.’

착각이 아니다. 시간이 지날수록 녀석은 빨라지고 있었다.

쉭!

지금조차도.

퍽!

팔을 들어 공격을 막아 낸 진무경의 심정은 당혹, 그 자체였다. 그런 그를 보며 진태경이 낄낄 웃었다.

“못 피할 것 같았지? 그래서 막은 거지?”

“……너.”

“내가 말했잖아. 따라잡는다고.”

“어떻게 된 거지? 공청석유라도 마셨나?”

“석유를 왜 마셔. 이거 완전히 미친놈이네.”

“……!”

난생처음 듣는 폭언에 진무경의 몸이 부르르 떨렸다.

그가 누군가. 홍안의 절정 고수, 무공의 천재! 진무경을 시기하는 중원 명문 세가의 자제들도 감히 이런 막말을 퍼붓지 못했다.

그런데 세 살 터울의 친동생에게 미친놈 소리를 듣다니.

“넌 죽었어.”

흉흉한 기세에 잠시 움찔했던 진태경이 피식 웃었다.

“말이 짧다?”

“뭐?”

“일각 버티면 내가 네 형이라면서? 일각 지났다. 그렇지, 무진아?”

숨도 제대로 못 쉬고 구석에 찌그러져 있던 혁무진이 눈치를 살피며 대답했다.

“예에, 아마도 그런 것 같은데요.”

하지만 이내 저를 죽일 듯이 노려보는 진무경의 시선에 거의 울먹이며 다시 답했다.

“아닌 것 같기도 하고요…… 저 그냥 나가 있으면 안 될까요?”

“안 돼.”

음산한 목소리로 중얼거린 진무경이 공력을 끌어올렸다.

절정 고수의 기파가 대기를 짓누른다. 바닥이 쩍쩍 갈라지고 공기가 터질 듯이 팽창했다.

그그극.

진태경의 얼굴에서 미소가 사라졌다.

“형님. 그건 좀 아닌 것 같습니다.”

반대로 형의 얼굴은 만면에 활짝 웃음을 머금었다.

“그냥 하던 대로 해, 이 새끼야.”

쾅! 콰과광!

굉음. 그리고 붕괴.

뒤늦게 도착한 진위경이 무너진 전각 앞에서 털썩 주저앉았다.

“막내야아-!”

스르륵, 쿵!

그때 건물의 잔해를 해치며 한 사람이 모습을 드러냈다. 피풍의를 입은 그는 살았는지 죽었는지 분간이 안 가는 덩어리 하나를 짐짝처럼 내던졌다.

“아직 안 죽었어.”

그리고 잠깐 생각하다가 말을 이었다.

“한 명은 죽었을지도 모르겠군.”

그에 응답하듯 잔해 더미 속에서 신음이 흘러나왔다.

“끄어어어어.”

“수문조장이다!”

“구해! 약왕당으로 옮겨!”

진무경은 산뜻한 얼굴로 하늘을 바라보았다.

“아, 날씨 좋다.”

싸가지 없는 동생은 매가 약이다.



* * *



약재 특유의 냄새가 코끝을 찌른다. 나는 슬며시 눈을 떴다.

깨끗하게 치워진 방. 문밖에선 십여 명의 인기척이 바쁘게 오가고 옆자리에는 붕대를 칭칭 감은 채 잠들어 있는 혁무진이 보인다.

‘약왕당이군.’

이 정도면 거의 제2의 고향이다. 생각해 보면 전각에서 깨어난 날보다 약왕당에서 깨어난 날이 더 많은 것 같다.

아, 전각도 무너졌지. 참.

“시벌.”

진무경 이 무식한 새끼. 이제 잠은 어디서 자냐. 멍하니 천장을 바라보는데 이불 속에서 뭔가가 꼬물꼬물 움직인다.

‘뭐여, 이건.’

이불을 들추자 옆구리에 찰싹 달라붙어 있던 하얗고 동글동글한 생명체 하나가 모습을 드러냈다.

잠깐의 침묵이 흐르고 내가 입을 열었다.

“너 여기서 뭐 하니?”

“합. 조용해! 조용!”

소천의 동생인 소율이다. 다섯 살 꼬마가 세상에서 가장 간절한 눈망울로 나를 바라본다.

“뭐 하는데?”

“조용히 해!”

“네 목소리가 제일 크거든?”

“합!”

뭘 하는지는 몰라도 인생 참 재미있게 사는구나.

나는 한숨을 내쉬며 이불을 덮었다. 하지만 그것도 잠시.

꼬물꼬물.

“푸하!”

얼굴을 쏙 내민 소율이 씩씩거리며 말했다.

“숨 막혀!”

여기 약왕당 맞아? 환자가 안정을 취해야 할 병실에 아무나 막 들락거려도 되는 거야?

“잘못했서, 안 했서!”

조막만 한 손으로 내 가슴을 탁탁 두드리는데, 그 표정이 제법 엄하기까지 하다.

“그래, 여기서 뭐 하고 있었는데?”

“숨바꼭질.”

“누구랑?”

“오라버니랑!”

소율이 배시시 웃었다.

“소율이가 여기 숨은 줄은 꿈에도 모를걸?”

“글쎄다.”

나는 닫혀 있는 문을 흘끗 바라봤다. 아까부터 문 앞을 서성이는 인기척이 느껴져서다. 보나 마나 뻔하지, 뭐.

“들어와.”

“…….”

“괜찮으니까 들어와.”

그제야 방문이 조심스럽게 열렸다. 소천이 황송하다는 얼굴로 말했다.

“잠시 실례하겠습니다, 은인.”

오빠의 등장에 소율이 충격받은 얼굴로 날 바라봤다.

“날 배신했서!”

나는 인자한 미소를 지으며 대답했다.

“인생은 배신의 연속이란다.”

“이건 무효야! 추잡한 음모야!”

“……그런 말은 어디서 배웠니?”

다섯 살치고는 제법 음험한 어휘력을 뽐내는 동생의 모습에 소천의 얼굴이 붉어졌다.

“율이, 그런 말 하면 못써!”

“오라버니도 한 무더기야!”

“한패겠지.”

이렇게 된 이상 쉬는 건 물 건너갔다.

내심 한숨을 내쉬며 일단 상반신을 일으켰다.

“끙.”

“은인, 괜찮으십니까? 아직 몸도 성치 않으신데…….”

“그 정도는 아냐. 멍 좀 든 거지.”

조금, 아니 조금 많이 두들겨 맞긴 했지만 뼈가 욱신거리고 전신이 멍투성이가 되었을 뿐이다.

그래도 하나밖에 없는 동생이니까 봐준 거겠지. 나도 그걸 감안하고 막 나간 거였고.

“아아, 그렇군요. 다행입니다.”

“그런데 그건 어떻게 알았냐? 소문이 벌써 퍼졌어?”

“가문에 이 소식을 모르는 사람이 없습니다.”

하긴 이른 아침부터 이 층 전각이 무너졌으니 당연한 결과다.

나는 한번 들어나 보자는 심정으로 물었다.

“그래, 다들 뭐라던?”

산서잠룡이 진천검한테 개처럼 두들겨 맞았다더라. 알고 보니 그놈 그거 순 거품이더라. 뭐 그런 소문이 쫙 퍼졌겠지.

안 봐도 비디오…….

“모두가 분노하고 있습니다. 이런 간악한 흉계라니요!”

“응?”

간악한 흉계라니. 이건 또 무슨 소리야. 나도 모르는 사이에 진무경이 독을 썼나? 나 중독됐었던 거야?

내가 어안이 벙벙한 얼굴로 기억을 더듬고 있는데, 소천이 분노에 찬 얼굴로 이를 갈았다.

“제 눈에 띄었다면 동귀어진을 해서라도 놈을 찢어 죽였을 겁니다.”

“……생각해 주는 마음은 고마운데, 너무 과한 거 아니냐? 진정해, 진정.”

진무경이 이 말을 들으면 마냥 허허 웃고 넘어가 주지는 않을 텐데.

그러나 내 만류에도 소천의 분노는 사그라지지 않았다.

“어찌 그럴 수 있겠습니까? 소가주님께서도 즉결 처단을 천명하셨습니다.”

“…….”

뭐야, 그거. 무서워.

둘째 형이 막냇동생 때리면 사형당하는 동네였어, 여기?

‘이게 무림인가.’

나는 떨리는 목소리로 물었다.

“죽인 거야?”

소천이 안타깝다는 얼굴로 고개를 저었다.

“도주했습니다. 지금쯤 추격대가 흔적을 쫓고 있을 겁니다.”

“미친.”

추격대까지 편성했단다. 나는 진위경과 소천의 머리를 쪼개서 뇌를 확인해 보고 싶은 충동을 애써 억눌렀다.

“그, 굳이 그럴 필요까지 있을까?”

“예?”

“아니, 그 양반이 나한테 좀 험하게 굴긴 했어도 그렇게 나쁜 사람은 아닌 것 같아서.”

“은인을 해치려 한 놈입니다!”

“그럴 수도 있지. 난 이해해.”

나도 동생이 있는 몸이라 잘 안다. 가끔은 하연이가 남동생이었으면 좋겠다는 생각도 가끔 한다. 시커먼 사내놈이라면 사회적 비판이나 양심의 가책 없이 뒤지게 팰 수 있을 테니까.

“봐라. 별로 다치지도 않았잖아. 이런 건 침 바르고 하루 이틀 쉬면 싹 나아.”

내 말에 소천의 눈빛이 격렬하게 요동쳤다.

“은인께서는…… 그야말로 군자(君子)십니다. 이 소천, 진심으로 감복했습니다.”

쿵.

미치겠네.

대뜸 큰절을 올리는 소천의 모습에 이마를 짚었다.

“됐고, 가서 추격대 물리라고 해. 아니다. 그냥 내가 가는 게 빠르겠다. 큰형 지금 어디 있어?”

소천이 즉시 대답했다.

“지금 이공자님과 집무실에 계실 겁니다.”

“응?”

“예?”

“아니, 뭐라고?”

“소가주님은 이공자님과 집무실에 계십니다.”

머릿속이 복잡하다. 나는 간신히 입을 열었다.

“그럼 추격대가 쫓는 건 누군데.”

소천이 고개를 갸웃하더니 대답했다.

“그야 당연히 살수지요.”

“살수?”

“뭔 살수?”

또 다른 목소리가 불쑥 끼어들었다. 어느새 잠에서 깬 혁무진이 이게 무슨 개소리냐는 말투로 말했다.

“쟤 무슨 소리 하는 겁니까?”

나는 혁무진을 무시하고 소천에게 계속 말하라는 손짓을 보냈다.

“일단은 대장로의 숨겨 둔 제자가 아닐까 추측 중입니다. 무공이 워낙 고강해 때마침 이공자님이 도착하지 않으셨다면 은인께서도 큰 변고를 당하셨을 거라고…… 아닙니까?”

도무지 믿을 수 없는 이야기에 혁무진이 입을 딱 벌렸다.

“너 미쳤니? 내가 왜 이 꼴이 됐는지 알려 줘?”

고래 싸움에 등 터진 새우가 진실을 말하려던 그때였다.

“아, 혁 무사님을 빠트렸군요. 살수에 맞서 용맹하게 싸우셨다고 들었습니다.”

순간 혁무진의 귀가 쫑긋 섰다.

“내가? 누가 그래?”

“소가주님께서요. 이번에 세운 전공도 있고, 은인을 보호하려다 큰 부상까지 입으셨으니 포상이 엄청날 거라고 다들 부러워하더군요. 차기 수문각주는 따 놓은 당상이라던데.”

“수, 수문각주!”

“그런데 알려 주신다는 건 뭡니까?”

“그건…….”

순간 움찔한 혁무진이 결연한 목소리로 말을 이었다.

“살수에 관해서다.”

“오오오!”

“강한 놈이었지. 차기 수문각주인 내가 백여 합을 겨뤘지만 승부를 보지 못할 정도로…….”

지랄이 풍작이다.
```

## Current accepted English baseline

```markdown
# Chapter 65

Jin Mukyung thought.

*What happened during the last three years?*

It was bewilderment of a kind he hadn’t felt in a long time. Even now, that bewilderment was growing like a snowball rolling downhill.

Whoosh!

Boom! Crash!

The air burst apart. The furniture in the bedroom—and even the walls—were shattered to pieces.

But that was all. Jin Taekyung was narrowly dodging every one of his attacks.

*He’s dodging this? That guy?*

It was an unbelievable sight, even for someone watching it happen.

Jin Mukyung knew Jin Taekyung well. A scion of a martial family in name only, he was a pathetically weak man in both mind and body.

When they were children, Mukyung had been willing to overlook it. But as the years passed, Taekyung’s behavior had grown more and more absurd.

*I used to wonder how someone like that could possibly be my little brother.*

He had been fifteen, perhaps. Mukyung still remembered the day Taekyung brought a chair to the training hall with perfect clarity.

*Little brother, what’s that?*

*A chair.*

*You left off the last syllable.*

*A chair, sir…*

*Why did you bring it?*

*I’m going to use it during horse-stance training.*

*Ah. Because horse stance is difficult?*

That groundbreaking idea had made Jin Mukyung smack his forehead.

At the same time, he had gained enlightenment.

*Ah. This guy can’t be reasoned with.*

*Get down.*

The Reformation Fist had been born.

*And now this guy is what? The Sleeping Dragon of Shanxi?*

When Mukyung first heard about it at the inn, the story was so ridiculous that he couldn’t even bring himself to snort. If the storyteller had been twenty years younger, Mukyung would have beaten him senseless.

That was also why he had gone straight to Taekyung’s room as soon as he arrived at the family.

*Has he gone so far as to fabricate rumors now?*

It was obviously the Three Calamities Sword Technique. Mukyung could already picture the whole thing.

The only thing Taekyung knew how to do was chase women, and now he wanted to taste fame, so he was pretending to be a Peak master.

*I’ve got you now.*

That was the spirit in which he had barged in.

But then…

*He’s different.*

He had realized it the moment he saw Taekyung.

His bones and muscles had grown larger and harder. Deep within eyes that still looked like those of a Third Rate wastrel, there was a sharp, piercing aura.

Then there had been the hand they clasped. It was rough and strong.

*Peak? No. Not yet. He’s First Rate.*

Mukyung knew because he had already walked that path himself. Jin Taekyung was still unrefined. He was merely standing before the wall of the Peak realm.

That made it even more astonishing.

*How on earth?*

Water and sunlight did not make everything grow. Just as a sprout needed spring to emerge, there was a proper time to learn martial arts.

Jin Taekyung had been born with a decent physique, as befitted the bloodline of the Jin Family of Taiyuan, but he had wasted away those years and missed his chance.

And yet that same man had grown this much in only three years.

*Unless he’s undergone a complete transformation…*

Whoosh!

The sharp sound of splitting air shattered Jin Mukyung’s thoughts. He narrowly avoided Taekyung’s fist, his face hardening.

*He’s getting faster.*

It wasn’t his imagination. The more time passed, the faster Taekyung became.

Whoosh!

Even now.

Thud!

Jin Mukyung blocked the attack with his arm, and his feelings were nothing but bewilderment. Watching him, Jin Taekyung snickered.

“You thought you couldn’t dodge it, didn’t you? That’s why you blocked it, right?”

“You…”

“I told you. I’m catching up.”

“What happened to you? Did you drink *gongcheong seokyu*[^2] or something?”

“Why would I drink oil? You’re completely insane.”

[^2]: *Gongcheong seokyu* is a rare martial-arts elixir; *seokyu* is also the Korean word for petroleum.

“…”

Jin Mukyung’s body trembled at the first verbal abuse he had ever heard in his life.

Who was he? A youthful Peak master, a genius of martial arts! Even the scions of prestigious families throughout the Central Plains who envied Jin Mukyung never dared to speak to him so rudely.

And yet his younger brother, only three years apart in age, had called him a crazy bastard.

“You’re dead.”

Jin Taekyung had flinched for a moment at the ominous aura, but then he let out a quiet laugh.

“Getting pretty casual, aren’t you?”

“What?”

“Didn’t you say that if I held out for a quarter of an hour, I’d be your hyung? A quarter of an hour has passed. Right, Mujin?”

Hyuk Mujin, who had been crumpled in a corner and barely able to breathe, cautiously answered.

“Yes, I suppose that’s probably the case.”

But when he saw Jin Mukyung glaring at him as though he meant to kill him, he answered again, nearly in tears.

“Though maybe not… Could I just go outside?”

“No.”

Jin Mukyung muttered the word in a sinister voice and drew up his internal energy.

The aura of a Peak master pressed down on the air. The floor cracked, and the atmosphere swelled as though it were about to explode.

Gr-r-rk.

The smile disappeared from Jin Taekyung’s face.

“Hyung-nim. I don’t think that’s quite fair.”

In contrast, Jin Mukyung’s face was covered by a broad grin.

“Just keep doing what you were doing, you little bastard.”

Bang! Crash!

A deafening roar.

Then, collapse.

Jin Wikyung arrived too late and dropped to his knees in front of the ruined pavilion.

“Youngest—!”

Swish. Thump!

At that moment, someone emerged through the wreckage. Wearing a wind cloak, he tossed out a shapeless lump as though it were a piece of luggage—something impossible to tell whether it was alive or dead.

“He’s not dead yet.”

After thinking for a moment, he continued.

“One of them might be dead.”

As if answering him, a groan rose from the pile of rubble.

“Grrrrr…”

“That’s the Captain of the Gatekeepers!”

“Save him! Take him to the Medicine King Hall!”

Jin Mukyung gazed up at the sky with a refreshed expression.

“Ah. Beautiful weather.”

A rude younger brother needed a good beating now and then.

* * *

The distinctive smell of medicinal herbs stung my nose. I slowly opened my eyes.

The room had been cleaned up. A dozen or so people hurried back and forth outside the door, and Hyuk Mujin was asleep in the bed beside me, swathed in bandages.

*The Medicine King Hall.*

At this point, it was practically my second home. Come to think of it, I had probably woken up in the Medicine King Hall more often than I had woken up in a pavilion.

Oh, right. The pavilion had collapsed too.

Great.

“Goddammit.”

That ignorant bastard, Jin Mukyung. Where was I supposed to sleep now?

I stared blankly at the ceiling. Then something began to squirm beneath my blanket.

*What the hell is this?*

I lifted the blanket and found a small, round, white life-form clinging tightly to my side.

A brief silence passed before I opened my mouth.

“What are you doing here?”

“Shh! Quiet! Quiet!”

It was Soyul, Socheon’s little sister. The five-year-old stared at me with the most desperate eyes in the world.

“What are you doing?”

“Be quiet!”

“Your voice is the loudest one here.”

“Shh!”

Whatever she was doing, she certainly knew how to live an interesting life.

I sighed and pulled the blanket back over us. But that lasted only a moment.

Squirm, squirm.

“Phew!”

Soyul poked her face out and huffed.

“I can’t breathe!”

Was this really the Medicine King Hall? Was anyone allowed to wander in and out of a patient’s room when they were supposed to be resting?

“You did bad, didn’t you!”

She tapped my chest with her tiny hands, and her expression was surprisingly stern.

“All right. So what were you doing here?”

“Playing hide-and-seek.”

“With whom?”

“With my big brother!”

Soyul smiled sweetly.

“He’ll never guess that I hid here!”

“We’ll see.”

I glanced toward the closed door. I had sensed someone hovering outside for a while now. It was obvious who it was.

“Come in.”

“…”

“It’s all right. Come in.”

Only then did the door cautiously open. Looking deeply humbled, Socheon said,

“Please excuse the intrusion, Benefactor.”

At the appearance of her brother, Soyul stared at me in shock.

“You betrayed me!”

I answered with a benevolent smile.

“Life is a series of betrayals.”

“That doesn’t count! It was a dirty conspiracy!”

“Where did you learn words like that?”

At the sight of his five-year-old sister showing off such sinister vocabulary, Socheon’s face turned red.

“Yul, you mustn’t say things like that!”

“Big brother’s a whole heap too!”

“You mean he’s in on it.”

At this point, any chance of getting some rest had gone out the window.

Suppressing a sigh, I first raised my upper body.

“Urgh.”

“Benefactor, are you all right? Your body hasn’t healed yet…”

“It’s not that bad. I’m just bruised.”

I had been beaten a little—or rather, quite a lot—but all that had happened was that my bones ached and my entire body was covered in bruises.

He must have spared me because I was his only younger brother. I had also been deliberately provoking him despite knowing that.

“Oh, I see. That’s a relief.”

“But how did you know? Have the rumors already spread?”

“Everyone in the family knows.”

Naturally. A two-story pavilion had collapsed early in the morning.

I asked, partly out of curiosity.

“So what are people saying?”

*The Sleeping Dragon of Shanxi got beaten like a dog by the Heaven Shaking Sword. Turns out he was nothing but hype.*

Surely rumors like that had spread everywhere.

*I can already see it…*

“Everyone is furious. What a treacherous scheme!”

“Huh?”

What did he mean, treacherous scheme? Had Jin Mukyung used poison without my knowing? Had I been poisoned?

While I searched my memory with a bewildered expression, Socheon ground his teeth, his face full of rage.

“If he had crossed my path, I would have torn him to pieces, even if I had to take him down with me.”

“Thanks for caring, but isn’t that a little excessive? Calm down. Seriously, calm down.”

Jin Mukyung probably wouldn’t simply laugh that off if he heard it.

But despite my attempts to stop him, Socheon’s anger did not subside.

“How could I? The Lesser Family Head has proclaimed that the man is to be executed immediately.”

“…”

*What the hell? That’s terrifying.*

*Was this a place where a second son got the death penalty for hitting his youngest brother?*

*Is this what the Murim is like?*

I asked in a trembling voice.

“Did they kill him?”

Socheon shook his head sadly.

“He escaped. The pursuit team should be tracking his trail by now.”

“Are you kidding me?”

They had even formed a pursuit team. I barely restrained the urge to split open Jin Wikyung and Socheon’s heads and check their brains.

“Was all that really necessary?”

“Pardon?”

“I mean, he was a little rough with me, but he didn’t seem like such a bad person.”

“He tried to harm you, Benefactor!”

“That happens. I understand.”

I had a younger sister too, so I knew how it was. Sometimes I wished Hayeon had been a younger brother. If she were some hulking bastard of a man, I could beat him senseless without worrying about social criticism or pangs of conscience.

“Look. I’m not even that badly hurt. A little spit and a day or two of rest will have me completely healed.”

Socheon’s eyes trembled violently.

“Benefactor… You are truly a *junzi*.[^1] I, Socheon, am sincerely moved.”

Thump.

This was driving me crazy.

I pressed a hand to my forehead as Socheon abruptly dropped into a full bow.

“Enough. Go tell them to call off the pursuit. No—if I go myself, it’ll be faster. Where’s my eldest brother?”

Socheon immediately answered.

“He should be in the office with the Second Young Master.”

“Huh?”

“Pardon?”

“No, what did you say?”

“The Lesser Family Head is in the office with the Second Young Master.”

My thoughts became tangled. I barely managed to speak.

“Then who is the pursuit team chasing?”

Socheon tilted his head and answered.

“An assassin, of course.”

“An assassin?”

“What assassin?”

Another voice suddenly cut in. Hyuk Mujin had woken up and spoke in a tone that clearly meant *What kind of bullshit is this?*

“What is he talking about?”

I ignored Hyuk Mujin and gestured for Socheon to continue.

“For now, we suspect he may have been the Head Elder’s hidden disciple. His martial arts were so formidable that, if the Second Young Master had not happened to arrive, you would have suffered a grave calamity… Isn’t that right?”

The story was so unbelievable that Hyuk Mujin’s mouth fell open.

“Are you crazy? Do you want me to tell you why I ended up like this?”

Just as the shrimp whose back had been broken in the fight between two whales was about to tell the truth, Socheon spoke up.

“Ah, I left out Warrior Hyuk. I heard that you fought bravely against the assassin.”

Hyuk Mujin’s ears perked up.

“Me? Who said that?”

“The Lesser Family Head. You distinguished yourself in battle this time, and you were badly injured while protecting the Benefactor. Everyone is envious, saying your reward will be enormous. They say you’re a shoo-in to become the next Master of the Gatekeeper Pavilion.”

“T-The next Master of the Gatekeeper Pavilion!”

“But what was it you were going to tell us?”

“That…”

Hyuk Mujin flinched for a moment, then continued in a resolute voice.

“About the assassin.”

“Ooooooh!”

“He was strong. Even I, the next Master of the Gatekeeper Pavilion, fought him for more than a hundred exchanges without settling the match…”

What a bumper crop of bullshit.

[^1]: A *junzi* is a Confucian ideal of a morally upright and virtuous gentleman.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 65`.

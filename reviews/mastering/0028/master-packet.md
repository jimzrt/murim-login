# Master Edit Task — Chapter 28

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
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 조필     | **Jopil**          |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 삼류     | **Third Rate**    |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 영약     | **elixir**                                       |                                                       |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 민첩               | **Agility**                    |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 태원     | **Taiyuan**            |
| 공자      | **Young Master**                                                |
| 흑산도 | **Black Mountain Blade** |
| 공야청 | **Gong Yacheong** |
| 소율 | **Soyul** |
| 삭주 | **Sakju** | Jin Family branch location |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 20–24

## Plot

The Jin Family and the Lower District Sect formalize a wartime alliance. In exchange for half of Mount Heng’s shops and exclusive rights to its pleasure district, the Lower District Sect stops selling Shanxi intelligence to other sects and devotes its resources to war intelligence. Wolhwa disguises the agreement by publicly claiming that she and Taekyung spent a passionate night together, presenting it as an unpaid Honghwaru tab. Her investigation has found neither evidence clearing Taekyung nor Lee Seogeun’s killer; she supports the Jin Family because either Taekyung is legitimate or the family is powerful enough to conceal the truth.

Taekyung recognizes Wolhwa’s coachman as Yama Whip, a Peak master. When the gate guards mistake Taekyung for the hero who helped Yama Whip defeat the Heavenly Axe, he encourages the story. The System reports that Poisoner rumors are fading, the Sleeping Dragon of Shanxi rumor is strengthening, and Taekyung gains 20 Fame. Meanwhile, Lee Cheonbaek, Mount Heng’s Sect Leader and Lee Seogeun’s father, expels the poison from his son’s body, vows revenge, and sends about two hundred armed martial artists toward the Jin Family.

Mount Heng’s attack begins with the murder of twenty-five children from the Jin Family’s Saneum, Eung-hyeon, and Sakju branches. The Head Elder calls the deaths necessary sacrifices and uses the Sleeping Dragon rumor and Taekyung’s supposed alliance with Yama Whip to force him into wartime service. Taekyung becomes leader of White Tiger Hall’s reconnaissance squad under the Head Elder’s faction and receives a repeating quest to earn 100 Merit.

The squad consists mostly of inexperienced second-rate martial artists. Taekyung appoints Level 22 Hyuk Mujin, who has killed five bandits, as deputy squad leader and assigns everyone numbers. He imposes a practical Hunter-style schedule, equips three members with wooden shields, and drills formations, dispersal, and all-out retreat. Hyuk mocks the retreat strategy and accuses Taekyung of causing the war. Taekyung knocks him unconscious with a sequence of slaps, then does so again when Hyuk attacks after waking in a hunter’s shelter during a blizzard. The rest of the squad accepts Taekyung’s methods and asks him to train them.

The squad is ordered to scout near Jeongyang and return within five days. A Lower District Sect messenger hawk reports that Jopil, One Question, One Kill, and a special detachment have appeared there. Jopil leads about fifty wandering martial artists in massacring survivors from the Sakju Branch, killing the defending martial artist and several women and children. He orders his First Rate subordinate Black Mountain Blade to pursue one escaping martial artist and two children toward Honju.

Fourteen-year-old Socheon flees with his younger sister, Soyul. Their mother led other survivors away earlier, while their father and the branch families were killed. Gong Yacheong, an old friend of Socheon’s father, guides the children and stays behind to delay the pursuers; his fate is unknown. The siblings reach the reconnaissance squad’s hunter’s shelter as more than twenty Mount Heng pursuers arrive. The System creates the Sudden Quest **Survivors of the Sakju Branch**.

Taekyung first orders an attack formation, then changes to a defensive formation so the squad can hold the enemy back while he claims the kills, EXP, and Merit. He charges alone through the low-level pursuers, using the Jin Family’s Manoeuvre and Spear Techniques and cycling through their forms. He finishes Level 32 Black Mountain Blade with Sky-Piercing Strike, completes the Survivors of the Sakju Branch Quest, receives substantial EXP and Merit, reaches at least Level 20, and triggers a Chain Quest.

## Continuity

- The Jin Family–Lower District Sect alliance lasts for the war. Its terms are half of Mount Heng’s shops, exclusive pleasure-district rights, and exclusive Lower District Sect intelligence support.
- Wolhwa is Eun Sowol, the Level 50 Branch Leader of the Lower District Sect’s Shanxi branch. Yama Whip is her Peak-level coachman.
- Lee Cheonbaek is Mount Heng’s Sect Leader, the Blood Wolf Sword, and Lee Seogeun’s father. He has committed Mount Heng to revenge.
- Taekyung leads ten reconnaissance-squad members in White Tiger Hall. The deployed group has eleven people including Taekyung. The group has nine sword users, one spear user—Level 13 Han Yeop—and no experienced shield user before Taekyung assigns three wooden shields.
- Hyuk Mujin is Level 22, has killed five bandits, and is Taekyung’s deputy squad leader. Han Yeop enthusiastically follows Taekyung’s orders.
- The squad is scouting near Jeongyang under a five-day return deadline. Taekyung’s standard movement cycle is two hours of travel followed by fifteen minutes of rest.
- Jopil, One Question, One Kill, commands about fifty wandering martial artists. Black Mountain Blade, his First Rate right-hand man, is dead.
- Socheon and Soyul survived the Sakju Branch massacre. Their mother’s fate and Gong Yacheong’s fate remain unresolved.
- Taekyung completed the Sudden Quest **Survivors of the Sakju Branch**, gained large EXP and Merit, levelled up repeatedly, and activated a Chain Quest. Its requirements and outcome remain unresolved.
- The war, the unidentified assassin who killed Lee Seogeun, the capsule’s purpose, the route home, and Murim’s death and resurrection rules remain unresolved.

## Translation Decisions

- Preserve **Lower District Sect**, **Branch Leader**, **Honghwaru**, **Yama Whip**, **White Tiger Hall**, **One Question, One Kill**, **Black Mountain Blade**, **Sakju Branch**, **Honju**, and **Jeongyang**.
- Keep the alliance terms precise: half of Mount Heng’s shops, exclusive pleasure-district rights, and exclusive wartime intelligence support.
- Render Taekyung’s staged introduction as: “Yama. Whip. Great Hero!”
- Preserve the repeating 100-Merit quest, the Sudden Quest **Survivors of the Sakju Branch**, and the Chain Quest as distinct System events.
- Retain Taekyung’s practical Hunter-style command, the numbered-squad joke, the formation commands “Form up,” and his EXP-driven decision to claim the enemies himself.
- Preserve the dark comedy and violence of the five-blow sequence, including Hyuk’s accusation and Taekyung’s grip holding him upright.
- Keep **Sky-Piercing Strike** as the final form of the Jin Family’s Spear Technique and retain “Splurt!” for the finishing impact.
- Render `반 시진` as “more than half a shichen,” with a brief factual footnote if used in the chapter translation.

### Prior accepted reading-copy tails

#### Chapter 26 tail (verified mastered)

…
through back alleys possibly leave behind? He should at least leave a hide. Leaving twenty stripped corpses behind, they continued onward. After the long night ended, they found the fugitives’ traces around daybreak. *We’ll be meeting soon, friend.* The corners of Jopil’s mouth lifted. This mysterious master was the first in a long while to pique his interest. His long-stiff heart began to pound. * * * I shuddered. “Ugh. What the hell?” A sudden chill ran through me. I raised my arm and found it covered in goose bumps. If this were a scene in a novel, the protagonist would have muttered, *Something feels off,* and gone on his way. But I was different. I acted on firm suspicion. “Hey. Get over here, quick.” I couldn’t see him, but I could feel it. Someone trudging behind me faltered. “W-why?” “I’m counting to three. One, two. Three.” The instant I hit three, Hyuk Mujin rushed over and pressed himself against my side. “It was you, wasn’t it?” “What?” “You were the one. Tell me the truth and I’ll let it slide.” “What are you talking about? It wasn’t me!” I silently stared at his face, swollen like a steamed bun. “You were cursing me behind my back just now, weren’t you?” “Gasp.” “You were cursing me, right?” “I-I was…” I knew it was this bastard. When I raised my hand, Hyuk Mujin squeezed his eyes shut. After getting beaten about three times, he had lost all his fighting spirit. On top of that, he had learned a valuable life lesson: Dodging only meant getting hit more. “Fine. Since you told the truth, I’ll let it go this once.” Hyuk Mujin jerked his head up. “Really?” I gave him a warm smile. “Of course. But don’t even think about deceiving me from now on. I’ll be watching you with mind-reading.” Hyuk Mujin stared at me with demon-filled eyes, then bolted back to his place. If I’d had enough time, I would have crushed his head with a mace. Swallowing my regret, I kept walking. “What’s mind-reading?” The chatter tickled my ears. It belonged to Soyul, Socheon’s little sister. Was she five years old? She was small enough to fit right inside my backpack. “Is it martial arts?” “Something like that.” “Is mind-reading strong?” “Really strong.” “Wow! Soyul wants to learn mind-reading, too!” “But you have to be one-eyed.” “Gasp!” I glanced over and saw Soyul staring at me, startled. Her eyes had gone huge. Ridiculously cute. *Hayeon used to be like that, too.* These days she was a gross little sister, but when she was little she had been a baby angel. She had even gotten offers to be a child model… Carrying her on my back felt exactly like carrying Hayeon when she was that age. “Want me to teach you?” “…Soyul doesn’t like martial arts. I want to become a proper young lady.” “That’s fine, too.” “Mm-hmm. Mister, do you like martial arts?” “Me?” “My brother says you’re really strong. Dad said only people who work hard can become strong.” “Your dad said that?” “Yes. My dad is really strong, too. Because…” She chattered excitedly for a while, then stuck out her lower lip. “Soyul wants to see Dad. But I guess Dad doesn’t want to see us. Oppa says he went out to play with Mom, leaving me and Oppa behind.” My heart dropped with a thud. An old memory filled my vision. In a funeral hall of black and white, little Hayeon had searched for our father, and I had no choice but to tell her an obvious lie. Just as Socheon had done for Soyul. It was the only thing I could say. “…I see.” What else could I say? I looked at Socheon, following along in the middle of the formation. He was panting hard, drenched in sweat. *He must be exhausted.* His willpower was far beyond his years. The saying that pain made people mature was fucked up, but it was true. Socheon hadn’t fallen behind even once, and the other reconnaissance squad members marveled at him for it. *But the real problem is somewhere else.* Gong Yacheong. His face was deathly pale; he still hadn’t shaken off his injuries. If not for the remarkable effects of the fasting pills I had given him, and the qi he had circulated last night, he might have collapsed long ago. *At this rate, we’ll be caught.* Even after the sun rose, the accumulated snow wouldn’t easily melt. I was out front, forcing a path through it, but everyone was exhausted, and our pace had slowed. On top of that, we had an injured man and children. *Should I run away by myself?* The thought came to me in an instant. It was a game. So what? Gong Yacheong, those two kids, the whole reconnaissance squad—every last one of them was created AI. Just NPCs. But me? I was alive. Among all of them, I was the only one who was real. The only one with a real body. But… *Fuck. It’s a simple problem… Why am I like this?* An inexplicable aversion surged through me. It was strong enough to startle me—strong enough to throw me off. *Why?* I didn’t know. I didn’t find the answer for hours after that, and then night came. [^1]: A shichen is a traditional time period of roughly two hours.

#### Chapter 27 tail (verified mastered)

…
since we started moving?* A sikyeong? Half a shichen? I couldn’t tell. In the dead of night, with darkness swallowing everything around us, even the passage of time was impossible to feel. With every step, one thought refused to leave my mind. *He must have left by now.* It was only natural. Gong Yacheong and I both knew it, and every member of the reconnaissance squad except Han Yeop had accepted it. Most importantly… I had a family waiting for me. There was a reality I would face once I got out. *Then why does this feel so damn awful?* My feet felt heavy. Not just because snow had piled up to my calves. Not because grass and branches blocked the path ahead. A mere NPC named Gong Yacheong kept weighing on my mind. I thought of his final smile. The cheap Quest without a single reward. I thought of Han Yeop defying my order, and Hyuk Mujin’s calm gaze pricked at my chest like a thorn. *It’s only natural. So why?* Because it was a game. Because it was only a game. *If I didn’t leave him behind, everyone would die. I’d die, too! You fucking bastards!* “Fuuuck…” The profanity that had been caught in my throat spilled out. Soyul stirred from her light sleep and mumbled something as she wrapped her arms around my neck. Her adorably tiny hands were cold. The sensation was so vivid it raised goose bumps across my skin. Too real to believe this was a game. Real enough to make me feel guilty for abandoning a single NPC. “…What a fucked-up game.” I turned around. “Where are you going?” I strode back the way we had come. Neither Socheon nor the faces of the reconnaissance squad members registered. That was why I didn’t notice the fleeting smile that crossed Hyuk Mujin’s face when he asked where I was going. Or that Han Yeop, who should have been at the very rear, was nowhere to be seen. “Huff. Huuuff.” I raced across the snow like the wind. And then I found him. Below the hill, Han Yeop was gritting his teeth and forcing one foot in front of the other even as he gasped for breath. Gong Yacheong, unconscious, was on his back. “You…” I didn’t know what to say. With a sigh, I grabbed Han Yeop’s hand and pulled him up. “Th-thank you.” *Shit…* *I don’t know anymore, either.* * * * This was a hidden retreat reserved for one person. Since becoming its owner thirty years ago, he had barred everyone else from entering. Over time, that had hardened into an unbreakable rule, and the others thought of it the same way. “How are things going?” The air trembled faintly as the two shadows conversed through Sound Transmission. “Smoothly. And on your end?” “Do you even need to ask?” “I wouldn’t expect otherwise.” “The Blood Wolf Sword. For a man with such an epithet, he’s surprisingly fond of his family.” “A wolf can still love its own blood. So?” “The vanguard alone numbers two hundred. A madman named Jopil is running wild as he pleases, but… it should be fine.” “Jopil, One Question, One Kill? The Blood Wolf Sword chose well.” “The wastrel young master is being chased all over the place. It wasn’t part of the plan, but this isn’t bad either.” “Hahahaha.” “Could it be…?” “That’s right. I sent him. Once the Lesser Family Head sees the severed head of the youngest brother he cherishes so dearly, he’ll change his mind.” “Whew. A heart as cold as poison, without blood or tears. You have my respect.” “Are you one to talk?” “I merely took one hopeless life.” “And thanks to that, a bloody storm will sweep across Shanxi?” “Isn’t that what you wanted?” “I can’t deny it. Yes. I’ve waited far too long.” “The fruit will be all the sweeter.” “I hope so.” “Ah, one more thing. The Lower District Sect has gotten involved.” “The Lower District Sect? How did they?” “The new Branch Leader has a sharp nose. Once this matter is settled, I plan to get rid of him.” “Be careful. No matter how formidable Heaven may be, you must never let your guard down…” At that moment, the wind stopped. The air quivered. “…I misspoke.” A long while passed before another Sound Transmission arrived. “You would do well to watch your words and actions.” The voice was as soft as a cat’s paw. But the listener could feel the razor-sharp blade hidden beneath it. “Let me apologize once more.” “Let’s end here for today. If any problems arise, I’ll visit you again in a few days.” The conversation ended there. The other person vanished without a sound or trace. *They’re like ghosts.* Sometimes, he wondered what their true identities were. How strong were they? Who were their members? But he soon shook his head. *That would only shorten my life.* He had endured years of hardship to reap the fruit. He couldn’t let mere curiosity ruin his great undertaking. *It truly has been a long time.* The shadow reached a hand toward the moon. Faint moonlight slipping between his fingers illuminated a silver beard. *Soon… everything will return to its proper place.* The Head Elder smiled with pleasure. [^1]: A shichen is a traditional time period of roughly two hours; a sikyeong is a shorter traditional interval.

## Korean source

```text
＃28화



후우.

가부좌를 튼 채 호흡을 골랐다. 내뱉는 숨에는 미처 갈무리하지 못한 기(氣)가 섞여 있다.

‘아깝다.’

운기조식은 외부의 기를 받아들여 내부의 기와 함께 순환, 축적하는 행위다. 하지만 체내에 남는 기는 소량에 불과했다.

대부분의 기운은 다시 자연으로 돌아간다.

‘소설에서는 조금만 해도 쭉쭉 오르던데.’

천하제일의 무공? 천고의 영약?

여긴 그런 거 없다. 진가심법의 등급이 절정이긴 하지만 공력 축적에는 영 젬병이고 영약은 개뿔, 구경도 못 해 보고 고생만 죽도록 했지 뭐.

‘희망은 하나뿐인가?’

단전 한구석에 웅크린 또 다른 공력. 그걸 전부 내 것으로 만든다면 앞으로의 싸움에 큰 도움이 될 것이다.

문제는 아무리 시도해 봐도 요지부동이라는 사실이다.

‘움직여라. 움직여!’

지금껏 장군바위처럼 버티고 있던 놈이 움직일 리가 있나. 공력을 끌어 올려 봤지만 묵묵부답이다. 나는 한숨과 함께 자리에서 일어났다.

“출발입니까?”

주위를 경계 중이던 혁무진이 물었다.

“그래.”

“알겠습니다.”

그러더니 잽싸게 순찰조원들을 준비시키고 소율을 품에 안는다. 어안이 벙벙해지는 순간이다.

‘이 자식이 뭘 잘못 먹었나.’

갑자기 왜 이렇게 빠릿빠릿해졌지?

주먹을 들이밀어야 마지못해 움직이던 놈인데, 어째 인간이 좀 달라진 것 같다.

‘나야 좋지만.’

잡생각은 치워 버리고 공야청을 둘러업었다. 중독 증상이 심해지면서 그의 안색은 검푸르게 변색되어 있었다.

혁무진이 걱정스럽게 물었다.

“괜찮을까요?”

“괜찮아야지.”

이미 할 수 있는 최선을 다했다. 공야청이 버텨 주기를 바랄 뿐이다. 혼절해 있는 그를 향해 중얼거렸다.

“얼마 남지 않았습니다. 조금만 더 버티세요.”

어스름한 새벽 사이로 햇빛이 비집고 들어왔다. 나는 햇빛을 향해 성큼 발을 내디뎠다.

아니, 내딛으려고 했다.

- 아우우우!

처음에는 바람 소리라고 생각했다. 하지만 그건 살아 있는 짐승들의 울음소리였다. 혁무진이 중얼거렸다.

“늑대들이 배가 고픈 모양이군요.”

“늑대?”

“그럼요. 산에 산짐승이 있는 게 이상한 일은 아니죠.”

고대 중국이 배경인 게임이다. 늑대, 호랑이가 어디서 튀어나와도 이상하지 않다. 나도 지난 며칠간 산짐승들의 울음소리를 여러 번 들었다.

그런데…….

‘기분이 이상해.’

지금까지의 그것과는 다르다. 저 울음소리를 듣는 것만으로도 가슴이 답답해지고 손끝이 찌릿하다.

지난 7년간의 경험으로 벼려 낸 직감이 속삭이는 듯했다. 아직 햇빛이 비치지 않은 저 숲 너머에 뭔가가 있다고.

“전투 준비.”

“그럼 이제 출발…… 예?”

“수비 대형 펼쳐.”

혁무진은 이내 정신을 차리고 내 명령을 전달했다. 얇은 철을 씌운 방패를 든 정찰조원 셋이 눈 덮인 길을 틀어막는다.

비좁은 오솔길에 언덕 위의 고지대. 유리한 위치다.

- 아우우우!

두 번째 늑대 울음소리가 들렸다. 더 가깝고, 그래서 불길하다. 혁무진이 조심스럽게 입을 열었다.

“단순한 늑대 무리인 것 같습니다만…….”

“그럼 더 좋고.”

“너무 시간을 지체하는 건 아닐까요?”

나는 고개를 저었다. 꼬박 이틀을 도망쳤다. 이 잠깐의 시간 때문에 붙잡힌다면 그건 운명인 거다.

“대기해. 조금만 더 기다린다.”

내 말을 짐승들도 알아들은 모양이다. 일 다경 동안 울음소리는 끊이지 않고 가까워졌다. 눈 덮인 새벽 산중에 나뭇가지 부러지는 소리와 눈 위를 뛰어오는 소리가 요란했다.

“한두 마리가 아닌 모양입니다.”

혁무진이 슬쩍 내 얼굴을 바라봤다.

“들리는 소리로는 수십 마리는 될 듯한데…… 늑대가 무리를 짓는 짐승이라지만 이상하긴 하군요.”

그 말이 끝나기가 무섭게 늑대 무리가 모습을 드러냈다. 겨울이라 먹잇감을 구하지 못했는지 대부분 갈빗대가 앙상하다. 하지만 그 본질은 맹수. 방심할 수 없다.

‘그것도 굶주린 맹수지. 애들이 다칠 수도 있겠어.’

생각과는 반대로 묘한 안도감이 들었다. 무림인들이 널리고 널린 곳이지만 설마 짐승까지 무공을 익혔을까.

느낌 운운할 것도 없이 손쉬운 상대인 것이다.

‘레이드 좀 안 뛰었다고 감 다 죽었네.’

나는 혀를 차며 앞으로 나섰다. 맹렬히 뛰어오는 수십 마리의 늑대들이 벌써부터 경험치 덩어리로 보인다.

“빨리 끝내자. 응?”

저 멀리 선두에서 달려오는 늑대에게 손가락을 까딱였다. 덩치를 보아하니 저놈이 우두머리다.

- 크허엉!

아니 무슨 늑대가 사자처럼 울어. 설마 뭐 영물, 그런 건가? 설마 나 짐승한테 지는 거야?

‘그건 안 되지.’

침을 삼키며 창을 곧추세웠다. 기 싸움에서 밀리면 안 된다는 생각에 눈에 힘을 빡 주고 목소리를 깔았다.

“와라.”

효과는 굉장했다!

- 크르르르.

달려오던 놈이 갑자기 방향을 틀어 숲속으로 뛰어든다. 수십 마리의 부하 늑대들도 우두머리를 따라 우르르 사라졌다.

아니, 이건 도망친 거다. 눈 위에 무수히 찍힌 발자국들 위로 찬 바람이 불었다.

‘뭐야, 이거.’

산 채로 씹어 먹을 것처럼 달려오더니 왜 도망쳐?

그때 문득 모 유명 만화가 생각났다. 과잉 행동 장애를 앓고 있는 고무 인간이 해상 공권력을 박살 내는 스토리.

“서, 설마 거기에 나오는 그거?”

기운만으로도 적을 겁먹게 만들고 기절시키는 그 능력.

워낙 정신 나간 게임이니 충분히 가능한 얘기다. 그럼 이 시점에서 시스템 알림 한 번 울려 줘야 하는데…….

띠링.

그렇지! 나는 기대에 부풀어서 시스템 음성을 기다렸다.

해괴한 표정을 한 정찰조원들은 신경도 쓰지 않고 쉴 새 없이 중얼거렸다.

“떠라, 떠라, 떠라!”

떴다.

퀘스트창이.



- 퀘스트가 생성되었습니다.



퀘스트



[일문일살 조필]

끈질긴 추격전이 끝났습니다. 당신은 이 잔인하고 집요한 추격자들과 맞닥트렸고, 일문일살 조필을 상대해야 합니다.

부디 명복을…… 아니, 무운을 빕니다.



등급 : 절정

제한 : 진태경

임무 : 생존 (미완료)

보상 : ???

실패 : 사망



- 당신은 퀘스트를 선택할 권한이 없습니다.

- 퀘스트가 강제 수락되었습니다!



“……어?”

이게 무슨 일인가. 여긴 어디고 나는 누구인가.

순간 수많은 물음이 떠올랐고 사라졌다. 그리고 누군가의 목소리가 들려왔다.

“드디어 만났군.”

앙상한 나무 옆, 한 남자가 서 있었다. 이십여 장의 거리. 멀다면 멀고, 가깝다면 가깝다. 문제는 아무도 그의 존재를 몰랐다는 것이다. 나조차도.

‘도대체 언제?’

레벨과 무공의 경지가 오를수록 오감(五感)은 날카로워졌다. 그런데 저 남자는 감지해 내지 못했다. 발소리조차 들리지 않았다.

그가 먼저 말하지 않았다면, 퀘스트창이 뜨지 않았다면 아무것도 모른 채 뒤돌았을 것이다.

‘늑대들.’

그 짐승들은 도망친 것이다. 내가 아닌 저 남자를 피해서.

아까부터 떠나지 않던 불안감이 실체를 드러내는 순간이었고, [기감]은 쓸 필요도 없었다. 나는 이미 남자의 이름을 알고 있으니까.

“조필?”

남자, 일문일살 조필은 활짝 웃으며 고개를 끄덕였다.



* * *



지금까지 내가 만난 절정 고수는 셋이다.

진위경, 위팽, 그리고 대장로. 셋 모두 외관상 절정 고수다운 풍모를 지닌 자들이다. 하지만 일문일살 조필은 달랐다.

‘평범해.’

진위경 같은 거인도, 위팽처럼 날카로운 눈매의 소유자도 아니었고 대장로처럼 은빛 수염을 기르지도 않았다.

일문일살 조필은 적당한 키에 평범한 인상의 소유자였고, 그래서 더 위험해 보였다.

“반갑네.”

조필이 환하게 웃으며 발을 내딛는 순간, 나는 고민할 것도 없이 훌쩍 물러났다.

“민첩하군. 반응도 좋고. 마음에 들어.”

가슴이 쿵쾅거린다. 긴장한 탓인지 쉰 목소리가 새어 나왔다.

“다가오지 마.”

“미안하게 됐네. 너무 반가운 마음에 그만.”

난 하나도 안 반갑다.

“너무 긴장하지는 말게. 단지 이야기를 나누고 싶을 뿐이니까.”

“이야기?”

“그래. 자네를 만나고 싶었거든.”

조필 입장에서는 만나고 싶긴 했을 거다. 불과 며칠 전 수하 스무 명을 잃었으니까.

‘시발. 좆 됐네.’

저런 고수가 나를 찢어 죽일 생각에 이틀 밤낮을 쫓아왔다고 생각하자 속이 울렁거렸다.

“개수작 부리지 마라, 조필!”

크게 소리치자 등 뒤의 공기가 얼어붙는 것이 느껴진다. 조필이 다 안다는 듯 웃었다.

“내 정체를 저들에게 알린다고 뭐가 달라지겠나. 이류, 삼류. 전부 머저리에 쓰레기들이야.”

정찰조원들의 수준을 정확히 짚어 낸다. 이 자식도 시스템을 사용하는 건 아닌지 의심이 들 정도다.

“그러지 말고 잠깐 대화를 나누는 게 어떤가? 자네에게 궁금한 게 많거든.”

“대화? 시간을 벌려는 건 아니고?”

“시간을 번다니. 그게 무슨 말이지?”

“무슨 말이긴. 당신이 수하들을 기다린다는 말이지.”

정곡을 찔린 듯, 조필의 콧잔등이 실룩거렸다. 맞다. 이유는 모르지만 지금 놈은 혼자다. 약간의 희생을 감수한다면 충분히…….

“기다려? 내가? 그 약해 빠진 놈들을?”

“……뭐?”

“앞서 말하지 않았나. 전부 머저리에 쓰레기들이라고. 노력도, 재능도 없는 구제 불능의 인생들이지.”

“…….”

“흑산도 그놈은 그나마 괜찮았는데…… 사람 보는 눈이 없었으니 죽어도 싸. 고수를 못 알아본 죄로 녀석의 눈을 찢어 주고 왔지.”

정정한다. 일문일살 조필은 위험해 보이는 게 아니라 존나 위험한 새끼다.

‘이건 완전히 미친놈이잖아.’

현실에서도, 게임에서도 조필 같은 놈은 처음 봤다. 천연덕스러운 말투와 태도. 놈은 인간을 도구 취급하는 사이코패스다.

“아무튼 자네가 걱정하는 일은 일어나지 않을걸세. 느려 터진 놈들이라 쫓아오려면 반 시진은 걸릴 거야. 모든 게 끝난 후겠지.”

하나는 확실하다. 놈이 생각하는 결말에 자신의 죽음은 들어가 있지 않다는 것.

“어떤가?”

“만약 거부한다면?”

조필은 부드럽게 웃어 보였다.

“자네한테 실망하겠지. 아주 많이.”

실망하면 무슨 일이 벌어질지 대충 그림이 그려진다.

“후배. 나는 자네에게 어떤 원한도 없어. 아니, 오히려 호감이 있는 편이지. 몇 가지만 사실대로 대답해 주면 보내 줄 수도 있네.”

“잠깐. 보내 준다고?”

“그래. 어떤 위해도 가하지 않고 멀쩡히 돌려보내 주지.”

“……정말로?”

“내 목을 걸지. 이 정도면 됐나?”

조필의 얼굴에서 진심이 묻어 나온다. 사이코패스에 종잡을 수 없는 놈이지만 어쩌면 모두가 무사히 살아갈 수도 있다는 생각이 들었다.

“그렇게 하지.”

최악의 상황이 오더라도 싸우기밖에 더 하겠나. 잠깐 시간을 벌면서 놈의 약점을 읽어 낼 생각이었다.

“좋아. 말이 통하는 친구로군, 하하.”

조필이 손뼉을 치며 웃었다. 왼쪽 허리춤에 찬 검갑이 흔들거린다.

‘오른손잡이. 검수.’

그렇게 머릿속에 정보를 입력해 나갔다.

“먼저 자네 나이를 묻고 싶군.”

“스물.”

조필은 눈을 동그랗게 떴다.

“허, 약관에 그 정도 경지라니. 대단하군.”

헌터 생활 7년 동안 F급을 벗어나지 못했는데 게임에서는 무공의 천재 취급 받는다. 묘한 기분이다.

“복장을 보아하니 태원진가의 인물인 것 같은데.”

선선히 고개를 끄덕여 주었다.

“약관에 초일류의 경지라. 그 유명한 진천검은 아닐 테고…… 자네 이름이?”

“진태경.”

“진태경. 진태경. 어디서 들어 본 이름인데? 아!”

곰곰이 생각에 잠겨 있던 조필이 탄성을 내뱉었다.

“망나니 삼공자! 그게 자네라고?”

“망나니는 아니고. 요즘은 잠룡 소리 듣고 있지.”

“푸하하! 그럼 그렇지. 태원진가, 그 고지식한 작자들이 독살은 무슨. 누가 짜 놓은 판인지는 몰라도 일이 재밌게 돌아가는군.”

조필은 흡족한 얼굴로 나를 바라봤다.

“자네에 관한 소문은 익히 들어 알고 있었지. 그건 전부 위장이었나?”

“……뭐, 그렇지.”

“좋아. 숨겨진 칼이라 이거지. 마음에 들어. 무공은 언제부터 익혔나?”

“칠 년.”

아주 틀린 말은 아니다. 무림으로 따지자면 헌터들의 전투법도 일종의 무공이니까.

“칠 년이라. 스승은?”

“없어.”

“스승이 없다?”

한동안 나를 바라보던 조필이 말했다.

“거짓말은 아닌 것 같군.”

“솔직하게 대답하면 살려 준다. 당신이 했던 약속 아닌가?”

“그래, 그랬지. 황당하면서 재밌는 이야기야. 태원진가의 직계가 스승도 없이 약관의 나이에 그 정도 경지에 올랐다…… 허, 참.”

입이 바짝 타들어 간다. 창을 꽉 움켜쥐고 조필의 몸을 훑었다. 지금의 그는 믿을 수 없을 정도로 허점투성이다. 하지만 정말 내 눈에 보이는 게 전부일까?

‘내가 먼저 달려들기를 노리는 것일 수도 있다.’

생각은 더 이상 이어지지 못했다. 조필이 돌연 웃음을 터트렸기 때문이었다.

“으하하! 좋아. 마음에 들어. 약속은 지키지.”

약속을 지킨다고?

설마 했던 일이 사실이 될 줄이야. 나는 멍한 얼굴로 조필을 바라봤다.

“그렇게 볼 것 없네. 사실 처음에는 자네를 꼭 죽이고 싶었는데…… 막상 만나 보니 더 지켜보고 싶다는 마음이 생겼거든.”

조필이 호의가 듬뿍 담긴 목소리로 말을 이어 갔다.

“이런 걸출한 인재를 죽이기에는 아깝지. 이런 상황에서는 더더욱.”

“이런 상황이라니?”

“아, 자네는 모를 수도 있겠군. 복귀하면 알게 될 거야. 그럼 가 보게. 다음에 볼 때는 좀 더 성장해 있길 바라지.”

가도 된다고? 정말로? 나는 경계를 풀지 않은 채 뒷걸음질 쳤다. 조필은 웃으며 나를 바라볼 뿐이었다.

그 모습이 송사리를 놓아주는 낚시꾼의 그것 같았다.

‘호랑이 굴에 들어가도 정신만 차리면 산다더니.’

조필의 어디로 튈지 모르는 성격이 탈출구가 될 줄이야.

안전거리가 확보되자 참았던 숨이 토해졌다. 하지만 숨 돌릴 틈도 없다. 1초라도 빨리 이 자리를 떠야 한다.

“이동한다. 빨리!”

하지만 다음 순간이었다.

“이보게. 후배.”

조필이 어리둥절한 얼굴로 나를 바라봤다.

“지금 뭘 하는 건가?”

“뭘 하다니. 그야 당연히 약속대로 돌아가는…….”

“내가 허락한 건 자네 혼자야.”

“……뭐?”

“이래 봬도 고용된 처지거든. 맡은 임무는 완수해야지.”

임무라니. 설마?

“삭주 지부의 생존자 셋. 그리고 자네가 수하라고 부르는 저 쓰레기들은 두고 가게. 이틀간 수고한 값은 받아야 하지 않겠나?”

어린아이처럼 맑던 눈동자가 번뜩인다. 다음 순간 그의 눈은 포식자의 그것으로 바뀌어 있었다.

“미리 말해 두지. 거부한다면 내가 아주 실망하게 될 거야.”

나는 멍하니 조필과 정찰조원들, 그리고 어린 남매와 죽어 가는 공야청을 바라보았다. 시간은 짧았지만 수십 번의 고민과 갈등 끝에 한마디가 튀어나왔다.

“그럼 실망해, 이 시발 새끼야.”

조필이 광포하게 웃었다.
```

## Current accepted English baseline

```markdown
# Chapter 28

*Hoo.*

I sat cross-legged and evened out my breathing. The breath I exhaled still carried qi I hadn’t managed to draw back in.

*What a waste.*

Circulating qi meant drawing in energy from outside, cycling it together with my internal energy, and accumulating it. But only a small amount stayed in my body.

Most of it returned to nature.

*In novels, you could shoot up just by doing a little of this.*

The greatest martial arts under heaven? An elixir of the ages?

Not here. The Jin Family’s Cultivation Technique was Peak-grade, but it was hopeless at accumulating internal energy. And elixirs? Bullshit. I hadn’t even gotten a look at one. All I’d done was suffer like hell.

*Is that my only hope?*

Another mass of internal energy crouched in a corner of my dantian. If I could make all of it mine, it would be a huge help in the fights ahead.

The problem was that no matter how many times I tried, it wouldn’t budge.

*Move. Move!*

As if the thing that had sat there like a boulder this whole time was going to start moving. I tried drawing up my internal energy, but it gave me nothing. I sighed and got to my feet.

“Are we departing?”

Hyuk Mujin had been watching our surroundings.

“Yeah.”

“Understood.”

Then he briskly got the reconnaissance squad ready and scooped Soyul into his arms. I was left staring.

*What the hell did this bastard eat?*

Why had he suddenly gotten so sharp?

This was the guy who used to move only when I shoved a fist in his face. Somehow he seemed like a different person.

*Not that I’m complaining.*

I shoved the stray thoughts aside and slung Gong Yacheong onto my back. As the poisoning worsened, his face had gone dark blue.

Hyuk Mujin asked, worried, “Will he be all right?”

“He has to be.”

I’d already done everything I could. All I could do was hope Gong Yacheong held on. I muttered toward the unconscious man.

“Not much farther. Just hold on a little longer.”

Sunlight squeezed through the dim dawn. I took a long stride toward it.

No—I started to.

- Awoooooo!

At first I thought it was the wind. But those were the cries of living beasts. Hyuk Mujin muttered,

“The wolves must be hungry.”

“Wolves?”

“Of course. It’s hardly strange for there to be wild animals in the mountains.”

This was a game set in ancient China. Wolves, tigers—nothing jumping out would be strange. I’d heard wild animals crying more than once over the past few days.

But…

*Something feels off.*

This wasn’t like the ones before. Just hearing those howls made my chest tight and my fingertips tingle.

The gut I’d honed over seven years seemed to whisper. Something was beyond that forest, where the sunlight hadn’t reached yet.

“Prepare for battle.”

“Then we’re leaving now… Huh?”

“Form a defensive formation.”

Hyuk Mujin snapped out of it and passed on the order. Three reconnaissance squad members with thin-iron-plated shields blocked the snow-covered path.

A narrow trail, high ground on a hill. Advantageous position.

- Awoooooo!

A second howl. Closer—and more ominous for it. Hyuk Mujin spoke carefully.

“They appear to be nothing more than a wolf pack…”

“Then that’s even better.”

“Won’t this delay us too long?”

I shook my head. We’d been running for two full days. If this brief pause was what got us caught, that was fate.

“Hold. We wait a little longer.”

The beasts seemed to take me at my word. For several minutes the howls never stopped, and they kept getting closer. In the snow-covered mountains at dawn, snapping branches and paws racing over snow made a racket.

“Doesn’t sound like one or two.”

Hyuk Mujin glanced at my face.

“From the sound, there must be dozens… Wolves are pack animals, but this is strange.”

No sooner had he finished than the pack showed itself. Maybe they hadn’t found prey in winter; most of them were nothing but ribs. But they were still predators. We couldn’t let our guard down.

*Hungry predators, at that. The kids could get hurt.*

And yet, oddly, I felt relieved. The place was crawling with martial artists, but it wasn’t as if the beasts had learned martial arts too.

Forget gut feelings—these were easy opponents.

*I skip a few raids and my touch is completely gone.*

I clicked my tongue and stepped forward. The dozens of wolves charging at us already looked like chunks of EXP.

“Let’s wrap this up. Yeah?”

I crooked a finger at the wolf running point in the distance. Judging by the size, that one was the leader.

- Grrrraaaah!

Since when did a wolf roar like a lion? Don’t tell me it was some kind of spirit beast? Was I seriously going to lose to an animal?

*Not happening.*

I swallowed and brought my spear up. I couldn’t afford to lose a clash of qi, so I glared hard and dropped my voice.

“Come.”

The effect was incredible!

- Grrrrr…

The charging wolf suddenly veered off and plunged into the forest. Its dozens of subordinate wolves poured after it.

No—that was a retreat. A cold wind swept over the countless pawprints stamped into the snow.

*What the hell.*

They came running like they were going to eat me alive. Why run?

Then a famous comic popped into my head. The one about a rubber man with hyperactivity disorder smashing the maritime authorities.

“D-don’t tell me it’s that?”

That ability that could scare enemies senseless—knock them out, even—with qi alone.

This game was insane enough that it was entirely possible. In which case the System ought to ping me right about now…

Ding.

There it was! I waited for the System voice, buzzing with anticipation.

I ignored the reconnaissance squad’s bizarre faces and muttered without stopping.

“Come on, come on, come on!”

It appeared.

The Quest Window.

> **System**
>
> A Quest has been created.
>
> **Quest**
>
> **Jopil, One Question, One Kill**
>
> The relentless chase has come to an end. You have come face-to-face with these cruel and tenacious pursuers, and you must confront Jopil, One Question, One Kill.
>
> May you rest in peace… No, fortune in battle.
>
> **Grade:** Peak
>
> **Limit:** Jin Taekyung
>
> **Task:** Survive — Incomplete
>
> **Reward:** ???
>
> **Failure:** Death
>
> - You do not have the authority to choose this Quest.
>
> - The Quest has been forcibly accepted!

“…Huh?”

What was this. Where was I, and who was I?

Countless questions rose and vanished. Then I heard someone’s voice.

“We finally meet.”

A man stood beside a gaunt tree, about twenty zhang away.[^1] Far if you called it far, close if you called it close. The problem was that nobody had known he was there.

Not even me.

*When the hell did he…?*

The higher my Level and martial realm, the sharper my five senses got. And I still hadn’t picked that man up. I hadn’t even heard footsteps.

If he hadn’t spoken first—if the Quest Window hadn’t appeared—I would have turned around without knowing a thing.

*The wolves.*

Those beasts had run. Not from me. From that man.

The unease that hadn’t left me since earlier took on a shape. I didn’t even need Qi Sense.

I already knew his name.

“Jopil?”

The man—Jopil, One Question, One Kill—smiled wide and nodded.

* * *

I had met three Peak masters so far.

Jin Wikyung, Wipeng, and the Head Elder. All three looked the part. Jopil, One Question, One Kill, did not.

*He looks ordinary.*

He wasn’t a giant like Jin Wikyung, didn’t have sharp eyes like Wipeng, and didn’t wear a silver beard like the Head Elder.

Jopil was average height, unremarkable face—and that made him look even more dangerous.

“Nice to meet you.”

The instant Jopil smiled brightly and stepped forward, I sprang back. No thought required.

“Nimble. Good reactions, too. I like you.”

My heart hammered. Maybe from the tension, a hoarse voice slipped out.

“Don’t come any closer.”

“Sorry about that. I got a little too happy to see you.”

I wasn’t happy at all.

“Don’t be so tense. I only want to talk.”

“Talk?”

“Yes. I’ve been wanting to meet you.”

From Jopil’s side, he probably had. He’d lost twenty men just a few days ago.

*Fuck. I’m fucked.*

The thought of a master like that chasing me day and night for two days, wanting to tear me apart, made my stomach turn.

“Don’t give me that bullshit, Jopil!”

When I shouted, I felt the air behind me freeze. Jopil smiled like he already knew.

“What difference does it make if you tell them who I am? Second Rate, Third Rate. All idiots and trash.”

He’d read the reconnaissance squad’s level exactly. I almost wondered if he was using the System too.

“Why not have a short conversation? There’s a lot I want to ask you.”

“A conversation? You’re not just buying time?”

“Buying time? What is that supposed to mean?”

“You know what it means. You’re waiting for your men.”

As if I’d hit the mark, the bridge of Jopil’s nose twitched. Right. I didn’t know why, but he was alone. If I was willing to take a few losses, it might be enough to…

“Waiting? Me? For those pathetic weaklings?”

“…What?”

“Didn’t I already say? They’re all idiots and trash. Hopeless lives. No effort, no talent.”

“…”

“Black Mountain Blade was decent enough, but he had no eye for people, so he deserved to die. I tore his eyes before I left. Punishment for failing to recognize a master.”

Correction. Jopil, One Question, One Kill, didn’t look dangerous.

He was a fucking dangerous bastard.

*This guy’s completely insane.*

I’d never seen anyone like Jopil, in real life or in a game. That unbothered tone and manner. He treated people like tools. A psychopath.

“Anyway, what you’re worried about won’t happen. They’re painfully slow. It’ll take them half a shichen to catch up.[^2] By then, everything will be over.”

One thing was certain. In the ending Jopil had in mind, his own death wasn’t part of it.

“Well?”

“And if I refuse?”

Jopil smiled softly.

“I’ll be disappointed in you. Very disappointed.”

I could more or less picture what happened if he got disappointed.

“Young friend, I have no grudge against you. No—if anything, I’m rather fond of you. Answer a few things truthfully, and I might even let you go.”

“Wait. Let me go?”

“Yes. I won’t lay a finger on you. I’ll send you back in one piece.”

“…Really?”

“I’ll stake my neck on it. Is that enough?”

The sincerity showed on Jopil’s face. Unpredictable psychopath or not, maybe everyone could walk out of this alive.

“All right.”

Even if the worst came, all I could do was fight. I’d buy a little time and try to read his openings.

“Good. A friend who can talk, haha.”

Jopil clapped and laughed. The sword case at his left hip swayed.

*Right-handed. Swordsman.*

I kept inputting the data in my head.

“First, I’d like to ask your age.”

“Twenty.”

Jopil’s eyes went round.

“My. That realm at twenty. Impressive.”

Seven years as a Hunter and I never got out of F-rank. In this game, they treated me like a martial arts genius. Strange feeling.

“Judging by your clothes, you seem to be from the Jin Family of Taiyuan.”

I nodded readily.

“Super First Rate at twenty. You wouldn’t be that famous Heaven Shaking Sword, so… your name?”

“Jin Taekyung.”

“Jin Taekyung. Jin Taekyung. I’ve heard that name somewhere. Ah!”

Jopil had been turning it over. Then he exclaimed.

“The wastrel third Young Master! That’s you?”

“Not a wastrel. These days they call me the Sleeping Dragon.”

“Puhahaha! I knew it. The Jin Family of Taiyuan, those rigid fools, poisoning someone? Please. I don’t know who set this board, but things are getting interesting.”

Jopil looked at me, satisfied.

“I’ve heard plenty of rumors about you. Was all of that a disguise?”

“…Something like that.”

“Good. A hidden blade, then. I like it. When did you start learning martial arts?”

“Seven years.”

Not entirely a lie. By Murim standards, Hunter combat methods were a kind of martial art too.

“Seven years. And your master?”

“Don’t have one.”

“No master?”

He studied me for a while, then said,

“Doesn’t seem like a lie.”

“You promised to spare me if I answered honestly. That was your promise, wasn’t it?”

“Yes, it was. An absurd, entertaining story. A direct descendant of the Jin Family of Taiyuan, no master, that realm at twenty… My, my.”

My mouth was bone-dry. I gripped the spear and scanned Jopil’s body. The openings on him right now were unbelievable. But was what I was seeing really all there was?

*He could be baiting me into attacking first.*

The thought didn’t go any further. Jopil suddenly burst out laughing.

“Hahaha! Good. I like it. I’ll keep my promise.”

He’d keep his promise?

The thing I’d thought was impossible was actually happening. I stared at him, blank.

“No need to look at me like that. Truth is, at first I really wanted to kill you… But now that we’ve met, I find I want to watch you a little longer.”

Jopil went on, his voice full of goodwill.

“It’d be a waste to kill talent like this. Especially in a situation like this.”

“A situation like this?”

“Ah. You might not know. You’ll find out when you return. Go on, then. I hope you’ll have grown a little by the next time we meet.”

I could go? He meant it?

I backed away without dropping my guard. Jopil just smiled at me.

He looked like a fisherman letting a minnow go.

*They say even if you walk into a tiger’s den, you live if you keep your head.*

Who’d have thought Jopil’s wild-card personality would turn into an exit.

Once I had a safe distance, the breath I’d been holding came out. But there was no time to catch it. I had to leave this place a second sooner, if I could.

“We’re moving. Hurry!”

Then—

“Hold on, young friend.”

Jopil looked at me, puzzled.

“What are you doing?”

“What do you mean? Going back, like you promised…”

“I only gave permission for you. Alone.”

“…What?”

“I may not look it, but I’m in someone’s employ. I have to finish the mission I took on.”

The mission. Don’t tell me.

“The three survivors of the Sakju Branch. And those pieces of trash you call your subordinates. Leave them. I should be paid for two days’ work, don’t you think?”

Eyes that had been clear as a child’s flashed. The next instant, they were a predator’s.

“I’ll say this now. If you refuse, I’ll be very disappointed.”

I stared blankly at Jopil, the reconnaissance squad, the young siblings, and the dying Gong Yacheong. Time was short, but after dozens of loops of doubt and conflict, one line came out.

“Then be disappointed, you fucking bastard.”

Jopil laughed savagely.

[^1]: A zhang is a traditional Chinese unit of distance, roughly 3.3 meters.
[^2]: A shichen is a traditional time period of roughly two hours.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 28`.

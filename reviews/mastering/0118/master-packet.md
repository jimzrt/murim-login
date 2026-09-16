# Master Edit Task — Chapter 118

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
| 진무경    | **Jin Mukyung**    |
| 철무백    | **Cheol Mubaek**   |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 창법     | **spear technique**                              |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 정파     | **orthodox faction**                             |                                                       |
| 진가창법   | **Jin Family's Spear Technique**       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 대사      | **Master** for a senior Buddhist monk                           |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 적혈십이도 | **Crimson Blood Twelve Sabers** | Pung Yang's domineering saber art; he has reached approximately seventy percent mastery. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 막내 | kinship | Youngest-child/youngest-member address, not generic “kid.” | |
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 110–114

## Plot

Cheol Mubaek, the Peak-level Tiger of Mount Heng, stops the Mount Heng Sword Sect’s elders from abandoning Lee Cheonbaek’s final wishes and forces them to recognize Lee Seowol as their Sect Leader. Seowol refuses to flee despite the sect’s overwhelming disadvantage, preparing a desperate defense with oil hidden throughout the estate while awaiting Jin Taekyung and Jin Mukyung.

Pung Yang leads more than two hundred Red Wind Band mounted bandits in surrounding Mount Heng. He offers Seowol a choice between total destruction and marriage, intending to preserve the sect’s useful forces under his control. Cheol kills the envoy, prompting the assault. The sect’s defenses initially repel the attackers, and Seowol’s concealed fire attack burns many mounted bandits, but the gate and walls eventually fall. Cheol holds the breached gate alone until Pung Yang confronts him.

Pung Yang swallows an unidentified red pill from a hard wooden case and gains enough power to defeat the mature Peak master Cheol, breaking all four of his limbs and severely injuring him. The surviving defenders retreat to a watchtower, where Seowol continues fighting until exhausted and signals Cheol with a fire arrow. Pung Yang reaches her and renews his demand that she marry him.

Taekyung, Mukyung, Mujin, and Wolhwa arrive at the fortress after a forced ride under Taekyung’s time-limited Peak Quest. Cheol recognizes Taekyung’s Taiyuan Jin Family affiliation, leaving the Jin party as the Mount Heng Sword Sect’s only immediate hope.

## Continuity

- Taekyung, Mukyung, Mujin, and Wolhwa have reached the Mount Heng Sword Sect after racing against the Quest’s irreversible twenty-two-hour deadline.
- Taekyung is Level 55; Mujin is Level 38.
- The Red Wind Band began the assault with more than two hundred mounted bandits, suffered at least one hundred casualties in the fire attack and initial fighting, and still retains more than one hundred fifty when Pung Yang enters personally.
- Pung Yang is an early Peak master whose saber and throwing-knife techniques are highly developed; the red pill temporarily raises his power far beyond Cheol Mubaek’s.
- Pung Yang possesses an unidentified hard wooden case containing the red pill and possibly a weapon or other anti-tiger object.
- Cheol Mubaek is alive but has four broken limbs and severe internal injuries. He refuses to surrender the single-successor Shura Annihilating Fist, though he fears for Lee Seowol’s safety.
- The Mount Heng fortress wall has been overrun. Lee Seowol and the remaining defenders are surrounded at the watchtower, while Pung Yang demands her marriage.
- Lee Seowol remains Sect Leader by choice and has not accepted Pung Yang’s demand.
- The Mount Heng Sword Sect’s survival, Seowol’s response, and Taekyung’s ability to rescue her and Cheol remain unresolved.
- The nature and origin of Pung Yang’s red pill remain unknown.
- The Peak Quest’s required invitation to the Jin Family for the coming Lunar New Year remains the governing objective.

## Translation Decisions

- Retain **Peak**, **early Peak**, **First Rate**, **shichen**, **Red Wind Band**, **mounted bandits**, **Sect Leader**, **Young Lady**, and **Taiyuan Jin Family**.
- Render **수라멸권** as **Shura Annihilating Fist**.
- Render **항산권문** as **Mount Heng Fist Sect**; retain **Mount Heng Sword Sect** where that established sect name is used.
- Render **화시** as **fire arrow**, **쇠뇌** as **crossbow**, **충차** as **battering ram**, and **벽곡단** as **fasting pills**.
- Render **멸문지화** as **total destruction**, **혼인 예물** as **wedding gift**, and **동귀어진** as **perishing together**.

### Prior accepted reading-copy tails

#### Chapter 116 tail (verified mastered)

…
“Two hundred moves. I’ll finish you before then.” “Are you even capable of that?” “Before cutting off your limbs, I should pull out your tongue first. Listening to you has been pissing me off for a while now.” “Be grateful you didn’t have to fight my younger brother. If he were your opponent, you’d have already plugged your ears and killed yourself. He’s mastered the art of making fun of people.” “The Sleeping Dragon of Shanxi? Then I suppose I should pull his tongue out too.” “…That actually sounds kind of appealing.” “Enough nonsense. Raise your sword. That way, you can struggle for even a moment longer before you die.” The instant Pung Yang’s red eyes gleamed eerily, immense internal energy surged from his lowered saber. Fwoooosh! When internal energy was infused into a medium and given tangible form, it was called Sword Energy. But after taking the Temporary Strength Pill, Pung Yang had now surpassed that realm. “Sword Force…” A Supreme Peak master. It was the symbol of those known as Martial Gods. Though his enlightenment was insufficient for it to be called true Sword Force, there was no doubt that he had reached the very pinnacle of the Peak realm. “Well, damn.” Jin Mukyung let out a hollow laugh. How many years would Pung Yang have needed to reach that realm through training alone? Ten? Twenty? But one tiny red pill had allowed him to leap over all those years—the contemplation of martial principles, the endless training, the blood and sweat. It had let him surpass all of it. “What kind of son of a bitch made something like that…” Tsssss. Sword Energy rose from Jin Mukyung’s sword as well. Pung Yang spoke with open contempt. “Last two hundred moves, and I’ll let you live.” “Yeah, go fuck yourself.” Fwoooosh! As he watched the Sword Force plunge down as though to split heaven and earth, Jin Mukyung suddenly thought he was beginning to resemble his insolent youngest brother. *But what is that guy doing, taking so long to get here?* KABOOOOM! * * * Rumble, rumble, rumble. The ground shook as though an earthquake had struck. I had no idea what kind of battle was taking place thirty jang away, but I knew one thing. *I can’t go over there.* I wasn’t joking. If I got caught up in that fight, I’d probably die. I had no desire to personally experience what happened when a First Rate got its back broken between Peak masters. And more importantly… Whoosh! Slice! “Gueeegh.” I had more than enough on my hands here. At this point, I might not be able to take on a hundred men, but I had to be good for at least seventy. I swung my weapon like a madman, drenched in the blood pouring down around me. Shwaaak! I caught the cavalry spear thrusting toward my side and pulled it toward me. I drove it into the stomach of the man bringing his saber down behind me, then chopped through the shaft with the edge of my hand. Crack! “Gasp!” “Use an iron spear next time. Something heavy and sturdy. You could even do squats with it. How great is that?” With that friendly advice, I smashed my fist into the mounted bandit’s jaw. His body went limp as his jawbone shattered. Shraaaaak! *Throat, side, leg.* I could read the daggers thrusting toward me from three directions without even looking. How could every last one of them be so slow and predictable? I was also genuinely amazed by myself. In that brief moment, I could think of a response and put it into action. Tap. Crack! I put my weapon into my Inventory, freeing my hands. As I simultaneously caught the wrists of the men stabbing toward my throat and side and broke them, I kicked backward with my leg fully extended. Their short screams and the dull impact told me I had struck exactly where I intended. *More. More. More.* My hands moved faster and faster, while the sounds around me grew more distant. Every time I brushed against the bodies of the enemies surrounding me, weapons summoned from my Inventory appeared and vanished. Stab. Slash. Swing. Broke. How many had I brought down? At some point, the noise that had been pushed far away came rushing back all at once. Thud. “Ggh…” “Urgh.” The dead lay motionless with their faces buried in the cold dirt. The survivors rolled around, groaning. The twenty or so mounted bandits who had escaped death and injury backed away from me. “T-the Sleeping Dragon of Shanxi…” One step. Two steps. Terrified, they retreated as I advanced, forgetting that furious enemies were still behind them. Shraaaaak! Thud! “Kill them! Kill every last mounted bandit!” “You fucking bastards!” They were the martial artists of the Mount Heng Sword Sect who had survived and fought to the bitter end. Caught by the surprise attack of those bloodshot-eyed men, the mounted bandits fell like dominoes. “Kyaaaagh!” “P-please, spare me…!” Everywhere I looked, the ground overflowed with corpses, blood, and groans. How many mounted bandits had died here today? Two hundred? Three hundred? I didn’t know. What I did know was that this battle would not end until one man died. *Pung Yang.* It was time to deal with that cheating, pill-popping bastard. “…” *I can do this, right? I should be able to. Probably…*

#### Chapter 117 tail (verified mastered)

…
him. The martial artists of the Mount Heng Sword Sect were already creeping closer with their weapons drawn. The beautiful woman among them, glaring at him with especially venomous hatred, had to be the Mount Heng Sword Sect’s new Sect Leader, Lee Seowol. *This man isn’t going to die peacefully.* It was time for him to pay for the karma of his past misdeeds. I flicked my spear toward Pung Yang. “Still going to keep spouting nonsense?” The bastard stared at us for a moment before speaking. “I think you’re laboring under a serious misconception.” The laugh in his voice was impossible to hide. “Is there anyone among you capable of defeating me?” “What the fuck does that even—” “If you find that hard to believe, it would be faster to ask the Heaven Shaking Sword standing before me. Well? What do you think?” Jin Mukyung didn’t answer Pung Yang’s question. Only then did I realize why he hadn’t said a word for some time. Why he had stood there like a stone statue without moving. Tap. Pung Yang’s hand touched Jin Mukyung’s chest. At what point had it happened? His unconscious body crumpled limply. Only then did I see the five throwing knives embedded in a neat row across his upper body. Thud. Pung Yang’s red eyes swept across the silent crowd and curved into crescent moons. “Well, shall we finish things up?” * * * The “finishing” began quickly. It started with the more than ten throwing knives that shot from Pung Yang’s sleeve as he approached us at an easy pace. Whoosh! Thunk-thunk-thunk! It might have been a close-range attack, but it was a throwing-knife technique that even Jin Mukyung hadn’t been able to evade. Pung Yang’s knives pierced their targets with perfect accuracy, and screams rang out without fail. “Urgh.” “Guhk!” The martial artists of the Mount Heng Sword Sect were already at the limits of their endurance, and none of them were particularly powerful. They were easy prey. By the time I finally stepped in front of Pung Yang, more than ten of them had already lost their lives. “Stop.” He shook his head. “No. That’s not how it works. Giving orders is a right reserved for the strong.” “…I’ll kill you.” “If you were the Heaven Shaking Sword, perhaps. But a wet-behind-the-ears fledgling like you dares?” I fell silent at Pung Yang’s sneer. He wasn’t wrong. My decision to block his path had been equal parts courage and recklessness. *But how do I take him down?* My mind felt like it was burning itself blank. Amid all the tangled thoughts, two faces surfaced. The first was the Head Elder. He had been the most powerful and despair-inducing opponent I had ever faced. But back then, I’d had Jin Wikyung and the martial artists of the Jin Family to help me. *What about now?* No one. There was no one. After taking the Temporary Strength Pill, Pung Yang had to be a master comparable to, or even stronger than, the Head Elder. And the only person left to face him was me. That naturally brought the second person to mind. *Jopil, One Question, One Kill.* Perhaps Jopil was the person who had forced me to face a genuine crisis. For the first time, I’d lost one of the subordinates I’d gained in the Murim, and I’d nearly died. Only after that had I managed to defeat the bastard. But the Pung Yang standing before me was on an entirely different level from Jopil. *This goddamn Temporary Strength Pill…* The more I thought about it, the more curses came out. I wanted to see the face of whatever son of a bitch had made it. “Once you’ve learned your place, curl up quietly.” Watching Pung Yang act like the greatest master under heaven simply because he trusted that pill twisted my gut. If he’d only been around Jopil’s level, I might have found a way to deal with him… *…Wait.* A fact I’d forgotten suddenly flashed through my mind. There had been something nasty among Jopil’s possessions. What was it again? *The Blazing Flame Divine Pill.* A peerless divine elixir that granted half a jiazi of internal energy when consumed—but also a double-edged sword that could kill its user with the fire qi it contained.[^4] *The Blazing Flame Divine Pill. The Blazing Flame Divine Pill…* The next moment, I abruptly spoke. “Hey.” Pung Yang, who had already walked past me, stopped and turned around. “Hey? Were you talking to me?” “Yeah, you pill-popping bastard.” “Hah. What did this little brat just say…?” “Did you enjoy being the only one popping pills?” “…What?” I looked straight at his face, mottled with bewilderment and fury, and enunciated each word. “I asked if you enjoyed taking pills all by yourself.” An eye for an eye. Doping for doping. Now I was going to pop a pill and fight, too. You bastard. [^1]: *Narye tagon* literally compares someone to a lazy donkey rolling on the ground. For martial artists from prestigious orthodox factions, it implies humiliatingly abandoning dignity to survive. [^2]: A martial-arts term describing force that passes through one object to strike another behind it. [^3]: Mount Beimang is traditionally associated with burial grounds and the dead; sending someone there is a euphemism for killing them. [^4]: A *jiazi* is a sixty-year cycle; half a jiazi is thirty years.

## Korean source

```text
＃118화



“너만 약 처먹으니까 좋았냐?”

“뭐?”

“혼자 약 처먹으니까 좋았냐고.”

풍양은 헛웃음을 흘렸다.

이제 고작 약관에 불과한 핏덩이 주제에 혀가 짧아도 너무 짧다. 태원진가의 막내 도련님으로 태어나 잠룡 소리를 듣고 있어 눈에 보이는 게 없는 건가?

“그놈 참, 허허.”

껍데기뿐인 웃음소리는 얼마 지나지 않아 잦아들고, 살기 어린 눈빛이 빈자리를 채웠다.

“관을 봐야 눈물 흘리겠느냐?”

진태경이 눈을 크게 떴다.

“이야, 저 대사 실제로 들으니까 되게 이상하네. 다시 해 봐.”

“말로 해선 안 되는 놈이군.”

풍양은 느긋한 걸음걸이로 다가가며 생각했다. 어떻게 해야 저 어린놈의 주둥이에서 살려 달라는 말이 나올까?

그가 평소 자주 사용하는 방법은 혀를 뽑고 사지를 잘근잘근 부러트리는 거다. 하지만 태원진가의 무공을 알려 줄 귀한 몸을 그리 함부로 대할 수가 있나.

적당한 타협이 필요했다.

‘다리 근맥을 끊어 놓으면 얌전해지겠지.’

태원진가와는 이미 돌이킬 수 없는 강을 건넜다. 풍양은 이 싸움이 끝나면 사람의 발이 닿지 않는 심산유곡에서 무공을 보완한 다음 다시 무림에 나올 생각이었다.

적풍단은 궤멸당했지만, 세력은 얼마든지 다시 모을 수 있다. 무림은 강자가 지배하는 곳이니까.

“전부 네가 자초한 일이니 날 원망 말거라.”

풍양이 곡도를 움켜쥔 그때였다.

“아, 잠깐만.”

손을 내저은 진태경이 뭔가를 입 안에 탁 털어 넣는다.

너무나도 자연스러운 모습에 풍양은 멈칫할 수밖에 없었다.

‘뭐 하는 거지?’

의문도 잠시.

한차례 몸을 부르르 떤 진태경의 전신에서 엄청난 열기가 피어오르기 시작했다.



* * *



어차피 내게 주어진 선택지는 하나밖에 없었다. 열화신단으로 최후의 도박을 벌이는 것.

위험성이 크긴 하지만 풍양에게 무공 구결을 토해 내고 죽는 것보다는 백배 나은 선택이다.

꿀꺽.

과연 영단은 영단인지, 혀에 닿자마자 스르륵 녹아 목으로 넘어간다. 문제는 그다음부터였다.

띠링.



- [열화신단]을 복용했습니다.

- [운기조식]으로 기운을 다스리십시오.



뜨겁다. 열화신단이 품고 있던 30년의 공력이 사지백해로 들불처럼 퍼져 나갔다.



- 일시적으로 [열양지기]의 속성을 부여받았습니다.

- 일시적으로 [공력]이 45년으로 상승합니다.

- 기운을 다스리지 못하면 죽음에 이를 수도 있습니다!

- 퀘스트, [영단 흡수]가 생성되었습니다.



끊임없이 울리는 시스템 알림을 확인할 여유 따위는 없었다. 당장 몸 안에서 날뛰는 열화신단의 기운을 제어하는 것만으로도 벅찼으니까.

“후우, 후우우우.”

인간 압력밥솥이 된 기분이다. 마치 정말 불이라도 난 것처럼 전신에서 연기가 모락모락 솟아올랐다.

딛고 선 땅 위로 덮여 있던 눈이 녹고, 축축한 흙이 물처럼 흐물흐물해졌다.

‘어느 정도 예상했지만 이건…….’

정말이지 상상 이상이다. 비명도 지르지 못하고 몸을 부르르 떠는 내 귓가로 풍양의 목소리가 파고들었다.

“무슨 짓을 한 거냐!”

당황한 놈의 얼굴을 보자 오히려 살짝 열기가 가라앉는 기분이다.

나는 억지로 입꼬리를 끌어 올리며 대답했다.

“무슨 짓이긴, 갈 데까지 가 보자는 거지.”

“놈!”

대답에서 불길함을 느낀 걸까? 풍양의 곡도가 눈부신 속도로 날아들었다. 쭉 뻗어 나온 붉은 도기(刀氣)가 내 가슴을 노린다.

쉭!

딱 반걸음 차이로 죽음이 빗겨 나간다. 목표를 놓친 곡도가 다시 한번 어지러운 궤적을 그렸다.

쉬쉬쉬쉭!

그러나 이번에도 곡도는 헛되이 허공을 갈랐다. 어느새 뒤로 물러난 나를 바라보는 풍양의 얼굴이 일그러졌다.

“너……!”

“뭐, 인마.”

애써 태연하게 대꾸했지만 사실 가장 놀란 건 나였다. 앞서 손을 섞었을 때는 이 정도로 손쉽게 피해 내지 못했다.

풍양의 압도적인 기세와 도기에 밀려 피하기에 급급했던 그때와는 차원이 다르다.

‘언제부터 몸이 이렇게 가벼웠지?’

공격을 피해야겠다고 생각한 순간, 몸이 그 어느 때보다 빠르게 움직였다. 달라진 것은 그뿐만이 아니다.

‘똑똑히 보인다.’

풍양의 움직임 하나하나가 보이고, 읽힌다. 공격이 보이니 못 피할 것도 없다. 도기가 아니라 도강(刀罡)이라 해도 피할 수 있을 것 같은 기분이다.

나는 마침내 그 이유를 깨달았다.

‘공력 때문이야.’

기존에 갖고 있던 15년의 공력과 열화신단의 30년 공력이 합쳐진 상태다. 비록 내가 완벽히 통제할 수는 없지만 그렇다고 해서 30년의 공력이 가진 힘이 없어지는 것이 아니다.

부풀어 오른 풍선처럼, 열화신단의 기운은 내 전신을 가득 채우고 있었다.

‘문제는 이 풍선이 언제 터질지 모른다는 거지만.’

그러니 그 전에 풍양을 쓰러트려야 한다.

나는 속에서 부글부글 끓어오르는 열기를 느끼며 철창을 고쳐 잡았다.

“덤벼.”

풍양이 입술을 깨물었다.

“어린놈이 벌써부터 기고만장하군. 네놈 정도로는 어림도 없다.”

“그런 것치곤 꽤 긴장한 것 같은데.”

“맹수는 토끼를 잡는 일에도 최선을 다하는 법이지.”

“근데 맹수는 토끼 잡을 때 잠력단 안 먹잖아.”

“……!”

풍양의 낯빛 위로 경악이 스쳤다. 입을 벌린 채 나를 응시하던 놈이 더듬더듬 물었다.

“자, 잠력단이라고?”

“그래, 잠력단.”

“그 이름을 네가 어떻게?”

“기업 비밀이다, 이 새끼야.”

“혹시 네놈도?”

“뭐, 비슷한 거 먹긴 했지.”

열화신단이라고 말하면 알까 모르겠다.

잠력단이랑 비교하면 안정성은 영 꽝이고, 효과가 어느 정도인지는 지금부터 알아볼 생각이다.

“넌 뒈졌어.”

마지막 한마디와 함께 땅을 박찼다.

쐐애애액!



* * *



풍양은 심란했다.

‘저놈이 어떻게 잠력단의 존재를 알고 있지?’

잠력단의 존재는 무덤까지 안고 가야 할 비밀이다.

언젠가 목숨을 구해 줄 숨겨 둔 한 수이기도 했지만, 세상에 알려진다면 피바람을 불러일으킬 기물(奇物)이기 때문이다.

복용자가 가진 힘의 두 배, 세 배를 끌어 올릴 수 있는 효능만 봐도 천하의 무인들이 군침을 삼키고 달려들 텐데.

그러나 그보다 더 큰 문제는 따로 있었다.

‘사마외도(邪魔外道)의 유산이니까.’

정마대전 이후 천하 무림은 정파 무림의 손아귀에 들어갔다.

풍양이 사마외도의 기연을 이었다는 소문이라도 퍼진다면 태원진가가 아니라 천하 무림이 그를 쫓기 시작할 것이다.

‘산서잠룡 진태경…… 반드시 죽여서 후환을 없애야 한다.’

풍양은 이를 악물고 무공을 펼쳤다.

단 몇 년간의 수련으로 어느덧 칠 성의 경지에 오른 적혈십이도(赤血十二刀)다. 나이로도, 무공으로도 턱없이 부족한 저 어린놈을 죽이기에는 차고 넘친다.

“죽엇!”

쉬잉-!

적혈십이도는 패도적인 무공, 곡도에서 쭉 뻗어 나간 붉은 도기가 사방을 난도질했다. 그 흉험한 기세에 땅거죽이 갈라지고, 바람이 터져 나갔다.

그러나 정작 베어야 할 목표는 이미 그곳에 없었다.

딱 반걸음 차이로 공격을 피해 낸 진태경이 창을 찔렀다.

쐐애애액!

목젖을 노리고 찔러 들어오는 창날. 황급히 고개를 꺾어 공격을 피한 풍양은 가슴 한구석이 서늘해졌다.

‘빠르다.’

빠르고 정확하다. 절정 고수의 상징인 검기상인(劍氣傷人)의 경지에까지는 이르지 못했지만 움직임은 이미 그를 따라잡고 있었다.

‘설마 이 녀석도 잠력단을? 아니다. 나와는 전혀 달라.’

이미 잠력단을 몇 번 복용한 전력이 있는 풍양이다.

전신이 시뻘겋게 달아오른 진태경의 모습으로 앞서 그가 삼킨 것이 잠력단이 아니라는 사실을 알 수 있었다.

‘그럼 도대체 뭘…… 헛!’

풍양은 생각을 이어 갈 수 없었다. 마침내 공세를 잡은 진태경이 본격적으로 진가창법을 펼쳐 내기 시작했기 때문이었다.

쉬쉬쉬쉬쉭!

소나기처럼 쏟아지는 수십 개의 창영(槍影). 보기만 해도 숨이 막히는 광경이다. 아니, 착각이 아니라 실제로도 그랬다.

풍양의 이마에서 땀 한 방울이 굴러떨어졌다.

‘이건…….’

열양지기.

그것도 절정 고수인 자신에게까지 영향을 줄 만큼 엄청난 열양지기다. 앞서 싸웠던 항산호 철무백도 열양지기의 소유자였지만 지금 진태경이 뿜어내는 것에 비할 바가 아니다.

‘영단, 열양 계열의 영단을 먹었구나!’

후우우웅!

알아챈다고 달라지는 것은 없었다. 아찔한 열기와 날카로운 공격. 연달아 물러서며 창날을 피하는 데에 급급하던 풍양이 입술을 질끈 깨물었다.

‘고작 이런 어린놈한테!’

일평생을 치열하게 살아온 그다. 잠력단까지 복용한 지금, 이제야 이름을 알리기 시작한 어린놈을 상대로 물러서는 자신이 수치스러웠다.

그 분노가 고스란히 곡도에 실렸다. 도신 위로 피어오른 도기가 그 어느 때보다 붉게 타올랐다.

쉬이익!

진가창법과 적혈십이도는 사용하는 병기와 투로는 다를지 몰라도 패도적인 무공이라는 공통점이 있다.

눈 깜빡할 시간, 진무경의 철창과 풍양의 곡도가 십여 합의 치열한 격돌 끝에 떨어졌다.

“음.”

먼저 물러난 것은 진태경이었다. 찢어진 손아귀에서는 피가 흘렀고, 무겁고 견고하던 철창은 예리한 도기에 잘려 나가 채 반도 남지 않았다.

“멍청한 놈.”

풍양은 득의양양한 웃음을 지었다. 무인이 병장기를 잃었다는 것은 패배를 의미했다.

오로지 권각으로 일가를 이룬 항산호 철무백도 자신에게 무릎을 꿇었는데, 아직 절정의 벽도 넘지 못한 진태경은 무기를 잃은 순간 이미 죽은 것이나 마찬가지다.

“정면 승부로 날 꺾을 수 있을 거라 생각했더냐?”

진태경이 손아귀에 묻은 피를 문질러 닦으며 대답했다.

“아니, 그 대신 귀중한 정보를 알았지.”

“……귀중한 정보?”

“그래, 너의 공격 패턴을 알았다.”

“패, 뭐?”

“너의 공격 패턴은 강강강강강이다.”

이건 무슨 개소린가.

자신의 무공에 관한 이야기라는 건 알겠는데 패 뭐시기라는 말은 난생처음 들어 본다. 게다가 강강강강강이라니?

풍양은 살기 어린 눈빛으로 진태경을 노려봤다.

“헛소리를 한 대가로 사지 근맥을 잘라 주마.”

진태경이 심드렁한 얼굴로 입을 열었다.

“사지 자르고 뽑는 거 되게 좋아하네. 사지 성애자야?”

“이 애새끼가…….”

“이 늙은 새끼가…….”

풍양은 깊게 심호흡했다. 그는 절정 고수였고 일평생을 냉철한 이성의 소유자로 살았다. 하지만 분노로 뚝뚝 끊기는 목소리만큼은 어쩔 수 없었다.

“넌, 반드시, 내 손으로, 죽인다.”

“난, 가끔, 사지를, 자른다, 가끔은, 이런 내가, 별로다.”

그는 인내심이 뚝 끊어지는 것을 느꼈다. 단언컨대 근 십 년간 이 정도로 분노한 적은 처음이다.

“크아아악!”

비명인지 고함인지 모를 괴성을 내지른 풍양은 광인(狂人)처럼 돌진했다.

그 어떤 초식도, 무공도 없이 있는 힘껏 진태경의 정수리 위로 곡도를 내리쳤다.

“죽엇!”

그때였다. 살기로 번들거리는 풍양의 핏빛 눈동자에 진태경의 담담한 표정이 비친 것은.

순간 찬물을 뒤집어쓴 것처럼 정신이 번쩍 들었다.

‘뭔가 잘못됐다.’

풍양은 공력을 있는 힘껏 끌어올렸다.

호신강기가 일어남과 동시에 텅 비어 있던 진태경의 손아귀에서 비수가 번쩍였다.

푹!
```

## Current accepted English baseline

```markdown
# Chapter 118

“Was it fun being the only one shoving pills down your throat?”

“What?”

“I asked if it was fun shoving pills down your throat all by yourself.”

Pung Yang let out a hollow laugh.

*For a mere brat barely twenty, his speech was far too disrespectful. Had being born the youngest young master of the Jin Family of Taiyuan and being called the Sleeping Dragon made him think he could get away with anything?*

“What a brat. Heh.”

The empty laughter soon died away, and murderous eyes took its place.

“Must you see the coffin before you shed tears?”

Jin Taekyung’s eyes widened.

“Wow, hearing that line in real life makes it sound really weird. Try it again.”

“You’re a brat who can’t be reasoned with.”

As he approached at a leisurely pace, Pung Yang wondered how he could make that young brat beg for his life.

His usual method was to pull out the tongue and slowly break all four limbs. But he couldn’t treat a valuable body that knew the Jin Family of Taiyuan’s martial arts so carelessly.

A reasonable compromise was necessary.

*If I sever the meridians in his legs, he’ll quiet down.*

He had already crossed an irreversible river with the Jin Family of Taiyuan. Once this fight was over, Pung Yang planned to retreat into some remote mountain valley untouched by human feet, refine his martial arts, and then return to the Murim.

The Red Wind Band had been annihilated, but he could gather a force again whenever he wanted. The Murim was a place ruled by the strong, after all.

“Everything that happened was brought on by you, so don’t blame me.”

Pung Yang was just tightening his grip on the curved saber when—

“Ah, wait a second.”

Jin Taekyung held up a hand, then casually tossed something into his mouth.

The action was so natural that Pung Yang couldn’t help stopping.

*What is he doing?*

His question was answered a moment later.

After Jin Taekyung’s body shuddered once, tremendous heat began to rise from every inch of him.

* * *

I had only one option left.

To make one last gamble with the Blazing Flame Divine Pill.

It was a dangerous choice, but it was a hundred times better than dying after being forced to spit out the Jin Family’s martial arts formulas for Pung Yang.

Gulp.

True to its name, the divine elixir melted the moment it touched my tongue and slid down my throat. The problem began after that.

*Ding.*

> **System**
> - You have taken the **Blazing Flame Divine Pill**.
> - **Circulate your qi** to control your energy.

It was hot. The thirty years of internal energy contained within the Blazing Flame Divine Pill spread through every part of my body like wildfire.

> **System**
> - You have temporarily gained the **Scorching Yang Qi** attribute.
> - Your **internal energy** has temporarily increased to 45 years.
> - If you cannot control your energy, you may die!
> - Quest, **Divine Pill Absorption**, has been created.

I had no time to check the System notifications that continued ringing in my ears. Controlling the Blazing Flame Divine Pill’s energy rampaging through my body was already more than enough.

“Hoo. Hooooo.”

I felt like a human pressure cooker. It was as though a real fire had broken out inside me, and wisps of smoke rose from my entire body.

The snow covering the ground beneath my feet melted, and the damp earth softened until it flowed like water.

*I expected something this bad, but this is…*

It was far beyond my imagination. I couldn’t even scream. I could only tremble as Pung Yang’s voice pierced my ears.

“What have you done?”

Seeing the bewilderment on his face actually made the heat subside a little.

I forced the corners of my mouth upward and answered.

“What else? I’m going all in.”

“You brat!”

Had he sensed something ominous in my answer? Pung Yang’s curved saber flew toward me at a blinding speed. A red strand of saber qi extended from the blade and aimed for my chest.

*Swish!*

Death passed me by at a distance of exactly half a step. The curved saber missed its target and drew another chaotic arc.

*Shh-shh-shh-shhk!*

But once again, the blade only cut through empty air. Pung Yang’s face twisted as he stared at me, already backed away.

“You…!”

“What, asshole?”

I answered as casually as I could, but the person most surprised was me. When we had crossed hands earlier, I hadn’t been able to dodge so easily.

This was on an entirely different level from before, when Pung Yang’s overwhelming aura and saber qi had forced me to do nothing but evade.

*Since when has my body felt this light?*

The instant I thought I needed to avoid an attack, my body moved faster than ever before. And that wasn’t the only thing that had changed.

*I can see everything clearly.*

I could see and read each of Pung Yang’s movements. If I could see the attacks, there was no reason I couldn’t evade them. I felt like I could dodge even saber force, not just saber qi.

At last, I understood why.

*It’s because of my internal energy.*

My original fifteen years of internal energy had merged with the thirty years from the Blazing Flame Divine Pill. I couldn’t control it perfectly, but that didn’t mean the power of thirty years of internal energy had simply disappeared.

Like an overinflated balloon, the Blazing Flame Divine Pill’s energy filled my entire body.

*The problem is that I have no idea when this balloon will burst.*

So I had to take down Pung Yang before that happened.

Feeling the heat bubbling up inside me, I adjusted my grip on the iron spear.

“Come at me.”

Pung Yang bit his lip.

“Young brat, you’re already getting cocky. Someone like you is nowhere near strong enough.”

“You look pretty tense for someone saying that.”

“A wild beast gives its all even when catching a rabbit.”

“But a wild beast doesn’t take a Temporary Strength Pill to catch a rabbit.”

“...!”

Shock flashed across Pung Yang’s face. He stared at me with his mouth hanging open, then stammered.

“Y-You mean the Temporary Strength Pill?”

“Yeah. The Temporary Strength Pill.”

“How do you know that name?”

“Corporate secret, asshole.”

“Did you take one too?”

“Well, I did eat something similar.”

I wondered whether he would recognize the name if I called it the Blazing Flame Divine Pill.

Compared to the Temporary Strength Pill, its stability was complete garbage. I intended to find out exactly how powerful its effects were starting now.

“You’re fucking dead.”

With those final words, I kicked off the ground.

*Shweeeeeek!*

* * *

Pung Yang was deeply troubled.

*How does that brat know about the Temporary Strength Pill?*

The existence of the Temporary Strength Pill was a secret he had to take to his grave.

It was a hidden trump card that might save his life someday. But if its existence became known, it would be a wondrous object capable of bringing a bloodbath to the entire world.

Just the fact that it could draw out two or three times the power of the person who took it would be enough to make martial artists throughout the land salivate and come running.

But there was an even greater problem.

*It’s a legacy of demonic, heterodox arts.*

After the Great Faction War, the Murim had fallen into the hands of the orthodox factions.

If even a rumor spread that Pung Yang had inherited the legacy of demonic, heterodox arts, it wouldn’t be only the Jin Family of Taiyuan pursuing him. The entire Murim would come after him.

*Jin Taekyung, the Sleeping Dragon of Shanxi… I must kill him and eliminate the trouble he’ll cause later.*

Pung Yang gritted his teeth and unleashed his martial arts.

After only a few years of training, he had already mastered seventy percent of the Crimson Blood Twelve Sabers. That was more than enough to kill a brat hopelessly beneath him in both age and martial arts.

“Die!”

*Shiiing!*

The Crimson Blood Twelve Sabers was a domineering martial art. Red saber qi shot from the curved saber and slashed wildly in every direction. The fierce momentum split open the surface of the earth and burst the air apart.

Yet the target he needed to cut was no longer there.

Jin Taekyung dodged the attack by exactly half a step and thrust his spear.

*Shweeeeeek!*

The spearhead drove toward Pung Yang’s throat. Pung Yang hastily twisted his head aside to evade it, and a chill settled in his chest.

*Fast.*

Fast and accurate. He had yet to reach the stage where Sword Energy could injure a person—the hallmark of a Peak master—but his movements had already caught up to Pung Yang’s.

*Could this brat have taken the Temporary Strength Pill too? No. It’s completely different from mine.*

Pung Yang had already taken the Temporary Strength Pill several times.

From Jin Taekyung’s body, which had turned bright red with heat, Pung Yang could tell that what he had swallowed earlier was not the Temporary Strength Pill.

*Then what did he… Wait!*

Pung Yang couldn’t continue thinking. Jin Taekyung had finally seized the initiative and begun to unleash the Jin Family’s Spear Technique in earnest.

*Shh-shh-shh-shh-shhk!*

Dozens of spear shadows poured down like a rain shower. It was a suffocating sight.

No, it wasn’t just an illusion. It really was suffocating.

A bead of sweat rolled down Pung Yang’s forehead.

*This is…*

Scorching Yang Qi.

And not just any Scorching Yang Qi—it was powerful enough to affect even Pung Yang, a Peak master himself. The Tiger of Mount Heng, Cheol Mubaek, had also possessed Scorching Yang Qi, but it couldn’t compare to what Jin Taekyung was emitting now.

*He ate a divine elixir—a Scorching Yang-type divine elixir!*

*Whooooom!*

Recognizing it changed nothing. The heat was dizzying, and the attacks were sharp. Pung Yang bit down hard on his lip as he repeatedly retreated, barely managing to evade the spearhead.

*Against a brat this young!*

He had lived his entire life fiercely. Now, even after taking the Temporary Strength Pill, he felt humiliated to be driven back by a young brat who had only just begun making a name for himself.

That anger flowed straight into his curved saber. The saber qi rising over the blade burned redder than ever.

*Hiss!*

The Jin Family’s Spear Technique and the Crimson Blood Twelve Sabers differed in their weapons and forms, but they shared one thing in common: both were domineering martial arts.

In the blink of an eye, Jin Mukyung’s iron spear and Pung Yang’s curved saber finally parted after more than ten fierce exchanges.

“Hmm.”

Jin Taekyung was the first to retreat. Blood flowed from his torn palm, and the heavy, sturdy iron spear had been cut by the sharp saber qi until less than half of it remained.

“You fool.”

Pung Yang smiled triumphantly. A martial artist losing their weapon meant defeat.

Even the Tiger of Mount Heng, Cheol Mubaek, who had built his reputation entirely with his fists and feet, had knelt before Pung Yang. Jin Taekyung hadn’t even crossed the wall into the Peak realm yet. The moment he lost his weapon, he was as good as dead.

“Did you think you could defeat me in a head-on fight?”

Jin Taekyung rubbed the blood from his palm and answered.

“No. But I did learn some valuable information.”

“...Valuable information?”

“Yeah. I learned your attack pattern.”

“Pat—what?”

“Your attack pattern is strong, strong, strong, strong, strong.”

*What kind of bullshit is this?*

Pung Yang understood that the brat was talking about his martial arts, but he had never heard of this “pattern-whatever” before. And what did he mean by strong, strong, strong, strong, strong?

Pung Yang glared at Jin Taekyung with murderous eyes.

“I’ll sever the meridians in all four of your limbs as payment for talking nonsense.”

Jin Taekyung opened his mouth with a bored expression.

“You really like cutting off and pulling out people’s limbs. Are you a limb fetishist?”

“You little brat…”

“You old bastard…”

Pung Yang drew a deep breath. He was a Peak master who had spent his entire life possessing a cool, rational mind. But he couldn’t stop his voice from breaking into pieces with anger.

“You. Will. Die. By. My. Hand.”

“I. Sometimes. Cut off limbs. Sometimes, I don’t like this version of myself.”

He felt his patience snap. He could swear that he had never been this furious in nearly ten years.

“Graaaargh!”

Pung Yang charged like a madman, emitting a howl that could have been either a scream or a roar.

Without using a single form or martial art, he brought the curved saber down over the crown of Jin Taekyung’s head with all his strength.

“Die!”

That was when Jin Taekyung’s calm expression was reflected in Pung Yang’s bloodshot eyes gleaming with killing intent.

In an instant, his mind snapped clear as though someone had dumped cold water over him.

*Something’s wrong.*

Pung Yang drew up his internal energy with all his might.

As his Body-Protecting Qi rose, a dagger flashed in Jin Taekyung’s previously empty hand.

*Shnk!*
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 118`.

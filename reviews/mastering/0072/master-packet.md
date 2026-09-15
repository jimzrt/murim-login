# Master Edit Task — Chapter 72

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
| 조필     | **Jopil**          |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 천무학관   | **Heaven's Gate Temple**         |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 큰형     | **eldest brother**                           |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 레벨               | **Level**                      |
| 보상               | **Reward**                     |
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 큰형 | kinship | Eldest older brother, not a generic older brother. | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 65–69

## Plot

Jin Mukyung is astonished that Jin Taekyung has become a First Rate martial artist approaching the Peak realm. When Mukyung uses internal energy, he defeats Taekyung and destroys the pavilion. Taekyung and the badly injured Hyuk Mujin are taken to the Medicine King Hall, while the Jin Family mistakes the incident for an assassin’s attack and begins a pursuit for the Head Elder’s possible hidden disciple. Mujin receives public credit for protecting Taekyung, leading to speculation that he may become the next Master of the Gatekeeper Pavilion.

Mukyung reunites with Jin Wikyung after three years but remains detached and focused on training. Wikyung sends Wipeng and thirty elites south under the cover of pursuing the nonexistent assassin, while secretly preparing to summon every sect in Shanxi Province on New Year’s Day and potentially seek the Alliance Leader position. Wikyung finds no mention of Dark Heaven in the family records. Gong Yacheong continues recovering and will oversee the rebuilt Sakju Branch, with Socheon and Soyul planning to join him in six months.

While Taekyung’s residence is rebuilt, Wikyung places him and Mukyung together temporarily. Mukyung imposes rules of polite speech, silence, and obedience regarding the training hall. After Mukyung harshly beats Taekyung with his scabbard, Taekyung sincerely asks to become stronger. Mukyung agrees to rebuild his martial arts from the fundamentals through practical, real-combat training.

The System grants Taekyung the Return achievement and Returnee title, activating Login and Logout and increasing all stats by ten. It then creates the Peak-Grade Quest “[Trial? Training?],” requiring Mukyung’s recognition before the remaining cohabitation period ends. Logout is restricted, and Mukyung orders Taekyung to bring his spear for training.

## Continuity

- Jin Mukyung defeated Taekyung in their spar, destroying Taekyung’s pavilion. Taekyung survived; Hyuk Mujin remains badly injured and under treatment.
- The Jin Family is pursuing an unidentified assassin believed possibly to be the Head Elder’s hidden disciple. The assassin’s identity, sponsor, and possible connection to Song Sword Sect remain unknown.
- Jin Mukyung has begun training Taekyung harshly and intends to reconstruct his inadequate martial arts from the basics.
- The Peak-Grade Quest “[Trial? Training?]” requires Jin Mukyung’s recognition. Its reward and failure conditions remain unknown, and Logout is restricted for its duration.
- Taekyung is Level 50 with fifty unspent points and fifteen years of Internal Energy after investing fifty points in Agility. The Returnee title grants All Stats +10 and activates Login and Logout.
- Jin Wikyung plans a New Year’s Day summons for all Shanxi sects and may pursue the Alliance Leader position; whether the sects will attend and whether he will become Alliance Leader remain unresolved.
- Wipeng is traveling south with thirty Jin Family elites under the pretext of pursuing the assassin.
- Gong Yacheong will lead the rebuilt Sakju Branch; Socheon and Soyul intend to accompany him in six months. Soyul still does not know that her parents are dead.
- Mukyung has spent three years attempting to open the Ren and Du meridians.
- Hyuk Mujin’s possible promotion to Master of the Gatekeeper Pavilion remains unresolved.

## Translation Decisions

- Use **First Rate**, **Peak**, **Internal Energy**, **Medicine King Hall**, **Master of the Gatekeeper Pavilion**, and **Alliance Leader** consistently.
- Render **삼재검법** as **Three Calamities Sword Technique**.
- Use **gongcheong seokyu** for 공청석유, with a footnote explaining the rare-elixir and petroleum wordplay.
- Use **junzi** for 군자, with a footnote explaining the Confucian ideal of a morally upright gentleman.
- Retain **Hyung-nim** for Taekyung’s deferential 형님, distinct from casual **hyung**.
- Use **Sleep Mode**, **Return**, **Returnee**, **Login**, **Logout**, **Ren and Du meridians**, **Heart Demon**, and **Quest** for established System and cultivation terminology.
- Render **두 시진** as **two hours**, **권각술** as **fist-and-kicking technique**, and **인정** in the Quest mission as **recognition**.
- Retain **Asmodeus** for 아스모데우스 and **Demon King Asmodeus** for 마왕 아스모데우스.

### Prior accepted reading-copy tails

#### Chapter 70 tail (verified mastered)

…
possible and spotted him below. “Hah!” With a short shout, his sword moved. Whoosh! Shh-shh-shhk! The wind split along the blade. Jin Mukyung moved without hesitation, thrusting and slashing through empty space at the speed of a ray of light. About fifteen minutes passed before he lowered his sword and released a long breath. “Hoo.” He wiped away his sweat with his sleeve, then turned toward me. It seemed he had noticed my presence some time ago. “Tell me.” The words came out of nowhere. Caught off guard, I asked, “Tell you what?” “About the martial art I just performed.” “Uh, well, first of all, it was really fast…” “For the record, if you spout pointless bullshit like ‘It was fast’ or ‘It was strong,’ I’ll kill you.” *He’s a mind reader.* I racked my brain for an answer that would keep me alive. What had Jin Mukyung’s martial art been like? As I thought about it carefully, a vague impression began to surface. “Rough?” Jin Mukyung’s eyebrow twitched. *Was that the right answer?* “Did you just speak informally to me?” “…It seemed rough.” “Even a little kid could say that. Be more specific.” The image in my head gradually became clearer. I remembered the blade pouring down upon an imaginary enemy and the movements that accompanied it. Fast and unrestrained. And the aura pressing down from every direction. It was like… “A waterfall?” “…” “Huh?” *What? Was that the right answer?* After a long silence, Jin Mukyung abruptly swung his scabbard. Smack! “Ow! Why did you hit me?” “Just because.” He stared at me with a strange look in his eyes. “How did someone like you ever come out?” Was that an insult or a compliment? I had no idea what he truly meant, but I had to hear the answer to his question if only because I felt wronged. Rubbing my throbbing forehead, I asked: “So, was that the correct answer?” “There are thousands of martial arts manuals in Heaven’s Gate Temple. They were arrangements left behind by the departed Seniors who hoped to cultivate the younger generation of the orthodox Murim.” “And?” “The Falling Flow Sword you just saw is one of them. I found it buried deep in the archives.” Falling flow. In other words, falling water. A waterfall. I had simply blurted out the first thing that came to mind, but it had actually been the right answer. “Oh, ooh.” *Am I really a genius?* If I could recognize martial arts like this after only two months of learning them, I was afraid of how strong I might become in the future. Even I found myself frightening. “Surely you’re not having the embarrassing thought that you’re a genius or something after managing only that much?” “…” *He really is a mind reader.* Still, I seemed to have at least a little talent. Unable to let go of the thought, I cautiously asked, “Can everyone normally do this much?” Jin Mukyung flinched. “O-Of course. Anyone with eyes should be able to guess this much.” “Come on.” “‘Come on’? Want me to pluck out one of your eyes?” “…That might be a bit much.” *Why is this bastard being especially stone-faced today? Did something unpleasant happen?* Even after I backed down, Jin Mukyung could not contain his anger. He kept huffing angrily. “It’s basic. Basic. Everyone can do it.” “I said I get it. Why do you keep getting angry? You’re scaring me.” “Are you rebelling against me? Is it because you’re going through the storm-and-stress stage of adolescence? Do you want to get beaten with the Twelve Gale Fists?” I did not know what the Twelve Gale Fists were, but getting hit by them sounded painful. I shook my head fiercely, but Jin Mukyung’s anger showed no sign of fading. “Do you know martial arts? Huh?” “N-No, sir.” “How long have you been learning martial arts?” The answer slipped out reflexively. “Two months. Two months.” “Right, a bastard who’s only been at it for two months… What? Two months?” Jin Mukyung glared at me with bloodshot eyes. “Not three years, but two months?” This was an emergency. The social instincts I had gained through seven years of working life shone at that moment. I hurriedly opened my mouth, making sure to emphasize one particular part. “Three years! Plus two months!” Jin Mukyung’s fist had been trembling as though he had suffered a stroke, but it steadied again. For some reason, even his voice seemed slightly gentler. “You little bastard. You startled me.” *You startled me even more, you son of a bitch.* *Does he have anger-management issues?* If he asked Jin Wikyung, my lie would be exposed immediately. But at least I would avoid the misfortune of experiencing the Twelve Gale Fists right now. In any case, Jin Mukyung’s anger subsided in the meantime. “I’ll say this only once. Listen carefully.” “I’ll engrave it on my heart.” I bowed deeply, and he declared in a domineering tone, “I teach. You obey.” “…” *Is this a dog-training school or what?* “There will be no objections. Why? Because I’m stronger than you.” It was true, so I had no desire to argue. Money, power, and force. Their forms might differ, but the world always revolved around the strong. I wanted to stand at its center. “What will you do?” My answer had been decided a long time ago.

#### Chapter 71 tail (verified mastered)

…
martial art I had learned. *I’ll show you what a real fight looks like.* With all my strength, I kicked Jin Mukyung in the shin as he grinned triumphantly. It was a decisive technique known as a soccer kick, or simply a shin-kick. I had never seen anyone stay fine after taking one of these. Clang! Add one more to the list. “You fucking—” “You idiot.” Jin Mukyung looked down at me as I collapsed, clutching my foot. His expression seemed to say that I was the most pathetic person alive. “Fifth… Never mind. I’m getting tired of talking.” He pulled a flat metal plate from beneath his pant leg and strode toward me. I tried to limp to my feet, but he kicked my ankle out from under me and sent me back down. *Damn it.* It was over. If I used Inventory, I might have a chance to turn things around, but I did not want to do something so blatantly suspicious right in front of him. I lowered my head with a sigh. “Let’s stop.” “You want to stop?” I lifted my head at his hard voice. Jin Mukyung’s face had gone cold. “After only this much?” The man who had been grinning as he gleefully beat me only moments ago was nowhere to be seen. His emotionless gaze made my skin prickle. My Adam’s apple bobbed. Gulp. Almost simultaneously with the sound of me swallowing, the wooden sword slammed into my right shoulder. My arm buckled with a thud, throwing me off balance. “Guh. What the hell are you doing…?” Jin Mukyung ignored me and swung the wooden sword again. The Jin Mukyung standing before me now seemed unable to hear the voice of the defeated. Thud. Thud. Thud. He struck my left arm, then both legs. Only then did his hand stop. “You just had all four limbs cut off. By a vicious Peak master of the dark path who is several times stronger than you.” “…” “If he were even nastier, he’d have other methods.” Tap-tap-tap. The instant Jin Mukyung’s hand blurred, my entire body went rigid and my tongue curled back. The System immediately alerted me to the abnormal conditions. Beep! > **System** > > - The **Paralysis Acupoint** has been subdued. You will be paralyzed for two hours! > > - The **Mute Acupoint** has been subdued. You will be unable to make a sound for two hours! I could not move so much as a hair or make a single sound. A breathing corpse. In my current state, even a child could kill me. *Jin Mukyung. You insane bastard!* The curses could only circle inside my head, unable to escape my lips. All I could do was glare at him. Jin Mukyung calmly met my furious gaze. “Tendon-Splitting and Bone-Twisting is a cruel technique. Within an hour at most, your qi and blood will twist and every bone in your body will be crushed. Even if you miraculously survive, you’ll either go insane or spend the rest of your life crippled.” “…” “Do you think you could endure that pain? You’d probably forget who you are within fifteen minutes.” My stomach churned. Not because of his explanation of Tendon-Splitting and Bone-Twisting. It was Jin Mukyung’s eyes. There was no emotion in them. Those black eyes were unfamiliar and frightening. *Could Jin Mukyung really be about to kill me?* No. That was impossible. I was Jin Taekyung. A direct descendant of the Jin Family of Taiyuan, and Jin Mukyung’s only younger brother. But what he did next went far beyond anything I had expected. “Don’t worry. I’ll send you off without pain.” Something cold touched my throat as he spoke in a low voice. It was the metal plate Jin Mukyung had pulled out earlier. Its thin, sharp edge slowly dug into my flesh. *I’m going to die? Like this?* I had survived dozens of brushes with death. In Gates, and in Murim. I had struggled all this time to survive somehow… And now I was about to die without even being able to blink. To that bastard who was supposed to be my biological older brother, even though we did not share a single drop of blood! *What the fuck kind of situation is this?* My body rigid, I could only stare at the ceiling as the voice of the Reaper reached my ears. “Die.” Slice. The strength drained from my entire body. I felt hot blood trickling down my neck. Jin Taekyung. Aged twenty-seven. Gone to sleep in Murim. I slowly closed my eyes. “…” No, wait. Something was wrong. *My acupoints were sealed, but I just closed my eyes?* At that moment— Ding. > **System** > > - The **Paralysis Acupoint** has been released. The paralysis has ended! > > - The **Mute Acupoint** has been released. You can speak freely! “Get up.” “…” At Jin Mukyung’s voice, I slowly opened my eyes. All five of my senses were sharp and clear, proving that I was alive. *How?* I hurriedly felt the back of my neck. The cut stung, and blood came away on my fingers, but there were only a few drops of it. Everything else had been an illusion brought on by the fear and tension of death. “Remember.” His cold voice continued—the same voice that had pronounced my death only seconds earlier. “You died once today.”

## Korean source

```text
＃72화



“넌 오늘 한 번 죽었다.”

서늘한 목소리가 이어졌다.

“사지가 잘려서, 분근착골을 당해서, 목이 베여서. 고통의 크기나 형태는 달라도 넌 죽었다. 확실하게.”

살았다는 안도감이 사라지자 그 빈자리를 채운 건 분노였다.

나는 후들거리는 다리로 일어섰다. 입 안 가득 고여 있는 핏물을 꿀꺽 삼키고 진무경을 노려봤다.

‘이런 미친 새끼.’

당장이라도 저 잘난 면상에 주먹을 꽂아 넣고 싶었지만 꾹 참았다. 내가 진무경보다 약해서가 아니다. 놈의 말이 틀리지 않다는 걸 알기 때문이다.

“……그래서? 하고 싶은 말이 뭐지?”

기다렸다는 듯이 대답이 튀어나왔다.

“네 명줄이 얼마 안 남았다는 얘기다.”

“뭐?”

“넌 반쪽짜리야. 무인도, 낭인도 아닌 반쪽짜리. 너처럼 어설픈 놈이 무림에 나가면 죽기 딱 좋지.”

반쪽짜리.

어쩌면 지금의 내 상태를 가장 정확히 표현한 말일지도 모르겠다. 나는 헌터인 동시에 무림인이니까.

“산서잠룡? 초일류 고수? 지나가던 개가 웃겠다. 넌 단순한 싸움꾼이야. 무인치고는 어설프고 낭인처럼 실리적으로 싸우는 것도 아니지. 운이 좋아 살아남은 걸 네 실력이라고 착각하지 마라.”

나는 간신히 입을 열었다.

“그럼 조필은? 네 말대로면 그것도 운인가?”

“일문일살 조필? 보나 마나 적을 앞에 두고 방심할 만큼 멍청한 놈이었겠지. 너는 그 상황을 뒤집을 만한 마지막 한 수가 있었던 거고.”

“……!”

“왜? 직접 보지도 않았으면서 너무 정확하게 맞췄다고 생각하나?”

진무경이 혀를 찼다.

“귀먹은 노인네도 태원진가의 삼공자가 망나니라는 사실을 아는데 조필이 몰랐을까. 방심한 순간 놈도 끝장난 거지.”

이 새끼 스토커야, 뭐야.

부처님 손바닥 위의 손오공이 된 기분이다. 그의 추측은 그만큼 정확했다.

“분명히 말해 두는데.”

진무경이 가라앉은 눈으로 나를 응시했다.

“그 운이 통하는 것도 여기까지야.”

“…….”

“무림에는 온갖 괴물들이 득실거린다. 그리고 그들은 조필처럼 방심하지 않아. 넌 더 이상 망나니 삼공자가 아니라 산서잠룡이니까.”

말 한마디, 한마디가 폐부를 찌른다. 진무경의 말은 모두 사실이었고, 이제는 현실을 받아들여야 할 때다.

“제기랄.”

맞다. 나는 반쪽짜리다.

시스템이라는 인생 최고의 행운 덕분에 어찌어찌 살아남았지만 그것도 딱 여기까지인 모양이다.

하지만…….

‘역시 난 운이 좋아.’

문제를 일찍 발견한 것도 모자라 풀이를 도와줄 훌륭한 해결사까지 내 눈앞에 있다.

“도와줘.”

진무경.

이미 완성된 절정의 무인이자 무공의 천재.

그리고.

“……형.”

내 형이다.

띠링.



제한 시간 : 9일 20시간 23분



* * *



무림인이라는 족속은 자존심이 강하다. 녹슨 칼 한 자루를 차고 싸구려 화주를 마시는 삼류 낭인도 그럴진대, 명문대파의 자제들은 그 오만함이 하늘을 찌를 정도다.

“도와줘, 형.”

그런 의미에서 이놈은 사람이 됐다. 삼 년 전이었다면 울먹거리며 큰형님께 달려갔을 텐데…… 성장했다. 기대 이상으로.

‘묘한 녀석이야.’

성격도, 무공도 종잡을 수가 없다. 그건 장점인 동시에 단점이다. 다만 한 가지 확실한 사실은, ‘진짜 고수’에게는 아무것도 통하지 않는다는 거다.

‘하지만 재능은 진짜다.’

진무경은 지난 삼 년간 천무학관에서 수많은 기재를 만났지만 진태경의 성장 속도는 타의 추종을 불허했다.

‘그놈들에게는 없는 장점도 있지.’

무공을 한눈에 파악하는 눈. 뛰어난 실전 감각과 다른 사람의 조언을 받아들이는 귀도 있다.

‘비록 아직은 뒤죽박죽 섞여 있는 반쪽짜리지만.’

시간이 흐른다면 부족한 부분은 채워지고 튀어나온 부분은 들어갈 것이다. 그때 진태경의 무공은 완성된다.

태극(太極)이 조화를 이룬 것처럼.

‘태극이라, 너무 거창한가?’

이거, 슬슬 부담이 되기 시작한다.

하지만 궁금해서 견딜 수가 없다. 저놈이 어떻게 성장할지. 어디까지 올라갈지.

‘갈 길이 바쁘겠군.’

늦어도 보름 안에는 출발해 천무학관으로 돌아가야 한다. 진무경은 마침내 입을 열었다.

“뭐 해? 창 들어.”

“형!”

환하게 밝아지는 진태경의 얼굴을 보니, 문득 드는 생각이 있었다.

‘그런데 이 자식이 언제부터 말 놨지?’

훈련 강도가 한 단계 올라가는 순간이었다.



* * *



쾅.

진위경은 잔뜩 충혈된 눈으로 마지막 서류에 인장을 찍었다.

근 열 시진에 달하는 중노동에서 해방됐지만 전혀 기쁘지 않았다. 어차피 내일 아침이면 새로운 일거리가 쌓여 있을 테니까.

‘이것들이 나 몰래 새끼를 치나.’

그나마 슬슬 끝이 보인다는 게 한 줄기 위안일까.

최종 검토까지 끝낸 진위경이 작은 종을 흔들었다. 맑은 종소리가 채 사라지기도 전에 건장한 체격의 하인 둘이 나타났다.

“부르셨습니까, 소가주님.”

“가져가게.”

“예.”

능숙한 솜씨로 수레에 서류를 차곡차곡 쌓은 하인들이 물러가려던 그때였다.

“아, 자네는 남고.”

지목당한 하인이 눈을 동그랗게 떴다.

“저 말씀이십니까?”

“맞네, 자네.”

하인과 단둘이 남게 된 진위경은 근엄한 목소리로 말문을 열었다.

“그래, 요즘 일은 할 만한가?”

“예에. 소가주님의 은덕 덕분입죠.”

“뭐 불편한 건 없고?”

“어이구, 그럴 리가요.”

하인, 칠득이는 연신 고개만 끄덕거렸다. 천자문도 못 뗀 까막눈이지만 그에게도 듣는 귀가 있고 보는 눈이 있다.

이번 전쟁에서 승리한 태원진가는 산서제일가로 우뚝 섰고 소가주인 진위경은 빠른 수습과 공정한 대처로 군자검(君子劍)이라 불리기 시작했다.

‘그런 대단하신 분께서 왜 나를?’

긴장 때문에 가슴이 두근거렸다. 내가 무슨 실수를 했나? 아니면 혹시라도 무공에 대한 재능을 본 건가?

전자라면 큰일이고, 후자라면 인생 역전의 기회다.

‘내가 근골 하나는 튼튼하지. 어릴 때부터 배앓이 한 번 안 했을 정도니까.’

검을 차고 영웅건을 휘날리는 자신의 모습이 벌써부터 눈앞에 어른거린다.

반면 몽롱하게 풀어지는 칠득이의 눈동자를 본 진위경은 흠칫했다.

‘뭐야, 이놈.’

뭔가를 간절히 원하는, 영혼을 바쳐 갈구하는 듯한 눈빛.

사내가 사내에게 보낼 만한 눈빛은 아니다.

‘설마?’

말로만 듣던 남색(男色)…… 아니, 아니다. 섣부른 오해는 금물이다. 믿어 주고 아껴 줘야 하는 태원진가의 식솔 아닌가.

진위경은 애써 의심을 지우며 입을 열었다.

“자네 이야기는 많이 들었네.”

“소, 소인에 관해서 말입니까?”

“물론일세. 오래전부터 눈여겨보고 있었지.”

정확히는 오래전부터가 아니라 사흘 전부터다.

진위경은 매우 중요한 임무를 맡길 믿을 만한 하인을 물색했고, 칠득이는 그가 직접 선발한 최적의 인재였다.

“인의예지(仁義禮智)를 두루 갖춘 인재. 그게 바로 자네였지.”

“이럴 수가……!”

인의예지를 두루 갖춘 특급 하인, 칠득이는 전율했다. 일자무식인 그는 인의예지가 무슨 뜻인지 몰랐지만 인재라는 말은 찰떡같이 알아들었다.

‘내가 인재라고?’

힘 좋고 성실하다는 칭찬은 들어 봤어도 인재라는 소리는 처음 듣는다. 게다가 다른 사람도 아니고 하늘 같은 소가주님께 이런 평가를 듣다니.

이게 꿈인가 생시인가. 칠득이는 극렬한 흥분 상태에 휩싸였다. 너무 흥분한 나머지 혀도 꼬였다.

“저도! 저도 소가주님을 항상 지켜보고 있었습니다!”

순간 진위경이 움찔 몸을 떨었다.

내가 방금 뭘 들은 거지?

“……그게 무슨 소린가?”

“오랫동안 이런 순간을 꿈꿔 왔습니다. 언젠가 소가주님의 뒤에 서는 그 날을!”

“잠깐만. 말이 좀 이상하잖은가. 왜 하필 자네가 내 뒤에 서?”

“헛.”

칠득이는 숨을 삼켰다. 뒤에 서지 말라. 즉, 앞장서서 공을 세우라는 뜻이다.

“그럼 제가 앞에 있겠습니다!”

“아냐! 그것도 이상해!”

하지만 칠득이의 야생마 같은 질주는 멈추지 않았다.

“소인, 이 한 몸 기꺼이 바치겠습니다!”

진위경은 눈앞이 캄캄해졌다!

“안 돼. 하지 마! 바치지 마!”

“소가주님!”

후욱, 후욱. 칠득이는 가쁜 숨을 내쉬었고, 진위경은 공력을 끌어 올렸다.

‘설마 이런 일이 생길 줄이야.’

아무리 그가 열린 사고방식의 소유자라고 해도 이건 아니다.

개인적인 성적 취향이야 그렇다 쳐도, 그 대상이 되는 건 사양이었다. 진위경은 침을 꿀꺽 삼켰다.

“자네, 그럼 정말 남색……?”

칠득이가 눈을 번쩍 떴다. 태원진가의 무인들이 입는 남색 무복을 입을 생각에 가슴이 쿵쾅거렸다.

“예! 시켜만 주십시오!”

“날 노리다니 어림도 없다. 이노옴-!”

철썩!

절정 고수의 따귀는 강력했다. 실 끊어진 인형처럼 풀썩 쓰러진 칠득이를 내려다보며 거친 숨을 내쉬던 진위경이 황급히 종을 울렸다.

띠링. 띵.

“소가주님, 부르셨…… 헉. 칠득아!”

기겁하는 하인에게 진위경이 말했다.

“당장 끌고 나가게!”

“이, 이게 무슨 일입니까?”

“저놈이 나를…… 아닐세, 됐네.”

도저히 식솔에게 할 수 있는 말이 아니다. 그는 난생처음 느껴 보는 분노와 서러움에 눈물이 날 것 같았다.

“조, 조치하겠습니다.”

눈치 빠른 하인이 칠득이를 업었을 때였다. 진위경은 가장 중요한 말을 잊지 않고 덧붙였다.

“그리고 저놈.”

“예?”

“보직 해임하게.”

“아.”

하인은 문득 칠득이가 맡은 임무를 떠올렸다.

‘식사 운반.’

인의예지를 두루 갖춘 특급 하인, 칠득이에게 주어진 가장 중요한 임무는 진무경과 진태경에게 매 끼니를 가져다주는 것이었다.

“내 아우들 근처에 얼씬거리지 못하게 해. 알았나!”

“옛!”



* * *



[훈련 1일 차]

오늘부터 일기를 쓰기로 했다.

이번 수련으로 배운 것을 잊지 않기 위해서다.

진무경의 지도 아래 온종일 창만 휘둘렀다. 하루의 시작과 끝은 늘 비무로 끝난다. 죽도록 맞았지만 버틸 만하다.

난생처음 먹을 갈아 보는데, 이거 은근히 재밌네.



[훈련 2일 차]

오늘도 죽어라 창만 휘둘렀다. 그 덕분인지 근력과 체력 능력치가 올랐고 진가창법이 구 성에 도달했다.

혼자 수련할 때보다 훨씬 빠른 속도긴 한데, 차라리 이 시간에 다른 절정 무공을 익히는 게 나을 것 같다는 생각이 든다.

하지만 진무경도 생각이 있겠지.

먹을 갈기 조금 귀찮아졌다. 피곤하다.



[훈련 3일 차]

또 진가창법이다. 다른 무공 가르쳐 달라고 했다가 뒤지게 맞았다. 정신이 썩어 빠졌단다.

필사적으로 공격을 피하는 와중에 진가보법이 팔 성으로 올랐다. 젠장, 이거 은근히 효과 있네.



[훈련 4일 차]

훈련을 시작한 이래 하루 두 시간 이상을 자 본 적이 없다.

대부분은 진무경과 수련, 비무, 수련, 비무의 반복이다. 어제부터는 밥 먹는 시간도 아깝다고 벽곡단으로 때우기 시작했다.

시스템이 있지만 슬슬 체력적으로 한계다.



[훈련 5일 차]

팔이 아파서 먹을 조금만 갈았다.

하늘이 노랗다. 잔다.



[훈련 6일 차]

시스템에 메모장 기능이 왜 없는지 이해가 안 되네.

먹 갈다가 열받아서 벼루를 깼다. 진무경한테 맞았다.



[훈련 7일 차]

진가보법이 구 성에 도달했다. 동시에 레벨도 하나 올랐다.

얼마나 지긋지긋하게 익혔는지, 요즘은 평소 걸어 다닐 때도 보법을 밟는다. 소름이 돋았다.



[훈련 8일 차]

오늘따라 손발이 꼬인다. 내가 알던 무공이 아닌 느낌.

천 번, 만 번도 넘게 펼친 무공이 낯설다. 진무경은 그게 자연스러운 현상이라고 했다.

뭔 개소리야?

표정이 불손하다고 맞았다.



[훈련 9일 차]

알 것 같다.



* * *



쾅!

목창 끝에서 응축된 공기가 터져 나갔다. 주르륵 밀려 나간 진무경이 부러진 검을 보며 혀를 찼다.

“아슬아슬하게 성공이군.”

나는 대답하지 않았다. 멍하니 창을 쥔 채 생각했다.

‘이런 거였구나.’

내가 익힌 무공들을 속속들이 안다고 생각했다. 하지만 아니었다. 그건 산 중턱에서 스스로 정상에 올랐다고 착각한 것에 불과했다. 무공이 오를 때마다, 새로운 풍경이 보인다.

‘바로 지금처럼.’

띠링. 띠링. 띠링.



- [진가창법]을 대성했습니다!

- [진가보법]을 대성했습니다!

- 업적, [일류 무공을 대성하다]를 달성했습니다!

- 보상으로 새로운 스킬, [비급 제작]이 생성됩니다!

- 모든 능력치가 크게 상승합니다!

- 레벨 업!

- 레벨 업!



시스템의 파도가 밀려왔다.
```

## Current accepted English baseline

```markdown
# Chapter 72

“You died once today.”

The cold voice continued.

“Your limbs were cut off, you were subjected to Tendon-Splitting and Bone-Twisting, and your throat was cut. The degree and form of the pain may have been different, but you died. Without a doubt.”

Once the relief of being alive faded, anger took its place.

I stood on trembling legs. After swallowing the blood pooled in my mouth, I glared at Jin Mukyung.

*What a fucking lunatic.*

I wanted to drive my fist into that smug face right away, but I held myself back. Not because I was weaker than Jin Mukyung. Because I knew he was right.

“…So? What are you trying to say?”

His answer came immediately, as if he had been waiting for me to ask.

“That you don’t have much life left.”

“What?”

“You’re only half-finished. You’re neither a martial artist nor a wandering martial artist. A half-baked mess. Someone as sloppy as you is just begging to die the moment he enters the Murim.”

Half-finished.

That might have been the most accurate description of my current state. I was a Hunter and a martial artist at the same time.

“Sleeping Dragon of Shanxi? First Rate master? Even a passing dog would laugh. You’re just a brawler. You’re sloppy for a martial artist, and you don’t even fight as pragmatically as a wandering martial artist. Don’t mistake surviving through good luck for skill.”

I barely managed to open my mouth.

“Then what about Jopil? Was that luck too, according to you?”

“Jopil, One Question, One Kill? He was obviously stupid enough to let his guard down in front of an enemy. You just happened to have one last move capable of turning the situation around.”

“……!”

“What? Do you think I guessed too accurately despite not seeing it myself?”

Jin Mukyung clicked his tongue.

“Even a deaf old man knows that the Third Young Master of the Jin Family of Taiyuan is a wastrel. Did Jopil not know? The moment he let his guard down, he was finished too.”

*What is this guy, a stalker?*

I felt like Sun Wukong trapped in the Buddha’s palm. His guess was that accurate.

“Let me make this clear.”

Jin Mukyung fixed me with a somber gaze.

“That luck of yours stops working here.”

“……”

“The Murim is crawling with all kinds of monsters. And they don’t let their guard down like Jopil did. You’re no longer the Jin Family’s wastrel of a Third Young Master. You’re the Sleeping Dragon of Shanxi.”

Every word stabbed straight into my vitals. Everything Jin Mukyung said was true, and it was time for me to face reality.

“Damn it.”

He was right. I was half-finished.

Thanks to the greatest stroke of luck in my life—the System—I had somehow survived this long. But it seemed that luck had taken me exactly this far.

*But… I really am lucky.*

Not only had I discovered the problem early, but an excellent problem-solver was standing right in front of me to help solve it.

“Help me.”

Jin Mukyung.

A fully realized Peak martial artist and a genius of martial arts.

And—

“…Hyung.”

My older brother.

Ding.

> **System**
>
> **Time Limit:** 9 days 20 hours 23 minutes

* * *

Murim people were a proud lot. Even a Third Rate wandering martial artist who wore a rusty sword at his waist and drank cheap baijiu was like that, so the arrogance of scions from prestigious sects reached the heavens.

“Help me, hyung.”

In that sense, this guy had become a decent human being. Three years ago, he would have run to his eldest brother with tears in his eyes… but he had grown. Far more than expected.

*He’s a strange one.*

Neither his personality nor his martial arts could be easily understood. That was both a strength and a weakness. But one thing was certain: nothing worked against a *true master*.

*But his talent is real.*

Over the past three years at Heaven’s Gate Temple, Jin Mukyung had encountered countless prodigies, but Jin Taekyung’s rate of growth was unmatched.

*He has advantages they don’t.*

He could understand martial arts at a glance. He had excellent combat instincts, and he also knew how to listen to other people’s advice.

*Though for now, he’s still a half-finished mess with everything jumbled together.*

As time passed, his weaknesses would be filled in and his excesses would be smoothed out. When that happened, Jin Taekyung’s martial arts would be complete.

Like taiji achieving harmony.

*Taiji? Is that a little too grandiose?*

This was starting to become burdensome.

But he could not stop wondering. How would that bastard grow? How far would he climb?

*I’m going to be busy.*

He had to leave and return to Heaven’s Gate Temple within fifteen days at the latest. Jin Mukyung finally opened his mouth.

“What are you doing? Pick up your spear.”

“Hyung!”

Seeing Jin Taekyung’s face brighten, Jin Mukyung suddenly had a thought.

*When did this bastard start speaking informally to me?*

That was the moment the intensity of his training rose another level.

* * *

Bang.

Jin Wikyung stamped his seal onto the final document with heavily bloodshot eyes.

He had been freed from nearly twenty hours of backbreaking labor, but he was not happy at all. New work would be piled up by tomorrow morning anyway.

*Are these things breeding when I’m not looking?*

The only comfort was that he could finally see the end.

After completing his final review, Jin Wikyung rang a small bell. Before its clear sound had even faded, two sturdily built servants appeared.

“Did you call, Lesser Family Head?”

“Take these away.”

“Yes, sir.”

The servants skillfully stacked the documents onto a cart. Just as they were about to leave, Jin Wikyung spoke.

“Ah. You stay.”

The servant he had pointed to blinked in surprise.

“Me, sir?”

“That’s right. You.”

Once he was alone with the servant, Jin Wikyung began speaking in a solemn voice.

“So, how have you been finding the work lately?”

“Very well, sir. It’s all thanks to your kindness, Lesser Family Head.”

“Nothing causing you any inconvenience?”

“Oh, goodness, of course not.”

The servant, Childeuk, did nothing but nod repeatedly. He was illiterate and could not even get through the Thousand Character Classic, but he still had ears to hear and eyes to see.

After its victory in the recent war, the Jin Family of Taiyuan had risen to become the foremost family in Shanxi. Its Lesser Family Head, Jin Wikyung, had begun to be called the Junzi Sword[^1] for his swift recovery efforts and fair handling of the aftermath.

*Why would such an esteemed person want me?*

His heart pounded with nerves. Had he made some mistake? Or had Jin Wikyung perhaps noticed his talent for martial arts?

The former would be disastrous. The latter would be a chance to turn his life around.

*My bones and muscles are sturdy, at least. I never even had a stomachache as a child.*

He could already see himself wearing a sword at his waist and letting his hero’s headband flutter in the wind.

But when Jin Wikyung saw Childeuk’s eyes growing hazy, he flinched.

*What the hell is wrong with this guy?*

Childeuk’s eyes were filled with desperate longing, as if he were willing to offer his soul to obtain whatever he wanted.

They were not the kind of eyes one man should direct at another man.

*Don’t tell me…?*

Male love, something he had only heard about…

No, that was not it. He could not jump to conclusions. Childeuk was a member of the Jin Family, someone he should trust and cherish.

Jin Wikyung forcibly erased his suspicions and spoke.

“I’ve heard a lot about you.”

“Y-You have, sir?”

“Of course. I’ve been keeping an eye on you for a long time.”

More precisely, not for a long time. Only for the past three days.

Jin Wikyung had been searching for a reliable servant to entrust with a very important task, and Childeuk was the ideal candidate he had personally selected.

“A talented man possessing all four virtues—benevolence, righteousness, propriety, and wisdom. That’s you.”

“How can this be…!”

Childeuk, an exceptional servant possessing all four virtues, shuddered with emotion. He had no idea what those four virtues meant, but he understood the word “talent” perfectly.

*I’m talented?*

He had been praised for his strength and diligence, but this was the first time anyone had called him talented. And to receive such an assessment from the Lesser Family Head himself, a man as lofty as the heavens…

Was this a dream or reality? Childeuk was swept up in overwhelming excitement. He was so excited that even his tongue became tangled.

“I’ve always been watching you too, Lesser Family Head!”

Jin Wikyung’s body flinched.

*What did I just hear?*

“…What do you mean?”

“I’ve dreamed of this moment for a long time. The day I would stand behind you, Lesser Family Head!”

“Wait. That sounds strange. Why would you stand behind me?”

“Ah.”

Childeuk swallowed. Jin Wikyung was telling him not to stand behind him. In other words, he wanted Childeuk to take the lead and win glory.

“Then I’ll stand in front!”

“No! That’s strange too!”

But Childeuk’s charge, like a wild stallion, did not stop.

“I will gladly offer this one body of mine!”

Jin Wikyung’s vision went dark.

“No. Don’t do it! Don’t offer it!”

“Lesser Family Head!”

Huff, huff.

Childeuk breathed heavily, and Jin Wikyung gathered his internal energy.

*I never thought something like this would happen.*

No matter how open-minded he was, this was too much.

Personal sexual preferences were one thing, but he had no desire to be the object of them. Jin Wikyung swallowed hard.

“Then… are you really into men?”[^2]

Childeuk’s eyes flashed. He was thinking about wearing the navy-blue uniform worn by the Jin Family’s martial artists.

“Yes! Just tell me to do it!”

“How dare you set your sights on me? Not a chance, you bastard!”

Smack!

A slap from a Peak master was powerful. Childeuk collapsed like a puppet with its strings cut, and Jin Wikyung stared down at him while breathing heavily before hurriedly ringing the bell.

Ding. Ding.

“Lesser Family Head, did you call—? Gasp. Childeuk!”

Jin Wikyung spoke to the horrified servant.

“Take him out immediately!”

“W-What happened?”

“That bastard tried to… No, never mind.”

It was not something he could say to one of his family’s servants. For the first time in his life, anger and wounded sorrow brought him close to tears.

“I-I’ll take care of it.”

Just as the quick-witted servant hoisted Childeuk onto his back, Jin Wikyung added the most important part.

“And that man.”

“Yes?”

“Remove him from his post.”

“Ah.”

The servant suddenly remembered Childeuk’s assignment.

*Delivering meals.*

The most important duty given to Childeuk, an exceptional servant possessing all four virtues, was to bring every meal to Jin Mukyung and Jin Taekyung.

“Don’t let him go anywhere near my younger brothers. Understood?”

“Yes, sir!”

* * *

### Training Day 1

I decided to start keeping a diary today.

So I would not forget what I learned during this training.

Under Jin Mukyung’s guidance, I did nothing but swing a spear all day. Every day begins and ends with a spar. I got beaten half to death, but it’s bearable.

This is my first time grinding ink, and it’s surprisingly fun.

### Training Day 2

I swung my spear to the point of death again today. Perhaps because of that, my Strength and Stamina stats increased, and the Jin Family’s Spear Technique reached the ninth stage.

It’s progressing much faster than when I trained alone, but I can’t help thinking that I would be better off learning another Peak martial art during this time.

Still, Jin Mukyung must have his reasons.

Grinding ink has become a little annoying. I’m tired.

### Training Day 3

The Jin Family’s Spear Technique again. I asked him to teach me another martial art and got beaten half to death. He said my mind was rotten.

While desperately dodging his attacks, the Jin Family’s Manoeuvre Technique rose to the eighth stage. Damn it. This is surprisingly effective.

### Training Day 4

Since starting training, I haven’t slept more than two hours in a day.

Most of my time is spent repeating training, sparring, training, and sparring with Jin Mukyung. Starting yesterday, I began using fasting pills instead of wasting time eating.

Even with the System, I’m reaching my physical limit.

### Training Day 5

My arms hurt, so I only ground a little ink.

The sky is yellow.

Going to sleep.

### Training Day 6

I don’t understand why the System doesn’t have a notepad function.

I got angry while grinding ink and broke the inkstone. Jin Mukyung beat me.

### Training Day 7

The Jin Family’s Manoeuvre Technique reached the ninth stage. My Level also increased by one.

I’ve practiced it so obsessively that these days, I even use the footwork when I’m simply walking around.

I got goose bumps.

### Training Day 8

My hands and feet keep getting tangled today. It feels like the martial arts I know, but not quite.

The martial arts I’ve performed thousands—even tens of thousands—of times feel unfamiliar. Jin Mukyung said it was a natural phenomenon.

*What the hell is he talking about?*

I got beaten because my expression was disrespectful.

### Training Day 9

I think I get it.

* * *

Bang!

Compressed air erupted from the tip of the wooden spear. Jin Mukyung skidded backward and clicked his tongue as he looked at his broken sword.

“That was a narrow success.”

I did not answer. I stood there blankly, gripping my spear.

*So that’s what it was.*

I thought I knew the martial arts I had learned inside and out. But I had been wrong. I had merely mistaken the middle of the mountain for the summit.

Whenever my martial arts rose to a new level, a new landscape came into view.

*Just like now.*

Ding. Ding. Ding.

> **System**
>
> - You have achieved mastery of **Jin Family’s Spear Technique**!
>
> - You have achieved mastery of **Jin Family’s Manoeuvre Technique**!
>
> - Achievement **Master a First Rate Martial Art** completed!
>
> - As a reward, a new Skill, **Martial Arts Manual Creation**, has been generated!
>
> - All Stats have increased significantly!
>
> - Level Up!
>
> - Level Up!

A wave of System notifications swept over me.

[^1]: *Junzi* is a Confucian ideal referring to a morally upright and cultivated gentleman.

[^2]: In Korean, *nam-saek* can refer both to male homosexuality and to the color navy blue, creating the misunderstanding between Jin Wikyung and Childeuk.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 72`.

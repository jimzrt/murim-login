# Master Edit Task — Chapter 71

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
| 태원진가   | **Jin Family of Taiyuan**        |
| 천무학관   | **Heaven's Gate Temple**         |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 검법     | **sword technique**                              |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 진가검법   | **Jin Sword Technique**                |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |

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

#### Chapter 69 tail (verified mastered)

…
fast.* I quietly got up and stretched. “Whew, I slept well.” When I casually turned my head, I found Jin Mukyung glaring at me. The sight of his face brought yesterday’s memories flooding back. A man without blood or tears. A bastard who deserved to be beaten to death. I addressed him in an innocent voice. “Oh? Hyung-nim. When did you get here?” “…Just now.” Seeing Jin Mukyung smack his lips with disappointment, I decided that switching to formal speech had been a stroke of genius. If he found even one thing to nitpick, he was the type to beat me like a dog. *Fuck… Being weak is a sin. A sin.* I had my pride, too. But in an unarmed fight, I could not beat Jin Mukyung even if I died and came back to life. While that bastard had been learning systematic fist and kicking techniques, I had been watching UFC matches. He was not someone I could overcome through sheer stubbornness. That was why I had chosen Logout as my last resort. Of course, it had failed spectacularly. *You can’t Logout during combat? What kind of bullshit rule is that?* They could have told me beforehand. I had charged in without knowing and nearly gotten logged out of life. I cast a sidelong glance at Jin Mukyung. “Hey.” “Yes?” “Why are you looking at me like that?” “Me?” At his icy tone, I made my eyes as bright and innocent as possible. Now I even had to watch how I looked at him if I wanted one less beating. “You… Hah. Watch yourself.” “Yes, Hyung-nim.” Jin Mukyung looked displeased by my sudden politeness. But he could hardly hit me just for having good manners. “About yesterday…” I quickly bowed my head. “It was my fault. I made so much noise while you were training. I deserved to get hit.” “No, hey.” “Oh, no. Your hand must hurt from hitting me yesterday. Would you like me to blow on it?” “You’re completely insane.” Jin Mukyung looked as though he was debating whether to hit me, but eventually gave up and lowered his fist. “Enough. Follow me.” “…Where?” “The training ground.” I took back what I had just thought. He planned to beat me in the training ground. He could not exactly turn my room into a wasteland again. Jin Mukyung clicked his tongue when he saw my expression stiffen. “It’s not that. Follow me. Training starts today.” “Training?” “Yes. I’m going to tear apart those horrible martial arts of yours and rebuild them from the ground up.” The man who had beaten me senseless every time he saw me was suddenly offering to help me train? And he was even carving out time from his own schedule? *I’d sooner believe the Demon King Asmodeus had repented.* Perhaps he noticed the suspicion in my eyes, because Jin Mukyung let out a deep sigh. “Hyung came by yesterday.” “Ah.” His personality might have been foul, but he had a clear sense of rank and propriety. If Jin Wikyung had personally asked him, the current situation made sense. “There are several empty buildings. Why do you think he sent you to me? Damn it. I should have refused from the beginning.” …I suppose he really did not want to teach me. But I desperately needed his help. If nothing else, there had to be some use for learning even one decent fist-and-kicking technique from him. “Please teach me.” Jin Mukyung shook his head. “Think before you speak. Meeting my standards will be difficult. If you’re going to give up as soon as things become hard, quit now.” If I had given up every time things became difficult, I would never have made it this far. “I want to become stronger.” Perhaps he sensed the sincerity in my voice. After staring at me for a long time, he finally opened his mouth. “Come out to the training ground.” Ding. > **System** > > A Quest has been created. > > **Quest** > > **Trial? Training?** > > Train under Jin Mukyung’s guidance for the designated period. No matter how strong you become, the Quest will fail if Jin Mukyung is not satisfied! > > **Grade:** Peak > > **Restriction:** Jin Taekyung > > **Mission:** Jin Mukyung’s recognition (Incomplete) > > **Reward:** ??? > > **Failure:** ??? > > **Time Remaining:** 9 days 23 hours 51 minutes 10 seconds *Jin Mukyung’s recognition.* It was an abstract mission, but I was confident enough. If I combined the System’s cheat-like advantages with my own effort, I could grow so quickly that Jin Mukyung’s eyes would pop out. *I can do this.* That was when I was steeling my resolve. “Oh, right. You use a spear, don’t you?” “Ah, yes.” “Bring that with you, too.” Jin Mukyung was a swordsman, so I had naturally assumed he would focus on teaching me fist techniques. Confused, I cautiously asked, “Why the spear all of a sudden…?” “Train as if it were real combat. Haven’t you heard that saying?” Jin Mukyung smiled brightly and added: “I even got Hyung’s permission. He said he doesn’t mind if we have to call an undertaker.” I stared blankly at his back as he walked away with light, cheerful steps. At last, I managed to open my mouth. “…Logout.” Beep. > **System** > > Logout is restricted during this Quest. *What the fuck.*

#### Chapter 70 tail (verified mastered)

…
possible and spotted him below. “Hah!” With a short shout, his sword moved. Whoosh! Shh-shh-shhk! The wind split along the blade. Jin Mukyung moved without hesitation, thrusting and slashing through empty space at the speed of a ray of light. About fifteen minutes passed before he lowered his sword and released a long breath. “Hoo.” He wiped away his sweat with his sleeve, then turned toward me. It seemed he had noticed my presence some time ago. “Tell me.” The words came out of nowhere. Caught off guard, I asked, “Tell you what?” “About the martial art I just performed.” “Uh, well, first of all, it was really fast…” “For the record, if you spout pointless bullshit like ‘It was fast’ or ‘It was strong,’ I’ll kill you.” *He’s a mind reader.* I racked my brain for an answer that would keep me alive. What had Jin Mukyung’s martial art been like? As I thought about it carefully, a vague impression began to surface. “Rough?” Jin Mukyung’s eyebrow twitched. *Was that the right answer?* “Did you just speak informally to me?” “…It seemed rough.” “Even a little kid could say that. Be more specific.” The image in my head gradually became clearer. I remembered the blade pouring down upon an imaginary enemy and the movements that accompanied it. Fast and unrestrained. And the aura pressing down from every direction. It was like… “A waterfall?” “…” “Huh?” *What? Was that the right answer?* After a long silence, Jin Mukyung abruptly swung his scabbard. Smack! “Ow! Why did you hit me?” “Just because.” He stared at me with a strange look in his eyes. “How did someone like you ever come out?” Was that an insult or a compliment? I had no idea what he truly meant, but I had to hear the answer to his question if only because I felt wronged. Rubbing my throbbing forehead, I asked: “So, was that the correct answer?” “There are thousands of martial arts manuals in Heaven’s Gate Temple. They were arrangements left behind by the departed Seniors who hoped to cultivate the younger generation of the orthodox Murim.” “And?” “The Falling Flow Sword you just saw is one of them. I found it buried deep in the archives.” Falling flow. In other words, falling water. A waterfall. I had simply blurted out the first thing that came to mind, but it had actually been the right answer. “Oh, ooh.” *Am I really a genius?* If I could recognize martial arts like this after only two months of learning them, I was afraid of how strong I might become in the future. Even I found myself frightening. “Surely you’re not having the embarrassing thought that you’re a genius or something after managing only that much?” “…” *He really is a mind reader.* Still, I seemed to have at least a little talent. Unable to let go of the thought, I cautiously asked, “Can everyone normally do this much?” Jin Mukyung flinched. “O-Of course. Anyone with eyes should be able to guess this much.” “Come on.” “‘Come on’? Want me to pluck out one of your eyes?” “…That might be a bit much.” *Why is this bastard being especially stone-faced today? Did something unpleasant happen?* Even after I backed down, Jin Mukyung could not contain his anger. He kept huffing angrily. “It’s basic. Basic. Everyone can do it.” “I said I get it. Why do you keep getting angry? You’re scaring me.” “Are you rebelling against me? Is it because you’re going through the storm-and-stress stage of adolescence? Do you want to get beaten with the Twelve Gale Fists?” I did not know what the Twelve Gale Fists were, but getting hit by them sounded painful. I shook my head fiercely, but Jin Mukyung’s anger showed no sign of fading. “Do you know martial arts? Huh?” “N-No, sir.” “How long have you been learning martial arts?” The answer slipped out reflexively. “Two months. Two months.” “Right, a bastard who’s only been at it for two months… What? Two months?” Jin Mukyung glared at me with bloodshot eyes. “Not three years, but two months?” This was an emergency. The social instincts I had gained through seven years of working life shone at that moment. I hurriedly opened my mouth, making sure to emphasize one particular part. “Three years! Plus two months!” Jin Mukyung’s fist had been trembling as though he had suffered a stroke, but it steadied again. For some reason, even his voice seemed slightly gentler. “You little bastard. You startled me.” *You startled me even more, you son of a bitch.* *Does he have anger-management issues?* If he asked Jin Wikyung, my lie would be exposed immediately. But at least I would avoid the misfortune of experiencing the Twelve Gale Fists right now. In any case, Jin Mukyung’s anger subsided in the meantime. “I’ll say this only once. Listen carefully.” “I’ll engrave it on my heart.” I bowed deeply, and he declared in a domineering tone, “I teach. You obey.” “…” *Is this a dog-training school or what?* “There will be no objections. Why? Because I’m stronger than you.” It was true, so I had no desire to argue. Money, power, and force. Their forms might differ, but the world always revolved around the strong. I wanted to stand at its center. “What will you do?” My answer had been decided a long time ago.

## Korean source

```text
＃71화



진가창법은 총 일곱 개의 초식으로 이루어져 있다. 그중 마지막 초식, 천관일(天貫軼)이 강철 인형을 후려쳤다.

콰광!

굉음과 함께 가슴이 움푹 꺼진 강철 인형이 벽면에 처박힌다. 창을 거둬들이는 내 귓가로 진무경의 목소리가 파고들었다.

“진가창법이라, 그럭저럭 쓸 만하지.”

“어, 네.”

“진가보법도 뭐, 비슷하고.”

잠깐, 내가 무슨 무공을 익혔는지 말해 준 적이 있던가?

기억을 더듬는 나를 보며 진무경이 피식 웃었다.

“내가 왜 천무학관에 들어갔는지 알아?”

“음. 제가 꼴 보기 싫어서?”

“……아주 틀린 말은 아니군.”

작게 중얼거리며 고개를 끄덕이던 그가 퍼뜩 정신을 차렸다.

“흠흠. 그런 것보다 더 중요한 이유가 있었다.”

“그게 뭔데요?”

“본가에는 더 익힐 무공이 없었거든.”

“예?”

“새로운 게 필요했어. 때마침 천무학관에서 입관 제의가 왔고, 거절할 이유가 없었지.”

“그럼 진가창법도?”

“방금 말했잖아. 더 익힐 무공이 없었다니까.”

“아니, 검수(劍手)잖아요.”

“그래서?”

“네?”

“넌 밥 먹을 때 반찬 안 먹어?”

“그거랑은 다르죠.”

“같아. 나한테는.”

다르다. 나한테는.

‘나도 여러 가지 무기를 익히긴 했지만…….’

진무경과는 완전히 다른 이야기다. 그건 무공도 아니었고 몬스터와의 전투에서 살아남기 위한 발버둥이었다.

창에 익숙해진 후부터는 다른 곳에 눈 돌릴 겨를도 없었다.

한 우물만 파는 것도 벅찼으니까.

“이해를 못 하겠다는 표정인데. 보여 주는 게 빠르겠군.”

스릉.

검을 뽑아 든 진무경이 강철 인형 앞에 섰다.

잠시 손을 까딱거리며 몸을 풀던 그의 입술 사이로 작은 목소리가 흘러나온다.

“이렇게 한번 해 볼까.”

빠르게 교차되는 두 다리. 뒤이어 쏘아진 섬광이 강철 인형의 가슴에 틀어박혔다.

쐐애애액! 쾅!

나는 할 말을 잃었다. 비록 형태는 조금 달랐지만 눈에 익은 동작들이다. 못 알아볼 리가 없었다.

“이건.”

“천관일. 진가창법의 마지막 초식이지. 아, 이 경우에는 진가검법이라고 해야 하나?”

순간 말문이 막혔다. 그리고 잠시 잊고 있었던 사실을 떠올렸다.

진무경은 천재다. 평범한 사람은 맨밥 한 그릇 먹기도 벅차지만 진무경은 팔 첩 반상을 차려도 전부 소화할 수 있다.

‘천재, 천재. 말로만 들었는데.’

간단한 동작 몇 개를 집어넣고 쳐내는 것만으로 진가창법을 검법으로 바꿨다.

무공의 천재. 결코 과장된 소문이 아니었다.

‘이놈…… 진짜다.’

시스템은 빠른 성장을 도와주지, 사용자를 천재로 만들어 주는 게 아니다. 하지만 진무경은 말 그대로 타고났다.

방금 보여 준 한 수도 빙산의 일각에 불과할 거라는 생각이 들어 소름 돋았을 때였다.

“내 말 듣고 있냐?”

차가운 목소리에 그제야 정신이 들었다.

“아, 네.”

“이 형님이 귀찮음을 무릅쓰고 시범까지 보였는데, 감히 한눈을 팔아?”

딱!

“크흑.”

눈앞이 번쩍한다. 내가 고통스러워하는 모습을 흐뭇하게 지켜보던 진무경이 다시 입을 열었다.

“다시 한번 말해 줄 테니까 집중해라. 알았냐?”

“크으. 넵.”

“아무튼, 그러니까. 무공은…….”

“……?”

“어, 무공은. 에이 씨.”

진무경이 붉게 달아오른 얼굴로 소리쳤다.

“너 때문에 까먹었잖아!”

빡!

이런 개새끼…….



* * *



결국 진무경이 택한 방법은 대화였다.

몸으로 하는 대화.

“어차피 말로 해서는 잘 못 알아먹어. 직접 몸으로 겪는 게 빠르지.”

“자, 잠깐만요.”

“실전에 잠깐만이 어디 있어. 너 죽이러 온 놈한테도 그렇게 말할래? 긴장되니까 소피 좀 보고 오겠습니다, 하면 똥도 누고 오세요, 할 것 같아?”

“지금은 비무잖아!”

“어? 또 반말 쓰네. 넌 이제 죽었다.”

목검을 단단히 말아 쥔 진무경이 비호처럼 달려들었다.

나는 더 볼 것도 없이 몸을 날렸다.

쾅!

모골이 송연해지는 굉음을 뒤로하고 거치대에 놓인 수련용 목창 한 자루를 낚아챘다. 음산한 목소리가 따라붙었다.

“지금부터 가르침을 내려 주마.”

쐐애애액!

심상치 않은 파공성. 나는 몸을 돌림과 동시에 창을 휘둘렀다. 그러나 이미 늦었다. 슬쩍 올라간 진무경의 입꼬리가 눈앞에 있었다.

“첫 번째.”

퍽!

밑에서 솟구친 주먹이 아래턱을 강타했다. 내 의지와는 상관없이 두 발이 땅에서 떨어진다.

흔들린 시야 너머로 진무경의 목소리가 이어졌다.

“자신보다 고수를 상대할 때는 신중할 것.”

다음 순간, 진무경의 손바닥이 가슴을 때렸다. 팡! 풍선 터지는 소리와 함께 튕겨 나간 나는 벽면까지 주르륵 밀려났다.

“쿨럭.”

핏물과 함께 내장 조각이 쏟아……지는 일은 없었다. 고개를 들자 천천히 걸어오는 진무경이 보인다.

“자식, 겁먹기는. 설마 형님이 아우를 상대로 공력을 쓸까.”

내가 퉁명스럽게 대꾸했다.

“그럼 목검도 버리시든가.”

“안 돼. 손맛은 이게 더 좋거든.”

강자의 여유다. 그럼에도 불구하고 검을 버릴 만큼 방심은 하지 않는다.

‘이런 상태면 까다롭지.’

다행인 건 진무경은 도발이 잘 먹히는 성격이라는 사실이다.

특히 나한테는 더더욱.

“쫄았냐?”

“뭐?”

진무경의 얼굴에서 미소가 사라졌다. 후환이 두렵지만 그거야 나중 일이다. 지금은 어떻게든 눈앞의 저놈을 이기고 싶다.

“쫄았냐고.”

“그게 무슨 뜻인지는 잘 모르겠는데…… 기분이 확 나빠지네.”

말이 끝나기가 무섭게 진무경의 신형이 쇄도했다. 이전에 비해 확연히 거칠어진 움직임이다. 어깨를 향해 내리 찍히는 목검을 창대로 밀어 냈다.

카가각.

목검에 아교라도 칠해 놨나. 거리를 벌려야 하는데…… 검이 떨어지질 않는다. 뱀처럼 창대를 칭칭 휘감으며 찔러 들어온다.

“이게 무슨!”

“뭐긴, 진가창법. 아니 진가검법이지.”

진가검법이라고? 이게?

“아까 봤던 거랑 완전히 다르잖아!”

“아. 다른 검법도 몇 개 섞었다.”

“이건 사기야!”

“두 번째. 네가 여자 끼고 술 처먹을 때 나는 피땀 흘려 가며 수련했다는 사실을 잊지 말 것.”

동시에 목검이 옆구리를 후려쳤다.

퍽!

아픈 건 둘째치고 깊은 빡침이 밀려온다.

‘뭐? 여자 끼고 술을 퍼마셔?’

남들이 크리스마스에 여자 친구 손잡고 데이트할 때, 나는 게이트에서 몬스터랑 단체 미팅 했다, 이 개새끼야!

퍼버벅.

목검이 연이어 허벅지와 팔뚝을 두들겨 댔지만 아무 느낌 없었다. 분노가 고통을 이겼다.

나는 이를 악물고 창을 흩뿌렸다.

쉬쉬쉬쉭! 캉!

날카로운 공세에 진무경이 서서히 밀리기 시작했다. 전투는 흐름이다. 수많은 실전을 겪으며 벼려진 본능이 속삭인다.

‘지금!’

그의 정수리로 힘껏 창을 내리찍었다.

쾅!

귀가 먹먹해질 정도의 굉음. 하지만 공격이 제대로 들어간 건 아니다.

검을 들어 손쉽게 창을 막아 낸 진무경이 코웃음 쳤다.

“너무 뻔해.”

“그래, 너무 뻔하면 재미없지.”

나는 득의양양한 웃음과 함께 녀석의 복부를 향해 일권을 내질렀다.

‘페이크다. 이 자식아!’

앞선 도발과 공격은 바로 이 순간을 위해서였다.

이렇게 바짝 붙어 있을 때는 무공이고 뭐고 필요 없다. 명치 한 대 맞으면 절정 고수가 아니라 절정 고수 할애비도 답이 없으니까.

‘끝이다.’

그동안의 울분이 실린 주먹이 진무경의 명치에 꽂혔다.

깡!

……깡?

‘뭐야 이거.’

어리둥절한 것도 잠시. 한 박자 늦게 비명이 터져 나왔다.

내 입에서.

“크악! 내 손!”

아프다! 그것도 더럽게!

고통으로 몸부림치는 내 시야에, 수줍게 상의를 걷어 올리는 진무경의 모습이 보인다. 무복 안에 걸친 불룩한 가죽조끼가 모습을 드러냈다.

‘저게 뭐야.’

방탄조끼? 아니다. 하지만 총알도 막아 낼 수 있을 것 같다. 가죽조끼의 주머니마다 철괴를 꽉꽉 채워 넣었으니까.

“세 번째…….”

진무경이 명치 부근에 달린 주머니에서 찌그러진 철괴를 꺼내 들었다. 주먹 자국이 선명하다.

“상대방의 의도를 파악한 후 싸울 것.”

“그딴 걸 왜 입고 있어!”

“네 번째. 평소에도 체력 단련을 게을리하지 않을 것.”

“아오!”

무공? 초식? 이제는 그딴 거 없다. 나는 어설픈 무림인의 모습을 벗어던지고 7년 차 헌터로 돌아왔다.

어차피 손도 다쳤겠다, 진가창법을 제대로 펼치는 건 무리다. 더군다나 내가 익힌 무공들을 전부 꿰고 있는 진무경이 아닌가.

‘진정한 실전 싸움을 보여 주마.’

있는 힘껏 의기양양하게 웃고 있는 진무경의 정강이를 발로 깠다. 사커킥, 혹은 쪼인트라 불리는 회심의 기술이다.

이거 맞고 멀쩡한 놈은 지금까지 한 명도 못 봤지.

까강!

여기 한 명 추가요.

“이런 개새……”

“멍청한 녀석.”

발을 부여잡고 쓰러진 나를 내려다보는 그의 표정은 한심 그 자체라고 말하는 듯했다.

“다섯 번째…… 됐다. 말하는 것도 지치는군.”

바지 밑단에서 납작한 철판을 끄집어낸 진무경이 성큼성큼 다가왔다. 절뚝거리며 일어나려고 했지만 발목을 걷어차이고 다시 주저앉았다.

‘젠장.’

끝났다.

인벤토리를 쓴다면 역전의 기회가 있겠지만 뻔히 의심받을 짓을 대놓고 하고 싶지는 않다. 나는 한숨과 함께 고개를 떨궜다.

“그만합시다.”

“그만하자고?”

딱딱한 목소리에 고개를 들었다. 진무경의 얼굴은 어느새 싸늘하게 식어 있었다.

“겨우 이 정도로?”

아까까지만 해도 히죽거리며 나를 신이 나서 두들겨 패던 모습은 온데간데없다.

그의 무감각한 눈빛에 피부가 따끔거렸고, 목울대가 크게 일렁였다.

꿀꺽.

침 삼키는 소리와 거의 동시에 목검이 내 오른쪽 어깨를 후려쳤다.

퍽 소리와 함께 꺾인 팔이 중심을 잃는다.

“큭. 뭐 하는 짓……!”

진무경은 아랑곳하지 않고 목검을 휘둘렀다. 지금의 그에게 패자의 목소리 따위는 들리지 않는 듯했다.

퍽. 퍽. 퍽.

왼팔. 그리고 양다리까지 때린 후에야 그의 손이 멈췄다.

“방금 넌 사지가 잘린 거다. 너보다 몇 배는 강하고 잔인한 흑도(黑道)의 절정 고수에게.”

“……!”

“조금 더 고약한 놈이라면 다른 방법도 있지.”

타다닥.

진무경의 손이 흐릿해졌다 싶은 순간, 전신이 뻣뻣하게 굳고 혀가 말려들어 갔다. 시스템 알림이 즉각 이상 신호를 알렸다.

삐빅!



- [마혈]을 제압당했습니다. 한 시진 동안 마비 상태에 빠집니다!

- [아혈]을 제압당했습니다. 한 시진 동안 소리를 낼 수 없습니다!



털끝 하나 움직일 수도 없고 목소리조차 내지 못한다.

숨 쉬는 시체. 지금의 나는 어린아이도 죽일 수 있다.

‘진무경. 이 미친 새끼!’

욕설은 머릿속에서만 맴돌 뿐, 입 밖으로 새어 나가지 못했다. 그저 노려보는 것 말곤 할 수 있는 것이 없었다. 분노에 찬 내 눈빛을 진무경은 담담히 받아 냈다.

“분근착골(分筋錯骨)은 잔혹한 수법이다. 길어도 반 시진이면 기혈이 뒤틀리고 전신의 뼈가 으스러지지. 기적적으로 살아남는다고 해도 미치광이가 되거나 평생 불구로 살아야 한다.”

“…….”

“네가 그 고통을 견딜 수 있을까? 아마 일각이면 네가 누군지도 잊을 거다.”

속이 울렁거렸다. 분근착골에 대한 설명 때문이 아니다.

감정이라곤 찾아볼 수 없는 진무경의 눈동자. 그 까만 눈동자가 낯설고 두렵다.

‘설마 진무경이 나를?’

아니다. 그럴 리 없다. 나는 진태경이다. 태원진가의 직계고 진무경의 하나뿐인 동생이다.

그러나 이어지는 그의 행동은 내 예상을 아득히 벗어났다.

“안심해라. 고통 없이 보내 줄 테니.”

나직한 목소리와 함께 차가운 뭔가가 목젖에 닿았다. 앞서 진무경이 빼낸 철판이다. 얇고 날카로운 철판 모서리가 천천히 살을 파고들었다.

‘죽는다고? 이렇게?’

지금껏 죽을 위기를 수십 번도 더 넘겼다. 게이트에서, 무림에서. 어떻게든 살아남겠다고 여태 발버둥 쳤는데…… 지금은 눈 하나 깜빡 못하고 죽게 생겼다.

그것도 피 한 방울 안 섞인 친형이라는 놈한테!

‘이런 개 같은 경우가.’

뻣뻣하게 굳어 천장만 바라보는 내 귓가로 사신(死神)의 목소리가 들려왔다.

“죽어라.”

서걱.

전신에서 힘이 빠져나간다. 뜨거운 선혈이 목을 타고 흘러내리는 게 느껴졌다.

진태경. 향년 27세. 무림에서 잠들다.

나는 스르륵 눈을 감았다.

“…….”

아니, 잠깐만. 뭔가 이상한데.

‘점혈 당했는데 눈을 감았다고?’

그 순간이었다.

띠링.



- [마혈]의 제압이 풀립니다. 마비 상태가 해제되었습니다!

- [아혈]의 제압이 풀립니다. 자유롭게 말할 수 있습니다!



“일어나.”

“…….”

진무경의 목소리에 천천히 눈을 떴다. 또렷한 오감이 내가 살아 있다는 사실을 증명한다.

‘어떻게?’

황급히 목덜미를 더듬었다. 베인 부위가 따끔거렸고 피가 묻어 나왔지만 출혈이라곤 피 몇 방울이 전부였다. 모두 죽음에 대한 공포와 긴장이 일으킨 착각이었던 거다.

“기억해라.”

서늘한 목소리. 불과 수십 초 전 내게 죽음을 선고하던 그 목소리가 이어졌다.

“넌 오늘 한 번 죽었다.”
```

## Current accepted English baseline

```markdown
# Chapter 71

The Jin Family’s Spear Technique consisted of seven forms in total. The final form, Sky-Piercing Strike, smashed into the steel dummy.

Boom!

With a deafening crash, the steel dummy’s chest caved in and it slammed into the wall. As I withdrew my spear, Jin Mukyung’s voice reached my ears.

“The Jin Family’s Spear Technique is passable.”

“Uh, yes.”

“The Jin Family’s Manoeuvre Technique is similar.”

Wait. Had I ever told him what martial arts I had learned?

As I searched my memory, Jin Mukyung gave a quiet laugh.

“Do you know why I entered Heaven’s Gate Temple?”

“Um. Because you couldn’t stand the sight of me?”

“…That’s not entirely wrong.”

He muttered under his breath and nodded, then suddenly came to his senses.

“Ahem. There was a more important reason than that.”

“What was it?”

“There was nothing left for me to learn in our family.”

“What?”

“I needed something new. As luck would have it, Heaven’s Gate Temple offered me admission, and I had no reason to refuse.”

“Then what about the Jin Family’s Spear Technique?”

“I just told you. There was nothing left for me to learn.”

“No, but you’re a swordsman.”

“So?”

“Huh?”

“Don’t you eat side dishes with your rice?”

“That’s different.”

“It’s the same to me.”

*It’s different to me.*

*I’ve learned several different weapons, too, but…*

My situation was completely different from Jin Mukyung’s. That had not been martial arts. It had been a desperate struggle to survive my battles with monsters.

Once I became accustomed to the spear, I had not had the time to look elsewhere.

Focusing on just one thing was already difficult enough.

“You look like you don’t understand. It’ll be faster if I show you.”

Shing.

Jin Mukyung drew his sword and stood before the steel dummy.

After casually warming up with a few movements of his hands, he spoke in a quiet voice.

“Let’s try this.”

His legs crossed rapidly. A flash shot out right after and slammed into the steel dummy’s chest.

Swoooosh! Boom!

I was speechless. The form was slightly different, but the movements were familiar. There was no way I could fail to recognize them.

“This is…”

“Sky-Piercing Strike. The final form of the Jin Family’s Spear Technique. Though in this case, I suppose I should call it the Jin Sword Technique.”

For a moment, I could not speak. Then I remembered something I had temporarily forgotten.

Jin Mukyung was a genius. An ordinary person might struggle just to finish a bowl of plain rice, but Jin Mukyung could digest an eight-dish spread without trouble.

*Genius. Genius. I’d only ever heard the word before.*

With just a few simple changes to the movements, he had transformed the Jin Family’s Spear Technique into a sword technique.

He truly was a genius of martial arts. The rumors had not been exaggerated.

*This bastard… He’s the real deal.*

The System helped its user grow quickly. It did not turn them into a genius. But Jin Mukyung had been born one.

The move he had just shown me had probably been no more than the tip of the iceberg. A chill ran down my spine.

“Are you listening to me?”

I only came to my senses when I heard his cold voice.

“Ah, yes.”

“Your hyung went to the trouble of giving you a demonstration, and you dare look away?”

Flick!

“Gah.”

My vision flashed. Jin Mukyung watched me suffer with satisfaction before speaking again.

“I’ll explain it one more time, so concentrate. Understand?”

“Gnh. Yes, sir.”

“Anyway, martial arts are…”

“…”

“Uh, martial arts are… Ah, damn it.”

Jin Mukyung’s face flushed red as he shouted.

“I forgot because of you!”

Whack!

*You fucking bastard…*

* * *

In the end, Jin Mukyung chose conversation as his method.

A physical conversation.

“You don’t understand very well when things are explained verbally. It’s faster for you to experience them with your body.”

“W-Wait a moment.”

“There’s no such thing as ‘wait a moment’ in real combat. Would you say that to someone who came to kill you? ‘I’m nervous, so I’ll go take a piss first.’ Would you expect him to say, ‘Then go take a shit, too’?”

“We’re sparring right now!”

“Huh? You’re using informal speech again. You’re dead.”

Jin Mukyung gripped his wooden sword tightly and charged at me like a leopard.

I launched myself away without waiting to see what happened.

Boom!

Leaving the bone-rattling crash behind me, I snatched a wooden practice spear from the rack. An ominous voice followed me.

“From now on, I’ll teach you a lesson.”

Swoooosh!

The sound of the air being torn apart was anything but ordinary. I turned and swung my spear at the same time, but I was already too late. The faintly upturned corner of Jin Mukyung’s mouth was right in front of me.

“First.”

Thud!

His fist shot up from below and struck my lower jaw. My feet left the ground against my will.

Through my shaking vision, Jin Mukyung’s voice continued.

“When fighting someone more skilled than yourself, be cautious.”

The next moment, Jin Mukyung’s palm struck my chest. With a bang like a bursting balloon, I flew backward and slid all the way into the wall.

“Cough.”

My organs did not spill out with a mouthful of blood. When I lifted my head, I saw Jin Mukyung slowly walking toward me.

“You’re such a coward. Did you really think your hyung would use internal energy against his younger brother?”

I answered gruffly.

“Then throw away the wooden sword.”

“I can’t. The feel of hitting things is better with this.”

That was the confidence of the strong. Even so, he was not careless enough to discard his weapon.

*This is going to be difficult.*

Fortunately, Jin Mukyung was easy to provoke.

Especially when it came to me.

“Did you chicken out?”

“What?”

The smile disappeared from Jin Mukyung’s face. I was afraid of what he’d do to me later, but that was a problem for later. Right now, I wanted to beat the bastard in front of me somehow.

“I asked if you chickened out.”

“I don’t really know what that means… but it’s really pissing me off.”

The moment I finished speaking, Jin Mukyung rushed toward me. His movements were noticeably rougher than before. I knocked aside the wooden sword descending toward my shoulder with the shaft of my spear.

Krrrk.

*Did they coat this wooden sword with glue?*

I needed to widen the distance, but the sword would not come away. It wrapped around my spear shaft like a snake and stabbed inward.

“What the hell is this?”

“What else would it be? The Jin Family’s Spear Technique. No, the Jin Sword Technique.”

*The Jin Sword Technique? This?*

“It’s completely different from what you showed me earlier!”

“Ah. I mixed in a few other sword techniques.”

“That’s cheating!”

“Second. Never forget that while you were drinking your ass off with women, I was training until I was covered in blood and sweat.”

At the same time, the wooden sword slammed into my side.

Thud!

The pain was secondary to the wave of fury that surged through me.

*What? Drinking with women?*

*While everyone else was holding their girlfriends’ hands and going on dates for Christmas, I was having a group date with monsters in a Gate, you fucking bastard!*

Whack-whack-whack!

The wooden sword pounded my thigh and forearm in succession, but I felt nothing. My anger had overwhelmed the pain.

I gritted my teeth and sent my spear flying in every direction.

Sshh-shh-shhk! Clang!

Under my sharp offensive, Jin Mukyung began to retreat little by little. Combat was all about momentum. My instincts, honed through countless real battles, whispered to me.

*Now!*

I brought my spear down with all my strength toward the crown of his head.

Boom!

The crash was loud enough to leave my ears ringing. But the attack had not landed properly.

Jin Mukyung raised his sword and blocked the spear with ease. He snorted.

“Too obvious.”

“Yeah. If it’s too obvious, it’s no fun.”

With a triumphant grin, I thrust one fist toward his abdomen.

*It’s a feint, you bastard!*

The provocation and the attack before it had all been for this moment.

When you were standing this close, martial arts did not matter. One punch to the solar plexus, and not even a Peak master’s grandfather would stand a chance.

*It’s over.*

My fist, carrying all the resentment I had built up, slammed into Jin Mukyung’s solar plexus.

Clang!

…Clang?

*What the hell was that?*

I was confused for only a moment before a scream burst out.

From my mouth.

“Argh! My hand!”

It hurt! And it hurt like hell!

Through my pain-filled vision, I saw Jin Mukyung shyly lifting his shirt. A bulging leather vest beneath his martial arts uniform came into view.

*What is that?*

A bulletproof vest? No, it was not one. But it looked like it could stop bullets. Every pocket in the leather vest had been packed full of iron ingots.

“Third…”

Jin Mukyung pulled a dented iron ingot from one of the pockets near his solar plexus. My fistprint was clearly visible.

“Fight only after discerning your opponent’s intentions.”

“Why the hell are you wearing that?”

“Fourth. Never neglect physical conditioning, even in everyday life.”

“Damn it!”

Martial arts? Forms? There was no more of that nonsense. I threw off the awkward appearance of a martial artist and returned to being a Hunter with seven years of experience.

My hand was already injured, so properly using the Jin Family’s Spear Technique would be difficult. Besides, Jin Mukyung knew every martial art I had learned.

*I’ll show you what a real fight looks like.*

With all my strength, I kicked Jin Mukyung in the shin as he grinned triumphantly. It was a decisive technique known as a soccer kick, or simply a shin-kick.

I had never seen anyone stay fine after taking one of these.

Clang!

Add one more to the list.

“You fucking—”

“You idiot.”

Jin Mukyung looked down at me as I collapsed, clutching my foot. His expression seemed to say that I was the most pathetic person alive.

“Fifth… Never mind. Talking is exhausting.”

He pulled a flat metal plate from beneath his pant leg and strode toward me. I tried to stand, limping, but he kicked my ankle and made me sit back down.

*Damn it.*

It was over.

If I used Inventory, I might have a chance to turn things around, but I did not want to blatantly do something that would obviously make him suspicious. I lowered my head with a sigh.

“Let’s stop.”

“You want to stop?”

I lifted my head at his hard voice. Jin Mukyung’s face had gone cold.

“After only this much?”

The man who had been grinning and enthusiastically beating me only moments ago was nowhere to be seen.

His emotionless gaze made my skin prickle, and my Adam’s apple bobbed.

Gulp.

Almost simultaneously with the sound of me swallowing, the wooden sword slammed into my right shoulder.

With a thud, my arm bent uselessly and I lost my balance.

“Guh. What the hell are you doing…?”

Jin Mukyung did not care. He swung the wooden sword again. The Jin Mukyung standing before me now seemed unable to hear the voice of the defeated.

Thud. Thud. Thud.

He struck my left arm, then both legs. Only then did his hand stop.

“You just had all four limbs cut off. By a vicious Peak master of the dark path who is several times stronger than you.”

“…”

“If he were even nastier, there would be other methods, too.”

Tap-tap-tap.

The moment Jin Mukyung’s hand blurred, my entire body stiffened and my tongue curled up. The System immediately announced the abnormal condition.

Beep!

> **System**
>
> - The **Paralysis Acupoint** has been subdued. You will be paralyzed for two hours!
>
> - The **Mute Acupoint** has been subdued. You will be unable to make a sound for two hours!

I could not move even a hair, and I could not speak.

A breathing corpse. In my current state, even a child could kill me.

*Jin Mukyung. You insane bastard!*

The curses circled only inside my head and could not escape my lips. All I could do was glare at him. Jin Mukyung calmly met my furious gaze.

“Tendon-Splitting and Bone-Twisting is a cruel technique. Within an hour at most, your qi and blood will twist and all the bones in your body will be crushed. Even if you miraculously survive, you’ll either become a madman or live the rest of your life crippled.”

“…”

“Do you think you could endure that pain? You’d probably forget who you are within fifteen minutes.”

My stomach churned. Not because of his explanation of Tendon-Splitting and Bone-Twisting.

It was Jin Mukyung’s eyes. There was no emotion in them. Those black eyes were unfamiliar and frightening.

*Could Jin Mukyung really be about to kill me?*

No. That was impossible. I was Jin Taekyung. A direct descendant of the Jin Family of Taiyuan, and Jin Mukyung’s only younger brother.

But what he did next went far beyond anything I had expected.

“Don’t worry. I’ll send you off without pain.”

A quiet voice accompanied something cold touching my throat. It was the metal plate Jin Mukyung had pulled out earlier. Its thin, sharp edge slowly pressed into my flesh.

*Die? Like this?*

I had survived dozens of brushes with death. In Gates, and in Murim. I had struggled all this time to survive somehow…

And now I was about to die without even being able to blink.

To a so-called biological older brother who did not share a single drop of blood with me!

*What the fuck kind of situation is this?*

My body rigid, I stared only at the ceiling. Then the voice of the Reaper reached my ears.

“Die.”

Slice.

The strength drained from my entire body. I felt hot blood trickling down my neck.

Jin Taekyung. Aged twenty-seven. Gone to sleep in Murim.

I slowly closed my eyes.

“…”

No, wait. Something was wrong.

*I was hit at an acupoint, but I closed my eyes?*

At that moment—

Ding.

> **System**
>
> - The **Paralysis Acupoint** has been released. The paralysis has ended!
>
> - The **Mute Acupoint** has been released. You can speak freely!

“Get up.”

“…”

At Jin Mukyung’s voice, I slowly opened my eyes. All five of my senses were sharp and clear, proof that I was alive.

*How?*

I hurriedly felt the back of my neck. The cut stung, and blood came away on my fingers, but there were only a few drops of it. Everything had been an illusion brought on by the fear and tension of death.

“Remember.”

His cold voice continued—the same voice that had pronounced my death only seconds earlier.

“You died once today.”
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 71`.

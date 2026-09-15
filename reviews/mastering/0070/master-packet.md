# Master Edit Task — Chapter 70

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
| 이천백    | **Lee Cheonbaek**  |
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 천무학관   | **Heaven's Gate Temple**         |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 영약     | **elixir**                                       |                                                       |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 정파     | **orthodox faction**                             |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 선배     | **Senior**                                   |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 퀘스트              | **Quest**                      |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 태원     | **Taiyuan**            |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 뭐랄까 | comedy | Keep the hesitation beat; do not delete the hedge before the realization. | |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
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

#### Chapter 68 tail (verified mastered)

…
you know they’re from the Jin Family of Taiyuan?” “The gate guards came running and said people from the Jin Family of Taiyuan were outside. And, uh, what was his name? They said some fellow called Wi… Wi-something asked if he could meet you.” Wi-something? The Sect Leader swallowed. “His name wasn’t Wipeng, was it?” “Ah, yes. Wipeng.” The Sect Leader nearly smashed the steward’s head with his wooden pillow. *Ghost Sword Wipeng came here in person?* He was the right hand of the Lesser Family Head, Jin Wikyung, and one of the core masters of the Jin Family of Taiyuan. The thought of a Peak master who had distinguished himself in the recent war paying them a visit nearly scared the soul out of him. “Wake everyone up! Right now!” This was an emergency. Even as the Sect Leader rushed outside, a thousand thoughts raced through his mind. *Is this retaliation?* Song Sword Sect was a small- to medium-sized sect in central Shanxi Province. It had fewer than fifty disciples, most of whom were only Second or Third Rate. They had received various forms of assistance because of their close relationship with the Jin Family of Taiyuan, but when war had actually broken out, they had quietly withdrawn. Perhaps this visit was only to be expected. *Even so, why did Ghost Sword come in person? And at this hour?* The Jin Family of Taiyuan was renowned for its fairness and integrity, so they were unlikely to do such a thing. But if they had come to annihilate Song Sword Sect, there was nothing he could do to stop them. Even he, the strongest martial artist in the sect, might not last three moves against Wipeng. “Sect Leader!” The gate guards, who had been whimpering like puppies desperate to poop, brightened at the sight of their leader. But the Sect Leader could not share their joy. His face stiff, he politely clasped his hands toward the uninvited guests. “I am Huang, the leader of Song Sword Sect.” At the same time, the thirty uninvited guests in bamboo hats parted to either side. Beneath the hazy moonlight, one man stepped forward. “Good to meet you. I’m Wipeng.” He was young, just as the Sect Leader had heard, and ruder than expected. Song Sword Sect might have been an insignificant sect, but how could he treat its Sect Leader like that? Still, the Sect Leader did not dare show his displeasure. The rude young man was Ghost Sword, and behind him stood the name of the Jin Family of Taiyuan. If this was the price of turning a blind eye to an ally’s crisis, then he was getting off cheap. The Sect Leader licked his parched lips. “I have long heard of Ghost Sword’s great reputation. If you had sent word in advance, I would have gone out to welcome you…” “Please do not trouble yourself, Sect Leader. I only intended to deliver a letter from the Lesser Family Head and leave.” “A letter?” Wipeng nodded and handed him a sealed letter. The seal of the Jin Family of Taiyuan was clearly visible in the torchlight held by one of the gate guards. “This is…” “An invitation. The Lesser Family Head requests that you visit our family on New Year’s Day.” The Sect Leader of Song Sword Sect had lived in Murim for many years. He immediately understood the hidden meaning. *What invitation?* This was both a summons and a warning. It was a warning that if they failed to answer the summons, they would be pushed out of the future course of Shanxi Murim. New Year’s Day would be the day the victorious lord accepted new vassals. *The Jin Family of Taiyuan has drawn its sword.* After a brief silence, the Sect Leader spoke. “I have wanted to meet the Lesser Family Head for some time… This will be an excellent opportunity.” “It is an honor that you are willing to visit.” Wipeng politely clasped his hands. The abrupt change in his attitude made the Sect Leader bite his lip. “You must be tired from your journey. Rather than standing out here, why don’t you come inside and rest?” “Thank you for the kind offer, but I think we should be leaving. There is someone we need to catch.” “The man Great Hero Wipeng is pursuing? He must be quite the villain.” “A vicious assassin. He dared to try to harm the Third Young Master.” “T-The Third Young Master? Who would dare attack the Sleeping Dragon of Shanxi?” “Well, we assume the assassin was sent by someone hostile to our family.” “Good heavens.” “But…” Wipeng’s eyes flashed. His sharp gaze swept through the interior of Song Sword Sect. “Wouldn’t you know it, our pursuit led us all the way to Song Sword Sect.” “T-That’s impossible. Surely there has been some misunderstanding?” The Sect Leader’s heart dropped. He was about to start making hurried excuses when Wipeng smiled and waved his hand. “Haha. Of course it must be a mistake. The whole world knows of the deep friendship between the Jin Family of Taiyuan and Song Sword Sect. How could such a thing be true?” “…!” “Thank you for your hospitality. I’ll see you again on New Year’s Day. Hyah!” Wipeng and his subordinates disappeared into the darkness. The Sect Leader of Song Sword Sect remained standing there for a long time.

#### Chapter 69 tail (verified mastered)

…
fast.* I quietly got up and stretched. “Whew, I slept well.” When I casually turned my head, I found Jin Mukyung glaring at me. The sight of his face brought yesterday’s memories flooding back. A man without blood or tears. A bastard who deserved to be beaten to death. I addressed him in an innocent voice. “Oh? Hyung-nim. When did you get here?” “…Just now.” Seeing Jin Mukyung smack his lips with disappointment, I decided that switching to formal speech had been a stroke of genius. If he found even one thing to nitpick, he was the type to beat me like a dog. *Fuck… Being weak is a sin. A sin.* I had my pride, too. But in an unarmed fight, I could not beat Jin Mukyung even if I died and came back to life. While that bastard had been learning systematic fist and kicking techniques, I had been watching UFC matches. He was not someone I could overcome through sheer stubbornness. That was why I had chosen Logout as my last resort. Of course, it had failed spectacularly. *You can’t Logout during combat? What kind of bullshit rule is that?* They could have told me beforehand. I had charged in without knowing and nearly gotten logged out of life. I cast a sidelong glance at Jin Mukyung. “Hey.” “Yes?” “Why are you looking at me like that?” “Me?” At his icy tone, I made my eyes as bright and innocent as possible. Now I even had to watch how I looked at him if I wanted one less beating. “You… Hah. Watch yourself.” “Yes, Hyung-nim.” Jin Mukyung looked displeased by my sudden politeness. But he could hardly hit me just for having good manners. “About yesterday…” I quickly bowed my head. “It was my fault. I made so much noise while you were training. I deserved to get hit.” “No, hey.” “Oh, no. Your hand must hurt from hitting me yesterday. Would you like me to blow on it?” “You’re completely insane.” Jin Mukyung looked as though he was debating whether to hit me, but eventually gave up and lowered his fist. “Enough. Follow me.” “…Where?” “The training ground.” I took back what I had just thought. He planned to beat me in the training ground. He could not exactly turn my room into a wasteland again. Jin Mukyung clicked his tongue when he saw my expression stiffen. “It’s not that. Follow me. Training starts today.” “Training?” “Yes. I’m going to tear apart those horrible martial arts of yours and rebuild them from the ground up.” The man who had beaten me senseless every time he saw me was suddenly offering to help me train? And he was even carving out time from his own schedule? *I’d sooner believe the Demon King Asmodeus had repented.* Perhaps he noticed the suspicion in my eyes, because Jin Mukyung let out a deep sigh. “Hyung came by yesterday.” “Ah.” His personality might have been foul, but he had a clear sense of rank and propriety. If Jin Wikyung had personally asked him, the current situation made sense. “There are several empty buildings. Why do you think he sent you to me? Damn it. I should have refused from the beginning.” …I suppose he really did not want to teach me. But I desperately needed his help. If nothing else, there had to be some use for learning even one decent fist-and-kicking technique from him. “Please teach me.” Jin Mukyung shook his head. “Think before you speak. Meeting my standards will be difficult. If you’re going to give up as soon as things become hard, quit now.” If I had given up every time things became difficult, I would never have made it this far. “I want to become stronger.” Perhaps he sensed the sincerity in my voice. After staring at me for a long time, he finally opened his mouth. “Come out to the training ground.” Ding. > **System** > > A Quest has been created. > > **Quest** > > **Trial? Training?** > > Train under Jin Mukyung’s guidance for the designated period. No matter how strong you become, the Quest will fail if Jin Mukyung is not satisfied! > > **Grade:** Peak > > **Restriction:** Jin Taekyung > > **Mission:** Jin Mukyung’s recognition (Incomplete) > > **Reward:** ??? > > **Failure:** ??? > > **Time Remaining:** 9 days 23 hours 51 minutes 10 seconds *Jin Mukyung’s recognition.* It was an abstract mission, but I was confident enough. If I combined the System’s cheat-like advantages with my own effort, I could grow so quickly that Jin Mukyung’s eyes would pop out. *I can do this.* That was when I was steeling my resolve. “Oh, right. You use a spear, don’t you?” “Ah, yes.” “Bring that with you, too.” Jin Mukyung was a swordsman, so I had naturally assumed he would focus on teaching me fist techniques. Confused, I cautiously asked, “Why the spear all of a sudden…?” “Train as if it were real combat. Haven’t you heard that saying?” Jin Mukyung smiled brightly and added: “I even got Hyung’s permission. He said he doesn’t mind if we have to call an undertaker.” I stared blankly at his back as he walked away with light, cheerful steps. At last, I managed to open my mouth. “…Logout.” Beep. > **System** > > Logout is restricted during this Quest. *What the fuck.*

## Korean source

```text
＃70화



밖은 어스름한 새벽이었다. 겨울철 공기는 얼음장처럼 차가웠고 걸을 때마다 연무장 바닥에 낀 서리가 바스러졌다.

미리 몸을 풀고 있던 진무경이 나를 보며 씩 웃었다.

“그래, 마음의 준비는 끝났고?”

당연히 아니지. 하지만 쓰린 속을 감추고 고개를 끄덕였다.

누가 그랬다. 피할 수 없다면 즐기라고. 강해지는 과정 중 하나라고 생각하니 마음이 한결 편안…….

스르릉.

“그럼 그 대단한 실력 좀 보자.”

이 새끼 한국인인가. 성격이 왜 이렇게 급해?

피할 시간도 없다. 순식간에 코앞까지 짓쳐 든 진무경을 향해 황급히 창대를 휘둘렀다.

캉! 카가가각!

서로 맞댄 무기 너머로 진무경의 입김이 흘러나온다.

“자세는 제법이구나.”

그럴 수밖에. 목숨이 왔다 갔다 하는 게이트에서 7년을 창 하나로 버틴 나다. 권각술과는 쌓인 깜냥부터 다르다.

나는 녀석의 눈을 노려보며 대답했다.

“이번에는 쉽지 않을 겁니다.”

한 글자씩. 또박또박.

“너…….”

범상치 않은 내 기세를 느낀 걸까? 진무경의 눈동자가 파르르 떨렸다.

“눈깔 똑바로 안 떠?”

“아.”



* * *



스르륵. 쿵!

진태경이 쓰러졌다. 그리 놀라운 일은 아니다. 벌써 다섯 번째 기절이니까. 정말 놀랄 만한 일은 따로 있다.

‘날 상대로 이백 합을 버틸 줄이야.’

두 시진 동안 이어진 다섯 번의 비무.

사람이라면 응당 지치기 마련이다. 하지만 진태경은 달랐다. 오뚝이처럼 일어났고 점점 강해졌다. 결국 마지막에는 진무경도 진심으로 상대해야 했다.

‘이 녀석, 정체가 뭐야?’

적수공권일 때는 여든 먹은 노인네처럼 엉거주춤하던 동생. 그러나 창을 잡자 모든 것이 달라졌다.

맞기 싫어 살살 비위를 맞추던 겁쟁이는 어디 가고 노련한 창수(槍手)가 그곳에 있었다.

‘낭인 같았다. 수도 없이 죽음의 위기를 넘긴.’

투박해 보일 정도로 간결한 움직임, 스스로의 직감에 의존하는 변칙적인 공격과 회피. 낭인의 싸움에는 정해진 것이 없다. 진무경의 눈에 비친 진태경이 바로 그랬다.

그렇기에 더욱 큰 의문이 남는 거고.

‘도대체 어떻게?’

걸음마와 동시에 검을 잡는 명문가의 자제들도 일류 언저리만 기웃거리는 놈들이 부지기수다. 한데 저놈은 삼 년 만에 절정의 벽 앞에 섰다.

그것도 기녀들의 분 냄새가 아닌, 노련한 낭인의 냄새를 풀풀 풍기면서. 생각할수록 기가 찼다.

‘이게 가능한 일인가?’

가능하긴 하다. 초절정 고수의 벌모세수, 영약을 이용한 체질 개선. 그다음 피똥 쌀 만큼 창을 휘두르며 실전 경험을 쌓으면 된다. 삼 년간 하루도 빠짐없이!

“……말도 안 되는 소리지.”

허탈한 목소리로 중얼거린 진무경이 머리를 벅벅 긁었다.

그렇다면 이제 남은 답은 하나밖에 없다.

‘천재.’

이 단어 하나면 모든 의문이 명쾌하게 해결된다.

왜? 천재니까. 말 그대로 하늘이 내린 놈. 재능을 타고난 놈이니까. 모든 면에서 천재는 앞서간다. 출발점부터가 다르다.

“드르렁. 푸우.”

“…….”

그런데 하필 이런 놈이 천재라고?

그럴 리가 없다. 그래서는 안 되는 거다! 문득 분노가 치밀어 오른 진무경은 동생의 엉덩이를 걷어찼다.

“푸루루루룹.”

데굴데굴 굴러간 진태경이 몸을 부르르 떨었다.

“워, 월화 누나. 거긴 안 돼요.”

“……!”

“갑자기 이러시면. 앗. 아아!”

뚜둑.

실오라기 같던 마지막 인내심이 끊어졌다.



* * *



삐빅!



- 수면 모드가 강제 종료 됩니다!



이거 강제 종료도 되는 거였구나.

새로운 기능을 알았다는 기쁨도 잠시였다. 수면 모드가 왜 강제 종료 됐겠는가. 누가 깨우니까 종료된 거지.

“신성한, 연무장에서, 뭐? 거긴 안 돼요? 안 돼요?”

뻑! 뻑! 뻑!

새우처럼 웅크린 나는 죽어 가는 목소리로 말했다.

“살려 주세요…….”

“안 돼요!”

퍼버버벅!

정확히 몇 대를 맞았는지 모르겠다. 중간에 두 번 정도 의식이 끊겼기 때문이다.

마지막 힘을 쥐어짜 연무장에 다잉 메시지를 남기다가 쓰러진 것이 마지막 기억이었고, 눈을 떠 보니 이미 밤이었다.

‘뭐 했다고 벌써 밤이냐.’

시간 여행자가 된 기분이다. 진무경을 만난 후로는 아주 그냥 하루가 휙휙 지나간다. 나는 전신을 엄습하는 통증을 느끼며 중얼거렸다.

“진무경, 세긴 세다.”

진무경을 제외한다면 지금까지 내가 상대한 절정 고수는 두 명이다. 대장로, 그리고 조필.

‘그중에서 대장로는 제외.’

대장로의 경우는 천운이 따랐다고 봐야 한다. 그는 태원진가 무인들의 희생과 이천백의 기습이 아니었다면 죽었다 깨어나도 이길 수 없는 고수였다.

‘그럼 조필과 진무경을 비교한다면?’

고민은 그리 길지 않았다.

두 명 모두 겪어 봤기에 선택은 쉬웠다.

‘진무경이 더 강해.’

조필은 분명 괴물 같은 놈이다. 화염신장에서 뿜어져 나오는 무지막지한 열기를 떠올리면 지금도 소름이 돋는다.

하지만 뭐랄까, 절정 고수답게 강하고 화염신장이라는 치명적인 무공을 사용했지만 그게 전부였다.

‘정확히는 무공의 활용 차이라고 해야겠지.’

진무경은 조필과 다르다. 그는 비무 중에도 최소 십여 개의 무공을 사용하며 내 공격을 철저히 차단했다.

무림인에게 무공이란 또 다른 무기다. 진무경은 적재적소에 알맞은 무기를 꺼내 쓸 줄 아는 녀석이다.

‘그에 비하면 나는?’

처음부터 있었던 진가심법은 제외. 무림에서 익힌 무공이라고는 진가창법과 진가보법 두 개가 전부다.

물론 둘 다 의심할 여지가 없는 일류 무공이지만…… 바꿔 말하면 딱 일류 수준에서나 쓸 만한 무공이라는 말도 된다.

무공의 한계. 내가 느낀 것을 진위경이 모를 리 없다.

‘그게 나를 진무경한테 붙여 준 이유고. 윽.’

고통에 절로 눈살이 찌푸려진다. 상반신을 조금 일으켰을 뿐인데, 전신의 뼈마디가 욱신거리고 살갗이 아려 왔다.

수면 모드를 통한 휴식에도 한계가 있었던 모양이다.

‘하긴, 그렇게 얻어맞았으니.’

진무경의 인정을 받아 퀘스트를 완료하려면 오늘 같은, 아니 오늘보다 더한 날들을 보내야 한다.

어쩌면 흠씬 두들겨 맞기만 하고 퀘스트까지 실패할지 모른다.

‘산 넘어 산이군.’

그래서 기쁘다.

F급 헌터였던 내게는 산을 오를 수 있는 자격조차 주어지지 않았으니까. 하지만 모든 것이 달라졌다.

넘어야 할 산이 있고, 그 산에 오를 자격이 주어졌다. 그것도 누구보다 빠르게!

‘이럴 때가 아니지.’

나는 통증도 잊은 채 자리에서 일어났다. 덧없이 흘려보내는 1분 1초가 아쉬웠다.



* * *



진무경은 지하 연무장에 있었다. 최대한 발소리를 죽이며 지하로 통하는 계단을 내려가자 그의 모습이 보였다.

“합!”

짧은 기합성과 함께 검이 움직였다.

쉭! 쉬쉬쉭!

검신을 따라 바람이 갈라진다. 빛살 같은 속도로 허공을 찌르고 베어 내는 진무경의 움직임은 거침없었다.

그렇게 일각 정도가 흘렀을까? 검을 내린 진무경이 긴 날숨을 토해 냈다.

“후우.”

소매로 땀을 훔친 그가 나를 향해 고개를 돌렸다.

이미 아까 전부터 내 존재를 눈치채고 있었던 모양이다.

“말해 봐.”

뜬금없는 한마디.

당황한 나는 엉겁결에 반문했다.

“뭐, 뭘요?

“내가 방금 펼친 무공에 대해서.”

“어, 그게 일단 굉장히 빠…….”

“참고로 빠르다, 강하다. 이딴 헛소리 지껄이면 죽는다.”

귀신이네. 나는 살기 위해 머리를 쥐어짰다.

진무경의 무공이 어땠더라? 곰곰이 생각해 보니 희미하게 떠오르는 느낌이 있었다.

“거칠다?”

진무경의 눈썹이 꿈틀거렸다. 정답인가?

“너 지금 나한테 말 놓은 거냐?”

“……거칠었던 것 같아요.”

“그따위 말은 삼척동자도 할 수 있어. 더 자세히.”

머릿속의 이미지가 점점 또렷해진다. 허상의 적을 향해 쏟아지던 검날과 움직임이 떠올랐다. 빠르고, 거침없는 동작들. 그리고 사방을 짓누르던 기세.

그건 마치…….

“폭포?”

“…….”

“엥?”

뭐야, 정답이야?

한동안 말이 없던 진무경이 돌연 검집을 휘둘렀다.

딱!

“악! 왜 때려요!”

“그냥.”

그가 묘한 눈빛으로 나를 응시했다.

“어쩌다 너 같은 놈이 나왔을까?”

저게 욕일까, 칭찬일까.

속뜻이 뭔지는 모르겠지만 질문에 대한 답은 억울해서라도 들어야겠다. 나는 욱신거리는 이마를 문지르며 물었다.

“그래서, 정답입니까?”

“천무학관에는 수천 권의 무공 비급이 존재한다. 정파 무림의 후학 양성을 생각한 선배 고인들의 안배지.”

“그런데요?”

“방금 네가 본 낙류검(落流劍)도 그중 하나다. 서고 깊숙이 파묻혀 있었던 것을 내가 찾아냈지.”

낙류. 풀이하자면 떨어지는 물의 흐름. 즉, 폭포다.

그냥 생각나는 대로 말한 건데 설마 정답일 줄이야.

“오, 오오.”

설마 나, 진짜 천재인 건가? 무공 입문 두 달 만에 이 정도면 앞으로 얼마나 강해질지 내가 생각해도 나 스스로가 무서워진다.

“설마 겨우 이 정도로 난 천재니, 뭐니 하는 낯부끄러운 생각을 하는 건 아니겠지?”

“…….”

진짜 귀신이네. 그래도 조금은 재능이 있는 것 같은데.

나는 미련을 버리지 못하고 조심스럽게 물었다.

“원래 다들 이 정도는 하는 건가요?”

내 질문에 진무경이 순간 움찔했다.

“그, 그럼. 눈 달린 놈이면 이 정도는 맞춰야지.”

“에이.”

“에이? 눈깔 하나 뽑아 줘?”

“……그건 좀.”

이 자식은 오늘따라 유난히 정색하네. 무슨 기분 나쁜 일이라도 있나. 한발 물러났는데도 진무경은 화를 삭이지 못하고 씨근덕거렸다.

“기본이야, 기본. 누구나 다 하는 거라고.”

“알았다니까요. 왜 자꾸 화를 내고 그러세요? 무섭게.”

“너 지금 반항하냐? 질풍노도의 시기라서 질풍십이권으로 맞고 싶어?”

질풍십이권이 뭔지는 모르겠지만 맞으면 아플 것 같다.

맹렬히 고개를 흔들었지만 진무경의 화는 좀처럼 가라앉지 않았다.

“네가 무공을 알아? 어?”

“모, 모릅니다.”

“너 무공 익힌 지 얼마나 됐어.”

반사적으로 대답이 튀어 나갔다.

“두 달, 두 달이요.”

“그래, 두 달밖에 안 된 놈이…… 뭐? 두 달?”

진무경이 핏줄 선 눈동자로 나를 노려본다.

“삼 년이 아니라 두 달?”

다급한 상황. 7년의 사회생활을 통해 얻은 눈치가 빛을 발하는 순간이다. 나는 재빨리 입을 열었다. 특히 일정 부분을 강조하는 것도 잊지 않고.

“삼 년 하고도! 두 달이요.”

풍 맞은 것처럼 부들거리던 진무경의 주먹이 안정을 되찾았다. 왠지는 몰라도 목소리까지 살짝 온화해진 느낌이다.

“자식이, 깜짝 놀랐네.”

내가 더 놀랐다. 이 새끼야…….

‘분노 조절 장애인가.’

진위경에게 물어보면 금방 들통나겠지만, 적어도 지금 당장 질풍십이권을 체험하는 불상사는 일어나지 않을 것이다.

어쨌건 그사이에 진무경의 분노는 수그러들었다.

“딱 한 번 말한다. 잘 들어.”

“가슴에 새기겠습니다.”

내가 넙죽 고개를 숙이자 그가 고압적인 자세로 선언했다.

“난 가르치고, 넌 복종한다.”

“…….”

애견 훈련소야 뭐야.

“반론은 없다. 왜? 내가 너보다 강하니까.”

맞는 말이라 반박할 생각도 들지 않는다.

돈, 권력, 무력. 형태는 달라도 세상은 강자를 중심으로 돌아가는 법이니까. 나는 그 중심에 서고 싶다.

“어찌하겠느냐?”

아주 오래전부터, 내 대답은 정해져 있었다.
```

## Current accepted English baseline

```markdown
# Chapter 70

Outside, dawn was dim. The winter air was cold as ice, and frost crumbled underfoot with every step across the training ground.

Jin Mukyung, who had already been warming up, grinned at me.

“Well, have you finished preparing yourself mentally?”

Of course not. But I hid my churning stomach and nodded.

Someone once said that if you couldn’t avoid something, you should enjoy it. When I thought of this as just another part of becoming stronger, I felt a little more at ease…

Shing.

“Then let’s see that impressive skill of yours.”

*Is this bastard Korean? Why is he so impatient?*

I had no time to avoid him. Jin Mukyung rushed toward me in an instant, and I hurriedly swung my spear shaft at him.

Clang! Kaga-gang!

Jin Mukyung’s breath drifted between us through the weapons we had crossed.

“Your stance isn’t bad.”

It had to be. I had survived seven years in a Gate where my life had been on the line, using nothing but a spear. The experience I’d built up with the spear was on a completely different level from my fists and kicks.

I glared into his eyes and answered.

“This time, it won’t be easy.”

One word at a time. Clearly and distinctly.

“You…”

Perhaps he sensed that something about my momentum was different. Jin Mukyung’s pupils trembled.

“Can’t you keep your damn eyes open?”

“Oh.”

* * *

Swoosh. Thud!

Jin Taekyung collapsed. It was not particularly surprising. This was already his fifth knockout.

The truly surprising thing was something else.

*I can’t believe he lasted two hundred exchanges against me.*

Five spars over two hours.

Anyone would naturally become exhausted. But Jin Taekyung was different. He kept getting back up like a roly-poly toy, growing stronger each time. By the end, even Jin Mukyung had been forced to face him seriously.

*What the hell is this guy?*

When he fought unarmed, his movements had been awkward enough to resemble those of an eighty-year-old man. But the moment he picked up a spear, everything changed.

The coward who had fawned over Jin Mukyung to avoid getting hit had vanished. In his place stood a seasoned spearman.

*He was like a wandering martial artist. Someone who had survived countless brushes with death.*

His movements were simple to the point of seeming crude. His attacks and evasions were irregular, relying on his own instincts. There was nothing fixed about the way a wandering martial artist fought.

That was exactly what Jin Taekyung looked like to Jin Mukyung.

And that was why the question only grew larger.

*How?*

Even among the heirs of prestigious families who picked up a sword as soon as they learned to walk, countless people only hovered around the threshold of First Rate. Yet this man had stood before the wall of the Peak realm in just three years.

And he did it while giving off not the scent of a courtesan’s powder, but the strong scent of a seasoned wandering martial artist. The more Jin Mukyung thought about it, the more absurd it seemed.

*Was something like this even possible?*

It was possible.

Having a Supreme Peak master cleanse his tendons and marrow. Improving his constitution with elixirs. Then swinging a spear until he shit blood while building real combat experience.

For three years without missing a single day!

“…That’s ridiculous.”

Jin Mukyung muttered hollowly and scratched his head.

If that was the case, only one answer remained.

*A genius.*

That one word resolved every question with perfect clarity.

Why?

Because he was a genius. Someone blessed by heaven, just as the word implied. Someone born with talent.

Geniuses were ahead in every way. They started from a completely different place.

“Zzz… Hoo…”

“…”

But of all people, this guy was a genius?

That was impossible. It couldn’t be true!

A sudden surge of anger rose within Jin Mukyung, and he kicked his younger brother in the rear.

“Prrrblblbl.”

Jin Taekyung rolled away several times before shuddering all over.

“W-Wolhwa noona. Not there.”

“…”

“If you suddenly do this… Ah. Aah!”

Crack.

The last thread of Jin Mukyung’s patience snapped.

* * *

Beep!

> **System**
>
> - Sleep Mode has been forcibly terminated!

*So it can be forcibly terminated?*

My joy at discovering a new function lasted only a moment. Why had Sleep Mode been forcibly terminated?

Because someone had woken me up, obviously.

“In the sacred training hall, you say what? ‘Not there’? ‘Not there’?”

Whack! Whack! Whack!

I curled up like a shrimp and spoke in a dying voice.

“Please, spare me…”

“No!”

Thwack-thwack-thwack!

I had no idea how many times I was hit. My consciousness had cut out twice in the middle of it.

My last memory was of squeezing out my remaining strength to leave a dying message on the training hall floor before collapsing.

When I opened my eyes, it was already night.

*What did I do for it to be night already?*

I felt like a time traveler. Ever since I had met Jin Mukyung, entire days had been flying by.

I muttered as pain swept through my entire body.

“Jin Mukyung is really strong.”

Excluding Jin Mukyung, I had faced two Peak masters so far.

The Head Elder and Jopil.

*The Head Elder doesn’t count.*

In his case, I had to admit that heaven itself had helped me. If not for the sacrifices of the Jin Family of Taiyuan’s martial artists and Lee Cheonbaek’s surprise attack, he was a master I could never have defeated, even if I had died and come back to life.

*Then what if I compare Jopil and Jin Mukyung?*

I did not have to think for long.

I had experienced fighting both of them, so the choice was easy.

*Jin Mukyung is stronger.*

Jopil was unquestionably a monster. Even now, I got goose bumps whenever I remembered the savage heat pouring from his Flame Divine Palm.

But how should I put it? He was strong like a Peak master, and he used the deadly Flame Divine Palm, but that was all.

*More precisely, it was a difference in how they used their martial arts.*

Jin Mukyung was different from Jopil. Even during our spar, he had used at least ten different martial arts to completely shut down my attacks.

To a martial artist, martial arts were another weapon. Jin Mukyung knew how to draw out the right weapon at exactly the right moment.

*Compared to him, what did I have?*

I could exclude the Jin Family’s Cultivation Technique, which I had possessed from the beginning. As for martial arts I had learned in Murim, I had only the Jin Family’s Spear Technique and the Jin Family’s Manoeuvre Technique.

Of course, both were unquestionably First Rate martial arts.

But put another way, they were only useful up to the First Rate level.

The limits of martial arts. Jin Wikyung could not possibly have failed to notice what I had felt.

*That was why he had sent me to Jin Mukyung. Ugh.*

My brow furrowed automatically from the pain. I had only raised my upper body a little, but every joint in my body throbbed, and my skin ached.

It seemed even Sleep Mode had its limits when it came to rest.

*Well, I did get beaten half to death.*

To complete the Quest by earning Jin Mukyung’s recognition, I would have to endure days like today—or even worse ones.

Maybe I would simply get beaten senseless and fail the Quest anyway.

*It really is one mountain after another.*

And that made me happy.

As an F-rank Hunter, I had not even been given the right to climb a mountain. But everything had changed.

There was a mountain I had to climb, and I had been given the right to climb it.

And I could do it faster than anyone else!

*This isn’t the time for this.*

I rose from my place, forgetting the pain. Every minute and second I wasted felt unbearable.

* * *

Jin Mukyung was in the underground training hall.

I descended the stairs leading underground, keeping my footsteps as quiet as possible, and saw him.

“Hah!”

With a short shout, his sword moved.

Whoosh! Shh-shh-shhk!

The wind split along the blade.

Jin Mukyung’s movements were as unrestrained as he thrust and slashed through the empty air at the speed of a ray of light.

About fifteen minutes passed.

Jin Mukyung lowered his sword and let out a long breath.

“Hoo.”

He wiped the sweat from his brow with his sleeve, then turned his head toward me.

It seemed he had noticed my presence some time ago.

“Tell me.”

The words came out of nowhere.

Confused, I reflexively asked:

“Tell you what?”

“About the martial art I just performed.”

“Uh, well, first of all, it was really fast…”

“For the record, if you say some pointless bullshit like ‘It was fast’ or ‘It was strong,’ I’ll kill you.”

*What a ghost.*

I racked my brain for an answer that would keep me alive.

What had Jin Mukyung’s martial art been like?

As I thought about it carefully, a vague impression began to surface.

“Rough?”

Jin Mukyung’s eyebrow twitched.

*Was that the right answer?*

“Did you just speak informally to me?”

“…It seemed rough.”

“Even a little kid could say that. Be more specific.”

The image in my head gradually became clearer.

I remembered the sword blades pouring toward an imaginary enemy and the movements that accompanied them. Fast, unrestrained motions. And an aura that seemed to press down from every direction.

It was like…

“A waterfall?”

“…”

“Huh?”

*What? Was that the right answer?*

After remaining silent for a while, Jin Mukyung suddenly swung his scabbard.

Smack!

“Ow! Why did you hit me?”

“Just because.”

He stared at me with a strange look in his eyes.

“How did someone like you ever come out?”

Was that an insult or a compliment?

I had no idea what he truly meant, but I had to hear the answer to his question if only to soothe my wounded pride. Rubbing my throbbing forehead, I asked:

“So, was that the correct answer?”

“There are thousands of martial arts manuals in Heaven’s Gate Temple. They were arrangements left behind by the departed Seniors who hoped to cultivate the younger generation of the orthodox Murim.”

“And?”

“The Falling Flow Sword you just saw is one of them. I found it buried deep in the archives.”

Falling flow. In other words, water falling down.

A waterfall.

I had only said the first thing that came to mind, but it had actually been the right answer.

“Oh, ooh.”

*Am I really a genius?*

If I could recognize martial arts like this after only two months of learning them, I was afraid of how strong I might become in the future. Even I found myself frightening.

“Surely you’re not having the embarrassing thought that you’re a genius or something after managing only that much?”

“…”

*He really is a ghost.*

Still, I seemed to have at least a little talent.

Unable to let go of the thought, I cautiously asked:

“Can everyone normally do this much?”

Jin Mukyung flinched.

“O-Of course. Anyone with eyes should be able to guess this much.”

“Come on.”

“‘Come on’? Do you want me to pluck out one of your eyes?”

“…That might be a bit much.”

*Why is this bastard being especially stone-faced today? Did something unpleasant happen?*

Even after I backed down, Jin Mukyung could not contain his anger. He snorted irritably.

“It’s basic. Basic. Everyone can do it.”

“I get it. Why do you keep getting angry? You’re scaring me.”

“Are you rebelling against me? Is it because you’re going through the storm-and-stress stage of adolescence? Do you want to get beaten with the Twelve Gale Fists?”

I did not know what the Twelve Gale Fists were, but getting hit by them sounded painful.

I shook my head fiercely, but Jin Mukyung’s anger showed no sign of fading.

“Do you know martial arts? Huh?”

“N-No, sir.”

“How long have you been learning martial arts?”

The answer slipped out reflexively.

“Two months. Two months.”

“Right, a bastard who’s only been at it for two months… What? Two months?”

Jin Mukyung glared at me with bloodshot eyes.

“Not three years, but two months?”

This was an emergency.

The social instincts I had gained through seven years of working life shone at that moment. I hurriedly opened my mouth, making sure to emphasize one particular part.

“Three years! Plus two months!”

Jin Mukyung’s fist had been trembling as though he had suffered a stroke, but it steadied again. For some reason, even his voice seemed slightly gentler.

“You little bastard. You startled me.”

*You startled me even more, you son of a bitch.*

*Does he have anger-management issues?*

If Jin Mukyung asked Jin Wikyung, my lie would be exposed immediately. But at least I would not have the misfortune of experiencing the Twelve Gale Fists right now.

In any case, Jin Mukyung’s anger subsided in the meantime.

“I’ll say this only once. Listen carefully.”

“I’ll engrave it on my heart.”

I bowed deeply, and he declared in a domineering tone:

“I teach, and you obey.”

“…”

*Is this a dog-training school or what?*

“There will be no objections. Why? Because I’m stronger than you.”

It was true, so I had no desire to argue.

Money, power, and force. Their forms might differ, but the world always revolved around the strong.

I wanted to stand at its center.

“What will you do?”

My answer had been decided a long time ago.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 70`.

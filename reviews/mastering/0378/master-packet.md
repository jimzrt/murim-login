# Master Edit Task — Chapter 378

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
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 시스템              | **System**                     |
| 로그아웃             | **Logout**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 팀장      | **Team Leader**       |
| 서천마군 | **Western Heaven Demon Lord** | Major obstacle recently overcome by Taekyung |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 쓰촨성 | **Sichuan Province** | Province containing Chengdu International Airport. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 기장 | passenger_to_captain | Captain | casual-urgent | Taekyung directly asks the captain for permission before cutting open the aircraft door. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 370–374

## Plot

Chapter 370 is intentionally skipped; no accepted English translation or plot details are asserted.

In Chapter 371, Taekyung is celebrated as the Flame Divine Dragon after reaching the Supreme Peak realm. The Qingcheng and Emei Sect Leaders ask him and Jeok Cheongang to investigate a strange Dark Heaven-related formation identified by Samgoe. Taekyung encounters Mungyeong and learns that the physician is secretly the Slaughter Saint.

The group enters a cave hidden by a phantom formation in Chapter 372. It contains supplies, weapons, and a huge inactive transport formation apparently capable of moving people over great distances. Its patterns are not writing, and its origin and purpose remain unclear. Slaughter Saint suggests Dark Heaven succeeded the Demonic Cult, while Taekyung senses something familiar about the formation.

Slaughter Saint decides to resume living as Mungyeong. Back at the Sichuan Tang Clan, Taekyung processes accumulated System messages, reaches Level 120, and discovers that the previously unnamed Inventory item is bound to him and summonable in either world. An investigative party from Henan arrives.

In Chapter 374, Jin Wikyung urges acting Family Head Tang Horyong to relocate the devastated Sichuan Tang Clan to Henan, Shaanxi, or Shanxi, promising orthodox Murim support as a larger war approaches. Horyong does not decide. Wikyung prepares to escort Samgoe to Henan, but Tang Sadok awakens after his long coma, delaying their departure. Taekyung identifies the bound item as the Myriad Poison Ring and expects to return to his original world soon.

## Continuity

- Chapter 370 remains a source-only gap; later references across it must be checked against the current Korean source.
- Taekyung is at the Supreme Peak realm and Level 120. His exact Fame, titles, martial-art stages, and unassigned points after the skipped range are not established here.
- Slaughter Saint is secretly living as Mungyeong and intends to leave Murim after intervening in the crisis.
- The inactive Dark Heaven-associated transport formation remains unexplained. Its origin, destination, mechanism, and connection to Dark Heaven are unresolved.
- Dark Heaven’s agents, larger purpose, and connection to the Demonic Cult remain unresolved.
- The Sichuan Tang Clan, Qingcheng Sect, and Emei Sect were devastated by Dark Heaven. Tang Horyong remains acting Family Head; Tang Sadok, the Poison King, has awakened.
- Jin Wikyung is the Lesser Family Head of the Jin Family of Taiyuan, leader of unified Shanxi Murim, and the assigned escort for Samgoe. He has offered the Tang Clan relocation and orthodox support.
- Orthodox Murim is preparing a new Murim Alliance after Mae Jonghak’s warning of a war greater than the Great Faction War.
- Samgoe remains under guard and is being taken toward Henan; the escort’s outcome and timing are unresolved.
- The Sichuan Tang Clan’s relocation decision and destination are unresolved.
- Taekyung’s return to his original world is imminent; roughly six hours have passed there while about two months passed in Murim.
- The previously unnamed bound Inventory item is the Myriad Poison Ring.
- The outcome of Taekyung’s spar with Jin Mukyung remains unresolved in the accepted earlier anchor.

## Translation Decisions

- Preserve **Flame Divine Dragon**, **Supreme Peak**, **Dark Heaven**, **Slaughter Saint**, **Mungyeong**, **Myriad Poison Ring**, **Sichuan Tang Clan**, **Qingcheng Sect**, **Emei Sect**, **Henan**, **Shaanxi**, and **Shanxi**.
- Preserve uncertainty around the transport formation; do not treat its patterns as writing or assert an origin, destination, or confirmed mechanism beyond its apparent transport function.
- Render **반 시진** and **한 시진** as **half a shichen** and **one shichen**, with a footnote explaining that a shichen is a traditional two-hour period.
- Render **종형** as **older cousin** in the Tang family context.
- Treat Chapters 371–373 as source-only bridge summaries, not complete accepted English translations.

### Prior accepted reading-copy tails

#### Chapter 376 tail (verified mastered)

…
because he hated killing, then it should have been right for him to abandon martial arts as well—the means by which he killed. Yet his martial arts had advanced even further. It was proof that he had been unable to let go of his attachment to them. *Why was that?* The old disciple’s voice broke through his brief reverie. “You can treat hundreds, even thousands, of patients, Master. At the same time, you are capable of saving tens of thousands of lives.” “…” “Please prevent the coming war—not as the Slaughter Saint, but as the Divine Physician. This disciple will care for the patients here.” Mungyeong suddenly lifted his head and looked at the sky. It was clear and blue. Seven days and nights earlier, when the Sichuan Tang Clan had been dyed in blood, the sky had been filled with dark clouds. “The sky is clear.” In his blunt voice, he resumed his halted steps. “I should go check on the patients. Take your time coming down.” As he descended the hill, Dongbong’s voice scattered behind him. “The Hour of the Dog. They said they would depart from Chengdu’s western port then.[^1]” “Pointless. The Murim is not where I belong.” Yet as the old disciple watched his master’s back recede into the distance, a faint smile formed on his lips. “Please… be well.” Whoooosh. A wind blew from somewhere, sweeping between the two men. * * * “What are you looking at so intently?” At Hyuk Mujin’s question, I turned away from the crowd surrounding the port. “Nothing. Just in case.” “Then what are you looking at?” “You little pest. Why are you interrogating me like this? If I say it’s nothing, take it as nothing.” Hyuk Mujin gave me a knowing smile. “I actually know why you’re acting that way, Squad Leader.” “…?” I froze for a moment. How the hell did he know? Even Cheongpung hadn’t heard the conversation between the Divine Physician and me. *Since when was this guy so perceptive?* As I wondered about it, he whispered, “Weren’t you looking at the young lady standing fourth from the right in the front row?” “…” “She is pretty, that’s for sure. She looks like the daughter of a fairly wealthy family. If you give me permission, Squad Leader, I could quietly go over there as your right-hand man and arrange a separate—” “Mujin.” “Yes? Ah, do you prefer meeting women naturally? If so…” “Do you want to sink to the bottom of the Yangtze?” “…!” “Stop talking nonsense and keep lying there. And don’t puke later because you get seasick.” “…Yes, sir.” As Hyuk Mujin quietly shrank in on himself, Gung Gibang snickered. “What a fool. It’s not the fourth woman on the right, but the third on the left. Anyone can see she’s much prettier. Your eyes must be crooked.” “Want me to make them crooked for real?” “…Sorry.” “Let’s live like human beings. Like human beings.” With a sigh, I shook my head and gave the crowd gathered like clouds one last sweeping look. They were both definitely pretty, but the third woman from the left was more my type— *No. That’s not what this is about.* *Damn it. Those idiots wouldn’t shut up about them, and now I can’t stop looking.* Just then, a towering, bronze-skinned man approached me. “Hey there, junior. No, not junior. Young Hero Jin. No, Great Hero.” *What is this, buffering?* I offered a solution to the boatman Mu Song, who was switching forms of address at lightning speed. “Just call me junior.” “Ahem. Th-That would be all right?” “Why wouldn’t it be? You used to do it just fine.” “Even so, you’ve accomplished such a great thing.” He had a point. I had gone from a local rising martial artist known as the Sleeping Dragon of Shanxi to a nationwide celebrity. “And Great Hero Jeok doesn’t seem to like me very much, either…” “It’s fine. He never liked water much in the first place.” Where Mu Song kept glancing, Jeok Cheongang stood with a face twisted in fury. Right beside him, Jin Wikyung was examining some bamboo slips whose contents I could not identify, while Cheongpung was teaching Mimi a new trick. “Mimi, ride the waves!” Sssrik—splaash! …Was that thing a water snake? Mu Song, whose attention had been stolen for a moment by the rare spectacle, finally spoke with a sour expression. “In any case, preparations for departure are complete. When should we set sail?” “What time is it now?” “The Hour of the Dog you mentioned has passed. It would be best to leave before it gets any darker.” “…Hmm.” “Is someone else coming?” I considered Mu Song’s question for a moment, then shook my head. “No. No one.” “Then we can depart.” “Let’s do that.” “Very well.” Mu Song raised one hand high, and the water bandits, who had already finished all their preparations, moved in perfect unison. The people gathered to see us off were waving in our direction when— “Wait! Just a moment!” “Stop! Stop!” The bow of the fast ship rocked as it was about to pull away from the port. Far in the distance, I spotted a boy pushing his way through the crowd and let out a quiet laugh. “Let’s take one more passenger.” [^1]: The Hour of the Dog was a traditional two-hour period, roughly corresponding to 7–9 p.m.

#### Chapter 377 tail (verified mastered)

…
ownership became bound to a new owner. Once given a name, it can be used freely anywhere. *Its ownership became bound because the previous owner died?* I had suspected as much, but it seemed this really was what I thought it was. After turning my inventory upside down, I finally found the new bound item. A flat, deflated sound escaped my lips. “…Eh?” The object resting on my palm was nothing more than a tiny fragment. It had originally been called Black Dragon Armor. *I definitely blew it away along with that bastard, the Western Heaven Demon Lord, in the final slash. Did it automatically enter my inventory because it was a bound item?* The sight of the Black Dragon Armor shattering into pieces was still vivid before my eyes. But what was I supposed to do with a fragment this small? *I guess I’d feel incredibly secure if I tucked it into the front of my underwear.* Ah. Maybe that was why it was classified as armor. I was tugging at the front of my pants and inspecting a suitable position when— “What are you doing th—” “…Ah.” A chilly silence descended in an instant. The boy’s face stiffened at the sight of my loosened waistband and the hand thrust inside it. After making sure no one else was nearby, the Slaughter Saint—no, Mungyeong—spoke. “Why here, of all places?” “Wait a second. I think there’s been a misunderstanding.” Just as I hurriedly began to make excuses, Mungyeong’s gaze turned cold. “I told you when we departed. In front of anyone other than the Fire King and Cheongpung, you are to treat me as Mungyeong.” I answered with an aggrieved expression. “You’re speaking casually to me right now too, you bastard.” “…!” “Oh. Sorry.” A multitude of emotions crossed Mungyeong’s face. He glanced sideways at the approaching river bandits and clicked his tongue. The terrifying Slaughter Saint transformed into the Divine Physician’s Disciple—a cheerful young physician-in-training—in an instant. “What were you doing, sir?” “What business is it of yours?” “…!” *This is surprisingly fun. But I can’t do it a third time.* I quickly held out my hand toward the speechless Mungyeong. “This got into the front of my pants.” That was slightly at odds with the truth, of course, but Mungyeong did not care about such details. More precisely, his eyes were fixed on the fragment of the Black Dragon Armor. “This is…” “Do you happen to know this? No—do you know it?” “Where did you get it?” “From that bastard.” Mungyeong understood that I meant the Western Heaven Demon Lord and nodded. “You obtained a divine weapon. Though I do not know how only a fragment remained.” “He called it Black Dragon Armor.” “Black Dragon Armor?” “Why? Is that different from the name you knew?” “I once read about it in an old secret history. A mysterious suit of armor with no fixed name, said to change its form and properties according to its owner.” “It changes its form and properties? How?” Mungyeong answered with a look that said I was hopeless. Only then did I realize what I needed to do next. *Internal energy.* Internal energy was the very form and nature possessed by its owner. Sssaaaaah. Following the formula of the Blazing Flame Divine Art, which had reached its eighth stage, I poured magma-like qi into the fragment of Black Dragon Armor. The ink-dark energy swirling over its surface vanished, and bluish-white Scorching Yang Qi filled the void. Engraved with patterns that seemed to blaze like flames, it was no longer something that could be called Black Dragon Armor. *Flame Dragon Armor.* The name was simple, but nothing could have suited it better. The instant I smiled in satisfaction, a bright chime rang out. > **System** > > You have given the bound item ??? a new name! > > From now on, you can freely use Flame Dragon Armor anywhere! > > Flame Dragon Armor is resonating with your qi! It requires its owner’s power to repair its damaged sections by itself! Whoooosh. I could feel it—a massive amount of internal energy rushing out of my body and into the Flame Dragon Armor. The fragment absorbed it like a sponge. Pretending to tuck it into my robes, I stored it in my inventory instead. *Automatic repairs? That’s incredible.* I had certainly obtained something useful. Thank goodness the final gift of this journey was the Flame Dragon Armor. As I turned away, Mungyeong stared at me with wide eyes. “Where are you go—going, sir?” “What business is it of yours?” “…!” This was strangely addictive. I waved to Mungyeong, who was probably repeating the character for *patience* to himself. “I’m going to get some sleep. Don’t wake me.” “…?” Yes. It was time to wake from a long sleep. But… *Why do I feel so uneasy? Did I forget something?* Tilting my head, I found a place in the fast ship’s cabin and lay down. I closed my eyes, took a deep breath, and called out the command. *Logout.* A chime rang out. > **System** > > Logging out in 10 seconds. Ten, nine, eight, seven… With the final count, the sound of splashing and someone’s cries faintly pierced my ears from somewhere. Splash! Gasp! Squad Leader, save me—gasp! [^1]: A sikgyeong was the time required to eat a meal, conventionally treated as roughly thirty minutes.

## Korean source

```text
＃378화



띠링.



- [로그아웃]을 성공적으로 완료했습니다.



경쾌한 시스템 알림과 함께, 잠시 떨어져 나갔던 감각들이 돌아오기 시작했다.

등을 타고 전해지는 침대의 푹신함, 전용기 내부의 따뜻한 공기.

그리고 내 양어깨를 잡고 흔드는 누군가의 손길과 외침까지.

“진태경 씨! 일어나십시오! 진태경 씨!”

- 일어나라! 간악한 인간아!

귓가를 파고드는 다급한 두 사람, 아니 한 몬스터와 인간의 목소리에 눈동자를 깜빡였다.

선명해지는 시야 속, 익숙한 얼굴이 눈에 들어왔다.

“어, 최 팀…….”

쫘악!

“일어나라고!”

- 잘했다! 조금 덜 간악한 인간이여!

“…….”

뭐야, 이거.

생각지도 못한 따귀 한 방을 얻어맞은 나는 얼떨떨한 목소리로 대답했다.

“저 일어났는데…….”

“도대체 어떻게 된 사람입니까! 그렇게 깨웠는데 왜 이제야 일어나요!

- 죽어, 그냥 죽어!

“죄, 죄송…….”

박력 보소. 이 정도로 극대노한 최 팀장을 보는 건 처음이다.

무슨 일이 벌어져도 침착을 유지하며 명품이나 자랑하던 최 팀장의 눈에서 번갯불이 튀고 있었다.

‘그런데 왜 저래. 아직 비행기 안인 것 같은데.’

엉겁결에 사과하긴 했는데, 이게 따귀까지 맞을 일인가 싶어 어리둥절하던 그 순간.

“지금 이럴 때가 아닙니다! 어서……!”

“꺄아아악!”

이어지려던 최 팀장의 목소리가 스튜어디스들의 비명에 파묻혔다. 조종사로 짐작되는 남자들의 외침이 뒤를 이었다.

“메이데이! 메이데이! 메이데이!”

“관제탑! 관제타아압!”

“……뭐여, 시벌.”

도대체 지금 무슨 일이 벌어지고 있는 거지?

정신없이 주위를 둘러보는 내게, 최 팀장의 믿을 수 없는 한마디가 날아들었다.

“몬스터의 습격입니다!”

“몬스터? 습격?”

뭔 개소리야. 우리는 중국 중앙위원회에서 보내 준 전용기를 타고 2만 5천 피트 상공을 날아가는 중이었는데.

지금쯤이면 목적지인 쓰촨성 청두 국제공항이 보여도 이상하지 않을…….

“어?”

무심코 고개를 돌려 창밖을 확인한 나는 멍하니 입을 벌렸다.

까마득한 높이로 내려다보이는 거대한 규모의 공항에서, 불길이 솟구치고 크고 작은 점들이 움직였다.

전투다. 인간과 몬스터 간의 죽고 죽이는 전투가 벌어지고 있었다.

심지어 그것으로 끝이 아니었다.

- 캬우우우우!

내가 타고 있는 전용기를 향해 빠르게 가까워지는 몬스터의 거대한 동체.

“저건…….”

틀림없다. 두 눈을 비비고 다시 봐도 와이번(Wyvern)이다.

드레이크와 함께 용족(龍族)으로 분류되는 A급 몬스터.

물론 땅에서 만나도 지랄 같지만, 2만 5천 피트 상공에서는 더더욱 만나기 싫은 놈들이 나타났다.

그것도 무려 십여 마리나!

‘……이게 무슨 개 같은 상황이야.’

지상에서는 청두 국제공항을 둘러싼 치열한 전투가 벌어지고, 2만 5천 피트 상공에서는 와이번 무리가 내가 탄 전용기를 쫓아 오고 있다.

잠깐 정지했던 두뇌가 결론을 도출해 내기까지는 그리 오랜 시간이 필요하지 않았다.

“리치(Rich)!”

나도 모르게 벼락처럼 튀어나온 외침.

현대 시간으로 일주일 전, 유례없는 몬스터 웨이브와 함께 나타난 최상위 언데드 몬스터가 어느새 여기까지 마수를 뻗친 것이 틀림없었다.

“관제탑이 응답하지 않습니다!”

“와이번이, 와이번이……!”

“끼아아아악!”

- 내 이럴 줄 알았다! 우린 이제 다 죽은 목숨이야!

나는 당황한 와중에도 스켈레톤 워로드의 말을 정정해 주었다.

“맞는 말이긴 한데, 넌 이미 죽은 목숨 아니었냐?”

- 닥쳐라, 이 간악한 인간! 모든 게 너 때문이다! 아아, 군단이여! 본 사령관을 용서하라!

몬스터고 인간이고 할 것 없이 패닉에 빠진 비명과 고함이 사방에서 빗발쳤다.

이들 중 그나마 이성을 유지하고 있는 건 한 사람뿐이었다.

“모두 진정하세요! 걱정하시는 일은 일어나지 않을 겁니다!”

역시 최 팀장, 믿음직하다. 분명 이 위기를 타개할 만한 수를 생각해냈음이 틀림없다.

침착한 어조로 혼란을 가라앉힌 최 팀장이 나를 가리켰다.

“여기 계신 진태경 씨가 해결해 줄 겁니다!”

“……?”

“진태경 씨. 어떻게 해야 합니까?”

“아니, 왜 그걸 저한테…….”

“저는 진태경 씨를 믿습니다!”

“…….”

그러니까 왜 날 믿냐고. 지금 같은 상황이면 하느님이나 부처, 알라를 믿는 게 더 도움이 될 것 같은데.

순간 할 말을 잃은 나를 향해 사람들의 시선이 우수수 날아와 꽂힌다.

“그, 그러고 보니 저 헌터님에 관해서 들은 적이 있어. 샤오 양 주석 동지께서도 특별히 요청할 만큼 대단한 실력자라던데.”

“저도 소문은 들었습니다. 어쩌면 새로운 S급 헌터일지도 모른다고. 네임드 몬스터를 둘씩이나 혼자서 잡았대요.”

“오오, 오오오!”

“살았다! 우린 살았어!”

- 너, 간악한 인간! 강한 줄은 알았지만 상상 이상이로군! 기뻐하라, 군단이여. 본 사령관은 살았다!

“……넌 이미 죽었다니까.”

미치겠네. 이미 전부 다 제정신이 아니다. 나는 어처구니없는 눈빛으로 최 팀장을 바라보았다.

“도대체 뭘 믿고 이러는 겁니까?”

최 팀장이 망설임 없이 대답했다.

“말했잖습니까. 진태경 씨를 믿는다고요.”

“그러니까 그 근거 없는 믿음이 어디서…….”

“근거 있는 믿음입니다.”

“예?”

“지금 같은 상황에서 진태경 씨가 보여 주는 태도, 말투, 표정. 그 모든 것들이 제 믿음에 대한 근거입니다.”

“……!”

그제야 비로소 깨달을 수 있었다. 지금의 나는 예기치 못한 상황에 당황했을 뿐, 그 어떤 두려움이나 공포도 느끼지 못하고 있다는 사실을.

정답은 생각보다 가까이에 있다.

‘강하니까.’

나는 강하다. 더욱더 강해졌다. 그 어떤 위험도 피해 갈 수 있을 만큼.

그것이 지상을 파도처럼 휩쓸고 있는 몬스터들도, 바짝 뒤를 쫓아오는 와이번 무리도 두렵지 않은 이유였다.

“그렇다는 거지…….”

내심 작게 중얼거린 나는 입을 열었다.

“기장이 누굽니까?”

내 물음에 저 앞 조종석에서 손 하나가 불쑥 솟아올랐다.

바들바들 떨리는 손. 나머지 한 손으로는 필사적으로 조종간을 붙잡고 달려드는 와이번을 피하려 안간힘을 쓰고 있을 것이다.

“저, 접니다만.”

“잠깐만 문 열어도 돼요?”

“예?”

“비행기 문 좀 열어도 되냐고요.”

얼마나 충격적이었는지, 기장이 미친놈 보는 듯한 시선으로 고개를 내밀었다.

“당연히 안 됩니다! 기압 차단 장치 때문에 열지도 못할뿐더러, 기체가 기압을 감당하지 못하고 파손될 겁니다! 그러면 호흡도 제대로 할 수 없어요!”

최 팀장이 손가락에 끼고 있던 반지를 만지작거리며 끼어들었다.

“기압은 제가 막을 수 있을 것 같습니다. 무슨 생각이신지는 모르지만 한 번 해보시죠.”

“오케이.”

“하지 말라고! 이 빵즈(棒子) 놈들아! 우릴 다 죽일 셈이냐!”

“……뭐, 빵즈?”

감히 자랑스러운 대한의 김치맨 앞에서 한국인을 비하하는 말을 하다니.

무심코 튀어나온 말실수를 알아차린 기장의 얼굴이 하얗게 질렸다.

“아니, 그게 아니고.”

“짱깨 새끼가. 팍 씨.”

“……!”

“야, 기장!”

“예, 예?”

“연다?”

“앗. 아앗!”

기장이 말릴 틈도 없이 나는 문을 열었다. 아니, 잘랐다.

스걱!

강기(劍罡). 현대에서는 오라 블레이드(Aura Blade)라 불리는 그것이 단단한 합금을 가르며 작은 문을 만든다.

무림의 초절정 고수가 그렇듯, 이곳에서는 S급 헌터만이 보여 줄 수 있는 강대한 힘.

최 팀장의 눈동자가 경악으로 부릅떠졌다.

“진태경 씨, 이건……!”

“팀장님!”

콰아아아아!

지금 놀라고 있을 때가 아니다. 엄청난 바람과 기압으로 기체가 휘청이고 기내는 엉망이 되고 있었으니까.

사람들의 비명과 내 외침에 정신을 차린 최 팀장이 반지를 문질렀다.

“빈틈없는 장벽이 주위를 감싼다. 배리어(Barrier)!”

“오.”

주문 영창과 함께 투명한 기의 막이 새로운 입구를 물 샐 틈 없이 가로막았다.

이런 방법이 있었구나. 나는 짧은 감탄과 함께 기내 밖으로 상반신을 내밀었다.

나를 아군으로 인식한 최 팀장의 배리어 마법은 아무런 제지 없이 통과시켜 주었다.

쿠구구구구!

압사라도 시킬 것처럼 상반신을 후려치는 풍압에 나는 씩 웃었다.

‘이거, 장난 아닌데?’

하지만 못 견딜 정도는 아니다.

아니, 내가 못 견디는 것이 오히려 이상했다. 서천마군이 내뿜던 기파에 비교하면, 이 정도는 살랑거리는 봄바람이나 다름없었으니까.

- 캬우우우우!

바로 그 봄바람에, 몬스터의 날카로운 괴성이 섞여 들어온다.

나는 어느새 지척까지 다가온 와이번 무리를 보며 거리를 가늠했다.

‘약 백여 미터. 한 번도 해 본 적은 없지만…… 이 정도 거리라면 충분하겠지.’

인벤토리 오픈. 장착.

스윽.

헌터 마켓에서 할인 구매한 창 한 자루가 손아귀에 잡힌다.

나는 창 던지기 선수처럼 어깨를 한껏 뒤로 젖혔다. 허리부터 손목까지. 필요한 근육과 힘줄이 활시위처럼 팽팽하게 당겨졌다.

- 캬우우!

뭔가 이상함을 눈치챈 선두의 우두머리 와이번이 괴성과 함께 고개를 젖혔다.

새하얀 기류가 놈의 주둥이를 향해 빨려 들어가는 것이 보였다.

‘저건…….’

- 브레스! 브레스다! 피해라, 간악한 인간이여!

스켈레톤 워로드의 외침은 정답이었다.

무수히 많은 몬스터 중에서도 오직 용족에게만 허락된 권능. 바로 브레스(Breath)가 쩍 벌어진 주둥이 안에서 형체를 갖추는 광경이 똑똑히 보였다.

고오오옹.

거대한 바람의 구(球). 금속을 종잇장처럼 갈기갈기 찢어 버릴 수 있는 에어 브레스가 완전한 형체를 갖춘 그때.

“야, 와이번!”

- 캬우?

“넣는다!”

나는 벼락처럼 외치며 한껏 젖혔던 어깨를 전방으로 뿌렸다.

화륵, 쐐애애애액!

창날에 서린 화염의 강기가 공기를 태우고 바람을 가른다.

일직선으로 뻗어 나가는 청백색의 빛줄기에, 와이번의 샛노란 눈동자가 크게 뜨였다.

- 키이이익!

후우우웅!

창날의 끝에서 터져 나가는 압축된 공기. 새하얀 구름. 그리고…….

퍼걱! 퍼버벙!

마치 실이 끊어진 연처럼, 지상을 향해 추락하는 거대한 동체가 있었다.



* * *



- 캬우?

- 키잇?

십여 쌍의 샛노란 눈동자들이 서로를 바라본다.

날 때부터 흉포하기 짝이 없는 와이번이지만, 지금 이 순간만큼은 당혹감에 사로잡혀 어찌할 바를 몰랐다.

- 키키킷?

- 키익…….

뭐야, 대장 죽은 거야?

아마 그런 것 같은데…….

자신들만의 대화를 주고받은 와이번들은 황당했다.

그들의 우두머리는 동족 중에서도 ‘검은 별’이라 불릴 만큼 강한 존재였다.

그리고 지금, 검은 별은 검은 점이 되어 까마득한 지상으로 추락하는 중이었다.

- 키리릭?

- 크르르륵.

심지어 어떻게 죽었는지 제대로 본 놈도 없었다.

다만 저 콩알만 한 인간 하나가 창을 던져서 맞추지 않았나 짐작할 뿐이다.

하지만 말도 안 되는 소리다.

어떻게 인간 따위가 감히 위대한 드래곤의 후예를…….

“야, 거기 그린 와이번!”

- 키릭?

“넣을게!”

퍼걱!

이번에는 똑똑히 볼 수 있었다. 빛줄기에 터져 나가는 동료의 머리통을.

- 키릭!

- 캬우우우!

대장에 이어 또 다른 혈족이 죽다니!

극도로 분노한 와이번들은 저 빌어먹을 인간에 대한 복수를 다짐했다.

- 키잇!

물론 오늘은 아니고. 나중에, 조금 더 나중에 복수하기로.

“야, 거기 블루 와이번!”

퍼걱!

……복수, 할 수 있을까?

십여 쌍의 날개가 필사적으로 퍼덕이기 시작했다.
```

## Current accepted English baseline

```markdown
# Chapter 378

Ding.

> **System**
>
> You have successfully completed **Logout**.

Along with the cheerful system notification, the sensations that had briefly slipped away began returning.

The softness of the bed against my back. The warm air inside the private jet.

And the hands gripping and shaking both my shoulders, along with the shouts that came with them.

“Mr. Jin Taekyung! Wake up! Mr. Jin Taekyung!”

- Wake up, you vile human!

I blinked at the urgent voices drilling into my ears—two voices, no, one monster’s and one human’s.

As my vision cleared, a familiar face came into view.

“Uh, Team Lea—”

Smack!

“Wake up!”

- Well done! You’re a slightly less vile human now!

“…”

What the hell was this?

After taking an unexpected slap across the face, I answered in a dazed voice.

“I’m awake…”

“What is wrong with you? I tried so hard to wake you up, so why are you only getting up now?”

- Just die! Go ahead and die!

“S-Sorry…”

Talk about force. This was the first time I’d ever seen Team Leader Choi this furious.

No matter what happened, Team Leader Choi had always kept his composure while showing off his designer goods. But lightning was practically shooting from his eyes.

*What’s gotten into him? We’re still on the plane, aren’t we?*

I had apologized on instinct, but I was still bewildered. Was this really something worth getting slapped over?

That was when—

“This is no time for this! Hurry and—”

“Aaaah!”

Team Leader Choi’s voice was swallowed by the flight attendants’ screams. The shouts of men who were probably the pilots followed.

“Mayday! Mayday! Mayday!”

“Control tower! Control towerrrr!”

“…What the fuck?”

What on earth was happening?

As I frantically looked around, Team Leader Choi delivered an unbelievable statement.

“We’re under attack by monsters!”

“Monsters? An attack?”

What kind of bullshit was that? We were flying at twenty-five thousand feet in a private jet sent by the Central Committee of China.

By now, it wouldn’t have been strange for our destination, Chengdu International Airport in Sichuan Province, to come into view…

“Huh?”

I unconsciously turned toward the window—and stared with my mouth hanging open.

Far below, a massive airport stretched across the ground. Flames surged into the sky, while large and small dots moved through the chaos.

It was a battle. A deadly battle between humans and monsters.

And that wasn’t all.

- Kyaaaauuu!

The enormous body of a monster was rapidly closing in on the private jet I was riding in.

“That’s…”

There was no mistaking it. Even after rubbing my eyes and looking again, it was still a wyvern.

An A-rank monster classified as part of the dragonkin alongside drakes.

They were a pain in the ass even on the ground, but at twenty-five thousand feet, they were the last things I wanted to encounter.

And there were around a dozen of them!

*…What kind of fucked-up situation is this?*

A fierce battle was raging around Chengdu International Airport below, while a flock of wyverns chased the private jet carrying me through the sky.

It didn’t take long for my briefly frozen brain to reach a conclusion.

“Lich!”

The shout burst from me like a thunderbolt.

There was no doubt about it. The supreme undead monster that had appeared alongside an unprecedented monster wave one week ago in modern-world time had extended its reach this far.

“The control tower isn’t responding!”

“The wyverns! The wyverns are—!”

“Kyaaaah!”

- I knew this would happen! We’re all dead!

Even in the middle of my panic, I corrected the Skeleton Warlord.

“That’s true, but weren’t you already dead?”

- Shut up, you vile human! This is all your fault! Ahhh, my legion! Forgive your commander!

Screams and shouts rained down from every direction as humans and monsters alike fell into a panic.

Only one person among them managed to retain his sanity.

“Everyone, calm down! The thing you’re afraid of won’t happen!”

As expected of Team Leader Choi. He was reliable.

He had obviously thought of a way to overcome this crisis.

After calming the chaos with his composed voice, Team Leader Choi pointed at me.

“Mr. Jin Taekyung here will solve it!”

“…?”

“Mr. Jin Taekyung. What should we do?”

“Why are you asking me?”

“I trust Mr. Jin Taekyung!”

“…”

Why did he trust me?

In a situation like this, believing in God, Buddha, or Allah would probably be more helpful.

I was momentarily speechless as people’s gazes came flying toward me from all sides.

“Come to think of it, I’ve heard about that Hunter. They say he’s so formidable that even Comrade Chairman Xiao Yang made a special request for him.”

“I’ve heard the rumors too. They say he might be a new S-rank Hunter. Apparently, he defeated two named monsters all by himself.”

“Ooh! Ooooooh!”

“We’re saved! We’re going to live!”

- You vile human! I knew you were strong, but you’re beyond my wildest imagination! Rejoice, my legion. Your commander has survived!

“…You’re already dead.”

This was driving me insane. None of them were in their right minds anymore.

I stared at Team Leader Choi in disbelief.

“What exactly are you basing this on?”

He answered without hesitation.

“I told you. I trust you.”

“That’s what I’m asking. Where does that baseless trust come from—”

“It isn’t baseless.”

“What?”

“Your attitude, tone of voice, and expression in a situation like this. All of them are grounds for my trust.”

“…”

Only then did I finally realize it.

I was flustered by the unexpected situation, but I felt no fear or terror whatsoever.

The answer was closer than I had thought.

*Because I’m strong.*

I was strong. Stronger than ever. Strong enough to avoid any danger.

That was why neither the monsters sweeping across the ground like a wave nor the flock of wyverns right behind us frightened me.

“So that’s it…”

I muttered quietly to myself before opening my mouth.

“Who’s the captain?”

A hand shot up from the cockpit ahead.

It was trembling violently. With his other hand, the captain was probably gripping the controls for dear life, desperately trying to evade the wyverns lunging at us.

“I-I am.”

“Can I open the door for a second?”

“What?”

“I said, can I open the plane door?”

The captain must have been so shocked that he poked his head out and stared at me as though I were insane.

“Of course not! Not only is it impossible to open because of the pressure-sealing system, the aircraft will be damaged because it can’t withstand the pressure difference! You won’t even be able to breathe properly!”

Team Leader Choi, fiddling with the ring on his finger, cut in.

“I think I can block the pressure. I don’t know what you have in mind, but go ahead and try.”

“Okay.”

“Don’t! You *bangzi* bastards![^1] Are you trying to kill us all?”

“…What did you just call us?”

The nerve of him, insulting Koreans right in front of a proud Korean kimchi man like me!

Realizing the slip of the tongue that had escaped him, the captain’s face turned pale.

“No, that’s not what I meant.”

“You fucking Chink bastard. Damn it.”

“…”

“Hey, Captain!”

“Y-Yes?”

“I’m opening it.”

“Ah! Ah!”

Before the captain had time to stop me, I opened the door.

No—I cut it open.

Shhk!

Sword qi—the force called an Aura Blade in the modern world—sliced through the sturdy alloy and created a small door.

Just as a Supreme Peak master of the Murim could do, it was a tremendous power that only an S-rank Hunter could display here.

Team Leader Choi’s eyes widened in shock.

“Mr. Jin Taekyung, this is—”

“Team Leader!”

Whoooosh!

This was no time to be surprised. The tremendous wind and pressure were making the aircraft lurch, turning the cabin into a complete mess.

Team Leader Choi came to his senses at the screams and my shout, then rubbed his ring.

“An impenetrable barrier surrounds us. Barrier!”

“Oh.”

Along with the incantation, a transparent membrane of energy sealed off the new opening without leaving so much as a gap.

So there was a way to do this.

With a brief exclamation of admiration, I stuck my upper body out of the cabin.

Because Team Leader Choi’s barrier recognized me as an ally, it let me pass through without resistance.

Rumble, rumble!

The wind pressure slammed into my upper body as though trying to crush me. I grinned.

*This is no joke.*

But it wasn’t unbearable.

Actually, it would have been strange if I couldn’t withstand it. Compared to the waves of qi the Western Heaven Demon Lord had emitted, this was no more than a gentle spring breeze.

- Kyaaaauuu!

The monster’s sharp cry mixed into that spring breeze.

The flock of wyverns had already drawn close enough for me to judge the distance.

*About a hundred meters. I’ve never tried this before, but… at this distance, it should be enough.*

*Open inventory. Equip.*

Ssswish.

A spear I had bought at a discount from the Hunter Market appeared in my hand.

Like a javelin thrower, I drew my shoulder far back. From my waist to my wrist, the necessary muscles and tendons pulled taut like bowstrings.

- Kyaau!

The leading wyvern, their chief, noticed that something was wrong and threw back its head with a shriek.

I could see a pure-white current of air being sucked toward its snout.

*That’s…*

- Breath! It’s using Breath! Dodge it, you vile human!

The Skeleton Warlord was right.

Among the countless monsters, Breath was a power granted only to the dragonkin. Inside the wyvern’s wide-open maw, I could clearly see it taking shape.

Whooooom.

A massive sphere of wind. An air breath capable of shredding metal like paper had formed completely.

“Hey, wyvern!”

- Kya?

“I’m putting it in!”

I shouted like a thunderbolt and whipped my drawn-back shoulder forward.

Fwoom—whooosh!

Fiery concentrated qi sheathed the spearhead, burning the air and cleaving the wind.

The wyvern’s bright yellow eyes widened at the blue-white streak of light shooting straight toward it.

- Kiiiiiik!

Whoooom!

Compressed air burst from the tip of the spear. A cloud of white.

And then—

Thwack! Boom-boom!

A massive body plunged toward the ground like a kite with its string cut.

* * *

- Kyaau?

- Kiiit?

Around a dozen pairs of bright yellow eyes stared at one another.

Wyverns were ferocious creatures from the moment they were born, but at this moment, they were utterly bewildered and had no idea what to do.

- Kikikit?

- Kiiik…

*What? Is the boss dead?*

*Looks that way…*

After exchanging words in their own language, the wyverns were dumbfounded.

Their leader was an exceptionally powerful member of their species—so powerful that he was known as the “Black Star.”

And now, the Black Star had become a black speck falling toward the impossibly distant ground.

- Kiririk?

- Grrrrr.

None of them had even properly seen how he died.

They could only guess that the tiny human had thrown a spear and hit him.

But that was impossible.

How could a mere human dare lay a hand on a descendant of the great dragons…

“Hey, green wyvern over there!”

- Kiiik?

“I’m putting it in!”

Thwack!

This time, they saw it clearly: their companion’s head bursting apart in the beam of light.

- Kiiik!

- Kyaaaauuu!

*Another of our bloodline has died after the boss!*

Furious beyond measure, the wyverns vowed revenge against that damned human.

- Kiiit!

Of course, not today.

They would get their revenge later. A little later.

“Hey, blue wyvern over there!”

Thwack!

*…Will they ever get their revenge?*

Around a dozen pairs of wings began flapping desperately.

[^1]: *Bangzi* (棒子) is a derogatory Chinese slur for Koreans.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 378`.

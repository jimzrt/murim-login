# Master Edit Task — Chapter 92

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

| 진태경    | **Jin Taekyung**   |
| 임춘수    | **Im Chunsoo**    |
| 임창수    | **Im Changsoo**   |
| 홍우진    | **Hong Woojin**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 정파     | **orthodox faction**                             |                                                       |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 평화 | **Peace Guild** | Guild name. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 85–89

## Plot

In the Boss Zone of The Minotaur’s Labyrinth, Im Changsoo plans to exploit Taekyung’s apparent interest in Song Song and use the Level 70 Minotaur Warrior to humiliate him. Taekyung instead kills the boss with a single spear technique, completes the B-rank Gate Clear Quest, and receives a Level Up and its undisclosed reward. Song Song declines his attempts to invite her to dinner.

After the raid, Changsoo transfers the wagered four billion won to Taekyung. His father, Im Chunsoo—the A-rank Guild Master of Sangdong Guild, known as Frozen—learns that Changsoo transferred eight billion won in total, fires him, and begins beating him with an ice club.

Taekyung visits his sick sister Hayeon and discovers that their mother, Kim Jeonghee, has been secretly working in a restaurant. When the restaurant owner insults Jeonghee and attacks Taekyung, he reveals his C-rank Hunter status and has Changsoo confirm both his identity and payment. Jeonghee quits and leaves with him.

At home, Taekyung uses Circulate Qi for Healing on Hayeon and Jeonghee, curing Hayeon’s fever and headache and greatly improving his mother’s condition. He gives each of them a Lesser Potion from his reality Inventory. After learning that Taekyung earned four billion won, Hayeon asks whether she can drop out of school.

## Continuity

- Taekyung killed the Level 70 Minotaur Warrior in one blow, completed the B-rank Gate Clear Quest, leveled up, and received its reward in his reality Inventory.
- Im Changsoo paid Taekyung the promised four billion won.
- Im Chunsoo is Sangdong Guild’s founder and A-rank Guild Master, known as Frozen and for his exceptional ice magic. He fired Changsoo and violently confronted him after discovering Changsoo’s eight-billion-won transfer.
- Kim Jeonghee quit her restaurant job after the owner insulted and attacked Taekyung.
- Kim Minsu is the owner’s son, a D-rank Hunter in Sangdong Guild, but Changsoo does not know him personally.
- Taekyung can safely use the Jin Family’s Cultivation Technique to perform Circulate Qi for Healing on others.
- Hayeon and Jeonghee recovered substantially after receiving the treatment; Taekyung also gave each a Lesser Potion.
- Taekyung’s reality and Murim Inventories remain separate.
- Hayeon has asked about dropping out of school, but no decision has been made.
- Retaliation by Im Chunsoo or Sangdong Guild, Jeonghee’s next circumstances, and Hayeon’s schooling remain unresolved.

## Translation Decisions

- Render 일섬 as **One Annihilation** and 미노타우로스 대전사 as **Minotaur Warrior**.
- Render 관심법 as **mind-reading technique** and preserve the **barbarian against barbarian** wording for 이이제이.
- Retain **Frozen**, **C-rank**, **D-rank**, **Circulate Qi for Healing**, **Lesser Potion**, and **Third Rate**.
- Retain **ajumma** and **goshiwon** with their established explanatory footnotes.
- Use **Minsu** as Kim Minsu’s short form.
- Preserve the established family addresses **Mom** and **Son**.

### Prior accepted reading-copy tails

#### Chapter 90 tail (verified mastered)

…
had reached the tens of millions. The property damage was too vast to calculate accurately. > The Great Cataclysm: The Most Horrific Ten Years in Human History. By the time the documentary reached its midpoint alongside the caption, the bathroom door flew open. “Whew. Now I feel alive.” The real estate agent plopped down after wiping his sweat-slick forehead. “Sorry to keep you waiting. You said you were looking to buy, right?” “Yes.” “Did you stop by anywhere else before coming here? There must’ve been plenty of real estate offices along the way.” “No, this is my first stop.” “Really?” Judging by the way his eyes rolled around, he seemed to be deciding whether or not to take me for a sucker. I pretended not to notice and held out the note I had prepared. It had the address written on it. “I’d prefer to see a property around this address, if possible.” “This address… That’s in a safe zone.” “Yes.” “You really said you wanted to buy, right? Did I hear you wrong because I had to take a dump so badly?” When I nodded, the man’s eyes traveled subtly up and down. Jeans and a white T-shirt. Twenty-thousand-won sneakers bought at a market or online. No matter how you looked at me, I wasn’t dressed like a man with money. “What do you do for a living?” “I run Gates.” “Oh, a Hunter? I thought so. You’ve done well for yourself at such a young age.” A bright smile blossomed across the man’s face. Hunters were one of the most prominent high-income professions. It was hardly unusual for young, successful Hunters to buy expensive houses and cars. He asked in a much friendlier tone, “Have you checked the market prices?” “I searched online on the way here.” “Then you’re in luck. There actually happen to be a few listings available. Let’s see…” Perhaps he was excited by the prospect of a sale, because the man began making calls to one person after another. He spent about five minutes hanging up and dialing again before putting away his smartphone and turning to me. “I found a listing that’s perfect for you, Boss. If you’re not busy, how about we go see it now?” “Sure. Why not?” I was on vacation, so I had no reason to refuse. As I rose, the man beamed. * * * Vroom. I sat in the passenger seat of the sedan and watched the scenery pass by. Detached houses stood in rows, shops dotted the streets here and there, and playgrounds and schools appeared along the way. “It’s changed a lot…” The agent glanced sideways at me. “Did you used to live around here?” “When I was a kid.” I had been in my third year of middle school—sixteen years old—so it had been exactly eleven years since then. I had been born and raised here, so in a way, this was my hometown. “This area was redeveloped about ten years ago, so it must look pretty different. It used to be an old apartment complex, but when they heard an Association branch was going to be built within thirty minutes of here, they tore the whole thing down.” “I see.” I already knew. Housing prices had skyrocketed as soon as news of the redevelopment broke. The jeonse deposit had risen by hundreds of millions of won, far more than we could afford, so we decided to move. *It wasn’t long after Dad died.* On the night before we moved, I saw Mom crying silently. It was several years later that I learned the place had been my parents’ newlywed home. “We’re here.” The agent’s voice pulled me from my thoughts. I opened the door and stepped out to find a detached house with a yard. “This is the address you gave me, Boss. The owner happens to be out, so let’s have a quick look and be on our way.” “Ah, just a moment.” Maybe it was nostalgia. The old apartment complex had already been demolished, but the area still felt strangely familiar. *Still… I’m glad it hasn’t changed completely.* Some traces of the old scenery remained even after the redevelopment. The real estate agent smacked his lips as he watched me look around, lost in nostalgia. “You must be happy to be back after all this time. Why don’t you take a lap around the neighborhood while you’re at it?” “Is that okay?” “You’re going to sign the contract, aren’t you?” “No. I mean, yes.” I had to buy this house, no matter what. The agent chuckled and took out a cigarette. “Then I should accommodate you. It won’t take long to walk around the neighborhood. I’ll stay here and smoke while I wait, so don’t worry about me.” After offering him a brief word of thanks, I began walking slowly. *Is this the right way?* I passed through an alley and spotted the supermarket I’d often visited as a child. “When Oppa was a kid, this place was his hangout. Back when he smoked like crazy in middle school, the old lady here was so old that…” A gleaming foreign car was parked in front of the supermarket. A man and woman who had been talking together stopped when they saw me. No—the man was the one who stopped. He tilted his head, approached me, and asked, “Do you know me?”

#### Chapter 91 tail (verified mastered)

…
who cut off contact. Were you really such close friends that you’d still defend him?” Park Jihoon smiled gently. “No. Not at all.” * * * “What do you think?” The real estate agent’s voice was thick with phlegm. He had chain-smoked for an hour while waiting for me, and his complexion looked awful. “It’s nice.” I wasn’t just being polite. The two-story detached house with a broad lawn was better than any house I had seen so far. *Four bedrooms, two bathrooms, and a spacious living room.* It looked like something straight out of a fairy tale. I toured the house while half-listening to the real estate agent’s detailed explanations, then stepped out through the front gate. “Listings like this are hard to find. The current owner has several buildings, but he’s putting this one up as a quick sale because he’s planning to put up another building in Incheon.” “So what’s the market price?” “Exactly what you saw online. 3.38 billion won.” It was still an amount that made me want to swear, but the house was worth every bit of it. For my family’s safety, and because this place held special meaning for us. “Please contact me.” “Then…?” “I’ll buy it.” “Oh, you’ve made an excellent decision, Boss!” I firmly clasped the hand he offered me. “Since we’re on the subject, would it be all right if I took another look around the neighborhood?” “…” “I’m joking.” Look at how hard he was squeezing my hand over one little joke. * * * “Have a safe trip home.” “Thanks. Take care.” I left the real estate office after putting down a ten-percent deposit. The owner and I had agreed to set a date soon and proceed with the formal purchase. Since he needed cash quickly, everything had been settled without delay. *I’ll have to put off moving for a while.* The new house was about an hour from where my family currently lived. Even after buying it, moving in right away would be difficult. More importantly, Hayeon had her college entrance exam this year. I would surprise them with the news immediately afterward. *I’ll need to remodel the place, too.* I intended to make it as similar as possible to our old home. It had happened a very long time ago, but perhaps because we had lived there for sixteen years, I remembered the layout perfectly. *I’ll sign the formal contract and find an interior contractor… What else is there?* I knew how to thrust a spear inside a Gate, but I was a complete novice when it came to any of this. I had no idea where to begin. I was turning into a dark alley while thinking about this and that when— *Hm?* The back of my neck prickled. My fine hairs stood on end, and the air seemed to shift. I sensed someone secretly watching me from behind. *Open Inventory. Summon.* I spun around like lightning, a dagger already in my grip. But… Meow. “What? A cat?” Meow. A mottled cat jumped down from the wall. It glanced at me, then slowly wandered away. *Did I overreact?* My senses had become more acute as they improved. Normally, I would have grown accustomed to them gradually as I developed, but I was progressing too quickly for any adjustment period to matter. *No. Something felt strange this time.* I belatedly raised my Qi Sense, but there was nothing in the deserted alley. Beep. > **System** > > There are no targets for **Qi Sense** to detect. If the System said there was nothing, then there was nothing. I must have been especially tired lately. “Ah, now I suddenly have a craving for samgyetang.[^1]” Since I had thought of it, maybe I should go out to eat with the whole family. The thought of tender chicken and piping-hot broth put a spring in my step. [^1]: Samgyetang is a Korean ginseng chicken soup traditionally served piping hot. * * * In a dark, cramped room, a young man deep in meditation snapped his eyes open. “Gasp!” His hair stuck out in every direction, soaked with sweat, and his breathing was ragged. He hurriedly gulped bottled water, then let out a relieved sigh. “Fuck, that scared me.” Everything had gone smoothly. In fact, it had been downright boring. The investigation target happened to be on vacation, and his movements were predictable. Home, convenience store, home. Today, he had traveled as far as an hour away, but tracking him had still been no trouble. But then… “What the fuck was that? Why did that bastard suddenly turn around and start pulling that shit?” The moment he saw that sharp gaze, his heart had dropped. If he had not hurriedly severed the Link with the cat, he might really have been discovered. “He didn’t know, did he?” The target was only a C-rank Hunter. Compared to the people he had investigated before, the man was far beneath them. *There’s no way. Who do you think I am?* Hong Woojin, a B-rank mage and information broker, shook his head. He was a master of tracking and surveillance magic. He couldn’t cast flashy offensive spells, but in this particular field, he prided himself on being the best. “That’s right. There’s no way. It was just a coincidence. A coincidence.” Hong Woojin muttered the words like a mantra. Anxiety lingered in his voice.

## Korean source

```text
＃92화



[표적 보고서]

이름 : 진태경

나이 : 27

거주지 : 주소지 xxx-xxx 희망 고시원. 가족과 별거 중.

가족관계 : 1남 1녀 중 장남. 11년 전 아버지 사고사. 어머니와 여동생에 관한 정보는 따로 첨부.



조사를 지시한 지 사흘 만에 받아 보는 보고서다. 다섯 장에 걸쳐 빽빽하게 적힌 정보들을 읽은 임춘수가 입을 열었다.

“야, 1팀장아.”

“예, 길드장님.”

맞은편에 앉아 있던 1팀장이 대답했다. 길드장인 임춘수를 제외하면 상동 길드 유일한 A급 헌터이자 임춘수의 충직한 오른팔이다.

“이 보고서, 읽어 봤냐?”

“아직 안 읽어 봤습니다.”

“왜?”

“길드장님 지시니까요. 추후 들어오는 정보는 중간에서 거르지 말고 그대로 보고하라고 하셨습니다.”

“그럼 이참에 읽어 봐.”

임춘수가 내미는 보고서를 공손히 받아 든 1팀장의 눈동자가 바삐 움직였다. 10분 정도 후, 고개를 든 그가 중얼거렸다.

“이건 좀.”

“그 보고서, 어떻게 생각하냐?”

“전 길드장님 판단에 따를 뿐입니다.”

“아냐, 허심탄회하게 말해 봐.”

잠깐 망설이던 1팀장이 대답했다.

“정보가 잘못된 것 같습니다.”

“정확히 어떤 부분이?”

“보고서 대상인 진태경은 불과 보름 전까지 F급 헌터였습니다. 그러나 C급 헌터로 재각성에 성공했죠. 여기까지는 드문 일이긴 해도 불가능하진 않습니다.”

“계속.”

“하지만 임창수 팀장, 아니 임창수 헌터와 해당 레이드에 참여했던 인원들의 증언에 의하면 진태경은 B급 몬스터인 미노타우로스 무리를 단신으로 해치웠습니다.”

“최소 다섯 마리. 최대 열 마리였지, 아마?”

“네. 심지어 보스 몬스터는 일격에 쓰러트렸다고 했죠.”

“그래. C급 헌터 나부랭이가 미노타우로스 대전사를 한 방에. 이게 말이 되냐?”

“말이 안 된다고 생각합니다.”

“그럼 뭘까?”

결코 몰라서 물어보는 것이 아니다. 1팀장이 자신과 같은 생각을 하고 있는지 다시 한번 확인하는 과정일 뿐이다.

“의심이 가는 부분이 셋 있습니다.”

“읊어 봐.”

“첫째, 보고서가 잘못됐을 경우입니다.”

“이 보고서, 누가 작성한 거지? 홍, 홍 뭐였는데. 홍길동은 확실히 아니고.”

“홍우진입니다. 아직 젊고 경력은 얼마 되지 않았습니다만, 실력은 정평이 나 있습니다.”

“그래, 홍우진인지 홍길동인지 하는 그 새끼한테 다시 한번 확인해. 으름장도 좀 놓고. 아무튼 그래서 두 번째는?”

“둘째, 임창수 헌터와 다른 인원들이 입을 맞춰 거짓말을 한 경우입니다.”

“창수 그 녀석이 정신이 똑바로 안 박혀 있어서 그렇지, 살면서 나한테 거짓말 쳐 본 적이 없다. 계속.”

“마지막은 진태경이 아직 확인되지 않은 A급 헌터이거나 혹은…….”

침착하던 1팀장의 얼굴 위에 곤란한 빛이 스쳤다. 잠시 후, 그가 머뭇머뭇 입을 열었다.

“3차 각성자가 아닐까요?”

“3차?”

“……네.”

“1팀장아. 네가 말해 놓고도 황당하지? 3차 각성자가 말이 되냐, 응?”

1팀장은 고개를 숙이는 것으로 대답을 대신했다.

그 모습에 혀를 찬 임춘수가 보고서를 집어 들었다. 그의 손끝에서부터 극한의 냉기가 흘러나온다.

파스스슥. 차창!

“보고서 다시 작성해. 이번 주까지 끝마치고 월요일 출근할 때 책상 앞에 갖다 놔. 산뜻하게.”

“알겠습니다.”

“그리고 거, 누구야. 평화 길드인가 사랑 길드인가 거기 다른 놈들 관련 정보는 어떻게 됐어?”

“……저, 그에 관해서 지금 막 보고드리려고 했습니다만.”

“뭐야, 하나도 파악 안 됐어?”

“세 명 제외하고는 전부 파악 완료된 상태입니다.”

임춘수가 눈살을 찌푸렸다.

“세 명? 그중 하나는 진태경일 테고. 나머지 둘은?”

“평화 길드의 길드장과 팀장입니다.”

아들놈에게 들어 본 적이 있다. 팀장이라는 젊은 놈은 싸가지가 없고, 길드장이라는 장년인은 레이드 내내 허허 웃기만 하는 속없는 인간이라고.

“그놈들이 왜?”

“락(Lock)이 걸려 있었습니다.”

“뭐?”

“말씀드린 그대롭니다. 개인 정보는 물론이고 계좌 관련해서까지 모두 보안 상태라 감찰팀에서도 당혹스러워하고 있습니다.”

“돈 아꼈냐?”

길드를 운영하려면 기관의 도움이 필요하다. 각 기관에 근무하는 타락한 공무원들은 뇌물을 받고 정보를 넘겨주는 걸 주저하지 않는다.

“안 그래도 듬뿍 안겨 줬는데…….”

“그랬는데?”

“그쪽에서도 좀 꺼리는 기색이 역력합니다. 그쪽 말로는 상부 기관에서 보안을 걸어 놔서 건드리기가 어렵다더군요.”

임춘수는 황당했다.

만들어진 지 한 달도 안 된 길드. 길드원을 다 합쳐 봐야 레이드 팀 하나도 안 나오는 소규모 길드다. 아니, 그 정도면 길드가 아니라 친목회라고 해도 이상하지 않다.

그런데 그깟 놈들이 뭐라고 락이 걸려 있단 말인가?

“허, 이 자식들 봐라.”

“어떻게 할까요?”

“일단 그 부분은 더 깊게 파지 말고 내버려 둬. 이번에 돈 찔러 준 놈들 입단속도 확실히 하고.”

대격변 시절, 불같은 성격으로 유명했던 임찬수는 길드를 운영하면서 중요한 한 가지를 배웠다.

목표를 이루기 위해서는, 그리고 목표 이상의 성과를 얻기 위해서는 침착하고 신중해야 한다는 것이다.

“그럼 그 셋 빼고는 전부 파악 끝났지?”

“네, 완벽합니다.”

철두철미한 성격으로 신임을 얻은 1팀장의 말이다. 임춘수는 고개를 끄덕였다.

“보안 걸려 있다는 두 놈은 방금 내가 말한 대로 조치하고. 우선 진태경 그놈만 집중적으로 파. 길드 감사팀 몇 명 동원해서 따로 감시 인원 늘리고.”

“따로……말입니까?”

“그래, 보고서 상태 보니까 영 아니야. 생각해 보면 우리 길드 감사팀도 뭐, 딱히 밀릴 거 없잖아?”

“그렇긴 합니다만.”

1팀장이 순간 멈칫했다. 의뢰를 하러 갔을 때 홍우진이 신신당부했던 말이 생각나서였다.



‘이 의뢰, 받는 순간 이거 내 일 되는 겁니다. 알죠? 일주일 안에 이 새끼 그날 입은 팬티 색까지 알아낼 테니까 믿고 맡겨요. 괜히 그쪽에서 일 벌렸다가 감시 대상이 눈치 까면 내 일 망치는 거니까.’



경력은 짧아도 일 잘한다고 알음알음 입소문이 나 있는 홍우진이다. 말투는 건방졌지만 프로다운 모습에 신뢰가 갔고, 직접 약속까지 했다.

‘말씀드려야 할 것 같은데.’

하지만 1팀장이 꺼내려던 반대 의견은 임춘수의 한마디에 목구멍 안으로 쏙 돌아갔다.

“왜? 더 할 말 있어?”

“아, 아닙니다. 그대로 전달하겠습니다.”

“그래, 가 봐.”

요즘 임춘수의 기분이 좋지 않다. 최대한 비위를 맞춰 주면서 좋은 방향으로 이끌어 가는 것이 그의 일이다.

‘괜찮겠지? 괜찮을 거야.’

1팀장은 길드장실을 나오면서도 찝찝한 기분을 감추지 못했다.



* * *



집, 휴가.

이 두 단어는 생각만으로도 행복감을 준다. 실제로도 그랬고. 그런데…….

왜앵. 왜애애애앵.

“아오, 미치겠네.”

나는 전광석화 같은 속도로 파리를 후려쳤다. 평범한 손바닥도 아닌 공력이 실린 손바닥이다. 일격에 즉사한 파리를 쓰레기통에 버리고 소파로 돌아왔다.

“뭔 놈의 파리 새끼들이 이렇게 많아?”

물을 마시려고 잠깐 거실로 나온 하연이가 한숨을 푹 내쉬었다.

“여름이니까 그렇지, 오빠 바보야?”

“그 정도가 아니라니까, 지금.”

“뭐 많아 봤자 얼마나 많다고. 방금도 한 마리밖에 없었잖아.”

“한 마리씩 계속 들어오니까 문제지. 잡는 족족 어디서 자꾸 들어오네.”

“몇 마리나 잡았는데?”

“하늘에 맹세코 오전부터 지금까지 100마리는 잡았다.”

“과장하는 것 봐. 이래서 남자들이란…….”

“진짜라고!”

“알았어, 알았어.”

와, 미치겠네. 나는 머리를 쥐어뜯으며 새로운 파리를 때려잡았다. 백 마리? 결코 과장이 아니다. 이놈의 동네는 어떻게 되었길래 한 집에 파리가 이렇게 들끓을 수 있지?

‘창문에 꿀이라도 발라 놨나.’

처음에는 그냥 거슬리는 정도였다. 앞서 하연이가 말했던 것처럼 여름이니까 당연한 현상이라고 생각했다.

하지만 갈수록 뭔가 이상하다는 걸 깨달았다.

‘한 30마리쯤 잡은 후였지.’

이 염병할 것들이 쉬지 않고 들어온다! 한 놈을 잡으면 또 한 놈이, 그놈을 잡으면 다른 놈이 들어와서 자리를 잡았다.

집 안의 모든 창문을 닫고 기감으로 수색 작업까지 거쳤음에도 파리 군단의 악몽은 이어졌다.

왜애애앵.

“저거 봐, 그새를 못 참고 또 한 마리 들어오잖아. 이놈들 도대체 어디서 들어오는 거야?”

미처 발견 못 한 미세한 틈 같은 게 있나 꼼꼼하게 살펴봤지만 나로서는 도저히 알 수 없었다. 말 그대로 개미 새끼 한 마리 통과할 만한 공간에서 들어오는 듯싶었다.

“때려잡지 말고 가만히 둬. 그럼 조용해지니까.”

“그게 무슨 창의적인 헛소리냐. 가만히 둔다고 쟤들이 가만히 있어? 왱왱 하는 소리에 잠도 못 잘 게 뻔한데.”

“내 방 파리는 가만히 있던데?”

“뭐?”

“내 방에도 한 세 마리 정도 있다고. 처음에는 신경 쓰여서 잡을까 했는데, 가만히 두니까 안 날아다니고 가만히 책상에 앉아 있어.”

“그거야 잠깐이고. 너 안 보는 사이에 엄청 날아다닐걸.”

“그냥 좀 게으른 파리들인 것 같던데. 한 번도 안 움직였어.”

“말이 되는 소리를 해라.”

“진짜라니까. 10만 원 내기 콜?”

“10만 원은 있냐? 수험생 주제에.”

“당연히 있지. 지난번에 오빠한테 받은 거.”

“나한테 받은 용돈으로 나랑 내기를 하겠다고?”

“쫄리면 뒈지시든지.”

“……콜.”

시바, 돈이 이렇게 돌고 도는구나. 우리는 하연이의 방으로 곧장 직행했다. 얌전히 앉아 있는 파리 한 마리를 가리키며 녀석이 의기양양하게 웃는다.

“봤지? 내 말이 맞지? 빨리 10만 원 내놔.”

“내놓긴 뭘 내놔. 실험을 해 봐야지.”

나는 파리 위로 손바닥을 내리쳤다. 딱 일반인 수준의, 파리가 충분히 피할 수 있는 속도였다. 그런데…….

움찔. 후다닥.

그 순간에 화들짝 놀라더니 다리를 바쁘게 놀려 도망치는 파리.

그 모습을 본 나는 황당함을 금치 못했다. 하연이도 저게 뭔가 하는 얼굴이다.

“동생아.”

“으, 응.”

“요즘 파리들은 다 저러냐?”

“그, 그럴 수도 있지 않을까? 아무튼 10만 원 줘.”

“줘야지. 주긴 주는데…… 저 파리 좀 이상하지 않아?”

“파리가 파리지. 그냥 좀 이상한 애 같은데.”

“저런 파리가 어디 있어. 내가 살면서 고블린에 미노타우로스는 봤어도 이렇게까지 안 날아다니는 파리는 처음 본다.”

말이 끝난 그 순간이었다.

왜애애앵-

“…….”

“…….”

수상해. 너무 수상해. 타이밍도 공교롭지만 마치 평범해 보이려고 애쓰는 듯한 날갯짓은 더 이상하다. 날아다니는 것도 뭔가 어설프게 비틀거리고.

‘그런 건 둘째치고 기분 나빠. 이 느낌 묘하게 익숙한데.’

어디서 비슷한 기분을 느꼈더라?

아, 그랬지. 이틀 전 집 보러 갔다가 돌아오던 그 골목길.

어쩐지 누군가 나를 감시하는 것 같은 기시감.

‘내가 진짜 예민한 건가.’

파리를 노려보던 내가 [기감]을 끌어 올렸다. 이제 반경 70미터에 이르는 기감의 발동 범위가 집 전체 구석구석으로 뻗어 나갔다.

그리고 아무도 예상치 못한 일이 일어났다.

띠링. 띠링. 띠링.



[Lv.1 집파리 – 패밀리어]

[Lv.1 검정파리 – 패밀리어]

[Lv.1 금파리 - 패밀리어]



“……?”

뭔데, 이거.
```

## Current accepted English baseline

```markdown
# Chapter 92

> **Target Report**
>
> **Name:** Jin Taekyung
>
> **Age:** 27
>
> **Residence:** Address xxx-xxx, Hope Goshiwon[^1]. Living separately from his family.
>
> **Family:** Eldest son in a family of one son and one daughter. Father died in an accident eleven years ago. Information on his mother and younger sister attached separately.

This was the report Im Chunsoo received three days after ordering the investigation. After reading through the densely packed information filling five pages, he opened his mouth.

“Hey, Team 1 Leader.”

“Yes, Guild Master.”

The Team 1 Leader seated across from him answered. Apart from Guild Master Im Chunsoo, he was the only A-rank Hunter in Sangdong Guild, as well as Im Chunsoo’s loyal right hand.

“Did you read this report?”

“Not yet.”

“Why not?”

“Because it was your order, Guild Master. You told us to report any information that came in without filtering it along the way.”

“Then read it now.”

The Team 1 Leader politely accepted the report Im Chunsoo held out to him. His eyes moved rapidly across the pages. About ten minutes later, he raised his head and muttered,

“This is a little…”

“What do you think of the report?”

“I can only follow your judgment, Guild Master.”

“No. Speak frankly.”

After a brief hesitation, the Team 1 Leader answered.

“I think the information is incorrect.”

“Which part, exactly?”

“The subject of the report, Jin Taekyung, was an F-rank Hunter until only half a month ago. However, he succeeded in reawakening as a C-rank Hunter. That much is rare, but not impossible.”

“Go on.”

“But according to the testimony of Team Leader Im Changsoo—no, Hunter Im Changsoo—and the others who participated in that raid, Jin Taekyung single-handedly defeated a group of B-rank monsters, the Minotaurs.”

“Minimum five. Maximum ten, if I remember correctly?”

“Yes. They even said he brought down the boss monster with a single strike.”

“Right. A mere C-rank Hunter taking down a Minotaur Warrior with one blow. Does that make any sense?”

“I don’t think it does.”

“Then what is it?”

He was not asking because he genuinely did not know. He only wanted to confirm once again whether the Team 1 Leader was thinking the same thing he was.

“There are three things that concern me.”

“List them.”

“First, the report may be wrong.”

“Who wrote this report? Hong… What was it? Definitely not Hong Gil-dong.”

“Hong Woojin. He’s still young and doesn’t have much experience, but his ability is well known.”

“Right, that Hong Woojin—or Hong Gil-dong, or whatever the hell his name is. Check with that bastard again. Put some pressure on him, too. Anyway, what’s the second?”

“Second, Hunter Im Changsoo and the others may have coordinated their stories and lied.”

“Changsoo’s an idiot who can’t think straight, but he’s never lied to me in his life. Continue.”

“The last possibility is that Jin Taekyung is an A-rank Hunter whose strength has not yet been confirmed, or perhaps…”

A troubled look crossed the otherwise calm Team 1 Leader’s face. After a moment, he hesitantly opened his mouth.

“Could he be a third-awakening Hunter?”

“Third awakening?”

“…Yes.”

“Team 1 Leader. Doesn’t it sound absurd even to you? A third-awakening Hunter? Does that make any sense?”

The Team 1 Leader answered by lowering his head.

Im Chunsoo clicked his tongue at the sight and picked up the report. Extreme cold began to flow from his fingertips.

Crackle. Crash!

“Rewrite the report. Finish it by the end of this week and put it on my desk when you come in on Monday. Make it nice and clean.”

“Yes, sir.”

“And what about the information on the other people from that Peace Guild—or was it Love Guild?”

“……I was just about to report on that.”

“What? You haven’t found out anything?”

“We’ve finished identifying everyone except for three people.”

Im Chunsoo frowned.

“Three? One of them must be Jin Taekyung. Who are the other two?”

“The Guild Master and Team Leader of Peace Guild.”

He had heard about them from his son. The young Team Leader was an insolent brat, while the middle-aged Guild Master was a clueless man who had done nothing but chuckle throughout the entire raid.

“Why those two?”

“There was a Lock on them.”

“What?”

“Exactly as I said. Not only their personal information, but even their account details are all under security restrictions. The Audit Team is at a loss as well.”

“Did you skimp on the money?”

“Not at all. I already gave them plenty…”

“And yet?”

“They seem very reluctant on their end as well. They said an upper agency had placed the security lock, making it difficult for them to touch.”

Im Chunsoo was dumbfounded.

A Guild that had not even existed for a month. A small Guild whose entire membership could not even make up one raid team. No, at that point, calling it a Guild was strange. It would not have been odd to call it a social club instead.

And yet, who the hell were those bastards to have a Lock placed on them?

“Huh. Look at these bastards.”

“What should we do?”

“Don’t dig any deeper into that part for now. Leave it alone. And make absolutely sure the people we paid this time keep their mouths shut.”

During the Great Cataclysm, Im Chunsoo had been famous for his fiery temper. But after running a Guild, he had learned one important thing.

To achieve a goal—and to gain results beyond that goal—one had to remain calm and cautious.

“So everything else is completely investigated?”

“Yes. Completely.”

That was the answer of the Team 1 Leader, who had earned Im Chunsoo’s trust through his meticulous nature. Im Chunsoo nodded.

“Deal with those two locked targets as I said. For now, focus only on Jin Taekyung. Mobilize a few people from the Guild Audit Team and increase the surveillance separately.”

“Separately…?”

“Yes. Looking at the state of this report, it’s no good. When you think about it, our Guild Audit Team isn’t exactly outclassed, is it?”

“That’s true, but…”

The Team 1 Leader suddenly hesitated. He remembered what Hong Woojin had repeatedly stressed when he went to commission Woojin for the job.

> “The moment I accept this assignment, it becomes my job. Got it? Within a week, I’ll find out the color of this bastard’s underwear on the day in question, so leave it to me. If you cause trouble on your end and the surveillance target catches on, you’ll ruin my job.”

Hong Woojin had little experience, but word had spread that he was good at his work. Despite Woojin’s arrogant way of speaking, his professionalism had inspired trust, and the Team 1 Leader had personally given him his word.

*I should probably tell him.*

But the objection the Team 1 Leader was about to raise went straight back down his throat at Im Chunsoo’s next words.

“Why? Is there something else you want to say?”

“Oh, no, sir. I’ll relay it exactly as you said.”

“Good. You can go.”

Im Chunsoo had been in a bad mood lately. It was the Team 1 Leader’s job to keep him appeased as much as possible and guide him in a favorable direction.

*It’ll be fine, right? It will be.*

Even after leaving the Guild Master’s office, the Team 1 Leader could not shake his uneasy feeling.

* * *

Home. Vacation.

Just thinking about those two words made me happy. And in reality, it was just as wonderful. But…

Bzzzz. Bzzzzzz.

“Ah, this is driving me crazy.”

I swatted at a fly with lightning-fast speed. It was not an ordinary palm strike, either—my palm was charged with internal energy. After killing the fly instantly, I tossed it into the trash and returned to the sofa.

“Why the hell are there so many flies?”

Hayeon, who had briefly come out into the living room to get a drink of water, let out a deep sigh.

“It’s summer, you idiot, Oppa.”

“It’s not just that.”

“What’s the big deal? How many could there be? There was only one just now.”

“That’s the problem. They keep coming in one at a time. Every time I catch one, another one keeps coming in from somewhere.”

“How many have you caught?”

“I swear to heaven, I’ve caught at least a hundred since this morning.”

“Look at you exaggerating. This is why men are…”

“I’m serious!”

“Okay, okay.”

Damn, this was driving me crazy. I tore at my hair and swatted down another fly. A hundred? I was not exaggerating at all. What had happened to this neighborhood that so many flies could swarm into one house?

*Did someone smear honey on the windows?*

At first, they had only been annoying. Just like Hayeon had said, I thought it was a normal phenomenon because it was summer.

But the more time passed, the more I realized that something was strange.

*It was after I’d killed about thirty of them.*

These damn things kept coming in without a break! I would kill one, then another would come in. I would kill that one, and a different fly would take its place.

Even after closing every window in the house and searching with my Qi Sense, the nightmare of the fly army continued.

Bzzzzzz.

“See? Another one came in before we could even turn around. Where the hell are these things coming from?”

I carefully searched for some tiny gap I had failed to notice, but I could not figure it out. They seemed to be coming through spaces barely large enough for a single ant to pass through.

“Don’t swat them. Just leave them alone. Then they’ll quiet down.”

“What kind of creative bullshit is that? You think they’ll stay still just because you leave them alone? We won’t be able to sleep with all that buzzing.”

“The flies in my room stay still.”

“What?”

“There are about three in my room, too. They bothered me at first, so I thought about killing them, but when I left them alone, they stopped flying around and just sat on my desk.”

“That’s only temporary. They must fly around like crazy when you’re not looking.”

“I think they’re just lazy flies. They haven’t moved even once.”

“Say something that makes sense.”

“I’m serious. Want to bet a hundred thousand won?”

“You even have a hundred thousand won? You’re an examinee.”

“Of course I do. It’s from the money you gave me last time.”

“You’re going to bet against me with the allowance I gave you?”

“If you’re scared, you can just die.”

“……Deal.”

Shit. So this was how money went around in circles.

We went straight to Hayeon’s room. She pointed at a fly sitting quietly in place and grinned triumphantly.

“See? I was right, wasn’t I? Hand over the hundred thousand won.”

“Hand over what? We need to run an experiment first.”

I brought my palm down over the fly. I struck at an ordinary person’s speed, slow enough for the fly to dodge easily. But then…

Flinch. Scramble.

The fly startled violently and scurried away, moving its legs as fast as it could.

I could not hide my bewilderment. Hayeon wore a similar expression.

“Sis.”

“Y-Yeah?”

“Are all flies these days like that?”

“Th-They could be, couldn’t they? Anyway, give me the hundred thousand won.”

“I’ll give it to you. I will. But isn’t that fly strange?”

“A fly is a fly. It’s just a weird one.”

“What kind of fly acts like that? I’ve seen goblins and Minotaurs in my life, but I’ve never seen a fly that flies around so little.”

The instant I finished speaking—

Bzzzzzz—

“……”

“……”

Suspicious. Extremely suspicious.

The timing was questionable enough, but the way its wings moved—as if it were trying hard to look ordinary—was even stranger. Even its flight was awkward and unsteady.

*Forget that. It gives me the creeps. This feeling is weirdly familiar.*

Where had I felt something similar?

Oh, right. That alley I had walked through on the way home two days ago, after looking at a house.

That déjà vu of someone secretly watching me.

*Am I really just being oversensitive?*

I glared at the fly and raised my Qi Sense. Its activation range now extended to a radius of seventy meters, spreading into every corner of the house.

And then something no one could have expected happened.

Ding. Ding. Ding.

> **System**
>
> Lv. 1 Housefly—Familiar
>
> Lv. 1 Black Blow Fly—Familiar
>
> Lv. 1 Green Bottle Fly—Familiar

“……?”

*What the hell is this?*

[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 92`.

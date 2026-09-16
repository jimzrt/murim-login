# Master Edit Task — Chapter 93

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
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 레벨               | **Level**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 마정석     | **Magic Gem**         |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 대한민국 | **Korea** | Country reference. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
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
| 기운 | murim_vs_hunter | Murim energy is qi; do not render Murim 기운 as Hunter mana. | |
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

#### Chapter 91 tail (verified mastered)

…
who cut off contact. Were you really such close friends that you’d still defend him?” Park Jihoon smiled gently. “No. Not at all.” * * * “What do you think?” The real estate agent’s voice was thick with phlegm. He had chain-smoked for an hour while waiting for me, and his complexion looked awful. “It’s nice.” I wasn’t just being polite. The two-story detached house with a broad lawn was better than any house I had seen so far. *Four bedrooms, two bathrooms, and a spacious living room.* It looked like something straight out of a fairy tale. I toured the house while half-listening to the real estate agent’s detailed explanations, then stepped out through the front gate. “Listings like this are hard to find. The current owner has several buildings, but he’s putting this one up as a quick sale because he’s planning to put up another building in Incheon.” “So what’s the market price?” “Exactly what you saw online. 3.38 billion won.” It was still an amount that made me want to swear, but the house was worth every bit of it. For my family’s safety, and because this place held special meaning for us. “Please contact me.” “Then…?” “I’ll buy it.” “Oh, you’ve made an excellent decision, Boss!” I firmly clasped the hand he offered me. “Since we’re on the subject, would it be all right if I took another look around the neighborhood?” “…” “I’m joking.” Look at how hard he was squeezing my hand over one little joke. * * * “Have a safe trip home.” “Thanks. Take care.” I left the real estate office after putting down a ten-percent deposit. The owner and I had agreed to set a date soon and proceed with the formal purchase. Since he needed cash quickly, everything had been settled without delay. *I’ll have to put off moving for a while.* The new house was about an hour from where my family currently lived. Even after buying it, moving in right away would be difficult. More importantly, Hayeon had her college entrance exam this year. I would surprise them with the news immediately afterward. *I’ll need to remodel the place, too.* I intended to make it as similar as possible to our old home. It had happened a very long time ago, but perhaps because we had lived there for sixteen years, I remembered the layout perfectly. *I’ll sign the formal contract and find an interior contractor… What else is there?* I knew how to thrust a spear inside a Gate, but I was a complete novice when it came to any of this. I had no idea where to begin. I was turning into a dark alley while thinking about this and that when— *Hm?* The back of my neck prickled. My fine hairs stood on end, and the air seemed to shift. I sensed someone secretly watching me from behind. *Open Inventory. Summon.* I spun around like lightning, a dagger already in my grip. But… Meow. “What? A cat?” Meow. A mottled cat jumped down from the wall. It glanced at me, then slowly wandered away. *Did I overreact?* My senses had become more acute as they improved. Normally, I would have grown accustomed to them gradually as I developed, but I was progressing too quickly for any adjustment period to matter. *No. Something felt strange this time.* I belatedly raised my Qi Sense, but there was nothing in the deserted alley. Beep. > **System** > > There are no targets for **Qi Sense** to detect. If the System said there was nothing, then there was nothing. I must have been especially tired lately. “Ah, now I suddenly have a craving for samgyetang.[^1]” Since I had thought of it, maybe I should go out to eat with the whole family. The thought of tender chicken and piping-hot broth put a spring in my step. [^1]: Samgyetang is a Korean ginseng chicken soup traditionally served piping hot. * * * In a dark, cramped room, a young man deep in meditation snapped his eyes open. “Gasp!” His hair stuck out in every direction, soaked with sweat, and his breathing was ragged. He hurriedly gulped bottled water, then let out a relieved sigh. “Fuck, that scared me.” Everything had gone smoothly. In fact, it had been downright boring. The investigation target happened to be on vacation, and his movements were predictable. Home, convenience store, home. Today, he had traveled as far as an hour away, but tracking him had still been no trouble. But then… “What the fuck was that? Why did that bastard suddenly turn around and start pulling that shit?” The moment he saw that sharp gaze, his heart had dropped. If he had not hurriedly severed the Link with the cat, he might really have been discovered. “He didn’t know, did he?” The target was only a C-rank Hunter. Compared to the people he had investigated before, the man was far beneath them. *There’s no way. Who do you think I am?* Hong Woojin, a B-rank mage and information broker, shook his head. He was a master of tracking and surveillance magic. He couldn’t cast flashy offensive spells, but in this particular field, he prided himself on being the best. “That’s right. There’s no way. It was just a coincidence. A coincidence.” Hong Woojin muttered the words like a mantra. Anxiety lingered in his voice.

#### Chapter 92 tail (verified mastered)

…
after leaving the Guild Master’s office, the Team 1 Leader could not shake his unease. * * * Home. Vacation. Just thinking about those two words made me happy. The reality was every bit as wonderful. Except… Bzzzz. Bzzzzzz. “Ah, this is driving me crazy.” I swatted a fly with lightning speed. Not with an ordinary palm, either, but one charged with internal energy. I tossed the fly, dead in one strike, into the trash and returned to the sofa. “Why the hell are there so many fucking flies?” Hayeon, who had briefly come out into the living room to get a drink of water, let out a deep sigh. “It’s summer, you idiot, Oppa.” “I’m telling you, this is more than that.” “How many could there possibly be? There was only one just now.” “That’s the problem. They keep coming in one at a time. Every time I kill one, another shows up from somewhere.” “How many have you killed?” “I swear to heaven, I’ve killed at least a hundred since this morning.” “Look at you exaggerating. This is why men are…” “I’m serious!” “Okay, okay.” Wow. This was driving me insane. I tore at my hair and swatted another fly. A hundred? That was no exaggeration. What the hell was wrong with this neighborhood that one house could be overrun with so many flies? *Did someone smear honey on the windows?* At first, they had merely been annoying. Like Hayeon said, I assumed they were only around because it was summer. But the more time passed, the more I realized that something was strange. *It was after I’d killed about thirty of them.* These damn things kept coming in without a break! I would kill one, then another would come in. I would kill that one, and a different fly would take its place. Even after I closed every window and searched the whole house with Qi Sense, the nightmare of the fly army continued. Bzzzzzz. “See? Another one came in before we could even turn around. Where the hell are these things coming from?” I carefully searched for some tiny gap I had failed to notice, but I could not figure it out. They seemed to be coming through spaces barely large enough for a single ant to pass through. “Stop swatting them and leave them alone. Then they’ll quiet down.” “What kind of creative bullshit is that? You think they’ll sit still just because you leave them alone? We obviously won’t be able to sleep with them buzzing all night.” “The flies in my room stay still.” “What?” “There are about three in my room, too. They bothered me at first, so I thought about killing them, but when I left them alone, they stopped flying around and just sat on my desk.” “That’s only temporary. They probably fly around like crazy when you’re not looking.” “I think they’re just lazy flies. They haven’t moved even once.” “Say something that makes sense.” “I’m serious. Want to bet a hundred thousand won?” “You even have a hundred thousand won? You’re supposed to be studying for exams.” “Of course I do. It’s the money you gave me last time.” “You’re going to bet against me with the allowance I gave you?” “If you’re scared, you can just die.” “…Deal.” Shit. So this was how money went around in circles. We went straight to Hayeon’s room. She pointed at a fly sitting quietly on her desk and grinned triumphantly. “See? I was right, wasn’t I? Hurry up and hand over the hundred thousand won.” “Hand over what? We need to run an experiment first.” I brought my palm down over the fly. I struck at an ordinary person’s speed, slow enough for the fly to dodge easily. But then… Flinch. Scramble. The fly jumped in alarm and scurried away as fast as its legs could carry it. I was dumbfounded. Hayeon looked just as baffled. “Sis.” “Y-Yeah?” “Are all flies these days like that?” “M-Maybe they do? Anyway, give me the hundred thousand won.” “I’ll give it to you. I will. But isn’t that fly strange?” “A fly is a fly. That one’s just a little strange.” “What kind of fly acts like that? I’ve seen goblins and Minotaurs in my life, but I’ve never seen a fly that flies around so little.” The instant I finished speaking— Bzzzzzz— “……” “……” Suspicious. Way too suspicious. The timing was questionable enough, but the way its wings moved—as if it were trying hard to look ordinary—was even stranger. Even its flight was awkward and unsteady. *Never mind that. It gives me the creeps. This feeling is weirdly familiar.* Where had I felt something like this before? Oh, right. That alley I had walked through two days ago, on my way home from viewing the house. That strange sense of déjà vu, as though someone were watching me. *Am I really just being oversensitive?* I glared at the fly and raised my Qi Sense. Its activation range now extended to a radius of seventy meters, spreading into every corner of the house. And then something no one could have expected happened. Ding. Ding. Ding. > **System** > > Lv. 1 Housefly—Familiar > > Lv. 1 Black Blow Fly—Familiar > > Lv. 1 Green Bottle Fly—Familiar “…?” *What the hell is this?* [^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.

## Korean source

```text
＃93화



‘이런 아마추어 자식들.’

홍우진은 분통이 터질 지경이었다. 지난번처럼 고양이의 몸에 들어갔다면 털을 바짝 세우고 하악질을 했을 것이다.

하지만 지금 그는 손톱보다도 작은 쌀벌레. 냉장고 밑 틈새에 숨어 꿈틀거리는 게 할 수 있는 최대의 분노 표출이었다.

왜애애앵.

‘저 새끼 저거, 또 들어오네.’

분노의 대상은 끊임없이 집 안으로 들어오는 파리였다.

어느 놈인지는 몰라도 나름 조심한다고 한 마리씩만 슬금슬금 들어오긴 하는데, 오히려 진태경의 경계심만 돋우는 꼴이다.

“아오, 이놈의 파리.”

후웅. 찍!

뻔한 최후. 홍우진은 혹시라도 진태경이 알아챌까 봐 몸이 달았다.

‘꼭 저런 놈들이 상도덕도 없는 주제에 머리까지 나빠요.’

어지간한 헌터들은 알아차리지 못하겠지만 그는 바로 알아봤다.

저 파리는 마법사가 조종하는 패밀리어(Familiar)라는 사실을. 같은 마법사만이 느낄 수 있는 매우 미약한 마나가 그 증거다.

‘누구한테 고용된 놈이지? 역시 상동 길드인가?’

만약 그렇다면 이 의뢰는 당장 때려치워야 한다. 그는 자신의 실력에 엄청난 자부심을 갖고 있는 프로니까.

신성한 업무 공간에 훼방꾼이 끼어드는 일은 참을 수 없었다.

‘그렇게 신신당부했는데도…….’

아무리 일을 잘 처리하더라도 결국 성질 급한 의뢰인이 풀어 놓은 미꾸라지 한 마리가 물을 흐릴 때가 있다. 바로 지금처럼.

“요즘 파리들은 다 저러냐?”

“그, 그럴 수도 있지 않을까? 아무튼 10만 원 줘.”

“줘야지. 주긴 주는데…… 저 파리 좀 이상하지 않아?”

젠장, 이렇게 될 줄 알았지.

홍우진은 욕을 삼키며 열심히 몸을 움직였다. 꿈틀꿈틀, 사람의 시선이 닿지 않는 더 깊은 곳으로 기어가던 그때였다.

찌릿.

‘……어?’

그는 몸이 붕 뜨는 듯한 낯선 감각에 사로잡혔다. 패밀리어 마법을 사용하기 시작한 이래 단 한 번도 없었던 일이다.

‘뭐지? 이번 패밀리어가 너무 작아서 그런가?’

찰나에 불과했지만 홍우진은 찝찝함을 감출 수 없었다. 순간 탐지 마법은 아닌지 하는 의심이 들었지만 이내 고개를 저었다.

‘마법은 절대 아니야.’

진태경이 비(非)마법 헌터이기 때문만은 아니다. 어차피 돈만 있으면 마법 장비를 구할 수 있는 세상 아닌가?

하지만 동류는 동류를 알아보는 법. B급 마법사인 그가 탐지 마법을 구분하지 못할 리 없다.

‘순간적으로 연결이 약해진 거겠지. 맞아. 분명히 그럴 거야.’

단순한 착각이라고 생각하게 된 결정적인 계기는 진태경의 반응이었다.

“날개를 다쳐서 그런가, 파리가 어째 비실비실하네.”

짝!

경쾌한 소리와 함께 다시 거실로 나온 진태경이 소파에 드러누웠다. 예능 프로그램을 보며 낄낄거리기를 잠시, 웃음소리 대신 요란한 코골이가 집 안을 가득 채웠다.

드르렁. 드르렁.

그제야 홍우진의 마음이 느슨하게 풀어졌다.

‘그럼 그렇지. C급 헌터, 그것도 얼마 전까지 F급이었던 놈이 뭘 알겠어. 이틀 전에 있었던 일도 전부 우연이 분명해.’

이틀 전, 고양이를 패밀리어 삼아 진태경을 관찰하다 놀랐던 일이 아직 마음 한편에 남아 있었다. 왠지 모르게 그 후로도 자꾸만 신경 쓰였는데 이제야 한시름 놓을 수 있을 것 같았다.

‘저런 허접한 패밀리어도 못 알아챌 정도면, 뭐. 말 다 한 거지.’

한 가지 문제가 있다면 저 게으른 놈이 도무지 움직일 생각이 없다는 건데…….

‘이제는 조금 더 과감하게 감시해야겠어.’

홍우진이 하고 많은 생명체 중 쌀벌레를 패밀리어로 골랐던 건 진태경에 대한 일말의 경계심 때문이었다.

그러나 이제는 이 작고 느려 터진 벌레의 몸에서 빠져나가도 될 듯싶었다.

‘내일은 다른 모습으로 만나자고, 진태경.’

팟.

홍우진은 링크를 해제했다. 냉장고 틈새에 숨어 있던 그것은 더 이상 패밀리어가 아니다. 그저 작고 연약한 쌀벌레에 불과했다.

그리고 다음 순간.

드르렁…….

진태경의 코골이가 서서히 잦아들더니 이내 뚝 끊겼다.



* * *



미약한 기운 하나가 사라진다. 감각을 총동원하고 있기에 느낄 수 있었던 변화였다.

‘갔나?’

기지개를 켜는 척 눈을 떴다. 가장 먼저 눈길이 향한 곳은 냉장고 바닥 틈새였다.



[Lv.1 쌀벌레]



불과 10분 전만 하더라도 ‘패밀리어’라는 꼬리표가 붙어 있던 레벨창이다. 링크가 끊긴 지금은 아니지만.

“흐아암. 뭐 먹을 거 없나…….”

나는 소파에서 일어나 자연스럽게 집 안을 돌아다녔다. 그러고 나서야 확신할 수 있었다.

‘더 이상 패밀리어는 없어.’

[기감]에 걸려드는 건 평범한 날벌레 몇 마리뿐. 그중 패밀리어는 어디에도 없다.

쉬지 않고 들려오던 파리 날갯짓 소리도 뚝 끊긴 후였다.

방금 일로 놈들도 아마 뜨끔했을 테니 최소한 오늘 하루만큼은 얼씬도 못 하겠지.

‘젠장, 패밀리어라니.’

패밀리어(Familiar) 마법.

마법사들이 사용하는 일종의 정신계 마법이다. 시전자는 패밀리어로 삼은 생물체와 정신이 연결되며 수준에 따라서는 자신의 뜻대로 조종할 수도 있다고 했다.

‘실제로 경험해 본 건 처음인데.’

근접 헌터라고 모든 무기의 달인이 아니듯 마법사도 마찬가지다. 그중에서도 정신계 마법은 꽤 어려운 축에 들어간다고 들었다.

‘그런 놈들이 왜 나를?’

놈, 이 아니라 놈들인 이유는 패밀리어가 두 마리였기 때문이다. 두 놈이 한패일 수도 있고, 아닐 수도 있다.

그러나 누가 보냈는지는 대강 짐작 가는 구석이 있었다.

‘상동 길드밖에 더 있나.’

현실에서 모종의 원한 관계를 맺은 곳이라고는 상동 길드 한 군데뿐이다. 정확히는 임창수지만.

‘자식을 건드리면 아버지가 뛰어나오는 법이지.’

냉혹하고 성질 더럽다는 A급 헌터, 임춘수.

오늘 벌어진 일이 그의 지시라면 쉽게 끝나진 않을 것이다.

하지만…….

‘이쪽에서도 당하고 있을 수만은 없지.’

이틀 전 나를 미행한 것까지는 괜찮다. 참을 수 있다.

그러나 오늘 일은 참을 수 없다. 이곳은 집이고, 사랑하는 가족이 사는 곳이니까. 놈들은 내 역린을 건드린 거다.

‘이 새끼들을 어떻게 엿 먹여야 하나…….’

고민하던 그때, 하연이의 방문이 벌컥 열렸다.

딱딱하게 굳은 얼굴. 혹시 놈들이 나 모르게 패밀리어로 무슨 수작질을 벌였나? 마음이 다급해진다.

“오빠.”

“왜, 무슨 일이야? 방에 뭐 이상한 거라도 있어?”

“아니, 그런 거 아냐.”

“그럼 뭔데?”

“10만 원 왜 안 줘?”

“…….”

그래. 내가 너를 너무 과소평가했구나.



* * *



다음 날 아침. 나는 날이 밝기가 무섭게 집을 나섰다.

지난밤 내내 [기감]으로 패밀리어의 침입을 대비하느라 눈이 뻑뻑했지만 운기조식으로 피로를 풀었다.

“어디로 모실까요?”

“일산 라페스타요.”

택시는 뻥 뚫린 도로를 막힘없이 달렸고, 생각했던 것보다 훨씬 빨리 목적지에 도착했다.

‘스토어는 몇 년 전에 한 번 와 봤던 거 이후로 처음인가?’

일산 중심가에 위치한 스토어(Store)는 멀리서 봐도 확연히 눈에 띄었다. 일단 근처의 다른 가게에 비해 압도적으로 컸고 화려했다.

거기에 다른 가게들과 다른 점이 또 있다. 입구에서 정장을 입은 경비가 손님들을 걸러 내고 있었다.

“아저씨, 우리 성인이라니까요?”

“안 됩니다.”

“성인인데 왜 출입 금지냐고요.”

“지문 인식기가 성인이 아니라고 하니까요.”

“그거 불량 아니에요?”

“아닙니다.”

“아 씨, 좀 들여보내 달라고요.”

“뭔 씨?”

경비의 말에 척 봐도 앳되어 보이는 10대 대여섯 명이 움찔하며 뒷걸음질 쳤다.

“……뭐요.”

“손님한테 이렇게 해도 되는 거예요?”

“손님? 하, 이 어린노무 새끼들이 진짜.”

경비가 피곤한 듯한 얼굴로 눈가를 문질렀다. 그는 평범한 성인 남성이 아니라 고용된 경비 헌터였다. 미성년자 대여섯이 아니라 격투기 선수가 떼거지로 와도 뚫을 수 없다.

“나한테 손님은 헌터 아니면 회원증 발급받은 민간인 성인들이야. 너네 같은 고삐리가 아니라.”

“…….”

“좋게 말할 때 갈래, 아니면 경찰 부를까?”

어딜 가나 저런 놈들이 꼭 있다. 일반인들은 접할 수 없는 온갖 물건들로 가득한 스토어에는 더더욱.

“……야, 야. 가자.”

앞에서 얼쩡거리던 놈들이 물러가고 나서야 나를 발견한 경비가 친절한 말씨로 물었다.

“무슨 일로 오셨습니까?”

“물건을 구입하려고요.”

“회원권 혹은 헌터 자격증을 제시해 주시면 됩니다.”

“여기요.”

“확인 절차 좀 걸치겠습니다.”

자격증 확인과 지문 인식을 거친 후에야 출입증이 주어졌다.

“C급 헌터님이시니 3층까지 이용 가능하십니다.”

스토어는 층마다 구비되어 있는 물품이 다르다. F급 헌터 시절에 딱 한 번 와 봤었는데, 당시 내 등급으로는 2층이 한계라 그 위로는 구경도 못 해 봤다.

“즐거운 시간 되십시오.”

“네, 고생하세요.”

문을 통과하자 끝도 없이 늘어선 유리 진열대가 보인다.

일반적인 가게와는 비교도 안 될 정도로 넓은 공간. 그러나 보이는 손님은 몇 되지 않는다.

‘하긴, 붐비는 게 이상하지.’

이곳을 이용할 수 있는 사람들은 극소수다. 대한민국 전체 인구의 0.1%에 불과한 헌터들, 그리고 회원권을 발급받을 수 있을 정도로 사회적 영향력이 있는 일반인들.

그들이 스토어의 주 고객이다.

“해당 상품은 국내 S사에서 제작하였으며 경보 마법이 내장되어 있어 보안에 유용…….”

“해외 M사에서 제작한 브로치입니다. 아름답고 감각적인 디자인과 실드 마법이 내장되어 있어 사모님 호신용으로…….”

열심히 고객들에게 제품을 설명 중인 직원들.

맞다. 스토어는 민간에서 구하기 힘든 고가의 마법 물품을 구매할 수 있는 일종의 명품 백화점이다.

“그럼 그거랑 이거랑. 저것도 줘 봐요.”

“더 성능 좋은 거 없나? 가격은 신경 쓰지 말고 가져와 봐.”

고객 숫자는 적을지 몰라도 구매력 하나는 최강이다.

기본 수백만 원 대의 물건을 사들이는 사람들을 멍하니 바라보고 있는데 예쁘장하게 생긴 여직원이 다가와 고개를 숙였다.

“안녕하십니까. 고객님의 안내를 도와드릴 일산 스토어 김선희 대리입니다.”

“아, 예.”

지난번에 왔을 때도 정중하게 대해 줬지만 이 정도는 아니었는데.

C급 정도 되니까 손님 접대가 제법 극진하다.

“혹시 찾으시는 제품이 있으십니까?”

“레이드 장비를 좀 사려고요.”

직원의 표정이 밝아졌다. 스토어에는 수많은 마법 물품이 있지만 그중에서도 가장 고가에 속하는 것이 헌터 장비다.

더군다나 나는 C급 헌터. 중급 헌터 정도면 장비 하나만 골라도 억 소리가 나온다.

그러니 판매 직원 입장에서는 실적 쌓을 생각에 기분이 좋을 수밖에.

“3층으로 안내해 드리겠습니다.”

에스컬레이터 쪽으로 몸을 튼 그녀에게 말했다.

“아뇨, 2층으로 가 주세요.”

“네? 하지만 C급 헌터 장비를 구매하시려면 3층으로…….”

“괜찮아요. 제가 사려는 건 하급 헌터용 무기니까.”

살짝 어두워지는 직원의 얼굴을 모른 척하고 먼저 에스컬레이터에 올랐다.

‘쥐새끼 잡을 때 쓸 만한 게 있으려나.’

인벤토리를 채워야 할 때가 왔다.



* * *



“괜찮아요. 제가 사려는 건 하급 헌터용 무기니까.”

고객의 말에 김선희 대리는 몰래 한숨을 내쉬었다. 판매 실적에 유난히 신경 쓰고 있는 그녀로서는 영 달갑지 않은 소식이다.

‘이번 달에 좋은 실적을 올려야 승진할 텐데.’

서울 지점에 있는 입사 동기는 벌써 팀장을 달았다. 운이 좋은 건지, 수완이 좋은 건지 걸리는 손님마다 큰손이란다.

그에 비하면 자신은…….

“이거 괜찮네요.”

“아, 네. 해당 제품은 F급 마정석으로 제작된…….”

김선희는 퍼뜩 정신을 차리고 설명을 시작했다. 고객이 집어 든 것은 날이 검게 칠해진 단검이었다.

다른 무기들에 비하면 특별한 것도, 그렇다고 마법이 내장된 것도 아닌 평범한 소모품.

“가격은요?”

“현재 여름 특가 할인 중이라 52만 원의 저렴한 가격으로 모시고 있습니다.”

“음. 비싼데.”

“…….”

C급 헌터 연봉이 어떻게 되더라? 기본 수당만 몇억 아니었나? 김선희는 어이가 없었지만 묵묵히 고객의 선택을 기다렸다.

“에이, 어쩔 수 없지. 살게요. 하나 주세요.”

“……네.”

돈 아까워 죽겠다는 얼굴이 밉상 그 자체다. 김선희가 내심 욕을 삼키며 단검을 집어 든 그때였다.

“아뇨. 그거 말고요.”

“네?”

“옆에 있는 거요.”

그녀의 시선이 옆을 향했다. 보관 박스에 가지런히 정렬된 100개의 단검이 보인다.

“같은 제품입니다, 고객님.”

“알아요. 저걸로 하나 주세요.”

“……설마 저 보관 박스를 말씀하신 건가요?”

“네. 저거 한 박스 주세요. 그리고 저것도 한 박스 주시고, 저것도…….”

김선희 대리의 실적 걱정이 사라지는 순간이었다.
```

## Current accepted English baseline

```markdown
# Chapter 93

*What a bunch of amateurs.*

Hong Woojin was furious enough to burst. If he had entered the cat’s body like last time, he would have puffed up its fur and hissed.

But right now, he was a rice weevil smaller than a fingernail. The most he could do to express his anger was hide in the gap beneath the refrigerator and wriggle.

Bzzzzzz.

*That bastard’s coming in again.*

The target of his anger was the fly that kept entering the house.

Woojin did not know who was behind them, but whoever it was seemed to think they were being careful by sneaking the flies in one at a time. Instead, they were only putting Jin Taekyung further on guard.

“Ugh, these damn flies.”

Whoosh. Smack!

A predictable end. Hong Woojin grew anxious, worried that Jin Taekyung might notice him.

*Bastards like that have no professional courtesy, and they’re stupid on top of it.*

Most Hunters would never have noticed, but he recognized it immediately.

That fly was a Familiar being controlled by a mage. The proof was the incredibly faint mana that only another mage could sense.

*Who hired the bastard? Sangdong Guild, after all?*

If that was the case, he would have to quit this assignment right away. He was a professional with immense pride in his abilities.

He could not tolerate an intruder interfering with his sacred workspace.

*I told them over and over…*

No matter how well you handled a job, there were times when a single loach released by an impatient client muddied the water. Just like now.

“Are all flies like that these days?”

“Th-They could be, couldn’t they? Anyway, give me the hundred thousand won.”

“I will. I’ll give it to you, but… don’t you think that fly’s a little strange?”

Damn it. He knew this would happen.

Swallowing his curses, Hong Woojin hurriedly moved his body. He was wriggling deeper into a place no human eyes could reach when—

A jolt.

*…Huh?*

He was seized by a strange sensation, as if his body had suddenly floated into the air. It had never happened once since he began using Familiar magic.

*Is it because this Familiar is too small?*

The sensation lasted only an instant, but Hong Woojin could not shake off his unease. For a moment, he wondered whether it had been some kind of detection spell, but he soon shook his head.

*It definitely wasn’t magic.*

That was not merely because Jin Taekyung was a non-mage Hunter. After all, this was a world where anyone could obtain magical equipment if they had enough money.

But mages recognized their own kind. As a B-rank mage, there was no way he could fail to distinguish a detection spell.

*The connection must have weakened for a moment. Yes. That has to be it.*

The decisive reason he convinced himself it had been a simple illusion was Jin Taekyung’s reaction.

“Maybe its wing’s injured. This fly’s looking pretty weak.”

Smack!

With a crisp sound, Jin Taekyung returned to the living room and sprawled out on the sofa. He chuckled at a variety show for a while, but soon the house was filled with loud snoring instead of laughter.

Grrrrr. Grrrrr.

Only then did Hong Woojin relax.

*Of course. What could a C-rank Hunter who was an F-rank until recently possibly know? What happened two days ago must have been a complete coincidence, too.*

The incident from two days ago still lingered in the back of his mind. He had been watching Jin Taekyung through a cat Familiar and had been startled by what happened. For some reason, it had continued to bother him ever since. Now, at last, he felt he could breathe a little easier.

*If he can’t even recognize a shoddy Familiar like this, then that says it all.*

There was only one problem: the lazy bastard had no intention of moving at all…

*I’ll have to monitor him a little more boldly from now on.*

Hong Woojin had chosen a rice weevil from among all the living creatures in the world because he had retained a sliver of caution toward Jin Taekyung.

But now, it seemed safe to leave the body of this tiny, painfully slow insect.

*Let’s meet in a different form tomorrow, Jin Taekyung.*

Pop.

Hong Woojin severed the Link. The creature hiding beneath the refrigerator was no longer a Familiar. It was nothing more than a small, fragile rice weevil.

And then—

Grrrrr…

Jin Taekyung’s snoring gradually faded before stopping altogether.

* * *

A faint presence disappeared. I could sense the change only because I was using every one of my senses.

*Did he leave?*

I opened my eyes while pretending to stretch. The first place I looked was the gap beneath the refrigerator.

> **System**
>
> Lv. 1 Rice Weevil

Only ten minutes ago, its Level window had carried the tag “Familiar.” Not anymore—not with the Link severed.

“Yaaawn. Is there anything to eat…?”

I got up from the sofa and casually walked around the house. Only then could I be certain.

*There aren’t any Familiars left.*

The only things caught by my Qi Sense were a few ordinary flying insects. There was no Familiar anywhere.

The buzzing of wings that had continued without pause had stopped, too.

They had probably gotten spooked by what just happened, so at least they would not show their faces for the rest of the day.

*Damn it. A Familiar?*

Familiar magic.

It was a kind of mental magic used by mages. The caster formed a mental connection with the creature chosen as a Familiar and, depending on the caster’s skill, could even control it at will.

*That was my first time experiencing it firsthand.*

A melee Hunter was not automatically a master of every weapon, and mages were the same. Mental magic, in particular, was said to be among the more difficult branches.

*Why would people like that come after me?*

The reason I thought of them as “people” rather than “someone” was that there had been two Familiars. The two could have been working together, or they might not have been.

Still, I had a rough idea of who had sent them.

*Who else could it be but Sangdong Guild?*

The only place I had formed some kind of grudge against in the real world was Sangdong Guild. More precisely, Im Changsoo.

*When you mess with someone’s child, the father comes running.*

Im Chunsoo, the A-rank Hunter known for being cold-blooded and foul-tempered.

If what happened today was his order, this would not end easily.

But…

*I can’t just sit back and take it.*

I could let the fact that they had followed me two days ago go. I could tolerate that.

But I could not tolerate what happened today. This was my home, the place where my beloved family lived. They had touched my one inviolable boundary.

*How should I screw these bastards over…?*

I was thinking about it when Hayeon’s bedroom door flew open.

Her face was stiff. Had they used a Familiar to pull something behind my back? My thoughts grew frantic.

“Oppa.”

“What is it? What happened? Is there something strange in your room?”

“No, it’s not that.”

“Then what is it?”

“Why haven’t you given me the hundred thousand won?”

“…”

Right. I had been underestimating you far too much.

* * *

The next morning, I left the house as soon as dawn broke.

My eyes felt gritty from staying alert all night in preparation for another Familiar’s intrusion with Qi Sense, but I shook off the fatigue by circulating my qi.

“Where should I take you?”

“Ilsan Lafesta, please.”

The taxi sped along the wide-open roads without a hitch, reaching the destination much faster than I had expected.

*Is this my first time coming to the Store since I visited once a few years ago?*

The Store, located in the center of Ilsan, stood out clearly even from a distance. For one thing, it was overwhelmingly larger and more splendid than the shops around it.

There was another thing that set it apart from ordinary stores. At the entrance, guards in suits were screening the customers.

“Sir, we’re adults, I’m telling you!”

“No.”

“We’re adults, so why aren’t we allowed inside?”

“Because the fingerprint scanner says you’re not adults.”

“Isn’t it defective?”

“No.”

“Ah, shit, just let us in!”

“‘Shit’?”

Five or six teenagers who looked obviously young flinched and took a step back.

“…What?”

“Is that any way to treat customers?”

“Customers? Ha. You little shits, seriously.”

The guard rubbed the corners of his eyes with a weary expression. He was not an ordinary adult man but a hired guard Hunter. Even if a whole crowd of professional fighters came instead of five or six minors, they would not be able to force their way in.

“Customers to me are Hunters or civilian adults who’ve been issued membership cards. Not high school punks like you.”

“…”

“Are you leaving while I’m asking nicely, or should I call the police?”

People like that existed everywhere. Especially in a Store filled with all kinds of goods ordinary people could never access.

“…Hey, hey. Let’s go.”

Only after the kids loitering in front had left did the guard notice me. He addressed me politely.

“What brings you here?”

“I’d like to purchase something.”

“Please present your membership card or Hunter certification.”

“Here.”

“I’ll need to complete the verification process.”

Only after my certification had been checked and my fingerprints scanned was I given an admission pass.

“As a C-rank Hunter, you may access up to the third floor.”

The items stocked on each floor of the Store were different. I had visited once when I was an F-rank Hunter, but the second floor had been the highest I could access at the time. I had never even gotten to look around above it.

“Have a pleasant time.”

“Thank you. Have a good one.”

Once I passed through the doors, I saw endless rows of glass display cases.

The space was incomparably larger than an ordinary shop. Yet there were only a handful of customers in sight.

*Well, it would be strange if this place were crowded.*

The people who could use this place were an extremely small minority: Hunters, who made up only 0.1 percent of Korea’s total population, and civilians with enough social influence to be issued membership cards.

They were the Store’s main customers.

“This item was manufactured by domestic S Company and has a built-in alarm spell, making it useful for security…”

“This brooch was made by overseas M Company. With its beautiful, tasteful design and built-in shield spell, it’s perfect for your wife’s personal protection…”

The employees were busy explaining their products to customers.

That was right. The Store was a kind of luxury department store where people could buy expensive magical goods that were difficult to obtain through ordinary channels.

“Then I’ll take that one and this one. Bring me that, too.”

“Don’t you have anything with better performance? Don’t worry about the price. Bring me some options.”

There might not have been many customers, but their purchasing power was unmatched.

I was staring blankly at people buying goods that cost at least several million won when a pretty female employee approached and bowed.

“Hello. I’m Assistant Manager Kim Seonhee from the Ilsan Store. I’ll be assisting you today.”

“Ah, yes.”

She had treated me politely the last time I visited, too, but not to this extent.

Now that I was a C-rank Hunter, the customer service was considerably more lavish.

“Is there a particular product you’re looking for?”

“I’d like to buy some raid equipment.”

The employee’s expression brightened. The Store carried countless magical goods, but Hunter equipment was among the most expensive of them all.

And I was a C-rank Hunter. Even a mid-level Hunter could spend hundreds of millions of won on a single piece of equipment.

Naturally, a sales employee would be delighted at the thought of adding that kind of sale to her record.

“I’ll show you to the third floor.”

As she turned toward the escalators, I spoke.

“No, please take me to the second floor.”

“Pardon? But to purchase C-rank Hunter equipment, you’ll need to go to the third floor…”

“It’s fine. I’m looking for weapons for low-rank Hunters.”

I pretended not to notice her expression darkening and stepped onto the escalator first.

*I wonder if they have anything useful for killing rats.*

The time had come to fill my Inventory.

* * *

“It’s fine. I’m looking for weapons for low-rank Hunters.”

Assistant Manager Kim Seonhee secretly sighed at the customer’s words. As someone who was unusually concerned with her sales numbers, this was far from welcome news.

*I need a good sales record this month if I want to get promoted.*

The colleague who had joined the company at the same time as her, but worked at the Seoul branch, was already a Team Leader. Whether it was because of luck or business savvy, every customer she encountered was apparently a big spender.

Compared to her…

“This one looks good.”

“Ah, yes. This product was manufactured using an F-rank Magic Gem…”

Kim Seonhee quickly pulled herself together and began her explanation. The customer had picked up a dagger with a black-painted blade.

Compared to the other weapons, it was nothing special. It did not even have magic embedded in it. It was just an ordinary consumable.

“How much is it?”

“It’s currently on sale as part of our summer promotion, so we’re offering it at the reasonable price of 520,000 won.”

“Hmm. That’s expensive.”

“…”

What was the annual salary of a C-rank Hunter again? Didn’t their basic allowances alone amount to several hundred million won? Kim Seonhee found it ridiculous, but silently waited for the customer to make his choice.

“Ah, well, I guess it can’t be helped. I’ll buy it. Give me one.”

“…Yes.”

The look on his face, as if parting with the money were killing him, was utterly obnoxious. Kim Seonhee was silently cursing him to herself as she picked up the dagger when—

“No. Not that one.”

“Excuse me?”

“The one next to it.”

Her gaze shifted to the side. One hundred daggers were neatly arranged inside a storage box.

“They’re the same product, sir.”

“I know. Give me one of those.”

“…Are you referring to that storage box?”

“Yes. Give me one box of those. And one box of that, too. And that one…”

That was the moment Assistant Manager Kim Seonhee’s worries about her sales numbers disappeared.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 93`.

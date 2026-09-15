# Master Edit Task — Chapter 78

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
| 최민우    | **Choi Minwoo**   |
| 선배     | **Senior**                                   |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 대사      | **Master** for a senior Buddhist monk                           |
| 임꺽정 | **Im Kkeokjeong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 70–74

## Plot

Jin Taekyung endures Jin Mukyung’s brutal training, repeatedly losing consciousness but steadily demonstrating exceptional spear instincts and rapid growth. Mukyung teaches him through real combat, exposing Taekyung’s reliance on luck and forcing him to develop caution, physical conditioning, and the ability to read an opponent’s intent. After ten days, Taekyung masters the Jin Family’s Spear Technique and Manoeuvre Technique, earns the Martial Arts Manual Creation Skill, gains substantial Stats and Levels, and receives Mukyung’s recognition. The Training? Trial! Quest is completed, placing its Reward in his Inventory and promising an additional Reward.

Jin Wikyung assigns the brothers to visit the Mount Heng Sword Sect at the request of its new Sect Leader, Lee Seowol. The System forcibly creates the First Rate Quest [Yesterday’s Enemy, Today’s Ally], requiring Taekyung to deliver the Jin Family’s New Year’s Day invitation to the sect. Mukyung accepts because Seowol may reveal some of Mount Heng’s Peak martial arts. Taekyung, Mukyung, and the injured Hyuk Mujin depart for Eung-hyeon in a four-horse carriage, while Taekyung prepares to log out during the journey.

## Continuity

- Taekyung has mastered the Jin Family’s Spear Technique and Manoeuvre Technique and possesses First Stage Martial Arts Manual Creation, currently usable for those two arts.
- Mukyung’s final spar ended with Sword Energy cutting Taekyung’s uniform without injuring him; Mukyung recognized Taekyung’s progress and declared training complete.
- The Training? Trial! Quest succeeded. Taekyung received a Level Up, has its completion Reward in his Inventory, and was notified of an additional Reward.
- Lee Seowol is the new female Sect Leader of the Mount Heng Sword Sect, Lee Cheonbaek’s third child, and the younger sister of the deceased Young Sect Leader and Lee Seogeun.
- [Yesterday’s Enemy, Today’s Ally] remains incomplete. Its objective is to deliver Jin Wikyung’s invitation for the coming New Year’s Day; its Reward is unknown and its Failure penalty is None.
- Taekyung, Mukyung, and Hyuk Mujin are traveling to Eung-hyeon, expected to arrive in approximately three days. The regular attendants and coachman were dismissed, and Mujin remains because he obeys Taekyung as squad leader.
- Hyuk Mujin is still badly injured and under treatment. The assassin’s identity and sponsor remain unknown, as does any connection to Song Sword Sect.
- Jin Wikyung still intends to summon Shanxi’s sects on New Year’s Day and may seek the Alliance Leader position.
- Taekyung’s prior relationship with Lee Seowol and the missing details of his memories remain unclear. Whether he can complete the new Quest and successfully log out is unresolved.

## Translation Decisions

- Retain established terminology: **First Rate**, **Peak**, **Sword Energy**, **Martial Arts Manual Creation**, **Quest**, **Reward**, **New Year’s Day**, **Alliance Leader**, **Hyung-nim**, **four-horse carriage**, and **Eung-hyeon**.
- Render [昨日之敵 今日之友]’s Quest title as **[Yesterday’s Enemy, Today’s Ally]**.

### Prior accepted reading-copy tails

#### Chapter 76 tail (verified mastered)

…
think? Are you asking because you don’t know?* I barely swallowed the words that had risen to my throat before managing to speak. “You said we’d arrived?” “Yes, we have.” I whipped my head toward Butler Kim. “Butler Kim, is this the place?” “It is.” Butler Kim nodded without hesitation, then added, “However, I believe you’re looking in the wrong direction.” “The wrong direction?” “Yes. If you turn your head a little to the right from where you’re standing, you should see it.” I turned as instructed. After a brief silence, I asked, “What is that run-down building?” Standing alone amid the luxurious skyscrapers, it looked especially small and dilapidated. Butler Kim kindly explained. “Strictly speaking, it’s a supermarket.” “More precisely, it looks like a corner store.” I narrowed my eyes and glared at the collapsing store. The yellowed sign read: **Sooni’s Super** “Who’s Sooni? What a tacky name.” “She’s an old woman who’s lived here for seventy years.” “Now that I think about it, it’s quite elegant. Sounds like a name that promises a long life.” “She passed away two months ago.” “Ah.” *Why is this happening to me?* “She was incredibly stubborn, so during the redevelopment of the Gate-dense area, she refused no matter how much money they offered. By then, the other Guilds had already established themselves… In the end, we purchased the property from her surviving family.” “So that Sooni’s Super is our Guild house?” “Precisely.” I stared at the half-collapsed Sooni’s Super with mixed feelings. A Guild house was the face of a Guild. Its signboard. No matter how expensive the land in this neighborhood was, they had really chosen a place like that…… *No, wait. For a newly established Guild, this is incredible.* It was only that my expectations had been too high. In an industry crawling with scams, Team Leader Choi had shown me enough sincerity that I could trust him and follow his lead. “Team Leader Choi.” “Yes, Taekyung?” I grabbed his hand. “I’ll work really hard. I don’t care whether our Guild house is Sooni’s Super or Sooni’s Building.” Team Leader Choi answered with an awkward expression. “I’m glad you understand.” “You know what they say. Though the beginning is humble, its end will be magnificent!” “It’s already fairly magnificent. Butler Kim, how much did it cost to purchase that lot?” Butler Kim answered, “A little over two billion won per pyeong.[^1]” “……Two billion won per pyeong?” “Yes.” After a brief silence, I spoke. “I believe the beginning is magnificent, but the end will be even more magnificent.” “……” “……” Team Leader Choi and Butler Kim’s gazes pierced me like arrows. Just as they stared at me with expressions that seemed to ask, *What kind of asshole is this?* a sound rang out. Screeeech. Crash! **Sooni’s Super** The sign, whose decades-old lettering had been neatly written in Hancom Batang, slammed into the ground. “……It’ll look fine once we remodel.” Team Leader Choi muttered in a tiny voice. Then the store door opened, and someone stepped out. “Oh dear, it fell again.” Grumbling, the monstrously strong man lifted the fallen sign with one hand. At the appearance of this completely unexpected person, my mouth fell open. “Uncle Kkeokjeong?” The good-natured, middle-aged E-rank Hunter Im Kkeokjeong spotted us and waved with a bright smile. “Hey, Taekyung!” *What the hell? How did this happen?* While I stood there dumbfounded, Im Kkeokjeong approached and patted me on the shoulder. “You little punk. Been doing well? I heard you made C-rank.” “No, why are you here?” “Hahaha! Why am I here? Is there something wrong with a Guild member being at the Guild house?” After letting out a hearty laugh, he continued. “I was stuck lying in the hospital when Team Leader Choi suddenly came to see me and asked if I wanted to join the Guild. I said yes without a second thought.” Team Leader Choi, who had been looking sadly at the fallen sign, added, “He seemed like someone I could trust.” “That young man knows what loyalty means. Mr. Kim over there doesn’t say much, but he’s a really good man. And Miss Song goes without saying.” “No, wait. Hold on.” What was going on here? I asked as calmly as I could, “You joined recently?” “Yeah.” Team Leader Choi cut in again. “He seemed like someone I could trust.” “That young man knows what loyalty means. Mr. Kim over there doesn’t say much, but…” “I heard that part already. What about the others?” “Huh?” “Where are the other Guild members? Surely these four aren’t everyone.” “Of course not.” Im Kkeokjeong answered firmly, then added, “Miss Song went grocery shopping. She said she’d throw you a welcome party.” “Miss Song? Don’t tell me she’s the last one.” “Yeah. Including Miss Song, there are five of us. She left over an hour ago, so she should be back soon.” I couldn’t hear anything after that. *Five people.* *Is this a dream?* Im Kkeokjeong’s booming voice snapped me out of my daze as I stared blankly at the collapsing Sooni’s Super. “Oh, there she is. Miss Song! Over here, over here! The newbie’s here!” I followed his gaze and turned my head. The final Guild member of the ultra-tiny Guild, and one of its founding members. *She* was there. [^1]: A pyeong is a traditional Korean unit of area equal to approximately 3.3 square meters.

#### Chapter 77 tail (verified mastered)

…
mouth. Fireworks start going off in your head!” I added one more point in a dignified tone. “I'm a Taurus.” “That’s right! A Taurus man grills meat well, and he’s pure-hearted, honest, and so steadfast…” Crack. Team Leader Choi set down the broken wooden chopsticks and muttered, “I'm sorry. I couldn't control my strength.” “Here.” As if she had been waiting for that moment, Song Song handed him a fresh pair of chopsticks. My heart sank. I hated to admit it, but the beautiful woman and the handsome man looked perfect together. *No way. It can’t be.* I tried to deny it, but my heart felt heavy. With a gloomy expression, I placed the meat on the grill. Sizzle. What kind of relationship did Song Song have with Team Leader Choi? Sizzle. It was obvious they had known each other for a long time. She wouldn’t be a founding member of the Guild otherwise. Sizzle. Come to think of it, that bastard Team Leader Choi was suspicious. He’d been interrupting our conversation from the start. And why had he snapped a perfectly good pair of chopsticks and ruined the mood? Sizzle. A B-rank Hunter claiming he couldn’t control his strength? What kind of bullshit excuse was that? Was he showing off how strong he was in front of Song Song? I could tie metal chopsticks into a knot too… “Excuse me.” I looked up with a start. Eyes as clear as a lake were staring straight at me. “It’s burning.” “Yes, yes?” “The meat. It’s burning.” “Gasp!” Sizzle-sizzle-sizzle. I hurriedly flipped the meat, but it was already too late. “I’ll do it.” “No. I will.” “Come to think of it, since you're here for the first time today, it's only right that I grill the meat and serve you.” My God. She wasn’t just an angel on the outside. *Oh, Miss Song. You’re an ethics textbook.*[^2] [^2]: Taekyung substitutes “ethics textbook” into a Korean phrase meaning “what on earth are you?” I fell for her nature, gentle as silk, all over again. Slice. Slice. Sizzle. After taking the tongs from me, she grilled and cut the meat with practiced skill. I watched her in a daze. *She even looks beautiful grilling meat.* Her hair was loosely twisted into a bun, and her slender, pale hands moved busily. Every movement seemed to shine. “Hmm.” How much time had passed? She had been watching the meat carefully when she spoke. “It’s done. Could you hand me a plate?” “Yes, ma’am.” She neatly placed the fully cooked meat into a disposable container. I had noticed it earlier, but this was clearly not something she had done only once or twice. “You must’ve done this a lot.” “Yes.” “Did you work part-time at a barbecue restaurant?” “Yes.” “Wow. For how long?” “Two years.” “Wow, when?” “When I was in high school.” “Huh. Not many kids had part-time jobs back then.” “Oh, yes.” *What am I going to do? Even her resourcefulness is exactly my type.* Her answers seemed strangely short, but that had to be my imagination. I kept showering her with enthusiastic little responses to keep the conversation going. *The conversation itself is going smoothly.* Jinho hyung had said that if you wanted someone to like you, you had to start by finding common ground. I launched into my story with enthusiasm. “We're pretty similar. I used to work two or even three shifts in a day. One day, after I finished work and came home…” “Oh, yes. But, um…” “Yes?” “You seem a little close. The grill is still hot…” Without realizing it, I had leaned my entire body toward Song Song. “It's fine. I'll just get a little burned. Hahaha!” “You should still be careful.” “I’m really fine. You don’t have to worry.” “……” Song Song’s expression seemed strangely dark. *Could it be…?* *Is she worried I might get hurt?* I was stunned. She was thinking about me this much even though we had only met today. And then I knew for certain. She was interested in me, too. Jinho hyung’s voice reached me from somewhere, like an auditory hallucination. *Do you know what the most important virtue is when it comes to becoming a couple? Courage.* *Taekyung, remember this. A man with courage wins the beauty.* *Hyung, I think I finally understand. And thank you.* *That's right. Let's be brave.* I stared at her, my heart trembling. What I was about to say was something I had never once said in all twenty-seven years of my life. “Miss Song. Starting today, you and I are on day one…” At that moment, Team Leader Choi shot to his feet and shouted. “Day one! Today is Hunter Jin Taekyung’s first day as a member of our Guild family! Butler Kim?” “Yes, Young Master! The soju is ready!” The usually unhurried Butler Kim filled the shot glasses at lightning speed. Glug-glug-glug! Not a gentle trickle—it was pouring full blast. Half of it spilled, and the other half was poured in with brute force. The sight left me speechless, but there was something I absolutely had to say. “Miss Song. Let me say it again. You and I…” Team Leader Choi raised his glass high. “To our Guild!” “Miss Song. Ignore them and listen to me.” Song Song answered. “To our Guild!” “……” She didn’t hear me, right? Yeah. She couldn’t have heard me.

## Korean source

```text
＃78화



헌터들은 하나같이 술고래다.

최하급인 F급 헌터라고 해도 일반인을 훌쩍 뛰어넘는 신체 능력과 신진대사의 소유자들이니까.

술을 안 먹는 헌터는 있어도 못 먹는 헌터는 없다는 말이 괜히 있는 게 아니다.

“히끅. 한 잔 더.”

그런데 여기 한 명 있었네.

어느새 반쯤 눈이 풀린 송이 씨가 맹렬하게 빈 잔을 흔들었다.

“한 잔 더어!”

취한 모습도 예뻐……가 아니고. 이 정도면 살짝 위험한 거 아닌가? 나는 걱정스러운 눈빛으로 송이 씨를 바라봤다.

‘너무 급하게 마신 것 같은데.’

본격적으로 술자리가 시작되자마자 소주 한 병을 나발로 불더니 쭉 저 상태다. 가끔은 혀 꼬인 발음으로 눈치도 더럽게 없다느니, 재수 옴 붙었다느니 하는 뜻 모를 소리를 중얼거리기도 했다.

‘안 좋은 일이라도 있는 건가?’

임꺽정이 그녀의 술잔을 채워 주는 틈을 타 최 팀장에게 소곤거렸다.

“팀장님. 송이 씨 무슨 일 있었어요?”

최 팀장이 떨떠름한 얼굴로 대답했다.

“……있긴 있죠.”

“역시.”

“그것도 아주 최근에.”

“앗. 아아.”

송이 씨의 불행은 곧 나의 불행. 지켜보고만 있자니 억장이 무너진다.

“후우. 잘 해결됐으면 좋겠네요.”

“…….”

“…….”

최 팀장은 물론이고 옆에 앉아 있던 김 집사까지 괴상한 표정으로 나를 바라본다.

이거 왠지 기분이 이상해지는데.

“왜요?”

“아닙니다.”

“젊을 때는 그럴 수도 있죠.”

어째 미적지근한 대답이지만 지금 그게 중요한 게 아니다.

까드득.

“마셔요! 오늘 마시고 죽어!”

세 병째 소주를 깐 송이 씨가 미쳐 날뛰고 있었으니까.

“으하하! 난 이래서 송이 씨가 참 좋더라!”

물 만난 고기. 아니, 술 만난 산적처럼 옆에서 거드는 임꺽정은 덤이다.

“말려야 되는 거 아니에요?”

“아, 송이 씨요?”

“네.”

최 팀장이 어깨를 으쓱했다.

“괜찮습니다. 하루 이틀 본 것도 아니고. 송이 씨 술버릇이 원래 저래요.”

“아무리 그래도…… 아니 잠깐만.”

나는 최 팀장을 지그시 노려봤다.

아까부터 수상하다 싶었는데, 이제야 덜미를 잡았다.

“팀장님이 송이 씨 술버릇을 어떻게 압니까?”

“같이 술을 마셨으니까 알죠.”

“…….”

이 자식이 누굴 놀리나. 내가 그걸 몰라서 물어본 것 같니?

“그 얘기가 아니잖아요.”

“그럼 어떤 얘깁니까?”

“그러니까…….”

막상 이렇게 나오니까 할 말이 없다. 생각해 보면 내가 뭐라고 두 사람 관계를 따진단 말인가?

순간 말문이 막힌 그때, 최 팀장이 불쑥 입을 열었다.

“아레스. 들어 보셨죠?”

“당연하죠.”

전신(戰神) 아레스.

고대 그리스 로마 신화에 등장하는 신의 이름이다. 지금에 이르러서는 다른 의미로 유명해졌지만.

“아레스 길드 모르는 사람이 어디 있어요?”

대한민국 헌터의 자존심이자 자부심.

국내에는 수백 개의 길드가 존재하지만 정점은 오직 하나, 아레스 길드였다. 대격변 초기부터 지금까지 그들이 이룩한 위업은 셀 수 없이 많다.

‘말 그대로 전설이지, 전설.’

학습 만화, 교육 애니메이션, 영화와 소설 등등. 심지어는 교과서에도 나온다.

아레스 길드가 국내에서 차지하는 위치는 살아 있는 세종대왕이요, 현역 이순신 장군에 버금간다. 아니, 그 이상일 것이다.

‘세계적으로 워낙 유명하니까.’

두 유노 킹 세종? 킹 갓 제너럴 순신 리? 하고 물어보면 대다수의 외국인들은 이 동양인 새끼가 뭐라는 거야, 하겠지만 아레스 길드는 다르다.

- 두 유노 아레스?

- 오, 예쓰!

터프하기 짝이 없는 텍사스 할아버지도 쌍권총을 탁 치며 알아듣는다는 게 학계 정설이다.

“그런데 아레스 길드는 왜요?”

맥주 한 모금을 삼킨 최 팀장이 대답했다.

“제가 거기 있었거든요.”

“아. 그렇구나…… 예?”

내가 지금 무슨 말을 들은 거지?

말문이 막혀 한동안 눈만 껌뻑이다가 입을 열었다.

“아레스 길드 소속이셨다고요?”

“팀장이었습니다. 그래 봤자 한참 말단이지만.”

아레스 길드의 문턱은 높다. 최고만 가려서 뽑고, 최고로 길러 낸다. 최 팀장은 스스로를 한참 말단이라고 했지만 이미 거기서 팀장을 달았다는 것부터가 대단한 거다.

지금 내 눈에는 그냥 미친놈처럼 보이지만.

“아니, 거길 왜 나왔어요?”

돈, 명예, 지위.

헌터라면, 남자라면 바라마지 않는 최고의 직장이다. 그걸 걷어차고 나오다니!

“혹시 사내 왕따, 뭐 그런 거 당했어요?”

곰곰이 생각하던 최 팀장이 대답했다.

“그랬을 수도 있겠네요. 절 편하게 대해 주는 사람은 송이 씨밖에 없었으니까.”

“……그럼 송이 씨도 아레스 길드?”

“제 팀원이었습니다. 팀 회식 때 술버릇을 알게 됐죠.”

침이 목울대를 타고 꿀꺽 넘어간다.

‘이거 완전 엘리트들이잖아.’

맥주를 홀짝이는 최 팀장과 병나발을 불고 있는 송이 씨를 번갈아 보던 내 시선이 한 사람에게 멈췄다.

“혹시 김 집사님께서도……?”

“저 말입니까?”

김 집사가 인자하게 웃으며 손을 내저었다.

“전 이미 오래전에 은퇴했습니다. 허허허.”

“네?”

그럼 전직 헌터란 소린데.

문득 김 집사를 대할 때마다 느꼈던 이질감이 떠올랐다. 지금까지 단 한 번도 그를 [기감]으로 파악해 보지 않았다는 사실도.

‘이 사람, 정체가 뭐지?’

기감을 끌어 올리려던 그때.

우리가 이야기를 나누건 말건 열심히 술과 고기를 흡입하던 임꺽정이 말했다.

“어, 버너 불 꺼졌다. 송 양. 가스 새 거 없어?”

“히끅. 그게 마지막이었는데요.”

“에이, 흐름 끊기면 안 되는데. 그냥 먹을까?”

한참 설익은 고기를 뒤집으며 투덜거리는 임꺽정을 향해, 김 집사가 부드럽게 웃어 보였다.

“그럼 안 되죠.”

그리고 다음 순간, 두 가지 일이 동시에 일어났다.

딱!

김 집사가 손가락을 튕겼고.

화아아악!

후끈한 열기가 뿜어져 나왔다. 정확히 불판 위로 솟구친 푸른 불꽃은 순식간에 판을 달구고 고기를 익힌 뒤 사라졌다.

“이건…….”

나와 임꺽정은 누가 먼저랄 것도 없이 외쳤다.

“마법사!”

“엄청 잘 구웠어!”

“…….”

“왜? 태경이 너도 빨리 먹어.”

됐네, 이 양반아. 나는 고개를 절레절레 저었다.

그보다 김 집사가 마법사였을 줄이야. 어쩐지 느낌이 이상하더라니.

“깜빡 속았네요.”

김 집사가 잘 익은 고기를 한 점 집어 올렸다.

“속일 생각은 없었습니다. 저야 말씀드렸다시피 이미 은퇴한 퇴물이니까요.”

퇴물은 무슨. 김 집사가 퇴물이면 지금 현역으로 활동하는 마법사 중에 절반은 대가리 박아야 한다.

‘최소 B급 이상.’

손가락 한 번 튕기는 것만으로도 불꽃을 불러내고 고기를 태우지도, 덜 익히지도 않고 알맞게 구울 만큼 컨트롤 역시 정교하다. 정황을 미루어 볼 때 은퇴 전에는 그 역시 아레스 길드 소속이었을 것이다.

만약 대격변 때도 활동한 인물이라면.

‘……이거 거물인데?’

거기에 더해 까마득한 대선배다.

나는 조심스럽게 물었다.

“저어, 혹시 헌터 훈련소는 어디 나오셨는지.”

“논산 나왔습니다. 태경 씨는요?”

“헉. 저도 논산입니다. 28연대 1대대.”

“그래요? 이거 우연이네요. 나도 28연대 1대대 나왔는데. 몇 중대 출신이에요?”

“2중댑니다.”

“우연이 아니라 인연인가 보네요. 하하.”

두말할 필요가 없다. 자리에서 일어난 나는 허리를 꺾었다.

“반갑습니다, 선배님.”

대한민국은 학연, 지연, 혈연이라는 말이 있다. 헌터도 마찬가지다.

각성 확률은 0.1퍼센트. 천 명당 하나꼴이고 이런 희박한 확률 때문에 사회에서 알던 지인이 각성하는 경우는 드물다. 별것 아닌 것처럼 보이는 헌터 훈련소가 인맥의 시작점인 셈이다.

“뭘 또 이렇게까지. 앉으세요.”

“말씀 편하게 하셔도 됩니다.”

“저는 그런 거 안 따지니까…….”

나와 김 집사가 선후배 간의 훈훈한 분위기를 연출하고 있던 그때, 가만히 지켜보던 최 팀장이 불쑥 끼어들었다.

“김 집사님. 진태경 씨 말대로 하는 게 어떻겠습니까?”

이런 버르장머리 없는 놈을 봤나. 감히 대선배님께 이래라저래라…….

‘으음. 할 수 있지.’

생각해 보면 최 팀장이 더 거물이다. 아레스 길드 출신 마법사를 집사로 쓰는 놈이니까.

‘도대체 어떤 집안이길래.’

할아버지가 대통령이고 아버지가 국무총리쯤 되나?

궁금증만 더해 갈 때 최 팀장의 말이 이어졌다.

“이쯤에서 호칭 정리를 해야겠죠. 명색이 우리 길드의 얼굴이신데 언제까지 집사님이나 아저씨라고 부를 수는 없는 것 아닙니까?”

잠시 고민하던 김 집사가 대답했다.

“도련님 말씀에 따르겠습니다.”

고개를 끄덕인 최 팀장이 준엄한 눈빛으로 좌중을 쓸어 보았다.

“그럼 앞으로 김 집사님에 대한 호칭은 길드장님으로 통일합니다. 이의 없으시죠?”

임꺽정과 송이 씨가 대답했다.

“크, 고기 맛 죽이네. 마법으로 구워서 그런가?”

“술이 들어간다. 술! 술술, 술술!”

“…….”

회한 어린 눈빛으로 두 사람을 응시한 최 팀장이 내게 시선을 돌렸다. 나는 보란 듯이 한쪽 팔을 들고 있었다.

“그건 무슨 뜻입니까?”

“질문드릴 게 있어서요.”

그나마 이놈은 좀 낫군. 최 팀장이 그런 얼굴로 말했다.

“말씀하세요.”

“최 팀장님이 길드장 아니었습니까?”

“…….”

배신당한 듯한 표정을 지은 최 팀장이 품에서 뭔가를 꺼내 건넸다. 받아 살펴보니 명함이다.

“저 이거 있는데요.”

“뭐라고 적혀 있습니까?”

“평화 길드 1팀장 최민우요.”

“네. 저 팀장입니다.”

“아.”

“김 집사님이 길드장. 제가 팀장. 나머지 세 분이 팀원입니다. 이제 이해되셨습니까?”

김 집사가 바지 사장인지, 얼굴마담인지는 모르겠지만 일단 고개를 끄덕였다. 그렇게 안 하면 최 팀장이 울 것 같아서.

“다른 분들도 알아들으셨습니까?”

최 팀장의 질문에 임꺽정과 송이 씨가 대답했다.

“이야, 술맛도 죽이네. 마법으로 구운 고기가 안주라 그런가?”

“언제까지 어깨춤을 추게 할 거야. 탈골됐잖아. 탈골! 탈골!”

“…….”

야, 우냐?
```

## Current accepted English baseline

```markdown
# Chapter 78

Every Hunter is a heavy drinker.

Even an F-rank Hunter, the lowest classification, possesses physical abilities and a metabolism far beyond those of an ordinary person.

There is a reason people say that while some Hunters do not drink, there are none who cannot.

“Hic. One more glass.”

Well, there was one here.

Miss Song’s eyes had already gone half-glazed as she furiously shook her empty glass.

“One more glaaass!”

*She’s pretty even when she’s drunk… No, that’s not the point. Isn’t this getting a little dangerous?*

I looked at Miss Song with concern.

*She must have drunk too quickly.*

The moment the drinking party had begun in earnest, she had chugged an entire bottle of soju straight from the bottle and had been like this ever since. Every now and then, she slurred incomprehensible things about someone having no damn tact and rotten luck clinging like a curse.

*Is something bad going on?*

While Im Kkeokjeong was filling her glass, I leaned toward Team Leader Choi and whispered.

“Team Leader. Did something happen to Miss Song?”

Team Leader Choi answered with an awkward expression.

“……Something did happen.”

“I knew it.”

“Something that happened very recently, too.”

“Oh. Ah.”

Miss Song’s misfortune was my misfortune. Just sitting there and watching her was breaking my heart.

“Whew. I hope things work out for her.”

“……”

“……”

Team Leader Choi, along with Butler Kim, who was sitting beside him, stared at me with strange expressions.

This was starting to feel weird.

“What?”

“Nothing.”

“People can be like that when they’re young.”

It was a lukewarm answer, but that was not important right now.

Crack.

“Drink! Drink until you drop dead today!”

Miss Song had opened her third bottle of soju and was going wild.

“Ha-ha-ha! This is why I really like Miss Song!”

Like a fish in water—no, like a bandit who’d found booze—Im Kkeokjeong egged her on from beside her.

“Shouldn’t we stop her?”

“Ah, Miss Song?”

“Yes.”

Team Leader Choi shrugged.

“It’s fine. It’s not like I’ve only known her for a day or two. That’s just how Miss Song gets when she drinks.”

“Even so… No, wait a second.”

I stared intently at Team Leader Choi.

I had thought he was suspicious for a while, but now I had finally caught him.

“How do you know what Miss Song is like when she drinks?”

“Because I’ve drunk with her.”

“……”

Was this bastard making fun of me? Did he think I was asking because I didn’t understand that?

“That’s not what I mean.”

“Then what do you mean?”

“I mean…”

Now that he had put it that way, I had nothing to say. When I thought about it, who was I to question the relationship between the two of them?

Just as I was rendered speechless, Team Leader Choi suddenly opened his mouth.

“You’ve heard of Ares, right?”

“Of course.”

Ares, the god of war.

The name of a god who appeared in ancient Greek and Roman mythology. These days, though, it was famous for something else.

“Who in Korea doesn’t know the Ares Guild?”

The pride and joy of Korea’s Hunters.

Hundreds of Guilds existed in Korea, but only one stood at the top: the Ares Guild. The achievements they had made from the early days of the Great Cataclysm to the present were too numerous to count.

*They’re legends. Plain and simple.*

They appeared in educational comics, educational animations, movies, novels, and all kinds of other media. They had even made it into textbooks.

The Ares Guild held a position in Korea comparable to a living King Sejong or an active General Yi Sun-sin. No, perhaps even higher.

*They’re famous all over the world, after all.*

If you asked most foreigners, *Do you know King Sejong? King-God-General Yi Sun-sin?* they would probably respond, *What the hell is this Asian guy talking about?* But the Ares Guild was different.

*Do you know Ares?*

*Oh, yeah!*

Even a tough-as-nails Texas grandpa would tap his twin pistols and understand. That was the accepted truth among scholars.

“Why are you asking about the Ares Guild?”

Team Leader Choi swallowed a mouthful of beer before answering.

“Because I used to be there.”

“Oh. I see… Huh?”

What had I just heard?

I blinked for a while before finally speaking.

“You used to belong to the Ares Guild?”

“I was a Team Leader. Though I was still pretty low-ranking.”

The Ares Guild had high standards. They selected only the best and trained them to become even better. Team Leader Choi had called himself a low-ranking member, but the fact that he had become a Team Leader there was already incredible.

Though at the moment, he just looked like a lunatic to me.

“Then why did you leave?”

Money, honor, and status.

It was the best job any Hunter—or any man—could dream of. And he had kicked it all away and left!

“Were you ostracized at work or something?”

Team Leader Choi thought about it for a moment before answering.

“That might have been the case. Miss Song was the only person who treated me normally.”

“……Then was Miss Song in the Ares Guild too?”

“She was on my team. I found out about her drinking habits during team dinners.”

I swallowed hard.

*These people are total elites.*

My gaze moved back and forth between Team Leader Choi, who was sipping his beer, and Miss Song, who was drinking straight from the bottle, before stopping on one person.

“Could it be that Butler Kim also…?”

“Me?”

Butler Kim smiled kindly and waved his hand.

“I retired a long time ago. Ha-ha-ha.”

“What?”

So he was a former Hunter.

Suddenly, I remembered the sense of incongruity I had always felt whenever I dealt with Butler Kim. I had also never once tried to assess him with my Qi Sense.

*What is this man’s real identity?*

Just as I was about to raise my Qi Sense, Im Kkeokjeong, who had been enthusiastically inhaling meat and liquor whether or not we were talking, spoke up.

“Oh, the burner went out. Miss Song, do we have another gas canister?”

“Hic. That was the last one.”

“Aw, we can’t let the momentum die. Should we just eat it?”

Im Kkeokjeong grumbled as he flipped a piece of meat that was still mostly raw. Butler Kim smiled gently at him.

“That won’t do.”

The next moment, two things happened at once.

Snap!

Butler Kim snapped his fingers.

Fwoosh!

A wave of scorching heat burst forth. Blue flames shot precisely up over the grill, heating the plate and cooking the meat in an instant before vanishing.

“This is…”

Im Kkeokjeong and I shouted at the same time.

“A mage!”

“It’s cooked incredibly well!”

“……”

“What? Taekyung, hurry up and eat.”

*Forget it, old man.*

I shook my head back and forth.

More importantly, who would have thought Butler Kim was a mage? No wonder something about him had always felt strange.

“You really fooled me.”

Butler Kim picked up a well-cooked piece of meat.

“I had no intention of fooling you. As I told you, I’m already a retired has-been.”

*Has-been, my ass.*

If Butler Kim was a has-been, half the mages still active today ought to bow their damn heads.

*At least B-rank.*

He could summon flames with a single snap of his fingers and control them precisely enough to cook the meat just right without burning or undercooking it. Judging from the circumstances, he had probably belonged to the Ares Guild as well before retiring.

If he had been active during the Great Cataclysm, too…

*……This guy’s a big shot.*

And on top of that, he was an incredibly senior one.

I asked cautiously.

“Um, which Hunter training center did you graduate from?”

“Nonsan.[^1] What about you, Mr. Taekyung?”

“Gasp. Me too. The 28th Regiment, 1st Battalion.”

“Really? What a coincidence. I was in the 28th Regiment, 1st Battalion too. Which company were you in?”

“Second Company.”

“Then it wasn’t a coincidence. I suppose it was fate. Ha-ha.”

There was no need for further discussion. I stood up and bent deeply at the waist.

“Nice to meet you, Senior.”

[^1]: Nonsan is home to Korea’s main Army recruit training center.

There is a saying in Korea about school ties, hometown ties, and blood ties.[^2] Hunters were no different.

The probability of awakening was 0.1 percent—one in a thousand. Because the odds were so slim, it was rare for someone you knew from ordinary society to awaken. The Hunter training center, which might seem like nothing special, was where a Hunter’s network began.

“You don’t have to go that far. Please, sit down.”

“You can speak comfortably with me.”

“I don’t really stand on ceremony…”

Just as Butler Kim and I were creating a warm senior-junior atmosphere, Team Leader Choi suddenly cut in.

“Butler Kim. Why don’t you do as Mr. Jin says?”

*What an ill-mannered bastard. How dare he tell such a senior what to do…*

*Hmm. He can do that.*

Come to think of it, Team Leader Choi was the bigger shot. He employed a mage from the Ares Guild as his butler.

*What kind of family does he come from?*

Was his grandfather the president and his father the prime minister?

As my curiosity continued to grow, Team Leader Choi went on.

“I think it’s time we sorted out everyone’s forms of address. You’re the face of our Guild, after all. We can’t keep calling you Butler Kim or Uncle forever, can we?”

Butler Kim considered it for a moment before answering.

“I’ll follow the Young Master’s wishes.”

Team Leader Choi nodded and swept his stern gaze over everyone present.

“Then from now on, we’ll all address Butler Kim as Guild Master. No objections, correct?”

Im Kkeokjeong and Miss Song answered.

“Man, this meat is incredible. Is it because it was grilled with magic?”

“The booze is going in. Booze! Down it goes, down it goes!”

“……”

Team Leader Choi gazed at the two of them with regret before turning his eyes toward me. I had raised one arm conspicuously.

“What does that mean?”

“I have a question.”

*At least this guy is a little better.*

Team Leader Choi spoke with an expression that seemed to say as much.

“Go ahead.”

“Wasn’t Team Leader Choi the Guild Master?”

“……”

Team Leader Choi wore an expression as if he had been betrayed, then pulled something from inside his coat and handed it to me. I took it and looked at it. It was a business card.

“I have this.”

“What does it say?”

“Choi Minwoo, Team Leader of Team 1, Peace Guild.”

“Yes. I’m the Team Leader.”

“Oh.”

“Butler Kim is the Guild Master. I’m the Team Leader. The other three are team members. Do you understand now?”

I didn’t know whether Butler Kim was a boss in name only or merely a figurehead, but I nodded anyway. If I didn’t, Team Leader Choi looked like he might cry.

“Did everyone else understand?”

At Team Leader Choi’s question, Im Kkeokjeong and Miss Song answered.

“Wow, even the liquor tastes amazing. Is it because we have magically grilled meat for an appetizer?”

“How long are you going to make me do the shoulder dance? It’s dislocated! Dislocated! Dislocated!”

“……”

*Hey, are you crying?*

[^2]: School ties, regional ties, and blood ties are traditionally regarded in Korea as major sources of social connections and influence.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 78`.

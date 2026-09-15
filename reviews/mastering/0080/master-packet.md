# Master Edit Task — Chapter 80

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
| 김화종    | **Kim Hwajong**   |
| 임창수    | **Im Changsoo**   |
| 절정     | **Peak**          |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 아이템              | **Item**                       |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 임꺽정 | **Im Kkeokjeong** |
| 평화 | **Peace Guild** | Guild name. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 아이템창 | **Item Window** | System window displaying an item's details. |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 75–79

## Plot

Taekyung logs out after roughly twenty days in Murim, finding that only 2:05:35 has passed in the modern world. He reunites with Seong Jinho, signs a contract to join Team Leader Choi’s new Peace Guild, and learns that the deal includes a 500 million won signing bonus, a 50 million won monthly salary, a seventy-percent settlement share, housing, and other benefits. The Guild house is Sooni’s Super, a dilapidated corner store in Bucheon.

Taekyung meets the Guild’s other members: Im Kkeokjeong, Song Song, and Butler Kim. He immediately develops feelings for Song Song and awkwardly attempts to confess during the Guild’s first gathering, but Team Leader Choi repeatedly interrupts him by turning the occasion into a membership celebration. The gathering ends with Song Song drunk and the others revealing their backgrounds: Choi formerly led a team in the Ares Guild, Song Song served on that team, and Butler Kim is a retired mage and former Hunter. Choi establishes Butler Kim as Guild Master and himself as Team Leader.

The next morning, the hungover members learn that the Peace Guild must begin working. Choi presents footage of the Bucheon Terminal Guild’s raid against seven B-rank Minotaurs in The Minotaur’s Labyrinth. Although the monsters were defeated, two C-rank Hunters died. Taekyung uses Qi Sense to assess the Peace Guild’s members—Choi Minwoo at Level 75, Kim Hwajong at Level 80, Song Song at Level 64, and Im Hyeokjun at Level 24—and concludes that their first raid will be dangerous.

## Continuity

- Taekyung is a Peace Guild member and has completed the Guild Membership achievement, receiving 10 points.
- His Peace Guild contract provides a 500 million won signing bonus, a fixed monthly salary of 50 million won, a seventy-percent settlement share, housing, a car, and other benefits.
- The Peace Guild has five members: Guild Master Butler Kim, Team Leader Choi, Taekyung, Im Kkeokjeong, and Song Song. Choi leads Team 1; Taekyung, Im, and Song Song are its members.
- Sooni’s Super is the Guild house, located in a dilapidated, Gate-dense district of Bucheon. The property cost slightly more than 2 billion won per pyeong.
- Im Kkeokjeong joined after Choi recruited him while he was hospitalized. He is married and has two children.
- Song Song previously worked under Choi in the Ares Guild. Taekyung is attracted to her, but his interrupted confession leaves her response unclear.
- Butler Kim is a retired mage and former Hunter. He and Taekyung trained at Nonsan’s 28th Regiment, 1st Battalion, but Kim’s former rank and wider background remain unknown.
- The Peace Guild is preparing for its first raid. The Bucheon Terminal Guild’s recent raid against seven B-rank Minotaurs killed two C-rank Hunters despite defeating all the monsters, establishing the danger of the upcoming operation.
- The members’ displayed Levels are Choi Minwoo 75, Kim Hwajong 80, Song Song 64, and Im Hyeokjun 24.
- Essence of the Himalayas temporarily increases Taekyung’s Intelligence by 1 for one hour.
- In Murim, Taekyung, Jin Mukyung, and Hyuk Mujin are traveling to Eung-hyeon to visit the Mount Heng Sword Sect. The forced [Yesterday’s Enemy, Today’s Ally] Quest—to deliver Jin Wikyung’s New Year’s Day invitation—remains unresolved.
- The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed. The possible connection to Song Sword Sect is also unresolved.
- Jin Wikyung still plans to summon Shanxi’s sects on New Year’s Day and may seek the Alliance Leader position. Whether the sects will respond remains unknown.

## Translation Decisions

- Retain **Peace Guild**, **Ares Guild**, **Guild Master**, **Team Leader Choi**, **Butler Kim**, **Song Song**, **Miss Song**, **Im Kkeokjeong**, and **Sooni’s Super**.
- Use **Minotaur**, **Bucheon Terminal Guild**, and **The Minotaur’s Labyrinth**.
- Retain **Qi Sense**, **Essence of the Himalayas**, **Sleep Mode**, **Return**, **Returnee**, **New Year’s Day**, **Alliance Leader**, and **Quest**.
- Use **mage** for 마법사, **Senior** for Taekyung’s deferential address to Butler Kim, and **haejangguk** and **makgeolli** with concise cultural footnotes.
- Retain **pyeong**, with a footnote explaining that it is approximately 3.3 square meters.

### Prior accepted reading-copy tails

#### Chapter 78 tail (verified mastered)

…
up. “Oh, the burner went out. Miss Song, do we have another gas canister?” “Hic. That was the last one.” “Aw, we can’t let the momentum die. Should we just eat it?” Im Kkeokjeong grumbled as he flipped a piece of meat that was still mostly raw. Butler Kim smiled gently at him. “That won’t do.” The next moment, two things happened at once. Snap! Butler Kim snapped his fingers. Fwoosh! A wave of scorching heat burst forth. Blue flames surged precisely up over the grill, heating the plate and cooking the meat in an instant before vanishing. “This is…” Im Kkeokjeong and I shouted at the same time. “A mage!” “It’s cooked incredibly well!” “……” “What? Taekyung, hurry up and eat.” *Forget it, old man.* I shook my head back and forth. More importantly, who would’ve guessed Butler Kim was a mage? No wonder something about him had always felt strange. “You really had me fooled.” Butler Kim picked up a well-cooked piece of meat. “I had no intention of fooling you. As I told you, I’m already a retired has-been.” *Has-been, my ass.* If Butler Kim was a has-been, half the mages still active today ought to bow their damn heads. *At least B-rank.* He could summon flames with a single snap of his fingers and control them precisely enough to cook the meat just right without burning or undercooking it. Judging from the circumstances, he had probably belonged to the Ares Guild as well before retiring. If he had been active during the Great Cataclysm, too… *……This guy’s a big shot.* On top of that, he was an incredibly senior one. I asked cautiously, “Um, which Hunter training center did you graduate from?” “Nonsan.[^1] What about you, Mr. Taekyung?” “Gasp. Me too. The 28th Regiment, 1st Battalion.” “Really? What a coincidence. I was in the 28th Regiment, 1st Battalion too. Which company were you in?” “Second Company.” “Then perhaps it isn’t a coincidence but fate. Ha-ha.” There was nothing more to discuss. I rose from my seat and bowed deeply at the waist. “Nice to meet you, Senior.” [^1]: Nonsan is home to Korea’s main Army recruit training center. There’s a saying in Korea about school ties, regional ties, and blood ties.[^2] Hunters were no different. The chance of awakening was 0.1 percent—one in a thousand. With odds that slim, it was rare for anyone you knew from ordinary life to awaken. The Hunter training center might not seem like much, but it was where a Hunter’s network began. “You don’t have to go this far. Please, sit down.” “You can speak casually with me.” “I don’t really stand on ceremony…” Just as Butler Kim and I were creating a warm atmosphere between Senior and junior, Team Leader Choi, who had been watching quietly, suddenly cut in. “Butler Kim. Why don’t you do as Mr. Jin Taekyung says?” *What an ill-mannered bastard. How dare he tell such a distinguished Senior what to do…* *Hmm. I guess he can.* Come to think of it, Team Leader Choi was the bigger shot. He employed a former Ares Guild mage as his butler. *What kind of family does he come from?* Was his grandfather the president and his father the prime minister? As my curiosity continued to grow, Team Leader Choi went on. “I think it’s time we sorted out everyone’s forms of address. You’re the face of our Guild, after all. We can’t keep calling you Butler Kim or Uncle forever, can we?” Butler Kim considered it for a moment before answering. “I’ll follow the Young Master’s wishes.” Team Leader Choi nodded and swept a stern gaze over everyone present. “Then from now on, we’ll all address Butler Kim as Guild Master. No objections, correct?” Im Kkeokjeong and Miss Song answered. “Man, this meat is incredible. Is it because it was grilled with magic?” “The booze is going in. Booze! Down it goes, down it goes!” “……” Team Leader Choi gazed at the two of them with regret before turning his eyes toward me. I had raised one arm conspicuously. “What does that mean?” “I have a question.” *At least this guy is a little better.* Team Leader Choi spoke with an expression that seemed to say as much. “Go ahead.” “Wasn’t Team Leader Choi the Guild Master?” “……” Looking as if he had been betrayed, Team Leader Choi pulled something from inside his coat and handed it to me. I took it and examined it. It was a business card. “I have this.” “What does it say?” “Choi Minwoo, Team Leader of Team 1, Peace Guild.” “Yes. I’m the Team Leader.” “Oh.” “Butler Kim is the Guild Master. I’m the Team Leader. The other three are team members. Do you understand now?” I didn’t know whether Butler Kim was a boss in name only or a public figurehead, but I nodded anyway. If I didn’t, Team Leader Choi looked like he might cry. “Did everyone else understand?” At Team Leader Choi’s question, Im Kkeokjeong and Miss Song answered. “Wow, even the liquor tastes amazing. Is it because we’ve got magically grilled meat to go with it?” “How long are you going to make me do the shoulder dance? It’s dislocated! Dislocated! Dislocated!” “……” *Hey, are you crying?* [^2]: School ties, regional ties, and blood ties are traditionally regarded in Korea as major sources of social connections and influence.

#### Chapter 79 tail (verified mastered)

…
its elegant design and outstanding performance, it’s sold exclusively to a select number of VIPs……” “Just give me the conclusion.” “I loaded some raid footage onto it. Watch.” He could’ve just said that from the start. Im Kkeokjeong and I put our heads together and watched the video stored on the tablet. “All right, stay calm. Stay calm. Especially the tanks! Keep those shields up. If they break through, everyone here is dead. Of course, I’ll kill you myself before that happens.” “Yes, sir!” Around fifteen Hunters formed an orderly formation at the raid leader’s command. Every one of them was visibly tense. *Four tanks, melee and ranged damage dealers. They’ve even got a mage and a healer.* Their teamwork seemed decent, and so did the team composition. And then…… *So that’s a Minotaur.* A B-rank monster I had only ever seen in monster encyclopedias appeared on the screen. “Moooooo!” A cow’s head on a human body. Seven half-human, half-beast Minotaurs advanced toward the intruders. No—they charged. “Mooooooo!” Their bellowing echoed through the cave. Rock dust shook loose and fell in little showers as the battle began. “Ranged! Fire!” The raid leader screamed himself hoarse. At the same moment, around twenty mana-infused arrows struck the lead Minotaur in the head. Fwish-fwish-fwish! Focusing fire on one target instead of using a wide-area attack had been a good choice. Aiming precisely for its head had been especially effective. No matter how strong a B-rank monster was, it couldn’t reinforce its eyeballs. The Minotaur clawed at its own face in agony. The finishing blow came from the companions following behind it. Crunch! A dark iron club smashed the cow’s head apart. And then— Thud, thud, thud! *Huh.* They used the dead Minotaur’s corpse as a shield and charged straight ahead. Arrows and magic rained down, but they only shredded the corpse. The Minotaurs hiding behind it were unharmed. *These bastards……* They knew how to use their heads. They were at least as intelligent as goblins and dozens of times stronger. That made them all the more dangerous. “Hold!” “Urrrgh!” At the team leader’s shout, the tanks’ veins bulged. Their shields, covered in hazy mana, blocked the iron clubs carrying tremendous force. Wham! Wham! Wham! A small shadow suddenly dropped out of the air between them. A stealth-type Hunter drove a black-painted dagger into another Minotaur’s eye, then vanished. “Moooo……” B-rank monsters weren’t invincible. With support from the other melee damage dealers, archers, and mage, two more Minotaurs fell in the blink of an eye. But the crisis came quickly. *They’re breaking through!* No sooner had the thought occurred to me than the wavering tank line collapsed. Kra-koom! “Graaagh!” “Healer! Healer!” Screams and roars filled the cave. Through the billowing dust, I could see the cow-headed monsters tearing through the formation and swinging their iron clubs. “Moooooo!” “Tanks, damage dealers! Ranged, don’t hold back your mana—pour it all in! Ranged, open up some distance!” Wham-wham-wham! “Mooooooo!” “Healeeeer!” The video continued for about ten minutes before cutting off. The battle hadn’t ended yet. The camera had simply been smashed by an iron club. “Mooooooo!” Bzzzt. As the Minotaur’s roar rang out, the screen filled with static and faded to black and white. Im Kkeokjeong swallowed hard. “……This is no joke.” *Of course it isn’t, old man.* I handed the tablet back to Team Leader Choi and asked, “What Guild was that?” “It was footage of the Bucheon Terminal Guild’s raid last week.” “……” *Whoever named that Guild had one hell of a sense for names.* Not that I had much room to talk as a member of the Peace Guild, but at least our name was better than Bucheon Terminal Guild. “What was the result?” “The Minotaurs were wiped out. Two Hunters died.” People dying during raids wasn’t particularly rare. Being a Hunter meant repeatedly drawing close to death, then running away from it. Even so, I couldn’t help feeling heavy-hearted. It was a burden the survivors would have to carry for the rest of their lives. Just as I did now. “I see.” That was all I could manage. I pulled out my smartphone and searched for the incident. Several related articles appeared. > **A Bucheon Guild: The Sacrifice Brought on by a Reckless Raid** > > On the sixteenth, C-rank Hunters identified as Mr. Lee and Mr. Park died in the B-rank Gate *The Minotaur’s Labyrinth*. The Hunter Association authorities…… So the Hunters who died had been C-rank. That made sense. A small-to-medium Guild like that couldn’t possibly have enough talent to fill all fifteen or so spots on a raid team with B-rank Hunters. *Then……* I quickly looked over the Guild members. The Qi Sense I had activated a moment earlier had already brought up their Level windows. Ding. Ding. Ding. > **System** > > **Level 75 — Choi Minwoo** > > **Level 80 — Kim Hwajong** > > **Level 64 — Song Song** The next moment, my eyes met Im Kkeokjeong’s. “What’s wrong?” “It’s nothing.” I answered as casually as I could and turned away, but my thoughts were anything but casual. > **System** > > **Level 24 — Im Hyeokjun** *This raid is dangerous.* [^1]: Haejangguk, literally “hangover soup,” is a Korean soup traditionally eaten after drinking to help ease a hangover. [^2]: Makgeolli is a traditional Korean rice wine with a milky appearance and a mildly sweet, tangy flavor.

## Korean source

```text
＃80화



게이트 관리소.

번쩍거리는 갑옷을 입은 청년이 얼굴을 구겼다.

“그러니까, 왜 안 되냐고.”

B급 게이트인 ‘미노타우로스의 미로’를 담당하는 공무원이 곤란한 기색을 내비쳤다.

“이미 말씀드렸잖습니까. 지난주에 있었던 사망 사고 때문에…….”

“내가 지금 그걸 몰라서 물어? 알 만한 사이에 왜 이렇게 빡빡하게 구냐, 이거지.”

“안전 단속 기간입니다. 인원이 부족하면 저도 허가해 드리기가 곤란해요.”

공무원은 죽을 맛이었다.

사망 사고가 발생한 게이트는 일주일간 안전 단속이 들어온다. 즉, 게이트 입장 인원이나 수준을 높여 사고를 방지하겠다는 건데…… 눈앞의 청년은 막무가내였다.

“평소보다 좀 더 넣었다. 됐지?”

“이게 무슨!”

청년이 불쑥 내민 흰 봉투에 공무원은 화들짝 놀라 주위를 살폈다. 얼마 전에 들어온 신입 하나가 눈을 동그랗게 뜨고 자신을 바라보고 있었다.

“이, 이러시면 안 됩니다.”

“안 되긴 무슨. 지금까지 잘 받아 놓고.”

“…….”

“게이트 담당이 원래 이런 재미지. 맞잖아?”

청년의 노골적인 말에 중년 공무원은 얼굴이 벌겋게 달아올랐다. 그의 말대로 하루 이틀 일은 아니지만 신입 앞에서 이 무슨 개망신이란 말인가.

하지만 어차피 엎질러진 물이다. 두툼한 흰 봉투만큼 공무원의 양심은 얇아졌다.

“……지금 팀 구성이 어떻게 되십니까?”

“나 포함해서 열 명.”

“열 명이요?”

“B급 다섯에 C급 다섯. 왜, 문제 있어?”

당연히 있다. 바로 지난주 있었던 사고의 당사자인 부천터미널 길드는 B급 헌터 다섯에 C급 헌터 열 명이 참여했고, 그들이 어떻게 됐는지는 지역 신문 1면에 대대적으로 실렸으니까.



[허술한 레이드가 불러온 참사]

[부천터미널 길드장, 헌터 협회 조사에 적극적으로 임할 것]



이런 상황에 열 명이라니. 공무원이 갈등하던 그 순간이었다.

“아저씨, 잠깐만.”

방금까지만 해도 험악한 얼굴로 쪼아 대던 청년의 얼굴에 언제부터인지 웃음이 맺혀 있었다.

“어차피 숫자는 얼추 맞춰야 하잖아. 그치?”

“아, 예. 그럼 좋죠.”

“그럼…… 쟤들 끼워서 가자. 모양새 좋게.”

공무원은 청년의 손가락을 따라 고개를 돌렸다. 막 관리소로 들어온 다섯 명의 남녀가 보였다.

‘중년 남자 둘. 젊은 놈 둘. 그리고…….’

끝내주는 미인 하나.

청년의 시선이 떨어지지 못하는 걸로 봐서, 속셈이 뭔지는 안 봐도 뻔했다.

“이제 됐지?”

빠르게 셈을 끝마친 공무원이 봉투를 집어 들었다.

“문제없습니다.”



* * *



중년의 공무원은 친절하게 상황을 설명해 주었다.

지금은 안전 단속 기간이라는 사실과 그로 인해 입장이 지연되는 길드들이 꽤 많다는 것. 현재 우리 인원으로는 용병을 구하든가, 다른 길드와 합류해야 한다는 사실까지.

“운이 좋으시네요. 상동 길드에서 온 분들이 대기 중이신데 딱 다섯 분이 부족하거든요.”

“저희까지 합류하면 게이트 진입까지 얼마나 걸리겠습니까?”

“들어오시면 바로 처리할 수 있습니다.”

그럼 우리야 땡큐지. 실질적인 결정권자인 최 팀장도 별말 없이 고개를 끄덕였다.

“그럼 좋습니다.”

길드장을 맡은 김 집사가 계약서에 서명한 그때, 불쑥 끼어드는 목소리가 있었다.

“반가워요. 상동 길드에서 팀장직을 맡고 있는 임창수라고 합니다.”

유들유들한 목소리와는 다르게 제법 다부진 체격이다.

성큼성큼 걸어오는 그의 모습에서 감출 수 없는 자신감이 흘러나왔다.

‘상동 길드 정도면 그럴 만하지.’

상동 길드는 부천 인근에서 다섯 손가락 안에 드는 중견 길드로, 소속된 B급 헌터만 스무 명이 넘는다.

기껏해야 20대 후반으로 보이는데 직책은 팀장이라니. 고스톱으로 올라갈 수 있는 자리가 아니다.

‘한가락 하는 놈이네.’

뒤이어 끌어 올린 [기감]이 짐작을 확신으로 바꿔 주었다.



[Lv.65 임창수]



그런데 어째 이름이 낯이 익다. 어디서 들어 봤더라?

내가 고개를 갸웃거리는 사이 김 집사가 인사를 건넸다.

“안녕하십니까. 평화 길드의 김화종입니다.”

우리야 김 집사님, 아저씨, 김 형 등등으로 부르고 바지 길드장인 걸 알고 있지만 외부인 시선에서는 딱 봐도 책임자일 거다.

임창수가 환하게 웃으며 응대했다.

“아하, 평화 길드요. 이름은 많이 들었습니다.”

옆에 서 있던 임꺽정과 송이 씨가 소곤거렸다.

“송 양, 우리 길드 만들어진 지 얼마나 됐지?”

“음. 2주 정도 됐을걸요?”

“레이드는? 많이 했어?”

“무슨 말씀이세요. 길드 하우스 리모델링도 시작 안 했는데. 이게 첫 공식 레이드예요.”

“…….”

B급 헌터쯤 되면 아무리 작게 말해도 다 들리는 법이다. 임창수의 고개가 두 사람을 향했다.

“이분들은?”

“우리 길드원들입니다.”

그의 시선이 두 사람을 스쳤다. 임꺽정에게 잠깐, 그리고 송이 씨에게는 좀 더 길게.

“그렇군요. 이거 제가 괜한 말을 해서, 하하.”

“별말씀을요.”

“어찌 됐든 이것도 인연인데, 기왕 한 팀이 됐으니 잘 부탁드립니다.”

“네, 그럼 저희는 장비로 갈아입고 오겠습니다.”

“게이트 앞에서 기다리죠.”

번쩍거리는 사슬 갑주를 쩔그럭거리며 떠나는 임창수의 뒷모습을, 최 팀장이 심각한 얼굴로 응시했다.

“저 사람…….”

“무슨 문제라도 있어요?”

“장비가 한정판이네요. 저거 굉장히 구하기 어려운 건데.”

“…….”

어, 그래. 비싸 보이긴 하더라.



* * *



헌터는 선망받는 직업이다. 대격변으로부터 인류를 지켜 낸 수호자들이라서……인 것도 있겠지만 일단 돈을 많이 벌기 때문이다.

최하급 헌터였던 나도 빡세게 생활해서 연봉 1억 이상은 벌었으니 두말할 것도 없다.

‘문제는 나가는 돈도 많다는 거지만.’

지출 중 가장 큰 비중을 차지하는 것이 바로 장비다.

기본적으로 마정석이 들어가니 아무리 가성비를 따져도 돈이 왕창 깨질 수밖에 없다. 거기에 꾸준한 관리와 파손 시 수리비까지.

가슴이 찢어지는 건 둘째치고 통장 잔고가 찢어진다.

‘장비 관련 보험이 괜히 나온 게 아니지.’

그런 의미에서 최 팀장의 최고의 고용주다.

고급 장비를 무상 대여해 주니까.

돌돌돌.

캐리어를 끌고 탈의실로 들어온 최 팀장이 우리를 불렀다.

“각자 포지션에 맞게 괜찮은 것들로 골라 왔습니다. 하나씩 가져가세요.”

단기 여행용으로나 쓸 법한 조그마한 캐리어다. 임꺽정이 실망한 얼굴로 중얼거렸다.

“내 건 없나 보네.”

최 팀장의 입꼬리가 슬며시 올라갔다.

“그럴 리가요. 이게 뭔지 아시면 깜짝 놀라실…….”

“어, 이거 공간 확장 마법이 걸린 캐리어네.”

“…….”

딱 맞췄군.

내 정확한 예측에 미소가 흐릿해진 것도 잠시. 순식간에 마음을 추스른 최 팀장이 재차 입을 열었다.

“맞습니다. K사에서 제작한 공간 확장 캐리어. 북미 최고의 장인으로 알려진 니콜라스가…….”

덜컹!

“우와, 진짜네! 태경아, 이거 봐라. 안이 엄청 넓어!”

“그러네요.”

“그밖에도 세계 굴지의 디자이너들이 참여…….”

“이야, 이런 건 또 처음 보네. 그냥 여기 들어가서 자도 되겠는데?”

“캐리어 닫으면 누가 열어 주기 전까진 못 나올걸요.”

“그런가?”

“해당 제품은 항상 적절한 온도와 환기를 통해 보관한 물건을 최상의 상태로…….”

철컥, 철컥.

“이거 엄청 멋있네. 어떠냐, 나 잘 어울려?”

“찰떡인데요. 맞춤 정장인 줄.”

“너도 멋있다. 그건 뭐야?”

“흑색 드레이크 가죽 세트라는데요? 아니, 가죽 세트예요.”

“그래? 최 팀장 거니까 좋은 거겠지 뭐. 으하하! 최 팀장 고마워!”

“……별말씀을.”

완전히 전의를 상실한 최 팀장이 힘없이 장비를 갈아입는 사이, 나는 입고 있는 장비들을 하나씩 확인해 나갔다.

‘아이템 확인.’

띠링.



아이템창



[장인의 흑색 드레이크 가죽 세트]

종류 : 갑옷

등급 : 절정

설명 : B급 몬스터 흑색 드레이크의 가죽으로 제작된 갑옷 세트. 훌륭한 장인의 손길이 느껴진다.

효과 : 근력, 체력, 민첩, 맷집 +10

- 풀 세트 효과가 적용 중입니다.





아이템창



[장인의 검은 가시 창]

종류 : 창

등급 : 절정

설명 : B급 몬스터 흑색 드레이크의 척추 뼈로 제작된 창. 매우 단단함과 동시에 날카롭다. 훌륭한 장인의 손길이 느껴진다.

효과 : 적에게 명중 시 90% 확률로 [출혈] 발동





확인 뒤 드는 생각은 딱 하나다.

‘미쳤네.’

착용하는 것만으로도 40포인트가 부여되는 갑옷에, 찌르는 족족 과다 출혈로 사망시킬 수 있는 창까지.

아이템 정보만 봐도 어마어마한 효과라는 걸 알 수 있었다.

‘이런 게 템빨이구나.’

무림에서의 기억을 문득 떠올리니 눈물이 앞을 가린다.

갑옷은 개뿔, 보들보들한 천 쪼가리 걸치고 싸구려 창만 수십 자루는 부러트렸다. 무림인들이야말로 하드보일드의 진수, 진정한 상남자들이 아닐 수 없다.

“명품이라 그런지 느낌부터 확실히 다르네.”

옆을 돌아보니 상기된 표정의 임꺽정이 제자리에서 펄쩍펄쩍 뛰고 있었다.

“무지 가볍고, 몸도 빨라진 것 같고. 기분 탓인가?”

“아닐걸요.”

기분 탓일 리가 있나. D급 헌터인 임꺽정을 위해서 최 팀장이 준비한 장비인데 당연히 좋은 거겠지.

‘살짝 확인해 볼까?’

내가 임꺽정이 입고 있는 풀 플레이트 메일에 손을 올리려던 그때, 어느새 장비를 갖춘 최 팀장이 다가왔다.

“준비되셨으면 출발하시죠.”

“김 집사님은요?”

“밖에서는 길드장님입니다.”

나를 향한 최 팀장의 일침에 김 집사가 허허 웃었다.

“괜찮습니다. 그리고…… 전 항상 장비를 입고 있어서요.”

말과 함께 정장 단추를 푸니 양 손목의 팔찌와 목걸이가 드러났다. 물론 일반적인 장신구가 아니다.

마정석이 박힌 목걸이와 기이하면서도 아름다운 문양이 음각된 팔찌.

“아티팩트(Artefact)?”

“지팡이보다는 이게 더 편하더군요.”

김 집사는 겸손하게 대답했지만 저 정도로 간편한 복장의 마법사는 흔치 않다. 생존율을 높이기 위해 경갑옷이나 호신용 지팡이 하나쯤 들고 있는 게 보통이지.

‘뭐, 보통 마법사는 아니겠지.’

아레스 길드 출신이라고 하면 다들 한 수 접고 들어간다.

문득 김 집사의 과거가 궁금해졌지만 다음 순간 의문은 깨끗이 지워졌다.

똑똑.

“남자분들. 아직 멀었어요?”

“아, 준비 끝났습니다.”

탈의실 밖에서 들려온 송이 씨의 목소리. 최 팀장이 대답하자마자 문이 살며시 열렸다.

“빨리 가요. 사람들 기다릴 텐데.”

“헉.”

질끈 올려 묶은 긴 생머리. 가벼운 가죽 갑옷을 착용한 그녀의 모습에 나는 헛숨을 삼켰다.

‘사람이 이렇게 예뻐도 되나.’

콩깍지가 아니라 사실이 그렇다. 지금까지 귀여운 조카 대하듯 굴던 임꺽정이 침을 삼키는 것만 봐도 알 수 있다.

꿀꺽.

“…….”

이 인간 조심해야겠군.

어쨌든 임꺽정이 이 정도인데 다른 놈들이야 말할 것도 없을 거다. 좀 젊고 한가락 한다 싶은 놈들이 트럭으로 몰려와 껄떡거릴 게 분명하다.

‘예를 들면 임창수라든지, 임창수라든지. 혹은 임창수라든지…….’

임창수. 상동 길드의 젊은 팀장.

아까부터 자꾸 놈의 얼굴이 눈앞에 어른거린다.

‘분명히 처음 보는 얼굴인데.’

그런데…… 왜 이렇게 신경이 쓰일까. 그 자식이 송이 씨한테 관심 있어 보여서 그런가?

“뭐 해? 안 나오고.”

“아, 네.”

생각은 이어지지 못했다. 임꺽정의 재촉에 나는 황급히 탈의실을 빠져나갔다.
```

## Current accepted English baseline

```markdown
# Chapter 80

Gate Management Office.

A young man in gleaming armor scowled.

“So why isn’t it allowed?”

The public official in charge of the B-rank Gate *The Minotaur’s Labyrinth* looked troubled.

“I already told you. Because of the fatal accident last week……”

“You think I don’t know that? What I’m saying is, why are you being so uptight with someone you know?”

“It’s a safety-inspection period. If you’re short on personnel, I can’t exactly approve your entry.”

The official was at his wit’s end.

Any Gate where a fatal accident occurred was subjected to a week of safety inspections. In other words, they raised the required number or level of personnel to prevent another accident. But the young man in front of him was being completely unreasonable.

“I put in a little extra this time. Good enough?”

“What is this!”

The official jumped at the white envelope the young man thrust out and glanced around in alarm. A new employee who had joined the office recently was staring at him with wide, round eyes.

“You—you can’t do this.”

“Can’t do what? You’ve been taking it just fine until now.”

“……”

“Being in charge of a Gate is supposed to have perks like this, right?”

At the young man’s blatant remark, the middle-aged official’s face flushed red. It wasn’t as if this was anything new, but what kind of disgrace was this in front of a new employee?

Still, the milk had already been spilled. His conscience grew thinner in proportion to the thickness of the white envelope.

“So……how is your team composed at the moment?”

“Ten, including me.”

“Ten?”

“Five B-ranks and five C-ranks. Why? Is there a problem?”

Of course there was. The Bucheon Terminal Guild, which had been involved in last week’s accident, had sent five B-rank Hunters and ten C-rank Hunters into the Gate. What happened to them had been plastered all over the front page of the local newspaper.

> **The Tragedy Brought on by a Shoddy Raid**
>
> **Bucheon Terminal Guild Master to Cooperate Fully with Hunter Association Investigation**

And now they were talking about ten people. Just as the official was hesitating—

“Hey, mister. Hold on.”

The young man’s menacing face had somehow acquired a smile.

“The numbers have to be roughly right anyway, don’t they?”

“Ah, yes. That works.”

“Then let’s take those guys along. Make it look good.”

The official followed the young man’s finger and turned his head. Five men and women had just entered the management office.

*Two middle-aged men. Two young men. And……*

One stunningly beautiful woman.

Judging by how the young man couldn’t take his eyes off her, his intentions were obvious.

“Good enough now?”

After quickly finishing his calculations, the official picked up the envelope.

“No problem.”

* * *

The middle-aged official kindly explained the situation to us.

It was currently a safety-inspection period, which meant that quite a few Guilds were experiencing delays in entering Gates. He even explained that with our current numbers, we would either have to hire mercenaries or join up with another Guild.

“You’re in luck. The people from Sangdong Guild are waiting, and they’re exactly five people short.”

“If we join them, how long will it take until we can enter the Gate?”

“We can process it immediately once you join.”

*That worked great for us.*

Team Leader Choi, who held the real decision-making power, nodded without objection.

“Then that sounds good.”

Just as Butler Kim, the Guild Master, signed the contract, an unexpected voice cut in.

“Nice to meet you. I’m Im Changsoo, the Team Leader from Sangdong Guild.”

His voice was smooth and easygoing, but his build was quite solid.

Unmistakable confidence radiated from him as he strode over.

*Sangdong Guild was strong enough to justify it.*

Sangdong Guild was one of the five leading mid-sized Guilds in the area around Bucheon, with more than twenty B-rank Hunters alone.

He looked to be in his late twenties at most, yet he was already a Team Leader. That wasn’t a position one could luck into over a game of cards.[^1]

*This guy’s no pushover.*

The Qi Sense I activated soon afterward changed my guess into certainty.

> **System**
>
> **Level 65 — Im Changsoo**

And yet, his name sounded familiar. Where had I heard it before?

While I was tilting my head, Butler Kim greeted him.

“Hello. I’m Kim Hwajong of Peace Guild.”

We called him Butler Kim, Uncle, Kim Hyung, and plenty of other things, and we knew he was only a figurehead Guild Master. But from an outsider’s perspective, it was obvious at a glance that he was the person in charge.

Im Changsoo answered with a bright smile.

“Ah, Peace Guild. I’ve heard the name quite a bit.”

Im Kkeokjeong and Miss Song, who were standing beside him, whispered to each other.

“Miss Song, how long has our Guild been around?”

“Hmm. About two weeks, I think?”

“Raids? Have we done many?”

“What are you talking about? We haven’t even started remodeling the Guild house. This is our first official raid.”

“……”

A B-rank Hunter could hear everything, no matter how quietly someone spoke. Im Changsoo’s head turned toward the two of them.

“And who are these people?”

“They’re Guild members.”

His gaze passed over the two of them—briefly over Im Kkeokjeong, then lingering a little longer on Miss Song.

“I see. I said something unnecessary, haha.”

“Not at all.”

“In any case, it seems fate brought us together. Since we’re on the same team now, I look forward to working with you.”

“All right, then. We’ll go change into our gear and be right back.”

“We’ll wait for you in front of the Gate.”

Team Leader Choi watched Im Changsoo’s back as he walked away, his gleaming chainmail clanking with every step. His face was serious.

“That man……”

“Is there a problem?”

“His equipment is limited edition. That stuff is incredibly hard to get.”

“……”

Oh. Right. It did look expensive.

* * *

Hunters were an enviable profession. Partly because they were guardians who had protected humanity from the Great Cataclysm……but mainly because they made a lot of money.

Even I made over 100 million won a year as a lowest-rank Hunter by working my ass off, so that said it all.

*The problem was that they spent a lot, too.*

The single biggest expense was equipment.

Magic Gems went into equipment as a matter of course, so no matter how carefully you considered cost-effectiveness, you couldn’t help but spend a fortune. On top of that, there were regular maintenance costs and repair fees whenever something broke.

The heartbreak was one thing. Your bank balance got ripped apart.

*There was a reason equipment insurance existed.*

In that regard, Team Leader Choi was the best employer ever.

He loaned us high-end equipment for free.

Rumble, rumble.

Team Leader Choi came into the changing room pulling a suitcase and called us over.

“I picked out decent equipment suited to each of your positions. Take one set each.”

It was a small suitcase, the sort you might use for a short trip. Im Kkeokjeong muttered in disappointment.

“Guess there isn’t one for me.”

The corners of Team Leader Choi’s mouth curled up.

“Of course there is. If you knew what this was, you’d be shocked……”

“Oh, this is a suitcase with a space-expansion spell on it.”

“……”

He had guessed it exactly.

My accurate prediction briefly wiped the smile off Team Leader Choi’s face. But he quickly composed himself and continued.

“That’s right. A space-expansion suitcase made by K Company. Nicholas, known as the greatest craftsman in North America……”

Clatter!

“Wow, it really is! Taekyung, look at this. It’s huge inside!”

“It is.”

“World-renowned designers also participated……”

“Wow, I’ve never seen anything like this before. I could probably sleep in here.”

“Once you close the suitcase, you won’t be able to get out until someone opens it.”

“Really?”

“This product keeps stored items in optimal condition through proper temperature control and ventilation at all times……”

Click, click.

“This is awesome. What do you think? Does it suit me?”

“It fits you perfectly. I thought it was a tailored suit.”

“You look good too. What’s that?”

“It says it’s a Black Drake Leather Set? No, it’s a leather set.”

“Really? If it’s Team Leader Choi’s, it must be good. Hahaha! Thanks, Team Leader Choi!”

“……Don’t mention it.”

Team Leader Choi had completely lost the will to fight by then and changed into his equipment without another word. I checked each piece of equipment I was wearing.

*Item Check.*

Ding.

> **System**
>
> **Item Window**
>
> **Masterwork Black Drake Leather Set**
>
> **Type:** Armor  
> **Grade:** Peak  
> **Description:** An armor set made from the leather of the B-rank monster Black Drake. You can feel the hand of a superb craftsman in it.
>
> **Effect:** Strength, Stamina, Agility, Toughness +10
>
> — Full Set Effect is active.
>
> **Item Window**
>
> **Masterwork Black Thorn Spear**
>
> **Type:** Spear  
> **Grade:** Peak  
> **Description:** A spear made from the spine of the B-rank monster Black Drake. It is extremely hard and sharp. You can feel the hand of a superb craftsman in it.
>
> **Effect:** Upon hitting an enemy, Bleeding activates with a 90% chance.

After checking them, I had exactly one thought.

*This is insane.*

An armor set that gave me forty points simply by wearing it, plus a spear that could kill an enemy from massive blood loss with nearly every stab.

The item information alone made it clear how incredible the effects were.

*So this is what gear advantage feels like.*

When I suddenly remembered my time in Murim, tears clouded my vision.

*Armor, my ass.*

I had fought in soft scraps of cloth and broken dozens of cheap spears. The people of Murim were the very definition of hard-boiled—the real tough guys.

“Maybe it’s because it’s designer gear, but it feels different right away.”

I turned my head and saw Im Kkeokjeong hopping up and down in place, his face flushed with excitement.

“It’s incredibly light, and I feel like my body’s faster too. Is it just my imagination?”

“I doubt it.”

There was no way it was just his imagination. Team Leader Choi had prepared this equipment specifically for Im Kkeokjeong, a D-rank Hunter. Of course it was good.

*Should I take a quick look?*

Just as I was about to place my hand on the full plate armor Im Kkeokjeong was wearing, Team Leader Choi approached us, already fully equipped.

“If you’re ready, let’s head out.”

“What about Butler Kim?”

“Out here, he’s the Guild Master.”

At Team Leader Choi’s pointed correction, Butler Kim chuckled.

“It’s fine. Besides……I’m always wearing my equipment.”

As he spoke, he unbuttoned his suit jacket, revealing bracelets on both wrists and a necklace. They were not ordinary accessories, of course.

The necklace was set with a Magic Gem, and the bracelets were etched with strange yet beautiful patterns.

“An artifact?”

“This is more convenient than a staff.”

Butler Kim answered modestly, but it was rare to see a mage dressed so lightly. Most carried at least some light armor or a staff for self-defense to improve their chances of survival.

*He’s probably not an ordinary mage.*

Everyone deferred to anyone who came out of Ares Guild.

I suddenly found myself curious about Butler Kim’s past, but the question was wiped clean from my mind the next moment.

Knock, knock.

“Hey, guys. Are you still not done?”

“Ah, we’re ready.”

It was Miss Song’s voice from outside the changing room. As soon as Team Leader Choi answered, the door opened a crack.

“Hurry up. People will be waiting.”

“Whoa.”

Her long, straight hair was tied tightly up, and she was wearing light leather armor. I swallowed a startled breath at the sight of her.

*Can a person really be this beautiful?*

It wasn’t just love making me see her through rose-colored glasses. That was simply the truth. I knew that much just from seeing Im Kkeokjeong, who had treated her like a cute niece until now, swallow hard.

Gulp.

“……”

*I’d better keep an eye on this guy.*

If even Im Kkeokjeong was reacting like this, the other guys would be no exception. Any young man who seemed even moderately capable would come crawling out by the truckload to hit on her.

*Take Im Changsoo, for example. Im Changsoo, say. Or maybe Im Changsoo……*

Im Changsoo. The young Team Leader from Sangdong Guild.

His face had been hovering in my mind since earlier.

*I was sure I’d never seen him before.*

And yet……why was he bothering me so much? Was it because that punk seemed interested in Miss Song?

“What are you doing? Aren’t you coming out?”

“Ah, yes.”

My thoughts were cut short. At Im Kkeokjeong’s urging, I hurried out of the changing room.

[^1]: Go-stop is a Korean card game traditionally played with a deck of flower cards.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 80`.

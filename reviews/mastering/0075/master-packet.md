# Master Edit Task — Chapter 75

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
| 조필     | **Jopil**          |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 시스템              | **System**                     |
| 로그아웃             | **Logout**                     |
| 헌터      | **Hunter**            |
| 팀장      | **Team Leader**       |
| 성진호 | **Seong Jinho** |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | A short laugh, snort-laugh, or quiet laugh; not necessarily a smirk. | smirk |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 끄덕 | idiom | A nod; do not reverse into a head-shake. | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

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

#### Chapter 73 tail (verified mastered)

…
moved to your Inventory! > > - Excellent work. An additional Reward will be granted! “Hm. You’re a shy child, aren’t you?” Jin Mukyung. An honest young man. “You bastard! What the hell is that supposed to mean?” “Forget it. Twenty-three is a bashful age.” “You little—” Jin Mukyung’s eyes went wild, and he was about to charge at me when— Creak. The door leading to the surface opened, and a servant cautiously poked his head inside. > **System** > > **Level 12: Jang Childeuk** “Um, Young Masters?” He was the servant who had regularly brought us meals until about three days ago. Something had clearly happened since we last saw him. His face was covered in bruises, and four or five of his teeth were broken. He continued speaking through the gaps in his teeth. “The Lesser Family Head is looking for you.” “…Damn it.” Jin Mukyung looked back and forth between Childeuk and me, then reluctantly lowered his fist. * * * We followed Childeuk. Jin Mukyung walked along with a sour expression, staring only at the ground as if everything offended him. Childeuk kept groaning whenever pain shot through him with each step. “Ow. Good grief. Urgh.” “…” That was seriously getting on my nerves. “How did you get hurt?” “There was a minor misunderstanding.” Those looked like fairly serious injuries for a minor misunderstanding. In the modern world, potions meant there was nothing that could not be healed. Murim was different. I clicked my tongue as I looked at Childeuk’s broken teeth. “That must hurt.” “It’s all right.” Childeuk puffed out his chest with stoic resolve. “A martial artist of the Jin Family of Taiyuan must be able to endure this much.” “…” He had been acting like he was about to die from the pain just moments ago. But wasn’t this man a servant? *Come to think of it, his clothes have changed.* He was wearing the dark navy martial arts uniform worn by martial artists of the Jin Family of Taiyuan. I thought he had been wearing a servant’s clothes before. Noticing my gaze, he smiled shyly. “Oh. I officially became a martial artist a few days ago.” “A martial artist?” Jin Mukyung, who had been walking silently behind us, suddenly spoke. “Under whose command?” I might have made a name for myself lately, but I was still nowhere near as famous as Jin Mukyung. Childeuk answered with an awestruck expression. “I serve directly under the Lesser Family Head.” “Only specially selected martial artists in our family are allowed to serve directly under our eldest brother.” Jin Mukyung looked Childeuk up and down. His gaze was not contemptuous so much as assessing, as though he were measuring Childeuk’s realm. “Your physique is decent, but you don’t seem to have learned any martial arts.” “Yes. To be honest, I’m bewildered myself. I’ve never properly performed so much as a single form.” According to my **Qi Sense**, Childeuk was Level 12. That was high for a servant who had done nothing but carry food, but by martial-artist standards, he was Third Rate. *The First Rate masters directly under Jin Wikyung are all above Level 40.* What was going on? Did he have powerful backing? Jin Mukyung seemed to have reached the same conclusion. His brow furrowed. “You must have good connections. What does your father do?” Childeuk blinked his large, calf-like eyes. “He died ten years ago.” “…” “…” “He was a famous herb gatherer, but he was killed by a tiger.” For a moment, my vision went hazy. Befitting a Peak master, Jin Mukyung was the first to regain his composure and hurriedly tried to smooth things over. “H-He must have been an excellent man.” “Even now, I remember him as a very innocent man. He and my mother were very loving, too.” “Then your mother… perhaps? No—she isn’t, right?” “She’s doing well.” Just as we breathed sighs of relief, Childeuk gazed wistfully at a distant mountain. “I buried her beside my father, so I’m sure they’re both doing well.” “…” “…” What followed was a march of death. I wanted to run away at full speed, but I gave up after hearing Childeuk muttering to himself. “Oh, I haven’t seen those flowers in a long time. I used to see them everywhere when I went into the mountains with my father.” “…” “…” If we had walked with him for another fifteen minutes, Jin Mukyung might have killed himself. Fortunately, after five minutes that felt like five hours, we reached our destination. “Oh, you’re here!” The sight of Jin Wikyung waiting in front of the pavilion nearly brought tears to my eyes. We cried out in voices thick with emotion. “Hyuung!” “Hyung-nim!” Childeuk awkwardly clasped his hands in a formal salute. “As ordered, I have escorted the Young Masters here.” Jin Wikyung had been hurrying toward Jin Mukyung and me, but he suddenly stopped and embraced Childeuk instead. “Jang Childeuk, a man of benevolence, righteousness, propriety, and wisdom! Martial Artist Jang, you’ve returned!” “Yes, sir, Lesser Family Head!” “You’ve completed a very important mission! Go and rest now.” What on earth was happening? Jin Mukyung and I stared blankly at the scene. Then a voice reached my ear through Sound Transmission. *There was, uh, a minor misunderstanding between me and this fellow…* “…” Somehow, I had a feeling I knew who was backing Childeuk.

#### Chapter 74 tail (verified mastered)

…
do you know her?” “Uh, well. You could say I do, and you could also say I don’t.” “What the hell does that mean? So what exactly is your relationship with her?” “Hmm.” *An ex-girlfriend whose face I’ve never even seen? Or a honey-trap scammer?* *One thing is certain.* Neither of us would be particularly happy to meet the other. I let out a deep sigh. * * * Long story short, Jin Mukyung agreed to go to the Mount Heng Sword Sect too. Jin Wikyung had used the masterstroke he had been saving. *I heard the Mount Heng Sword Sect has a lot of martial arts manuals…* *Even if they do, what good is that? It’s not like I can read them.* *It does matter.* *Pardon?* *The new Sect Leader has you figured out. She said she’d be willing to show you some of their Peak martial arts if you came.* *…When are we leaving?* *Right now.* Everything moved at lightning speed. It had been only two hours since Jin Wikyung saw us off and we climbed into the four-horse carriage. Jin Mukyung sat across from me, grumbling. “A carriage? It’ll take forever just to get there.” The land was so vast that, even by a rough estimate, it would take three days to reach Eung-hyeon, where the Mount Heng Sword Sect was located. For Jin Mukyung, who wanted to see the Mount Heng Sword Sect’s Peak martial arts as soon as possible, three days was an eternity. “Hey, coachman, can’t you go any faster?” A reply came from the driver’s box beyond the partition. “First of all, I’m not the coachman. And no, I can’t go any faster. You may not know this from inside, but it’s freezing out here, and I’m about to freeze to death. Anyway, that’s how things are.” “Use the whip and spur the horses on! A coachman should be able to do at least that much.” “I’ll say it again: I’m not the coachman. Also, the whip is frozen solid, so it would be more accurate to call it an icicle. If I jab the horses in the rear with this icicle, I think they’ll get very angry…” “What? If you’re not the coachman, why are you sitting there?” “Before we left, you shouted that the attendants were getting in your way and ordered everyone to get lost. The coachman got lost too.” Jin Mukyung thought about it carefully, then smacked his forehead. “Oh, right.” “…” As expected, this guy wasn’t normal either. “Then who are you?” Recalling the law of conservation of idiots, I answered, “Hyuk Mujin.” “Who’s Hyuk Mujin?” “You’ll know when you see his face. Hey, Mujin!” The partition slid down, revealing Hyuk Mujin’s frost-covered face. His teeth chattered nonstop as Jin Mukyung studied him closely, then snapped his fingers. “Oh, that guy.” Hyuk Mujin answered curtly, “Yes. I’m that guy.” “Then why didn’t you get lost too? You should’ve brought the coachman instead.” As if he had been waiting for that question, Hyuk Mujin proudly puffed out his chest. “I only obey my Captain’s orders.” “Captain?” “The Third Young Master.” Jin Mukyung’s head snapped toward me. “Did you call him?” “No. He was already there without me calling him.” “That’s what he says?” Hyuk Mujin looked back and forth between us with a wounded expression. “You two really are brothers, I suppose.” “Did you say your name was Hyung Mujin? Explain exactly what you mean by that.” Jin Mukyung bristled and spoke in a sharp voice, but I merely let out a long yawn. Hyuk Mujin clowning around was nothing new; when it came to dealing with that, I already had a full sixty-year cycle of internal energy. “It’s not Hyung Mujin. It’s Hyuk Mujin. I’ll try jabbing the horses in the rear with this thing, whether it’s a whip or an icicle.” Clack. Jin Mukyung glared at the partition, which had quickly slammed shut, then sighed and settled back into his seat. “I shouldn’t have expected anything. If the water upstream is filthy, how could the water downstream be clean… What are you doing?” I wrapped a fur hide around myself as I answered, “I’m going to circulate my qi.” “Really?” “Yeah. Circulate my qi.” “Then why does it look to me like you’re getting ready to sleep?” “You’re imagining things.” “Then why are you covering yourself with a fur hide?” “I get cold easily.” I made a show of sitting cross-legged. I also pressed myself firmly against the carriage wall so I wouldn’t topple over. *I can’t entrust my precious body to that guy.* I absolutely refused to come back and find my arms or legs broken. Better to make sure he couldn’t touch me at all. “You know what happens if you touch me, right? Huh? Do you know what qi deviation is or not?” “Seriously, this bastard’s been getting on my nerves for a while now…” The moment Jin Mukyung raised his fist, I hurriedly closed my eyes. From the outside, it would look as though I had begun circulating my qi. As expected, no fist came flying at me. All right, then. Now… *Logout.* Ding. > **System** > > - Would you like to log out? There was only one possible answer. [^1]: A *jeonse* lease is a Korean rental arrangement in which the tenant pays a large lump-sum deposit instead of monthly rent.

## Korean source

```text
＃75화



현대와 무림을 구분하는 방법은 우습게도 냄새와 온도다.

VR 헬멧 안의 땀 냄새. 창문 너머에서 비춰 오는 햇살 때문에 적당히 달궈진 캡슐 안의 열기.

“후아.”

헬멧을 벗고 캡슐을 빠져나오자 좀 살 것 같다. 그래 봤자 열탕에서 온탕으로 바뀐 정도지만.

‘얼마나 지난 거지?’

손목에 찬 시계를 확인했다. 약 7년 전, 헌터 훈련소 앞 가판대에서 샀던 만이천 원짜리 싸구려 디지털시계는 알람과 스톱워치 기능이 있다는 장점이 있었다.

삑.



[02:05:35]



두 시간 하고도 5분 35초.

무림에서 20일 정도를 머물렀으니 지난번과 비교해 얼추 시간이 맞아떨어진다.

‘현대로 왔으니 시간 배율이 역전되었을 거고.’

로그아웃을 한 지금은 현대에서의 열흘이 무림의 한 시간이다. 나는 고시원 공용 샤워장에서 몸을 씻은 다음 방으로 돌아왔다.

방문을 닫으려던 찰나, 검은 그림자가 휙 솟구쳤다.

“왁!”

그래, 성진호 이 인간일 줄 알았다.

“어.이.구. 깜.짝. 놀.랐.네.”

“……뭐냐 그 반응은. 알고 있었어?”

“들숨 날숨이 아주 격렬하시던데. 진호 씨, 흥분하셨나 봐.”

날이 지날수록 예리해진 오감은 굳이 [기감]이 아니어도 주위의 소리와 움직임을 잡아낼 수 있다.

나름 숨죽인 채 기다리고 있었던 모양이지만 내 귀에는 그의 작은 움직임과 숨소리 하나하나가 천둥처럼 들렸다.

“숨 좀 작게 쉬어. 명색이 고시원 총무인데 숨소리가 커서 민원 들어오면 곤란하지.”

“젠장. 어떻게 알았지? F급 헌터 주제에…… 아, 너 얼마 전에 C급 됐지. 참.”

“인성 봐라. F급이라고 놀리는 게 아주 입에 붙었구만.”

“야, 네가 내 나이 돼 봐라. 어제 먹은 반찬도 기억 안 나는데 겨우 일주일 전에 있었던 일이 팍팍 떠오르겠냐?”

“일주일?”

겨우 그것밖에 안 됐나?

내게는 한 달도 훨씬 지난 일이 진호 형에게는 고작 지난주에 있었던 일이다. 미묘한 괴리감이 느껴졌다.

“어. 표정이 왜 그래? 문제라도 있냐?”

“문제는 무슨. 그런데 무슨 일로 찾아왔어?”

“이 자식 이거 말 뽄새 보게. 우리가 볼일 있어야 볼 수 있는 비즈니스 관계야? 어?”

“본론만. 짧게.”

진호 형의 얼굴이 굳어졌다. 장난이 너무 심했나?

생각해 보니 요즘 내가 너무 무심했던 것 같기도 하다. 무림으로 돌아가기 전에도 여러 가지 문제로 얼굴도 자주 못 봤는…….

“저녁. 사 줘.”

“…….”

“삼겹살. 철판구이. 치맥.”

시바. 그럼 그렇지.

그 와중에 메뉴도 자기가 고르고 자빠졌네.

“나한테 돈 맡겨 뒀어?”

“네 돈이 내 돈. 내 돈이 내 돈 아니냐.”

“발음 똑바로 해라. C급 헌터 주먹맛 보고 싶지 않으면.”

움찔한 진호 형이 손바닥을 싹싹 비볐다.

“부탁드립니다. 선생님의 돈으로 제 메마른 위장에 기름칠 좀 해 주십시오.”

“…….”

태세 전환 봐라. 우디르도 울고 가겠다.

어이가 없었지만 한편으로는 피식 웃음이 나왔다. 한 달 가까이 제대로 된 진짜 음식을 못 먹은 위장도 비명을 질러 대던 차였다.

‘간만에 제대로 먹어 보자.’

나는 엄숙한 목소리로 말했다.

“태도가 마음에 드는군. 앞장서라.”

“어디로 모실까요?”

“삼겹살이나 철판구이는 질렸다. 오늘은 좀 더 비싸게 먹어 보자꾸나.”

“서, 선생님. 그렇다면!”

진호 형이 눈을 부릅떴다.

“한우! 방목으로 키워져 환상적인 마블링을 자랑하는 그것?”

“뭔 개소리야. 곱창 먹으러 갈 건데.”

“…….”

“싫으면 굶든가.”

턱.

내 어깨를 붙잡은 진호 형이 비장한 얼굴로 말했다.

“예전부터 꼭 그렇게 먹어 보고 싶었습니다.”

그날 오후 다섯 시부터 시작된 이른 식사는 3차 막걸리 집에서 끝났고, 진호 형은 술에 떡이 됐다.

“크워어어.”

“…….”

이거 어디서 많이 본 장면인데.

묘한 기시감을 느끼며 진호 형을 들쳐 업었을 때, 휴대폰이 울렸다.



〈 명품충



명품충

내일 같은 시간, 같은 장소에서 뵙죠.



짤막한 문자 한 통. 발신인은 최 팀장이었다.



* * *



수면 모드의 단점이자 장점은 수면 시간이 줄어든다는 점이다. 조필과의 싸움에서 큰 부상을 입었을 때를 제외하면 세 시간을 넘긴 적이 없다.

‘수련하기에는 좋지.’

새벽 세 시.

최적의 컨디션으로 눈을 뜬 나는 가부좌를 틀었다. 언제부턴가 하루의 시작과 끝은 늘 운기조식이다.

솨아아.

공력의 물결이 흐르기 시작했다.

단전에서 솟구친 15년의 공력이 신체 내부에 쌓인 노폐물을 정화시키며 잠들어 있던 혈도에 생기를 불어넣었다.

띠링.



- [운기조식]을 마쳤습니다.

- [공력]이 아주 약간 증가했습니다.



시스템 알림과 함께 눈을 떴을 때는 두 시간이 훌쩍 지난 후였다. 무림이었다면 곧장 연무장으로 나가 몸을 풀었겠지만 현실은 여러 가지 제약이 많다.

양계장처럼 다닥다닥 붙어 있는 고시원에서는 더더욱.

‘망할 놈의 고시원. 빨리 탈출하든가 해야지.’

수련도 돈으로 하는 시대다. 잘 버는 놈들이야 널찍한 개인 트레이닝 룸을 몇 개씩 가지고 있지만 나처럼 없는 놈들은 열악한 환경에 맞추는 수밖에.

“후읍. 흡.”

오전 내내 동네를 뛰고, 돌아와서는 기본적인 맨몸 운동을 쉬지 않고 이어 갔다. 능력치가 높아진 덕분인지 지치기는커녕 오히려 활력이 샘솟는다.

그런 나를 보며 진호 형이 질린 얼굴로 물었다.

“지치지도 않냐?”

“별로.”

“한 손 팔 굽혀 펴기를 너처럼 쉽게 하는 놈은 처음 본다. 몇 개째야?”

“몰라. 삼백까지 세고 귀찮아서 안 셌어.”

“괴물이네. 원래 C급 헌터쯤 되면 그 정도는 하는 거냐?”

“그런데, 성진호 씨.”

“어?”

“왜 왔어?”

십여 분 전 퀭한 몰골로 나타나더니 아직도 내 방에서 안 나가는 진호 형이었다.

“보면 모르냐. 라면 먹으려고 왔지.”

톡톡. 촤아악.

다 익어 가는 면발 위로 날계란을 투하하는 모습이 자연스럽다.

반숙을 만들기 위한 버너 화력 컨트롤은 절정 고수라고 해도 좋을 정도다.

“그걸 굳이 여기서 처먹어야 하는 이유 세 가지만 대 봐.”

“첫째. 내 방에 TV가 없으니까. 둘째. 네 방에 TV가 있으니까. 셋째. 라면은 TV를 보면서 먹어야 제맛이니까.”

청산유수로 흘러나오는 말을 들으니 피가 거꾸로 솟는다.

“차라리 하나 사! 돈 없으면 그냥 가져가!”

“아, 그건 좀. 어차피 나갈 건데 짐 늘려 봤자 뭐하냐.”

“그럼 귀찮게 자꾸 들락거리지 말고…… 응? 방금 뭐라고?”

“뭐가?”

“아니, 나간다고?”

“아, 그거.”

진호 형이 떡이 진 머리를 긁적였다.

“그냥 그렇게 됐다. 뭐, 날짜까지 확정된 건 아닌데 조만간 방 빼려고. 언제까지 여기 처박혀 있을 수도 없는 노릇이고.”

“…….”

“뭘 그런 눈으로 쳐다봐?”

“아니, 뭐. 그냥.”

나는 머쓱한 얼굴로 시선을 피했다.

고시원에 사는 사람들 중 사연 없는 사람이 어디 있겠나. 나도 그렇고 진호 형도 마찬가지다. 구태여 이유를 묻는 건 실례다.

‘그래도 아쉽긴 하네.’

몇 년간 친구처럼, 형제처럼 지냈던 사람이다. 이렇게 갑자기 나간다니.

복잡 미묘한 기분에 사로잡혀 있던 나는 조심스레 입을 열었다.

“형, 혹시…….”

“네 마음은 알겠는데. 정중하게 거절한다.”

무슨 말을 하려는지 알아챈 걸까? 내 말을 단칼에 잘라 낸 진호 형이 말을 이었다.

“인마, 형 나이가 서른이야. 내 밥그릇은 내가 챙겨.”

“그렇다면 어쩔 수 없고.”

진호 형이라면 같이 살아도 될 것 같았는데, 섣부른 오지랖이 그의 자존심을 건드린 모양이었다.

형이 구겨진 얼굴로 냄비 뚜껑을 열었다.

“차라리 처음부터 말을 하든가.”

“애초에 생각도 없었으면서 무슨.”

“무슨 헛소리야. 네가 안 먹는다고 해서 하나만 끓였는데.”

“……?”

아니, 잠깐만. 이거 이야기 흐름이 어떻게 되는 거냐.

몇 초간의 침묵 끝에 내가 입을 뗐다.

“무슨 얘기야 그게. 갑자기 뭘 끓여.”

“당연히 라면이지.”

진호 형이 흉흉한 눈빛으로 나를 노려봤다.

“꼭 안 먹는다고 해 놓고 맛있게 끓이면 한 젓가락 달라는 놈이 있어요. 내가 너한테 한두 번 당해?”

“…….”

“C급 헌터라는 놈이 가난한 형님 밥그릇에 손을 뻗쳐? 네가 그러고도 사람이냐?”

“…….”

앞에서 밥그릇 운운한 게, 진짜 밥그릇이었구나.

방금 들은 말 그대로 돌려주고 싶다.

‘저게 사람이냐.’

저런 인간하고 같이 살 생각을 한 내가 병신이지.

나는 자괴감을 느끼며 옷을 걸쳐 입었다. 슬슬 최 팀장을 만나러 갈 시간이다.

쾅!

부서져라 방문을 닫고 빠져나오는 내 등 뒤로 마지막 외침이 울려 퍼졌다.

- 마트 가는 거면 김치 좀!

아, 죽이고 싶다.



* * *



‘장소가 어디였지?’

약 20일 전의 기억을 더듬어 약속 장소에 도착했다.

빌딩 숲 중심부에 위치한 대형 카페. 창가에 앉아 있던 잘생긴 남자가 나를 발견하고 손을 흔들었다.

“여깁니다.”

굳이 말하지 않아도 알 수 있었다. 매장 안에 수십 개의 테이블이 있는데도 앉아 있는 손님은 오직 최 팀장 혼자였으니까.

‘여전히 잘생겼네.’

얇은 캐주얼 정장을 걸친 최 팀장은 방금 화보에서 튀어나온 것 같았다. 20대에 모든 걸 가진 성공한 인생. 외모, 재력, 성격…… 아니다. 성격은 빼자.

가벼운 악수를 나눈 우리는 자리에 앉았다.

“식사는 하셨습니까?”

“아뇨.”

최 팀장이 고개를 갸웃했다.

“그래요? 라면 드신 것 같은데.”

“…….”

젠장, 이 자식 완전 개코네.

고시원에서 있었던 이야기를 구구절절하게 설명하기에는 너무 부끄럽다. 나는 황급히 화제를 돌렷다.

“점심시간인데 사람이 없네요.”

“영업을 안 하니까요.”

“예?”

“유리창도 커튼으로 가리고 문에 클로즈(Closed) 팻말도 걸어 놨는데 당연히 안 들어오죠.”

주위를 둘러보니 정말 최 팀장의 말대로였다.

약속 장소가 여기니, 당연히 열려 있을 거라고 생각하고 들어와서 눈치를 못 챈 모양이다. 이 상황 자체가 너무 이상해서 눈을 깜빡였다.

“그런데 지금 영업하는 중이잖아요.”

매장 안의 불빛은 환하고, 에어컨 바람으로 시원하다. 언뜻 보이는 직원들만 열 명인데 왜 문을 닫아 놓은 거지?

최 팀장은 태연하게 대꾸했다.

“해야죠. 손님이 있으니까.”

“영업 안 한다면서요?”

“그거야 사장 마음 아니겠습니까.”

“어…… 팀장님. 혹시나 해서 물어보는 건데요.”

“굳이 안 물어보셔도 됩니다. 이 카페 제 거니까요.”

그래, 그럴 것 같더라.

곰곰이 생각해 보니 지난번에 만났을 때도 카페 안에는 우리 둘뿐이었다.

‘파도 파도 끝이 없네.’

나는 혀를 내두르며 말했다.

“팀장님, 돈 많으시네요.”

“부족하지 않을 만큼 있습니다. 그러니까 이런 계약서도 내밀 수 있는 거고요.”

최 팀장이 부드럽게 웃으며 서류철을 내밀었다.

“자, 이제 일 얘기를 해 볼까요?”

더 이상 망설일 이유는 없다. 나는 힘차게 고개를 끄덕였다.

“그러시죠.”

한 시간 후, 내가 마지막 서명을 끝마침과 동시에 시스템 알림이 울렸다.

띠링.
```

## Current accepted English baseline

```markdown
# Chapter 75

The way to tell the modern world apart from Murim is, oddly enough, by smell and temperature.

The smell of sweat inside a VR helmet. The heat inside a capsule warmed just right by sunlight streaming through the window.

“Phew.”

Once I took off the helmet and climbed out of the capsule, I finally felt like I could breathe. It was still only the difference between a scalding bath and a hot bath, though.

*How much time has passed?*

I checked the watch on my wrist. The cheap twelve-thousand-won digital watch I had bought from a street stall in front of the Hunter training center about seven years ago had the advantage of coming with an alarm and stopwatch function.

Beep.

[02:05:35]

Two hours, five minutes, and thirty-five seconds.

I had spent around twenty days in Murim, so the timing roughly matched what had happened last time.

*Since I came to the modern world, the time ratio must have been reversed.*

Now that I had logged out, ten days in the modern world amounted to one hour in Murim. I washed myself in the communal shower of the goshiwon[^1] and returned to my room.

Just as I was about to close the door, a black shadow shot upward.

“Wah!”

Of course. It was Seong Jinho.

“Oh. My. God. What a surprise.”

“……What’s with that reaction? You knew I was here?”

“Your inhaling and exhaling were extremely intense. Mr. Jinho, were you excited?”

My five senses had grown sharper with each passing day. I could pick up every sound and movement around me without even using Qi Sense.

He seemed to have been waiting in silence, but to my ears, every tiny movement and breath he made sounded like thunder.

“Breathe a little more quietly. You’re supposedly the goshiwon manager, so it would be a problem if people filed complaints because your breathing was too loud.”

“Damn it. How did you know? You’re just an F-rank Hunter…… Oh, right. You became C-rank a while ago.”

“Look at the way you talk. Making fun of me for being F-rank has really become a habit.”

“Hey, if you were my age, would you remember something that happened barely a week ago? I can’t even remember what side dishes I ate yesterday.”

“A week?”

Was that really all the time that had passed?

To me, it had been well over a month. To Jinho-hyung, it had been barely a week. I felt a subtle sense of disconnect.

“Hey. Why do you look like that? Is something wrong?”

“What do you mean, something’s wrong? Anyway, what brings you here?”

“Listen to the way you talk. Are we some kind of business relationship that we can only see each other when there’s business involved?”

“Just get to the point. Keep it short.”

Jinho-hyung’s face hardened. Had I gone too far with the teasing?

Come to think of it, I had been too indifferent lately. Even before returning to Murim, I hadn’t been able to see him often because of all sorts of problems……

“Buy me dinner.”

“…….”

“Grilled pork belly. Teppanyaki. Fried chicken and beer.”

Shit. Of course.

And he even had the nerve to choose the menu himself.

“Did I leave money with you?”

“Your money is my money. And my money is my money, isn’t it?”

“Pronounce that properly. Unless you want to feel the fist of a C-rank Hunter.”

Jinho-hyung flinched and rubbed his palms together.

“Please, sir. Use your money to put some grease on my parched stomach.”

“…….”

Talk about changing his tune. Even Udyr would weep.

It was absurd, but I let out a quiet laugh. My stomach had also been screaming after going nearly a month without a proper meal.

*Let’s eat something decent for once.*

I spoke in a solemn voice.

“I approve of your attitude. Lead the way.”

“Where would you like to go, sir?”

“I’m tired of grilled pork belly and teppanyaki. Let’s go for something pricier today.”

“Th-then, sir!”

Jinho-hyung’s eyes widened.

“Hanwoo![^2] The pasture-raised beef famous for its incredible marbling?”

“What the hell are you talking about? We’re going out for gopchang.[^3]”

“…….”

“If you don’t like it, starve.”

Thump.

Jinho-hyung grabbed my shoulder and spoke with a solemn expression.

“I’ve always wanted to eat that.”

The early dinner that began at five that afternoon ended at a third-round makgeolli bar, and Jinho-hyung was completely plastered.

“Krroooorr.”

“…….”

I had seen this scene somewhere before.

As I felt a strange sense of déjà vu and hoisted Jinho-hyung onto my back, my phone rang.

〈Designer-Brand Junkie

**Designer-Brand Junkie**

See you tomorrow at the same time, same place.

It was a short text message. The sender was Team Leader Choi.

* * *

The downside—and upside—of Sleep Mode was that it reduced the amount of time I needed to sleep. Other than when I had suffered serious injuries fighting Jopil, I had never slept for more than three hours.

*It’s useful for training.*

Three in the morning.

I woke up in peak condition and sat cross-legged. At some point, circulating my qi had become how I began and ended every day.

Fwoosh.

A wave of internal energy began to flow.

The fifteen years of internal energy surging from my dantian cleansed the waste products accumulated inside my body and breathed vitality into dormant acupoints.

Ding.

> **System**
>
> - You have finished circulating your qi.
>
> - Your internal energy has increased very slightly.

By the time I opened my eyes at the System notification, more than two hours had passed. If I were in Murim, I would have gone straight to the training yard to warm up, but the real world came with all sorts of restrictions.

Especially in a goshiwon, where the rooms were packed together like a chicken farm.

*Damn goshiwon. I need to get out of here soon.*

This was an age when training was done with money, too. People who made good money had several spacious private training rooms, while people like me had no choice but to adapt to poor conditions.

“Huff. Inhale.”

I spent the entire morning running around the neighborhood, then continued with basic bodyweight exercises without taking a break after I returned. Maybe it was because my Stats had increased, but instead of getting tired, I felt more and more energized.

Watching me, Jinho-hyung asked with a horrified look:

“Don’t you get tired?”

“Not really.”

“I’ve never seen anyone do one-arm push-ups as easily as you. How many have you done?”

“I don’t know. I counted to three hundred, then got too lazy to keep counting.”

“You’re a monster. Is that normal for a C-rank Hunter?”

“By the way, Seong Jinho.”

“Huh?”

“Why are you here?”

Jinho-hyung had appeared ten minutes earlier with a haggard face, and he still hadn’t left my room.

“Can’t you tell? I came to eat ramen.”

Tap tap. Ssshhk.

He naturally dropped a raw egg onto the noodles, which were almost cooked.

His control of the burner flame to leave the egg perfectly runny was worthy of a Peak master.

“Give me three reasons you have to stuff your face with that here.”

“First, there’s no TV in my room. Second, there’s a TV in your room. Third, ramen tastes best when you eat it while watching TV.”

The words poured out of him like a flowing stream, and my blood started boiling.

“Just buy one! If you don’t have money, take mine!”

“Ah, maybe not. I’m leaving soon anyway. Why bother adding to my luggage?”

“Then stop coming in and out of here and bothering me…… Huh? What did you just say?”

“What?”

“No, wait. You’re leaving?”

“Ah, that.”

Jinho-hyung scratched his matted hair.

“It just worked out that way. The date isn’t set yet, but I’m planning to move out soon. I can’t stay holed up here forever.”

“…….”

“Why are you looking at me like that?”

“No, it’s nothing.”

I awkwardly looked away.

Who living in a goshiwon didn’t have a story of their own? I had mine, and Jinho-hyung had his. It would be rude to ask for the reason.

*Still, it’s a shame.*

He was someone I’d spent years with, like a friend and a brother. And now he was leaving so suddenly.

Caught up in complicated feelings, I cautiously opened my mouth.

“Hyung, by any chance……”

“I know what you’re about to say, but I respectfully decline.”

Had he realized what I was going to say? Jinho-hyung cut me off decisively and continued.

“Kid, I’m thirty years old. I’ll fill my own bowl.”

“Then there’s nothing I can do.”

I had thought I could probably live with Jinho-hyung, but my premature meddling seemed to have pricked his pride.

With a crumpled expression, he opened the lid of the pot.

“You should’ve just said so from the start.”

“What are you talking about? You weren’t even planning to.”

“What nonsense. I only cooked one because you said you weren’t eating.”

“……?”

Wait a second. How had the conversation suddenly ended up here?

After several seconds of silence, I finally spoke.

“What are you talking about? What’s this about cooking something all of a sudden?”

“Obviously, ramen.”

Jinho-hyung glared at me with a threatening look.

“There’s always someone who says he isn’t eating, then asks for a bite when you cook it well. How many times have I fallen for that one with you?”

“…….”

“So a C-rank Hunter reaches into his poor hyung’s bowl? Are you even human?”

“…….”

So when he had been talking about his bowl earlier, he had meant an actual bowl.

I wanted to throw his own words right back at him.

*Is that thing even human?*

I was a fucking idiot for thinking I could live with someone like him.

Feeling deeply ashamed of myself, I threw on some clothes. It was almost time to meet Team Leader Choi.

Bang!

I slammed the door hard enough to break it and left. One last shout rang out behind me.

“If you’re going to the market, get some kimchi!”

Ah, I wanted to kill him.

* * *

*Where was the place again?*

I dredged up my memories from about twenty days ago and arrived at the meeting place.

It was a large café in the heart of a forest of skyscrapers. A handsome man sitting by the window spotted me and waved.

“Over here.”

I didn’t need him to say anything. There were dozens of tables in the café, yet Team Leader Choi was the only customer sitting inside.

*He’s still handsome.*

Wearing a thin casual suit, Team Leader Choi looked as though he had just stepped out of a fashion shoot. A successful man in his twenties who had everything: looks, money, personality……

No. Leave personality out of it.

After exchanging a brief handshake, we sat down.

“Have you eaten?”

“No.”

Team Leader Choi tilted his head.

“Really? You look like you’ve eaten ramen.”

“…….”

Damn it. This guy’s nose was incredible.

It was too embarrassing to explain the whole story about what had happened at the goshiwon, so I hurriedly changed the subject.

“It’s lunchtime, but there’s no one here.”

“We’re closed.”

“What?”

“The windows are covered with curtains, and there’s a ‘Closed’ sign on the door. Of course no one’s coming in.”

I looked around. Just as Team Leader Choi had said, everything was covered up.

I had assumed the café would naturally be open since it was the meeting place, so I hadn’t noticed. The whole situation was so strange that I blinked.

“But you’re open right now.”

The lights inside were bright, and the air-conditioning kept the place cool. I could glimpse at least ten employees, so why had they closed the door?

Team Leader Choi answered calmly.

“We have to. There’s a customer.”

“You said you weren’t open.”

“That’s up to the owner, isn’t it?”

“Uh…… Team Leader, I’m asking just to be sure.”

“You don’t need to ask. This café is mine.”

Right. I had figured as much.

Thinking back, the café had also been empty except for the two of us the last time we met.

*I keep digging, and the hole never ends.*

I clicked my tongue and said:

“Team Leader, you have a lot of money.”

“I have enough that I don’t need to worry about running short. That’s why I can put a contract like this in front of you.”

Team Leader Choi smiled gently and handed me a folder.

“Now, shall we talk business?”

There was no reason to hesitate any longer. I nodded firmly.

“Let’s.”

An hour later, the System alert rang out just as I finished signing the last page.

Ding.

[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement, often with shared facilities.

[^2]: Hanwoo is a Korean breed of native cattle whose beef is prized for its marbling.

[^3]: Gopchang is a Korean dish made from grilled intestines, usually beef intestines.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 75`.

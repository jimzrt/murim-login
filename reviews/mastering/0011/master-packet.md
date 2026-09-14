# Master Edit Task — Chapter 11

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
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 일격     | **One Strike**                         |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 아이템              | **Item**                       |
| 습득               | **Acquired**                   |
| 숙련도              | **Mastery**                    |
| 로그아웃             | **Logout**                     |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |

## Matched address pairs

(No matching address pairs.)

## Matched risk notes

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 형 | kinship | Junior-to-senior kinship/address. Casual speech often retains hyung; do not flatten every 형 to “brother.” | |
| 마나 | murim_vs_hunter | Modern Hunter-system energy is mana when the source distinguishes it from Murim qi. | |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 5–9

## Plot

Taekyung completes the tutorial, learns that Logout requires First Rate, Lv. 30, and 500 Fame, and is taken to the Medicine King Hall after his fight with Hyuk Mujin. He begins cultivating the Jin Family’s Cultivation Technique, pretends that his memory has not returned, and discovers an unused room filled with martial arts manuals. The System reveals that martial arts occupy ten slots, three of which are already filled. Jin Wikyung and Wipeng catch him practicing footwork at night, but accept his explanation. In Chapter 9, Taekyung sorts the manuals, acquires the Jin Family’s Manoeuvre Technique, completes its achievement, and earns the title Novice Trainee. Seeking a proper place to practice, he asks for an empty room. Jin Wikyung instead orders his indefinite confinement in the training hall as a protective measure against the Elder Council’s coming attack. Wipeng secretly explains the plan through Sound Transmission and promises to release him within seven days; Taekyung negotiates that down to three days before being escorted away.

## Continuity

- Taekyung remains trapped in Murim; Logout and death rules remain unresolved.
- Logout requires First Rate, Lv. 30, and 500 Fame.
- He is practicing the Jin Family’s Cultivation Technique and has acquired the Jin Family’s Manoeuvre Technique; he has also located the Jin Family’s Spear Technique.
- His martial arts interface has ten slots, with three already filled.
- Taekyung continues pretending that his memory has not fully returned.
- Jin Wikyung is the Lesser Family Head and Taekyung’s protective older brother; Wipeng is his capable aide and can use Sound Transmission.
- The Elder Council is preparing to challenge Jin Wikyung’s authority by attacking Taekyung’s conduct.
- Taekyung is being held in the training hall for an indefinite period, with Wipeng promising release within three days after their negotiation.

## Translation Decisions

- The hereditary martial art is rendered **Jin Family’s Manoeuvre Technique**, using British spelling consistently with the chapter’s terminology.
- The achievement reward is rendered as the title **Novice Trainee**.
- `음성 전송` is rendered **Sound Transmission**.
- `소가주` is rendered **Lesser Family Head**.
- System messages remain grouped into `> **System**` blockquote windows whenever consecutive.

### Prior accepted reading-copy tails

#### Chapter 9 tail (verified mastered)

…
fully returned. And besides… he changed into an entirely different person overnight. You’ve noticed it too.” “That’s true, but…” Wipeng trailed off. The Third Young Master had definitely changed. Whether the memory loss was a lie or the truth, the way he was behaving now was undeniably hopeful. Jin Wikyung thought for a moment before speaking. “Wipeng.” “Yes.” “Prepare an order in my name.” “What sort of…?” “Find a few suitable charges and sentence him to indefinite seclusion in the training hall.” “Ah.” Wipeng slapped his forehead. It was mostly for show, but under the circumstances, it was an excellent emergency measure. It would relieve the pressure Jin Wikyung was about to receive at the upcoming family council meeting while lowering the severity of the punishment imposed on Jin Taekyung. And on top of that… “It fulfills the Third Young Master’s request too. He was looking for somewhere to train.” Wasn’t this three birds with one stone? Wipeng was genuinely impressed. “As expected of you, my lord.” “That’s how the people in my family are. Oh, did I ever tell you? Taekyung was such a clever child when he was young. One day…” “…I’ll go write the order.” * * * “Therefore, for violating fourteen regulations and disrupting the discipline of the family, the Third Young Master, Jin Taekyung, is hereby sentenced to indefinite seclusion in the training hall.” His name was… Wipeng, wasn’t it? I listened silently to the sour-looking bastard, then raised my hand. “I have a question.” “Go ahead.” “What does ‘indefinite’ mean?” Wipeng answered reluctantly. “It means there is no set deadline.” “Oh.” I’d thought the game’s language system had malfunctioned. Fortunately, it meant exactly what I thought it meant. Ha ha. “Ha ha ha.” “Ho ho ho.” Laughter was contagious. The warriors who had accompanied Wipeng began laughing along with me. In that warm atmosphere, Wipeng read the final line. “The convict, Jin Taekyung, shall submit to the bonds.” “No.” “…” “…” “I said no. Fuck.” The two men approaching with rope restraints looked at Wipeng as if to say, *This isn’t how it was supposed to go.* I ignored them and said what I had to say. “I asked you to find me a room to practice in, not throw me in prison.” Were these people all completely fucking insane? “Now, Third Young Master. Calm down and listen to me.” “Listen to what, for fuck’s sake? You’re going to tell me the training hall has everything I need for practice and the living conditions aren’t bad. That kind of bullshit.” Judging by Wipeng’s expression, I’d hit the nail on the head. I drove the point home. “You people are the type to tell someone to enjoy military service because soldiers got a pay raise. Forget it. I’m not going in. I’ll practice by myself in my room or out in the yard.” Honestly, on the surface, the training hall didn’t sound so bad. But the word *indefinite* stuck in my mind like a thorn. I needed to learn martial arts and Level up immediately. I couldn’t spend day after day in the training hall, craning my neck and waiting to be let out. I flopped onto the floor. “Go ahead and gut me!” “Third Young Master, that’s enough. Please get up.” Wipeng scowled at me. “The Lesser Family Head made this decision entirely for your sake.” “Jin Wikyung—I mean, my brother?” That brother-obsessed idiot had given this order? At that moment, Wipeng’s lips moved. A voice reached my ears at the same time, with a strange quality unlike ordinary speech. > This is Sound Transmission. Don’t be alarmed. Just listen. Sound Transmission. I remembered seeing it in martial arts novels. A kind of telepathy that only masters could use. > “You may not know this because you’ve lost your memory, but the Third Young Master is a person of concern. A harsher punishment may be handed down soon, so the Lesser Family Head is taking action beforehand.” I had worked hard for twenty-seven years. What did I do to deserve an aggravated sentence? As I lamented, Wipeng’s Sound Transmission continued in my ear. > “It may be called indefinite confinement, but do you really think the Lesser Family Head intends to bury you in the training hall for the rest of your life?” I shook my head. There was no way he would do that. Unless he wanted the two of us locked in there together. > I’ll get you out within seven days and nights at the latest. How does that sound? There was fierce determination in Wipeng’s eyes. If I refused this too, he looked ready to beat me and drag me there if he had to. *Fuck, are all the NPCs here thugs or what?* *Hey, you bastard. Are you really that good at fighting?* I raised my Qi Sense and checked Wipeng’s Level. > **System** > > - **Lv. ???** “…” *He really is a thug.* A Level thug. He was probably every bit the human butcher Jin Wikyung was. Wipeng opened his eyes wide and asked, > What will you do? Even as I trembled with fear, I held up three fingers. > …You want me to get you out in three days? *What kind of bastard is this?* Wipeng glared at me as if he were thinking exactly that. Then he sighed. “Escort him.” #TrainingHall #ClosedDoorTraining #Negotiation #Successful.

#### Chapter 10 tail (verified mastered)

…
was no joke. By feel alone, the monster had to weigh close to fifty kilograms. My Stamina wouldn’t last if I swung something like this for hours. My current realm was Second Rate. Even with the System’s help, swinging around more than half a sack of rice as if it were a pinwheel was impossible. *It’s not like I suddenly have tiger power or something.* That was when it hit me. “…Huh?” What had I just said? The strength of a tiger? “I do have it.” This was a game. It had a System and stats. And I had internal energy. Ten years of internal energy that I could draw out through a cultivation technique! It was embarrassing that I had forgotten, even for a moment. “It’s not like I’ve ever used anything like that before…” They say you only know what something is like once you’ve experienced it. Was it any wonder an F-rank Hunter was F-rank? With barely any mana to speak of, I made do with my bare body. Even among Hunters, I was treated like a half-baked amateur. *Still, that solves one problem.* I let out a dumbfounded laugh, then picked up the spear. Slowly and carefully, I began drawing out my internal energy. The formula of the Jin Family’s Cultivation Technique, imprinted in my mind by the System, rewound rapidly through my thoughts, guiding my internal energy along its prescribed path. A prickling sensation ran through me. The response was immediate. The ten years of internal energy coiled in my dantian spread throughout my body. Because this was a game and I was a martial artist, I could feel it spreading through every part of me. *This is…* Power surged through my entire body. My vastly heightened physical abilities and senses once again brought exhilaration to someone who had spent his life as an F-rank Hunter. *How can a person change this much?* I gripped the spear and began practicing the *Jin Family’s Spear Technique*. The fifty-kilogram iron spear no longer felt heavy. It thrust and slashed through the air along the paths I wanted it to follow. Before long— Ding. > **System** > > - Successful attempts (6 / 100) The notification I had been waiting for began to ring. * * * Jin Wikyung spoke with a worried expression. “He’s doing well, right?” “He should be, if he has any sense of shame.” “He still hasn’t fully recovered… He’ll be all right, won’t he?” “Anyone who didn’t know better would think the Third Young Master was on death’s door. At that point, even spit would cure him.” “No. You only say that because you don’t know how frail the youngest has been since childhood.” Wipeng answered with an incredulous look. “The elixirs and tonics that have gone into the Third Young Master alone would be enough to fill an entire room. And have you already forgotten about the hundred-year snow ginseng theft last year?” “Ahem. That was…” “At the time, the Medicine King Hall Master was so furious that he ran around shouting that he was going to cut open the Third Young Master’s stomach. To be honest, even while I was stopping him, I found myself thinking that cutting him open would qualify as self-defense.” Jin Wikyung subtly averted his gaze. The matter had ultimately been settled by compensating the Medicine King Hall out of Jin Wikyung’s personal fortune, but the Hall Master’s fury at the time had been extraordinary. “He swallowed that much elixir. Whatever else may be true, he probably won’t suffer from minor ailments until the day he dies.” “It still isn’t enough. Can’t you tell just by looking at him? Every time I see the youngest, I feel sorry for him. He looks like a skeleton with a few scraps of flesh stuck to it. Every morning he’s so feeble and drained of strength.” “Drained of strength?” Wipeng suddenly remembered a rumor he had heard in the past. Among the courtesans of Taiyuan’s red-light district, Jin Taekyung was supposedly known as the Night King. *Just how impressive is he?* The medicine must have worked properly in at least one respect. Without realizing it, Wipeng raised his forearm and began imagining the size. “What are you doing?” “Ah, nothing.” Jin Wikyung sighed as he looked at the mountain of documents piled before him. “Between the youngest and everything happening inside and outside the family, there’s no end to my worries. Especially… I don’t like that ‘they’ have made contact.” “You mean the Mount Heng Sword Sect.” Mount Heng Sword Sect. The weight of that name was anything but light. Since an undefeated wandering martial artist first hung its signboard decades ago, the sect had grown at a frightening pace. Now, it had become powerful enough to threaten the Jin Family of Taiyuan’s position. “What could their intentions be?” “I’ve sent my subordinates to investigate.” Jin Wikyung fidgeted with the letter from the Mount Heng Sword Sect. Why were they coming? For what purpose? One question led to another, until he arrived at a single conclusion. “Notify every branch in Shanxi. Whatever the Mount Heng Sword Sect’s purpose may be, tell them to make every possible preparation.” This was Murim. Only those who were prepared would survive to see tomorrow. [^1]: In Korean, “gold spoon” is shorthand for someone born into wealth; “God-Spoon” is a pun that escalates the expression.

## Korean source

```text
＃11화



쉬익. 후웅-

허공에서 반짝이는 수십 개의 점을 창끝이 차례차례 관통한다.

한 번의 동작이 끝날 때마다 창날 아래 매달린 붉은 수실이 요동쳤다. 그저 멋으로 달아 놓은 것이 아니라, 적의 시선을 분산시키기 위한 용도다.

팡!

다시 한번 바람이 찢어지는 소리가 들렸다. [진가창법]을 이루는 일곱 개의 초식. 그중 마지막인 천관일(天貫軼)이다.

그리고 이번 천관일은 앞서 성공시킨 아흔아홉 번의 천관일보다 정확하고, 강력했다.

‘이거지.’

손끝이 짜릿하다. 진가창법의 일곱 개 초식은 끊어서 펼쳐도 충분히 파괴적이지만, 이어졌을 때 진정한 효과가 드러난다.

자동차 경주에 비교하자면 일 초식은 시동. 마지막 천관일은 골인이라 할 수 있겠다.

“후.”

더운 숨을 내뱉으며 창을 바로 세운 순간이었다.

띠링.



- 남은 성공 횟수 (100 / 100)

- [진가창법]을 습득했습니다.

- 반복된 수련의 결과로 관련 스탯이 상승합니다!

- 근력, 체력, 민첩이 각각 1씩 올랐습니다.



“오. 스탯 상승.”

이런 방법으로 능력치를 올릴 수도 있구나. 나는 신기해하며 상태창을 띄웠다.

띠링.



상태창



[Lv.11 진태경]

직업 : 이류 무인

명성 : 10

칭호 : 3개 (칭호 효과 적용 중)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 가문의 수치 (모든 능력치 –5, 명성 –50)

- 초보 수련자 (수련 속도 +10%)

근력 : 41체력 : 51

민첩 : 51 지력 : 10

매력 : 10 공력 : 10년

잔여 포인트 : 0





이 정도면…….

“훌륭한 이류 나부랭이네.”

하지만 현실보다는 낫다. 더욱더 위로 올라갈 수 있으니까. F급으로 각성한 날부터 매일매일 느꼈던 한계와 사회가 덮어 놓은 유리천장이 느껴지지 않으니까.

“그럼 뭐 하냐. 마음대로 로그아웃도 못 하는데.”

나는 한숨을 내쉬며 바닥에 주저앉았다. 몇 시간 동안 쉬지 않고 수련했더니 몸이 물먹은 솜처럼 무겁다.

“어이고. 힘들다.”

띠링.



- 당신은 피로와 허기를 느낍니다. 음식물을 섭취하여 몸 상태를 회복시키십시오.



그래. 그럴 것 같더라.

“피로와 허기라.”

답은 휴식밖에 없다. 잘 먹고, 잘 자는 거다. 하지만 태평하게 배나 긁으면서 쉬기에는 시간이 아깝다.

이럴 때 회복 아이템 같은 거라도 하나 있으면…….

“아, 맞다. 벽곡단.”

인벤토리에 넣어 두었던 벽곡단을 꺼냈다. 희한한 냄새를 풍겼지만 찬밥 더운밥 가리면 프로 헌터가 아니다.

나는 입을 크게 벌리고 벽곡단을 한입 가득 베어 물었다.

그리고 생각했다.

‘그냥 뱉을까.’

맛이 없는 정도가 아니다. 혀가 살려 달라고 비명을 지르고 위장이 출입 금지 팻말을 걸 정도의 맛이다.

하지만 인간은 때때로 초인적인 의지를 발휘하는 법. 나는 눈을 질끈 감고 벽곡단을 남김없이 씹어 삼켰다.

꿀꺽.

“으어어. 먹었어. 진짜 먹었어.”

다음 순간 시스템 알림이 울리지 않았다면 한참을 그렇게 뒹굴었을 것이다.

띠링.



- [뛰어난 벽곡단]을 섭취했습니다.

- 당신은 포만감을 느낍니다.

- 피로가 회복됩니다.

- 한 시간 동안 모든 능력치가 2씩 상승합니다.



“뭐?”

황급히 상태창을 열어 보니 공력을 제외한 모든 능력치가 2씩 올라 있었다. 거기에 피로와 허기 회복까지. 나는 쌩쌩한 몸 상태와 포만감을 느끼며 중얼거렸다.

“완전 사긴데?”

더럽게 맛없는 곡물 덩어리에 이런 엄청난 효능이 있을 줄이야. 아니, 잠깐만.

“이거, 중복 효과 있나?”

고작 하나를 먹었는데 총합 10포인트가 올랐다. 두 개, 세 개, 아니 열 개를 먹는다면?

‘저게 고블린 똥이라도 먹어야지.’

왠지 고블린 똥이 더 맛있을 것 같긴 한데…… 확실히 시도해 볼 만한 일이다.

‘할 수 있다. 할 수 있다. 진태경.’

떨리는 손으로 두 번째 벽곡단을 집어 들었다.

그리고 잠시 뒤.



- [뛰어난 벽곡단]을 섭취했습니다.

- 효과가 중복되지 않습니다.

- 당신은 과한 포만감을 느낍니다.

- [과식]의 영향으로 한 시간 동안 움직임이 둔화됩니다!



나는 시스템 알림과 함께 무릎을 꿇었다.

“우웨에에엑!”



* * *



[과식]으로 빵빵해진 배가 겨우 꺼진 뒤에야 다시 수련을 시작할 수 있었다. 수련동에 머무는 시간은 사흘. 그동안 최대한 힘을 키워서 나가야 한다.

“하!”

짧은 기합과 함께 창날이 묵직한 궤적을 그렸다.

‘자세는 낮게, 발은 무겁게, 창은 빠르게.’

진가창법은 공격적이다. 끊임없이 적을 압박하며 나아간다. 창의 궤적은 단순하지만 치명적이다.

‘군대에서 파생되었다고 했나?’

게임의 설정이 어떤지는 몰라도 일개 병졸이 익힐 만한 무공은 아닌 것 같다.

명색이 일류 무공인 데다 펼치려면 상당한 신체 능력이 필요하기 때문이다. 정예병, 혹은 지휘관들이 익혔던 무공이 아니었을까 싶다.

‘헌터 훈련소 시절 배웠던 거랑 비교하면 천지 차이지.’

그런 생각을 했을 때였다. 체력의 고갈인지, 아니면 잡념 때문인지 발이 꼬였다. 발이 꼬이니 손도 흐트러진다. 잔뜩 힘을 머금은 창날이 기세를 잃고 바람을 갈랐다.

쉬익-

시스템이 울린 것도 동시다.



- [진가창법]의 숙련도가 1 오릅니다. (6 / 100)



“겨우 1?”

방금처럼 무공을 처음부터 끝까지 펼칠 때마다 숙련도가 오른다. 시스템의 판정에 따라 얻는 숙련도도 다른데, 이번에는 발이 자주 꼬여서 1이 오른 게 전부였다.

“어떻게 갈수록 못하지?”

습득 후 세 번째로 펼친 진가창법은 점점 형편없어지고 있었다. 처음에 얻은 숙련도는 3. 두 번째는 2. 세 번째인 지금은 1이다.

“삼, 이, 일. 카운트 세는 것도 아니고 뭐야, 이게?”

네 번째는 아예 숙련도를 1도 안 줄 기세다. 나는 한숨과 함께 다시 창을 잡았다. 호흡이 점점 달리는 게 느껴졌지만 다시 진가창법을 펼쳐 냈다.

그리고 사 초식을 펼칠 무렵 균형을 잃고 쓰러졌다.

띠링.



- [진가창법]의 숙련도를 얻지 못했습니다. (6 / 100)



“돌겠네.”

그대로 누워 종유석이 매달린 수련동 천장을 바라봤다.

자꾸 발이 꼬인다. 내가 익힌 그대로 했는데 도대체 왜? 습득할 때도 이런 일은 없었다.

“뭐가 문제지?”

계속 턱, 하고 걸리는 부분이 있다. 그걸 알아내야 한다.

나는 오뚝이처럼 일어나 다시 진가창법을 펼쳤고, 이번에는 삼 초식 만에 넘어졌다.



- [진가창법]의 숙련도를 얻지 못했습니다. (6 / 100)



창이 아니라 발에 집중해서 펼치자 문제점이 희미하게 모습을 드러낸다. 좋아, 한 번 더.



- [진가창법]의 숙련도를 얻지 못했습니다. (6 / 100)



이제 알겠다. 그런데…….

“여기서 진가보법이 왜 튀어나와?”

처음 익힐 때 고생하긴 했다. 한나절 내내 보법만 밟았으니까. 하지만 창법을 펼칠 때 나도 모르게 섞어 쓸 정도냐, 물어보면 그건 아니다.

‘그렇게 따지면 7년 동안 익힌 동작 다 섞었지.’

나도 창술을 배우긴 했다. 헌터 훈련소에 입소하면 기본적으로 배우는 건데, 마나를 사용할 수 없는 F급을 대상으로 보급된 거라 우리끼리는 좆밥 창술이라고 불렀다.

그거에 비하면 진가창법은 중급 헌터용은 된다.

“한번 해 볼까?”

머리 싸매고 생각해 봤자 원형 탈모만 생긴다. 기술은 일단 몸으로 부딪쳐 봐야 아는 법.

나는 천천히 진가창법을 펼치기 시작했다. 그리고 하체로는 진가보법을 펼쳤다.

‘동작이 부자연스러워.’

자꾸만 어긋난다. 하지만 다르다. 지금까지는 실이 뒤죽박죽 얽혀 있었다면 이번에는 톱니바퀴가 미세하게 비껴가는 느낌이랄까. 그렇게 몇 번을 시도했을까.

쉬익- 팡!

단순한 찌르기 동작. 나도 모르는 사이에 마지막 일곱 번째 초식까지 펼쳤나 생각했지만 오 초식의 한 동작이다.

“방금 뭐야?”

등줄기가 찌릿했다. 한순간, 보법과 창법이 완벽하게 맞물린 결과였다. 손에 쥔 창이 부르르 떨렸다.



- [진가창법]의 숙련도를 얻지 못했습니다. (6 / 100)



이제 시스템 알림은 저 구석으로 처박고, 다시 창을 단단히 말아 쥔다. 조금 전의 느낌을 떠올리며 발을 내디뎠다. 그리고 다시 한번.

쉭- 쉬쉭-

이거다. 창을 뻗는 순간 느꼈다. 보법과 창법. 이 두 톱니바퀴가 정확히 맞물린다.

이루 말할 수 없는 쾌감에 휩싸여 두 개의 톱니바퀴를 굴리고, 또 굴렸다. 내딛는 걸음이, 찌르고 베고 휘두르는 창날이 빠르고 정확했으며 강했다.

단전이 뜨겁다. 공력은 하나의 불덩어리가 되어 창에 스며들었다. 토해 내야 했다.

바로 지금!

“합!”

천관일. 하늘을 뚫는다는 진가창법의 마지막 일격이 뻗어 나갔다. 먹먹한 굉음이 터져 나왔다.

쾅-!

먼지가 피어오르고 돌이 사방으로 비산한다. 수련동의 벽에 박힌 창이 몸을 떨었다. 깊숙이 박혀 보이지도 않는 창날을 중심으로 커다란 구멍이 생성되어 있었다.

구멍? 아니다. 이건 크레이터다. 숨 막히는 광경이다.

“헉, 헉…….”

쾌감에 등골이 오싹했다. 시발, 나야. 내가 해냈다고!

트롤도 한 방에 끝장낼 수 있는 저런 미친 일격을 내가……!

휘청.

‘어?’

떠나가라 소리를 지르고, 인증 사진도 찍어야 하는데. 쌀벌레라고 놀리던 진호 형 코를 납작하게 만들어 줘야 하는데.

‘아, 여기. 게임이었지.’

눈앞이 흐릿하다. 몸에 힘이 빠진다. 견딜 수 없는 졸음이 밀려와 나를 덮쳤다.

‘졸려.’

나는 생각하는 것을 멈추고 본능에 몸을 맡겼다. 어디선가 많이 듣던 소리가 아스라이 멀어진다.

띠링. 띠링. 띠링.

.

.

.

- 공력이 모두 소진되었습니다.

- 극도의 피로감을 느낍니다.

- 업적, [물아일체]를 달성하셨습니다. 보상이 주어집니다!

- 무공의 연계를 스스로 깨달았습니다. 보상으로 무공의 경지가 크게 상승합니다.

- [진가심법]의 경지가…….

- [진가보법]의 경지…….

- [진가창법]의…….

- 레벨 업!

- 레벨 업!



* * *



- 수면 모드가 종료되었습니다.



눈을 떴다. 종유석이 매달린 동굴 천장이 보인다.

‘수련동.’

얼마나 기절해 있었던 걸까. 반나절? 아니면 하루?

모르겠다. 중요한 건 내가 아직 게임 속이고, 충분히 쉬었다는 사실이다.

‘컨디션도 최상이고.’

이상할 정도로 몸 상태가 좋다. 그러고 보니 기절하기 직전에 시스템 알림을 들었던 것도 같다.

“메시지창 오픈.”

다음 순간 확인 안 한 메시지들이 시야를 가렸다. 메시지를 다 읽고 생각을 정리했을 때는 십여 분이 훌쩍 흐른 뒤였다. 나는 짧게 소감을 중얼거렸다.

“대박 났네.”

진가보법, 창법은 삼 성으로 무려 두 단계나 뛰었고 진가심법은 이 성으로 올랐다. 거기에 더해…….

“2레벨이나 올랐다고?”

기쁘면서도 얼떨떨하다. 사실 수련동에서 레벨을 올릴 수 있으리란 기대는 거의 하지 않았기 때문이다.

“보통 퀘스트 깨거나 몬스터를 잡아야 오르는 거 아니었어?”

무공을 익히고 지금처럼 어떤 깨달음을 얻는 것으로도 레벨 업이 된다니. 게임 장르가 무협이라 그런가? 확실히 종잡을 수가 없다.

“아, 어쩐지 몸이 가뿐하더라.”

레벨 업 효과로 몸이 회복된 모양이다. 레벨 업 전까지 남아 있던 타박상과 약간의 통증도 모두 깨끗이 사라져 있었다.

“상태창 오픈.”

상태창에도 변화가 있었다. 13레벨로 오르면서 스무 개의 잔여 포인트를 얻었고, 수련의 영향으로 근력, 체력, 민첩이 소량 오른 상태다.

“13레벨이라.”

퀘스트 완료 조건은 일류 경지와 레벨 30, 명성 500 달성.

빠르지는 않지만 수련만으로도 착실히 레벨을 올리고 있으니 순항하고 있는 셈이다.

‘수련동만 나가면 돛을 피고 쭉쭉 나아가는 거지.’

나는 흐뭇하게 웃으며 포인트를 분배했다.

이제 [물아일체]의 업적을 이루면서 받은 보상 확인만이 남았다.

“인벤토리 오픈.”



- 신규 아이템이 1개 존재합니다. 확인하시겠습니까?



어, 내놔.
```

## Current accepted English baseline

```markdown
# Chapter 11

Whoosh. Fwoom—

The spearhead pierced dozens of sparkling points in the air one after another.

Each time I completed a form, the red tassel hanging beneath the spearhead whipped around. It wasn’t just for show; it was meant to draw the enemy’s eye.

Bang!

Again, the sound of wind being torn apart rang out. It was the seventh and final form of the Jin Family’s Spear Technique: the Sky-Piercing Strike.

This Sky-Piercing Strike was more precise and powerful than the ninety-nine I had successfully performed before it.

*This is it.*

My fingertips tingled. Each of the seven forms in the Jin Family’s Spear Technique was destructive enough when performed separately, but its true effect emerged when they flowed together.

If I compared it to a car race, the first form was starting the engine. The final Sky-Piercing Strike was crossing the finish line.

“Whew.”

I exhaled a hot breath and raised the spear upright.

Ding.

> **System**
>
> - Successful attempts: (100 / 100)
>
> - You have acquired **Jin Family’s Spear Technique**.
>
> - As a result of repeated training, related stats have increased!
>
> - Strength, Stamina, and Agility have each increased by 1.

“Oh. My stats went up.”

So this was another way to improve my stats. Intrigued, I opened my Status Window.

Ding.

> **System**
>
> **Status Window**
>
> **Lv. 11 Jin Taekyung**
>
> **Occupation:** Second Rate Martial Artist
>
> **Fame:** 10
>
> **Titles:** 3 (Title effects active)
>
> - **Child of a Prestigious Family:** All stats +5, Fame +50
>
> - **Shame of the Family:** All stats –5, Fame –50
>
> - **Novice Trainee:** Training speed +10%
>
> **Strength:** 41  
> **Stamina:** 51
>
> **Agility:** 51  
> **Intelligence:** 10
>
> **Charm:** 10  
> **Internal Energy:** 10 years
>
> **Remaining Points:** 0

This was…

“What a fine second-rate nobody.”

Still, it was better than reality. I could keep climbing higher. I no longer felt the limitations I’d sensed every day since awakening as an F-rank, or the glass ceiling society had placed over me.

“So what? I can’t even log out whenever I want.”

I sighed and sank to the floor. After several hours of nonstop training, I felt as heavy as a waterlogged cotton blanket.

“Ow. I’m exhausted.”

Ding.

> **System**
>
> - You feel fatigued and hungry. Consume food to restore your physical condition.

Yeah. I figured that would happen.

“Fatigue and hunger…”

The only answer was rest. Eat well and sleep well. But I didn’t have time to lie around leisurely scratching my belly.

If only I had some kind of recovery item…

“Oh, right. Grain-repelling pills.”

I took one of the grain-repelling pills from my inventory. It gave off a strange smell, but a professional Hunter couldn’t afford to be picky about whether his rice was hot or cold.

I opened my mouth wide and took a huge bite.

Then I thought,

*Should I just spit it out?*

It wasn’t merely tasteless. It tasted bad enough that my tongue screamed for mercy and my stomach hung up a no-entry sign.

Every now and then, humans could summon superhuman willpower. I squeezed my eyes shut, chewed the grain-repelling pill thoroughly, and swallowed every last bit.

Gulp.

“Uuugh. I ate it. I actually ate it.”

If the System notification hadn’t sounded the next moment, I probably would have kept rolling around on the floor for quite a while.

Ding.

> **System**
>
> - You have consumed an **Excellent Grain-Repelling Pill**.
>
> - You feel full.
>
> - Your fatigue has been restored.
>
> - All stats increase by 2 for one hour.

“What?”

I hurriedly opened my Status Window. Every stat except Internal Energy had increased by 2. On top of that, my fatigue had lifted and my hunger was gone.

Feeling energized and full, I muttered,

“This is completely broken.”

Who would have thought such a foul-tasting lump of grain could have such incredible effects? Wait a second.

“Do the effects stack?”

Just one had increased my stats by a total of 10 points. What if I ate two? Three? No, ten?

*I’d eat goblin shit if I had to.*

Goblin shit might actually taste better… but it was definitely worth a try.

*I can do this. I can do this. Jin Taekyung.*

With trembling hands, I picked up a second grain-repelling pill.

And a short while later—

> **System**
>
> - You have consumed an **Excellent Grain-Repelling Pill**.
>
> - The effects do not stack.
>
> - You feel excessively full.
>
> - Your movements will be slowed for one hour due to **Overeating**!

I dropped to my knees as the System notification sounded.

“Bleaaargh!”

* * *

I could only resume training after my bloated stomach finally went down. I had three days to stay in the training hall. I needed to grow as strong as possible before leaving.

“Hah!”

With a short battle cry, the spearhead traced a heavy arc.

*Keep my stance low, my feet heavy, and my spear fast.*

The Jin Family’s Spear Technique was aggressive, constantly advancing while pressuring the enemy. Its spear movements were simple but lethal.

*Was it derived from the military?*

I didn’t know what the game’s setting was, but it didn’t seem like a martial art an ordinary foot soldier could learn.

After all, it was a first-rate martial art and required considerable physical ability to perform. Perhaps it had been practiced by elite soldiers or commanders.

*Compared with what I learned at the Hunter training camp, it’s like heaven and earth.*

That was when my foot tangled—whether from exhaustion or distraction, I wasn’t sure. Once my foot got tangled, my hands lost their rhythm too. The spearhead, loaded with strength, lost its momentum and sliced through the air.

Whoosh—

The System sounded at the same time.

> **System**
>
> - Jin Family’s Spear Technique Mastery increased by 1. (6 / 100)

“Only 1?”

My Mastery increased each time I performed the martial art from beginning to end. The amount I gained depended on the System’s evaluation, and this time, all I got was 1 because my feet had tangled so often.

“Why am I getting worse the more I do it?”

The third time I performed the Jin Family’s Spear Technique after acquiring it, I was getting worse and worse. The first time, I gained 3 Mastery. The second time, 2. This third time, 1.

“Three, two, one. It’s not even a countdown. What is this?”

The fourth attempt looked like it would yield no Mastery at all. I sighed and took hold of the spear again. My breathing was becoming increasingly ragged, but I performed the Jin Family’s Spear Technique once more.

Around the fourth form, I lost my balance and fell.

Ding.

> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

“This is driving me insane.”

I lay there and stared at the training hall’s ceiling, where stalactites hung overhead.

My feet kept getting tangled. I was performing the technique exactly as I had learned it, so why was this happening? Nothing like this had happened when I acquired it.

“What’s the problem?”

Something kept throwing me off. I had to figure out what it was.

I got back up like a roly-poly and performed the Jin Family’s Spear Technique again. This time, I fell after only the third form.

> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

When I focused on my feet instead of the spear, the problem started to come into focus.

Good. One more time.

> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

Now I understood. But…

“Why is the Jin Family’s Manoeuvre Technique showing up here?”

I had struggled when I first learned it. I’d spent half a day practicing nothing but footwork. But if you asked whether it was enough to make me unconsciously mix it into my spear technique, the answer was no.

*If that were the case, I’d have mixed in every movement I’ve learned over seven years.*

I had learned spear fighting before, too. It was one of the basics taught at the Hunter training camp. Since it was distributed to F-ranks who couldn’t use mana, we called it shitty spear fighting among ourselves.

Compared with that, the Jin Family’s Spear Technique was good enough for intermediate Hunters.

“Should I give it a try?”

No matter how hard I racked my brain, all I’d get was a bald spot. The only way to understand a technique was to try it with my whole body.

I began performing the Jin Family’s Spear Technique slowly. At the same time, I performed the Jin Family’s Manoeuvre Technique with my lower body.

*The movements don’t flow naturally.*

They kept falling out of sync. But it was different. Until now, it had felt as if tangled threads were being pulled in every direction. This time, it felt as if gears were slipping past each other by a hair.

How many times had I tried?

Whoosh—Bang!

It was a simple thrust. For a moment, I wondered if I had performed all the way through the seventh and final form without realizing it, but it was only one movement from the fifth form.

“What was that?”

A shiver ran down my spine. For one brief moment, the footwork and spear technique had meshed perfectly. The spear in my hand trembled.

> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

I shoved the System notification into a corner of my mind and tightened my grip on the spear. Recalling the sensation from a moment ago, I stepped forward.

And again.

Swish—Whoosh—

*This is it.*

I felt it the instant I thrust the spear. The footwork and the spear technique. The two gears meshed perfectly.

Overwhelmed by indescribable pleasure, I turned those two gears again and again. My steps were fast and precise. The spearhead that thrust, slashed, and swung was fast, precise, and powerful.

My dantian grew hot. My internal energy became a ball of fire and seeped into the spear.

I had to release it.

*Right now!*

“Hah!”

The Sky-Piercing Strike—the final blow of the Jin Family’s Spear Technique, said to pierce the heavens—shot forward.

A deep, muffled boom erupted through the cavern.

Bang!

Dust rose, and stones scattered in every direction. The spear embedded in the training hall’s wall trembled. A massive hole had formed around the spearhead, which had plunged so deeply that it was no longer visible.

A hole? No.

This was a crater.

The sight was breathtaking.

“Huff, huff…”

The exhilaration sent a shiver down my spine.

*Fuck, it was me. I did it!*

I had unleashed that insane strike—the kind that could take down a troll in one blow.

Me!

I staggered.

*Huh?*

I needed to shout my head off and take a proof photo. I needed to put Big Brother Jinho in his place—he used to call me a freeloader.

*Oh, right. This was a game.*

My vision blurred. The strength drained from my body. An unbearable wave of sleepiness washed over me.

*I’m sleepy.*

I stopped thinking and surrendered my body to instinct. A familiar sound gradually faded into the distance.

Ding. Ding. Ding.

.

.

.

> **System**
>
> - All internal energy has been depleted.
>
> - You feel extreme fatigue.
>
> - You have completed the achievement **Unity of Self and Object**. A reward will be granted!
>
> - You have realized the connection between martial arts on your own. As a reward, the realms of your martial arts will rise substantially.
>
> - The realm of **Jin Family’s Cultivation Technique**…
>
> - The realm of **Jin Family’s Manoeuvre Technique**…
>
> - The realm of **Jin Family’s Spear Technique**…
>
> - Level up!
>
> - Level up!

* * *

> **System**
>
> - Sleep mode has ended.

I opened my eyes. The cave ceiling, with stalactites hanging from it, came into view.

*The training hall.*

How long had I been unconscious? Half a day? Or a full day?

I didn’t know. What mattered was that I was still in the game and had gotten plenty of rest.

*I feel great, too.*

My physical condition was strangely excellent. Come to think of it, I seemed to have heard System notifications just before I passed out.

“Open Message Window.”

The next moment, unread messages covered my vision. By the time I finished reading them all and sorting through my thoughts, more than ten minutes had passed.

I muttered a brief reaction.

“I really hit the jackpot.”

The Jin Family’s Manoeuvre Technique and Spear Technique had risen all the way to the Third Stage—two whole stages. The Jin Family’s Cultivation Technique had reached the Second Stage.

And on top of that…

“I went up two Levels?”

I was happy, but also bewildered. I hadn’t seriously expected to Level up in the training hall.

“Don’t you usually Level up by completing Quests or killing monsters?”

Apparently, learning martial arts and gaining insight like I had could also lead to a Level Up. Was it because this was a martial-arts game? It was definitely impossible to predict.

“No wonder my body felt so light.”

The Level Up effect must have restored my condition. The bruises and slight pain that had remained before I leveled up had vanished completely.

“Open Status Window.”

The Status Window had changed too. Reaching Level 13 had given me twenty remaining points, and the effects of training had slightly increased my Strength, Stamina, and Agility.

“Level 13…”

The Quest completion requirements were reaching the first-rate realm, Level 30, and 500 Fame.

I wasn’t progressing quickly, but I was steadily leveling up through training alone. That meant I was cruising along.

*Once I leave the training hall, I can spread my sails and surge forward.*

I smiled contentedly and distributed my points.

Now, all that remained was to check the reward I’d received for completing the Unity of Self and Object achievement.

“Open Inventory.”

> **System**
>
> - You have 1 new Item. Would you like to check it?

Yeah. Give it here.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 11`.

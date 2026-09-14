# Checkpoint Review — 385–389

Review only this bounded packet. Check the English reading copies, summaries,
and active state for voice drift, terminology drift, dropped hooks, formatting
differences, internal contradiction, and accidental spoilers. Do not redo the
source-fidelity reviews and do not rewrite files. Return exactly one JSON object
using the chapter-review schema: summary plus a findings array. Use stable IDs
`C01`, `C02`, and so on; source identifies the chapter/location, current quotes
one exact uniquely occurring English span, replacement supplies finished text,
and confidence is 0 through 1. Use an empty findings array when nothing is
actionable.

Return this exact shape with no Markdown fence:

{
  "summary": "brief assessment",
  "findings": [
    {
      "id": "C01",
      "severity": "critical|major|minor",
      "source": "chapter and location",
      "current": "exact current English",
      "defect": "specific defect",
      "replacement": "finished exact replacement English",
      "rationale": "specific reason",
      "confidence": 0.0
    }
  ]
}

## Binding rules

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

## Checkpoint summary

# Chapters 385–389

## Plot

Jin Taekyung clashes verbally with Wu Heixing, an arrogant S-rank Hunter whose anti-Korean slurs and jealousy escalate the tension. Pai Chen intervenes, while Taekyung publicly mocks Wu’s drug and sexual-assault scandals. Prince Felix Alexander Louis further irritates the group with his elaborate royal etiquette and condescending treatment of commoners. Wei Penghu then arrives with Lee Jungryong, whose presence immediately draws Taekyung’s attention.

Lee recognizes that Choi Minwoo has grown dramatically and that Taekyung has crossed the wall. During the ensuing strategy meeting, Senior General Liao proposes using nuclear weapons against the Sichuan monster wave, but Wei Penghu rejects the plan because of the danger to survivors, the land, and possible magical teleportation. Six S-rank Hunters are assigned to separate fronts, each supported by military divisions and Public Security Armed Forces Hunters. An unidentified person contacts Taekyung through Sound Transmission.

The sender is Wu Heixing, who lures Taekyung into a forest and attacks him with a sword and martial-arts techniques. Taekyung decisively defeats him, takes his Supreme Potion as compensation, and gives him an Advanced Potion. Meanwhile, Team Leader Choi, Pai Chen, and Magic Johnson prepare to deploy; Choi agrees to a nine-to-one settlement split after Taekyung rescued him from their drinking-game predicament. Lee later approaches Wu in the darkness to request a private discussion, but its subject is not revealed.

An Unexpected Quest, **The Battle Situation Has Become Critical**, orders Taekyung to reach the battlefield quickly and defeat the enemies. Felix departs before dawn after receiving a battle signal. Chairman Xiao Yang announces the disaster to the United Nations Security Council, and China remains under martial law as UN-approved peacekeeping forces join the fighting.

Four days into the full-scale battle, the monster army has exceeded 100,000, communications and satellite surveillance remain disrupted, and the western front is breached by a rapid monster advance. Taekyung, Choi, and Shao Shen remain deployed there. Shao Shen commands more than a thousand Public Security Armed Forces Hunters and, after receiving permission, addresses Taekyung as hyung-nim. Taekyung leads the countercharge with Flamefire Path, White Flame, and Extreme Yang force.

## Continuity

- Jin Taekyung is a Supreme Peak martial artist who has crossed the wall. His exact Level, Fame, complete Titles, martial-art stages, and unassigned points remain unstated.
- Taekyung is cooperating with China to stop the Sichuan disaster and locate Lei Fei and the missing Sichuan Hunters.
- The six S-rank Hunters were assigned to six fronts, with three Army and Air Force divisions and Public Security Armed Forces Hunters attached to each.
- China is under martial law, and UN-approved peacekeeping forces are fighting on the front.
- The monster army exceeds 100,000, is centered around an Arch Lich, and is supported by magical interference that disrupts communications and satellite surveillance.
- The east-west front was breached, but Pai Chen prevented the damage from spreading. The western-front breach is a monster advance through the enemy line, not the collapse of Taekyung’s position.
- Taekyung and Team Leader Choi have fought on the western front for four days of full-scale battle.
- Shao Shen is twenty-one, commands more than a thousand Public Security Armed Forces Hunters, follows Taekyung’s battlefield orders, and now calls him hyung-nim.
- Wei Penghu remains Senior General and Minister of Defense at the Central Military Commission. He raised his missing nephew Lei Fei as his son.
- Xiao Yang remains Chairman of the Central Military Commission, General Secretary, and state chairman of China, retaining overall authority over the crisis.
- Lee Jungryong leads Ares Guild in practice and is one of the world’s three strongest S-rank Hunters. He recognizes Choi Minwoo’s growth and Taekyung’s breakthrough.
- Wu Heixing is an S-rank Hunter from a powerful Communist Party family. He is arrogant, volatile, status-conscious, and considers the missing Lei Fei an insurmountable rival.
- Wu knows Sound Transmission and martial arts. Taekyung defeated him after Wu initiated the attack, taking his Supreme Potion and leaving him with an Advanced Potion.
- Pai Chen is an S-rank Hunter, Great Cataclysm hero, and former romance-film actress who appears far younger than her actual age.
- Magic Johnson is an S-rank Hunter, one of the world’s three Archmages, and a combat-specialized War Mage.
- Prince Felix Alexander Louis is third in line to the British throne and holds multiple senior British titles; William is his formal attendant.
- The subject and consequences of Lee Jungryong’s private discussion with Wu Heixing remain unresolved.
- Lei Fei’s fate, the missing Sichuan Hunters’ fate, the western-front battle’s outcome, Wu’s reason for contacting Taekyung, and the monster wave’s larger plan remain unresolved.
- The Arch Lich’s identity, its relationship to the earlier Lich, the reason for the mana surge, and the full extent of the Skeleton Warlord’s increased power remain unresolved.
- Dark Heaven, the hidden transport formation, the Sichuan Tang Clan’s relocation, Mungyeong’s response, Dongbong’s request, Ae-hyang’s superior, and the Chengdu port boy remain unresolved.

## Translation Decisions

- Preserve **Jin Taekyung**, **Team Leader Choi**, **Lee Jungryong**, **Lei Fei**, **Wei Penghu**, **Pai Chen**, **Wu Heixing**, **Shao Shen**, **Magic Johnson**, **Prince Felix Alexander Louis**, and **William**.
- Render **전음** as **Sound Transmission**, **검강** as **Sword Force**, **상급 포션** as **Advanced Potion**, and **최상급 포션** as **Supreme Potion**.
- Render **다급해진 전황** as **The Battle Situation Has Become Critical** and **유엔 안전보장이사회** as **United Nations Security Council**.
- Render **대마법사** as **Archmage** and **워 메이지** as **War Mage**.
- Retain **hyung-nim** for Shao Shen’s address to Taekyung, **Sibeol-jwa**, **Flamefire Path**, **White Flame**, and **Extreme Yang**.
- Preserve the established **bangzi** footnote and the source’s offensive insult exchange, conversational self-mockery, drinking-game wordplay, and Felix’s ceremonial satire.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is a Supreme Peak martial artist who has crossed the wall; his exact current level, Fame, complete Titles, martial-art stages, and unassigned points remain unstated.",
    "Taekyung has returned to the modern world and is working with Chinese authorities to stop the monster disaster while seeking Lei Fei and the missing Sichuan Hunters.",
    "Sichuan Province remains in a wartime state after the monster wave began in Gaoping District, Nanchong City.",
    "China has declared martial law, and UN-approved peacekeeping forces have joined the front.",
    "Wei Penghu is a Senior General and Minister of Defense at the Central Military Commission; he raised his missing nephew Lei Fei as his own son.",
    "Xiao Yang is Chairman of the Central Military Commission, General Secretary, and state chairman of the People's Republic of China, and retains full authority over the crisis response.",
    "Team Leader Choi trusts Taekyung, was rescued by him from a drinking-game predicament, and agreed to adjust Taekyung's settlement share to nine-to-one.",
    "The six S-rank Hunters were assigned to six fronts; Prince Felix left before dawn after receiving a battle signal.",
    "Magic Johnson is an S-rank Hunter, one of three Archmages worldwide, and a combat-specialized War Mage.",
    "Pai Chen is an S-rank Hunter, Great Cataclysm hero, and former romance-film actress who appears much younger than her actual age.",
    "Wu Heixing is an S-rank Hunter from a powerful Chinese Communist Party family; he is arrogant, volatile, status-conscious, and regards the missing Lei Fei as an insurmountable rival.",
    "Prince Felix Alexander Louis is a British prince, third in line to the throne, and holds multiple senior British titles; William serves as his formal attendant.",
    "The Sichuan Tang Clan was devastated by Dark Heaven, owes Taekyung's group a debt, and is considering relocation.",
    "The Chengdu International Airport attack involved an undead army controlled by three incomplete Arch Liches, all of whom Taekyung destroyed.",
    "The Skeleton Warlord absorbed the death energy of the remaining two Arch Liches and became much stronger, but the persistence and full extent of that increase remain unknown.",
    "Dark Heaven's agents, purpose, and connection to the hidden transport formation remain unresolved.",
    "Lee Jungryong is the practical leader of Ares Guild and one of the world's top three S-rank Hunters; he recognizes Choi Minwoo's growth and that Jin Taekyung has crossed the wall.",
    "Wu Heixing used Sound Transmission and possesses martial-arts knowledge; Taekyung defeated him after he attacked, taking his Supreme Potion and leaving him with an Advanced Potion.",
    "An unrefusable Unexpected Quest, The Battle Situation Has Become Critical, orders Taekyung to reach the battlefield quickly and defeat the enemies.",
    "The monster army has exceeded 100,000, and the western front has been breached by a rapid monster advance while Jin Taekyung's force remains engaged."
  ],
  "continuity_sources": [
    389
  ],
  "open_questions": [
    "The outcome of Taekyung's spar with Jin Mukyung remains unresolved.",
    "Dark Heaven's larger purpose, its reason for sparing Taekyung, and the origin and function of the hidden transport formation remain unresolved.",
    "The Sichuan Tang Clan's relocation decision and destination, along with the timing and outcome of the Samgoe escort to Henan, remain unresolved.",
    "The request Dongbong wants to make of Taekyung, Mungyeong's eventual response to the coming war, and the identity and fate of the boy from the Chengdu port remain unresolved.",
    "Ae-hyang's superior and the consequences of the Sichuan Governor's false memorial remain unresolved.",
    "The relationship between the Lich and the Arch Lich, the full extent of the Skeleton Warlord's increased power, and the monster wave's larger plan remain unresolved.",
    "Lei Fei's fate and the fate of the missing Sichuan Hunters remain unresolved.",
    "The subject and consequences of Lee Jungryong's discussion with Wu Heixing, Wu Heixing's reason for sending the Sound Transmission, and the outcome of the western-front battle remain unresolved."
  ],
  "safe_through": 389,
  "temporary_decisions": [
    "Render Zhonghua as Zhonghua and preserve the Jongseok mishearing joke for 총서기.",
    "Render Xiao Yang's offices as Chairman of the Central Military Commission, General Secretary, and state chairman.",
    "Render 대마법사 as Archmage and 워 메이지 as War Mage.",
    "Retain Teacher Jin for 진 선생 and Comrade Chairman for 주석 동지.",
    "Render 반도의 빵즈 as peninsula bangzi and retain the derogatory-slur footnote.",
    "Preserve Taekyung's conversational, self-mocking first-person voice and the source's jokes, including the forum's exaggerated online register.",
    "Render established names and titles consistently, including Pai Chen, Wu Heixing, Prince Felix Alexander Louis, William, Senior General Liao, the Princelings, the Shanghai clique, Sound Transmission, Sword Force, Advanced Potion, and Supreme Potion.",
    "Render 다급해진 전황 as The Battle Situation Has Become Critical, 유엔 안전보장이사회 as United Nations Security Council, 형님 as hyung-nim for Shao Shen's address to Jin, and 정 드래곤 as Jung Dragon."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 385

# Chapter 385

“Isn’t that right, you peninsula bangzi?”[^1]

“What are you saying, you mainland chink bastard?”

A heavy silence descended.

Even with translation magic, foreigners like Magic Johnson had no idea exactly what *bangzi* and *chink* meant, leaving them bewildered. Team Leader Choi clicked his tongue quietly, while one man’s face hardened like stone.

“What?”

“What, asshole?”

“Say that again, bangzi.”

“Sure. Chink.”

“You fucking—”

“Fine. Let’s get this straight. I’m a dog. You’re a chink.”

“…!”

I watched his face twist violently. Just as he was about to shove back his chair and leap to his feet, the woman sitting beside him raised a hand to stop him.

“Enough.”

She was a beautiful woman in her early twenties, with an air as clean and refreshing as a soft drink. A calm voice continued from between her lips.

“I’d appreciate it if you both toned it down.”

*Tone it down, huh…*

I stared at her for a moment, then shrugged.

“Sure, if you insist.”

Perhaps my unexpected answer had caught her off guard. Her eyebrows curved slightly.

“I heard you weren’t easy to deal with, but you’re accepting it more readily than I expected.”

“I have to accept it. It’s your request, after all.”

“You fell for the beauty trap? Ah, this is why being pretty is such a hassle.”

When she nonchalantly swept back her long hair, I let out a quiet laugh.

“Did you just laugh?”

“You seem more interesting than I expected, Ms. Pai Chen.”

Pai Chen. That was her name.

I couldn’t let myself be fooled by the looks and atmosphere of someone who could have been a university cover model. She might not have married, but she was well past fifty.

She was also a Senior from a generation far beyond mine—and one of the heroes of the Great Cataclysm.

“So you knew who I was from the start. Hmm. I thought kids these days might not recognize me.”

That wasn’t wrong. Compared to other S-rank Hunters, Pai Chen had definitely appeared in the media far less often.

Behind the scenes, it wasn’t uncommon to hear that she had assumed a new identity and begun a new life.

But I had known about her since I was little.

“My mother’s been a fan of yours for years. You starred in that romance movie that came out about twenty years ago, didn’t you?”

“Oh my. How long ago was that? Still, it’s nice to meet someone who remembers.”

“Would it be all right if I came to get your autograph sometime? I think my mother would love it if I brought her one from you.”

“Of course. And from now on, just call me Chen. My full name sounds too stiff. If you want to be more casual, you can call me *older sister*.”

“Excuse me? What are you talking about? I looked you up online, and you’re five years older than my mother.”

“……You really aren’t easy to deal with. Just as I heard.”

But there was someone else who was truly not easy to deal with.

“You fucking turtle-dick…!”

His voice boiled over. The man who had briefly been forgotten amid our conversation glared at me with furious eyes.

“How dare a bangzi from some weak little country look down on me? Do you even know who I am?”

“…Wow. That line was fucking terrible.”

Pai Chen rested her chin on her hand, looking back and forth between us with interest.

“Indeed. I’ve been wondering since earlier—do you even know who this boy is?”

Pai Chen wasn’t the only one who wanted to hear my answer.

Everyone was staring at my mouth except Team Leader Choi, whose expression had reached a state of near enlightenment.

The man huffing and puffing like a seven-year-old who had lost an argument, Magic Johnson, America’s Archmage, and even the young man from Britain. Their attendants were no exception.

Under everyone’s gaze, I nodded.

“Of course I do. Wu Heixing.”

He competed for first or second place in media exposure even among S-rank Hunters, so there was no way I wouldn’t know him.

At my answer, the man who had been picking a fight with me about bangzi since earlier—Wu Heixing—widened his eyes.

“You knew who I was, and you still acted that way?”

“Even a stray dog passing by would know there’s one complete piece of human trash among the S-rank Hunters.”

“W-What did you say?”

“Why? Who doesn’t know that your hobby is getting attention and your specialty is committing crimes, then working the media afterward?”

“…!”

“Come to think of it, didn’t you cause trouble last year? You uploaded a raid photo on your official social media with some bullshit about ‘the only drug my country allows me.’ Then a month later, you got caught taking actual drugs. Was it marijuana?”

“Mr. Jin Taekyung.”

“Team Leader Choi, don’t stop me.”

“It wasn’t marijuana.”

“Huh?”

Team Leader Choi cut in abruptly and calmly corrected the Taekyung Wiki.

“It was cocaine and methamphetamine.”

“Oh, I see. Thank you for letting me know.”

“You’re welcome. Now that things have come this far, what’s left that we can’t say?”

Look at that enlightened expression.

Leaving Team Leader Choi behind as he seemed to be giving up on everything and preparing to ascend to immortality, I continued speaking to Wu Heixing with a broad smile.

“Damn, how did you think of setting up foreshadowing like that? This bastard is Wu Heisunwon at minimum. *Purple Raid*.”

“W-What did you say?”

“Come to think of it, there’s another one. Five years ago, you got caught sexually assaulting someone after drugging them at some club called Burning Moon. How did you get acquitted? Under Chinese law, for something like that, it wouldn’t have been strange if you’d been executed two or three times.”

“…!”

“I heard rumors that you’re the son of someone at the very top of the Communist Party. Did you buy your way out with money and power? Look at this clever bastard.”

“Sh-Shut your mouth! How dare a lowborn bangzi speak to me that way!”

Wu Heixing’s face flushed bright red as he shouted. Then someone who had been quietly watching the entire situation opened his mouth.

“You’re loud.”

An arrogant voice flowed smoothly through the room.

“Frivolous and vulgar. I hear you’re descended from a Chinese aristocratic family. Did the elders of your house never teach you proper etiquette?”

Wu Heixing bit his lip when he recognized the speaker.

“Y-You’re…”

“You’re?”

Faintly green eyes beneath neatly groomed brown hair swept slowly over Wu Heixing, then moved away.

“William.”

At the young man’s call, a middle-aged man with half-gray hair stepped forward from behind him.

His shoes were spotless, his suit pressed sharp as a blade. He stood tall, surveyed the room, and spoke in a pleasing baritone.

“Everyone, rise and pay your respects to His Royal Highness Prince Felix Alexander Louis, Duke of Cambridge, Earl of Strathearn, Baron Carrickfergus, Knight of the Garter, and Knight of the Thistle.”

*The Duke of Cambridge and the Earl of Strath… Fuck, why are his titles so long?*

Anyway, Prince Felix-whatever sternly added,

“Everyone, just call me His Royal Highness Prince Felix.”

“…”

“…”

Look at everyone’s faces. They looked more uncomfortable than anyone else in the world.

Naturally, the most spectacular reaction came from Wu Heixing, who had just called me a lowborn commoner.

And why wouldn’t it? If this came down to social status, how was he supposed to beat a member of the British royal family?

“S-So, this is…”

“Ah.”

Prince Felix looked at the flustered Wu Heixing and nodded as if he had just understood.

“I see. Are you a stutterer?”

“A st-stutterer?”

“If not, why can’t you speak properly? Did your family fail to provide you with speech training?”

Long live His Royal Highness the Prince.

I didn’t even have to step in myself. The third in line to the British throne was injecting carbonation straight into me, and I could feel it fizzing all the way down to my duodenum.

I was grinning so hard my mouth threatened to split when Prince Felix suddenly turned his gaze on me.

“You.”

“Hm? You mean me?”

At my question, the middle-aged man standing behind Prince Felix opened his mouth.

“When His Royal Highness Prince Felix Alexander Louis, Duke of Cambridge, Earl of Strathearn, Baron Carrickfergus, Knight of the Garter, and Knight of the Thistle, deigns to ask you a question—”

“That will do, William.”

Prince Felix raised a hand and cut off the parrot. Then he gazed at me with benevolent eyes.

“I have cast aside my dignity and personally intervened because I have always believed that the barriers between social classes must be broken down.”

“…?”

“What does it matter whether one is a commoner or a noble? We are all simply equal people beneath God. So don’t let that man’s words hurt you too much.”

*What the fuck is he talking about?*

I was momentarily at a loss for words when Team Leader Choi whispered discreetly.

“I believe he thinks you’re a commoner.”

“…!”

*Has that prince bastard lost his mind?*

As I stared at Prince Felix with an incredulous expression, he slowly rose from his seat and extended the back of his hand toward me as if it were the most natural thing in the world.

“Well, go on.”

“…Go on? What is it this time?”

The middle-aged man—whether he was a secretary or a parrot, I couldn’t tell—spoke with a pleased smile.

“Kiss the back of his hand and express your gratitude for the benevolence His Royal Highness Prince Felix Alexander Louis has shown you.”

“…”

*Are these people complete lunatics?*

*Did these eighteenth-century fuckers all arrive here in a time capsule?*

My head was still reeling when a message spell from Team Leader Choi reached my ear.

- No.

I replied through Sound Transmission.

- What do you mean, no?

- In any case, no. Just smile and let it pass. Prince Felix is famous for being a bit of an oddball.

- If I break the back of his hand right now, wouldn’t that make him even more famous?

- No. Absolutely not!

- Just a little damage to the back of his hand. Or even just one finger.

- I said no!

I hadn’t known Message Magic could carry this much emotion. Team Leader Choi must have been desperate in his own way.

*Fine. He’s a British prince. It can’t be helped.*

I was trying to swallow my anger when—

“Hey, Sibeol-jwa.”

*What now?*

I looked warily at Magic Johnson, who had suddenly approached me.

I hadn’t expected much from Wu Heixing, who was infamous for his anti-Korean sentiment and various scandals in the first place. But the joy of seeing in person the S-rank Hunters I had only watched on television was gradually running out.

“…No, please. Call me by my name instead of Sibeol-jwa. Would you like it if I called you Fuckson instead of Johnson?”

“Hmm. Now that you mention it, I see your point. Jin, then?”

“That’s much better. But why?”

“It’s nothing special. You’re not thinking of kissing the prince’s hand, are you?”

*That sounds pretty special to me.*

Taken aback, I immediately asked,

“Of course not. What is this, the Middle Ages? Would you want to if you were me, Johnson?”

“I would.”

“What?”

A flash of enlightenment struck my mind.

I had completely forgotten. Magic Johnson was an American national hero—and the nation’s gay icon.

*Time* magazine’s choice for “the world’s most influential LGBT person” looked at me with a perfectly serious expression and made a proposal.

“So I’d like to express your gratitude to the prince on your behalf.”

“…”

What a way to package it.

But unlike Magic Johnson, Prince Felix quietly withdrew his hand.

“We are all equal human beings beneath God. This antiquated etiquette must disappear. Magic Johnson, I will accept your kind offer at a later time.”

“…”

*Was that really something the bastard who had just held out his hand to me could say?*

Pai Chen had been listening too. Apparently just as dumbfounded, she muttered,

“Oh my. He’s shameless. He may not be a criminal, but he might be even worse than Wu Heixing.”

“Even so, he’s better than Wu Heixing. That bastard should have been executed under the law.”

“That’s true.”

Wu Heixing had shriveled in the presence of one heavyweight after another, but now sparks flew from his eyes.

“Th-this, this, this bangzi bastard!”

“Enough with the bangzi routine. Even the national anthem gets hard to get through from the second verse onward. The same goes for me going easy on you.”

“……Going easy on me? You? On me?”

His tone made it clear that he genuinely couldn’t understand. I nodded.

“Yeah. It just became obvious.”

I had a pretty good idea what level Wu Heixing was at, but he hadn’t realized in the slightest who I was.

A fight starts with sizing up your opponent. This one was over before it even began.

“So stop picking fights for no reason and leave while I’m still asking nicely. Let’s each focus on doing our own jobs.”

“You’re a mere A-rank Hunter, yet because Comrade Chairman expects great things from you, you’ve forgotten your place and started running wild—!”

“Ah.”

I’d been wondering why he had acted like an asshole from the moment we met. So that was it.

The reason was so obvious and childish that a dry laugh escaped me.

“Still, calling it cute would be a stretch. You’re too damn old.”

“…!”

“What are you going to do? You want all of the Chairman’s expectations and attention for yourself, but some Korean guy has edged you out.”

“You…”

Wu Heixing’s face flushed with shame and fury as he realized I had seen through his thoughts.

By now, everyone’s attention was fixed on us. He must have felt their contemptuous stares all the way to his bones.

And when people like him found themselves in situations like this…

*They always cross the line.*

My prediction was dead on.

A faint movement.

His fingertips slid almost imperceptibly toward the hilt of his sword.

The magnanimous Chairman Xiao Yang hadn’t asked anyone present to disarm as a sign of trust, but that consideration would be poison to Wu Heixing.

*Draw it. Don’t hesitate.*

No matter how reckless I might seem, I did at least consider the circumstances.

I had held back until now only because I had come to help China at the Chairman’s request. If Wu Heixing drew a weapon, I would have grounds to rough him up within reason.

*That’s it. More. More.*

As if he were being controlled by me, Wu Heixing’s hand reached for the hilt. Just as he was about to seize it—

Step. Step.

Several sets of footsteps echoed through the hallway outside the quiet underground bunker.

Wu Heixing’s hand stopped, and the tightly shut door opened at almost the exact same moment.

The moment I saw the man who entered alongside Minister of Defense Wei Penghu, Wu Heixing’s existence vanished from my mind.

“I’m too late. Have you all been waiting long?”

Bold features that looked as though they had been painted with a brush, and a solid build that even his clothes couldn’t conceal.

He looked like a middle-aged man barely into his forties, but beneath that skin lurked an old tiger and a cunning snake.

*Lee Jungryong.*

When Lee Jungryong’s eyes met mine, a deep smile formed at the corners of his mouth.

[^1]: *Bangzi* is a derogatory Chinese slur for Koreans.
## Chapter artifact 386

# Chapter 386

“I’m too late. Have you all been waiting long?”

Lee Jungryong swept his gaze over the assembled people. Some faces were familiar, while others were strangers he was seeing for the first time today.

Magic Johnson and Pai Chen, whom he had encountered several times during the Great Cataclysm. The young British prince. And China’s problem child.

Each time his eyes met someone’s, the S-rank Hunters gathered in the underground bunker greeted Lee Jungryong first.

“It’s been a while, Lee. You’ve become an even more attractive man since we last met. Every time I see you, I feel like confessing my love.”

“Please restrain yourself, Magic Johnson. I don’t swing that way—though Pai Chen over there might be another matter.”

At Lee Jungryong’s nonchalant reply, Pai Chen swept back her long hair.

“Oh my. I didn’t realize Mr. Lee felt that way about me. What a shame. I found out too late.”

“What’s there to regret? You’re still in your prime.”

“Thank you for saying that, but if the youngsters heard us, they’d laugh. They’d wonder what a pair of old people like us thought we were doing.”

“Is that really how it is?”

When Lee Jungryong looked at him, Wu Heixing hurriedly waved his hands.

“Oh, no, Mr. Lee. How could that possibly be?”

“I’ve heard a lot about you. You’re remarkably talented and, hmm… a young man who’s honest about everything, I’m told.”

“T-Thank you.”

Wu Heixing bowed, looking deeply honored.

Normally, he was so hostile toward Korea that he constantly spat out the word *bangzi*, an insult for Koreans. But he lacked the nerve to show that side of himself in front of Lee Jungryong.

A bead of cold sweat rolled down the back of Wu Heixing’s neck.

“I’d heard you were coming, but I never thought you actually would.”

“Of course I had to come. When your neighbor is in trouble, shouldn’t you help?”

“It’s an honor to meet you, Mr. Lee.”

Even Magic Johnson and Pai Chen, heroes born from the Great Cataclysm, could not compare with Lee Jungryong.

He was the sworn brother of Cheon Taemin, called the Jesus of the twenty-first century and the savior of the world. He was also the real leader of that Ares Guild.

A powerful Guild counted among the strongest in the world. And a man ranked among the top three strongest S-rank Hunters.

Lee Jungryong.

Anyone who faced him had to show the proper respect.

Wu Heixing, arrogant as he was, was no exception. Neither was royalty of noble blood.

“Pleased to meet you. A pleasure to meet you, Jungryong Lee.”

“Ah. So you’re that prince.”

“How dare—”

Prince Felix raised a hand to stop his secretary and gave a dignified little bow.

“Felix. You may call me Felix. You may.”

The Korean produced by the translation device was awkward, and his level of formality was strangely ambiguous.

But with that, Felix Alexander Louis—third in line to the British throne—made the difference between Lee Jungryong and everyone else perfectly clear. He had actually allowed Lee Jungryong to omit the title *Your Royal Highness*.

Of course, Lee Jungryong did not care in the slightest.

*They’re all just brats.*

The only ones Lee Jungryong acknowledged were Magic Johnson and Pai Chen.

Whatever their personalities, Wu Heixing and Prince Felix were considered geniuses by the public. But in Lee Jungryong’s eyes, they were nothing more than chicks that had only just learned to walk.

And…

The people who truly irritated Lee Jungryong were elsewhere.

*The Peace Guild.*

Lee Jungryong’s gaze shifted to one side. A deep smile formed on his lips as he looked at the two men standing there in silence.

“I’ve been seeing you two quite often lately. Have you both been well?”

At Lee Jungryong’s greeting, Jin Taekyung and Choi Minwoo exchanged glances and shrugged.

“Not really.”

“Not particularly.”

“…?”

What?

Lee Jungryong faltered without realizing it.

It had been less than a month since he had last seen them. Yet there had been a great change in the way the two men treated him.

*Hostility.*

That was it.

The obvious hostility and wariness he had felt from them before were no longer there.

As Lee Jungryong looked at the two men, who were as calm as could be, he soon understood why.

*They’ve grown stronger. Incomparable to before.*

There was no doubt about it. Choi Minwoo’s energy was far greater and more refined than before—so much so that Lee Jungryong wondered how he could have grown this much in such a short time.

And the other man, Jin Taekyung…

*…What is this?*

He could feel it through his skin and sixth sense. The tremendous energy contained within Jin Taekyung’s entire body. The deep, still look in his eyes.

It could mean only one thing.

*He crossed the wall.*

The shock struck Lee Jungryong as though someone had hit him in the back of the head. He had to struggle with all his might not to show his agitation.

*How?*

Jin Taekyung had already been a powerful man. He might even have stood above the countless A-rank Hunters in the world.

After all, he had defeated two named monsters alone. It was only natural that people and the media had been loudly proclaiming the birth of a new S-rank Hunter.

But Lee Jungryong had known the truth.

Jin Taekyung had not yet crossed the wall.

He knew it would take a very long time for the man to climb over the wall blocking his path and become a true powerhouse.

And yet…

*How could something this absurd happen?*

Mere surprise could not begin to describe it.

As Lee Jungryong met Jin Taekyung’s impassive gaze, he remembered emotions he had long forgotten.

Anxiety. Impatience.

It was the first time Lee Jungryong had felt such unease since taking complete control of the Ares Guild.

Only a few months ago, Jin Taekyung had been nothing more than someone he found ridiculous and irritating.

Yet that man had awakened feelings of anxiety and impatience within him.

*You…*

The smile on Lee Jungryong’s lips vanished as though it had been washed away. Wei Penghu looked at his stiff face in puzzlement.

“Mr. Lee? Is something wrong?”

“…It’s nothing.”

“Hmm. Then may we begin the meeting?”

Lee Jungryong nodded silently, his gaze fixed on one person the entire time.

Leaning diagonally against the back of his chair, the young man named Jin Taekyung muttered as if to himself,

“Well, it certainly looks like something to me.”

“…!”

“Or not. Never mind.”

Without realizing it, Lee Jungryong clenched his fists tightly.

* * *

The meeting in the underground bunker continued for a long time.

The monster wave had caused at least hundreds of thousands of casualties over the past week. It was already a massive natural catastrophe in its own right, and they were unquestionably at war. Naturally, they had to proceed with the utmost caution.

“Accordingly, we should divide our forces into five armies and pressure the enemy…”

Someone interrupted Wei Penghu as he continued speaking with a serious expression.

“Comrade Minister of Defense.”

“Speak, Senior General Liao.”

The middle-aged man known as Senior General Liao wore a uniform dripping with medals. Stroking his beard, he began to speak.

“Listening to the Minister of Defense, I find myself so frustrated that I have to speak. At this rate, how long will it take us to deal with those monsters?”

*Wow…*

His tone was unbelievably obnoxious.

He was talking that way to Wei Penghu—the Chairman’s right-hand man and the military’s highest-ranking power broker.

As if he had read my question, Team Leader Choi sent me a Message Spell.

- The Communist Party has factions too. Senior General Liao is a pure-blooded member of the Princelings, the Communist Party’s largest faction, going back to his grandfather’s generation. They’re rivals of the Shanghai clique, which Chairman Xiao and Minister of Defense Wei Penghu belong to.

- The Princelings and Shang… what?

- …If we’re being precise, it means the Princelings are number one and the Shanghai clique is number two.

- Ah.

Until now, I had assumed that the Communist Party operated under a strict one-party system. Apparently, they fought each other tooth and nail too.

- But is that allowed? If Chairman Xiao simply points at someone and says, “That man is dangerous,” wouldn’t that person be beheaded in Tiananmen Square?

- They do it because they’re allowed to.

- …Right. When you put it that way, I’ve got nothing to say.

- The factions reached an agreement. During the Great Cataclysm, the Chairman from the Princelings made so many mistakes that they felt awkward about continuing to hold power.

- Ah. Pingping?

- Yes. Pingping.

That damn Great Cataclysm really had changed all kinds of things.

While I was listening to Team Leader Choi’s explanation, Senior General Liao—who apparently came from the Princelings’ pure-blooded younger generation—made an absolutely brilliant proposal.

“Let’s use nuclear weapons.”

“…”

“…”

“Let’s formally request it from Chairman Xiao and fire dozens of nuclear weapons across all of Sichuan. Wouldn’t that solve everything cleanly?”

“…”

“…”

What a lunatic nuclear-happy bastard.

Everyone, myself included, stared at each other in disbelief.

Wei Penghu’s expression was especially spectacular. He answered with the face of a man who desperately wanted a pistol.

“Rejected.”

“Why? Are you dismissing me because I’m not part of the Shanghai clique?”

“Say something that makes sense. Something that makes sense! If we do that, what happens to the people who are still alive or haven’t been harmed? What about the land we leave barren?”

“Sacrificing the few for the sake of the many is unavoidable!”

Forget the rest—he just sounded like an ox head to me.[^1]

Magic Johnson, who had been listening quietly, suddenly spoke in his deep voice.

“The damage from a successful nuclear attack is bad enough, but what are you going to do if someone uses spatial teleportation magic to move the nuclear warheads? To Beijing, for example.”

“That’s why we have an Archmage like you…”

“Me? Our opponent isn’t an ordinary Lich. If this Arch Lich is more skilled in magic than I am, then it will cause an irreversible catastrophe. Something similar already happened several times during the early days of the Great Cataclysm, remember?”

“B-But even so… sacrifices on this scale…”

“Hey. Motherfucker.”

Bang!

I nearly jumped out of my skin. Magic Johnson shot to his feet, his bronze muscles rippling.

“Knock it off. I like Asian men too, you know. I might punish you.”

“…!”

“…!”

That was the scariest threat I had ever heard.

Senior General Liao’s face turned deathly pale as he looked around for help. But the officials who appeared to belong to his faction avoided his gaze. Even Wu Heixing, the last line of defense, looked away.

*So this is how it gets resolved.*

The opponent was an American national hero and a national gay icon.

Everyone seemed desperate not to become the Asian man Magic Johnson liked.

Of course, the ridiculous bullshit Senior General Liao had been spouting also played a major role.

“Enough, both of you. And especially Senior General Liao—stop talking such utter nonsense.”

Under Wei Penghu’s leadership—a Chinese man who had just subdued the chink—the meeting moved forward quickly.

After gathering the opinions that had been raised and exchanging heated arguments, Wei Penghu finally won everyone’s agreement. He spoke with a tired expression.

“We will divide the six S-rank Hunters present here among six fronts. According to the official organization, each front will receive three Army and Air Force divisions, along with Hunters from the Public Security Armed Forces.”

Three Chinese divisions, along with the Public Security Armed Forces.

I had no idea exactly how many that meant, but their sheer numbers would be enormous.

When it came to the number of Hunters it possessed, China was always competing for first or second place.

*Of course, the other side is no pushover either.*

The casualty estimates alone were in the hundreds of thousands.

If the Arch Lich had resurrected the dead as undead…

Then an unimaginable number of enemies would be waiting for us.

“This concludes the meeting. Please move out as soon as possible.”

Just as everyone rose from their seats after Wei Penghu said he would provide the exact numbers and unit composition in writing, a voice pierced my ear.

- Come see me for a moment.

It was not a Message Spell, but unmistakably Sound Transmission.

[^1]: The Korean word *so* can mean both “the few” in the general’s maxim and “ox,” turning his solemn justification into an insult.
## Chapter artifact 387

# Chapter 387

By the time we emerged from the underground bunker, it was already deep into the night.

I drew a deep breath, letting the cold air seep into my lungs. As I gazed up at the star-studded night sky, thinking of Murim’s Sichuan somewhere out there, a small hand tapped me on the shoulder.

“Want to come along? I was thinking of having a light drink.”

“Now?”

“Yeah. Just us.”

It was Pai Chen. Behind her stood the other two people included in that “us.”

One of them spoke in a tone overflowing with dignity.

“O noblewoman of the East, might there be a bottle of Romanée-Conti among the wine we shall drink together?”

“I’m no noblewoman, but of course there is. Do you like wine, Prince?”

Prince Felix answered with a displeased expression.

“I told you to call me Your Highness Felix, not Prince. And I enjoy wine in moderation—especially 1945 Romanée-Conti.”

“We don’t have the 1945 vintage.”

“Then I must decline. I’ll be going.”

*Is he actually insane?*

Prince Felix disappeared with his attendants, and Pai Chen turned to the one person left.

“You’re coming, right, Johnson?”

Magic Johnson smiled, baring his snow-white teeth.

“I’m sorry. Unfortunately, I think I’ll have to take a rain check.”

“Why?”

“I might be deployed to the front as early as tomorrow. I should at least get *Memorize* ready beforehand so I can put my mind at ease.”

As expected of an Archmage. You didn’t become a hero of the Great Cataclysm for nothing.

Deeply impressed by Magic Johnson’s attitude, I spoke up.

“I don’t think I can go right now either.”

“No.”

“Why not?”

“You’re neither a prince nor an Archmage.”

“…”

“What kind of logic is that?”

Unbelievable. Her ridiculous stubbornness was one thing, but this middle-aged woman was really something, suggesting drinks at a time like this.

“You just insulted me in your head, didn’t you? Called me a thoughtless middle-aged woman for wanting a drink in a situation like this.”

“…How did you know?”

“Oh my. Look how pointlessly honest you are.”

Pai Chen poked the tip of my nose with one long finger. She looked like a beautiful woman in her early twenties, but she was actually older than my mother. It felt strange.

“How about finding someone else? Mr. Lee, maybe…”

“Lee?”

Pai Chen tilted her head slightly. Lee Jungryong had long since disappeared with the Ares Guild members he had brought along.

“Hmm. He’s difficult to deal with. He wasn’t that bad during the Great Cataclysm, but he’s turned into a slippery old fox. I can never tell what he’s thinking.”

*She’s a pretty accurate judge of character.*

Pai Chen continued, casting a sidelong glance at another candidate disappearing in the distance.

“Wu Heixing. He’s too rude. Drinking with him would ruin the wine.”

I stared at Wu Heixing’s back as he headed into a deserted forest and answered.

“Nothing we can do. You’ll have to drink next time.”

“No. This is exactly the sort of night you drink on.”

“…?”

“It might be our last chance.”

“Ah.”

I thought I understood, at least to some extent, why Pai Chen wanted a drink.

War exhausted people. At the same time, it brought unexpected farewells in the form of death.

This was her own eve-of-battle ritual after losing countless companions during the Great Cataclysm.

By the time this crisis was over, one of us might have crossed the river of no return.

“Well, now that things have turned out this way, I have no choice but to change targets. Don’t you agree, handsome bachelor over there?”

“I told you I’m not going.”

Pai Chen stared at me in disbelief.

“Have you no shame? I meant that young man, not you.”

Contrary to my expectations, the handsome bachelor Pai Chen had singled out—Team Leader Choi—nodded readily.

“If you’ll have me, I’d be honored.”

“Wait, Team Leader. You’re really going?”

“Of course. When will I ever get another chance to have a drink with Pai Chen? Besides, I have plenty of questions.”

Pai Chen burst into laughter.

“I thought you were only handsome, but you say such pretty things, too. All right, then. What are you so curious about?”

“The Equipment you’re wearing right now. Where did you buy it?”

“…That’s your question?”

“Yes.”

“This one’s quite a handful too.”

As Pai Chen let out a deep sigh, Magic Johnson burst into hearty laughter.

“Haha! Miss Chen, shall we all go have that drink now?”

“All of us? Johnson, didn’t you say you weren’t coming?”

“I did. I don’t make a habit of drinking alone with women. But if a charming man like Mr. Choi joins us, that changes things.”

“…”

“I like men. Especially East Asian men.”

“R-right. Let’s go.”

No wonder *Time* had named him the world’s most influential LGBTQ person.

I sent Team Leader Choi a Sound Transmission as he was dragged away, stiff as a board.

—If anything happens, contact me.

Team Leader Choi looked at me with the sad eyes of an ox being led to slaughter, then disappeared with the two S-rank Hunters. I looked around before setting off.

*This was the direction.*

How long had I walked along the dark path to avoid people’s eyes? I stopped in the pitch-black darkness and spoke.

“Come out.”

After a brief silence, someone’s voice drifted out.

“…Not bad.”

Rustle.

A figure emerged with the sound of someone approaching. Wu Heixing looked me up and down.

“How did you know?”

*What kind of question was that?*

I answered listlessly.

“You might as well ask me what one plus one is. That’d be harder.”

“Hmm. You’re more capable than I expected.”

“Don’t pretend to compliment me now. It’s obvious you’re trying to pull some cheap trick.”

“…!”

Bull’s-eye. Wu Heixing’s face flushed red.

In a way, he was incredibly easy to handle. I knew he was already past his mid-thirties, yet it was hard to imagine anyone being this simple.

“N-no, that’s not it. I sincerely—”

“You probably do sincerely think I’m a *bangzi*.[^1] You were annoyed because some Korean guy who isn’t even an official S-rank Hunter yet was getting attention instead of you. You picked a fight with your usual one-dimensional behavior, but it didn’t go over well, and that *bangzi* bastard turned out to be tougher than you expected, huh?”

Without giving him a chance to answer, I continued at machine-gun speed.

“So now you’re throwing out a few compliments you don’t mean and acting friendly while you look for an angle… Did I get any of that wrong?”

“…”

“Yeah, I’ve seen plenty of people like you. I’ve been blindsided so many times that even this slow brain of mine has learned to work fast.”

I looked at him like he was pathetic. His face already bright red, Wu Heixing stammered.

“I wasn’t trying to pull another trick.”

“Then what? If you’re thinking of becoming friends with me, fold that thought up neatly and tuck it away. If I stand next to shit, the stink rubs off on me too.”

“…!”

“By the way, what are you doing right now?”

At my quiet question, the hand moving toward his sword hilt stopped dead.

“Don’t draw it. You’ll get hurt.”

Wu Heixing stared at me, visibly conflicted, before blurting out,

“You knew all along… so why did you follow me so readily?”

“Because I had something to ask.”

“What?”

I looked straight into Wu Heixing’s eyes.

“Sound Transmission. Right?”

“…!”

His face stiffened. That was answer enough. I had suspected as much, but I scratched the back of my head and muttered,

“So it was. Well, this is the mainland, after all. There could still be all kinds of martial arts here. An internal-energy cultivation technique, for example.”

“W-what are you talking about? That was a Message Spell…”

“Oh, please.”

A dry laugh escaped me at the sight of his frantic excuses.

People who had never encountered martial arts might not be able to tell the difference, but he couldn’t fool me.

*Come see me for a moment.*

What had reached my ear near the end of the meeting had unmistakably been Sound Transmission.

The reason I had accepted an offer I could have ignored was that Wu Heixing himself had sent it.

“H-how did you know that?”

“What, was it a secret no one else knew?”

I stared at the flustered Wu Heixing and continued.

“I did think it was somewhat possible, but it’s still fascinating. Didn’t you wipe out all the martial artists during your Cultural Revolution and whatnot? Martial arts somehow survived even through that.”

“Shut your mouth!”

“Ah, you said your family was powerful. Did the highest levels of the Communist Party use their positions to quietly spirit it away?”

“…”

His expression instantly sank.

*Looks like I was right.*

As a foreigner, I didn’t know exactly how serious a problem this was. But I knew how valuable an internal-energy cultivation technique was—the thing now called a mana cultivation method in the modern era.

*If this were the Murim, a bloody storm would have erupted.*

Now that he’d been caught with the golden calf that had been secretly spirited away, no wonder he wasn’t taking it well.

“It would be best if you never uttered what you just said again.”

“I wasn’t planning to, but that tone of yours is pretty damn irritating.”

Wu Heixing glared at me viciously.

“Do you think you’ll still be able to act this way once you learn who my father is?”

“I don’t know who your father is, but I have a feeling he used to be a Red Guard.”

“…!”

“Wasn’t your father the one who smashed Confucius’s tomb with a sledgehammer in his youth?”

“You fucking *bangzi* bastard—!”

Fwish!

With a furious roar, he shot forward.

A straight sword had already been drawn from its scabbard. The Aura Blade rising from it—no, the Sword Force—flew toward my neck.

Shiiiiing!

The cool wind scattered my hair. I bent backward until my back nearly touched the ground, letting the Sword Force pass overhead, then sprang upright and drove my knee into his chin.

Crack!

Teeth and blood shot into the air. As he staggered, I seized both his arms and whispered into his ear.

“I told you not to draw that sword.”

Hiss! Crack!

“Gaaaaaaaaah!”

The powerful Scorching Yang Qi surging through both my hands shattered his armor and seared his flesh.

The scream that tore from Wu Heixing’s lips struck the Qi Curtain I had spread and went no farther.

“You bastard!”

Whooom!

That bastard had learned fist-and-foot techniques too. Unlike his shoddy sword technique, this one was reasonably sharp.

Of course…

*Compared with the Murim, the quality of his martial arts was far lower.*

Slightly disappointed, I reached out.

Boom!

Internal energy collided with internal energy.

The leg he had whipped toward my waist like a lash stopped dead.

Wu Heixing’s eyes trembled with shock and disbelief.

“H-how?”

“Well.”

I grabbed his ankle and slammed him into the ground with all my strength.

Whoom! Boom!

Once more.

Whoooom! Crash!

More, more, more.

Crash! Crash! KRA-KOOM!

The ground turned over, and rocks and trees were ripped from the earth.

A little while later, when I finally stopped using him as a living pickaxe, Wu Heixing lay spread-eagled in a huge crater, looking as if his soul had left his body.

“Still, you’ve got a sturdy body. You’re not hurt that badly.”

“Hh… hhaa…”

“Hey, are you crying?”

“Hhaaa…”

He was completely out of it.

Clicking my tongue, I bent over and searched through his pockets.

After rummaging through the pouch enchanted with spatial expansion magic for some time, I finally found what I wanted.

“Ah, here it is. An Advanced Potion.”

Ding.

> **System**
>
> **Acquired:** Supreme Potion!

“…No, wait. Supreme Potion? What the hell, you bastard?”

I stared in shock at the sprawled-out Wu Heixing. Even for an S-rank Hunter, who carried something like this around?

Advanced Potions were rare enough, but only one or two Supreme Potions appeared in an entire year, if that.

Never mind the price, which was so high it hardly felt real. They were so scarce that even having the money wasn’t enough to get one.

*I’d only ever seen one online. And now here it is.*

After a moment’s thought, I quietly slipped the Supreme Potion into my inventory. Then I searched his pouch again, found an Advanced Potion, and poured it over him.

“I’ve taken my settlement payment, so I’ll let you off here. You’ve got plenty to hide yourself, so if you go around blabbing about what happened today… you know what’ll happen, right?”

“Hh… hhh…”

“Okay. We’ve reached a settlement.”

Just as I neatly wrapped things up, the phone in my pocket shuddered.

A short text message had arrived from Team Leader Choi.

> 〈 Team Leader Choi
>
> Team Leader Choi
>
> Ji nTaekyung please come quic kly

“…”

*No, Johnson.*

[^1]: *Bangzi* is a derogatory Chinese slur for Koreans.
## Chapter artifact 388

# Chapter 388

“Hey. Hey.”

Tap. Tap-tap.

Someone nudged Wu Heixing in the side with the tip of a foot. He barely managed to open his eyes. A huge figure loomed over him.

“Hngh…”

“I’ve got something urgent to take care of, so I have to go. If anyone comes by, make up some excuse for me.”

“Hngh… hngh…”

“I poured an Advanced Potion over you, so quit milking it, punk. Keep that up and I might call Magic Johnson over to make you moan for real. See you!”

Fwish!

With that parting remark—one that made his ass ache just from hearing it—the man’s presence rapidly faded into the distance.

A little over ten minutes passed before Wu Heixing, still sprawled spread-eagled, finally growled in a seething voice.

“Jin Taekyung…!”

His broken bones and flesh had recovered thanks to the Advanced Potion, but it could not heal the pain etched deep into his bones or his cracked pride.

*How?*

He couldn’t believe it. No matter how worked up he had been, how could an S-rank Hunter like him have been toyed with so thoroughly?

The fact that Jin Taekyung had seen through his martial arts was shocking enough, but for someone who took such immense pride in his own power, the shock of defeat struck even harder.

*Me? Me, of all people?*

Wu Heixing had been born destined to become a Hunter.

Even as an infant, his potential had been recognized through an enormously expensive mana aptitude test, and his family—part of the highest echelons of the Chinese Communist Party—had spared no expense in supporting him.

They possessed vast wealth and power amassed through corruption. Raised in the finest environment with every possible advantage, Wu Heixing awakened as an A-rank Hunter at the age of twenty. Ten years later, he accomplished the remarkable feat of becoming an S-rank Hunter.

And yet…

*But why? Why did I lose to that bangzi bastard from such a small country?*[^1]

A fierce light flashed in Wu Heixing’s eyes as he glared at the pitch-black night sky.

His gaze held anger, but also jealousy—and a trace of fear toward the power Jin Taekyung had displayed.

And those emotions were ones Wu Heixing had been sickeningly familiar with for more than a decade.

Wu Heixing shouted at the one person he could no longer find.

“Was this your doing? Are you trying to torment me even after death?”

The public and the media reviled Wu Heixing as an incorrigible degenerate even as they praised him as a genius born of Zhonghua. But a tiny handful of people, Wu Heixing among them, knew the truth.

The true genius was someone else. That was why they had kept him hidden instead of letting him come to light.

“Answer me, Lei Fei!”

Lei Fei possessed not only overwhelming skill but also a noble character. To Wu Heixing, he had been an insurmountable wall.

How flustered—and delighted—had Wu Heixing been when he first heard that Lei Fei had disappeared?

But only a week later, another wall had appeared.

Its name was Jin Taekyung.

“Gaaaaaaaaah!”

His roar echoed across the night, making the bushes tremble.

“That feeling… I know it well, too.”

At the quiet voice of someone who had approached without a sound, Wu Heixing sprang to his feet like a bolt of lightning.

“Who are you?”

“I’m hurt. I thought we knew each other.”

Step.

A figure suddenly stepped out of the darkness. Wu Heixing’s eyes widened.

“You’re…?”

Beneath the faint moonlight, Lee Jungryong continued with a smile.

“It seems we have something important to discuss. What do you think?”

“…!”

* * *

Ding.

> **System**
>
> - You have finished circulating your qi!
>
> - Your realm in the Blazing Flame Divine Art has risen slightly!

By the time I gathered my qi and opened my eyes, daylight was already beginning to brighten the world outside.

As if it had been waiting for this exact moment, the Skeleton Warlord promptly spoke.

- Vile human. You have finally awakened?

“I wasn’t asleep, punk.”

- Drinking before a battle. Tsk, tsk.

“I’m not going to get a hangover, so shut up.”

Drinking too much caused alcohol toxins to accumulate, but any halfway decent internal arts master could purge them with ease.

With my powerful Scorching Yang Qi, I had even less to worry about.

*Come to think of it, I really did drink a lot. I polished off every last bottle Pai Chen had flown in on her private jet.*

I had definitely gone there to stop Magic Johnson, but I had no idea how things had ended up that way.

- Human, how much longer do you intend to stay in this cramped place?

“I was about to leave anyway.”

The clock showed five-thirty in the morning. It was about time to get ready.

After packing my things in the hotel room assigned as my temporary quarters, I headed down to the lobby and found Team Leader Choi drinking coffee.

“Oh, Team Leader.”

“…You’re out.”

One glance told me he had dark circles under his eyes. His skin, normally flawless thanks to his meticulous self-care, looked rough.

“Didn’t you sleep?”

“Would you be able to sleep if you were me, Mr. Jin?”

“…”

Fair point.

Last night, I had received the most desperate emergency message in the world and rushed over. What I witnessed there had been nothing short of horrifying.

*“Hey, Choi. It’s a drinking game. Come on, just do it once. Be cool. Right?”*

*“Pai Chen! Please help me, Pai Chen!”*

*“Hmm… Sorry, but this is a drinking game. The king’s command is absolute. Isn’t that the rule?”*

*“Even so, a kiss? This is my first time playing a drinking game! You didn’t even explain the rules properly!”*

*“Ah, whatever, whatever. Number Two will kiss Number Three on the cheek. That’s my command.”*

*“Choi. Stay still. I don’t want to cast a binding spell on you.”*

*“This is absurd… Jin Taekyung! Jin Taekyung, over here!”*

*“Jin. Don’t interfere. I don’t want to use an attack spell on you.”*

Honestly, if I had been one minute late, it would have ended in a catastrophe.

I had been forced to chug an enormous amount of alcohol in exchange for rescuing Team Leader Choi, but I didn’t regret it in the slightest. I had been promised a fair reward in return.

“You remember the promise you made yesterday, right? The one about adjusting my share of the settlement.”

“…I remember. Nine to one.”

Team Leader Choi glared at me coldly.

“How could you do that in such an urgent situation? Are you even human?”

“Then give him one good, passionate kiss right now. Look, here comes Number Two.”

He might have been Number Two, but his gay stat was number one in the world.

Team Leader Choi spotted the huge Black man who had just entered the lobby—Magic Johnson—and sprayed out a mouthful of coffee.

“Ptooey! Please, please hide me!”

“I think it’s already too late.”

The moment I finished speaking, Magic Johnson spotted us and waved a palm the size of a pot lid.

“Hey, gays!”

Wasn’t it usually *guys*? He must have misspoken… right?

As Team Leader Choi and I wondered whether we had heard him correctly, Magic Johnson walked over and laughed heartily.

“Don’t look at me like that. I got a little too excited yesterday and played a tiny prank.”

“…You were really excited?”

“Ah. I suppose that’s how it sounded.”

“Watch what you say. You startled me.”

“Haha. Anyway, something came up yesterday.”

“…What came?”

“Huh? No, not that kind of coming.”

“Please watch what you say. You really startled me.”

“Please, both of you, stop. I’m afraid someone might hear you.”

Wearing the serene expression of a man who had transcended all worldly concerns, Team Leader Choi drained the rest of his coffee and turned his head.

A group of people had passed through the hotel’s main entrance and were walking toward us.

“It is time to depart, gentlemen.”

Minister of Defense Wei Penghu led the group, his voice stiff with tension.

At his signal, an elderly-looking military general began handing out folders one by one.

“What’s this?”

“Information on the areas to which you have been assigned and the forces stationed there. Of course, we have already sent the necessary information and established communications with the people on that side. From now on, you will travel aboard the designated jets.”

Modern technology certainly made things like this convenient.

A short while later, we followed Wei Penghu to the temporary airfield, where several familiar faces were surrounded by tight security.

“Did you sleep well, youngsters?”

“…”

“You’re late.”

Pai Chen greeted us with a long stretch. Wu Heixing lowered his gaze without a word, perhaps because of what had happened yesterday, while Lee Jungryong wore a strange smile.

The Skeleton Warlord, safely stored inside my Inventory, spoke in a displeased voice.

- There is something unpleasant about that human. This commander does not like him one bit.

“I agree.”

Pai Chen heard me mutter and raised an eyebrow.

“Hm? What did you say?”

“Nothing. By the way, where’s Prince Felix?”

“He left just before dawn. Apparently, a battle signal came from the area assigned to him.”

“…I see.”

Another battle had broken out less than twenty-four hours after our arrival.

At the thought of the word *war*, something suddenly clenched in one corner of my chest.

Our nationalities and upbringings were different, but the thought of people just like me being brutally slaughtered somewhere weighed heavily on my heart.

“Hey, young man.”

“Yes?”

Pai Chen gazed at me for a moment, then lightly tapped my shoulder.

“Relax your shoulders. How are you supposed to swing your spear when they’re weighed down like that?”

“…”

“Don’t blame yourself, and don’t rush. Don’t try to take responsibility for every death.”

Responsibility.

After thinking about it for a moment, I answered honestly.

“...I’m not sure. I can’t say I’m very confident.”

“Well, for someone who feels that way, you certainly drank yourself senseless yesterday.”

“That was…”

“I know. I’m joking. This is how people like us forget the burden for a little while. We might die tomorrow—or even today.”

The words didn’t match her bright voice at all.

The hero who had fought her way through the maelstrom of the Great Cataclysm with her entire body raised her head and gazed at the sky.

“Ah. Perfect weather for a fight.”

Then she turned and walked lightly toward the jet, which was ready for takeoff.

She left us with one quiet remark.

“Let’s all see each other alive.”

Her back disappeared into the aircraft.

Magic Johnson gazed up at the sky for a moment with emotion in his eyes, then abruptly spoke.

“Hey, Choi.”

“Yes?”

“Relax your ass, too.”

“…”

“No, I mean relax your shoulders. Let’s see each other alive again.”

*I had a feeling his true feelings had just slipped out.*

Magic Johnson laughed heartily at Team Leader Choi’s wary gaze and boarded the jet after Pai Chen.

Wu Heixing then walked off as though fleeing. Lee Jungryong, the last one left, looked Team Leader Choi and me over with a strange gaze.

“Both of you, take care. You can’t go dying in a place like this when you’re still so young.”

*What an old man’s way of putting it. What a loaded remark.*

I smiled and spoke in place of Team Leader Choi, whose face had gone rigid.

“We should. Unlike some people, dying now wouldn’t exactly count as a good death for us.[^2]”

“…!”

“If you kick the bucket, I’ll make a generous condolence contribution.”

“I’ll look forward to it.”

After a brief silence, Lee Jungryong tossed out that one remark and led the Ares Guild members away.

Now only the two of us remained.

I stretched with all my might, then patted Team Leader Choi on the shoulder.

“Let’s go, Team Leader.”

“Yes. We should.”

“There’s no need to be nervous. Relax your ass.”

“…”

“…It was a joke. Sorry.”

*At this rate, two jokes would be enough to kill a man.*

I was cautiously watching Team Leader Choi’s expression as I climbed aboard the jet when—

“Troops—attention!”

A thunderous shout erupted behind us.

Minister of Defense Wei Penghu was saluting us, his half-gray hair whipping in the wind.

The people filling the airfield followed his example and saluted.

It was a gesture of respect toward the heroes going to fight for the gathered crowd’s families and friends.

They held their salutes until the jet’s door closed and the aircraft dwindled to a distant speck, then vanished from sight.

*Good grief.*

After a send-off like that, how could my shoulders not feel heavy?

I suddenly felt tired and leaned back against my seat.

Static crackled.

- …respond. Respond. This is…

Along with the distorted radio transmission coming from the cockpit, an alert pierced my ears.

Ding.

> **System**
>
> - Unexpected Quest generated: The Battle Situation Has Become Critical.
>
> - You cannot refuse the Quest. Arrive as quickly as possible and defeat the enemies!

“…”

*Damn it. That’s just how my life goes.*

I let out a deep sigh, then shouted toward the cockpit.

“Sir, give it full throttle!”

* * *

“What about them?”

The speaker was an old man in his eighties. Wrinkles and age spots covered his face. His aged body was no longer what it had been in his youth, but his eyes held even greater strength than they had back then.

Even through the holographic screen, the force of the old man’s gaze was palpable. Wei Penghu swallowed hard before answering.

“They have all departed, Comrade Chairman.”

“How is the battle situation?”

“We cannot easily determine the enemy’s movements because of communication interference caused by magic and the barriers, but we are doing our best to detect their movements.”

“If the S-rank Hunters arrive…”

“With their power, they should be more than capable of turning the tide.”

“Do not jump to conclusions. Do not let your guard down for even a moment. Countless lives depend on our decisions.”

“Yes. I will keep that in mind.”

After ending his brief communication with Minister of Defense Wei Penghu, state chairman Xiao Yang sat alone in the vast conference room, lost in thought.

*How did it come to this?*

This was an unprecedented catastrophe since the Great Cataclysm.

They had committed vast amounts of manpower and funding, yet still failed to stop the monster army centered around the Arch Lich.

He had wanted to prevent panic if at all possible, but if they delayed any longer, the opportunity might disappear forever.

That was why Xiao Yang had come here today, despite the countless objections from within the Communist Party.

“We are ready.”

“…Connect me immediately.”

At the secretary’s words, Xiao Yang opened his closed eyes.

One by one, holographic figures began to appear above the empty seats throughout the vast conference room.

Fourteen people of different races and genders.

No—fifteen, including Xiao Yang.

Each one was the leader of a nation, and all belonged to a single organization.

*The United Nations Security Council.*

The old chairman announced the beginning of the emergency meeting in a grave voice.

[^1]: *Bangzi* is a derogatory Chinese slur for Koreans.

[^2]: A *ho-sang* is a death considered fortunate because it comes after a long, full life, usually at an advanced age.
## Chapter artifact 389

# Chapter 389

It was a day when the cold snap had finally eased.

Students finally freed from the college entrance exam were busy either preparing to retake it or having fun, while office workers boarded public transportation with dark circles hanging beneath their eyes.

And in the midst of that peaceful, ordinary routine, a bombshell no one had expected dropped.



**[Breaking News—United Nations Security Council Makes Major Announcement]**



The roughly thirty-minute video began with Chairman Xiao Yang staring gravely into the camera.

“I stand before you as the ninth state chairman of the People’s Republic of China and a member of the United Nations Security Council to speak about the massive monster wave that has occurred in Sichuan Province.”

It was a bombshell that seized the attention of the entire world and sent all of Asia into upheaval.



* * *



One day passed. Then two. Then three. Even after four days, the situation had not calmed down.

There had been countless incidents and accidents since the Great Cataclysm, but the monster wave that had erupted in Sichuan Province was unprecedented in scale.

Chinese state chairman Xiao Yang declared official martial law, and peacekeeping forces were deployed to the front with the approval of the United Nations Security Council.

The entire world was watching.

The Asian countries bordering China were especially on edge.

South Korea was no exception. Even today, the Hunter Issues section of the country’s largest forum site was boiling like a cauldron over a charcoal brazier.



Here’s a summary of the situation so far.

Nobody here hasn’t watched the Security Council’s major announcement video, right? If there is, go outside and die. This is a genuine emergency. Even that northern supreme leader bastard has probably watched the whole thing on iTube and is lurking on this forum too.

Anyway, there were so many fucking vermin demanding a summary of something that could literally cost them their lives that I finally got fed up and wrote one.

**1. An unexplained massive wave occurred in Sichuan Province. The current estimated casualties are at least 300,000.**

Of course, that estimate is already a week old, and the current figure probably can’t even be compared to it. Realistically, I think it’s impossible to calculate the numbers.

**2. The Chinese government intervened, but the scale was completely insane.**

A monster army numbering at least tens of thousands has gathered around a creature called an Arch Lich.

The People’s Liberation Army and Air Force were thoroughly wrecked, and more than two thousand Hunters from the Public Security Armed Forces have gone missing. Communications were cut off because of magical interference, and satellite surveillance was neutralized, so they can’t even confirm whether anyone survived.

**3. The Chinese government secretly contacted several countries and hired several S-rank Hunters to suppress the situation as quickly as possible. The UN peacekeeping forces were deployed to the front two days ago, and they’re fighting desperately.**

The Security Council is updating the battle situation, so anyone interested can check here.

*(Link attached.)*

Everything below this is just my personal opinion, so you can skip it if you want.

**4. Anyone with a functioning brain knows this, but the current situation is not merely serious. Mainland China is basically hell on earth.**

They’re dragging every usable Hunter to the front, so the mana levels of other Gates, which are being neglected, are unstable too. Hyperinflation is happening everywhere.

The truly frightening part is this: if the front collapses and the monster army advances beyond Sichuan…

I’ll leave the rest to your imagination.

**5. So go to the supermarket and buy emergency rations before everyone gets completely fucked. Of course, I’m not telling you to hoard supplies and make an unfair profit.**

**6. It felt like a shame to end things here, so I’m adding some patriotic hype.**

Our Sibeol-jwa and Ares Guild’s Jung Dragon are both doing great work at the front. Keep stanning them as hard as you have been.

The end.



Within a few hours of being posted, the thread surpassed 100,000 views and caught fire with comments from netizens watching the situation closely.



**(Best Comment)** The situation really is as serious as the post says, but the author is laying it on a little thick lol. There are S-rank Hunters in the fight, plus a hundred thousand regular Hunters. What’s there to worry about? And is the military just sitting around?

└ Yeah, they’re fooling around in the maintenance units right now.

└ …………?

└ Didn’t you watch the news? All the Chinese military equipment broke down this time, exposing the largest military-procurement corruption scandal ever. They say it’s worth at least tens of trillions of won. Apparently more than one or two divisions are stuck.

└ Huh. This sounds really familiar.

└ Please replace the canteens already, you fucking assholes. I got discharged last year, so why does mine still taste like Normandy water? Every time I take a sip, I can’t tell whether my name is Kim Cheol Soo or James.

└ Corporal Kim. Tonight’s dinner is braised boneless pollock.

└ Not eating that shit.

└ Anyway, the military being stuck because of broken equipment is a problem, but they have manpower to spare, so they’ll be fine. Hunters are the only ones who can actually hurt the monsters anyway. There’s a bigger problem than that.

└ What?

└ The number of monsters has broken through 100,000.

└ ??

└ ?????

└ What do you mean, 100,000? Fuck off; don’t talk nonsense.

└ It’s not nonsense. It’s official from the UN Security Council. Follow the link in the post and check it yourself. It was posted five minutes ago.

└ Wow… fuck.

└ Judging by the reaction above, I guess it’s true. Holy shit.

└ No. I only reacted like that because it’s all in English and I have no idea what it says. I’m running it through Goggle Translate right now.

└ Is this guy insane?

└ But seriously, if the monster count has really passed 100,000, isn’t this a disaster? The largest monster wave so far didn’t even exceed a thousand, did it?

└ Obviously, the wave wasn’t this big in the beginning. The problem is that there’s an Arch Lich over there. Even the appearance of an ordinary Lich would be a major incident, but that thing is a top-tier named monster unknown even to the academic world. Realistically, most of the monsters currently fighting are undead revived by the Arch Lich.

└ Arch Lich: “Kaioken times one hundred.”

└ Then can’t we just kill the Arch Lich? If most of the monsters are undead, killing the controller should end it, right?

└ ???????

└ Who the hell is going to kill the Arch Lich, you bastard? You can only use Aura Blade on a keyboard, and your mouth’s still the only thing that works.

A fierce argument broke out.

Some commenters watched from a safe distance, as though observing a fire across a river, while others took the situation extremely seriously.

And even as doomsday theories and optimism battled for control, new updates continued to pour in.



**(Best Comment)** Security Council official: The front in the east-west sector was breached an hour ago. Fortunately, Pai Chen arrived as reinforcement and prevented the damage from spreading.

└ Damn, it’s true.

└ If it’s the east-west front, isn’t that where Wu Heixing is?

└ Yeah. That Chinese junkie guy.

└ But how did it break through? He’s an S-rank Hunter.

└ Because he’s a Chinese-made S-rank Hunter.

└ Ah…

└ It could’ve been a real disaster if Pai Chen hadn’t been there. Maybe it’s because Pai Chen is a well-made Hunter from the Great Cataclysm.

└ Pai Chen’s parents have Hong Kong citizenship, so she’s Hong Kong-made.

└ Does the commenter above work in quality control or something? That was fucking clear.

└ While you’re at it, does anyone have news about the Korean Hunters?

└ Jung Dragon is in charge of the northern front and gaining the upper hand. I heard Sibeol-jwa won two or three times on the western front, but there’s been no news since, so I guess they’re holding the line.

└ Hmm… Nobody needs to worry about Lee Jungryong’s skills, but is Sibeol-jwa safe? He’s still an A-rank Hunter.

└ ?? LOL

└ LMAOOOOOOOOOO

└ There’s still an innocent idiot who treats Sibeol-jwa like an A-rank Hunter? As a current A-rank Hunter, all I can do is laugh. That Jin Taekyung guy is just a monster lol



Hey heyheyhey!! The U—N Security Council just announced the w—estern front situation!

└ Oh, Sibeol-jwa news. Been a while.

└ That sounds incredibly urgent. The western front? What are they saying?

└ They say it broke through?

└ Huh?

└ Huh?

└ What the hell does that mean? Don’t tell me Sibeol-jwa died…?

└ Wait. What is this actually saying? Guys, I’m going back to check it again. It’s on the main page, so go look for yourselves.

└ Ah. I’m suddenly fucking terrified. I’m checking it right now.

└ Go go go go go



The netizens who had been enthusiastically writing comments hurriedly accessed the United Nations Security Council website.

Because too many visitors had flooded the site at once, they had to wait for quite some time after hitting the traffic limit. At last, when they saw the announcement that had appeared on the main page, they could do nothing but doubt their own eyes and ears.

“…What the hell is that?”

The map displayed the standoff with the monster army. The front line formed an oval, but the western front had been gouged inward like an awl.



…I just checked. It really broke through.

└ Is Jin Taekyung dead? How bad are the casualties?

└ No, the monsters’ line was breached.

└ ??

└ ???

└ The breakthrough happened so fast that the updates couldn’t keep up.

└ …Does that even make sense?

└ Shut up and pull down the shutters. Today is the tavern lady’s death anniversary…[^1]

[^1]: Korean internet slang calls for a tavern lady to pour celebratory drinks when national pride surges; the joke is that today’s celebration will work her to death.



* * *



The battlefield where a fierce battle was about to erupt was chaotic. An endless wasteland stretched out before us, and countless monsters filled my field of vision.

A wind that blew in from somewhere carried the thick killing intent and stench pouring off the creatures.

“Fuck. They really gathered a lot.”

Team Leader Choi, standing beside me, answered my mutter.

“No matter how many we kill, they never end.”

It was the fourth day since we had been deployed to the western front and the full-scale battle had begun. The Team Leader Choi who had always looked immaculate was nowhere to be found.

Covered in blood and dust, he looked at me with a calm, somber gaze.

“When do we begin?”

“Who knows? We should hear what our little commander thinks first. Right?”

That last question was not directed at Team Leader Choi.

The twenty-one-year-old “little commander” who had not left my side the entire time answered. It was Shao Shen.

“I will follow Teacher Jin’s orders!”

A snort of laughter escaped me at the sparkle in his eyes.

“You’re still going on about calling me Teacher. You were the one who first told me to drop the formal speech. I told you to call me hyung instead.”

“Is it… Is it really all right if I do that?”

“I told you it was fine as long as you were okay with it. But can you really do this in front of your men? I heard you’re getting promoted to major general now.”

Shao Shen shook his head at lightning speed.

“There’s no problem at all! H-hyung-nim!”

He was frighteningly calm when fighting, so I had no idea why he stammered so much in ordinary situations.

I looked at the Hunters from the Public Security Armed Forces lined up behind him. There were more than a thousand of them.

Their heated eyes held admiration and awe for the strong.

Of course, Shao Shen stood out even among them.

“Give us your orders. H-hyung-nim.”

“An order.”

I suddenly looked up at the sky.

A huge eagle with its wings spread wide circled above our heads. I had a good feeling about today, too.

“Follow me. Just like you’ve done until now.”

“……!”

“Right now.”

I stepped forward as I answered.

Crack.

The force of ten thousand geun packed into my toe made the ground split like a spiderweb and cave inward.

And then, in the next moment—

Boom!

Accompanied by a deafening roar that left my ears ringing, I shot forward as a streak of light.

*Flamefire Path.*

The wind carrying the cold heated up and transformed into a blast of hot air.

As the ground, wind, and scenery streaked past, a tremendous roar erupted behind me.

“Charge! Charge!”

“Descendants of Zhonghua! People! Sweep every last one of them away!”

“Waaaaaaah!”

Thud-thud-thud-thud!

Kyaaaauuuuu!

Human battle cries and monster shrieks rang across heaven and earth. The immense vibrations shook the very ground.

At the threshold of that chaos, I swung the White Flame in my hand with all my strength.

Whoooosh!

The Extreme Yang force that surged from the spearhead sliced through everything standing in its way.

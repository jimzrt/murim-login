# Checkpoint Review — 515–519

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

## Checkpoint summary

# Chapters 515–519

## Plot

At Xixia, Sama Pyo confronts Shaolin’s young Martial Uncle, the scarred and hoarse-voiced Unnamed, over the Black Dragon Saber. Unnamed reveals his identity, orders Sama Pyo to return the sword, and warns that Henan will not tolerate disorder. After three months in Repentance Cave, treatment with Shaolin’s Great Restoration Pill, and enlightenment driven by regret over Hong Dao’s death, Unnamed has advanced to the Supreme Peak realm and resolved to carry on his Master’s will.

Jin Taekyung reaches Shaolin after nearly drowning during his journey toward Henan. He completes Stage 2 of Fake Murim Practitioner, earns the achievement **Single Reed Crossing the River**, improves his internal-energy control and attributes, receives bonus points and substantial EXP, and levels up. He later reunites with Unnamed, recognizes Jung Ho as his former Garam Middle School classmate Park Jung Ho, and learns that Shaolin’s new Abbot—Unnamed’s eldest Senior Brother—wants to meet him.

With the New Murim Alliance’s founding three days away, orthodox and unorthodox factions, distant great families, and eccentric experts gather near Mount Song. Jeok Cheongang, restored to middle age through Returned to Youth, finally begins his long-delayed duel with Nangong Cheon, the Azure Sky Sword King, using chopsticks as swords. Their clash coincides with a Dark Heaven assault, sending the gathered Murim forces into battle.

Jeok emerges from a burning inn and is mistaken for a Dark Heaven fiend. Unnamed’s attempt to identify him as Hong Dao’s master worsens the misunderstanding, until the Thunderbolt Saber King recognizes Jeok as the Returned-to-Youth Fire King. After arguing over the destruction and injuries caused by their clash, Jeok, Taekyung, Unnamed, and Peng Cheolhu proceed toward the Murim Alliance. Nangong Cheon intervenes after exchanging blows with Jeok and sustains a minor Internal Injury.

## Continuity

- Unnamed is now a scarred Supreme Peak master, Jung Ho’s young Martial Uncle, and Hong Dao’s practical Disciple. He spent three months in Repentance Cave, received Shaolin’s Great Restoration Pill, and carries on Hong Dao’s will.
- Shaolin’s new Abbot has held the position for less than a month, is Unnamed’s eldest Senior Brother, and wants to meet Taekyung.
- Jung Ho is Park Jung Ho, Taekyung’s former Garam Middle School classmate, and Shaolin’s Discipline Hall Master.
- Taekyung completed Stage 2 of Fake Murim Practitioner, achieved **Single Reed Crossing the River**, improved his internal-energy control and attributes, gained 50 bonus points and substantial EXP, and leveled up.
- The New Murim Alliance’s founding is imminent near Mount Song. Major orthodox and unorthodox factions, great families, and independent experts have gathered there.
- Jeok Cheongang has expelled his Heart Demon, entered a new realm, achieved Returned to Youth, and begun his promised duel with Nangong Cheon. The duel’s outcome remains unresolved.
- Peng Cheolhu, the Thunderbolt Saber King, is Jeok’s longtime rival and friend, Hong Dao’s close friend, and protective toward Unnamed. He recognizes Jeok despite his rejuvenated appearance.
- Dark Heaven attacked near the Alliance gathering. Jeok’s emergence from the burning inn caused a chaotic misidentification; the assault’s broader consequences remain to be seen.
- Nangong Cheon intervened after fighting Jeok and sustained a minor Internal Injury.
- The Black Dragon Demon Gate is an ancient unorthodox faction formerly belonging to the Demonic Cult’s Twelve Branches and remains one of the Central Plains’ strongest unorthodox powers.
- The source and significance of the familiar red gaze and gigantic snake from Taekyung’s nightmare remain unknown.
- The Lord of Heaven’s identity and connection to the dangerous force associated with Taekyung’s original world remain unresolved.
- The permanence and repeatability of Zhuge Feng’s Demon-Sealing Formation remain unresolved, as does the Southern Heaven Demon Empress’s ultimate destination and intent in Yunnan.

## Translation Decisions

- Retain **New Murim Alliance**, **Murim Alliance**, **Outer Murim**, **Outer Lands**, **Black Dragon Demon Gate**, **North Sea Ice Palace**, **Nanman Beast Palace**, **Small Thunderclap Temple**, **Mad Wind Society**, **Potala Palace**, **Five Poisons Sect**, **Poison Valley**, **Fire Gate Clan**, **Fire Gate Divine Technique**, and **Rising on Duckweed, Crossing Water**.
- Render **가짜 무림인 2단계** as **Fake Murim Practitioner, Stage 2** and **Single Reed Crossing the River** for the achievement.
- Render **계율원주** as **Discipline Hall Master**, **대환단** as **Great Restoration Pill**, **십이지파** as **Twelve Branches of the Demonic Cult**, and **어린 사숙** as **young Martial Uncle**.
- Render **모용세가** as **Murong Family**, **요녕** as **Liaoning**, and retain **Jindotgae One**, with a footnote identifying it as South Korea’s highest military alert level.
- Retain **Thunderbolt Saber King** for 벽력도왕, **Azure Sky Sword King** for 창천검왕, **Fire King** for 화왕, and **Murim Alliance** for 무림맹.
- Render **팽 대협** as **Sir Peng**, **남궁 대협** as **Great Hero Nangong**, and **시주** as **Benefactor** in formal address.
- Preserve Taekyung’s profane, irreverent internal narration and Unnamed’s formal Buddhist voice, including his precept against killing.
- Keep the identity of the person emerging from the burning building initially ambiguous; the later reveal identifies him as Jeok Cheongang.

## Durable state

{
  "active_continuity": [
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he has entered a new realm, achieved Returned to Youth, and begun his long-promised duel with Nangong Cheon, the Azure Sky Sword King.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; Mu Song and five Water Dragon Stronghold subordinates know he is exceptionally powerful but not that he is the Slaughter Saint.",
    "Mungyeong is training Taekyung to refine the stability and precision of the violent internal energy produced by the Fire Gate Divine Technique through Rising on Duckweed, Crossing Water.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "The New Murim Alliance has been publicly announced from Mount Song, and major orthodox and unorthodox factions, eccentric experts, distant great families, and uncertain allied factions are gathering in Henan.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Unnamed, Hong Dao's practical Disciple, endured three months in Repentance Cave, achieved enlightenment, received Shaolin's Great Restoration Pill, and is now a scarred Supreme Peak master and Jung Ho's young Martial Uncle; Shaolin's new Abbot wants to meet Taekyung.",
    "The Black Dragon Demon Gate is an ancient unorthodox faction that once belonged to the Demonic Cult's Twelve Branches and now ranks among the Central Plains' strongest unorthodox powers.",
    "Jin Taekyung completed Stage 2 of Fake Murim Practitioner, achieved Single Reed Crossing the River, improved his internal-energy control and attributes, gained 50 bonus points and substantial EXP, and leveled up.",
    "The Dark Heaven assault near Mount Song has ended in a chaotic misunderstanding: Jeok Cheongang emerged from a burning inn, was mistaken for a Dark Heaven fiend, was identified as the Returned-to-Youth Fire King by Peng Cheolhu, and was separated from the mob by Nangong Cheon."
  ],
  "continuity_sources": [
    519,
    518
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?"
  ],
  "safe_through": 519,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, 갠지스강 as Ganges River, and 대환단 as Great Restoration Pill.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain sa-eo for 사어, shark for 상어, Old Master for 노야, this old man/I for 노부, Shark Water-Ski Team for 수상스키단, and swift ship for 쾌조선.",
    "Render 정호 as Jung Ho, 사마표 as Sama Pyo, 흑룡도 as Black Dragon Saber, 대초자곤 as two-section staff, 시주 as Benefactor, 계율원주 as Discipline Hall Master, 십이지파 as Twelve Branches of the Demonic Cult, 모용세가 as Murong Family, 요녕 as Liaoning, 진돗개 하나 as Jindotgae One, 소하문 as Xiao He Gate, 장충도 as Long Serpent Saber, 방가 as Fang Family, 월미도 as Moon Beauty Saber, and 검기상인 as the level of injuring others with Sword Energy."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 515

# Chapter 515

It was clear that the chaos breaking out in the marketplace had not yet spread to the ferry landing.

If it had, there would be no cheers ringing out now, either.

“The Jin Family of Taiyuan! The Jin Family of Taiyuan has arrived!”

“Hooray!”

There was a considerable distance between the main road and the ferry landing, but not one of the people still gathered there failed to hear the cheers drifting from afar.

Black Dragon Saber Sama Pyo was one of them.

*The Jin Family of Taiyuan…*

Sama Pyo’s gaze sank.

The Jin Family of Taiyuan. A rising power that had grown explosively in less than two short years.

Then again, perhaps “rising” was not the right word. The family possessed a deep-rooted history and legitimacy spanning three hundred years.

And it was the existence of one person that had raised the once-fading great family back to its feet.

*Blazing Flame Divine Dragon Jin Taekyung.*

The young man, who had once been no more than a sickly sprout that seemed unlikely to amount to anything, had put down deep roots in the soil of the Murim and was growing into a mighty tree.

Each of the branches connected to him was thick and flourishing.

Fire King Jeok Cheongang. Huashan Divine Dragon Cheongpung. Sword Saint Mae Jonghak, Cheongpung’s master. Huashan, a powerful force counted among the strongest of the Nine Sects and One Gang. And several other prestigious great sects with which he had formed no shallow ties while traveling throughout the martial world.

And…

Shaolin Temple, the Mount Tai and Northern Dipper of the Murim, was among them as well.

“I was wondering what kind of remarkable guest would prompt Shaolin’s Discipline Hall Master to come all the way here to meet him. Now I understand.”

“Amitabha. This humble monk is not so idle.”

Jung Ho stared at Sama Pyo with a stiff expression and continued.

“Nor am I so easygoing that I would stand by while someone picks a pointless quarrel.”

“Ah.”

Sama Pyo removed the hand that had somehow found its way onto the hilt of his saber and smiled.

“My apologies. It’s a bad habit.”

“I hope that is the truth.”

“I know proper conduct. Surely you didn’t think I would harbor disrespectful thoughts toward Shaolin.”

“Amitabha. It would be best to refrain from actions that could invite misunderstanding, Benefactor Sama Pyo.”

“I will. However…”

The faint smile at the corner of Sama Pyo’s lips sharpened again. He looked back and forth between Jung Ho and the unidentified monk wearing a conical hat pulled low over his face.

“Judging by how firmly a Master of such deep Buddhist faith is speaking, it seems this person is someone you hold very dear.”

Jung Ho’s position in Shaolin was far from low, as anyone could tell from the fact that he was the Master of the Discipline Hall.

His own master had been one of the three disciples of Hong Dao, the deceased former Abbot of Shaolin and Dharma King.

Whether one judged by his position or by seniority, Jung Ho was one of the leading figures within Shaolin. Sama Pyo guessed that the reason he was displaying such open hostility had less to do with his personality than with the identity of the person beside him.

“I have heard that you have not yet accepted a Disciple, Master.”

“…You have sharp ears.”

“As you know, I have a keen eye as well.”

Jung Ho frowned.

“Amitabha. Enough with the wordplay. Let us speak another time. We must go and receive a guest who arrived earlier than expected.”

“Ah, I see. Have you taken in a new Disciple?”

“Benefactor.”

Woom.

At that moment, the Zen staff in Jung Ho’s hand released a low resonant hum.

A person who had been silently watching the situation finally spoke.

“It is all right, Martial Nephew.”

“……!”

“……!”

A rough voice, like metal scraping against metal, emerged from beneath the deeply lowered conical hat and pressed down on the air around them.

Jung Ho and the Shaolin monks trembled at the immense internal energy contained in that voice, while the eight-foot-tall giant beside Sama Pyo opened his enormous, round eyes wide.

But the reason Sama Pyo was startled was not merely the aura emanating from the monk in the conical hat.

*Martial Nephew? Martial Nephew?*

As Sama Pyo stood momentarily frozen, the monk in the conical hat spoke quietly.

“Return the sword to its rightful owner. Here in Henan, we will tolerate no disturbances.”

“……!”

“If fate brings us together, I will see you again.”

That was all.

Having delivered those words as lightly as though entrusting them to the wind, the monk in the conical hat turned and disappeared.

The Shaolin monks followed after him without a word.

The giant turned toward Sama Pyo and spoke in his halting voice.

“Young Sect Leader. That monk. Who is he? I cannot defeat him.”

“……”

“He has no hair. But he has skill. Very strong.”

Sama Pyo did not answer.

He recalled the faint righteous gleam he had glimpsed in the monk’s eyes beneath the conical hat at the final moment, then muttered.

“The Discipline Hall Master’s young Martial Uncle.”

It had only been a brief encounter, but it had been long enough to estimate the monk’s age.

The face revealed beneath the conical hat had been extremely young, and also…

“Young Sect Leader?”

“Yes, I’m listening. You idiot.”

Sama Pyo returned from his thoughts and clicked his tongue softly. He tossed the sword back to the merchant cowering and trembling in a corner, then looked up at the sky and stretched.

“Let’s go. I need a drink.”

“Pleasure house! Pleasure house!”

“Yes, yes.”

The sky was blue, and the heroes who had traversed the Murim were gathering in Henan.

And in the distance, the cheers of the crowds gathered at the ferry landing continued without end as they called out the name of the Jin Family of Taiyuan.

* * *

“I am sorry for causing you trouble, Martial Uncle.”

On the way to the ferry landing, Jung Ho hurried his steps to catch up beside the monk in the conical hat.

The monk shook his head.

“It was not your fault, Martial Nephew Jung Ho.”

“No. It was an issue I should have resolved myself. I never expected that young Benefactor to behave like that…”

Jung Ho’s displeasure was plain on his face.

He was still offended by Sama Pyo’s conduct.

At a time like this, on a main road under countless eyes, the young man had not only beaten Blood Cudgel to death but had also tried to provoke one of Shaolin’s senior figures.

“I had heard that the Black Dragon Demon Gate wielded considerable influence in Gansu, but he is even more insolent than I expected.”

“Is that so?”

The voice that emerged from beneath the conical hat was rough, but the speaker’s manner was utterly calm.

The monk continued walking as he spoke.

“There are still many things I do not know, as my experience remains limited. However, I have heard that the forces practicing demonic, heterodox arts are not particularly strong.”

“That is true. But not every unorthodox sect is the same.”

“The Black Dragon Demon Gate is one of those exceptions.”

“Yes. The Black Dragon Demon Gate easily ranks among the three strongest unorthodox factions in the Central Plains. It might even be considered the greatest focal point among them.”

“What do you mean by a focal point, Martial Nephew?”

“Symbolism, Martial Uncle.”

“Symbolism…”

“The Black Dragon Demon Gate has the longest history of any unorthodox faction in the Murim. It was once one of the Twelve Branches of the Demonic Cult.”

“Did they betray the Demonic Cult?”

“Amitabha. I think ‘compromise’ would be more accurate.”

The Black Dragon Demon Gate’s compromise had succeeded.

The victory in the long and brutal war had ultimately gone to the orthodox faction, while the Black Dragon Demon Gate gathered the scattered unorthodox martial artists of the Central Plains like blades of grass, restored its losses, and strengthened its power.

“But for the Black Dragon Demon Gate’s Young Sect Leader to behave so insolently. It means he looks down on Shaolin, which suffered such enormous losses during the past bloodshed, and—”

Jung Ho suddenly closed his mouth.

As though he had read the thoughts in his heart, the monk walking beside him spoke in a low voice.

“It is all right. Do not concern yourself with it, Martial Nephew Jung Ho.”

“……Martial Uncle.”

“Everyone in Shaolin suffered grievous wounds. Some lost Senior Brothers and Junior Brothers with whom they had shared hardship. Others lost their Disciples. I am no different.”

Step. Step.

Their pace gradually quickened. The rough voice continued from beneath the conical hat.

“I was… unquestionably so grief-stricken that I thought I could not bear it. But merely because that person departed on a distant road from which he could not return, that does not mean his will has vanished as well.”

Jung Ho and the other Shaolin monks bit their lips.

How could they forget that day? How could they not understand the sorrow he had felt?

Everyone remembered. Everyone knew.

“I will carry on my Master’s will. I endured my time in Repentance Cave with that single conviction.”

The skin glimpsed beneath the conical hat was as rough as the monk’s voice, covered with countless scars.

For someone whose name was unknown, the past three months had been a hellish time.

Every day, he had repeated treatment and training while writhing in terrible pain. Those who heard the screams echoing from Repentance Cave could not keep themselves from shedding tears.

Three months stained with anguish and suffering.

Yet he had endured to the very end. He carried the grief brought by his master’s death and the anger he felt toward those responsible for it upon his shoulders, advancing without pause.

And at the end of that road, enlightenment had come like a single ray of light.

“Martial Nephew Jung Ho.”

“Yes, Martial Uncle?”

“My Master would sometimes say this. Everything begins with one person. If one is not enough, then two. If even that is difficult, then three should step forward. That is how we raise up what has fallen and move onward.”

The Master who had departed on a road from which he could not return had loved wine and meat.

He would lie on a rock and sleep through the entire day, opening his eyes only after the world had grown dim.

Then he would shake the shoulder of the Disciple who had come to wake him, only to fall asleep beside him, and point toward the night sky stretching high above them.

*Look. You are there too.*

The Disciple, rousing himself with disheveled hair, would rub his eyes and ask in return.

*Why do you call that star your Disciple?*

*Because I followed that star when I first went to bring you back.*

*But… that star is so small and faint.*

*That is why it is good.*

*What?*

*The star that shines with the brightest, clearest light will soon disappear. But your star will illuminate the sky from that place for a very long time.*

The Disciple still remembered what his Master had told him that day.

Even after a long time had passed, the heavenly patterns had become distorted, and a new star had risen somewhere in the north.

Even on the day his Master departed on a distant road and the grounds of Shaolin were stained with blood.

The Disciple remembered.

Even now, he was still wandering around that day and that place.

*Master. Where is my star now? Have you become a star somewhere in the sky, watching over this Disciple?*

His steps stopped.

Standing tall on a hill overlooking the ferry landing, he suddenly raised his head toward the sky.

There was no star anywhere in the clear blue sky.

Even if darkness fell, he would not be able to recognize his own star. Nor would he be able to find his Master’s star.

No matter how wide he opened his eyes, all he could see were the two vessels moored at the ferry landing and the people filing down from them.

Even when he listened closely, all he could hear were the cheers of the crowd gathered like a bank of clouds.

*Master. Where are you?*

He slowly closed his eyes.

But even when his vision dimmed, he could not see the stars. Even when he opened his ears wide, his Master’s voice did not reach him.

In the end, today was no different.

Just as he realized reality once again and was about to open his eyes with composure—

Splash!

“A person! Someone was running across the river and fell into the water!”

“Gasp! That’s… the youngest!”

People screamed. Someone let out a shriek. Then a familiar yet desperate voice rang out.

“For fuck’s sake, don’t just scream! A rope! Throw me a rope!”

Light shimmered before his eyes, which had been filled with nothing but pitch-black darkness.

It was the Morning Star that had risen in the north.

It was a trace of his Master.

*Have you come?*

A smile formed on the stiff lips of the monk in the conical hat, Unnamed.
## Chapter artifact 516

# Chapter 516

It was human nature for things to feel several times harder the closer one got to one's destination. After ten days and nights of pushing my body to its limits, I had not even a shred of strength left to squeeze out.

*Dad, I'm coming.*

Was this really how a father and son were going to reunite after so long? That was the moment the strength drained from my flailing limbs.

Grab!

My vision, which had been slowly fading, snapped back into focus.

Someone's hand had a firm grip on my wrist. Through my waterlogged ears, a voice forced its way in.

“Trying to get there before this old man? What a rotten little punk.”

When had he gotten here? Jeok Cheongang had closed the distance from the ferry landing in an instant. He was looking down at me with a grin.

The moment I finally saw his face, all the tension left my body.

“…Hrk.”

As I exhaled the breath I had been holding, Jeok Cheongang's grin deepened.

“You're still breathing, at least.”

“That's amazing. Am I still alive?”

“Listen to this fool. Yes, you're alive.”

“Then don't just stand there and look at me. Pull me up. I think I'm actually about to die.”

“Such an exaggeration. You're still a hundred years too young to die.”

Whoosh! Drip.

A powerful hand gripped my wrist and hauled me straight up.

River water and the plants clinging to my bloated body came pouring off me.

“Can you see?”

“Who? God?”

“The people waiting for you.”

Exhausted, I blinked. The crowd gathered like a bank of clouds at the distant ferry landing was rapidly drawing closer, and I could make out several familiar faces among them.

Cheongpung, waving both arms frantically. Gung Gibang and Hyuk Mujin, their eyes opened wide. Jin Wikyung, who was practically bawling his eyes out.

And… Mungyeong, quietly watching us.

—Welcome to Henan.

After sending that brief Sound Transmission, Jeok Cheongang's feet touched the ground while he held me in his arms.

At the same time, a clear ringing sound pierced my ears.

Ding. Ding. Ding.

> **System**
>
> **Fake Murim Practitioner, Stage 2** completed successfully!
>
> You have achieved the rare achievement **Single Reed Crossing the River**!
>
> As a reward for demonstrating remarkable persistence and effort, you will receive a fitting reward!
>
> Your control over **internal energy** has become freer! The power and efficiency of your martial arts have increased!
>
> All attributes have increased slightly!
>
> You have acquired 50 bonus points!
>
> You have acquired a massive amount of EXP!
>
> **Level Up!**

System notifications rang out one after another. Holographic windows filled the air.

Along with the Level Up message, I felt my body becoming lighter. At the same time, a wave of sleepiness came crashing over me.

“…Old Master.”

“Hm?”

“Don't wake me.”

That was the last thing I said before the heavy lids of my eyes closed and the demon of sleep swallowed me whole.



* * *



Where am I?

That was my first thought when I opened my eyes.

I slowly blinked and looked around. Every direction was drowned in pitch-black darkness.

As my eyes gradually adjusted, I finally realized where I was.

*A swamp.*

Yes, this was a swamp.

White bones of uncertain origin—human or beast—were scattered everywhere, and a horrific stench filled the air, strong enough to make me gag.

Even worse was the fact that my body was moving on its own.

Splosh.

My bare foot, without even a shoe on it, stepped into the sticky mud. I struggled with all my might to stop, but my body had already escaped my control.

One step. Then another.

That was when my body began to slowly sink deeper into the swamp.

Whoooosh.

A wind blew in from somewhere, making the skeletal trees that formed a forest throughout the swamp shudder.

Then, beyond the thick darkness, an unidentified red light surged upward.

*…What is that?*

It wasn't a flame. It looked more like the glow of someone's eyes.

A chilling gaze, devoid of even the slightest warmth, stared at me. As though it were saying, *If you can come, then come.*

If this were an ordinary protagonist from a movie or novel, he would struggle and crawl toward it…

*You come here, asshole.*

*Fuck the cliché.*

I had already figured out what I was dealing with.

Judging by appearances, I was having a nightmare after suffering through too much lately. There was no reason to play along.

An ordinary person would have felt the urge to piss himself the moment he saw those red eyes, but I was the kind of person who felt the urge to use Flame Divine Palm.

There was only one small, insignificant problem…

Splosh. Splosh.

*Ah, fuck.*

My body kept moving forward regardless of my will.

Slowly, as though swimming with the lower half of my body already sunk deep into the swamp. And steadily.

But I knew. No matter how long I continued forward, I would never reach it.

I would sink into the depths of the swamp before I ever met the owner of that gaze.

*Fine. Let's get this over with.*

That was when I had almost resigned myself to my fate.

Crack!

*Gasp!*

Something unidentified tightened around my neck.

My eyes flew open, revealing a gigantic body covered in smooth scales. A low, hissing growl pierced my ears.

*A snake?*

No, it was far too large to be called a snake. A python would be more accurate.

Its thick body wrapped tightly around my neck, then bound both my arms.

*Hngh.*

Damn it. Had dreams gotten a graphics patch lately? Why was this so vivid?

Rotten mud had already risen to my neck, and the stench forcing its way into my nostrils made me gag uncontrollably.

Unable to move as I sank into the swamp, I met the red gaze.

*…!*

A cold sensation surged up my spine.

A vivid fear, sharp enough to jolt my mind fully awake, swept over me. This couldn't be an ordinary nightmare. It couldn't be.

At the same time, a horrifying sense of incongruity enveloped me.

*This feeling… Why does it seem familiar?*

If so, when and where had I felt it? I dug through memories I did not want to recall, and that was when my whole body began to tremble.

Flash!

From somewhere, a blindingly bright light exploded.

The red gaze that had been spreading an ominously oppressive energy disappeared. Even the darkness that had swallowed everything around me shattered, and the chilly cold vanished.

Feeling a warm radiance envelop my entire body, I reached toward the mass of light that had come right up to my face.

Grab!

…Huh?

All kinds of thoughts raced through my mind.

Why could I grab the light? Why did it feel so good? I had definitely woken up from the dream, so why could I still feel it?

Rub, rub.

What the hell was this?

After thinking for a moment, I opened my eyes, which I had closed slightly.

There was a bright light—or rather, someone's shiny, smooth head.

A Buddhist precept seal was visible on his forehead.

“Krillin?”

The monk, whom I had never seen before—not Krillin—opened his mouth with an awkward expression.

“You have finally awakened, Benefactor Jin.”

“Excuse me, but who…?”

“This humble monk is Jung Ho.”

Who was Jung Ho?

After thinking briefly, I asked in a hoarse, halting voice.

“Were you perhaps Park Jung Ho from Class 6, Grade 3 at Garam Middle School…?”

“Pardon?”

“When did you become a monk?”

“A good forty years, at least… No, wait. Could you please listen to me, Benefactor?”

“Oh, now that I think about it, you bastard. Didn't you say you were going to become a priest? When did you switch? Apostate. Apostate. Did the Full Gospel Church Crusaders beat you up? Look how old your face has gotten. What temple hired you?”

My old classmate answered with an expression of half resignation.

“…I am Shaolin's Discipline Hall Master.”

“Shaolin?”

“Yes, Shaolin. I mean Shaolin Temple.”

“Wait a second. If it's Shaolin Temple, then…”

Oh, shit. What was this?

Only then did my mind fully clear. I hurriedly shook my head to dispel the sleep and cautiously opened my mouth.

“Ah, I'm sorry. I hadn't fully woken up yet.”

“I understand.”

Jung Ho, the middle-aged monk, replied with an expression that showed he did not understand at all, then continued.

“Could you please remove your hand from this humble monk's head now? You have been touching it for a while…”

“Whoops. Sorry.”

“It is all right.”

This man's expression and words did not match at all.

He clearly wanted to give me a piece of his mind, but was holding back because he owed me for the help he'd received.

*But why was Shaolin's Discipline Hall Master beside me the moment I opened my eyes?*

Only then did I sense that something was strange. I looked around and tried to understand the situation.

It was a large room, big enough for ten people to stay in at once. Sunlight streamed in through the half-open window and gleamed off Jung Ho's forehead, while familiar faces…

They were scattered all around me.

*So it was a dream, but half of it was reality.*

No wonder it had seemed too vivid to be a dream.

I let out a deep sigh, then first kicked the lump curled up asleep at my feet.

Thump!

“Ah! Meat dumplings for lunch today!”

“…”

What the hell was that wake-up call?

Cheongpung sprang awake from the sudden impact and opened his sleepy eyes.

“Ah, Benefactor. Did you sleep well?”

“I slept, but not well.”

“Why not? Then sleep some more.”

“…Are you kidding me? Stop babbling and get this thing off me.”

“Oh! Mimi! Come here!”

Only then did Cheongpung notice the pet snake coiled around my neck. At his shout, the thick body slowly slid down across my chest.

Wait a second. A thick body?

I stared open-mouthed at the Thousand-Year Poison Horned Snake, which looked practically like a python now.

“Young Hero Cheongpung. Was it always that big?”

“No. It has grown a lot lately. It's right in the middle of its growth period.”

“How old is it?”

“Grandpa Tang says it isn't even a hundred years old yet.”

“…Oh. I see.”

“It might end up bigger than me. Ah, I need to grow more quickly too.”

“You're already fully grown. Waiting won't make you any taller.”

“No, I haven't. Mimi will keep getting bigger as she gets older. I'll keep growing too.”

“…?”

Then damn it, shouldn't Jeok Cheongang and Mungyeong be at least three zhang tall?

I gave up trying to reason with Cheongpung and looked at him with a troubled expression. Instead, I smacked the mouth right beside me, which was giving off a horrific stench.

Smack!

“Urgh!”

“I told you to brush your teeth before bed. You damn beggar, your mouth is a swamp. A goddamn swamp.”

“Guh. Guhhh.”

Gung Gibang, forcibly awakened, glared at me with his moist eyes.

“Why do you always pick on me!”

“I don't only pick on you. I'm going to deal with this guy the exact same way.”

People had to be treated equally.

A little while later, Hyuk Mujin, who had been sleeping soundly while clutching one of my legs, met a similar fate.

Whack!

“Argh! Why do you always pick on me!”

“Did you two rehearse those lines? Or are you long-lost brothers or something?”

“Don't just hit me. Young Hero Gung too—oh, he's awake.”

“…Hah. You hateful bastards.”

I kicked Hyuk Mujin hard enough to send him tumbling beneath the bed while he muttered under his breath.

Because of these idiots, I'd even had a dream when I hardly ever dreamed at all—and an incredibly unsettling nightmare at that.

*That gaze.*

Even thinking back on it, that red light sent chills through me.

I was just about to retrace the strange sense of incongruity I had felt in the dream when Jung Ho, who had slipped away amid the commotion, opened the door and entered.

“Benefactor Jin. Could you spare me a moment?”

“Ah, yes.”

At Jung Ho's words, I straightened my posture.

I had rubbed his head as though it were a bowling ball, so I had to make time even if I did not have any.

“Please, speak, Monk.”

“The Martial Uncle of this humble monk wishes to see you, Benefactor.”

“Your Martial Uncle? Is he the person waiting outside right now?”

“Yes. He wishes to speak with you after such a long time…”

That explained it. I'd been wondering why I could sense two presences.

In any case, if Jung Ho's Martial Uncle was a senior monk of Shaolin, that much was certain. But he wanted to speak with me after such a long time?

*Who could it be? Judging by the way he put it, it has to be someone I already know.*

Besides the Dharma King, was there anyone at Shaolin with whom I had formed that kind of connection?

My puzzlement lasted only a moment before I readily nodded.

“Of course.”

And no sooner had the words left my mouth than I saw someone entering through the door and narrowed my eyes.

“Excuse me, but who…?”

He had a slender build, and every inch of exposed skin was covered in scars. A rough voice came from the lips of the fierce-looking monk I had never seen before.

“I am glad. Though the heavens have grown dim, the Morning Star that rose in the north seems to shine even brighter.”

“…!”

“How have you been, Benefactor?”

Only then did I realize who the monk before me was.

His atmosphere and appearance had changed so completely that I could not bring his name to mind right away. Then I called it out.

“Unnamed.”
## Chapter artifact 517

# Chapter 517

“Have you been well, Benefactor?”

I almost failed to recognize him. That was how different Unnamed was from the person I had met a year ago. His face, speech, and atmosphere had all changed. Everything surrounding him felt unfamiliar and strange.

And the reason he had changed was probably…

*It must be because of what happened that day, three months ago.*

What was I supposed to say? My mouth felt bitter. I only spoke after Jung Ho and Hyuk Mujin left the room with the others.

“I haven’t been doing all that well, either. A lot more happened than I expected.”

Unnamed smiled faintly.

“It seems so. In fact, this humble monk only managed to hear about you two days ago.”

No martial artist could have remained unaware of the events that had unfolded over the past three months. But if Unnamed, who held an important position within Shaolin, had only heard about them two days ago, there was only one reason I could think of.

“You underwent closed-door training.”

“Amitabha. I was staying in Repentance Cave.”

“Repentance Cave? Could it be…”

“You are correct. It was something I requested myself, so there is no need for you to worry.”

The first character meant shame; the second, remorse. Repentance Cave was where criminals were confined.

What had he been so ashamed of? What did he need to repent for? Perhaps he regretted failing to prevent his Master from entering Nirvana. Unnamed had spent three months there, considering himself a sinner because he had failed to protect even the Green Jade Buddha Staff, the sacred treasure of Shaolin that his Master had entrusted to him before passing away.

“I had many thoughts in that darkness, where I could not see even an inch ahead.”

Unnamed stroked his cheek with a callused finger. A large portion of his face, covered in scars both large and small, had turned dark bluish-black.

Three months ago, the Yin-Cold Qi left behind by the enemy he had risked his life to stop had left that mark. It was also a yoke he would never be free of.

“I kept thinking that if only I had been a little stronger, I could have protected my Master. I could have properly carried out his final request.”

But regret was always late. A venerable monk respected by everyone had entered Nirvana unexpectedly. Someone had lost a close friend. And someone else had been consumed by guilt over failing to fulfill even his Master’s final words, so he had entered Repentance Cave.

*Anyone else would have been the same.*

I would have been no different. I did not even want to imagine how I would have felt if I had failed to treat Jeok Cheongang and had been forced to watch him leave this world. I might have returned to the days when I was F-rank Hunter Jin Taekyung and repeated the same cycle of deep regret and despair.

But pain changes people. For better or worse. In Unnamed’s case, it had been for the better. His heart might have been broken, but at least in terms of advancing his martial arts, the pain had helped him.

“This is only my personal opinion, but I doubt you spent all your time thinking in Repentance Cave.”

“Amitabha. Everything was thanks to the Buddha’s and Shaolin’s benevolence.”

Unnamed pressed his palms together toward the window, where sunlight streamed in, then gazed at me with calm eyes. There was a pure power in that gaze. A year ago, his body had been built from sturdy muscle. Now it had withered like an old tree. But the quiet aura flowing from his entire body was incomparable to what it had been before.

*He crossed the wall.*

The supreme realm every martial artist in Murim dreamed of reaching. There was no doubt that Unnamed had finally stepped into it.

At the awed look in my eyes, Unnamed gave a small nod.

“To heal a body that had fallen into critical condition and advance to a higher realm, I needed more than enlightenment. The Great Restoration Pill was one of those things.”

“Ah.”

If it was Shaolin’s Great Restoration Pill, it was an elixir whose effects ranked among the very best in the world.

*Yes. If it was the Great Restoration Pill, it might have been possible.*

The pill’s effects were one thing, but Unnamed was the Disciple whom Dharma King Hong Dao, a man capable of reading heavenly patterns, had personally brought in and raised with all his heart. He was a genius born with tremendous martial talent—not quite on Cheongpung’s level, perhaps, but still extraordinary. There was no doubt that he was worthy of the Great Restoration Pill.

He had reached the Supreme Peak realm while still in his thirties, proving not only his Master’s discerning eye, but also his own talent.

“Congratulations. I heard the Great Restoration Pill is an extremely precious item even within Shaolin.”

“That is why this humble monk vehemently refused it. But my Senior Brother Abbot gave it to me, telling me not to ask any questions. As it turned out, my Master seems to have said something about it several years ago. Perhaps… he knew this would happen.”

A faint smile touched Unnamed’s lips. He gazed into empty space for a moment, as though remembering his Master, then continued.

“Oh, my Senior Brother Abbot would also like to meet Benefactor Jin.”

“Your Senior Brother Abbot?”

I had never heard anything about the next Abbot after Dharma King Hong Dao. According to Gung Gibang, it was supposed to be one of the Dharma King’s direct Disciples, but spectacular events had kept occurring one after another, and I had never found the time to think about it.

“The two of you have probably never met face-to-face. In our lineage, he is my eldest Senior Brother, but he has been Abbot for less than a month, so it is only natural that you would not know him.”

“Ah, I see.”

“He said that he was sorry he had been too distracted to even say goodbye before sending you away last time.”

“He doesn’t need to apologize. I was in such a daze back then that I could hardly think straight, either.”

The Shaolin Bloodshed that had occurred during the Star-Array Grand Banquet had been an unprecedented incident, but I had left Henan for Sichuan within a day or two. To save Jeok Cheongang, who was in critical condition, I had needed to find the Divine Physician as quickly as possible.

“Amitabha. This humble monk was truly delighted when he belatedly heard that Benefactor Jeok had made a full recovery. My Master, who must be watching over me from somewhere, would have been relieved to see his friend in good health.”

“Ah, now that you mention it, you must have already met Old— No, my Master.”

“Until you woke up, we had been speaking together. At first, I almost failed to recognize him.”

“Well, he, uh… did change a little.”

“Yes. He changed as much as this humble monk did.”

“…Uh.”

What was I supposed to say to that?

As I hesitated in response to the sudden self-deprecating joke, Unnamed politely pressed his palms together.

“Amitabha. It was a joke.”

“Oh. Ah. I see.”

“You do not seem to have found it amusing. This humble monk will refrain from doing so again.”

The words *Please do* rose all the way to my throat.

A joke like that was only funny when it came from someone who hadn’t suffered quite so much. When Unnamed said it, the mood could only turn solemn in an instant. But I did not have the courage to nod.

“…No. It was funny.”

“Amitabha. Then this humble monk will continue.”

“…”

“That was the end of the joke.”

*Should I just crack his head open with a wooden fish?*

I stared at Unnamed in disbelief, then let out a quiet laugh. Still, the fact that he was making such clumsy jokes meant he had weathered everything much better than I had expected.

Even if I could not offer him any comfort, I could at least listen to his borderline temple jokes.

*That aside…*

“Where are we? This doesn’t look like Shaolin Temple.”

The sun was shining outside the window, so I seemed to have slept for a full day. But I had no idea where we actually were. As I looked around the room once more, Unnamed explained.

“We are at an inn near Mount Song. It was rented in the name of the Murim Alliance, so please stay here and get plenty of rest.”

“The Murim Alliance.”

It had been a distant-sounding term, but hearing it directly from Unnamed in Henan made it feel much more real. I got out of bed and approached the window to look at the scenery outside.

The first thing that caught my eye was the peak of Mount Song, rising in the distance so high it seemed to pierce the sky. Beneath it, buildings were packed densely along the mountain’s lower slopes, and people of every kind filled my view.

A Murim practitioner with a narrow-bladed sword at his waist. Another carrying a massive saber on his back without even a scabbard. Others carrying spears and twin axes…

“…”

Yes, they were all different, but something felt wrong.

*They’re scary.*

At the sight of me watching the Murim practitioners everywhere I looked, Unnamed let out a low laugh.

“Amitabha. They are Benefactors who heard the news and gathered from every corner of the world.”

“Even a quick glance makes it seem like there are more of them than there were at the Star-Array Grand Banquet.”

“If the Star-Array Grand Banquet was a festival for young prodigies, the founding of the Murim Alliance concerns everyone. Members of the orthodox and unorthodox factions have gathered, along with a considerable number of eccentric experts who were previously little known and had been living in seclusion.”

That made sense. The scale alone was entirely different, so it was only natural that so many people had gathered. If the Star-Array Grand Banquet had been the Han River fireworks festival, the founding of the Murim Alliance was Jindotgae One.[^1] Perhaps for that reason, there were almost no commoners to be seen, unlike during the Star-Array Grand Banquet.

*They can feel it too. They must know what is happening here.*

As I thought that to myself, a group of Murim practitioners crossing the main road suddenly caught my eye. Their aura was unusual enough that they could not be mistaken for ordinary martial artists. They clearly belonged to one of the great prestigious factions.

*Their clothes are strange, too. Who are they?*

I did not even need to ask Unnamed. Their arrival—wrapped in furs that did not suit the warm spring weather and wearing leather armor unlike ordinary Murim practitioners—had already caused whispers to spread in every direction.

“Could they be…”

“That’s right. They’re the Murong Family.”

“My word. It’s well over a thousand li from Liaoning to Henan. They arrived quickly.”

“Do you think people call them descendants of horse-riding nomads for nothing? What luck. I never expected to see people from the Murong Family in my lifetime.”

It was my first time seeing the Murong Family, too. Shanxi Province, where the Jin Family of Taiyuan was located, was also considered a frontier region, but Liaoning lay far to the northeast beyond Hebei. It was not somewhere one could visit as casually as the neighborhood next door.

They were so far away that I had heard even members of the Murong Family rarely ventured into the Central Plains.

*So this is that Murong Family.*

As one of the stronger families among the Five Great Families, the Murong Family’s reputation had reached my ears so often that I was sick of hearing it. I had heard that, unlike other factions, they even operated a cavalry unit.

*Maybe that’s why they all have muscles like horses.*

*The orthodox Murim, led by the Nine Sects and One Gang and the Five Great Families. It sounds like the unorthodox Murim has joined in, too. And on top of that, all the martial artists who belong nowhere at all…*

People often called the United States a melting pot of races. To me, Henan looked exactly like that right now. Of course, the people here were all the same or similar in terms of race, but regardless, every kind of Murim practitioner one could rarely see had gathered in one place.

*Three days.*

Three days from now, countless martial artists would gather beneath a single banner. United under the name of the Murim Alliance, they would raise their weapons and stand against Dark Heaven.

The moment that thought occurred to me as I looked at the people outside—

Boom!

A tremendous roar echoed from somewhere.

[^1]: Jindotgae One is South Korea’s highest military alert level, used when an enemy attack is considered imminent.
## Chapter artifact 518

# Chapter 518

A middle-aged man, thoroughly drunk, suddenly raised one hand.

“Innkeeper, bring me a bottle of strong liquor!”

“Roast duck, too!”

“Would you look at these petty-minded fools. We’re on the verge of a momentous event—the founding of the Murim Alliance—and you want strong liquor and roast duck? We’ve come to Henan, so we should at least drink Dukang wine!”

“Oh, we’d love that, but aren’t you pushing yourself too far?”

“It’s fine. We’re splitting the bill anyway.”

“…You’ve lost your mind. Switch it to strong liquor.”

The inn along the main road near Mount Song was packed with people. Most of them, of course, were Murim practitioners.

From wandering martial artists who still looked like greenhorns to old veterans who had roamed the martial world for ten years—or even several decades.

The people gathered here differed in purpose, age, and gender.

And wherever people gathered, conflict was bound to follow. Especially when the people in question were drunk Murim practitioners.

“Wait. You’re…!”

“Oh-ho. Aren’t you the Senior Disciple of the Xiao He Gate? Is that finger they cut off still missing?”

“You bastard! You came looking for a place to die!”

The world might be vast, but enemies had a way of meeting even on a single-plank bridge.

Whenever people tangled in such complicated webs of gratitude and grudges happened to meet, a clash of blades was sure to follow.

Clang! Slash!

Sharp weapons swung at one another, and blood sprayed through the air. The fierce exchange unfolding before them sent the surrounding Murim practitioners into an uproar.

“Waaah!”

“It’s a fight!”

“One silver nyang on the Senior Disciple of the Xiao He Gate!”

“Then I’ll bet two nyang on the Long Serpent Saber!”

They said the two most entertaining things in the world were watching someone else’s house burn and watching someone else fight.

The very few people with no connection to Murim backed away with horrified expressions. But the Murim practitioners, who were crazy about fighting regardless of whether it involved the orthodox, unorthodox, or Demonic Path, shouted and applauded without hesitation.

And amid all that chaos, almost no one noticed the middle-aged man who had just opened the inn’s old door and entered.

Clang! Bang!

Waaah!

A fierce battle was raging in the middle of the inn, but the middle-aged man did not spare it a glance. He flicked a silver nyang toward the innkeeper.

“Two bottles of strong liquor and one roast duck. Bring them to a seat with a good view of the street. Oh, and roast the duck until it’s crisp.”

“Great Hero…”

“Hm?”

The innkeeper bowed deeply toward the middle-aged man.

“I’m sorry, but there aren’t any suitable seats available right now.”

“There aren’t?”

“No, Great Hero. As you can see, so many heroes of the Murim have come to visit…”

The middle-aged man looked around, then suddenly raised his head. Several faces were peering down from the landing above.

“There seem to be seats up there.”

“Ah, I’m terribly sorry, but that floor is occupied by other—”

“That one looks good.”

“W-wait a moment, Great Hero! Great Hero!”

The middle-aged man ignored the innkeeper’s desperate cries.

He strode up the stairs, ignoring the sharp gazes that poured down on him, and muttered,

“Much better. It’s quiet.”

The second floor of the inn was reserved for people of higher status.

It was only about twenty steps above the first floor, but unlike the noisy chaos below, a serious atmosphere hung over the second floor. Nor were the people seated at its tables anything like Third Rate martial artists.

“G-Great Hero! You can’t go up there!”

At the innkeeper’s cry from behind him, the low conversations abruptly stopped.

A graying middle-aged man seated at the table closest to the stairs frowned and spoke.

“Such noise. What is going on?”

“I-I’m sorry, Great Hero. This gentleman seems to have mistaken his place and—”

“Send him downstairs. And quiet down the first floor as well.”

“Yes, sir.”

But the middle-aged man was already walking somewhere else.

“That seat by the window looks fine.”

“Gasp, Great Hero!”

The one who stepped forward in place of the horrified innkeeper was the graying middle-aged man from before.

“Stop.”

The middle-aged man slowly turned around.

“Was that directed at me?”

“Who else would I be speaking to?”

“You?”

“You look a great deal younger than I am, so don’t cause unnecessary trouble. Go back downstairs.”

The graying middle-aged man added one more remark in a dignified tone.

“You appear to be lacking in worldly knowledge, so allow me to enlighten you. I am Fang of the Fang Family, widely known throughout the martial world by the sobriquet Moon Beauty Saber.”

“Oh.”

“That should be enough for you to understand. Now stop making a scene and go downstairs quietly.”

The middle-aged man blinked a few times before speaking.

“What you just said—was it really true?”

Moon Beauty Saber gave a short laugh.

Who was he? He was a top-tier wandering martial artist who had long since reached the level of injuring others with Sword Energy.

He was on an entirely different level from wandering martial artists like Blood Cudgel, who strutted around despite being merely at the early Peak realm.

“Heh heh. Why would I lie? Then again, I suppose it’s understandable that you don’t believe me. You probably never expected to meet me in a place like this.”

“No, not that. I meant, do I really look that way?”

“…?”

What was this man talking about?

Moon Beauty Saber stared blankly at the middle-aged man for a moment, then frowned.

“What do you mean? I don’t understand you at all.”

“You said I looked young. That was certainly true, wasn’t it?”

“…!”

“Hm. I don’t dislike hearing that. Good. I understand.”

Before Moon Beauty Saber could say another word, the middle-aged man let out a hearty laugh and raised a hand toward the window.

“Don’t mind me. Keep drinking. I happen to know someone.”

“Why, you bastard…”

“Great Hero!”

Moon Beauty Saber and the innkeeper shouted at the same time.

That was when the old man drinking alone by the window suddenly spoke.

“I was feeling lonely drinking by myself, so this is perfect. Come, sit.”

“…”

“…”

The innkeeper and Moon Beauty Saber both fell silent.

From the innkeeper’s perspective, the guest had said it was fine, so he had nothing more to say. Moon Beauty Saber, meanwhile, hesitated because of the old man’s manner—a manner that had been bothering him for some time.

*He looks like nothing more than a wealthy old man, but he also seems like no ordinary person… What connection could he have with that ignorant bastard?*

Moon Beauty Saber wanted nothing more than to teach the middle-aged man a lesson right then and there, but he felt strangely uneasy.

Whether he knew what Moon Beauty Saber was thinking or not, the middle-aged man dropped into the seat across from the old man and immediately tilted back a bottle.

“Ah, good. Is this Yeoahong?”

The old man nodded.

“The innkeeper said it had been aged for at least twenty years.”

“It’s good liquor. But among all liquor, strong liquor is still the best. The innkeeper will bring some soon, so have a taste.”

“I’ll pass. I don’t usually drink much.”

“What a shame. But why are you here alone?”

“It’s nothing. I simply thought I would try burying myself among other people after such a long time.”

The old man suddenly turned his head and gazed out the window.

He watched and listened to the many people passing through the street and the raucous noise for a while without speaking. Then he continued.

“Now that I’m here, it isn’t so bad. Being alone like this.”

“You don’t seem to have come alone.”

“Of course I have children and grandchildren. Just as you have a Disciple.”

“I do have one fellow who may be a Disciple or an enemy. But how did you know?”

“How could I not? I even saw him myself.”

Clack.

The middle-aged man set down the bottle with a loud sound.

Liquor had spilled from the corner of his mouth, dampening his beard. Perhaps because of the soft light, the beard looked unusually red.

“Damn it. I knew it. But that brat kept insisting to the very end that he’d never met you.”

“You certainly raised your Disciple well, Fire King.”

The middle-aged man wiped his beard with his sleeve, then stared at the old man.

“Last time, my Disciple caused you trouble. So I came to meet you myself, Azure Sky Sword King.”

The old man—no, the Grand Family Head of the Nangong Family and one of the Ten Kings, the Azure Sky Sword King—smiled faintly.

“That is most welcome news.”

“I knew you, of all people, would recognize this old man.”

“I almost failed to recognize you. Returned to Youth… It was worth waiting for.”

“May I keep the promise I made back then, even if I’m late?”

“I have been waiting for those words. For a very long time.”

Joy filled the Azure Sky Sword King’s eyes.

More than twenty years ago, in exchange for entrusting one person’s life to Jeok Cheongang, he had been promised a duel.

Today’s meeting was the fruit of that long wait.

“What a shame. The strong liquor will be here soon.”

“Let whoever is left standing drink it.”

“What about the sword? Will you be all right without one?”

“The sword?”

The Azure Sky Sword King picked up the two chopsticks lying neatly on the table.

“These will suffice.”

Jeok Cheongang gave a short laugh and looked out the window.

“The sky is blue, and you have a sword in your hand.”

“The sun is up as well, so the timing couldn’t be better.”

Whoooosh.

The wind blew.

Invisible waves of martial aura erupted from the two men’s bodies and swept through every direction.

And before anyone in the inn could notice, the two supreme masters struck at each other.

KABOOM!

* * *

Bang! Bang! KABOOM!

“Good Lord.”

*What in tarnation is that?*

I stood there gaping at the scene visible in the distance beyond the window.

No, it wasn’t only because of the successive booms or the black smoke rising high into the sky.

Unnamed, who realized it a moment after I did, spoke with a hardened expression.

“Did you feel it too, Benefactor?”

I gave a small nod.

A wave of qi that could be felt all the way here despite the considerable distance.

*This is a clash between at least Supreme Peak masters.*

“If something like this happened, then it must be…”

“Amitabha. Yes. It appears to be an assault by Dark Heaven.”

“Dark Heaven, those sons of bitches!”

“Though we took every precaution, this has happened again. Given that, this humble monk will have no choice but to break the precept against killing and go all out against them.”

“I’ll join you. I make a hobby of breaking the no-killing precept against Dark Heaven.”

And it seemed I wasn’t the only one with that hobby.

Ding. Diiing!

“Dark Heaven! It’s an attack by Dark Heaven!”

“Kill them and uphold justice!”

“Beat those wicked fiends to death!”

Along with the alarm bells ringing throughout the area, the Murim practitioners traveling along the main road rushed toward the disturbance like a pack of dogs.

It was a sight that made the blood boil.

*Ah, so this is the Murim Crusade.*

*Our side is fucking strong. And there are a hell of a lot of us.*

Until now, I had suffered every kind of hell against Dark Heaven because of our numerical disadvantage—or simply because of the gap in strength.

I was almost moved to tears.

*I can’t sit this one out.*

“Follow me! Follow me!”

Those who saw me leap out the window and stand tall widened their eyes.

“The Blazing Flame Divine Dragon!”

“It’s the Blazing Flame Divine Dragon of the Jin Family of Taiyuan!”

“Ooooooh!”

Believe it or not, I was quite a big name in Murim.

I was living proof that even a cramped backwater like Shanxi Province could produce a dragon! A young icon of the orthodox factions!

“Waaah!”

“Let’s go! Let’s sweep Dark Heaven away!”

“The Blazing Flame Divine Dragon is with us!”

Whoosh, whoosh, whoosh, whoosh!

The Murim practitioners, their courage redoubled, charged forward with a roar.

Needless to say, Unnamed and I were at the very front.

“Fuck! Wreck ’em all!”

When I shouted with all my internal energy behind my voice, the uproar grew even louder.

With this many Murim practitioners at my side, I was certain we could beat the hell out of any opponent.

“It’s a holy war!”

“Great Hero Jin says it’s a holy war!”

“Kill those demons!”

“Amitabhaaa!”

*You Dark Heaven bastards! Stay right there! I’m bringing the Murim Crusade to you, and I’m going to bash your heads in. Your heads…*

“Ah.”

My brain suddenly stopped working.

A single person was walking out from inside a building burning horribly.

“What the hell are you all doing?”

“…”

*The fiend was ours.*
## Chapter artifact 519

# Chapter 519

KABOOM!

A large inn was engulfed in flames. Blackened wooden pillars collapsed, sending clouds of ash into the air. The face of the fiend who emerged through the wreckage was so familiar that it was shocking.

“What the hell are you all doing?”

“…”

*That’s what I wanted to ask.*

A moment of silence followed. Unnamed’s gaze trembled as he stared at me, as though an earthquake had struck. Sound Transmission slipped through his faintly moving lips and pierced my ears.

*Why, why is Benefactor Jeok coming out of there?*

*How should I know?*

*Wasn’t he Dark Heaven?*

*That’s what I want to ask.*

*Amitabha. Could you be Dark Heaven?*

*What kind of crazy question is that?*

*If we’re Dark Heaven, does that make you a member of the Vatican?*

I wasn’t the only one dumbfounded by Unnamed’s words. Jeok Cheongang, who was exceptionally skilled at eavesdropping on Sound Transmission, already had a face twisted like an evil spirit.

“What? This old man is Dark Heaven?”

“N-no, that’s not what I meant. There’s been a small misunderstanding…”

To get straight to the point, my attempt to clear up the misunderstanding ended in failure.

More precisely, our proud Murim Crusade, already burning with fighting spirit ahead of the founding of the Murim Alliance, refused to let it happen.

“Dark Heaven!”

“The fiend just declared himself Dark Heaven!”

*Keyword entered.*

“Wait a moment. He seems to know the Blazing Flame Divine Dragon.”

“Of course he knows him! How many times has the Blazing Flame Divine Dragon fought Dark Heaven?”

“I see. He’s a Dark Heaven fiend!”

*The miracle of logic.*

“You fiend! You look like a demon straight out of hell!”

“His hair is red as blood. He looks like the type to dye the world red!”

*Personal attacks based on appearance.*

“Kill him first!”

“Capture him and you’ll become a hero!”

*Medieval Crusader-style conclusion reached.*

The entire chain of events took place in less time than could reasonably be called an instant.

Faced with the collective madness of more than a thousand Murim Crusaders, Unnamed and I—both of us standing there in a daze—hurriedly waved our hands.

“No! That’s not it!”

“Amitabha! Everyone, stop! That man is not a fiend! He is the late Master Hong Dao’s…”

At Unnamed’s shout, the Murim practitioners who were relatively close widened their eyes.

“Gasp.”

“Is that true?”

*Now we’re finally getting somewhere.*

Unnamed looked at me with exactly that expression and nodded.

“It is.”

“Good heavens. Not just an ordinary fiend, but the culprit who did that to Master Hong Dao!”

“What?”

“What an unforgivable fiend! Tear that bastard limb from limb!”

“…”

*Fuck. I can’t work with this.*

Did these martial artists suffer qi deviation whenever they listened to someone all the way to the end? They simply refused to understand a single word anyone said.

And the grand finale of this collective madness was provided by an unfamiliar figure emerging from the wreckage of the collapsed building.

“Stop, you wicked fiend! How dare you commit such a heinous crime in Henan!”

Jeok Cheongang, who had been staring at the situation with his mouth hanging open, muttered with a grim expression.

“Not one of these people is in his right mind. First, listen to what this old man has to say…”

“Enough talk! This Moon Beauty Saber will not forgive you!”

“…Let’s start with you taking a beating.”

Fair enough. Considering Jeok Cheongang’s personality, he had shown remarkable restraint up to that point.

Whoosh. Fwoom!

*Moon Beauty Saber, enjoy your ride on the Disco Pang Pang.*

Moon Beauty Saber’s figure, rushing forward like a streak of light, flew backward like a cannonball and slammed deep into the wreckage.

The punch was something none of the martial artists gathered there had seen—or had even been capable of seeing.

The overwhelming force of that punch instantly froze the air around them.

“Moon Beauty Saber was sent flying in a single blow…!”

“Aaah! The fiend’s martial arts have reached the heavens!”

*Forget his martial arts. His anger looks like it has reached the heavens.*

And regardless of whether I was here or not, it seemed everyone understood that they absolutely should not provoke Jeok Cheongang in his current mood.

Everyone wanted to defeat a fiend and make a name for themselves. But no one wanted to be defeated in the process. That was human nature, wasn’t it?

*It’s finally quiet.*

Now that everyone had fallen silent, this was my only chance to clear up the misunderstanding.

I cleared my throat and opened my mouth.

Or rather, I was about to.

“There seems to be a serious misunderstanding. The person over there isn’t a fiend, but—”

“Yaaah! Make way!”

“Oh, for fuck’s sake!”

*I’m going to lose my mind. Who is it this time?*

But the intruder who appeared through the wall of people splitting apart like the Red Sea was not someone I could simply call a bastard.

“The Thunderbolt Saber King has arrived!”

“Great Hero Peng has come to personally punish the fiend!”

Thud. Thud.

An enormous old man walked forward through the atmosphere of renewed courage.

Broad shoulders. Bulging eyes. A massive saber slung over one shoulder.

At the sight of the Thunderbolt Saber King, Jeok Cheongang sighed.

“Someone who can finally understand what people are saying has arrived.”

*I agree.*

The Thunderbolt Saber King might bicker with Jeok Cheongang constantly, but the two were actually quite close.

He was the sort of person who could be described as a longtime archrival, but read as a friend.

Surely he would recognize Jeok Cheongang’s identity without any trouble.

As expected, the Thunderbolt Saber King looked Jeok up and down, then opened his eyes wide.

“What are you doing here?”

“It’s a long story. First, make these people withdraw.”

“Answer my question first.”

“Hm?”

“I asked what a bastard fiend who deserves to be torn limb from limb is doing here.”

“…”

“…”

Jeok Cheongang’s eyelids began to tremble.

* * *

Clip-clop. Clip-clop.

In the quiet silence, the only sound was the steady rhythm of horse hooves.

The enormous old man, who had been silently watching the scenery outside the carriage, suddenly spoke.

“To tell you the truth, I recognized you the moment I saw you. There was no way I wouldn’t.”

With people watching him, the Thunderbolt Saber King continued in a serious voice.

“Red hair and a red beard. Anyone would know you were the Fire King. The others couldn’t have dreamed that you had Returned to Youth, but I was able to figure it out.”

“I see.”

I nodded, then asked,

“Then why did you suddenly start swinging your saber?”

“That was…”

“Oh, and I’d also like an explanation for why you ordered an all-out attack after getting cold feet from exchanging a single move.”

“Getting cold feet? Hahahaha.”

A heavy silence descended once more.

Faced with the distrustful eyes of everyone—including me—the Thunderbolt Saber King spoke with a stiff expression.

“It was to give them experience in actual combat.”

“Ah. Actual combat.”

“A foundation for the battle against Dark Heaven that will soon take place. If their opponent was the Fire King, Jeok Cheongang, then wouldn’t it be valuable experience for all of them?”

I asked seriously,

“By ‘experience,’ do you mean experience of the afterlife?”

“…”

The Thunderbolt Saber King fell silent, as though he had swallowed honey.

If he had any conscience at all, he had no choice but to do so. The number of people carried to the medical clinic alone was close to twenty.

Most of them were Third Rate martial artists who had been caught in the aftermath of the attacks exchanged between the Fire King and the Thunderbolt Saber King—the two Ten Kings.

*It was fortunate that it ended there.*

If the poet Yun Dong-ju suffered at even the wind stirring a leaf, they suffered like hell in the howling blade wind.[^1]

“Still… I heard everyone is safe.”

“They’re safe. At least for the next two weeks. They’ll be lying in the medical clinic the whole time.”

The results of their afterlife experience were undeniable.

No matter how accustomed martial artists were to living on the edge of a blade, PTSD was not something to dismiss.

I had visited the victims in the medical clinic. Their faces had gone pale, and they couldn’t even speak.

The worst of all was the wandering martial artist called Moon Beauty Saber. He was trembling so violently that I almost mistook Henan for Antarctica’s King Sejong Station.

“None of this would have happened if Great Hero Peng hadn’t ordered that all-out attack.”

At my continued barrage of criticism, the Thunderbolt Saber King raised his round eyes.

“And what about you?”

“Me?”

“Yes, you! Wasn’t it you who rounded up every martial artist in the area and brought them here?”

“I admit that part. But given the circumstances, it was unavoidable. Isn’t that right?”

At my question, Unnamed—the accomplice sitting in a corner—ran his fingers over his prayer beads.

“Benefactor Jin is correct. Even if Shakyamuni had been in my position, he would have rushed forward crying out for the destruction of demons.”

“Could you uproot a bodhi tree and crush the fiend’s skull with it?”

“Amitabha. It is possible.”

“…”

The Thunderbolt Saber King had just as much of a temper as Jeok Cheongang, but he couldn’t openly bully Unnamed.

Unnamed, the only Disciple left behind by his close friend the Dharma King Hong Dao, was someone the Thunderbolt Saber King couldn’t help but feel protective of.

“Grrr.”

After making a pained sound, the Thunderbolt Saber King glared at me and shouted,

“But you’ve been mouthing off since earlier!”

“What? Why?”

“Are you close with me?”

“No.”

“Then do you think the Hebei Peng Family is a joke?”

“How does that follow? You have nothing left to say, so you’re just muddying the issue.”

“You’re a kid whose blood hasn’t even dried on his head, yet you keep talking back to me…”

“Oof. Clack, clack. Dentures.”

I had no idea exactly what the dentures were supposed to imply, but the emotion contained in my words clearly got through.

“How dare you!”

The Thunderbolt Saber King’s face flushed red, and he was just about to leap to his feet when the two people who had remained silent throughout the journey spoke almost simultaneously.

“Calm yourself, Sir Peng.”

“Quiet. All of you, shut your mouths.”

The two voices and atmospheres were completely different.

Perhaps the only thing connecting the two men was the two characters in their title: Ten Kings.

“I was rash. My blood was running hot after so long, and I lost control.”

The Azure Sky Sword King calmly admitted his mistake.

Jeok Cheongang followed after him.

“This old man did nothing wrong. You were the ones being rash.”

“…”

*That’s our Old Master.*

He was an evergreen tree, if ever there was one.

The Thunderbolt Saber King stared at Jeok with an expression that seemed to ask whether he was even human, then spoke.

“Jeok, do you feel even a little guilty?”

“Why should this old man feel guilty? When martial artists meet, they can have a little brawl. There were already people fighting when I entered the inn.”

“What would have happened if Great Hero Nangong hadn’t stepped in at the right moment?”

As the Thunderbolt Saber King said, the dove of peace who had brought the situation under control was the Azure Sky Sword King.

After a brief exchange with Jeok Cheongang, he had suffered a minor Internal Injury. He only appeared after settling his internal energy, and one of the Nangong Family members among the gathered heroes recognized him.

*Whoa, whoa, whoaaaa! Grand Family Head!*

It was a scream as though he had seen a ghost.

The other Murim practitioners, whose eyes had been blinded by the words *Dark Heaven*, finally returned to their senses as well.

There was even one lunatic who asked whether the Nangong Family was Dark Heaven, but fortunately, the members of our proud Murim Crusade managed to regain their sanity.

In truth, if Jeok Cheongang hadn’t Returned to Youth, at least a few people would have recognized him.

“That was almost a catastrophe!”

“I could have explained everything. And it happened because your eyes are as bad as a dog’s, you Peng bastard.”

“The inn collapsed! People were injured!”

“Ahem.”

Perhaps he felt a bit guilty himself. Jeok Cheongang cleared his throat, then opened his mouth with a shameless expression.

“It was the location, so this old man controlled his strength appropriately. At most, they were struck by a few pieces of falling debris. At that level, some spit would fix them right up. This old man will compensate the innkeeper sufficiently. Even I admit that the place burned rather badly.”

“Is that really coming from the man who killed a thousand members of the Demonic Cult because they burned down Mount Jiuhua? The more I listen, the more my chest swells.”

“Those bastards obviously had to die. They never intended to pay compensation in the first place.”

“…”

*What is this?*

It was completely unreasonable, yet it somehow felt strangely logical.

The Thunderbolt Saber King, momentarily left speechless, muttered,

“Returned to Youth only changed the skin you’re wearing. The contents are still the same. Your personality is still completely fucked.”

“You should try changing the skin on your face, Peng bastard. What kind of person grows old without even Returning to Youth?”

“What did you say?”

“Ho. They say a man who failed to Return to Youth gets angry when reminded of it. You’re a perfect example.”

“How dare you, Jeok!”

“Hm? What did you say? I can’t hear you. The words of an insignificant nobody who couldn’t even Return to Youth are hard to make out.”

*Would you look at him dealing some clean area-of-effect damage.*

Everyone else might have missed it, but I saw the Azure Sky Sword King’s shoulders twitch from his seat by the carriage window.

Then, as he stealthily avoided my gaze and looked out the window, his lips suddenly parted.

“You two should stop now.”

At first, I thought he was simply trying to change the subject.

Then I followed his gaze out the window and muttered,

“Yeah. You definitely should.”

At the end of my line of sight stood a long stretch of city walls and a massive crowd.

And above the iron gates was a huge sign bearing three characters written in a bold, soaring hand.

**Murim Alliance.**

[^1]: Yun Dong-ju was a Korean poet of the Japanese colonial period, known for poetry marked by intense sensitivity and introspection.

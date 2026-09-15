# Checkpoint Review — 180–184

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

# Chapters 180–184

## Plot

The Jin Family of Taiyuan opens a three-day New Year’s Day banquet and publicly declares its rise as Shanxi Murim’s hegemon. Jin Wikyung finalizes an alliance with Wolhwa’s Lower District Sect, while the family receives support and visitors from Huashan, the imperial family, and major Shanxi factions. News also arrives that the Heavenly Wind Band was annihilated near Datong by an unknown Supreme Peak master; Wikyung privately suspects Sword Saint Mae Jonghak.

Jin Taekyung, Hyuk Mujin, and Cheongpung return after three days away, with Taekyung still carrying Jeok Cheongang’s Unnamed Sword. At the crowded gates, Chulwoo of Huashan’s Three Plum Blossom Elites provokes Woo Hwangtae, then fights Taekyung when Taekyung intervenes. Their evenly matched exchange is stopped by Wipeng, and the two return together while the crowd mistakes their rivalry for sudden friendship.

Inside the gathering, Baek Museong formally greets Cheongpung as his Martial Uncle, though Cheongpung fails to recognize him. Meanwhile, Gong Ilhyuk tells the Roaring Fury Swordsman that Cheongpung is the Sword Saint’s Disciple, sending the furious Zhongnan elder and the Three Hands of Zhongnan toward the Jin Family.

## Continuity

- Jin Wikyung has led the Jin Family in place of the absent Family Head for two years and established it as Shanxi Murim’s hegemon.
- The Jin Family and the Lower District Sect have formed a cooperative alliance.
- The Heavenly Wind Band was destroyed near Datong by an unidentified Supreme Peak master; Wikyung suspects Mae Jonghak.
- Taekyung returned late to the banquet after leaving to commission Jang Taebo to forge the Ten-Thousand-Year Cold Iron. The Treasured Jade remains missing.
- Taekyung, Mujin, and Cheongpung are back in Taiyuan; Taekyung is temporarily carrying Jeok Cheongang’s Unnamed Sword outside his inventory.
- Jin Mukyung remains in seclusion training after receiving enlightenment.
- Baek Museong, Chulwoo, and Eunhyang are Huashan’s Three Plum Blossom Elites. Baek is Cheongpung’s Martial Nephew; Chulwoo is a Level 95 early-Peak martial artist known as the Defeated Flower Fist; Eunhyang is the Flower Sword Phoenix.
- Taekyung and Chulwoo fought without a decisive result before Wipeng intervened. Their public image is now that of close companions, despite their continuing private rivalry.
- Woo Hwangtae sought an apology concerning Woo Jintae, clashed with the Jin Family’s gathering, and was targeted and beaten by Chulwoo before Taekyung intervened.
- Cheongpung is Mae Jonghak’s Disciple and the youngest Junior Brother of Huashan’s Heavenly Sword True Person. He did not recognize Baek’s relationship to him.
- The Roaring Fury Swordsman and the Three Hands of Zhongnan are approaching the Jin Family to verify Cheongpung’s identity and confront the gathering.
- Open hooks: the identity of the Supreme Peak master, the consequences of Taekyung’s absence and Woo Hwangtae’s conflict, completion of Taebo’s weapon, the location of the Treasured Jade, Jeok’s intentions toward Taekyung, and the Zhongnan elder’s response.

## Translation Decisions

- Render 원단 as “New Year’s Day,” 천풍단 as “Heavenly Wind Band,” 천검진인 as “Heavenly Sword True Person,” and 매화삼절 as “Three Plum Blossom Elites.”
- Render 수문각 as “Gate Guard Pavilion,” 장주 as “Lord,” 패화권 as “Defeated Flower Fist,” and 화검봉 as “Flower Sword Phoenix.”
- Render 산서기협 as “Shanxi Extraordinary Hero,” distinct from 산서괴협.
- Render 절정 초입 as “early Peak” and 권기 as “fist qi.”
- Render 화산파 일대제자 as “First-generation Disciple of Huashan,” 사숙 as “Martial Uncle,” 노호검객 as “Roaring Fury Swordsman,” 하곡문 as “Hequ Sect,” and 양천 as “Yangcheon.”
- Treat 화산말학 and 매화손절 as Taekyung’s mistaken hearings of established Huashan titles.

## Durable state

{
  "active_continuity": [
    "Jin Wikyung has led the Jin Family in place of the absent Family Head for two years and established it as Shanxi Murim's hegemon.",
    "The Jin Family is holding a three-day grand banquet beginning on New Year's Day, with support from Huashan, the imperial family, and Shanxi Murim.",
    "Jin Wikyung and Wolhwa finalized a cooperative alliance between the Jin Family and the Lower District Sect.",
    "The Heavenly Wind Band was annihilated near Datong by an unknown Supreme Peak master; Jin Taekyung privately suspects Mae Jonghak.",
    "Jin Taekyung is absent while having a weapon forged and has stopped sending news; Jin Mukyung is undergoing seclusion training after enlightenment.",
    "Woo Hwangtae sought an audience and apology regarding Woo Jintae, became enraged at the Jin Family's representatives, and was prevented from escalating the conflict.",
    "Baek Museong and the Huashan group are present at the Jin Family; Baek Museong is the first Senior Brother of the Three Plum Blossom Elites and has now formally greeted Cheongpung as his Martial Uncle.",
    "The Treasured Jade remains missing.",
    "Jang Taebo is forging Taekyung's commissioned weapon.",
    "Chulwoo is the second of the Three Plum Blossom Elites, bears the epithet Defeated Flower Fist, and is a Level 95 early-Peak martial artist; he did not recognize Cheongpung as his Martial Uncle.",
    "Eunhyang is the youngest junior disciple in Baek Museong's group, bears the epithet Flower Sword Phoenix, and was found after becoming separated in the crowd.",
    "Taekyung, Hyuk Mujin, and Cheongpung returned to Taiyuan after three days away.",
    "Taekyung is temporarily carrying Jeok Cheongang's Unnamed Sword outside his inventory.",
    "Cheongpung has speculated that Jeok Cheongang may want Taekyung as his Disciple; this is unconfirmed.",
    "Chulwoo singled out Woo Hwangtae from the crowd, fought with Taekyung, and returned with him after Wipeng intervened.",
    "At the Jin Family gathering, Taekyung was mobbed by Shanxi power players, including Jang Se-pal, leader of the small Hequ Sect, and received multiple marriage proposals.",
    "Cheongpung is Mae Jonghak's Disciple and the youngest Junior Brother of the current Huashan Sect Leader, the Heavenly Sword True Person; Baek Museong is therefore his Martial Nephew.",
    "Gong Ilhyuk has told the Roaring Fury Swordsman that Cheongpung is the Sword Saint's Disciple and is leading the elder toward the Jin Family's gathering.",
    "The Roaring Fury Swordsman is a fiery-tempered elder of the Zhongnan Sect who has decided to verify Cheongpung's identity and confront the Jin Family's gathering."
  ],
  "continuity_sources": [
    184
  ],
  "open_questions": [
    "Who annihilated the Heavenly Wind Band near Datong?",
    "What consequences will follow Taekyung's absence from the Jin Family's grand banquet?",
    "When will Jang Taebo complete Taekyung's weapon?",
    "Who has the Treasured Jade, or was it lost by Jopil?",
    "Does Jeok Cheongang actually intend to take Taekyung as his Disciple?",
    "What consequences will follow Woo Hwangtae's conflict with Chulwoo and the Jin Family?",
    "How will Baek Museong and Cheongpung respond after Cheongpung failed to recognize their relationship?",
    "What will the Roaring Fury Swordsman do when he reaches the Jin Family's gathering?"
  ],
  "safe_through": 184,
  "temporary_decisions": [
    "Render 원단 as “New Year's Day,” 천풍단 as “Heavenly Wind Band,” 천검진인 as “Heavenly Sword True Person,” and 매화삼절 as “Three Plum Blossom Elites.”",
    "Render 수문각 as “Gate Guard Pavilion.”",
    "Render 장주 as “Lord.”",
    "Render 패화권 as “Defeated Flower Fist.”",
    "Render 산서기협 as “Shanxi Extraordinary Hero,” distinct from 산서괴협.",
    "Render 절정 초입 as “early Peak” and 권기 as “fist qi.”",
    "Render 화산파 일대제자 as “First-generation Disciple of Huashan,” 사숙 as “Martial Uncle,” 노호검객 as “Roaring Fury Swordsman,” 하곡문 as “Hequ Sect,” and 양천 as “Yangcheon.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 180

# Chapter 180

*New Year's Day.*

Jin Wikyung’s reaction upon seeing the sunlight on the first day of the new year was short and simple.

“Fantastic.”

Wolhwa, who had been tilting her teacup with graceful composure, let out a quiet laugh. She had arrived at the Jin Family of Taiyuan the previous night.

Considering the family’s policy of barring anyone who wasn’t a member of the family from entering at present, it was a measure of respect for their alliance.

“Are you really that happy?”

“How could I not be?”

“I suppose you have every reason to be. When you think about everything that’s happened, it’s understandable. I never thought a day like this would come, especially two years ago.”

“That hurts to hear.”

Wolhwa covered her mouth in exaggerated dismay.

“My goodness, shouldn’t I be the one saying that? We’ve been waiting for you for so long.”

“I’ll keep my promise. I swear.”

“I hope so. It would be troublesome if you changed your word twice.”

“Let’s stop. I’m tired.”

“Likewise.”

The previous night had been a long one. After an intense back-and-forth, they had finally found an agreement that satisfied both sides.

In any case, both sides needed each other’s help if they wanted to wield influence in Shanxi Murim.

At last, Wolhwa, having obtained what she wanted, smiled coyly.

“Still, our side did give you one valuable piece of information, didn’t we?”

Jin Wikyung answered with a sullen expression.

“Oh, that information? I heard the Datong Branch of our family played some part in it as well.”

“We were the ones who brought the information to you in the first place. We were also the ones who promptly sent a messenger eagle.”

“That much… I’ll admit.”

Wolhwa suddenly narrowed her eyes.

“But aren’t you worried?”

“About what?”

“The Heavenly Wind Band.”

The news that the Heavenly Wind Band, which had been prowling around Datong, had been annihilated was certainly good news. But it was also shocking beyond measure.

A single person had wiped out hundreds of mounted bandits, including a Peak master? It was nearly impossible unless the person was a Supreme Peak master.

Wolhwa ran one of her long fingers along her teacup.

“Who do you think it was?”

“Who knows? We’ll have to find out in time.”

Jin Wikyung secretly swallowed a laugh. No matter how vast the world was and how many reclusive eccentrics it contained, Supreme Peak masters were never common.

When he first heard the news about the Heavenly Wind Band, only one name had flashed through his mind.

Sword Saint Mae Jonghak.

*It’s highly likely that it was him.*

Considering the relationship they had built over the years, he ought to tell Wolhwa as well. But the matter was far too weighty to share with the Chief Branch Leader of the Lower District Sect.

“Don’t worry too much. Our family is keeping a close eye on the situation.”

“For someone saying that, you look awfully relaxed.”

“How could I be relaxed? I merely assume that whoever annihilated the infamous Heavenly Wind Band wasn’t a master of demonic or heterodox arts.”

Wolhwa narrowed her eyes at his answer, delivered as though he knew nothing.

But it was difficult for her to question him further. If the Jin Family of Taiyuan had truly been connected to a Supreme Peak master, the family’s rise to its current position would have been far easier.

“Well, in any case. My sincere congratulations.”

“Thank you.”

“But one of you has been silent this whole time.”

Knowing exactly whom Wolhwa meant, Jin Wikyung shook his head.

“He’s been dissatisfied since birth.”

A prickly voice asked,

“Are you talking about me?”

“Who else would I be talking about?”

Wipeng, who had been leaning diagonally against the wall of the office, opened his mouth.

“I wholeheartedly agree with my lord. It truly is a fantastic day.”

“What’s gotten into you? Whenever I say something like that, you’re always lecturing me about dignity and propriety.”

“How else am I supposed to describe something fantastic?”

His subordinate, who was as fussy as an old schoolmaster, was humoring him for once. Jin Wikyung smiled in satisfaction.

“Exactly. That’s how important this occasion is going to be.”

“Can you hear the murmuring from far away? I hear that not only the influential martial artists of Shanxi Murim, but even commoners who heard the news have come.”

“Oh, is that true?”

“Of course. And a letter of congratulations has arrived from the Heavenly Sword True Person, the Sect Leader of Huashan.”

“Oh!”

“The Three Plum Blossom Elites should be arriving soon as well.”

Jin Wikyung already knew all of this, but it still felt good to hear it again.

The Nine Sects and One Gang were pillars of the Murim world, and their influence was immense. Even if only part of them had come, it was practically the same as having the entire orthodox Murim vouch for the legitimacy of the Jin Family of Taiyuan.

Of course, he couldn’t deny that matters involving the Sword Saint and Cheongpung had played a significant role.

“And that’s not all. Isn’t Prince Shangshan, a descendant of the Son of Heaven, coming as well? This means that both the government and the Murim have acknowledged our family as the undisputed hegemon of Shanxi Province.”

“Of course! Absolutely!”

Watching Jin Wikyung grow more cheerful by the moment, Wipeng smiled.

“Do you know what the even better news is?”

“You’re really going all out today. What is it? Tell me already!”

The next moment, the smile at the corners of Wipeng’s mouth vanished without a trace.

“At this gathering, where countless martial artists and commoners, distinguished guests from the Nine Sects and One Gang, and even a descendant of the imperial family are coming, both Young Masters are absent.”

“…Ah.”

“I can at least understand the Second Young Master. Enlightenment doesn’t come whenever you want it to, so undergoing seclusion training is understandable. I’m a martial artist too. But!”

Wipeng continued with a fierce glare.

“The Third Young Master absolutely cannot be let off the hook. It wasn’t enough for him to leave at a time like this as if none of it concerned him—on top of that, all word from him has completely stopped.”

Jin Wikyung subtly averted his gaze. Wolhwa, his only lifeline, shrugged as if she didn’t know anything either and watched the spectacle.

“He’ll come.”

“What do you mean, he’ll come? He left last year saying he’d be back shortly.”

Jin Wikyung was about to object, then paused. When he thought about it, Wipeng’s words sounded strange, but they weren’t wrong.

Wipeng ground his teeth and continued.

“Going off to make a weapon when we’re facing such a momentous occasion… I’m an idiot for trusting the Third Young Master even for a moment.”

“Now, now.”

“Am I wrong?”

“Now, hold on!”

“Why? What about it?”

Jin Wikyung flinched at Wipeng’s bulging eyes. Then a voice of salvation came from outside the office.

“Lesser Family Head, the preparations are complete.”

“…There you have it.”

Wipeng’s lips moved as if he wanted to say something, but he let out a deep sigh instead. It wasn’t as though this had only happened once or twice. They had to deal with what was right in front of them first.

“This time, you must give the Third Young Master a proper talking-to.”

“Of course I will.”

Jin Wikyung grinned and left the office.

Fifty martial artists radiating sharp auras stood in formation before the pavilion. Every one of them was at least a First Rate master, and they stared at their lord with unwavering composure.

Jin Wikyung was a giant standing eight cheok tall. As the Lesser Family Head of the Jin Family of Taiyuan, he had led the family in place of the absent Family Head for the past two years and had finally set it on a firm foundation.

His tightly closed lips parted.

“Let’s go.”

Wipeng, Wolhwa, and the fifty martial artists followed behind him. And each time they crossed another part of the quiet Jin Family of Taiyuan’s grounds, their numbers grew.

Fifty became a hundred, a hundred became two hundred, and two hundred became three hundred…

The Jin Family of Taiyuan had suffered the pain of losing limbs during the previous war, but its recovery had been swift, and its growth had been steep.

*Our family has grown stronger.*

The One Pavilion, Two Halls, and Three Teams advancing alongside him were proof of that.

They were the arms and legs, the waist and torso of the Jin Family of Taiyuan, which had grown stronger and sturdier.

Remembering the countless sacrifices and efforts that had been required to reach this day, Jin Wikyung felt his chest tighten with emotion.

“Lesser Family Head.”

Before he knew it, they had reached the Gate Guard Pavilion.

The gate guards standing watch at the main entrance bowed with crisp, disciplined movements. Beyond the flawlessly built stone walls, the cheers of countless people could be heard.

“Wow, this really is fantastic.”

“My lord, give the order.”

Wolhwa was smiling brightly, while Wipeng wore a more solemn expression than ever.

Jin Wikyung took in their faces and drew a deep breath. The next moment, his dignified voice rang out.

“Open the gates.”

It was the beginning of the grand banquet that would continue for the next three days—and the opening salvo announcing that the Jin Family of Taiyuan had become the hegemon of Shanxi Murim.

* * *

The area in front of the Jin Family of Taiyuan’s gates was packed with people. Martial artists wearing swords and blades, merchants trying to seize an opportunity, and commoners who belonged to neither side.

Even though it was broad daylight, firecrackers celebrating the first day of the new year went off now and then.

*Boom! Boom-boom!*

“Waaaaah!”

While well over several hundred people laughed and chatted in the festive atmosphere, some wore faces like they were attending a funeral.

“Damn it.”

“What kind of situation is this?”

“I ought to just—”

The five middle-aged men, the heads of the five sects known collectively as the Five Gates of Shanxi, couldn’t smooth out their crumpled expressions.

Of them, Woo Hwangtae, the chief of the Seongun Escort Bureau, was in the worst state by far, shitting himself with worry thanks to his worthless son.

*They wouldn’t even grant me an audience.*

He had arrived five days earlier and asked for a meeting countless times.

He had come to clean up after the mess caused by his son, Woo Jintae.

But the letters and gifts he had carefully sent were returned without ever crossing the threshold of the Jin Family of Taiyuan. His pride had been wounded, but in the end, he had even resorted to coming in person.

*I am Woo of the Seongun Escort Bureau.*

The Seongun Escort Bureau had continued for three generations, and there was no one in Shanxi Province who didn’t know it. That was because it had flaunted enormous wealth amassed by every means imaginable.

But the gate guard’s reaction had been indifferent.

*You can’t meet him right now.*

“Come now, man. What do you mean? I’m telling you, I’m the chief of the Seongun Escort Bureau!”

*Whether you’re a bureau chief or a sect leader, I don’t know or care. I follow orders.*

*…!*

Had he ever suffered such humiliation in his life?

Like Woo Jintae, he had always enjoyed every advantage of his family’s prestige. He had experienced a few failures and had been ignored by people of higher status, but he could endure that much.

But to be treated like this by some mere gate guard!

Every time he thought about it, the back of Woo Hwangtae’s head throbbed.

*Those fucking bastards. No matter how powerful they are, how can they treat someone like this?*

His own son, who even had a child of his own, had come back beaten so badly that it was difficult to tell whether he was human or some blue-skinned beast.

Father and son had been publicly humiliated at the same time. It was too embarrassing to complain about it to the other sect leaders.

“Huff… Hoo…”

The other heads of the Five Gates of Shanxi watched him cautiously as he exhaled through his flushed face.

“Chief Woo, are you all right?”

“If you’re feeling unwell, perhaps we should come back tomorrow…”

Woo Hwangtae answered in a sharp voice.

“Would you be all right, Sect Leader Song? My son was beaten like a street dog, and now we’re in a position where we have to apologize on top of that. And, Lord Tae, if I retreat like this, what will the Jin Family of Taiyuan think? Are all of you seriously saying that?”

“…”

“…”

The two men who had spoken flinched after drawing his ire, while the other two let out sighs of relief.

But inwardly, all four of them were thinking the same thing.

*This damned merchant, I ought to just…*

They were only enduring him because they still needed the Seongun Escort Bureau’s support.

They clearly remembered what their respective sons had told them.

*The Sleeping Dragon of Shanxi said he would make the Seongun Escort Bureau an example.*

*Chief Woo and that man aren’t ordinary people… Unless it’s the Nine Sects and One Gang, how do they plan to swallow it whole at once?*

*Given the Jin Family of Taiyuan’s recent power, maybe they can.*

*For now, we watch.*

If the balance tipped even slightly, they would have to change sides. The four men were gauging the right moment, and as long as they could preserve their respective families, they could face Woo Hwangtae with smiles on their faces.

“Ha-ha, Chief Woo. Calm yourself.”

“Indeed. You and we are equally aggrieved, aren’t we? It’s not that we don’t understand how you feel.”

“Let’s go in soon. We can’t stand here watching forever.”

“Here, these pills came from a renowned physician. They have the effect of calming even the most fiery temper. Let’s each chew one before we go in.”

“Hoo…”

Woo Hwangtae let out a heated sigh and was just about to toss the pill into his mouth when—

“Wow, there are a lot of people here. They’re really swarming.”

Along with the booming voice, something shoved against his arm. The pill dropped, and someone immediately stepped on it.

“...!”

That was the limit of Woo Hwangtae’s patience. He glared at the culprit with eyes blazing like fire.

The man was a full two heads taller than everyone else. With his cow-like eyes and the way he was picking his nose, he looked every bit the country bumpkin.

“You! Stop right there!”

The huge man came to an abrupt halt.

“Huh? Me?”

“Yes, you bastard! If you knock into someone, you should apologize immediately!”

“Ah. There were so many people, I didn’t notice. Sorry ’bout that.”

The man quickly bowed and turned away, but Woo Hwangtae’s anger only flared hotter.

The humiliation his son had suffered. The memory of being ignored by the gate guard for days. And now this oversized country bumpkin’s behavior had lit the fuse.

“You ox-headed bastard! Stop right there!”

The giant flinched.

“What did you just say?”

“I called you ox-headed. You bastard, you’re worse than an ox!”

“That’s one of the things I hate most.”

“If you hate it, what are you going to do about it?”

The giant snorted a plume of breath before opening his mouth.

“Can I hit him?”

“You bastard, I’ll kill—!”

Just as Woo Hwangtae was about to strike, a clear voice came from behind him.

“No.”

The speaker was a clean-cut young man.

Baek Museong, Huashan’s Lone Crane, had stopped his Junior Brother just before he exploded. He smiled at Woo Hwangtae.
## Chapter artifact 181

# Chapter 181

“You cause trouble whenever I take my eyes off you, even for a moment.”

After lightly scolding his Junior Brother, Baek Museong bowed his head toward Woo Hwangtae.

“It seems there was a minor misunderstanding between you. I hope you’ll forgive him with your broad magnanimity.”

His voice was as gentle as his appearance.

Woo Hwangtae was closer to a merchant than a martial artist. His martial arts were First Rate, but he could pride himself on having a Peak-level eye for people and situations, honed through years of running an Escort Bureau.

Under normal circumstances, he might have thought this upon seeing Baek Museong:

*The extraordinary within the ordinary.*

Unfortunately, Woo Hwangtae was not in his right mind at the moment.

Baek Museong had stepped in out of nowhere, and his clean-cut appearance made him seem like an easy mark. His polite voice carried a strong man’s composure, but to Woo Hwangtae, it sounded merely insolent.

“What did you say? Forgive him with my broad magnanimity?”

His voice bubbled with rage as he raised his eyebrows.

“How dare you order me around?”

“That was not my intention, but if I’ve offended you, I apologize.”

“An apology? Hah. You little pup.”

Crack.

Once anger took hold, a person’s judgment naturally grew clouded.

As Woo Hwangtae stepped forward with his fists clenched, the other Sect Leaders hurriedly tried to restrain him.

“Chief Woo, it would be best to stop here.”

“Sect Leader Song is right. Nothing good will come of making a scene.”

“Some bastards who God knows where they rolled in from are acting arrogant, and you’re telling me to put up with it? Do you all think lightly of me too?”

“No, that’s not what we meant.”

“Then what are you trying to say?”

His tone was now nearly that of someone speaking down to them. The Sect Leaders of the Five Gates of Shanxi frowned inwardly, but they had to prevent an unnecessary conflict.

“We only mean that this is the wrong time and place. Have you forgotten our situation?”

“If you insist, I won’t stop you anymore, but… there’s no need to cause trouble when the Jin Family of Taiyuan already has us in its bad books.”

“We understand that you’re angry, but please think of our situation as well. Let’s all try to survive.”

Again. Again with the Jin Family of Taiyuan!

Woo Hwangtae barely managed to swallow the curses that were about to burst from his mouth. If not for the countless eyes and ears around him, he would have hurled every curse he knew and smashed everything in sight.

But the last shred of reason held him back.

“Nggh.”

After barely calming himself, Woo Hwangtae glared at Baek Museong. He was still standing there with a calm expression.

“I’d like nothing more than to beat you to death with a single blow right now, but… I’ll let it pass as a country bumpkin’s mistake. Get lost before I change my mind.”

Baek Museong looked at him for a moment before bowing his head.

“Thank you for showing consideration.”

“Hmph. Lucky bastards.”

But the lucky one was Woo Hwangtae.

If Baek Museong hadn’t sent a Sound Transmission a moment earlier, he would have been hovering between life and death by now.

“Second, stop.”

The second of the Three Plum Blossom Elites, Chulwoo of the Defeated Flower Fist, stopped dead just as he was about to launch himself forward.

A voice that no one else could hear leaked between his teeth.

“He wasn’t satisfied with going after me—he even went after you, Senior Brother.”

“It doesn’t matter.”

“It matters to me. Can’t I hit him once? Just once?”

“That sounds like you want to beat him to death.”

“…I’ll hit him gently. Just once. Really.”

“That sounds like you want to gently beat him to death. Have you forgotten Master’s strict order not to attract unnecessary attention?”

After wrestling with himself, Chulwoo lowered the fist he had been gripping tightly.

“Whew. This is driving me crazy.”

Baek Museong patted him on the shoulder as if he were proud of him.

“You held back well. This too is training.”

“How is this training? I can’t even use the martial arts I worked so hard to learn when the time comes.”

“Mindless killing will only ruin you. Martial arts are meant to hone your essence, qi, and spirit, not to kill someone.”

“Every time I look at you, I get confused. Am I a disciple of Huashan or a Shaolin monk?”

“Could a monk possibly suit your personality? I only feel sorry for all the wooden fish you’ll break in the future.”

Baek Museong let out a quiet laugh, and Chulwoo sighed.

He deeply respected his Senior Brother, but the man was simply too kindhearted. That was the problem.

“Those bastards should have their mouths smashed in…”

“Hey, watch that mouth!”

“All right, all right.”

Chulwoo watched Woo Hwangtae’s back as he grew smaller in the distance and smacked his lips.

*I’ve memorized his face. Let him cross my path once.*

Baek Museong naturally knew what his Junior Brother was thinking. He shook his head from side to side.

“Stop thinking nonsense and find the youngest.”

“Did Eunhyang disappear again?”

“Yes, just like you.”

Chulwoo flinched.

“I went to take a leak.”

“That’s right. But why did someone who went to take a leak end up picking a fight in a crowded place?”

“I was on my way back after relieving myself. Seriously, Senior Brother, you don’t believe me? I haven’t washed my hands yet. Want to smell them?”

“…Never mind.”

Baek Museong rubbed his temple. He cherished his Junior Brothers more than anyone, but they were exceptionally difficult to handle.

At least Chulwoo was large enough to find quickly. The youngest Junior Disciple, Eunhyang, was practically invisible in a crowd like this.

“Do you see anything?”

Chulwoo, who was at least two heads taller than everyone else, swept his gaze around.

“Not really. There are too many people.”

Even the eyes of a Peak master would have difficulty finding a small girl in the endless, bustling crowd.

There were so many people that peddlers had even set up stalls all over the place.

“By the way, was the Jin Family of Taiyuan always this big? I’d never even heard of it before we came.”

“Those in the know do. The current Sect Leader, the Shanxi Extraordinary Hero, is fairly well known, and so is the Heaven Shaking Sword, isn’t he?”

“I don’t know the Shanxi Extraordinary Hero, but the Heaven Shaking Sword… Is that the guy who’s supposedly one of the Ten Dragons and Phoenixes?”

“Don’t call him that. Watch your mouth.”

“He’s just a milquetoast scholar who attends an academy. In my opinion, Senior Brother is much more…”

“Hey. Where did you learn that bad habit of judging people before you’ve even seen them? He’s clearly a gifted talent.”

“Well, for someone from Shanxi Province, being that good is practically the same as a dragon rising from a ditch.”

Chulwoo answered indifferently, then suddenly frowned.

“Wasn’t there someone else besides the Heaven Shaking Sword? Some kind of dragon or loach?”

“A dragon? Do you mean the Sleeping Dragon of Shanxi?”

“Ah, right. The Sleeping Dragon of Shanxi.”

“I heard he’s a fairly impressive talent, though not as much as the Heaven Shaking Sword.”

“Whether he’s a dragon or a loach, I’ve heard about him nonstop on the way here. I should at least see his face once.”

Baek Museong’s lips curled slightly upward when he saw Chulwoo clench his fists.

“Do you want to spar with him?”

Chulwoo scratched the back of his head.

“Not necessarily. I’d win anyway.”

“Competitive pride is a good thing, but you should avoid causing trouble whenever possible.”

“Would there even be anything to cause trouble over? Since we came all this way, I just want to see what he’s made of.”

Baek Museong stared intently at his Second Junior Brother.

Despite his words, Chulwoo was obviously quite curious.

After spending years cooped up on Huashan and facing the same people every day, he seemed excited.

“You’ll see him soon enough. Of course, we have to find the youngest first.”

The words he added at the end sounded more like a sigh.

The gates of the Jin Family of Taiyuan were already open, and the invited guests were streaming inside like a gathering cloud.

Baek Museong was wondering if he would have to climb a tree when—

“Senior Brother, it’s all right to be a little noisy, isn’t it?”

“What?”

Chulwoo grinned and drew in a deep breath.

The next moment, a thunderous shout burst forth.

“Eun—hyang!”

There was no time to stop him. Chulwoo’s voice was as tremendous as his body.

The people around them covered their ears and dropped to the ground, while the countless people who had been laughing and chatting abruptly fell silent.

Just as everyone stood in silence as if cold water had been thrown over them—

“Big Brothers! I’m over here!”

Far away, Chulwoo spotted a young girl jumping up and down enthusiastically in place. He spoke triumphantly.

“Ha-ha! Senior Brother, I found her!”

“…Yes, good job. Very good.”

Baek Museong put a hand to his head.

That was when hundreds of people began murmuring and parted like reeds splitting in the wind.

At the end of the opened path stood a man as tall as an iron tower. Chulwoo unconsciously muttered,

“Is that a man or a bear?”

“He’s a man. If not for him, the Jin Family of Taiyuan wouldn’t be what it is today.”

Baek Museong respectfully performed a cupped-fist salute toward the bear-like man, Jin Wikyung.

* * *

Thud-thud-thud-thud!

The scenery whipped past us. Hyuk Mujin, riding right beside me, shouted over the pounding hooves.

“It was definitely slow when we were going there, but it’s incredibly fast on the way back. Is it because we took it easy two days ago?”

“Everything has a reason.”

“What reason?”

“It gets faster when no one tries to eat something while riding a horse.”

“Ah.”

Cheongpung had worn a gloomy expression the entire time. Before we left, I had stopped him from packing a huge amount of food.

“I’m hungry.”

I answered coldly.

“Endure it.”

A Peak master’s digestive power was Peak-level too. Cheongpung crapped as much as he ate, then ate as much as he crapped.

On top of that, he ate often, so he had no choice but to crap often…

Damn it. This is too disgusting. I’ll stop there.

“How far have we come?”

“We just passed the ninth village, so… We should arrive in half a shichen at the earliest, or a full shichen at the latest.”

The sunlight pouring down made my eyes sting. I looked up at the sun, which was slowly climbing toward the middle of the sky.

“We’ll arrive around noon, then?”

“Probably.”

“We’re late, aren’t we?”

“Of course we’re late. Isn’t that why we’re riding like hell, trying to be a little less late?”

He was right.

Instead of answering, I dug my heels into the horse. Every time it ran, the long bundle strapped across my back thumped against its body.

*Ugh, what a pain.*

The bundle held the Unnamed Sword.

It was something I had originally been supposed to return to Jeok Cheongang, but I had ended up taking it back again.

As long as I lived in a Murim where the law was damn far away and fists were painfully close, I had no choice.

*I can’t put it in my inventory either.*

I could at least claim that I had tucked the Flame Divine Palm martial arts manual inside my clothes. But if a sword suddenly came flying out of my pocket, there would be no way to explain it.

If I were alone, it might be different. But with other people watching, it was the perfect situation to be accused of practicing demonic, heterodox arts.

*This really turned into a nasty bind.*

It wasn’t that I was complaining about being saddled with a troublesome object. I simply hated the thought of having to meet Fire King Jeok Cheongang—that terrifying old man—again.

*I’ll see you again soon.*

*Who wants to see him again?*

Every time I remembered the words I’d heard a few shichen ago, my stomach churned.

Hyuk Mujin, who had been sneaking glances at me from time to time, asked,

“Why do you look like that?”

“I was thinking about the Fire King.”

“Ugh. We don’t have enough time for happy thoughts, so why are you imagining something so horrible?”

“If you were me, wouldn’t you think about him? He said he’d come again soon.”

“Speaking of which, could you give me a vacation? I suddenly miss my family.”

“This bastard is trying to save his own skin.”

“You never know what might happen. Before I die, I should at least see my parents’ faces one more time.”

“That doesn’t sound like something an unfilial son who hasn’t shown his face in years should be saying.”

“I want to become a good son while I have the chance.”

“No. You can’t.”

I completely ignored Hyuk Mujin’s bullshit and looked up at the sky with a sigh.

“What an unfeeling heaven. Why did that old man have to give me this thing?”

“He said it was a pain to carry around.”

“For such a petty reason?”

“With him, I can completely believe it.”

“…”

That was actually pretty convincing.

“I could lose it in the meantime. Or I could quietly swipe it.”

“You, Captain?”

Hyuk Mujin laughed as if he had just heard a brilliant joke.

“What have you done all this time? If you hadn’t been in mortal danger, you would have just kept the Blazing Flame Divine Pill too, wouldn’t you?”

“That’s…”

He had a point.

“Just hide it somewhere no one will notice. Who knows? Maybe that great Fire King will teach you a move in return.”

“Teach me, my ass. As if he’d do that for someone who killed his Disciple.”

I let out a quiet laugh at the absurdity of it.

The Fire Gate Clan was said to be a sect whose arts were passed down to a single successor and never taught to outsiders. Setting personal feelings aside, the idea that he would teach martial arts to an outsider like me was ridiculous.

“Your nonsense is only funny when you keep it in moderation, you idiot.”

“Well, now that you mention it, that’s true.”

At that moment, Cheongpung, who had been hanging limp like a corpse and repeating that he was hungry, spoke up.

“Isn’t he trying to take you as his Disciple, Benefactor?”

“…”

“…”

“Maybe not? I think he is. Grandpa Jeok seemed to be watching you closely, Benefactor.”

“Me?” I asked.

“Captain?” Hyuk Mujin asked.

Our gazes collided in midair. He looked utterly baffled. I was probably wearing much the same expression.

We both let out a quiet laugh.

“That’s great. Congratulations in advance, Captain.”

“Yeah. Thanks.”

*Me? Someone he’d known for barely a day or two?*

It was such an absurd idea that it did not even qualify as a joke.

“Or not? Is that right?”

As Cheongpung tilted his head after saying something so bizarre, Hyuk Mujin raised a finger and pointed into the distance.

“Can you see it?”

I could.

People were walking along a well-kept road. Farther ahead was a broad expanse of land surrounded by a crowd.

*The Jin Family of Taiyuan.*

It was my return after three days away.
## Chapter artifact 182

# Chapter 182

Step. Step.

Under the eyes of countless people, two men walked toward each other. When they finally came face-to-face, they performed a cupped-fist salute.

“I am Jin Wikyung of the Jin Family of Taiyuan.”

“I’m Baek Museong of Huashan.”

Huashan.

And Baek Museong.

The impact carried by those two words was enormous.

Exclamations erupted from every direction, instantly sweeping away the silence.

“Huashan!”

“Baek Museong—the Huashan’s Lone Crane, Baek Museong!”

Though ordinary people were mixed in among them, a considerable number of those gathered here today were martial artists.

The weight carried by the Huashan name and the epithet Huashan’s Lone Crane was immense.

“My heavens, why did Huashan’s Lone Crane come here?”

“Was the Jin Family of Taiyuan really this influential?”

“W-Wait. If Huashan’s Lone Crane came here, then…”

The people who had been talking over one another began scanning their surroundings. Before long, they spotted the man and woman beside Baek Museong, and another round of exclamations escaped them.

“That young man must be the Defeated Flower Fist. He’s enormous, just as I heard.”

“The Flower Sword Phoenix is here too! She’s even beautiful!”

“Whoa! It’s the Three Plum Blossom Elites!”

Chulwoo and Eunhyang wore bewildered expressions at the unexpectedly intense attention.

Both of them had accompanied their Master, the Heavenly Sword True Person, into the martial world a few times, but this was the first time they had ever received such a cheer.

“What the hell? Am I really this famous? They even know my epithet?”

“Senior Brother Chul, did you hear that? Someone just called me beautiful.”

Chulwoo answered with a stern expression.

“You heard wrong, so don’t pay it any mind.”

“…You’re seriously annoying.”

The two had grown up studying under the same Master since childhood, and had been raised like biological siblings. Seeing them snarl at each other with their eyes, Jin Wikyung smiled faintly.

“You two seem close.”

“They’re still immature and constantly causing trouble. They have a long way to go.”

“Ha-ha. The Defeated Flower Fist and the Flower Sword Phoenix are both outstanding young prodigies. Surely that can’t be true.”

“You flatter us.”

A faint smile also appeared at the corners of Baek Museong’s mouth as he answered. Though this was their first meeting, he liked Jin Wikyung.

Perhaps it was because of the man’s distinctive air that put people at ease. Or perhaps it was his familiar bulk, which reminded Baek Museong of Chulwoo.

“Let us go inside. This is hardly an appropriate place for an important conversation.”

“I agree.”

They had already drawn attention unintentionally.

If even a single word about the Sword Saint came up while so many eyes were watching them, an uproar was sure to follow.

“Well, then.”

Jin Wikyung gave a light nod and began walking ahead.

Baek Museong followed him through the pouring gazes and cheers, but then stopped short.

He could no longer sense his junior disciples behind him.

*What is it?*

Baek Museong glanced back and saw Chulwoo standing tall like an iron tower. He was staring intently at something.

“Second.”

At Baek Museong’s call, Chulwoo slowly turned his head.

“Yes, Senior Brother.”

“Is something wrong?”

“No. Nothing.”

Eunhyang, who was standing beside Chulwoo, abruptly cut in.

“That’s not true. Senior Brother Chul was staring at someone just now.”

“Do you know that person?”

Chulwoo immediately shook his head. His thick body subtly blocked Eunhyang from view.

“As if. Other than going out a couple of times with our Master, I’ve been cooped up at headquarters the whole time.”

“That is… true.”

“I was just looking for a privy because my stomach suddenly started hurting.”

“Really?”

“Yes. Which is why I was wondering if I could stop by the privy before we go.”

“How long has it been since you last took a piss?”

Chulwoo deliberately hardened his expression.

“If you take care of the big business first, you can take care of the small business at the same time. But you can’t take care of the big business while taking care of the small business.”

“…Uh, sure.”

Baek Museong felt uneasy.

Perhaps it was because his Second Junior Brother, who usually rambled on with statements that made no sense, had given such a smooth answer.

“Second, are you thinking about something else—”

He could not finish.

Jin Wikyung had stopped walking and was looking back at them with a puzzled expression.

“Young Hero Baek, is something the matter?”

“Oh, no. My junior disciple said he had an urgent matter.”

“What sort of matter?”

“Well… bodily functions.”

“Oh.”

The people who had been listening closely to their conversation let out quiet snickers. Chulwoo scratched the back of his head awkwardly.

“I apologize.”

“Not at all. You must be exhausted from traveling all the way to our family. Please get some proper rest.”

Baek Museong pondered for a moment, then nodded. The important conversation was between him and Jin Wikyung anyway. There was no point leaving his junior disciples beside him to yawn loudly. It would be better to let them rest.

“Since Great Hero Jin has given you permission, go ahead.”

“Big Bro—no, Senior Brother. Can I go too?”

“Yes. Do you dislike it?”

“Yes. I just want to stay beside Senior Brother.”

Eunhyang nodded vigorously, and Jin Wikyung smiled.

“Then that settles it. Young Hero Baek?”

“Ah, yes. Let us go.”

Baek Museong continued walking with an unconvinced expression. But before long, he shook off his doubts.

*Surely nothing could have happened during that brief moment?*

* * *

As Chulwoo watched the group recede into the distance, a martial artist from the Jin Family of Taiyuan approached him.

“I’ll guide you to the privy.”

“What do we need a privy for?”

“Pardon me?”

“It’s all mountains around here. I can just take a dump by the side of the road. Don’t you agree?”

The people surrounding them burst into loud laughter.

There was a common prejudice that members of the Nine Sects and One Gang would be arrogant and rude. But Chulwoo’s refreshing banter made everyone feel as if a weight had been lifted from their chests.

“Of course. That’s right.”

“Though this is the frontier, the mountain scenery around here is beautiful. Go take care of your business while enjoying the view!”

“Hey, Defeated Flower Fist! Since we’ve met by fate, would you like me to recommend a scenic spot?”

Chulwoo threw back his head and roared with laughter.

“Ha-ha-ha! A scenic spot? Sounds good. But I don’t want to go to the place where you took a dump. Let’s see…”

Chulwoo casually swept his gaze over the crowd, then raised a finger and pointed at one man.

“How about that Brother over there guides me?”

The middle-aged man who had been staring at Chulwoo with a blank expression since earlier jolted in surprise.

“M-Me?”

“That’s right. You.”

The middle-aged man was Woo Hwangtae, and his complexion turned the color of shit.

* * *

“Slow down a little. Let’s take it easy from here.”

“Why?”

“Can’t you see the horse is foaming at the mouth? And if we arrive panting and out of breath, everyone will look at us and think, *Ah, that bastard was late.*”

“That actually makes a strange amount of sense.”

We gradually eased up on the reins. The view of the Jin Family of Taiyuan was beginning to appear below us as we descended the hill.

“By the way, there are a lot of people gathered.”

“Seriously. From what I heard, they weren’t supposed to invite anywhere near that many.”

Even a rough count put the crowd camped out before the main gate of the Jin Family of Taiyuan well over several hundred.

Though we were still quite far away, we could even hear faint cheers.

*Did an idol come?*

I circulated my internal energy and focused it on my ears. My hearing, now several times sharper than usual, picked up every bit of the people’s cheering.

Hyuk Mujin, who had been quietly watching me, asked,

“What’s going on? Did they say an important guest arrived?”

“Huashan’s Last Crane and the Plum Blossom Cutoff, apparently.”

“…Those are epithets?”

“Don’t ask me. That’s what I heard.”

The distance was considerable, so there was a limit to how much I could make out.

But still. What kind of epithets were those? Did the Plum Blossom Cutoff have some grudge against Huashan?

At that moment, Cheongpung, who had been lying facedown across his horse’s neck, opened his mouth.

“Benefactor. They said Huashan’s Lone Crane and the Three Plum Blossom Elites.”

“Oh, really?”

“Yes. I heard it clearly.”

He could hear that from this distance?

Cheongpung was the most powerful martial artist among us, so it was probably true.

“I see.”

Unlike me, who merely nodded without much interest, Hyuk Mujin was so shocked that he fell off his horse.

“H-Huashan’s Lone Crane! The Three Plum Blossom Elites!”

“Are they famous?”

“Famous? That’s putting it mildly! They’re the direct disciples of the Heavenly Sword True Person, the Sect Leader of Huashan!”

“Is it the kind of thing where you’re an idiot if you don’t know them?”

“No martial artist could not know them!”

“Oh, really?”

I casually pointed over my shoulder. Cheongpung had his eyes wide open and was clapping.

“Wow, those are cool epithets. But where did they say they were from?”

“…”

“…”

“Shaolin Temple, maybe?”

Was he insane?

These were the words of the youngest Junior Brother of Huashan’s Sect Leader, no less.

After remaining silent for a long while, Hyuk Mujin finally spoke.

“Huashan’s Lone Crane, the Three Plum Blossom Elites. You really haven’t heard of them?”

“I like Huashan! I like plum blossoms even more!”

“…Right.”

Style was temporary, but class was forever.

*It wasn’t even “I like Dad, but I like Mom more.” What the hell was this?*

Was Huashan stored in his head as Dad and plum blossoms as Mom?

While I was contemplating the structure of Cheongpung’s brain, Hyuk Mujin finally came to a conclusion.

“Anyway, they’re insanely famous.”

“I see.”

“I see.”

“…Is that really the end of your reaction?”

“What reaction were you expecting?”

“Normally, people react like I did.”

“Are you supposed to be shocked enough to fall off your horse?”

Hyuk Mujin climbed back into his saddle and launched into an impassioned speech.

“I’m telling you, that’s how shocked you’re supposed to be. The Heavenly Sword True Person’s disciples! The future of Huashan!”

“I see. They’re no joke.”

I turned toward Cheongpung.

“May I ask your grandfather’s full name?”

“His surname is Mae, and his given name uses the characters Jong and Hak. Mae Jonghak.”

“And his epithet?”

“The Sword Saint.”

“Did you hear that, Mujin?”

“Yes.”

Hyuk Mujin nodded with a blank expression, then came to his senses. His eagerness to make us understand how extraordinary Huashan’s Lone Crane and the Three Plum Blossom Elites were was almost palpable.

“Great Hero Mae Jonghak, the Sword Saint, doesn’t count. Honestly, that would be like an adult joining a children’s fight.”

“So what’s your conclusion?”

“Huashan’s Lone Crane is already a master who has surpassed the level of a young prodigy. At this rate, becoming the next Sect Leader won’t be a problem. The other two members of the Three Plum Blossom Elites are also objects of admiration among young martial artists.”

They really were impressive. From the way he talked about young prodigies, they still seemed to be quite young, yet the public considered them at least world-class.

“Then why am I not particularly impressed?”

“That… I’m not sure.”

Hyuk Mujin thought about it carefully, then his expression suddenly went flat.

“Now that I think about it, I’m not exactly bursting with excitement either.”

“Really?”

“Yes. Huashan’s Lone Crane used to be my idol.”

Cheongpung abruptly cut in.

“Isn’t it because of Grandpa Jeok?”

“Huh?”

“Eh?”

“He’s incredibly strong. And he’s trying to take you as his Disciple.”

The latter part was complete bullshit, but the first part was right.

If the Sword Saint, Mae Jonghak, was something above the clouds that I could not even properly picture in my mind, the Fire King, Jeok Cheongang, was a monster that had revealed itself in the flesh.

After experiencing a monster larger than a hundred-story building, it was only natural that a monster the size of a four-story commercial building would make less of an impression.

“And…”

Cheongpung looked straight at me and continued slowly.

“You’re plenty strong, Benefactor.”

“…What?”

“I mean it.”

Something tickled in one corner of my chest, but that statement was also undeniably true.

It was not confidence that I could go up against Huashan’s Lone Crane right now without falling behind.

*It was the certainty that I could catch up to him before long.*

It had taken only a few months to go from a Third Rate martial artist who did not even know martial arts to a Peak master.

I could not even begin to imagine how much I would grow in another year or two.

To me, Huashan’s Lone Crane was a milestone along the road—not an impassable wall.

“Thanks for saying that.”

Cheongpung answered with a sunny smile.

“You’re welcome. Grandpa said weak martial artists without firm resolve need constant attention.”

“…”

Fuck me. It had just been a pep talk.

It was at that moment, while I was caught in an inner struggle over whether to split open the crown of Cheongpung’s head, that—

“H-Hey, Young Hero Chul!”

“Hah, listen to this old coot calling me Young Hero Chul. Didn’t you call me a cow’s head earlier?”

“N-No, Great Hero Chul! I committed a grave discourtesy, *so*!”

“Committed-*so*? *-so*? Cow? You just called me a cow again, didn’t you?”[^1]

[^1]: The formal Korean sentence ending *-so* is pronounced the same as the Korean word for “cow.”

“Eeeeeek! Isn’t that taking it too far? Do you even know how old I am?”

“Yes, Elder. Let’s go up there and have a little talk.”

A young man with a massive build reminiscent of Jin Wikyung, and a middle-aged man being dragged along by him, were just about to enter the mountainside beside the hill.

The young man saw us and stopped.

“Brother over there, do you need something?”

*He means me, right?*
## Chapter artifact 183

# Chapter 183

A hulking man reminiscent of a Minotaur glared at me with eyes as big as saucers.

“Brother over there, do you need something?”

He was telling me to pretend I hadn’t seen anything and move along.

It was no different from the lines spoken by third-rate thugs in movies, but according to what I’d sensed with Qi Sense, that hulking man was neither a third-rate thug nor an inept wandering martial artist.

> **System**
>
> **Level:** 95 — **Chulwoo**

*He’s as skilled as he looks.*

In Murim terms, he was a Peak master. In modern terms, he was at least an A-rank Hunter.

If a guy like that were a thug, the police—the people’s cane—wouldn’t stand a chance. Even the people’s sledgehammer wouldn’t be enough.

*Where did this guy come from?*

For a moment, the epithets I’d heard just now—Huashan’s Lone Crane and the Three Plum Blossom Elites—flashed through my mind, but that was as far as it went.

No matter how I looked at him, he seemed more like a knife-wielder from Majang-dong or a twin-axe fighter from Seocho-dong than a crane or a plum blossom. Those sorts of nicknames seemed much more appropriate.

When I merely stared at him without answering, the hulking man, Chulwoo, frowned.

“Didn’t you hear me? Are you deaf? Or mute?”

Before I could say anything, Hyuk Mujin jumped in.

“Have you ever seen such an outrageous bastard? How dare you speak so rudely to our Young Master?”

“Is pretending not to hear someone a polite thing to do?”

“Ahem!”

“What are you ahem-ing about? How important do you think you are that you don’t answer when someone speaks to you?”

“You insolent bastard! Do you need a beating to come to your senses?”

I stopped Hyuk Mujin as he reached for his sword scabbard.

“That’s enough.”

“Please don’t stop me. Someone like this needs to be taught a harsh lesson!”

“He’s stronger than you.”

“Ah. I don’t think this is my place to step in.”

“…”

“…”

Chulwoo opened his mouth with an incredulous expression.

“Is he your subordinate?”

“For now.”

“You must have a hard time.”

“Every day is a battle with my patience.”

After looking our group up and down, Chulwoo clicked his tongue.

“You look like martial artists, so it would be best if you just went on your way. This man made a very serious mistake with me.”

Chulwoo grabbed the collar of *this man* and lifted him up. He was so strong that the heavyset middle-aged man shot straight into the air.

“Eeeek! H-Help me!”

Above the terrified middle-aged man’s head floated the Level window I had detected earlier with Qi Sense.

> **System**
>
> **Level:** 60 — **Woo Hwangtae**

That was a name that made me crave hangover soup.

It also sounded vaguely familiar.

*Woo Hwangtae, Woo Hwangtae… Where have I heard that before?*

While I was thinking, Chulwoo grabbed Woo Hwangtae by the collar and shook him violently.

“What do you mean, help you? Don’t drag innocent people into this. Just take a few hits and get it over with.”

“G-Great Hero, please don’t do this. Let’s resolve it through conversation. Conversation.”

“Conversation?”

“Y-Yes! Conversation!”

“Conversation sounds good. Then let’s have a private conversation somewhere without any people around.”

He clearly meant to have a physical conversation.

Woo Hwangtae, who was being dragged along against his will, shouted like he was screaming for his life.

“I-I was invited here by the Jin Family of Taiyuan! I’m supposed to have a private audience with the Lesser Family Head!”

“I was invited too. And I’m a simple, crude man by nature, so I don’t particularly care whether you’re meeting the Lesser Family Head or the Family Head.”

“Eeeeeek!”

This wouldn’t do. Someone was going to die before I remembered his name.

I had no desire to get dragged into an unnecessary dispute, but there was something that bothered me about simply walking past.

*From what I’ve heard, he seems to be a fairly important guest.*

The fact that he was supposed to have a private audience with Jin Wikyung bothered me. So did Chulwoo’s casual disparagement of the Jin Family of Taiyuan.

I smacked my lips and stepped forward.

“Excuse me.”

“All that fat and you still have to make people’s lives difficult… Did you call me?”

“Yes.”

“What do you want?”

“It’s nothing important.”

I continued, addressing Chulwoo, who had paused.

“It’s a good day. Wouldn’t it be better to work things out through conversation?”

“Give it a rest?”

“I’m sorry for sticking my nose in where it doesn’t belong, but wouldn’t it look bad for the Jin Family of Taiyuan if guests started fighting on a day like this?”

“Hey, Young Hero.”

Chulwoo rubbed his neck with an annoyed expression. At the same time, his speech, which had previously been close to polite, was cut in half.

“This is personal. If you stick your nose in, you’ll only make yourself tired.”

“I’m already tired. What can you do?”

“Your speech is getting short?”

“Yep. Same goes for you.”

“How old are you?”

“Twenty.”

“Twenty? Huh. Fresh as a daisy. Fresh as a daisy.”

“How old are you?”

“I’m twenty-five, you young bastard.”

Good grief. I was surprised twice.

Once by the boomer attitude of a twenty-five-year-old, and again by the fact that his face belonged to a man in his mid-twenties.

Even if he had been fed protein supplements instead of breast milk as a baby, he shouldn’t have ended up like this. I asked with considerable astonishment,

“Twenty-five? Are you Benjamin? You’re living your life backward.”

Benjamin Chulwoo glared at me.

“What the fuck are you talking about?”

“It’s not bullshit. It’s a fact. It must have been tough looking prematurely old.”

“Prematurely old? Shut up! Everyone around me thinks I look incredibly young!”

“Everyone around you? Number one, your mother. Number two, your father. Number three, your grandmother. Pick one of the three. Oh, let’s make number four your youngest maternal aunt.”

“This beardless little brat…”

“Pull down your pants. I want to see whether you’ve got hair on your dick.”

“You little—!”

“Woof, woof-woof! Woof-woof-woof!”

Chulwoo released his grip on Woo Hwangtae’s collar. Trembling as he looked from the ground to the sky, he took several deep breaths.

“You… Hoo. Hoooo.”

“Are you angry, Benjamin?”

“Shut that damn mouth!”

He seemed to have completely lost his temper.

*I didn’t mean to take it this far.*

I had simply answered him one insult at a time, and somehow this was where we had ended up.

Chulwoo, snorting like a frenzied Minotaur, finally managed to open his mouth. It took him a great deal of effort. A very great deal.

“Y-You bastard, what the hell are you?”

“What kind of bastard do you think I am?”

“A bastard who’s gone mad wanting to die.”

Crack.

The sound of bones grinding came from the fist as large as a shovel handle.

Chulwoo ground his teeth and glared at me.

“Do you even know what it means to interfere in someone else’s personal gratitude and grudges in Murim?”

“I already apologized for sticking my nose in where it didn’t belong. But if guests start throwing punches, what does that make the people who invited them? You ought to think about our family’s position too.”

“Our family?”

“Yeah. Our family.”

“Are you perhaps a member of the Jin Family of Taiyuan?”

“I don’t think I’m a freeloader.”

“Make one more wordplay joke and I’ll put you in bed for three years.”

“Watch your mouth—unless you want your family mourning you for three years.”

Chulwoo smiled thinly. It wasn’t a smile born of amusement. It was the kind of smile that appeared on its own when someone’s anger had reached the top of his head.

“My Senior Brother warned me over and over… but I can’t let you off. Time for you to take a few hits.”

Boom!

Before he could finish speaking, an enormous roar rang out, and the ground shattered.

The two-meter-tall giant launched himself like a cannonball. The time it took him to reach the tip of my nose was no more than an instant.

“It’s going to hurt.”

Whoosh!

With a chilling voice, the air scattered.

No—it was crushed.

It was nothing more than a simple punch, with no form or martial principle added to it. The force contained in that fist exploded with enough momentum to shatter a thousand-jin boulder.

But…

*As long as it doesn’t hit me.*

Bang! B-bang!

I bent backward as if lying down. The fist struck the air a handspan above me, and compressed air exploded from its tip. A tree more than ten feet away flew through the air as if caught in a typhoon.

*Wow. This guy was serious.*

I was left speechless by the overwhelming power.

If an ordinary First Rate master had taken that blow, it would not have ended with mere pain. Once Chulwoo lost his temper, he seemed unable to see anything else.

“Hey, hey. Take it easy. Take it easy.”

“You rat-like bastard!”

Whoosh! Whoooosh!

One punch, two punches, three. Each time I easily avoided another punch, my suspicion hardened into certainty.

*I think I can win.*

Even a thousand-jin boulder had to be hit before it could be shattered.

No matter how powerful an attack was, it was useless if it failed to connect.

Moreover, Chulwoo was only at the early Peak realm and could not even project fist qi. If our martial insight was comparable, I had an overwhelming advantage.

Because I possessed a special power no one else had.

*Stats.*

Whoooosh! Bang!

After yet another wild swing, Chulwoo exploded in frustration.

“What the hell!”

“You’re too excited. Take a deep breath and relax your body. That way, you might be able to touch even a single hair.”

Meanwhile, I had completely regained my composure. Hyuk Mujin and Cheongpung were watching from the sidelines as if none of this concerned them, while Woo Hwangtae stared at our exchange with his mouth hanging open.

Given the situation, Chulwoo also seemed considerably flustered.

“What the hell are you?”

“A member of the Jin Family of Taiyuan.”

“There’s no way someone like you could be in this backwater… Wait.”

Chulwoo stared intently at me, then suddenly narrowed his eyes.

“Are you the Heaven Shaking Sword?”

“I am somewhat related to that man. As far as I know, we came from the same womb.”

“Then… are you the Sleeping Dragon of Shanxi?”

I grinned.

“Bingo.”

He might not have known what *bingo* meant, but he understood its positive connotation and clenched his fist.

“I knew you had some skill.”

“Try hitting me at least once before saying that. You said it would hurt, but this just feels refreshing.”

“I’ll admit it. You may not be a dragon, but you could at least qualify as an imugi.[^1]”

“Good grief, that’s a harsh assessment.”

“Your mouth has reached the realm of transcendence.”

“It’s all psychological warfare. Take a look at yourself. You’re showing nothing but the whites of your eyes while throwing punches at thin air.”

“Don’t get confused. I simply had no desire to use my sect’s martial arts against an unknown nobody like you.”

“Which sect is that? The Dodong Sect?”

“You don’t need to know.”

He spat out a wad of phlegm and muttered,

“Damn it, the Sleeping Dragon of Shanxi. What a letdown.”

Same for me.

He was obviously a disciple of a fairly well-known sect, but if we fought until one of us fell, both of us would have to deal with the backlash.

“I’m holding back because of my eldest brother.”

“I’ll let you off because of my Senior Brother.”

We spoke at nearly the same time and glared at each other.

“Oh? Look at this bastard.”

“Bastard? You little brat, how dare you speak to an adult that way!”

“Adult, my ass. Do you even know how old I am, calling yourself an adult?”

“What else is someone who’s barely twenty supposed to be but a child?”

“That’s not what I meant…!”

If I added my age in the Murim to my age in the modern world, I was practically fifty. But there was no chance of getting that across to him.

I swallowed the words that were about to burst out.

“Forget it. What’s the point of talking to a guy like you? Anyway, in Murim, the strong are the adults.”

“What? Are you saying I’m weaker than you?”

“Obviously. Didn’t you feel the difference between us just now?”

“You son of a bitch! I could chew you up and still not feel satisfied!”

“Try hitting me, if you can.”

“You think I can’t?”

It was at that moment, as Chulwoo raised his fist with a heavy snort, that someone’s voice abruptly cut in.

“It would be best if you both stopped now.”

Wipeng alighted with an ethereal movement technique and swept over us with a chilly gaze.

His eyes passed over Cheongpung, Hyuk Mujin, and Woo Hwangtae, whose appearance had become a complete mess from being dragged around, before finally pinning me and Chulwoo like arrows.

“Defeated Flower Fist, and Third Young Master.”

“No, Great Hero Wipeng. It’s not like that. The circumstances…”

“That’s right. I was merely…”

A voice colder than the northern wind and bitter snow froze the words in their throats.

“Are you both determined to bring utter shame upon your respective schools?”

Chulwoo and I quietly shut our mouths.

* * *

“How long has Defeated Flower Fist been gone?”

“Dunno. Feels like it’s been more than half an hour.”

“Why isn’t he back?”

“Maybe he got stuck.”

“A Daoist from Huashan?”

“Why would that matter? If he’s a Daoist from Huashan, does that mean his shit should come out smoothly too?”

“I suppose you’re right.”

Just as the theory that Chulwoo was constipated was all but confirmed, the people who spotted a group of people and horses coming down the hill burst into cheers.

There was a face among them that no martial artist in Shanxi Province could possibly fail to recognize.

“It’s the Sleeping Dragon of Shanxi!”

“The Sleeping Dragon of Shanxi! He’s coming with the Defeated Flower Fist!”

“Wooaaah!”

The appearance of two young and outstanding men sent the crowd into a frenzy.

The two young prodigies whom everyone believed would become future leaders of Murim walked side by side, waving their hands.

Every time they did, cheers erupted from all directions, along with hands reaching out to touch even their clothing.

“The Sleeping Dragon of Shanxi!”

“The Defeated Flower Fist!”

“Well now, they look pretty close. Were they acquainted?”

“Does that matter? Real talent recognizes real talent. There’s nothing strange about them forming a deep friendship in such a short time.”

“Now that you mention it, that makes sense. They look great together.”

While everyone looked on with warm smiles, the broadly grinning Jin Taekyung and Chulwoo exchanged words in very low voices.

“I let you off earlier. You know that, right? You couldn’t even touch me.”

“Bullshit. I didn’t use even half my strength.”

“I didn’t use even a third.”

“I misspoke. I didn’t use even one-tenth.”

“My mistake too. Truth is, I didn’t use even one percent.”

“Now that I think about it, same here.”

“Is this guy completely insane?”

“Who are you to say that?”

Amid the tremendous cheers, a fierce exchange took place—one that only Peak masters could hear.

[^1]: An *imugi* is a legendary serpent said to have the potential to become a dragon.
## Chapter artifact 184

# Chapter 184

It looked like there were a thousand people, not hundreds. With the martial artists of the Jin Family of Taiyuan escorting us, we made our way through the enormous crowd.

*This feels amazing.*

I felt like a star in the Chinese-speaking world. The Korean Wave and all that.

Then again, I was actually Korean, so it wasn’t entirely wrong.

“Sleeping Dragon of Shanxi! Look this way just once!”

“Eeeek! Young Hero Jin!”

“Waaah!”

They say even a mutt has home-field advantage.

No matter how famous the Three Plum Blossom Elites were, they couldn’t beat the pride of Shanxi Province—the son of Taiyuan—on his home turf.

As I smiled warmly and waved, Chulwoo whispered to me.

“Look at the corners of your mouth. Enjoying this?”

“Look at the corners of yours. Are you crying?”

“You Shanxi bumpkin.”

“Yeah, next mountain man.”

“You little—”

“What, you—”

Just as sparks were about to fly again, a thread of Sound Transmission pierced my ear.

—Third Young Master!

Wipeng was glaring at me with a fierce expression. He looked like he wanted to slap me right then and there.

He must have sent a similar Sound Transmission to Chulwoo, because the man added a single word with a dissatisfied expression.

“I let you off.”

I answered with a derisive snort.

When I first realized from the people’s cheers that Chulwoo was a fairly prominent young prodigy of Huashan, I was rather surprised.

But that was all.

*So what if he’s one of the Three Plum Blossom Elites?*

I had already experienced enough of Huashan’s martial arts, thanks to a certain person plodding along beside me.

“I’m hungry. I’m hungry.”

“……”

Cheongpung was a strange fellow no matter how many times I saw him, but there was no denying that he was a Peak master who had mastered Huashan’s foundational secret arts.

Because of that, I was confident I could respond no matter what martial arts Chulwoo used. The only thing Chulwoo had over me was his background as a member of Huashan.

“……”

Ah, no. I take that back.

The difference in our backgrounds was pretty serious when I thought about it. No matter how much the Jin Family of Taiyuan had risen in status, the Nine Sects and One Gang were overwhelmingly powerful.

*Fuck. I lose.*

The Nine Sects and One Gang and the Five Great Families, as I saw them, were no different from a corporate alliance in Murim.

Powerful conglomerates had joined forces into one coalition and were ganging up on everyone else. There was no one who could stand against them.

Fortunately, they didn’t invade the alley markets despite calling themselves the orthodox faction, which was why small and medium-sized companies like the Jin Family of Taiyuan could still climb their way upward.

*In that sense, it’s obvious that Huashan is paying close attention to this matter.*

Huashan’s Lone Crane, Baek Museong.

If everything Hyuk Mujin had told me was true, Baek Museong was practically the next Sect Leader of Huashan—recognized as such by everyone, including himself.

There was one person among Huashan’s young prodigies who could be considered his only equal, though…

“Benefactor, I’m really hungry. Do you have any dumplings left?”

“No. I don’t.”

“Oh. Aaaah…”

Cheongpung was a lost cause.

It would probably be faster for Huashan’s Daoists to convert to Islam than for that guy to become the Sect Leader of Huashan.

Even I, an outsider, couldn’t help thinking, *What kind of person is this?* How much worse must it be for the people of Huashan?

*Once he’s experienced everything in the world, he’ll probably decide that he wants to try being the Sect Leader of Huashan too. Yeah.*

Just as I was imagining a fairly believable future, Chulwoo opened his mouth with an irritated expression.

“Hey, did a ghost of someone who died because he couldn’t eat dumplings latch onto you? Please shut your mouth and walk.”

“……?”

“……?”

“……?”

Chulwoo flinched when the gazes of Wipeng, Hyuk Mujin, and me all fell on him at once.

“W-What? Why are you looking at me like that all of a sudden?”

“Hey, you don’t happen to…”

“Young Hero Chul, you don’t know?”

“Come on, no way. You’re one of the Three Plum Blossom Elites. Surely you can’t not know.”

As the reactions came one after another, Chulwoo’s ox-like eyes rolled around.

“What? Why is everyone acting like this?”

Why else? Because he couldn’t recognize the elder of his own sect.

By seniority, Cheongpung was the Disciple of the Sword Saint and the youngest Junior Brother of the Heavenly Sword True Person, the current Sect Leader of Huashan.

To Chulwoo, that made him his Master’s Junior Brother—in other words, his Martial Uncle.

*Come to think of it, he might not know.*

Cheongpung had been raised by the Sword Saint, Mae Jonghak, while Mae Jonghak was living in seclusion. There was no doubt that only a handful of people within the sect knew what he looked like or who he really was.

I clicked my tongue as I looked at Chulwoo, who stood face-to-face with his Martial Uncle without recognizing him.

“Tsk, tsk. They say it’s darkest beneath the lamp.”

“What the hell does that mean?”

“Never mind. You’ll find out soon enough.”

“Damn it, this is driving me crazy.”

As Chulwoo pounded his chest in frustration, we left the cheers of the crowd behind and entered through the main gate of the Jin Family of Taiyuan.

At the same time, more than a hundred pairs of eyes and countless whispers flew toward us from every direction. The atmosphere was completely different from outside the gate.

“That young man…”

“That’s the Sleeping Dragon of Shanxi. He’s as handsome as I’d heard.”

“The Defeated Flower Fist is here too. Isn’t he the second Disciple of the Heavenly Sword True Person?”

“Then who are the two young men beside them?”

“I couldn’t tell you.”

More than a hundred people of all ages, both men and women, were mingling together. Their wealth and leisure were evident in their clothes and manner.

*The power players of Shanxi Province.*

Some of them were Sect Leaders, while others were wealthy merchants. They had enough influence and ability to be formally invited to this gathering.

*At a glance, it almost looks like a ball for aristocrats.*

I walked on, swept up in a strange feeling.

The fact that these people, who could be considered Shanxi Province’s ruling class, were no more than supporting characters at this gathering—and the curious, admiring gazes they sent my way—made one corner of my heart itch.

And then it happened.

“My name is Jang Se-pal. I lead a small sect called the Hequ Sect.”

“Ah, yes. Hello.”

“I’ve long admired the reputation of the Jin Family of Taiyuan and the Sleeping Dragon of Shanxi from the bottom of my heart, and…”

A middle-aged martial artist began an elaborate speech about how honored he was to meet me. Then people started surging toward us like a horde of zombies.

“Greetings. I run a small martial arts academy near Yangcheon…”

“Pardon me? Oh, yes.”

“Young Hero Jin, I have something important to discuss with you. Perhaps we could move somewhere else…”

“Right now? I’d rather not.”

“This is my daughter. She wanted to meet the Sleeping Dragon of Shanxi at least once, so I brought her along. If you happen to find her appealing…”

“Yes, yes.”

“Oh! Then shall I send a matchmaker right away?”

“Wait, wait! I answered that wrong!”

What on earth was going on?

Requests for handshakes—or rather, a barrage of fist-and-palm salutes—were pouring in from every direction. I was on the verge of losing my mind.

If Wipeng hadn’t stepped forward at just the right moment, I would have ended up accepting every request and marriage proposal wrapped in flowery language.

“Everyone, restrain yourselves!”

The shout of a Peak master infused with internal energy made the people flinch, and we took the opportunity to escape. Chulwoo clicked his tongue as though he’d had enough.

“That was excessive. Are all the people of Shanxi like that?”

Of course not. This situation was a bit unusual.

Wipeng was the only member of our group who hadn’t been flustered. He opened his mouth with a calm expression.

“You’ll experience this often from now on, so you’ll have to get used to it.”

“I’m supposed to experience things like this often?”

“You’re a direct descendant of the Jin Family of Taiyuan, after all.”

“I almost got married five times just now.”

“That’s only natural for a promising young prodigy without a partner.”

“I heard someone say they were betrothed to me before I was even born… Is that true?”

“What difference does it make whether it’s true or false? Think positively.”

The hair on my body stood on end.

I had spent twenty-seven years of my life as a lifelong single in the modern world, and now I was suddenly worried that I might be forced into an arranged marriage.

In Murim, thousands of miles from home, no less.

*No. I have Song-i.*

Veins bulging in my neck, I shouted,

“Marriage is an incredibly important matter! You can’t just brush it aside like that! Love between a man and a woman! Pure feelings! Don’t I get any of that?”

“No. You don’t.”

“Why?! How come?!”

Wipeng looked me up and down as though he were looking at an insect.

“Is that something a man who’s been going in and out of pleasure houses since he was sixteen should say? Did you throw away your conscience along with your silver nyang?”

“……”

“Let’s walk quietly. Our Lord is waiting.”

If I’d actually been to one, at least I wouldn’t feel so wronged.

Fuck, I’d never even been to a pickup bar, let alone a pleasure house.

As I said nothing and shed silent tears of blood inside, Chulwoo sidled up and asked,

“Is that true?”

“What is?”

“That you’ve been going to pleasure houses since you were sixteen.”

“You don’t need to know. Why are you suddenly asking about that?”

Chulwoo flinched and began to ramble.

“Well, how should I put it? I suppose you could call it personal curiosity. About a man who has walked only the straight path of a martial artist…”

“You want to visit a pleasure house?”

“Ahem!”

“Finish walking the path of a martial artist. Don’t go wandering down side paths for no reason.”

I replied with utter disdain. That was when a voice cut in.

“Young Hero Jin is absolutely right. How long has it been since you left the main sect, and you’ve already forgotten the duty of a martial artist?”

The tone was stern, yet carried a hint of amusement.

The owner of the unfamiliar voice was a clean-cut man. He approached with an unwavering stride and respectfully made a fist-and-palm salute.

But he wasn’t addressing me or Wipeng.

“Baek Museong, First-generation Disciple of Huashan, pays his respects to his Martial Uncle.”

Cheongpung was silent for a moment before answering.

“Who are you?”

* * *

Around sixty, perhaps?

He was an old man with a slender frame and strikingly narrow eyes.

A deeply hoarse voice came through his chapped lips.

“So you were humiliated by an unknown nobody with no name?”

“E-Elder, that’s not what happened…”

The three men standing before the old man were sweating profusely.

They were known as the Three Hands of Zhongnan, but before an elder of their sect, they had to watch every word they spoke and every movement they made.

Even more so when that elder was the Roaring Fury Swordsman—a master counted among the top five in the Zhongnan Sect and a man famous for his fiery temper.

“Then what is it? No matter how I listen, it sounds to these old ears as though you idiots smeared shit all over the name of the great Zhongnan Sect.”

The Three Hands of Zhongnan trembled beneath the old man’s sharp gaze.

Just as the Roaring Fury Swordsman was about to unleash his thunderous reprimand, one of the men, who had kept his mouth tightly shut the entire time, suddenly spoke.

“He wasn’t an unknown nobody.”

“What?”

The man with a splint on his arm, Gong Ilhyuk, continued.

“He said he was the Sword Saint’s Disciple.”

The statement was so shocking that the Roaring Fury Swordsman momentarily forgot how to speak. Then he asked with an expression of disbelief,

“…The Sword Saint?”

“Yes.”

“The Sword Saint, who has been living in seclusion for so long, raised a Disciple?”

“We suspected it at first, but… it seems to be true.”

“Your evidence?”

“Li Feng, a lay Disciple of Huashan, serves in the military of Shanxi Province. Judging by his reaction, it seems certain.”

“Li Feng?”

The old man’s already furrowed brow creased further.

His memory wasn’t good enough to remember some lay Disciple of Huashan.

“Is that all?”

At the lukewarm reaction, Gong Ilhyuk hurriedly spoke again.

“He mastered Huashan’s foundational secret arts to the Peak realm despite being only twenty. He used martial arts that are permitted only to the direct Disciples of the main sect, one after another…”

After hearing the entire account of what had happened, the Roaring Fury Swordsman silently rubbed his sword scabbard.

*The Sword Saint’s Disciple. The Sword Saint’s Disciple.*

The Sword Saint had already been living in seclusion for decades.

No one even knew whether he was alive or dead, and now his Disciple had suddenly appeared in Murim?

It was difficult to believe, but his mind had already begun to lean toward accepting it.

*At the very least, I should verify it.*

After remaining silent for a long while, the Roaring Fury Swordsman abruptly rose from his seat. An order fell on the startled Three Hands of Zhongnan.

“Guide me.”

“W-Where do you mean?”

“Could you mean the Sword Saint’s Disciple…?”

While the other two men stood there flustered, Gong Ilhyuk’s eyes flashed.

“As far as I know, that bastard is traveling with a scion of the Jin Family of Taiyuan.”

“If you mean a scion of the Jin Family of Taiyuan, are you talking about that Jin Taekyung fellow you mentioned earlier?”

“Yes. He’s half a day from here.”

The Roaring Fury Swordsman clicked his tongue.

“Cunning bastard. That must be why you came looking for this old man.”

“The name of the great Zhongnan Sect has fallen into the dirt because of these inept Disciples. Elder, aren’t you the person who cares about our sect more than anyone? I happened to hear that you were in the area on business, so…”

“Cut it out. From what you’ve told me, this Jin Taekyung fellow sounds like an incredibly arrogant bastard too.”

“That’s right. A bastard like that needs to be taught a harsh lesson.”

Gong Ilhyuk added, as though he had just remembered something,

“I hear the Jin Family of Taiyuan is holding a gathering.”

“A gathering?”

“They’ve invited every sect in Shanxi Province to show off their power.”

“They’re trampling on our sect and holding a gathering?”

Anger filled the Roaring Fury Swordsman’s eyes.

“I’ve heard enough. Lead the way.”

“I obey, Elder.”

A smug smile spread across Gong Ilhyuk’s lips.

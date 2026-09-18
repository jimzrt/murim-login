# Checkpoint Review — 315–319

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

# Chapters 315–319

## Plot

After his defeat by Jin Taekyung, Hyuk Sopyung is ordered back to Zhongnan by the Taeeul Sword Unit because his feared Senior Martial Uncle, Hwangbo Eom—the Taeeul Merciless Sword—has come to Xi’an. Taekyung successfully guides qi into the unconscious Jeok Cheongang, slightly improving Jeok’s condition and strengthening his own Scorching Yang Qi. The experience raises the Fire Gate Divine Technique to seven stars and causes Taekyung to level up.

Gung Gibang learns that the Yongbong Escort Bureau’s decline began with the generosity and later qi deviation of its former Bureau Head, Ju Hogun. The Xi’an Beggars’ Sect also uncovers indications that Zhongnan may have engineered the bureau’s downfall to absorb its position. The bureau reaches Xi’an after losing thirty-three escorts while protecting the Thousand-Year Snow Ginseng, but surveillance of the suspicious Escort Captain Song lapses.

At Tengwang Pavilion, Hwangbo Eom reprimands Hyuk Sopyung and declares that he is trying to restore Zhongnan’s standing. Ju Hwaran presents the sealed shipment, supposedly prepared by the Pill Physician, Family Head of the Shandong Seongsu Jang Family. When Hwangbo opens it, the casket contains Hundred-Year-Old Snow Ginseng instead of the contracted Thousand-Year Snow Ginseng. He refuses compromise and demands two hundred thousand silver nyang, threatening to destroy the Yongbong Escort Bureau financially. Song Ilseom shows almost no reaction. Taekyung’s party then enters Tengwang Pavilion, and Hwangbo recognizes Taekyung while sensing overwhelming qi from the group.

## Continuity

- Jeok Cheongang remains unconscious and is being transported beneath fur on Taekyung’s pack frame. Taekyung’s True Qi Guidance can affect Jeok because both share Fire Gate Clan lineage; Jeok’s condition has improved slightly but remains critical.
- Taekyung’s Fire Gate Divine Technique is now seven stars, and his Scorching Yang Qi increased slightly after guiding qi into Jeok.
- Taekyung’s party at Tengwang Pavilion consists of Taekyung, Cheongpung, Gung Gibang, Hyuk Mujin, Baek Museong, and unconscious Jeok Cheongang.
- Hwangbo Eom, the Taeeul Merciless Sword, is a Supreme Peak master of Zhongnan and Hyuk Sopyung’s Senior Martial Uncle. He is working to restore Zhongnan’s declining reputation.
- Ju Hwaran is the Young Bureau Head of the Yongbong Escort Bureau. The bureau has lost thirty-three escorts and may collapse under Hwangbo’s demand for two hundred thousand silver nyang.
- The casket bears the seal of the Shandong Seongsu Jang Family. Its current Family Head, the Pill Physician, supposedly placed and signed the Thousand-Year Snow Ginseng inside.
- The shipment currently contains Hundred-Year-Old Snow Ginseng. The substitution’s timing, method, and culprit remain unknown.
- Song Ilseom was present when the substitution was revealed and displayed almost no reaction. His connection to the discrepancy remains unresolved.
- Ju Hwaran suspects Zhongnan leaked information about the ginseng and arranged circumstances that endangered the escort mission. Whether Zhongnan or another party caused the attacks and substitution remains unresolved.
- The Xi’an Beggars’ Sect believes Zhongnan may have worked to absorb the Yongbong Escort Bureau’s position in Shaanxi. Huashan’s awareness of this remains uncertain.
- Hwangbo Eom has recognized Taekyung and sensed power from the approaching party comparable to an Elder of the Nine Sects and One Gang.

## Translation Decisions

- Use **Taeeul Sword Unit** for 태을검대 and **Taeeul Merciless Sword** for 태을무정검.
- Use **Hwangbo Eom**, **Tengwang Pavilion**, **The First Sword of Zhongnan**, and **Huashan–Zhongnan gathering**.
- Use **Escort Captain Song** for 송 표두 and **Chief Escort** for 총표두.
- Use **Pill Physician** for 환의 and **Shandong Seongsu Jang Family** for 성수장가.
- Retain **Thousand-Year Snow Ginseng** and **Hundred-Year-Old Snow Ginseng**.
- Preserve the **Turtle Breath Technique/Ghost Technique** wordplay and use **Cardiopulmonary Resuscitation Fist** for 심폐소생권.

## Durable state

{
  "active_continuity": [
    "Hwangbo Eom, the Taeeul Merciless Sword, is at Tengwang Pavilion and has rejected compromise after Ju Hwaran's shipment proved to be Hundred-Year-Old Snow Ginseng.",
    "Hwangbo Eom demands two hundred thousand silver nyang as compensation from the Yongbong Escort Bureau.",
    "Ju Hwaran and Heo Jun face the possible financial destruction of the Yongbong Escort Bureau.",
    "The shipment bears the seal of the Shandong Seongsu Jang Family and was said to have been prepared and signed by its current Family Head, the Pill Physician.",
    "Song Ilseom is present at Tengwang Pavilion and behaved suspiciously when the shipment discrepancy was revealed.",
    "Jin Taekyung's party has entered Tengwang Pavilion with Baek Museong, Cheongpung, Hyuk Mujin, and unconscious Jeok Cheongang.",
    "Hwangbo Eom has recognized Jin Taekyung and sensed overwhelming qi from his approaching party."
  ],
  "continuity_sources": [
    319
  ],
  "open_questions": [
    "Who changed the shipment from Thousand-Year Snow Ginseng to Hundred-Year-Old Snow Ginseng, and when did the substitution occur?",
    "Did the Zhongnan Sect leak information about the Thousand-Year Snow Ginseng or arrange the escort mission's attacks?",
    "Is Song Ilseom connected to the shipment discrepancy?"
  ],
  "safe_through": 319,
  "temporary_decisions": [
    "Use Tengwang Pavilion for 등왕루.",
    "Use The First Sword of Zhongnan for 종남제일검.",
    "Use Chief Escort for 총표두.",
    "Use Young Hero Cheong for 청 소협.",
    "Use Pill Physician for 환의 and Seongsu Jang Family for 성수장가."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 315

# Chapter 315

Step. Step.

The Zhongnan One Dragon, Hyuk Sopyung, walked neither quickly nor slowly.

Every time he took a step, people’s eyes and whispers followed him.

“Tut-tut. Causing such a commotion in broad daylight…”

“To think someone known as his sect’s greatest young prodigy would turn out like that. You can tell what kind of level the Zhongnan Sect is at. No wonder Huashan is always considered the best in Shaanxi.”

“Why is his cheek so swollen? I heard Huashan’s Lone Crane came here. Could it be…?”

Hyuk Sopyung unconsciously rubbed his cheek.

The throbbing pain wasn’t caused only by the stinging gazes of the people around him. The three slaps he had taken helplessly—and one man’s low voice—came vividly back to him.

*I believe I already said this. Think carefully before you swing that sword.*

The Fire King’s chosen successor, a Hidden Dragon who had risen from the small stream that was Shanxi Province.

Hyuk Sopyung had already heard enough about that bastard to last him a lifetime.

But…

*How can he be that strong?*

He couldn’t understand it at all. He had become the direct Disciple of the Zhongnan Sect’s Sect Leader and learned martial arts with the full support of the sect.

Countless Peak martial arts, elixirs, and the name of one of the Ten Dragons and Phoenixes were all things Hyuk Sopyung had taken for granted.

But now, everything surrounding Hyuk Sopyung was beginning to shake precariously.

The cold expression of Xi’an Tower’s chief manager when he encountered him at the entrance was one sign of it.

“I heard you caused another disturbance.”

“A disturbance? There was a little commotion, that’s all. Nothing worth worrying about, so let’s forget it.”

Hyuk Sopyung was about to continue on when the chief manager’s next words made him stop dead.

“I believe I told you last time that if anything like this happened again, I would file a formal complaint with the Zhongnan Sect.”

“A complaint?”

Hyuk Sopyung glared at the chief manager with gleaming eyes before speaking.

“Our Manager Song has grown quite bold.”

“Young Hero Hyuk!”

“Don’t get cocky.”

A growl slipped between Hyuk Sopyung’s teeth.

“You seem to think your shoulders have gotten a lot broader just because you put the owner’s son into Huashan as a lay Disciple… Do you really think the Great Zhongnan Sect is so easy to laugh at?”

“Your words are too harsh.”

At the chief manager’s stiff expression, Hyuk Sopyung twisted his lips.

“You’re the ones going too far. You tavern keepers dare look down on our sect? You’ve got more nerve than sense.”

“May I convey those words to the owner exactly as you said them?”

“Don’t forget. Be sure to tell him. Then I’ll see you next time.”

Pat, pat.

Hyuk Sopyung patted the chief manager’s shoulder and walked away, a bitter smile on his lips.

*Now I’m being looked down on even by people like him.*

Of course, Xi’an Tower’s owner had considerable influence for someone who could be called a mere businessman. He was a major player who controlled the entertainment district of Xi’an, the capital of Shaanxi Province.

But no matter how powerful someone was in the business world, before the name of the Nine Sects and One Gang, he was nothing more than a firefly before the sun.

And to think Hyuk Sopyung had been subjected to such humiliation by the manager of a single pleasure house—not even its owner.

*Things really are going from bad to worse.*

In the span of only a year or two, the Zhongnan Sect’s standing had continued to decline.

The first arrow had been fired by the Fire King Jeok Cheongang when he crushed the Roaring Fury Swordsman in front of countless witnesses. Then came the Sword Saint Mae Jonghak breaking his seclusion and the emergence of the name Huashan Divine Dragon.

*How can two tigers live on the same mountain?*

Someone had to become the stronger one, and someone else had to become the weaker.

The Zhongnan Sect’s role was the latter.

*It won’t always be like this.*

Blood ran from the fist Hyuk Sopyung had clenched with all his strength.

The alcohol’s poison from the night before had long since been expelled. Hyuk Sopyung was staring up at the sky with a hardened expression when—

“Gasp, gasp. Senior Brother, there you are.”

“You’re… Bong-su?”

Hyuk Sopyung looked at the familiar face with surprise.

The young man was panting heavily. He was a Disciple of the Zhongnan Sect like Hyuk Sopyung. Though they had different Masters, they were of the same generation.

“What brings you here when you should be at headquarters?”

By headquarters, he meant Mount Zhongnan, a two-day journey from Xi’an. His Junior Brother, Bong-su, answered.

“I’m on a mission. The entire Taeeul Sword Unit came as well, not just me.”

“A mission? And the Taeeul Sword Unit?”

The Taeeul Sword Unit was a force made up of the Zhongnan Sect’s second-generation Disciples. Though they were no match for Huashan’s Plum Blossom Swordsmen, they were still an elite unit the Zhongnan Sect took pride in.

For the Taeeul Sword Unit to come all the way here when they rarely ever left headquarters…

Hyuk Sopyung frowned in puzzlement. His Junior Brother spoke.

“I was ordered to bring you back, Senior Brother.”

“Ordered? Who is looking for me?”

“Senior Martial Uncle is in Xi’an right now.”

“……!”

Hyuk Sopyung’s eyes widened. There were only two people his Junior Brother, who was of the same generation as him, could call Senior Martial Uncle.

One of them, the Roaring Fury Swordsman Song Il, had been confined to the main sect because of the internal injury he had suffered from the Fire King. That left only one person.

*But why is he in Xi’an…?*

Hyuk Sopyung hurriedly pushed the question from his mind.

If his Second Martial Uncle was looking for him, he couldn’t afford to delay even for a moment. That man frightened Hyuk Sopyung more than even his own Master, the Wind-and-Cloud Sword Lord.

No—not only Hyuk Sopyung. Every Disciple of the Zhongnan Sect felt the same way.

The anxious expression on his Junior Brother’s face was proof enough.

“Senior Brother, there’s no time.”

“Take me to Senior Martial Uncle at once.”

A short while later, Hyuk Sopyung shot forward at tremendous speed using his movement technique. One question continued to circle through his mind.

*What on earth is going on?*

One thing was certain.

If his Second Martial Uncle, the Taeeul Merciless Sword, had stepped in, this was no ordinary matter.

* * *

True Qi Guidance was a dangerous and difficult undertaking.

Even when circulating one’s qi alone, there was always the danger of qi deviation. Guiding someone else’s energy to circulate their qi was a task whose difficulty needed no explanation.

*Especially when the target is the Fire King.*

The tension was on an entirely different level from when I had performed True Qi Guidance on the Peace Guild members.

I began moving the Scorching Yang Qi with the sensation of stepping onto a sheet of thin ice.

*Slowly. Carefully.*

Those were the only two words I repeated over and over. Without allowing a single distracting thought, I drew in Jeok Cheongang’s enormous energy.

Whoooong.

The two energies met.

But there was none of the collision or resistance I had encountered with the Peace Guild members. They simply blended together naturally.

They assimilated and flowed together as though they had originally been one body—as naturally as reuniting with a twin separated long ago.

*Because they grew from the same root.*

That was right. Jeok Cheongang and I shared the same root: the Fire Gate Clan.

If someone who had never learned the Fire Gate Divine Technique had recklessly attempted True Qi Guidance, they might have been unable to withstand Jeok Cheongang’s immense internal energy and suffered qi deviation.

*Thank God.*

I had already done this several times, but it was always terrifying.

Feeling my heart clench with tension, I began the actual True Qi Guidance.

Following the formula of the Fire Gate Divine Technique, I circulated the Extreme Yang qi that had now become one without pause.

One shichen, or perhaps two.

I became so absorbed that I lost all sense of time. The True Qi Guidance, which had seemed as though it would never end, finally came to a close when all the internal energy returned to the dantian.

Chime.

> **System**
> - **True Qi Guidance** successfully completed!
> - The target’s condition has improved slightly!
> - Your **Scorching Yang Qi** has increased slightly!

“Phew…”

I closed my eyes and steadied my breathing.

It wasn’t over yet. For a brief moment, I had assimilated with and experienced the enormous energy possessed by the Supreme Peak master known as the Fire King Jeok Cheongang.

The root called the Fire Gate Clan. The trunk of the great tree that had grown from it, along with its countless branches. I had clearly witnessed a glimpse of a realm so distant it was almost impossible to imagine.

Insight came from experiences and circumstances like this.

Just like now.

*I finally have some idea of where to go.*

I could see it: the steps leading to a higher realm.

It was a small insight that no one could have taught me.

Chime.

> **System**
> - The realm of **Fire Gate Divine Technique** has risen to seven stars!
> - You can manipulate, release, and withdraw qi more freely!
> - You can now perform the martial arts of the **Fire Gate Clan** with greater power and effectiveness!
> - You have acquired a large amount of EXP and Bonus Points as a reward for your enlightenment!
> - Level Up!

Yes. This was it.

I opened my eyes to the cheerful chime. I had climbed only a single step, but the difference was immense.

Through my newly sharpened senses, information about everything around me came flooding in.

My entire body, drenched in sweat. The stench rising from the turbid qi I had expelled. And the presence of someone struggling silently behind my back.

“……”

What the fuck?

I turned my head and saw Cheongpung wrapped around Hyuk Mujin’s entire body like an anaconda. Both hands were firmly clamped over Mujin’s mouth and nose.

“What are you doing over there?”

Cheongpung answered brightly.

“Hyuk Mujin was about to snore, so I was stopping him!”

“Ah, well done. That bastard nearly gave me qi deviation from pissing me off.”

I told that idiot Hyuk Mujin to stand guard, and he was off dreaming the Butterfly Dream.[^1]

I looked at Hyuk Mujin, whose face had turned blue as he struggled, and asked a question that suddenly occurred to me.

“You only need to cover his nose. Why are you covering his mouth too?”

“When I covered his nose, sounds started coming out of his mouth!”

“Oh.”

“So I covered both!”

“Hmm. Then won’t he die of suffocation?”

“He can use the Turtle Breath Technique!”

“What exactly is this damn Turtle Breath Technique?”

“You hold your breath, stop your heartbeat, and lower your body temperature at the same time!”

“Sounds incredible. Is that even possible?”

“Of course. That’s what Hyuk Mujin is doing right now!”

“Mujin is?”

“Yes! His heartbeat has already stopped.”

“……?”

My mind went blank. I stared at Hyuk Mujin without saying a word.

While we were talking, the man who had stopped struggling lay there with his limbs hanging limp.

“Gasp, Mujin!”

“He’ll be cold soon!”

“Get your hands off him right now, you lunatic!”

“Oh? Maybe it isn’t the Turtle Breath Technique. Young Hero Hyuk? Can’t you hear me? Young Hero Hyuk?”

I didn’t know about the Turtle Breath Technique, but the Ghost Technique certainly seemed accurate.

I struck Hyuk Mujin in the chest with a palm strike just before he could achieve Great Completion in the Ghost Technique.

“Cardiopulmonary Resuscitation Fist!”

Thud!

Along with the dull impact, a harsh breath burst from Hyuk Mujin’s open mouth.

“Gahk!”

“Oh no, Mujin! My left pinky!”

“Cough, cough! Captain?”

“Are you all right? Can you breathe?”

“What?”

Hyuk Mujin looked around with a bewildered expression. Perhaps because he had been attacked in the middle of his sleep, he didn’t seem to understand what had happened.

“What suddenly happened? I was just on a cloud.”

“A cloud?”

This idiot had really almost died.

Just as I was letting out a sigh of relief, Hyuk Mujin continued.

“A man in white came and started saying strange things. Something about a little lamb having come, and so on.”

“What kind of lamb?”

“A little lamb. He tried to embrace me, but there were holes this big in both his palms. I was about to cut him down without mercy when I woke up.”

“……”

Why was that person there?

Just as I was at a loss for words, the door to the private room where we were staying at Xi’an Tower slid open, and a grimy face poked inside.

Gung Gibang looked over the dejected Cheongpung, Hyuk Mujin, who had just come back from the dead, and finally me, whose soul had left my body.

Then he muttered,

“What a kennel.”

Being treated like a dog by a beggar left a bad taste in my mouth.

After barely pulling myself together, I asked Gung Gibang,

“Were you out begging?”

Gung Gibang shouted with an offended expression.

“What are you talking about? I’m on my way back from the Xi’an branch of my sect!”

The previous night, I had decided to stay at Xi’an Tower for a day and recover from the fatigue of our journey. At the same time, I had asked Gung Gibang to gather information, so he must have stopped by the Xi’an branch for that reason.

Since beggars were scattered throughout the world, the Beggars’ Sect had branches everywhere.

In terms of sheer numbers, it was the greatest sect under heaven.

“So? Did you get any useful information? Something about the Divine Physician’s whereabouts, for example.”

“I did. Though it wasn’t about the Divine Physician.”

Gung Gibang thought for a moment before continuing.

“This information reeks to high heaven.”

“More than you?”

“……”

“Sorry. Tell me.”

Gung Gibang was deeply offended and didn’t open his mouth until he had received five silver nyang in alms.[^2]

[^1]: A reference to Zhuangzi’s famous dream of becoming a butterfly.

[^2]: A traditional silver currency unit.
## Chapter artifact 316

# Chapter 316

Gung Gibang carefully tucked the silver nyang into his clothes before opening his mouth.

“It’s information about the Yongbong Escort Bureau.”

“The Yongbong Escort Bureau? You mean the one we ran into on the way here?”

“That’s right. It’s been reduced to Shaanxi Province now, but in the past, it was one of the largest escort bureaus in the world.”

“The Yongbong Escort Bureau?”

I recalled what I had seen two days earlier.

Of course, it had been an impressive force for a mere escort bureau. Its Young Bureau Head, Ju Hwaran, was a remarkably skilled swordswoman worthy of the title Ten Dragons and Phoenixes, while an escort named Song Ilseom was at least one level above her.

*Even counting the old man who looked like he could have written the Donguibogam, that made three Peak masters.*[^1]

That was enough to put them on par with most mid-sized sects.

But compared to the past, when the Yongbong Escort Bureau had ranked among the top three in the world, what I had seen that day had been downright shabby.

“What the hell happened to leave it in that state?”

“It began immediately after the Escort King passed away.”

“The Escort King? The one I know?”

“There can’t be two Escort Kings under Heaven. The Great Hero Ju Gongsan, the Escort King you know, was the former Bureau Head of the Yongbong Escort Bureau.”

Escort King Ju Gongsan.

I didn’t know his name, but I had heard his sobriquet plenty of times. Perhaps I had accumulated enough experience in the Murim by now, because I had a fair amount of basic knowledge.

Besides, I had spent the past year practically attached at the hip to the Fire King Jeok Cheongang.

He was a living witness to history—and occasionally an old man who reminisced about the past.

*Come to think of it, that friend of mine, the Escort King, was quite something too.*

*He’s not your friend.*

*You were hit by the Flame Divine Palm not that long ago, weren’t you?*

*Please tell me more. I’ll listen with rapt attention.*

The anecdote Jeok Cheongang had told me about the Escort King that day had been quite moving.

*It was when the Great Faction War was reaching its peak. At the time, the Demonic Cult had seized eight provinces, including Gansu, Sichuan, and Yunnan, and was advancing into the Central Plains at the head of a hundred thousand demonic soldiers.*

*When does the Escort King show up?*

*You were hit by the Flame-Extinguishing Divine Fist not that long ago, weren’t you?*

*Please continue. I’m begging you.*

*In any case, the Escort King of that time was nothing more than a wandering escort. Of course, he was already known as a famed escort because of his remarkable skill and chivalrous spirit. But with the Demonic Cult sweeping across the world, would orthodox Murim practitioners have had the time to care about something like that?*

*That’s true. Strictly speaking, escorts are closer to the business world than the Murim.*

*The Demonic Cult needed money as well, so rather than oppressing escort bureaus and merchant groups, they chose to win them over. Given the circumstances, it wasn’t particularly strange that the Escort King of those days was in Guangdong, which was under the Demonic Cult’s control. Everything went smoothly until he met a woman who was about to give birth.*

*She was about to give birth?*

*The last seed of the Guangdong Chen Family was in the woman’s womb. The Guangdong Chen Family had already been wiped out for resisting the Demonic Cult more fiercely than anyone else.*

*They must have found out right away.*

*The Escort King only realized the truth after he encountered a Demonic Cult pursuit squad. If he refused to hand over the woman, he would have to make an enemy of the Demonic Cult.*

At the time, the Demonic Cult had already swallowed half the world after winning battle after battle, Jeok Cheongang had said.

To make matters worse, Guangdong Province was tens of thousands of li from orthodox territory. It was nothing less than the Demonic Cult’s lair.

*What do you think the Escort King did?*

*If he’d handed the woman over to the Demonic Cult, he wouldn’t have been the Escort King.*

*Correct. He rejected the Demonic Cult’s demand without a word of hesitation. There was only one reason: he had already been paid the escort fee.*

On a day when war had engulfed the world, the young escort began what might have been his final escort mission.

The woman of the Guangdong Chen Family had paid him with an old jade hairpin, which he tucked inside his clothes.

*I heard it took him two whole years.*

From Guangdong through Jiangxi and Hubei, all the way to Henan, where the Murim Alliance was located.

The young escort crossed half the continent while evading the pursuit squad. He climbed mountains, ran across fields, and swam through rivers.

No one knew how he had done it or how many crises he had overcome, but one thing was certain.

The young escort had completed an escort mission unlike anything in the history of the Murim.

When the escort’s footsteps finally reached Henan, the last seed of the Guangdong Chen Family was crying vigorously in the woman’s arms, and the escort Ju Gongsan had become the Escort King.

*The Martial God said he was truly worthy of being called a king. No one disagreed.*

Jeok Cheongang often brought up stories about the Escort King after that.

Even to Jeok Cheongang, who viewed the world with a crooked eye, the Escort King seemed to have been a fairly decent man.

*I heard he established an escort bureau in his hometown of Shaanxi after the Great Faction War ended… I don’t know what happened after that. Perhaps I should stop by sometime and share a few drinks with him.*

In the end, Jeok Cheongang’s wish was never to come true.

According to what I had just heard from Gung Gibang, the Escort King Ju Gongsan was already dead.

*The continent sure is small.*

So the Yongbong Escort Bureau we had happened to encounter two days ago was the legacy of that Escort King.

Gung Gibang spoke when he saw the interest in my eyes.

“Great Hero Ju Gongsan couldn’t hold out for long after the internal injuries he suffered during the Great Faction War, and passed away. It was a tragic thing.”

“Then who’s the current Bureau Head?”

“Great Hero Ju Hogun, the Junzi Sword. He’s the Escort King’s only child by blood and Young Lady Ju Hwaran’s father.”

“Junzi Sword? Somehow, the sobriquet alone gives me a pretty clear impression of him.”

“I’ve never met him myself, but… my Master once said he was a very good person.”

A single particle could change the feeling of someone’s words entirely.

Gung Gibang’s Master, the Beggars’ Sect Leader, hadn’t said that Ju Hogun was a good person.

He had said that, *as a person,* Ju Hogun was good.

*That reeks of a sucker.*

I had a feeling that the Junzi Sword’s personality had contributed significantly to the Yongbong Escort Bureau ending up in its current state.

Sure enough, Gung Gibang nodded as though he had read my expression.

“As you guessed. Great Hero Ju is sentimental and can’t stand by when he sees injustice, so he’s suffered tremendous losses in various ways since taking over the Yongbong Escort Bureau.”

“He was in the wrong line of work from the start.”

“My Master once said something. A chivalrous hero can’t become a merchant.”

He was right. You had to disregard profit to be called a chivalrous hero, while you had to pursue profit more fiercely than anyone else to become a successful merchant.

An escort bureau could be called the intersection of the Murim and the business world, but in the end, it was closer to the latter.

*One hundred points as a chivalrous hero. Zero points as a merchant.*

The reason the Escort King had managed to catch two rabbits at once and build the Yongbong Escort Bureau into one of the five biggest in the industry was his fame.

But that advantage must have vanished after the Escort King’s death. For Ju Hogun, who lacked the qualities of a merchant, it would have been impossible to make up the difference.

“Whenever a great famine struck, he would buy grain even after exhausting his own stores, paying extra for it if necessary, and give it all away. He would take in poor or parentless children, feed them, and give them a place to sleep…”

“At that point, isn’t he basically UNICEF?”

“Huh?”

“Nothing. Keep going.”

“In any case, more went out than came in, so the Yongbong Escort Bureau gradually began to decline. My Master also offered him advice several times because of his connection with the previous Bureau Head, but apparently, none of it got through. Great Hero Ju insisted that this was his policy.”

“Wow.”

He was certainly an admirable and respectable businessman. It was just a shame he wasn’t a capable one.

Gung Gibang continued while scratching his back vigorously.

“What could anyone do? Since a man like Great Hero Ju inherited the escort bureau, its size had no choice but to shrink drastically in just thirty years.”

“Thirty years? They say a rich family lasts for three generations no matter how badly it falls.”

“It would have lasted three generations easily. If Great Hero Ju hadn’t collapsed from qi deviation two years ago.”

“…What’s that supposed to mean? Is this some kind of Age of Tribulations for the Yongbong Escort Bureau?”

“Considering all the misfortunes the Yongbong Escort Bureau has suffered over the past two years, you could call it that.”

“Good grief. They must have been through a lot.”

For an instant, Ju Hwaran’s bold figure flashed through my mind.

Back then, I had thought only that she was smart and pretty. But as it turned out, she was a young head of household carrying a tremendous burden.

But then…

“What exactly is this stink you keep talking about?”

Gung Gibang had opened the conversation with such meaningful words that I had been listening closely. But the only foul smell around here was the reek coming off that bastard.

My fastball straight at his body made Cheongpung and Hyuk Mujin, who had been listening in silence, crane their necks forward.

“That’s right. I don’t smell anything. I want to smell the stink too!”

“Young Hero Gung, when was the last time you brushed your teeth?”

When the guy who had nearly killed someone and the guy who had nearly died asked in unison, Gung Gibang’s face twisted into a scowl.

“Oh, shut up with all that yapping.”

“Forget that. Tell us quickly. And open your mouth a little less. Seriously, when did you last brush your teeth?”

“Four months ago.”

What a filthy bastard.

At my stare, which regarded him like some kind of beast, Gung Gibang flinched and hurriedly spat out a name.

“Z-Zhongnan Sect.”

“Huh? Zhongnan Sect?”

“According to what our Xi’an branch uncovered, there are signs that the Zhongnan Sect was deeply involved in the downfall of the Yongbong Escort Bureau.”

“Good grief. Those bastards have their fingers in everything.”

This really was information that stank.

No wonder a foul smell had suddenly filled the air the moment I heard the words Zhongnan Sect.

For a moment, I wondered if it was because Gung Gibang had opened his mouth too wide. But considering the behavior of every Zhongnan Sect member I had encountered so far, this wasn’t a rumor. It was a fact.

“They’re trying to swallow the Yongbong Escort Bureau whole, right?”

“Swallow it whole? Is it tasty?”

“Young Hero Cheong, could you shut your mouth for a moment?”

“Yes, Benefactor!”

By now accustomed to every part of this situation, Gung Gibang answered as though nothing had happened.

“That is highly likely. The Zhongnan Sect does operate an escort bureau, but it can’t compare to the position the Yongbong Escort Bureau holds within Shaanxi. From Zhongnan’s perspective, the Yongbong Escort Bureau must be a thorn in its side, along with Huashan.”

“So they’ve been methodically bringing it down for the past two years?”

“Ju Hwaran is certainly a gifted young woman. But she’s far too inexperienced. Being as sentimental as her father is another weakness.”

So, she was a clever fool.

Then again, according to what I had heard, Ju Hwaran was only twenty-one.

It was hard enough to organize everything she had learned in her head. Adjusting to practical work while leading an escort bureau of that size must have been a difficult task.

*Especially if the Zhongnan Sect was pulling dirty tricks behind the scenes.*

No matter how far beneath Huashan the Zhongnan Sect might be, it was still one of the Nine Sects and One Gang.

The Yongbong Escort Bureau might have been able to withstand the pressure while the Escort King was alive, but it had no way of doing so now.

It would be nibbled away little by little until it finally collapsed.

“How widely known is this?”

“It’s top-secret information told to me by the head of the Xi’an branch.”

“Top secret, huh? Then Huashan doesn’t know either?”

“Who knows? They might know, or they might not. Even if they do know, they could pretend not to and let it pass.”

“Pretend not to know? What’s that supposed to mean?”

Gung Gibang hesitated for a moment before answering with a sigh.

“Because they’re both part of the Nine Sects and One Gang.”

“…What?”

“Huashan’s Lone Crane, Baek Museong, is an upright and fair man. The Sword Saint Mae Jonghak is clear as a stream, and so is the Young Hero Cheong standing here. But remember that judging everything by a single facet is foolish.”

It was a single sentence that saw straight through my thoughts.

I was leaving today anyway. I had been planning to discreetly tip Baek Museong off about this information.

He was someone I knew to be a good man. And he had enough standing to be called the future of Huashan.

But I had been wrong.

*The future is only the future. It isn’t the present.*

Once again, I realized that the Murim was more complicated than I had thought.

Even the world of ignorant, simple-looking swordsmen had rules—and a league of its own.

*I guess even an arm bends inward.*[^2]

When I remained silent, Gung Gibang cautiously watched me and asked,

“What are you planning to do?”

“What do you mean, what am I going to do?”

“Are you thinking of stepping in yourself?”

“Me?”

I considered it for a moment, but soon shook my head.

My encounter with the Yongbong Escort Bureau had been nothing more than a chance meeting. I had things I needed to do.

“If I run into them before I leave, I can give them a heads-up. But that’s it.”

Now that Jeok Cheongang had collapsed, getting entangled with the Zhongnan Sect would complicate matters.

For some reason, Ju Hwaran’s face suddenly came to mind. I shook my head and let it pass.

[^1]: *Donguibogam* is a famous Korean medical text compiled in the seventeenth century.

[^2]: A Korean idiom meaning that people naturally favor their own side.
## Chapter artifact 317

# Chapter 317

“Ah.”

Sunlight broke across her long, fluttering eyelashes. Even after waking, Ju Hwaran remained lying on the bed, staring at the ceiling for a long while.

The night before, she and the Yongbong Escort Bureau had finally reached Xi’an.

The Black Stone Stronghold, led by Heavenly Axe, had been the final obstacle on this escort mission.

They had passed through Xi’an’s safe, bustling streets and unloaded their baggage at a secluded inn. Beds, warm food, and hot bathwater had all been waiting for them.

After checking every single item in the shipment, Ju Hwaran had collapsed into sleep.

*At last, the end is in sight.*

This place was safe. There were no bandits blocking the mountain roads, nor wandering martial artists hiding their identities and attacking in groups. Once they delivered the Thousand-Year Snow Ginseng, the primary objective of this escort mission, to the Zhongnan Sect, it would be over.

The Yongbong Escort Bureau would receive a reward worthy of its efforts, and they would all return home together.

Together with thirty-three bone urns.

*Thirty-three…*

Ju Hwaran’s eyes suddenly flickered faintly.

Thirty-three bone urns. Thirty-three faces. Memories of laughing and crying with them flashed before her eyes.

“Ah, I shouldn’t be doing this…”

Ju Hwaran rubbed at the corners of her eyes with her sleeve, then slapped both cheeks hard. The sharp crack brought her scattered thoughts back, if only a little.

“It’s only just beginning. I have to keep my head straight.”

The escort mission was not over yet.

Three days remained until the deadline agreed upon with the Zhongnan Sect, and the mission would not be complete until the Thousand-Year Snow Ginseng was safely delivered within that time.

“And then… it’ll be a new beginning.”

Muttering softly, Ju Hwaran reached inside her robes. She pulled out the tightly sealed wooden casket and checked it before putting it away again and securing it with a cord.

Even that alone allowed a refreshing fragrance to linger at the tip of her nose before vanishing.

Inside the casket was the Thousand-Year Snow Ginseng, an age-old elixir coveted by every martial artist in the Murim.

“Don’t lose focus, Ju Hwaran. This is only the first step.”

That was when someone spoke from outside the door.

“Hwaran, are you awake?”

The familiar voice reached her from beyond the door. After straightening her clothes, Ju Hwaran answered.

“Yes, Uncle Heo. You may come in.”

“Then excuse me for a moment.”

A short while later, Chief Escort Heo Jun opened the door and entered, his face bright.

“We’ll be able to return to the Escort Bureau earlier than expected.”

“You mean…”

“The Zhongnan Sect is waiting in Xi’an.”

“The Zhongnan Sect?”

“That’s right. And I hear the Taeeul Merciless Sword himself has come. Hahaha.”

Unlike Heo Jun, who was smiling, Ju Hwaran’s gaze sank deeply.

*The Zhongnan Sect? And the Taeeul Merciless Sword came all the way to Xi’an himself?*

Their return had been moved forward, so she should have been happy, just like Heo Jun.

But the more she thought about the arrogant and discourteous attitude the Zhongnan Sect had shown them until now, the more unease slowly crept up from the depths of her heart.

“Uncle Heo, don’t you think something is strange?”

“Hm? What do you mean, strange?”

“There are still three days until the agreed-upon deadline.”

“There are only three days left. Even traveling slowly, two days is enough to get from Xi’an to Mount Zhongnan.”

“You used to say this all the time, Uncle. There are no coincidences in the Murim. It’s a place where nothing is too strange, no matter what happens.”

“Hwaran, what are you trying to say?”

Under Heo Jun’s utterly baffled gaze, Ju Hwaran spoke gravely.

“The Zhongnan Sect has been quietly hostile toward our Yongbong Escort Bureau until now. More than anyone, they must have wanted this escort mission to fail. That’s why they deliberately set such difficult conditions.”

“But we accepted them. And we’ve handled them admirably.”

The conditions demanded by the Zhongnan Sect had been extremely difficult. The other heads of escort bureaus who had flocked there, lured by the Zhongnan Sect’s reputation, had even shaken their heads emphatically and abandoned the commission.

If they failed to transport the Thousand-Year Snow Ginseng within the required time, the mission would be deemed a failure, and they would have to pay an astronomical sum in damages.

But after much deliberation, Ju Hwaran had accepted the Zhongnan Sect’s commission.

There had been only one reason: to raise the Yongbong Escort Bureau to greater heights.

*And we had to pay a terrible price for it.*

Something that should never have happened had happened.

The cause had been the leak of information about the Thousand-Year Snow Ginseng.

Ju Hwaran was not a fool. She simply lacked experience. She possessed a sharp mind capable of considering every possibility and keeping all options open.

The suspicions she had kept buried in her heart until now were slowly taking shape. Ju Hwaran spoke quietly.

“Perhaps, perhaps the Zhongnan Sect…”

“Enough.”

Heo Jun’s face had hardened as he cut her off.

“Stop. I know what you’re thinking, but anything beyond that is absurd. No—it’s dangerous.”

“But—”

“I know the rumors about the Zhongnan Sect well. It’s also true that they’ve been keeping us in check so they can build up their own escort bureau. But what you’re trying to say right now, Hwaran… is a dangerous conjecture.”

“Uncle Heo…”

“As your uncle and as the Chief Escort of the Yongbong Escort Bureau, I’m asking you. Don’t put yourself or the Escort Bureau in danger.”

Though they shared not a drop of blood, he was her uncle in every way that mattered, a man who had always treated her warmly since childhood.

When he deliberately poured out those words with such a stern expression, Ju Hwaran could no longer continue speaking about the Zhongnan Sect.

“Phew.”

As Ju Hwaran let out a quiet sigh, Heo Jun gently placed an arm around her shoulders.

“I’m sorry if I was too harsh.”

“No. I suppose I was being overly sensitive.”

“You had reason to be. The Zhongnan Sect did something it had never done before. Who would have expected them to send the Taeeul Merciless Sword instead of a Hall Master or Chief Steward?”

One of the two Senior Brothers of Zhongnan’s Sect Leader.

The Taeeul Merciless Sword usually remained at the main sect, rarely showing himself in public. There was one simple reason people had remembered him for so long.

*The First Sword of Zhongnan.*

He was a Supreme Peak master produced by the Zhongnan Sect. The owner of a terrifying sword art said to have mastered the ultimate principles of the Heavenly River Thirty-Six Swords was none other than the Taeeul Merciless Sword.

There had to be great significance in a figure comparable to the Sect Leader, the Wind-and-Cloud Sword Lord, personally stepping forward.

That was what Ju Hwaran found most puzzling.

“Why the Taeeul Merciless Sword, of all people?”

“He must be in a hurry. The reason Zhongnan spent a fortune acquiring the Thousand-Year Snow Ginseng was the Roaring Fury Swordsman’s Internal Injury, after all. His only Senior Brother ended up like that. How could he not be frantic?”

At first glance, it sounded reasonable.

But Ju Hwaran clearly remembered what her father, Ju Hogun, had told her years ago.

*He called him a frightening man.*

Her father had been such a kind person that people called him the Junzi Sword. If even Ju Hogun, who was generous in his judgment of others, had described him that way, then the Taeeul Merciless Sword must have been as sharp a person as his swordsmanship.

*We must not let our guard down until the very end.*

After organizing her thoughts, Ju Hwaran asked Heo Jun a question.

There was still one person weighing on her mind.

“What about Escort Captain Song?”

“Ah, about that…”

Heo Jun hesitated briefly before answering.

“I had trustworthy escorts watching him discreetly day and night, but as you know, Hwaran, everyone let their guard down last night…”

“You took your eyes off him.”

“I have no excuse. It was my fault for failing to keep a closer watch.”

At Heo Jun’s embarrassed attempt to avoid her gaze, Ju Hwaran let out a small sigh.

“Haa…”

Song Ilseom, whose origins were unclear and whose reputation among the public was poor, had been one of their primary subjects of surveillance.

Her suspicions of him had grown particularly strong after he met Jin Taekyung.

*I told you repeatedly to keep a close eye on him.*

Heo Jun was certainly a good man. He had served the Yongbong Escort Bureau for more than thirty years and had been close enough to Ju Hogun to address him like a brother.

But the careless side he occasionally showed, like now, had also caused one mistake after another, both large and small.

*All I can do is hope it doesn’t happen this time.*

The milk had already been spilled. In any case, the Thousand-Year Snow Ginseng was in her possession.

Hiding her disappointment, Ju Hwaran spoke.

“Where did the Zhongnan Sect say they wanted to meet?”

“They asked us to meet at a teahouse called Tengwang Pavilion on the western edge of Xi’an by noon.”

Tengwang Pavilion was a famous teahouse that Ju Hwaran had occasionally visited herself.

There would be plenty of witnesses, and the atmosphere was quiet, making it the perfect place to conclude an escort mission.

“We’ll leave in fifteen minutes. Please prepare.”

* * *

Baek Museong came to Xi’an Tower while we were in the middle of packing.

“Are you really leaving right away?”

“I’d like to stay a few more days too, but as you know, our schedule is a little tight.”

“That’s unfortunate. If possible, I would have liked to escort you to the main sect.”

“I’ll stop by on the way back. Give me a tour of Huashan then.”

“Haha, don’t worry. I’ll take responsibility for showing you everything properly.”

There it was again. The full-course promise.

I wasn’t even expecting a full course. I just hoped that the next time we met, he wouldn’t be in the middle of another bloody fight like this one.

Then, as I stared at Baek Museong’s hearty, laughing face, a thought suddenly occurred to me.

*Should I at least bring it up? The Yongbong Escort Bureau and the Zhongnan Sect.*

I was still debating when Baek Museong touched his face and asked,

“Why are you looking at me like that? Is there something on my face?”

“…”

“Young Hero Jin?”

“Oh, no. I just got distracted by something for a moment.”

*Shit. I don’t know.*

When you got right down to it, the Zhongnan Sect and the Yongbong Escort Bureau were both complete strangers to me. Whatever dispute they had was something they needed to resolve among themselves.

I already had more than enough problems of my own. Worrying about something like this would just be meddling where I wasn’t wanted.

*This is the Murim, after all.*

I muttered inwardly as I seated Jeok Cheongang on the pack frame. Then I picked up the furs and began piling them on top of him one by one.

Even while doing so, I couldn’t figure out why Ju Hwaran kept coming to mind.

Song Ilseom, whom I had only glimpsed in passing, came to mind along with her.

*Now that I think about it, he was a suspicious bastard. He gave off an even worse stink than Gung Gibang.*

After learning about the relationship between the Yongbong Escort Bureau and the Zhongnan Sect, I became curious about that bastard’s identity.

His Level was an astonishing 110. At that level, he could probably flay one of the Ten Dragons and Phoenixes down to the bone.

He looked to be in his early to mid-thirties at most, but… which sect did he belong to, and who was he?

*Could he be an assassin sent by the Zhongnan Sect? No, that’s going too far.*

Had he simply fallen for Ju Hwaran’s beauty and stayed behind?

No. If that were the case, there would have been no reason for him to hide his true abilities. Was this one of those stories where the protagonist hides his power? Did some loser hiding his power look cooler when he rescued her?

*Ju Hwaran. We only exchanged a few words, but she seemed like a good person. And she had such a refreshingly direct way of speaking.*

She also possessed extraordinary martial talent, having reached the Peak realm at her age.

And then, again… yes. The dimples that appeared when she smiled were pretty. So were the eyes that curved like half-moons.

*Come to think of it, she looked like a cat.*

Cats had always been my favorite animals.

“Um, Captain?”

“Hm? Yeah?”

I turned my head and saw Hyuk Mujin staring at me strangely.

Not just him, either. Gung Gibang, Cheongpung, and even Baek Museong were all looking at me that way.

“What? Why is everyone staring at me?”

“Well, the thing is…”

Hyuk Mujin cautiously pointed at the pack frame.

“In my humble opinion, Great Hero Jeok is going to suffocate if this continues.”

“Gasp!”

I hurriedly flung off the furs that had piled up like a mountain.

Jeok Cheongang, who had nearly gone to meet that person while in a coma, was breathing faintly.

“Oh, Benefactor! You’re just like me!”

“Are you insulting me right now?”

“Ah. No, no. That isn’t what I meant…”

Ignoring Cheongpung, who instantly drooped, I began piling the furs back on. Jeok Cheongang’s small frame soon disappeared beneath them.

Only after confirming that enough air could pass through did I hoist the pack frame onto my back.

“All right. If everyone’s ready, let’s get going.”

We stepped outside amid Xi’an Tower’s lavish hospitality.

In Xi’an’s bustling streets, crowded with people, Baek Museong spoke through the noisy din.

“I’d like to see you off, but you won’t allow that, will you?”

“We’ll be seeing each other again later anyway.”

“Haha. I knew you’d say that. Then I’ll be off. Stay in good health, Martial Uncle Cheongpung.”

“Take care, Martial Nephew Baek!”

In the end, I hadn’t even brought it up. Good. This was fine.

Just as I was about to turn away with a lingering sense of unease amid the warm atmosphere, I heard someone speak.

“Did you hear? The Taeeul Merciless Sword of the Zhongnan Sect is in Xi’an.”

“What? The Taeeul Merciless Sword? Why on earth would he come here?”

“How should I know? Someone saw him heading toward Tengwang Pavilion in the west. Apparently, he’s meeting with the Yongbong Escort Bureau… but I can’t say for sure.”

The whispering voices slowly faded into the distance.

I asked Cheongpung,

“Young Hero Cheong.”

“Yes, Benefactor.”

“Have you tried tea?”

“Yes! I have!”

“No, you haven’t tried tea yet.”

If I said you hadn’t, then you hadn’t.
## Chapter artifact 318

# Chapter 318

“It's astringent.”

The old man muttered as he savored his Tieguanyin tea.

His shoulders were broad enough to belie his age, and his snow-white beard hung down to his navel, giving him the appearance of an immortal.

He certainly would have looked the part if not for the old sword resting against his side.

“I-I’m sorry, Senior. I haven’t reached my father’s level yet…”

“It’s a shame, but what can be done? When the owner changes, it’s only natural for the tea’s flavor to change as well. You may go.”

The owner of the teahouse, who had been bowing repeatedly, vanished as though he had been waiting only for those words.

The old man watched him disappear into the distance, then gently stroked the teacup.

“We three martial brothers used to stop by this place from time to time. That was more than thirty years ago. Your Master wasn’t the Sect Leader back then, either.”

“I see.”

Hyuk Sopyung answered from across the table.

He had kept his mouth shut for more than half an hour while the old man performed his tea ceremony, and his voice was cracked like a drought-stricken rice paddy.

“Would you like to savor a cup?”

The old man’s gentle voice contained not the slightest hint of coercion.

But when the old man in front of him offered something, it had to be accepted. Hyuk Sopyung knew that, as did the thirty members of the Taeeul Sword Unit stationed throughout the teahouse.

“I would be honored, Senior Martial Uncle.”

The old man picked up the jade-colored teaware containing the tea and tilted it over the empty cup Hyuk Sopyung had respectfully held out.

*Trickle.*

The tea began to fill the cup slowly.

At the same time, Hyuk Sopyung’s expression changed drastically.

“…”

“What is it?”

“I… It’s nothing.”

Contrary to his words, Hyuk Sopyung’s condition was anything but normal. His hand trembled, and his face had flushed red as if it might burst at any moment.

It was only tea, yet every drop that struck the cup bore down on Hyuk Sopyung with terrifying pressure.

*What the hell…?*

It was an enormous amount of internal energy. An overwhelming force that even Hyuk Sopyung, the Zhongnan Sect’s greatest prodigy, could not withstand despite receiving every elixir available without restraint.

He drew up all the internal energy in his body and poured it into the teacup, but he reached his limit almost immediately.

*Tap. Crack.*

The moment the last drop fell, a hairline crack spread across the cup in Hyuk Sopyung’s hand, and tea spilled over the rim.

That was when the old man’s gaze sank deeply.

He was Hwangbo Eom, the Taeeul Merciless Sword.

“How old are you this year?”

“I have reached thirty.”

“When was the last time you saw this old man?”

“Ten years ago.”

“Yes, that’s right. It was at the Huashan–Zhongnan gathering. Right there.”

The Huashan–Zhongnan gathering. Or the Zhongnan–Huashan gathering.

Huashan and Zhongnan—the dragon and tiger crouched in Shaanxi Province—held a gathering once every ten years where their young prodigies competed against one another.

Officially, it was meant to promote exchange and friendship through duels. But no one was ignorant of the fact that it was a competition between the two sects.

“I remember now. I watched with my own eyes as you were toyed with by that bastard Baek Museong.”

“…”

Hyuk Sopyung’s eyelids trembled.

How could he forget? That defeat. And the merciless gaze of The First Sword of Zhongnan, who had sought him out the moment he returned to the main sect.

“At your age, this old man had already mastered eight-tenths of the Taeeul Divine Technique. What about you?”

“...I apologize.”

“Ten years is enough time for mountains and rivers to change. Yet you’re still standing in the same place.”

*That applies to you too, Senior Martial Uncle.*

Hyuk Sopyung fought desperately to hold back the words rising in his throat.

*Surely you haven’t forgotten. Everything you did to me that day.*

Talent without effort could never bloom.

Hyuk Sopyung had loved martial arts. That was why he had been called the Zhongnan Sect’s greatest prodigy. He loved martial arts and swung his sword until his palms bled, sweating blood in the process.

The reason he had slowly fallen apart was not simply that he had been defeated by Huashan’s Lone Crane, Baek Museong, in front of everyone.

“I already know that you’re disgracing the name of our sect. I hear you’ve made quite a name for yourself in Xi’an.”

“Senior Martial Uncle…”

“This old man is speaking. Can’t you shut your mouth?”

Hwangbo Eom’s previously emotionless voice had now become colder than a thousand-year snowstorm.

“Watching you all has been like witnessing some kind of farce. From the highest ranks to the lowest, every one of you has been splashing mud onto the Zhongnan Sect’s signboard.”

The top referred to the Roaring Fury Swordsman, Song Il, while the bottom referred to Hyuk Sopyung.

Even though his only Senior Brother was laid up with an Internal Injury, Hwangbo Eom continued to spew venom at him. Hyuk Sopyung and the disciples of the Taeeul Sword Unit realized once again that the two words in his epithet—

*Taeeul Merciless Sword.*

The mercilessness was not reserved for his enemies.

“Your Master, who led the Zhongnan Sect into this state, is just as pathetic. How could our Master have handed the position of Sect Leader to such a man…?”

That was when Hyuk Sopyung’s tightly pressed lips finally parted.

“Your words go too far.”

“What did you say?”

*Whoosh.*

A gust of wind swept across Hyuk Sopyung’s entire body.

No—it was not wind.

It was a powerful aura flowing from the Taeeul Merciless Sword, the Supreme Peak master produced by Zhongnan.

“Your ears must have grown hard with age. Say that again.”

But Hyuk Sopyung did not yield, even beneath the suffocating pressure.

“Your words… *ngh.* Go too far.”

Though the Wind-and-Cloud Sword Lord had never shown him any warmth or affection, he was still Hyuk Sopyung’s one and only Master. And besides—

“He is the Sect Leader of the Great Zhongnan Sect. You are also a Disciple of the Zhongnan Sect, just like this junior. Show proper respect to the Sect Leader.”

“Respect for the Sect Leader?”

A sharp glint flashed through Hwangbo Eom’s eyes.

There had been a time when he was the one closest to ascending to the position of Zhongnan Sect Leader.

He had had a Senior Brother and Junior Brother under the same Master, but neither had been his rival. Neither of them could match his martial prowess or his ruthlessness.

The Sect Leader of the Zhongnan Sect should have been Hwangbo Eom. It was only natural.

“And what could a nobody like you possibly know to dare—?”

Hwangbo Eom was about to roar when he abruptly closed his mouth.

He had noticed Hyuk Sopyung’s unwavering gaze. He had also sensed the strange current flowing among the Zhongnan disciples of the Taeeul Sword Unit.

*These bastards.*

Hwangbo Eom’s gaze turned cold. At the same time, the powerful aura pouring from his body slowly subsided.

His lips moved beneath his snow-white beard.

“The Sect Leader of the Great Zhongnan Sect…”

Hwangbo Eom lifted the teacup, which was not even half empty, and drained it cleanly. Deep furrows formed between his wrinkled brows.

“It’s still astringent. The owner has changed, so the flavor and fragrance aren’t what they used to be.”

“…”

“The Great Zhongnan Sect? What a laughable thing to say. Zhongnan today is nothing more than a castle in the air. While you were lost in despair and wasting your days on drinking, women, and gambling, this old man was working to restore our sect.”

“What does that mean…?”

Confusion entered Hyuk Sopyung’s voice.

Hadn’t Hwangbo Eom shut himself away at the main sect? Even when his Senior Brother, the Roaring Fury Swordsman, returned with a serious Internal Injury, he had not shown his face even once.

*Then how…?*

Hyuk Sopyung’s thoughts were interrupted.

A group of people had just entered the teahouse.

At the front was a young woman whose mere appearance seemed to brighten her surroundings.

“I am Ju Hwaran, Young Bureau Head of the Yongbong Escort Bureau. I pay my respects to Great Hero Hwangbo, the Taeeul Merciless Sword.”

Ju Hwaran, the Dagger Hidden Flower.

At her bold greeting, the corners of Hwangbo Eom’s mouth lifted.

“Good. Did you safely bring the item I requested?”

He stroked his thick beard, his eyes flashing with an unreadable light.

* * *

“By the way, who’s the Taeeul Merciless Sword?”

Speed Beggar answered gruffly.

“Who do you think the Taeeul Merciless Sword is? He’s the Taeeul Merciless Sword.”

“Gibang. Don’t you wonder which is stronger—the five-tenths Eighteen Dragon-Subduing Palms or the seven-tenths Flame Divine Palm?”

“…”

“The Taeeul Merciless Sword, Hwangbo Eom. He’s the Junior Brother of the Roaring Fury Swordsman, Song Il, and the Senior Brother of the current Zhongnan Sect Leader, the Wind-and-Cloud Sword Lord.”

As expected, he was a walking encyclopedia of the Murim. I hadn’t brought him along for moments like this, but he was useful in more ways than one.

*Aside from the smell.*

I muttered inwardly as I continued walking.

We were on our way to a teahouse called Tengwang Pavilion. Gung Gibang, who had been walking beside me, muttered with clear displeasure.

“I’ve been thinking about this, and I don’t think it’s a good choice.”

“Why?”

“The matter is bigger than I expected. And it isn’t just anyone—it’s the Taeeul Merciless Sword. The Wind-and-Cloud Sword Lord is at least someone you can talk to, but that man…”

Gung Gibang couldn’t finish his sentence and shook his head repeatedly.

“Why? How bad can he be? Have you actually met him?”

“I saw him right beside my Master exactly once. And I thought to myself that he was someone I never wanted to meet again.”

Judging by Gung Gibang’s reaction, his first impression must have been spectacularly unpleasant.

He shuddered with a disgusted expression, then gave me a sidelong glance.

“You don’t even need to ask me. Neighbors know what goes on next door.”

At the end of Gung Gibang’s gaze was Baek Museong, who had been walking silently without saying a word.

His face, which usually wore a calm smile, had long since hardened like stone.

*Okay. I get the picture.*

*The Taeeul Merciless Sword.*

As you experience the Murim, you come to notice several interesting things. One of them is martial epithets.

A person’s epithet contains a part of who they are. It can tell you what weapon they primarily use—or what kind of personality they have.

In the case of Hwangbo Eom, the Taeeul Merciless Sword, it was both.

*Merciless. Just those two words tell me more or less what I need to know.*

I’d bet Hyuk Mujin’s wrist that he wasn’t some genial, chuckling neighborhood grandpa. If that wasn’t enough, I’d bet his ankle too.

That was when Gung Gibang spoke in an anxious voice.

“It’s not too late even now.”

“Hm? For what?”

“Interfering in matters between sects is likely to cause trouble. Even more so when the other party is the Taeeul Merciless Sword of the Zhongnan Sect.”

“So?”

“What do you mean, ‘so’? I’m saying we should stop fooling around and go to Sichuan!”

I blinked innocently.

“What the hell are you talking about?”

“Huh?”

“What meddling? We’re just going to have some tea. Right, Young Hero Cheong?”

Cheongpung, who had been chewing on the candied sweets I bought to keep him quiet, answered enthusiastically.

“Yes! We’re going to have tea!”

Gung Gibang stared at Cheongpung with an incredulous expression.

“Didn’t you say earlier that you’d already tried it?”

“Uh-huh. That was…”

No wonder his answer had sounded evasive.

Cheongpung had already polished off the sweets in the blink of an eye. He licked his fingers and looked back and forth between Gung Gibang and me.

His eyes dripped with longing as they swept across a street stall overflowing with snacks.

“Young Hero Cheong, you haven’t had tea before, have you?”

As I spoke, I spread my palm and waved it over Gung Gibang’s shoulder. Five more candied sweets were added to Cheongpung’s share, and he nodded excitedly.

“That’s right! I’ve never had tea before! My butt is itching to get to the teahouse!”

“That’s what he says.”

Gung Gibang, his will to fight completely gone, tore at his matted hair.

“Damn it. If Master beats me with the Dog-Beating Staff later, I’m telling him it’s all your fault.”

“Go ahead. Our Master is the Fire King.”

“You miserable bastard. You’re lower than a dog.”

“Stop whining and let’s go. What about you, Mujin? Are you dissatisfied too?”

Hyuk Mujin asked with a hopeful look.

“Am I allowed to say so?”

“Go ahead. If you want to die.”

“…”

“All right. We’re almost there.”

The old signboard bearing the name Tengwang Pavilion gradually came into view.

I walked straight ahead until I finally stopped in front of the teahouse door.

*Well, this is no joke.*

The Taeeul Merciless Sword. The greatest swordsman Zhongnan was proud of. The aura of a Supreme Peak master could be felt beyond the door, along with the presence of dozens of people carrying considerable qi.

The pack frame on my shoulders suddenly felt heavier.

“Old Master, don’t worry. No matter what happens, I’ll protect you.”

“Nothing will happen,” I muttered softly, then threw open the door.
## Chapter artifact 319

# Chapter 319

“I am Ju Hwaran, Young Bureau Head of the Yongbong Escort Bureau. I pay my respects to Great Hero Hwangbo, the Taeeul Merciless Sword.”

Ju Hwaran performed a formal clasped-hands salute.

The Taeeul Merciless Sword, Hwangbo Eom, truly lived up to his reputation. Just meeting his gaze made her chest tighten and left her struggling to breathe.

*The First Sword of Zhongnan…*

The Nine Sects and One Gang and the Five Great Families—the fifteen pillars supporting the current Murim.

The man standing before her was the greatest master of one of them, the Zhongnan Sect. The immense weight carried by his name pressed down on her.

*But it’s all right.*

She had completed an escort mission everyone had agreed was impossible.

That was why she could stand proudly even if the Wind-and-Cloud Sword Lord had come instead of the Taeeul Merciless Sword.

“Well? Did you bring the item I requested?”

“Of course.”

As she answered, Ju Hwaran took the wooden casket containing the Thousand-Year Snow Ginseng from inside her robes. The knot in the straw rope wound tightly around the entire casket bore a few small words.



Shandong Seongsu Jang Family.



After checking the writing, Hwangbo Eom nodded.

“No mistake. It bears the seal of the Seongsu Jang Family.”

People said that if Sichuan had the Tang Clan, then Shandong had the Seongsu Jang Family.

The Seongsu Jang Family was that famous for its medicine. Unlike the Sichuan Tang Clan, a Murim great family, it was a prestigious medical family whose roots lay in the practice of medicine.

The Zhongnan Sect had purchased the Thousand-Year Snow Ginseng through that very family and entrusted its transportation to the Yongbong Escort Bureau.

“The Pill Physician, the current Family Head of the Seongsu Jang Family, personally placed the Thousand-Year Snow Ginseng inside and signed it.”

“Oh? The Pill Physician did it personally?”

“Yes. Several witnesses, myself included, watched the entire process.”

“You’re remarkably thorough for someone your age.”

Hwangbo Eom’s wrinkled fingers stroked his white beard.

“This old man has heard that the Junzi Sword’s daughter is a gifted young woman. Thank you for handling such a difficult assignment so reliably.”

“Our Yongbong Escort Bureau does not tolerate even the slightest mistake in an escort mission.”

“That must be why you’re called the best in Shaanxi. Our sect operates an Escort Bureau as well, but it cannot compare with yours. Ha ha ha.”

Ju Hwaran’s heart pounded.

Was it because Hwangbo Eom had praised her?

No. It was because of an emotion that had nothing to do with that praise—a feeling constricting her chest. And she knew its name.

Anxiety.

*Something is wrong.*

It was an intuition bordering on foresight. But before Ju Hwaran could even begin to trace the source of her anxiety, Hwangbo Eom opened his mouth.

“Well, only the final procedure remains.”

They would inspect the requested item, then leave their signatures to prove that the handover had been completed.

After a simple procedure that would take less than a quarter of an hour, the four-month escort mission, which had cost them so dearly, would come to an end.

That was how it was supposed to happen.

*…Was it really?*

A chill unlike anything she had ever felt traveled up her spine.

Hwangbo Eom’s voice pierced her frozen ears.

“What are you waiting for? Show me the item.”

Ju Hwaran slowly raised her head.

His voice was kind and gentle. Yet the old man’s pitch-black eyes gleamed with a strange light.

A voice squeezed out with difficulty slipped between her red lips.

“…Great Hero Hwangbo.”

“Open the casket. With your own hands.”

Ju Hwaran realized it then—the source of her anxiety, and the fact that there was nowhere left for her to retreat.

In the end, only one choice remained.

*Rustle.*

Her thin, trembling fingers began to untie the knot. The wooden casket she had kept close to her heart for the past four months felt strange, as if she were seeing it for the first time.

*No. No, that can’t be. I’m sure of it. There’s no way…*

And then—

*Click.*

At last, the wooden casket opened, revealing what lay inside. A clear fragrance, straight roots, and a frost-covered, snow-white body.

There was no doubt that it was snow ginseng. But everyone who saw it stopped breathing and widened their eyes.

In the suffocating silence, Hwangbo Eom’s gentle voice rang out.

“How amusing.”

He crooked one wrinkled finger, and a powerful stream of internal energy flowed forth.

The snow ginseng floated into the air through Seizing an Object Through Empty Space as he continued.

“A Hundred-Year-Old Snow Ginseng… Is this old man seeing things because his strength has waned?”

It was obvious who he was asking.

Every gaze turned toward one place. The horrified Chief Escort Heo Jun—and Song Ilseom, who had been standing at an angle as though he were invisible—were no exception.

At the end of those dozens of pairs of eyes stood Ju Hwaran, her face pale and her eyes closed.

*It’s over.*

The moment she saw the Hundred-Year-Old Snow Ginseng inside the casket, she had closed her eyes rather than face what was happening.

Something that could not and should not have happened had happened.

*I saw it myself. I even had it in my possession.*

Where had everything gone wrong?

The past few months flashed through the darkness before her eyes like scenes from a dream.

She had staked the Yongbong Escort Bureau’s very survival on this mission.

The amount the Zhongnan Sect had offered for it was an enormous sum. But if they failed, they would have to pay a penalty ten times that amount.

And now, this double-edged sword had plunged straight into the hearts of both her and the Yongbong Escort Bureau.

“I won’t ask how this happened. I’m not particularly curious about what extraordinary circumstances caused the Thousand-Year Snow Ginseng to turn into a Hundred-Year-Old Snow Ginseng. However…”

Hwangbo Eom swept his gaze over the people of the Yongbong Escort Bureau, including Ju Hwaran, with a deliberately regretful expression.

“We will have to receive compensation for this matter.”

“……!”

“Our sect already paid the Seongsu Jang Family one hundred thousand silver nyang for the Thousand-Year Snow Ginseng. And if the Yongbong Escort Bureau successfully completed the escort mission, we agreed to pay a fee of ten thousand silver nyang—one-tenth of the cargo’s value.”

The value of the lost Thousand-Year Snow Ginseng, plus the tenfold penalty the Yongbong Escort Bureau owed for failing to fulfill the contract.

Together, they amounted to the astronomical sum of two hundred thousand silver nyang. It was an amount they could cover only by selling off most of what the Yongbong Escort Bureau owned.

When Ju Hwaran realized that, blood ran from her lips, and Chief Escort Heo Jun’s face darkened.

“G-Great Hero Hwangbo, that is…”

“Two hundred thousand silver nyang. I will not permit any compromise.”

“A-Ah…”

The escorts who had accompanied Ju Hwaran let out groans of despair.

Every one of them except Song Ilseom.

Even though the Escort Bureau where he had worked for nearly ten years had fallen into a desperate crisis, he showed no reaction at all. He merely twitched the corner of his mouth once.

Hwangbo Eom caught the movement out of the corner of his eye, then held out a full cup of tea to Ju Hwaran.

“Have a cup. When your mind is troubled, nothing is better than a warm cup of tea.”

Ju Hwaran’s long eyelashes, which had been tightly shut, trembled. Slowly, she opened her eyes and stared at Hwangbo Eom.

“Is this… Is this Zhongnan’s way?”

“I’m afraid I don’t know what you mean.”

Hwangbo Eom gave a soft laugh and tipped his own teacup.

As expected, it was astringent. The young owner who had inherited the teahouse from his family was still inexperienced.

And yet, for some reason, the aroma and flavor lingering in Hwangbo Eom’s mouth now were incomparable to what he had tasted a moment ago.

“Very good. It feels as if I’ve gone back thirty years.”

“……!”

“What’s wrong? Why don’t you drink it before it gets cold?”

Ju Hwaran silently bit her lip.

She had been completely outmaneuvered. Even after taking every precaution, she had still fallen into the trap.

For the past two years, she had led the Escort Bureau in place of her father, the Junzi Sword, Ju Hogun. She had experienced all sorts of failures and setbacks, both large and small, but she had never faced anything as hopeless as this.

*Can I rise again like before?*

She might stumble, but she had never been brought down. Yet two hundred thousand silver nyang possessed enough destructive power to crush the Yongbong Escort Bureau to death.

*We can pay the penalty.*

It was possible.

They would have to sell every field and parcel of land owned by the Yongbong Escort Bureau at a bargain price, then send away the hundreds of caravan porters, escorts, and Escort Captains whose wages they could no longer pay.

And once that entire process was over, nothing would remain of the Yongbong Escort Bureau but an empty shell.

*Is it really over? Just like this?*

Hwangbo Eom watched Ju Hwaran with an amused expression.

He had long heard that the Young Bureau Head of the Yongbong Escort Bureau was quite capable.

But to him, she was still nothing more than an inexperienced greenhorn.

*Heh. How pitiful.*

That was when Hwangbo Eom was quietly laughing to himself.

“Hmm?”

His gaze suddenly turned toward the door of the teahouse. Several people’s qi was drawing closer.

*This is…*

The qi was so powerful that even Hwangbo Eom, a Supreme Peak master, could not easily ignore it.

A vast amount of internal energy, comparable to that of an Elder of the Nine Sects and One Gang, slowly approached. Then it abruptly stopped right outside the teahouse.

*Could it be Huashan?*

Hwangbo Eom’s expectation was spectacularly wrong.

*Creaaak.*

“Oh, I was just in the mood for some tea, and look at that! There’s a teahouse right here.”

A broad-shouldered young man opened the door and entered at the front.

Hwangbo Eom’s eyes sank deeply as he looked at Jin Taekyung.

* * *

Even at a glance, it was an unusual sight.

Dozens of swordsmen stood scattered throughout the room, and the air had grown heavy.

*Ju Hwaran—or rather, the Yongbong Escort Bureau?*

The question had barely arisen when I spotted them.

On a table surrounded by people, a pair of slender fingers trembled faintly.

I had only seen her once, but I could tell who they belonged to just from her fingers. Funny how that worked.

*Were her hands pretty?*

As I scratched the back of my head, everyone’s gaze flew toward me.

A middle-aged man who appeared to be the owner of the teahouse hurried over and bowed repeatedly.

“Sir, I’m sorry, but we’re completely full right now…”

“There’s a seat over there.”

“That seat isn’t in use.”

“Then I’ll have my tea standing.”

At that moment, a martial artist who appeared to be a Disciple of the Zhongnan Sect approached with measured steps.

“Are you a martial artist?”

“No, I’m just fat.”

The martial artist looked me up and down as though he had found a complete lunatic.

“I don’t know who you are or where you come from, but an important person is here right now. You would do well to leave.”

“I’m an important son in my own family too, so why should I? There’s plenty of room anyway.”

“……You’re being troublesome. I am a Disciple of the Great Zhongnan Sect. You should understand by now, so leave.”

“Why do you keep telling me to leave? I just want to sit down and have a cup of tea.”

From behind me, Cheongpung suddenly shouted excitedly.

“Benefactor! Candied sweets too!”

“Candied sweets? Hey, Mujin. Does this teahouse sell them too?”

“Are you seriously saying that right now?”

What the hell was with these guys?

The Zhongnan Sect disciple had been looking at us as if to say exactly that, but his face stiffened when he spotted someone.

“H-Huashan’s Lone Crane, Baek Museong!”

Maybe it was because this was Huashan’s home ground, but more than one person here recognized Baek Museong’s face.

In any case, the Zhongnan Disciple’s involuntary shout had an immediate effect. Unlike when we had first entered, everyone was now looking at us.

Two gazes stood out from the rest.

I waved at one of their owners.

“Oh, we meet again.”

“…Young Hero Jin?”

Ju Hwaran stared at me with her pale face and wide, round eyes.

Across from her sat an old man with a white beard hanging down from his chin.

I gave Ju Hwaran a small smile, then gazed intently at the old man.

“Is there some problem between you and Young Lady Ju?”

The old man, the Taeeul Merciless Sword Hwangbo Eom, stroked his beard and laughed.

“An interesting fellow has appeared.”

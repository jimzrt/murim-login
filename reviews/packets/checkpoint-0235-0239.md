# Checkpoint Review — 235–239

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

# Chapters 235–239

## Plot

Jeok Cheongang intensifies Taekyung’s training on Mount Jiuhua with waterfall stances, weighted exercises, cliff climbing, and other ordeals. Taekyung completes Fire King’s Hellfire Training-2, earns the Unmoving achievement, converts Toughness into Endurance, gains levels and Bonus Points, and continues training for over two months. Jeok’s worsening sleep and memory loss become apparent, but he brings Taekyung into the Fire Gate Cavern and offers to pass down the clan’s martial arts. Taekyung accepts, becoming the heir to the Fire Gate lineage, and trains there for a year.

After leaving the cavern, Taekyung and Jeok descend Mount Jiuhua. Taekyung gives a struggling herbalist a ginseng root, which Namgung Ryong purchases for three hundred silver nyang after arriving with a large escort. The pair then travel to the Nangong Family estate for the Azure Sky Sword King’s birthday. Taekyung’s chained iron balls cause a confrontation with the guards, but Namgung Ryong orders them to admit him.

Namgung Ryong asks Taekyung to prevent a duel between Jeok and the Azure Sky Sword King, warning that the clash could devastate the martial world. After Nangong Ok confronts Taekyung, Taekyung deliberately summons Namgung Cheon to a secluded mountain and asks him to delay the duel for one year. Namgung Cheon agrees to consider the request if Taekyung withstands three moves. Taekyung accepts the Sudden Quest Three-Move Kill, removes his shackles, and faces the Azure Sky Sword King’s opening Emperor’s Sword Form.

## Continuity

- Taekyung completed a year of training in the Fire Gate Cavern and is publicly recognized as Jeok Cheongang’s Disciple and heir to the Fire Gate Clan’s orthodox lineage.
- Taekyung can open the cavern using the internal energy of the Scorching Sun Divine Arts.
- Taekyung’s chained Ten-Thousand-Year Cold Iron balls remained on his limbs throughout training; Jeok held the key until Taekyung removed them before facing Namgung Cheon.
- Taekyung completed Fire King’s Hellfire Training-2, earned Unmoving, converted Toughness into Endurance, gained two levels, and received 50 Bonus Points.
- Jeok Cheongang’s dementia and infirmities of old age continue to progress despite a temporary easing of his symptoms.
- Jeok harvested Mount Jiuhua’s spiritual herbs; Taekyung gave one remaining ginseng root to Hong, a herbalist from Sichuan.
- Namgung Ryong is the Family Head of the Namgung Family, the richest man in Anhui; Nangong Cheon is its Grand Family Head, the Azure Sky Sword King.
- Nangong Cheon once spared Jangcheon in exchange for a spar with Jeok; Jeok won by half a form, after which Nangong Cheon entered seclusion.
- Nangong Ok is Namgung Ryong’s only child, the Nangong Family’s Lesser Family Head, and the Sword Dragon.
- Namgung Ryong wants Taekyung to stop the duel between Jeok and Nangong Cheon because of the danger to both masters and the wider martial world.
- Nangong Cheon will delay the duel for one year only if Taekyung withstands three moves. The outcome of the first move remains unresolved.
- Open hooks include the progression of Jeok’s illness, Namgung Ryong’s investigation of Taekyung, Jin Wikyung’s private matter for Jeok, Cheongpung’s discipleship plans, Dark Heaven’s purpose, the approaching calamity, and whether the birthday invitation was chiefly a pretext for another duel.

## Translation Decisions

- Use Fire Gate Cavern for 열화동 and Heir of the Fire Gate for 열화의 계승자.
- Preserve Fire King’s Hellfire Training-2 as distinct from Fire King’s Inferno Training-1.
- Use Fist-and-Foot Training for 권각 수련 and fist-and-foot martial arts for 권각술.
- Retain Mountain Spirit, samgyeopsal, and the Sichuan Province tile-game pun.
- Use Namgung Ryong and Namgung for the family name in ordinary references; retain Nangong Ok and Nangong Cheon in the formal names established for the family’s younger and elder heads.
- Render 검룡 as Sword Dragon, 제왕검형 as Emperor’s Sword Form, and 삼초살 as Three-Move Kill.
- Render 검미새 as sword nut, 노환 as infirmities of old age, and 헨젤과 그레텔 as Hansel and Gretel.

## Durable state

{
  "active_continuity": [
    "Jeok Cheongang publicly recognizes Jin Taekyung as his Disciple and heir to the Fire Gate Clan's orthodox lineage.",
    "Taekyung completed a year of training in the Fire Gate Cavern and remains bound to chained Ten-Thousand-Year Cold Iron balls whose key Jeok holds.",
    "Jeok Cheongang's dementia and age-related weakness have eased but continue to progress.",
    "Taekyung and Jeok Cheongang arrived at the Nangong Family estate in Anhui for the Azure Sky Sword King's birthday celebration.",
    "The Nangong Family is one of the Five Great Families and the hegemon of Anhui, with more than one hundred blood relatives and thousands of subordinate martial artists.",
    "The Azure Sky Sword King is the Grand Family Head of the Nangong Family and is obsessed with swords and martial training.",
    "The Azure Sky Sword King spared Jangcheon in exchange for a spar with Jeok Cheongang; Jeok won by half a form, after which the Sword King entered seclusion.",
    "Namgung Ryong is the Family Head of the Namgung family and orders Taekyung admitted after guards challenge his chained training equipment.",
    "Ten Peak martial artists guard the pavilion where Namgung Ryong receives Taekyung.",
    "Namgung Ryong's only child is Nangong Ok, the Nangong Family's Lesser Family Head and the Sword Dragon, one of the Ten Dragons and Phoenixes.",
    "Namgung Ryong asks Taekyung to stop the duel between Jeok Cheongang and Namgung Cheon because of the danger to both masters and the wider martial world.",
    "Namgung Cheon agrees to consider Taekyung's request only if Taekyung withstands three moves.",
    "Taekyung accepts the Sudden Quest Three-Move Kill and removes his chained iron balls before Namgung Cheon's first attack."
  ],
  "continuity_sources": [
    238,
    239
  ],
  "open_questions": [
    "How quickly will Jeok Cheongang's dementia progress, and how much time does he have to teach Taekyung?",
    "Why has Namgung Ryong committed the family's intelligence network to investigating Taekyung?",
    "What important matter does Jin Wikyung need to discuss privately with Jeok Cheongang?",
    "Did Mae Jonghak actually grant Cheongpung permission to become Jeok's Disciple, and will Baek Museong escort Cheongpung to Huashan or search the Central Plains for Mae?",
    "What is the unknowable calamity approaching as the heavenly patterns become distorted?",
    "What does Dark Heaven intend, and how is it connected to the approaching calamity?",
    "Is the Azure Sky Sword King's birthday invitation a pretext for another spar with Jeok Cheongang?",
    "Can Taekyung withstand Namgung Cheon's three moves and secure the requested delay?"
  ],
  "safe_through": 239,
  "temporary_decisions": [
    "Use Hidden Thread for 비선 and Lesser Threads for 소선.",
    "Use Huangshan Sect for 황산파 and Mountain Lord for 산주.",
    "Use Namgung Ryong for 남궁룡 and Namgung for 남궁.",
    "Use concealment technique for 은형술.",
    "Use Pressure-Point Strike for 점혈 and Sleep Acupoint for 수혈.",
    "Use Heaven-grade for 천급; Fire King's Special Restriction Pill for 화왕 특제 금제단.",
    "Preserve the source's quest-title variants: 화왕의 불지옥 수련-1 is Fire King's Inferno Training-1, while 화왕의 지옥불 수련-1 is Fire King's Hellfire Training-1.",
    "Render 검미새 as sword nut, 노환 as infirmities of old age, and 헨젤과 그레텔 as Hansel and Gretel."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 235

# Chapter 235

The training Jeok Cheongang put me through was simple.

Take a horse stance beneath the waterfall. Do push-ups. Go fetch me some bird eggs because I feel like eating them…

That much was fine. The problem was the options attached to every exercise.

“Six shichen[^2] in a horse stance.”

“You’re joking, right?”

“Does it sound like I’m joking?”

Whoosh!

It was a waterfall plunging hundreds of jang below. Even with my exceptional physique, just one shichen beneath it left my entire body aching as though it had been smashed apart, and my vision growing hazy.

And he wanted me to stay there for six shichen. In a horse stance, no less.

“Old Master, this is a bit much. If I stay in there for six shichen, I’ll really die.”

“Have you tried it?”

“Huh?”

“Try it before you say that. If you don’t like it, go back to your family.”

It took me ten full days to complete the Quest.

As a side effect, I briefly lost consciousness. When I opened my eyes again, the iron balls had grown heavier.

“An additional hundred geun[^1]. From now on, we’re increasing it to twelve shichen.”

“……”

For a moment, I considered using Logout.

But I had to finish the training. It might have looked foolish to some people, but it was a rule I had set for myself when I began.

*If I go back, both my body and mind will grow lax.*

Whoosh!

The pressure of the waterfall was terrifying. With my internal energy and physical abilities restricted, I had to endure using nothing but my body and mental strength.

At last, when I finished the waterfall training, I was greeted by legs harder than steel—and an unexpected System notification.

Ding.

> **System**
>
> **Fire King’s Hellfire Training-2** has been completed successfully!
>
> Outstanding achievement: **Unmoving** achieved!
>
> **Toughness** changes to **Endurance**!
>
> **Level Up!**
>
> **Level Up!**
>
> You acquired 50 Bonus Points!

The training continued without pause. I wasn’t even given time to rest.

I got one shichen of blissful sleep a day. Other than that, everything was part of my training.

“Next are push-ups.”

“That’s too easy. Wait. How many?”

“Ten thousand. Put the iron balls on your back.”

“……”

It was the most hellish push-up routine in the world. But I gritted my teeth and did it.

On the day I completed every kind of push-up Jeok Cheongang wanted, the year’s first sprouts were pushing up from the ground.

“The weather has grown warm. I feel like eating a swallow’s nest dish for once, so go fetch one.”

“Aren’t swallows migratory birds? They won’t come until it gets warmer.”

“You know nothing! This old man has lived on Mount Jiuhua his entire life. By this time, a few impatient swallows should already be starting to build their nests.”

“Whew. Where am I supposed to look for them?”

“Cliffs.”

That was the Quest that took the longest. I had to find a swallow’s nest when I didn’t even know where one might be.

By then, I was combing through every cliff on Mount Jiuhua, carrying iron balls that had long since surpassed a thousand geun in total weight.

At last, I found a newly completed swallow’s nest and brought it to Jeok Cheongang.

“Here it is. A swallow’s nest.”

His long silence was followed by a single muttered sentence that was more than enough to snap the last thread of my patience.

“……It really exists.”

“You fucking old bastard!”

My eyes rolled back, and I lunged at Jeok Cheongang. He beat me within an inch of my life.

When I came to again, the iron balls had grown heavier. That was only natural.

“If you’re awake, get moving.”

“Is this a new training routine?”

“It is. In a sense.”

Jeok Cheongang thrust a deranged schedule in front of me.

It contained every single thing I had done so far, without leaving out even one.

“Three round trips across Mount Jiuhua in the morning, ten thousand one-arm push-ups on each side at noon. Climb the cliffs, then take a horse stance beneath the waterfall… Human, are you insane?”

“Five hundred geun more if you don’t like it.”

“I’ve actually wanted to spend every day like this for a long time. I’ll be right back.”

“Good.”

From then on, I did whatever he told me to do.

I wondered if it was even possible, but once I tried it, it turned out to be possible.

When your body is exhausted, the day passes quickly. As the training grew more intense, time flew by faster and faster.

* * *

The frozen earth thawed, and fresh sprouts began to bloom.

Two months passed, but my daily routine remained unchanged. The only differences were that the training had become more brutal and the iron balls had grown heavier.

Rustle.

Flowers and grass that had grown tall brushed against my calves.

On one of Mount Jiuhua’s high peaks, painted in vivid colors, Jeok Cheongang, who had been sleeping with his back against a tree, groggily opened his eyes.

“Is that you?”

“Who else would come looking for you besides me?”

“I thought you were the Grim Reaper.”

“I think even the Grim Reaper would run away in fear.”

Jeok Cheongang let out a short laugh at my nonsense.

“You grow more flattering by the day.”

“Yes, and you’ve been sleeping more, too, Old Master.”

Just as I said, Jeok Cheongang had been sleeping much more often lately. Given his age, perhaps it was only natural.

“I was training.”

“Ah. In your dreams?”

“I was merely resting my eyes.”

“You were snoring.”

“……Ahem. More importantly, what are you doing here instead of training?”

“I’m finished.”

“Already?”

Jeok Cheongang’s eyes widened slightly.

“I wasn’t slacking off, so don’t give me that suspicious look.”

“Who said anything? Fine, then shut your mouth and work on your fists and feet.”

“Yes, sir.”

I answered promptly and took up a stance in an open area not far away.

Unlike spear techniques, I was practically a beginner when it came to fists and feet, so I was currently working on my fundamentals.

“You know what you’re supposed to do, right?”

“Yes, yes.”

Ding.

> **System**
>
> Repeat Quest **Fist-and-Foot Training** has been created.

I began with the simplest straight punch.

Each movement came with the insane requirement of one thousand repetitions, but compared to everything I had done before, it was easy.

*The fact that I think this is easy means I’m going insane, too.*

After letting out a deep sigh, I began throwing punches.

Whoosh. Bam!

The wind split around my fists, and compressed air burst outward.

In the past, I had simply relied on strength, speed, and internal energy. Now, I could perform each movement accurately and control my strength accordingly.

Clatter!

How long had I listened to the chains connected to my wrists sway and rattle? I kept driving my fists into an imaginary point without pause until I heard a System notification in my ear.

Ding.

> **System**
>
> Repeat Quest **Fist-and-Foot Training** has been completed successfully!
>
> Perfect movements without a single error!
>
> **Strength**, **Stamina**, and **Agility** have each increased by 1!
>
> You have not yet learned fist-and-foot martial arts. Additional rewards will be granted when you acquire a related martial art in the future!

The rewards from the repeat Quest were worthwhile. The quality of the rewards decreased with each repetition, but even this was more than enough to make me grateful.

*I think I could do this two or three more times.*

You only received rewards after accepting the Quest.

I relaxed my stance and walked toward Jeok Cheongang. He was watching me from beneath the tree, just as before.

“Old Master. I’m finished.”

“……”

“Old Master.”

“Uh… huh?”

He snapped awake and looked up at me.

“What is it?”

“I finished the fist-and-foot training.”

“What did you finish?”

“The fist-and-foot training. Fists and feet!”

“What are you talking about?”

“You told me to do it. About a shichen ago.”

“What?”

Jeok Cheongang narrowed his eyes.

“When did I?”

“Huh?”

“Why are you suddenly saying such nonsense? This old man has been sitting here watching you with both eyes wide open.”

“……”

*What the hell is going on here?*

I asked him, bewildered.

“Why are you doing this to me?”

“What?”

“Are you doing this on purpose to make me train more? You didn’t have to go this far. I was planning to keep training anyway.”

“What kind of nonsense are you spouting?”

Jeok Cheongang was about to erupt in anger when he suddenly closed his mouth.

For an instant, unknowable emotions passed across his wrinkled face. After remaining silent for some time, he finally spoke.

“You’re a perceptive one. If you’ve figured it out, go and practice your fists and feet some more.”

Ding. A notification appeared telling me that a Quest had been created, but I didn’t move an inch.

I stared at Jeok Cheongang for a long moment before suddenly opening my mouth.

“Old Master. I just want to ask you something.”

Jeok Cheongang’s shrewd, gray eyes trembled.

The suspicion I had thought *could it be?* became certainty.

“Are you feeling unwell?”

It wasn’t an easy subject to bring up, so I had phrased it indirectly. But there was no doubt that he understood what I meant.

After a suffocating silence, a sigh-like word escaped Jeok Cheongang’s lips.

“……Follow me. There is somewhere we need to go together.”

* * *

Dementia.

Even in the modern world, where magical medicine had advanced tremendously, dementia remained an illness that could not be completely cured.

Its progression could only be slowed. Everyone was equal before the curse of time.

*Why didn’t I realize it?*

Thinking back, there had definitely been warning signs. His increasing hours of sleep, and the kind of forgetfulness he had just displayed—I had noticed it several times before.

Even so, I hadn’t been particularly suspicious because he wasn’t an ordinary old man.

*Fire King Jeok Cheongang.*

I had never imagined that a Supreme Peak master whose martial arts had reached the heavens could suffer from the ailments of old age.

Perhaps it was a fact even Jeok Cheongang himself wished to deny.

“The history of our sect stretches back hundreds of years.”

Jeok Cheongang’s voice echoed through the cave.

The inside was hot and humid like a steam sauna, and the deeper we went, the more intense the heat became.

I had already been staying on Mount Jiuhua for more than two months, but I had never once visited this place.

“Our founding ancestor was the greatest under heaven of his era. However, his forthright nature earned him many enemies.”

His calm voice continued like flowing water.

It was the history of the Fire Gate Clan, from its beginning to the present.

From the first Sect Leader to Jeok Cheongang’s master, the seventeenth Sect Leader.

Some of them went out into the Murim and made their names known throughout the world. Others remained buried in the countryside their entire lives and quietly raised successors.

Countless sects had fallen over the past several hundred years, but the Fire Gate Clan had preserved its lineage.

“Even that became uncertain in this old man’s generation. It is all the result of my lack of virtue.”

After about half an hour, we finally stopped walking.

By then, my entire body was drenched in sweat.

The heat was coming from beyond a moss-covered stone gate.

“This place is…”

“The Fire Gate Cavern. This is where our sect began, and where its legacy continues.”

Jeok Cheongang gazed at the stone gate with a nostalgic expression before placing his palm against its surface.

The instant the Scorching Yang Qi flowing from his fingertips touched the stone gate, an intricately engraved sun emblem began to shine, and the firmly closed gate slowly opened.

“……Whoa.”

I stared into the Fire Gate Cavern as though entranced.

It was several times larger than the training hall of the Jin Family of Taiyuan. Seventeen urns had been arranged around a blue-white flame.

It wasn’t difficult to guess what the urns contained.

*The former Sect Leaders of the Fire Gate Clan.*

Their funeral urns, most likely. Just as I expected, Jeok Cheongang abruptly dropped to his knees and bowed deeply before the urns.

“Your unworthy Disciple, Jeok Cheongang, pays respects to the Sect Ancestors.”

He rose and gestured for me to follow.

“Come in.”

“Ah, yes. Excuse me.”

The instant I carefully stepped into the Fire Gate Cavern, a System notification pierced my ears.

Ding.

> **System**
>
> You have entered **Fire Gate Cavern**!
>
> The effects of **Fire Gate Clan** martial arts are amplified when learned!
>
> Your **Scorching Yang Qi** is reacting intensely!
>
> The restriction on **internal energy** has been lifted!

Hummm.

The internal energy in my dantian, awakened from its long slumber, spread through my limbs and body.

Jeok Cheongang spoke as though he had already expected my astonished expression.

“Your internal energy comes from the Blazing Flame Divine Pill. It is only natural that it would react to the Fire Gate Cavern.”

*Found its roots—is that it?*

It was a strange feeling. As my internal energy throbbed like a living creature, my heart began to pound as well. This place, where I was setting foot for the first time, felt strangely familiar.

“Sit.”

We sat facing each other with the flame between us.

Beyond the blue-white fire, Jeok Cheongang’s face looked noticeably older.

“I will pass on our sect’s martial arts to you.”

“……!”

“What? Did you think I would suddenly tell you to become my Disciple?”

“To be honest… yes, I did.”

“A master and Disciple are not bound together by necessity or coercion. Besides, this old man is already suffering from the ailments of old age. Learning from me will place you in great danger as well.”

Every word Jeok Cheongang said was perfectly reasonable.

If he became confused about the formula of an internal cultivation technique, if he forgot even a single word, I would cross an irreversible river.

The river of qi deviation—or death.

“Can you learn martial arts from someone like me?”

I took a deep breath.

Only after finishing countless worries and thoughts did I finally reach a conclusion.

“I will.”

“I’ll say it again…”

“I trust you, Old Master. That’s enough.”

At that moment, indescribable emotions rose over Jeok Cheongang’s face, leaving him speechless.

Then a smile spread across his wrinkled lips.

“Then we’re alike in that regard.”

One-person succession, never passed on to the wrong person.

The Fire Gate Clan had been passed down for hundreds of years to a single person at a time—one talented individual who could be trusted not to commit evil deeds.

The fact that Jeok Cheongang had brought me here to the Fire Gate Cavern meant that he already trusted me.

*Fire King Jeok Cheongang trusted me and chose me. He intends to pass everything in the Fire Gate Clan on to me.*

My heart swelled at the thought. As though it had sensed my emotions, the blue-white flame surged violently.

Ding.

> **System**
>
> Quest **Heir of the Fire Gate** has been created!

Along with the System notification, Jeok Cheongang reached out his hand. As Seizing an Object Through Empty Space took effect, the lid of a dark metal box that had risen from the flames opened.

I read the title of the old book floating toward me.

“Fire Gate Divine Technique…”

I instinctively understood. This was the foundation of the Fire Gate Clan, a martial art that was practically the clan’s entirety.

Jeok Cheongang had risen to his feet and now stood straight behind me.

“We’ll begin at once, so sit cross-legged and close your eyes. From now on, circulate your energy according to the formula I teach you.”

I followed his instructions and closed my eyes. In the darkness filling my vision, the blue-white flames seemed to flicker.

At last, Jeok Cheongang’s voice pierced my ears.

“What about your fist-and-foot training?”

“……Huh?”

“Did you finish your training and start slacking off? Wait, fuck, that startled me. This is the Fire Gate Cavern. What the hell is this?”

“……!”

*Oh, fuck. Dementia…*

* * *

After that day, the two people who had caused such a commotion on Mount Jiuhua for some time vanished without a trace.

While they were gone, the trees sprouted green leaves, the flowers bloomed in full, and the swallows built their nests on the cliffs.

From green, to autumn foliage, and then to white snow.

Until Mount Jiuhua changed clothes three times.

[^1]: A *geun* is a traditional Korean unit of weight; here, one geun is approximately 600 grams.

[^2]: A *shichen* is a traditional time unit of approximately two hours.
## Chapter artifact 236

# Chapter 236

The man gazed at the neatly arranged Four Treasures of the Study.

The brush was made from sable fur, the inkstone was bluish jade, and the ink and paper were tribute goods said to be used by the royal family of Haedong,[^2] ten thousand *li* away.

[^2]: Haedong is a traditional name for Korea.

Every one of them was a luxury that only the wealthiest of the wealthy could afford.

“Excellent. Simply excellent.”

A satisfied smile spread across his face. The man was famous for his frugality, and the only luxury he allowed himself was the Four Treasures of the Study.

“Well, then. Shall we begin?”

Just as the man was happily grinding his ink, the door opened, and someone approached with brisk, unhesitating steps.

“Anyone who saw you would think you were a Hanlin Academician.”

The unexpected visitor was a martial artist covered in dust.

He had narrow, sharply slanted eyes and a well-worn sword hanging from his waist. The man made a show of hardening his expression when he saw him.

“A Hanlin Academician? I’d rather you call me a master painter.”

“You still paint?”

“It’s my only pleasure.”

“Sadly, you don’t have the bearing of a master painter. Would you like to learn some martial arts from me?”

“I must respectfully decline. This is the limit of my abilities as a martial artist.”

“What a shame. You seem to lack the qualities a martial artist ought to possess.”

“It doesn’t matter. I have a subordinate who handles a sword brilliantly. Why else would his epithet be Ghost Sword?”

At the man’s sly response, the unexpected visitor’s expression slowly relaxed.

The next moment, the two of them let out quiet laughs as though they had planned it together.

“My lord, you haven’t changed.”

“Neither have you, Wipeng.”

It had been no less than four months since they had last seen each other, which made their reunion all the more welcome.

Jin Wikyung, the Lesser Family Head of the Jin Family of Taiyuan, wore a broad smile as he slapped Wipeng on the shoulder.

“What brings you here without any warning? The messenger pigeon said you wouldn’t arrive until noon tomorrow.”

“The Jin Dragon Squad can manage perfectly well without me.”

The Jin Dragon Squad was currently the Jin Family of Taiyuan’s foremost armed force.

It had been established only a year ago, but every member possessed impressive martial skills, and their loyalty to the family was even greater.

The fact that Wipeng, Jin Wikyung’s trusted subordinate, served as its Commander was enough to reveal the squad’s status.

“You didn’t slip away by yourself without telling anyone, despite being the Commander, did you?”

“Of course not. I left that Hyuk fellow in charge. He’ll manage just fine.”

“The acting Deputy Commander?”

“Yes.”

“This was his first mission, wasn’t it? What did you think after watching him?”

Wipeng’s eyebrow twitched.

He had thought he was becoming somewhat accustomed to Hyuk Mujin, but merely thinking about the man gave him a headache.

Still, business was business, and personal feelings were personal. His answer came out like a sigh.

“He’s serviceable enough. The only problem is that he never stops running his mouth.”

“I had a rough idea, but he sounds more cheerful than I expected.”

“He’s so goddamn cheerful it’s a problem.”

“What about the rest?”

“…If you teach him things one by one, he does learn quickly.”

“If you’re saying that, he must possess considerable martial talent.”

A year earlier, Hyuk Mujin had been granted the honor of joining the Jin Dragon Squad in recognition of his service.

Naturally, Jin Taekyung’s influence had played a role in that decision.

*That fellow is better than he looks. Try raising him.*

Jin Wikyung would do anything for his younger brothers.

On the off chance Taekyung was right, he had placed Hyuk Mujin in the Jin Dragon Squad and assigned Wipeng to train him. The young man’s skills had improved by the day.

His slick personality allowed him to get along well with the other members, and there was no question about his loyalty.

“Ha-ha-ha! As expected of our youngest—he has an eye for people.”

Jin Wikyung laughed heartily. In his hand was a bottle of liquor that no one had seen him take out.

After filling a cup to the brim and handing it over, he spoke.

“In any case, you’ve worked hard. So, is everything in Northern Gaoyuan settled now?”

“Yes. There shouldn’t be any trouble for at least the next ten years.”

Stabilizing Northern Gaoyuan.

That was why Wipeng had been away from the Jin Family of Taiyuan for the past four months.

Jin Wikyung believed that he needed to subjugate the mounted bandits of Gaoyuan to become the true hegemon of Shanxi Province. After months of secret, meticulous preparation, he had swung his sharpest weapon at them.

The sword known as Ghost Sword Wipeng.

“We attacked from seven directions, and they collapsed without being able to do anything.”

The Murim of Shanxi—and especially the sects and merchant groups in the northern region, which had suffered the most damage—welcomed the Jin Family of Taiyuan’s bold decision and actively cooperated.

The so-called Seven-Route Army had been formed with Wipeng and the Jin Dragon Squad at its forefront. With the merchants’ full support, they were equipped with quality weapons and warhorses.

They also had a powerful ally.

“The Lower District Sect was frightening. I was reminded once again of how terrifying information can be.”

The Lower District Sect had received a considerable share of the northern region’s interests immediately after the war ended, and they had welcomed Jin Wikyung’s decision with open arms.

Like seasoned information merchants, they monitored the mounted bandits’ every move while spreading false information and setting traps.

Their thoroughness was enough to make even Jin Wikyung shake his head in admiration.

“Everything in this world is used differently depending on who owns it. But the truly frightening one is Wolhwa. She isn’t meant to be confined to Shanxi Province.”

“Is that so?”

“Can’t you tell from the results? Her true weapon isn’t her beautiful appearance. It’s her strategy.”

Two thousand.

That was the number of mounted bandits who had been killed or captured in Northern Gaoyuan that day.

Seven battles had broken out in different locations, and after claiming seven victories, the army had advanced without hesitation.

“After that, we killed or captured every one we came across.”

Hundreds of crows flew through the sky, while corpses that seemed to number ten times as many lay scattered across the ground below.

By the time the Seven-Route Army’s horses came to a stop, five major mounted-bandit groups had been annihilated, and more than ten others had surrendered.

“Effectively, we had already achieved our objective.”

“I believe there’s more to the story.”

“Ah. You mean the nomads?”

“You got it.”

Thanks to their rapid mobile strikes, the Seven-Route Army had suffered few casualties. But the successive battles had left them thoroughly exhausted.

That was when thousands of nomads appeared amid a massive cloud of dust.

“To be honest, even I felt dizzy when I saw them.”

There were thousands of them, and every single one was a master of mounted combat.

No matter how seasoned a Peak master Wipeng was, he had no way to turn the tide of battle by himself.

“That was when the matter I reported earlier by messenger pigeon took place.”

“You mean the people who called themselves khans?”

The great nomadic empire that had once ruled even the Central Plains had long since become a distant memory. But the conquerors’ bloodline had not been severed, and neither had the title of khan.

“There were two of them. They came forward first and introduced themselves…”

“Temur and Chinggen, descendants of the Great Khan and members of the Golden Clan.[^1]”

“Exactly.”

Wipeng nodded.

The young chieftains of the steppe had arrived with two thousand riders each. They were neither aggressive nor arrogant.

Instead, they cautiously attempted to converse in halting Han language.

“Is there anyone among you from the Jin Family of Taiyuan?”

The battle that everyone had expected never took place.

All because of the name of the Fire King, Jeok Cheongang.

“The rumor had already reached Gaoyuan. They knew about the relationship between Great Hero Jeok and the Third Young Master, and they said they didn’t want to become enemies with us.”

“That’s what I’m curious about. It seems suspicious to say they withdrew after hearing only the Fire King’s reputation.”

“Ah, that? I found it rather unsettling myself, so I beat the information out of the mounted-bandit prisoners we captured.”

Wipeng grinned as he continued.

“They had been taught a lesson the previous winter. Great Hero Jeok killed two notorious mounted-bandit leaders from Gaoyuan—Black Sand and the Human Butcher—with a single palm strike. The two of them were there as well.”

“They were frightened.”

“On the other hand, it helped them, too. After their leaders died, the mounted-bandit remnants fell into chaos, and Temur and Chinggen absorbed them. That’s how they grew this powerful.”

Temur and Chinggen had been lucky.

Black Sand and the Human Butcher had died in the same place, and not long afterward, even the Heavenly Wind Band had been annihilated by Jeok Cheongang. A power vacuum had formed.

After swallowing up the mounted-bandit remnants and gathering the scattered nomads, the two men had rapidly emerged as powers in Gaoyuan in the span of only a year.

“They said they wanted to be friends from now on. They even loaded us down with furs and gold and silver treasures they’d plundered.”

“What? Ha-ha-ha!”

Jin Wikyung burst into delighted laughter.

The outcome could not have been better.

The campaign had strengthened the Jin Family of Taiyuan’s fame and position in the Shanxi Murim, while also winning it the support of the affiliated sects and the common people.

“You’ve worked hard. You deserve great credit.”

“I don’t know about that, but I do know that my cup is empty.”

“Ha-ha! Let’s drink until we’re completely drunk tonight.”

The two men took turns filling each other’s cups as they talked.

An enormous number of things had happened over the past year, so they had plenty to discuss.

“Oh, right. What happened to the Seongun Escort Bureau?”

“We finished dealing with it completely right after you left. Though I suppose we should call it the Jin Family Escort Bureau now.”

Woo Hwangtae, chief of the Seongun Escort Bureau, had fled with his family, taking only a paltry sum of money. It had been discovered that they had bribed several officials and secretly diverted military supplies.

Prince Shangshan, Zhu Bao, an ardent admirer of Jin Taekyung, had of course provided considerable help during the process.

“Our cooperation with the other sects is progressing smoothly as well. An escort caravan traveling through Mount Song to Hefei is already under way.”

“Mount Song and Hefei…?”

“Shaolin and Namgung. There was no reason to reject such a good offer.”

Shaolin, the Mount Tai and Northern Dipper of the world’s Murim, and the Nangong Family, counted among the foremost of the Five Great Families.

They were so large that Jin Wikyung would have been satisfied merely to open trade relations with them. Instead, they had been the ones to propose a deal first—and on extremely generous terms, at that.

“The presence of Great Hero Jeok has been a tremendous help to our family.”

At Wipeng’s words, Jin Wikyung merely smiled.

He firmly believed that in the Murim, at least, no favor came without a price.

Their goodwill contained the price of two people.

One was the Fire King, Jeok Cheongang.

The other was the value of Jin Taekyung, a Sleeping Dragon.

*Come to think of it, it’s already been a year since our youngest left.*

It had been a year filled with countless hardships and events.

Once the ground thawed, the Star-Array Grand Banquet would be held in Henan. The brothers would meet again there.

*Are you staying safe?*

Just as Jin Wikyung was raising his cup while thinking about his thoughtless youngest brother, who had not contacted him even once, Wipeng suddenly spoke.

“By the way, what were you planning to paint this time?”

“I wonder.”

“You were grinding ink without even deciding what to paint?”

“It happens from time to time. There are many occasions when I grind ink for one or two shichen before putting everything away again.”

“Huh. Are you really trying to become a master painter now?”

“Put that thought aside for now. But once this painting is complete, I think I’d be happy to be called a master painter.”

“Didn’t you just say you hadn’t decided what to paint?”

“It’s merely that I can’t easily visualize what it will look like. I decided on the title long ago.”

“Then what is the title of this magnificent work?”

Jin Wikyung answered with a smile.

“The Sleeping Dragon Enters Service.”

* * *

He was a young man in shabby clothes.

His long, loose hair reached his shoulder blades, and his chin and philtrum were covered in thick stubble.

The final touch was the iron balls dangling from all four limbs, making him look like a convict at a forced-labor camp.

But there was one thing that set him apart.

His eyes.

The young man stared at the blue-white flame with a gaze so deep its bottom could not be seen, then muttered,

“Ah. This would be the perfect place to grill some meat.”

And then—

Fwoosh! Smack!

With a savage crack of displaced air, a wrinkled palm struck the young man on the back of the head.

“What an insolent brat! How dare you think of grilling meat over our sect’s sacred flame!”

The old man was furious. The young man grumbled.

“Ah, why not? It seems like it’d be fine if I just put it in for a second and pulled it right back out.”

“What did you say?”

“You’ve never heard of kiln-roasted pork belly? It’s insanely good.”

“You—you’re dead today!”

Smack! Crash!

On a day in early spring, when the earth had thawed and fresh sprouts were poking their heads aboveground, peaceful Mount Jiuhua began to grow noisy.

[^1]: The Golden Clan is a traditional name for the ruling lineage descended from the khans.
## Chapter artifact 237

# Chapter 237

Jeok Cheongang shouted at the top of his lungs.

“You’re a disgrace to our sect!”

“No, I’m not.”

“What do you mean, you’re not? In all the hundreds of years of the Fire Gate Clan’s history, there has never been a bastard who wanted to grill meat over the sacred flame!”

“I wasn’t talking about that.”

“What?”

“I’m not a formal Disciple yet. So I’m not a disgrace to the Fire Gate Clan, either.”

“……”

His face turned bright red, as though it might burst at any moment.

Before he could shout even louder, I quickly slung my pack over my shoulder.

“If there’s nothing else to pack, let’s get out of here.”

“Y-you little…”

Jeok Cheongang’s fist trembled, but soon he let out a deep sigh.

This wasn’t the first or second time something like this had happened over the past year. Even the famously short-tempered Fire King had reached the point where he simply took it in stride.

*Ah, I’m so proud.*

I had actually managed to beat the Fire King at something. Somehow, it felt like I had accomplished something incredible.

After glaring at me as I grinned foolishly, he turned toward the seventeen ancestral urns and performed a deep bow.

“Your unworthy Disciple, Jeok Cheongang, will take his leave. Until then, please remain in good health.”

“Shouldn’t it be ‘attain Buddhahood’?”

“……And here, before the seventeen Sect Leaders who came before us, I swear that I will turn that bastard into a proper human being.”

After firmly renewing his resolve in front of the seventeen former Sect Leaders, Jeok Cheongang rose to his feet.

“Come, let’s go, you beast.”

“Wait a moment.”

I slowly looked around the enormous cavern.

This was the place where I had spent a year. There had been times when the pain was enough to make me think I would die, and there had been joyful moments, too. There were even times when I had been so sick of it that I wanted to smash through the stone gate and run outside immediately.

But when had it happened?

Everything had gradually become familiar, and the happy days had begun to outnumber the painful ones.

The tremendous heat pouring from the blue-white flame now felt warm and cozy, like home.

“What are you thinking about so intently?”

“Just…”

What was I supposed to call it?

After a moment’s thought, one sentence slipped out.

“I was thinking that meat would taste really good if you grilled it over that.”

“You insolent little—!”

Avoiding Jeok Cheongang as he went berserk, I placed my hand against the stone gate. At the same time, I released the internal energy in my dantian, and the tightly sealed door slowly opened.

> **System**
>
> - **Scorching Sun Divine Arts** internal energy detected.
>
> - You may freely enter and exit **Fire Gate Cavern**!

*Yes. Take care.*

*Thanks for everything over the past year.*

*And…*

*Your unworthy Disciple, Jin Taekyung, will take his leave.*

I ran like the wind toward the wide-open cavern entrance. The iron balls dangling from all four of my limbs whipped around like pinwheels.

* * *

Mount Jiuhua had been famous since ancient times for its spiritual energy.

With good energy filling the entire mountain, it was only natural for spiritual herbs such as ginseng and He Shou Wu to grow there. To herbalists, the mountain was no different from a gold mine.

“You just wait. Today, I’ll find at least one for sure.”

At the foot of Mount Jiuhua, a middle-aged herbalist with the surname Hong pulled the strings of his straw sandals tight.

He had traveled a long way from Sichuan in pursuit of a big haul, but he had spent more than fifteen days finding nothing but disappointment.

“Damn it. What happened to all the spiritual herbs? It’s like every last one of them has vanished…”

The herbalists who had come with him had already given up and gone home. They had searched everywhere from the foot of Mount Jiuhua to halfway up the mountain without finding a single ginseng root.

There might have been a chance higher up, but something more terrifying than any wild beast lived there.

*The Fire King.*

Even martial artists who killed people as casually as eating trembled at the mere mention of his name.

Hong had once heard that the Fire King had single-handedly torn apart and killed a thousand vicious fiends of the terrifying Demonic Cult.

When he had asked how such a thing could be possible, he had been told that the Fire King was a three-headed, six-armed monster.

*But I heard there’s no problem going as far as halfway up the mountain. Don’t be scared, Hong. There are eight mouths you have to feed.*

To cover the cost of coming this far, his wife had even been forced to sell the silver ring she had received as a wedding gift. How could he face her if he went home empty-handed now?

Smack! Smack!

The herbalist slapped his cheeks to steel his resolve, then began climbing the mountain.

And before even two shichen had passed,[^1] he encountered the strangest sight he had ever seen.

“So what is samgyeopsal?”[^2]

“You don’t know what pork belly is? Is it called something else here?”

“No, you impudent brat. Just where are you from that you keep going on about names?”

“I’m from Korea! Do you know kimchi?”

“…You’re becoming more insane by the day. Is there something wrong with your Fire Gate Divine Technique?”

A wild-haired freak and a tiny old man were walking down the mountain path while having an incomprehensible conversation.

The combination itself was strange enough, but as they drew closer, a series of thunderous noises reached the herbalist’s ears, and his eyes widened.

Clank. Rattle. Boom! Rattle-rattle. Boom!

*W-what in the world is that?*

The source of the heavy noises was the iron balls connected by chains to the freak’s limbs.

The smaller ones were as large as a child’s head, while the larger ones were big enough to fit inside a basket.

With dozens of such vicious objects dangling from his body, the herbalist had no choice but to be shocked.

*What am I looking at?*

The herbalist stared blankly at the sight, then suddenly jolted.

Two pairs of eyes had drawn close enough to stare directly into his face.

Up close, the freak had a thick beard, while the old man’s face was covered in patches and too many wrinkles to count.

“Gyaaaah!”

As the herbalist nearly suffered a fit, the tiny old man spoke to him.

“Hey.”

“Y-yes?”

“Where are you headed?”

“I-I’m on my way to dig up medicinal herbs.”

The herbalist barely managed to squeeze out his voice.

He didn’t know why, but he had a strong feeling that something terrible would happen if he failed to answer.

The old man looked him up and down, then clicked his tongue.

“You’ve wasted your time. Don’t suffer for nothing. Go home.”

“W-wasted my time?”

Even though he was terrified, the herbalist instantly snapped to attention.

Go home? If he returned empty-handed, he would be wasting nearly two months of his life.

With the heavy load on his shoulders, that was absolutely unacceptable.

*This old man is no ordinary person.*

Not only was his appearance unusual, but his manner of speaking made it sound as though he could see through everything in the world.

As the thought flashed through his mind like lightning, the herbalist collapsed to his knees.

“Please help me just this once!”

“Good heavens, what’s gotten into you? What could this old man possibly help with?”

“No! You’re the Mountain Spirit! You know everything, don’t you?”

Bafflement spread across the old man’s face.

“……What spirit?”

“Mountain Spiriiit!”

The freak beside him grabbed his stomach and burst out laughing.

“Puhahaha! He thinks you’re a Mountain Spirit. Old Master, wasn’t it three months ago that you forgot your formula while circulating your qi and almost became a ghost?”

Wham! Craaack!

The freak had been laughing until his voice nearly burst, but one punch from the old man sent him flying dozens of *jang* away, where he crashed into the ground.

The herbalist’s faith only grew stronger.

*The Mountain Spirit has subdued an evil spirit!*

It was true that the white-haired old man inspired far more confidence than the freak dressed in rags. The herbalist begged again.

“Mountain Spirit! Please help me just once!”

“Mountain Spirit, my ass. And this old man can’t do anything for you, either. I’ve already pulled them all up, so what do you expect me to do?”

“P-pulled them up? Who pulled up all the spiritual herbs on Mount Jiuhua?”

“Now you’re finally making sense.”

“W-who would do such a thing…?”

The old man clasped his hands behind his back and gazed toward the distant mountain.

“My, what fine weather.”

“……”

“What are you staring at? Whoever pulls them up first gets to keep them.”

A look of despair crossed the herbalist’s face. Only then did he realize that the old man in front of him was no immortal.

“Then are you an herbalist too, Elder?”

“Hm? Well, I was for a few days. Digging up medicinal herbs is rather difficult.”

“You pull people’s heads off easily enough.”

The evil spirit—or rather, the freak—had returned and casually joined the conversation while dusting off his clothes.

His manner and tone were so nonchalant that the massive trees that had been snapped apart behind him might as well not have been there.

“My ancestors always said that feeding spiritual herbs to a Disciple was pointless. They were absolutely right.”

“Buurp.”

“You fucking—!”

A dreadful pressure flowed from the old man’s clenched fist. At last, the herbalist understood the identities of the two men.

“M-m-martial artists!”

“If you understand that much, give up and go home. And be careful not to spread unnecessary rumors.”

The freak also offered his advice with a serious expression.

“Especially don’t go any higher. They say a monster named Fire King Jeok Cheongang lives up there. If he catches you, he’ll chew you up, tear you apart, savor you, and enjoy you alive before killing you.”

“……”

“……”

It was horrifying even to imagine. The herbalist shuddered as he pictured his own gruesome death.

Seeing that the old man reacted similarly, he decided that this Fire King Jeok Cheongang had to be the three-headed, six-armed monster he had heard about.

“Understood? Be sure to remember what I told you.”

“Y-yes, I understand.”

That was the only answer the herbalist could give.

He had already been beaten to the herbs, and the people in front of him were martial artists. If he annoyed them for no reason, his head might be sent flying.

It was at that moment, when he lowered his shoulders and stepped aside to let the two men pass, that the freak spoke.

“Oh, wait a moment. Sir, would you like to take this, if you don’t mind?”

The freak rummaged through his pack and suddenly held out a ginseng root about three finger joints long.

The unexpected kindness left the herbalist trembling as he asked,

“W-why are you giving this to me?”

“If you go home like this, you won’t have anything to show for it. Judging by your age, you probably have a family to support, too. Where are you from?”

“I-I’m from Sichuan Province.”

“Sichuan Province is fun, isn’t it? I used to play it all the time during evening self-study.[^3]”

“Pardon?”

“No, never mind. Anyway, you came a long way, so use this to help cover your travel expenses.”

The old man, who had been silently watching the scene, clicked his tongue.

“You little fool. You give him something worth only a few coins, then act like you’ve made some grand gesture. If a man is going to be generous, he should give generously.”

“Come on, this is all I have left. What else could I do?”

“You call that ginseng? At least exchange it for silver.”

“How?”

“The value of an object is determined by people.”

“Oh. So that’s one way to do it.”

What a bizarre conversation.

As the herbalist looked back and forth between the two men, feeling as though he had been bewitched, the freak suddenly shouted at the top of his lungs.

“Anyone want to buy some ginseng?”

It was still early dawn. As the cold wind blew, the trees shuddered.

Then, from below on the mountain path, several dozen men appeared in orderly ranks.

Blue martial uniforms and sword sheaths hung from their waists. At a glance, it was obvious that every one of them was a highly trained martial artist.

“Guh!”

Unlike the herbalist, whose mouth fell open, the two men remained calm. The freak gently waved the ginseng root worth three silver nyang and said,

“I’ll sell it for a hundred silver nyang.”

What a highway robber.

The herbalist swallowed the words rising to his throat. At that moment, the middle-aged man at the head of the group spoke.

“I’ll buy it.”

“……”

The shock did not end there. A second later, the old man let out a long yawn and casually added,

“Three hundred silver nyang. You’re the richest man in Anhui, so you can pay that much.”

The middle-aged man bowed deeply.

“That’s a bargain for the price of offending the Fire King. I’ll buy it.”

The freak grinned and asked,

“Then, sir, may I ask your name?”

“Namgung Ryong.”

The middle-aged man raised his head. Authority that could belong only to a leader flashed in his deep-set eyes.

“I’m the Family Head of the Nangong Family.”

[^1]: A *shichen* is a traditional time unit of approximately two hours.

[^2]: *Samgyeopsal* is Korean grilled pork belly, traditionally cut into three visible layers of meat and fat.

[^3]: In Korean, “Sichuan Province” (*Sacheonseong*) is also the name of a tile-matching game; *yaja* refers to school-supervised evening self-study.
## Chapter artifact 238

# Chapter 238

The Nangong Family.

It was one of the Five Great Families that ruled the Murim alongside the Nine Sects and One Gang.

They supposedly had more than a hundred blood relatives, and when their subordinate martial artists were included, their numbers reached into the thousands.

Perhaps that was why their estate was incomparable to the Jin Family of Taiyuan, even in sheer size.

“Wow.”

How many times larger was it? Five times? Ten?

The guest room we had been shown was spacious and lavish, as though meant to prove the wealth and authority of the family.

Jeok Cheongang watched me gape in admiration as though I were pathetic.

“Is this your first time visiting the Nangong Family?”

“……Of course it is.”

“Ah, right.”

It wasn’t as though the Nangong Family were some neighborhood convenience store.

Normally, I would have made at least one more sarcastic remark, but not today.

I knew that Jeok Cheongang and the Nangong Family were not on particularly pleasant terms.

*Because that bastard Jopil left a pile of shit behind when he went.*

When a student did something wrong, the school called his parents.

The Nangong Family was indisputably a great power of the Murim and the hegemon of Anhui.

There was no way they could avoid having ties with Jeok Cheongang, who had taken a murderer who had brutally killed dozens of commoners in Anhui as his Disciple.

*Then again, that’s probably why he came along without resisting.*

I remembered something I had heard at an inn in Shanxi Province and asked,

“He was the Azure Sky Sword King, right? The person who came looking for you back then.”

“That’s right. He was the one who first informed me of that fact, and he was also the one who later granted my request. I owe him a great debt.”

On the day Jeok Cheongang had been unable to bring himself to kill Jopil and let him go, if the Nangong Family had intervened, Jopil would never have made it out of Anhui alive.

The person Jeok Cheongang had gone to see at the time was the Grand Family Head of the Nangong Family, the Azure Sky Sword King.

“What kind of person is he?”

“I have only met him twice, but…… the Sword King I know is truly a man who is crazy about swords.”

“Oh. A sword nut.”

“A sword nut?”

“It’s a term for someone who’s crazy about swords. It’s a compliment, so let it go.”

“There’s no trusting anything you say.”

He was pretty sharp.

Jeok Cheongang glared at me suspiciously, then continued.

“In any case, there is no doubt that he is an unpredictable man. He wanted to spar with this old man in exchange for sparing Jangcheon, that child.”

“A spar?”

“Can you guess what kind of man he is now?”

“I get the picture.”

A horrific series of murders had taken place in Anhui, yet the Grand Family Head of the Nangong Family, the hegemon of the province, had let the culprit go.

Setting aside the victims’ grievances, it could not have been a welcome outcome for the Nangong Family, either.

People would whisper that one of the Five Great Families was incompetent.

*He really is a sword nut.*

They said that Supreme Peak masters repeatedly trained without end to gain even the smallest enlightenment.

I had never met the Azure Sky Sword King, but I suspected he was that kind of person.

That aside……

“Who won the spar?”

“The day after sparring with this old man, the Azure Sky Sword King entered seclusion.”

“Oh.”

“It was a difference of half a form.”

In other words, Jeok Cheongang had won by the narrowest of margins.

Even fights between Third Rate martial artists could be decided by the smallest detail. What would a battle between Supreme Peak masters be like? The outcome would be determined by a difference as thin as a single strand of silk.

“It happened more than twenty years ago, so he must be even stronger now. He was formidable even then, but I can no longer guarantee victory with any confidence.”

I stared silently at Jeok Cheongang’s solemn expression.

Even he, a man who possessed earth-shaking martial arts, was only human.

I had realized that several times during the year we spent together in Fire Gate Cavern, and we had grown closer because of it.

*The infirmities of old age.*

A curse brought by time that even a Supreme Peak master could not overcome.

Fortunately, a stroke of heavenly luck had eased his symptoms. But it had only slowed the wheel already in motion, not stopped it completely.

Guessing at Jeok Cheongang’s feelings, I put on my brightest expression and spoke.

“Come on, don’t worry too much. We didn’t come here to fight. We were simply invited to the Sword King’s birthday celebration.”

“Do you truly think that?”

“Hm?”

“Didn’t this old man tell you? He is crazy about swords.”

“……!”

A thought suddenly flashed through my mind.

People who were crazy about something did not look around them. They immersed themselves in it—literally, *madly*—solely to satisfy their own desires.

Alcohol, gambling, drugs…… martial arts were no different.

It had been none other than the Azure Sky Sword King who released Jopil so that he could spar with Jeok Cheongang.

“Now that I think about it, the timing is perfect.”

“He must have been waiting.”

“So his birthday is just an excuse?”

“The Azure Sky Sword King is the sort of man who could change the day of his birth hundreds of times. I suspect the only day that matters to him is the day his breath stops. He will have no choice but to put down his sword then.”

“……”

What the hell? That was terrifying.

At this point, the bastard really was completely insane about swords.

I was rubbing my gooseflesh-covered arms when a delicate woman’s voice came from outside the door.

“The Family Head wishes to meet Young Hero Jin.”

* * *

Clank, boom. Clank, boom.

The chains clashed, and the iron balls gouged deep into the ground, leaving long tracks behind them.

I glanced back and saw a line drawn through every part of the estate I had passed.

*Is this Hansel and Gretel?*

If the siblings in the fairy tale had possessed something like this, they would never have gotten lost.

Even if they did get lost, there would have been no need to worry. I imagined Hansel strangling the witch with a Ten-Thousand-Year Cold Iron chain while Gretel smashed the back of her head with an iron ball, then shook my head.

“Ugh, no. That’s not it.”

“Young Hero Jin?”

At the maid’s stare, which seemed to regard me as though I were insane, I waved my hand.

“No, it’s nothing. Let’s keep going.”

“No, that’s not what I meant……”

“Yes?”

“I-I beg your pardon, but the things you’re carrying are rather……”

“Ah.”

The maid’s finger was pointing at my iron balls.

Apparently, I had done quite a number on someone else’s courtyard.

Several sturdy servants had gathered by then, filling in the marks I had left with dirt while wearing gloomy expressions.

“I’m sorry. I’ll just carry them in, then.”

Clank.

I gathered the chains and lifted the iron balls.

I had weighed them regularly during the first few months, but after that, I gave up. If they got heavier, then I supposed they got heavier.

*They must weigh a hell of a lot by now.*

In any case, there was no way I could cross the grounds of the Nangong Family like that without attracting attention.

To other people, I probably looked like a fruit seller carrying dozens of watermelons.

Every time I moved, murmuring voices pierced my ears.

“Who is that guy? Did you hear anything?”

“No idea. With iron balls chained to him, he looks like a prisoner.”

“Can you really say he’s chained to them?”

“……I suppose not.”

“To begin with, no one could carry that many iron balls of that size. They must be weapons with only an iron shell.”

“What on earth does that man do? From his appearance, he’s a beggar among beggars. At that level, he’d be an Elder in the Beggars’ Sect.”

“He doesn’t have any knots, so maybe not……”

Listening to the Nangong martial artists quietly argue among themselves, I thought,

*You fucking bastards.*

A beggar among beggars? An Elder of the Beggars’ Sect?

That year in Fire Gate Cavern had been a literal scorching hell.

If a sauna was dangerous to pregnant women and the elderly, Fire Gate Cavern was simply dangerous to human beings.

I had made puddles out of my sweat, and every breath had felt as though my lungs were burning away.

*I’d even deliberately endured it without using Logout.*

After going so long without washing, it had become such a habit that I could no longer tell whether I smelled or whether insects were crawling over my body.

*I should’ve washed as soon as we arrived.*

If we had gone to the inn first, I could have soaked in hot water, but everything had gone wrong when we came straight to the Nangong Family.

Jeok Cheongang had been speaking so seriously about the Azure Sky Sword King. I couldn’t exactly have told him I was going to scrub off some dirt first.

“You bastards try it yourselves…… It’s not like you’re going to scrub my back.”

The maid’s steps quickened after I muttered that. It was definitely my imagination.

A short while later, I arrived at a pavilion surrounded by tight security.

The Nangong Family’s guards, each with the two characters **azure heaven** embroidered across his chest, blocked my way.

“Are you Young Hero Jin Taekyung of the Jin Family of Taiyuan?”

I concealed my surprise and nodded.

There were ten guards. They ranged in age from their twenties to their forties, and every last one of them was a Peak master.

Good heavens. They were using ten Peak masters merely to guard a pavilion.

*Is this why people call them one of the Five Great Families?*

For the first time, I could truly feel the power and status of the Nangong Family.

Perhaps he noticed my reaction, because one of the guards who looked the youngest let out a quiet laugh and spoke.

“Disarm yourself.”

I suppressed my surprise and answered.

“Disarm myself? I don’t have any weapons on me.”

“Then what do you call the things in your hands?”

“Oh.”

Right. I had these.

If even a ballpoint pen could kill someone, the iron balls I was carrying certainly qualified as weapons.

To me, they were merely heavy clothes I had to wear, but other people saw them differently.

The problem was……

“I’m sorry, but I’m still training. I can’t just take them off whenever I want.”

“Training?”

“Yes.”

It wasn’t a lie. I had become so accustomed to them that I could no longer find any reason to remove the iron balls.

But the young guard looked thoroughly displeased.

“It can’t be helped. Rules are rules.”

“Well, then, I can’t help it either.”

Clank.

I deliberately raised my hands and feet one after another.

Shackles were fastened tightly around all four limbs, and unusually gleaming chains connected them to the iron balls.

“These can’t be removed without a key.”

“Who has the key?”

“Of course, the Ol—no, my Master has it.”

“Your Master would be……”

A year had passed since Jeok Cheongang had publicly declared me his Disciple.

Even a servant would know that much. There was no way a Peak master could be unaware of it.

No matter how vast the continent was, the Fire King Jeok Cheongang was one of the few Supreme Peak masters in the entire world, and everything he did attracted attention.

“Hmm.”

The young guard furrowed his brow deeply as he looked back and forth between me and the iron balls. Then he abruptly spoke.

“We’ll have to cut them off.”

“What?”

No, what the hell had he just said?

Even when I gave him an incredulous look, the young guard remained completely confident.

“The Nangong Family has its own laws. Great Hero Jeok will understand.”

“……Uh, I’m not sure he’ll understand that.”

A phrase Jeok Cheongang had repeated like a habit in Fire Gate Cavern suddenly came to mind.

*“This old man entered the Fire Gate Clan at the age of nine. If we assume that one hundred people began learning martial arts at that age…… I’m the only one among them who became as strong as I am now. So how did this old man come this far?”*

*“How?”*

*“I shoved aside bastards from the unorthodox factions, sent dark-path figures packing, and killed every bastard who set fires like a Demonic Cultist. In that spirit, add a hundred geun to the iron balls.”*

A history of blood and violence.

Even the Roaring Fury Swordsman, the Senior Brother of the Zhongnan Sect’s Sect Leader, had been beaten black and blue. I could only imagine what would happen to this young guard.

I gave him my most sincere advice.

“Do that and you’ll die. Seriously, you’ll be in real trouble.”

“……What did you say?”

“I mean, you won’t die by my hand.”

“How dare you—!”

The young guard shouted angrily and placed his hand on his sword hilt.

That was when a deep, resonant voice infused with internal energy reached everyone’s ears.

“Enough. Let him in.”

Namgung Ryong, Family Head of the Nangong Family.
## Chapter artifact 239

# Chapter 239

Namgung Ryong was a middle-aged man with a sharp, intimidating air.

As befitted the Family Head of the venerable martial household known as the Nangong Family, his dignified bearing radiated authority. His lips were pressed into a firm straight line, revealing the sort of personality he possessed.

In fact, despite traveling with him all the way from Mount Jiuhua to Hefei, I had heard him say fewer than ten words.

“Would you wait a moment? There’s one important matter left to attend to.”

As the Family Head of the Nangong Family, he must have had a considerable workload.

I was used to this from watching Jin Wikyung, so I nodded without complaint.

“Ah, yes.”

Crunch!

*Oh, right. I forgot about the iron balls.*

Unable to bear their weight, the chair had been smashed to pieces beneath me. I remained seated on the debris and glanced at Namgung Ryong.

“Oops, what happened here? We should make the chairs a little sturdier…”

“It’s made of ebony imported from Nanman.[^1] The wood is harder than steel.”

“……”

“Just stand.”

A short while later, Namgung Ryong set down the bamboo slips he had been examining carefully and spoke.

“I invited a guest and gave him such poor treatment. You have my apology.”

“No, it’s fine. You may have been busy.”

“In addition, I owe you an apology for the discourtesy committed by my son.”

“What are you talking about…?”

“I believe I heard some commotion.”

I suddenly remembered the young guard who had aggressively demanded that I disarm myself.

*I wondered why the youngest one was acting so cocky…*

“You’re his father?”

“He’s my only child, so I raised him with great care. Perhaps because of that, he still has many shortcomings.”

*Yeah, he definitely has shortcomings.*

Thinking of that bastard’s unpleasant expression, I nodded.

“It’s all right. I’m sure he’ll improve with time.”

“……”

“Was there something else you wanted to say?”

“Ahem. No, nothing.”

After clearing his throat, Namgung Ryong continued.

“People around him kept filling his head with talk of his talent for martial arts. You’ve heard the title Sword Dragon, haven’t you?”

“The Sword Dragon?”

“So you have heard of him. Well, it would be impossible not to…”

“I’ve never heard of him before.”

“Oh.”

“That’s a cool title, though.”

“Is it…?”

A dark shadow passed over Namgung Ryong’s face.

“He is well known throughout the martial world as one of the Ten Dragons and Phoenixes.”

“Oh, so he’s one of the Ten Dragons and Phoenixes. My second elder brother is one of them too.”

“I heard the two of them got into quite a fight as soon as they entered Heaven’s Gate Temple.”

“Good grief. They were young—very young. If they had just enrolled, they would have been twenty. That’s the age when people act like that.”

“……”

“It’s all right. People that age grow up by beating each other black and blue. But the reason you called me here was…?”

This man was definitely more of a doting fool than he looked.

Namgung Ryong had been momentarily at a loss for words after my swift interruption, but finally parted his lips.

“It concerns Great Hero Jeok.”

“That old—no, you mean my Master?”

“That’s right.”

He nodded heavily before continuing.

“I’ll be direct. I want you to dissuade Great Hero Jeok.”

The relaxed muscles around my waist tensed on their own. I ran a hand over the beard that had grown thickly over the past year and asked,

“Is this about his duel with the Azure Sky Sword King… Great Hero Nangong Cheon?”

“That’s right. Do you know what happened between Great Hero Jeok and my father more than twenty years ago?”

“I know roughly what happened. I also know that my Master won.”

“It was a razor-thin difference. It was a battle so close that it would not have been strange for either of them to lose or win.”

Namgung Ryong sighed.

“My father must have been deeply resentful of that defeat. For several years afterward, he devoted himself to secluded training, stewing over it.”

Defeat always cut deep.

And if the person in question was one of the greatest masters in the world—someone who loved martial arts enough to be called a sword nut—the sense of loss would only grow in proportion.

*If his own son is talking about it like this, he must have been really pissed.*

This was a fight between Supreme Peak masters. Its intensity went without saying, and in the worst case, it could even lead to bloodshed.

If they had planned to calmly exchange a few moves, laugh good-naturedly, and withdraw, Namgung Ryong would have had no reason to bring this up.

The problem was…

“I’m not confident I could persuade my Master, either. No, I can’t persuade him.”

The Fire King, Jeok Cheongang, was not the sort of man who would retreat just because someone tried to stop him.

The year I spent in Fire Gate Cavern had taught me and shown me many things. Not only about martial arts, but also about the personality of the person beside me.

Jeok Cheongang was a man whose character was impossible to mistake.

“He’d rather die than back down.”

“You misunderstand me. I’m not saying you should stop them as much as possible. I’m saying you must stop them.”

Namgung Ryong stared at me.

“Do you know what will happen if something happens to either of them during this duel?”

“I can make a rough guess.”

The Fire King and the Sword King. Both were giants who ruled over the martial world.

If the worst happened, the aftermath would be like a meteor crashing into the shore of a quiet lake.

“Then you shouldn’t have brought us to the Nangong Family.”

“That…”

“I know. You had no choice. But if even the Family Head can’t persuade his father, what could I possibly do?”

I shook my head. Whatever else I said here would be meaningless anyway.

“I’ll at least try talking to him.”

“I’ll do my best as well. I should go see my father immediately.”

“I’m not sure that’ll do you any good…”

“What do you mean?”

“Nothing. Then I’ll be going.”

I gave the puzzled Namgung Ryong a polite bow and turned around.

As soon as I left the pavilion, I found the young guard—or rather, the Lesser Family Head of the Nangong Family, Sword Dragon Namgung Ok—waiting for me with a fierce glare.

“You bastard!”

“Oh, what now? When have we ever met for you to keep calling me bastard?”

“I heard everything from outside. How dare you treat my father with such disrespect? Do you think the great Nangong Family is a joke?”

“What disrespect? I showed him the utmost courtesy, just as I do my Master.”

“What kind of bullshit are you spouting?”

“I’m serious. If you’re really curious, ask my Master. Anyway, I’m leaving.”

I was just about to drag the iron balls past Namgung Ok when—

“How dare you!”

Shing! Click!

It happened in an instant.

The blade, radiating a frigid sharpness, had not even been drawn halfway before it vanished back into its scabbard.

Namgung Ok stared at my hand, which was pressing down on his sword hilt.

“H-how did you…?”

“That isn’t something you can draw and swing so casually. Keep doing that and you’ll wind up dead.”

“……!”

“Act like a gentleman, young friend.”

Pat, pat.

I patted the shoulder of the man who had gone rigid as a stone statue, then approached the wide-eyed maidservant.

“Excuse me.”

“Y-yes?”

“Is there a mountain nearby where few people go?”

“Why would you want to…?”

“Just because.”

I glanced at the clear sky and continued.

“I thought I’d get some air.”

* * *

I shook off the maidservant, who insisted on coming with me, and began walking up the mountain path.

It was the height of spring. The mountain was green, and the sky was blue.

I walked past drifting scraps of cloud and birds chattering from the branches. After some time, I entered a broad clearing and suddenly stopped.

“You can come out now.”

Everything was exactly as it had been. The leaves rippling in the breeze, sparrows crying as they turned their heads back and forth without rest, and unfamiliar wildflowers blooming in full.

Yet an incongruous presence stood tall amid the natural scenery.

Then a voice wormed its way into my ears.

“Not bad. Not bad at all.”

He was a very tall old man. The fingers stroking his beard, which reached down to his chest, were knobby with protruding joints. His eyes were sunken, but a fierce light shone from within them.

I clasped my hands before the old man, who looked remarkably similar to Namgung Ryong.

“It is an honor to meet the Azure Sky Sword King, Great Hero Nangong Cheon.”

The Azure Sky Sword King Nangong Cheon—the Grand Family Head of the Nangong Family and one of the Ten Kings—stared at me before abruptly speaking.

“There must be a reason you called this old man all the way here.”

“What do you mean…?”

“Great Hero Jeok took a sly little bastard as his Disciple in his later years. I know exactly what you’re scheming, so there’s no need to pretend otherwise.”

“Ah, I’m sorry if I offended you.”

I scratched the back of my head and grinned. It was embarrassing to have him cut straight to the point like that, but it also made things easier.

“Did I make it a little… too obvious?”

I had first noticed his presence in the Family Head’s pavilion.

Namgung Ryong had not realized it, but I had. The reason I had come up to the mountain under the pretense of getting some fresh air was the Azure Sky Sword King.

An unspoken invitation and acceptance had passed between us.

“Hah.”

A breathy sound escaped the Azure Sky Sword King’s lips. His expression seemed to say, *What kind of brat is this?*

“You’re an audacious one. No, perhaps you simply have no fear?”

“My Master says I’m just being arrogant.”

“Yes, I believe that is the right word. Arrogant… It has been so long since I felt that way about someone that I had forgotten the sensation.”

“Exactly. Who would dare act arrogantly toward the Azure Sky Sword King?”

“No one has appeared in the past several decades. Not until you came along today.”

His fierce eyes fixed on me. That alone made my body hair stand on end and my senses draw taut.

“Speak. Why did you call this old man here?”

I took a deep breath. Then, without hesitation, I threw myself facedown before the Azure Sky Sword King and bowed.

Clank.

The chains collided, spewing a cacophonous rattle.

“What are you doing?”

“Please reconsider your duel with my Master.”

“Reconsider? Why should this old man do that?”

“I cannot tell you the reason.”

“……What?”

I had no idea what expression the Azure Sky Sword King was making at that moment.

But judging by the prickling sensation in the back of my head, as if I were being stabbed by a blade, he was clearly debating whether or not to kill me.

*It does sound insane.*

He had trained for twenty years for today’s duel.

And now some young brat who looked young enough to be his grandson had suddenly appeared and asked him to cancel it. On top of that, I was telling him I could not explain why.

But the die had already been cast. Pressing my face into the fresh earth, I spoke again.

“I’m sorry. But I cannot tell you the reason.”

“Tell me.”

“I cannot tell you.”

“You bastard!”

Whoooosh!

A powerful wave of qi swept through the surroundings. Trees snapped, and flowers that had only just managed to bear fruit were torn out by the roots.

“This is the last time I’ll ask.”

My answer had already been decided.

“I cannot tell you.”

When I repeated the same answer like a parrot, a tangible killing intent pressed down on my entire body.

After a brief silence, I heard the Azure Sky Sword King speak.

“Get up.”

Crumble.

When I rose, clumps of dirt poured from my clothes. The Azure Sky Sword King’s voice was as dry as grains of sand in the desert.

“I waited twenty years.”

“Then please wait one more year.”

I continued calmly.

“I cannot tell you the exact reason, but my Master is not in good condition right now. You did not wait twenty years just to obtain a victory like that, did you?”

“A victory like that…?”

The Azure Sky Sword King muttered the words under his breath and let out a hollow laugh.

“Great Hero Jeok trained his Disciple well.”

“He’ll be happy to hear that.”

“But you have the look of someone destined to die young. To survive in the martial world, one needs at least a minimum degree of etiquette.”

“That…”

“Three moves. If you can withstand this old man’s three moves, I will grant your request.”

Ding.

> **System**
>
> - A Sudden Quest, **Three-Move Kill**, has been generated!
>
> - Would you like to accept the Quest?

I looked into his eyes, which boiled like lava.

These were none other than three moves from the Azure Sky Sword King. Three strikes capable of cleaving mountains and splitting rivers would soon rain down upon me.

I opened my parched lips.

“I’ll do it.”

Ding.

As the System notification announced that the Quest had been accepted, anger rose in the Azure Sky Sword King’s eyes.

“The recklessness you’re showing now will kill you.”

“Maybe it will. Maybe it won’t. But before that…”

I grinned and raised my arms.

Clank.

Dozens of iron balls swayed together with the chains.

“May I take these off?”

“Go ahead. The outcome will not change.”

Along with his cold, stern gaze, the dignity of an emperor capable of forcing all under heaven to their knees surged from the old man’s entire body.

The blue sky spread above our heads began to churn.

“Emperor’s Sword Form. Can you stop it?”

Craaack! Clang!

I tore apart the steel shackles that had bound my limbs for more than a year as easily as sheets of paper.

The instant the chains and iron balls fell to the ground—

Whoosh!

A flash of light burst from the Azure Sky Sword King’s waist.

[^1]: Nanman is a historical Chinese term—often translated as “Southern Barbarians”—for peoples and territories south of the traditional Chinese heartland.

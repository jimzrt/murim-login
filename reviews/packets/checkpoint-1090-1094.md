# Checkpoint Review — 1090–1094

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

# Chapters 1090–1094

## Plot

A frost-covered Beggars’ Sect disciple reaches Xining with the Blood Lord’s threat to destroy the city, then dies. Nearly thirty disciples remained across Qinghai Lake; the messenger was the only one to return. Jin Taekyung identifies Blizzard’s traces on him. As Dark Heaven’s army arrives and shakes the city, Taekyung admits his fear of failing the civilians. Jeok Cheongang tells him that facing fear and caring about others’ pain make someone a hero.

Taekyung, Jeok, and the Slaughter Saint leap from the wall to confront the Blood Lord. Taekyung recognizes that the Blood Lord remains stronger, but is no longer beyond his reach. The Blood Lord’s monstrous strength comes with an abnormally enlarged, stitched-looking arm, which he credits to “his grace.” He knocks White Flame from Taekyung’s hands and wounds him, but Taekyung keeps fighting. The Bow Saint supports him with an arrow; Jeok and the Slaughter Saint engage the Black Ghosts, while Jeok’s full-strength Flame-Extinguishing Divine Fist turns hundreds to ash. The Grand Mage survives behind an immense ice wall and vows to kill Jeok for that person.

Cheongpung, Cheongheoja, Perfected Being Hyeoncheon, the Slaughter Saint, and the Bow Saint join Taekyung against the Blood Lord. Taekyung senses a second encirclement: about a dozen Black Ghosts and the Grand Mage. He fears the clash could end in mutual destruction or worse. The Blood Lord believes the Lord of Heaven wants Taekyung kept alive, though he wants permission to kill him. He breaks free from Taekyung and vows to kill him as a distant horn sounds.

## Continuity

- Dark Heaven’s army has arrived at Xining under the Blood Lord. The Grand Mage is with the army; her Blizzard spell carried the forces across Qinghai Lake.
- Jin Taekyung, supported by the Bow Saint, is fighting the Blood Lord. Taekyung is wounded and was disarmed, but continues to resist an opponent who remains stronger.
- Cheongpung, Cheongheoja, Perfected Being Hyeoncheon, the Slaughter Saint, and the Bow Saint have joined Taekyung against the Blood Lord.
- The Slaughter Saint and Jeok Cheongang fought the Black Ghosts. They can rise again after apparently fatal injuries. The Grand Mage survived Jeok’s attack behind an ice wall; their confrontation remains unresolved.
- About a dozen Black Ghosts and the Grand Mage encircle the allied fighters. The Blood Lord has broken free from Taekyung; a horn sounds in the distance, with its meaning unresolved.
- The Blood Lord interprets the Lord of Heaven’s wishes as prioritizing Taekyung’s safety above that of his loyal servants. This is the Blood Lord’s belief, not confirmed fact.
- The black-robed captive in Qinghai remains unidentified; what he knows is unresolved.

## Translation Decisions

- Keep Blizzard as the Grand Mage’s large-scale ice spell; distinguish “magic formations” from “Moving Formation(s).”
- Keep Blood Lord distinct from Blood-Sword Demon Lord; retain Grand Mage for 대술사.
- Render Jeok Cheongang’s address 노야 as “Old Master.”
- Render 나려타곤 as “Narye tagon,” retaining its humiliating implication of rolling on the ground like a lazy donkey.
- Render 생강시 as “living jiangshi”; retain “Black Ghosts” for 흑귀.
- Keep the Blood Lord’s belief about the Lord of Heaven’s priorities framed as his interpretation, not confirmed fact.

## Durable state

{
  "active_continuity": [
    "Dark Heaven's army has arrived at Xining under the Blood Lord.",
    "Jin Taekyung and the Blood Lord are fighting; the Blood Lord is stronger, but Taekyung continues to resist.",
    "The Bow Saint is supporting Taekyung; Cheongpung, Cheongheoja, Perfected Being Hyeoncheon, and the Slaughter Saint have joined them.",
    "About a dozen Black Ghosts and the Grand Mage encircle the allied fighters.",
    "The Blood Lord believes the Lord of Heaven wants Taekyung kept alive, though he wants to kill him.",
    "A horn sounds in the distance during the standoff."
  ],
  "continuity_sources": [
    1094
  ],
  "open_questions": [
    "Who is the black-robed captive in Qinghai, and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "What will happen in the confrontation at Xining, and what does the distant horn signal?"
  ],
  "safe_through": 1094,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1090

# Chapter 1090

Qinghai was unquestionably a border region.

It had one of the largest areas in the world and some of the most beautiful scenery, but in truth, its supplies were scarce and its population was nowhere near that of the Central Plains.

So whenever people compared Qinghai to the Central Plains—which had stood at the center of the world for thousands of years and developed a wide range of culture and civilization—Qinghai’s people liked to joke:

“Qinghai and the Central Plains have only three things in common: they see the same sun, they’re connected by the same river—the Yellow River—and, last of all, they have beggars.”

Beggars were common everywhere, after all.

They lived along busy main roads, in dark, filthy alleys, or in shantytowns near streams. They could be found in the Central Plains or the border regions without distinction.

There were so many of them, in fact, that people joked the Beggars’ Sect could found a nation of its own if it took in every beggar in the world.

But around daybreak, as a scouting party searched the area through the faint morning mist, they came across a white-haired beggar whose appearance was unlike anything anyone had ever seen.

No—he was so strange that their hair stood on end.

Step. Step.

His staggered footsteps made him look ready to collapse at any moment. His eyes were empty, as if his soul had left his body.

And then…

“Deliver this message. No matter who survives.”

A voice filled with terror slipped between his blue lips.

Perhaps that was why the scouts, frozen like statues for an instant, noticed the two knots tied at the beggar’s waist only too late.

“……The Beggars’ Sect.”

There was no mistaking it. The beggar before them was a martial artist of the Beggars’ Sect.

And a two-knot disciple, just one rank below a Branch Master.

As far as they knew, there was only one reason a Beggars’ Sect disciple would appear here, a hundred li west of Xining, where the scouts had set out from.

“Old man, what on earth happened at Qinghai Lake—”

At that moment, one scout hurriedly dismounted and rushed toward him. Then he sucked in a breath and stared.

Only then did he see.

In the faint mist, the Beggars’ Sect disciple’s hair had looked white from age. In truth, it was frozen stiff, like someone trapped in a glacier.

And his face, pale as snow, belonged not to an old man but to a young one.

“W-what is this…”

Was this what it felt like to have a bolt of lightning strike through the crown of your head?

The twenty scouts could only fall silent, a tingling sensation running down their spines.

They didn’t even realize that the Beggars’ Sect disciple’s next words were the last spark of his life, delivered with every ounce of strength he had left.

“Deliver this message. I’m coming. I’ll go there and kill and burn everything in Xining.”

“……!”

“……!”

For an instant, the scouts trembled, their eyes wide with shock.

Was it the terrifying killing intent behind those words?

No. They had it wrong.

The Beggars’ Sect disciple was smiling. And crying at the same time.

As if imitating whoever had ordered him to deliver that message.

As if grieving the deaths of the comrades who had already become the dead.

Then, in the suffocating silence pressing down around them, the Beggars’ Sect disciple’s body tilted with a faint murmur, his difficult journey finally at an end.

“Just wait. I, the Blood Lord, have returned—”

Thud.

His body crumpled like a rotten log.

The scouts stared blankly at the body of the Beggars’ Sect disciple, his breath finally gone. Then, all at once, they lifted their heads and looked west.

Why?

Was it the fear that had already taken root in their hearts, or the instinctive sense of those who had realized what they were about to face?

Beyond the thick mist, they could almost hear the shrieks and smell the stench of hideous monsters.

“……Take care of the body.”

Even the commander’s voice, strained out with difficulty, couldn’t hide his fear.

“We’re going back to Xining. Right now.”

* * *

The office of the Qinghai City Lord, now a headless corpse, was as impossibly spacious and luxurious as ever.

As if to prove why he had been doomed to die.

The table, carved from expensive ebony, was large enough for dozens of people to sit around at once. He had even used Shu brocade—considered the finest quality in Sichuan—to keep the sunlight out.

But the Qinghai Governor could never have known that those gaudy luxuries he’d been reluctant to part with until the moment of his death were now being used for a shabby beggar.

“Living in this kind of luxury when you’re only a two-knot disciple. He forgot what it means to be a beggar.”

Gung Gibang muttered, doing his best to sound calm.

The corpse lay atop the ebony table, wrapped in Shu brocade. Gung Gibang stared at it with eyes glistening with tears.

“I didn’t know him for that long, but he was a decent kid. He was still young, and already talented enough to be granted the second knot.”

I didn’t answer.

Neither did anyone else among the leaders gathered in the office.

“He asked me if he could visit the Central Plains someday, once things got better. I snapped at him and told him not to say such childish things.……Damn it.”

Gung Gibang swore in a hollow voice, then managed a bitter smile.

“What can you do? He and the others were just unlucky.”

Nearly thirty Beggars’ Sect disciples had been left on the other side of Qinghai Lake. Only one young, nameless disciple had made it back to Xining.

And even he had died along the way.

He’d been in such a wretched state that the scouts who found him first could barely get their words out.

But his final words, which might as well have been a will, contained information more valuable than this entire goddamn lavish office.

“Blood Lord. If it’s the Blood Lord…”

The Sect Leader of the Kunlun Sect, Cheongheoja, suddenly spoke. I nodded.

“It’s the same name you know, Sect Leader. The one who caused the Shaolin Bloodshed.”

“……!”

“……!”

An invisible ripple spread through the room.

Those who had already known the Blood Lord’s name only murmured in silence. Those who knew nothing of the details stared in shock.

And the Fire King, Jeok Cheongang, was among a rare few who belonged to neither group.

“It’s been a long time since I heard that name.”

His voice was quiet, and his expression barely changed.

But I knew better than anyone.

How furious Jeok Cheongang was right now.

And how hard he was fighting to hold that fury back.

“Now I can hold my head up in front of that damned monk.”

Hong Dao was the Abbot of Shaolin Temple, hailed as a pillar of the Murim and respected enough to earn the title of Dharma King. Jeok Cheongang had always called him “that damned monk.”

He was one of the very few friends Jeok Cheongang had ever had. Maybe the only one.

That was why he could never have forgotten, not for a single moment.

His grudge against the man who had killed Hong Dao: the Blood Lord.

But there was a more pressing matter than his grudge.

“So they’re planning to throw everything they have into this after all.”

A young Daoist spoke in a voice so calm it almost sounded cold. Hak Eui, Cheongheoja’s second Disciple, continued,

“They went to the trouble of releasing a Beggars’ Sect disciple they’d already captured. That must mean they’re certain of their victory.”

“S-second Junior Brother.”

Hak Su, his Senior Brother, had been watching the room uneasily and tried to stop him. Hak Eui paid him no mind.

He’d gained a measure of influence after the last meeting about the Qinghai Governor.

“But it’s unfortunate that we weren’t given the most important information. If we’d known even the enemy’s numbers, we could have come up with a much better plan—”

That was when Gung Gibang’s brow furrowed.

He’d been staring at the corpse in silence until then.

“What?”

He turned on Hak Eui, his anger plain.

“What did you just say?”

Hak Eui replied evenly to Gung Gibang’s glare.

“I was only expressing my thoughts. I regret that we didn’t receive more information.”

“So what? Are you blaming the man who risked his life for everyone and died? Asking why he didn’t try harder?”

“That’s…”

Hak Eui was about to respond to Gung Gibang, whose emotions were running high, when someone who had been watching quietly suddenly spoke up.

“Second Disciple.”

It was none other than his Master, Cheongheoja.

Hak Eui paused at the quiet call, then bowed his head to Gung Gibang.

“I spoke carelessly because I was inexperienced. I hope there won’t be any further misunderstanding.”

His stiff apology showed little feeling. Gung Gibang’s expression grew even more hostile, but Cheongheoja spoke again.

“I failed to raise my Disciple properly. I offer my sincere apology.”

It was no small thing for someone else to apologize on his behalf—especially a much more senior figure, and the Sect Leader of the Kunlun Sect.

And there were others present who outranked him, too.

No matter that Gung Gibang was the Beggars’ Sect Successor Beggar; taking the argument any further here could be considered a grave act of disrespect.

I watched Gung Gibang bite his lip, then glanced at Hak Eui. At just the right moment, I sent Gung Gibang a Sound Transmission.

*—Let it go. For now.*

“……!”

*—Or I can beat that socially maladjusted bastard half to death right now. Just say which you’d prefer.*

At last, Gung Gibang gave a bitter smile and shook his head.

“Understood. I’m sorry for disrupting the mood, too.”

That brought the brief commotion to an end. Hak Eui spoke again, without the slightest sign of having been cowed.

“Fortunately, we still have time before the enemy reaches Xining. We should come up with adequate defenses before then.”

There was something odd about his tone.

I’d been watching him all along with a somber gaze. Now I couldn’t help asking,

“What defenses?”

“You already know, Great Hero Jin.”

Of course I did. I knew all too well.

That was why it surprised me even more.

That Hak Eui, heir to the Kunlun Sect’s Daoist lineage, had come up with that idea.

“It’s not too late to leave, even now. We should abandon this place before our rear is completely cut off.”

“Junior Brother, what are you saying?”

But even when Hak Su finally sprang to his feet, unable to hold back any longer, and his Master, Cheongheoja, murmured in dismay, Hak Eui didn’t stop.

“This isn’t a battle. It’s a war. I know it’s wrong to say this, but… we can’t make the mistake of grasping at something small and losing everything.”

“……!”

“……!”

The air inside the room froze in an instant. Then I spoke.

“First off, there’s so much bullshit here that it’s hard to know where to start. But let’s get one thing straight.”

I added quietly, looking at Hak Eui, whose face had gone rigid.

“Does the Blood Lord look like a pushover to you?”

I pointed straight at the table.

More precisely, at the corpse of the Beggars’ Sect disciple, lying there with frost on patches of his body.

I’d known from the moment I first saw him.

That terrible cold lingering in places on his dead body. I recognized the familiar traces, the kind only I could notice.

*Blizzard.*

A top-tier ice spell with devastating power.

It meant two things.

First, just as I’d expected, the Grand Mage was with them.

And second—

“They’ve already crossed Qinghai Lake.”

They wouldn’t have needed any boats. They could just cross the lake, frozen solid by magic.

In the first place, the Blood Lord had released the Beggars’ Sect disciple only for his own amusement.

“So.”

I added quietly, looking at Hak Eui, who was wearing an inscrutable expression.

“If you want to run, go now. You cowardly bastard.”

And at that moment—

Grnk. Grnnnk.

A rumble came from somewhere, and the office began to shake.

No—the whole of Xining.
## Chapter artifact 1091

# Chapter 1091

Xining, the capital of Qinghai, was a city built on a vast plateau.

Tributaries of the Yellow River, which flowed east and west all the way to the Central Plains, ran through the region. Mountains large and small surrounded it on every side, giving it scenery beautiful enough to draw gasps from anyone who saw it.

But at that moment, not one of the countless people crowding Xining’s high walls could think the view before them was beautiful.

It wasn’t merely that they failed to see its beauty. They couldn’t.

The sight of a mountain that should have stood tall and still, as always, now in motion was enough to freeze the spine.

Rrrk. Rrrrk.

A tremendous rumble unlike anything they had ever felt.

The city shook with it. So did the people, body and soul.

And at the end of all those gazes, filled with undisguised horror, was a pitch-black mountain drawing closer from the distance.

No—a force of enemies moving as one, like a mountain.

Dark Heaven.

At last, they had come.

Fiends from beyond the desert, come to blacken the blue sky and the green earth alike.

* * *

The world had suddenly grown dark. I knew I wasn’t the only one who felt it.

Dark. In every direction.

Dark clouds hid the sun, and a chill that seemed to swallow the sunlight filled the space it left behind.

And—

At the center of it all, they stood.

Dark Heaven’s vast army, where monsters and humans mingled.

“……Benefactor.”

Cheongpung’s voice came from somewhere behind me on the wall. It was lower than usual, with the faintest tremor in it, but I didn’t answer.

More precisely, I couldn’t.

I, too, had been overwhelmed by the sight of the enemy filling the horizon beyond the wall as they advanced.

I couldn’t let anyone find out. Not ever.

I might have been able to fool the whole world, but there was one person I couldn’t fool.

*—Are you afraid?*

At Jeok Cheongang’s Sound Transmission in my ear, I quietly bit my lip.

*Yes. I am.*

At this moment, I was terrified enough to shudder.

I was terrified that their strength was far greater than I’d merely guessed up until now. That, the moment I saw what they truly were, my instincts had made me think of the word defeat.

Squeeze.

I felt a warm sensation in my fist, clenched so tightly I hadn’t even realized it. I tightened it further, keeping the beads of blood from slipping between my fingers, and answered.

*—Yes. I’m afraid.*

*—What are you so afraid of?*

*—I’m most afraid of myself—of how I’ve shrunk back, even after making up my mind and preparing myself for this. And of what will happen because of it.*

I wouldn’t say I wasn’t afraid of dying.

That would be denying the person I’d been all this time, fighting tooth and nail just to survive. It would be a laughable lie.

But there was something I feared far more: the hundreds of thousands of lives behind the wall I stood on, vanishing.

Because of my own bad decision. No one else’s.

Jeok Cheongang saw right through me.

*—Yes. That’s the difference between you and this old man.*

Before I could ask what he meant, his next Sound Transmission reached my ear.

*—I’ve never once pursued some grand cause in my life. I simply went where my feet took me, where the wind blew. So the deaths of strangers I’d never met didn’t trouble me much.*

People saw Jeok Cheongang as the foremost of the Ten Kings, one of the towering figures representing the orthodox faction. But in truth, he was different.

He was a free man.

Like the Sect Leaders of the Fire Gate Clan before him, he belonged to none of the orthodox, unorthodox, or demonic factions. He had walked only his own path.

*—Maybe that’s why the title of Great Hero, which stuck to me like a label before I knew it, always felt like an ill-fitting suit.*

*—But you deserve to be called one.*

*—No. That’s wrong.*

Jeok Cheongang answered firmly and looked at me with deep, thoughtful eyes.

*—Only those who fear the pain of others, and know how to shed tears, deserve to be called Great Heroes. Just like you.*

*—……!*

*—But remember this one thing. If you don’t want to shed tears later, you have to overcome the fear right in front of you first.*

Then Jeok Cheongang added in a low voice,

*—Only then do you become a hero.*

A hero. A hero, huh.

I mouthed those two words in my mind. They had always felt so far away. Then I gave a bitter smile.

*—I never wanted any of that.*

*—It doesn’t matter. You don’t become a hero just because you want to. You earn the title when the world calls you one.*

*—Like how they call you a Great Hero, Old Master?*

*—What?*

*—You just said it yourself. You didn’t go out of your way to pursue some grand cause. You just went where your feet took you, where the wind blew—and before you knew it, people were calling you a Great Hero.*

*—……!*

Jeok Cheongang stared at me, eyes wide. Then he licked his lips.

*—You got me with that one.*

*—Let’s call it even.*

*—You haven’t lost your knack for running that mouth. Now you’re finally starting to feel like the little hellion I knew.*

Jeok Cheongang let out a quiet laugh and gestured with his chin toward the other side of the wall.

*—Well? Still afraid?*

*—Yes.*

I answered without hesitation, then added calmly,

*—But I won’t try to look away from that fear.*

Everyone carries some fear in a corner of their heart.

But only those who admit it and face it head-on can find the strength to stand up to it.

Just as I was now.

Rumble. Rrrumble!

The rumbling grew stronger by the moment, and the ground shook as if an earthquake had struck.

I felt the powerful vibrations climb through my whole body as they traveled up the tall, sturdy wall.

And at the same time, I saw him.

At the head of the enemy forces, so numerous I couldn’t begin to count them, one man was grinning as he looked straight at us.

*The Blood Lord.*

He looked quite different from the last time I’d seen him, but the moment I saw that crooked smile, I knew by instinct.

That thick, viscous killing intent and madness, so palpable it seemed like you’d get it on your hand if you touched him, outstripped even the Blood-Sword Demon Lord I’d taken down in Gansu.

And in the instant we recognized each other, his lips moved.

“Looking up at you is a pain in the neck. Why don’t you come down for a bit and say hello?”

His words rang out through the deafening rumble and clouds of dust. Jeok Cheongang, who had already been staring hard at the Blood Lord, had a reddish gleam in his eyes.

“My body was getting restless anyway. He’s doing me the favor of scratching the itch.”

Bow Saint immediately sensed the danger and tried to stop him.

“It’s goading you. Obvious as can be.”

At her expectant glance, the Slaughter Saint, who had appeared out of nowhere at some point and taken up a place on the wall, calmly nodded.

“Yeah, it’s crazy.”

Then, as Jeok Cheongang furrowed his brow, the Slaughter Saint added,

“But it’s not like anyone here is thinking straight.”

My expression solemn, I drew the obvious conclusion.

“Let’s do it now.”

“Right. It’s not like we’ll die or anything.”

Whoosh!

There wasn’t even time for anyone to stop us.

Reciting the number-one last words of men everywhere, the three of us sprang off the wall at the same time.

Behind us came the sharpest, loudest shout I’d ever heard from Bow Saint.

“I said don’t go!”

Uh.

Sorry.

* * *

The Blood Lord watched three figures plummet across the distant sky in an instant. Without thinking, he muttered,

“They’re crazy. They’re really coming?”

He’d only tossed out a casual remark. They’d traded a few words, and now the three of them were charging straight at him without the slightest hesitation.

“Like half-mad fighting dogs or something…”

The Blood Lord trailed off, considerably taken aback. Then the three men—now over thirty yards away, moving like flashes of light—spoke at once.

“You told us to come down, you son of a bitch.”

“You worthless bastard. You goddamn bastard. You piece of shit. You’re the kind of bastard I’d burn alive and still not be satisfied—”

“So you’re the Blood Lord I’ve heard about. I know this is a strange request for a first meeting, but would you mind calmly offering your neck and stepping aside?”

First came Jin Taekyung, whose curses had an oddly satisfying ring to them. Then Jeok Cheongang, hurling every obscenity he knew. And finally the Slaughter Saint, whom the Blood Lord was meeting for the first time.

For a moment, surprise had covered the Blood Lord’s anger. Now he felt it surge back to the surface.

“Are you done talking?”

At the Blood Lord’s low voice, Jin Taekyung hesitated briefly and glanced at the Slaughter Saint.

“Do you have anything else to say?”

“Probably not. We’ve only just met, so I don’t have much to say.”

The Slaughter Saint had already been remarkably rude for someone who’d just met him. Jin Taekyung nodded as if it were nothing, then answered the Blood Lord.

“He says he’s done.”

Crack.

The Blood Lord gritted his teeth and opened his mouth at that nonchalant response.

Or tried to.

Before he could, another wave of obscenities swept over him.

“I’ll grind every bone in your body to dust. I’ll toss your flesh to the Nanman Beast Palace to feed their beasts, and scatter your bones in the Shaolin Temple latrines, and—”

“Ah, this one isn’t done yet. Wait a bit. Honestly, aren’t you kind of curious what comes next?”

At that moment, the Blood Lord’s last thread of reason snapped. His vision went white.

“Hah!”

KWA-A-A!

A powerful wave of energy swept out in every direction.

The immense internal energy packed into that single shout made Dark Heaven’s army, which had seemed as though it would march on without end, and the people on the wall over three hundred yards away, all hold their breath.

But the three men closest to him, who felt the full force of that wave, were the exception.

Whoosh!

A single sharp gust cut through the dust that had billowed into the air.

At its center, Jin Taekyung had already brought his clear, almost transparent spearhead slashing down. He grinned.

Just as the Blood Lord had before they came down from the wall.

“Why are you getting so worked up? I’m just glad to see you after all this time.”

An explosion meant destruction, but it was also tied to erasure.

The Blood Lord had drawn his anger together and unleashed it all at once. Now he stared at Jin Taekyung with eyes gone cold.

“You’re just the same as before. That damned mouth of yours.”

At that moment, the smile on Jin Taekyung’s lips disappeared.

“This time will be different. Everything else will be.”
## Chapter artifact 1092

# Chapter 1092

To a martial artist, a wave of qi was the outward release of power.

That was why Jin Taekyung could feel it more clearly than ever.

Just how terrifyingly skilled the Blood Lord—his enemy standing right before him—was.

Rumble.

The air refused to settle under the influence of that powerful wave of qi.

But unlike the faint tremors reaching him from every direction, Jin Taekyung’s heart sank into an even calmer stillness.

Calm enough to answer evenly, even beneath the Blood Lord’s cold, burning voice and gaze.

“You’re just the same as before. That damned mouth of yours.”

Jin Taekyung’s smile faded. At the same time, he raised his beloved spear, which he had named White Flame, and pointed it at the Blood Lord.

“This time will be different. Everything else will be.”

“Different? Puhaha.”

This time, it was the Blood Lord’s turn to laugh. He stared at Jin Taekyung with a mocking gaze.

“I heard you went from Hidden Dragon to Divine Dragon, but now you act like you’ve gotten your hands on a dragon pearl, too. No matter how hard you struggle, you’re still no match for me. You know that yourself, don’t you?”

Contrary to the Blood Lord’s expectations, Jin Taekyung answered with an easy nod.

“Yeah. Probably.”

“What?”

“Why the reaction? Shouldn’t you be a little happy I admitted it so honestly?”

“……You.”

The Blood Lord’s voice was sinking into a low growl when Jin Taekyung spoke first.

“I knew as soon as I saw you. I couldn’t get an exact measure of your strength.”

Even stones rolling along the roadside came in all shapes and sizes. So why should a towering mountain reaching the clouds have no difference in height?

And because Jin Taekyung had climbed from the very bottom of the Murim to the peak of Supreme Peak, he’d understood the instant he stood face-to-face with the Blood Lord.

“You’re stronger than me. No question.”

He didn’t know exactly how wide the gap between them was.

But even if the gap was only one move—or half a move, Jin Taekyung accepted that the Blood Lord was the stronger one.

And with that, something suddenly came back to him.

His not-so-distant past, when he’d been no better than an ant, helpless beneath a power so immense it felt absolute.

The Blood Lord, who had seemed impossibly far away, like someone living above the clouds.

“But you know what?”

Jin Taekyung gazed at the Blood Lord as he asked quietly.

The past and present overlapped before his eyes. Along with the knowledge that the Blood Lord was stronger than him, another realization coursed down his spine like an electric current.

“Back then, no matter how hard I fought, I thought I wouldn’t even be able to touch a hair on your head…”

His voice trailed off, and Jin Taekyung smiled.

Only today had he finally realized it.

The Blood Lord in his memory, whose mere presence had left him short of breath, was no longer someone who lived above the clouds.

“Now it feels like I could reach you just by stretching out my hand.”

“……!”

The instant the Blood Lord’s eyes widened, Jin Taekyung’s figure, standing tall over thirty meters away, wavered like a mirage.

Fshh.

His shape remained, but his body was gone. There wasn’t even a trace of his presence, yet the killing intent within it was unmistakable.

Whooosh!

The Blood Lord heard the eerie sound as clearly as if the wind itself were howling.

And at the same time, he saw it.

In the space warped by immense pressure, a spearhead that had outpaced its own sound tore through the compressed air, propelled by Shifting Form and Position at its pinnacle.

“Jin Taekyung!”

And then—

KWA-A-A!

The Blood Lord’s furious shout and the muffled boom of a sonic blast rang out as a blood-red flash clashed with a dark-blue wave, swallowing the world around them.

* * *

One exchange.

A single exchange was enough.

Enough to realize the gap between the Blood Lord and me at that very moment.

KRRRACK!

The Blood Lord’s red saber swung like lightning and locked against White Flame’s spearhead. The resulting boom wasn’t the kind of sound weapons could make.

Neither was the shock wave that followed.

Rumble!

The hard ground cracked like a spiderweb. Everything crumbled to dust beneath my feet as they slid backward, unable to withstand the force.

“Dare to wag that tongue at me when this is all you’ve got?”

Beyond our crossed weapons, blood-red light flashed in his eyes as his voice seethed with fury.

Killing intent I could almost touch. A terrifyingly vast force.

*Strong.*

It was astonishing. At the same time, I realized something else.

The Blood Lord had grown stronger, too, over the past year—which could feel long or short, depending on how you looked at it.

*At least half a move above me. No—a full move.*

At the Supreme Peak level, a single move made an enormous difference.

But the reason I couldn’t help being surprised was that the Blood Lord’s strength couldn’t be measured by his martial enlightenment and internal energy alone.

Grnnnk.

The spearhead began to give way. Slowly—no, faster than that.

Beyond it was a red blade that flashed without any blood-red Force, and a muscular arm, bulging with veins as he squeezed out every ounce of strength.

*This is… not human strength.*

I could feel it by instinct.

I’d spent the past few years fighting monsters rather than humans. How could I not?

At that moment, the physical ability the Blood Lord was unleashing had gone far beyond human limits.

No—beyond even that.

Just looking at the skin exposed through the rips in his clothes was enough to guess what he’d been up to over the past year.

“Unusual, for a prosthetic arm.”

I put everything I had into holding back the immense force pressing in on me, and stared steadily at the Blood Lord.

More precisely, at his arm, swollen to an abnormal size, and the marks on it that looked as if it had been sewn together.

The Blood Lord bared his teeth and growled at me.

“Everything is thanks to his grace.”

During the Shaolin Bloodshed, the Blood Lord had lost an arm to the Sword Saint, Mae Jonghak, and fled.

The fact that he’d shown up in one piece with both arms, when he should have spent the rest of his life one-armed—and that he could wield this kind of strength—meant only one thing.

“Did you want to get stronger that badly? Enough to splice yourself together with a monster?”

“……!”

“Well, forget about me. To get revenge on the Sword Saint, you’d have had to tear something off and stick it on. Right?”

“……You.”

Had I hit a nerve with a single remark? Or had I just figured out what he was so easily?

The Blood Lord glared at me, eyes wide, then clenched his teeth.

“I look forward to seeing whether that mouth of yours can still run after you’re dead.”

At that moment—

Crack—KWA-AANG!

His arm swelled even larger, like the trunk of an old tree. With an immense force that could only belong to a monster, it knocked the spearhead skyward.

Clang!

Even my Strength stat, which had been in triple digits for a long time, couldn’t handle that force and internal energy. They sent the shaft spinning into the air.

My palm split open. In an instant, I was left empty-handed—and the Blood Lord’s red saber drew a dazzling arc toward me.

Whoosh! KWAANG!

Crude and brutal, but capable of breaking and shattering anything, the strike tore through the air like lightning, followed by another.

His saber swung after my feet as they moved without pause, the blood-red Force at its edge bending like a whip.

Whish—slice!

Every hair on my body stood on end. The Force skimmed past, slicing off a few strands of hair before slamming into the ground.

KWAANG! Rrrumble!

The earth shook like an earthquake, unable to withstand the tremendous force carried by the Force.

But even a thick cloud of dust spreading across a radius of hundreds of feet couldn’t block the Blood Lord’s view.

“That’s all! That’s all you’ve got!”

Whoosh!

The dust cloud split beneath a fierce sonic boom. I threw myself to the side on instinct, dodging the blood-red Force plunging down like an axe swung by some ancient giant.

Slice!

The ground split cleanly in two and opened a pitch-black maw.

I’d dodged the strike just in time, but even its backwash had left me covered in blood. The Blood Lord smirked when he saw me.

“Narye tagon.[^1] I’d heard you’d become the Divine Dragon while I was away, so I expected more. Instead, here’s a lazy donkey rolling around on the ground.”

Among martial artists—especially masters with pride to spare—Narye tagon was the height of humiliation.

After all, nobody who thought they were somebody in the martial world wanted to be seen rolling around covered in dirt.

But I didn’t care about any of that.

In low-level dungeons, I’d pressed myself against the damp cave floor because I was afraid of the poison darts fired by kobolds. When an enemy got too close for me to use my spear, I hadn’t hesitated to go for the eyes or head-butt them.

A character in some pirate manga that still hasn’t reached its ending once said that a scar on your back was a swordsman’s shame. I’ve never agreed with that for even a second.

“A wound on your back just fucking hurts. Shame’s something you can only feel while you’re alive.”

“What?”

My feet came to an abrupt stop.

The Blood Lord’s face seemed to ask what the hell I was going on about. I stood up, my body aching, and continued.

“I am talking nonsense, so stop staring at me like that. You’re so cute I want to bite you to death.”

“You little—!”

“And what the fuck does it matter whether I’m a dragon or a donkey? You’re the one who ripped off some monster’s limbs and stuck them onto yourself.”

“……!”

A heavy Patriot missile of a fact was what hurt the most.

Grind.

The Blood Lord clenched his teeth so hard they seemed about to break and started forward again.

Or tried to.

The killing intent thickened, and the blood-red Force stirred around his saber. Then a tremendous explosion rang out, jolting his long-paralyzed reason back to life.

KWA-AANG!

The source of the deafening boom that shook the world around us was behind him.

And the ones who filled the opening left by the Blood Lord, who had chased me for over three hundred meters while unleashing attack after attack, were none other than the two giants—the Fire King and the Slaughter Saint.

Crack—pboom!

Flames shot up all around us, and blood sprayed without pause.

Only then did the Blood Lord grasp what was happening. He shot me a blood-red glare, but I only shrugged.

“A goading strategy. Obvious as can be.”

“You—!”

“Oh, I’m not taking all the credit. Someone said something pretty similar a little while ago.”

At that moment—

Whoooosh!

From the city wall, now much closer, a streak of lightning plunged through the hazy cloud of dust.

KWA-A-AANG!

[^1]: Narye tagon is a humiliating martial arts term for rolling on the ground like a lazy donkey to evade an attack.
## Chapter artifact 1093

# Chapter 1093

KWA-A-A-ANG!

After the deafening boom, a tremor traveled through the ground. Jeok Cheongang turned to check what was happening behind him, then finally let out a sigh of relief.

*The old hag’s joined the fight.*

Even now, flashes of light streaked through the cloud of dust.

Once he confirmed that the Bow Saint was helping Jin Taekyung, a corner of his heart finally seemed to settle.

Now that the Bow Saint had joined them, his Disciple was safe.

At least for the brief time Jeok Cheongang needed to accomplish his goal.

*I was worried sick… Maybe there was nothing to worry about after all.*

In Jeok Cheongang’s judgment, Jin Taekyung still wasn’t a match for the Blood Lord. That was why he hadn’t been able to hide his unease, even after hearing the Sound Transmission that had reached his ear moments ago.

*“I’ll draw out the Blood Lord and buy us time. You two should target their main force.”*

*“What?”*

*“Don’t worry. You know my life motto, right?”*

Of course he knew.

No matter how long or short life was, survive at all costs and make it last.

But if everything in the world went according to one’s wishes, every martial artist in the land would be a Supreme Peak master, and the common people would live long, healthy lives.

So Jeok Cheongang had firmly opposed the idea.

No—he’d meant to oppose it.

Before Jeok Cheongang could even respond to that carefree answer, Jin Taekyung had already charged out without hesitation to face the Blood Lord.

*You idiot. You don’t even know enough to value your own life.*

And yet, contrary to what he was thinking, Jeok Cheongang had gradually found a smile on his lips.

It was such a clear smile that the Slaughter Saint, who was in the middle of stirring up a bloodstorm not far away, couldn’t hold back a comment.

“I know you adore your one and only Disciple, but are you really so eager to die that you—”

The Slaughter Saint stopped mid-sentence and sucked in a breath, his body twisting aside.

Whoosh-whoosh-whoosh!

Three streaks of sword light suddenly carved through the air, passing within inches of him.

At the same time, a flash of light glinted from the Slaughter Saint’s sleeve as he spun in midair.

KLANG! Thud!

Two sparks—and one sickening sound of flesh being pierced.

Three black-robed men, clad head to toe in pitch-black armor and charging at the Slaughter Saint like bolts of lightning, faltered and stepped back.

Or, more precisely, two of them did.

Thump.

One of the black-robed men fell like a dead tree.

A dagger the Slaughter Saint had just thrown was buried deep between the eyeholes of the helmet, which was pulled so low that not even the man’s face was visible.

“One down.”

The Slaughter Saint landed smoothly, as if nothing had happened. Jeok Cheongang, who had just swept away dozens of enemies with a flaming punch, shook his head.

“I don’t think so.”

“…What do you mean?”

“What do you think?”

Jeok Cheongang jerked his chin toward the fallen black-robed man.

“That.”

At that very moment—

Thrust.

The black-robed man, whom they’d thought dead, moved his own arm and pulled the dagger from his helmet.

Then he staggered to his feet and raised his sword.

As if he’d only been stung by a bee for a moment.

“…!”

The Slaughter Saint blinked silently. Jeok Cheongang shook his head.

It reminded him of the first time he’d laid eyes on that loathsome monster.

“Didn’t that brat Taekyung tell you? There are damned things that openly defy the natural order set by Heaven.”

Only then did the Slaughter Saint realize who the enemies before them were. He let out a low groan.

“…Black Ghosts.”

The Slaughter Saint had already heard about what happened in Gansu.

There were monsters that got back up no matter how many times you killed them, and every one of them had been fiends who once dominated the Demonic Cult.

“I heard they were like the legendary living jiangshi. So it was true.”

“Worse bastards than jiangshi. You can tell just by watching them move, can’t you?”

As he answered, Jeok Cheongang stood beside the Slaughter Saint and gathered his internal energy once more. The Black Ghosts, now six in number, were closing in as they took up positions all around them.

“How do you take them down?”

“As I understand it, there are only two ways. First, keep killing them until they die.”

Fwoosh.

White flames rolled over Jeok Cheongang’s hands.

In the space that seemed darker than it should have, the approaching Black Ghosts made strange noises, while the enemy forces packed tightly around them came into view. Deeper within that vast encirclement, so did the other figures hiding and controlling them.

“Second, cut off their heads and disable their arms and legs.”

And at that moment—

BOOM!

Jeok Cheongang threw out both palms with all his might.

As waves of rolling flame scattered in every direction, he kicked off the ground and shot forward.

“Defend!”

—GRAAAAAH!

The shouts of humans and monsters tangled together.

A path of fire opened through the enemies covering every direction. But the Black Ghosts stood their ground before Jeok Cheongang. A sharp gust of wind swept past their angled legs.

Whoosh. Slice!

The sword swinging toward Jeok Cheongang shot up into the air.

The Slaughter Saint, who had sliced through the arm of the first Black Ghost to charge, shouted with force.

“Go!”

It was a short cry, but its meaning was clear. Jeok Cheongang nodded slightly and pushed forward without slowing, drawing back a fist.

Rrrrrk.

At the heart of the space, now veiled in shimmering heat, the Flame-Extinguishing Divine Fist—mastered to its utmost—gathered white flame.

The heat made even the monstrous figure standing nearly thirty feet tall and the Dark Heaven faithful, who had formed a dense defensive line, open their eyes wide.

And in that world, where time seemed to stop for an instant—

“I am the—”

Jeok Cheongang’s fist shot forward, crushing the wind.

“Fire King!”

KWA-A-A-A-A!

Space warped. The ground sank.

Heat so enormous it was horrifying melted the flesh and bones of everything in its path. A flash so impossibly white it was hard to believe it was flame blocked his view.

Fwoosh—KRRRUMBLE!

With that momentary flash of light, Jeok Cheongang finally saw what lay before him and exhaled the breath he’d been holding.

Huu.

Heat poured between his trembling lips, like a weary fire dragon breathing flame.

But more than the exhaustion of pouring out all his strength, Jeok Cheongang felt the joy of having achieved what he wanted.

Sizzle. Szzzz.

The green ground was gone. All that remained was a hellscape spread between the scorched earth, black as a volcanic region, and a pale haze of steam.

Fsssh.

A hot wind blew from somewhere, and the bodies that had barely held their shape crumbled.

Monsters and humans alike. Even one unlucky Black Ghost who had stood directly in Jeok Cheongang’s path.

With a single strike, hundreds of enemies had turned to ash and scattered. The same had happened beyond the thick veil of steam, which now spread dozens of yards in every direction.

Or at least, that was what Jeok Cheongang thought.

Until he felt something strange suddenly reach his senses.

Ssshhh.

The moment he sensed an invisible force passing subtly through the ground and air, Jeok Cheongang immediately recognized what felt wrong.

*…This is.*

Maybe it was because he was briefly exhausted after using all his strength.

Looking back, things had seemed strange from the start.

How had such a thick, vast cloud of steam formed?

And why had the enemies beyond it shown no reaction at all?

*Cold qi.*

As the two words pierced his mind, Jeok Cheongang stamped down on the ground, which was slowly freezing over. He had already forgotten the horrifying heat from moments ago.

Crack.

A chill followed the tip of his foot.

At the same time, someone’s face came to mind.

Jeok Cheongang looked at the steam with a sunken gaze and parted his lips.

“Anyone with the slightest bit of manners would greet an elder properly. You’ve got less respect than an eyelash, you little brat.”

At that moment—

KRRRACK!

The steam blocking Jeok Cheongang’s way split apart.

No—it shattered in midair.

Beyond the chilling cold, an immense wall of ice revealed itself.

And with it, the person Jeok Cheongang had just thought of.

“You noticed. That’s just like you.”

At the Grand Mage’s reply, Jeok Cheongang spat.

“Yeah. I knew it was you.”

That had been his own full-strength strike.

It was more than enough to turn even the sorcerers hiding among the countless enemies into ash in an instant.

Even a Supreme Peak master comparable to him would have found it nearly impossible to completely block the damage.

Unless they had that bizarre sorcery Jin Taekyung called Magic.

“So that brat was right. You managed to stay alive.”

“An old man who should’ve long been dead and buried is still wandering around in perfect health. What’s one little thing like this?”

The Grand Mage continued, her face twisted in a sneer.

“If you’re that old, you should be resting in the back room, watching your grandchildren play. Why come all this way to play with fire?”

“If my one and only Disciple is putting on a show for me, I can play with fire a hundred times over. A thousand, even.”

“Don’t overdo it. You should think about your age.”

“Don’t worry. No matter how old I am, killing you is well within my reach.”

For an instant, the Grand Mage’s eyes sank deep behind her veil.

She could feel the certainty in Jeok Cheongang’s words.

Sizzle.

The ice wall, unable to fully withstand the heat of the Flame-Extinguishing Divine Fist, was still melting little by little. It only confirmed his claim.

*…Jeok Cheongang, the Fire King. So his reputation isn’t empty.*

Just as the Grand Mage thought this to herself and cautiously gathered her energy, Jeok Cheongang, who had been watching her and the three Black Ghosts guarding her with a sunken gaze, suddenly spoke.

“But today isn’t our only chance.”

In truth, Jeok Cheongang was just as pressed for time.

There wasn’t much time.

The Slaughter Saint was fighting desperately, surrounded by the six—or, now, five—Black Ghosts. And his Disciple, who absolutely could not be allowed to die, was fighting the Blood Lord.

The time they’d agreed on was up, and although it was a little short of what he’d wanted, they’d accomplished enough.

“Clear the way. Before I burn you all to ashes.”

Across the distance of dozens of yards, Jeok Cheongang’s reddish-hot gaze met the Grand Mage’s ice-cold one.

After a brief but long silence, the Grand Mage’s quiet voice rang out.

“For that person’s sake, I’ll kill you. Even if it isn’t today.”

“Got any more bullshit to say?”

Jeok Cheongang gave a quiet laugh at the Grand Mage’s silence, then swiftly turned around.
## Chapter artifact 1094

# Chapter 1094

Time was always absolute.

But the way its passage felt was entirely relative.

Especially for Jin Taekyung, who had been locked in a desperate exchange that seemed destined to go on forever, all within a brief span of barely half a quarter-hour.

Slice!

Feeling the scorching pain along his side, Jin Taekyung thought:

Was his body growing sluggish as one wound after another piled up? Or was the Blood Lord getting faster?

Or was it both?

But compared to what the Blood Lord was feeling at that very moment, Taekyung’s thoughts were nothing.

*What… the hell is this guy?*

The Blood Lord’s eyes, once blazing with rage and spattering streaks of crimson light, had sunk deep. Now they trembled faintly.

Three times.

This was the third time he’d met Jin Taekyung.

The first time, he’d merely watched from afar.

On the day the Jin Family of Taiyuan rose to become the preeminent clan of Shanxi Province, the young upstart who’d gone from a disgrace to the family to a Hidden Dragon had struck the Blood Lord as quite interesting.

At their second meeting a year later, he’d felt more than interest.

No, to be honest, he’d been surprised.

Chosen as the Fire King’s Disciple, Jin Taekyung had grown so strong he was almost unrecognizable. More than that, he was a young beast brimming with a venomous ferocity.

So the Blood Lord had crushed him.

Thoroughly.

Though the Sword Saint’s intervention had forced him to retreat in humiliation, facing Jin Taekyung had still been easy.

The Fire King’s teachings might have helped the young beast grow, but the gulf between them was like the distance between heaven and earth.

But now, another year later, the Blood Lord was confronted with a new emotion, beyond the interest and surprise he’d felt until now.

That emotion was none other than astonishment.

*…Why? Why won’t you fall?*

Of course, he knew the facts.

Four Demon Lords and Demon Empresses had met their ends at the hands of Jin Taekyung, who’d once been nothing more than a young upstart.

But he couldn’t understand it in his heart.

How could something like that happen?

How could Taekyung face him so unflinchingly, when the Blood Lord’s might had advanced even further than before?

“You!”

Crimson light surged once more over his sunken eyes. A larger, more powerful blade-force shot toward Jin Taekyung.

Whoosh—slice!

Cut strands of hair fluttered through the air. The pressure of the wind tore at the skin showing through his already-ragged clothes.

But that was all.

Jin Taekyung dodged the blade-force by barely a handspan and lunged forward without a care.

Pop.

His figure shot forward, erasing the distance between them.

At the same time, a flash like a beam of light burst from far away and streaked through the space over Taekyung’s shoulder.

A Force arrow—by now, one he’d grown sick of seeing.

*The Bow Saint…!*

The Blood Lord gritted his teeth and swung his red blade down.

KWA-ANG!

Force clashed with Force.

And through the chaos of that split-second opening, a palm wreathed in searing heat shot out.

Fwoosh!

The space around them wavered, and wisps of rising heat shimmered through his vision like a dream.

But the Blood Lord’s movements showed not a hint of hesitation.

“How dare you!”

His shout burst with internal energy as he reached out his remaining hand and seized the flames just before they reached him.

No—the palm strike Jin Taekyung had launched.

KRRK!

Hand met hand. Crimson Force and flame collided and twisted together.

With them came a terrible burning pain that would have made an ordinary person faint on the spot.

Sizzle.

The Bow Saint’s intervention had forced the Blood Lord’s counterattack half a beat late.

But even as his flesh burned, the Blood Lord didn’t so much as blink.

Instead, he growled at Jin Taekyung, whose attack had been stopped, his voice low and heavy.

As if making a vow to himself.

“Did you really think this would be enough to break me?”

He was well accustomed to pain.

He’d faced death—not just a few times, but dozens—and always risen again.

By the blessing his master had bestowed upon him. By his own Will.

“How dare a wretch like you—!”

Just then, Jin Taekyung spoke in a quiet voice.

“More precisely, ‘you lot.’ Not ‘you.’”

“What?”

The Blood Lord’s startled question escaped him before he realized it.

Whoooosh!

Powerful whooshes swept in from every direction.

The thick cloud of dust slowly dispersed. In its depths, blurry figures stirred, finally revealing themselves.

“Sorry I’m late, Benefactor.”

Cheongpung’s voice was unusually subdued. His eyes had turned a deep purple.

Over Cheongpung’s shoulder, two voices rang out, old yet clear. The qi of the Zaha Divine Technique enveloped his entire body.

“Infinite Life Buddha. It seems we’re only now meeting the unwelcome guest at our mountain.”

“So you’re the fiend who’s been causing all this trouble.”

Cheongheoja and Perfected Being Hyeoncheon.

With Cheongpung followed by the Sect Leaders of Kunlun and Kongtong, the Blood Lord’s brow twitched.

Though it was also because he’d spotted someone even more troubling.

*The Bow Saint.*

The woman silently aiming her great bow at him, without a hint of wavering, was no one the Blood Lord could afford to underestimate.

Especially not in a situation like this.

But that wasn’t the end of it.

“I had a dream one day. Some guy called Shakyamuni, or whatever the hell his name was, showed up and told me this.”

Step. Step.

Footsteps belatedly reached the Blood Lord’s ears. The master who’d returned to his one and only Disciple continued, his voice churning with fury.

“Hong Dao. He told me to burn the bastard who killed that monk to a crisp, without leaving so much as a hair.”

“I figured it had to be nonsense, coming from you. But I’ll believe you this once. I had a similar idea myself, though not quite the same.”

“It’s all true.”

“Sure, let’s say it is. Still, I doubt Shakyamuni went around calling people bastards.”

The Slaughter Saint had joined the encirclement, appearing like a ghost without the slightest warning. The Blood Lord suddenly felt as though he were surrounded by a mountain of sabers and a forest of swords.

Including Jin Taekyung before him, he now had to face no fewer than seven Supreme Peak masters.

Among them were members of the Three Saints and the foremost of the Ten Kings, a master fully their equal. This was no mere illusion.

“So this was what you were after?”

Crack.

A bone shifted in the Blood Lord’s hand, where their palms were locked together.

His hand, so badly charred it seemed certain to melt away at any moment, was forcing the flames back with an unbelievable rate of recovery.

Sizzle. Slither.

As his grip tightened, even while it alternately charred and healed, the Blood Lord let out a growl of laughter.

“But look around. Which of us is actually surrounded?”

Jin Taekyung didn’t answer.

No—more precisely, he couldn’t.

Just handling the Blood Lord’s internal energy pouring endlessly through their joined hands—and his inhuman strength—was already pushing him to his limit.

But Taekyung’s gaze, sunk deep, and his keen senses still took in every detail of what was happening around him.

Such as the other vast encirclement, stretching hundreds of yards in every direction.

And the figures at its head and center.

*Black Ghosts.*

It was them.

Beings reborn from the pit of death.

Death Knights cursed with something close to immortality.

In another world, they were called Death Knights. Jin Taekyung could sense their presence clearly.

There were a dozen or so of them, standing like an iron wall and exuding suffocating demonic qi. He could sense someone else behind them, too.

*The Grand Mage. No—the Grand Mage.*

He’d already expected it.

She wasn’t someone who would die that easily.

But no matter how far ahead he’d predicted things, that didn’t make reality any less grim.

*At this rate, we’ll all die together.*

No—Jin Taekyung had a feeling the outcome might be even worse than that.

As long as the Blood Lord and the Grand Mage were here, with greater martial might and supernatural abilities than they’d possessed during the Shaolin Bloodshed, no one could say what might happen even if they took down every Black Ghost.

And Jin Taekyung wasn’t the only one torn at this crossroads.

*Must I truly let this man live?*

The Blood Lord repeated the question in his heart, wanting to relay it to his master.

Of course, he knew.

The Lord of Heaven.

The master who deserved that title more than anyone in the world wanted that accursed man before him.

That was why, when he’d heard that four Demon Lords and Demon Empresses had died one after another, he’d mocked and cursed them instead.

Was it simply because they were weak?

Half right, half wrong.

The Blood Lord had cursed the dead because, contrary to their master’s command, they’d let Jin Taekyung come close to death again and again.

But…

*Now I understand why those bastards tried so hard to kill you.*

At this moment, the Blood Lord finally understood how they’d felt.

And at the same time, he understood even less.

Why his master wanted Jin Taekyung so badly, when he was an obstacle who kept interfering with Dark Heaven’s plans and was growing at a rate unprecedented throughout history.

Why the Lord of Heaven cared more for Jin Taekyung’s safety than for the loyal servants who’d always served him, willing to give their lives.

*Lord of Heaven. My one and only master. Please, tell this servant.*

Tell him to cut down this bright-yellow sprout now, before it was too late.

No—to kill Jin Taekyung, who had somehow already grown into a towering tree, by any means necessary.

The Blood Lord pleaded more desperately than ever.

But that was all.

His voice would never reach his master, and nothing would change.

Gritting his teeth, the Blood Lord wrenched his hand free with all the fury surging through him.

KWA-ANG!

Jin Taekyung was driven back ten steps with a thunderous boom. The Blood Lord spoke as if spitting out the words.

“There won’t be a next time. I’ll kill you. No matter what.”

And at that moment—

Bwoooooo!

A deep, resonant horn sounded in the distance, cutting straight through the taut tension.

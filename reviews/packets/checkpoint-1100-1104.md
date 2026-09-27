# Checkpoint Review — 1100–1104

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

# Chapters 1100–1104

## Plot

Dark Heaven and the Potala Palace assault Xining with ice, arrows, water spheres, and hulking monsters. The defenders repel the opening attacks, but Jin Taekyung’s assault on the enemy vanguard cannot stop Dark Heaven’s hundred-thousand-strong main force. As the siege presses across the gates, the Dalai Lama leads the Potala Palace’s army against Jeok Cheongang at the North Gate, and the Blood Lord receives a signal that allies are approaching by river.

At the western wall, Taekyung enters a No-self Trance while fighting. Cheongpung intercepts a blood-red attack aimed at him, and the blast breaches the wall. Cheongpung goes missing in the aftermath. As fighting continues at the breach, the Blood Lord confronts Taekyung. Taekyung is injured but standing; the Blood Lord absorbs blood from nearby corpses and attacks again. The chapter ends in a flash of red, with others beginning to rise behind Taekyung.

## Continuity

- Dark Heaven and the Potala Palace are attacking Xining; the western wall is breached, and fighting continues there.
- The Blood Lord fights Taekyung at the breach. He can command weapons from a distance and absorb blood from nearby corpses to gain vitality and strength.
- Taekyung is injured but still standing. The Lord of Heaven appears to want him above all else; the Blood Lord suspects this but attacks him anyway.
- Cheongpung intercepted the blood-red attack aimed at Taekyung and is missing after the blast breached the wall.
- The Dalai Lama and roughly ten thousand Potala Palace monks, including the Twelve Secret Monks, charged toward the North Gate to attack Jeok Cheongang.
- The Blood Lord received a signal that allies were approaching by river from the east; their identity remains unknown.
- The hidden Dark Heaven agent among Xining’s defenders remains unidentified. Cheongheoja’s favor to Taekyung remains undisclosed and unfulfilled.

## Translation Decisions

- Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective.
- Render 일당백 as “One Against a Hundred,” distinct from 일기당천, “One Against a Thousand.”
- Keep No-self distinct from Trance: No-self is the self-forgetting state; Trance describes Taekyung’s intense, dreamlike state.
- Render 天上天下, 萬魔仰伏 as “Heaven above and earth below; All demons bow!”

## Durable state

{
  "active_continuity": [
    "Dark Heaven and the Potala Palace are attacking Xining; fighting continues at the breached western wall.",
    "The Blood Lord has coordinated pressure across Xining’s gates; the siege is underway.",
    "The Blood Lord is fighting Jin Taekyung at the western breach and can command weapons and absorb blood to gain strength.",
    "The Lord of Heaven appears to want Jin Taekyung above all else; the Blood Lord suspects this but attacks Taekyung anyway.",
    "Taekyung is injured but still standing; others have begun to rise behind him."
  ],
  "continuity_sources": [
    1103,
    1104
  ],
  "open_questions": [
    "Why does the Lord of Heaven want Taekyung, and what does he intend to do with him?",
    "Who are the allies approaching by river from the east?",
    "Which of Cheongheoja’s Disciples is the hidden Dark Heaven agent, and what did Cheongheoja ask Taekyung to do?",
    "What happened to Cheongpung after he intercepted the attack?"
  ],
  "safe_through": 1104,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 1100

# Chapter 1100

Someone once said that people feel the greatest wonder and fear when they come face-to-face with the unknown.

When they encounter something they’ve never experienced before and see it for what it really is, every emotion races to its extreme.

And Jin Taekyung wholeheartedly agreed.

As he did with the saying left behind by a certain philosopher: Humans are creatures of learning.

*Whooosh!*

Hundreds of ice spikes shot through the curtain of rain amid a surging swell of enormous energy.

Yet even as a vast spell of considerable power took shape, Jin Taekyung didn’t flinch in the slightest.

He’d already expected it.

“Defend!”

The instant his shout, infused with deep reserves of internal energy, burst from between his lips—

*Shhk! Fwssh!*

A wave of shields covered the heads of his allies, who filled the lofty city wall without leaving a gap. At the same time, brilliant beams of light shot up from all around them, streaking toward the hundreds of ice spikes.

*Boom!*

A thunderous crash. A flash of light.

The ice spikes shattered by the Sword Energy scattered by the Peak masters ricocheted toward the city wall at high speed. But that was all.

*Clang! Clang!*

The massive rectangular shields, their outer surfaces clad in steel, did their job admirably.

Had the ice spikes retained their full strength, things might have been different. But after being weakened once, their shattered remnants weren’t enough to break through the firmly constructed wall of shields.

“Everyone’s safe!”

Reports came from all around, voices raised with excitement.

But Jin Taekyung—the one who’d predicted all this and made preparations beforehand—didn’t let his guard down for a moment.

They’d gotten the battle off to a good start. Successfully defending against magic, which in this world was little different from a supernatural miracle, had also lifted his allies’ morale. That was a major gain.

But Jin Taekyung knew better than anyone that this was only the beginning.

So did the Grand Mage and the Blood Lord, watching from beyond the city wall.

“Loose!”

At the forceful shout, the signalers on the wall waved their flags to pass along the command. Arrows that had gleamed from between the shields finally left their taut bowstrings.

*Whooosh!*

Thousands of arrows darkened part of the sky as they rained down.

They were meant to pierce the throats of the enemies advancing below—the merciless invaders.

But their desperate hopes vanished the moment the red lips concealed beyond a distant veil moved.

“O invisible veil.”

There’s an inexplicable power in human speech.

And a mage’s incantation gives that power substance.

*Fwoom.*

An invisible wall split the air, pressing through the space between one place and another.

It was a powerful protective spell, one that arrowheads of steel could never pierce.

*Crack!*

Thousands of arrowheads snapped or bounced away in an instant.

The people on the wall gasped as they witnessed the unbelievable sight. But the person who’d performed that astonishing miracle remained as calm as ever.

“They seem to have prepared quite thoroughly. Their countermeasures aren’t bad, either.”

At the Grand Mage’s murmur, the Blood Lord spoke in a quiet voice.

“Of course they have. They have to struggle with everything they’ve got.”

“Don’t you think we gave them more time than necessary?”

“You’re bringing that up now? You know better than anyone that this is the surest way. And besides…”

The Blood Lord gazed calmly at the Grand Mage as he added:

“You used that time to prepare, too.”

The Grand Mage gave a short laugh and nodded.

Her white, slender fingertips had already formed a hand seal.

The movement was soft and delicate, but it held another spell within it—one of terrible destructive power.

*Rumble.*

The air began to tremble. Strange patterns etched beneath the Grand Mage’s feet flared with multicolored light.

There were dozens of them.

They were magic circles she had prepared over the past two days for the battle.

“So, what do you want?” the Grand Mage asked.

The Blood Lord briefly considered the question.

*What do I want?*

*Without a doubt, Jin Taekyung’s death.*

But he had to swallow the words welling up in his throat.

That foolish woman would never defy *that person’s* will.

And he had no idea how she’d react if she learned what he was thinking.

So the Blood Lord forced himself to answer in a calm voice.

“The wall. Aim for the wall. Hit it hard enough to bring it down in one blow.”

The Dalai Lama, who’d been listening quietly to their conversation like a docile lamb, suddenly spoke.

“If the wall falls before the rear is completely sealed off, won’t the enemies give up resisting and flee?”

His suggestion sounded reasonable at first, but neither the Blood Lord nor the Grand Mage paid it the slightest mind.

There was a reason to target the wall first—and it wasn’t simply to bring it down.

*Fwoosh.*

The Grand Mage slowly extended a hand. Far above her, the rain that had poured endlessly through the air stopped at her will, then began to gather together.

By the time dozens of enormous spheres of water had formed—

“Fly.”

At the Grand Mage’s quiet command, the spheres hurtled toward the city wall. Each one now carried a weight and force of ten thousand geun.

They surged forward at a fierce speed, as if they would tolerate no interference.

*ROOOAR!*

It happened in an instant.

The archers who’d been firing nonstop at the enemies closing in on the wall stared with their mouths hanging open. The shield bearers who’d been firmly protecting the front line lowered their shields without realizing it.

At last, *they* stepped forward.

*Whoosh!*

Dazzling flashes cut across the air.

Some were as hot as lava. Others were so stealthy they sent a chill down the back of the neck. Still others were as swift as lightning.

By the time the martial artists and imperial troops atop the wall sensed them, it was already over.

*Fwoosh! Boom!*

The enormous spheres of water evaporated, were sliced apart, and burst.

The colossal spheres that looked powerful enough to flatten a mountain, not just the city wall.

The terrifying calamities that had seemed as impossible for humans to stop as a natural disaster.

“……!”

“……!”

Those who’d instinctively sensed their imminent deaths opened their eyes wide in unison.

And at the same time, they remembered what they’d momentarily forgotten:

Those terrifying dark arts called magic weren’t the only thing beyond human power.

“They’re coming in rough right from the start.”

A throne granted to only ten great martial artists across the entire world.

Jeok Cheongang, Fire King, who sat highest among them and stood shoulder to shoulder with the stars in the heavens, spat out some phlegm and grinned.

“How’d they know this old man likes this sort of thing?”

At his voice, like a beast’s growl, the people felt warmth rise in their chests.

The tiny spark of hope, beginning to stir again, blazed brighter still when the giants who appeared next came into view.

“They’re trying to wear down our key fighters.”

A figure closer to a boy than a young man.

But now, everyone knew.

That boy, who still looked as if he hadn’t even lost all his baby fuzz, was the Slaughter Saint, once revered by all.

And there was another living legend beside them, one who’d written a legend of his own to rival the boy’s.

“It’s an obvious move, but an effective one.”

With a voice clearer than raindrops, he drew the bowstring with a rough finger that seemed entirely at odds with it.

*Whoosh!*

A beam of light shot forth.

And then, destruction.

*Crack!*

The beam shattered the invisible protective veil over the enemy forces in an instant, then exploded with a thunderous roar.

It smashed into the ground, piercing the enemies’ lives.

*BOOM!*

The ground shook. The explosion swallowed the screams.

The hulking monsters that moved like little hills, and the Dark Heaven followers advancing behind them, were both powerless to stop that strike.

It proved that the title of Bow Saint was no empty boast.

*We can do this.*

A glimmer of hope flashed through the minds of the people atop the wall, and they trembled with excitement.

They saw the radiance of those people, who hadn’t lost their light even in a world this dark.

They saw the other Supreme Peak masters stepping forward to block the magic that kept crashing toward the wall, and Jin Taekyung, who remained completely unfazed even in this dire situation.

They were moved. And they shuddered.

Because they stood shoulder to shoulder with living legends.

Because those legends were giving everything they had to save them.

*Thud. Thud-thud. Thud-thud-thud!*

A massive rumble rippled outward like a wave.

As if they’d all agreed, the people began stomping their feet. They slammed their shields down, pounded their spear shafts, and struck their swords and sabers together.

Even as a rain of fierce flames poured down.

Even as flashing lightning, ice bearing a dreadful chill, and rain that should have soaked their heads came flying at them—the rain transformed into arrows.

They did not yield.

No—they had no doubt.

Even if they met their end here today, they would become part of a legend, too.

And just as the tiny sparks in their hearts began to flare into a great bonfire—

*Rumble!*

The hulking monsters, who’d steadily advanced despite the relentless rain of arrows and other attacks, charged toward the wall with a roar like an earthquake.

—*GRAAAAH!*

A roar that made their hair stand on end.

At the same time, a body propelled by strength and speed far beyond human limits hurtled toward the wall and slammed into it with all its might.

*RUMBLE!*
## Chapter artifact 1101

# Chapter 1101

For ages, people had used the Yellow River to divide the lands to its north and south, calling them the Central Plains and considering them the heart of the world.

The birthplace of the first ancient civilization, with fertile land and abundant resources driving its insane productivity.

With such ideal conditions, people were bound to flock there from every direction.

The problem was that among them were foreign peoples from distant borderlands, who often wanted to “borrow” the Central Plains’ gold and silver treasures.

In their own special way: by looting or occupying them.

Naturally, the people of the Central Plains weren’t too fond of that.

So they built the Great Wall, stretching a full ten thousand li, strengthened the armies stationed along the borders, and steadily reinforced impregnable fortresses and castles throughout the land, generation after generation.

There was no need to say more about Xining, the capital of Qinghai, the farthest of the borderlands—the continental equivalent of the GOP.

But the rulers of the past who had issued those orders, and the craftsmen and laborers who had worked themselves to the bone, could never have dreamed that there were madmen who would slam their bare bodies into walls built of solid stone, stacked layer upon layer and sealed tight with lime.

Nor could they have imagined that those madmen would be enormous monsters, with monstrous appearances and incredible strength.

*Rumble, rumble!*

The ground—or rather, the city—shook.

The sight of several thousand monsters battering the wall with their bare bodies, or with huge logs and clubs from who knew where, was so overwhelming it made the blood run cold.

As if someone had doused the defenders’ spirits, which had just burned so hot, with ice water.

“Hah…!”

“Don’t break formation! Hold your positions!”

Choked breaths escaped here and there, amid a storm of shouted commands.

And this wasn’t happening only at the West Gate, where I was stationed.

The North Gate and South Gate were the same, as was the East Gate, where the enemy assault was relatively light.

Countless enemies had encircled Xining for dozens of li, and now they were beginning their full-scale siege, leading with monsters that refused to die.

“Archers, ready!”

“Loose! Loose!”

*Shhk, thud-thud!*

Our response was swift, too.

We held back the Dark Heaven followers with a dense rain of arrows fired on nearly direct trajectories, while bringing out the countermeasures we’d prepared for the monsters.

“Is it ready?”

At my quiet question, one of the commanders answered. His helmet was already soaked with sweat inside.

“Everything’s been prepared, just as the Marquis of Shangshan ordered.”

Then there was no need to hesitate any longer.

I turned to the tense commander and imperial troops waiting nearby.

“Pour it all out. Give them the works.”

The moment the order finally came—

*Rumble.*

At the vigorous motion of the signal flags, the large iron cauldrons installed at intervals along the wall tilted with a heavy metallic groan, disgorging their contents.

Thick, black, boiling oil.

*Splash! Ssssss!*

—*GRAAAAH!*

Acrid smoke and the smell of burning mixed together, drowned out by the monsters’ screams.

But I knew better than anyone that this alone wasn’t enough to destroy these things, which were practically undead monsters already.

And with the sorcerers controlling them still nowhere to be seen, I knew this was the right moment for me to act.

*Fwoosh.*

I drew in a deep breath, and the fire dragon curled deep inside me awoke.

It left its longtime home in my Lower Dantian. The enormous flames, now nested atop the peak of my Middle Dantian, stirred and flowed into every limb and point of my body.

Endlessly. Fiercely.

And at the same time, as swiftly as a ray of light.

*Whoosh.*

The moment I stepped forward, a sensation of weightlessness swept over my whole body, chilling my spine.

Before I knew it, everything was beneath my feet.

The city wall, rising a dozen or so jang like a barrier at the edge of the world. The monsters and fanatics blackening the ground below.

Only one thing was level with my eyes now.

A spear, wreathed in the flames of dark blue Force.

*Grind.*

My muscles drew taut like a bowstring, and my senses, sharper than ever, focused at my fingertips.

For the most destructive and perfect arc, slowly cutting through the sky before plunging down.

*Now.*

With that thought, I sent White Flame hurtling toward the distant ground below.

*Whoosh!*

A flash of light. In the space warped by the intense heat, a streak of dark blue flame slipped among the enemies near the wall.

Then came a deafening roar, as if the sky had split apart.

*BOOM!*

A vast pillar of fire surged up along the city wall, mocking the heavy rain that poured down without end.

Beneath it lay the ground, soaked with all the oil we’d poured out without holding back—and the enemies’ flesh and bones.

“Ghk, aaagh!”

“Keugh…!”

Whether by misfortune or good luck, the enemies who’d barely survived were engulfed in flames, shrieking horribly.

Hundreds, by my rough count.

Maybe more.

But before the enormous roar that had shaken heaven and earth could even fade, my body was already dropping over their heads.

*Bang! Bang! Ba-bang!*

The air exploded beneath my feet with each step.

Feeling the ground, which had seemed so impossibly far away, rush up to meet me, I reached out into the empty air, where only wind and rain whipped around me.

*Inventory open. Summon.*

*Ding.*

Along with the System notification came the solid feel of something filling my empty hand. At the same time, the enemies who’d gathered around me, spotting me dropping from the sky, widened their eyes.

“What the—”

*Shhk!*

One strike, one clean cut.

The enemies’ bodies split apart left and right, proving those four words with their lives.

A fountain of blood, vivid red even beneath the dark sky, spurted up. Madness glinted in the eyes of the enemies, already losing their focus.

“Heaven above and earth below, all demons bow!”

“Attack!”

*Shh-shh-shhk!*

A chilling wind of blades swept through the air, colder than the rain.

The enemies had me surrounded on all sides, from every direction, and rushed in without regard for their lives.

Like moths, enthralled, flying toward a flame.

*Shhk!*

Sharp Sword Energy slashed in every direction.

Each streak was blood-red and looked dangerously unstable, as if betraying that its wielder had reached into a realm they had no business touching. Yet their power and speed rivaled a Peak master’s.

Just like the way I still remembered them so clearly.

*Temporary Strength Pills.*

The final flame of a person’s life, kindled with their own life as the fuel.

I knew well that though the pills’ effect lasted only a short time, their power was as great as their danger.

And I knew just as well that the shoddy kindling they’d piled up couldn’t match the heat of the furnace I’d built by surviving countless brushes with death.

*Thump!*

I didn’t even channel internal energy into the blow, conserving my strength as much as possible.

But that was enough.

My body had already surpassed human limits by several steps. My senses, honed in the face of death, made it possible.

*Grrk.*

As the Dark Heaven follower’s throat was torn open in an instant and he clutched at his neck, I’d already passed him and plunged toward the other enemies.

*Whoosh!*

Half a step to the left.

Three lines of Sword Energy brushed past me by a hair and tangled together in midair. The rough broad-bladed saber that had been rusting in Xining’s armory left my hand.

*Wham!*

The blade spun with terrifying force and not an ounce of internal energy, cutting through three necks.

No—it smashed through them.

At the same time, with a command ringing in my mind, a new pair of blades appeared in my hands.

A straight sword in my left. A narrow-bladed sword in my right.

They were unfamiliar. Yet, strangely, they felt familiar enough to be a contradiction.

*Shreeeek! Thud-thud!*

The most fitting strength and speed. And with them, movements that read the flow of battle.

I was swept into a state of No-self as I tore through the enemies beneath the wall. Each time I swung my sword and saber as if dancing, blood and screams burst forth. With every step I took, corpses spread beneath me like a carpet.

*Come.*

I spared even the single breath I might have let out without thinking.

With only those words murmured in my heart, I kept cutting down the enemies surging toward me from every direction.

I dodged a thrusting sword and pierced its wielder’s heart with the narrow-bladed sword. With nothing but a straight sword gone red with rust, I controlled the blades of five swords imbued with Sword Energy.

*Clang-clang-clang!*

I pressed down on the sides of their blades and twisted. That alone sent the swords tangled together in a wild snarl flying away from one another, while cutting off the enemies’ breath.

Strength when strength was needed. Softness when softness was needed.

When the narrow-bladed sword broke, I summoned an axe from the nearly infinite storeroom of my Inventory. With the broken straight sword, I wielded a blade technique infused with the principles of the Flame Divine Palm.

Even I couldn’t understand it, but in this moment, I was free from every restriction and limit.

And suddenly, I understood.

*So this is what it means.*

Jeok Cheongang had once told me:

When one’s understanding of martial arts reached a certain realm, everything alive and moving became a martial art of its own.

Even a reed, bent weakly in the wind, would be no different from a Divine Sword.

Of course, I hadn’t reached that level. But at last, I thought I could faintly grasp what he’d meant.

*Shhk!*

With the sensation of death running through my fingertips, I started to turn toward another enemy—then blinked.

There was no one. Everything was quiet.

The Dark Heaven followers who’d taken Temporary Strength Pills. The enormous monsters that could no longer be called human, either.

Beneath the western wall, I was the only one left standing on two feet.

And the blood-soaked scene spread before me meant one thing.

I’d wiped out the enemy vanguard, which had numbered a thousand at the very least.

All by myself.

*Ding. Ding. Ding.*

> **System**
>
> You have met the activation conditions for the Title **One Against a Hundred**!
>
> You have met the activation conditions for the Title **One Against a Thousand**!
>
> **Intimidation** rises significantly!
>
> Your enemies are rapidly cowed by your powerful **Intimidation**!
>
> The status effect **Fear**, applied to some allies, is removed!
>
> Allied morale rises significantly!

As the System notifications poured into my ears like a dam breaking, a tremendous roar erupted from atop the wall.

*BWOOOOO!*

A horn sounded, its deep reverberation enough to make me shudder. With it, the main force of Dark Heaven—no less than a hundred thousand strong—began advancing toward the city walls.

And then I understood what their movement meant.

“……!”

The monsters.

No—the giants.

Their corpses, each one well over a jang tall, had piled up to the middle of the wall.
## Chapter artifact 1102

# Chapter 1102

Looking back over the whole of human history, sieges had always been overwhelmingly favorable to the defending side.

If you wanted to take something that belonged to someone else, you had to pay a price worthy of it.

An attacking force needed at least three times as many soldiers to capture an ordinary castle or fortress. And even with more than that, the chances of losing a siege were still considerable.

Of course, to some people, that was nothing but old history, worn out and rusted.

“‘Impregnable’ is nothing but nonsense left behind by weak losers.”

*Rumble.*

A vast rumble rolled over the Blood Lord’s low voice.

At that very moment, Dark Heaven’s enormous army, turning the once-green, vast expanse of land pitch-black, advanced toward the city wall like a single wave.

They would climb that towering wall using the corpses of humans and monsters as footholds.

They would write a new history of their own.

*The vanguard was annihilated faster than I expected…but it doesn’t matter. As long as we take Xining and cut that bastard’s throat.*

Jin Taekyung, defending the West Gate, hadn’t been the only one to stop the vanguard.

The Bow Saint and Slaughter Saint had defended the South Gate and East Gate, respectively, while the Fire King, Jeok Cheongang, held the area around the North Gate. Four other Supreme Peak masters supported them from behind.

Yet even after thousands in the vanguard had vanished in reckless charges against the walls on all four sides, the Blood Lord remained utterly unmoved.

*This much damage is nothing if it means achieving my goal.*

The monsters had been prepared for a moment just like this.

They would have been powerful forces in a battle on open ground, but every expendable asset had its use, depending on the situation.

Though he had lost nearly half the monsters as a result, the Blood Lord was certain he’d made the right choice.

If he had sent ordinary followers—mere humans—out in front, they would have lost not thousands but tens of thousands before they could begin a proper siege like this.

“What about the mages? Are they all in their assigned positions?”

The Grand Mage nodded at the Blood Lord’s sudden question.

The hundred or so mages under her command were a core part of their forces, no different from a modern magic corps, and they had a vital role in this battle.

Under the ironclad protection of their allies, their task was to throw the Supreme Peak masters off balance.

“Keep up the pressure. Make sure they have no choice but to spend their strength without a moment’s rest.”

Even with an overwhelming advantage, the Blood Lord wasn’t letting his guard down.

The four Demon Lords and the Demon Empress who had already met their ends had taught him a valuable lesson. And even without them, the defenders were an impressive lot.

No fewer than eight Supreme Peak masters.

One of them, the fool they called Great Sir, seemed so far gone that it was hard to imagine he could function like a normal person. But it was rare for so many powerful fighters to gather in one place, even among the countless battles of the Great Faction War.

No—for that matter, the total number of troops assembled on this battlefield might be unprecedented in the history of Murim.

That was why the Blood Lord couldn’t allow even the slightest variable.

Especially not the one person who had created more variables than anyone else, time and again.

*Jin Taekyung.*

His gaze settled into a deep, still calm.

In the distance, a young man stood before the charging followers, whose cries shook heaven and earth. His figure appeared in the Blood Lord’s eyes.

So did the fountains of blood erupting ceaselessly around him.

*Fwoosh!*

With every flash of light, one life after another flickered out.

His movements had reached an astonishing realm: simple, swift, and utterly overwhelming.

And yet—

*Nothing lasts forever.*

Jin Taekyung was undoubtedly strong.

He might even be growing stronger, little by little, at this very moment.

But everything had its limits.

*In the end, he’ll grow tired. Jin Taekyung, the Fire King, and all the other old men.*

Unless the Blood Lord gave the order, the wheels of this enormous war of attrition, turning on the back of overwhelming numbers and strength, would never stop.

Not until those eight Supreme Peak masters—their heads and hearts—were exhausted.

And the Blood Lord had an instinctive feeling that the moment was drawing near.

He also knew what he needed to prepare in order to cut Jin Taekyung’s throat.

“From now on, I’ll take full responsibility for the West Gate.”

At the Blood Lord’s sudden announcement, the Grand Mage understood the meaning behind it and spoke.

“For some reason, that sounds like you’re ordering me to leave. Am I imagining things?”

“That’s exactly what it is: your imagination.”

“Then why should I leave the West Gate?”

“Do you need a reason? I’m the commander in chief.”

“I acknowledge that. I’m just a little suspicious, that’s all.”

“Suspicious? What exactly are you trying to say?”

“Who knows. For instance…”

The Grand Mage let her voice trail off. She glanced back and forth between the Blood Lord and Jin Taekyung, who was fighting desperately to defend the western wall, then added:

“I worry that someone who’s always claimed to be *that person’s* most devoted servant might go overboard with his loyalty—even to the point of defying his master’s wishes.”

The words sounded as if she’d seen straight through him.

But the Blood Lord showed not the slightest hint of agitation.

He had considered that the Grand Mage might suspect his intentions ever since deciding to kill Jin Taekyung.

“That’s not just a misunderstanding. It’s senility. Do I look like an idiot who’d commit such an act of disloyalty?”

At his calm reply, not a trace of hesitation or uncertainty in his voice, the Grand Mage stared at him for a moment, then shrugged.

“Certainly, the you I’ve known so far has been far from disloyal. Though sometimes your loyalty was so excessive that you looked like an idiot.”

In the past, the Blood Lord would have bared his teeth and snarled at that. But his mind was colder than ever.

“So, what’s your answer?”

“Fine. Where should I go?”

“Take the South Gate.”

“The South Gate? You mean the Bow Saint?”

“I’ll assign you three Black Ghosts. No, four. With that much force, even the Bow Saint won’t have many options.”

What the Blood Lord said was undoubtedly true, but the Grand Mage furrowed her brow.

“Four Black Ghosts?”

There were still nine Black Ghosts who hadn’t been sent into battle.

Even after one had been lost in vain to the Fire King and Slaughter Saint’s surprise attack, they still retained their living martial prowess and had near-immortal recovery. It was hard to understand why the Blood Lord would assign four of them to her.

That wasn’t just a matter of her own safety. It meant leaving a gap in the forces that could break through the walls on all sides when the time came.

But the question that had crossed her mind disappeared the moment she heard the Blood Lord’s next words.

“Don’t hold back. You and the mages. And if the Black Ghosts appear as well, the enemy will put even greater forces at the South Gate.”

The Grand Mage finally understood the Blood Lord’s intention and let out a quiet laugh.

“So, in the end, I’m bait to draw in the Fire King or the Slaughter Saint?”

“Half right, half wrong.”

“What?”

“The Fire King won’t go to the South Gate. He’ll be busy greeting an unexpected guest.”

The Blood Lord answered without hesitation, then turned his cold gaze toward the Dalai Lama, who had been watching the northern wall all this time.

“Isn’t that right, Palace Lord?”

“……!”

His eyes trembled with emotion.

Realizing that the moment of revenge he had waited so long for had finally arrived, the Dalai Lama slowly parted his lips.

“What should this humble monk do?”

“Show that old man, the Fire King, the resentment and strength of the Potala Palace—built up over a long, long age of endurance.”

“I have waited my whole life for this moment alone.”

The Dalai Lama pressed his palms together with heartfelt sincerity, then leaped atop a massive elephant.

“Come. The time has come to avenge our ancestors.”

His quiet voice, infused with internal energy, carried on without end.

The Twelve Secret Monks, including two Supreme Peak masters, and the Potala Palace’s monks, numbering a full ten thousand, let out a roar so loud it made their ears ring.

*Bwooooo!*

A horn sounded, shaking the battlefield.

And so the great army of Xizang’s Murim, now a single religious state, charged through the torrential rain toward the North Gate.

To trample the descendants of the Fire Gate Clan, sworn enemies with whom they could never share the same sky.

To offer the head of the current Fire Gate Clan Sect Leader, the Fire King Jeok Cheongang, heir to that accursed lineage, before the spirits of their ancestors.

As the Dalai Lama’s forces quickly disappeared into the distance, the Grand Mage’s voice reached the Blood Lord’s ears.

“Does that mean the East Gate is all that’s left?”

“I’ll send two Black Ghosts to the East Gate.”

“Two? An awkward number. The Slaughter Saint could take them.”

“But that won’t happen. I’ll order them to avoid a direct fight with the Slaughter Saint as much as possible and stick to a cautious attack.”

“I take back what I said about the number being awkward.”

The Grand Mage’s lips curved softly beneath her veil.

“It seems like the right number. The Slaughter Saint won’t leave his post to help the South Gate, even if it’s in danger.”

The Blood Lord gave a faint smile to match hers.

“And that will keep them from suspecting us.”

If Dark Heaven didn’t assign any significant forces to the East Gate, that alone would arouse suspicion.

But if they had enough forces there and merely kept up a looser assault, the troops at the East Gate, including the Slaughter Saint, would have a little room to breathe—and time to look around.

Time to help their other allies, who were on the verge of collapse, unlike themselves.

And the gap that opened up at that very moment would be the crack that brought down that strong, massive dam in an instant.

*Whoosh.*

The wind and rain whipped at his clothes.

An ordinary person would have trembled in the biting cold that seeped into their bones, soaked through and through. But the Blood Lord smiled as he reached out.

An east wind.

A fierce wind blowing from the east along a tributary of the Yellow River—stronger than ever.

Along with more guests riding the surging river currents, who would bring this battle to its grand finale after the Potala Palace.

*Preee!*

Against the dark sky and driving rain, an eagle flew in from the east, cried out with a powerful call, and landed on the Blood Lord’s shoulder.

Its bones showed through in patches, and its blood-red eyes gleamed.

Recognizing the good news heralded by the eagle’s arrival, the Blood Lord stroked the hilt of the sword tucked at his waist and murmured:

“The time has come.”
## Chapter artifact 1103

# Chapter 1103

One Against a Thousand.

Just a few years ago, I’d been living a life that had nothing to do with those four words.

I’d scraped together some secondhand gear at a bargain price after a few rounds of haggling. I couldn’t even afford a decent supply of the cheapest potions. The most I could handle was a few dozen small monsters in the dark, damp caves inside the subspaces known as Gates.

But a lot had changed since then.

More than I could put into words.

*Thwack!*

The rusty iron sword I swung on instinct sank into the crown of an enemy approaching from the side. His skull split, and bright red blood sprayed in every direction.

*Plop.*

A sticky, hot sensation brushed my cheek.

Once, that chilling touch would have made me flinch. Then the foul stench that crawled into my nose would have made me recoil again.

But that rookie Hunter, who’d thrown up at the horrible stench of blood he’d never smelled before, existed only in my memories now.

*Thrust!*

I drove the blade into the throat of the enemy charging straight at me, twisted it, and yanked it free. Blood poured from the gaping wound.

*Grrk.*

His body trembled as a wet rattle rose from his throat.

But to the fanatics, intoxicated by the strength of the Temporary Strength Pills and years of brainwashing, their comrade’s gruesome death was martyrdom—and just another chance to exploit an opening in my guard.

*Shh-shh-shhk!*

Blood-red Sword Energy rained down from every direction. The dense, destructive energy tangled together like a net, covering my entire body.

Or at least, that was what it must have looked like to them.

*Tap.*

One step.

With that single step, the space between my enemies and me vanished.

As I spun, the iron sword in my hand traced a perfect, deadly arc.

*Whoosh!*

For an instant, the world seemed to stop.

The enemies realized that instead of retreating, I’d plunged straight into their midst. Their eyes slowly widened.

And then—

*BOOM!*

As the Sword Energy they’d already unleashed exploded, dozens of heads shot into the air like fireworks.

*Shhk, fwoosh!*

Red.

The world—and everything in my sight—was red.

Yet even now, all my senses and bodily functions kept working without pause.

*Whoosh.*

Everything caught in the slanted path of my sword split apart.

As I crossed the rising mound of corpses, sticky blood and screams—darker still—spilled around my feet.

*Thwack! Thrust-thrust!*

I cut, stabbed, and smashed without pause.

It didn’t matter what I held in my hands.

An axe, a sword, or some oddly shaped weapon like a mace or a scythe—all of them were, at their core, weapons meant to kill.

*Crack!*

A storm of blood and flesh swept through the air.

The weapons that had been left deep in Xining’s armory, rusting red, became masterworks imbued with a craftsman’s blood and sweat the moment they landed in my hands. They might break against Sword Energy, but they still fulfilled their purpose.

By taking the lives of my enemies, just as their new owner intended.

……!

……!!

The enemies surrounding me on all sides, and the shouts of my allies raining down from the wall above, filled the air.

But I couldn’t even make out what they were saying.

My ears, which should have been taking in every sound with razor-sharp senses, felt muffled. The world before my eyes moved so slowly it was almost boring, yet every detail was crystal clear.

I had no idea how many enemies I’d taken down, or how many weapons I’d broken.

I was certain of only one thing.

Insight.

I was climbing another step toward a new realization.

Wrapped in a fog of No-self, forgetting not only the situation around me but even myself, I moved through a battlefield where life and death hung in the balance.

*More. Just a little more.*

As if bewitched, I kept muttering the words in my heart.

At some point, everything around me had begun to feel hazy, like a dream.

A sensation, impossible to tell whether it was pain or pleasure, ran down my spine like an electric current.

I’d felt it before.

Now the sensation of Trance was more intense than ever, taking over my entire body.

*Come.*

As though they’d heard the quiet whisper that echoed only in my heart, the enemies charged at me as one. They recited those eight words, that curse disguised as a creed—“Heaven above and earth below, all demons bow!”—then roared and lashed out with the weapons in their hands, putting all their strength behind each blow.

And in that same instant, every one of them became a lonely soul.

*Shhk. Shhk. Shhk.*

Was this what the prophet in the old myths had been like?

Everything split apart as I strode forward without hesitation.

There was no sea before me, but the blood the enemies spilled surged like waves. It was another kind of Red Sea.

And at the end of those red waves spilling away on either side, an insight awaited—one that would lift me to a higher level.

*I can do this. I know I can.*

Instinct gradually layered over my fading reason.

Without even looking, I dodged the blade swung at me from behind. With one sweep, I cut down five enemies charging from the side and the front.

But still, it wasn’t enough.

I suddenly wanted this dreamlike sensation to last forever. This dream belonged only to me, and it was the sweetest sleep I’d ever known.

Even if I woke from it, I’d sell my soul just to see this story through to the end.

If I could make the insight that drew closer with every step my own, I could fall into this same sweet sleep whenever I wanted.

But then I remembered something I’d briefly forgotten.

If there was someone dreaming, then there was someone who could wake them.

*Whoooooosh!*

Through ears that had been receiving every sound around me as a distant echo came the sharp whistle of something cutting through the air.

The fury in it, the enormous force drawing nearer by the second, dragged me out of my dream and threw me into reality.

Along with someone’s urgent, unfinished shout, suddenly bursting from somewhere in the open air.

“Dodge—!”

At that very moment—

*Fwoosh.*

The fog of No-self that had taken over my mind and body scattered in an instant.

No—it burst apart.

At the same time, a blood-red flash hurtled toward me from far away, its dazzling glimmer staining my vision with a sticky red.

“……!”

My eyes flew open before I knew it. A red alarm rang in my mind, whispering:

*It’s too late. You can’t dodge this.*

The flash shot toward me with such terrifying speed, and I’d been thrown straight from a sweet dream into reality so abruptly that I couldn’t move fast enough to keep up.

Unlike whoever had warned me of the danger half a beat earlier—someone who might have been watching over me the whole time.

*Whoosh!*

In the slowed-down world, the figure of a person falling through the air appeared on my retinas.

A snow-white blade blocked the flash, which was already almost at my nose. Violet Sword Force scattered around it like flower petals.

*Cheongpung.*

The instant his name surfaced in my frozen thoughts—

*BOOM!*

A tremendous shock wave shook the air with a roar like the sky splitting apart.

* * *

*Cough.*

In the dusty haze that covered everything, Jin Taekyung blinked dazedly and wondered:

*Am I still alive?*

The question surfaced in his mind.

The answer came right away.

Small and large pains pricked through his whole body, accompanied by a System alert only he could hear.

No—warning sirens was the more accurate description.

*Beep! Beep!*

Trying to ignore the sirens that kept drilling into his ears, Jin Taekyung struggled to his feet.

*Rumble.*

Stone dust slid off his body.

Heavy. Painful.

Maybe it was because he’d suddenly woken from a Trance in which every sense had been pushed to its limit.

His body sagged like cotton soaked with water. But despite the barrage of warning sirens, he didn’t seem to have any serious injuries.

Of course, he had someone to thank for that: the person who’d blocked the flash in his place at the last moment.

“Young Hero Cheong.”

His tired, cracked voice slipped past his lips. But in the dust cloud, so thick he couldn’t see a hand in front of his face, all he heard were groans from people he couldn’t identify.

“……Young Hero Cheong?”

When no answer came, even after he’d called several times, a foreboding feeling crept over him.

Jin Taekyung took a deep breath and flung out the sleeve that had already been torn to shreds.

*Boom!*

Compressed air exploded. A gust imbued with internal energy swept away part of the dense dust cloud, and the scene hidden beyond it finally came into view.

A gaping hole in the city wall, wide enough for five grown men to stand shoulder to shoulder, and allies sprawled everywhere, groaning in pain.

But even now, there was no sign of Cheongpung.

*Dammit.*

Jin Taekyung clenched his teeth without realizing it.

Then he stretched out his hand toward the enemies charging through the ruins of the broken wall and the dust cloud.

More precisely, toward his beloved weapon, which lay behind them.

*Vooooom.*

His Middle Dantian opened. With a low hum, a spear buried deep in the ground shot upward and returned to its master’s grasp.

It pierced through every obstacle in its way.

*Crack!*

A fountain of blood surged up.

Dozens of enemies who’d been charging with their spirits high fell like rotten logs. Taking advantage of the opening, the allies formed ranks and fought with all their might to close the gap.

*Clang!*

*Thrust!*

“Gaaagh!”

“Hold them! Don’t let a single one through!”

“Cough—Archers! Where are the archers?”

Chaos spread in an instant.

And even as the melee broke out around the breached wall, Jin Taekyung cut down enemies with all his strength, shouting one person’s name.

“Young Hero Cheong! Cheongpung!”

But no matter how keenly he strained his senses, there was no answer.

Only the screams and shouts of friend and foe alike rang out all around him. That damned innocent voice was nowhere to be heard.

His heart thundered in his chest, and every moment made it harder to breathe.

*……No way.*

No. It couldn’t be.

Cheongpung—he wasn’t the kind of guy who’d go down this easily.

Like the hero in a fairy tale, he’d somehow survive and live happily ever after.

Then why?

Why did this inexplicable unease keep growing heavier and darker?

“You… bastards!”

With a shout full of rage, Jin Taekyung charged toward the enemy.

It was anger at the invaders who’d caused all this—but also blame directed at himself, the idiot who’d been consumed by a single-minded pursuit of enlightenment.

And the dazzling point of his spear, cutting through the enemy and raising a storm of blood, was drawing closer to one person approaching at a leisurely pace.

The Blood Lord.
## Chapter artifact 1104

# Chapter 1104

*Splash. Splash.*

The sound of footsteps crossing ground covered in blood, rainwater, and countless corpses rang out with unusual weight.

Tens of thousands.

No—even on this vast battlefield, where friend and foe together numbered well over a hundred thousand, his presence was utterly overwhelming.

*Vooooom.*

Qi spread through the space with every step he took.

Even now, rain and arrows poured unceasingly from the sky, only to bounce off an invisible barrier of energy. The Dark Heaven followers charging toward the collapsed western wall split to either side and prostrated themselves.

As if bewitched, they murmured a creed of eight words.

“Heaven above and earth below.”

“All demons bow!”

It was reverence.

Reverence offered to the true ruler of this world—their god—and permitted only to the six Apostles he had personally favored.

The creed, begun with a few quiet murmurs, soon became a tremendous roar that swallowed the battlefield.

……!

……!!

A ripple became a current, then a wave that swept in every direction.

The pounding rain, the thunder flashing between the dark clouds, even the arrows raining down to fill the sky—nothing could stop the creed pouring from their lips.

“Now! Attack!”

“Archers! Loose together!”

*Shhk! Thud-thud-thud!*

Blades flashed, and heads sprang up all over the battlefield.

And that wasn’t all.

Arms and legs severed from their bodies plunged into the mud. Arrows streaking in like flashes of light buried themselves in backs and waists.

But that was all.

Even when their limbs were cut off, even when arrowheads pierced their backs and poked out through their chests, they stubbornly continued reciting the creed.

Until the very moment death fell over them.

“Heaven above and earth below—cough. All demons bow……”

*Thud.*

The Dark Heaven follower collapsed. He’d kept reciting the creed to the bitter end, even as blood poured from him. The Kunlun Sect Daoist who had stabbed him through the chest trembled, lips quivering.

“P-Primordial Heavenly Venerable.”

A wave of fanaticism beyond words.

And there were fanatics like these everywhere, people who didn’t even fear death.

No—all the enemies, darkening this vast battlefield, were like that.

“This… What in the world is this?”

The one phrase someone managed to squeeze out was what everyone felt. It was steeped in the greatest fear and horror a person could feel.

*Splash. Clatter.*

Weapons slipped from suddenly slack hands and sank into the mud.

For an instant, some of the Murim warriors and imperial troops lost their will to fight without even realizing it. Their trembling eyes stared blankly at the enemy.

They were afraid. Terrified to the point of shuddering.

Not of some huge, savage monster, but of those who looked just like them.

Those mad fanatics, stripped of the joy, anger, sorrow, and pleasure every human being ought to feel, blindly following only the Lord of Heaven.

And at their center, at the head of their ranks, walked a man wreathed in rippling, blood-red qi.

“What a bunch of worthless bastards.”

His soft sneer revealed a row of white teeth.

At the same time, as the Blood Lord gently extended his fingertips, countless weapons that had been rolling across the ground rose upright.

No—they shot forward at their new master’s command.

Toward the enemies, frozen in place.

“You don’t deserve to live.”

At that moment—

*Pa-pa-pa-pat!*

Hundreds of weapons tore through the air in an instant.

A wave of steel surged through the ruins of the collapsed wall.

There was no choice left for those facing that blinding flash. They weren’t even granted time to close their eyes, let alone draw one last breath.

All they could do was stare, eyes wide, at the death bearing down on them.

And feel a streak of searing wind sweep over their heads.

*Gooooom.*

Space warped.

A heat so tremendous it was horrifying, dark blue light-flames, filled everyone’s sight.

And at last—

*Fwoosh—KRAAASH!*

The wave of steel met a wall of fire.

They collided head-on.

Unleashing all the unimaginable power they held within them—the blinding light and rumbling force—into every corner of the battlefield.

*Rumble-rumble-rumble……!*

Would this be the sound a fully awakened volcano made as it roared after a long sleep?

Or would a storm like this sweep over the land if an ancient giant exhaled with all its might?

No one could say.

No one, that is, except the two people standing tall as iron towers in the fierce light and shock wave that heated and drove back everything within dozens of yards.

“Good. You, at least, deserve to live.”

The Blood Lord murmured and brought down the edge of his hand. The cloud of dust coiling around the western wall split apart in an instant, revealing what it had concealed.

A young man, drenched from head to toe in blood and rain, stood perfectly steady, aiming a pure silver-white spear at him.

“That’s precisely why I can’t let you live.”

The Blood Lord watched the young man, admiration in his voice.

“Blazing Flame Divine Dragon, Jin Taekyung.”

At that moment, Jin Taekyung’s tightly closed lips parted.

“Thanks for the surprise worship, but……”

*Squelch.*

He pulled out the shards of blades that had somehow pierced his body in several places as they flew through the wall of fire, then continued:

“No matter how I look at it, you don’t deserve to live, you son of a bitch. That’s why you have to die.”

His voice was calm, but flames poured in streams from his eyes.

The Blood Lord gave a quiet laugh as he looked at him.

“Do you think you can do that? In your current condition?”

The Blood Lord wasn’t exaggerating.

Jin Taekyung’s appearance alone made him look like a man drenched in blood.

Given how many enemies he had cut down, that was only natural. But that didn’t mean he’d come away unscathed.

No. Jin Taekyung was undoubtedly exhausted and injured, too.

So were the others now rising one by one behind his back, which stood as imposing as a mountain.

But he wasn’t afraid at all.

He’d already been afraid enough before now.

He had acknowledged and accepted every negative feeling that had weighed down his body and mind.

And so, even as the Blood Lord approached, Jin Taekyung managed a faint smile.

“Sure, you could think that. But do you know what?”

“What are you talking about?”

“Your precious friends all pulled that same shit on me before they died.”

“……!”

“That’s what you call a death flag, you moron. Ah, would you even understand if I explained it?”

At Jin Taekyung’s laugh and incomprehensible words, the sneer at the Blood Lord’s lips vanished without a trace.

“But I’m different from those idiots. I gave up on the idea of halfheartedly letting you live long ago.”

*Fwoosh.*

Blood-red qi rose in wisps with every step.

In the Blood Lord’s red-glinting eyes, only Jin Taekyung was clearly reflected.

“You die today. No question.”

“Wouldn’t the Lord of Heaven be upset to hear that? He must’ve thought you were a good dog and taken a liking to you.”

“He will understand. This choice I make today comes from loyalty alone.”

“Is that so? Or is it just what you hope?”

“What?”

The Blood Lord stopped walking for an instant. Jin Taekyung’s voice slid into his ear.

“You think he won’t understand. You think you’ll be screwed if you get caught. So you’re doing it first and hoping for the best. Even going so far as to send the Grand Mage far away, just in case.”

“……!”

“Why are you staring at me like a rabbit caught in headlights? You look disgusting enough already. Anyone would think you’d just been slapped awake from the deepest sleep. Didn’t you already get a rough idea in your dream?”

*Crunch.*

The Blood Lord clenched his teeth without realizing it.

It wasn’t Jin Taekyung’s relentless taunts that made him do it. It was the truth he’d tried to ignore, stabbing into his heart like an awl.

“You know well enough, too. What your master—that damned Lord of Heaven—wants most.”

He had to refute him.

That insolent brat was openly insulting the master he worshiped like a god and questioning his intentions. The Blood Lord should tear his mouth apart right now and rip out that wicked tongue.

But he couldn’t refute him.

The Blazing Flame Divine Dragon, Jin Taekyung.

The Blood Lord had a vague sense that everything coming from that impertinent mouth was true.

He didn’t know when it had begun. He hadn’t even been told why.

But everything that had led to this moment pointed to one painful truth.

“What your master wants most isn’t the world. It sure as hell isn’t the lives of hunting dogs he uses and throws away, like you.”

It was more than a voice that burrowed into his ears. It was a truth that shook him to the core.

“It’s me. Only me.”

“……!”

“So go on, try to kill me. If I can screw the Lord of Heaven over by using you, I don’t care how it happens.”

That very instant, the Blood Lord’s eyes, which had been slowly reddening, turned completely bloodred, their white pupils swallowed up.

And countless corpses scattered across the ground within a dozen yards convulsed and spewed blood.

*Swoosh.*

The blood mixed with rainwater writhed as if it were alive and gathered at one man’s feet.

At the same time, as his footsteps began to move again, the blood kept flowing together, joining and merging, until it climbed his calves and wrapped around his whole body.

No.

It was absorbed into him.

As if it had always been part of him, from the distant past.

*Fwoosh.*

Feeling an unending well of vitality and strength rise from deep inside him, the Blood Lord’s eyes blazed red.

“I heard your last words.”

Jin Taekyung stared blankly at the unexpected sight, then smacked his lips and replied:

“Uh, maybe. Could I say a little more?”

The Blood Lord answered that ridiculous question with a massive flash of blood-red light.

*Whoooosh!*

In an instant, the world turned red.

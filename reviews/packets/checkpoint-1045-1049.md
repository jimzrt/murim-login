# Checkpoint Review — 1045–1049

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

# Chapters 1045–1049

## Plot

The Bow Saint shatters the Grand Mage’s Hell Fire sphere with Force arrows, killing thousands—mostly Dark Heaven’s forces—and saving survivors from the falling fireballs. The arriving Embroidered Uniform Guard and Coalition Army rally against Dark Heaven. Sima Gong reveals he joined Dark Heaven for a calculated bargain but turned against the Blood-Sword Demon Lord to help Jeok Cheongang and protect the Black Dragon Demon Gate’s future. Gravely wounded and missing an arm, he survives the chapter.

The Bow Saint and Jeok Cheongang badly wound the Blood-Sword Demon Lord, and Sima Gong stabs his ankle before Jeok sends him crashing beside the Grand Mage. Jin Taekyung’s spear attack fails against her barrier. Instead of finishing the Demon Lord, the Grand Mage heals Jin enough to regain consciousness and binds him with plant magic. She says the Lord of Heaven ordered the Demon Lord’s disposal after his role was fulfilled, then urges Jin to kill him and grow stronger. Jeok Cheongang and the Bow Saint reach the hill and see Jin bound; the battle continues below.

## Continuity

- The Bow Saint’s Force arrows destroyed the Hell Fire sphere and later the falling fireballs; the blast caused thousands of casualties, overwhelmingly among Dark Heaven’s forces.
- The Embroidered Uniform Guard and surviving Coalition Army have joined the battle against Dark Heaven.
- Sima Gong betrayed his bargain with Dark Heaven to aid Jeok Cheongang and protect the Black Dragon Demon Gate’s future. He is gravely wounded and missing an arm; his fate remains unresolved.
- The Blood-Sword Demon Lord is gravely injured and beside the Grand Mage. She says the Lord of Heaven ordered his disposal after his role was fulfilled.
- Jin Taekyung is conscious but weakened and bound by the Grand Mage’s plant magic. She urges him to kill the Demon Lord.
- Jeok Cheongang and the Bow Saint have reached the hill and seen Jin bound. The battle at the Great Snow Mountain continues.

## Translation Decisions

- Render 대술사 and 대마도사 as Grand Mage.
- Retain Hell Fire for 헬파이어 and use hellfire for descriptive 겁화.
- Render the Bow Saint’s arrows as Force arrows; the chapters give them no named technique.
- Use Flame Divine Palm for 화염신장 and Flame-Extinguishing Divine Fist for 멸염신권.
- Render 기세 as “momentum” for the battle’s shifting tide.
- Render 사냥개 as “hunting dog.”

## Durable state

{
  "active_continuity": [
    "The battle at the Great Snow Mountain continues.",
    "The Blood-Sword Demon Lord is gravely injured; the Grand Mage says the Lord of Heaven ordered his disposal after his role was fulfilled.",
    "Jin Taekyung is conscious but weakened and bound by the Grand Mage’s plant magic; she urges him to kill the Blood-Sword Demon Lord and grow stronger.",
    "Jeok Cheongang and the Bow Saint have reached the hill and seen Jin bound.",
    "Sima Gong remains gravely wounded and missing an arm; his fate is unresolved."
  ],
  "continuity_sources": [
    1048,
    1049
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Why did the Lord of Heaven order the Blood-Sword Demon Lord’s disposal?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who are the white-robed mages, and what is their purpose?",
    "How were the former Demonic Cult fiends made into Black Ghosts?"
  ],
  "safe_through": 1049,
  "temporary_decisions": [
    "Render 대마도사 as Grand Mage.",
    "Use Fire Ball, Stone Wall, and Magic Arrow for the named spells.",
    "Render 헬 파이어 as Hell Fire; use hellfire for descriptive 겁화.",
    "Render 쇄월검진 as Moon-Shattering Sword Formation."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 1045

# Chapter 1045

Regardless of its type or purpose, there were two main conditions for bringing a spell’s power to its limit.

First: the caster’s immense mana.

Second: a magic circle capable of gathering and releasing that mana with the greatest efficiency.

That was why the magic wielded by the woman known as the Grand Magecould only be utterly perfect.

Just as a masterwork sword was born after countless rounds of hammering and quenching, magic, too, could reach its greatest power when enough time and effort were devoted to it.

While the hillside below was turning red with blood, the spell circle that had already been completed began to activate. No one could stop it. And Jin Taekyung wasn’t the only one who had some idea of the power contained in that enormous sphere of flame.

Fwoooooosh!

The world slowed.

Light and flame spread, slowly.

The fireball was still two *jang* from the ground, but the heat pouring from it was already horrifyingly intense.

The shadow of the flames, having swallowed the wind and moisture all around, stretched over part of the battlefield. Fire King Jeok Cheongang watched it descend with stunned eyes.

*So this is… Magic.*

The words *dark arts* had long since vanished from his mind.

Yes. This was Magic.

A spell wielded not by a human, but by a demon. Jeok Cheongang knew there could be no more fitting description.

He also knew that, at this very moment, he was the only one left who could stop that powerful explosion.

Boom!

Flames burst from his toes as he shot forward at the speed of a flash.

But as Jeok Cheongang charged toward the fireball with the Flamefire Path, a chilling whistle rang out behind him. He had to duck in a hurry.

Shwoooosh! Slice!

The back of his head suddenly grew hot.

Like a skilled butcher slicing meat, a streak of dark-red Force skimmed past Jeok Cheongang’s head, slicing off a thin layer of hair and skin before cutting through the air.

“Where are you in such a hurry to go?”

His toes shifted for the briefest instant as he dodged. By then, the butcher of a man had appeared in front of him at a speed beyond Shifting Form and Position. Jeok Cheongang bit his lip.

“Blood-Sword Demon Lord, how dare you…!”

“How dare I? After ending up in that state, you still don’t get it?”

The Blood-Sword Demon Lord smiled and gave the sword in his hand a shake.

Unlike Jeok Cheongang, who was covered in blood after their fierce battle, he’d suffered only a few minor wounds. Now he was utterly certain.

Of their obvious difference in strength.

Of his own advantage.

“You can’t stop it. Nothing.”

Shwaaak!

His sword turned hazy like a heat shimmer and rushed in, tearing through the wind.

Bang! Bang! KWA-BOOOOM!

Its speed and destructive power defied imagination.

Force surged up like a giant wave, striking and shattering everything around them.

Jeok Cheongang barely dodged the attacks raining down on him, not even taking time to catch his breath. His eyes grew still.

*I can’t stop anything, huh? Yes, I suppose that’s true.*

If he’d possessed nothing but a fiery temper, his title of Fire King might already have been erased from the world.

But Jeok Cheongang had survived this long amid the mountain of sabers and forest of swords that was the Murim, and even at a moment like this, with life and death hanging in the balance, he faced reality with a cool head.

There was only one way past the Blood-Sword Demon Lord blocking his path—and one way to stop the terrible calamity that had yet to reach the ground.

*Dance of the Fire God and Demon.*

Yes. That was his only choice.

The final dance of a fire demon, performed with death already accepted.

The beginning and end of the Fire Gate Clan. The fiercest blaze—and the final ashes.

There was no flame in this world that burned forever. When the dance ended, the heat would fade and his body would burn to ash.

The more powerful the spark within, the greater its blaze. And to endure that growing fire, one had to throw ever more of one’s life into it as kindling.

*This will be the last time.*

Fire King Jeok Cheongang knew it by instinct.

The dance about to begin would be his third—and his last.

This body, holding more Scorching Yang Qi than ever before, wouldn’t survive it this time.

But he had no regrets.

Even if his body turned to ash and scattered, the spark he left behind would remain.

Even if Fire King Jeok Cheongang’s flames died out, the spark called Jin Taekyung, the Blazing Flame Divine Dragon, would burn brighter somewhere in the world.

So…

*That’s enough.*

Jeok Cheongang murmured to himself and twisted his body. He evaded the dense net of Force covering every direction and drew up every last bit of energy he possessed.

The Scorching Yang Qi he’d accumulated over countless years—several *jiazi*’ worth.

And at last, he awoke the innate qi sleeping deep inside his body, a forbidden realm for martial artists.

No—more precisely, he tried to awaken it.

At that very moment, a massive jet-black Force came flying from somewhere and blocked the Blood-Sword Demon Lord.

Whooom—KWA-BOOOOM!

Power clashed with power, Force with Force.

A thunderous crash sent the air around them into turmoil.

The Blood-Sword Demon Lord emerged, parting the cloud of dust that was about to rise in an instant. He recognized the intruder and frowned.

“…Why are you here?”

“Go, Fire King.”

The dry words slipped between his firmly closed lips.

The intruder—no, Black Night King Sima Gong—kept his eyes fixed on the Blood-Sword Demon Lord as he calmly added, addressing Jeok Cheongang behind him,

“Before I change my mind.”

“……!”

Jeok Cheongang’s eyes widened at this unexpected appearance.

Sima Gong—the man he’d thought was a traitor.

No, he’d been certain of it.

There was so much he wanted to ask him, so much he wanted to say.

But Jeok Cheongang had almost no time. He put all of it aside and sprang forward again, leaving only a short Sound Transmission behind.

*Stay alive, you filthy unorthodox bastard.*

There was no answer.

Only the wind that tore across his whole body as he followed the Flamefire Path, and the terrifying crashes and shouts that rang out through it.

“How dare a bastard like you—!”

KWA-BOOOOM!

The air around them shook. That was all.

Jeok Cheongang realized that Sima Gong had barely blocked the Blood-Sword Demon Lord’s Force from behind him. Gritting his teeth, he pushed himself to go faster.

A few moments.

That was all Sima Gong could hold out against the Blood-Sword Demon Lord as he was now.

He might lose his life in only a few dozen exchanges.

But…

*That’s enough.*

A single finger’s breadth could decide life and death, and a gap of a split second—divided and divided again—could change one’s fate.

That was the Murim. The world of superhumans.

Crack!

The ground sank beneath Jeok Cheongang’s toes as he pushed off with all his strength. The world slowed, and pure-white flames surged up.

BANG!

No flame could move faster than light.

But in that instant, Jeok Cheongang crossed dozens of *jang* in a single bound. Nothing could hold him back.

If one chain bound him, it was time alone.

*Damn it!*

Jeok Cheongang swallowed the groan threatening to break from his lips.

His body shot forward in an explosion of speed, heading straight for the enormous sphere of flame.

It was less than one *jang* away from the ground now, a terrible blaze spreading over everyone’s heads.

*Just a little farther…!*

But no matter how desperately he wished otherwise, reality followed its cruel course.

Fwoooooosh.

Hot.

Even from more than twenty *jang* away, it was hard to breathe.

Watching the flames swell at last before they touched the ground, Jeok Cheongang suddenly thought:

If only he’d had a few more seconds.

If only he’d been a dozen *jang* closer to it.

And…

If only someone other than Jeok Cheongang or Jin Taekyung were here—someone who could stop the calamity.

*Damn it.*

Jeok Cheongang clenched his teeth and forced himself forward with his last strength.

He knew.

It was already too late to stop this enormous explosion.

But he still had to move.

He belonged to neither the righteous path, the unorthodox factions, nor the Demonic Path—but this was the path he’d chosen.

If he didn’t at least try, he felt he’d never be able to look that reckless brat of a Disciple in the face again.

“Come on!”

Jeok Cheongang unleashed the azure dragon’s roar, shaking the air in every direction, and threw a punch with all his might at the calamity twenty *jang* away.

Then, in the next instant, he saw it clearly.

And heard it, too.

Shwoooooosh!

Just as the white light-flames of the Flame-Extinguishing Divine Fist shot out in an explosion, a dazzling streak of light shone across the dark sky ahead of it, cutting through space.

Those brilliant bolts plunged into the enormous, swelling sphere of flame.

Gooooooong.

In a world that seemed frozen, a distant flash of light and fire blended together, turning everyone’s vision white.

* * *

The sky and the earth split apart.

Instead of the world everyone knew, a new world made of light opened up.

At least in that moment, everyone on the battlefield—not just Jin Taekyung—must have felt that way.

*Could this be…?*

Fwoosh.

Before Jin Taekyung could fully recall the unbelievable sight he’d seen at the last moment, he felt his vision, which had been washed in blinding light, slowly return.

The blinding white flash that had obscured everyone’s vision faded. What filled the space it left behind was a tremendous roar that came belatedly, and flames surging up across the battlefield.

BANG! KWA-BOOOOM!

KOOOOROOM!

Would this be what it looked like if the sun in the sky rained down?

Hundreds of fireballs, great and small, fell over a radius of more than a hundred *jang*.

They crushed frail human flesh and bone, melted the ground, and evaporated snow mixed with blood.

Just as its name suggested, Hell Fire—like the flames of death.

But death did not treat everyone on the battlefield equally.

“Ah.”

The groan that suddenly slipped between someone’s lips didn’t belong to Jin Taekyung.

The Grand Mage silently gazed at the hellscape spread out below the hill.

More precisely, she was watching the Dark Heaven cultists collapse into charred lumps, unable even to scream.

*Why?*

She felt no sorrow at the sight of her allies meeting such a horrible death.

Only pure confusion.

Why had the fireball that should have exploded in the midst of the enemy’s forces broken into pieces and swept through her own allies instead?

Among the roughly thousands of casualties, why did the enemy number fewer than a hundred?

Her mind was filled with nothing but questions. The Grand Mage had watched only Jeok Cheongang at the last moment, but someone else, who’d taken everything in, already knew the answer.

“You’re damn late.”

“What?”

At the voice that suddenly rang out behind her, the Grand Mage turned without thinking—and saw Jin Taekyung smiling, weakly but unmistakably.

Over her shoulder, in his eyes fixed on some distant place, she caught the faint reflection of something golden.

“Damn old hag.”

“……!”

At that instant, the Grand Mage understood something and spun around in a hurry.

At the same time, she saw the answer to her question with her own eyes.

Shwoooosh!

The streak of light that had torn the fireball apart—the Force arrows.

“Bow Saint…!”
## Chapter artifact 1046

# Chapter 1046

Among the tens of thousands of allies and enemies locked in a brutal battle across the vast battlefield, killing and dying, no one noticed at first.

Not the dazzling white flash that suddenly flew in and shattered the enormous ball of fire.

Nor the Force arrows still raining down over the slopes of the Great Snow Mountain.

Shwip, shwip, shwip!

One, two, three. Then ten.

Ten streaks of light burst forth one after another, tearing through the air all at once.

Though there had been a slight delay between them, the dazzling streaks lined up side by side and swept across the battlefield, spanning more than two hundred *jang*.

More precisely, they struck the great and small balls of fire that were falling in a direction they had no right to take.

KWA-BOOOOM!

A deafening roar rolled over itself, and the heat from the impact swept across the ground.

Fwoosh, sizzle!

Collars blackened. Hair melted away.

But to those who had already sensed death as they watched the spheres of flame come crashing toward them, pain like this was nothing.

No—their astonishment and shock were so great that, if only for a moment, they forgot the pain.

“H-How…? Cough.”

The old Daoist, the Taeeul Merciless Sword, coughed up a mouthful of blood. He couldn’t finish his sentence; the corners of his eyes trembled.

At the last moment, he had given up everything and closed his eyes. He couldn’t believe he was still among the living.

Beside him, though, someone who had stared death in the face as it bore down on them reacted differently.

“Heh. Heh…”

The Roaring Fury Swordsman let out a weak laugh, not even noticing that one of his arms had been burned black.

He had wanted to die like this. He deserved to die.

And yet he had survived.

Thanks to help he had never expected.

Today, right here, he had seen once more that destructive, dazzling flash he’d witnessed in his distant youth, when his white hair had still been black—and before that dreadful hair had melted away.

*Bow Saint. Is it really you?*

An incredible coincidence? Or Heaven’s grace?

As the words echoed in his heart, the Roaring Fury Swordsman squeezed out what strength remained and rose to his feet.

He didn’t know whether this was mere good fortune or a fate decreed by Heaven.

But one thing was certain.

If there was a reason they were still alive, it was to pay for the sins they had yet to atone for.

“…Primordial Heavenly Venerable.”

At last, the Roaring Fury Swordsman planted both feet on the ground. For the first time in ages, he invoked the Primordial Heavenly Venerable, then looked up at the sky.

Shaa.

As if answering his call, a ray of light slipped through the black clouds blanketing the sky.

Beneath that light, the Zhongnan Sect Disciples—whom he’d thought had already left—were sweeping through their enemies.

Shing! Slice!

Swords flashed, scattering blood.

Beneath the fireballs raining down only on their enemies, a desperate yet powerful battle cry rang out.

“Disciples of the Zhongnan Sect! Don’t you dare retreat!”

“Yaaah!”

KWA-BOOM!

Rrrrmmble!

Flames surged endlessly, and the earth turned over.

Even as they were charred black, the Dark Heaven forces advanced as if possessed, chanting words of worship to the Lord of Heaven.

Yet the Zhongnan Sect Disciples, now fewer than five hundred, never stopped moving—not for a single moment.

“Our path is here!”

Zhongnan One Dragon, Hyuk Sopyung.

His cry, ragged as if he were coughing up blood, roused the minds of all those sunk in exhaustion.

The sight of them fighting with death already accepted, together with the Force arrows raining down one after another, stopped the Gansu Coalition Army from retreating as it staggered backward on the brink of defeat.

“Damn it! Attack!”

“Now! Push them all back!”

“Yaaah! You fucking bastards!”

Unorthodox factions, orthodox factions, dark-path figures. Even the imperial army.

They were jumbled together as chaotically as the battle itself. They still couldn’t make sense of what was happening, but all of them instinctively knew:

If they didn’t seize this chance now, they’d never get another.

And at the front of the group charging at the enemy again with screams that sounded like cries of anguish was a band of fighters who hadn’t retreated for even an instant—not from the beginning, not now.

“Uoooooh!”

Whoom!

The whistle of the weapon alone sent a chill down the spine.

With a battle cry like a beast’s roar, the massive two-section staff swept through the enemies blocking the way.

KRAK-KOOM!

Blood and flesh flew in every direction.

Perched on the shoulder of the giant who stood out even on the battlefield, the small, foreign old man spat out the piece of flesh that had gotten into his mouth and screamed.

“Hey! To the side! Look to the side!”

But before Taishan could understand the foreign old man Namho’s shout, seven enemies rushed in from the flank, swinging Sword Energy.

Shing! Slice!

Three weapons had already cut across the space ahead of them, cleaving through their necks and chests.

Splaash!

Amid the spray of blood, Soul-Chasing Guest Song Ilseom spoke as he shook the sticky blood from his willow-leaf saber.

“Is everyone all right?”

Namho had had his mouth open and swallowed a mouthful of blood. He answered, “No. My stomach’s churning.”

Thwack!

With a horrifying impact, Taishan felled another enemy—or rather, smashed him halfway to pieces. His voice was unusually subdued as he replied,

“Namho. Don’t throw up. Not until we find the Lord.”

“Look at this little shit. Is that how you talk to an old man who’s suffering at his age?”

“Then why’d you come? Did someone threaten you with a knife?”

“……!”

Namho was at a loss for words. Ju Hwaran, who had been cutting down enemies with movements as graceful as a dance, spoke up.

“We’re all right, too. I’m just worried about the Pavilion Master.”

Hyuk Mujin clutched his side, where a long gash had opened during the fight, and muttered, “I’m hurt, though…”

“Everyone’s fine. So stop hesitating and let’s get to the Pavilion Master.”

“No, why didn’t you even ask—”

“Pavilion Master. Danger. Urgent.”

Hyuk Mujin immediately shut his mouth. Ma Junggeol, the leader of the Seven Masters of Baekma Bang, who had somehow ended up here with them, looked sadly back and forth between the dagger stuck in his thigh and Ju Hwaran.

“Do you have something to say?”

“Young Lady, well. It’s just…”

“You don’t.”

“…Right. Let’s say that.”

At the sight of Ju Hwaran, whose eyes had begun to gleam, Ma Junggeol lowered his head gloomily.

They were crazy.

There was no doubt about it. These people were completely insane.

*Why did I come all the way here?*

He didn’t know.

He’d blinked a few times, and somehow he was running with them. Before he knew it, he was fighting on the front line.

How could anyone be unscathed in the middle of a battle unless they were a Supreme Peak master?

He’d been hit by a sword and stabbed with a dagger in the thick of the fighting.

But he had to keep fighting.

No—he was being told to keep fighting.

*Shit…*

More than ever before, Ma Junggeol wished he could see his sworn brothers, who weren’t here.

The image of the Lord, who did nothing but talk nonsense, kept appearing before his eyes.

*You said you’d bring him here in time. You damn bastards.*

Swallowing back tears, Ma Junggeol glanced behind him for no reason.

The Great Snow Mountain—perhaps the last thing he’d ever see—still stood magnificent and radiant, as it always had, even now that tens of thousands of unwelcome visitors had left it behind…

“Hm?”

For a moment, Ma Junggeol doubted his own eyes.

And it wasn’t because of the streaks of light pouring down the slopes of the Great Snow Mountain and into the battlefield one after another.

He already knew, through these suspicious companions, that the legendary Bow Saint had appeared.

But…

*What’s that?*

What had caught Ma Junggeol’s eye at that moment was a golden wave flowing down the Great Snow Mountain.

* * *

The Great Snow Mountain was always white, blanketed in snow that never melted.

In spring, summer, fall, and winter.

It had been that way for a thousand years, and it would still be the same a thousand years from now.

But today, at this very moment, was an exception.

Whoooosh!

The wind howled.

The snow on the ground scattered as figures that had appeared out of nowhere somewhere in the mountain range raced forward in streaks of light.

They raced down the steep mountainside as if it were flat ground, moving like a single wave.

A golden wave, its dazzling radiance undimmed no matter where it went.

“The Embroidered Uniform Guard…!”

When someone’s shout, brimming with barely restrained emotion, swept across the battlefield, a thousand Embroidered Uniform Guards in golden armor were already racing down the mountainside like a wave, picking up speed.

All the while, they repeated two words in their minds: victory.

And listened to the commander’s voice, clear in their ears.

“Do you see them?”

No one answered the question from Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard.

Only their aura, simmering like water in a cauldron, steadily grew stronger.

“Our enemies are there. Evil men who defy the natural order and seek to plunge the world into misery.”

It had been more than a hundred years since the age of warring heroes came to an end and a new dynasty took its place.

The hero of the Zhu clan ascended the throne and at last became the father of all his people. His descendants, the dragon-blooded heirs, called themselves the Sons of Heaven and firmly established their authority.

Among the countless people, those with the greatest martial skill and loyalty were selected and given golden robes and armor. Thus was the Embroidered Uniform Guard born.

“They disturbed the imperial court and sought to bring down this nation, ruled by His Majesty the Emperor!”

As Jeong Hogun’s voice grew stronger, a thousand pairs of eyes glinted beneath their lowered helmets.

From Zhejiang Province, where the Imperial Capital stood, all the way to Shanxi.

Then on through Liaoning and Hebei—and, as though that were not enough, across half the continent to Gansu.

It had been a grueling journey.

It would be a lie to say they weren’t tired.

No matter how elite they were, the finest force of the Great Nation guarding the Imperial Family, their bodies were not made of steel.

But the Will and loyalty they carried in their hearts were harder than steel and shone as brightly as gold.

*Go. You are my sharpest sword and my shield. Protect the Marquis of Shangshan, benefactor of the Imperial Family, and put his enemies to the sword.*

The thousand Embroidered Uniform Guards still remembered it vividly.

No—they would never forget it, not until the moment they died.

The sight of the Son of Heaven they had met the day before leaving the Imperial Capital.

Despite his pallid, sickly complexion, the Emperor had spoken of Jin Taekyung, the Marquis of Shangshan, with a smile—and given them his final command.

*Remember. His enemies are my enemies.*

As the Emperor’s commanding voice echoed in their ears, Jeong Hogun cried out with force,

“Do you all remember the imperial command from that day?”

At their commander’s question, they answered.

In their own way.

Clang, clang, clang!

Countless weapons finally emerged into the open, glinting in the light. Beneath their helmets, their eyes shone toward the enemies drawing rapidly closer.

A thousand weapons shimmering with tangible energy.

A thousand pairs of eyes radiating suffocating fighting spirit.

And a thousand masters, each possessing both.

The enormous golden wave covered the mountainside and poured toward the battlefield.

No—it became a wave and swept away everything in its path.

Shing! KWA-BOOM!

At the very moment the Force arrows fired by the Bow Saint vaporized the enemy ranks—

KRAK-KOOM!

The thousand Embroidered Uniform Guards drove through the opening like awls, changing the course of the battlefield.
## Chapter artifact 1047

# Chapter 1047

If you asked what mattered most in deciding the outcome of a battle, every single person would give the same answer.

The quality of the troops—or their numbers.

But if the person you asked were a general commanding an army, he would answer differently.

He would name the two words that flashed through the Blood-Sword Demon Lord’s mind at that very moment.

*Momentum.*

There was no doubt about it.

The enemy’s momentum, the tide of battle, had changed.

The Blood-Sword Demon Lord suddenly felt the air grow hot.

The fighting spirit of his enemies, which had been fading little by little like a campfire soaked by drizzle, was rising. Their shouts, wrenched from them with all their strength, were growing more and more intense.

An emotion close to desperation. A resolve to face death without hesitation.

Weapons swung with their final spark of life, as if their wielders had never once considered giving up.

And then—

Shwaaa!

A dazzling streak of light cut across the sky, one step ahead of them.

KWA-BOOOOM!

A flash packed with terrible destructive force swallowed dozens of Dark Heaven cultists in an instant.

The explosions of fireballs, large and small, had already opened gaps in their ranks.

Now the tremendously powerful streak of light shook their once-solid formation. All the enemy needed was a spear to slip through the opening and pierce their heart.

Something like…

A golden spear called the Embroidered Uniform Guard.

KRAK-KOOM!

Deafening shouts and thunderous booms blended together.

As they collided, countless lives were won and lost amid blades swinging like lightning. A thick mist of blood blanketed the area.

It took only an instant for the golden wave that had swept over the steep slopes of the Great Snow Mountain and charged onto the battlefield to turn red.

Slice! Thud-thud!

A flashing blade cut through a neck in one stroke. A sharp spearhead pierced a chest.

Every one of them had reached at least Supreme First Rate, with some attaining the Peak realm. That was how they had earned the honor of protecting the imperial family. The Great Nation’s most powerful force cut and stabbed through everything in their path.

Their fierce shouts proclaimed why they had come to this battlefield.

“Long live His Majesty the Emperor! May His Highness the Imperial Crown Brother live a thousand years!”

“For the Marquis of Shangshan!”

“Charge!”

Shwish-shwish-shwish!

Led by those armed with a fanatic’s loyalty, more than twenty thousand surviving Coalition Army soldiers charged forward.

Some sought revenge for their comrades. Others fought for a greater cause.

Their reasons and aims differed, but they all wanted the same thing.

Victory.

And the Blood-Sword Demon Lord, who felt the scales of battle tipping rapidly in the face of this unexpected turn, wanted a glorious victory here today just as much as they did.

“You’ve got to be fucking kidding me…!”

A groan slipped through his clenched lips.

The battle was unfolding in a way the Blood-Sword Demon Lord hadn’t expected.

*The Bow Saint—and now the Embroidered Uniform Guard?*

One of the Three Saints, the Bow Saint, needed no introduction. The Embroidered Uniform Guard, directly under the imperial family, was the Great Nation’s sharpest sword.

His side still had the advantage in numbers, but he could no longer be sure they were stronger overall.

And now that this powerful reinforcement had restored the momentum of the more than twenty thousand enemy soldiers, they were charging wildly. Unease began to take root in one corner of the Blood-Sword Demon Lord’s mind.

*No… No, that can’t be.*

He desperately rejected it.

The two words that had appeared in his mind without his noticing: *defeat.*

And the sight of himself, growing more and more apprehensive even now, when he had become more powerful than ever.

*The sorcerers are still here. The Grand Mage is, too. If that bitch can do what she did before, we won’t be at a disadvantage.*

But why?

The enormous ball of fire that had even stunned the Blood-Sword Demon Lord, one of its own allies, hadn’t appeared again.

He sensed neither another spell nor a surge of qi heralding one.

*…Why?*

Could something have happened to the Grand Mage in that brief time?

The Blood-Sword Demon Lord’s heart lurched. He turned to check what was happening on the hill.

Or rather, he tried to.

Until someone who had been watching him calmly spoke up.

“Things aren’t going as you planned.”

Black Night King Sima Gong.

At the words that slipped between his bloodied lips, the Blood-Sword Demon Lord’s face twisted like a fiend’s.

“What?”

“I understand. Sometimes things just don’t go your way.”

Sima Gong continued in a calm, weary voice.

He looked at his arm—or rather, the shoulder where the Blood-Sword Demon Lord had brutally torn it away.

“I couldn’t have imagined I’d end up like this, not even half an hour ago.”

He wasn’t saying this merely because he’d lost an arm.

Sima Gong was half-submerged in a pool of blood. Thick blood that belonged to him alone.

Yet the Blood-Sword Demon Lord, who had struck down the traitor in his path in moments, trembled with rage, not the joy of punishment.

“If it weren’t for you—if it weren’t for you…!”

Everything had gone badly wrong.

Under the original plan, Sima Gong was supposed to order the Gansu Coalition Army to retreat at the right moment, and the Blood-Sword Demon Lord would have won easily.

That had been their bargain.

If Sima Gong helped Dark Heaven win in Gansu, they would use it as a foothold to seize the Central Plains and recognize his ownership of Gansu and Shaanxi.

A secret, reasonable deal.

And part of it had already been carried out successfully.

Not here, at the Great Snow Mountain, but in Dunhuang, at the western edge of Gansu Province.

“Was this your plan from the beginning? Are you saying you used the Kongtong Sect—not anyone else—as a simple decoy just to win today and make us believe you were still our spy?”

Questions poured out of him in a rush.

There was no time to waste.

By all rights, he should have cut short the life of this traitor he wanted to tear apart with his bare hands and started to salvage the situation at once.

But the Blood-Sword Demon Lord still couldn’t believe he’d been wrong. He had to hear the answer.

Because the Black Night King Sima Gong he knew was an unorthodox man to the bone.

A pest worse than a bat, ready to join hands with the devil himself—not just Dark Heaven—if it meant surviving.

That was why the Blood-Sword Demon Lord had chosen Sima Gong as a partner, but even when he set foot in Gansu, he still hadn’t let go of his last doubts.

Only after they won a tremendous victory over the Kongtong Sect guarding Dunhuang, using the information Sima Gong had given him, did he finally trust him.

“Answer me! Now!”

Anyone else would have reacted the same way, not just the Blood-Sword Demon Lord.

The Kongtong Sect’s resistance in Dunhuang had been fierce, and the damage they suffered was severe.

No one could come up with the insane idea of using a member of the Nine Sects and One Gang as a decoy in a temporary ruse, no matter how much they believed in sacrificing the small for the greater good.

At last, under the overwhelming pressure radiating from the Blood-Sword Demon Lord, Sima Gong’s tightly closed lips parted.

“I’m no madman. I’m too rational to betray one side only to turn on the other. That’s why I joined hands with you.”

One sentence confirmed the Blood-Sword Demon Lord’s suspicions.

But it was both the answer he wanted and one that planted an even greater question in his mind.

“Then why the hell—”

“Why? Why would I do this? Well…”

Sima Gong cut him off, blinking weakly as he asked himself the question.

Why had he made such a foolish choice?

When everything had been going smoothly, why had he crossed a river he could never return from?

Then he found himself thinking of someone who wasn’t here—and shouldn’t be—and gave a bitter smile.

“Maybe I went crazy for a little while.”

“What… did you say?”

“But I’m incredibly lucky that moment of madness worked. Don’t you think?”

In the end, the moments Sima Gong had spent standing against the Blood-Sword Demon Lord hadn’t changed the course of the battle. But Fire King Jeok Cheongang, whom he had helped, would never forget it.

That was enough for Sima Gong.

Even if he died, the Black Dragon Demon Gate would survive with at least some measure of absolution.

His heir, who wasn’t here, would live and make everything Sima Gong had passed down even stronger.

“I’m tired. I should rest now.”

The old unorthodox sect leader spoke calmly to the Blood-Sword Demon Lord, who stood frozen, eyes wide.

Then he added one last thing he’d wanted to say to the fanatic before him, who had betrayed the Heavenly Demon and taken a new master.

“Go ahead and kill me. You bat-like Demonic Cult bastard.”

“……!”

Grind.

A chilling scrape came from between his clenched teeth.

The Blood-Sword Demon Lord clenched his molars as if to crush them, then raised his sword, pouring his rage into its tip.

He aimed it at the traitor who had ruined a plan that should have succeeded—and dared to throw filth in the path of the mighty Lord of Heaven.

Shwaaa!

But just as the sword, wrapped in dark-red Force, was about to come crashing down like lightning—

Shing! KRAK-KOOM!

A streak of light flew in from somewhere, striking the flat of the blade dead on.

Slice!

The sword veered off at the last moment and carved into the ground instead, as easily as a knife slicing tofu. At the same time, the Blood-Sword Demon Lord recognized the streak of light and shouted, his voice boiling with fury.

“Bow Saint…!”

As if answering his call, another Force arrow came flying through the crumbling ranks of Dark Heaven’s cultists.

Shwish-shwish-shwing!

Five streaks of light illuminated the surroundings. The Blood-Sword Demon Lord’s figure blurred for an instant as he gritted his teeth.

Bang! Bang! KWA-BOOOOM!

Explosions and thunderous booms followed the sword as it moved faster than sound.

The trembling blade sent a powerful shock through him, but that was all.

The Blood-Sword Demon Lord easily cut or deflected every Force arrow the Bow Saint fired. He bared his teeth in a grin.

“So this is all you’ve got?”

The Blood-Sword Demon Lord remembered something he’d briefly forgotten in his disbelief.

That’s right.

With the sorcerers’ help, he was stronger now than he’d ever been.

Even with one of the legendary Three Saints, the Bow Saint, on the battlefield, she couldn’t match him now that he’d surpassed his limits.

*I don’t know why that insolent bitch, the Grand Mage, is still quiet…*

Tzzzz.

Beyond the blazing Force, a sinister red light glinted.

“Come on. I’ll take you all on.”

And in the very next moment, the Blood-Sword Demon Lord realized—

“Now that’s good to hear.”

—another thing he’d briefly forgotten.

“Being this old and ganging up on someone’s pretty embarrassing. You’ve made me feel a lot better.”

Fire King Jeok Cheongang.

The Blood-Sword Demon Lord’s pupils trembled as he spotted the old monster of Mount Jiuhua, a warm smile on his lips, with flames so fiercely bright they were horrifying wrapped around both hands.
## Chapter artifact 1048

# Chapter 1048

The Blood-Sword Demon Lord stared, his gaze wavering, at the two figures before him.

It was a strange sensation—one even he, a fiend who had made his mark on an entire age, had experienced only a handful of times.

Beneath a sky buried in storm clouds, countless enemies and allies were locked in a desperate battle. And yet it seemed as though those two alone filled his field of vision.

That was how much weight and meaning their titles carried: Fire King and Bow Saint.

All the more so when two living legends appeared in one place.

*I can’t see an opening…*

The Blood-Sword Demon Lord swallowed without realizing it.

Not a hundred enemies. Not a thousand. There were only two people before him.

And yet those two made him feel as if he were surrounded on all sides by an army of more than ten thousand.

No—that wasn’t all. There was even greater pressure than that.

Step.

For an instant, three footsteps overlapped.

Jeok Cheongang and the Bow Saint slowly closed in from either side. The Blood-Sword Demon Lord instinctively stepped back, then belatedly realized what he’d done and flushed.

He’d been pushed back.

By their aura. By their fighting spirit.

And Fire King Jeok Cheongang was not the sort of man to politely overlook it.

“What happened? A moment ago, you said you’d take us all on. Changed your mind already?”

“…You damn old bastard.”

“Sounds pretty good today. Go on, say some more.”

“What?”

“Has that young brat’s hearing gone bad already? I said keep running your mouth.”

Jeok Cheongang grinned and continued.

He was visibly wounded, but a fierce heat still burned in his voice and across his face.

“Come to think of it, every bastard who’s talked to this old man like that has ended up dead. Every last one.”

“……!”

The Blood-Sword Demon Lord’s eyelids quivered.

It was an obvious taunt, but he knew from experience that Jeok Cheongang wasn’t just putting on a show.

No matter how far he’d surpassed his former limits, it was hard to imagine him gaining the upper hand against both the Fire King and the Bow Saint at once.

Shwaak!

And then, at that very moment, a streak of light cut through the air. For all its dazzling brilliance, it was more than enough to deepen the Blood-Sword Demon Lord’s unease.

Rrrr, KWA-BOOM!

A Force arrow came flying without warning.

The Blood-Sword Demon Lord reacted at once, batting away the terrifying streak of light. As he tightened his grip on the sword hilt trembling from the impact, a graceful figure emerged through the cloud of dust.

Swish.

Her steps were so light they seemed weightless.

Her dust-covered clothes fluttered, proof of the punishing journey she’d made across half the land without a moment to catch her breath.

But the woman’s face, visible above them, was flawless, and her gaze fixed on the enemy beyond the dust cloud shone cold and bright.

*Three jang straight ahead. Three chi to the left.*

So Gyo—no, the great martial artist known by the title Bow Saint—thrust herself forward and gripped her beloved weapon.

At the same time, three streaks of Force gathered along her white fingers as they flashed into motion.

Pa-pa-pat!

The dust cloud split apart. Force arrows, carrying power greater than lightning, cut through everything in their path.

The Blood-Sword Demon Lord felt the surging power beyond them before he could even see it. He whipped his sword through the air with all his strength.

Whoooom!

A horizontal slash that seemed capable of cutting through even Mount Tai.

Dark-red Force swelled around the blade, then swept aside the Force arrows with speed and strength far beyond human limits.

KWA-BOOOOM!

The air burst in every direction. The Force that had swallowed the streaks of light shot straight ahead.

Rrrrmmble!

It didn’t merely shake the earth. The strike laid waste to everything in its path.

But the destructive trail of that bloody flash held no sign of the enemies the Blood-Sword Demon Lord was looking for.

Only two different whistles tore in from the blind spot he couldn’t see.

Fwoosh! Shing!

In a world that seemed to slow, the Blood-Sword Demon Lord’s eyes flew wide.

One attack was as fierce as could be. The other was so stealthy it raised goose bumps.

Their energies were opposites—he could tell that from the sound alone. But the Blood-Sword Demon Lord knew better than anyone what they had in common.

*If I let even one strike through, it’s over.*

How many martial artists in this vast land could withstand the attacks coming at him now, even if the whole world were turned upside down?

The Fire King and the Bow Saint.

The Bow Saint and the Fire King.

They weren’t merely relics of a distant past.

They had written their own legends then, and carried those legends into the present. In the distant future, countless people who loved to tell a story would sing of their deeds and praise them.

That was how legends lasted. How giants were remembered forever.

And perhaps, here today, a new verse would be written in that legend.

Two great martial artists had felled the fiend known as the Blood-Sword Demon Lord on the open plain of the Great Snow Mountain, amid blood and snow.

But…

*That will never happen.*

The Blood-Sword Demon Lord clenched his teeth. As the flow of time slowly returned, he pushed every ounce of strength and every sense he possessed to its limit and twisted his body.

It was a nimble movement he believed he would never be able to repeat in his life.

Slice!

A sudden, burning pain ran along his arm and the side of his neck.

The Bow Saint.

She had separated her beloved weapon, which had been shaped like a bow, into two curved swords. She had already passed him by.

The two flashes she’d swung, secretive yet swift as lightning, had torn away part of his nape and the shoulder of his left arm.

But the attack, which should have been enough to take his life outright, had done surprisingly little. Before the pain could fully register in his mind, the Blood-Sword Demon Lord felt an appalling heat rush at him from the side.

Fwoosh! Poom!

*Hng…!*

It all happened almost at once.

Jeok Cheongang’s Flame-Extinguishing Divine Fist had swept fiercely past his flank.

The heat from that glancing blow had melted away a fistful of flesh.

And the unbearable pain had made the Blood-Sword Demon Lord suck in a breath and stop moving without realizing it.

But that was all.

At that moment, the Blood-Sword Demon Lord was cheering deep down at the fact that he’d survived.

Even though the Bow Saint had taken one of his arms, and the heat from Jeok Cheongang’s fist had melted part of his flank and reached his innards as well.

*That’s enough.*

The Blood-Sword Demon Lord had something to fall back on. An injury like this was something he could endure.

What mattered more than anything was that he hadn’t fallen to the combined attack of the Fire King and the Bow Saint—and that, unlike them, who had already missed their perfect chance, he still had one move left.

*I’ll kill them. I swear it!*

A decisive strike always left an opening.

The Blood-Sword Demon Lord suppressed the pain surging through him and slashed his sword down at Jeok Cheongang, who watched him with eyes wide open.

No—more precisely, he tried to slash down.

But before he could, someone moved with a desperate resolve equal to—or perhaps greater than—his own moments earlier.

Thuk!

A fierce, unexpected pain shot through him. The Blood-Sword Demon Lord staggered, then stared in disbelief at the dark blade that had pierced his ankle—and at the face of the man holding it.

Black Night King Sima Gong.

“You son of a—”

The moment he managed to force out a groan—

“I told you. Every last one of them died.”

Poom! Krrrcrack!

At Jeok Cheongang’s cold voice, the Blood-Sword Demon Lord’s vision flipped over.

The dark sky. The ground covered in blood and snow. The countless people fighting and killing one another across it.

Everything turned blindingly white, then red.

Flame Divine Palm.

The dreadful heat, unlike Jeok Cheongang’s cold voice, melted flesh and broke bones as it sank deep into his body. Paralyzed by the excruciating pain, the Blood-Sword Demon Lord could do nothing.

Except that an unexpected stroke of luck awaited him—something even he hadn’t foreseen.

KWA-BOOM! KWA-BOOM! Krrrcrack!

His body shot away like a cannonball, unable to withstand the tremendous force. It rolled and crashed along the ground before finally slamming into something.

“Well.”

The Blood-Sword Demon Lord spat blood mixed with bits of his innards. A voice drifted faintly into his ear.

“You’ve been badly hurt, Demon Lord.”

Was it an illusion?

The Blood-Sword Demon Lord blinked weakly as he wondered. Then he realized the slope beneath his battered body was a hillside, and that the voice he’d just heard sounded uncannily familiar.

“Guh, hahahaha!”

The Blood-Sword Demon Lord burst out laughing without meaning to.

Blood bubbled in his throat, and every time his body shook with laughter, tremendous jolts of pain shot through his broken limbs. He didn’t care in the least.

He laughed like a madman.

Like the happiest person in the world. Like someone who had been rescued at the very edge of death.

Trembling with joy, he stretched a bloodied hand toward his savior.

No—he gave his subordinate an order.

“Heal me. Right now.”

The savior, the Grand Mage, gazed silently at the Blood-Sword Demon Lord. She slowly parted her lips to speak—

Shwaak!

A streak of light whistled through the air. The Blood-Sword Demon Lord’s eyes flew wide.

He saw a young man beyond the Grand Mage’s shoulder, hauling himself up from where he had fallen. With a fiery gaze, the young man brought his spearhead down.

There was not even a thread of internal energy in it. No trace of his usual strength or speed.

It was Jin Taekyung, squeezing out every last bit of strength he had left to unleash a strike with all his might.

*You’ve got to be fucking kidding me…!*

The Blood-Sword Demon Lord screamed soundlessly.

Clang!

An invisible barrier around the Grand Mage knocked away the silver-white spearhead.

It did so with astonishing ease, as if mocking the desperate hope behind the blow.

And then—

That was all.

Thud.

The spear shaft rolled from its owner’s powerless hand.

In the Blood-Sword Demon Lord’s eyes, still wide with a moment’s shock, someone’s figure was slowly tipping over.

Thump.

The body finally crumpled.

Jin Taekyung lay in a wretched heap, glaring weakly at him. The Blood-Sword Demon Lord sucked in a breath without realizing it.

*You stubborn bastard.*

He’d already reached his limit, and still he’d waited for a chance to strike.

His persistence was so terrifying it inspired awe—or rather, sent a chill down the Blood-Sword Demon Lord’s spine.

But…

*That desperate struggle ends here.*

The Blood-Sword Demon Lord bared his bloodied teeth in a grin.

If he were his former self—or even just an ordinary flesh-and-blood human—those injuries would have killed him several times over.

But his body, strengthened to an extreme degree, had granted him a brief handful of moments. Those moments would change everyone’s fate.

The Fire King and the Bow Saint, both rushing here with all their strength even now.

The tens of thousands of enemies and allies swinging their weapons amid the sea of corpses and blood.

And, most important of all, the Blood-Sword Demon Lord’s own life and death.

“It’s time… to put an end to this damned battle.”

The Blood-Sword Demon Lord spoke, his breathing visibly growing more labored. The Grand Mage nodded calmly.

“Of course.”

At that moment—

Fwoosh.

A brilliant light spread from the Grand Mage’s fingertips.

A healing light, warm as the midday sun and clear as a pond deep in the mountains.

*Ah.*

The Blood-Sword Demon Lord’s eyes closed without his meaning to.

For a moment, he let himself sink into the peace the light brought.

Then, after a moment that felt both brief and eternal, he opened his eyes.

He stared, unable to believe what he saw.

“What… is this?”

His body was still horribly mangled, not healed in the slightest.

And someone else, wrapped in the fading glow, was breathing more steadily than before.

No.

Jin Taekyung.
## Chapter artifact 1049

# Chapter 1049

In that instant, the Blood-Sword Demon Lord’s mind went blank save for a single thought.

*Am I dreaming?*

It was a perfectly natural question.

How could it not be?

The woman before him, the Grand Mage, was his ally.

They served the same master and shared the same goal.

That was why the Blood-Sword Demon Lord could hardly accept the unbelievable sight before his eyes as reality.

Not until the next moment, when the Grand Mage—who had been silently looking down at him—parted her tightly closed lips.

“Are you still dreaming?”

“…What?”

“This isn’t a dream, Demon Lord. It’s very much real.”

The Blood-Sword Demon Lord stared blankly at the Grand Mage, thinking about what her voice had just whispered into his ear.

About why this was happening.

And then, as if to prove her words—that all of this was real—the agony spreading through every inch of his body hit him. He barely managed to squeeze out a voice.

“Your joke… has gone too far.”

“A joke? I’m afraid I don’t know what you mean.”

The woman tilted her head with an innocent air. The Blood-Sword Demon Lord clenched his teeth.

Rage surged from deep in his chest, and blood welled up with it.

“Hurry. Cough. Hurry and heal me.”

“You don’t need to worry about that anymore.”

Beneath her veil, her red lips curved softly.

The Grand Mage smiled at the Blood-Sword Demon Lord, who was panting hard, then turned her head and added,

“I’ve already finished healing you.”

She was telling the truth.

It was healing in the truest sense of the word.

Not complete healing, but enough to hold on to someone’s consciousness as it slowly sank into darkness.

Hoooo.

His ragged, wheezing breaths steadied. His deathly pale face and lips gradually regained their color.

As the warm radiance surrounding the young man faded away completely, the Grand Mage’s slender fingers swept through the air.

Crack! Shhhhk!

The earth split open like a sealed box being forced apart.

At the same time, plant stems hidden deep beneath the earth surged up, coiling around the young man—Jin Taekyung—and lifting him into the air.

As if to show him to the intruders who were still rushing toward the hill at full speed.

And when Jeok Cheongang and the Bow Saint saw Jin Taekyung bound like a hostage in the distance, they had no choice but to stop. They couldn’t tell exactly what had happened.

“I’m a little sad my sincerity didn’t get through, but what can you do? This is the only way.”

The Blood-Sword Demon Lord stared blankly at the Grand Mage as she clicked her tongue softly. Only then did he finally understand.

This was no mere dream or cruel prank.

“Why?”

The question held a multitude of meanings.

But the answer that came back was brief and clear.

“Because that person wants it.”

Her silver-white veil swayed.

The Grand Mage’s eyes, faintly visible behind it, were devoid of emotion. They no longer looked at him as a subordinate might look at a superior.

Her calm voice, addressed to the Blood-Sword Demon Lord, who had gone rigid as a statue, was no different.

“You’ve had a good long life to run wild. It’s about time you got some rest, don’t you think?”

Maybe it was because his senses were slowly growing dull even now.

Or maybe it was the shock of something he’d never expected.

The Blood-Sword Demon Lord had been listening blankly to her voice echoing in his ears like a distant call when a word suddenly slipped out.

“Bullshit.”

His voice carried unmistakable exhaustion, but within it lay unshakable certainty.

The certainty that he couldn’t possibly be abandoned like this.

Even if his master had always thought of him as nothing more than a hunting dog, he wouldn’t throw him into the cauldron so pointlessly.

The old saying about cooking the hound after the hare is dead?

That only happened after the hunt was over.

But what was the state of the Lord of Heaven—of Dark Heaven—now?

The Western Heaven Demon Lord and the Southern Heaven Demon Empress had fallen. Then the Eastern Heaven Demon Lord and the North Heaven Demon Lord had fallen, too.

The four fiercest beasts he’d trusted most were gone.

The Central Plains martial world, rallied under the Murim Alliance’s banner, was no mere hare. And the Blood-Sword Demon Lord, who had survived alongside the Blood Lord, was more than a hunting dog.

The proof was that he had brought an army of tens of thousands all the way here under his command.

And that wasn’t all.

He only had to reach out a little farther—just a little—and sweet victory would be his.

If only this damned body could recover.

If he took Jin Taekyung hostage, he could handle even the Fire King and the Bow Saint.

Dominion over Gansu lay before him—a bridgehead for victory across the realm.

*And he thinks he can abandon me now?*

The Blood-Sword Demon Lord gave a hollow laugh.

Then he glared with crimson-black eyes at the insolent woman trying to drive a wedge between him and his master with such absurd lies.

“Enough of your nonsense, woman. Do you think he doesn’t know you betrayed him?”

There was no doubt about it.

The Grand Mage. That filthy traitor had ruined everything.

The only reason he was in this situation was that he hadn’t recognized the tumor growing inside his own ranks.

“Tell me, what did those deceitful bastards promise you? A grand estate? Mountains of gold and treasure? Or a stunningly handsome man to satisfy those filthy desires of yours?”

The Blood-Sword Demon Lord spat out the words, his voice boiling over.

He was angrier now than he’d ever been.

Looking back, things had seemed suspicious from the beginning.

The Grand Mage had stopped him when he tried to step into the battle without hesitation. Because of that, the Black Ghosts, their core fighting force, had been wiped out.

And even though she could use powerful spells the Blood-Sword Demon Lord himself hadn’t known about, she had refused to help to the very end.

He’d been deceived.

Thoroughly toyed with.

That unbearable truth made the Blood-Sword Demon Lord thrash about.

“You dare! Do you think a mere woman like you can kill me? Do you think you can ruin his grand plan with this little stunt?”

Crack. Thud.

From the crater left by their earlier collision, the Blood-Sword Demon Lord used every ounce of strength he had to haul himself upright.

He had lost an arm. The tendons in his leg had been severed, and his joints shattered. Even so, he still had the endurance and vitality that an ordinary person couldn’t even imagine.

But consumed by his fury, the Blood-Sword Demon Lord had forgotten the most important fact.

The reason he’d survived injuries that should have killed him outright several times over was that the Grand Mage’s Magic had been imbued in his body.

“Can I kill you? Of course I can.”

The Grand Mage watched impassively as the Blood-Sword Demon Lord crawled out of the crater toward her, then added,

“And it would be very easy.”

She was telling the truth.

She didn’t even need to use Magic against the Blood-Sword Demon Lord in his current state.

All she had to do was dispel the body-enhancement Magic she’d placed on him.

If the Grand Mage decided to kill him right now, the fiend who had once made his mark on an entire age would meet a miserable death in moments.

“But…”

The Grand Mage continued.

“You’re right about one thing. Someone like me can’t kill you.”

“…What?”

Step.

In response to the Blood-Sword Demon Lord’s reflexive question, the Grand Mage took a light step backward instead of answering.

Then, leaving the Blood-Sword Demon Lord behind as he struggled to understand what she meant, she spread both arms wide in a movement that was almost exaggerated.

“Because there’s only one person here who can kill you today.”

At that very moment—

Shhhhk.

The plant stems, now thicker and sturdier than chains, responded to their mistress’s will.

They moved as if they were living creatures with minds of their own, carrying the young man before their mistress. His eyes were closed, and he looked to be in a deep sleep.

Or rather, he looked as if he were in a deep sleep.

“Enough with the pointless act. How about you say something? If you keep lying there, you’re only going to make me more suspicious.”

The next moment—

“Fuck. If you knew, you should’ve said so sooner.”

A curse burst from Jin Taekyung’s lips, which still had drool on them. He slowly opened his eyes and fixed the Grand Mage with a sharp gaze.

* * *

I’d nearly lost consciousness.

No—maybe I really had, for a little while.

If someone hadn’t helped me when I least expected it, I’d probably be floundering in another long, endless nightmare by now.

Of course, even this situation felt like a dream.

*…Hah.*

I swallowed the laugh that was about to escape me.

Right. This really wasn’t a dream.

The wind was still fierce, and the sky was dark.

The unceasing cries of battle were growing louder in my ears. Beneath the blades they swung, life and death crossed paths.

Aside from Jeok Cheongang and the Bow Saint, staring at me with faces frozen in place, the scene below the hill was exactly as I’d last seen it.

Nothing had changed.

Nothing at all.

But the situation on this hill was different.

In this narrow space, everything had turned upside down.

Common sense, expectations, even friend and foe.

And I, who’d been listening to everything with my eyes closed as if I were dead, had no choice but to ask the woman before me—the Grand Mage—

“You… No. What exactly are you thinking?”

I still couldn’t understand.

Why she’d healed me.

Why she was trying to finish off the Blood-Sword Demon Lord when she had the power to restore him to full health right now.

“Answer me. Come on.”

I glared at the Grand Mage, my eyes burning.

I wanted to break this binding Magic right now and grab her by that pale throat. But I didn’t have the strength for that.

All I could do was barely cling to my fading consciousness and move my limbs a little more freely than before.

That was all the healing power inside me was meant to do.

The Grand Mage spoke to me in a calm voice.

“That’s a shame. If I were you, I wouldn’t waste what little strength I had on questions like that.”

“What?”

“Your question is wrong. This situation isn’t happening because I chose it.”

“……!”

As soon as I grasped the meaning of her words, my eyes widened.

“…You mean?”

“You’re thinking along the right lines. A hunting dog only ever does its job. It follows its master’s orders.”

The Grand Mage calmly answered, then pointed at the Blood-Sword Demon Lord and continued,

“And when its job is done, it’s no longer needed.”

Her words were so cold they sent a shiver down my spine.

The Blood-Sword Demon Lord had done his best to deny it. Anyone would have. But now he was facing a truth so shocking that it seemed impossible to deny, his eyes staring at her as if his soul had left his body.

“Why…?”

That was the question I wanted to ask, too.

Why? For what reason was the Lord of Heaven abandoning the Blood-Sword Demon Lord?

How could he so casually throw away this crucial battle, one that could determine the outcome of this enormous war?

But the Grand Mage didn’t answer.

Instead, she gazed at me with an inscrutable look and slowly parted her lips.

“You can’t fall here. You have to get stronger.”

“What… did you say?”

“Kill him. And then…”

Her lips, red as blood, moved beneath the veil.

“Get stronger.”

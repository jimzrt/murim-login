# Checkpoint Review — 1035–1039

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

# Chapters 1035–1039

## Plot

Jin Taekyung identifies Magic behind the strange phenomena and the Blood-Sword Demon Lord’s surges in strength. After the Demon Lord charges the seriously injured Jeok Cheongang, Jin heads for the white-robed mages, hoping to cut off their support. Jeok holds the Demon Lord back while Jin fights So Gunak, the last Black Ghost, and more than a hundred Peak masters. As the defenders grow stronger and Jin is wounded and outnumbered, he summons Fire Dragon Armor and charges.

Meanwhile, Sama Pyo risks his life rather than dodge an enemy’s Sword Energy into an ally. A young Black Dragon Demon Gate martial artist dies saving him. Sima Gong arrives with the Gate’s elite; Sama Pyo confronts him over his delay and his choice to follow a different path from his father. Sima Gong recognizes the dead young man as one of two men he had ordered into the front line, where both died.

## Continuity

- The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.
- Jeok Cheongang is seriously injured but holds off the Demon Lord while Jin Taekyung targets the mages. Jin asked Jeok to hold out for half a quarter-hour.
- The white-robed mages’ Magic empowers the Demon Lord and appears to increase the strength of So Gunak and the other defenders. A Grand Mage may be among them; none has yet used a battlefield-wide attack.
- So Gunak is the last Black Ghost. He and more than a hundred Peak masters fight Jin as he tries to reach the mages. Jin summons Fire Dragon Armor as he charges.
- A young Black Dragon Demon Gate martial artist dies saving Sama Pyo. Sima Gong had ordered him and another man into the front line; both died there.
- Sama Pyo says the Black Dragon Demon Gate will survive regardless of the battle’s outcome.

## Translation Decisions

- Render 마법 as “Magic”; keep “mage” and “Grand Mage” distinct.
- Use “sorcerers” only when it is the Blood-Sword Demon Lord’s label for the mages.
- Keep “Black Ghost,” “Black Dragon Saber,” “White Flame,” “Force,” and “Will.”

## Durable state

{
  "active_continuity": [
    "The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.",
    "Jeok Cheongang is injured but holding off the Blood-Sword Demon Lord while Jin Taekyung targets the mages.",
    "The mages’ Magic empowers the Blood-Sword Demon Lord and is increasing the strength of So Gunak and the other defenders.",
    "Jin Taekyung is fighting So Gunak, the last Black Ghost, and more than a hundred Peak masters to reach the mages.",
    "Jin Taekyung summoned Fire Dragon Armor as he charged into the defenders."
  ],
  "continuity_sources": [
    1038,
    1039
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who are the white-robed mages, and what is their purpose?",
    "How were the former Demonic Cult fiends made into Black Ghosts?"
  ],
  "safe_through": 1039,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1035

# Chapter 1035

Ding. Ding. Ding.

The clear chime rang in my ears, and at that very moment, new vitality welled up from deep within me, accompanied by System notifications proving the results of my actions.

> **System**
>
> Defeated Lv. 152 Go Gwangryung!
>
> Defeated Lv. 150 Jeok Hwanyang!
>
> Defeated Lv. 155 Pung Sogwi!
>
> Defeated Lv. 160 Hwang Dokso!
>
> Acquired a massive amount of EXP and Fame!
>
> Level Up!
>
> The effects of leveling up have restored all energy, cured all status conditions, and healed some injuries!

Shaaah.

Was this what it felt like to wash all the way down in a cool mountain stream on a sweltering summer day?

I took a deep breath, feeling the exhaustion built up over that brief but fierce clash melt away all at once.

Whew.

But this wasn’t a sigh of relief at having taken down four Black Ghosts.

It was just a breath to steady my body and mind as I waited for the person who hadn’t fallen yet—the person I had to defeat if we were going to win this battle.

“Old Master.”

“Yeah.”

Jeok Cheongang nodded at my brief call, then continued.

“He’s coming.”

At that moment—

Clack, clack, clack.

The Dark Heaven followers, who never seemed to grow fewer no matter how many we killed, had been closing in around us without so much as a pause after the Black Ghosts’ end. Now, those fanatics stopped in unison.

Then, with grave, orderly movements, they opened a path.

A path for just one person.

Step. Step.

“My apologies. I’m later than I intended.”

His footsteps and calm voice carried clearly, even from a distance.

I shrugged at the Blood-Sword Demon Lord.

Thump.

I kicked the remains of what had been called Black Ghosts—now scattered into dozens of large and small fragments.

“If you’re sorry, go kill yourself.”

“That would be difficult.”

“Figured. Anyway, I’m fine. I was playing with your friends.”

“Friends? If you mean those piles of trash lying over there, then I think you’re mistaken.”

“Trash?”

“They were all hopeless. During the Great Faction War, they either ran wild like reckless fools who didn’t know their place and got themselves killed, or failed to recognize the true Heaven and raised their swords against it.”

His words brought something to mind.

The Black Ghosts who had appeared here today—the Death Knights—and what they had been in life.

“They were Demonic Cult fiends. You used to share a bowl with them.”

The Blood-Sword Demon Lord nodded readily.

“Once, yes. A very long time ago.”

I’d suspected as much.

Everything that came into being had a cause to match. It was obvious that making Death Knights of this caliber required materials of comparable stature.

“No wonder. Even just from their names, they sounded like a bunch of lowlifes.”

“Their names?”

“Go Gwangryung, Jeok Hwanyang, Pung Sogwi, Hwang Dokso… Those aren’t names that could come from a normal person’s head. Don’t you think?”

The names came tumbling out without a moment’s hesitation. The Blood-Sword Demon Lord looked at me with surprise.

“That’s strange. How do you know their names?”

“What, weren’t they famous? Just hearing those names puts me in a bad mood. Makes it pretty obvious what kind of lives they led.”

“Of course they were once known throughout the Central Plains. But only by their sobriquets. Still…”

The Blood-Sword Demon Lord looked between Jeok Cheongang and me before adding, “A martial artist is known by their martial arts and sobriquet, not their name. Even back then, very few knew those men’s real names. Even with someone who’s spent many years gaining experience at your side, you couldn’t have learned those names.”

There was certainty in his voice.

And for good reason. Xinjiang, the Demonic Cult’s stronghold—and now Dark Heaven’s home—had been that way since time immemorial.

A Land of Ruin no one could enter without permission.

A religious state beyond the desert, where even the Hidden Shadow Pavilion had managed to lift the veil only a little after long and meticulous preparations.

But I was different.

Even if it was only in fragments, I had the ability to read information that no one else knew.

As long as the target was right in front of me.

And if the gap between my own strength and abilities and my opponent’s wasn’t too great.

Shaaah!

At that moment, a blue circle I couldn’t see swallowed up the space around us in a flash of light, responding to my will.

Qi Sense, now nine-tenths mastered, spread out from me, washing an area with a radius of more than fifty *jang* in blue.

Ding. Ding-ding-ding.

Countless System windows appeared over the heads of the hundreds—no, thousands—of enemies within Qi Sense’s range.

But my gaze stayed fixed on one person alone.

The Blood-Sword Demon Lord, who had abruptly stopped walking the moment Qi Sense activated.

> **System**
>
> Lv. 170 Chuk Banghyeol

I could make out the Level window above his head clearly, even from more than twenty *jang* away.

I could also see his face, brow furrowed in confusion.

“What in the world did you just—”

The term Qi Sense didn’t belong to me alone. It was routine for martial artists who’d reached a certain realm to gauge and read their own and their opponents’ energy.

But Qi Sense, as part of the System, felt different from theirs.

“What did you do?”

His voice was lower than before, his tone suddenly cold and barren.

But I only curled the corner of my mouth at him.

“Our Banghyeol’s got a lot of questions. Is it because you’re still in your prime?”

“……!”

“Oh, was that name a secret, too? What do you fiends have to hide so much for?”

Jeok Cheongang, who’d experienced my Qi Sense back when we first met in Shanxi Province, clicked his tongue before chiming in.

“You may not know this, but that thing feels pretty damn unpleasant. Even I thought I’d been hit with some bizarre dark art the first time.”

“But he’s a fiend, isn’t he? Wouldn’t dark arts be familiar to him?”

“Well…”

Jeok Cheongang studied the Blood-Sword Demon Lord’s rigid face, then answered.

“Maybe he’s embarrassed. Even without hearing the whole thing, it doesn’t sound like a very good name. It’s a person’s name, and yet it’s Banghyeol. Banghyeol? Sounds like a fart.”

“Come on. Even if you’re old enough to have shoved your years up your ass, you can’t make fun of him for that. That man’s probably almost a hundred himself.”

“You wait till you’re old. Sometimes you feel strange for no reason at all. Who knows? Maybe that man sits beneath the moon every night with tears in his eyes.”

“Oh.”

The idea that the infamous great fiend had belatedly entered menopause was pretty interesting. But the next words out of the Blood-Sword Demon Lord’s mouth were enough to make my face stiffen.

“You’re right, Blazing Flame Divine Dragon Jin Taekyung.”

“What?”

“Didn’t you just say it yourself? That dark arts ought to be familiar to him.”

As if trying to recall the lingering sensation from my Qi Sense, the Blood-Sword Demon Lord gazed down at his hands before speaking again.

“I see. It’s a little different from what I know, but still quite familiar.”

“……!”

My eyes widened before I could stop them.

Different, but familiar.

The meaning behind those few words—and the source of the vague anxiety welling up somewhere in my heart—was slowly becoming clearer.

“At first, I was surprised. Now I finally understand why that person watched you so closely.”

Step. Step. Splash.

Crossing the dry, frozen ground, the Blood-Sword Demon Lord finally stepped into a pool of blood on the ground.

Plip.

Blood splashed with his roughened stride.

A powerful energy covered the slowly rising blade, thicker and more viscous than the blood itself.

“But this time, that person’s judgment was wrong. I should have handled this myself from the start. There was never any need for anyone to dissuade me or worry.”

Wooooong.

At that moment, I sensed something changing around the Blood-Sword Demon Lord.

It wasn’t because the wind had stopped or the air was trembling.

It wasn’t even because the sword in his grip was roaring and spewing out an immense Force.

Beep.

> **System**
>
> Lv. 175 Chuk Banghyeol

“……!”

It had changed.

The energy he was giving off. The number in his Level window.

*This is…*

I knew instinctively.

The Blood-Sword Demon Lord hadn’t simply been hiding his power with Returning to Simplicity.

*He definitely, definitely wasn’t this strong before.*

We’d already clashed once before the full-scale battle began. I, Jeok Cheongang, and the Blood-Sword Demon Lord had all fought at full strength. There was no doubt about the result: he had been at a disadvantage.

So why?

Beep.

> **System**
>
> Lv. 178 Chuk Banghyeol

How?

Beep.

> **System**
>
> Lv. 180 Chuk Banghyeol

How could he, the Blood-Sword Demon Lord, keep growing stronger even as he slowly approached us?

“What in the world… what kind of dark arts are you using?”

There was no way a master wouldn’t feel what his Disciple felt.

And the obvious question that slipped between Jeok Cheongang’s lips shed light on the anxiety swelling within me.

*Dark arts.*

A dark, devious technique, just as the words themselves meant.

Those who practiced such arts strayed from the righteous path, and were called practitioners of demonic, heterodox arts. As for those who dwelled in the deepest abyss among them, people called them—

The Demonic Path.

People who rejected the human way of life and chose the path of demons.

Then what should we call the dark arts they wielded, filled with inexplicable and mysterious power?

How had those beings known as Black Ghosts come into existence, and appeared here?

“……No.”

“What?”

“It’s not dark arts.”

I suddenly parted my lips and murmured, my voice dazed.

Jeok Cheongang’s repeated questions grew distant, like echoes. For a moment, I even forgot the Blood-Sword Demon Lord’s presence, growing stronger with every step he took toward us.

As if entranced, I looked at the white-robed figures.

They’d been obscured by the Blood-Sword Demon Lord’s presence until now, a tiny part of this vast battlefield where the fight was still raging.

No—their power was just as impossible in this world as that of the Black Ghosts.

“Magic.”

And at the moment that one word, so familiar and yet so unbelievable, slipped from between my lips—

“Power of the Wind Ghost.”

Far away, a chant rang out clearly.

“Take root in him.”

A spell imbued with intent manifested in the Blood-Sword Demon Lord’s body.
## Chapter artifact 1036

# Chapter 1036

Had I been unable to guess from the start, or had I been trying so hard to deny it because reality was that hard to believe?

This time, at least, I could answer that question for myself.

*I think it was the latter.*

*It was true. All of it.*

The realization struck my mind, now as white as a blank page.

At the same time, I felt the last shred of faith I’d held in my heart crumble, along with everything I’d thought I knew about this world.

The strange Moving Formation, whose existence had already been revealed long ago in Henan and Sichuan.

The Water God Dragon and countless Blood Fish, corrupted by something in Hubei and sent into a rampage.

An utterly ordinary fisherman who’d eaten those Blood Fish and gained monstrous strength and an equally monstrous appearance.

The cause of all those phenomena—and not just that, but the rift that had appeared once more in the jungles of Nanman.

And the familiar beings called Black Ghosts, whom I’d come face-to-face with right here today.

And.

And…

At last, everything came into focus.

In this very moment, it was laid out before my eyes for all to see. It pierced my ears and flowed clearly through my senses.

All those portents, signs, and omens that had come before.

Whatever you wanted to call them, all of them had finally burst through a colossal dam and swept over me.

Turning the suspicion I’d only toyed with in my heart into certainty.

With one word:

Magic.

Shaaah.

The wind blew. A shadow with speed and power far beyond human limits glided toward me, leaving a long afterimage.

But I couldn’t even twitch a finger.

In a world gone slow, with my whole body feeling as if the blood in it had turned cold, all I could do was stare, dumbfounded.

*What is this…?*

Where a massive bomb had exploded, nothing remained but ruins and the shock wave.

And in my mind, now little better than those ruins, words and question marks scattered in every direction in the wake of the blast.

Magic, mage, monster, Blood-Sword Demon Lord, buff.

A large-scale attack spell and the sacrifice of our allies. Countless deaths and blood overflowing in every direction. Mangled corpses floating among it all.

How could this be possible?

How had it come to this?

And finally—

*What am I supposed to do now?*

Everything scattered through my mind. I was left alone with a question I couldn’t answer.

Then—

Grab.

A hard, rough hand—familiar, too—landed on my shoulder.

No. The instant I felt it, a powerful force had already dragged me backward, sending me stumbling without strength.

Only then did I realize that time had begun flowing again—and that a streak of light had been swung like lightning through the gap.

Whoooom—KABOOM!

A roar like the sky splitting apart, and my senses returned.

Somewhere in the air behind me, I was already soaring, caught up in a weightless sensation. The enormous shock wave hit me along with it.

KRRRACK!

The earth flipped as if in an earthquake. Two immense forces melted and crushed everything around them.

At the center of that tremendous clash, which had swallowed an area dozens of *jang* across, Jeok Cheongang had shoved me aside when I froze like a statue and stepped in to stop the Blood-Sword Demon Lord.

“Gah!”

How had I flown so far?

Even so, I could tell that Jeok Cheongang’s shout, backed by his profound internal energy, wasn’t just a battle cry.

*He’s shouting at me. Trying to bring me back to my senses.*

The shout reached my ears and jolted my half-dazed mind awake. Only then could I let out the breath I’d been holding.

*Right. It’s not over yet.*

I still couldn’t understand how something like this could happen in the real world, but what did that matter when death was right in front of me?

There was no use in understanding when the water had already spilled.

Here on this battlefield, all I could do was accept reality and find a way through it.

And that was how I’d save everyone.

Slip.

Still feeling weightless, I smoothly twisted my body.

The muscles and internal energy I’d fully recovered after that last Level Up carried out the order from my mind with perfect speed and precision.

*Now.*

Boom—shwaaash!

I stepped on the air with a qi-charged foot and shot forward like an explosion, toward Jeok Cheongang, clashing with the Blood-Sword Demon Lord twenty *jang* away.

No—that was what I meant to do.

Until a tremendous invisible force came crashing down on me as I cut through the wind.

Wooooong.

The air vanished. The wind vanished.

And as soon as I realized it, I heard a voice ringing faintly from far away.

“Taishan.”

“……!”

My eyes widened as I recognized the meaning behind that quiet voice. But there was nothing I could do to stop it, coming from a hill fifty *jang* away, beneath the pure-white veil of a woman dressed in white.

“Bring him down. Crush him.”

At that very moment—

Fwooom!

A weight as immense as Taishan pressed down on my whole body.

No—it made me fall.

Down through the ranks of countless enemies, who’d gathered like clouds during the brief moment I’d been airborne and aimed their spears and bows at me.

*Gravity magic…!*

I swallowed the cry of shock that was about to slip through my lips.

And instead of resisting this unexpected spell, I let it take hold and turned it into a weapon.

KWA-BOOM!

I came crashing down with the weight of ten thousand *geun*. The ground split, and the enemies around me staggered, losing their balance. At the same time, I felt the crushing pressure around me naturally disperse.

*Of course it did.*

Gravity acted on a space, not on a specific person.

I’d been the first to feel its effects while I was airborne, but once I landed, that changed.

The white-robed figures were clearly mages. If they wanted to bind me even a little, their gravity magic would have to target the Dark Heaven followers who were their allies, too.

So they were trying to delay me from joining Jeok Cheongang, even if only for a moment…

*Fine by me.*

The enemies staggered like lifeless wooden puppets. I turned in place and swept the White Flame in my hand across them.

KWA-AAAH!

The sound of the spear cutting through the air was more than fierce—it was destructive.

A horizontal strike was a simple attack anyone could perform. But none of the enemies surrounding me could stop the wave of Force bursting from White Flame’s translucent spearhead.

Not one of them.

SHHK! KRRRACK!

Everything was cut apart and crushed.

Weapons and people alike.

In the blink of an eye, the ground within a three-*jang* radius had become a field of death. Yet the fear had been stripped from them. They stared at me with dark, unseeing eyes and kept charging.

As if bewitched, they murmured the eight words of their creed.

“Heaven above, earth below.”

“All demons bow.”

“Heaven above…”

CRUNCH!

A body without a head toppled over. The spearhead swung again, flashing sideways through three enemies approaching from the side.

SHK!

Neither a weapon imbued with Sword Energy nor a body trained in the external arts was enough against overwhelming force.

I pressed forward without hesitation, piercing through the fragments of steel and flesh that scattered around me.

I streaked like lightning between the enemies blocking my way like a wall, thinking and commanding without pause.

*Open Inventory. Summon. Summon. Summon.*

SHHK, THUNK, KRRRACK!

I cut, stabbed, and crushed without holding back.

The weapons that had rested briefly in my hands disappeared after devouring one, or two or three, lives. And countless blades still lay hidden in the vast subspace, too immense to measure.

For a moment, the thought crossed my mind that perhaps I could make some ridiculous idea real.

*No. There’s no way.*

But why?

CLANG!

I knocked away the weapons slashing at me from every direction.

THWACK!

I crushed an enemy’s head with one punch as he approached from my blind spot.

SHWEEESH—SHHK!

The more I cut down the enemies in front of me, the stronger this inexplicable certainty grew.

*Could this really be nothing more than a fantasy?*

SHWAAASH!

Blood scattered along the arc of my spear as I turned and swung it.

I took a quick breath as I watched the enemies surge in from every direction to fill the gap left by the dead.

*I don’t know until I try it myself.*

Now that I thought about it, it had always been that way.

Every time I needed to break through a wall, I had to go beyond it. I had to make the impossible possible, turn imagination into reality.

Just as I would now.

*Open Inventory.*

The time it took to exhale once. That was all I needed.

Leaving behind the countless enemies who blocked my way, endlessly filling every empty space no matter how many I killed, I quietly closed my eyes and pictured the mountain of gleaming, razor-sharp steel somewhere inside the void called the Inventory.

Then, at last, I gave the command.

*Summon.*

It was certainly insane. Something that could only exist as an idea.

But even in response to that absurd, desperate call, the System answered.

In its own familiar way.

Ding.

One small, clear chime.

Ding. Ding. Ding-ding.

The chimes piled on top of one another. Their faint ripples became a wave, and the wave swallowed the space around me.

Ding-ding-ding-ding-ding!

My ears grew muffled. This was the first step toward making imagination real.

I opened my eyes to a chime so vast and majestic I’d never heard anything like it.

And saw.

Shaaah.

Something looming over my head, forcing its way through a gap in unseen space and casting darkness below.

I also heard.

Shrring.

The cold ring of hundreds of pieces of steel sliding against one another.

And finally—

*I can do this.*

I felt it. I understood.

The possibilities within me, the limits I’d been given, were far higher and more distant than I’d imagined.

I had the power to turn that ridiculous idea I’d just pictured into reality—at least in part.

Fwoosh.

In the slowed world, an immense force surged up from deep within me.

The fire dragon coiled in my lower dantian flowed into every limb and bone. My blood surged faster, following the pounding of my heart.

Thump. Thump. Thump.

A fierce tremor. My heart pounded sharply.

*No. That’s not it.*

Right. That beat wasn’t coming from my heart alone.

The Jade Hall Acupoint.

What the people called martial artists had newly named the Middle Dantian.

At this very moment, all my senses and nerves were focused there.

Past the lower dantian, where lava rolled in waves, up to that lofty peak that reached toward the heavens.

Into a realm of Will that couldn’t be measured by strength or speed.

Kiiiiing.

My vision blurred. A sharp pain stabbed through my head, as if someone were driving a needle into it.

But as if possessed, I spread both arms.

In the flash that filled my vision, I felt a thrill greater than the pain. My hands were empty, holding nothing—but beyond the realm of touch, I traced and grasped each and every thing.

One, two, three.

Ten, twenty, thirty.

And at last…

*One hundred.*

I opened my eyes.

In that time that had felt like eternity, yet lasted no more than an instant.

Beneath a mountain of sabers and a forest of swords—a hundred blades aimed at countless enemies as if held by an invisible hand.

And then, I parted my tightly closed lips.

“Move.”

SHWAAAAASH!

The sky filled with flashes of light.
## Chapter artifact 1037

# Chapter 1037

Sama Pyo suddenly wondered.

Where was this place? Who was he?

And what was he supposed to do, with enemies pouring in without end even now?

Thwack!

His body moved on instinct, and his saber cut through an enemy’s neck. But Sama Pyo already knew.

Even if he cut down dozens, even hundreds, tens of thousands of enemies would remain behind them.

His strength was far too meager to turn the tide of this disadvantageous battle.

Clang! Krrr-crack!

“Argh!”

“Gah…!”

Horrifying screams rang out from every direction.

No—more precisely, only their allies were screaming.

Standing at the center of the front line as it rapidly began to crumble beneath an endless spray of blood, Sama Pyo read the future about to unfold.

*At this rate… everything is finished.*

His body was soaked in exhaustion, but his mind was colder than ever.

That was why his judgment was clear and precise.

When two forces of roughly equal size clashed, the quality of their troops and their momentum ultimately decided the victor.

In that regard, Dark Heaven’s army was superior to their own in every way.

*We have half an hour at most. No—fifteen minutes. The front line will be completely broken by then.*

Sama Pyo quietly swallowed the words that would have filled anyone in his army with despair, then charged at another enemy.

He thought of Jin Taekyung, who had plunged deep into enemy territory and was now hidden from view by a sea of enemies.

And he poured out his anger and resentment at himself for barely managing to hold the line, let alone follow him.

Slice!

One clean strike cleaved the enemy’s upper body in two.

Beneath the shower of blood, a young martial artist who’d been trembling, already certain he was about to die, lit up with relief.

“Th-thank you… Huh?”

His eyes were wide, his voice dazed.

The young man looked barely twenty, and just as he recognized Sama Pyo at once, Sama Pyo recognized the Black Dragon Demon Gate uniform he wore.

The young man also seemed strangely familiar.

*Where have I seen him before?*

But the question only flickered through his mind. A moment later, Sama Pyo hurriedly twisted around and swung his saber.

Whish—Kkakak!

Sword Energy tore through the air and slammed against the blade of his saber.

The eyes reflected between the weapons were vacant as a corpse’s, but the Sword Energy gleamed bright and sharp.

Sharper than Sama Pyo’s own.

*A master…!*

It had been a brief clash, but the considerable difference in their strength was enough to travel through Sama Pyo’s skin and into his bones.

There was just one thing he hadn’t noticed in that moment.

Crack.

His saber had already grown too fragile to withstand the enemy’s fierce Sword Energy—a testament to the enemy’s mastery of the Peak realm. It had been battered and dulled by colliding with dozens of enemies already.

KWA-CLANG!

The brief but fierce clash came to an end.

A broken half of Sama Pyo’s blade spun high into the air, and a streak of light shot straight toward its target.

*Danger!*

The moment he saw that devastating flash, a red alarm blared in Sama Pyo’s mind.

At the same time, instinct whispered ahead of reason.

*Get out of the way.*

*Survive, whatever it takes. No matter how disgraceful you have to be.*

But…

*Where am I supposed to dodge?*

Time seemed to slow as if his life were flashing before his eyes. Sama Pyo could sense everything around him, clear as day.

Clang-clang! Thud!

“Gaaah!”

The ceaseless clash of blades. Blood scattering uselessly through the air, followed by dying screams.

And, even in this desperate situation, his allies standing shoulder to shoulder, packed so tightly that they brushed against one another, as they faced the enemy.

Sama Pyo could clearly sense the tremor in their breathing. And at the same time, he knew:

*There’s… nowhere to run.*

No. That was wrong.

There were plenty of ways he could dodge.

He could dart to either side right now, or duck and roll to avoid as much of the enemy’s Sword Energy as possible.

A Narye tagon?[^1]

Who cared? In the face of death, dignity was a luxury.

Even if he ended up covered in filth instead of blood, even if he used one of his allies as a shield, surviving was the way of the unorthodox faction.

Use any means necessary.

That was what his father, the Black Night King Sima Gong, had taught him—the man who’d passed his blood down to him.

*Yes. That’s what he taught me.*

But not anymore.

One year.

In that brief time, the son had stepped out from beneath his father’s deep shadow, which had hung over him all his life. He’d met many people, experienced a great deal, and changed.

That was why, at this moment, Sama Pyo could see no way out.

He could have dodged, but he couldn’t.

Even in this frozen moment, if he avoided the Sword Energy slowly stretching toward him, one of his allies would surely die.

*What a damn mess.*

The curse circled soundlessly on the tip of his tongue.

But Sama Pyo didn’t notice the faint smile that had formed at the corner of his mouth.

Nor the strange relief he felt as he watched death rush toward him.

He launched the dagger he’d hidden under his sleeve, thinking that if the person who’d suddenly come to mind were watching, they might even praise him for this.

*Not a bad way for an unorthodox punk to go, don’t you think, Pavilion Master?*

Sama Pyo smiled brightly.

At the same time, he felt the enemy’s Sword Energy grow even fiercer. It swallowed the dagger flying toward it and surged toward his chest.

He also heard two unexpected, sharp whistles cutting through the air.

Slice! Thud!

Sama Pyo stared with wide eyes.

At the very last moment, when he’d sensed his end, someone had leaped in front of him.

A blackish-blue saber blade passed over the shoulder of the man who staggered, blood spraying from his chest, and pierced the enemy’s throat.

*This is…*

Sama Pyo recognized the familiar blade at once.

And the owner of the Force within it: the same Force that dwelled in his treasured weapon, the Black Dragon Saber, which he’d left behind before the meeting with the Blood-Sword Demon Lord.

“You fool.”

The voice was chillingly familiar—and yet one he could never grow used to.

Thwack!

The warped blade of the Black Dragon Saber finished cutting through the enemy’s neck. Then black Force rose like a spreading wildfire and swept across the front.

KRRR-CRACK!

A fierce blood-red gale engulfed dozens of enemies. The allies who witnessed that overwhelming display of martial might cried out, one after another.

“L-Lord!”

“The Sect Leader is here!”

That was exactly right.

The Black Night King, Sima Gong.

The great tree that supported the unorthodox Murim had finally appeared on the front line, together with the elite martial artists of the Black Dragon Demon Gate under his command.

“Attack.”

The short command slipped through his tightly closed lips.

Whoosh-whoosh-whoosh! KABOOM!

Dozens of Peak masters plunged into the enemy ranks.

Cheers erupted here and there at the sight. And in that moment, not one of the allies holding the front line dared to wonder:

Why had he only appeared now?

Why had he remained in the rear until now, despite having plenty of time to join them?

But one person was the exception.

“You’re late.”

The son did not look at his father, whom he’d met on the battlefield.

Sama Pyo’s gaze was fixed on the corpse of the person who’d just thrown himself in front of him.

It was the young martial artist he’d saved once before, the one who still looked as if he hadn’t lost his baby fat.

His father followed his gaze and glanced at the corpse. His reply was cold.

“He died because you were weak.”

“That’s right. If I’d been stronger, he would’ve lived.”

Sama Pyo nodded calmly.

Then he spoke without restraint.

“Then what were you doing, you who are so strong?”

“What?”

“The monsters called Black Ghosts never came this way. If you’d brought your forces here in time, I think we could’ve broken through the enemy lines.”

Why hadn’t the Black Ghosts appeared?

Why hadn’t they targeted this place, when Sima Gong’s thirty-thousand-strong army was the key force on this battlefield?

And why had he stood by and watched this perfect opportunity pass?

His father’s gaze sank deep as he looked at his son, who’d given voice to the questions everyone else had momentarily forgotten.

*What are you trying to say?*

At the sudden Sound Transmission in his ear, his son gave a quiet laugh.

*What, are you afraid there are too many ears listening?*

*How dare you…*

*I’d already guessed you had other plans. But I didn’t want to believe it. I kept hoping I was wrong.*

His son—no, Sama Pyo—drew a deep breath.

*You’re still my father, after all.*

*……!*

*Do you still not understand why I volunteered for a place that was practically a death sentence?*

Sama Pyo had known instinctively.

His father was already harboring other intentions.

If the heir who would inherit everything he’d built over a lifetime hadn’t been in danger, he wouldn’t have shown up here now.

“But please, don’t worry. No matter how this battle ends, the Black Dragon Demon Gate will survive.”

For the first time, the son chose a path different from his father’s, then turned away without hesitation. Before charging at the enemy, he offered one last parting remark—perhaps the last he’d ever have the chance to make.

“It looks like the other one is already dead. Unfortunately.”

The son left those words, whose meaning was unclear, and was gone.

The father stayed behind.

When Sima Gong’s gaze, still frozen like a statue, finally settled on the fallen body, he suddenly remembered a middle-aged man and a young man from several days earlier, as they crossed the desert. They’d dared to speak of the Black Dragon Demon Gate’s and Sama Pyo’s hidden history.

And the command he’d given that had decided their fate in an instant.

*“See to it as you see fit.”*

His command had been carried out properly.

They’d been placed in the front line, the most dangerous position.

And, at last, both men had met their deaths.

But the Black Night King, Sima Gong, didn’t know.

No—no one could have known.

That a young man whom a cold-hearted father had sent to his death would save his son.

“……What a cruel twist of fate.”

Sima Gong murmured quietly, then looked down at the Black Dragon Saber in his hand.

The treasured blade he’d given his son as his first and last gift now reflected an old man with a troubled look in his eyes.

At that very moment, it also reflected a flash of light erupting far in the distance.

* * *

It was like a lightning bolt.

Lightning falling without end, tearing and burning everything beneath it with irresistible force.

But everyone staring wide-eyed at the scene unfolding in the distance knew, at that moment.

They knew through the heightened senses of their entire bodies, through the instincts and common sense of martial artists.

The countless flashes of light bursting across the battlefield weren’t ordinary bolts of lightning.

They were just like the blades in their own hands.

Fwoosh!

Dozens of brilliant streaks of light tore through the darkness beneath the heavy clouds.

They moved freely through the air, like living things, sweeping over beings that could no longer be called alive because they felt nothing.

KRRR-CRACK!

Instead of screams, a terrifying crunch of flesh rang out.

The weapons had been forged in the lands beyond the desert, through hundreds of rounds of tempering. The moment they met the steel wave, they shattered into pieces—and their owners’ bodies were no better off.

Splash. Thud-thud-thud!

Blood surged up like a wave.

Beneath that red rain, bursting from the bodies of dozens and soaking the ground, one man slowly walked forward.

Squish.

Sticky. Blood pooled up to his ankles and sloshed with each step. Its foul stench seeped into his nose.

But even with blood covering him from head to toe, Jin Taekyung kept walking forward.

Along with the enormous steel wave under his sole command.

Clack. Thud-thud-thunk!

A clattering sound rang out, followed by a whistle through the air. At the same moment, Jin Taekyung’s fingers moved slightly.

Clang!

Five great sabers floating through the air spread their broad blades to shield his flank.

Like petals in full bloom, the steel shield opened wide, blocking the arrowheads that came flying at him in quick succession. It all happened in the blink of an eye.

Kakakakclang!

A dozen arrows bounced away in showers of sparks.

But Jin Taekyung didn’t flinch at the sudden ambush.

He’d already made the space within a three-*jang* radius his own.

And whoever had hidden among their many allies to fire that repeating crossbow wouldn’t get the chance to spring another ambush.

*Go.*

He didn’t need to turn and check the enemy’s position.

Jin Taekyung gave the command. The five great sabers that had served as shields instantly became enormous arrows and shot away.

Thud-thud-thud!

In the time it took to exhale once, more than twenty lives disappeared.

The enemy who’d fired the repeating crossbow, and the other enemies who’d stood in the path of the flying sabers or lingered nearby.

They all died.

But the five sabers didn’t return, either.

Even Jin Taekyung had clear limits when it came to hurling steel weighing dozens of *geun* each like lightning.

Grit.

A terrible headache abruptly seized him. Jin Taekyung clenched his teeth in silence.

*Was that too ambitious?*

Unlike the Lower Dantian, the Middle Dantian was a domain of Will, which meant mental strength.

Just controlling this many weapons was nothing short of a miracle. But imbuing every single one with internal energy and controlling them perfectly was another matter.

A master who’d reached a certain level could block weapons that relied on nothing but force and speed.

Just as they were doing now.

Thud! Kakakakclang!

Weapons shot forward again at Jin Taekyung’s command, piercing flesh and bone.

But in the time it took them to cross a distance of barely ten *jang*, the number of blades that had once been close to a hundred had been cut in half. Some of the enemies who’d reached the Peak realm were beginning to deflect them without much trouble.

*Not yet. Not yet.*

Since the battle began, he’d already taken down hundreds of enemies alone.

No—perhaps more than a thousand.

An incredible feat, worthy of being called One Against a Thousand.

But…

*It’s not enough.*

Jin Taekyung knew.

The deeper he went into enemy territory, the closer he got to Jeok Cheongang fighting the Blood-Sword Demon Lord, the stronger the enemies became.

To cut down every enemy still surging toward him, he had to unleash everything he’d been given.

*Just one. One strike is enough.*

The instant the thought arose in his mind and took shape as Will—

Slip. Clang-clang-clang!

The dozens of weapons surrounding Jin Taekyung fell from the air.

All except one spear, which had held more blood than any of the other blades and still hadn’t lost its gleam.

*Now.*

Fwoosh.

White Flame, wrapped in Force, flared to life in the wavering space and shot forward.

At the end of that fierce streak of light, which tore through a human wave numbering in the hundreds, stood one man.

KWA-BOOM!

With a roar like the sky splitting apart, a figure was driven backward by the immense force carried in the spearhead.

The Blood-Sword Demon Lord had been rushing toward Jeok Cheongang, who was already drenched in blood.

Now, he bared his bloodstained teeth at Jin Taekyung, standing in a red path where enemies had been chopped into tiny pieces of flesh.

“So, you’ve come?”

[^1]: A humiliating idiom comparing a fighter’s evasive roll to a lazy donkey rolling on the ground.
## Chapter artifact 1038

# Chapter 1038

It was probably because of the Middle Dantian’s ability, which I’d pushed beyond its limits.

Step.

The dead and the living.

The moment I stepped onto that blood-red path, with everything else evaporated away, an agonizing headache unlike anything I’d ever felt before came crashing down on me.

*Hup.*

A pain like a long, sharp needle probing around inside my skull.

But I gritted my teeth and held back a groan, doing my best to suppress my trembling body with every ounce of strength I had.

If I showed even the slightest weakness in front of a beast that had already bared its fangs, it would devour me on the spot.

“So, you’ve come?”

The Blood-Sword Demon Lord.

The moment I heard his utterly unruffled voice, my headache swelled twice as strong.

No—or maybe the real reason was the sight of Jeok Cheongang, now drenched in blood.

Or perhaps…

> **System**
> **Lv. ???**
> **Chuk Banghyeol**

Maybe it was because I’d confirmed the strength of the Blood-Sword Demon Lord—a true monster who’d grown beyond anything I could accurately measure at my current level.

*At least a twenty-Level gap… This is going to be a much harder fight.*

Swallowing a groan, I reached out. White Flame, still connected to me by an invisible thread, shot back into my grasp.

Without the slightest interference—enough to make all my earlier caution feel foolish.

“Qi-Controlled Sword. No, should I call it Qi-Controlled Spear? You must’ve been in quite a hurry to push yourself this far.”

His relaxed manner and voice.

The Blood-Sword Demon Lord wore the easy smile of a man who knew he was stronger than his opponent.

“Still, I’ll give you credit. It was a good try. At least you made it back before your master died.”

And the instant the Blood-Sword Demon Lord laughed and casually waved his hand, Jeok Cheongang spotted an opening and thrust out his palm like lightning.

“You bastard!”

KWA-AAAH!

A wave of heat surged forward with his shout.

Even as the force of Flame Divine Palm, burning everything in its path, bore down on the Blood-Sword Demon Lord’s face, the smile on his lips didn’t change.

The only thing that did was a streak of blood-red Sword Force, now cutting through the space between them.

SHWAK! KWA-BOOM!

The palm force split precisely in two. The halves ricocheted left and right, slamming into the ground.

A roar swallowed everything within a dozen *jang*, and acrid smoke billowed into the air. Through it, the Blood-Sword Demon Lord appeared like a ghost and swept his sword down.

SHWAAASH!

The space warped under the horrifying pressure.

But Jeok Cheongang seemed to have anticipated the sword strike, powerful enough to cleave a mountain, and threw himself to the side.

SHK!

The ground split like tofu.

Jeok Cheongang narrowly avoided that deadly strike and immediately righted himself. But the Blood-Sword Demon Lord’s fading figure was already darting toward his flank.

*Danger…!*

He was so fast that even I could only react a beat too late.

There wasn’t even time to shout.

In the briefest moment—less than a single breath—the two superhumans exchanged attacks like streaks of light. The Blood-Sword Demon Lord’s movements were faster than sound itself.

WHOOOM—PAM!

Compressed air burst apart.

They were too close to swing a sword.

The Blood-Sword Demon Lord struck Jeok Cheongang in the shoulder with his outstretched palm, sending him flying backward like a cannonball.

And at the end of that flight—

SHWEEEE—THUD!

It was me, racing at full speed to help Jeok Cheongang.

“Old Master!”

The panicked shout burst from me before I knew it.

Jeok Cheongang was hurtling backward, but with my help, he just barely managed to stop himself. His reply came in a rasping voice.

“I’m fine. Stop making a fuss and lower your voice. You’ll burst my eardrums.”

His tone was as gruff as ever, so familiar that most people wouldn’t have noticed a difference. But I knew the Fire King Jeok Cheongang better than anyone in the world.

The more dangerous things got, the more he pretended to be calm.

If only to reassure someone else.

“You’re doing it again. Time for your medicine.”

With a sigh, I placed a hand on Jeok Cheongang’s back and poured internal energy into him without hesitation.

Tap. Fwoosh.

Fire and fire were one and the same.

The Scorching Yang Qi that sprang from the same source joined together in an instant, driving the impurities pooled deep inside his body out of him.

“Cough.”

Drip-drip.

A mouthful of blood welled up between his lips, against his will.

I clicked my tongue when I saw how black it was—a sign of a serious Internal Injury.

“You’re fine, are you?”

Jeok Cheongang spat out a bloody phlegm with a *ptoo*.

“It’s just a mouthful of blood. What’s there to make a fuss about?”

Honestly, I wanted to let it go in a situation like this. But confirming whether someone was telling the truth was important.

All the more so when their life was on the line.

THWACK!

The enemy had lost many in that last attack, but plenty of their forces still remained in the rear. As one of them charged at us before he could hold back, I kicked him in the chest and caved it in.

“Sure, after you’ve already been covered head to toe in blood?”

“I didn’t spill it. I got busy running around, and somehow it got on me.”

“That guy looks perfectly fine.”

I pointed toward the Blood-Sword Demon Lord, who was strolling toward us through the parting waves of men. Jeok Cheongang smacked his lips quietly.

“Then he must’ve been less busy.”

“Ah. Less busy. I see.”

“Anyway, I’m fine. Not a scratch on me… Well, not quite, but this is nothing.”

PAM!

Jeok Cheongang sprang upright and turned three enemies to charcoal in the same motion. Then he licked the blood from the corner of his mouth.

“Well?”

“Just tell me the truth. I won’t tell the others.”

“You insolent brat. Are you saying this old man is making things up?”

“Are you not?”

“I’m not. What does a bastard like him amount to?”

“Then I’ll go help the others.”

“Hm?”

“You can handle a bastard like him by yourself, right? Everyone else is having the worst time of their lives out there.”

GRAB!

The instant I started to turn away, Jeok Cheongang snatched my wrist like lightning and replied in a stern voice.

“The wise men of old said, ‘Even a sheet of paper is easier to lift when two people carry it.’”

“……”

“I don’t know what trick he’s using, but every so often he gets shockingly stronger and faster. It’s almost as if he’s possessed by a ghost.”

“……”

“And that’s not all. Whenever this old man tried to hit him with all my strength, some unknown force kept stopping me, stopping—”

“Old Master.”

I cut off the long-winded explanation and added quietly,

“You’re talking too much.”

“……”

“Sum it up in one sentence. Keep it short and clear.”

Jeok Cheongang fell silent for a moment, then answered.

Just as I’d asked: short and clear.

“That bastard’s strong as fuck.”

“Perfectly put.”

“And those pure-white things way over there are helping him with some bizarre dark arts. Every time that strange energy of theirs surges, he gets stronger. I tried to take them out before things got even worse, even if I had to overextend myself, but…”

“You failed. You got hit by those dark arts, too.”

“Right. The sensation I felt then was like…”

“Like the sky was crushing you.”

Gravity magic. No doubt about it.

Jeok Cheongang looked momentarily stunned by how exact—and no more than exact—my description was. I continued in a calm voice.

“More precisely, that’s not ordinary dark arts. It’s an ability called Magic.”

“Wait. If you mean Magic…”

“Yes. The very Magic you know. The kind you’d only see in my homeland.”

“……!”

Jeok Cheongang’s eyes widening was only natural.

Though I hadn’t told him every last detail, he knew a little about where I came from and what kind of world it was.

But even Jeok Cheongang couldn’t fully understand or accept what was happening now.

Neither could I.

Still, more important than any of that was the fact that we had to defeat the enemy in front of us.

*We have to target them first. Not the Blood-Sword Demon Lord, but those white-robed people… the mages.*

Even as I sent him the message through Sound Transmission, a chill ran down my spine at how unfamiliar the idea felt.

Mages. Mages.

And here they were—not in the modern world, but right here in the Murim.

But when I saw the mages in their white robes fluttering on the hill behind the Blood-Sword Demon Lord, who was still narrowing the distance between us at a leisurely stroll, the reality I was facing finally sank in.

*We have to take them out first, no matter what.*

From the moment I’d first realized the mages existed, there had been no other option in my mind.

I already knew.

Of the tens of thousands of allies on this battlefield—standing their ground or already falling—I was the only one who knew.

How many variables and dangers lurked behind the word *Magic*.

And how much power mages blessed with that incredible ability could bring to bear in a large-scale battle like this.

Besides…

*There’s one mage among them who’s especially skilled. Skilled enough to hold me and Old Master back with Magic.*

The principle was different, but Magic, too, was ultimately an ability drawn from qi.

That was why even a fairly advanced mage wouldn’t pose much of a threat to me or Jeok Cheongang.

Unless they were one of the rare few said to have reached the very edge of truth.

“……A Grand Mage.”

The title slipped from my lips like a groan.

And just as I was about to conclude that one of them had to be a Grand Mage, a question suddenly occurred to me.

*If they really have a Grand Mage, how has the situation stayed like this?*

I didn’t mean that we were winning.

Even though everyone, myself included, was giving it their all, the battle was clearly going badly for our side.

*But if the Grand Mage had stepped in, we wouldn’t even have been able to keep things at this disadvantage.*

I knew better than anyone the effect a Grand Mage could have on a battlefield. It didn’t take much thought.

A wide-area attack spell unlike anything the world had ever seen.

How long could an allied army, at least a third of which was made up of undisciplined rabble, last against that incomprehensible power—a natural disaster with a will of its own?

And yet the supposed Grand Mage hadn’t stepped in.

They’d used gravity magic to hinder Jeok Cheongang and me for a moment, and body-enhancement magic to help the Blood-Sword Demon Lord. But they hadn’t done anything beyond that.

Squish.

The Blood-Sword Demon Lord had crossed the blood-red path, and now, in this very moment, his steps finally came to a halt.

“What exactly… are you after?”

I was genuinely curious—and uneasy.

Were the mages holding back because they were preparing a powerful spell that could end the battle at once?

Or were they plotting some other scheme?

In response to my question, which I’d blurted out before I could stop myself, the Blood-Sword Demon Lord, watching us with a smile from three *jang* away, suddenly furrowed his brow.

“After? From the start, I’ve only been after two things in this battle: victory and you.”

“You sure took a long time to say you don’t want to answer.”

“I don’t know what you’re talking about, but… it doesn’t matter.”

The Blood-Sword Demon Lord shrugged with an expression that could have been sincere or an act, then raised the sword he’d been holding loosely and continued.

“Let’s finish this. Of course, I’d prefer an ending where one of you dies and the other is taken prisoner.”

Jeok Cheongang and I answered together, in one voice.

“Go fuck yourself.”

And at that moment—

PAPAT!

We charged at the Blood-Sword Demon Lord.

No—more precisely, only Jeok Cheongang shot toward him.

*Hold him off for half a quarter-hour. Just half a quarter-hour.*

With that Sound Transmission sent through the wind, I twisted my body and charged toward the hill.

SHWEEEE!
## Chapter artifact 1039

# Chapter 1039

It happened in the blink of an eye.

Tap—SHWEEEE!

Jin Taekyung’s figure, which had been hurtling straight ahead without hesitation, flowed sideways with a subtle twist of his foot.

A movement as if he’d been waiting for this exact moment all along.

Faced with this sudden turn of events, the Blood-Sword Demon Lord couldn’t help but be taken aback.

*What the…!*

An unexpected variable.

No—not just the Blood-Sword Demon Lord. Anyone would have been caught off guard.

With the gap between them already clear, and the situation so dangerous, there was no way a Disciple would leave his injured Master behind.

But that wasn’t the main reason the Blood-Sword Demon Lord was so startled.

*He’s… going after the mages!*

There was no doubt.

Jin Taekyung veered toward the Blood-Sword Demon Lord’s flank, then shot forward again.

The tips of his feet drove through the wind toward the twenty or so white-robed figures surveying the battlefield from beneath a high hill.

*Why in the world would he—no, how could he…?*

A jumble of thoughts tangled in the Blood-Sword Demon Lord’s mind in a fleeting instant.

But now that he’d been caught off guard, there was no time to hesitate. He pushed aside every question, twisted with all his might, and thrust out a hand.

SHWAAK!

A sword strike crossed the space at a terrifying speed.

In the slowed passage of time, blood-red Force coiling around the blade shot toward Jin Taekyung’s back.

No—in the very instant it was about to shoot forward—

FWOOSH!

That dreadful heat suddenly rushed in. In the disarray of his composure, the Blood-Sword Demon Lord remembered someone he’d momentarily forgotten.

The Fire King, Jeok Cheongang.

*You son of a bitch…!*

He didn’t even have time to shout. The horrified Blood-Sword Demon Lord barely managed to turn his sword and block the flames that had rushed right up to him.

KWA-BOOM! GRRRR!

The earth’s crust flipped up as if an earthquake had struck, accompanied by a tremendous roar.

Amid the acrid black smoke and steam billowing up to blanket the area, a fist spewing blindingly white light-flames appeared before the Blood-Sword Demon Lord’s eyes.

CRUNCH.

The owner of that immense power, steadily pushing back his sword, still wrapped in blood-red Force.

“Daring to take your eyes off me.”

Beyond the trembling blade, barely holding back the Flame-Extinguishing Divine Fist, the Blood-Sword Demon Lord stared at Jeok Cheongang’s faint smile. His gaze sank low.

It was already too late.

A moment’s surprise and carelessness had cost him Jin Taekyung.

“You’re full of energy, Senior. At your age, shouldn’t you be resting in a coffin by now?”

“Under normal circumstances, perhaps. But one day, someone high above the clouds told me this.”

FWOOSH.

Amid the flames rising even more fiercely, belying the Internal Injury he’d suffered earlier, Jeok Cheongang breathed out a scorching sigh.

“He said he’d send me one hell-raising but remarkable young brat as my Disciple, and that I should build coffins for the other bastards until the boy learned to act like an adult.”

“……!”

“But what use do I have for a coffin? I can burn the whole lot of you to ashes. Isn’t that right?”

Even now, the reason the Blood-Sword Demon Lord’s sword was slowly being pushed back wasn’t just that Jeok Cheongang was drawing on every last bit of strength he had.

It was his aura.

The history contained in the two words Fire King. The weight of the years borne on the shoulders of an old giant who’d lived for more than a century.

And…

“Even if you died and came back a hundred times, you’d never understand why I’m here.”

It was the spirit only shown by those who fought with their lives on the line—not to kill someone, but to protect something precious.

“So when you die this time, don’t be reborn as a human again.”

A pair of eyes shimmered with ghostly blue fire, like flames from hell.

The Blood-Sword Demon Lord clenched his teeth, momentarily overwhelmed by Jeok Cheongang.

“This damned old monster dares to…!”

His form of address had changed completely, and his tone had grown rougher.

But Jeok Cheongang only smiled more broadly at the sight.

It was proof that his opponent’s ease and composure were crumbling.

“Much better. I’d rather bite down on a sword and die than keep hearing ‘Senior’ from the likes of you.”

“Shut your mouth!”

CRUNCH!

The balance of power, which had been slowly tipping, flipped in an instant.

The fearsome power bestowed on him by the mages—or sorcerers, as the Blood-Sword Demon Lord called them—poured into his sword. A pressure as vast as Mount Taishan bore down on Jeok Cheongang.

*Hup.*

A vein stood out on Jeok Cheongang’s forehead as he sucked in a breath.

But even as he felt his toes dig deep into the earth, he didn’t retreat.

No—he couldn’t.

*What? Just hold him off for half a quarter-hour?*

Beyond the Blood-Sword Demon Lord’s shoulder, Jeok Cheongang watched the retreating figure of some insolent brat, leaving his Master—who was like the heavens to him—behind as though he were a worn-out rag. A faint smile touched the corner of Jeok Cheongang’s mouth.

*He treats this old man like some feeble old geezer. What a cheeky little brat.*

Of course, Jeok Cheongang knew perfectly well that the situation favored the Blood-Sword Demon Lord.

He’d already spent a considerable amount of internal energy fighting the Black Ghosts, while the Blood-Sword Demon Lord wasn’t tired at all. Just as the Southern Heaven Demon Empress had once done, he’d gained power that exceeded his own limits.

But…

*I’ll show you why they call me the Fire King.*

A full hundred and twenty years.

Every last one of those long years had been a struggle.

He’d fought enemies, every manner of inner demon, and even Jeok Cheongang himself.

Once, he’d been consumed by overwhelming loneliness. But not anymore.

There was someone who trusted him more than anyone else in the world. He had something he would protect even at the cost of his life.

*If you want, I’ll hold out for half a year, not half a quarter-hour. I’ll wait for you as long as it takes.*

That was why the Fire King Jeok Cheongang would not break.

He could not break.

FWOOSH—GRRRR!

The fiercely burning light-flames wavered as they crashed against the enormous blood-red Force.

But even the immense power surging forward with a roar like the heavens splitting apart couldn’t erase the smile on Jeok Cheongang’s lips.

“Come on, then.”

KWA-BOOM!

The two streams of energy, one white and one red, clashed and mingled without end, their collisions shaking everything around them.

All of this was happening far behind the back of someone who had become a sharp awl, piercing through the enemy lines.

* * *

From some point on, I could clearly feel the constant roars and the shock waves from the immense power.

*Old Master.*

One person’s face came to mind.

Half a quarter-hour.

A short stretch of time—not enough to leisurely finish a cup of tea.

But in a fight between superhumans, trading blows that flashed like lightning, half a quarter-hour was enough time for someone to lose their life.

And it was precisely for that reason that I had no choice but to keep moving forward instead of looking back to check on Jeok Cheongang.

*If I kill the mages, the Magic empowering the Blood-Sword Demon Lord will disappear.*

That was one of the reasons I’d changed direction, leaving Jeok Cheongang behind.

As long as the Magic remained in place, the Blood-Sword Demon Lord wouldn’t go down easily.

No—he might even keep getting stronger.

But if the Magic that let him grow so powerful were cut off, we’d have a chance to turn the tide.

Of course, as I’d expected, things weren’t going smoothly.

SHWISH-SHWISH-SHWISH!

Whistles of passing weapons relentlessly pierced my ears, and flashes of light skimmed past my body by the narrowest margin.

Sabers, swords, spears, and, here and there, weapons of unfamiliar shapes.

They varied, but shared two things in common.

First, every one of them had been swung at me.

Second, bright light flowed over the countless blades.

*Peak masters…!*

It wasn’t just a few of them.

There were only about a hundred enemies stationed in the rear, but every last one had reached the level of injuring others with Sword Energy.

And at their center was one being, radiating an especially powerful aura.

> **System**
> **Level:** 170
> **So Gunak**

A hulking figure, completely enclosed in jet-black armor.

Naturally, I didn’t know his title. Even if I’d known who he was in the past, it wouldn’t matter much.

The enemy in front of me had already lost his former self.

*Black Ghost.*

The reason my heart suddenly grew heavy wasn’t just the appearance of a troublesome obstacle.

The last Black Ghost, who hadn’t shown up on the battlefield, was still here. That made me think of one possibility I hadn’t wanted to believe.

WHOOOM!

The heavy whistle that rushed at me next snapped me back to reality. Feeling my feet, light as feathers despite my thoughts, I shot forward.

SWISH! KWA-BOOM!

The great saber missed its target and tore into the ground, sending the earth flying high. As ice and clods of dirt scattered in every direction, I thrust out White Flame’s spearhead with all my strength.

SLICE!

The flash-like arc cut the skin at the back of his neck.

But the distinctive feel that traveled up the shaft and reached my fingertips told me the attack hadn’t been enough to cut off his breath.

*He dodged?*

I hadn’t carelessly let my guard down.

There was no time to waste—not even a minute or second.

That was why I’d put everything into that first strike. The spear’s trajectory and timing had both been exact.

And yet, if there was one thing I hadn’t calculated perfectly, it was the sheer number of variables that came with the supernatural power of Magic.

> **System**
> **Level:** 173
> **So Gunak**

Three levels.

It might have seemed like a small difference to some, but not in the realm of superhumans.

WHOOOM—KWA-BOOM!

A strike faster and stronger than before.

No—a strike getting faster and stronger even now.

> **System**
> **Level:** 175
> **So Gunak**

SHWEEEE!

The heavy whistle sharpened. The massive, blunt blade of the great saber came crashing down like lightning, tearing through space.

KWA-KWA-KWA-BOOM!

The ground sank beneath the tremendous force. As I backed away to escape its shock wave, the sound of more than ten streaks of wind rang past my ears.

SLICE! SPLAT!

Red blood welled up from all over my body.

The moment I sensed danger, I’d twisted to dodge, but it was already too late.

No—more precisely, they were faster.

*They’d grown stronger. Stronger than they were a moment ago.*

I saw it clearly.

At the last moment, the blades had suddenly gained speed and force, shooting out like flashes of light.

And I felt it, too.

The Black Ghost and more than a hundred Peak masters closing in from every side. And beyond their shoulders, the clear pulse of energy spilling down from the hilltop.

*They’re trying to stop me somehow. Before I can get any closer.*

At this moment, I wasn’t the only one who sensed danger.

The twenty white-robed figures standing in a perfect circle—the mages.

They must have felt their lives were in danger, too.

*But I’m different.*

Everyone fears death.

Me, and them.

But what makes the difference in the face of that fear is the strength of one’s Will and desperation.

*Inventory open.*

I murmured inwardly and threw myself forward with all my strength.

Toward the more than a hundred Peak masters, who had grown even stronger.

Toward the last Black Ghost, whom I absolutely had to get past.

PAPAT!

One step.

Every distance vanished, and time slowed.

At the same time, dozens of streaks of light blazed destructively, coloring the world around me. And a single bolt of lightning, more enormous than all of them combined, came crashing down toward me.

SHWAAAK!

Yeah. I knew it, too.

One against many. The difference in strength revealed in this moment was undeniable.

But what the eye could see wasn’t everything.

*I have to get through. No matter what it takes.*

Those who try to cross over, and those who stand in their way.

Those who fight to protect something, and those who’ve forgotten what they’re supposed to protect.

They had no Will. They’d forgotten what it meant to be desperate, and they couldn’t even remember the word duty.

But I wasn’t like them.

Because I knew all that, I could move forward with my life on the line.

I could hurl myself at the relentless attacks and strike with everything I had—even my soul.

Just like now.

SHWAK!

White Flame’s spearhead tore through space.

At the same time, I whispered the command I’d held back.

*Fire Dragon Armor, summon.*

Ding.

KWA-BOOOOM!

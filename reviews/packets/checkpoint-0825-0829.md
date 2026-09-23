# Checkpoint Review — 825–829

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

# Chapters 825–829

## Plot

Jin Taekyung and the Skeleton King confront the Doppelganger at a ruined oil field. A surge of magical power reveals a hidden temple built, the Doppelganger claims, for Demon King Asmodeus’s return. Jin destroys its seventy-two Golems and magic circles with white-blue flames, while the Skeleton King fights through temporary blindness to help stop the Doppelganger’s escape.

Though repeatedly cut down, the Doppelganger regenerates by consuming its stored lives. Jin’s attacks reduce it to a Level 10 shadow, and the Eye of Truth confirms its true essence. As Jin pins it down, the Doppelganger begs for its life and blames Asmodeus for its crimes. Jin’s anger wavers at the accusation.

## Continuity

- Jin remains the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate the Doppelganger, also known as The Prophet.
- The Doppelganger claims it served Demon King Asmodeus, was ordered to infiltrate humanity, and that the temple was built for Asmodeus’s return with his armies. These claims remain unverified.
- Jin believes Asmodeus died on Victory Day, the day Jin was born. Whether Asmodeus is dead or will return remains unresolved.
- The Doppelganger regenerated repeatedly by consuming stored lives. After Jin’s attacks, it remains as a Level 10 shadow, pinned down and at Jin’s mercy; its remaining lives and ultimate fate are unknown.
- Jin’s white-blue flames destroyed the temple’s seventy-two Golems and magic circles, causing mana backlash in the Doppelganger.
- The Skeleton King helped fight the Doppelganger and was temporarily blinded by its enhanced Light magic. Jin guided him with Sound Transmission.
- The cause of the radiance that filled the temple remains unknown.

## Translation Decisions

- Keep magical power distinct from mana.
- Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.
- Keep Fire Storm and Aqua Storm as distinct named spells.
- Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” 실드 마법 as “Shield magic,” and 수마 as “sleep demon.”
- Keep Erasure distinct from ordinary death or destruction.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate the Doppelganger known as The Prophet.",
    "The Doppelganger is the last surviving member of its species and can absorb appearances, abilities, and memories; it had Siegfried Bassman’s face and Grand Mage abilities.",
    "The Doppelganger claims to have served Demon King Asmodeus and received his order to infiltrate humanity before Asmodeus fell.",
    "The Doppelganger says the temple’s empty throne was made for the Great King and that Asmodeus will return with his armies.",
    "Jin believes Asmodeus died on Victory Day, the day Jin was born, but cannot yet determine whether the Doppelganger’s claims are true.",
    "Jin’s white-blue flames destroyed the temple’s seventy-two Golems and magic circles, causing mana backlash in the Doppelganger.",
    "The Skeleton King interrupted the Doppelganger’s escape and repeatedly cut it down; it regenerated by consuming stored lives and remains as a Level 10 shadow after Jin’s attack.",
    "Jin’s Eye of Truth revealed the Doppelganger’s true essence as Level 10.",
    "Jin is confronting the Doppelganger over the devastation it caused; its claim that Asmodeus ordered its crimes has unsettled him."
  ],
  "continuity_sources": [
    828,
    829
  ],
  "open_questions": [
    "Is Demon King Asmodeus truly dead, and will he return?",
    "Are the Doppelganger’s claims about Asmodeus and the temple true?",
    "What caused the radiance that filled the temple?"
  ],
  "safe_through": 829,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword.”",
    "Render 에어 슬래시 as “Air Slash” and 실드 마법 as “Shield magic.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 825

# Chapter 825

A distant flash burst forth with the Teleport spell.

That was how it began.

The space around me warped. A horrifying pressure unlike anything I’d ever felt seized my heart, and my joints and muscles, sucked into a third void, screamed.

*Hngh.*

I couldn’t breathe. It hurt.

A brief span of less than a few seconds felt as long as days.

But I clung to the thread of my consciousness, just as it was about to snap.

*Crack.*

I had to endure. I had to hold on, no matter what.

Clenching my teeth with that single thought, I watched the ground and sky flip endlessly past through the dazzling beams of light that flooded my vision.

A vast wilderness. A desert stretching toward hills curved like a crescent moon.

A distance of hundreds of kilometers vanished in an instant, and the violently churning flash quickly faded.

And at last, when deep darkness settled over us—

*Fwoosh.*

Space split open. Beyond the gap, a new light—different from the flash moments ago—began to seep in.

No, it wasn’t the only thing that was new.

*This is…*

I could see it. I could feel it.

The dim light, neither dark nor bright, and the damp air of early morning.

Sand grains mingled with the wind—and, on top of that, the uniquely sticky, unpleasant sensation that belonged only to magical power.

*We did it.*

I knew it instinctively.

This perilous attempt had succeeded.

The Grand Mage’s Teleport spell had overcome the magical power interfering with it and brought us to the designated coordinates.

And beyond that unfamiliar space we’d finally reached was the being we’d searched for so desperately.

The Doppelganger.

“……!”

Our eyes met in midair. At the same moment, our pupils widened.

I looked at the Doppelganger, and the Doppelganger looked at me.

Time crawled by, as if the world had come to a stop.

But my body already knew what it had to do. It pushed forward, defying time and space.

*Whoosh.*

Wind split to either side along the spearhead, brushing past my ears.

As I pulled back the shaft of White Flame, gripped tightly in my hand, an unexpected pain surged through me with the sound of bones shifting out of place.

*Crack.*

It was an aftereffect of the unstable Teleport spell.

Unlike the Doppelganger’s Blink spell, which had moved it only a few hundred meters, this dangerous attempt had hurled us hundreds of kilometers. My body had to bear the full cost.

*Fuck.*

My breath hitched, and my fingertips trembled. I could feel the Scorching Yang Qi racing along the spearhead falter as it sensed something was wrong with my body.

But all of that was needless worry.

Because I wasn’t alone.

*Thump.*

A firm hand, backed by tremendous strength, pressed against my back. The Skeleton King’s clear voice pierced my ears.

“Go.”

In that instant—

*Whoom!*

I shot forward.

Tearing through the gap in space opened by the Teleport spell, I plunged down like a bolt of lightning. The Scorching Yang Qi, which had faltered for a moment, rose like a wildfire and coiled around the spearhead.

*Fwoosh.*

Seething heat spread out. Ten-odd meters of space vanished in an instant.

And at the end of it stood the Doppelganger, eyes wide at this unexpected turn of events.

“Y—!”

What had it been trying to say? What had it wanted so badly to say?

But no one—not even the bastard itself—could hear the rest of it.

No. It couldn’t finish.

*KWA-BOOM!*

Blue-white flames erupted like a wave and swallowed the Doppelganger’s body along with its unfinished cry.

* * *

The Doppelganger writhed.

Among the countless deaths it had experienced, this was one of the most terrible pains it had ever endured. It was fire in the truest sense.

*Shhk. Fwoosh.*

Along with the spearhead that had slashed diagonally across its upper body, a lava-like force seeped into every part of the Doppelganger’s body and rampaged through it.

Even as it died, that force continued gnawing away at the life force that took the place of each life it lost.

It vaporized its blood and melted its flesh and bones.

“GRAAAAH!”

The Doppelganger let out a scream of agony.

The flames that had penetrated its body had already reduced more than ten lives to ash. If its endlessly regenerating flesh and bones hadn’t acted as firefighters, it would still be dying at that very moment.

“Grrr…”

Its bloodshot eyes were red with burst blood vessels.

The moment the Doppelganger groaned in pain and straightened up—

*Whizz—thunk!*

Before it could steady its unbalanced body, something came flying and pierced its forehead.

The Doppelganger revived before its body, falling backward, could touch the ground, then hurriedly threw itself to the side.

*Thud-thud-thud!*

Something pure white grazed its body and embedded itself in the ground.

Realizing the objects were pieces of bone, the Doppelganger lifted its head.

A being with a power both utterly familiar and strangely alien was rushing toward it.

*That thing…!*

The Skeleton King.

A sword imbued with power far too great for a mere undead monster—but impossible to dismiss—flashed.

*Shhk!*

A sharp slicing sound.

Magical power scattered dazzling light, utterly at odds with the name **Hero’s Sword**, as it cut through the Doppelganger’s wrist.

The Doppelganger recoiled in pain and roared in a savage voice.

“How dare an undead like you…!”

Even in the Demon Realm, where countless monsters existed, undead were at the very bottom.

Unless they were beings like Liches, who chose to become undead only after reaching the highest realm, they were mere foot soldiers.

No, that was how it was supposed to be.

*Crack—splash!*

Blood erupted with a blinding flash of the sword.

The Doppelganger met death once more in an instant and clenched its teeth.

*Damn it.*

The exchange had been brief, but it had no choice but to admit it.

The Skeleton King was no easy opponent.

That aberration before it had broken through the limits of an ordinary undead and reached a higher level of existence.

But…

*It’s still no match for that monster.*

The Doppelganger leapt far back to get away from the Skeleton King and quickly shifted its gaze.

In its sunken eyes, it saw Jin Taekyung breathing hard, using a spear as a cane.

*He’s different from the last time I saw him. He definitely used more power than his limits should allow.*

The Doppelganger wasn’t foolish.

In fact, it was far more cunning than any human or monster.

It had spent decades manipulating the world from behind Michael Silbert, a mere puppet.

And even when Jin Taekyung had appeared out of nowhere and struck, it had managed to swap Siegfried Bassman’s soul for another.

*Take hold.*

*KWA-AAH.*

A fierce wind whipped around the Doppelganger. Sensing the ominous aura, the Skeleton King kicked off the ground and reached out.

*Whoosh!*

Part of his arm bone cut through space with a sharp whistle. The pure white pieces of bone, flying like hidden weapons, embedded themselves throughout the Doppelganger’s body.

Or so it seemed to the Skeleton King.

The Doppelganger’s body, which should have fallen in a spray of blood, vanished as if it had never been there in the first place.

*Pop.*

It was gone. Literally in the blink of an eye.

And that meant one thing.

Magic.

*Blink?*

As realization struck, the Skeleton King instinctively twisted his body.

But the Doppelganger, which had caught him off guard for an instant and slipped out of his sight, was already preparing its next move.

*Grrrrk.*

Mana surged in a world that had slowed down.

At its center was the monster that had greedily swallowed up everything belonging to the Grand Mage, once a great man in life, and grown fat by absorbing it all.

*Air Slash.*

At that moment—

*Whoooosh!*

Watching blades of wind rain down on the Skeleton King, the Doppelganger was certain.

Even if they couldn’t erase that aberration outright, the spell was powerful enough to leave it unable to fight for a while.

It could end this wretched battle.

But it was mistaken.

Just as the Skeleton King had briefly lost sight of the Doppelganger, the Doppelganger had also forgotten the presence of one person.

*Fwoosh.*

Floating more than ten meters in the air, the Doppelganger suddenly felt heat surging toward it.

Only then did it remember someone who, just moments ago, hadn’t even been able to control his own body properly.

*You’ve got to be fucking kidding me…!*

The Doppelganger sucked in a startled breath and hurriedly drew back its mana.

*Whoosh.*

The gale that had been descending as if to swallow the Skeleton King scattered into a gentle breeze. At the same time, translucent shields layered over the Doppelganger’s entire body.

Then, just as a dazzling flash shot across the space and finally struck the surface of the shields—

*Crack!*

The Doppelganger heard it clearly. It saw it.

A single flame piercing through dozens of layers of Shield magic, and the mana barriers shattering into pieces.

*KWA-BOOM!*

Ignition. Shattering. Explosion.

All three happened at once, and a massive shock wave lashed out in every direction alongside blue-white flames that filled the air.

*Rumble-rumble-rumble!*

Feeling the impact travel all the way through the ground, the Skeleton King thought for the briefest instant:

Perhaps that strike had cost the Doppelganger one of its most precious souls.

But Jin Taekyung knew better.

Even in his exhaustion, he’d summoned every last bit of strength and struck. He knew better than anyone why the familiar, clear chime wasn’t ringing now.

*Not yet. Not yet.*

The bastard—the Doppelganger—still had the Grand Mage’s power and soul.

But his legs, which should already have kicked off the ground with all their might, wouldn’t move.

His depleted mental strength kept dragging his consciousness toward the abyss, and the dozens of movements and attack routes that flashed through his mind at that moment were nothing but impossible imaginings.

There was only one friend who could understand what he meant just by meeting his eyes.

*Bang!*

Their gazes crossed in midair for the briefest instant.

But that was enough. Reading the intent in Jin Taekyung’s eyes, the Skeleton King launched himself off the ground without a moment’s hesitation.

Through the acrid smoke that filled the air.

Toward the Doppelganger, at the center of the explosion.

*Tssssss!*

Golden magical power surged along the blade.

The force was less than half of what it would normally have been, thanks to the aftermath of the reckless Teleport spell. But the dazzling sword light cut through the sky without hesitation.

It sliced through the thick smoke and shot toward the enemy beyond.

*Shing!*

A single streak of light.

At the end of that keen strike—

*Shhk!*

A fountain of crimson blood burst forth.

* * *

Though my vision was slowly blurring, I saw it clearly.

The Skeleton King’s strike cutting through the air. And someone’s arm shooting up through the blood.

*He cut it off.*

No doubt about it. That slender white arm belonged to the Doppelganger—or, more precisely, to the Grand Mage the bastard had absorbed three years ago.

But there was no head that should have fallen, no scream that should have torn through the air.

If I hadn’t figured out where the Doppelganger had gone after vanishing from sight again, I might have let out a full-throated yell.

But instead of venting my anger, I held it in.

A voice, exhausted and unfamiliar, as if it belonged to someone else, slipped between my lips.

“Are you a fucking lizard or something? You son of a bitch.”

I slowly turned around. The Doppelganger stood in the middle of the ruins. Blood poured from its cleanly severed shoulder.

“Let’s try your head this time. Not your arm or leg—your whole damn head. How’s that?”

“I’m afraid that won’t be possible.”

The Doppelganger replied, its face twisted like a Fiend, then continued:

“I need the Grand Mage’s soul for what comes next.”

What?

Just as I was about to blurt out a question—

*Vwoom.*

A tremendous force pulsed around the bastard.

No—the entire ruin shuddered like a living creature.
## Chapter artifact 826

# Chapter 826

That’s how humans are.

There are billions of people, and each one sees and understands the world by their own standards, by their own common sense.

And it’s only when they witness something they can’t easily accept by their own measure that they feel shock.

Of course, I’m no exception.

Even after I suddenly began moving between two worlds one day, even after I made it this far with the unbelievable power called the System, that hadn’t changed.

I’d always been honest about my feelings, and sometimes I got so caught up in them that I even forgot what I was supposed to do.

Like right now.

*What… is that?*

One question brought every thought in my mind to a halt.

I stared, stunned, at the sight unfolding before me.

No. I wasn’t the only one.

“What the hell is this?”

Even the Skeleton King, who’d been about to attack the Doppelganger again, muttered blankly.

The golden magical power that had brilliantly colored the Hero’s Sword had long since faded.

We felt the tremendous force flowing out from the Doppelganger, and at the same time, heard a rumbling rise from deep beneath the ruins at our feet.

*Rumble. Rumble-rumble.*

*This is…*

The sensation was familiar. But this rumbling wasn’t just some noisy roar. It was something deeper, more fundamental.

If I had to find the right word, then…

*Resonance.*

Even as the thought occurred to me, I felt like I was talking crazy.

In Murim, a First Rate swordsman could draw out the ringing of a sword. But this was just the earth.

A barren wasteland where not a single tree or weed grew, now a ruin no one visited anymore.

And this land of death, these ruins stretching in every direction, were trembling as if in resonance.

Even after thinking it over, it still sounded crazy.

If not for a thought that flashed through my mind like lightning, I might have stood there for a long time, stalled by this unanswered question.

But, as always, the answer was closer than I thought.

“Magic.”

The moment that one word slipped from my lips, almost like a groan—

*Boom!*

The ruins, which had been giving off a deep rumble like a heartbeat, rippled. At the same time, a dazzling mass of light burst out, coloring everything around us.

*Fwoooosh!*

A flash brighter than anything I’d ever seen—not even the Teleport spell I’d experienced earlier came close.

I closed my eyes without hesitation and bent my body at an angle. The spear shaft, gripped tightly in my hand, quivered.

*It’s coming. It has to be.*

An instinct carved deep into my bones long ago moved my exhausted body.

I was fully prepared to evade the Doppelganger’s imminent attack and counter its ambush.

My body and mind felt as heavy as waterlogged cotton.

But even if I was the one who died in this clash, I was certain the Doppelganger wouldn’t get away unscathed.

*One Strike.*

Whoever fell, it would be decided in a single move.

I couldn’t see him right now, but the Skeleton King was probably waiting for it with the same resolve.

*Come on.*

I steadied my breathing and drew my senses up as high as I could.

My eyes were shut tight. But through my sharp five senses, I could feel the air trembling and smell the earth of the dead ruins.

The dazzling flash seeping through my thin eyelids, brushing against my retinas before slowly fading, was no exception.

*The light… faded?*

It was only natural that the first question to come to mind was why.

That moment had been perfect for the Doppelganger. The ideal chance.

But there wasn’t even a hint of the ambush I’d expected. All that reached my ears was a voice I’d grown familiar with.

“You’re more timid than you look, Chosen One.”

I bit my lip.

Was that meant to be a trap, or had it simply let its guard down?

But I only hesitated for an instant. The choice left to me was clear.

I slowly opened my eyes. In my sharpened vision, I saw the Doppelganger staring at me.

No—the whole world around me had changed completely.

“……!”

“……!”

Over the Doppelganger’s shoulder, I saw the Skeleton King, eyes wide open.

Or maybe I had the same expression on my face.

That’s how unthinkable the sight before me was.

“This is…”

“What do you think? Impressive, isn’t it?”

The Doppelganger snatched the end of the Skeleton King’s sentence and swept both arms out in an exaggerated gesture.

A ball of light rose and floated at the Doppelganger’s fingertips, illuminating the ruins—or rather, the space that had been “ruins” only moments ago.

“Consider it an honor. You’re the first guests in this marvelous temple.”

The Doppelganger’s words were half lie and half truth.

This place certainly had enough to it to be called a temple, but “grotesque” suited it far better than “marvelous.”

Naturally.

Everything in sight was grand and immense, as if modeled after a temple from mythology. But rotten plant roots coiled around its towering pillars, and the ceiling blocking the sky let in not a single ray of sunlight.

For a moment, I thought this temple resembled the Doppelganger.

It had copied mythology’s outer shell convincingly enough, but inside, everything was rotten and dead.

The only thing that seemed remotely like the myths was the enormous stone statues of monsters, packed tightly into this vast space, hundreds of meters across.

“It’s a masterpiece, don’t you think?”

Instead of answering, I stared calmly at the Doppelganger.

Its attitude was unmistakably different from a moment ago.

And the instinct I’d developed from facing countless enemies told me that its relaxed demeanor wasn’t carelessness.

*Composure.*

No doubt about it. The Doppelganger had regained the composure it had briefly lost.

But that wasn’t just because a new arm had grown where one shoulder had been empty, or because a temple filled with monster statues had appeared.

*There was a reason it came here in the first place.*

I thought to myself and quietly spread out my senses.

I could feel an unseen force writhing all around us. At the same time, something Magic Johnson had once mentioned about Siegfried Bassman casually drifted into my mind.

*“Bassman was a great Grand Mage. He wasn’t a War Mage on my level, but he was more scholarly than anyone, and especially skilled at using magic circles.”*

I already knew that.

And I was certain the Doppelganger, which had spent a long time absorbing countless souls and gaining experience, had become even stronger than the Grand Mage had been in life.

*Three years.*

A strange amount of time—long if you thought of it as long, short if you thought of it as short.

But it had been enough for the Doppelganger, after taking the Grand Mage’s power and soul, to complete various preparations.

“Hey.”

The Doppelganger, staring at me, suddenly clicked its tongue.

“When someone asks you a question, you should answer.”

*Vwoom.*

A low hum reverberated with its emphatic words.

I exchanged a glance with the Skeleton King for an instant, then spoke.

“Are you an idiot? I’m not answering because you’re not a person—you’re a piece of shit.”

“Hmm. You have no respect for your elders. Siegfried Bassman would be a well-respected hero in this world.”

“That’s right. If you mean the Grand Mage I know. But…”

I lowered the spearhead and continued:

“A monster like you doesn’t count, you bastard.”

I had no idea what Siegfried Bassman had been like in life. I’d never seen him or met him. I only knew him from textbooks and what people around me had said.

But it still pissed me off to listen to the taunts of a bastard wearing someone else’s shell.

Of course, I was openly showing my hostility now because it was one of the reactions the Doppelganger would consider natural.

*Just a little longer. Just a little.*

I’d lowered the spearhead I’d been aiming at the Doppelganger, but the other spear I held in my heart was still pointed at it.

I slowly gathered the energy in the air.

Quietly and carefully, so my opponent wouldn’t notice.

It was one of the principles I’d learned this time, after gaining some understanding of the Middle Dantian’s uses.

*I used too much power before I could recover from the effects of the Teleport spell. I need a little time.*

The same was true of the Skeleton King. But since he was already dead, he was actually in a better state than I was, and was slowly absorbing the magical power scattered through the air.

So that when my signal came, he could strike off the Doppelganger’s head—even as it kept running its mouth.

“Monster. Right, that’s what I am. I’ve spent so many decades among humans that I sometimes forget.”

The Doppelganger scratched its chin and continued.

“But there was one thing I never forgot, no matter the circumstances. This place. The command I heard from my master here.”

I paused without meaning to.

The Doppelganger’s master.

The very being who had sunk the Doppelganger’s roots into this world, just as it had used Michael Silbert as a puppet.

“Don’t tell me…”

My voice trailed off.

A question that had suddenly risen in my mind made my chest churn.

And as if it had seen right through me, the Doppelganger’s lips curved into a gentle smile.

“Want me to guess who you’re thinking of?”

Why did my heart sink at the sight of that smile?

I answered as calmly as I could.

“Shut your mouth.”

“What? Weren’t you curious?”

“It doesn’t matter who it is. Even if…”

It felt like I’d swallowed a handful of sand. My mouth was gritty.

I steadied my breathing and continued in a hoarse voice.

“Even if your master is the Demon King Asmodeus.”

“……!”

The air trembled. I could feel the Skeleton King’s agitation from here.

The Demon King.

The master of the Demon Realm, the land of death no human had ever reached, and the ruler of monsters.

To humanity, the Demon King Asmodeus was both a source of calamity and calamity itself.

His appearance changed human history. Civilization was overturned, and countless people lost those they held dear.

Just like me.

*Father.*

A beloved face flashed before my eyes. The misfortune that struck my family had lasted only an instant, but the sorrow and longing lasted forever.

Maybe that was why.

Maybe that was why something hot was boiling deep in my chest, even now, when I had to be calmer than ever.

This contradictory urge—to tear apart the mouth of the bastard grinning in front of me, and at the same time demand an answer.

*Crack.*

My hand had clenched so hard that it had turned stark white.

I glared at the Doppelganger and opened my mouth. No—muttered as if making a vow to myself.

“He—the Demon King—is already dead.”

And at that very moment,

I saw it clearly.

The Doppelganger’s smile deepening. Then the truth I couldn’t accept, in the voice that asked me:

“Do you really think so?”

“……!”
## Chapter artifact 827

# Chapter 827

For a moment, it was as if the world had stopped.

I stared blankly at the Doppelganger, smiling without a sound.

In my frozen mind, the voice I’d heard moments ago kept playing over and over.

*“Do you really think so?”*

I couldn’t breathe.

I’d already realized what that question meant.

But a deep, instinctive rejection surged up from my chest, and before I knew it, my lips were moving.

“Don’t spout that bullshit.”

There was no way.

I knew it, and so did everyone in this world.

The Demon King—Asmodeus—was already dead.

Near the end of the Great Cataclysm, on what would later be called Victory Day, humanity’s hero fought the Demon King and finally brought down the calamity that had turned the whole world into a blazing inferno.

And hours later, a small life was born in a country on a peninsula surrounded by the sea on three sides.

That life stood here now.

“The Demon King died the day I was born. On Victory Day.”

The hoarse voice escaping my lips sounded like someone else’s.

I continued, putting force into my words as if making a vow to myself.

“He was erased, and we won. That’s all there is to it. That’s the truth.”

I was only standing there. Only moving my lips to speak. Yet I was short of breath. Every exhalation tasted bitter, as if it carried poison.

Like the voice now burrowing into my ears.

“Yes. That, too, is true, Jin Taekyung. Chosen One.”

The Doppelganger.

The abyss-like monster looked at me and curled its lips.

The smile it drew with the Grand Mage’s stolen face was as sly and wicked as a serpent’s.

“That is all you know. And it is the truth, as far as you know it.”

*Step.*

It took a slow step toward me.

The sound echoed through the vast, grotesque temple, mingling with its voice.

“But look at me.”

Its gaze was dark and deep. Its eyes, swirling like the abyss, fixed on me.

“Look at me, who merely watched while countless humans died, and watched as you wept for joy at your victory. Look at me, who was with you, carrying out the command of the Great King.”

“……!”

“Do you still not understand? My very existence is proof. Proof that the truth you believe is a lie, and that there is a truth you don’t know.”

My vision blurred in an instant.

The massive pillars supporting the temple vanished, along with the grotesque statues and the Skeleton King, whose lips were moving as if to say something.

There was only one presence.

The Doppelganger filled my vision. Its image was etched clearly into both my eyes.

*The Great Battle of Paris.*

My mind reeled.

Small puzzle pieces surfaced within it, one by one, filling the empty spaces.

*Long before the Demon King Asmodeus fell, the Doppelganger had already infiltrated this world.*

Michael Silbert hadn’t chosen the Doppelganger from the start.

The Doppelganger had chosen him.

The monster from another world had recognized a monster in this one. It had read the immense ambition curled up inside a human body of flesh and bone.

*Why had the Doppelganger chosen Michael Silbert, of all people?*

I already knew the answer to the question I’d asked myself.

*Because all it wanted wasn’t simply to exist in this world.*

The Doppelganger possessed an ability that could only be called one of a kind.

It could absorb not only someone’s appearance and abilities, but even their memories, making them its own. Living as a single human would have been easier than anything.

But now I understood.

The Doppelganger’s infiltration of humanity hadn’t been a simple act of betrayal or defection.

It had received an order.

An order from the master it served with its very life—the Demon King Asmodeus.

Everything that came after must have happened just as I knew it.

The Doppelganger used Michael Silbert to move the world.

The puppet that had made a name for itself at the Great Battle of Paris quietly grew in the shadow of Cheon Taemin, the sky above it. And the shadow controlling the puppet fed on someone’s soul, out of sight.

For more than thirty years, it climbed the stairs, reflecting on the order it had received.

Until this endless staircase came to an end.

Until the long-awaited moment arrived, and a tightly shut door appeared.

“Judging by your face, it looks like you’re finally starting to understand.”

The Doppelganger laughed aloud and raised a hand.

*Whoosh.*

A solitary sphere of light, drifting through the darkness where not a single ray of sunlight could reach, stopped at the far end of the vast temple.

A hazy glow illuminated the enormous space.

And beneath it stood a single throne.

*That’s…*

The moment I saw the empty throne, I knew instinctively.

I knew who this temple—and that seat—had been built for.

And I knew what the seventy-two bizarre, hideous stone colossi meant.

“The seventy-two commanders of the Demon Realm…”

The Skeleton King muttered as if groaning. The Doppelganger spread both arms toward the throne, its face alight with rapture.

“The Great King will surely return. On that day, which is not far off, He will come with the countless armies that follow Him.”

“……!”

Every hair on my body stood on end. A chill crawled up my spine like a snake.

I didn’t believe the Doppelganger. It was made of lies, through and through.

For now, I couldn’t be sure whether what I’d heard was true or a lie meant to shake me.

But…

*If every word it said was true.*

Then I already knew what I had to do.

Dynamite with a severed fuse doesn’t explode. A locked door won’t open without a key.

And in that sense, the Doppelganger was both the fuse and the key.

The opening signal for a massive calamity about to unfold.

This was the only chance to stop the return of a being who would be a nightmare for humanity.

*I’ll kill it.*

The clouds filling my mind cleared.

Along with the single thought that felt like a mission, energy boiled throughout my body.

*Fwoooosh.*

My vision went hazy. My body, still bearing the full brunt of the strain from the reckless Teleport spell, cried out in pain.

But without a moment’s hesitation, I sent the Scorching Yang Qi I’d drawn up from my Lower Dantian rushing through every limb and acupoint. I dulled the pain, forced life into my torn muscles, and finally unleashed it.

*BOOM!*

Flamefire Path.

Blue-white flames burst from my heels, devouring the darkness.

In a moment split into ever smaller pieces, I erased the space between us and thrust my spear.

With a motion I’d repeated tens of thousands of times.

Toward a single being.

*SHWAAA!*

Just as its name, White Flame, promised, the spearhead cut through the darkness, bright as a white flame, burning fiercely.

As if nothing could stop it.

As if it would turn everything to ash.

At least, that was how it looked—until the next moment, when something invisible blocked the way at the Doppelganger’s gesture.

*BOOM!*

A deafening roar filled my ears.

Then came a tremendous force of repulsion.

*Hngh.*

I gripped the spear shaft tightly as it vibrated in my hands.

Ten paces away.

The Doppelganger’s still-smiling face wavered inside a transparent barrier I couldn’t see.

“Do you understand now why I came all the way here?”

Shield magic?

No. This wasn’t simple Shield magic.

Even if the Doppelganger was now a Grand Mage, it was nearly impossible for it to conjure a barrier sturdy enough to stop my strike so effortlessly.

Unless there was one explanation.

*A magic circle.*

Siegfried Bassman.

One of only three Grand Mages in the entire world, and considered the greatest master of magic circles among them.

And the three years granted to the Doppelganger after it absorbed his soul.

“You son of a…”

“You humans take out insurance. Can you understand if I say it’s similar?”

There was confidence in the Doppelganger’s curled lips.

It hadn’t been smiling like this when it was fleeing after suffering one death after another at my hands.

“Don’t waste your effort. I am the master here.”

*Vwoom.*

An unprecedented force resonated from every direction.

Magic circles, holding dazzling halos of light, rose up all around us, and the enormous statues depicting the seventy-two commanders of the Demon Realm began to tremble.

“As the Great King’s representative, I command you: awaken from your slumber.”

*Crackle.*

At the Doppelganger’s commanding voice, fragments of stone fell from all around us.

And at the same time, the colossi that seemed destined to remain still forever began to move.

No—they opened their eyes.

*Flash.*

Monsters, ranging from a few meters to dozens of meters tall, gazed down at the distant ground with glowing red eyes.

The Skeleton King, whose earlier attempt to attack had been blocked by a translucent barrier just like mine, stared blankly at the sight.

Then he shouted like a bolt of lightning.

“Move!”

At that moment—

*WHOOOOM!*

Arms, legs, and claws made of stone filled my vision as they came crashing down.

At the same time, the world slowed, and my breath scattered.

*No. I can’t dodge.*

Not because the statues’ attacks were too powerful or too fast.

The farther I retreated to avoid them, the farther I’d get from the Doppelganger.

*Now’s the time to go.*

The statues controlled by the Doppelganger were undoubtedly powerful.

But I knew that, though it had copied the forms of the seventy-two commanders of the Demon Realm, their individual strength didn’t even measure up to an S-rank monster.

Then…

*I’ll cut them down.*

My body moved as soon as I thought it.

No—in that instant, it wasn’t only my body of flesh that moved.

*Vwoooooom.*

With a powerful hum, my closed Middle Dantian opened.

At the same time, a space woefully small compared to the enormous temple—but sufficient to accomplish my goal—fell under my control.

*Hngh.*

A headache so sharp it nearly blacked out my vision.

But I endured. I had to.

Clenching my teeth until my lips were ragged, I let go of the shaft of White Flame in my hand.

*Fwoosh.*

Hot. Blinding.

The spear, holding the Scorching Yang Qi that sprang from my Lower Dantian, blazed blue-white, and the will of my Middle Dantian moved it.

No—it sent it hurtling.

*SHWAAAA!*

There was no roar.

In a world filled only with the sound of air splitting, a streak of light-flames cut through everything around it.

*SHWAK!*

It cleaved through space.

*SHHK!*

It sliced through the soulless Golems as if barely grazing them.

Again and again. Maybe dozens of times.

And at last, when I caught it in my hand as it tore through everything around us and returned to its master—

*KWA-AAAA!*

Everything crumbled.

The seventy-two colossal statues. The pillars as thick as the World Tree.

And—

The countless magic circles that had filled every corner of the temple.

*KWA-CRASH!*

Maybe it was because my body had reached its absolute limit.

My vision turned white. I couldn’t see a thing.

But I could hear. I could feel.

The mana and magical power scattering into fragments. And beyond them, a presence stricken with shock.

“Say that again.”

My voice came out broken as I muttered.

I gathered up the last of my strength and stepped forward.

*Step.*

“Who exactly is the master here?”

At that moment, instead of an answer, a dazzling radiance filled the temple.
## Chapter artifact 828

# Chapter 828

Fear comes in different kinds and degrees.

Some people spend their whole lives afraid of water because they fell into a valley stream as children. Those who’ve lived through an earthquake carry trauma like a brand.

But the greatest and deepest fear of all is fear of the unknown.

A realm no one has ever seen—or even imagined.

That’s what the unknown is.

The universe and the deep sea, beyond the reach of even humanity, with its brilliant civilization built on science and magic.

And now, in this very moment, a single streak of fire tearing everything around it to shreds.

*BOOOOM!*

It was like a storm.

A storm of fire, so razor-sharp it made your skin crawl, turning everything it touched to ash.

The Doppelganger stared at the scene in stunned silence.

Blue-white flames, pouring out suffocating heat, stained its pupils red.

*SHWAAK!*

Tearing. Ripping. Slicing.

The wind shrieked. The Golems it had spent three years painstakingly shaping burst apart like fireworks.

Limbs of massive, solid rock and weapons crashing down hard enough to split the earth—none of it mattered.

*Fwoosh. KRRRACK!*

They melted. They crumbled.

It took only an instant for all seventy-two Golems to become nothing but heaps of rubble. It happened before the Doppelganger could even order them to retreat.

No—that wasn’t quite right. It hadn’t even had time to do that.

The flames tearing through everything hadn’t destroyed only the Golems.

*CRASH!*

A tremendous force raged through the air.

The magic circles, scattering dazzling halos of light, exploded one after another.

The Doppelganger watched in horror as the translucent barrier surrounding it melted like candle wax.

“What the…”

But before it could finish, something hot surged up from deep inside its body, spilling through its throat and into its mouth.

*Hack.*

The Doppelganger spat out a clump of dark red blood. Its pupils trembled.

Knowledge surfaced from Siegfried Bassman’s memories and struck its empty mind.

Mana backlash.

The forced severing of its connection to so many magic circles had sent the energy in its body into a frenzy.

If it hadn’t prepared the magic circles through various conduits and spells, and had instead cast the magic directly, it wouldn’t have been surprising if it had died several times over. The blow was that severe.

*How? How is this possible?*

The Doppelganger gasped for breath and raised its head.

There wasn’t a trace of composure left in its eyes, only shock.

The only thing reflected in them was one human who seemed as unknowable as the unknown itself.

*Jin Taekyung.*

There he was.

He stood tall, gripping a silver spear that glowed white as the Golems’ remains rained down over his head.

Then, through the halo of light left behind by the magic circles melted by the flames, the Doppelganger saw a predator staring straight at it.

“Say that again.”

His voice sounded like it might break at any moment, yet boiled like lava as it pierced the Doppelganger’s ears.

His unsteady footsteps approached, as if he might collapse at any moment.

*Step.*

It was strange.

The whole place was filled with thunderous noise. The temple, stripped of its pillars, was slowly collapsing, and the rocks that had once been Golems were scattering in every direction…

*Step.*

And yet the footsteps of that small human sounded like thunder. The sound of his voice made every hair on the Doppelganger’s body stand on end.

“Who exactly is the master here?”

“……!”

The Doppelganger had to swallow a scream that was rising unbidden between its lips.

Clear fear was carved into its eyes as it stared at Jin Taekyung.

A monster. That human was a monster.

One who surpassed expectations and limits by an impossible distance, every single time.

After dying countless times on the battlefield, the Doppelganger had long since abandoned its contempt for Jin Taekyung.

It had let go of everything and judged the situation coldly. This time, it had been certain.

Once it reached its destination, everything would go smoothly.

Jin Taekyung would never catch it.

But it had been wrong.

The Doppelganger, which had left the battlefield before anyone else, hadn’t known Jin Taekyung had reached an even higher realm in that brief time.

Now that it had realized the truth, it was too late.

*If I waste even a little more time here… then I’m finished.*

Erasure. Forever.

At the thought, a cold fear crawled up its spine.

The movement that followed was instinct, not reason.

The Doppelganger burned through the souls it had left without hesitation. It healed the body mangled by mana backlash, then gathered the energy that had once again filled it to the brim into both hands and unleashed it.

At the inhuman monster approaching it.

At Jin Taekyung.

*FWOOSH!*

The instant a blinding flash burst forth—

“No!”

The Skeleton King, who had been charging at the Doppelganger a step ahead of him, hurriedly twisted around and put himself in the flash’s path.

*POP!*

The Skeleton King in his usual state wouldn’t even have snorted at it.

For all his bluster, he accepted that Jin Taekyung was stronger than him.

But…

*Right now, I’m the only one who can protect that devious human.*

Protect him. Even if it meant putting himself in danger.

For the Skeleton King, it had become the most natural thing in the world.

Why?

At some point, he’d stopped thinking about the reason. Friends didn’t need a reason.

*SHWAA!*

The Skeleton King swung the Hero’s Sword down.

Golden magical power, bright as sunlight and strangely unlike magic, split the flash.

No.

The moment he thought he’d cut it, the flash passed through the blade like mist and swelled like a balloon.

*WHUM.*

*What the—*

Before the question in his mind could finish, a light far brighter than the last filled the Skeleton King’s vision.

*FWOOSH!*

The whole world turned white.

In that blinding flash, which would have instantly robbed an ordinary human of their sight, the Skeleton King belatedly remembered the answer to his question.

*Damn it.*

There was no doubt.

This was Light magic, something even mid- and lower-level mages could cast with ease.

A simple convenience spell, rarely used in actual combat because it had little killing power and produced only a faint light.

At least, that was what the Skeleton King knew. Hunters accepted it as established fact, too.

If he’d known that Siegfried Bassman, a scholarly Grand Mage, had shut himself away in his hideout to study countless spells, and had increased the power and usefulness of Light magic by several levels, he could have prepared for it.

But the milk had already been spilled. The painful mistake was enough to make the Skeleton King’s heart sink.

*I can’t see. Anything.*

He hadn’t lost his sight completely.

The Skeleton King was undead, after all, with a vitality that couldn’t be compared to that of a human made of flesh and blood.

But even temporarily losing his sight while fighting a powerful enemy like the Doppelganger—and having to protect someone else at the same time—was a mistake he couldn’t take back.

*It planned this from the start. It knew I’d step in…*

In the white world where he couldn’t see a thing, the Skeleton King raised his sword. With his sight gone, his hearing took in everything around him.

The roar of rubble crashing down a moment later.

An unfamiliar cracking sound from somewhere above.

And then…

A low voice, too quiet for any other being to hear, reached his ear.

—Don’t let it get away.

“……!”

The Skeleton King heard Jin Taekyung’s Sound Transmission and understood.

Why no magic had come flying at him, even though this was the perfect chance to knock him down.

And what the energy being carried quietly through the air was.

*Teleport!*

The Skeleton King’s guess was right.

The Doppelganger was now pouring all its strength into drawing a Teleport magic circle.

It felt both relief and regret at having taken the soul of an exceptional Grand Mage.

*You piece of shit…!*

The Doppelganger’s nature might be that of a monster familiar with magical power, but right now it was in the body of an ordinary human.

If it tried to cast Teleport without a magic circle just to get as far as possible from the monster named Jin Taekyung, it would crumble into dust without even a chance to resurrect.

*Fwoosh.*

Mana flowed from the Doppelganger’s hand as it swept through the air, slowly wrapping around its body.

Completing the magic circle would take a little time, but it would cut the risk by more than half.

Instead of its body being disintegrated without a trace, it might at least save its upper half.

That was more than enough for the Doppelganger to survive. And the deep-abyss monster, which had lived for countless ages, would never allow an intruder to interfere with this careful matter of its own survival.

*Whoosh. CLANG!*

It happened in an instant.

A bone fragment shot in with a sharp whistle and was deflected by the defensive magic the Doppelganger hurriedly cast.

*SH-SH-SH-SH! CLANG!*

The Doppelganger’s face twisted as it watched the Skeleton King fire bone fragments without pause, with the magic circle almost complete.

*What? The effect should last much longer.*

According to the Grand Mage’s memories, the spell was perfect. It had taken away the Skeleton King’s sight by striking the weakness precisely.

Losing your sight in battle was like losing the use of both legs.

That was exactly why the Doppelganger hadn’t bothered trying to disable the Skeleton King any further.

He was no pushover, and escaping as far away as possible from Jin Taekyung—who might do who knew what next—was more urgent.

But right now, the Skeleton King’s movements were far beyond anything the Doppelganger had expected.

*CRASH!*

The bone fragments, shot with incredible speed and force—and, above all, in a precise direction—finally shattered the defensive magic.

The Doppelganger’s eyes widened in confusion as it escaped the danger with a Blink spell, taking advantage of that instant opening.

*How the hell…*

It could tell from each of its opponent’s movements. Those attacks weren’t possible without certainty.

Even though the Skeleton King had taken the full force of the Light magic, he continued his attacks without the slightest hesitation.

*POP.*

His hazy form shot across the space. At the same time, the golden magical power coating his sword traced a graceful arc.

As the sword’s wielder willed.

And as the voice in his ear directed.

—One step left.

At that moment—

*SHWAAK!*

The Skeleton King’s unhesitating charge wavered.

An ice spear grazed the golden hair whipping through the air and slammed into a pile of rubble.

*BOOM! CRACK-CRACK!*

The air turned cold. The Skeleton King followed his senses and the Sound Transmissions reaching his ears.

—Three steps right. A horizontal slash.

*SHHK!*

Binding magic, which summoned vines to ensnare the target.

The thick, tough vines, like chains, were severed in an instant.

—Duck.

Dozens of Magic Missiles shot through empty air.

—Ten steps forward. Pierce it.

*BOOM-BOOM-BOOM!*

As expected of magic cast with a Grand Mage’s power, it was strong, and the explosions were spectacular.

But not a single spell touched the Skeleton King. The Doppelganger swallowed a startled breath as he closed to within ten steps.

*Already…!*

The Doppelganger felt as though it had been bewitched by a ghost.

He fired bone fragments without pause, disrupting the completion of the magic circle, and dodged or cut through every attack spell, foiling them all.

*Was he always this strong? That mutant?*

But the question disappeared without a trace the moment the Doppelganger saw the Skeleton King’s unfocused eyes.

A shock like a bucket of cold water filled the empty space where the question had been.

*It was him. From the start.*

What on earth had he done?

How could he be barely standing, as if he were about to collapse at any moment, and still render the Doppelganger this helpless?

The Doppelganger felt both confusion and fear as it gathered its mana.

Blink magic.

That instant flicker put distance between it and the Skeleton King once again.

Or so it thought.

Just before several meters of space disappeared, the voice that reached the Skeleton King’s ear came before the Blink spell could take effect. Without it, that was certainly what would have happened.

—Five o’clock. Move forward and—

Before the Doppelganger’s form could blur, the Skeleton King changed direction and charged, raising his sword.

*Fwooooosh.*

In the slowed world, brilliant golden magical power surged like a wave.

Then, with the voice that followed, it cleaved through space.

—From the sky to the ends of the earth. Bring it down.

*SHWAAK!*

A streak of golden light cleaved the deep-abyss monster standing in the spot that had been empty only moments before.

*SHHK. FWOOSH!*

A red line ran from the crown of its head down to its crotch.

Blood burst out, and a Sound Transmission that sounded like a groan reached the Skeleton King’s ear.

—Ah, shit. Right. My EXP.
## Chapter artifact 829

# Chapter 829

The Doppelganger.

The last abyss, which had existed for hundreds of years, saw and felt everything in the slow passage of time.

The Skeleton King charging toward it.

Blink magic to put some distance between them.

And…

*SHWAK.*

Along with a soft rush of air that suddenly reached its ears, a golden flash of swordlight filled its vision.

It all happened in the blink of an eye—and ended in the blink of an eye.

The monster of the abyss, born in the deepest reaches of the Demon Realm, couldn’t react at all. It happened that fast.

*Slice.*

Hot.

The strike it could neither block nor dodge split its crown. It carved through flesh and bone, devoured its organs and mana, and raced down to its crotch.

Like a bolt of lightning.

*Ah.*

The Doppelganger staggered backward with a silent sigh.

No—at the moment it felt itself take a step, it crumpled, spraying a fountain of blood.

*SPURT!*

Its blood-red view tilted slowly.

As the Doppelganger recognized the sudden arrival of death, the chain around its soul—wound tight for the past three years—was torn away.

*Siegfried Bassman.*

The Doppelganger could feel it clearly.

The mana, memories, and carefully hoarded vitality of the Grand Mage once hailed as a hero were draining away like the tide.

The ticket for the last flight out of here had just sold out.

*Splash.*

The body, split cleanly in two, crashed into a pool of blood.

A death no one could deny.

And a resurrection that defied the natural order.

*Pop!*

Reborn in a new life, in a new body, the Doppelganger threw itself forward without hesitation.

It had failed to escape using Teleport magic, but there was still a way out.

*I’ll get as far away as possible. Even if I have to spend every life I have left!*

It had lived for hundreds of years.

Throughout that long life, it had survived by prostrating itself at the king’s feet—and had been promised certain rewards on the day that would soon arrive.

A commander of one of the Demon Realm’s seventy-two legions? Even those arrogant, mighty beings couldn’t dare dream of sharing a glory like its own.

No, many of them had already died anyway.

It had laughed so hard when it learned that Leviathan, one of the commanders, had been killed by Jin Taekyung.

But it couldn’t die like this. Not when it was destined to stand at the Great King’s right hand.

*I have to survive. I can’t die here.*

The Doppelganger ran with all its strength.

Toward an exit from the temple it had hidden away in case of emergency.

Toward the countless glories waiting for it in the near future.

And only then did it realize.

At this very moment, only its lower half was running to save its life.

*Slice—*

The delayed sound of something being cut reached its ears.

The Doppelganger’s upper half, already severed, tilted in midair.

Its eyes, looking down at the lower half as it ran on with its original strength, held a distant, dazed look. It didn’t even know its body had been split apart.

“You son of a—”

*SH-SH-SH-SH!*

The forceful rush of air swallowed the unfinished words.

As the upper half burst into dozens of pieces and scattered through the air, the Skeleton King’s sword moved once more.

*Thrust!*

“Ghk.”

A suppressed groan.

In one small piece of its body, the Doppelganger gained a new body and was reborn, as if the gruesome death moments ago had never happened. It writhed.

Even with its chest pierced, its bloodshot eyes were fixed solely on the exit.

*Damn it. Damn it!*

The Doppelganger cursed soundlessly, regretting everything.

How many souls had it stolen from humans over the past thirty years? And how many of them had been people called strong?

It didn’t know. Even the Doppelganger itself couldn’t count them all.

It had all been little more than a harvest. Like a chicken farmer gathering the eggs his hens laid each morning, the Doppelganger collected human souls, and spent most of them without a second thought.

It didn’t matter.

No matter how much it used up, it could simply replenish them. Even without replenishing them, it had more than enough.

No—it had had more than enough.

At least, until today, when it met a monster wearing a human’s skin.

*Swish.*

A cold breeze brushed its nape. As a razor-sharp blade sliced through its neck, death and rebirth arrived together.

No—they repeated endlessly, like a broken record.

*Slice! Thrust! SH-SH-SH!*

It was cut, stabbed, and broken into dozens of pieces that scattered through the air.

Each time, the Doppelganger died and came back in the form of a man, a woman, or an old person. It drew on the powers and memories it had stolen from them as it edged closer to the exit.

A hundred meters narrowed to dozens.

Dozens of meters narrowed to a few.

It threw away its lives one by one, each now precious rather than a mere expendable resource.

*I can’t… I can’t lose any more.*

Fear rose at the word *Erasure*.

The lives that had once numbered around a thousand were nowhere to be found.

Feeling its vitality dwindle until it could count what remained on both hands, the Doppelganger summoned every ounce of strength and stood up again.

*Slide. WHOOSH!*

Its body regenerated in an instant, like a beanstalk shooting up in an old fairy tale. With a grotesque rebirth that words couldn’t explain, the Doppelganger hurriedly rolled away.

*Slash!*

A pain like a burn raked down its back.

But its desire to survive was stronger than the pain that lingered. As the Doppelganger threw itself forward, heedless of its life, the Skeleton King reached out without hesitation.

*Thud-thud-thud!*

Its body staggered.

The Doppelganger swallowed a surge of blood.

It saw something pure white jutting out from the middle of its chest. At the same time, another fragment of bone had pierced its calf and lodged deep in the ground.

“Where do you think you’re going?”

With the Skeleton King’s voice sinking low, wind rushed in from behind.

Feeling the Skeleton King’s presence rapidly closing in, the Doppelganger gritted its teeth. The bone fragment pinning its calf to the ground was as solid as a stake.

*Crack!*

Though far below the Skeleton King, its new body was still strong enough to be called an A-rank Hunter.

The Doppelganger tore off its leg below the knee and moved its one remaining leg.

It gathered all its strength and kicked off the ground.

*BOOM!*

A deafening crash, and a fierce wind swept over its body.

The Doppelganger’s eyes burned with longing as it stared at the temple entrance, now right in front of it.

Just this once. If only it could get out of here.

If only it could somehow avoid Erasure…

*I swear, I’ll turn the world you tried to protect into ashes.*

And just as it reached out toward the secret door, open only to it—

*SHWEEEE!*

From somewhere far away—

*CRUNCH!*

A streak of light tore through space and swallowed the Doppelganger whole. It ripped and smashed it to pieces.

In the darkness that flooded its vision, someone’s voice pierced its ears.

“You fucking bastard. You invite a guest over and then try to leave?”

How cold that voice sounded.

And how hot the flames bursting from the spearhead buried in its body.

*Fwoosh.*

*ROOOAR!*

In a view dyed entirely blue and white, the Doppelganger writhed, engulfed in blue-white flames, unable even to scream.

Until the body that had once belonged to someone else burned to ash along with every last bit of its vitality.

Until, where all the lies it had piled up had burned away, only a single truth remained.

*Step. Step.*

*Whoosh.*

Wind swept through the unsteady footsteps, scattering the ash.

Among the ash that had settled in a thick layer, a black and ashen-white shadow stirred.

“…So that’s it.”

Jin Taekyung stood before it, supported by the Skeleton King. He looked down at the shadow with a faint light in his eyes.

The sole truth of a being built entirely from lies. He had pierced through to its pathetic essence.

> **System**
> **Level 10 Doppelganger**

“Turns out this is all you were.”

The shadow trembled—no, the Doppelganger trembled.

* * *

Just standing there was enough to leave me gasping.

As my senses slowly faded and my vision blurred, the pounding of my heart echoed like thunder.

*Thump. Thump-thump.*

Was this the price of pouring all my strength into that final strike?

My whole body trembled. If the Skeleton King hadn’t been supporting me, I would’ve collapsed long ago.

But I didn’t collapse.

Even now, I pushed back the sleep demon pressing in from every direction, pulled away from the Skeleton King’s support, and stood tall on my own two feet.

Then I looked down.

At a shadow as small as a child, yet made of an evil so pure it couldn’t be compared to any child’s.

At the hideous being that was now nothing more than a shadow.

“Yeah. This was all you were.”

I muttered the words I’d said earlier, almost to myself.

Looking at the Doppelganger trembling as if afraid, at the Level window floating over its head, I couldn’t help but feel a bitter laugh bubbling up.

> **System**
> **Level 10 Doppelganger**

Level 10.

That was all. Nothing more, nothing less.

For a Hunter, it was at the bottom of F-rank. For a Murim practitioner, it was about the level of a Third Rate swordsman who’d only just begun to sense internal energy.

That was the Doppelganger’s essence, confirmed by the *Eye of Truth*. Its origin, and the one and only truth.

*To think, a thing like this…*

I swallowed the words rising in me and clenched my teeth.

When I closed my eyes, flames flickered in the darkness.

A city in ruins.

Among the smoke rising from every corner, I saw bodies strewn about. The screams of those still alive echoed in my ears.

How many people had died because of the Doppelganger’s terrorist attacks, because of the monsters?

How many had lost their homes and had to say goodbye to their precious family and friends?

Hundreds of thousands? Millions?

I didn’t know.

More than thirty years had passed since the Doppelganger had slipped into this world. I couldn’t even begin to guess what it had done behind the scenes.

*Grind.*

My fists clenched tight.

I felt red drops of blood run between my nails, which had dug deep into my skin. I opened my eyes, but nothing had disappeared.

Not the ruined city. Not the emptiness in the dead people’s eyes or the cries of those still alive.

My mind remembered it all. It was branded into my eyes and ears, impossible to erase.

And the only thing among all of that, the only thing before my eyes, was this one being.

*Crush.*

“Ghk. Guhh…”

The energy in my foot crushed the shadow.

The Doppelganger, writhing and groaning, begged me for mercy. It could feel pain, even in this cursed form.

“S-save…”

“Save you?”

“Y-yes. Anything. I’ll do anything! I swear!”

I found myself staring down at it, momentarily dazed. Then I gathered the internal energy I had left and sent it surging through my foot.

*Crack. Crunch!*

“AAAGH!”

I just watched the Doppelganger scream.

Then the Skeleton King suddenly placed a hand on my shoulder.

“Human.”

“What?”

I’d only asked him a question, but when the Skeleton King met my gaze, he quietly moved his lips.

“…Nothing.”

What kind of expression did I have on my face right now? Was I tired and worn out? Or was my face twisted with a rage I’d never shown before?

It was probably the latter.

The Doppelganger had been writhing in pain, but when it saw my expression, it stopped screaming.

Then it said this in a voice filled with terror:

“I-I didn’t want to do it! Have you forgotten? It was all on the king’s orders!”

The king.

Demon King Asmodeus.

At the name that rose with its cry, the anger that had seized my body and mind wavered.

# Checkpoint Review — 365–369

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

# Chapters 365–369

## Plot

Jin Taekyung reaches the Supreme Peak realm, advances the Fire Gate Divine Technique and Fire Dragon Divine Spear to the eighth stage, and manifests Force. Fighting beside Jeok Cheongang, he severely wounds the Western Heaven Demon Lord before the Lord of Heaven possesses the Demon Lord’s body. Taekyung destroys the borrowed body with One Annihilation, but the possessing entity escapes and promises to return. Taekyung collapses, and the underground prison begins to collapse around them.

The Dark Heaven assault on the Sichuan Tang Clan, Qingcheng, and Emei is delayed or repelled by defenders and allied forces. Cheongpung defeats First Fiend’s techniques and Mungyeong, revealed as the Slaughter Saint and Dong Feng’s Master, kills First Fiend and massacres the attackers at the Tang Clan. Jeok escapes the prison carrying unconscious Taekyung and Dong Feng, whose dantian and martial arts were destroyed. Tang Sadok survives the Tang Clan’s fall, and Cheongpung begins treating him.

Five days later, Mungyeong pursues the Third Fiend, who escaped the Emei assault after Extinction Divine Nun and other defenders intervened. Disguised as First Fiend, Mungyeong lures the Third Fiend into an ambush, severs his wrist, and confronts him; the Third Fiend’s fate remains unresolved.

## Continuity

- Jin Taekyung is unconscious after reaching the Supreme Peak realm, manifesting Force, and exhausting himself. His Fire Gate Divine Technique and Fire Dragon Divine Spear are at the eighth stage, and White Flame remains in his possession.
- Jeok Cheongang escaped the collapsing underground prison with Taekyung and Dong Feng but remains severely weakened after exhausting his internal energy.
- Dong Feng is the Divine Physician; his dantian and martial arts were destroyed while shielding Jeok. Mungyeong, the Slaughter Saint, is Dong Feng’s Master.
- The Heavenly Power Demon’s corpse remains inside the collapsed prison.
- The Lord of Heaven escaped after possessing and destroying the Western Heaven Demon Lord’s body. The Demon Lord’s true fate is unknown.
- The Myriad-Poison Ring remains in Taekyung’s possession and cannot be appraised by the System.
- Mungyeong killed First Fiend and other Dark Heaven attackers and has intercepted the surviving Third Fiend.
- The Third Fiend attacked Emei and was wounded by Mungyeong; the Second Fiend’s fate after the Qingcheng assault is also unknown.
- Extinction Divine Nun is alive, a Supreme Peak master, and helped repel the Emei attack.
- Tang Sadok survived the destruction of the Sichuan Tang Clan but is gravely wounded; Cheongpung is treating him with True Qi Guidance.
- The Three-Gate Bloodbath devastated the Tang Clan, Qingcheng, and Emei, though their defenders and allies prevented complete destruction.

## Translation Decisions

- Use **Supreme Peak**, **Force**, **One Annihilation**, **Slaughter Saint**, **Three-Gate Bloodbath**, **Extinction Divine Nun**, and **Seven Fairies**.
- Render **삼괴** as **Third Fiend** for the individual and **Three Fiends** for the collective Qilian group.
- Retain **Fire Gate Divine Technique**, **Fire Dragon Divine Spear**, **White Flame**, **True Qi Guidance**, and **Demon-Subduing Dragon-Taming Formation**.
- Preserve Cheongpung’s dreamy, childlike voice, Mungyeong’s restrained authority, and Jin Taekyung’s profane, self-mocking narration.

## Durable state

{
  "active_continuity": [
    "Jeok Cheongang escaped the collapsing underground prison carrying unconscious Jin Taekyung and the awakened Divine Physician; the Heavenly Power Demon’s corpse remained inside.",
    "The Divine Physician is Dong Feng, whose dantian and martial arts were destroyed while shielding Jeok Cheongang; the Slaughter Saint is Dong Feng’s Master.",
    "Jeok Cheongang remains severely weakened after exhausting his internal energy while protecting Taekyung and Dong Feng.",
    "Mungyeong, the Slaughter Saint, killed First Fiend and at least one other Qilian Fiend, and has now intercepted the surviving Third Fiend after disguising himself as First Fiend.",
    "The Third Fiend led the Dark Heaven attack on Emei, escaped the battle, and was wounded by Mungyeong near Chengdu; his fate is unresolved.",
    "Extinction Divine Nun, Heaven-Shaking Venerable Nun’s only Senior Aunt, is an alive Supreme Peak master who emerged from presumed death and forced the Third Fiend to flee Emei.",
    "Jin Taekyung is unconscious after exhausting himself while seeking to save Jeok Cheongang.",
    "Jin Taekyung has reached the Supreme Peak realm through enlightenment and manifested Force; the Fire Gate Divine Technique and Fire Dragon Divine Spear remain at the eighth stage, and White Flame remains in his possession.",
    "The Lord of Heaven temporarily possessed the Western Heaven Demon Lord’s body, which crumbled after One Annihilation; the possessing entity escaped after promising to return.",
    "The Myriad-Poison Ring remains in Jin Taekyung’s possession and cannot be appraised by the System.",
    "Cheongpung remains a Supreme Peak master and has begun treating the gravely wounded Tang Sadok with True Qi Guidance.",
    "Most Dark Heaven remnants from the Sichuan assault have been hunted down or captured, but the fate of the Second Fiend and the Third Fiend remains unresolved."
  ],
  "continuity_sources": [
    369
  ],
  "open_questions": [
    "What becomes of the Third Fiend after Mungyeong severs his wrist and confronts him?",
    "What happened to the Second Fiend who was assigned to the Qingcheng attack?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?",
    "Can Jin Taekyung recover, and can Jeok Cheongang protect him and Dong Feng from Dark Heaven and the Slaughter Saint?",
    "What is the full nature of the Slaughter Saint’s connection to the identity or name Mungyeong?"
  ],
  "safe_through": 369,
  "temporary_decisions": [
    "Use Red Slaughter Demon and Red Slaughter Asura Net for 적살마 and 적살수라망; use First Captain for 일 단주 and deputy captain for 부단주.",
    "Use mechanism array for 기관진법.",
    "Maintain Cheongpung’s dreamy, childlike speech while rendering his copied techniques precisely.",
    "Use Ghost Illusory Slaughter Step for 유령환살보.",
    "Render 삼괴 as Third Fiend in singular contexts and Three Fiends only when the collective Qilian group is meant."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 365

# Chapter 365

*So this is what it feels like.*

The Supreme Peak realm. The domain of the great martial artists chosen by heaven.

I had taken a step into a place that had never been granted to me before, and I felt endless freedom.

How should I describe this feeling…

*This is incredible.*

A faint smile had already formed at the corners of my mouth.

Ding. Ding. Ding.

> **System**
>
> - The realm of **Fire Gate Divine Technique** has advanced to the eighth stage.
> - The realm of **Fire Dragon Divine Spear** has advanced to the eighth stage!
> - **Flamefire Path** has advanced to…!

System notifications announcing increases in various martial arts, along with Level Ups and achievement completions, rang out without pause.

Qi like molten lava surged from deep within my entire body. The darkness rushing toward Jeok Cheongang and me no longer frightened me in the slightest.

“Die!”

A scream-like shout. A face twisted like a fiend.

There was no trace left of the middle-aged man who had once worn a good-natured smile.

Only a monster consumed by killing intent remained.

Whoooosh!

The ink-black Sword Force, wrapped in savage killing intent, came crashing down like a bolt of lightning. I could feel the destructive power lurking within it just by looking at it.

But…

*In the end, you were human too.*

The Western Heaven Demon Lord was already exhausted from his injuries and fatigue, and his excessive rage had scattered his mind.

When the mind wavered, so did the qi. You could not pierce a boulder with a needle, but passing between grains of sand was not difficult.

Sss.

One step. As the tip of my foot pushed against the ground, space vanished.

Jeok Cheongang hurriedly shouted when he saw my back suddenly blocking his path.

“You little bastard, get back—”

His voice could not continue. Cyan-white energy was surging over the transparent spearhead of White Flame.

Filled with the heat of Extreme Yang, the energy connected toward itself like tangled threads, gathered together, and finally took shape.

A beautiful yet destructive concentration of internal energy. The exclusive province of great martial artists.

*Force.*

I had finally made it this far.

Trembling with joy, I thrust my arm toward the darkness rushing at me.

Ssssh!

A single line was drawn through the air. Cyan-white flames shot forward like an arrow and collided with the darkness.

Heavenly Strike.

The fire dragon's claws tore the ink-colored Force to pieces.

KRAAAAAA!

Amid the deafening roar, I could see it clearly. The scattering darkness. And the Western Heaven Demon Lord's face, twisted with rage and shock.

Blood and a howl poured from his mouth as the backlash of his shattered Force inflicted an Internal Injury.

“You dare—you dare!”

“What, you fucking bastard?”

*You’re fucking dead now.*

I smiled brightly and kicked off the ground. But someone had already shot toward the Western Heaven Demon Lord, one step ahead of me.

A small body. Jeok Cheongang, who had gathered the qi that had briefly fallen out of balance.

—I'll hear what happened later.

A short Sound Transmission followed.

—First, let's beat down that double-damned bastard.

It was the kind of comment that made me want to hit the Like button—or rather, it was a Sound Transmission.

* * *

The Western Heaven Demon Lord was stunned.

*How? How could this be happening?*

More than a hundred years of time. Several jiazi of internal energy. Everything he had built up until now was collapsing. Being denied.

And by a mere brat in his twenties!

*Could such a thing be possible?*

At this moment, the thought that flashed through the Western Heaven Demon Lord's mind went beyond doubt.

*Supernatural powers.*

A young man barely past twenty had manifested Force. And that was not all. He possessed the strength of a giant and the speed of the wind.

It was something that could not be explained without the aid of a ghost. And yet…

*You will be the ones who die.*

The Western Heaven Demon Lord clenched his teeth and planted his foot on the ground. At the same time, a powerful qi aura surged from his entire body and burst outward.

“Come!”

The Western Heaven Demon Lord roared like an injured tiger.

No—he really was an injured tiger. Fatigue accumulated through a long battle and exhausted internal energy. One wrist had been torn away, and one ankle had been broken. Because of a momentary misjudgment, he had even suffered an Internal Injury at the hands of a mere brat.

But even so, one fact remained unchanged.

“I am the Lord of Heaven’s loyal servant. So long as that person is with me, even death itself shall pass me by!”

The Western Heaven Demon Lord’s shout carried an almost heroic grandeur. Two voices—one old, one young—immediately followed.

“What kind of bullshit are you spouting now?”

“Sounds less like Dark Heaven and more like Darkcheonji.[^1] Hey, try saying, ‘Lee Man-ui is a son of a bitch.’”

[^1]: “Darkcheonji” and “Lee Man-ui” parody Shincheonji and its founder, Lee Man-hee; challenging a presumed follower to insult its leader is the joke.

Jeok Cheongang and Jin Taekyung.

Master and Disciple rushed forward like the wind and thrust out their arms at the same time.

KWAANG!

After a terrifying qi aura swept through the underground prison with a thunderous roar, blood began to flow from one man's mouth.

“Cough.”

The Western Heaven Demon Lord's body staggered slightly after absorbing the tremendous impact head-on.

Under normal circumstances, perhaps it would have been different. But for a man who had already suffered serious injuries, the joint attack of two Supreme Peak masters was truly threatening.

Even so, the Western Heaven Demon Lord did not give up.

*I’ll bring down one of them first.*

A young Disciple overflowing with strength thanks to the aid of a ghost, and an old Master suffering from the effects of his injuries.

Naturally, the Western Heaven Demon Lord chose the latter.

“Die!”

His leg swung like a whip.

Boom!

At the moment Jeok Cheongang blocked the terrifying kick with his hand and let out a low groan—

“How dare you touch him.”

Crack! Crunch!

The spear shaft struck upward like lightning and caught the Western Heaven Demon Lord beneath the jaw. His vision flashed white. The tremendous force, which even his Body-Protecting Qi could not fully absorb, snapped his jaw shut and severed his tongue.

The Western Heaven Demon Lord rose into the air from the pain and impact. Waiting for him were two hands wreathed in flame.

“This old man is the Fire King, you fucking bastard!”

Jeok Cheongang unleashed the Flame Divine Palm along with a thick curse.

BOOM!

The already unstable Body-Protecting Qi scattered. The heat of Extreme Yang seeped between the cracks in the Black Dragon Armor, which had split like a spiderweb.

Along with a pain like being burned alive, something hot surged up his throat.

“Gwaaaaaaagh!”

Black blood mixed with pieces of his organs sprayed out. Before the blood could even reach the ground, a brief sound of something cutting through the air pierced the Western Heaven Demon Lord's ears.

Ssssh-sh-sh-sh!

“……!”

Dozens of spear shadows appeared in the Western Heaven Demon Lord's bloodshot eyes, with burst blood vessels spreading across them.

As cyan-white flames flew through the air, scorching it in every direction, the Western Heaven Demon Lord dragged up every last bit of strength he possessed.

Ssssss!

Ink-colored Sword Force surged along his blade and collided with the spear shadows. Every clash produced a tremendous roar and shock wave that shook the underground prison and churned the Western Heaven Demon Lord's insides.

“Graaagh…!”

But it was not over.

“Do you have time to look away?”

At the sound of the cold voice, Jeok Cheongang's Flame-Extinguishing Divine Fist drove into the Western Heaven Demon Lord's side.

Crack! KRRRUNCH!

This was a punch unleashed with all the strength of Jeok Cheongang, the Fire King who was called the greatest among the Ten Kings.

Part of the Black Dragon Armor shattered along with the Body-Protecting Qi, unable to withstand the enormous impact. Flesh burned, and bones broke.

“Gaaaaah!”

A horrific scream reverberated. Even as he writhed in agony, the Western Heaven Demon Lord drew up every bit of his remaining internal energy and unleashed it in all directions.

BOOM! KWA-KWAKWANG!

The ground, ceiling, pillars, and rocks. The manifested ink-colored Force shot out without discrimination. Everything it touched turned to dust or was sliced apart like tofu.

Yet the two people who should have been its targets had already torn through the net of Force and reached the Western Heaven Demon Lord.

Shhk!

The Force gathered on the transparent spearhead slashed diagonally through the Western Heaven Demon Lord's upper body, while the two flame-wreathed palms struck his collapsing chest.

BOOM! KWAANG!

“……!”

The Western Heaven Demon Lord's body was hurled away like a cannonball, accompanied by an unimaginable pain he had never experienced before. It smashed through solid rock and buried itself deep in the wall.

“Ghk, ghek.”

The Western Heaven Demon Lord blinked with a bizarre groan. Through his blurred vision, he saw two people walking toward him.

*Is this how I die?*

The Western Heaven Demon Lord thought blankly.

For a long time, he had reigned as a powerful figure. He had enjoyed trampling the weak and taking away the things they cherished.

Every ordinary martial artist in Murim thought about death at least once. But not the Western Heaven Demon Lord.

The only beings in the world who should have been capable of taking his life were himself and the one sole, dignified existence known as the Lord of Heaven.

And yet…

“How dare you wretches try to kill my servant?”

A dry voice, like grains of sand in a desert, slipped between his blood-soaked lips.

There was no pain or reason in the Western Heaven Demon Lord's voice.

His two eyes, shining with pure bloodlight, were no longer human.

Nor did they belong to the Western Heaven Demon Lord anymore.

“As this body descends to earth from heaven, kneel—from the lowest to the highest.”

At that moment, Jeok Cheongang and Jin Taekyung shouted like thunder.

“No way…”

“The Lord of Heaven!”

Rumble-rumble!

A terrifying energy spread from the Western Heaven Demon Lord—or rather, from the being temporarily borrowing his body—and shook the ground and ceiling.

An ink-colored current writhed like a tentacle from the stump of his torn-off arm, slowly sealing the wound that had been gushing blood like a waterfall.

“Worship me. Submit before omnipotent power.”

Plop. Plop.

The Western Heaven Demon Lord's body slowly rose.

With every step he took toward them, manifested internal energy spread out behind him like wings.

And then—

“……!”

Everything stopped. The trembling, the wind, even the drifting dust and the movement of the air.

In that world where everything had stopped, a streak of darkness shot forward.

Ssssss!

The darkness approached without a sound and swallowed them both.

No—it would have, if not for the spearhead that thrust out, cleaving through a flow of time divided into ever-finer instants.

Gooooooong—

Wind and qi condensed around the spearhead, then burst out like an explosion. The spearhead, carrying cyan-white flames, advanced while erasing everything in its path.

One Annihilation.

A blinding flash erupted.

* * *

When time began to flow again, it brought with it pain that made my entire body feel as though it were breaking apart, along with complete exhaustion.

*I want to collapse just like this.*

My arms and legs, my fingers, even every individual strand of muscle. Every part of my body felt as though it might snap at any moment.

But I held on with superhuman strength.

*Not yet. Not yet.*

At the very least, I did not want to collapse before him.

“So die already, you fucking bastard.”

I raised my head and looked at the Western Heaven Demon Lord—or rather, the thing borrowing the Western Heaven Demon Lord's body.

After confirming that his entire body had been burned black and that a hole had been blown through his chest, the corners of his mouth slowly lifted.

“Interesting. Very interesting.”

Fwoosh.

No sooner had he finished speaking than his fingers turned to ash and scattered. In a breeze that had come from somewhere, his body slowly began to crumble.

But the thing borrowing another person's body could not feel pain. Instead, it tossed out a single line with a laugh.

“We’ll meet again next time.”

I barely raised my middle finger.

“Go eat a dick.”

No answer came.

Beyond the drifting ash, System notifications announcing Quest success and Level Up rang out.

But the mental fatigue caused by the battle did not recover.

I only wanted to collapse right there. No—I was already in the process of collapsing.

Grab.

A wrinkled hand caught my shoulder.

It belonged to Jeok Cheongang, the Fire King. When I saw his welcome face, I suddenly remembered something I needed to say.

“How was it?”

“What?”

“One Annihilation. It was incredible, right?”

The concern filling Jeok Cheongang's face slowly faded. Before long, a gentle smile formed on his lips.

“Yes. It was incredible.”

That was enough.

Alongside an answer that never escaped my lips, I closed my eyes. The sound of the underground prison collapsing echoed faintly in the distance.
## Chapter artifact 366

# Chapter 366

Drip. Drip-drip-drip.

The world was submerged in a darkness so deep that it was impossible to tell how much time had passed.

The sky was filled with black clouds, and the rain that had seemed like a passing shower refused to stop.

Within the grounds of the Sichuan Tang Clan, near a puddle of spilled blood, corpses had piled up into a small hill.

“So? How are things inside?”

At the gates of the Sichuan Tang Clan, a black-clad man was sitting astride the corpse of an unknown Tang Clan martial artist. A subordinate who had just arrived from the Inner Hall answered his question.

“The situation still hasn’t ended. I hear about a hundred of them are left.”

“What? That many?”

“Only half of them are martial artists. The rest are craftsmen who haven’t learned martial arts, women, or children.”

“Then they should just wipe them out without a second thought. What kind of pointless nonsense are they doing?”

The black-clad man’s dissatisfaction was only natural. It was unpleasant enough to be stuck guarding the entrance while others made accomplishments. The fact that this tedious gatekeeping still had not ended irritated him even more.

“Well, you see…”

“Is there some reason?”

Seeing his superior frown, the subordinate hurriedly continued.

“The surviving Tang Clan martial artists are elites, for one thing. But it seems the Tang Clan activated a mechanism array, which has delayed things.”

“A mechanism array? If it’s a poison array, it shouldn’t be difficult to break through.”

“It isn’t poison. It’s explosives. They had hidden Heaven-Shaking Thunder.”

“……You don’t mean the Heaven-Shaking Thunder of the Pyeokryeomun,[^1] do you?”

[^1]: The Pyeokryeomun was a martial sect that had been destroyed long ago.

“It seems so. Because some of them charged in carrying Heaven-Shaking Thunder and died in the explosions, quite a few of our brothers suffered serious losses.”

“Ha. Would you look at these lunatics?”

The black-clad man’s mouth fell open. He had wondered what was happening when the ominous booms began echoing around them. He had never expected the Tang Clan to possess Heaven-Shaking Thunder from the Pyeokryeomun, a sect that had been destroyed long ago.

He could now understand, to some extent, why the battle had been delayed.

“Wait. Then what has the Demon Lord been doing? He should have been able to slaughter them all by himself.”

The black-clad man’s question was founded on his unwavering faith in the Western Heaven Demon Lord.

That was only natural. The Western Heaven Demon Lord was one of the few servants permitted to pay respects to the exalted Lord of Heaven, and he possessed terrifying martial might.

The black-clad man did not know how powerful the Heaven-Shaking Thunder he had only heard about was. But even if the grandfather of Heaven-Shaking Thunder itself appeared, it would not be able to harm the Western Heaven Demon Lord.

“I heard he went to the Tang Clan’s underground prison an hour ago.”

The subordinate’s answer made the black-clad man nod.

If the Demon Lord had moved personally, there had to be a reason. He would resolve the matter without the slightest mistake. The black-clad man felt not even a trace of worry or doubt.

Nor was that thought unique to him. Everyone felt the same way.

“Then what about the First Captain?”

First Captain was the post that First Fiend, the eldest of the Qilian Three Fiends, had assumed upon entering the Western Heaven Demon Lord’s service.

After hesitating briefly, the subordinate answered.

“He’s engaged in a life-and-death duel with the Sword Saint’s successor in the Inner Hall. No one has been able to approach him since one of our brothers who went to deliver news about the Heaven-Shaking Thunder lost his head.”

“……I see.”

The black-clad man said no more.

If his feelings toward the Western Heaven Demon Lord were reverence and trust, what he felt toward First Fiend was fear. He had no desire to complain carelessly and meet a horrible end.

“Um, Captain.”

“Do you have something to say?”

“Yes. The deputy captain asked about the brothers who went to Qingcheng and Emei.”

“A message arrived just before you got here.”

The black-clad man handed him a small tube. After checking its contents, the subordinate raised his head with a bewildered expression.

“This is…”

“It came from Emei.”

“Is this the only one?”

“Yes. We still haven’t received anything from Qingcheng.”

“I believe the time for it to arrive has already passed.”

“That’s true. But you know what the other captains are like.”

The three brothers of the Qilian Three Fiends resembled one another in more than their ugly appearances.

They were all cruel and eccentric, fiends who went wild at the sight of blood.

The Third Fiend, who had been assigned to Emei Sect, was somewhat better than the others. At least he had sent a messenger eagle at the appointed time.

The problem was that the situation described in the letter from Emei was not progressing smoothly.

*The Beggars’ Sect got involved.*

The letter said that Beggars’ Sect disciples carrying bamboo staffs and dog clubs had suddenly appeared.

Their individual martial arts could not compare to those of Dark Heaven’s martial artists, but the meaning behind their appearance was significant.

*They’ve already caught our scent.*

The attack had been calculated down to the last detail. A battle that should have ended quickly was dragging on. Even so, the black-clad man had no doubt that their side would win despite this unexpected variable.

Just as he was casting off the unease that had briefly touched him, he suddenly raised his head.

“Hmm?”

“What is it?”

“What’s that?”

At the black-clad man’s questioning voice, not only the subordinate who had brought news from the Inner Hall but also the thirty-odd martial artists scattered at regular intervals to guard the walls gathered around their superior.

And soon, they saw it.

Beyond the collapsed wall, a streak of wind cutting through the sheets of rain.

It moved fast enough to be called a ray of light. Then it burst into a dazzling flash.

Ssshhhhhhk—crack!

The thirty-odd martial artists blinked. When they reflexively touched their faces, sticky blood came away on their fingers.

Slowly—very slowly—their mouths fell open and their heads turned.

In the slowed-down world, they saw their superior’s body collapse like a rotten old tree.

A hole the size of a fingernail had been punched through the center of his forehead.

“……!”

It felt as if something had struck them across the backs of their heads.

Their superior was a Peak master capable of making a name for himself anywhere under heaven. And yet a man with such skill had met his death from a blow they could not even see.

Before anyone present could recover from that tremendous shock, a figure sprang up onto the wall.

And then—

Ssssh-sh-sh-sh!

In the darkness, rays of light filled with death plunged down like lightning.

* * *

First Fiend was on the verge of going insane.

No—he had already been insane for more than fifty years. He was merely becoming even more of a lunatic.

“Why! Why! How could this be!”

Boom! Boom! Boom!

Blood-red Force surged from the twin axes in his hands, smashing and cleaving everything around him.

The sturdy pavilion where the Family Head of the Sichuan Tang Clan had once lived had long since become a ruin.

A figure was darting back and forth through it.

“Ah! Eeng! Eek! Whoosh!”

Cheongpung hopped and skipped around, dodging the Force with strange noises. First Fiend’s eyes rolled white.

“You fucking bas—!”

It was enough to drive him mad.

His opponent was a blood-brat who was not yet thirty. No matter how unprecedented a monster he was—a man who had received the Sword Saint’s teachings and reached the Supreme Peak realm in his twenties—the gap that came from age could not simply be ignored.

First Fiend was an old monster from two generations back. He possessed immense internal energy, experience, and martial arts of the highest realm.

That was why, although he had been surprised at first, he had not felt any particular sense of danger.

*The Sword Saint raised quite a monster. There must have been a reason the Demon Lord warned me before he left. But he’s still far from being able to face this old man. Heh heh heh.*

However, it did not take long for the smile at the corners of his mouth to turn into fury.

“Die! I said die!”

With a mad shout, the twin axes slashed down through the air. A net of Force spread wide and fell over Cheongpung’s head.

The Red Slaughter Asura Net.

It was one of the signature techniques left behind by the Red Slaughter Demon, a fiend who had dyed the martial world red with blood three hundred years ago.

The unparalleled slaughter saint, pursued by the Central Plains Murim as a public enemy, had met his end in an unknown cave in the Qilian Mountains. The three brothers who had gone into hiding to escape the people of the martial world had learned the martial arts manual he left behind and emerged reborn as the Qilian Three Fiends.

And now, the ultimate form of the Red Slaughter Asura Net—a technique no one had been able to perform since the Red Slaughter Demon—was finally being recreated through First Fiend’s twin axes.

Whoooosh!

That was when Cheongpung’s eyes sank deeply as he stared at the red Force net rushing toward him from every direction.

Shaaah—

A cool breeze blew.

At the same time, purple Sword Force wrapped around the straight blade of his sword and sliced diagonally through the net of Force.

Slice!

First Fiend’s mouth fell open as Cheongpung’s One-Character Wisdom Sword dismantled the ultimate Red Slaughter Asura Net with such ease.

“You—you knew the Red Slaughter Demon’s martial arts?”

No perfect martial art existed.

Every martial art left behind by the Red Slaughter Demon could be called a signature technique, but each clearly had weaknesses. Those weaknesses were a secret known only to the Qilian Three Fiends.

And yet the blood-brat before him had seen through them precisely.

“Answer me this instant!”

Cheongpung’s reply came the next moment. It was short and simple.

“What’s the Red Slaughter Demon? I’ve never heard of him before.”

“……What?”

“Oh, is that why you’re upset?”

Cheongpung tilted his head and continued.

“I could just see it.”

“It showed itself?”

“If you keep looking at something, you start to understand it. Grandpa has more internal energy than I do, and your martial arts are more complicated, so it took a little longer.”

“It took longer?”

“Yes. But I don’t think I need to take that long anymore.”

“……!”

First Fiend understood what Cheongpung’s final words meant the next moment.

Ssssh!

A purple flash filled his vision.

First Fiend hurriedly whirled the axes in both hands like lightning against the sword strike that came without warning.

The Red Slaughter Eighteen Axes lacked sophistication in its martial theory, but its destructive power was unparalleled. With more than two jiazi of internal energy added to it, its strength seemed capable of splitting heaven and earth.

However…

Kagagagak!

The smoothly extending blade guided one axe blade aside. Then it struck the other axe that had been driving toward Cheongpung’s side.

KWAANG!

With a thunderous boom, First Fiend’s body staggered. He had effectively slammed the two axes in his own hands together. Even as he retreated, he could only stare in stunned disbelief.

*W-What on earth just happened?*

Pop!

Cheongpung shot toward First Fiend.

His clear eyes had sunk deeply, and sunset-colored purple energy surged from the blade of his sword.

Whooooom!

First Fiend stared blankly at the strike descending toward the crown of his head.

*Th-This is…*

There was no mistake.

The Red Slaughter Eighteen Axes.

No—this martial art should now be called the Red Slaughter Eighteen Swords.

In less than a shichen, Cheongpung had not only seen through and dismantled First Fiend’s martial arts. He was making them his own.

*How can this be!*

First Fiend swung his twin axes with a silent cry of shock.

The tremendous shock had slowed his reactions, but it was not enough to prevent him from countering.

That was what he thought, at least—until Cheongpung’s sword moved.

Whoooong.

A blunt, destructive sword technique descended gently like a falling flower. Thirty-six plum blossoms bloomed from the tip of the sword and fell through the air.

A martial art surfaced in First Fiend’s mind.

*The Thirty-Six Plum Blossom Swords.*

At the same time, he realized.

*I can’t avoid it.*

Ssssh-sh-sh-sh!

Thirty-six plum blossoms—or rather, Force—wrapped around First Fiend’s entire body.

With blood spreading like mist, First Fiend staggered backward, his entire body covered in slashes.

Fear appeared in his eyes as he stared at Cheongpung, whose sword hung loosely at his side.

“Cough. You… You are…”

“It’s fortunate that it’s raining.”

Cheongpung stepped forward, his voice calm.

“I don’t like the smell of blood.”

Squelch.

Cheongpung’s foot stepped into a red puddle where raindrops and blood had mixed together. First Fiend let out a tearing scream.

“Anyone! Is there no one out there? Hurry, get this bastard…!”

At that moment, a low voice slipped into his ear.

“Don’t call out. There’s no one here.”

“……!”

“……!”

There had been no footsteps and no sign of anyone’s presence.

And yet he was there.

The raindrops pouring down overhead shattered in midair before they could touch him.

“Who the hell are you—”

Slice!

First Fiend’s head flew into the air.

Cheongpung flicked the blood from his sword, then stared with a rigid expression at *him*, standing tall before him.

“I want to ask you that instead. Who are you?”

Cheongpung continued in a faintly trembling voice.

“Mungyeong.”
## Chapter artifact 367

# Chapter 367

The signs had already been there.

There was more than enough reason.

Rumble, rumble, rumble!

The ground split apart, and the ceiling shook. The underground prison that had symbolized the darkness of the Sichuan Tang Clan for hundreds of years could not withstand the aftermath of the successive battles and was collapsing.

Along with the countless vengeful spirits of prisoners who had died in the prison—and the three people who were still alive and well.

“……What the fucking hell is this?”

Jeok Cheongang looked around with an incredulous expression.

Before he had closed his eyes, he had definitely been in a forest. When he opened them, he was in a cave that might or might not have been a prison.

And that wasn’t all. He had dragged his still-ailing old body into a fight to the death against some unknown son of a bitch.

Fine. He could understand things up to that point. Jin Taekyung passing out the moment the battle ended? That, too, was entirely possible.

But…

“No, isn’t this taking things too far? Fuck.”

This was the kind of situation that made profanity slip out on its own.

Where was this place? Who was I? Why was the ground splitting apart, and why were boulders the size of people raining down from overhead?

For a moment, Jeok Cheongang was overcome by deep regret and nearly ascended to immortality.

“Goddamn it.”

He had no idea what was happening, but first he had to get himself to safety.

Once his thoughts straightened out, his movements followed with the speed of lightning.

*First, I need to take care of Taekyung… But who the hell is this old man?*

*Ah, hell. Whatever.*

With unconscious Jin Taekyung and the Divine Physician slung over his shoulders, Jeok Cheongang hurriedly shot forward.

Sssshhhk! Boom!

A massive rock that fell from the ceiling grazed Jeok Cheongang by a hair and smashed into the ground. But that was only the beginning.

Boom! Boom! Rumble!

With every step he took, bizarre rocks came pouring down like a rain shower. The spectacle made Jeok Cheongang’s flesh crawl.

*If I make one mistake, I might end up buried here.*

It clearly wasn’t a small cave.

If a cliff weighing tens of millions of geun[^1] came down on their heads, then even Jeok Cheongang could not guarantee that he would survive.

Especially not with the aftereffects of his injuries still lingering.

“Cough.”

His figure, shooting forward over the cracked ground, staggered. Jeok Cheongang swallowed down the blood rising into his throat and smiled bitterly.

*What a sorry state I’m in.*

His limbs were stiff as stone from having been unable to move for so long. He felt extreme hunger and exhaustion.

After clashing hands with some monstrous bastard who had crawled out of who-knew-where in this condition, it was only natural for his body to have deteriorated even further. If he had not possessed any internal energy, he would have collapsed long ago.

Rumble!

At that moment, the vibrations grew larger and more violent. Jeok Cheongang gritted his teeth.

*All right, I get it, so stop rushing me. I’ll get out somehow.*

There was someone he had to save. His one and only Disciple, who had become light and warmth when Jeok Cheongang wandered through cold, dark memories.

*Yes, my one and only Disciple. My Disciple, no doubt about it.*

His grip tightened on the two men. It felt as if some unknown energy had surged from deep within his body.

Flamefire Path.

Jeok Cheongang’s figure, which had paused for a moment, shot forward as a single streak of flame.

Whooosh!

The clash between Jin Taekyung and the Western Heaven Demon Lord had caused the underground prison to collapse, but it had actually helped Jeok Cheongang.

The inside had been reduced to a wasteland by the clash. The walls that had blocked the underground prison like a maze had all collapsed, leaving it as one enormous cavern.

*There!*

As Jeok Cheongang ran forward, using his movement technique, his eyes flashed.

Every place had an entrance or exit.

At the place where he felt a faint breeze blowing from somewhere, Jeok Cheongang saw the entrance to the underground prison—barely wide enough for one person to pass through.

*Hurry, hurry…!*

Jeok Cheongang flung himself forward with every ounce of strength he had.

He stepped across the ground as it turned over beneath him and dodged the rocks falling from overhead.

He passed the corpse of the Heavenly Power Demon, the old man lying dead as though asleep with a peaceful smile on his face, and shot farther and faster.

Within a short span of time that felt like an eternity, Jeok Cheongang was finally about to take the last step toward the prison entrance.

“Made it…!”

Rumble! Rumble!

A vibration and roar as loud as—or even louder than—the sum of every tremendous sound that had come before struck all at once.

The ceiling collapsed.

Massive rocks accumulated over hundreds, even thousands, of years crushed down upon the entrance to the underground prison.

And then—

“Get the hell out of my way!”

With an azure dragon’s roar that shook the underground prison, Jeok Cheongang drove his fist, filled with blue-white flames, into the center of the rocks.

Kwaaang!

The superheated energy contained in the Flame-Extinguishing Divine Fist smashed and melted the rocks.

After a roar that sounded as if the sky itself had split apart, a blast of hot air suddenly swept through the underground prison.

* * *

“What is this?”

A middle-aged black-clad man who had hurried over after hearing the roar swallowed a groan at the sight before him.

Whoooosh!

The collapse of nature itself. The cliff hundreds of zhang high behind the Sichuan Tang Clan was slowly sinking down.

It was an utterly shocking sight even from more than a hundred zhang away, but there was an even greater problem.

“D-Deputy Captain. That place is where the Demon Lord is…”

The underground prison!

The middle-aged black-clad man, the deputy captain of Dark Heaven, felt a chill run down his spine at his subordinate’s words.

The Western Heaven Demon Lord. If something had happened to him…

*We’re all finished.*

Cold sweat rolled down his forehead. Even when the Sichuan Tang Clan had used Heaven-Shaking Thunder, he had never felt this tense.

He gave an urgent order.

“Gather every brother scattered throughout the area immediately!”

“E-Everyone? But there are still Tang Clan members—”

“Those bastards aren’t the problem. Hurry!”

“Y-Yes, sir!”

The subordinate, frozen stiff, pulled a firework from inside his clothes and lit it. With a pop, a red streak of light burst in the air.

At the emergency signal, the black-clad men scattered throughout the Sichuan Tang Clan began gathering one after another.

A group numbering well over a hundred assembled only a brief instant later.

“Deputy Captain. Please give us your orders.”

The deputy captain wanted to smash the skull of the man who had just spoken. The First Captain, First Fiend, was likewise nowhere to be seen, despite the emergency signal.

*Damn it.*

The deputy captain’s throat bobbed heavily as he stared at the cliff, which was still collapsing.

The order he was about to give was tantamount to suicide. He was telling them to walk beneath the collapsing cliff and find the Western Heaven Demon Lord.

But there was no other choice. He had to give the order.

“The Demon Lord is in there. I, the deputy captain, will lead from the front, so not one person is to—”

Just as the deputy captain struggled to continue his command—

KABOOM!

With an unknown roar, the rocks forming a small hill exploded outward.

At the same time, everyone, including the deputy captain, saw it.

A large figure bursting up through the rocks.

“Demon Lord! The Demon Lord has come ou—!”

Someone’s shout scattered unfinished.

Splat! Crack-crack-crack!

The figure bounced a considerable distance from the cliff like a cannonball before rolling across muddy water and sludge and finally coming to a stop.

An old man had two people larger than his own build clutched tightly beneath his arms. Jeok Cheongang looked up at the sky filled with dark clouds and drew in the breath he had been holding.

“Phaaah!”

Fresh air and rainwater seeped in through his nose and mouth.

The refreshing sensation felt as if it were washing even his soul clean. His internal energy was already exhausted, and his body felt as though it had been smashed to pieces, but Jeok Cheongang smiled with relief at having rescued Jin Taekyung.

Then, in the next instant, he staggeringly raised his upper body—and froze.

“……!”

A group stood tall just over twenty zhang away, staring at him.

There were well over a hundred black-clad men, all holding bloodstained weapons.

Jeok Cheongang muttered like a groan.

“……Goddamn it. No matter how I look at them, they don’t seem like good people.”

A reply came that turned his guess into certainty.

“They are called Dark Heaven.”

Jeok Cheongang was not surprised even when the voice suddenly came from behind him.

He had endured every kind of hardship, and he had only just escaped the threat of being crushed to death. He had known from the changed breathing that the unknown old man he had saved had awakened.

“I see. Dark Heaven. I knew it was those sons of bitches.”

After muttering a curse, Jeok Cheongang continued without turning around.

“Do you know where we are?”

“This is the Sichuan Tang Clan. Unfortunately, it appears the battle has already been decided.”

“……This is driving me crazy.”

Jeok Cheongang ended his assessment with that short sentence.

He did not have much time to wonder how this had happened.

“What’s your name?”

“Dong Feng. My name is Dong Feng.”

“Do you have a sobriquet?”

“I am not a martial artist, so it would be strange for me to have one.”

“Your dantian was damaged. You’re not a martial artist?”

“It was only a little training I picked up because my Master pestered me into it. Medicine was where my heart lay.”

Jeok Cheongang’s eyebrow twitched.

Even though he had suffered a serious injury, the old man’s calm manner and speech carried an air of wisdom. Why did Jeok Cheongang suddenly think of a physician whose medical arts were said to have reached divine heights?

“The Divine Physician?”

“I am merely an old medical apprentice of no consequence.”

Jeok Cheongang let out a hollow laugh at the Divine Physician’s answer. He finally felt as though he understood what had happened.

“Thank you. For waking this old man who was nearly dead.”

“You rose on your own. That was how strong your will was, Sir Jeok.”

“I had no choice. I woke up because of some reckless fool.”

“That very reckless fool crossed the Central Plains to find me and asked me to help. He said he would do anything if I could save you, Sir Jeok.”

Jeok Cheongang turned his head to the side. Jin Taekyung’s form, collapsed and covered in blood and mud, entered his eyes.

“……What a foolish boy.”

If only he could wake that child right now, he wanted to wake him.

Perhaps they could have one final conversation.

But Jin Taekyung had exhausted every bit of his strength. He would not be able to rise. Even without the Divine Physician telling him, Jeok Cheongang knew that much.

*Yes. Perhaps… perhaps this is for the best.*

Jeok Cheongang slowly rose to his feet. Ignoring the pain stabbing through his entire body, he spoke toward the Divine Physician behind him.

“Got any strength in you?”

“I could in my younger days. Before I met my Master, I worked as a carpenter.”

“That’s an unusual past for the Divine Physician. What about now?”

“I am seventy years old.”

“Your dantian is damaged, so it won’t be easy, but squeeze out every last bit of strength you have. Run as far away as possible.”

“With Young Master Jin?”

“I’m glad you understand.”

After a brief silence, the Divine Physician spoke.

“Sir Jeok… You intend to throw your life away.”

“Throw it away?”

A faint smile appeared at the corner of Jeok Cheongang’s mouth. His gaze slowly turned toward the approaching black-clad men.

“Do you know why a flame dies out?”

Jeok Cheongang did not wait for the Divine Physician’s answer.

With each step he took, muddy water splashed. The rain that had seemed as though it would fall forever had stopped at some point.

His voice continued, refreshed and unburdened.

“Because there is nothing left to burn. That is why it slowly dies out atop the ashes.”

Jeok Cheongang had finished preparing to kindle his final flame.

He felt no fear or anger toward the death approaching him.

He only felt regret. He would no longer be able to remain at his Disciple’s side.

“I’m leaving Taekyung in your care.”

It was at that moment, as Jeok Cheongang stepped forward with his heartfelt request, that the Divine Physician spoke.

“After watching countless births, aging, sickness, and deaths, I found myself wondering. Does a place called the underworld exist? If it does, who is that fellow called Yama? And if I go there, will I be able to meet the patients I failed to save?”

“……?”

“Whenever I asked myself that, my Master would tell me this: ‘The underworld must be full because of all the people you sent ahead. You should ascend to the celestial realm and spend your days with the immortals.’”

The Divine Physician looked at Jeok Cheongang as he spoke in a quiet voice.

“Sir Jeok. The underworld is full. Please wait a little longer.”

“……!”

At that moment, Jeok Cheongang felt as if every hair on his body had stood on end, and he raised his head.

High in the sky, a boy stood bathed in sunlight streaming through a break in the retreating dark clouds.

*No. That isn’t right. That man is…!*

Those eyes were clear and bright like a boy’s, yet the gaze itself was ancient and seasoned, betraying no emotion whatsoever.

Eyes Jeok Cheongang had encountered only once, a very long time ago. That was why the sensation was all the more impossible to forget.

Remembering someone from the boy’s appearance, Jeok Cheongang cried out in shock.

“The Slaughter Saint…!”

[^1]: A geun is a traditional East Asian unit of weight; in Korea, it is roughly 600 grams.
## Chapter artifact 368

# Chapter 368

The boy—or rather, the “he” bearing the name Mungyeong—looked down at the ground below his feet.

Countless eyes gazed up at him in disbelief. Among them was a familiar face.

They had only met once, a long time ago, but recognizing him was not difficult.

“It has been a long time, Fire King.”

At his greeting, Fire King Jeok Cheongang’s eyes trembled violently.

“So it really was you…”

The greatest assassin under heaven. A man who had inspired awe in countless martial artists beyond condemnation and contempt had vanished without a trace one day and never shown himself again.

At least, not until a moment ago.

“Why are you here…?”

“A lot has happened. So very much. Isn’t that right?”

The question was directed at an old man. He gazed at the Divine Physician—or rather, Dong Feng—with indescribable eyes before opening his lips.

“What a relief. I wasn’t too late.”

His voice rang out from every direction.

Six-Harmonies Voice Transmission.

Everyone shuddered at the unfathomable heights of martial arts displayed before their eyes. The old physician quietly shook his head.

“You were too late.”

A note of regret followed.

“To turn back the years that have passed.”

“What can be done? Once water has spilled, gathering it back is no easy task.”

“Do you not regret it?”

“Regret…”

At his Disciple’s words, he raised his head and looked toward the sky.

The rain that had seemed as if it would pour forever and the black clouds that had hidden the sunlight were gone. An azure heaven stretched across the sky.

*Is this what you intended?*

He posed the question to someone who might be looking down at the lower realm from above.

But no answer came. Just as it never had.

*What a damnable thing this is.*

He slowly closed his eyes. In the pitch-black darkness, memories steeped in blood and struggle flashed past.

The life he had lived as an assassin after being raised as one. His inborn karma had made him an assassin, so he killed people—but he had been born a human being, and he hated killing.

That was why, at the end of the great war that had stained the continent with blood, the old assassin buried his weapons and began living as a physician.

But…

Had it truly come to this in the end?

With a faint murmur, he opened his eyes.

A boy’s hands, white and soft.

The Returned to Youth he had undergone several years ago had changed his flesh, but it could not erase the scent of blood ingrained in his hands.

“I lived for more than forty years as a physician. I wanted to die as one.”

His voice, carrying immense internal energy, thundered into everyone’s ears. The black-clad men staggered as if their very spirits had been shaken.

“And yet, why have you come here?”

Killing intent that made every hair on the body stand on end radiated from him. The deputy captain, who had frozen while staring at the being in the sky, spoke in a trembling voice.

“E-Even if you truly are the Slaughter Saint, this is not your concern.”

“Not my concern?”

He muttered the words in a low voice before throwing down the travel bag he had been holding.

Thud!

Something bounced out of the bag when it struck the ground and landed at the deputy captain’s feet.

“T-This is…”

They were the severed heads of two men. Though they belonged to different people, their wide eyes and twisted expressions looked almost exactly alike.

As if they were twins born on the same day.

The deputy captain’s gaze fixed on one of them.

“Captain!”

The deputy captain stared in horror at the First Fiend’s severed head. Slowly, the man opened his mouth.

“I’ll ask you one thing. Was the one in Qingcheng the second or the third of the Qilian Three Fiends?”

“……!”

Only then did the deputy captain understand.

Why there had been no word from the Qingcheng Sect. And where his brothers, who had failed to return after seeing the emergency signal, were.

In the end, only one path remained.

With a flash of insight, he shouted with internal energy behind his voice.

“Everyone, attack! Kill hi—”

Slash!

The deputy captain could not finish his shout.

Along with the wind brushing his neck, a figure stood behind him.

*Is this really… a human movement?*

That was the last question to pass through his mind.

He had failed to recognize the Ghost Illusory Slaughter Step performed by the greatest assassin under heaven—or rather, in all history.

Only death awaited him.

Fwoosh!

A fountain of blood erupted from the severed neck. As a figure brushed past his collapsing body and took another step, wind carrying the scent of blood swept through the air.

Slash. Slash. Slash!

The black-clad men who had watched their superior die with vacant expressions saw their heads rise into the air.

Before the streams of blood could even touch the ground, something pale and ghostlike passed through them.

“It was the life I wanted so badly.”

Muttering in a low voice, he stretched out both hands. Thin, elongated threads flowed from his ten fingers.

Threads of Force—beautiful and destructive.

“And yet, why did you…”

Whoosh!

When his ten curved fingers slashed downward through the air, Force tore through space.

Everything that stood in its way was cut apart and split open. Shattered armor and weapons, limbs and heads, flew in every direction.

In a world brought to a standstill by blood and death, only one person was free to move.

“Did you wake me?”

Consumed by sorrow and fury, he was no longer the cheerful boy or the physician who had passed the two-character name Divine Physician down to his Disciple.

He had returned to the person he had been before earning the name Divine Physician, before meeting the young carpenter who had fallen into grief after losing his wife and children to an epidemic, and before burying his weapons and leaving the Murim.

“The Slaughter Saint…!”

Someone shouted the words like a scream.

With eyes sunk deeper than an abyss, he flung out both arms. The wind, which had already become a storm, swallowed more than a hundred black-clad men.

Kwaaang!

* * *

There was a high hill east of the Sichuan Tang Clan.

From that hill, the entire Tang Clan grounds could be seen at a glance. A small watchtower had once stood there, along with martial artists who took turns standing guard.

Once.

Drip. Drip.

Drops of blood fell from the watchtower and dampened the grass. Some slid down the hill and touched someone’s hand.

The hand was covered in deep wrinkles, and the nails had taken on a green hue from years of practicing poison arts.

The owner of that hand was Tang Sadok, the current Family Head of the Sichuan Tang Clan—the Myriad-Poison Asura.

“Cough.”

Blood spattered between his parched lips. His eyes, usually cold and forceful, looked ready to go out at any moment.

“Is this how it ends?”

Tang Sadok murmured in a faint voice.

Everything was rushing toward its end. His life. The glorious history of the Sichuan Tang Clan.

“The family we built over hundreds of years… is collapsing in a single day.”

Tang Sadok’s lament was hollow. He no longer had the strength even to feel anger or sorrow.

With his limbs crushed and his internal injuries severe, the only thing permitted to the old Family Head was to lean against an unnamed tree and watch his clan perish.



*This is my final gift to you.*



The smiling face of a middle-aged man flashed before Tang Sadok’s eyes.

The middle-aged man, the Western Heaven Demon Lord, had not kept his promise. As far as he was concerned, the destruction of the Sichuan Tang Clan had been decided from the very beginning.

“Urgh. Blergh!”

The resentment blazing up like a wildfire worsened his internal injuries. Tang Sadok vomited nearly half a gallon of blood and gasped for breath.

“I’m sorry. I’m sorry…”

He was apologizing to the ancestors of the Sichuan Tang Clan, to the blameless members of his household who had lost their lives under an unworthy Family Head, and to Jin Taekyung and the others, who had likely already met gruesome deaths at the hands of the Western Heaven Demon Lord.

Of course, not one of them could hear Tang Sadok’s voice.

*If we meet in the afterlife, I’ll apologize to you myself.*

It was then, as Tang Sadok murmured inwardly—

Sssshhk.

The bushes stirred, and he felt something approaching.

No. It was not human.

Only when it reached the very tip of his nose did Tang Sadok realize who possessed that strange presence.

Hiss. Hiss.

A triangular head with horns and a flicking tongue. A snake with a pure-white body burrowed into Tang Sadok’s embrace.

“Ha… hahaha.”

Tang Sadok laughed weakly, both happy and hollow.

“So it was you.”

Hisss.

The Thousand-Year Poison Horned Snake, Mimi, hissed as if answering its master. Its cold tongue licked the beard matted with blood.

“Clever creature. How did you find your way all the way here?”

Tang Sadok looked at his pet snake with blurred eyes.

He had let Mimi loose because he was worried the snake might be injured in the melee. He had never thought they would meet again like this.

And he had never imagined that their final farewell would be like this, either.

Rumble!

A tremendous roar shook the hill. The earth rose, and the branches of the trees trembled.

Tang Sadok raised his head and tried to find the source of the roar, but with his vision already clouded, he could not tell what was happening.

He could only infer one thing.

*Has the time come?*

The roar was on an entirely different level from Heaven-Shaking Thunder.

At last, the destruction of the great Sichuan Tang Clan had reached his doorstep.

Tang Sadok slowly closed and opened his eyes before speaking.

“Leave.”

Hiss?

The snake’s triangular snout tilted to one side.

“This old man and the Tang Clan have little time left. If you stay here, you will be caught up in it as well.”

Tang Sadok was the Family Head of the Sichuan Tang Clan. Even if the Western Heaven Demon Lord did not come, someone would certainly come to confirm whether he was alive or dead.

Tang Sadok could easily imagine what those vicious men would do if they saw the Thousand-Year Poison Horned Snake guarding its master’s side.

“So go. Hurry!”

He wanted to shout, but the voice he forced out was so thin it seemed ready to break apart.

Yet the spirit creature that had spent so many years beside Tang Sadok understood the final wish of the man who had been both its master and its friend.

Drip. Drip.

Damp drops fell onto Tang Sadok’s wrinkled hand.

Leaving behind a few tears, Mimi slithered away and disappeared, the snake’s white body gliding across the ground.

As Mimi’s presence faded into the distance, a bitter smile briefly formed at the corner of Tang Sadok’s mouth.

“Yes. Go carefully.”

In his youth, he had roamed the battlefields. After the war ended, he had devoted his entire life to helping his father, the Poison King, rebuild the Sichuan Tang Clan.

He had always been required to remain cold-headed and thorough. He had no friend with whom he could share his heart, no lover, and no child born of his blood.

If not for the spirit creature that had remained at his side for so long, he would never have been able to endure his loneliness.



“From today onward, your name is Mimi. Tang Mimi.”



On the day he first encountered the tiny Thousand-Year Poison Horned Snake, Tang Sadok had given her the Tang family name.

The blood flowing through Mimi was different. Even the snake’s species was different. But Tang Mimi was a member of the Sichuan Tang Clan, recognized as such by its Family Head.

*I’ve lost everyone, and I’m sending only you away alive. Hahaha.*

Tang Sadok let out a hollow laugh and blinked.

Through his fading senses, the roar and someone’s screams echoed faintly from below the hill.

It must have been the final struggle of those resisting the destruction of the clan.

*This old man is here, too. I, Tang Sadok, Family Head of the great Sichuan Tang Clan, am here! Come to me!*

The cry, as if he were coughing up blood, only hovered at the tip of his tongue.

Tang Sadok slowly felt the strength drain from his entire body. His heavy eyelids tilted downward, little by little, ever so slowly.

*I’m tired.*

What would happen if he simply closed his eyes and fell into a deep sleep?

If he took a short nap and awoke in the grand armchair in the Family Head’s Hall, perhaps he would be able to see the familiar faces of his family.

How wonderful would it be if everything that had happened up to now—including his father’s death—were nothing more than a Butterfly Dream?[^1]

*Yes. If only that were true.*

Slowly. His trembling eyelids finally closed tight.

No, it was the moment before they closed.

“Mimi! Quick Attack!”

Hisssssss!

“……?”

*What the hell is this bullshit?*

Tang Sadok involuntarily opened his eyes wide.

In his suddenly brightened field of vision, he saw a young man running toward him and Mimi’s white body shooting forward like an arrow.

“Y-You?”

“Wow! Wild Grandpa Tang spotted!”

At the sight of Cheongpung grinning brightly with blood all over his face, Tang Sadok blinked.

“What… what is going on? How did you…?”

Cheongpung answered energetically.

“Mimi! Whirlwind!”

Whirrrrr!

If Tang Sadok had possessed even a shred of strength, he would have cursed him out.

Cheongpung and Mimi realized their mistake too late and bowed their heads.

“Ah, I’m sorry.”

Hiss.

“……”

Forgetting that he had been half dead a moment ago, Tang Sadok stared blankly at the one man and one snake before him. With difficulty, he opened his mouth.

“Our family—what happened to our family?”

“They all died.”

“……!”

“Oh. I meant Dark Heaven’s black-clad men, not the Tang Clan.”

*You should have said that first!*

Just as Tang Sadok was unable to continue speaking from shock and fury, Cheongpung pressed Tang Sadok’s Mingmen acupoint. Warmth like a spring day caressed his body.

“Cheongpung! True Qi Guidance!”

*This bastard is going to keep doing this to the end…*

Tang Sadok wanted to ask what had happened, but this time he could not resist the sleep washing over him.

Just before his eyelids closed, a soft voice like a spring breeze brushed against his ears.

“It’s all over now. Rest easy.”

It was the voice announcing the end of a day that had been longer and darker than any other.

[^1]: The Butterfly Dream is an allusion to the ancient Chinese philosopher Zhuangzi’s dream that he was a butterfly, leaving him uncertain afterward whether he was a man who had dreamed of being a butterfly or a butterfly dreaming of being a man.
## Chapter artifact 369

# Chapter 369

“Search every inch of the place. If you half-ass it like you do your martial arts practice, you’ll catch hell.”

“Oh, come on, Senior Brother. Anyone listening would think that was actually true. You really say anything in front of the kids.”

“You’re always wandering around pleasure houses… Do I need to beat you senseless right here before you come to your senses?”

“Fine, fine. I get it.”

Even after his Senior Brother’s scolding, the young man’s frown did not lift.

His name was Hwangso, a first-generation disciple of the Gongdao Sect, a martial sect in Sichuan. He had been called out for this mission along with around thirty second- and third-generation disciples.

*Damn it. What the hell have I been putting up with for five days?*

Hwangso grumbled inwardly.

Born to a fairly prosperous merchant family, he had grown up wanting for nothing.

He was already irritated enough that his father had forced him onto the path of a martial artist—a path that had never been part of his plans—simply because he wanted to establish ties with the Murim. But five days of sleeping rough in the wind and dust had been more than enough to grind away the last scrap of patience he had left.

*Whew. They say the new courtesan at Tengwang Pavilion is an absolute beauty…*

Just as Hwangso’s thoughts began racing toward his favorite pleasure house—

“You brat! After I said all that, you’re still letting your mind wander?”

“Ah, yes, I understand. I said I understand!”

Startled by his Senior Brother’s sudden, tiger-like roar, Hwangso trudged away.

His Senior Brother clicked his tongue at the sight, as if he found him hopeless.

“If you don’t want to die a senseless death, keep your wits about you. You do understand what kind of situation we’re in.”

“I understand perfectly. Aren’t we going through all this trouble to catch some fiend who isn’t even here?”

“What do you mean, he isn’t here?”

“You know what I mean. That Third Fiend or whatever. The bastard ran off ages ago, and we’re searching for him in all the wrong places.”

At Hwangso’s sullen reply, his Senior Brother’s face stiffened.

“Watch your words. Since the Great Faction War, the martial world of Sichuan has never united like this to form a net over heaven and earth. There is a reason for everything.”

“Who said there wasn’t a reason? I’m not deaf. I’ve heard it all already.”

Hwangso had heard the reason for the net over heaven and earth so many times that his ears were practically bleeding.

Dark Heaven or whatever they were called had invaded and turned the Tang Clan, Qingcheng, and Emei into ruins.

At the head of the attack had been a peerless fiend who had slain the Poison King and the Heaven-Shaking Venerable Nun single-handedly. The Qilian Three Fiends, old monsters from two generations ago, and hundreds of Fiends had split into three groups and stained the three sects representing Sichuan in blood.

And everyone in Sichuan, Hwangso included, knew how that day—soon being called the Three-Gate Bloodbath—had ended.

“In the end, they were defeated right in front of everyone, weren’t they? Every fiend who could be called a leader was killed except for one, and the rest of the foot soldiers scattered and ran away. Isn’t it over?”

“……Whew.”

His Senior Brother moved his lips as if he were about to say something, then answered with a sigh instead.

Whatever he said would go in one ear and out the other. His Junior Brother had no interest in learning how much luck and sacrifice had gone into their victory.

*The unknown master who suddenly appeared and saved Qingcheng Sect. The countless Beggars’ Sect disciples and nearby martial sects who rushed to Emei’s aid when it was in danger. And…*

If not for *them*, who had saved the Sichuan Tang Clan from annihilation, the three illustrious sects with their long histories would have vanished from the Murim five days ago.

The Three-Gate Bloodbath had been a large-scale assault carried out with such thoroughness and suddenness that it had sent a tremendous shock through the entire orthodox martial world.

*But for a martial artist’s thoughts to be this shallow… Even if he only joined because circumstances forced him to…*

At the sight of his Senior Brother shaking his head, Hwangso bristled.

“What?”

“Enough. Pick around ten men and search beyond that hill.”

“Again? We’ve already searched that place several times over the past five days…”

“The area assigned to our sect must be searched a hundred times, a thousand times if necessary. I’ll search the nearby grass myself, so do as you’re told without another word.”

His Senior Brother cut him off decisively. Hwangso clamped his mouth shut.

*I’ll have to talk to Father and get back home as soon as possible. No, seriously, why would the fiend who fled Emei show up here?*

The net over heaven and earth, in which thousands of people had been deployed, had lived up to its name.

Most of Dark Heaven’s remnants who had fled after the Three-Gate Bloodbath had already been hunted down or captured.

Only the Third Fiend, the youngest of the Qilian Three Fiends who had attacked Emei, remained. The area assigned to the Gongdao Sect was near Chengdu, practically the center of Sichuan.

*I hear the fiend isn’t in good shape, either. Why would he walk straight into the tiger’s den instead of choosing somewhere sensible like Tibet or Yunnan?*

Hwangso’s complaint was not entirely unreasonable.

No matter how true it was that it was darkest beneath the lamp, there was no reason for a fiend branded as an enemy of the Murim to break through such a dense net over heaven and earth and head for Chengdu.

*If there were even the slightest chance of that, why would I be here? The Qingcheng Daoists would have been guarding the place.*

This was all because his Senior Brother was so rigid that he was practically suffocating.

Muttering a quiet curse under his breath, Hwangso crooked a finger at the third-generation disciples standing around blankly.

“You there, the big-nosed one. Yes, you, all the way to the big-eared one over there. Ten of you. Follow me.”

What else could he do? When they told him to dig, he had to dig.

But as Hwangso left to search, with his Senior Brother’s contemptuous gaze boring into his back, his head was filled with nothing but idle thoughts.

*Just wait. The second this is over, I’m going straight to Tengwang Pavilion and having myself one hell of a time.*

With his mind somewhere else, there was no chance of the search being carried out properly.

The third-generation disciples glanced at Hwangso for cues as they lazily looked over their surroundings. Not one of them noticed the faint traces of blood clinging to the leaves during their sloppy search.



* * *

*Good thing they’re all idiots. At this rate, I don’t need to worry at all.*

The Third Fiend let out a sigh of relief and extended one foot.

Sssshk.

His body shot forward, skimming over the leaves.

A master of considerable skill might have noticed him if one had been nearby, but judging by the level of everyone he had seen so far, there was no chance of that.

*They never imagined I would double back toward Chengdu.*

The thrill of having fooled the orthodox faction so completely lasted only a moment before anger and killing intent surged from somewhere deep in the Third Fiend’s chest.

*If it weren’t for those bastards…!*

Five days ago, everything had gone smoothly when he led his subordinates in the attack.

The death of the Sect Leader, the Heaven-Shaking Venerable Nun, and the Elders had left a tremendous gap in Emei’s forces, and the Dark Heaven martial artists under the Third Fiend’s command had driven straight into it like a massive harpoon.

Then, just as the brutal battle overflowing with blood and death was underway, *they* appeared.



*You worthless pieces of trash, lower than dogs!*



A single filthy beggar.



*Hyuk Mujin, Vice Squad Leader of the Jin Dragon Squad of the great Jin Family of Taiyuan, the right arm and little toe of the Sleeping Dragon of Shanxi, Jin Taekyung, has arrived!*



A young man whose name seemed to be either Right Arm or Little Toe—it was hard to tell.



*Senior Sister! I’m here!*



And a middle-aged nun who appeared to be a disciple of Emei Sect.

Even the Third Fiend had been dumbfounded by such a fearless entrance at first.



*What? Worthless pieces of trash, lower than dogs? This filthy beggar wants to die? Just wait. This old man will tear your limbs off and—*



The Third Fiend had approached with a contemptuous snort, but he was forced to swallow the rest of his words.

Behind the fearless young beggar, countless more filthy beggars were rushing forward.

It was a wave of beggars!



*B-Beggars’ Sect?*



That response had come far too quickly for the Third Fiend.

Not even half a day had passed, yet more than a thousand Beggars’ Sect disciples—not dozens or a hundred—had gathered and come to Emei’s aid.



*The Successor Beggar commands you! Beat those bastards lower than dogs to death like dogs!*



*Armor! They’re wearing armor!*



*Hit the exposed parts! Crush their balls!*



An Emei nun charged them from the front without regard for her life, while countless Beggars’ Sect disciples surged in without end from behind.

The Third Fiend and the black-clad men under his command fought like mad, cutting down enemy after enemy, but the tide of battle had already begun to turn against them.



*Brothers of the Beggars’ Sect! Never retreat!*



*Waaah!*



*Avenge Gaeddongi!*



It was a human-wave assault terrifying enough to make the mind go blank.

If one beggar was cut down, two did not rush forward in his place. Five or ten did.

And if he dredged up every last ounce of strength and cut them down too? There was no need to worry about what came next. A club flying in from somewhere would smash his balls while an iron staff cracked the back of his skull.

The dead had no future.



*Guh…!*



Like a body slowly soaked through by drizzle, the black-clad men collapsed one after another as cold corpses.

Even the Third Fiend, who should have turned the tide of battle, had no time to look after his subordinates.



*Form the Demon-Subduing Dragon-Taming Formation!*



The Seven Fairies, Emei Sect’s finest masters, used a combined formation to bind the Third Fiend’s feet.

Even when seriously wounded, they never retreated. They attacked as if their lives meant nothing, and the Third Fiend gradually grew exhausted from the mounting fatigue and anxiety.

The Third Fiend’s face twisted violently as he recalled what had happened five days earlier.

*And then Extinction Divine Nun appeared. That damned old monster brought it all to an end.*

The arrival of Extinction Divine Nun had shocked not only the Third Fiend but also the disciples of Emei.

Thirty years ago, at the age of one hundred, she had withdrawn from worldly affairs. She was the Heaven-Shaking Venerable Nun’s only Senior Aunt, and everyone believed she had since died.

With another Supreme Peak master suddenly appearing, the Third Fiend chose to flee without a moment’s hesitation. The black-clad men under his command scattered and ran after their superior.

It had been a clear defeat.

And yet, the Third Fiend had survived to the very end.

He disguised himself with a mask made of human skin and a disguise technique, then found the weakest point in the net over heaven and earth and made his way here.

To this nameless cliff, untouched by anyone’s feet.

“At last… Guh!”

As the cliff rapidly drew closer, the Third Fiend suppressed the emotions welling up inside him.

Only now had the grief and anger of losing his only blood relatives reached him all at once.

“Do not feel too aggrieved. Though I must retreat for now, this youngest brother will surely avenge you, my elder brothers.”

The Third Fiend had just made a firm vow of revenge and reached a hand toward the cliff when—

Slice!

The Third Fiend’s eyes flew wide.

Along with a sensation as hot as a burn, his wrist dropped away.

It was agony he had not felt in a very long time. A beat later, a scream burst from his cracked lips.

“Kyaaaaargh!”

At the same time, a chill ran down his spine.

He pressed his acupoints like lightning to stop the bleeding, then jerked his head up.

Where there had been nothing but a solid cliff moments ago stood a painfully familiar face.

“B-Big Brother?”

The Third Fiend’s cry held both delight and shock.

But First Fiend’s response was calm.

“So it seems. Your disguise technique was so poor that I suspected as much.”

“……!”

Crack. Crackle.

At that moment, First Fiend’s hideous face rippled like a wave. His hunched back straightened, while his arms and legs grew long and slender.

In the place of the ugly old man now stood a handsome boy.

“Who the hell are you?”

At the Third Fiend’s shout, a faint smile passed across the boy’s impassive face—the face of the Slaughter Saint.

“Mungyeong.”

A faint smile passed across the boy’s impassive face—the face of the Slaughter Saint.

“Your enemy.”

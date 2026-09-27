# Checkpoint Review — 1040–1044

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

# Chapters 1040–1044

## Plot

Jin Taekyung defeats So Gunak and revives through a level-up, then fights through the white-robed mages’ varied spells to reach their veiled leader, the Grand Mage. He launches an incomplete, life-consuming One Annihilation as her wide-area Magic erupts, but the blast engulfs the hill. Left severely exhausted with an empty dantian and damaged acupoints, Jin uses White Flame to bend the descending Hell Fire sphere’s course and open a rift in its flames. Other fighters’ attacks also strike toward the sphere, but its fate remains unknown.

Elsewhere, the Wind-and-Cloud Sword Lord defeats the two Black Ghosts attacking him after a distant blast unbalances them, despite being badly wounded and urged to retreat by his two Senior Brothers. Song Il and Hwangbo Eom reunite at the battlefield’s front and combine their attacks, slightly shifting the sphere but failing to stop it. They regret accepting Sima Gong’s transaction to pursue revenge against the Fire Gate Clan and protect Zhongnan. As the Hell Fire engulfs the battlefield, they face it rather than flee; their fate is unknown.

## Continuity

- The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army. Jeok Cheongang is injured but holding him off.
- Fire Dragon Armor is severely damaged, stored in Inventory, and unavailable until its automatic repair completes in three days.
- The Grand Mage leads the white-robed mages. Nineteen of the twenty have fallen; repeated dispellings caused energy backlash that incapacitated them.
- Jin’s incomplete One Annihilation failed to break all the Grand Mage’s barriers. He remains alive but severely exhausted, with an empty dantian and damaged acupoints.
- The Grand Mage’s Hell Fire is a vast sphere capable of killing thousands. Jin’s White Flame spear throw and other fighters’ attacks have not stopped it; its fate remains unknown.
- The Wind-and-Cloud Sword Lord refused to retreat despite his injuries and defeated the two Black Ghosts who attacked him. His two Senior Brothers had urged him to withdraw.
- Hyuk Sopyung is leading Zhongnan’s surviving disciples.
- Song Il and Hwangbo Eom accepted Sima Gong’s transaction to pursue revenge against the Fire Gate Clan and protect Zhongnan. They regret it and face the Hell Fire sphere; their fate is unknown.

## Translation Decisions

- Render 대술사 and 대마도사 as Grand Mage.
- Render the named spells 파이어 볼, 스톤 월, and 매직 애로우 as Fire Ball, Stone Wall, and Magic Arrow.
- Render 헬 파이어 as Hell Fire when named; use lowercase hellfire for descriptive 겁화.
- Render 일섬 as One Annihilation and 백염 as White Flame.
- Render 쇄월검진 as Moon-Shattering Sword Formation.
- Render 대사형 and 사제 in the Song Il–Hwangbo Eom exchange as Senior Brother and Junior Brother.

## Durable state

{
  "active_continuity": [
    "The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.",
    "Jeok Cheongang is injured but holding off the Blood-Sword Demon Lord while Jin Taekyung targets the mages.",
    "Fire Dragon Armor is severely damaged, stored in Inventory, and unavailable until its automatic repair completes in three days.",
    "Repeatedly dispelling the white-robed mages’ varied Magic causes energy backlash that incapacitates them; nineteen have fallen, and their veiled leader, the Grand Mage, remains.",
    "The Grand Mage’s Hell Fire is a vast sphere capable of killing thousands; Jin’s incomplete One Annihilation failed to break all the Grand Mage’s barriers, leaving him alive but severely exhausted, with an empty dantian and damaged acupoints.",
    "Jin’s White Flame spear throw bends part of the Hell Fire sphere’s course and opens a rift in its flames, but does not stop it; other fighters’ attacks have an unknown result.",
    "The Wind-and-Cloud Sword Lord is badly wounded and refused to retreat; his two Senior Brothers urged him to withdraw after securing a way out.",
    "The two Black Ghosts facing the Wind-and-Cloud Sword Lord were disrupted by a shock wave; the chapter confirms that he defeated them.",
    "Hyuk Sopyung is leading Zhongnan’s surviving disciples.",
    "Song Il and Hwangbo Eom accepted Sima Gong’s transaction to pursue revenge against the Fire Gate Clan and protect Zhongnan; they regret it and face the approaching Hell Fire sphere, with their fate unknown."
  ],
  "continuity_sources": [
    1043,
    1044
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who are the white-robed mages, and what is their purpose?",
    "How were the former Demonic Cult fiends made into Black Ghosts?",
    "What happens to the Hell Fire sphere, Jin Taekyung, Song Il, and Hwangbo Eom?"
  ],
  "safe_through": 1044,
  "temporary_decisions": [
    "Render 대마도사 as Grand Mage.",
    "Use Fire Ball, Stone Wall, and Magic Arrow for the named spells.",
    "Render 헬 파이어 as Hell Fire; use hellfire for descriptive 겁화.",
    "Render 쇄월검진 as Moon-Shattering Sword Formation."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 1040

# Chapter 1040

KWA-BOOOOM!

A terrifying explosion shook the very earth.

The immense shock wave erupted without warning, rattling everything around it. It was powerful enough to reach beyond a radius of several dozen *jang* and all the way up to the steep hill.

Rumble.

“May I speak, my Lady?”

At the old man’s voice, which cut through the rumbling ground and pierced her ears, red lips stirred beneath a silver-white veil.

“No. You may not.”

There was no trace left of the woman who’d been rattled by the Blood-Sword Demon Lord’s fury just fifteen minutes ago.

At her superior’s cool, almost icy reply, the old mage’s frame twitched.

“…Grand Mage.”

His voice was filled with concern.

But the woman called the Grand Mage, standing at the center of the white-robed figures, paid him no mind as she spoke.

“Put your pointless worries aside. What you’re afraid of won’t happen.”

“B-but…”

“But what?”

Under normal circumstances, the old mage, her subordinate, would have fallen silent by now.

The hierarchy within Dark Heaven was mercilessly strict, and the woman before him had enough power to crush him like an ant with a mere flick of her hand.

But the old mage had seen it clearly.

At the last moment, one man’s figure had been swallowed by countless flashes of light.

A young man who’d thrown himself in front of what should have been certain death—not merely recklessly, but as if he’d already given up on living.

The old mage knew his own role well. Swallowing hard, he had no choice but to force the words out.

“But if things continue like this, he may be in danger. As you know, if ‘he’ dies here, how are we to bear that person’s wrath?”

He was right.

Jin Taekyung, the Blazing Flame Divine Dragon.

If the absolute one’s keenly watched favorite met such a futile end, they too would die for failing their mission.

No—they would die. Without a doubt.

The old mage believed there would be no exception, not even for the woman before him, his superior and one of the absolute one’s closest confidantes.

Of course, that was only what he thought.

“Danger? Die?”

The woman repeated his words, then let out a quiet laugh.

Beyond the finely woven veil, her black eyes remained fixed on the hill below, as they always had.

“Who, exactly?”

“Pardon? Why, of course…”

The old mage had just begun to answer when—

FWOOSH.

The hazy dust cloud covering the foot of the hill split apart.

And, as if an invisible, razor-sharp blade had passed through it, the veil parted cleanly to reveal the scene hidden within.

“……!”

“……!”

The old mage—and everyone on the hill—stared wide-eyed.

What their stunned eyes saw in that moment was a figure standing tall amid ground devastated as if by a falling meteor.

“Th-that’s…”

One mage raised a hand and pointed before he even realized what he was doing. The gesture was pointless; every eye nearby had already turned that way.

A familiar figure, towering nine feet tall, with arms and legs as thick as pillars.

His entire body was covered in black armor.

“Black Ghost…!”

A trembling groan escaped the old mage’s lips.

The brief shock vanished, replaced by deep despair. His eyes fixed on the man lying bloodied at the Black Ghost’s feet.

The one who must not die here.

Jin Taekyung.

*It’s over. All of it.*

The old mage’s vision blurred.

He’d held on to a sliver of hope after seeing the Grand Mage’s confidence just moments ago. That only made the shock worse.

Half of the hundred elite guards they’d kept behind in case of trouble had vanished. But compared to the fact that Jin Taekyung was dead, that meant nothing.

The twenty mages all thought the same.

At least, until the Grand Mage’s quiet voice rang out the very next moment.

“As expected…”

The mages widened their eyes at the incomprehensible murmur—and at the admiration in it.

Then, all at once, they saw.

Rustle. THUD.

Far below, the Black Ghost crumpled like a rotten log.

Only now could they see what had been hidden behind his enormous body: a silver spearhead embedded between his brows.

But though they saw it, they could not hear—

Ding.

The clear chime meant for only one person.

The voice of recovery sounded by the ear of a man everyone believed was dead, but who still lived.

> **System**
> - You defeated Lv. 175 So Gunak!
> - Level Up!

A warm radiance welled up from deep within his body, which had been growing cold.

It stopped the blood seeping through gaps in his red armor, torn apart by countless blades of Sword Energy and Force. It mended his torn flesh and broken bones, and rekindled the flame of life once more.

*Huff.*

His breath was hot as fire.

As if waking from a long dream, Jin Taekyung slowly opened his eyes. He looked up at the dark sky he’d seen once before and muttered,

“Fuck, it’s good to see you.”

The moment the old mage saw that unbelievable sight, he understood.

*Danger? Die?*

He understood what the words he’d heard a moment ago meant.

*Who, exactly?*

The Grand Mage had been right.

It wasn’t Jin Taekyung who now had to face the danger of death. It was them.

WHIP—GRAB.

The spear embedded deep between the Black Ghost’s brows flew into its owner’s grasp, as if drawn by an invisible force.

No—at the very instant it seemed to, it shot out in a flash.

SHWAAAAK—SPLAT!

A blue-black flame, swinging savagely like a giant dragon’s tail, tore through the surviving enemies.

“Grand Mage!”

“We have to stop him, whatever it takes! If this goes on, he’ll—he’ll…”

Urgent shouts rang out from all directions, starting with the old mage.

But the Grand Mage silently watched the horrifying, wondrous sight, her eyes flashing with an inscrutable light.

*At last.*

A quiet exclamation hovered on her tongue.

Even as the mages clenched their teeth and stepped forward, unable to wait for her command, she alone stood there, smiling quietly.

* * *

From the moment I first opened my eyes in Murim, I’d run into the same reality over and over. Put simply:

High risk, high return.

It had always been that way.

An adventure with no set ending always came with enormous danger. But the greater the risk, the more certain the reward.

Just like now.

Ding. Ding. Ding. BEEP-BEEP.

Chimes and warning beeps rang out in rapid succession, tangling together in my ears.

A message confirming I’d defeated the Black Ghost, the last obstacle. A Level Up. And a holographic window telling me I’d recovered as a result.

And the final warning beep was…

> **System**
> - Fire Dragon Armor has suffered severe damage from powerful energy!
> - Fire Dragon Armor has been automatically recalled to Inventory! It cannot be resummoned until the damaged sections are repaired to a certain degree!
> - Time until Fire Dragon Armor is automatically repaired: 3 days

The message told me my divine weapon had taken the hit. It was the biggest reason I’d been able to take this risk—and the thing that had kept death at bay, if only for a little while, despite the crazy stunt I’d pulled.

*I actually survived.*

Maybe it was because I’d just barely come back from the brink of death.

It still didn’t feel real.

Of course, I’d taken the gamble hoping I’d survive.

I just hadn’t been a hundred percent sure.

If that damned Black Ghost had taken even a little longer to die, we probably would’ve ended up killing each other at best.

But…

SHK!

I was alive. I’d survived.

Just as I had all along, from the very beginning, I remained here, relentlessly cutting down my enemies.

My body was brimming with life—the reward I’d won for risking my life.

PUK! BOOM!

I drove my spear through three enemies in one powerful thrust, then swept out a palm at those rushing in from my blind spot.

KWA-AAAA!

Flesh and bone melted in the terrible heat.

Of the fifty or so enemies left alive after my clash with the Black Ghost, their numbers kept visibly dwindling.

*Faster. Faster.*

But I gritted my teeth and pushed myself harder.

I had to end this fight as quickly as I could.

My mental strength, already stretched to the limit, was running dry.

If I hadn’t gotten my body back through the Level Up—if I hadn’t been thinking of everyone still behind me—I might have collapsed already.

*They won’t go down until I take them down.*

As if possessed, I swung White Flame.

My hands and feet, their movements etched into them through endless training and instinct, swept through my enemies faster than my mind could keep up. My brain had slowed sharply from pushing the Middle Dantian’s ability to its limit.

I was relying on instinct rather than reason.

Even so, there was one last thread of reason I clung to: the reason I couldn’t fall, and the greatest variable my enemies had.

*Magic.*

That was probably why.

My instincts, sharper than ever and racing ahead of my reason, sensed another anomaly. I’d been keeping those two words in the back of my mind all along.

WHOOOOOM.

Space and air trembled.

At the same time, a desperate shout rang out in the distance.

“The power of the Wind Ghost!”

“The might to uproot mountains!”

FWOOSH!

Energy boiled up from the hilltop and hurtled toward me.

An invocation, followed by its manifestation.

But I knew.

Magic that strengthened the body like this required its target to still be alive.

SHWAK!

White Flame, wreathed in blue-black fire, tore through the air.

The terrifying ring of fire swept through a dozen or so enemies within the spell’s range.

SHK! PUK!

Ten heads flew into the air.

At that very instant, pain flared along my side.

But I’d been ready for it. I turned without a second thought and swung my elbow.

CRACK! KWA-BOOM!

The enemy’s face caved in, and he went flying. I pulled the dagger from my side and swept out my arm in a flash.

SWISH—PUK!

With a dull thud, another enemy’s head snapped back. There were only about twenty left now.

“What is this…!”

“No! Stop him!”

Listening to the shouts of the white-robed figures—or rather, the mages—now tinged with fear, I could roughly guess what was happening.

There was a limit to the Magic they could use.

That was what set them apart from the mages I knew in the modern world.

And in the next moment, the confidence that certainty gave me burst out through my feet.

CRUNCH—BOOM!

The earth’s crust heaved, then melted away.

Flamefire Path.

With a single explosive burst, my body shot forward. There was no one left nearby who could stop me.

No matter how fiercely a hunting dog was raised, it couldn’t stand against a wolf. And even a thousand-year-old *imugi* couldn’t ascend to the heavens without a dragon pearl.

Even if the thing trying to stop me wasn’t human.

“Great mountain.”

WHOOOOOM.

“Fall and crush him.”

Along with a voice I remembered, an immense pressure bore down on me as I shot forward like a streak of flame.

But unlike last time, I was ready.

*I can see it.*

I could feel it, too.

The flow of qi. A single line hidden beneath that immense power.

And…

*Now.*

SHK!

My spearhead cut through space without a sound.

It cut through the great mountain.
## Chapter artifact 1041

# Chapter 1041

Magic was an unpredictable and powerful force.

It could strengthen allies and weaken enemies, and create countless variables, from wide-area attacks to defensive barriers.

That was why mages were so highly valued even in the modern world, where the insane profession known as Hunter had taken root.

But if someone asked me whether mages were the most powerful among Hunters of the same rank, I’d answer without hesitation.

No.

They could wield more power than anyone else on the battlefield, depending on the circumstances. But that required a few conditions to be met.

The first was having allies who could protect the mages while keeping approaching enemies in check.

SHING!

I cut through it.

There was no sensation of slicing through flesh and bone, no hot blood spurting like a fountain. And yet I felt it clearly.

I’d cut through something intangible and odorless that people called qi, and the System knew it.

Ding.

> **System**
> - You successfully dispelled **Gravity Magic**!
> - **Qi Sense** has improved slightly!
> - You can now control qi a little more freely!

A translucent holographic window appeared in the air as the System’s notification rang suddenly in my ears.

But I paid it no mind.

I drew up every bit of energy sleeping deep within my body and kept moving forward.

SHWEEEE!

The distance of several dozen *jang* closed rapidly. In time with my terrifying speed, the immense energy covering the hill surged more and more violently.

“F-Fire Demon, answer our call!”

“Strange rocks and crags, block our master’s enemies!”

Urgent incantations rang out.

At the same time, dozens of massive fireballs filled the air, and the ground ahead flipped over as a wall of stone surged upward.

FWOOSH! GRRRR!

If anyone else had seen it—or even a seasoned master of the martial world—they would have stared in awe, calling it the work of supernatural powers.

But in all the vast world, I was the one exception.

*Fire Ball. And a Stone Wall, too?*

The moment I recognized the newly manifested Magic, my face stiffened before I could stop it.

Was it because this time, even I couldn’t easily dispel the spells?

Wrong.

Judging by their size, range, and power, these were spells that even B-rank or upper C-rank mages could cast.

There was only one problem: I’d realized the theory I’d just come up with was wrong.

*They weren’t limited in the kinds of Magic they could use. They just hadn’t used them.*

Magic was valued not only for its power, but also for the variety of its forms and the variables it could create.

But despite having the ability and the opportunity, all they’d shown so far was body-enhancement Magic and Gravity Magic.

*Why the hell?*

A question filled my mind.

But the Magic reached me much faster than I could find the answer.

KWA-AAAA!

The dozens of fireballs, tiny when they were first launched from afar but now as huge as boulders weighing a thousand *geun*, sailed over the stone wall and fell toward me.

Their heat was enough to make anyone else’s breath catch.

But the heat flowing through White Flame’s spearhead as I swung it down at them was incomparably deeper and more fierce.

SHING—KWA-BOOOOM!

I dodged half and cut through the other half.

The fireballs exploded in midair, painting the sky with dazzling bursts of flame. By the time they did, I was already bursting through the acrid smoke, driving a punch into the enormous stone wall blocking my way.

WHOOOM!

A fist that sliced through the wind—or rather, burned its way through.

It had none of the shifting forms or profound principles of the peerless arts boasted by the other great sects, but its explosive force and destructive power were second to none.

Long ago, unlike my spear-loving Master, the third Sect Leader of the Fire Gate Clan had been obsessed with fist-and-foot martial arts. He’d named the martial art he created:

*Flame-Extinguishing Divine Fist.*

CRUNCH—KRRR!

True to its name, the wall of strange rocks and crags crumbled without resistance, scattering into hundreds, then thousands of pieces.

No—it melted and burst apart all at once.

GRRRR!

The ground shook as if an earthquake had struck.

I passed beneath the many boulders raining down overhead and shot toward the hill again.

Ding. Ding. Ding.

> **System**
> - You successfully dispelled **Fire Ball**!
> - You successfully dispelled **Stone Wall**!
> - **Qi Sense** has improved slightly!
> - You can now control qi a little more freely!

“He’s—he’s coming!”

“Arrows of Radiance, answer our call!”

Listening to shouts that were now nearly screams, I stared straight at the hilltop.

Twenty people in white robes.

Some were vomiting blood from the backlash of having their Magic dispelled. Others were bringing forth another spell. Still others were trembling, their faces as pale as the clothes they wore.

And there was one person who stood out all the more because she was the exception to all of it.

*So it’s you.*

The Grand Mage.

A great mage who had reached the very edge of truth—and an enemy I absolutely had to defeat.

She was a woman.

Her slender figure couldn’t be entirely hidden by her voluminous robes, and red lips showed beneath her silver-white veil.

She was another formidable foe, her presence concealed by that of the Blood-Sword Demon Lord.

And along with that, she might be the only person who could give me a proper answer to my question.

SHWISH-SHWISH-SHWISH!

Magic Arrow.

I swung my spearhead up toward the countless streaks of brilliant light shooting at me.

FWOOSH!

Blue-black Force surged like a wildfire and swallowed the light.

No—as soon as I thought it had, everything there burned to ash, and new spells came rushing in.

POW-POW-POW! SHWEEEE!

The air and the ground below it were blanketed in lights of every color.

A spear of ice. A rain of fire. Blades of lightning and wind.

It all came crashing down on one person alone.

On me.

Each of the countless streaks of light, merging and following one another, had the force of a Sword Energy strike from a Peak master.

But that was all they were, and they could never wound me.

SHING.

I cut through a spear with my own spear—the spear made of ice.

SHWISH-SHWISH! KWA-BOOOOM!

I dodged the rain of fire that blanketed the area with movements as swift as Shifting Form and Position.

BA-BOOM!

The lightning and blades of wind waiting for me were swallowed by the heat of Flame Divine Palm.

Ding. Ding. Ding.

Clear chimes rang in succession, announcing the dispelling of Magic.

The Peak.

The towering, thickly wooded summit I’d built by crossing the brink of death again and again hadn’t been threatened in the slightest.

From this hill overlooking the battlefield covered in blood, nothing could stop me now.

Not people. Not Magic.

“Plants sleeping beneath this earth, rise up and bind our master’s enemies!”

RUSTLE!

Before the incantation was even complete, I felt it. I knew what it was.

The pulse of energy beneath my feet. The identity of this Magic.

But there was no reason to dodge, nor any need to cut it apart.

Thick roots burst from deep underground and coiled around my whole body, binding me tight. I simply stepped forward in silence, and that was enough.

CRUNCH. CRUNCH.

The branches, hardened like steel by Magic, trembled.

Feeling the pressure of the roots wrapped tight around my limbs, waist, and neck, I reached out and tore them apart.

KRRRUNCH!

Under normal circumstances, I shouldn’t have been able to reach out at all. I shouldn’t have been able to move a single step.

But…

*That’s what you think.*

That was only what they thought, their eyes wide with disbelief.

To me, this was perfectly natural.

A reward earned after one life-threatening adventure after another.

Pure physical ability that no simple binding spell could restrain.

That power, far beyond human limits, was made possible by the internal energy of several *jiazi*, still surging endlessly from my lower dantian.

CRACK! BOOM!

The roots binding my whole body burst apart in an instant.

But they kept coming, persistent as living creatures. I trampled them one by one and ripped them out by the roots.

So they could never rise again.

And so whoever had cast this spell would collapse, spitting blood.

Ding.

Another chime rang, announcing that I’d dispelled the binding spell.

“Ugh—bleeegh!”

Another white-robed figure collapsed to his knees, coughing up dark red blood.

He looked like the oldest of the twenty mages—and he was the nineteenth to fall.

What that meant was clear.

There was only one person left.

While the mages under her command kept collapsing from the backlash of their energy, the Grand Mage stood alone on the hill without the slightest sign of being shaken.

No—more precisely, it was just her and me, now almost face-to-face.

“I’d only heard about you until now… I’m glad. Seeing you in person is wonderful.”

Her red lips moved beneath the closely woven silver-white veil.

Her voice was calm, though it carried a hint of excitement.

“Crazy bitch.”

At my heartfelt insult, a breeze accompanied by a low laugh stirred her veil.

“What an uncouth man. Cursing a woman whose face and name you don’t even know.”

She was right.

I didn’t know this woman’s name or face.

I already knew that even the supernatural ability granted to me by the System couldn’t reveal any information about her.

Otherwise, she wouldn’t dare speak to me like that now, with less than a *jang* between us.

WHOOOOOM.

I couldn’t see it, but I could feel it.

The immense, deep energy blocking the space between us.

Though we occupied the same space, it separated us as if we lived in different worlds—a defensive barrier of extreme solidity.

“So you’ve been sitting up on that hill, scheming away, and this is all you’ve got?”

“Ah, I knew you’d be able to feel it.”

The Grand Mage nodded happily, then added,

“Of course, I also knew you wouldn’t dare try anything in a situation like this.”

“……!”

“Oh, did I hit a nerve?”

I silently clenched my teeth.

What she said was undeniably true.

I had only one chance.

If I failed to break the barrier and take her life with that one strike, the Grand Mage would escape the narrow distance I’d managed to close.

That was what kept me from acting recklessly, even though every second mattered.

But the quiet voice that slipped into my ears next was enough to shake me far more than anything she’d said before.

“Still, I’m a little disappointed. I prepared more than just this.”

“……What?”

“Shall I show you? I was getting a little bored anyway.”

At that very moment—

GROOOOOM.

In stark contrast to her bright, laughter-filled voice, an utterly dreadful amount of energy surged up around her slender body.
## Chapter artifact 1042

# Chapter 1042

Gooooom.

The instant he felt the enormous energy surging up around the Grand Mage, two words shot into Jin Taekyung’s mind like bullets, bleaching it white.

The first was wide-area Magic.

And then…

*One Annihilation.*

Jin Taekyung knew it by instinct.

To stop the insane thing the woman before him was about to do, he would have to make an insane choice of his own.

Unless he unleashed a desperate strike he’d thought he could never use again—a strike with barely any chance of bringing him back to life this time—he wouldn’t be able to stop the wide-area Magic from activating.

At the same time, he realized he’d already made his decision, and laughed bitterly to himself.

*Damn it.*

He still didn’t want to die.

He wanted to live, somehow—even if he had to struggle pathetically, whatever it took.

But there was no way.

No—there was only one way.

To break through the powerful barrier surrounding the Grand Mage right now and take her life with that strike, Jin Taekyung would have to burn up his own life, too.

Was he certain the strike would work?

No.

There was only a chance.

Survival or death?

The latter was far more likely.

But even if that was the case, it was enough.

This was the only option left to protect the tens of thousands of allies still fighting on the battlefield—and the precious people among them.

*All right.*

That was enough.

A noble sacrifice, or a pointless death.

He didn’t know which ending awaited him, but these chaotic times were forcing Jin Taekyung to become a hero in this very moment, and he was ready.

Perhaps he had been for a very long time.

Fwoosh.

The wind stopped all at once. The air trembled.

Time seemed to stand still. Hundreds of acupoints awakened, and he could feel every strand of muscle throughout his body, one by one.

And then…

Qi flowed along the white spearhead.

Dark as the deep sea, flashing like lightning, burning like a flame.

At last, the energy merged into one and swelled larger than ever before. A mighty force capable of devouring its owner’s life, it whipped along the spearhead, drawn back like a bowstring.

In that moment, it blazed with such dazzling light that it seemed to color the Grand Mage’s eyes, hidden behind her finely woven veil.

*This is…*

Before that destructive radiance, which even the barrier couldn’t fully conceal, the Grand Mage felt fear suddenly seize her.

Along with awe for the young man before her, who had made such an unbelievable choice.

*At this rate, I’ll die. Without a doubt.*

The Grand Mage was certain.

Once that terrifying strike was complete and launched, she would vanish without a trace along with her barrier.

And Jin Taekyung’s life would scatter like ash, too.

But neither the Grand Mage nor the master she served wanted that outcome.

*We’re both lucky, you and I.*

A money pouch burdened with more weight than it can bear is bound to tear. But if you tie it shut before all that weight is put inside, it won’t.

In that sense, they had missed disaster by a hair’s breadth.

The Grand Mage’s Magic had been prepared a step ahead of this moment. Jin Taekyung’s strike was a step behind.

And that tiny difference in timing, no more than an instant, changed the fate of them both.

*Pour forth, flames of hell.*

Fwoosh!

An immense energy exploded around the Grand Mage.

Its power began spreading far faster than Jin Taekyung had expected. He had only one choice left.

Shwoosh!

The spearhead tore through space.

At the same time, a One Annihilation larger than ever before, and therefore not even half-formed,finally met the barrier between them.

Gooooom.

A deafening roar made his ears ring, and white light washed over the hill.

* * *

Amid the faint pain coming from all over his body, the old Daoist steadied his ragged breathing.

Hoo.

His sweetish-smelling breath slowly dispersed.

Beyond the red haze of his vision, stained by blood running down from the scar on his forehead, two men stood tall as iron towers.

No—as soon as he thought he saw them, they vanished.

Whish.

A faint whistle, chillingly subtle, pierced his ears.

An alarm rang in his mind, warning him of danger. His brain finished its judgment and ordered his body to move.

Dodge.

Move now to avoid the enemy.

But his body, already badly wounded, couldn’t move as it normally would.

Shhk!

A wave of excruciating pain.

The two blades he hadn’t managed to avoid completely slashed his side and shoulder, and the tremendous energy held within the steel tore deep through his body.

*Hng…!*

His vision blurred.

But the Wind-and-Cloud Sword Lord soon steadied his wavering form and unleashed his treasured sword. Brilliant Sword Force flared along the blade, now only half its former length.

Bang! Bang! Baaang!

Three clashes, as swift as lightning. Then one figure shot through the cloud of dust like a cannonball.

“Sect Leader!”

The Zhongnan Sect disciples fighting amid the Dark Heaven cultists screamed.

At that very moment, two figures appeared from nowhere and caught the Wind-and-Cloud Sword Lord as he flew backward.

Grind.

Only after sliding back several feet did they finally stop.

Coughing up dark blood, the Wind-and-Cloud Sword Lord moved his lips toward his helpers, whose faces were blurred in his sight.

“Senior Brothers…”

“Damn it, don’t say a word.”

The First Senior Brother, the Roaring Fury Swordsman, snapped back irritably. Then the Second Senior Brother, the Taeeul Merciless Sword, spoke, his expression grave.

“This is enough. Junior Brother, Sect Leader.”

This is enough.

It was only a short sentence, but the Wind-and-Cloud Sword Lord immediately understood what it meant.

And that was why he couldn’t believe what he’d just heard.

“Enough? What in the world are you…”

“We’re out of time. The longer this goes on, the greater our sect’s losses will be.”

“Senior Brother!”

His voice rang with shock.

But the Taeeul Merciless Sword pressed his lips together, while the Roaring Fury Swordsman slowly stepped toward the two approaching Black Ghosts, gritting his teeth.

“The Second Brother is right. We’ve already secured a way out. Give the order, damn it! Now!”

He sounded more like he was berating him than urging him.

In the midst of this unexpected turn, the Wind-and-Cloud Sword Lord stared blankly at his two Senior Brothers.

“Are you… serious?”

But neither the Roaring Fury Swordsman nor the Taeeul Merciless Sword answered.

Unable to meet the wide, disbelieving eyes of their Junior Brother, they only watched the Black Ghosts before them, fear in their eyes.

They knew.

They knew how far their position strayed from the right path.

And seeing them like that, the Wind-and-Cloud Sword Lord finally accepted the unbelievable truth.

“…You were serious. Both of you.”

What was he supposed to call this feeling?

It was strange.

They had spent their entire lives together, studying under the same Master. Yet something about them felt unfamiliar, as if he were seeing them for the first time.

*Retreat. Retreat.*

The two words echoed in his hollow heart, and suddenly he remembered the past.

All the memories from the day he first joined the Zhongnan Sect until now.

Even in the distant past, long buried in dust, the three Senior and Junior Brothers had always been together.

That was why he’d been happy.

They were closer to martial artists than Daoists, and sometimes caused trouble with their aggressive words and actions, but they were still his Senior Brothers.

On the day he was appointed Sect Leader of the Zhongnan Sect, they’d been angry that they weren’t chosen—but in the end, they’d accepted it and followed him.

When trouble arose with the Nanman Beast Palace during the Great Faction War.

And just a year ago, when they’d been humiliated one after another by Jeok Cheongang and Jin Taekyung because of their own mistakes.

The Wind-and-Cloud Sword Lord had stood up for them. He’d stood up to those who criticized his Senior Brothers and defended them.

When they both recovered from their Internal Injuries at an astonishing pace, contrary to everyone’s expectations, he’d been the happiest of all.

But…

“Why have you become like this?”

The Wind-and-Cloud Sword Lord let out a quiet sigh.

He shrugged off the support of his two Senior Brothers, who stared at him with wide eyes, and gripped the hilt—all that remained of his beloved sword—so tightly it seemed ready to break.

“Do you remember? When our Master gave me this sword, he said: ‘You need not strive to become a Daoist. Just live rightly. If you uphold your duty as a human being, that is what makes you a Daoist.’”

“……”

“……”

“If you want so badly to live, then go, Senior Brothers. I’ll stay. That is the only way not to disgrace the name of the Great Zhongnan Sect we inherited from our Master.”

The Wind-and-Cloud Sword Lord, the Roaring Fury Swordsman, and the Taeeul Merciless Sword all knew.

Everyone on the battlefield knew.

If the Zhongnan Sect, one of the forces holding the battlefront together at this point, withdrew, this battle would be a certain defeat.

That was why the Wind-and-Cloud Sword Lord could never retreat.

At least, he couldn’t.

Grnk.

He bit his tongue. The sharp pain cleared his vision.

The Wind-and-Cloud Sword Lord stepped toward the two Black Ghosts, who approached in billowing clouds of black smoke.

Squish.

His steps were heavy. So was his heart.

Perhaps he, too, wanted to flee this place.

But the Wind-and-Cloud Sword Lord didn’t stop.

He couldn’t run away.

That was the duty his Master had taught him to uphold as a human being.

*Come to think of it, I wasn’t much of a Daoist either.*

He’d always envied the Huashan Sect for forging ahead, and pursued only the Zhongnan Sect’s interests.

He’d grown the sect’s influence through wealth exchanged in collusion with those in power, and accepted Disciples for their talent rather than their character.

He’d believed it was the right way to serve the Zhongnan Sect.

But even so, he’d never forgotten the bonds of affection and loyalty.

And even now, countless allies were fighting for their lives here.

In the most dangerous place, a young man was facing a crisis greater than anyone else’s.

Shame.

That was why he couldn’t retreat.

“Come. No—this time, I’ll come to you.”

The Wind-and-Cloud Sword Lord’s voice was thick with blood.

His eyes clearer than ever, he watched the two monsters approaching him and poured every last bit of energy into the beloved sword, now no longer worthy of the name.

Tsssss!

Brilliant Sword Force blazed.

The final flame he could kindle as Sect Leader of the Zhongnan Sect, as a martial artist.

“For the Great Zhongnan Sect.”

He murmured the words, then hurled himself forward with all his might.

“Don’t!”

“Junior Brother, Sect Leader!”

Leaving the cries of his Senior Brothers behind, the Wind-and-Cloud Sword Lord flew at them like a moth to a flame. Two streaks of light waited for him.

Whish! Sshhh!

A massive battle-ax that shattered the wind, and a white sword blade that sliced through space.

Charging into the wave of their destructive power, the Wind-and-Cloud Sword Lord calmly knew:

It was over.

Even this strike, made with every ounce of strength he had, wouldn’t stop them breathing.

But then, an unexpected turn—one that neither the Wind-and-Cloud Sword Lord, who had accepted his own death, nor anyone else on the battlefield could have predicted—took place.

Whoom—KWA-BOOOOM!

A distant, blinding flash struck like a massive shock wave, slamming into the area.

An explosion. A calamity.

He didn’t know what to call it, but one thing was clear.

Grind!

The unexpected shock wave threw the two Black Ghosts off balance where they stood, while the Wind-and-Cloud Sword Lord’s strike, already hurtling through the air, slipped between their two streaks of light.

Shhk!

The Heavenly River Thirty-Six Swords, made of dazzling light, cleaved through space.

Fwoosh.

The Wind-and-Cloud Sword Lord swept past the two Black Ghosts like the wind. And he—and everyone else on the battlefield—looked up on instinct.

Then, at last, they saw it.

Flicker.

A sphere of flame so enormous it was hard to believe it belonged to this world.

Hellfire, dragged up from the depths of hell—Hell Fire.
## Chapter artifact 1043

# Chapter 1043

For one instant, everyone on the battlefield stared at the sky, their eyes vacant.

Not a single person was an exception.

Not even the Wind-and-Cloud Sword Lord, who had brought down two Black Ghosts thanks to what could only be called a stroke of heaven-sent luck.

Not even his two pathetic Senior Brothers, who had somehow gone somber and were now rushing to support their Junior Brother as he staggered, utterly spent.

Not even the Disciples of the Zhongnan Sect and the Gansu Murim Alliance, still fighting their separate battles on the blood-soaked snow.

Not even a father standing like a stone monument where his son had disappeared, or the Fire Dragon Pavilion members pouring every last bit of strength into chasing after their friend and leader, who had already raced far ahead.

Not even the Dark Heaven cultists, whose eyes were empty as they continued their mindless fighting.

Every living being looked at *it*.

A vast sphere of fire, unlike anything they had ever seen or heard of.

Grrrrrrr-BOOM.

Would this be the sound of an ancient giant roaring?

If the hellish brimstone fires recorded in old scriptures really existed, would they look like this?

A deafening roar that left their ears ringing poured down over everyone’s heads.

Following the thing as it fell from dizzying heights like a meteor, an unbearable heat scorched the sky.

“A-aah…”

Groans rose from here and there.

Everyone froze where they stood. It was all they could do.

They were seeing it with their own eyes, and still couldn’t believe it. Something beyond comprehension.

No—a calamity.

That was why no one knew its exact name.

No one except the one person who had desperately tried to stop the calamity, but failed in the end.

*Hell Fire…!*

In a world that seemed frozen in time, Jin Taekyung bit back the scream rising between his lips.

Hellfire, just as its name suggested.

One of the most powerful wide-area spells a human could wield—and a calamity in its own right, capable of taking thousands of lives with a single cast.

*No.*

He knew its power better than anyone, and that was why he’d tried to stop it.

He hadn’t cared if he lost his life in the process.

If he could bring someone down in exchange—if he could stop the calamity—that would have been a decent end. He could have told himself as much.

But in the end, he hadn’t stopped it.

Right now, all Jin Taekyung could do was feel the weakness constricting his entire body and stare blankly as the calamity unfolded.

*Even now… I have to do something. Somehow.*

His vision wavered, no matter how desperately he wished otherwise.

And that wasn’t all.

Every bone and muscle in his body screamed in pain, as if squeezed in a giant’s fist. His dantian was already empty; he couldn’t find even a trace of internal energy.

The One Annihilation he’d launched while it was still incomplete.

That had been both misfortune and good luck.

Because it was incomplete, it hadn’t shattered every defensive barrier. And because of that, Jin Taekyung had survived.

But for someone who had been prepared to give up everything, this was misfortune.

*Shit.*

The horrible aftereffects tore deeper and deeper through his body. Jin Taekyung shuddered without meaning to.

But he couldn’t give up. He didn’t want to give up everything here.

Crack.

He clenched his teeth and moved his twitching arms and legs.

Gripping the spear shaft before it could slip from his grasp, he used it as a cane and hauled his unsteady body upright.

“—Run! Everyone, run!”

“Aaah! Aaaaaah!”

He heard the screams of those who finally understood that the calamity falling from the sky, painting it red, was real.

He heard, too, the terrible confusion and fear covering the battlefield below the hill—and, somehow out of place amid it all, a calm voice.

“Why don’t you just lie down? If you push yourself any harder, you really will be in trouble.”

At the Grand Mage’s utterly composed voice, blood trickled from between Jin Taekyung’s clenched lips.

“Shut your damn mouth, you bitch.”

“That’s a little harsh. When you think about it, I’m the one who saved your life.”

Pop.

She appeared beside him as if she’d teleported—or, rather, she’d used Blink, which was teleportation itself—and stopped less than a *jang* away.

More precisely, she stopped before the invisible magic barrier still standing between them.

“Honestly, you really surprised me just now. It gave me goose bumps.”

Her fingers, so thin and translucent that every vein showed through, gently traced the barrier.

The powerful barrier she’d personally layered dozens of times was down to a single layer, barely holding its shape. But she showed no sign of tension.

She knew Jin Taekyung could barely get to his feet under his own power, let alone attack.

“I’m only saying this out of concern, but don’t waste your effort. You know, don’t you? Killing me now won’t undo what’s already happened.”

“Yeah. I know.”

Jin Taekyung answered between ragged breaths.

But unlike his voice, his eyes weren’t on the Grand Mage.

He watched the hellfire as it crossed the blackened sky, as slow as its enormous size, and continued,

“I also know you—and the rest of your lot—can never kill me.”

Because he knew that better than anyone, Jin Taekyung turned without hesitation and gripped White Flame in a reverse hold.

He hadn’t risked his life just to kill the Grand Mage.

He’d fought to protect one ally rather than bring down one formidable enemy—to protect tens of thousands of lives.

*Please. Just once. One last time.*

With a desperate prayer, Jin Taekyung wrung every last thread of energy from his body.

He made his body, ready to break at any moment, into a bow and set White Flame, his spear, against its string.

Crrrk.

Excruciating pain filled his vision.

His already-weakened body screamed.

The acupoints damaged earlier by the excessive release of power burned even under the tiny amount of Scorching Yang Qi he could muster.

Grind.

But Jin Taekyung clenched his teeth and endured pain no ordinary person could even imagine.

He swallowed the blood pooled in his mouth along with the molar that had cracked and finally broken apart.

Even now, the blazing sphere was drawing closer to the ground. He aimed his spearhead at it.

A faint, delicate energy clung to the spearhead, like a heat haze. It could no longer be called Force.

“You really are a fool.”

The Grand Mage’s voice came with a sigh, but Jin Taekyung didn’t hear it.

He focused every sense and every ounce of strength on seizing his last chance.

*Can I do this? Can I?*

The question surfaced in his mind.

But Jin Taekyung already knew the answer.

No—or rather, anyone who saw this situation would give the same answer.

He couldn’t.

It was nothing but a foolish dream.

Nothing more than the desperation and hope of a man who wanted to do his best, right up to the end.

But…

*If I couldn’t even dream a foolish dream like this, I never would’ve made it this far.*

For one young man, life had been a long dream.

He’d been enraged by cruel reality, resigned to it, and, for a time, despaired. But the young man had kept dreaming.

Then, one day, the dream became reality.

In that dream, he discovered an unexpected new goal and longing, great power—and an even heavier responsibility.

That was the one reason.

The reason he could never give up, even if he was a moth flying toward a blazing flame, even if he was a firefly destined to vanish beneath the heat of the burning sun.

Step. Scrape.

His trembling legs finally steadied and planted themselves in the ground like iron pillars.

At the same time, his shoulder drew back. The spearhead aimed at the distant sky shot forward with his next powerful step.

*Go.*

Whoom!

Every bit of a person’s strength condensed, then burst forth.

At the same time, compressed air exploded outward.

Shwoooosh!

White Flame’s spearhead tore through the wind. It split open space.

A streak of light crossed the sky, dyed in ominous darkness, and shot toward a sphere whose size and power dwarfed it.

It covered more than a hundred *jang* of distance, shrinking until it became a single point. Jin Taekyung watched it with eyes growing dim.

The spearhead hadn’t reached its target yet.

But some things could be known without seeing them.

Like this.

*It’s no use.*

An empty murmur echoed in Jin Taekyung’s heart.

Failure.

He was nowhere near strong enough, fast enough, or possessed of enough internal energy to stop the Hell Fire the Grand Mage had prepared.

That was all. That was all there was to it.

Now that he’d poured out everything, Jin Taekyung had nothing left.

If anything remained, it was exhaustion weighing even more heavily on his body, and a helplessness greater than that.

And the enemy’s sneer—the one who’d brought all of this upon him.

“Oh, don’t be too disappointed. From where I was standing, it was a very impressive attempt.”

The Grand Mage spoke with a mix of sympathy and amusement as she watched the spearhead, carrying the faintest trace of energy, finally touch the Magic she’d cast.

And at the same time, she heard it clearly.

The deafening boom that rang out all around them, as if the sky had split apart.

KWA-BOOOOM!

“……!”

“……!”

Jin Taekyung and the Grand Mage both stared wide-eyed.

Grrrrrrr-BOOM!

Hell Fire.

The horrifying hellfire, the enormous sphere of flame, was shaking.

“What is this…!”

The Grand Mage was astonished.

The outcome had seemed as certain as a life-and-death duel between a child and a Supreme Peak master.

Jin Taekyung was exhausted, and the force behind White Flame’s spearhead had been pitifully weak.

That was why she’d simply watched without even trying to stop him.

She’d known from the start that he couldn’t do it.

To her, it was nothing more than a foolish dream.

And yet that single spear had changed the course of a sphere of fire hundreds of times its size.

It had bent part of the blazing flames and opened a rift in them.

“How…? How could this possibly happen?”

And in the midst of a reality she couldn’t begin to understand, the Grand Mage suddenly turned her head.

At last, she saw Jin Taekyung, forcing his unsteady body to hold together as he watched the unbelievable scene.

She saw the faint smile on his lips, and those lips, caked with dried blood, moving.

“Yeah. Nobody wants to give up.”

His voice came out with difficulty, but it rang clearly in her ears.

“Me, too. And them.”

“……!”

A brief remark.

But the Grand Mage felt something and whipped her head around. At the same time, she found the answer to the question she’d asked herself moments earlier.

Shwoooosh—KWA-BOOM!

Dazzling streaks of light shot up from the ground and rained down on the sphere of fire covering everyone’s heads.

The people who shared the same dream as that young man were there.
## Chapter artifact 1044

# Chapter 1044

The Roaring Fury Swordsman, Song Il, suddenly wondered what he was doing.

With barely enough time to escape this hopeless battlefield, why was he scattering his sword strikes with all his might?

Shwoooosh!

Force poured in streams along his blade, tearing through the air as it shot forward.

The dazzling streak of light, aimed neither ahead nor behind but into empty space, crossed a distance of more than twenty *jang* and struck the enormous ball of fire in the blink of an eye.

KWA-BOOM!

The sphere of fire shuddered with a deafening roar.

But its hesitation lasted only a moment. As the calamity continued its descent as if nothing had happened, despair filled the Roaring Fury Swordsman’s eyes.

*It’s no use. I can’t stop it.*

He knew by instinct. He’d already given it everything he had several times.

Though he was fully worthy of being called a superhuman, his strength was nowhere near enough to completely stop that enormous fireball, a force as unnatural as supernatural powers themselves.

*What the hell is this…*

He could barely breathe.

The unbearable heat radiating from the sphere of fire, slowly covering part of the battlefield even now.

The helplessness constricting his whole body—a feeling he’d experienced only a handful of times in his life.

But at that very moment—

Pop, sh-sh-sh-shk!

The Roaring Fury Swordsman felt it, and saw it at the same time.

Someone had appeared beside him, and with them came a dazzling light, flung forward with all their might.

Fwoosh!

*This is…*

The Roaring Fury Swordsman’s eyes widened.

Dazzling light spread. Even from more than twenty *jang* away, the heat that had warmed his skin vanished in an instant.

Dozens of streams of Force surged forward, brilliant and tightly woven like a net. And they were unmistakably familiar.

“Junior Brother!”

KWA-BOOOOM!

As his reflexive shout mingled with another deafening roar, a familiar figure appeared beneath the fragments of fire raining down from the collision.

“It hasn’t been long, Senior Brother.”

His expression and voice were so cold another person might have thought him indifferent.

The Roaring Fury Swordsman murmured, almost groaning, at the sight of his Junior Brother, known to the world by that very demeanor as the Taeeul Merciless Sword.

“How did you get here…!”

The Senior Brother’s face showed more confusion than joy, and a trace of worry and anger.

The Taeeul Merciless Sword answered calmly. “What, did you really think this Hwangbo Eom would follow your orders so obediently?”

“You fool! What kind of nonsense is that? What about Junior Brother, the Sect Leader, and the other Disciples?”

The Roaring Fury Swordsman bellowed, as fiery as his sobriquet.

Only moments ago, he’d turned away after entrusting the well-being of the Sect Leader—who’d finally collapsed from overwhelming fatigue and injuries—and the surviving Disciples of their sect to Hwangbo Eom.

And yet here he was, beside him, when he should have been leading them in a swift retreat.

For a moment, the Roaring Fury Swordsman forgot everything else around him and shouted at the top of his lungs.

“You idiot! If you’re gone too, who in the world is going to lead our sect…!”

“They say old habits die hard. You certainly live up to your sobriquet. Come to think of it, you’ve always been like that, Senior Brother—even as a child.”

“What?”

But no answer followed.

Ignoring his Senior Brother’s incredulous question, the Junior Brother silently swung his sword.

His face was as cold as ever, but his bulging veins showed that he was giving it more than ever before.

Shwaak! KWA-BOOOOM!

Force stretched out along his sword and collided with the flames.

The fireball faltered once more. Some of the fragments that broke off in the impact fell toward the ground, scattering sparks like a drizzle.

“As expected, this won’t be enough. Not by myself, at least.”

“……”

“Are you ready for the Moon-Shattering Sword Formation?”

Just as his Junior Brother had done moments earlier, the Senior Brother gave no answer.

The Roaring Fury Swordsman glared at the Taeeul Merciless Sword with fury in his eyes, then focused all his strength and swung his sword upward.

Shhk, shwoooosh!

Their sword strikes, as opposite as their temperaments, tore through the air side by side, shooting forward as though they were competing.

No—as they seemed to collide, they somehow blended together, increasing their power.

As if to prove they had grown from the same root.

KWA-BOOOOM!

The roar and shock wave were greater and more intense than ever.

Seeing the fireball’s course change by the slightest degree, the two Senior Brothers drew what little strength they could from the sight and began pouring out Force with everything they had.

Shhk, whoooosh!

They slashed, swung upward, and thrust.

Amid the ceaseless explosions, a voice slipped from the lips of the two old Daoists and reached the other’s ear.

“Don’t worry about Junior Brother, the Sect Leader, and the other Disciples. So Pyeong will do his duty well.”

“So Pyeong… I see. So that’s how it ended up.”

It was already too late to change things.

Only then did the Roaring Fury Swordsman realize who was leading the survivors of the Zhongnan Sect. Shadows fell across his face.

The Zhongnan Sect’s thousand finest.

In less than half a shichen, a third of them had been killed or wounded. Among those still able to move, there were few Disciples fit to entrust with the future.

Hyuk Sopyung, the Zhongnan One Dragon.

The Zhongnan Sect’s greatest prodigy, and one of the Ten Dragons and Phoenixes, the young talents hailed as the finest of the Central Plains.

Once, he’d been so lost in wine and women that he couldn’t come to his senses. But after the dispute between the Taeeul Merciless Sword and the Yongbong Escort Bureau, he’d shown dazzling growth.

In character as well as martial arts.

Even so, the Roaring Fury Swordsman’s concern did not fade.

“He’s still too young. You should have stayed behind instead.”

“By that reasoning, you’re the problem, Senior Brother, and we could go on forever. Besides, I was even younger than him during the Great Faction War. Junior Brother, the Sect Leader, was younger still.”

“That was different.”

“I’d like to ask how, but I’ll let it go this time.”

Shwaak!

The blade tore through the air.

The Taeeul Merciless Sword spread a net of Force with all his might, then added in a low voice,

“At least back then, the battlefield wasn’t overrun with supernatural powers.”

KWA-BOOOOM!

A roar like the splitting of the heavens. Heat so fierce it could burn them at any moment.

At the center of it all was a fireball much larger than it had been only moments ago.

It wavered for a moment, and parts of it broke away, but the calamity kept falling like an unchanging mountain.

The closer it came, the larger it seemed—the hellfire that would devour thousands of lives.

“Can we… stop that?”

The Roaring Fury Swordsman asked between ragged breaths. The Taeeul Merciless Sword, just as visibly exhausted, replied with a question of his own.

“What do I look like to you, Senior Brother?”

A short silence passed, yet felt as long as eternity.

But the Roaring Fury Swordsman had a good idea what his Junior Brother meant.

Right. They couldn’t stop it.

They were only human, and that was a power beyond their understanding, a force of supernatural powers.

If anyone could even slightly hold back this mad calamity, it would be the true superhumans—those whose human bodies had reached a realm comparable to monsters or gods.

“I feel like I’ve gone senile. I never thought I’d miss that mad old monster, the Fire King.”

“For once, I had a similar thought. A moment ago, I saw some reckless brat flash before my eyes. It made me wonder if I’d really lost my mind.”

The Fire King, Jeok Cheongang.

And the Blazing Flame Divine Dragon, Jin Taekyung.

To the two Senior Brothers, they were beings they would never forget as long as they lived.

For all the wrong reasons, of course.

“They won’t make it here, will they?”

“Why ask? You already know.”

The senses of a Supreme Peak master surpassed anything an ordinary person could imagine.

The two men, reading the events unfolding across the battlefield, already suspected that neither the old monster nor the young one from the Fire Gate Clan could come to their aid.

And at the same time, they held the contradictory wish that they didn’t want help from either of them, whatever the circumstances.

Even now, they hadn’t been able to let go of their grudge against the Fire Gate Clan’s Master and Disciple.

And that grudge had led them to commit an irreversible mistake.

KWA! KWA! KWA-BOOOOM!

Explosions rang out one after another.

But the Force of the Roaring Fury Swordsman and the Taeeul Merciless Sword had grown noticeably weaker. The fireball, now less than ten *jang* away, radiated a hideous, searing heat.

Hot enough to burn away even the last of their will to fight.

Grrrrrrr.

It was hot.

A crimson-black shadow, unlike anything they’d ever seen and something they’d never experience again, covered part of the battlefield.

“Do you… regret it?”

The Taeeul Merciless Sword’s quiet question passed between his parched lips.

The Roaring Fury Swordsman stared blankly at the sky and answered.

“Yes.”

Seeing his Senior Brother like that, the Junior Brother didn’t ask anything more.

He didn’t ask what he regretted.

And seeing his Junior Brother, the Senior Brother didn’t ask either.

He didn’t ask whether the one asking him regretted it, too.

Though they’d exchanged only a few words, they’d said everything.

Only silent thoughts circled through their minds.

*We shouldn’t have done that.*

The two men had temperaments as different as their sobriquets, but they’d lived similar lives. In this moment, the same thoughts came to them.

Their peaceful childhood, spent honing their martial arts instead of cultivating compassion and justice.

Their bloody youth, spent chasing achievements rather than the righteous path of the warrior.

The time when, as their black hair turned white, they’d quickly become tainted by personal gain and selfish desires amid the peace they’d regained.

And then—

> *I hear you two went through quite an ordeal.*

One day, after paying the price for their greed and becoming trapped in the depths of Internal Injuries and demonic thoughts, a tempting hand had reached out to them, consumed as they were by hatred.

> *This is a rare elixir I managed to acquire. Its effects rival Shaolin’s Great Restoration Pill. It will be more than enough to heal your Internal Injuries.*

Though they’d made clear they did not want to meet, the uninvited guest had secured an audience anyway. Seeing the two martial brothers distrust his almost unbelievable generosity, he said something they could not refuse.

> *This isn’t generosity. It’s a transaction. And if you accept it… not only will you settle an old grudge, you’ll help protect the Zhongnan Sect.*

They’d hesitated, but in the end, accepted the deal.

They’d spent their lives as the direct disciples of the Zhongnan Sect Leader, heroes of the Great Faction War and respected masters of the martial world. They couldn’t go on living with this indelible humiliation weighing on them.

They had to take revenge.

Even if their revenge stopped short of killing, they had to make the Fire Gate Clan suffer the same humiliation they had.

And the deal would also ensure the safety of the Zhongnan Sect.

So they couldn’t refuse the sweet offer.

They’d gladly taken the hand held out to them by the uninvited guest. No—by Sima Gong, the Black Night King.

Only months later did they regret the decision they’d made.

Even now, they stared at the blazing flames slowly covering the sky above them.

> *How did it come to this?*

The Wind-and-Cloud Sword Lord.

His Junior Brother, the youngest of them, had asked those words in a hollow voice.

The moment they heard the regret in his voice, they understood.

What choice remained to them.

What they had to do.

“Run. There’s still time.”

“I refuse. You go, Senior Brother.”

“I refuse, too.”

Three *jang*.

The two Senior Brothers stared, dazed, at the enormous sphere of flames now filling their entire field of vision.

“It was never possible to begin with.”

“That’s right.”

“Then why did you come?”

“For the same reason you did, Senior Brother. I felt I had to do something. Even if it was only this. And…”

Two *jang*.

The heat and light pouring from the flames were so blinding that the Taeeul Merciless Sword closed his eyes.

Or perhaps he was too ashamed of himself to face the world openly as he died.

“…I was ashamed. I was sorry.”

To the Master who’d taught them benevolence.

To their youngest Junior Brother and the Disciples of their sect, who’d treated them as Senior Brothers despite how unworthy they were.

To everyone else.

And to a certain Master and Disciple who, unlike them—who’d strayed from the path long ago—still walked the righteous path.

“This is truly one hell of a mess.”

The Taeeul Merciless Sword—or the Roaring Fury Swordsman.

The voice that might have slipped from either man’s lips sounded more hollow than ever.

Fwoooooosh!

The heat and light pouring from the enormous fireball, stretching across hundreds of *jang*, were more magnificent than ever.

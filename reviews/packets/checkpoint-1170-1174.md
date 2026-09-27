# Checkpoint Review — 1170–1174

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

# Chapters 1170–1174

## Plot

Jin rejects the importance of being chosen, deciding instead to keep carrying his burdens and survive alongside his allies. Morgoth reveals he returned the Skeleton King to make Jin stronger and notices a trace of the being he sought in the object at Jin’s neck. Jin’s spear pierces Morgoth’s Dragon Heart, killing him and releasing its accumulated power. The Skeleton King revives as a Lv. 180 Undead King, while Jin falls unconscious from exhaustion.

The released power triggers the Great Cataclysm: darkness spreads from Moscow, the System’s Rift and Collapse quest fails, and Gates mutate across Eurasia. The new Main Quest, Predestined Collapse, warns of irreversible consequences. As monster waves emerge worldwide, Hunters and governments mobilize; a battlefield alert announces that Alpha has awakened.

After three days, Jin wakes and learns that the crisis has worsened. He visits the still-unconscious Cheon Taemin at a secret facility beneath the Pentagon, confirms that Taemin is the Martial God and a former Player, then tells his allies he will leave to confront the invader from beyond their world.

## Continuity

- Morgoth is dead; his Dragon Heart opened and released the power that began the Great Cataclysm.
- The Skeleton King revived as a Lv. 180 Undead King. Jin survived, but was unconscious for three days from exhaustion.
- The Great Cataclysm and Collapse are underway, with Gates mutating and monster waves emerging worldwide.
- The Main Quest “Rift and Collapse” failed; “The Foreordained Collapse” replaced it and warns that player choices can have irreversible consequences.
- Alpha has awakened; what Alpha is and what its awakening means remain unknown.
- Cheon Taemin remains unconscious in a secret facility beneath the Pentagon. Jin knows Taemin is the Martial God and a former Player.
- Jin intends to confront the invader from beyond this world and knows its location.

## Translation Decisions

- Use “Great Cataclysm” for 대격변, “Collapse” for 붕괴, and “The Foreordained Collapse” for 예정된 붕괴.
- Use “Undead King” for 언데드 킹, distinct from the Skeleton King.
- Keep “Dragon Heart” for 드래곤 하트 and distinguish mana from magical power.

## Durable state

{
  "active_continuity": [
    "Three days passed while Jin Taekyung was unconscious; Choi Minwoo and the others survived.",
    "The Dragon Heart opened, causing magical power and rift progress to surge.",
    "The Main Quest “Rift and Collapse” failed; “The Foreordained Collapse” warns that player choices can cause irreversible consequences.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon; Jin knows he is the Martial God and a former Player.",
    "Jin intends to leave to confront the invader from beyond this world and knows its location.",
    "An alert reported that Alpha had awakened; what Alpha is and what its awakening means remain unknown."
  ],
  "continuity_sources": [
    1174,
    1173
  ],
  "open_questions": [
    "What is Alpha, and what does its awakening mean?",
    "What choices will Jin make in the new Main Quest, and what consequences will follow?",
    "Why is Cheon Taemin still alive despite the capsule’s stated permanent binding to its Player until death?"
  ],
  "safe_through": 1174,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1170

# Chapter 1170

The relief of finally getting the Skeleton King back lasted only a moment.

Jin Taekyung’s eyes sank as he heard the Dragon’s words spill between bloodied teeth.

“I was chosen by God?”

Morgoth gave a dry laugh at the question that escaped like a mutter.

“If you’re asking me, that’s foolish.”

“What does that—”

“Jin Taekyung, I cannot know all there is to know about you. I can only guess. Even Asmodeus, who brought countless worlds to their knees with his immense power, would be no different. He may be omnipotent, but he is not omniscient.”

Of course.

Omniscient and omnipotent were words meant for only one being.

God.

A being nowhere to be seen, yet present everywhere.

One who knew all things and could do all things.

But now, Morgoth was looking not at the sky, but at Jin Taekyung.

At a human wearing the shadow of the God he had spent thousands of years searching for like a cloak.

“Ask yourself, not me. The answer is there.”

“……!”

His eyes trembled. His body stiffened.

Jin Taekyung gave no answer.

No—he couldn’t answer.

He was swept away by a wave of memories that came crashing in without warning, amid a single shiver racing up his spine.

*Asmodeus is dead. On the day I was born. The day of our victory.*

At the heart of the enormous temple built atop the desert, the Jin Taekyung of the past spoke through gritted teeth to the enemy before him.

*He was erased, and we won. That’s all. That’s the truth.*

The hoarse voice coming from his lips sounded unfamiliar, as if it belonged to someone else.

Watching him, the monster of the abyss—the Doppelganger—smiled.

*That is also true, Jin Taekyung, chosen one. It must be all you know, and the truth as you understand it.*

Chosen one.

When Jin Taekyung first heard that strange phrase from the Doppelganger, he had no idea that before long, he would hear the same words from someone he never expected.

*So it was you.*

In the imperial palace’s grand banquet hall, covered in the rebels’ blood and corpses, the Bow Saint finally revealed her identity and spoke.

*The chosen one the Martial God spoke of.*

Right.

This wasn’t the first time.

The Doppelganger. The Bow Saint. The Martial God, who had left her a letter.

Even the System had called him the chosen one.

On the very day he erased the Doppelganger.

> **System**
>
> You are the chosen one, Master of the Ark.

Remembering that brief line of System text, Jin Taekyung looked at Morgoth.

More precisely, at his own reflection in the Dragon’s enormous eye.

“You’re right.”

Unlike his body, soaked in exhaustion, his eyes shone more clearly than ever.

Jin Taekyung continued, as if whispering to himself.

“Maybe… I already knew the answer.”

He’d always wondered.

Where had this incredible power he’d suddenly gained come from? And who had given it to him?

But he’d done nothing but deny and doubt it.

Why him?

Of all the billions of people in the world, why had an insignificant F-rank Hunter been chosen?

If a God as omniscient and omnipotent as that truly existed, why hadn’t He personally stopped the countless tragedies and disasters that had happened?

But the instant he heard Morgoth’s question, he understood why he had kept turning away from the truth, even when it was right in front of him.

“It was too much. Everything I had to carry, every moment.”

His father’s untimely death. The family he left behind. A life that could continue only by standing on someone else’s sacrifice.

The burdens took different forms, but weighed the same.

And each one pressed down on a person’s body and mind like a mountain.

“Maybe that’s why I came to resent God.”

“Resent Him?”

Morgoth laughed, his voice thick with bloody phlegm, at the unexpected answer.

“Interesting. You, who should be more grateful to Him than anyone?”

“I’ve lost too much for that. Things that mattered more than anything.”

“You gained things, too. They must have mattered just as much.”

“Yeah. The more they matter, the heavier they are. Now they’re almost too much to bear.”

“Do you really think so?”

“You don’t know me. You know even less about humans.”

“No. I know them well. Perhaps better than anyone among you.”

With that calm reply, Morgoth looked out at the world sinking into the colors of sunset.

“This place is certainly different. It’s nothing like the world where I was born and raised.”

Of course it was.

This strange world called Earth had neither three moons and a sun, nor twelve continents and nine seas.

And that wasn’t all.

There were no great cities built and run entirely by magic, no brilliantly colored natural landscapes teeming with spirits.

Nor were there different races living across the world, each protecting its own territory.

If the disaster called the Great Cataclysm hadn’t brought such enormous changes, the contrast would have been even more striking.

“But I found one exception. Even if Asmodeus had never invaded this world, this one thing would have remained the same.”

Jin Taekyung suddenly realized what Morgoth was about to say.

“Humans.”

“Yes. You humans. The weakest and most foolish beings among all the races I’ve seen and known. That was what I found so strange.”

Looking straight at Jin Taekyung, Morgoth added,

“Even in the world I left long ago, humans were always the rulers.”

“……!”

“At first, I couldn’t understand it. Your lifespans and wisdom couldn’t match the elves. You weren’t physically gifted like the dwarves, and you didn’t even have the reproductive capacity of monsters.”

And yet, humans had thrived in Morgoth’s homeland.

The civilization they built was so brilliant that no race except the Dragons could match it. The fame of their extraordinary mages and knights had crossed the seas and shaken every continent.

The race Morgoth thought inferior in every way had seized dominion over a world.

And after a long period of study and amusement, longer than ever before, he finally found an answer.

“Desire. You humans are made of endless desire. That’s why you keep changing.”

He had found the answer, but he couldn’t understand it.

Humans were such complicated creatures.

When they were weak, they banded together as if they’d made a pact. When their numbers grew, they split apart again and again.

Even after gaining more than enough, they continued to fight.

To capture beautiful elves and enslave them.

To plunder the dwarves’ mines, where gold and treasure lay.

To use monster parts to study Magic and make weapons sharper and stronger.

They even fought to kill their own kind and take their land.

They didn’t fight to survive. They bled and died to get something more.

Their desire had turned into greed.

“But not all humans were like that. If some were ruled by instincts uglier than a monster’s, there were others at the opposite extreme.”

The eyes that had once glinted like obsidian had long since lost their light.

Morgoth looked at Jin Taekyung through a gaze that was slowly growing dim.

“Like you.”

“……What are you trying to say?”

“You’re human, too. So you have desires rooted deep in your heart, and you must have kept changing to fulfill them, whether you wanted to or not.”

“That’s—”

Jin Taekyung suddenly fell silent.

Everything Morgoth said was true.

At first, he’d simply wanted to get stronger.

To break free of the limits imposed on him, and through that, gain more money and fame—and become a son and older brother his family could be proud of.

But when he came to his senses, everything had changed.

And with it came the weight of an enormous responsibility he had never imagined—and could never have imagined—just two years earlier.

*Then how have I managed to bear all this until now?*

The answer was close at hand this time, too.

*I changed, too. Enough to bear the responsibility as it kept getting heavier. I kept changing.*

And the world called that something else. Not change.

Growth.

He had grown, and he was still growing.

A child had become a boy, a boy had become a young man—and before he knew it, a torch lighting the way for all humanity, a new savior.

That was why what Jin Taekyung held deep in his heart was the purest of desires, and at the same time, something beyond the word desire.

“Hope.”

In that moment, Morgoth could feel it.

The power and bright vitality in the word that had passed through those parched lips.

“Hope. Is that the answer you found?”

Jin Taekyung shook his head.

“That’s what I thought. But it wasn’t.”

“Then?”

“I’d just forgotten. I was so overwhelmed, just struggling through one suffocating moment after another.”

That was exactly it.

He hadn’t found it. He had remembered.

A feeling he’d forgotten somewhere along the way.

Even though everyone looked at him and thought of hope, Jin Taekyung himself hadn’t felt at ease for a single moment.

Because he was a torch.

He had to press forward alone at the very front, fighting the deepest darkness.

But not anymore.

Jin Taekyung hoped more fervently than ever. He wished, he prayed.

That he would survive to the end alongside those who were fighting even now, shouting his name.

And that this goddamn story would, please, have a happy ending.

“Honestly, I don’t care who chose me. Even if it was all a delusion or a misunderstanding.”

Using his spear as a cane, Jin Taekyung pushed himself to his feet.

“I’ve made it this far, and I’ll see it through.”

*Shing.*

Like the unwavering will of its master, the spearhead retained its keen edge and flashed in the sunset.

“I have one question.”

“I’ll allow it.”

“Why?”

The question was brief, but Morgoth understood what lay behind it.

Jin Taekyung was asking why he had so readily given up the Skeleton King.

Why he would say these things and act this way toward the one who was about to end his life of thousands of years.

But to Morgoth, the answer was obvious—and simple.

“If you can become even a little stronger, then what comes next will be more interesting.”

“What?”

At Jin Taekyung’s stiff-faced reply, Morgoth laughed aloud.

His laughter held both a longing for amusement that he could not quite give up, even in the face of death, and self-mockery.

*Yes, Asmodeus. Now I understand why you summoned me to this world.*

He had realized it far too late, but this was enough.

He had seen a being who stood outside the ordained order, and confirmed the existence of a human chosen by God.

And—

*That thing around his neck… It can only be. I’m certain.*

Morgoth had seen it clearly.

One object, glimpsed through Jin Taekyung’s clothes, torn to shreds.

At the same time, he could feel it clearly.

A mysterious energy, neither mana nor magical power, enveloped it completely.

*How fortunate. At least I could confirm a trace of that person.*

With those words fading emptily in his heart, Morgoth summoned the last of his strength and opened his mouth.

“Now, shall we begin a new amusement?”

In that instant—

*Shwaa!*

The dazzling sunset shattered into pieces, following the streak of light shooting toward the Dragon Heart.
## Chapter artifact 1171

# Chapter 1171

It was like a jewel.

A jewel possessed of a beauty and mystery beyond any work of art in the world—or even all of them combined.

But the thing casting an ominously dark glow in every direction was no mere mineral.

Dragon Heart.

Just as its name said, it was the heart and source of power of the mighty race known as Dragons.

And now, in this moment, someone who had once been the wisest and most powerful Dragon Lord since the division of heaven and earth—and had fallen deeper into corruption than any other Dragon—was realizing that his long life had come to an end.

With his whole body. With his soul.

And with a sound ringing in his ears like thunder.

*Crack.*

Hairline fractures spread across its smooth surface like a spiderweb.

Nothing could stop the cracks in the Dragon Heart, which had barely held its shape through the master’s iron will and the last of his strength.

There was only a streak of light, bringing forward the destruction that had already been ordained.

*Crunch!*

It shattered. Split apart.

The sunset glow that had flowed along the spearhead—and the Dragon’s heart, which had never allowed anyone to touch it.

*Rumble.*

Darkness surged out in place of blood.

The surrounding air trembled, as if the world had realized what was about to happen.

But even in the moment his life was fading, the Demon Dragon’s gaze never wavered from the Divine Dragon who had driven a spearhead into his heart.

“Fight with all the strength you’ve been given. Keep surpassing yourself. Keep struggling.”

The voice that slipped out as if in soliloquy held neither regret, anger, nor a curse.

It was encouragement the listener couldn’t understand, tinged with deep disappointment.

He would miss the astonishing amusement that lay ahead.

“…So I can see it, wherever I am.”

At that moment—

*Rumble.*

Everything in the area stopped moving.

The wind. The air.

Even the Dragon’s enormous body, which had just breathed out its last after a life beyond imagining.

And then—

*Whooooom!*

The Dragon Heart spilled the millennia of time and nearly infinite magical power stored within it in every direction.

* * *

Darkness and brilliance should never coexist.

But for that moment at least, everyone on the battlefield saw and felt it clearly:

A pillar of dazzling darkness surging skyward, and an enormous power erupting as it shook the whole world.

And the first to experience it—and the one closest to it—was, naturally, Jin Taekyung.

*Whoosh—*

From the moment he faced the pitch-black darkness that covered his vision in an instant, he didn’t need to think anymore.

Jin Taekyung moved on instinct alone.

As he pulled his spearhead from the Dragon’s heart, he cradled the Skeleton King’s head—recovered at last—deep in his arms and curled up like a fetus.

Then he felt the wave of magical power crash over him, tearing through the brief silence.

*Rumble, rumble!*

A deafening roar filled his ears, and the world turned upside down.

The sky and earth spun around and around, making his vision reel, while a feeling of weightlessness took hold of his entire body.

But Jin Taekyung managed to stay conscious through the chaos thanks to his own iron will—and the clear sound of bells that even the roar couldn’t drown out.

*Ding. Ding. Ding.*

> **System**
>
> You have defeated Lv. 195 “Black Dragon Duke” Morgoth!
>
> You have achieved the great feat Dragon Killer!
>
> Achievement Reward has been granted!
>
> You have gained a tremendous amount of EXP!
>
> Your Intimidation has increased significantly!
>
> You have acquired the Title Dragon Slayer!
>
> All abilities are greatly increased when fighting dragonkin. If you ever encounter another Dragon, how it treats you will depend on its disposition.
>
> Level Up!
>
> Level Up!
>
> Level Up!
>
> Level Up!
>
> All injuries and status effects have been healed!

System notifications.

The clearest proof that he had survived yet another crisis.

Maybe that was why Jin Taekyung was about to let go of the thread of consciousness he’d been holding onto with all his might.

*I want to rest.*

That was all he could think about.

He didn’t care what happened next.

His body was still flying off into the distance like a cannonball, but what did that matter?

Morgoth had certainly met his death, and the countless monster armies had been utterly shattered and reduced to prey.

Even if he crashed into something and broke a few bones, he’d be fine.

No—he might not even feel pain.

If he closed his eyes now, he would fall straight into a deep sleep that could easily drown out any physical pain.

With everything over, there was nothing to keep him from resting.

*Right. Nothing.*

At least, that was what Jin Taekyung was sure of.

Until he heard someone’s voice in his ear, just before he let his terribly heavy eyelids fall shut.

“Damn it. This is awful.”

At first, he thought he’d imagined it.

Or that the howling wind had made him hallucinate.

But neither was true.

He wasn’t asleep yet, and the voice that followed was so clear it proved all of this was real.

“To wake up in the arms of some guy reeking of sweat. Just my luck.”

The gruff voice was all the more welcome for it. Jin Taekyung forced his eyes open with every ounce of strength he had.

He stared blankly at the owner of the voice, who had somehow awakened in his arms, then suddenly opened his mouth.

“You can’t smell anything. You’re undead.”

“…You bastard.”

A brief silence, then a single curse.

But an unmistakable laugh crept into the words, and golden energy running across the brow of the pure-white skull burned like a torch.

Feeding on the Dragon’s magical power spilling in every direction, it blazed more fiercely than ever.

*Whoosh!*

In an instant, the thick darkness that had spread on the wind shot toward Jin Taekyung.

No—to be precise, the being in his arms was sucking it in.

As if rain awakened life, the sun gave it strength, and the earth nourished its growth.

*Fwoosh.*

The more darkness seeped in, the clearer the golden energy became.

And beyond those two contrasting streams of color, a shadow steadily grew.

It was a wondrous sight unlike anything anyone had ever seen.

Regeneration. Resurrection.

Perhaps even a new birth.

But the thing that grew by devouring all the darkness around it was no ominous presence.

Even if someone else might point at him and curse him, Jin Taekyung would never see him that way.

He shone as brightly as that radiant golden crown.

*Rustle.*

Jin Taekyung blinked.

The dizzying world had stopped spinning, and the wind that had whipped past like blades was gone.

Through his dreamlike, hazy consciousness, he could make out only the familiar touch of someone carefully laying him on the ground, and a single line of text hovering above that person’s head.

[Lv. 180 “Lord of the Dead” Undead King]

The friend he’d met again after a brief farewell had changed a little. Jin Taekyung let out a hollow laugh at the sight.

He thought of that day long ago, when the two of them had joined forces to defeat the Arch Lich.

“You’ve grown a lot, Bones.”

The Skeleton—or rather, the Undead King—replied as casually as ever to words that still stood clear in his memory.

“Well, I was always a little taller.”

“Bullshit.”

“Now, now. How vulgar.”

The next moment, the two friends laughed aloud as if they’d planned it.

They didn’t know exactly what had happened to each other while they were apart, but one thing was certain.

They trusted each other, and they’d fought to protect what they held dear.

“Human.”

“What?”

“You’ve been through a lot.”

Maybe he really had reached his limit. Jin Taekyung answered in a faint voice, the sound of his friend’s words seeming to echo from far away.

“…Yeah. You too.”

“Rest easy.”

If Jin Taekyung had been his usual self, he would have grumbled, “What, is someone dying?” But this was as far as he could go.

Rest easy.

That short, tempting offer was more powerful than Morgoth’s magic, and his exhausted mind was already poised to defy his will.

*Thump.*

His head drooped, and his eyelids shut tight. The Undead King watched as his friend sank into a deep sleep, as if he’d passed out the instant the words were spoken.

Then he murmured, as if to himself, the words he hadn’t quite been able to add.

“…It’ll be far too short a rest for you to rest easy.”

If Jin Taekyung’s will had held out just a little longer, he would have understood exactly what those words meant.

No—he surely would have figured it out on his own, even without hearing it from him.

The Jin Taekyung he knew had power and instincts as remarkable as his foul temper.

But the gigantic Grand Mage who had drawn near without anyone noticing was also, beyond a doubt, one of the most remarkable beings among all of humanity.

“Why? Why on earth?”

His voice was full of confusion, and his eyes wavered.

Magic Johnson, dragging his battered body along, looked around as if under a spell.

The joy of reunion and the thrill of victory had long since vanished from his mind.

He’d first come to check on Jin Taekyung, but the ominous pulse of power coming from every direction made him forget all of that.

*Rumble.*

Magic Johnson gritted his teeth.

A mage who had reached such a high realm could sense it all the more clearly: a boundlessly dark, swamp-thick energy.

Magical power.

So pure and dense that it called to mind the decades-old past, when the Great Cataclysm had reached its height, it was staining everything around them.

“…Dragon Heart.”

The last Grand Mage of humanity trembled before he knew it, having realized the cause.

A source of magical power so nearly infinite that it made even the vast power the Undead King had absorbed seem like a drop in the bucket.

But the thought that had suddenly occurred to Magic Johnson was darker and more ominous than the magical power the Dragon Heart continued to pour out.

“Surely…?”

“Yes.”

The Undead King tried to sound calm, but couldn’t hide the fear in his voice as he gazed at the swelling darkness and added,

“It’s begun. No—more precisely, it’s been completed.”

He was right.

It was the final piece and the key to this enormous puzzle.

The beginning of another catastrophe, completed by the death of the greatest and most powerful Dragon.

*Beep.*

At that instant, a cold mechanical tone rang out—one that only the chosen could hear, yet now reached no one.

*Rumble, rumble!*

With a tremendous roar that shook the world, the pillar of magical power connecting heaven and earth exploded.

Like an active volcano that had finished making all its preparations.
## Chapter artifact 1172

# Chapter 1172

“Active volcano” was no exaggeration.

If anything, it fell woefully short.

From the moment the last breath of the evil Dragon that had terrorized the whole world for thousands of years dispersed, an unstoppable catastrophe had been racing along its predetermined course.

An eruption—or an explosion.

It didn’t matter what you called it.

As if this were all it had left to do, the Dragon Heart had, for the first time, slipped beyond its master’s control and vomited everything it had accumulated over an unfathomably long time out into the world.

Using the body of the Dragon that had finally met its end as kindling, it raged more fiercely than a newly awakened active volcano.

*Roooar!*

Before the deafening roar that shook heaven and earth even reached their ears, everyone on the battlefield felt the terrifying shock wave.

The S-rank Hunters were gathering the bodies of the seven Guardians who had found peace with Morgoth’s death—their former comrades.

Thousands of Hunters were chasing monsters that had lost the will to fight and scattered in every direction.

At that enormous, instinct-stirring rumble, they all turned their heads in the same direction as if on cue. Then they froze like statues.

*Fwoooosh.*

A chilling cold carried on the wind. A dark, ashen mist.

And beyond it, a towering pillar of pitch-black darkness, vast beyond comprehension.

“What is that…?”

The solitary groan that slipped from someone’s lips spoke for everyone staring at the scene before them in stunned disbelief.

The evil Dragon—Morgoth—was definitely dead.

They had won here today. The immediate danger was gone.

So why?

Why did that deep, pitch-black darkness feel more frightening than the unprecedented monster that had split the sky and poured its deathly breath down upon the earth?

They already knew the answer.

Their senses and minds, frozen by the icy magical power, simply hadn’t reacted in time to the memory of *that day*—the day that had arrived without a word of warning just a few decades ago.

But two beings realized what was happening first—and more clearly than anyone else.

“…We have to stop it.”

The Lord of the Dead spoke to the Grand Mage, who was muttering as though possessed by something unseen, his voice vacant.

“We can’t stop it.”

Unlike Magic Johnson’s, the Undead King’s tone was calm.

As if he’d already given up on everything.

But that wasn’t true.

There was still hope in his words, however faint—a tiny ember that had yet to lose its light.

“At least, not right now.”

With those quiet words, the Undead King held his unconscious friend in his arms and felt warmth pass into his fingertips.

That was right.

Their hope hadn’t gone out yet.

And protecting that ember was the best they could do now.

“We’re leaving. Right now.”

Before something happened that couldn’t be undone.

Unable to force out the words that had risen to the back of his throat, the Undead King and Magic Johnson turned away.

The sky above them was no longer filled with mere storm clouds. It was turning to pure darkness, casting a cold shadow over them.

The Great Cataclysm.

The three ominous syllables humanity had forgotten over the past few decades were branded into everyone’s minds once more.

And even after the Grand Mage’s large-scale Warp Magic Formation appeared and vanished in a dazzling flash, a hard mechanical beep—one that hadn’t reached its owner—continued to ring out somewhere in the world.

*Beep.*

> **System**
>
> The distribution and concentration of **magical power** are skyrocketing. Take action immediately.
>
> **Current Rift Progress:** 73%
>
> When the **Rift** reaches a certain level, the ferocity and strength of **monsters** increase significantly.
>
> **Current Rift Progress:** 85%
>
> When the **Rift** reaches a certain level, the danger posed by **Gates** and the probability of a **Monster Wave** increase significantly.
>
> **Current Rift Progress:** 90%

.

.

.

> **System**
>
> You have failed to meet the Quest success requirements.
>
> **Mission:** Defeat “Black Dragon Duke” Morgoth (Complete)
>
> Halt the Rift’s progress (Incomplete)
>
> Main Quest Rift and Collapse has failed.
>
> A new Main Quest, Predestined Collapse, has been created.
>
> Good luck.

* * *

The System never lied.

And even people who didn’t know it existed had no need for its warning messages. Every change came dramatically.

Or like a marauder who barged in without warning.

“The magical power levels…! They’re skyrocketing!”

“It’s not just the Moscow area! St. Petersburg and Novosibirsk—and even the Kazan region…!”

Like waves crashing into one another, panicked shouts from all directions swallowed each other up.

Eyes webbed with red veins. Veins bulging along people’s necks.

The pit of this dreadful chaos wasn’t confined to any one place.

It was happening in underground bunkers around the world, where the people who ran entire nations had gathered; in cabinet meeting rooms; and, on a smaller scale, anywhere with an internet connection.

The Hunters still on the battlefield weren’t the only ones who witnessed the unbelievable phenomenon.

When a spearhead wreathed in flames cut through Morgoth and the thick storm clouds covering Moscow’s sky, billions of people had been given a brief chance to watch a battle that would decide their fate.

They shuddered at the sight of the evil Dragon falling, then cheered the young hero who had saved them once again.

But humanity didn’t know that the single ray of light shining on them in their deepest despair would fade before the tears they shed had even dried.

*Rumble.*

Those watching the unstable, grainy feed transmitted from a satellite suddenly realized something was wrong.

A gigantic pillar, spewing darkness so vivid it looked unnatural—like a black hole sucking everything in.

That was all they saw.

Dazzling. That oppressive beam, so bright it seemed impossible to call it darkness, closed the sky. This time, it never opened again.

And the darkness that had swallowed Moscow began to multiply.

*Roooar.*

Like a horse galloping across the wilderness, the darkness raced silently through a world steeped in quiet.

East, west, south, north.

Wherever its hooves passed, the light vanished.

Just as it had blotted out the sunset over Moscow, the darkness devoured every light.

Even the blazing sun couldn’t pierce the darkness. No—the pure, profound magical power. The stars in the sky vanished, too.

By the time the Dragon Heart, having poured out all its strength, crumbled to dust, the catastrophe that had finally blossomed had already scattered its spores across the world.

Just like now.

“Code Red! Code Red! Mutation Gate detected!”

“Mutation Gate? Shit, we’re calling that Code Red now? Report only Monster Waves!”

The superior’s bark was understandable.

A few years ago, the appearance of a Mutation Gate would have covered the front page of morning papers and dominated every breaking-news broadcast. Now the situation was so urgent that even that had become something to dismiss.

But the shout that came next was so clear and shocking that it wiped his jumbled thoughts clean in an instant.

“A-all Gates across Eurasia are mutating at once.”

“What?”

“At least twenty percent of them have reached levels high enough to progress into Monster Waves…”

He didn’t hear the rest.

Seized by the sudden ringing in his ears, the superior fell silent. He squeezed out every last bit of strength and managed to say one thing.

“Tell the higher-ups immediately.”

“Which higher-ups, exactly…?”

There was no time to answer.

There were more than a thousand Gates scattered across Europe and Asia.

Shoving aside his hesitant subordinate, the superior picked up a special communications device he hadn’t touched once in the more than ten years since he’d been appointed head of this place.

A direct line that connected to only one place.

After a signal that seemed to ring on forever, someone answered. The tremor in the recipient’s voice was impossible to hide as they summed up the situation.

“Activate Code Black.”

That was the end of the call.

But both of them knew that this brief conversation, lasting less than a minute, would go down in history.

Or rather, anyone who understood what the words *Code Black* meant knew.

And those facing the recipient on-screen—the person who had just set down the receiver, the President of the United States—belonged to the tiny fraction of humanity privy to that top-secret information.

“It's begun.”

“…Yes. In the end.”

Though they differed in race and gender, these two hundred people shared one thing: they all led a nation. For a while, they looked at one another in silence.

There was only one exception among them: a distinctly young East Asian man.

He wasn’t a national leader, nor did he have the seasoned, battle-hardened political instincts they did. But he had every right to attend this gathering.

He was also the person who best understood the wishes of someone unable to attend today.

“It’s begun, but it isn’t over.”

His face was still healing, his hair matted with blood.

But no one criticized him for appearing before them like that without showing proper respect.

No—they wouldn’t dare.

The young man before them was a hero who had bled and fought for the world in their place.

Just as his grandfather, recorded in humanity’s history, had—and just as those who had fallen in Moscow today had.

As if this place didn’t belong to him, Choi Minwoo stood alone and continued, his voice and eyes burning like torches.

“We will end this war.”

The ominous code name that hadn’t been spoken anywhere for decades: Code Black.

No—the Great Cataclysm.

The irreversible war had already begun, and the hero was not dead yet.
## Chapter artifact 1173

# Chapter 1173

Humans are animals that learn.

Of course, they often forget important things. But if they forgot everything without ever learning a thing, humanity as we know it wouldn’t exist.

They kept learning, little by little.

And over millions of years, they developed without end.

They learned to use fire and chip away at stone, until at last they glimpsed the boundless world of empty space above the clouds.

But for humanity, which had built a great civilization over such an unfathomable stretch of time, the past thirty-odd years were far too short to forget the horrific catastrophe named the Great Cataclysm.

*Wheeeeeee!*

A blaring siren swept over the city—no, over the entire world.

Faster than magical power rising from the frozen lands of the Far East could stain the sky, and with an urgency that couldn’t even be compared to it.

Naturally, every available person and resource was thrown into action without restraint.

Governments declared martial law and deployed the military to evacuate their citizens to safe zones. The whole process moved swiftly and efficiently.

For better or worse, ever since Morgoth appeared, people had been gripped by fear. They’d already evacuated, or made all the preparations to do so at a moment’s notice.

But even those still beneath the blue sky faced no less danger.

—Monster Wave detected 3.2 kilometers away to the east and west!

—Sending location and scale. Deploy immediately!

The System was right again.

The rift stage was over. The Collapse had begun.

As magical power spiraled out of control, countless Gates scattered around the world began opening their dark maws, one after another. Monsters poured out of that cursed world, rampaging with greater strength and savagery.

Just like now.

*Rumble, rumble.*

The ground trembled at the vibrations coming from far away.

So did the hand gripping the handle of a Tower Shield bigger than its owner, tight enough to crush it.

*Thump.*

At the heavy touch that suddenly landed on his shoulder, the young man jumped as if burned. Then he let out a sigh of relief.

“…Team Leader.”

“You’re jumpy, kid.”

The middle-aged man grinned, showing his teeth between bristly whiskers. The young man might have been annoyed for a moment, but instead he swallowed hard and answered.

“N-no, I’m not.”

“Sure you are. It’s obvious. Just be honest.”

“Well, the truth is, a little.”

“Look at this guy. You call yourself a Hunter, and you’re already scared before the fight’s even started?”

“…I’m sorry.”

The young man’s face fell in an instant. The middle-aged man, who’d been putting on a stern expression, and the Hunters around them all chuckled.

“Team Leader, you keep that up and the kid’ll cry. Give it a rest.”

“Now, now. A grown man shouldn’t cry over something like this. We’ve all been through it once. Back in my day…”

“Jesus, here comes his ‘back in my day’ latte again.[^1] And all he ever drinks is Mocha Gold.”

[^1]: The Korean phrase for “back in my day” sounds like “latte,” setting up the instant-coffee joke.

“I switched a while ago. White Gold now.”

“Good for you.”

“Thanks.”

“Don’t mention it. It’s nothing.”

Listening to the old guys chatter, the young man felt like his head was about to burst.

*Where am I, and who am I?*

In this serious situation, where he should have been on edge, what was this conversation that made him lose all his nerve just listening to it?

*Did I pick the wrong team?*

Of course, there was a serious flaw in that thought.

The young man hadn’t had a choice in the first place.

And the person who’d “picked up” this twenty-year-old and brought him into a veteran party with an average age of 41.5 suddenly spoke.

“How about it?”

“Huh?”

“Feeling a little better?”

The young man blinked for a moment, then answered.

His voice was much calmer than before, but even more bewildered.

“Uh, yes.”

“You were so stiff I figured I’d mess with you a little. Don’t be too hard on me for fooling around at my age.”

“N-no, not at all. I’d never think that.”

“Good. But I understand either way. It’s natural to shake at first. Your nerves are bound to be on edge.”

The middle-aged man patted the young man’s shoulder encouragingly and laughed out loud.

It was a friendly laugh, hard to believe coming from a face that could make even the most vicious criminal think twice.

Maybe that was why the young man, who was at the bottom of the pecking order in this veteran party, decided to work up the courage to speak.

“Um, could I ask you something?”

Thankfully, that laugh hadn’t come from a vicious criminal pretending to be an ordinary person.

When the middle-aged man readily nodded, the young man cautiously continued.

“Why did you choose me…”

His words trailed off after only a few syllables.

But that was enough for the middle-aged man to understand. He answered without a moment’s hesitation.

“You reminded me of someone.”

“Reminded you of someone…?”

“Yeah. Someone I know.”

Truth be told, when the middle-aged man first saw the young man two days ago, he’d looked like every other rookie he’d ever seen.

Arms and legs locked stiff. Lips parched. Eyes darting around anxiously.

But if that had been all there was to him, the middle-aged man wouldn’t have chosen him as a teammate to entrust with his life.

“I saw you training.”

“Training?”

“Yeah. You were working really hard. Hard enough to look desperate.”

“But that was…”

“I know. All the rookies there were doing it. Trying to stand out so they’d get into a decent team.”

That was right.

Two days ago, when the two of them first met, hundreds of rookies who’d just graduated from the regional Hunter training center had gathered there, showing off as they waited for their team assignments.

They wanted to get into a team with a better chance of survival.

Not to earn more money like before, but to protect the one thing they couldn’t trade for anything: their lives.

And of all those rookies, the young man had been the only one who wasn’t there.

“Where were you then?”

“Outside. I needed to find somewhere without people, somewhere with a little space.”

“Why?”

“Because I had to train.”

“You could’ve done it there, like everyone else, and used it to show off, couldn’t you? Everyone knows the people in charge watch the waiting room through the monitor room.”

“That’s true, but…”

The young man hesitated, then continued.

“I didn’t think I could train properly in there.”

Naturally. It was a waiting room, not a training room for the official test. It was fairly spacious, but with so many people swinging around bladed weapons, it would have been hard to concentrate.

But the young man was different.

The act of training might have been the same, but his reason for doing it was entirely different.

He was working with all his heart.

Not to get onto a good team, but to become even a little stronger.

That day, after secretly following the young man, the middle-aged man had watched him train alone in an empty lot. The sight brought back a memory from a few years ago.

“That guy was like that, too.”

“Who?”

“The friend I mentioned earlier. I ran into him at a Hunter manpower office. He was young, like you—no, younger. A rookie at a glance. I figured I wouldn’t be seeing him for long.”

“Was there a reason you thought that?”

“He was F-rank.”

“Ah.”

F-rank.

At the word, the young man understood.

An untouchable in the Hunter world.

So far beneath the bottom that you could tack UCK onto the F and it would fit perfectly.

The young man had even thought the same thing on the day he got his first rank assessment, when he saw the E on the monitor:

*At least I’m not F-rank.*

But just as the young man was different, so was the “guy” the middle-aged man was talking about.

“At first, I didn’t know I’d keep seeing him for over half a year.”

“At least he managed to find work, then.”

“What are you talking about? I said he was F-rank. I had some experience and connections, so there were places that’d occasionally call me in as a porter. But an F-rank rookie? Not a chance.”

“But you just said…”

“I said I saw him. I didn’t say we worked together.”

The young man’s eyes widened.

“So he just kept showing up at the manpower office? Even when there was no work?”

“Yeah. For nearly half a year. From the crack of dawn until evening, without missing a single day.”

Most people would’ve quit by then.

That is, if they’d been ordinary people.

“He wasn’t. He’d leave a perfectly good sofa behind and climb the hill behind the office, training like hell every day. Like some guy I saw two days ago.”

“...!”

“He’d take a number, train, come back when his turn was up, get turned down like always, take another number, train again… He never even got near a Gate, but by closing time at the office he’d be more exhausted than someone who’d done five runs in a day.”

The young man listened, dazed, then answered honestly.

“I think I would’ve lost it halfway through.”

“Right? And here’s the funny part: his face always looked miserable, and his mouth was going *fuck, fuck, fuck*, but he trained harder than anyone I’d ever seen. He wasn’t doing it because it was easy. He did it even though it was hard. Every single day.”

“That’s incredible.”

“Yeah. He was an incredible guy.”

“No, I mean you, too, Team Leader.”

“Me?”

“If you saw him every day for half a year, doesn’t that mean you were doing the same thing he was?”

The middle-aged man was quiet for a moment, then let out a hearty laugh.

“You got me. Heh. But I’ll never be like that guy.”

“I don’t think that’s true. You’re already amazing.”

It wasn’t just flattery.

Just as the middle-aged man had watched the young man, the young man had been watching his superior closely, too.

He’d only known him for two days, so it was a stretch to say he’d watched him for long. But he’d seen more than enough to know he was someone worth respecting.

“My dream is to become like you, Team Leader.”

“...Me?”

“Yes. You have character, skill, and you work hard. I even saw a news article about you once. I remember the headline: *From F-rank to B-rank: A Hunter’s Life of Extraordinary Ups and Downs.*”

The young man had dredged up an embarrassing chapter of his life that the middle-aged man would rather forget. Laughter broke out around them, and the middle-aged man scratched his bushy beard, his face turning red.

Just as he started to stammer out a reply, his expression suddenly hardened.

*Rrrrrumble.*

The vibrations were stronger than they’d been ten minutes ago. Now they weren’t just coming up through the soles of their feet; they were shaking their whole bodies.

*It’s coming.*

Everyone felt it at once, and realized anew how close they were to death.

But they couldn’t back down.

They were humanity’s last line of defense.

They must have been given their powers for this very moment.

“Hey, rookie.”

“Yes, Team Leader.”

The young man answered hoarsely when the call came from behind him.

At some point, his hand and his Tower Shield had stopped shaking.

“Thanks.”

“What?”

“Thanks for saying I’m someone’s dream.”

Even now, the middle-aged man—Im Kkeokjeong, Team Leader of Ares Guild’s Team 32—hadn’t lost his smile. He pulled his helmet down low and thought:

*I may not be able to become like that guy, but I’m a Hunter, too.*

Then he fixed his gaze on the dust cloud rising a few hundred meters away and shouted with all his might:

“Formation—!”

At that moment, as a roar pierced the sky, the communicator on Im Kkeokjeong’s chest received a message.

—All Hunters, listen. Alpha—Alpha has awakened.

A blade-sharp wind swept across the battlefield.
## Chapter artifact 1174

# Chapter 1174

The first thought that came to me when I opened my eyes was simple.

*Is this a dream?*

It wasn’t an unreasonable thought.

Anyone who saw that perfectly white ceiling, spotless and dozens of meters high above a room as vast as a sports field, would probably have thought the same.

But a moment later, I realized this was all real.

*This place…*

It was familiar.

Or rather, maybe not familiar exactly, but I’d definitely been here before.

Even through the dreamlike haze of my mind’s eye, I vividly remembered staying in a place like this—both there and in reality.

Then, the voice that reached me confirmed what I’d been thinking.

“You slept well.”

His voice carried unmistakable exhaustion.

Following the sound, I saw a familiar face and parted my parched lips.

“Yeah. I tend to sleep a lot.”

I saw it.

A faint smile appeared on Team Leader Choi’s usually stern face.

I was probably smiling, too, from the way he looked at me.

* * *

For Hunters, meeting again alive held a very special meaning.

But the smile that briefly touched Choi Minwoo’s lips, and the joy of seeing each other again, lasted only a moment.

Just as he’d said, they were alive. And because they were, they had to face reality.

“How much time has passed?”

Jin Taekyung didn’t beat around the bush, and Choi Minwoo saw no reason to hide the truth.

“Three days. About seventy-six hours, to be exact.”

“…Three days.”

It wasn’t a long time.

For someone living an ordinary life, it was just the blink of an eye.

But Jin Taekyung knew better.

He’d known from the moment he saw Choi Minwoo, exhausted from head to toe.

No—maybe he’d known even before he lost consciousness.

“A lot happened while you were away, Mr. Jin.”

Choi Minwoo paused to catch his breath, then added, almost to himself,

“A lot. So much.”

For a while, only Choi Minwoo’s voice echoed through the vast, empty white space. When his story ended, the silence that followed lasted even longer.

Unlike Jin Taekyung’s mind, where countless scenes and voices were still swirling together.

*Let me ask you one thing.*

—You have my permission.

*Why?*

—If you can grow even a little stronger, what comes next will be all the more entertaining.

Jin Taekyung remembered the end of the wicked Dragon who had sent the world trembling.

He remembered the vivid emotion that even the shadow of death looming right in front of him couldn’t hide.

—Fight with every last bit of strength you have. Keep surpassing yourself. Keep struggling.

Even in his final moment, as the last breath of his life faded away, Morgoth hadn’t shown the slightest anger.

—So I can see it from where I am.

It had been nothing more than a sigh.

A sigh born from the fact that he hadn’t been the one chosen by God, and from the regret that he wouldn’t be able to experience the grand game about to begin.

The vague sense of foreboding that had seized Jin Taekyung at that moment had become reality three days later, sweeping across the world.

*He knew what was going to happen.*

Judging by Morgoth’s actions, Jin Taekyung didn’t think he’d wanted this outcome from the start.

More precisely, that no longer mattered.

The Dragon Heart, Pandora’s box containing every kind of calamity, had opened.

And this time, it wasn’t a myth. It was real.

The power contained in the wicked Dragon’s heart, which had pulsed for thousands of years, was incomparably greater than that of the Hatchling Michael Silbert had defeated in Paris.

It was without precedent.

Even if Choi Minwoo hadn’t told him what had happened, the signals reaching Jin Taekyung through his five senses would have proved it.

*Beep-beep-beep.*

> **System**
>
> —There are System messages you haven’t checked.
>
> —The distribution and density of magical power are skyrocketing…
>
> —Current progress of the rift…

Jin Taekyung wasn’t the only one who’d woken up after three days.

Dozens of holographic windows he hadn’t been able to check while unconscious washed over his retinas like a wave, and he was swept along with them.

Among them, he fixed his eyes on the words that glowed an especially vivid red, like reefs hidden beneath a violent current.

> **System**
>
> —Quest success requirements have not been met.
>
> —Main Quest, Rift and Collapse, has failed.
>
> —A new Main Quest, The Foreordained Collapse, has been created.
>
> —Would you like to view this Quest? Y / N

Jin Taekyung thought the final message, asking for his consent, was crueler than ever.

He had no other choice.

*…View Quest.*

And a little while later, Jin Taekyung finally broke the long silence.

“Team Leader Choi.”

“Yes?”

“I need you to gather everyone. Right now.”

Choi Minwoo already had a good idea exactly who Jin Taekyung meant by “everyone.”

He also knew that Jin’s request included one being who was more human than most humans.

* * *

Maybe it was because the space was so vast.

Team Leader Choi’s absence—he’d left without asking a single question—felt like a big one.

But I wasn’t lonely.

I still had someone to talk to.

Of course, there was the slight problem that my companion wasn’t in any condition to hold a normal conversation.

Knock, knock.

I tapped on the surface of the transparent recovery capsule, as if knocking on a door.

Then I gazed at the face of the person sleeping soundly inside.

*Cheon Taemin.*

I’d learned this as soon as I regained consciousness: this was a secret facility deep beneath the Pentagon.

A vast hospital room and shelter built for one person alone, inaccessible even to the President of the United States.

“Well, now there are two of us.”

My words, spoken almost to myself, received no answer.

Just as always.

But I didn’t mind and kept talking.

“I know what kind of person you are. Better than anyone else in the world.”

There was no longer any doubt that Cheon Taemin and the Martial God were the same person.

Or that he’d been a Player who’d used the System before I did.

But one question still remained deep in my heart.

“How are you… still alive?”

It was a cruel thing to ask someone who was still breathing, but I had to ask it.

The instruction manual for that beat-up old capsule, the starting point of all this, said it remained permanently bound to its Player until the Player died.

But ironically, it was this incomprehensible error that had given me the reckless courage to go alone to face Morgoth.

*I thought that if I died, you might wake up.*

I quietly swallowed the words that had risen to my throat.

At the same time, I remembered something Morgoth had said.

*The one chosen by God.*

I didn’t doubt it anymore.

I was chosen.

Whether I’d wanted it or not.

Some great being existed—a being humanity had never encountered, even after reaching out beyond the clouds and into space. Another dimension existed, too.

And that unknown being was asking me a question.

Through the receiver called the System.

*Open System window. View Quest.*

*Ding!*

> **System**
>
> **Quest**
>
> The Foreordained Collapse
>
> At long last, the balance of the world has crumbled.
>
> This is no mere coincidence.
>
> It is the spark left behind by an invader from beyond this world, and the flame kindled by all of humanity, yourself included.
>
> But one last chance remains.
>
> Save the world by preventing the collapse, even if only a little.
>
> At the same time, remember this:
>
> Just as a great mountain leaves its mark when it moves, every choice you make will affect the whole world.
>
> **Grade:** None
>
> **Restriction:** Jin Taekyung
>
> **Mission:** ???
>
> **Reward:** ???
>
> **Failure:** ???
>
> —This Quest may change drastically depending on the Player’s choices.
>
> —Be as cautious as you can. A single choice may bring about irreversible consequences.

This was the first time.

The first Quest to warn me with words and a tone this heavy.

And so the decision I’d already made in my heart began to waver.

Maybe—maybe my choice really would bring about the terrible consequences the System had warned me about.

But there was no time.

The feeling that if I delayed any longer, things would truly become irreversible weighed on my body and mind.

Just like those hurried footsteps I could clearly sense beyond the countless layers of magic covering this place.

*Whoosh.*

As the Grand Mage’s hand dispelled the magic, familiar faces came into view.

Comrades I could trust with my back. Friends I’d gladly lay down my life for. People I could call family now.

I turned to them and spoke my first words.

“Have any of you ever traveled between dimensions?”

The Skeleton—or rather, the Undead King—muttered awkwardly.

“Uh… are you still half asleep?”

“…You little shit.”

Of course, it sounded like a dream.

A nightmare, if anything.

* * *

The people—or, more precisely, several people and one monster—couldn’t bring themselves to speak even after I’d finished explaining.

The first to break free of that unspoken staring contest was the huge Grand Mage, who’d been wearing a dazed expression throughout the whole story.

“I’m being serious. If you’d said something like that two or three hundred years ago, they’d have accused you of being a witch and burned you at the stake.”

“I agree, but I’m not a woman.”

“By the time they tied you to the stake, you would’ve been. They’d just have to cut off what’s dangling down there.”

“Fair enough.”

“Actually, we don’t have to go that far back. Before the Great Cataclysm, they’d have locked you up in a psychiatric hospital for saying that.”

“Probably.”

“But now… Yeah. This is after that damn Great Cataclysm. And I’m the Grand Mage.”

That was right.

These were the times we lived in.

It had only been three days since we’d fought to take down a Dragon the size of an aircraft carrier. After hearing my whole story, no one suggested putting me in a psychiatric hospital.

Not even the monster.

That was why not one of them doubted my story for a second.

Even in a world a little different from this one, I was sure they would have believed me.

Just as Jeok Cheongang had believed in me.

And there had only been one reason I’d confessed the secret I’d kept deep in my heart.

“I’m… going to leave. To put an end to all of this.”

I knew where the invader from beyond this world was.

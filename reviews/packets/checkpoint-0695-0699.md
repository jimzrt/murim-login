# Checkpoint Review — 695–699

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

# Chapters 695–699

## Plot

Jin Taekyung, Yohi, Muyaho, the guardian spirit, and a vast beast army invade the Nanman Beast Palace as civil war erupts. After Jin breaks through the North Gate, the beasts destroy the Outer Palace watchtowers and confront Baeksang, who admits betraying Nanman to pursue a decades-old promise. The Southern Heaven Demon Empress then appears and reveals herself as Honglan, the courtesan Jin once rescued. She opens a massive rift behind the Inner Palace, releasing demonic qi and claiming the Lord of Heaven has blessed the resulting evolution.

The Beast King Stone’s radiance blocks the demonic qi, prompting the Empress to demand it for the Lord of Heaven. Jin and the White Tiger attack her while Yohi evacuates civilians. Their clash devastates the palace, and Baeksang rescues an old attendant before continuing toward his office. There, after finding the Empress absent and believing her promise broken, he sees a dark figure carrying a Force-infused sword emerge from his mirror. Meanwhile, the White Tiger leads the beasts in rescuing victims, while Jin repeatedly rises despite severe injuries and continues fighting the overwhelming Empress as darkness consumes the Inner Palace.

## Continuity

- The Nanman Beast Palace is collapsing amid civil war and the Great War begun by Jin’s arrival with the beast army.
- The Southern Heaven Demon Empress is Honglan, the former singing courtesan from Dongting Lake, and is vastly stronger than Jin.
- She created the massive rift behind the Inner Palace, whose demonic qi is corrupting and killing Nanman’s warriors and beasts.
- The Beast King Stone’s radiance is currently suppressing the demonic qi; the Empress seeks the stone for the Lord of Heaven.
- Jin, Yohi, Muyaho, and the White Tiger remain at the center of the confrontation. Yohi is evacuating civilians, while the White Tiger leads beast rescues.
- Jin has suffered severe Internal Injury and cracked bones but continues fighting because retreat would doom Nanman and the Central Plains.
- Baeksang has betrayed Nanman for a decades-old promise from the Southern Heaven Demon Empress. He reached his office, found it empty, and nearly lost hope.
- A dark human figure carrying a sword imbued with Force has emerged from Baeksang’s mirror. Its identity, allegiance, and connection to the Empress’s promise remain unresolved.
- The Empress’s attack on Jin, the fate of the Beast King Stone, the extent of the demonic qi’s spread, and the survival of Nanman remain unresolved.
- Dark Heaven’s larger scheme had not yet begun when the beast army entered Nanman, but the Empress’s rift and the Lord of Heaven’s blessing are now active threats.

## Translation Decisions

- Use **Beast King Stone** for 수왕석 and **sacred stone** for 신석; use **divine artifact** for 신물.
- Retain **Southern Heaven Demon Empress**, **guardian spirit**, **White Tiger**, **Force**, **Internal Injury**, and **demonic qi**.
- Use **mirror** for 면경 and keep the figure emerging from it unidentified.
- Use **Hwi** for 휘 in Baeksang’s vocative.
- Preserve Jin Taekyung’s conversational, determined, and bluntly profane first-person voice.

## Durable state

{
  "active_continuity": [
    "The demonic qi from the rift is devastating the Inner Palace and overwhelming Nanman's warriors and beasts.",
    "Baeksang has betrayed Nanman while pursuing a decades-old promise from the Southern Heaven Demon Empress.",
    "Baeksang reached his office, found it empty, and broke down after believing the promise had been abandoned.",
    "The office mirror rippled and emitted a dark human figure carrying a Force-infused sword, reviving Baeksang's hope.",
    "The White Tiger leads the beast army in rescuing victims of the demonic qi and carrying them toward the Outer Palace.",
    "Jin Taekyung is severely injured but continues fighting the Southern Heaven Demon Empress.",
    "Jin considers the Southern Heaven Demon Empress stronger than the Western Heaven Demon Lord.",
    "Darkness is descending over the collapsing Inner Palace as the confrontation worsens."
  ],
  "continuity_sources": [
    699
  ],
  "open_questions": [
    "Who or what is the dark figure emerging from Baeksang's mirror, and how does it fulfill the Southern Heaven Demon Empress's promise?",
    "Can Jin Taekyung survive his injuries and stop the Southern Heaven Demon Empress?",
    "Can the White Tiger and the beast army rescue enough victims from the demonic qi?",
    "What will Baeksang do now that the mirror's promise has begun to manifest?"
  ],
  "safe_through": 699,
  "temporary_decisions": [
    "Use mirror for 면경 and do not identify the figure emerging from it until the source confirms its identity.",
    "Use Hwi for 휘 in Baeksang's vocative, while keeping the mirror figure's identity unresolved.",
    "Retain Force for 강기, Finger Qi for 지풍, Internal Injury for 내상, and hellscape for 지옥도.",
    "Preserve Jin Taekyung's first-person voice as conversational, determined, and bluntly profane when describing the Southern Heaven Demon Empress."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 695

# Chapter 695

At first, no one paid any attention.

No—it would be more accurate to say that no one had even had time to worry about anything else.

The major incidents that had occurred one after another recently, along with the general mobilization order, had caused the military forces to swell by the day. Even the ordinary tribespeople living in the Outer Palace had been reduced to holding their breath, while nearly ten thousand warriors and beasts of prey waited in the Inner Palace for their new Palace Lord.

Even so, there were still those who remained at their posts amid the chaos.

“I’m going to die. It’s hot, and the atmosphere is a mess. If this was how things were going to be, I should’ve been stationed at the East or West Gate, where things are nice and quiet.”

At the young junior’s grumbling after returning from patrol, a middle-aged warrior with graying hair, sitting with his back against the wall of the North Gate, clicked his tongue.

“Tsk, tsk. Look at you. You’re still young and have your whole life ahead of you, yet you’re already thinking about slacking off.”

“Is that something you can say after sitting in the shade while I was out on patrol?”

“I’m old, aren’t I? And if I don’t rest at a time like this, when am I supposed to?”

“Well, I suppose you’re not wrong.”

The Nanman Beast Palace had three gates in total: the East, the West, and the North Gate where they were stationed.

There had never been a South Gate. The sheer cliff rising behind the Inner Palace was sturdier than any gate could have been.

“How was the patrol? What about the Outer Palace?”

“There wasn’t even a single rat in the marketplace.”

“……Of course there wasn’t. Everyone must be nervous.”

The middle-aged warrior sighed.

There were nearly ten thousand warriors gathered in the Inner Palace alone. It was an army large enough to be called a small country without exaggeration.

Not since the Great Faction War more than fifty years earlier had so many warriors gathered in one place.

History had a way of repeating itself.

The older people kept their mouths shut as they remembered the past, while parents pulled their children close and barred their doors.

Anxiety filled the air on all sides—the anxiety that a massive war would soon break out.

“But… are we really going to war with the Central Plains?”

At the young junior’s cautious question, the middle-aged warrior answered quietly.

“Who knows? But one thing is certain.”

“What?”

“Before we fight a war in the Central Plains, blood will have to be spilled right here in Nanman.”

“……!”

“You know that the former Palace Lord is still alive, and that the five tribal chieftains who support him left the Outer Palace. The higher-ups will want to settle things internally before heading to the Central Plains.”

This was not something only the middle-aged warrior had guessed. Anyone with a certain amount of sense and life experience would have arrived at the same conclusion.

A civil war.

A civil war for the first time in more than three hundred years was waiting for them.

To pass through the road leading to the Central Plains, they would have to walk over the corpses and blood of comrades with whom they had shared hardship until only a few days ago.

“……”

The shadow that had always been absent from the young warrior’s carefree face now settled over it.

Among the tribespeople who had left the Outer Palace were several close friends who had grown up with him.

Watching the junior’s darkened expression, the middle-aged warrior quietly rose to his feet.

“Where are you going?”

“I’ve slacked off enough. I’m going to take a quick look around the walls. My body’s aching from sitting still for too long.”

“Don’t bother. Just keep resting. The other squad should be covering the walls anyway—”

“Do you think those idiots will stand watch properly? They’ll all sneak down here like us and sit in the shade. If the higher-ups catch us, I’m the gate captain, so I’ll be the only one who gets my ass chewed out.”

He was not wrong. Since outsiders almost never entered, the guards had never been particularly strict even in normal times. After an army of nearly ten thousand had taken up position, they had become even more lax.

Even someone desperate to die would have been committing suicide by attacking the Nanman Beast Palace now.

Besides…

*Everyone must be troubled.*

There were not as many people burning with fighting spirit as one might expect.

Yayul Cheok, now branded a traitor who had betrayed Nanman, was a Palace Lord respected by everyone. And the tribespeople, who had lived together beneath the banner of the Nanman Beast Palace for more than three hundred years and grown accustomed to one another, were wary of the civil war and Great War that had arrived at their doorstep.

But what could they do? When the people above gave the order, those below had to obey.

“Whew.”

The middle-aged warrior let out a sigh and climbed onto the wall. Just as he had expected, the top of the wall was quiet.

Well, there was at least one man left behind. The problem was that he was asleep and snoring loudly.

*…Fine. Get some rest while you still can.*

This was the calm before the storm. Perhaps today would be the last day these pathetic subordinates of his could rest.

Shaking his head, the middle-aged warrior stood tall atop the wall and stared into the distance.

It was noon.

The sun, already high overhead, radiated suffocating heat, and the high hill overlooking both the broad pasture beyond the North Gate and the Outer Palace shimmered in the heat haze—

*Wait.*

What was that? Had he seen it wrong?

A question flashed through the middle-aged warrior’s mind, and his eyes widened.

But no matter how many times he blinked or roughly rubbed his eyes with his sleeve, the scene before him did not change.

“What… is this?”

The dazed words slipped from his lips before he even realized it.

At the far end of the direction in which the middle-aged warrior was looking, a massive White Tiger took a step forward.

Step.

Its fur was pure white, almost silver. Its enormous forepaw brushed through the grass as it advanced. At the same time, a wind that had come from somewhere swept through the forest behind the hill.

Whoosh!

The densely tangled branches swayed, along with the countless leaves hanging from their ends. And beneath the shade cast by the thick forest, another forest began to move.

Rumble.

The ground shook, the air trembled, and the wind scattered. Countless pairs of vertically slit eyes gave off a chilling gleam.

“……!”

The middle-aged warrior’s mouth slowly fell open.

Beasts of prey.

An unimaginably vast number of beasts of prey.

As nothing more than an ordinary warrior, he could not even begin to guess how many beasts lurked beyond that forest or where those predators, with their sharp teeth and claws, had appeared from.

But he could guess one thing.

The being leading that army of beasts, which sent chills down his spine simply by looking at it, might perhaps be a person like himself.

Whoosh!

Large and small silver figures raced across the pasture with the cool wind.

By then, the number of White Tigers had increased to two. They stopped before the enormous iron gate, along with the man and woman riding on their backs.

*Th-that’s…*

The middle-aged warrior’s pupils trembled.

If he had been anyone else, he might not have recognized the identities of the man and woman at once.

But he had been responsible for the North Gate for the past ten years. The moment he saw their faces, he felt as though he had been struck in the back of the head with an iron club.

How could he not know?

The woman was one of Nanman’s only four Great Chieftains, while the other young man was…

*Jin Taekyung.*

Just thinking of those three syllables made it difficult to breathe.

There was no doubt.

It was him. The outsider who had come to this land for the first time in hundreds of years after the destruction of the Five Poisons Sect. The eye of the enormous storm hanging over Nanman.

He—Jin Taekyung—had come to the Nanman Beast Palace of his own accord.

And he had brought with him countless beasts of prey and Yohi, the Great Chieftain of the Yao people, who was said to have been abducted by him.

*Wh-what in the world is going on…?*

But before the middle-aged warrior could finish his question, one person’s tightly closed lips opened.

“A word of advice. You’d better take your hand off that.”

“……!”

The middle-aged warrior froze just as he instinctively began to sound the alarm. Watching him, Jin Taekyung inwardly let out a sigh of relief.

*Thank God. I’m not too late.*

The moment he saw the face of that unknown warrior, he knew. Dark Heaven’s sinister scheme had not begun yet.

*If the Rift had opened, this place would already have been transformed into a hell where no human could live.*

And yet, within this stillness—a stillness so quiet that it felt ominous—he sensed a bomb with its fuse burning down.

“Right, Whitey?”

The enormous body beneath his backside flinched.

The guardian spirit of the sacred stone. True to that name, the White Tiger, which had regained its former appearance, sent its thoughts outward.

—…How dare you call this body a name like that?

“You would’ve been Blackie before. Of course, I’m not a racist.”

—What in the world are you babbling about? You sound like a mad human.

A madman, huh? Yeah. I’d heard that one a fair number of times in my life.

Muttering inwardly, Jin Taekyung gave a quiet laugh and lowered the spearhead in his hand.

Fear of what lay ahead? Of course he had it.

But he had crossed countless thresholds between life and death to reach this place, and he had done everything he could with the situation he had been given.

Baeksang. The Southern Heaven Demon Empress. Dark Heaven.

It no longer mattered who stood in his way. He would simply stake his life and fight back.

*That’s right. Stake my life.*

This was a battle with tens of thousands, hundreds of thousands—perhaps even more—of lives on the line.

Blood might flow like rivers, and corpses might pile up into mountains.

But…

*I have to do it.*

Someone had once said:

*Do everything in your power, then leave the result to Heaven and wait.*

But Jin Taekyung thought differently. Only when a person could even change the will of Heaven could it truly be called *Will*.

*Isn’t that right?*

He raised his head and looked up at the sky. In place of an answer, scorching, dazzling sunlight poured down.

On a day like this, he could not afford to die.

Of course, that applied in any weather. He hated dying, and he had no intention of dying.

Even if…

the Lord of Heaven were waiting behind this iron gate.

Swish! Slash!

In an instant, a blue-white Force tore through the air like a flash of light and split the enormous iron gate in two.

The guardian spirit, reborn as a dazzling silver White Tiger, released a roar that shook Heaven and Earth.

—GRAAAAAAAWR!

Hidden inside the predator’s jaws, opened wide enough to swallow the world, were not only teeth harder than steel and a red tongue.

Fwoosh!

A brilliant beam of light.

In an instant, blinding radiance dyed the world.

A pillar of light surged from the sacred stone held inside the guardian spirit’s mouth, passed over the fortress walls, and pierced the sky.

BOOOOM!

It was a pillar of light large enough to be seen from a hundred li away. Perhaps even a thousand.

Everyone could see that strange power, that wondrous sight.

The ten thousand warriors gathered in the Inner Palace.

And the immeasurable number of beasts filling the hill.

—Kyaaaaaaau!

—GRAAAWR!

With their roars, an unseen dam broke.

The beasts that had been waiting for their master’s command became a wave and swept across the vast grassland.

Rumble, rumble, rumble!

Thud, thud, thud!

Beneath the blazing sunlight, the earth shook and the wind scattered.

And at the very front of it all was one man.

“Let’s go.”

The quiet words slipped between his lips.

At the same time, the guardian spirit powerfully kicked off the ground.

Whooosh!

The Great War that would decide Nanman’s fate had begun.
## Chapter artifact 696

# Chapter 696

Rumble, rumble, rumble!

Buildings shook, and the earth trembled.

The silence surrounding the Nanman Beast Palace had long since been shattered.

The tribespeople of the Outer Palace, who had locked their doors and hidden inside their homes, pulled their young children into their arms. Warriors who had been spending their shifts listlessly atop the watchtowers scattered throughout the palace happened to turn their heads—and their eyes widened.

“W-what is that…?”

GRAAAAAAAWR!

A tremendous roar that shook Heaven and Earth swallowed the dazed voice that had slipped between someone’s lips.

One of the warriors who came to his senses belatedly shouted as though screaming.

“Th-the enemy!”

But most of the warriors did not move even at those words. No—they could not move.

How could they?

They could only stand there with their mouths hanging open, staring at the army of beasts racing across the dozen or so broad roads running through the Outer Palace.

*Th-this can’t be.*

It was a sight so wondrous that it was terrifying.

Thousands—tens of thousands—of beasts were racing as one.

No one present had ever witnessed anything like it.

Not even the oldest elder in the land. Probably not even his grandfather.

It was a calamity.

Or perhaps a miracle.

Faced with something incomprehensible, something beyond the realm of understanding, every one of them—ordinary warriors all—stiffened like stone statues.

Even the shout of their superior, who was the first to recover, merely scattered around their ears like an echo drifting from far away.

“Sound the alarm! Sound the alarm bell! We have to inform the Inner Palace immediately!”

“Ah… ah…”

“You idiots!”

The enraged superior shoved aside his dazed subordinate. Then, just as he reached for the rope connected to the alarm bell, he realized that the sunlight that had been beating down fiercely only moments ago had vanished.

Whoooooosh.

Dark clouds?

No. At least, the dark clouds he knew did not move this quickly, nor did they hang so low.

At last, he recognized the identity of the dark cloud drawing nearer amid the strange sound reaching his ears, and he involuntarily spat out a curse filled with shock.

“…Goddamn it.”

At that moment—

The dark cloud—or rather, countless flying beasts that had flown in and dyed a section of the vast sky black—descended upon him.

Whoooooosh!

Flap, flap, flap!

He could not determine either their kinds or their number. Sharp cries, flashing beaks, and scattering feathers filled every direction.

The flying beasts, transformed into one enormous monster, swept through five watchtowers like a storm.

No—they smashed them apart.

CRACK! CREEEAK!

“The watchtower’s collapsing!”

“AAAAARGH!”

The flying beasts that had charged in as one were no different from a living battering ram.

As the world slowly tilted and a sensation of floating lifted their bodies, the warriors fell to the ground together with the shattered remains of the watchtower.

Rumble, rumble, rumble! Daaang!

The alarm bell, nearly as large as a grown man, tumbled across the ground first. The warriors who twisted their bodies in midair landed awkwardly after it.

Then, as they panted and raised their heads, a vast shadow fell over them.

“Where is Baeksang?”

“……!”

The quiet voice bored into their ears. Yet everyone there felt a chill that seemed to freeze their hearts.

Was it because of the enormous White Tiger, so massive that merely looking at it made their knees go weak?

Or because of the countless beasts behind it?

No. The sensation emanating from the White Tiger was strangely warm and mysterious, while the eyes of the beasts confronting them at close range were gentle.

What froze them was the gaze of the man sitting atop the White Tiger’s back and looking down at them.

A tall, perfectly balanced physique. Hair tousled without care. Exotic features that extended boldly and cleanly, unlike those of the other Nanman people.

And…

A single pure-white spear held in his hand.

“Jin Taekyung!”

As someone shouted his name like a scream, the warriors instinctively reached for the weapons at their waists.

More precisely, they tried to draw them.

At least, they did until Jin Taekyung opened his mouth.

“If you draw those, you’re not going to like what happens.”

“……!”

“And if you’ve got eyes, look around you. Who else is here besides me?”

Jin Taekyung was the monster blamed for throwing all of Nanman into an uproar. Since he had appeared with an enormous number of beasts, they had thought there could be nothing left to surprise them.

But when the warriors recognized another person’s face, they could not help opening their eyes wide.

Step.

Another White Tiger, relatively smaller in size, took a step toward them.

A beautiful woman whose exhaustion could not conceal her beauty was riding on its back.

“Su-surely not…”

“Great Chieftain Yohi?”

Yohi. A clear voice flowed from between her red lips.

“Do you recognize me?”

How could they not? Whenever the Tribal Grand Council was held once a year, the streets became packed with people hoping to catch a glimpse of her as she appeared before the public.

But more than anything, what confused them was that she—rumored to have died after the incident at the Western Yao Estate several days ago—was standing beside Jin Taekyung without fear or restraints.

And she was at the very front, leading an immeasurable number of beasts.

“G-Great Chieftain. Why are you with a monster like him…?”

“A monster…”

Yohi muttered quietly and turned her head to look at Jin Taekyung, but Jin Taekyung was not looking at her.

He was staring at the end of the broad road, where an ominous feeling lingered—the enormous iron gate dividing the Outer Palace from the Inner Palace.

Then he suddenly spoke.

“There he comes—the monster.”

And the next moment—

Rumble, rumble, rumble.

The iron gate began to open with a heavy grinding sound. Along with the countless arrowheads appearing atop the stone walls of the Inner Palace, which had been built high overhead.

Click, click, click!

The arrowheads flashed in the sunlight.

With bowstrings pulled taut and breath held tight, nearly a thousand archers aimed down at them from atop the stone walls. Then, at last, the silhouette of one person hidden behind the iron gate came into view.

Step.

His footsteps rang out with unusual clarity.

The hem of his spotless white robes brushed the ground, and his calm gaze crossed the space to meet the eyes of one man.

“You came. In the end, you did.”

Baeksang.

His voice carried powerful internal energy. Jin Taekyung lowered the spearhead and answered.

“Yes. I came.”

*You fucking bastard.*

* * *

Baeksang.

The moment I saw his face, I felt the internal energy throughout my body boiling like lava.

I wanted to charge out immediately.

I wanted to kick off the guardian spirit’s back, race toward him like the wind, and end his life with the fastest, strongest strike I could manage.

But…

Slick.

A slender finger caught hold of my sleeve. Yohi’s trembling voice reached my ears.

“No. Not yet.”

Yes. I knew that too.

If I cut Baeksang’s head off right now, it would be like lighting the fuse of a bomb with no time left on it.

Baeksang—he could not die like that. He had to die not as the Palace Lord of the Nanman Beast Palace, but as the traitor and usurper who had deceived all the Nanman people and joined forces with Dark Heaven.

If the Palace Lord died, a brutal battle would await us. But there would be no warriors anywhere willing to fight for a traitor.

That was the only way to reduce the number of needless sacrifices, even if only slightly. And Yohi standing beside me was the decisive card that could reveal the entire truth and prevent the battle now bearing down on us.

“Let’s go.”

At my whisper, the guardian spirit and Muyaho nodded and began to move.

A thousand arrowheads moved along with us as we advanced at a pace that was neither fast nor slow.

As though they were ready to send a rain of arrows the instant the order was given.

However, as the distance slowly narrowed, the arrowheads that had been flashing began to tremble, and the taut bowstrings slackened.

Beginning with those who recognized Yohi, a small disturbance was spreading across the stone walls of the Inner Palace.

Of course, there was one exception.

Baeksang.

Looking at his unmoving face, I opened my mouth.

“Even so, the Great Chieftain you used to share a pot with has come back alive. You should at least say hello. Don’t you think?”

My voice, charged with internal energy, spread in every direction.

As the disturbance swelled even further, Baeksang finally parted his tightly sealed lips.

“What affection is there between us that a greeting should be necessary? We were merely bound together by our respective purposes.”

“……!”

“……!”

I felt my face stiffen despite myself. Yohi had probably reacted the same way.

We were both thinking the same thing.

*Why?*

The Baeksang I knew was not like this. He was sly and cunning. One of the greatest causes of Nanman’s current chaos was his scheming, which was even more frightening than his martial arts.

And yet he had admitted it.

He had acknowledged Yohi’s existence, in front of everyone who followed him.

The hand gripping my spear shaft tightened.

Clenching my teeth, I glared at Baeksang with blazing eyes.

“What the hell is this…? What kind of bullshit are you pulling?”

“Did you think I would deny it?”

Baeksang answered my question, then suddenly turned around.

Beyond the wide-open iron gate, countless Nanman warriors forming a mountain of sabers and a forest of swords, along with the archers atop the stone walls, were staring at him with their eyes wide.

“What more needs to be said? Everything you know—and everything they will soon realize—is true.”

“……!”

“Yes. That is correct.”

Baeksang took his gaze away from the warriors following him and looked up at the sky.

The weather was clear, without a single cloud. Hot sunlight fell across his face.

“I betrayed everyone.”

His quiet voice, charged with internal energy, broke the suffocating silence that had settled over the area.

It traveled on the air, pierced through the wind, crossed the broad road running through the Outer Palace, passed over the stone walls of the Inner Palace, and reached everyone.

“I lived each day as though it were ten years. To accomplish a single purpose, I became an unforgivable turncoat, and at last I made it this far.”

Suddenly, I found it hard to breathe.

This was not a confession in which he admitted the sins he had committed and begged for forgiveness.

No. Rather…

*The relief that comes when everything is over. And despair.*

It was an emotion fundamentally different from giving up.

The Baeksang before us was merely vomiting out the emotions he had pressed down day after day for several decades.

Even after achieving the purpose he had desired for so long, he was revealing without concealment the sight of himself sinking into despair.

*No way.*

Along with a thought that flashed through my mind like lightning, the sensation of every hair on my body standing on end swept over me.

Then a scream burst from my lips.

“Everyone, fall back—!”

And the next moment—

Rumble, rumble, rumble! Flash!

Thunder that shook Heaven and Earth rang out, and dark clouds spread over everyone’s heads.

In a world where not even a single ray of sunlight could be found, someone’s voice bored into my ears.

“What a shame. It’s already too late.”
## Chapter artifact 697

# Chapter 697

“What a shame. It’s already too late.”

A languid voice slipped into my ears.

No. It wasn’t just me. Everyone here could hear that voice.

The herald announcing the arrival of something dangerously enchanting—and even more dangerous than it was enchanting.

“The Southern Heaven Demon Empress!”

I whipped my head around at the thunderous shout.

Above the heads of everyone frozen like stone statues by the unexpected situation, voluminous robes fluttered atop a pavilion that rose high toward the sky.

The catlike eyes looking down at the ground curved like half-moons.

“Oh my, who could this be?”

An unfamiliar woman’s face.

But the voice and distinctive feeling were unforgettable.

There was no doubt.

With that certainty, I spat out the words as though chewing them.

“It’s me, you fucking bitch.”

My stomach seethed with heat, as if I had swallowed lava. The fingers gripping the spear shaft tightly trembled, and my heart pounded violently against my ribs.

A tidal wave of emotion raged through me—far more fiercely than when I had faced Baeksang.

But simple hostility and anger were not the only things that had seized me.

*She’s strong.*

Had she always been this strong?

Just meeting her gaze made my heart seem to drop into my stomach.

Several months had passed since the incident in Hubei Province.

The insight I had gained during that time allowed me to glimpse a little more of my opponent’s true nature. And the Southern Heaven Demon Empress I faced again today was a monster beyond anything I had imagined.

A realm no one else here could even begin to guess at.

Yet my eyes—and my senses, honed to their sharpest—were tracing the power she concealed.

The ferocity hidden behind those gently curved eyes.

The enormous darkness coiled within that slender frame.

“You fucking bitch.”

“Ahaha! Just as I expected. Just as I expected!”

Whatever she found so funny, the Southern Heaven Demon Empress clutched her stomach and laughed even after being cursed at. Then she curled up the corners of her mouth at me.

“You’re so refreshingly straightforward. That’s what I like about you, Benefactor.”

“What did you say?”

“Have you forgotten already? On that cold Dongting Lake, where corpses floated on the water, who was it that saved me?”

“……!”

As if I could forget.

I had regretted that moment countless times afterward.

Was it because I had saved the Southern Heaven Demon Empress with my own hands?

No.

The person I had saved that day had not been the Southern Heaven Demon Empress, but Honglan.

The Southern Heaven Demon Empress in Hubei had been nothing more than a beautiful singing courtesan favored by some idiot of the Huang tribe.

She had deliberately approached me from beginning to end, and even if I had not come, she would have survived.

There was only one thing I truly regretted.

My stupidity in failing to recognize the culprit even when she had been standing right in front of me.

My anger at myself for failing to realize I had been toyed with for someone else’s amusement.

And my guilt at failing to prevent an even greater sacrifice.

Rustle.

“At last, I can greet you properly.”

Lifting the voluminous hem of her robes, Honglan—or rather, the Southern Heaven Demon Empress—gracefully lowered her head.

“This lowly woman, Honglan, greets her Benefactor.”

At that moment, I thrust out one palm like a flash of lightning.

Fwoosh!

Moisture evaporated in an instant.

The force of the Flame Divine Palm, carrying horrific heat, reached the Southern Heaven Demon Empress in less than a heartbeat.

But—

Slice!

The powerful palm force, which even Baeksang could not have blocked easily, was split cleanly in two like tofu in even less time.

Boom!

Beneath the sky now covered by dark clouds, the divided palm force ricocheted off in opposite directions before exploding in midair.

Shocked voices rose from every direction at the unbelievable scene unfolding before them.

“W-what is this?”

“W-what did I just see? That woman just—”

“The Southern Heaven Demon Empress. She definitely said the Southern Heaven Demon Empress.”

Some people here knew that title. Others did not.

But that fact did not matter.

Before long, everyone would learn.

Who the Southern Heaven Demon Empress was.

How vicious she was, and what kind of terrifying power the monster concealed.

I stared coldly at the edge of the pavilion rising high above us.

A woman was standing there, straightening her disheveled court robes. She was far too beautiful to be called a monster.

“Hm. I did try to show some courtesy, but I can’t say I’m especially pleased with the way you answered my greeting. Still, I’ll let it pass out of my generous nature. I can’t gouge out my Benefactor’s eyes right away when I owe him a life-saving debt.”

I could feel the killing intent contained in her innocent voice.

Rather than being shaken, I grew calmer and answered.

“Shut your damn mouth.”

“What rough language. That word is only used for beasts. For example…”

Her voice trailed off as the Southern Heaven Demon Empress’s gaze shifted slightly downward.

At the end of that gaze was an enormous White Tiger baring its teeth.

“Yes. It’s a word that suits that hideous beast perfectly.”

Grrrrr.

The guardian spirit growled low and glared at the Southern Heaven Demon Empress. I could feel its muscles tense as it prepared itself.

—A hideous beast, is it? Then what should a human like you be called?

If the guardian spirit’s thoughts had followed the same pattern as Sound Transmission until now, this was different.

Its voice was like something everyone could hear.

As countless warriors surrounding the Inner Palace inside and out drew in sharp breaths, the Southern Heaven Demon Empress opened her eyes wide. Then she let out a quiet laugh and looked at me.

“I’ll have to correct myself. Not only a hideous beast, but an interesting one as well.”

“I doubt it.”

I tightened my grip on the spear shaft and opened my mouth.

Even now, dozens of movements and forms flashed through my mind.

Ways to cut off my opponent’s breath with the fastest, most lethal strike.

“You’ll find it even more interesting in a moment. This one’s going to bite through the back of your neck.”

“A beast is still a beast. The same was true of a certain foolish imugi that waited for Heaven’s call.”

—He was not foolish. He was merely kind. Kind enough to sacrifice even his life, along with the cultivation he had built over hundreds of years.

The guardian spirit stared at the Southern Heaven Demon Empress with its blue-white eyes, its gaze seeming to pierce through everything.

—I know you.

A faint smile appeared around the Southern Heaven Demon Empress’s lips.

“That isn’t particularly welcome news. I have no interest in some musk-reeking beast.”

—I saw you in the imugi’s memories. The form of a human who was endlessly dark and filled with malice.

“Memories?”

—Everything that makes up the world possesses an essence and traces. And in that sense, you in its memories were…

“Beautiful, I suppose. Dazzlingly so.”

—Old and hideous. So much so that it was hard to believe you were human.

“……!”

—That is your essence. You have denied and hated your true form, eking out a long existence. You are no different from a Fiend.

The moment the guardian spirit’s thoughts ended, silence descended.

The people who had been murmuring from shock, as well as the countless beasts that had been making low growls, held their breath and lowered their bodies.

And at the center of it all stood one person.

Fwoooooosh!

The sleeves of the voluminous court robes swelled as though they might burst.

A terrifyingly immense wave of qi pressed down in every direction with the weight of a mountain, making every living thing freeze in place.

Crack. Crack.

The wind stopped.

The roof of the pavilion, unable to withstand the tremendous pressure, began to collapse.

“…Is that so?”

The smile had vanished from her lips as though it had been washed away.

Her deeply sunken eyes looked down upon the world spread out beneath her feet.

“Old and hideous. Yes. So that’s how it is.”

The Southern Heaven Demon Empress muttered calmly, then suddenly turned her head and stared at me.

“I’ll praise you for making it this far. If you had been even a day—or no, half a day—earlier, even I couldn’t have guaranteed the outcome.”

She was different.

Her way of speaking. Her atmosphere.

Yet my mind grew calmer instead.

People were frightening when they did not reveal their true nature. When they lost the smile and composure they had maintained until the very end, a gap finally appeared.

*More importantly.*

I still had a hidden card.

A move I could bring into play even if the worst possible situation came crashing down before me—as long as I still had the strength to use it.

That was why I could say this.

“Hm. I’m asking because I’m genuinely curious.”

Just as I was doing now.

“How ugly is your face, really, for someone to say something like that to you?”

“……!”

“Were you a mortar in your past life?”

The next moment—

“I’ll make you regret those words.”

A cold voice shattered the brief silence, and countless dark clouds covered the sky.

And then…

Fwoooooosh!

From the enormous cliff embracing the rear of the Inner Palace, a mass of pitch-black radiance began to pour forth.

*That’s…*

It was a strange sight that made it difficult to breathe just by looking at it.

Yes.

It was a *rift*.

* * *

Rumble, rumble, rumble!

The earth trembled.

The world shook.

The enormous cliff that had stood in that place for hundreds—no, perhaps thousands—of years began to split apart with a tremendous roar.

“Ah. Ahhh…”

At the strange and terrifying sight, someone let out a shocked groan.

*So it has come to this. At long last.*

Someone else spat out a despairing mutter in the depths of their heart.

“It’s over. All of it.”

Someone who had been consumed by anger watched the scene they had created with eyes filled with rapture.

*At last. At last!*

The Southern Heaven Demon Empress trembled, having already forgotten even the anger that had seized her moments earlier.

How could she not?

This was the fruit she had harvested after enduring for so many long years.

That rift was incomparably larger and more powerful than the one in Hubei Province.

It was her own creation.

It was also the moment when the will of the omnipotent Lord of Heaven descended upon this land.

Kraaaaaaash!

A gale as sharp as a blade swept in every direction.

Through the widening gap in the cliff, an intensely dark and viscous energy began to crawl out, gnawing away at the world.

Demonic qi that would corrupt life and conquer this land!

—Krrk, krrrk!

—Kyaaaaa!

“Ghk. Guhk!”

“W-what’s happening all of a sudden—krrk!”

The rift had not even opened completely, yet its power was already spreading in every direction.

Look.

Look at that surging darkness.

At the countless beasts and humans writhing with their eyes rolled back to show their white sclera, waiting for a new change.

And soon, the change caused by the rift would begin.

*No. That’s not right.*

This was not change.

It was *evolution*.

It was the process of being reborn as more powerful and beautiful beings, as well as a blessing bestowed by the omnipotent Lord of Heaven upon lowly lifeforms.

The Southern Heaven Demon Empress’s gaze, a thick smile spreading around her lips, suddenly fell upon one person.

*Jin Taekyung.*

A young man stood tall, staring at the unbelievable, overwhelming spectacle unfolding before him.

To the Southern Heaven Demon Empress, his appearance was laughable and pitiful.

Enough to make her want to rip his throat out in one go.

*You… should never have come here.*

Muttering those words inwardly, the Southern Heaven Demon Empress launched herself toward Jin Taekyung.

No.

It was at the very moment she was about to launch herself that—

Fwoooooosh!

A tremendous radiance burst from somewhere and swallowed the darkness.
## Chapter artifact 698

# Chapter 698

*What is that?*

Along with the single question filling her mind, the Southern Heaven Demon Empress’s eyes widened.

Light.

It was larger and brighter than anything she had ever seen.

A tremendous radiance that had erupted without warning swelled as though it might burst, swallowing the approaching darkness as it seeped into the world.

Kwooooooo!

A pillar of light shot toward the distant sky and pierced the heavens. Sunlight poured through a gap in the dark clouds.

The darkness that had surged over the stone walls like a wave faltered the moment it touched the radiance, as though something had blocked its path.

*It was blocked? Even the demonic qi summoned from the rift?*

It was an unbelievable phenomenon.

The demonic qi of the rift was enormously powerful—the pure force of darkness. Even the imugi, which had cultivated for hundreds of years, had been corrupted because it could not withstand that power in its entirety.

And yet the scene unfolding before the Southern Heaven Demon Empress’s eyes was undeniably real.

The dark clouds slowly scattering.

The wave of darkness blocked by the radiance and unable to advance any farther.

And then—

“Wow. This really works.”

“……!”

Jin Taekyung stood tall at the center of the radiance, grinning as he looked at her.

The Southern Heaven Demon Empress clenched her teeth.

“How… How in the world?”

Before she could finish, Jin Taekyung shrugged.

“It’s nothing special. Everyone has at least one divine artifact stashed away, right? Don’t they?”

“……!”

Divine artifact.

Those two words struck the back of the Southern Heaven Demon Empress’s head like a solid hammer.

Only then did her gaze slowly slide away from Jin Taekyung and land on another existence.

*That beast.*

A gigantic White Tiger. Like the imugi the Southern Heaven Demon Empress had corrupted in the past, it was clearly something beyond a spiritual creature. It had its jaws open as though roaring.

Through the dazzling radiance, she could faintly make out a form that glimmered with a crystalline light.

And at the same time, an ancient legend of this land flashed through her mind.

“……The Beast King Stone.”

At the voice that slipped between her pomegranate-red lips, Jin Taekyung let out a quiet laugh.

“Oh. You know it?”

How could she not?

The symbol of a king before whom every beast in the world bowed and submitted. A sacred treasure of Nanman that had vanished over the course of several hundred years.

No. It was impossible for her not to know.

The Southern Heaven Demon Empress was the one who had searched every inch of this rugged land of Nanman for the Beast King Stone.

For more than ten years.

Yet even after enough time had passed for mountains and rivers to change, she had failed to find so much as the slightest trace of the Beast King Stone itself. In the end, she had left the ancient legend behind and begun her grand plan.

But why?

Why now?

“You bastaaaaards!”

Whoooooosh! Crack!

A terrifyingly immense surge of qi rose and pressed down on everything around it.

The countless beasts that had been baring their teeth and growling tucked their tails between their legs. The pavilions filling the area began to collapse as though they had been crushed beneath a giant’s foot.

Tribespeople fleeing the Outer Palace in terror discovered the existence standing tall in the air and gaped at it.

“A-Ah……!”

Darkness.

A woman with deep, surging darkness wrapped around her entire body looked down upon the ground.

Like a god—or a Fiend out of legend—she was gauging how much longer they had to live.

But unlike everyone else, the Southern Heaven Demon Empress’s gaze was fixed on only one place.

“Hand it over.”

Rumble.

The dark clouds filling the sky let out a tremendous cry.

In a world where light and darkness coexisted, a chilling voice rang out and pierced everyone’s ears.

“It is something the Lord of Heaven must rightfully take. It is not an object that insignificant beings like you are fit to possess.”

Beast and human alike.

Everyone froze before that overwhelming power and terror. They forgot how to scream and how to run, staring blankly at the figure in the air.

Everyone except two people.

No—two beings.

“Bullshit, you crazy bitch.”

—How dare a mere human covet the sacred stone?

Jin Taekyung and the guardian spirit stared at the Southern Heaven Demon Empress standing tall in the air.

Rumble, rumble, rumble!

They could feel it.

The unprecedented power crouching within that small body.

The weight of the qi pressing down around them surpassed that of any human the guardian spirit had encountered over the past several hundred years. It surpassed even the Western Heaven Demon Lord, whom Jin Taekyung had fought in the past while narrowly escaping death time and again.

*Strong.*

And frightening.

It was an emotion every living creature felt.

But feeling fear and being seized by fear were fundamentally different things.

They knew that even now, they had to endure the fear pressing down on their entire bodies and advance. Only then could they win.

—Much blood will flow, human.

“Fuck. If I survive this, I won’t even take a piss toward Nanman again.”

Jin Taekyung muttered the words through clenched teeth and gripped White Flame’s spear shaft tightly.

Then he spoke quietly to Yohi, who was frozen behind him.

“You know what to do, right?”

“……!”

“Get the people out of here right now. With everything you’ve got. As far away as possible.”

Even beyond the people currently within sight, countless tribespeople lived in the Outer Palace.

Jin Taekyung wanted to avoid drawing their figures into the horrific hellscape that would soon unfold here.

Only the powerful needed to bleed. The tribespeople, who had neither weapons nor sharp teeth, had to survive.

Even if the Southern Heaven Demon Empress killed everyone here.

*But… I’ll stop her. We’ll stop her.*

The demonic qi flowing from the rift was currently blocked by the power of the sacred stone.

He did not know how long this tense standoff would last, but before the situation grew any worse, they had to defeat the Southern Heaven Demon Empress and close the rift.

*No matter what it takes.*

Whoosh.

Jin Taekyung took a deep breath and glared at the existence standing high in the distant sky above the ruins of the collapsed pavilions.

The Southern Heaven Demon Empress.

The beginning and end of everything that had happened in this land.

Someone had to fall before they could see the conclusion of this cruel story.

“Let’s go.”

The low voice had just slipped between his lips when—

—Kraaaaaaang!

A fierce roar tore through the wind.

The radiance that had gradually faded after colliding with the darkness swelled, awakening the minds of the terrified beasts and humans.

Fwoosh! Kwoooooosh!

Light burst forth alongside the roar.

And flames rose around the silver spearhead.

An outsider who had come to this land after several hundred years surged upward as one with the enormous White Tiger.

Bang!

He kicked off the ground.

Pop!

He stepped on the invisible air and wind.

Whoooooosh!

Toward the darkness spread across the distant sky.

No.

Toward the existence that had grown even more powerful by receiving the darkness.

“Southern Heaven Demon Empress!”

The flame-wreathed azure dragon’s roar flew in with the spearhead, cleaving through space.

A chilling look crossed the woman’s face, now twisted like a Fiend’s, with not a trace of beauty left.

“The Lord of Heaven desires it.”

At that moment—

Flash!

The muddled mixture of light and darkness dyed the Nanman Beast Palace.

* * *

Groooooooan.

A tremendous wave of qi swept in every direction amid a deafening roar that seemed to split the sky.

Baeksang instinctively closed his eyes against the blinding flash that erupted in an instant. Feeling the gale pushing against his entire body, he swallowed a low groan.

*Hngh.*

What kind of overwhelming power was this?

Even he, a Supreme Peak master, could barely keep his balance against the aftershock.

When he finally opened his eyes, the area around him had already been reduced to ruins. The tribespeople who had barely survived thanks to the protection of the beasts were fleeing while screaming.

“Kyaaaaaa!”

“Hoya! Hoya! Where are you?”

“M-Mother!”

The pavilions and houses built over many long years collapsed one after another.

A grown son wailed as he saw his old mother pinned beneath a fallen stone wall.

Screams and death.

Blood and corpses.

The streets that had been filled with laughter and music only a few days ago could no longer be found anywhere.

Only endless roars and screams spilled out from every direction.

Bang! Kwoooooang!

In the space of an instant, light and darkness shot ceaselessly toward each other and tangled together.

Baeksang stared blankly at the hellscape spread beneath the muddled flashes and the deafening roars that seemed to split the sky.

Then, all at once, he stretched out a hand toward one direction.

Boom!

The palm force he released across space knocked away a massive boulder.

A half-gray-haired middle-aged man who had been struggling to save an old woman trapped beneath the stone wall widened his eyes.

“You… You’re…….”

Perhaps they had met somewhere before. The face seemed strangely familiar.

Baeksang silently watched as the middle-aged man supported the old woman, anger and gratitude mingling on the man’s face.

Then, the moment he saw the old woman’s revealed face, he understood.

*He resembles her. Very much.*

It was her.

The old palace attendant he had personally ordered expelled from the Inner Palace before everything had begun.

One of the few people who still knew what he had once been was now bleeding and groaning.

“Cough. Mmm…….”

“M-Mother!”

*Did she have a child?*

Baeksang watched the middle-aged man hurriedly check the old woman’s condition, then suddenly began to walk.

He did not know why.

He had simply felt that he had to.

“D-Don’t come any closer!”

A cry filled with hostility.

Even if they shut the doors and locked them, their ears were still open.

By now, everyone in the Nanman Beast Palace knew.

Their Palace Lord—the Great Chieftain of the Bai people—had betrayed them all.

They knew that Baeksang was the cause of the screams and deaths that continued even at this very moment.

The middle-aged man before him was one of them.

To protect his old mother, he had stepped in front of Baeksang. In his hand was a sharp fragment of stone he had picked up at some point.

“If you take even one more step…….”

Swish! Crack!

The stone fragment pierced by Finger Qi crumbled apart.

Baeksang passed the frozen middle-aged man and reached toward the old woman.

Tap. Tap.

The blurred hand moved like lightning, touching the old woman’s acupoints.

At the same time, the wrinkles furrowed across her brow slowly smoothed out.

“Cough.”

After she spat out the stagnant blood, the old woman looked much more at ease.

The middle-aged man hurriedly checked his mother’s condition, then looked at Baeksang with an expression of incomprehension.

“W-Why?”

Why?

Even that simple question was something Baeksang could not answer.

Perhaps he would still be unable to answer it even ten years or a hundred years from now.

He did not know the answer himself.

In the end, the single sentence that broke his brief silence was not an answer to the question.

“Leave with the others. Go as far away as possible.”

“S-Sir!”

“Do you intend to let your mother die like this? Or…….”

Baeksang’s eyes sank deeply.

“Do you intend to make your mother watch you die?”

“……!”

“Go. If you head for the East Gate, a way out will open.”

With those words, Baeksang turned away.

The middle-aged man’s hoarse voice escaped belatedly and pierced his ears.

“Do you think this will… Do you think this will make the sins you committed forgivable!”

At the angry shout, Baeksang answered inwardly.

No.

He had never once thought he would be forgiven.

Rumble, rumble!

A deafening roar descended behind him as he headed toward the Inner Palace.

But his figure streaked away without even a trace of hesitation.

It was time to face the moment he had pictured for decades.
## Chapter artifact 699

# Chapter 699

Rumble! Crash!

Unable to withstand the fierce vibrations, the stone walls of the Inner Palace crumbled helplessly, and the iron gate that had broken free slammed into the ground with a heavy roar.

It looked as though a small hill had collapsed.

But Baeksang’s figure slipped past the falling debris and shot forward at tremendous speed.

Whoooosh!

Wind brushed across his entire body. His sharpened senses caught the metallic scent of blood and the screams echoing from every direction.

Feeling the internal energy churning inside him, Baeksang took a deep breath.

*I must not be swept away.*

A massive cliff stood tall behind the Inner Palace like a folding screen.

The demonic qi flowing from the gap in that cliff—a gap that now had to be called a rift—was not something even Baeksang could take lightly.

No. It was precisely because he was a Supreme Peak master that he could move freely through the Inner Palace.

Unless one walked the Demonic Path, even a fairly skilled internal-energy master would have had his internal energy thrown into disarray and lost his composure the moment he entered the demonic qi’s domain.

Just like the middle-aged man now staggering into his path to block him.

“P-Palace Lord? Is that you, Palace Lord?”

It was a face he could never mistake.

A man as greedy as his father, who had inherited the position of tribal chieftain without possessing any particular ability and had lived in comfort and luxury.

That was why he had supported Baeksang more enthusiastically than anyone else.

But the man who had always offered Baeksang oily smiles filled with flattery was now crying out with blood pouring from his seven apertures.

“Please, please save me! I don’t want to die ye—!”

The hand he thrust out desperately brushed against Baeksang’s snow-white collar.

Baeksang quietly looked down at the fallen tribal chieftain, who had lost his balance, and opened his mouth.

“Why should I?”

“P-Palace Lord?”

“You must have known already. That what I intended to do would bring great harm to Nanman.”

“……!”

“We exchanged fair payment for the sake of our respective goals, so please do not consider yourself wronged.”

*I will do the same.*

Along with the words that never escaped his lips, Finger Qi shot from Baeksang’s fingertips.

Puhk!

The tribal chieftain collapsed as the attack pierced the crown of his skull.

His eyes were wide with disbelief. Even in death, his gaze seemed to ask Baeksang a question.

*Why? How could you?*

*How can you still stand so proudly even in the face of this hellscape?*

And Baeksang answered the dead man’s question in his heart.

*Because I had already made up my mind.*

Even so, the breath escaping between his lips trembled.

If that man had begged him to save the tribespeople instead of his own life, would Baeksang have saved them?

No. Perhaps meeting such a peaceful death was actually an act of mercy for a man with such poor martial arts.

Ten thousand.

A full ten thousand. So many warriors and beasts were bleeding and writhing as they were swallowed by the demonic qi.

Their screams seemed to squeeze his heart and claw through his mind like blades.

But Baeksang did not stop walking.

Whoooosh!

His figure shot forward without hesitation and crossed the vast training ground blanketed in screams.

The stable where he and Yayul Cheok had hidden whenever they got into trouble as children, and the storehouse they had entered to steal fruit wine, both slipped past like gusts of wind.

Vengeance. Rage. Regret.

The emotions that had piled up layer after layer with every step whipped around him.

*If only I had not taken my only son to the battlefield. If only I had drawn my sword instead of clasping hands with the Southern Heaven Demon Empress on the day she came.*

*If only I had told the one sworn elder brother who trusted me more than anyone—even more than Baeksang himself—the whole truth.*

*Or perhaps……*

*If only I had carried everything alone and taken my own life.*

Step.

At some point, the footsteps that had advanced without pause came to a stop.

His eyes, fixed on the tightly closed door, had long since become bloodshot.

At that moment, the voice of the Southern Heaven Demon Empress from the previous night echoed through Baeksang’s mind.

“*Noon. Tomorrow at noon. Gather every warrior in the palace in the Inner Palace.*”

“*Tomorrow…… at noon?*”

“*Yes. That is as far as your role extends. After that, we will take care of the rest……*”

“*Our promise.*”

“*Hm?*”

“*Please keep our promise. The promise you made to me long ago.*”

“*You’re rather impudent, aren’t you? You even dare interrupt an adult while she’s speaking.*”

The Southern Heaven Demon Empress had laughed, and Baeksang had knelt without a moment’s hesitation.

Only after watching the new lord of the Nanman Beast Palace repeatedly strike his head against the floor for quite some time did she finally give him the answer he had so desperately wanted.

“*A polite child deserves a reward, doesn’t he? Fine. Once the grand plan begins, return to your office.*”

“*……My office?*”

“*Yes, this very place. The promise I made will be fulfilled then.*”

Her laughter-filled voice scattered beside his ears.

Baeksang’s only hand trembled as he slowly—so very slowly—reached toward the door.

He had never wondered *How?*

If the Southern Heaven Demon Empress and Dark Heaven said it was so, then it was so.

Considering the supernatural powers they had displayed until now, there was even less reason to doubt it.

No matter how many eyes had been placed throughout the Inner Palace, the promise would be kept.

*At last.*

He had finally reached this place.

When he gently closed his eyes, waves of distant memories surged over him and swallowed his body and mind.

Long years of suffering.

But even this lonely story had a final chapter.

As though awakening from sleep, Baeksang opened his eyes and pushed the door open with all his strength.

Creak.

The door swung wide.

At the same time, the spacious office came into view.

Simple, crude furnishings that still held the warmth of their former owner. A table that had preserved the traces of many long years.

And, entirely out of place in such an office, a large mirror occupying one corner.

And then. And then……

That was all.

*It’s gone. There’s nothing.*

The unbelievable reality became a rock weighing ten thousand measures and crushed one man beneath it.

Baeksang stared at the office with hollow, empty eyes, then suddenly let out a hollow laugh.

“Heh. Heh heh. Heh heh heh.”

He laughed because he could not cry, and he laughed because he had no choice but to laugh.

The Southern Heaven Demon Empress had not kept her promise.

Decades of time. Everything he had done during that time.

All of it turned to ash and scattered in the wind.

In the end, everything had ended like this.

“Ha-ha-ha-ha-ha!”

Baeksang burst into uproarious laughter.

As though he had returned to his boyhood, he clutched his stomach, rolled across the floor, and laughed with tears streaming down his face.

No.

He was crying.

“Ha—ha-ha! Aaaaaah!”

A scream burst out instead of laughter.

Baeksang struck the floor and walls with a fist that held not even a trace of internal energy.

Bang! Bang! Krrr-boom!

His fist shot out without pause.

The office was not the only thing shattered by the thunderous impacts.

The callused back of his hand split open, and white bone showed faintly through the blood covering his fist.

*It hurts.*

More than ever before.

Drip. Drip-drip.

Drops of blood fell and pooled in the spiderweb cracks spreading across the floor.

Baeksang staggered to his feet and approached the window.

Unlike him, who thought the world had stopped, everything beyond the wide-open window was still turning rapidly at that very moment.

“Graaah!”

“P-Please, just kill me……!”

—Grrk, grrrk!

Humans and beasts struggled as they resisted the demonic qi devouring their bodies and minds.

And large and small shadows raced toward them as they released horrifying screams.

Thud-thud-thud-thud!

Countless beasts thundered across the ground, climbed over the collapsed stone walls, and descended upon them.

But their purpose was not slaughter.

It was rescue.

—Graaaar!

With the roar of a familiar White Tiger at the head of the group, the beasts moved in perfect formation. They bit the arms, legs, or scruffs of the nearest people and beasts, then raced toward the Outer Palace.

To escape this terrible demonic qi.

To guide them toward the light, even if only one step farther.

Crkk.

Baeksang clenched his fist tightly.

Blood welled at the tips of his nails as they dug deep into his flesh.

He raised his head and stared into the distance.

At the end of his gaze, light and darkness continued to twist together without pause.

Rumble!

He could feel it.

The waves of an unimaginably immense power.

And, each time the clashes continued, the light gradually fading—and the figure of one person continuing to fall.

Boom! Crack!

A figure was blasted away with a deafening roar and plunged toward the ground like a meteor.

Two pavilions collapsed, and the earth trembled.

But only for a moment.

Blue flames stepped on empty air and shot toward the thick darkness.

Without resting for even a single moment.

As though it intended to burn away even the death that would soon arrive.

*Jin Taekyung.*

*Why are you going this far? Why?*

The question that could not escape lingered inside his mouth.

A single sentence he had heard in a corner of a dark underground prison in the recent past echoed beside Baeksang’s ears.

“*How much more blood are you planning to spill, Baeksang?*”

Baeksang stared blankly out the window and finally gave his answer.

“I don’t know. I don’t either.”

It was a secret he had been unable to tell anyone.

After losing his son, he had dreamed of revenge.

After meeting the Southern Heaven Demon Empress, he had seen hope.

Then, at some point, he had discovered himself standing on the other side of a river he could never cross back over, and despaired.

And…… at the end of the thorny path he had walked, he had come face-to-face with an empty nothingness.

Step.

Baeksang staggered backward from the window.

He could no longer bear to watch the hellscape he had drawn with his own hands—or the young outsider who was trying to stop its completion with his life.

*What had it all been for?*

Along with a question he would never find an answer to, Baeksang turned his head away from the window.

His entire body suddenly stiffened like a statue.

“……!”

A blood- and dust-covered person stood where his gaze had stopped, looking back at him.

A man who had lost everything and become an empty shell.

An old man who had merely suppressed the years with his formidable martial arts and survived as a monster.

The large mirror occupying one corner of the office reflected his figure.

But that was not all Baeksang saw.

“Ah.”

*Hwi.*

With a call that could never reach its destination, he extended his hand.

No—he tried to extend it.

At least, until the surface of the transparent, smooth mirror began to ripple like water.

Ssssrrrk.

At that moment, Baeksang finally understood.

Who had given him this mirror.

Why the Southern Heaven Demon Empress had said the promise would be fulfilled here.

*It wasn’t a lie.*

In the heart that had gone cold, the ember of hope he had thought extinguished began to burn once more.

And in Baeksang’s trembling eyes, the mirror, now stained with murky darkness, turned black and spat out a shadowy human figure.

Along with a cold sword blade imbued with Force.

Puhk!

* * *

Flash.

The Southern Heaven Demon Empress thrust out her foot.

It was smaller than a boy’s palm.

But the moment it touched the side of the spearhead, a force more powerful than that of a giant surged through my entire body.

Crack—bang!

—Human!

Hearing the guardian spirit’s cry, I plummeted to the ground and was driven deep into the earth.

The impact traveled through my back, forcing my lips open.

Cough.

A line of red blood ran from the corner of my mouth.

I had already suffered no small amount of Internal Injury, and the cracked bones complained with pain, creaking whenever I moved.

*Monster.*

The Southern Heaven Demon Empress was one of the greatest fucking bitches in history, but she was also one of the greatest monsters in history.

A monster with martial arts more formidable than anyone I had faced until now—even the Western Heaven Demon Lord.

But……

*I have to get up. No matter how many times.*

Even if it was not a few times but dozens of times, it made no difference.

There was nowhere left to retreat.

If I took even one step backward, that place would become hell.

Not only me, but every living thing in Nanman—and even the Central Plains—would inevitably be swallowed by the flames.

*I have to stop her.*

I wiped the blood from the corner of my mouth with my sleeve and stood.

And before I could even summon my internal energy again, I realized that the situation I was in still did not qualify as the worst.

Rumble, rumble, rumble!

I instinctively turned my head.

And I saw it.

“……For fuck’s sake.”

Darkness descending thickly over the collapsing Inner Palace.

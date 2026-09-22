# Checkpoint Review — 720–724

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

# Chapters 720–724

## Plot

The Corrupted Divine Artifact is purified in the Sacred Land’s Pond of Life, becoming a new sacred stone. The pond’s remaining life energy falls as Sacred Rain across Nanman, healing the wounded, restoring the land, and revitalizing its people before the pond dries up. Muyaho becomes guardian of the sacred stone.

Jin Taekyung turns the miracle into a religious and political revolution by proclaiming the Earth Mother Goddess Nanman’s sole supreme deity and appointing the Beast Miao King as her priest. The Tribal Grand Council adopts the new faith, traitorous chieftains are executed, and the thirty-two tribes unite. Nanman abolishes the Great Chieftain system, places authority solely with the Palace Lord, and retains the council for emergencies. Yohi is pardoned for helping evacuate the Outer Palace.

Yayul Mok completes the Mother Goddess Scripture, which records Nanman’s history and names Jin an Apostle of the Earth Mother Goddess, triggering his Religious Reformation achievement. Nanman formally joins the Murim Alliance and pledges its forces against Dark Heaven. As the Sacred Rain fades, the Beast Miao King memorializes Baeksang, sounds the war drums, and begins mobilizing Nanman’s people and beasts for the Great War.

While departing with his companions, Jin reflects on Nanman’s recovery and the danger posed by Dark Heaven’s unrevealed strength. He grows suspicious of the Lord of Heaven’s personal interest in him, then receives Jeok Cheongang’s request for a private conversation.

## Continuity

- The former Corrupted Divine Artifact was purified and transformed into a new sacred stone.
- Muyaho guards the new sacred stone in the Sacred Land.
- The Pond of Life dried up after releasing its remaining power as Sacred Rain.
- Sacred Rain healed injuries and fatigue, restored Nanman’s land, and temporarily enhanced its people; its effects are fading.
- The Earth Mother Goddess is now Nanman’s sole publicly recognized deity.
- The Beast Miao King is both Nanman’s Palace Lord and the goddess’s sole priest.
- The Great Chieftain system has been abolished; the Palace Lord holds central authority, while the Tribal Grand Council remains for crises.
- Yohi was pardoned after helping evacuate Outer Palace residents.
- The Mother Goddess Scripture has been written, and Jin, Jeok Cheongang, the Fire Dragon Pavilion members, and Namho are recorded as apostles.
- Jin received the Title Apostle of the Earth Mother Goddess and completed the Religious Reformation achievement.
- Nanman’s thirty-two tribes are united and the Nanman Beast Palace has formally joined the Murim Alliance.
- Yayul Mok has committed himself to protecting Nanman and its allies.
- Nanman is mobilizing for the Great War and promises a force larger than the one it sent during the Great Faction War.
- The White Tiger is present above Nanman’s assembled forces.
- Dark Heaven’s full strength and plan remain unknown.
- The Lord of Heaven has shown unexplained personal interest in Jin.
- Jeok Cheongang has requested a private conversation with Jin during their journey.

## Translation Decisions

- Retain **Pond of Life**, **Sacred Rain**, **Corrupted Divine Artifact**, **Corrupted Sacred Stone**, **Sacred Land**, and **new sacred stone** as established distinctions.
- Render **Earth Mother Goddess**, **Mother Goddess Scripture**, **Apostle of the Earth Mother Goddess**, and **Religious Reformation** consistently.
- Render **전고** as **war drums**.
- Render **신강** as **Xinjiang**.
- Retain **God wills it!** for **신께서 원하신다!**.
- Preserve **Beast Miao King**, **Palace Lord**, **Murim Alliance**, **Dark Heaven**, and **Lord of Heaven**.
- Preserve Jin Taekyung’s profane, comic narration and the established religious terminology.

## Durable state

{
  "active_continuity": [
    "Nanman is unified under the Beast Miao King's authority, with the Great Chieftain system abolished and the Nanman Beast Palace operating as a Murim Alliance ally.",
    "The Nanman Beast Palace has formally joined the Murim Alliance and pledged to send more troops against Dark Heaven than during the Great Faction War.",
    "Yayul Mok learned humanity from Jin Taekyung and is committed to defending Nanman and its allies with his life.",
    "The Sacred Rain is fading but has healed Jin Taekyung's companions from their injuries.",
    "The prelude to the Great War has begun with Nanman's beasts and people mobilizing.",
    "The White Tiger is present above Nanman's assembled forces and answers the Beast Miao King's war cry.",
    "Dark Heaven's full strength remains unrevealed despite its previous interventions.",
    "The Lord of Heaven has taken an unexplained personal interest in Jin Taekyung.",
    "Jeok Cheongang has requested a private conversation with Jin Taekyung during the journey from Nanman."
  ],
  "continuity_sources": [
    724
  ],
  "open_questions": [
    "Why is the Lord of Heaven interested in Jin Taekyung, and what does the Lord of Heaven intend?",
    "Why has Dark Heaven withheld its full strength, and what is its larger plan?",
    "How will the Great War unfold now that Nanman has joined the Murim Alliance?",
    "What will happen to Nanman and the Sacred Rain after the rain ends?"
  ],
  "safe_through": 724,
  "temporary_decisions": [
    "Render 전고 as war drums.",
    "Render 신강 as Xinjiang.",
    "Retain God wills it! for 신께서 원하신다!.",
    "Preserve the established Lord of Heaven rendering for 천주 and the chapter's profane comic banter."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 720

# Chapter 720

Whew.

I could feel a cool breeze. After taking a small, deep breath, I looked around.

The Sacred Land.

Could there be another place where those two words fit so perfectly?

But the place where I stood was merely its body.

*Even a Sacred Land like this has a separate heart.*

A place filled with the energy of life and Purification.

The very place that had already brought my dying body back to life once before.

I slowly walked toward the pond in the distance.

Although there was no sun, the light shining down from above was warm, and the flowers and grass blooming wildly in every direction were fresh and vibrant.

Jeok Cheongang and the Beast Miao King stared at the bizarre space with stunned expressions. Their lips moved as though they were about to say something, but before long, they firmly shut their mouths and followed behind me.

However, their patience didn’t last very long.

Splash.

As I stepped straight toward the pond, the cold water quickly rose to my waist. Seeing me like that, Jeok Cheongang let out an alarmed shout.

“Th-that bastard…!”

He seemed to think I was about to kill myself.

Jeok Cheongang looked ready to grab me by the collar and drag me out at any moment, but instead of explaining myself, I bit down on my pinky finger.

Crack.

The flesh split, and blood flowed with a faint sting of pain.

But after giving the wide-eyed Jeok Cheongang a crooked grin, I plunged my hand into the clear water without hesitation.

*One. Two. Three…*

I slowly counted in my head before pulling my hand out.

In barely thirty seconds, my pinky had completely healed.

Even Jeok Cheongang, who had looked ready to leap into the pond, and the Beast Miao King, who had been trying to stop him, could only mutter like they were groaning in disbelief.

“What is this?”

“……What Yohi said was true. Every word of it.”

Do you think people in olden days came up with the saying that seeing something once was better than hearing about it a hundred times for no reason?

No matter how much you talked until your mouth went dry, showing someone directly was still faster.

*It was a kind of performance.*

Fortunately, the performance had worked perfectly. At the same time, I was able to confirm one more thing.

*It still works.*

To be honest, I had been a little worried.

Just as a Golem whose core had been destroyed would collapse into pieces, I had feared that the Sacred Land might have disappeared because of the sacred stone consumed by demonic qi.

But that concern vanished as cleanly as the wound on my pinky, replaced by a suspicion bordering on certainty.

*This is it. This is the answer.*

The System had never lied to me—not even once.

It only conveyed facts exactly as they were. Finding a new path within its maddeningly plain text was entirely up to me.

Just like this time.

*The Quest information said “by some means or another.” I’m sure of it.*

That was right. From the beginning, the mission I had been given was to *dispose of* the Corrupted Divine Artifact, not to *destroy* it.

I had realized the meaning relatively late, and the memories connected to the guardian spirit had reminded me of a mysterious place.

A pond that had healed my body when I was critically injured and purified the impurities within me.

*Healing and Purification.*

I didn’t know where those mysterious effects came from, but they had to be my only option.

I stepped toward the center of the pond.

Ssssh.

Gentle ripples spread outward from me. The pond wasn’t very deep, and on its surface—clear enough to see through—I could see the face of a man stiff with tension wavering in the water.

Gulp.

After swallowing my dry saliva, I looked down at my tightly clenched fist.

Along with the solid feel of the Corrupted Divine Artifact, I could sense powerful demonic qi surging up between my fingers.

*……But if this backfires, we’re in for a total shitshow.*

I wasn’t joking. With demonic qi this powerful, it would be more than enough to wreck not only the pond but the entire Sacred Land.

Then this place would become the real, true Poisonblood Grounds, and the guardian spirit—who had only just finished filing his move-in registration in the afterlife—would show up in my dreams every night and hiss at me.

But still…

*What am I supposed to do? I don’t have any other choice.*

Fuck it. I don’t know.

I squeezed my eyes shut and plunged the Corrupted Sacred Stone in my hand straight into the water.

Splash! Fwoosh!

The calm surface scattered, and a spray of water shot up and soaked my entire body.

And then…the surroundings fell silent.

“……?”

What the hell? Why was it so quiet?

After hesitating for a moment in that brief span of time that felt like an eternity, I opened my eyes.

Just a little. Very carefully.

And at the moment I cautiously peered through narrowed eyes—

Blub blub.

Bubbles rose to the surface.

Whoooooosh.

From the center of the pond, water mixed with murky darkness began to whirl into a vortex.

Which meant…

*Fuck, so this is it?*

At the same time as that realization struck me, a gigantic pillar of water surged up from beneath my feet.

* * *

Kwaaaaaaah!

There wasn’t even time to react.

There was only water and darkness in every direction.

Caught in the chaos that had rushed upon me without warning, I thrashed about with all my strength.

No—I tried to.

That was what I would have done if I hadn’t realized the truth in the next moment.

“……!”

I saw it clearly, and I felt it.

The water and darkness swirling violently around me. The fresh air and wind that I shouldn’t have been able to feel underwater.

*Air? Wind?*

I blinked and looked around.

I no longer felt any sensation of floating beneath the surface. The water that had risen to my chest was gone as well.

There was solid ground beneath my feet, while water and darkness continued to swirl endlessly in every direction.

*It…surrounded me?*

There was no doubt. Instead of sweeping across my entire body, the enormous pillar of water had enclosed me. Beyond the darkness and waves blocking me in on every side, impossible and unbelievable scenes flashed past my eyes.

Fwoooosh!

*This is…*

I understood immediately.

What I was seeing wasn’t a hallucination caused by extreme confusion or anything of the sort. It was simply the history of some place contained within this pond.

No. It might have been the memories of the divine artifact that had shared this land’s fate since its birth.

“……Sacred stone.”

I muttered the words like a groan and gazed with stunned eyes at the column of water walling me in on every side.

Within the ceaselessly flowing water, an impossibly distant span of time was flowing as well.

On a barren land where nothing existed, a sprout pushed its way up and grew into a great tree. Once grass and flowers began to grow, animals appeared one after another.

*It’s fast.*

Within a span of time too short to even be called an instant, the scenery reflected in the waves changed without pause.

Day and night switched places dozens of times in the blink of an eye. One day, thunder and lightning filled the entire world. On another, a mountain collapsed and erased a river.

Hundreds. Perhaps thousands of years.

Yet even amid the endlessly changing flow of time, the sacred stone remained exactly where it was. There were also beings that stayed by its side.

Horses. Monkeys. Leopards. Bears…

Animals of different species and appearances. And yet, they were beings that could hardly be called animals.

Countless among them shone like stars in the night sky before fading away, and eventually, a snow-white White Tiger began guarding the sacred stone.

*The guardian spirit.*

Then darkness arrived.

A horrifying darkness that made the body shudder. A sticky, wicked energy undulated through the waves.

The memory of that day, reached after the passage of a long age.

But the final guardian spirit charged forward, its white mane flying behind it. It tore into and clawed at the darkness with a roar.

Until demonic qi seeped through the scars covering its body.

Until the moment its blue-white eyes turned black.

And then every memory contained within the sacred stone ended as well.

No. Perhaps it was a new beginning.

Ssssh.

The surface rippled once more.

The darkness vanished, and a man’s face appeared within the pillar of water coiling around me.

The figure of a young man with his eyes squeezed shut as he immersed something in his hand deep into the pond was unmistakably familiar.

A new memory of the sacred stone.

Its beginning was me, and that meant only one thing.

Ding.

Along with the clear chime that pierced my ears, the darkness writhing within the pillar of water faded away without a trace.

As I stared blankly at the sight, a translucent holographic window appeared before me.

> **System**
>
> - Pond of Life purifies all evil and impure energy.
>
> - The demonic qi that had seeped into the Corrupted Divine Artifact has completely disappeared!
>
> - Mission: Dispose of Corrupted Divine Artifact (Complete)
>
> - You have successfully completed the Quest, Corrupted Divine Artifact!
>
> - You have obtained a vast amount of EXP and Fame as a Quest completion Reward!
>
> - Level Up!
>
> - Level Up!
>
> - You have accomplished an unbelievable achievement!
>
> …
>
> …
>
> …

Ding. Ding. Ding.

System notifications rang out without pause, and holographic windows filled the air around me.

But the reason everything surrounding me felt so distant was the single object shining alone through the slowly dispersing column of water.

Ssssh.

The water parted along the path of my hand as I reached out as though entranced.

The moment my fingertips touched it—something smaller and lighter than a child’s fist, yet unbelievably warm—

Fwoooooosh!

Dazzling radiance swelled outward.

At the same time, the column of water walling me in on every side shot into the sky and burst apart like an explosion.

Fwooooooosh!

The power of life spread endlessly beyond the hidden Sacred Land, toward some faraway place.

Holding the new sacred stone in my hand, I suddenly tipped my head back and looked at the sky.

Another clear chime rang out amid the droplets falling all around me.

Ding.

> **System**
>
> - The energy contained within the Pond of Life becomes rain and seeps into every corner of this land.
>
> - The earth will become even more fertile, the plants will remain evergreen, and the wounded will be healed.
>
> - The Pond of Life has lost all its energy and dried up. But do not worry. Time possesses the power to change many things.
>
> - The Sacred Stone will continue to exist in this land, just as it has until now. Together with a new guardian spirit.

A new guardian spirit?

Before I could understand what those words meant, the sound of someone’s footsteps reached my ears.

Thud.

A large forepaw stepped onto the parched ground that could no longer be called a pond.

Snow-white fur fluttered in a breeze that had come from somewhere, and the blue-white eyes, now clearer and more distinct, looked exactly like those of someone from my memories.

“……So it’s you.”

Grrrr.

Muyaho.

No—the new guardian spirit approached and rubbed its head against me.

Without saying a word, I stroked the back of its neck. Jeok Cheongang, who had watched the entire scene with a dazed expression, barely managed to part his lips.

“……Could this old man take that one with him?”

The Beast Miao King immediately asked with a stern expression.

“Would that be possible?”

They didn’t know.

They didn’t know that a green leaf had just poked its head out beneath the rain falling on them.

Nor did they know that this rain would soak the entire land of Nanman for three days.
## Chapter artifact 721

# Chapter 721

Even now, nearly ten days after *that day*, restoration work was still underway at the Nanman Beast Palace.

The Inner Palace, which could be called its heart, had been completely devastated, and the Outer Palace had also suffered considerable damage in the aftermath of the battle.

Fortunately, by mobilizing all the warriors and beasts, they had managed to clear away most of the rubble in a short time. But considering all the houses and pavilions that still had to be built for the tribespeople who had suddenly lost their homes, the road ahead seemed endless.

“Now, let’s lift it together on three. One, two.”

“Hngh!”

Crack!

They combined their strength to lift a huge boulder, then hoisted thick timber onto bruised shoulders.

Yet despite the unending hard labor, not a single person complained as they continued working.

Because this was work for everyone's sake.

The Nanman Beast Palace was a symbol of everyone who lived on this land, a spiritual homeland passed down from their ancestors.

It no longer mattered which tribe the people working together belonged to, what they wore or ate, or which local deity they believed in.

Everyone present had come here for one goal alone: the reconstruction of the Nanman Beast Palace.

It was also the reason one middle-aged man had walked three hundred li to reach this place.

Whack!

The ax blade he swung with all his strength bounced off the thick timber. At the same time, a sharp pain traveled up through his palm.

A young man approached the middle-aged man, who had instinctively groaned.

“You’re not supposed to swing it like that. Let me see your hand for a moment.”

The middle-aged man instinctively held out his hand. He had inherited the family business and spent his entire life as a merchant, but his palms were now covered in blisters and blood.

“Ouch, that must hurt. You’ve hardly ever done this kind of work, have you?”

“I-I suppose not.”

“This isn’t something you can do just by using your strength. You have to put your weight behind the ax blade and follow the grain of the wood. One solid whack, like this. Want me to demonstrate?”

The middle-aged man stared blankly at the young man speaking to him so affably.

Despite his easygoing manner, there was something subtly unfamiliar about him.

It wasn’t merely because he was a stranger. It was the young man’s appearance—and his awkward way of speaking, almost like a child.

Only then did a thought suddenly occur to him.

“Could you be…?”

“You mean, am I Han Chinese? That’s right.”

“Ah, then you’re the one I’ve only heard about through rumors…”

“Yes. I’m that very person.”

“Oh! Ohhh!”

As the middle-aged man exclaimed, the young man opened his mouth with a gracious smile.

“My name is Hyuk Mujin.”

“The Blazing Flame Divine Dragon Jin Tae…what Mujin?”

“Hyuk Mujin. The famous Blazing Flame Divine Dragon Jin Taekyung’s right-hand man! The pillar of the great Jin Family of Taiyuan! The proud Vice Pavilion Master of the Murim Alliance’s Fire Dragon Pavilion!”

What the hell was wrong with this guy?

*Hyuk…what?*

Had the Han Chinese started giving people names like that?

The middle-aged man stared at Hyuk Mujin with an uncertain expression, but just as he was about to pick up his ax again—

Tap. Tap-tap.

Raindrops suddenly began to fall.

At the same time, sighs escaped from the people working nearby. There was a mountain of work left to do, and rain would naturally slow them down.

“Damn it. Now it’s raining from a clear sky, too.”

“What can we do? We’ll just have to think of it as a passing shower.”

“Come on, everyone. Let’s keep going a little longer!”

The middle-aged man glanced up at the sky.

Rain from a clear day without a single cloud? Even in Nanman, with its unpredictable climate, this was unusual.

*Still, if it’s only a shower, it should be fine.*

Perhaps because his entire body was already soaked in sweat, the sudden rain didn’t feel entirely unpleasant.

No. In fact, the raindrops striking his palms felt as though they were washing away his wounds, and he found himself enjoying it.

*Refreshing.*

The middle-aged man unconsciously closed his eyes for a moment.

Then—

Grab!

A powerful hand clamped around his wrist. Startled, the middle-aged man opened his eyes and saw it.

“What…is this?”

Hyuk Mujin’s face had gone rigid.

His gaze was fixed on the middle-aged man’s palm, where something strange was happening.

Slowly.

It was disappearing. No—it was healing.

The blisters that had filled both palms, the skin crushed and torn by swinging the ax…

The rain washed away the abundant blood, revealing new muscle and flesh beneath—paler and firmer than before.

“……!”

“……!”

As though they had planned it together, the two men looked up at the sky with wide eyes.

Boom. Boom. Booooom!

Between the sunlit streams of rain, the sound of drums began to ring out, announcing someone’s return.

* * *

A miracle.

Everything could be explained with those two words. No, it was the only way to describe the phenomenon.

Tap. Ssshhh.

At some point, rain had begun falling.

Warmth filled the rain as it soaked countless buildings and the earth, causing flowers and sprouts to bloom. It fell upon the heads of every living thing.

Washing away their wounds and fatigue.

“My wound! My wound healed!”

“My body feels so light!”

“W-what in the world is this…?”

—Growl?

What roused the people, who had been dazed before this unbelievable reality, was a lion’s roar that rang out from somewhere.

—By order of the Palace Lord of the Nanman Beast Palace, I command you all to come outside!

The shout, filled with powerful internal energy, spread throughout the Outer Palace. Those who began walking as if bewitched by the command saw a massive White Tiger and three people standing tall before everyone.

Jeok Cheongang. The Beast Miao King. And Jin Taekyung.

“I called everyone here like you told me to. What are you planning to do now?”

“Wouldn’t it be enough to tell them to come outside and get rained on? They’ll understand once they experience it themselves.”

At the Beast Miao King and Jeok Cheongang’s whispers, Jin Taekyung shook his head without hesitation.

Unlike those two, who were martial artists to the bone, he had been born and raised in the modern world. He knew exactly how effective marketing could be.

“Is it over after they get rained on once? First, you have to process it properly and package it.”

“Process it? Package it?”

“What in the world does that mean?”

“It’s complicated, but in this case, you can think of it as a kind of political maneuvering.”

Martial artists were generally far removed from politics, even when they were old and nearing death.

But being born in twenty-first-century Korea was a different story.

It was a ruthless world where you could become someone who deserved to die just because you were bad at a game.

Jin Taekyung, who had been called an orphan dozens of times in games he had logged into just for fun, knew the importance of politics better than anyone.

*Make the guy who did well look like he failed, and the guy who failed look like he did well. And…*

Politics—modern marketing—was what made the guy who had done well look even better.

Jin Taekyung had no intention of letting this perfect opportunity slip away.

*It’d be a shame to just end things with everyone going, “Wow, a miracle!”*

He muttered inwardly, then took a deep breath. He shouted toward the people, filling his voice with internal energy.

“Listen, everyone! This is a holy rain bestowed by the Earth Mother Goddess!”

The Earth Mother Goddess?

The people blinked at the unfamiliar name, while the Beast Miao King whispered with a displeased expression.

“What is that?”

“A god.”

“There’s no god like that in our land.”

“There is now.”

“……?”

*What the hell is wrong with this bastard?*

As the Beast Miao King fell into deep confusion and lost all words, Jin Taekyung continued shouting.

“The Earth Mother Goddess is the mother of this land, and she is the One God!”

“……!”

“……!”

The One God.

The people who had been listening blankly to Jin Taekyung opened their mouths at those three words.

What kind of place was Nanman?

Thirty-two tribes coexisted here, and there were more than a hundred local gods—more gods than there were tribes.

And now he was claiming there was only one God?

Nanman might have suffered a disaster and the Nanman Beast Palace might have gone to shit, but the faith they had held all their lives remained.

Angry voices erupted from every direction.

“How dare you say such nonsense!”

“The Earth Mother Goddess? I’ve never heard of her!”

“I know you have worked hard for Nanman, but how dare you utter such blasphemy! The Wood God I worship is the One God!”

“What do you mean, the Wood God? The Fire God is the true god!”

“Why, you little bastard!”

The entire courtyard became a chaotic mess.

Yet Jin Taekyung looked pleased as he watched the believers grabbing one another by the collars and fighting.

*Idiots.*

Nanman’s religious scene was as chaotic as the Sixteen Kingdoms.[^1] Thanks to that, things were about to become much easier.

Unlike theirs, his claim had both justification and evidence.

“You fools! Even while being drenched in this holy rain, you still can’t feel the Earth Mother Goddess’s grace?”

His stern reprimand rang across the courtyard, and the noise vanished as if it had been washed away.

One tribesman who had been about to throw a decisive uppercut at another believer looked up at the sky in confusion.

Ssshhhhhh.

Rain poured from the clear sky.

As he watched the rain heal the sick and coax sprouts from the earth, he couldn't help feeling conflicted.

“B-but the Wood God…”

“So what did your Wood God do ten days ago? Even when I was setting fire to the mountain, it didn’t do much.”

“Th-that…”

Jin Taekyung silenced the hesitating believer with a shout.

“Everyone gathered here must have seen it! The dazzling radiance of that day! The warmth!”

“……!”

“The miracle that day and the miracle today are both blessings bestowed by the Earth Mother Goddess, who took pity on you!”

The people’s eyes wavered.

Just as Jin Taekyung said, they had all seen and experienced everything themselves. Even the rain falling on their heads was an unbelievable miracle.

“The Earth Mother Goddess…”

Even her name was warm and familiar. Simply murmuring those four words made them think of a mother’s embrace.

And she was the One God, too. The one and only One God.

“Th-then what are the other gods we’ve worshiped until now?”

At someone’s question, Jin Taekyung answered without the slightest hesitation.

“How dare you compare the great Earth Mother Goddess with miscellaneous gods?”

“M-miscellaneous gods…!”

“The Earth Mother Goddess bestowed this miracle and gave me a divine message: ‘Useless gods. The kind that aren’t worth knowing.’ She told me to protect you from them.”

“Oh! Ohhh!”

“How could this be? A miracle, and now a divine revelation, too!”

Before long, the atmosphere grew feverish, filled with shouts from people united in heart and mind.

Jin Taekyung seized the moment and raised both hands high.

“Shout together! Earth Mother Goddess!”

“Earth Mother Goddess! Earth Mother Goddess!”

“Louder!”

“Earth Mother Goddess! Earth Mother Goddess!”

“Repeat after me. Mother Goddess Heaven! Unbeliever Hell!”

“Mother Goddess Heaven! Unbeliever Hell!”

“Those in Nanman who believe in the Earth Mother Goddess will be saved even after death, while those who do not believe will fall into a pit of fire when they die!”

“Woooooah! O Mother Goddess!”

“Save us! Save this land!”

The tribespeople had already become sons and daughters of the Earth Mother Goddess.

The Beast Miao King stared at Jin Taekyung with an empty expression.

*What the hell are you doing, you lunatic?*

He wanted to stop him. He had to stop him.

He didn’t know anything about politics or packaging, but everyone’s eyes had already gone completely off the rails.

The heavens and earth shook beneath the people’s cries, shouted as though they were vomiting blood.

“Mother Goddess Heaven! Unbeliever Hell!”

“Where’s that guy who said he believed in the Wood God?”

“He’s over there! That one! Throw him into the fiery pit!”

“Gasp! No! I-I’ve already converted!”

“Prove it!”

“M-Mother Goddess Heaven! Unbeliever Hell!”

“He’s one of us! Stop tying him up! Now find the guy who believed in the Fire God!”

A wave of conversions overflowed in every direction.

The oppressive force radiating from thousands—tens of thousands—of people was so great that even Jeok Cheongang, who had privately wondered whether he should try believing in the Fire God, fell silent.

The Beast Miao King, meanwhile, desperately wanted to stop this insane fervor.

“E-enough now…”

And at the moment the Beast Miao King finally managed to drag a voice from his throat, Jin Taekyung’s shout rang out.

“Everyone, quiet! The Palace Lord of the Nanman Beast Palace—the priest chosen by the Earth Mother Goddess—is about to speak!”

“Enough…what?”

“Please speak, Priest.”

“What kind of boss?”

*Priest? Me?*

Before the Beast Miao King could even understand the meaning of the word, countless gazes flew toward him.

A suffocating silence settled over the entire area.

Even he, a Palace Lord with considerable popularity, had never seen gazes so filled with love and trust.

“……!”

The next moment, the lips of the Beast Miao King, who had gone rigid like a statue, parted.

“Mother Goddess Heaven. Unbeliever Hell.”

“Waaaaaaaaah!”

Under the care of the great Earth Mother Goddess, it was a historic moment—the true unification of Nanman.

[^1]: The Sixteen Kingdoms was a period of political fragmentation and competing states in Chinese history.
## Chapter artifact 722

# Chapter 722

The Earth Mother Goddess.

Warmth seemed to radiate from the name alone, and this One God turned all of Nanman upside down the moment she appeared.

It was a spectacular debut that swept away Nanman’s religious scene—once every bit as fiercely competitive as Korea’s idol market.

And then came the wave of faith.

No, the tide of fanaticism.

“Earth Mother Goddess! Earth Mother Goddess!”

“Mother Goddess Heaven! Unbeliever Hell!”

Those who believed in the Earth Mother Goddess would be saved even after death, while those who denied her would die and be thrown into a pit of flames.

Within half a day, those who had become the Earth Mother Goddess’s sons and daughters began marching through the streets, shouting slogans. Before long, that led to proselytizing.

“Hey, you. Wait a moment.”

“Why, why do you ask?”

“Do you happen to believe in any god?”

“Well, um… Ah, yes! I believe in the Earth Mother Goddess!”

“Mother Goddess Heaven.”

“Pardon?”

“You don’t know the slogan? You’re a heretic! Unbeliever Heeell!”

“Eek! I’ll convert! I’ll convert!”

Jeok Cheongang, who had been watching the spectacle, summed up his thoughts in a single short sentence.

“What a fucking shitshow.”

Since Jeok Cheongang was ultimately an outsider, his reaction ended there. But the Beast Miao King, who had somehow become the Earth Mother Goddess’s priest, was half out of his mind.

“This, this isn’t right. No, our traditions… Our native faith…”

But it didn’t take him long to realize what this phenomenon meant.

“Wait a moment. This…”

The Beast Miao King, who had been lost in deep thought, suddenly muttered,

“Not bad. No, this is actually great.”

“You get it now? Nothing brings people together like religion.”

Nanman was in the middle of rebuilding itself, and everyone was working together and cheering each other on. Even so, there was no denying that the current Nanman Beast Palace was divided.

“You’ve been wondering how to deal with the tribal chieftains we’ve thrown into the underground prison, haven’t you?”

“…Yes. No matter how many crimes they committed, they were still the heads of their tribes.”

It wasn’t some pointless, frustrating sense of human sympathy that had made him spare them.

The Nanman Beast Palace was, at its core, an alliance of thirty-two tribes. And more than twenty of those tribes’ chieftains had taken part in this affair.

But if they cut off all their heads under the pretext that they were traitors, some people were bound to grow resentful.

People naturally took their own side.

“For now, the people want them executed, but there will definitely be problems once some time passes. They just haven’t surfaced yet.”

Memories were bound to become embellished over time.

Once things had settled down and the current chaos had faded, people would probably begin whispering things like this:

*Our chieftain was still a decent man.*

*That’s right. He couldn’t help it after falling for Baeksang’s schemes.*

*Come to think of it, something feels strange. Does it really make sense that so many chieftains all took part in it together?*

It was easy to picture.

The conversations that began in small groups, spoken cautiously among themselves, would spread throughout the Nanman Beast Palace and eventually create another division.

“On top of that, the tribes whose chieftains were traitors involved in this affair will be subjected to the other tribes’ silent contempt. That will lead to resentment between the tribes.”

“But we can’t just release all of them, either.”

“They were blinded by wealth and glory and betrayed Nanman once already. Do you think betraying us a second time would be difficult?”

That was why the Beast Miao King had been forced to agonize over how to deal with the traitors.

He had to find the best way to punish them while preventing Nanman from splitting apart.

At least, that had been the case until the One God known as the Earth Mother Goddess appeared and performed an unprecedented miracle.

“Now is the perfect time. We can expose every one of their crimes according to the law, execute them, and tear out every weed from this land!”

The law? Executions?

As the Beast Miao King clenched his fists, I clicked my tongue softly.

*He still doesn’t get it.*

“What?”

“The law is fine, but this is a judgment. God’s judgment.”

“God’s… judgment?”

“The men rotting in the underground prison are traitors who joined hands with the Fiend known as Dark Heaven to corrupt this land. And Great Hero Yayul, as the one and only priest, received a divine revelation from the Earth Mother Goddess. She told him to kill every last one of those bastards and purify Nanman.”

“……!”

“……!”

The Beast Miao King wasn’t the only one to stare at me with wide eyes. Jeok Cheongang, who had been listening to our conversation, did the same.

Their thoughts were written plainly in their eyes.

*Wait, he’s spinning it like that?*

*Wow. Is this guy seriously insane?*

What a pair of naïve old men.

Ten Kings be damned—perhaps because they had spent their entire lives focused solely on martial arts, they still knew nothing about the ways of the world.

Even the Beast Miao King, who had led the Nanman Beast Palace for so long, wasn’t much more politically savvy than Jeok Cheongang.

*No wonder Baeksang’s faction ran rampant.*

But who was I?

A proud citizen of Korea.

I had spent my entire life in a country with more churches than fried-chicken restaurants, where you could see twenty-first-century martyrs carrying crosses whenever you went near a subway station.

I decided to awaken the power within the Beast Miao King, who still lacked any awareness of himself as a priest.

“Now, repeat after me.”

The Beast Miao King, who had been staring blankly at me, reflexively echoed my words.

“Now, repeat after me.”

“No, not that. We’re starting now.”

“Ah. Uh-huh.”

“I am a priest.”

“I am a priest.”

“The Earth Mother Goddess is a god.”

“The Earth Mother Goddess is a god.”

“Good job. Now continue.”

“I am a priest. The Earth Mother Goddess is a god.”

“Excellent. Repeat it.”

“I am a priest. The Earth Mother Goddess is a god. I am a priest. The Earth Mother Goddess is a god. I am… invincible!”

“……?”

That seemed a little different from what I had taught him.

Regardless, the Beast Miao King, awakened as the Earth Mother Goddess’s priest, trembled with a shiver of excitement and took the first great step toward reforming Nanman.

“In the name of the benevolent Earth Mother Goddess, I hereby convene the Tribal Grand Council!”

“…….”

“…….”

He really had become a priest.

* * *

The Tribal Grand Council began in the blink of an eye.

Partly because so few tribal chieftains were able to attend, but even if no messengers had been sent, it probably wouldn’t have mattered.

They were already waiting for the Beast Miao King in a hastily prepared meeting room.

“Palace Lord!”

“It’s a false rumor, isn’t it? Please say it’s a false rumor!”

“What do you mean, the Earth Mother Goddess all of a sudden?”

“Fuck, the tribespeople have gone completely insane. They look just like the Demonic Cultists during the Great Faction War!”

“This is utter nonsense! Are you telling us to abandon the Wood God we have worshiped all our lives?”

But the moment they heard about the marketing effect that launching a new brand called the Earth Mother Goddess would have on the market, those who had rushed at the Beast Miao King with faces full of disbelief and shock declared in solemn tones,

“As tribal chieftain, I must set an example. I shall convert.”

“Our council supports you, Palace Lord.”

“Wow, Nanman has become one!”

“What’s the Wood God? When it comes to gods, it has to be the Earth Mother Goddess.”

They were the people at the top, after all. They knew which way the wind was blowing.

Of course, some people who lacked that sense had also come to confront the Beast Miao King.

“Palace Lord! How can this make any sense?”

“What, exactly, is the Earth Mother Goddess, and where did this nonsense about Mother Goddess Heaven and Unbeliever Hell come from?”

“It’s poison! The Palace Lord has spread poison throughout Nanman!”

“Do you think our priests will stand by and watch? We would rather die than let this situation pass!”

They were dozens of priests, all old—very old.

They had worshiped the traditional local gods all their lives, yet their voices rang out with tremendous force as they confronted the Beast Miao King.

At least, until Jeok Cheongang opened his mouth.

“If you can’t let it pass, what exactly are you going to do about it?”

“What did you say?”

“Huh. Would you look at the way this young bastard talks to his elders.”

“Palace Lord! Punish that insolent man at once! How dare some nobody we’ve never heard of open his mouth so carelessly—”

“Fire King.”

“……?”

“……?”

“That’s my sobriquet. Fire King Jeok Cheongang.”

“……!”

“……!”

“I’ll let those a hundred or older off. Everyone younger, put your heads to the floor.”

The fame of the Fire King Jeok Cheongang—or rather, his temper—was well known not only in the Central Plains but also throughout Nanman.

“Palace Lord?”

“Ah, what a lovely downpour.”

“…….”

When even the Beast Miao King, their final lifeline, looked off toward a distant mountain, the priests immediately got down with their heads to the floor and swore that from then on, they would keep their mouths shut about the Earth Mother Goddess no matter what.

“Honestly, we’re called priests, but we’ve never even seen the gods we serve. Isn’t that right?”

“Hahahaha. Yes, exactly. But the Earth Mother Goddess has personally shown us a miracle like this. How extraordinary is she?”

“Um, Palace Lord. Is there perhaps any room left on the Earth Mother Goddess’s side? Of course, you would remain the priest. But perhaps another position…”

“Ahem. Since you brought it up, the gods we serve are all closely connected to this land, aren’t they? So perhaps we could join forces a little…”

“Exactly! The Earth Mother Goddess is the mother of this land, so in a sense, she gave birth to all the gods, didn’t she?”

It was a fantastic collaboration between the priests, who didn’t want to lose their livelihoods, and the Beast Miao King, who wanted to unify Nanman completely.

After a serious discussion, the Earth Mother Goddess was reborn as a god commanding dozens of useless gods. Since I had no desire for a religious war, I offered a little assistance as well.

“This is getting complicated. Why don’t we just make one while we’re at it?”

“Make what?”

“Well… I suppose we should call it a Bible for now?”

“A Bible?”

“What is that?”

“The history of this land. The word of God. You can think of it roughly that way.”

“Oh!”

“Such a gifted man, surely sent by the gods!”

After that, I simply tossed out a few hints and watched from the sidelines.

The people began racking their brains to cobble together the lore like webnovel authors staring down an imminent deadline.

And at last, the traitors who had spent the past ten days locked in the underground prison were dragged out before everyone.

“P-please spare me!”

“I only fell for Baeksang’s schemes! I never joined hands with Dark Heaven!”

But there was no forgiveness. No mercy.

Ssshhhhhh.

The blessing the benevolent Earth Mother Goddess had bestowed upon this land.

Beneath the rain, which at some point had come to be called the Sacred Rain, the people cried out for judgment, and the executioner’s blade flashed.

Slash!

That was the end of it. The bodies of the traitors who had once led this land were thrown to the beasts.

The endless rain washed away the blood they had spilled.

And only then did the people suddenly realize.

They had finally become one.

They had overcome a catastrophe together, witnessed and experienced an unbelievable miracle, and at last become one family within the warm embrace of the Earth Mother Goddess.

That was the true miracle.

The miracle that had finally united the tribespeople who had been divided into thirty-two factions.

And the forest keeper, who had cut down every diseased tree and weed in the forest, shouted before them all:

“From this moment on, we are the people of Nanman—wholly united as one!”

“Waaaaaah!”

The roar they raised with one voice echoed in every direction.

It sounded like the war cry of warriors heralding the Great War that was soon to come.
## Chapter artifact 723

# Chapter 723

One day. Two days. And then three.

The rain that had come to be called the Sacred Rain was still drenching all of Nanman, and beneath the benevolent grace of the Earth Mother Goddess, nothing could stop the Nanman people who had become one.

Boom. Crack!

With a single swing of an ax from an older man, a massive tree snapped, while a thin woman casually hoisted a mountain of firewood.

Watching the entire scene from beside the window, I muttered under my breath.

“Wow. They got one hell of a buff.”

“B-buff?”

The question came immediately. I had already known there was an uninvited guest, so I turned around and answered.

“Nothing important. But what brings you here? Shouldn’t you be right in the middle of being swamped?”

“I stopped by on the way. And I’m not as busy as I was before. Everything is being sorted out in the blink of an eye.”

“Really?”

For an uninvited guest, he was a fairly welcome sight. I looked at Yayul Mok, the Young Palace Lord of the Nanman Beast Palace, and continued.

“That’s good news. Who do they say they have to thank?”

At my question, Yayul Mok shrugged.

“According to what my father told me, it is thanks to some Han Chinese man. He must have been mistaken.”

“Perhaps. But as far as I know, he wasn’t mistaken.”

“No, he was. There is no way a despicable Han Chinese man would help us.”

“True. The ones from the Central Plains are all like that. You can never trust them.”

“Now you’re speaking sense.”

A short silence passed, and as if we had planned it, we both let out quiet laughs at the same time.

“It’s all thanks to you, Jin Taekyung.”

“We all worked hard, but that’s true. I did contribute quite a lot.”

At my shameless reply, the smile at the corner of Yayul Mok’s mouth deepened.

“Are all Han Chinese people as incapable of humility as you?”

“No. Just me.”

“That’s a relief.”

“Why?”

“Because now I think I might be able to like Han Chinese people more than I did before.”

“Oh…”

I looked at Yayul Mok with renewed interest.

Who would have thought he could say something like that?

I had sensed it little by little before now, but the hostility that had once filled his attitude toward the Central Plains was nowhere to be found.

“Don’t like them too much. Once you actually go there, you’ll find plenty of crazy people.”

“You take me for a child. I know that every place where people live is more or less the same. Nanman and the Central Plains alike.”

“Really? You didn’t seem to know that when we first met.”

“……That was because you turned the fields into a sea of fire.”

Perhaps he had remembered what he had been like back then. Yayul Mok answered with a slightly embarrassed expression before approaching the window where I stood.

He stared at the scene visible through the half-open window, then suddenly spoke.

“It still doesn’t feel real. That something like this happened in the place where I was born and raised.”

“A disaster? Or a miracle?”

“Both.”

After his brief answer, Yayul Mok added one more thing.

“But this, too, must be a god’s will.”

“……Do you believe in the Earth Mother Goddess, too?”

“I’m not sure. At the very least, I believe a god exists. I’ve experienced something that couldn’t be explained otherwise.”

Anyone who encounters something beyond human understanding is bound to think of a god.

They might not know who was up there in that impossibly distant sky, but they would figure that whoever it was had to be one impressive fellow.

*I’m no different.*

Swallowing the rest of my thought, I smoothly changed the subject.

“So, is the cleanup going well?”

“If you mean the restoration work, it has already entered its final stage. We should see the final results within a few days at the latest.”

Considering that the Inner Palace had been reduced to a wasteland and more than several hundred houses and pavilions in the Outer Palace had collapsed, it was a truly astonishing pace.

But instead of being surprised, I gave a small nod.

*Well, the buff is pretty incredible.*

The rain still falling at this very moment contained the powers of life and purification.

It was an area-wide buff that constantly infused everyone with vitality while also enhancing their physical abilities.

*Of course, its effect will end when the rain stops. But even a few days will be enough.*

There was an old saying that even a single sheet of paper was easier to lift with two people. This time, tens of thousands of Nanman people were working around the clock to rebuild the Palace.

They were rebuilding their home. Their homeland.

And their efforts were bearing fruit at an astonishing speed.

“What about the other matters?”

Yayul Mok understood what I meant and answered.

“To eliminate the remaining superiority and boundaries between the tribes, we abolished the Great Chieftain system. We received the agreement of not only the Miao people but also all four of the other great tribes.”

“Good work. Ah, then what about Yohi?”

Yayul Mok nodded.

“She was the first person to call for the abolition of the Great Chieftain system.”

The tribal chieftains who had joined hands with Baeksang had been executed in front of countless witnesses, but Yohi alone had received a full pardon.

She had repented of her mistakes, albeit belatedly. More importantly, she had played a vital role in leading the beasts and evacuating the tribespeople from the Outer Palace. Because of that, no one had raised any serious objection to her pardon.

“She said that she couldn’t leave behind the same precedent as Baeksang, Heugung, and herself.”

“She was right. Before this, the Great Chieftains had wielded far too much power.”

“My father and the other tribal chieftains agreed as well. Because of what happened, the Nanman Beast Palace will now operate under the sole authority of the Palace Lord. The Tribal Grand Council will remain in place to prepare for any unforeseen situations. And…”

As I listened to the rest of Yayul Mok’s explanation, I realized once again that the Nanman Beast Palace had been reborn.

The authority of the Beast Miao King, who now served as both Palace Lord and priest, had become incomparably greater than before. The unsettled public mood had stabilized with the appearance of the Earth Mother Goddess, and the people had united regardless of their tribes or faiths.

After hundreds of years, the balance of this land, which had been divided into thirty-two pieces since the Nanman Beast Palace was founded, had finally become one.

*At this point, I could really call it a small kingdom.*

Tens of thousands of tribespeople and nearly ten thousand warriors.

And if you counted the beasts they commanded, it was by no means an exaggeration.

Even allowing for the fact that the Nanman warriors were inferior to the martial arts of the Central Plains, they still represented an immense military force.

I looked at Yayul Mok with renewed interest.

“……Why are you looking at me like that?”

“No, now that I look at you, you seem to have a touch of nobility. So you’re actually a prince, or something like that?”

“……A prince?”

Yayul Mok muttered in an awkward voice, then suddenly let out a quiet laugh.

“Why are you laughing? Looking at the current situation, it’s not entirely wrong.”

“Now that I think about it, I suppose it is an honor.”

“What?”

“The Apostle of the great Earth Mother Goddess is calling me a prince. How could that not be an honor?”

“……?”

What was he talking about now?

As I blinked at Yayul Mok, unable to understand him, he handed me something he had taken from inside his robe.

“Take it.”

“This is…”

“We decided to call it the Mother Goddess Scripture. My father told me to give it to you.”

The moment I accepted the bundle of bamboo strips with a bewildered expression—

Ding.

> **System**
>
> — You have acquired Mother Goddess Scripture.
>
> — Mother Goddess Scripture is a scripture containing records of the Earth Mother Goddess.
>
> — A god can exist only when someone believes in it.
>
> — The Earth Mother Goddess has become known as the One God of Nanman!
>
> — Countless believers who follow the Earth Mother Goddess are ecstatic!
>
> — According to the records in Mother Goddess Scripture, your name has become known anew!
>
> — You have achieved Religious Reformation, an achievement that makes one wonder whether anyone would actually go this far!
>
> — You have acquired the Title Apostle of the Earth Mother Goddess!

Holographic windows filled the air along with the System notifications.

I stared blankly at the sight, then hurriedly unfolded the bundle of bamboo strips in my hand.

After reading the tiny writing etched across them, I burst out laughing in disbelief.

“What is this?”

Seeing my reaction, Yayul Mok shrugged.

“It says exactly what it means. The Earth Mother Goddess has been with this land since ancient times as its mother goddess, and whenever Nanman fell into crisis, she personally sent her apostle to save the people…”

“That’s me?”

“Of course. Three hundred years ago, it was my ancestor, the first Palace Lord. And two hundred years ago, it was the Sect Leader of the Fire Gate Clan at the time—the clan you belong to.”

They had managed to force everything together like this.

It was true that I had dropped a few hints, but I never expected to see my three-character name written right there.

No. To be precise, it was *our* names.

Flip.

When I skimmed through the rest, I found quite a few familiar names.

Jeok Cheongang, of course. The members of the Fire Dragon Pavilion. Even Namho’s name.

This was supposed to be something like a Bible. Was this really allowed?

“I know it was thrown together in a hurry, but this is ridiculous. Who the hell came up with this setting?”

“My father.”

“No wonder it’s so impressive. How did he manage to make the setting this detailed?”

“……”

I avoided Yayul Mok’s gaze and tucked the bamboo strips into my robe.

*The Apostle of the Earth Mother Goddess.*

I had somehow become a god’s apostle, something that had never been written in my fate, but I didn’t feel particularly bad about it.

No. In a situation like this, it was actually a major gain.

*The ill feelings Nanman’s people have toward the people of the Central Plains should be diluted now.*

As I was muttering inwardly, Yayul Mok suddenly asked,

“So, have you finished preparing?”

“Hm?”

“Preparing to leave Nanman.”

“……!”

After a brief silence, I smacked my lips.

“You’re sharp.”

“It would be strange if I hadn’t noticed.”

“How did you know?”

“Leaving aside everyone else, that huge fellow has been frantically gathering food since yesterday. Like someone preparing to set out on a long journey.”

There was no need to ask who he meant by “that huge fellow.” Guessing the culprit, I sighed.

“Taishan, you crazy bastard. I told you to move quietly.”

“Your Master, the Fire King Jeok Cheongang, secretly took five jars of fruit wine.”

“…….”

Oh, come on. Old Master.

I squeezed my eyes shut, and Yayul Mok’s voice pierced my ears.

“You should at least say goodbye before you leave. Everyone is waiting.”

* * *

Only after we drew near the North Gate did I realize that the two words Yayul Mok had used—“everyone”—were not an exaggeration in the slightest.

*This is…*

Thousands. Perhaps tens of thousands.

Among the countless people filling the field outside the North Gate, where fresh grass and flowers had spread thanks to the life-giving downpour, I saw several familiar faces.

Jeok Cheongang, pretending not to notice anything in front of a cart loaded with jars of fruit wine.

Taishan, holding meat in both hands with a solemn expression, along with the members of the Fire Dragon Pavilion, each mounted on a beast.

And then…

“You’ve finally arrived.”

The Beast Miao King, Yayul Cheok, spoke with a stern expression. As the master of the Nanman Beast Palace, he represented every Nanman person on this land.

“Why were you trying to leave without saying a word?”

I scratched the back of my head.

“I was going to tell you.”

“You were?”

“Through a letter.”

“Just a letter?”

“No, it’s just that you looked so busy…”

“Do you think that makes sense?”

“……”

Was this what they called a question-mark murderer?

Unable to think of anything to say, I hesitated. The Beast Miao King, who was at least a head taller than me, silently looked down at me.

“Blazing Flame Divine Dragon Jin Taekyung.”

It was a quiet summons. The Beast Miao King continued in a solemn voice.

“You had a purpose. There was a reason you came to our homeland—to this land. Was there not?”

“……”

“But today, you are trying to leave without a word even though you have not achieved your purpose. You crossed a foreign land and survived countless brushes with death. You saved the lives of countless people. And yet you never once demanded a rightful price.”

The Beast Miao King’s powerful gaze and voice were directed at me, but everyone present was listening. Everyone was watching.

“What is the reason?”

At the Beast Miao King’s question, I suddenly opened my mouth.

“I was simply a person trying to save people.”

“……!”

“I didn’t do it to receive a reward. And I couldn’t ask for another sacrifice. That’s why I was going to leave.”

Silence fell.

Even though tens of thousands of people had gathered together, the silence was so deep that not even a breath could be heard.

Because of that, the rain falling over our heads sounded especially loud. Beyond it, the Beast Miao King’s towering figure moved.

Ssshh.

His back, firm as a pillar—the back of the master of the Nanman Beast Palace, which should never have bowed before another—leaned toward me.

Then, before everyone watching, the Beast Miao King performed the most courteous of clasped-fist bows and spoke.

“I, Yayul Cheok, the Beast Miao King, on behalf of everyone who lives on this land, formally petition Great Hero Jin Taekyung, Fire Dragon Pavilion Master, for our admission into the Murim Alliance.”

It happened on a certain day when the rain was slowly coming to an end.
## Chapter artifact 724

# Chapter 724

Some people left, while others stayed behind.

But as the Beast Miao King watched the backs of those departing on a long journey, he knew. Before the lingering ache of this farewell had even faded, they would meet again.

And that place of reunion would be a battlefield where they fought back-to-back.

“In the end, we’re heading to the Central Plains once again.”

At the voice that pierced his ears, the Beast Miao King gave a small nod.

“Yes. It came to this in the end.”

“A great deal of blood will be spilled.”

“Do you think your father’s decision was wrong?”

“No.”

Yayul Mok continued calmly.

“If my father… No, if the Palace Lord had not wanted to go to the Central Plains, I would have left with them even on my own.”

“……!”

Yayul Mok’s gaze turned toward the figures receding in the distance.

Strangers from a foreign land. And yet, because those strangers had come, they had been able to protect their homeland.

“Now it is our turn to help them.”

There had certainly been a time when he, too, had regarded the Central Plains with hostility and rejected the Han Chinese.

But things were different now. The still-unseasoned Young Palace Lord of the Nanman Beast Palace had learned what it meant to act with humanity from one stranger, and he would never forget the conversation they had shared that day.



*“What would you do if the pasture caught fire?”*

*“Put it out right away.”*

*“Why?”*

*“If we don’t put it out, the flames will spread in every direction.”*

*“Good. There’s your answer.”*

*“……!”*

*“Don’t overthink why we came. A fire started, so we’re putting it out. Just like the Nanman people of this land who left their homeland for the Central Plains decades ago.”*



At first, he had not believed it. He could not believe it.

The Han Chinese he knew were nothing but utterly despicable people who had betrayed trust and driven countless Nanman people to their deaths.

There was no way they had crossed a distance of more than ten thousand li to offer help without asking anything in return.

That was what he had thought back then…

*But now I understand. I understand what you meant.*

The pasture called the world had already caught fire, and the enormous conflagration known as Dark Heaven would devour everything.

Where someone had been born and raised, what clothes they wore, or what they looked like no longer mattered.

Just as Nanman had finally become one, everyone would have to join forces to put out that fire.

“We will fight with our lives on the line. For everyone living on this land. And for them.”

Seeing Yayul Mok display such unyielding determination, the Beast Miao King smiled faintly.

*When did he grow so much?*

Just as Nanman had finally become one, his only son had taken another step forward.

And yet, why was it that at this moment the Beast Miao King’s heart felt as hollow as an empty jar?

*You hopeless brat.*

Swallowing the bitter mutter, the Beast Miao King tilted the flask he had taken from inside his robes.

Fruit wine carrying a fragrant scent of alcohol seeped into the earth along with the slowly fading rain—into the soil of the homeland where two sworn brothers had been born and raised together.

“This wine tastes excellent. Don’t you agree?”

The Beast Miao King had not tasted a drop, yet at his mumble the people around him looked puzzled. He merely laughed with relief.

This was enough.

In the distant future, they would meet again and raise their cups together.

*Yes. One day, surely.*

The Beast Miao King suddenly lifted his head and looked at the sky.

Between the slowly fading sheets of rain, azure heaven stretched above the heads of countless Nanman people.

Or perhaps it was the gaze of an unseen absolute being.

“Sound the war drums.”

His quiet voice broke the suffocating silence. Taking a deep breath, the Beast Miao King drew up his internal energy and shouted.

“God wills it!”

As the azure dragon’s roar reverberated in every direction, a snow-white White Tiger gazing down at them from somewhere atop a high hill let out a roar.

—Kraaaaaaang!

Clang-clang-clang!

Waaaaaaah!

Thousands—tens of thousands—of beasts and humans stamped their feet and roared. Sunlight reflected off countless blades and spread in every direction.

At long last, the prelude to the Great War had begun.



* * *



Eyes filled with sorrow and a solemn atmosphere. With everyone watching him, Hyuk Mujin slowly parted his lips.

“It was simply one person trying to save another.”

“Stop it.”

“I didn’t do it to receive a reward. And I couldn’t ask for another sacrifice. That’s why I was going to leave.”

“I said stop.”

“Come on, why are you like this? I never get tired of doing this, no matter how many times I repeat it. Honestly, you all agree, don’t you?”

Taishan, tearing at a wild boar’s hind leg atop a bear that was running without pause, vigorously nodded.

“Taishan agrees!”

“See? Even he agrees. It was simply one person trying to save another…”

I quietly cut Hyuk Mujin off.

“Mujin.”

“Yes.”

“Do you want to become a eunuch?”

The smile that had spread across Hyuk Mujin’s face faded.

“No.”

“Or is life boring?”

“Of course not. I’m already worried that my life is too intense as it is.”

“Then do you want me to make it peaceful?”

“You don’t mean that you’re going to kill me, do you?”

“What if I do?”

“Wow, look over there. The scenery is beautiful.”

“Good. Let’s travel quietly.”

“……Yes, sir.”

But unlike Hyuk Mujin, who promptly shut his mouth, Taishan wore a disappointed expression and asked for an encore.

“Pavilion Master! Taishan wants to hear more!”

So I called in his designated bully.

“Old Man Nam, I think it’s time to shut that bastard’s mouth.”

“Oh! Finally!”

Namho cheered like an independence fighter celebrating liberation and, as if he had been waiting for this moment, pulled a muzzle from inside his robes.

It was a bizarre yet strangely familiar device made of black, sturdy iron connected by leather straps.

“Wait. Where did you get that?”

“I got it from a Nanman trainer. Apparently, it is mainly used to tame wild bears.”

“……”

“Why are you looking at me like that? Is there some problem?”

“Well, I wouldn’t say it’s exactly a problem.”

It was just that it somehow bothered me a little. Or perhaps it was more like an odd feeling that, from now on, I should call Taishan by the product number TAESAN-317 instead of his name…

After hesitating for a moment, I finally gave in to my unease and sighed.

“Don’t put that on him. No. Just throw it away.”

“No! Why?”

Why? Because I felt like it would dirty my eyes.

I snatched the muzzle from Namho, who was practically wailing, and threw it far into the distance. Jeok Cheongang, who had watched the whole thing, opened his mouth with an unpleasant expression.

“What on earth happened in Nanman?”

For a moment, I failed to understand the question and asked,

“Pardon?”

“I’m asking what happened for all of you to lose your minds.”

“Nanman certainly went through a lot, but everyone is still exactly as they were before.”

“What!”

“Surprisingly, it’s true.”

“You insolent brat! Don’t talk nonsense. Does it make any sense that not a single person died when everything is this much of a goddamn mess?”

“……”

Yeah. Fuck.

Looking back on what had happened in Nanman, I had a reasonable suspicion that the Earth Mother Goddess really had blessed us.

*I had come close to death several times, but the fact that I was returning in one piece was a miracle in itself.*

Of course, I was the only one who had repeatedly come close to death. As for the others, who had suffered injuries both major and minor, the Sacred Rain had done its work thoroughly enough that they had now recovered as if they had never been hurt.

*On top of that, we somehow managed to stop Dark Heaven’s sinister plot.*

Though not a small number of people had been sacrificed in the process, being able to stop the Southern Heaven Demon Empress—who had practically been the top priority for both me and the Fire Dragon Pavilion—was more than half a success in itself.

*And on top of that, the Nanman Beast Palace had officially joined the alliance.*

In truth, the Nanman Beast Palace’s joining had been more or less inevitable the moment we stopped the Southern Heaven Demon Empress.

Even without the Earth Mother Goddess’s brand effect, the outcome would not have been much different.

An ember trampled down halfheartedly would burn even hotter, and the emotion of anger would bind together those who had been scattered.

I had merely given them another center around which to gather.

The existence of a One God who could erase even the boundaries between tribes that had been passed down for hundreds of years. A center around which they could become an even more united and powerful force.

*And thanks to that, the Murim Alliance’s strength had increased as well.*

This time, I could say it without hesitation. Because of this incident, the Nanman Beast Palace had unquestionably become an ally.

According to what the Beast Miao King had promised before we left, they would send more troops than they had during the Great Faction War and do everything in their power to hold back Dark Heaven.

But why?

*Why do I feel so uneasy?*

Even though we had achieved major results, one corner of my heart was still filled with an unpleasant unease that I could not shake.

And perhaps the reason was the question that remained unresolved.

*The new Murim Alliance has been born, and all the strength of the Central Plains is gathering around the Nine Sects and One Gang and the Five Great Families. And yet Dark Heaven’s full strength still hasn’t been revealed.*

Dark Heaven’s first intervention in Shanxi Province, the Shaolin Bloodshed that followed, and the series of incidents that had continued to this day could never be called minor.

But they were merely fragments—not even a fraction of the organization as a whole.

*The time for testing the waters should have passed already.*

What the hell were they—or rather, what was the Lord of Heaven—trying to accomplish?

And why was the Lord of Heaven…

“Why would the Lord of Heaven take this much interest in me, of all people?”

My mutter slipped out without thought, and everyone’s gaze snapped toward me. Before I could say anything to smooth things over, Hyuk Mujin suddenly raised his head like a meerkat.

“Gasp, Captain. Did someone confess to you? Oh my God. A Nanman?”

“……”

I wanted to gouge out those eyes of his, shining like newly risen stars.

I suppressed the impulse and answered.

“It’s not like that, you crazy bastard.”

“No way. Then a Han Chinese woman?”

“How many times do I have to say it isn’t… Ah, come to think of it, the Han Chinese part is right.”

“Wow. When did this happen? Who confessed?”

“The Lord of Heaven.”

“Wow. That’s quite an extraordinary name for a young lady. She sounds like the daughter of a respectable family…”

Hyuk Mujin, who had been making a fuss, suddenly fell silent. After blinking and thinking for a moment, he continued.

“Who?”

“The Lord of Heaven.”

“The one I know? I mean, the one everyone knows?”

“Who else could it be?”

Hyuk Mujin remained silent for a moment, then muttered under his breath.

“Fuck. That respectable household was in Xinjiang…”

Beyond Qinghai, where the Kunlun Sect was located, lay Xinjiang—and Xinjiang had been the domain of the Demonic Path for a thousand years.

Once everyone realized that the young lady interested in me was a daughter of the Dark Heaven household, they stared at one another in silence, at a loss for words.

Then questions erupted from all sides.

“Why would the Lord of Heaven be interested in him?”

Namho cut in at Hyuk Mujin’s question.

“Isn’t it obvious? Because he keeps getting in the way?”

“That’s true, but the Captain isn’t one of the Three Saints or the Ten Kings. He’s just a scrap who only recently earned a reputation.”

“Now that you mention it, that’s not wrong either.”

“Taishan can eat scraps too.”

“You son of a bitch. I knew this might happen, so I brought another muzzle. Come here. Open your mouth.”

“No, why are you all putting it like that? Our Pavilion Master is a scrap? Song Escort, Young Hero Sama! Say something!”

“Young Lady Ju, I’m sorry, but I think I have to leave at this point. We somehow made it all the way to Nanman, but the Lord of Heaven taking an interest in that man is a bit much.”

“Taishan! That isn’t meat, so don’t bite it! Old Man Nam! Will you put that muzzle down right now!”

“……”

Fuck. I had never seen such a complete mess.

And as I stood there blankly staring at the total disaster unfolding before my eyes, a quiet Sound Transmission pierced my ears.

—Let’s talk.

It was Jeok Cheongang.

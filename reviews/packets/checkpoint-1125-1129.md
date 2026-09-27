# Checkpoint Review — 1125–1129

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

# Chapters 1125–1129

## Plot

Taekyung’s spear pierces the Blood Lord but misses his heart when Taekyung’s power runs out. The Blood Lord takes White Flame, crushes Taekyung’s wrist and legs, and chokes him. Mae Jonghak arrives and severs the Blood Lord’s arm; the Lord of Heaven’s power then disappears. Taekyung holds the wounded Blood Lord in place and bites his neck as reinforcements arrive.

The Blood Lord dies after one last attack on Taekyung, which Jeok Cheongang blocks. The Dark Heaven army collapses. The System grants Taekyung several Level Ups and completes Quests, but his innate qi is damaged beyond recovery. With his Final Rally countdown expiring, Taekyung says farewell to his allies and the world closes around him.

Taekyung later awakens in a boundless gray-white space. An unidentified old man who can read his thoughts refuses to explain who he is or how he helped Taekyung, then attacks him. Taekyung retains his internal energy and martial techniques; the old man gives him a spear, and their fight begins.

## Continuity

- The Blood Lord is dead; the Dark Heaven army has collapsed. Reinforcements from the Yangtze River Channel League, Green Forest Alliance, and Murim Alliance arrived, and the battle was still underway when Taekyung’s countdown expired.
- Taekyung’s innate qi was damaged beyond recovery. His survival after the countdown was uncertain until he awoke in the gray-white space.
- Hyuk Mujin is alive but unconscious and badly injured; the Seafaring King removed the lethal blood in time, and Mae Jonghak says Mujin is out of danger.
- The Seafaring King and Green Forest Battle King joined the resistance after Mae Jonghak persuaded them. Allied forces were fighting in Xining under Taekyung’s name.
- Taekyung asked Jeok Cheongang to pass a message to his family in the realm of immortals if they met. Jeok hoped they would meet again after death; their conversation ended before he could state the favor he wanted in return.
- The unidentified old man can read Taekyung’s thoughts and says he has already pushed himself to help him, but does not explain how. Taekyung retains his internal energy and martial techniques in the gray-white space. The old man’s identity, how he helped, and what happens in the space remain unresolved.

## Translation Decisions

- Render 하청지회 as “an auspicious meeting after the Yellow River runs clear,” preserving Wolhwa’s wordplay and the letter’s promise to meet again.
- Render 선천지기 as “innate qi” and 진원진기 as “original true qi” when both terms are stated.
- Render 저승 as “afterlife” in Taekyung and Jeok Cheongang’s conversation.
- Render 우화등선 as “ascend to immortality.”
- Render 골골아 as “Golgoli” when Taekyung addresses the Skeleton King.

## Durable state

{
  "active_continuity": [
    "Taekyung awakens in a boundless gray-white space after his apparent death.",
    "An unidentified old man can read Taekyung’s thoughts and says he has already helped him, but does not explain how.",
    "Taekyung retains his internal energy and martial techniques in the gray-white space.",
    "The old man attacks Taekyung and gives him a spear; their fight begins."
  ],
  "continuity_sources": [
    1129
  ],
  "open_questions": [
    "Who is the old man, and has he met Taekyung before?",
    "How did the old man help Taekyung, and what does he intend to begin?",
    "What is the gray-white space, and what happens to Taekyung there?"
  ],
  "safe_through": 1129,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1125

# Chapter 1125

KRRRCH!

At the moment a ghastly sound of flesh being torn apart rang out, the Blood Lord was suddenly overcome by the illusion that the world had stopped.

*Ah.*

Hot. Distant.

His vision wavered, and the noise around him seemed impossibly far away.

Everything surrounding him felt so unfamiliar that he wondered if perhaps everything that had happened until now had been a dream.

If not for the terrible heat scorching his flesh and bones, he might truly have thought so.

No.

If not for the face he could see beyond the acrid smoke and shimmering haze of the flames.

*Cough.*

Fresh blood spilled past his lips.

Amid the searing pain that turned his vision white, the Blood Lord coughed up blood mixed with bits of his innards and looked at the young man before him.

The reckless young moth, now joined to him by a single spear.

Then, suddenly, he parted his blood-soaked lips.

“How?”

His eyes held genuine confusion.

Jin Taekyung answered the brief question, laden with meaning.

“I don’t know either.”

“What?”

“I just… knew, as if it were the most natural thing in the world.”

His voice astonishingly calm, Jin Taekyung continued.

“Every move you’d make. And what I had to do.”

“……!”

“That’s all.”

For an instant, the Blood Lord’s eyes widened before he even realized it.

Was it because of the pain, as if he were burning alive?

Wrong.

The accursed spearhead had pierced his palm and driven deep into his body, spreading heat through him. But compared to the shock he felt now, that was nothing.

*He knew? Everything I’d do?*

If he’d heard those absurd words a moment ago, he would have scoffed.

His power had grown beyond its limits, and the gulf between them was so vast that even the word *possibility* had become meaningless.

But—

*He isn’t lying. He isn’t boasting.*

The moment their eyes met, the Blood Lord understood instinctively.

A single truth, unbearably cruel to him.

And that he had been desperately denying it.

“So there was no point in asking from the start.”

“Yeah.”

Jin Taekyung gave a small nod, then added in a faint voice,

“At least in that moment, I was stronger than you.”

At last, the enemy’s lips gave voice to a truth he could no longer deny. A shiver ran down the Blood Lord’s spine.

Countless emotions swept through him, overwhelming even the pain.

Bitter defeat. Fear born of something impossible to understand. And, at the same time, something entirely opposed to those feelings.

Deep relief and joy.

In this moment, his whole body knew he had made the right choice.

*Lord of Heaven, my revered master. Are you watching? Can you hear me?*

The Blood Lord suddenly looked up at the sky.

He whispered to his own heavens, hidden behind the unceasing rain and dark clouds.

*My choice was never wrong.*

Truthfully, a thread of anxiety had been stirring in a corner of the Blood Lord’s heart.

He hadn’t resolved to eliminate Jin Taekyung out of unwavering loyalty alone.

He’d been disappointed. Resentful.

His master seemed to have no thought for the welfare of his servants, who gave their lives in service.

And, absurdly, he’d been jealous.

Jealous of Jin Taekyung, who had all but monopolized that same master’s almost affectionate attention.

So he’d wanted to kill him.

He’d claimed it was to remove an obstacle that kept standing in Dark Heaven’s way, and forced himself to rationalize it beneath those three words: *loyalty to his master.*

But now there was no need.

Here, today, Jin Taekyung had proved with his own actions why he absolutely had to die and disappear.

And he would. Without fail.

“Blazing Flame Divine Dragon Jin Taekyung. I’ll admit it. You truly deserve to be called a Divine Dragon.”

The Blood Lord whispered to Jin Taekyung, and there wasn’t a trace of falsehood in his words.

No—the title *Divine Dragon* even seemed insufficient.

Even as he stood at death’s door, he’d been swept into a trance, drawing closer to a higher enlightenment. The memory of it still sent a chill through the Blood Lord.

“Yes, you were right. In that moment, you were terrifyingly strong. Strong enough that even I couldn’t stop you.”

He didn’t know what profound enlightenment Jin Taekyung had gained.

He didn’t know how he could fight so desperately when his life was hanging by a thread.

He didn’t know how a spearhead carrying no more than a trace of energy had broken through his formidable Force.

But—

“That means nothing.”

By then, the Blood Lord was smiling.

With a bright smile no defeated man could wear, he grasped the spearhead buried deep inside him.

More precisely, the spearhead of White Flame, embedded a handspan from his heart.

*Squish. Crack.*

Blood burst out with a ghastly sound of torn flesh.

The Blood Lord pulled out the spearhead with a hand wrapped in dense Palm Force and muttered,

“I thought I was dead. In that moment, I certainly did.”

Jin Taekyung’s final attack, thrown with all his strength, had been a strike the Blood Lord could not possibly have stopped.

If Jin Taekyung’s internal energy hadn’t run dry at just the right moment—

If the weakened spearhead hadn’t veered off course because of it—then that would have been the end.

But it hadn’t happened.

“This is Heaven’s will.”

The Blood Lord felt joy welling up from deep within him.

The heavens above had, in the end, chosen him—not Jin Taekyung.

“Not that paltry heaven you believe in. This is the will of the true Heaven I serve!”

Right then.

With a shudder like a bolt of lightning, powerful enough to make him forget the pain in an instant, the Blood Lord pulled his pierced hand free and twisted the spear shaft.

SHWIK—KRRRCH!

The spear shaft spun violently, driven by a force too great to resist.

White Flame, as it was called, snapped through the collar of the garment that had been tightly tied to keep its owner from losing his beloved weapon. It was more than enough to leave its owner’s grasp bloodied.

*Splatter.*

Jin Taekyung was shoved backward, unable to withstand the force.

He fell, unable even to keep his body upright.

The Blood Lord stepped toward him without hesitation.

Or rather, he tried to.

Until another Divine Dragon—one who had grown up on the slopes of Mount Huashan, not beside a pond—charged in with a roar.

“No!”

SHWAAAAK!

Sunset spread through the darkness. Force bloomed along the sword’s blade, cracked from end to end, then scattered in thirty-six petals.

A sword strike beautiful enough to draw gasps from anyone who saw it.

But the feelings behind it were more desperate than ever, and that made it all the more heartbreaking.

FWOOM!

Then the blood-red Force that engulfed the space was so powerful it could cut down not only the petals, but an entire forest.

KWA-BOOOOM!

The earth shuddered with a deafening crash.

Beyond the cloud of dust that even the pounding rain couldn’t settle, a figure staggered to his feet and stood in front of Jin Taekyung’s fallen body.

Not one, but two.

“Where do you think you’re going? *Cough.*”

At the sight of Jeok Cheongang and Cheongpung, their bodies no better than blood-soaked men, rising once more to block his path, the Blood Lord’s red eyes sank into a cold glare.

“Mount Beimang.”

Raising the spear that now belonged to him at an angle, the monster added,

“Of course, you’re the ones going there.”

*Hummm.*

The spearhead, separated from its master, let out a sorrowful hum.

* * *

*Shhhhh.*

Beyond the rain pouring without end, I stared blankly at the dark sky stretching endlessly above me.

*This is Heaven’s will.*

Listening to the Blood Lord’s voice echoing in my ears even now.

*Not that paltry heaven you believe in. This is the will of the true Heaven I serve!*

Remembering those blood-red eyes, boiling with joy, I muttered to myself,

*Yeah. Maybe it is.*

I’d certainly done everything I could.

No—every one of us had fought with all we had.

Until there was nothing left to give.

Until there was no room for regret or anger.

But…

*I never followed some will of Heaven.*

Quietly, desperately, I struggled.

*Crunch.*

With a hand crushed and broken all over, I gripped a clod of dark red earth mixed with blood as hard as I could and pushed myself up.

I had to. There was no other choice.

For the people even now collapsing, their blood scattering around them.

The paltry heaven the Blood Lord had mocked—that was these people.

*BOOM!*

A fierce crack of air burst through the space.

Jeok Cheongang, staggering as he dropped to one knee. Cheongpung’s figure, flung like a cannonball and rolling across the ground. Both came into my blurred vision.

And the monster’s steps, as he came toward me after tearing down every last obstacle in his way.

*Splash.*

One step, then another.

As the distance closed, the Blood Lord’s red eyes grew clearer. I used every bit of strength I had to get up.

Like a baby turning over for the first time, I rolled onto my front, braced myself on my hands and knees, and somehow got my unsteady body to its feet.

And at the moment I met the Blood Lord’s eyes, now close enough to blaze red like the sun—

*Inventory open. Summon.*

From the boundless storehouse granted to me alone in this vast world, I drew a finely sharpened dagger and thrust it forward.

At the same time, I heard a quiet sneer cut into my ears.

“As expected.”

*Crack.*

I felt no pain, but the sound alone told me what had happened.

The Blood Lord had snatched my wrist in a flash and crushed it beyond any hope of recovery.

But the Blood Lord wasn’t the only one who could predict his opponent.

*Slip. Tap.*

Ignoring the pain erased by my final rally, I kicked the dagger’s hilt with my toe as it fell from my grasp.

*Thud.*

“……!”

With a cool, tearing sound, the dagger sank deep into flesh.

The Blood Lord’s eyes flew wide as he looked down at the blade buried in his shin. He licked his lips.

“Impressive. Truly impressive. But because of that…”

Without a moment’s hesitation, he whipped his remaining leg like a lash.

“You can never be allowed to live.”

KRRRCH!

White bones burst through mangled flesh.

After crippling one arm and both legs, the Blood Lord shot out his hand like lightning and grabbed me by the throat.

*Crack.*

My bones shifted with a crunch, and my vision darkened.

The Blood Lord’s voice, sunk deep and low, reached my ears as I gasped for breath.

“This has been a long and bitter connection. Blazing Flame Divine Dragon Jin Taekyung.”

At that moment—

*FWOOSH.*

Like the last candle recalling the life that had come before, my vision, tumbling into pitch-black darkness, turned white.

No.

Perhaps it was a shade deeper and redder than sunset.

*Slash.*
## Chapter artifact 1126

# Chapter 1126

It was a very low, faint noise—one no one would have paid attention to under ordinary circumstances.

Nothing compared to the incessant roar of the battlefield, which shook the heavens and earth even now.

Just the sound of wind brushing past somewhere.

But to someone else, it was a sudden storm, an unstoppable bolt of lightning.

*Shhk.*

At the cold slicing sound that belatedly pierced his ears, the Blood Lord’s lips moved before he knew it.

“……Huh?”

A moment ago, his eyes had been alight with joy. Now, a deep question had surfaced in them.

So had the blood-red pupils that reflected a fine line running across his arm.

But before the Blood Lord could find an answer, blood welled up through his skin and raced along that line.

*PSSSHHH!*

As a fountain of blood shot into the air, the Blood Lord could only stare, eyes wide, at his arm falling away in a spray of crimson.

And at the figure who, having barely escaped death, collapsed beside the severed limb.

*Splatter!*

The moment Jin Taekyung’s already-crippled body crumpled to the ground, time—which had stood still—began to move again.

Yet even with the man he had so desperately wanted to kill fallen at his feet, the Blood Lord couldn’t move.

No—he wasn’t the only one whose movements had stopped for an instant.

Jin Taekyung’s master, reaching a trembling hand toward his disciple, who lay in a deep pool of blood facing death.

The Bow Saint and the Slaughter Saint, who had finally shaken off countless enemies, including two Black Ghosts, and were hurtling forward, slicing through every fraction of an instant.

Cheongpung, driving the blade of his sword—now only a handspan long—deep into the ground as he forced himself upright.

They all felt it. And at the same time, they saw it.

Beyond the curtain of wind and rain blocking the space, a figure flickered faintly.

*Fwoosh.*

Amid the endless rain, an ancient silver blade suddenly swept down, following the fingertips of a black-clad figure walking through the storm.

*Shhhk.*

In that instant, the world split apart.

The rain and wind.

The air and energy that permeated them.

And the darkness.

*SHWAAK!*

The dazzling flash that filled everyone’s eyes was deeper than a sunset and as brilliant as dawn.

Just like that day a year ago, burned into the Blood Lord’s mind like a brand.

*This is…*

In a moment so brief it seemed time had been cut into slivers, the Blood Lord froze, eyes wide. Someone’s presence flashed through his mind.

A name that shouldn’t—or couldn’t—have appeared here today.

A man without peer when it came to the sword, and thus known as the Number One Sword Under Heaven.

A man whose realm had finally reached the heavens, and so was called the Sword Saint.

“Mae Jonghak—!”

The Blood Lord’s cry burst from his lips.

*FWOOSH!*

Within the enormous swelling flash, dozens of branches of purple Force blossomed.

*Tap.*

Beneath the dazzling petals of Force, a hand abruptly reached out and touched the Blood Lord’s foot.

No—

*KRAK!*

It seized the monster’s ankle with all its strength as he hurried to turn away.

Just like that day when Mount Song was stained with blood.

“……!”

In the monster’s blood-red eyes, suddenly wide, a young man’s faintly smiling face was reflected.

And the purple flash that had finally reached him.

*KWA-BOOOOM!*

* * *

Not being able to feel pain is both a curse and a despair.

Pain is proof that you’re alive and breathing.

For the living to feel no pain means death is close.

But that’s only one side of the coin.

For someone who has stared death in the face as it draws near and accepted that truth deep in their heart, it might not be a curse. It might be one last blessing.

No—it must be.

At least right now, Jin Taekyung was more grateful than ever that he couldn’t feel pain.

Even with both legs crushed and one arm shattered to pieces, he could still move. It made him so happy he could cry.

*KRAK!*

Where on earth had that strength come from?

Even Jin Taekyung didn’t know.

He’d reached out as if bewitched, as though something were controlling him. The strength in the only one of his four limbs that wasn’t broken had been enough to stop the monster in his tracks.

*I got him…*

Jin Taekyung smiled.

Through his blurred vision, he curled the corners of his mouth at the Blood Lord, who stared down at him with wide eyes.

And then—

*KWA-BOOOOM!*

He felt the enormous roar batter his ears, the dreadful explosion of power shaking everything around him.

At the same time, his heart had settled into a peaceful calm, like a deserted lakeshore.

*This is enough.*

Within the flash that had swallowed his vision, Jin Taekyung murmured to himself.

That was right. It was enough.

He’d done all he could, and he had no regrets.

No—not a single regret.

If even the smallest regret remained, he wouldn’t be able to leave in peace.

He’d cry like a child, calling out the names of the family and friends he wanted to see, blaming himself for failing to see things through.

But now, it was all right.

He had come. Mae Jonghak had come.

With the Martial God—the heavens—gone, the Sword Saint Mae Jonghak was the highest star in the sky and the greatest under heaven in this era.

Taekyung had a vague idea how Mae Jonghak, who should have been protecting the Central Plains by fulfilling his duties as Alliance Leader, could have appeared here. But he didn’t bother to follow the thought.

He was simply grateful for the hope that this unexpected savior could bring down the monster before them and save those who remained.

*Thank goodness. Really.*

Just as Jin Taekyung’s eyelids began to close, with that empty thought swallowed deep in his heart—

*CRACK!*

Amid the fading roar and flash, someone’s hand shot out like lightning and clamped around his throat.

*Drip. Drip.*

A hot, sticky liquid fell onto Jin Taekyung’s forehead.

Above him, the monster’s blood-red eyes still burned.

“How dare… *cough*… someone like you…”

The Blood Lord growled like a wounded beast.

He’d had to swallow mouthfuls of blood just to get those words out, and his body was covered in terrible wounds, some deep enough to expose bone. Yet he was still alive.

Lifting his dying prey like a trophy, he bared his bloodstained teeth again.

“Did you think you could defeat me—me, who inherited his mighty power?”

It was then.

Between Jin Taekyung’s lips, paling under the strength of the hand squeezing his throat, came a faint voice.

“Yeah. You piece of shit.”

“……What?”

“I think I can.”

Jin Taekyung smiled faintly.

At the Blood Lord, staring at him in silence. At those blood-red eyes, trembling ever so slightly.

At the same time, he understood.

There was more in that tremor than anger.

“You’re scared, aren’t you? Of what’s happening right now.”

“……You.”

“Yeah. Even a bastard like you has to be scared. That’s why you’re pulling this cheap hostage stunt.”

At that moment—

*Grind.*

The Blood Lord gritted his teeth without realizing it.

A cheap hostage stunt?

That was complete bullshit.

No—it had to be.

But why?

The Blood Lord couldn’t answer. Instead, the strength in his grasp loosened.

Taekyung’s voice, edged with mockery, drifted into his ear.

“Look around. Then you’ll see whether you’re the hunter right now—or the prey.”

The Blood Lord didn’t answer. He didn’t look around, either.

More precisely, he couldn’t bring himself to.

He didn’t want to admit that he was now surrounded by five Supreme Peak masters led by the Sword Saint.

And he didn’t want to acknowledge that he had grabbed Jin Taekyung to hold them back, if only for a moment, and buy himself time.

*At this rate… I’ll die.*

He could feel it in his skin. Instinct told him.

That cruel truth—something he didn’t want to believe and couldn’t believe—was stabbing into the Blood Lord’s heart.

*Why?*

The Blood Lord couldn’t understand it.

How could the power bestowed on him by his great master have left him in an instant?

It was gone. Every last bit.

The healing power that had been nearly worthy of the name *immortality*, the energy that had surged endlessly from blood.

Only the remnants of his power remained, just enough to keep him standing.

*But I will not die.*

The Blood Lord bit his lips, trembling with shame.

He thought of the last hope he still had—the final hammer blow that would bring this horrific, momentous battle to an end.

“Watch closely. You’ll see who survives here today.”

The Blood Lord muttered the words at Jin Taekyung, who was still smiling.

Then, at last, the hope he’d been waiting for appeared, accompanied by a powerful trumpet call that shook the battlefield.

*Bwoooooo!*

*Rumble, rumble, rumble!*

Countless footsteps shook the earth, followed by enormous flags waving high enough to pierce the sky.

Tens of thousands of troops in all manner of uniforms. The words inscribed on two flags fluttering above them struck everyone’s eyes.

Yangtze River Channel League.

And Green Forest Alliance.

“……!”

“……!”

An unseen shock swept through the battlefield.

“Ah. Ahhh…”

The suicide squad and civilians, who had fought the invaders with everything they had, froze like statues.

“Lord of Heaven!”

The Dark Heaven fanatics, who had kept the battle at a stalemate despite a counterattack backed by overwhelming numbers, chanted the eight-character invocation praising the Lord of Heaven as if entranced.

Just like the Blood Lord, who watched the scene with joy in his eyes.

“Heaven above, all demons bow…!”

A shiver ran down his spine as the Blood Lord turned his gaze toward Jin Taekyung.

He wanted to see the despair on Taekyung’s face as soon as possible—and for as long as possible.

Then, the Blood Lord suddenly realized.

Something was wrong.

That his last hope might have been despair all along.

“An auspicious meeting after the Yellow River runs clear.”

“What… did you say?”

“Someone once sent me a letter saying she’d wait until the Yellow River ran clear. That we’d meet again then.”

Jin Taekyung remembered a letter Wolhwa had sent while he was staying in Gansu.

A single line he’d long since forgotten.

*Hoping that one day, we can meet when the Yellow River runs clear,  
Wolhwa.*

Wearing his brightest smile yet, Jin Taekyung lifted his trembling hand and pointed east.

“Looks like this is the moment.”

More precisely, he pointed to another enormous flag slowly rising behind the two banners at the head of the army.

Through the countless streams of rain falling hard enough to clear the Yellow River, three characters came into view.

Murim Alliance.

“……!”

Then, facing the Blood Lord, who stood frozen, eyes wide, Taekyung played the last card he had.

*KRAK!*

The Blood Lord couldn’t stop him.

He couldn’t stop Jin Taekyung’s teeth from sinking into his neck like a beast’s.

Through the unbearable pain, the world slowly tilted.

*Splatter.*

The monster, stripped of all his power, finally crashed into the pool of blood.
## Chapter artifact 1127

# Chapter 1127

It all began in an instant—and ended in one.

But that brief moment, flashing past like a bolt of lightning, could feel like ten years to someone caught inside it.

*KWA-DRRRK!*

With a grisly sound of flesh tearing, the Blood Lord’s body shuddered.

Hot. Distant.

That was all. That was everything.

*How?*

The Blood Lord couldn’t understand.

Why hadn’t the palm he’d instinctively thrust out toppled his opponent just before those beastlike teeth sank into his neck?

Why was the Murim Alliance’s banner flying over the heads of those damn bandits?

And as he felt his body, no longer under his control, being pushed helplessly backward, he muttered to himself:

*Well, it doesn’t matter anymore.*

*Splatter.*

Sticky blood sprayed. Time, which had stopped, began to move again.

Lying in a pool of blood like a pond, the Blood Lord suddenly looked up at the sky filling his vision.

*Was it always this dark?*

In truth, he already knew the answer.

The world was unchanged. Only he had changed.

The monster’s pupils were still as red as blood, but even now, his fading gaze could no longer make out light from shadow.

A world entirely gone black.

Beyond it, the only things the Blood Lord could feel were the relentless rain pouring down and the chill of blood soaking his entire body.

No. Those weren’t the only things.

Someone’s voice rang in his ears like an echo.

“You… still listening, you son of a bitch?”

Jin Taekyung.

It was him.

He spat out the flesh and blood that had filled his mouth and smiled.

Even as he panted like he was about to collapse.

Even with a face that looked as though it took all he had just to force out each syllable.

“I can hear you. Crystal clear, too.”

The Blood Lord couldn’t answer.

He could only swallow the blood and phlegm bubbling up in his throat and listen to the roar shaking the heavens and earth.

—Destroy the Demonic Path and restore Heaven!

We shall destroy evil and set the heavens right.

It was the old Murim Alliance’s banner, the vow it had upheld to the very end—and the hoof that had trampled its invaders.

Just as it was doing now.

*KWA-DRRRRCK!*

He couldn’t see.

But he could picture it just by listening.

The fanatics wavering in shock at this unexpected turn—and the countless forest of spears and blades closing over them.

The undying will and desperate sense of duty carried by every one of those weapons.

“……Why?”

The Blood Lord barely managed to squeeze out his voice.

He wanted to ask.

Jin Taekyung. All of them.

What were they fighting so desperately for?

What could they possibly hold so dear that they would give their lives to protect it?

Jin Taekyung answered the Blood Lord’s short question, heavy with meaning, with two words even shorter.

“Fuck off.”

“So you don’t want to tell me.”

“I’m sick of it. It’s not like you’re the first idiot like this I’ve met. I’ve gone out of my way to explain before, and none of you ever understood a damn thing.”

“I see. So that’s how it was.”

Jin Taekyung watched the Blood Lord manage a weak nod, then abruptly spoke.

“What about you?”

“What?”

“You. What the hell were you carrying on for?”

The Blood Lord fell silent for a moment, and was startled by his own silence.

Was it the exhaustion weighing down his eyelids?

Or was it the feeling of death closing in by the second?

“……I don’t know.”

His lips, which should have said that everything he’d done was for the Lord of Heaven—that he would do anything for his great master, and swear his loyalty even if he died here and became a ghost—gave a completely different answer.

“I don’t… know anymore. Anything.”

With that feeble mutter, the Blood Lord looked up at the sky.

Where was the heaven he’d trusted so completely, at this very moment?

Would his master, who would hear of the death of his most faithful servant from somewhere far beyond reach, feel even a trace of grief?

*Of course not.*

A faint smile suddenly touched the Blood Lord’s lips.

Right.

He’d only been trying to deny it. He already knew the answer.

When the four Demon Lords and the Demon Empress had died one after another, when news came that countless followers had been wiped out, the Lord of Heaven hadn’t wavered.

Not for a single moment.

He’d acted as though he wanted it to happen.

*Then did you want the death of this lowly servant, too?*

The Blood Lord reached a trembling hand toward the sky.

It was far away. He couldn’t reach it.

Just like the distance between him and the Lord of Heaven.

Just like the relationship that had never drawn any closer, no matter how hard he’d tried.

*Ah.*

The Blood Lord swallowed a groan.

He had believed in and revered the Lord of Heaven—but the light pouring down from that heaven had always shone on only one person.

Even though the owner of those blazing eyes could no longer lift a finger, he was watching the Blood Lord die.

*Jin Taekyung.*

At that moment—

*Shhk!*

The fingertips that had been groping desperately through empty air curled like a hook and plunged downward.

And just as the monster’s strike, filled with anger and hatred whose target he no longer knew, carrying a final sense of duty that seemed almost futile, was about to pierce Jin Taekyung’s brow—

*KRAK!*

A hand, caked in dried blood, blocked the monster’s strike.

It crushed the bones in the monster’s fingers and burned his flesh and blood.

*Hiss.*

A haze rose with the smell of something scorching.

Beyond it, the lips of the old master who had returned to his Disciple’s side parted.

“How dare you lay a hand on him?”

Through the heat that pierced even his dulled senses, the Fire King, Jeok Cheongang, looked down at the monster, trembling in pain.

And it wasn’t just him.

The Bow Saint and Slaughter Saint. Sword Saint Mae Jonghak and Cheongpung.

Along with them, several others who had rushed over, covered in blood.

They surrounded him like the God of Death—or an iron tower.

Blocking out the entire sky that had been the monster’s whole world.

Becoming a broad, sturdy roof that sheltered someone else from the rain pouring down on them.

That was why Jin Taekyung could laugh aloud.

Remembering the monster’s cry of joy just moments ago.

“Can you see?”

He spoke emphatically to the monster, its blood-red eyes wide open.

“The faces you’re looking at right now—that’s the paltry heaven I believed in.”

“……!”

What could he say?

What more could he do?

The monster blinked helplessly.

He swallowed the blood that kept spilling over his lips and summoned all his strength to force out the words.

“Rejoice… all you want. This will be the last time.”

And through the vision darkening like pitch, Jin Taekyung’s voice rang faintly in his ears.

“I was planning to.”

As a bitter smile touched Jin Taekyung’s lips, the monster’s final breath dispersed into the air.

*Ding.*

A clear chime rang out like the bells of an ancient cathedral, announcing that everything was over.

It carried boundless joy—and even greater sorrow.

* * *

There’s a saying.

Animals leave their hides behind when they die, and people leave their names.

But monsters that are neither animal nor human can leave behind a massive amount of EXP.

*Ding. Ding. Ding.*

The familiar clear chime rang nonstop in my ears.

If everyone could hear it, not just me, I bet it would’ve carried for hundreds of miles.

*That bastard sure knew how to make an exit.*

The Blood Lord’s end was miserable and shabby, but the System’s payouts were lavish.

How many times had I leveled up in that short instant?

Three times? More?

I wasn’t sure.

What I did know was that several Quests had been completed when the Blood Lord died, and I’d turned off notifications after my third Level Up.

*If this were any other time, I’d have passed out from happiness.*

No, I definitely would have.

Leveling up several times in a row, when it had only happened once in a blue moon for a while now, was nothing short of a miracle.

But none of it meant anything to me now.

The chimes, which should have sounded like heaven, were nothing but irritating noise. The recovery of my flesh and bones, all crushed and broken, offered only a little comfort.

The small, final comfort of being able to pat someone’s trembling shoulder.

“Quit bawling. Your dick’ll fall off.”

Cheongpung didn’t stop crying, despite my attempt to comfort him.

He could only speak through his sobs.

Saying he was sorry. Saying thanks again.

But my farewell to Cheongpung, which was surely going to be our last, was brief.

Unlike him, I still had so many last faces left to see.

And at the end of them, my real final moment would be waiting for me.

**Time Limit: 5 minutes 35 seconds**

I calmly looked at the hourglass of Final Rally, still suspended in midair.

Truthfully, I’d already guessed.

To be precise, ever since the moment I’d launched One Annihilation at the Blood Lord.

There was a limit to how much a Level Up could heal, and the injuries I’d suffered from the backlash of One Annihilation went beyond that limit.

Now that what was called innate qi—or original true qi—had been damaged, my fate was like a boat that had crossed a river with no way back.

*The System warned me, and I accepted it.*

That was all.

I’d simply taken the next step I needed to take, even if death was waiting for me.

Because I’d already made peace with it, I was even grateful for my situation now.

If I hadn’t recovered through the Level Ups, if they hadn’t extended the time I had in Final Rally, I wouldn’t have been able to say my final goodbyes like this.

*If that’s what happened, then it was enough.*

The Blood Lord was dead, the Dark Heaven army had crumbled, and I’d been granted a few precious extra minutes.

And now I was smiling at faces I’d thought I’d never see again.

Like a peaceful day with no enemies left to defeat and no one precious I had to protect.

Just like this moment.

Yeah.

I was ready to leave.

I definitely had to be.
## Chapter artifact 1128

# Chapter 1128

If I’d let myself think for just a little longer, I might have started crying without meaning to.

I knew better than anyone that I wasn’t ready to leave yet.

But the time I’d thought was endless was inching toward its end even now, and I forced the corners of my mouth upward.

For my sake.

And for the sake of those who would remain, and remember my final moments for a long time.

“Oh, you’re here?”

Personally, I thought it was a very convincing performance.

A smiling face. A calm voice.

But the Fire Dragon Pavilion members, reunited with me at last, weren’t foolish enough to miss what my condition and the heavy silence around us meant.

“……Pavilion Master.”

There was nothing more to say.

Sama Pyo stared at me blankly, then bit his lip. Song Ilseom quietly closed his eyes, and a cloudy film of tears welled in Taishan’s enormous eyes.

And Ju Hwaran—

*Squish. Squish.*

She staggered across the pool of blood spread like a lake and buried her trembling head against my shoulder.

That was all.

There were no more words, but it was enough for me.

*They’re all alive.*

My ominous hunches were never wrong, but this time, they’d been the exception.

As I confirmed they were safe, I felt my stiffened smile soften.

*Thank God. Really…… thank God.*

The smile on my lips now wasn’t an act anymore.

Gung Gibang and Cheongheoja appeared after the Fire Dragon Pavilion members.

Even the face of that wild-haired weirdo who gave me a headache every time I saw him made my heart swell with relief.

No—maybe it wasn't Great Sir himself I was so glad to see, but the person on his back.

“Don’t worry. He suffered a serious Internal Injury, but the Seafaring King got the stagnant blood out in time. His life isn’t in danger.”

At the voice that suddenly reached my ears, I gave a small nod instead of answering.

Hyuk Mujin had lost consciousness, covered in blood from head to toe, but I could trust those words a hundred times over.

They came from none other than a man worthy of being called the greatest under heaven in this age.

“Swift Wind Sword Hyuk Mujin fought magnificently. He never gave an inch. He stood his ground with pride.”

Sword Saint Mae Jonghak added in a low voice.

“Just like you.”

At the sincerity in his words, I parted my blood-crusted lips.

“Yes. I’m sure he did.”

I looked at Hyuk Mujin and smiled faintly.

“He’s my right arm, after all.”

Mae Jonghak had been watching me with a deeply solemn gaze. Then he smiled along with me.

“So that’s how it is.”

“But he probably doesn’t know.”

“Why not?”

“I was always giving him a hard time. Told him he wasn’t nearly good enough to be my right arm.”

If there’d been even the slimmest chance I could recover, Mae Jonghak would’ve answered without hesitation.

*Tell him yourself when you get the chance.*

*Hyuk Mujin would be happy to hear it.*

But like the Slaughter Saint and Bow Saint, who stood with clenched jaws, he knew I didn’t have much time left.

“When he wakes, I’ll tell him. Every word you just said. I won’t leave a thing out.”

“He’s so starved for praise that you can exaggerate all you like. Like……”

A conversation I’d had with Hyuk Mujin a long time ago came to mind, and I let out a quiet laugh.

“He has what it takes to become the next Alliance Leader. Yeah. That’d make him faint with joy.”

“The next Alliance Leader, you say? I have much to reflect on. To have my successor right in front of me and not recognize him.”

“I’ll let it slide this time. You saved everyone, after all.”

“No. That’s not right.”

*Tap.*

With a firm voice, Mae Jonghak placed a hand on my shoulder.

“It wasn’t me who saved everyone. It was you. And them, too.”

“……!”

“Look. Listen. See who they’re fighting for—and whose name they’re shouting.”

At that moment—

*Fwoooosh.*

Warm energy flowed from the tips of his fingers resting on my shoulder and seeped into my body.

Like the sunset, it roused my consciousness as it sank into darkness, showing me the fanatics crumbling apart and the shouts of our allies sweeping over them like a wave.

A roar that swallowed the fierce wind, the rain, and even the eight-character maxim.

—Fight back! For the Blazing Flame Divine Dragon, Jin Taekyung!

Banners soared so high they seemed to pierce the sky, whipping wildly in the wind.

A forest of glittering steel covered the city and advanced, raising red flowers as it went.

Murim warriors, government troops, and commoners.

Three forces as incompatible as water and oil had blended into one, piercing the invaders.

Everyone was shouting my name.

With a desperate will and resolve that drowned out even the fanatics’ madness.

“……!”

My body trembled before I knew it.

As a bolt of lightning-like shiver ran up my spine, Mae Jonghak’s voice drifted into my ears.

“A month ago, when I went to persuade the Seafaring King, he told me that ships couldn’t sail through a storm. The sails and oars would break, and there wouldn’t be a single glimmer of light. You wouldn’t even know which way was forward or back.”

At last, the age of war had come.

The sun of peace that had shone brilliantly over the land for more than fifty years had disappeared, and night had fallen with the dark clouds of Dark Heaven, black as pitch.

The darkness was deep enough to shake even the two giants of the dark path, who had once fought the Hundred Thousand Demonic Disciples led by the Heavenly Demon.

“The Green Forest Battle King said much the same thing. They were afraid of Dark Heaven’s power, and spies planted in their ranks long ago had urged them to submit in order to survive.”

But what I saw now was the exact opposite.

*KRA-DRRRK!*

Two streaks of red and blue Force flashed so fiercely I could make them out even from here.

At the heart of those vast energies, cutting down fanatics without mercy, were two Supreme Peak masters who ruled the mountains and rivers of the land.

“Yes, I did manage to persuade them. And it was easier than I expected.”

“How on earth?”

“It was just like the Great Faction War. All they needed was someone to believe in, someone who could move forward with them—a single ray of light.”

I didn’t know.

That past had long since faded into the distant years.

And yet, I could still guess.

I knew what light had shone through the darkness of the Great Faction War.

That was probably why my eyes widened without my meaning to.

That brilliant light, which had illuminated an age of war, had disappeared long ago.

“……No way.”

I looked at Mae Jonghak, smiling faintly, and asked as if groaning.

“Has the Martial God returned?”

At his answer, a hot, sudden swell rose from deep in my chest.

“No. But you were here.”

“……!”

“One who goes ahead of everyone else to light the way. Someone who can bring everyone together because he isn’t bound by status or formality. That’s why you are the Blazing Flame Divine Dragon and Prince Shangshan—but before either of those, you’re a human being.”

His voice, reciting the words like a poem, spread across the battlefield.

At the same time, countless footsteps trampled through the pools of blood left by the invaders, and dazzling spears and blades lit up the darkness.

The darkness was fading.

The flame inside me was fading, too.

But the shouting didn’t stop.

Everyone in Xining was still screaming my name until their voices broke.

As if mourning my death, just around the corner.

“Thank you. And I’m sorry. For coming too late. For failing to protect you.”

Mae Jonghak said much the same thing as Cheongpung had, and cried in the same way. Then he had no choice but to turn away from me.

He was the Alliance Leader.

He had the duty and responsibility to end this damn battle even a moment sooner and save as many lives as he could.

No.

Maybe he was sparing someone.

Someone who stood a few steps behind me, frozen in body and spirit, silently watching everything.

“What’s so amusing?”

His voice was so cold it seemed at odds with his title, the Fire King.

But I knew better than anyone that his anger was aimed at himself.

And I knew that the only help I could offer him, as his heart bled tears, was to smile.

“What, I’m not even allowed to smile when I feel like it?”

“I can tell you’re forcing it.”

“……Is it that obvious?”

“Yeah. Look at the state you’re in.”

“I can’t see myself. Why don’t you bring me a mirror?”

“Do you need one? You’re covered in blood from head to toe, grinning like some evil spirit.”

“Like you’re in any position to talk.”

Jeok Cheongang and I fell silent.

Then, as if we’d planned it, we smiled at the same time.

We knew it was the only thing that might comfort each other, even a little.

Of course, we could tell from each other’s eyes that it was forced.

“I can definitely tell you’re forcing that smile.”

“It isn’t easy.”

“No. It isn’t. When I look back, nothing ever has been.”

I murmured weakly and looked at Jeok Cheongang.

The translucent hologram window was still there in the corner of my vision, no matter which way I turned my head.

> **System**
> **Time Limit:** 59 seconds

“Old Master.”

“Speak.”

“Do you think there really is an afterlife?”

“There must be. No—there definitely is.”

“How do you know?”

“Hong Dao said so. The great Abbot of Shaolin Temple said it, so you’d better believe him without arguing.”

“Come on. You’re always dismissing him as a drunken monk.”

“This time, I’ll choose to believe him.”

“Why?”

“……There has to be an afterlife for us to meet again.”

> **System**
> **Time Limit:** 30 seconds

“I don’t mind if it takes a long time. Just try to take as long as you can.”

“It’ll take quite a while regardless. There are too many people I need to kill.”

“Now that you mention it, you’re right. You know, that gives me an idea.”

“What is it?”

“Once you’ve killed those sons of bitches, I’ll be waiting in the afterlife. I’ll kill them one more time.”

“Unacceptable.”

“What? Why not?”

“You only need to beat them to within an inch of their lives. Then we can kill them together once more.”

“Wow. Are you a genius?”

“I suppose I was close to a natural disaster.”

> **System**
> **Time Limit:** 15 seconds

“By the way, Old Master.”

“Hmm?”

“I think I’m getting sleepy.”

“……Yeah. You must be exhausted.”

“I’m sorry, but could I ask you for one favor?”

“I’ll grant it. Anything.”

“I have a family. They’re not here. So I don’t think I’ll get to see them now.”

> **System**
> **Time Limit:** 10 seconds

“If you happen to meet them someday—though I know that probably won’t happen—could you tell them how I’m doing?”

“What must this old man do to reach the realm of immortals where you once stayed?”

“I’m not sure. Ascend to immortality? I don’t really know.”

“Understood. I’ll find a way, whatever it takes. But you must grant this old man one favor in return.”

“Tell me.”

> **System**
> **Time Limit:** 5 seconds

I blinked weakly.

Beyond my blurring vision, I saw Jeok Cheongang crying like a child.

“Please…… can’t you stay alive?”

As the darkness swept toward me, I answered.

“I’m sorry, Master.”

> **System**
> **Time Limit:** 1 second

And then the entire world surrounding me closed.
## Chapter artifact 1129

# Chapter 1129

Looking back, I think I’d wondered about death from the time I was very young.

That didn’t mean I was particularly precocious, of course.

I was just curious.

Why was the amusement park I’d been promised a trip to if I got a perfect score on my spelling test blazing on the TV screen?

Why was there a pure white bouquet on the desk of the classmate who’d played with me just yesterday?

It didn’t take long for me to learn the truth.

Death, destruction, grief, and anger.

Hunters and monsters. Gates left all over the world. A war that still hadn’t ended.

That was all. It was just the kind of era we lived in.

An age of chaos, where truths so vast and terrible that nothing could stop them kept spilling out without end.

I quickly came to understand what it meant when my parents changed the TV channel with grim faces, and what the pure white bouquet on my friend’s desk meant.

But my kindergarten teacher’s choice to call my friend’s absence a “long journey” left me with even more questions.

That it was a grown-up’s way of showing consideration didn’t change the fact that one thought led to another, then another.

Why do people die?

Where do they go after they die?

If they really have gone on a journey, does a world beyond death truly exist?

Even after a long time had passed, there was no one who could answer those questions for me.

Of course there wasn’t.

The departed don’t speak.

So I wanted to find the answer from someone who had died, but wasn’t dead anymore.

“Hey, Golgoli.”

“A mere human like you dares call me by such a vulgar name? Can’t you see this radiant crown?”

“Want me to make it so you can’t see anything at all?”

“……Why did you call me? Get to the point.”

I’d secretly believed that Bones—or rather, the Skeleton King—could answer the question that had haunted me for so long.

But faith was often betrayed.

“The afterlife? I don’t know why you’re asking me.”

“Does that mean—”

“That’s right. I don’t know a thing. I don’t remember my life before death, so why would what came after be any different? I just woke up in the dark like this.”

It was ironic.

Even an undead being who had already crossed death’s threshold and been reborn didn’t know what lay beyond it.

In the end, I gave up on finding an answer.

Or, more precisely, I put it off.

I’d learn someday.

Whether I wanted to or not, that thing called death would hide in the shadows, biding its time, then swallow everything whole.

Just—

Like this very moment.

Ssshhh.

Everything blurred and drifted away.

The sky that had only just begun to clear. The faces looking down at me.

The wails they poured out, the shouts of battle that still hadn’t faded.

The past I’d struggled through. Fleeting moments I’d let slip by without a thought.

All of it.

*Ah.*

With no voice left to escape my lips, I sank weakly.

Into pitch-black darkness.

Into the swamp of death, pulling hard at my soul.

And in a gap in time that felt like eternity, I heard someone’s voice echo as if in a hallucination.

—Open your eyes.

At that moment—

Whooosh!

A beam of light appeared from nowhere, somehow, tearing through the darkness and illuminating the world.

A new world, where everything had changed.

* * *

I blinked blankly.

Then, looking at the sight spread out before me, I wondered:

*Where am I?*

It was a vast space—or no, so boundless that even “vast” didn’t begin to describe it. An expanse of grayish white stretched without end.

The horizon, drawn far in the distance, was hazy. When I looked up, there was a ceiling overhead, higher and more distant than the sky.

It felt as if I’d been shut inside a gigantic box.

But strangely, I wasn’t afraid.

This empty, infinite space was enough to stir some unknowable awe just by looking at it.

That’s right.

The answer to the question I’d carried for so long was here.

Though it looked nothing like I’d imagined.

“Hmm. That can happen.”

“……!”

A voice came from behind me without any hint of someone’s presence. I instinctively twisted away and retreated, fixing my gaze on the uninvited guest standing only a few steps away.

“……You’re—”

I had no time to be surprised by the new discovery that I could speak.

The unexpected visitor—or rather, the old man—was a far greater shock.

Unlike me, the old man spoke calmly.

“Do you know who I am?”

I nodded and answered as evenly as I could.

“The Grim Reaper?”

“……”

“Uh, no?”

After a brief silence, the old man shook his head.

“Think whatever you like. It isn’t important.”

“But it’s pretty important to me.”

“Why? Worried you’ll be dragged to hell?”

“Honestly, yes.”

“You must have sinned a lot.”

“……Who knows?”

I gave the old man, whoever he was, a bitter smile.

I’d sometimes wondered if every enemy I’d defeated really deserved to die like that.

If the pile of corpses and river of blood I’d built with these two hands could be balanced out by the lives of the people who’d survived because of me.

*Maybe I’m the one who deserves to go to hell more than anyone.*

That was when—

“You’re worrying over nothing. It’s not so easy to get into hell.”

The old man’s sunken gaze settled on me.

As if he could see right through my thoughts.

“And the people you miss won’t be there, either.”

“……!”

“Isn’t that what worries you most? That even after you die, you won’t be able to see them.”

For a moment, I couldn’t speak. I stared at him, frozen like a statue, then barely managed to squeeze out a voice.

“Wait. Is this, by any chance—”

“Ah, forgive me. I didn’t mean to let that slip.”

His answer was as good as an admission that I’d guessed right.

The old man shrugged at me as I struggled to find the words.

“Well, that’s how it is.”

“I knew something was off. So it really was true.”

“It happens more often than you’d think. When the thing you thought couldn’t happen does. It’s easier if you think of it as just one of those cases.”

There was no way to make it simple or easy, but for some reason, I could accept it all surprisingly quickly.

Even who owned that voice, the one that had sounded like a hallucination just before I opened my eyes in this strange place.

“You’re quick on the uptake. That’s good.”

I looked anew at the old man, who now read my thoughts as naturally as breathing.

A spotless robe, not a speck of dust on it. A beard grown so long it reached the floor.

And, for some reason, a feeling of familiarity.

“Have we…… met before?”

The old man seemed to ponder the question for a while before answering.

“We may have. Or we may not have.”

“Excuse me?”

“This is the best answer I can give you. I have my own circumstances, you see. I’ve already pushed myself quite far to help you.”

“You helped me? How?”

“Find the answer to that question yourself. You don’t have as much time as you think, so…… let’s get started.”

I wanted to ask the old man what on earth he was talking about, and what he meant by getting started.

But the instant the old man’s figure blurred, it was enough to wipe all the tangled thoughts from my mind.

Pop.

I didn’t see him move. I didn’t even feel it.

He was fast enough to leave no afterimage.

By the time I turned around, the old man had crossed the few steps between us and gotten behind me. His punch was already filling my vision with black.

Thud!

My vision swam, and strength left my legs.

I’d never seen an attack so fast and precise.

But even though I had no reason to fight anymore, I forced my buckling legs to hold and reached out on instinct.

Whoosh—BOOM!

Indigo flames engulfed the gray-white space.

Before I could even wonder why I still had internal energy, the old man’s characteristically calm voice rang out from beyond the scorching heat.

“The Flame Divine Palm. An excellent martial art.”

“……How do you know that?”

“Didn’t I tell you? Keep it simple and accept it.”

Whooosh.

The flames split as he answered.

Without even forming Palm Force, the old man waved a hand and blew away the heat of the Flame Divine Palm as if snuffing out a candle. Then he signaled to me with his eyes.

“Now, fight back all you like. The Flame-Extinguishing Divine Fist would do, or the Blazing Flame Divine Spear would be even better.”

“……!”

“Ah, but leave out One Annihilation. For your sake, not mine.”

Was this what it felt like to be haunted by a ghost?

I could only stare at the ghost—or rather, the old man—in a daze, unable to speak.

Of course, the old man didn’t even allow me that moment.

Slash!

When had he moved? How?

The old man, who’d been standing amid the dying flames, had already slipped into my blind spot. The invisible qi in the edge of his hand swept smoothly across my chest.

So sharp that a beat later, the flesh it sliced through—like tofu—let out a scream.

Blood sprayed into the air. At the same time, a distant pain I’d thought I’d never feel again came surging back.

Along with the fear I’d briefly forgotten.

*At this rate…… I’ll die.*

It was bizarre.

I’d already died once, and yet here I was, thinking about dying again.

But I had no time for questions like that.

I had to fight back with everything I had against that overwhelming power, powerful enough to erase not just my body but my soul.

“Good. That’s right. Looks like you’re finally starting to understand the situation.”

The old man nodded, seeing right through my thoughts. A curse slipped out before I could stop it.

“You crazy old bastard.”

“High praise. Thank you.”

“What…… the hell are you?”

“Who knows? I might be your grandfather.”

The old man smiled faintly for the first time. Then he reached out toward me, leaving me speechless at the unexpected family insult.

No—more precisely, he held something out.

A spear that had suddenly appeared in midair.

“Take it. Even if you’re going to die, you should at least get to fight back properly once, shouldn’t you?”

Gritting my teeth, I grabbed the shaft as the spear flew slowly across the space toward me.

Then I spoke through clenched teeth.

“You’re dead.”

The old man replied:

“May you be reborn in paradise.”

At that moment—

Ssshh!

A dazzling flash of light streaked across the vast gray-white space.

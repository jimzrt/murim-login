# Checkpoint Review — 1130–1134

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

# Chapters 1130–1134

## Plot

In the gray-white space, the Helper pushes Taekyung to perceive an invisible attack with the Mind’s Eye, then gives him an unknown gift and sends him back. Taekyung’s heart restarts; after Bone Transformation restores his body, he awakens and tells Jeok Cheongang he kept his promise. The allied forces celebrate victory over the Blood Lord and Grand Mage, but Taekyung realizes Ma Sanbao is preparing an attack on the Central Plains through the Moving Formation at Mount Kunlun. Mae Jonghak forces Taekyung to rest while Ma sets out with his subordinates.

Ma changes his plan to attack Henan and Shanxi with roughly five thousand troops, including three thousand monsters. Zhuge Feng’s ambush at the Magic Formation’s destination kills about two thousand of Ma’s followers. Baek Yeon and the Son of Heaven confront Ma, who is unable to move; the chapter ends without revealing the outcome.

## Continuity

- Taekyung recovered after Bone Transformation and awoke. The Helper gave him an unidentified gift, then remained by choice in the enduring gray-white space.
- The allied forces defeated the Blood Lord and Grand Mage. Ma Sanbao remained at Mount Kunlun, intending to attack the Central Plains through the Moving Formation.
- Ma’s changed plan targeted Henan and Shanxi. Roughly two thousand of his troops died in Zhuge Feng’s ambush; Ma and about one thousand followers survived in a remote Henan valley.
- Ma was unable to move when Zhuge Feng, Baek Yeon, and the Son of Heaven confronted him. His fate is unresolved.

## Translation Decisions

- Render the Helper’s title as “the Helper” and 심안 as “the Mind’s Eye.”
- Render 환골탈태 as “Bone Transformation,” 이동진 as “Moving Formation,” 선천진기 as “innate qi,” and 점혈 as “Pressure-Point Strike.”
- Render 강시술사 as “corpse sorcerer” and 마법진 as “Magic Formation.”

## Durable state

{
  "active_continuity": [
    "The Helper gave Taekyung an unidentified gift and chose to remain in the enduring gray-white space, awaiting an unknown end.",
    "Ma Sanbao and roughly one thousand followers survived Zhuge Feng’s ambush in a remote Henan valley; Baek Yeon and the Son of Heaven confronted him while he was unable to move."
  ],
  "continuity_sources": [
    1133,
    1134
  ],
  "open_questions": [
    "What did the Helper give Taekyung?",
    "What will happen to Ma Sanbao after the Son of Heaven confronts him?"
  ],
  "safe_through": 1134,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1130

# Chapter 1130

Light doesn’t exist only to illuminate.

Sometimes it wipes everything away and lets you forget.

Just like the beam of light flying toward Jin Taekyung at this very moment, covering his vision in pure white.

Whoooooosh!

As the flash swelled, Jin Taekyung’s gaze sank low.

He cleared every stray thought and question from his mind.

No—he had no choice.

Dozens of beams had split off and were writhing as if alive, aiming for the vital points all over his body.

*It’s no feint.*

He could feel it instinctively.

Every one of those solid beams held terrifying destructive power unlike anything he’d ever experienced.

But Jin Taekyung chose to advance, not retreat.

Fwoosh—BOOM!

Flames streamed along his feet as he thrust them forward.

Keeping low, he darted through the downpour of flashes, narrowly evading them. The old man watched him and nodded.

“The Flamefire Path. You certainly know how to fight.”

Jin Taekyung answered the old man’s praise in his own way.

Ssshh.

Across the space closing in an instant, his spear surged toward the old man, engulfed in afterimages and rippling like a wave.

Like the tail of a colossal dragon.

Whoooosh!

Indigo flames blossomed along the spearhead.

Just like the old man’s move moments earlier, the flames split into dozens in an instant, blanketing the space as they surged forward.

KWA-BOOM!

If a hell where sulfurous flames boiled were real, would it look like this?

Yet even before that awful, lava-like heat, the old man’s calm eyes didn’t waver in the slightest.

Nor did his hands as he brought them together to meet the spearhead amid that life-or-death crisis.

Crack!

For an instant, Jin Taekyung’s eyes flew wide.

Between the old man’s palms, pressed together as if in prayer, the spearhead trembled. Jin Taekyung saw it in his own eyes.

“……How?”

The question slipped out before he knew it.

But the old man had blown away every flame aimed at him with a single joining of his palms. He answered with a puzzled expression.

“Hm? I just grabbed it.”

“……!”

“Anyway, try something hotter this time. This is making me pleasantly drowsy. Not bad.”

Jin Taekyung felt his vision swim.

The old man was already a madman for stopping his full-power strike with Empty-Hand Seizes the Blade. And now he was treating several jiazi of Scorching Yang Qi—hot enough to melt steel—as if it were hot spring water.

*What kind of old man is this?*

Even the Blood Lord, the strongest opponent he’d faced until now, hadn’t come close.

Not even remotely.

The Blood Lord had used blood as a source to gain near-Regeneration and endless internal energy. But even that terrifying power had its limits.

The old man was different.

His very nature, his level, was different from the Blood Lord’s.

There was no particular killing intent in his eyes, as tranquil as a secluded lake. Yet something about him froze Jin Taekyung from head to toe just by being there.

It felt like facing an enormous wall he could never climb, no matter how desperately he struggled.

And the old man was looking straight into that brief thought that had flashed through Jin Taekyung’s mind.

“Your head’s full of stray thoughts. You must still have some life left in you. In that case……”

At that moment—

CRASH!

The spearhead in the old man’s grasp shattered to pieces, and his palm glided forward to touch Jin Taekyung’s chest.

BOOM!

An explosion rang out from deep within his body.

Jin Taekyung dropped to one knee, pain bleaching his vision white.

At the same time, amid the ringing in his ears, the old man’s whisper came through with unnerving clarity.

“I’ll clear those stray thoughts away for you again.”

“……!”

Jin Taekyung wasn’t given time to answer—or even to steady himself against the pain.

More precisely, the old man didn’t wait.

Whoosh!

A massive force descended toward his crown, accompanied by a heavy rush of air.

The energy wave was so terrifying it made him forget even the pain. Jin Taekyung rolled to the side without time to think.

KWA-BOOM!

A shock wave swept the surroundings after a roar like the sky splitting apart.

Jin Taekyung felt himself thrown far away, as if weightless. Behind him, the old man appeared, having crossed more than ten jang in an instant.

“That was a good decision. If you hadn’t used Narye tagon, it would’ve been over right there.”

Normally, Jin Taekyung would have told any enemy standing before him to shut the hell up.

But this time was different.

His whole body had reminded him that facing the old man made even a single deep breath—or the smallest stray thought—a luxury he couldn’t afford.

“You only just figured out something that simple?”

……And that so long as this mysterious old man could see right through his mind, he’d never escape this damned situation.

“Oh, that’s quite an insight. So what will you do now?”

Meeting the old man’s interested gaze, Jin Taekyung used the spear, now nothing but a shaft, as a cane to get back to his feet.

Slowly, and carefully.

And when he finally stood upright on both legs, he found his answer.

Ssshh.

His eyes closed without warning.

The thought that it was madness, the fear of what might happen—both lasted only a moment.

His trembling eyelids soon grew still. His vision was already dark, shutting out the information his eyes had been sending him.

By giving up one important thing, Jin Taekyung had gained something new.

The thread of enlightenment left unfinished during the fierce battle against Dark Heaven.

And the only way to overcome the situation he was in now.

Seeing Jin Taekyung like this, the old man once again wore a faint smile.

“Yes. That’s how it should be.”

At that moment—

Pop.

As if on cue, the young man and the old man shot toward each other.

Fwoosh—BOOM!

As if entranced, Jin Taekyung thrust out the Flame-Extinguishing Divine Fist.

Heat that seemed capable of melting even a thousand-year-old boulder swept through the gray-white space. But he already knew.

He could feel it, too.

The old man was no longer where he’d been.

He was moving faster than sound, slipping into Jin Taekyung’s blind spot.

BOOM!

Jin Taekyung twisted like lightning. A powerful palm strike slammed through the air where his head had been a moment earlier.

“Much better.”

In the darkness of his vision, Jin Taekyung barely dodged the old man’s attacks as they kept closing in from every direction, swallowing a breath.

Was it just his imagination?

The old man’s voice, once clearer than anything else, had grown more distant and faint than an echo.

“The fact that you can still hear me means you’re not there yet.”

He was right. Maybe.

It wasn’t anything new.

It had always been like this.

He hadn’t been strong enough to protect everyone, and the guilt and anxiety that followed had given him nightmares deep into the night.

He’d wavered like a candle in the wind, then finally gone out without a fight.

“But that is greed. Humans cannot become perfect.”

Jin Taekyung knew that, too.

But even if it wasn’t mere desire but greed, he didn’t care.

He’d only wanted to save someone—and to live himself.

He’d simply wanted to live in a more peaceful world, together with the people he cherished.

“Everyone dreams of that, though reality is cruel.”

Despite his calm voice, the old man kept pressing Jin Taekyung.

A foot that bent like a whip, a hand blade that slashed diagonally, a palm that thrust forward smoothly—all were swords and spears.

None of those moves carried any deep killing intent, yet each overflowed with an energy that seemed capable of erasing not just his body but his very soul.

“Who knows? Perhaps entering perfect rest just like this would be a good thing for you.”

That was when it happened.

Jin Taekyung’s retreating steps came to a sudden stop, as if nailed to the ground.

KWA-BOOM!

Two fists collided in midair.

The impossibly wrinkled old man’s fist carried a force almost too great to withstand, but Jin Taekyung braced himself even as his feet slowly slid back.

“What do you mean by that?”

The old man answered Jin Taekyung’s question, forced out between clenched teeth, in a calm voice.

“Tell me. What do you think I mean?”

“……You can’t be saying—”

“Good. It seems you already know. We’re out of time, so let’s settle this now.”

Just as Jin Taekyung was about to ask what he meant, the old man’s fist gathered more force and shoved him away.

KWA-BOOM!

His body shot backward like a cannonball.

Jin Taekyung barely regained his balance in midair. The moment he landed, he felt the space around him resonate.

Hmmm.

He couldn’t see it. But he could picture it.

Far away, an invisible sword pointed straight at him.

The old man holding it—not a blade, but something made entirely of energy.

“Try to dodge it. If you can’t…… then this is as far as you go.”

Jin Taekyung couldn’t ask what the words meant.

No—he couldn’t even bring himself to open his eyes.

He felt that if he lost the sensation he’d barely managed to grasp, even for an instant, or if the slightest stray thought crept in, his whole body would be torn to pieces.

And that judgment was right.

Gooooong.

The gray-white space trembled as the old man’s hands slowly rose.

At the same time, a faint beam of light flowed into some corner of Jin Taekyung’s pitch-black vision.

*What is this?*

A sensation he’d never felt before.

Or rather, it had come to him only very rarely after he combined three forms of internal energy, lingering briefly before fading.

It belonged to a realm where reason didn’t exist—pure instinct.

A realm where the body moved before the mind could give an order. No, somewhere beyond that.

It was taking hold of Jin Taekyung’s mind, touching on the sixth sense.

At last, he stared straight at the invisible sword slashing down from the old man’s fingertips.

Sssshing!

At the instant a sound like the whole world splitting apart rang out—

Whoooosh.

Jin Taekyung saw it.

A single beam of light, brightening his vision as dark as the deep night.

And at the same time, he stepped forward as if entranced.

Shhk!
## Chapter artifact 1131

# Chapter 1131

In the silence of time brought to a halt, I slowly lifted my eyelids.

It was a strange feeling.

My mind was hazy, as if shrouded in thick fog, yet my vision was clearer than ever.

Clear enough to make me wonder if all of this was a dream.

But the low voice that reached my ears a moment later was enough to remind me that this moment was no illusion.

“Did you see it?”

I raised my head and stared blankly at the old man.

Then, recalling the formless qi that had flown across the space moments ago, cleaving it in two and missing me by no more than a thread, I parted my lips.

“Yes. I saw it.”

Everything felt natural.

The respectful way I had begun speaking, and the old man’s acceptance of my attitude as if it were only right.

“What did you see?”

“A beam of light. A line.”

The old man stroked his snow-white beard, which hung down to his knees.

“How could that be? It must have been formless.”

“It had a form. For that moment, at least.”

“Even with your eyes closed?”

“I didn’t see it with my eyes.”

“You saw it, but didn’t see it. Then what was it?”

“That…”

I suddenly found myself at a loss.

Not because I didn’t know the answer to the old man’s question, but because the thought that had flashed through my mind as soon as I heard it seemed absurd even to me.

But my silence was as good as an answer.

The old man’s gaze, whose depths I couldn’t begin to fathom, was already looking into my heart.

“People often have the truth right before their eyes and still fail to believe it, passing it by. A truly regrettable thing.”

Step.

One step.

With that single stride, the old man erased all distance between us and whispered to me.

“You saw what cannot be seen, and avoided what cannot be avoided. So why can’t you believe what you yourself did?”

“……!”

“Sit in meditation.”

My mind was still hazy as if in a dream. I followed the old man’s words as if entranced and sat down.

Then I heard his voice, no longer ringing in my ears but inside my head.

—Clear your mind like a stream. Keep your focus, and let yourself go with the flow.

Suddenly, I felt as though I’d heard something like this said before, somewhere.

But the brief thought that crossed my mind vanished along with my consciousness as it sank deeper and deeper.

Fwoooosh.

Light and darkness flickered endlessly before my eyes, throwing everything into confusion.

In that distant chaos, I forgot everything.

Where I was. Who I was.

And yet the voice coming from somewhere was astonishingly clear.

—Remember once more. What you saw. The sensation of that moment.

I took a slow, deep breath.

At the same time, I murmured in my mind the name of the thing that had no shape, color, or scent.

*Qi.*

It was everywhere and nowhere.

The source and seed of all things in the world.

That was right.

For a brief moment, I had seen its true nature clearly.

Through a new realm that lay beyond the senses.

And the owner of the voice echoing deep within my soul was no different from someone who had already set foot in that realm.

—I’ll ask again. What did you see it with?

Right.

I still hadn’t answered the old man’s earlier question.

But this time, I could answer without hesitation.

I found the other eye hidden within me, the one even I hadn’t believed in.

*My heart. No…*

The Mind’s Eye.

At the moment those two words finally came to me and were branded into my mind—

—As always, you’ve made a good decision.

Flash!

Along with the old man’s low voice, the light and darkness that had been endlessly clouding my vision scattered.

Or rather, everything surrounding me did.

“Ah.”

I exhaled the breath I’d been holding and looked around.

Crack. Crack.

Why was this happening?

How could such a thing be possible?

The vast, endless gray-white space was shaking.

Cracks spread in every direction like a pane of glass about to shatter, and the figure of the man standing beyond it twisted along with the shifting space.

“Don’t be alarmed. The time we were granted is simply coming to an end.”

In contrast to the unbelievable sight before me, the old man’s tone was calm and composed.

I stared at him as if entranced.

Then, recalling a fragment of a memory I’d long forgotten, I finally spoke.

“I’ve met you before. I’m sure of it.”

The old man smiled faintly.

“Is that what you think?”

It was neither a yes nor a no.

But at last, I was certain.

Though the gray-white space and the old man looked different from how I remembered them, their essence hadn’t changed.

And now I knew who the mysterious voice was that had sometimes come to me like an auditory hallucination since my Bone Transformation.

“You’re…”

With a voice I could barely force out, I stared at the old man, who only smiled in silence.

No.

*The Helper.*

The one who had first taught me to circulate my qi when I’d just taken my first steps into the unknown world of Murim.

The mysterious being I’d been forced to forget for so long because I’d thought he was just part of the tutorial system.

“……Who on earth are you?”

Was this what it felt like to be struck by lightning through the crown of your head?

Faced with the immense truth at last, I trembled as the shock surged through me like a tidal wave.

And at the same time, I knew instinctively:

The old man would never answer my question, and even this brief meeting was drawing to a close.

“You don’t have to answer. I already know.”

Grgrgrk.

Amid the contorting space, I shouted at the old man, whose face I could no longer make out.

“Then what—what happens now?”

“Who knows? I don’t know what lies ahead, either. For now, we have no choice but to return to our respective places.”

“What does that—”

“Jin Taekyung.”

The old man’s voice sank low.

Then, cutting me off, he spoke.

“Do your best. Only then can you save everyone—and yourself.”

“……!”

“Well, it’s time to go. To the place where you belong.”

The instant I opened my eyes wide, understanding what his words meant—

Whoooosh.

As my vision was swept away, sucked toward somewhere, something glimmering touched my hand.

Along with the old man’s final words, ringing out like an auditory hallucination.

—Take it. It’s this old man’s final gift.

I instinctively clenched my hand around it.

And as my consciousness faded, I heard a single sound ringing out from somewhere.

A clear bell chime I’d been certain I would never hear again.

Ding.

A brilliant light rushed from far away and covered my vision.

* * *

The old man left alone gazed in silence at the empty space for a long while.

The person who had just disappeared must have seen the entire gray-white space vanish, but the old man knew better.

This space would last forever, and Jin Taekyung had been no more than a guest who’d stopped by for a brief visit.

And he himself would once again have to continue his endless, uncertain wait.

“When will it end?”

The old man murmured softly.

He had spent so long alone that talking to himself had become a habit.

“No. Will it ever end at all?”

With a bitter smile on his wrinkled lips, the old man looked around.

An endless gray-white space stretching in every direction.

Cold and pale, it was the old man’s only home—and a vast prison without bars or an exit.

But the brief emptiness brought on by that truth soon passed, and the old man’s eyes settled back into calm.

He was a prisoner in this prison by his own choice, not because anyone else had forced him.

“Yes. So that’s enough.”

The old man muttered quietly, as if making a promise to himself, and began to walk.

Then, suddenly, he stopped and turned to look back along the way he’d come.

Or, more precisely, at the place where the guest who had visited after so long had stayed.

“Jin Taekyung.”

Letting the name slip from his lips, the old man wondered:

Could he really do it?

Had his choice truly been right?

And if he’d made the wrong choice, how terrible and cruel would the future ahead be?

But all those worries were meaningless.

The old man had already made his choice, and thanks to his help, Jin Taekyung had been given another chance.

“I suppose I have no choice but to believe in you.”

With words that would never reach him, the old man resumed his halted steps.

Then he began to walk slowly.

Across the endless gray-white space, just as he always had.

* * *

The Fire King, Jeok Cheongang, was crying.

Clutching his Disciple’s lifeless body, he sobbed quietly, oblivious to everything around him.

The cheers and clangor of steel that continued to ring out even now. The gazes of those watching him.

None of it mattered to the Master who had lost his one and only Disciple.

He didn’t hold back his tears.

No—he couldn’t.

Two years.

Only two years out of a life that had lasted over a hundred, but his time with Jin Taekyung had shone brighter than any other.

Taekyung had been the only light to find him when he was at his darkest.

And now that Jin Taekyung, his Disciple, was dead.

He had left for a faraway place, despite his Master’s plea for him to live.

*I’m sorry, Master.*

That final voice wouldn’t leave his ears.

The corners of Taekyung’s mouth, strained into a smile for the sake of his grieving Master. His eyes, half-closed and empty. Even now, they seared into Jeok Cheongang’s heart like a brand.

He was swallowed by grief so profound he couldn’t make sense of anything.

His eyes blurred by tears that kept welling up, he couldn’t see what he needed to see.

Plip.

At the moment one tear rolled down the Master’s cheek and touched his dead Disciple’s hand—

Sss.

The surface of the blood rippled with a sudden tremor, and the finger submerged in it moved.
## Chapter artifact 1132

# Chapter 1132

No one there had dared to expect it.

That the corpse of someone already dead would move.

Perhaps that was why even the few people who witnessed the finger twitching faintly failed to realize what it meant.

They put the movement down to the grieving Master’s hands as he held his Disciple’s body and sobbed, the lingering vibrations of the battlefield—or simply their imagination.

An illusion born of the desperate wish that the young hero who had met such a noble end might come back to life, even now.

And the Master, sunk in profound sorrow, thought no differently.

Thump.

At first, he thought he’d imagined the sound.

But when a vibration traveled through his Disciple’s body, held tight in his arms, Jeok Cheongang could only blink in a daze.

*How?*

It couldn’t be. It was impossible.

Yet contrary to what Jeok Cheongang’s instincts told him, the vibration, once begun, did not stop.

No—instead, it grew louder and clearer.

Like a war drum beating out the order to charge.

Thump. Thump-thump.

“……!”

In an instant, Jeok Cheongang hurriedly pressed his ear to his Disciple’s chest. His eyes flew wide.

There was no mistaking it. This wasn’t some imagined sound.

The heart that had stopped was beating again, like an extinguished ember catching fire once more.

And just as Jeok Cheongang shuddered at the unbelievable sight—

Fwoosh!

A scorching wind surged up around one person’s body.

No—

A tremendous wave of qi, powerful enough to envelop a radius of a dozen or so *jang*.

Rrrrmmm.

The space trembled in tiny shivers, like a living creature.

Everyone still nearby stared, eyes wide.

They watched the dark blue heat wavering like a mirage, and the young man slowly floating up at its center.

“Ah, ah……!”

An exclamation filled with emotion slipped from Jeok Cheongang’s lips.

Most of the people there were simply overwhelmed by the mysterious sight, seeing nothing like it before. But he knew all too well what this phenomenon meant.

So did the two other giants who had remained behind to witness it all, unlike Sword Saint Mae Jonghak, who had gone to bring the long battle to an end.

“……Am I seeing this right?”

The Slaughter Saint asked as if he couldn’t believe it. The Bow Saint answered, her voice trembling unlike usual.

“I think so. No, I’m sure of it.”

Watching the young man drift out of his Master’s arms and rise into the air, she murmured as if to herself.

“Bone Transformation.”

At that moment—

Ssshh!

The heat that had surged like waves, the dark blue streaks of light, gathered fiercely together.

Toward the body, still warm.

To rekindle the faint ember within.

* * *

People had feared fire since ancient times.

A campfire burning in the mountains at night could give them strength, but any heat beyond that could become a great disaster.

So they believed fire was bound to destruction.

They failed to look past destruction and see fire’s power to purify.

And at this very moment, the heat coiling around one person’s body was unquestionably a purifying flame.

Flicker.

Though trapped in a consciousness where he couldn’t tell dream from reality, Jin Taekyung could feel it clearly.

The heat surging from deep within his body.

The agony of his whole body burning, and at the same time, the refreshing sensation of his wounds being washed clean.

Kwoooosh!

A wave of fire overflowed in every direction. The horrific heat seemed ready to melt even his already-healed body in an instant.

Yet for some reason, Jin Taekyung felt not a trace of fear.

Of course not.

He instinctively understood.

The purpose of that immense heat wasn’t merely to sweep through and melt his every limb and bone. It was also to peel back a layer of the unknown power hidden inside him.

But that wasn’t the only reason Jin Taekyung could calmly accept his transformation.

Ding. Ding. Ding.

Beyond his hazy sight and senses, bells rang out one after another.

The chimes he’d thought he would never hear again were clearer than ever, and letters that swept past his eyes like the wind tickled his retinas.

New insights and related achievements, an increase in Qi Sense and martial arts……

Unable to bear the weight of the words pouring down without end, Jin Taekyung closed his eyes.

Focusing entirely on his mind’s inner landscape, he sank deep beneath the surface.

And the next moment, he found himself standing in a new scene.

*Where is this?*

He had seen it only once, yet the sight was familiar.

How could he forget?

The beautiful view, with endless land and sea spread across the distant earth, and clouds thick as far as the eye could see.

*The peak. It’s the same peak as before.*

When he had brought together the demonic qi of the Heavenly Power Demon, the lightning qi of the Thunderbolt Saber King, and his own Scorching Yang Qi, Jin Taekyung had finally become the conqueror of this lofty peak.

At last, he had stepped into a new realm: the Summit of Martial Achievement.

*But that was all.*

He had claimed the peak that touched the clouds, but no matter how far he reached, he couldn’t touch the sky beyond them.

That realm hadn’t been open to him then.

He hadn’t yet earned the right—the enlightenment—to glimpse it, even for a moment.

Yes. That was certainly how it *had* been.

Until today, when he received another insight from the old man.

*Climbing higher was never the only answer to begin with.*

He had thought of it in the simplest, most obvious way.

But now he knew.

There was more than one way to glimpse the sky beyond these thick clouds. Raising the peak beneath his feet wasn’t the only one.

*There’s more than one answer.*

Why hadn’t he realized that?

He had always gone beyond his own imagination. So why had he placed limits on his thinking?

Jin Taekyung suddenly remembered a forgotten moment from his past.

Back when he was a novice martial artist, still stuck at Second Rate. He had asked Jin Wikyung how on earth he could reach the First Rate realm, and his brother had answered with a single word: *faith.*

*“What does that…… mean?”*

*“Exactly what it sounds like. Believe in yourself.”*

*“What does believing have to do with advancing realms?”*

*“Martial arts begin with belief.”*

Only then did he understand.

Now he understood.

The person who had never believed in Jin Taekyung was not someone else. It was Jin Taekyung himself.

Even after he’d far surpassed Jin Wikyung’s martial prowess, even after he’d earned the right—he had always been that way.

*But not anymore.*

He decided to try believing, just a little.

Believing the old man’s words: Don’t set limits for yourself.

Believing in the new potential he still hadn’t discovered.

*If I want to see it, I can.*

At the very top of the peak, Jin Taekyung lifted his head as if spellbound.

He gazed at the clouds flowing in a long line, blocking his inner landscape.

Not with his eyes, but with his heart.

With the Mind’s Eye.

And the next moment—

Fwoosh!

Beyond the clouds as they scattered as if by magic, light flooded his vision white. A pain as if his retinas were burning shot through him.

“……!”

Would this be what it felt like to be thrown into a vast pit of fire?

Or would dozens, hundreds of bolts of lightning striking down at once hurt like this?

But Jin Taekyung held on to the thread of his fading consciousness with all his might.

Suppressing the pain in his mind, which felt ready to turn to mush at any moment, he endured the unprecedented heat pouring down with the light.

Just that alone made his body, and the memories in his mind, feel as if they were burning away completely.

Who he was.

Where he was.

And yet there was one thing he didn’t forget: why he was enduring such horrific pain.

*I have to go back. No matter what.*

He had left something precious behind.

He had failed to protect what he needed to protect, and there was still something he had to do.

So…… that was reason enough to endure this pain.

If he could only return, he could bear this stretch of agony, each second feeling like ten years.

Even the horrific heat that had seeped deep into his body and flowed through it like lava.

But expanding the bounds of his own limits didn’t mean every boundary had disappeared.

Kiiiiing.

This was a limit he couldn’t help but face.

A limit Jin Taekyung couldn’t change by his own will; one he couldn’t cross because he truly wasn’t qualified.

And the moment Jin Taekyung realized this—

Ssshhh.

Along with the dense clouds that once again blocked the light, the immense heat still flowing inside him spread throughout his body.

It flowed through hundreds of acupoints—not his Lower Dantian, nor his Middle Dantian—and was absorbed, as if melting into them.

As though it had been part of his body from the start.

As though it were replenishing his own qi, damaged and ruined beyond recovery, and filling him with even greater vitality and strength.

*Ah.*

Jin Taekyung understood in an instant.

That his endurance hadn’t been in vain.

That the old man’s words—that it was time for each of them to return to their own places—could finally become reality.

And his hunch was right.

Ding.

With the clear chime ringing somewhere beyond the depths of his consciousness, Jin Taekyung—

No.

I opened my eyes.

This time, I didn’t need anyone’s help.

* * *

The dark blue radiance that had blazed brightly for half a day was slowly dying down. All around, a suffocating silence had fallen.

The allies who had finally won this horrific bloodbath, and the fanatics who had survived by sheer luck and been captured—

No one dared open their mouth.

It was as if even the dead were watching.

Through the fading heat, a person slowly descended.

But unlike those frozen in place, forgetting even how to breathe, the old Master reached out with a trembling hand to catch his Disciple.

The body that now carried warmth like a campfire.

At the same time, a thought suddenly occurred to him.

What if—what if none of this were real?

If it were a spring dream unfolding in the mind of an old man who had already gone mad, what would he do?

That was why Jeok Cheongang couldn’t bring himself to part his lips.

If this truly was a dream, then he would rather never wake.

But unlike Jeok Cheongang, someone knew.

That all of this was undeniably real.

“I kept my promise.”

Half-raised eyelids, and a languid voice.

The Disciple smiled at his Master, who stared back in a daze, then added:

“Master.”
## Chapter artifact 1133

# Chapter 1133

The moment a small but unmistakable voice slipped between someone’s lips, the countless people surrounding him all widened their eyes at once, as if they’d rehearsed it.

What should they call this?

Survival?

Or resurrection?

No one knew the answer.

All they knew was that something hot surged up from deep within their chests.

“……!”

“……!”

A muffled roar, powerful enough to shake heaven and earth, rose beyond the Inner City.

The rain that had poured down without end had stopped long ago, but their cries didn’t let up.

Some wept. Some laughed. Others raised their weapons high and roared as if the battle still raged.

Exhausted as they were, they rejoiced with all their hearts.

The brutal bloodbath that had seemed as if it would never end was over.

And yet, alongside their joy, they felt a grief too deep for words.

They looked at the empty places left by comrades who had stood shoulder to shoulder and fought back to back with them only a few hours ago.

Finally, they shuddered at the sight before their eyes: a young hero awakening amid a blue-black radiance, in a miracle beyond belief.

His Master watched his Disciple with an expression of disbelief, then parted his trembling lips and spoke.

“Yeah. I believed in you.”

His words said one thing, but his eyes were soaked with tears.

At the sight of Jeok Cheongang, Jin Taekyung said nothing, only managing a faint smile.

Whether his Master had believed in him or not—what did it matter?

What mattered was the feeling in his Master’s tears, and that he had kept his promise.

*I’m back. Really.*

Perhaps it was because his mind was exhausted beyond its limits.

His consciousness was hazy, as if sunk deep in sleep, but Jin Taekyung knew that everything around him was real.

The sky slowly clearing.

The familiar faces that surrounded him now, laughing and crying, though he’d thought he would never see them again.

And—

Among the countless holographic windows floating in the air, the words that stood out most clearly and prominently.

> **System**
>
> Innate qi has been restored!
>
> Status abnormality, Final Rally, has been lifted!
>
> The sudden Quest, A Candle in the Wind, or a Flame, has been successfully completed!

Would he become a candle, its flame dying helplessly away?

Or a blaze that devoured his enemies?

At that crossroads, Jin Taekyung had chosen the latter, and the dying ember inside him had finally been reignited.

The ember called innate qi.

And the second Bone Transformation that followed was nothing short of a miracle—one no one present could have expected.

Not even the peerless giant known as the Sword Saint.

“You make a lot of noise in your sleep. More than I ever imagined.”

At Mae Jonghak’s joking remark as he came over, Jin Taekyung let out a quiet snort of laughter.

“I almost woke up halfway through. It was so noisy around me.”

“Is it still noisy?”

“Yes.”

Jin Taekyung glanced at his allies, still shouting their lungs out, and added:

“But… it sounds good.”

It sounds good.

At Jin Taekyung’s brief comment, Mae Jonghak watched him in silence, then gave a small nod.

“Yes. I feel the same.”

No one needed to ask about the battle’s outcome, or explain it.

The proof was all around them: countless allies surrounding them, and a handful of fanatics on their knees, bound from head to toe.

*The battle is over.*

At those few words, something hot surged up from one corner of Jin Taekyung’s chest.

Perhaps this was only a victory for today.

Today’s victory might be erased by a defeat tomorrow, whenever that day came.

But… for now, this was enough.

Enough that this horrific hellscape had come to an end.

Enough that they had defeated the enormous Dark Heaven army that had stood in their way like a mountain, along with the powerful enemies who led it.

*The Blood Lord. And the Grand Mage.*

Jin Taekyung lifted his head and looked northeast.

He didn’t know how many more enemies were waiting beyond that vast desert outside Qinghai.

But the deaths of the Blood Lord and the Grand Mage on this battlefield were undoubtedly a major victory for the allies.

He couldn’t be certain, but as far as he could tell, those two had been the Lord of Heaven’s last hunting dogs.

*But… what is this feeling?*

A sudden sense of déjà vu made Jin Taekyung’s eyelids flutter.

Why?

He felt as if he’d forgotten something.

Something very important—something he couldn’t afford to overlook.

But it didn’t take him long to realize what that feeling was.

Whoooosh!

The next moment, Jin Taekyung’s eyes flew wide as he saw a dozen or so shadows shoot up into the distant sky.

*Those are…!*

They were none other than strange birds.

They flew across the sky with their wings spread wide, white bone joints exposed and blood-red eyes flashing.

Like messengers rushing to deliver urgent news to someone.

“No!”

The shout burst from him on instinct.

But before he could do anything, the birds, already far away, shot west at a speed far beyond anything they’d managed while alive.

Leaving behind one name that struck Jin Taekyung’s mind like a bolt of lightning.

“……Ma Sanbao?”

He’d forgotten about him for a moment.

No—that wasn’t quite right. He hadn’t had even a moment to think about him.

The powerful jiangshi sorcerer who carried on the Maoshan Sect’s legacy had been hidden from sight by the shadows of the two monsters, the Blood Lord and the Grand Mage.

And at the same time, the Blood Lord’s final words before he met his end rang through Jin Taekyung’s mind like an auditory hallucination.

*“Celebrate to your heart’s content. This will be your last laugh.”*

He hadn’t understood it then.

He’d thought those words were nothing more than the tired bluster of a defeated general.

But now, the cold running down Jin Taekyung’s spine foretold another crisis.

*Could it be?*

The tangled threads of information in his mind began to unravel one by one.

Ma Sanbao had never appeared on the battlefield, despite being an undeniably powerful force—if not a match for the Blood Lord and the Grand Mage.

The Sword Saint and the Murim Alliance’s elite had traveled thousands of *li* to Qinghai without even telling their own allies the truth.

And then there were the strange birds that had watched everything unfold before flying west.

*Wait. If they’re heading west…*

No doubt about it.

Mount Kunlun.

That place, already in Dark Heaven’s grasp, had to be the birds’ destination.

At the same time, Jin Taekyung recalled one of the questions he still hadn’t answered.

Why had Dark Heaven’s enormous army, which had occupied Mount Kunlun before he and the reinforcements even set foot in Qinghai, remained so immovable?

And had the Blood Lord really made all these moves just to catch him and every other big fish in a single sweep of the net?

*No. That wasn’t all the Blood Lord was after from the start. It was just… they needed time, too.*

Perhaps because his mind was already exhausted beyond its limits.

Or perhaps because he’d finally grasped the shape of the foreboding he’d felt.

His face had turned as pale as paper as he looked around at the people surrounding him. Without realizing it, Jin Taekyung let out the breath he’d been holding.

Along with two bitter words that lingered on the tip of his tongue.

“……Moving Formation.”

That was the answer Jin Taekyung had found.

It was one of the main reasons Dark Heaven’s powerful army had hunkered down on Mount Kunlun—and the Blood Lord’s last move, prepared in case things went wrong.

And Ma Sanbao, the hidden blade, would move as soon as he heard this news.

Through the Moving Formation newly inscribed somewhere on Mount Kunlun, he would pierce the allies’ most vital point.

The very place called the Central Plains.

“We have to move. Right now. If we don’t, the Central Plains—”

Jin Taekyung’s voice trembled as he groaned.

His breath caught in his throat, his heart pounded hard.

Beyond his vision, swaying wildly, he saw the faces around him one after another. Perhaps they shouldn’t have come here today at all.

Especially the man who had been known as the Sword Saint for decades, and was now the Alliance Leader.

But—

“Yeah. We have to move.”

That was as far as Jin Taekyung could go.

Tap.

A hand suddenly touched the back of his neck.

In the same instant, Mae Jonghak struck a Pressure-Point Strike with lightning speed. In an even voice, he continued:

“But this time, you’re going to rest.”

Jin Taekyung answered.

Or tried to.

No. Absolutely not. He couldn’t rest now.

But despite his desperate resolve, his lips wouldn’t move, and exhaustion and sleep washed over him, pressing down on his eyelids with the weight of ten thousand *geun*.

*Ah.*

As his vision went dark in an instant, Jin Taekyung let go of consciousness, a voice ringing in his ears like an auditory hallucination.

“You’ve done well, my friend.”

* * *

Qinghai is vast.

But the wings of the strange birds, granted boundless vigor by death, were swift enough to make the distance between Xining and Mount Kunlun—more than several hundred *li*—seem insignificant.

And the shocking news brought by these exceptional messengers, unlike any seen in the past or present, reached Mount Kunlun’s highest peak in less than a *shichen*.

No—

It reached a certain jiangshi sorcerer who carried on the Maoshan Sect’s legacy.

“……So that’s what happened.”

Ma Sanbao muttered to himself as he stared east, his gaze sinking deep.

The news was impossible to believe, but he had no choice.

More than a dozen strange birds had already relayed everything they’d seen and heard in vivid detail.

The result of a bloody battle that had continued without a break for half a day—and the presence of people who, he’d thought, could never appear in Qinghai.

*I owe the Blood Lord an apology. I thought he was just a man crazed by blood.*

Ma Sanbao let out a quiet snort of laughter.

More than anyone, the Blood Lord had obsessed over Jin Taekyung. Yet by keeping one last move in reserve, he hadn’t forgotten his most basic loyalty to the master who held his leash.

A final sword stroke that would lay waste to the Central Plains, now all but undefended.

And Ma Sanbao was willing to play that part.

“It’s about time I left this wretched mountain.”

Ma Sanbao rose from the grand chair and addressed his waiting subordinates.

“Let’s go. To the Central Plains.”
## Chapter artifact 1134

# Chapter 1134

The air on Mount Kunlun felt heavy and cold that day.

The mist flowing over its towering peaks was unusually thick, and it had been a long time since any sign remained of the large and small creatures that once lived alongside humans amid the beautiful landscape stretching in every direction.

Only blood-red eyes glimmered through the dense mist, accompanied by eerie cries.

“Grrr.”

A vicious growl spilled between yellowed teeth.

The mountain lord[^1] who had ruled Mount Kunlun only a month ago bent his body, now larger than it had been in life, to greet his master.

Along with thousands of human demons who now surrounded Taiqing Hall—the very symbol of the Kunlun Sect—without leaving a single gap.

“Everyone has gathered, as you commanded.”

The report came from one of the hundred or so men wrapped head to toe in jet-black robes. Ma Sanbao’s voice grew eager.

“How many in all?”

“About five thousand. Three thousand of them are monsters.”

The corners of Ma Sanbao’s mouth lifted in a gentle smile.

“Then Mount Kunlun’s spiritual creatures must be nearly extinct.”

Anyone familiar with the state of Murim who heard their purpose and conversation might have scoffed at such an absurd claim.

Five thousand troops was no small force. But even the Hundred Thousand Demonic Disciples, who had once blanketed the world in darkness, had failed to bring the Central Plains under their control.

But there was good reason for the smile on Ma Sanbao’s face.

*It’s enough. More than enough.*

Ma Sanbao swept his sunken gaze over the subordinates packed in all around him.

The monsters’ blood-red eyes flashed without pause. The fanatics moved only at his command, little more than soulless puppets.

Now that they had completed their preparations and waited only for his orders, they truly deserved to be called a Demon Army.

Comparing them with the mere Demonic Cult of the past, now only a ghost of history, would be an insult to them.

And the greatest source of Ma Sanbao’s confidence was the hundred or so corpse sorcerers standing before him, including the man in black.

They might not measure up to Ma Sanbao himself, but each was a true monster capable of leading an army, as long as there were corpses to work with.

Ma Sanbao regarded them with satisfaction, then spoke.

“We’ll split the army in two and move out.”

“Forgive me, but has the plan changed?”

At the black-clad man’s cautious question, Ma Sanbao nodded.

Under the original plan, they would have split into seven groups and stirred up chaos across the land. But circumstances had changed.

Sword Saint Mae Jonghak had appeared in Qinghai, leading no less than ten thousand elite troops from the Murim Alliance.

*Who would’ve thought the Alliance Leader himself would bring reinforcements?*

Ma Sanbao had stayed behind in case of a situation like this. Even so, Mae Jonghak’s arrival was as surprising as the Green Forest Alliance and the Yangtze River Channel League betraying them.

But the fact that Alliance Leader Mae Jonghak had left the Murim Alliance meant he must have left at least a minimal defense in Henan.

*Of course, with its main force gone, it’ll be nowhere near enough. Still, to prepare for any eventuality, we’d be wise not to spread ourselves too thin.*

Ma Sanbao was cautious.

This was an opportunity he had fought hard to seize—perhaps one granted by Heaven itself.

The corpse sorcerers’ abilities might make such caution excessive, but he wanted to choose the safest and surest method possible.

Ma Sanbao wanted to enjoy a position second only to one and above ten thousand in a world reshaped under the Lord of Heaven’s rule—not meet a miserable end like the Blood Lord.

After carefully weighing the matter, he had finally narrowed his targets down to just two places.

“Henan and Shanxi.”

At his superior’s voice, which broke the brief silence, the black-clad man bowed deeply.

“Understood. A most excellent decision.”

With the Jin Family of Taiyuan gone, Shanxi Province was all but an ownerless mountain. Henan, meanwhile, had to be taken for its symbolic importance and strategic location in Murim.

In fact, with Mae Jonghak absent, this was the perfect opportunity to seize Henan with ease.

And Henan and Shanxi shared a border. One of the greatest advantages was that they could support each other at any time, should anything go wrong.

“If I give you two thousand troops and half the sorcerers, can you take Shanxi Province within seven days and nights?”

Ever since the Jin Family of Taiyuan united Shanxi Province, it had continued to grow stronger by the day.

But the black-clad man answered without so much as a pause.

The mere two thousand troops would multiply endlessly, thanks to the several dozen sorcerers he would have at his disposal.

“Four days will suffice.”

“And if I include Hebei?”

“Give me ten days. I’ll return leading an army of a hundred thousand.”

The black-clad man’s prompt answer deepened Ma Sanbao’s smile.

“I’ll remember that promise.”

At that very moment—

Sssaaaa.

Faint light began to rise in strands from the ground.

The Moving Formation the Grand Mage had set up during her stay on Mount Kunlun—no, the Magic Formation—began to activate, stirred into motion by the few sorcerers who had remained behind with Ma Sanbao.

Vroooom.

Two enormous circles spread outward, growing larger by the second and enveloping everyone in light.

Feeling the mysterious energy surge from every direction, Ma Sanbao trembled with rising elation.

*I’ll end it all in one stroke. With my own two hands.*

His confidence was more than justified. No one who knew Ma Sanbao could deny it.

He was the most powerful corpse sorcerer to carry on the Maoshan Sect’s legacy, and even as a martial artist, he was a Supreme Peak master who could stand shoulder to shoulder with the Ten Kings.

With the Three Saints, Jin Taekyung, and Jeok Cheongang all absent, the current Murim of the Central Plains held not the slightest fear for him.

*Sword Saint, if nothing else, you shouldn’t have left.*

No matter what defenses they had prepared, with this much power, he could cut through the heart of the Central Plains in an instant.

By the time word of their arrival reached the enemy, their force would number not thousands but tens of thousands.

An immortal army that would replenish itself no matter how many times it was killed.

*Today, the course of history will change.*

And the world would remember forever that Ma Sanbao himself had been there at the first step of this grand history, destined to last a thousand years.

Fwoosh!

As a brilliant flash of light washed his vision white, Ma Sanbao smiled and closed his eyes.

He let himself be carried by the mysterious force pulling his spirit and flesh toward some distant place.

He imagined the great strides he would take, one after another, and the mighty trail they would carve across the world.

Paht.

The change happened in an instant.

In the next moment, Ma Sanbao felt the air and wind around him had changed completely. Instinctively, he realized that the Magic Formation prepared by the Grand Mage had transported him and some three thousand of his subordinates to their promised destination.

*At last, it begins.*

With the thrill reserved for the one taking the first great step, Ma Sanbao opened his eyes.

Or, more precisely, he tried to.

Crunch—splat!

A gruesome sound of flesh being torn rang out, and something hot and sticky covered his face before he could open them.

“……!”

The scent of blood seeped deep into his nostrils, sickeningly familiar.

As though the whole world had stopped, Ma Sanbao struggled to lift his trembling eyelids.

And then he saw it clearly with his own two eyes.

The other thing he hadn’t realized.

Thump. Splatter.

In some nameless, remote mountain valley where even the moonlight didn’t reach, large and small figures crumpled like bundles of straw without so much as a dying cry.

Ma Sanbao couldn’t stop it. He couldn’t move.

Neither could the few who had survived alongside him.

All they could do was stare, dumbfounded.

At the deaths of fully two thousand of their comrades, felled before they could take their first step in Henan.

They had died in horrific, bizarre shapes, their bodies fused not with blades or spears, but with rocks and trees.

“What—what in the world is this?”

Just then, an unexpected answer reached Ma Sanbao’s ears as he muttered in a dazed voice, as if under a spell.

“What does it look like? It’s exactly what you’re seeing.”

A calm voice rang out from beyond the thick darkness.

Ma Sanbao whipped his head toward it like lightning and stared.

How long had he been there?

Several dozen *jang* away, an unfamiliar middle-aged man stood on a hill that walled in the area, looking down at the basin—now gripped by fear and confusion.

No. He was looking at Ma Sanbao.

“Good to meet you. I mean that. I was so worried you might not show up that I was beside myself.”

The middle-aged man slowly looked over Ma Sanbao, frozen stiff as a statue, and the subordinates who had survived. He smacked his lips, then added:

“Of course, I can’t say I’m not a little disappointed…but this should be enough of a welcome, don’t you think?”

Ma Sanbao didn’t answer.

More accurately, he couldn’t.

For now, he could barely process the word filling his blank mind.

*A trap…!*

Yes, it was a trap.

One laid with extraordinary care.

And the refined-looking middle-aged man smiling on the hill was unmistakably the one who had laid a trap in the Moving Formation the Grand Mage had carved deep into a remote valley in Henan that no one ever visited.

A hunter who’d set the simplest, surest—and most horrific—trap of all.

“Don’t look at me with such murderous eyes. I’m the one who should be disappointed. If I’d only figured out the exact range of the Moving Formation, I could’ve finished it in one stroke.”

At the middle-aged man’s feigned sigh, Ma Sanbao felt his blood boil with fury.

“You’ll regret failing to do so. I’ll tear you and every last one of your family to pieces.”

The middle-aged man hadn’t yet revealed his identity, but Ma Sanbao already knew who he was.

The portrait he’d seen during his time in the East Depot, and the pure-white fan in the middle-aged man’s hand, were enough to bring one man to mind.

“Crouching Dragon Guest, Zhuge Feng.”

At Ma Sanbao’s confident declaration, Zhuge Feng, the current Family Head of the Zhuge Clan, raised his eyebrows.

“Oh? You know me?”

“I do. I remembered you. After today, though, I’ll forget you.”

Ma Sanbao answered in a dry voice and drew up the energy inside his body.

Though he had lost more than half his subordinates to an unexpected ambush, the most important force—the corpse sorcerers—had suffered little damage.

As soon as the battle began, the number of corpses would naturally increase.

Whatever Zhuge Feng had prepared, Ma Sanbao was certain that he would be the one to leave this place alive at sunrise.

At least, he was—until he saw a familiar face appear behind Zhuge Feng.

“Then I suppose you remember me, too. Don’t you, Eunuch Ma?”

Ma Sanbao felt a chill in his chest for an instant.

How could he forget?

He had seen that face for decades.

He knew the resonant voice of the veteran general who had protected the imperial household through every peril.

But it wasn’t only Baek Yeon, the greatest master in the imperial household, who had shaken Ma Sanbao.

The presence of the man who was the imperial household’s sword and shield meant something else, too.

Scuff.

A slender figure stepped out from behind the burly veteran.

He looked down at his former servant with the haughty gaze only someone born to noble blood could possess.

No—at the criminal for the ages who had dared to overthrow the imperial household.

“So, how did you like being a traitor?”

At the Son of Heaven’s question, Ma Sanbao groaned.

[^1]: *San-gun*, literally “mountain lord,” is a traditional epithet for a tiger.

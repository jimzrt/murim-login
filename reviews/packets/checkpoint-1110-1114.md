# Checkpoint Review — 1110–1114

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

# Chapters 1110–1114

## Plot

After the Blood Lord regains his strength, Jeong Hogun takes a blow meant for Cheongpung and loses an arm. He and roughly three hundred surviving Embroidered Uniform Guards charge the Blood Lord to protect the people, but a blood-red flash engulfs them. Jin Taekyung, barely conscious, revives through returning memories and a flower-scented energy.

The West Gate falls. Taekyung and Cheongpung retreat to the Inner City, gravely injured. At the South Gate, the Slaughter Saint stays to defend the position with the Bow Saint. Jeok Cheongang answers the Slaughter Saint’s call with an earthquake, then kills the Dalai Lama at the North Gate after learning of the Potala Palace’s vendetta against the Fire Gate Clan and its alliance with Dark Heaven.

After learning Jeong Hogun died protecting others, Taekyung forces himself to stand and rallies the Inner City’s defenders. The Blood Lord kills a hundred defenders on his way there, but a flash of fire stops him: Jeok Cheongang has arrived. Exhausted and badly injured, Jeok is overpowered. The Kunlun Five Immortals intervene, use Temporary Strength Pills by breaking their innate qi, and hold off the Blood Lord for fifteen minutes before dying. The Blood Lord resumes his advance toward the Inner City.

## Continuity

- The West Gate has fallen; more than half its garrison are casualties. Jin Taekyung and Cheongpung are badly injured in the Inner City, and Taekyung has forced himself to stand and rally its defenders.
- Jeong Hogun is dead. Roughly three hundred surviving Embroidered Uniform Guards charged the Blood Lord; their fate after the blood-red flash is unknown.
- The Blood Lord is advancing toward the Inner City. The Kunlun Five Immortals died after buying fifteen minutes.
- Jeok Cheongang left the North Gate and is heading toward the Inner City, severely exhausted and injured. The Dalai Lama is dead; Perfected Being Hyeoncheon is alive but barely conscious.
- The Slaughter Saint remains at the South Gate with the Bow Saint; her motives remain unclear. The South Gate faces the Grand Mage and four Black Ghosts.
- The Lord of Heaven’s interest in Taekyung remains unexplained. The hidden Dark Heaven agent among Cheongheoja’s Disciples remains unidentified, and Cheongheoja’s favor to Taekyung remains undisclosed and unfulfilled.

## Translation Decisions

- Retain “Blood Lord,” “Lord of Heaven,” “Embroidered Uniform Guard,” “Twelve Secret Monks,” “Black Ghost,” and “Zaha Divine Technique.”
- Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective.
- Retain “Kunlun Five Immortals,” “Perfected One Taecheong,” and “Temporary Strength Pills.”

## Durable state

{
  "active_continuity": [
    "The West Gate has fallen; more than half its garrison are casualties, and some survivors retreated to the Inner City.",
    "Jin Taekyung and Cheongpung are badly injured in the Inner City; Taekyung is still alive and has forced himself to stand.",
    "Jeong Hogun died defending others; Taekyung remembers him as a steadfast officer.",
    "Taekyung has rallied those around him to keep fighting for the Inner City's people.",
    "The Slaughter Saint remains at the South Gate to support its defense; the Bow Saint’s motives are unclear.",
    "Jeok Cheongang left the North Gate and is heading toward the Inner City, severely exhausted and injured after fighting the Blood Lord.",
    "The Dalai Lama is dead; Perfected Being Hyeoncheon is alive but barely conscious.",
    "The Blood Lord killed a wounded follower and is advancing toward the Inner City.",
    "The Kunlun Five Immortals died after using Temporary Strength Pills to hold off the Blood Lord for fifteen minutes."
  ],
  "continuity_sources": [
    1113,
    1114
  ],
  "open_questions": [
    "Will Jin Taekyung survive his injuries, and can he receive treatment from the Divine Physician?",
    "What is the Bow Saint hiding, and why did she accept the possibility of Taekyung’s death?",
    "Can the South Gate hold against the Grand Mage and the four Black Ghosts?",
    "Can the Inner City’s defenders stop the Blood Lord?"
  ],
  "safe_through": 1114,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 1110

# Chapter 1110

It all began and ended in an instant.

“I remember. Your name.”

The low voice of the monster that had absorbed the life force of countless fiends raining down from the sky rang across the battlefield.

“And the debt I owe that bastard, Sword Saint Mae Jonghak.”

At last, the monster—the Blood Lord—had awakened with all his strength and memories restored. His red eyes flashed.

Then he sent a bloody beam blazing through the air, brighter than the light in his eyes.

*Whoosh!*

Cheongpung had to dodge.

If that beam hit him, he would surely die.

But Cheongpung had already spent all his strength. He could only watch helplessly as the Blood Lord’s palm, striking the air like a bolt of lightning, sent a blood-red palm strike tearing through space.

Only someone else moved—guided by careful calculations born of countless past experiences, and by instinct that struck in an instant.

*Crunch!*

A horrible tearing sound, enough to chill the spine.

Then flesh and bone ripped away all at once, and the red liquid hidden inside burst out.

*Splatter. Thud-thud.*

Feeling hot, sticky blood wash over his face, Cheongpung blinked dazedly without realizing it.

It wasn’t because of unbearable pain, nor because he’d seen death looming before him.

What Cheongpung saw through his blood-red vision was the face of a man looking down at him. Somehow, Cheongpung had ended up sprawled on his side.

“Get…… up. Quickly.”

*Cough.*

The man struggled to speak, swallowing the blood that surged up with every word. His voice was calm despite the effort.

It was hard to believe he was someone whose arm had been torn away all the way to the shoulder by the palm strike.

“Leave now. Before it’s too late.”

“B-but—”

Cheongpung’s mind had gone blank at this unexpected turn. He was just starting to stammer out a reply when—

“You fool!”

A fierce shout suddenly rang out.

Then, from between the bloodied man’s lips, came a voice like a beast’s growl.

“Do you still not understand? Can you still not see?”

Blood spilled with every word he ground out.

Even so, he didn’t stop speaking.

There was something far more precious than the pain, so distant it could numb the mind, and more precious even than the death that was all but certain.

“This isn’t for you! We’re doing this to save everyone—to save the whole world!”

Like a great tiger, the man roared.

He pointed at the Blood Lord, approaching even now with bloody beams scattering from his body, and at the people throwing themselves without hesitation at that unprecedented monster.

*BOOM!*

*Crack! Splaash!*

Deafening crashes shook the area. Fountains of blood erupted without pause, blotting out the rain.

In that horrific hellscape of slaughter, Cheongpung had stared blankly at the scene before him. At last, he gritted his teeth and stood.

*Grind.*

A dull pain, and the taste of blood filled his mouth.

But that was nothing.

Not compared to the agony of those people, being torn apart and broken even now.

“I’ll…… thank you later.”

What more was there to say?

The man gave him a faint smile and a nod, then watched Cheongpung walk away and murmured as if to himself:

“Please, look after him. The Marquis of Shangshan.”

That was the end.

It was the resolve of a man who knew his own end had come—a final moment with no later.

*Step.*

With a step that felt unusually heavy, the man turned around.

Calmly, he fixed his gaze on the monster approaching through a dense mist of blood and spoke.

“You who dared to plot rebellion and throw the world into chaos: state your identity and surrender peacefully.”

“Criminal? Surrender?”

The Blood Lord twisted his mouth into a smile.

There was mockery in the curling corner of his mouth—and anger, too.

The anger of a predator who’d had its prey slip away right in front of it.

“There are a lot of you idiots who’ve got a death wish.”

*Shhhhh.*

In a matter of moments, the blood-red beams that had swallowed hundreds of lives rose in strands from the Blood Lord’s entire body.

“You should’ve run. You might only have escaped for a little while, but at least you’d have had a chance to look back on the life you lived.”

The man gripped the great sword in the one hand he had left and answered.

“I don’t need that kind of chance. I’m not like you.”

And he truly wasn’t.

Though not everything he’d done had been perfectly just, he had lived his life true to his loyalty.

He had never blindly submitted to orders, nor had he ever wavered when powerful men dangled sweet offers before him.

That was why he had earned the right. He had proved himself.

Just as the others now formed a square formation around him, despite looking ready to collapse at any moment.

“Let me ask you all: what is our duty?”

At the man’s sudden question—or rather, his commander’s—the roughly three hundred surviving Embroidered Uniform Guards answered as one.

“To protect the Imperial House, with an unshakable oath and unwavering loyalty!”

Some voices were young, others old.

The familiar faces of friends and comrades who had shared their lives with them—less than half remained.

But none of them had forgotten.

Each remembered the oath they had etched into their hearts the day they first received shining golden armor.

“Then what is our obligation?”

They were all exhausted.

In body and mind.

Now, even raising their voices was a struggle.

But that was why they squeezed out every last bit of strength to answer.

So the fear slowly sinking into their hearts wouldn’t overcome them. So the oath they had sworn would not fade, even in death.

“To protect all the people—and beyond them, the whole world!”

“……!”

As their cry shook the space around them, the sneer on the Blood Lord’s lips began to fade.

*Vroooom.*

The great sword in the man’s hand trembled and shone brightly.

The magnificent, radiant Force that had long seemed like an unreachable realm in a corner of his heart.

*Was this enlightenment, brought at last by letting go of everything? Or…… is Heaven telling me to fight back, no matter what?*

As the question crossed his mind, the man let out a quiet laugh.

He didn’t know where this sudden power had come from, but now it hardly mattered.

He knew what he had to do. That was enough.

“As a Thousand Captain of the Embroidered Uniform Guard, carrying out His Majesty the Emperor’s exalted will, I give you your orders!”

The man—or rather, Jeong Hogun—swallowed the blood surging up his throat and shouted.

He aimed his Force, burning like a final rally, at the many enemies now surrounding them and the monster at their center.

“Behead the rebels!”

At that moment—

“Loyalty!”

With a military salute that rang out more fiercely than ever, Jeong Hogun and the roughly three hundred Embroidered Uniform Guards charged forward, their muffled roar bursting from them.

Straight toward the death looming before them.

Toward a final stand that would endure even after their mortal bodies perished.

Their charge was truly majestic.

*Whoosh.*

And it was glorious.

*CRUNCH!*

Right up to their final moment, when they fell, engulfed by a massive blood-red flash that erupted without warning and stained everything around them.

* * *

My vision was blurry.

Sharp pains, large and small, jabbed through my body like awls. Every sound reaching my ears seemed distant, like an echo from beyond a mountain ridge.

*Ah.*

A question suddenly occurred to me.

Where was I? Who was I? And why were my eyelids so heavy?

It was strange.

I could’ve sworn I remembered everything just a moment ago.

*I just want to sleep. Peacefully.*

I couldn’t think of anything else.

If I just fell asleep like this, I felt like I could enjoy the deepest peace.

A desperate longing to rest somewhere without pain or worry was the only thing ruling my body.

—Rest, huh? That doesn’t sound so bad.

An unknown voice suddenly echoed in my mind, but I wasn’t even curious who it was anymore.

It could’ve been a hallucination, since my mind was wandering. Or maybe another part of me was agreeing.

Honestly, what did it matter?

As long as I could fall asleep peacefully.

*Right? There’s nothing wrong with taking a little rest.*

In response to my question, the unknown voice spoke again.

—If you put it that way…… I’d have to say there are plenty of reasons it could be a problem.

*A problem?*

—I don’t know. You probably know the reason better than I do.

*What?*

For an instant, I was bewildered.

I didn’t even remember who I was, but somehow I knew the reason?

And then, a moment later, the mysterious voice rang out in my mind again.

—You don’t seem to feel it. Even now, you’re fighting with everything you have to wake up.

That couldn’t be right. That was nonsense from some clueless idiot.

My vision was blurry and spinning, and every kind of pain was gnawing at my body. Who wouldn’t want to rest in a state like this?

I wanted to fall asleep so badly.

—Are you sure?

Of course.

Or…… at least, I thought so.

—Then how have you managed to stay conscious this whole time? If you just close your eyes and let instinct take over, everything will become peaceful.

*That’s……*

—I hope you’re not about to say you’ve forgotten how to fall asleep.

I was at a loss for words.

Some confusion had suddenly crept in without warning, and it was gradually pushing the drowsiness aside. I didn’t even realize that was happening. I just stared blankly at the question that came to mind.

*Why? Why am I fighting this hard to hold on?*

But this time, no answer came.

All that came were fragments of memories, one after another, landing on the surface of my once-calm consciousness.

And with them came an unknown energy, slowly rising from somewhere deep inside me.

*Whooosh.*

It felt like the wind was blowing.

A clear, refreshing breeze pressed down on the pain that had tormented me all along and rekindled the embers of memories that had been dying out.

My name, countless faces and voices—and, carried by my senses as they grew sharper, the strong smell of blood and someone’s shout.

……!

……!!

My vision slowly sharpened, and the echo drew closer.

And amid all of it, at last, I remembered.

Why I had wanted so badly to rest.

And why, despite that, I had never let go of consciousness.

*I…… I’m…*

As my consciousness slowly returned, so did the pain.

Would this be what it felt like to fall into a pit of fire? To have my body torn into thousands of pieces?

I didn’t know. I couldn’t know.

But there was one thing I did know.

I still had so much left to protect.

—As always, a good decision.

At the moment the unknown voice whispered its last words in my mind—

*Whoooosh.*

The wind that had been sweeping through my body became a wave of energy, mingled with the fragrance of flowers, and washed over me.

No—it lifted my dying body and mind back to their feet.

Along with a familiar voice, finally reaching my ears.

“……Benefactor! Benefactor!”

A frantic cry. A face drenched in tears.

Cheongpung’s voice pierced the ears of me, gasping awake, and boomed like thunder.

“The West Gate—the West Gate…!”

The reality I’d barely returned to was still cruel.
## Chapter artifact 1111

# Chapter 1111

Boom, boom, ba-boom!

There was nothing strange about war drums sounding in the middle of a battle.

The drum installed on the highest watchtower was practically another command post, keeping watch over the entire perimeter of the walls.

But this beat rang out more urgently and perilously than ever before. Something about it made the hearts of those who heard it tighten.

*Slice!*

A streak of light shot across the foot of the wall like a bolt of lightning.

Dozens of fanatics charging in while scattering Sword Energy were cut to pieces and sent flying. Yet the man responsible for this display of divine might wore a rigid expression.

“This is……”

His words trailed off. The Slaughter Saint, who had been fighting enemies right beneath the wall, turned his head on instinct and looked—not toward the Inner City, where the war drums had sounded, but far away, toward the west, where a muffled roar reached them.

Even he didn’t know exactly why.

All he knew was that his instincts, honed by countless experiences, and the immense surge of power that had boiled over from the west moments ago were stirring every one of his senses.

For an instant, they mattered enough to push even the streaks of light plunging down from above out of his mind.

*Shreeeeeeek!*

Countless ice spikes rained down, freezing the air around them.

The Slaughter Saint felt the icy chill aimed at him, but he didn’t take his eyes off the west.

Someone utterly dependable stood behind him.

*Whoosh!*

The wall lit up. A beam of light shot from someone’s fingertips and swallowed hundreds of ice spikes whole.

*KABOOOOOM!*

A thunderous crash burst out alongside a blinding flash.

Before the shockwaves of the collision had fully faded, the Bow Saint’s clear Sound Transmission rang in the Slaughter Saint’s ears.

—The West Gate has fallen.

“……!”

The Slaughter Saint swallowed the groan rising to his lips.

The ominous premonition he’d feared had come true. But that left him even less time to lament. With one of the pillars holding their already fragile balance now completely broken, everything was in danger.

—Then what happened to the allies defending the West Gate……

—More than half are casualties, according to the numbers confirmed so far. They say the Embroidered Uniform Guards bought us at least a little time by fighting to the death.

Half.

It was no wonder the Slaughter Saint bit his lip at that staggering number.

The West Gate’s garrison had numbered more than ten thousand.

And half of them had vanished—in barely half an hour after the battle began in earnest.

—What happened to those who survived?

—Some retreated to the Inner City. Others seem to still be holding off the enemy from the rear.

—Then, could it be—

A grim suspicion suddenly crossed his mind. The Slaughter Saint fell silent, and the Bow Saint’s low Sound Transmission continued.

—Cheongpung and Jin Taekyung. The two of them retreated to the Inner City.

—……They were lucky.

The Slaughter Saint suppressed the sigh of relief that nearly escaped him.

After so many had already been lost, it wouldn’t be right to focus only on the survival of those two just because he had ties to them.

But that wasn’t all the information the Bow Saint had received.

—If those two are alive, we still have a chance. While they defend the Inner City, we can counterattack as much as—

—That won’t be easy, not in their current condition.

—What…… do you mean?

—I heard Jin Taekyung was badly injured. Cheongpung isn’t in good shape, either.

—……!

The Slaughter Saint’s eyes widened.

And as he unconsciously froze, a stray blade swung at his shoulder.

*Slice!*

A swift, powerful strike.

He twisted at the last moment, but the Sword Energy trailing the blade still grazed him, slicing his skin.

Of course, even the man lucky enough to land that remarkable hit couldn’t escape death.

*Thud!*

The dagger that left the Slaughter Saint’s fingertips pierced the enemy between the brows. At the same time, his figure blurred like a ghost and shot up along the wall.

*Whoosh, slice!*

In the blink of an eye, the Slaughter Saint stood atop the wall, cutting down enemies climbing up ladders and chains as his lips moved.

—How bad is it?

The Bow Saint, like the Slaughter Saint, was firing arrows of Force at the enemies without pause. She answered him.

—I was told he might not survive.

—……Blood Lord. We underestimated that bastard.

A low groan slipped between the Slaughter Saint’s lips.

He hadn’t been comfortable leaving the West Gate to Jin Taekyung from the start. He’d only been persuaded by the same argument they had used with Jeok Cheongang.

—We shouldn’t have left him there after all.

—Nothing would have changed, not as long as the Blood Lord’s intentions remained the same.

—I have to go to the Inner City. Hold this place until I get there.

There was no more time to waste.

If Jin Taekyung’s life was hanging by a thread, he was the only one who could pull him back from death.

With a heavy heart, the Slaughter Saint turned to leave.

Or tried to.

Until a clear voice reached his ears.

“Are you sure that’s the best choice?”

“……What do you mean?”

“Without you, the Slaughter Saint, we won’t be able to hold this place any longer. Not on my own.”

The Slaughter Saint was suddenly at a loss for words.

Of course he knew how dangerous their position was here, at the South Gate.

Even without the Grand Mage, there were four Black Ghosts.

And the sorcerers backing them were still targeting the wall with various spells while granting the fanatics even greater strength and speed.

Wasn’t that why the Slaughter Saint, who had originally been assigned to defend the East Gate, had been forced to join them at the South Gate after only fifteen minutes?

But……

“Are you saying we should just let him—Jin Taekyung—die?”

The Bow Saint met the Slaughter Saint’s disbelieving gaze and spoke in a voice more somber than ever.

“We have no choice. If that’s the death he was destined for.”

“You……!”

“That boy needs the Divine Physician. I know. But what all of us need right now is the Slaughter Saint.”

“……!”

“So, what’s the best choice?”

The Slaughter Saint’s eyelids trembled.

He knew better than anyone the answer contained in the Bow Saint’s final question, which pierced his heart like a needle.

And, in another way, he found the woman before him utterly unfamiliar.

*Why?*

He already knew why the Bow Saint, who had disappeared for so long, had returned.

He’d also heard that she had followed the Martial God’s letter, searching for the one called the “chosen one” through the long years.

That only made her words and actions now harder to understand.

Why wasn’t she trying to save the chosen one—or rather, Jin Taekyung?

Her strange look and voice suggested something beyond simple faith that he would survive—something he couldn’t begin to fathom right now.

*Bow Saint, what exactly are you hiding?*

But he had no choice but to force down the question on the tip of his tongue and the doubts in his mind.

The enemy’s assault was growing stronger, as if it wouldn’t allow even this moment’s hesitation.

*Fwoooosh.*

A massive sphere of flame suddenly turned the sky red, wiping away even the wind and rain.

The Slaughter Saint leaped from the wall without hesitation to meet it, the enormous power hurtling toward them.

*Whoosh!*

A streak of light cut through the air along the path traced by his fingertips. A rift opened, followed by an explosion.

*KABOOOOOM!*

The ball of fire shattered into hundreds of pieces and scattered in every direction. The Slaughter Saint landed where he had started and fixed a profound gaze on the Bow Saint.

“Is that answer enough?”

Perhaps she had read the change in his eyes. A bitter smile briefly crossed the Bow Saint’s lips.

“Of course.”

Leaving her behind, the Slaughter Saint silently turned to face the enemies, who had dyed the land outside the wall pitch-black.

More precisely, he looked toward the one who had just displayed magic of a power beyond anything they’d seen so far.

*The Grand Mage.*

The face of another ringleader, who had finally stepped forward, burned itself onto the Slaughter Saint’s eyes.

Four Black Ghosts guarded her like bodyguards.

And then—

*Rumble……*

Feeling a chilling tremor rumble deep beneath the earth, the Slaughter Saint turned his head and looked in one direction.

He thought of the one person in the world who cherished Jin Taekyung more than anyone and would rush headlong into danger for his sake.

*You’re the only one left now. I’m counting on you, Fire King.*

Just as the Slaughter Saint murmured those words in his heart—

*Rrrrrumble!*

Centered on the South Gate, the ground within a radius of over a hundred jang heaved its massive, heavy body upward.

And a man’s voice rang clearly across the battlefield.

—Shake the earth.

Earthquake.

*KABOOOOOM!*

* * *

*Rumble!*

The people who felt the violent tremor begin in the south and spread in every direction reacted in all sorts of ways.

“An earthquake!”

Some, reminded of a disaster no human power could stop, were overcome with fear.

“Don’t falter! What could possibly scare us now?”

Others, already prepared to die, fought the enemy without giving an inch.

“Damn bitch. I hope she hasn’t figured it out already.”

And one person, feeling a familiar power, shot bloody flashes at the moths foolish enough to block his way to the Inner City.

He needed to take one man’s life quickly—and for good—before anything else could get in his way.

But that person—no, the Blood Lord—didn’t know that, several hundred jang away, an even more incredible massacre was unfolding at the North Gate.

“A-a demon……”

*Cough.*

Bloody spittle mixed with bits of entrails slipped from between his lips.

His bright yellow robe was drenched in blood, its original color long gone, and blackened corpses lay scattered all around him.

None of them knew how many had met such a horrific end.

Not even the one who had created this hellscape.

There was only one thing he knew for certain.

*Crack.*

The middle-aged monk whose neck he had just snapped in his grasp was the last surviving member of the Twelve Secret Monks, known as the greatest in Tibet.

“Now you’re the only one left.”

That old monk, frozen like a statue, was the only obstacle still standing in his way.

“……!”

The Dalai Lama’s eyes were wide open, his pupils trembling.

The Fire King, Jeok Cheongang, walked wearily toward the man frozen like a statue as he witnessed the terrible scene.

Thinking of the Disciple who must be in danger by now.

Remembering his own resolve.

“Let’s finish this quickly. He’s waiting.”

*Fwoosh.*

A white flame spread across his fatigue-dimmed pupils.
## Chapter artifact 1112

# Chapter 1112

*Is this a dream?*

The Dalai Lama wondered.

At the same time, he wished for it more desperately than ever before.

If all of this really was a dream—a terrible nightmare—then he wanted to wake from it as soon as possible.

And he never wanted a nightmare like this to come again.

But—

*Grind.*

The pain from his bitten lip, the stench of blood seeping into his nostrils, and the acrid smoke surrounding him all whispered the same truth.

That this utterly horrific, unbelievable scene was real.

“Truly…… there’s no mistaking it. He’s a fiend.”

The Dalai Lama muttered like a groan.

At that moment, the figure reflected in the old monk’s eyes was no different from a demon torn from an ancient scripture.

A fiend who had burned to death not only the Twelve Secret Monks—his Disciples and fellow martial brothers—but even the two Black Ghosts who had been such dependable reinforcements.

“Fire King Jeok Cheongang.”

His voice trembled, anger and fear mingling in it.

By contrast, the fiend striding toward the old monk showed no hint of hesitation.

*Whoosh.*

Embers scattered. The air grew hot.

The Dalai Lama’s eyes flew wide open. Jeok Cheongang had closed the distance of more than ten jang in an instant and was rushing straight at him.

White flames flickered at Jeok Cheongang’s fingertips.

*BOOM!*

Compressed air exploded, and the flames swallowed wind and rain.

*KABOOOOOM!*

Was this what a wave of fire looked like?

Watching the searing heat sweep through the place where he had stood just moments ago, the Dalai Lama felt a chill run down his spine.

“Flame Divine Palm……!”

There was no way he wouldn’t recognize it.

It was the fiend’s martial art, passed down for two hundred years from the first record left by his ancestors—and the very thing that had driven all the Twelve Secret Monks, including two Supreme Peak masters, to their deaths.

“You know it, at least. Did word of this old man spread all the way to that backwater?”

*Whoosh!*

A low voice rang out above him, followed by the sound of something tearing through the air.

Jeok Cheongang had already emerged through the acrid smoke. His tightly clenched fist came crashing down toward the crown of the Dalai Lama’s head.

The Flame-Extinguishing Divine Fist—the technique that had reduced the two Black Ghosts to ash before the Twelve Secret Monks met their end.

*KABOOM!*

The ground shook. A pillar of fire shot upward, and the rolling heat burned skin at a mere brush.

*Sizzle.*

The pain was like being seared with a branding iron.

Yet the Dalai Lama dodged the attack by a hair once more, then thrust both palms forward with all his strength.

*Crack!*

Their hands met. The immense qi within them tangled and collided without pause.

But unlike a moment ago, the fear was gradually fading from the Dalai Lama’s eyes as he clashed head-on with Jeok Cheongang.

*He’s strong, but that’s all.*

He could feel it clearly through their joined hands.

Jeok Cheongang’s qi—the same man who had displayed such unbelievable power mere moments ago—was wavering sharply.

And that was the truth his fear had briefly obscured. The truth Jeok Cheongang wanted to hide.

Nothing comes without a price.

Perfected Being Hyeoncheon of the Kongtong Sect, who had helped Jeok Cheongang defend the North Gate, was already down with severe internal injuries after fighting amid a clash between no fewer than five Supreme Peak masters.

Even Jeok Cheongang’s body couldn’t have come through that unscathed. At last realizing this, the Dalai Lama stared at the enemy before him with a baleful gaze.

The fear that had briefly driven out his anger was gone. His anger returned in its place.

“You’re gravely mistaken.”

“What?”

“People don’t know of you because of Fire King Jeok Cheongang. They learned of you from your ancestor—the one who should have fallen into the Eight Hot Hells long ago.”

The Dalai Lama spoke, biting off every syllable.

“Our Potala Palace never forgot. No—we came to a point where we could never forget.”

It had all begun more than two hundred years ago, on the day a wild-haired stranger in blood-red rags set foot in Tibet.

For the Potala Palace, it was the deepest, most devastating wound—and a history of humiliation that could never be washed away.

*Bring in that suspicious foreigner staying at an inn in Chamdo immediately. I will personally interrogate him to find out who he is, where he came from, and why he’s here.*

The Dalai Lama of that era, who had issued this order, could never have guessed what would happen.

They had considered themselves powerful enough in Tibet to rival the Demonic Cult, and had never imagined some clueless foreigner would have the nerve to defy them.

Nor could they have imagined that the foreigner, after turning more than twenty martial monks sent to capture him into cripples, would charge into their palace with his eyes rolled back in his head.

*Who are you? Which bald bastard ordered you to smash the meal this old man finally got after three days?*

Perhaps that had been their last chance.

They could have started by apologizing for the martial monks’ rather rough attempt to make contact with the stranger.

Then they could have prepared enough meat and liquor to make the table sag, to make up for interrupting his deeply gratifying first meal in three days.

And, in an atmosphere warmed like a firebox stuffed with kindling, they could have talked.

If only they had done that.

But, as the recorded history proved, no such heartwarming turn of events had followed.

Twenty martial monks had already been crippled for overturning the man’s table and trying to use their weapons. And the Potala Palace, which rigorously upheld the principles of non-killing and abstinence, had neither liquor nor meat on hand to calm the stranger down.

That day, the stranger had charged straight into the Potala Palace’s main sanctuary in a fit of rage. Instead of enough liquor and meat to make a table sag, there were two hundred martial monks who could break a person’s limbs with their bare hands.

Among them were the Dalai Lama of that era, acknowledged by all as Tibet’s greatest master, and four of the Twelve Secret Monks, who served closely at his side.

*You seem like a fairly well-known martial artist from the Central Plains…… If you surrender peacefully now, I’ll settle this with twenty years of wall-gazing meditation. What do you think, donor?*

But the stranger gave the Dalai Lama a firm answer.

*That’s a terrible deal. I refuse.*

*Good grief. You’re making this difficult.*

*You bald monks made this what it is. This old man hasn’t done a damn thing wrong. At least, not yet.*

*……Not yet?*

*Ahem. Anyway, I was planning to rest for a while and then leave quietly. This time, at least.*

*……This time, at least?*

*I didn’t like it when bald monks I’d never seen before came barging in out of nowhere. But if you’d waited quietly in a corner until I finished eating, I would’ve gone along with it. Hell, if you hadn’t tried to force me down, none of this would’ve happened.*

*I can’t say you’re entirely wrong. Still, even allowing for my Disciples’ slight discourtesy, your response was excessive.*

*They overturned my precious meal and even tried to use weapons. And you call that a slight discourtesy?*

Faced with the pointed question, the Dalai Lama chose silence over admitting the truth. The stranger watched the Dalai Lama, who already seemed more like a martial artist than a monk, then let out a long sigh.

*Hearing you say that, I deeply regret it.*

*Oh? Really?*

*Of course. I swear it to Heaven and Earth.*

The stranger’s next words sealed everyone’s fate.

*I should’ve crippled them all completely instead of leaving them half-crippled.*

*……You’re a fiend to the bone. What can be done now? It’s come to this. Please, don’t hold it against us. May you find peace in your next life.*

And so, the killing began.

A storm of blood swept through—not from both sides, but from only one.

A dreadful storm of blood that would be remembered for more than two hundred years, and would still be remembered a thousand years later, as long as the Potala Palace endured.

“One hundred were killed that day, right there. Another hundred were crippled.”

The Dalai Lama, once more recalling the humiliation of his sect, spoke in a voice edged with iron.

His gaze fixed on Jeok Cheongang was colder than ever. The anger simmering in his unwavering voice had swallowed his fear.

“The previous Dalai Lama died then, too.”

The four Twelve Secret Monks who had been there with him barely survived, but like the martial monks who lived through it, they were never able to use martial arts again.

“It was a terrible humiliation. Something that should never have happened—and could never have happened.”

It had all unfolded in barely half a day. Every martial monk of the Potala Palace, scattered throughout Tibet to maintain order, rushed to the main sanctuary with all their might.

And at last, they saw it.

The main sanctuary, so magnificent in its heyday, lay in utter ruin. One of its charred, uprooted pillars bore a line of writing scrawled across it.

> [The Jade Emperor says: Even a dog should be left alone while it eats.]

And beneath those words, whose source was deeply suspect, the writer had carefully inscribed his credentials at equal length and in grandiose style.

“Fifth Sect Leader of the great Fire Gate Clan. Ghost Flame Fist Songhak.”

The Dalai Lama ground out that accursed name, still passed down to this day.

“If we’d captured him then, none of this would be happening today.”

But Ghost Flame Fist Songhak was never captured by the martial monks and sent off to meet Yama.

After etching an indelible humiliation into the Potala Palace, he melted through the net over heaven and earth laid by Tibet’s Murim and headed straight for the Central Plains.

He’d avoided pursuit by the Mad Wind Society of the great desert—the decisive reason he’d set foot in Tibet in the first place—even though they’d kept him from eating for three days. The man had cared about meals more than any other Sect Leader in the Fire Gate Clan’s history.

Then, with a satisfied heart, he returned to Mount Jiuhua, the Fire Gate Clan’s home, and briefly recorded his thrilling exploits.

> I have always held the Fourth Ancestor, the Third Sect Leader, in the deepest respect. In pursuit of his deeds, I explored the world and the Outer Murim.
>
> As it happened, I fought the Mad Wind Society of the great desert beyond the hot sands, and uprooted the Potala Palace’s very pillars.
>
> All the men and horses of Tibet were enraged and pursued me.
>
> But who am I?
>
> I, Ghost Flame Fist Songhak, Fifth Sect Leader of the great Fire Gate Clan. Without so much as a hair harmed, I…… evaded them and returned safely to the Central Plains.

Of course, Ghost Flame Fist Songhak didn’t know that more than two hundred years later, a distant descendant would find his proud record and mutter that he was a madman.

Nor did he know the Potala Palace would hold on to this grudge for so long.

In truth, he hadn’t cared in the slightest.

“I learned later that he’d already slaughtered more than five hundred of the Mad Wind Society’s mounted bandits in the desert.”

The Mad Wind Society had tried to steal Songhak’s horse—and lost most of its leadership instead. Unable to withstand the damage, it eventually disappeared into the pages of history. The Potala Palace, however, had not.

They had no rivals in all of Tibetan Murim, and quietly resolved to take revenge.

Some scholarly monks argued they should forgive and show mercy to avoid causing even more bloodshed, but they were no match for the fury of the martial monks, who were closer to martial artists than to monks.

And so, the Potala Palace gradually changed.

They began to value books on martial arts more than scriptures and dramatically increased the number of martial monks, accepting only gifted children.

“We swore that even if Ghost Flame Fist died and turned to dust before we could avenge that day, we would cut off the line of those fiends with our own hands.”

By the time the rivers and mountains had changed nearly ten times over—

The Potala Palace had become a formidable military force, far surpassing anything it had been in the past.

So powerful that even they believed the time for revenge had come.

But about a hundred years ago, the boy chosen as the new Dalai Lama at a young age, according to Potala Palace tradition, wasn’t satisfied with that.

“We had certainly grown stronger, but it still wasn’t nearly enough. To exact our revenge ourselves, we would have to face the Central Plains in its entirety.”

Just as Songhak had been treated as an outsider when he set foot in Tibet, the Potala Palace was nothing but a group of outsiders in the Central Plains.

And they were a military force powerful enough to bring about a storm of bloodshed if things went wrong.

Even though the Fire Gate Clan had steadily built up gratitude and grudges by stirring up all manner of trouble, there was no chance the martial artists of the Central Plains would hunt them down and hand them over so dangerous outsiders from the west could take revenge.

“In the end, all we needed was greater strength. Or…… an alliance strong enough to stand against the Central Plains.”

*Crack.*

The strength flowing through their tangled hands surged, slowly forcing Jeok Cheongang’s hands back.

The balance of power that had held steady was finally beginning to collapse.

“The Demonic Cult was truly foolish. The arrogant Heavenly Demon mocked us for being weak. That was his greatest mistake.”

“The Great Faction War…… Hah. I thought you were just a bald monk consumed by an old, unjustified grudge. Now I can’t even call you a monk.”

Jeok Cheongang swallowed a mouthful of blood that surged up and stared at the Dalai Lama with a scornful gaze.

“How ridiculous. Don’t you think?”

“What?”

“Look at yourself. You’ve joined hands with fiends worse than the Demonic Cult, and you dare call anyone else a fiend?”

“……!”

The Dalai Lama’s body jolted to a halt.

The terrible aura flowing from Jeok Cheongang, who had suddenly shouted at him, made him see his true reflection in those eyes pouring flames.

Red. They were red.

The Dalai Lama’s eyes had gradually taken on the color of the pool of blood at his feet.

Slowly, but surely.

“After all that, you even broke a taboo for that pathetic strength.”

“N-no. I……!”

His voice and eyes trembled.

But no words could deny the truth of the past.

He had needed to grow stronger. Somehow, he needed more and more power.

The countless pills and martial arts Dark Heaven offered had made that possible.

No—more precisely, that new power, infused with demonic energy, had made it possible.

Jeok Cheongang let out a quiet laugh at the Dalai Lama, who had just been caught in a contradiction he’d forgotten—or desperately tried to ignore.

“If you’ve got nothing to say, shut your mouth. Even this old man, with a strong stomach, can’t take the disgusting excuses spilling from a fiend’s tongue.”

“You bastard! Shut your mouth!”

*Fwoosh!*

A vast aura surged in every direction.

Using his blazing rage as kindling, the Dalai Lama finally wrung every last bit of power and potential from deep within himself and drove his full strength against the enemy before him.

*Crack!*

The balance of power had tipped decisively.

As the sound of bones shifting rang out and the flames gathered around Jeok Cheongang’s hands began to dim, a single azure dragon’s roar burst from between his bloodied lips, bearing witness to his mounting injuries and exhaustion.

“Hyeoncheon! Now!”

At that moment—

*Shhhhh.*

The Dalai Lama, moving through the slowed world, tore his hands free of Jeok Cheongang’s grip with all his strength. He spun around, feeling the hairs all over his body stand on end.

At the same time, he remembered someone whose existence had briefly slipped from his mind.

The Kongtong Sect Leader—the man he had thought already incapacitated.

Far off, he saw Perfected Being Hyeoncheon leaning against the corpse of a huge elephant, breathing faintly. The Dalai Lama froze.

No.

*Crack!*

At that very moment, the terrible heat that drove deep into his body gave him no time even for that instant.

“……!”

His body trembled as if pierced by lightning.

But not a drop of blood, not a single scream, came from him.

The flames had vaporized the blood that should have burst out and inflicted such distant, unbearable pain that he’d even forgotten how to cry out.

But perhaps the greatest pain of all for the Dalai Lama was the low voice of his enemy, now piercing his ears.

“Fire King Jeok Cheongang says: Never harm a being who has something they must protect, even if that being is a beast.”

Like the ancestor who had carved his own words into a Potala Palace pillar, Jeok Cheongang whispered in a faint yet clear voice.

He clenched his hand, which had pierced through his enemy’s back and burst out through his chest.

“Especially if that being belongs to the Fire Gate Clan.”

The Dalai Lama couldn’t answer.

Even as every sense connecting him to the world went dark, even as darkness swallowed his vision completely.

“Go on ahead, fiend of Tibet. This old man still has something to protect.”

*Thud.*

At last, his head slumped limply.

Along with his enemy’s final words, echoing like Yama’s, the world surrounding the Dalai Lama closed in.
## Chapter artifact 1113

# Chapter 1113

Nothing can be gained without sacrifice.

That was even more true for those seeking victory through war—the most terrible form of violence—in an age of savagery that had thrown law and benevolence to the dogs.

But even knowing that cruel reality, there were some things one could never get used to.

Like realizing that someone who had been laughing and talking with you only moments ago was gone.

“……So, it ended that way after all.”

After hearing what had happened immediately after he lost consciousness, Jin Taekyung quietly closed his eyes, muttering to himself.

And at the same time, someone came to mind.

Though they had shared little time, so many pairs of eyes had looked at him with trust.

Along with them came the stony face and voice of someone whose presence had gradually become familiar.

*“It doesn’t matter who you are. The Embroidered Uniform Guard obeys only His Majesty the Emperor’s command. If you stand in our way in defiance of his imperial decree, I’ll kill you.”*

*“Perhaps it’s because you’re a martial artist without even an identity tag, but your manners are atrocious.”*

*“Thank you. For protecting us—for protecting the imperial family.”*

Fleeting moments brushed past his eyes and ears, faint as mist.

And at the end of those memories was always the figure of someone who had pressed forward without wavering.

*“Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard, answers the command of the Marquis of Shangshan!”*

Remembering the voice he would never hear again, Jin Taekyung opened his eyes without a word and forced down something rising up from deep in his chest.

The officer had been so stubbornly steadfast it was almost foolish. He had always been calm, and always stood tall.

Taekyung had lost consciousness before witnessing Jeong Hogun’s final moments, but he was certain they had gone that way.

Because that was the kind of man he was.

The Embroidered Uniform Guards who had served under Jin Taekyung over the past three months must have been the same. So must the defenders at the West Gate, who had fought with their lives on the line.

They had all fought to protect others, and gone up in a blaze of glory.

Jin Taekyung would remember forever that, thanks to their sacrifice, no small number of people—including him—had survived.

So would the person beside him, head bowed as he shed tears.

“……I’m sorry, Benefactor. I wasn’t good enough.”

His eyes glistened, and his voice trembled.

Looking at Cheongpung as he blamed himself, Jin Taekyung spoke in a calm voice.

“You’re right. We weren’t good enough. Neither you nor I.”

“No. You did everything you could. If only I’d been a little stronger……”

“Young Hero Cheongpung.”

“Yes?”

“If only the Blood Lord—or no, the Lord of Heaven—had never been born in the first place. Wouldn’t that have been nice?”

“……!”

“Those stupid thoughts—what if, maybe, if only—get them out of your head. Even if you feel terrible for the dead, even if you hate yourself like crazy for surviving, bear it.”

His teeth ground together.

Jin Taekyung slowly shifted his body, which had been propped against the Inner City wall. He clenched his jaw without meaning to, against the terrible pain that seemed to reach every cell in his body.

And against the fury and self-reproach he had been trying with all his might to hold back since regaining consciousness, though they kept surging up from deep within him.

His legs suddenly gave way like a puppet with its strings cut.

Jin Taekyung managed to grab the wall, but he staggered. Cheongpung reached out in alarm to support him.

Or, more precisely, he tried to.

Until Jin Taekyung firmly shook his head before that helping hand could reach him.

“B-Benefactor.”

In Cheongpung’s unsteady eyes, Jin Taekyung forced himself upright.

A sheen of sweat had begun to run down his forehead, and his face was deathly pale.

But what showed on the outside was not the whole story.

Cheongpung, who had poured his internal energy into Jin Taekyung to lend him strength, knew better than anyone that his insides were in even worse shape than they seemed.

Some of the tears he had shed earlier had come from a terrible premonition: that he would be unable to stop Jin Taekyung from dying.

But—

Thump.

Jin Taekyung did not stop. He did not give up.

Bearing the pain with everything he had and tamping down the emotions boiling like lava in a corner of his chest, he gripped the wall and stood up again.

Slowly. And stubbornly.

Then, through a distance so vast that each second felt like ten years, he forced the words out.

“Think about why we survived. Why they had to give up their lives to save us.”

They couldn’t let that happen. They mustn’t.

If they fell apart now, if they gave up, everything would have been for nothing.

The sacrifice of those who had given their lives to open a path of retreat.

The sacrifice of others who might even now be dying.

“Save your apologies to the dead and your sobbing until after we’ve finished everything we have to do.”

He wasn’t speaking only to Cheongpung.

Jin Taekyung kept speaking resolutely to everyone around him. Their heads hung low, their faces marked by desperation or defeat. Exhausted in body and mind, they had briefly forgotten their duty.

“That’s the only way…… we can show them the respect they deserve. It’s our duty.”

Step.

The moment Jin Taekyung finally took a step after forcing out those last words—

“……!”

“……!”

The air around them rang.

An invisible surge and heat rose as one.

One step.

He had moved only one step.

He looked wretched—a young man covered in blood, who wouldn’t have seemed out of place if he collapsed right then and there.

But why?

Just watching him made their hearts pound.

The oppressive defeat that had taken hold of their whole bodies slowly lifted, and something hot filled the space it left behind.

Thump. Thump. Thump.

A pulse whose source no one could name began to spread like ripples across a still pond.

Outside the Inner City, the war drums grew more urgent, signaling death’s approach. But it didn’t matter.

At least not now.

As long as they stood with him—a martial artist who had crossed a mountain of sabers and a forest of swords, a Great Nation’s marquis, and, beyond that, one of the people living in this vast world.

For a moment, they could forget.

They could remember something they had forgotten.

KABOOM!

Even when a thunderous crash sounded in the distance and the war drums that had seemed destined to ring forever fell silent.

But the tremors of countless enemy footsteps swept down the avenue toward the Inner City.

The clash of steel rang out, and desperate screams filled the air.

Still, they stamped their feet with all their strength and brought their weapons down, fanning the embers of a battle cry that had yet to die.

Thinking of the countless people huddled in the depths of the Inner City, trembling.

Holding the image of one man in their heated eyes.

“Remember this, all of you.”

They watched the silver-white spearhead slowly rise, his voice now clear.

“What we’ve been alive for all this time.”

Shing.

At that moment, the spearhead gave off a frosty aura, and Jin Taekyung spat out his words.

Swoosh.

Behind him, standing tall as an iron tower, strands of violet light rose and blazed brighter than torches, illuminating the darkness.

And beneath the energy of the Zaha Divine Technique spreading like the sunset at dusk, the corner of one person’s eye was no longer wet.

His voice, sunk deeper than ever, was the same.

“I’ll do it. I promise.”

The battle was not over yet.

* * *

Red. Everything was red.

At least, every part of one person’s view was submerged in corpses and blood.

Slice!

How many lives vanished with a single deep breath?

Heads flew everywhere. Limbs went sailing. Some died slowly, writhing in agony.

Some had been Daoists in fluttering white robes, as refined as immortals; others had been government soldiers living on the nation’s payroll. They had been martial artists and common people, too. Now it was impossible to tell them apart.

Drenched in blood from head to toe, they had become part of the hellscape painted across Xining’s main road.

The man who had drawn the first strokes of this hellscape and would put the final touch to it watched the slaughter unfold before his eyes.

*What a bunch of fools.*

He couldn’t understand it.

What were they fighting for?

For an emperor who had earned his place through nothing but his bloodline?

Or for that embarrassing word, “justice,” which had no shape or form?

*Ridiculous.*

Most of them had probably never even seen the Emperor’s face. And the justice the Central Plains martial artists were so willing to die for was nothing more than something made within their own little walls.

But the Lord of Heaven was different. The Lord alone.

His power and presence were so overwhelming that just being near him made one tremble.

In a world where might made right, what ruler could be more fitting?

*This loyal servant will fulfill your wish.*

With a vow he couldn’t tell whether he made to the Lord of Heaven or to himself, the Blood Lord shot forward.

Whoosh!

A moment after the horrifyingly low whistle of air, the front line of defenders—still refusing to give up the fight as they blocked the main road to the Inner City—crumpled helplessly.

A hundred bodies collapsed like puppets with their strings cut, and a torrent of dark blood burst high into the air.

Splatter!

Blood sprayed in every direction.

Among the defenders who witnessed the unbelievable sight, a trembling voice escaped someone’s lips.

“A-a monster……”

“Yes. I suppose that’s what I look like to you.”

The Blood Lord smiled as he replied, then reached out.

Boom!

A flash of blood-red light swelled and exploded. The blast swallowed their screams, scattering torn flesh and bone.

“But after he takes the world, who will call me a monster?”

It was a world where might made right.

It wouldn’t be long before the blood-mad monster was hailed as a divine general sent by Heaven.

Though he had failed to take the life of one man whose death was necessary for that great undertaking—

“Open the way, you worthless moths.”

Slice! Thud-thud-thud!

To the Blood Lord, all of it was only a matter of time.

The Inner City was already close enough to see clearly. And while fierce battles continued at the other three walls, there was no one who could block his path.

*Grand Mage, you bitch, stay out of this. Even I don’t want to kill a servant girl the Lord of Heaven favors with my own hands.*

The Blood Lord was about to continue his slaughter, muttering to himself—

Whoooooosh! Boom!

A sharp, dazzling flash blocked the monster’s steps, which had seemed impossible to stop.
## Chapter artifact 1114

# Chapter 1114

The beam of light that cut through space in an instant was dazzling—and devastating.

Even barehanded, the Blood Lord had been mercilessly slaughtering the defenders. The flash had been powerful enough to make him draw the beloved blade that had rested quietly at his waist.

KABOOM!

A deafening crash—and blood sprayed in every direction.

But this time, unlike before, the blood hadn’t come from the defenders. It came from the fanatics who followed the Blood Lord.

“C-cough. Blood Lord……”

Had the man been lucky, or unlucky?

Unlike the dozens of comrades who had been caught in the sudden flash and died without even a chance to scream, this fanatic had barely survived. He crawled toward the Blood Lord, hoping the great Apostle chosen by the Lord of Heaven would ease his pain, even a little.

And the Blood Lord answered his desperate plea.

With a foot weighted by a thousand geun.

CRUNCH!

His spine broke. That was the end of it.

The Blood Lord didn’t know whether the man had been clinging to the last thread of life or hoping to find peace in death.

No—that wasn’t quite right. The truth was that the death of a nobody, little more than a disposable pawn, had never interested him in the first place.

The Blood Lord’s gaze had been fixed all along on the other side of the thick cloud of dust.

“Come out.”

The instant his cold voice left his lips—

Swoosh!

A flash of light burst out of nowhere, splitting the cloud of dust as it surged toward him.

To be precise, it was heat shining like a flash of light.

Fwoosh—KABOOOOOM!

Flames roared through the air, sweeping toward him.

The dreadful heat made his suspicions certain. The Blood Lord swung the Red Blade down with all his might.

Slice!

With a keen cutting sound, the flames split in two.

The avenue, more than twenty jang wide, was engulfed in fire in an instant. Through the shimmering heat rising in waves, a person’s shadow wavered.

“Where are you in such a hurry to go?”

His voice was low and steady.

And even through the heat haze, his eyes shone clearly as flames poured from them.

Fire King Jeok Cheongang.

It was him.

The Blood Lord’s eyes narrowed at the sight of Jeok Cheongang. He hadn’t expected the man to appear yet—and had thought he might never see him again.

“So the head of the Ten Kings, whom the orthodox faction praises so highly, is no more than a mere warrior after all. You abandoned all those allies to save your one and only Disciple?”

The Blood Lord spoke with scorn, certain Jeok Cheongang had abandoned the North Gate to come here.

Jeok Cheongang caught his breath before replying.

“I never asked anyone to praise me. But everything has its reasons.”

“What?”

“Since the day I defeated a thousand demonic soldiers, the world has called me the Fire King. It’s been so long that I was starting to grow tired of the title…… But perhaps that will change after today.”

“……!”

The Blood Lord’s face twisted as he finally realized what Jeok Cheongang’s appearance meant.

The Potala Palace forces sent to the North Gate had certainly been formidable.

The Dalai Lama, the greatest master in Xizang, and the Twelve Secret Monks, who included two Supreme Peak masters—even if they were still greenhorns.

And, to prepare for any unforeseen circumstances, they had sent two Black Ghosts as well. It wouldn’t have been surprising if they’d done more than hold Jeok Cheongang in place—if they’d even taken his life.

*But how?*

The Blood Lord couldn’t find an answer to the question that had crossed his mind without his realizing it.

No. Perhaps he would never find one.

The battle between those fighting to protect something and those consumed entirely by revenge could often defy expectations by a wide margin.

And Fire King Jeok Cheongang had someone he would protect, even if he had to give everything he had.

“Did you really think a few bald monks like that could stop this old man?”

At the low voice that burrowed into his ear, the Blood Lord clenched his teeth.

“You crazy old bastard. No matter how hard you struggle, nothing will change.”

“I protected him. And I will again.”

“You mean that precious Disciple of yours, who might be dying even as we speak?”

“……What did you say?”

Jeok Cheongang instinctively hesitated. The Blood Lord twisted his mouth into a smile.

“No. That’s not right. Perhaps he’s already dead. Last I saw him, he was hovering at death’s door.”

“You dare……!”

The moment Jeok Cheongang heard his Disciple was in danger and was swept up in an emotion he couldn’t hide—

Whoosh!

With a faint whistle of air, the Blood Lord’s figure vanished like an illusion. He crossed more than ten jang in an instant and came crashing down on him.

Slice!

The ground split as easily as tofu.

At the same time, Jeok Cheongang twisted just enough to evade the attack, but blood burst from several places on his body.

Thud-thud-thud!

The overwhelming Sword Pressure caused damage with nothing more than a near miss.

Yet Jeok Cheongang knew better than anyone what the blood scattering through the air meant.

*My body……!*

It felt as heavy as a thousand geun. His senses were slow to respond, too.

Jeok Cheongang realized he’d forgotten something important in his anger and desperation: how exhausted his body was after the grueling battle at the North Gate.

And how severely his momentarily uncontrollable emotions could hinder him in a life-and-death duel like this.

The Blood Lord saw right through Jeok Cheongang’s condition.

KABOOOOOM!

A storm of blade strikes tore through the air.

Dozens—no, hundreds—of attacks rained down on each other, as if even time itself were being sliced apart. Jeok Cheongang, already exhausted, instinctively sensed that the fight was nearly over.

He knew the end would bring his death. He knew, too, that he had only one card left that could change it.

*Dance of the Fire God and Demon.*

A final flame, kindled by burning everything he was.

A divine art passed down through the generations of the Fire Gate Clan—and forbidden because of its terrible aftermath.

Jeok Cheongang had already once faced death because of it. But now, it was all he had left.

The only way to defeat the Blood Lord, whose power could do more than heal—it could Regenerate.

But perhaps even the brief moment he spent considering it was a luxury. Every instant was a crisis for Jeok Cheongang now.

*An opening!*

The Blood Lord’s eyes flashed in that split second.

Whoom!

Instead of the Red Blade, which was embedded deep in the ground, a fist swung with all his might toward Jeok Cheongang’s side like a cannonball.

Since falling into danger after Jin Taekyung’s One Annihilation, the Blood Lord’s strength and speed had somehow grown even greater.

“……!”

Jeok Cheongang didn’t even have time to gasp.

His body was exhausted, his senses dulled, and his internal energy had all but run dry.

The best he could do was cross his Force-clad arms with all the strength he had.

KABOOM!

His vision flipped with the deafening crash.

Jeok Cheongang’s body shot across more than ten jang and smashed through a large inn that had once been crowded with people.

CRASH!

A pillar fell. Wooden splinters flew everywhere.

Only after he’d smashed through seven buildings, starting with the inn, did Jeok Cheongang cough up something hot rising violently from his gut.

Puhak.

Blackened blood stained some back alley or other.

Through his blurring vision, he saw the Blood Lord rushing toward him like a gale.

There was joy in those blood-red eyes, along with killing intent.

“Jeok Cheongang!”

The Blood Lord roared his name and swung the Red Blade down—

CLANG!

A sharp crash rang out.

The Blood Lord was forced back, eyes wide with disbelief, after deflecting five streaks of light fired from an unexpected angle.

Whoooom.

A vibration traveled through his grip.

The Red Blade trembled, then quickly steadied. But the Blood Lord’s face, twisted like a Fiend’s, did not.

“Not bad…… But if you’re old enough to have lived this long, you should know when to stay out of it. Don’t you think?”

His growling voice came with the slow turn of his head.

The Blood Lord’s blood-red gaze flashed toward the five old men standing in front of Jeok Cheongang.

“If you don’t want to be torn limb from limb and die.”

But even in the face of that overwhelming killing intent, the slender old Daoist at their center quietly helped Jeok Cheongang to his feet.

Fwoosh.

As internal energy flowed into him, color began to return to Jeok Cheongang’s deathly pale face.

Jeok Cheongang coughed up another mouthful of blood. The old Daoist spoke calmly.

“Thank you for all you’ve done. We’ll take it from here.”

“Cough. You’re……”

“Jin Taekyung may not have much time left.”

“……!”

“Go. Quickly. It’s for everyone’s sake, too.”

Of course, the word “everyone” in the old Daoist’s mouth left out one person.

“Ha. Now there are six crazy old men.”

With a sneer, the Blood Lord tilted the Red Blade down at an angle.

“Then die, all of you.”

Swoosh!

A crescent of blood-red Force shot along the Red Blade.

The strike carried a horrifyingly immense power, its Force stretching a full jang in size.

And the very next moment—

KABOOM!

A crash like the sky splitting apart rang out. The entire area within a ten-jang radius crumbled to dust.

Beneath the six figures standing in midair, high above the ground.

“……!”

As the Blood Lord’s gaze darkened, the slender old Daoist—the same one who had been supporting Jeok Cheongang—bowed his head slightly toward him.

“Please forgive the impertinence of someone so far your junior.”

Jeok Cheongang was already suffering from severe exhaustion and Internal Injury, accumulated since the North Gate. He couldn’t even answer.

No—that wasn’t quite right. There was no time.

Before he could reply, the old Daoist’s arms swung with force.

“You crazy—!”

By the time the Blood Lord’s frantic shout rang out, it was already too late.

Whoooosh!

Jeok Cheongang’s body shot through the air toward the Inner City with a fierce whistle.

Before the enraged Blood Lord could chase after him, the five old Daoists landed softly on the ground and blocked his way.

They had the bearing of immortals and an aura like noble cranes.

And their astonishing movement technique, which they had just displayed.

Only then did the Blood Lord realize who the uninvited guests were. He spoke in a chilly voice.

“The Kunlun Five Immortals.”

“You know us?”

“How could I not? It’s a heartbreaking story: old men who should have died long ago, still eating up the Kunlun Sect’s rice.”

Naturally, the Blood Lord’s idea of them was worlds apart from how they were known to the public.

The Kunlun Five Immortals were the Martial Uncles of Cheongheoja, the current Sect Leader, and Elders who had sustained the Kunlun Sect well into their eighties.

Though each of them had stopped just short of Supreme Peak, their reputation was that the cooperative technique they’d developed through a bond like that of brothers, having grown up together since childhood, could not be broken even by a Supreme Peak master.

Of course, right now, to the Blood Lord, they were nothing but a few more troublesome, aged moths.

“Get out of my sight. I’d like to tear you apart and kill you in an instant, but you’re not worth the time.”

The slender old Daoist, the eldest of the Kunlun Five Immortals, Perfected One Taecheong, shook his head.

“I cannot accept that offer. Allow me to propose an alternative.”

“There is no alternative. And you just threw away your last chance.”

The Blood Lord let the Red Blade hang at an angle and stepped toward the Kunlun Five Immortals.

First Jin Taekyung, then Jeok Cheongang.

Twice now, he’d lost prey he’d nearly caught—prey he had to kill.

Their aura felt far stronger than what was known to the world, which was puzzling. But their cooperative technique, said to let them face even Supreme Peak masters, would be no more than a house of cards before him. It would collapse in an instant.

Or so he’d thought.

“You’re mistaken. We still have a chance.”

“What?”

“This is the alternative we came up with.”

The Blood Lord noticed the calm smile on Perfected One Taecheong’s lips and sensed something was wrong.

Shaaaaa.

An overwhelming power rose around Perfected One Taecheong—or rather, around all five of the Kunlun Five Immortals—and shook the space around them.

Their fierce aura was hard to believe in men whose skill was said to have stopped at the very edge of Peak. It was so rough, it made the immortal meaning of their title seem absurd.

And the Blood Lord didn’t need long to recognize what felt so familiar about it.

“You…… No way.”

“As I’d heard, this is a fearsome thing. This Temporary Strength Pill.”

“……!”

“Don’t be so surprised. We’ve never practiced demonic martial arts in our lives. To take this, we had to pay a price.”

Perfected One Taecheong was telling the truth.

The Temporary Strength Pill was a power usually reserved for those who practiced demonic, heterodox arts—especially those whose skill was incomplete and who had not reached Supreme Peak.

So even if those who practiced righteous energy got their hands on one of the spare pills carried by Dark Heaven’s followers and took it, it wouldn’t have much effect.

There was only one way.

To break the innate qi they’d built up over more than eighty years, forcing themselves to absorb the energy in the pill.

Unless they did something mad like that.

“To stop a monster……”

Whoooom.

His voice trailed off amid a deep rumble.

At the same time, a restless, pale Force—undeniably Force—covered the sword in Perfected One Taecheong’s hand.

No. It surged up along the swords of all five Kunlun Five Immortals.

“If that’s what it takes, then we’ll gladly become monsters, too.”

At that moment—

Whoosh!

Space split, and six figures clashed in a tangle.

* * *

Fifteen minutes.

That was all the time the Kunlun Five Immortals could stay on their feet.

But to someone else, it was a full fifteen minutes.

Perhaps that was why Perfected One Taecheong could smile even through the distant pain of having both his legs torn off.

Slice!

Why he could swallow his screams as his arms were cut off.

Boom!

Why, even as his internal organs were torn apart, the old Daoist could hold to his Daoist principles and offer a final farewell to his Junior Brothers, who had already stopped breathing.

“Remember…… Our deaths will not be in vain……”

CRACK!

His brain matter burst out with a horrible pop.

The Blood Lord lifted his foot from Perfected One Taecheong’s shattered head and whispered coldly.

“No. This is a meaningless death.”

As he slowly raised his head, he heard a roar from all around him—louder and closer than ever.

No. It was a creed of exactly eight characters.

Above heaven and below heaven, ten thousand demons bow in homage.

Above heaven and below heaven, let all things kneel.

“……So it shall be.”

Leaving those low words behind, the monster continued toward the Inner City.

With sticky blood at his feet.

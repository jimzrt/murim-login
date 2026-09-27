# Checkpoint Review — 1165–1169

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

# Chapters 1165–1169

## Plot

Jin Taekyung and the arriving allies fight through Morgoth’s forces and Guardians. As Morgoth’s spells push Jin to exhaustion, Jin enters Trance, reads and splits Dragon Breath with Heavenly Strike, then strikes Morgoth’s unhealed wound from the Skeleton King. He cuts off Morgoth’s wings and defeats him with Open Heaven, the Fire Dragon Divine Spear’s Third Form.

Humanity rallies after the victory. System notices register Jin’s new spear form, martial-arts advances, and level-ups that heal his physical injuries. Morgoth, gravely wounded with his Dragon Heart exposed, says he spent millennia seeking God and believes Jin is chosen by God. The Skeleton King’s head appears in Jin’s arms and speaks to him.

## Continuity

- Humanity defeated Morgoth; the surviving allied forces are wounded but rallying.
- Morgoth is gravely wounded and nearing death, with his Dragon Heart exposed. His fate remains unresolved.
- Jin’s physical injuries healed through leveling up, but he remains severely mentally exhausted. His Fire Dragon Armor was destroyed.
- Jin created Open Heaven, the Fire Dragon Divine Spear’s Third Form. Fire Gate Divine Technique and Qi Sense reached the ninth star.
- Jin gained insight into the Mind’s Eye, which activates only under certain conditions and causes extreme fatigue.
- Morgoth spent millennia seeking God and calls Jin chosen by God; whether Jin is truly chosen and what that means remain unresolved.
- The Skeleton King’s head appeared and spoke to Jin; what will happen to him remains unresolved.
- Magic Johnson’s Anti Magic backlash left him coughing blood and on his knees after his Hell Fire briefly opened a path for Jin.

## Translation Decisions

- Use “Dragon-tooth soldiers,” “Guardians,” “Warp,” and “Magic Formation.”
- Render 일기당천 as “One Against a Thousand.”
- Render 대성 as “Great Completion,” 무아지경 as “Trance,” and 무아 as “No-self.”
- Render 심안 as “Mind’s Eye,” 개천 as “Open Heaven,” and 드래곤 하트 as “Dragon Heart.”
- Keep magical power distinct from mana; Morgoth’s Anti Magic consumes human mana.
- Retain “Sky” for 스카이.

## Durable state

{
  "active_continuity": [
    "Humanity won the battle against Morgoth; its surviving forces are wounded but rallying.",
    "Jin’s physical injuries were healed by leveling up, but severe mental exhaustion remains; his Fire Dragon Armor was destroyed.",
    "Jin created Open Heaven, the third form of the Fire Dragon Divine Spear; Fire Gate Divine Technique and Qi Sense reached the ninth star.",
    "Jin gained insight into Mind’s Eye, which activates only under certain conditions and causes extreme fatigue.",
    "Morgoth is gravely wounded and nearing death, with his Dragon Heart exposed.",
    "Morgoth spent millennia seeking God and now calls Jin chosen by God.",
    "The Skeleton King’s head appeared and spoke to Jin."
  ],
  "continuity_sources": [
    1169
  ],
  "open_questions": [
    "Is Jin truly chosen by God, and what does that mean?",
    "What will happen to Morgoth and the Skeleton King?"
  ],
  "safe_through": 1169,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1165

# Chapter 1165

*Rrrrrumble!*

If light could turn to liquid and overflow, would it look like this?

Watching the waves of aura wash across the horizon and surge toward him, the ground shuddering as if an earthquake had struck, Morgoth knew instinctively:

If he didn’t act now, he might never get another chance to unleash everything he had.

“Answer my call.”

A low voice, its reverberation spreading deep and far.

Language had power.

And the Dragon’s words, imbued with immense magical power, had reached a realm no other race had ever trespassed.

*Craaaack!*

The empty air split open.

At the same time, countless eyes gleamed ominously from within the dark rift in space.

“Gwoooar!”

Large and small shadows plummeted to the ground with bloodthirsty roars.

With a single Warp spell, Morgoth had gathered the remaining forces occupying cities across the region. His voice turned cold as he gave the order.

“Kill them all.”

That one command was the signal.

Monsters charged at humans, humans charged at monsters, and soon light and darkness blurred together.

*Clang-clang-clang!*

*Thwack! Splatter!*

The shriek of keen steel and the sickening sound of flesh being torn apart swallowed the shouts. The Black Dragon’s eyes watched it all without a flicker as he gazed upon the blood mist hanging thick over the battlefield.

His shock had lasted only an instant.

Morgoth had already regained his composure. His mind was colder than ever.

Even if his elite monster legion, the force that had guarded his stronghold, had suffered heavy losses, he still had the reinforcements he’d just summoned. That alone was enough.

No—even if every one of those monsters were wiped out, it wouldn’t matter.

The fate of the world would be decided in this great battle, and the victor would be determined not by mere numbers, but by whether one human lived or died.

*Jin Taekyung.*

There he was.

A blue-black flame advancing through the thousand Dragon-tooth soldiers surrounding him on every side like a dense forest.

At the same time, the short vow that small, insignificant human had spoken earlier echoed in Morgoth’s ears—and chilled a corner of his heart.

*Me? Morgoth? Becoming just like them?*

The Black Dragon bared his gleaming teeth and let out a low growl.

Wrong. He was nothing like anyone else.

With the Demon King Asmodeus gone, Morgoth alone was the true ruler destined to reign over every world—and that was exactly what he would become.

“Fire Lance.”

*Fwoosh—KABOOM!*

A dozen or so spears of flame appeared out of nowhere in the air, poised to fall on Jin Taekyung.

“Ice Blaster!”

A desperate shout rang out from somewhere. A massive icicle shot through space and blocked the flames.

*KABOOM!*

Space shook.

The deflected flames slammed into the ground, harmless to their intended target. A dense cloud of steam rose, spreading across a radius of roughly a hundred meters and blocking the view in every direction.

But the Black Dragon’s gleaming eyes saw clearly through it all.

A group of people, their bodies covered in blood and dust, yet their eyes shining fiercely.

“Clear a…!”

The towering Grand Mage caught his breath, then shouted like a roar.

“Clear a path!”

*Whoosh! Whoooooosh!*

With a sky-piercing battle cry, thousands of the suicide squad—the first to arrive at this dreadful battlefield—charged toward the Dragon-tooth soldiers.

No.

They were charging toward their Alliance Leader, their one and only hope.

* * *

It was a battle no one could control.

*BOOM!*

*Clang! Krrrunch!*

Flashes and explosions burst and mingled without pause.

Blood sprayed like fountains. Severed arms and legs rolled limply across the ground.

And through the chaos, a long-awaited voice reached my ears.

“Wind Cutter!”

Magic Johnson. It was him.

At the same time, the blades of wind that rushed in passed close by the two Dragon-tooth soldiers charging at my flank.

*Shwaa!*

Two heads floated into the air.

If he’d aimed anywhere but their necks, even the Grand Mage’s Magic wouldn’t have been enough to kill them in one blow. But Magic Johnson had fought them before, in the Middle East. He knew their weakness exactly.

And he knew this wasn’t the time for a long, friendly greeting.

“Fuck.”

I tossed a dagger I’d just summoned from my Inventory to the man who’d greeted me with a single syllable.

More precisely, I threw it at the Dragon-tooth soldier lunging over his shoulder.

*Thwack!*

A dagger thrown with all a normal Murim martial artist’s strength should properly be called a hidden weapon. But my Strength had long since surpassed that of most large monsters.

The dagger shot forward like a flash and shattered not only the helmet made of some unknown metal, but the head beneath it, too. Drenched in the enemy’s brain matter, Magic Johnson muttered another curse.

“This is a special kind of hell.”

“Sorry, but it’s too late to go back.”

“Everyone here knows that. We knew, and we came anyway.”

That was true.

They knew their lives would be in danger, and still they’d answered my call without hesitation.

There were only twenty S-rank Hunters left in the entire world—or rather, now only a dozen or so—and they’d chosen only the very best before racing here from all over the globe.

Across continents and oceans.

But the tide of this great war, with the fate of all humanity at stake, was still as dark and heavy as the storm clouds overhead.

“Damn it, what the hell are those things? There are this many of them?”

Anyone who’d ever faced a Dragon-tooth soldier would react the same way.

Their magical power surpassed that of even the strongest Death Knights, classified at the top of A-rank. Their bodies were horrifyingly tough, and they were stubbornly hard to kill.

Calling each one as formidable as a named monster would be no exaggeration.

But even Magic Johnson, who knew all this well, still didn’t know one thing.

The Dragon-tooth soldiers weren’t the only obstacle we’d have to overcome to reach Morgoth.

*Shiiiiing!*

Something shot toward us at the speed of light.

It came without giving me a moment to breathe. I blocked it with the side of my spear blade, held at an angle.

*Clang!*

Even with no small amount of internal energy poured into it, the shaft of my spear trembled.

Magic Johnson let out a low groan at the familiar face that appeared beyond it.

“Pai Chen?”

His mouth fell open. His eyes wavered.

The moment he recognized his old comrade, someone he’d known for decades, ever since the Great Cataclysm began, Magic Johnson was shaken more than ever. And when their number finally reached seven, his whole body trembled.

“What is this?”

“Guardians.”

“What?”

“That’s what Morgoth calls them. His Guardians. They’re supposed to protect him.”

“……!”

Magic Johnson clenched his teeth as he understood what I meant.

Even I, a complete outsider to Magic, could clearly sense the magical power controlling them. There was no need to ask what the Grand Mage could feel.

“……Guardians.”

Bitterness, anger, grief.

The voice, tangled with too many emotions, mingled with the wind and gradually quieted.

Leaving only one behind.

Anger.

And Magic Johnson wasn’t the only one feeling it.

“Near the end of the Great Cataclysm, we talked about it when we were all together.”

*Boom!*

A fist shot forward like a cannonball, followed by a roar.

Chuck Hagel crushed the Dragon-tooth soldiers blocking his path one by one as he went on.

“If we survived this goddamn war, we’d live happier than anyone else in the world until the day we died.”

The fists he kept throwing carried more than just the mysterious power known as aura.

Memories from the past.

The memories of those days, so painful they could have killed him, yet filled with hope that things would soon get better, poured forth with his aura.

“Then why?!”

*Krrrunch!*

They burst outward in every direction. They scattered.

Shattered weapons. The armor and bodies of the Dragon-tooth soldiers.

And the tears of an old man who had lost his longtime friends.

“Why are they like this now?!”

The roar, filled with grief and anger, contained everything.

Why had it come to this?

Why hadn’t they been allowed to keep even that simple promise to live happily for a long time? Why did they have to suffer this humiliation even after death?

But no voice answered his questions.

The only answer was the Black Dragon’s Magic once again filling the sky, and the footsteps of his old comrades as they advanced.

*Fwoosh, crackle!*

*Shiiiiing!*

Giga Lightning.

Dozens of bolts plunged down like divine punishment, while the seven Guardians and countless Dragon-tooth soldiers charged forward, their pitch-black magical power streaming behind them like cloaks.

An overpowering force that seemed impossible to stop.

But that wasn’t what happened.

Because I wasn’t alone anymore.

“Stone Wall!”

A single spell rang through the roar of battle.

And dozens of voices filled it.

At the front stood Magic Johnson. Behind him were the world’s greatest mages, following the only Grand Mage humanity had.

*KABOOM!*

The sky darkened, then flashed.

A ceiling of rock suddenly appeared over our allies’ heads. When it met the lightning, a tremendous explosion shook the battlefield.

No—cancellation.

Several mages, unable to withstand the backlash, coughed up blood and fell to their knees. The enraged Black Dragon’s roar thundered across the battlefield.

“How dare you!”

*Rrrrrumble!*

As immense magical power shook space again, I shot straight forward, leaving the falling rocks behind me.

Just as I always had.

But there was one difference.

This time, people were following me.

*Whoooooosh!*

Another group of familiar faces finally broke through the chaotic battlefield.

The brown-haired foreigner at the front gave me a slight nod.

“Too late?”

“Not at all.”

“Good. Though even if I were, I wasn’t planning to apologize.”

That irritating way of speaking, still exactly as I remembered it.

Prince Felix had joined us with four S-rank Hunters. He added, “Go. Now. We’ll handle things here.”

I didn’t answer.

I just suppressed the hot feeling rising deep in my chest and pushed forward with all my might.

Leaving the seven S-rank Hunters behind as they clashed with their old comrades.

*Slice!*

I cut them down, one after another.

*Krrrunch!*

Kept going, without stopping.

And then—

*Crack!*

Toward the monster who was the beginning and end of it all.

*BOOM!*

I shot forward like a streak of flame.

“Morgoth!”

In the Black Dragon’s vast, gleaming eyes, a human leaping upward, stomping on thin air, was reflected.
## Chapter artifact 1166

# Chapter 1166

*Fwoooosh.*

For an instant, time slowed.

The sounds around him faded into the distance, and his heartbeat thundered in his ears.

At the same time, instinct and reason whispered in unison.

*Now.*

His senses sharpened until every hair on his body stood on end. Jin Taekyung shot upward on the explosive force of Flamefire Path and brought his spear down with all his strength.

Toward the Black Dragon’s eye—larger than Jin’s entire body, and darker than anything else in existence.

*Fwoosh—KABOOM!*

A line of fire split the air.

No—the countless threads hidden within that space.

*Shhhhk.*

A chillingly low, faint whistle.

That was all.

Nothing else could be seen or heard.

Even if someone else had been standing right there, watching it all unfold, they would never have understood what had happened.

But at last, the two beings facing each other knew.

That single strike had instantly shattered the highest-grade defensive magic, layered dozens of times over.

*I cut it.*

A shiver ran up Jin Taekyung’s spine.

It worked.

The flow of qi, which had become clearer to him as his insight deepened and his martial prowess grew, was there in the monster before him, too.

But the spearhead that had torn through the defensive magic never reached its target.

*Rrrumble—!*

An immense force suddenly dropped from above.

And the force humanity called gravity was faster and heavier than Jin Taekyung had expected.

*Whoooosh—BAM!*

A cloud of dust rose in the wake of his body as it slammed down at tremendous speed.

Just as Jin Taekyung had cut through the defensive magic with a single attack, Morgoth had sent him crashing to the ground with overwhelming gravity. The Black Dragon muttered in a low voice.

“Did you think I wouldn’t see even this coming?”

The words slipping between the Black Dragon’s teeth were more than mere sound.

“Wind Cutter.”

The magic within the Dragon’s words stirred. Countless blades of wind formed, then tore through the cloud of dust.

*BOOM!*

The thick dust cloud burst apart. Jin Taekyung raced over the ground, sliced through like tofu, dodging the onslaught as Morgoth unleashed one spell after another.

His voice continued, almost as if he were talking to himself.

“Thank you. Thanks to you, I’ve finally realized something important.”

Until now, fear had seemed to the great being Morgoth nothing more than a weakness.

So he had tried to forget it.

He simply hadn’t been able to.

But today, by watching a certain human, he had glimpsed a great truth he had been ignoring.

“If you fully acknowledge and accept the fear lurking in your heart, you can no longer call it fear.”

Yes.

Morgoth believed that was why Jin Taekyung—and humans—could be strong.

Their lives were absurdly short, their bodies fragile.

Humans were undeniably weak. They had neither the long lives of elves, nor the dwarves’ strength, nor monsters’ ability to reproduce quickly.

But because they knew their own weakness and fear, they spent their lives struggling to grow stronger, each in their own way.

Like the person fighting his way through a curtain of magic that now surrounded him on all sides, closing in without a gap, relying on nothing but a single spear.

“And so, I too will grow stronger.”

Morgoth let go of the barest courtesy he had used not for his opponent, but to maintain his own dignity. He let go of the last sliver of arrogance that remained. Then he added quietly:

“Because I’m… afraid of you, you bastard.”

At that moment—

*CRACK—KABOOM!*

The ground caved in within a hundred meters of Jin Taekyung. Countless thorny vines burst through the cracks and surged toward their target.

*Shwaaa!*

A sharp whistle rang out from every direction.

This was no ordinary binding spell, nor were these common thorny vines.

Their trunks were as thick as mature trees, covered without a gap by enormous thorns.

Instead of sunlight, they had drunk their fill of the Black Dragon’s magical power. Each one was strong enough to crush a human body in an instant, and Jin Taekyung could feel the power within them.

He also knew there was only one way to escape this tenacious magical prison closing in from every direction.

*Grit.*

He steadied his breathing. Clenched his teeth.

He planted a step with the weight of a thousand pounds, using that foot as his pivot, he gathered the internal energy he had left—not even half of what he’d started with—and poured it into the tip of White Flame.

Then—

He swung.

A storm that swept everything away, and hellfire capable of burning anything.

*Whoooooosh!*

Fire Dragon’s Single Tail.

In the life-or-death crisis, the first form of the Blazing Flame Divine Spear, at last approaching the pinnacle of its realm, flowed along the spearhead.

The fiery storm crossed a single line, then spread into a vast circle, hungrily devouring everything in its path.

The ice and lightning that had ceaselessly blanketed the sky and rained down.

The thorny vines that surged from every direction, seeming to swim through the ground.

*KABOOOOOM!*

Ash-white powder and still-glowing embers drifted like snow.

They swept past Jin Taekyung, standing alone and upright in the heat haze rising from the ground.

At the same time, Morgoth instinctively knew.

Now that Jin Taekyung had poured out all the strength he had left at once, this was the moment he had been waiting for.

It was why he had waged a relentless war of attrition, using tens of thousands of monsters—and even the thousand Dragon-tooth soldiers he had spent so long creating—as bait.

“Dark Vine.”

*CRRACK!*

Black thorny vines erupted again and surged toward Jin Taekyung.

And that wasn’t all.

*Rrrrumble!*

“Gravity.”

A force far beyond the bounds of ordinary gravity magic shook the sky. Magic spells of devastating power filled the gaps, each one as powerful as the dazzling flashes they produced.

All in one direction, for one purpose.

And this time, nothing unexpected happened.

*BOOM! Shrrrk!*

First, his knees buckled under the weight of dozens of tons of gravity. Thick thorny vines, slithering like living snakes, bound his whole body.

At the same time, dozens of spells converged in the air, shining on one human like a small sun.

*Jin Taekyung.*

As Morgoth watched him, bound like a criminal and waiting for death to come, a thought suddenly crossed his mind.

If he hadn’t been a Dragon.

Or if Jin Taekyung had possessed a Dragonheart, brimming with power almost without limit like his own, perhaps Jin Taekyung would be the one standing there now instead of him.

But…

*At least today, I was stronger.*

It was the difference in what they had been born with.

The size of the vessel that could contain their power, the total amount of strength they possessed—it was different.

Morgoth and Jin Taekyung.

Jin Taekyung and Morgoth.

The two beings were different in every way, and each had fought the other with everything they had. But the vessel of power within Morgoth was deeper and larger than Jin Taekyung’s.

That was all.

That was the sole reason that decided the battle today—and, beyond that, the fate of this world.

*Meeting you was the greatest amusement I have ever experienced.*

With the highest praise he could offer, the Black Dragon opened his enormous jaws.

*Vwooom.*

The Dragon’s heart, deep within his body, shuddered.

No matter how much he emptied and poured out, pure magical power continued to fill him without end. Its chillingly low rumble swirled between the Dragon’s teeth, dark as a cave.

Dragon Breath.

A supreme power granted only to dragonkin.

The range and destructive power were far below their usual level, partly because he feared harming the Dragon-tooth soldiers, and partly because he had so little time left to use it.

But it was more than enough.

His only purpose was to erase a single human from this world without leaving a trace.

*Jin Taekyung. The weakest of humans, and yet a hero stronger than anyone.*

*Gooooong.*

His chest suddenly swelled.

At the same time, the immense magical power flowing from the Dragonheart—the purest, deepest darkness—finally became a single flash and shot forward.

Carrying heartfelt respect, and a murderous intent heavier still.

*This is the end.*

At that moment—

*KABOOOOOM!*

A beam of darkness, black enough to swallow the sun, tore through space like a bolt of lightning.

* * *

The world stopped.

Or at least, that was how it seemed to Jin Taekyung.

But his dimming eyes weren’t fixed on the countless spells coloring the air, or the Dragon’s breath, which held more power than all of them combined.

*So this is what it was.*

Jin Taekyung gazed clearly—not with his eyes, but with his mind.

At himself, thoroughly bound and forced to his knees.

At the enormous Black Dragon looking down on him with haughty disdain.

And at this world, and the secrets it had hidden.

It was a sensation that had come to him after another life-or-death struggle, one he had already experienced once in the not-so-distant past.

“People often fail to believe the truth, even when it’s right in front of them, and pass it by. It’s truly a pity.”

The voice echoed from his memory, belonging to the old man who had served as his Helper in the Tutorial, the Martial God without equal in all history—or the savior of humanity.

“You saw what cannot be seen, and avoided what cannot be avoided. So why can’t you believe what you did yourself?”

In another space, one that existed in neither dream nor reality, the Absolute One had asked him that question.

Back then, Jin Taekyung hadn’t answered.

No—he couldn’t.

He had been captured by a sensation that ruled his body and flesh.

Just like now.

*Ding. Ding. Ding.*

He heard it, but didn’t hear it.

> **System**
>
> Martial arts are built through endless training and pain, and perfected in battles fought on the brink between life and death.
>
> Congratulations. The **Fire Dragon Divine Spear** has reached **Great Completion**.
>
> You have gained a tremendous amount of **EXP** and **Fame** as a reward.
>
> **Level Up!**
>
> Status effect **Trance** applied.

He saw it, but didn’t see it.

No-self.

True to the meaning contained in those two characters, Jin Taekyung forgot everything.

His memories up to that point. The many emotions lurking like thorns in his mind and heart.

Even Jin Taekyung himself.

And yet his pupils, now tinged with a deep blue-black light, were reading everything in the world.

*Mind’s Eye.*

In a sensation he hadn’t experienced once since that day, Jin Taekyung lifted his spear as if entranced.
## Chapter artifact 1167

# Chapter 1167

It wasn’t a simple thrust.

More precisely, it was something that had slipped beyond the concepts of attack and defense.

*Why should it have to be?*

As the question surfaced amid his hazy consciousness, Jin Taekyung had already tilted the White Flame’s spearhead, wreathed in blue-black fire, upward.

Toward the Dragon’s Breath pouring down to blanket the sky.

Like a fool trying to stop a waterfall with an umbrella that had no fabric.

*Shh.*

A movement so simple it could hardly be called a form.

But the result of that tiny change, in the very next instant, was something even an Ancient Dragon with unprecedented power and knowledge could never have predicted.

*Rrrrrumble!*

Morgoth’s pupils widened in an instant.

As time’s rapid flow finally returned, the Black Dragon’s eyes flew open before he even realized it.

*What is this…?!*

It was splitting apart.

A massive pillar of magical power, several meters in diameter, was splitting into dozens of streams the moment it touched the spearhead.

Even now.

*How is that possible?*

He had lived for thousands of years.

At times as a human, an elf, or a dwarf; at others wearing the hide of a monster. He had enjoyed the amusements only the strong could afford, and gained countless experiences and knowledge.

That was precisely why Morgoth found this all the harder to understand.

How could such a phenomenon be possible?

How could a human smaller than his claw read the flow of energy in Dragon Breath?

But Morgoth’s questions were nothing more than empty echoes.

Even Jin Taekyung, lost in Trance, couldn’t properly answer them.

No—his consciousness had wandered so far away that he didn’t even know what he was doing.

He simply did what he saw.

*Rrrrrumble!*

Dark. Pitch-black in every direction.

A muffled roar filled his ears. The magical power deflected up, down, left, and right along the spearhead had, unintentionally, formed a rounded barrier around Jin Taekyung alone.

At least, that was how it looked to anyone else.

*Fwoooosh.*

Why?

It was bright. Radiant.

The whole world was already swallowed in darkness, yet the view reaching Jin Taekyung’s eyes, now glowing blue-black, glittered with countless lights.

*Beautiful.*

Jin Taekyung gazed at the strands of color filling his vision.

Some were red, others blue.

Some shone a dazzling white, while others held a pure darkness of unfathomable depth.

The dozens of kinds of Magic that arrived a step behind the Breath were just like that.

Water, fire, ice, gusts of wind, lightning.

Each held enough power to take a thousand lives. They had been unleashed for the sole purpose of erasing one person from this world, and Jin Taekyung was grateful for it.

If those spells had been aimed at his allies instead of him, they would have suffered a horrible death.

*Inventory open. Summon.*

It all happened in an instant.

The old iron spear suddenly appeared in midair. At the same time, Jin Taekyung instinctively drew up the energy in his Middle Dantian.

*Fwoosh!*

It was swift and powerful.

More so than at any point since he had unlocked the power of his Middle Dantian.

The iron spear, carrying a blaze and streaking through space like a bolt of lightning, pierced the core of every spell in its path before its power finally ran out.

*KABOOOOOM!*

The sky and the earth shook.

The spells, which had exploded before reaching their target, painted the sky in a dazzling display. Witnessing the unbelievable sight, the Black Dragon opened his enormous jaws wide.

He drew even more power from the vast magical force dormant within his Dragonheart.

*Rrrrrumble!*

An immense pressure came through the spearhead.

That was when Jin Taekyung lifted the knee he had driven deep into the ground, beneath the Dragon’s Breath raining down harder and harder without pause.

*I have to get up.*

One thought filled his mind.

He had to go. He had no choice but to go.

And so, just this once, he could forget everything.

The pain of his bones grinding out of place.

The horrifying mass of magical power, ready to swallow his body along with the spearhead at any moment.

The thorny vines constricting his entire body, and the immense gravity pressing down on both shoulders.

*Crack!*

He took a step forward, unsteady as a child’s first step.

But like the deep footprint he left behind, the strength and will within Jin Taekyung were heavier and stronger than ever.

No mere Magic could stop him.

*Crack!*

The thorny vines wrapped around his body like chains tore apart, and the gravity that had weighed as much as a massive boulder began to weaken.

*Crack.*

One step.

*Crack.*

Another step.

Slowly, but without hesitation, Jin Taekyung moved forward.

Toward the enormous shadow blurred in his dreamlike vision, using the spearhead that shone alone at the center of the pitch-black Breath as a torch.

And behind him stood a comrade willing to brave any danger for his sake.

“May the flames of hell consume our enemies—”

Just then, the Grand Mage’s cry, like a roar, rang out amid the din.

*Fwoooosh!*

Against the suddenly reddened sky, a dozen or so fireballs emerged from the storm clouds and took aim at the Black Dragon’s head.

“Hell Fire!”

*Rrrrrumble!*

The spell was complete. A fierce heat rushed in, scorching the sky.

But Morgoth wasn’t even slightly startled by this sudden attack.

No—he wore an enraged sneer at the thought that what was coming for him was Magic, not a blade.

He was no one but a Dragon.

The master species of Magic, born of wonder—and a Dragon Lord who had once led all his kind from the highest place of all.

*Disappear.*

He didn’t even need to say it aloud.

Morgoth had a powerful will and even greater magical power. His Magic existed in a distant realm no other race, humans included, could ever reach.

*PAAAM!*

Anti Magic.

The Dragon’s magical power devoured the humans’ mana.

Ash and embers swirled through the air. Far away, Magic Johnson—who had risked intervening in the middle of his fight with the Guardians—coughed up blood and dropped to his knees.

Mana Backlash.

The most devastating injury a mage could suffer.

And yet, the Grand Mage’s mouth, drenched in blood, had curved into a gentle smile.

Because the brief opening he had created gave someone else a chance, even if only for a moment, to escape the gravity.

“Go, Jin.”

At that moment, a faint voice slipped between his barely moving lips.

*Fwoosh.*

Flames surged from the tip of Jin Taekyung’s foot as it touched down.

Heat strong enough to overcome the momentarily weakened gravity and carry him beyond the range of the Magic surrounding a radius of dozens of meters.

*KABOOM!*

Compressed energy and an explosion.

And then—

A charge.

*Whooooosh!*

Cutting through the Dragon Breath, which stretched ahead like a single line, Jin Taekyung raced forward.

The closer he got—and the more danger Morgoth felt—the rougher and more powerful the Dragon’s Breath pouring toward the ground became. But it didn’t matter.

If anything, the rougher it grew, the more clearly he could follow the flow of its power.

Leaving behind the countless roars and screams blanketing the battlefield.

Without a single moment’s hesitation, he kept going. Forward, and farther forward.

And at last, as the Dragon’s enormous shadow loomed over him like a mountain, Jin Taekyung instinctively realized what he had to do.

Fire Dragon Divine Spear, Second Form.

Heavenly Strike.

*Rrrrrumble!*

It was a wondrous sight no one there had ever seen.

The spearhead, wreathed in blue-black flames, rose as it cleaved through the colossal pillar of darkness.

Like a dragon soaring into the sky.

Becoming the fire dragon itself.

* * *

Everything began and ended in the blink of an eye.

*Fwoooosh!*

The darkness—the Dragon’s Breath, finally spent—dispersed.

By the hand of no one but a human.

Watching that unbelievable sight, Morgoth suddenly wondered where it had all gone wrong.

Had the arrogance and complacency deep within his heart really grown into such a massive snowball that it could come crashing down on him like this?

Or—

Had the strength and will of a mortal with a lifespan of barely a hundred years truly surpassed his own?

*No. That can’t be.*

His name was Morgoth.

Master of the lofty Silver Mountain, and Archduke of the Demon Realm.

Alone in the slowed world, the ancient Black Dragon muttered to himself and spread his enormous wings.

Then he dove toward the small figure shooting skyward once more, cutting through the heavens.

*PAAAM!*

Compressed air exploded.

From sky to ground.

From ground to sky.

Two shadows shot toward each other.

The Dragon’s claw, wrapped in pitch-black magical power, and the spearhead filled with blue-black fire tore through space as they advanced.

As if they had lived for this moment alone.

“I—I…!”

Beyond the howling wind, Morgoth let out a fierce cry and put everything he had into a slash of his massive claw.

At the same time, he suddenly realized:

The foreleg he had just swung had already been cut by someone else.

And that wound still hadn’t healed—not even now, after he had returned to his true form.

*The Skeleton King.*

A shallow wound, but one that had never healed.

To some, he had been no more than a trophy. To someone else, he had been a friend. Perhaps it was Morgoth’s instinct that made him remember, at that very moment, the final trace of the Skeleton King’s stubborn resolve.

Perhaps.

Just perhaps.

The long game he had played for thousands of years might finally be coming to an end.

And ominous instincts were never wrong.

*Shhk.*

A low, keen sound of something being sliced.

The spearhead, imbued with its wielder’s will, bit into the last trace his friend had left behind.
## Chapter artifact 1168

# Chapter 1168

It connected.

And it cut.

That was all.

There was no need to explain anything more about the whole process, which had begun and ended in an instant.

Not even a trace of doubt had entered Jin Taekyung’s mind from the start, and the hellfire spearhead that surged forward without hesitation could melt and cleave through anything.

Even dragon bone and hide.

*Shhk.*

A hair’s breadth.

That was all the difference.

But the result of that difference—shorter than a dagger—was as vast and deep as the distance between heaven and earth.

The enormous claw had barely grazed his Fire Dragon Armor. The spearhead that shot upward in a perfect arc, however, pierced straight into the tiny wound etched into the Dragon’s foreleg.

*Fwoooosh!*

Blood burst forth like a waterfall.

The Dragon’s blood, strangely tinged with silver, flooded his vision in an instant. Its vicious acidity even began to melt Jin Taekyung’s exposed skin and parts of his Fire Dragon Armor.

But he didn’t care.

No—there was no reason to.

Compared to everything that had happened so far, and everything still to come, this much pain was nothing.

*Grit.*

Through the faint pain, Jin Taekyung clenched his teeth.

At the same time, he planted a foot on the Dragon’s foreleg beneath him as if it were a stepping-stone, then thrust out a tightly clenched fist with all his strength.

*Flame-Extinguishing Divine Fist.*

*BAM!*

Compressed air exploded from the fist he drove forward like lightning.

The fierce heat packed into his knuckles swallowed the spraying blood, opening a new path beyond it.

*Whoooosh!*

It was a charge.

A charge in which one man staked everything—and a storm of hellfire that would melt and devour anything in its way.

*CRRRUNCH!*

A trail of flame carved through the air like an icebreaker smashing through a glacier.

The spearhead, driven deep into the enemy’s flesh and bone, erupted with lava as it climbed higher and higher.

The flames that rose in the wake of Jin Taekyung’s arrowing form burned so brilliantly and clearly that they seized the attention of everyone still locked in battle.

Human and monster alike.

No one was an exception.

Without realizing it, they lowered the blades in their hands or drew in their sharp claws and fangs.

Every living thing that had survived this horrific battlefield sensed it instinctively.

That rising flame, devouring the space around it, would decide all their fates.

If there were any exceptions, they were the only two beings who had faced each other from the beginning.

Leaving behind the vast battlefield and the countless eyes watching them, the Ancient Dragon and the human raced toward their final moment, gazing at each other like a scene from a myth.

*Jin Taekyung.*

*Morgoth.*

An inaudible whisper passed between them—not through their mouths, but through their eyes, across the open air.

Even though they couldn’t hear it, they could listen.

And even without speaking, they could feel.

And he could feel the emotions in the enemy’s eyes as they drew closer like the wind, as though defying the slowing of time.

And in this moment, Jin Taekyung saw a Dragon’s eyes filled with pain and fear.

*Yeah. This must hurt.*

With a thought that would never reach Morgoth, Jin Taekyung poured more strength into his charge.

He ran up the long, massive foreleg like a flight of stairs, heading for the head that loomed above him like a skyscraper.

*Like the people you killed with your own hands, or those who lost someone precious because of you.*

Jin Taekyung suddenly thought that he wished Morgoth’s pained roar—his every emotion and every ounce of suffering—could reach all those people.

Tens of millions had died.

Hundreds of millions had lost their families, friends, and homes.

That was why Jin Taekyung couldn’t stop.

It was the fuel for his will to keep moving forward.

*CRRRUNCH!*

Perhaps that was why.

His will had risen beyond the limits of his body.

The flame on his spearhead, which had been weakening along with the rapidly dwindling emptiness in his lower dantian, roared back to life. Part of his skin and muscle melted in the Dragon’s acidic blood, yet he couldn’t even feel the pain.

*Whooooom!*

The sky suddenly darkened, and gusts of wind slammed in from both sides.

Jin Taekyung didn’t waver in the slightest.

He simply swung the spearhead that had been cutting through the enemy’s body upward, straight at the two wings bearing down on him with enough force to crush a mountain.

*Shhhh.*

The rolling flames rose at an angle.

A single line, chillingly swift and savage.

In the arc of blue-black fire that suddenly appeared in the air were the Dragon’s two wings, which had ruled the vast sky and blanketed the earth for thousands of years.

*Shhk!*

—Kraaaaaa!

Pinning down the body thrashing with a muffled scream, Jin Taekyung dug his toes in.

*Fwoosh—BAM!*

Flamefire Path.

His form shot upward, propelled by a fierce explosion worthy of its name, and reflected in Morgoth’s pitch-black eyes.

No—that was wrong.

He soared into the sky like a fire dragon that had finally reached the time of its ascension. His form wasn’t merely reflected in those eyes; it overflowed from them.

—…!

Was this what it felt like when time stopped?

In the strange sensation, with every sound and movement around him gone, Morgoth watched Jin Taekyung.

He sensed the gaze sunk into an unfathomable depth, the blue-black light in his eyes unlike anything he had ever seen, and the countless fragments of emotion seeping through it.

And then came the realization, a step too late.

*Too late.*

Whether reason or instinct had reached that conclusion, Morgoth couldn’t say. But one thing was certain.

In this world where everything had stopped, that spearhead falling slowly, all alone, could neither be stopped nor avoided with any ability he possessed.

That left him only one path.

—Kraaaaaa!

His enormous jaws gaped open.

With the Ancient Dragon’s last struggle, heedless of death, the immense magical power and countless teeth lurking within its maw flashed toward a single human.

And at that very moment—

*Rrrrk.*

Jin Taekyung gripped the spear shaft with all the strength he had left.

The muscles throughout his body swelled. Fire raced through hundreds of acupoints and spread to every limb.

*Thump. Thump. Thump.*

His heart hammered furiously.

His lower dantian was empty enough to make the single recovery from leveling up seem meaningless, and his mind, already far beyond its limits, had been crying out from exhaustion for some time.

But he didn’t stop.

More precisely, there was no reason to stop.

*I can see it.*

In this new world painted in lines of every color, one trajectory shone brighter than all the rest.

Following the path he read through the Mind’s Eye, Jin Taekyung poured all his strength and will into the spearhead.

*Fwoosh—*

As time returned, the flame on the spearhead wavered.

But it wasn’t a sign of danger. It was a change—and an evolution—that took place in an instant.

*Shhhh.*

The wavering flame gathered into one.

It came together and connected, no longer a flame but a single line, as though it had become the spearhead itself. Then, at last, it settled.

It had advanced one step beyond the innate savagery of fire, becoming hellfire refined to the utmost degree.

And it was a peak Jin Taekyung had built on his own insight—a third path no one had ever taught him.

Fire Dragon Divine Spear.

Third Form.

*Fwoooosh.*

Space twisted.

The spearhead that had risen as if to cleave the sky—and the fire refined within it—gave off a terrifying heat.

Like another sun prepared to bring forth a new sky.

*Open Heaven.*

Amid the fierce shiver that seized his body and mind, Jin Taekyung brought down the hellfire spearhead, roaring silently.

*KABOOOOOM!*

The blue-black sun opened a world drowned in darkness.

* * *

They heard it, but didn’t hear it.

They saw it, but didn’t see it.

Among mountains of corpses and rivers of blood, countless living creatures watched an unbelievable sight unfold in the distance. In that moment, they all shared the same emotion.

A shudder.

They shuddered.

A blinding flash filled their vision, too bright to look at directly. A muffled roar blocked their ears. And yet everyone who survived could feel it clearly.

This long and terrible battle had finally come to an end.

The scene emerging beyond the slowly fading light proved their guess was right.

*Fwoooosh.*

A fierce wind swept through.

It wrapped around the enormous body tumbling down, silver blood spraying from it like a waterfall.

Yes. It was a fall.

And at the same time, the downfall of an Ancient Dragon that had lived for thousands of years.

What falls has wings. But his wings would never take flight again.

*KABOOOOOM!*

The earth shook. Dust billowed up and swirled across the area like a sandstorm in the desert.

And yet tens of thousands of eyes that had witnessed it all still faced the sky.

More precisely, they watched the lone being moving within the terrible stillness weighing down on the world.

*Step.*

He walked slowly through the air, as if stepping on an invisible staircase.

Even from a distance, he looked utterly exhausted. But no one there dared entertain the thought, or feel anything of the sort.

With the sky—its clouds torn away without a trace—at his back, he descended toward the ground against the falling sun. His very presence inspired an overwhelming awe.

As if he were something beyond human.

Or like an old image of someone the world would remember forever.

“…Sky.”

At the moment a nameless someone’s breathless murmur slipped from their lips, the people watching Jin Taekyung with trembling eyes realized one important thing they had forgotten.

They had won.

No—they, all of humanity, had won.

And the one who had led them was a new savior of humanity.
## Chapter artifact 1169

# Chapter 1169

The Dragon’s roar, which had pierced the clouds and shaken the sky, was gone. So were the two wings that had cast an immense shadow over the earth.

But there wasn’t the slightest empty space in the endless sky.

No—instead, it was overflowing.

With the presence of a single being.

Another Dragon, the one who had brought the first crashing down.

“Jin!”

It happened in an instant.

The Grand Mage’s shout, amplified by magic, swept across the battlefield. A moment later, tens of thousands of voices joined as one.

“Jin! Jin! Jin!”

As if they’d made a promise, they cried out with all their might.

They staunched the bleeding from severed arms and hauled their blood-soaked bodies upright.

They stared at one man walking down through the distant sky.

They cried out the name of the savior who had dragged from the heavens the evil Dragon that had nearly plunged the world into ruin.

*Clang, clang, clang!*

Countless spears and swords swayed like a forest caught in the wind, then surged toward the enemy like a wave.

*Shhk! Krrrrrrunch!*

The two waves that had surged toward each other, roiling with thick killing intent, were gone.

There was only humanity advancing, and monsters being swept away.

And amid that enormous scream and roar that shook heaven and earth, the clear sound of a bell rang in one man’s ear.

*Ding. Ding. Ding.*

> **System**
>
> *The Fire Dragon sweeps the earth with its raised tail (火龍一尾), then shakes the open sky (天擊), and a new heaven shall open (開天).*
>
> You have forged your own path based on your deep insight into the Fire Dragon Divine Spear.
>
> A new form has been added to the Supreme Peak martial art Fire Dragon Divine Spear. Its power and underlying principles have grown stronger.
>
> Third Form, Open Heaven, has been registered. It will be recorded in the history of the Fire Gate Clan, and future generations will remember your name and your achievement.
>
> You have accomplished the remarkable feat Learn from the Old, Know the New!
>
> Your understanding of the Fire Gate Clan’s martial arts has deepened. When using related martial arts, you can direct qi more freely, and the amount of internal energy consumed is reduced.
>
> The realm of Flamefire Path has increased!
>
> The realm of Flame Divine Palm has increased!
>
> …
>
> …
>
> …
>
> Congratulations. The realms of Fire Gate Divine Technique and Qi Sense have reached the ninth star!
>
> This is both a stairway leading to a new realm and a massive wall blocking your path. May martial fortune be with you.
>
> You have gained insight into Mind’s Eye. This ability activates only when certain conditions are met and causes extreme fatigue.
>
> You have gained a tremendous amount of EXP and Fame.
>
> Level Up!
>
> Level Up!
>
> All injuries have been healed as a result of leveling up.
>
> Status effect Trance has been lifted.

At the moment the last holographic window appeared in his blurry vision—

*Squish.*

Jin Taekyung’s foot came down on the ground, soaked in someone’s blood, as he stumbled forward as if about to collapse.

*Sssssss.*

A thick cloud of steam rose behind his staggering form.

But he knew all too well that even this terrible acidity could no longer harm a single hair on his head.

So did the owner of the silver blood flowing like a small river.

“Morgoth.”

At Jin Taekyung’s quiet voice, the Ancient Dragon’s eyelids, shut without so much as a twitch, slowly lifted.

“You’re late. Why did you only come now?”

His breath came raggedly, and his upper body was half melted.

Between the cracks in his chest, a large black jewel was visible.

No—a Dragon Heart.

Despite Morgoth’s calm tone, his condition was ghastly. Jin Taekyung dropped down beside him.

“I was tired. Thanks to someone.”

It was no lie or exaggeration.

Even though he’d completely shattered the Dragon’s Breath, the aftershock had been enough to destroy his divine weapon, the Fire Dragon Armor. And the mental exhaustion that had built up over the course of the battle was beyond anything he could imagine.

He could have lost consciousness at any moment.

If leveling up hadn’t healed his body, Morgoth wouldn’t have been the only one lying there.

“Fortunately, I got lucky.”

“Luck, you say.”

Morgoth muttered as if to himself, then took in Jin Taekyung’s figure with his enormous eyes.

His clothes were in tatters, nearly leaving him half-naked, and his whole body was covered in blood and dust.

But that was only what he looked like on the outside. The skin visible between the rags was smooth as a newborn child’s.

Though Morgoth couldn’t sense even the slightest trace of healing magic.

“I don’t think it was mere luck.”

“I was born with the kind of luck that comes from heaven.”

“Are you sure?”

“What do you mean?”

“That expression doesn’t quite fit. Perhaps….”

With his gaze turned toward the sky steeped in sunset, Morgoth continued.

“Divine favor. That might be the most accurate way to put it.”

“……!”

“You can use subspace freely without ever learning a single spell, let alone becoming a Grand Mage. And that extraordinary healing power… Yes, it’s hard to explain without divine favor.”

For a moment, Jin Taekyung fell silent.

God.

Ever since that blisteringly hot summer several years ago, when he obtained the capsule and woke up in Murim, God had felt like the being closest to him—and yet the farthest away.

That single word, appearing so suddenly in an unexpected turn of events, disturbed Jin Taekyung’s mind like a rock thrown into a calm lake.

Before he could steady himself from the confusion that had seized him for just an instant, Morgoth continued.

“Do you believe in God?”

Morgoth asked the rigid Jin Taekyung without warning, then went on without waiting for an answer.

“I do. I always have.”

Of course he did.

Morgoth had always thought that he himself was practically a blessing from God.

A lifespan approaching immortality, and immense power granted at birth.

That was what Dragons were—and among them, Morgoth had been so great as to stand apart.

Perhaps that was why he had tried to draw closer to God, despite being the greatest scholar, warrior, and mage among every race on the continent.

“Every desire and pleasure I’ve pursued all this time was for that one purpose alone.”

At that moment, Morgoth was making a confession without concealment.

His entire life had been devoted to a single goal.

He had wanted to meet the absolute being who had created humans, elves, and dwarves—not to mention monsters.

“An absurd length of time has passed in vain. Before I knew it, I had become a being who was everywhere and nowhere. Much like the God I had sought for so long.”

He had been a creator and destroyer of worlds, and at the same time, a wanderer.

He had built an empire that ruled the whole continent, then broken it into pieces. He had lived as a member of every race in the world, learning their ways and customs.

But God never appeared.

Not even when God’s greatest creation reached for the forbidden, irredeemable realm in pursuit of a clue.

“That was how I left for the Demon Realm. No—I suppose it would be more accurate to say I met him. As it happened, he was on his way to my homeland, too.”

“If you mean him—”

“Asmodeus. The most cursed demon of all since the heavens opened and the earth stirred. The most terrible nightmare, and the ruler of the Demon Realm.”

“……!”

“We fought, and he won. A helplessness and sense of defeat I’d never known before crushed me.”

Even in the shame of defeat, something he had never felt before, Morgoth found the answer to one question.

“Before meeting Asmodeus, a thought occurred to me. If I couldn’t find God anywhere in the land where I’d lived for thousands of years, perhaps it was because God existed in another world, in a form I hadn’t expected.”

But Morgoth’s guess had been wrong.

Demon King Asmodeus was unquestionably a powerful being beyond Morgoth’s reach, but he could never be called a god.

“In the end, I had to set out on another long journey. And that meant burning my homeland and striking down my own kind under Asmodeus—not anyone else.”

As Jin Taekyung listened to the story drift by like the wind, the old Dragon didn’t miss the slight tremor in his eyes.

“You won’t understand. Perhaps no one would. But I had a goal I absolutely had to achieve. I believed I’d been born for it.”

And so Morgoth survived.

As Dragon Lord, he killed dozens of his own kind and took their hearts. With the power he gained, he became a Demon Duke second only to Asmodeus.

A long time passed again. Then he heard news that was hard to believe.

“A mere human defeated Asmodeus? At first, I didn’t even find it funny.”

But it was all true.

Some of the monsters who had returned to the Demon Realm through the Gates relayed everything they had seen and heard. The Demon Realm soon plunged into utter chaos.

Everyone was thrown into turmoil.

Everyone except Morgoth.

He thrilled at the news.

In another world, one he’d never known existed, someone had appeared who had defeated Asmodeus—the being closest to God of all he had ever seen.

The astonishing news was enough to revive Morgoth’s interest, which had slowly faded under the weight of time piled up like dust.

And at last, the ancient Dragon’s long-awaited wish was answered.

Right here, today.

“It was the first time. The first time in these eyes, which had watched the laws of nature remain unchanged for thousands of years, that I had seen a being defy them.”

At that moment—

*Pop.*

The Skeleton King’s head suddenly appeared in midair and came down into Jin Taekyung’s arms as if nestling against him.

“Jin Taekyung. Great human hero. No…”

Along with Morgoth’s voice and gaze, which shone more vividly than ever, despite his body drawing closer to death by the moment—

“Chosen by God.”

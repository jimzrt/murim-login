# Checkpoint Review — 1160–1164

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

# Chapters 1160–1164

## Plot

The Skeleton King’s self-destructive strike devastates the Dragon Lair, killing tens of thousands of monsters and wounding Morgoth, but leaves the Skeleton King alive and reduced to his head. Morgoth keeps him as a trophy. When Jin arrives, he calls the Skeleton King his friend and attacks Morgoth, who summons thousands of Dragon-tooth soldiers—including Pai Chen—and reveals that his Guardians include seven S-rank Hunters presumed dead in the Black Dragon’s invasion.

Jin survives Morgoth’s Ice Wall and Hell Fire and drives many monsters back with One Against a Thousand, but is left exhausted. The Skeleton King’s sacrifice weakens Morgoth’s isolated territory. Reinforcements arrive through countless Warp formations as Magic Johnson attacks the monsters. Morgoth admits he fears Jin and transforms into his Black Dragon form. Jin faces Morgoth’s forces and vows to defeat him.

## Continuity

- The Skeleton King survived his sacrifice but remains severely damaged; his current condition is unresolved. His explosion weakened Morgoth’s territory.
- Morgoth has transformed into his Black Dragon form. One thousand Dragon-tooth soldiers and seven empowered Guardians remain arrayed against the exhausted Jin.
- Morgoth’s Guardians include seven soul-stolen S-rank Hunters who were Jin’s comrades; Pai Chen, Joel Schumacher, and Pablo Albatroses are among them.
- Numerous reinforcements have arrived through Warp formations. Magic Johnson is attacking the monsters; who else has arrived and whether they can change the battle’s outcome remain unresolved.
- Morgoth admitted that he fears Jin. Their confrontation continues.
- Morgoth’s three-day deadline and demand for Cheon Taemin and Jin Taekyung as tribute remain in effect. Cheon Taemin remains unconscious in a hidden Pentagon chamber.
- Jin believes Cheon Taemin was the Martial God and The Helper, and suspects Asmodeus was not completely erased; neither suspicion is confirmed.

## Translation Decisions

- Use “Black Dragon,” “Dragon-tooth soldiers,” “Warp,” and “Magic Formation.”
- Capitalize “Guardian” for Morgoth’s collected beings and their assigned role.
- Render 일기당천 as “One Against a Thousand.”

## Durable state

{
  "active_continuity": [
    "The Skeleton King’s sacrifice unleashed a power explosion that weakened Morgoth’s territory; his current condition is unresolved.",
    "Morgoth’s territory is losing its isolation, and numerous Warp formations bring reinforcements across the horizon.",
    "Morgoth has transformed into his Black Dragon form; a thousand Dragon-tooth soldiers and seven empowered Guardians remain arrayed against the exhausted Jin.",
    "Morgoth admits that he fears Jin, and their confrontation continues."
  ],
  "continuity_sources": [
    1163,
    1164
  ],
  "open_questions": [
    "Who has arrived through the Warp formations, and can they change the battle’s outcome?",
    "What is the Skeleton King’s condition after his sacrifice?",
    "Can Morgoth’s seven Guardians be freed from his control?",
    "What will happen in the confrontation between Jin and Morgoth?"
  ],
  "safe_through": 1164,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1160

# Chapter 1160

Undead.

Beings who had met death but had not died; who could move, yet could not be called alive.

But even the undead were not immortal.

They simply met another kind of death: Erasure.

*Erasure, huh.*

As time slowed, the Skeleton King gazed at the countless black flashes covering every direction and murmured to himself.

A path he had not yet taken.

And yet, one he would have to walk in the end.

He quietly closed his eyes.

Of course, he knew.

If he moved now, he could still avoid Erasure.

If he struggled with every ounce of his strength, until the last fragment of his soul crumbled into ash, he might even leave a tiny sword wound on that terrifyingly powerful Ancient Dragon’s body.

But in the end, it would be pointless.

The gap in their power—the difference in their very being—was too vast for him to hope for anything more.

*There’s no turning this around. This body—or rather, Jin Taekyung—will fall here today. At the hands of a monster bent on destroying the world.*

And word would spread soon.

Everything moved fast in this world.

That was why he had drawn as much attention as possible on his way here in Jin Taekyung’s form. By now, everyone around the world would be watching Moscow closely.

*If that happens, I won’t regret it.*

But unlike the Skeleton King, the people would regret what they had done—and be furious.

At the sight of a hero, driven by an unseen hand to willingly meet his end, they would finally realize their mistake. Then they would unite and fight.

Even if the whole truth came to light, hearts once set would not be easily swayed.

*Yeah. That’s enough.*

But why?

Even after making that resolve and repeating it to himself countless times, why did his heart feel as heavy as lead?

The sound of space being crushed left his ears ringing. His eyes were firmly shut behind their lids, yet he could still see those faces and hear those voices. What were they?

And why—

*KA-BOOOOM!*

—hadn’t a single one of those terrible black flashes touched him, though the tremendous magical power seemed capable of devouring not only his body, but the soul within it, without a trace?

*This is…*

A sudden sense of déjà vu swept over him. The Skeleton King opened his eyes.

And saw him.

Far away, a Black Dragon sat leaning at an angle against his throne, staring at him with eyes that gleamed strangely.

“Just as I thought. Was that your plan from the start?”

“……!”

“I suppose I should take back what I said earlier. It seems I underestimated all of you… No, I underestimated you.”

The Skeleton King’s reflection gleamed in eyes like pieces of obsidian.

After slowly wearing away over thousands of years, the Ancient Dragon’s heart was now pounding fiercely.

“Why didn’t you dodge?”

The Skeleton King gritted his teeth at the question. Morgoth had already seen through not only his appearance, but the whole situation.

“Because I had to.”

“……!”

*Crack.*

The armrest of the golden throne crumbled to dust.

But it was not an outburst of anger at the Skeleton King for trying to deceive him.

Morgoth was trembling.

With rising excitement and joy.

*Because you had to?*

Yes. This was it.

If the Skeleton King had tried to fight back in any way, Morgoth would have erased him with all his power, without the slightest hesitation.

He had no intention of letting a moment’s curiosity cost him the two prized catches he sought: Cheon Taemin and Jin Taekyung.

*The Adversary who defeated the Demon King in a mere human body. And the one who would lead the world after him.*

Those two alone had been Morgoth’s greatest purpose and reason for coming to this world.

At least, until a moment ago.

But the sight the Skeleton King had just shown him was enough to shake him to the core.

*A cursed undead monster, and it has a soul like this.*

Everyone wanted to live. Humans and monsters alike.

But sacrifice was different.

Morgoth had spent vast stretches of time among many races in the name of amusement. Yet even among the Elves of the forest, supposedly the most noble of them all, he had never felt so astonished.

No. There was no point in comparing them.

Just as Morgoth had been born to rule the world, they had been born with pure hearts.

But the Skeleton King was unmistakably an undead monster.

A being corrupted by an inescapable curse.

And yet he had tried to sacrifice himself—the very undead monster who should have been made of nothing but rage and fear.

Though he felt afraid of Erasure, and had the power to delay his end, even for a little while, he still refused to retreat.

*How is this possible?*

It was like discovering an entirely new species.

Morgoth, who had chosen to become an evil dragon, abandoning everything he had built over the ages in pursuit of curiosity alone, felt the strongest urge of his life.

To be precise, he felt a greed his lofty intellect could not possibly suppress.

*I want him.*

No. He had to have him.

A noble soul dwelling in the most corrupted of bodies.

If he could make this strange being, whom he had never seen before, completely his own, then perhaps he could reach not only that extraordinary essence, but the realm of the unknown he had longed for over thousands of years.

The greatest question—and driving force—that had made Morgoth who he was.

“This won’t do. I can’t hold back.”

The moment Morgoth murmured to himself and rose from his throne—

*Flash.*

It happened in an instant.

Morgoth’s figure vanished without a trace, though he had been dozens of meters away.

The Skeleton King, every nerve on edge, felt a sudden chill rush over him.

*Blink!*

The thought flashed through his mind, but it was already too late.

His opponent was a Dragon, born blessed by mana in a way no other race could approach.

Morgoth cast a wordless spell as naturally as breathing, pushed Blink magic past its limits, and appeared to strike the Skeleton King in the back.

*CRRACK!*

He couldn’t block it or dodge it.

His body flew like a cannonball with a dreadful cracking sound.

Before the Skeleton King could regain his balance in midair, Morgoth leapt across space again and reached for him.

*Fwoosh—slice!*

A chillingly low whistle cut through the air by his ear.

At the same time, the Skeleton King put everything he had into widening the distance—and realized his left arm had just been severed from his body.

He also knew that if he hadn’t twisted instinctively at the last moment, he would have lost something other than his arm.

*He was aiming for both my legs from the start. He wasn’t trying to erase me.*

Morgoth’s voice followed. The Skeleton King knew his guess had been right.

“Stop resisting. It’s only a waste of time.”

It was true.

There was nothing to add or take away from that.

The gap between them was dozens of times greater than the distance separating them.

“I’ve changed my mind. I want you.”

Morgoth’s eyes flickered with greed now, not mere curiosity.

The Skeleton King couldn’t fully understand this change in him, but he was certain of one thing.

In the pitch-black darkness where he could see nothing, a faint glimmer of light had finally begun to seep in.

“I understand. I am pretty damn handsome, after all. In fact, it feels like a crime to be stuck with a face this ugly.”

With a calm retort, the Skeleton King raised the [Hero’s Sword] at an angle in his one remaining hand.

*One chance.*

The only path left to him now. It would surely be the first and last.

*Vwooom.*

His enormous but murky magical power welled up.

It wrapped around the Skeleton King’s body, swirling around the silver blade—so utterly at odds with its nature.

Yet even that mighty force, rippling like living mist as it swallowed up the space around them, could not compare to Morgoth’s power.

“Skeleton King. You awoke in the darkest, coldest grave and took the crown in your hand—the king of the cursed undead.”

The Black Dragon Duke Morgoth, once a Dragon Lord who had ruled over three moons and a sun, twelve continents and nine seas, smiled brightly and spread his arms.

His pure yet impossibly powerful magical power, worthy of his title as a Demon Realm archduke, pressed down on everything.

“Come to me—to your true master.”

At that very moment—

*Fwoooosh!*

The space between them disappeared.

No—the Skeleton King saw it twist and vanish at the same time.

But unlike Morgoth, who came hurtling toward him faster than sound, his wings of magical power spread wide, the Skeleton King’s two legs remained firmly planted where they were.

All that remained was the final strike he would unleash with his one remaining hand.

*Shwoosh!*

The tip of the sword shot through the air.

Without the slightest tremor.

With confidence, yet calm.

Carrying a force greater than anything it had ever borne, it flew in the single direction its wielder intended.

Not at Morgoth, but at the Skeleton King’s own neck.

“……!”

If a scream could make no sound, would it look like this?

In the instant, divided into countless fractions of a second, Morgoth witnessed the unbelievable sight. His eyes flew wide and he reached out.

And then—

*FWOOSH!*

A flash, deeper and more vast than any darkness, erupted and swallowed everything around them.

* * *

If someone living in Moscow had survived to see it, they would surely have thought of one word:

Apocalypse.

The world’s death cry.

The end of all living things.

But in that place, already a land of death and little different from part of the Demon Realm, the first to sense danger were not humans.

*Thud.*

A rumble seemed to rise from deep beneath the earth.

The vast wave struck something beyond instinct, stirring the soul. Across the area, countless monsters raised their heads in unison.

Even the large monsters who, seized by a moment’s hunger, had been chewing a nearby Orc alive.

Even the Death Knights approaching to punish them, and the Liches raising undead monsters to reinforce their ranks.

Even the dragonkin circling the tall spires and the black clouds overhead.

Every last one of them stopped moving and turned toward the source of the ominous rumble.

The dwelling of the Black Dragon Duke Morgoth, now as good as their new king.

The Dragon Lair.

*Whoooosh!*

Suddenly, a beam of light shot upward.

No—darkness.

For some reason, it felt not the least bit familiar. It burst from the heart of the lair and rose skyward in a single enormous pillar.

Without end.

Erasing everything in its path.

It split the spires, the dragonkin, and the clouds blocking the light above them, then finally pierced the sky.

And then—

*Thud.*

The monsters, watching the strange sight with vacant stares, realized at the same time how precious the brief moment they had just been given was.

*Rrrrrumble!*

A beam of light poured down through the rift in the torn black clouds, illuminating the earth as it heaved and rolled in waves.
## Chapter artifact 1161

# Chapter 1161

A storm.

A storm of power that swept away and destroyed everything in its path—and, at the same time, a colossal explosion born of collision.

KABOOOOOM!

As the world shook beneath a roar that seemed to split the sky, the monsters staring blankly at the Dragon Lair, having forgotten even the savagery etched into their souls, suddenly felt darkness fall over them.

Then came an unimaginable force.

—!

Eyes wide, mouths agape. And finally, their legs frozen by primal fear.

The monsters could not even let out a death cry.

No—in their final moments, the pitiful screams they managed were swallowed and erased by the deafening roar.

The impact was so horrific that “unprecedented” hardly did it justice. They were swept away helplessly, crushed into ruin.

RUMBLE, RUMBLE—!

Would this be what it looked like if thousands upon thousands of meteors covered the sky?

The colossal castle, reduced to countless fragments by the tremendous blast of power, stained the air as it plunged down. At the end of its destructive arc stood the monsters, frozen like statues.

CRASH! CRASH-CRASH-CRASH!

Destruction and death.

Those two words ruled the area in an instant, and sky and earth shuddered beneath them.

Everything mingled.

Buried. Crumbling.

There was no way to stop it, no time to flee to safety.

Their tough hides and skin—so resilient that ordinary artillery could barely scratch them. Their bones, harder than alloys, and the immense durability those bones gave them.

And finally, the powerful magical power unique to superior monsters, which had made all this possible.

Nothing they had could save them from the death rushing toward them.

However brave a fighting dog might be, it would still be eaten by a tiger. Great strength was bound to yield to greater strength.

CRUNCH! CRACK!

An ogre with both legs crushed let out a shriek. A troll, half its body torn away by a fragment that had flashed past in an instant, shuddered and fell.

Even the Wyverns, descendants of Dragons who claimed the sky as their domain, would never fly again.

Those closest to the explosion’s center had either died the moment the shock wave reached them or were now falling helplessly, their proud wings gone.

The explosion of power spread in every direction beyond the vast Dragon Lair. Its unprecedented magical power engulfed the monster army that had been in the area.

Relentlessly. Greedily.

This wave of death, which seemed as if it would never end, only began to subside after swallowing tens of thousands of monsters.

And at the center of it all, one being opened his eyes.

*Psshh.*

Ash slid down his slender frame.

Morgoth rose from the ashes of what had been the Dragon Lair—no, the word “ruins” could hardly describe it now—and turned to survey his surroundings.

The earth was overturned as if by a massive earthquake, and monster corpses were piled up like mountains.

Green blood flowed in rivers. Through a break in the dark clouds, a single shaft of sunlight peered down at the dreadful scene.

Yet in this moment, not a hint of anger shone in the Black Dragon’s obsidian eyes.

“What a sight.”

That was all he said, the brief exclamation escaping through his cracked lips.

Nothing more.

Though a moment’s carelessness had cost him countless subordinates, Morgoth didn’t care in the slightest.

More precisely, there was no reason to care.

He had gained a treasure far more precious and fascinating than those trifling losses could ever be.

“To obtain something, one must pay a price worthy of it. Don’t you agree?”

It sounded like a question to himself, but the answer came before long.

From right at his feet.

“Shut… up.”

At the faint voice, as hazy as a broken radio, Morgoth breathed a sigh of relief.

“I’m glad you still have enough strength to speak. I was worried you might be erased.”

He wasn’t exaggerating.

The shock wave from the collision of two immense, utterly different forces had been truly terrifying.

If Morgoth hadn’t protected himself with all his might, his entire body might now have been covered not in dust, but in his own blood.

“Still, there was some unintended damage… What can you do? This, too, must be the order of things, determined by someone.”

Morgoth smiled and brushed the dust from his shoulder. Like the dust drifting away in a pale cloud, the deaths of inferior monsters meant nothing to him.

Now, only one thing mattered to him. The being before him was his greatest interest and sole objective.

“Thank you. For holding on so well. You exceeded my expectations in every way.”

In truth, even “exceeded” didn’t begin to cover it.

The blow his opponent had unleashed against himself, prepared to be erased, had awakened a sensation Morgoth had forgotten over the course of ages.

Tap. Drip, drip.

Liquid began to wet his feet.

Morgoth frowned as he looked at his own silver blood, like molten silver, and the blade protruding through his palm.

“Yes. So this is pain.”

A sensation he hadn’t felt in a thousand years.

That was why it hurt more. Stung more.

Perhaps it was because of the memory of the last day he had felt pain—and, at the same time, endured a humiliation greater than the pain itself.

“…Asmodeus.”

Morgoth murmured the name in a whisper, then, as if to shake off the memories of the past, yanked the [Hero’s Sword] free and gripped it.

*Crash!*

The blade, split in two, plunged deep into the ground.

Reflecting its owner’s form, now reduced to a head.

“Skeleton King. King of the cursed wraiths.”

Morgoth slowly bent down toward the Skeleton King, who glared up at him. He stroked the skull, where blue ghostly flames flickered in place of eyes.

“Can you see it? Your true self.”

“I told you… to shut up.”

“Calm your anger. You only need to acknowledge and accept it. Where you come from, and whom you belong with.”

His captivating voice rang out, almost like a hypnotic spell.

But the Skeleton King didn’t waver in the slightest.

Clinging to a thread of consciousness that seemed ready to snap, he squeezed out the last bit of strength he had and spoke.

“You really are different from that guy.”

“That guy?”

“Yeah. An arrogant, downright devious human. But…”

That guy—Jin Taekyung—had once told him:

You’re just you.

And—

“He’s my friend.”

“……!”

“He’s the one who pulled me out of that godforsaken darkness. He’s the one who showed me a new world I’d never known.”

He had seen so much.

He had learned so much.

He had left the Gate, where only darkness and death churned, and spent time with everyone beneath the shining sun.

There had been happy days and sad days, but every moment had been dazzling.

Because he wasn’t alone anymore.

Because he was with them.

That was enough.

“So don’t waste your time with any more of that stupid bullshit. You’d better get ready.”

The Skeleton King smiled.

Brighter and more radiant than ever.

“My friends will be here soon.”

At that moment—

*Flick.*

Like a lamp going out, the ghostly flames flickering in his empty eye sockets suddenly vanished.

“…Your friends, you say?”

Morgoth mulled over the Skeleton King’s final words alone. At last, the Skeleton King could hold on no longer and let go of consciousness.

Friend.

A familiar word, yet strange, as if he’d never heard it before.

Even though Morgoth had spent a long time in human society in another world, he had never been able to understand the idea of a friend.

Why did people with not a drop of blood in common care so deeply for one another? Why did they sometimes make the foolish choice to lay down their lives?

Morgoth knew all too well that they did such things. Why they did so remained a source of fascination and astonishment to him.

First, that the Skeleton King—nothing more than a cursed undead monster—could show such humanity.

And second—

*Jin Taekyung.*

A human who might have changed the Skeleton King into this extraordinary being.

*There’s more I need to find out.*

Of course, Morgoth already knew about Jin Taekyung.

The savior of a new age. The center of this world, a young hero who stood at the head of them all.

After Cheon Taemin, Jin Taekyung was one of the people Morgoth had to watch most carefully. That hadn’t changed.

He had simply gained a powerful curiosity about him unlike anything he’d felt before.

“Yes. I’ll have to get ready, as you advised.”

Morgoth murmured to the silent skull, then looked out over the earth, where the rumbling had finally stopped.

Perhaps it was because of the shaft of light peeking through the split dark clouds. The place, overturned and cracked all over, had lost much of its pitch-black color—like the Demon Realm—and much of the dense magical power that had seeped through it.

But Morgoth didn’t care.

He slowly roused the endless power in his heart: the magical power that was nearly infinite and utterly pure, the product of corruption.

No—he was about to.

Until he sensed someone unexpected.

*Vwoom.*

The magical power that seemed ready to erupt like an active volcano subsided. At the same time, the Black Dragon’s eyes grew dark.

Then, amid the unsteadily trembling air and the wind that had come to a stop, Morgoth’s tightly closed lips parted.

“My apologies. I didn’t realize we had a guest.”

Dark mist drifted away as he spoke in a low voice.

Beyond it, someone answered.

“I’m asking because I’m curious.”

The voice was calm, yet seething like lava.

“What’s that you’re holding?”
## Chapter artifact 1162

# Chapter 1162

For an instant, it was as if the world had stopped.

The haze of magical power faintly wrapping around the surroundings. The monsters’ corpses piled up like mountains, and the surviving monsters’ roars.

Everything around me vanished.

I could no longer feel or see any of it.

There was only one thing.

Far away, a man with pitch-black hair hanging down like a cloak, and the pure-white skeleton in his hand, burned into my retinas.

As if they were the only things in the world.

Pain clenched my heart.

“What are you holding in your hand?”

My restrained voice crossed the hundred or so meters between us. At the other end stood a man gazing at me in silence.

No—a wicked Black Dragon wearing human skin.

“Ah. This?”

A beauty that seemed to belong to another world, and an evil so pure it was all the more horrifying, spilled from his lips.

“A clue that may satisfy my long-held desire, and a very valuable trophy.”

Morgoth added, one corner of his mouth curling upward.

“Perhaps someone’s friend, too.”

“……!”

“The friendship between a human and a monster. It was a moving story. Judging by the fact that you came here alone, it seems it was all true.”

I didn’t know.

I didn’t know exactly what had happened here.

Or what had been said.

But I was certain of one thing.

The Skeleton King had done everything he could, and he had done it for me—for all of us.

That was why I couldn’t ask the most important question. His obsidian eyes watched me closely, taking in every part of me.

“Are you afraid?”

As if he’d read my mind, he asked. I gave him a brief answer.

“Yeah.”

“Of what?”

“There’s a crazy Dragon standing in front of me, and he’s holding someone I know very well. I want that guy to still be alive.”

Maybe it was my unhesitating answer. After a brief silence, Morgoth gave a quiet laugh.

“You’re honest. Almost disconcertingly so.”

“So, your answer?”

“Didn’t I already tell you? A valuable trophy. He was so violent in his rampage that he’s a little damaged, but I have no desire to see him shattered to pieces.”

The meaning behind those words was clear.

Right. He was still alive.

That bastard, the Skeleton King.

The answer I’d been desperately waiting for ever since setting foot in this godforsaken ruin.

Only then did I let out the breath I’d been holding. I put my whole heart into my words.

“Thanks, you son of a bitch.”

“Don’t mention it. I couldn’t pass up such a precious opportunity after all this time.”

“You don’t have a hobby of taking hostages, do you?”

“Hostage-taking? My intellect and stature are far too great for such a cheap amusement.”

“That’s good to hear.”

“Perhaps. Or perhaps it’s the worst news you could have heard. I make a clear distinction between trophies and everything else.”

“A distinction?”

“If something is too dangerous to possess, then it must be destroyed. That way, there won’t be any trouble later.”

Morgoth’s smile deepened.

“Just like you.”

At that moment—

*Vwoom.*

Magical power churned around us.

An unbelievably pure, colossal wave of power.

And a murderous intent so vivid it felt within reach.

“Were you planning this from the start?”

“No. But the moment we first met, I realized I might make the same mistake Asmodeus once did. And, more than anything…”

His unpleasant gaze, a mixture of interest and regret, pierced through me as if it could see right through my body.

“Prey.”

His hair, long enough to reach the ground, floated into the air.

Like the wings of a being from myth.

Except they belonged to a demon, not an angel.

“You already see me as prey, don’t you, Jin Taekyung? Young, strong human hero.”

Silence passed for an instant. I opened my mouth.

“Yeah. I do.”

A Hunter—the sword and shield that protects humanity, and a hunter.

But that wasn’t the only reason I intended to face him head-on.

If Morgoth had really been someone I could trust, I would have gladly done whatever he wanted.

I would have prostrated myself before him. If he’d told me to cut off my own arms and legs, I would have done it.

My life?

If the deaths of Cheon Taemin and me could bring peace to billions of people, I would have given them up without a second thought.

That was my duty.

But just as Morgoth had, I understood with absolute clarity the moment I faced him.

His eyes.

Those eyes, so clear they seemed pure, were no different from those of a child watching an ant crawl across the asphalt on a midsummer afternoon.

That was why tens of millions of lives had been ground to dust.

Right here, in the very place where I stood.

And one more thing.

“He’s not a trophy.”

“What?”

“He’s not some trophy. That guy.”

With a voice boiling over, strange enough to sound like someone else’s, I took a step.

Slowly. Heavily.

As my foot came down with more force than ever before, memories as vivid as yesterday sank deeper than its imprint.

*Thud.*

> “Human, instead of that, how about making a deal with me?”
>
> “A deal?”

Yeah. It was there.

A-rank Gate, the Black Forest of the Black Wizard.

We’d first met in that dark, damp forest thick with dead trees. And then we’d stayed together.

For far longer than I’d expected.

*Thud.*

> “Hey, Warlord Mon.”
>
> “Do not call me by such a name. I am the master of the Black Forest and commander of the mighty undead legion.”
>
> “Hmm. All right.”
>
> “At last, you understand.”
>
> “So, Bones.”
>
> “……Damn it.”

I couldn’t say exactly when it happened.

When I began to see him as more than just a monster.

> “Something wrong? Why’ve you been so down all day?”
>
> “I was just thinking about something.”
>
> “What?”
>
> “What kind of being was I, in the past?”

That day, I’d told him as he brooded that I didn’t really know, but he’d probably been a pretty decent guy.

And he hadn’t forgotten the words I’d let slip as if talking to myself, embarrassed for no good reason.

> “Human, I have a question.”

Even now, the memory stood clear before my eyes.

The spearhead of White Flame, which the Arch Lich had sent flying at me when I was too exhausted and injured to move.

The Skeleton King forcing his way out of my Inventory by his own power and shielding me with his entire body.

> “Why…?”
>
> “Human. I have a question.”

The voice I’d thought I would never hear again.

> “What you said to me before—did you mean it?”
>
> “Of course I did.”

Only after hearing my answer did his dim ghostly eyes curve like a crescent moon.

> “I see.”

The Skeleton Warlord I’d first met in the Black Forest fell.

> “You asked why.”

Then, on human land, a new being who’d sacrificed himself to protect humans rose once more with a shining crown.

Returning the words I’d once said to him—the words someone would never forget.

> “You’re cunning, but you’re a pretty decent human. That’s all.”

The Skeleton King.

King and master of the dead who wander the Nine Springs.

And…

*My friend.*

I was burning up.

The eyes fixed solely on Morgoth.

The two dantians that, like a volcano erupting after a long wait, poured forth Scorching Yang Qi without pause.

And the step I took, carrying every memory that had just passed through me.

*Crack.*

A deep rumble spread.

The devastated ground crumbled again.

Hairline fractures spread in every direction like a spiderweb, then erupted.

*Fwoosh—KABOOM!*

Flamefire Path.

I shot forward as a single, blazing streak of fire.

* * *

It happened in an instant.

*BOOM!*

With a sudden flare of blue-black flames, the hundred or so meters between the two of them disappeared at once.

No—“vaporized” might have been more accurate.

The heat Morgoth felt was that horrifyingly intense, and the speed surpassed even sound.

But—

*I can see it.*

The Black Dragon’s obsidian eyes flashed as they read and saw through everything.

The streak of fire rushing up to his face—and something that suddenly emerged from within its immense heat.

*Whoosh!*

“……!”

Morgoth’s eyes flew wide. In them, a silver spearhead slashed down at an angle.

Where had it come from? How?

He hadn’t sensed the power of any magic.

But before he could find an answer, the flames riding the spearhead thrust into his chest.

Or so it seemed.

For the briefest moment.

*Tap. Slice!*

In a moment split into smaller moments, Morgoth crossed the distance in an instant. He silently raised a hand to touch the area around his chest.

More precisely, the patch of skin that had been scorched black by the slightest graze.

“……Hot.”

The third time in thousands of years that he’d felt pain.

But unlike the undead monster that had inflicted the second pain on him, the human approaching from afar with his spearhead lowered still held immense power.

Enough to make Morgoth ask with genuine curiosity:

“Are you, by any chance, one of my kind?”

Slowly but carefully closing the distance, Jin Taekyung answered calmly.

“Yeah. Long time no see, son.”

“Your vulgar speech makes it certain you’re not one of my kind…but how can a human grow so strong so quickly?”

Morgoth already knew about Jin Taekyung. He knew a great deal.

And until Morgoth had been summoned to this world, Jin Taekyung’s power had been nothing like this.

“A lot’s happened. Things even you couldn’t possibly imagine.”

“Things even I couldn’t imagine…”

How could it be so fascinating?

But Morgoth had to force down the curiosity that rose unexpectedly from deep within him.

The human before him was dangerous enough that he couldn’t afford to be swept away by a moment’s curiosity.

“I’m afraid I’ll never get to hear that interesting story of yours.”

With a low mutter, Morgoth clenched both hands like claws and grasped at empty air.

No—he tore it.

*Grrrrrrk.*

The warped space opened its jaws, and beyond the gap, where only darkness rippled, beings that had remained hidden until now emerged.

*Clank, clank.*

Sharp spears and blades. Armor covering them from head to toe without a gap.

They numbered in the thousands and resembled one another like twins born of the same womb, and Jin Taekyung recalled the first day he’d returned to this world.

“Those are…”

“My most loyal guardians.”

Dragon-tooth soldiers.

Guardians born of Dragons and existing only for Dragons.

But that wasn’t all that made Jin Taekyung go rigid.

“……Pai Chen?”

At the familiar face among the Dragon-tooth soldiers, a low groan slipped from his lips.
## Chapter artifact 1163

# Chapter 1163

Partings always brought sadness and regret.

All the more so when it was a permanent farewell caused by the death of someone close.

But I had never wanted to reunite like this.

“……Pai Chen?”

A name slipped out like a groan.

And a face so familiar I could recognize it at a glance from far away, yet more unfamiliar than ever.

No.

Faces.

“Long ago, there were some especially exceptional beings in the world where I lived. The ones called warriors or heroes.”

The wicked Dragon’s voice, steeped in old memories, reached Jin Taekyung’s ears as he stood frozen like a statue.

“At first, they were a nuisance. I didn’t much care for them coming all the way to my lair to cause trouble over some trivial matter.”

Morgoth could never quite understand their behavior.

All he had done was burn a few cities and wipe out a kingdom, and they came all the way to his lair to make a scene.

“At least, not until I met one human.”

He was exceptional, even among the hundreds of heroes who had come before him.

Strong, tough, and more desperate in battle than anyone.

Perhaps that was why.

When he died, leaving behind nothing but a pool of blood—not even a proper corpse, just like all the other intruders—Morgoth felt regret for the first time.

And, deep in his heart, a powerful desire to possess him rose with it.

“That was when I began to collect ‘trophies’ in earnest.”

Not mere cold, hard gold and jewels, but special trophies that retained their own memories and light.

Humans, elves, dwarves. Sometimes monsters.

If they could be made to submit, he made them submit. If they refused every offer, he killed them just to keep them by his side.

His most precious trophies, under the name of Guardians.

And this fascinating collection had continued in an unfamiliar world called Earth.

“They’re still unfinished, but the material is good, so the results are excellent.”

“……!”

“What do you think of my new Guardians?”

Jin Taekyung didn’t answer the question, which was brimming with satisfaction.

No—he couldn’t. All he could do was stare at the faces, pale and bloodless, now standing at the head of the Dragon-tooth soldiers, and mutter their names to himself.

*Pai Chen, Joel Schumacher, Pablo Albatroses……*

Seven names.

Seven S-rank Hunters.

Heroes who represented their countries, comrades reliable enough to entrust with one another’s backs.

During the Black Dragon’s great invasion over the past several days, they had been reported to have perished gloriously, their bodies never even found.

And now they stood here.

Unable to rest even in death.

Reduced to puppets whose very souls had been stolen.

*Shing.*

They raised keen-edged swords, maces, halberds, and shields. They drew their bows.

Not at anyone else, but at Jin Taekyung.

The one who had been their only beacon in the darkness, lighting the way before them all—their hope.

*Fwoooosh.*

A cold wind swept across the devastated land.

The murderous intent of the monsters, now surrounding them on every side without a gap, surged like blades. Beyond the thousand Dragon-tooth soldiers, forming one enormous wall before their master, the wicked Dragon smiled white as snow.

“Now, shall we begin?”

And that one line was the signal that announced the start of everything.

*Rumble-rumble-rumble!*

A wave of monsters poured down without end, shaking heaven and earth.

At the same time, Jin Taekyung, who had stood frozen in the cold, half-opened his eyes.

*Whoosh—KABOOM!*

Blue-black flames burst out, coiling around his spearhead and flooding the whole area with blinding light.

* * *

*Slice!*

He slashed.

*Thwack! Thud-thud-thud!*

He stabbed.

*Crunch!*

He smashed and crushed.

And then—

*Rumble!*

He pushed forward.

*Ding. Ding. Ding.*

> **System**
>
> You defeated the Lv. 98 Enhanced Minotaur Warrior!
>
> You defeated the Lv. 110 Enhanced Twin-Headed Ogre!
>
> You defeated the Lv. 120 Enhanced Death Knight!
>
> …
>
> EXP gained is reduced due to the difference in strength!
>
> You gained a small amount of EXP!

Jin Taekyung let out the breath he’d been holding.

The chimes ringing incessantly in his ears seemed to grow more distant. The stench and roars pouring from the monsters had never been closer or clearer.

“Gwoooar!”

Suddenly, a shadow fell across hundreds of heads.

The Cyclops, a one-eyed giant as tall as a walking skyscraper, slammed both fists down with a roar that shook heaven and earth.

*BOOM!*

Compressed air exploded. The mountain of force behind its fists crushed and burst everything it touched.

Everything except the one person it absolutely had to bring down.

By the time the giant finally spotted that human, smaller than its palm, a spearhead wreathed in blue-black flames was already boring into its single eye.

*Thud!*

The spear pierced its eye as smoothly as if slicing through tofu. At the same time, the dreadful heat flowing through the spearhead melted the giant’s brain and sent its massive body crashing down.

*Whoooosh—BOOM!*

A thick cloud of dust billowed upward.

Monsters caught beneath the dying giant screamed. Those who lost sight of their target in the momentary dust hesitated.

Not realizing that this was the last mistake they would ever make.

*Fwoosh!*

The cloud of dust split in two.

No—it evaporated.

At the same time, a spear shot through the air like a ray of light, sweeping through the Liches commanding the monster army that had survived the massive explosion.

*Rumble!*

Dozens of layers of defensive spells were useless. So were Blink spells cast in the blink of an eye.

More precisely, the unprecedented force carried by the spearhead made them all meaningless.

A power and speed so astonishing that even “overwhelming” fell short.

“What an interesting world. Truly.”

Watching Jin Taekyung dominate the battlefield like the hero of an ancient myth, Morgoth was genuinely impressed.

He had personally seen and fought countless powerful beings over the past several thousand years.

But neither an elven Elder who had lived nearly a thousand years, nor a Dwarf king blessed by the rocky mountains, nor the human knight called the greatest on the continent had ever displayed such martial prowess.

No. They had been nowhere close.

“Asmodeus, I think I’m beginning to understand why you failed.”

The humans in this unfamiliar world were strong.

They grew stronger through some mysterious power Morgoth couldn’t begin to understand. And a tiny handful of those humans, chosen from among the rest, became superhumans who far surpassed their given limits.

Like Cheon Taemin, who was as good as dead now.

Or the young hero of the human race, recklessly brave as he was.

And so—

*Vwoom.*

He had to crush them.

Even if he had to set aside his pride.

“Ice Wall.”

A short Spell, yet one imbued with powerful Magic no other race could match, rang across the battlefield.

*Fwoooosh.*

An extreme cold that froze everything spread across hundreds of meters.

At its far end stood a human who had reduced the endless flood of high-level monsters to a mere flock of sheep.

*Rumble!*

Suddenly, an enormous shadow fell across the ground.

An ice wall erupted around him, several meters thick and ten times as tall, enclosing him on every side. It was closer to a prison.

A prison built solely to hold Jin Taekyung—and a coffin prepared for his death.

“Hell Fire.”

*Fwoooosh.*

The sky turned red.

At the same time, a sphere of flame emerged from between the dark clouds.

An unbearable heat, so vast no Grand Mage in any world had ever imagined it, crashed down upon the ice wall.

*KABOOM!*

A blinding flash, fierce enough to make your eyes go blind just by facing it.

The flames, worthy of being called the fires of Hell itself, melted the ice wall and burned everything trapped inside.

The thousand monsters thrown away as bait—and one human who hadn’t managed to escape the spell’s range in time.

That was what should have happened.

*Tap. Tap-tap.*

A tiny tremor began among the monsters’ corpses, now reduced to piles of charcoal.

When a familiar face emerged from the gaps, Morgoth quietly licked his lips.

*He endured it? That spell just now?*

That hadn’t been ordinary Hell Fire.

He had used his knowledge to maximize its power and limits, and he had even put his full strength behind the attack.

A direct hit would have left even another Dragon with a potentially fatal wound.

And Jin Taekyung had withstood all that heat, without even being able to dodge.

Morgoth muttered in a low voice.

“This is…… a little troublesome.”

No, perhaps more than that.

An unpredictable danger always lurked behind a situation that exceeded expectations.

And this danger was bigger and faster than Morgoth had thought.

*Crack—BOOM!*

An explosion burst from Jin Taekyung’s toes with a thunderous roar.

Just like the meaning contained in the name Flamefire Path, he surged forward, blazing a trail of blue-black flames.

*Slice, rumble!*

Everything blocking his way was split apart and broken.

If the monster army flooding in from every direction was a wave, he was a single spearhead piercing through it.

One strike.

Then another.

An ogre’s head burst beneath a punch. A Death Knight struck by his whip-like kick never got back up.

And at some point, Jin Taekyung saw something familiar in the eyes of the monsters collapsing as they sprayed green blood.

Fear.

It was fear.

*Ding. Ding. Ding.*

> **System**
>
> You have met the activation requirements for One Against a Thousand!
>
> The enemies are greatly intimidated by the effect of the Title One Against a Thousand!
>
> Intimidation has greatly increased due to the effect of the Title One Against a Thousand!
>
> Enemies who fear your Intimidation are beginning to retreat!

A sturdy dam crumbled.

The instinct that had craved nothing but slaughter began to fade, and a strange emotion called fear filled the space it left behind.

“Gwoooar!”

The monsters turned their backs and fled, their roars no longer so ferocious. Jin Taekyung didn’t bother to chase them.

He still had enemies left.

And the battle about to begin would decide not only the outcome here today, but everything that came after.

*Squish. Squish.*

His weary steps splashed through pools of blood on the ground.

Beyond the thousand Dragon-tooth soldiers still standing like iron towers, Morgoth had been watching Jin Taekyung in silence. Suddenly, he spoke.

“You’re tired.”

Jin Taekyung answered in a weary voice.

“Thanks to you.”

“Do you think you can defeat me in that state?”

“Who knows? Maybe. If you’d just clear away the guys in front of you.”

“Perhaps. If I were a little more foolish, I might have.”

Morgoth fixed his gaze on Jin Taekyung, his eyes sunk deep, and continued.

“But I’m afraid I’ve already made up my mind. Today, just this once, I’ll set aside my pride.”

*Clank.*

The Dragon-tooth soldiers stepped forward at Morgoth’s gesture.

*Fwoooosh!*

Far away, beyond the horizon where the monster army had vanished, a flash of light flared.
## Chapter artifact 1164

# Chapter 1164

It was a pillar of light, vast and dazzling.

*Fwoooosh.*

A flash so brilliant it seized everyone’s attention in an instant.

And Morgoth knew better than anyone what had descended from the distant sky.

He simply couldn’t understand how it had become reality.

“How?”

Someone answered the question that slipped between his lips.

“Why are you so surprised?”

Jin Taekyung.

It was him.

Despite the exhaustion in his voice, a faint smile—one that hadn’t been there before—rested on his lips.

“Just accept it and move on. The weather’s nice. Don’t overthink it.”

“……What?”

Following the direction Jin Taekyung was pointing, Morgoth instinctively raised his head. Only then did he realize he’d overlooked something important.

It had split apart.

The dark clouds that had completely blocked out the clear sky and bright sunlight—his magical power, which had cut everything off from the world as it was.

The Black Dragon’s vast territory, once close to another Demon Realm, had begun to lose its power.

And this rift had opened because of Morgoth’s own greed, and the sacrifice of someone willing to face even Erasure.

“I told you. He wasn’t some trophy.”

At Jin Taekyung’s low voice, which seemed to bore into his ears, Morgoth remembered the precious trophy he had just moved to his subspace.

No. The Skeleton King.

“Yes. Perhaps he wasn’t.”

Resolve had brought about sacrifice, and sacrifice had led to an upheaval like this.

The Skeleton King had risked his life to unleash a tremendous explosion of power. That was what had created the situation before them.

It was the greatest reason that this utterly insignificant human’s Magic could dare to encroach on the domain of the great Black Dragon.

But……

“What can that small force possibly change?”

His voice not wavering in the least, Morgoth looked toward the distant horizon.

More precisely, at the group coming into view beyond the flash, which was already beginning to fade.

*BOOM!*

Before the light had even vanished, a thunderous boom shook heaven and earth.

Above the heads of the monster army charging the humans who had suddenly appeared and blocked their retreat, an endless rain of fire poured down, scattered by humanity’s strongest War Mage.

“A Warp on this scale, and wide-area Magic. Quite impressive. One step above the human mage from a few days ago.”

Quite impressive.

That was all Morgoth said of Magic Johnson, and there wasn’t a trace of arrogance in his appraisal.

Dragons were mysterious creatures born for Magic—Magic itself, one might say—and Morgoth was the very pinnacle of their kind.

Before he had even reached adulthood, Morgoth had already touched the limits of Magic. To him, the Magic of other races was little more than child’s play. That remained true even in this unfamiliar world called Earth.

Otherwise, Merlin—the Grand Mage who, after Siegfried Wassman’s death, was one of only two left alongside Magic Johnson—wouldn’t have chosen to blow himself up in the battle a few days ago.

“He was quick to catch on. When he saw me collecting the bodies of his comrades, he didn’t hesitate to choose death.”

The Grand Mage had been a rare trophy, so Morgoth had felt a trace of regret.

Not anymore.

“I suppose I should thank you. I never expected you to give me such fine trophies.”

Greed, held in check until now, glinted briefly in his two obsidian eyes.

Of the thousands of humans closing in as they crushed the monster army, only two posed even the slightest threat to him.

But even Magic Johnson and Chuck Hagel were no more than trophies in Morgoth’s eyes. And before Jin Taekyung, already weighed down by no small amount of fatigue, stood a thousand Dragon-tooth soldiers, each one practically a named monster in its own right, blocking his way like an iron wall.

Alongside them were the seven Guardians, reborn as beings far more powerful than before.

“Nothing has changed. This battle is over.”

He was right.

Anyone would have thought so.

The odds were overwhelmingly in Morgoth’s favor.

And yet.

They should have been. So why?

Jin Taekyung was still smiling.

At the same time, Morgoth saw an unfamiliar figure reflected in the heat shimmering in Jin’s eyes.

His own face, frozen stiff despite the words he’d just spoken.

“What’s so funny?”

Unable to hold back, Morgoth demanded an answer. Jin Taekyung lifted the spear he’d been leaning on like a staff.

“I just feel a little better.”

“……You feel better?”

“Yeah. I’ve been in situations like this plenty of times. Heard those same things you just said, too.”

Jin Taekyung spat out the phlegm gathered in his mouth.

“You know, the usual stuff. ‘I’m different from everyone else.’ ‘I never let my guard down.’ ‘I’ll kill you for sure.’ ‘It’s all over.’ That kind of crap.”

All those countless times he’d come close to death.

They were memories so awful Jin Taekyung never wanted to think about them again. But this time was different.

Why?

Simple.

“The weird thing is, not one of those bastards ever followed through on what they said.”

It was true.

He’d fought every one of them, and he’d beaten every one of them.

His arms and legs crushed, his insides churned to mush, brought to the edge of death—he had always been the one to survive.

But perhaps the deepest reason he’d won so many hopeless battles wasn’t just the power of the System.

“Why was that? Some of them really could’ve killed me. So why waste time on pointless words and actions, leaving themselves open?”

He was afraid.

Always. Every time.

In battle—and even in every quiet moment of everyday life.

He feared losing his life to some powerful enemy he would meet someday, and he suffered at the thought that he might have to stand on someone else’s sacrifice to survive.

So whenever he met an enemy, he hurled insults at them.

He piled on every kind of abuse, then dragged up even the smallest fragments of anger and grief sleeping deep inside him, smothering his fear beneath them.

He had to make himself stronger, even if that was the only way.

People called him a hero, but the person he knew himself to be was far too weak to carry such a heavy burden.

But looking back, he hadn’t been the only one afraid of the person standing in front of him.

“Then, all of a sudden, I started feeling better.”

Jin Taekyung had finally realized it.

“The guys I beat were afraid of me, too.”

“……!”

“What they said was all just fear talking. Same as you right now.”

Looking at Morgoth’s face, suddenly gone cold, Jin Taekyung smiled faintly.

“What, did I hit a nerve?”

Morgoth didn’t answer.

No—he couldn’t.

Everything Jin Taekyung said was true.

His pride and insight were too great for him to deny it.

“……Fear.”

He’d forgotten it.

More precisely, he’d tried to forget the one time he’d ever felt that pathetic emotion.

But at last, Morgoth had no choice but to admit it.

What he felt for Jin Taekyung was more than caution.

“Yes. I see. I was a little afraid of you, too.”

Though the strength of their feelings differed, their nature was the same.

Muttering in a low voice, Morgoth looked at the tiny human who had dared to make him feel afraid.

At the same time, he understood what he had to do.

“But I’ll swear to you one thing.”

*Vwooom.*

The wind stopped. The air around them shuddered.

“I am nothing like anyone you’ve faced before.”

At that moment—

*Fwoosh!*

Darkness erupted around Morgoth and swelled, engulfing his entire body.

It rose as high as the spire that now lay in ruins, and grew as vast as a fortress wall.

Jin Taekyung instinctively understood what the phenomenon before him meant.

*Polymorph.*

Would the world look like this if the sun vanished without a trace?

The Black Dragon finally shed his human skin. The darkness surrounding him blackened the sky overhead and the battlefield for hundreds of meters in every direction.

As if announcing the end of the world.

But Jin Taekyung’s eyes didn’t waver as he watched it all.

The darkness, having completed its task, was slowly dissipating. At the same time, a thousand Dragon-tooth soldiers, obeying their master’s command, were charging straight at him.

*It’s coming. It has to.*

He knew.

Just as darkness existed wherever there was light, a new light awaited him beyond this darkness.

And his faith was rewarded.

Just as someone had answered the voice with which Jin Taekyung had once cried out for salvation.

*Fwoooosh!*

The world lit up in an instant.

The horizon, sinking into darkness like an extinguished campfire, and the land, being swallowed by an even deeper gloom, were bathed in light.

In dozens, then hundreds of pillars of light.

In the hearts of those who had crossed thousands, then tens of thousands of kilometers, time and again, to answer his call.

“……What is this?”

The horizon blazed like a line of fire, crowded with countless Magic Formations of Warp.

At Morgoth’s groan, which thundered from high in the distant sky, Jin Taekyung spoke.

“I’ll swear one thing, too.”

His low voice rode the wind.

Along with the step he took forward, and the spearhead he leveled at the enemies bearing down on him.

“You’ll end up just like them.”

*Whoosh—slice!*

As fierce flames rose like dawn and lit the battlefield, a mighty roar raced along the horizon and shook the field of battle.

# Checkpoint Review — 805–809

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

# Chapters 805–809

## Plot

Jin and the Skeleton King battle the monster commanders as the army breaks through the Hunters’ defensive line. Jin kills the Manticore Lord, while Yamamoto kills the Lycanthrope Champion and an ally whose identity is not yet revealed. The Skeleton King defeats the Death Knight Legion Commander. With the flying monsters brought down and the enemy formation broken, the Hunters win the battle and pursue the fleeing army.

The victory costs 185 Hunter lives, and roughly five thousand monsters remain. Jin calls for the exhausted Hunters to regroup before continuing the mission to kill the Prophet. He suspects the Prophet planned the chaos and wants to face him, but the Prophet remains missing. Jin’s injuries worsen into the Broken Body debuff. After less than an hour of recovery, the Hunters prepare to continue; a memory of Michael Silbert prompts an unspoken question in Jin’s mind.

## Continuity

- Jin remains the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate the Prophet within an unspecified time limit.
- The Prophet’s location, identity, objective, and means of directing events remain unknown. Jin suspects the Prophet planned the battlefield chaos and wants to face him.
- The Hunter victory leaves 185 dead and roughly five thousand fleeing monsters. The surviving Hunters regroup before continuing their pursuit.
- Yamamoto Genji killed the Lycanthrope Champion; the unidentified ally who arrived and addressed Jin as “Jin Sama” also remains unidentified.
- The Skeleton King killed the Death Knight Legion Commander and helped bring down the flying monsters.
- Jin’s Myriad-Poison Ring absorbed the Manticore Lord’s venom, curing his Poisoned and Convulsions status abnormalities. He remains physically exhausted, with depleted internal energy.
- Jin has Broken Body in addition to Damaged Body. Broken Body weakens his Muscles and Bones, increases injury risk, and accelerates internal energy consumption. His condition improved somewhat after less than an hour of recovery.
- A memory of Michael Silbert has prompted a question Jin has not yet voiced.

## Translation Decisions

- Keep **magical power** distinct from **mana**.
- Use **Manticore Lord**, **Lycanthrope Champion**, **Death Knight Legion Commander**, and **Reverse Gravity**.
- Keep **Broken Body** distinct from **Damaged Body**.
- Preserve **“Jin Sama”** as the unidentified ally’s form of address.

## Durable state

{
  "active_continuity": [
    "Jin is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate the Prophet within an unspecified time limit.",
    "The Prophet remains missing after the Hunter victory; Jin suspects the Prophet planned for the battle’s outcome and wants to face him, but the Prophet’s objective and location are unknown.",
    "The surviving Hunters regroup before pursuing the fleeing army; roughly five thousand monsters remain, and 185 Hunters died in the battle.",
    "Jin has the Broken Body debuff in addition to Damaged Body: Muscles and Bones are weakened, injury risk is higher, and internal energy consumption has increased.",
    "A memory of Michael Silbert has sparked a question in Jin’s mind that he has not yet voiced."
  ],
  "continuity_sources": [
    809
  ],
  "open_questions": [
    "Where is the Prophet, what is his objective, and how is he directing events?",
    "What question did Jin’s memory of Michael Silbert raise?"
  ],
  "safe_through": 809,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Broken Body distinct from the existing Damaged Body debuff."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 805

# Chapter 805

A beast.

At this very moment, Jin Taekyung looked like a beast to everyone watching. Fierce as a hungry tiger, majestic as a lion, and swift as a leopard.

*Rumble!*

Sand and earth surged up, swirling in every direction. Jin Taekyung’s figure vanished from where he stood, as if rippling out of sight, then shot forward at terrifying speed.

Flamefire Path.

A single streak of flame cut across the space between them. It was incomparably faster than his earlier, reckless charge—and, at the same time, controlled.

Jin Taekyung felt he could now understand, if only a little, the enlightenment the two giants known as the Fire King and the Slaughter Saint had achieved over the course of their lives.

He even felt he knew how to bring down the enemies drawing closer by the second.

> **System**
> Lv. 130 Lycanthrope Champion
> Lv. 140 Death Knight Legion Commander
> Lv. 148 Manticore Lord

S-rank monsters whose levels had risen along with the increased concentration of magical power.

But Level wasn’t an absolute measure of an opponent’s strength.

A lower-Level enemy might possess far greater energy, while a higher-Level one could be physically weaker.

Once your opponent reached the highest tier, it ultimately came down to timing and matchup.

Just as Jin Taekyung had turned the Level 140 Scorpion King into a roast with his surprise attack a moment ago.

And there was only one way to figure out an opponent’s strength and matchup as quickly as possible.

Go head-to-head and find out.

*Whoosh.*

In the instant the distance of several dozen meters vanished—

Three streaks of light fell toward Jin Taekyung as he charged straight at them, keeping his center of gravity low.

*Shraaah!*

The Death Knight’s sword. The Lycanthrope’s axe. And, last of all, the Manticore’s claws.

Dark crimson magical power, so thick it seemed to warp space, pierced Jin Taekyung’s body.

Or at least, the three S-rank monsters had no doubt that it had.

*Boom!*

The earth flipped over with a deafening crash. Then a dark shadow fell overhead—

—and their instincts awakened alongside the warning lights flashing in their minds.

The S-rank monsters were intelligent enough that they couldn’t be dismissed as simple beasts. They immediately realized what had happened, and at the same time, were forced to accept the incomprehensible reality before their eyes.

That inside the small, frail body of that human, a force and energy greater than their own were boiling.

And in that moment—

*Heavenly Strike.*

As Jin Taekyung plunged toward the ground, blue-white hellfire poured down along White Flame’s spearhead and swept in every direction.

*Fwoosh—KRAAAAAASH!*

The ultra-hot flames, spreading as wide as a Grand Mage’s Fire Wall spell and burning even hotter, swallowed the front ranks of the monster army.

They were horribly ravenous to behold, more ferocious than any beast.

—Aaaaaaagh!

—Kieeet!

*Ding. Ding. Ding.*

System alerts mingled with the dying screams of monsters.

But the screams and System alerts weren’t all that awaited Jin Taekyung as he rose from the center of the blackened ash.

—How. Dare. You!

The Lycanthrope Champion.

The strongest half-man, half-beast, trapped beneath the curse of the eternal moon, roared and swung its enormous axe.

*Whoooom!*

Dark crimson magical power stormed through the air, cleaving space and erasing the wind.

Just as it was about to split the human in front of it clean in two, White Flame’s fire-wreathed spearhead shot up in a flash.

*Clang!*

A sharp ring. At the same time, the impossibly sturdy axe blade burst apart.

*Crack—BOOM!*

The shattered axe flew in every direction.

Hundreds of fragments rained down on the monsters rushing to save their commander.

*Thud, thud, thud!*

Screams and blood burst into the air. Corpses piled atop corpses.

Jin Taekyung stared at the Lycanthrope Champion, frozen with its bright yellow eyes wide, and slashed down with his spearhead without a moment’s hesitation.

Or he would have, if not for the whistling sounds rushing in from both sides.

*Whoooosh!*

Jin Taekyung bent backward like a lightning bolt had struck him. His hair touched the ground, and two fierce gusts passed just inches from his face.

*Pip!*

The skin split under the pressure, and a sharp sting ran through him—but that was nothing.

If this was the price of dodging an attack, it was an absurdly cheap one.

*I’ll just pay them back more than they gave me.*

His body moved before the thought was even complete. Straightening up, Jin Taekyung let go of the spear shaft and thrust out both palms.

*Whoom—BOOM!*

A shockwave and crash shook the ground.

But the sword and claws, shrouded in immense magical power, canceled out the aftershock of the Flame Divine Palm.

No—they didn’t stop there. They pressed the attack.

*Shraaah!*

The Death Knight Legion Commander’s strike cut down like a streak of light.

—Grrraaaah!

As the Lycanthrope charged with a roar, the Manticore Lord swung its iron-hard, spike-covered tail like a whip.

*Are they working together? Monsters of different species?*

Jin Taekyung’s eyes widened as he saw the attacks converging from three directions. That brief hesitation left him with the slightest opening.

*Fwoooosh! BOOM!*

There were no less than three S-rank monsters.

Together, their destructive power was too much to withstand even with his Scorching Yang Qi pushed to its limit. The Manticore Lord’s cunning and strength, in particular, exceeded his expectations.

*Whoosh. Slice!*

It was hot. Like being seared by fire.

But before he could fully register the pain in his thigh, three more flashes erupted one after another, filling his vision.

*BOOM!*

A deafening crash, as if the sky had split, sent him flying backward.

Jin Taekyung twisted in midair to regain his balance, and the moment he landed, he threw a punch.

*Poom!*

The heat of the Flame-Extinguishing Divine Fist erupted from his knuckles and swept forward.

Dark crimson magical power burst from between the monsters shrieking as they burned in the flames.

*Whoooosh.*

The flames died down in an instant beneath a pressure crushing in from every direction.

The three S-rank monsters, who had cut down even their struggling subordinates without hesitation, were about to charge at Jin Taekyung again when someone’s voice suddenly rang out.

—Good. That’s far enough.

The unmistakable sound of the Demon Realm language made them stop in their tracks.

Looking at the S-rank monsters, the Skeleton King grinned and tossed a remark at Jin Taekyung.

“You lunatic.”

Jin Taekyung met his hostile glare with a calm question.

“What?”

“What the hell are you doing charging off alone like that? Weren’t we just saying we’d each take one?”

“I was testing them out. Seeing which one was strongest and which was weakest.”

The Skeleton King’s gaze suddenly dropped. Jin Taekyung’s thigh looked as if something had torn a chunk out of it, and it was already covered in blood.

The Manticore Lord had aimed its attack with the Fire Dragon Armor around his upper body in mind. It was as clever as it was strong.

“Looks more like it tested your blood.”

“They’re stronger than I expected. One of them, especially, is practically a named monster even among the S-ranks.”

“Which one?”

“The one in the middle.”

“The Manticore? It does look exceptional, even at a glance.”

The Skeleton King glared at the Manticore Lord, his face hardening. His voice turned cold.

“So that’s the one who wounded you.”

“It’s not that bad. I’d be much better off taking the Manticore…”

“Fine. I’ll take the Death Knight.”

“…?”

“What’s with that unpleasant look?”

“No, I just thought this was where you’d say you were avenging your friend or something.”

The Skeleton King’s eyes widened at Jin Taekyung’s words.

“What the hell are you talking about? We’ve got a much better chance if the strongest fight the strongest.”

“…”

“Anyway, that’s the plan. You take the Manticore. I’ll take the Death Knight. And that Lycanthrope over there…”

The Skeleton King trailed off and looked around. Then he blinked.

“Why is it just the two of us?”

Jin Taekyung, who had staunched the bleeding in his thigh, kindly explained.

“One of them already ran off.”

“Huh?”

“Maybe he had a shred of conscience left, because he didn’t run off entirely. He’s back there in the front ranks.”

Far off, Yamamoto Genji had sidled up beside Choi Minwoo and was putting on a determined expression. The Skeleton King spotted him and muttered,

“I’ll kill that bastard someday.”

“Sure. But first, let’s finish this damn fight as quickly as we can.”

Jin Taekyung spat a mouthful of bloody phlegm and lowered his spear.

Behind him, the flying monsters were already screaming, and explosions were going off.

*Magic Johnson can hold them off.*

All he could do was trust him. Just as he, and the others, had trusted Jin Taekyung.

*Clop. Thud.*

The three S-rank monsters took a step forward, and the entire army moved with them.

No matter how many monsters they killed, the wave seemed like it would never get any smaller.

Meanwhile, the open desert all around them was the worst possible battlefield for humans.

“You know what I regret most since I became a monster?”

Jin Taekyung answered without hesitation.

“I know. Not getting to go clubbing.”

“Wrong. It’s getting mixed up with you.”

“Really? I’m the exact opposite.”

“What?”

“One of the best things I ever did was get you out of that Gate.”

“…Damn it. Am I the only piece of trash here?”

“You knew that already. Why ask?”

The Skeleton King let out a quiet laugh and took a deep breath. The aura of death that flowed out in place of breath raised the monsters scattered around them.

A total of one thousand.

That was the maximum he could maintain while fighting and directing them at the same time. But it was a meager force against the vast army drawing nearer, gradually picking up speed.

“Can we… hold them all back?”

No.

Jin Taekyung swallowed the answer that hovered on the tip of his tongue.

*Someone is going to die. No matter what.*

That was battle. That was why it was war.

There was no way to save everyone.

But there was one thing he could promise: not the hollow promise that everyone would make it out alive, but revenge.

“No matter how many of us die here today…”

*Shing.*

His words trailed off as his gleaming spearhead leveled at the monsters.

“They’re all going to die by my hand.”

The Skeleton King’s eyes widened.

*KRUNCH!*

A wave of monsters beyond counting swept over them.

* * *

…!

…!!

His ears were ringing. The ground shook beneath the movement of a monster army more than ten thousand strong, and their cries seemed to reach the ends of the earth and the heavens above.

And right at the head of that army, at its center, were those monsters.

*Fwoosh. Slice!*

Fire Dragon’s Single Tail.

A line of flame traced along the spearhead and cut through the air. Dozens of heads caught in its path—unable to dodge or block—rolled across the ground.

*Splatter!*

Blood burst belatedly, soaking the ground in every direction. But the monsters that should have charged with savage cries scattered in every direction, avoiding me and the Skeleton King.

Was it because of the martial prowess I’d shown, or my Intimidation?

No. The monsters avoiding me to charge the Hunters weren’t afraid. They were obeying someone else.

The kind of obedience you only saw in a trained elite army.

“You’ve got to be fucking kidding me…”

*Crunch!*

The Skeleton King blew apart an ogre’s head and let out an angry shout.

He and I had the undead army with us, but it was impossible to block every enemy’s path.

For every ten we killed, a hundred got through. For every hundred, a thousand monsters broke past.

The net we’d spread was tight, but far too small—and that was exactly what the enemy had intended.

—So it’s you. The human that person spoke of.

The voice seemed to come from inside my head.

Its smooth, composed tone, like a nobleman’s, showed a high level of intelligence. And the meaning behind its words matched my guess.

“The Prophet. Where is he now?”

A mythical monster with the face and body of a tiger, the tusks of a boar, and the horns of a bull.

The Manticore Lord smiled and answered.

—He is everywhere, and nowhere.

“What the hell does that mean?”

I answered the Skeleton King’s question.

“It means he’ll tell us if we beat the shit out of him.”

Then I brought my spearhead down toward the monster. No—toward *them*.

*Shwoosh!*

The wind split apart.
## Chapter artifact 806

# Chapter 806

There’s an old saying that’s been passed down in the Murim for ages.

*A Third Rate swordsman gets beaten to death by street thugs. A Peak master dies fighting another master like himself. But the only things that can kill a Supreme Peak master are his own arrogance and carelessness.*

That was how martial artists thought of Supreme Peak masters.

Beings to be marveled at and feared.

While everyone else wandered the treacherous mountains of the Murim, they stood tall on the highest peaks, looking down at them all.

But the word *invincible* has no place in this world.

Even among those who reach the chosen realm, there are clear differences in strength.

Those looking up from below can’t see them, but the ones standing on their own peaks can see and feel it:

Someone else standing on a peak beyond the thick fog, higher or lower than their own.

And I was no different.

*Shwaa!*

A sharp gust burst from the spearhead as it slashed down at an angle.

The wind tore the limbs off the monsters unlucky enough to get caught in its path, then shot toward its target. But a massive roar swallowed it up.

—Kyaaaaa!

A shockwave imbued with magical power faded along with the wind.

I looked at the monster that had canceled out my spear strike with a single roar.

*Strong.*

Magical power boiled all around us, prickling my skin. The air tasted bitter and stale each time I breathed in and out.

*Manticore Lord.*

A monster crawled out of myth.

And a leader strong enough to be called a *Lord* even among its kind.

*Step.*

The moment its lion-like forepaw touched the blood-soaked sand, its body vanished from where it stood and tore through space.

*Boom!*

As fast as the wind—or faster.

In some ways, it was far more troublesome than Leviathan, the most recent named monster I’d taken down.

Leviathan had possessed far more magical power, but the overwhelming strength I’d sensed earlier, combined with the speed and sheer size I saw now, made this one better suited to one-on-one combat than mass slaughter.

*And there’s the Lycanthrope Champion, too.*

This was a fight where I couldn’t afford to let my guard down for even a second.

Keeping an eye on the two S-rank monsters, I kicked off the ground at just the right moment—and sent a message to the Skeleton King through Sound Transmission.

—Don’t lose and embarrass yourself.

No answer came.

The Death Knight Legion Commander summoned a Nightmare, a ghost horse that was an A-rank monster in its own right, then leapt high and came crashing down toward the Skeleton King.

*BOOM!*

A thunderous crash erupted behind me, already far off in the distance. The Skeleton King’s voice rang out across the battlefield.

“Daring to challenge me, a mere legion commander! When you stand before a king, you get on your knees!”

It would be ideal if the Death Knight Legion Commander did as he said, dropped to its knees, and swore allegiance. But reality wasn’t so accommodating.

They already served another master—and a tail and claws brimming with magical power were bearing down on me.

*BANG!*

The spearhead of White Flame, held straight up to block the attack, shuddered.

But unlike our previous clash, this time it was my opponents who had to back off.

*Whoosh! Slice!*

My spear slashed down without hesitation, cutting through the Lycanthrope Champion’s huge, hook-like claw as easily as tofu.

*Not a difficult opponent.*

If it were the only one.

—Grr?

The Lycanthrope Champion let out a startled growl and stumbled backward. I was about to cut it in two when the Manticore Lord’s tail—knocked away by my spear—writhed like a snake and lunged for my face.

*Whoom!*

The pressure of the wind brushing past my neck was as heavy as a block of iron.

But I’d already dealt with this move once.

If I’d been facing all three of them alone, I’d have been in real trouble. But in a situation like this, things were different.

*One at a time.*

*Fwoosh.*

The Lycanthrope Champion saw the flames gathering in my hand and twisted away, but it was half a beat too late.

No—I was faster.

*BOOM!*

Struck dead-on by the Flame Divine Palm, it slid backward. For a brief moment, it clutched its one arm, charred black, and let out a roar like a scream.

—GRAAAAAH!

What a shame.

It was the weakest of the three, but it was still an S-rank monster. The attack just barely missed its intended target: its chest.

*One strike. One more and I can finish it.*

But the Manticore Lord was every bit as cunning as it was strong.

Just as I swung my spear to finish the Lycanthrope off, the Manticore Lord moved faster than it had at any point so far and went for my back.

*BOOM!*

I blocked the claw that came crashing down like lightning.

The spear shaft shook under the tremendous pressure, and my legs—usually free to move even in the desert—sank deep into the sand.

That, too, was exactly what the monster had calculated.

*Shwaa! Thud!*

Its tail struck my side with more weight and force than a battering ram.

The stinger on its tip couldn’t pierce all the way through my Fire Dragon Armor, but I had to bear the full force of the tremendous impact it delivered.

“Ugh…!”

My vision went hazy. At the same time, something hot surged up through my chest.

I swallowed the blood that welled up past my throat, then reached out despite my blurred vision.

*Open Inventory. Summon.*

As one hand left the spear shaft, the pressure grew even heavier. But I swung the dagger I pulled from my Inventory at the speed of a streak of light.

*Shhk, slice!*

There was one sound of cutting, but three thin lines crossed the iron-hard tail.

The Manticore Lord’s eyes widened just as it tried to crush me with its two massive forepaws.

*FWOOSH!*

Blood belatedly sprayed from the faint lines like a fountain.

Its jaws gaped wide in pain, and the stench of countless deaths poured out.

—GRAAAAAAAH!

A roar like a lion’s. The roar it unleashed from right in front of me left my ears ringing.

No—my eardrums had to have burst.

*You son of a bitch.*

I clenched my teeth, feeling hot blood running from my ears.

Then, taking advantage of the moment when its weight on me briefly eased, I drove the dagger still in my hand into its ribs.

*Thud!*

The Force on the dagger came from Scorching Yang Qi.

Like lava, its heat sliced through tough hide and flesh, broke bone, and burned its way through the inside.

*Sssss!*

—GRAAAAH!

—Kyaaaaa!

The Manticore Lord’s roar seemed to overlap, like a pair of broken earbuds. Maybe that was because my eardrums had burst.

But my instincts told me it wasn’t just my imagination.

*This…*

It was different. I hadn’t misheard the first time.

If the first cry was a scream of pain, the second was a roar of rage.

And my ominous hunches were never wrong.

*Lycanthrope Champion.*

The name came to mind, and the half-man, half-beast monster I’d momentarily forgotten lunged at me from behind.

*Shwaa!*

It moved at a blinding speed worthy of an S-rank monster.

It charged, its one arm dangling as if it were about to crumble into ashes, then swung its still-healthy arm. Hooked claws flashed.

*Too late to pull out the dagger and swing it.*

In that instant, countless movements and possible futures flashed through my mind.

Only one choice remained at the end of them.

In a world that had somehow slowed down, I let go of the dagger stuck in the Manticore Lord’s ribs and thrust out my palm.

*Fwoosh—crack!*

The internal energy I’d hurriedly drawn up scattered like sparks.

With a dizzying pain running through my hand, I stared at the silver claw that had pierced my palm and emerged from the back of my hand.

*…Fuck.*

Looking at the claw stopped just short of my face, I couldn’t help swearing.

But that wasn’t the end of the pain I had left to suffer.

*Crack. Crunch!*

Bones shifted with a series of cracks, and a neck stretched out like a turtle’s. At the brink of death, the Manticore Lord unleashed an ability it had cunningly kept hidden until the very end. Its neck surged over the spear shaft between us and lunged at me.

—GRAAH!

Its jaws gaped all the way to its ears like a ghost from a horror story, reeking of rotting corpses. The sight of those huge, serrated teeth sent a chill through my whole body, raising every hair on end.

“……!”

A chill ran down my spine.

If those jaws closed on me, all that would be left was death.

I twisted with all my strength. The teeth that had been about to swallow my entire head brushed my hair and sank into my collarbone.

More precisely, into the red armor covering my collarbone.

*CRUNCH!*

*Beep. Beep-beep!*

> **System**
>
> Part of your **Fire Dragon Armor** has been damaged!
>
> The durability of your **Fire Dragon Armor** has dropped significantly!
>
> **Danger! Danger!** If you are exposed to another attack like that, your **Fire Dragon Armor** may be automatically returned to your Inventory!
>
> **Manticore Lord’s Venom** has entered through the gap in the damaged armor!
>
> Status abnormality **Poisoned** has been applied!
>
> Detoxify as soon as possible! If you do not detoxify within the time limit, your condition may worsen!

*Damn it. What the hell is this now?*

My collarbone had been tingling, and now suddenly I was poisoned.

I was just a guy with a pair of balls, but this bastard was a named monster. No wonder it had so many damn abilities.

“……Human!”

Even while fighting, the Skeleton King had somehow seen what happened. His urgent shout came from far behind me.

But despite his worry, I had no intention of dying here. Not even the slightest.

If anything, I was almost glad that being **Poisoned** had dulled my senses.

At least now I wouldn’t feel much pain from what I was about to do.

“Thanks for the help, you son of a bitch.”

At my barely audible whisper, the Manticore Lord’s eyes widened.

I dropped White Flame from my remaining hand and struck the spot I guessed was its throat.

*Thwack!*

A heavy impact.

The Manticore Lord sucked in a breath, and its eyes turned vicious.

*Thud!*

Its teeth drove in with even more force than before, widening the gap in my Fire Dragon Armor and sinking deep into my collarbone.

The warning beeps rang in my ears, but the pain had dulled even further. Enough that I could move my hand without a care, despite its palm being nothing more than raw flesh pierced through by a hook.

*Crack.*

The Lycanthrope Champion’s claw remained lodged in my palm. It bared its teeth in a sneer.

Pure contempt.

But the sneer lasted only an instant.

—Grr?

Its face filled with surprise in no time at all. It blinked at me, unable to budge me no matter how hard it pulled. I calmly spoke to it.

“You really think I can’t beat your ass, you little shit, just because I’m in bad shape?”

Going by the Strength stats I’d built up, I outranked even an ogre’s dad.

Even with all my stats drastically reduced by the special debuff, my physical abilities were still comparable to—or better than—those of most S-rank monsters.

The Lycanthrope Champion was specialized in Agility rather than Strength. I could slam it into the ground with one hand.

“Now, you little punk… Attention!”

*Whack! Crack!*

The knee I kicked in the joint shattered in an instant.

As the strongest of the half-man, half-beast warriors let out a mournful cry, I kept a firm grip on its claw and slammed the monster into the ground.

*Whoom—BANG!*

The earth rumbled, and a cloud of dust rose. At the same time, blood burst from the palm the claw had just torn out of.

But only one thing mattered to me.

At last, one of my hands was free.

*Open Inventory. Summon.*

A sharp dagger flashed. Above it, blazing hellfire surged and flew toward the Manticore Lord’s head.

—…!

The Lycanthrope Champion realized my plan too late and threw itself forward, but it was already too late.

*Thud—KRAAAAAASH!*

The blade cut through hide, flesh, and bone. Then the flames exploded.

*Ding.*

Just as the clear chime I’d been waiting for rang in my ears, a flash of light suddenly swept in from somewhere and cut through the Lycanthrope Champion’s neck as it charged at me.

*Slice!*

“I’m here, Jin Sama!”

“……”

This son of a bitch stole my kill.
## Chapter artifact 807

# Chapter 807

Even a Supreme Peak master will go down if he gets kicked in the balls. No matter how strange or powerful a monster is, its weaknesses are much like a human’s.

Blow its head off, or burst its heart.

Of course, there are exceptions to everything.

There are Trolls that can put even a shattered head back together, and Golems that won’t fall until you destroy the core somewhere inside their bodies.

A Lich, both undead and a skilled black wizard, might store part of its soul in a Life Force Vessel.

But as far as I knew, there wasn’t a single Lycanthrope anywhere that could survive having its head cut off.

Not even one that was an S-rank monster and had earned the title of Champion as the strongest warrior of its kind.

“I’ve arrived! Jin Sama!”

“……”

I looked back and forth between Yamamoto Genji, who was chattering so loudly he was spitting, and the headless body of the EXP… No, the Lycanthrope Champion.

*No, fuck…*

What kind of bullshit was this?

It had been the perfect time to level up. The meal was already laid out in front of me, and some bastard had swooped in and gobbled it all up.

I was so furious, it felt like my hands and feet might start shaking.

*Beep.*

> **System**
>
> Status abnormality **Convulsions** has been applied!
>
> Status abnormality **Poisoned** is worsening!
>
> **Manticore Lord’s Venom** must be removed from your body as soon as possible!

“……”

Right. No wonder my hands were shaking so much.

With my condition already this bad, the anger made my vision blur for a moment.

If things had gone as I’d calculated, I’d have leveled up by now and recovered completely. But since it had come to this, I had no choice but to use another method.

“Um? Jin Sama, are you feeling unwell?”

“Does this look like I’m feeling fine, you fucking idiot?”

“Ah. Oh…”

I shut Yamamoto Genji up with a single remark, then muttered to myself.

*Open Inventory. Summon.*

The System manifested in response to the command.

*Shk.*

The moment my trembling fingers touched something cold, a clear chime unlike the earlier ones rang out.

*Ding. Ding. Ding.*

> **System**
>
> Equipped **Myriad-Poison Ring**.
>
> An unknown energy washes over your entire body!
>
> The **Myriad-Poison Ring** has absorbed **Manticore Lord’s Venom**!
>
> Status abnormality **Poisoned** has been removed!
>
> Status abnormality **Convulsions** has been removed!

As the chimes rang one after another, my vision cleared and the convulsions stopped.

The Myriad-Poison Ring had drawn in the poison spreading from around my collarbone throughout my body. It gleamed with its usual black light.

*I may not have leveled up, but at least I had the Myriad-Poison Ring. Thank God for that.*

It was a good thing I’d ended the fight quickly. The venom the Manticore Lord had carried was truly terrifying.

With Scorching Yang Qi, which was the natural enemy of poison, and a top-grade potion, I could have been cured without much difficulty. But a potion ultimately worked by paying in advance with the body’s energy and vitality to maximize its recovery.

In a situation like this, with so many enemies left, leveling up—with none of the risk—would have been a hundred times better.

Of course…

“A-are you all right?”

Some bastard had been hanging back, watching for an opening, then rushed in and stole the last hit from me.

“Forget it. Don’t worry about it.”

But what could I do?

The bus had already left, and I didn’t have time to stand at an empty bus stop waiting for the next one and slap Yamamoto Genji across the face.

The one bit of good news amid all the bad was that the Skeleton King was the kind of excellent monster who knew how to finish his assigned job on time.

*Crack-crunch!*

We’d gotten quite far apart while fighting our respective opponents, but I could clearly see—and hear—the Death Knight, well over two meters tall, crumple along with his armor.

His final scream came with it.

—GRAAAAAAH!

*Fwoosh!*

That was the end.

Black mist poured out from beneath the helmet pulled low over his face. The Skeleton King seemed to absorb the Death Knight’s soul as it spilled out just before Erasure. Then he grinned at me as I approached using lightfoot.

“You monster.”

Then he spotted Yamamoto Genji tucked under my arm like a piece of luggage and added, “That fucking bastard.”

I agreed. If that little shit had even slowed the Lycanthrope Champion down for a moment, everything would’ve ended much more smoothly.

But kicking Yamamoto Genji in the joints in the middle of a battle involving thousands—tens of thousands—of fighters would be something only a lunatic would do. If I had time for that, I needed to use it to save one more person.

“Let’s go.”

With that brief word, I shot forward. My limbs creaked, proof of the fierce battle that had just taken place, and my internal energy was considerably depleted.

Even so, I had to go. I had to fight.

*Shweee—BOOM!*

The spearhead of White Flame, sent flying with tremendous force, swept through the rear of the monster army swarming like ants.

A muffled boom swallowed the screams, and the flames that erupted in an instant burned the limbs off the living monsters.

*One more time.*

I kept running without slowing down.

I pulled another spear from my Inventory, gripped it in a reverse hold, and hurled it.

*Boom!*

A thunderous crack split across the desert.

The spear didn’t carry the same internal energy as the first one, but its spearhead still held all that terrible force and speed—enough to pierce dozens of monsters with ease.

*Crack-crunch!*

—GRAAAH!

Even a glancing blow burst their heads like watermelons, sending severed limbs flying into the air.

I could feel the monster army, which had seemed like it would never grow smaller no matter how many I killed, falter.

*Boom!*

—Grrk, gaaah!

The screams drew closer by the moment. The stench grew stronger.

By the time I hurled my spear for the third time, hundreds had already fallen. I kicked off the air and soared upward, then flung Yamamoto Genji from under my arm toward the ground and reached out.

*Come.*

White Flame came flying in response to the call through my Middle Dantian and landed in my hand with a snap.

Somehow, its familiar grip had become so natural that I could recognize it without even looking.

As soon as I reclaimed it, I poured in Scorching Yang Qi. The transparent spearhead took on a reddish glow.

*Fwoosh.*

Flames. Wind. A world moving slowly.

And… the eyes staring blankly at me as I soared through the air, with the entire battlefield laid out below.

*Whoosh.*

The wind brushed across my body. Time, which had stopped, gradually returned to its usual pace.

I saw conflicting emotions surface in countless eyes that had opened wide.

There was joy in some. In others, despair was slowly sinking into reality.

Humans and monsters. Monsters and humans.

Which of the two opposing species was rejoicing and which was despairing? No one here needed to say it.

*Fire Dragon Divine Spear. This form.*

I drew in a breath.

My body descended slowly, keeping pace with time as I perceived it, while the flame-filled spearhead rose high, as if to pierce the sky.

*Fwoosh.*

At that moment, when the space around me warped under the extreme heat, a massive shadow that had been circling over the Hunters surrounded by monsters shot toward me.

—Screee!

A piercing cry rang in my ears.

At the same time, I could sense it without looking. Unlike the other monsters, it was flying toward me like a streak of light. The gale raised by a single flap of its wings carried immense magical power.

*The leader of the Griffins.*

Yeah. It had to be.

As a flying monster that ranged through the sky as if it owned it, it was one of the most troublesome opponents in its own way.

But…

*I don’t care.*

Ignoring the Griffin leader rushing at me with its gale of magical power, I brought the spearhead down.

Heavenly Strike.

*Whoooooom!*

Flames poured over the spearhead of White Flame, wiping out the gale of magical power rushing toward me and cleaving through space.

A fierce, razor-sharp slash, like a dragon’s claw, rained down toward the center of the densely packed monster army.

*Fwoosh!*

The heat and flash were so intense they seemed capable of melting everything before they even touched it.

Hellfire engulfed hundreds—maybe a thousand—monsters and exploded.

*BOOM! Rumble-rumble!*

A rain of fire poured down. Screams and death flowed like lava.

Neither the hides of the upper-level monsters—unmarked even by bullets—nor the quick-footed lower-level ones who sensed danger and tried to flee could escape it.

Death was equal for all the monsters, and the leader of the Griffins watching the scene let out a roar like a scream.

—Kyaaaah!

*Whoom.* A heavy pressure pushed against my whole body.

I raised my head. The leader of the Griffins, already overhead, was shooting toward me.

Even within its massive shadow, which blocked the sunlight, the monster’s beak shone like the sun, packed with immense magical power.

What if I met that attack head-on?

Even I wouldn’t come away unscathed.

At the fork in the road I’d faced a moment ago, I’d chosen not to fight it, but to break up the monster army’s formation.

But—

“I don’t have to be the one to do it. Right?”

—…!

The eyes of the flying beast narrowed into vertical slits at the Demon Realm language that came through the System.

A brief hesitation in its final moment.

And the ones waiting for that very moment didn’t betray my faith in them.

*Shwoop! Clang!*

The leader of the Griffins deflected something that flew up from the ground with a sharp crack, then staggered, unable to withstand the force.

*That’s…*

A bone spear.

As I watched it fall to the ground after serving its purpose, I thought of one person—or rather, one monster.

The Skeleton King.

That bastard, who never got tired and was much slower than me, had finally made it all the way here.

But the person I’d truly been counting on was someone else.

*Rumble.*

The air all around us shuddered. Everyone here, not just me, felt the battlefield’s atmosphere grow heavy.

I felt the wind die down in an instant, and the enormous mana rising from somewhere deep below press down on the battlefield.

—Screep?

The leader and more than a hundred Griffins looked at one another in confusion.

They were no longer flapping their wings.

No—they’d been bound in midair by someone.

“Rise, then crash back down.”

The voice that followed was stripped of every trace of his usual cheer. It was bleak and subdued.

“Reverse Gravity.”

And then—

*Whoooooom!*

Gravity within the area went wild.

Mana seized the remaining flying monsters with precision and slammed them into the ground.

—Screee!

Listening to the leader of the Griffins cry out, I found myself wondering what to call the sight of a massive flock of nearly a hundred Griffins plummeting toward the ground like streaks of light from hundreds of meters in the air.

A spectacular sight? Or…

*Magic?*

At least one thing was certain.

The Grand Mage who had staged this spectacular scene to close out the battle certainly deserved to be called the world’s greatest War Mage.

*Rumble! Crack-crunch!*

The flames spread without end. Chaos took hold. Countless monsters were crushed beneath the Griffins’ huge bodies as they rained down like a meteor shower.

Watching the monster army, its center completely broken, I shouted as I poured internal energy into my voice.

“Formation! Change!”

This battle was already won.

“Kill every last one of those bastards!”

A massive roar shook heaven and earth. The thousand spears and blades, still sharp, surged forward like a wave.
## Chapter artifact 808

# Chapter 808

The Great Cataclysm was a massive event that changed the course of human history.

Naturally, it had been the subject of countless studies and analyses. Scholars around the world named three decisive reasons humanity had been able to win.

First: the existence of Cheon Taemin.

Second: the emergence of the Awakened, who would come to be known as Hunters.

And third, the last one:

*The intelligence and will of human beings.*

They were right.

If Cheon Taemin’s existence and the emergence of the Awakened had been unexpected salvation, human intelligence and will were what allowed us to overcome any crisis.

That was what had let humanity win—and what had caused the monsters to lose.

Decades ago.

And… right now, in this very moment.

*CRRRRACK!*

With a tremendous roar, a thousand Hunters surged forward like a wave.

The healers’ blessings rained down over the tanks, who had exhausted every ounce of their strength holding back the monsters pouring in from all sides. The towering Grand Mage dispelled the defensive magic that had enveloped the area and revealed his true power.

“Burn as bright as you like, and cut right through them.”

His voice seemed to boil with power as a massive amount of mana surged.

It was a large-scale spell that would take an ordinary mage several minutes to prepare.

But following the staff Magic Johnson swept through the air, a magic circle appeared overhead and finished forming with just a short incantation.

“Fire Wall.”

*Fwoosh—WHOOOOSH!*

Flames carrying a horrible heat raced in every direction. They burned through thick scales, melted flesh and bone, and split the monster army’s ranks apart.

—Kyaaaaaah!

Horrible cries of pain rang out as a choking stench rose all around us.

A wide-area spell that tore right through their densely packed formation.

In the midst of the chaos, one of the higher-level monsters, which seemed to have a fair amount of Intelligence, hurried to pull the broken formation back together.

Or tried to.

—Alu. Karsh…!

*CRUNCH!*

Before it could, I dropped from above and drove a punch infused with internal energy into its head, bursting its rock-hard skull.

*Ding.*

> **System**
>
> You have defeated the Lv. 101 Minotaur Warrior!
>
> You have gained a small amount of EXP!

*Slump. Thud.*

With the System notification, its stumbling body fell like a rotten log.

I spat on the corpse, adjusted my grip on White Flame, and muttered, “You piece of shit. Who asked you to ruin the moment?”

At the sight of me dropping out of the sky like a comet, the monsters around me blinked. Their eyes were as innocent as those of herbivores gathered by a stream.

But I already knew.

Those eyes only looked so gentle because they were incredibly stupid. The instincts hidden behind them were more savage and cruel than those of any living thing in the world.

—Grrk?

“Nice meeting you. Now get lost.”

With a greeting that would be both my first and last, I twisted around and swung the spearhead.

*CRRRACK!*

Flesh and bone came apart, and a haze of blood spread through the air. Dozens fell in a single strike; with the second, swung as I stepped forward, the area around me was empty.

*Squish.*

As I approached, stepping through the blood-soaked sand, the air around me gave a sharp, tingling hum.

The heat stirred up by Scorching Yang Qi was intense, but the monsters looking at me had long since frozen their eyes cold.

One Against a Thousand.

The overwhelming martial prowess and aura radiating from me.

The **Intimidation** pressing down on their bodies felt close enough to touch. Fear erased their ferocity and swallowed their instincts.

And the Hunters, who had patiently waited for this moment, didn’t let it pass.

*CRUNCH!*

“Charge! Wipe them all out!”

“Die, you bastards!”

*Clang-clang! Slice!*

With a tremendous roar, a shining wave of steel crashed into the monsters.

It had been a relatively short time, but these elites had held their ground against a force more than ten times their size without taking heavy losses.

After holding back for as long as they could against the endless tide of monsters, the Hunters seized their chance. They plunged into the formation broken apart by Magic Johnson’s wide-area spell and stabbed and slashed at everything in their path.

*Slice, thud-thud-thud!*

“God damn it! Motherfucker!”

—GRAAAAAH!

Curses and screams mingled as Force and magical power, light and darkness, clashed all around us.

And the scales of that clash were tipping toward the light by the second.

“Team Three, eyes on two o’clock! Circle around and break through!”

“Ranged unit, get ready! Fire!”

“Fire!”

*Whoosh-whoosh-whoosh—BOOM!*

A rain of arrows fell with a sharp whistle as they cut through the wind. The mages’ wide-area spells swept across the battlefield.

Each team moved like a living organism. Their tactics were disciplined, always aimed at the enemy’s openings.

The monster army had grown stronger than before as magical power became more concentrated.

But if superior physical abilities and magical power, granted at birth, were enough to win every battle, the monsters would have already conquered the world.

“Come on, you bastards.”

I shot forward, my voice cold. The moment I chose a target, my body was already moving—erasing the distance and launching into its next action.

*Slice, boom!*

I cut down the goblin shaman trying to prepare a spell, then smashed the chest of the Orc chieftain beside it.

A rain of arrows poured down over the Orcs, who were left scrambling after losing their chieftain in an instant.

*Whoosh, thud-thud-thud!*

Arrows wreathed in Force pierced their thick hides, passing through their heads and chests.

Just as a particularly huge Troll hurried to retreat at the sight of me approaching, two streaks of light curved out from behind it.

*Thud, slice!*

The first sword pierced its chest. The second cut off its head.

Their movements were perfectly coordinated, without a hint of hesitation or wasted effort.

The swordsmen who had chopped the Troll—which still writhed despite its fatal wounds—into dozens of pieces spotted me and smiled faintly.

*Xiao Shen. And Team Leader Choi.*

There was no time for the two of them and me to exchange words in the chaos of battle.

Especially when we understood each other without saying a thing.

They gave me a light nod, then charged toward another target. They were going after the higher-level monsters intelligent enough to control their respective groups.

*Good choice.*

Most people instinctively resist killing living things—especially other people.

I didn’t know if that instinct had been ingrained over the course of history or learned through civilization, but there was no doubt it existed.

Monsters were different from the start. Born to a fate of struggle, they barely even recognized their own kind.

*If we take out the monsters leading these groups, the real chaos will begin.*

No—chaos had already begun.

Four S-rank monsters, including the most powerful of them, the Manticore Lord, had fallen. On my orders, Magic Johnson and the Hunters, who had been focused solely on defense, were now plunging into the center of the monsters and cutting them apart.

The higher-level monsters leading each group, their equivalent of lower-ranking commanders, were falling all over the battlefield at the hands of A-rank Hunters led by Team Leader Choi and Xiao Shen. Yamamoto Genji was also making a conspicuous contribution.

“Hup. Gale Slash!”

The name of the technique, barked in a low voice, was pure Japanese bravado. But the power behind that single sword strike was no bluff.

*Shwaa—slice!*

With a flash of light streaking across the battlefield, dozens of monsters fell, spraying blood.

Hunters rushed into the space that had been emptied in an instant and cut down every monster in their path.

*CRUNCH! FWOOSH!*

The formation slowly collapsed, and the front line was pushed back.

But waiting for the monster army as it gave ground, step by step, were the Skeleton King and a thousand Skeletons, blocking off their rear.

“Surround them! If you have no teeth, then hold them back with your bones!”

*Clack-clack-clack!*

—GRAAAAH!

*CRUNCH!*

A massive monster several meters tall swung its mace and smashed a dozen Skeletons to pieces.

At the same time, dozens of Skeletons used the opening to latch onto it or climb up its body, sinking their rusty swords and teeth into its enormous frame.

*Thud. Crack!*

—GRAAAAAH!

The enraged roar turned into a scream of pain. Then, as the massive monster met a gruesome death, a cold blue light appeared in its eyes.

—Grr. Ah. Ah. Ah.

Reborn as an undead, the massive monster charged off, dragging its heavy body along.

The Hunters flinched at the sight, but once they spotted the Skeleton King, they went right back to fighting as if nothing had happened.

“Attack! They’re breaking!”

“Their formation’s falling apart! Don’t back down—keep pushing!”

It had been less than an hour.

But victory had already begun to swing toward humanity.

Thousands of monsters had already been wiped out. The force that had initially outnumbered us ten to one was now down to five to one—and the gap was shrinking by the second.

*CRACK! THUD!*

An Ogre Warrior, over four meters tall, collapsed without even a scream.

I leaped into the air, pushing off the shoulder of the monster as it tipped forward, its chest blown open. In the brief instant I was airborne, I took in the battlefield below.

*It’s over. If we keep pushing a little longer, we’ll win.*

The monsters no longer had any trace of the momentum they’d shown at the start, when they surrounded the Hunters and attacked without letup.

Having lost four S-rank monsters as well as the lower-ranking commanders leading their groups, the monsters were in utter disarray. The Grand Mage’s wide-area spells from the front, and the Skeleton King’s undead soldiers pressing them from behind, only made things worse.

*And the Hunters are fighting like hell, too.*

The monster army was now nothing but beasts with a lot of bodies.

Victory was only a matter of time.

Not one of those countless monsters could stop us. Could stop me.

Except for the one being that still hadn’t shown itself.

*Where the hell are you?*

Thinking of The Prophet, who was one big mystery, I dropped back toward the ground.

*BOOM! Slice!*

White Flame’s spearhead plunged down with me and split open another monster’s skull. Its body split cleanly in two and fell to either side. Between the halves, I saw eyes filled with fear.

“Die.”

I charged like a beast of prey and went on a rampage.

The lower-level monsters froze as though gripped by **Fear**, staring at the death rushing toward them. The higher-level monsters used every last bit of strength to fight back.

They fell in different ways, but the result was always the same.

Death.

*Thud!*

I twisted the spearhead that had pierced the Lycanthrope between the eyes, then pulled it free. Brains ran down White Flame’s transparent spearhead.

A dull ache crept through my arms and legs, which had been in constant motion.

*Damn it.*

How long had I been fighting? How many monsters had I killed?

I didn’t know. Better not to know. The moment my brain registered it, my body would only feel more exhausted.

If The Prophet, still nowhere in sight, was watching me now, all the more reason not to show any weakness.

*Hoo. Hah.*

I steadied my breathing and adjusted my grip on White Flame.

The moment I turned to face yet more monsters, I realized the scales of the battle had finally tipped all the way over.

*Rumble. Rrrumble!*

—GRAAAAAH!

—Krrk. GRAAAAH!

The desert shook. With terrified cries, wave after wave of monsters were retreating.

*They’re running. All those monsters.*

The thought that flashed through my mind was exactly what I was seeing.

The advantage in numbers?

The monster army, having lost its will to fight and fleeing at full speed, no longer cared about any such thing.

The Hunters stared, blinking, then raised their tired spears and swords. With bloodshot eyes, they raced after the monsters.

“Kill every last one!”

The only thing left on the battlefield now was slaughter.
## Chapter artifact 809

# Chapter 809

It was like watching a massive dam collapse.

*Boom. Boom. KABOOM!*

The most ferocious of the large monsters turned and fled.

Every time their several-meter-tall bodies took a step, the enormous weight crushed corpses and smaller monsters underfoot like tofu.

*Crunch! Crack-crunch!*

—Kiiiiie!

—Kyargh!

Painful death cries rang out all around us, but not one of them belonged to a Hunter. At least on this battlefield today, the weak weren’t human. They were monsters.

The strong devour the weak.

Monsters moved according to the instincts stamped into them from the moment they were born.

But unlike when they’d been seized by ferocity and destroyed cities and slaughtered humans, the instinct driving them now was something far more primal.

*Fear.*

Even the S-rank monsters, so powerful no one had dared meet their eyes, had been wiped out. Most of the leaders who’d led the groups behind them had been massacred, too.

The threadbare chain of command had collapsed, and the ten-to-one difference in numbers was rapidly closing.

There were still several thousand monsters, by a rough count. But a beast that had lost the will to fight was an easier target than a herbivore.

And the Hunters, despite having endured a grueling, hard-fought battle, had no intention of calling this hunt over.

“They’re running! Wipe them out!”

“Don’t let a single one get away!”

“Aaaah!”

Bloodshot eyes. Weapons slick with flesh and blood.

Proof of how fierce the battle had been, the Hunters were soaked in blood from head to toe. Looking like people made of blood, they chased down their prey.

They cinched leather straps around sword hilts that kept slipping from their hands, then felt for the quivers at their sides with arms trembling from drawing the bowstring so many times.

They were exhausted. They wanted to collapse on the sticky sand and sleep.

But they couldn’t stop.

“Because of you bastards, Benjamin—Benjamin’s… You motherfuckers!”

Some had lost friends.

“N-no! Emma!”

Some had lost a comrade who was also a lover.

“Motherfucker. Were you in San Francisco a month ago, too? What? Damn it. Quit spewing shit I can’t understand and go to hell.”

And others had to finish avenging something that had happened not so long ago.

They had to kill monsters, again and again, until this anger finally went away.

*Shhk. Thud!*

Monstrous shrieks rang out as green blood spurted in every direction. An arrow flew from somewhere, piercing an Orc’s head and then a Troll’s ankle.

—Krrk.

The Hunters surrounded the staggering Troll and scraped together every last bit of their mana, pouring it into their weapons. Dozens of blades, brimming with rage, hacked the monster to pieces.

*Thump! Crack-crack-crack!*

We’d fought against overwhelming numbers. The Hunters had suffered heavy losses, and the price they’d paid in blood had to be repaid in monsters.

“Die! Die!”

Hoarse shouts rang out here and there, voices raw from exhaustion and excitement.

After spitting on the Troll’s corpse, chopped up like ground meat, the Hunters moved on to find their next prey, their eyes bloodshot.

*Boom! Boom-boom-boom!*

Attack spells rained down.

Even now, thousands of monsters were tramping mercilessly over corpses and their own kind as they surged south like a wave. The Hunters stood in its path like an enormous reef.

And I was right at the center of it.

*Whoosh!*

A slanted downward slash.

A razor-sharp gust shot along the spearhead and swept past the fleeing monsters.

*Shraaaak.*

Blood burst out instead of a scream, soaking into the sand.

But the monsters lucky enough to escape the attack’s range widened the distance between us and picked up speed.

They were monsters who hadn’t even recognized their own kind as kin from the start.

With evasion now their sole priority instead of fighting, they fled desperately for their lives. Even now, countless monsters were scattering in every direction and escaping the encirclement.

*I can’t let them get away. I have to take down as many as I can.*

The battle was already over. The result so far was a great victory that would be talked about for generations and recorded in history.

But there were still roughly five thousand monsters left.

We’d killed so many, and yet there were still enough to make up a full army.

If we let them go here today, we’d be leaving behind the seeds of another disaster.

*Still, chasing them right now would be impossible.*

Everyone was exhausted from a long and brutal battle. Right now, the only things driving the Hunters were their anger and desire for revenge against the monsters. Nothing more, nothing less.

And I wasn’t the only one thinking this.

“Human!”

“Jin!”

The Skeleton King, who had been holding the rear, and Magic Johnson, who had fought his way through the monsters to reach us, came up on either side of me.

“We need to regroup as quickly as possible, then pursue them. It would be best to split the troops into separate units.”

Magic Johnson spoke in a breathless voice. The Skeleton King, who had just cut down an injured ogre that had fallen behind, answered him.

“I agree. My magical power is nearly depleted, but we can’t let this opportunity pass. I’ve already turned several Griffins into undead. They’ll be enough to give us a view of the area.”

I started to answer, then suddenly caught my breath. I struggled to steady my ragged breathing and only managed to nod. The Skeleton King frowned.

“Human, are you all right?”

“It’s… it’s nothing. Don’t worry about it.”

It was a lie.

My arms and legs felt as heavy as if they’d been soaked in water. The internal energy that had filled my dantian was already running low.

More than anything, the dull ache I’d felt deep inside my body on and off throughout the battle was growing worse.

*Damn debuff.*

I forced myself to keep a calm expression as I recalled the System message I’d seen a while ago.

It was one of the notifications that had greeted me just after I defeated Michael Silbert and woke from a long sleep.

> **System**
>
> All things come with a price. But you have once again ignored repeated warnings and used power that surpasses your limits.
>
> Information for the special debuff **Damaged Body** has been updated.
>
> The special debuff **Broken Body** has been newly applied.
>
> The existing stat penalties caused by debuffs remain unchanged, and the effects of the new debuff will also apply.
>
> **Muscles and Bones** have weakened. The chance of injury has increased considerably.
>
> **Internal energy** is consumed more rapidly. Your control over qi is no longer as free as before.

Broken Body.

That was the price I’d paid for ignoring the System’s warning.

The unprecedented destructive power of One Annihilation had eaten away not only at my enemy’s life, but at my own body as well. It wasn’t the kind of damage that could be healed by any method—not even leveling up.

*Should I not have used One Annihilation against Michael Silbert?*

The thought left a bitter taste in my mouth, but there was nothing I could do about it. Back then, I hadn’t had much choice beyond One Annihilation.

I pushed aside the potion Magic Johnson held out to me with a worried look and spoke.

“That won’t be enough. If I use a potion in a situation like this, I’ll only get more exhausted.”

“But—”

“Right now, pursuing them is the priority. Especially…”

“Yes. The Prophet.”

The Skeleton King murmured in a low voice. He understood what I meant from my expression and clicked his tongue.

“We haven’t found him yet. I thought he was watching from somewhere, but we were wrong.”

Magic Johnson added, “It’s the same for me. Jin, perhaps The Prophet was never here in the first place.”

“Never here? Then was it a trap aimed at something else from the start?”

“I can’t be certain. But it’s certainly possible.”

I thought for a moment, then shook my head.

Four S-rank monsters and an army of more than fifteen thousand monsters. That was far too much to use as bait for a mere trap.

*But why hasn’t he shown himself?*

The Prophet was an unpredictable powerhouse. He had killed Siegfried Bassman, the Grand Mage surrounded by all kinds of barriers, without leaving behind any obvious signs of a fight. His might might be on par with Michael Silbert’s—or even greater.

*If he’d joined the battle, who knows how things would have turned out.*

Even for me, fighting the Manticore Lord and the Lycanthrope Champion at the same time would have been anything but easy.

And that would have been the perfect moment for The Prophet to show himself.

*But he never did.*

Even if this battle had been a trap, and The Prophet’s real target had been our main camp, it still didn’t make sense.

It might sound embarrassing to say it myself, but I was the heart and head of the World Hunter Federation.

In the end, I reached one conclusion.

“It’s not a trap.”

I’d thought about it for a long time, but the time it took was short.

I looked at the Hunters, still chasing after the monsters like mad, and continued.

Even though the Team Leaders—the lower-ranking officers—were ordering them to stop the pursuit, they kept chasing, as if they’d gone deaf.

“I don’t know what The Prophet truly wants, but… this situation is part of his calculations, too.”

“What?”

“If we keep pursuing them without rest, the units will fall apart in no time. First, get the worked-up Hunters back under control as quickly as you can.”

“Jin.”

Magic Johnson looked at me, his eyes dark and serious.

“I agree that we need to regroup the troops… But then what did The Prophet drive all those monsters into this desert for?”

“Either he thought this much would be enough to deal with us…”

I stopped for a moment, then continued as if spitting the words out.

“Or he’s already built up a force so powerful that losing an army this size wouldn’t matter.”

“……”

“……”

The air around us went cold.

I looked at their stiff faces and let a thought I hadn’t been able to say aloud drift through my mind.

One thing was certain. My instincts, sharpened to their limit, had taken hold of me like a premonition.

*The Prophet wants to face me.*

The monsters’ cries faded into the distance. Only then did the wind blow among the people collapsing one after another.

Heavy with the stench of blood, it spread through the cool night air.

* * *

One hundred and eighty-five.

That was how many people had fought more bravely than anyone else—and, because of that, had crossed a river they could never come back over.

But those who survived had to keep moving forward.

We hadn’t come here to win a battle. We’d come to kill The Prophet and uproot the disaster he’d set in motion.

*There’s no time.*

The idea that the one being chased is more desperate than the pursuer is complete bullshit. Especially if the one being chased is carrying a bomb capable of swallowing the whole world.

“Everyone has completed their preparations.”

I opened my eyes as I listened to Team Leader Choi’s report.

Though I’d only spent a little under an hour circulating my energy, my body felt much better than before. My mind had settled, too.

*What the hell is The Prophet?*

It was a question I’d been asking for a long time.

The fifth Muninn. A being believed to be a monster, using magic that wasn’t human. And the desert’s pope, leading countless fanatics.

The more I learned about him, the deeper I felt myself sinking into a swamp. What was his true identity? What was his goal? And where was he now?

If the System were a physical being, I felt like grabbing it by the collar and demanding answers.

I’d take any debuff it threw at me. Just give me one tiny clue.

*Damn it.*

I cursed to myself and gazed up at the darkening sky.

Daylight in the desert was brief, and the sky was gray, perhaps due to the distribution of magical power.

Just like Michael Silbert.

That monster who had been born human and met his death as a monster.

And just as all my memories of him came back to me one by one—

“……!”

A question like a flash of light pierced my mind.

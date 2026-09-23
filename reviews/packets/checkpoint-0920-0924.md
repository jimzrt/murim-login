# Checkpoint Review — 920–924

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

# Chapters 920–924

## Plot

So Gyo’s attack devastates the rebels, and she reveals herself as the Bow Saint. The Emperor’s forces surround the banquet hall; Jin Taekyung, Jeok Cheongang, So Gyo, and the imperial troops defeat or capture the three thousand rebels. So Gyo tells Taekyung that he is the chosen one named by the Martial God, but postpones explaining.

The captured Eastern Heaven Demon Lord claims Dark Heaven has agents throughout the land and warns of a coming civil war. The Emperor explains that the Demon Lord poisoned and manipulated the former Emperor and court, and that the fourth prince’s restoration was meant to save the Great Nation. Prince Shangshan Zhu Bao apologizes to the Demon Lord for his grandfather’s actions and speaks of his dream of a peaceful age. Moved, the Demon Lord relinquishes his hatred and asks Taekyung to hear his final message. Taekyung receives it through Sound Transmission, then kills the Demon Lord with blue-white flames. The Demon Lord is revealed to be Wei Zhong, the East Depot’s Seal-Holding Eunuch.

## Continuity

- Wei Zhong, the Eastern Heaven Demon Lord, is dead; Jin Taekyung killed him with blue-white flames after receiving an undisclosed Sound Transmission.
- The Emperor’s blade pierced Wei Zhong’s throat before Taekyung’s final act; Zhu Bao’s apology and dream changed Wei Zhong’s resolve.
- Prince Shangshan Zhu Bao is thirteen and dreams of an age of peace in which no one suffers the misfortunes he and Wei Zhong endured.
- So Gyo is the Bow Saint. She identifies Taekyung as the Martial God’s chosen one and has a story to explain later; her allegiance remains unknown.
- The Demon Lord’s claims about Dark Heaven’s agents and an impending civil war are unconfirmed.
- Ma Sanbao remains missing. The Salcheonmun may pursue Mungyeong and may learn that Taekyung killed Gye Yabu.
- Jeok Cheongang, Hyuk Mujin, Ju Hwaran, Song Ilseom, Sama Pyo, Taishan, and the Divine Physician survived and reunited with Taekyung.
- The cause of Taekyung’s return from seemingly fatal injuries remains unexplained.

## Translation Decisions

- Keep “Eastern Heaven Demon Lord” as the title and “Wei Zhong” as his revealed personal identity.
- Keep “Force” for 강기 distinct from “death energy” for 사기.
- Render 반정 as “restoration,” preserving that it was disguised as a rebellion.

## Durable state

{
  "active_continuity": [
    "The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch; Jin Taekyung killed him with blue-white flames after receiving an undisclosed Sound Transmission.",
    "Prince Shangshan Zhu Bao, now thirteen, dreams of creating an age of peace in which no one suffers the misfortunes he and the Demon Lord endured.",
    "Ma Sanbao remains missing.",
    "So Gyo identified Jin Taekyung as the Martial God’s chosen one and intends to explain the story behind it later; her allegiance remains unknown.",
    "The Salcheonmun vowed to pursue Mungyeong regardless of cost or delay and may pursue Jin Taekyung if it learns he killed Gye Yabu.",
    "Jeok Cheongang, Hyuk Mujin, Ju Hwaran, Song Ilseom, Sama Pyo, Taishan, and the Divine Physician survived and reunited with Jin Taekyung."
  ],
  "continuity_sources": [
    923,
    924
  ],
  "open_questions": [
    "What did Wei Zhong tell Jin Taekyung through Sound Transmission?",
    "Where is Ma Sanbao, and what is his current status?",
    "What does the Martial God’s reference to a chosen one mean for Jin Taekyung, and what story has So Gyo kept to herself?",
    "Will the Salcheonmun pursue Mungyeong or discover that Jin Taekyung killed Gye Yabu?",
    "What enabled Jin Taekyung to return from his seemingly fatal injuries?"
  ],
  "safe_through": 924,
  "temporary_decisions": [
    "Keep “Force” for 강기 distinct from “death energy” for 사기.",
    "Render 반정 as “restoration,” while preserving that it was disguised as a rebellion."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 920

# Chapter 920

It all happened in an instant.

At least, that was how it felt to the East Depot masters charging at the vanguard, scrambling over the rubble of the collapsed outer wall.

*Fwoosh.*

What in the world was this?

How could anything be so fast—and so destructive?

The dazzling flash washed over their vision, leaving them stunned for a moment. It was the last thing they ever saw.

*KABOOM!*

A tremendous roar battered their ears. An irresistible force swept over their bodies, frozen like stone statues.

*Crack! Fwoosh!*

The flash vanished as quickly as it had come. One of the East Depot eunuchs charging alongside his comrades blinked.

Then, as his vision finally cleared, he understood.

That flash had been Force someone had sent flying.

That terrifying energy had swept away dozens of his comrades—and taken one of his arms, too.

“A-ah. Ahh. Aaaaaah…”

His jaw trembled. A dazed moan slipped between his teeth as they clattered without pause.

They were dead. No—they’d been butchered.

His pupils, fixed on what remained of his former comrades, sent the impossible sight to his brain: chunks of meat so mangled he could no longer tell what they had been.

Only then did pain reach him from his shoulder, horribly shredded as though a beast had torn into it.

“GRAAAAH!”

A scream of agony poured from his gaping mouth.

But he wasn’t the only one consumed by shock and pain in that moment.

“Ugh… Uuugh.”

“P-please, save…”

“Ugh—bleurgh!”

Some groaned as they clutched their severed legs. Some pleaded desperately for help on the brink of death. Others bent over and vomited at the carnage before their eyes.

They trembled, terrified by the gruesome deaths they’d witnessed with their own eyes, helpless to do anything.

Those who realized what had happened a moment later were little better off.

“W-what is this…?”

Some of the Imperial Guards, long since recruited by the Eastern Heaven Demon Lord and drawn into the rebellion, and the East Depot eunuchs who had led them into the grand banquet hall were struck speechless.

One strike.

A single strike had killed or incapacitated more than fifty soldiers.

They had charged at the vanguard without hesitation, and every one of them was a formidable fighter, ranging from Supreme First Rate to Peak.

Compared to the full force of some three thousand, it wasn’t a major loss. But everyone had stopped because that one attack had swallowed dozens of Peak masters in its terrifying power.

No—it was because of the master whose might seemed almost demonic.

*Who…?*

Who was it?

The question pierced everyone’s mind.

The three thousand rebels who had surged into the grand banquet hall.

The Embroidered Uniform Guard and Fire Dragon Pavilion members fighting the dead who kept rising no matter how many times they were killed.

Even the dead, who had lost what little reason they had left when the bell was destroyed, stopped moving at some instinctive warning.

Then they turned their heads.

Toward the source of the flash.

At the end of countless gazes stood someone, trampling the twitching limbs of the dead.

*Whoosh.*

A breeze from somewhere stirred the woman’s thick hair.

“So Gyo…!”

In the silence that had fallen over the hall, a cry like a scream rang out belatedly. The woman—no, So Gyo—lifted her head and looked toward the voice.

More precisely, at the person standing there.

Jin Taekyung.

Her lips moved silently, and her dark blue eyes sank deep.

* * *

Hundreds of steps leading up to the dais were already buried beneath countless bodies.

The thousand or so dead had been torn to shreds and finally died—or lay there writhing with their limbs severed.

As if hoping someone would put an end to their tenacious lives.

*Slice.*

A streak of light cut through the air.

The man who had split in two the body of a dead man crawling up the steps on a single arm lowered his sword and let out a ragged breath.

*Huff. Huff.*

His entire body, soaked in blood and sweat, heaved.

His golden armor and sword, exquisitely ornate as works of art, felt heavier than ever.

No—perhaps what weighed on him was the responsibility and guilt he had carried all this time.

And yet… he had no regrets.

He couldn’t afford to.

The Embroidered Uniform Guard who had fallen to ash here today had also been prepared to die.

To pity them for a sacrifice they had accepted of their own accord would be an insult greater than death.

Even if the man was the most exalted person beneath the heavens, the one above all others.

“Baek Yeon.”

The man—the Emperor—spoke, his voice rough with a metallic rasp.

Then he addressed the foremost military commander of the imperial court, who had done more than anyone to protect the late Emperor and the imperial family, and who had repeatedly lifted him back to his feet with harsh reprimands whenever he faltered. The Emperor gave him a request, not an order—as he would to a comrade rather than a subject.

“Sound the drum. The war drum.”

“……!”

Baek Yeon’s eyes trembled.

Taking in the Emperor’s exhaustion, his fatigue more visible than ever, he bowed deeply and extended a palm toward the great drum that had announced the start of the banquet.

*Boom!*

The drumbeat, charged with his profound internal energy, rang out without end.

It carried the heart of a warrior who had waited a long time for this day. It carried the Emperor’s will.

Once.

Then again.

The sound was immense enough for everyone in the grand banquet hall to hear. No—it rolled like a wave that would sweep through the entire imperial capital and beyond.

*Booooom!*

Even when the third drumbeat rang out, the three thousand rebels didn’t know what to do. They hesitated.

Everything had unfolded so naturally.

So Gyo’s overwhelming display of martial power had abruptly swept through the vanguard, and the drumbeat resounded with a grandeur they couldn’t explain. For a moment, they had been overwhelmed before they even knew it.

Even the Eastern Heaven Demon Lord—the instigator and center of the rebellion, who should have been leading them from the front—lay in a horrific state at Jin Taekyung and Jeok Cheongang’s feet.

*What is this? What in the world is happening?*

The Eastern Heaven Demon Lord had been captured. Ma Sanbao was nowhere to be seen.

The Imperial Guards and East Depot leadership who had already betrayed the imperial court and the Great Nation to join Dark Heaven were thrown into confusion. They looked at one another, their eyes bewildered.

When they took the Outer Palace, they had thought it was all over.

Even when they had seized every gate leading into the imperial palace and defeated the remaining defenders, taking advantage of another allied force sweeping through the capital, they had been certain a new age was about to begin.

But the reality they’d met with such joy—and the battle that should already have been theirs—had turned out differently.

The flags that had flown so proudly when they first stormed into the grand banquet hall now fluttered as uneasily as their hearts.

And at that very moment—

*Boom. Boom.*

The drumbeat rang out once again, reaching their ears.

Instinctively, every hair on their bodies stood on end. A chill ran down their spines.

The fourth drumbeat was no louder than the ones before it, nor did it have a deeper, more resonant ring.

But there was only one reason it made the rebels’ hearts sink more than ever.

Behind them.

The sound came not from Baek Yeon, visible in the distance, but from somewhere behind them.

And then it spread in every direction.

*Boom. Boom-boom.*

Countless drumbeats spread like flames sweeping across a wide plain. They weren’t echoes bouncing back from somewhere, nor were they hearing things.

They were the signal that this long and gruesome banquet was coming to an end—the footsteps of hunters closing in on prey at last caught in a trap.

*Rumble.*

How long had this been going on?

Where had such a vast army been hiding all this time, and why hadn’t it made a move until now?

*A trap!*

A shock struck them as if lightning had pierced their skulls. At the same time, the rebels felt the colossal tremors rapidly drawing closer.

Then they saw it.

Hundreds of flags rising high around them at last.

Following the fluttering flags, a dragon embroidered in golden thread writhed as though alive.

“……!”

“……!”

Unseen shock, joy, and despair swept across the grand banquet hall.

Some were seized by an elation so intense their hearts felt ready to burst. Others clenched their teeth until they tasted blood.

The three thousand rebels were the latter.

Thousands. Or tens of thousands.

No one could guess the exact number of their enemies, but one thing was certain.

Even now, the force of the enemy closing in around them would overwhelm them.

The rebels felt the killing intent bearing down on them.

Looking at their faces reflected in the rippling pools of blood, they imagined the ominous future about to descend.

But at the same time, they thought of the only way to break through this hopeless situation, surrounded on all sides.

The center and beginning and end of everything.

The ruler at the highest peak in this vast realm beneath the heavens.

“The Emperor…”

The faint voice that slipped from someone’s lips soon erupted into a massive shout, born of the desire to survive.

“Capture the Emperor!”

The victor is king; the loser, a rebel.

With their backs already against the cliff, they had no other choice.

A body without a head could not move.

Capturing the Emperor and his family to make the rebellion succeed was the only way forward.

“Whoever captures the Emperor and his family will become a marquis and enjoy wealth and glory for generations to come!”

At that moment—

*Rumble!*

Thousands of men and horses surged forward like a wave.

Toward the Emperor, who looked down at them from the high steps with his aged face.

And at the same time, trying to drown their fear of the woman standing tall in front of him with angry shouts.

“GRAAAAAH!”

“Charge! Don’t stop!”

Their cries, like screams, and the countless footsteps and thundering hooves woke the deep night. They rang out through the thick darkness hanging over everything like a curtain.

Far away. Farther still.

Loud and clear.

But their desperate advance and shouts seemed unbearably slow and distant.

At least, to the young man and woman facing each other at that moment.

He looked at her. She looked at him.

The more than three hundred yards between them meant nothing now.

They already knew.

They knew they were looking at each other. They knew whose gaze they had met in midair.

But only So Gyo had realized the other person’s true identity.

*So it was you.*

Swallowing a cryptic murmur, So Gyo silently looked down at the battlefield spread out beneath her.

It was vast. And it was horrific.

The grand banquet hall, stretching nearly a thousand yards in both length and breadth, was submerged in blood. Abandoned weapons and severed limbs lay scattered across the ground. The wide-open eyes of the dead held no trace of life.

Only death had filled the silence left behind when the music briefly fell quiet, and now more people were surging in to paint another layer of death over it.

*Whoosh.*

Amid the enemies’ thunderous shouts, a cold wind blew from somewhere, billowing her silky hair into a lush cloud.

The smell of blood, carried by the wind and seeping deep into her nose, was as thick as the crimson pools of blood collected all around her.

Thick enough to dredge up fragments of a past submerged by time.

Thick enough to revive the horrific memories she’d wanted to forget but never could.

Perhaps that was why she felt not even the slightest joy, despite having found the answer and key she had searched for so long.

Perhaps that was why she felt certain the time had come to end this long and gruesome banquet.

*Shhk.*

In the silence, So Gyo moved both hands. The two curved swords, clutched in hands caked with dried blood, pointed toward the sky and the earth. Then they turned to face each other.

*Shrring. Clack.*

The steel, forged through countless rounds of quenching and hammering by some master artisan, gave off a cold ring. An invisible groove and the metal set inside it joined the two weapons together.

As if they had been one from the beginning.

As if they had never been curved swords at all.

*Wooooong.*

After countless years, it had regained its original form. It trembled in its owner’s hands, resonating with the familiar energy seeping deep into it, and shed tears that resembled light.

*Zing.*

The air quivered.

Between the two ends, bent at an angle and shaped to call a curved sword to mind, a pure-white flash connected them.

Just as it had looked in the distant past.

Still bearing the splendor of an age when it had been divine punishment to some, salvation to others.

“Hello again, old friend.”

In a tender voice, So Gyo lifted her beloved weapon.

And, as she had done tens of thousands of times before, she gripped the flash joining its ends and pulled hard.

*Fwoosh.*

A brilliant shaft of light appeared as though traced in midair, set against the shining bowstring.

The unbelievable sight stirred the old memories of someone watching from afar. It raised someone’s figure from a past buried in dust.

A crone who had ruled the battlefield with a bow larger than any other, unleashing Force like lightning.

“The Bow Saint…!”

At that very moment—

*SHWAAAAAK!*

The beam of light left So Gyo’s—or rather, the Bow Saint’s—fingertips and streaked across the grand banquet hall.
## Chapter artifact 921

# Chapter 921

*Fwoosh!*

The moment they saw the streak of light hurtling across the open space, the three thousand rebels charging as one instinctively understood.

The only path they had thought could save them was where unavoidable death awaited.

“Dodge—!”

*KABOOOM!*

Someone’s scream was swallowed by the deafening roar. Amid the dust cloud that billowed up with the explosion, headless corpses and men and horses torn limb from limb shot into the air, spraying fountains of blood.

“GRAAAH!”

“S-spread out! Spread out at once and keep charging!”

“Don’t stop! Stop, and you’re dead!”

Urgent commands rang out over countless screams.

Overcome by fear and confusion, the rebels forced strength into their trembling legs at the direction of the command still coming from their surviving leaders.

That was right.

If they stopped here, it was all over.

The moment they climbed onto the back of a rampaging tiger, their fate had been sealed.

“AAAAAAH!”

“Charge! Chaaaarge!”

With bloodshot eyes and faces gone white as paper, the surviving rebels screamed in desperation and pressed forward.

Praying that the Force arrows that seemed liable to come flying from anywhere, at any moment, would spare them.

Using the unlucky men at the front as shields.

*Please, please!*

And as they continued their charge, an earnest plea circling endlessly between clenched teeth, a dazzling streak of light suddenly swept across their path.

No—it swept them away.

*BOOM! CRUNCH!*

The earth shook. The cloud of dust rising into the air turned red as it soaked up blood.

Yet the gaze of the person watching that horrific scene—and the hand that kept drawing the bowstring—remained terrifyingly calm.

*Four hundred paces.*

*Ziiing.*

The great bow shuddered. The string and arrow, glowing brilliantly with their owner’s internal energy, unleashed a speed and force no other archer could imitate.

Just as they did now.

*Thrum. Fwoosh!*

With another howling gale of light, the death already in store—and the screams that came with it—swept over the enemy. Every time an arrow made of Force flew, dozens of lives went out like candles in the wind.

*Three hundred paces.*

Again.

*Two hundred paces.*

Again.

*KABOOM! KABOOM!*

The closer they came, the higher the pile of corpses grew. The rebels at the front had changed several times over by now, and the men charging forward were howling like madmen.

The only path left to them—and the road to their graves.

They pressed on, pawns on a vast game board, until they faced the brilliant light that would be the last thing they ever saw.

*Crunch!*

How many had died by the time the four hundred paces between them had been cut in half?

And how many more would die before they covered the remaining two hundred?

No one could answer the question that suddenly crossed their minds.

Not those collapsing as they felt the life draining out of them. Not those who had to leave their fallen comrades behind and keep going.

Not even the leaders, who kept shouting for the charge while sending their own men ahead of them.

“We’re almost there! Whoever captures the Emperor will be made a marquis and—!”

*Poom!*

The cry cut off at the same time as a sharp crack through the air.

In the blink of an eye, the commander’s body shot off his saddle and slammed into a pool of blood.

*Splash.*

“Ugh!”

“G-General of the Swift Cavalry!”

No one heard the rest of what he said, but looking at the General of the Swift Cavalry lying motionless in the blood, no one could help thinking of death.

There was no question. He was dead.

The powerful military commander, who had held control over the army for many years, died just like that.

So suddenly and miserably, leaving behind one question.

*How?*

The leaders nearby were momentarily bewildered.

That terrifying streak of light, too powerful to seem like an arrow, had been nowhere to be seen a moment ago.

*Then who…?*

Just as they turned their heads to look for the unseen enemy, a low voice slipped into their ears.

“There’s something this old man’s curious about. What do you call the bastards who started this goddamn mess?”

Someone else answered.

“What else? They’re fucking assholes.”

“Then what about the ones hanging back even now?”

“Hmm. Shitheads?”

“And if they’re both?”

“In four-character idiom? Fucking dog-shitheads.”

“Fucking dog-shitheads, is it? That does roll right off the tongue.”

Not in front. Not behind. Not to either side.

The leaders, frozen like statues, slowly raised their heads.

And there they were—two people standing tall in midair above them.

At the same time, an ominous feeling came over them.

Maybe what they were seeing and hearing now would be the last thing in their lives.

“W-wait. If you help us now, we can give you whatever you want…”

*Whoosh.*

A breeze blew. That was all.

It should have been all.

Then why was their consciousness growing hazy?

There had been two people standing over them. Where had one of them gone?

“Y-you fucking…”

A voice squeezed out between someone’s lips.

*Shhk.*

Deep inside their bodies, death awoke late and stretched.

The faint red lines left by a spearhead that had flashed past too fast to see appeared across them.

*Slip. Fwoooosh!*

Blood, welling in soft beads, burst out like an explosion. Heads, arms, legs, bone, and flesh—defying their owners’ will—came apart and slid away.

The young man with the spear, not a drop of blood on it, stood beneath the falling bodies as they collapsed behind him.

*Thud-thud-thud!*

The young man, drenched by the red rain pouring from the dark sky, was Jin Taekyung.

He finally gave them his answer.

“Help you? The best help you bastards can offer is to just fucking die. You fucking dog-shitheads.”

“……!”

“……!”

Those who had witnessed the horrific, unbelievable sight before their eyes were struck with shock—and despair, as they realized it was all over.

Every one of them wore splendid clothes. They were powerful figures whose families had pledged loyalty to Dark Heaven and the Eastern Heaven Demon Lord for generations. They had crossed a river they could never return from.

*It’s over. Completely.*

Surrounded by hundreds of guards, Jin Taekyung stood with a calm expression, his spearhead hanging low. Jeok Cheongang still stood tall in the air.

Only then did they understand that their ominous premonition had come true.

This grand rebellion—and the wealth and glory they had enjoyed for so many years—was finished.

Their only consolation was that instead of suffering through brutal torture before being torn limb from limb by carts, they might be granted a quick death by that martial-world ruffian.

Or so they thought.

Until Jeok Cheongang spoke.

“Leave the ones who look like the top dogs alive. I don’t know if they’re a gold mine or a spent mine, but who knows what we’ll find if we dig? We should at least try a few swings of the pickaxe.”

“……!”

“……!”

It took no more than an instant for the shock and resignation in their eyes to turn into fear. At the end of that brief moment, ten sharp cracks through the air were waiting for them, unleashed by Jin Taekyung.

*Fwish-fwish-fwish!*

They weren’t given time to take out the poison pills they had kept hidden, just in case—or even a moment to draw the daggers at their waists and slash their own throats.

*Thud-thud-thud!*

They felt it.

Finger Qi racing through the air in an instant, stiffening their entire bodies. The world slowly tilting as deep despair weighed down on their minds and bodies.

*Slip. Thump!*

They fell like waterlogged logs. In their eyes, golden flags were already fluttering all around them.

Above the writhing dragons, countless arrowheads rained down, painting over the dark sky.

*Shhhhhhh.*

A steel rain poured from a thousand repeating-crossbow soldiers, covering the remaining rebels.

*Thud-thud-thud!*

The sounds of flesh being pierced announced the end of the blood-soaked banquet. Screams of pain joined them, mingling with the powerful, unceasing beat of drums.

Rich and sticky as blood.

*Boom. Boom. Booooom.*



* * *



Fifteen minutes.

That was how long it took for all three thousand rebels to be wiped out.

Along with a rain of arrows, the Imperial Army swept into the grand banquet hall with enough force to put an end to this long, horrific feast.

“Rebels, listen!”

“Rebels, listen!”

“Disarm and surrender at once!”

“Disarm and surrender at once!”

A powerful voice charged with internal energy rang out over and over.

The twin military officers, urging them to surrender with identical voices and intonations, as though one person were speaking, seemed to extinguish the surviving rebels’ last hope.

*Clunk. Clunk.*

*Clang.*

They loosened the joints of their bloodstained armor and dropped their cracked and broken weapons as if throwing them away.

No one knew who had begun the wave of surrender, but it soon swelled into a tide that swept through the grand banquet hall.

“I surrender. I’ll surrender.”

“Please, just spare my life…”

Eyes and faces that looked as if their souls had left them.

Some clutched their missing arm and begged for their lives. Others made an irreversible choice at the edge of a cliff, unable to take another step back.

*Stab.*

“Kh… Urgh!”

A body pitched forward with a muffled death rattle.

The nameless rebel crumpled without strength. Despair that everything was over mingled in his face with the faint peace he had found in escaping this hell.

“It’s over.”

At the faint words Jeok Cheongang murmured as if to himself, I forced myself to nod calmly.

Yeah. It was over.

This great battle, which had swallowed countless lives in plain sight and out of it, had finally come to an end.

But not everything was over.

The dead had gone somewhere far away, never to return. But the monster who was neither dead nor alive still remained here.

And there was still the matter of dealing with the living.

*Squish.*

Someone’s footsteps sank into a pool of blood.

Each light, graceful step left a sticky imprint in the blood—an unpleasant contrast to her delicate gait. I watched her approach, my gaze cold and steady.

So Gyo.

No—the Bow Saint.

The woman whose every detail had been shrouded in mystery.

At our first meeting, she had pretended to be the Emperor’s loyal servant. At our second, she had put on the mask of Dark Heaven. Only at our third meeting had she finally revealed herself.

She was coming toward me.

With the catlike steps that suited her name, So Gyo, she crossed the ground scattered with countless corpses—people who wouldn’t have had to die if she had revealed her identity a little sooner.

*Fwoooosh.*

Blade-sharp qi rose from every part of my body. The Bow Saint stopped a few steps away and looked at me in silence, then suddenly spoke.

“So it was you.”

What did she mean?

I hesitated, unable to understand the meaning behind her words. A low voice sounded in my ear.

*—The one the Martial God spoke of. The chosen one.*

…What?
## Chapter artifact 922

# Chapter 922

What made humans seem so special in a world teeming with countless living things was their ability to think deeply and broadly.

That was true of every human being.

They took in their current situation through their eyes and ears, thought about what to do or say to the person in front of them, and put together the right words.

At the same time, they predicted what would happen because of their words and actions.

But those predictions didn’t always come true.

When the situation around them took an unexpected turn, or the person they were talking to reacted in a way they hadn’t anticipated, humans were thrown off.

Their minds, spinning at full speed, came to a halt. They lost all sense of what to say.

Just like I was right now.

“So it was you.”

So Gyo—no, the Bow Saint—stared at me. Her lips moved, and a voice only I could hear slipped between them.

*—The one the Martial God spoke of. The chosen one.*

…What?

The shock of learning that So Gyo was the giant known as the Bow Saint had completely disappeared.

Those few words, transmitted like a hammer blow to the back of my head, left me blinking blankly.

I’d expected an excuse, at least.

I thought she’d explain that she hadn’t expected things to turn out this way, that she’d had no choice—especially since I wasn’t hiding my anger.

But she didn’t.

The Martial God.

And the chosen one.

As I froze like a statue at that utterly unexpected combination of words and their incomprehensible meaning, the Bow Saint’s Sound Transmission continued.

*—Yes, you must be confused. I was, too, a long time ago.*

A long time ago? Just when was she talking about?

What had the Martial God, who had vanished into the distant past, told her?

But the question that flashed through my mind was cut short before it could even take shape.

*—It’s a long story I’ve kept to myself. But this isn’t the best place to talk.*

I desperately wanted to press her for answers, but the Bow Saint’s Sound Transmission was enough to remind me of the situation I’d momentarily forgotten.

Right.

The massive bloodbath that had unfolded here today was over, but that didn’t mean everything was finished.

Just as a curtain call still follows when the curtain falls on a performance.

The actors on this blood-soaked stage still had parts to play.

*I’ll get my answers after that.*

I nodded. The Bow Saint understood what I meant and quietly turned away.

Her gaze flicked toward the one person who’d stood beside us all along, watching everything in silence.

“That old hag’s still the same. No, she’s even more irritating now that she’s gotten younger. Her eyes are worse than before.”

Jeok Cheongang muttered it under his breath, then added, “And playing games with some young punk through Sound Transmission right in front of me, too.”

“……”

“What? You think I wouldn’t notice?”

I peeled a crust of dried blood off my cheek and answered, “I figured you’d know. And even if you didn’t, I would’ve told you myself.”

“You sure know how to talk.”

“So, did you hear everything?”

“Do you take the title Bow Saint for the name of the dog next door?”

“Then I’ll tell you. Every last word. I won’t leave out a single syllable.”

Jeok Cheongang stared at me for a moment, then clicked his tongue.

“Forget it. There’s no rush. She must have had her reasons. Anyway…”

*Pat. Pat.*

His sturdy palm tapped my shoulder. Jeok Cheongang quickly turned his head away, and his gruff voice came from his profile.

“Uh, well. What I’m trying to say is… hmm.”

“Yes?”

“No, I mean. What this old man wants to say is… Hey, look at you. Are you laughing?”

At some point, a laugh must have slipped out of me.

But I didn’t hurriedly wipe the smile from my lips like I used to.

I knew how he felt. And he’d understand what I was feeling, too.

*Thank you. For coming back to me.*

That was what Jeok Cheongang had said just a little while ago, when I’d been hovering between life and death, after I finally clawed my way back from death and recovered.

And now it was my turn to say it back to him.

“Thank you. For always staying by my side.”

I murmured so quietly he could barely hear, then pretended to be distracted by something in the air.

It was a little embarrassing. And I wasn’t sure I could handle seeing his reaction.

But… well. Sometimes you just want to say something like that.

Even when you’re close enough that you don’t need long explanations, there are times when you simply want to speak from the heart.

And in that regard, at least, Jeok Cheongang was far clumsier than his immense martial prowess would suggest.

“Ahem. Ahem. What’s with that creepy stuff coming from a hairy bastard like you…”

He hesitated, clearing his throat for no good reason, then suddenly gave a quiet laugh. At the end of the direction his finger pointed, a group of people was rushing closer.

“This old man’s a given. Save your thanks for those guys. They threw themselves into a deathtrap just to save you. They deserve at least that much praise, don’t they?”

I turned my head. Familiar faces came into view, hurrying toward me with blood covering them from head to toe.

One, two, three… six.

Every one of them had survived. Not a single person was missing.

That was enough. More than enough.

*Ah.*

Was it the overwhelming relief? Or the exhaustion I’d forgotten about?

In an instant, all strength left my body. I staggered and began to fall.

No—I nearly fell.

If a flurry of hands hadn’t reached out from every side to catch me, I certainly would have.

*Grab.*

Jeok Cheongang, Hyuk Mujin, Ju Hwaran, Song Ilseom, Sama Pyo, Taishan, and the Divine Physician caught my arms and legs. They held up my body as it threatened to tip over.

Not like a heavy burden, but like sturdy pillars.

Every one of them had come back to this deathtrap, hoping they could help even a little. Each of them had become the greatest reason I had to win this horrific battle.

“Damn it. I should be lending a hand in this awesome moment, but this guy’s so tall I can’t even reach him.”

At the mournful remark from the old Hidden Shadow Pavilion agent perched on Taishan’s shoulder, everyone let out a quiet laugh.

Even I, who’d nearly closed my eyes against the sleep demon washing over me.

*No. Not yet.*

I clenched my teeth and forced strength back into my crumbling body. Then, ignoring the worried looks around me, I started walking.

To bring this hellish night to an end.

To finish off the monster who had created a hellscape no painter could ever depict.

*Clop. Clop.*

I walked, and kept walking.

Past the dead and the rebels, bound tight in thick iron chains and struggling to break free.

Looking toward the dozens of flags rising high into the air.

Until, at last, in that vast space where not a single protest or scream could be heard, I saw the monster writhing alone at the Bow Saint’s feet.

“Eastern Heaven Demon Lord.”

At my call, the monster’s movements stopped abruptly.

* * *

The moment Jin Taekyung’s low voice reached his ears, the Eastern Heaven Demon Lord felt all the strength leave his body.

Why?

He didn’t know.

Maybe it was because the man before him was Jin Taekyung—the one who had stood in his way at every turning point, every moment when the course of events might have changed.

Or maybe he’d been waiting for someone other than the Bow Saint, who had watched in silence all this time, to stop him.

To stop this meaningless struggle.

This hollow sense of defeat and fury, now that he could no longer achieve his goal.

“Yes, it’s you.”

A volcano that had spewed lava soon cooled. The Eastern Heaven Demon Lord was the same now.

“You’re late. It’s rude to keep someone waiting this long.”

Jin Taekyung looked down at him in silence, then spoke.

“Well, I don’t think that applies to an immortal monster like you.”

“A monster, is it? So that’s how it is?”

“Right. And to be precise, I’m not exactly big on manners even with people.”

“Ah. So you were born rude.”

“If you’d said that in front of my mom, she would’ve beaten you to death.”

“Didn’t you just call me a monster who wouldn’t die?”

“Mom’s Divine Palm hits your soul. Not your body.”

The Eastern Heaven Demon Lord let out a hearty laugh before he could stop himself.

“I think I know what you mean. That makes sense.”

Once, he’d had a mother, too.

She was gentle most of the time, but when he did something wrong, she’d scold him harshly and smack him on the back.

Even after all these long years, the pain of it still lingered faintly.

“Yes, I remember. I had times like that, too. My Master was usually gentle, too, but sometimes the switch would come out.”

But the more he recalled those happy memories from long ago, the fainter the smile on the Eastern Heaven Demon Lord’s lips became.

“But… now I can’t remember.”

Once, all of that had been the present.

It had been today, and yesterday.

But now, the only faces left in his memory were twisted hideously with pain. Only the sight of them dying, or already dead.

*“You bastards! You’ll be cursed for this!”*

*“Go! Hurry!”*

It was strange.

His mother’s piercing scream as the soldiers brutalized her while she fought to protect her only surviving child, and his Master’s final words—those memories were so vivid. So why were their smiling faces so faint?

Why were they all blurred, as if hidden in fog?

*Crack.*

The Eastern Heaven Demon Lord clenched his teeth so hard that his molars shattered.

But, naturally, the pain that should have followed never came.

Only the result remained: they were broken.

Just as the people around him had died screaming.

Just as he had chosen to become a monster instead of a human being.

“Do you know something?”

His lips, wet with blood, moved. His eyes, fixed on Jin Taekyung, the Bow Saint, and the countless people who had gathered around him, flickered with cold flames.

“This is only the beginning.”

He spat out the words.

Each syllable was filled with anger.

He swallowed his resentment toward the world—and his grief at knowing he could never be happy again.

“Even if you’ve protected the imperial capital, you can’t stop the fires spreading throughout the land.”

He had served the imperial family for more than half a century. There wasn’t a single person who hadn’t taken shelter beneath his vast shadow, and not one of them was beyond Dark Heaven’s reach.

The frogs who had escaped the vast well of the imperial capital had each received an official post and spread throughout the land. They’d put down new roots, growing branches and bearing fruit.

That was why the Eastern Heaven Demon Lord could smile.

Thinking of the Great Nation, soon to be swept up in a massive civil war and firestorm. Thinking of the Dark Heaven forces that would use those flames to march into the Central Plains.

“That day, the Great Nation will fall.”

The Eastern Heaven Demon Lord threw his head back and laughed.

He looked at the man standing before him, mocking the Emperor, who would feel helpless to do anything.
## Chapter artifact 923

# Chapter 923

How many people feel no fear in the face of death?

Very few.

No—none.

Of course, if you turned the whole world upside down and shook it out, you might find a few. But I can say with certainty that even among Murim warriors, whose guts are in a league of their own compared to ordinary people, there isn’t a madman like that.

After all, it’s only natural for someone who has lived their life to fear death.

Whether it’s a battle-hardened veteran who’s crossed the line between life and death countless times on brutal battlefields, or a green kid whose baby fat hasn’t even faded, everyone feels fear in the face of death.

All the more so when a full course of unspeakably horrific torture awaits you before death.

But there are exceptions to everything.

Like the Eastern Heaven Demon Lord, laughing loudly before the Emperor at this very moment.

“Ha! Hahahahaha!”

He was a wretched sight, sprawled on the ground with all four limbs gone.

But his laughter rang out like that of a victor.

Though the complete death he’d delayed once, or perhaps dozens of times, had finally come within reach, there wasn’t a trace of fear in the Eastern Heaven Demon Lord now.

Was it simply because his body couldn’t feel pain?

*No.*

Even if he’d been an ordinary human instead of a monster, he would have laughed just the same.

He would have cursed the imperial court and the Great Nation that had taken everything from him, and gladly accepted torture and death.

After all those distant years, the only emotion the Eastern Heaven Demon Lord had left was bitterness.

Self-reproach and regret that he hadn’t been able to complete his revenge with his own hands.

That was all.

The sole truth and outcome, with nothing to add or take away.

“It’s over. Completely.”

The meaning behind Jeok Cheongang’s muttering was clear.

No amount of sweet talk or kind gestures could get information out of the Eastern Heaven Demon Lord now.

Like a horse galloping across a wilderness without looking back, his path had been set long ago.

“I’ve seen eyes like that before. There’s no need to waste time. The only sensible thing is to cut off his breath now and eliminate the threat.”

He wasn’t speaking only to me.

Jeok Cheongang was speaking to everyone here.

It was the greatest respect he could show the people who had fought beside him on the same battlefield—and a proposal addressed to one man.

The ruler of this vast continent.

The Emperor.

“Your Majesty.”

Jeong Hogun, a Thousand Captain of the Embroidered Uniform Guard, stepped forward. Blood covered him from head to toe, and he held a sword broken in half.

“Please, give your command.”

But the Emperor didn’t answer.

He kept his lips pressed shut, gazing down at the Eastern Heaven Demon Lord with an exhausted face. Only after some time had passed did he speak.

“What do you think?”

At first, I didn’t know who he was asking.

But as the Emperor’s gaze settled squarely on me, and the people around us erupted as if a dam had burst, I understood.

At this very moment, the Emperor was asking me—not anyone else—what should be done with the Eastern Heaven Demon Lord.

“Y-Your Majesty!”

“You mustn’t!”

“How could Your Majesty, the sovereign of all under Heaven, ask an ordinary subject—one of those lawless ruffians from the martial world, no less—”

“Lawless ruffians from the martial world, you say.”

The Emperor muttered softly and looked around. Before I knew it, officials in full court dress had surrounded him on every side.

The Emperor turned his gaze from one face to the next. The Emperor and the Eastern Heaven Demon Lord had been so focused entirely on each other that many of these officials had survived. Then the Emperor continued, slowly.

“It is a strange thing. The martial-world ruffian you speak of fought desperately and ended up covered in blood, while you ministers of the court somehow look untouched after such a fierce battle.”

“……”

“……”

Silence fell in an instant.

The Emperor’s words shut everyone up. He turned his head toward me.

“Now answer me. I want to hear what you think.”

I didn’t know.

I didn’t know why, out of all these people, the Emperor had singled me out.

Or what answer he wanted from me.

But I didn’t dwell on it. As always, I could just say what I had to say.

“If I opposed killing him, would you let him live?”

A single, explosive question that no one had expected. I heard people around us catch their breath.

Even the Eastern Heaven Demon Lord stopped laughing and opened his eyes wide.

But the Emperor looked at me without wavering and answered.

“No.”

“Why not?”

I wasn’t asking because I truly didn’t know the answer to this outrageous question.

Everyone needed to know.

Even if no one outside the imperial palace ever learned the truth, the people here needed to hear it.

I believed the Emperor understood that much, too.

“He is a traitor without equal in all history. For many years, he blinded and deafened My Father, and used poison to slowly drive most of the imperial family—including My Crown Prince Brother—to their deaths.”

A ripple of shock spread through the crowd.

Everyone held their breath at the hidden history that had never been revealed.

As far as the world knew, the root of all evil was the Emperor himself.

“When I learned the truth, it was already too late. Traitors who sought to bring down the Great Nation had seized control of the imperial family and tightened their grip on most of the real power.”

Everyone here could imagine what had followed.

An Emperor reduced to a puppet. The princes already poisoned.

There was no more time, no more people for those born of a noble and great bloodline to rely on.

Except for one old general who had protected the Embroidered Uniform Guard with unwavering loyalty, and the Great Nation’s fourth prince, who was far from the throne and had been wandering the provinces.

“There was only one way left.”

And so came a restoration disguised as a rebellion.

More than a decade ago, right here in this grand banquet hall.

In a single night, several hundred high-ranking court officials died. Before long, tens of thousands more were exiled or executed.

And the fourth prince wielded the sword of purging without hesitation.

He climbed the bodies of the traitors who had tried to destroy the Great Nation, with the unseen glares and curses of its people at his back.

All the while, he swore that one day soon he would reveal the whole truth and wash away this disgrace.

“Then, the reason the late Emperor and the other members of the imperial family were confined…”

“We tried every way we could to cure them, but even the Imperial Physicians couldn’t determine the cause. They said there was a great physician who wandered the world like a cloud, driving away even the Grim Reaper. If we could find him, they said, there might be a way.”

“The Divine Physician.”

“Yes.”

The Emperor added bitterly to my mutter, spoken almost to myself.

“But in the end, I could never find him.”

I’d heard it directly from the Slaughter Saint, too.

The Slaughter Saint and the Divine Physician had wandered all across the land, treating the people. The people, never forgetting their kindness, had hidden them from the imperial court’s search.

*If the imperial court had found them then…*

History would have changed.

Even if the poison that cast its long shadow of death over the imperial family had been the Blood Soul Gu, the Slaughter Saint and the Divine Physician I knew might have found some way to deal with it.

But the cruel twist of fate ended with the deaths of the late Emperor, the crown princes, and several other members of the imperial family. The fourth prince, who had been far removed from the throne, became a usurper and a parricide in every sense.

“Why didn’t you reveal it? The whole truth?”

“It wasn’t that I didn’t reveal it. I couldn’t. At some point, everything I said and did amounted to nothing more than a usurper’s excuse. Only when My Father regained his senses at the very end and told Me he would abdicate in My favor did I finally understand the reality.”

It was a stain that could never be erased.

Even after the fourth prince had formally succeeded to the throne and become the ruler of all under Heaven, people turned their backs on a truth they couldn’t believe.

A usurper, blinded by ambition, who had dragged his father from the throne.

As if that weren’t enough, a murderer and parricide who had led countless families and members of the imperial clan to their deaths.

The traitors who had driven the Great Nation toward ruin became loyal patriots. Meanwhile, those who had tried to protect it had to wear the stench of filth.

And yet…

Even so, he had no choice but to keep moving forward.

He had to tear out this enormous weed that cast its shadow over the entire Great Nation.

“I took the capital and purged countless traitors, but the main root survived. That restoration was only half a success.”

The Eastern Heaven Demon Lord hadn’t been the monster he was now.

He’d fought against the Bow Saint and Baek Yeon, and suffered injuries so severe he could never recover. Then he proposed a deal.

A bargain: his life in exchange for the fate of the entire Great Nation.

“For Me… it was an offer I couldn’t refuse.”

The Emperor was the realm, and the capital was the heart of the realm.

But the Emperor and the capital weren’t all there was to the realm.

If the Eastern Heaven Demon Lord had been killed that day, the Great Nation would have split in two and plunged into a massive war.

With the country hanging by a thread, the only path the fourth prince could choose would have given those who had conspired with the Eastern Heaven Demon Lord long ago, and had waited for the right moment, another excuse to rebel.

“I had to stop that. I couldn’t let any more blood be spilled.”

He’d taken up the sword as soon as he could walk.

By the time the calluses on his hands felt natural and the reins were familiar to his touch, he was marching off to war.

Time and again, he’d led armies with outstanding martial skill and strategy, earning great victories. But whenever he went to the battlefield, he would murmur to himself:

*This will be the last war.*

*It has to be the last.*

The throne? Military honors as a general?

He didn’t need any of it.

He’d given up on those things long ago.

His brilliant, kind eldest brother had all the makings of a sage king. The only reason he’d taken part in dozens of great and small wars was that he wanted the new world his brother would rule to be peaceful.

That was all.

And yet. And yet…

“So this is how it ended.”

*Shing.*

The fourth prince—the Emperor—drew his sword.

Through the richly colored blade, not stained with a drop of blood despite having cut down countless dead, he looked at me and asked:

“Jin Taekyung of the Jin Family of Taiyuan. I ask you once more. Do I need any further reason to kill him?”

I answered.

“What you’ve told us is enough.”

He wasn’t the only one who had been waiting for the moment of revenge.

“Then that settles it.”

His answer was calm, but heat simmered beneath it. The Emperor brought his sword down.

Against the enemy of his family.

Against the traitor of all time, who had plunged his country and its people into misery.

Or rather, he was about to bring it down.

The Emperor’s treasured sword was moving with enough force to split the man in two when a clear young voice rang out.

“One thing is still missing.”

*Whoosh!*

A sharp sound cut through the air.

The Emperor stopped his sword just short of the Eastern Heaven Demon Lord’s throat. He, I, and everyone else turned our heads.

And saw him.

A boy in clothes stained here and there with blood, his eyes calm and sad.

Prince Shangshan, Zhu Bao.

Everyone was looking at the young prince, but the young prince was looking at only one person.

Even his small steps, with his growing years not yet behind him, carried him forward.

“Your Highness! Your Highness!”

Hong Jin, a face that hadn’t been visible until now, called after him in a panic. He must have gone to his master’s side as soon as the battle began. But Prince Shangshan didn’t stop walking.

*Step.*

One step.

*Step.*

Another.

No one could stop him.

At that moment, the boy reflected in everyone’s eyes was a man.

Not a young prince, but another ruler.

And the man, the ruler, slowly bowed his head.

Toward a man who hadn’t been able to cast off all his fury, even in the face of death.

Toward the enemy who had killed his parents and brothers.

*Swish.*

The hem of his clothes brushed against a pool of blood. Prince Shangshan bent deeply toward the Eastern Heaven Demon Lord and spoke.

“I’m sorry. I know this won’t comfort you, but… I sincerely apologize for what my grandfather did.”

“……”

“……”

Everyone was left speechless.

Me, the Emperor, the Bow Saint, and the Fire King.

Even the Eastern Heaven Demon Lord.

“Ah.”

A quiet groan slipped between his parted lips.

He stared at Prince Shangshan with trembling eyes, then gave a faint smile.

“What a damnable thing.”

*Thud!*

The blade that had been resting against his skin pierced his throat.
## Chapter artifact 924

# Chapter 924

*Thud.*

There was no resistance. Nothing to stop it.

The imperial family’s treasured sword split the flesh and bone it touched as easily as tofu, doing its job faithfully, regardless of its master’s wishes.

“……!”

“……!”

Silence fell over the entire place in an instant.

No one here had expected this.

Who could have imagined that a vengeful ghost who had devoted his entire life to bringing down the accursed imperial court and the Great Nation would choose this path?

That he would thrust his own neck onto the blade held out by his enemy’s descendant?

And yet, even so, a fate twisted once did not easily grant him death.

*Grrk. Cough.*

Blood and phlegm bubbled through the gaping wound in his throat. Gasping for breath, the Eastern Heaven Demon Lord felt his body slowly, little by little, beginning to recover. A rasping laugh escaped him.

It was absurd.

He had made himself a monster to stay alive, and now he was struggling to die.

The very power he had once considered a blessing had become a curse, binding him in its grasp.

*What kind of farce is this?*

The Eastern Heaven Demon Lord gazed up at the sky and laughed emptily.

He resented the body that wouldn’t die, no matter how much he wanted to.

He didn’t want to meet the Emperor’s gaze, or Jin Taekyung’s as he looked down at him with those inscrutable eyes.

And…

He didn’t have the courage to face the boy who was still bowing deeply to him, a child no more than a scrap of blood.

No. He was ashamed.

“Twelve years. It was twelve years ago.”

*Cough.*

Spitting out the froth of blood that welled up in his throat, the Eastern Heaven Demon Lord slowly continued.

“I watched from a distance as a little child, still too young to be weaned, left the imperial palace in the arms of a eunuch.”

The eunuch’s name was Hong Jin. The child’s name was Zhu Bao.

“I wanted to kill him. More than once, even after that.”

But he hadn’t.

It wasn’t only because Prince Shangshan Zhu Bao would one day make the perfect puppet—someone to depose the Emperor and fill the vacant throne.

The Eastern Heaven Demon Lord had vaguely suspected that the Emperor’s decision to make his youngest brother Prince Shangshan and send him far away was a kind of deception. And still, he had never given the order to assassinate him.

He hadn’t even known why he agonized over it so much.

No. He had known, but pretended he didn’t.

“That child… reminded me of myself.”

In the little boy who had lost his parents and siblings, in that small child being carried out of the palace as if in flight, the Eastern Heaven Demon Lord had seen his own past.

The messenger pigeon arrived at regular intervals, bringing news. In those few lines of writing, he could read the child’s loneliness.

“They said that far away, more than ten thousand li from here, the five-year-old cried every night. His sobs were so loud they could be heard over the walls.”

By misfortune or good fortune, the child was precocious. In the year he turned five, he learned the truth.

That he was far more special than other people—and perhaps just as unfortunate.

That other children his age didn’t call their mothers wet nurses.

“Time passed quickly. They said that when the child turned seven, he stopped crying. Instead, he grew lively, practicing martial arts day and night.”

But the Eastern Heaven Demon Lord knew.

In those few short lines of the missive, he could still find the child who was crying.

“That child… had only learned how to hold back his tears. Just as I once did.”

Something he didn’t want to get used to.

But had no choice but to get used to.

And so the child held back his tears. Every night, he buried his face in his blanket and cried silently, out of sight of the eunuch and wet nurse who cared for him so devotedly.

He was afraid they would be sad if they heard him crying.

Afraid his sobs would carry over the walls and rob him of his dignity as a prince.

Seven years old.

The child had grown up, and faced reality.

Far earlier than anyone had wished.

“That was when I finally understood. I could no longer kill him.”

After that, time flowed on like a river.

The Eastern Heaven Demon Lord, unable to recover from the injuries he had suffered at the hands of the Bow Saint, performed his sect’s forbidden ritual and turned himself into a jiangshi. Meanwhile, the child, whose days had always been much the same, met a young man.

Jin Taekyung.

The Third Young Master of the Jin Family of Taiyuan.

A wastrel who had only just taken his first step toward turning his life around.

And this unimpressive young master of an unremarkable martial family gave the boy something he had never had in his life.

A dream.

“‘Dreams come true.’ That’s what it said, wasn’t it?”

When the Eastern Heaven Demon Lord read that in the missive, he laughed despite himself.

The cheek of that young punk, spouting such nonsense to a prince, was amusing, even if he was only a child. And the boy’s decision to turn that punk’s nonsense into a plaque and hang it in his residence was funny, too.

At the same time, he felt a pang of bitterness.

He, too, had once had a clear, shining dream.

The child’s dream would never come true as long as he was alive.

“But even then, I found myself wondering. What was the dream that child wished for, deep in his heart? What goal did he want to achieve?”

The Eastern Heaven Demon Lord slowly turned his head.

He saw the boy still bowed low, trembling faintly. Tears had filled the boy’s eyes at some point, and he couldn’t bring himself to straighten up and show them.

“Now I want to hear the answer. From that child, who must be thirteen by now.”

Twelve years had passed.

The child had become a boy, and the old man had become a monster.

And now, in this very moment, the boy—Prince Shangshan Zhu Bao—steadied himself with effort.

“My dream…”

Slowly straightening his deeply bowed back, he gave voice to the dream he had kept in his heart.

“To ensure that no one else ever suffers the misfortune that you and I had to endure.”

“……!”

The Eastern Heaven Demon Lord’s pupils trembled.

No—everyone here felt the same.

“That… will be impossible.”

“That’s why it’s a dream.”

“Do you intend to simply wish for something you know you can’t achieve?”

“It’s a dream because I won’t give up, even so. Because I’ll keep trying, and struggle with all my might to make it come true.”

“Do you understand what it is you’re talking about?”

Facing the Eastern Heaven Demon Lord, who could no longer hide his agitation, Prince Shangshan spoke quietly.

“An age of peace and prosperity.”

It was a four-character phrase that had been the wish of all the people since time immemorial, and had always betrayed them.

And yet, a boy of only thirteen was speaking of it.

He was telling them he, at least, wouldn’t betray them. That he would usher in a new age like the reigns of Yao and Shun, when everyone lived in peace and happiness.

He spoke with all his heart.

“I will punish the wicked and reward the good, regardless of their station.”

That was righteousness.

“I will always watch over and cherish the people, and listen carefully to the counsel of those around me.”

That was humanity, and justice.

“I will respect all my people. I will look beyond their birth and accept their goodness and wisdom.”

That was propriety and wisdom.

“And I will sow no seeds of misfortune. Whatever consequences that choice brings, I will bear them and take responsibility for them.”

“Ah.”

The Eastern Heaven Demon Lord groaned.

The meaning behind the young prince’s final words—the two characters for *mercy*—cut into his heart like a blade.

“I… I couldn’t forgive anything. At some point, I began cursing everything.”

At the end of a brutal age of turmoil, the warlords who had caused him to lose his family had turned to dust and disappeared.

Taizu, who had burned his sect to the ground and slaughtered his Master and fellow disciples, was dead too.

But the Eastern Heaven Demon Lord—and his thirst for revenge—remained.

No, it had only burned more fiercely.

Against those who remained. Against people who were completely innocent.

“But how… how can you…!”

Unable to bring himself to look straight at the boy, the Eastern Heaven Demon Lord closed his eyes and cried out, his voice boiling over.

It wasn’t anger like before.

He was simply more anguished than ever.

Even now, he couldn’t let go of everything.

And he was ashamed.

The boy before him was offering him the forgiveness he had never managed to achieve in his entire life, cradled in his small hands.

“You know something?”

At the sudden voice, the Eastern Heaven Demon Lord opened his eyes.

Prince Shangshan was looking at him with trembling eyes.

“Today, when I learned the whole truth, I wanted to kill you more than anyone.”

“Then why…?”

“Because I felt sorry for you. I realized what made us different: something that came to me like good fortune, but was never given to you.”

Prince Shangshan slowly turned his head. A man stood beside him, looking haggard but entirely at ease, as if there were nowhere else he could be. The young prince’s gaze fell on him.

“I had a subject who was closer to me than family.”

His name was Hong Jin. From the prince’s earliest memories to this very moment, he had always been by his side.

“And I had an elder brother and loyal subjects who endured countless humiliations for the sake of this country.”

The Emperor closed his eyes with a low groan.

The loyal old general and the Embroidered Uniform Guards, who had been forced to seize the throne to confront a greater injustice, clenched their teeth, trying to suppress their agitation.

“When there was not a glimmer of light to be seen, there were people who offered me a hand without asking for anything in return.”

The martial artists of Murim.

People who had stepped outside the Great Nation’s laws and drawn a boundary around their own world.

And yet they had willingly crossed that boundary and rushed into a deadly place full of danger.

Prince Shangshan’s gaze passed from one to the next. One awkwardly scratched his bald head. Another gave him a gentle nod. One was rubbing his stomach as if he were hungry.

And at the end of his gaze stood one man.

He wasn’t the strongest or the wisest among them. Even so, he stood at the center of them all as naturally as if he belonged there.

The young man who had planted a dream in someone’s heart and promised to be his friend was smiling at the boy who had grown so brilliantly.

So bright and warm that, for an instant, even the Eastern Heaven Demon Lord thought the world before his eyes had grown brighter.

*Chivalry.*

He had forgotten that single word for so long that it felt strange. The Eastern Heaven Demon Lord turned it over in his empty heart.

Then, reflected in the young prince’s tear-filled eyes, he saw his own warped, blurred face—the face of a monster.

“The man I saw in you was not only a sinner of the ages, burdened with unforgivable karma. You were also an unfortunate person who had no choice but to walk a different path from mine.”

Unfortunate, he had chosen revenge instead of forgiveness.

Inhuman, he had become a monster.

He had believed revenge was the only path. That was what had made the Eastern Heaven Demon Lord live as a human being, then as a monster.

But he had been wrong.

About his goal. About his reason.

“Now… you can stop.”

At that quiet murmur, which pierced his ears, the Eastern Heaven Demon Lord’s body stiffened.

*You can stop now.*

*It’s all right to stop.*

Those plain words melted the heart of someone who had spent so many years burning to ashes, only to freeze solid again.

At last, they brought him peace.

*So that was how it was.*

The Eastern Heaven Demon Lord gazed silently up at the sky.

He had resented it endlessly.

The sky. The whole world.

But when he let go of the last layer of anger that had hung over his heart, he saw a new world.

Countless stars glittered in the sky that had once been filled with nothing but darkness. The wind blowing from somewhere carried the scent of grass.

It mingled with the thick stench of blood rising from the hellscape he had created.

*It’s too late. I understood far too late.*

Thousands upon thousands of people had already been killed or wounded.

And how many more would be sacrificed because of his choices?

He couldn’t even begin to guess.

Nor could he measure the weight of the crime he would bear for the countless lives swallowed up in the great war he had set in motion.

But as he reached the end, a new fork in the road appeared before the Eastern Heaven Demon Lord, whispering insistently for him to make the better choice—even if only by a little.

A choice that could make his whole life, painted black, seem like nothing.

*—Listen carefully to what I’m about to tell you.*

*Whoosh.*

The Sound Transmission slipped between his moving lips and rode the wind.

It passed the young prince and the Emperor, crossed the Embroidered Uniform Guards and the assembled ministers, and reached one man.

Jin Taekyung.

“……!”

The Eastern Heaven Demon Lord gave a bitter smile at the sight of him staring down in surprise, eyes wide.

It was far too late. But at the very end, he had made a slightly better choice.

That was all.

*—I’ve told you my story. Now it’s time to collect my fortune-telling fee.*

Jin Taekyung watched the Eastern Heaven Demon Lord in silence, his gaze sunk deep. Then he nodded and stepped forward.

*Splash.*

Ripples spread across a pool of thick, sticky blood.

Everyone watching knew what Jin Taekyung was about to do. Still, not one of the ministers stopped him.

No—they couldn’t.

The Emperor and Prince Shangshan Zhu Bao had personally stepped aside to clear the way.

At this moment, Jin Taekyung was the Emperor’s appointed proxy, granted the authority to execute this great traitor on the Son of Heaven’s behalf.

*Shing.*

A cold breeze brushed against the spearhead, held in a reverse grip. Watching the blue-white flames slowly gather at its tip, the Eastern Heaven Demon Lord suddenly spoke.

“Do you think someone like me will be given an afterlife?”

“Probably. But you’ll have to spend about three thousand jiazi as a cockroach or a mosquito first.”

“I see. I suppose so.”

At Jin Taekyung’s matter-of-fact answer, the Eastern Heaven Demon Lord let out a dry laugh. Jin Taekyung continued in an even voice.

“But in your next life, make sure you’re born human again.”

“What do you mean…?”

“You never know. Maybe someone will help you then, unlike in this life.”

“……!”

“If we get the chance, let’s meet again then. Just don’t wait too long.”

The Eastern Heaven Demon Lord—or rather, Wei Zhong—fell silent.

Then, at last, he gave a faint smile.

Without a word, he watched the dazzling flames that filled his vision.

*Whoosh.*

That warmth, strangely enough, wrapped around his entire body.

# Checkpoint Review — 960–964

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

# Chapters 960–964

## Plot

At Eight Spring Gorge, Jin Mukyung, Wipeng, and Cheol Mubaek fight the Demon Bird, also known as the Blood Soul Fat Demon. Mukyung’s strike, Blue Wave, Falling Bird, cuts through the Demon Bird’s Force and kills him, bringing Mukyung to Supreme Peak. Though badly injured, Mukyung keeps fighting. Wipeng and Cheol, gravely wounded, urge him to flee, but he refuses to abandon them. His next strike kills ten Keshik squad leaders.

Jamukha arrives with thousands of reinforcements, turning the battle against Shanxi’s exhausted defenders. Jin Wikyung entrusts Lee Seowol with the aftermath and stays to fight. Jamukha offers to spare Mukyung and the others if Mukyung submits and becomes his hunting dog. Mukyung refuses. Horns then announce an enemy attack; the tremor came from another approaching force, whose identity is unknown.

## Continuity

- Jin Mukyung killed the Demon Bird and reached Supreme Peak. He remains severely injured; Wipeng and Cheol Mubaek are gravely wounded.
- Mukyung’s named strike, Blue Wave, Falling Bird, killed ten Keshik squad leaders. He refused Jamukha’s offer of submission.
- Jamukha’s reinforcements have turned the battle against Shanxi. Jin Wikyung has chosen to stay and fight after entrusting Lee Seowol with what follows; Wikyung’s fate is unresolved.
- An enemy attack has been signaled by horns. The force that caused the tremor, and how the confrontation with Jamukha will unfold, remain unknown.
- The Emperor remains gravely ill with Blood Soul Gu; saving him requires him to die once, and Taekyung’s treatment remains unresolved.
- Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung. The improved Temporary Strength Pill’s source, effects, and distribution remain unknown.
- The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown. The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.
- Taekyung resolved to trust his allies rather than bear every burden alone.

## Translation Decisions

- Render 혈혼비마 as “Blood Soul Fat Demon” and 권호 as “Fist Hero.”
- Keep “Blue Wave, Falling Bird” for 청파낙조.
- The Demon Bird mistook Wipeng and Cheol Mubaek’s Water God Dragon bone weapons for Ten-Thousand-Year Cold Iron; preserve the distinction.

## Durable state

{
  "active_continuity": [
    "Jin Wikyung has entrusted Lee Seowol with the battle’s aftermath and chosen to remain in the fight; his fate is unknown.",
    "Jin Mukyung refused Jamukha’s offer to spare him and the others in exchange for submission.",
    "An enemy attack has been signaled by horns; the force that caused the tremor is unidentified.",
    "Jin Mukyung killed the Demon Bird at Eight Spring Gorge and remains severely injured; Cheol Mubaek and Wipeng are gravely wounded.",
    "The Emperor remains gravely ill with Blood Soul Gu; saving him requires him to die once, and Taekyung’s treatment remains unresolved.",
    "Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung; the improved Temporary Strength Pill’s source, effects, and distribution remain unknown.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.",
    "Taekyung resolved to trust his allies rather than bear every burden alone."
  ],
  "continuity_sources": [
    964,
    963
  ],
  "open_questions": [
    "Who is the approaching enemy force, and how will the battle and Mukyung’s confrontation with Jamukha unfold?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain?",
    "What will become of Jin Wikyung?"
  ],
  "safe_through": 964,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 960

# Chapter 960

The time it takes to drink a cup of tea.

Though only that much time had passed, the Demon Bird couldn’t help but admit it.

He had underestimated the prey before him—or rather, the people of Shanxi.

“Loose!”

*Fwish-fwish-fwish-fwish!*

Holding back the cliff wasn’t the end of it.

Five earthen fortifications stood near the entrance to the gorge.

Their ramparts of earth and rock were still incomplete, but a considerable number of archers waited behind them. At a sharp cry, a rain of arrows poured down over the heads of the people who had been crowding together into a single mass.

More precisely, it fell on the steppe forces that had been surging without pause toward the gorge’s passage.

*Fwoosh! Thud-thud-thud!*

“Aaagh!”

“M-my eye! My eye!”

Screams and blood erupted all around.

Nomads struck in vital spots writhed in pain.

After several coordinated volleys flowed one after another like water, gaps opened in the once-dense formation. The people of Shanxi, led by the Jin Family of Taiyuan, drove into them like awls.

“Attack!”

“Waaaaah!”

Those trying to break through and those trying to stop them.

Two waves of people surged toward one another. At the point where they collided, there was no white sea foam—only red blood waiting for them.

*Clang! Krrrunch!*

*Thwack!*

Steel clashed against steel, sending sparks into the air.

A nomad’s sharp lance pierced a government soldier through the chest. A martial artist of the Jin Family of Taiyuan leaped over the man’s limp body and cut the nomad’s throat.

*Shhk!*

“Ghk—cough!”

Screams and groans spilled from every direction.

Everyone killed and died without pause.

At this moment, on this battlefield, there was no mercy or compassion to be found in anyone.

The strong devoured the weak.

A place where the weak could never survive.

That was the battlefield. And at the center of this terrible slaughter, the Demon Bird felt a pleasure he hadn’t known in decades.

“Yes! More! Give me more!”

Laughing loudly, he swung the two swords in his hands.

Just as he had in the days when nothing could stand in his way.

He remembered his past, when he had freely taken the lives of his enemies and bathed in their blood during the great war called the Great Faction War.

*Shwaaa!*

The wind split apart. Force surged from the long and short swords, cleaving through the air as it raced toward the most delectable prey.

“Scatter!”

*Whoosh!*

It happened almost at the same time.

Jin Mukyung, at the head of the line, shouted like a thunderclap.

As his cry rang out, the Tiger of Mount Heng, Cheol Mubaek, and the Ghost Sword, Wipeng, twisted their bodies aside.

And then—

*Shhk!*

The red Force barely missed them and swept away the unlucky men standing near its target.

*Fwoooosh!*

There were no screams. Only severed bodies and fountains of blood remained.

Someone’s scream of terror was the only clue to the fate of the thirty or so government soldiers and martial artists.

In the blink of an eye.

With one swing, dozens of lives vanished.

No—they were erased.

As if they had never existed at all.

As if that had been their natural fate from the beginning.

*So this is a Supreme Peak master…!*

Wipeng and Cheol Mubaek felt a chill run down their spines before they knew it.

Peak and Supreme Peak.

Only a single character separated the two, but the wall between those realms was immeasurably high and vast.

About half a year ago—

If another Supreme Peak master hadn’t unexpectedly become a retainer of the Jin Family of Taiyuan, they might have lost the will to fight just from seeing that attack.

*But even that Senior, who was so powerful, was ultimately defeated by that monster.*

That was true even considering that the Dongting Fisherman had only recently recovered enough to leave his sickbed.

The two men had received the Dongting Fisherman’s instruction over the past several months. They knew better than anyone how strong he was.

They knew how great a fortuitous encounter it had been to hear a few words from a master of his caliber and take part in the training bouts he held so often.

The Dongting Fisherman had always been grateful to the Jin Family brothers for stopping him when he had gone on a rampage and helping him recover. Thanks to the goodwill he had shown them, the Jin Family of Taiyuan’s strength had grown by leaps and bounds.

And yet he had died.

At the hands of one man.

No—at the hands of a monster who hardly seemed human.

And the monster who had chewed up and swallowed the old fisherman now opened his jaws toward the new prey charging at him.

Even now.

*Whish.*

With a faint sound, the air split.

The instant a red flash flickered in the darkness, Wipeng and Cheol Mubaek twisted their bodies with all their strength.

*Pipip!*

Hot.

Though they had dodged the attack by a mere handspan, the pressure had been enough to split the skin at the back of their necks.

But that sudden, stinging pain cooled their muddled thoughts.

*This is…*

Wipeng and Cheol Mubaek’s eyes, briefly wide with surprise, quickly settled into a steady gaze.

Their evasion hadn’t been a simple coincidence or an instinctive movement.

It was the result of everything they’d gained through their training bouts with the Dongting Fisherman—their senses, their techniques, and all the rest—coming together.

And half of those countless bouts over the past few months had been fought by the two of them together.

*We can do this.*

Now they could tell just from looking into each other’s eyes.

Their gazes crossed in the air for an instant, and Wipeng and Cheol Mubaek blurred at the same time.

*Fwap!*

They shot off in opposite directions. In the blood-soaked chaos, they vaulted over friend and foe, each swinging blades at one another, and raced along the steep rock face.

They put everything they had into dodging the monster’s Force, which was faster and stronger than the Dongting Fisherman’s.

*Shhk! KABOOM!*

The solid cliff face, formed over what must have been hundreds of years, split like tofu. The tremendous energy that seeped into it tore everything around it to shreds, but Wipeng and Cheol Mubaek didn’t stop.

No—they couldn’t stop.

If they failed to defeat the enemy before them, everything would be over.

If they retreated out of fear, or hesitated over the large and small wounds multiplying as the distance between them closed, they wouldn’t be able to face the young man charging ahead of them.

*Second Young Master.*

*Heaven Shaking Sword.*

At this very moment, Wipeng and Cheol Mubaek could see him clearly.

Jin Mukyung, charging toward the enemy without hesitation amid the endless shower of Force.

His sturdy back and legs showed no hint of wavering, though flecks of blood scattered around him.

They suddenly wondered how he had spent those two years before finally emerging from that lightless darkness into the world.

How the other genius, who had briefly been overshadowed by Jin Taekyung and Cheongpung, had passed that time.

And then, at last, they saw it.

*Hssss.*

Moonlight slid along the white blade.

No—a massive Sword Energy shone even brighter than Wipeng’s and Cheol Mubaek’s.

*Whish.*

In a world that seemed to have slowed down,

the blue Sword Energy swept down at an angle and met the Demon Bird’s red Force.

* * *

*KABOOOOM!*

It was an explosion that brought everyone’s hands and feet to a halt in an instant—and a shockwave that shook the gorge.

For someone standing at the center of the blast, it also brought joy and astonishment.

*Rumble.*

“Ha! Hahahahaha!”

Beyond the fragments of rock scattering in every direction and the cloud of dust rising thick in the air, the Demon Bird laughed like a madman and thrust out his hand like a thunderbolt.

*Boom!*

The compressed air burst, clearing the view. Jin Mukyung stood at the far end of a deep furrow stretching a full *jang*. The Demon Bird bared his yellow teeth.

“Well, well! What a brazen little brat!”

Powerful killing intent mingled with delight. The two swords in his hands trembled—but not just because of what he was feeling.

*Tap.*

The Demon Bird already knew what the firm sensation against his heel was.

A rock.

A fragment of stone that had been three steps behind him just moments ago, but now touched his heel.

The distinctive firmness and chill he felt through his leather shoe, soaked in blood, were the greatest reason for his smile.

“I can’t even remember the last time I backed down from someone.”

That was right.

The rock hadn’t come to him.

The Demon Bird had retreated.

No—he had been forced back.

By a mere brat who wasn’t even thirty, against an old monster who had lived a life steeped in blood, from the Great Faction War to the present.

Though the distance of three steps and a *jang* was considerable, it meant nothing to the Demon Bird. He had seen it clearly.

Just before the two different streams of Sword Energy and Force met, the beautiful path traced by the brat’s fingertips.

That light, as blue as the sea.

“Ah, so that’s it.”

*Squelch.*

The Demon Bird stepped forward slowly, his foot sinking into a pool of blood.

The blood overflowed around his heavy step, befitting his immense frame.

“I always found it strange. Why your face kept appearing before me, even though I never saw you once while fighting that old man, the Dongting Fisherman.”

A few days ago, alongside news of the vanguard’s annihilation, a messenger had brought him the severed head of a Keshik commander of a hundred. On it, he’d seen the Sword Demon’s handiwork.

“The moment I first saw it, I became interested. The work was that perfect.”

Everything leaves a trace.

Beasts, people, and martial arts.

Every death has its own cause—and that is all the more true of Murim martial artists.

Looking at the chillingly smooth cut across the severed neck, the Demon Bird felt the blood that had been cold for decades begin to boil.

Was it because he’d found traces of a divine art said to have disappeared long ago?

Or because he’d sensed a skill to rival his own?

No.

The Demon Bird had only now realized why he hadn’t been able to get the Sword Demon out of his mind, even while facing a Supreme Peak master like the Dongting Fisherman.

“One Strike.”

A strike without a single wasted movement, no matter how many hundreds or thousands of times you watched it.

Truly dazzling. Beautiful, even.

A perfect strike in every sense.

That single movement.

The young Sword Demon before him possessed it.

He didn’t have internal energy accumulated over several *jiazi*, nor had he mastered a divine art that could look down on all the world.

It was simply colorless and odorless.

And that made it more lethal than anything else.

Like the Formless Ultimate Poison, which swallowed a person’s life before they could do anything about it.

Like an assassin who crept through the darkness and cut a man’s throat.

“Amazing. No—extraordinary.”

Along with his heartfelt exclamation, the Demon Bird’s eyes held a trace of regret and sorrow as he looked at Jin Mukyung.

“Why? Why did I have to meet someone like you now?”

*Ptooey.*

Jin Mukyung spat out a clot of dark red blood and answered in an even voice.

“Even if I’d met you much earlier, there’s no way I’d have called a mangy pig like you my Master.”

Wipeng and Cheol Mubaek approached with him, moving to surround the Demon Bird. He let out a regretful sigh.

*Why? Why did it have to be now?*

If they had met a year—or even three years—later, they could have had a match so good it would have made his whole body tremble with joy.

But Jin Mukyung had only a half-collapsed wall ahead of him.

Still…

That moment of joy would never come again.

Jin Mukyung wouldn’t survive this place today.

“What a shame. Truly.”

*Hssss.*

Red light rose from the Demon Bird’s entire body.
## Chapter artifact 961

# Chapter 961

The moment he saw the faint blood-red glow rising through the darkness, the Tiger of Mount Heng, Cheol Mubaek, finally understood the identity of the obese old man who had introduced himself with the unfamiliar title Demon Bird.

“Blood Soul Fat Demon.”

At the words, which slipped from Cheol Mubaek’s lips like a groan, the Demon Bird’s face twisted.

“How does a brat like you know…?”

Cheol Mubaek would turn sixty in a few years, but in the Demon Bird’s eyes, even a veteran like him was no more than a green young pup.

At that moment, though, what bothered the Demon Bird most was hearing that old title again after so long.

Blood Soul Fat Demon.

He had earned it because he considered murder a form of hunting and, among the countless fiends, was unusually obsessed with death and blood. The title had always carried a note of mockery, too.

Fat.

That single word always got under the Demon Bird’s skin. He had never been one to deny his feelings or instincts.

“It’s been a long time since I heard that damned title. I’ve killed so many people over the years that now, even when they recognize me, plenty of them pretend they don’t.”

He had killed the execution squads sent by the orthodox faction, the unorthodox rabble who’d bowed and scraped to curry favor with him, and even the fiends he’d once been fairly close to.

The reason was simple.

They’d said the title that made his blood boil just to hear.

Why else would he have given himself the title Demon Bird, a name that didn’t suit his appearance at all?

And now a green young pup with the unheard-of title Tiger of Mount Heng had dredged up those unpleasant memories he’d buried away.

*How dare you.*

His fate was all but sealed.

The Demon Bird wrote Cheol Mubaek’s name at the top of the list of people he intended to kill, then spoke.

“A brat like you couldn’t possibly have met me before… So who was your master?”

Crack.

Cheol Mubaek clenched both fists and replied.

“Fist Hero.”[^1]

“Fist Hero?”

The Demon Bird had been approaching at an unhurried pace, but now he stopped.

He hadn’t expected much when he asked.

He had spent his life killing people, over and over. Once the count passed a thousand, he stopped keeping track. There was no point in remembering them all.

But Fist Hero was still a title that remained vivid in his memory.

More so because he was one of the few who had survived a life-and-death duel with the Demon Bird.

“What a coincidence. You’re the Fist Hero’s Disciple? Wait—he raised a successor with that body?”

The Demon Bird forgot his anger and burst out laughing. Cheol Mubaek answered in a cold voice.

“Don’t insult my master. He was a far greater man than you could ever be.”

“Of course he was. Even after his life as a fist master was over, he still managed to raise a Disciple. I’ll give him credit for his grit. You should’ve seen his face when I cut off both his arms.”

“……!”

“Now that I take another look, this really is quite the lavish feast. The young Sword Demon of the Jin Family of Taiyuan—and the successor of the Shura Annihilating Fist.”

As the Demon Bird’s satisfied gaze swept over them, Wipeng spat.

“Can’t see me, either?”

“Of course I can. I can already picture your corpse lying dead in front of me in a moment.”

“You have to see how long or short it is before you can tell.”

“That’s the kind of bullshit weaklings say.”

Thud.

With each step, the old man’s heavy, wrinkled flesh rippled.

His sharp eyes looked completely at odds with his massive frame as he sized up the three men.

“Well, then…”

*Whoosh.*

“Who should I kill first?”

In a single step, the Demon Bird closed a distance of several *jang*. Two swords swept in arcs from his hands.

Like a bird with blood-red claws.

*Whoooosh!*

* * *

*Shhk—KRRRUNCH!*

A gale howled.

Mighty pressure swallowed the air and tore at their skin. Dirt and shards of rock blasted outward with a roar.

—Second Young Master!

Wipeng’s Sound Transmission pierced Jin Mukyung’s ears.

As Mukyung retreated again and again to avoid the Demon Bird’s Force, he suddenly jerked his head aside.

*Whoom.*

Two razor-sharp streams of wind skimmed past the back of his neck.

The two Keshik holding crescent-shaped sabers clicked their tongues in disappointment as Mukyung dodged their ambush, as if he’d been expecting it.

And that was the last anyone saw of them alive.

*Shhk!*

By the time a blood-red flash flickered, it was already over.

The Keshik fell quietly, never knowing how—or why—they had died.

Behind their headless bodies stood the one who could have explained it, radiating an enormous killing intent.

“You dare try to steal my prey?”

*CRUNCH!*

Blood Soul Fat Demon. Or the Demon Bird.

The old man’s massive frame didn’t suit his title. He angrily trampled the fallen Keshik’s bodies.

At that very moment, he seemed to have forgotten the other prey rushing at him from behind.

Or perhaps he didn’t think they were worth noticing.

“You bastard!”

The Tiger of Mount Heng, Cheol Mubaek.

A Disciple of the great fist master who had lost both arms to a fiend long ago, he had become a protector of the Mount Heng Sword Sect to help a friend’s only daughter. With a roar, he threw a single punch.

*Whoooooom—BANG!*

Compressed air exploded. Fist Energy shot from his spinning fist and engulfed his master’s killer.

Or at least, that was what it looked like for that one moment.

*Fwoosh!*

A long sword, stained a reddish hue like its owner, sliced through space.

The Fist Energy, which had seemed ready to turn everything in its path to ash, faded and scattered without force. A sneer touched the Demon Bird’s lips.

“You’re certainly no match for your master. I’m not even sure that’s the Shura Annihilating Fist I knew.”

But even the Demon Bird knew the truth.

Two hundred years ago, the Shura Annihilating Fist had ranked among the ten greatest fist and foot arts in the world. And Cheol Mubaek’s current realm wasn’t all that far below the Fist Hero’s, either.

It wasn’t the Shura Annihilating Fist or Cheol Mubaek who fell short.

The Demon Bird had simply grown stronger.

“Come!”

The Demon Bird felt the blood in his whole body boil.

The two swords in his hands had never felt lighter. The movements of his prey looked clear—and slow.

As if he could see a future that had yet to happen, he raised his blade toward a flash thrusting diagonally from his blind spot.

*KABOOM!*

The thunderous impact was far too loud to have come from two swords simply clashing.

Wipeng groaned as the tremendous recoil sent him flying. The Demon Bird shot his massive frame toward him.

*One first.*

As water flowed from high to low and people grew old and died, everything in the world had its own destined end.

To the Demon Bird, Wipeng’s death was just such a thing.

A Peak master who had achieved an impressive realm for his age.

An outstanding swordsman whose practical sword technique justified the title Ghost Sword.

But to the Demon Bird, that was all Wipeng was.

With enough effort and luck, perhaps he would reach Supreme Peak within a dozen years or so. But that day would never come.

Meeting the Demon Bird in this gorge today was proof that Heaven had already abandoned him.

Those who had yet to cross the wall—and those who had.

That was the difference between Peak and Supreme Peak.

*Become a ghost. Live up to your title.*

With blood-red light flashing, the Demon Bird swung both swords.

The short sword in his left hand went for Cheol Mubaek, rushing to save his comrade. The long sword in his right went for Wipeng, who was meeting him with all his strength.

But the clash that followed unfolded in a way the Demon Bird had never expected.

*CRUNCH—KRRRRANG!*

“……!”

A substantial recoil traveled up both sword blades.

The Demon Bird’s eyes widened as he watched the dazzling sparks bloom from three different streams of energy clashing together.

*What?*

The shock of what he felt was greater than he’d imagined.

Cheol Mubaek and Wipeng.

Those two young pups who hadn’t crossed the wall—prey who should have been no more than a meal—had stopped his strike.

They were holding their ground against the Sword Force he’d unleashed with all his strength, using nothing more than their puny Fist Energy and Sword Energy.

*How is this possible?*

The Demon Bird was a born killer and hunter.

That was why he knew better than anyone that his prey were far behind him—not only in their insight into martial arts, but also in the internal energy they held within their bodies.

And yet the impossible was happening right before his eyes.

A mere Peak master had met head-on the Force he’d swung with several *jiazi* of internal energy. It was something that couldn’t happen—and shouldn’t.

*Cough. Spurt.*

Blood mixed with bits of their innards poured from Cheol Mubaek’s and Wipeng’s split lips.

The Demon Bird stared, frozen with shock. Cheol Mubaek and Wipeng bared their bloodied teeth and smiled.

They were only barely holding out against the blood-red Force. Their snow-white gauntlets and sword blades trembled under its overwhelming might.

Behind them, the Demon Bird saw the faint glow coming from the two martial artists’ beloved weapons, which even the thick blood hadn’t been able to conceal. Only then did he recall something he’d briefly forgotten.

Force was not the only thing capable of standing up to a Supreme Peak master’s Force.

*Ten-Thousand-Year Cold Iron…!*

The Demon Bird swallowed at the unexpected truth.

How could he have known?

Even he, who had lived through so many long years, had never obtained a divine weapon like this. And yet such weapons were in the hands of two Peak masters from remote Shanxi Province.

At the same time, he could never have guessed the truth: that the weapons he now mistook for Ten-Thousand-Year Cold Iron were made from the bones of a spiritual creature that had guarded a river unseen for hundreds of years.

And the opening he’d left by revealing his surprise was nothing less than an opportunity for someone who hadn’t fallen yet.

*Hup!*

Wipeng summoned every last bit of his strength and twisted his sword.

His wrist was already broken, his hand mangled. But he swallowed the blood rising from his severe Internal Injury and redirected the energy bearing down on him, turning it aside.

*KRRRRUNCH!*

The long sword slid down the snow-white blade and drove into the ground.

As deep as the force behind it had been.

*Thud!*

The Demon Bird’s eyes blazed with anger as he came out of his shock—at that very instant—

*CRUNCH!*

Cheol Mubaek seized the short sword that had been slowly forcing his gauntlet back, gripping the Force shrouding its short blade.

*Crack. Krrrunch.*

A chilling sound of rupture, followed by unbearable pain.

Under the irresistible force, the flesh beneath his gauntlets was crushed and his bones splintered.

If he hadn’t had a divine weapon made from the Water God Dragon’s bones, both hands would have vanished without a trace the moment they touched the Force.

But Cheol Mubaek didn’t let go.

He couldn’t even groan through the indescribable pain. His internal organs twisted, unable to bear the immense energy, yet he clung to the blade with all his strength.

He remembered the great master who had taught him long ago, even without his arms.

And he waited for someone to kill the bastard in his stead, doing what he, an unworthy Disciple, could not.

At last, that wish reached another man’s sword.

*Shwaash.*

A faint, chilling sound as it cut through the air.

Like a bolt of lightning, a flash shot forward and descended toward the Demon Bird.

[^1]: Literally, “Fist Hero,” his master’s sobriquet.
## Chapter artifact 962

# Chapter 962

In that brief instant, split into ever smaller fragments, the Demon Bird realized that he had only one choice left.

*Shwaa.*

A faint whistle of displaced air reached him like a ghost, brushing softly against his ear.

At the same time, the world slowed.

Everything was clear.

The faint breaths of Wipeng and Cheol Mubaek, both suffering severe Internal Injuries. The drops of blood spilling from between their lips.

And then the Demon Bird finally released the two beloved swords he had been gripping tightly and turned around.

He kicked off the ground with all his strength, thrusting both palms forward like a bolt of lightning.

*Fwoosh!*

A flash of blood-red Force curled around his hands.

The tremendous energy, enough to reduce even a boulder weighing ten thousand *geun* to dust in an instant, surged forward without resistance.

Toward the sea-blue Sword Energy falling over the Demon Bird’s head.

Toward the man who had brought that blade-sharp wave of Sword Energy crashing down.

Jin Mukyung.

The eyes of the young Sword Demon of the Jin Family of Taiyuan and the old fiend who had spent his life piling up countless killings met in midair.

The two men couldn’t have been less alike.

Not in the lives they had led, the eras they had been born into, or the ideals they held in their hearts.

The young man had learned martial arts simply because he loved the sword. The old man had wielded one to kill.

The young man had wanted strength so he could raise his declining family back up.

The old man had craved strength because the stronger he became, the more people he could trample underfoot.

The young man was one of the countless people who wanted no part of an age of chaos. The old man longed more than anyone for those days gone by, when rivers of blood flowed and corpses piled up like mountains.

The paths they had walked, and the directions they had to go from here, were different.

Even the sounds of the Sword Energy and palm force they sent at each other in this very moment were different.

*Shhk.*

The Sword Energy fell like a blue wave—or a single bolt of lightning. It was as faint as a child’s breath.

*RROOOAR!*

The enormous blood-red palm force roared like thunder.

And between those small differences lay a gulf as deep and wide as everything that had come before.

One of them crushed the wind. The other cut through it.

*Gooooom.*

A distant flash. Air seething with heat.

Watching the two different lights—one red, one blue—race toward each other, the Demon Bird suddenly thought:

Supreme Peak and Peak.

The walls between the insights known as Sword Energy Becoming Force and the level of injuring others with Sword Energy might not have been as high and imposing as he had once believed.

*This is…*

Even amid the raging gale, the Demon Bird looked at the blue light shining clearly.

That unwavering strike, descending at an angle along its destined path, was proof of all the enlightenment the young man had gained so far—and of his progress toward a new realm.

*Rumble.*

At last, the two enormous forces met and erased the wind.

They warped space.

And under that tremendous pressure, enough to tear his whole body apart, Jin Mukyung closed his eyes.

A deep night, when even the moonlight was dim.

With his sight cut off, pitch-black darkness settled over him.

It was so familiar. Every bit of energy and sensation in his body surged and flowed into the sword in his hand.

He couldn’t see a thing, but he could feel it.

The opponent’s overwhelming power, ready to sweep everything away.

The gaps in his ferocious, but therefore unstable, palm force.

*Yes.*

*There.*

As if entranced, Jin Mukyung swept his sword down. Blue light slipped between his calmly closed eyelids, clearer than ever.

A thousand times, ten thousand times—or dozens, hundreds of times more.

Strike and cool it beyond counting, and even worthless scrap iron will one day become a fine sword.

A single drop of water from somewhere can crack a solid rock. A single thorn in an elephant’s foot can bring it down.

Just as it was now.

*Shwaaaash.*

The Demon Bird saw it clearly.

A blue flash, so sharp it looked like a single thread, split his palm force from side to side. It was unbelievable.

And at the same time, he marveled.

*Ah.*

Speed, power, trajectory.

Every part of it was dazzling. Perfect enough to make his skin crawl.

The divine weapon’s flash—no longer sharpness that could be called Sword Energy—cut through the blood-red Force and pressed onward.

*Truly beautiful.*

With that one word, left unspoken, the Demon Bird smiled brightly.

Then he reached out both trembling hands toward the blue streak of light falling over his head.

*Shhk.*

That beautiful, dazzling wave was cold enough to make him shudder.

* * *

The world stopped.

No—in truth, everyone stopped moving.

The nomads kept fighting, not daring to interfere in the battle of their superior, who was practically a tyrant. The Shanxi defenders, gradually tiring against the endless waves of enemy troops.

Not even Cheol Mubaek and Wipeng were spared. They had watched everything from closer than anyone else on the battlefield, barely managing to hold on to their fading consciousness.

*Shhk.*

The single, unusually clear slicing sound from moments ago still rang in their ears.

Along with a question they couldn’t understand.

*What on earth…?*

*What just happened?*

The same thought had crossed everyone’s mind.

Red and blue light had flashed within a distant, swelling blaze of light. That was all.

Everyone on the battlefield had seen that dazzling light clearly, and at the same time, no one had seen a thing.

At that moment, only the two men standing with a *jang* between them, their backs to each other, could break the silence that had settled over the narrow gorge, thick with blood and corpses.

Jin Mukyung and the Demon Bird.

The Demon Bird and Jin Mukyung.

The old fiend, who had spent a lifetime accumulating countless killings, and the young Sword Demon, who had spent the past two years swinging a sword in pitch-black darkness, slowly turned to face each other.

*Splash.*

With a heavy step, a pool of blood—no one knew whose—overflowed onto the ground.

And soon, fresh blood from someone filled the space it had left.

*Cough.*

His lips, clenched with all their strength, parted.

Like a cracked dam giving way, a spurt of blood mixed with pieces of his innards burst through that tiny gap.

*Splaaash!*

Dark red liquid painted the air and soaked the ground. Reflected in the pool of blood, now filled again, was the pale face of the young Sword Demon.

—No! Mukyung!

*CLANG!*

Along with someone’s desperate cry from far away, the clamor of steel began to ring out again.

Thinking of the familiar voice behind that cry, Jin Mukyung smiled faintly. The Demon Bird suddenly spoke to him.

“What was that strike?”

It was far too short to contain all the feelings and questions he had.

Jin Mukyung swallowed another surge of blood and answered.

“I don’t know, either. It was the first time.”

The Demon Bird let out a dry laugh.

It wasn’t mockery. Those who stepped into a new realm in a state of selflessness, forgetting even themselves, always gave the same answer.

He had, when he was young, too.

“Honest, at least.”

“Can’t help it. It’s the truth.”

“If only I could see that strike of yours one more time. Just once, before the end.”

“I’ll pass. I’ve had more than enough of your face.”

The smile on the Demon Bird’s lips grew wider.

“Have you named that form?”

Jin Mukyung quietly shook his head.

What he had trained in was martial arts, and at the same time, in a sense, it wasn’t.

Only One Strike.

He had spent two years searching for a single path for his sword, and today, in this place, he had glimpsed its very edge.

He had never even considered giving it the name of a form.

Not until the old monster in front of him spoke.

“Blue Wave, Falling Bird.”

A blue wave surges, and a bird falls.

Murmuring as if reciting a line of poetry, the Demon Bird asked Jin Mukyung with a self-satisfied air:

“Well? Pretty good, isn’t it?”

“Hard to say. It’s kind of cheesy.”

“Oh.”

Disappointment spread across the Demon Bird’s face. Then Jin Mukyung continued, his voice calm.

“But I guess it might grow on me.”

“Really? I knew you’d see it my way.”

The Demon Bird grinned from ear to ear.

He had no idea that faint red lines were beginning to appear all over his body.

No—he was making an effort to pretend he hadn’t noticed.

“Heaven Shaking Sword, Jin Mukyung. Of the Jin Family of Taiyuan… Cough, you young Sword Demon.”

*Drip. Drip.*

Blood fell in scattered drops.

The Shanxi defenders rushing to save Jin Mukyung, and the steppe fighters who had been holding them back with high morale, certain of their superior’s victory, stared at the Demon Bird with wide eyes.

At the old fiend who steadied his swaying frame and kept his eyes fixed on Jin Mukyung alone.

“Kill them. Kill them, and kill them again.”

His eyes and voice burned with the obsession he had held onto all his life: the desire for nothing but murder.

“With that strike you used to cut me down. Anything that stands in your way—every last one. Guh… Every last one…!”

*Slith.*

But the Demon Bird’s words never reached their end.

The red lines crossing his body, and the beads of blood swelling along them, finally burst in a magnificent explosion.

*FWOOSH!*

A fountain of blood surged upward, staining the air.

Everyone’s eyes widened in shock as the Demon Bird collapsed like a rotten tree.

One man fallen, one man still standing.

It was clear who had won and who had lost.

Looking down at the corpse sprawled face-first in the pool of blood he had made, his upper body and both arms severed, Jin Mukyung spoke in a low voice.

He returned the very words the Demon Bird had said before the battle began.

“When you get to the afterlife, tell them a man from Shanxi killed you.”

Then, gripping the hilt that felt heavier than ever, he cut off his enemy’s head without hesitation and raised it for all to see.

*Shhk.*

“I am Jin Mukyung of the Jin Family of Taiyuan! I have slain the Blood Soul Fat Demon!”

“……!”

“……!”

His powerful shout, backed by the little internal energy he had left, froze the air in the gorge.

Jamukha’s personal guard, already well aware of the Demon Bird’s identity, was stunned by his end. The Shanxi defenders stared wide-eyed at the title of the fiend who had stained the world with blood long ago.

The Demon Bird’s death.

And, at the same time, a new Supreme Peak master.

“Waaaaah!”

A tremendous roar shook the gorge. The Shanxi defenders, their blood boiling like lava bursting forth, charged forward, heedless of their lives.

They looked ready to swallow the personal guard, still frozen by the unexpected turn of events, and the nomads in the rear, bewildered by the connection between their Great Chieftain Chinggen and the Blood Soul Fat Demon.

“Attack!”

“We are Shanxi! We will not fall!”

“Wipe out every barbarian who dared invade this land!”

“Loose!”

*Shh-shh-shh-shshsh!*

Beneath a downpour of arrows, thousands of martial artists and government troops, led by Jin Wikyung with his eyes red and bloodshot, drove like a wedge into the broken enemy line.

“They’re coming!”

“Shields! Sh—!”

*Puhpuhpuk! KRRUNCH!*

The blood mist, briefly settled, rose thickly again.

The Shanxi defenders, their morale at its peak as the tide turned in an instant, charged forward, risking their lives.

They swung their weapons with every last ounce of strength, and endured the pain, biting at their enemies until their final breath.

*Shhk! CRUNCH!*

For every one they cut down, two took their place. For every two, three.

And there would be no next time. Only death remained.

*CRUNCH!*

Seven out of every ten Keshik were First Rate warriors. They were, without question, the finest troops on the grasslands. Yet in no time at all, the roughly three hundred men deployed in the gorge had been cut in half.

“What do we do? What are we supposed to do now?”

The Keshik squad leader didn’t answer his subordinate’s desperate shout.

No—he couldn’t.

The three commanders of a hundred were dead. So was the Demon Bird, another absolute master on a level with Jamukha.

And that wasn’t all.

Even now, his men were dying to blades flying at them from every direction.

And at the center of it all was a ghost, staggering as he drank in blood without end.

*Shhk. Shhk!*

He brings the sword down, cuts, thrusts.

With those simple movements, Jin Mukyung felled twenty Keshik.

Despite his clearly severe Internal Injury, the Sword Demon of the Jin Family of Taiyuan stood in the middle of the gorge, protecting his two companions.

*What is this…?*

The Keshik squad leader squeezed his eyes shut.

Then, after a brief hesitation, he gave the order to retreat.

Or, more precisely, he was about to.

Until he heard the familiar sound that rang out behind him.

*Boooooo!*

The squad leader knew what it meant.

That great sound, blown from dozens of horns at once, was meant for only one man.

Jamukha.

The great Khan, the supreme ruler of the grasslands.
## Chapter artifact 963

# Chapter 963

*Boooooo!*

Listening to the meaningless horn echo through the night, Jin Mukyung suddenly wondered:

Was it his will or his instinct that was moving his body right now?

*Shhk!*

A flash swept through the air.

Another enemy fell beneath the sword that scattered light as it swung.

The movements carved into his whole body through countless repetitions still traced their paths with precision, even as he staggered and bled.

*Shhk, thud!*

He dodged a thrusting spear from behind, then drove the sword in his reverse grip between the enemy’s ribs.

“Guh!”

The death rattle reached his ears.

Jin Mukyung pulled his sword from the chest of the enemy who had let out the stifled groan.

Leaving the crumpling corpse behind, he raced off to find another target. His eyes were—impossibly—calmly closed.

And yet…

*It’s all so clear.*

He could feel everything, even without sight.

No—with his eyes closed, everything around him seemed all the more vivid.

Darkness.

He had spent two years in that pitch-black darkness, where not a single ray of light could seep in.

He had to swing his sword to grow stronger—and sometimes, to keep himself from going mad.

As his sight dulled, his other senses had sharpened beyond measure. That meant his Qi Sense had improved by leaps and bounds.

“K-kill him!”

“He’s only one man! If we take him down…!”

*Crunch!*

A grisly sound of flesh being torn cut off the shout. Amid the endless carnage, Jin Mukyung took down yet another enemy—he had lost count of how many—and steadied his ragged breathing.

He was dizzy.

His body was as heavy as waterlogged cotton, and his mind was hazy, as if he were dreaming.

The fierce battle against the Demon Bird had given him more than a moment of enlightenment.

A severe Internal Injury.

His innards and acupoints were twisted and torn, their cries of pain seeming to ring in his ears.

Of course, Jin Mukyung knew it, too.

Defeating the Demon Bird had been close to a stroke of heavenly luck.

Cheol Mubaek and Wipeng had helped him, heedless of their own lives. He had landed a perfect strike—one he might never be able to perform again.

And finally, there had been a divine weapon capable of standing up to Force.

If even one of those three things had gone differently, the man standing here now would have been the Demon Bird, not Jin Mukyung.

But…

*Damn it.*

Nothing came without a price.

Jin Mukyung swallowed the blood surging into his mouth and caught his breath.

He tightened his grip on the hilt, which kept slipping from his grasp, and felt the enemies surrounding him with every sense. They breathed in fear and rage.

Beyond the ceaseless shouts and screams, he also heard someone’s faint voice.

“Hurry. Go on.”

Jin Mukyung already knew who owned that hoarse, elderly voice.

“I’m not going. No—I can’t go.”

Jin Mukyung opened his eyes. Through his vision, stained red with blood running down his forehead, he saw Cheol Mubaek and Wipeng gasping on one knee.

“We’re going back. All of us.”

At Jin Mukyung’s firm reply, Wipeng let out a hearty laugh.

“See? What did I tell you? Jin Family people are stubborn as hell, hu—”

He broke off, coughing up blood that pattered onto the ground. Jin Mukyung’s gaze sank as he watched.

The severity of coughing up blood depended on its color and what came with it.

By that measure, Wipeng’s condition was so dire that it was a miracle he hadn’t lost consciousness.

“Damn it. I’ve coughed up bucketfuls of blood, and now all I can manage is a handful.”

He tried to sound casual, but Wipeng himself knew how dire things were. He forced open his eyes, which kept wanting to close, and looked at Jin Mukyung.

“Second Young Master. May I say one thing?”

“No. Don’t say anything more. Save your strength as much as you can—”

“Mukyung.”

“……!”

Wipeng smiled at Jin Mukyung, who had gone rigid in an instant, showing his teeth stained with blood.

“Go. Stop being so stubborn.”

“……”

“I know it, Great Hero Cheol here knows it, and you know it yourself. What the best choice is.”

Jin Mukyung clenched his teeth.

“It’s not too late. We can still go back.”

“Yes. We can go back.”

Wipeng added gently:

“If you go alone.”

“What are you—!”

“Leave before it’s too late. You can still break through and make your escape.”

It had been the right choice to push deep into enemy territory and fight there, to minimize the casualties among their allies. But it had also been a bitter mistake.

Even now, hundreds of enemies surrounded them, waiting for a chance to strike.

Wipeng and Cheol Mubaek saw that cruel reality clearly.

The old tiger who had once commanded Mount Heng, and the Peak swordsman with his ghostly swordplay, were gone.

The tiger’s claws were broken, and the Ghost Sword’s art had disappeared along with his shattered arm.

That was the price they had accepted to tie down, for just one moment, the hand of a fiend who had once shaken an entire age.

But…

“You, Mukyung—you, of all people, have to live.”

“It’s not because you’re the Second Young Master of the Jin Family of Taiyuan.”

Wipeng and Cheol Mubaek looked at Jin Mukyung through eyes that seemed ready to go dark at any moment.

The young man reflected in their eyes now was not Jin Mukyung.

He was the hope they had to save, even if it cost them their lives—the very revenge that would one day come back at their enemies tenfold, a hundredfold.

“Live. Survive, no matter what.”

“And come back. To us—and to them.”

Spring. Summer. Fall. Winter.

The seasons passed in an unchanging cycle. In all that time, only people disappeared.

That was why Wipeng believed. Cheol Mubaek was certain.

The winter that had come early for them today would one day come for their enemies, too.

The young Sword Demon of the Jin Family of Taiyuan, who would protect countless people in the years to come, would bring them down.

“So…”

Wipeng looked at Jin Mukyung with a faint smile.

He remembered the young man back when he was a boy, coming to ask him to teach him the sword.

“Leave this place right now. Jin Mukyung—no, Commander of the Heaven Shaking Squad.”

“……!”

“This is an order from your senior in the family.”

Jin Mukyung was struck speechless. He squeezed his eyes shut.

He knew.

What the best choice was. What he had to do to save more people.

But his feet wouldn’t move.

Because Jin Mukyung still remembered the lesson he had learned alongside martial arts when he first picked up a sword.

*Chivalry.*

Suppress the strong and help the weak.

Never turn away from injustice, and uphold one’s word as dearly as one’s life.

That was what it meant to be a chivalrous hero. It was the way of life a martial artist of the orthodox faction, one who stood for what was right, was supposed to follow.

He had learned martial arts because he loved the sword, because he wanted to grow stronger. But he had never forgotten the weight and meaning behind those two words.

*What is the best choice?*

Wipeng and Cheol Mubaek had said it, and Jin Mukyung had endlessly repeated it in his heart even as he cut down his enemies.

And then, suddenly, Jin Mukyung understood.

“You’re both wrong.”

*Shhk.*

He opened his eyes. His toes pressed into the blood-soaked earth.

The tip of his sword, which had trembled with fatigue and doubt, now pointed at the enemy without the slightest wavering.

“Before thinking about what’s best or worst, there’s one thing you mustn’t forget.”

*Shhk, shhk!*

A nomad who had approached cautiously was cut diagonally in half. Blood trickled down the white blade that had sliced through his body and the thrusting spear with it.

“What is right?”

Jin Mukyung moved like flowing water. Blue Sword Energy, faint moments before, rippled along his sword, now slowly steeped in his moment of enlightenment.

*Shwaaash!*

A thick blood mist bloomed. Jin Mukyung cut down three Keshik with one stroke, then snatched the crescent saber from the hand of a corpse and flung it.

“What choice will I have no regrets about?”

*Whoosh! Thud!*

A single streak of light cut through the air. At its end, death came without even a scream.

The death of the one stringing a bow on his composite bow became the signal. The enemies packed tightly around them erupted with pent-up fear and rage, charging all at once.

*Shhk-shhk-shhk!*

*Fwoosh! CLANG!*

Flashes glinted in the darkness.

Jin Mukyung knocked away the throwing blades, but a dozen thrusting spears and crescent sabers came down on him.

*Pit, pit!*

It was hot. Blood droplets mingled with the wind whipping past.

He knew he could avoid them, but his body refused. The places all over his body where blades had grazed him burned with pain.

No—perhaps it was the disappointment and anger he felt toward himself.

The shame of having thought, even for a brief moment, about what was best instead of what was right.

*This is the only right choice.*

His muddled thoughts cleared. Jin Mukyung clenched his teeth with all his might.

*Crack.*

The stench of blood filled his mouth.

One pain drove out another. His fading consciousness returned.

And at the same time—

*Tsutsutsu.*

The blue Sword Energy, rippling like small waves, came together as one.

Following the will of the swordsman holding it, it joined, blended, and finally became one, tracing a beautiful arc.

An arc so perfect that the old fiend, now among the dead, would have laughed out loud if he had seen it.

*Shwaaaash.*

The wind disappeared. A chill cleaved through the darkness.

The ten Keshik squad leaders charging toward Jin Mukyung opened their eyes wide as if on cue.

And at last, they understood.

What the Demon Bird had seen in his final moments.

What the monster with such overwhelming martial prowess had felt.

*Shing.*

The thrusting spears, shining with tangible energy, groaned. So did the crescent sabers.

As the energy in each weapon faded away, the ten Peak martial artists watched fragments of their beloved weapons fall to pieces. They felt their vision tilt.

“S-Sword Demon…”

*Fwoosh!*

A dense fountain of blood stained the air.

Beneath the sticky blood pouring down like a shower, Jin Mukyung had felled ten birds with a single strike, like a blue wave. He murmured softly.

“I’ll keep that promise.”

*Blue Wave, Falling Bird.*

Remembering the old fiend who had become the first prey of that once-nameless strike, Jin Mukyung stepped toward the frozen enemies.

And at that very moment—

“May I ask who you made that promise to?”

“……!”

Jin Mukyung’s whole body went rigid.

The owner of the unfamiliar voice that had suddenly spoken stood only about ten feet away, looking at him.

“You…”

“Jamukha Khan!”

Someone shouted. No—the call erupted from every direction, all at once, drowning out Jin Mukyung’s voice.

*Jamukha.*

Unlike the voice, the name was familiar.

The words spoken by the strongest nomad warrior as he died—the day Jin Mukyung annihilated the thousand-man vanguard that had invaded Shanxi Province ahead of the main force—were still vivid in his mind.

*He will punish you—Jamukha Khan will. He’ll take everything from you and burn it: your family, your friends, your home.*

And now, as Jin Mukyung finally faced Jamukha, he understood.

There hadn’t been even the slightest exaggeration in those words, which were little more than a curse.

“So it’s you. The one they call the Sword Demon.”

Jamukha.

The supreme ruler of the grasslands took a step toward Jin Mukyung.

*Rrrumble.*

A small but unmistakable tremor traveled through everyone’s feet.
## Chapter artifact 964

# Chapter 964

*Rrrumble.*

Ripples spread across the pool of blood that had lain still.

Tiny fragments of stone trembled. So did the countless corpses, eyes wide open in death.

*This is…*

Everyone felt the tremor, small but unmistakable.

And at the same time, they knew instinctively what it meant.

An earthquake?

Ridiculous.

This tremor was undeniable proof that at least several thousand men and horses were closing in on them.

The cruel omen was enough to give some people hope, and others utter despair.

“Waaaaah!”

*Wheeeee!*

The gorge filled with shouts.

The nomads, whose morale had plummeted at the Demon Bird’s death, let out shrill cries and charged.

“Reinforcements!”

“Khan Jamukha has arrived!”

If Jin Mukyung’s defeat of the Demon Bird had turned the tide of battle, now the reverse was happening.

Jamukha.

A name unfamiliar even to the people of Shanxi. The ruler of the western grasslands, the undisputed master of the vast Great Steppe. And now, at least several thousand reinforcements had joined him.

The nomads’ morale, which had been sinking as steadily as a dying ember while they were pushed back, soared. The Shanxi defenders, who had been driving back the invaders moments ago, felt the fatigue and fear they had forgotten return to them.

Even the man leading them felt it.

*What do I do now? What am I supposed to do?*

Jin Wikyung swallowed a groan.

As if to prove how fierce the battle had been, blood from his enemies ran down his sword, the weapon of the commander in chief.

He had fought with everything he had.

He had joined the fighting himself to raise his men’s spirits. Whenever a crisis arose, he had given flawless orders, sealing the gorge entrance so thoroughly that not even a drop of water could pass.

Fifteen thousand troops, scraped together from across Shanxi Province.

But reality was cold.

Less than half of those fifteen thousand could be called the main force, and even they had suffered heavy losses fighting the enemies who kept pouring in.

For every enemy they felled, there were two. For every two, five.

For every five, ten.

And behind them, tens of thousands more still waited.

In this long, dreadful war of attrition around the narrow gorge, it was not the rocks that broke first, but the pebbles.

*Was this how it had to end?*

Jin Wikyung breathed hard and looked around.

Everything was hazy, muffled.

Enemies and allies charged at one another over heaps of corpses, all tangled together. His retainer’s cries to him as he stood rooted to the spot were drowned out by the enemy’s shouts, reaching him only in broken snatches, like stepping-stones across a stream.

“…urry, hurry!”

He couldn’t make out the words, but Jin Wikyung understood exactly what his retainer meant.

A hand tugging hard at his sleeve.

A face full of desperation and urgency.

And it wasn’t just the retainer in front of him. Everyone around him—the martial artists of the Jin Family of Taiyuan, the Sect Leaders of their vassal sects, and the government troops—was speaking to him with their eyes.

*You have to get out of here.*

*You have to live.*

*Yes. I suppose so.*

Jin Wikyung understood how they felt.

The scales of victory and defeat had already tipped, and the invaders from the steppe were stronger than anyone had expected.

No—the strength of Dark Heaven, planted deep in the steppe, was far more terrifying than he had imagined.

Even now, the best course was to order a retreat.

While the troops at the front held out to buy time, he—the commander in chief—could gather the remaining forces and withdraw. That was the best strategy.

But…

*There’s no reason the commander in chief has to be me.*

Jin Wikyung smiled faintly and closed his hand around the sword hilt he had been holding loosely.

He had spent the past few years more accustomed to a brush than a sword, but the Sword Energy of a Peak master had not dulled in the slightest.

*Shhk!*

A Keshik trying to break through his guards crumpled without a fight.

Jin Wikyung advanced, cutting down the enemy with clean, precise movements. His retainer hurried after him again.

“Lesser Family Head, why—”

*Thuk!*

Jin Wikyung took another life and spoke.

“Tell Lee Seowol, the Sect Leader of the Mount Heng Sword Sect, that from this moment on, I entrust everything that follows to her.”

“……!”

“Go. Now!”

With that shout, Jin Wikyung swept his sword through the air.

A defeated general had nowhere to return to. After sacrificing the lives of so many of his people, this was where he belonged.

*She’s clever. She’ll manage.*

With the weight on his heart lifted, his sword felt lighter. Pain flared from the wounds where lances and arrows had grazed him, setting his blood ablaze.

*I promised everyone. I would protect this land—Shanxi Province.*

He had made another vow, too.

Even if everyone else fled in terror, he would remain here.

He would live and die with them.

“Come on, then! I am Jin Wikyung, Lesser Family Head of the Jin Family of Taiyuan! I’m right here!”

*Crack!*

At the sight of Jin Wikyung advancing with a beast’s roar, a flame sprang up deep in the eyes of the Shanxi defenders who had been wavering.

A shiver, its origin unknown, raced from the crown of their heads through their entire bodies.

*There he is.*

The man they had been searching for all this time was right there.

The man who cherished and loved this barren land and the people living on it more than anyone.

The true Alliance Leader of Shanxi Province.

“Yaaaaah!”

“Protect the Lesser Family Head! Protect Shanxi Province!”

With a tremendous roar that shook the gorge, the people of Shanxi charged with all their strength.

They did not retreat.

Not one of them.

* * *

Jin Mukyung suddenly felt fatigue seep through his whole body.

It was the pain of his flesh, which he had momentarily forgotten, and the vague helplessness of facing an insurmountable wall.

*Was this how it had to end?*

Jin Mukyung looked up at the sky and muttered inwardly.

Even the faint moonlight had been swallowed by the clouds. As always, the sky offered no answer.

It simply hung over everyone in silence, watching, as though this too were fate.

The countless enemies and allies.

The corpses that had left this world and could no longer move.

And the two men standing tall at the center of it all.

Jin Mukyung and Jamukha.

“That’s a fine sword. More than worthy of being called a divine weapon.”

Jamukha’s gaze moved slowly.

To the blade, shining white even in the darkness. To Jin Mukyung. And, finally, to the Demon Bird’s corpse, sprawled in a pool of blood without so much as a twitch.

“He always called himself a hunter. Arrogant and stupid, considering how long he’d lived.”

His eyes and tone were calm.

Jamukha showed not the slightest regret at the Demon Bird’s death. Jin Mukyung tightened his grip on the hilt and spoke.

“If he’d heard that, he’d have been sad. You’re saying he was a hunting dog his master didn’t even acknowledge.”

“Master?”

“He was a subordinate you cared for, wasn’t he? Or was I wrong?”

Jin Mukyung had tossed out the remark to create even the smallest opening. But Jamukha’s gaze did not waver in the slightest.

“I’m disappointed.”

“What?”

“Speak with your sword, not that silver tongue of yours. A provocation like that doesn’t suit someone like you.”

“……!”

“You’re still far too clumsy. Though, of course, choosing the wrong opponent was a big part of it. Like that pathetic fool lying over there.”

At Jamukha’s scornful glance toward the Demon Bird’s corpse, Jin Mukyung bit his lip.

Jamukha was right.

Trying to provoke an opening by using the Demon Bird’s death had been the wrong move from the start.

Jin Mukyung didn’t know why, but even after losing his sharpest-toothed hunting dog, Jamukha seemed entirely unmoved.

No—somehow, he even seemed pleased.

*What is it? Why?*

As Jin Mukyung wrestled with the question, Jamukha, who had been studying the Sword Demon with interest, suddenly spoke.

“If you’re not going to swing that sword, why not put it down?”

For a moment, Jin Mukyung understood what he meant and let out a quiet laugh.

“You want me to surrender? To you, of all people?”

“Surrender?”

Jamukha frowned and shook his head.

“No. I mean submit. Roll over and show your belly to your master, wag your tail, and lick his feet like a dog.”

“……!”

“You’ll have to become my new hunting dog. Fortunately, I happen to have a spare collar.”

Jin Mukyung stared silently at Jamukha.

Then he spoke without warning.

“The Blood Soul Fat Demon—the Demon Bird—said something similar to me.”

“Did he offer to take you as his disciple?”

“I didn’t listen closely. It sounded like a pig squealing. But something like that.”

“That’s no surprise. He would’ve trained you and eventually tried to kill you himself. Though, looking at how he ended up, he’d have been the one to die.”

Jamukha spoke calmly, then continued.

“But don’t misunderstand me. I’m not like the Demon Bird.”

“You don’t look any better than him. If anything, you look worse.”

“I only intend to raise you as a hunting dog instead of prey. I might even let you off the leash when the time is right.”

“Sure. I bet you would.”

*Shing.*

A cold, sharp edge filled the air.

Jin Mukyung slowly raised his sword upright and spoke through its white blade.

“By the time that ‘right time’ you’re talking about comes, everything I want to protect will be gone.”

Their conversation was over. He had no regrets.

Better to die as a human being, the Second Young Master of the Jin Family of Taiyuan, than survive as a hunting dog.

To Jin Mukyung, who had already resolved to die, everything Jamukha had said was bullshit from beginning to end.

At least, until he heard Jamukha’s next words.

“I’ll spare your life. Yours, and all of theirs.”

“……What?”

“If you refuse to become a hunting dog because you have something to protect, then I mean to give you enough food.”

Jamukha looked at Jin Mukyung, whose eyes had widened, and gestured toward the battlefield, filled with screams and shouts.

“Do you know how to tame a hunting dog? It’s surprisingly simple.”

A leash alone was not enough.

A hunting dog that hadn’t been fully tamed would become a beast the moment its leash came off, and bite its master.

“But what if it’s starving?”

A hunting dog kept on a tight leash and starved for days on end would grow docile. It would have no strength left to bite anyone, and in the helplessness it had never experienced before, it would realize it was nothing but an animal.

“That’s when the master appears and tosses it some food.”

*Shk.*

Jamukha held out his hand toward Jin Mukyung.

There was nothing in his empty palm. Yet Jin Mukyung could see it clearly.

Not meat dripping with blood, but the countless people of Shanxi fighting to the death inside the gorge.

Everyone’s lives—including his own.

“……!”

Jin Mukyung gritted his teeth without realizing it.

Was it fear of the man in front of him?

Wrong.

It was hope.

Just for a little while.

The hope that if he betrayed righteousness and turned his back on chivalry for only a short time, everyone could survive.

That he could save the people continuing a blood-soaked battle whose ending was already decided, his one and only older brother, and the two Peak masters waiting to die behind him.

“Mukyung!”

“No! Absolutely not!”

Wipeng and Cheol Mubaek.

Jin Mukyung looked at the two men shouting with what little strength they had left, his gaze sunk deep.

“I’m sorry. Both of you.”

“……!”

“……!”

Wipeng and Cheol Mubaek’s eyes widened. Jamukha smiled.

Jin Mukyung looked at Jamukha and parted his lips.

“Did I ever tell you?”

“Tell me what?”

“What I said to a certain pig bastard who wanted to take me as his disciple.”

Jamukha’s smile had faded a little as Jin Mukyung stepped toward him.

With a single phrase, spat out through clenched teeth, he answered:

“Go suck a dick.”

“……!”

At the instant Jamukha’s expression hardened—

*Boooooo!*

Far away, the resonance of dozens of horns reached the gorge at once.

Jamukha knew better than anyone what that urgent blast meant.

*An enemy attack!*

And at the same time, he realized something.

The tremor everyone in the gorge had felt moments ago hadn’t belonged only to the nomads.

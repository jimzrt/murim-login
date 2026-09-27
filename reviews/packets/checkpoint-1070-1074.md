# Checkpoint Review — 1070–1074

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

# Chapters 1070–1074

## Plot

Jin Taekyung’s roughly three thousand allies are surrounded by at least ten thousand monsters coordinated by bell-ringing sorcerers. The Blood Lord orders the sorcerers to thin the allied force and capture Jin alive. A hidden intruder and his Little Grandpa disable one sorcerer; the intruder believes the others are dead. As Jin’s exhausted troops prepare to break the enemy formation, the Great Sir appears and commands the monsters to kneel. Cheongpung and the Slaughter Saint arrive; they are revealed to have defeated the monsters, and the Slaughter Saint spends nearly two days stopping Dark Heaven’s pursuit. The group escapes the wilderness with a bound black-robed captive and reaches a lakeside camp, where Gung Gibang and other beggars are waiting.

## Continuity

- Jin’s force reunited with Cheongpung and the Slaughter Saint after several months. Cheongpung still calls Jin “Benefactor.”
- Cheongpung and the Slaughter Saint defeated the ten thousand monsters; the Slaughter Saint then held off Dark Heaven’s pursuit for nearly two days.
- Bow Saint recognizes the Slaughter Saint, who says he is acting to set the changed world right.
- The group reached a large lake with Gung Gibang’s group and brought a bound black-robed captive. The captive’s identity and what he knows remain unknown.
- Great Sir gives her name as Soonja and befriends Cheongpung. Her connection to the Slaughter Saint and what happened to her boy companion remain unclear.
- The group’s arrival at the lakeside camp leaves what awaits them there unresolved.

## Translation Decisions

- Use “Soonja” for 순자.
- Retain Cheongpung’s established address “Benefactor” for Taekyung; translate 아주머니 as “Auntie” when Cheongpung addresses Soonja.

## Durable state

{
  "active_continuity": [
    "Taekyung’s group reunited with Cheongpung and the Slaughter Saint after several months.",
    "Bow Saint recognizes the Slaughter Saint, who acts to set the changed world right.",
    "The Slaughter Saint and Cheongpung defeated the ten thousand monsters; the Slaughter Saint stopped Dark Heaven’s pursuit over nearly two days.",
    "The group reached a large lake with Gung Gibang’s group and brought a bound black-robed captive."
  ],
  "continuity_sources": [
    1074
  ],
  "open_questions": [
    "Who is the black-robed captive, and what does he know?",
    "What is the connection between Soonja and the Slaughter Saint?",
    "What does Bow Saint mean by setting everything right?",
    "What happened to the Great Sir’s boy companion?",
    "What awaits Taekyung’s group at the lakeside camp?"
  ],
  "safe_through": 1074,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1070

# Chapter 1070

The senses were information.

Through their five senses—sight, hearing, smell, taste, and touch—people could learn what was happening around them.

Just like now.

*This is…*

The sensation came without warning, like an uninvited guest. I held my breath and stared into the darkness.

Beyond it, I could barely make out anything a hundred feet away.

But improving your martial arts meant sharpening your senses, and the several jiazi of internal energy stored within me were more than enough to push those sharpened senses past their limits.

“Don’t take it off yet.”

“……!”

One short sentence was all it took.

Jeong Hogun’s eyes widened in an instant, answering for him.

And nearly at the same time as me—or, no, just a hair before me—Bow Saint and Jeok Cheongang each spoke in turn.

“Dust cloud. About a thousand yards out.”

“They’re not like the ones we’ve faced so far. Everyone, prepare yourselves.”

Bow Saint told us what she’d seen and heard. Jeok Cheongang voiced his suspicions.

The same ominous suspicions I’d been having.

*Rumble. Rumble.*

The ground trembled, the vibration drawing closer by the moment.

But something was different this time.

The rumble was incomparably louder and deeper than the pursuing forces we’d clashed with three times already.

*What is it?*

I pushed my senses further, and at last picked up a new clue.

*Boom. Boom.*

Amid the constant, faint tremors came the occasional, heavier impact.

No.

*A thunderous boom.*

The moment I realized, a chill ran down my spine.

That sound—that tremendous boom—wasn’t something an ordinary human could make.

It belonged to cursed monsters that shouldn’t exist in this world, but had come into reality all the same.

*Rooooom!*

The rumble surged closer and shook the earth. Another darkness, carrying a stench with it, spread over the low hill.

And then—

“Grrrraaaah.”

Something that could hardly be called human slowly raised its head above the hill, letting out a low, ominous roar.

No. It was a monster.



* * *



The moment they saw the cursed monster with their own eyes, all three thousand people froze.

The Embroidered Uniform Guard, clad in loyalty harder than steel.

The martial artists of the Black Dragon Demon Gate, who’d endured every hardship the unorthodox martial world could throw at them.

The Disciples of the Zhongnan and Kongtong Sects, who’d spent long years cultivating their minds and bodies in the Daoist tradition.

In that moment, the level of their martial arts and their experience in the martial world meant nothing.

The enormous shock that hit them was beyond the reach of skill, age, or experience.

It couldn’t have been otherwise. It was only natural.

*What the hell… is that?*

The moment the monster came into view atop the hill, everyone had the same thought.

It was huge. Just huge.

Faced with that overwhelming sight, the very unit of measurement called a *foot* vanished from their minds.

Anyone in the world would have felt the same if they’d seen that monster, nearly twenty feet tall, with a torso as thick as a great tree.

“Grrrraaaah.”

A vast hole opened—or rather, the monster’s mouth—and wind blew from it.

Its cry was too slow to call a roar, and all the more chilling for it. The wind that poured out with that sound carried more than a horrible stench.

Fear.

It was fear.

The darkest emotion a human could feel—and, for some monsters, a power bestowed at birth.

There was no other word for it. So people from another world called that power exactly what it was: Fear.

*Hummmmmm.*

The people could feel it.

The air trembling around them. Their vision growing hazy.

And their legs, unable to move from the ground.

“P-Primordial Heavenly Venerable…”

The single groan that slipped from one Daoist’s lips spoke for them all.

Supernatural powers?

The inexplicable?

No. Wrong. Not enough.

What words could possibly describe this moment, this monster, in full?

Why had the god they followed allowed such a cursed being to walk this earth?

Only days ago, countless followers of Dark Heaven had blackened the vast snowy fields of Great Snow Mountain. Even they hadn’t filled the people with this much terror.

Nor had the jiangshi who, following the Eastern Heaven Demon Lord’s bell, had stained the imperial palace’s great banquet hall with blood—the ones the Embroidered Uniform Guard remembered all too well.

At least they’d still had human shapes.

No matter how far they’d fallen from being human, they’d retained some trace of what they once were.

But—

*This can’t be real.*

*It can’t be. This is impossible.*

*It’s a dream. Yes. It has to be.*

Frozen in place, the people stared with distant, clouded eyes at the monster standing atop the hill.

If Pangu, the primordial giant said to have opened the world with a single swing of his axe, had truly existed in some unimaginably distant past, perhaps he’d looked like that.

Of course, unlike Pangu’s majestic myth, passed down through rumor alone, this monster looked as though it had been dragged straight out of someone’s nightmare.

*Boom. Rumble!*

One step.

But no one who saw the low hill crumble in a single step could call it “just” a step. The monster’s heavy footfall trapped them in endless terror.

A vague fear of something they’d never seen or heard of before.

Just looking at it felt enough to stop their breath. Their fear seemed to become an invisible hand, squeezing their hearts until they burst.

That was what would have happened—if a dazzling flash hadn’t erupted from somewhere at that very moment.

*Whoosh!*

In an instant, the pitch-black darkness split apart.

Space warped along a deep blue flame, dark yet bright, bright yet dark.

Something that was neither light nor darkness.

It was fire.

Hellfire, holding both darkness and light, powerful enough to burn and purify everything.

At the very tip of that fire, warping space as it surged forward, stood the enormous monster that had just stepped over the hill.

“Grrrraah!”

Its roar shook the air in every direction.

At the same time, an arm as thick as a log swung toward the flame, bursting through the compressed air.

No.

It was swinging at the small, unimpressive human being who was flying toward it, fused with a spear wreathed in flame.

*Whoooosh!*

A horrifyingly violent rush of air.

But even as the monster’s fist, packed with tremendous force, bore down on him, Jin Taekyung’s gaze didn’t waver. He rushed toward the monster, stepping on invisible stairs in midair.

Neither did his advancing steps, his body hurtling forward with them, or the silver-white spearhead wreathed in navy-blue flame.

*Shhk.*

The spearhead moved with sudden, fluid grace, the flames rippling along its edge.

Space warped with the tremendous heat within them. The sight looked like a fire dragon in motion.

Just like the name of one of the forms of spearplay devised long ago, after painstaking thought, by an old ancestor of the Fire Gate Clan.

*Fire Dragon’s Single Tail.*

The fire dragon’s tail, gliding through the air, met the monster’s fist.

*Slice!*

Everyone on the ground heard the chillingly sharp cut.

They saw the enormous mass of flesh separate from its owner’s body.

And the monster saw it, too.

“Grr…?”

With a puzzled look, it stared at its huge fist—or, more precisely, the place where its fist had been.

Only now did blood begin to bead along the cleanly severed edge.

*Splaaash!*

Blood erupted in a fountain. Caught between the pain that arrived a moment late and a question it couldn’t answer, the monster writhed, overwhelmed by an emotion beyond description.

It didn’t notice the spearhead, moving at blinding speed toward a single point even now.

*Thud.*

The monster felt something so hot it turned its vision white—and, at the same time, so cold it made its body shudder.

The spearhead had driven straight into its throat. It cut off the roar the monster had been about to unleash and poured out a fire it couldn’t possibly resist.

Just like the eyes of the man filling its vision.

“This isn’t a Troll or an ogre… What the hell are you?”

His voice was low and steady.

But the monster’s intelligence was too low to understand him. Jin Taekyung read the truth in its large, bewildered eyes.

“Yeah. I figured. That’s as far as you’re allowed to go, isn’t it?”

A monster’s Intelligence was proportional to its strength.

Jin Taekyung murmured softly, looking at the monster with a deeply troubled gaze.

It couldn’t make a sound with the spearhead lodged in its throat. As its eyes slowly dimmed, it stared back at the human before it. Jin Taekyung’s jaw clenched.

“Who made you? And how?”

He wasn’t asking for an answer.

It was a question Jin Taekyung asked himself—and a question for the other enemies emerging over the giant’s shoulder.

*Boom! Rumble!*

Large and small shadows, cloaked in darkness, surged forward like a wave.

The ground, which had trembled faintly, now shook violently, as though an earthquake had begun. And it wasn’t happening in just one direction.

*Rumble.*

Amid the tremendous noise raised by the enemies, now a few hundred feet away, came faint vibrations nearly lost beneath it.

Feeling the large and small tremors, layered in from every direction in the distance, Jin Taekyung muttered without realizing it.

“…A net over heaven and earth.”

There was no doubt.

They’d been surrounded. And very carefully, too.

Jin Taekyung knew better than anyone that this wasn’t a net a pack of low-Intelligence monsters could form.

*Jingle. Jingle.*

Hearing the faint sound of bells carried by the wind from all around, Jin Taekyung twisted the spearhead embedded deep in the monster.

*Crack. Splaaash!*

The monster’s body crumpled, its life ending without so much as a dying cry. Foul-smelling blood burst out and soaked Jin Taekyung’s collar.

He didn’t care in the slightest.

He’d have to be drenched in their blood countless times before tonight was over—maybe even for days to come.

Only then could he tear through this horrifyingly tight net and make it east.

“You all saw that, right? These fuckers ain’t shit.”

Jin Taekyung spoke to everyone.

East, west, south, north.

There was nowhere to run. The only path left was to fight.

“Let’s go.”

With that low, steady command, three thousand weapons leveled toward the enemy.
## Chapter artifact 1071

# Chapter 1071

I quickly read the situation around me and assessed it.

Above all, I focused on estimating the enemy’s numbers from the size of the dust clouds rolling in from every direction and the strength of the vibrations coming through the ground.

*At least ten thousand. It can’t be any less.*

Naturally, things didn’t look good.

Even a rough estimate put them at more than three times our numbers.

And the enemies drawing closer by the second were monsters that neither tired nor died easily.

*There might even be another mutant like that one among them.*

I turned to look at the giant’s corpse, its head split in half and its life well and truly ended.

I could say with certainty that the identity of that huge monster wasn’t a Troll or an ogre.

Not even the monster encyclopedia—which recorded every kind of monster to appear since the Great Cataclysm plunged the modern twenty-first century into chaos—contained anything like it.

Just as I’d thought to myself earlier, *mutant* was the only word that fit.

Like the other monsters that had begun appearing in Murim some time ago.

*Right. The same pattern as back then.*

This wasn’t the first time a mutant had appeared.

Similar things had happened in Hubei and at the Nanman Beast Palace.

And I clearly remembered that at the center of all of it had always been the followers of the Lord of Heaven—and the *rifts* they brought with them.

*If that’s true, then could it be…?*

A single ominous thought suddenly flashed through my mind.

But I shook my head and cut it off.

Even if the thought that had just occurred to me was entirely true, taking down the enemies right in front of us had to come first.

“Sama Pyo. Jeong Hogun.”

I spoke abruptly, looking the two of them straight in the eye.

“From now on, you each take one side. Left and right.”

Sama Pyo and Jeong Hogun bowed without a word and moved immediately.

Each commanded a thousand men. From this moment on, they would form our left and right wings.

Along with one Supreme Peak master who’d delayed us in this urgent situation—but, by an absurd coincidence, had also bought us time to prepare for the enemy.

“Great Sir.”

“Hm? Me? Can’t I sit this one out? I don’t have any particular grudge against them.”

“Fuck, Great Sir.”

“…Where should I go?”

“Left and right. Go back and forth, and help whichever side is in trouble.”

“Ugh. Fine.”

With that, our two wings would grow sharper and stronger.

His mind might wander, but as long as a Supreme Peak master stood with us, they wouldn’t break easily.

“And what should I do?”

I answered at once when Perfected Being Hyeoncheon, the Sect Leader of the Kongtong Sect, asked.

“Please take the rear with the Kongtong Disciples, Sect Leader.”

“It’s unfortunate that the Zhongnan Sect has taken the vanguard from us, but in this situation, our sect must play the most important role. I understand your intentions, Daoist Friend.”

When the enemy had nearly completed their encirclement, the rear mattered more than the vanguard.

In that regard, Perfected Being Hyeoncheon understood tactics better than the average martial artist.

He was a veteran who’d weathered the great turmoil of the Great Faction War with his own body. It wasn’t hard for him to see what I intended.

Of course, even Perfected Being Hyeoncheon hadn’t seen everything.

“The Zhongnan Sect won’t take the vanguard.”

“What do you mean?”

Leaving Hyeoncheon staring at me in confusion, I called to the man gripping his sword with a tense expression.

“Hyuk Sopyung. You and the Zhongnan Sect will help the Kongtong Sect take the rear.”

Hyuk Sopyung, the Zhongnan One Dragon.

He was leading the surviving Zhongnan Disciples in place of the Wind-and-Cloud Sword Lord, who’d been severely injured in the battle at Great Snow Mountain and had to remain in Gansu. His eyes widened.

It wasn’t just Hyuk Sopyung. Everyone around us, listening closely to my every word, reacted the same way.

“Then the vanguard will be…”

As Hyuk Sopyung trailed off, a rough voice rang in everyone’s ears.

“What are you standing around for? Get your asses to the rear.”

It was the Fire King, Jeok Cheongang.

And beside the giant who’d violently stamped his mark on this vast martial world stood a woman called a star, not a king.

*Click.*

Everyone fell silent as Bow Saint joined her two curved swords together, forming a massive bow.

Who were they?

The Fire King and the Bow Saint.

The King of Kings, holding the most savage flames. A star of the martial world who’d dominated countless battlefields with a single bow. Living legends of Murim.

And—

*Step.*

I, too, had earned the right to stand beside them.

In this moment, I’d become a symbol of someone who could walk toward the Fire King and the Bow Saint.

Even if I was a little smaller than they were, and still a little weaker.

I, Jin Taekyung—the Blazing Flame Divine Dragon—was another giant who’d risen in this goddamn war.

*Rumble, rumble!*

The ground trembled. No—it writhed.

Apart from the low hill behind us, the reed bed had once been open in every direction. Now it was surrounded by dense clouds of dust.

No. We were surrounded by monsters whose origins and identities we didn’t even know.

But—

“Anyone still scared of those worthless bastards?”

I wasn’t afraid of them.

If there was anything I feared, it was the misfortune of someone dying because of my mistake.

“If you’re afraid, if you want to run, leave the formation now. I won’t blame you.”

I meant every word.

Everyone had a family, someone or something they needed to protect.

There was no such thing as cowardice when it came to survival.

If anyone wanted to fall back so they could make it home alive, I’d gladly protect them.

Just as someone had done for me, years ago, in that dark, reeking cave.

And now I had people beside me worth risking my life to protect.

“Fuck it, what’s life anyway? I’ve spent all this time following your ass around, Captain. Now I wouldn’t even flinch if the Heavenly Demon’s granddad showed up.”

Hyuk Mujin’s sudden remark drew quiet laughter from around us. Then he added, softly:

“I’ll follow you. Even to the edge of hell.”

“……!”

“……!”

For an instant, the air around us rang like a struck string.

In that moment, it was as if the great rumbling all around us, and the monsters’ roars beyond it, had vanished from the world.

At the same time, a wave of steel swept it all away.

*Clang, clang, clang, clang!*

Everyone raised their weapons and let out a shout.

Forgetting their physical exhaustion and their fear of monsters they’d never seen before, they roared like beasts and glared into the wavering darkness.

Remembering why they had to be here. Remembering the faces of those they missed, killed by the monsters.

And at the head of them all stood me.

“Remember only two things.”

I started toward the vanguard and continued.

“First. Hold the current formation no matter what.”

*Clack, clack, clack!*

The human tide parted as I advanced.

Beyond it, an empty space came into view.

Unlike the other sections, where a thousand men had gathered in each, this vacant spot looked like a massive hole that could collapse at any moment. But it wasn’t one anymore.

“Second.”

*Step.*

I stopped among the reeds.

Bow Saint to my left. Jeok Cheongang to my right.

And behind the three of us stood the members of the Fire Dragon Pavilion, who’d followed me without hesitation.

There weren’t many of us, but we filled the empty space at the front completely, finishing the formation.

“Survive, no matter what it takes.”

Just as I spoke those final words—

*Rrrrmmm!*

With a deafening roar that sounded as if the sky had split apart, countless shadows came pouring in from every direction.

They surged toward the circular formation of roughly three thousand elite fighters.

No—the enormous wheel of steel.

*Whoooosh—BOOM!*

A streak of light shot from Bow Saint’s fingertips, tearing through the darkness and exploding.

*Craaaack!*

The steel wheel—the wheel of death—finally collided with the monsters that didn’t belong in this world.

*Jingle.*

The eerie, sinister sound of a bell rang out beyond the swirling spray of blood.



* * *



They existed in deep darkness.

No, perhaps at least in that moment, they were the darkness itself.

They weren’t simply hiding in the dark. They used it as a curtain to conceal themselves.

Even without every last inch of their bodies covered by black robes, few could see through the curtain that surrounded them and glimpse what lay within.

The people capable of seeing through their concealment were hundreds of yards away, fighting countless monsters.

Those monsters were the concealed figures’ subordinates, moving under their control.

*Jingle.*

The black-robed man shook the evil bell in his hand.

Its sound was dull, issuing from the old, dark object, but it carried clearly into the distance, relaying further commands and information.

Just like the black-robed man’s other comrades, hidden at regular intervals in every direction.

“So it’s finally begun.”

*BOOM!*

The black-robed man quietly murmured as he spotted a flash of light far away, accompanied by a deafening boom.

The monsters’ ceaseless roars made it impossible to judge precisely from sound alone, but that streak of light was unmistakably Bow Saint’s. It was proof the battle had begun.

“It’s not where we wanted them, but… at least we’ve completed the encirclement.”

The black-robed man couldn’t help feeling disappointed.

Another fifteen minutes.

If they’d moved just that much faster and gotten out of the reed bed, he and his comrades could have started the battle from a far more advantageous position.

“But it’s already begun. Nothing to do about it now.”

The battle was underway, and the role assigned to the thirty sorcerers, including the black-robed man, was clear.

“Cut down their numbers as much as possible. If you can, capture Jin Taekyung alive.”

The black-robed man quietly repeated the order he’d received from the Blood Lord just half a day earlier, then furrowed his brow.

“Capture him alive instead of killing him?”

The black-robed man had received information about the enemy before the order came. It sounded absurd.

Among them were no fewer than six Supreme Peak masters, and two of those were the Fire King and the Bow Saint.

If they concentrated all their strength on Jin Taekyung alone, they might have a good chance of killing him.

Capturing him alive, though, would be an extremely difficult task.

“Damn it.”

The black-robed man instinctively sucked in a breath and glanced around, having cursed the Blood Lord without thinking.

But, as always, all he saw were monsters standing vacantly around him, giving off a horrible stench.

“…This is bullshit.”

The black-robed man looked at his subordinates with irritation in his eyes and voice.

He hated that he was trembling in fear of the Blood Lord, who was nowhere near him. And today, he found himself especially disgusted by the monsters that had lost their reason and only gave off a foul stench.

“Stupid bastards.”

*Jingle.*

The black-robed man shook the evil bell with a shooing motion. The hundred monsters surrounding their master to guard him immediately took a step back without hesitation.

At least, that was what the black-robed man knew was supposed to happen.

*Step.*

“…?”

The black-robed man blinked.

Ninety-nine monsters stepped back. He stared at the one that had stepped forward alone.

“What the hell is this?”

Before the black-robed man could find the words, the monster finally seemed to realize its situation. Its backside twitched as it fidgeted, then it said:

“W-Wow. Amazing. You’ve never seen a monster like this before, right?”

“……!”

“I-I haven’t either. Damn it.”

The monster—or, clearly, someone who was a person—continued in a trembling voice, then wore a miserable expression and sighed.
## Chapter artifact 1072

# Chapter 1072

At that moment, there was only one thought in the black-robed man’s mind.

*Am I seeing things?*

It was a perfectly reasonable question for him to ask himself.

He was a sorcerer.

A highly experienced one, with considerable skill.

He had neither internal energy measured in jiazi nor martial arts exceptional enough to be called divine. But he did have the ability to control hundreds of monsters perfectly.

And yet…

*What the hell is this guy?*

The black-robed man stared blankly at the monster before him—or, more precisely, at the uninvited guest who had obviously pulled a monster’s hide over himself.

Only after pinching his arm hard enough to confirm he wasn’t dreaming could he finally squeeze out the question he’d been holding back.

“Who are you?”

The mysterious intruder flinched and answered in a halting voice.

“I-I’m a monster.”

“……You’re talking like a person.”

“A-aren’t there monsters that talk like people?”

“……There can’t be.”

At the black-robed man’s thoroughly logical rebuttal, delivered with all the confidence of an expert, the intruder fell silent for a moment, then opened his mouth.

“Grrroooar.”

“……”

“Ahem. Grrroooar.”

“……”

“G-grraaaah.”

The intruder kept making uncertain monster noises, now raising both arms like a jiangshi. The black-robed man sank into even greater confusion and shouted.

“Stop!”

“Gasp. Why?”

“What the hell is this supposed to be?”

“I was doing my best to imitate them… Wasn’t that last one pretty close?”

“No, that one was a little close.”

“Wow! I knew it! Thank you!”

An exchange that strayed far enough from common sense could paralyze the mind.

Just as the black-robed man ran out of words, the intruder, unable to hide his delight, added proudly:

“All that practice for two days straight paid off. I guess it’s true what they say: hard work doesn’t betray you.”

The black-robed man, still floundering in confusion, blinked at the unexpected answer.

“W-what did you just say?”

“Hm?”

The intruder tilted his head. His eyes, visible beyond the rotten hide, were clear and bright.

“Oh, that hard work doesn’t betray you? My grandfather’s been telling me that since I was little…”

“Not that!”

“Oh, I know what you mean. The big people. Well, it’s not quite right to call them people, but anyway, I hid in there and kept trying to imitate them.”

“S-so you mean…”

“That’s right. Like I said before, I’ve been doing it for two days.”

“……!”

Despite the intruder’s innocent answer, the black-robed man was struck by a shock that seemed to freeze his spine.

*For two days? And I never noticed?*

It made no sense.

After grueling training, he’d gained the ability to perfectly control some five hundred monsters. That was why he could detect the life energy of living humans with his eyes closed.

But…

*He’s not lying.*

The black-robed man sensed it instinctively.

Every word the mysterious intruder before him had spoken was true—not a single one a lie.

As far as he could tell, the man didn’t have the Intelligence to lie convincingly. And now that he’d been caught so plainly, he had no reason to hide anything.

Those thoughts, and the situation unfolding around him, finally helped the black-robed man come to his senses, as if he’d been bewitched.

“You… You’re an orthodox faction lackey.”

The intruder gasped and hurriedly waved his hands.

“N-no, I’m not!”

“Shut up, you lunatic.”

“Lunatic? That’s a very vulgar and bad word. My grandfather told me never to say it.”

“You little piece of—!”

The black-robed man felt his blood rushing to his head.

Even if the situation had caught him completely off guard, he’d let himself be played by some lunatic, if only for a moment.

He shook the evil bell in his hand, his anger lending force to the motion.

*Jingle!*

It wasn’t his imagination. There was unusual force behind the bell’s sound.

The distinctive death energy possessed only by sorcerers who commanded monsters made the sound more ominous and clear. That chilling tone carried two meanings.

First: alert the other sorcerers stationed nearby to the situation.

And second—

*Whoosh! Thud!*

Leave the disposal of that lunatic to the hundred or so monsters he’d brought as guards.

“You have one chance left to receive my mercy.”

The monsters swept around them with speed that belied their enormous frames, forming an impenetrable wall in front of the black-robed man. From behind it, he spoke through clenched teeth.

“If you surrender quietly right now and tell me everything you know, I’ll promise you a relatively quick and painless death.”

The black-robed man wasn’t relying on numbers alone.

Each monster guarding him had skill comparable to a master ranging from at least Supreme First Rate up to Peak.

Their strength and speed surpassed human limits, and, more than anything, their tenacious vitality was a nightmare.

And there were a hundred of them.

Even if the intruder before him was a lunatic with tremendous skill, the outcome wouldn’t change in the slightest.

The monsters here weren’t the only ones he’d have to face.

“Go ahead and struggle all you want. You won’t even be able to do that a few moments from now.”

The black-robed man curled one corner of his mouth as he thought of his fellow sorcerers, who should have received the signal and be rushing here at once.

“But why haven’t I gotten a reply?”

The intruder’s sudden question made the black-robed man reflexively ask:

“What?”

“A reply. Uh, in this case, should I call it a reply-sound? Anyway, from what I’ve seen over the past two days, you always communicate with the bell, even over the smallest things.”

“……Huh?”

The black-robed man suddenly realized something. He hurriedly looked around.

No—he focused all his attention on listening.

He was waiting to hear his fellow sorcerers answer, their sinister bell sounds similar to his own.

But the only sounds reaching his ears were the wind blowing from far away and the breathing of the monsters surrounding them. Nothing answered.

Nothing at all.

“……!”

The black-robed man’s heart lurched.

Something had gone wrong.

Terribly wrong.

With a sense of foreboding sweeping through his mind, his confused eyes turned toward one figure.

The intruder, surrounded by horrible monsters, had perked up his ears and even cupped his hands around them like a trumpet to listen.

“Oh. You’re right. I can’t hear anything. Nothing at all.”

“You, you…”

What was he supposed to say?

How could he make sense of this situation?

The black-robed man could barely get the words out. Beyond the discolored monster hide, the intruder’s eyes curved clearly into crescents.

“What a relief. I knew I could count on Little Grandpa.”

“L-Little Grandpa?”

“Yes. He’s the one who teaches me all sorts of things. He gets really angry whenever I call him Little Grandpa, but sometimes it seems like he secretly likes it, too.”

The intruder stopped rambling and snapped his mouth shut with a little gasp.

“Oh, don’t tell Little Grandpa I said that. He’ll get angry again.”

The black-robed man didn’t answer.

More precisely, he no longer had the presence of mind to answer.

He could only stare blankly at the intruder, who had finally stopped talking, then squeeze out the question that had just come to mind.

“Who… No, who are you people?”

His vision was blurring. The words he’d just heard had made him realize a truth he desperately didn’t want to believe.

The other thirty or so sorcerers who’d come here with him were already dead.

They’d been killed the same way the intruder had slipped in beside him—or in a manner even more secretive and deadly.

Even if anyone was still alive, they wouldn’t be for long.

If the owner of the sobriquet that had just flashed through the black-robed man’s mind was here now…

“Th-that Little Grandpa of yours—could it be…?”

The black-robed man’s voice trailed off. Then—

“What did you just say?”

The flat voice suddenly pierced his ears, and a shock like lightning striking the crown of his head swept over him.

He was here.

Little Grandpa—no, *that man.*

Right behind him.

And yet he hadn’t sensed the man’s breathing. He hadn’t detected the breath that should have brushed the back of his neck along with the voice—not even the slightest trace of presence or life energy.

The breathless voice sounded again in the black-robed man’s ear, whose body had gone rigid as a statue.

“I asked you. What the hell did you say?”

The black-robed man forgot how to speak. He even forgot how to breathe.

He could only make one last desperate attempt—the instinctive final struggle to survive.

He didn’t even realize that a thin line had cut across his wrist before he could move the old, bloodstained evil bell, which was practically everything he had.

*Slice. Plop.*

Everything happened a moment too late.

The wrist, severed from its owner, hit the ground. Its owner noticed it only after it was gone.

And the black-robed man recognized the pain only when it arrived at last, then let out a scream filled with fear.

“Guh…!”

*Thump. Collapse.*

His body crumpled helplessly as the Sleep Acupoint was pressed.

And so the black-robed man plunged into a pitch-black abyss with no end in sight, unable even to scream properly.

Behind him, the voices of two people sounded distant and dreamlike.

“I told you I’d kill you if you called me that one more time.”

“I’m sorry, Little Grandpa.”

“……This is driving me crazy. Let’s go find that guy.”

“Yes! Little Grandpa!”

Truly, right to the very end, it was like a nightmare.
## Chapter artifact 1073

# Chapter 1073

*Slice!*

From the moment my forcefully swung spear cut through its first victim, my heart had been sinking heavily.

Because the enemies were stronger than I’d expected?

Or because, in a corner of my mind, I’d already been turning the word *defeat* over and over?

No. That was wrong.

I’d believed in our victory from the start, without a doubt.

It was just that, as always, I’d been made to face my own limits.

The limits of a mere human—limits I could never completely escape, no matter how many times I broke through them.

*How many people will die this time?*

Of course, I knew.

I wasn’t an omnipotent god who could save everyone.

And no one else could be such a god, either.

That was true even of the heroes in ancient myths. Cheon Taemin, hailed as humanity’s savior, was no exception.

To gain something, you had to pay a price worthy of it.

Whether that price was time or a life.

But knowing that didn’t make it something I could get used to.

No—it was something I must never get used to.

Because then, I’d start taking everything for granted.

And another person’s sacrifice and death must never become something I take for granted.

*Crraaaack!*

Just once.

The spearhead swept through, wreathed in Force, and a thick mist of blood burst out amid a ghastly squelch of torn flesh.

If the enemies had been human, the sight would have filled them with shock and fear in an instant.

But even as dozens of monsters were minced into chunks and scattered, they didn’t so much as flinch. They surged in from every direction, a relentless tide.

Their ranks were tightly packed—an orderly formation that didn’t match their ferocious, savage momentum.

*Their Intelligence isn’t high enough for this. Someone’s definitely directing them.*

Before the battle had properly begun, the eerie sound of bells had carried on the wind from all around us. It hadn’t been my imagination.

Mutants, or monsters.

I didn’t know exactly what to call those hideous creatures, but one thing was clear: somewhere, a command center was controlling them like puppets.

There was just one problem…

*They’re hiding well.*

Maybe they’d considered the presence of Supreme Peak masters like me.

Whatever the reason, I couldn’t find them anywhere. There had to be quite a few, too.

And I wasn’t the only one who couldn’t see them. The same was true even of the person among our allies with the sharpest eyes.

*Whoosh—BOOM!*

Four streaks of light shot one after another toward the east, west, north, and south, devouring space before exploding.

Amid the massive shock waves and thunderclaps that shook the air in every direction, a familiar, calm voice reached my ears.

“I can’t see or sense them from here. They’re at least a hundred *jang* away.”

The Bow Saint spoke as if she’d already read my mind.

At the same time, Jeok Cheongang appeared, drenched in the monsters’ blood, and added, “And there are a hell of a lot of them.”

*Fwoosh—BOOM!*

Before he’d even finished speaking, he thrust out a fist.

Flames raced forward, burning even the air, and swallowed up the monsters in a blast of scorching heat.

“Grrr…”

“Aaagh!”

Screams rang out over one another.

Yet even after a mighty strike brought down dozens more enemies, Jeok Cheongang’s expression didn’t brighten in the slightest.

“At this rate, it’ll never end. Unless we wipe out every last one of them, we won’t open a path.”

It was obvious the battle was going our way.

The problem was what would happen after we’d taken down all the countless monsters surrounding us.

A substantial number of our three thousand allies would surely be killed or injured, and Dark Heaven’s pursuit would continue relentlessly.

*Damn it.*

I swallowed the curses rising in my throat and looked around.

The battle against ten thousand monsters had begun only moments ago.

For now, thanks to the efforts of several Supreme Peak masters, myself included, we hadn’t suffered any notable casualties. But that was only a matter of time.

*They were already exhausted. They’ll crumble before long.*

Battle was also a fight against yourself.

No matter how carefully selected and elite they were, they were still human, made of flesh and blood—not like their enemies.

The moment people realized they were standing at the threshold between life and death, their bodies grew exhausted at an alarming rate, and their minds began to blur.

The Supreme Peak masters, who’d been giving everything from the start to protect our allies as much as possible, were also burning through their strength faster than usual.

I was no different.

*Thwack! Thud!*

My spearhead cut cleanly through the tendon in a monster’s calf. The hulking beast, a full two *jang* tall, dropped to one knee.

Its enormous frame didn’t look human in the slightest.

The flesh covering the monsters was tough as leather armor. Cutting through their bones, which were even harder, required even more strength.

*Crack.*

I poured a good deal of internal energy into a palm strike and crushed its skull. Gritting my teeth, I shouted, “Hold the formation!”

Shouts of acknowledgment rang out from every direction, but I could feel at once how much quieter and weaker they’d already become.

*Something has to change.*

Fear.

The darkest emotion given to humankind.

Of course they were afraid. They were surrounded by monsters they’d never seen or heard of before.

And right now, I had enough power to break the chains of fear holding them down.

There was one move—our best chance to turn the situation around, even if it took a tremendous amount of strength.

*One chance. Just one. I’ll find an opening and rip through their formation in a single strike.*

Even the strongest wall would collapse once a crack was forced into it.

I slowly drew in a breath.

At the same time, the world began to slow, the noise around me faded away, and a new sense opened deep within me.

The sensation of the Middle Dantian—a feeling that still seemed unfamiliar.

*Rumble…*

The space around me suddenly trembled.

I reached out, sensing everything that surrounded me.

Or tried to.

Right then, someone appeared, letting out a roar loud enough to shatter my intensely focused senses.

“Gaaaaal!”

His voice was overflowing with resolve.

And with a sprightly, utterly incongruous flourish, the Great Sir who’d cut in front of me swung a steel sword around in wide circles. I had no idea where he’d found it.

“You foolish, pitiful monsters! Gaettong, a divine general descended upon this land in answer to Heaven’s will, has arrived! Get on your knees this instant!”

“……!”

“……!”

A cold silence fell.

My allies stared blankly at the Great Sir. So did the monsters surging in from every direction.

*What the hell is this guy?*

Same look. Same thought.

But the man responsible for the miracle of bringing humans and monsters together in a moment of mutual incomprehension carried on shouting in a stern voice, undeterred.

“Hey! What are you waiting for? Can’t you hear Chunja’s command?”

At the Great Sir’s pronouncement, having changed not only his name but his gender, Jeok Cheongang muttered like a man sighing, “We should’ve grabbed that guy and killed him first.”

It was a perfectly reasonable suggestion. I almost nodded along, but that wasn’t what mattered right now.

The Great Sir showing up at the vanguard meant there was a gap in the left wing, led by Sama Pyo. And that meant our entire formation might soon collapse.

*That lunatic…!*

I knew he wasn’t in his right mind, but I hadn’t expected him to pull this shit at the most critical moment.

But we didn’t have time to vent our anger.

I was trying to suppress the curses rising from deep in my lungs and send the Great Sir back to his original position when—

*BOOM!*

The ground shook with a tremendous rumble. The nearest monster suddenly dropped to one knee.

“What… What is this?”

The single gasp that slipped from someone’s lips was the same question that had occurred to all of us, me included.

Before we could find an answer, the other monsters forming an iron wall around us began to tremble.

“Grrk. Grrrk.”

“Kuwo?”

Their pupils dilated. Strange, meaningless groans escaped them.

And then the change began.

*Thud. Rumble!*

The ground shook. Heavy bodies fell one after another, raising thick clouds of dust.

Hundreds, then hundreds more, and then hundreds again.

It went on until every monster filling the vast reed bed had fallen.

It was like watching an enormous domino chain collapse. Faced with the unbelievable sight unfolding right before our eyes, everyone—including me—was struck speechless.

Everyone except one person.

“Mm. Yes, that’s right. You’re finally being a little more obedient.”

The Great Sir turned to me, muttering smugly.

“Ahem. Did you see that? I can do this much.”

Of course I’d seen it.

I’d seen it all very clearly, right in front of me.

So at that moment, I could manage just one question.

“…What is this? Am I dreaming?”

“A dream, you say? That’s a fair way of putting it. A person’s life is, after all, like a dream in the light of day.”

The Great Sir nodded with a knowing smile.

Over his shoulder, Jeok Cheongang looked at me, half out of his mind.

“What… What in the world is going on?”

As if I knew. I was just as dumbfounded.

I answered in a dazed voice, “I have no idea either.”

“You don’t know?”

“No.”

“I’ve seen all sorts of bizarre things, but this takes the cake. Have I lived too long?”

“You certainly have.”

“Or are we perhaps sharing the same dream?”

“Could be. If you don’t mind, could you hit me once? If you hit me, it’d hurt too much.”

“For a dream, that’s a very you-like load of bullshit. Come to think of it, it’s been a while since I hit you, hasn’t it?”

“That’s a very realistic reaction. I guess it’s definitely not a dream.”

That was when it happened.

I swiftly changed course to avoid the disaster of getting hit by Jeok Cheongang, and a voice reached my ears from far away.

“Those two really haven’t changed.”

I paused at the voice of a boy who sounded too young to have gone through puberty.

“Wow! I’ve never seen a Master and Disciple like that before!”

The next moment, a cheerful voice I could never forget arrived on the wind. My lips parted before I knew it.

“…Cheongpung?”
## Chapter artifact 1074

# Chapter 1074

There’s an old saying.

*Those who meet must part; those who leave will surely return.*

Every meeting ends in a farewell, and everyone who leaves will one day come back.

At this very moment, that old proverb came to mind as I stared wide-eyed at the two figures approaching from far away, weaving their way between the monsters strewn across the darkness all around us.

“Over here! We’re over here!”

“How many times do I have to tell you not to shout like that…? Never mind. Do whatever the hell you want.”

“Yes! Thank you!”

“This is driving me insane.”

The young man bounced along as if he had springs in his feet, while the boy beside him let out a deep, old-man-like sigh. To some people, it might have been a rather strange sight.

But I—or, rather, a tiny handful of people including me—already knew who those two were.

Especially the young man cheerfully bouncing along in front. Even if you’d seen him only once, he had the kind of energy you could never forget.

“…Cheongpung?”

The name slipped from my lips before I could stop it. The people who’d been frozen in a daze after the monsters’ bizarre collapse blinked.

“If you mean Cheongpung, could it be…”

“T-the Huashan Divine Dragon?”

Their reaction was immediate.

The only Cheongpung who could appear in a situation like this was someone I knew well enough to recognize at a glance. Even if you turned the whole world upside down and shook it out, there was only one.

Of course, there were some with a reasonable question.

“I can’t see from here. Captain, are you sure you’re not mistaken? Why would Young Hero Cheongpung suddenly show up here…”

Just then, Hyuk Mujin opened his mouth, unusually cautious. A clear voice rang out from beyond the pitch-black darkness.

“Benefactooor!”

“…That’s him.”

“…It is.”

“…I knew it. That voice alone is enough to make your mind go foggy. It’s definitely him.”

At this point, the voice was practically a fingerprint.

Hyuk Mujin and I confirmed it, and then Jeok Cheongang put the matter to rest.

“Benefactor! I’m here!”

With that final shout, Cheongpung swept in like a gust of wind, waving at me with a flushed face.

“Wow, it’s been so long! Have you been doing well?”

How was I supposed to respond to that?

I stared at the first-time-experience menace before me, half bewildered and half glad to see him. After a moment, I finally managed to speak.

“No. Not at all.”

“Oh. You do look that way, actually.”

“Then why’d you ask?”

“I haven’t been doing well, you see. But I hoped things might be different for you, hee-hee.”

Watching Cheongpung cheerfully carry on even while saying something gloomy, I realized what I should do right now.

More precisely, a quiet laugh slipped out of me before I knew it.

“Wait, why are you laughing?”

“Is that what you call a question? I’d laugh too if I saw the way you act, you idiot.”

That wasn’t my answer.

Swish.

A boy appeared from the darkness with a presence like a ghost—or rather, the greatest assassin of all time. He stared straight at me, then added:

“Though the one laughing is just as much of a reckless brat.”

His tone was as blunt as ever.

But when I saw the faint smile at the corner of his mouth, I could only laugh aloud instead of answering.

We’d met again after several months.



* * *



Reunions with people you’ve missed are always a joy.

But none of us was stupid enough to sit around a campfire, chatting away, in a situation like this.

“We’d best get out of here quickly. Follow me.”

Before the warmth of our reunion had even faded, the Slaughter Saint wiped the smile from his face and got moving as if nothing had happened.

“Throw away anything that might slow us down. Especially that idiot over there.”

Jeong Hogun, the idiot the Slaughter Saint had pointed out, replied.

“I don’t know which elder you are, but you should at least show some basic courtesy. I am a Thousand Captain of the Embroidered Uniform Guard, serving under His Majesty the Emperor’s solemn command…”

*Whoosh.*

It happened in an instant.

The Slaughter Saint’s figure blurred.

Then came the sound of wind, and a gleaming blue dagger pressed against Jeong Hogun’s neck.

“Keep talking. If you waste even a few more moments, I’ll make you a real dead man.”

Everyone, myself included, recognized the loyalty Jeong Hogun and his Embroidered Uniform Guards had for the Emperor. It was extraordinary.

But reality was cold.

Unlike the Emperor, who was somewhere far away, the dagger was right in front of him. Jeong Hogun stared at it in silence before finally speaking with a grim face.

“As I said, I am a Thousand Captain of the Embroidered Uniform Guard, serving under His Majesty the Emperor’s solemn command…but you appear to have a close relationship with the Marquis of Shangshan, so I’ll let this pass.”

The Slaughter Saint replied in a dry voice to what was an exceedingly poor excuse for an Embroidered Uniform Guard.

“We’re not that close.”

“You seem to know each other at least somewhat, so I’ll let it pass.”

“Of course we know each other, but I said we’re not close.”

“……”

“Just let it go. Understand?”

“……”

“I’ll take that as a yes.”

The Slaughter Saint had spared him the last shred of his dignity in the name of martial-world etiquette. By the time he lowered the dagger, most of our three thousand allies were staring at him in shock.

A boy who wasn’t even twenty, no matter how generously you counted, had subdued a Thousand Captain of the Embroidered Uniform Guard who stood at the very peak of the Peak realm.

And he’d done it in one swift move, so fast he’d been impossible to see.

Everyone was astonished by the unbelievable sight before them, but Perfected Being Hyeoncheon seemed more shaken than anyone.

“Fellow Daoist…who are you?”

The view changes depending on where you stand.

Perfected Being Hyeoncheon was a seasoned Supreme Peak master, skilled enough to vaguely discern the Slaughter Saint’s true realm. He was so caught up in shock and confusion that he couldn’t continue. Bow Saint spoke for him.

“It’s been a long time. I never thought I’d see you again like this.”

The Slaughter Saint had seen through her identity, just as she had his. He answered with a bitter smile.

“I feel the same. I thought we’d never meet again after that day.”

“Mountains and rivers have changed, and the world has changed with them. I had to act to set everything right.”

As the people around them grew more confused with every word they exchanged, Bow Saint quietly added:

“Just as you did, Slaughter Saint.”

“……!”

“……!”

“……!”

The air around us seemed to crackle.

The Slaughter Saint.

Once condemned by the whole martial world, he had become the greatest assassin of all time after the Great War between the Orthodox and Demonic factions began, striking fear into countless great fiends.

Those two words alone were enough to explain the situation and make everyone understand.

The Slaughter Saint gave Bow Saint a small nod, then addressed the people frozen like statues.

“So. Is there another idiot who wants to waste this precious time?”

Of course, there wasn’t.

Or, to be precise, even if there was, there shouldn’t be.

Not if the person asking was called the Slaughter Saint.

*Clank. Clatter!*

Jeong Hogun and the other Embroidered Uniform Guards began throwing off their armor with the speed of reservists who’d just finished a training exercise and were hurrying home. The Slaughter Saint’s eyes suddenly narrowed.

“But what exactly is that thing?”

I followed his gaze and immediately understood what he meant.

I also understood why he’d called a perfectly healthy human being a thing.

“Well, how should I put it… That gentleman’s a little out of his mind.”

“…I’ve already gathered that.”

The Slaughter Saint sighed as he watched the Great Sir, who had somehow blended in among the Embroidered Uniform Guards and was cheerfully stripping off his clothes.

“I’ll have to hear the details, but it seems clear enough that we’ve got one more madman.”

The original madman, of course, was watching the new madman’s striptease in wonder.

“Wow! I’ve never seen anyone take their clothes off so boldly!”

The Great Sir, whom Jeong Hogun had just stopped from removing his underwear, noticed Cheongpung and brightened.

“Thank you for the compliment. And who might you be?”

“Hello! I’m Cheongpung!”

“You’re a spirited young man. I like that. I’m Soonja.”

“Nice to meet you, Auntie!”

No.

Are these guys seriously insane?

Just as everyone stood aghast at the meeting of two natural disasters that shouldn’t occur even once in a hundred years, the Slaughter Saint shook his head and spoke.

“Right. Let’s get going.”

In his hand was a rope that stretched far off into the distance.

“What’s that?”

“War trophy.”



* * *



To get straight to the point, the enemies didn’t pursue us after that.

Or maybe it would be more accurate to say that they did, and they didn’t.

“Go on ahead. I’ll catch up soon.”

The Slaughter Saint said that and left us several times. Each time he returned just when we needed him, his body reeking of blood.

After nearly two full days had passed, he said, “It should be less of a nuisance from here on.”

Not one of our three thousand allies, myself included, doubted what he meant: he’d shaken off Dark Heaven’s relentless pursuit.

And we all knew how he’d dealt with the pursuers so quickly—and that it was he and Cheongpung, not the Great Sir, who had taken down the ten thousand monsters.

“Mm! Mm!”

The trophy—no, the black-robed man bound from head to toe in rope—twitched. Taishan, who was running with him tucked under one arm like a piece of luggage, raised a fist as big as a cauldron lid.

“Don’t move. I’ll hit you.”

“Mm! Mmm!”

“Don’t make noise. I’ll eat you.”

“……!”

It was a strange threat, but it worked perfectly.

The black-robed man immediately fell silent as a mouse. Our allies had been on a brutal forced march for days without rest, but before long we finally escaped that miserable wilderness.

What awaited us was an enormous lake I’d never seen before, and a group of beggars huddled around it, lighting campfires.

One of them had a face we knew very well.

“Oh! They’re here! Over here!”

A face so shabby you’d reach for your wallet just by looking at it from a distance.

Gung Gibang—the next beggar king, destined to lead a hundred thousand beggars.

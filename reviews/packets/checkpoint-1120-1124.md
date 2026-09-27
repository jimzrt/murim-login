# Checkpoint Review — 1120–1124

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

# Chapters 1120–1124

## Plot

The East Gate falls, and Pa Ryun and Tae Gunak arrive with an army of about thirty thousand. As the Inner City crumbles under siege, the Blood Lord kills the Grand Mage, claims command of the Dark Heaven army, and orders the fanatics to kill everyone inside.

Critically wounded, Jin Taekyung reaches Jeok Cheongang and asks him to open a path. The exhausted defenders make a desperate stand, joined by the Slaughter Saint, the Bow Saint, Cheongpung, and civilians armed with crude weapons. A powerful, unidentified figure approaches. Taekyung briefly wakes, then Final Rally activates: it suppresses his pain, heightens his Qi Sense, and lets Jeok’s Scorching Yang Qi heal some of his injuries. Taekyung fights forward with Jeok and Cheongpung, while the Saints engage two Black Ghosts whose severe wounds regenerate under overlapping magic. Taekyung confronts the Blood Lord with five minutes left on the quest timer.

The Blood Lord’s counterstrike batters all three attackers and sends Jeok flying. Taekyung evades the Blood Lord’s attacks with unexplained precision, then pierces the Blood Lord’s already-wounded, unhealed palm with his spear. The result is unresolved.

## Continuity

- The Inner City remains under siege. Its defenders are badly outnumbered and exhausted; civilians have joined the fight.
- The Blood Lord killed the Grand Mage, claimed command of the Dark Heaven army, and ordered the fanatics to attack.
- Final Rally is active. The sudden quest has a nine-minute-59-second limit; five minutes remained when Taekyung confronted the Blood Lord.
- Taekyung is critically injured but fighting beside Jeok Cheongang and Cheongpung. Jeok has been knocked away; Cheongpung is under heavy pressure.
- Taekyung evades the Blood Lord’s attacks with unexplained precision. His spear pierced the Blood Lord’s wounded palm; the effect is unknown. The Blood Lord absorbs battlefield blood to replenish his strength, but that palm wound has not healed.
- The Slaughter Saint and Bow Saint are fighting two regenerating Black Ghosts.
- Taekyung believes Hyuk Mujin is dead, but did not witness his fate. He remembers an unfulfilled promise to Ju Hwaran.
- The fates of the defenders missing after the retreat from the other gates remain unknown. An unidentified powerful figure approached the Inner City defenders; this block does not reveal his identity or what followed.

## Translation Decisions

- Use she/her for the Bow Saint.
- Render 大宗師 as “Great Master,” 육호 as “Number Six,” 강시술사 as “jiangshi sorcerer,” and 부각주 as “Vice Captain” for Hyuk Mujin’s Fire Dragon Pavilion title.
- Render 멸마정천 as “Destroy the Demonic Path and restore Heaven,” 노야 as “Elder” when Taekyung addresses Jeok Cheongang, and 회광반조 as “Final Rally.”
- Retain “Black Ghost” for 흑귀 and “Force” for 강기.
- Render the quest title 바람 앞의 촛불, 혹은 불꽃 as “A Candle in the Wind, or a Flame.”
- Keep the approaching figure unidentified.

## Durable state

{
  "active_continuity": [
    "The Inner City battlefield remains under siege.",
    "The quest timer begins counting down from five minutes as Taekyung confronts the Blood Lord.",
    "Taekyung is critically injured but evades the Blood Lord’s attacks with unexplained precision.",
    "Jeok Cheongang and Cheongpung fight beside Taekyung; Cheongpung is injured and Jeok is knocked away.",
    "The Blood Lord absorbs blood to replenish his strength; a wound in his palm remains unhealed.",
    "Taekyung’s spear pierces the Blood Lord’s wounded palm; the outcome is unresolved.",
    "Taekyung believes Hyuk Mujin is dead, though he did not witness his fate.",
    "Taekyung remembers an unfulfilled promise to Ju Hwaran."
  ],
  "continuity_sources": [
    1124
  ],
  "open_questions": [
    "Will Taekyung survive the remaining quest time and defeat the Blood Lord?",
    "Why can Taekyung evade the Blood Lord’s attacks with such precision?",
    "What effect will Taekyung’s spear thrust have on the Blood Lord?",
    "What happened to Hyuk Mujin?",
    "Will Taekyung ever fulfill his promise to Ju Hwaran?"
  ],
  "safe_through": 1124,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1120

# Chapter 1120

Boom!

The moment a low boom of breaking air rang out, it felt as if the whole world had stopped.

At least, that was how it seemed to the members of the Fire Dragon Pavilion who witnessed a palm, launched at lightning speed, strike a man in the chest.

And then—

Splatter.

As Hyuk Mujin’s body crumpled, scattering dark-red blood, the world that had stopped began to move again.

“No!”

Taishan’s eyes were bloodshot, and the muscles across his body swelled as if they might burst.

At the unbelievable sight before him, he let out a thunderous roar and charged toward the gate.

He forgot his exhaustion. He cast aside his fear.

Like an enraged bull, Taishan swung his two-section staff with all his strength and pressed forward.

Whoooosh! Wham!

Each time the furious wind rose, brains flew and bones shattered like powder.

Fanatics had taken the place of the monsters, frozen like statues at the death of the jiangshi sorcerer. They tried to stop him, but none of them could easily halt Taishan, consumed by an overwhelming rage.

No—more accurately, they couldn’t stop *them*.

KRRRUNCH!

A fierce rush of saber energy tore through the space, and severed limbs flew in every direction.

Amid the swirling spray of blood, Sama Pyo’s eyes—usually so composed—blazed with blue fire.

And someone else plunged into the dozens of fanatics closing in around Sama Pyo, heedless of their fallen comrades.

SHWEEEE!

The narrow-bladed sword cut through the air in quick, simple strokes—and with utter cruelty.

So much so that even the epithet Soul-Chasing Guest seemed inadequate.

Stab! Stab-stab!

Song Ilseom stabbed and twisted wherever he could.

With the most efficient movements, he dealt his enemies the surest pain and death.

Blood burst from a terrible scream and splashed across his face. Blades rained down indiscriminately from every direction, leaving cuts large and small across his body. But his tightly pressed lips didn’t tremble.

The blood flowing through Song Ilseom’s veins came from a noble family. But what had made him the Soul-Chasing Guest was the blood he’d shed on the battlefield.

Just as he had once left the path of the wandering martial artist he’d walked his entire life to repay his ancestors’ debt, now he was throwing his life away to repay the blood debt of his comrades.

He surrendered himself to pure rage, without a thought for the cost.

And Song Ilseom wasn’t the only one who felt that way.

“How dare you…!”

“You bastards are lower than this beggar!”

Sssshing! Slice!

Ju Hwaran, Gung Gibang, and the thousand defenders who had barely survived gritted their teeth and forced themselves to their feet.

Hope that they could win?

They’d long since erased that from their hearts.

Even if the monsters had stopped moving, fanatics remained—several times as many. And to make matters worse, tens of thousands of enemy reinforcements had appeared.

But hope wasn’t the only thing that could move people.

In that dark, bottomless despair, they had seen it clearly:

Hyuk Mujin, refusing to lose his dignity until the very last moment before he fell.

*The Fire Dragon Pavilion… No.*

His spirit hadn’t bent, not even before an enemy so powerful they couldn’t possibly oppose him.

*Swift Wind Sword Hyuk Mujin.*

CLANG-CLANG-CLANG!

At last, a thousand blades began to shine again, rippling like a wave.

They clamped their hands over severed arms and slashed-open bellies, bit their tongues to suppress their pain and fear, and rose with weapons in hand.

With all their strength, they cried out what might be their last words—the final trace of their existence in this world.

“Knife-and-Dagger Hero So Gyuhyeok is here!”

“Swift Blade Shakes the Heavens Mu Cheol is here!”

“Figures the orthodox faction would have such fancy titles. I’m Black-Killing Sword Jo Hyeok, you bastards!”

Orthodox faction, unorthodox faction, or masters belonging to neither—the gray area between the two.

Their roots, branches, and fruits might all have differed, but they shared the same great cause they sought to protect.

“Destroy the Demonic Path and restore Heaven.”

Destroy the Demonic Path and set the heavens right.

An old Daoist murmured the four characters they had shouted until they were spitting blood, back when they fought a hundred thousand followers of the Demonic Path. He tightened his grip on his sword.

Slice.

A body split into dozens of pieces along a streak of white light and scattered.

Leaving behind Black Ghost, who had finally met his true end, the old Daoist turned away. Then—no, Cheongheoja’s voice rang out, carrying the force of his internal energy.

“I miss those days. The time when you and I were ‘us.’ Don’t you agree?”

In Cheongheoja’s eyes, steeped in sorrow and anger, a huge figure stood before the ruined gate in the distance.

“Seafaring King Pa Ryun.”

The next moment—

“You haven’t changed, Cheongheoja.”

With a heavy voice that brushed over Hyuk Mujin’s fallen head, the master of the long, vast Yangtze strode out beneath the faint moonlight.

Two more unwelcome guests followed, hidden behind his imposing frame.

Unlike the mysterious figure dressed in black from head to toe, the short old man standing beside him had a familiar face.

“It’s been a long time, Cheongheoja.”

At the greeting offered first, Cheongheoja’s gaze turned cold.

“Right. You were there too. Green Forest Battle King Tae Gunak.”

“Such a sharp edge to your words. Last time we met, I believe you called me a fellow Daoist, not ‘you.’”

“Those days will never return. Not after the irrevocable choices some people made.”

Tae Gunak’s brow furrowed slightly as he looked around.

“I’m sorry things came to this. I mean that.”

“You mean that…”

Cheongheoja murmured hollowly, then drew up every last bit of his remaining internal energy.

Hummm.

As if sensing that his master’s end was near, the treasured sword that had been with him all his life trembled.

Not far away, Great Sir was still struggling against Black Ghost. But Cheongheoja’s senses and energy had already focused entirely on the unwelcome guests guarding the gate.

The opponents he had to bring down weren’t just the two giants who divided the underworld of the land between them.

There was also the mysterious man in black, who instinct told him was no weaker than either of them.

*He must be one of Dark Heaven’s key figures. But who?*

The question crossed his mind, but Cheongheoja could only smile bitterly.

Worry was ultimately a luxury for those who survived.

For an old Daoist who had to face three Supreme Peak masters alone, there was no point in worrying any further.

All he could do was resolve to meet his end without shame before those remarkable young people, still advancing as they cut down their enemies.

“Come, you thieves of the world. I am Cheongheoja of Kunlun.”

The old Daoist’s eyes flashed, colder than ever.

“Let’s finish this quickly.”

Along with a quiet voice that pierced everyone’s ears—

Rumble.

An enormous force began to churn around the black-robed man who had suddenly stepped forward.

Cheongheoja, charging forward with all his strength.

Great Sir, fleeing in haste from Black Ghost’s sword.

The Fire Dragon Pavilion members, fighting like mad as they cut through the fanatics, and the thousand defenders behind them, continuing their final stand.

Every one of them stared wide-eyed, watching in shock and dread.

A mighty explosion of force, painting their vision like the last sight of their lives.

SHWAAAA!

A single line—impossible to block, impossible even to see clearly—cut across the world.

* * *

“……!”

Why had his body suddenly gone rigid?

Where had this enormous rock come from, pressing down on his chest?

Jin Taekyung couldn’t tell what had caused it or why.

No—he didn’t want to know.

The moment he found out what this sudden feeling of dread meant, he felt the last thread barely holding him together might snap.

But despite that, Jin Taekyung’s gaze toward somewhere in the east, hidden behind enemies and buildings, had begun to tremble.

*This is…*

His vision was blurry, as though veiled in mist. His senses were as dull as an axe waiting out the winter. His entire body hung limp, like a waterlogged cotton ball.

Even so, he could faintly hear and feel it.

The enormous blast that had rung out far to the east. The sharp wave of power.

And it pointed to only one thing.

*The East Gate… has fallen.*

He wanted to deny it, to tell himself it couldn’t possibly be true. But it was no use.

Unlike the fire raging in his chest, his mind had gone cold. It faced the reality coming toward him head-on.

*It’s them. It has to be.*

Pa Ryun, the Alliance Leader of the Yangtze River Channel League. And Tae Gunak, the Alliance Leader of the Green Forest Alliance, his lifelong rival, considered Pa Ryun’s equal.

The two giants who divided the underworld between them had finally reached the battlefield.

And they’d brought a force of thirty thousand.

*…Then that means—*

With the thought in his mind left unfinished, Jin Taekyung raised his hazy eyes and looked around.

People leaned against the low walls of the Inner City, gasping for breath amid countless bodies and pools of blood scattered in every direction.

Among those who had retreated from the three sides other than the East Gate, some faces were familiar. But others had yet to appear.

*Why?*

Jin Taekyung wondered in a daze.

Why hadn’t they returned yet?

Even though he already knew the answer, he asked himself again.

*Right. So that’s how it ended.*

A weak, humorless laugh escaped him.

He thought of the faces he would never see again.

He felt the presence of tens of thousands of enemies surrounding the Inner City, and the monster leading them.

KWA-BOOOOM!

With a tremendous crash, the Inner City crumbled.
## Chapter artifact 1121

# Chapter 1121

Regardless of a wall’s height, size, or durability, whether it existed at all made a huge difference in a siege.

Even the shabbiest wall was still a wall.

And in that regard, Xining’s Inner City—built with the possibility of street fighting against foreign invaders in mind—had a considerable advantage in battle, even if it couldn’t compare to the Outer City’s walls.

It should have, anyway.

KWA-BOOOOM!

It all began in an instant, and ended in an instant.

At the hands of one man.

No—a monster.

Rumble.

As the Inner City wall crumbled amid a thick cloud of dust, a deafening roar like a scream, the Blood Lord laughed wildly.

To him, a man who prided himself on having gained power beyond human limits, the scene unfolding before his eyes was nothing short of laughable.

They should have scattered in every direction and run for their lives. And yet the best they could do was flee to the Inner City?

“Did you think a pile of rocks like that could stop me?”

With a low mutter, the Blood Lord raised the Red Blade once more.

Shhhhh!

A blood-red flash surged along its blade.

A massive half-moon of Force took shape in an instant, about to rip across the space between them—

“Stop!”

A voice suddenly rang out, urgent and sharp.

But even as someone appeared out of nowhere to stop him, the Blood Lord brought the Red Blade down without hesitation.

WHOOOSH!

The space turned red.

In a flash like a bolt of lightning, the Force swept across a distance of dozens of jang and sank into the dust cloud.

No—it swallowed it whole.

With a ferocity that could only be called monstrous.

KRRRUNCH!

Feeling the earth and sky shake with the deafening crash, the Blood Lord smiled smoothly.

Then he turned to look at the uninvited guest who had dared try to stop him.

“You’re late. You should’ve said something sooner. Then I might’ve stopped in the nick of time.”

At the Blood Lord’s almost nonchalant reply, the Grand Mage’s gaze turned cold.

“What have you done?”

“What does it look like?”

The Blood Lord shrugged and pointed with his chin at the distant cloud of dust.

“I was crushing their last hope. So they wouldn’t even want to resist anymore.”

“You…”

Her voice trailed off.

The Grand Mage stared silently at the still-smiling Blood Lord, unable to find the words. Then, at last, she asked in a calm voice about the one thing that mattered most: whether one person was still alive.

“So he’s still safe, right?”

“Safe? I’m better than fine. Look at me. Can’t you feel this power?”

The Blood Lord spread his arms with the innocent pride of a child showing off something to a parent. A chill crept into the Grand Mage’s chest.

He was different.

He’d changed.

Everything about him had changed.

His pupils, now completely blood-red. The unfathomable aura flowing naturally from his grotesque body, as if a human and a monster had been fused together. Those things had changed, but the greatest difference lay elsewhere.

Madness.

At that moment, the Grand Mage felt a bottomless madness whose depth and intensity she couldn’t begin to fathom.

And with it came the instinctive judgment that she must never let him know she’d noticed.

“Cut the pointless nonsense. You know better than anyone that’s not what I meant.”

“Now that’s disappointing. So something mattered more to you than the well-being of a comrade who’s in the same boat?”

“Since when were we so close?”

“Well, if you put it like that, I don’t have much to say. Fine.”

The Blood Lord let out an exaggerated sigh before continuing.

“Jin Taekyung’s still alive. Probably.”

“Probably?”

“Then let me correct that to definitely. There’s no way those old monsters still in there couldn’t protect one little brat.”

Even to the Grand Mage, it didn’t sound like an unreasonable guess.

Just fifteen minutes earlier, the defending forces had retreated at once from the walls on three sides, excluding the East Gate, and gathered in the Inner City. Among them were the Bow Saint, the Slaughter Saint, and the Fire King, Jeok Cheongang.

They’d all suffered serious injuries while withdrawing to the Inner City, but even so, their wounds shouldn’t have been severe enough to prevent them from keeping Jin Taekyung safe.

And as if to prove the Blood Lord was right, familiar faces appeared just then, beyond the thinning cloud of dust in the distance.

Including the one person who absolutely could not die—the most important one.

“……!”

The Slaughter Saint and Bow Saint were pale with exhaustion and Internal Injuries.

But the Grand Mage’s attention had already forgotten about them—and even Jeok Cheongang, who looked to be in worse shape than either of them.

There was only one person.

Jin Taekyung.

The moment she finally saw him, she let out the breath of relief she’d been holding.

There was no mistaking it.

He was covered in blood from head to toe, looking every bit the blood-soaked man he was—but Jin Taekyung was alive.

He could barely stand, using a white-glowing spear as a cane and leaning on Cheongpung for support. But that was enough for the Grand Mage.

She had the Lord of Heaven’s mysterious power: Magic.

Still, Jin Taekyung’s condition looked so grave she could sense his precarious state even from this far away.

*I have to take him to that person. As soon as possible.*

His injuries might be beyond even Magic’s ability to fully heal.

Just as the anxious Grand Mage was about to quietly recite a teleportation spell in her mind—

“What’s the rush?”

“……!”

At the Blood Lord’s low whisper, suddenly coming from behind her, the Grand Mage’s eyes widened before she could stop herself.

*How?*

If the core and root of martial arts was the accumulation of energy, Magic was a matter of attunement to energy.

That was why she was more sensitive than anyone to the fluctuations of energy.

Yet without seeing or sensing him, the Blood Lord had moved behind her and was smiling.

Like a predator with its prey already in its mouth.

“Magic really is an interesting power, the more I think about it. Being able to travel thousands and tens of thousands of ri in the blink of an eye…and bring back someone who’s half dead. Right?”

Feeling his hot breath against the back of her neck, the Grand Mage spat out her reply.

“I already told you. Cut the pointless nonsense.”

“Nonsense?”

The Blood Lord gave a short laugh and licked his lips with his red tongue.

“Sorry, but not this time. I don’t want to let prey I’ve already caught get away like this.”

Understanding what he meant, the Grand Mage gritted her teeth.

“Blood Lord, you’ve finally gone mad.”

“That’s strange. I could’ve sworn you’ve always called me a madman.”

“You dare go against that person’s will…?”

After a brief silence, the Blood Lord answered with a bright smile.

At last, he’d cast aside his mask and shackles. He was freer—and stronger—than ever.

“Why not? Just this once.”

At that very moment—

Slice!

A streak of red flashed. The Grand Mage’s hazy figure appeared three jang away.

And then—

SPLAAASH!

Her body staggered, spraying blood, then collapsed like a puppet with its strings cut.

Thud.

That was the end.

Her body lay in a pool of blood without so much as a twitch. Her eyes were frozen wide open, without a trace of life left in them.

“I wasn’t planning to kill her…but, well, can’t be helped.”

The Blood Lord muttered to himself, then looked around.

Countless eyes stared at him from every direction, in a silence that had settled over the scene. Tens of thousands of fanatics had surrounded the Inner City without leaving a single gap, and they watched this unexpected turn of events with wide eyes.

The Blood Lord spoke calmly to the fanatics, who couldn’t quite hide their agitation this time.

It was the shortest, surest method—one only Dark Heaven could use.

“By the command of the great Lord of Heaven, I have executed the apostate. From now on, I will command the entire army.”

“……!”

“……!”

“Kill them all. Every last one.”

The order finally broke the heavy silence.

Rumble!

With a roar that shook the earth and sky, tens of thousands of fanatics charged toward the Inner City.

To punish the wicked heretics who dared oppose the Lord of Heaven—the living god and sole absolute ruler.

Watching the fanatics surge forward like a giant wave, the Blood Lord laughed aloud and began to walk.

Toward taking the life of the one man he’d longed to kill for so long.

“Jin Taekyung—!”

The monster’s roar, imbued with an unprecedented aura, rang across the battlefield and swallowed it whole.

* * *

“……!”

“……!”

The air trembled. My ears were muffled.

Shouts and screams burst without pause from every direction. The bone-chilling clang of steel engulfed the battlefield.

But even through the chaos and my fading senses, I could feel it.

The warmth radiating from the people fighting countless enemies to protect me.

At the same time, I heard it.

The monster’s roar, steeped in joy and madness.

*Jin Taekyung.*

Right. That was my name.

The name I’d been given at birth.

Across two different worlds, I existed as one person—and two.

And maybe today was the last moment I’d been given.

*I have to go.*

I didn’t know where I’d found the strength.

My organs must have been twisted, and my Eight Extraordinary Meridians torn to shreds. With only a handful of internal energy, there was nothing I could do.

And yet, shrugging off Cheongpung’s support, I staggered forward as if in a trance.

Slice!

A stray blade grazed my shoulder.

Blood flowed—blood I hadn’t even known was still there—but I felt no pain as I reached out.

CRACK.

The fanatic’s gleaming eyes widened in pain.

He instinctively tried to wrench his wrist out of my grasp with all his strength, but before he could, a surge of scorching heat reached out and engulfed him.

BOOM!

To someone else, it might have felt like flames hot enough to burn them alive. To me, it felt like the warmest thing in the world.

Maybe because of who had saved me.

“El…der.”

Squeezing out every last bit of my voice, I grabbed Jeok Cheongang’s shoulder and whispered.

“A path. Please open a path for me.”
## Chapter artifact 1122

# Chapter 1122

The defenders at the backs of the collapsed walls fought more fiercely and more valiantly than ever.

After surviving against impossible odds and retreating to the Inner City, they numbered a little over five thousand.

Compared to the tens of thousands of fanatics blackening the land on every side, the gap was so vast that *a mere handful* seemed an apt description. Yet the last-ditch defenders who stood against them didn’t give an inch.

No—they couldn’t.

Behind them, beyond the rubble of the fallen walls, countless civilians trembled before the specter of death drawing closer by the second.

But even if there was nowhere left to retreat, that didn’t mean they could advance.

KRRRUNCH!

Flesh split, revealing white bone. Amid the red mist that swirled over the battlefield at the moment of impact, anguished screams and shouts rang out, muffled and dull.

“Graaaagh!”

“Hold the line! We have to hold—!”

Stab!

The shout ended with an axe blade cleaving through the crown of his head.

The man who crumpled to the ground had been a Peak master renowned as a hero of Qinghai for decades. But in this horrific melee, amid all this death, none of that meant anything.

And he wasn’t the only one.

The Sect Leader of a school. The Family Head of a household surrounded by relatives.

A young man whose downy cheeks hadn’t even lost their softness.

The moment the fanatics’ blind blades swept them up, they became nothing more than lumps of meat, collapsing to the ground.

CRUNCH! Stab-stab-stab!

Perhaps the outcome of this desperate final battle had been decided before it even began.

The exhaustion crushing the defenders had long since gone far beyond its limit.

Surviving this long in today’s battle was proof of their strength. But what lay before them couldn’t be overcome by sheer will.

Their remaining energy. The number of soldiers.

They were short on everything. Desperately short.

The dead rolled limply across the ground. Those still alive could only tremble on instinct as they watched the advancing enemy trample over the bodies of their fallen comrades.

They felt fear and anger, along with the helplessness of being unable to do anything.

Perhaps that was why.

When their bodies, their hearts, the whole world around them seemed to sink into pitch-black darkness—

A flame kindled by someone shone all the brighter.

Fwoosh—BOOM!

The air caught fire. Heat like the sun evaporated the rain and swallowed the fanatics whole.

At the heart of the fierce flames, surging forward in waves, stood a giant of fire, his burning eyes flashing.

“Who dares!”

With a furious roar, Jeok Cheongang, the Fire King, swept his sleeve.

The flames, whipped up by a fierce wind, melted steel and burned the fanatics’ flesh and bones.

“Stand in our way?!”

Jeok Cheongang had always referred to himself as “this old man,” but not this time.

He wasn’t walking alone anymore.

Now, they walked together.

Along the perilous, steep path to the brink of death that Jeok Cheongang had always been forced to walk alone, there was now someone at his side—a man who had become both a part of him and his whole world.

“Don’t retreat! Don’t be afraid!”

Supporting Jin Taekyung’s unsteady frame as he burned the enemies rushing in from every direction, Jeok Cheongang shouted with all his might.

The blades he’d normally have scoffed at and dodged grazed his body. Every time he summoned his internal energy, tangled acupoints sent pain blazing through him. But none of that mattered to him now.

“Open a path!”

It was a request from Jin Taekyung, his one and only Disciple.

A reckless request. One that might truly be his last.

But the old Master couldn’t refuse his Disciple, already standing at death’s door.

And this wasn’t the will of Jeok Cheongang alone.

Slice!

Dozens of heads shot into the air in a dazzling flash.

Jeok Cheongang swallowed the blood that suddenly surged into his mouth, then watched the sight with a faint smile.

“Took you long enough. You’re slow as hell.”

At the familiar reproach, the Slaughter Saint spoke, his face pale as a sheet.

He, too, had suffered serious injuries while fighting to hold back the Grand Mage and the Black Ghosts during the retreat to the Inner City.

“I couldn’t see the patient, so I went looking. Figured I’d drag him back by the collar.”

“And what do you intend to do?”

SHWICK!

The Slaughter Saint answered by bringing down his small knife.

His strike was as swift and precise as a ghost. The fanatics rushing in to fill the momentary gap crumpled like bundles of straw.

Just as his heart had crumpled when he saw Taekyung’s condition.

“Before it’s too late…I’ll take the lead.”

At the Slaughter Saint’s quiet reply, something tightened in Jeok Cheongang’s chest.

Perhaps the man could escape this battlefield right now.

He was the greatest assassin of all time.

That had to be why they called him the Slaughter Saint.

And yet Jeok Cheongang gritted his teeth, feeling something heavy press down on his heart.

*Before it’s too late.*

That was what he’d said. Clear as day.

Jeok Cheongang instinctively understood that this wasn’t a diagnosis from the Slaughter Saint, but from the Divine Physician.

And that the reply had held not the faintest hope, but despair.

*He’s going to die.*

A cruel truth too hard to believe, too hard to accept.

But as Jeok Cheongang stared blankly at Jin Taekyung, limp in his grasp as if unconscious, he clenched his fist.

There were no choices left for them now.

All they could do was give everything they had and kindle one last flame—perhaps their final one.

And even as they stood there, that flame was slowly growing larger and hotter.

SHWAAAA!

Force suddenly shot out from somewhere, spreading across the space.

Unlike the Slaughter Saint’s Force, so keen it seemed it could cut you just by looking at it, this web of Force felt as free as the wind. It wrapped around the enemies.

Calmly. Gently.

With a force so devastating it wiped away even that brief impression.

Slice—SPLAAASH!

A fountain of blood burst into the air.

Among the enemies crumpling to the ground, the Bow Saint appeared. Following the movement of her fingers, the broken bowstaff—split in two amid the fierce battle at the West Gate—moved with blinding speed.

KRRRUNCH!

Though it had lost its original shape, her bow had always been used in both forms: assembled, or separated into a pair of curved swords.

The Bow Saint swept through the fanatics like a storm, without a word. Close behind her, another familiar face appeared.

“Benefactor!”

Despite his urgent shout, Cheongpung’s sword technique moved as gracefully as a painter’s brush across white paper.

SHSHSHK!

A handful of purple Force, the color of sunset, sketched out flowers.

The dozens of plum blossoms seemed beautiful—until they touched the fanatics. Then they turned an even deeper red and bloomed in a glorious spray.

“Why’d you have to come along too…?”

The Slaughter Saint hadn’t even had time to stop him from plunging deep into enemy lines for this perilous journey when a roar from far away swallowed up the battlefield.

“……!”

“……!”

If a sound could take the shape of a giant, would it look like this?

The roar was so immense it shook even the eardrums of someone whose hearing had already burst. And there was a desperate, almost spiteful edge to it.

Everyone who turned to find its source could only stare, wide-eyed.

Jeok Cheongang and Cheongpung, wounded themselves, supporting Jin Taekyung as they fought off their enemies.

The Slaughter Saint and Bow Saint, realizing that the enemy reinforcements who had finally taken the East Gate had arrived.

And, walking slowly toward them as he scattered an overwhelming aura—

One man.

No, one monster.

“That’s…”

The words trailed off before they could be finished.

Watching the source of the roar with an indescribable expression, the Blood Lord suddenly burst into laughter.

“Pfft—hahahahaha!”

His booming laughter didn’t belong on a battlefield covered in a sea of corpses and blood.

But the Blood Lord didn’t care. He laughed like a madman.

Bent over, clutching his stomach, as if he’d never heard anything funnier in his life.

Then, as abruptly as he’d started, he lifted his head and looked over with a cold expression.

From far away came a host of people, shouting as if to pierce the heavens.

More pathetic and insignificant than any enemy he’d faced so far—and all the more infuriating for it. Those damn moths flying into the flame.

“What in the… Have I ever seen such a bunch of lunatics?”

The Blood Lord genuinely wondered if they had lost their minds.

Otherwise, he couldn’t explain the absurd sight reflected in his blood-red eyes.

But no matter how much he questioned it or thought it over, he couldn’t find an answer.

No—even if the Blood Lord gained the power of true immortality, he could never understand it.

That the old, the weak, and the very young—

The weak, born to spend their whole lives being trampled and trembling in fear, would risk their lives to protect someone.

He couldn’t even imagine it.

And yet they were still there.

They raised their voices, their faces set and their voices trembling, a mixture of desperate resolve and fear they couldn’t quite shake.

They gripped crude bamboo spears and rusty axes with all their strength.

They had spent their lives yielding to fate. Now they were defying it, trying to help those who had staked their own fates on protecting them.

Countless civilians, seeking for the first time in their lives to protect someone beyond their own families.

They were here.

Today. Right here.

“How—dare you!”

And then, as the monster’s roar, filled with an unprecedented aura, crushed the civilians’ seemingly endless shouts—

“…down.”

With a faint voice only a handful of people could hear, Jin Taekyung forced his eyelids open in his Master’s arms and struggled to speak.

“Would you shut up already…you son of a bitch.”
## Chapter artifact 1123

# Chapter 1123

“You…!”

Hearing that familiar voice tremble with agitation, I let out the breath I’d been holding.

I slowly blinked and swallowed the blood pooled in my mouth.

It was a strange feeling, unlike anything I’d ever experienced.

I felt hazy, as if I were trapped in a dream I could never escape. And yet, at the same time, everything around me came through with perfect clarity.

As for what this unfamiliar sensation was—the first I’d ever experienced—the System gave me a clear answer, as it always did.

In its uniquely kind and cruel way.

*Beep.*

> **System**
>
> **Status Effect:** Final Rally has been applied.

Final rally.

Like the sunlight that blazes just before the sun sets, the last flame burning at the edge of a life fading into darkness.

*So this is what it feels like.*

The thought came to me suddenly.

I remembered the final moments of all those people I’d personally brought down with these two hands—or desperately tried to hold on to, only to watch them leave anyway.

All the countless emotions I’d glimpsed in them.

At last, I felt like I could understand it all.

And I understood something else, too: unlike them, who’d waited for death as it slowly drew near, I was the kind of fool who had no choice but to run straight toward it.

*Ding.*

> **System**
>
> Final Rally is an act of divine mercy, a testament to human will, and a candle by which you may reflect on the life you have lived. Though its flame burns only briefly, that instant of light will shine so brightly that even death may be forgotten.

This time, it wasn’t the cold, harsh warning tone.

A clear chime, so familiar it rang in my ears, roused my body and mind from their endless plunge into darkness.

The radiant light the System had promised—a light bright enough to make me forget even death.

> **System**
>
> All pain you feel is greatly reduced for the duration of Final Rally.

The trembling of my body, groaning under the pain and death closing in by the second, came to a halt.

> **System**
>
> **Qi Sense** temporarily increases by a great amount.

A spark caught in the ashes of my cooling mind.

Fwoosh.

A sudden warmth pierced my back. The spark swelled into a flame.

> **System**
>
> Scorching Yang Qi cradles your exhausted body and heals some of your Internal Injuries.

Two flames could not coexist.

Someday they would clash and destroy each other.

But if they sprang from the same root, then they were originally one and the same.

Just like the person who, despite suffering severe Internal Injuries of his own, had given me his energy without hesitation.

“What are you waiting for?”

His face was as pale as paper. Great and small wounds were etched across his body, and his frame trembled.

But he—Jeok Cheongang—was smiling at me.

Trying to suppress the joy that his Disciple had recovered a little strength, along with the sorrow of what that meant.

“Come on. Let’s go. Together.”

At that moment—

*Ding.*

> **System**
>
> A sudden Quest, A Candle in the Wind, or a Flame, has been generated!
>
> Death awaits you. You cannot refuse this Quest!
>
> **Time Limit:** 9 minutes, 59 seconds

As time, which had stood still, began to flow again, I gripped White Flame tightly and took a step forward.

Into the nightmare that wasn’t over yet.

No—toward a reality worse than any nightmare.

*I’ll change it. I have to.*

If this had been a fight I had to face alone, I might have given up already.

I might have leaned my exhausted body against a pile of corpses, looked back on the time I’d left behind, and waited for death to slowly descend.

But—

SHWICK!

I wasn’t alone anymore.

KWA-BOOOOM!

Dazzling light-flames swallowed the enemies whole.

Amid the reddish, overheated earth and the shimmering haze that warped the air, a giant of fire roared.

At the same time, the Slaughter Saint, the Bow Saint, Cheongpung, and the last of the devoted defenders—

And countless civilians beyond counting, surging behind them like a wave.

Their cries were no longer angry shouts. They were shouting the name of someone none of us had expected.

“Charge! Charge! Protect the Marquis of Shangshan!”

“……!”

The great shout shook the battlefield and reached my ears. A streak of lightning shot up my spine.

They said they would protect me.

Me, of all people.

Those people, who didn’t have a scrap of internal energy or a proper weapon, who held sickles and pickaxes in their hands.

They were risking their lives for me—the man who hadn’t even managed to protect his own people.

*Right. In the end, I couldn’t protect you.*

As the beloved faces I would never see again flashed through my mind, I shot toward the fanatics.

SHWIIK!

The toes of my feet. My waist. My shoulder. My arms and wrists.

Following movements etched into instinct through countless repetitions and real battles, I split the raging wind and rain.

Slice!

A single, cool cutting sound swept through the air.

At the same time, more than ten pairs of eyes flew wide open.

The fanatics stared at me in disbelief, clutching their severed throats as they crumpled to the ground.

White Flame’s spearhead, trailing a faint heat, was slower and weaker than it had ever been. But for some reason, the enemies waiting in its path couldn’t react in time.

And neither could the next wave, surging in to fill the gaps left by their dead comrades.

Stab! Crack!

I stabbed through everything in my way, pulled my spear free, and twisted it.

My vision was still hazy, but my senses were sharper than ever.

So were the faces and voices that flickered past, one by one, through the thickening mist of blood.

*“I’ll join you. Just make sure the danger pay is generous.”*

A pair of fierce eyes, and the willow-leaf saber he always carried in his arms.

But despite his appearance, Song Ilseom had always been a reliable comrade and a good person to me.

He complained every time about how dangerous the missions were and how much extra pay he deserved, but Song Ilseom always fought in the most dangerous places.

He’d left behind the path he’d walked his whole life in order to protect someone. I was sure he’d kept that vow until his final moments.

*He must have. If it was the guy I knew.*

There was more to a person than what you saw.

That was true of a wandering martial artist others might have seen as nothing but rough and uncouth. It was true, too, of the two unorthodox faction members I’d unexpectedly formed ties with.

*Am I too late?*

That day in Gansu, when a battle like this one had raged, Sama Pyo had returned from staying with his father through his final moments and asked me that question.

I’d answered without hesitation.

No. You came right on time.

Every word had been the truth. Not a trace of a lie in it.

Even if he lost his way after agonizing over his choices and took a long detour, Sama Pyo was the sort of person who would find his way back to the right path in the end.

No.

*He was that kind of friend.*

With those words muttering endlessly somewhere deep inside me, I moved as if entranced.

SHWICK!

Like Song Ilseom, I rolled through a pool of blood to evade blades flying at me from every direction.

Slice!

Like Sama Pyo, I cut off my enemies’ breath with the cruelest, surest methods.

KRRRUNCH!

Like someone else who wasn’t here, I swept through everything in my way with an overwhelming aura as immense as Taishan.

*Taishan believes in Pavilion Master! Likes him second best in the world, after Lord!*

I pressed forward.

Listening to voices that rang like hallucinations amid flying screams and blood.

Seeing familiar faces laid over the enemies collapsing like bundles of straw.

*“Would you like to take a walk?”*

They rose like mist and passed like the wind.

The Fire Courtyard of the Yongbong Escort Bureau, shrouded in deep darkness, and the full moon, unusually bright and large that night.

*“Great Hero Jin.”*

The light, lively voice and the graceful, dancing steps, as if buoyed by drink.

*“Do you think…I can do it?”*

And the tearful eyes she couldn’t hide, no matter what she did.

*“Can I really do it?”*

I remembered it all, vividly.

Every bit of it.

Even when I made a pointless fuss about how bright the moon was that night, then fell silent at her unexpected question.

Even the moment I looked into her eyes, brimming with tears, and opened my mouth.

*“It’s all right if you can’t do it well. You don’t have to force yourself.”*

That night, I hadn’t been looking at the moon.

*“Wouldn’t that be enough, Young Lady Ju?”*

I’d been staring blankly at the eyes that shone brighter than the full moon and curved like a crescent moon.

Never imagining that a day like today would come, like the pitch-black Force rushing toward me right now.

WHOOOOOSH!

“Get out of the way!”

When had I gotten this far?

Jeok Cheongang’s urgent shout rang out behind me, deep in enemy lines, and a terrible whooshing sound swallowed the noise around us.

But I didn’t flinch.

More precisely, I didn’t have enough reason left to do so.

I simply stared at the two streams of energy that darkened even my hazy vision—so murky that they seemed less alive than anything else.

Not with my eyes, but with my senses.

No—with my heart.

And at the same time, in the gap between moments slowed to a crawl, I thrust out my spear.

SHWICK!

White Flame’s spearhead, wreathed in a faint blaze, cut through the air.

It pierced space, the darkness beyond it, and a single point.

Fwoosh!

“……!”

“……!”

The two streams of Force, which had seemed ready to swallow everything without a trace, scattered helplessly. I felt the air tremble all around me.

Destruction? A clash?

No.

The only word that could describe what had just happened was shattering.

Something so mysterious that even I, who had caused it, couldn’t understand.

So perfectly shattered that it enraged even the dead who had just fired Force at me.

—JIN. TAE. KYUNG!

The two Black Ghosts still standing cried out in unison and charged.

A ghostly horse leaped across the dozen or so jang of open air in an instant, casting its shadow over me. With its blood-red eyes flashing, the now-enlarged Force came crashing down.

KWA-BOOOOOOM!

The blast was so violent it shook my eardrums, already burst.

But I wasn’t the only one waiting where they were headed.

KWAANG! RUMBLE!

In the blink of an eye, four streaks of light collided in midair and swelled.

The compressed air exploded, and the earth overturned, unable to withstand the tremendous force.

At the heart of it were two superhumans who’d rushed to save me.

Stab! Crack!

The Slaughter Saint’s short knife and ox-hair needles, and the two curved swords clenched in the Bow Saint’s hands, stabbed and sliced through the Black Ghosts at lightning speed.

But unlike the Black Ghosts, the two Saints gritted their teeth, faces ashen, forcing out what little strength they had left.

The Black Ghosts refused to fall.

No. They recovered from not just mortal wounds, but even severed limbs, rising again after dying dozens of times.

Wooooong.

The air trembled.

Countless overlapping spells bolstered the Black Ghosts’ ability to heal, giving them even greater strength and speed.

Enough to face two of the Three Saints, who had fought more fiercely than anyone and were now pushed to their absolute limits.

“Go! Hurry!”

The Slaughter Saint’s urgent shout pierced my ears. The Bow Saint’s tired, lowered gaze touched my cheek, as if telling me to prove I was the one who’d been chosen.

Or that this wasn’t where I was meant to die.

*Right. I can’t fall here.*

I staggered forward, leaving them behind.

Following Jeok Cheongang and Cheongpung as they led the way, I cut down the enemies that appeared beyond my dreamlike, hazy vision, again and again, as I thought about a promise with someone that could never be kept now.

About the me who hadn’t been able to tell someone who’d become the greatest memory in the world to run away.

*“I’m Hyuk Mujin, Captain of the Gatekeepers of the great Jin Family of Taiyuan. State your identity and purpose for visiting… What? A pleasure house?”*

*“Third Young Master, I may be a low-ranking Captain, but let me say one thing.”*

Our first meeting had been a stubborn feud.

*“A scouting squad? Why me, Third Young Master…?”*

*“I’ll follow your orders. Captain—no, Captain, sir.”*

Before long, the two of us had fallen into step together.

*“Now, now, Captain. What’s there to worry about when you’ve got me?”*

*“Your heart! Your right arm! Trust Hyuk Mujin!”*

*“……Even so, isn’t your little toe a bit much?”*

And then we’d become inseparable.

So close that, at some point, we couldn’t even bear to be apart.

When I couldn’t see him, I missed him. When he was away, I worried about him.

My most trusted friend and subordinate.

That guy—Hyuk Mujin—had died.

In the end, I hadn’t even seen where or who had killed him.

*Even if he somehow survived by some miracle, I’ll never see him again.*

The last promise I’d made to him would never be fulfilled.

Because I would die first.

Because I’d have to leave behind the people I’d wanted to protect—or the people waiting somewhere for me, desperate for my return—and set off down a long road from which there was no coming back.

*But…!*

I gritted my teeth and let out the breath I’d been holding.

I swung my spear, tirelessly rekindling the dying flame.

Trampling the corpses piling up with each step and the blood spurting into the air, I moved as one with the people protecting me.

Toward the last and only path left to the living and the dead.

Toward the blood-red eyes I could sense with perfect clarity, even through my hazy vision.

KRRRUNCH!

The fanatics’ flesh and bones broke apart beneath the spearhead I brought down on instinct.

Beyond the fierce storm of blood, a monster steeped in blood and madness stood waiting.

“You should’ve been running for your life, and instead you’ve come right to me. I don’t know how to thank you.”

The Blood Lord, at last standing before me again, smiled broadly.

Or rather, at Jeok Cheongang and Cheongpung, already exhausted beyond measure, and me standing between them.

“Well, it’s time for you to die.”

Maybe he was right.

But—

*Beep.*

> **System**
>
> **Time Limit:** 5 minutes, 00 seconds

Not yet.
## Chapter artifact 1124

# Chapter 1124

*Beep.*

> **System**
>
> **Time Limit:** 5 minutes, 00 seconds

At the moment the second hand of the clock granted to only one person on this vast battlefield began to move—

*Flash.*

Space split apart.

It was erased, shattered.

And at its center, four figures were hurtling toward one another with all their might.

More precisely, one monster and the three humans standing against it.

And one of them was Jin Taekyung.

SHWAAK!

A horrifyingly low whistle of air pierced his ears.

A strike that split mountains, faster than sound itself.

The Red Blade came down at an angle, swift and fierce in equal measure.

Jin Taekyung wondered whether he could have properly seen that movement even in his usual condition.

Even if he had, he wouldn’t have dared to meet the enormous Force coiling around the blade head-on.

But his senses, honed sharper than ever at the edge of death, were guiding his still-warm body toward a path of survival.

*Rustle.*

The wind stopped. Time slowed.

In Jin Taekyung’s hazy pupils, like a sky clouded over, the blood-red blade and its blazing Force passed within a hair’s breadth of his face.

*Slice!*

Along the path that missed him by mere inches, the ground split as easily as tofu.

The wind pressure whipped around like a blade and tore at his body, but Jin Taekyung had already forgotten pain. As if entranced, he thrust out his spear.

SHWAAK!

The spearhead pierced straight through space.

At the same time, Jeok Cheongang’s Flame-Extinguishing Divine Fist and Cheongpung’s sword cleaved through the wind.

FWOOSH, SHWISH-SHWISH-SHWISH!

Two streams of flame surged forward as one, while violet Force, like the colors of sunset, scattered like flower petals.

Though their renown varied, each of the three Supreme Peak masters could make the entire Murim tremble on the strength of his name alone. Together, they launched a perfect combined attack.

But waiting for them was a monster that had already far surpassed the limits of humanity.

HWAASH!

An enormous energy boiled up in an instant.

At the same time, the Blood Lord’s hands—now both free of the hilt—struck through space like twin bolts of lightning.

KWA-BOOOOM!

Twin palms, faster than sound itself.

With a roar as if the sky had split, a blood-red flash erupted around the Blood Lord and swept in every direction.

An overwhelming, destructive force that made no distinction between friend and foe.

RUMBLE, RUMBLE……!

A deep reverberation surged through the devastated battlefield.

It swept over the countless fanatics’ corpses, now scattered as chunks of flesh, and reached the three men staggering back to their feet.

“They survived that?”

The Blood Lord muttered despite himself.

He had put tremendous power into that strike.

He had poured a third of his strength into a single attack.

It had been powerful enough to erase every living thing within a radius of over ten jang and turn the area into a hellscape where only death remained.

Of course, he hadn’t thought the outcome was entirely impossible.

No matter how grievously wounded and bloodied they were, a beast was still a beast.

Especially when even the weakest beast among them was called the Huashan Divine Dragon.

No—perhaps this was for the best.

If he’d killed them all with that last strike, he might have been left feeling empty.

“No. Not like this. Not so easily.”

It was just as the Blood Lord took a step forward, a low laugh escaping him.

*Rustle.*

A strange sensation came over him without warning.

He raised his hand to inspect it, and his gaze immediately turned cold.

Blood.

A bead of blood welled up through a shallow split in his skin—too slight to even call a wound—and ran across his palm.

From the very hand that had just met someone’s attack head-on.

“This is……”

The Blood Lord’s voice trailed off. Slowly, he lifted his head.

And saw him.

One man, covered in blood from head to toe, breathing hard as he steadied himself.

His face was so pale he could have collapsed at any moment, yet his eyes still held a flame that hadn’t died out.

*Jin Taekyung.*

The Blood Lord ran his red tongue over his lips.

How had this happened?

He’d been sure he had blocked the attack.

None of their strikes could have broken the Palm Force gathered in his hands.

And yet—

“Yes. This is how it should be. You ought to manage at least this much.”

The Blood Lord murmured softly, almost to himself.

The light that had dimmed in his eyes flared to life, and his wavering lips curled into a gentle smile.

At this moment, he was truly enjoying himself.

Carelessness? Fear of what might happen?

He’d felt none of that from the start.

He had simply been certain.

Certain that he could hunt the prey before him, whether it was a powerless rabbit or a beast hiding its fangs.

Though it had been only a single exchange, the Blood Lord had realized once again just how immense the power within him was at this moment.

And how boundless.

*Squelch.*

As the monster stepped forward, the pool of blood at his feet, spread out like a small lake, swirled and rushed toward him.

SHWAAAAA!

The Blood Lord greedily swallowed the blood. Intoxicated by his strength surging anew, the monster shot through space like a flash of light.

*Drip.*

A single drop of blood fell behind him.

* * *

The Blood Lord’s confidence was no arrogance.

He moved faster than anyone else on the battlefield, and the immense blood-red Force bursting from his Red Blade was enough to make anyone who saw it think of the word *unprecedented*.

At least at this moment.

He was the strongest predator on this vast battlefield, an absolute being no one could oppose.

With even the two giants among the Three Saints pinned down by the enemies’ fierce counterattack, he was powerful enough to crush the three Supreme Peak masters—each already seriously injured—in an instant.

And Jin Taekyung knew that better than anyone. Which was why he couldn’t understand what was happening.

SHWEEEE!

Why—

KRRRCH!

Why was that terrifying Force, powerful enough to split a mountain—

SHWAAK!

Why was the Blood Lord’s movement, faster than wind, sound, even light—

WHOOOOSH!

Missing him by a hair every time, every single moment?

Why couldn’t it touch him?

“You—!”

Jin Taekyung didn’t hear the monster’s voice echoing through the blade-sharp wind.

No. More precisely, he couldn’t hear it.

Amid flashes that constantly blurred his vision, he simply kept moving as if entranced.

*Slice!*

He brought his advancing foot back to where it had been, ducked his head, and let the blood-red Force pass overhead.

A flawless dodge, without a moment’s hesitation.

Jin Taekyung himself didn’t know how he could evade such a swift and ferocious strike. He didn’t know why he’d made that choice, either.

He just felt he had to.

It all seemed perfectly natural.

Like the sun rising in the east each morning, or water flowing downhill.

Like a duel whose every move had been carefully arranged in advance.

But that was true only for Jin Taekyung.

*Rustle, SHWEEEE!*

Just as the Red Blade, descending toward the crown of Jin Taekyung’s head, abruptly changed direction—

KWAANG!

With a single deafening crash, Cheongpung, who had rushed in to attack from the blind spot, dropped to one knee and spat up blood.

Above him, the Red Blade had wiped away the path of the Thirty-Six Plum Blossom Swords in an instant and crashed down like lightning, its weight pressing into his sword as if it weighed ten thousand geun.

CRACK.

The violet Force faded rapidly, and hairline fractures spread across the blade like a spiderweb.

As Cheongpung swallowed blood and summoned all his strength, the Blood Lord’s dark-red light poured down on him.

“You dare, you little—!”

The monster’s earlier delight had turned to anger.

Why? How?

With martial prowess this immense, and Jin Taekyung clearly dying, why couldn’t he finish this simple, certain fight?

And even when victory was all but decided, why did that damned brat before him keep resisting to the end?

Just as he had on that day at Mount Song, when he’d inflicted a humiliation that was like a brand upon the Blood Lord.

“Fine. I’ll kill you first.”

As the Blood Lord spat out the words, the blood-red Force swelled and surged into the blade.

Then—

HWAASH!

Feeling a wave of heat sweep in from behind him, the Blood Lord released the hilt without hesitation and thrust out a fist.

KWA-BOOOOM!

Two fists collided in midair.

White flames and blood-red Force charged at each other, each trying to devour the other.

But the difference in their power was already clear. Through the thick heat haze, the Blood Lord bared his teeth at Jeok Cheongang.

“Get lost, old man.”

*BOOM!*

Blood-red Force swallowed the flames. With an explosion, Jeok Cheongang’s body was sent flying helplessly and rolled across the ground.

Right where someone had been standing just moments before.

*…What?*

The realization came in an instant.

At the same time, an alarm rang in the Blood Lord’s mind, and a gust of wind cut through space.

*Fwoosh.*

A whistle of air so low and faint it raised goose bumps.

In time slowed to a crawl, the Blood Lord turned. Jin Taekyung’s figure was fixed in his blood-red pupils, thrusting out his spear with unfocused eyes.

“……!”

The Blood Lord couldn’t even manage to say the words *How?*

He couldn’t think about how he, overwhelmingly powerful as he was, had failed to sense the dying wretch before him as he crept closer to death by the second.

And Jin Taekyung was no different.

*Now.*

It was as if someone else, someone he couldn’t see, were whispering in his ear.

His vision was clouded white, and he couldn’t see a thing.

Time was running out. A horrible weariness—and an even stronger feeling of death—was seeping into his body.

*Shhk.*

Jin Taekyung thrust out his spear smoothly.

The shouts and screams of friend and foe, ringing out without pause even now. The cold clang of steel. The sound of a trumpet, now drawing close.

Even the palm the Blood Lord thrust out on instinct.

Nothing could stop him.

Leaving it all behind, as if it had been decided from the beginning, Jin Taekyung let the flames deep inside his body flow toward a single point.

*Thud.*

A spearhead carrying faint warmth pierced the palm wrapped in Force and drove through.

Past that very hand, whose wound, for some reason, had yet to heal.

KRRRCH!

The monster’s eyes flew wide, bulging as they filled with shock.

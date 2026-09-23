# Checkpoint Review — 905–909

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

# Chapters 905–909

## Plot

The imperial banquet battle intensifies. Jeok Cheongang clashes with Cang Gong, revealed as the Eastern Heaven Demon Lord, while Jin Taekyung kills Ma Sanbao and the Golden Ox Palace commander, who served the Lord of Heaven. The Emperor cannot intervene directly, and So Gyo says she is watching Taekyung; her identity and allegiance remain unclear. Jeong Hogun and the Embroidered Uniform Guard protect Taekyung and declare for the Emperor.

Taekyung uses the unknown power of his Middle Dantian to stop and redirect arrows, then turns to rescue Hyuk Mujin and the Fire Dragon Pavilion members from a large force of black-clad pursuers. He reunites with the group and unleashes Fire Dragon’s Single Tail, a devastating blue-white fire attack. The strike leaves him nearly out of internal energy and struggling to stand. As the smoke clears, the group sees something that may explain the pursuers’ urgency and Ma Sanbao’s confidence in the rebellion, but the chapter ends before it is identified.

## Continuity

- Taekyung is badly injured and nearly out of internal energy after using Fire Dragon’s Single Tail; he is struggling to stay upright.
- More than a thousand black-clad pursuers appeared to remain after Taekyung’s attack. Their identity, capabilities, and the scene revealed in the smoke remain unknown.
- Taekyung has killed Ma Sanbao and the Golden Ox Palace commander, a servant of the Lord of Heaven.
- Taekyung can use the unknown power of his Middle Dantian to halt and redirect arrows.
- Jeok Cheongang is fighting Cang Gong, the Eastern Heaven Demon Lord; the outcome is unknown.
- Jeong Hogun and the Embroidered Uniform Guard have declared for the Emperor and protected Taekyung.
- So Gyo’s identity and allegiance remain unknown. The Emperor and Cang Gong have not revealed all their forces.

## Translation Decisions

- Use “Eastern Heaven Demon Lord” for Cang Gong’s title, distinct from “Lord of Heaven.”
- Use “Twelve Palaces of the Zodiac” and “Golden Ox Palace.”
- Keep the five-spice pork joke’s contrast between “two hundred” and Taishan’s mistaken “one hundred two.”
- Use “Blazing Flame Divine Spear” and “Fire Dragon’s Single Tail” for 열화신창 and 화룡일미.

## Durable state

{
  "active_continuity": [
    "Taekyung has reunited with the Fire Dragon Pavilion members who were fleeing the black-clad pursuers.",
    "Taekyung used Fire Dragon’s Single Tail, the first form of the Blazing Flame Divine Spear; he is nearly out of internal energy, injured, and struggling to stay upright.",
    "More than a thousand pursuers appeared to remain after Taekyung’s attack; the group is still in danger.",
    "The scene revealed as the smoke clears may explain the urgency of Hwaran, Ilseom, and Sama Pyo and Ma Sanbao’s confidence in the rebellion, but has not yet been identified.",
    "Jeok Cheongang is fighting Cang Gong, the Eastern Heaven Demon Lord.",
    "Jeong Hogun and the Embroidered Uniform Guard are on the Emperor’s side and intervened to protect Taekyung.",
    "So Gyo’s identity and allegiance remain unknown.",
    "The Emperor and Cang Gong have not revealed all their forces."
  ],
  "continuity_sources": [
    908,
    909
  ],
  "open_questions": [
    "What is the scene revealed as the smoke clears?",
    "Who are the black-clad pursuers, and what are their capabilities?",
    "Who is So Gyo, and where does her allegiance lie?",
    "What is the nature of Cang Gong’s power and his relationship to the Lord of Heaven?",
    "What forces are the Emperor and Cang Gong still withholding?"
  ],
  "safe_through": 909,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 905

# Chapter 905

The torches wavered. Dark blood, visible even in the darkness, burst out in every direction.

*Clang-clang-clang!*

*Thrust!*

Well-honed blades met, flashing with swordlight.

And with them came cries of pain.

“Gyaaaagh!”

“Ghk, gah!”

With a dying cry that announced the end, someone nameless met their death, and someone else stepped into the empty space they left behind.

Again and again.

A cycle of death that would not end until one side was wiped out.

As if to prove the weight carried by those two words—Son of Heaven—the Emperor sat on his throne without so much as a tremor, watching the Grand Banquet Hall turn into a battlefield.

*It’s been a long time since I’ve seen a sight like this.*

He wore a dragon robe embroidered in brilliant colors now, but a little over a decade ago, the Emperor had been a general who strode across battlefields in armor.

The fourth prince of the Great Nation, with neither the prospect nor the desire to inherit the throne.

No one could have imagined that the man who led an army to crush border warlords and nomads would one day ascend the throne.

Not even he himself.

“Strange how things turn out. Truly strange. Wouldn’t you agree?”

At the Emperor’s sudden murmur, Commander Baek Yeon of the Embroidered Uniform Guard, who stood beside the throne like an iron tower, replied in a heavy voice.

“This subordinate failed in his duty.”

A full third of the Embroidered Uniform Guard, whose duty was to protect the imperial family, had turned their blades against their own side.

On top of that, the Imperial Guards responsible for the Outer Palace kept raining arrows down without pause.

The Emperor had not been entirely unprepared for the existence of traitors, but Cang Gong’s shadow had fallen far darker than he’d expected.

Over the imperial family—or rather, over the entire Great Nation.

*Shhh-shhh-shh—clang!*

Hundreds of arrows fired straight at the Emperor bounced off harmlessly.

The Emperor moved his lips toward the Embroidered Uniform Guard who had blocked the attack by forming a wall with their massive iron shields.

“Advance.”

It was a short command, but enough.

A hundred martial artists, handpicked from among the finest elite of the Great Nation’s greatest force, launched themselves forward without hesitation.

Not to stay beside the Emperor, but to charge into the battlefield stained with death and screams.

*Whoooosh!*

Dozens of yards vanished in an instant.

At the same time, a hundred spears and swords swung forward, blazing with dazzling light as they bore down on the traitors.

*Whiiing!*

*Slice! Thrust!*

“Gyaaaagh!”

Screams and blood erupted without pause.

The martial prowess of warriors at the very brink of the Peak realm—overwhelming, and horribly powerful.

But that alone could not turn the tide of battle.

At the center of this battlefield, true monsters who had surpassed the limits of human ability were rampaging.

*BOOOOM!*

*Rrrumble!*

A tremendous roar and tremor shook the area. Beyond a pillar of fire that surged high into the air, piercing the darkness, a painfully white light blazed.

*Shhk!*

Space split open.

Those who felt that frigid energy, like frost in the depths of winter, shuddered from head to toe as if on cue.

Then, watching their vision slowly tilt, they understood.

*Ah.*

That cold they’d felt at the end was death.

*Rrrumble!*

Dozens of corpses fell like rotten old trees.

Their armor, drenched in blood, no longer shone gold. The gray eyes looking down at them had settled into a cold gaze.

“Is that all you have?”

*Whump!*

A casual palm strike crushed a man’s whole body.

“The Emperor’s hunting dogs. The might of the imperial family.”

*Craack!*

A light stomp made the ground within dozens of yards ripple like a wave.

“Is that all you have? That’s what I asked!”

“Gwaaaah!”

The shout, filled with immense internal energy, burst through the compressed air.

It shook the bodies and minds hardened by grueling training, and tore at their eardrums.

“Ghk.”

Groans rose from all around.

Then, toward the Embroidered Uniform Guards who staggered, hands pressed to their bleeding ears, another white flash came hurtling toward them.

No—it was just about to.

*Fwoosh.*

Somewhere, flames flickered.

In the blink of an eye, the air that had been cold as ice began to boil like lava, soon swallowing even the darkness.

*BOOM!*

Would it sound like this if a volcano erupted?

Leaving that question in everyone’s minds, the burst of flame came pouring down toward one person alone.

An old man with pale skin.

Cang Gong’s gray eyes held every bit of that terrible heat.

*BOOOOM!*

Impact—and explosion.

The dreadful shock wave that followed hurled friend and foe alike through the air. Cang Gong was no exception.

*Shhhhh. Thud.*

His body was forced back by the immense power, but he managed to stop himself.

Straightening his back, which had bent at an angle, Cang Gong fixed his gaze on one man.

“When the situation demands you fight with everything you have, you waste your strength showing off against children. You must’ve eaten your age through your ass.”

Fire King Jeok Cheongang.

As Jeok approached through the heat haze rising all around him, Cang Gong’s lips twisted.

“And you’re no different. In the end, didn’t you earn the title of Fire King by killing countless weaklings?”

“Even without balls, a man should speak straight. The Demonic Cultists I killed weren’t mere weaklings. They were arsonists I wouldn’t have been satisfied with even if I’d burned them alive.”

“Then why did you kill the other Demonic Cultists? They had done nothing to you.”

“One day, I woke up to find my ancestral home going up in flames. How do you think that felt?”

Without waiting for a reply, Jeok Cheongang continued.

“Filthy. It felt like shit. So I kicked every last one of them in the ass and sent them to the afterlife. That way, even if they were reborn, they’d never set fire to someone else’s home again.”

“In other words, it was personal revenge.”

“That’s right. I didn’t like what those bastards were doing anyway.”

Jeok Cheongang raised a fist wreathed in rolling flames and added,

“Just like you.”

*Swish—BOOM!*

Thousands of soldiers filled the Grand Banquet Hall, but not one of them saw what happened.

How Jeok Cheongang moved. Or how Cang Gong evaded that terrifying attack.

But a tiny handful of people were different. They were more than worthy of being called superhuman.

“If I were in his place, how long could I last?”

In response to the Emperor’s question, as he watched every detail of the battle, Baek Yeon answered,

“A hundred moves.”

“You don’t hesitate to be cruel. Still, I’ve put in no small amount of effort to reach this realm.”

The Emperor wore a bitter smile. Baek Yeon replied without a change in expression.

“It would be the same for anyone. The only question is how long they could last. The outcome would not change.”

“Even if you went out there, Baek Yeon?”

“If I went as Commander of the Embroidered Uniform Guard, victory would be certain. If I fought as a single martial artist, I would lose by a hair.”

“Then what are you now—a martial artist, or the Commander of the Embroidered Uniform Guard?”

“This subordinate has always been the Commander of the Embroidered Uniform Guard. One who obeys only Your Majesty’s commands. And…”

Baek Yeon murmured in a faint voice,

“The late Emperor’s final order was to make plans for the future alongside the fourth prince.”

“……!”

The Emperor’s eyes trembled.

How could he forget?

That day. The voice he heard for the last time.

More than a decade had passed since then.

Frost had settled early on the head of the young man burdened with more than he could bear. The infant who had once been swaddled in blankets had grown into a boy, now sharing this very moment with him.

“What on earth—”

He struggled as if he might shake off the palace attendants’ hands at any moment and rush onto the battlefield.

“What on earth are you thinking?”

His eyes, filled with anger and confusion, were fixed on the Emperor.

“Why? Why won’t you help them? The people risking their lives for Your Majesty…!”

*BOOOOM!*

The rest of his words were swallowed by the roar that burst out with the flames.

The next moment, Prince Shangshan spotted a familiar face in another fierce battle across the hall—a man rising to his feet with a broken spear shaft for a cane—and let out a quiet groan.

“Jin Taekyung.”

He could recognize him at a glance, even from far away.

No. How could he fail to recognize him?

He was Jin Taekyung.

The first person to bring life to the young prince’s dull, unchanging days, and the only one to treat him as someone other than a prince.

Prince Shangshan Zhu Bao remembered clearly the day he first met Jin Taekyung.

“Could I become like you?”

And to that question, asked after much thought, Jin Taekyung had answered without hesitation.

“Of course. You can.”

Prince Shangshan truly wanted to be like Jin Taekyung.

Not simply because Jin Taekyung was a formidable martial artist.

He was amazed and envious that someone who had been no more than the family’s unwanted child had defeated one powerful enemy after another and won everyone’s affection.

Though he was a royal more honored than anyone in the world, the young prince had always been lonely. In one young martial artist, he had seen someone like himself.

A few days ago, that palm had gently ruffled his hair without a trace of propriety. He had felt a warmth he could never forget.

“I hope we meet again. Then I can repay the debt I owe you.”

“Your Highness.”

“Yes?”

“Don’t you know? Friends don’t owe each other anything.”

It was the first time.

The first time someone had called him a friend.

The first time someone had ruffled his hair as if he were an ordinary child.

That was why he wanted all the more to keep his promise. He wanted to return Jin Taekyung’s kindness, to repay what he owed him.

He was his one and only friend.

“Please, please save him.”

Prince Shangshan had no idea what was happening, or what lay behind this situation.

Still, he bowed his head and fell to his knees without hesitation.

Before his only blood relative.

He pleaded with the ruler of the continent, who could move several Supreme Peak masters with a single word.

“If there is anything you wish of me, I will do it. If you order your younger brother to leave the Great Nation, I will obey. But please, do not refuse this request from your brother—the first and last I will ever make of you.”

“……!”

“Save him. Save Jin Taekyung, Your Majesty!”

As the Emperor watched Prince Shangshan prostrate himself and cry out, an indescribable emotion crossed his face.

Relief. Pride. Perhaps even sorrow. At the end of that tumult of feelings, there was something he could never quite bring himself to say.

*Not ‘Your Majesty’… Wouldn’t you call me ‘older brother’?*

But no voice came through his parted lips, and despite Prince Shangshan’s plea, the Emperor did not nod.

No—he could not.

At least as far as everything happening on this battlefield today was concerned, he had already entrusted it to one person, more than a decade ago.

*No matter how I think about it, I can’t understand why you’re doing nothing, even in a situation like this.*

So Gyo answered the Emperor’s quiet Sound Transmission as it slipped into her ear.

*I’m not doing nothing. I’m watching.*

As she had from the beginning, she kept her gaze fixed on Jin Taekyung without the slightest sign of wavering.

*Until he shows his true self.*
## Chapter artifact 906

# Chapter 906

I didn’t know what to call this situation.

A melee?

A bloodbath?

Maybe both. Everywhere I stepped, I was trampling the corpse of someone I didn’t know, while enemy spears, swords, and arrowheads came hurtling in without pause, from the ground and the sky alike.

Even now.

“Look out!”

One of the Embroidered Uniform Guards heard my shout and jolted, twisting at the waist.

*Fffft!*

With a sharp whistle, his armor split open.

The traitor who’d tried to ambush him amid the chaos of battle missed by a hair. Without hesitation, I kicked a crescent blade lying on the ground.

*Whoooosh! Thud!*

There wasn’t even the usual dying cry.

The blade shot out like a flash of light, piercing its target and then skewering a couple of nearby enemies like meat on a spit. The Embroidered Uniform Guard, who’d barely escaped with his life, gave me a slight nod.

“Thank y—”

Then he never raised his head again.

*Thwack!*

An arrow pierced his throat, right through the windpipe.

Enemies rushed in, trampling the fallen guard’s body as he gurgled his last, and swung their weapons at anyone in reach.

All accompanied by a calm voice that had no place in a situation like this—which made it all the more chilling.

“Heaven above, earth below.”

“All demons bow in reverence.”

Why did it bring to mind the deranged fanatics I’d fought right before coming to Murim?

“Fucking lunatics…”

Short cries of dismay rang out here and there. The Embroidered Uniform Guards had continued fighting calmly despite the sudden betrayal of their allies, as if to prove the weight of the golden armor they wore. But even they looked afraid as they watched the traitors, who had become entirely different people.

Or maybe it was because of the martial prowess of someone who seemed impossible to defeat.

*Splash.*

A step forward, and his leather shoe sank into a pool of blood.

One of the Embroidered Uniform Guards had backed away without realizing it. A groan slipped through his lips.

“Ma Sanbao…”

That’s right. It was him.

Ma Sanbao, the East Depot’s Brush-Holding Eunuch.

Its second-in-command and de facto leader.

Or, to be precise, that was the identity he’d used to deceive the world. Now he was walking toward me.

So fast that “approaching” hardly did it justice—he moved like a flash of light.

*Whoosh! BOOM!*

His blows rained down like lightning from above. Every time I blocked one, my hands went numb.

My breathing had grown rougher than before, disrupting movements that should have flowed like water.

*Huff. Huff.*

I panted, wondering whether I was struggling this badly because I was in poor condition—or because I’d run into an opponent that formidable.

But even that thought didn’t last long.

*Shhk!*

The flexible sword curved like a living snake and grazed the bridge of my nose.

Hot blood welled through the split skin. I retreated, feeling a burning pain, as a low laugh crept into my ear.

“What happened to all that momentum you had at the start, hmm?”

Instead of answering, I turned my head. A dagger sprang from Ma Sanbao’s voluminous sleeve and pierced the empty space beside me like a streak of light.

*Thwack!*

Another life vanished with a sickening sound.

And then Ma Sanbao’s voice continued as if nothing had happened.

“That’s a shame. If you hadn’t dodged, that young Embroidered Uniform Guard would still be breathing.”

I looked at Ma Sanbao, who was taunting me, and wondered:

If I hadn’t dodged, would he have survived?

Could he have made it through this battle and returned to his family someday?

I didn’t know. I knew nothing.

The pointless guilt made me feel like shit. Even though the only person who should feel sorry for that guard, whose life had just ended, was someone else.

*Why…?*

I wanted to turn and look. I wanted to stare straight into the eyes of the Emperor and So Gyo, who had thrown me, Jeok Cheongang, and even their own subordinates into this battlefield, only to stand by and watch. I wanted to ask them:

Why had they held this damn banquet?

Why weren’t they acting, even though they had the power to turn the tide?

“Why the hell?!”

The one who answered my shout, which I could no longer hold back, was neither the Emperor nor So Gyo. It was Ma Sanbao.

“Do you still not understand why they’re standing by and doing nothing?”

He let out a derisive laugh and continued.

“Blazing Flame Divine Dragon Jin Taekyung. You were used by the Emperor in the end, too. Just like we tried to use you and the Fire King to get rid of So Gyo.”

“……!”

“Borrowing another’s blade to kill. There’s no better weapon than someone else’s when you don’t want to get blood on your own hands. Especially a fine sword like the Fire King and the Blazing Flame Divine Dragon.”

I wanted to tell him to shut his damn mouth.

But despite how badly I wanted to deny it, I couldn’t bring myself to speak.

Because it was plausible enough.

If the Emperor was anything like the man I’d experienced firsthand…

And if that woman, So Gyo, whose identity I couldn’t make head or tail of…

“The only role left for you and your Master is to fight desperately until you die. And then, in the end, to die.”

*Whoosh-whoosh-whoosh!*

With a sharp whistle, the flexible sword multiplied into dozens of blades, coming at me from every direction.

A sword technique at the limit of speed—so fast it seemed to have reached the very edge of what was possible.

But no matter how many afterimages crowded around me, there was only one real blade.

*Clang!*

A tremendous clash—too loud to believe it came from nothing more than two weapons meeting—sent me sliding back.

As the flexible sword kept swinging without pause, pressing its advantage, Ma Sanbao’s voice continued from beyond the blade.

“The Great Nation, the Emperor—it’s always been like this. To the rulers who hold this vast land, people like you and me, people of Murim, aren’t subjects to govern.”

*Whoosh-whoosh! Slice!*

The pressure of the sword split my skin. Thin streams of blood slipped through the cuts and scattered into the air.

“That’s why I followed my Master and pledged my loyalty to that person. And it’s why you’ll die here today. The Emperor wants to protect Prince Shangshan, nothing more. He won’t bring out even the hidden cards he’s kept in reserve just to save a pack of Murim ruffians.”

“What?”

At a realization that flashed through my mind, my eyes widened.

Even though there was considerable distance between us, I suddenly thought of someone fighting a thunderous battle alongside Jeok Cheongang far away.

*Could it be?*

No, not “could it be.”

Ma Sanbao had said it himself. This wasn’t a guess. It was a certainty.

*Krrrrang!*

Different kinds of Force struck each other and spat sparks.

Originally, it had been one weapon. But under Ma Sanbao’s fierce assault, it had split into two short spears. I crossed them to block the flexible sword, and felt the chill flowing from the blade, which stopped right in front of my face.

“Cang Gong. Were you his disciple?”

“Cang Gong? How dare you call him a servant of that sinister, weak Emperor?”

Ma Sanbao twisted his lips and continued.

“Eastern Heaven Demon Lord. That is the new name the great and all-powerful Lord of Heaven bestowed upon his loyal servant.”

“……!”

“And it’s the disciple of that very Eastern Heaven Demon Lord who will make you kneel.”

At that moment—

*Whirr.*

The blade of the flexible sword bent, its length coiled with the weapon’s natural spring.

Like a living snake, it slid over the spear shaft blocking its way and darted in as a flash of light. I saw it coming and swung my crossed short spears upward with all my strength.

*Clang!*

The flexible sword, which had been rushing toward my chest, veered off course.

But I’d only survived a dangerous moment. The attack wasn’t over.

*Wham!*

*Hk!*

My breath caught, and my vision flashed.

A fist struck my exposed chest. I staggered back more than ten steps in a row, and Ma Sanbao saw his chance. It was one he couldn’t afford to miss.

*Tap.*

Just one step.

At the same time, Ma Sanbao’s figure vanished like an illusion.

Yet even with my dulled senses and battered body, I reacted quickly.

*Left!*

The instant I was sure, I flung one hand out.

Even though splitting it in two had cost it its original advantage of long reach, it had gained a length and speed perfectly suited for throwing. I hurled it with tremendous force.

*Whoooosh!*

A single fierce whistle ripped through the air.

And at its end, a massive impact rang out.

*BOOM!*

Dust that had settled on the ground billowed up with the explosive sound.

Then—

*Shhhhk!*

Space split open.

The flexible sword that had knocked my short spear aside released a brilliant Force. It sliced through the cloud of dust and came at me.

Along with a taunting Sound Transmission that could only have been Ma Sanbao’s.

—Don’t worry. I’ll only cut you enough to leave you barely alive.

And that was his mistake.

In a slowed-down world, I was clearly watching the dozens of sword-images raining down to cover the air once more.

*Cut me? And only enough to leave me alive?*

That was ridiculous.

He was running his mouth like that while his opponent was still standing on two perfectly good legs.

The victor of a life-and-death duel had the right to spit on his opponent. He could boast about his strength and laugh in their face.

But…

*That’s what you do after everything’s over.*

My body was heavy as waterlogged cotton. The internal energy that usually surged in like a wave was faltering, strand by strand.

But it didn’t matter.

My eyes—and the hand gripping the one short spear I still had—hadn’t wavered.

*I see it.*

*Shwoosh!*

The spear tip pierced one precise point, wiping away dozens of sword-images as it met the real blade.

*BOOM!*

The impact sent the figure flying, unable to withstand the force of the collision.

Not me.

Ma Sanbao.

*Crunch.*

The tip of his foot dug into the ground as he planted it with all his strength. He barely steadied his swaying body and stared at me, eyes wide.

*Tap.*

By then, I was right in front of him.

“You bastard!”

Ma Sanbao’s flexible sword cut through the air with a scream of its own.

Its speed was more than worthy of being called extreme.

He scattered Force like a glacier—colder and more merciless than even that.

*Shwoooosh!*

Before that force, which seemed capable of freezing everything solid, I drew on every last bit of internal energy in my body.

*Fwoosh.*

A flame caught in wet firewood.

I poured the Scorching Yang Qi that surged like fire through my acupoints, as unstable as twisted railway tracks, into my hand and grabbed the blade just as it began to pierce my side.

*Krrk, KRAAAASH!*

Power collided with power.

At the same time, horrible pain shot through both hands.

It wasn’t Empty-Hand Seizes the Blade, catching a weapon between bare fingers with the precise timing and speed required.

This was just a brute-force grab.

“You crazy—”

No martial artist could blame Ma Sanbao for saying that.

This really was crazy.

Unless your opponent was at least a level below you, trying something like this against a master of similar skill—

And especially one with greater internal energy—

Would get both your arms cut off in an instant.

But…

*Things are different if the lunatic doing this has been busting his ass to raise his Muscles and Bones through the System.*

If my other stats were blue-chip stocks, then Muscles and Bones were a savings account that had steadily built up every time I leveled up or trained.

So what about now, more than a year after I’d gotten the System?

*What level am I again?*

I smiled.

I endured the horrible pain as my palm turned into a shredded mess, and looked into Ma Sanbao’s eyes, bulging as if they were about to burst.

Then I returned his earlier words with only a couple of words changed.

“Don’t worry. I’ll only stab you enough to kill you.”

“……!”

Ma Sanbao tried to shout something, but no sound came out.

*Krrk!*

Just as his lips began to part, the short spear in my hand pierced his throat.

“Ghk. Kgh.”

His eyes dimmed as he stared at me, while blood bubbled in his throat.
## Chapter artifact 907

# Chapter 907

I won’t say the fight with Ma Sanbao was fiercer and more difficult than any I’d ever fought.

There had been plenty of stronger opponents in the hellish battlefields I’d fought my way through. Even now, I could name several who’d been far worse than him.

But one thing was certain: today, Ma Sanbao had been stronger than me.

*No. More precisely, I was weaker than usual.*

The System was practically sealed, and my body—wrecked by the aftereffects of One Annihilation—wouldn’t move the way I wanted it to.

And yet, at this very moment, I was the one standing on two feet.

In this merciless world ruled by the law of the jungle, Ma Sanbao had made a mistake. A small one, but a fatal one.

He’d mistaken himself for someone a step above me.

“If you wanted to take me alive… you should’ve come at me ready to kill me from the start.”

I whispered as I looked into Ma Sanbao’s hollow eyes. Then I drove the short spear through his throat even deeper.

*Squish. Crack.*

Bone fragments burst through his skin with a sickening sound.

Only after the spear had severed his carotid artery and slid along his collarbone to somewhere near his heart did I let go. At last free of my grip, Ma Sanbao’s body slowly tilted over.

Along with the spear buried deep in him like a tree root.

*Thud. Splash.*

There was no System message saying I’d defeated an enemy. No clear, familiar chime, either.

But this was enough.

*Finally. One down.*

I stared at the corpse lying motionless in a pool of blood, panting, then let out a shout charged with internal energy.

“Jin Taekyung of the Jin Family of Taiyuan has killed Ma Sanbao, Brush-Holding Eunuch of the East Depot!”

Before anyone could even grasp what that shout meant, I charged back into the battlefield, where swords and spears clashed.

*Whoosh! Thud!*

Short, simple movements. Only the bare minimum of internal energy.

I dodged, struck, and smashed.

*Crack!*

The face of a man muttering those eight words like a mantra—“Heaven above, earth below. All demons bow in reverence”—caved in.

*Whsssh!*

I jerked my head aside, avoiding the blades that flew in from both sides of the collapsing corpse, its features mangled beyond recognition.

*Clang!*

The two blades that had missed me by a hand’s breadth struck each other. Ignoring the vibrations reaching my ears, I thrust out my hand, its grip torn to ribbons.

*Boom!*

Compressed air, heated until it glowed, burst outward.

The Flame Divine Palm I unleashed held only three-tenths of my internal energy. Even so, the force and heat packed into that palm strike were enough to kill all but the most exceptional Peak masters on the spot.

“Gah—!”

The man’s body flew backward, spraying dark red blood.

But whether that nameless enemy lived or died was no longer my concern. What he’d left behind was another matter.

*Tap.*

The sword had already slipped from its owner’s grasp. I caught the hilt smoothly and swung it in one motion.

*Shhhh!*

Space split open. Flames coiled around the blade, scorching the air, flesh, and bone.

Simple, but fast. And so powerful it couldn’t be stopped.

At the end of it were the enemies’ blood and screams.

*Fwoosh!*

“Gaaah!”

I pushed forward, drenched in blood spraying like a fountain. I dodged the countless blades crashing in from every direction, knocked them aside, then sent them flying right back where they came from.

When the sword broke, I used a spear. When the spear snapped, I used an ax or a dagger.

If I had nothing else, I used arms and legs harder than steel.

*Grit!*

*Boom!*

I broke the bones and crushed the flesh of every enemy in my way.

There was no need to reach for some grand concept like all streams returning to the sea.

Every weapon in the world had been made to fight more efficiently. Martial arts existed for the same reason.

Stab. Slash. Strike.

To me, martial arts were a chain of points and lines.

If your life was on the line, you used every means at your disposal.

If it could kill the enemy as quickly and reliably as possible, the shape of the weapon didn’t matter.

Just like now.

*Cr-rack!*

A corpse collapsed, its neck bent at an unnatural angle.

The enemies kept pouring in, their lips endlessly murmuring those mantra-like words, no matter how many I killed. But I could see the emotion rising in their eyes.

*Fear.*

*Huff. Huff.*

I struggled to suppress my ragged breathing. Every muscle in my body throbbed as if I’d been electrocuted, and the hand that had gripped Ma Sanbao’s sword could barely feel pain anymore.

After pulling something that crazy, I was probably in terrible shape.

But I couldn’t show even the slightest weakness.

Wolves hunted in packs, but no matter how hungry they were, they couldn’t bare their teeth at a lion that roared and charged at them.

They only tried to sink their teeth into a lion’s nape when it started backing away.

*Splash.*

My heavy footstep sent the blood pooled around my ankles rippling.

Like the blood still seeping from the countless wounds carved into my body, the blood reflecting the night sky was dark red.

*Can I do this?*

Suddenly, I felt exhausted to my very bones.

I’d killed well over a hundred of them, by my rough count, and still the enemies filled my field of vision.

The Great Nation’s—no, Dark Heaven’s—elite troops. Every one of them was at least Supreme First Rate, some nearing the peak of Peak.

I had to defeat them all, every last fanatic who worshiped the Lord of Heaven, before I could reach Jeok Cheongang, who was still fighting a thunderous battle that seemed like it would never end.

*Goddammit.*

I didn’t know.

Even as we gained the upper hand without the Emperor’s help, why did one corner of my heart keep trembling with unease?

Why did that storm-clouded night sky feel so ominous?

No. I did know.

*This isn’t over.*

No matter how I looked, I couldn’t see them. The assassins who should have been protecting the Emperor. The twin Supreme Peak masters who’d served as the gatekeepers of Qianqing Palace.

Even the Embroidered Uniform Guards in this great banquet hall numbered only half as many as I knew to be here.

*And it’s the same for Cang Gong.*

The Emperor and Cang Gong.

The two men had crossed a point of no return, yet neither had revealed all their forces. No doubt they were holding back their cards, waiting for the other to make the first move.

Even if the entire imperial capital had split in two by now, locked in a bloody battle, I wouldn’t have been surprised.

*Fuck.*

This was a shitty situation.

But even so, I had to fight.

I had to survive.

I had to survive the Dark Heaven dogs charging at me beneath a rain of arrows—and the Emperor and So Gyo, whose allegiance I couldn’t even guess.

*What the hell are you planning?*

I turned my head and looked at the raised platform in the distance.

Baek Yeon and So Gyo.

The Emperor was watching the battlefield with those two Supreme Peak masters at his sides, each powerful enough to turn the tide of the battle in an instant.

I also saw Aehyang, surrounded by a handful of palace attendants, and the young king, kneeling for some reason.

For just a moment, my attention was drawn to them. Then the countless whistles that had crossed the sky belatedly reached my ears.

*Whoosh-whoosh-whoosh-whoosh!*

A thick darkness spread over my head.

Hundreds of arrowheads flashed as they fell, all aimed at me alone. At the same moment, a red alarm bell rang violently inside my head.

*Shit.*

I knew before I even moved.

Dodging all those arrows was next to impossible.

I was already exhausted. My body and senses had grown sluggish, and I was stranded in far too open a space to avoid every arrow shot by First Rate masters using their internal energy.

*I have to use as little strength as possible and avoid a fatal injury.*

I clenched my teeth, pulling an abandoned spear from the ground as I raised my remaining hand toward the sky.

*Whummm.*

The air surrounding me trembled.

I’d avoided using my Middle Dantian except in the most dangerous situations, even during battle, to conserve my stamina. But now wasn’t the time to be picky about what was bitter and what was sweet.

Even if it was bitter, I had to swallow it.

I had to bear it myself.

There was no way in hell I was going to fall here, of all places.

Just as I clenched my fist, ready to meet the arrows hurtling toward me with a ferocious whistle that seemed to tear through my ears—

“Shield formation! Defend!”

At a familiar shout from somewhere, a group rushed in at lightning speed and surrounded me.

They held up massive shields.

*Bam-bam-bam!*

Sparks lit up the darkness. Countless broken and splintered arrow fragments scattered in every direction. A second rain of arrows came moments later, and dozens of crescent-bladed polearms flashed toward them.

“Slash!”

*Whoosh-whoosh-whoosh! Slice!*

Blade Force spread across the sky in brilliant half-moons.

The powerful energy formed a kind of barrier, slicing apart every arrow that flew toward them. The scattered fragments couldn’t pierce the gaps in their golden armor.

*Clatter. Thud-thud-thud!*

Countless fragments lost their momentum and fell.

I watched in silence, then spoke to the familiar face beneath a helmet pulled low.

“Should I thank you for that?”

Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard, answered without a hint of emotion.

“I didn’t know you knew how to say thank you.”

“I don’t do it very often.”

“I figured as much. I wasn’t expecting it in the first place.”

“What about you?”

“When I owe someone a debt, I say thank you. Like now.”

*Clank.*

Jeong Hogun struck his golden armor with a military salute, then continued.

His tone was different now. Respectful.

“Thank you for helping His Majesty. And us.”

“……Huh.”

“I’m sure you have plenty to ask me, and plenty you want to say. But I’d like you to save it until after this is over.”

Goddammit.

If he came out with something like that before I could even open my mouth, there was nothing left to say.

I clicked my tongue quietly and looked toward the enemies pressing in from all sides.

“Hey, let me ask you one thing.”

“Anything.”

“That guy over there playing peeping Tom—is he on our side?”

Jeong Hogun flinched at “peeping Tom,” then nodded.

“At least His Majesty is. We are on your side.”

*At least?*

I immediately understood why he’d gone out of his way to add that qualifier.

*So not So Gyo. No—more precisely, he doesn’t know, either.*

There was no doubt.

Even Ma Sanbao, who was no longer among the living, and Cang Gong seemed not to know.

Who that mysterious woman was, or what she had in mind.

And unknown variables like her meant danger.

*…Shit. Good thing I left the kids behind.*

I muttered to myself and raised the ownerless spear I’d picked up moments ago, aiming it at the enemies surging toward us.

I thought of the Fire Dragon Pavilion members who were probably waiting somewhere safe, expecting the Murim Alliance reinforcements that weren’t coming.

They’d probably make a huge fuss later, parroting “Captain” over and over. Still, if they’d stayed here, they’d have been dead by now. Or at least, it wouldn’t have been surprising if they were.

“Captain!”

“……?”

“Captaaaain!”

What the hell?

I turned around, feeling as though I’d been possessed by a ghost, and spotted familiar faces appearing in the distance.

“Captaaaaaain!”

More precisely, I saw Hyuk Mujin at the head of the Fire Dragon Pavilion members, hollering at the top of his lungs.

*Rumble-rumble-rumble!*

And countless black figures trailing behind him like a tail.
## Chapter artifact 908

# Chapter 908

For a very brief moment, every thought in my head ground to a halt.

*What the hell is this?*

I stared, mouth hanging open, at the scene in the distance.

The Fire Dragon Pavilion members were running toward me, panic written all over their faces.

And a group was charging after them at full speed.

*Rumble, rumble, rumble!*

The ground shook. The figures were dressed in black from head to toe, and even the ones I could see right then numbered well over a thousand. The more clearly I felt their chilling aura as they drew closer, the more obvious one thing became.

*Enemies!*

A red warning light flashed in my mind at the same moment I reached that conclusion.

*Shit.*

I had no idea what was going on, but what I needed to do now was clear.

The battlefield had fallen into a momentary lull at the appearance of the unknown black-clad figures. I shouted into the quiet.

More precisely, I shouted at the Embroidered Uniform Guards.

“Quit standing there with your jaws hanging open and pick up your weapons!”

Of course, I didn’t expect the Embroidered Uniform Guards to obediently follow my orders just because I’d given them. But right beside me was a man of high standing—a Thousand Captain of the Embroidered Uniform Guard, no less.

“Rally! Rally immediately!”

As Jeong Hogun’s shout roused the battlefield, I channeled my internal energy and kicked off the ground.

*Boom!*

Flamefire Path.

Flames burst from my toes, scorching the air.

Riding the shock wave from the explosion, I took a step, then another. In an instant, the distance of twenty-odd *jang* vanished, and the shadows atop the stone wall drew near.

The Imperial Guards.

Along with the Embroidered Uniform Guard, they were one of the Great Nation’s elite forces, charged with protecting the imperial capital. They were also traitors who’d betrayed the Emperor and taken refuge in the shadow of the Eastern Heaven Demon Lord, who had lived behind the guise of Cang Gong.

The archers who’d hidden behind the towering stone wall and fired arrow after arrow had now turned their bows toward the Fire Dragon Pavilion members, who had appeared behind them alongside the black-clad figures.

At least, that was where they’d been aiming before I arrived.

“General, your orders!”

At the urgent call of someone who looked like a junior officer, a middle-aged man in ornate armor swung the baton in his hand without hesitation.

He swung it at me as I closed the dozens of *jang* between us in an instant.

“Loose!”

The order came after a brief moment of hesitation.

*Thwang-thwang-thwang! Fwoooosh!*

A full thousand archers turned and released their taut bowstrings.

Countless silver arrowheads, imbued with internal energy, blanketed the sky as they came raining down on me.

A near-perfect volley, with enough power that even a Supreme Peak master couldn’t afford to ignore it.

But…

*If they don’t hit their target, they’re useless.*

*Boom!*

With another burst of flame from my toes, I shot forward like a cannonball.

A sudden burst of speed. Then a swerve.

*Thup-thup-thup-thup!*

A fierce, chilling whistle of arrows rang out behind me.

I didn’t bother looking back, but I could tell from the sound alone that the spot where I’d stood a moment ago was now covered in arrows.

And I knew the Imperial Guards, one of the Great Nation’s elite forces, wouldn’t stop attacking after just that.

“What the—!”

“Don’t lose your nerve! Loose!”

Their surprise at my speed lasted only a moment. The Imperial Guards under the commander’s control had been trained thoroughly. They nocked new arrows and loosed them in a smooth, swift rhythm.

*Fwoooosh!*

Once.

*Thup-thup-thup!*

Then again.

“Fire! I said fire!”

“Begin staggered fire!”

*Thwang-thwang!*

And just as I narrowly evaded the fourth rain of arrows, shot in two successive waves—

*Bang!*

I kicked off the ground and shot into the air. The Imperial Guards were already nocking the fifth and final volley when their screams broke out.

“H-He’s coming!”

“Loose! Loose!”

It all happened in the blink of an eye.

The four volleys had been fired in barely any time at all. And I’d crossed that thick storm of arrows to reach the top of the stone wall just as quickly.

In the world that had slowed to a crawl, a few of the most alert Imperial Guards had reacted to the order and loosed their arrows at me. The arrows cut through space.

Very slowly. Slowly enough that I could hear the wind rushing along each advancing arrowhead.

*Whoosh.*

I reached out toward the dozens of arrows flashing in the darkness, each imbued with internal energy.

At the same time, I stirred my quiet heartbeat—the pulse I alone could sense at the very center of my chest, in the spot called the Jade Hall.

*Stop.*

At that instant—

*Whoooosh!*

An invisible force—an unknown power on a completely different plane from internal energy—spread out in every direction at my will.

It erased the wind, stilled the air, and caught the dozens of arrows moving sluggishly through it.

*Rrrrrumble.*

The air trembled. Time, which had slowed, returned to its normal pace.

But the Imperial Guards looking up at me, standing upright in midair, could only stare, their faces frozen in shock.

“Th-This is insane…”

The groan that slipped from someone’s lips broke the heavy silence.

In their wide eyes, bulging as if they might pop out, the dozens of arrows hanging in midair—as though caught by an invisible hand—and me at their center were reflected in full.

“A m-monster.”

“How… How is this possible?”

Shock and fear. Questions only those who’d witnessed something close to incomprehensible could ask.

And lastly, the desperate resistance of a few who still hadn’t given up.

“What are you waiting for? Shoot him!”

“B-But…”

“All Imperial Guards! Follow the General’s orders and take down that heinous—!”

I shot my hand out like a bolt of lightning toward the few officers screaming at their men.

Or, to be exact, I scattered the arrows I’d been holding with the power of my Middle Dantian.

*Whoosh! Thup-thup-thup!*

“G-Gah!”

“Gaaah!”

Screams rang out after the arrows’ fierce whistle.

True to their reputation as Imperial Guards, each of them was a master of no small skill. But they couldn’t dodge the arrows I sent flying as if I were controlling them.

Except for one man.

*Clang-clang!*

Arrows bounced away in a flash of swordlight.

The middle-aged man had cut down the attacks coming at him from all sides in a single sweep, his Force shining as brilliantly as the ornate armor that set him apart from every other Imperial Guard. A thought flashed through my mind, and I let it slip out.

“One of the Twelve Palaces of the Zodiac?”

The Twelve Palaces of the Zodiac.

The title collectively referring to the twelve Supreme Peak masters who represented the imperial court.

*“Have you ever heard of the Twelve Palaces of the Zodiac?”*

*“Sure. Aren’t they the names of constellations?”*

*“It’s also what they call the twelve Supreme Peak masters who represent the imperial capital. And half of them are on our side.”*

It was one of the things Ma Sanbao had told me himself. The middle-aged man looked at me with a grave expression and tightened his grip on his great saber.

“Do you know me?”

“I know you well.”

I nodded and went on.

“You’re the treacherous piece of shit who betrayed the Emperor and sided with Dark Heaven. The asshole who wanted to turn me and my people into pincushions. And the asshole who’s about to die.”

“……!”

“That seems like enough to me. If you need more explanation, spit it out.”

“……No. That’s enough. Except for one thing.”

With a sharp gleam in his eyes, the middle-aged man added quietly,

“I’m not the one who’s going to die.”

At that moment—

*Whoosh!*

The man’s figure blurred.

Shifting Form and Position, a supreme movement technique that only those who’d reached the highest realms could perform.

The moment he kicked off the stone wall and sprang into the air, his great saber—longer and larger than most men—crossed the space between us in a flash.

Speed and power that left nothing wanting in a superhuman.

And the terrifying aura pouring from the Force wrapped tightly around the blade.

*Strong.*

I could tell at a glance how powerful this nameless middle-aged man was. I could also tell how grueling the training must have been that brought him to this realm and made him the commander of the Imperial Guards.

But that was exactly why his great saber could never touch me.

To take in the scenery of an entire mountain range at a glance meant you were looking down at it from higher up.

*Whoooosh!*

A single step. That was all it took.

The great saber tore through distorted space, but it couldn’t match my speed as I moved through the air as if it were solid ground. Only the strands of Force it sent flying barely grazed me.

*Sizzle.*

Pain like a burn.

The powerful pressure split the skin showing through my already-tattered clothes. It burst open, scattering drops of my blood.

They mingled with someone else’s.

*Grrk. Cough.*

With a wet, phlegmy sound, the middle-aged man’s body quivered. Something that hadn’t been there moments ago jutted from his thick, bull-like neck.

Something glinting coldly in the darkness.

“Grrk. Wh-What is this?”

Even as he struggled to maintain Stepping on Empty Air, he fumbled at the arrowhead, unable to believe what had happened. I looked at him calmly.

“I’ve been getting so many unexpected gifts that I started feeling bad. I’ll return one of them. Take it.”

“Seizing an Object Through Empty Space?”

“Similar, but different.”

*Tap.*

I touched the center of his unsteady chest with my finger and continued.

“But it’s much harder—and a lot more certain.”

“……The Middle Dantian. It’s the Middle Dantian.”

*Cough.*

The middle-aged man spat out a mouthful of blood and looked at me with trembling eyes.

Then, with what little strength he had left, he struggled to raise the great saber he still clutched.

His voice fading, he said,

“I… I am the Golden Ox Palace of the Twelve Palaces of the Zodiac, the Chief Commander of the Imperial Guard, and one who gives his life to the great and almighty Lord of Heaven…”

The rest of his words would never be spoken.

*Slip.*

Was it the great saber sliding from his hand that happened first?

Or his body, tipping over as death loomed darkly before his eyes?

I didn’t know which hit the ground first. I didn’t care to know.

Master and weapon fell as one. Then, as the dull thud rose from the ground below, I stepped onto the stone wall.

More precisely, into the middle of the Imperial Guards, who stood frozen like statues.

*Hff.*

Someone sucked in a breath. A whirl of emotions rose from the countless men crowding the top of the wall.

Fear and anger, shock. And, last of all, confusion at not knowing what to do.

And that confusion could only mean one thing.

*Not all of them are Dark Heaven’s lackeys.*

There were thousands of traitors on this battlefield alone.

No matter how long the Eastern Heaven Demon Lord had served in the imperial court under the name Cang Gong, it was clear that not all these men had been raised as Dark Heaven’s dogs from the beginning.

The Great Nation’s imperial court wasn’t that easy to fool.

*Winning them over. Coercion. Or orders they couldn’t refuse.*

Dark Heaven had probably broken them in that way. And now the carrots and sticks they’d used were in my hands.

“There’s one thing I can promise you, at least.”

I spoke up abruptly, then addressed all the Imperial Guards.

“If you side with the imperial court now, I’ll make sure you don’t end up as traitors, one way or another.”

As soon as I finished speaking, I reached out.

Toward the Imperial Guard officer who was approaching unseen from a blind spot, his killing intent clear.

*Whoosh. Thud.*

A streak of air whistled by, and one more corpse hit the ground.

I pointed at the body lying there, a Finger Qi hole through its brow, and added calmly,

“Anyone here who doesn’t like my offer, raise your hand.”

“……!”

“……!”

No one raised a hand. I jumped down from the stone wall.

Of course, I didn’t forget one last thing I absolutely had to say.

“Oh, and if you see someone who’s a real bastard, cut him down right now.”

“E-Excuse me?”

“Kill him. Do it yourselves.”

“……!”

That’s right.

From here on out, kill each other.

I left the Imperial Guards glancing at one another and ran toward the Fire Dragon Pavilion members fleeing from the mysterious black-clad figures.

To meet them.

To save them.

*Whoooosh!*
## Chapter artifact 909

# Chapter 909

“Hah… Hah…”

Hyuk Mujin was gasping for breath. His arms and legs, moving nonstop while he was on edge, creaked like they belonged to someone else. His heart felt ready to burst at any second.

*How did it come to this?*

Even as he ran for his life, Hyuk Mujin wondered when and where everything had started going wrong.

But, as always, one question led to another, and they went on without end. In the end, all that remained at the end of the trail was a single, self-mocking thought.

*Fuck. Was being born the mistake?*

Hyuk Mujin felt so wronged and miserable he could have cried.

Why the hell had a textile-shop owner’s son thrown a fit about becoming a martial artist? He could’ve quietly taken over the family business.

If he hadn’t read all those trashy books where martial artists who could fly and fight like the wind appeared as heroes, he might be just like everyone else by now—with a family and two or three kids he loved more than life itself.

At the very least, he wouldn’t be getting chased by a bunch of weirdos who’d appeared out of nowhere.

*Thud-thud-thud-thud!*

The pursuers’ heavy footsteps rang out behind him. A chill ran down Mujin’s spine.

*Shit. If they catch me, I’m done for.*

He didn’t know who they were or where they’d been hiding before suddenly showing up, but one thing was certain.

*Those things are monsters. No—actual monsters.*

Mujin’s judgment wasn’t based solely on the level of their martial arts.

The primal fear and chill he’d felt from the moment he first spotted the black-clad figures had only grown stronger with time.

*What the hell… are they?*

His mind was full of questions he couldn’t answer.

And his body, already pushed to its limit, was slipping out of his control a little at a time without him even realizing it.

*Slide.*

“……!”

His legs suddenly gave out.

Unable to stop himself from the momentum of his run, Mujin pitched forward. His eyes flew wide—

“Hyuuuuuk!”

*Grab!*

A thunderous shout rang out as a powerful hand seized his collar. Mujin had nearly slammed face-first into the ground. He steadied his wildly beating heart and looked up.

*Thump. Thump!*

He saw the face of the giant—no, Taishan—running with Mujin tucked under his arm like a piece of luggage.

“Hyuk. You okay?”

Mujin barely managed to squeeze out a reply.

“No. Not even a little.”

“Yeah. You look that way.”

“……If you know, why ask? Are you messing with me?”

“Hyuk. Is that how you treat the person who saved your life?”

“Not really. Thanks, then.”

“If you’re thankful, pay me back with a hundred plates of five-spice pork later.”

“I’ll buy you two hundred plates, not a hundred. For now, let’s just stay alive. Alive.”

“Two hundred plates?”

Taishan furrowed his brow and slowed down, muttering to himself.

“How much is two hundred plates?”

Namho and the Divine Physician, who occupied Taishan’s broad shoulders, and Mujin, who had somehow become one with the whole arrangement, all screamed at once.

“What kind of lunatic does that? Why the hell are you slowing down all of a sudden?”

“Young Hero Taishan! This is no time for that!”

“What are you doing, you crazy bastard?”

But even amid their fiery protests, Taishan’s brow remained furrowed as he pondered the problem.

“I don’t understand. How much is the number two hundred?”

“Goddamn it…”

Namho groaned toward the heavens and turned to look behind them.

The others bringing up the rear—and the black-clad figures right on their heels—were rapidly drawing closer.

“Just answer him! Looks like he’ll need an answer even if his head gets smashed in! Hurry!”

At the Divine Physician’s desperate plea, Namho’s face went pale as he shouted,

“One hundred plates! If you have one hundred plates twice, how many is that?”

“Hmm. One hundred plates twice is… Ah. Taishan understands now.”

At last, Taishan found his answer and spoke with a triumphant look.

“One hundred two.”

“You fucking bastard!”

“You goddamn idiot!”

“Ah, Master…”

Wails erupted all around them.

Namho, driven to the edge of his patience, brought his elbow down on Taishan’s blockhead. Mujin let out a sobbing scream. The Divine Physician thought of his absent Master and felt around inside his sleeve for a large acupuncture needle, entertaining for the first time the thought of killing someone.

But unlike the others, who were reacting with such passion, Taishan’s face shone like the midday sun. He’d found his own answer to how much two hundred plates was.

“Two hundred plates. A lot. Anyway, it’s a whole lot!”

Even a hundred plates would be enough to eat until his stomach burst. And two hundred plates!

Truthfully, he didn’t know the exact difference between two hundred and one hundred two. But Taishan decided there was no need to worry about such trivial details.

Then, grinning broadly, he waved both hands at someone who hadn’t heard the good news yet.

“Pavilion Master! Pavilion Master! Taishan gets to eat five-spice pork! Hyuk said he’ll feed me until I burst—one hundred two? Two hundred? Anyway, until I burst!”

“Don’t worry about your stomach bursting. Before that, I swear to Heaven I’ll burst your head myself—Wait, what did you just say?”

Namho, who’d been steadily hammering Taishan on the crown with the heart of the Foolish Old Man who moved mountains, widened his eyes and looked up.

And saw them.

Namho. The Divine Physician. Hyuk Mujin. Every Fire Dragon Pavilion member running behind them.

*Whoooosh!*

Someone was rushing toward them amid a fierce whistle of air. The familiar flames burst from his toes.

“Captain!”

Mujin finally let out the tears he’d been holding back.

* * *

A lot of things in life are hard to understand.

For people living before the Great Cataclysm, there were monsters and Hunters, as if they’d dropped from the sky one day. For me, it was the world I’d come to know through the capsule.

The situation in front of me wasn’t quite on that level, but it was still more than enough to leave me confused.

“Five-spice pork! One hundred two! Two hundred!”

Taishan, his face alight with near-maniacal joy.

“Kill this bastard right now! You’re more than capable of cracking this fucking idiot’s head open!”

Namho, radiating so much rage that even *mania* didn’t quite cover it.

“Waaah! Captain! Why’d you only get here now?”

Hyuk Mujin, sobbing his eyes out with the relief of someone who’d died and come back to life.

“Ah, Master… This unworthy Disciple had a wicked thought.”

And finally, the Divine Physician, muttering with such a serene, transcendent expression that he looked like he could even knock the Buddha flying with a Palm Strike of the Tathagata.

“……”

What the fuck?

I had no idea what was going on.

I stared at them, speechless for a brief moment, then gave up on trying to understand.

Of course, it would’ve been more accurate to say there wasn’t time to make sense of the situation in the first place.

*Pat-pat!*

“Pavilion Master! No, Young Master Jin! No, Benefactor!”

Ju Hwaran came running toward me, showing off her skill at changing how she addressed me three times in one short moment. Her clothes were a mess.

Behind her, Song Ilseom and Sama Pyo were desperately swinging their weapons, trying to keep their pursuers at bay.

*Clang!*

*Slice!*

Sword Energy flashed in the darkness, and what looked like blood sprayed through the air.

The wind carried an unbearable stench with it.

*What’s that smell?*

Even though they were still a considerable distance away, it was enough to make me frown and feel nauseous.

But I didn’t have time to guess what the smell was. I moved my lips toward the three who were barely managing to shake off their pursuers as they drew closer.

—When I give the signal, everyone get down.

Along with the Sound Transmission I sent into each of their ears, I gathered all the internal energy in my body.

*Shhhh…*

I sent the heat I’d drawn up from deep within me flowing through every limb and acupoint.

My battered acupoints screamed, and I could feel the large and small wounds I’d sustained in the fight tearing wider. But there was no other way.

*I have to do it.*

*Whummm.*

The iron spear I’d taken from some nameless Imperial Guard just before jumping down from the stone wall trembled, filled with Scorching Yang Qi.

The spearhead glowed red. Over it spread a blue-white flame, no longer anything like it once was—but still too powerful to ignore.

And at last—

*Fwoosh.*

Hellfire surged up around the spearhead, burning the air and devouring the darkness. It swelled toward the figures drawing closer without a scream or a shout.

Like a beast preparing to charge a flock of sheep.

Hotter and more ferocious than anything else in the world.

—Now.

As I sent the signal to the three, I swung the spear with all my strength, as if I were about to cut the world in two.

Like the tail of a dragon reaching out without end.

*The first form of the Blazing Flame Divine Spear.*

**Fire Dragon’s Single Tail.**

*Fwoooosh!*

In that moment, all around us lit up as brightly as day.

The blue-white flames leaped from the spearhead and surged forward, burning and melting the ornaments scattered throughout the imperial palace.

They passed over the heads of the three, who’d heard my Sound Transmission and dropped down half a beat before the final moment.

They also filled the field of vision of the black-clad figures close on their heels.

*Kwaaaaaa!*

*Rumble-rumble-rumble!*

A tremendous explosion and roar. Then the earth shook.

A flash of light, and the swelling flames fell like rain, covering a radius of several dozen *jang*.

There was no better way to describe it than as a fire demon.

And through the smoke in that pit of flames, where not even a scream could be heard, people came running.

*Pat-pat!*

Ju Hwaran. Song Ilseom. Sama Pyo.

I spotted their familiar faces and gave a faint smile.

Or maybe it was my vision that was growing faint, tilting a little more with every passing moment.

*Thump.*

Making it look as natural as possible, and without anyone noticing, I straightened the spear and used it to support myself. Then I suppressed my labored breathing.

*……Damn it.*

A wave of weakness crawled up my body like a living snake.

My internal energy, which had been abundant despite its instability, had run dry. My body, which should’ve been resting, was crying out in pain after all that exertion.

And on top of that, I was mentally exhausted beyond what I could bear.

*I should’ve held back with the Middle Dantian as much as possible…*

I knew well enough that there was no point regretting it now.

If I’d held back more, I wouldn’t be in this state. But there was no guarantee the overall situation would’ve been any better.

I could only be grateful that I’d managed to save the Fire Dragon Pavilion members who, for some reason, had come back here—save them from the danger that had just rushed up in front of me.

“Benefactor!”

Ju Hwaran, now right in front of me, shouted with alarm written across her face.

Song Ilseom and Sama Pyo, approaching at her sides, spoke too, their expressions twisted with concern.

“We have to run. Everyone—we have to get out of here.”

“Right now!”

Their reaction was only natural.

Even though my all-out strike had swept through the front ranks, there were still more than a thousand enemies at a glance. I couldn’t judge their individual strength precisely, but none of them would be easy to deal with.

But the next moment, as the smoke dispersed and the scene slowly came into view, I finally understood.

Why they’d been so desperate.

And why Ma Sanbao had been so confident the rebellion would succeed.

“That’s…”

A faint groan slipped through my parted lips.

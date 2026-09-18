# Checkpoint Review — 355–359

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

# Chapters 355–359

## Plot

Cheongpung arrives as the Western Heaven Demon Lord defeats Tang Sadok and the surviving members of the Tang Clan’s Ten Wonders. The Demon Lord captures Tang Sadok, orders First Fiend to deal with Cheongpung, and enters the Inner Hall to search for the Myriad-Poison Ring. Dark Heaven destroys the Tang Clan’s defenses, killing Tang Jinhu and nearly all resistance while leaving Tang Sadok alive to witness the ruin.

Jin Taekyung defends the underground prison, killing infiltrators before confronting the Western Heaven Demon Lord. The imprisoned Heavenly Power Demon reveals that the Demon Lord was once one of the Divine Cult’s four Protectors and the Cult Leader’s closest aide, but led the Cult Leader astray before taking his current title. During the battle, Taekyung breaks the Demon Lord’s sword and wounds his hand, then uses White Flame, Flame Divine Palm, Flame-Extinguishing Divine Fist, and One Annihilation. One Annihilation wounds the Demon Lord’s shoulder but fails to defeat him.

The Demon Lord’s Black Dragon Armor, Body-Protecting Qi, superior internal energy, and overwhelming Sword Force allow him to dominate the fight. Taekyung survives more than three hundred exchanges despite severe internal injuries, a fractured left arm, probable chest fractures, and nearly depleted internal energy. With no Stat Points remaining, he continues standing to protect Jeok Cheongang and Cheongpung, raises a faint Spear Energy, and challenges the Demon Lord to attack.

## Continuity

- Jin Taekyung and the Western Heaven Demon Lord remain locked in an unresolved fight in the underground prison.
- Taekyung is critically injured, nearly out of internal energy, has no Stat Points remaining, and has a fractured left arm and probable chest fractures.
- The Demon Lord’s broken sword still emits ink-black Sword Force. His Black Dragon Armor and Body-Protecting Qi have withstood Taekyung’s strongest attacks.
- Taekyung’s One Annihilation wounded the Demon Lord’s shoulder but did not defeat him.
- The Western Heaven Demon Lord seeks the Myriad-Poison Ring and intends to deliver Taekyung and Cheongpung alive to the Blood Lord.
- Cheongpung has reached the Supreme Peak realm and remains engaged with First Fiend. The outcome of their fight is unresolved.
- Dark Heaven has effectively destroyed the Sichuan Tang Clan. Tang Sadok remains alive but gravely wounded and captive on a hill overlooking the ruins.
- Jeok Cheongang remains unconscious in the underground prison, with the Divine Physician watching over him.
- The Heavenly Power Demon remains alive and restrained. He has identified the Western Heaven Demon Lord as a former Protector of the Divine Cult and close aide to the Cult Leader.
- Taekyung and Cheongpung remain friends and true martial rivals.

## Translation Decisions

- Use **First Fiend**, **Western Heaven Demon Lord**, **Blood Lord**, and **Dark Heaven**.
- Use **Protector of the Divine Cult** for 호교사자, **Cult Leader** for 교주, and **underground prison** for 뇌옥.
- Use **Black Dragon Armor** for 흑룡갑.
- Use **Sword Force** for 검강 and **Fist Force** for 권강.
- Use **One Annihilation** for 일섬 and **supernatural powers** for 괴력난신.
- Use **Essence-Siphoning Great Technique**, **Get Hit and Fucking Die Technique**, and **physically strong Supreme Peak master** according to the established temporary decisions.

## Durable state

{
  "active_continuity": [
    "The Western Heaven Demon Lord possesses the Black Dragon Armor, has a broken sword that emits Sword Force, and remains in an unresolved fight with Jin Taekyung.",
    "The Western Heaven Demon Lord seeks the Myriad-Poison Ring and intends to deliver Taekyung and Cheongpung alive to the Blood Lord.",
    "Taekyung has no Stat Points remaining and is critically injured and nearly out of internal energy, but continues fighting while standing.",
    "Taekyung's One Annihilation wounded the Western Heaven Demon Lord's shoulder but did not defeat him.",
    "Dark Heaven has effectively won the assault on the Sichuan Tang Clan, while fighting continues in the ruined Family Head's Hall.",
    "Tang Sadok remains alive but gravely wounded and captive on a hill overlooking the destroyed Tang Clan.",
    "Jeok Cheongang remains unconscious and the Divine Physician remains in the underground prison.",
    "Cheongpung remains alive at Supreme Peak and is fighting First Fiend.",
    "Cheongpung and Taekyung recognize each other as friends and true martial rivals."
  ],
  "continuity_sources": [
    359,
    358
  ],
  "open_questions": [
    "What will be the outcome of Taekyung's fight with the Western Heaven Demon Lord?",
    "Can Taekyung protect the Fire King and Cheongpung from Dark Heaven?",
    "Can Cheongpung survive his fight with First Fiend?",
    "Can the Tang Clan's remaining forces protect Tang Sadok and the Divine Physician?",
    "What will the Blood Lord do when the Western Heaven Demon Lord brings the survivors or reports the battle?"
  ],
  "safe_through": 359,
  "temporary_decisions": [
    "Render 호교사자 as Protector of the Divine Cult, 교주 as Cult Leader, and 뇌옥 as underground prison.",
    "Render 권강 as Fist Force and 검강 as Sword Force.",
    "Render 흑혈검법 as Black Blood Sword Technique and 후발선제 as Striking Second, Hitting First.",
    "Render 흡정대법 as Essence-Siphoning Great Technique and 괴력난신 as supernatural powers.",
    "Render 맞고 뒈져라 신공 as Get Hit and Fucking Die Technique and 물리 초절정 고수 as physically strong Supreme Peak master."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 355

# Chapter 355

“Phew. I’m not too late. Thank you for waiting!”

*What kind of lunatic is this?*

At the sight of the young man strolling in as casually as if he belonged there, the Western Heaven Demon Lord let out an involuntary, hollow laugh.

*I haven’t come out in a while, and now I’m running into all kinds of strange people.*

He considered himself a man who had lived a fairly extraordinary life, but the young man before him easily exceeded the boundaries of what he had imagined.

For the Western Heaven Demon Lord, that was rather unfortunate. He had wasted time, while the young man had hurried his own death.

“What’s there to thank me for? Have a pleasant journey.”

Swish!

There were different knives for butchering livestock.

If Tang Sadok and the Tang Clan’s Ten Wonders were pigs, that brat was an ant.

The Western Heaven Demon Lord did not even feel the need to draw his favored weapon. He flicked a finger toward the young man’s brow, then turned his head toward Tang Sadok.

Or rather, he was about to turn his head when—

“Whoa. That nearly scared the life out of me.”

“…?”

The Western Heaven Demon Lord stared at the young man with widened eyes.

The brat should have been lying dead by now, yet he was looking back with an innocent smile and giggling.

And in the iron pillar exactly half a step to his side was a hole the size of an egg.

It was right where the young man’s head had been only a moment ago.

*…He dodged it? Eighty percent of the Ghost Prison Finger?*

It should not have happened. It could not have happened.

Just as the Western Heaven Demon Lord began to wonder whether something had somehow gone wrong with his body without his realizing it—

“Stand back.”

Tang Sadok spoke with a stiff expression. His face was pale from his internal injuries, and there was even a trace of distress in his eyes.

“There’s no place for a greenhorn like you to interfere… Cough!”

“Gasp! Blood! You’re bleeding!”

When Tang Sadok suddenly vomited blood, the young man took a worried step forward.

“Grandpa Tang, are you all right?”

Swish!

In the blink of an eye, the young man flipped through the air, and a flash of light sprang from his waist.

Drawing his sword at the same time, he deflected the slash that came flying through the air. Then he panted heavily.

“Huff, huff. That startled me. Why did you do that without saying anything?”

“Ha-ha. Ha-ha-ha!”

The Western Heaven Demon Lord looked back and forth between the sword in his right hand and the young man before bursting into hearty laughter.

He had not used his full strength, but that single exchange had taught him two things.

First, the mysterious young man was not merely a lunatic.

And second—

“You’re the Disciple Sword Saint Mae Jonghak took in during his later years. Your name is… Cheongpung, was it?”

The young man, Cheongpung, looked at the Western Heaven Demon Lord with round eyes.

“Oh? You know me?”

“How could I not, when the scent of Huashan’s plum blossoms is practically pouring from your footwork? It has been a long time since I saw a Dark Fragrance Drift this exceptional.”

“Wow! You know Dark Fragrance Drift! But how do you know my name…?”

“I have many eyes and ears that you cannot see.”

Dark Heaven had hidden spies throughout the world over many years, and Sichuan Province was no exception.

The Western Heaven Demon Lord had already known for ten days that Cheongpung was staying at the Tang Clan.

He had not expected to meet him at such a perfect moment, though.

*To have reached this realm at that age… The Sword Saint raised a monster.*

There had been a reason he had not recognized Cheongpung at a glance.

Tang Sadok moved his bloodstained lips as the Western Heaven Demon Lord looked Cheongpung up and down with a strange light in his eyes.

“You vicious bastard. Is it not enough to attack our family? Now you intend to harm that boy as well?”

The Western Heaven Demon Lord answered gently.

“No, not at all.”

“He has nothing to do with our family… What?”

Tang Sadok and even the three surviving members of the Tang Clan’s Ten Wonders doubted their ears at the unexpected answer.

But the Western Heaven Demon Lord, the man at the center of it all, remained impassive.

“I have no intention of pursuing prey that someone else has already marked. Personally, I do not like him very much, but we serve the same master.”

“…What are you talking about?”

“An acquaintance of mine became quite angry recently. Perhaps the wound to his pride was greater than the loss of his arm. He has been determined to kill you with his own hands.”

Tang Sadok’s expression twisted at the incomprehensible explanation.

Then Cheongpung suddenly spoke.

“The Blood Lord. It’s him.”

“So you do remember him. He’ll be very pleased if I tell him.”

“I don’t like him.”

Anyone who knew Cheongpung—especially Jin Taekyung—would have stared at him with his mouth hanging open.

Cheongpung possessed a spirit as clear as a mountain stream and had never once judged anyone by saying he liked or disliked them.

Not even those who approached him with malicious intentions.

But now, unmistakable hostility had appeared in Cheongpung’s transparent eyes.

“Is he here right now?”

“Unfortunately, he is far away. But he would be very happy to see you. Ah, of course….”

The Western Heaven Demon Lord continued smoothly.

“The same goes for the Fire King being treated at the Tang Clan and the young man named Jin Taekyung.”

“…!”

“I told you. I have many eyes and ears.”

A smile formed at the corner of the Western Heaven Demon Lord’s mouth.

“Try not to worry too much. I intend to take all three of you—including yourself—alive. But I do not know what my friend the Blood Lord will think.”

Cheongpung could sense the chilling edge hidden beneath the man’s gentle voice.

Without realizing it, he tightened his grip around his sword hilt. A different tone and voice than usual slipped through his lips.

“It won’t be easy.”

“I wonder if that’s really—”

The Western Heaven Demon Lord’s voice never finished.

A tremendous boom split the air, and dozens of flashes filled the pavilion reduced to rubble.

Swish, swish-swish-swish!

Tang Sadok and the Tang Clan’s Ten Wonders—or rather, the three who should now be called the Tang Clan’s Three Skills[^1]—shot toward a single target like arrows, as if they had planned it together.

Dozens of hidden weapons covered every direction, aiming for vital points, while Tang Sadok gathered every ounce of strength he had and slammed his fist into the Western Heaven Demon Lord’s chest.

“You bastard—!”

Kwahhhhhng! Rumble, rumble!

The aftermath was powerful enough to be called an earthquake.

Tang Sadok and the three Tang Clan martial artists had personally experienced the Western Heaven Demon Lord’s might.

They had no intention of wasting their only opportunity, and the final attack they launched after even drawing up their innate qi was devastating.

*We did it.*

Inside a cloud of dust so thick he could not see even an inch ahead, Tang Sadok smiled brightly despite coughing up blood.

He had realized that the punch he had unleashed with all his strength had crushed the enemy’s flesh and bones and pierced through his chest.

*This is the Tang Family’s revenge.*

That was when—

“Did you think this would be enough?”

“…!”

Crack!

Along with the calm voice, a powerful hand closed around Tang Sadok’s neck.

Through the dispersing dust, the Western Heaven Demon Lord could be seen reaching over the shoulder of a dead member of the Tang Clan’s Three Skills, a massive hole punched through the man’s chest.

At the Western Heaven Demon Lord’s feet, two people who had once possessed human shapes lay shattered across the ground.

*How?*

That single thought filled Tang Sadok’s mind.

Still gripping the dazed man by the neck and smiling gently, the Western Heaven Demon Lord suddenly swung the sword in his other hand.

Kwahhhhhng!

A wave of Sword Energy spread outward like a tide.

The thirty blades of Sword Energy flying toward the Western Heaven Demon Lord like flower petals were swept away and vanished.

But even when flower petals disappeared, their fragrance remained.

From the foot of the young man driving into the air at the speed of a flash, the scent of plum blossoms planted by Huashan and brought into bloom by the Sword Saint rose up.

Sssshing!

“The Meteor Chasing the Moon Sword!”

A single sword thrust forward, leaving behind a pale afterimage.

The Western Heaven Demon Lord let out a brief cry of surprise and brought his sword down.

The Western Heaven Demon Lord’s sinuous, snake-shaped sword collided with Cheongpung’s sword, which was engraved with plum-blossom patterns.

Kwang! Kwang-kwa-kwa-kwang!

Every time the two swords met, thunderous sounds like exploding shells rang out in every direction.

It did not take long for it to become clear who held the advantage.

Swish—bang!

With a fierce impact, one figure was sent flying.

Cheongpung twisted his body in midair and landed before staring quietly at the Western Heaven Demon Lord.

“I expected it, but… you’re strong. Truly.”

The Western Heaven Demon Lord’s martial prowess was astonishing.

He had completely dominated the fight with one hand while holding Tang Sadok captive.

At Cheongpung’s apparently awed words, the Western Heaven Demon Lord let out a quiet laugh.

*What an impudent brat. And he is hiding plenty, too.*

For a moment, he considered teaching the brat a lesson himself out of irritation.

But there was something more urgent.

The Western Heaven Demon Lord clicked his tongue softly, and a low voice slipped between his lips.

“First Fiend.”

“Yes, Demon Lord.”

Cheongpung was not surprised when First Fiend appeared in response.

He had known for fifteen minutes that the man was nearby.

That meant the attackers had already passed through the Outer Hall and entered the Inner Hall.

The screams were drawing closer.

“Take care of that one.”

“You mean the Sword Saint’s successor? I couldn’t be more grateful….”

First Fiend grinned, baring bloodstained teeth.

He had already claimed nearly a hundred lives, including Tang Jinhu, the Sichuan Tang Clan’s Head Elder.

But intoxicated by the slaughter he had not tasted in so long, he had been feeling that it was far from enough.

“You know about the Blood Lord’s request, I assume.”

“Of course. The Sword Saint’s youngest Disciple, whom he cherishes like his own child… Heh-heh. This should be fun. I’ll leave him barely breathing.”

“It would be better if you kept him alive, but if that proves impossible, killing him is fine.”

“What?”

“He is dangerous. If you decide he cannot be handled, cut him down before he can grow.”

“He’s nothing but a greenhorn. I never knew the Demon Lord made jokes. Ha-ha-ha!”

First Fiend’s booming laughter rapidly faded.

It was because of the Western Heaven Demon Lord’s gaze, which had turned cold.

The instant their eyes met, First Fiend felt his heart drop. He hurriedly threw himself facedown on the ground.

“Y-Your orders.”

For a moment, he had forgotten what kind of man the Western Heaven Demon Lord was.

He was a man who hid a grim reaper behind a gentle voice, soft manner, and mild expression.

The Western Heaven Demon Lord looked down at First Fiend, who was sweating nervously, then silently walked past him.

Tang Sadok struggled in pain with the hand around his neck, but the Western Heaven Demon Lord’s arm did not move an inch.

“No!”

“Heh-heh. Do you have any idea whose path you’re blocking?”

Swish—boom!

With Cheongpung charging forward in desperation and First Fiend moving to stop him, a fierce boom rang out.

Leaving the thunderous clash behind, the Western Heaven Demon Lord continued walking.

The Inner Hall, where craftsmen made weapons and children and martial artists once walked side by side, was already covered in blood and corpses.

Screams and death overflowed from every direction.

And only a short distance away, one man watched the destruction of his family while tears ran down his face.

“Can you feel it? Everything in the Tang Clan is collapsing.”

Tang Sadok’s hollow eyes trembled.

It was not only the Tang Clan that was collapsing. His firm convictions and his heart were crumbling as well.

Then, as tears continued to stream down his face, a quiet voice slipped into his ear.

“Answer me. Where is the Myriad-Poison Ring?”

[^1]: In Korean, the final words in “Tang Clan’s Ten Wonders” and “Tang Clan’s Three Skills” are homophones, preserving the wordplay as their number dwindles.
## Chapter artifact 356

# Chapter 356

The underground prison beneath the Sichuan Tang Clan was a dark, damp place by nature.

The torches hanging here and there gave off less light than fireflies, and the floor was covered in stagnant water of unknown origin that made squelching sounds whenever anyone walked across it.

Just like now.

“What a foul smell. Even if this is a prison, how can they lock people up in a place like this?”

“People? This is a place for raising beasts. Haven’t you heard that the Sichuan Tang Clan captured the fiends of the Great Faction War and subjected them to all kinds of torture? It’s no surprise that a place like this exists.”

Squelch. Squelch.

There were two voices, but several sets of footsteps.

I quietly raised my Qi Sense and counted them.

*Fifteen.*

The two men at the front, whom I assumed to be the leaders of the group, continued talking.

“But why can’t I see any prisoners? There are only iron bars, and the cells are empty.”

“Everyone imprisoned here is an old monster from the Great Faction War. It wouldn’t be strange if they had died long ago. Especially after being tortured in a place like this.”

“That’s true.”

Their guess was half right and half wrong.

It was true that many of the first-generation inmates of the underground prison had already gone to the other world, but more than ten prisoners still remained here.

What they had failed to anticipate was that someone unseen had used Pressure-Point Strike on the prisoners and moved them elsewhere.

“I can’t see even a single ant. Wouldn’t it be better to go back upstairs and kill at least one more person?”

“I don’t think we’ve even searched half the place yet.”

“Since you mention it, what could possibly be further in? The others will come and search every corner anyway.”

“Don’t talk nonsense. Have you forgotten the order given by the Lord of Heaven? What if someone of the Tang Clan’s bloodline is hiding here…?”

“No one would be stupid enough to hide in an underground prison. The battle isn’t even over yet, so why would they hide here? I could understand trying to break through the encirclement and escape, but this?”

“Hmm…”

The man let out a low groan, then spoke in a firm voice.

“Impossible. We serve the solemn command of the revered Lord of Heaven. With the Demon Lord leading by example, do you intend to handle your duty carelessly?”

“Phew. Damn it.”

“Stop complaining and follow me.”

The Dark Heaven martial artist whose face I did not know had no idea that his fate had been decided by those words.

The other man grumbled at his firm tone.

“You really need to show some flexibility. If you keep living so rigidly, you’ll die before your time.”

“Don’t say such unlucky things. I’ll live longer than you, who always do everything half-assed, so don’t worry.”

“Want to bet on it?”

“Fine. It’s not as if I can’t—”

To give you the conclusion first, the longevity bet between the two men ended with the one who did everything half-assed winning.

Of course, the difference between their deaths amounted to no more than a moment.

Thrust!

It was a perfect surprise attack.

In the maze-like corridor, I had been waiting in the darkness with my presence concealed. The instant I drove the dagger in my left hand into one man’s eye, I swung the sword in my right.

The blade, which I had coated in mud beforehand to keep it from reflecting light, cleaved through flesh and bone.

Slash! Splat!

The two Peak masters died without even managing to scream. Their bodies collapsed like rotten logs.

The black-robed men, suddenly drenched in blood and filthy water, stared back and forth between the bodies of their leaders and me with vacant eyes.

“W-What is…?”

There were thirteen left.

I answered by swinging my sword.

Once again, accompanied by a dreadful sound of flesh being torn, a severed head rose into the air.

“Twelve now.”

“……!”

An emotion appeared in their previously empty eyes.

It was fear.



* * *

“You’re trapped, right? The layout here is kind of fucked up. Apparently, they built it this way in case any prisoners tried to escape.”

“Eek!”

I walked toward the rat cornered at the end of the passage.

Of course, he was far too large to actually be called a rat. Despite his size, however, he had been the quickest of them all to run away, perhaps because he was such a coward.

“All right. Let’s go to hell and join your friends.”

“F-Fiend!”

“You crazy bastard. So it’s romance when you do it, but adultery when I do?”

Thud.

The black-robed man dropped to his knees, his face gone deathly pale. He was still holding a weapon, but he already knew perfectly well that it would do him no good against me.

In the end, the method he chose was to beg for his life.

“P-Please, spare—”

“F-Fuck off.”

Crack.

Without hesitation, I broke the black-robed man’s neck. His head tilted at an unnatural angle, his tongue hanging from his mouth.

Instant death. No doubt about it.

“You people always make me do things twice. You weren’t going to get very far anyway.”

With a sigh, I hoisted him over my shoulder and started walking back the way I had come. It did not take long to return to the place where I had launched my first surprise attack.

The black-robed man had not been able to run very far in the first place, and I had grown familiar with the underground prison’s labyrinthine structure over the past ten days.

“Bastards. What the hell are you crawling all the way in here for? Is there something to eat?”

This was the second time black-robed men had infiltrated the underground prison.

About thirty minutes earlier, seven of them had entered first, and I had taken care of every last one.

I had helped the Sichuan Tang Clan reduce the enemy’s numbers, but I did not feel the slightest bit happy about it. I knew what their intrusion meant.

*The battle is going badly.*

The underground prison was located on the outskirts of the Tang Clan’s Inner Hall. That meant the Outer Hall, which could be considered the front line, had already been breached.

*Then what about Cheongpung…?*

I shook my head at the ominous thought that suddenly crossed my mind.

*No way. Even if you dropped Cheongpung into the middle of hell, he’d be the kind of guy who came back alive.*

No. He had to be.

*Damn it. If only I could at least log out. Then there’d be a little hope.*

I had wondered if it might work, but as expected, it did not.

The System had blocked the Logout function as soon as the Quest began.

Besides, even if Logout suddenly became available right now, I could not recklessly return.

There had already been two intrusions in the past thirty minutes. If the enemy stormed in while I was spending even a short time in the modern world…

*Not only me, but Jeok Cheongang and the Divine Physician would be finished.*

*I have no choice but to stop them here.*

They had numbers on their side, while I was alone.

So, just as before, I needed to make the most of surprise attacks and conserve my strength in case of an emergency.

*If they come in and find corpses scattered everywhere, it’ll all be for nothing.*

I began moving the bodies lying around one by one.

The place I had designated as a temporary morgue was the deepest, darkest part of the underground prison.

Creeeak.

“It’s been a while. Has it been about half an hour since I last saw you?”

“……”

“I brought some new friends so you wouldn’t be lonely.”

At the center of the prison, where not a single ray of light reached, an old man covered in dangling restraints glared at me with blazing eyes.

He was the Heavenly Power Demon.

“What? Got something to say?”

“……!”

“What are you going to do by glaring at me like that? If you have something to say, go ahead.”

“……!!”

“Oh, right. The pressure points.”

I had struck his Paralysis Acupoint and Mute Acupoint, so naturally he had been unable to say anything.

I walked over and unsealed his acupoints. Only then did his angry voice burst out.

“What the hell do you think you’re doing?”

“Can’t you tell? I’m moving corpses.”

“Then why the hell are you moving those corpses here?”

“Don’t shout. If you raise your voice one more time, I might strike a lethal acupoint instead of your Mute Acupoint.”

“……!”

Good. He was quiet now.

Leaving the silenced Heavenly Power Demon behind, I began stacking the bodies I had brought into the prison.

Thump. Rumble-rumble.

“Could you pick up that head over there?”

“……Are you speaking to this old man?”

“Oh, right. You’re wearing restraints.”

“Huff. Huff.”

The Heavenly Power Demon’s face reddened as he snorted angrily. Even so, he seemed unwilling to have me strike a lethal acupoint, because he barely managed to suppress the shout rising to his throat.

“What the hell is wrong with you…?”

“All done. I’m leaving.”

“……!”

“What? Did you have something to say?”

The Heavenly Power Demon had remained silent despite my efforts to coax information out of him for the past several days.

A man who must have seen enough corpses during the Great Faction War to be sick of them had to have a reason for whining now. Having struck the mark, I watched him stammer.

“N-No. Nothing.”

“Then we’re done here.”

“W-Wait. Wait just a moment.”

“This is your last chance. If you have something to say, say it quickly.”

The Heavenly Power Demon moved his lips for a while before letting out a deep sigh.

“Why did you leave only this old man here? Where are the other prisoners?”

“You don’t need to know.”

“Then what exactly are these corpses?”

He asked as if it were nothing important, but the way he cautiously watched my expression showed that this was what he had really been curious about.

For the past several decades, the only person who had visited the prison had been Old Man Gung, carrying torture implements. It was understandable that he would be curious after nearly twenty naked corpses had suddenly been piled up here.

“Has some disaster befallen the Tang Clan?”

“It has.”

I added one brief sentence.

“Dark Heaven invaded.”

“……!”

It was the same expression he had worn a few days ago.

I ignored the Heavenly Power Demon, who had frozen at the words *Dark Heaven*, and continued.

“The Outer Hall has already been breached, and a fierce battle is probably still raging in the Inner Hall. The battle is going worse than expected.”

“Who did you say it was?”

“What?”

“You must have interrogated the prisoners as well. I’m asking who is leading those bastards.”

“You’re sharper than I expected.”

I had already squeezed information out of one of the seven who first entered the prison.

He had been so terrified that he severed his own heart meridian and killed himself, so I had not learned much. But I had managed to hear one man’s title.

“The Western Heaven Demon Lord.”

Clatter! Clank!

Just four words.

But the effect they had on the Heavenly Power Demon was enormous.

The old man, who had always hung from his restraints with a gaunt body reduced to skin and bones, yanked at the chains as if he might leap out of the prison at any moment.

He even glared at me with bloodshot eyes.

“Did you just say… the Western Heaven Demon Lord?”

“You know him?”

“I-Is he still alive? Then what about the Cult Leader? What happened to the Cult Leader?”

What was wrong with this old man all of a sudden?

Taken aback, I answered.

“……At this hour? He’s probably eating breakfast.”

It was my first time hearing the title Western Heaven Demon Lord, so how would I know what had happened to the Demonic Cult’s Cult Leader? It was not as if the Demonic Cult had an official Twitter account.

“So it finally came to this. In the end, it came to this! Ha-ha… Ha-ha-ha!”

After muttering incomprehensible words, the Heavenly Power Demon began laughing like a man who had lost his mind.

I stared at him for a moment, then suddenly spoke.

“Spill it now. What’s the relationship between the Demonic Cult and Dark Heaven? And what the fuck kind of bastard is this Western Heaven Demon Lord?”

The laughter that had echoed throughout the prison abruptly stopped.

The Heavenly Power Demon’s empty gaze turned toward me.

“He—the man you call the Western Heaven Demon Lord—was one of the four Protectors of the Divine Cult. He served the Cult Leader from closer than anyone else…and he was the one who led him astray.”

“Then…”

“One day, he began calling himself the Western Heaven Demon Lord. That was the beginning of everything. And in the end, it came to this. It finally came to this. Ha-ha… Hahahaha!”

At that exact moment, the Heavenly Power Demon burst into crazed laughter.

Boom! Rumble-rumble!

Along with a tremendous roar from far away, the underground prison trembled.
## Chapter artifact 357

# Chapter 357

A serene expression and an unhurried gait. A clean yellow robe.

He alone stood apart—the only person whom the aura of death filling the Sichuan Tang Clan could touch.

“They’re no more than a handful of men at best. Push them back!”

“Fight to the end! We are the Sichuan Tang Clan!”

“Waaaaah!”

With a tremendous roar that shook the earth, two waves crashed into each other. Screams and battle cries mixed together as a thick mist of blood began to form.

It was a fierce battle in which no one paid any heed to their own life. The victor and loser were decided just as quickly.

“Surround them! Don’t let a single one survive!”

“Gaaaah!”

The black wave of men dressed in black swallowed the green wave.

What remained where the wave had swept through were corpses dressed in green, scattered like foam.

Watching it all from more than a thousand feet away, the Western Heaven Demon Lord suddenly spoke.

“It’s over.”

Their resolve to stand and fight without retreating was worthy of respect, but from the start, this had been a fight in which the few could never overcome the many.

Even the poison and hidden weapons that formed the foundation of the Sichuan Tang Clan were unable to display their full power.

The battle—or rather, this war—belonged to Dark Heaven.

“It seems I won’t be able to keep my promise. I’m sorry, Family Head Tang.”

The more desperate people became, the more their judgment deteriorated. Tang Sadok had been no exception.

After extracting the answer he wanted in exchange for promising to preserve the Tang Family’s lineage, the Western Heaven Demon Lord had taken a simple and cruel course of action.

Instead of killing Tang Sadok immediately, he had seated him in a tree atop a hill overlooking the Sichuan Tang Clan.

That way, Tang Sadok could watch his family be destroyed until the moment his life ended.

“Everything is according to the Lord of Heaven’s will.”

Drip. Drip-drip.

The Western Heaven Demon Lord looked up at the sky, which had begun releasing raindrops, then turned around.

The entrance to a cave gaped like a pitch-black maw. Beside a fallen brazier, an old, hunchbacked man lay dead with his eyes wide open.

What caught the Western Heaven Demon Lord’s interest were the scars carved into the old man’s body.

*The Black Blood Sword Technique.*

The Black Blood Sword Technique was a sword technique permitted only to Dark Heaven martial artists.

Realizing the identity of the men who had arrived before him, the Western Heaven Demon Lord followed the stone steps leading underground.

Clear footprints, mixed with blood and mud, remained on the stairs. At least twenty subordinates had certainly visited this place before him.

And most likely…

*They’re all dead.*

There were traces of people going down, but none of them coming back up.

Once he entered the underground prison, his guess became a certainty.

The Western Heaven Demon Lord had lived a life stained with blood. He could feel the heat of battle lingering in the dark corridor, along with the fishy scent of blood buried beneath the stench.

*Who did this?*

He wondered as he looked at the fine droplets of blood splattered across the wall.

*Skilled work. They were killed without even being able to put up a proper resistance.*

With the Sichuan Tang Clan in a crisis as precarious as a candle in the wind, there was no chance any of the clan’s masters would be here protecting outsiders.

If Tang Sadok’s words were true, only three people remained in the underground prison.

The Divine Physician was a negligible force, and Fire King Jeok Cheongang had yet to regain consciousness. That left only one person.

*Jin Taekyung, the Sleeping Dragon of Shanxi.*

The Western Heaven Demon Lord suddenly remembered what the Blood Lord had said about Jin Taekyung.

The most arrogant, tenacious young bastard in the world, with enough nerve to let his guts hang outside his body.

For some reason, the Blood Lord had wanted to kill Jin Taekyung even more than the Sword Saint who had cut off his arm or the Fire King.

*So he’s skilled enough to survive an encounter with the Blood Lord?*

But Jin Taekyung would not have a second stroke of luck.

The Sword Saint was not here, and the Fire King was also incapable of fighting.

The Western Heaven Demon Lord intended to easily capture the rats trapped in the jar and return.

*Along with the Myriad-Poison Ring they possess.*

Squelch. Squelch.

The Western Heaven Demon Lord was walking leisurely when he suddenly stopped.

A solid stone wall extending from the ceiling now blocked his way.

“Well, well. They certainly made this place complicated.”

He stared at the wall for a moment, then gathered his hands. A dark-red mist coiled around his arm and wrapped around his fist.

Gooooooong.

Everything happened in an instant.

The manifestation, compression, and explosion of qi. Nothing could stand in the path of his Fist Force.

Rumble-rumble-rumble!

It shattered, collapsed, and shook.

The concentrated mass of immense qi shot straight forward, piercing dozens of walls. Stalactites rained down from the ceiling like hail, and a thick cloud of dust rose into the air.

*Much better.*

The next moment, the Western Heaven Demon Lord looked at the scene he had created and spoke.

“Why don’t you come out now?”

The answer was an ear-splitting sound slicing through the air.

Whoosh!

As the dust cloud split apart, the Western Heaven Demon Lord caught the dagger flying toward his throat and smiled faintly.

“Are you Jin Taekyung?”

“You already know. Why ask?”

Step. Step.

A tall young man emerged through the dust cloud and stared at the Western Heaven Demon Lord with an impassive gaze.

* * *

I tried to look unfazed.

Half of any fight was decided by aura. Just because my opponent looked weaker than me, I could not afford to lower my guard. And just because he looked stronger, I could not let myself be intimidated.

Especially when I had come face-to-face with a genuine powerhouse like this.

*What kind of monster is he?*

I looked at the middle-aged man before me, inwardly clicking my tongue.

If Moses had parted the sea with his staff, this man had created another path through the underground prison with a single punch.

That was not all. He stood there with a faint smile on his face, the very picture of tranquility.

*Even the air around him smells different.*

The Blood Lord had been an openly insane bastard. This middle-aged man, however, was dangerous simply by existing.

Their martial arts might have been comparable in strength, but they were completely different in nature.

“I’ve heard a great deal about you. You’re an amusing young man, just as I was told.”

I answered while lowering the spearhead of White Flame at an angle.

“I’m pretty entertaining myself.”

“I’ve also heard that you’re ill-mannered.”

“You’ve got the wrong man. My nickname is Mr. Manners.”

“Well, I would have to spend more time with you to know for sure. But according to what an acquaintance told me, that seems to be the case.”

“You don’t look like you have any friends. Who’s this acquaintance?”

The smile at the corner of the middle-aged man’s mouth deepened.

“The Blood Lord.”

“…!”

“He says he wants to see you very much.”

“I don’t even want to look at that son of a bitch.”

“You use exactly the same words as that young man, Cheongpung. Your tone is different, though.”

*This bastard has already met Cheongpung.*

And yet he was here…

I felt the muscles in my face stiffen before I could stop them.

“You, by any chance…”

The middle-aged man smiled and waved his hand.

“There’s no need to worry. I won’t kill you. I intend to take you, Cheongpung, and the Fire King back alive.”

I asked with a dumbfounded expression.

“Take us?”

“I told you. The Blood Lord wants to see you. So you’ll be safe, at least until then.”

“……”

“Of course, what happens afterward will be up to the Blood Lord.”

The middle-aged man had given me two pieces of good news and one piece of bad news.

The two pieces of good news were that Cheongpung was alive and that the Blood Lord was not here. The bad news was that if I lost this fight, I would be having a group get-together with the Blood Lord.

Of course, the chances of us having a drink over grilled intestines before parting ways were close to zero.

*Instead, there’s about a fifty percent chance I’ll become the grilled intestines.*

The other fifty percent was the chance of becoming grilled tripe.

Damn it. Just thinking about it was making my mouth water.

I swallowed dryly and looked the middle-aged man up and down.

A man who could call someone presumed to be one of Dark Heaven’s highest-ranking figures his “acquaintance.” A man who had demonstrated this much destructive power with a single punch.

One person’s title came to mind.

“You’re the Western Heaven Demon Lord, aren’t you?”

“Ah, now that you mention it, I haven’t introduced myself yet. It’s a pleasure to meet you.”

“Pleasure my ass.”

I stared at the Western Heaven Demon Lord’s two perfectly functional arms and muttered.

“I heard you only had one arm.”

“That was true. Until ten days ago.”

“What?”

“I had another one attached. It wasn’t originally mine, so it still doesn’t move quite as well as I’d like. If you’re going to try something, aim for my left arm.”

“…!”

What the hell was this guy?

Even if I granted that some kind of suturing operation was possible, he had swapped out an arm like a computer component.

Aside from the subtly different skin tone, its movements were perfectly natural.

*Is this even possible? In only ten days?*

I could not understand it at all, but I had to set aside my surprise and questions for the moment.

What bothered me more was what he had said at the end.

*He even told me his weakness.*

There could only be one reason for this kind of absurd behavior.

It was the kind of arrogance only someone convinced of his own overwhelming strength could display.

And this man—the Western Heaven Demon Lord—was powerful enough to make arrogance look like ease.

“Damn it.”

I took a deep breath and glared at the Western Heaven Demon Lord with a cool, level gaze.

“Can’t you just turn around and leave, as if you’d only come to visit a patient?”

“That would be difficult. Setting you people aside, there’s something I have to take with me.”

“Something?”

Instead of answering, the Western Heaven Demon Lord asked me a question.

“This old man will ask you this time. Will you surrender? Peacefully.”

“Could you kill yourself for me? Peacefully.”

“Then there’s only one answer.”

We stood roughly a hundred yards apart.

The instant our gazes collided across the space between us—

Whoosh! Swish!

We both reached out at the same time.

No. At least when it came to launching our attacks, I was faster.

The only problem was that the finger qi the Western Heaven Demon Lord fired reached its target one step before my dagger did.

*He struck second and hit first.*

A red warning light came on in my head. At the same time, my sharpened senses took in everything around me.

The finger qi was formless and invisible. But I could clearly feel the energy approaching. It was a new sense I had acquired while fighting Hwangbo Eom, the Taeeul Merciless Sword.

*Now!*

I twisted my head and sprang forward. Something faster than a bullet grazed past my ear.

The Western Heaven Demon Lord watched me with an expression of surprise.

“To evade a Ghost Prison Finger at eighty percent power… You certainly have a talent for surprising people as well—”

“Yup, Ghost Prison Finger.”

Whoosh!

The Western Heaven Demon Lord’s voice broke off.

In that slowed instant, his widening pupils reflected my figure rushing right up to him.

It was a speed beyond the range he had imagined, something that had far surpassed the limits of a Peak master.

*Stamina, Strength, Agility. And the Flamefire Path.*

I poured everything into a single step. I erased the distance and pierced through the air.

The fire dragon curled within my qi sea spread its wings and took flight. The transparent spearhead of White Flame became the dragon’s claw as it plunged toward the enemy.

*Heavenly Strike.*

Kraaaaaash!

* * *

Rumble-rumble-rumble!

It was a tremendous reverberation.

As if proving the intensity of the battle, the corpses piled together in a tangled mass of enemies and allies collapsed.

The pavilion shook as though an earthquake had struck, and even those swinging weapons at each other staggered, momentarily unable to keep their balance.

“An earthquake! It’s an earthquake!”

“Damn it, of all times…”

An earthquake was a calamity that human strength could not stop.

The reverberation appeared and vanished in an incredibly brief moment, but the people were terrified.

Everyone, that is, except for the two people facing each other in the Family Head’s Hall of the Sichuan Tang Clan, which had already become a ruin.

“Ha-ha-ha-ha-ha!”

After releasing a great roar of laughter toward the heavens, the First Fiend turned toward Cheongpung.

“You felt that too just now, didn’t you?”

Cheongpung nodded with a dazed expression.

“Yes.”

He had no choice. The reverberation had been a tremendous wave of qi, powerful enough to be felt from hundreds of yards away.

The First Fiend continued in a sneering voice.

“It seems the Demon Lord has finally made up his mind. Heh-heh.”

“I know. It’s really amazing.”

“He has finally thrown away his last shred of mercy and embraced killing intent. Neither the Fire King nor that disciple of his will survive. Do you understand what that means?”

“Yes. My Benefactor really is amazing.”

“Now that we no longer need to worry about the Blood Lord’s feelings, even I won’t show you any mercy from here on—what?”

The First Fiend stopped and frowned.

He could not understand what the greenhorn in front of him had just said.

“Your Benefactor? You mean that disciple of the Fire King?”

But Cheongpung’s next answer was not directed at the First Fiend.

In fact, none of his answers had been directed at him from the beginning.

A quiet murmur slipped between Cheongpung’s lips.

“At first, I thought I was far ahead of him, but before I knew it, he’d already come this far…”

Cheongpung gazed toward the place beyond where the reverberation had begun, his eyes sparkling with joy and ruefulness.

No one else in the Sichuan Tang Clan could have guessed it—not even the First Fiend standing before him.

But Cheongpung knew.

“There’s no doubt. It’s my Benefactor.”

Cheongpung had been happy on Huashan, but he had also been lonely.

There was something that could not be filled by the beautiful scenery, the animals he could play with, or even the grandfather he revered more than anyone.

*“There are many young prodigies your age in the Murim. The Ten Dragons and Phoenixes are the best among them.”*

*“Um. Are those Ten Dragons and Phoenixes stronger than me?”*

*“Huh? What kind of question is that? Of course you, Pung, are—”*

*“Grandpa?”*

*“Ahem. Of course you’re lacking.”*

*“Gasp! Really?”*

*“O-Of course! The world is vast, and there are many masters. So you’ll have to keep working hard at your martial arts from now on, right?”*

*“Yeees…”*

From the single thoughtless remark his grandfather had let slip, Cheongpung felt the unfamiliar emotion in one corner of his heart grow stronger.

He learned the name of that emotion only later.

Competitive pride.

*Which of us is stronger?*

He wanted to find out. He wanted to pit his martial arts against theirs and spend time with them.

And so Cheongpung left Huashan and ventured out into the world. On one sunny winter day, he met him.

*“If it isn’t an imposition, could I have just one candied hawthorn skewer?”*[^1]

*“...Mujin. Give him one.”*

That was Cheongpung’s first meeting with Jin Taekyung.

A person who was his Benefactor in name and his friend in truth. And now, his only true rival.

A gentle smile formed at the corner of his mouth.

“I know. I know my Benefactor thinks the same way I do.”

“…!”

Flames rose in the First Fiend’s eyes as he watched this.

The young brat who would have died long ago if not for the Western Heaven Demon Lord’s orders had dared to ignore him. His fate was as good as sealed.

“You little bastard…”

The First Fiend raised his double axes, their blades caked with someone’s flesh.

And then, at the sight of what happened before his eyes, he froze like a stone statue.

Swooshhh.

The wind was blowing.

A scarlet wind of qi flowed from one person’s body, slid down his wrist, and passed onto his sword.

It traveled past the plum blossom engraved on the hilt, wrapped around the blade, and finally bloomed into a single red plum blossom.

Crackle-crackle-crackle!

It was a halo of light more brilliant and destructive than anything else.

A dazed voice escaped between the First Fiend’s lips as he stared at the unbelievable sight.

“...Sword Force.”

The product of great martial artists. Proof that its wielder had reached the exalted realm known as Supreme Peak.

Yet the twenty-three-year-old young man’s face wore an innocent smile wholly unsuited to a great martial artist.

“So, shall we begin?”

[^1]: Candied hawthorn skewers are a traditional snack made by coating hawthorn fruit on a skewer in hardened sugar.
## Chapter artifact 358

# Chapter 358

Kraaaaaash!

A spearhead wreathed in blue flame came plunging down toward the crown of a man's head.

It was the claw of a fire dragon descending from the heavens—a destructive force capable of erasing anything that stood in its way.

*This is…*

Within a moment split into ever-smaller fragments, the Western Heaven Demon Lord thought.

*I can't evade it.*

This was not a strike he could avoid by taking a few steps back.

Then what should he do? Before he could even form the question, the body that had survived countless life-and-death duels was already moving.

Whoosh!

A dark-red Sword Force shot up from his waist and collided with the blue flames.

* * *

Boom!

A shock wave swept through my entire body with a tremendous roar. My ears rang, and the breath caught in my throat.

The sword and spear collided, releasing a flash of dark-red light. In the next instant, I was flying far away as if someone had yanked me backward.

Bang! Bang! KABOOM!

The thick wall of sedimentary rock crumbled like castella the moment my back struck it.

I knocked away a stalactite falling toward my eyes and twisted my body around.

The instant my feet touched the ground, the solid stone floor gouged open like a plowed field.

Krrrrrk!

Damn it. I must have flown at least thirty feet.

I pulled off the leather shoes whose soles had completely disappeared, tossed them aside, and glared at the bastard in the distance.

“Fucking bastard. You’re pretty good, huh?”

“……”

Even through the cloud of dust, I could see the Western Heaven Demon Lord’s stiffened expression.

He silently looked down at the sword blade broken clean in half and his blood-soaked grip before opening his mouth.

“That spear is a divine weapon.”

“Divine weapon? That’s a bit much.”

“What martial art was that?”

I answered without hesitation.

“Get Hit and Fucking Die Technique.”

“I’m beginning to understand why the Blood Lord called you arrogant. And… why he wanted to kill you so badly.”

The Western Heaven Demon Lord’s eyes swept over my entire body.

“You’re dangerous.”

“I am kind of dangerous. Maybe that’s why all the women avoid me.”

“Cheongpung, the young man who reached Supreme Peak at such a young age, is certainly remarkable, but he is not as remarkable as you. To be honest, yes. You have far exceeded my expectations. You wounded me despite being merely at Peak.”

I was not surprised. I had already vaguely realized that Cheongpung had broken through the wall and reached Supreme Peak.

The Western Heaven Demon Lord’s accurate assessment of my martial arts realm followed the same logic.

“Was that a compliment?”

“Of course. But do not be too pleased. I do not like people who exceed my expectations.”

Speaking in a low voice, the Western Heaven Demon Lord clenched and unclenched his bloodied palm. Sticky blood dripped down, wetting the rocks and sand.

“My use of Four Ounces Deflecting a Thousand Catties was perfect. And yet I could not redirect the attack completely. An attack from a greenhorn of a young man who is merely at Peak.”

Four Ounces Deflecting a Thousand Catties—the martial principle of controlling a thousand catties of weight with four ounces.

And just as he said, the Western Heaven Demon Lord’s use of Four Ounces Deflecting a Thousand Catties had been flawless. Even after being caught off guard, his attempt to calmly and precisely redirect Heavenly Strike had been impressive enough to earn my secret admiration.

But if there was one thing he had failed to anticipate…

“I’m a little stronger than I look.”

The man he was facing now was not an ordinary Peak master.

A Third Rate could not stand against a Second Rate, and a Second Rate was forced to kneel before a First Rate.

The higher one’s realm, the wider the gap became, and the more distant the difference in strength grew. That was the common sense of this world—the Murim.

But I was an existence that defied common sense.

“Call me a physically strong Supreme Peak master.”

“A physically strong Supreme Peak master. I do not know what that means, but if that is what you are, then so be it. Understood.”

I stared at the Western Heaven Demon Lord as he nodded, utterly dumbfounded.

“…What exactly do you understand?”

“Living a long time exposes one to all sorts of experiences. Compared to the supernatural powers I have known, what you have shown is merely a drop in the bucket.”

With a faint smile, the Western Heaven Demon Lord raised one arm.

His movement was so natural that it was hard to believe he had been one-armed until only ten days ago.

That arm was certainly included among the supernatural powers he had mentioned.

“Everything will unfold according to the will of the most exalted Lord of Heaven. Now, why not abandon your futile hopes and surrender?”

“Surrender?”

“If you do so, I will personally petition the Lord of Heaven to put you to good use. Even the Blood Lord will not dare touch you.”

“Wow, you’ve got it all planned out.”

“May I take that as your consent?”

“Hmm, wait a second. I just thought of something better.”

I slowly walked toward the Western Heaven Demon Lord as I continued speaking.

“Stories like this always end with good triumphing over evil anyway. So stop fooling around in some place called Dark Heaven or Cheonggyecheon and come over to the orthodox faction. I’ll put in a good word with Grandpa Sword Saint and get you an easy job.”

“Heh. Well, this is something.”

The Western Heaven Demon Lord took a step forward with a faint smile.

“That is unfortunate. Do not come to regret it when you meet the Blood Lord.”

“Every bastard who’s said that to me is now bowing their head before Yama.”

“You are young, so your blood runs hot. If you are hoping for the same luck you had at the start, forget it. I know that strike was your full strength.”

“That’s the best bullshit I’ve heard all year. Have you been taking bullshit lessons from the yellow dog next door?”

I answered him casually, but unfortunately, the Western Heaven Demon Lord’s words were true.

A surprise attack had to end with a single strike. Either render the opponent unable to fight or kill them.

Breaking a weapon and tearing open a hand was not enough.

The Western Heaven Demon Lord was a master far above me. Showing him my full strength and still failing to inflict any significant injury had been a painful mistake.

*Should I have used One Annihilation from the beginning?*

What would have happened if I had gone all in from the start?

I sent the thought flying far away. Even if I could return to that moment, I probably would not be able to stake everything on one move.

A gamble with only all or nothing as the possible outcomes had to be avoided. Especially when not only my own life but someone else’s was on the line.

*And… I haven’t played all my cards yet.*

Step. Step.

The Western Heaven Demon Lord and I. He and I. We slowly approached each other.

Unlike our first clash, neither of us launched finger qi or daggers.

We measured the distance between us, watched each other’s hands and feet, and waited for the right moment.

For a moment exactly like this.

Snap!

The Western Heaven Demon Lord moved first.

He erased thirty feet of distance in a single step, and his hand blurred. His snake sword, with its winding, serpentine shape, burned with ink-black Sword Force.

*Avoid a direct clash at all costs.*

If there was a gap even the System could not bridge, it was the existence of enlightenment.

Those who had attained the insight needed to reach Supreme Peak and those who had not—the difference between them was as vast as heaven and earth.

No matter how great my strength was, if I kept colliding with Sword Force, I would inevitably suffer internal injuries.

Whoosh! Boom!

The instant the Sword Force split the ground, a crater that looked like something out of a movie formed with a thunderous roar. If I had not barely evaded that strike, I would certainly have been cut in half.

I retreated and flicked my hand.

*Inventory open. Summon.*

Shhk-shhk-shhk!

I had never formally learned the art of throwing daggers, but daggers fired with tremendous force and speed possessed power all on their own.

Of course, that did not apply against the Western Heaven Demon Lord.

Slice!

A single horizontal line.

Ink-black Sword Energy shot out along the blade, slicing through the daggers as it flew toward me.

I tilted my head to the side. The intense heat and Sword Energy grazed past me.

Boom!

Ignoring the roar and vibrations echoing behind me, I planted my foot on the ground.

Grind. Crack!

The solid stone floor split like a spiderweb. In the next instant, I shot forward like a flash of light.

My speed was fast enough to be considered a Supreme Peak movement technique—or perhaps even faster.

“As expected!”

With a short exclamation, the Western Heaven Demon Lord swung his sword downward.

Ink-black Sword Force, dark enough to swallow the surrounding light, cut across my entire body.

If not for the single thought that had flashed through my mind before that split-second moment, it certainly would have.

*Thirty points each into Agility and Strength.*

Swoosh.

The change was dazzlingly fast. My entire body grew lighter, while my muscles gained density and springiness and squeezed out every last bit of strength.

As my body stepped on the wind, the ink-black Sword Force sliced through empty air.

Kraaaaaash!

I saw the Western Heaven Demon Lord’s eyes widen.

It was already too late for him to retrieve his sword. He hurriedly stretched out his other hand and tried to seize the spear approaching his chest.

His reflexes were astonishing. But if there was one other thing that astonished me, it was that my prediction had been exactly right.

*Inventory open. Store.*

Whoosh!

The Western Heaven Demon Lord’s hand, wrapped in Force, swept through empty air.

The spear that had seemed certain to be caught—White Flame—should now be safely tucked away somewhere inside my inventory.

And this was the moment I had been waiting for.

*Flame Divine Palm.*

My right hand, engulfed in blue flames, slammed into the Western Heaven Demon Lord’s abdomen.

Boom!

The moment his body rose slightly into the air amid tremendous heat, I swung the fist I had prepared with my left hand.

*Flame-Extinguishing Divine Fist.*

Crack!

The strike that had brought down a cliff slammed into the Western Heaven Demon Lord’s side.

The impact traveled through my fingertips. His body flew like a cannonball and slammed into the wall.

Bang! KRA-KA-BOOM!

The entire underground prison shuddered. At the same time, an unbearable weakness and hunger washed over me.

It had been an exchange in which I had poured my full strength into every movement. Naturally, ragged breaths spilled between my lips.

“Whew.”

Rumble.

I steadied my breathing and slowly walked forward through the piles of stone raining down around me.

The Western Heaven Demon Lord had been driven deep into the solid rock. He stared at me through a hazy gaze.

“I was definitely trying to catch the spear… How did you…”

“It’s probably similar to that supernatural power you believe in.”

“Cough. I see. Then was that also why you suddenly became faster?”

“Yeah. A few perfectly good lives were wasted because of you. They were bastards who deserved to die anyway, though.”

“What do you mean?”

“This is an underground prison. Don’t you notice anything strange?”

After a brief silence, the Western Heaven Demon Lord answered.

“…There are no prisoners.”

“Correct.”

“How did you do it? Did you perhaps use the Essence-Siphoning Great Technique on the prisoners?”

“You could say that, in a way.”

The difference was that the Essence-Siphoning Great Technique absorbed the opponent’s qi, while I sucked up EXP.

*Thanks to those guys, I earned sixty points. It was a stroke of genius.*

Instead of destroying the prisoners’ dantians, the Sichuan Tang Clan had chosen to suppress their internal energy and bind them in restraints.

That way, they could live longer. That way, the clan could make them taste hell through prolonged torture.

Thanks to that, the dozen or so prisoners—excluding the Heavenly Power Demon—were able to become nourishment for me.

“Cough. The Essence-Siphoning Great Technique. I see. So that was it.”

“Are you satisfied now?”

“If I ask, will you answer me?”

“Yeah. So…”

I looked down at the Western Heaven Demon Lord as he weakly nodded and continued.

“Quit the lousy acting and get up. And cut it out with those coughs that don’t even produce blood.”

“Well, this is something.”

The Western Heaven Demon Lord’s eyes, which had seemed ready to go out at any moment, curved into crescents.

“Apparently, I’m really no good at this sort of thing.”

“…Haa.”

You son of a bitch.
## Chapter artifact 359

# Chapter 359

Rustle.

After brushing the bits of stone from his body, the Western Heaven Demon Lord twisted his neck from side to side. His brow furrowed at the sound of bones grinding against each other.

“Your fists pack quite a punch. If I hadn’t had Body-Protecting Qi, I might have been seriously injured.”

*Punch, my ass.*

I let out a deep sigh as I watched the Western Heaven Demon Lord stand up without a scratch after taking both my full-powered Flame Divine Palm and Flame-Extinguishing Divine Fist.

“Forget the Body-Protecting Qi. Isn’t it cheating for someone like you to equip gear, too?”

“Gear? What is that?”

I pointed at the black-scaled armor visible through the tears in his yellow robe.

“That thing you’re wearing underneath. You bastard.”

“Ah. You mean the Black Dragon Armor.”

“The Black Dragon Armor?”

Now that was one hell of a cool name.

I didn’t know exactly what the Black Dragon Armor was, but its defensive performance was so impressive that calling it a divine weapon still wouldn’t be enough.

It had blocked two full-powered attacks, and all it had suffered was the loss of a few scales.

*With that level of defense, fists and palms won’t be enough.*

The armor worn by Dark Heaven’s ordinary martial artists had been formidable as well, but it was nothing compared to the Black Dragon Armor.

*An eye for an eye. A tooth for a tooth. A divine weapon for a divine weapon.*

As long as the Black Dragon Armor existed, White Flame was essential if I wanted to inflict a fatal wound on him.

*If not that…*

As I watched him searchingly, the Western Heaven Demon Lord smiled faintly.

“The more I see of you, the more interesting you become. Your strange techniques are one thing, but I like your refusal to back down.”

“So? Want to date?”

“I must politely decline. I already have a lover I’ve been with for a very long time.”

The Western Heaven Demon Lord gently stroked the winding blade of his sword. Ink-black Sword Force rose from the cut surface of the sword, which had broken cleanly in half.

“I’ve seen all your cards. Now it is my turn.”

With a quiet murmur, the Western Heaven Demon Lord stepped forward. A suffocating aura rippled behind his back like wings.

Only then did I realize it.

The Western Heaven Demon Lord’s martial arts had reached a realm far beyond what I had imagined.

“…Damn it.”

Deng.

Somewhere, it felt as though a bell had rung to announce the beginning of the second round.

But this wasn’t a boxing match that ended after twelve rounds. There were no spectators shouting cheers and groans, and no staff to throw in a towel.

This was a match that ended only when someone staked their life—nothing but their life.

*Inventory open. Summon.*

The cold spear shaft settled into my grip. I drew in a deep breath and leveled the spearhead at the Western Heaven Demon Lord.

“Come at me.”

The Western Heaven Demon Lord did not hesitate.

* * *

Snap!

The Western Heaven Demon Lord extended one foot.

*Shifting Form and Position.*

His vanished figure reappeared in the air above my head.

The sensation of my fine hairs standing on end reached me as I leaned my body backward.

Saaak! Boom!

The heel of his foot grazed my nose by the narrowest margin before slamming into the ground. The floor caved in, and fragments of stone flew in every direction.

Blood trickled from the bridge of my nose, sliced by the wind pressure, but I wasn’t given even a moment to wipe it away.

Shh-shh-shh-shhk!

Ink-black Sword Energy rained down from every direction. It slashed, cut, and swung without discrimination at my waist, chest, and stomach.

Attacks I could never have dodged in the past.

But not anymore.

*I can see them.*

Within the slowed-down world, I sensed the Sword Energy shooting toward me.

I could picture where that destructive energy would move and how I needed to move to evade it.

My body was already moving ahead of my thoughts.

Kra-kra-kra-kaboom!

I dodged some attacks and knocked others away with my spear. Thick clouds of dust rose everywhere, along with craters that looked like they belonged in a war movie.

And then…

Whooong!

Ink-black Sword Force, casting a dull light, shot out through the dust cloud. With a steady gaze, the Western Heaven Demon Lord brought his sword down along a diagonal line.

I had no way of knowing what martial art it was or what form he was using.

But I knew one thing.

If I backed down here, the only thing left for me was death.

*I have to strike back.*

I needed power strong enough to stand against Sword Force. This was the moment to use the best move I had.

The answer had been there from the beginning.

*One Annihilation.*

Grind.

Every muscle in my body drew taut like a bowstring. My foot shot forward first, followed by my waist, which had bent as far back as possible. Rotational force flowed through my shoulder and arm and poured into the spearhead.

Kraaaaaash!

It was a concentration of energy far too massive to be called Spear Energy.

The spearhead, wreathed in blue flames, surged forward. It burned through the air and devoured the dust cloud as it shot toward a single man.

“……!”

The Western Heaven Demon Lord’s eyes widened. At the same time, his blade trembled, and an even larger mass of Sword Force erupted from it.

The next instant, blue flames and black darkness collided.

KABOOOOOM!

With a roar unlike anything I had ever heard, everything within a radius of over a hundred feet shattered and exploded.

Part of the ceiling collapsed under the impact, and the incredibly solid rock was pulverized into drifting dust.

In the middle of it all, one person stood tall.

“Damn it.”

Even my full-powered One Annihilation wasn’t enough.

At my dejected expression, the Western Heaven Demon Lord shook his head. Blood was running down from his shoulder. That was all One Annihilation had left behind.

“There is no need to be disappointed. It was a sufficiently powerful form. For a moment, it was enough to make my heart turn cold.”

“Let me ask you one thing.”

“Anything.”

“If I hadn’t wasted my strength from the beginning and had launched that strike just now… could I have killed you?”

After thinking it over carefully, the Western Heaven Demon Lord answered.

“I believe you could have taken one of my arms. Perhaps even more than that. But you would have died.”

“Damn it. I knew it.”

“I think it is time to finish this.”

Whooooosh.

It no longer surprised me. Sword Force surged up like water from an inexhaustible spring and was swung like a whip.

I gritted my teeth as extreme weakness washed over me from the expenditure of my internal energy.

“It’s not over yet.”

I pulled up every bit of internal energy I had left and unleashed the Fire Dragon Divine Spear.

Unlike before, the blue flames were visibly smaller. They shot toward the Western Heaven Demon Lord’s exposed neck.

Screeeeeech!

The next moment, I met the unwavering gaze of the Western Heaven Demon Lord and realized it.

*He read me.*

By the time the realization pierced my mind, it was already too late. The Sword Force that had seemed ready to cut me in half abruptly bent in midair and struck the spearhead.

Boom!

A roar like the sky splitting apart rang out. I gritted my teeth as I clung to the violently shaking spear shaft.

The Sword Force swung toward me, my ankles already driven deep into the ground.

Shh-shh-shh-shh-shhk!

Above, below, left, and right.

Terrifying energy flew in from thirty-six directions centered on my body.

With every nerve in my body standing on end, I swung my spear like a madman.

Boom! Kra-kra-kra-kaboom!

Every time I blocked a strike, my body staggered and my breath caught in my throat.

This wasn’t a problem of speed or strength.

It was martial arts—and internal energy.

The Western Heaven Demon Lord’s martial arts were in a distant realm I could never reach, and the terrifying internal energy transmitted through my spear shook the inside of my body.

*What the hell…!*

Blood sprayed between my clenched teeth. My torn hands had been covered in blood for some time already.

I squeezed out every last bit of strength and swung my spear at the ink-black Sword Force cleaving toward my chest.

The second form of the Fire Dragon Divine Spear.

Heavenly Strike.

Screeeeeech! Boom!

But unlike the first time, the fire dragon’s claw was pitifully weak, and the Western Heaven Demon Lord’s ink-black Sword Force had not lost even a fraction of its power.

Krrrrk!

I was driven backward, carving a long furrow through the ground.

What I saw was the underground prison shaking as though struck by an earthquake, with thick clouds of dust filling the surroundings.

*He’s gone.*

I couldn’t see the Western Heaven Demon Lord ahead of me, to either side, or in the air.

Then there was only one answer.

I spun around and unleashed a palm strike.

Bang! Boom!

Two sounds rang out at the same time.

The heat of the Flame Divine Palm burned through the air, while the Western Heaven Demon Lord’s palm had already reached my chest.

My vision turned white, followed by the pain of my heart meridians snapping apart one strand at a time. I swallowed the blood surging into my throat and righted my flying body.

“That was amazing. I mean it.”

“……!”

It was instinct.

At the quiet voice coming from beside me, my arm moved on its own. The hand blade shooting toward the back of my neck struck my forearm instead.

Crack!

Pain surged through me with the sound of a bone being forced out of place. Then the Western Heaven Demon Lord’s foot, swung like a whip, drove into my side.

Thud! Boom!

After smashing through the rock and embedding me in the wall, the Western Heaven Demon Lord slowly walked toward me.

The emotions in his eyes were admiration and delight.

“Incredible. Truly incredible. Do you know what you just did?”

I spat out a mouthful of bloody phlegm and answered.

“No, you fucking bastard.”

“You may be proud of yourself. You lasted more than three hundred moves against me while I was fighting at full strength.”

“Three hundred moves. I’m crying tears of joy.”

“You do not seem particularly happy, so let me put it another way. What if the Heaven-Shaking Venerable Nun and her Elders had lasted more than five hundred moves?”

“No. Not at all.”

“Why not?”

The Western Heaven Demon Lord looked genuinely unable to understand. I tossed him a single answer.

“They died anyway.”

Even if someone lasted three hundred moves, five hundred moves, or a thousand moves, if they lost the fight, the only thing left for the loser in the end was death.

The Heaven-Shaking Venerable Nun and the Poison King had been no exception.

And…

I suppose I was no different.

“Cough.”

Blood seeped through my parted lips.

I wanted to stand up as casually as the Western Heaven Demon Lord had earlier, but my body was in no condition for that.

*Internal injuries aside, my left arm is fractured, and I think I’ve cracked some bones in my chest.*

I had really been beaten to hell. No wonder breathing had felt difficult for a while.

Breathing heavily, I used White Flame as a cane to pull myself upright.

At the sight of me, the Western Heaven Demon Lord’s eyes lit up.

“Do you still have something left to show me?”

“Of course.”

“That must also be the power of supernatural powers. Show me. Quickly. Quickly!”

“I was planning to.”

I leveled my spear at the Western Heaven Demon Lord, who was getting excited like a child.

And that was the entirety of what I did.

“……?”

“What are you doing? Aren’t you coming in?”

The Western Heaven Demon Lord stared at me with incomprehension and asked,

“What did you just do?”

“I’m showing you. The supernatural powers you wanted to see.”

“What?”

“I’m good with my body, but I’m hopeless with my head. I’m such a dumbass that I even failed the Level Eight Hanja exam.[^1] But then I came across the term ‘supernatural powers’ in a martial-arts novel. I didn’t know what it meant, so I looked it up.”

Even if I explained it like this, he probably wouldn’t understand half of what I was saying.

My vision wavered. Every time I exhaled, my lungs prickled as though they were being stabbed with needles, and the spear shaft that had always felt light now seemed like a boulder weighing ten thousand geun.

But still…

“‘Supernatural powers.’ Mysterious beings or phenomena that are difficult to explain through reason. That’s what it meant.”

I neither staggered nor collapsed. I simply stared at the Western Heaven Demon Lord and continued speaking slowly.

“What’s so special about supernatural powers? A bastard who keeps fighting even after being reduced to this state—that’s supernatural powers.”

Remaining Stat Points? None.

Physical condition? It was a miracle that I could still stand.

Now that everything had escaped as if from Pandora’s box, the one thing I had left was not hope.

*Sheer grit.*

Hope could make people stand back up, but it could also make them weak.

But as long as that grit remained—as long as I still had the will to fight until the very end—I would not fall.

No.

I had decided not to fall.

Because there were people I had to protect. The Fire King and Cheongpung had fought for my sake, so even if I had to become a ghost instead of some supernatural being, I had to stop this bastard.

“So…”

I gathered all the internal energy I had left. A fistful of qi desperately surged toward the spearhead.

A faint wisp of Spear Energy lit up the darkness like the glow of a firefly.

“Quit spouting bullshit and come at me, you bastard with a supernatural-powers fetish.”

The Western Heaven Demon Lord fell silent.

After countless emotions passed across his face, his gaze settled into a deep solemnity.

Swish!

[^1]: Hanja are Chinese characters used in Korean writing; Level Eight is a basic certification level, making failing the exam a mark of being exceptionally bad at them.

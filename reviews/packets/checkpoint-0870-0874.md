# Checkpoint Review — 870–874

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

# Chapters 870–874

## Plot

Taekyung and Prince Shangshan are escorted to the Emperor’s bedchamber, where the gaunt guide reveals himself as the Emperor—a Supreme Peak master who had concealed his strength even from Ma Sanbao. The Emperor probes Taekyung about Hong Jin, then questions Shangshan and proposes keeping him in the palace instead of sending him to Shanxi. When Taekyung challenges the Emperor’s sudden concern for a prince he neglected for years, assassins surround and wound him. Shangshan begs for Taekyung’s life; the Emperor orders First Shadow to execute Third Shadow for disobedience, then gives Taekyung a chance to say goodbye.

Shangshan accepts the Emperor’s authority and stops Taekyung from attempting an unprepared rebellion. Before they part, Taekyung gives Shangshan the Myriad-Poison Ring for protection, telling him to hide it and return it later. The Emperor reveals No Shadow, another concealed Supreme Peak assassin, and Shangshan leaves with palace attendants led by So Gyo.

## Continuity

- Shangshan remains in the imperial capital under the Emperor’s authority, accompanied by palace attendants led by So Gyo. Their true orders and the Emperor’s intentions for Shangshan remain unclear.
- Taekyung gave Shangshan the Myriad-Poison Ring as temporary protection against poisoning; Shangshan promised to keep it hidden and return it.
- The Emperor is a Supreme Peak master who concealed his strength and identity from Ma Sanbao. He has at least three Shadow assassins: First Shadow, Third Shadow, and No Shadow. He ordered First Shadow to execute Third Shadow for disobedience.
- The palace attendants assigned to Shangshan are First Rate martial artists armed with flexible swords.
- Taekyung chose to retreat rather than attempt to seize the Emperor. His System and Inventory remain unavailable during the update, and his condition worsens without the Divine Physician’s pills.
- Ma Sanbao and Hong Jin seek to enthrone Shangshan. Taekyung has not agreed to help them; how he and Hong Jin can protect Shangshan remains unresolved.

## Translation Decisions

- Render 흠천감 as “Imperial Astronomical Bureau” and 형부 as “Ministry of Punishments.”
- Render 합격술 as “combined attack technique,” 야명주 as “night-shining pearls,” 초절정 as “Supreme Peak,” and 황공 as “stand in fear and awe.”
- Render 삼영 as “Third Shadow,” 일영 as “First Shadow,” 무영 as “No Shadow,” 관내후 as “Marquis Within the Passes,” and 소교 as “So Gyo.”

## Durable state

{
  "active_continuity": [
    "Prince Shangshan has agreed to follow the Emperor’s will and remains in the imperial capital under the care of palace attendants led by So Gyo.",
    "Taekyung gave Shangshan the Myriad-Poison Ring for protection against poisoning; Shangshan promised to keep it hidden and return it.",
    "The Emperor has a concealed Supreme Peak assassin, No Shadow.",
    "The palace attendants assigned to Shangshan are First Rate martial artists who carry flexible swords."
  ],
  "continuity_sources": [
    874
  ],
  "open_questions": [
    "What does the Emperor intend for Shangshan, and what are the palace attendants’ true orders?",
    "Can Taekyung and Hong Jin devise a way to protect Shangshan?"
  ],
  "safe_through": 874,
  "temporary_decisions": [
    "Render 삼영 as “Third Shadow,” 일영 as “First Shadow,” 무영 as “No Shadow,” and 관내후 as “Marquis Within the Passes.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 870

# Chapter 870

For a moment, I doubted my own ears.

*What did I just hear?*

To be honest, even after arriving at the imperial palace, I hadn’t really thought I’d get to meet the Son of Heaven.

It was only natural.

He was the exalted ruler of this vast continent, above all others.

Compared to him, I was a lawless thug from the martial world without so much as an identification plaque, and no more than a son of the unimpressive Jin Family of Taiyuan.

Whatever standing I held in Murim, however much the Jin Family of Taiyuan had grown, none of it meant anything in the face of those two words: Son of Heaven.

This was the imperial palace, and he was the Emperor, with civil and military officials and countless subjects under his command.

And yet the Emperor, born of the dragon’s blood and having seized the realm through rebellion, had summoned me to an audience even Hong Jin wasn’t allowed to attend.

*Could this be the world’s lamest hidden-camera prank?*

I swallowed hard, then checked that I was still in working order.

I picked at my ear with my pinky, slapped my cheek two or three times with my palm, and steadied my breathing before I finally spoke again.

“Say that again.”

“What?”

“Say it again. Every last word.”

Jeong Hogun looked at me in silence, then answered without complaint.

“I said that only His Highness Prince Shangshan and Jin Taekyung of the Jin Family of Taiyuan had been summoned by His Majesty the Emperor.”

Judging by his unflappable expression, this definitely wasn’t a hidden-camera prank. I fell silent for a moment, faced with this unexpected reality, then asked again.

“Is this a dream or something?”

Jeong Hogun replied calmly.

“You slapped yourself just now. Pretty hard, too.”

“I did.”

“Did it hurt?”

“It did.”

“Then it wasn’t a dream.”

“I see.”

The second silence lasted a little longer. The first to break it wasn’t me, but Hong Jin.

“Why?”

“I don’t know.”

Jeong Hogun gave a brief answer, then added, “We, the Embroidered Uniform Guard, merely follow His Majesty the Emperor’s orders. We need no reason or explanation.”

Of course, that was the perspective of the Embroidered Uniform Guard, as government officials. My own situation was far more complicated than that.

*Why is he summoning me all of a sudden?*

I had a bad feeling about this. No—I already felt the back of my neck prickling.

Why was I thinking of Jeong Hogun’s manner, which suggested he had some idea what had happened last night, and Ma Sanbao’s face as he spoke of rebellion?

I felt a chill run down my spine and parted my lips.

“What if…I refused the invitation?”

Contrary to what I expected, Jeong Hogun answered in a casual tone.

“Do you have a reason to?”

“I haven’t been feeling well lately. Besides, like I said, I didn’t get much sleep last night.”

“If you’re ill, then there’s no helping it.”

“Oh. Really?”

“Of course. It would be best to move you to a different residence while we’re at it.”

“No, I appreciate the thought, but I’m fine. There’s no need to go that far…”

“Guards. Contact the Ministry of Punishments at once. Tell them to prepare the most spacious accommodations.”

“Huh?”

I blinked at Jeong Hogun.

Then I thought about it for a moment.

Was this the same “brother-in-law” as the one who’d married your wife’s older sister? If so, was Jeong Hogun the continent’s first transgender Imperial Guard? Or was it…

“Um. That Ministry of Punishments…”

“It’s nothing to worry about. It’s simply the institution that administers punishments under the Embroidered Uniform Guard.”

“……”

So it was a big deal. Shit.

I glared at Jeong Hogun, who didn’t so much as twitch an eyebrow, then held out my hand toward Prince Shangshan Zhu Bao.

“Shall we go, Your Highness? I’ll escort you.”

Then, as I followed the Embroidered Uniform Guard out of the pavilion, I heard Hyuk Mujin mutter with relief.

“Phew. Glad it wasn’t me. I really thought I was getting hauled off.”

You little shit.

* * *

The imperial palace was far bigger than I’d imagined.

Several times larger than the Forbidden City I’d toured on a school field trip with a VR headset.

The one saving grace was that the Embroidered Uniform Guard had the decency to prepare a palanquin.

“Please get in, Your Highness.”

“Huh? What about mine?”

“I’ll have to contact the Ministry of Punishments again.”

“……”

Of course, there was no palanquin for me. Only Prince Shangshan, a member of the imperial family, got to enjoy the luxury of riding in a four-man sedan chair carried by four Embroidered Uniform Guards.

“We’re moving.”

*Whoosh, whoosh, whoosh!*

At Jeong Hogun’s order, a golden current surged forward at tremendous speed.

I stayed close beside Prince Shangshan’s sedan chair, ready for anything, and took in every corner of the imperial palace.

*Couldn’t hurt to know the layout.*

Thinking about the worst-case scenario was one of my old habits.

Where each building stood, how many soldiers guarded it, and how strong they were.

If what awaited me wasn’t the Son of Heaven but a forest of spears and blades, I needed to find the fastest, most efficient escape route.

Especially if I had someone else with me.

—Your Highness.

At the Sound Transmission I sent discreetly, Prince Shangshan’s body gave a small jerk.

But it lasted only an instant. I sent another Sound Transmission to the young prince, who had quickly regained his composure.

—It’s unlikely, but…if the worst should happen, you must leave everything to me. Do you understand?

Prince Shangshan was just about to give a small nod when I noticed Jeong Hogun, riding at the head of the procession with his eyes fixed ahead, starting to turn his upper body.

I spoke a beat before he could.

“What are those people?”

Fortunately, my timing was perfect.

Half a beat later, Jeong Hogun glanced toward Prince Shangshan, then followed the direction of my finger.

*Splash. Splash.*

With every step, still-wet rainwater mixed with blood.

Surrounded by another group of Embroidered Uniform Guards, dozens of men were being dragged somewhere, covered in blood. Jeong Hogun saw them and answered.

“You can see for yourself. Prisoners.”

“Anyone can see that. I asked what they did.”

“Those men belong to the Imperial Astronomical Bureau. Or rather, they used to.”

“The Imperial Astronomical Bureau?”

“It’s the institution that observes and analyzes the heavens. And they’ll be punished for failing to predict last night’s lightning and torrential rain.”

“……”

“Don’t waste any more time on something so irrelevant. His Majesty is waiting.”

I answered with a silent nod, but the sight of the prisoners’ backs, already receding into the distance, wouldn’t leave my mind.

*These people are seriously insane.*

They’d beaten men half to death just because they hadn’t predicted the weather.

It felt far more brutal than something you could write off as the way things were in this era.

*No. Even for this era, that’s not normal.*

A change in perspective often revealed more.

Even as I hurried along behind the Embroidered Uniform Guard, I studied the expressions of the palace attendants, whose faces I hadn’t paid much attention to before.

Their faces and movements were stiff as wooden dolls. Whenever their eyes flicked toward the soldiers stationed all around them, I could see a tremor they hadn’t managed to hide.

*Everyone is afraid.*

By the Emperor’s will—or even by a single careless word—someone could be tortured or killed.

No matter how brave you were, you couldn’t refuse or voice your displeasure.

This was the imperial palace, where not even the smallest mistake was tolerated. The Emperor’s power must have been absolute, given that he’d climbed onto the throne after killing countless high officials and even his own blood relatives.

The cold, oppressive atmosphere pressing against my skin even now was something more than the mere nature of an era ruled by an absolute monarch.

*Terror rule.*

A wise and benevolent ruler embraced people with kindness as vast as the sea.

A tyrant, on the other hand, drove them into a thorny enclosure of his own making with spears and fear.

I’d heard plenty of stories, but never experienced it for myself. Even so, I could guess what kind of person the current Son of Heaven was.

And the biggest problem was…

*I’m walking right into his presence of my own accord.*

Out of habit, I reached into my chest. My hand met a small bundle containing pills made by the Divine Physician.

Remembering the unbelievably foul stench coming from them somehow made me feel a little better.

*If—I mean, if—I got into a fight here, what would happen?*

Whether I should call it reassuring or not, based on what I’d seen so far, the Embroidered Uniform Guard stationed in the imperial palace numbered in the thousands, perhaps as many as ten thousand.

That alone was enough to make a great army. Still, compared to the combined forces in the imperial capital and its surrounding areas, they were as lovely as fairies.

*The real issue is the Supreme Peak masters loyal to the Emperor. And the System is unavailable because of the update.*

Not being able to use the System was an enormous penalty.

With the System down, I couldn’t gain EXP, let alone recover by leveling up.

On top of that, my Inventory—the handy trick that had gotten me out of trouble with attacks my enemies never saw coming—was firmly shut.

*If I’d known this would happen, I should’ve taken White Flame out of my Inventory the last time I logged out in Murim. Or at least the Fire Dragon Armor.*

The reckless way I’d fought until now had been possible because I could level up. And I’d been able to beat masters in higher realms than mine thanks in large part to my Inventory and divine weapons.

But…right now, I had nothing.

No System to save my life in a dangerous moment. No divine weapons.

All I had was a bundle of pills that even the neighborhood mongrel would spit out, and a body that would get worse unless I forced myself to swallow the rotten-smelling things.

Oh, and I had a few other things, too.

A young prince and an eunuch I had to protect. And some damn idiot with a bad snoring problem.

*Perfect.*

At this point, I was almost tempted to ask Prince Shangshan to assassinate the Son of Heaven. I called out to Jeong Hogun, who was walking silently ahead of us, just in case.

“Hey, can I ask you something? Ever heard of *chokbeop sonyeon*[^1]?”

“Chokbeop what?”

“*Chokbeop sonyeon*.”

“What’s that? Never heard of it.”

“…Never mind.”

[^1]: A Korean legal term for a child too young to be criminally prosecuted.

Now that I thought about it, people were being strung up and killed through collective punishment. What good was the age of criminal responsibility here?

I pictured a sweet little fantasy that could never come true.

The Emperor, collapsed in a pool of blood. Embroidered Uniform Guards rushing in from every direction at the sound of a scream. And Prince Shangshan, grinning triumphantly with a dagger in his hand.

—Your Majesty! Your Majesty!

—Yeah. I killed my imperial brother, didn’t I?

—His Highness Prince Shangshan! What are you doing?

—The Embroidered Uniform Guard can’t do a thing, can you? Now I’m the Emperor, right?

—His Majesty has been assassinated! Apprehend the traitor Zhu Bao at once!

—Yep. I’m still too young to be prosecuted!

“……”

It was a sweet fantasy, but now that I thought about it, it seemed pretty serious in its own way.

Becoming Emperor because he was too young to be prosecuted.

If this were a Western fantasy setting, wouldn’t they call him Brat the First?

“Jin Taekyung. Why are you looking at me like that?”

“Ah, it’s nothing.”

I was trying to dodge Prince Shangshan’s question without revealing what I’d been thinking when it happened.

*Vrrrrmm.*

The air shook violently.

With an oppressive weight like ten thousand *geun*, two middle-aged men who looked exactly alike appeared and blocked our procession.

“Stop.”

“Stop.”

The twins, identical in face and build, spoke in unison. It looked a little ridiculous—but I didn’t laugh.

*Supreme Peak masters.*

No doubt about it. This place was a demon-slaying battleground.
## Chapter artifact 871

# Chapter 871

Even the Embroidered Uniform Guard, called the Emperor’s hands and feet alongside the East Depot, apparently had its limits.

Jeong Hogun led Prince Shangshan and me over to the middle-aged twins, whose names I didn’t know, and sent us a brief Sound Transmission.

—From now on, you must be careful with every word you say and every move you make. Otherwise, you won’t come out of here alive.

Who the fuck did that bastard think he was kidding?

I could already feel it in my bones.

Not just because of those twin Supreme Peak masters who’d appeared out of nowhere, but because of all the people inside the palace whose presence I could sense even though we hadn’t entered yet.

*This place is insanely well guarded.*

My mouth felt dry, as if I’d swallowed sand. I slowly drew on my internal energy, carefully enough that no one would notice, and moved my lips.

—Just answer me one thing. Why the hell was I summoned?

—I told you I don’t know.

Are you saying you really don’t know, or that you know but won’t tell me?

—Both.

Damn it. I was an idiot for asking.

I glared at Jeong Hogun, who stood with his usual impassive face, then passed beneath the plaque reading Qianqing Palace alongside Prince Shangshan, who had climbed down from his palanquin.

Clop. Clop.

Our footsteps rang out unusually loudly.

I quietly sized up the twins’ backs as they walked in perfect sync, their movements identical down to the smallest detail.

*They’ve definitely trained in a combined attack technique…but what martial art, exactly?*

No matter how I looked at it, the situation was bad.

Not being able to guess what martial arts they’d learned was one thing. Just imagining two fully accomplished Supreme Peak masters using a combined attack technique made my stomach hurt.

And on top of that…

*Why the hell are there so many bats?*

Shadows that didn’t show even in the faint light.

Those watching our every move from the darkness had to be imperial guards trained by the royal family—and assassins.

If the worst came to pass, those assassins, nearly a hundred of them, would carve me up with the one-strike killing techniques they’d spent their lives honing.

Along with the twin Supreme Peak masters, who looked as if they’d learned their combined technique in the womb.

*Unless you’re one of the Ten Kings—or maybe a master on par with the Three Saints—you’re almost certainly going to be buried here.*

People say the martial world is a mountain of sabers and a forest of swords.

But they’re wrong.

This was the real mountain of sabers and forest of swords. A place where the Emperor alone decided who lived and who died.

*How many masters does he have under his command?*

The Nine Sects and One Gang and the Five Great Families might have two Supreme Peak masters at most. Some had only one. And here the Emperor had two of them working as gatekeepers.

It felt as if I were walking along a blade’s edge.

Just then, as a bead of cold sweat trickled down the back of my neck before I even realized it, I noticed a small hand tugging at my sleeve.

Squeeze.

A hand gripping so tightly that my sleeve crumpled. Only then did I notice the young prince’s ragged breathing.

*He’s trembling.*

Before he was a member of the imperial family or a prince, he was a child.

He’d been the same the first time I met him, and nothing had changed now.

He’d said he left the imperial palace when he was so young he couldn’t even remember it. Of course he wouldn’t remember the Son of Heaven, either.

*And now his only family, his one and only older brother, is threatening his life.*

A thought suddenly occurred to me.

The cheerful side Prince Shangshan had shown on the way to the imperial capital—maybe it was an attempt to hide his fear and disappointment.

When Hong Jin warned him that the Son of Heaven was a threat and he shook his head, saying that couldn’t be true…maybe that was the only choice a child could make when faced with a reality too hard to believe.

*He shouldn’t have to understand any of this…but he’s had to grow up far too soon.*

My feelings grew complicated.

I thought of the boy from that winter in Shanxi Province, when icy winds howled through the mountains. He’d lost his parents and climbed a hill with his tiny, fern-like hands clinging tight to his little sister.

And I remembered young Hayeon patting our mother’s back as she lay facedown, sobbing at our father’s funeral.

*Damn it.*

I bit my lip hard to hold back a sigh.

Murim and the modern world had nothing in common. They were completely different worlds.

But there was one thing that never changed.

People.

That was why I, who’d once thought all of this was a game, had started accepting Murim as another reality.

They were people, after all. They got angry, felt joy, and grieved.

There were evil people who deserved to die, and good people with eyes as clear as glass.

I’d killed the former without a moment’s hesitation. When it came to the latter, I’d even risked my life to help them.

And now, I felt sorry for this young prince.

His trembling breaths reminded me of the young siblings who’d lost everything and fled after Jopil’s attack. His small hand clutching my sleeve made me think of my own little sister, Hayeon.

*I need to think about this coldly. I have to. I can’t afford not to…*

But no matter how much I thought about it, I wasn’t sure I could.

If I had to choose between treason and submission, could I really leave this child behind?

Could I look back on it years later as if it meant nothing?

*Man, he really knows how to make things difficult.*

I smiled bitterly and looked down at Prince Shangshan, who didn’t even reach my chest.

Then, almost on impulse, I raised a hand and gently patted his head.

“……!”

His eyes flew wide, and his lips parted slightly, as if he were about to shout that I’d overstepped my bounds. But Prince Shangshan only stared up at me in surprise, his mouth working soundlessly.

Instead, the hand that had been gripping my sleeve so tightly loosened, as though he felt relieved.

Who had ever dared to pat this child on the head?

Even this little thing that every child his age should have experienced was something Prince Shangshan, Zhu Bao, had probably never known.

*This is the best I can do for him right now.*

Just then, the twins, who had been striding forward without hesitation, stopped in front of a massive door.

Click. Grrrrr.

With a heavy rumble, an iron door swung open, its surface carved with a dragon so lifelike it seemed to move. The twins, who hadn’t said a word since we entered the palace, broke their silence.

“Please enter.”

“Please enter.”

It wasn’t as though we had any choice left.

Besides, hearing that we’d be separated from the Supreme Peak masters was a welcome surprise.

I nodded, then stepped through the iron door ahead of Prince Shangshan, shielding him as I went.

Rrrr. Thud.

The heavy door shut behind us with another rumble. Beneath the faint light of countless night-shining pearls glowing on the ceiling, a man stepped forward.

Clop.

A slender frame, as slight as his light footsteps.

He looked about fifty. A middle-aged man in a long robe whose sleeves dragged along the floor. Prince Shangshan spoke first when he saw him.

“Who goes there?”

Who goes there? Who goes there? Who goes there…

His tense voice echoed again and again through the empty corridor. Not another person in sight—not even an ant.

The middle-aged man gazed at the tense-faced Prince Shangshan and at me, standing slightly in front of him to shield him. Only when the echoes had faded did he speak.

“To see His Highness Prince Shangshan grown so tall, and from so close, fills me with deep emotion after all these years.”

After hesitating, Prince Shangshan asked, “Do you…know me?”

“Of course. Though Your Highness does not remember me.”

A faint smile appeared on his wrinkled lips. The man turned his gaze from Prince Shangshan to me.

“You’re a stranger to me.”

I chose silence instead of answering. The moment I saw him, I’d had to fight to keep a string of curses from spilling out.

Why? Simple.

The middle-aged man in front of me—no, this middle-aged man, too—was a Supreme Peak master.

*No, fuck me… This is so goddamn unfair.*

I’d only been at the imperial palace for two days.

And that was being generous. If you counted the actual time I’d spent here, it hadn’t even been twelve shichen—a full day.

And yet this was already the fifth Supreme Peak master I’d come face-to-face with.

*I’m so screwed.*

Just as I was seriously wondering if I should start wearing a condom instead of clothes, the middle-aged man spoke again.

“You needn’t tell me who you are. I already know. Jin Taekyung of the Jin Family of Taiyuan.”

Damn it. There was no way around it now.

I let out a deep sigh and answered.

“Does everyone around here recognize me wherever I go?”

“The imperial court’s eyes and ears are everywhere. And you do stand out.”

“Because I’m handsome?”

“No. Because you look like a thug at first glance.”

Listen to the way this guy talks.

“Then what do you do around here? The eyes? Or the ears?”

“Hmm. Which do you think I’m closer to?”

“The cleaning crew.”

“What?”

“Your sleeves are dragging on the floor, so I figure you must be great at mopping.”

The middle-aged man stared at me blankly for a moment, then burst out laughing.

“Ha ha. Just as I’d heard.”

“Heard what? Are the rumors already spreading?”

“I told you—there are eyes and ears everywhere. Everyone who needs to know already does. They’ve heard that some audacious martial artist dared to set foot in the imperial palace and has a knack for making people laugh.”

“That’s strange. I usually get under people’s skin more than I make them laugh.”

“I forgot to mention that ‘making people laugh’ was a considerably toned-down version of what I’d heard.”

“……”

“Of course, the stories I heard were all over the place, so I was curious myself. Now, this way.”

Without giving me a chance to answer, the middle-aged man spun around and naturally took the lead, not even looking back.

“Where are we going?”

“Interesting question. Have you forgotten why you came here?”

I’d had my suspicions, and I’d been right.

Apparently, this old guy was the third transfer point on our way to the Emperor—and the final guide who would take us to our destination.

*Obviously, he wasn’t a cleaner.*

Who the hell was he? His clothes didn’t offer much of a clue.

The East Depot? Or the Embroidered Uniform Guard?

His gaunt frame made him look more like a eunuch, but his voice was so weighty it could knock even an Embroidered Uniform Guard off his feet.

And there was the way he moved around as naturally as if this were his own home.

*Even the twins didn’t come this far. So he must be one of the Emperor’s closest, most trusted confidants…*

According to Ma Sanbao last night, the young Emperor was hot-tempered and suspicious. Only a handful of high-ranking officials and trusted servants who’d proven their loyalty were allowed into his residence, Qianqing Palace.

And that wasn’t all.

The guards, of course, as well as the eunuchs and palace attendants who stayed inside to see to every need…

This place had been created for the Emperor, by the Emperor, and in service of the Emperor.

Could just anyone come and go in Qianqing Palace—let alone somewhere this deep inside?

I didn’t know for sure, but he’d probably need to be close in standing to Baek Yeon, Commander of the Embroidered Uniform Guard.

*Then could this guy be the East Depot’s leader, the Director? No. I heard he was much older, and that he’d been bedridden with illness for years.*

I quickly racked my brain, but no one came to mind.

Ma Sanbao had mentioned far too many people, and the man didn’t match the distinctive features of any of the few he’d described.

*If only I could use my Qi Sense Skill right now…*

But there was nothing I could do about that.

If you’re thirsty, you dig a well.

I’d just have to pry the information out of him somehow.

Walking behind the middle-aged man as he strolled along at an unhurried pace, I tossed out a question.

“When do I get to meet the Emperor?”

“Soon.”

“At this rate, we’ll get there tomorrow.”

The middle-aged man gave a quiet laugh without looking back.

“You’re as impatient as you look. Just wait a little. His Majesty is enjoying a rare diversion.”

“Enjoying a diversion? After summoning us?”

“And what, do you intend to complain?”

“……!”

“Everyone has a place of their own. To ascend the throne means to look down upon them all. Isn’t that a simple and straightforward truth of the world?”

My expression hardened.

Not because I objected to the Emperor’s behavior, or because the middle-aged man’s answer had struck a nerve.

It was the casual look and tone he’d just shown me. The effortless confidence that came through in every small movement.

And on top of that, he didn’t look anything like any of the Emperor’s confidants Ma Sanbao had mentioned.

*No way.*

The moment I let out a quiet groan inwardly—

Clop.

The middle-aged man came to an abrupt stop. He threw open the door before them, decorated with gold, silver, and jewels, without the slightest hesitation, then spoke.

“Your Majesty. In accordance with your solemn imperial command, I have brought the two people you requested.”

But there was no answer from anywhere.

In fact, there wasn’t a hint of anyone else’s presence.

Only one person stood within this enormous bedchamber.

The middle-aged man.

He slowly turned around. Then he smiled at us, showing his white teeth.

“It was a brief diversion, but I enjoyed it.”

“……!”

“……!”

A bolt of lightning shot down my spine.
## Chapter artifact 872

# Chapter 872

“It was a brief diversion, but I enjoyed it.”

The moment I heard those words, a shiver ran down my spine.

At last, I’d figured out the middle-aged man’s identity. No matter how hard I’d tried, I hadn’t been able to place him before.

*The Son of Heaven…!*

The ruler of the continent, who governed all under heaven.

The man who’d seized the throne in a coup after bathing the imperial capital in blood a little over ten years ago.

I stared wide-eyed at the middle-aged man before me—no, at the Emperor.

*How?*

Even though everything that had happened proved who he was, that question still sprang to mind. It was because of what I already knew.

*He should still be somewhere around forty, shouldn’t he?*

When the young, ambitious fourth prince of the Great Nation launched his coup, he’d been no older than his late twenties.

A little over ten years had passed since then. At most, he should have just turned forty.

And yet…

*Even being generous, he looks over fifty.*

It was hard to write it off as mere premature aging.

How could the Emperor, the person above all others—not some country bumpkin who’d spent his life farming under the blazing sun—look this old? And on top of that, he was a master who’d reached Supreme Peak.

By comparison, the fact that the Emperor of the Great Nation was a Supreme Peak master wasn’t all that shocking.

Back when he was known as the fourth prince, he’d earned many military merits thanks to his exceptional martial talent.

Even so, that fact had also defied my expectations.

Suddenly, I thought of someone.

Ma Sanbao. The East Depot’s second-in-command, who’d spent the past decade and more serving as the Emperor’s right hand while hiding his own rebellious ambitions.

*Did he know about this?*

The answer to my question came instantly.

If Ma Sanbao had known, he would have told me long ago.

So there could only be one conclusion.

*Even Ma Sanbao didn’t know. No—that’s not quite right. The Emperor must have deliberately kept it hidden.*

A chill ran down my spine. Part of my conversation with Ma Sanbao the night before flashed through my mind.



‘The Emperor is a sinister man, and deep in his schemes. You can see it in how he still has the Embroidered Uniform Guard keeping the East Depot in check, even after all these years.’

‘But isn’t the East Depot also the Emperor’s right hand?’

‘Yes. More precisely, it was the late Emperor’s right hand.’

‘…!’

‘Do you know what all powerful people have in common? They’re suspicious. And then they’re suspicious some more. I still haven’t figured out how the current Emperor and Baek Yeon joined forces, but after the coup led by the Embroidered Uniform Guard succeeded, the East Depot became something the Emperor had little use for but couldn’t simply discard. He handles all his duties from Qianqing Palace and has been keeping to himself for years.’

‘Qianqing Palace?’

‘The Emperor’s residence. It’s almost impossible, but…if you ever find yourself face-to-face with him, be careful with your manners and think before you give even a short answer.’



The Emperor had hidden the truth even from Ma Sanbao, who was nominally the East Depot’s second-in-command but was, in practice, its leader.

So why—why on earth had he shown me this side of himself?

I couldn’t be certain of anything just yet, but at least some of what Ma Sanbao had told me that day was right.

The Emperor was sinister and deep in his schemes.

I could tell from the way he looked at me now, as if he could see straight into my heart.

“Ha ha. You look rather surprised.”

The corners of his mouth were raised, but not his eyes.

The Emperor had laughed aloud at my frozen expression, then continued in a low voice.

“Why? Is this quite different from what someone else told you about me?”

“……!”

For a moment, I couldn’t breathe. Through the air that had suddenly grown heavy around us, I could sense the Emperor’s intentions all too clearly.

*He suspects me…*

But now, more than ever, I had to stay calm. I tried not to let it show and answered him.

“Yes.”

“What?”

“I’ve already heard a few things from Hong Jin—or rather, the Deputy Military Commissioner of Shanxi Province.”

“Hong Jin, Hong Jin. It’s been a long time since I heard that name.”

The Emperor gazed into empty space as if reminiscing about old memories. Then he turned his sharp, shining eyes on me.

“So, what did he say?”

“He said Your Majesty distinguished yourself in martial arts early on and gained the throne at a young age, before you’d even turned thirty.”

“And?”

“That was all.”

“That can’t be all.”

Of course, it wasn’t.

But how was I supposed to say, “He said you were a fucking bastard,” right in front of the man who’d risen to the throne by killing even his own blood relatives?

Still, I couldn’t deny everything outright.

Hong Jin was a loyal retainer the late Emperor had cherished enough to entrust with Prince Shangshan’s care. The Emperor must have known long ago that someone like him wouldn’t have warm feelings toward him.

In the end, I had to come up with an answer that would keep the Emperor from suspecting me without getting Hong Jin hauled off by the Embroidered Uniform Guard.

The question was, would that even work…

*Fuck, I don’t know.*

At times like this, you just had to close your eyes and take the plunge.

I swallowed dryly and spoke.

“Actually, he did tell me more.”

“Speak.”

“Well, I can’t bring myself to say it myself.”

“What?”

“If you’re really curious, perhaps you could summon him later and ask him directly…”

The instant my voice trailed off—

Whoosh! Whoosh! Whoosh!

Sharp winds swept in from every direction. Dozens of men dressed in black dropped out of empty air, surrounding me as they leveled the weapons in their hands.

Shhk.

Had this been planned from the start? Or had anger, born of loyalty to the Emperor, driven them to it?

Blood welled from the cuts left by their keen blades, then rolled down my neck.

*These bastards… They’re serious.*

The black-clad men had me surrounded without leaving a gap. They felt as impassive as butchers slaughtering livestock, yet I sensed their desperate resolve to kill me the moment they received the order.

At the same time, a hand gripped my sleeve hard.

Squeeze.

It belonged to Prince Shangshan Zhu Bao.

The young prince had been frozen since the moment we learned the middle-aged man was the Emperor. I smiled at him, as if to tell him not to worry.

The Emperor had been watching us in silence. Suddenly, he shook out his voluminous sleeve.

Flap.

The black-clad men withdrew their weapons and leaped into the air with the flutter of his robes.

Their concealment technique was almost a divine skill. They seemed to melt away throughout the Emperor’s quarters, leaving behind only the faintest trace of their presence.

“Your Majesty’s men are certainly loyal.”

This time, I wasn’t being sarcastic.

At my genuine admiration, the Emperor replied in a dry voice.

“Loyalty isn’t all they have. They’re no match for the Slaughter Saint you’re close to, of course.”

“……!”

“What, did you think I wouldn’t know even that much?”

I fell silent for a moment. This time, I was genuinely surprised.

Everyone under heaven knew the title Slaughter Saint, but only a tiny handful knew that he’d reappeared after vanishing long ago.

Yet the Emperor knew not only that the Slaughter Saint was around, but that he and I had a connection.

He must have been drawing on the vast intelligence network he’d laid across the continent.

“Was that information from the Embroidered Uniform Guard?”

At my question, which slipped out after a moment of silence, the Emperor’s expression turned to a mix of displeasure and interest.

“You have remarkable nerve, asking me that.”

Even if I’d managed to get through what had just happened, there was no point in irritating the Emperor further.

Sensing an invisible line, I lowered my head.

“I’m sorry.”

“I stand in fear and awe, Your Majesty.”

“Pardon?”

“Not sorry. You should be in fear and awe. As everyone who addresses me is.”

The two characters for *hwanggong* each meant fear. It was the highest form of deference, befitting the Emperor’s absolute authority over all things.

The Emperor continued to stare at me intently even after he’d finished speaking. I spoke again.

“I stand in fear and awe, Your Majesty.”

“Better. You’re a lawless thug from the martial world, so I can’t expect much. But from now on, you can learn one thing at a time.”

A faint smile spread across the Emperor’s wrinkled lips. My stomach twisted.

But…

*First, I have to survive.*

I wasn’t the only one in danger. Everyone’s lives depended on my every word and action.

That included this young prince, who was clutching my sleeve with a trembling hand.

Just then, the Emperor’s gaze, which had been indifferent until now, finally settled on his only younger brother.

“Come here.”

At those words, the trembling I could feel through the fabric stopped.

It wasn’t because Prince Shangshan had regained his composure. He stood rigid as a statue as the Emperor spoke in a low voice.

“Do you intend to make me say it twice?”

“……!”

Prince Shangshan looked at the Emperor with trembling eyes, then lifted his head to look up at me.

He took a ragged breath, let go of my sleeve, and walked toward the Emperor.

No—he threw himself down in a full prostration and bowed.

“I-I, your subject, Prince Shangshan Zhu Bao, pay my respects to Your Majesty, my imperial brother.”

A heavy silence fell over the room, for a moment—or perhaps for quite some time.

The Emperor looked down at Prince Shangshan with eyes so deeply sunken that it was impossible to guess what he was thinking. His expression was cold enough to make it hard to believe he was facing his much younger brother.

Then he spoke.

“How old are you this year?”

“T-Twelve, Your Majesty.”

“You have good Muscles and Bones. Have you trained in martial arts?”

“Yes.”

“My brothers and I were always devoted to martial arts, even when we were young. Only our eldest brother was more like a civil official.”

Prince Shangshan drew in a small breath. He must have heard this and that from Hong Jin as he grew older, but hearing his family’s history from his only brother would have a different weight.

All the more so when that only brother was the Emperor of the Great Nation—a man he couldn’t treat like an ordinary sibling, and an enemy who’d sent his family to their deaths.

“I… see.”

“Taizu, our grandfather, founded the Great Nation through martial force, too. It’s part of the imperial family’s tradition. Looking at you, it seems blood really does tell.”

The Emperor added in a dry voice,

“Though I don’t know whether that will prove a poison or a boon.”

“……!”

“……!”

I barely managed to suppress the groan that was about to escape me.

Even before we reached the imperial capital, I’d already guessed that the Emperor’s intentions toward Prince Shangshan were anything but friendly. Even so, his response to the prince was far too blatant.

*Is he really that wary of him? His little brother, who’s so much younger?*

Power was ruthless.

People fought like beasts over the little wealth they had, even with their own parents and siblings. What would it be like over a vast continent, an entire empire?

But even so, the Emperor was far too thorough in his suspicion of his youngest brother, who was only twelve years old. In a way, he was right to be.

People were already emerging who dreamed of rebellion, led by Ma Sanbao.

And the Emperor’s next words were unmistakable proof that his wariness had already reached a point of no return.

“From now on, I’ll take care of you.”

“……!”
## Chapter artifact 873

# Chapter 873

The same words can mean different things depending on who says them and the circumstances.

That was true of the Emperor’s words at this very moment, too.

“From now on, I’ll take care of you.”

“……!”

At the unexpected words, Prince Shangshan jerked his head up from his prostration. I couldn’t stop a groan from slipping through my lips.

“Mm.”

That was probably why the Emperor’s gaze shifted from Prince Shangshan, prostrated at his feet, to me.

“Do you have something to say?”

Plenty.

But the man before me was the ruler of the continent. I lowered myself onto one knee and answered as politely as I could.

“If I may be so bold as to say something, Your Majesty.”

“If you think it’s so bold, you’d be wise not to say it aloud—if you want to keep your head attached.”

“……!”

“Still, very well. Go on, then. It might be interesting to see how much my patience has grown over the past dozen years.”

Those in power often dressed their whims up as patience.

Just like now.

*He’s really enjoying this.*

I lowered my head slightly as I watched the Emperor’s eyes gleam like a child who’d found an amusing new toy. I was trying to hide the way I’d clenched my teeth without realizing it.

Just how far did that arrogant Emperor’s patience extend?

If I crossed some invisible line he’d drawn, could I bear the consequences?

Questions like those suddenly flashed through my mind, but right now I had to do whatever I could to fend off the Emperor’s grasping hand reaching for Prince Shangshan.

*Stay calm.*

I took a small, steadying breath and slowly spoke.

“Your Majesty’s offer is truly gracious, but His Highness Prince Shangshan is already well cared for by his loyal subjects. In fact, he may not need anyone to care for him anymore.”

“Your manners have improved all of a sudden. You’re still far from skilled at hiding the barbs in your words, though.”

The Emperor looked at me with a mocking expression, then continued.

“Tell me, who are these loyal subjects you spoke of? That devious eunuch? Or that martial-world ruffian who flouts the Great Nation’s rules of propriety and roams the land?”

Everyone, even a stray dog, knew the former meant Hong Jin and the latter meant me.

But I didn’t so much as flinch. I bowed deeply and answered.

“Your Majesty is right that I belong to the martial world. I have roots in my family and my school.”

“So you are not my younger brother’s subject. Then what gives you the right to wag that tongue of yours in front of me?”

“Though I am not his subject, I was summoned as His Highness’s guest, and Your Majesty gave me permission to speak.”

“This is getting more interesting by the moment. But dress a beast in clothes, and does that make it a person? Don’t waste my precious time on pointless formalities that don’t suit you. Get to the point. Briefly and simply.”

Briefly and simply.

That was music to my ears.

But now was the time to bow once more, just in case. I looked down at the soft carpet and said,

“How could I do that?”

“Fifteen minutes should be enough.”

“Pardon?”

“For those fifteen minutes, I’ll forgive whatever rudeness you commit. Speak freely. That is my imperial command.”

Good.

With that safety net in place, I finally lifted my head, which I’d been keeping bowed. Looking at the Emperor, I said the words that had been circling the tip of my tongue.

“You already know, don’t you?”

“What?”

“His Highness Prince Shangshan has grown up well without Your Majesty’s care. He did so in the past, and he’ll continue to do so.”

“……!”

The instant the Emperor’s eyes flashed—

Whoosh!

Killing intent like invisible blades shot in from all sides and wrapped around me.

It was the killing intent of dozens of imperial guards—or rather, assassins—who had already revealed themselves once before. They’d all sent it at me at the same time.

Their individual martial skill was Peak, but their ability as assassins had reached Supreme Peak.

If they unleashed the one-strike killing techniques they’d spent their whole lives honing, staking their lives on them, even I wouldn’t get away unscathed.

But the thing I’d feared never happened.

The Emperor raised a hand before the sword light could reach me, stopping them in their tracks.

Shff.

The darkness on all sides rippled.

The Emperor gazed at me through narrowed eyes, holding back the assassins who seemed ready to drop from the air at any moment and carve me to pieces.

“Prince Shangshan doesn’t need my care?”

“Yes.”

“Do you not know he’s only twelve years old?”

“I do.”

“Then how can you say that?”

“Because that boy, who’s only twelve, dared to shout at the Commander of the Embroidered Uniform Guard—the man said to be able to knock even a flying bird from the sky.”

“……!”

“If someone else had told him to do it, then His Highness would still be a child in need of care. But no one there advised him to do so.”

Prince Shangshan had made the decision himself, and he’d carried it out without flinching.

I didn’t know if that was something he’d been born with or something his circumstances had gradually taught him, but it meant he was fit to be an adult.

The thirteen-year-old Prince Shangshan had already proved on his own that he could do what even adults who’d done nothing but age with the time handed to them could not.

“Deputy Military Commissioner Hong Jin, who has been with him for so long, treats His Highness like a child, just as Your Majesty does. But I see it differently. When I was a child, I couldn’t even have dreamed of doing something like that.”

“Of course not. You weren’t a member of the imperial family, or a prince.”

I shrugged and answered.

“I happened to meet one member of the imperial family. I can say with confidence that His Highness Prince Shangshan is ten times more mature than that person.”

“An imperial relative? You mean Ju Wongong?”

“You know about him, too.”

The Emperor even knew about the Slaughter Saint.

I didn’t know how deeply he’d dug into my affairs, but the fact that I was involved with one of the few members of the imperial family probably didn’t even count as noteworthy information to him.

At the sudden mention of Ju Wongong, the Emperor furrowed his brow.

“Everything ultimately comes from status and authority, not age. If this boy were no more than a distant imperial relative like Ju Wongong, do you think he could have shouted at Baek Yeon so boldly?”

“I’ve heard there’s nothing more pointless than arguing about something that never happened. And making the most of what you’ve been given isn’t something a child can do, either.”

At my smooth reply, the Emperor clicked his tongue softly.

“That tongue of yours is quite slick.”

“It’s one of my signature skills.”

“But can that signature skill of yours defeat an imperial command?”

“Pardon?”

“What if I issued an imperial command right here and now to revoke Prince Shangshan’s assigned territory in Shanxi Province, grant him the title Marquis Within the Passes, and keep him by my side?”

“……!”

*What a fucking bastard. He’s playing this argument like a real piece of shit.*

*An imperial command isn’t some damn Spirit Bomb.*

I forced down the curses that were about to burst out of my mouth and asked,

“If you do that, where will His Highness stay?”

It might have crossed a line. A ruffian from the martial world had no business asking about that, and the Emperor could have shouted me down with that very argument.

But the Emperor answered readily, like a judge watching to see how far I’d cross the line.

“He’ll return to where he belongs. He’ll stay in the imperial palace, study under excellent teachers, and receive the care of loyal palace attendants in an environment far better than barren Shanxi Province.”

“Would Hong Jin be among them?”

“I said loyal palace attendants. Not a devious eunuch like him.”

The Emperor was right about one thing and wrong about everything else.

The imperial palace was where Prince Shangshan belonged. But the teachers who instructed him and the attendants who served him would all be the Emperor’s people.

And…

*They’ll watch his every move for the Emperor and do whatever they’re ordered to do.*

Even if that order were to assassinate him.

By the time my thoughts reached that point, my mind had gone cold.

“If I may ask, Your Majesty, why are you going this far?”

The Emperor curled his lips with amusement as he answered.

“Because it’s only natural.”

“Natural?”

“I’m his older brother. I’m taking care of my one and only younger brother. Do I need another reason?”

“Of course not. I just find it a little strange.”

“What do you find strange?”

“Why Your Majesty, who hasn’t cared for that one and only younger brother for more than a decade, would suddenly decide to play the part of an older brother.”

Clang! Clang! Clang!

It happened in an instant. Before any order had been given, the assassins appeared again and surrounded me on all sides.

From behind the pitch-black mask of one of them came a growling voice.

“Do you truly want to die?”

I didn’t answer. I simply looked at the Emperor, whose expression I couldn’t make sense of, and spoke in an even tone.

“The fifteen minutes aren’t up yet.”

“You bastard!”

“Your Majesty made the promise yourself. You said you’d forgive any rudeness for fifteen minutes. I’ve only been following Your Majesty’s command and speaking honestly.”

“Shut that foul mouth of yours! How dare you—”

Slice.

A cold, burning pain. Blood ran down my neck, from a wound deeper than the one I’d already received there.

“Your Majesty!”

It was Prince Shangshan, who’d been frozen like a statue all this time.

Seeing me surrounded by assassins, he hurriedly turned to his one and only older brother.

“Jin Taekyung of the Jin Family of Taiyuan is my guest and my friend! Spare him! Please forgive his rudeness!”

Thud! Thud! Thud!

There was no time to stop him. The young prince prostrated himself and struck his forehead against the ground. I bit my lip, while the Emperor, looking down on the scene with cool arrogance, suddenly spoke.

“Enough.”

Everything stopped at that one word.

The dagger that had been slowly pressing into my neck, and Prince Shangshan’s desperate, humiliating plea to save me.

Then the Emperor continued, slowly, to his younger brother, who lifted his reddened forehead and looked up at him.

“That man dared to insult me. Even if I made a promise earlier, he crossed the line by a wide margin.”

“Y-Your Majesty…”

“But the fact remains that I made that promise myself. An Emperor cannot go back on his word. Isn’t that right, Third Shadow?”

The assassin called Third Shadow, who had been holding his dagger down as if ready to cut my throat at any moment, fell silent.

“You’re slow to answer.”

“……I beg your forgiveness, Your Majesty.”

“I clearly made a promise. Yet you disobeyed my command and tried to harm him.”

“Your Majesty, that was—”

“First Shadow. Carry it out.”

Slice. Shhk!

With a sharp cutting sound, the dagger under pressure slid away.

Another masked man dropped from the air and, without the slightest hesitation, slashed Third Shadow across the throat. Then he bowed before the Emperor.

“I have executed him.”

“……!”

“……!”

The air in the vast bedchamber froze.

After wiping Samyeong’s blood from my face, I stepped in front of Prince Shangshan, who was breathing in short, shallow gasps. This time, no one stopped me.

No—they couldn’t.

Their master, the one who held the power of life and death over them, hadn’t given the order.

*You fucking bastard.*

I glared at the Emperor, my eyes burning, and spoke.

“Your Majesty.”

“This time, you’d better choose your words carefully. The fifteen minutes I promised you are already up.”

“……!”

“And I’ll give you one last chance.”

“A chance?”

“Yes. A chance. I hear you’re Prince Shangshan’s friend.”

The Emperor laughed softly and continued.

“You’ll never meet again after this, so say your final farewells. That is the last act of kindness I’ll grant you.”

Shff.

The moment the Emperor finished speaking, I looked at the assassins closing in from all sides and understood.

There was no longer any way to protect Prince Shangshan here.

The Emperor had won.
## Chapter artifact 874

# Chapter 874

Perhaps the outcome had been decided long ago.

The imperial palace, a perfect enemy stronghold. A guard so tight that even “ironclad” didn’t do it justice. And the Emperor, ruler of all under heaven.

He alone had taken charge of the stage, the actors, and the direction. Even if I, a mere character, had entered the scene, the situation probably wouldn’t have changed much.

The thought came to me suddenly.

Perhaps all of this was a kind of amusement to the Emperor.

There was no particular reason to summon me along with Prince Shangshan. He’d brushed aside my words—words that could have gotten me branded a traitor on the spot—as if they were nothing.

And on top of that, he was now looking at my rigid face and sneering.

Crack.

A bone shifted with a sound from my tightly clenched fist. I scanned the impassive eyes visible above the assassins’ pitch-black masks, weighing my options.

*What do I do?*

The Emperor’s little game was daring—and supremely confident.

Naturally, all of us had been forced to surrender the weapons we’d brought into the palace. But beyond that, no restrictions had been placed on me.

Perhaps he was so confident that no one in the world could harm him, the Emperor.

But that choice had been an obvious mistake.

Even barehanded, I was a superhuman who had opened my Middle Dantian, an heir to the Fire Gate Clan who had inherited the Fire King Jeok Cheongang’s fearsome fist, palm, and finger techniques.

*All I have to do is take their weapons.*

With every shift of my gaze, an invisible path took shape in my mind.

A path to kill the assassins as quickly and efficiently as possible, then escape with Prince Shangshan.

The fact that the Emperor was a master who had entered the realm of Supreme Peak was unexpected, but that was all.

*He’s still at the threshold of Supreme Peak. What if I’m willing to sacrifice an arm and capture the Emperor first?*

If I took the Emperor hostage, it would all be over. The Great Nation was one enormous mechanism, and the Emperor was its most important component—and its master.

And if the Emperor fell into my hands, I could neutralize not only the assassins in here but also the twin masters waiting outside.

Perhaps even Baek Yeon, Commander of the Embroidered Uniform Guard.

*But… what then? What happens after that?*

Once I started, there would be no going back. That would be the beginning of a true rebellion.

If I took the Emperor hostage and fled Qianqing Palace, would the East Depot, led by Ma Sanbao, help us? Were the people who had signed the collective pledge he’d mentioned the night before fully prepared?

As all kinds of thoughts tangled through my mind—

“Your servant, Prince Shangshan Zhu Bao, will obey the will of my most august elder brother, Your Majesty.”

Prince Shangshan bowed deeply before his one and only elder brother, the Emperor and the highest person under heaven, then cried out at the top of his voice.

“Long live the Emperor! Long live the Emperor! Long, long live the Emperor!”

“……!”

My heart lurched.

Was it because Prince Shangshan’s sudden action broke the tension that had been squeezing my whole body?

No.

In the sight of that young prince, so small he couldn’t even reach my chest, I read a desperate, urgent plea.

*Don’t step in any further.*

It was as if a voice I couldn’t hear, a voice that couldn’t be heard, had sounded in my ear.

Prince Shangshan was trying to stop me. Before I could make an irreversible choice, he’d stepped forward first.

And an arrogant gaze looked down at him.

“……You’ve certainly grown.”

The Emperor murmured, his expression hard to read, and swept his sleeve. Prince Shangshan, who had been crying “Long live” and bowing again and again, understood and rose to his feet.

“Do you truly intend to obey my will?”

“Of course, Your Majesty.”

“That sounds like you’re saying it isn’t your own will. You may refuse if you don’t want to.”

The Emperor said that, but his narrowed eyes held another thought.

Prince Shangshan bowed his head in silence. Unlike before, his answer was utterly calm.

“It is my will, too.”

“I’m overjoyed that my brother and I are so much of one mind.”

“I am deeply honored.”

Prince Shangshan seemed to have accepted reality. At the sight of his calm expression, the tension drained out of me. I steadied my breathing.

*It’s no good.*

Prince Shangshan had made the right choice.

The conclusion was already clear.

We had to retreat when we weren’t prepared.

*At least for today.*

The Emperor watched me and smacked his lips, then suddenly spoke.

“Now that you’ve decided, there’s no need for further discussion. This audience is over. Everyone, withdraw.”

“As Your Majesty commands.”

As the assassins picked up Third Shadow’s body and melted into the darkness, the Emperor added,

“No Shadow. You too.”

Shff.

I barely held back a groan at the sight of the air rippling in place of an answer.

*This is insane.*

A Supreme Peak master whose presence even I hadn’t sensed.

No—not quite. A Supreme Peak assassin.

That was probably why the Emperor had been so untroubled about letting me into his chambers without imposing any serious restrictions.

*He’d been testing me to the very end.*

I revised my judgment of the Emperor at once.

He wasn’t merely arrogant and daring. He was more meticulous and suspicious than anyone.

*If you succeed, you’re the Emperor. If you fail, you’re a traitor.*

I hadn’t thought it through. When he was still known as the Fourth Prince, he’d drawn his sword just once, swung it, and overturned the imperial capital to seize the Great Nation.

A boldness and decisiveness no ordinary person could even dream of.

The thought suddenly crossed my mind: if I’d made a move, I would never have left Qianqing Palace alive.

*Damn it.*

Was this the power of the Emperor? The power of the Great Nation?

Was my best option really to withdraw so helplessly, unable even to protect a young prince?

“Let’s go.”

At Prince Shangshan’s quiet murmur, I turned away to hide my gritted teeth.

The Emperor, having finished his little game, had already disappeared behind the fluttering silks.

Rumble.

A massive iron door, ill-suited to such a splendid chamber, slowly opened. Standing beyond it were dozens of palace attendants I hadn’t seen on the way in.

“We greet His Highness Prince Shangshan.”

“We greet His Highness Prince Shangshan.”

The attendants bowed to Prince Shangshan with utmost deference. Every one of them was a striking beauty.

Each had the kind of exquisite looks that could topple kingdoms.

But one woman standing a step in front of the rest immediately caught my eye.

“Please call me So Gyo.”

So Gyo. That was the woman’s name.

Her voice was calm, and her eyes sparkled like morning stars. Even before you considered the beauty of her features, there was something unusual about her.

“By His Majesty’s solemn command, we have been assigned to serve His Highness Prince Shangshan. From now on, we humble women will attend to you, so please do not worry.”

It was simple enough to understand why none of them were heavily armed Embroidered Uniform Guards, despite being assigned to accompany a prince.

*They’ve trained in martial arts. And at a considerable level, too.*

Every one of them had the internal energy of a First Rate master.

I also immediately recognized that the thin belts at their waists were flexible swords.

And I couldn’t help guessing that if the Emperor gave the order, they’d be ready to drive those blades into Prince Shangshan’s neck at any moment.

*There’s no time.*

I was getting anxious. I had to meet Hong Jin as soon as possible and make a plan. I had to see through the Emperor’s hidden intentions, to discern his scheme.

“Your Highness.”

Prince Shangshan lifted his head at my call. The young prince looked at me with a calm gaze that might have been resignation, or composure, then turned to So Gyo.

“I’d like you to give us a moment.”

Working as a palace attendant in Qianqing Palace meant that they, too, were among the Emperor’s many loyal servants.

But So Gyo seemed to consider it for a moment, then quietly led the attendants away down the maze of corridors.

Only then could Prince Shangshan manage a faint smile.

“Speak. Though we may not meet again for some time, understand that the circumstances aren’t right for a long farewell.”

There was something about a child forced to grow up too soon that brought a lump to your throat.

But I couldn’t let my emotions take over.

I swallowed the words rising to my throat and held out my hand.

“First, take this.”

“……?”

“Come on. There’s no time.”

Prince Shangshan hesitated at my urging, then accepted the object.

He looked down at the small, glimmering thing in his palm and his eyes widened.

“This is…”

“My gift to you.”

Prince Shangshan examined it curiously, then asked,

“That’s the very ring you always wear.”

Prince Shangshan couldn’t know—and had no reason to guess—that its proper name was the Myriad-Poison Ring.

A divine artifact of the Sichuan Tang Clan, and one of the divine weapons Dark Heaven had targeted.

Unlike White Flame and Fire Dragon Armor, which I usually kept in my Inventory, this was a ring I wore at all times, just in case.

“Why would you suddenly give this to me?”

“I thought you might need it, Your Highness. You’ve shown an interest in it several times on the way to the imperial capital.”

That was true. We’d spent a long time in the carriage, and Prince Shangshan had been curious about everything I owned.

Even this ring, too clunky for the women of this era and awkward for a man to wear.

A few days ago, he’d even pestered me to give it to him.

*“About that ring.”*

*“Hm? Oh, this one?”*

*“Yes. The one you’re wearing. Would you give it to me?”*

*“Um, sorry, but that’s a little difficult. Have you always been interested in accessories?”*

*“No. I just want something of yours.”*

*“Oh, collecting keepsakes…”*

*“What was that?”*

*“Nothing. Just talking to myself.”*

*“At any rate, I’d like to have it. Of course, I’ll pay you handsomely.”*

*“I’m sorry. I can’t give this to anyone, and I couldn’t sell it for any amount of money.”*

*“Why not? Is it so precious that you’d refuse even my request?”*

*“Well, you see… Right. It was my father’s keepsake.”*

*“Oh.”*

*“It’s important not only to me, but to the whole family. My eldest brother still cries whenever he sees this ring.”*

*“I believe your father is still alive.”*

*“……Now that you mention it, I think it was my mother’s keepsake. I was mistaken.”*

The Myriad-Poison Ring was never supposed to end up in anyone else’s hands.

In the end, Prince Shangshan had been disappointed, and I’d promised to sign about five thousand autographs when we returned to Shanxi Province.

That was before I had the faintest idea what might be waiting for us in the imperial capital.

“Are you really giving this to me?”

“I’m not giving it to you for good. You have to return it later.”

“Didn’t you say it was your mother’s keepsake?”

“Uh. Well, you see…”

Just as I ran out of things to say, Prince Shangshan let out a quiet laugh.

“I already know you were lying.”

“Ah.”

“I’m a little disappointed that you’d lie even to me, but it’s all right. You must have had a reason. It must be that precious.”

I smiled along with Prince Shangshan.

“That’s right. It’s very precious, so keep it hidden from other people at all times…and make sure you return it.”

He wasn’t a precocious old soul for nothing. He understood the meaning behind my words.

Prince Shangshan hesitated, as if he didn’t know what to say, then nodded firmly.

“Mm. I understand. I promise.”

Only then did I feel a little more at ease.

The Emperor had ascended to the throne through a coup more than a decade ago, making countless enemies in the shadows and earning no shortage of blame.

The Emperor cared enough about having a legitimate pretext to summon Prince Shangshan to the imperial capital before bringing him under his control. If he meant to kill his one and only younger brother, the most likely method was poison.

*If Prince Shangshan keeps the Myriad-Poison Ring on him, poisoning him won’t be an option.*

That would buy me some time to come up with another plan.

I murmured to myself as I sensed the palace attendants slowly returning from farther down the corridor.

Our brief farewell was almost over.

“It’s time for me to go.”

Prince Shangshan murmured in a subdued voice. I bent down to meet the young prince’s eyes and answered,

“We’ll meet again soon.”

“I hope so. Then I’ll be able to repay the debt I owe you.”

“Your Highness.”

“Yes?”

“Don’t you know? Friends don’t owe each other anything.”

“……!”

“Still, if you insist on giving me something, I’ll accept it gratefully.”

Grinning, I ruffled Prince Shangshan’s hair.

The young prince stared blankly at me with wide eyes, then smiled, too.

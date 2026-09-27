# Checkpoint Review — 1115–1119

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

# Chapters 1115–1119

## Plot

The Slaughter Saint orders the South Gate defenders to retreat, with the elite troops covering them. He and the Bow Saint head for the Inner City and Jin Taekyung.

At the East Gate, Cheongheoja discovers that his Senior Disciple Hak Su is a Dark Heaven spy, Number Six. Hak Eui returns alive, exposing the disguised corpse used to fake his death. Hak Su and five other embedded spies take Temporary Strength Pills. The defenders spring a trap, letting two Black Ghosts and a thousand monsters into the gate before moving to close it. Hak Su is killed as a traitor.

The Green Forest Alliance, Yangtze River Channel League, and Dark Heaven forces approach from the east. Hyuk Mujin and the Fire Dragon Pavilion defenders fight the intruders. A captured jiangshi sorcerer uses ritual bells recovered near Qinghai Lake to confuse the monsters, though the bells cannot control the Black Ghosts. Mujin kills the sorcerer, and the roughly three hundred surviving monsters stop moving when the bell falls. Then an unidentified figure blasts open the East Gate and strikes Mujin in the chest; his vision goes dark.

## Continuity

- The South Gate defenders were ordered to retreat; the outcome is unknown. The Slaughter Saint and Bow Saint are heading to the Inner City.
- Hak Eui is alive. The corpse mistaken for him was a prisoner disguised with a human-skin mask by the Slaughter Saint.
- Hak Su, Dark Heaven’s Number Six, and five other spies embedded in Kunlun took Temporary Strength Pills. Hak Su was killed at the East Gate.
- Two Black Ghosts and a thousand monsters entered the East Gate. The ritual bells confused the monsters but did not control the Black Ghosts; the surviving monsters stopped moving after the jiangshi sorcerer was killed and his bell fell.
- The Green Forest Alliance, Yangtze River Channel League, and Dark Heaven forces are approaching from the east; they have not been shown reaching the East Gate.
- An unidentified powerful figure opened the East Gate and struck Hyuk Mujin in the chest. Mujin’s condition is unknown.

## Translation Decisions

- Use she/her for the Bow Saint.
- Render 大宗師 as “Great Master,” 육호 as “Number Six,” and 강시술사 as “jiangshi sorcerer.”
- Render 부각주 as “Vice Captain” for Hyuk Mujin’s Fire Dragon Pavilion title.

## Durable state

{
  "active_continuity": [
    "The East Gate battle continues amid Dark Heaven fanatics, defenders, and monsters.",
    "Hyuk Mujin killed the jiangshi sorcerer; roughly three hundred surviving monsters stopped moving when the ritual bell fell.",
    "A powerful unidentified figure opened the East Gate and struck Hyuk Mujin in the chest; his condition is unknown.",
    "The coalition approaching from the east had not yet been shown reaching the East Gate."
  ],
  "continuity_sources": [
    1118,
    1119
  ],
  "open_questions": [
    "Will Hyuk Mujin survive the blow, and who is the figure that opened the East Gate?",
    "What will happen when the approaching coalition reaches the East Gate?"
  ],
  "safe_through": 1119,
  "temporary_decisions": [
    "Render 부각주 as “Vice Captain” when Taishan addresses Hyuk Mujin."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 1115

# Chapter 1115

It was a fierce battle.

Unprecedented in all the history of Murim—a history stretching back a full thousand years, to the day a monk from a distant land crossed the Yangtze on a single reed leaf.

And at the same time, it was a bloodbath.

One the entire continent’s history had never seen, not just Murim’s.

CRUNCH!

A skull split open. Brain matter sprayed.

A death without even a final cry.

But no one grieved anymore for the end of a boy soldier who hadn’t even reached twenty.

No—they couldn’t.

In the relentless turning of this brutal hellscape, the word “death” had long since become cheap.

If there was one thing they could do for the dead, it was take revenge.

“The Lord of Heaven is with us……!”

The fanatic’s eyes were bloodshot as he stepped onto the wall, trampling the boy soldier’s corpse.

Thud.

A gleaming blade suddenly burst out between his brows.

“Who’s with you?”

Of course, the fanatic—already dead—couldn’t answer.

The small shadow pulled a dagger from the back of the corpse’s head as it crumpled like a rotten log, then strode toward the other enemies, still caught up in the joy of having seized the wall.

Whoosh.

The figure vanished like a ghost.

The Sword Energy that came flying a beat too late shot toward the space where the shadow had stood, but a cool breeze from somewhere had already swept past them.

Slice—SPLAT!

A fountain of blood arced into the pitch-black night sky.

Blinding speed, paired with efficient movement that wasted nothing.

But the shadow—no, the Slaughter Saint—had just cut down dozens of enemies in the blink of an eye, and his eyes were sunk deeper than ever.

*I’ve reached my limit. I can’t hold out any longer.*

He wasn’t talking about himself alone.

The South Gate, once an impregnable fortress thanks to the presence of two giants—the Slaughter Saint and the Bow Saint—was faltering. Every last defender stationed there was wavering.

*It was a miracle we held out this long.*

Perhaps this had been an impossible fight from the start.

Their side had even needed to call up commoners, while the enemy were all trained in a certain level of martial arts and had used Temporary Strength Pills as well.

They were hopelessly outmatched in both numbers and quality. The only reason they’d managed to hold on at all was that they’d made the most of the advantages of defending a fortress and deployed their small elite force wherever it was needed.

But—

*So this is as far as we go.*

The Slaughter Saint swallowed the groan at the tip of his tongue and looked around.

Beyond the unrelenting downpour, the scene before him was a sea of corpses and blood.

His own forces were collapsing, gripped by exhaustion that had carried them far beyond the limits of their will.

Everyone was tired.

Their bodies were heavy as waterlogged cotton, and all they could manage was to keep their minds from giving way.

Even the Slaughter Saint felt the weight of his exhaustion and his dantian running empty.

*If only we’d taken out the Grand Mage. If we’d managed that, we might have had a chance to counterattack……*

But the Grand Mage had been no easy opponent. If anything, she was more formidable than he’d heard.

The enemy’s defensive formation around the hundred or so mages, including her, had been as solid as an iron wall. When the Slaughter Saint threw everything he had into breaking through its center, he found no fewer than four Black Ghosts waiting for him.

And they had all been strengthened by every kind of enhancement spell.

If the greatest archer under Heaven hadn’t helped him—a man who could tear apart a target from hundreds of jang away—even the Slaughter Saint would never have made it back in one piece.

Still, he had managed to defeat two Black Ghosts. That was an achievement born of his pride and sheer determination.

Sssshing!

A brilliant flash suddenly erupted, shattering his brief reverie.

BOOM!

A massive beam of light swallowed and exploded among the twenty or so fanatics who had been charging at the Slaughter Saint from behind.

“You seem relaxed. Even enough to daydream.”

In response to the Bow Saint’s pointed remark, the Slaughter Saint flicked his sleeve.

Thud-thud-thud!

The enemies who had been aiming their bows from unseen blind spots crumpled all at once.

Every one of them had a long, slender ox-hair needle embedded between the brows.

“I wish I looked relaxed, like you said. Maybe then those bastards would be at least a little scared.”

“Do you think they still have any fear left in them?”

“……Damn it.”

With a bitter curse, the Slaughter Saint launched himself forward again.

To protect as many of his allies as he could from those fiends who had mortgaged their very souls to the two words “fanatical faith.”

Slice! CRACK!

He cut, stabbed, and broke whatever was in his way, striking down one foe after another.

But that was all.

No matter how tirelessly the two giants who had once adorned their age cut down their enemies, the resistance of their exhausted defenders quickly faded, and the fanatics’ fervent voices overwhelmed the wall.

“Great Lord of Heaven!”

“Let your majesty and power descend upon this land!”

Grit.

Feeling as if he were facing a massive wave, the Slaughter Saint clenched his teeth without realizing it.

For every hundred he killed, a thousand came. For every thousand he cut down, tens of thousands stood behind them.

He could hardly help wondering if this battle would ever truly end.

*What the hell are we supposed to do……?*

Even the thought that came to mind refused to take shape.

He was human, made of flesh and blood—not an all-knowing, all-powerful god.

*……This is the first time. The first time I’ve wanted to see someone this badly.*

Was it because of the large and small wounds etched across his body?

Or because his internal energy was rapidly running dry even now?

Caught in the exhaustion and emptiness he’d forgotten, the Slaughter Saint suddenly thought of someone who, long ago, had always brought him confidence and certain victory—even when facing a Demonic Cult army more than ten times their size.

*Martial God, what would you have done?*

It was a foolish question.

If he were here, he wouldn’t have entertained such doubts in the first place.

That was the kind of man he was.

A true heaven, beyond the reach even of the three brightest stars in all the Murim world.

And yet, for some reason, at that very moment, the Slaughter Saint found himself thinking of someone else.

*Jin Taekyung.*

The master of the Morning Star, the new star Dharma King Hong Dao had once spoken of—and now the young man who had drawn the Lord of Heaven’s inexplicable obsession.

And—

*The Chosen One.*

The Slaughter Saint couldn’t be sure of anything.

Was all this merely a coincidence, or was it a fate decided long ago by someone high above in the distant heavens?

All he could do was hold on to his one hope with all his might.

Even if it was no more than a handful.

Slice!

Force streamed from the dagger as it cut through the air, bending like a whip and sweeping across the wall.

Amid scattered limbs and overflowing blood, the Slaughter Saint gathered what little internal energy he had left and slaughtered his enemies in a single sweeping attack. Then he parted his tightly closed lips.

“Everyone, retreat.”

“……!”

“……!”

The defenders, who had barely been holding on, stared wide-eyed. But the Slaughter Saint had already made up his mind, and there wasn’t a hint of wavering in his voice.

“Messenger, take word to the South and North Gates immediately. The elites stationed at each gate will cover the rear and buy us some time. The rest of the troops are to retreat as quickly and orderly as possible.”

Silence pressed down on the space between them. It lasted only an instant, yet felt like eternity.

To them, abandoning the wall meant that the word they’d been trying so hard to ignore—defeat—was finally becoming real.

But there was only one person there who could oppose the Slaughter Saint’s decision, and she was watching him with an unshaken gaze.

*In the end, is that the best we can do?*

A line of Sound Transmission settled in his ear.

Without looking away from the Bow Saint, the Slaughter Saint answered calmly.

*I don’t know. But…… I want to believe.*

Yes. That was all.

The one person chosen by Dharma King Hong Dao, who had read the heavenly patterns.

By the Blood Lord, who had thrown those very patterns into disarray.

And by the Martial God, whose life or death was now unknown.

*I want to see it clearly with my own eyes. Where coincidence ends and fate begins.*

Even if a wretched end awaited him, the Slaughter Saint would never regret it.

The young brat he’d watched as Mungyeong—not as the Slaughter Saint—had the bearing of a Great Master worth risking one’s life for, regardless of age or martial prowess.

Everyone felt the same way.

*Bow Saint.*

At his quiet call, the Slaughter Saint looked at the Bow Saint, his gaze sunk deep.

*I don’t know exactly what you have in mind. But there’s one thing I do know. No—anyone who’s been even a little close to Jin Taekyung knows it.*

*……*

*No matter how much you distance yourself and try to keep your mouth shut, you just can’t bring yourself to hate that boy.*

*……!*

*I want to believe in him. And in you, too.*

Her pupils wavered for an instant.

But the Bow Saint’s agitation—and her silence—didn’t last long.

Fwoosh!

Far above them, enormous balls of fire that evaporated even the torrential rain came pouring down like a meteor shower.

Sssshing!

The Bow Saint’s hand moved with the speed of lightning, and a dazzling arrow of light shot forth.

KABOOM!

The sky turned red with a crash that seemed to split heaven and earth.

Beneath the massive and small fireballs that fell in hundreds, then thousands of pieces, the Bow Saint watched the scene with a grim expression before speaking.

“I honestly don’t know what choice I should make.”

Just as the Slaughter Saint was about to groan, she quietly added:

“Still, I want to believe, too.”

“……!”

“Come with me. To the Inner City. To that boy.”

At last, a faint smile touched the Slaughter Saint’s tired lips.
## Chapter artifact 1116

# Chapter 1116

As everyone knew, Xining Fortress—the last line of defense in Qinghai—had an enormous advantage when it came to defending against a siege.

But looking back over the dozens of battles fought over the years, it wasn’t just the fortress’s high, sturdy walls that had given invaders their worst nightmares.

“As expected, even those Fiends can’t cross the moat easily.”

At the middle-aged Daoist’s admiring murmur, Cheongheoja, the Sect Leader of the Kunlun Sect, nodded.

“If we didn’t have that moat, this fight would be twice as hard as it is now. The gates would have been breached long ago.”

Cheongheoja spoke the truth.

Even now, the moat—which was more than ten jang wide and quite deep—was forcing the enemy to pay a terrible price.

And that wasn’t all.

Even if they crossed the moat, they would face the fortress gates, made of immensely thick black iron. No matter how skilled in martial arts Dark Heaven’s fanatics were, they had no choice but to accept the losses and climb the walls rather than attack the gates.

Of course, the walls had occasionally been in danger, perhaps because of the enemy’s overwhelming numbers and the power boost from their Temporary Strength Pills. But at least at the East Gate, which they were defending, the siege was going more smoothly than anywhere else.

So smoothly, in fact, that they could almost believe they might win if they just kept things as they were.

The middle-aged Daoist standing beside Cheongheoja seemed to feel much the same.

“If we win this battle, we can all return to the main sect together, can’t we?”

“All of us together…… How wonderful that would be.”

At the deep, heavy note in Cheongheoja’s voice, the middle-aged Daoist’s expression turned bitter as well.

“Are you thinking about your Second Disciple?”

At the cautious question, Cheongheoja was silent for a moment, then shook his head.

“No.”

“Then……”

“I was thinking about the shortcomings of a foolish master who failed to guide his Disciple down the right path.”

“……!”

“It was my fault. From beginning to end. All of it.”

“Master……”

The middle-aged Daoist—Cheongheoja’s Senior Disciple, Hak Su—looked at his master with sorrow.

“Don’t blame yourself. It wasn’t your fault.”

“Is that what you think?”

“I know it. No—everyone in Kunlun knows. You kept your Second Disciple closer than anyone else and cared for him especially well.”

“I had to. Unlike you, who were always gentle, and your Third Junior Brother, who was full of energy, that child always seemed rough and unsettled.”

“And wasn’t that why you gave him the Daoist name Hak Eui?”

“Yes. That was certainly why.”

The boy had grown up in the dark, treacherous back alleys and gained a new name and a family. Cheongheoja had always told his rough-tempered Second Disciple to become a more righteous person, just as the name Hak Eui implied.

To never forget, even for an instant, that he was a Daoist.

“But…… who could ever have guessed? That he was a spy who’d been conspiring with Dark Heaven.”

Hak Su pressed his lips together and shook his head.

“To be honest, I still can’t believe it. And I don’t want to.”

His gaze suddenly shifted to the side.

For a moment, it seemed as if his Second Junior Brother might be standing there in his usual crooked pose.

But that wasn’t going to happen.

No. It was impossible.

Hak Eui was already dead.

Before dawn today, he had fought against those trying to capture a spy under cover of night, and in the end, he’d lost his life.

Hak Su had arrived at the scene too late. He’d seen his master holding his Junior Brother’s severed head and a sword dripping with blood.

He’d seen his master with eyes sadder than ever—just like now.

“……Master.”

Just as Hak Su was looking at Cheongheoja with a complicated expression—

Whoooosh!

A messenger came racing in, using his movement technique with all his might. His cry burst through the sharp whistle of air as he cut across the space.

“Sect Leader!”

He was covered in blood, and his face was as white as a sheet.

Cheongheoja swallowed the groan that almost escaped him and spoke in a heavy voice.

“Where have you come from?”

“South Gate. Hah…… South Gate.”

“Then the two Seniors ordered a retreat to the Inner City?”

“How did you……?”

“I understand. The situation must be the same elsewhere.”

There was no need to say more. From the messenger’s appearance, Cheongheoja had a rough idea of what had happened. He calmly continued:

“Go at once and tell them. I’ll lead the East Gate forces and join them in the Inner City shortly.”

“May you have good fortune in battle.”

The messenger left with a brief bow. Hak Su spoke, his expression stiff.

“Go ahead without me. I’ll buy you some time with part of the force.”

His eyes and voice were full of resolve.

But Cheongheoja immediately shook his head.

“I can’t leave you behind.”

At the concern in his master’s reply, Hak Su gave a faint smile.

“The road to the Inner City won’t be easy. No—it may be even more dangerous than here. They need you more than they need me.”

It was a perfectly reasonable prediction.

The dire news that the West Gate had fallen to the Blood Lord had reached the East Gate just before the war drums were about to be destroyed.

Unlike the East Gate, where the enemy forces were comparatively weaker than at the other three gates, a retreat without a plan might lead them straight into the Blood Lord and his fanatics, who could be rampaging unchecked through the fortress from the West Gate.

Even so, Cheongheoja would not yield.

“I forbid it.”

“Master, we’re out of time!”

Just as Hak Su shouted in desperation—

“Who is out of time?”

Cheongheoja’s voice sank strangely low, piercing Hak Su’s ear.

“……Master?”

“I asked who’s out of time.”

Hak Su blinked, bewildered.

And he wasn’t the only one who reacted that way.

The old Daoist’s presence had changed so suddenly that the Kunlun Disciples who knew him well—and all the soldiers nearby—were staring at Cheongheoja.

Then, through the rain, a voice no one expected rang out.

“Why hesitate to answer? Your Master, who’s as lofty as the heavens, is asking you.”

Splash.

A foot came down in a puddle, accompanied by a hard-edged voice.

At the same time, a man who looked to be around thirty took off his low-pulled straw hat. He stared at Hak Su with cold eyes and continued:

“Answer me, Senior Brother.”

“……!”

“……!”

A shock rippled across the wall.

No—it was more than shock.

Someone everyone had believed had crossed the point of no return had appeared before them. The man they had believed dead stood before them.

Unlike most of the people, who could not recover from the shock, Hak Su silently looked at his Junior Brother. Then he spoke in a calm voice.

“I thought you were dead.”

“If it looked that way, then I was.”

The man who had appeared so suddenly—Hak Eui—answered with a face set in stone.

He rubbed his neck, which had supposedly been severed last night.

“The fool who truly cared about you is already dead. And before dawn, I was born anew.”

“Then the head I saw……”

“You must have forgotten how crowded Xining’s underground prison is.”

Only then did Hak Su recall.

A few days ago, the Qinghai City Lord and several other leaders had been dragged into the streets and executed on the spot. But even after they were gone, well over a hundred prisoners had remained in the underground prison, waiting for judgment.

And there had been someone who could find a prisoner built like Hak Eui and craft a human-skin mask so perfect it deceived everyone.

“The Slaughter Saint.”

Hak Su murmured the words as if to himself, then gave a slight nod.

“So that’s what happened.”

His calm acceptance of what had happened left the onlookers who had been watching in disbelief murmuring.

Hak Su. It was him.

The traitor who had sided with Dark Heaven.

No one else but the Kunlun Sect Leader’s Senior Disciple had betrayed the sect he’d belonged to for thirty years.

Cheongheoja looked at his Disciple—whose actions he’d wanted to disbelieve until the very end—with an expression beyond words.

“Why……?”

At the brief question, Hak Su slowly parted his lips.

“Don’t seek reasons or question the mission you’ve been given. Think only of your assigned task.”

It was an answer—and a memory.

A newborn child, born on a land beyond a distant desert, had heard those words countless times before he grew into a thirteen-year-old boy.

A duty and a mission etched into his bones, impossible to defy even after decades.

“Heaven above and earth below, let ten thousand demons bow in homage.”

“……!”

“That is all there is. No further reason is needed.”

Hak Su met the eyes of the trembling man who had been his master, and continued.

His expression and voice were utterly unlike what they had been before.

“I used to tell you from time to time that meeting you by Qinghai Lake was the greatest luck of my life.”

He had meant it.

Cheongheoja was more deserving of being called a Daoist than anyone else. He had accepted his meeting with a boy wandering near Qinghai Lake as fate, never knowing the boy had made it look like chance.

“Thank you. I wasn’t especially gifted in martial arts, so even I didn’t know I’d reach a position like this.”

But Cheongheoja had never cared about status or talent.

Even if the Kunlun Sect hadn’t suffered devastating losses in the wake of the Great Faction War, he would have gladly accepted Hak Su as his Disciple.

Just as Hak Su had been raised to become a spy, Cheongheoja had always been that kind of person.

“It was all thanks to you, Cheongheoja.”

The instant a clear smile came to Hak Su’s lips—

“You dare, Hak Su—!”

Unable to watch any longer, Hak Eui roared in anger and shot forward.

And he wasn’t the only one charging at the traitor who had turned his back on his sect.

Whoooosh!

Their movement techniques were swift, their auras extraordinary.

The Kunlun Ten Guests, regarded as future Elders who would succeed the Kunlun Five Immortals and as indispensable pillars of the Kunlun Sect, drew their swords without a moment’s hesitation.

Slice!

A sword flash pierced the enemy’s torso, and hot blood gushed out.

Splatter. Thud, thud.

Blood sprayed across the wall.

Cheongheoja had stepped into his path. Over his master’s shoulder, Hak Eui caught sight of something unbelievable, and his eyes widened.

“What is this……!”

“I was getting tired of being called Hak Su.”

Hak Su watched the five corpses, their throats cut and hearts pierced, their breathing stopped. Then he—or rather, the Dark Heaven spy—slowly raised his head.

With the other shadows who had infiltrated the Kunlun Sect before him, or around the same time.

“Number Six. That’s my name.”

At that moment—

Crack.

The Kunlun Five Guests, now reduced to five—or, more precisely, the spies raised by Dark Heaven—pulled out the Temporary Strength Pills hidden in their robes and chewed them.

Sssssss!

Amid the enormous aura rising like a wildfire, Cheongheoja’s low voice rang out.

“I truly can’t leave you behind.”
## Chapter artifact 1117

# Chapter 1117

These days, nowhere in Xining could you find the word peace.

East, west, south, north—not even in the heavens above.

Rain and blood flooded every direction, while screams and crashes rang without pause.

And yet there was one exception: a hill rising tall several hundred jang from the East Gate.

*It’s really coming down out there.*

It was hardly the sort of thought someone in a life-or-death crisis could afford to have.

As he watched the sky pour down thick sheets of rain, as though a giant hole had opened overhead, the black-robed man suddenly turned east.

Whoooosh.

In the deep darkness, waves rippled beneath a fierce wind that swept over them like a storm.

After days of unprecedented rain without a moment’s pause, the place—which had once been a fairly level stretch of ground—had changed so much that it would not have been strange to call it a river.

Of course, that wasn’t what the black-robed man was looking for.

“Have they arrived?”

His companion abruptly asked the question, and the black-robed man answered.

“Not yet.”

“They’re later than expected. They should’ve had plenty of time to get here by now.”

“If they were diligent enough to keep to a schedule, why would they spend their lives robbing people?”

His companion, whose black hood was pulled low, gave a quiet laugh of agreement and continued.

“But I didn’t think they’d be this stupid. Even if they’re nothing but bandits with no proper roots, I thought they’d have at least a little skill or sense if they dared call themselves an Alliance.”

“Maybe this is the result of them thinking things through, in their own way.”

“What do you mean?”

“Even a pack of fools could guess they’d be used as cannon fodder. Most of them are little more than bandits, but their leaders—the Seafaring King and the Green Forest Battle King—know how to think.”

“So they’re deliberately dragging their feet to minimize their losses?”

“The weather’s gotten worse, too, but it’s certainly possible.”

“Even with a full ten thousand of our people keeping watch over those bandits?”

“Who knows? Even if we keep our eyes wide open, those water ghosts of the Yangtze River Channel League might pull something if they’re determined to.”

“Ha. If that’s true, they’re not just stupid. They’re beyond saving.”

At his companion’s clicking tongue, the black-robed man nodded.

He had not said it outright, but there was no one in Dark Heaven who did not know how cruel the Blood Lord could be once he started rampaging with no thought for what came after.

If the combined forces of the Yangtze River Channel League and the Green Forest Alliance arrived only after all the fighting was over…

*After today, the Central Plains will be clean. Not a single bandit in sight.*

But even those bandits still had a chance to survive.

If they arrived in time, before the East Gate opened, and managed to earn at least a little credit to save face, they could extend their tenacious lives just a bit longer.

Of course, that all depended on the Blood Lord’s mood.

*If you want to live, row with every last bit of strength you’ve got. That way, neither of us has to deal with a headache.*

Looking toward the East Gate, where a battle was raging, the black-robed man thought to himself.

What did he care whether a bunch of bandits lived or died? But for someone Dark Heaven classified as a jiangshi sorcerer, it mattered quite a lot.

The black-robed man’s role was less that of a soldier fighting on the battlefield and more like a member of the crew responsible for hauling away the corpses scattered across it.

And while he worried about the excessive workload, the course of the battle around the East Gate—swinging back and forth between attack and defense—was changing abruptly.

BOOOOM!

A deafening crash rang out of nowhere.

The immense noise swallowed not only the sound of the rain but even the thunder that had been striking from time to time. The black-robed man and his companion opened their eyes wide.

At the same moment, they saw the top of the fortress wall collapsing in a flash of light.

“What was that…?”

The black-robed man murmured, almost groaning.

It had lasted only an instant, but he was sure.

Even now, flashes of light were flickering without pause along the wall. He knew that destructive energy was Force.

*Why? We haven’t even pressed the attack. Why would Cheongheoja…?*

The Kunlun Sect Leader’s name flashed through his mind, but the black-robed man soon had to shake his head.

POP! RUMMMBLE!

Another distant flash burst into view.

The light within it was so pale and ominous that it could hardly have come from Daoist martial arts.

“It’s not the Black Ghosts, either. They’re still holding their positions as ordered.”

His companion’s voice came at just the right moment. He was right.

The two Black Ghosts were waiting on the battlefield in front of the wall, along with a considerable number of troops that the Blood Lord had deliberately held back.

“Which means…”

The black-robed man stopped himself.

If the one wielding that Force was neither a Black Ghost nor Cheongheoja, there was only one possibility.

Spies.

The spies they had planted in the Kunlun Sect over many years had finally made their move.

And a step ahead of schedule.

“What do we do?”

At his companion’s question, the black-robed man bit his lip.

It was a real pain in the ass.

The combined forces of the Yangtze River Channel League and the Green Forest Alliance, who should have arrived at the battlefield by now, were still nowhere to be seen. Meanwhile, the spies who were supposed to open the East Gate were caught up in an unexpected fight.

To make matters worse, Ma Sanbao—effectively their direct superior—wasn’t there today. In the end, the black-robed man had to make the call himself.

And he had to do it fast.

In the brief moment that felt like an eternity, the black-robed man stared at the East Gate, beset by a thousand doubts. Then he suddenly opened his eyes wide.

CLANK. GRRRRNNG!

With a heavy grinding sound, the iron bridge began to move slowly.

The massive bridge connected to the moat in front of the gate. It was coming down like a ray of light.

*The iron bridge connects to the gate. That means it can only be operated from inside.*

Then this was clear proof that the spies planted in the Kunlun Sect were opening the gate from within—and a perfect opportunity.

There was no point hesitating any longer.

“I command you: answer the call!”

The black-robed man shouted and pulled the ritual bell from his belt, shaking it with all his might.

Wooooong.

A sinister sound carried on the wind, sending a wave of force outward.

At the same time, the hill they had been standing on—or rather, the enormous masses of flesh that the rain and chaos made impossible to distinguish from a hill—answered the force.

GRRRRKK!

The ground shook as if an earthquake had struck. A horrible corpse stench rose from the rain-soaked earth and mud.

BOOM. BOOOOM!

The monsters shook off the mud plastered all over their bodies and rose to their full height on limbs as thick as tree trunks. There were a thousand in all.

Perched on the shoulder of one of them, the black-robed man shook his ritual bell once more and whispered:

“Wipe them all out.”

At that instant—

—KROOOAAAR!

With a roar as immense as their bodies, a thousand monsters surged toward the battlefield like a wave.

THUDDUDDUDDUD!

Was this what it would look like if the Yellow River flooded?

Screams rose belatedly from the wall as the monsters came charging in with a ferocious momentum no one could stop. But they weren’t the only enemies the defenders had to face.

—All. Troops.

—Charge.

A low voice emerged from beneath black armor.

At the same time, the two Black Ghosts who had been waiting sprang into action.

SHWOOOSH!

A ghost horse, its white bones exposed, raced forward like the wind, with several thousand fanatics charging behind it.

A roar that shook the battlefield rang out.

—Heaven above and earth below! Let ten thousand demons bow in homage!

—The Lord of Heaven is with us!

At the immense war cries from behind him, the black-robed man felt a thrilling shiver run up his spine.

Things had strayed a little from the original plan, but now such minor setbacks didn’t matter.

He had a literal army at his back. And behind the iron bridge, which had now descended nearly halfway…

*I see it!*

There was no doubt.

He wasn’t seeing things.

As the iron bridge lowered on its chains, the enormous iron gate began to open. The sight was clear in the black-robed man’s eyes, brimming with delight.

Tss-tss-tss-tss!

The two jiangshi sorcerers waved their hands with confidence, and the ritual bell danced in the air. The monsters, moving at full speed, shot toward the East Gate.

*We can do this.*

As time seemed to slow, the black-robed man held his breath and watched the battlefield.

Flashes of light flickered without pause atop the wall, which was shrouded in crashes and dust. The bridge, more than halfway down, now covered the moat.

The remaining distance was only a little over a hundred jang.

*Faster. Faster…!*

The monsters leading the charge thundered forward, their footsteps like thunderclaps. Beside them, the ghost horse carrying the two Black Ghosts galloped as if it were a specter.

Whoooosh!

A fierce wind wrapped around him. As the distance closed by the second, his heart pounded harder.

A little over a hundred jang became half.

Then half of that.

And at last—

GRRRNNG. BOOM!

The long, sturdy iron bridge came down over the moat.

BOOOOM!

Led by the two Black Ghosts, who crossed the bridge first, a thousand monsters surged toward the wide-open gate like one enormous spear.

KRRRRRUNCH!

Amid a terrifying crash and a cloud of dust, the black-robed man and his companion—who had finally broken through the East Gate’s defenses—let out the breaths they had been holding.

They had done it. By their own strength.

It was a flawless success, one no one could dispute—and a truly remarkable feat.

Even the merciless Blood Lord would have to acknowledge it.

At least for that moment, both men could rejoice to their hearts’ content.

SHWING—BOOM!

Until a dazzling flash of Force flew in from somewhere and shattered the thick chain connecting the gate to the iron bridge.

CLANK. RRRRRK!

It happened in an instant. No one could react in time.

“……!”

“……!”

As the two jiangshi sorcerers stared blankly at the gate, which had begun to close with a heavy crash, a hazy silhouette appeared beyond the dust cloud as it slowly settled.

SPLASH. SPLASH.

A staggering gait. A robe soaked in blood.

Then a middle-aged face gradually came into view, its eyes glowing red—the proof that he had committed a forbidden act.

“……You.”

The black-robed man slowly parted his lips.

At that moment—

Slice!

A streak of light suddenly shot out, slicing through the dust cloud and the middle-aged man’s—no, Hak Su’s—neck.

A voice, thick with sorrow and anger, followed.

“By the solemn rules of the Great Kunlun Sect, I will execute the traitors of our sect.”

THUD. FWOOSH.

As the headless body collapsed, the cloud of dust split apart.

Only then could the two jiangshi sorcerers clearly see what was around them. They finally understood.

It was not the spies who had lowered the bridge and opened the gate. It was the defenders who had been guarding the East Gate.

*A trap…!*

The realization flashed through their minds like lightning.

But the shock lasted only a moment. Seeing that there were fewer than three thousand defenders and that Cheongheoja looked exhausted, the black-robed man twisted his lips into a grin.

“You dare pull a shoddy trick like this?”

It was a trap—but at the same time, it wasn’t.

The fanatics following them had been blocked by the gate, but the most powerful forces—the Black Ghosts and the monsters—had already entered.

“Did you think you could stop us with this?”

A young man standing beside Cheongheoja answered his scornful question.

“Why not? We’ve had plenty of situations a whole lot worse than this. Right, everyone?”

At the sight of the young man, who looked like he’d be fun to torment, the black-robed man frowned. Just then, a young beggar, grime streaming down his face, spoke up.

“Quit calling me a beggar. It hurts the feelings of the beggar listening.”

“Who the hell are you…?”

“Honestly, we’ve been in this situation every time. I can’t even begin to figure out how much extra pay we should be getting.”

A young man with a cold expression cut the black-robed man off, followed by a clear voice that didn’t fit the mood at all.

“But we always make it through. Together.”

“That’s true, but this time’s different. The most important person isn’t here.”

“Right. Taishan wants to eat Pavilion Master. Old Man Nam, too.”

“Taishan. You mean you miss them, not that you want to eat them.”

“Oh, I got mixed up. Lord is smart, as expected.”

“Not bad. Still, not as good as me.”

The two jiangshi sorcerers had never seen these young men and women before. There was also a hulking man who looked none too bright, and a wild-haired eccentric.

Faced with the bizarre scene, the two sorcerers couldn’t even think of what to ask.

More precisely, they didn’t think it was worth asking.

“Wipe them all out.”

The ritual bell began to move with his quiet mutter.

Boooooo!

At the sound of a horn from far away, everyone at the East Gate stopped moving.

No—some heard it as hope; for others, it was the greatest despair.

“The Yangtze River Channel League…”

Someone’s low groan pressed heavily on the space around them.
## Chapter artifact 1118

# Chapter 1118

Boooooo!

The moment the blast of a horn rang out from far away and reached their ears, the defenders guarding the East Gate found themselves thinking:

*If only that sound, drawing closer by the moment, belonged to reinforcements rushing to help us.*

But the reality before them was cruel—and crystal clear.

“The Yangtze River Channel League……”

The groan that slipped from someone’s lips spoke for every defender.

They couldn’t see it, but they heard it loud and clear.

Not the west. Not the south. Not the north.

The horn was sounding beyond the East Gate wall where they stood. That could only mean one thing.

*They’re here.*

Everyone already knew the identity of the uninvited guests arriving from the east.

The Green Forest Alliance and the Yangtze River Channel League.

Two vast gangs of bandits who roamed the broad, blue rivers and mountains—and still weren’t satisfied, reaching for a piece of the world itself.

And, on top of that, the forces of Dark Heaven that must be accompanying them.

An enemy army estimated at no less than thirty thousand had finally appeared here, today.

Following the long course of the Yangtze, and even pushing upstream against the Yellow River’s mighty current.

At the sight of the defenders falling silent before this brutal reality, the two jiangshi sorcerers twisted their mouths into grins.

“You fools.”

“Do you understand now how shallow your little scheme was?”

The black-robed man and his companion made no effort to hide their delight.

They may have fallen for the defenders’ trap and ended up inside the fortress, but their forces alone were enough to easily offset a three-to-one disadvantage.

And now, tens of thousands of reinforcements had arrived right on time. They were almost embarrassed to recall how tense they’d been a moment ago, when they realized they’d fallen into a trap.

*Indeed, the Lord of Heaven is helping us.*

The black-robed man was smiling faintly as he thought of the new heaven he served when—

Step.

A group of people took a step forward. In a situation where they ought to retreat at once, they were moving forward instead.

*Of course. I knew the Kunlun fools would come out like this.*

The black-robed man gave an inward nod when he spotted Cheongheoja and the Kunlun Disciples at the front. Then, in the next moment, he saw a few faces pop out and line up beside them—and sighed.

“I’ve been meaning to ask for a while now… Who the hell are you people?”

If they’d looked even remotely ordinary, he wouldn’t have spared them a thought.

But the seven men and women made up a truly bizarre group, even by the standards of a jiangshi sorcerer. Unfazed by his reaction, they answered.

To be precise, for some reason, only the young man standing at the center spoke for them.

“Swift Wind Sword Hyuk Mujin. That’s who I am.”

The black-robed man’s eyes widened.

“Swift Wind Sword?”

“That’s right. So you’ve heard of—”

“Never heard of you.”

“…Fine. Let me introduce myself again. I’m Hyuk Mujin, Vice Squad Leader of the Jin Dragon Squad. Though I’m taking a little break from that job.”

“I haven’t heard of that either. You might as well keep taking a break. Not that you’ll be around in this world after today.”

“…Damn it. Then what about Hyuk Mujin, Vice Captain of the Fire Dragon Pavilion?”

This time, it was the others’ eyes that widened.

“What? Since when? Do Vice Captains get extra pay?”

“Why would they make Warrior Hyuk Vice Captain of all people? Wasn’t the position vacant?”

“I don’t know. Honestly, I thought I was the best fit among us, but I guess I’m being discriminated against because I’m from the unorthodox faction.”

“Discrimination. Know. Delicious.”

“Is this guy possessed by a glutton or what? I’ve never met anyone more of a deadbeat than my own Master, and I’ve been alive a long time.”

“Oh, so your Master’s a beggar too. No wonder. The moment I saw you, I thought you looked like you knew how to beg for a living.”

Greed and distrust they couldn’t hide even now. Disappointment with the orthodox faction’s rigged playing field. Endless appetite. And last of all, disrespect toward their Master and a steady stream of rudeness, as natural as breathing.

It felt like staring into the depths of a true abyss. The black-robed man and his companion were left dizzy.

If they hadn’t heard Hyuk Mujin’s answer just before, they might not have dared open their mouths at all.

But the three characters that made up Fire Dragon Pavilion were quite familiar to the jiangshi sorcerers.

Everyone in Dark Heaven knew them, regardless of rank. They were closely connected to one particular person.

“If you’re from the Fire Dragon Pavilion… are you Jin Taekyung’s people?”

Hyuk Mujin looked at his companions with a somewhat chilly gaze, then answered in a solemn tone.

“That’s right.”

“Thanks, but strictly speaking, I’m not with the Fire Dragon Pavilion. I’m from the Beggars’ Sect.”

“Neither am I. I think.”

“…Could the two of you please shut up for once? Please?”

The black-robed man studied them with a fresh look.

Because of his role and duties, he hadn’t known the minor details about Swift Wind Sword or the Jin Dragon Squad, but he had heard of the Fire Dragon Pavilion.

Whenever Dark Heaven’s grand plans were thwarted by the obstacle that was Jin Taekyung, hadn’t the Fire Dragon Pavilion made a name for itself by helping him? Its reputation had shaken the whole world.

He didn’t know why the one who looked most like a nobody was its Vice Captain, but he could understand how this strange assortment of people had ended up in one place.

And why they could step forward so boldly in a dangerous situation like this.

“Birds of a feather flock together. You’ve gathered all the crazy men and women who don’t value their lives, just like your Pavilion Master.”

The black-robed man let out a quiet laugh.

The Fire Dragon Pavilion?

He’d admit that they’d been a thorn in Dark Heaven’s side.

But they’d only managed that because Jin Taekyung had been there with them.

At that very moment, the members of the Fire Dragon Pavilion in his sight were nothing more than a group of young prodigies who hadn’t fully matured.

Puppies drunk on clumsy bravado and heroism, still unable to tell when to step forward and when to back down.

“The reason you’re going to die is that you didn’t run away while you had the chance, instead of wasting time spouting nonsense.”

What more was there to say to puppies whose teeth hadn’t even come in properly?

It was another matter if he faced an old, wounded beast quietly catching its breath for one last struggle.

*As long as there’s a Supreme Peak master here, we can’t let our guard down.*

*You worry too much. With forces like theirs, they can’t break through this and hurt us.*

The black-robed man and his companion silently exchanged glances. They watched Cheongheoja and the Kunlun Disciples, who aimed their swords at them with grim faces, and raised the ritual bells in their hands.

Tss-tss-tss-tss.

—Grrrrrr.

The thousand monsters groaned, stirred by the waves pulsing from the two ritual bells.

Each was as large as two grown men put together, with such toughness and regenerative power that they couldn’t be dealt a fatal wound without reaching the level of injuring others with Sword Energy. Ready to lunge at any moment, they fixed their eyes on the enemies before them.

Ssshhhh.

Alongside the two Black Ghosts, already radiating terrifying energy, they poured out such overwhelming killing intent that even the defenders—who had resolved to fight to the death—couldn’t help but take an instinctive step backward.

And then, at last—

“Kill every last one of them.”

The two jiangshi sorcerers swung their ritual bells through the air with a sharp command. At that very instant—

Tss-tss-tss-tss-tss.

The cursed sound waves, branded deep in the souls of the Black Ghosts and monsters, swept across the East Gate.

Along with a quiet voice coming from beyond them.

“Why would we run? We need to buy time by spouting whatever bullshit we can.”

“…?”

“…?”

The black-robed man and his companion stopped moving without realizing it and blinked blankly.

Was it because they couldn’t understand the words of that nobody—Hyuk Mujin, who’d butted in out of habit and now claimed to be the Fire Dragon Pavilion’s Vice Captain?

No.

Unlike the Black Ghosts, who were charging toward the defenders, a thousand monsters were trembling, their limbs shaking as if something invisible had bound them.

*I gave the command… So why?*

Just as the question suddenly crossed the two jiangshi sorcerers’ minds—

“Hey, can’t you do it?”

Along with the baffling question, one person appeared behind Hyuk Mujin, who had turned around. Someone they’d never imagined they would meet here.

“I tried to focus as hard as I could. Hngh. But there’s no way I can manage the Black Ghosts…”

“……!”

“……!”

Their eyes met in midair, and his voice trailed off.

The two jiangshi sorcerers stared wide-eyed at their missing companion. They’d thought he would be dead by now. Ever since the Slaughter Saint had captured him at Qinghai Lake, he’d vanished without a trace.

And they saw the dozen or so ritual bells in his hands—undoubtedly belonging to the other jiangshi sorcerers who’d died near Qinghai Lake—and the sad smile spreading over his bruise-covered face.

“Sorry. That’s how it went.”

At that moment—

SHWEEEE!

A dazzling streak of light cut through the darkness and blocked the two Black Ghosts, who were racing forward like the wind alongside their ghost horse.

KWA-BOOM!

A deafening crash sent a fierce wind sweeping in every direction.

At the same time, through the thick cloud of dust, Cheongheoja and a wild-haired eccentric—no, a Great Sir—appeared and spoke to the Black Ghosts.

“Where do you think you’re going?”

“Why don’t we talk this over first… Oh, that line was pretty cool.”

The two jiangshi sorcerers gritted their teeth as they realized another Supreme Peak master had been hidden amid the frantic fighting around the four walls.

And perhaps what angered them most at that moment was the insolent smile on the face of one nobody.

“If Captain—no, if the Pavilion Master were here, he’d say this.”

At Hyuk Mujin’s gesture, the captured jiangshi sorcerer shook the ritual bells in both hands like mad.

Not just one, but more than ten.

Tss-tss-tss-tss!

The desperate jingle, driven by a stronger instinct to survive than at any other point in his life, pushed him one step beyond the limit of his usual ability.

In other words—

—Ghk, grrk?

He couldn’t completely seize control from the two jiangshi sorcerers—yesterday’s companions, now his enemies—but he could throw the thousand monsters into confusion.

—Kraaaagh!

—Gueeeeee!

Their red eyes flashed wildly, their killing intent no longer fixed on its original target.

THOOM!

KRRRUNCH!

Freed from their restraints, the monsters began rampaging madly, no longer distinguishing between friend and foe. As the two jiangshi sorcerers froze at this unbelievable sight, Hyuk Mujin’s words pierced their ears like arrows.

“From now on, kill each other.”

Boooooo!

Over the horn sounding ever closer by the moment, the monsters’ ferocious roars mingled with the defenders’ shouts.
## Chapter artifact 1119

# Chapter 1119

BOOOOM!

A deafening crash rang out, and the ground shook.

A thousand monsters rampaged without distinguishing friend from foe, while three thousand defenders prepared to fight to the death.

And on top of that, four Supreme Peak masters flashed across the battlefield, constantly clashing as they tangled together.

The battle raging around the East Gate was more chaotic and brutal than ever.

Even the man who had designed and set this whole situation in motion could barely suppress his fear, despite putting all his strength into it.

—Kyaaaaa!

Hyuk Mujin watched the monsters charge at him, roaring ferociously. His eyes trembled.

They stood over one jang tall, with limbs as thick as the trunks of great trees.

Their immense strength and speed, far beyond human limits, made their charge feel like an unstoppable tidal wave.

*How in the world has Captain faced countless monsters like these?*

The thought came to him instinctively.

Jin Taekyung—the man who had always fought at the head of the group, at its center, risking his life.

And at the same time, Mujin understood once more.

Why he had survived every one of the countless crises they’d faced until now.

The enormous gap Taekyung had been filling alone, and the weight of the responsibility he’d borne.

*So this is what it felt like.*

With a question that would never reach its recipient, Hyuk Mujin let out a ragged breath.

He was afraid.

So afraid that he wanted to throw down his sword and run as far away as he could, right now.

*If this had happened before, I definitely would have.*

But everything was different now.

The heir to a venerable textile shop had become a martial artist of the Jin Family of Taiyuan, and he had already come too far to run away.

He had seen and learned so much from the people who had gladly taken someone as untalented and unskilled as him along for the journey.

Especially from Jin Taekyung.

“Don’t you dare retreat.”

The quiet words slipped past his trembling lips. They were less a warning to his allies than a vow to himself.

They were also words the Third Young Master, the reckless son who now existed only in his memories, had once said to him.

“The moment you retreat once… you’ll never be able to move forward again.”

And so Hyuk Mujin didn’t retreat.

He suppressed the fear surging up from the depths of his chest, steadied his trembling sword tip, and charged at the monsters with all his might, roaring at the top of his lungs.

Like Jin Taekyung had, and like the other companions who had always believed in him.

SHWEEEE!

A fierce wind whirled around him, wrapping his entire body.

* * *

Anyone who has experienced war agrees on one thing.

Battle is another word for madness, and war is the sum of that madness.

If you keep knocking down the enemy in front of you and dodging attacks flying at you without pause, before you know it, you forget everything you once knew.

Hyuk Mujin remembered those words clearly. He’d heard them as a child from an elderly man.

He also remembered what the old man had told him when Mujin declared he would become a martial artist.

*Hope is dazzling, but reality is cruel.*

Yes. That was probably how he’d put it.

And Hyuk Mujin once more learned, down to his bones, that the old man had been right about all of it.

THUD!

A heavy thump, and a powerful shock that shook him from head to toe.

There was no time to react.

No—even if he’d had time, he wouldn’t have been able to dodge it completely.

He’d run out of strength long ago.

KRRRUNCH!

How many times had the sky and ground turned over in his vision, bleached white? The first thing Hyuk Mujin felt after he was flung a long way was pain, great and small, sweeping through his body.

Cough.

Blood came up with his cough and ran from the corner of his mouth.

His aching joints and twisted innards told him the truth: he was in terrible shape.

*Damn… it.*

Hyuk Mujin gritted his teeth and swallowed down the blood welling in his throat.

Just as the old man—whose face he could no longer remember—had said, reality was cruel.

At least, it was for him.

*I’m in this shape after only fifteen minutes.*

Feeling his body, which barely had the strength to move, he gave a feeble, self-mocking laugh.

Losing control and going mad didn’t make the monsters any less powerful.

The monsters born of Dark Heaven were every bit as strong as their horrifying appearance suggested.

Even now, he couldn’t imagine bringing down twenty of them alone without the famous sword in his hand.

*When you think about it, the fact that I managed to fight this well at all is thanks to Captain.*

Hyuk Mujin looked at the sword in his hand.

Its keen edge remained sharp and clear, even after cutting through the monsters’ bones and flesh, hard as they were.

The sword had been made from the iron chain Jin Taekyung gave him, after finally breaking the iron balls just before the Star-Array Grand Banquet.

The very chain the Fire Gate Clan had made to restrain criminals within the sect.

Only part of the chain had gone into the sword, of course, but the blade contained a full four nyang of Ten-Thousand-Year Cold Iron. Its strength and sharpness more than earned it the name of a famous sword.

People who knew that often teased Mujin, saying the sword was too good for him. Though he always bristled at the jabs, deep down he knew the truth.

He’d received such a precious sword only because Jin Taekyung cared for his subordinate—even though Mujin himself had been stuck in the First Rate realm, making no progress.

“Seriously… he talks all sharp, but he still makes sure we have everything we need.”

With a snort of amusement, Hyuk Mujin slowly forced his screaming body upright.

Then he squeezed out what strength he had left and charged at the back of the nearest enemy.

Slice!

Maybe it was the exhaustion of a body that had reached its limit.

His sword tip wavered at the last moment, but he still managed to cut his target’s neck without the slightest trouble.

Especially since this time, his opponent was made of flesh and blood, just like him.

SPLAT.

The headless body staggered and collapsed into a pool of blood, but Hyuk Mujin’s heart sank as he looked down at the dead fanatic.

*If only we’d had a little more strength—just a little more…*

The strategy involving the captured jiangshi sorcerer had worked.

Most of the thousand monsters had fallen into confusion, and the three thousand defenders had charged into the chaos, forcing the enemy back with attacks that disregarded their own lives.

But the enemies they had to face weren’t all inside the fortress.

While the East Gate defenders threw everything they had into fighting the monsters, Dark Heaven fanatics had climbed over the walls with hooks and ladders. The moment they broke in, they had instantly tipped the balance of power away from the defenders.

Even now—

“……!”

“……!”

The familiar eight-character sermon, steeped in madness, rang dully through the air.

Fanatics kept streaming down from the walls. His allies were already exhausted. And, one by one, the monsters were starting to come to their senses.

All of it passed before Hyuk Mujin’s eyes.

Along with the powerful blare of a horn, now only a few hundred jang away, and the face of someone who had regained their smile as if nothing had happened.

—Your struggle ends here.

He couldn’t hear the words. But he could see them.

Far away, in front of the tightly shut gate, the black-robed man’s lips were moving.

Unlike his companion, who had been killed by the monsters he’d commanded as soon as the battle began, this man had managed to exert a measure of control. He was still alive, using dozens of monsters as a shield.

He was savoring a victory that had seemed uncertain for a moment but now looked all but assured.

*Yeah, maybe it really is over. But…*

If he ran away now, where could he win?

Hyuk Mujin muttered to himself as he staggered forward.

Not backward, but ahead.

Whoooosh!

Through his dulled senses, he felt a fierce rush of air.

A monster’s fist, carrying the strength of hundreds of geun, came crashing down toward the top of his head. The blow could have crushed him in an instant.

And then—

Slice.

A sharp streak of Sword Energy, swung from somewhere, cut through thick bone and flesh.

“It’s too late. If you don’t want to die, get back! Right now!”

A familiar face and voice.

But even with Song Ilseom trying to stop him, Hyuk Mujin didn’t halt.

More precisely, he heard nothing at all.

At that moment, only one person’s voice echoed in his ears like a hallucination.

—Mujin.

Jin Taekyung.

The person Hyuk Mujin most wanted to be like—and the person who had made him realize he never could be.

As if the owner of that voice were right in front of him, he parted his lips, caked with dried blood.

Remembering the conversation he’d had with Jin Taekyung before the battle began, he said:

“Yes. Go ahead.”

SHWICK!

A burst of air from his blind spot came back as the answer. But Song Ilseom wasn’t the only one who didn’t want Hyuk Mujin to die.

THUNK!

The fanatic who had charged at Mujin from the side bent backward like a bow.

Ju Hwaran pulled the sword from the back of the body as it crumpled limply. The dozen or so enemies who had been rushing to stop Mujin changed course and charged at her instead.

KRRRANG!

Amid the screams and shouts that never let up, steel rang out. Hyuk Mujin walked as if entranced, toward the path that had opened wider before him.

Leaving everything around him behind, he listened to the voice that kept ringing in his ears.

—If, I mean, if something goes wrong—just in the very unlikely event…

He had been different.

Jin Taekyung had definitely been different then from how he usually was.

With not a trace of laughter or playfulness, he’d said:

—At least die where I can see you.

And then, facing his subordinate, who had gone rigid, he’d forced a strained smile.

—Of course, that won’t happen. But if it did, I’d be able to avenge you, wouldn’t I?

It was the first time.

The first time Jin Taekyung had ever said something like that.

Until then, through all the dangers they’d overcome together, he’d only ever said two things.

Run.

Or make sure you survive.

No matter what danger came their way, Jin Taekyung was always the same.

Always at the center and out in front. He had never hesitated to lead the way in this damn game of chance where they wagered their lives.

To protect a subordinate, a companion, a Master.

Or even someone he’d never met before.

That was why Mujin couldn’t help but respect him, and why he had no choice but to give him the answer he wanted.

—Of course we’ll win this time, too. But yes. If it comes to that, I promise I will.

Maybe that was when it started.

When Hyuk Mujin began quietly turning the word death over in one corner of his mind.

When he truly prepared himself to die.

But…

*Even if I die, I can’t just throw my life away for nothing.*

Forcing up the corner of his mouth, caked with dried blood, Hyuk Mujin swung the sword he gripped tightly.

Slice!

The two fanatics in his path fell at the same time, as if they’d planned it together.

So easily. As if it were all part of a play.

Then, at the fanatics who had stopped short, eyes wide at this unexpected turn, a fierce torrent of saber energy swept in.

KRRRUNCH!

Beneath a fountain of blood, a cold voice rang out, at odds with the wild energy.

“Go. If that’s your choice… I’ll clear the way.”

That was all.

Sama Pyo plunged into the ranks of the enemy without hesitation, and a hard hand caught Hyuk Mujin’s shoulder as he briefly stumbled.

“Hyuk Mu…”

Hyuk Mujin quietly shook his head at Taishan, who trailed off.

He knew what Taishan wanted to say.

He wanted to tell him that even if they killed the jiangshi sorcerer—the black-robed man now just twenty jang away—the outcome wouldn’t change.

But Jin Taekyung would have said this:

Even if you died, this was a deal well worth making.

“Hur…ry.”

The words took all the strength he had left.

Taishan watched Hyuk Mujin in silence, then gripped him tightly.

And with one short sentence, he used all his strength to send Mujin flying far away.

“Let’s go eat something good later, Vice Captain.”

SHWEEEE!

Feeling the fierce wind pass over his entire body, Hyuk Mujin answered in his heart.

*We will. We’ll eat until we burst.*

And as he flew through the air, he saw the black-robed man’s wide eyes suddenly right in front of him.

Slice!

A flash carrying the last of his strength swept across the jiangshi sorcerer’s neck.

* * *

In a battle where thousands, tens of thousands, clash, one person’s death might mean nothing.

But the single head now tumbling through the air was enough to bring about a great change in the battle around the East Gate.

Thud. Clatter.

The head fell, then the ritual bell slipped from the dead body’s hand.

At the same time, the roughly three hundred monsters that had survived the horrifying melee and continued rampaging stopped moving.

“……!”

“……!”

A silence settled over the instant, stretched thinner and thinner.

Some opened their eyes wide. Some smiled faintly.

And someone else, who had made all of this possible, felt a shiver run down his spine as he silently looked at the head at his feet.

Or, more precisely, at the sharp cut across the jiangshi sorcerer’s neck.

At the trace of what people under heaven called Sword Energy.

*It wasn’t the sword…*

It had lasted only an instant.

Maybe it had been a hallucination, born while he was already out of his mind.

But it didn’t matter.

At last, he had done it with his own strength.

He had proved, at least a little, why he’d been able to defeat twenty monsters, and why he deserved to stand alongside companions who were far more than he could ever hope to deserve.

And just as a feeble smile formed on Hyuk Mujin’s lips—

BOOOOM!

A tremendous blast, like the sky splitting apart, shook heaven and earth. An immense surge of qi flung open the tightly shut gate.

Wooooooong.

The air trembled.

Through the faint darkness, a shadow wreathed in an aura as immense as Mount Taishan leaned toward Hyuk Mujin, standing alone before the gate.

“What is your name?”

At that moment, Hyuk Mujin understood.

This was where his life ended.

He wouldn’t be able to keep the promise he’d made to Jin Taekyung before the battle began.

“Fire Dragon Pavilion’s… no. Swift Wind Sword Hyuk Mujin.”

Hyuk Mujin answered.

Calmer and more composed than ever.

And with a quiet reply, he felt an immense force pierce into his chest.

“I’ll remember it.”

POOM!

Hyuk Mujin’s vision plunged into darkness.

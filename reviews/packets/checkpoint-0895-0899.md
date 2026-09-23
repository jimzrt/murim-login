# Checkpoint Review — 895–899

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

# Chapters 895–899

## Plot

Ma Sanbao explains how So Gyo helped the coup succeed and asks Jin Taekyung to join the restoration effort. Taekyung signs the pledge and arranges for Murim Alliance reinforcements to be summoned for the grand banquet. After the flood, the Emperor announces a three-day birthday banquet for the imperial prince, while a mysterious bamboo-hat man stirs public hopes around Prince Shangshan.

Taekyung reunites with Hyuk Mujin and sends the Fire Dragon Pavilion members to await the reinforcements, keeping himself and Jeok Cheongang behind. On the way to the banquet hall, Taekyung recognizes opium’s scent on Hong Jin’s pipe and wonders whether the Emperor smokes it. The Emperor prepares to leave Qianqing Palace; So Gyo, having stopped his agents from following the departed martial artists, waits on the roof with her weapons. At the banquet hall, Taekyung sees a vast golden procession approaching five hours late.

## Continuity

- Taekyung joined the restoration effort, signing the pledge in his name alone. He gave Ma Sanbao a cipher to summon Murim Alliance reinforcements for the banquet.
- So Gyo helped Baek Yeon defeat Cang Gong during the coup more than ten years ago. Her identity and connection to Dark Heaven remain unconfirmed.
- The Emperor announced a three-day birthday banquet for the imperial prince, beginning the day after the flood. Public anger is growing, and a mysterious bamboo-hat man’s reference to shelter at Shangshan led the crowd to imagine Prince Shangshan as a successor.
- Murim Alliance reinforcements were expected within half a day to a day. Hyuk Mujin is leading the Fire Dragon Pavilion members to await them; Taekyung and Jeok Cheongang stayed behind. Mujin is to check Taekyung’s note only after ensuring they are not followed.
- Taekyung suspects the Emperor smokes opium, having recognized its scent from his earlier audience at Qianqing Palace. The reason is unknown.
- The Emperor is preparing to leave Qianqing Palace for the banquet. So Gyo prevented his agents from pursuing the martial artists who left the palace and has reclaimed her weapons.
- The banquet is underway, and the Emperor’s five-hours-late golden procession is approaching the Grand Banquet Hall.

## Translation Decisions

- Render 黃道十二宮 as “Twelve Palaces of the Zodiac,” the title for the twelve Supreme Peak masters protecting the capital.
- Render 東廠掌印太監 as “Seal-Holding Eunuch of the East Depot.”
- Keep “Shangshan” in the crowd’s mountain imagery, where it alludes to Prince Shangshan.
- Retain “Tenfold Man” as Hyuk Mujin’s boastful title.
- Translate 앵속 as “poppy” in the explanation and use “opium” when Taekyung identifies the substance.

## Durable state

{
  "active_continuity": [
    "The imperial birthday banquet is underway; Taekyung and Hong Jin are being escorted to the Grand Banquet Hall by the Embroidered Uniform Guards.",
    "Taekyung suspects the Emperor smokes opium, having recognized its scent from his earlier audience at Qianqing Palace; the reason is unknown.",
    "The Emperor is preparing to leave Qianqing Palace for the banquet. Taekyung and his Master are present, while the other martial artists have left the palace.",
    "So Gyo stopped the Emperor’s agents from pursuing the departing martial artists and has reclaimed her weapons.",
    "A vast golden procession is approaching the Grand Banquet Hall five hours late."
  ],
  "continuity_sources": [
    898,
    899
  ],
  "open_questions": [
    "Why might the Emperor be smoking opium?",
    "What will happen when the Emperor’s procession reaches the banquet hall?",
    "What purpose do the departed martial artists have, and where are they going?"
  ],
  "safe_through": 899,
  "temporary_decisions": [
    "Translate 앵속 as “poppy” in the explanation and use “opium” when Taekyung identifies the substance."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 895

# Chapter 895

The pavilion’s interior was as dark as a cave.

Listening to the heavy rain outside the window, I quietly turned over the meaning of what I’d just heard.

And the image of the eunuch who’d led me here as if he’d been waiting for me from the start.

“You already knew?”

Ma Sanbao nodded.

“About two shichen ago, the assassins reported that you’d discovered their identities. They were concerned the situation might interfere with completing the job.”

You’d have to be remarkably oblivious not to realize that *concerned* was a considerable understatement.

Especially when the people involved were assassins.

“So the assassins you hired tried to kill me.”

“Not exactly, but you know what kind of people assassins are.”

“I’ve never dealt with them firsthand, but I have a general idea. And you brought people like that into this affair.”

“I had no choice. If you pay them a fair price, they become more loyal than anyone.”

“So what did you tell them to do about me?”

“…My friend.”

Ma Sanbao fixed me with a furrowed brow, then continued with a sigh.

“Don’t mistake me for a madman like the Son of Heaven. You came all this way, a thousand li, to help His Highness Prince Shangshan. They’re merely assassins carrying out a job they were promised payment for. Which of you is the more trustworthy ally?”

“Well…”

“Exactly. You are. Is that answer enough?”

Not yet.

I barely managed to keep the words from slipping out.

*Right. Not yet.*

Was it because of everything I’d experienced up to now?

Or because my mind had grown as cold as the rain outside?

Instinct told me it wouldn’t be a good idea to lay all my thoughts bare.

Instead, I nodded as if I understood and brought up the question I’d set aside for a moment.

“Then did you know about So Gyo, too?”

“No. I deliberately withheld information about the assassins because I knew how people like you in Murim would see them, but… she’s different.”

The shadow I thought I saw fall over Ma Sanbao’s face just then wasn’t only because of the darkness around us.

“We didn’t tell you about that woman who goes by So Gyo because we didn’t know much about her ourselves.”

“You didn’t know? The East Depot, of all people?”

The Embroidered Uniform Guard and the East Depot were enormous intelligence organizations with roots all across the land.

It was hard to understand how the East Depot could have failed to learn what was happening in the imperial palace, which was practically its own stronghold—even after its influence had shrunk in the wake of the coup.

“Tell me more.”

“All right. It may help you trust me, even a little.”

Ma Sanbao read the distrust in my eyes and continued with a bitter smile.

“It was more than ten years ago. That was when So Gyo—or rather, the unidentified master—first appeared.”

As the rain slowly began to ease, his voice filtered through it.

* * *

The story was over.

Ma Sanbao had spoken without pause for about fifteen minutes. He pulled the flask from his belt, and I looked at him, still bewildered.

“Why are you only telling me this important information now? If I’d known sooner…”

“I was afraid.”

Ma Sanbao had just raised the flask to his lips. He went on.

“It may sound like an excuse, but I couldn’t help it. I didn’t think the forces I’ve gathered so far would be able to handle her.”

The harsh aroma of liquor drifted from the flask’s mouth. Noticing my gaze, Ma Sanbao tossed it to me.

“Want a drink? You look like you could use one.”

I reached out reflexively and caught the flask.

After hesitating for a moment, I brought it to my lips.

After hearing a story that complicated, a drink was only natural.

I could drink straight from the jar and still hardly get drunk, so I took several long gulps.

The liquor’s burning strength went down my throat, its harsh aroma filling my mouth.

It was strong liquor, the cheap kind sold at any inn in the land.

“Maybe it’s because you’re from the north, but you certainly drink with gusto.”

I grimaced and swallowed the liquor still in my mouth.

“Surprising. I thought you’d drink something better.”

“What, you figured the East Depot’s Brush-Holding Eunuch wouldn’t drink cheap stuff like this?”

Ma Sanbao let out a small laugh and shook his head.

“No matter how high I’ve risen, strong liquor is what I am at my core. Like the cheap stuff you can find anywhere, I was once a man from the bottom of society. And like it, I don’t show people what I keep inside. If you want to survive for long in the imperial palace, you have to hide your true feelings like the harsh aroma of strong liquor. In that sense, I suppose I’m the same kind of person as So Gyo.”

So Gyo.

I quietly turned the name over in my mind, along with the unbelievable story I’d just heard.

“Is all of it true?”

“What do you think? Does it sound like a lie?”

“I want an answer.”

“If you want certainty, then yes. Every word is true—not a single lie. I stake my life on it.”

Ma Sanbao answered with a solemn expression, then suddenly turned toward the window.

Beyond it, the rain had grown much lighter. His eyes, fixed on the thinning rain, had sunk deep.

“I can say this with certainty: without So Gyo, that coup would never have succeeded. Cang Gong wouldn’t be bedridden as he is now, either.”

So Gyo had first appeared more than ten years ago, on the day the imperial palace was engulfed in flames of war.

“Hong Jin may not have known, since he stayed by the late Emperor’s side the whole time, but as I said, the East Depot did everything it could to stop the coup.”

If Ma Sanbao’s story was true, then Cang Gong, now fallen to illness, had been a remarkable man.

He had served the late Emperor even before Baek Yeon, and Ma Sanbao said his martial arts were on a level comparable to Baek Yeon’s, despite Baek being hailed as the strongest warrior in the imperial family.

“Lord Cang Gong was the first to sense something was wrong. He summoned the Imperial Guards from the outskirts of the capital and planned to drive back the rebels alongside the East Depot inside the palace.”

At the time, Ma Sanbao had also served under Cang Gong. He’d judged they had a good chance of winning if they could defeat the Embroidered Uniform Guard inside the palace and retake the late Emperor.

That was, until one person appeared.

“The life-and-death duel between Baek Yeon and Lord Cang Gong was evenly matched. If things had stayed that way, we could have put down the coup. The Embroidered Uniform Guard wouldn’t have been able to hold out once the Imperial Guards joined us. But…”

Ma Sanbao continued in a stiff voice.

“Things don’t always go the way you want.”

The battle turned sharply against them when an unidentified master, dressed all in black, appeared.

Baek Yeon and the figure in black.

Cang Gong couldn’t withstand the combined assault of the two Supreme Peak masters. He collapsed with severe Internal Injuries, and the balance of the battle fell apart.

“Our forces were no weaker than the Embroidered Uniform Guard. The only reason we lost was that figure in black… No, that unidentified master I should now call So Gyo.”

As if his throat had gone dry, Ma Sanbao tried to raise the flask I’d returned to him. But it slipped from his fingertips, which had started to tremble.

It hit the floor with a hollow thud and rolled.

The flask was still half full, and the liquor spilled out in a rush.

Ma Sanbao stared down at the puddle forming on the floor, his eyes heavy, then murmured as if to himself.

“Her skill that day was… chilling. I couldn’t do a thing in the face of that overwhelming aura.”

I suddenly remembered So Gyo’s energy, calm as a spring breeze from beginning to end. And the terrifying wave of power that surged from her in that brief instant.

“Surely she wasn’t even going all out.”

Was that what it felt like to stand before an insurmountable wall?

I’d met plenty of powerful people, but fewer than ten—enemy or ally—had ever made me feel that kind of pressure.

*And every one of them was one of the Three Saints, or a master who could stand as their equal.*

They had moved beyond the Supreme Peak realm that every martial artist dreamed of, stepping into an even higher, exalted realm.

Just as Jeok Cheongang had cast off the Heart Demon that had gnawed at him for so many years and at last reached the realm of Returned to Youth, So Gyo, too, was a master who could rightly be called *a match for ten thousand men*.

“So that’s why you chose me. No, me and my Master.”

“That’s right. Just as I told you before.”

Now that he’d revealed the whole truth, Ma Sanbao continued with a grave expression.

“Someone who would come a thousand li to help Prince Shangshan. Someone who’d put human decency ahead of any reward. And…”

“Another master who could face the unidentified expert at the Emperor’s side. The Fire King, Jeok Cheongang. Am I right?”

Ma Sanbao was silent for a moment, then nodded weakly.

“Exactly. That’s why I wrote your name in the secret letter I sent to Hong Jin. It wasn’t hard to guess that if you, Jeok Cheongang’s only Disciple, risked going to the imperial palace, your Master would come along.”

“Then you knew everything that happened in Nanman, too?”

“I’ve been keeping an eye on things for a while. Not on Nanman—on you.”

“Why didn’t you ask the Murim Alliance for help officially? That would have been much better.”

“I know quite a bit about the current Alliance Leader, Sword Saint Mae Jonghak. Cang Gong once called him one of the few true chivalrous heroes left in this age.”

“Then there was no reason to choose me or my Master.”

“The less a secret is exposed, the better, don’t you think? Especially when that secret is a coup.”

“Ah.”

I let out a low groan, and Ma Sanbao smiled bitterly.

“We may call ourselves a restoration army, but in the eyes of the world, aren’t we the traitors? And if our ties to Murim were revealed, things would never go well for us.”

Murim existed within the Great Nation’s borders, but it was also a society that openly defied the laws of the land.

So if the Murim Alliance intervened, it would be like bringing in a foreign force to this crucial struggle over the throne.

A pack of beasts that had slipped beyond the fence, with no leash on them.

“Of course, the current Alliance Leader was probably willing to help us. You can tell from the secret order he gave you to guard Prince Shangshan.”

“That’s true. We also have to keep a close eye on every move the imperial family makes.”

“But that’s about as far as he can go. If he formally asked them to join the restoration army, how many of the Alliance’s leaders would agree?”

“Well…”

My voice trailed off.

Coup.

Just thinking of the word sent a chill down my spine.

Maybe the Heavenly Demon, who’d supposedly ruled the Demonic Cult like a king, could make that kind of decision alone. But the Alliance Leader, elected through the support of others, couldn’t.

The Nine Sects and One Gang. The Five Great Families. And all the other sects under the Murim Alliance’s banner.

Getting support from most of them was practically impossible.

Right or wrong, a coup was a dangerous gamble that could ruin you in an instant.

“In that case, Blazing Flame Divine Dragon Jin Taekyung, I’ll ask you directly.”

The pounding rain had stopped as if by magic. Ma Sanbao’s eyes flashed in the darkness.

“Will you join forces with me—or rather, with us?”

His voice was full of conviction, cutting clearly through the silence.

“Will you help us restore order to this troubled land and put His Highness Prince Shangshan on the throne?”

“……!”

My body trembled before I could stop it.

A bolt of lightning struck through the tangled mess in my head.

After a brief silence that somehow felt longer than any other, I stared at Ma Sanbao and suddenly spoke.

“Do you still have that joint pledge you showed me last time?”

At the meaning behind my words, a bright smile spread across Ma Sanbao’s face.
## Chapter artifact 896

# Chapter 896

The pledge Ma Sanbao pulled from his robe was already quite worn, as if it had been keeping track of all the years that had passed.

The paper had yellowed, and stains had spread in places.

But the names and titles, written densely in each person’s own hand, remained clear. At the center was one person’s name, written in the largest, boldest script of all.

Wei Zhong, Seal-Holding Eunuch of the East Depot.

“Lord Cang Gong.”

Ma Sanbao noticed where I was looking and spoke without warning.

“He was the first to draw up and sign the pledge. He made me promise over and over that even if he passed away, we had to see the coup through.”

“His condition must have been serious enough for him to consider his own death.”

“His Internal Injury was bad enough that it wouldn’t have been surprising if he’d died right then and there. Thankfully, he survived…”

Ma Sanbao sighed, his face full of regret.

“But it’s not good. He still hasn’t recovered completely. Of course, if he hadn’t been injured that badly, he wouldn’t still be alive.”

“What do you mean?”

“Why do you think the Emperor let Lord Cang Gong live? He was the foremost among the late Emperor’s old retainers. The fallout from executing him outright would have been too much to bear.”

It was something I’d wondered about, too.

That meticulous Emperor had spared Lord Cang Gong, the man who stood in his way—and the head of the East Depot, the most threatening force of all.

“Is there something else I don’t know?”

At my question, Ma Sanbao quietly nodded.

“There was. A bargain that put the fate of the Great Nation on the line.”

“What kind of bargain?”

“The life of a child who hadn’t even learned to walk yet. And the lives of countless loyal officials in exchange.”

“……!”

“Yes. Just as you’re thinking. Nearly a hundred high-ranking officials were sacrificed to save His Highness Prince Shangshan. Not just them—their entire families.”

The air around us grew heavy. Flames flickered in Ma Sanbao’s eyes.

“With the late Emperor, His Highness the Crown Prince, and the other princes all seriously ill, we had to protect His Highness Prince Shangshan, our last hope, even at that cost. It was the only way.”

“Then what did the Emperor get in return?”

“Legitimacy and time. The late Emperor, after securing a promise about His Highness Prince Shangshan’s future, formally abdicated the throne. Lord Cang Gong calmed the opposition forces that had wanted to fight the new Emperor.”

The capital might be the heart of the realm, but the capital was not the realm itself.

The Great Nation’s vast territory depended on its many officials and armies.

The new Emperor had gained at least some legitimacy by receiving the throne through a formal abdication from the late Emperor. But he would have needed time to quell the rebellions simmering across the land.

Lord Cang Gong, the most respected and authoritative of the late Emperor’s old retainers, and Prince Shangshan’s safety must have been the restraints that kept them in check.

“We suffered a devastating blow, but the bargain still let us achieve at least our bare minimum. The Emperor wasn’t the only one who needed time to recover.”

The Emperor had probably expected Lord Cang Gong to die before long.

But despite his terrible Internal Injury, Lord Cang Gong had miraculously survived, and the East Depot he led had endured to this day.

So had the restoration army, which dreamed of rebellion under Lord Cang Gong’s leadership.

“So the two sides split apart and faced off against each other. And they’ve been doing that for more than a decade.”

“That’s right. This clash was inevitable from a long time ago. We kept our blades pointed at each other, but neither side could bring itself to act. At least, not openly.”

I frowned at the words Ma Sanbao added.

“Not openly?”

“There have been several assassination attempts. The Emperor went after Lord Cang Gong, and we went after the Emperor.”

The outcome was obvious without asking.

The Emperor and Lord Cang Gong were both still alive.

But unlike the Emperor, who lived in Qianqing Palace under strict guard, Lord Cang Gong had survived attempts on his life. That was quite a surprise.

“When I went to Qianqing Palace, I saw that the Emperor had one hell of an assassin working for him. How did you stop them?”

“Of course, the Emperor has several Supreme Peak masters under his command. But our side is no weaker. Have you ever heard of the Twelve Palaces of the Zodiac?”

“I’ve heard the name a few times, but aren’t those constellations?”

“Usually, yes. But it’s also the title given to the twelve Supreme Peak masters who protect the capital.”

What?

I couldn’t hide my surprise. My eyes widened.

There were twelve Supreme Peak masters in the capital—people rare even in Murim.

Even knowing that much of the Great Nation’s strength was concentrated in the capital, it was astonishing. And what Ma Sanbao said next was even more unexpected.

“Half of those twelve Supreme Peak masters belong to our side. Some of them are staying with Lord Cang Gong.”

“……!”

“And that’s not all.”

Ma Sanbao continued, pointing to the titles and names written on the pledge one by one.

Among them were old scholars who enjoyed the overwhelming support of the realm’s Confucian scholars, and senior court officials of the highest rank, such as the Three Dukes. But the most important figures were others.

The military officers—that was who mattered most.

Commanders guarding either the capital or the borders beyond it.

One of them was even a governor-general with tens of thousands of troops under his command.

“Do you understand now why this standoff has lasted so long?”

I nodded heavily.

The names on this pledge were enough to make up half the Great Nation. If either side struck first under these circumstances, the land would become a sea of corpses and blood.

“The Emperor was the one who drew his sword first. We had no intention of breaking this balance. At least, we wanted to wait until His Highness Prince Shangshan had grown older.”

Compared with children in the modern world, children of this era generally matured much faster.

But the cold reality was that Prince Shangshan was still too young to take on the burden of this vast empire.

“Even His Highness the Crown Prince, who was so intelligent, and the two princes, who were every bit as fit to be members of the imperial family, along with other members of the imperial family, all wasted away and died. Just like someone you know.”

“……The City Lord of Sichuan Province.”

“That’s right. He supposedly fell ill like that right after meeting the Emperor. Do you really think that was a coincidence?”

Ma Sanbao continued in a voice that was both grave and certain.

“The Emperor must have joined hands with that treacherous group called Dark Heaven. Baek Yeon, who suddenly betrayed the late Emperor, and that woman So Gyo must also be closely connected to Dark Heaven.”

“……!”

“You and I have come too far to turn back now. It’s time to put an end to this long and terrible turmoil. The grand banquet that’s coming…”

Ma Sanbao’s eyes shone brightly.

“Will be the grand enthronement ceremony of a new Son of Heaven—the rightful one.”

Without realizing it, I closed my eyes.

Dark.

The rain that had poured down in a single furious burst had stopped. I could no longer hear it.

A suffocating silence.

In that quiet, I looked inward. I examined my thoughts and questions once more, searching them deeply.

What was right? What was wrong?

What waited at the end of this choice?

The die had already been cast.

From the moment I’d asked Ma Sanbao for the pledge, I’d already made my decision. This choice was only the last fork in the road before I reached my destination.

Rustle.

I opened my eyes. Ma Sanbao’s face was tense.

After staring at him in silence for a while, I brought my hand to my mouth.

Crack. Tap.

A dull pain, and drops of blood began to fall. With my pinky finger wet with blood, I filled in the pledge’s empty space.

Jin Taekyung.

Just those three syllables.

That was all.

Unlike everyone else whose names and details filled the pledge, I wrote no sobriquet, family, or affiliation.

Ma Sanbao immediately understood what my action meant.

“You intend to bear it all alone. In case the coup fails.”

“Does that make me a coward?”

“No. I can’t blame you. You don’t want to suffer the same fate as the Maoshan Sect, annihilated for opposing the Great Nation in the past. Besides…”

Ma Sanbao tucked the pledge, now bearing my name, into his robe and continued.

“If you and your Master join our side, the coup won’t fail.”

His expression and tone were full of conviction.

I looked at him for a moment, then spoke without warning.

“That’s not enough.”

“What?”

“It shouldn’t be ‘it won’t fail.’ It should be ‘it has to succeed,’ shouldn’t it?”

“What are you—”

Before Ma Sanbao could finish, I walked over to the bookcase in the corner of the pavilion and pulled out a book.

Without hesitating, I tore off one of its pages. Then, with a finger that was still bleeding, I scrawled a short message and handed it to Ma Sanbao.

“What is this…?”

Ma Sanbao frowned as he read what I’d written.

“I have no idea what this means. I can’t even read it properly.”

“That’s to be expected. It’s a secret code.”

“A secret code?”

“Yes. A cipher only a tiny handful of people can decipher.”

“Then why are you—wait. You can’t mean…”

“I do.”

I nodded at Ma Sanbao, whose eyes had widened, and continued slowly.

“Send one of your men to the place I’m about to give you, and have them deliver that message. Then, on the day of the grand banquet, reinforcements from the Murim Alliance will arrive. It may even be a powerful force that includes the Slaughter Saint or one of the Ten Kings.”

“……!”

“You said it yourself last time. If we succeed, we’re kings. If we fail, we’re traitors.”

I met Ma Sanbao’s face, colored with shock and amazement, and muttered,

“In that case, shouldn’t we make sure this coup succeeds?”

Right.

The die had already been cast.

* * *

It was a downpour the likes of which had rarely been seen.

The rain that fell overnight flooded parts of the capital. Hundreds of homes were submerged, and many people were killed or injured.

As it happened, ominous rumors began to spread.

They said they’d found a venomous serpent in a well on the outskirts of the capital—one bigger than several grown men put together.

They said it was Heaven’s warning to the current Son of Heaven, who had defied the natural order—and a prophecy that an even greater disaster was about to begin.

They said the rain had stopped so soon thanks to His Highness Prince Shangshan, who had inherited the late Emperor’s will.

All sorts of ill omens, mixed with superstition, spread like wildfire. By the time just two days had passed, they’d crossed the towering city walls and reached the imperial palace.

Even the deepest, most secret part of it: Qianqing Palace.

When the Emperor heard the rumors, he gave an impatient laugh.

“Looks like the time has come.”

It was the first sign of a storm.

And the beginning of the grand banquet—with its wind, rain, and sea of corpses and blood.
## Chapter artifact 897

# Chapter 897

That day, everything was different from usual.

The streets, where laughter and music never seemed to stop, were quiet. The clouds that had yet to clear cast shadows over everyone’s heads, and the canals, swollen by unprecedented rainfall, churned uneasily as if reflecting the state of things.

At the end of it all, and at its center, stood the imperial palace.

Rumble.

It was the dim hour before dawn. Even as the massive iron gates swung open with a heavy metallic groan, no one noticed anything strange.

The imperial palace gates always closed at the hour of the Rat and opened at the hour of the Rabbit.

Before long, dawn would break. Ministers from the various courts would make their way to the palace, while the people of this beautiful, dangerous metropolis—high and low alike—began another day in their own places.

Like precisely meshing gears.

As if things had been set in motion that way from the start.

But the dazzling light that appeared through the slowly opening gates was proof that this day was not beginning as usual.

“H-Hey. Is that…?”

“Hm?”

A vendor who had set up his stall along the main road in front of the palace, as usual, turned at the call of a fellow merchant. His narrow eyes swelled wide.

“T-The Embroidered Uniform Guard?”

The moment those words slipped between his reflexively parted lips—

“Ha!”

With a short battle cry shouted in unison, a thousand Embroidered Uniform Guards mounted on their fine steeds poured through the wide-open gates.

Thud-thud-thud-thud!

Hooves thundered, waking the dawn.

The ground shook. Dust, settled by the cool morning air and rainwater that had yet to dry, rose into the air.

The thousand riders shot forward like a single arrow, racing across the main road in front of the palace in the blink of an eye. At a hand signal from the commander at the head of the formation, they scattered in every direction.

From a thousand to hundreds. Hundreds to a hundred. A hundred to dozens.

They split up, then split up again, exactly as planned.

The people who had started their day early watched this sudden turn of events in a daze. But when they saw the notices left behind by the golden tide that had swept across the entire capital, they understood why.



Tomorrow. The hour of the Goat.

The grand banquet for the imperial prince’s birthday. Begins.



That was how the first line of the hundreds of proclamations began, each written by the imperial court calligrapher whose elegant handwriting was renowned throughout the realm. The faces of the people already suffering from the untimely flood twisted with anger.

“Three days? He’s holding that damn banquet for three whole days in a situation like this?”

“Shh. Keep your voice down. Want to get arrested for treason?”

“Treason, my ass. We’ve worked like oxen our whole lives to buy a house, and now we’ve lost that and every last one of our belongings. What’s there to be afraid of?”

“Right!”

“Fuck, is it to hell with what the people think? His own kid’s birthday comes first, is that it?”

Some had lost their property. Others, their families.

And they were all neighbors who had been closer than family.

So the people trying to calm those furious at the proclamation didn’t look happy, either.

The Son of Heaven. Or the Emperor.

How could the supreme ruler, descended from the dragon appointed by Heaven and charged with caring for all his subjects, do such a thing?

Those who had lost what they treasured in the flood were furious. And the people watching them suddenly realized that they too might one day be standing there, furious over their own losses.

*This country… something’s gone wrong.*

At first, they had done nothing but look up to him. To them, the Son of Heaven was someone so exalted they couldn’t even imagine seeing him in a dream, no different from the sun shining high above the sky.

But the current Emperor was a man who had defied the natural order.

A heartless monster who’d seized the throne after wiping out his parents, his siblings, and countless loyal officials and their families.

And so Heaven’s favor must have turned away from him.

At the Shaolin Temple, known to everyone under Heaven, eminent monks had been dying. In Sichuan, thousands of martial artists had turned the broad daylight into a sea of corpses and blood.

And that wasn’t all.

Unbelievable rumors had reached them from Hubei of an imugi gone on a rampage. There were also sinister tales of the barbarians who lived in the harsh lands of Nanman forming a massive army and marching north.

On top of that, the northern tribes, which had lain low and silent for the past hundred years, were showing signs of unrest. And now unprecedented rainfall had struck the capital.

What could this string of disasters mean?

*Heaven has forsaken this country. No—the heavens are trying to punish the Emperor.*

If these had been peaceful, prosperous times, no one would have paid attention to rumors and superstitions like these.

If they had houses earned through hard work, beloved families, and ample grain and wealth, that alone would have been enough.

For more than a decade, the realm had been as calm as the waters of West Lake, and the people hadn’t voiced much displeasure with their new Son of Heaven—not as much as one might have expected.

They could condemn the Son of Heaven for defying the natural order, but their lives and livelihoods hadn’t changed all that much.

No—in fact, some had cheered when corrupt officials who’d run rampant during the late Emperor’s peaceful reign were caught up in the treason case and purged. Good riddance, they’d said.

But that was no longer the case.

In barely two years, strange events that could only be called supernatural powers had taken place all over the realm. A young prince beloved by the people had been summoned to the capital, and the Son of Heaven, turning his back on his suffering subjects, had spent a fortune to hold a banquet celebrating his offspring.

“Is this truly… is this really the right thing to do?”

The mutter of a man in a worn bamboo hat pulled low over his face spoke for everyone.

“Public sentiment is Heaven’s will, and Heaven’s will is public sentiment. So why has His Majesty turned his back on Heaven and his people?”

His voice rang clearly among the crowd, which had fallen quiet.

The invisible air pressed down on them, heavy and still.

In the suffocating silence, people clenched their teeth and their eyes shone. For some reason, they strained to hear every word of the man’s voice, which sounded unusually clear.

“The azure heaven’s power is waning, and dark clouds gather. The storm that will soon descend will soon swallow the realm whole.”

It was strange.

Though hundreds of people had gathered in one place, not a single one spoke. They all listened to the man.

The rough laborer who had spent his entire life unable to read. The street vendor who lived day to day. Even the elderly Confucian scholar, whose learning was likely as extensive as the years he’d lived.

The man’s words and voice held an inexplicable, profound insight and conviction. They were more than enough to draw everyone in.

Along with a question they couldn’t help asking.

“Um, sir. Forgive me for interrupting, but may this lowly man ask you something?”

At the laborer’s cautious approach, rough as he looked, the man in the bamboo hat nodded.

“Go ahead.”

“If it’s not too much trouble, what should a poor man like me do to escape the storm you mentioned?”

“Go to the mountain.”

“What?”

The laborer’s eyes widened at the answer, given without a hint of hesitation. The man in the bamboo hat went on slowly.

“Find the highest mountain in the realm and seek shelter there. It has a stream that never runs dry, luscious fruit and wild animals, and a forest that can provide houses and firewood. It is more than large enough to shelter all the people under Heaven.”

The laborer, who’d asked the first question, was dumbfounded.

As was most of the crowd gathered there.

The highest mountain in the realm?

Where in the world was there a mountain so vast it could shelter everyone, with an abundance of food and resources?

While the laborer searched for words, another man, more impatient, blurted out,

“I don’t know who you are, but you seem like a master who’s cultivated deeply. Do you mean the Five Sacred Mountains of the Central Plains?”

A few people nodded with a soft “Ah.”

The five famous mountains said to be the highest in the realm and filled with sacred energy—if he meant those, then it would make sense, they murmured.

“Which one of the Five Sacred Mountains do you mean? Mount Song in Henan? Taishan in Shandong? Huashan in Shaanxi? Or perhaps…”

“You’re all wrong. I didn’t mean the Five Sacred Mountains of the Central Plains.”

“What? What do you mean? If not the Five Sacred Mountains, then what—”

The man’s answer was calm but firm, and the crowd was left speechless. Just then, an elderly voice suddenly spoke from somewhere.

“There’s one place left. No, from the very beginning, it was the only place.”

Everyone’s gaze swung in the same direction.

An elderly Confucian scholar in faded but neat clothes gazed at the gloomy sky and murmured, almost to himself,

“Shangshan.”

“……!”

A few people understood what those words meant, and their eyes widened. Most remained confused.

At least, until the old scholar continued.

“Yes. That place could shelter all the people under Heaven. No matter how fiercely the storm swallowed the Five Sacred Mountains of the Central Plains, it would never dare reach Shangshan. The mountain’s master is under Heaven’s protection, a descendant of the dragon who commands rain and lightning.”

For a moment, it was as if the world had stopped.

Everyone there stood frozen like statues, looking at one another. Then, together, they realized they’d all reached the same conclusion.

Shangshan.

Higher and wider than the Five Sacred Mountains of the Central Plains, a mountain capable of sheltering all the people under Heaven.

And the dragon’s blood under Heaven’s protection. The master of Shangshan.

Why hadn’t they realized it? How could they have been so foolish?

The man hadn’t been talking about the mountain itself from the beginning. Every word he’d said pointed to one person who could shelter this chaotic realm.

*Prince Shangshan…!*

Was this what it felt like to be struck right through the crown of your head by a bolt of lightning?

Everyone’s whole body trembled as if they’d been electrocuted.

Mouths agape. Teeth clenched. Fists balled, as they fought to cool their heads, burning hot with excitement.

And yet, at the same time, they imagined a future they’d never dared picture before.

*What if… what if His Highness Prince Shangshan ascended the throne?*

Heaven’s favor had already turned away, and the people’s hearts were wavering.

And the child who’d survived that vast, brutal purge in the past had returned to the capital, to the very place where he’d let out his first cry.

Was this fate, or coincidence? Or was it another sinister plot by an Emperor who had already defied the natural order once?

Or perhaps…

Was it the Mandate of Heaven?

Daring not even to speak, the people slowly turned their heads.

They wanted an answer to that question.

They wanted to face the man who’d dropped this enormous shock on them.

But the next moment, all their anticipation and excitement came crashing down.

The place where the man in the bamboo hat had stood just moments ago was empty.
## Chapter artifact 898

# Chapter 898

Someone once said humans are creatures of adaptation.

But there’s always at least one thing in the world that no one can get used to, no matter how many times they experience it.

For me, one such thing was being responsible for other people’s lives. Another was waking up to someone’s ugly face.

“What are you doing?”

Hyuk Mujin answered, “I was checking on you, Captain.”

“Why?”

“You barred everyone from coming in and spent two whole days shut up in your room circulating your qi. I thought you might’ve suffered qi deviation, so I slipped in to check.”

“Two days?”

“Yes. You didn’t know?”

“No, I knew.”

That was a lie. I’d thought half a day had passed at most. I couldn’t believe it had been two whole days.

I looked toward the window, where sunlight streamed in, then sighed inwardly.

“I appreciate you worrying about me, but next time, just leave me alone.”

“Why?”

“Because seeing your face first thing when I woke up nearly gave me qi deviation.”

“Isn’t that a bit harsh?”

“Your face is harsh.”

“Then I’ll just stay nearby. You need someone to stand guard, don’t you?”

“Don’t stand guard, either.”

“Why not?”

“Your snoring will give me qi deviation.”

“……At this point, it’d be better if I just disappeared. Keep this up and I might get fed up and head back to the Jin Family on my own.”

I had just uncrossed my legs and was about to get up when I stared at Hyuk Mujin, who was putting on a show of threatening me.

“W-Why are you looking at me like that? Is there some rule that says I have to follow you around, Captain?”

He was talking tough, but his eyes kept darting nervously. A laugh escaped me.

Hyuk Mujin had been shrinking into himself, either to dodge the punch he never knew when I might throw, or to make sure it hurt as little as possible. Now he looked confused.

“What’s going on? Am I seeing things? Why are you acting like this all of a sudden, Captain?”

“Like what?”

“I mean, you’d normally have hit me at least twelve times by now, but you’re just smiling like some virtuous gentleman.”

I barely held back the laugh bubbling up inside me.

Then, in the next instant, I kicked off the floor and shot forward at lightning speed.

Whoosh!

Hyuk Mujin instinctively tried to defend himself. The movement he showed in that split second was so quick and composed, it was hard to believe he was still only a First Rate martial artist.

Of course, the fact that he was facing me meant his response had already failed.

“Hup.”

Realizing everything had gone wrong, Hyuk Mujin let out a strangled breath and squeezed his eyes shut. He was probably bracing for the usual bone-rattling blow.

But despite all that mental preparation, what he expected never happened.

Tap.

Instead of smacking him like I usually did, I lightly tapped the back of his head and clicked my tongue.

“You’ve been learning martial arts wrong all this time. Who told you to close your eyes?”

“……Huh?”

“Even if you’re getting hit, keep your eyes wide open. Even just keeping your eyes on your opponent puts you halfway there.”

Hyuk Mujin rubbed the back of his head, looking dazed, then blurted out, “Why are you acting like this all of a sudden?”

“Like what?”

“Isn’t it strange? Normally…”

“So, you want me to hit you like I usually do?”

Hyuk Mujin answered at once. “No. Not really.”

“Then shut up. I’m saving your strength.”

“Saving my strength?”

“Yeah. We’re going to be fighting like hell soon. Why would I hit you on the back of the head? If you get hit by some stray blade after that, I’ll have nightmares for nothing.”

Hyuk Mujin grinned.

“Ohhh. So that’s what it is. You could be a little more honest, you know.”

“What?”

“I know all about it. When I said I might leave, it bothered you, didn’t it, Captain? Right?”

I was about to say something, but all that came out was a quiet laugh.

“Yeah, you little shit. Must be nice to be so perceptive.”

“I knew it. I thought so. Even you need someone like me, your right-hand man, stuck to your side if you want to get anything done.”

“Right-hand man, my ass. You’re a little toe.”

“Now, why would you say that? Calling me your right-hand man is already a pretty big concession on my part.”

“A concession?”

“Yes. Where else are you going to find a subordinate as loyal as me? At this point, I’m not your right hand—I’m your heart. Your heart.”

“Not a chance. You’ve got balls, for crying out loud. How dare you?”

“Then if I get them removed, do I qualify?”

Whack!

This time I put a bit of force into it, but for some reason, Hyuk Mujin clutched the back of his head with a groan, looking happier than ever.

“Now that’s more like it.”

“……Huh?”

“It’s still a little weak, though. Hit me harder.”

What was with that creepy reaction?

As I began to question Hyuk Mujin’s tastes, he grinned and went on.

“It’s just… nothing special. You’ve been acting so different from usual that it was bothering me.”

“……!”

“I know you’ve had a lot on your mind lately, but it’ll all work out. So just keep doing what you’ve always done. Same as always.”

For a moment, I couldn’t speak.

At the same time, the truth I’d kept buried in my heart welled up and tickled the back of my throat.

But…

*I can’t.*

I couldn’t let myself speak while swept up in a passing emotion. To survive and win in this enormous gamble, crawling with monsters, I had to keep my words to myself.

In the end, after thinking it over, I managed to say only one thing.

“Aren’t you scared?”

“Hm? Scared of what?”

“This situation we’re in. And the unknown situation we’re about to face.”

Hyuk Mujin blinked for a long while after hearing me, then answered, “What kind of question is that? Of course I’m scared.”

“Your words and actions don’t seem to match.”

“I’m used to being scared.”

“You’re used to it?”

“Yes. How do I put it? I’ve always been kind of a coward.”

Hyuk Mujin scratched the back of his head, looking embarrassed.

“When I was little, I was afraid my parents’ love would go to my younger sibling, so I cried every day. Then, when I got a bit older and decided to become a martial artist, I’d tremble just from holding a sword. I thought I’d gotten better after joining the Jin Family of Taiyuan, but after I started going around with you, Captain… I really thought I’d piss myself every single day.”

That was the first I’d heard of it.

Thinking back, I’d never really asked Hyuk Mujin much about his past.

I’d only found out by chance that he was the eldest son of a huge textile shop that had been in his family for three generations. It wasn’t as if I’d gone out of my way to learn about him.

Maybe that was why.

Normally, I would’ve cut off this long-winded story with a flick to his forehead. But today, for some reason, I wanted to hear more.

“……Anyway, I wound up stuck to your side somehow.”

Hyuk Mujin finished with a shrug, then suddenly looked at me.

“This is all your fault, Captain.”

“Mine?”

“Yes. You’re like a ghost, always heading straight for places where people die. I got so much practice along the way that now, even when I’m scared, I don’t feel scared anymore. You know what I mean?”

“Then, was it hard for you?”

“It wasn’t hard. I thought I was going to die. But I never actually did. Or, to be more precise, whenever I thought I was going to die, you saved me.”

*Maybe not this time.*

I swallowed the words that had been circling in my mouth.

Unaware of what I was thinking, Hyuk Mujin continued speaking as if nothing were wrong.

“Maybe that’s why I’m not all that scared this time, either. Even when I heard what you told Comrade Hong and me recently, I felt pretty calm.”

“Because you figure I’ll save you again this time?”

“No.”

“No?”

“No. I just had a thought.”

For a moment, Hyuk Mujin looked straight at me and spoke.

“Oh, I thought, maybe this time I can be the one to save you, Captain.”

“……!”

“You said it was dangerous. That you and Great Hero Jeok might have to risk your lives. That it was basically a gamble. Then this time, couldn’t even a low-level fighter like me be useful?”

Hyuk Mujin added with a bright smile, “I may be a First Rate nobody, still a long way from good, but they say in a tough spot, even a cat’s paw will do. Right?”

I didn’t answer.

No, I couldn’t.

It felt as if an invisible hand had closed around my throat, cutting off my breath.

I was afraid that if I opened my mouth, I might accidentally let the truth slip out. I couldn’t manage any answer at all.

So I silently looked at his bright smile, then simply smiled back.

“Yeah. Now you’re finally going to be useful.”

“Ahem. This time, just trust me. I, Hyuk Mujin, am your right hand and your heart. I’m the Tenfold Man of the Jin Family of Taiyuan, aren’t I?”

Watching Hyuk Mujin thump his chest with exaggerated force, I let go of every worry still weighing on my mind.

And I was certain.

Every choice I made from here on out would be the right one.

“Do you remember what I told you two days ago?”

Hyuk Mujin’s smile faded as he nodded.

“Which part do you mean…?”

“The Murim Alliance reinforcements.”

“Oh, of course I remember. But when did you manage to get in touch with the Murim Alliance, Captain?”

“That’s not important, so forget it. I have a mission for you.”

“Just me?”

“No, the entire Fire Dragon Pavilion.”

“The entire pavilion means… you’re coming with us, Captain?”

“I’m not going. And neither is my Master. You’ll lead the rest of the group to the place I tell you and wait there.”

“Are we meeting the Murim Alliance reinforcements there?”

“Yeah. They’ll arrive within half a day at the earliest, and by tomorrow at the latest.”

Hyuk Mujin nodded as if he understood, then suddenly furrowed his brow.

“But that’s longer than I expected. Being away at a time like this is a bit… And you’re not in your usual condition, either.”

“I’m not. So, are you worried that a Supreme Peak master who isn’t in his usual condition might keel over, coughing blood, at any moment?”

Hyuk Mujin grinned.

“Right, I was a crow-tit worrying about a Heavenly Eagle.”

“Usually, it’d be a stork you were worried about, not a Heavenly Eagle.”

“With the Blazing Flame Divine Dragon, even a Heavenly Eagle isn’t good enough. Anyway, is that the only mission you’re giving me?”

“Yeah. Right now.”

I answered and took a neatly folded note from inside my robe, then handed it to him.

I’d prepared it two days ago, but until the last moment, I’d wavered over whether to take it out at all.

“People other than me and my Master should be able to leave the imperial palace without any particular restrictions. Once you’re sure no one’s following you, check the destination written there.”

“This is starting to feel less like the Fire Dragon Pavilion and more like the Hidden Shadow Pavilion.”

Hyuk Mujin carefully took the paper and tucked it away. Then he clasped his hands in a salute.

“I’ll get going, then.”

“One last thing.”

“Yes?”

“Be careful. You and everyone else.”

Hyuk Mujin, who’d been looking at me in confusion, gave a playful grin. Then he turned and disappeared.

When his presence had faded completely, I slowly left the room and came face to face with the one person still there.

Whoosh.

A slow exhalation. Hong Jin looked at me through the cloudy smoke of his long-stemmed tobacco pipe, then murmured as if to himself,

“Martial artist Hyuk seemed pretty busy.”

“He is. I gave him a mission.”

“It must be an important one, if you sent him off at a time like this.”

“Yes. It is.”

“I understand how you feel.”

Creak.

The old wooden chair let out a groan. Hong Jin rose with elegant poise and spoke through the faint haze of smoke.

“In a dangerous gamble where no one knows what will happen, you must want to save even one more person.”

“……!”

“So, Young Master Jin, are you ready?”

I nodded with a bitter smile.

“I’ve always been ready.”

A little while later, golden-armored guards lined up in front of the pavilion to escort us to the Grand Banquet Hall.
## Chapter artifact 899

# Chapter 899

Maybe it was because everything around me was gleaming gold, but for a moment I felt like the richest man in the world.

Sadly, reality was a long way from that.

Clank. Clank.

I might’ve been able to immerse myself a little more if not for those ominous metallic sounds.

But the Embroidered Uniform Guards surrounding Hong Jin and me as they marched along showed no sign of offering that kind of consideration.

*To be fair, it’d be crazy to expect consideration from them.*

A laugh slipped out before I could stop it. I felt a heated gaze from beside me. Hong Jin was staring at me, looking baffled.

“What is it?”

“……I’m only asking just in case, but you do know why I’m looking at you, right?”

“Hmm. Because I suddenly laughed in a situation like this?”

“Thank goodness. I thought Young Master Jin had completely lost his mind.”

“Don’t worry. I’m holding on to my sanity.”

It wasn’t as if I could just stand there grinning like a lunatic with my life hanging by a thread.

When you’re backed up against a cliff, your mind actually grows calmer.

Everything gets wiped away, leaving only one word behind: survival.

Just like right now.

“I’ll take your word for it. I have no choice.”

Hong Jin muttered as if to himself, then slowly drew on his still-lit long-stemmed tobacco pipe.

Whoosh. A stream of white smoke billowed out with the glowing ember and drifted among the guards.

Smoking so boldly inside the imperial palace, with his head possibly about to roll any moment now. I was privately impressed by Hong Jin’s nerve when I caught sight of his eyelashes trembling and his face growing languid.

Even the distinctive fragrance of the smoke reached my nose.

*Now that I think about it, I always smell that whenever I’m near Hong Jin.*

Normally, I’d thought nothing of it.

I wasn’t some anti-smoking spokesperson. There was nothing strange about Hong Jin puffing on a pipe, and no reason for me to stop him.

I’d simply assumed he was filling up on nicotine since he was missing something a man ought to have.

But even so, I’d occasionally felt a strange sense of déjà vu.

There was something familiar about it, and I had no trouble remembering when I’d felt that way before.

*Right. Immediately after I returned from my audience with the Emperor. That very day.*

At the same time, an idea flashed through my mind.

I gazed at Hong Jin as he slowly exhaled smoke, then spoke up.

“It seems to taste better than I expected. It didn’t smell like much when I caught a whiff.”

“What are you talking about? Oh, this?”

When I gave a quiet nod, Hong Jin lightly waved the pipe in his hand.

“I wouldn’t say it tastes good. It’s just… a kind of habit. A very bad one, too.”

Of course smoking was bad for your health.

At least by modern standards.

*But in this era, it wasn’t exactly frowned upon.*

This world had no place in any history that made it down to the twenty-first century, but it was remarkably similar in many ways. The names of its regions, the clothes and food, and even people’s attitudes.

And in that sense, smoking wasn’t something you’d call a bad habit. If anything, it was encouraged by the claims of the powerful, who indulged in all manner of pleasures. Tobacco leaves were expensive, though, so it was a luxury most commoners could hardly afford.

*But Hong Jin, one of those powerful people himself, calls it a bad habit?*

That set off alarm bells.

There was something to it. Something I hadn’t figured out yet.

I held out my hand to Hong Jin.

“Can I try it?”

“Hmm? You want to smoke? This?”

“Yes. I thought I’d give it a try while I had the chance.”

In the brief moment our eyes met after I answered, Hong Jin’s eyebrow twitched so slightly that no one else could have noticed.

It was also a sign that he’d understood exactly what I meant.

“How curious. The martial artists I know drink readily enough, but they rarely touch poppy.”

“Poppy…?”

“It’s the dried sap of the poppy. If you smoke it when your mind is troubled, sometimes it calms you down and makes you feel drowsy. It’s often used to relieve pain, but it’s highly addictive, so—”

Hong Jin’s words drifted away, like an echo.

Only one word was floating through my mind.

*Opium!*

I might’ve treated school lessons as extra time to catch up on sleep, but at least a little basic knowledge had managed to stick.

Especially since my world history teacher had a booming voice so passionate it could chase away the sleep that had already claimed me.

*“Hey! Jin Taekyung!”*

*“Hrk. Huh?”*

*“You punk. What did the teacher just say? Don’t roll your eyes around—tell me.”*

*“Uh, well…”*

*“Right. You don’t know. Of course you don’t. You’ve been sleeping through three whole periods back there, so at this point, I can’t tell if this is a hotel or a school…”*

*“Oh, I remember now.”*

*“What? You remember? Fine, let’s hear what kind of creative bullshit you picked up in your dream. What is it?”*

*“Hey, Jin Taekyung.”*

*“……”*

*“No…?”*

*“No, you’re right. You are. But… Jesus, you’re a real nutcase. The Opium War! We were talking about the Opium War. You’ve got to be kidding me. Repeat after me. The Opium War!”*

*“What? The Youth Protection War?[^1]”*

*“Youth Protection… Hey, class president! Kim Minjeong!”*

*“Yes?”*

*“Call the cops right now. I’m going to beat this punk and get arrested for assaulting a student.”*

[^1]: Taekyung mishears *apyeon* (opium) as *acheong*, shorthand associated with Korea’s law protecting children and youth from sexual crimes.

Fortunately, it never came to the police getting called. Right after I got an earful of my teacher’s furious shouting, I was sentenced to write out a whole section on the Opium War by hand.

As a result, I managed to cram all sorts of trivial details into my thick skull—including the fact that the white-skinned island chinks invaded the genuine mainland chinks.

For instance, that opium came from a plant called the poppy.

*So that’s useful now.*

I silently thanked my world history teacher, who’d been more passionate than anyone.

Thanks to him, I’d just learned something new.

*Opium. No, that distinctive scent of poppy… I’ve smelled it before. Stronger than Hong Jin’s.*

Just a few days ago.

I’d definitely felt that déjà vu. And only now did I realize what I’d overlooked at the time.

*Listen carefully. Don’t react in any way.*

Still walking along as if nothing had happened, Hong Jin received a Sound Transmission from me as my lips barely moved.

*If the Emperor smokes opium, what do you think the reason might be?*

That day. That time. That moment.

The first source of the déjà vu I’d felt had been the one above all others, whom I’d encountered at Qianqing Palace.

* * *

“Hah.”

With a ragged exhale, the man suddenly opened his eyes.

The first things to fill his view were the torchlight flickering faintly beyond the darkness and the long, colorful silk curtains hanging around him.

*Where am I…*

There was no way he could mistake it. This was his bedchamber and fortress, where he’d spent most of the past decade or so.

The man lay there for a while, soaked in cold sweat as he caught his breath. Then he suddenly spoke.

“Is anyone there?”

The dry sound of his voice had barely faded when—

Rustle.

A breeze from somewhere stirred the silk curtains. A thread of Sound Transmission slipped through them and reached his ear.

*—At your command.*

The man said nothing for a while, slowly running a hand over his face.

He could feel the signs of fatigue in the deep furrows that didn’t belong on a face his age.

Though some time had passed since he’d awoken, his heart still pounded fiercely.

“It seems the sun has already set.”

*—It will soon be the hour of the Dog.*

“The hour of the Dog, you say. And the grand banquet?”

*—The appointed hour of the Goat has long since passed. The civil and military officials have all gathered.*

“Then is he there, too?”

He.

It was an inadequate way to refer to just one person among the many gathered for the grand banquet. Yet the shadow in the darkness answered without hesitation.

*—Yes.*

“……Unexpected. The martial artists of the world may be reckless enough to rush headlong into anything, but this is absurdly reckless.”

The Emperor muttered as if to himself, then continued.

“But someone had already foreseen this. In that case, his Master must still be there, too.”

*—He has attended as well. However…*

“Go on.”

*—The other martial artists, except for the two of them, have left the imperial palace.*

“Left?”

*—Yes. From what we’ve learned, they seem to be moving with a purpose, but we could not follow them any farther.*

“You couldn’t follow them?”

The man frowned, but the shadow’s next words left him with no choice but to fall silent.

*—Yes. ‘She’ personally intervened and stopped us.*

“……I see.”

*—If you command it, we can act at once.*

“No. No.”

The man shook his head and slowly rose from his bed.

The room was far too vast to be a bedchamber for one person. He stood before a large mirror, dressed in sleeping robes embroidered with golden thread.

Rustle. Thud.

The soft silk slid over his skin and fell to the floor.

An ordinary person would have shivered at the sudden chill. But the man standing alone was as solid as an iron tower.

Just as he’d been when he led a great army to crush the rebels.

Just as he’d been that day, more than a decade ago.

But for all his enduring spirit, the figure reflected in the mirror bore little resemblance to the man he’d once been.

*I’ve aged. Beyond recognition.*

The man thought to himself, but he felt no regret.

The path he’d walked was one someone had to take.

He’d simply been the one chosen.

He’d donned a dragon robe so dazzling no one dared look up at him, and been granted the two characters of Son of Heaven.

He had no regrets.

There was only the path still ahead, with just one step left to go.

“It’s time for me to leave Qianqing Palace.”

At his words, the darkness where the shadow had melted stirred, and Qianqing Palace, silent as a grave, sprang to life.

No. They had been ready from the very beginning.

Ready to kill and die at the Emperor’s command.

And on the roof of Qianqing Palace, its pulse throbbing like a volcano on the verge of eruption, a woman gazed up at the cloudy sky.

“Will it rain again today?”

So Gyo stroked the weapons hanging at either side of her waist.

She’d reclaimed them after a long time. They were as cold as ice, and the energy within them boiled as hot as fire.

* * *

The Grand Banquet Hall was unbelievably vast and impossibly quiet. Countless officials, great and small, had gathered in one place, yet not a single one of them spoke.

At least for that moment, they were all blind and sightless, all mute and unable to speak.

Those who already knew what was happening quietly reflected on the lives they’d led up to then. Those who didn’t know were frozen in place by the suffocating presence that had swallowed the Grand Banquet Hall.

Who would speak first?

Who would be the first to… draw a sword?

Just as everyone was thinking the same thing—

“There he is.”

A voice broke the silence.

“Five hours late. Are you kidding me?”

Jin Taekyung’s gaze pierced the darkness beyond the flickering torches.

More precisely, it pierced the enormous golden procession approaching from beyond, like a dragon.

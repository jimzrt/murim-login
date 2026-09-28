# Checkpoint Review — 1185–1189

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

# Chapters 1185–1189

## Plot

After the Imperial Army and Murim Alliance miss their deadline, Jeok Cheongang’s group follows Mae Jonghak’s contingency plan and enters Tianshan on foot, leaving the exhausted horses behind. Taekyung remains unconscious as the group struggles through the mountain’s lightless, uncanny mist. The mist suddenly overwhelms them and separates Jeok from the others.

Jeok stays with Taekyung on his back and fights the monsters emerging from the mist. A Black Ghost appears wearing the face of Jangcheon, Jeok’s former Disciple, later known as Jopil. Jeok nearly believes the figure’s plea for forgiveness, but recognizes the deception when it attacks and destroys it. Four more Black Ghosts then coordinate their attacks against him. Wounded while shielding Taekyung, Jeok prepares to unleash his full power, but Taekyung suddenly speaks.

## Continuity

- Jeok Cheongang is wounded and facing four coordinated Black Ghosts and waves of monsters in Tianshan’s mist. Jin Taekyung remains on his back, unharmed, and has just spoken after being unconscious.
- The group was separated by the mist’s power. The whereabouts and condition of the Bow Saint, Slaughter Saint, Gung Gibang, Hyuk Mujin, Ju Hwaran, and Song Ilseom are unknown.
- Jeok destroyed a Black Ghost wearing Jangcheon’s appearance. Whether it was connected to the real Jangcheon remains unknown.
- Mae Jonghak’s contingency plan is in effect: Jeok’s group advanced toward Tianshan after the allied forces missed their deadline, while the Murim Alliance and Imperial Army draw Dark Heaven’s attention away from the desert.
- Taekyung’s chest pain and difficulty sleeping remain unexplained. The Slaughter Saint also wondered whether Taekyung had held back his strength despite the fasting pill.
- The Lord of Heaven has awakened but says the process is incomplete; the Grand Mage awaits his command. The Main Quest “Rift and Collapse” failed, and “The Foreordained Collapse” warns that player choices can cause irreversible consequences. Cheon Taemin remains unconscious in a secret facility beneath the Pentagon. Alpha’s nature and awakening remain unexplained.

## Translation Decisions

- Use **Black Ghost** for 흑귀; distinguish **demonic qi** (마기) from **magical power** (마력).
- Render **환마** as **Illusion Fiend** and **귀곡자** as **Guiguzi**.
- Keep **Jangcheon** (장천) distinct from **Jopil** (조필), the name he used after leaving Jeok Cheongang.
- Render **파문하겠다** as “I cast you out of the sect.”
- Retain the established rendering of 진인사대천명: “Do all that man can, then await Heaven’s will.”

## Durable state

{
  "active_continuity": [
    "Jeok Cheongang destroyed a Black Ghost wearing Jangcheon’s appearance; four coordinated Black Ghosts and waves of monsters are attacking him in the mist.",
    "Jeok Cheongang was wounded while protecting Jin Taekyung, who remains on his back and unharmed.",
    "The other separated companions’ status remains unknown.",
    "The group is following Mae Jonghak’s contingency plan after the allied forces missed their deadline; the Murim Alliance and Imperial Army are drawing Dark Heaven’s attention away from the desert.",
    "The Lord of Heaven has awakened and regained strength, but says the process is incomplete; the Grand Mage awaits a command.",
    "The Main Quest “Rift and Collapse” failed; “The Foreordained Collapse” warns that player choices can cause irreversible consequences.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon; Jin knows he is the Martial God and a former Player.",
    "An alert reported Alpha’s awakening; what Alpha is and what its awakening means remain unknown.",
    "Taekyung has experienced unexplained chest pain and difficulty sleeping; the Slaughter Saint also wonders whether Taekyung used his full strength while affected by the fasting pill."
  ],
  "continuity_sources": [
    1189,
    1188
  ],
  "open_questions": [
    "Is the Black Ghost that wore Jangcheon’s appearance connected to the real Jangcheon?",
    "What is causing the mist’s power, and what has happened to the separated companions?",
    "What is the source of Taekyung’s chest pain and sleeplessness, and did he use his full strength against the fasting pill’s effects?",
    "What remains to be completed for the Lord of Heaven, and what command will he give the Grand Mage?",
    "What is Alpha, and what does its awakening mean?"
  ],
  "safe_through": 1189,
  "temporary_decisions": [
    "Render 진인사대천명 as “Do all that man can, then await Heaven’s will.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 1185

# Chapter 1185

“Good. There’s nothing wrong.”

At the Slaughter Saint’s first words after examining Jin Taekyung, Jeok Cheongang spoke with a grim expression.

“Are you sure?”

“I guarantee it.”

“That’s what you told me about three shichen ago.”

“Why not try having a little faith? The medicine just took a bit longer to spread through his system.”

“It’s hard to trust you. Things nearly went wrong because of some quack’s careless guarantee.”

For an instant, their eyes met in midair.

The tension tightened. After a brief silence, Jeok Cheongang let out a quiet sigh.

“I went too far. I apologize.”

“No, there’s no need to apologize. I understand how you feel.”

The Slaughter Saint truly didn’t mind.

He had spent half his life as an assassin and the other half as a physician.

Tending to more patients than he could count had taught him more than medicine.

It had taught him about the heart.

He had learned to feel the hearts of the sick, and of those who suffered alongside them, watching from closer than anyone else.

That was why he knew better than anyone that the man before him wasn’t the great martial artist known as the Fire King. He was Jeok Cheongang—a man, and the family of a patient.

*Besides, I’m at fault for not giving him enough reason to trust me as a physician.*

With that thought, the Slaughter Saint quietly studied Jin Taekyung’s face. He had already lost consciousness.

And at the same time, he remembered the terrifying strength and speed Taekyung had displayed moments ago.

*Everything had been perfect. The medicine I’d prepared in advance, even the time it would take for the effects to kick in.*

The fasting pill Taekyung had taken was the Slaughter Saint’s masterpiece, painstakingly crafted with the Myriad-Poison Ring in mind.

At first, it was no different from an ordinary fasting pill. But after more than three shichen, its effects would slowly begin to spread, and everything changed.

His limbs would be paralyzed, his mind and Qi Sense would grow hazy, and the medicine would even disperse his internal energy. The Slaughter Saint had been certain that no Supreme Peak master could easily endure all that.

He had even thought that if he himself were caught unaware after taking a dose, he would be in trouble.

*So how did this brat…?*

The Slaughter Saint’s gaze deepened as he looked at Taekyung.

Was it just his imagination? His back still seemed to tingle where the fierce wind from Taekyung’s fist had swept past moments ago.

A faint doubt crept in, too. Had that really been Taekyung’s full strength?

“……Maybe.”

The words slipped from his lips before he realized it.

When Jeok Cheongang turned to him with a questioning look, the Slaughter Saint immediately realized his mistake and shook his head.

“It’s nothing. Something just crossed my mind.”

“Could it be…?”

“Rest easy. I’ve told you more than once: there’s nothing wrong with your Disciple. At the latest, he’ll come around in two days.”

The Slaughter Saint watched as Ju Hwaran and Hyuk Mujin helped carry Jin Taekyung away, then added,

“And by the time he wakes up, we’ll be somewhere out there.”

At that, Jeok Cheongang turned toward the window.

Beyond the world where even the stars had disappeared, the immense Tianshan Mountains stood tall, impossible to erase completely with darkness, like monsters from myth.

As if they had stood there a thousand years ago and would still stand a thousand years from now.

But the Lord of Heaven, crouched somewhere in those mountains, was the true monster—a being worthy of being called an abyss.

They would have to wager the fate of the world to defeat him.

“I can’t tell if this was truly the right choice.”

At Jeok Cheongang’s question, spoken almost to himself, the Slaughter Saint replied,

“You know as well as I do. This isn’t the best choice, or even the second-best. It’s only the lesser evil that barely lets us avoid the worst—and the only choice left to us now.”

He was right. They had come too far to talk about the best choice.

With neither the Imperial Army nor the Murim Alliance arriving by the agreed date, there was only one path ahead of them.

And it was one of several possibilities they had considered even before leaving Qinghai.

*If no one arrives by the appointed date—if, by some chance, that happens…*

Jeok Cheongang suddenly remembered the Sword Saint, Mae Jonghak, whispering in a low voice during their secret meeting at dawn.

*“Leave this place and go to Tianshan. Without a moment’s hesitation.”*

*“Leave? Are you serious?”*

*“If things went wrong despite following a plan devised by the strongest martial artists and wisest strategists under Heaven, what more is there to say? The Son of Heaven has already agreed.”*

*“But—”*

*“This isn’t a sacrifice. It’s simply a choice made for everyone’s sake. No matter what calamity befalls us, we can still avoid the worst. We should have one move left.”*

Do all that man can, then await Heaven’s will.

Having done all they could, they would wait for Heaven’s decree.

Mae Jonghak had spoken aloud the six characters everyone had engraved in their hearts. He had clearly been smiling.

*“Then I’ll see you in Tianshan.”*

When morning came, they parted.

The Murim Alliance headed west. The Imperial Army headed east. And a single carriage, carrying the hope of them all, went into the desert.

To guard against any possible spies, the entire operation was carried out in utmost secrecy.

By the time everyone realized Jin Taekyung’s group was missing, Mae Jonghak announced that they had already joined the Imperial Army and were on the move. The Imperial Army did the same.

They pressed forward with all their might, constantly feeding the enemy false information.

They had to keep Dark Heaven’s eyes and ears—who knew where they might be hidden—from turning toward the desert.

So that, if the worst came to pass, they could serve as bait.

And their fears had become reality.

*What in the world happened?*

Jeok Cheongang forced down the question that lingered on the tip of his tongue.

And it wasn’t only his question. Everyone there knew something had happened to their allies. But no one said it aloud.

What they needed now was courage and hope that wouldn’t die—not anxiety, deep and sticky as a swamp.

*We have no choice but to keep going.*

The plan had not failed yet.

Though things had gone wrong, they would continue toward Tianshan without wavering, and their allies, once they arrived, would follow and join them.

It was only a faint hope, but for now, believing it was the best they could do.

“We leave. Before it gets any later.”

At the sound of Jeok Cheongang’s heavy voice—

*Fwoosh.*

The candle, flickering precariously and lighting the room, finally went out.

* * *

Once the decision was made, everyone moved in perfect order.

Only Jin Taekyung had been kept in the dark. The rest of the group had already considered every possibility and accepted the reality before them, so not one of them hesitated.

In that sense, the two days they had spent in this abandoned small town had been invaluable.

They had recovered from their accumulated fatigue. And the horses, worn out by their relentless forced march and no longer able to travel, could now become fresh provisions.

“Drain their blood and store it in gourds. Make jerky from the meat. The terrain will be too rough for a carriage from here on, and if we set them free, they’ll starve to death anyway.”

“D-do we really have to go this far?”

“What, have you grown attached?”

“I’d be lying if I said I hadn’t. They may be beasts, but we’ve been together for a while. Look at their eyes. Can’t you see they’re already filling with tears? It’s almost like they understand what we’re saying.”

“Fine. Then you can go hungry starting tomorrow, Hyuk.”

“Now that I think about it, my mouth’s watering.”

“……”

“What can they do about it? It’s their fault for being born beasts.”

It was a miserable fate for the eight sweat-blood horses that had done their best for them until now. But apart from the moral question, it was a perfectly reasonable decision.

Just after midnight, the moment they set foot in Tianshan for the first time, they all sensed it.

*What is this place…?*

It was different.

The weight of the air. The way the wind moved. Everything.

The atmosphere had changed, as though this were another world cut off from their own, and a chill suddenly ran up everyone’s spine.

They even felt as if they had been trapped in a prison shaped like a maze with no way out.

*What a vicious aura.*

Jeok Cheongang thought as his senses prickled.

Even a pool filled with corpses and poison wouldn’t feel this bad.

No—perhaps this was only natural.

This very Tianshan was the Land of Ruin, which had harbored the poison called demonic evil for the past thousand years.

And yet, it was also the final hill they had to cross.

They had rested, and they had secured plenty of food.

If they stayed alert for dangers lurking somewhere in the thorny undergrowth, they would soon reach their destination.

*The fact that we made it this far without a single interruption proves that, at least for now, we haven’t drawn their attention.*

With that thought, Jeok Cheongang gazed into the dark forest.

The situation might be going badly, but that alone was reason enough to hope.

And the old master, with his beloved Disciple on his back, would break before he bent.

*Step.*

Jeok Cheongang took his first step, putting his weight behind it.

A strong wind blew from somewhere. The dense gray branches all around them swayed, waving at the uninvited guests who had come without permission.
## Chapter artifact 1186

# Chapter 1186

Everything has a beginning.

Even a white-haired old man was once a baby, and not even a pebble by the roadside had always looked the way it did now.

All things in the world blend together according to a fixed order and change in the flow of time.

Nothing is perfect from the start. Nothing lasts forever.

That is the law of nature, the proper order of the world everyone knows.

And yet, right now, the group pushing through the pale mist was thinking the same thing.

Or, more precisely, they were wondering whether everything they had always taken for granted might be little more than an illusion.

The Fire King, Jeok Cheongang, was one of them.

*Damn it.*

He swallowed the curse rising to his throat and looked around.

Mist coiled in every direction. Beyond it, black branches appeared and vanished in fleeting glimpses. And beyond those, the rugged mountains climbed without end.

Order and laws?

Those ideas had long since been wiped clean from his mind.

Facing a landscape that seemed perfect in its present form, as if it had always been this way and would remain unchanged ten thousand years from now, Jeok Cheongang licked his parched lips.

The sight before him was more chilling than a mountain of sabers and a forest of swords. Looking at it, he could almost feel that the life he had lived for well over a hundred years, and all the experience he had gained, amounted to nothing.

If there was any small comfort, it was that he wasn’t the only one who felt that way.

“Damn Tianshan.”

At the voice that suddenly reached his ear, Jeok Cheongang silently agreed and parted his lips.

“Don’t say that. The youngsters will lose heart if they hear you.”

There was only one person who would send Jeok Cheongang a Sound Transmission in a situation like this.

The Slaughter Saint’s reply came at once.

“That’s why I’m using Sound Transmission.”

“Don’t use it at all.”

“Why not?”

“It wastes internal energy.”

The Slaughter Saint, who was walking a dozen paces ahead, turned to Jeok Cheongang with an incredulous look.

“Do I look like some Third Rate sword-for-hire rolling around the marketplace? And if you’re so worried about wasting internal energy, why don’t you practice what you preach instead of answering me?”

“This old man doesn’t mind.”

“Why not?”

“My internal energy is profound. Unlike some people’s.”

“……You can still crack jokes at a time like this.”

“What else can you do in a situation like this?”

This time, it was the Slaughter Saint’s turn to agree.

Even through Sound Transmission, he could hear how subdued Jeok Cheongang sounded. His own gaze grew heavy.

“Like I said earlier, this place is truly something. I thought I’d seen a fair bit of the world after traveling all across the land, but…… I’ve never heard of or seen anything like this.”

Unlike Jeok Cheongang, who had spent most of his life on Mount Jiuhua, the Slaughter Saint had lived a wandering life—as an assassin, and then as a physician.

In his youth, he had traveled a thousand li to take someone’s life. In his old age, he had wandered ten thousand li in search of herbs to save one.

Even a young woodcutter who lived day to day cutting trees would have his own experiences and his own life. For someone who had made his mark at opposite ends of life and death, calling his experience “a fair bit” was an understatement born of extraordinary modesty.

Of course, to Jeok Cheongang, who shared the same reality, it sounded entirely sincere.

“So even you don’t have an answer, then, though I expected as much.”

“There’s no way forward, nothing we can do. We can’t even tell day from night. What can we possibly do?”

The Slaughter Saint was right.

The fog blocking their way wasn’t limited to the ground.

There were dark clouds.

At first, they had thought the enormous black mass was just passing by. But it had covered the sky, too.

The moon and stars, which had faintly lit the sky above them at first, disappeared. The clouds swallowed up every last one of them, and wouldn’t even allow a single ray of sunlight through.

As if they meant to frighten the rude intruders who had come without permission.

“Do you think these phenomena are coincidences?”

“Coincidences?”

Jeok Cheongang let out a hollow laugh before he knew it.

“If you’d asked the old me, I would’ve said they were. Yes—if I hadn’t met that impudent brat riding on his master’s back and giving the old man a hard time at this age.”

Jeok Cheongang gazed at the face of the “impudent brat” occupying one of his shoulders.

His Disciple, who had appeared out of nowhere one day and turned the life of an old, sick man upside down.

And now, the man who was changing the world for everyone, not just the life of one person.

“There are no more coincidences for us. Everything that happens from here on is intended, inevitable—and maybe……”

Maybe it was fate, decided from the very beginning.

Jeok Cheongang quietly swallowed the words he had been about to add.

It wasn’t because he didn’t believe in things like fate.

It was because if all of this was fate, then it was cruel beyond measure to Jin Taekyung—and, more than that, he was afraid of how this story would end.

“Maybe what?”

“No, nothing. Let’s move on. What matters more is our situation right now.”

Jeok Cheongang’s words and behavior were unnatural to anyone watching, but the Slaughter Saint didn’t press the matter.

He was a little disappointed, but everyone had their own worries. And the Jeok Cheongang he had watched over the years was far more thoughtful and introspective than people believed.

Especially where Jin Taekyung was concerned.

*Then again, I’m hardly in a position to judge him for that.*

With that thought, the Slaughter Saint’s gaze shifted past Jeok Cheongang’s shoulder.

The young men panting hard as they raced across the rugged mountain terrain, and the Great Sir and Bow Saint bringing up the rear with calm expressions.

But his gaze lingered on them only for a fleeting moment. Then, as if nothing had happened, he spoke.

This time, in his own voice rather than through Sound Transmission.

“We should take a short break.”

His voice spread through the increasingly dense mist.

* * *

The Slaughter Saint had judged well.

No sooner had they been given a brief rest than Hyuk Mujin began retching. Gung Gibang, instead of patting his back, pulled out some jerky.

“……You traitor. Is that jerky really so good?”

After Ju Hwaran helped him stop retching, Hyuk Mujin glared at Gung Gibang. The beggar answered without hesitation.

“Of course.”

“……”

“Still, this stuff is incredible. Maybe it’s because it came from sweat-blood horses? The flavor’s remarkably consistent.”

“……”

“Don’t just glare at me. Eat quietly. You need your strength. Or you could sit down and circulate your qi like that fellow.”

Hyuk Mujin glanced between Song Ilseom, who was already sitting cross-legged, and Gung Gibang, who was still tearing into his jerky. Then his expression hardened as he made up his mind.

“Give me a piece. I want to see what’s so good about it that you’re eating like a beggar who hasn’t had a meal in three days.”

When they had first met, the two had been worlds apart in martial prowess and status. But they had spent enough time together to become almost like friends.

Gung Gibang grinned, showing his yellow teeth.

“Excellent decision. Oh, Young Lady Ju, would you like some, too?”

“No, thank you. I think I’d better circulate my qi for a while.”

Replenishing one’s strength and refining one’s internal energy were both good choices.

Climbing mountains—and rugged mountains at this altitude, no less—caused a completely different kind of exhaustion from running across flat ground.

Besides, even they, whose martial arts were far less advanced than those of the masters traveling with them, could feel the heavy air hanging over all of Tianshan and the strange phenomena that defied explanation.

“Damn, I can’t even remember the last time I felt warm sunlight.”

At Gung Gibang’s grumble, Hyuk Mujin spoke with his mouth full of jerky.

“We got some in the desert.”

“How was that warm sunlight? During the day, I was too scared to even walk around in case I burned to death. Though, by the time we got halfway across, I was starting to miss it.”

“Fair enough. The weather was a real pain in the ass.”

In truth, “a real pain in the ass” didn’t begin to cover it.

What kind of desert had no cacti or bugs, and got alternating hailstorms and downpours for more than half a month?

But now, this was the world they lived in.

And to survive in a changed world, they had to change, too.

“I’m dying here. How many peaks have we climbed already?”

“Five.”

“Already? That’s more than I thought.”

“Not that many, considering how hard we’ve run. And we don’t know how much farther we have to go.”

The Tianshan Mountains were wide.

No, “wide” didn’t do them justice. They were vast.

The range stretched for more than a thousand li, and covered no less than a third of Xinjiang.

And that wasn’t all. It was a Sacred Land, where only a select few among the old Demonic Cult had been allowed to enter—and a Land of Ruin, where any outsider was sure to meet death.

They still had no idea which of the hundreds of peaks held the Cult’s headquarters.

“Terrible.”

“Terrible.”

“At least nothing’s happened yet. That should mean we haven’t been spotted.”

“If the Captain heard you say that, he’d smack you one.”

“Why?”

“He hates that kind of talk. Says it’s bad luck. Something like ‘cli’ or ‘guli’—anyway, it sounds like he’s talking about copper. I never know what he means.”

“Honestly, I can never figure him out.”

“Tell me about it.”

The two muttered as if to themselves, then lay on their backs, gazing blankly at the sky.

Or, more precisely, at the dark clouds that filled it completely.

“How long exactly have we been here?”

“More than a day, less than two.”

“Are you sure?”

“I’m sure.”

“Hard to believe you can say that when you can’t even tell night from day.”

Hyuk Mujin answered firmly.

“Because the Captain still hasn’t woken up.”

“Oh, right. The Slaughter Saint said he’d wake up within two days at the latest.”

“Yeah. So it definitely hasn’t been two days yet.”

Gung Gibang studied Hyuk Mujin for a moment, then suddenly gave a quiet laugh.

“What?”

“It’s just…… You’re something else.”

“Something else how?”

“Almost everything seems to revolve around Jin Taekyung.”

“I don’t know. This all seems perfectly natural to me.”

“Don’t get me wrong. I’m not saying it’s strange or that I don’t understand. I’m saying it because I know exactly how it feels.”

The smile lingering on Gung Gibang’s lips faded.

“That’s what a martial family is. You may not share blood, but sometimes the bonds are thicker than blood.”

Gung Gibang drifted into old memories for a moment, and Hyuk Mujin fell silent.

It felt like a wound he’d kept hidden for a long time had finally burst open.

The Jin Family of Taiyuan. And the Beggars’ Sect.

They were their martial families, their other homes—and the names of two enormous stones weighing down their hearts.

What had happened to the people who had headed west with their banners held high?

If they were still alive, would they ever meet again?

They traded silly remarks on the surface and tried to keep smiles on their lips, but reality was cold enough to make them shudder.

It was even quick enough to allow them no chance to fend off the chill seeping into their very bones.

*Shhhhhhhh.*

A sudden sense of wrongness.

In the next moment, the mist, twisting as if alive, was reflected in Hyuk Mujin’s suddenly widened eyes.
## Chapter artifact 1187

# Chapter 1187

A snake.

That was the first word that came to everyone’s mind when they saw the mist writhing toward them.

It crept closer, gloomy and dark, like a huge predator that had spotted its prey. Their legs, already frozen stiff as statues, would hardly lift from the ground.

Something beyond what they could see was stirring the most primal fear in them.

And the Fire King, Jeok Cheongang, was one of the few people who could recognize the true nature of the power within that mist before anyone else—and understand it clearly.

*This is……!*

There was no doubt.

Demonic qi.

No—or magical power, as it was now called. That abyssal energy flowed through his five senses, binding his body and mind.

Terrifyingly fast. Insidiously.

But why? Separate from the fear surging in one corner of his mind, Jeok Cheongang suddenly felt an intense, inexplicable pull.

It was a truly strange feeling.

Like the warm embrace of a mother he could no longer remember, it made him feel that if he gave himself over to the mist now, everything would be easier.

Surely, in that hazy world, a peaceful paradise awaited him—one without hardship or anguish—

*Crack!*

Blood burst forth with a sharp sting of pain.

In that instant, Jeok Cheongang bit his tongue to regain his reason. He spat the blood filling his mouth and roared.

“Ha!”

His azure dragon’s roar shook the air in every direction with the force of his internal energy.

And he wasn’t the only one to unleash a battle cry like a beast’s roar.

The Bow Saint and the Slaughter Saint.

The two superhumans who had reacted at the same time as Jeok Cheongang groaned as they watched the mist falter, if only briefly.

Dark arts.

And not just any dark arts. A powerful, sinister force unlike anything they had ever seen was consuming the space around them.

No—perhaps all of Tianshan.

But they faced an even greater problem.

“Ah.”

“Ahhh.”

Dazed eyes, as if they were dreaming, and vacant voices. Hands reaching through empty air, feet slowly carrying them toward the mist.

Not a single person was spared. Gung Gibang and Hyuk Mujin, who were closest to the mist, and even Ju Hwaran and Song Ilseom, who were farther away.

As their companions turned into soulless people who seemed to have lost their reason, the three veteran masters sensed the danger and shot toward them without hesitation.

And the moment they reached out, hands moving like streaks of light—

*Whoosh!*

A sharp whistle cut through the air, and space warped.

The mist, now curved into a giant beast’s razor-sharp claw, and the darkness seeping through it reflected in Jeok Cheongang’s reddish eyes.

“How dare you!”

*Fwoosh—BOOM!*

With his furious cry, the flames of the Flame Divine Palm burst forth, shattering the claw of magical power and heating the air.

A searing blaze that allowed not so much as an inch of approach.

But it didn’t take long for him to realize that this momentary ambush had been entirely deliberate.

*Shhhhhhh.*

In the cloud of steam that rose pale and white, Jeok Cheongang’s eyes widened before he knew it.

He couldn't see them.

Gung Gibang’s threadbare collar, within reach if he stretched out a hand. Hyuk Mujin’s head, which made Jeok Cheongang want to smack him just looking at it.

No.

*They disappeared.*

Yes, that was probably the best way to put it.

He had seen it with his own eyes.

He had watched their bodies, swallowed by the mist, get erased from the world.

*What is this…?*

Jeok Cheongang swallowed the groan rising to his throat and hurriedly looked around.

At the same time, he realized something very important.

They weren’t the only ones who had vanished along with the mist.

“……Huh.”

Jeok Cheongang let out the breath he had been holding.

When had it started?

That strange sense of déjà vu he’d felt earlier?

He didn’t know. The scenery before his eyes hadn’t changed, but everything else had.

No one. There was no one.

Even the Bow Saint and the Slaughter Saint, who had been barely three yards away, were nowhere to be seen.

Not a trace of their presence—not even a hair’s breadth of their energy, which he should have been able to feel.

*An illusion technique? Or a Mystic Gate Formation?*

All manner of dark arts he had heard about in rumors, or experienced firsthand on the battlefields of the Great Faction War, flashed through Jeok Cheongang’s mind. But he couldn’t reach an answer.

Even he, a giant who had lived for over a century and made his mark on an era, had never encountered dark arts of this kind.

*This is on a different level.*

He meant it literally.

Even the great fiends of the previous generation, infamous under names like the Illusion Fiend and Guiguzi, couldn’t wield dark arts this powerful.

More precisely, Jeok Cheongang’s formidable martial prowess had never allowed them to.

No matter how powerful the dark arts, they still had limits.

The Illusion Fiend, the Demonic Cult’s greatest master of illusion, had had both eyes gouged out. Guiguzi, who had slaughtered hundreds of orthodox Murim warriors with his intricate Mystic Gate Formation, had melted into a pool of blood.

Both at the hands of one man: the Fire King, Jeok Cheongang.

But……

*I’ve never seen or heard of a formation like this.*

Jeok Cheongang expanded his search with senses sharper than ever. The longer he searched, the more his thoughts solidified into certainty.

No matter how bizarre the dark arts, everything had a flow of energy and a core at its center.

But in this strange space, he couldn’t sense a thing.

Only the dark mist approaching with the uniquely sticky, unpleasant energy of demonic qi—and someone’s steady breathing against his back.

“Sleeping soundly even after all this. You’ve got it easy, you know.”

His tone was gruff, but a faint smile brushed his lips.

Jeok Cheongang glanced at the face of the Disciple who would have complained bitterly if he were awake. Then, as if making a promise to himself, he muttered,

“Don’t worry. No matter what happens, I won’t let a hair on your head be harmed……”

His voice suddenly trailed off.

For some reason, he fell silent for a moment, then added with a sigh,

“Just bear with it. One hair getting hurt won’t kill you.”

This time, too, his Disciple did not answer. His Master gazed beyond the dense mist with eyes that shone fiercely.

“What are you waiting for? Crawl the hell out here!”

At the giant’s call, the beings beyond the pale veil answered.

*Grrrr.*

In the mist flowing like waves, countless eyes suddenly gleamed.

Jeok Cheongang slowly took a deep breath.

“You came in a pack.”

Heat shimmered out from the Extreme Yang energy extending through his limbs and every part of his body. His two fists, engulfed in fierce flames, pointed at the monsters that did not belong in this world.

“Come on.”

The long night had begun.

* * *

Mist so thick he couldn’t see an inch ahead. Countless shadows surged through it.

And at the center of it all, flames burned ever more fiercely.

*Boom!*

One palm strike.

No more was needed. At the end of that supremely efficient, devastating motion, there was only heat enough to melt rock—and death.

*Thud!*

A huge body that could hardly be called human sank to its knees.

Three red eyes embedded in its single head still fixed on their prey, but its chest, melted without a trace, proved which of them had been the hunter.

*Grrk.*

The last gasp escaped it, and light quickly faded from its eyes.

But before the monster had even breathed its last, the hunter had already turned away, setting other lives ablaze.

*Crack!*

He smashed, burst, and crushed without pause.

Hands, feet, legs, knees and elbows—sometimes even his forehead.

Everything was a weapon, and everything led to something’s death.

Neither the five-foot-tall monsters nor the three-headed, six-armed ones could break through the blazing wall of fire.

Claws sharper than scythes and rusty blades where human arms should have been relentlessly targeted his limbs, but neither Jeok Cheongang’s body nor his mind faltered.

It was like the day Mount Jiuhua had been engulfed in flames, decades ago.

No—the state he was in now was far stronger and colder than he had been then.

The thousand members of the Demonic Cult who had drawn the old monster called the Fire King out of Mount Jiuhua had at least looked human. The monsters before him were cursed beings that should never have appeared in the human world.

*Kyarruk!*

*Kraaaaah!*

A madness and killing intent he had never felt anywhere before.

They had clearly lost their reason long ago and moved only at their master’s command, yet they kept charging at him—

*RrrrCRUNCH!*

—and kept dying without respite.

*Splaaat!*

Blood sprayed high into the air.

With a single sweep of his hand, as if brushing away insects, he sent hundreds of pieces of flesh flying in every direction.

“Is that all you’ve got?”

In the gap of death and emptiness that had opened in an instant, Jeok Cheongang swept his gaze across the area and muttered,

“Did you really think you could take me down with this?”

Suddenly, the words of his Master, whose face had grown hazy with time, came to mind.

*“Cheongang, the world is vast, and there are many strong people.”*

Just as his Master had said, the world beyond Mount Jiuhua had been vast.

The Heavenly Demon, who had swallowed half the world, and the great fiends who followed him had been strong. So had the Daoists and Buddhist monks who occupied the Central Plains.

But that wasn’t all his Master had said.

*“But you could become one of the strongest among them.”*

As always, his Master’s words had been right.

And on top of that, the presence of a certain young life he carried on his back made him even stronger now.

“Since you won’t come to me, I’ll come to you.”

*Hiss.*

Heat rose with every forceful step.

Had even instinct survived in the monsters who had lost their reason?

The monsters, who had briefly halted their attack in the face of the overwhelming difference in strength, watched as Jeok Cheongang slowly walked toward them.

No—more precisely, he was about to.

Until a voice he could never forget pierced his ear.

“You’re as I remember.”

In an instant, Jeok Cheongang froze.

At the same time, the fierce light in his eyes faded like a lamp caught by the wind, and someone’s figure was reflected in them.

The face of someone who could not be here—and should not be.
## Chapter artifact 1188

# Chapter 1188

It was as if time had stopped.

Every foul odor and the reek of blood that had filled the air around him faded, and the monsters’ roars became faint echoes. But Jeok Cheongang felt none of the changes surrounding him.

No—he couldn’t feel them.

All his senses were already focused on a single being.

*Squish.*

Unhurried footsteps approached, treading through a pool of blood.

The monsters had stopped moving at some point, splitting apart to either side. Through them, someone came into view, filling Jeok Cheongang’s vision completely.

His heart froze with a chill so sharp it hurt.

“……You.”

The trembling voice that slipped between his pale lips was more than a mere sound.

It was a groan that escaped him unbidden, a scream he had barely managed to suppress.

“How have you been?”

A voice he had never forgotten. And a face that had grown a little unfamiliar.

The name of the man he was seeing again after well over ten years spilled from Jeok Cheongang’s lips with a cold breath.

“Cheon-ah, how are you—?”

The man, Jangcheon, smiled faintly at his old Master.

“It’s been a long time since anyone called me that.”

Each quiet word sank into Jeok Cheongang’s ears.

Raking through his lungs. Piercing his heart.

“I admit, I was worried you might not recognize me.”

As if that were possible.

Even if a hundred years had passed instead of ten, Jeok Cheongang would have recognized him.

Then, as now.

Though much had changed, he was someone Jeok Cheongang could never forget—not even until his dying breath.

“But it seems my worry was misplaced. You, of all people, would never forget me, Master. I nearly failed to recognize you, though, unworthy Disciple that I am.”

Since the day they parted in a dark back alley, the Disciple had aged a little, while his Master had grown much younger.

But it wasn’t only his appearance that had changed, becoming that of a middle-aged man after he Returned to Youth.

Everything had changed.

Every last thing.

And among those changes was one unshakable truth that no one could ever alter.

“You…… weren’t you already dead?”

It was a day of heavy snowfall, so he’d heard.

At Jeongyang in Shanxi Province, somewhere on an unnamed mountainside, Jangcheon had died in front of several witnesses. Miserably and pitifully, as if being judged for all the sins he had accumulated.

But.

How could—

“Dead? You mean me?”

His eyes widened for a moment, then curved with a laugh.

“Ha. Did you really think I was the kind of bastard who’d die that easily?”

“No. I definitely heard—”

“Yes, you heard. You didn’t see it for yourself.”

Jeok Cheongang’s eyes wavered at the calm reply.

It was true.

When he had finally asked around and found the place, all that remained were a few traces of a fierce battle. Jangcheon’s body was nowhere to be found. No one knew exactly why, and no one was particularly eager to find out.

Jeok Cheongang had only thought that the heavy snow said to have continued for nearly seven days and nights, along with the mountain beasts, might have erased Jangcheon’s last traces from the earth.

That was all.

He had left a bottle of liquor and a few drops of tears there, then returned to his own life.

That was what had happened.

“……You were really alive all this time?”

“I nearly died, at least. At the hands of that brat you’re tending like a shrine.”

His eyes were pale as mist.

At their end, over Jeok Cheongang’s shoulder, was Jin Taekyung’s face.

“I can feel a familiar power coming from him. The qi of the Fire Gate Clan—our sect, a power that once belonged to only you and me.”

Jeok Cheongang didn’t answer. Jangcheon slowly took another step.

*Squish.*

“I’ve heard it until my ears were worn out. The story about how I somehow got an unexpected Junior Brother.”

“You’re wrong. All of it.”

Jeok Cheongang’s voice came through his clenched teeth.

“This boy is not your Junior Brother, and you are no Disciple of this old man.”

“Why not?”

“Because you were cast out. Because you died after committing unforgivable atrocities. And that is the only truth.”

*Crack.*

His lips split, and blood filled his mouth.

But the scene before him, which should have been an illusion, didn’t change at all.

Not the shadowed face of his old Disciple, nor the voice that kept pouring into his ears.

“But Master, look. I’m still alive, aren’t I?”

“Don’t call me that!”

Even at Jeok Cheongang’s thunderous shout, Jangcheon kept coming. He looked at him with eyes full of regret.

“I knew what you must think of me, Master.”

“Will you shut your mouth!”

“After I came back from the brink of death, I spent a great deal of time thinking about everything that had happened. A time when each day felt like ten years.”

*Squish.*

The pool of blood rippled beneath his advancing steps.

The monsters stood motionless behind him, as if they had made an agreement to stay put. As he drew closer, Jeok Cheongang could sense no danger or killing intent from him.

But—

*That’s impossible. This is all an illusion and a hallucination.*

Jeok Cheongang clenched both fists. As if responding to their master’s turmoil, the qi within him bucked out of control. He subdued it and drew it up again.

Then a single unexpected sentence reached his ears.

“I was wrong. This unworthy Disciple was wrong about everything.”

“……!”

In that instant, the eyes that held the weight of a long life trembled, unlike the body that had regained its youth.

“Please forgive me. No—Master, punish this wretched man yourself.”

No. That couldn’t be.

He mustn’t fall for this nonsense conjured by dark arts.

And yet, for some reason—

The Extreme Yang energy gathering in his clenched fists wavered like a candle in the wind, then went out.

Just as on that day when, despite having martial arts powerful enough to look down on the whole world, he could only watch his Disciple walk away.

“I won’t make excuses. Whatever punishment you give me, I’ll bear it all.”

The words he had wanted to hear so badly.

“I betrayed your trust, disgraced our sect, and killed innocent people, committing sins that can never be washed away.”

The scene he had imagined countless times.

“So please, kill me.”

“……Enough.”

“Kill me. With the very hands that took me in more than twenty years ago.”

“Enough. Stop.”

He couldn’t breathe. His heart hurt as if an unseen hand were squeezing it.

Everything he was seeing and hearing had to be nothing but an illusion.

It had to be.

The wound deep inside him, the one he thought had healed, was opening again.

“Master.”

Jeok Cheongang didn’t answer.

He only stared blankly at his old Disciple as his vision grew hazy.

Along with him came the faded, tattered memories settling over the present.

*“If I can’t take you as my Master…… I’ll kill myself.”*

Even now, more than twenty years later, he remembered it clearly.

*“No, kill me right now. With the very hands that saved my life.”*

The desperate look in the boy’s eyes.

*“Might Makes Right. Didn’t you teach me that, Master? That’s the Murim—or rather, that’s the world. The weak should die at the hands of the strong.”*

The murderer’s smile, impossible to forget.

*“Kill me. That’s the only way to stop me.”*

And the sight of a feeble old man, unable to stop him in the end.

Even after he had gone out into the world to correct that mistake, he had lingered for a long time at the very spot where wild beasts and snow-laden winds had passed.

*“Old man, has something happened?”*

The mountainside where a man who had lived as Jangcheon had fallen under the name Jopil.

A traveler had wondered at the old man standing there late into the night, still as a stone monument, and asked him what was wrong. Jeok Cheongang had answered:

His only blood relative had died here.

The man had been foolish and useless beyond words, but he had come hoping to at least recover the body.

And in that moment, he had suddenly realized:

Even after nearly ten years, he still wasn’t ready.

“Master.”

At that clear voice, the layers of memories began to scatter.

Through the streams of tears flowing like a broken dam, he saw the face of the Disciple he had wanted so badly to meet.

“Cheon-ah.”

“Yes. I’m listening, Master. I’m here with you.”

*Squish.*

One step.

*Squish.*

Another step.

*Squish.*

They were close enough to feel each other’s breath.

The Master finally beckoned to the Disciple he had been reunited with. The Disciple who had returned across the long years took the final step toward that small embrace.

And with him came a single streak of light, prepared from the very beginning for this moment alone.

*Thud.*

A pain hotter than any Scorching Yang Qi.

At the same time, blood burst forth, proving that this was all real.

*Shhk—thud-thud-thud!*

On the ground splattered with fresh blood, two gazes met across the handspan of empty space between them.

One deeply sunken. The other wide with disbelief.

Then, in the silence of that instant, one man’s lips parted.

“……How?”

At Jangcheon’s question, his agitation impossible to hide, Jeok Cheongang smiled sadly.

“I wanted to be fooled for a moment. I wasn’t fooled.”

Jeok Cheongang tightened his grip on the blade he had caught at the last moment.

*Crreeeak.*

It hurt.

Every time the dagger embedded in his palm twisted, a dizzying pain spread through his body.

But it didn’t matter.

This pain was nothing compared to the mind demon that had tormented him only moments ago.

*“What’s your name?”*

It had been more than twenty years ago.

He had met a boy who endured kicks raining down on his whole body and still managed to shove a dirt-covered bun into his mouth.

*“……I don’t know.”*

The old man had seen his younger self in that boy.

A fiercely determined little boy who had wandered the world long ago, begging for food without even knowing his own name.

Perhaps that was why the old man’s heart had changed its mind on a whim.

*“Jangcheon. From now on, that’s your name.”*

The Master had given him a name and a new life. The Disciple had thrown them both away and left.

And the wound that had sunk deep into his heart because of it had become a scar that would never fade.

But……

“I think I can let you go now.”

Yes. At last.

With those words, which Jangcheon would never hear, Jeok Cheongang threw a single punch.

*Kwaaaaaah!*

A raging inferno engulfed Jangcheon—or rather, whatever had taken on his illusion—and swept over the mountainside.
## Chapter artifact 1189

# Chapter 1189

“Grrrraaaaaah!”

It wasn’t a scream a human could make—or even a sound any living creature could produce.

It was all that remained of a monster that had already died once and forgotten pain.

A warning bell announcing that his corrupted soul had burned away. The final death cry that heralded his second death.

*Fwoooooom!*

The hellfire of the Flame-Extinguishing Divine Fist swept wildly through the space.

Then came a blinding flash, followed by an even louder roar.

*RrrrRUMBLE!*

The ground shook. Embers and ash, churning in the murky air, scattered in every direction.

Beyond them, a shadow slowly crumpled.

Jangcheon.

No—one of the monsters wearing Jangcheon’s face.

*Black Ghost.*

Jeok Cheongang recognized it at once.

A monster given new life using the body and soul of the dead.

Neither dead nor alive, they were the strangest and most powerful among the countless monsters under the Lord of Heaven.

Yes, this was surely—

*Magic, after all.*

A space where even the wind brushing his skin felt alien.

Phenomena too intricate and bizarre to be explained by a mere formation.

The suspicion he had been harboring became certainty. Jeok Cheongang felt the flow of qi surrounding the area begin to churn.

And he sensed the cause of the change, too.

*Shhhhh.*

A sudden cold wind swept in, pressing down on the heat haze that distorted the space and settling the drifting embers and ash.

It wasn’t an ordinary wind. It was a wave of qi announcing the arrival of something else.

“So, you’ve come.”

Jeok Cheongang looked at the new intruders with steady eyes.

East, west, south, and north.

Four shadows had appeared, each holding a position around him and gazing his way.

Different faces, yet somehow alike.

“Master.”

Four voices rang out as one.

There was Jangcheon as a dirt-covered child, just as he’d looked the day they first met.

Jangcheon as a boy, pleading to be accepted as a Disciple.

Jangcheon, now a young man.

And Jangcheon as he’d looked on the day he left.

All frozen in forms from a day that could never be taken back.

“Master. I’ve come. Cheon-ah is here.”

The four Jangcheons spoke together and stepped forward. At the same time, the countless monsters encircling the area closed in.

A net over heaven and earth, drawn tight for one man alone.

Yet even amid the monsters’ thick killing intent, Jeok Cheongang spoke calmly.

“What a strange business. Four more Disciples I never knew I had.”

“Master. How could you forget me?”

The voice rang out from every direction, as if all four shared a single body. Jeok Cheongang gave a bitter smile.

“I haven’t forgotten. I simply resolved to keep you as a memory now.”

He wasn’t speaking to the monsters wearing the illusion. He was speaking to his old Disciple, who wasn’t there.

It didn’t matter if his voice reached no one. Only now had he understood for certain. If he didn’t say it now, he might never get the chance.

Even if the living Jangcheon had appeared before him, his choice would have been the same.

“I was a wretched Master, and you were a wretched Disciple. But let’s settle the debts we owe each other—not in this life, but some distant day when we meet again.”

Spilled water couldn’t be gathered up, and time that had passed could never be turned back.

What mattered was now. And Jeok Cheongang still had something precious to protect.

“So, Cheon-ah.”

Just as he had long ago, Jeok Cheongang gently let the name of his old Disciple leave his lips.

His eyes moved from one face to the next, taking in the features still etched vividly in his memory.

He felt the warmth and breath of someone on his back.

He felt alive—and resolved to stay that way.

“I cast you out of the sect.”

In that instant—

*Whoosh!*

A flash erupted in the dark mist.

No. It was a flame burning as bright as light—and a giant of fire, finally risen to his feet.

*Fwoooooom!*

The heat of the Flamefire Path distorted the space.

One step. Nearly a hundred yards vanished, and the monsters’ wide eyes rushed closer.

*Crunch!*

No more words or thoughts were needed.

The Fire King, Jeok Cheongang, crushed everything in front of him.

Enemies surged in from every direction, but he saw and felt everything happening around him.

With his eyes, his ears, and sometimes with a sixth sense beyond the other five.

“Grrrraah!”

A group of monsters charged at him, each with eight arms and three heads.

They looked like asuras from legend. Their many arms—impossible to tell apart as human or beast—whipped wildly, raining blows down on Jeok Cheongang’s head.

Or, more precisely, the spot where he had been.

*Crack-crack-crack!*

Their attacks cut through empty air and carved up the ground. Then a voice pierced the monsters’ ears.

Quiet, yet hot as fire—and all the colder for it.

“How many hearts do you have?”

That was the last thing they heard.

*Fwoosh—SPLAT!*

Even as their consciousness faded, the monsters didn’t know when or how they had died.

They didn’t know Jeok Cheongang had launched himself off the ground, extended his Palm Force, and slashed downward with it.

Nor that the horrific heat within it had burned not only their hearts, but every organ in their bodies.

But the four pairs of eyes watching Jeok Cheongang did know.

They had been waiting for this moment from the start, and moved together as if on cue, without a hair’s breadth of error.

*ShhhhK!*

A low, faint whistle slipped into his senses, keen as a blade and chilling enough to raise goose bumps.

Jeok Cheongang, who had just melted dozens of monsters in an instant, immediately sensed the ominous energy rushing right up to him.

He sensed that there was more than one.

But their speed—and the power they carried—exceeded anything he’d expected.

“……!”

In that slowed instant, Jeok Cheongang sensed four lines of Force closing in from his blind spots.

He twisted with all his might, moving by instinct more than reason.

*Shhk!*

Blood sprayed with a cool slicing sound.

Not the monsters’ green blood, with its foul stench and poisonous fumes, but the red blood of a living human.

Even through the sting of pain, Jeok Cheongang regained his balance at the last possible moment and landed with a satisfied smile.

What a relief.

His flesh was injured, but Jin Taekyung hadn’t so much as been scratched.

But the smile brought on by that relief didn’t last long.

His wound wasn’t serious. The battle, however, was clearly turning against him.

A Master fighting to protect his Disciple, against countless monsters charging without fear of death.

And the greatest problem of all: the four Black Ghosts, carefully measuring their distance and looking for an opening even now.

*Strong. Stronger than I expected.*

They seemed at least a full step above the other Black Ghosts he had faced—perhaps even two.

He didn’t know whether that was because of the Magic surrounding the area or because these four were particularly powerful specimens. But one thing was certain.

*This will be a tough fight.*

In truth, even that didn’t begin to describe it.

Their individual strength was formidable, but the four Supreme Peak masters moved like one organism, sharing their thoughts. Even Jeok Cheongang couldn’t afford to underestimate them.

The same would be true even if they were living humans. But these monsters felt neither emotion nor pain.

And the situation was going their way in every respect.

Even now.

“Grrrraaaah!”

The monsters roared and charged again, while the Black Ghosts vanished among them. Jeok Cheongang understood their intentions at once.

*They’re taking turns wearing me down…!*

To break a huge rock quickly, you needed a sharp chisel and a heavy hammer. But given enough time, even the occasional rain shower could do the job.

Drop by drop, the water struck the hard surface of the rock, wearing it down and making cracks.

And the monsters surging without end under the Black Ghosts’ command were neither light raindrops nor a passing shower.

They were waves.

Raging waves, bearing the force to smash through any reef—and a blind madness that made them hurl their lives away without hesitation.

But Jeok Cheongang wasn’t a rock that would simply stand still and wait to be worn down.

*I’ll finish this in one blow.*

His nature was fire. He had raised a greater flame than anyone under heaven, and so he was the Fire King.

*Crack.*

Jeok Cheongang clenched his teeth.

His eyes glowed red, piercing the dark mist. Space warped along the heat haze rising strand by strand from his entire body.

*Fwoooosh.*

An energy like molten lava surged through his limbs and every part of his body. A breath like steam escaped between his slowly parting lips.

“I’ll kill every last one of you.”

If they were rocks, he would melt them. If they were waves, he would make them evaporate.

Even if he himself turned to ash, even if everything burned away, the Fire Gate Clan’s flame would never die.

No—the blaze that rose from it would become even greater than his own.

“Come!”

The giant’s roar shook the air in every direction as he completed his preparations.

“Whoa, that scared the hell out of me. My ears are going to burst.”

“……!”

Jeok Cheongang barely managed to rein in the internal energy that had nearly turned back on him.

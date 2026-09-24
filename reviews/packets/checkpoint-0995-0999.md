# Checkpoint Review — 995–999

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

# Chapters 995–999

## Plot

After learning that Dark Heaven is massing in Xinjiang, Taekyung leads the Fire Dragon Pavilion west to investigate. The Hidden Shadow Pavilion has lost more than thirty agents, and Dark Heaven’s army may number over a hundred thousand. Taekyung completes his meditation and assimilates the Heavenly Power Demon’s and Peng Cheolhu’s energy, bringing his controlled internal energy to four jiazi. The System assigns him the “Desert Mirage” Quest to investigate the western threat.

Taekyung travels overland, choosing to check Gansu before continuing toward Qinghai. Dark Heaven’s destination is uncertain, and its Moving Formations make possible routes difficult to predict. At the Shaanxi–Gansu border, his group encounters a large Zhongnan Sect party led by Sect Leader Gong Iljung. Taekyung and Jeok Cheongang confront Song Il and Hwangbo Eom over Zhongnan’s delayed and reduced reinforcements to Shanxi, suspecting the two elders have been holding their party back. Jeok, restored to a middle-aged appearance, pointedly calls out the delay.

Meanwhile, the Jin Family’s larger force remains behind to follow Taekyung, and Mukyung promises to catch up. Elsewhere, the Zhuge Clan reports that it has completed its assignments, marking the start of an all-out war.

## Continuity

- Taekyung and the Fire Dragon Pavilion are at the Shaanxi–Gansu border after three days of overland travel. They plan to check Gansu before proceeding to Qinghai.
- Taekyung controls four jiazi of internal energy after assimilating the Heavenly Power Demon’s and Peng Cheolhu’s energy.
- The “Desert Mirage” Quest to investigate the western threat remains unresolved.
- Dark Heaven’s army is advancing beyond the desert, but its destination and objective are unknown. Qinghai, Gansu, and Tibet remain possible routes into the Central Plains.
- Dark Heaven’s Moving Formations could transport forces into the Central Plains; their number and locations are unknown. The Demon-Sealing Formation may neutralize them, but doing so would take time and manpower.
- Sama Pyo’s Black Dragon Demon Gate in Gansu may be threatened by Dark Heaven’s advance through Xinjiang.
- The Nanman Beast Palace is defending Sichuan alongside Qingcheng and Emei.
- Zhongnan’s party, led by Gong Iljung and including Song Il and Hwangbo Eom, is near the Shaanxi–Gansu border. Zhongnan sent only three hundred of its reported thousand reinforcements to Shanxi, arriving a day after the fighting ended. Taekyung and Jeok suspect Song and Hwangbo delayed the party; their reasons are unknown.
- Jeok Cheongang has regained a middle-aged appearance and youth.
- The Zhuge Clan has completed its assigned tasks; the all-out war is beginning.

## Translation Decisions

- Render 十萬魔徒 (십만마도) as “Hundred Thousand Demonic Disciples” in Namho’s estimate.
- Render 사막의 아지랑이 as “Desert Mirage.”
- Retain “all-out war” for 총력전.
- Render 일각 as “fifteen minutes.”
- Translate 대 종남파 literally as “The Great Zhongnan Sect,” preserving Taekyung’s suspicion that the banner contains a typo.
- Preserve the greeting gag: Taekyung’s mistaken phrase wishes the Daoists would be split in two, followed by Hwaran’s correct, healthy-greeting version.

## Durable state

{
  "active_continuity": [
    "Taekyung’s group has reached the Shaanxi–Gansu border after three days overland and plans to check Gansu before continuing to Qinghai.",
    "Dark Heaven’s army is reportedly advancing beyond the desert, but its destination is unknown; Qinghai, Gansu, and Tibet are possible routes into the Central Plains.",
    "Dark Heaven’s Moving Formations could transport forces into the Central Plains; their number and locations are unknown, and neutralizing them would require time and manpower.",
    "The Demon-Sealing Formation may be able to neutralize Moving Formations; Zhuge Feng’s clan used it to contain the rift at Dongting Lake.",
    "Sama Pyo’s Black Dragon Demon Gate in Gansu may be threatened by Dark Heaven’s advance through Xinjiang.",
    "The Nanman Beast Palace accepted the Murim Alliance’s request and is defending Sichuan alongside the still-intact Qingcheng and Emei.",
    "Zhongnan’s party, led by Sect Leader Gong Iljung and including Song Il and Hwangbo Eom, is traveling near the Shaanxi–Gansu border; Taekyung and Jeok suspect the two elders have delayed the group.",
    "Jeok Cheongang has regained a middle-aged appearance and youth.",
    "Zhongnan sent only three hundred of its reported thousand reinforcements to Shanxi, and they arrived a day after the fighting ended."
  ],
  "continuity_sources": [
    998,
    999
  ],
  "open_questions": [
    "Where will Dark Heaven’s advancing army strike, and what is its objective?",
    "What caused the System malfunction, and is it connected to the Lord of Heaven?",
    "Why did Sama Pyo’s father order him to return immediately?",
    "Why have Song Il and Hwangbo Eom been holding Zhongnan’s party back?"
  ],
  "safe_through": 999,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 995

# Chapter 995

Some conversations don’t need many words.

The more urgent the matter, the less they need.

That was certainly true of my conversation today with Jin Wikyung, who’d suddenly come to my room.

It had lasted less than fifteen minutes.

But what we’d discussed had been as heavy as a massive stone, and as soon as Jin Wikyung left, I called everyone together.

The people who could help me bear the immense weight of that conversation.

Creak.

“Well, I’ll be damned. You live long enough, and you see everything. Who’d have thought a bunch of martial-world lowlifes like us would live to see the face of the Marquis of Shangshan?”

Namho tossed out a silly joke the moment the door opened, and I couldn’t help but chuckle.

For two reasons.

First, because seeing Namho again—or rather, seeing all of them again—felt like a relief. It was almost as if I hadn’t seen them in ages.

Second, because Namho was sitting astride Taishan’s shoulders as though that were the most natural thing in the world. It was ridiculous.

“What are you doing?”

“What does it look like? I’m sitting.”

“I can see that. I’m asking why you’re sitting there of all places.”

“That’s easy to answer. It’s incredibly comfortable. This guy’s a real find.”

Namho smiled with the satisfaction of a great inventor who’d discovered something that could change the world, then patted Taishan on the crown of his head.

“What are you waiting for? Get inside.”

Taishan stood blankly in the open doorway, then glanced off into the distance before answering.

“Taishan. Feet won’t move. Must be hungry.”

“What the hell are you talking about? The jerky you stuffed into your mouth barely fifteen minutes ago amounted to a whole calf.”

“……”

Apparently, he ran on a pay-as-you-go plan.

And one with terrible mileage, at that.

“Don’t remember. Hungry.”

“Good grief. You’re a gluttonous demon if I ever saw one…”

With a deep sigh, Namho pulled a piece of taffy from his sleeve and waved it in front of Taishan’s eyes.

“There. Happy now?”

In that instant, Taishan’s eyes narrowed to razor-sharp slits.

“Just one?”

“Damn it. I’ll give you another as soon as we get back.”

“Three.”

“You little bandit. No way. Two. That’s my final offer, so think carefully before you decide.”

Just as Taishan’s eyes began to waver, a voice sounded from behind his huge body, putting an end to his hesitation.

“Move. Right now. Otherwise, I’ll personally stab each of you twice.”

“……!”

“……!”

“What, two knives each still isn’t enough? Should I make it three?”

Her voice was quiet and composed.

Maybe that was why the warning felt even more dangerous. Taishan swallowed hard, then hurried into the room.

He even snatched the taffy Namho had been waving in front of him, displaying a thoroughness I could only admire.

Only then was the entrance clear. Ju Hwaran, who’d brought the rush-hour traffic to an abrupt stop, strode toward me.

Her voice had grown thick with emotion, as if nothing had happened.

“Young Master Jin! No, Benefactor! No, Pavilion Master!”

“……”

I was pretty sure I’d asked her several times to pick just one.

The situation was funny, but Ju Hwaran’s sudden change in attitude also caught me off guard. While I floundered, she even teared up.

“I’m sorry I arrived so late during the last battle. You must’ve had such a hard time.”

Over Ju Hwaran’s shoulder, Sama Pyo stood like an invisible man and muttered to himself.

“I’d guess the enemies had a harder time.”

Song Ilseom, arms crossed and his willow-leaf saber tucked against his chest as always, nodded.

“From the signs of the fight, he was a monster. None of them stood a chance.”

Jaw clenched, Ju Hwaran ignored the voices behind her and continued.

“Were you hurt? Are you all right now?”

Sama Pyo and Song Ilseom at least had some sense.

They both slipped away at the right moment instead of butting in without a clue like Hyuk Mujin was about to.

“No, Young Lady Ju. Why are you asking about the condition of someone who went through Bone Transformation just the other day—”

A chill settled over the room.

I didn’t know what expression Ju Hwaran had on her face as she slowly turned around, but I saw terror spread across Hyuk Mujin’s face as his voice trailed off. I decided I’d go on living without ever finding out.

“Mujin, shut your blabbering mouth. Young Lady Ju, I’m fine. Completely fine, so there’s no need to worry. And Taishan, I need to talk about something important, so hurry up and swallow the taffy in your mouth—oh, you already finished it. Did you chew it, or did you drink it?”

After Taishan’s startling magic trick, which made me wonder if taffy came in liquid form, I finished sorting out the traffic. Namho gave me a dubious look.

“Something important, huh? For some reason, I already have a very bad feeling about this… Am I just being an old worrywart?”

“If that were all, how nice that would be.”

I wasn’t the one who said it.

The last guest in the room stepped inside. Jeok Cheongang gave me a nod.

“Tell everyone what’s happening beyond Shanxi Province.”

His sunken gaze told me he’d heard the same news I had.

By now, the room was full. I silently looked around at everyone, one by one, then finally parted my tightly shut lips.

“Something’s happening in the west.”

“The west? Where exactly in the west…?”

As expected, Namho was the first to react. He furrowed his brow as he began to ask, then his narrow eyes suddenly widened.

“D-Don’t tell me…”

“Yes. It’s where you’re thinking.”

I nodded, then spoke in a heavy voice.

The far western edge, the birthplace of the Heavenly Demon Divine Cult—called the Demonic Cult in the Central Plains—and now the home base of Dark Heaven. That accursed land.

“Xinjiang.”

“……!”

“……!”

A massive shock swept through the room like an invisible wave.



* * *



When did the other world within the world—known as Murim—and the martial artists who lived in it first come into being?

No one knew for sure.

But according to oral traditions passed down from one person to another, and the few lines left in records from the distant past, many claimed that Shaolin Temple in Henan had set this long history of Murim in motion. Before long, that claim had become accepted as fact.

Of course, what Jeok Cheongang had told me while I was undergoing grueling training on Mount Jiuhua had been different.

*“History is always shaped and pieced together in the end. People believe whatever they want to believe—whatever suits their taste.”*

Back then, Jeok Cheongang had been suffering from the infirmities of old age, and he’d begun reminiscing about the past more often. Or, to be more accurate, I’d half-begged him to.

I thought I’d once read somewhere that bringing up and revisiting old memories whenever you had the time could slow the progression of age-related illness.

And Jeok Cheongang’s vast knowledge included hidden histories of Murim that weren’t widely known.

*“Light and darkness are inseparable companions. It’s absurd enough to claim martial arts were born in Shaolin, where people who want to become Buddhas are packed together. But do you really think no one tried to use that great power for evil?”*

*“Then what you’re saying is…”*

*“That’s right. According to records left by the founders of our sect, the Demonic Cult came into being the same way. We don’t know the exact date, but it was probably around the same time as Shaolin Temple.”*

The world of Murim, a mountain of sabers and a forest of swords, had formed in an age of such chaos that it could hardly have happened any other way.

The Shaolin monks learned martial arts as a means of protecting others. But when someone else encountered that astonishing power, they learned martial arts as a means of conquering the world.

*“People of every stripe must’ve gathered from all directions, in droves. They used martial arts to wield such mysterious power that they hardly seemed human. Just imagine how astonished everyone must’ve been.”*

There must’ve been only a few dozen at first.

In a world that remained dark even beneath the sun, they’d encountered a power like a great light. Before long, they became followers and spread in every direction.

They told others of the astonishing sight they’d witnessed with their own eyes, then grabbed the sleeves of those who refused to believe them and led them there.

To the man with that unbelievable power. To the leader who would protect them in this wretched age of chaos.

The followers who gathered around him grew from hundreds to thousands, then finally to a hundred thousand. At last, their leader declared himself the Cult Leader and a divine man sent by Heaven.

*“That was the beginning of the Heavenly Demon and the Demonic Cult.”*

Jeok Cheongang had also said that they probably hadn’t called themselves the Heavenly Demon or the Demonic Cult from the very beginning.

What mattered was that the first Heavenly Demon had never managed to conquer the world. Instead, he and his followers had settled in the desert on the western frontier.

For nearly a thousand years after that, they sometimes turned their blades against one another. After several splits and reunifications, they eventually brought about the Great Faction War, a calamity on an enormous scale.

Throughout those long years, the scorching sands ruled absolutely by Fiends became a wasteland that even Murim of the Central Plains couldn’t hope to challenge.

And they remained so even now, with a new shadow called Dark Heaven cast across the desert.

“And now something unprecedented is happening in Xinjiang?”

After the short account came a long silence.

Namho’s question broke the quiet. I nodded.

“That’s what I heard.”

“Where did the information come from?”

“Where do you think?”

I pointed upward with a finger, and Namho murmured as if letting out a sigh.

“The Murim Alliance… No, the Hidden Shadow Pavilion.”

“I heard thirty-odd elite agents were killed. Their contact was cut off after the first and last messenger eagle they sent.”

“Damn it. Then there’s no room left for doubt. What’s the estimated number of enemies?”

“That…”

For once, I couldn’t bring myself to continue easily. Namho groaned at the sight of me.

“I see. The return of the Hundred Thousand Demonic Disciples.”

“There may be even more. At least, that’s what the information I received suggests.”

And what mattered more was that they were far stronger and more horrifying than the Demonic Cult’s followers had been fifty years ago.

The desert no longer belonged to the Demonic Cult. It belonged to Dark Heaven.

They weren’t merely the successors of the Demonic Cult under a different name. They were a new group of followers, ruled by a power incomparably stronger and more dangerous.

*Could this be why Logout was suddenly blocked?*

The thought crossed my mind, but I soon shook my head.

No. That was wrong.

The Quest hadn’t appeared yet. Because I hadn’t chosen yet.

And now was the moment to make that choice.

“From this moment on, we’re heading west.”

Ding.

An alert rang out, announcing a new Quest.
## Chapter artifact 996

# Chapter 996

Sometimes, I wonder.

Maybe the real benefit of circulating your qi isn’t getting stronger by storing up internal energy, but calming your mind.

Kwoooosh.

I had no idea how much time had passed.

I could only surrender myself to the swift, powerful current.

At last, the wave of internal energy swept through hundreds of acupoints—including the Eight Extraordinary Meridians—and I gathered it all in. I opened my eyes amid a breathless silence.

Ding.

A clear chime rang out right on cue.

As the alert confirmed that I’d successfully finished circulating my qi, I calmly surveyed the energy within me.

*The peak.*

The word came to mind without hesitation, and there wasn’t a shred of exaggeration in that conviction.

That’s right.

I’m stronger now than I’ve ever been.

I’d fully absorbed not only the energy of the Heavenly Power Demon, which had coexisted inside me for quite some time without being completely assimilated, but also the energy of the Thunderbolt Saber King.

*Four jiazi.*

That was an incredible amount of internal energy. Even more so when you considered my age and how long I’d been practicing martial arts.

A greenhorn who’d just entered Murim might wonder why I’d gained only one jiazi after receiving Transmitting Internal Energy Across the Body from two old masters. But martial artists who’d reached a certain realm knew better.

Martial arts weren’t as simple as one plus one.

No matter how much internal energy you possessed, if its essence was impure, you couldn’t draw out even half of it. And you couldn’t properly control it, either.

In that sense, the four jiazi of internal energy, reborn through their complete fusion, was pure power I could wield with absolute control.

*If the Heavenly Power Demon and the Thunderbolt Saber King had been in their usual condition when they transferred their energy, I might’ve grown even stronger, but…*

Wanting more would be greedy.

Even I, with the mysterious divine strength known as the System, had risked my life twice while undergoing Transmitting Internal Energy Across the Body.

And yet, I still felt a little disappointed. The reason was the reality I’d faced the moment I finished circulating my qi.

> **System**
>
> **Quest**
>
> Desert Mirage
>
> You have learned of strange developments taking place in Xinjiang, the far western edge of your world.
>
> A cursed land, long separated from the Central Plains.
>
> A group is crossing the scorching desert, where nothing exists but hot sand and the blazing sun, and heading toward the center of the world. But their true nature remains hidden behind a dense mirage.
>
> Please remember. Never forget.
>
> The world—and the heavens—are changing.
>
> Nothing is set in stone.
>
> The countless enemies drawing near from far away, even now, may be no more than a brief spark.
>
> Or they may become a hellfire that brings the world to ruin.
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Head west (Incomplete)
>
> **Reward:** A large amount of EXP and Fame
>
> Follow-up Quests depending on your choice
>
> **Failure:** ???

It was the Quest window I’d already read dozens of times, after sending the Fire Dragon Pavilion members away in preparation for the perilous journey ahead.

I gestured, and it vanished from the corner of my vision. Then, suddenly, I remembered the conversation I’d had with Jin Wikyung two hours earlier.

“If Dark Heaven crosses Xinjiang and cuts through the desert, as the information from the Hidden Shadow Pavilion suggests, where would it focus its attack?”

“The Murim Alliance is considering three possibilities at once. They might advance through Tibet, which could be considered part of the Outer Lands. They might target Gansu Province, where the Kongtong Sect and Black Dragon Demon Gate are holding their ground. But the most dangerous place is probably…”

“Qinghai. The Kunlun Sect, then.”

“That’s right. Kunlun Mountain is a natural fortress in its own right, but for Dark Heaven, which is targeting the Central Plains, it’s also the first obstacle they’ll have to overcome. They’ll never leave Qinghai alone.”

Shanxi Province was a remote backwater, but it was nothing compared to Qinghai, at the westernmost edge of the Central Plains.

And in a high-altitude region full of terrain so rugged it was downright brutal, producing abundant supplies was difficult. Commerce and industry hadn’t developed much, either, thanks to the Demonic Cult’s influence over the desert for so many years.

Merchants would risk their lives for profit, but no one could cross a desert expecting certain death.

But even setting all that aside, Qinghai was an indispensable strategic stronghold from a military standpoint.

A place one side absolutely had to defend—and the other had to trample underfoot to get past.

*Dark Heaven has enough strength to do it. Besides, Qinghai has already been trampled once before.*

Over fifty years ago, the hundred thousand demonic soldiers led by the Heavenly Demon defeated the Kunlun Sect and took control of Qinghai. That was the beginning of the Great Faction War.

And now—

That brutal history of bloodshed was about to repeat itself after all these long years.

*Qinghai. Qinghai Province…*

I gazed out the window, my eyes sinking into shadow.

Beyond the latticed window, hundreds of torches swayed in the darkness that had settled without my noticing.

The sun had set and night had come, but everyone in the Jin Family of Taiyuan was still awake.

No, it wouldn’t be just the Jin Family.

I could picture the whole of Murim in the Central Plains—including the Nine Sects and One Gang and the Five Great Families—boiling like a cauldron over hot coals.

*It’s coming. The all-out war we can’t avoid.*

The drums of war had been pounding across the land for a long time. But the countless enemies even now crossing the desert toward somewhere in the west weighed on my heart more heavily than ever.

Those who wanted to defend—and those who wanted to take.

A colossal battle, one that would make everything we’d faced until now seem insignificant, awaited everyone in the west. Each side would stake its fate on it.

*The fate of this world might be decided by a single battle, soon to come.*

Maybe that was why.

Why the System had suddenly malfunctioned.

Why this absolute law, which had never strayed from its set path no matter the circumstances, was beginning to waver.

Then what had seized my ankle as I tried to leave this place for a little while—just a little while?

The System? Or…

*Dark Heaven. No—more precisely, the Lord of Heaven.*

I couldn’t be sure yet, but there was at least one thing I could guess.

Far away in the west.

Somewhere in that place hidden by the pitch-black darkness, the answer to this mystery was waiting.

Or perhaps death.

*Damn it.*

Nothing ever goes smoothly.

I gave a bitter smile to myself, then spoke to someone waiting beyond the firmly shut door.

“We leave in exactly fifteen minutes.”

“As you command.”

I heard Hyuk Mujin’s footsteps receding after his unusually forceful reply. As I stood, I suddenly sensed something strange and turned around.

Tap. Tap-tap.

Something damp and white drifted into the room on the wind.

I looked at the unwelcome visitor that had arrived months ahead of schedule—the snowflakes slowly piling up—and remembered a line from the Quest window.

*The world—and the heavens—are being turned upside down.*

I prayed silently that, at least, those words weren’t a malfunction.

The world I could feel at this very moment—the sky pouring down those pure white snowflakes—seemed to have finished changing already.



* * *



The light in the room was dim.

It was already pitch-black outside, and the wind seeping through the crack in the door made the candle flame flicker precariously.

Yet even under such poor conditions, the person reading the letter in their hand didn’t so much as twitch an eyebrow.

Years of grueling training since childhood had honed his eyesight. Even in the faint light, which looked ready to go out at any moment, he could clearly make out the tiny writing on the letter.

And as he stared at a letter he’d already read several times, some of the words reflected in his eyes, lit by the wavering flame.

**Return immediately.**

The handwriting was sharp and pointed as a blade, and beside it was a familiar official seal.

Guessing who had sent the letter, he muttered softly.

“You haven’t changed, have you?”

His voice echoed hollowly, low and subdued.

The letter wasn’t a request or a favor. It was an order.

It had always been that way, and everyone took it for granted. But he could never quite get used to it.

After all, the person who’d written the dry, lifeless letter as though a master were ordering a servant was his own flesh and blood.

No—more precisely, it was the person who’d given him his blood.

“…Father.”

The word came after a brief hesitation.

Quietly repeating the unfamiliar title, he was suddenly reminded of the past.

Of a childhood that had been rigid and cold, where there’d been no dreams, only purpose—and of the pair of eyes that had watched over him sternly.

Creepy as it was, those eyes still seemed to be watching everything he did.

Perhaps that was why he didn’t notice the presence approaching outside the door.

Thump.

“Ugh!”

A sudden noise overlapped with a cry of pain. Then a sharp shout rang out, breaking the silence.

“You idiot! Higher! I said you need to think about height!”

“Taishan not stupid. Namho stupid. How can’t he dodge when he sees it?”

“You little punk! Is this because I didn’t give you taffy?”

Familiar voices pierced his ears.

Guessing the intruders’ identities, he tossed the letter in his hand into the lamp.

Fwoosh. Crackle.

The small piece of paper, less than half the size of his palm and soaked in oil to keep it from getting wet, blazed up in an instant.

And at that moment, the firmly shut door flew wide open.

It would be more accurate to say it had been smashed to pieces.

“My lord! Are you ready?”

*Bam!*

As his booming shout rang out, splinters of the shattered door flew in every direction. But he—or rather, Sama Pyo—didn’t look the least bit startled. He grabbed the travel bag beside him and stood.

“Of course. What about you, Taishan?”

“Taishan ready! Perfect!”

Namho, who’d been perched on Taishan’s shoulders, spat out pieces of wood and added, “Of course it’s perfect. The jerky that guy packed would be enough to bring five cows back to life.”

“That sounds like a reasonable amount for him to pack. Not too much.”

“…It’s a wonder the Black Dragon Demon Gate hasn’t gone bankrupt. He’s a gluttonous demon through and through.”

Sama Pyo gave a short laugh. He already knew that the old Hidden Shadow Pavilion agent, who hadn’t seemed all that pleasant at first, had a warm heart and a fair amount of affection for others.

“More importantly, what were you doing here alone?”

“I stopped by for a moment. There was something I needed to take care of before we left.”

“Is that so?”

Namho glanced over Sama Pyo’s shoulder, but the letter, soaked through with oil, had already burned away without a trace.

“Then put that fire out before you come out. The weather’s already fucking awful. Unless you’re planning to burn down someone else’s little house.”

“Oh, I almost forgot.”

Sama Pyo answered gently, waved a hand, and snuffed out the candle. Then, as though nothing had happened, he headed for the door.

“Let’s go. Everyone must be waiting.”

Namho watched Sama Pyo’s back with a curious look.

But only for a moment.

Thump.

“Ugh!”

Namho let out a cry after hitting his forehead on the eaves again, then grabbed Taishan by the hair and yanked.
## Chapter artifact 997

# Chapter 997

Fifteen minutes.

It was too short a time to properly savor even a cup of tea, but plenty for the Fire Dragon Pavilion members, myself included, to finish all our preparations.

And to prepare a send-off no one else had expected.

Whoooosh. Fwoosh.

Countless torches swayed.

Neither the darkness that had fallen early nor the snowstorm now whipping fiercely through the air could put out those enormous flames.

Crunch.

Footprints marked the snow-covered ground.

Leaving behind hundreds of people standing like iron towers, each holding a torch in one hand, Jin Wikyung stepped forward alone. Then he suddenly spoke.

“The prodigal son finally came home, only to leave again.”

His voice was stern, as if passing judgment on a criminal, but the word *prodigal* drew quiet laughter from here and there.

By now, everyone in the Jin Family of Taiyuan knew it. Not just them, but all of Shanxi Province—or rather, the whole world.

The name Jin Taekyung was no longer a stain on his family or a dissolute rogue.

Ever since that day, more than a year ago, when I defeated the traitors—including the Head Elder—and restored peace, I had become their pride and their symbol.

“I never wanted to see you off again.”

I shrugged at Jin Wikyung, who muttered the words with a bitter expression.

“What can I do? Guess it’s fate.”

“What came from the Murim Alliance was information, not an order. If you change your mind, even now, you can stay with the family and move out with everyone.”

“That sounds nice. But I’ll go ahead and wait for you. I hate being late.”

Jin Wikyung let out a small groan at my polite refusal.

He was practically the Family Head of the Jin Family of Taiyuan, so he couldn’t just move at a moment’s notice. He had to lead not only the family members, but countless martial artists from Shanxi—and the nomads they had subdued, too.

It was much the same for the Bow Saint and the Embroidered Uniform Guard, who still hadn’t returned after rooting out the Murong Family’s threat.

A massive army and a small advance unit.

It was obvious which would be slower and which would be faster. And that considerable gap in timing might become the flap of a butterfly’s wings somewhere far away and change a great many things.

Of course, even knowing that didn’t make worrying about family any easier.

“It will be dangerous. More than ever before.”

At the sight of Jin Wikyung’s worried expression, the journey I’d taken so far suddenly flashed through my mind.

Dangerous, huh?

Yeah, of course it would be.

But…

“It’s always been the same. There hasn’t been a single exception, and there won’t be one from here on out.”

Looking back, there had never been a time when I wasn’t in danger.

There had never been a moment that wasn’t hard, either.

When I first opened my eyes, I was a tadpole. I struggled to survive, and became a frog.

Then I threw myself into one leap after another until I escaped the well. Beyond it, a world immeasurably wider and more treacherous than the well had been waiting for me.

And at every fork in the road that blocked my way, I had always made a choice.

“It’s the road I chose. I don’t know when I’ll be able to stop, but… I have to run. All the way to the end.”

Jin Wikyung was silent for a moment at my utterly matter-of-fact answer. Then he suddenly let out a rueful laugh.

“You’ve grown up. Before I knew it, you’d grown so much I hardly recognized you.”

Looking at Jin Wikyung, whose imposing build was enough to make me wonder if he had Hebei Peng blood, I smiled back.

“I’m still not as big as you, hyung.”

“Hyung. That sounds especially good today. Maybe because it’s been so long since you called me that.”

It wasn’t just because I’d spent so long wandering outside. I’d simply needed a little more time to truly accept the new family I’d found in this unfamiliar world.

Even if the body’s true owner wasn’t me.

*Right. The real owner—the Jin Family’s Third Young Master—is someone else.*

The thought weighed on me, but the familiar face that appeared beside Jin Wikyung a moment later washed it away.

“Oh, would you look at that. Isn’t that our family’s second son?”

At my exaggeratedly wide-eyed expression, Jin Mukyung shook his head.

“Here we go again.”

“What? Did I say anything wrong? You are the second son.”

“You conveniently left out the ‘hyung’ that’s supposed to come after it.”

“I’ll add it if you want. Beat me first.”

“…You shameless bastard.”

“What, you don’t think you can?”

Jin Mukyung stared at me in disbelief, then let out a quiet laugh.

“Of course I can. Just wait. I’ll catch up soon.”

“Confidence is good, but just know it won’t be easy.”

“I know. But you’d better remember one thing, too.”

“What?”

“Until I catch up, don’t let anyone else take you down. Ever.”

“……!”

For a moment, I couldn’t speak. Seeing me just blink in silence, Jin Mukyung seemed to realize he’d said something embarrassing. After hesitating briefly, he suddenly thrust out his fist.

Tap.

It was a slow, forceful punch. His fist touched my chest.

Even with the snowstorm raging all around us, warmth spread from the spot where Jin Mukyung’s fist had touched before pulling away.

“Go ahead. This time, I won’t be late. I promise.”

Maybe he was embarrassed to show a side of himself he normally didn’t. Or maybe some emotion had surged up in him.

Whatever the reason, Jin Mukyung turned away after those words. In the direction he headed, more familiar faces were waiting for me.

Wipeng, who had come to see me off despite his grievous injuries.

Lee Seowol, forcing a smile despite the death of her uncle, Cheol Mubaek—the Tiger of Mount Heng—who had been her staunchest guardian and almost another father to her.

The Jin Family of Taiyuan’s senior members, who had served Jin Wikyung with unwavering loyalty and helped him raise the once-declining family into one of the Five Great Families.

The scouts who had once crossed life and death alongside me. The young brother and sister who had grown so much while I was away from the Jin Family of Taiyuan. And countless family retainers whose faces were more familiar than their names.

Every one of them was looking at me.

As I met each person’s eyes, they smiled brightly, nodded quietly, and stamped their feet with such overwhelming emotion that their hearts seemed ready to burst.

Hard and strong. Without anyone having to lead, they stamped the ground, now blanketed in white, and drew their weapons like lightning.

Clang-clang-clang-clang!

Between the hundreds of swaying torches, a dazzling wave of steel lit up the surroundings—nothing like the snowstorm pouring down overhead. A wildfire-like aura rose, heating the air.

Thud. Thud. Thoom!

The ground shook beneath their vigorous footfalls. My heart, which had gradually settled into a steady rhythm to match them, began to pound. Just then, Jin Wikyung’s quiet voice slipped into my ear.

“Do you see it?”

I didn’t answer.

No—I couldn’t.

I could only listen to Jin Wikyung’s voice echoing around me, my chest trembling deep inside.

“You are our pride.”

“……!”

“Go. Down the road you chose.”

Go forward without hesitation, with all your might.

Hearing the rest of his words swallowed by the fierce snowstorm, I finally moved my feet.

Crunch.

Beneath a roof of steel, crisscrossed countless times, new footprints began to mark the white snow.

* * *

The untimely snowstorm wasn’t confined to Shanxi Province.

The young man had remained silent for a long time, even after his expected guest arrived. Watching the snow whip past the window, he suddenly spoke.

“Long ago—very long ago—someone said something like that to me.”

Across the rough table, the guest sat with perfect composure despite a full shichen—about two hours—of silence. He answered,

“You’ve made me curious already. Who was he?”

To anyone who didn’t know them, it would have seemed like a strange sight.

Unlike the young man who owned the room, his guest was an old man who looked to be about eighty.

But the scars visible beneath his graying white hair testified to a life shrouded in secrecy. The young man sitting opposite him was no different.

“You know him, too. I can tell you now, if you want.”

He spoke to the older man as an elder would to a junior, as though it were the most natural thing in the world.

The Thousand-Faced Fox, Song Ho, lightly declined the Sword Saint Mae Jonghak’s offer.

“I’ll try to guess after I hear it. I prefer figuring things out for myself to being given the answer.”

“Wouldn’t most people choose the former?”

“As Chief of the Hidden Shadow Pavilion, shouldn’t I at least be able to do this much?”

“That’s a fair point.”

“So, what did that someone say to the Alliance Leader?”

Still gazing out the window, Mae Jonghak answered.

“He told me to protect it. The place where I stood, the convictions I held in my heart, and the world.”

“……!”

“He told me to remain here, unchanged, even if one day he disappeared. Of course, at the time, it was just something he said in passing, so I didn’t think much of it. That’s all.”

The Thousand-Faced Fox let out a breath he’d been holding.

“I think I know who it was.”

“You do?”

“Yes. As it happens, I believe I heard something similar myself.”

“If he knew, he’d be pleased. You didn’t take his words lightly. You’ve kept the Hidden Shadow Pavilion’s intelligence network going all this time.”

The Thousand-Faced Fox nodded without a word.

He certainly would have been pleased. Maybe he would even have clapped his hands and burst out laughing.

In Song Ho’s memories, the Martial God seemed to carry every worry in the world, yet at times he could be as innocent as a child.

“There’s something I’d like to ask you.”

“Go ahead, Alliance Leader.”

The Thousand-Faced Fox tensed without meaning to.

He worried that the Number One Sword Under Heaven, the man now the new symbol of the Central Plains Murim in the Martial God’s place, might waver at the most crucial moment.

But Mae Jonghak’s next words immediately swept those fears away.

“When this war is over, what are you going to do?”

“Pardon?”

“No, it’s nothing. I just suddenly started worrying. For all the work you do, you hardly get paid. Should I give you a raise now? How about doubling your salary?”

“……!”

“Hmm. Or tripling it? Then you wouldn’t have to worry about retirement.”

The Thousand-Faced Fox stared blankly at Mae Jonghak, frozen like a statue. Then he suddenly burst into a hearty laugh.

When he’d finished laughing, he answered,

“Don’t worry about my retirement. If I need to, I can always siphon some money off to the side.”

“Oh. So you already have a plan.”

“Of course.”

“But let’s keep this conversation between the two of us. If our friends outside that door find out, they might give us a hard time. Right?”

Mae Jonghak stood without waiting for an answer.

A current of qi flowed through the air and swung open the firmly shut door. Beyond it sat dozens of people around a massive table.

“I’ll say this up front: as long as the amount is reasonable, I’m willing to turn a blind eye to whatever the Chief of the Hidden Shadow Pavilion does.”

At the first playful remark from a middle-aged man, Mae Jonghak nodded with satisfaction.

“Clever, as always. You know what to say at the right time.”

“Not at all.”

“Now then, did you complete your mission safely, Family Head Zhuge?”

The middle-aged man, Zhuge Feng, the Crouching Dragon Guest, waved his tattered feather fan.

“Can you see it?”

“Quite clearly.”

“These are the marks of my suffering. I thought I was going to die.”

“Which means…”

“The Zhuge Clan has completed every task assigned to it.”

Exclamations rose from all around the room. Everyone present knew what mission Zhuge Feng had been given, and how important it was.

And it meant one thing.

All preparations were complete. A new phase was beginning.

“Well, then. Everyone’s going to be busy from here on out.”

The opening act of an all-out war had begun.
## Chapter artifact 998

# Chapter 998

As Jin Wikyung had already said, the most likely place for a major battle with Dark Heaven was Qinghai, where the Kunlun Sect was located.

It was a strategic foothold the enemy would have to take before advancing into the Central Plains—and one the orthodox Murim would have to defend with their lives.

And that was exactly why I could answer Hyuk Mujin’s question about how we would get to Qinghai without a moment’s hesitation.

“We run. Fucking hard.”

“I know that much, of course. But what I wanted to ask was…”

“You mean, running fucking hard is fine, but how long do we keep it up?”

“Ah, Captain. You really do know exactly what I’m thinking.”

“Keep going.”

“…Excuse me?”

“Keep going. All the way.”

“Wait, all the way to Qinghai?”

I asked as I kept the reins tight, urging my horse onward at full speed.

“Otherwise?”

“I think taking the water route would be better. We can travel overland as you said, then follow a tributary of the Yangtze from Shaanxi straight to Qinghai. It’d save us about half a day and take a lot less effort.”

At first glance, it was a pretty reasonable suggestion.

Even if it only saved half a day, we’d still get there sooner and conserve our Stamina before an important battle.

And the Yangtze River Channel League, the nationwide gangsters of the river with a long history and tradition, was part of the Murim Alliance. If we were lucky, we might even be able to hijack a swift ship… I mean, borrow one.

Or at the very least, a Great Nation military vessel.

But I immediately shook my head.

“The land route is better.”

“Why? Do you get seasick?”

“……”

“Even if you do, just bear with it. I’ll pat your back for you.”

Was this bastard looking down on a Supreme Peak master?

And I wasn’t some newly minted Supreme Peak master, either.

I’d reached the pinnacle of martial arts and even completed Bone Transformation. I was a superhuman among superhumans.

I could ride a Disco Pang Pang at Wolmido and still feel perfectly steady. And this guy was talking about seasickness?

I stared at Hyuk Mujin in disbelief, momentarily at a loss for words. Just then, a fierce gust of wind swept toward the back of his head.

Whoosh—smack!

“Gah!”

It was the sort of impact that felt satisfying just to hear. Jeok Cheongang, who had expertly smacked the back of Hyuk Mujin’s head, clicked his tongue.

He was traveling by stepping on the branches that stretched endlessly along either side of the road, because he found the saddle uncomfortable.

“You stupid fool. Why do you have to talk so much? If your superior tells you to do something, you do it.”

If anyone but me had smacked Hyuk Mujin on the back of the head, he’d have been glaring daggers. But when that someone was the Fire King, Jeok Cheongang, it was a different story.

Hyuk Mujin gingerly rubbed the back of his aching head, glancing around before speaking up.

“I was just making a better suggestion. Why are you doing this to me?”

“A better suggestion? You really think so?”

“Wasn’t it…?”

“I’ll admit it was a fairly plausible suggestion. But you overlooked one very important fact.”

Before Hyuk Mujin could answer, Jeok Cheongang’s low voice carried through the wind.

“Dark Heaven. Whether those thoroughly devious bastards are truly targeting Qinghai.”

“……!”

“We know nothing for certain yet. No one knows where Dark Heaven’s army, said to be marching beyond the desert, is headed. Qinghai isn’t the only route into the Central Plains.”

I nodded in agreement with Jeok Cheongang’s assessment of the situation.

That was right.

There wasn’t just one route. There were three, maybe more.

Qinghai, Gansu, and even Tibet, beyond the borderlands and counted among the Outer Lands.

Qinghai was likely to be the main target because of its strategic importance, but Gansu and Tibet were also entirely possible targets for an invasion.

And besides…

*They have a Warp Gate—or rather, a Moving Formation.*

The Moving Formation gave the enemy more options, while serving as a painfully sharp dagger aimed at our backs.

They could send as many as a thousand people—at least, that was the number we’d confirmed so far—to somewhere in the Central Plains through a Moving Formation. How could we take that lightly?

Of course, it wasn’t impossible to deal with them.

The Zhuge Clan, known as the finest in the world at mechanisms and formations, possessed a formation called the Demon-Sealing Formation. Just as its name suggested, it could suppress and seal magical power.

When a “rift” had opened at Dongting Lake, the Zhuge Clan had managed to contain it with the Demon-Sealing Formation, led by their Family Head, Zhuge Feng. That was why the incident had been brought to an end without even greater losses.

*If they can stop a rift, they should be able to neutralize a Moving Formation, too. I’ve seen the Demon-Sealing Formation myself, so I know it works. The problem is time and manpower.*

The world was vast beyond measure.

And no one knew how many Moving Formations Dark Heaven had built somewhere in that boundless sea of sand.

Even though it had been well over half a year since we found a way to deal with the Moving Formations, several sects near Shanxi Province had still hesitated to send reinforcements, even temporarily. That alone proved the point.

Even if just one Moving Formation remained, it would be like a sharp shard of glass, digging deep into the sole of someone walking carelessly across the sand.

*That’s why we have to travel overland.*

Qinghai had been a battlefield whenever foreign invasions came over the centuries. The Murim Alliance would have prepared the best defenses it could.

Those defenses wouldn’t be so flimsy that a difference of half a day—or even a full day—could bring them down.

*Tibet should be reasonably safe, too. Even if the Potala Palace in Tibet has joined hands with Dark Heaven, the forces stationed in Sichuan should be able to hold them off.*

The Sichuan Tang Clan, which the Western Heaven Demon Lord had directly targeted, had suffered tremendous losses. But Qingcheng and Emei were still intact.

And on top of that, some unexpected guests were currently staying in Sichuan.

*The Nanman Beast Palace.*

We’d left in a hurry, with a long road still ahead of us, but I’d heard news about them from time to time.

The tropical warriors had finally left the jungle in an unprecedented mass migration. They’d readily accepted the Murim Alliance’s request and were now defending Sichuan.

“The western front will have prepared to some extent. There’s just one place that hasn’t.”

I wasn’t speaking to Hyuk Mujin alone.

After finishing my train of thought, I suddenly spoke. I looked around at the Fire Dragon Pavilion members riding alongside me, then added quietly,

“Gansu.”

“……!”

“……!”

“If Dark Heaven defies everyone’s expectations and targets Gansu, that will be the greatest battlefield of this war.”

That wasn’t an exaggeration.

Dark Heaven had always found ways to catch us off guard.

Thanks to the efforts of countless people, myself included, who’d practically shit themselves trying to stop them, their plots had been thwarted time and again. But that didn’t mean the Murim Alliance had gained the upper hand in this war.

No—in fact, it would be more accurate to say Dark Heaven had been toying with us.

*Shutting the stable door after the horse has bolted.*

If we caught the arsonist targeting the stable before the fire started, that would be our victory.

But the stable had burned every time, and countless people had been slaughtered like livestock.

As the person who’d repeatedly run around dousing the stables wherever I went, I was sick and tired of all of it.

So…

*This time, we have to stop them. No matter what.*

Before another fire started. Before there were more terrible losses.

We had to be more cautious than ever.

Like tapping a stone bridge before crossing it, I had to see the situation in Gansu with my own eyes before moving on to Qinghai.

That was the biggest reason I’d chosen the land route over the slightly faster, more comfortable water route.

*And this choice should be a lot more reassuring for him, too.*

I glanced to the side at one man.

It had been half a day since we left the Jin Family of Taiyuan, and he still hadn’t said a word. He simply held the reins in silence: Sama Pyo.

He’d always been taciturn, but lately I’d felt it getting worse.

*He can’t help it. If Dark Heaven’s army is crossing the deserts of Xinjiang right now, his family could be in danger.*

Along with the Kongtong Sect, the Black Dragon Demon Gate was one of the two powers that divided Gansu Province between them. And Sama Pyo was the Black Dragon Demon Gate’s Young Sect Leader. Of course he’d have a lot on his mind.

Especially after hearing what Jeok Cheongang and I had just said.

But I didn’t bother trying to console him.

In a situation like this, comfort was a luxury. When our eyes met, Sama Pyo gave me a slight, silent nod. I looked away and tightened my grip on the reins.

“Hyah!”

Thud-thud-thud-thud!

The grassland horses, said to have more stamina than even sweat-blood horses, galloped on without a trace of fatigue.

Night and day passed each other once more, and the moon and sun crossed paths overhead.

Then, as three days swept by like the wind, we left Shanxi Province and reached the border between Shaanxi and Gansu.

* * *

“Stop. We’ll rest for half a shichen here.”

The one who suddenly spoke and brought everyone to a halt was an old man, perhaps around sixty, with a slender build and sharply slanted eyes.

Of course, the several hundred people following behind him knew better than to judge by appearances.

Just as what they saw with their eyes wasn’t all there was, the old man had lived far longer than he looked. Only his formidable martial prowess could account for it.

Great age and formidable skill.

Of all those present, there was only one person who could refuse the orders of an old man with both.

“Why are we stopping for a rest out of nowhere? What on earth do you mean, Eldest Senior Brother?”

A half-white-haired Daoist in a clean robe hurried over, looking confused. The old man answered without a care.

“My old body is uncomfortable, and I can’t go any farther. So I thought we’d rest for half a shichen. Is there a problem?”

“Senior Brother!”

“Lower your voice, Junior Brother Sect Leader. How can you be so rude to Eldest Senior Brother?”

Someone’s voice cut in abruptly.

The half-white-haired Daoist turned toward the scolding voice and sighed.

“Why are you doing this too, Senior Brother Lee? It’s been two days since we left the main sect, and we still haven’t reached Gansu. You know that…”

“Enough.”

The man he’d called Senior Brother Lee, an old Daoist with a luxuriant white beard who looked like an immortal, lifted a hand and cut him off.

“What can we do? Our bodies have grown weak, and there’s a limit to how far we can travel. Eldest Senior Brother and I are disappointed in you, Junior Brother Sect Leader.”

“What do you mean?”

“After devoting ourselves to recuperation for so long, your two Senior Brothers have only just become able to get around again. Why are you rushing us like this?”

The half-white-haired Daoist moved his lips as if he had something to say, but he couldn’t get another word out. He turned away.

And even if he’d spoken the words on his mind, the outcome would probably have been much the same.

Because at that very moment, the sound of pounding hooves rang through the deserted forest.

Thud-thud-thud-thud!

Several grassland horses burst through the rising cloud of dust. They spotted the group halted in the middle of the forest path and began to slow.

Or rather, it was more accurate to say they’d stopped after seeing the flag rising above the group.

**The Great Zhongnan Sect.**

From atop his panting grassland horse, the young man riding in front read the characters embroidered in a single flowing stroke and muttered under his breath,

“I think there’s a typo…”
## Chapter artifact 999

# Chapter 999

When I’d just entered the workforce and started out as a Hunter, the veteran Hunters with years under their belts had a saying they repeated like a mantra.

“You never know when or where your paths might cross again. That’s what connections between people are.”

“So whenever you make or break a connection with someone, you’ve got to be careful and flexible. That way, you won’t regret it later.”

Looking back now, I don’t think I’ve ever heard advice that proved more valuable.

The only problem is that advice like that doesn’t mean a damn thing to a guy like me.

“I think there’s a typo…”

The four characters embroidered in ornate silk read **The Great Zhongnan Sect**. The moment I read them, the words slipped out before I could stop myself.

The nearest Daoist frowned.

“Friend, what did you just say?”

“Oh, nothing. Just talking to myself.”

“Talking to yourself?”

“Yeah.”

“You’re awfully casual.”

“Yeah, sir.”

The middle-aged Daoist stared at me, momentarily dumbfounded, then took a breath and finally managed to ask,

“What are you trying to do?”

“You called me your friend, so I spoke casually. Besides, you were the one who started talking casually to me.”

“You appear to be a fellow martial artist, but you’re young enough to be my junior. You really don’t hold back, do you?”

“I can get away with it. I might be young, but in martial seniority I’m an old man.”

“What… did you say?”

At this point, it was only natural for him to sense something was amiss.

My unexpected answer had thrown him off, and an invisible stir rippled through the Zhongnan Sect Disciples watching me and the Fire Dragon Pavilion members who’d suddenly appeared.

“It’s true.”

A low voice rang out as the crowd parted to either side like a wave.

I smiled warmly at the familiar faces clearly visible beyond them.

“It’s been a while. Both of you.”

I greeted them cheerfully, but neither replied.

I spoke again to the two old Daoists who’d abruptly stopped three jang away.

“May your health be… um… what comes after that?”

Hyuk Mujin answered without hesitation.

“May you be split in two.”

“May your health be split in two. That sounds a little off. Are you sure?”

“No. I’m not really sure either. I just said the first thing that came to mind.”

“Are you insane? Now I’m even more confused.”

“I’m sorry.”

“Whatever. Anybody know the right one?”

Ju Hwaran shot her hand up and quickly answered,

“May you be healthy in every way. May your health be sound in every respect.”

“Oh! As expected of Young Lady Ju. Ten points to the Griffin Yongbong Escort Bureau.”

“Hehe.”

I gave the bashfully smiling Ju Hwaran a thumbs-up, though she had no idea what I meant, then respectfully clasped my hands toward the two old Daoists.

“Anyway, yes. I hope you’ve both been split in two.”

“……!”

“……!”

The mood turned as cold as if someone had dumped a bucket of water over us.

Realizing belatedly that I’d misspoken, I let out a deep sigh.

Depending on who heard it, they might take it the wrong way—but yes, it was a slip of the tongue.

“Damn it, I got mixed up. Hyuk Mujin.”

“Yes?”

“Get down and put your head on the ground.”

“Ah, yes.”

Just then, as Hyuk Mujin performed the amazing feat of bowing his head down to his horse’s back, one of the two finally opened his tightly sealed lips.

“You haven’t changed. Still as brazen as ever.”

The first to speak was the old Daoist with a luxuriant white beard.

His snow-white beard hung down to his navel, making him look like an immortal who’d descended to the mortal world. But I already knew better.

The old Daoist before me—no, Hwangbo Eom, the Taeeul Merciless Sword—was about as far from an immortal as you could get.

*And then some. If his inner self matched his appearance even halfway, he never would’ve pulled such a shameless stunt.*

The Zhongnan Sect and the Taeeul Merciless Sword might find it unfortunate, but my memory wasn’t that of a goldfish.

They’d entrusted Ju Hwaran’s Yongbong Escort Bureau with transporting their priceless Thousand-Year Snow Ginseng, then secretly stolen it back and demanded compensation—an insurance scam meant to swallow the Bureau whole. That was the sort of thing I’d never forget as long as I lived.

Of course, the old man standing beside the Taeeul Merciless Sword, looking this way and that, wasn’t far behind when it came to having a colorful record of his own.

“Are you looking for someone?”

“……What?”

“I asked if you were looking for someone, Great Hero Song Il.”

At my amused question, the Roaring Fury Swordsman’s eyebrows twitched.

A year and several months ago, he’d tried to overturn the banquet table of the Jin Family of Taiyuan, flaunting his Supreme Peak martial prowess and his illustrious position as an Elder of the Zhongnan Sect. He’d very nearly ended up being the one everyone mourned at a funeral instead. Now he was anxiously scanning us, searching for one person.

A man who, to hell with the Zhongnan Sect or anything else, would dish out a slap across the face as a matter of course—and kick you in the shins for good measure—if he took a dislike to you.

I spoke gently to the Roaring Fury Swordsman.

“You can relax. The person you’re looking for isn’t here.”

“……!”

“Or did I get it wrong? Were you looking for someone else?”

The Roaring Fury Swordsman had kept his mouth shut, glaring at me. Now he squeezed out a voice boiling with anger.

“You dare—”

“Dare to what?”

That wasn’t me speaking.

A moment later, Jeok Cheongang dropped out of empty air, and the Roaring Fury Swordsman’s eyes went wide.

“H-How can you be here?”

“What? ‘You’?”

“N-No, that’s not what I meant.”

The Roaring Fury Swordsman stammered and stepped backward.

Jeok Cheongang’s smooth bald head now sported a bristly crop of red hair, and his face had regained the appearance of a middle-aged man.

The rumor that Jeok Cheongang had reached another extraordinary realm and regained his youth had spread far and wide. The Zhongnan Sect was no exception.

“F-Fire King Jeok Cheongang…!”

At someone’s involuntary exclamation, an invisible shock swept through the crowd.

First, they were seeing the Fire King in person after hearing about him for so long. Then they realized that the young upstart who’d suddenly appeared was none other than the Blazing Flame Divine Dragon, Jin Taekyung.

And in particular, the Roaring Fury Swordsman kept glancing between Jeok Cheongang and me, looking utterly disbelieving.

I spread both arms wide, as if I’d been waiting for the moment.

“Ta-da! I was lying!”

“……!”

“What do you think? Did I scare you?”

We hadn’t seen each other in ages. A little surprise was only fair.

Judging by the Roaring Fury Swordsman’s trembling body and the sharp breath he’d sucked in, I’d definitely startled him.

Not just startled him, actually. He looked like he was about to have a fit.

Still, the Roaring Fury Swordsman was fairly lucky.

Someone cut in just as he was about to keel over.

“This humble Gong of the Zhongnan Sect pays his respects to Great Hero Jeok.”

The Zhongnan Sect’s Sect Leader, a Daoist with a half-white beard of an awkward, in-between length, respectfully clasped his hands despite the urgency of the moment.

Jeok Cheongang, who’d been just about to keep giving the Roaring Fury Swordsman a hard time, clicked his tongue in disappointment.

“Well, it’s been a while. What was your name again? Gong Piljung?”

“Not Piljung. Iljung. I’m Gong Iljung, Great Hero Jeok.”

“Ah, right. I remember now. Wind-and-Cloud War God Gong Iljung.”

“……Wind-and-Cloud Sword Lord.”

“Good grief. I keep getting my words mixed up today. Sorry about that, Wind-and-Cloud Sword Lord Gong Piljung.”

Having completely lost the will to fight, the Wind-and-Cloud Sword Lord Gong Iljung turned to look at me.

His eyes, already half resigned to his fate, held a question he clearly wanted answered.

*Are you doing this on purpose to mess with me?*

Eyes are sometimes an excellent way to communicate. I answered with my own.

*No. He’s just like that.*

That wasn’t just empty reassurance.

Honestly, neither Jeok Cheongang nor I had any particular grudge against the Wind-and-Cloud Sword Lord.

We had plenty of grievances against his Senior Brothers, the Roaring Fury Swordsman and the Taeeul Merciless Sword. But the Wind-and-Cloud Sword Lord? We’d only crossed paths a couple of times, at the Star-Array Grand Banquet and when the Murim Alliance was founded. We had no real reason to hold anything against him.

The proof was right there: Jeok Cheongang, who looked ready to punch the Roaring Fury Swordsman, was calling the Wind-and-Cloud Sword Lord “you” in a friendly way.

*Besides, people don’t have much bad to say about the Zhongnan Sect’s Sect Leader.*

Feeling a little sorry for having insulted him unintentionally, I shook my head. The Wind-and-Cloud Sword Lord looked considerably more at ease and spoke.

“I’m surprised. I didn’t expect to see you here again.”

“Likewise.”

Jeok Cheongang answered without hesitation, then looked over the Zhongnan Sect Disciples filling the forest path and added,

“I figured you’d be in Gansu or Qinghai by now.”

“……”

“Shaanxi’s just a stone’s throw away. Why are you sprawled out resting in a place like this?”

That was a heavyweight fact bomb.

Jeok Cheongang’s words drove straight into the Zhongnan Sect’s gut, and the Wind-and-Cloud Sword Lord’s face flushed red.

“W-Well…”

He couldn’t bring himself to finish, but his gaze shifted instinctively toward the answer.

The Roaring Fury Swordsman and the Taeeul Merciless Sword.

Their faces had gone dark as they watched us, and I could piece together most of what had happened.

*They’d dug in their heels and dared anyone to do something about it.*

For some reason, those old bastards seemed to have been holding the Zhongnan Sect back from moving. Actually, I was almost certain of it.

Especially since something similar had happened fairly recently.

*Come to think of it, those two were the only ones who didn’t show up.*

When the bloodshed erupted in Shanxi Province a little while ago, the Hebei Peng Family, Huashan, and even the Murim Alliance Headquarters had sent reinforcements. Thanks to them arriving in time, we’d been able to bring things to a complete close.

The Zhongnan Sect?

Strictly speaking, they did come.

A day after the battle was over.

Of course, we were grateful they’d sent reinforcements and taken a certain degree of risk to do it. But I couldn’t deny that it had left a bad taste in my mouth.

*They said they’d sent a thousand troops, but only three hundred made it to Shanxi Province. More than half were nobodies. And even they were late.*

With all three things fitting together so perfectly, it was only natural for the feeling of *this is such bullshit* to start creeping up from deep in my gut.

And seeing two faces I never wanted to see again only made my lips move on their own.

“Well, it happens. Just making the journey while you’re unwell is a fine display of righteous spirit.”

The moment I aimed the remark squarely at my targets, the Roaring Fury Swordsman and the Taeeul Merciless Sword frowned.

“You brat! I’ve told you not to flap your mouth!”

Jeok Cheongang scolded me in a stern voice, then continued,

“Just making it this far while pissing blood all the way here makes you heroes! These great seniors of the Murim are only now beginning to act their age after all this time. How can you speak to them so rudely?”

“……!”

“……!”

“Now then, what have they done so wrong? Did they use their influence to force a weaker sect to close its doors? Or did they steal a Thousand-Year Snow Ginseng and try to swallow a perfectly innocent Escort Bureau whole?”

With each word, the merciless Tongue King’s verbal blows seemed to separate flesh from bone. The Wind-and-Cloud Sword Lord struggled to squeeze out a voice.

“G-Great Hero Jeok, please, for my sake and my Master’s…”

“All right. I’ll stop here.”

“Thank you.”

“No need to thank me, Wind-and-Cloud Sword Lord Gong Piljung.”

“……”

This was vicious. Absolutely vicious.

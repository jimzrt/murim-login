# Checkpoint Review — 1020–1024

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

# Chapters 1020–1024

## Plot

After Dark Heaven captures Dunhuang and breaches the Jade Gate Pass, Jin Taekyung invokes his authority as Marquis of Shangshan to mobilize the forces gathered in the Qilian Mountains and lead them toward the Great Snow Mountain. Sama Pyo returns to Taekyung’s group under orders from his father, Sima Gong, to watch them. Sima says he still intends to restore the Black Dragon Demon Gate and make Pyo ruler of Gansu.

Taekyung’s force reaches the Great Snow Mountain, where allied troops gather for the defense. He worries that the force’s thirty thousand people overstate its actual strength and remains uncertain about Sima Gong’s designs and Pyo’s secret orders. Meanwhile, a Dark Heaven killer slaughters more than a hundred Kongtong members, including the Kongtong Sword Dragon. The killer’s identity and strength remain unknown.

The Blood-Sword Demon Lord, who once served the Heavenly Demon but now serves the Lord of Heaven, declares his confidence in the army’s hidden strength and orders a messenger sent to the Great Snow Mountain. He has been ordered not to kill Taekyung and wants to meet him. At the mountain, all one hundred scouts return dead, each killed with an identical single sword strike. As an enemy army of tens of thousands approaches, a group bearing a white banner advances through its ranks.

## Continuity

- Dark Heaven captured Dunhuang after breaching the Jade Gate Pass, devastating the defenders. The Kongtong Sect Leader escaped with surviving troops; his whereabouts remain unknown.
- Taekyung’s forces have gathered thirty thousand people at the Great Snow Mountain, though he doubts their numbers reflect their combat strength. The enemy army approaching the mountain numbers tens of thousands.
- The Blood-Sword Demon Lord serves the Lord of Heaven, believes the Lord’s army will defeat the Fire King, and has been ordered not to kill Taekyung. The reason for the Lord of Heaven’s interest in Taekyung is unknown.
- One person killed all one hundred Great Snow Mountain scouts with identical single-sword strikes. Jeok Cheongang recognizes the similarity of the wounds but cannot identify the technique or killer.
- An unidentified group carrying a white banner is approaching through the enemy army; its identity and purpose are unknown.
- Sima Gong ordered Sama Pyo to observe Taekyung’s group. Sima says his goal remains the Black Dragon Demon Gate’s resurgence and Pyo’s eventual rule over Gansu. The secret letter Pyo received remains unexplained, and any connection between Sima’s orders and Dark Heaven is unconfirmed.
- A middle-aged killer slaughtered more than a hundred Kongtong members, including the Kongtong Sword Dragon. The killer’s identity and strength remain unknown.
- Taekyung suspects Dark Heaven has at least three Supreme Peak masters or one overwhelming superhuman; these are suspicions, not confirmed facts.

## Translation Decisions

- Render 玉門關 as “Jade Gate Pass,” 伏魔隊 as “Demon-Subduing Squad,” 真人 as “Perfected One,” and 共同劍龍 as “Kongtong Sword Dragon.”
- Render 血劍魔君 as “Blood-Sword Demon Lord” and 天山三老 as “Three Elders of Tianshan.”
- Retain “Moving Formation” for 이동진 and “Marquis of Shangshan” for 상산후.

## Durable state

{
  "active_continuity": [
    "Dark Heaven captured Dunhuang after breaching the Jade Gate Pass, inflicting catastrophic losses on the defenders.",
    "The Blood-Sword Demon Lord once served the Heavenly Demon but now serves the Lord of Heaven and commands an army advancing on the Great Snow Mountain.",
    "The Blood-Sword Demon Lord has been ordered not to kill Jin Taekyung and wants to meet him before battle; the reason for the Lord of Heaven’s interest in Taekyung is unknown.",
    "One person killed all one hundred Great Snow Mountain scouts with identical single-sword strikes; Jeok Cheongang recognizes the wounds but cannot identify their technique.",
    "An army of tens of thousands has reached the Great Snow Mountain, and an unidentified group carrying a white banner is approaching through its ranks.",
    "Sima Gong ordered Sama Pyo to watch Taekyung’s group; the secret letter Sama Pyo received remains unexplained.",
    "The Kongtong Sect Leader escaped Dunhuang, but his whereabouts remain unknown."
  ],
  "continuity_sources": [
    1023,
    1024
  ],
  "open_questions": [
    "What is the hidden strength accompanying the Blood-Sword Demon Lord, and can it overcome the Fire King and the Great Snow Mountain’s defenders?",
    "Why has the Lord of Heaven taken an interest in Jin Taekyung, and what is the purpose of the order not to kill him?",
    "Who killed the Great Snow Mountain scouts, and what is the origin of the sword technique?",
    "Who is approaching under the white banner, and what do they want?",
    "Who sent Sama Pyo the secret letter, what did it say, and are Sima Gong’s orders involving Pyo and Taishan connected to Dark Heaven?"
  ],
  "safe_through": 1024,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1020

# Chapter 1020

It happened in a fleeting instant no one could have predicted.

Whoosh—BOOM!

Even from several hundred *jang* away, everyone—including me—could see and hear it clearly.

A brilliant burst of red light embroidered the sky in the distance, followed by the sound of an explosion.

*A signal flare!*

No doubt about it.

It was a signal flare shot by the scouts who’d gone ahead of the main force. And not just any flare—it was red, the color for extreme danger.

Clang! Clang! Clang!

For a moment, everyone froze at the sudden turn of events. But those who’d quickly grasped the reality before them drew their weapons without hesitation.

“Prepare for battle!”

“Disciples of the Martial Might Sword Sect, prepare for an enemy ambush!”

“Zhongnan Sect Disciples, form the Moon-Shattering Sword Formation!”

The sudden shift in momentum sent a shiver through the air.

As countless blades flashed all around us, I watched our allies move in unison at the shouts ringing through the ranks and kicked off from the saddle.

I didn’t forget to leave a quick word for Hyuk Mujin, who was closest to me.

“Hold your position. Until I get back.”

“W-wait a—!”

I didn’t hear the rest.

A fierce gust swallowed Hyuk Mujin’s voice, and the distance of a dozen *jang* disappeared in an instant.

Feeling the buoyancy that took hold of my whole body, I stepped lightly on empty air, on the wind, and soared upward as I surged forward.

“Th-there!”

“Archers! What are you waiting for? The enemy’s here! Fire!”

“You idiots, lower your bows! He’s one of ours!”

My movements were so free that a few people below, still caught up in the confusion, mistook me for an enemy.

And someone was following close on my heels.

“You don’t give an old man a moment’s peace. What in the world is going on?”

The familiar voice came with the effortless Stepping on Empty Air, as if its owner were running along the ground.

I answered Jeok Cheongang’s question without turning around.

“Something must have happened to the scouts who went ahead.”

“Something happened? You don’t mean what this old man thinks you mean?”

“We don’t know yet. But one thing’s certain…”

I fixed my gaze on the dust cloud rising over the distant, winding sand dunes and added,

“Whatever’s happening, it can’t be good news.”

A quarter of an hour later, I realized once again that bad premonitions, as always, never missed.

“Cough. D-Dunhuang. Dunhuang has…”

His lips were parched, his face pale, and his clothes were little more than rags.

Unlike the scouts, who looked mostly unharmed apart from being covered in dust, the unfamiliar man was marked all over by hardship and desperation. His voice trembled as he continued.

“It’s been… taken by them.”

“……!”

“……!”

Not one of us had any doubt who he meant by “them.”

Dark Heaven.

The Fiends beyond the vast desert had finally crossed the river of sand and set foot in human territory.

* * *

The unknown man was a messenger sent from the Great Snow Mountain, and the urgent news he brought was enough to send a shock through the entire leadership.

“S-say that again. What, what did you just say?”

The Wind-and-Cloud Sword Lord, Sect Leader of the prestigious Zhongnan Sect, stammered despite the fact that he should have been unshakable in any situation. Not a single person so much as let a trace of amusement show.

No—that wasn’t quite right. They couldn’t.

Everyone in that room felt just as he did.

What they’d just heard from the messenger’s lips was enough to make them doubt their own ears.

Yet despite their reaction, the messenger’s account didn’t change when he repeated it.

“I-I regret to report that…”

“Start from the beginning and explain it slowly. Quickly!”

He squeezed his eyes shut, unable to bring himself to continue.

But the messenger from the Great Snow Mountain soon clenched his lips, then managed to speak under the barrage of sharp commands.

“It began when the Jade Gate Pass was breached.”

As far as I knew, in ancient times the Jade Gate Pass had been one of the main passes along the Silk Road, connecting the Central Plains with the Western Regions.

It stood in a wide-open stretch of desert, and though it was only a small earthen fortress, its position made it ideal for keeping watch over the surrounding area.

*In other words, it was a strategic position perfectly suited to monitoring the border with a small force.*

Small, of course, only in comparison to the total force Gansu’s Murim had mobilized. At the recent leadership meeting, we’d heard that at least a hundred scouts had been stationed at the Jade Gate Pass.

No—there *had* been at least a hundred.

By now, every last one of them was probably dead.

“Are you saying they all died? Every single one?”

“We had no way to confirm it, but that is likely. They said the enemy wasn’t detected until it had advanced to within three hundred *li* of Dunhuang.”

“Then when exactly did Dunhuang fall into enemy hands?”

“They said it was about three days ago.”

“Three days ago…!”

A murmur of disbelief rippled through the leadership. That was when I suddenly spoke up.

“Wait. I heard you came from the Great Snow Mountain, not Dunhuang. Who told you this?”

“I never learned his Daoist name, but he was a Daoist of the Kongtong Sect, defending Dunhuang.”

“You don’t know his Daoist name?”

“N-no.”

I quietly furrowed my brow.

The Kongtong Sect was a Daoist sect, and to its members, a Daoist name was as good as their own. Just as the monks of Shaolin Temple had abandoned their worldly names and introduced themselves by their Dharma names, Daoist names were basic introductions among martial artists.

That he hadn’t even given his Daoist name brought two possibilities to mind.

First, the messenger standing before us had brought false information.

Or…

*He died in such a desperate situation that he didn’t even have time to give his Daoist name.*

The messenger’s next words supported my second guess.

“I was too flustered to mention it earlier, but the Daoist was seriously injured when I first saw him. He’d barely arrived at the Great Snow Mountain when he breathed his last.”

“Good heavens.”

A groan escaped someone’s lips.

The leadership’s mood had grown even heavier, and it wasn’t only because the unknown Daoist was dead.

In Murim, a messenger had to be fast enough to break through enemy encirclement and skilled enough to hold his own.

So if the man the Kongtong Sect had sent as a messenger had died moments after arriving, what kind of state had the forces stationed at Dunhuang been in?

Of course, everyone in that room, myself included, already knew what had become of them.

They’d only been trying to deny the shocking news they’d just heard.

“So it was true. All of it.”

At Jeok Cheongang’s cold mutter, the messenger answered.

“It’s a terrible report, hard to believe, but that’s what I was told.”

It hadn’t exactly been a pleasant dream, but it was time to wake up and face the cruel reality.

Leaving the leadership behind as they sat in stunned silence, I managed to part my lips.

My spine was instinctively turning cold.

“At least two thousand dead, and three thousand seriously injured or missing. Is that right?”

The messenger didn’t answer.

He only lowered his head in exhaustion. Seeing him, everyone was finally forced to accept the reality they’d put off for as long as they could.

“H-how can this make any sense…?”

“What can we do? It’s already happened.”

“Ten thousand. A full ten thousand! How could a force that large be defeated so easily?”

Yes. Ten thousand. A full ten thousand.

And yet that massive force, defending Dunhuang under the leadership of the Kongtong Sect, had been wiped out by half—even though they’d fought a defensive battle.

In just half a day.

But that wasn’t the only bad news.

“About thirty percent of the Kongtong Sect’s strength has been lost. During the desperate retreat, two Perfected Ones serving as Kongtong Elders and all one hundred members of the Demon-Subduing Squad died at Dunhuang.”

“……!”

“……!”

Gasps rang out around the room.

What kind of sect was the Kongtong Sect?

One of the Nine Sects and One Gang, one of the fifteen great pillars that supported the martial world.

And now the Kongtong Sect had been broken.

They’d retreated, leaving behind two Elders said to have reached Supreme Peak more than a decade ago and the Demon-Subduing Squad, whose reputation was known even in the Central Plains.

“Then… what happened to the Sect Leader? What happened to the Sect Leader?”

At the Wind-and-Cloud Sword Lord’s urgent question, everyone held their breath and waited for the messenger’s answer.

By modern standards, a loss of thirty percent was catastrophic enough to be called annihilation. But Murim had a different standard.

What mattered, in the end, was whether they still had a master.

No matter how devastating the losses, if the force’s center—the head—survived, there was hope.

If the Sect Leader of the Kongtong Sect, the strongest martial artist in Gansu and someone said to be half a step ahead of even Sima Gong, the Black Night King, had survived, there was still room to counterattack.

And as dozens of pairs of eyes fixed on him, the messenger swallowed hard and gave an answer that could be called a small blessing amid misfortune.

“I heard that the Sect Leader managed to withdraw from the battlefield safely, thanks to the two Elders and the entire Demon-Subduing Squad being prepared to die there.”

“Ah…”

“Thank goodness. Heaven was watching over him.”

Sighs of relief escaped all around them. At that moment, someone suddenly spoke.

“And?”

“Pardon?”

“I asked what happened next.”

Unlike most of the leadership, whose emotions rose and fell with every word the messenger spoke, the voice was calm.

Sima Gong stared at the messenger with a deeply sunken gaze and spoke again.

“If the Sect Leader withdrew with the surviving troops, he must have headed for the Great Snow Mountain. But from what you’ve said, it seems there’s been no word since. How do you explain that?”

Silence fell once more. The messenger looked at a loss before answering.

“I—I have no way of knowing.”

“No way of knowing?”

“Yes. The tide of battle turned in an instant, so the surviving allies split into two groups and retreated. The Sect Leader led many of them away and ordered a Disciple of the sect to deliver this news.”

The dead could say nothing.

The Disciple, sent by the Sect Leader to the Great Snow Mountain, had pushed himself to the limit and died before he could provide any more information. The ten thousand troops defending Dunhuang had been scattered to the four winds, and no word had come from them since.

“However, I left the Great Snow Mountain half a day ago, so it’s possible that the troops from Dunhuang have joined up by now.”

A few members of the leadership nodded with hopeful expressions at the messenger’s addition, but…

*If even the wounded Kongtong messenger, who must have escaped the battlefield ahead of everyone else, was injured that badly…*

Dark Heaven’s great army would already be sweeping the Dunhuang area like a net as it advanced toward the Great Snow Mountain.

Chasing the surviving allies and, at the same time, chasing the surviving allies to break through the second line of defense in their path.

*Their speed is absurd. Far faster than I imagined.*

And at that moment, I realized there was no longer any choice.

“We’re not too late yet. Send a messenger at once and mobilize every force in the Qilian Mountains.”

“What?”

Sima Gong furrowed his brow at my abrupt declaration.

“What did you just say?”

“I said to mobilize every force stationed in the Qilian Mountains. If the Great Snow Mountain falls, it’s over.”

“We’ve already discussed that and reached a conclusion.”

I shrugged at Sima Gong’s steady gaze.

“Then change that conclusion.”

“……You.”

“Ah, just so there’s no misunderstanding.”

The next moment, I pulled something from inside my clothes and added in a low voice,

“This isn’t a suggestion. It’s an order.”

Marquis of Shangshan, Jin Taekyung.

Sima Gong’s eyes widened as he stared at the identity tablet, its characters engraved in elegant script.
## Chapter artifact 1021

# Chapter 1021

The truth was, until just a little while ago, I hadn’t planned to go this far.

The rule that officials and martial artists must not interfere with each other hadn’t come from nowhere.

In a world where the two sides barely spared each other a glance, it was obvious that flaunting either side’s authority would only breed resentment.

But at the same time, authority could be remarkably effective when used in the right place.

Like right now.

“Marquis of Shangshan…”

A low groan slipped from someone’s lips, breaking the brief silence.

In the heavy, sunken atmosphere, Sima Gong stared wide-eyed at the identity tablet in my hand. It was then that he spoke.

“So this isn’t a request. It’s an order.”

His voice was dry as sand. Then his gaze, gone cold, shifted to my face.

“How interesting. Truly interesting.”

Despite his words, the corners of his mouth were stiff. I scratched the back of my head and spoke.

“I’m glad you find it interesting, but I’d rather hear your answer than your opinion. As you know, every fifteen minutes feels like three autumns right now.”

“Am I to understand that you mean every word you said a moment ago?”

“Oh? You still don’t understand? That’s strange. I thought I’d explained it clearly enough.”

“……!”

“Well, if you insist, I’ll say it again. Gather every last soldier you’ve got holed up in the Qilian Mountains and bring them to the Great Snow Mountain right now. That’s an order from the Marquis of Shangshan.”

A stifled gasp went around the leadership.

Who was Sima Gong, the Black Night King?

He was a ruler who shared Gansu Province with the Kongtong Sect—or rather, one who now held an even more dominant position than they did.

It was still only speculation, but if things were settled and peace returned, the Kongtong Sect, having suffered such severe losses, wouldn’t be able to stand against the Black Dragon Demon Gate.

But…

*So what?*

I calmly surveyed Sima Gong and the other leaders, one by one.

At that moment, the people before me didn’t look like the heads of factions shouldering immense responsibility and tens of thousands of lives. They looked like gambling addicts.

Fools, fiddling with their tiles at a vast gambling table where tens of thousands of lives were at stake.

This was when you used authority.

Even if it brought fierce opposition and discord.

And right then, one of the leaders spoke.

“I hear your words and conduct have been getting more and more out of line.”

I looked to see who it was. His face was fairly familiar.

The Sect Leader of a mid-sized sect with around two hundred disciples, someone who carried a fair amount of weight in Gansu.

He’d been at Sima Gong’s side whenever the leadership gathered, which made him more familiar to me than the others.

A close ally, you might say.

“I’ll say this much: I agree with Sect Leader Seok.”

“Young Hero Jin—no, Great Hero Jin—I respect the sense of justice you’ve shown us until now, but surely there are certain principles we must uphold.”

“Although the Great Nation’s imperial court is now standing with us against the great enemy Dark Heaven, that doesn’t mean you should invoke your title as a marquis to strong-arm us like this over Murim’s affairs.”

Birds of a feather flock together; crabs side with crabs. Maybe it was the support of the neighbors, each adding their own word while watching the room. Or maybe it was because Jeok Cheongang stood there with his arms crossed, quietly watching without saying a thing.

Whatever the reason, Sect Leader Seok sounded bolder when he spoke again. Like a loyal dog checking his master’s mood, he stole a glance at the silent Sima Gong.

“Look. Everyone feels the same way. And Sect Leader Sima here has given this plenty of thought…”

At this point, I was almost curious what nonsense he’d say next. But I wasn’t very patient.

“So?”

I cut him off, then added quietly,

“Is there a problem?”

The Sect Leader stared at me in silence, as though he’d been struck dumb. Then, his face stiff, he replied,

“And if there is?”

“Put up with it.”

“What… did you just say?”

“Put up with it, even if it feels dirty and unfair. What are you going to do about it, even if it pisses you off? Does a marquis appointed by the Son of Heaven—no, by His August Majesty the Emperor himself—look like jack shit to you?”

“T-that’s not what I meant!”

His face flushed as he shouted. A laugh slipped out of me before I could stop it.

“Then take off your rank badge and fight me. I’ll keep it a secret from His Majesty. We’ve only just managed to join hands with the Murim Alliance and work together. It’d be bad for both sides if something like this happened now, wouldn’t it? Right?”

The words coming from my lips were directed at the Sect Leader before me. But my gaze wasn’t.

And Sima Gong, whose eyes met mine, wasn’t stupid enough to miss that.

“Those are memorable words.”

As soon as the leader spoke, the room fell silent as a grave.

At last, Sima Gong spoke, looking at me with an expression I couldn’t read.

“You’re right. I, too, am a subject of the Great Nation. I should obey the order of a marquis appointed by His Majesty.”

“……!”

“……!”

Eyes shifted uneasily around the room.

They probably hadn’t expected Sima Gong to agree so readily.

As for me, I’d more or less expected this response.

“May I take that to mean you’ll follow my orders?”

“I will. This time, I’ll be the one to yield.”

“So there won’t be a second time.”

“What can I do? I have my pride, which I must uphold even if it kills me, and my own judgment. I trust you and the Senior over there will understand that much.”

Sima Gong was even managing a faint smile now. Without meaning to, my gaze sank.

*What the hell is this guy?*

He was definitely hiding something, but I couldn’t tell what it was. No—he wasn’t giving me the slightest opening to catch a glimpse.

*I came on strong on purpose, but he barely reacted.*

I hadn’t invoked the authority of a marquis and tried to force him into line simply because the situation was urgent.

Even a massive boulder weighing ten thousand *geun* would shake when struck.

I wanted to infer Sima Gong’s intentions from his reaction. I also wanted to see how many of the leaders gathered here were on his side.

The latter had yielded a little. The former had failed spectacularly.

And until his true intentions came to light, Sima Gong and I were allies under the same banner.

“As you said, every fifteen minutes feels like three autumns right now. Is there anything else you need to say?”

I stayed silent for a moment, but I couldn’t read anything in the gaze we held across the open space between us.

“No.”

“Good. Then I’ll immediately send someone to bring in every force in the Qilian Mountains. Does Zhongnan agree?”

The Wind-and-Cloud Sword Lord had been glancing back and forth between Sima Gong and me, his eyes still unsettled. He opened his mouth.

“If the Great Snow Mountain falls, Gansu will be on the brink. I see no reason to disagree.”

“Then it’s settled. Family Heads and Sect Leaders, inform your martial artists and make sure they’re ready. We must reach the Great Snow Mountain ahead of them within half a day at the latest.”

The leaders of Gansu’s Murim exchanged wary glances, then performed the clasped-fist salute. Sima Gong was hurrying back to his saddle when he suddenly stopped.

As if he’d forgotten something, he gave a quiet exclamation and turned toward me.

“Ah, could I ask one favor?”

“What favor?”

“I’m thinking of entrusting my son to you again. The one I borrowed for a while. What do you think?”

I stared at him in surprise. Sima Gong continued with a hearty laugh.

“I was glad to see a blood relative I hadn’t seen in a long time, so I kept him by my side for a few days. But in wartime, we must strictly separate public duty from private affairs. He’s a member of the Fire Dragon Pavilion before he’s the Young Sect Leader of the Black Dragon Demon Gate. Isn’t that right?”

Sama Pyo hesitated for a moment, then answered in his usual blunt voice.

“……That’s right.”

What was he up to?

Truthfully, I already had a good idea of Sima Gong’s intentions. But I couldn’t let that show—not in a situation like this.

I nodded, keeping my expression and tone as calm as possible.

“If that’s all you’re asking, of course I’ll do it. I’ve been wondering when he’d come back.”

“That’s good to hear. Then I’ll take that as a yes and send him back to the rear shortly. With no one knowing what could happen at any moment, shouldn’t a father and son have a chance to say goodbye?”

At Sima Gong’s faint smile, I found myself newly certain of the suspicion I didn’t want to believe.

Before he was a member of the Fire Dragon Pavilion, Sama Pyo was Sima Gong’s blood relative—and the Young Sect Leader of the Black Dragon Demon Gate.

From now on, he’d be with us not as a comrade, but as a spy.

*Damn it.*

To hide my twisting expression, I gave a deep clasped-fist salute and turned away.

* * *

Thud, thud, thud, thud!

The five thousand men and horses surged forward at full speed the moment they set out.

The earth shook as if there had been an earthquake, and the cloud of dust rising amid the thunderous noise was more than enough to obscure them from any prying eyes.

“Do you know why I want you to stay by Jin Taekyung’s side?”

Sima Gong asked, watching his son’s expression with a sharp gaze. The answer that came back didn’t waver in the slightest.

“What do you want me to do?”

“Exactly what you suspect. Watch their every move.”

“That’s a difficult task.”

“Why do you think so?”

“Because I mustn’t draw needless suspicion.”

Sama Pyo had already accepted the order. Sima Gong smiled inwardly with satisfaction.

To ask no questions. To harbor no doubts.

That was exactly the way he wanted his son to be—and the way he’d wanted him to be again.

“Aren’t you curious why I’m giving you this order?”

“I’ll simply follow your command. It must be for the good of our sect.”

His answer came without hesitation. A faint smile appeared at the corners of Sima Gong’s mouth.

“That’s right. It’s all for the resurgence of our family and the Black Dragon Demon Gate. And before long, it will all be yours. Then you’ll be the undisputed ruler of Gansu Province, and you might even be able to expand into the Central Plains.”

“You mean…”

His son let the words trail off. The father gave a small nod.

“There can’t be two tigers on one mountain.”

“……!”

“Things went awry, unlike what we initially expected, but nothing has changed. No matter what gets in our way, we will get what we want.”

As always.

The words he added quietly were swallowed by the wind. His son watched his father’s eyes gleam with ambition, then turned his horse with a respectful clasped-fist salute.

There was no tender father-son farewell like the one Sima Gong had just spoken of to Jin Taekyung.

As always.
## Chapter artifact 1022

# Chapter 1022

The five thousand men and horses pushed themselves to the limit as they raced forward.

They threw away even the food and supplies they’d been carrying in the barest quantities, trying to lighten their loads by even a single *geun*. They whipped their horses on without a thought for pacing them.

If a horse foamed at the mouth and collapsed, they ran on foot, pouring all their internal energy into their movement techniques.

It was a forced march that would leave even a well-trained martial artist utterly exhausted.

For the Zhongnan Sect and Fire Dragon Pavilion members, who had managed only a couple of brief rests unlike the martial artists of Gansu, the final half day must have felt like ten years.

But thanks to the short forced march that had pushed everyone to their limits, we spotted the snow-white mountain range appearing alongside the first light shining over our backs.

*The Great Snow Mountain.*

True to its name, the snow-covered peaks glowed in the dawn light, dazzlingly white and utterly alien.

No—perhaps the strangest thing of all was this fickle weather.

*It was nothing but desert all around us just two hours ago.*

I glanced up at the sky, which was dumping great flakes of snow as if it had never been otherwise, then looked back at the Great Snow Mountain.

Dozens of high peaks met the clouds, and the range wound between them.

The colossal barrier of nature still shrouded in darkness was silent. Wariness and unease spread among the five thousand men and horses as they gradually slowed and drew closer.

It was only natural.

By now, everyone had heard the news that the front line at Dunhuang, built around the Kongtong Sect, had been utterly crushed half a day ago.

*Of course, given the distance and the time, it’s unlikely the Great Snow Mountain has already fallen to Dark Heaven…*

War was a monster too changeable to be reduced to probabilities.

Especially when we had to fight enemies who wielded bizarre powers that were hard to define with the simple term *dark arts*.

*Still, I never thought the Kongtong Sect would fall this easily.*

To be fair, the Kongtong Sect’s strength wasn’t among the highest of the Nine Sects and One Gang.

Even so, according to the gossips, it had three Supreme Peak masters, including its Sect Leader, and its main disciples—the core of its strength—were also accomplished martial artists.

Yet it hadn’t held out for days. It hadn’t even lasted half a day. Even I, despite having clashed with Dark Heaven several times, had trouble gauging their strength.

*The Kongtong Sect must have had enough time to prepare, and enough strength to defend itself.*

Three Supreme Peak masters who embodied the Kongtong Sect, a thousand disciples, and a force of no less than ten thousand gathered around them.

Thanks to the information Ma Junggeol had brought, we knew Dark Heaven’s army numbered at least thirty thousand. But there was an enormous difference between defending a fortress and attacking one.

Hearing that Dark Heaven had overcome such an advantage and crushed our forces so one-sidedly brought one possibility to mind.

*There must be at least three Supreme Peak masters among them. If not… then they have one monstrously powerful master. Powerful enough to dominate the battlefield with sheer martial might.*

The first possibility would be fortunate. The second would make for a hard fight.

Just as not every martial artist was alike, neither were the people called superhuman.

Those at the foot of the mountain didn’t know how many trees stood on its vast slopes or how many steep gorges cut through it.

The dozens of peaks that looked much the same from afar had heights and shapes that varied wildly when you saw them up close.

That difference between superhumans was why the force of ten thousand, including the Kongtong Sect, had suffered near-annihilation and been forced to retreat.

*Our force is formidable too. But did Dark Heaven really pour tens of thousands of troops into Gansu without knowing that?*

Jeok Cheongang, myself, the three old Daoists of the Zhongnan Sect, and Sima Gong, the Black Night King.

There were six Supreme Peak masters right here, and the thousands of men and horses crossing Gansu were bound to be noticed wherever they went.

In the end, I reached one conclusion.

*They must have advanced into Gansu because they believed they had a good chance of winning.*

Then what could make them so confident despite losing four Demon Lords and a Demon Empress?

The Blood Lord, who had vanished after the Shaolin Bloodshed?

Or some other force Dark Heaven had yet to reveal?

Or…

*The Lord of Heaven?*

Just as those two words slipped from my lips without my realizing it, a chill ran down my spine by instinct.

Whoosh!

A sharp whistle suddenly rang out. I turned toward the sound and saw flames rising one after another from deep in the Great Snow Mountain.

Boom. Boom. Boom!

Once, twice. Then three times in a final burst.

The fireworks burst across the sky in quick succession, and a red line appeared along the mountain slope, still blanketed in white.

*That’s…*

A signal.

The forces who had taken the Great Snow Mountain were signaling with fireworks and torches.

A sigh of relief passed among the people who’d been on edge.

Hyuk Mujin and Song Ilseom, their hands resting on their sword hilts as if ready to draw at any moment, were no exception. Neither were Ju Hwaran and Namho, watching ahead with tense expressions.

But there was one exception among them: Sama Pyo, who had rejoined the Fire Dragon Pavilion half a day earlier.

*…That guy.*

I wanted to ask him right then and there.

Why had he been silent the whole time?

How could he keep his composure as if he’d expected this, even while everyone else had been forced to stay tense and wary?

But I didn’t ask. I couldn’t.

I watched Sama Pyo riding alongside the still-dejected Taishan, my gaze tangled with conflicting thoughts, then quietly turned away.

Jeok Cheongang’s question from recently came back to me.

*“If Sama Pyo and Taishan are up to something on Sima Gong’s secret orders, and those orders are connected to Dark Heaven… what would you do?”*

*Hell if I know. What should I do?*

With that question still unanswered in my heart, I silently tightened my grip on the reins.

Unlike the reality before me, the dawn spreading from the east was bathing the Great Snow Mountain in light.

* * *

“Guh… ack.”

The man’s lips trembled as he vomited a mouthful of dark red blood.

His Daoist robe, once as white as snow, had long since been stained with blood and dust. His unfocused eyes could barely make out what was in front of him.

And yet, he didn’t let go of the sword in his hand. He couldn’t.

*Not yet. It isn’t over.*

His ever-reliable Senior Brother, his tiger-like Senior Martial Uncle, and the young Junior Sister he’d thought of as a niece were no longer by his side.

They were dead. Every last one of them.

Their heads had been cut off. Their hearts pierced. Or their bodies blown apart so completely that not a trace remained.

That was why he had to rise. He had to take revenge.

Crack.

Blood burst between his clenched teeth.

His senses had gone numb; he couldn’t even smell the metallic tang of blood.

The man drank his own blood as if it were the elixir of life.

He forced his unsteady legs upright and swung the beloved sword he’d received long ago from his Master, from his sect, at the enemy before him.

With more desperation than ever. Squeezing out even the last scrap of strength he had left.

“Ugh. Aaargh!”

At the moment he brought his sword down with a ferocious shout that made the veins in his neck stand out, the man was suddenly seized by a strange sensation.

*Whoosh.*

It was as if time had stopped.

The air against his skin, the wind blowing from somewhere, even the sword blade falling with the movement of his hand—

Everything slowed, and at the same time, everything grew clear.

*This is…*

The man shuddered.

In all his thirty-some years of life, he had felt this sensation only once before.

It had happened on the day he finally reached the Peak realm after grueling training, just before he gained enlightenment.

*No-self.*

The moment of insight every martial artist longed for: a brief instant when they forgot even their own existence and advanced toward a higher realm.

*Ah. Aah.*

The man’s eyes trembled.

His focus returned, and beyond his now-clear vision he saw a middle-aged man trapped in the slowed flow of time.

No—a monster who had slaughtered more than a hundred members of his sect all by himself.

But not anymore.

The monster, who had been too fast for him to follow with his eyes only moments ago, was now frozen in place, unable to move. The man’s sword was falling through the slowed time, toward the crown of the monster’s head.

*Die.*

The man was certain.

This enlightenment had made his martial might advance by leaps and bounds.

He had broken through the wall that had held him back for so long. His Demon-Subduing Sword had finally reached eight-tenths mastery, and it would cut down the monster before him.

And then—

*Whoosh! Clack.*

The monster reached out at the speed of light and caught the blade in his hand.

Only then did the man understand.

It had all been an illusion.

It wasn’t time that had slowed. It was only him.

Crack!

The man’s nightmare shattered along with his beloved sword. In his vacant eyes, he saw the monster smiling.

“You flailing around by yourself was quite a sight. How about I give you another chance, just in case?”

The man stared blankly at the enemy before him.

The monster’s face, seen up close for the first time, belonged to such an ordinary-looking middle-aged man—if you overlooked the blood covering him from head to toe.

Maybe that was why, even after feeling the truth of what he was down to his bones, even knowing that he was beyond reason, the man forced his voice out.

“Why… why are you doing this?”

“What?”

The monster—no, the middle-aged man—furrowed his brow.

“Why am I doing this? What a pathetic question. You might as well ask a fisherman why he catches fish.”

“……!”

“And this is all your own fault. I told you I’d spare you for now if you surrendered quietly, but you had to… Honestly, those damned Daoist bastards don’t listen until they see blood.”

The middle-aged man let out a deep sigh and looked at the man with pity.

“From the looks of it, you won’t be able to give me the answer I want either.”

The man, already at the threshold of his final rally, answered in a faint voice.

“Heaven… Heaven will punish you.”

“What? Heaven’s punishment? Did you just say Heaven’s punishment?”

The middle-aged man’s eyes widened. Then he suddenly chuckled. At some point, his blurred hand pierced the man’s chest.

Crack!

His back arched with the agony of bone and flesh being crushed. Through his vision, slowly turning black, the man saw clouds drift across the sky as if nothing had happened.

Then a voice pierced his ears for the last time.

“Can you see it? The new Heaven.”

“……!”

Crack. Thud!

The man’s body crumpled as the hand was pulled free.

The middle-aged man stepped on the corpse of the Kongtong Sect’s most renowned rising martial artist, the Kongtong Sword Dragon, and turned his head toward the vast mountain range in the distance.

The Great Snow Mountain.

It would soon be stained red with countless streams of blood, but for now it shone brilliantly in the rising sunlight.

“Come on, let’s have ourselves a little fun.”

Behind the middle-aged man’s smile, a tremendous rumble began to shake the earth.
## Chapter artifact 1023

# Chapter 1023

Huff, huff.

Footsteps climbed the steep mountain slope without a word, while clouds of white breath billowed here and there.

The Great Snow Mountain was cold year-round, like the middle of winter, and its air was thin. Those who had come to defend this land were no exception to its harsh conditions.

If anything, the brutal environment might have been even harder on our side.

“Cough. Haa…”

Was it because we’d entered the highlands?

Or because his body had grown old?

Namho kept coughing, struggling to catch his breath. I was just about to give him an order when someone stepped up beside him first.

“Steady your breathing and relax your body.”

Tap.

A calm voice, a hand pressing the Mingmen acupoint. At the same time, a faint energy stirred around Namho.

Whoosh.

The pallor creeping across his face eased, and his complexion regained some color. With the internal energy sent through the Mingmen acupoint, Namho looked as if nothing had happened and went back to grumbling as usual.

“Damn it. Getting old’s a crime. Anyway, thanks for the help…”

His words trailed off before he could finish.

Namho had just turned to thank him when his voice faltered despite himself. Standing behind him, Sama Pyo asked with an impassive face,

“What is it? Is something wrong?”

The surprise lasted only an instant. The old Hidden Shadow Pavilion agent recovered quickly and smoothly.

“Hm? No, nothing’s wrong. I just thought I saw something moving over there.”

“Over there?”

As Sama Pyo turned to look where Namho was pointing, a small shadow sprang out from behind a dry tree and darted across the snow.

“It was a mountain hare. No need to worry.”

“Is that so? Well, it’s not like they could’ve snuck all the way up here. Getting old just means you’ve got more to worry about.”

Namho replied nonchalantly, then looked at me and smacked his lips.

“Getting winded from something this small must mean I really am old. If I were just ten years younger—not a day more or less—I’d be leading the charge. Wouldn’t you say?”

The more someone knew, the more they tended to give themselves away.

Even so, Namho had hidden his feelings smoothly. I answered in an even tone.

“Have you lost your mind? You wouldn’t be fit to lead the charge even if you were thirty years younger.”

That wasn’t just an answer meant to brush off the situation.

All around us, plenty of people were huffing and puffing as they climbed the Great Snow Mountain.

*Can’t be helped. We chose quantity over quality.*

Gansu Province was vast, but it was still just one province.

The only reason we’d managed to gather the staggering number of thirty thousand was that we’d taken in all manner of riffraff during recruitment.

From green youngsters whose upper lips had only just begun to darken to Third Rate swordsmen who’d spent their entire lives roaming the back alleys until they’d grown old.

The place was full of people who might never have had their lives threatened—or taken another’s.

In a word, they were like little fish in the vast sea of Murim, nothing more than prey for the predators around them.

Of course, I didn’t look down on them.

I had neither the right nor the inclination to.

I’d once been weak too. And even now, there were still people to whom I was nothing but weak.

What truly worried me was having to face Dark Heaven’s forces with an army whose numbers had been inflated without adding much strength.

And besides…

*More than half of them belong to the unorthodox faction.*

Someone once said that it didn’t matter whether a cat was white or black, as long as it caught mice.

I agreed with the sentiment.

History had already proved it.

The Great Faction War had been the decisive turning point that united Murim under one banner. And during the Great Cataclysm in the modern era, even the infamous Mexican drug cartels had joined the government forces to fight the monsters.

The appearance of an outside enemy could turn yesterday’s foe into today’s ally.

But what mattered now was who had put bells around the necks of all those black cats—and what that person truly intended.

*The Black Night King, Sima Gong.*

The biggest and most powerful black cat to survive the Great Faction War, and another Alliance Leader who now ruled the unorthodox Murim.

If he’d already set his sights on something else, then the crushing defeat at Dunhuang and the fall of the Kongtong Sect might have been nothing more than steps in a process decided long ago.

And at the end of that process, a new Heaven called Dark Heaven would be waiting for everyone.

*I have to stop that. No matter what it takes.*

I muttered the words inwardly and glanced behind me.

Sama Pyo, walking along in silence, caught my brief look and gave me a small nod.

He looked no different from usual. Yet just then, it felt as if a huge boulder were pressing down on one corner of my chest.

Rustle.

Dozens of *jang* away, a group appeared as the bare, leafless trees shivered all at once.

Hundreds of silver arrowheads flashed between the branches.

But the brief flare of alarm soon eased at someone’s shout.

“Lower your bows. They’re brothers from Gansu Murim!”

Of course, not everyone lowered their guard.

“Stand by. Do not let your guard down until I give the order!”

A booming voice, a rough suit of armor to match it.

The sight of a heavily armed man, his helmet pulled down low, brought two words to mind.

*The military.*

Step, step.

Despite the weight of his armor, he moved with easy grace.

The man closed the distance at an unhurried pace—not too fast, not too slow. Sima Gong, who had been leading our group, opened his mouth to speak.

No—that wasn’t quite right. He was about to speak.

The man passed Sima Gong as smoothly as water flowing downstream, fixed his gaze on me, and asked,

“May I ask your name, sir?”

“Have you no manners? Do you even know who this man is, to demand an answer from him?”

Naturally, that wasn’t my answer.

Before I could say a word, Hyuk Mujin stepped forward, putting on airs as he raised the silver tablet in his hand—no, wait. When had he taken that?

“If I may introduce him, he is the Third Young Master of the great Jin Family of Taiyuan, the hegemon of Shanxi Province; a Commander of the Embroidered Uniform Guard who protects the Great Nation’s imperial family; and one personally appointed by His August Majesty the Emperor…”

“Hong Pyo, Deputy Thousand Captain of the Gansu Regional Military Commission!”

A roar swallowed Hyuk Mujin’s voice. The knees of the man, who had stood like an iron tower, bent.

Thud.

With a heavy sound, the man—Hong Pyo—knelt on one knee and gave me a crisp military salute.

“I pay my respects to the Marquis of Shangshan!”

“We pay our respects to the Marquis of Shangshan!”

Hundreds of voices carried across the cold snowfield.

Only then did the imperial troops lower their bows and weapons, kneel in unison like Hong Pyo, and bow low. Hyuk Mujin trembled.

“Grrr. Ugh. Ahhh.”

“…What is that weird noise?”

“Captain. I think I’m gonna burst.”

“…”

Burst, my ass. You lunatic.

I sighed and shook my head. Just then, I met Sima Gong’s gaze as he watched us with a peculiar look, and I clicked my tongue.

“Mujin.”

“Yes?”

“Just do it. Let it all out.”

Hyuk Mujin’s face turned stern.

“What do you mean, let it out? I was just saying.”

“…”

“Don’t say embarrassing things like that in front of your subordinates. You need to maintain your dignity as a marquis. Otherwise, you’ll look vulgar.”

I really wanted to kill him.

* * *

Hong Pyo, the man with the lengthy title of Deputy Thousand Captain of the Gansu Regional Military Commission, was built like a bear.

To put it kindly, he was steadfast. To put it less kindly, he had absolutely no flexibility—and no sense of when to back down.

In a word…

*An unlucky Jeong Hogun, maybe.*

Thinking of Thousand Captain Jeong Hogun, whom we’d had no choice but to leave behind because we were in such a hurry, Hong Pyo reminded me of him, yet was unmistakably different.

And the biggest reason I could make such a firm judgment about Hong Pyo’s character, whom I’d only met today, was probably his attitude toward Sima Gong.

“So you’re the Deputy Thousand Captain everyone’s been talking about. They say no one in the world is more meticulous than you when it comes to carrying out official business.”

Sima Gong had already been ignored once, but he addressed Hong Pyo with a gentle smile. Hong Pyo stared at him blankly for a moment, then spoke.

“Your identity tablet.”

“Pardon?”

“Present your identity tablet. I’ll confirm your identity first, as procedure requires.”

“…You’re asking me to present my identity tablet? Surely you’re talking to me?”

Hong Pyo nodded without hesitation, as if the question were perfectly reasonable.

“I am.”

“Do you not know who I am?”

“I saw you once from a distance at the City Lord’s sixtieth-birthday banquet the year before last. When I asked my superior, the Regional Military Commissioner, he told me you were the Sect Leader of the Black Dragon Demon Gate.”

“I see. Then you know.”

“Know what? That was then. This is now. My assigned duty is to guard this stretch of about three hundred *jang* and verify the identities of those passing through. Nothing more. The Marquis of Shangshan has already gone through the procedure.”

Hong Pyo looked at Sima Gong as if he’d never seen such a strange man before, then furrowed his brow.

“Don’t make me repeat myself. You’re clearly older, so I’ll overlook how casually you speak to me. But keep refusing, old man, and you won’t like what happens.”

“……!”

The air around us seemed to freeze. It wasn’t just because we were on the Great Snow Mountain, covered in everlasting snow.

Who was Sima Gong?

The Sect Leader of the Black Dragon Demon Gate, with enormous influence over Gansu Murim. Given his standing and power, he could sit as an equal with the City Lord.

In short, he was a powerful figure in Gansu Province, with strong ties to both Murim and the government.

And Hong Pyo had demanded his identity tablet and called him an old man.

That alone was enough to leave everyone speechless. But Hong Pyo didn’t stop there. He went a step further.

Shing.

“I said it clearly. There won’t be a second time.”

As he added those quiet words, Hong Pyo drew the iron baton from his waist.

Sima Gong and everyone around him were at a loss for words.

“Ha! Hahahaha! Yes, that’s right! That’s how it should be!”

Jeok Cheongang’s laughter rang out. Holding his stomach, he guffawed as he looked at Hong Pyo.

“A man should fulfill the duty entrusted to him. Now, what was your name again?”

Hong Pyo answered Jeok Cheongang’s friendly question.

“Your identity tablet.”

“…What?”

“You should have yours ready too. You’re next, old man.”

“……!”

“And your travel pass as well. Even your hair is bright red. You look downright suspicious.”

In the silence, heavy enough to suffocate everyone, Hyuk Mujin trembled and whispered in a voice quieter than an ant’s squeak.

“Captain. I really think I’m gonna burst.”

But before I could answer, a sound echoed like a distant call from beyond the white ridge stretching far away.

Boom. Ba-boom. Ba-boom!

A drumbeat, urgent with alarm.

The sound of the war drums shook the snow-covered mountain range.
## Chapter artifact 1024

# Chapter 1024

For martial artists who were always brushing up against death, hearing was an invaluable sense.

Sound could carry a great deal of information.

When you were facing an enemy, the whisper of a sleeve brushing past could only mean they were launching a sneak attack. And you could read someone’s state of mind from the pitch and tremor of their voice.

In other words, to a martial artist, sound was information.

And the drumbeats rolling in from far away at that very moment were no exception.

Thump. Thump-thump. Thuuump!

The rhythm was all over the place, and each beat rang out at a different volume.

An image came to the middle-aged man’s mind: somewhere in the snow-covered mountains, a drummer was pounding away with all his might, looking as if half his soul had already left his body. He scratched the back of his neck.

“Did we come on a little too strong with the welcome?”

Low laughter rippled through the group at his words.

By now, they weren’t the only ones who knew that the hundred scouts from the Great Snow Mountain they had encountered nearby two hours earlier were dead.

“Can you blame them? Their comrades, the people they shared meals with, came back as corpses overnight.”

“Looks like those horses came back with heads dangling all over them, and scared the daylights out of everyone. They don’t even know this is only the beginning.”

“Still, we mustn’t let our guard down either. We don’t know exactly how powerful the Fire King, that old monster, is…”

*Boom!*

A tremendous crash swallowed the rest of his words.

Before he could finish speaking, the old man felt an immense force slam into his chest. His body shot backward like a cannonball, but he righted himself in midair and landed on the ground.

Or tried to.

“Ugh, bleurgh!”

A spray of blood poured from his lips as he staggered, his balance gone.

At last, unable to withstand his internal injuries, the old man dropped to one knee. The other two elders, who had been laughing along with him just moments ago, stared at the middle-aged man with stiff faces.

The man who had felled a Supreme Peak master with a single move glanced back and forth between his hand and the fallen elder, his expression perfectly calm.

“Well, I put too much into that. Elder Three, are you all right?”

The old man—Elder Three—coughed up blood as he knelt and gasped for breath.

“I’m… I’m fine.”

“Good. I didn’t mean for it to come to that… Anyway, what do you think?”

“What… do you mean?”

The middle-aged man smiled faintly at Elder Three’s question.

“I’m asking how I compare to the Fire King, that old man.”

“……!”

“What, you think I don’t stand a chance? Well, you don’t know much about the Fire King either, so I suppose it’s hard to answer. You said you’d only seen him once, from a distance, a long time ago. Wasn’t that right?”

The middle-aged man looked over the three elders in turn, smacked his lips, and muttered.

“Shouldn’t have asked. You ran off like rats, so how would you know?”

Could there be a more humiliating thing to say to martial artists, who were said to be made of pride and confidence instead of flesh and blood?

And yet the three old men—the Three Elders of Tianshan—could only tremble in silence.

Were they trying to suppress the rage welling up inside them?

No.

How could you suppress something that didn’t exist?

In the old men’s bodies and hearts, there was no anger toward the middle-aged man.

The emotion binding them like chains at that very moment was fear.

He’d lashed out with a killing blow without hesitation over a single word that displeased him. His expression and tone made it seem as though he were looking at ants he could crush underfoot at any moment.

The middle-aged man before them had both the strength and the right to act that way.

“Please forgive us!”

“I-It’s because we’re lacking.”

“This foolish old man misspoke. How could someone like the Fire King ever be a match for the Demon Lord?”

The three fiends of Tianshan, who had once drenched the Central Plains in blood beneath the Demonic Cult’s banner, scrambled to prostrate themselves before him.

If they didn’t, they felt the middle-aged man—the Blood-Sword Demon Lord—might kill them on the spot.

Looking down at them, the Blood-Sword Demon Lord wore an unmistakable sneer.

*Pathetic fools. Had they really tried to conquer the world with the likes of these men?*

His scorn wasn’t limited to the Three Elders of Tianshan.

It was also directed at the one man he’d once followed, the man who had been everything to him.

*You were doomed to fail, Cult Leader. A mere human compared himself to Heaven.*

The Heavenly Demon.

Remembering the man who had inherited that title through the generations and ruled as the king and Heaven of the Hundred Thousand Demonic Disciples, the Blood-Sword Demon Lord let out a hollow laugh.

Thinking back on it now, it was truly ridiculous.

That he had pledged his loyalty to someone so ordinary.

That he had dreamed of a Demonic Path ruling the world—a feat no Heavenly Demon had achieved in a thousand years.

But things were different now.

He had gained insight through failure and accepted a new Heaven.

A new Heaven called the Lord of Heaven.

His true master.

And the Blood-Sword Demon Lord firmly believed that his enemies at the Great Snow Mountain, drawing nearer even now, would soon serve the Lord of Heaven alongside him.

Even if they refused fiercely, resisted, and chose death in the end, the outcome would be the same.

*In the end, they’ll seek shelter in that person’s shadow.*

With a quiet laugh, the Blood-Sword Demon Lord suddenly turned to look behind him.

*Crunch. Crunch.*

Tens of thousands of troops were marching toward the Great Snow Mountain, crushing the frost-covered plants underfoot.

At their head were seven strange figures clad in robes as black as night, and several dozen men in white, their appearance a stark contrast.

“Your concerns seem to be weighing on you, so I’ll tell you something.”

The Blood-Sword Demon Lord spoke without warning, then continued slowly, addressing the Three Elders of Tianshan.

“Someone like the Fire King could never stop us.”

This wasn’t confidence. It was certainty.

Certainty in the hidden strength they hadn’t revealed when crossing the Jade Gate Pass—not even when they trampled Dunhuang, defended by the Zhongnan Sect, in an instant.

Of course, the Three Elders of Tianshan had an inkling of it too.

Even they, fiends who had once dominated their age, could sense that there was nothing ordinary about the people whose identities filled them with dread.

But…

*What are they?*

*He hasn’t told us their names or titles. How can he be so certain?*

*There’s nothing we can do. We’ll just have to follow him.*

They could only quietly swallow their questions.

The Blood-Sword Demon Lord clicked his tongue softly at the sight of the Three Elders bowing their heads, unable even to meet his eyes. Then he issued his first command on the Great Snow Mountain.

“Send them a messenger.”

“A messenger, you say?”

“We’ve already given them a greeting. It’s only fair to show them the mercy of offering them a chance to surrender. And…”

The Three Elders waited for him to continue, but the Blood-Sword Demon Lord silently swallowed the rest of his words. Then he smiled faintly and thought to himself,

*There’s someone I’d very much like to see, too.*

He didn’t mean the Fire King, Jeok Cheongang, his former enemy, who had fought for his own goals on battlefields far from his.

Before the fighting truly began, the person the Blood-Sword Demon Lord wanted to meet wasn’t the old monster from Mount Jiuhua, but his Disciple.

The Blazing Flame Divine Dragon, Jin Taekyung.

For some reason, the young colossus of the orthodox Murim had drawn the attention of his master—the Lord of Heaven—in a way the Demon Lord couldn’t understand.

From the moment he’d received an order that went further than necessary, telling him not to kill Taekyung even if they met, the Blood-Sword Demon Lord’s thoughts had been fixed on him.

*Let’s see if he’s really worthy of all that.*

The Blood-Sword Demon Lord’s eyes shone brightly.

* * *

A hundred.

Not one person out of the Great Snow Mountain’s hundred-man scouting party had been spared.

They had left four hours earlier to check on the enemy’s movements. Now they’d returned as one.

Their heads hung from the saddles.

“J-Junior Sister…”

“No. No!”

Cries like screams rang out from all around us.

Those who had lost people close to them in the scouting party poured out their grief and rage. Even the Fire Dragon Pavilion members, who were used to gruesome sights, clenched their teeth.

“This…”

The speaker’s lips trembled, unable to finish the thought.

But in a situation like this, someone had to keep a cool head.

I studied the severed heads with a steady gaze, then exchanged a look with Jeok Cheongang.

“You saw it?”

“Yes. Every one was cut by a single sword strike. And the wounds are all identical.”

“So that means…”

“One person did it. A truly fearsome sword technique. I’ve only seen anything like it a few times in all my life.”

Death left its mark. The cuts on the scouts’ heads were so even and sharp they could have been measured with a ruler.

If even Jeok Cheongang judged it that way, then it had to be a master at least comparable to one of the Ten Kings—or someone even stronger—who had slaughtered them all.

“And this…”

Jeok Cheongang stopped mid-sentence and frowned.

“Damn it, I can’t place it. I’m sure I’ve seen a wound like this somewhere before…”

He seemed to be racking his brain, digging through his memories, but I quietly shook my head.

The enemy’s identity wasn’t what mattered right now.

It was the horrifying number of enemies approaching in the distance, raising a vast cloud of dust.

I couldn’t make out their exact numbers yet, but even just counting those pouring down the hill toward us, there were a staggering twenty thousand.

Though they were still several hundred *jang* away, the aura and killing intent pouring from that enormous army made even the wild birds living in the harsh Great Snow Mountain take frenzied flight.

“Damn it. It was real. What I saw was real. Those fiends made it all the way here.”

Ma Junggeol, chief of the Seven Masters of Baekma Bang, had been dragged here as something of a hostage. He chewed his lip and muttered to himself.

In his trembling hand was a telescope—no, in Murim, it was called a *siptiryeong*.

“Madness. The Hundred Thousand Demonic Disciples, just like I’d heard. We’re finished. It’s all over now…”

“Shut your mouth, unless you want to be the first one finished.”

Hyuk Mujin cut Ma Junggeol off with a single sentence, snatched the telescope from his hand, and whispered to me,

“Captain. What do you plan to do now?”

I answered evenly.

“You know what we have to do.”

With the enemy almost upon us, only one choice remained.

Battle.

No—a bloodbath.

Once a fire had taken hold, it didn’t end until it had burned the whole field. The fire called Dark Heaven had started in the desert and reached the Great Snow Mountain. We would meet it with a fire of our own.

*Once everything around us is drenched in blood, it’ll finally be over.*

Hyuk Mujin, who’d asked the question; me, who’d answered it; and everyone on the Great Snow Mountain preparing for a battle to the death—we all knew it.

There was one thing we didn’t know: how the battle would end.

*Of course, someone might already have a guess.*

I glanced at Sima Gong, directing the martial artists of the Black Dragon Demon Gate far away.

And Sama Pyo, too, who stood watching the mountainside with a rigid expression, unlike his usual calm.

The next moment, I understood.

The reason Sama Pyo’s face was so tense had nothing to do with the pressure of battle or some secret he was hiding.

“They’re coming.”

I turned at his quiet words and saw them.

A group was approaching, carrying a pure white banner raised high as it crossed the tens of thousands of troops who had crested the hill and blackened the foot of the mountain.

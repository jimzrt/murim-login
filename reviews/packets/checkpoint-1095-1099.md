# Checkpoint Review — 1095–1099

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

# Chapters 1095–1099

## Plot

The Nanman Beast Palace leaves its bloodied homeland to join the Murim Alliance and avenge its people, while the Potala Palace arrives at Xining with elephants and thousands of troops, joining Dark Heaven’s siege. The Blood Lord reveals that Jin Taekyung is the Lord of Heaven’s true objective and offers to spare everyone else if Taekyung leaves Xining, severs the sinews and meridians in all four limbs, and surrenders. He does not intend to honor the offer; he wants Taekyung to choose a fight that gives him a pretext to kill him.

The Blood Lord waits for a signal from a long-hidden agent among Xining’s defenders. Taekyung rejects a risky nighttime strike, then finally tells Jeok Cheongang about the ultimatum. Cheongheoja later confides that he failed to teach one of his Disciples properly. Taekyung realizes a Dark Heaven agent is hidden deep within the defenders, but does not identify the Disciple. Cheongheoja asks Taekyung a favor, whose nature remains undisclosed.

Meanwhile, Mu Song confronts his Master, Pa Ryun, for ordering the execution of captured imperial troops. He claims the Eldest Senior Brother and Elders serve someone else, but Pa Ryun knocks him unconscious before he can explain. A Yangtze River Channel League fleet prepares to meet thousands of unidentified allies near the river.

As a vast enemy force approaches Xining through torrential rain, Taekyung leads the defenders through the city. The battle begins with hundreds of ice spikes.

## Continuity

- Dark Heaven and the Potala Palace are allied at Xining. The Dalai Lama accepts the alliance’s unequal terms; the Palace still hates the Fire Gate Clan and expects Dark Heaven to destroy it.
- The Blood Lord offered to spare everyone else if Taekyung left Xining alone within a day, severed the sinews and meridians in all four limbs, and surrendered. The Blood Lord’s offer is not trustworthy, and he privately intends to kill Taekyung even if that means defying the Lord of Heaven.
- The Blood Lord expects thirty thousand reinforcements—the Yangtze River Channel League’s fleet and ten thousand Green Forest Alliance followers—within one or two days. A vast enemy force has now approached Xining, and fighting has begun.
- The Blood Lord awaits a signal from a hidden Dark Heaven agent within the defenders. Taekyung suspects the agent is one of Cheongheoja’s Disciples; the identity remains unknown.
- Cheongheoja asked Taekyung a favor, but Taekyung has not yet disclosed or fulfilled it.
- Taekyung believes the Lord of Heaven wants him more than anything, possibly more than the world; the reason remains unknown.
- The Nanman Beast Palace has left its homeland to join the Murim Alliance; Namho fears its departure may leave Sichuan exposed to enemies from Tibet.
- Mu Song disobeyed Pa Ryun’s order to kill captured imperial troops. Mu Song claims the Eldest Senior Brother and Elders serve someone other than Pa Ryun, but loses consciousness before explaining.
- The Yangtze River Channel League fleet was preparing to meet thousands of new allies near the river; their identity is unknown.

## Translation Decisions

- Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective.
- Retain “sinews and meridians” for 근맥.
- Render 달뢰라마 as “Dalai Lama” and 십이밀승 as “Twelve Secret Monks.”
- Keep Taekyung’s speculation that the Martial God may have crossed between worlds and treated Murim like a game unconfirmed.

## Durable state

{
  "active_continuity": [
    "Dark Heaven’s army surrounds Xining under the Blood Lord; the Potala Palace has joined its forces with elephants and the Twelve Secret Monks.",
    "Cheongheoja says he failed to teach one of his Disciples properly; Taekyung realizes a Dark Heaven agent is hidden deep within Xining’s defenders.",
    "Cheongheoja privately asks Taekyung a favor; its nature is not revealed before a day passes.",
    "A vast enemy force approaches Xining through torrential rain, and the battle begins with hundreds of ice spikes.",
    "The Blood Lord offered to spare everyone else if Taekyung leaves Xining alone within a day, severs the sinews and meridians in all four limbs, and surrenders; Jeok Cheongang believes the Blood Lord will break his promise.",
    "Taekyung believes the Lord of Heaven wants him more than anything, possibly more than the world; the reason remains unknown.",
    "The Potala Palace and Dark Heaven are allies, but the Palace has a deep, longstanding hatred of the Fire Gate Clan; the Dalai Lama accepts the alliance’s unequal terms.",
    "Namho fears Sichuan may be exposed to enemies from Tibet after the Nanman Beast Palace’s departure.",
    "The Fire Gate Clan’s leaders are unlikely to abandon Xining while their allies and civilians remain there.",
    "Mu Song disobeyed Pa Ryun’s order to kill captured imperial troops; Pa Ryun says the Eldest Senior Brother and Elders obeyed him without deviation.",
    "Mu Song claims the Eldest Senior Brother and Elders serve someone other than Pa Ryun, but loses consciousness before explaining.",
    "The Yangtze River Channel League fleet was preparing to meet thousands of new allies gathered near the river; their identity is unknown."
  ],
  "continuity_sources": [
    1098,
    1099
  ],
  "open_questions": [
    "Which of Cheongheoja’s Disciples is the hidden Dark Heaven agent, and what did Cheongheoja ask Taekyung to do?",
    "What will decide the battle for Xining, and will its defenders survive?",
    "Why does the Lord of Heaven want Taekyung, and what does he intend to do with him?",
    "Whom do the Eldest Senior Brother and Elders serve, and what was Mu Song about to reveal?",
    "Who were the new allies gathering near the river?"
  ],
  "safe_through": 1099,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 1095

# Chapter 1095

Bwooo! Bwooooooo!

The deep, resonant sound of a horn pierced Jin Taekyung’s ears, carrying across hundreds of yards. At that moment, he suddenly thought of something.

He was sure he’d heard a similar sound somewhere before.

In a damp, pitch-dark land thousands of miles away, at the very southern edge.

*…No way.*

A suspicion flashed through his mind like lightning. Eyes wide, Jin Taekyung stared in the direction the horn had come from.

And at last, he saw them.

Through a thick cloud of dust rising in the distance, enormous creatures came charging toward them. Even from this far away, he could clearly make out their great trunks swinging as they ran.

*Those are…*

They were none other than elephants.

The largest, strongest living creatures of all—not just among beasts, but among every creature that lived on land or in rivers.

The people of the Central Plains called them *xiang*—elephants—and regarded them as mysterious animals. But to a few people, Jin Taekyung among them, they were fairly familiar.

They’d spent a brief time with people who lived alongside countless animals, elephants included, and who trained and tamed them. When the elephants died, those people carved their beautiful tusks into horns.

“Nanman Beast Palace! The Nanman Beast Palace is here!”

On the nearby wall, Hyuk Mujin spotted the herd—hundreds of elephants by his rough estimate—and shouted, brimming with excitement.

“Do you see that, you bastards?!”

Barely fifteen minutes ago, Hyuk Mujin had only been able to stand on the wall, watching the fierce battle below and swallowing nervously. But not anymore.

“Come on, bring it on! Now we’re not so badly outnumbered!”

He had good reason to be sure of himself.

The Nanman Beast Palace had begun to move in earnest soon after the enormous upheaval caused by the Southern Heaven Demon Empress’s scheme was brought under control.

No, “move” hardly did it justice. This was a mass migration on a staggering scale.

They’d purged every diseased shoot that had grown within their ranks. And that wasn’t enough—they’d even abandoned the homeland where their ancestors had lived since time immemorial.

Beast Miao King Yayul Cheok was more furious than ever at Dark Heaven’s scheme, which had drenched Nanman’s jungles in blood. He grieved the death of his sworn brother Baeksang more than anyone. And at the same time, he was deeply moved by the outsiders from the Central Plains who had saved them from this enormous crisis.

Thus, with the Beast Miao King at their center, the Nanman Beast Palace became wholly united. They swore to join the Murim Alliance and avenge their people, then left their bloodstained homeland.

Every last one of Nanman’s tens of thousands of people went with them, along with the countless ferocious beasts they commanded.

And the fact that the Nanman Beast Palace’s forces—who should have been in Sichuan—had appeared here meant something else, too.

“The Nanman Beast Palace, the Sichuan Tang Clan, Qingcheng, and Emei must all have come together! You’re all dead now!”

At Hyuk Mujin’s shout, his fist clenched, the allies on the wall—who had been frozen stiff before Dark Heaven’s overwhelming forces—finally brightened.

“Waaah!”

“Reinforcements! The reinforcements are here!”

“Yeah, you bastards! Let’s give them a proper fight!”

The Nanman Beast Palace’s forces were said to be practically a small kingdom in their own right. And now they had three great sects with them, each representing the very heart of the martial world.

Even those who had already sensed defeat and resigned themselves to it, and those who had clung to hope while forcing down their unease, all let out a full-throated cheer as if they’d never felt that way at all.

But amid the wave of joy that swept over the wall, one person gazed at the approaching dust cloud in the distance with eyes that had somehow sunk even deeper.

*The Nanman Beast Palace, and the other three Sichuan factions, too? They couldn’t possibly have left Sichuan unguarded.*

Sitting on Taishan’s unusually high shoulder, Namho slowly retraced his thoughts as he watched beyond the wall with a seasoned gaze.

The Nanman Beast Palace’s strength. The current state of Sichuan’s Murim, already dealt a tremendous blow by the chain of events centered on the Western Heaven Demon Lord.

And why he’d thought they couldn’t come here.

*Sichuan is one of the largest regions in the world. Given the length of its front lines, the imperial army alone wouldn’t be enough. So how could they…?*

The world today was like a steep mountainside where even the boundary between Murim and the state had disappeared.

The snowball that was Dark Heaven had been rolling for half a century already. The enemy had become a boulder weighing ten thousand pounds, rolling down the snow-covered slope and on the verge of crushing the villages below.

No—the entire world.

That was why the Murim Alliance wouldn’t have been able to think of a way to rescue Qinghai under these circumstances.

If even the slightest gap opened, Dark Heaven would become a sharp awl and drive straight into it.

Not just to pierce the surface, but to reach somewhere deep inside, using that bizarre sorcery called a Moving Formation.

On top of that, the situation in Sichuan’s Murim was worse than anywhere else in the Central Plains.

More than bad—it was the worst it could be.

The only enemies they had to watch out for weren’t the ones who might appear like ghosts somewhere within Sichuan.

*If they really have abandoned their homeland to come save us, the enemies bordering Sichuan in Tibet could cross straight through Sichuan and head for the Central Plains…*

At that moment—

The countless thoughts tangled together in Namho’s mind, looping and colliding, vanished all at once.

A chill ran down his spine. As he froze, a low exclamation reached his ears.

“Damn, there are a lot of elephants gathered in one place. Seeing them from up high is quite a sight. Sure glad I stayed.”

Great Sir.

It was him.

Unlike Bow Saint, Cheongpung, and the other Supreme Peak masters, he had stubbornly held his position until now. He muttered in a carefree tone, like a spectator enjoying the view.

“Sure is unusual. I’d heard it was the kind of place where you’d be gasping for breath just standing still, but do all the people of Nanman shave their heads like that?”

Namho, who’d been staring blankly like a man in a daze, whipped his head around to look at Great Sir.

“What… What on earth are you talking about?”

“What do you mean? I’m just saying what I see.”

Great Sir tilted his head and pointed at the dust cloud slowly drawing nearer from hundreds of yards away.

From atop the wall, dozens of yards high, he could see what no one else could—not with anyone else’s eyes, anyway. His Supreme Peak eyesight let him pick out the scene.

No.

More precisely, he could see thousands of people wearing red and yellow robes, advancing with a herd of elephants at their head through the pale, hazy dust cloud, where it seemed impossible to make out anything a few feet ahead.

“Huh? Wait. Now that I look again…”

Great Sir stared hard at them, scratching his chin, then added:

“They kind of look like monks, too.”

At that moment—

A shout erupted from the lips of the old Hidden Shadow Pavilion agent, who was nearing eighty, so loud that even he was startled by it.

“You damn bastard! That’s the Potala Palace!”

And at the same time—

Bwooooooo!

To the deep, resonant sound of the horn, the Potala Palace’s army charged forward like mad, led by hundreds of elephants.



* * *



There was an undeniable gap between the modern world of the twenty-first century and this one.

Some things were similar. Others were a little different.

And the land people here called Xizang, thousands of miles from the Central Plains and classified as part of the Outer Lands, was closer to the latter, as far as I understood it.

Xizang.

In Murim, I alone knew its other name: Tibet.

And the Potala Palace—a religious group that had built its own little world there.

That was the identity of the enormous dust cloud that had suddenly appeared.

Bwooooo!

Hundreds of elephants charged like mad, trumpeting all at once.

Now that I could see them up close, their long, beautiful tusks were blackened, as if someone had deep-fried them. Their bloodshot eyes were completely out of control.

*Those things… are elephants?*

Watching them draw closer by the second, I realized it again.

They were different. On another level entirely.

They were nothing like the elephants I’d seen behind the bars at the zoo when I’d gone with my mom as a kid, or the ones I’d seen in Nanman.

Their size, their madness, their ferocity. Everything.

Dumbo the baby elephant I’d seen as a kid?

Give me a break.

If the original author had used these lunatics as inspiration, the cartoon I’d watched would’ve been called *He’s Just a Baby, but He’s Freaking Strong: Elephant Heavenly Demon’s Reign*.

Rumble, rumble, rumble!

The earth shook as if they really were using the Heavenly Demon’s Reign.

No—as if that weren’t enough, the ground was cracking apart.

Facing real-life versions of the giant elephants from that movie about little folk destroying a ring, Cheongpung murmured his verdict, half dazed.

“Whoa. I’ve never seen anything like that in my life…”

Neither have I, shit.

The words nearly slipped out of my mouth, but I barely managed to hold them back.

Why?

Simple.

Even without the Potala Palace rapidly closing the distance, Dark Heaven’s forces still surrounded us on every side, packed tightly around us even now.

“They arrived sooner than expected. How fortunate.”

The Blood Lord spoke with a relaxed smile.

“Of course, it’s the worst possible luck for you.”

I tightened my grip on the shaft of my spear instead of answering.

This was getting worse by the second.

We were already at a disadvantage, and now the Potala Palace from Tibet had joined Dark Heaven, too.

*They never cared about Sichuan in the first place.*

It wasn’t as if I hadn’t considered this possibility.

I’d just thought the odds were slim.

I wasn’t the only one. Most people thought so.

We believed Dark Heaven had drawn in the Potala Palace, which had been quietly staying in Tibet, to block the front lines in Sichuan and stop any reinforcements from reaching Qinghai Province.

But we were wrong.

What the Blood Lord—or rather, the Lord of Heaven behind him—wanted from what was happening in Qinghai wasn’t some foothold from which to advance into the Central Plains.

*It was me. I was the one he wanted.*

As the realization finally came, a huge rock seemed to press down on one corner of my chest.

So heavy it made me ache.

“Why?”

The brief question slipped from my lips before I knew it.

But the Blood Lord understood what I meant and answered readily.

“Do you think a fishing rod cast over a lake knows what its owner is thinking?”

“What?”

“I don’t know, either. I only do as my master commands. If he’d had them attack Sichuan, they might have opened a route into the Central Plains… but the Lord of Heaven had other ideas.”

“…”

“Don’t worry. I’ll keep my promise to spare you today. But understand this: you’re already caught in a net. One you’ll never escape.”

And then, right after that—

The Blood Lord’s low Sound Transmission pierced my ears.

*I’ll give you one day. If you sever your Sinews and Meridians and surrender of your own accord within that time, I’ll spare everyone but you.*

The Blood Lord slowly raised a hand and curled his lips into a smile at me, frozen in place.

*I swear by the name of the Lord of Heaven, that person who is my one and only light and sky. This is my last mercy—and the only way to save your people.*

That was the end of it.

As the encirclement parted at the Blood Lord’s gesture, the scornful smile on his lips stabbed into my chest.
## Chapter artifact 1096

# Chapter 1096

Rumble, rumble, rumble.

The enormous, heavy iron gates of Xining slowly opened their mouths.

The Grand Mage watched the enemy’s backs as they passed through the encirclement, which had parted to either side at the Blood Lord’s signal, and headed for the gates. Then she spoke.

“Don’t you think you let them go too easily?”

“Maybe I did. But…”

The Blood Lord replied in a low voice, then nodded toward the towering city walls.

“If we’d fought them head-on right then, our losses would’ve been considerable, too.”

The Grand Mage had to admit he was right, at least to a point.

Qinghai was a frontier among frontiers, a province prepared since ancient times to stand against any foreign invasion.

Perhaps that was why its stone walls, built from enormous blocks of dressed rock, were sturdier than anything in the Central Plains. Silver arrowheads already glinted atop them.

And beyond Xining’s slowly opening gates, a forest of spears and blades stretched as far as the eye could see.

“Cornered prey fights all the harder. They still have teeth to bite with.”

Even a lowly rat would charge a cat if it thought the situation was desperate. How much more would those people?

And there were no fewer than seven Supreme Peak masters among them.

No—eight, if they counted the mysterious Great Sir who had never come down from the walls.

Then there were the Qinghai martial artists and imperial troops who had gathered in Xining early, with barely any losses. The Blood Lord’s judgment hadn’t been far off.

Of course, the Grand Mage thought there was another, far more decisive reason he’d made that choice.

*He wasn’t certain. He wasn’t certain he could capture Jin Taekyung as that person wished—or, for that matter, that they could win outright.*

But the Grand Mage didn’t say the thought circling in her mind aloud.

She could hardly stand the Blood Lord, but there was no need to touch a nerve when they shared the same master and goal.

At the same time, she could partly understand why he’d let Jin Taekyung and the other Supreme Peak masters leave without resistance.

“Well, it’s a shame, but there’s nothing to be done. I wasn’t the first to be entrusted with Qinghai’s affairs by that person.”

“That’s unusual. I never expected to hear you say that.”

“I can separate business from personal matters. I could feel it, too. That would’ve been a difficult battle.”

There were levels even among those who had reached Supreme Peak.

And in that regard, the seven Supreme Peak masters they’d just surrounded were far beyond ordinary.

Though Jin Taekyung’s exploits had somewhat overshadowed him, Cheongpung, the Huashan Divine Dragon, had martial talent so extraordinary that it wouldn’t have been strange to call him the greatest in history.

Perfected Being Hyeoncheon and Cheongheoja, who led the venerable Daoist lineages of Kongtong and Kunlun.

The Bow Saint and Slaughter Saint, who needed no embellishment—and the Fire King Jeok Cheongang, their equal.

And finally, the Blazing Flame Divine Dragon Jin Taekyung, who had proven through his every action that his very existence was a variable.

Looking at that overwhelming, dazzling lineup, even the Black Ghosts—nearly immortal as they were—seemed to fade into the background.

“If a battle had broken out, those things would’ve been wiped out, regardless of whether we survived.”

The Grand Mage gestured toward the silent Black Ghosts, then added:

“Though one of them has already melted away without even leaving a shape behind.”

Jeok Cheongang’s full-strength strike had been that powerful. It had even broken through part of the defensive magic she’d cast.

“And there’d be no question of it if the Bow Saint and Slaughter Saint joined in. Besides, there’s something about Jin Taekyung that even I can’t quite understand.”

In the Murim world, where the strong ruled above all, power followed an honest logic.

The strong devoured the weak; the weak were trampled by the strong. That was only natural.

But from what the Grand Mage had seen, there was one person—Jin Taekyung—who stood farther outside that logic than anyone.

Even if he’d received help from those around him whenever he faced a life-or-death crisis, defeating four Demon Lords and a Demon Empress hadn’t been mere luck.

It was enough to make her understand why people called him the Chosen One.

“That must be why. His special nature is what makes that person so obsessed with him.”

At the faint note of wonder in the Grand Mage’s voice, the Blood Lord’s lips twisted.

*Obsessed. Is that what it is?*

As the thought turned over in his mind, he watched the gates slowly closing.

More precisely, he watched Jin Taekyung’s back disappear between them.

And suddenly, he remembered what he’d said moments before.

*Do you think a fishing rod cast over a lake knows what its owner is thinking?*

Those words hadn’t been meant for Jin Taekyung alone.

They were a self-mocking question he’d asked himself—and a plaintive complaint addressed to the Lord of Heaven, who wasn’t here.

*Why is that brat special to you? Why, exactly?*

At that moment, the person the Blood Lord most wanted to kill wasn’t Mae Jonghak, who had taken his arm from him once, nor Jeok Cheongang.

It was Jin Taekyung.

A greenhorn who’d grown into a towering tree in barely two years.

But even though he was no longer a bright yellow sprout the Blood Lord could crush with one step, and now had deep roots and thick branches, his master still hadn’t allowed his servants to cut him down.

*Lord of Heaven. What is it you truly want? This foolish servant cannot begin to guess.*

A fishing rod.

Even if it broke under the strength of the great fish that had taken its bait, it could simply be replaced.

The three words he’d spoken of his own accord, and the meaning they carried, weighed unusually heavily on the Blood Lord’s heart.

That was when it happened.

Bwooooo!

A long blast of a horn rang out. The Potala Palace’s army slowed and came to a halt some sixty meters away.

Among the hundreds of elephants standing like iron towers, thirteen—each the largest and most lavishly adorned—moved forward.

Thud. Thud.

A massive shadow fell across the Blood Lord’s face as he slowly lifted his head.

The elephants reached him, their heavy footfalls rumbling. A voice came down from atop their heads.

“It has been a long time, donor.”

The clumsy Han speech would have drawn a snort from anyone in the Central Plains.

But the mighty internal energy and imposing authority in that voice belonged only to the grand master of a sect—and it carried unmistakable anger.

“And yet…”

With a sharp rush of air, thirteen figures dropped to the ground.

At their center stood an old monk, slender and bony, as thin as a withered tree.

“If this humble monk has not mistaken what he sees, then I believe a convincing explanation is in order.”

The old monk who ruled Xizang like a kingdom—the Potala Palace’s Palace Lord, known by their ancient custom as the Dalai Lama—fixed his piercing gaze on the Blood Lord.

“Why did you let them go? I may be old, and my eyes may be failing, but even from a distance it was clear they were no ordinary people.”

Waking from his thoughts, the Blood Lord turned to look at the gates, now firmly shut.

Then he smiled warmly at the Dalai Lama, who had brought a substantial force to join them.

“As expected of the Palace Lord. You saw them clearly.”

But even at the Blood Lord’s unusually friendly manner, the Dalai Lama didn’t smile.

One of the decisive reasons the head of that deeply insular religious sect had accepted Dark Heaven’s proposal decades ago and formed an alliance with them…

And one of the main reasons he’d gathered every last force in Xizang and brought them all the way to Qinghai…

…was here.

“Then forgive this old monk for asking, just in case.”

The Dalai Lama continued, his tone so cold there wasn’t a trace of clumsiness in it.

“Among the enemies you just sent back, were the people I’ve been searching for?”

At that very moment, the Grand Mage’s lips moved behind her tightly woven silver-white veil.

*I’m only saying this in case, but… don’t forget. Until we achieve our goal, the Potala Palace is a rather useful card to have.*

Before he could answer, the Grand Mage’s warning reached his ear first. The Blood Lord twisted his lips without meaning to.

*Our goal?*

Ordinarily, he would’ve let the words pass without a second thought. For some reason, right now they struck him as absurd.

She, too. And he, too.

They were only fishing rods, after all—things someone could replace whenever they pleased.

*My goal has been the same from the beginning. To serve that person with body and heart, and help him rule as the master and father of all under heaven.*

But why?

Why on earth was he suddenly thinking that his master, the great Lord of Heaven, wanted not the vast world, but one young man?

“Ha.”

A quiet laugh escaped him before he could stop it.

At the sight of the Blood Lord, the Dalai Lama’s eyes sank further.

“I’m still waiting for an answer.”

The Blood Lord replied, amusement in his voice.

“Surely you’ve already guessed.”

“Does that mean…?”

“That’s right. The Fire King Jeok Cheongang. And the Blazing Flame Divine Dragon Jin Taekyung. The Fire Gate Clan’s scions you’ve been searching for so desperately were among them. Ah, come to think of it…”

He pointed with a straightened finger at the spot where the Dalai Lama stood, then added:

“I believe they were standing right where you are now. Though, of course, that was only moments ago.”

“……!”

“……!”

The air around them shifted violently.

It was the aura emanating from the Dalai Lama—and from the Twelve Secret Monks, the Potala Palace’s finest fighters.

“You let them go so easily? Even knowing how much I—how much we—hate the Fire Gate Clan?”

The Dalai Lama’s voice suddenly spilled from his lips, as dry as a desert of burning sand.

At that moment, the ruler of Xizang’s vast martial world was truly furious.

The Fire Gate Clan.

A cursed name impossible to forget, known to every Secret Monk of the Potala Palace.

They were the ones who had transformed the Potala Palace from a Buddhist sect—known for being more belligerent than necessary—into a theocratic state with formidable martial power.

“How dare you break your promise? What in the world is this?”

“Well, now…”

The Dalai Lama glared at him with a frostbitten aura, and his familiar use of casual speech was now entirely natural. The Blood Lord gave a short laugh.

“Don’t worry. I remember it clearly: that heartrending story from two hundred years ago, and the unbreakable promise we made to each other.”

“What?”

The Dalai Lama’s eyes widened at the casual reply. The Blood Lord continued in a low voice.

“But it seems you’ve forgotten all about it.”

“Forgotten? What are you talking about?”

“You know better than anyone how much help you received from that person in building the Potala Palace you have today.”

“That…”

The Dalai Lama bit down on his lip, unable to continue. The Blood Lord clicked his tongue softly.

“As I said, I always keep my promises. If you help capture Jin Taekyung in a meaningful way, I’ll hand that old man, the Fire King, over to you—and give you a generous reward besides.”

The Dalai Lama was silent for a moment before speaking heavily.

“How can I believe that?”

“What, you don’t trust me?”

“I trust that person. But you let them go right before my eyes, despite the perfect opportunity.”

A sneer touched the Blood Lord’s lips.

The Dalai Lama’s distrust didn’t offend him. He simply found it laughable that the man genuinely believed that.

Dark Heaven had given the Potala Palace its full support, but even so, the strength the palace had built up was undeniable.

The Dalai Lama’s own martial prowess, the best of them all, went without saying. Even against one of the Ten Kings other than Jeok Cheongang, he wouldn’t be outmatched.

But…

*That’s all you are.*

It wasn’t a question of martial skill.

It was a question of the size of one’s inner self. Of the person one was.

That was why, unlike the Grand Mage—who already understood what the Blood Lord had expected when he let them go and said nothing—the Dalai Lama regretted losing the great fish right before his eyes.

“Do you still not understand?”

“What is it I’m supposed to understand…?”

“I only wanted to make sure of everything. To leave not even the smallest opening for them to slip through.”

The Dalai Lama was about to say something when he suddenly realized something and opened his eyes wide.

“Could it be…?”

The Blood Lord nodded without a word.

If his guess was right, it would be today.

The Yangtze River Channel League’s hundreds of ships would finally enter the Yellow River tributary leading to Qinghai, and the Green Forest Alliance would meet them with ten thousand followers who had joined in advance.

“Another day, two at most. This battle will be over within that time.”

A total of thirty thousand reinforcements would cut through the swift current and reach Qinghai, sealing even the tiniest gap.

They were the final key to ensuring victory in this battle.

That was why he’d given Jin Taekyung a day to think, too.

A promise?

He’d never intended to keep it in the first place. But deep down, he hoped Jin Taekyung wouldn’t do something foolish and sever the sinews and meridians in his own arms and legs.

Only then…

Only if Jin Taekyung resolved to fight to the death would the Blood Lord have a reason to kill him.

*Lord of Heaven, forgive me. Even if you do not wish it, my actions are born only of loyalty.*

As if confessing his sins, the Blood Lord murmured to himself, then slowly parted his lips.

“So…”

He spoke to the Dalai Lama, who was looking back at him with a far brighter expression than before.

“Shut your mouth. If you speak down to me again, I’ll tear it off your face.”

“……!”

Watching the Dalai Lama freeze in place, the Blood Lord laughed wildly.

Being treated like a fishing rod by someone else was enough to bear once.
## Chapter artifact 1097

# Chapter 1097

The moment he met the Blood Lord’s wild smile, the Dalai Lama felt a chill run up his spine.

*What in the world is this man?*

He was different. In every way.

There was something about the man before him that stirred the primal fear every human being carried within them.

A darkness as deep as the abyss, enough to send a shiver through even the ruler of Xizang’s vast lands.

A predator.

The three words flashed through his mind. The Dalai Lama’s trembling lips parted.

He looked at the Dark Heaven followers who had surrounded him and the Twelve Secret Monks as if to enclose them.

“This humble monk… has been discourteous.”

For a moment, he’d forgotten.

What sort of man the Blood Lord was. Who stood behind him.

But the instant the Blood Lord bared the fangs he’d kept hidden, the Dalai Lama finally remembered the reality he’d let slip from his mind.

Who was weak, and who was strong.

If an irreparable conflict broke out at this moment, which side would be devoured?

That was why the king of the theocratic state that ruled Xizang had no choice but to bow his head slowly.

“I swear, I had no intention of insulting someone the Lord of Heaven favors. It’s only that I was troubled, and made a mistake…”

“A mistake.”

The Blood Lord cut off the Dalai Lama’s words and licked his lips with a red tongue.

Like a beast savoring the sight of its prey.

Then he smiled gently at the Dalai Lama.

“I understand. Anyone can make a mistake now and then. Once.”

The meaning in the Blood Lord’s quiet final words was unmistakable.

Once. Just once.

He wouldn’t tolerate a second mistake.

The Blood Lord’s respectful manner had returned as though nothing had happened, but his attitude was the exact opposite. The Dalai Lama had no choice but to grit his teeth and accept it.

“Thank you for saying so.”

“Now, there’s no need to be so formal. We’re comrades working together toward a great cause, aren’t we?”

“…You’re absolutely right.”

Of course, the Dalai Lama knew how hollow those words were.

The balance of power had been decided decades ago, when he took the hand the Lord of Heaven had offered.

This was the magnanimity only the strong could show—a carrot tossed to him as a gesture of goodwill after a crack of the whip.

But by now, only one choice remained before the Dalai Lama and the Potala Palace.

They had to accept everything and acknowledge it.

Only then could they avenge the old grudge handed down from their predecessors—and survive in the new world Dark Heaven would one day rule.

“The Potala Palace will do everything it can to repay, in some small measure, the grace the Lord of Heaven has bestowed upon us. However…”

“However?”

As the Blood Lord’s eyebrow twitched, the Dalai Lama added in a deeply subdued voice:

“I trust you’ll honor your promise.”

The Blood Lord, who had been staring at him as if to see right through him, clicked his tongue.

“So that’s what you were going to say… Don’t worry. The Fire Gate Clan’s lineage will end right here, in Xining.”

“I don’t doubt you, donor, but couldn’t they escape Xining and flee to the Central Plains before the Green Forest Alliance and Yangtze River Channel League have completely sealed off the rear?”

“Escape? Did you just say escape? And you mean the Fire King and Jin Taekyung, of all people?”

Before the Dalai Lama could answer, the Blood Lord laughed aloud and continued.

“Palace Lord, you hate the Fire Gate Clan more than anyone, yet you know nothing about those people.”

“They’re a small handful of people. If it’s just those two, there are more than enough opportunities to get away. Even the Fire Gate Clan’s reckless fools might think about living to fight another day when they’re at such a disadvantage.”

He was right.

They weren’t talking about the tens of thousands of troops huddled in Xining, or its hundreds of thousands of people. They were talking about a tiny handful.

And if that handful consisted of none other than the Fire King Jeok Cheongang and the Blazing Flame Divine Dragon Jin Taekyung, they could slip through the rear right now and tear a hole in the encirclement.

But despite the Dalai Lama’s concerns, the Blood Lord could only laugh even harder.

“Impossible. Absolutely impossible.”

“What makes you so sure?”

“Don’t you know? You just said it yourself.”

“What do you mean—”

The Dalai Lama’s question was cut short. The Blood Lord suddenly stopped laughing and spoke in a hoarse voice.

“Idiots who don’t know up from down. That’s the Fire Gate Clan.”

“……!”

“Master and Disciple alike—they’re all the sort who don’t give a damn about their own lives. And if tens of thousands of allies and hundreds of thousands of civilians are still here… well, there’s nothing more to say.”

If those two had wanted to live to fight another day, they wouldn’t be in Xining right now.

No. Their entire history up to this point would never have happened.

Once they lost their temper, they’d charge even if their opponent were the Demonic Cult—or the Jade Emperor himself. And even when their lives were on the line, if there was something they had to protect, they protected it.

Some people, the Blood Lord among them, might mock it as a stupid stunt rather than a chivalrous act.

But that was the Fire Gate Clan.

“I’ll say it one last time: they will never leave Xining. I’ll stake my life on it.”

As he answered with more conviction than ever, the Blood Lord suddenly remembered.

A year ago, in a valley on Mount Song drenched in blood, how desperately that young pup had fought when he dared to face him.

And today, in the eyes of the young beast he’d faced once more—eyes that held a fire too fierce for him to call it a young pup anymore.

At last, he understood for certain.

What kind of person that boy—the Blazing Flame Divine Dragon Jin Taekyung—was.

And at the same time, he made up his mind.

Even if it meant defying the Lord of Heaven’s command, he would kill the boy and eliminate the threat he posed.

*Even if someone else in there smuggles him out the back, it won’t matter.*

Farmers worried about crops being swept away by the rain kept their eyes on the sky. Everyone else only realized storm clouds had gathered when raindrops fell on their heads.

The peace that had lasted more than fifty years was long. And the storm clouds that had crept slowly toward them were now overhead.

They still hadn’t noticed—not even now, as Dark Heaven’s hidden sword, planted deep within their ranks long ago, pierced their flesh.

*The moment I get the signal from inside, I’ll strike and finish this in one go.*

The Blood Lord smiled faintly, then lifted his head and looked at the sky.

In the dark, murky heavens, raindrops began to fall one by one, promising an unprecedented downpour.

An omen of the storm that would sweep away everything in Qinghai.



* * *



Tap. Plip.

As I felt the sudden raindrops wet the top of my head, I thought:

*For a victory celebration, this is one hell of a damp affair.*

Though we’d ended up fighting an unexpected battle, our side had achieved a great deal in the short time it lasted.

We’d taken down hundreds of enemies, by my estimate—and among them was the Black Ghost who’d been reduced to ashes by Jeok Cheongang’s full-powered strike.

*Of course, that was only a fraction of them.*

I kept the thought to myself and stared beyond the wall at the massive army that had turned the land black.

Hundreds fewer, but thousands more.

For a moment, the balance of power had edged the tiniest bit closer to even. With the Potala Palace’s arrival, it had tipped further against us than before. The weight of it pressed down on one corner of everyone’s heart, mine included.

“Maybe… we’ve already missed our chance.”

Watching the enemy build an ever tighter, more impregnable encirclement, Bow Saint continued in a heavy voice:

“Since we were already committed, we should’ve finished things before the Potala Palace arrived. We might’ve had a chance then.”

At that one sentence, which put into words what everyone already felt, someone who’d been standing with his arms crossed in silence spoke up.

“Even so, we have a good chance if we take advantage of the darkness and eliminate their entire leadership.”

If Hyuk Mujin had said that, I’d have strung him up by his ankles and thrown him over the wall. Thankfully, we weren’t in that unfortunate situation.

Those words had come from none other than an assassin hailed as the greatest of all time.

But unlike the others, who waited for the rest of his plan with hopeful eyes, I shook my head without hesitation.

“Absolutely not.”

The Slaughter Saint asked:

“Why do you object?”

“Can I be honest?”

“When have you ever been anything else? Go on.”

“It’s simple. We’d go there just to die like dogs.”

“……!”

The mood sank in an instant. The Slaughter Saint looked at me with a deep, searching gaze.

“That’s beyond honesty. It’s almost a provocation.”

“I know I like joking around and I’m good at provoking people, but that doesn’t apply to allies on the same boat. You know that already, don’t you?”

“I learned something by facing them myself just now. If I went in, there’d be a chance.”

“How much of a chance?”

“One in ten.”

The Slaughter Saint answered as if the slim odds were no big deal, then looked at the rain, growing heavier by the moment.

“One in five, if the heavens lend a hand.”

“That’s all?”

“That’s as much as one in five. Considering what we’d gain if we succeeded, staking my one life would be a bargain.”

He was right.

Even so, I could only smile bitterly.

“If we stood to gain anything at all, I wouldn’t have called it dying like dogs.”

“Now that they know I’m here, I expect them to prepare. They might even set every Black Ghost they have left to guard their leaders.”

“I know. And I know you’ve considered all the other possibilities, too.”

“Then why?”

“Because it’s obvious.”

Naturally, I wasn’t the one who answered.

Jeok Cheongang had been silent all along. Now he spoke up and continued as everyone turned to look at him.

“Dark arts—no, magic. When it comes to that cursed stuff, even the greatest assassin of all time would be as good as deaf and blind. Am I wrong?”

I nodded.

No—more precisely, before I could even nod, Jeok Cheongang grabbed my shoulder and made me move.

And before I could ask why he’d done that, the low Sound Transmission that slipped into my ear left me with no choice but to fall silent.

—So, are you really not going to tell me until the very end?

Jeok Cheongang stared at me, his gaze sunk deep.

—What nonsense that bastard the Blood Lord was spouting at the last moment.
## Chapter artifact 1098

# Chapter 1098

The human body held more information than anyone could imagine.

And masters who had reached the limits of their five senses could read and interpret what that information meant from the slightest change in an opponent’s expression or movement.

Just like right now.

—So, you’re planning to keep quiet until the very end?

A low Sound Transmission. Eyes sunk so deep I couldn’t guess what lay beneath them.

That alone was enough.

I hadn’t managed to completely hide my momentary agitation, and the shift in my eyes was practically a confession.

—At the last moment, what kind of nonsense did that bastard the Blood Lord spout?

As Jeok Cheongang’s deep gaze seemed to see through everything, his Sound Transmission coming as if he were spitting out the words, I suddenly realized something.

Even if he hadn’t been one of the world’s foremost Supreme Peak masters, even if I hadn’t let my agitation show, nothing would have changed.

Like the branches of a tree grown from the same root, connected even when they spread in different directions, my old Master had already seen straight through his Disciple’s heart.

So there was only one answer I could give.

—Maybe your hearing got better because you got younger.

I’d be lying if I said I hadn’t anticipated this situation at all.

Jeok Cheongang had once overheard the Sound Transmission of the Roaring Fury Swordsman, who’d come to the Jin Family of Taiyuan and threatened me, then beaten him to a pulp.

But the Blood Lord’s martial prowess was so formidable that comparing him to the Roaring Fury Swordsman was almost embarrassing.

I’d assumed that even Jeok Cheongang couldn’t read the Sound Transmission of someone who’d grown even stronger since the Shaolin Bloodshed. And I’d secretly felt relieved that, ever since we returned inside the city, Jeok Cheongang hadn’t let on that anything was wrong.

Of course, looking back now, that answer had been half-right at best.

“Answer me. Now.”

Jeok Cheongang’s voice suddenly slipped past his lips.

Feeling dozens of pairs of eyes turn toward me at once, I took a deep breath.

And at last, I told him the truth he wanted to hear.

“You were right. The Blood Lord made me an offer.”

“What offer?”

“He said I had one day, starting now, to leave the city alone, sever the sinews and meridians in all four of my limbs myself, and surrender.”

“……!”

“……!”

An invisible ripple shivered through the air.

As murmurs rose from the people who were only now grasping the situation, Jeok Cheongang spoke with a face gone stiff as a stone statue.

“So, he promised everyone else’s safety in exchange for your life?”

As expected.

I nodded with a bitter smile.

“Yes.”

“Why… didn’t you tell me sooner?”

“Because I was thinking it over. And if things hadn’t come to this, I would’ve kept thinking about it.”

“Thinking it over? You mean that ridiculous load of crap?”

“The Blood Lord himself swore on the Lord of Heaven’s name. If he kept his word, it’d be a bargain more than fair for one life. Wouldn’t you agree?”

The Slaughter Saint, who’d just had his own words thrown back at him, frowned when he met my gaze.

“Yes, perhaps. But you’re overlooking the most important thing.”

“What’s that?”

“Trust. Whether you can trust the person you’re making a deal with.”

The Slaughter Saint answered without hesitation, then continued:

“They’ll never keep their promise. If the gamble I proposed earlier rests on confidence in my own skill, you’re trying to make a deal with someone you can’t trust in the first place.”

I bit my lip in silence.

Honestly, I didn’t know.

No—I might have known already, somewhere in the back of my mind.

That Jeok Cheongang, that the Slaughter Saint, was right about everything.

That the Blood Lord’s thick killing intent before he made his final offer, and his vow that he would kill me, had never been empty words.

But there was another reason I couldn’t help considering this absurd deal.

“The Lord of Heaven’s goal right now is me. And me alone.”

Looking back, the Lord of Heaven had always wanted me.

And for a very long time.

Otherwise, he wouldn’t have left me alone all this time as I grew stronger by the day—so quickly that the saying “treat someone with new eyes” couldn’t keep up—even though I kept standing in the way of his path to ruling the world.

Why the Lord of Heaven wanted me, exactly?

I didn’t know.

But there was one thing I thought I could make out, however dimly.

“To him, I’m more important than anything else right now. Maybe…”

My voice trailed off.

At the same time, I felt the hairs all over my body stand on end and let out the breath I’d been holding.

“Even more than this entire world.”

“……!”

“……!”

The truth, too clear now to hide, was chillingly cold and dark.

Like the air around us, frozen in an instant.

And like the other reason I couldn’t help agonizing over this.

Whoooosh.

With the racket of rain pounding all around us, I turned my head toward somewhere far to the east.

The rain still burrowing into my ears sounded, for some reason, like water parting around the prow of a ship.

*They’re coming.*

I couldn’t see them.

But I could feel them.

The final wave, ready to snap the scales of this already-lopsided battlefield—and sweep away every last person in Xining.



* * *



Sometimes, there are nights like that.

When the birds, insects, and even fish are asleep, and only the moon shines bright in the sky.

The fishermen of the Yangtze liked nights like those.

Whether they cast their nets or not, whether they were fishermen or not, on those nights everyone went down to the river. They’d swim and set out in boats, filling their cups with cheap strong liquor and drinking their fill.

Grateful for the vast river that had given them so much, they’d row across the moon’s reflection on the water, singing and enjoying a little time for themselves.

There was a time.

There really was.

*Splash!*

Deep in the night, the pitch-black river split open.

Before the moon emerged from between the dark clouds and could even see its face reflected on the water, hundreds of prows covered the river and forged ahead.

Fiercely. Without end.

It was like watching a city move, a wave that nothing could stop.

A mighty current that defied the order of heaven and dreamed of defying Heaven itself, one not even the Son of Heaven—the father and ruler of all under it—could stop.

And the countless flags fluttering from the swollen sails had long since become objects of fear in their own right.

“What brings you here?”

The old man, leaning against the prow, had silently looked up at the five characters inscribed on the flag in bold, imposing strokes: Yangtze River Channel League. Now he slowly turned and added:

“And alone, without even sending word.”

At the Seafaring King Pa Ryun’s quiet voice, the subordinate who’d brought the unexpected visitor lowered his head, face stiff.

“My apologies, Alliance Leader. It’s just—”

“Enough.”

Pa Ryun cut him off with a single word, then addressed the uninvited guest standing in the shadow of the mast.

“I said I’d punish anyone who neglected their duties before we reached our destination. Have you already forgotten?”

The visitor shook his head.

“No.”

“Then did you think my Disciple would be an exception?”

“No.”

“Then?”

Thud.

With a heavy step, Ship-Fire Boy Mu Song emerged from the shadows and answered:

“I came to watch the moon with you, Master.”

Watch the moon.

Pa Ryun found himself glancing up at the cloud-filled sky. His voice remained gruff.

“By the rules of the League, you’ll receive thirty strokes with the rod on deck at dawn.”

Mu Song hesitated, then immediately objected.

“Wasn’t it twenty?”

“You disobeyed an order and spouted nonsense on top of it. You knew what you were getting into. Thirty.”

“But—”

“Forty.”

Mu Song fell silent. Then Pa Ryun turned to the subordinate, who was still standing there, and added:

“You neglected your duty, too. Ten strokes.”

“B-But, Alliance Leader—”

“Leave us. This matter will go unpunished.”

The Yangtze River Channel League’s corporal punishment was no ordinary beating.

The strokes were delivered with an oar made of hard birchwood and soaked in water—by a Peak master in charge of discipline.

The master didn’t use internal energy, but even ten strokes were enough to leave your backside raw and break several bones. You’d be bedridden for a couple of months.

But Seafaring King Pa Ryun’s strictness made no exceptions—not for his own Disciple, and not for a subordinate who’d followed him for over thirty years.

In the end, the subordinate left without another word. By the time his presence had completely faded, Pa Ryun, still watching the river split around the ships, spoke abruptly.

“Perhaps it ought to be fifty.”

“What?”

“It’s obvious whose fault this is. You’re ten years younger and in better shape, so take the extra strokes for him.”

Mu Song stared blankly at his Master, then nodded with a bitter smile.

“I will. If it’s that many, I won’t be able to move for three months. Maybe that’s for the best.”

“There’s a barb in your words.”

“Then you heard me right.”

Mu Song took a deep breath and suddenly dropped to his knees.

*Thump.*

“Please—please reconsider your decision, just this once.”

Before the echo had even faded, he struck his forehead against the deck and added:

“No matter how I look at it… this isn’t right.”

But even as his Disciple suddenly prostrated himself, the Master kept his eyes on the Yangtze.

“Not right, you say.”

“I know it sounds absurd. I’ve been a bandit since I was a snot-nosed kid, too.”

Pillaging had been his trade.

Ever since he’d taken charge of Water Dragon Stronghold at thirty, he’d led a large family of followers, taking what belonged to others and sharing it with them.

But… he’d never once wanted something like this.

“The Yangtze is being stained with blood. And it’ll keep happening. I mean that vast, blue river we all love.”

Mu Song’s voice had begun to tremble. Pa Ryun suddenly spoke.

“Is that why, in the last battle, you were the first to capture so many imperial troops?”

“You knew…?”

“Do you think there’s anything that happens on the Yangtze that this old man doesn’t know about?”

“……!”

“It wasn’t only you. The Third Disciple and quite a few of the senior members pulled similar tricks. Should I call it insubordination?”

“Master, this isn’t insubordination. We only—”

“How dare you raise your voice in whose presence?”

Pa Ryun turned his head and looked down at Mu Song, his eyes gone cold.

“This old man ordered them killed, and you should have killed them. They were people it was all right to kill.”

“No. There was no need to kill them.”

If they’d been strong, Mu Song might not have shown them mercy.

He had to protect himself and his followers, too.

But the imperial troops he’d faced that day had been so weak. Weak enough to make him afraid to see blood.

“That—that wasn’t a battle. It was a massacre.”

“Yes. That’s what this old man wanted.”

“……!”

“But in the end, the only ones who carried out my orders without the slightest deviation were your Senior Brother and the Elders.”

Hiss.

Mu Song shuddered without meaning to.

He had to stop.

Given his Master’s anger, the right thing to do was stop.

Right now.

But even with that overwhelming aura bearing down on him, Mu Song clenched his teeth and endured it.

Thinking of someone who flashed through his mind at that very moment.

A man whose martial arts were insanely strong and whose personality was a total bastard—he’d put Mu Song through all kinds of hell. But he’d also shown him that even a bandit like himself could pursue chivalry.

Jin Taekyung.

“D-Do you still not understand?”

Under the weight of his Master’s mighty aura, Mu Song gasped for breath and struggled to continue.

“Eldest Senior Brother—and those damn Elders, too. They weren’t following you.”

“What?”

“The people they’re loyal to are someone else. Maybe they have been for a long time, M-Master…”

*Thump.*

That was as far as he got.

As far as he could withstand the force of Pa Ryun, one of the Ten Kings.

His Disciple had lost consciousness before he could finish speaking. Pa Ryun looked down at him with a deep gaze, then turned back to the river and muttered.

Or, more precisely, to the tributary of the Yellow River, whose waters had begun to turn the color of brown earth.

“Yes. Better stay just as you are. Even if you stepped in now, nothing would change. It would only rush toward its end.”

Just then, moonlight poured down to the ground as the moon reappeared between the clouds.

At the same time, countless figures began gathering in the grass not far from the riverbank.

Thousands—no, tens of thousands of shadows.

A voice, its laugh as faint as moonlight, spoke.

“It seems the moon’s looking rather fine tonight after all.”

Hundreds of ships bearing the Yangtze River Channel League’s flags began preparing to welcome their new allies.
## Chapter artifact 1099

# Chapter 1099

That night was unusually long.

Maybe it was because the torrential rain showed no sign of letting up. Maybe it was because the dark clouds still hadn’t budged, even after several shichen had passed.

And the meeting, which had dragged on in that suffocating atmosphere, didn’t wrap up until the hour of the Rabbit.

“Now, all that remains is one final battle. I ask each Great Hero here to get plenty of rest and fulfill the duties entrusted to you.”

My tone was much more formal than usual.

Yet among the leaders gathered here, not a single person seemed uncomfortable with my unfamiliar formality or with such a distant junior presiding over them.

Anyone liable to cause even the slightest trouble had already been removed from the picture.

The eminent masters and generals of Qinghai Murim treated me with respectful, resolute courtesy, then left to fulfill their respective duties.

There was one exception: an old Daoist still tilting a teacup that had gone cold quite some time ago.

“Nothing tastes worse than cold tea. What do you say? Want this old man to warm it up for you?”

Jeok Cheongang had been on his way out, but stopped and tossed out the question. The old Daoist shook his head.

“Cold things have their own flavor, just as hot things do. Besides…”

The old Daoist answered in a voice as airy as drifting clouds, then smiled at me.

“Must I trouble Senior for help when I could simply ask this young Fellow Daoist here?”

Anyone else might have thought he was just playing with words.

For Cheongheoja—the old Daoist, or rather the Sect Leader of the Kunlun Sect—warming tea with Samadhi True Fire would have been child’s play.

But Cheongheoja’s answer had been a roundabout way of refusing the offer.

He still had something to discuss with me alone.

And Jeok Cheongang wasn’t the sort to miss that.

“You’re talking like a Daoist who grabs at clouds. Do as you please.”

Jeok Cheongang gave a quiet snort and finally left. Only then did Cheongheoja pick up the teapot in front of him.

“Would you care for a cup, Fellow Daoist?”

I didn’t know what he still wanted to say, but I had no reason—or excuse—to refuse.

“I’d be grateful.”

“No need to be grateful.”

Cheongheoja smiled faintly as he poured. I took a polite sip, and a hard-to-describe taste and bitter aroma filled my mouth.

“How is it? The tea?”

“Uh, it’s cold.”

“And?”

“Bitter. Really bitter.”

“I often drink it cold like this. I should have warmed it to suit your taste.”

“Mm. It’s fine. Even warm tea doesn’t really suit my palate.”

“Is that so? I put quite a bit of effort into growing these tea leaves.”

“……?”

Why on earth would you wait until now to tell me something that important?

At my momentary dismay, Cheongheoja burst into hearty laughter.

“I’m joking. It’s true that I tend my own tea garden, but why would I have brought tea leaves along in a situation this urgent?”

“Oh.”

Only then did I realize I’d fallen for his trick. I shook my head.

Well, it made no sense to bring tea leaves along when a hundred thousand enemies were bearing down on Mount Kunlun.

It wasn’t as if he were Geum Jandi, honorary Sect Leader, or anything.[^1]

“You got me. I didn’t know you were like this.”

“Likewise.”

“Pardon?”

Before I could ask what he meant, Cheongheoja smiled and continued.

“You have so many sides to you, Fellow Daoist. When you uprooted the Qinghai City Lord and his faction in one stroke, you seemed like a Great General who could command the world. At times, you seem like an immature hero who leaves everything to his emotions. And yet, in the end, you have the bearing of a grand master whom everyone cannot help but follow.”

Hmm.

What was I supposed to say to that?

Flustered by Cheongheoja’s sudden praise, I scratched my chin for no reason.

“You’re too kind.”

“No one would think so. At least, no one who’s ever met ‘that person.’”

That person.

As I realized who those two words, filled with the deepest reverence, referred to, Cheongheoja slowly parted his lips.

“The Martial God. The greatest grand master in all of history. Though his whereabouts have long been unknown…”

He paused.

“I sensed his presence in you, Fellow Daoist.”

A thought suddenly occurred to me.

Maybe Cheongheoja’s words came close to a certain truth that was growing clearer in my mind.

A boundary-crosser who had traveled between the modern world and Murim before me.

A Player who’d roamed this world—which truly existed somewhere in the endless dimensions—as if it were a game.

Maybe that was why, in that moment, a tiny murmur slipped from my lips before I could stop it.

“…Maybe.”

“Hmm?”

“No, nothing. I just meant I wanted to become like him.”

It was a pretty flimsy excuse, even to me, but Cheongheoja didn’t seem to give my earlier words much thought.

That was understandable. My voice had been very quiet, and unlike the Martial God, whose very existence was a mystery, my origins were clear.

“I see. I believe you could.”

Cheongheoja nodded without a hint of suspicion, took another sip of tea, then added:

“Unlike a certain Daoist who never even reached his feet, despite devoting his whole life to it.”

As the Kunlun Sect Leader, and as a Daoist in his own right, he had lived a life of great renown. Yet his self-deprecating voice carried an unfathomable regret.

“The Martial God was a truly great man. Everyone under heaven trusted and followed him, even though he always concealed his appearance with the disguise technique and never properly revealed his true identity.”

Cheongheoja wasn’t putting himself down by comparing his skill or great achievements to the Martial God’s.

He was talking about character, tolerance, and leadership.

And this whole conversation was drawing nearer to the real reason he’d wanted to speak with me.

“Of course, he wasn’t flawless. Dark Heaven’s schemes had already taken root out of sight, long ago.”

“If he’d still been around, do you think this situation would never have happened?”

“Of course. Though I lack the gift for reading the heavens that Master Hong Dao possessed before he entered Nirvana, I’m certain that if the Martial God had still been around and strong, they would have made a different choice.”

Cheongheoja answered firmly, then sighed.

“But I could never become like him. Even after the age of turmoil that drenched the world in blood had ended and peace had arrived, I couldn’t properly lead even my own sect, let alone all under heaven.”

Without meaning to, I furrowed my brow.

*Don’t tell me…*

My instincts whispered that what came next wasn’t going to be trivial.

Maybe this story would turn out to be a crucial part of the battle ahead.

Cheongheoja noticed my expression change. He stroked his teacup with a bitter look.

“Until now… I didn’t mind that the tea was as cold as ice. I thought that as long as I could swallow it, as long as I could embrace it that way, that was enough.”

Until now, he’d said.

Definitely.

“I take it you mean that’s no longer the case.”

“That’s right. It wouldn’t matter if this old man alone suffered from cold illness. But surely I can’t let hundreds of thousands of people get stomachaches?”

“Hundreds of thousands…?”

At those words, I finally understood for certain.

There was a traitor right here inside Xining.

And deep, deep inside our ranks—close at hand—lurked Dark Heaven’s hidden sword.

Along with that realization, Cheongheoja’s low voice pierced my ears.

Now I understood why he’d wanted to be alone with me.

Why he’d looked so pained and self-deprecating.

“It’s my fault. I didn’t teach that child properly.”

“……!”

Leaving me staring wide-eyed, the old Daoist with a hopeless Disciple silently lifted his teacup to his lips.

By then, it had been heated until hot with Samadhi True Fire.

*Fwoosh.*

Warmth spread, steam curled from the tea, and Cheongheoja drank it slowly. Then he spoke in a voice heavier than ever.

“I have a favor to ask.”

At that moment—

*Ding.*

A System alert rang in my ears, and a translucent holographic window appeared before my eyes.

And then… a day passed.



* * *



The air in Xining was heavier and colder than ever.

Just a few days ago, the townspeople had welcomed the newly arrived reinforcements with smiles. Now their faces were as dark as the sky overhead, as though they vaguely sensed the future awaiting them.

Destruction and death.

The erasure of every living thing that would come at the end.

But who was it that said it?

That humans were creatures of hope.

That they were at their strongest when something was being taken from them—stronger than when they were trying to take something from someone else.

And so, they had not fallen into the depths of complete despair.

Here and now.

With the last sliver of hope and yearning in their hearts, they looked toward the saviors who would light up the darkness settling all around them.

*Splash. Splash.*

Each time the steps of dozens of people fell together, the rainwater—which had risen to their calves in the downpour—splashed beneath their feet.

Even now, rain fell in thick sheets, enough to obscure their vision. But the countless townspeople filling the main road made way, scarcely daring to breathe.

*Whoooosh.*

The human tide slowly parted amid the clamor of the rain.

At its head, cutting through the countless people gathered around him, strode a man without hesitation.

A young giant who had already carved his name into the memories of all the people under heaven and the martial artists of Murim.

*Jin Taekyung.*

By now, everyone knew him.

Some might remember that young man as the Marquis of Shangshan; others, by his sobriquet, the Blazing Flame Divine Dragon.

But no matter how anyone chose to regard him, one fact would never change.

Today’s battle—

And the name Jin Taekyung—

Would become part of the long sweep of history.

Even if it ended in a hollow, miserable death.

“Fuck, did a hole open up in the sky or something?”

The young giant muttered a thick curse in a voice barely loud enough to hear, one that would have shocked anyone who’d overheard it. He lifted his head, and the sky at the end of his gaze was dark.

*Dark as fucking hell.*

“Exactly the kind of weather that makes you not want to die.”

With a snort of laughter, Jin Taekyung watched the shapes slowly approaching through the distant curtain of rain.

An enemy force, horrifyingly vast.

And at that moment—

*Wooooong.*

The opening shot of the battle—one that would decide the fate of Qinghai, or perhaps all under heaven—cut through the air.

*Shhheeeek!*

In the form of hundreds of ice spikes.

[^1]: Geum Jandi is the heroine of *Boys Over Flowers*. The joke refers to her namesake, the Golden Grass.

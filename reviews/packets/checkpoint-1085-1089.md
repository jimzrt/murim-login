# Checkpoint Review — 1085–1089

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

# Chapters 1085–1089

## Plot

As the Yangtze River Channel League and Green Forest Alliance advance west with Dark Heaven reinforcements, some orthodox leaders refuse to fight. Mae Jonghak entrusts Zhuge Feng with Song Ho’s intelligence and a prepared operation against Dark Heaven, then leaves. Zhuge Feng orders his clan to evacuate and carries out the tasking.

The Blood Lord reveals that the advancing armies served as bait and cover while Dark Heaven tested its hidden magic formations. Ten thousand Dark Heaven faithful crossed into the Central Plains through them. Most formations can still be used once, though two or three used at Shaolin may be spent. The Blood Lord orders an advance on Xining.

Four days after arriving in Xining, Jin Taekyung learns that roughly thirty thousand allied fighters are closing in, the Yangtze routes are in enemy hands, and support from Sichuan cannot be counted on. Though Jeok Cheongang says he could not be blamed for retreating, Taekyung chooses to stay and defend the civilians. Jeok supports his decision and intends to use his remaining strength.

At Qinghai Lake, the Blood Lord and Grand Mage ambush the Beggars’ Sect gathering. The Grand Mage freezes the lake, trapping the disciples, while the Blood Lord orders that a survivor be left to deliver his threat. The chapter does not reveal who survives.

## Continuity

- The advancing allied force numbers roughly 30,000, including 10,000 Dark Heaven faithful. The Blood Lord’s forces are marching on Xining to take Qinghai and secure Jin Taekyung if possible.
- Most hidden magic formations retain one use; two or three used in the Shaolin attack may be spent.
- Jin Taekyung has chosen to defend Xining’s civilians. Jeok Cheongang supports him and intends to expend his remaining strength.
- The Great Nation’s vessels guarding the Yangtze tributaries have been destroyed; the enemy controls the river routes for now. Potala Palace has joined Dark Heaven, and Sichuan support cannot be counted on.
- Mae Jonghak entrusted Zhuge Feng with Song Ho’s intelligence and an operation against Dark Heaven. The Zhuge Clan fled its ancestral home to Mount Wudang.
- The Blood Lord and Grand Mage attacked the Beggars’ Sect at Qinghai Lake; who survives remains unknown.

## Translation Decisions

- Render 통산 as Tongsan and 천도객 as “Heaven-Stealing Thief.”
- Keep “magic formations” for 마법진 distinct from “Moving Formation(s)” for 이동진.
- Render 옥쇄 through the image of jade shattering, preserving Taekyung’s contrast between being defiled and breaking with his integrity intact.
- Render 만총 as Man Chong; retain Blood Lord and Grand Mage for 혈주 and 대술사.

## Durable state

{
  "active_continuity": [
    "The Yangtze River Channel League and Green Forest Alliance are advancing west with Dark Heaven forces; their combined force is estimated at roughly 30,000, including 10,000 Dark Heaven faithful.",
    "The Blood Lord’s forces are marching on Xining to take Qinghai; securing Jin Taekyung is a further objective if possible.",
    "The Blood Lord and Grand Mage have attacked the Beggars’ Sect gathering at Qinghai Lake; the Grand Mage froze the lake, and the Blood Lord intends for a survivor to carry his threat.",
    "Potala Palace has allied with Dark Heaven, and Sichuan support can no longer be counted on.",
    "The Great Nation’s vessels guarding the Yangtze tributaries have been destroyed; the enemy controls the river routes for now.",
    "Jin Taekyung has chosen to remain in Xining and defend its civilians against the approaching forces.",
    "Jeok Cheongang supports Taekyung’s decision and intends to put his remaining strength to use.",
    "Most hidden magic formations retain one use; two or three used in the Shaolin attack may be spent.",
    "Mae Jonghak and the New Murim Alliance prepared an operation against Dark Heaven; Zhuge Feng has its intelligence and tasking to execute it.",
    "The Zhuge Clan left its ancestral home and fled to Mount Wudang."
  ],
  "continuity_sources": [
    1088,
    1089
  ],
  "open_questions": [
    "What is the black-robed captive in Qinghai’s identity and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "Who survives the Blood Lord’s attack at Qinghai Lake?"
  ],
  "safe_through": 1089,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1085

# Chapter 1085

The rumors spread in an instant.

From mouth to mouth.

On the beating wings of messenger pigeons.

Along with the hooves of horses racing across mountains and fields under the crack of whips, and the smoke of beacon fires staining the sky gray.

Before the people shaken by the astonishing news could even determine whether it was true, they saw it with their own eyes.

Countless ships cutting swiftly through the river, their flags billowing proudly in the favorable wind.

The Yangtze River Channel League.

The moment they made out the five characters written on the flags, swollen full by the wind, they realized that denying it any longer would be no different from escaping reality.

Everything they had seen and heard was no baseless rumor.

It was true.

A mere band of river pirates, who had lived parasitically on the Yangtze with the world’s tacit consent, had at last risen to become its true rulers.

And they had done it against the Great Nation itself—the master of the world.

“…Gods of heaven and earth.”

The groan that slipped between someone’s lips was hollow.

After all, this vast empire, founded under the Mandate of Heaven, was collapsing.

No—their heaven was.

“If this isn’t defying heaven, then what is?”

More than a hundred years had passed since the age of warring heroes came to an end and a unified dynasty was born.

The country folk, who had held the Great Nation ruled by the Son of Heaven up as the heavens themselves, trembled with unease. The Confucian scholars groaned as they realized that the natural order had crumbled. The betrayed martial artists were swept up in anger and shock.

“Those bandits finally…!”

“I knew something was off. We should never have trusted dark-path figures in the first place!”

But the Yangtze River Channel League’s betrayal wasn’t the only news to shock everyone.

“Two days ago, the Green Forest bandits rebelled in Hubei and Shaanxi!”

The Green Forest Alliance, which divided the world’s dark-path forces with the Yangtze River Channel League, had risen up.

And on top of that, people belatedly realized that storm clouds were gathering beyond the distant Great Wall.

“An urgent report from Sichuan! Potala Palace in Tibet is on the move!”

Potala Palace.

The news that the esoteric monks—counted among the Three Outer Powers alongside the North Sea Ice Palace and Nanman Beast Palace—had finally broken their long silence and stirred to action surprised no one in the Murim.

In their eyes, as people of the Central Plains, Potala Palace had been nothing more than a pseudo-religion following evil doctrines since the distant past.

The New Murim Alliance had sent envoys to seek an alliance several times since its founding, but Potala Palace had always answered with silence. For them to act now, in a situation like this, could only mean one thing.

“...Dark Heaven. It’s them again.”

Fortunately, Sichuan had powerful reinforcements.

Unlike the North Sea Ice Palace, which—as always—remained neutral, Nanman Beast Palace had overcome the threat of civil war thanks to the astonishing exploits of a young man and resolved to ally itself with the Murim Alliance.

So the world’s attention focused on the Yangtze River Channel League and the Green Forest Alliance.

The initial shock of learning the truth soon passed, and quite a few voices began to scoff at the dark-path forces’ uprising.

“Even if they won one great victory, dark-path figures are still dark-path figures. Nothing’s changed.”

It wasn’t entirely wrong.

The Yangtze River Channel League and the Green Forest Alliance together had nearly twenty thousand men, but if numbers alone could claim everything, the Beggars’ Sect would own the Murim world.

Everyone was confident that the orthodox factions, now completely united around the Murim Alliance, wouldn’t be shaken by a force this small.

“Shaanxi has Huashan and Zhongnan, and Hubei has Wudang and the Zhuge Clan. And if the Imperial Army under the Son of Heaven moves out, those bastards will regret joining hands with Dark Heaven.”

But this prediction had a few fatal flaws.

First, the Zhongnan Sect had very few forces left at its headquarters.

Second, most of the hundreds of thousands of Imperial Army troops were concentrated in Jiangsu, where the Imperial Capital—home of the Son of Heaven—was located.

And third, the Green Forest Alliance and the Yangtze River Channel League were marching west in broad daylight, with no thought of hiding themselves, and their forces were far larger than anyone had expected.

Like a snowball slowly growing as it rolled down a snow-covered slope.

“The Green Forest bandits gathered in Hubei crossed Tongsan half a shichen ago! Their numbers are estimated at around five thousand!”

“Five thousand? What in the—”

“Didn’t you say they were only around three thousand at most half a day ago?”

“W-Well, it seems the forces scattered among the various strongholds have joined them.”

“That’s absurd!”

But the men who had so forcefully denied the messenger’s report soon learned the truth.

Another force had joined the two bands of outlaws who had secretly gathered around Hubei and Shaanxi even before the great battle in Gansu.

And they had done so by means of a certain method the Central Plains Murim had been most wary of.

“...Damn it. They must have used that accursed dark art.”

“Dark art? Don’t tell me…”

“That’s right. A Moving Formation.”

The existence of the Moving Formation, once kept under the tightest security, was no longer a secret known only to a tiny handful.

As long as people had eyes and ears, secrets would always find a way to leak.

The Murim Alliance leadership and the Hidden Shadow Pavilion, led by the Thousand-Faced Fox Song Ho, had taken the field, but for some reason, the secret of the Moving Formation had still gotten out. Now that they’d finally seen it for themselves, the Sect Leaders and Family Heads felt a chill.

*We have to strike. Right now.*

The Yangtze River Channel League and the Green Forest Alliance were, after all, coalitions of separate groups.

Their Stronghold Lords commanded anywhere from a few dozen to several hundred, or even a thousand, men each. They pledged loyalty to their respective alliance leaders and repeatedly gathered and dispersed at their command.

So the best time to strike them was right now.

Before the enemy had fully assembled. Before they had gathered in one place and formed a powerful force.

But the variable everyone had secretly feared had finally come to pass.

No one knew where the Moving Formations were. And through them, Dark Heaven’s powerful forces were joining the dark-path figures.

*What if we fight them now?*

It was dangerous.

The Moving Formations themselves posed an enormous threat, and there was no guarantee they could win the battle.

Shaolin, the Mount Tai and Northern Dipper of the Murim. The Sichuan Tang Clan, one of the Five Great Families, with its deadly poisons and hidden weapons. Nanman Beast Palace and even the Hebei Peng Family had all suffered terrible losses.

That wasn’t all. According to reports, the Kongtong and Zhongnan Sects had also been hit hard in Gansu.

The damage was no less severe than during the Great Faction War, a time no one wanted to remember. If anything, it was worse.

The Nine Sects and One Gang. The Five Great Families.

With even the fifteen great trees supporting the Murim world trembling at their roots in the typhoon stirred up by Dark Heaven’s storm clouds, it was no easy thing to summon the courage to risk everything and face the danger.

Especially for Sect Leaders and Family Heads, who were responsible for the lives of their families—not just their own.

“I… I give up.”

“Sir Seok! What are you saying?”

“Let’s be realistic. Do you think the forces gathered here can stand against them?”

“But—”

“You know it too, don’t you? The outcome is already decided. We have to conserve what strength we can. Fortunately, those traitors who joined hands with Dark Heaven are heading only west. We can avoid a clash for now.”

“Fortunately? Did you just say ‘fortunately’? Do you really not know what they’re after?”

“I know. They want to pin down the reinforcements from the Central Plains and take Qinghai completely into their grasp. That must be their goal.”

“And you know that, yet…”

“But this time, I have no choice. I’m no Supreme Peak master, nor am I a Sect Leader of one of the Nine Sects and One Gang. I’m sorry.”

“Sir Seok!”

“Please don’t call me that. I’m not worthy of it. I’m just a cowardly Sect Leader who wants to protect his family.”

After muttering bitterly, he left. Several other Sect Leaders, their faces downcast, got up and followed him.

And so did the middle-aged man sitting quietly in the seat of honor, watching them.

Scrape.

The others wore complicated expressions—betrayal and anger, mixed with a sympathy that lingered in one corner of their hearts. At the sight of the middle-aged man getting up, their eyes widened.

They had firmly believed that even if everyone else left, he wouldn’t.

“F-Family Head!”

“What is this?”

But contrary to their ominous suspicions, the middle-aged man merely shrugged, his expression calm.

“Ah, don’t misunderstand. I’m just going to get some air.”

The others relaxed, but let out a sigh at the same time.

A third of Hubei Murim’s leading figures had left. And he was going to get some air.

It was certainly like him, but it was no less ridiculous.

“Why now, of all times?”

“Yes. Right now.”

“There’s so much to discuss. Even the Murim Alliance hasn’t made a proper decision yet…”

“If it’s that urgent, I’ll just piss right here.”

“Pardon?”

As the others stared at him in bewilderment, the middle-aged man clutched the front of his trousers, looking grave.

“My bladder’s about to burst.”

“...!”

“I don’t know if it’s because I’m getting old, or because I’ve spent so long away from our family, living out in the world, but I think my bladder’s gotten weak. And on top of that, even when I’m just sitting still, a certain private spot on my backside starts tingling…”

The middle-aged man rambled on, then saw their expressions and smacked his lips.

“Goodness, I shouldn’t have brought that up. Let’s continue where we left off.”

“...Just go.”

“No need. I’ll just wet myself right here. I’m sure even Zhuge Wuhou did the same when he was busy.”

“Please go. We’re begging you.”

“Oh? Then it’s all right if I do?”

“Yes. For our sake, please.”

“Since you’ve begged me so earnestly three times, I suppose I’ll have to follow the story of the Three Visits to the Thatched Cottage.”

The middle-aged man smiled at the half-resigned group. Then, Zhuge Feng, Family Head of the Zhuge Clan—or rather, the Crouching Dragon Guest—hurriedly left.

He didn’t head for the privy. He walked for a long while through winding paths like a maze, until he reached the garden in the Inner Hall, a place only the Family Head was permitted to enter. At last, he stopped.

“It’s all well and good to stay out of sight, but you should at least let me know where you’ll be.”

In a corner of the spacious garden, someone stood with their back to him, gazing at a mulberry grove said to have been planted by Zhuge Kongming himself.

Zhuge Feng addressed the figure in a low voice.

“Don’t you agree, Alliance Leader?”
## Chapter artifact 1086

# Chapter 1086

To put it kindly, he had an open, easygoing face. Put it less kindly, and he was the sort of young man you might forget in a moment, even after being introduced.

He was neither tall nor short, and had the kind of natural air that let him blend in wherever he went.

Perhaps that was why no one had thought of the title Sword Saint when they saw the young man beside Zhuge Feng, who had returned to his family after a lengthy absence.

“Oh, there you are.”

Mae Jonghak finally turned around and smiled at Zhuge Feng.

His eyes were deep yet clear, and his smile seemed to put anyone who saw it at ease.

While the world was gripped by turmoil and anxiety, the Murim Alliance Leader—who ought to have borne a heavier burden than anyone else—continued in an almost childlike tone.

“I was wandering here and there and got bored. At some point, I found myself just walking wherever my feet took me, and here I am.”

“You came here without knowing where you were?”

“I did.”

“This garden and everything within roughly a hundred *jang* of it are part of the Family Head’s Hall. Even our family’s direct descendants need my permission to enter.”

“Is that so? I did think something was a little odd. Aside from the people hiding here and there, there were all sorts of mechanisms and formations set up.”

Hearing Mae Jonghak’s answer, Zhuge Feng could only let out a hollow laugh.

“Is something good happening?”

“Not at all. I just found it funny.”

The Zhuge Clan was a place even the greatest thieves in the world wouldn’t dare try to break into.

The Heaven-Stealing Thief, who supposedly could steal even from heaven, had once barged into the Zhuge Clan’s Family Head’s Hall—and wound up trapped in its mechanisms and formations, wandering for over a month.

At the time, he was the greatest thief in the world. In the end, he was rescued by the Zhuge Clan’s martial artists on the merciful order of the previous Family Head. Released in a state of skin and bones, he left these words behind:

> “Break into the imperial palace, and you’ll be tortured to death. Break into the Sichuan Tang Clan, and you’ll be poisoned to death. But break into the Zhuge Clan, and they’ll rob you down to your soul and let you starve to death.”

And so the Three Forbidden Places were born, leaving a painful lesson for the thieves who came after him.

Of course, it had now been proven that even the Zhuge Clan’s Family Head’s Hall—where the greatest thief of the age had nearly starved to death—was powerless before the greatest swordsman in the world.

“My apologies. If I’d known this was the Family Head’s Hall, I would’ve asked permission.”

“I was in a meeting at the time.”

“Does the door stay shut if the homeowner isn’t there? I could’ve asked the people hiding around here to let me in.”

“Even if you had asked, would they really have opened it and said, ‘Goodness, where have you been all this time?’”

“True enough. It’s not as if I could tell them I’m the Alliance Leader.”

As Mae Jonghak scratched the back of his head, Zhuge Feng shook his own.

People did call him a bit of an eccentric, but compared to the man before him, he couldn’t hold a candle to him.

“So, what were you doing here?”

“Smelling the fragrance.”

“The fragrance?”

Zhuge Feng cocked his head.

Though he had been the Family Head for many years, he had visited this garden only a handful of times.

Part of the reason was that he spent most of his time studying and researching mechanisms and formations. But the place was also far too rugged to call a flower garden.

“As you can see, this garden is full of nothing but mulberry trees. There isn’t much to see, and they don’t smell especially nice.”

“That’s not so. Everything in the world has its own fragrance. These mulberry trees are no different.”

Mae Jonghak added quietly,

“And neither are the plum blossoms, blooming somewhere I can’t reach right now.”

At the faintness in his voice, Zhuge Feng fell silent for a moment, then asked carefully,

“Do you… want to return to Huashan?”

“I always have. But not in a time like this. It’s clear where I need to be.”

“Then…”

“I just miss those peaceful days. That day I lay beneath the sunlight in a forest full of plum blossoms.”

Mae Jonghak reached out and stroked a nearby mulberry tree.

Perhaps because of the unseasonably cold weather, its branches hung bare, without a single fruit. It looked much like the world did now.

“One day, this mulberry tree will bear fruit too. Don’t you think?”

“It will. No—I’ll make sure it does. With my own hands.”

Mae Jonghak gave a faint smile at Zhuge Feng’s firm reply.

“Your hands are precious. Use them elsewhere. For rough work like this, a swordsman like me is the right one to step forward.”

“...!”

Zhuge Feng’s eyes trembled as he understood what Mae Jonghak meant.

A year.

Short, if you called it short. Long, if you called it long.

But the result of the work they had pursued more fiercely than ever before was finally within reach. He could feel it down to his skin.

Even he, who already knew every step and turn of the plan, was shaken.

“Alliance Leader, do you mean…”

“We can’t keep taking hits forever. So many people have endured and waited for so long.”

“Then, at last?”

Mae Jonghak nodded quietly.

“We can’t afford to let this chance pass us by. We may never get another.”

“...!”

“You’ve worked hard, Family Head Zhuge. Without your efforts, we wouldn’t have this opportunity today.”

Zhuge Feng finally managed to calm his excitement. After taking a deep breath, he replied,

“No. It’s thanks to everyone’s sacrifices, great and small.”

He looked down at his hand, still trembling.

It was rough and calloused.

Like the hand of a martial artist who had spent their whole life training.

His slender, elegant hand was gone—the one that had learned only the minimum martial arts required of a Family Head, and whose calluses had slowly faded away.

Ever since the dark cloud of Dark Heaven had spread across the world, he had waited for this day.

The day he could prove why he had spent so long away from home.

“Have you decided who will stay and who will leave?”

“Yes.”

“You know what your mission is.”

“As if I could forget. I’ve been waiting for this moment all along.”

“Everyone under heaven is ready.”

Mae Jonghak emphasized the final words, then pulled a rolled-up sheet of paper from his robes and held it out.

“This is…”

“Chief Song gave it to me before I left Henan.”

Mae Jonghak’s absence was currently being kept an absolute secret. At the mention of Song Ho, Chief of the Hidden Shadow Pavilion, Zhuge Feng’s gaze grew intent.

“What does it say?”

“The names of the enemy spies still embedded in our ranks, along with the people who’ll join you and a map showing where they’ll meet.”

As Zhuge Feng opened the letter and read it for himself, delight flashed in his eyes.

“Just as I thought…”

“We put the Beggars’ Sect and Lower District Sect to work alongside the Hidden Shadow Pavilion. Chief Song personally selected everyone involved, so there’s no risk of the secret getting out.”

“I thought as much. I’ll carry it out without the slightest mistake.”

“Everyone’s worked hard to cultivate this field. We can’t let birds or insects peck it apart.”

“Don’t worry. Getting here was painful and hard, but I’ll finish the harvest in one swift stroke without a single mistake.”

“I trust you.”

Mae Jonghak took the letter back from Zhuge Feng and filled his hand with internal energy.

Whoosh.

The paper was swallowed by the flames of Samadhi True Fire, scattering into ash.

Having burned the letter as a precaution, Mae Jonghak watched as Zhuge Feng clasped both hands and bowed with utmost respect.

Zhuge Feng already knew the time had come for the greatest swordsman in the world to leave.

“Travel safely, Alliance Leader.”

He bowed, his respect sincere.

And when he raised his head again, all that remained were hundreds of mulberry trees trembling in the cold wind.

“What a hurry. He didn’t even say goodbye before leaving.”

Zhuge Feng let out a quiet snort and reached out to touch a drooping mulberry branch.

These trees were said to have been planted by the Zhuge Clan’s ancient ancestor, Zhuge Wuhou, and were one of the clan’s symbols. But the story the common folk liked to repeat was nothing more than a rumor.

*Wuhou followed Emperor Zhaolie of Han to settle in Bashu. There’s no way the mulberry trees he planted himself could be thousands of li away, in Hubei.*

These mulberry trees had been planted by Zhuge Wuhou’s descendants, who laid the foundation for the Zhuge Clan as it stood today.

They had planted them to carry on the Zhuge family line—and to remember their great ancestor.

No one knew what had become of the hundreds of mulberry trees left behind in Shu Han, which had ultimately fallen after Zhuge Wuhou’s death.

But their roots had taken hold in a new land.

As long as a single seed remained, the line would not end.

“What matters is the people, not the land.”

Murmuring softly, Zhuge Feng brushed the frost from the branches.

“When I come back, I hope you’ll be bearing fruit.”

With one last faint smile, Zhuge Feng turned and walked away without hesitation.

A few moments later, he addressed the people who were tearing through the Inner Hall, worried their Family Head might have been assassinated in the privy.

“All right, start packing.”

“What? Packing what now?”

“Wait, you haven’t finished packing yet?”

The bewildered group couldn’t make sense of his unexpected words. Then he struck them with another thunderbolt.

“I said pack! The Zhuge Clan is leaving this place immediately!”

At that moment, a few of them thought that damn Family Head might have been better off getting assassinated in the privy.

Yet a smile they couldn’t understand tugged at Zhuge Feng’s lips as he dropped that bombshell.

*May fortune be with you, Alliance Leader. And…*

*Just a little longer. Please, hold on just a little longer.*

Zhuge Feng repeated his desperate wish in his heart.

Blazing Flame Divine Dragon Jin Taekyung.

His gaze was fixed far to the west.
## Chapter artifact 1087

# Chapter 1087

While Zhuge Feng gazed west with an earnest wish in his eyes, a low laugh rang out from the highest peak in the western lands.

“Good. This is how it should be. It has to be.”

At the Blood Lord’s smiling nod, the messenger who had just finished his report felt a quiet sense of relief.

He had brought news good enough to satisfy his master.

And, unlike his comrades, who had already become cold corpses one after another, he wouldn’t be killed by the violent man in front of him.

But it was too soon to feel safe.

This hour wasn’t over yet.

“So they’re all just watching carefully and waiting to see what happens?”

At the Blood Lord’s question, the messenger lowered himself further, prostrating himself before he answered.

“That is correct. The Nine Sects and One Gang and the Five Great Families are watching the situation and strengthening their defenses, but they have made no further moves.”

“They used to praise one another as chivalrous heroes, but now that the moment has come, they’re scared stiff.”

The Blood Lord’s smile deepened. Then a clear voice rang out from somewhere.

“Better a coward than an idiot like you. Don’t you think?”

The Blood Lord frowned without meaning to when he saw who had spoken, but soon answered in a leisurely tone.

“Couldn’t agree more. Stupidity leads straight to incompetence. That must be why he entrusted this plan to me.”

“And what about taking the sorcerers under my command and starting this without my permission?”

“Since I was entrusted with everything happening in Qinghai, why would I need to consult a mere defeated general?”

The Grand Mage smiled coldly at the reminder of her failure in Gansu.

“Your eloquence has certainly improved. Last time, was it your head that got cut off instead of your arm? I suppose I should praise you for getting a little smarter.”

For an instant, the smile on the Blood Lord’s lips faded.

Ever since Sword Saint Mae Jonghak’s strike had taken one of his arms during the incident the Central Plains Murim called the Shaolin Bloodshed, it had become a sore point he could not bear to have touched.

*That damned woman.*

Of course, he had accomplished his mission well enough.

He had stolen the Green Jade Buddha Staff, the most important prize, and killed countless Shaolin Temple martial monks, including the Abbot, Hong Dao, dealing the temple a devastating blow.

But despite the success, the wound to his pride from how it had all happened showed no sign of healing.

Even remembering that violet Sword Force sent a chill through him. The place it had severed still throbbed, even now that a new arm was in place.

And he still carried his anger toward one reckless young pup who had stood against him to the very end, without the slightest fear.

“Shut your mouth, bitch. You weren’t even there, so you’ve got no right to run your mouth about it.”

The Blood Lord’s voice sank low. The Grand Mage gave him a faint smile.

“Right. That’s what I regret most.”

“What?”

“If I’d been there, you never could’ve come out with that nonsense about losing after fighting the Sword Saint for hundreds of exchanges.”

“……!”

“Be honest. After a life-and-death duel with the Fire King—that violent old man—you fought the Sword Saint for hundreds of exchanges? Quite a nerve you have. How dare you lie to him?”

“You’re imagining things. I’ve always told him the truth.”

The Blood Lord replied as calmly as he could, but he knew better than anyone that the Grand Mage was right.

It was true.

He had lied to the Lord of Heaven about his final fight with Mae Jonghak.

The first time he had ever lied—and the last.

Why?

It was simple.

He had been furious, and afraid.

If he had known Mae Jonghak’s identity from the start, and had conserved his strength in preparation for his arrival, he wouldn’t have lost his arm before he could even last three exchanges.

And if he had reported everything without leaving out a single detail, the master he trusted and worshiped like a god might have cast him aside.

*But he believed in me. That’s enough.*

The Blood Lord quietly settled his thoughts.

It didn’t matter what the Grand Mage said to his face.

Whether the Lord of Heaven truly believed him or had simply pretended not to know, he had made no issue of it—and he never would.

“Enough. Keep this up and I’ll want to blow your head off.”

At the Blood Lord’s warning, his composure now restored, the Grand Mage shrugged.

“I doubt you could, but let’s leave it there. We have important work ahead. I don’t want to waste my strength.”

The Blood Lord nodded without a word.

The two of them had snarled at each other without pause, like sworn enemies from a past life. But carrying out the mission their master had given them mattered more than anything else.

“As you’ve probably guessed, the Central Plains won’t be able to interfere in Qinghai’s affairs for now.”

The Green Forest Alliance and the Yangtze River Channel League were still pushing west even as they spoke.

Of course, if the Murim Alliance brought all the Central Plains’ strength together and committed its full forces, it could crush them in an instant. But now that the Moving Formations had shackled them, taking that heavy first step would be difficult.

No—not just difficult. It was close to impossible.

Sending enough troops to save Qinghai would mean cracking the solid wall of the Central Plains.

“So if they want to save Qinghai, the Central Plains’ defenses will be left exposed. And if they want to protect the Central Plains, they have to abandon Qinghai.”

The Blood Lord’s smile returned as he continued.

“Looks like all that effort we put into those Central Plains bandits has paid off. A perfect checkmate, wouldn’t you say?”

Unlike him, the Grand Mage’s lips did not move beneath her veil.

“Of course I know. That’s why I regret it even more.”

“Why regret it? It’s only a matter of time before Xining, where they’ve gathered, is surrounded from both sides.”

“Is that all?”

“Take complete control of Qinghai, then, if possible, secure Jin Taekyung according to further orders. Wasn’t that what he instructed?”

The Grand Mage let out a hollow laugh at the Blood Lord’s question.

“I take back what I said earlier. You’re still just as stupid.”

“What?”

“Don’t you understand? If the Murim Alliance had moved this time, we could have taken the Central Plains Murim—or even everything he wants.”

The Grand Mage stared straight at the Blood Lord through her fine veil and added quietly,

“The whole world.”

“……!”

“You should have consulted me before making your decision. To waste those precious magic formations, each usable only twice, on something like this…”

A low hum.

Qi surged in time with her cold voice.

At that moment, the Grand Mage was truly furious.

Furious that the Blood Lord had moved so many troops without so much as a word of discussion with her.

That he had wasted the dozens of magic formations Dark Heaven had planted throughout the world over a long period—and missed a golden opportunity to take the world.

Yet even as she seethed, the smile on the Blood Lord’s lips did not disappear.

If anything, it grew even broader.

*What?*

The Grand Mage only realized something was wrong a moment too late. The Blood Lord tossed out a scornful reply.

“I think you need to take back what you just said. Did you really think I was that stupid?”

“What are you talking about?”

“The Yangtze and the Green Forest. Those mangy bandits were recruited as bait from the very beginning. I never intended to waste real effort on bait like that.”

The Grand Mage’s eyes widened as she grasped what he meant.

“Then perhaps…”

“That’s right. It was all for show. At the same time, I thought there was a chance it might work. The people of the Central Plains must have been keeping a close watch for magic formations for a long time, unless they were complete idiots.”

That was why they needed to test them.

Had the dozens of magic formations Dark Heaven’s sorcerers secretly set up throughout the world been discovered?

And if not, were they still working properly?

“And now we know for certain.”

The test had succeeded.

A total of ten thousand Dark Heaven faithful had crossed into the Central Plains through the magic formations and joined the Green Forest Alliance and the Yangtze River Channel League. The Blood Lord had only just received the news.

From the messenger still unable to raise his head in front of them.

“Perfect. Unfortunately, two or three of the magic formations used when we attacked Shaolin may have lost their power, but most still have one use left.”

The Grand Mage had fallen silent and was listening closely. Now she murmured,

“That’s enough. With that much…”

They wouldn’t need to bring all of Dark Heaven’s forces into play.

They could drop tens of thousands of troops into the heart of the Central Plains all at once and bring down its major sects. A single great war would be enough to conquer the world.

But that alone could not quell all her anger.

The Grand Mage looked at the Blood Lord with a piercing gaze.

“I understand your reasons. I understand the justification. But it’s not enough.”

“Why not?”

“We still have that final chance to activate a magic formation. But now they’ll be even more wary of us because of it.”

“No. It’s the other way around.”

“What?”

“When bandits start rampaging all around them, wouldn’t it be stranger if we did nothing to help or intervene?”

“……!”

“It was something we had to do anyway. We need to keep watch over those two bandit gangs, in case they change their minds again.”

If they could betray them once, they could do it twice or three times.

The ten thousand Dark Heaven faithful sent ahead were also a deterrent against that betrayal.

Another shackle, to keep the Green Forest Alliance and the Yangtze River Channel League from entertaining other ideas.

To make sure they wouldn’t even dare.

“No matter what happens, it won’t hurt us.”

The Blood Lord rose to his feet and continued,

“If the Central Plains’ chivalrous heroes can’t bear their guilt and rise from their seats, the magic formations will come into play.”

Step. Step.

His voice scattered as his footsteps rang out slowly.

“And if they stay where they are, we’ll pass through Qinghai and head into the Central Plains.”

Rumble.

At the Blood Lord’s gesture, the massive iron doors swung open.

Below them lay countless troops, blackening the mountain range.

“Raise the army. We march on Xining.”
## Chapter artifact 1088

# Chapter 1088

I’d made it through more crises than I could count.

Even if I considered only what I’d faced inside Gates, I’d been in life-or-death situations countless times. By sheer experience, it wouldn’t be an exaggeration to say I was as seasoned as any old master.

So I knew very well:

The more dire the situation, the more clearheadedly you had to assess it.

And now, four days after arriving in Xining, I’d finally reached a conclusion, thanks to some clearheaded thinking and a few more pieces of information.

“Mujin.”

“Yes, sir. Just give the order.”

Hyuk Mujin looked at me with blazing eyes and thumped his chest.

“Your reliable right-hand man is right here, Captain.”

I opened my mouth to the guy who was about as useful as a pathetic little toe.

“I think we’re fucked.”

“Pardon?”

“I said I think we’re fucked. For real.”

The fire in his eyes went out as if someone had doused it with cold water, but I could only answer calmly.

“Yeah. Completely.”

“But you weren’t saying that a few days ago.”

“I wasn’t. Not at first.”

But the situation had changed beyond recognition.

The Yangtze River Channel League and the Green Forest Alliance.

As if getting blindsided by those two bands of thieves wasn’t enough, Potala Palace in Tibet had joined forces with Dark Heaven.

Potala Palace’s rise at such a perfectly awful moment also meant we could no longer count on support from Sichuan.

And the Central Plains—

“Now that even the Great Nation’s military vessels guarding the Yangtze’s tributaries have been wiped out, the river routes through the Central Plains are basically in their hands for the time being.”

I wanted to deny it, but the truth was impossible to deny now.

A messenger eagle had arrived the night before, confirming the reports that Seafaring King Pa Ryun’s Yangtze River Channel League pirates had scored an overwhelming victory against the Great Nation.

“Even if they suffered a crushing defeat this time, don’t they still have plenty of military vessels left? The Great Nation has more strength than that, and the Yangtze is huge.”

Mujin had a point.

The Great Nation wasn’t called great for nothing.

The battle with the Yangtze River Channel League had dealt it a terrible blow, but if that were enough to make it lose control of the entire Yangtze, it never could have claimed to rule the world in the first place.

The important thing, though, was—

“Time. It’s a question of time, isn’t it?”

A familiar voice cut in.

Bow Saint emerged from behind Jeok Cheongang, who had appeared at some point.

“The time they’ve gained, however brief, will be more damaging to us than anything.”

Exactly.

Whether their reign lasted only three days or their glory faded as quickly as a flower, there was no way to stop the Yangtze River Channel League right now.

By the time the Great Nation invoked its authority to requisition ships wherever it could and gathered its naval forces from across the land, it would be too late.

By then, Qinghai Province—no, Xining itself—would be completely surrounded, front and back.

“So how many of those damn bandits have gathered?”

At Jeok Cheongang’s question, I answered,

“Our estimate so far is around thirty thousand.”

“Hah. They’re swarming in like a pack of dogs. Then again, numbers are about the only thing those dark-path bastards have to brag about.”

“If it were just numbers, that would be much better. Take out their heads, and the rest would collapse on its own.”

As was true everywhere, the dark-path figures and the unorthodox factions were especially dependent on having someone at their center.

Their nature was to gather and scatter around individuals who became the head of the group through overwhelming strength and the ability to command others.

Seafaring King Pa Ryun.

And Green Forest Battle King Tae Gunak.

If we took out those two Supreme Peak masters who embodied the dark path, the combined forces of the Yangtze River Channel League and the Green Forest Alliance might not be such a difficult opponent.

Of course, that was only if no new uninvited guests showed up.

“Right, Dark Heaven. You said they’d joined them.”

“Yes. Ten thousand of them. A full third of their forces.”

Jeok Cheongang smacked his lips at my answer.

“They’ve put a tight leash on those two. Made sure they won’t dare bare their teeth at their master.”

“That’s what makes it worse. Even if Pa Ryun and Tae Gunak are taken out now, their forces will still come after us.”

“Of course. Those cowards have seen for themselves that the dark arts they’d only heard about are real. They’ll be even more inclined to tuck their tails between their legs.”

Ten thousand enemies had appeared.

And right in the heart of the Central Plains.

The existence of Moving Formations had always been a source of concern for the Murim of the Central Plains. But having that concern become reality was another matter entirely.

It seemed even the great sects like the Zhuge Clan and Wudang couldn’t ignore the problem.

Even they, more or less the dominant powers of Hubei’s Murim, had chosen to avoid a direct confrontation.

I’d heard that the Zhuge Clan had gone so far as to flee to Mount Wudang, abandoning the family home where they’d put down roots for hundreds of years.

*They’re weaker than the other great sects, so I understand. But was that really the best choice?*

I found myself thinking of Zhuge Feng, Family Head of the Zhuge Clan and the Crouching Dragon Guest.

We hadn’t known each other for all that long, but from what I’d seen of him while I was in Hubei, he was a good man.

Like a rock in a raging current, he was carefree yet steadfast, with the ability to back up that resolve.

And most of all, he was a man who deserved to be called a Great Hero.

*So why?*

I wanted to ask.

Not in the privacy of my own thoughts, but to their faces.

The Nine Sects and One Gang. The Five Great Families. The many Sect Leaders and Family Heads of the orthodox factions.

The Murim Alliance—a single banner raised by all of them.

I wanted to look each of them in the eye, men who never hesitated to call themselves righteous, and ask:

Was this the righteous path they were so proud of?

Was this the great cause they spoke of, the reason they couldn’t stop the traitors heading west?

Crack.

Just then, my clenched fist popped. Jeok Cheongang, who had been watching me with a solemn gaze, spoke up.

“Anyone can become a coward when faced with a crisis.”

“I know.”

I added quietly, remembering a past that still lingered like a scar.

“I’ve been one myself.”

“It sounds like you’re saying you’ll never do it again.”

“I promised myself.”

“You must feel it in your bones, but even judging by what we know so far, their strength is beyond anything we imagined. If Xining is surrounded, we’ll be in for a very difficult fight.”

As if agreeing, Bow Saint nodded quietly. Both had reached heights martial artists could scarcely dream of, and yet even they had to consider the possibility of defeat. That was how dire things were.

“I told you before: anyone can become a coward in a crisis.”

Jeok Cheongang fixed his deep gaze on me. His voice was low and steady.

“In a situation like this, not a soul under heaven could blame you for choosing to live and fight another day.”

*Live and fight another day.*

Mujin’s eyes widened as he understood what Jeok Cheongang meant. Bow Saint stayed silent.

And I—

“Probably. No, definitely.”

I met Jeok Cheongang’s gaze and continued,

“Even if I chose to live and fight another day—no, if I ran away—they’d have no right to criticize me.”

“Even so, it wouldn’t matter. If anyone dared to criticize you, I’d personally rip out his tongue. If anyone pointed a finger at you, I’d turn it to ash.”

“I know that too.”

“Then?”

“I’m staying. Here.”

At my calm reply, Jeok Cheongang’s brow furrowed.

“Why?”

“Because if we leave, Qinghai is finished. The countless civilians living in Xining won’t even have time to escape.”

“If we meet our deaths here, it may not just be Qinghai that falls into their hands. It could be the whole world.”

He wasn’t being arrogant. He wasn’t exaggerating.

The Three Saints and Ten Kings were symbols of the Murim world, and its strongest forces.

It was embarrassing to admit, but I, too, had become a symbol of sorts.

And a gap in our forces could lead straight to defeat.

Jeok Cheongang let out a sigh as he looked at me in silence.

“The world has already looked away. The Nine Sects and One Gang, the Five Great Families, the Murim Alliance—they’ve all turned their backs. And you still plan to make such a foolhardy choice?”

That was when I finally parted my tightly closed lips.

“Even so, we have to.”

“What?”

“No. Because everyone has turned away and abandoned us, we have to do it even more.”

Jade is beautiful even as it shatters.

The light it throws off as it breaks into dozens of pieces is more brilliant than ever.

That is what it means to shatter like jade.

That is why it is called jade’s shattering.

It is so brilliant, you forget the word *destruction*.

It would rather break than be defiled.

“Have you ever seen jade covered in filth and dust?”

Jeok Cheongang stared at me, eyes wide. I continued, slowly, but clearly.

“I haven’t. But I know that jade already covered in grime can lose its value, at least for a while.”

Even so, the essence of the jade remained.

Even if it looked like nothing but dirt on the outside, there was still light hidden within.

But seeing filth cover its beautiful surface, no one would reach out to touch it.

Not unless a sudden downpour washed the jade clean.

Not unless someone who remembered what it once looked like found it and carefully wiped it off.

So—

“Better to break than to be defiled.”

“……!”

“……!”

“……!”

I felt the air tremble and let out the breath I’d been holding.

Yes. This was right.

Even if it ended in death, I couldn’t lose that brilliant light I’d had from the beginning.

I had to make everyone remember. I had to make them realize what mattered most—the thing they’d briefly forgotten while hiding behind excuses about the greater good and worrying about what they might lose.

The jade called justice.

And I would do everything in my power to protect it.

I wouldn’t break. I wouldn’t be defiled.

There was still far too much left to do before I could face a final moment of brilliance.

The greatest, strongest wall casting its shadow over the world was still standing.

*The Lord of Heaven.*

Just then, as the meaning of those two words rang through my heart and drew nearer than ever, Jeok Cheongang—head bowed, lost in thought amid the heavy silence—suddenly spoke.

“You asked whether I’d ever seen jade covered in filth and dust?”

He muttered as if speaking to himself, then raised his head.

Though his body had grown young again, a familiar face was reflected in eyes that held the weight of his years.

“Yes. I saw it. I remember it very clearly.”

He looked at me.

The gaze that had been sunk deep in memories of that day, not so long ago, began to shine.

“That was when I realized how brilliant a light the pathetic, weak little brat in front of me was carrying.”

“……!”

“I told you, didn’t I? If anyone dared to criticize you or point a finger at you, I’d personally punish them. But do you know something?”

The furrows between his brows deepened.

With a clear smile on his face, he slowly reached out and rested a hand on my shoulder.

“If you’d made the same choice as them, I never would have forgiven you.”

Bow Saint spoke with a faint smile.

“Unfortunately, that won’t be happening. Your Disciple is far too good for that.”

A laugh escaped me before I knew it.

Yeah. That was probably true.

The Jeok Cheongang I knew had been that sort of person from the start.

First, he’d go find everyone who insulted his one and only Disciple and beat them to a pulp. Then he’d use whatever strength he had left to thrash his idiot Disciple soundly.

“Looks like you’ll have to use that strength somewhere else.”

Jeok Cheongang laughed out loud at that.

“That’s the plan. I’ll squeeze out every last drop of strength I’ve got.”

And before half a day had passed, his words became reality.
## Chapter artifact 1089

# Chapter 1089

Just as the hour of the Rooster began, an old beggar looked at the sun sinking little by little toward the western mountains and muttered to himself,

“How strange. It’s not time for the sun to set yet.”

The other beggars huddled around a nearby campfire reacted to his words.

“Then what about weather like this at this time of year? Does that make sense?”

“Right. It’s not like this just started yesterday or the day before.”

“Branch Master, don’t stand out there getting chilled by the wind. Come warm yourself by the fire. Have a bowl of hot soup, too.”

He had a point.

The world had been going haywire for more than a day or two.

The old beggar—or rather, Man Chong, Branch Master of the Beggars’ Sect’s Xining branch in Qinghai—let out a small sigh and walked toward the fire.

Gung Gibang, the Successor Beggar, had returned to Xining several days ago. Man Chong, however, had stayed behind with around thirty Beggars’ Sect disciples under his command to gather information.

“Got anything to eat?”

“Why, of course. Even if we don’t have a damn thing, we’re the sort who’ll find a way to fill our bellies.”

“You saved some for the ones out on patrol, didn’t you?”

“Come now. Do you take us for beggars with no sense of decency? Don’t worry. There’s enough for them to come back and eat their fill, too.”

One of the beggars grinned, yellow teeth showing, and offered him a steaming bowl. Man Chong found himself smacking his lips.

“That smells incredible.”

“Just eat it. You’ll see it tastes just as good as it smells.”

He was right.

Man Chong polished off the bowl in the blink of an eye, then patted his full belly with a satisfied smile.

It looked like a hodgepodge of the highest order, but perhaps because it had been made with fish freshly caught in Qinghai Lake, it tasted as if it had come from a first-rate chef.

*Well, I’m old. I deserve a little luxury like this.*

Drowsy with contentment, Man Chong picked his teeth with a fish bone and looked around.

As he watched the waters of Qinghai Lake slowly bathe in the sunset, he felt his worries wash away, if only for a moment.

Of course, the reality was still bleak.

*What good are a pretty view and a full belly? I can’t sleep easy until those bastards are gone.*

Dark Heaven. At the thought of those terrifying Fiends, a shadow fell over Man Chong’s face.

The situation had hardly improved, even after Jin Taekyung and the reinforcements passed through here and joined the others in Xining about four days ago.

No—the situation was getting worse by the day, as if to crush that brief glimmer of hope.

*At this rate, we’ll be surrounded from both sides for sure… Damn it. We’re caught in a hell of a mess.*

The mere thought of Dark Heaven’s massive army, which had already taken Kunlun Mountain, was enough to send a chill down his spine. And from the rear, bandits who’d dealt the Central Plains Murim a vicious blow were said to be swarming in like ants.

There was only one thing they had going for them.

Dark Heaven’s main force had yet to make a serious move.

*But that’s only a matter of time now. They’re coming, and soon.*

As far as that thought, the full feeling in his belly vanished. Anxiety and fear filled the space it left behind.

“……Damn it.”

His mood souring in an instant, Man Chong snatched up a pebble within reach and flung it as hard as he could.

Whoosh!

His clothes were shabby, but he was a master of the Beggars’ Sect with years of experience behind him.

The pebble shot from his fingertips toward the endless expanse of Qinghai Lake.

Splash!

The water split violently. Only then did the tightness in his chest ease a little. Man Chong snorted and turned away.

Or tried to.

He stopped when he saw the ripples from the pebble settle and the water slowly return to stillness.

*What is it?*

It didn’t take long for him to understand the sudden sense of déjà vu.

*The color. The color of the water…*

It was dark.

No—it was as black as if someone had poured ink into it.

The waters of Qinghai Lake, which had been tinted with sunset only moments ago, were no longer beautiful. Even the quiet conversations reaching his ears felt unusually ominous.

“Man, why’s it getting dark so fast today? Usually it takes half an hour for the sun to set.”

“What can we do about it? It is what it is. Have some more food before the patrol comes back.”

“I certainly won’t say no. Oh, Branch Master, would you like another bowl?”

Man Chong didn’t answer.

More precisely, he couldn’t.

At that moment, his instincts were sounding a red alarm in his head.

*Something’s… wrong.*

Of course, it could be nothing, just as the other Beggars’ Sect disciples seemed to think.

Frost had fallen before harvest season, and giant monsters with appearances that barely seemed human were running wild. What was left to be surprised by?

But he had a feeling he couldn’t explain.

The experience he’d built up in more than sixty years, the instinct of an old master etched into his bones.

“When will the patrol be back?”

“Huh? Why do you ask all of a sudden?”

“Answer me. Now!”

At the old Branch Master’s sudden bark—he was usually so easygoing—the startled Beggars’ Sect disciples stumbled over their words.

“Th-they should be back soon.”

“W-well, they’re about half a gak later than usual, but they must be close by now. There’s no need for you to worry, Branch Master. Ah?”

One of the disciples trailed off, eyes widening as he looked over Man Chong’s shoulder. Everyone turned to see what he was looking at.

On a low hill about two hundred zhang away, a group of riders had just appeared, tiny as specks. They were slowly descending the hill through the dim darkness.

“Speak of the devil. They’re right on time.”

“Look at those lazy bastards. They’re already late, and now they’re taking their sweet time?”

“Branch Master, you can relax. I’ll give them a proper scolding this time.”

As everyone tossed out remarks while watching Man Chong’s expression, he stared at the patrol with sunken eyes and muttered,

“Twelve.”

“What?”

“Twelve. Unless my eyes are wrong.”

“What does that—”

Someone began to ask, then suddenly faltered.

The patrol that had left about two shichen ago to survey the area had numbered ten.

“Th-that means…”

“Could be one of two things. Either they found survivors who made it through by sheer luck…”

Man Chong drew the iron staff, worn smooth from years of handling, from his waist and added quietly,

“Or some sons of bitches who deserve to be chewed up alive are pretending to be the patrol.”

“……!”

“Get to the boat now. We’ll raise anchor, put some distance between us, then see what happens.”

“W-we’ll do as you say!”

The disciples finally realized how serious the situation was and moved into action without another word.

By the time they’d boarded the boat moored by the shore and rowed far enough away, the mysterious group—friend or foe, they couldn’t tell—had reached the campfire they’d left behind.

“Seok Sam! Seok Sam, are you there?”

Man Chong’s sudden shout was answered from beyond the darkness, which had grown noticeably deeper.

“I’m right here! What is it?”

In that instant, Man Chong’s face went rigid.

So did every other Beggars’ Sect disciple’s.

No one among those who’d been staying at Qinghai Lake could speak informally to Man Chong, the oldest among them and their Branch Master.

But what shocked them more than anything was that the voice coming from beyond the darkness was exactly like Seok Sam’s.

“B-Branch Master…”

Leaving the Beggars’ Sect disciples behind, their faces pale as if they’d seen a ghost, Man Chong gritted his teeth and shouted again.

“Who are you bastards?”

A brief silence followed.

It lasted only a moment, but felt longer than ever—like an eternity.

Then an unfamiliar voice suddenly rang out, shattering the silence that seemed ready to suffocate them.

“Well, I guess beggar bastards are quick on the uptake.”

With a buoyant voice that even carried a hint of laughter, the figure that had only been a silhouette emerged into view, heading for the still-burning campfire.

Tap-tap.

Between the sparks rising into the air, a man and a horse crossed the gravel without a sound. Man Chong’s eyes widened at the sight.

“W-what is that…?”

For a moment, he was speechless.

Partly because of the skeletal horse, its white bones exposed, but more than that, because the man sitting casually atop it filled him with a fear he’d never experienced before.

Grin.

He showed his unnaturally white teeth—sharp fangs like a wild beast’s.

And those blood-red eyes, gleaming clearly even from far away, seemed to bind his body and mind just by meeting his gaze.

“Y-you…”

The man shrugged at Man Chong, whose body was trembling.

“You know who I am, more or less.”

His nonchalant manner only made him more terrifying. But Man Chong managed to force out his voice.

“The patrol… What happened to them?”

“Aw. How touching. Guess you’ve grown pretty attached to them begging for a living?”

“You bastard! Answer the question!”

“I mean, it’s hard to talk properly when a beggar’s yelling at you. Fine, fine. Don’t get so worked up.”

The man waved a hand as if to calm him down, then smacked his lips.

“To sum it up, they went to a better place. Though they didn’t taste like much.”

“W-what did you say?”

Man Chong froze, his mind settling on a suspicion too horrible to put into words. The man frowned.

“Hey, don’t get the wrong idea. Maybe it’s because they were mangy beggar bastards, but their bodies weren’t much to write home about either. I only drank a little blood, just to have some fun.”

“……!”

“What? Not what you expected? That voice was pretty convincing, though.”

Grit.

The taste of blood flooded Man Chong’s mouth.

Even so, he gritted his teeth with all his strength.

It wasn’t only the rage of losing a subordinate who’d been like a brother to him.

He had to clench his teeth. Had to do this, if only to bear the fear that was tightening its grip on him with every passing moment.

Dark arts.

The words had never seemed so chilling.

Nor had he ever felt as if his head could be severed at any moment by someone standing a hundred zhang away.

“So you’re the one. The leader we’ve heard about.”

“Well, let’s say I am. At least here, that person has entrusted everything to me.”

The man—or rather, the Blood Lord—looked at Man Chong with a smile.

Then he slowly scanned the twenty Beggars’ Sect disciples, frozen like statues around him, unable to react. Suddenly, he spoke.

“So, who’ll it be?”

“What?”

“I’m planning to let at least one of you live. You’ll be glad one of you survived, and I need someone to deliver a message. Seems like a good deal for both of us, doesn’t it?”

“……!”

“Quite a sight, those faces. What, did you think you could just run away?”

Grinning at their rigid faces a hundred zhang away, the Blood Lord suddenly turned around.

“Time to get moving, isn’t it? It’s something we have to do anyway.”

At his words, one of the figures lingering in the darkness stepped forward.

Swish.

Long robes brushed the gravel. The Grand Mage, as if the Blood Lord weren’t worth answering, passed him and reached the lakeshore. She extended her hand.

“Cold north wind…”

Wooooom.

The air trembled. A vast chill swept across the surface of Qinghai Lake.

And then, they saw it.

“Freeze.”

Rumble!

With a crack of ice, Qinghai Lake froze white.

“……!”

“……!”

Man Chong and all twenty Beggars’ Sect disciples stared, wide-eyed.

A miracle that should not—and could not—exist.

Faced with that unbelievable reality, they could do nothing.

Not even when the foul stench of monsters began to drift toward them from beyond the thick darkness in the distance.

Not even when the Blood Lord, crossing the frozen surface as casually as if out for a stroll, climbed onto the bow of their boat and looked down at them.

“Whoever survives, go tell them. I—the Blood Lord—am coming.”

At that moment, Man Chong forced out his voice with everything he had.

“You’ll never win…”

Crack!

Scarlet blood sprayed across the white ice.

“So, have you decided who gets to survive?”

In the cold, deep night, the Blood Lord’s blood-red eyes gleamed.

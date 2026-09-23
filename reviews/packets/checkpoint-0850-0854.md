# Checkpoint Review — 850–854

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

# Chapters 850–854

## Plot

The Divine Physician captures the Blood Soul Gu found in the deceased City Lord of Sichuan Province. Namho explains its origin in the Five Poisons Sect’s war with the Nanman Beast Palace and its effects: it weakens its host, causes episodes of madness, and eventually kills them. Jin suspects Dark Heaven brought it to the Central Plains as part of a scheme against the Great Nation, possibly involving the imperial family. He orders an investigation and considers Prince Shangshan Zhu Bao’s trembling token a key clue.

In Shanxi, Hong Jin asks a Lower District Sect contact to find Jin Taekyung, whom he trusts to protect Zhu Bao. An imperial party takes Hong Jin away, and he heads toward the unharmed prince. Meanwhile, Jin and Jeok Cheongang convene senior allies in Sichuan to discuss the Blood Soul Gu in secret. Reports reveal that disguised Embroidered Uniform Guard agents have moved through several provinces and gathered in Shanxi with Zhu Bao and Hong Jin. After a tracking team is wiped out, the Hidden Shadow Pavilion orders Jeok, Jin, and the entire Fire Dragon Pavilion to escort Zhu Bao. The group leaves to intercept him in Jiangsu.

At Yichang’s West Gate, survivors report that more than a thousand bandits and river pirates attacked a three-company caravan at Yuhua Mountain. After a three-day pursuit and the burning of their ships, fewer than a hundred of the roughly five hundred travelers survived. Two company masters were killed, and survivors say the attackers fought with unnatural ferocity. A middle-aged man with about ten companions arrives and asks who set the ships on fire.

## Continuity

- The Divine Physician secured the Blood Soul Gu found in the deceased City Lord of Sichuan Province. It weakens hosts, causes episodes of madness, and eventually kills them. The official account of the City Lord’s death is illness.
- Jin suspects Dark Heaven brought the Blood Soul Gu from Nanman and that the City Lord’s death may be part of a scheme targeting the Great Nation or its imperial family. The motive remains unknown.
- Prince Shangshan Zhu Bao is traveling with fifty Embroidered Uniform Guard members; Hong Jin joined him in Shanxi. Their expected route passes through Shandong and Jiangsu toward Zhejiang.
- A Shanxi tracking team was wiped out. The Hidden Shadow Pavilion issued an Alliance Leader-approved order for Jeok Cheongang, Jin Taekyung, and the entire Fire Dragon Pavilion to escort Zhu Bao; they have departed to intercept him in Jiangsu.
- At Yuhua Mountain, a caravan of three trading companies was attacked by more than a thousand bandits and river pirates. Fewer than a hundred of about five hundred survived; two of the three company masters were killed, and the attackers fought with unnatural ferocity.
- An unnamed middle-aged man with about ten companions has asked the survivors who set their ships on fire.

## Translation Decisions

- Render 血魂蠱 as “Blood Soul Gu,” 독혈지 as “Poisonblood Grounds,” and 대국 as “Great Nation.”
- Render 금의위 as “Embroidered Uniform Guard” and 옥화산 as “Yuhua Mountain.”
- Render 수적 as “river pirates.”

## Durable state

{
  "active_continuity": [
    "The Divine Physician secured the Blood Soul Gu found in the deceased City Lord of Sichuan Province; it weakens hosts, causes episodes of madness, and eventually kills them.",
    "Jin suspects Dark Heaven’s covert killing of the City Lord is part of a scheme targeting the Great Nation, possibly its imperial family.",
    "Prince Shangshan Zhu Bao is traveling with fifty Embroidered Uniform Guard members; their expected route from Shanxi passes through Shandong and Jiangsu toward Zhejiang.",
    "Hong Jin joined Prince Shangshan in Shanxi after requesting support from the Lower District Sect.",
    "A Shanxi tracking team was wiped out while following the group, and its operation was suspended over concern about official intervention.",
    "The Hidden Shadow Pavilion issued an Alliance Leader-approved order for Jeok Cheongang, Jin Taekyung, and the entire Fire Dragon Pavilion to escort Prince Shangshan.",
    "Jin and his party have departed to intercept Prince Shangshan in Jiangsu before the first of next month.",
    "A caravan of three trading companies, about five hundred people, was attacked by over a thousand bandits and river pirates at Yuhua Mountain; after three days of pursuit and the burning of their ten ships, fewer than a hundred survived.",
    "Two of the caravan’s three company masters were killed; survivors say the attackers fought with unnatural ferocity.",
    "A middle-aged man traveling with about ten companions has appeared before the survivors and asked who set their ships on fire.",
    "Jang Il is a gate commander at Yichang’s West Gate and is corrupt, though he considers himself moderate."
  ],
  "continuity_sources": [
    853,
    854
  ],
  "open_questions": [
    "Why did Dark Heaven secretly kill the City Lord of Sichuan Province?",
    "Is Dark Heaven targeting the Great Nation’s Emperor or imperial family, and is it influencing the Son of Heaven?",
    "What is the Embroidered Uniform Guard’s purpose in traveling with Prince Shangshan, and can Jin’s party reach him in time?",
    "What prompted the imperial decree against Hong Jin, and what will happen to him and Prince Shangshan?",
    "Who is the middle-aged man, and what explains the attackers’ unnatural ferocity and the assault on the caravan?"
  ],
  "safe_through": 854,
  "temporary_decisions": [
    "Render 혈혼고 as “Blood Soul Gu.”",
    "Render 독혈지 as “Poisonblood Grounds.”",
    "Render 대국 as “Great Nation.”",
    "Render 금의위 as “Embroidered Uniform Guard.”",
    "Render 옥화산 as “Yuhua Mountain.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 850

# Chapter 850

Blood Soul Gu.

The name of the gu poison Namho had identified was ominous enough on its own.

*Not that I’d ever seen a gu poison in person before.*

I muttered to myself and studied the tiny creature writhing in the Divine Physician’s palm.

It was much smaller than a grain of millet, its threadlike body entirely bloodred.

It looked impossible to make out with the naked eye, and it kept struggling to burrow into the Divine Physician’s skin.

As though that were its sole reason for existing.

“If I hadn’t been careful from the start, it would’ve caught me off guard. It’s incredibly strong for something so small.”

Sssk. Ssssk!

As if it understood what he’d said, the Blood Soul Gu struggled even harder, trying to escape. The Divine Physician carefully enclosed it, took out a tiny gourd, and slipped it inside, then sealed the stopper tight.

Only after checking several times for any gaps did he remove the thick leather gloves he’d been wearing.

“Blood Soul Gu. I’ve received countless lessons from my Master over the years, but…to be honest, even I have never seen a gu poison like this.”

Namho nodded at the Divine Physician’s murmur.

“That’s only natural. Blood Soul Gu is a venomous creature scarcely known even in Nanman. More precisely, there can’t be many people left who still remember the name.”

“You mean…”

“It was a very long time ago. Nanman was divided into three rival powers, like a three-legged cauldron, and they were locked in a horrific war. That was when Blood Soul Gu first came to light.”

I couldn’t have been unfamiliar with that story.

I’d heard it several times while staying in Nanman, and if you went back far enough, it was connected to my own sect, the Fire Gate Clan.

It was a story from the past, passed down like a legend through word of mouth and the few records that remained.

And at its center, one sect always appeared.

“…The Five Poisons Sect.”

I murmured the name like a groan, then looked at Namho.

“So Blood Soul Gu originated with the Five Poisons Sect?”

“It happened so long ago that I can’t be certain. But if everything I saw and heard while staying in Nanman is true, Blood Soul Gu was one of the venomous creatures the Five Poisons Sect created after countless attempts.”

“But I never saw anything like this in the Poisonblood Grounds.”

“Gu poisons prefer deep, secluded places. Even if you searched the Poisonblood Grounds as thoroughly as if you were tearing apart a beehive, would this one have been easy to spot?”

He had a point.

The Poisonblood Grounds were crawling with all sorts of bizarre monsters, including the Thousand-Year Spider. In all that chaos, there was no way to identify every creature—including something as hard to see as Blood Soul Gu.

“I’ve heard of the Five Poisons Sect, too. One of the Four Founders of our sect left behind a brief record about Nanman.”

Jeok Cheongang had spoken up without warning. His sunken gaze rested on the gourd holding Blood Soul Gu.

“But that thing is too different from an ordinary gu poison. Its vitality is so tenacious it could survive being pierced through the body with a large needle. And it doesn’t have enough deadly poison to kill its host outright, either.”

“That only makes it more likely to be Blood Soul Gu. Senior Jeok, the gu poisons you’re thinking of cause no trouble as long as the host takes the antidote at regular intervals.”

“That’s what everyone knows.”

“But Blood Soul Gu is different. Ordinary gu poisons are used to threaten and control their hosts. The Five Poisons Sect created that dreadful creature for one reason alone.”

Under everyone’s gaze, Namho let out a breath he’d been holding and finished his thought.

“To kill its host. In a way, it was close to a perfect assassination.”

“……!”

“I spent a long time in Nanman collecting information. I searched through every scrap of what little remained in the records, and sought out the oldest and wisest people from each tribe. I had to feel my way toward the truth in their stories, then sift out whatever might be false.”

One day, after the great war called the Great Faction War had ended, the Martial God vanished without a trace.

Hundreds, even thousands, of sects bound together by every kind of interest and emotion had lost their focal point. Perhaps it was only natural that they began to collapse.

The dissolution of the Murim Alliance.

But the roots of the Hidden Shadow Pavilion remained scattered throughout the world. In a shabby old inn slowly falling apart. On crowded thoroughfares.

And in the remote reaches of Nanman, where venomous creatures and fierce beasts ran rampant.

Namho was one of its deepest and oldest roots.

“The war between the Five Poisons Sect and the Nanman Beast Palace was truly fierce. Sometimes the two sides were evenly matched; at other times, one gained the upper hand.”

The war, they said, had lasted a hundred years. The wells and rivers were poisoned, and the warriors and beasts of the Nanman Beast Palace cut down and tore apart the Five Poisons Sect’s Poison Men.

“All of Nanman was engulfed in poison and flames. If things had continued that way, there would have been no victor or loser—only mutual destruction.”

Namho looked back and forth between Jeok Cheongang and me, then continued.

“Until one day, when an outsider appeared.”

The leader of the Fire Gate Clan, who was traveling the world at the time, received a grand welcome the moment he arrived in Nanman.

A hundred warriors from the Five Poisons Sect welcomed the stranger who dared enter their territory with poison and hidden weapons. That stranger promptly burned everything to the ground, then joined forces with the Nanman Beast Palace.

“With the Fire Gate Sect Leader’s arrival, the tide turned sharply. The Five Poisons Sect must have realized they had nowhere left to retreat. As time passed, they began unleashing things more and more dreadful and vicious.”

When people have lost nearly everything, all that remains is their spite.

The Five Poisons Sect prepared its final counterattack in the deepest reaches of Ailao Mountain, at the Poisonblood Grounds—the most secret and dangerous place of all.

“Near the end of the war, the best warriors of the Nanman Beast Palace began dying one after another. Neither the physicians versed in poison and medicine nor the spiritually gifted priests knew why.”

The Divine Physician, who’d been listening to Namho in silence, spoke with a grim expression.

“They must not have shown any visible injuries.”

“You’re right. It wasn’t poisoning or a plague. The Nanman Beast Palace realized what was causing it only after the number of dead warriors passed a hundred.”

“Even if Blood Soul Gu was so small and stealthy that it was difficult to find, surely they could have discovered it sooner once so many people had died.”

“I thought so, too. But it seems there was a good reason.”

Namho shook his head slightly and continued.

“Everyone was exhausted from the hundred-year war. The word ‘peace’ had long since lost its meaning, and death was seen as a form of rest. In those circumstances, it might have seemed only natural that some warriors were afflicted with madness.”

“Madness…?”

“That’s right. They said most of them would act like they’d lost their minds one day, then fight more bravely than anyone the next.”

The Divine Physician murmured as if sighing.

“City Lord. That was exactly how the City Lord behaved. When I first heard about it, I thought it was a mental illness brought on by losing his beloved concubine.”

“Blood Soul Gu grows stronger when its host’s mental strength weakens, so the two are likely connected.”

“Then how did the Nanman Beast Palace learn the truth?”

“They said the information came from interrogating an Elder of the Five Poisons Sect after capturing him. At first, it wandered through the duodenum and the acupoints, using mild poison to cause auditory and visual hallucinations. In the end, it gradually ate away at the brain and drove its host to death.”

“……!”

“Each warrior died at a different time. Some held out for as little as six months; others lasted several years.”

“So they only begin to act once their host’s body and mind grow weak.”

“That’s right. But their killing power and the time they took fell far short of what the Five Poisons Sect had originally wanted. Perhaps that’s why they managed to improve so few specimens before the sect was destroyed. That’s everything I’ve learned.”

After Namho finished, a heavy silence fell.

No one spoke, but it wasn’t hard to imagine what the others were thinking.

A great war that had drenched Nanman in blood for more than a hundred years.

And now, after all those years, Blood Soul Gu had appeared once more—in the body of a government official from the Great Nation, someone who wasn’t even a martial artist.

I closed my eyes and muttered to myself.

No. The two characters had been circling in my mind ever since I learned Blood Soul Gu came from Nanman. I finally said them aloud.

“Dark Heaven.”

The darkness before my eyes cleared. When I opened them, I saw three faces looking at me beneath the soft light of the night-shining pearls.

“Blood Soul Gu was almost forgotten in Nanman. The only way it could have made its way to the Central Plains is if they brought it here. This is definitely their doing.”

Jeok Cheongang spoke in a low voice.

“The Southern Heaven Demon Empress.”

“It’s been decades. Dark Heaven set foot in Nanman and waited for its moment in the Poisonblood Grounds. They had more than enough time to find Blood Soul Gu.”

“More than enough. No, plenty.”

Jeok Cheongang nodded slightly, then asked,

“But why would they harm this man?”

“That…”

My voice trailed off as I looked down at the City Lord of Sichuan Province’s corpse.

His arms and legs were cold. His face was as white as paper, with no trace of pain.

Yes. Jeok Cheongang’s question was the key.

Why had they killed this man? Why use such a secretive method?

He’d held the high office of City Lord, but that was all.

A corrupt, moderately greedy official, the kind you could find anywhere.

If Dark Heaven wanted, they could take his life as easily as pulling a coin from their pocket.

*So why go to all this trouble?*

Was it because the City Lord had mobilized the government troops to help us during the Sichuan Blood Tragedy?

The thought crossed my mind, but I shook my head.

No. If they wanted to retaliate, a far more horrific death would have been a hundred times better.

Even if he was a high-ranking official like the City Lord, they could make sure the whole world knew that no one should dare stand against Dark Heaven again.

Even those who thought themselves separate from Murim would have reason to fear them.

*But if they chose this method anyway…*

There was something else. Some still-unknown goal that Dark Heaven truly wanted to achieve.

And just as my thoughts, one after another, reached that point—

Tap.

A faint footstep from somewhere broke my concentration. I instinctively turned toward the sound and saw a small maid standing there, her face full of fear.

“Um, well…”

Her hands were clasped tightly together. She looked at us anxiously and continued in a voice barely louder than a whisper.

“I-I’m sorry, but the new City Lord asked me to find out when you’d be finished talking…”

Damn it. How could something as trivial as that ruin my concentration?

I frowned without meaning to. Then a flash of insight suddenly shot through my mind.

The new City Lord. Ju Wongong. One of the few remaining members of the imperial family.

And the reason Dark Heaven had needed to deal with the City Lord of Sichuan so secretly. No—the suspicion.

If my hunch was right, this was only the beginning.

The City Lord’s death was a signal of Dark Heaven’s sinister scheme—and enough to make me suspect they were targeting one place.

*The Great Nation.*

A chill ran up my spine.

I watched the maid hurry away, then managed to force the words out.

“We need to send people out immediately. Find out everything about the City Lord of Sichuan and Ju Wongong. No—the Emperor and all his relatives, too.”

At the same time, someone’s name rose to the surface of my memory.

Someone closer to the title of Son of Heaven than Ju Wongong, a distant member of the imperial family—or any other royal left in the world.

And someone who could be the most important key of all.

“…Zhu Bao.”

“What?”

“Prince Shangshan. Zhu Bao.”

Inside my firmly shut Inventory, the token that little boy had given me seemed to tremble.
## Chapter artifact 851

# Chapter 851

It was an especially beautiful day.

Warm sunshine, a cool breeze, and even wisps of pure white cloud.

The people working up a sweat wore smiles, and the well-kept main road bustled with crowds.

Perhaps that was why someone who was always living as though pressed for time suddenly spoke to the coachman, who was about to set off in a hurry.

“Could we take it a little slower today? There’s no particular rush.”

“Pardon?”

“I’d like to take my time on the way back. Look around outside, too.”

The coachman wondered at his employer’s uncharacteristic mood, but put the question aside and eased the reins.

All he had to do was follow orders, after all.

And as a coachman, he much preferred guiding the horses slowly and safely to shouting at people to get out of the way.

*Still, he’s acting strange today. Did something happen inside?*

The coachman glanced sideways. A sturdy wall, built high in two or three layers like a fortress, came into view.

On an ordinary day, perhaps not. But at this pace, it would take a full fifteen minutes to reach the end of that wall.

*Good grief. It’s impressive no matter how many times I see it.*

The coachman silently marveled. This enormous estate stood not on the outskirts, but right in the center of a city. Prime real estate among prime real estate.

The fact that the family owned so much land in the very heart of the city was proof enough of its tremendous power, but that wasn’t what amazed the coachman most.

*It was nothing like this when I first saw it.*

A fallen great family.

There was probably no more fitting description.

That was the cold reality, and not just the coachman but everyone nearby had thought so.

Yet no one could have guessed.

That a family slowly declining, its past glory behind it, would rise in barely more than two short years to become the power ruling over an entire city.

*Just goes to show, you never know what’ll happen in this world.*

Muttering to himself, the coachman looked up at the flag rising high above the stone wall.

The silk fluttered in a breeze from somewhere, and four characters written in a bold, flowing hand caught his eye.

Jin Family of Taiyuan.

The owner of that enormous estate, and a family that had become a symbol of Shanxi Province.

The changes surrounding the Jin Family of Taiyuan had been swift and undeniable.

The pavilions and walls, once shabby and crumbling, had been repaired until they looked as solid as a fortress. The martial artists, supplied with fine weapons and elixirs, now had a righteous spirit in their eyes the coachman had never seen before.

And that wasn’t all.

The entrance, once crowded with debt collectors demanding payment for the reckless Third Young Master’s unpaid bills, was now so packed you could hardly set foot inside—but for entirely different reasons.

There were wealthy merchants from other regions, come to entrust their business to the Jin Family Escort Bureau. There were shopkeepers of every kind, lined up to pay tribute at the end of each month, as well as martial arts sects and Branch Leaders under the Jin Family of Taiyuan.

So many important people from all over Shanxi Province came and went that the threshold was worn down. Some people with nothing better to do even loitered around the Jin Family of Taiyuan, chatting about what they’d seen and heard.

Just like the two men squatting beside the wall at the roadside right now.

“Didn’t she come today, either?”

“Didn’t who come?”

“Oh, come on. You know perfectly well who I’m waiting for. Why do you keep asking?”

“Don’t tell me you’re at it again…”

“What do you mean, ‘don’t tell me’? I’ve been devoted to her from the start.”

“Cut the nonsense. If your wife catches you, she’ll beat you to death—and then I’ll get killed, too.”

“It’s fine. You only die once, don’t you?”

“I’m telling you, it’s not fine. Your wife’s arm is thicker than my calf.”

“Good grief. You’re a man, and you’re scared? Just answer my question. Didn’t she come today, either?”

“She was here just four days ago. Of course she didn’t come today. Do you think she’s an unemployed layabout like us, with nothing but time on her hands?”

“Damn it. I thought maybe this time I’d get to see her up close.”

“Just give it up already. What would you do if you saw her up close?”

“Do I need another reason to see Shanxi’s foremost beauty? I saw her from far away once, half a year ago, and my blurry old eyes cleared right up.”

“Have you considered that one good whack from your wife might make everything go dark? And calling her Shanxi’s foremost beauty hardly does her justice. She leads the Mount Heng Sword Sect despite being a woman—and she’s formidable. If you cross her the wrong way, you won’t walk away in one piece.”

The man gazed dreamily into space, then suddenly swallowed.

“…Well, I heard she’s got some old man following her around like a shadow, and he’s got one hell of a temper.”

“If temper were all he had, would they have called him the Tiger of Mount Heng? Quit acting up and go home while both your legs still work. Take care of your kid.”

“Take care of him? He’s all grown up.”

“Already? Time flies. I remember him being born just about this time last year.”

“Yeah. That’s right.”

“…Are you insane?”

The two men’s low conversation gradually faded away.

The coachman, who’d been listening to them, gave a quiet laugh and took hold of the reins he’d let slacken for a moment.

Clip-clop. Clip-clop.

The carriage, drawn by four fine horses, crossed the main road slowly, just as his employer had asked.

In the past, a single four-horse carriage would have taken up half the street. But now the road was several times wider, and the crowds packed into it simply moved aside a little and carried on with their conversations.

Most of what they said was ordinary gossip, but from the coachman’s perspective, some of it was worth listening to.

“Have you all heard the rumors? The Jin Family of Taiyuan’s blacksmith shop has been making nothing but weapons lately.”

“I thought you were about to say something important. That’s been going on for a while, hasn’t it? The Jin Family of Taiyuan is a Murim sect. It’s hardly strange.”

“True. But for the past six months, they’ve been dealing exclusively in weapons. If you want to buy farming tools, you’ll have to go at least as far as Gohyeon.”

“Well, now. Gohyeon’s a good three or four days on foot. Luckily, the tools we bought ahead of time are sturdy enough that we won’t need to buy more.”

“That’s because the craftsmen Old Man Jang brought with him are so good.”

“Hey, don’t call him Old Man Jang. The Jin Family of Taiyuan trusts him with important work. We ought to call him Master Jang Taebo now.”

“Ah, it’s just a habit. Anyway, the more I think about it, the more worried I get. Things in the martial world are supposed to be tense these days. Do you think something big is really about to happen…?”

“Put your worries aside and finish your game of Go. Dark Heaven or whatever can make all the trouble it wants; in the end, it’s a Murim affair. The Great Nation is out there, and the Jin Family of Taiyuan is standing firm right here. What’s there to worry about?”

“I only said it because the rumors coming from all over don’t sound good. Things up in the northern plateau, which had been quiet for the past year or two, too. The currents in the martial world don’t seem normal.”

“What’s going on in the northern plateau now? The Jin Family of Taiyuan must have gone out and wiped out the mounted bandits.”

“Do mounted bandits disappear just because someone uproots them once? They’re weeds. They keep cropping up. And a few merchant caravans that headed north last month…”

Even with his employer’s instructions, there was only so long the coachman could keep the horses moving slowly.

*Come on, get to the point.*

Just as he was silently licking his lips, curious about the rest of the story he hadn’t managed to hear, his employer—who had been staring out at the scenery without a word all the way out of the main road—suddenly spoke.

“Everyone has a lot to worry about. Then again, when it’s happening around you, it’s hard not to notice.”

“Y-yes?”

“I mean those people. You’ve been listening with your ears pricked up this whole time, so why are you acting so surprised?”

“Uh, well. It’s just…”

The coachman swallowed and stammered on.

“You’ve never spoken to me first like this before, so I was caught off guard.”

“Ah. Well, when you put it that way, I suppose.”

The coachman glanced over his shoulder. Through the beaded curtain, he caught a glimpse of his employer nodding as if it were nothing.

The skin powdered pure white, and lips red as cherries, too.

*No matter how I look at it…he’s definitely acting differently than usual.*

What had gotten into him?

The coachman had served him for nearly a year, but after all he’d seen and experienced, his employer remained a mystery.

He was always smiling, but for some reason it never seemed like a genuine smile. And there was only one occasion when he ever spoke first to the coachman.

When they reached their destination.

A brief “Thank you for your hard work” was both the beginning and the end of their conversations.

*But today he spoke first, and he hasn’t even looked at his bamboo slips while we’ve been on the road.*

His high-ranking employer was always busy. There was a mountain of work to handle and people to meet everywhere.

The coachman had watched him like that for the past year, so it was only natural that his employer’s mood today felt so unfamiliar.

Maybe that was why a pointless curiosity, one he would never normally have let show, instinctively moved his lips.

“Um, has something happened?”

“Hm?”

“Ah, well…”

The coachman regretted the question as soon as he asked it. There was nothing to gain by upsetting his employer—especially when his employer was a high-ranking official.

But his employer proved far more generous than the coachman had expected.

“Hm. Something happened? Yes, it did. I heard some unpleasant news not long ago.”

“I-I’m sorry.”

“No, why apologize over something like this? When you bow and scrape too much, it makes me uncomfortable, too. It brings back memories from long ago.”

“Pardon?”

“Memories I never want to return to. For example…”

His employer’s voice trailed off, and he suddenly gazed out the window.

Beyond the wooden lattice, children were laughing in a clean, orderly street.

“Something like going out into the street after going three whole days without food, singing to impress people in silk robes.”

“……!”

“Oh, don’t get the wrong idea. I’m not saying that to make you feel bad. It’s just something that happened.”

The coachman’s mouth fell open at the unbelievable past of such a high-ranking person. His employer, meanwhile, watched the people passing slowly by and smiled faintly.

“It’s nice to see everyone looking so happy.”

It had happened a very long time ago.

But in someone’s memory, it was also a brand that would never fade.

Poverty. Death. Sorrow. Anger.

The days spent doing everything he could to escape the shackles that had gripped his throat since birth flashed past.

“I managed somehow back then…but can I do it this time, too?”

The quiet mutter was carried away by the wind.

The coachman didn’t dare say another word. He kept guiding the horses onward, while his employer took in everything slowly passing by.

And as the destination drew nearer, the hoofprints in the ground grew clearer. At last, he knew the time had come.

“Could I ask you a favor?”

“A favor…sir?”

His employer suddenly spoke, then nodded at the coachman’s question.

“Yes, a favor. And an apology, too, for not having been very kind to you until now.”

“Th-there’s no need to say that, sir. If you need anything, please just give me the order. Deputy Military Commissioner.”

His employer—or rather, Hong Jin, Deputy Military Commissioner of Shanxi Province—parted his red lips.

“I’m going to get off here. Go to Honghwaru right away and tell them. Or should I say the Lower District Sect’s Shanxi branch?”

“……!”

“You thought I wouldn’t know, didn’t you? But they’ve probably figured it out to some extent already. No matter how secretly the Embroidered Uniform Guard operates, they can’t avoid that many eyes.”

The fact that Hong Jin knew his identity, and the existence of the Embroidered Uniform Guard, said to act only on the Emperor’s orders.

The coachman couldn’t even tell which of those two things he ought to be more surprised by. Then he realized what he needed to ask.

“What would you like me to do, Deputy Military Commissioner?”

“Tell them everything that’s happened. And have them use every bit of the Lower District Sect’s information network to find one person.”

“One person, you say?”

“Someone who can protect us in any situation—or rather, His Highness Prince Shangshan. The most trustworthy person in all Murim.”

Hong Jin spoke slowly, but with emphasis.

“The Blazing Flame Divine Dragon, Jin Taekyung.”

“……!”

“Go. Hurry.”

That was all.

The carriage sped away like the wind, and Hong Jin watched it disappear before suddenly turning around.

A group arrived in a rush, the sound of their horses’ hooves growing louder.

“We have an imperial decree. You’ll have to come with us, Deputy Military Commissioner.”

“And His Highness Prince Shangshan?”

“Rest assured. He is unharmed—for now.”

“For now… Well, fine.”

Hong Jin smiled.

Then he set off toward his young lord.
## Chapter artifact 852

# Chapter 852

The ways a Murim martial artist could get information were extremely limited.

The easiest place to start was an inn or a pleasure house.

They were packed with all kinds of people from all kinds of professions, so you could hear countless stories just by listening a little.

The downside was that none of the important information was there. Most of it was unverified rumor.

So martial artists with heads that weren’t just for decoration, and who’d spent some time earning their keep with a sword, went to information merchants instead.

These professionals bought and sold information in every region. Their prices were steep, but their information was reliable.

The problem was that there were clear limits to what they could gather.

They could provide high-quality information about the region where they were based, but that was as far as it went.

And so, the paths of those with money, a respectable sect behind them, and a few useful connections naturally split in two.

The Lower District Sect.

And the Beggars’ Sect.

They had taken root throughout the land. The weeds of this world, gathering one by one until they’d grown into vast forests of their own.

The Beggars’ Sect was one of the Nine Sects and One Gang, so there was no need to explain its importance. But the Lower District Sect was a force that couldn’t be dismissed, either.

Waiters and courtesans, coachmen and pickpockets. Back-alley gamblers and merchants running shops of every size.

Like the beggars of the Beggars’ Sect, they were everywhere in the world.

With such vast networks, they combed the land and hauled in information by the basketful. Even the Sect Leaders of the most prestigious Murim sects couldn’t treat them carelessly.

Of course, there were exceptions to every rule.

“Gather everyone.”

“Pardon?”

“Gather everyone. You have half a day. To the Sichuan Tang Clan.”

At least for today, Jeok Cheongang was a Grand Mage.

In precisely half a day, he’d summoned the Lower District Sect and the Beggars’ Sect, along with the Qingcheng and Emei Sects, and seated them all in one place.

“Um, may I ask why you’ve called us here so suddenly…?”

“Quietly plant yourself in a corner and sit there. You need to hear this, too.”

Of course, Tang Sadok, the Family Head of the Sichuan Tang Clan, was there as well.

But what surprised everyone except Jeok Cheongang was that the Sect Leaders of Qingcheng and Emei had come in person.

“I, Bicheonja of the Qingcheng Sect, a junior of the Murim, pay my respects to you, Senior.”

Sect Leader of the Qingcheng Sect or not, in front of Jeok Cheongang, he was a junior of the Murim.

Bicheonja was clearly fresh from a desperate, sweat-soaked dash. Jeok Cheongang nodded at his cupped-fist greeting. No—at the greeting of Cheongpung the Ancient Sword, as he was better known in the Murim.

“So, is your master still doing well these days?”

“……He passed away twenty years ago.”

After a brief silence, Jeok Cheongang spoke without batting an eye.

“I was asking whether you’ve been tending his grave. No matter how busy you are, visit often and pull the weeds.”

“……Yes. I’ll remember that.”

Anyone could see Jeok Cheongang had forgotten, but Cheongpung the Ancient Sword showed the patience of a Daoist and took his seat.

No, maybe it was more accurate to say he let it slide because his opponent was the Fire King, Jeok Cheongang.

There was no one in the Murim who could match his seniority, and he was overwhelming in both age and martial arts.

But Extinction Divine Nun, who’d taken the vacant post of Emei Sect Leader after the Sichuan Blood Tragedy, was someone even Jeok Cheongang couldn’t treat carelessly—at least, given her age.

“You’re here, old hag.”

“……”

“……”

I take it back. I must’ve been mistaken.

*He’s treating her however the fuck he wants. Seriously.*

I pressed a hand to my forehead, while everyone else’s mouths fell open.

At least there was one saving grace: Extinction Divine Nun, who was famous for rampaging like a madwoman on the battlefield, was usually an exceptionally gentle person.

“Benefactor Jeok, you’re just as I remember you, no matter how long it’s been. In more ways than one.”

“Old hag, you’ve gotten older since I last saw you. It feels like forty years, not four months. I mean that literally.”

“Amitabha. At your age, you should’ve grown up long ago. When are you going to start acting your age?”

“I’ve grown about a hundred years younger, so I plan to live like this for another hundred. Though by then, Venerable Nun, you’ll no longer be of this world.”

“……Amitabha. That was too harsh.”

“If you’re that offended, you should Return to Youth yourself.”

“Amitabhaaaaa!”

I sensed we were in deep shit and hurriedly stepped between them. It was the best move I could’ve made.

If they’d traded one more line, Extinction Divine Nun’s wooden prayer block would’ve come down on Jeok Cheongang’s skull.

Of course, Jeok Cheongang wouldn’t have just let her hit him. The important thing was that Extinction Divine Nun’s anger quickly subsided when I appeared.

“Oh, Benefactor Jin.”

“Have you been well, Venerable Nun? No—I mean, Sect Leader.”

“You needn’t be so formal. Call me whatever feels comfortable. In any case, you’ve become even more striking since I last saw you. And your hair’s still so thick.”

Extinction Divine Nun added that last part while glancing at Jeok Cheongang, then patted my shoulder with her wrinkled hand.

Perhaps because she’d thought so highly of the way I’d rushed around trying to minimize the damage during the Sichuan Blood Tragedy, both she and Cheongpung the Ancient Sword were looking at me with stars in their eyes.

“Before we begin, I must say you’ve been through a great deal. I hear you distinguished yourself against Dark Heaven’s fiends in Nanman and even brought the Nanman Beast Palace into the alliance?”

“Fellow Daoist Jin’s chivalrous spirit is truly remarkable. I, too, can’t help but admire you.”

Words could travel a thousand li without legs.

Word had already spread among those with even a halfway decent information network. And that went double for the people gathered here today.

Two Sect Leaders from the Nine Sects and One Gang, not to mention the heads of the most powerful information organizations in the land.

“Congratulations, though belated, Great Hero Jin Taekyung. Our Shaanxi Branch Leader was delighted when he heard the news.”

“I only wish that brat Gung Gibang—or rather, the Successor Beggar—could follow your example, even halfway. Anyway, what you did was incredible.”

The Lower District Sect’s Sichuan Branch Leader politely offered his congratulations, mentioning Wolhwa, who was in Shaanxi. An Elder of the Beggars’ Sect chuckled and jabbed me in the side, but at a single remark from Jeok Cheongang, his laughter stopped dead.

“Where’s the Sect Leader? Why’s some no-name Elder hanging around?”

“……Sir Jeok, even so, how could we bring the Sect Leader from Henan in half a day?”

“Henan? Is that bastard in Henan right now?”

“Yes.”

Getting from Henan to Sichuan in half a day would’ve been impossible without a jet.

Jeok Cheongang seemed to accept that the Elder had a point and started looking for another target.

“Hey, you. Lower District Sect.”

“Yes, sir.”

“Where’s the Sect Leader?”

“I’d be more than happy to bring him here, but even I don’t know where he is. Our sect is organized into cells, so his location is top secret…”

“So a nobody who doesn’t even know where his own Sect Leader is showed up?”

For a Lower District Sect with countless members, a Branch Leader was on the same level as a Beggars’ Sect Elder. The Sichuan Branch Leader swallowed hard under Jeok Cheongang’s pressure.

“Of course not. Whatever information you want, we’ll get it by any means necessary and bring it to you as quickly as we can!”

“Whatever you want. By any means necessary. As quickly as you can?”

“Yes, sir.”

“That sounds pretty good. I’ll remember it clearly, so you remember this one thing, too. Understand?”

“I’m not sure what you mean…”

The Lower District Sect Branch Leader’s eyes wavered. Just then, Jeok Cheongang’s voice rang out, low and heavy.

“If even a single word of what’s said here today gets out…”

Whoooosh.

He didn’t finish the sentence, but he didn’t need to.

The terrifying wave of energy that rolled out from Jeok Cheongang was a wordless warning—a precaution against the unlikely but possible mishap.

And there wasn’t a single person here too slow to understand what he meant.

They all understood that something important was about to be discussed.

“Around noon today, the City Lord of Sichuan Province died.”

With Jeok Cheongang’s first words, the curtain rose. Every eye turned toward the Divine Physician and Namho as they stepped forward.

“The late City Lord died of illness. His physical and mental strength had declined sharply over the past few months, and that led to his death.”

“The renowned physicians in the area have already examined the body at the City Lord’s Residence and reached the same conclusion. The Divine Physician here has as well.”

I added quietly, “There’s no room for suspicion. It’ll be reported as a natural death. At least, officially.”

I could feel the air around us shift.

*Officially.*

Anyone could tell those words carried weight. They implied a secret that wasn’t meant to reach the outside world.

At my subtle glance, the Divine Physician nodded, took a small wooden case from his robe, and carefully opened it.

“This is known as Blood Soul Gu.”

The people who saw it stared wide-eyed. It was smaller than any bug I’d ever seen, and red as spilled blood.

* * *

By the time everyone had left, evening had fallen.

Jeok Cheongang and I were the only ones left. We stood together, looking out at the pitch-black darkness all around us as we talked.

“How long do you think it’ll take?”

“Who can say? All we can do now is trust them and wait.”

“If we wait, we’ll be too late. We need to move.”

“If we take one wrong turn, it’ll take even longer to get back. Besides, haven’t we already gained something from their information?”

I nodded without a word.

Just as Jeok Cheongang said, we’d already received information from the Lower District Sect and the Beggars’ Sect.

*The Embroidered Uniform Guard.*

No one living in this land could fail to recognize that name.

One of the Great Nation’s most powerful and secretive forces, acting only on the orders of a single person.

They’d shown themselves—and well before we arrived in Sichuan.

In Anhui Province, not Zhejiang Province, where the Great Nation’s capital and the Emperor’s residence were located.

*And they’d been disguised, unlike usual.*

Why had the Embroidered Uniform Guard—an agency directly under the Emperor—appeared in Anhui Province, even changing their identities?

We had no way to learn more. The informants who’d caught their scent and followed them had been found dead. But I couldn’t help making a grim assumption.

*If they hadn’t stopped in Anhui and had kept heading northwest…*

That would take them to Shanxi Province. And he was in Shanxi Province.

*Prince Shangshan, Zhu Bao.*

The only direct member of the imperial family the current Son of Heaven had spared after winning the horrific power struggle over the throne.

The only vassal king in the land, and—since the Son of Heaven had no heir—the current successor to the Great Nation’s throne.

*But the Emperor, who’d been quiet until now, has set the Embroidered Uniform Guard in motion. And so secretly, too.*

If their destination was Shanxi Province… I couldn’t help anticipating the worst.

That the shadow of Dark Heaven had reached the Great Nation’s imperial family.

*The Captain of the Guards said the City Lord of Sichuan Province had started showing signs of madness after the Son of Heaven took his favorite concubine. And the Blood Soul Gu found in his body was so rare that I’d never even seen one in the Poisonblood Grounds in Nanman.*

There was enough evidence. I silently stared up at the night sky, lit only by the hazy moonlight.

A question that would reach no one.

*What the hell are you after?*

And then, at that very moment—

A faint sound came from somewhere in the sky and reached my ears.

No. It reached both our ears.

Flutter.

“Old Master.”

“This is…”

It wasn’t the wind. Something was flying toward us, beating its wings through the air.

*A messenger pigeon!*

The moment I realized it, Jeok Cheongang and I both looked toward the distant sky. Our eyes widened.

Whooosh!

The shadow of a bird raced toward us, slicing through the wind. There were more than ten of them.
## Chapter artifact 853

# Chapter 853

Information is like a puzzle that can never be completed with just one piece.

Unless you gather the pieces and fit them together, they’re not information at all—just questions with no value.

The Embroidered Uniform Guard who appeared in Anhui about fifteen days ago was no different.

They were just one small piece.

At least, they were until the City Lord of Sichuan Province died suddenly and the Blood Soul Gu was discovered.

*Things are different now.*

Emei and Qingcheng, members of the Nine Sects and One Gang; the Sichuan Tang Clan and the Beggars’ Sect—and even the Lower District Sect, whose ranks were largely made up of commoners—were all bona fide Murim organizations.

Now that a full-scale war with Dark Heaven had begun, information about the government was bound to fall down the list of priorities.

If your own neighborhood is on fire, you’d have to be crazy to go looking around the neighborhood next door.

But if the fire spread there, that changed everything.

We had to dig up every puzzle piece of information that had gone unreported for one reason or another—or been dismissed as mere suspicion.

And the dozen or so messenger pigeons that had just arrived at the Sichuan Tang Clan were carrying precisely those pieces.

“Have you arrived, Old Master? You too.”

It went without saying that the most important matters were reported to the Family Head first.

A scattering of tightly sealed missives lay in front of Tang Sadok, who had greeted Jeok Cheongang and me with a brief nod.

“Are those all… messages related to this?”

“Probably.”

At Tang Sadok’s brief reply and glance, the old man beside him—who had been carefully inspecting the messenger pigeons and their missives—spoke up.

“From what I’ve seen, there’s no sign the messenger pigeons were attacked, and none of the missives have been damaged.”

“Are you certain? This is important.”

“I stake my life on it.”

“That’s enough for me. I’ll send for you when the time comes. Until then, don’t let anyone in.”

“Yes, Family Head. I won’t let even a single rat get near.”

The old man bowed politely and left the room. His presence quickly faded into the distance.

Tang Sadok caught the meaning in Jeok Cheongang’s eyes and spoke first.

“He’s a household retainer who’s absolutely loyal to me. He’s handled messenger pigeons here for more than half his life, so I had him check them in case.”

The place Tang Sadok called “here” looked less like a pavilion and more like a huge aviary.

Even standing still, the sharp, musty smell of birds stung my nose. Iron cages of all sizes filled the space, and feathers of every color fluttered through the air.

It was clear that this place had been used for years solely to train messenger pigeons and send and receive their messages. Dozens of unopened missives were piled up inside.

“There are more than I expected. A lot more than the number of pigeons we saw before coming here.”

Tang Sadok gave a small nod at my words.

“I’m surprised, too. Usually, they send only the bare minimum of information to keep the messenger pigeons from attracting attention. But sending several pages on each one means…”

“They had a lot of information they needed to get through, even if they had to send it this way.”

Jeok Cheongang spoke up, then added in a low voice,

“And that means it was urgent.”

I opened the first missive and read it. I realized the words I’d just heard weren’t exaggerated in the slightest.

“What does it say?”

I was silent for a moment before answering Jeok Cheongang’s question.

“After Anhui, people suspected of being members of the Embroidered Uniform Guard appeared in Hubei.”

“Hubei? When did the information come in?”

“About twenty days ago.”

“Twenty days. Damn, that’s late.”

“By then, their trail in Anhui had already gone cold, and it seems neither the Beggars’ Sect nor the Lower District Sect in Hubei guessed they were the Embroidered Uniform Guard.”

Tang Sadok frowned.

“Isn’t it possible they weren’t the Embroidered Uniform Guard at all? If your guess is right and their target is Prince Shangshan, they’d have no reason to detour through Hubei to reach Shanxi. They could’ve gone straight from Anhui to Henan.”

He was right. Anhui was closest to Henan, and they could enter Shanxi by heading just a little farther north.

But Tang Sadok had clearly forgotten one important thing.

“If they are the Embroidered Uniform Guard, and they went so far as to disguise themselves to hide their identities from the start, then of course they’d avoid Henan.”

“What does that mean…? Ah.”

Tang Sadok let out a small exclamation and uttered a single word.

“The Murim Alliance.”

“Exactly. They nearly had their trail picked up even in Anhui. Henan is practically an impregnable fortress right now.”

The vast storm of war was reaching its peak, and the full-scale war with Dark Heaven had begun.

With everyone in the Central Plains Murim on high alert, crossing Henan—the home of the Murim Alliance’s headquarters—to reach Shanxi would be no different from giving away their identities.

The Murim Alliance wasn’t a fool.

Whether they were Dark Heaven’s agents or the Embroidered Uniform Guard, anyone suspicious would be identified in no time.

Even if the Sword Saint, Mae Jonghak, leader of the Murim Alliance, merely stood by with a gentle smile and watched, one old fox beside him would be different.

*Song Ho, the Thousand-Faced Fox.*

He had another title: Chief of the Hidden Shadow Pavilion.

At that very moment, as I pictured the Thousand-Faced Fox’s face, always marked by a faint smile—

Rustle.

A faint sound came from the crack beneath the firmly shut door. But no one in the room, myself included, was surprised or flustered.

We already had a fair idea who was approaching—and who it was.

Creeeak.

At Jeok Cheongang’s glance, I reached out. A gentle current of energy pushed the door open, revealing someone.

No—more accurately, it revealed two people who looked like one.

The Tang Family retainer who had left earlier had Namho pinned in an embrace from behind, a blade pressed to his Adam’s apple.

“……?”

“……?”

“……?”

What the hell was going on?

My brain stalled for a moment, but I quickly figured it out.

The Tang Family retainer who was supposedly so devoted to Tang Sadok that he’d do anything for him had been guarding the place to make sure not even a rat got in. Then he’d found Namho.

The minor problem was that Namho had almost died.

“You’re still young at heart. It’s not easy to get fired up at your age.”

Namho, restrained with the retainer pressed up against his back, replied with a face like he’d bitten into a turd.

“What does that mean?”

“Nothing. Anyway, stay still. Your Adam’s apple moves when you talk, and you’ll cut yourself on the blade.”

“Don’t push it with the threats—”

Slice.

“Shit, you’re right.”

“I told you not to talk.”

“So I’m using ventriloquism now.”

“Oh, ventriloquism. Teach me sometime.”

“Maybe, if I get the chance… Damn it. Cut the crap and get this man to stand down. He won’t listen no matter how much I explain.”

Jeok Cheongang stroked his chin, looking amused at Namho’s predicament.

“You were right about him being loyal. If he were just a little more reliable, he’d have killed an innocent man.”

“……Sometimes his loyalty goes too far. Let him go. He’s one of ours.”

At Tang Sadok’s sighing words, the retainer blinked, finally withdrew his dagger, and stepped back.

Namho watched him leave without so much as an apology and muttered,

“I’ve seen all kinds of lunatics, but this is something else. No wonder the Sichuan Tang Clan is—”

“Is what?”

When Namho met Tang Sadok’s meaningful gaze, he changed course at the speed of light.

“No wonder it’s called one of the Five Great Families under Heaven.”

That was an impressive drift. Still, even if you’d lived a long life, there was no reason to spend whatever you had left worrying about being poisoned.

“Anyway, why did you take so long? It’s been ages since I sent for you.”

“I was thinking back over something. Maybe it’s because I’m getting old, but my memory isn’t what it used to be.”

“Your memory?”

“Yes. My memory.”

Before I could even ask what he meant, Namho nodded toward the missive in my hand.

“That information you’re looking at—where did it come from?”

“The Hubei branches of the Beggars’ Sect and the Lower District Sect.”

“No. What about the one beside it?”

I opened another of the dozens of missives scattered across the table and checked it.

“It says Hoyeon Trading Company. I’ve never heard of it before. The contents say…”

“It’s a trading company under the Qingcheng Sect. More precisely, Hoyeon Sword, a lay disciple of the Qingcheng Sect, has been running it for twenty years. He’s a Peak master, but he’s much better at running a trading company than at martial arts. Hoyeon Trading Company is one of the five largest in Shandong.”

“What?”

“Oh, and there’s no need to tell me what it says. I’m looking for a different name. Just check where each message came from and let me know.”

“……”

I didn’t know what to ask first.

As far as I knew, he hadn’t set foot in the Central Plains since the Great Faction War. How could he know so much about news from twenty years ago?

Or what was the source he wanted me to look for, if he didn’t care about the contents?

Jeok Cheongang and Tang Sadok stared at him with wide eyes. I could only look at him, dumbfounded and silent. Namho clicked his tongue, displeased.

“I’m no Jiang Taigong. Did you think I spent all those years in Nanman just sitting around fishing? I kept up with news from the Central Plains through the Hidden Shadow Pavilion’s Hidden Thread while I was there. There’s nothing to be so surprised about.”

“This seems like more than just keeping up with the news. Even if I heard some of that, I wouldn’t remember it.”

“Call it an old man’s pastime. Anything else you want to say?”

It was probably more like an occupational habit than a pastime, but personal curiosities like that weren’t important right now.

I kept quiet and hurriedly began opening and reading the remaining missives.

They’d all been sent through the Sichuan Branch, but each had a different source. And since I had to read their contents to find what Namho was looking for, I naturally began sorting the information out in my head.

The result was shocking.

*It wasn’t just Anhui and Hubei.*

Anhui, Hubei, Hunan, Jiangsu, Shandong.

If the contents of each missive were true, people suspected of being members of the Embroidered Uniform Guard had appeared in all five provinces, then vanished without a trace.

*This is…*

A dispersed movement.

More likely a mobile strategy to avoid being noticed than a diversion.

They had split into groups of as few as ten and as many as thirty, spread out across the provinces, and then vanished upon reaching Shaanxi or Shandong.

*Shanxi. They gathered in Shanxi.*

There was no doubt. Avoiding Henan and drawing as little attention as possible, they’d gone around it, slipping into Shanxi through Shaanxi and Shandong—the provinces that lay along the continent’s flank.

And there…

*Prince Shangshan Zhu Bao.*

My heart sank. The next moment, I mechanically grabbed another missive. As soon as I read it, my teeth clenched without my realizing.

Crack.

“What is it?”

“What does it say?”

I didn’t answer. I unfolded the missive and held it out. Tiny letters had been written on the yellowed animal hide.

> 1. Sender: Shanxi Branch of the Lower District Sect.
>
> 2. Prince Shangshan Zhu Bao. Accompanied by the Embroidered Uniform Guard.
>
> 3. Hong Jin, Shanxi Province’s Second-Rank Deputy Military Commissioner. Requested support from the Lower District Sect and joined up with Prince Shangshan.
>
> 4. Tracking began. Concern that the authorities may intervene.
>
> 5. Operation suspended after the tracking team was wiped out.
>
> 6. This document is Grade Heaven. Deliver the information to the designated recipient as quickly as possible.
>
> 7. Blazing Flame Divine Dragon Jin Taekyung. Urgent search requested.

One missive that turned suspicion into certainty.

Tang Sadok and Jeok Cheongang read its contents and let out quiet exclamations.

“……This is…”

“This was already five days ago. Judging by the distance, the Sichuan Branch must have received the information and passed it on only today.”

That was probably right. If the missive had reached the Sichuan Tang Clan before we gathered here, I would’ve known about it already.

But we were a step too late. Prince Shangshan had already fallen into the Embroidered Uniform Guard’s hands, and behind the Guard stood the Son of Heaven. Or Dark Heaven.

*No—maybe Dark Heaven is controlling the Son of Heaven.*

It might have been an overreaching assumption, but the existence of the Blood Soul Gu alone gave me reason to suspect it.

Baeksang, the Great Chieftain of the Bai people and the second-in-command of the Nanman Beast Palace, had been the same.

And if that suspicion was true…

*We’re finished. What happened in Nanman won’t even come close.*

The Nanman Beast Palace was a sect and a small kingdom.

But the Great Nation was a great nation in the truest sense.

The size of the bomb—and the extent of the damage when it exploded—would be on another level entirely.

Just thinking about it sent a chill down my spine.

It was enough to make me start walking before I even knew where Prince Shangshan was.

Thud.

“Where are you in such a hurry to go?”

The voice didn’t belong to Jeok Cheongang or Tang Sadok.

I slowly turned around. Namho was calmly reading a missive, without even looking my way.

“We have to go. We need to protect Prince Shangshan.”

“Fine. But where are you planning to go? East, where the imperial capital is? Or north, where Shanxi is? Surely not south or west.”

Even in the midst of my confusion, I did my best to speak calmly.

“I’m thinking we should head northeast first. We’ll use the Beggars’ Sect and the Lower District Sect to track them down.”

“Wrong.”

“What? What do you mean…?”

I was baffled by his utterly firm tone. Namho said nothing, only holding out the missive in his hand.

> 1. Sender: Nakjo Escort Bureau.
>
> 2. Prince Shangshan and fifty members of the Embroidered Uniform Guard. Departed Shanxi Province.
>
> 3. Expected to head for Zhejiang through Shandong and Jiangsu.
>
> 4. At their current speed, they’ll enter Jiangsu Province on the first day of next month.
>
> 5. Escort order issued. The person to be escorted is Prince Shangshan Zhu Bao. Participants: Fire King Jeok Cheongang, Blazing Flame Divine Dragon Jin Taekyung, and every member of the Fire Dragon Pavilion.

The moment I saw the four characters *escort order issued* on the last line, I instinctively realized where the missive had come from.

There was only one place in the world that could issue orders to me—or rather, to Jeok Cheongang.

“The Murim Alliance…!”

“More precisely, the Hidden Shadow Pavilion. Though it must have had the Alliance Leader’s approval, of course.”

“The Nakjo Escort Bureau? What is this? I already checked every missive, so where did this even—”

My voice trailed off. I turned toward the scent of blood creeping into my nostrils.

When had that happened? One of the messenger pigeons in a cage had been disemboweled and lay dead.

“It’s a method the Hidden Shadow Pavilion often uses. It’s rough on the poor pigeon, but hiding the message inside its belly makes it safer for us.”

As everyone stared at him, speechless, Namho gave a calm smile and continued.

“Do we still have time to hesitate? There are fewer than fifteen days until the first of the month. If we leave now, we should be able to catch Prince Shangshan in Jiangsu at the very least.”

He was right. We didn’t have time to hesitate any longer.

I shot into the darkness.

We had a little over fifteen days left. We had to hurry, even if it was only by a single hour.
## Chapter artifact 854

# Chapter 854

Jang Il, a junior military officer in Hubei Province, was a man who knew how to be satisfied with his life.

Some people who knew him would click their tongues and say he had no ambition, despite being born a man. But Jang Il himself was proud of who he was.

*I’ve done enough. Damn right I have.*

He’d been born into a commoner family that had next to nothing, yet he’d risen to the rank of an official military officer.

His low rank meant the government paid him a pittance, but the important thing was that he was one of the seven gate commanders in Yichang, a major city in western Hubei Province.

What kind of place was Yichang?

A port city on the banks of the Yangtze, which ran across Hubei Province, it drew a steady stream of poets and scholars eager to take in its splendid scenery.

That meant countless people and goods passed through every day, and naturally, each gate collected a hefty toll.

And, of course, there were the little extras called bribes that were never reported to the higher-ups.

*I wonder what big shots will come through today.*

Jang Il had risen early, eager to get ready for work.

He wore a silk robe that gleamed with a rich sheen and carried a finely decorated sword.

It stung a little that he couldn’t see how he looked in a mirror, since they were far too expensive for him to buy. But his elderly servant’s words offered some comfort.

“You truly have the bearing of a hero, my lord.”

“Ahem. You think so, too?”

“Yes, my lord. Whoever passes through the gate, none of them will dare raise their heads properly in the face of your authority.”

“Now, now. What a silly thing to say.”

Despite his words, Jang Il’s lips twitched upward. The elderly servant laughed easily and waved a hand.

“Oh, when have you ever known me to flatter you? But seeing you wear your finest silk robe and carry your sword today, you must have something important going on.”

“You’re always quick to catch on. You’re right. Some real big shots might be coming through today. A trading caravan that left for Chongqing about two months ago is supposed to return around now.”

“Goodness. But haven’t things been getting strange around Chongqing lately?”

“Who told you that?”

“I heard it from a traveling merchant I know. There’s been a bloodbath among martial artists not just around Chongqing, but in Guangxi as well…”

“It’s all nonsense, so ignore it. I’ve heard a little about Guangxi myself, but Chongqing only has a few disorganized bandits and river pirates. This caravan is bound to bring in a fortune.”

Jang Il straightened his clothes, smiling with satisfaction.

Chongqing lay between Sichuan Province and Hubei Province. It wasn’t quite a province, but it had abundant resources and local specialties that made countless trading companies eager to do business there.

The profits were huge, so competition was fierce, and the trading companies that won out were massive.

*This caravan especially so.*

Three trading companies had joined forces.

The number of guards and caravan porters they’d brought along was a staggering five hundred.

They’d loaded more than a hundred carts onto ten merchant ships and set out about two months ago. Jang Il couldn’t help looking forward to the little extras that would soon come his way.

*How could I not get something out of it, after everything it took to get this job?*

The old saying “you reap what you sow” meant something entirely different to Jang Il.

He’d scattered a fortune in bribes to become a gate commander in Yichang, and in less than two years, he’d collected far more than he’d spent. But he had no intention of being satisfied now.

*As long as I keep collecting like I am now, that’s plenty. No need to get greedy. Just enough to buy a decent estate.*

One greed was soon forgotten in pursuit of another.

Jang Il prided himself on being a conscientious official—corrupt just enough, and lazy just enough—and left home.

The moment he arrived at his post at the West Gate, he realized something was wrong.

*What is this?*

The air was taut.

The soldiers, who would usually be yawning with their arms folded, were drenched in sweat as they ran in every direction. Bloodied stretchers and charred scraps of debris lay scattered all around.

The three flags that had flown proudly when the caravan left for Chongqing two months ago were among them.

“What on earth is…”

“My lord! Officer Jang!”

At the sudden call that pierced his ears, Jang Il snapped out of his daze.

A familiar subordinate was standing in front of him, pale as a sheet.

“What—what happened here?”

“Th-that is…”

“Why don’t you tell me the truth at once!”

The subordinate flinched at his superior’s sharp shout, then stammered out an answer.

As Jang Il listened to his rambling story, his mouth fell open.

“A-an attack?”

“Yes, yes. They say the caravan was attacked by bandits on its way back.”

“That’s impossible! There were five hundred guards and caravan porters! What bandit would be crazy enough to try that?”

Just as he let out his horrified shout—

“The world’s gone mad. Why should bandits be any different?”

A weary voice cut in. Jang Il turned to look and blinked.

“M-Master of the Trading Company?”

There was no mistaking him. Even with his body drenched in blood and his clothes reduced to rags, Jang Il recognized him at once.

He was one of the three trading company masters on the caravan—the big shot Jang Il had been eagerly awaiting for the past two months.

“Glad I survived to see you again, Officer Jang.”

“W-what on earth happened? What about the other two?”

“They came with us. But we’ll never have the chance to speak again.”

Jang Il looked where the trading company master pointed and felt the world go dark.

Several dozen bodies lay wrapped in straw mats. The identities of the two corpses set apart from the rest were obvious.

“……Surely not.”

“Just what you think. They fought bravely to the very end, but there was nothing we could do. We were simply outnumbered.”

“Outnumbered? There were that many bandits?”

“Strictly speaking, they were bandits and river pirates. Even while reeling from the unexpected ambush, I could tell who they were. Harpoon-wielding men were swarming everywhere.”

“R-river pirates? How could they be here?”

“Whether they’re in the mountains or on the Yangtze, thieves make their living by thieving, don’t they?”

The trading company master muttered wearily and leaned against a shattered cart.

“Everything went smoothly when we left Yichang two months ago. But the moment we reached Chongqing, I had a feeling something was going wrong. Sure enough, no sooner had we set foot on Yuhua Mountain than they appeared.”

Despite its beautiful scenery, Yuhua Mountain was known as one of Chongqing’s rugged mountains.

The trading company master remembered the first moment they’d encountered their enemies, in a patch of brush hemmed in by narrow, blocked-off paths. He shuddered without realizing it.

“We had nothing to worry about. Each trading company had brought only its best men, and we’d hired dozens of famous wandering martial artists in case of trouble. But the moment they showed themselves, I realized none of that mattered.”

“How many of them were there?”

“A thousand.”

“Pardon?”

“I said a thousand. That’s how many I estimated at a glance, so there must have been even more.”

“……!”

For a moment, Jang Il thought he’d misheard.

A band of more than a thousand bandits? In the north, nomads or mounted bandits based on the grasslands sometimes joined forces and invaded with a large army. But not in Chongqing.

It was an unprecedented thing, something that should never have happened.



*“But haven’t things been getting strange around Chongqing lately?”*

*“Who told you that?”*

*“I heard it from a traveling merchant I know. There’s been a bloodbath among martial artists not just around Chongqing, but in Guangxi as well…”*



Remembering his conversation with the elderly servant before he left home, Jang Il felt his heart sink.

His cherished silk robe was already damp with cold sweat, though he couldn’t remember when he’d started sweating.

*No way.*

Chongqing was right next to Hubei. From Yichang, where he served as a gate commander, it was three days by boat or five days by land.

*If—if all of this is true…*

His hands and feet trembled, and his breathing grew shallow.

He should’ve been on his feet, directing the soldiers and sounding the alarm, but his body wouldn’t move.

Whether he knew what was happening to Jang Il or not, the trading company master continued.

“We said we’d pay the toll, but their answer was a volley of arrows.”

Someone’s death set off a fierce battle.

The fighters trained by the trading companies and the hired wandering martial artists fought back. Even the caravan porters who had been hauling the carts joined in. But the river pirates and bandits, who’d spent their whole lives as raiders, cut them down without hesitation.

“It was less a battle than a slaughter. We had plenty of men, but half of them were caravan porters. The rest could only do so much.”

“B-but how could that happen? Most of those men must’ve been farmers or fishermen, too, right?”

“Right, they probably were. But there was something different about them. They kept charging at us like they were possessed.”

The trading company master’s voice, which had been as calm as he could make it, suddenly quivered.

“Even with their legs slashed and their arms torn off, they kept coming. Knock one down, and three more came. Knock three down, and five more appeared. And if we held back our rising fear and took them down, ten more enemies were waiting. Over and over, again and again…”

The trading company master still remembered it clearly.

No—he would never forget it, not until his last breath.

The way they charged like fiends bursting out of a hellscape.

“The battle ended decisively in just half a shichen—roughly an hour—and our side broke. Men started running in every direction. Surrounded by screams and death, I led my subordinates away, too. The caravan had failed, but we had to get out alive somehow.”

There was nothing more precious than one’s life.

He’d fled with the other two trading company masters and the troops still standing. When they emerged from Yuhua Mountain, they found that their number had been cut in half from the five hundred they’d started with.

“We kept running along the mountain foothills. For three whole days.”

“Th-three days?”

“We wanted to go down to the foot of the mountain and ask the imperial troops or another Murim sect for help, but with those men around, that was nearly impossible. It was our only choice.”

The enemy had been watching the main routes closely. The survivors, barely clinging to life, had made a break for Hubei along the shortest route and finally escaped Chongqing.

Or so they’d thought.

That was before they saw the ten merchant ships they’d left at the nearest dock, all burning.

“I was sure it was over. I couldn’t even bring myself to consider running any farther.”

The chase had gone on for three whole days. It had been brutal and fierce.

From five hundred, their number had been cut in half. From that half, it had fallen to fewer than a hundred. They began to think of death.

They watched the merchant ships—their last hope—sink beneath the dark red flames.

They heard the enemies shouting behind them.

And just as their final battle was about to begin, people no one could have expected appeared.

“There was a middle-aged man. He was with a group of about ten.”

“A middle-aged man…?”

“Yes. He walked toward us as if out for a stroll, pointed at the burning ships, and asked us this out of the blue.”

The trading company master steadied his breathing and continued.

“Which son of a bitch set those on fire?”

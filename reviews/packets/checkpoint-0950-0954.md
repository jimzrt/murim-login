# Checkpoint Review — 950–954

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

# Chapters 950–954

## Plot

With Shanxi facing an advancing steppe army of an estimated thirty to forty thousand, the Jin Family rescinds its retreat and prepares to defend Eight Spring Gorge. Reinforcements arrive from the Hebei Peng Family, Murong Family, Huashan, and Zhongnan Sect; the Murim Alliance also sends two thousand martial artists north. Mae Jonghak persuades Song Ho that the defenders are fighting to protect the people, not merely their homes.

The invading army is led by Jamukha and includes Temur and a man impersonating Chinggen—the real Chinggen was killed in an earlier attack. Jin Mukyung, newly returned from more than two years of secluded training, becomes Commander of the Heaven Shaking Squad. His two-hundred-strong force annihilates a thousand-man vanguard, including a hundred Keshik, suffering twenty-three deaths and thirty-seven wounded.

Jin Wikyung prepares Shanxi’s defenses with scorched fields, poisoned water, traps, and five earthen forts at Eight Spring Gorge. Thousands of commoners join the effort, many in gratitude for the Jin Family’s past aid during famine. When the steppe army reaches the gorge, Jamukha leads its charge. Temur privately recognizes the impostor as Chinggen’s killer but hides that knowledge. Jin Wikyung promises the defenders they will celebrate the next Double Ninth Festival together on Mount Heng. The battle begins, with its outcome unresolved.

## Continuity

- The battle at Eight Spring Gorge has begun. Jin Wikyung leads the defense; Jin Mukyung commands the Heaven Shaking Squad. The steppe army, led by Jamukha, is charging the gorge.
- Jin Mukyung’s squad destroyed a thousand-man vanguard, including one hundred Keshik; it lost twenty-three fighters, with thirty-seven wounded.
- The Jin forces devastated northern Shanxi’s fields and water sources, set traps, and prepared five earthen forts at Eight Spring Gorge. Thousands of commoners are helping defend the region.
- Jin Wikyung promised the defenders they would celebrate the next Double Ninth Festival together on Mount Heng.
- The real Chinggen was killed. An impostor wearing his face accompanies Jamukha; Temur knows the impostor’s identity and conceals his knowledge. Jamukha has long awaited a call from “that person,” whose identity and purpose remain unknown.
- The Emperor remains gravely ill from Blood Soul Gu. The Divine Physician says saving him requires him to die once; Taekyung’s effort to remove the Gu and treat him remains unresolved.
- Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung. The improved Temporary Strength Pill’s source, effects, and distribution remain unknown.
- The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown. The Eastern Heaven Demon Lord’s papers and silk pouch also remain unexplained.

## Translation Decisions

- Render 협 as “chivalry” in Mae Jonghak and Song Ho’s exchange.
- Render 진천대 as “Heaven Shaking Squad” and 진천대주 as “Commander of the Heaven Shaking Squad.”
- Render 토성 as “earthen fort” and 철질려 as “iron caltrops.”
- Render 안다의 맹세 as “the anda oath,” a sworn-brother bond.
- Render 한 고조 as “Emperor Gaozu of Han,” 항우 as “Xiang Yu,” 유방 as “Liu Bang,” and 장량 as “Zhang Liang.”

## Durable state

{
  "active_continuity": [
    "The steppe army has begun its assault on Eight Spring Gorge after the Jin forces devastated northern Shanxi’s fields, water sources, and homes and laid traps; the defenders’ battle remains unresolved.",
    "Jin Wikyung has promised his defenders they will celebrate the next Double Ninth Festival together on Mount Heng.",
    "Temur regrets ignoring the real Chinggen’s warnings and knows the man beside him is Chinggen’s killer and impostor, but conceals his knowledge.",
    "Jamukha leads the steppe army and has long awaited a call from “that person”; that person’s identity and purpose remain unknown.",
    "The Emperor remains gravely ill from Blood Soul Gu; the Divine Physician says saving him requires him to die once, and Taekyung’s quest to remove the Gu and treat him remains unresolved.",
    "Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung; the improved Temporary Strength Pill’s source, effects, and distribution remain unknown.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.",
    "The real Chinggen was killed; an impostor wearing his face continues to accompany Jamukha."
  ],
  "continuity_sources": [
    953,
    954
  ],
  "open_questions": [
    "How will the battle at Eight Spring Gorge fare?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain?",
    "What will the Chinggen impostor do, and what is their purpose?"
  ],
  "safe_through": 954,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 950

# Chapter 950

For everyone, that summer was unusually short and chaotic.

The strangely capricious weather was only one of many reasons.

Floods no longer even counted as surprising.

One midsummer day, hail poured down in place of the monsoon rains. Once, after the worst heat wave in recorded history, a blanket of white frost settled over the land.

Those whose crops were ruined overnight collapsed and wept. With grain prices soaring, they were left wondering where their next meal would come from.

The government released famine relief rice, but by the time a sack of it had passed through a few hands, it had dwindled to a single cup.

In the end, those who could no longer endure their hunger headed for the mountains.

There they stripped bark from trees to eat, or took up rusted farm tools and became bandits.

But even that wouldn’t last long.

What could people who had spent their whole lives dutifully working the fields possibly do? All that awaited these clumsy bandits was death.

Whether by government troops or martial artists, they would eventually be hunted down. And only when cold blades cut through their bodies would a question suddenly occur to them:

*How had I ended up like this?*

But no one knew the answer.

Events unfolding across this vast land were often so difficult that no one could understand them.

Especially when one looked back on the past two years.

“Have you heard? Just a couple of months ago, in Nanman…”

“That’s not all. Guangxi has run red with blood.”

“This is driving me mad. What’s become of the world?”

Stories were always circulating wherever people gathered.

But compared to a few years ago, the atmosphere was different. No—the very air felt different.

The voices of the people filling the inn had sunk low as morning fog, and their eyes and faces were full of worry they could not hide.

Rumors about the Murim, once no more than something to accompany a drink or pass the time, had become blades of reality, slowly cutting into their skin.

They could no longer laugh and sing.

They watched the government troops patrolling the streets in groups of dozens and the occasional martial artist who passed by with anxious eyes, hurrying home before nightfall.

By now, everyone knew it instinctively.

A new war had already begun.

A catastrophe beyond comparison to the hundred thousand Demonic Cultists who had trampled the Central Plains several decades ago was looming over their heads.

And those who belonged to the world of the Murim felt the present reality more clearly than anyone.

“I hear they’ve reached as far as the Imperial Court. And they’ve been at it for decades, since around the time of the Great Faction War.”

“I heard as much through the Beggars’ Sect.”

“Dark Heaven is stronger than we imagined. Thank goodness their plan fell through. If it had succeeded…”

It was no longer unusual for dozens of martial artists to gather—especially Sect Leaders and Family Heads who led their own organizations.

In grave voices, they discussed the current situation and tried to predict what would come next.

And one name came up every time.

“The Blazing Flame Divine Dragon made another remarkable contribution. I hear this incident earned him the Imperial Court’s full support and the Son of Heaven’s favor.”

“Then is that rumor true?”

“What rumor?”

“You haven’t heard yet, it seems. A few days ago, when the Blazing Flame Divine Dragon left the Imperial Capital, the Son of Heaven himself came out to see him off and made him a marquis.”

“What? The Son of Heaven gave a martial artist an official title—and made him a marquis, no less? Is that even possible?”

“There were plenty of witnesses. Since it happened in the Imperial Capital, it took the Lower District Sect and the Beggars’ Sect a little while to get the information, but it seems to be true.”

News travels a thousand li without feet.

The Imperial Court’s proclamation declaring war on Dark Heaven as a foreign enemy, along with Jin Taekyung’s achievements and the unprecedented honors he had received as he was raised to the rank of marquis, spread from mouth to mouth in no time.

Now even the Imperial Court had stepped in.

The Great Nation, which had sat back and watched even during the Great Faction War, possessed more troops and supplies than anyone could count. If it joined the fight, Dark Heaven would be little more than a candle in the wind.

Or rather, that was what everyone expected.

Except for the handful of people who knew the full situation.

Flap, flap!

Watching the messenger eagle disappear into the distance with a harsh beat of its wings, the old man unfolded the tiny scrap of paper in his hand.

As his eyes passed over the minuscule writing, the sword scar on his face twisted ever so slightly.

“So that’s how it is.”

The quiet mutter slipped between his dry lips.

After standing still for a while, deep in thought, the old man tossed the paper into a brazier set in one corner of the room.

He watched until the oil-soaked missive, prepared to keep it from getting wet, had burned away in an instant. Then he set off for his destination.

Thud. Tap.

A dull sound rang out with each limping step.

Whenever the old man passed, those who looked like Confucian scholars lowered their heads slightly.

“Welcome, Chief of the Hidden Shadow Pavilion.”

“I have a brief report concerning what happened in Guangxi.”

“We’ve received an urgent message from the Nangong Family.”

“And from Hebei, Liaoning, and Shaanxi…”

Some passed with their arms full of bamboo slips; others offered only a brief greeting before leaving. But most of them gave the old man new information, and each time, he organized and refined his thoughts.

At last, he stopped in front of a firmly shut door.

Click.

The door opened as if it had been waiting for him.

But the old man wasn’t surprised.

Just as he knew the details of events taking place thousands, even tens of thousands, of li away, so did the master of this room.

Though they were alike in one way, the truth was on an entirely different level.

The old man had countless eyes and ears. His counterpart, however, could sense everything happening within a radius of more than three hundred yards by his own power alone.

“Were you practicing martial arts?”

At the old man’s first words as he entered the exceedingly plain room, the man sitting cross-legged opened his eyes.

“I was. Until just now.”

“I’m sorry. It seems I interrupted you without meaning to.”

“Don’t give it another thought. I’m sure you had a good reason.”

The man smiled gently. He was young.

His face looked barely thirty, and his bare upper body was covered in tightly packed muscles, perfectly balanced.

Of course, once he put his clothes on, he looked like any ordinary young man.

“So, what is it?”

The man continued to address the old man with the easy familiarity of a senior.

But he had more than enough standing and experience to do so.

Sword Saint Mae Jonghak was one of the greatest pillars supporting the Murim world.

“I’ve come because there’s something I must report to the Alliance Leader immediately.”

“Something you must report immediately.”

The smile on Mae Jonghak’s lips disappeared. He took his seat and tilted a teapot, continuing as he poured the tea.

“Is the report about Shanxi?”

Trickle.

Before the cold tea had even filled the cup, steam rose from it. The old man sat down across from Mae Jonghak and ran a hand over the teacup, heated by Samadhi True Fire.

“Yes.”

The cup was warm. But the news that followed would be cold and dark.

Mae Jonghak read as much from the old man’s expression.

“Speak, Chief of the Hidden Shadow Pavilion.”

The old man, Song Ho, the Thousand-Faced Fox, answered.

“The Jin Family of Taiyuan has rescinded its retreat.”

“Tell me more.”

“All of Shanxi Murim is mobilizing. More than thirty sects and families have gathered around the Jin Family of Taiyuan, and the Shanxi Provincial Office is also mobilizing every available troop.”

“Hmm.”

Mae Jonghak let out a low hum.

There was no need to hear more.

This was an all-out war in the truest sense. It would be a battle for the fate of all Shanxi Province, not just Shanxi Murim.

“What forces does Shanxi have?”

“First, more than five thousand martial artists are standing by, led by the Jin Family of Taiyuan. In addition, the government has ten thousand troops, including a thousand cavalry.”

Fifteen thousand in all.

They had scraped together every last man.

They wouldn’t even have managed to gather five thousand martial artists if the Jin Family of Taiyuan hadn’t accomplished an extraordinary resurgence over the past two years.

But the biggest problem was…

“Less than half the enemy’s numbers.”

At Mae Jonghak’s mutter, the Thousand-Faced Fox gave a solemn nod.

According to the Hidden Shadow Pavilion’s intelligence, the grassland army marching south would number at least thirty thousand, and as many as forty thousand.

Because it bordered the grasslands, The government troops stationed in Shanxi Province were highly capable. But the wave of cavalry, more than twice their total strength, was a nightmare in itself.

“The plan seems to be to clear out the north first, then fight in the central region to minimize casualties.”

“The central region would mean Taiyuan, their stronghold?”

“More precisely, they seem set to make their stand at Jeongyang, about three hundred li from Taiyuan.”

“Jeongyang. Jeongyang…”

Mae Jonghak murmured the name, then suddenly realized why it sounded so familiar.

“That place. Eight Spring Gorge.”

“Yes. That’s right.”

The Thousand-Faced Fox continued in a calm voice.

“Eight Spring Gorge is almost a fortress created by nature. During the Great Faction War, it was where the Demonic Cult’s great army was successfully repelled. And two years ago, it played a decisive role in the Jin Family of Taiyuan’s victory.”

Eight Spring Gorge, situated on the boundary between central and northern Shanxi Province, was a gorge shaped like a jar.

Its paths were steep and its entrance narrow, making it the perfect battlefield for a small force to fight a larger one.

And considering that most of the enemy forces were cavalry, it would be hard to find a better location.

The problem was that the cavalry numbered tens of thousands—and the true enemy still hadn’t revealed its full nature.

“If the decisive battle is fought at Eight Spring Gorge, what do you think are the Jin Family of Taiyuan’s chances of winning?”

“Even at the most generous estimate, twenty percent. No matter how much the battle turns in the Jin Family of Taiyuan’s favor, anything higher than that would be difficult.”

The Thousand-Faced Fox answered firmly, his eyes darkening.

“If the enemy forces consisted only of nomads, their chances would be over fifty percent. But…”

“Right. We can’t forget them.”

Dark Heaven.

The pitch-black clouds had already swallowed the blue skies over the grasslands. Their very presence had bound everyone’s feet like a trap.

“Right now, we can’t expect to send support to the Jin Family of Taiyuan.”

The Thousand-Faced Fox’s face was dark as he said it.

As the Murim Alliance Leader’s right hand and the head of the Hidden Shadow Pavilion, he was one of the people who understood the current state of the world better than anyone.

“Everyone already knows that if we act rashly, we could be caught in their dark arts and suffer a grave disaster.”

It was difficult to understand by any reasonable measure, but Dark Heaven had already used the dark art known as the Moving Formation several times.

As a result, Shaolin—the Mount Tai and Northern Dipper of the Murim—had suffered devastating losses. The Nine Sects and One Gang and the Five Great Families would be no exception.

Not even here in Henan, where the Murim Alliance’s headquarters was located.

“Then the forces we can mobilize right now…”

“None.”

“None?”

Mae Jonghak gazed steadily at the Thousand-Faced Fox, who had answered as if there were no room for reconsideration.

“I want to ask you one thing. Please answer carefully.”

“Go ahead.”

“Is it absolutely true that we have no troops to send to Shanxi?”

“…”

The Thousand-Faced Fox chose silence instead of answering.

He had lived a life worthy of his epithet.

Concealing his identity and spinning blatant lies as if they were the truth came as naturally to him as breathing.

But even the Thousand-Faced Fox could not bring himself to lie beneath the clear gaze of the man in front of him, Sword Saint Mae Jonghak.

“You know as well, Alliance Leader…”

The Thousand-Faced Fox finally parted his heavy lips.

“The balance of power has already tipped too far. Helping Shanxi now would be the worst choice. The right thing to do is order the Jin Family of Taiyuan to retreat at once.”

“I think it’s too late.”

“It isn’t. Even if time is short, if we pull the front line back to Henan without delay, we can preserve our remaining forces and plan for what comes next.”

“No. It’s definitely too late.”

Mae Jonghak gave a slight shake of his head, then added,

“To change their minds.”

“…”

“The Lesser Family Head of the Jin Family of Taiyuan is an astute man. He always sees the full picture and is exceedingly cautious before making a decision. Isn’t that why you recommended him to the Murim Alliance’s Strategist Corps?”

The Thousand-Faced Fox let out a quiet hum before he could stop himself.

If such a cautious man had made a decision that put his family’s fate on the line, it meant he could never take it back.

Not even if it was the Murim Alliance Leader’s order.

“But if this continues, we could lose Shanxi—all of them.”

“I know. If they retreat now, the innocent commoners who haven’t managed to flee will be massacred by the enemy.”

“…”

“Don’t turn your eyes away. They aren’t fighting only to protect the homes where they grew up.”

For a moment, the Thousand-Faced Fox was at a loss for words. Unable to meet Mae Jonghak’s gaze, he closed his eyes.

That was right.

He knew. He had only pretended not to.

This wasn’t a battle. It was a war.

To win it, a few thousand martial artists mattered more than a hundred thousand people.

“Was my judgment… wrong?”

“No. It was excellent. You’re a better strategist than anyone I know.”

At the unexpected answer, the Thousand-Faced Fox opened his eyes.

Mae Jonghak was looking at him with a gentle smile.

“You simply forgot one thing.”

“What was it?”

“You were so busy looking at the whole forest that you failed to see the small branch within it.”

It happened at that very moment.

Srrk.

With a motion of Mae Jonghak’s hand, a surge of qi reached out and flung open the firmly shut door.

Then, with the faint stir of a hidden presence, a figure swept in like the wind.

“What news have you brought?”

At Mae Jonghak’s question, as if he had been expecting the arrival, a messenger from the Alliance Leader’s Office bowed low and answered.

“Urgent news! The Hebei Peng Family, the Murong Family, Huashan, and the Zhongnan Sect are each sending two thousand reinforcements to save Shanxi Province…”

The Thousand-Faced Fox froze and couldn’t hear the rest.

To send such a large force as reinforcements when their own strongholds might be in danger?

That went against every military strategy he’d learned and every bit of common sense everyone knew.

But…

*So that’s what it was.*

The Thousand-Faced Fox smiled bitterly.

Only after the messenger, bearing news he could hardly believe, had left did he break the long silence.

“I understand now. I know the name of the branch I failed to see.”

“What is it?”

“Chivalry.”

Mae Jonghak smiled gently.

He remembered his younger self, who had sworn to build chivalry through martial arts.

“Don’t forget again. We’re all martial artists.”

That day, with the Double Ninth Festival only four days away, two thousand martial artists left the Murim Alliance headquarters and headed north.
## Chapter artifact 951

# Chapter 951

*Whoosh…*

The sudden downpour sent everything into a flurry of activity.

Birds folded their wings and hurried into the grass. Beasts that had been prowling for food lay down inside caves, far from any human footsteps.

They were trying to preserve their body heat against the thick sheets of rain that kept falling without pause.

But the animals that inhabited this vast stretch of grassland would soon realize something.

For once, the ever-unwelcome gift of nature had saved them from an unseen danger.

*Rumble. Rrrumble.*

A sudden vibration.

The earth shook. No—it wouldn’t have been an exaggeration to say the entire grassland was trembling.

The animals hidden here and there instinctively bristled, every hair standing on end.

At the same time, with the senses they had been born with—their noses, their ears, their eyes—they saw and felt it.

Beyond the dense sheets of rain, so thick they couldn’t see an inch ahead: countless riders crossing their land.

*Splash! Thududududu!*

Mud sprayed in every direction. Hooves trampled through puddles of standing water as the horses charged forcefully onward.

At the head of the enormous, seemingly endless column, two men stood out.

“It doesn’t look like it’s going to let up.”

The lean man muttered as he gazed at the sky, then turned to the hulking man riding beside him.

“Temur.”

At the sudden call, the hulking man—Temur—flinched.

“Y-yes?”

“We should pick up the pace. If we delay, the whole area will turn into a quagmire.”

“Yes. I suppose so.”

Temur nodded in a hoarse voice. The lean man furrowed his brow.

“And?”

“Hm?”

“Is that all?”

“Oh.”

Temur blinked blankly, then realized his mistake. He gestured toward somewhere, and dozens of cavalrymen armed with bows and lances came galloping over like the wind. They bowed their heads.

“What is it, Khan Temur?”

“Tell every chiliarch under my command: no rest until the rain stops. We move at full speed.”

Temur forced himself to issue the order sternly, then added with a sidelong glance at the lean man beside him,

“Anyone who neglects this order will be severely punished in the name of me, Khan Temur, and Khan Chinggen here.”

“Understood!”

The cavalrymen scattered in every direction with a spirited salute.

Only then did the furrow between Chinggen’s brows ease.

“Good. That’s how it should be. Well done.”

Temur swallowed dryly and nodded.

“Thanks for the praise.”

“Now it’s time for you to do your part as a khan. I can’t stand beside you and give you every little piece of advice forever, can I? Right, my proud brother?”

*Tap.*

At Chinggen’s hand patting his armor, Temur’s body gave a start.

“You look terribly cold. Are you all right?”

“…Of course. Nothing’s wrong.”

“No. I know your heart better than anyone, brother.”

Chinggen let out a quiet sigh, then suddenly clenched his teeth.

“What filthy, despicable bastards. Every last one I capture, I’ll tear limb from limb and toss to the eagles.”

Chinggen’s voice rang through the rain. The nomads racing silently around them, their eyes fixed ahead, flashed killing intent in their eyes beneath their helmets.

Everyone across the grasslands already knew of the massacre that had taken place that day.

Temur and Chinggen.

The two young khans had seized the eastern grasslands in a single stroke, bringing peace and prosperity. Each had been accompanied by a hundred trusted retainers when they met.

Neither had dreamed that the ger, once filled with laughter, would soon be drenched in blood.

“Who could have known those damned Han Chinese would hatch such a horrifying plot?”

The uninvited guests—several hundred of them—were Han Chinese from the Central Plains. They were the sort known as Murim martial artists.

They had burst in at the height of the feast and swung their weapons at anyone in reach.

By the grace of heaven, the two khans had survived. But after a fierce battle, most of the retainers under their command had been left lying in pools of blood.

“My dear brother. If Tengri hadn’t watched over us, the eastern grasslands would have been torn apart in an instant and fallen into the hands of those Han Chinese.”

Chinggen gripped his reins tightly in his whitened hand.

“It’s obvious what they were after. They must have judged that we’d become a threat, with each of us commanding a powerful force. At last, they’ve shown the ambition they’d kept hidden.”

At the cold light in Chinggen’s eyes, Temur answered in a voice rough as iron.

“I—I think so too.”

“It wasn’t just us. Everyone on this land was being used by them from the very beginning. Those despicable bastards were planning to seize the entire grassland all along.”

The nomads listening to Chinggen’s seething voice nodded together, as if they’d agreed to do so.

That was right. The Han Chinese had always been like that.

Since time immemorial, they had called them barbarians, scorned them, and thought them worth less than beasts.

Even after their great ancestors had trampled the Central Plains beneath countless hooves and built a vast empire, nothing had changed.

No—instead of mere contempt, they had come to show hatred.

All because a mere band of barbarians had sullied the history of the continent.

But human beings were creatures of forgetfulness.

As the years stretched on and the achievements of their ancestors gradually faded from memory, they began to want something new.

Peace, instead of conquest.

Gold and silver, instead of horse manure.

Perhaps that was why everyone had welcomed the two promising young men of the Golden Clan with open arms when they joined forces with the Han Chinese.

Temur and Chinggen.

“It was my mistake.”

Chinggen lamented as the rain poured down on him.

“I should have thought more deeply about what kind of people they were, and why they’d agreed to work with us. Noble warriors of the grasslands died because their leader was ignorant and foolish.”

At the sight of his grief and regret, everyone lowered their heads.

Then came a calm, powerful voice.

“If you correct that mistake, the warriors of the grasslands will be welcomed into Tengri’s embrace.”

Chinggen’s eyes widened as he spotted a middle-aged man with the distinctive braided hairstyle of the nomads.

“Why is Khan Jamukha here? You should be in the rear…”

“Greetings, Khan Jamukha!”

Exclamations erupted in every direction, beginning with Chinggen.

The middle-aged man, Jamukha, swept his gaze over them, his eyes imbued with an irresistible force, then spoke.

“It was dull staying in the rear. I thought this old man might be of some help, so I came to see.”

His hair was as black as night at the temples, and his imposing build was more robust than that of a young man in his prime.

But that was only what he looked like. Jamukha was well over eighty years old.

The greatest warrior on the grasslands, and another khan who had ruled the western grasslands for many years.

He had joined the army with more than twenty thousand tribespeople. In practice, he was the one leading this immense force.

“Old man? Who would dare think that of you? Isn’t that right, Temur?”

Temur gazed at Jamukha with trembling eyes, then hurriedly nodded.

“Y-yes.”

“Khan Jamukha is our elder in the Golden Clan, a great warrior and a khan. We’re grateful just to have been entrusted with the vanguard.”

Chinggen raised his voice so everyone around them could hear.

“Those foolish Han Chinese probably never knew how strong Khan Jamukha was—not even as they were dying.”

Even without a word from Chinggen, the looks fixed on Jamukha were already full of admiration and reverence.

Jamukha, the greatest warrior on the grasslands.

According to what people knew, he had been attacked by several hundred Han Chinese before Temur and Chinggen were.

He had only a dozen or so personal guards with him.

But the outcome had been staggering.

Jamukha had proved his prowess beyond doubt.

With a mere handful of guards—barely a match for the enemy numbers—he had fought a battle against the Han Chinese that was little short of a massacre.

In the end, the Han Chinese plot that had threatened even the western grasslands came to nothing. Enraged, Jamukha had led his tribes south toward the Central Plains.

Just as he was now.

“It was nothing. My men were simply skilled.”

Jamukha answered calmly and jerked his chin over his shoulder. His personal guards, clad in dark armor, galloped after him with expressionless faces.

They were the elite warriors created by the great conqueror who had laid the foundations of the nomadic empire in the distant past.

Known as the *Keshik*, they still followed Jamukha as remnants of the Golden Clan.

Each one was as strong as the finest warrior in any tribe.

And there were a thousand of them.

The immense grassland army, numbering tens of thousands, wasn’t confident of victory on nothing but hope.

“From here on, some of my personal guards will take the vanguard.”

“The Keshik, you mean?”

“Yes. Is there a problem?”

Chinggen fell silent for a moment at Jamukha’s unexpected words, then shook his head.

“Of course not. We’d be the ones asking you. Isn’t that right, Temur?”

“…That’s right. I agree.”

The strongest warriors would lead the charge.

It was an obvious decision, and everyone accepted it.

Everyone but one person.

*Are you sure that’s wise?*

At the sudden Sound Transmission that pierced his ear, Jamukha’s lips moved.

*Didn’t you just say you’d be the one asking me?*

*Well…*

*I won’t change my mind. We’ll put those children in the vanguard and cross the border in the shortest time possible.*

*There could be a trap. The place is crawling with fodder to take arrows for us. Why waste precious forces?*

*What trap are you talking about? Fire King and Jin Taekyung, who won’t reach Shanxi Province for several days? Or those insignificant Shanxi fools?*

Jamukha answered bluntly and stared directly at the source of the Sound Transmission.

*You’d better keep that idiot beside you under control. I’m starting to regret not killing him back then.*

*I told you we should’ve spared the smarter one instead.*

Chinggen—or someone wearing his face—let out a faint, nearly imperceptible chuckle and ran a hand over his own features.

*That man was impressive, in a way. He tried to negotiate even as his men were dying all around him.*

He remembered it clearly.

Beside Temur, who had surrendered before an overwhelming difference in strength and even wet himself, Chinggen had shown his mettle, telling them to name what they wanted.

*Compared to that dead man, this idiot…*

*I kept him alive because he’s an idiot. Someone who’s surrendered deep in his heart is that much easier to handle.*

*I’ll grant you that. Thanks to his cooperation, far more barbarians gathered than I expected.*

His amused gaze swept across the vast army that filled the grasslands.

Only about a day remained.

When the rain stopped, they would cross the grasslands and pass over the fortress walls.
## Chapter artifact 952

# Chapter 952

The Double Ninth Festival was one of the continent’s biggest holidays.

It was the time of year when the swallows left for the warmer south, and snakes and frogs burrowed underground to prepare for hibernation.

Around this time, people would climb mountains, drink chrysanthemum wine, recite poetry, and enjoy the scenery.

That was true of everyone, from commoners who lived from one day’s wages to the next, to high-ranking officials who wanted for nothing, to martial artists who had made their home in the turbulent martial world.

“Do you remember?”

A voice suddenly rang out behind him.

But the young man, silently gazing at the field of bright yellow chrysanthemums, wasn’t startled at all.

He had known for some time who the voice belonged to.

“Remember what?”

The young man, Jin Mukyung, asked without taking his eyes off the flowers. A familiar presence approached and came to stand beside him.

“Five years ago, when the three of us brothers climbed the hill behind the house and spent the Double Ninth Festival together. We had a wonderful time.”

“…You mean the Double Ninth Festival ten years ago?”

At his younger brother’s doubtful response, Jin Wikyung looked hurt.

“Goodness. You don’t even remember anymore?”

“I remember. I only ask because it seems quite different from what I remember.”

“Different?”

“Taekyung, that reckless fool, got completely drunk and caused a scene. It wasn’t exactly a pleasant time.”

Jin Wikyung tilted his head.

“Is that so? You looked like you were having a pretty good time when you were beating him with your scabbard.”

“I wasn’t smiling. I was simply disciplining my own flesh and blood to guide him onto the right path.”

“For someone who wasn’t smiling, the corners of your mouth were practically up to your ears.”

Jin Mukyung fell silent for a moment at Jin Wikyung’s spot-on remark.

Come to think of it, perhaps he had been smiling.

A troublemaking youngest brother, and an older brother who doted on him to no end.

How could he not smile when, in this unbearably frustrating situation, he’d been given an excuse?

Of course, that had all happened long ago.

It remained only as a tiny fragment of memory in his mind.

“The youngest bawled like the sky had fallen, and you didn’t touch your food. You just started training. You went off into the woods, away from everyone, and swung your sword until sunset. I can still picture you as clearly as if it were yesterday.”

“I don’t remember that, but I’m sure it happened.”

Jin Mukyung replied calmly.

Training was as natural to him as breathing. He had held a sword since childhood, and had always devoted himself to training, wherever and whenever he could.

Five years ago, the last time the three brothers of the Jin Family of Taiyuan had celebrated the Double Ninth Festival together, Jin Mukyung had already reached the Peak realm, though he was barely twenty.

“I still remember the day you left home.”

“Ah.”

Jin Mukyung smacked his lips.

He remembered his brother coming to see him off with a swollen face, as if he’d spent the previous night crying.

*“Do you… do you really have to go?”*

*“Yes. I really do.”*

*“Even if your older brother begs you like this?”*

*“Not a chance.”*

*“What’s so special about that Heaven’s Gate Temple that you’d abandon your own family and go all the way to a foreign land?”*

*“Even disciples of the great sects wait years to get into that Heaven’s Gate Temple you call so unimportant.”*

*“All right. If that’s really what you want, I’ll personally escort you to Henan.”*

*“…You’re serious?”*

*“There’s something I need to tell the Hall Master in person.”*

*“What on earth do you need to tell him?”*

*“Just a few important precautions he absolutely needs to know. Some foods you hate, your habits… Mukyung! Where are you going, Mukyung!”*

He ran. With every last bit of strength he could muster.

It was the first time in his life he had ever used his movement technique with such effort.

Jin Mukyung had only wanted to grow stronger at Heaven’s Gate Temple. He’d never had the slightest intention of earning the distinction of being its shortest-lived expelled cadet.

“I still remember your back as you left, covering your eyes with your sleeve to hide your sobs.”

“……”

Jin Mukyung quietly closed his mouth.

Some truths were more beautiful left unrevealed.

Like covering your eyes with your sleeve to keep out the dust, or running away to escape your overzealous older brother.

And then, before he knew it, a quiet laugh escaped him.

“Why did you suddenly laugh?”

“It’s nothing. Just…”

Jin Mukyung finally managed to stop laughing and turned his head.

The face of someone who had watched him with deep concern, about two years ago, when he left once again to enter seclusion for training with no end date in sight.

Just as it had been then.

“I laughed because I’m glad to see you. You haven’t changed at all, older brother.”

“Mukyung, you…”

“I’m glad everything is still the same.”

He had spent a little over two years in pitch-black darkness.

He’d staved off his hunger with bitter, astringent fasting pills, and quenched his thirst with dew and rainwater that collected in the training hall deep inside the cave.

And whenever he swung his sword until he collapsed from exhaustion, sprawled on the cold ground, a thought would come to him.

Where was this place? Who was he?

If he ever escaped this darkness, what would be waiting for him?

“Part of me was afraid, too. Afraid that the world I knew, the people I knew, would have changed beyond recognition.”

That guess had been half wrong and half right.

Everything around him had changed, but the people he knew were just as they’d always been.

Even the troublemaking youngest brother, whose whereabouts were unknown now, would surely be the same.

“The day that brat left home, he came to find me and said something.”

It was a conversation he had turned over in his mind thousands of times. No—tens of thousands.

Jin Taekyung’s voice, so very calm for once, still echoed in his ears at that very moment.

*“See you later.”*

It had been more than a simple farewell.

At the Star-Array Grand Banquet, among the countless stars gathered from the Nine Provinces and Eight Wastes and the Four Seas and Five Lakes, Taekyung had challenged him to meet and test their skills together with Cheongpung.

As brothers born of the same mother. As martial artists.

And Jin Mukyung, standing motionless as he watched the empty place his younger brother had left behind, had murmured the answer he hadn’t managed to give him.

*Yeah. See you later. I promise.*

But that promise had never been kept.

In that place, where he could not even feel time passing, Jin Mukyung swung his sword without rest. He slashed, stabbed, and tore through what lay beyond the pitch-black darkness.

Whenever he opened his eyes to something new, another wall rose before him.

He had to climb it. He had to break it.

With the unkept promise tucked away in a corner of his heart, Jin Mukyung continued to press forward.

Until he found a faint light in the darkness.

Until that light grew as clear as the sun.

And at last, he returned to the world.

Leaving behind the darkness that had enveloped him for two years, only to emerge into a world filled with another kind of darkness.

“Older brother.”

Jin Mukyung called softly and looked his own flesh and blood straight in the eyes.

His eyes held a light.

They were honest eyes that made it impossible for anyone looking into them to lie.

“Tell me what I have to do now.”

“……!”

“No. Give me an order. As the Lesser Family Head of the Jin Family of Taiyuan.”

For a moment, Jin Wikyung’s eyes trembled.

“You knew…?”

Jin Mukyung gave a quiet nod.

The Jin Family of Taiyuan now stood at the head of Shanxi Murim, and Jin Wikyung, who led them all in place of the missing Family Head, was its Alliance Leader.

Shanxi Province was already in a state of war.

Li Feng, a lay disciple of Huashan and Shanxi Province’s Assistant Military Commissioner, had mobilized all the forces of the Shanxi Provincial Office to evacuate the people in the north. Around five thousand martial artists had gathered in the central region.

Every moment mattered.

Jin Wikyung must have sought him out for more than the simple wish to reunite with the younger brother who had returned to the world after two years.

“Just as you know me well, older brother, I know you just as well.”

“This will be a dangerous mission.”

“I don’t mind.”

Jin Mukyung continued in an even tone.

“I learned martial arts because I loved the sword, but I sought strength for the sake of our family.”

Only great strength could restore a fallen martial family.

The sword Jin Mukyung had wielded all this time had carried more than just his passion for martial arts themselves.

“Jin Mukyung, Second Young Master of the Jin Family of Taiyuan. I will devote myself to carrying out the Lesser Family Head’s orders.”

At the sight of his younger brother cupping his hands in a salute and speaking without the slightest hesitation, Jin Wikyung slowly closed his eyes.

Then, after a brief hesitation, he opened them again. By then, he was no longer just an older brother. He was the Alliance Leader of Shanxi Murim and the Lesser Family Head of the Jin Family of Taiyuan.

“From this moment on, you are neither the Second Young Master of the Jin Family of Taiyuan nor the Lesser Family Head’s younger brother.”

He let out a breath he’d been holding, then spoke.

Jin Wikyung looked at his younger brother—or rather, his retainer—with a calm gaze and continued.

“I command Jin Mukyung, Commander of the Heaven Shaking Squad.”

Jin Mukyung, the Heaven Shaking Sword.

About five years ago, a young prodigy from the frontier had reached the Peak realm at barely twenty and earned a new epithet. His only older brother had named a fighting force after it.

In the hope that his younger brother would return to this place one day.

And with the wish that, just like the two characters in Heaven Shaking, his name would one day resound beyond the world and reach the heavens.

“The enemy vanguard that invaded the north has split off some of its troops and is taking a detour to avoid Jeongyang. Take two hundred men from the Heaven Shaking Squad and blunt their vanguard.”

Jin Mukyung smiled as he answered.

“As you command.”

* * *

The next day.

The vast steppe army, which had entered the north without meeting any resistance, was met not by chrysanthemums, but by dark-red blood covering the mountain slopes and a terrified survivor of its vanguard.

“K-Khan…”

Jamukha stared silently at the man trembling like a leaf.

He knew instinctively: the thousand-man vanguard that had invaded Shanxi Province half a day ahead of the main force had been completely wiped out.

And what the only surviving fool before him had brought was a stark warning to the invaders.

“H-he told me to deliver this to you, Khan…”

*Slide. Thump.*

The cloth slipped from the man’s trembling fingertips.

Jamukha silently watched the head of a Keshik centurion roll out from among the blood-soaked fabric, then spoke.

“Is that all?”

“He left a message. A message…”

The survivor, his queue come loose and his face contorted with fear, continued.

“He said, ‘Even five years from now, my brothers and I will climb the mountain together and celebrate the Double Ninth—’”

“Bullshit.”

*Shhk.*

A hand without the slightest hesitation.

His severed head rolled into the chrysanthemum field.

As Jamukha gazed at the field of flowers whose original color was no longer visible, Chinggen clicked his tongue.

“Why not hear him out? You don’t even know who he was.”

“Does that matter?”

What mattered was that a thousand men in the vanguard had been annihilated.

No—what mattered was that a hundred Keshik among them had died in a single battle.

“Either way… we’ll meet soon enough.”

Jamukha’s voice sank low as he stared south.

At that moment, a thought suddenly crossed his mind.

This war, which was supposed to be overwhelmingly one-sided, might not be as easy as he had imagined.
## Chapter artifact 953

# Chapter 953

When dozens or hundreds of people fought tangled together, it was a battle.

But when the numbers grew to thousands, tens of thousands, it could no longer be called a battle.

It was war.

A war in which both sides clashed with all their might, each staking everything they had.

And Jin Wikyung had not the slightest intention of gambling everything he had on a single throw.

“Commander of the Heaven Shaking Squad, Jin Mukyung. I report to the Lesser Family Head.”

His voice was calm, but his whole body was soaked in blood.

Jin Mukyung had left at noon and returned only around midnight. He looked like nothing so much as a blood demon.

So did his men, whose squad took its name from his epithet, the Heaven Shaking Sword.

But their proud strides and blazing eyes were proof of the Jin Family of Taiyuan’s first victory.

“Under your strict orders, I broke the enemy’s vanguard and returned.”

Jin Mukyung continued, unhurried.

Of the slightly more than two hundred men in the Heaven Shaking Squad, twenty-three had died and thirty-seven had suffered injuries, both serious and minor.

At the news that a single battle had left sixty casualties among the elite fighting force the Jin Family of Taiyuan had devoted itself to cultivating alongside the Jin Dragon Squad, several of the senior leaders grew somber. But the report that followed washed away even that brief sadness.

A thousand.

They had annihilated the enemy vanguard, five times their number.

And that included a hundred of the enemy’s elite troops.

“Waaaah!”

The people who had been listening in tense silence all let out a cheer at once.

Their first victory against the enemy.

And not just a victory, but an overwhelming one beyond any dispute.

Yet even as the air grew hot with excitement, Jin Wikyung kept his composure amid the celebrations.

*This is only the beginning.*

He knew it.

War was like building a sandcastle. You had to keep scooping up sand and piling it on, again and again, before it was complete.

And even a sandcastle painstakingly built that way could collapse from a single hard kick.

*But if we build it solidly enough that it won’t collapse even when kicked, that changes things.*

Fortunately, the Jin Family of Taiyuan’s preparations had been thorough enough to make the limited time they’d had seem irrelevant.

By now, the grassland army—likely crossing the Great Wall and passing through northern Shanxi Province—must have been bewildered.

First, by the news that its vanguard, which included its finest troops, had been wiped out.

Then again, by the situation in the north, which had truly been left *empty*.

*You won’t find a thing to take in the north.*

It wasn’t only the people who had left the north.

Jin Wikyung had pulled all the troops and commoners back from the north. He had also ordered every field—on the verge of harvest—to be burned.

A scorched-earth strategy.

Naturally, it was an excellent tactic against a huge army numbering in the tens of thousands. But Jin Wikyung had agonized over the decision dozens of times before making it.

That was, until Assistant Military Commissioner Li Feng of Shanxi Province and several hundred people came to him first.

*“We have several tens of thousands of seok of provisions in reserve. We can more than handle their food supply.”*

Li Feng, who could be considered the most senior official actually present at the Shanxi Provincial Office in the absence of Zhu Bao and Hong Jin, promised his full cooperation.

*“Just burn the whole damn lot.”*

The northern villagers, forced to leave their homes overnight—or rather, the village headmen—were already half blind with rage.

*“Those damn bastards. They’ve been storming in and raising hell all the time, and now they’ve come to take our fields, too?”*

*“Everyone in our village has already agreed. If even one grain of rice gets into those barbarian bastards’ mouths, I’ll be torn to pieces.”*

*“I’d sooner feed rice to pigs and cows. I wouldn’t stand for that even after I’m dead!”*

*“Shit. If anyone objects, step forward now. I don’t know who you are, but if you so much as open your mouth, I’ll call you a barbarian and shave your head clean so I can give you a queue!”*

*“Hey, you, Mr. Song! Why aren’t you saying anything? You got honey on those fields?”*

And the village headman, Mr. Song, who had stayed silent without saying a word, earned a round of applause from everyone with just one suggestion.

*“Don’t just set fires. Let’s poison the wells.”*

*“……!”*

*“It’d be even better if we took a dump and pissed in the stream before we left.”*

*“Why the piss and shit, too?”*

*“It’ll dirty the water. You think those bastards will be fine after gulping down water mixed with shit and piss?”*

*“Good heavens! How could anyone come up with such a brilliant plan…!”*

*“I tried it once. Drank nearly half a gallon of the stuff. Thought I was going to die.”*

Mr. Song, a farmer with the unusual distinction of having drunk sewage, became a hero overnight. As people shoved poisonous weeds into the wells and shat and pissed by the streams, they wondered why he hadn’t placed first in the civil service exams.

All while saying that the only good barbarian was a dead one—words that would have shocked someone if they’d heard them.

*The road here won’t be easy.*

Jin Wikyung wore a cold smile.

Shanxi Province was undeniably a frontier.

It produced plenty of grain, but it was neither as developed as the Central Plains nor as powerful.

But for that very reason, when crisis came, its people could come together all the more strongly.

The long years of raids by mounted bandits and nomads had instilled a fierce resolve in the people of Shanxi. Now that resolve had caught fire.

*We will protect it. No matter what.*

Jin Wikyung had already made up his mind.

He had given up sleep and rest, devoting himself to everything at hand. He sent swift-footed subordinates to survey the situation in the north and organized small detachments to watch for any unexpected division of enemy forces.

He had personally ordered traps and iron caltrops set along every detour except Jeongyang, and checked on the progress of the work himself. All of it was part of the same effort.

“How is the earthen fort coming along?”

“Taking the reinforcement work into account, it should be finished within half a day at the latest.”

Eight Spring Gorge.

At the end of this vase-shaped gorge, which had swallowed countless lives from the Great Faction War to the present, five new towers now rose where none had stood before.

Made from a mixture of mud, wood, and stone, each stood three *jang* high and had a flat area large enough to accommodate a little over two hundred people.

Two hundred archers, to be exact.

“Taking the heights above the gorge isn’t enough. These forts are essential to our victory. Please do everything you can to make sure they don’t collapse.”

“Of course, sir.”

The old carpenter answered in a folksy drawl.

Even as the two exchanged a few brief words, countless people around them went about their assigned tasks.

They were a diverse lot.

Martial artists in uniforms embroidered with the names of their sects tirelessly hauled weapons and heavy materials. Government troops in official uniforms moved in orderly formation at the commands of their officers.

But Jin Wikyung’s gaze was fixed on another group, each dressed so differently that their affiliations were impossible to make out, all hard at work.

“On three, pull!”

“One, two!”

“Hyaah!”

The men, covered in dust, labored on, sweat streaming off them.

“Where should we put these arrows?”

“Oil! Bring the oil over here!”

The women carried supplies needed for battle and prepared simple meals.

As Jin Wikyung looked at the several thousand commoners, he felt a tightness in his chest.

*I told them to flee as far away as they could.*

He had warned them in all sincerity, over and over. He had tried to persuade them.

This wasn’t just a dispute among martial artists.

It was a brutal war that would claim countless lives, and they—the powerless—would suffer the most.

But the people who had already made up their minds had refused to leave to the very end.

They had come here to help, even onto a battlefield about to be swept by a storm of bloodshed.

Like the old carpenter standing before him.

“Looks like our Lesser Family Head has a lot on his mind.”

The old carpenter, who had been glancing sideways at Jin Taekyung, chuckled.

He said he had turned seventy several years ago. As he laughed out loud, air whistled through the gaps between the few teeth he had left.

“Don’t you worry about it. This old man and all those folks out there came prepared.”

“But still… how could I not worry?”

“Goodness, please don’t speak so formally to me. I may be an old man with little time left, but I’m not shameless enough to expect the Lesser Family Head to address me with honorifics.”

The old carpenter hurriedly waved his hands. Warmth shone in his pale gray eyes as he looked at Jin Wikyung.

“Even a beast that can’t speak repays a kindness someday. How could a person turn away from a situation like this?”

“What do you mean by that…?”

“When I was young and in my prime, the country must have been nearing its end. The Demonic Cult, or demons, or whatever those wretches were, stirred up trouble all over the place, and then years of bad harvests followed.”

It had happened a long time ago.

Before Jin Wikyung was even born.

But the old carpenter remembered it clearly. The days when they boiled and ate leather, and stripped bark from trees to chew.

Everyone was starving, so there was no one to turn to for help—and no one who could help.

If a group of men hadn’t come to their village one scorching day, he and his family would have starved to death before long.

*“Is this Hong Family Village?”*

*“Y-yes, it is. What brings you here…?”*

*“Phew. Thank goodness we found the right place.”*

What was the point of tilling fields that yielded not a single grain?

They had abandoned the already barren land long ago, gone into the mountains, and become slash-and-burn farmers.

So at first, they’d thought the newcomers were bandits.

Or strongmen sent by some powerful official to squeeze the last bit of blood from them, when they didn’t have a single iron coin or handful of grain left.

Otherwise, there would have been no reason to come all the way into these deep mountains.

But instead of drawing the swords at their waists, the men set down the loads they had been carrying.

They were huge sacks.

Dozens of them, filled to the brim with grain and meat—the kind of sight they could barely remember ever seeing.

*“W-what in the world is this…?”*

*“Get in line. We’ll hand it out one by one.”*

It felt like a dream.

When every villager lined up together at the men’s direction, and when he watched his wife and children—who had been lying weak and helpless for days—eat until their bellies nearly burst.

And then, when he had stared blankly at that unbelievable sight and swallowed a mouthful of warm meat broth, only then did he realize it was all real.

So he cried.

No—everyone cried.

They wept aloud even as they chewed and swallowed what was in their mouths.

Because they wanted to live. Because they wanted to make sure they were alive.

“If we hadn’t received help that day, this old man and my family would have starved to death right there.”

The old carpenter looked at Jin Wikyung with tear-bright eyes. Unlike back then, a radiant smile now rested on his lips.

“But those kind people were about to leave without saying a word. So I grabbed one of them by the leg and clung on.”

He couldn’t read, not even the characters written on their clothes.

So he’d clung on stubbornly, asking where they were from and begging them to tell him their three-character names.

After a long struggle, he finally heard the answer he wanted.

“From that day on, I vowed that if the Jin Family of Taiyuan ever needed it, I would give this worthless life of mine.”

“……!”

“And it’s not just me. Every one of these people has received help from the Jin Family of Taiyuan, in one way or another.”

Some of those who had received their kindness left. Others stayed.

And those who stayed were ready to lay down their lives.

To protect the land where their fathers and mothers—and they themselves—had lived.

To repay the Jin Family of Taiyuan, who had reached out to help them on the day they had lain exhausted, waiting to die.

That was the Jin Family of Taiyuan’s true strength: the strength of a distinguished family that had endured for three hundred years through the rise and fall of fortune.

*Ah.*

Jin Wikyung felt an ache deep in his chest.

He wondered if he himself had been the one to underestimate the Jin Family of Taiyuan—and Shanxi Province—most of all.

And just as Jin Wikyung turned away to hide his reddened eyes—

*Thududududu!*

A fierce pounding of hooves, clear even from a great distance.

A single fine horse raced across the gorge as if fleeing something. Hanging from its back was a martial artist of the Jin Family of Taiyuan, dead with his eyes wide open.

“……!”

“……!”

The air froze in an instant. Jin Wikyung shouted as if spitting blood.

“Everyone, prepare for battle!”

They were here.
## Chapter artifact 954

# Chapter 954

When the sun dipped toward the western mountains and darkness settled all around, the quiet world carried things you’d never been able to hear before on the wind, right to your ears.

The cries of crickets. Leaves brushing against one another.

And, from hundreds of *jang* away, something like a shout from someone whose voice carried internal energy.

“I don’t know who that bastard is, but he’s got a set of lungs on him. Don’t you think?”

At the low voice that pierced his ears, Temur swallowed nervously.

His trembling eyes reflected the sight of someone smiling in the faint moonlight.

Chinggen.

His blood relative, who had grown up alongside him since childhood—so long ago that even those memories had grown hazy.

Though they hadn’t been born to the same parents, Chinggen was his cousin, closer to him than a blood brother, and his sworn brother, bound to him by the anda oath.[^1]

And… now he was dead. No longer one of the living.

*This is no time to laugh and chatter, Temur.*

Before the unusually cold steppe wind pushed open the entrance to the ger, Chinggen had spoken to him with a worried look on his face. The memory suddenly flashed before his eyes.

*Brother, I’m sorry. You were right.*

Temur lowered his head, his heart heavy.

Why hadn’t he listened to Chinggen?

Even before that day—the day of the tragedy that made his whole body shudder just to remember it—Chinggen had sent word through messengers several times.

The mood on the grasslands was turning strange.

It seemed something unknown was beginning to unfold somewhere beyond their reach.

But Temur had dismissed his words without a second thought.

He had filled his ger with all manner of rare treasures brought in along the trade routes, then drank and feasted to his heart’s content with his men.

Never once dreaming what it would lead to.

“What’s got you so lost in thought this time, brother?”

In an instant, Chinggen’s face, wavering before his eyes, disappeared.

Temur jerked his head up, startled like a man just woken from sleep, and answered in a trembling voice.

To the man who had killed Chinggen—and had now become Chinggen.

“It’s nothing. Nothing at all.”

“Goodness. You must be nervous before the battle. Is that why you didn’t hear me?”

“What do you mean…?”

“That shout we just heard. Don’t you recognize the voice?”

Only then did Temur grasp what he meant, and hurriedly answered.

“Y-yes. It’s the Lesser Family Head of the Jin Family of Taiyuan. It can only be him.”

“Ah, I see. I thought I’d heard that voice somewhere.”

Of course, it was a lie to avoid arousing suspicion from anyone nearby.

Temur might have been simple, but there was no way the meticulous Chinggen would forget an important figure he’d met several times.

“Jin Wikyung… So that’s who it is.”

Chinggen smacked his lips in satisfaction, then glanced over his shoulder.

At the meaningful glance, Jamukha, who had been riding ahead with an impassive expression, gave a slight nod.

*He’s not just loud. The Lesser Family Head of the Jin Family of Taiyuan has some nerve.*

Sound Transmission spread discreetly through the darkness.

A faint smile touched Jamukha’s lips.

*If he’d planned to run from the start, he wouldn’t have gone to the trouble of pulling off that trick.*

*It was quite a trick for a mere ruse. We took losses we never expected, thanks to it.*

Chinggen frowned and spat out a mouthful of phlegm from the swaying saddle.

The Great Wall, built across a full ten thousand *li* by a cruel and merciless emperor who had unified the continent long ago, was hardly worthy of being called a wall.

Yet the north, which should have been unoccupied, was littered with obstacles everywhere.

*I can accept that the vanguard was wiped out, but I never expected them to turn the whole place into such a filthy shitshow.*

A shitshow.

In Chinggen’s view, it was the perfect word.

Northern Shanxi Province, where they had arrived after braving wind and rain, had been utterly devastated.

The fields, which should have been on the verge of harvest, had been laid to waste. Wells and streams were covered in poison and filth. Even the houses had been reduced to ashes.

*Those lunatics. They burned down every last thing they’d called home until just recently, then left.*

At Chinggen’s Sound Transmission, Jamukha’s lips moved, his expression still calm.

*Do you know of Emperor Gaozu of Han?*

*I’ve heard of him. The Liu Bang from the story of Xiang Yu and Liu Bang, right?*

*That’s right. Even the man who became the final victor was once driven back by Xiang Yu and forced to retreat to Hanzhong. At the time, his strategist Zhang Liang advised him to burn the plank roads.*

*He cut off his own way back.*

*But he eventually returned to the Central Plains, drove out Xiang Yu, and became its ruler. To them, this land is that plank road. As long as people remain, they can rebuild it whenever they want.*

One person alone was an individual. Ten people made a group.

But when a hundred or a thousand gathered, villages and cities came into being.

In the end, people were what mattered.

Though everything in the north had been destroyed, they must have burned their own homes and vowed to themselves:

*We’ll return and reclaim this land.*

*Just as our ancestors did in the distant past, we’ll begin anew from these ruins, with nothing left.*

*Of course, all of it is nothing but a vain hope.*

Jamukha smiled faintly.

Xiang Yu had been arrogant and foolish.

That was why, despite having the might and power to look down on all under Heaven, he had ultimately been defeated by Liu Bang.

But Jamukha was different.

For decades, he had steadily strengthened his hold over the western grasslands and built his forces, waiting for that person to call for him.

And at last…

*The time has come.*

Jamukha gazed into the pitch-black darkness. There, where even the moonlight was dimmed by dark clouds, he could almost see the enemy holding their spears and swords upright, struggling to master their trembling hearts.

“Can you feel it? Their fear.”

His low voice rang through the darkness.

Jamukha’s voice, charged with internal energy, pierced clearly into everyone’s ears, and his eyes shone fiercely.

“Our enemies have spent their entire lives hiding behind tall walls. They’re no different from cows and pigs, wallowing in peace and doing nothing but consuming food!”

But what of the grasslands?

They had been born from grass and earth.

They had endured the cold north wind in gers, not behind walls, and raced with their horses across snowy fields to hunt beasts.

To the nomads of the grasslands, the word *death* came cheap. Plunder and murder were taken for granted.

“They don’t know where we came from, or how mighty our ancestors were as conquerors!”

His forceful voice pressed down on the night air.

It was as if the sound of their ancestors’ hooves, trampling across lands covered in frost and ice and crossing the dreadful, scorching desert, were faintly echoing in everyone’s ears.

“Draw your bows with clear eyes. Thrust your spears like a tiger’s claws. Slice through their flesh with your crescent sabers, sharp as an eagle’s talons, and trample them under your horses’ thundering hooves!”

A light slowly kindled in the nomads’ slack eyes.

More than half a month of relentless marching, and traps scattered everywhere.

Thousands had lost their beloved horses to iron caltrops coated in poison. Thousands more had collapsed after drinking contaminated water.

And that wasn’t all.

With even their homes burned down, they had to sleep outside beneath the night dew, and fill their stomachs with tough jerky made in the saddle, all in the name of speed.

But it didn’t matter.

Even if thousands of men and horses had fallen, tens of thousands remained.

If they crushed the enemy—who numbered less than half their own force—and won this battle, it would all be over.

Beyond that gorge, shrouded in deep darkness and waiting for them, lay more than just their weak and helpless enemies.

Wealth and honor. And a new age.

“My beloved brothers, remember our ancestors! Remember the grasslands, where nothing but glory awaited us!”

Jamukha cried out.

Like the king of beasts ruling the grasslands.

Like the great conquerors of the past, who had left their gers and thundered across the continent with the sound of their horses’ hooves.

Then, glaring at the gorge, now less than a hundred *jang* away, he spoke in a low but clear voice.

“Now, it’s time to conquer.”

At that moment—

*Clang-clang-clang-clang!*

Countless waves of steel swallowed the darkness.

Gently curved crescent sabers, sharp lances, and arrows nocked to bowstrings like lightning flashed all around them.

“Waaaaah!”

With a tremendous roar that not only shattered the deep night but made heaven and earth themselves seem to tremble—

*Thududududu!*

Dozens became hundreds. Hundreds became thousands.

At last, tens of thousands surged toward the gorge like the wind.

They let out eerie cries that sent chills down the spines of those who heard them. Their hair, waving like horses’ tails with every bounce, streamed behind them.

They charged forward with all their might, to avenge the tragedy built on lies and seize the ancient glory their ancestors had won.

*Rrrrummmble!*

And the people beyond the gorge could feel the fierce shaking beneath their feet, as if an earthquake had struck.

“So it comes to this, after all.”

Jin Wikyung murmured, then looked down at his hand.

His fingers, clenched tight around his sword hilt, had begun to tremble.

Why?

Was he afraid of the enemies bearing down on them, radiating a tremendous aura even now?

No.

What he feared was not the enemy, but the countless allies who would die here.

And himself, unable to protect them all.

*That’s why… we have to win.*

He had already taken every measure he could.

There was no turning back, no retreating now.

*Do everything within your power, then leave the rest to Heaven.*

Jin Wikyung suddenly remembered the old saying: people should do all they can, then leave what remains to Heaven.

And with it, someone who had hated those words more than anyone, and was no longer here.

*No. If you’re just going to leave it to Heaven in the end, why go through all that hell? You’ve got to make Heaven change its mind, even if you have to raise all kinds of hell to do it.*

Yes, that was exactly what the guy would have said.

At the vivid voice ringing in his ears, Jin Wikyung let out a laugh before he knew it.

Then, the next moment, he realized his hand had stopped trembling.

“Wipeng.”

At the low call that cut through the thunder of approaching hooves, his longtime loyal retainer answered.

“Yes, my lord.”

Tens of thousands of men and horses would arrive in mere moments.

Ragged breaths sounded all around them.

Everyone’s eyes were fixed on their commander-in-chief, Jin Wikyung, when an unexpected remark reached their ears.

“Next year, I think we should spend the Double Ninth Festival on Mount Heng.”

“……!”

“Let’s all drink chrysanthemum wine together, play music, laugh, and enjoy ourselves.”

“M-my lord.”

“What? Don’t you like my suggestion?”

Everyone, Wipeng included, stared blankly at Jin Wikyung, who was smiling faintly.

Then, as if they’d agreed in advance, they all wore smiles that resembled his.

They held back the surge of emotion welling up inside them.

*Next year, we’ll all be together for the Double Ninth Festival.*

The meaning contained in those few words stirred something in their hearts.

As smiles touched their lips, fear disappeared. When they laughed aloud, their stiff bodies loosened.

The deep darkness hanging all around them no longer felt unsettling.

*Step.*

A footfall rang out, unusually clear. Someone stepped forward before them all and spoke.

“Next year’s Double Ninth Festival sounds like it’ll be quite enjoyable.”

Jin Mukyung was smiling.

Amid the vibration and shouts that had swallowed the gorge.

In the darkness that had been his only friend for the past two years.

And the next moment—

*Thudududu—whoosh!*

As if a curtain had been drawn aside, he turned toward the dozens of men and horses bursting out of the pitch-black darkness.

*Shing!*

A dazzling flash leapt from his waist and cleaved through the faint moonlight.

[^1]: An *anda* is a sworn brother in Mongolian tradition; the oath binds two people as brothers.

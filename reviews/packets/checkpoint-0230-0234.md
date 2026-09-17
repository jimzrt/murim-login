# Checkpoint Review — 230–234

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

# Chapters 230–234

## Plot

Jeok Cheongang and Jin Taekyung reach Luoyang on their journey to Anhui. At an inn, Jeok defeats Heukgeol, a Dongcheon Sect officer, while Taekyung subdues the other dark-path swordsmen. A young Shaolin monk named Unnamed then arrives, defeats Heukgeol without killing him, and leads them to Mount Song.

At Shaolin, the monk’s master, Hong Dao—the Abbot and Dharma King—reveals that Taekyung is the Master of Morning Star. A new Morning Star appeared in the north when Taekyung awakened in the Murim, and its growing light contrasts with the dark, unknowable calamity Hong foresees. Jeok identifies Dark Heaven as the force behind the Blade of Flowers and the Head Elder’s restricted faction. Hong orders Jeok to remain beside Taekyung while Shaolin prepares for the coming disaster.

Meanwhile, Namgung Ryong orders the Hidden Thread to investigate Taekyung. After a fifteen-day forced march, Jeok and Taekyung reach Mount Jiuhua. Jeok begins six months of extreme training, binding Taekyung to four enormous iron balls and suppressing his abilities with the Fire King’s Special Restriction Pill. Taekyung is repeatedly blasted from the summit and must climb back without internal energy. After ten days, he completes the first quest, levels up, and receives 30 Bonus Points. Jeok begins the next stage with an iron vest and a shorter time limit, intending to train him even more harshly because his own time is limited.

## Continuity

- Jeok Cheongang and Jin Taekyung are training at Mount Jiuhua in Anhui for six months.
- Unnamed is Hong Dao’s young Shaolin disciple in practice: naturally timid but violently powerful when angered. He uses Ten-Thousand-Year Cold Iron prayer beads and Arhat Fist.
- Hong Dao is Shaolin’s Abbot and the Murim’s Dharma King, Jeok’s old friend, and Unnamed’s master.
- Hong Dao identifies Taekyung as the Morning Star that rose when he awakened in the Murim. He foresees an unknowable calamity as the heavenly patterns become distorted.
- Dark Heaven manipulated the Blade of Flowers for decades and placed restrictions on the surviving faction of the Head Elder.
- Namgung Ryong has ordered the Namgung family’s Hidden Thread and Lesser Threads to investigate Taekyung.
- Taekyung continuously wears four two-hundred-geun iron balls linked by Ten-Thousand-Year Cold Iron chains.
- The Fire King’s Special Restriction Pill suppresses internal energy and reduces Strength, Stamina, and Agility by 100 each for one week.
- Taekyung completed the first mountain-climbing quest after ten days, gained a level, and received 30 Bonus Points. The repeat quest now includes an iron vest and a half-shichen time limit.
- Jeok Cheongang has suffered sudden weakness and believes he has little time to teach Taekyung.
- Jin Mukyung remains isolated, practicing ten thousand sword strikes without internal energy.
- Taekyung and Cheongpung still intend to attend the Star-Array Grand Banquet in one year.

## Translation Decisions

- Retain Luoyang, Mount Song, Mount Jiuhua, Anhui, Shaolin, Jeok Cheongang, Jin Taekyung, Hong Dao, Unnamed, Heukgeol, and Dark Heaven.
- Use Dongcheon Sect for 동천파 and Dongcheon Gang for the source variant 동천방.
- Use Hidden Thread for 비선 and Lesser Threads for 소선.
- Use Morning Star for 신성 and Master of Morning Star for 신성의 주인.
- Use Green Jade Buddha Staff for 녹옥불장 and heavenly patterns for 천기.
- Use Arhat Fist, Ten-Thousand-Year Cold Iron, Pressure-Point Strike, and Sleep Acupoint.
- Use Fire King’s Special Restriction Pill for 화왕 특제 금제단.
- Preserve the quest-title distinction: Fire King’s Inferno Training-1 for 화왕의 불지옥 수련-1 and Fire King’s Hellfire Training-1 for 화왕의 지옥불 수련-1.

## Durable state

{
  "active_continuity": [
    "Taekyung and Jeok Cheongang have reached Mount Jiuhua in Anhui for six months of extreme training.",
    "Taekyung wears four two-hundred-geun iron balls continuously; their chains are made from Ten-Thousand-Year Cold Iron.",
    "Fire King's Special Restriction Pill suppresses internal energy and reduces Taekyung's Strength, Stamina, and Agility by 100 each for one week.",
    "Taekyung completed the first mountain-climbing Quest after ten days, gained a level, and received 30 Bonus Points.",
    "Jeok has prepared an iron vest for the next stage, shortened the time limit to half a shichen, and made the Quest repeatable.",
    "Jeok intends to train Taekyung more harshly because he has limited time to teach him.",
    "Jin Mukyung remains isolated in an unlit training cave, practicing ten thousand sword strikes without internal energy.",
    "Hong Dao is the Abbot of Shaolin and the Murim's Dharma King, master of Unnamed, and an old friend of Jeok Cheongang.",
    "Hong Dao identifies Taekyung as the Morning Star and foresees an unknowable calamity as the heavenly patterns become distorted.",
    "Dark Heaven manipulated the Blade of Flowers for decades and restricted the Head Elder's surviving faction.",
    "Namgung Ryong ordered the Namgung family's intelligence network to investigate Taekyung.",
    "Taekyung and Cheongpung intend to attend the Star-Array Grand Banquet in one year.",
    "Jeok Cheongang has suffered sudden weakness and believes he has little time."
  ],
  "continuity_sources": [
    233,
    234
  ],
  "open_questions": [
    "What is causing Jeok Cheongang's sudden weakness, and how much time does he have?",
    "Why has Namgung Ryong committed the family's intelligence network to investigating Taekyung?",
    "What important matter does Jin Wikyung need to discuss privately with Jeok Cheongang?",
    "Did Mae Jonghak actually grant Cheongpung permission to become Jeok's Disciple, and where is Mae now?",
    "Will Baek Museong escort Cheongpung to Huashan or search the Central Plains for Mae Jonghak?",
    "Will Jin Mukyung eventually attend the Star-Array Grand Banquet?",
    "What is the unknowable calamity approaching as the heavenly patterns become distorted?",
    "What does Dark Heaven intend, and how is it connected to the approaching calamity?"
  ],
  "safe_through": 234,
  "temporary_decisions": [
    "Use Hidden Thread for 비선 and Lesser Threads for 소선.",
    "Use Huangshan Sect for 황산파 and Mountain Lord for 산주.",
    "Use Namgung Ryong for 남궁룡 and Namgung for 남궁.",
    "Use concealment technique for 은형술.",
    "Use Pressure-Point Strike for 점혈 and Sleep Acupoint for 수혈.",
    "Use Heaven-grade for 천급.",
    "Use Fire King's Special Restriction Pill for 화왕 특제 금제단.",
    "Preserve the source's quest-title variants: 화왕의 불지옥 수련-1 is Fire King's Inferno Training-1, while 화왕의 지옥불 수련-1 is Fire King's Hellfire Training-1."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 230

# Chapter 230

Luoyang, the thousand-year-old capital.

This historic city, whose legacy stretched back thousands of years, was one of the foremost centers of commerce, literature, and art under heaven.

Even in the vast province of Henan, Luoyang was unrivaled in size, so wherever one went, the streets were always packed with people.

The same was true of a small inn on the outskirts of Luoyang.

“Two bowls of huimian noodles![^1]”

“Yes, yes! Coming right up!”

“Three more bottles of baijiu!”

“Right away!”

Merchants who had just finished a long journey clinked their cups from midday onward. A group of scholars engaged in heated debate. Even singers in shabby clothes whose circumstances looked anything but prosperous.

And then there were the people who could never be absent, no matter where one went.

Martial artists.

Crash!

The inn’s door exploded into splinters, and five or six swordsmen poured inside.

The one-eyed man leading them shouted without hesitation.

“Get them!”

His shout was directed toward a secluded corner of the inn.

A group of fierce-looking men had been guzzling strong liquor from a large jar. They overturned their table and rose to their feet.

“Damn it, the Dongcheon Sect?”

“Kill them!”

Clang! Clang-clang!

With a cacophony of noise, more than a dozen martial artists drew their weapons and clashed.

Blades tangled and broke apart, throwing sparks into the air. Tables split, and the odds and ends on them went flying in every direction.

“R-run!”

“It’s the Dongcheon Sect! The dark-path factions are fighting!”

The Murim was not made up solely of righteous heroes.

The orthodox faction, the unorthodox faction, and dark-path figures coexisted, while several thousand li away[^2] stood the Demonic Cult, filled with fiends and monsters.

[^2]: A *li* is a traditional East Asian unit of distance, commonly approximated as one-third of a mile.

Among them, the Dongcheon Sect was a dark-path faction that ruled Luoyang’s nights.

“…I’m ruined!”

The innkeeper, who had been cheerfully taking orders, collapsed onto the floor.

The Dongcheon Sect was not just some common gang of ruffians. Despite being a dark-path faction, it had a deep-rooted history stretching back more than fifty years and strong connections within the government.

If he reported this incident for no reason, they would tear him to pieces.

*Please, just don’t let anyone die.*

The innkeeper’s desperate wish collapsed the very next moment.

Slash!

“Grrrk.”

With a chilling sound, one of the men clutched his throat and fell.

He was one of the dark-path swordsmen who had recently gotten into a minor dispute with the Dongcheon Sect.

“Gungsu!”

“You goddamn bastards!”

The swordsmen, driven mad by their comrade’s death, charged at the enemy with their weapons raised.

But in a fight between evenly matched dark-path swordsmen, nothing mattered more than numbers.

“One of them’s down!”

“Beat the rest to death!”

The Dongcheon Sect’s swordsmen were experienced and ruthless. They struck at every opening, stabbing and cutting without mercy. Blood sprayed every time their blades flashed.

Swish-swish-swish! Thud!

“Gaaaaah!”

“Guh!”

“P-please, spare me!”

At the last survivor’s plea, the one-eyed man burst into laughter. He was a lower-ranking officer of the Dongcheon Sect.

“What? Spare you?”

“Please, just this once. If you let me off, I’ll never—”

“You should’ve known who you were messing with.”

Thunk!

A dagger shot from his sleeve and buried itself in the last swordsman’s forehead.

“Gueugh.”

Thump!

With a grotesque groan, the corpse toppled backward like a rotten old tree.

“You’ve got no pride at all. And you call yourself a dark-path man.”

The one-eyed man retrieved the dagger from the corpse’s forehead and crooked a finger at his underlings.

“Clean this up.”

“Yes, sir!”

With a vigorous reply, the swordsmen gathered the bodies and piled them together. The peaceful inn had long since become a sea of blood.

Step. Step. Tap.

Blocking the wrecked entrance, the one-eyed man swept his gaze over the terrified innkeeper and guests.

“Some of you know who I am, and some of you don’t. So I’ll trouble myself to tell you again.”

In the suffocating silence, everyone froze beneath the cold, murderous gleam in his eyes.

His harsh voice continued, as though he had swallowed iron filings.

“I am the lone beast of the mighty Dongcheon Gang, Heukgeol[^3]—”

[^3]: *Heukgeol* is a sobriquet meaning “Black Hero.”

Smack! Boom!

Startled by what had happened so suddenly, the people inside the inn blinked.

The lone beast of the Dongcheon Gang, Heukgeol, who had been blocking the entrance like Mount Tai, was nowhere to be seen. In his place stood a short old man.

“You rotten son of a bitch. What are you doing blocking the entrance?”

“…”

An invisible tremor swept through the inn.

Only then did the guests notice Heukgeol embedded in one of the walls. Their eyes widened.

*Gasp!*

*A martial artist!*

*He’s a master. An incredibly powerful one!*

While everyone was still reeling in shock, a young man who had entered behind the old man spoke with an incredulous expression.

“Still, was it really necessary to beat him like that? What if he dies?”

“Who cares whether some dark-path piece of garbage lives or dies?”

The old man answered gruffly and jerked his chin toward the inn, which had become a sea of blood.

More precisely, he was pointing at the Dongcheon Sect’s swordsmen, who were gathering the corpses and severed limbs.

They stared at the old man with vacant expressions.

“See? Can’t you tell? That’s the kind of people they are. There’s nothing in their heads, so whenever they meet, all they can do is swing their swords at each other.”

“Wow. They really deserve to die.”

“Right?”

“Yes. Shall we eat now?”

“Order the drinks first. I’ve inhaled so much dust that my throat’s scratchy.”

“Got it.”

The young man answered brightly and hurried over to the innkeeper.

“You have rooms, right?”

“Y-yes?”

The innkeeper, who was only half-conscious, answered automatically.

“Of course, sir.”

“Then give us the best room you have, and three bottles of baijiu. As for the food…”

The old man, who had already claimed a table, shouted from behind the young man.

“Crisp-roasted duck and huimian! You have to eat huimian when you come to Luoyang.”

“Sir, you heard him, right?”

“Yes, sir.”

“How much will that all be?”

That was why habits were so frightening.

The innkeeper instinctively finished calculating the entire bill and was just about to name the price when—

“You crazy bastard!”

“Fuck! Get him!”

They were not called dark-path figures for nothing.

They were mayfly lives, born in the back alleys and dying in the back alleys.

Armed with their innate simplicity and ferocity, the Dongcheon Sect’s low-ranking swordsmen rolled their eyes back and charged at the young man.

“Die!”

The bald man at the front let out a thunderous shout and swung a rough-looking broad-bladed saber.

Its blade, red with rust, came down toward the crown of the young man’s head.

Or rather, that was what it was about to do.

Whoosh! Thud!

With a chilling sound, the bald man’s body crumpled. His jaw had been shattered, and he was already unconscious.

The sword slipped from his limp hand.

Clunk. Clatter.

“I thought hair was the only thing you were missing. Turns out you’re useless at fighting, too.”

The young man muttered without much interest and turned back to the innkeeper.

“So how much did you say?”

“…”

“…”

The atmosphere inside the inn, which had already been frozen solid, became even more rigid.

As countless people watched with their eyes bulging, the young man paid the bill and even collected his change.

He was walking toward the table where the old man sat when he suddenly stopped.

“Hey.”

The Dongcheon Sect’s swordsmen, who had been frozen like statues beneath his gaze, flinched.

“Yes, sir?”

“Were you talking to us?”

The young man nodded.

“Yeah. What are you going to do?”

“W-what do you mean?”

“That thing in your hand. If you’re planning to swing it, swing it quickly. Otherwise, put it away. It’s ugly.”

Shk-shk-shk!

The swordsmen sheathed their weapons with lightning speed.

“Now collect the bodies and your friends. Move.”

“Yes, sir! Moving!”

“Since you’re at it, clean up the mess you made, too.”

With the call-and-response of men fighting for their lives, the swordsmen moved in perfect order.

They removed the corpses, the bald man, and finally the one-eyed man embedded in the wall. Then they swallowed nervously and waited for their next order.

“Why are you standing there gawking? Get the hell out.”

“Th-thank you!”

That was precisely the one thing they had been praying to hear.

Afraid they might be stopped, they hurried out of the inn. Words like arrows followed them from behind.

“If you show your faces here one more time, you die. Remember that.”

“Yes, sir!”

“Yeah, take care.”

A suffocating silence filled the inn.

As the young man walked toward the old man’s table beneath the horrified gazes of everyone present, he suddenly drew in a sharp breath.

“Gasp!”

Had the Dongcheon Sect attacked again?

The people who had been watching his every move were startled as well and looked around.

But the young man’s gaze was fixed on only one thing: the roast duck that had appeared on the table.

“H-how could you?”

His eyes were wide, and his pupils trembled as though an earthquake had struck.

After a brief silence, the young man suddenly shouted,

“How could you eat both legs by yourself?!”

“…”

* * *

Seven days and nights.

That was how long it had taken to get from Taiyuan to Luoyang.

Even riding a horse at full speed would have taken ten days to cover that distance, so there was no point explaining what the journey had been like.

The most important fact was that I had not complained even once.

But still…

“This isn’t right!”

I was genuinely furious.

He had eaten both legs! And after I’d finally gotten a proper meal for the first time in a week!

He had even left me with only one wing.

“Even dark-path bastards don’t do this!”

I continued shoving whatever food I could grab into my mouth while venting my outrage. Across from me, Jeok Cheongang looked utterly dumbfounded.

“Look at this ill-mannered brat. You’re shouting at this old man over something so trivial? What? Dark-path figures?”

“Am I wrong? Even the Demonic Cult Leader would eat only one duck leg.”

“You little—”

Whoosh!

A gentle heat began to rise from Jeok Cheongang’s palm when a gruff voice suddenly cut in.

“Hey, let me ask you something.”

A hulking man entered the inn with heavy footsteps. His face was covered entirely in scars.

Behind him came dozens of dark-path swordsmen with equally menacing faces.

*His face alone is rated 18+.*

The one-eyed man Jeok Cheongang had dealt with earlier could be considered fierce-looking in his own right, but compared to this giant, he looked like a model prisoner.

*Does everyone around here make a living off their faces?*

Well, at least it made them easy to identify.

Jeok Cheongang did not even bother looking at them, so I answered in his place.

“Yeah, that’s us.”

“I heard some very interesting news, but…”

Confusion passed over the giant’s face.

“What?”

“You haven’t even asked yet.”

“It’s obvious. The interesting news you heard was probably that some old man and a fresh-faced young guy showed up and beat a bunch of your lackeys half to death. Something like that, right?”

“…”

“Yeah, I know. Come on in. And bring the friends you brought along, just in case. They can all attack at once.”

The result had been entirely predictable.

Whether the men I had let go had called them, or someone among the onlookers had informed their gang, it did not really matter.

*I can just beat them down as they come.*

The difference in strength was overwhelming.

If they were at this level, the result would be the same whether ten or a hundred of them came rushing in. There was no need to kill them. I could simply brush them away like flies.

“Not coming? Then I’ll come to you.”

“You little bastard!”

Still, the man who had come this time had some sense.

Perhaps sensing something ominous, the giant subtly backed away and waved his hand.

“Get him!”

Schliing.

The moment dozens of weapons began to emerge from their sheaths—

“Amitabha, m-may we pass through for a moment?”

[^1]: Huimian is a famous Henan noodle dish made from broad, hand-pulled noodles served in a rich broth.
## Chapter artifact 231

# Chapter 231

“Amitabha. Excuse me, but may I pass through for a moment?”

The person who appeared alongside that timid voice was a young monk wearing a shabby robe.

Holding a large strand of prayer beads in one hand, he bowed repeatedly as he squeezed his way between the dark-path swordsmen.

“Then, please excuse me. Amitabha. Amitabha…”

“Uh-oh. Look at this.”

“Uhhh?”

The swordsmen were bewildered by the monk’s fearless behavior, which had come out of nowhere.

Several of them hurriedly pulled themselves together and tried to stop him, only to be pushed aside helplessly.

“W-what the hell is this?”

“Gasp. Where does he get that kind of strength…?”

Skrrt! Thump!

It made no difference when they charged him. No one could stop him.

I realized that an incredible amount of muscle was hidden beneath the monk’s old, baggy robes.

Massive forearms and bulging veins. At first glance, he looked like a man of average build, but those were compact, combat-ready muscles.

*Damn, look at those muscles. That’s insane.*

At that point, he looked like he should be wearing Under Armour instead of a monk’s robe.

While I admired him in silence, the monk passed through the dozens of dark-path swordsmen and wiped the sweat from his brow.

His face was filled with tension.

“Phew…”

The hulking man wasn’t going to stand there and watch.

His face had flushed red, and his eyebrows kept twitching.

I waved at him as he stared back and forth between the monk and me, clearly debating what to do.

“Hey, take your time. I’ll wait.”

“…How considerate of you.”

Crack.

The hulking man ground his teeth as he stepped in front of the monk.

“Who are you?”

“This poor monk is…”

“Never mind.”

His sharp gaze swept over the monk from head to toe.

“You’re a monk?”

“Of course.”

“You don’t even have a precept seal on your forehead.”

A bead of sweat ran down the monk’s forehead.

“My practice is still too shallow, so I have yet to receive one.”

“Practice, huh? What’s your Dharma name?”

“I have not received one of those, either.”

“So you’re a monk with neither a precept seal nor a Dharma name…”

The hulking man muttered under his breath, then gave a derisive laugh and asked his subordinates,

“Judging by his appearance, he’s clearly one of us. Don’t you think?”

“Yes, sir!”

“He looks like he’d be good at the job. We should take him in as the youngest member.”

“Right?”

The hulking man laughed loudly, then suddenly hardened his expression and glared at the monk.

“Where did you come from?”

“…I’m afraid I don’t understand the question.”

“I know all about you, you bastard. I asked where you came from. The Poison Dragon Sect? Or the Black Blood Sect?”

“T-the Poison Dragon Sect and the Black Blood Sect? This poor monk is from Shaolin.”

“What? Shaolin? Shaolin Temple on Mount Song?”

“Yes.”

Shaolin Temple?

This situation was getting interesting.

Even Jeok Cheongang, who had been ignoring everything behind him, turned around to watch.

“Old Master, he says he’s from Shaolin Temple.”

“Be quiet. I’m thinking about how to straighten out this rude brat of yours.”

“…”

That wasn’t good news.

My expression probably looked a lot like the monk’s.

His face had darkened as he stared at the hulking man, who burst into booming laughter.

“Ha-ha-ha-ha! Shaolin Temple? You say you’re from Shaolin Temple?”

“B-benefactor, why are you laughing?”

“Benefactor, my ass. What mangy dog bone did you crawl out from under to run your mouth in front of me?”

Boom!

The hulking man’s fist shattered a solid section of the wall.

Unlike his subordinates, who were Third Rate at best, he possessed enough martial prowess to pass himself off as a Peak master wherever he went.

Though he had barely entered the realm.

“You little bastard… You think our Dongcheon Sect is a joke? Do I look that stupid to you?”

“Benefactor, you appear agitated. Please calm down. Settle your heart.”

“Calm down, my ass!”

Boom!

The remaining rubble came crashing down.

The innkeeper, who was watching the situation from behind, had probably felt his heart collapse along with it.

“You have neither the precept seal that should obviously be stamped on your forehead nor a Dharma name, and you look like a fine dark-path thug, yet you claim to be a monk? You little shit. You might as well say that the Abbot of Shaolin is your master!”

“Gasp. How did you know?”

The young monk opened his eyes wide in surprise.

That was the last straw for the hulking man’s patience.

“You little son of a—!”

Whoosh!

A mace covered in sharp steel spikes shot toward the monk. It traced a clean, practiced arc, the attack of an experienced First Rate master.

The monk sucked in a startled breath and raised the prayer beads in his hand.

At that instant, screams erupted from the crowd watching the situation outside the inn.

“Eek!”

“It’s dangerous!”

But what they feared did not happen.

Clang!

With a sharp metallic ring, something came raining down.

The small, pointed objects were, astonishingly, the steel spikes that had been protruding from the mace.

“…Huh?”

The hulking man stared at his mace in confusion.

Then the young monk shouted in a terrified voice,

“Benefactor, you started this!”

“W-wait a minute!”

But the situation was already moving in an unexpected direction.

Rattle-rattle-rattle!

The prayer beads, large enough to look almost absurd, wrapped around the monk’s entire arm.

A strangely familiar sheen gleamed from the beads threaded between his fingers.

Wait a second. Could that be…

*Ten-Thousand-Year Cold Iron?*

The instant that realization flashed through my mind, a terrifying sound rang out.

Crack! Crunch!

The single punch that shattered the mace drove straight into the hulking man’s side.

“Guh!”

Blood poured from his mouth, which had fallen open from the pain.

“W-wait a minute!”

The hulking man cried out desperately, but it was a futile shout that never reached his opponent.

The young monk, his face already deathly pale, squeezed his eyes shut and shouted,

“Amitabha!”

Thud!

“Namu!”

Crack!

“Avalokiteshvara!”

Crunch!

“Amitabha, Amitabha, Amitabhaaa!”

Bam-bam-bam-bam-bam!

He hit him, broke him, then struck the places he had already hit again.

Every time the gleaming prayer beads shot forward, blood sprayed into the air.

Watching the scene, I muttered like I was groaning in pain.

“Oh, shit…”

That was the strongest reaction I could manage.

I had expected the monk to win from the moment he appeared, but I had never imagined he would be this insane.

“T-that…”

Jeok Cheongang had risen from his seat without me noticing. His mouth hung open.

“The Arhat Fist!”

“The Arhats? You mean Shaolin’s Hundred and Eight Arhats?”

“Y-yes. That is definitely Shaolin martial arts.”

“…That?”

I turned my head again.

The young monk’s eyes were now half-rolled back as he delivered a final finishing blow to the fallen hulking man.

“Gate, gate, paragateeek!”

Bam-bam-bam!

The scene was covered in brutal violence and blood. I wiped the blood from my cheek and barely managed to speak.

“…Old Master.”

“Speak.”

“Is that really Shaolin martial arts?”

“…Technically.”

“Then why don’t I feel even a trace of the Buddha’s compassion or anything like that?”

After a brief pause, Jeok Cheongang gave a short answer.

“At least he didn’t kill him.”

“…”

At this point, killing him seemed like it might actually be kinder.

But I had to swallow those words before they reached my throat.

Clink, clink.

The prayer beads swung and rattled with every step.

A robe drenched in blood and a pair of unsteady eyes approached me.

“Um, excuse me.”

“Yes?”

“Forgive me, but may I ask your name, benefactor?”

“W-why?”

My voice trembled before I could stop it.

The young murderer—no, monk—approached me with timid steps.

“Could you perhaps be someone from the Jin family…?”

“I’m sorry. You have me confused with someone else.”

“That is Jin Taekyung.”

Jeok Cheongang interrupted, and I immediately changed my answer.

“That’s right. I was just joking around. I didn’t offend you, did I?”

“Amitabha. How could I be offended?”

Fortunately, he didn’t seem upset.

Unlike me, who kept glancing uneasily at the prayer beads, he wore a joyful smile around his mouth.

If there hadn’t been a drop of blood splashed beneath his chin, I might have thought, *So this is the smile of a Buddha.*

“But why were you looking for me?”

“This poor monk was ordered to bring the Master of Morning Star.”

*The master of what?*

Before I could ask again, Jeok Cheongang abruptly spoke.

“Do you know Hong Dao?”

“Yes. He is my master.”

“…Hah. That damned monk is as uncanny as ever. He can still see a thousand li without leaving his seat.”

“Then you must be the Fire King, Great Hero Jeok Cheongang.”

“Did your master tell you that, too?”

The young monk silently lowered his head, and Jeok Cheongang let out a quiet laugh.

“Then there’s no need for a long explanation. Lead us to Hong Dao.”

“Yes.”

As the Yama disguised as a monk took the lead, the crowd parted like the Red Sea.

While everyone was distracted by the commotion, I asked Jeok Cheongang in a low voice,

“Old Master, who is Hong Dao?”

“The Abbot of Shaolin.”

That alone was surprising, but Jeok Cheongang wasn’t finished.

“In the Murim, they call him the Dharma King.”

“…”

* * *

Unnamed.

That was the Dharma name of the young monk who introduced himself as the Disciple of Dharma King Hong Dao.

Though, technically, it could hardly be called a Dharma name.

The word itself meant that he had no name at all.

“He’s still the same even in his old age. To give his Disciple a Dharma name like that…”

When Jeok Cheongang clicked his tongue, Unnamed gave an embarrassed smile.

“My master gave it to me, so it is both my name and my Dharma name.”

“From what this old man can tell, you don’t seem to be a formally accepted Disciple. You have no regrets about that?”

“Isn’t it all Heaven’s will?”

Unnamed pointed toward the sky and smiled brightly.

Jeok Cheongang shook his head.

“Even when he chooses a Disciple, he really… What should I say?”

After a brief hesitation, Jeok Cheongang continued,

“He chose a peculiar one.”

“Hehe. Amitabha. Thank you.”

“…”

“…”

*Don’t laugh. That wasn’t a compliment. And stop saying Amitabha.*

Even now, whenever I closed my eyes, I could vividly see Unnamed covered in blood.

With his smiling face, he looked no different from a living Buddha. But whenever he slipped the beads between his fingers, he turned a ten-meter radius into a living hell.

*This guy is the scariest of them all.*

From what I had heard during the half day we’d traveled together, he was so naturally introverted that once he snapped, he couldn’t control himself.

Jeok Cheongang tilted his head several times before giving a cursory nod.

But I had a different opinion.

I even knew his exact diagnosis.

*Anger-management disorder.*

That made him a walking time bomb.

That was also why I had been trying to travel behind Unnamed whenever possible.

A Peak master with anger-management disorder could strangle me with those Ten-Thousand-Year Cold Iron prayer beads.

*No. Absolutely not. I refuse to be strangled with prayer beads…*

Fortunately, it didn’t take long to get from Luoyang to Mount Song.

The two places were geographically close, and the roads had been well maintained because so many pilgrims visited Shaolin Temple.

As we reached the foot of Mount Song, wooden buildings began to appear in the distance.

“Have we arrived?”

Jeok Cheongang shook his head at my question.

“Not yet. We have to climb halfway up Shaoshi Peak. Visitors without a specific purpose are only allowed to remain at the Guest Reception Hall.”

“You know a lot about this place. Have you come here often?”

“I’ve heard plenty about it.”

“Oh.”

Well, if the Abbot of Shaolin was his friend, that much was probably only natural.

Jeok Cheongang dismounted and began climbing Shaoshi Peak. After a moment, he spoke.

“That lazy habit of yours hasn’t changed. Do you still sleep five shichen a day?”[^1]

The next moment, an unexpected answer came from a broad, flat rock far above us.

It was a presence only a master of Jeok Cheongang’s caliber could have sensed.

“Hmm. Five shichen. There was a time when I could sleep that long.”

The voice sounded like the tolling of a bell in an ancient temple.

It was quiet but weighty, carrying a deep resonance.

“Being the Abbot of Shaolin is a heavy responsibility. I can’t sleep as much as I used to.”

“Is that so?”

“Of course. It’s a sense of responsibility that a carefree Fire Gate Sect Leader like you could never understand.”

Jeok Cheongang and Hong Dao spoke as casually as friends who had seen each other only yesterday.

“So how many shichen do you sleep?”

“Well, that is…”

Whoosh.

A black silhouette slowly descended from the broad, flat rock several dozen meters above us.

Very slowly, stepping on empty air as though it were solid ground, Dharma King Hong Dao landed and smiled like a child.

“I can only sleep about four shichen.”

“You lazy bastard.”

A smile appeared at the corners of Fire King Jeok Cheongang’s mouth.

[^1]: A *shichen* is a traditional Chinese time unit of approximately two hours.
## Chapter artifact 232

# Chapter 232

Unlike the short Jeok Cheongang, Dharma King Hong Dao was a remarkably tall old man.

His eyes were full of mischief, and his steps were brimming with energy as he climbed the mountain path.

*Where are we going, anyway?*

It was only natural to wonder when he ignored the well-maintained road and deliberately chose paths that looked as though no one had ever traveled them.

After walking for some time, Hong Dao finally stopped.

“Some humble guests have come to this precious place. I know it may be a burden, but don’t stand on ceremony. Come in.”

Jeok Cheongang stared blankly at the “precious place” before speaking.

“Did you get kicked out of Shaolin Temple or something?”

“Hm? Why?”

“Are you asking because you don’t know? What happened to your residence?”

Just as Jeok Cheongang had said, the place was surrounded by thick weeds and trees. It looked far too shabby to be the residence of the Abbot of Shaolin Temple and the Murim’s Dharma King.

“Tell me honestly. You got fired as Abbot of Shaolin, didn’t you?”

Seriously, what was he, a convenience-store part-timer?

Dumbfounded by Jeok Cheongang’s words, I asked,

“Can an Abbot even be fired?”

“Have you ever seen anyone so narrow-minded? They can depose an emperor through rebellion, so why couldn’t they do the same to an Abbot of Shaolin?”

“…”

When he put it that way, I didn’t have much to say.

Besides, I used to beat monsters for a living in the modern world. With demon kings and Gates running around in this world, it wasn’t impossible for the Abbot of Shaolin to be a temporary employee.

Hong Dao, who had been listening to our exchange, chuckled.

“Wherever I am becomes the Abbot’s quarters. Our Shaolin doesn’t bother with that sort of formalities. Isn’t that right, Disciple?”

Unnamed answered,

“He is currently staying here despite the repeated pleas of the Discipline Hall.”

“…”

Just like his friend, this old man was no pushover.

Hong Dao, however, only laughed heartily as he pulled out some kind of staff from inside his robes and waved it around.

“What can they do about it? They were the ones who gave the position of Abbot to someone who said he didn’t want it in the first place.”

The staff was ridiculously short. Its surface was so smooth, as though it had been coated in oil from the countless hands that had touched it, and a faint green light shimmered across it.

*And there’s some strange-looking stone set into it.*

In some ways, it resembled the staffs used by mages.

But there was something different about Hong Dao’s green staff. In addition to the marks left by time, it possessed a unique energy all its own.

*What is that?*

My question was answered the next moment.

“The Green Jade Buddha Staff. To think they entrusted a thousand-year-old Shaolin sacred treasure of such immense authority to a dirty monk like this. They must all have gone blind.”

Jeok Cheongang clicked his tongue.

“Shaolin is really going downhill.”

“It’s still much better than the Fire Gate Clan, which has only one Disciple to its name.”

“What did you say?”

“Your fiery temper hasn’t changed. I hope you are reborn as a good and calm person in your next life.”

“My next life? Why are you killing me already when I’m still perfectly healthy?”

“Oh, my. A corpse is talking. Amitabha.”

“Hong Dao, you dirty monk!”

I watched the two of them bicker as they entered the Buddha hall, then turned around.

Unnamed was looking at me with a faint smile.

“It seems both of them are happy to meet an old friend after such a long time.”

“...I can’t really figure out how they became friends.”

The eccentric Abbot of Shaolin and the foul-tempered Sect Leader of the Fire Gate Clan.

Even if their personalities were a decent match, they didn’t seem like the sort of pair who would become friends. Besides, wasn’t Jeok Cheongang a man who had committed countless acts of killing, something forbidden by Buddhism?

Unnamed seemed to ponder my dubious remark. Then he suddenly smacked his gleaming forehead.

“Ah, I remember now.”

“You startled me. I thought you were about to use Solar Fist… What do you remember?”

“What brought the two of them together. During the Great Faction War, my master was secretly eating meat and drinking alcohol. After Benefactor Jeok caught him, they became drinking buddies.”

“What?”

For a moment, I wondered if I had heard wrong.

“He was eating meat and drinking alcohol?”

“Yes.”

“Wasn’t he the Abbot of Shaolin even back then?”

“That is correct.”

*Oh, so the monks here eat meat. Well, I suppose they need to bulk up while training in martial arts, so that makes sense…*

“That is not the case. The Buddhist faith forbids killing. Livestock are no exception.”

“...?”

“...?”

Where had things gone wrong, and how?

I stared blankly at Unnamed for a while, unable to continue the conversation.

Then I looked at the muscles writhing beneath his loose robes and became certain.

*This bastard eats meat too.*

Just look at those muscles. That was not a physique he could have built on temple vegetable bibimbap alone.

He might have been able to develop them by roasting an entire pig whenever he felt bored and eating it with bibimbap—but even then, it would have to be beef-tartare bibimbap.

*It wasn’t Shaolin Temple. It was the Temple of Meat and Wine.*

Someone once said that nothing in the Murim could be predicted even an inch ahead. They had been absolutely right.

I shook my head and followed the two of them into the Buddha hall.



* * *



The interior of the Buddha hall was small and old, but it possessed an elegant, antique charm.

The floor was spotless, and statues of the Buddha, both large and small, stood throughout the hall.

Unnamed left for a moment, while Jeok Cheongang, Hong Dao, and I sat facing one another and emptied our teacups. The drink had been brewed from some kind of unknown herb. It was astringent and bitter.

“This is no way to treat an honored guest. What is this?”

“What do you think? Tea leaves I grew myself.”

“Tea leaves? You?”

“I was getting on in years, so I decided it was time to give up ‘grain tea’ too. That was decades ago.”

“…”

For someone who had supposedly given it up, he seemed to have drunk enough alcohol to last a lifetime.

I couldn’t bring myself to say that, so I merely tilted my teacup. Jeok Cheongang, however, dropped his jaw.

“Are you sick? Have you caught some terminal disease?”

“A terminal disease… It could be, or it might not be. I don’t know either.”

His answer was calm, but for some reason Jeok Cheongang’s face hardened.

“Does that mean…?”

“We’ll discuss that later.”

Hong Dao lightly waved his hand to cut him off, then turned to stare intently at me.

“Now, then… Are you the Master of Morning Star?”

The Master of Morning Star.

It was a term I had first heard from Unnamed only half a day earlier.

It seemed that rumors about a Morning Star appearing in the Murim had been passed around by gossip-loving busybodies.

*The rumor has already spread this far?*

The title Sleeping Dragon of Shanxi was rising in popularity by the day, but I hadn’t expected even the Abbot of Shaolin to know about it.

Having suddenly become world-class, I gave an awkward smile.

“That is too much praise. I’m not quite at that level yet.”

“You are more obtuse than you look.”

“Excuse me?”

“Did I not say that you were the Master of Morning Star?”

*Yes, but what does that mean?*

Seeing my bewildered expression, Hong Dao smiled faintly.

“Benefactor, do you know what a Morning Star is?”

“Uh, well… Don’t people usually call those who distinguish themselves Morning Stars?”

“And?”

“...A star?”

“You got it right.”

Hong Dao nodded and continued in a calm voice.

“I have observed the heavens for a very long time. Perhaps it was not an entirely futile pursuit, because I have learned to see and read the heavenly patterns to some extent.”

“The heavenly patterns…”

The events of the past half day suddenly flashed through my mind.

Unnamed had come looking for us at his master’s command, and the moment he saw me, he had called me the Master of Morning Star.

And what had Jeok Cheongang said? Ah, yes.

*What an uncanny dirty monk. He can still see a thousand li without leaving his seat.*

That meant he had guided us by reading the heavenly patterns, not by obtaining information through other people.

*If that’s true, he’s definitely more than some fake fortune-teller.*

No, he could even be called a prophet without exaggeration.

I sensed something unusual from Hong Dao and swallowed hard.

“So?”

“A Morning Star is like a firework in the night sky. It shines brightly, then gradually fades with time. But this time was different.”

Hong Dao pointed toward the door of the Buddha hall. He was indicating the distant north, beyond where Shanxi Province lay.

“One day, a new Morning Star rose in the north. And that Morning Star has yet to lose its light. No, its brilliance has only grown stronger with each passing day.”

“…”

“People often compare humans to stars. I believe that Morning Star is you.”

Whenever someone is born or dies after accomplishing something great, people rejoice or lament.

*A new star has risen. Or a great star has fallen.*

*But the Morning Star that appeared this time is supposed to be me?*

Interpreting Hong Dao’s words, it was clearly a good thing.

But still, I wasn’t sure what to make of it.

Just as I scratched the back of my head with a perplexed expression, one of Hong Dao’s words pierced my ears.

“That was four months ago.”

“...!”

My entire body tingled as though I had been struck by electricity.

My mouth went dry, and my heart began to pound. Only one thought spun around in my head.

*Four months ago?*

If it was then…

That was around the time I had first awakened in the Murim.

Hong Dao smiled warmly at me as I swallowed dryly.

“You seem to have an idea.”

“N-no, no, not at all.”

Jeok Cheongang, who had been listening silently, cut in with a look of disgust.

“It’s written all over your face, you idiot.”

“I-it really isn’t.”

“Oh? Shall I just rip out that tongue of yours?”

“W-why are you doing this?”

Damn it. My tongue kept getting twisted.

Hong Dao burst into laughter as I slowly edged my bottom away from Jeok Cheongang to avoid his sharp gaze.

“It seems the benefactor is in urgent need of the privy. You may leave now.”

“Go on—if you want me to shove you into the latrine.”

I looked back and forth between the two of them, then bolted for the door.

Behind me, I heard Hong Dao’s booming laughter and Jeok Cheongang’s shouts.



* * *



“Ha-ha! Ha-ha-ha!”

“What an ill-mannered brat. How dare he run off while his master is speaking…”

Hong Dao looked at the grumbling Jeok Cheongang.

“Is he the Disciple you took in recently?”

Jeok Cheongang flinched and hurriedly coughed.

“Ahem. Kheh-hem! He isn’t my Disciple. He kept begging me to teach him a thing or two, so I’m just looking after him for a while. Yes. That’s all.”

“Is that so?”

“Of course it is!”

“If that’s the case, then why are you shouting? You’ll anger the Buddhas.”

“Well, listen to the way this dirty monk talks.”

Ignoring Jeok Cheongang’s reaction, Hong Dao emptied his teacup in one gulp and frowned.

“Ugh, bitter. You should drink yours as well.”

“Drink this crap? Why would I eat something so bitter?”

“We need to empty the cups before we can pour the liquor.”

“What?”

“I have something prepared for a day like today.”

Hong Dao rose from his seat with a sly smile that was unbefitting of a monk and approached the Buddha statues standing in a row.

He lifted and moved the largest statue with ease, fiddled with something behind it, and soon pulled out a small earthenware jar.

“Snake liquor aged for thirty full years.”

“Snake liquor?”

“The Thousand-Year Poison Horned Snake. Have you heard of it?”

“The Thousand-Year Poison Horned Snake!”

Jeok Cheongang’s eyes lit up.

Jeok Cheongang hurriedly opened the tightly sealed jar. Sure enough, the snake inside was larger than a python, and a horn protruded from its triangular head.

On top of that, a poisonous aura strong enough to make the tip of Jeok Cheongang’s nose tingle poured from the jar. He clicked his tongue.

“Isn’t that a venomous creature with an incredibly deadly poison? Where did you catch it?”

Hong Dao gazed at the distant mountains.

“While I was out for a walk.”

“...You must have searched the entire mountain with the intention of making snake liquor in the first place. There’s a limit to how much of a dirty monk you can be. Now you’re killing things just so you can drink?”

“If you don’t like it, forget it. I’ll drink it alone.”

“Hmph.”

Jeok Cheongang glared pointedly at Hong Dao and muttered,

“But this thing’s poison must be no joke…”

“Indeed. A single drop of venom squeezed from a Thousand-Year Poison Horned Snake can kill a hundred cows.”

“It’s been sealed away for thirty years. At this point, it isn’t liquor anymore. It’s poison.”

“We only broke the seal for a moment, and already this much poisonous energy has spread through the air. What more is there to say?”

“Something this strong would kill even a decent master, wouldn’t it?”

“It’s madness. We must not drink it.”

Their gazes collided in midair. Then they spoke almost simultaneously.

“Then we have to drink it.”

“Of course. Absolutely.”

“Surely it won’t kill us.”

“Drink it. No matter what. I read the heavenly patterns, and today is not the day we die.”

Both men were over a hundred years old, but they were still unable to escape the simplicity and recklessness carved into the bones of every man.

Before long, they began passing the jar back and forth and guzzling down the liquor as though possessed.

Half a shichen[^1] later, early darkness settled over the mountain, and the jar was empty.

“Whew. The venom tingles on the tip of my tongue, and the flavor is incredible. The Scorching Yang Qi keeps it from getting close to me.”

Jeok Cheongang licked the very last drop from the jar.

Hong Dao stared at him with a frown.

Though they were both members of the Ten Kings, there was naturally a slight difference in their skill.

Hong Dao had lost out in the grappling technique they used to wrestle the jar away from each other, so he had not managed to drink even half of what it contained.

“Old man with nothing but strength. You certainly have a long life.”

“Did you hope I would die?”

“At the very least, I expected you to clutch your stomach and roll around.”

Jeok Cheongang, pleasantly drunk, burst into laughter.

“That’s what the heavenly patterns said, isn’t it? What can you do when Heaven has decided your lifespan?”

“The heavenly patterns…”

Hong Dao murmured the words quietly, then tossed out a single sentence.

“That was a lie.”

“Hm? What do you mean?”

“Exactly what I said. I’ve been gradually going blind for the past thirty years.”

“W-wait. Are you saying you can’t read the heavenly patterns anymore?”

Hong Dao silently nodded, and Jeok Cheongang’s heart sank.

“How did that happen? Is it because of your age?”

“At first, I thought so as well. But I was mistaken. I gave up the liquor I loved so much and secluded myself in the wilderness to calm my mind, yet nothing changed.”

“Then…”

“It means it isn’t because this old man’s mind has grown dull.”

Hong Dao sighed and raised his head.

Though the ceiling of the Buddha hall blocked his view, the profound gaze of the old monk seemed to pierce through it.

“The heavenly patterns are becoming distorted. Drawing closer, and moving faster.”

“...!”

“A Morning Star appeared amid all of that. Even in those disordered heavens, I could see its light clearly.”

Jeok Cheongang’s eyelids trembled.

“And?”

Hong Dao thought for a long moment, then shook his head.

“This is as much as I can say. Though the heavenly patterns are confused, they still retain their form, and the great trees rooted throughout the land will not be easily shaken. However…”

An unknowable light entered Hong Dao’s eyes.

The words that followed held the wisdom of a sage, something only someone who was both the current Abbot of Shaolin—the sect hailed as the Murim’s greatest pillar for a thousand years—and deeply versed in the study of the heavens could display.

“An unknowable calamity is approaching. Dark clouds gathering from somewhere will cover the sun and blanket the stars.”

A sky dyed in darkness, without a single ray of light.

Jeok Cheongang imagined the scene and let one word escape like a groan.

“Dark Heaven?”

“Dark Heaven. Yes, it will become just as you said…”

Jeok Cheongang hurriedly cut him off.

“No, that’s not what I meant. I just remembered something I heard from Jin Wikyung, the Lesser Family Head of the Jin Family of Taiyuan.”

“Jin Wikyung? I don’t know who that is, but are you saying he predicted this situation as well?”

“More accurately, it appeared before them. I saw it with my own eyes.”

Jeok Cheongang gave Hong Dao a detailed account of what had happened seven days and nights earlier, just before he left the Jin Family of Taiyuan.

He told him about the surviving remnants of the Head Elder’s faction, who were still alive despite the restrictions placed on them, and about everything that had happened up to that point. He also told him about the mysterious pill called the Temporary Strength Pill that he had taken from Pung Yang, the Red Wind Band Leader.

Jin Wikyung had passed all those facts to Jeok Cheongang, and Jeok Cheongang now passed them to Hong Dao.

“It was astonishing. The restrictions placed on those men were so complex that even I could not easily break them, and the effects of that Temporary Strength Pill were bizarrely powerful.”

“What a thing to happen.”

“The hidden force that manipulated the Blade of Flowers from behind for decades. They are Dark Heaven.”

“Ha…”

After the story ended, Hong Dao let out a low groan and fell into deep thought.

A long time passed before he finally opened his mouth.

“Leave immediately.”

“...!”

“It seems that the time has come for each of us to do what we must. I will prepare for the calamity with all my strength, and you…”

Jeok Cheongang gazed deeply at his old friend and finished the sentence.

“You must stay beside the Morning Star. So it doesn’t fade easily.”

Jeok Cheongang knew that protecting it was not the end of his task. He had to guard that light while making it shine even more brightly.

Having realized their respective duties, neither man hesitated any longer.

“I’ll be going.”

“I won’t see you far off. We’ll save the rest of our reunion for another time.”

Their farewell was long, but their meeting had been short.

Jeok Cheongang smiled at Hong Dao one last time, then strode out of the Buddha hall without hesitation.

Remembering the words he had not managed to finish saying.

*It was a short meeting, but I enjoyed it.*

Late that night, the young man and the old man left Mount Song and Shaoshi Peak.

Their journey continued until the sun rose and set again.

[^1]: A *shichen* is a traditional time unit of approximately two hours.
## Chapter artifact 233

# Chapter 233

The middle-aged man gazed down at the transparent blade.

His features were as sharp as a blade, and his lips were pressed tightly together. His hair, beginning to show strands of white here and there, was reflected on the blade’s surface.

It was only after some time that he finally opened his mouth.

“You’ve worked hard waiting.”

His low but powerful voice echoed throughout the spacious room. Yet there was no one to be seen anywhere his eyes reached.

The answer came from above the middle-aged man’s head—from the ceiling.

“It is my duty.”

The owner of the whisper was a person known as the Hidden Thread. The Hidden Thread had existed in the previous generation, and the generation before that. It had existed since the family was first established hundreds of years ago.

They had sworn absolute loyalty to one person alone—the Family Head—and, true to their name, they were hidden threads.

The countless pieces of information that flowed in along those threads could quietly be forgotten, or they could become weapons used to choke someone.

“Then, do you have any new information?”

“Yes. It is Heaven-grade.”

“Heaven-grade.”

The middle-aged man ran his fingers over the blade.

The information the Hidden Thread had delivered up to now was invariably confidential, but it was divided into Heaven, Earth, and Human grades according to its importance.

Heaven-grade was the highest of them all.

Even for a middle-aged man who had led his family for nearly twenty years, it was by no means something he encountered often.

“It’s been a long time. Is this the first since the Huangshan Sect?”

The Huangshan Sect was a prestigious great sect with a long history. Yet it was also a name that had slowly begun to fade from the memories of the people.

Survival of the fittest.

The Murim was a merciless world that did not look back at those who had been weeded out. The middle-aged man had weeded out the Huangshan Sect and feasted on their corpses.

“There should still be quite some time before their closed gates are opened.”

“The Huangshan Sect has already collapsed. Even if their gates are opened, they are beyond recovery.”

“Then?”

“The Mountain Lord has returned.”

At that brief answer, the fingertips that had been caressing the blade came to an abrupt stop.

“…Is that true?”

“Without a doubt.”

The Mountain Lord—the master of the mountain.

Some might tilt their heads and wonder what sort of nonsense that was. They might even scold him, asking how many mountains there were in the world and whether each one had its own master.

However, here in Anhui Province, the Mountain Lord referred to only one person.

“Fire King Jeok Cheongang…”

An unprecedented master who had faced a thousand martial artists alone.

Mount Jiuhua was his territory, as well as the sacred ground of the Fire Gate Clan, which had been passed down for hundreds of years.

On the day the Demonic Cultists set fire to Mount Jiuhua, an old man who had been growing old like any ordinary man became the Fire King.

The people of Anhui Province, who had protected their precious home thanks to him, began calling him the Mountain Lord out of respect.

“When and where did this information come from?”

“The report says he passed through the north gate two shichen[^1] ago.”

“What is his destination?”

“Mount Jiuhua.”

“I see.”

The middle-aged man nodded lightly, then suddenly felt that something was strange.

From the time he had become Family Head until now, the middle-aged man had received countless reports from the Hidden Thread and asked for his opinions, but the Hidden Thread had never once spoken with certainty.

This time was different.

Sensing his lord’s question, the Hidden Thread spoke first.

“He was accompanied by his Disciple. Going to his sect is only natural.”

“His Disciple?”

The middle-aged man frowned. The Fire Gate Clan was a sect built on a single-person succession. If the Fire King had a Disciple, there could only be one person.

Although it had happened nearly twenty years ago, he remembered everything related to the Fire King clearly.

“Did he come back for that vicious bastard?”

“The person you have in mind is not him. According to confirmed information, he died three months ago.”

“And he found a new Disciple?”

“Yes.”

The Hidden Thread’s emotionless voice continued.

“Jin Taekyung. He turned twenty-one this year and is a direct descendant of the Jin Family of Taiyuan.”

“I feel like I’m hearing both that name and that family for the first time.”

“He shares blood with the Blade of Flowers, who distinguished himself during the Great Faction War, and with the Heaven Shaking Sword, who has recently risen to prominence as one of the Ten Dragons and Phoenixes.”

“Ah, that Jin Family.”

“Yes.”

Fortunately, the two names that came from the Hidden Thread were familiar enough to the middle-aged man.

“Hm. So that’s how it is.”

The middle-aged man sank into deep thought, forgetting even that the Hidden Thread was there.

Jin Taekyung of the Jin Family of Taiyuan. The new Disciple of Fire King Jeok Cheongang. No matter how he thought about it, the name was unfamiliar.

But now he would have to become accustomed to it.

*The descendant of a frontier martial family was chosen by the Fire King.*

For the Fire King to accept a young man past the age of twenty as his new Disciple, there had to be some reason.

*It has to be one of two things. Either he has some leverage over the Fire King, or he possesses martial talent so extraordinary that his age and background are irrelevant.*

The more he thought about it, the more the pieces fell into place.

By the time the middle-aged man spoke again, a considerable amount of time had passed.

“Set all the Lesser Threads in motion.”

The Lesser Threads were the countless informants who operated beneath the Hidden Thread.

They gathered information from every corner of the world, which then flowed through the Hidden Thread before reaching the middle-aged man.

“All of them?”

Unlike before, a faint trace of surprise colored the Hidden Thread’s voice.

The middle-aged man’s order meant that most of the family’s intelligence-gathering power would be poured into a single person.

But the surprise lasted only a moment. Realizing his duty, the Hidden Thread hurriedly answered.

“Forgive my insolence.”

“It doesn’t matter. I’ll give you a month. Use every means necessary and find out everything about that Disciple.”

“Understood.”

“You’re going to be busy for a while.”

The Hidden Thread understood the meaning hidden in those words, and its presence vanished as though it had been wiped clean.

His concealment technique had reached the very pinnacle of Peak. He would spend the next fortnight with no time to breathe.

*I can’t sit around doing nothing either.*

The middle-aged man slowly rose from his seat.

Unlike his father, who had been a martial artist to the bone, he had inherited the blood of a leader.

Having led the family since he was the Lesser Family Head and solidified its position as a hegemon, the middle-aged man radiated authority from his entire bearing.

Step. Step. Step.

The middle-aged man crossed the spacious interior in long strides and threw open the door. A dozen or so guards surrounding the pavilion greeted him by dropping to one knee.

“We greet the Family Head!”

The middle-aged man nodded slightly. Every one of them was an outstanding Peak swordsman and a blood relative who shared the same lineage.

A massive group gathered beneath the surname Namgung, a towering tree rooted in the Murim.

“Gather the family. The weather is fine, so we should share a drink together.”

“Understood!”

The middle-aged man, Namgung Ryong, raised his head and gazed at the sky.

A boundless azure heaven, without a single cloud, stretched above him.



* * *



I spoke with the most serious expression in the world.

“I have a wish I’ve held on to for a long time.”

Jeok Cheongang answered in an equally solemn voice.

“This old man has a wish as well.”

“If it wouldn’t be too rude, may I speak first?”

“That would be plenty rude.”

“Then I’ll be rude this once.”

“Want to have an accident in your pants? Should I make you shit and piss yourself for the rest of your life, not just this once?”

“…”

If my mother had seen this, her heart would have broken.

I felt as though tears might fall from the injustice of it all, but I held them back and opened my mouth again.

“Please hear me out just once.”

“Fine. It’s obvious what you’re going to say, but I’ll hear you out once.”

I swallowed dryly and stated my wish.

“Could we stop at an inn just once?”

“That’s your wish?”

“Yes.”

“Then I’ll tell you this old man’s wish.”

Jeok Cheongang glared at me with terrifying eyes.

“Shut your mouth and follow me.”

“…Why?”

“Didn’t you say you wanted to train? We’re going to train, so why do you have so many complaints?”

“When did I say I didn’t want to train? I’m going to be buried in the mountains for half a year, so I’m saying we should eat our fill and wash up just once—just once—before that happens!”

My shout rang through the darkened mountains.

That was right. We were currently standing at the base of Mount Jiuhua in Anhui Province.

“It took seven days and nights to get from Shanxi Province to Henan, and another seven days and nights to get from Henan to Anhui. I haven’t even been able to sleep properly.”

At least he had let me sleep one shichen at a time before we reached Henan. But after we left Hong Dao’s residence, he had shown us absolutely no mercy.

We had run and run, chewing jerky without even stopping for meals.

“I wanted Shaolin Temple’s vegetable bibimbap!”

During the fifteen-day forced march, the only proper meal I had eaten was at the inn in Luoyang.

“And even then, you ate all the legs yourself! You left me one wing and nothing but dry breast meat!”

I had barely gotten to tear off a few pieces of meat when some sword-wielding dark-path figures showed up and ruined everything. Then the Under Armour monk appeared and took me to Shaolin Temple.

“I kept telling you that we should stop at an inn just once. What did you say? That we were almost there. You said we could rest once we got there!”

“And we did get there. Mount Jiuhua.”

Jeok Cheongang scratched inside his ear with a dirty little-finger nail, then blew away the earwax.

“Go on up and rest. Once we get there, you can eat your fill, wash, and sleep.”

“Even if I eat my fill, it’ll be jerky and fasting pills. Forget hot water—I’ll just get my fill of forest bathing. And you won’t let me sleep even half a shichen a day!”

“Ha-ha-ha!”

Jeok Cheongang laughed heartily, then abruptly stopped. At the same time, a chilling energy began to flow from his entire body.

“This is why I can’t stand youngsters with good instincts.”

“……!”

*Ed oppa… No, not that.*

A shiver ran down my spine.

A voice as cold as ice spilled from his lips.

“Yes, your guess is correct. I plan to let you sleep half a shichen a day and work you like a dog.”

“Gasp.”

“I’ll use fasting pills to squeeze every last drop of fat from your body. Then, for the next six months, I’ll make you train every single day at the most extreme level a human being can imagine.”

“Y-you’re a devil.”

“Did you just call this old man a demon? I suppose I’ll have to raise the intensity of your training.”

“N-no. This is a scam.”

“Why don’t you understand that by the time you realize it, it will already be too late?”

“Wait. I’ll just go to the privy for a moment.”

As I slowly backed away, the Fire King spread a wrinkled palm toward me.

“You can come whenever you want, but you can’t leave whenever you want.”

Whoosh!

An irresistible, unprecedented force transformed into ropes and bound my entire body.

For all my near-superhuman physical abilities and nearly a jiazi[^2] of internal energy, neither could do a thing.

I tried to resist somehow, but it was already too late. Following the movement of his hand, my body floated into the air.

“Seizing an Object Through Empty Space?”

“If you know what it is, come here.”

Whoosh!

The next moment, I shot toward Jeok Cheongang faster than an arrow. At the same time, one of his wrinkled fingers brushed against some spot on my neck.

A sharp sting of pain, followed by an ominous sound that pierced my ear.

Beep!



> **System**
>
> You have been struck by **Pressure-Point Strike**!
>
> Your **Sleep Acupoint** has been struck. You cannot resist sleep!
>
> 5 seconds, 4 seconds, 3 seconds, 2 seconds……



Sleep came rushing over me along with the System’s countdown.

As my consciousness blurred, Jeok Cheongang’s voice slowly faded into the distance.

“Today, I’ll make a special exception and let you sleep for two shichen.”

“…”

*Well, fuck. Thanks a lot.*

I couldn’t spit out the words circling the tip of my tongue before I fell asleep.



* * *



Snore. Snore.

“That young bastard has some serious strength.”

Jeok Cheongang clicked his tongue as he looked down at the peacefully sleeping Jin Taekyung.

Seizing an Object Through Empty Space and Pressure-Point Strike were not omnipotent. The amount of force required differed depending on the opponent.

It was a good thing he had known what kind of person this young man was. If he had been caught off guard and his technique had been countered, he would have been utterly humiliated.

“It feels like only yesterday that I first met him in Shanxi, yet he’s already reached this level… What a strange fellow.”

Just as Jeok Cheongang let out a fatigue-laced sigh, his vision suddenly blurred and the strength left his legs.

“Gasp!”

Thud.

He barely managed to regain his senses before grabbing hold of a nearby tree.

His heart pounded, and his mind snapped fully awake, as though someone had thrown a bucket of cold water over him while he slept.

“Th-this…”

Had he used too much strength all at once? If not, was it because his aged body could no longer withstand the arduous journey?

Jeok Cheongang bit his lip. Although his prime as a martial artist had passed, he was still a Supreme Peak master who had reached the pinnacle of martial arts.

*It wasn’t his body that had grown old. It was something else.*

*I need to hurry. I don’t have much time.*

Perhaps that was why his old friend Hong Dao had told him to leave immediately.

After steadying himself, Jeok Cheongang slung Jin Taekyung over his back. Though he was over a hundred years old, the young man’s large frame felt as light as a feather.

“Not yet. Not yet.”

He muttered the words in a voice that had suddenly grown old, then moved on.

Each step covered more than ten jang, and the scenery flashed past.

Before long, thick fog settled over the area and erased his trail.

[^1]: A *shichen* is a traditional time unit of approximately two hours.

[^2]: A *jiazi* is a traditional sixty-year cycle.
## Chapter artifact 234

# Chapter 234

Ding.

> **System**
>
> **Pressure-Point Strike** has worn off!
>
> You awaken from sleep!

I opened my eyes as the System notifications appeared.

The first things to enter my view were the rippling branches below, swaying in the night wind, and the stars scattered across the blackened sky. Against my back, I felt the cold, hard touch of rock.

*I’m outside.*

I had expected as much. Even a preschooler could have guessed that Jeok Cheongang wouldn’t lay me down on a soft goose-down bed.

Besides, my body was sturdy enough to sleep anywhere.

*Then why does my body feel so heavy?*

Was it because I had been pushing myself too hard lately?

System or not, apparently I was still human after all.

Maybe it was because of the fifteen-day forced march. My body felt heavy, as if I had an iron ball hanging from me…

Clank.

“Huh?”

Clank?

I turned my head toward the sound.

I saw manacles fastened tightly around both hands and ankles, with chains connecting them to iron balls.

“…They’re really iron balls.”

What the hell was this?

My brain stopped working for a few seconds. Who was I? Where was I?

And why were these ridiculous things locked onto my limbs?

The answer came quickly. It was an easier problem than one plus one.

“Fire King!”

It was at that exact moment that I shouted the words like a thunderclap.

Smack!

“Ah!”

“Look at this disrespectful little bastard.”

Jeok Cheongang, who had nailed me in the back of the head with a pebble, was approaching at a leisurely walk, his feet turned outward.

“How dare you toss around my epithet so casually in front of me? Am I your friend?”

I had been rolling around on the rock in pain, but I sprang to my feet.

Clank.

“What is this?”

“That? Iron balls.”

“I wasn’t asking because I didn’t know what they were.”

“Then why did you ask when you already knew?”

“……”

“From now on, these will be your arms and legs. They are training tools passed down through the Fire Gate Clan for generations, so treat them like your own children.”

I was a virgin bachelor who had never even been in a relationship, let alone married, and he was talking about children?

Dumbfounded, I grabbed the chains attached to the iron balls and pulled.

Rattle.

The sound of metal scraping filled the air, followed by a tremendous sense of weight.

They were heavy enough that even a decent First Rate martial artist wouldn’t be able to stand still while wearing them.

“These are training tools passed down through the sect for generations?”

“Did this old man not just say so?”

“How much do they weigh?”

“Not much. About two hundred geun?”[^1]

“……”

“Oh, of course, that’s not combined. Each one weighs two hundred geun.”

Two hundred geun came to 120 kilograms even by modern standards.

With such monstrous objects fastened to all four of my limbs, their total weight was…

*About five hundred kilograms. Half a ton.*

I thought it over carefully before opening my mouth.

“Have you gone senile?”

“……You really don’t hold anything back, do you?”

I had expected to get hit for saying that, but for some reason, Jeok Cheongang’s reaction stopped there.

He stared at me with a complicated expression for a moment before continuing.

“Regardless, you’ll live with those iron balls chained to you from now on. While training, of course, but also while sleeping and eating.”

“Hmm.”

“This is all part of your training.”

“You’re serious?”

“If you don’t believe me, quit. I won’t bother seeing you off.”

Jeok Cheongang turned around without hesitation, so I hurriedly called out to him.

“W-wait a moment!”

“What? I thought you didn’t want to do it.”

“No, but you can’t just leave before I’ve even answered.”

“So, what’s your answer?”

“Well…”

*Damn it. I’m having a serious internal conflict here.*

But once the initial shock of seeing the iron balls faded, my mind gradually settled.

*It’s not impossible.*

I had made it this far after narrowly escaping death dozens of times.

The world wasn’t easy. To receive a reward, you had to pay a corresponding price. That was true in the Murim and in the modern world.

Everyone—not just me—was living through a series of endless Quests.

And…

*If I were going to turn back over something like this, I wouldn’t have come all the way here.*

Compared to the fruits I would harvest in the future, this was a bargain.

After reaching my decision, I met Jeok Cheongang’s gaze.

“Fine. I’ll do it.”

“I didn’t hear you.”

“I said I’ll do it!”

“Ha-ha-ha! Good!”

A smile spread across Jeok Cheongang’s wrinkled lips.

*What a sly old man.*

He had acted as though he didn’t care either way, but I had known for a while that deep down, he wanted me.

“So what do I start with?”

“You want to start right away?”

“They say you should strike while the iron is hot. If I’m going to do it anyway, it’s better to start now.”

“You have a bold streak, I’ll give you that. But you need to eat first.”

“What? Why all of a sudden?”

“Do you think training means starving yourself? You need to have something in your stomach before you can accomplish anything worthwhile.”

I caught the object Jeok Cheongang pulled from inside his robe and tossed to me.

Under the faint moonlight, I peeled away the damp paper and found a fasting pill with a reddish cast.

“You should’ve given me jerky instead.”

“Stop complaining and eat it. It isn’t an ordinary fasting pill. It was made using a secret Fire Gate Clan method.”

“What does it do?”

“It’s superior in every way, but…”

“This stuff makes my stomach feel so bloated. These days, just looking at one kills my appetite.”

“It’s especially good for your virility.”

“Wow, my mouth’s watering just looking at it.”

“……”

“I’ll enjoy the meal!”

If it was good for virility, I had to eat it. Even if I had no immediate use for it, I had to eat it no matter what.

Thinking of the future, I chewed the fasting pill thoroughly and swallowed it.

Jeok Cheongang watched me intently before asking,

“Did you finish it?”

“Yes, Old Master.”

“What, you don’t feel anything?”

“I’m not sure. I think my sperm count may have gone up a little…”

Jeok Cheongang frowned at my answer and muttered,

“Strange. Perhaps the medicine lost its potency because it was made too long ago?”

“Huh?”

What the hell was he talking about?

I had just asked him that without thinking when—

Ding.

> **System**
>
> You have taken **Fire King’s Special Restriction Pill**.
>
> You feel full!
>
> **Agility** decreases by 100!
>
> **Strength** decreases by 100!
>
> **Stamina** decreases by 100!
>
> You cannot use **internal energy**!
>
> The effects will last for one week!

“…Huh?”

It happened without any warning.

As soon as the System notification appeared, strength drained from my arms and legs, and my breathing grew short.

Finally, the internal energy that had been flowing steadily through the lesser meridians throughout my body descended into my dantian. Then it became completely immobile, as though bound by something.

“Guh!”

Thud!

My strength vanished all at once, and the body that had somehow been supporting the weight of the iron balls sagged.

The half-ton weight pressing down on my entire body made my knees buckle.

“What the hell is this?”

“Heh-heh. The medicine is finally taking effect.”

I stared at Jeok Cheongang, who was letting out a sinister laugh, with my jaw hanging open.

“What the hell did you do, you crazy old man?”

“What did you call me? A crazy old man?”

“Gasp. No, that’s not what I meant.”

“Let’s see… For your first training session, that seems like the best choice.”

As soon as he finished speaking, his wrinkled palm opened toward me.

An immense flow of qi filled the air. The wind that had been blowing fiercely changed direction and began to whirl around him.

Then a flash of insight struck me.

*There’s a cliff below this, isn’t there?*

I hurriedly looked behind me. The view below the rock was dizzying.

If I fell from here with these insane iron balls attached to me…

“W-wait a moment!”

“What do you mean, wait? Didn’t you say it was better to strike while the iron was hot?”

“But that was—!”

“Too late.”

Fwoosh!

Compressed air burst from Jeok Cheongang’s palm. A blast of fist wind powerful enough to uproot rocks and trees transformed into the fist of a giant and hammered into me.

Against that powerful wind, even several hundred kilograms of iron balls were useless.

Boom!

*Ah, shit.*

The next moment, the ground vanished beneath my feet, and I was flung into the air.

Through my upside-down vision, I saw Jeok Cheongang waving at me with a broad grin.

“You have one shichen to get back up. If you’re even fifteen minutes late, you fail.”[^2]

Ding.

> **System**
>
> Quest **Fire King’s Inferno Training-1** has been created!
>
> You cannot refuse this Quest!

“This is such bullsh—!”

Before I could finish speaking, gravity bore down on my entire body.

As I plummeted like a streak of light, there was only one thing I could say.

“Aaaaaaaaaaaah!”

My terrified scream shook Mount Jiuhua, which lay submerged in darkness.



* * *



Splash—

Far below the sheer cliff, Jeok Cheongang let out a quiet laugh at the sound of water echoing up from below.

A memory from his youth had suddenly come to mind.

“Master! Save me!”

“I’m counting to three. Let go. Three.”

“Please! If I fall from here, your Disciple will die!”

“Two.”

“Master!”

“One.”



His Master had been merciless—harsh enough to seem excessive when inflicted on a child whose baby fuzz had yet to disappear.

But without such harsh instruction, neither the Fire Gate Clan of today nor Fire King Jeok Cheongang would exist.

*I’ll put you through what I went through… No, I’ll push you a little harder.*

Jin Taekyung didn’t know it, but Jeok Cheongang did.

There was no time to teach him everything gradually, one step at a time.

The heavenly patterns Hong Dao had foreseen told him as much, as did Jeok Cheongang’s current condition.

*Hold out until then. This old man will do his best, too.*

After staring down the mountain for some time with a profound look in his eyes, Jeok Cheongang suddenly muttered,

“…Perhaps I shouldn’t have put the iron balls on him.”

He had never imagined that the object meant to restrain criminals of the Fire Gate Clan would be used for something like this.



* * *



“Hngh. Hnnnngh!”

Grrrnk. Grrrnnngh.

With every step I took, the ground that had only just begun to thaw sank beneath me. Deep trenches formed in my wake.

But I was already used to it. Sweating profusely, I continued climbing the steep mountain path.

“Huff. Huff.”

Ding.

> **System**
>
> Extreme Training!
>
> Endless effort never betrays you!
>
> **Strength**, **Stamina**, and **Agility** have increased by 1 each!
>
> **Muscles and Bones** and **Sinews and Meridians** have increased by 2 each!

Even a drizzle will soak you through eventually, so these stat increases, though small, helped more than you might think.

*If only I didn’t have these fucking iron balls! If only it weren’t for that damn restriction pill!*

If either one had been absent, I would have completed the Quest long ago.

But my most important internal energy was restricted, my physical stats had each dropped by 100, and the tremendous weight had been added on top of that. I had no way to endure it.

To top it all off, the time limit was only one shichen.

*Shit, Mount Jiuhua isn’t some little hill behind the neighborhood.*

It was so difficult that I even considered breaking the chains connecting the iron balls.

That was before I learned the chains were made of Ten-Thousand-Year Cold Iron.

*They used this for chains? Are they insane?*

In the end, I had no choice but to grit my teeth and power through.

One day, two days, three days, four days…

And finally, today—ten days later.

Ding.

> **System**
>
> Quest **Fire King’s Hellfire Training-1** has been completed!
>
> You acquired a substantial amount of EXP!
>
> Level Up!
>
> You acquired 30 Bonus Points!

With about fifteen minutes remaining on the time limit, I finally reached the summit.

Thud!

“Yaaaaaah!”

I slammed the heavy iron weights onto the ground and let out a roar that rose from the depths of my lungs.

The sound startled Jeok Cheongang, who had been nodding off against a rock. He sprang awake.

“W-what happened?”

*Damn old man. He was always going on about how martial artists shouldn’t waste time sleeping, yet he slept like a baby while I was going through hell?*

Grinding my teeth, I walked toward him.

“Can’t you tell by looking? I climbed Mount Jiuhua within one shichen. I succeeded!”

“Huh? Why are you climbing Mount Jiuhua?”

“What?”

Jeok Cheongang blinked, then hurriedly shook his head.

“Ah, no. You did pretty well.”

“And?”

“I think we can move on to the next stage now. I’ve made the preparations, so handle it yourself.”

I turned my head toward where his finger was pointing.

Propped against a massive rock was a vest. A huge, incredibly thick vest made of iron.

My fingertips began to tremble despite myself.

“…Is this what I think it is?”

“What were you thinking?”

“That I’m supposed to put this on and repeat exactly what I’ve been doing until now.”

“You rascal. What a joke.”

“Right? Wow, you scared the hell out of me.”

“Ha-ha. You had such a cute little imagination.”

Jeok Cheongang let out an amiable laugh like a kindly old man from the neighborhood before continuing.

“If you manage one, the next step should be two or more. Now that I think about it, one shichen was far too generous.”

“What?”

“I’ll give you half a shichen. Hurry up, pick it up, put it on, and get back here.”

“……”

Ding.

> **System**
>
> Quest information has been changed!
>
> Repeat Quest **Fire King’s Inferno Training-1** has been created!

[^1]: A *geun* is a traditional Korean unit of weight; here, one geun is approximately 600 grams.

[^2]: A *shichen* is a traditional time unit of approximately two hours.

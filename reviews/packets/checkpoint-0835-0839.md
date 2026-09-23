# Checkpoint Review — 835–839

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

# Chapters 835–839

## Plot

After five days aboard the swift ship, Jin Taekyung and the Fire Dragon Pavilion party reach Sichuan. Sudal, exhausted by his passengers’ antics, decides to retire. Namho’s swollen forehead turns out to be from a Black Gold Bee sting, despite his boasts.

Near the landing, government military vessels fire on the swift ship. The party deflects the cannonballs, and Jin orders the crew to approach under a white flag rather than retaliate. Ju Wongong recognizes Jin and calls off the attack. Reunited, Wongong reveals that he has been temporarily appointed acting City Lord of Sichuan Province despite remaining under exile. Jin plans to use the office’s authority and government manpower to guard against Dark Heaven.

Jin and the party reach the rebuilt Sichuan Tang Clan, where members of the clan and other Sichuan sects welcome him. Seeing Sichuan Murim beginning to recover and reunite after Dark Heaven’s attack, Jin is greeted by Tang Sadok, who leads him to the Old Master.

## Continuity

- Jin Taekyung is the World Hunter Federation’s Alliance Leader. He erased the Doppelganger, but Main Quest [Cataclysm] and its “Stop the Summoning” mission failed.
- The supernatural Rift began at 10%; its progress increases the distribution and concentration of magical power. The System’s Status Window remains inaccessible, and Jin suspects an update may be responsible.
- Jin’s [Broken Body] injury around his lower dantian remains unresolved; leveling up did not heal it. Jeok Cheongang went to Sichuan to bring his former Disciple, the Divine Physician, to treat Jin.
- Jin’s vision of a black-haired man killing Ahomed after the ritual remains unexplained; Jin believes the man was not Asmodeus.
- Ju Wongong is temporarily serving as acting City Lord of Sichuan Province by imperial order while his punishment and exile remain in effect. Jin intends to use Wongong’s authority and government manpower to prepare for possible Dark Heaven activity in Sichuan.
- The Sichuan Tang Clan and Sichuan Murim are rebuilding and reuniting after Dark Heaven’s attack. Tang Sadok is escorting Jin to the Old Master.
- Sudal decides to retire upon reaching Sichuan. Namho’s blackened, swollen forehead is from a Black Gold Bee sting, not Iron Head Technique.

## Translation Decisions

- Keep magical power distinct from mana. Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.
- Keep Fire Storm and Aqua Storm distinct named spells. Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”
- Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”
- Render 철두공 as “Iron Head Technique” and 흑금봉 as “Black Gold Bee.” Namho’s wartime boasts are comic exaggerations, not evidence that he is a martial artist.
- Keep “military vessel” for 군선 and “cannon” for 대포/포신 in the attack. Preserve Namho’s name-mangling joke when he calls Sudal 해달 (“sea otter”). Ju Wongong’s claim of 황족명 is not an established form of imperial authority.
- Render 천리경 as “thousand-li lens,” 주원공 as “Ju Wongong,” and 진 공자 as “Young Master Jin” when Wongong addresses Taekyung.
- In chapter 839, render 균열 as a social fracture or division, not the supernatural Rift.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader.",
    "Jin erased the Doppelganger, but Main Quest [Cataclysm] and its “Stop the Summoning” mission failed.",
    "The supernatural Rift began at 10%; its progress increases the distribution and concentration of magical power.",
    "The System’s Status Window is inaccessible; Jin suspects an update may be responsible.",
    "Jin saw a vision of a black-haired man killing Ahomed after the ritual; whether it was real remains unknown, and Jin believes the man was not Asmodeus.",
    "Jin’s [Broken Body] injury around his lower dantian remains unresolved; leveling up did not heal it.",
    "Jeok Cheongang went to Sichuan to bring the Divine Physician, his former Disciple, to treat Jin.",
    "Ju Wongong remains temporarily appointed acting City Lord of Sichuan Province by imperial order while under exile.",
    "The Sichuan Tang Clan and Sichuan Murim are rebuilding and reuniting after Dark Heaven’s attack.",
    "Tang Sadok has welcomed Jin as the Tang Clan’s benefactor and is taking him to the Old Master."
  ],
  "continuity_sources": [
    838,
    839
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and who or what was summoned?",
    "Was Jin’s vision of the summoned being real, System-delivered, or prophetic?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, and what is the Ark?",
    "What changed in the System update, and when will its functions return?"
  ],
  "safe_through": 839,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”",
    "Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”",
    "In chapter 839, render 균열 as a social fracture or division, not the supernatural Rift."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 835

# Chapter 835

*Splaaash.*

Sudal, a river pirate belonging to the Yangtze River Channel League and Deputy Stronghold Lord of the Water Dragon Stronghold, which held sway over Hubei Province, sat at the bow of a ship cutting swiftly through the current, lost in thought.

*Looking back, things have gone pretty well so far.*

Sudal had made quite a name for himself in his line of work.

He was the deputy lord of a major stronghold with more than five hundred river pirates under its command. And though it had taken him a long time, he had finally reached the Peak level of martial arts.

Simply staying active and in one piece as he approached fifty made him a model of a successful river pirate. But Sudal had already achieved more than that.

*I’ve saved up a decent amount of money, too.*

It was rare for a water stronghold to have hundreds of fighters.

On top of that, Mu Song, the Ship-Fire Boy who headed the Water Dragon Stronghold, was a shrewd man with powerful backing: he was a direct Disciple of the Alliance Leader of the Yangtze River Channel League. As his deputy, Sudal had made plenty just by picking up the scraps that fell his way.

Of course, a good deal of that wealth had gone to pleasure houses.

*Could I buy a decent manor somewhere out in Hubei? Though property prices have probably gone up again. Damn it. Do they plate the pillars in gold or something?*

Sudal stared gloomily at the current, which broke into rough waves around the ship.

*I never thought I’d be thinking about stuff like this.*

Retirement? Settling down?

A few years ago—not even a few months ago—those soft, mushy words wouldn’t have crossed his mind.

Sudal had always thought of himself as a born sailor and river pirate.

But not anymore. His carefree life as a raider, and his life as a bold man of the water, were both slowly coming to an end.

Even at this very moment.

“Um, Deputy Stronghold Lord?”

At the cautious call from behind him, Sudal squeezed his eyes shut.

*We’re fucked.*

It wasn’t a guess. He was certain.

Ever since they’d left the wretched land of Yunnan five days ago, the same nightmare had come around again and again.

*I thought we might make it through the whole day for once…*

In the end, the inevitable had arrived.

But Sudal didn’t run. He resolved to face it like a brave river pirate and answered.

“I’m listening. Speak.”

“Well, you see, it’s just—”

“Talk, or get your ass kicked.”

“I’m too old to want a beating, so I’ll talk. It’s just… do we have any beef?”

Sudal turned around slowly and looked at the familiar face of his subordinate.

“Are you really that eager to get your ass kicked?”

“Of course not.”

“Then say it again. What meat?”

“I need beef. Specifically, beef marinated in a spicy sauce.”

“Beef, spicy marinade…”

Sudal trailed off and took a deep breath. Recent experience had been teaching him to rediscover the composure he’d forgotten over the past few decades.

“You know where we are right now, don’t you?”

His subordinate nodded enthusiastically.

“Of course. We’re aboard the swift ship, the pride of the Water Dragon Stronghold, symbol of the mighty Yangtze River Channel League!”

“And where is that swift ship?”

“We’ve finally left that godforsaken Yunnan behind and are crossing the Yangtze on our way to Sichuan.”

“Then one last question. In the middle of the Yangtze, after more than a month without setting foot on land, do you think we can get our hands on marinated beef?”

“No.”

“Correct. You’re smarter than you look.”

“Thanks, I guess.”

The subordinate smiled awkwardly at the rare praise, then suddenly turned serious.

“But we have to bring some back.”

“I said we don’t have any.”

“They told me to make some if we don’t.”

“Could it be… that bastard?”

His subordinate looked around before answering in a voice kept low with great effort.

“Sure enough, it’s that bastard.”

You could always count on him to be the one.

Neither of them said the name, but they both knew who they meant.

At the moment, there was only one lunatic who’d demand spicy marinated beef aboard a ship crossing the Yangtze.

*Taishan, the Tiger Giant Child.*

Spending thirty years as a river pirate meant seeing all kinds of idiots and morons. But even a seasoned pirate like Sudal had never seen anyone like him.

A build and appetite that barely seemed human. A level of simple-mindedness that could shock even the most uncultured river pirates.

Actually, Sudal had once met another lunatic of the same sort, albeit one considerably smaller.

“Shit. I’d almost forgotten him, and now I’m thinking about that bastard too.”

“Who’re you talking about?”

“That guy.”

“Oh. That guy.”

They both thought of him at the same time.

The young man who looked perfectly normal, but seemed possessed by some kind of ghost, and would stuff his face with dumplings and sweets whenever he got the chance.

Sudal gazed wistfully back on the past, a few months ago, then let out a sigh.

Before Hubei was stained with blood, he’d been living a peaceful, sensible life as a river pirate.

“Still, things were a lot better when he was around. At least he brought his own food.”

“What the hell are you talking about? He’d gobble it all up, then raise hell demanding candied hawthorn skewers.[^1]”

“Oh, really? That’s what happened?”

“I’m telling you. The second he made eye contact with you, he’d start whining for candied hawthorn skewers. That son of a bitch was a real pain in the ass.”

One lunatic demanded beef with the sauce already on it, and another demanded candied hawthorn skewers.

Sudal shuddered at their cruelty. But then, as now, there was nothing he could do.

The lunatic who wanted beef was a Peak master from the Black Dragon Demon Gate, one of the foremost factions among the unorthodox. He was also the right-hand man of its Young Sect Leader, who was all but certain to inherit the sect. And that little shit he’d mentioned was a far, far bigger figure than even him.

*If it’s Cheongpung, the Huashan Divine Dragon, he’s a big shot among big shots.*

His backing was insane: the Sword Saint, Mae Jonghak, was his Master, and the Sect Leader of Huashan was his Senior Brother.

In terms of seniority alone, he stood on equal footing with the Sect Leaders of the Nine Sects and One Gang. And according to public opinion, his talent for martial arts was among the top three throughout history.

*The heavens are cruel. Why give all that to a bastard like him?*

As Sudal looked up at the clear sky and lamented his fate—

*Crack!*

Something broke, followed by a shout like the roar of a beast.

“Beef! Taishan wants beef! Spicy sauce!”

Sudal’s subordinate turned pale as he spoke.

“This is bad. He’s already at moderate rage.”

“Moderate rage?”

“I’ve watched him for the past five days and worked out the stages. Once he reaches full-blown rage, he’s barely human.”

“Pretty sure he’s been like that from the start…”

“Anyway, give him something, anything! Right now, before he puts a few holes in the swift ship!”

“What?!”

Sudal snapped out of it and told him where he’d hidden his emergency rations for drinking snacks.

“There’s a jar in the corner of the cabin I use.”

“Beef?”

“No. Salted pork. Top quality.”

“That still won’t be enough, will it?”

“Of course it won’t. With his appetite, he could eat the whole jar and still want more. But what if you take it over with the Young Sect Leader of the Black Dragon Demon Gate?”

“Ah!”

“Go. The fate of this ship is in your hands.”

“That’s our Deputy Stronghold Lord, all right!”

The subordinate raised a thumb and hurried off. Sudal watched him go with a proud smile and rubbed the bridge of his nose.

“That boy…”

But the smile disappeared in an instant.

Instead of taking their possessions, he was giving them a ride—and he still had to worry about this.

He’d even felt proud of himself for coming up with a decent solution. Now, all of a sudden, the misery welled up in him, and his eyes grew wet.

*Is this why I became a river pirate?*

A sudden sense of futility weighed on him, but Sudal forced himself to shake his head.

No. He only had to hang on a little longer.

It had already been five days since they left Yunnan. With the heavens on their side, and a good wind, they could arrive within a day.

Then he could say goodbye to those wretched people…

“Hey, don’t block the way. Move over.”

“Huh?”

Sudal snapped out of his thoughts and blinked. An old man who looked stern as hell stood before him, holding a fishing rod.

“You’re…”

“Me?”

“No, Elder…”

“Elder?”

“……What should I call you, then?”

“Just call me Senior No. And get that hideous face of yours away from the bow. The Dragon King would turn tail if he came up here for some fresh air and saw your mug.”

“Ah, yes. Understood, Senior No.”

The old man hadn’t been with them when they sailed from Sichuan toward Yunnan about two months ago.

Now, five days into their voyage back, Sudal still didn’t know exactly who he was. But looking at him now, the old man somehow gave off the air of a master.

Especially…

*That forehead.*

The old man’s forehead was black as if it had been painted, and swollen to twice the size of anyone else’s. Sudal couldn’t take his eyes off it.

*I’ve heard of external arts like that.*

Sudal quickly moved away from the bow and studied him before speaking cautiously.

If he could get on the good side of the mysterious old master who’d been living in seclusion in Nanman and obtain the formula for a martial art, what better fortuitous encounter could there be?

“Um, so…”

“Don’t talk to me. I’m concentrating.”

“Yes, sir.”

Silence settled at once after that single sentence.

Just as Sudal was watching for a chance to speak, the old man sitting at the bow with his fishing line cast suddenly shouted.

“Enough! You brat!”

“Me?”

“Do you know what kind of person I hate most in this world?”

“W-what kind?”

“A man who never finishes what he’s saying!”

“But, Senior, you’re the one who—”

“Shut that crafty mouth of yours and finish what you were going to say. I’m going out of my mind wondering.”

Sudal stared at the old man before him, who already looked like he was out of his mind.

*I thought I’d finally escaped the Fire King, and now there’s another crazy old man!*

The Fire King, Jeok Cheongang, had already left for Sichuan ahead of them on another swift ship.

Sudal had foolishly thought he could breathe easy again. Swallowing his misery, he spoke.

“I was wondering if you’d learned Iron Head Technique.”

“Iron Head Technique?”

“Yes. As far as this junior knows, masters who’ve trained Iron Head Technique to its limits have black foreheads and can even break steel…”

“Hm. I don’t know where you heard that, but you know your stuff. That’s right. Iron Head Technique has different levels and forms, but once you reach Great Completion, you can easily block even Sword Energy.”

“Ooh! Then could you be the famous Great Hero Ironblood Elder?”

The old man scoffed.

“Great Hero? What nonsense. That Ironblood Elder is the lowest of the low. One of the scum of the Murim who absolutely must be hunted down and killed. Though he might already be dead. He spent the entire Great Faction War pretending to sit on the sidelines, while he was up to all kinds of dirty business behind the scenes.”

“Oh. So you aren’t Great Hero Ironblood Elder. I mean, that scum.”

“Obviously not. Are you picking a fight with this old man?”

“Absolutely not. Then, if you don’t mind, who are you?”

“Me?”

The old man puffed out his chest and replied.

“My name is Namho.”

“Ah! Namho?”

“That’s right. This Namho is none other than the very man standing before you.”

The old man, Namho, smiled fondly as he thought back on his youth. Sudal wondered.

*Who the hell is Namho?*

Perhaps because he was an old master from the previous generation, but Sudal couldn’t recall ever hearing that name.

Then the old man spoke again, and Sudal, who’d been unsure, couldn’t help but jump in shock.

“I killed dozens of fiends during the Great Faction War.”

“Dozens!”

“That’s not all. A thousand orthodox martial artists owe their lives to me, and twice that many members of the Demonic Cult died because of me.”

“Wow! A thousand, and two thousand more! A hero born of the Great Faction War!”

“Sure, the Nine Sects and One Gang? The Five Great Families? They’re strong, very strong. But charging in and swinging a blade isn’t the only thing that matters. What matters is victory in battle!”

“Wow! Victory!”

“When I was young, whenever I sent out a messenger pigeon, the great sects everyone had heard of would move, huh? And sometimes the Three Saints and Ten Kings would rush right out!”

“Wow! The Three Saints! The Ten Kings! You must be the Martial God at the very least!”

“And that man was me, Namho!”

“Wooo! Long live! Long live! Long live our Senior No!”

Sudal threw both arms up and shouted along. Then something struck him as odd, and he blinked.

“Um, what did you say just now?”

“What are you talking about?”

“Er, I thought I heard you say you sent out a messenger pigeon.”

“Yeah. I did. From the rear.”

“……?”

“Is that a problem?”

Sudal stared at Namho, who remained completely unashamed. After a brief silence, he parted his lips.

“Then, Senior, do you have a title?”

“No.”

“Your martial arts…?”

“Why would I learn something like that?”

“……?”

“Martial artists have it filthy dangerous and hard. When they’re young, they show off and get stabbed to death. When they’re old, they’re practically guaranteed to end up with their bodies wrecked.”

“……!”

“Look at you. You’re trembling right now. You’re getting old, your martial arts are mediocre, and your body’s starting to give out. Might be a stroke, so if you’re interested, come along. I’m on my way to see a famous physician.”

About half of what Namho said was true.

Sudal had already lost it. But he wasn’t trembling from a stroke—he was trembling with rage.

The last thread of reason he had left was moving his lips to resolve one final question.

“T-then what about that Iron Head Technique you mentioned?”

“I said I knew about it. I never said I’d learned it.”

“But if you haven’t even learned Iron Head Technique, why is your forehead so—”

“I got stung by a bee.”

“……!”

“Some beastly bastard disturbed a Black Gold Bee’s hive because he wanted the honey, and I nearly died for it. We somehow managed to draw out the venom, but this swelling just won’t go down.”

As Namho gently rubbed his black, swollen forehead, Sudal felt the world go dizzy, as though he’d been stung by a bee himself.

*What kind of fucked-up situation is this…?*

Two months.

A whole two months. He’d left the merchant ships laden with wealth and grain behind, and under what was practically a threat, he’d been dragged away from his home base in Hubei to Sichuan, and then all the way to Yunnan.

And it still wasn’t over.

The waiting had gone on forever. He’d stopped in Guangxi for a chance to make some pocket money, only to be caught by the Fire King, Jeok Cheongang—who was known as the Blood Monk—and dragged along.

It was easy to call it two months, but being trapped on a ship with the ugliest, most uneducated people in the world had made those two months feel like two years.

*All I have to do is take them to Sichuan, then I can go back to Hubei. And this is what happens at the very end.*

One beast of a man spent all day shoving whatever he could into his mouth. This time, he’d been tricked by a powerless old man he’d never met before and showered with insults.

That wasn’t all. The rest of them were just as crazy.

Hyuk Mujin—the one he’d already seen enough times to know—was going around preaching some religion called the Earth Mother Goddess, or something. Song Ilseom and Sama Pyo, who’d looked like they disliked each other from the start, had dueled on deck and half destroyed the mast.

And Ju Hwaran, the Ten Dragons and Phoenixes and the most beautiful woman in Sichuan?

Just two months ago, when they’d set out for Nanman, she’d looked like a fairy. Now she spent her days coming out onto the deck to keep an eye on everyone.

And whenever she heard even the slightest sound somewhere, she’d prick up her ears and mutter as though she wanted everyone to hear.

*Oh. The Pavilion Master still needs to rest. Does that barrel really have to be moved right now?*

*Oh. That rope scraping is so loud. Should I just cut every rope so the Pavilion Master can be comfortable?*

*Oh. Why’s he gulping down water like that? Couldn’t he go without drinking and slowly dry up instead?*

*Oh. The waves are so rough. What if the Pavilion Master suffers qi deviation while circulating his qi because of all the noise? You’re river pirates, aren’t you? Can’t you do something about a single wave?*

What was he, the Dragon King? How was he supposed to calm a raging river?

He’d been patient long enough. Five days of seeing things he couldn’t stand and hearing things he didn’t want to hear.

*That’s it. I’ve got nowhere left to retreat. I’m settling this today.*

Overcome with fury, Sudal drew the broad-bladed saber tucked into his waistband.

Or, he tried to.

Until a familiar voice sounded behind him.

“Whew. I feel so much better after getting a good rest. Hey, mister, how far have we come?”

Sudal slowly turned around. He looked up at Jin Taekyung, who’d shown himself for the first time in five whole days, and answered with a grin.

“Hehe. We’ll be there soon.”

That night, the swift ship arrived in Sichuan, and Sudal decided to retire.

[^1]: Candied hawthorn skewers are a traditional Chinese street snack made by coating hawthorn fruit with hardened sugar.
## Chapter artifact 836

# Chapter 836

Five days. A short time, if you looked at it one way; a long time, if you looked at it another.

I didn’t know which one it was closer to.

But one thing I could say for certain: it was enough time for the swift ship the Yangtze River Channel League was so proud of to travel from Yunnan to Sichuan along a tributary of the Yangtze.

*It’s been a while since I was here.*

I murmured to myself and looked at the scene spread out before me.

A stretch of the Yangtze so vast it looked like the sea.

The river, turned pitch-black with the setting sun, was streaked with lights of every color.

“What are those…?”

Namho narrowed his eyes. Hyuk Mujin explained what the countless lights in the distance were.

“Pleasure boats.”

“Do you think I asked because I didn’t know?”

“Oh, you know about those too, Old Man Nam? I thought you were seeing them for the first time, since there’s nothing like that in Nanman.”

“Hah!”

Namho snorted so hard I wondered if he’d done it through his ass instead of his nose, then gave a hollow laugh.

“Have you ever seen such a fool? You’ve already forgotten what kind of man this old man is.”

That was right. Namho wasn’t just some ordinary old man from another people.

Nanman blood ran through his veins, but there was no doubt he knew the Central Plains’ geography and customs better than some old martial-world veteran who’d chewed his fair share of bok choy in his youth.

Even if it was all in the past now, Namho had once been one of the finest agents in the Hidden Shadow Pavilion.

“Oh, right. I keep forgetting because you’re always right there.”

Hyuk Mujin scratched the back of his head sheepishly. Namho nodded at him with a solemn expression.

“I’ll forgive you. It’s only natural—you find this old man so sociable and approachable.”

“You are approachable, all right. Looking at you reminds me of Grandpa Hong, who lived next door when I was a kid.”

“Grandpa Hong? Whoever he was, he must have been a good man if he reminded you of me.”

“He made a fortune lending money at exorbitant interest. He always had bodyguards with him whenever he went out to the market, probably because he did so many things to make enemies. Anyway, he ended up getting killed.”

“……”

“Then why were you looking at the pleasure boats like they were so fascinating, if you already knew what they were?”

Was this bastard trying to start something with me?

Namho glared at Hyuk Mujin with exactly that look, then let out a deep sigh.

“I wasn’t looking because I found them fascinating. I felt empty.”

“Empty?”

“Yes. It made me think about how little the Central Plains have changed.”

Namho gazed at the ships gliding along the Yangtze, their lights bright in the distance, and continued slowly.

“Some people in this world risk their lives fighting to set a collapsing realm back on its feet, while others float pleasure boats and lose themselves in indulgence. How could that not seem ridiculous? How could it not leave me feeling empty?”

“Ah.”

“I’m not blaming you, young as you are. Nor am I telling you to be angry with them. But there’s just one thing I’d like to ask of you.”

Hyuk Mujin had fallen silent. Namho took in the faces of him and the others one by one, then added in a bitter voice:

“No matter what you see, please don’t lose heart. If you have the will, you can get back up no matter how many times you fall. But if your will is broken, you won’t accomplish a thing.”

This wasn’t the Namho we usually saw.

This was advice from a veteran who’d weathered the storm of the Great Faction War—and from an old man.

And the feeling that Namho’s gaze lingered on me in particular at that moment wasn’t just my imagination.

*He must be worried. The Jin Taekyung I am now—the Blazing Flame Divine Dragon—has never been through a proper war. I’m just a kid.*

I was young even by modern standards, but in Murim there was all the more reason for people to look at me with concern.

I’d only started making a name for myself in Murim less than two years ago. And on top of that, I’d barely passed twenty.

To an old martial-world veteran, Jin Taekyung of the Jin Family of Taiyuan was far too young to be expected to have matured mentally.

Of course…

*Hunter Jin Taekyung is different.*

If someone asked whether I’d grown up, I’d say… probably not. I still acted like a kid now and then—or pretty often, honestly—and I had a bad habit of letting my emotions get the better of me.

But at least I wasn’t so easily shaken that the people around me needed to worry.

No. I’d already been through too much for that.

I’d been stabbed in the back by someone I’d thought was on my side—someone I’d once even looked up to. And in the process, I’d lost someone close to me.

While I struggled to save people, risking my life to do it, the media tore into me, and people online split into two camps and waged another war.

Even when a country’s capital falls and a hundred thousand people are killed or injured, there are bystanders everywhere.

People who click the news without a hint of feeling, then close the article before they’ve even read half of it.

Why?

*It’s obvious.*

They’ve got a new game to play, or it’s time to head to the club.

Or they’re the type who don’t care if tens of thousands die, as long as it’s on the other side of the world and not in the neighborhood next door.

Once, every one of those things hurt.

But as time passed, my heart—scratched raw by countless strangers whose faces I’d never seen—grew calloused and hard. The pain that used to pierce deep into me eventually became familiar.

Yeah. That was that.

I had too much on my shoulders to let every little thing wound me and make me suffer.

“They’re having a good time.”

I finished thinking, gave a quiet laugh, and said it aloud. Namho’s eyes widened at my words. Then he, too, gave a bitter smile.

“Yes. They are.”

I didn’t know how much that had reassured him. But after some time passed, he’d understand on his own.

That the Blazing Flame Divine Dragon Jin Taekyung wasn’t just some kid overflowing with strength and talent.

“Let’s go. The moment we reach the landing, we move out without delay. Don’t anyone think about dawdling.”

At my order, Taishan shot his hand up.

“Taishan wants five-spice pork.”

“Five-spice pork?”

“Yes. Taishan’s favorite.”

“Five-spice pork, sure. It’s delicious.”

“Captain. Good. Taishan and Captain agree.”

“But are you sure? By the time we get to an inn, you’ll have swallowed so much river water there won’t be room in your stomach for five-spice pork.”

Taishan looked back and forth between the river, black enough to hide its depth, and me, who’d made thorough preparations for the Yangtze dip-and-taste punishment. Then he slowly lowered his hand.

“No. Taishan thought again. Taishan doesn’t want five-spice pork.”

“You sure?”

“Mm-hm. Sure…”

Taishan answered in a drooping voice. Sama Pyo looked at him with sympathy, while Namho—wearing a look of regret for a different reason—beckoned to the head of the river pirates.

“Hey, sea otter. Come here.”

“It’s Sudal.”

“That’s what I said. Sea otter.”

“Sudal…”

“Sea otter.”

“……”

Watching the river pirate’s face as Namho stubbornly mangled his name until he didn’t even have the energy to argue, I felt sorry for him.

I patted his shoulder sympathetically.

“Come on, we’re almost there. Just hang in there a little longer.”

“Th-thank you, Great Hero Jin.”

“I know we’ve been pretty hard on you. When we see Senior Mu Song later, I’ll tell him Uncle Heimdall had a rough time.”

“Sorry, but who’s Heimdall…?”

“Your name isn’t important right now. Let’s just get to the landing first. Mister, are you sad to leave us? If you are, how about we take a trip around the Yangtze for about a week?”

Sudal, Sea Otter, Heimdall—whatever his name was—his unfocused eyes suddenly flashed. His expression gave away some emotion I couldn’t quite place, somewhere between anger and madness. He bellowed at his subordinates until his voice nearly gave out.

“You lazy bastards! Pick up the speed!”

“……”

Judging by his reaction, they really must have had a rough time.

Then again, with the Fire Dragon Pavilion members—each one more impossible to control than the last—it was only natural.

Even Ju Hwaran, the only woman in our party and the only sane person, was showing signs of something being wrong.

“Ah, does he have to shout so loudly? The Captain’s already exhausted. What if all that noise gives him qi deviation? What’s he thinking?”

“……”

At this point, even hearing it scared me.

She kept moving her lips and muttering under her breath. Her diction was at the level of a Murim Alliance announcer, and her projection was like an opera singer. Every word hammered into my ears like a nail.

I’d only been outside the cabin for half a day, and I was already like this. The river pirates, who’d endured it for five whole days, had gone pale.

*They look more like the ones about to suffer qi deviation than me…*

As I seriously considered the river pirates’ condition, their leader—who’d been directing the swift ship and burning through the last of his energy—hurried over.

“G-Great Hero Jin. There’s a problem.”

His face, already no less terrifying than a demon’s, had gone stiff.

At least we were on the Yangtze. If we’d been on the Grand Line, his face alone would’ve sent his bounty soaring and made the government mark him as a target.

I asked with sincere concern.

“I knew this would happen. Are your qi and blood all tangled up?”

“What? No. I’m perfectly fine—”

“I’ll do whatever I can. Don’t hold it in—tell me what’s going on. Your complexion’s awfully dark. And you’re looking off in a completely different direction. You’re a wreck.”

“My face has looked like this since I was born. And my eyes have been like this ever since my father beat me when I was fifteen.”

“Pardon?”

“Please don’t misunderstand. My father was just startled. He’d been sleeping soundly, then suddenly woke up and saw my face the moment he opened his eyes. If it were me, I’d probably have thrown a punch too.”

“Ah. Your father…”

A normal person would’ve been flustered here. They’d stammer, unsure what to say next, then watch the other person’s face and apologize in a way that was worse than not apologizing at all.

But, using the composure befitting a Supreme Peak master, I naturally pointed up at the fireworks that were now filling the sky.

“Whoa, look over there. Fireworks. Are they having a festival?”

“They are fireworks, but it’s not a festival. That’s what makes it a problem.”

“A problem? What’s wrong with setting off a few fireworks?”

“Look closely. At the ships, not the sky.”

The ships? What about them?

I lowered my eyes without thinking.

And when I saw how close the pleasure boats had gotten, I finally understood why Sudal had hurried over.

“Those are…”

“They’re not all pleasure boats. No wonder there were so many more lights than usual.”

He was right.

From far away, those ships had looked like just a few more lights among the many. But now that they were closer, they looked ten times bigger and sturdier than any pleasure boat I knew.

They were more like…

“Huh. They look like military vessels.”

“They are military vessels.”

“Oh.”

I paused for a moment when he confirmed it, but it didn’t really matter.

Military vessels, my ass. What was there to worry about?

The Yangtze River Channel League’s flag was flying from the swift ship I was on, and I knew perfectly well that this huge band of river pirates had long ago greased the officials’ palms and made friends in the right places.

Or at least, that was what I thought I knew.

*Bang. Bang. Baaang!*

Fireworks burst one after another as the military vessels angled around to present their broadsides. Then, through the gaps in the sturdy wooden hulls, something dark came into view.

“Sudal, what’s that?”

“Looks like a cannon.”

“I know that. Are you messing with me, Heimdall? Why are they pointing it at us?”

The river pirate leader, who’d by now completely lost his name, gave a hollow laugh.

“Because the fireworks they just set off were the signal to attack.”

“What?”

The moment I asked again, dumbfounded—

*BOOOOM!*

About a hundred cannon barrels belched fire at once.
## Chapter artifact 837

# Chapter 837

*Boom! Boom! Boom!*

White smoke billowed up with the flames.

The iron balls came hurtling across more than six hundred yards, smashing the swift ship and crushing the people aboard into finely minced fish…

Naturally, that didn’t happen.

The only thing this world could be said to do far better than the modern twenty-first century was martial arts—not science.

*Boom! Splash!*

The iron balls struck the water instead of the swift ship, sending up waves as the water failed to withstand their force.

Taishan snatched a fish out of the air as the blast sent it flying toward the deck. He looked dejected.

“Taishan sad. This not five-spice pork.”

“……”

Since when did five-spice pork come from the Yangtze?

I gave Taishan a frosty look, then tapped the back of the Water Dragon Stronghold Deputy Stronghold Lord’s head. He was crouched on the deck like a shrimp, just like the other river pirates.

“Get up. You’re a river pirate. Why are you so scared?”

“Gasp! Am I alive?”

“Did you think we’d all died?”

“But I saw them fire with my own eyes…”

“They did fire. Their aim was just terrible.”

Even people who pissed at least once or twice a day sometimes missed the target. Was it really so easy to shoot an old-fashioned cannon?

Only about half of the hundred or so iron balls had been fired properly, and more than half of those hadn’t come anywhere near us.

The ones that had miraculously reached the swift ship had merely served as sacrifices to the river’s wave pool.

*Well, I suppose they’ve only fired a few shots now and then during training.*

When you looked at it that way, it made sense.

The age of competing warlords, when countless factions rose like wildfires to fight for supremacy, had ended long ago.

Even modern humanity, after going through the Great Cataclysm, had settled into peace in just over thirty years. The word Hunter had come to be understood as a profession, not a calling. It was only natural that the soldiers of this unified dynasty, ruled by the Son of Heaven, would grow lax.

There was just one thing I didn’t understand: why were they suddenly firing cannons at us?

“I’ll ask them.”

“Pardon?”

“I was talking to myself. Don’t worry about it. Just steer the ship.”

“Pardon?”

“Get moving. Do you want to spend the night here?”

“Pardon?”

If failing to understand this much counted as a talent, then he had a real talent.

I clicked my tongue at the Deputy Stronghold Lord, who just kept staring blankly and asking me to repeat myself, then called over one of the nearby river pirates.

“Hey, you there.”

“M-me?”

“Yeah. You’re the acting captain now, so steer the ship. Oh, and hang the white flag somewhere it’s easy to see, just in case.”

I didn’t know what had happened in Sichuan while we’d been in Nanman, but I had no intention of attacking the government troops just because a few cannonballs had landed nearby.

No matter how inviolable the boundary between the government and Murim was, martial artists were still subjects of this land. We could end up charged with something as serious as treason.

*Did some local river pirates cause trouble recently?*

As I thought it over, the swift ship—which had paused for a moment—started toward the landing. One of the river pirates shouted:

“They’re reloading!”

Not great news, but not something I was particularly worried about, either.

Even if I didn’t step in, we had human shields who could easily stop a few old-fashioned cannonballs.

“Earn your keep.”

The moment I tossed out that one line—

*Boom!*

The second volley thundered, and a faint whistle came from behind me.

*Whoosh!*

Sama Pyo, Taishan, Song Ilseom—and finally, Ju Hwaran.

In the blink of an eye, they raced across the deck. The brilliant light they summoned met the iron balls flying toward the swift ship.

*Slice! Crash!*

* * *

*Thump. Thump. Thump.*

*Boom! Boom! Boom!*

The cannons kept roaring alongside the urgent beat of drums.

A young man, who’d been watching a singing courtesan dance aboard the largest and most splendid pleasure boat among dozens of them, gave a quiet laugh.

“I don’t know what kind of idiots they are, but they’re having a hell of a bad day.”

His voice was thick with drink, his eyes relaxed. The others had been watching him warily, knowing his usual temperament, but now they finally laughed along.

“Ha ha. That’s what happens to the uneducated.”

“If they realized Young Master was here, they’d abandon their boats and run a thousand li away.”

“But… that flag concerns me.”

The young man reacted to the comment.

“The flag? What about it?”

“Have you ever heard of the Yangtze River Channel League?”

“The Yangtze River Channel League…”

The young man, holding a cup of wine, searched his memory for a moment, then suddenly exclaimed.

“Oh, those river pirates? Of course. There was a group called the Yangtze River Channel League where I used to stay.”

“Yes, exactly. They’re a notorious bunch of scoundrels, even in the martial world. But the boat our navy is attacking is flying the Yangtze River Channel League’s flag.”

“And?”

“Generally speaking, the government and Murim are not supposed to interfere with one another. Besides, the head of the Yangtze River Channel League is famous for being savage and devious. I’m worried this might cause trouble…”

His words, which had been flowing smoothly, gradually faded.

The pleasure boat had fallen quiet. The smile that had been on the young man’s lips a moment ago had dimmed.

*Clack.*

He set his cup down roughly, splashing the wine inside.

“Trouble?”

Every one of them wore glossy silk and had a face that spoke of wealth and status.

Some looked young enough to be the man’s peers; others were middle-aged, old enough to be his father. But all of them held their breath and watched his every move.

“I’m asking because I genuinely want to know… What kind of trouble are you worried about?”

“Th-that is…”

The merchant who’d first spoken stammered.

He ran a sizable trading company in Sichuan, and was already regretting his careless words with every fiber of his being.

He’d even paid a bribe to attend this gathering, hoping to win the young man’s favor. As a merchant, he’d heard and seen a lot, so he’d spoken without giving it much thought. Now, instead of catching the young man’s eye, he was about to fall out of favor.

“I-I’m sorry, Young Master.”

The apology came too late. It wasn’t enough to calm the young man’s temper, which had already turned sour.

His eyes, drooping drunkenly a moment ago, had once again slanted upward with their usual cunning.

*How dare a lowly merchant…*

The young man glared at the back of the bowed merchant’s head.

He valued authority and dignity above all else. And now, right in front of him, this man had spouted nonsense about worrying over a bunch of martial-world ruffians.

The Yangtze River Channel League?

A grand name, but in the end, it was just a collection of stinking, uneducated river pirates.

No matter how inviolable the boundary between the government and Murim was, to the young man they were nothing but bandits who ought to be beaten down on sight.

His belief had only grown stronger since what had happened a few months ago.

“Those ruffians of the martial world are nothing more than subjects of the Great Nation. What is it you’re all worried about?”

At the chill in the young man’s voice, the others, who’d been watching him warily, bowed their heads in a hurry.

“Y-you are absolutely right!”

“I have nothing to worry about. The government troops are as sharp as blades, and with such a wise Young Master here, why would we fear a few martial artists?”

The cannons had long since drowned out the music. The courtesans’ fluttering sleeves, which had danced like butterflies, had settled along with the mood.

The young man stood alone and looked down at the bowed figures with arrogant eyes.

*Pathetic. What are a few martial artists, anyway?*

The drunken haze that had felt pleasant just a quarter of an hour ago now irritated him, and the courtesans, who had seemed to have descended from heaven, had lost their charm.

Perhaps it was because of the dreadful memories he’d had not long ago. The young man still couldn’t let go of his anger. He raised his hand and pointed toward the Yangtze.

“Everyone, raise your heads and look at those river pirates! Look at their end as they’re crushed beneath the might of the Great Nation!”

But as he turned at the same time he shouted, he blinked without meaning to.

“Huh?”

*Did I drink too much?*

That was the first thought to cross his mind.

But even after rubbing his eyes hard with his sleeve and looking again, the scene before him remained unchanged.

Well, not quite unchanged.

The pleasure boat that should have sunk long ago was speeding closer.

“Huh?”

“Oh?”

“What the hell is that?”

The courtesans, who’d been watching their employer for cues, and those who’d reluctantly raised their heads at the young man’s order, all blinked as they watched the unbelievable sight.

*How is it still in one piece?*

*Didn’t they fire the cannons?*

*They did, though.*

*Now that I think about it, they’ve been firing this whole time, haven’t they?*

*Huh? They’re firing right now, too.*

Just as someone had thought, more than ten military vessels were still busy sending cannonballs flying. They were firing more urgently and chaotically than before.

“Y-you idiots! Aim properly!”

“We are aiming properly!”

“Then why aren’t you hitting it?!”

“We are! We definitely hit it! We heard the sound!”

“Then why is it still in one piece?!”

“Hell if we know!”

There was nothing but sincerity in the soldier’s curse.

They’d fired, and fired, and fired again. Together, the military vessels had fired hundreds of cannonballs by now.

They might not have trained enough, and they might have aimed like a bunch of goddamn idiots, but by now, common courtesy—and common sense—said at least one shot should’ve hit.

And yet… it was still in one piece.

The sleek vessel cutting through the black current as it approached from beyond the darkness looked like a ghost.

*Why?!*

Fear slowly rose in everyone’s minds along with that one question.

Every sailor had heard the stories at least once: ships belonging to the dead, said to be impossible to sink with cannonballs and impossible to kill.

*I-is it really a ghost ship?*

*But this is the Yangtze, not the sea.*

*Then was the Yangtze the sea?*

While the soldiers’ absurd thoughts chased one another around, the young man had come right up to the bow of the pleasure boat. He was putting to the test the strange gift he’d received just that day: an instrument called a thousand-li lens.

And he was horrified.

“This is insane…”

The young man muttered an uncharacteristically vulgar phrase under his breath and gaped.

He couldn’t believe what he was seeing through the thousand-li lens.

*Boom! Boom! Craaash!*

Cannonballs bounced away amid the thunderous blasts.

Or, more precisely, people were batting away the cannonballs as they came hurtling toward the ship.

“Y-Young Master. What’s happening?”

At the sudden voice in his ear, the young man hesitated for a moment.

How was he supposed to explain what he’d just seen? Would they think he was crazy?

But the young man’s concern didn’t last long.

Through the thousand-li lens, he saw the face of someone he could never forget, no matter how hard he tried.

“Uh, uh, uhhhh!”

The young man made strange noises as if he’d forgotten how to speak. Then Ju Wongong shouted toward the military vessels.

“Cease fire! Cease! This is an imperial command—no, an imperial-family command, issued by me as His Majesty the Emperor’s eighth-degree relative!”

From far away, Jin Taekyung recognized Ju Wongong and muttered when he heard the shout.

“I heard of an imperial order, but what’s an imperial relative’s order?”

Namho, who knew a thing or two, answered.

“There’s no such thing as an imperial relative’s order. He’s just talking shit. But do you know that guy?”

“Yeah. I, uh…”

Jin Taekyung scratched the back of his head and added:

“I saved his life once, along the way.”
## Chapter artifact 838

# Chapter 838

As you go through life, you meet all sorts of people.

Of course, only a tiny fraction of them become what you’d call meaningful connections.

Most people you meet just pass through your life by chance, then gradually fade from your memory. Their names. Their faces.

But there are exceptions to everything.

Like the guy sprinting toward me at full speed, right as I set foot on the landing.

“Young Master Jin! Young Master Jin!”

Was this guy a coincidence in my life, or a connection?

I pushed the thought aside and faced the young man, who’d already rushed right up to me.

He was handsome in a refined, aristocratic sort of way, though his upturned eyes made him look sly.

Actually, now that I thought about it, his personality had been a bit like that too.

Though right now, he looked about as happy as a dog who’d found the owner it thought it had lost.

But…

“What was your name again?”

The young man, who’d been panting away as if to prove just how poor his stamina was, heard my mutter and stared at me in shock.

“Y-you mean you don’t even remember my name?”

Of course I didn’t. Who remembers every extra’s name when they watch a movie?

But instead of saying that out loud, I answered shamelessly.

“Of course I remember.”

“Liar! I heard exactly what you just said!”

“You misheard. I talk about you all the time. Don’t I, Mujin?”

Unlike the Fire Dragon Pavilion’s fresh-faced newbies, Hyuk Mujin was a veteran. Apart from the year he’d spent at Mount Jiuhua, he’d been by my side the whole time.

He caught the signal in my words and answered with a relaxed smile.

“Of course. You’ve praised Young Master Protagonist so often I’ve got calluses on my ears.”

“See? You heard him, Young Master Protagonist.”

I’d shown him some goodwill and found out his name. A perfect bit of banter had me feeling rather pleased with myself—until the young man looked back and forth between Hyuk Mujin and me with a completely flat expression.

“Ju Wongong.”

“…?”

“…?”

“Not Protagonist. Ju Wongong.”

“…!”

“…!”

After a brief silence, I carefully opened my mouth.

“Did you happen to change your name…?”

“Would I have?”

“Right, no. I just thought…”

“How could you forget? Even now, when I close my eyes, I can still feel the warmth I felt in that cold, dark Dongting Lake!”

At Ju Wongong’s deeply wounded cry, everyone around us turned to look at me. Their voices were hushed, of course.

“What’s going on…?”

“Could it be…?”

“No way…”

“Remember that time our captain went from the Night King to a blushing innocent, then turned into a Supreme Peak-level homosexual…?”

I’d wondered which bastard was making up nonsense like a webnovel title. Turns out it was the very bastard I knew.

I sentenced Hyuk Mujin to death with a glare, then spoke as calmly as I could.

All the while keeping a close eye on Ju Hwaran, who had her hand clamped over her mouth.

“I’ll explain everything. It’s all a misunderstanding.”

And right then—

“Remember that time our captain went from the Night King to a blushing innocent, then became a Supreme Peak-level homosexual? The allegations he denied…?”

For the first time in a while, I lost my temper.

* * *

“Hyah!”

At the coachman’s vigorous crack of the whip, the splendid carriage drawn by six fine horses raced down the smooth highway.

A carriage was a symbol of wealth—a luxury anyone with enough money could afford, regardless of status. But a six-horse carriage was different.

Especially when a golden flag fluttered above it.

*Clip-clop, clip-clop, clip-clop!*

“Clear the road!”

“Make way for Young Master Ju Wongong!”

With dozens of mounted soldiers escorting the enormous carriage, and a golden flag marking it as belonging to the imperial family, the crowd parted like the Red Sea.

“Mom, what’s that?”

“Shh!”

Commoners along the road, young and old, hurriedly dropped to the ground. Even the fat, powerful official who’d been lounging in a sedan chair carried by four sturdy men climbed down with a wobble.

*Huh. So what I heard before we left was true?*

I peered out through the lattice window and looked at Ju Wongong.

It had been over four months by Murim’s reckoning since I last saw him. He seemed more full of life than before.

Well, of course he was doing better. The last time I saw him, he’d looked more like a drowned corpse than a person.

“Everything is thanks to Young Master Jin.”

It seemed his face wasn’t the only thing that had changed while we were apart. Had he learned to read minds? Ju Wongong spoke out of nowhere, stroking his neatly trimmed beard.

“After I nearly died at Dongting Lake, I resolved to be reborn. I repented of my old ways, when I did nothing but drink, chase women, and gamble…”

“And yet you launched a pleasure boat and had a great time.”

Ju Wongong faltered at my words, then changed his tune.

“I repented, but resolved to cut back gradually. I’ve also been training my body…”

“You were about to collapse after running barely a hundred yards just now.”

“Physical training isn’t easy, so I’m taking it one step at a time. Trying to look at the world with an open mind…”

“So you’ve thought about it, but haven’t actually done anything.”

My neat summary could’ve made even Daechi-dong’s top cram-school instructor weep.[^1] Ju Wongong fell silent for a moment, then spoke.

“Why are you doing this to me?”

“And why did you do that to me?”

“I only said what came to mind. I never imagined it would cause such a ridiculous misunderstanding.”

“You should’ve known. Before you hurt my feelings.”

After spending half an hour explaining the whole “time our captain went from the Night King to a blushing innocent, then became a Supreme Peak-level homosexual” incident, I gazed off to one side with a deliberately mournful look and continued.

“One of my subordinates got hurt because of you.”

Ju Wongong followed my gaze and shuddered.

In one corner of the carriage, still racing without pause, a bloody mess—no, Hyuk Mujin—was sprawled against the luxurious interior.

“But it’s not my fault he ended up like that.”

“You did it. He died because of you.”

“Is he really dead…?”

“He’s alive. For now. But he almost died.”

“B-but that’s because you beat him like you were going to kill him!”

“I don’t remember. When I opened my eyes, he was already like that.”

“Of course you don’t! You’d already gone wild by then!”

“Are you shouting at me right now? Just because you’re part of the imperial family, you think you can go around scaring innocent people?”

“N-no, that’s not what I—”

“This won’t do. I’m really hurt. Get out of the carriage. I’m going back to my hometown right now.”

“Why are you telling me to get out of my own carriage? And if you mean your hometown, that’s Shanxi Province. Why would you suddenly go there…?”

“To visit the little—no, His Highness, Prince Shangshan. He must’ve grown quite a bit by now. When I saw him about two years ago, I was even changing his poopy diapers.”

“P-Prince Shangshan! Diapers!”

Even among Celestial Dragons, there were different levels.

Ju Wongong had been horrified at the name of Prince Shangshan Zhu Bao—the Son of Heaven’s only younger brother, the sole Prince, and the chairman of my personal fan club. Then he suddenly furrowed his brow.

“Wait. From what I’ve heard, His Highness Prince Shangshan was already over ten years old a few years ago, and only met you around then. Why would he be wearing diapers?”

Oh, right.

Even when a sharp reader catches a sloppy continuity error, you don’t have to panic. I widened my eyes and shot back:

“Are you making fun of His Highness Prince Shangshan for wearing diapers at his age?”

“Huh?”

“This is treason.”

“Wha—?”

“This is treason! Rebellion!”

“You’re insane! Shut your mouth!”

“Listen, everyone! Protagonist, a member of the imperial family, has insulted His Highness Prince Shangshan!”

“It’s Ju Wongong, not Protagonist! And would you please stop!”

Of course, no matter how loudly I shouted, nobody outside could hear me. I’d sealed off every sound from inside the carriage with my internal energy.

Ju Wongong didn’t know that, though. He immediately dropped to his knees.

“I’m begging you! I’ll do anything you ask, Young Master Jin, so please stop!”

“I’ll have His Highness Prince Shangshan, who brings shame on the imperial family, struck from the imperial genealogy—oh, seriously?”

“I-I mean it. So please, stop. Just let me live.”

If you didn’t know the situation, you might wonder why he was groveling like this. But the current Son of Heaven had a long and colorful history of purging his own relatives on his way to the throne.

Put simply, he wasn’t just an expert at killing his own blood relatives. He was practically the equal of the Primordial Heavenly Venerable.

And if even a hint of the word “rebellion” reached the Son of Heaven’s ears?

Instead of offering a long-winded excuse, the best choice would be to head straight for the Sichuan Tang Clan.

At the very least, people there knew dozens of poisons that would kill you less painfully than the cup of poisoned wine that was sure to arrive soon.

“Why are you crying now? Anyone would think you were actually plotting treason.”

I patted Ju Wongong on the shoulder. I felt a little sorry for him, but there was a simple reason I was pushing him this far.

*It’s easier when you’ve got someone in your pocket.*

Before the carriage left, I’d heard why the guy—who should’ve been stuck in Hubei Province for taking bribes—had suddenly turned up in Sichuan, merrily sailing a pleasure boat.

“My crime hasn’t been completely wiped away. His merciful Majesty merely moved my place of exile to Sichuan for a while, and I’m obeying his command. But if some rumor about treason starts going around… Really, really…”

“Yeah, yeah. I understand. But is what you said earlier true?”

I gazed fondly at Ju Wongong, who was still streaming tears, and continued.

“W-what do you mean?”

I gazed fondly at Ju Wongong, who was still streaming tears, and continued.

“That you’re the acting City Lord of Sichuan Province.”

Ju Wongong sniffled and nodded.

“That’s right. I didn’t expect it either, but there’s no doubt it was an imperial command.”

A lot had happened while I was away from Sichuan.

The City Lord of Sichuan Province had suddenly fallen ill. And the officials weren’t trustworthy enough to be entrusted with such a vast stretch of land and its military forces.

That was probably why Ju Wongong had been chosen.

He was a distant imperial relative, with no real claim to the throne.

He lacked the nerve, ability, and backing to make such a claim, and his only real talent was drinking, chasing women, and gambling. There couldn’t have been a more suitable person to fill an empty seat for a while.

But Ju Wongong could offer me more than I’d expected.

His appointment might only be temporary, but the authority of the City Lord of Sichuan Province was a different matter from his personal incompetence.

*At least as long as I’m in Sichuan, I can make sure they’re well prepared for Dark Heaven.*

The government and Murim had long maintained an uneasy coexistence.

But if I could mobilize the government’s manpower—which was incomparable to Murim’s—then maybe we could uncover whatever plans Dark Heaven might have in Sichuan.

Of course, before that…

“Hey, let’s go to the Sichuan Tang Clan.”

I had someone to meet. Someone I’d been separated from for a while.

[^1]: Daechi-dong, in Seoul, is known for its elite private academies and cram schools.
## Chapter artifact 839

# Chapter 839

Time changes many things.

The living. The dead.

Before the laws of time, all things were equal.

Even an absolute ruler who once commanded the world would one day return to the earth. A seed carried on the wind and buried in the soil might grow, hundreds of years later, into a dense thicket of grass.

Murim was no different.

In the distant past, people trained in martial arts and built fences around themselves, each pursuing their own goals.

Countless days and nights passed. Great wars and shining heroes came and went, until at last the present arrived.

The Nine Sects and One Gang.

And the Five Great Families.

Fifteen pillars supporting the Murim of the Central Plains.

Deep-rooted trees that had never been uprooted in the past several hundred years, even when they swayed.

The Sichuan Tang Clan was one of them.

“Once we cross that hill up ahead, we’ll be there.”

At the coachman’s words, Ju Wongong nodded, then sneaked a look at me.

“It’s a shame we have to part here. If it were up to me, I’d treat Young Master Jin with the utmost hospitality, but…”

“Then let’s go to the city. I don’t mind being treated.”

“Young Master Jin seems to have a great many important affairs to attend to, so we’ll save that pleasure for another time.”

I’d only said it to tease him, but the guy had gone and gotten scared.

I snickered as I watched Ju Wongong hastily change his tune.

When you got right down to it, he wasn’t exactly a bad guy. He was just incompetent, fond of pocketing money from anyone and everyone, and used his imperial status to live in luxury.

“……”

Now that I put it that way, he did sound like a bad guy. Some of the bribes Ju Wongong had accepted must have come from squeezing the people dry.

*He still hasn’t learned his lesson, even after nearly dying. Should I lay into him some more?*

My concern must have shown on my face. Ju Wongong went pale and urged the coachman on.

“Every second counts! Pick up the pace!”

“It’s not that urgent. Don’t hassle the poor guy for doing his job. You should worry about yourself.”

“Every second does not count! Maintain this speed!”

This feeling of controlling an avatar was surprisingly fun.

Maybe it was even more fun because he was a distant imperial relative and the acting City Lord of Sichuan Province.

Well, I had saved his life, and he was easy to handle. Keeping him on friendly terms could come in handy.

“No need to go any farther. Let’s stop here. We’re almost there anyway, and neither side will be happy if we show up at the Sichuan Tang Clan like this.”

We might not have many, but if we rolled up with dozens of heavily armed cavalrymen and a six-horse carriage bearing the imperial flag, we weren’t exactly going to draw a welcoming crowd.

The relationship between the government and Murim was, to put it nicely, one of noninterference. In practice, they tended to keep their distance from each other.

“Oh, that’s a very good idea.”

Brightening at the thought of parting ways with me, Ju Wongong quickly ordered the procession to stop. Then he kindly climbed out of the carriage and opened the door for me himself.

“I hope you’ll forgive me for not seeing you off any farther. And I sincerely wish Young Master Jin a future filled with w-w…”

“Martial fortune?”

“Ah, yes. I sincerely wish you the best of martial fortune.”

I had no idea how sincere he was, but kind words deserved kind words in return. I smiled and patted Ju Wongong on the shoulder.

“Right. You take care of yourself until we meet again, Your Highness. And maybe cut back a little on the wine, women, and gambling while you’re at it. Got it?”

“I understand. I won’t forget your advice, Young Master Jin.”

“Good. See you.”

“Travel safely.”

I nodded and shut the carriage door.

*Clack.*

Ju Wongong, who’d been staring blankly at me through the lattice window, opened the door again.

“Um… aren’t you getting out?”

I blinked and asked him back.

“Why would I get out?”

“Huh?”

“Oh, I haven’t told you yet. I’m going to borrow this carriage.”

“……?”

“As you know, we’ve got elderly people and sick people in our party. I figured it’d be more comfortable if we had one. And when we’re out on the road, people are more likely to clear the way.”

“……!”

“You Fire Dragon Pavilion folks. Come on in. You’ve had a hard time riding all this way.”

An ordinary martial artist would’ve been flustered by what I said.

It’s an imperial carriage, can we really do this? No, it’s all right, I’m fine, and so on—one model answer after another.

But the great Fire Dragon Pavilion members were a different breed.

Actually, whatever fresh-faced promise they’d once had had come back from Nanman dyed yellow.

“Aw, shit. My whole body’s aching bad enough to kill me, and these Central Plains bastards are so high and mighty they don’t even respect the elderly…”

Namho started, muttering just loud enough for everyone to hear and patting his lower back. The Fire Dragon Pavilion members climbed down from their horses and filed into the carriage.

Of course, they didn’t forget to make their own comments.

“They didn’t even give us five-spice pork. Taishan angry. Want to smash everything.”

“Now, now, Taishan. No matter how poorly they treat us, you mustn’t do that.”

“It reminds me of when I’d just started life as a wandering martial artist. People didn’t treat me like a person back then, either.”

“Nice carriage, Pavilion Master. Could we take it back to our Escort Bureau later?”

I told Ju Hwaran she could, then turned to the carriage’s owner, who stood there stunned, and politely asked:

“Could you pull off the flag hanging there? We’re not imperial family, and it’d be a pain if we went around with that thing still on.”

“……”

Ju Wongong looked from us, packed snugly inside the carriage, to the cavalrymen staring awkwardly off at the distant mountains. He let out a deep sigh.

Then he yanked the splendid golden flag free.

“Oh, and close the door for us.”

“……”

“Don’t want to?”

*Clack.*

This feeling of controlling an avatar really was a lot of fun.

* * *

The first to greet us when we reached the Sichuan Tang Clan were the gate guard’s gruff voice and wary eyes, watching from atop the newly built stone wall.

“Stop! State your affiliation and name. If you’re a martial artist, give your title and reason for coming.”

The gate guard’s wariness vanished without a trace the moment I leaned my head out of the carriage.

“Open the gate! Open the gate!”

“Why? Who’s here?”

“I said open it, you little bastard!”

When I first visited the Sichuan Tang Clan a few months ago, I was pretty sure hidden weapons had come flying at me. This time, the gate opened before I could even open my mouth.

*Rrrrumble.*

As the massive iron gate swung open, the gate guard smacked the dim-witted new recruit on the back of the head. He clasped his hands to me several times, then rushed off somewhere in a panic.

“Everyone, come outside! The Fire Dragon Pavilion has arrived!”

“What?! Are we under attack again?”

“What kind of crazy talk is that? The Fire Dragon Pavilion led by Great Hero Jin Taekyung, the Blazing Flame Divine Dragon, is here!”

“What?!”

Maybe he’d been taking a nap after his shift. A martial artist of the Sichuan Tang Clan, a white trail of drool still at the corner of his mouth, tossed aside the hidden weapon in his hand and came running.

Or, to be precise, it wasn’t just the Sichuan Tang Clan.

“Great Hero Jin! Do you remember me?”

“It’s a pleasure to see you again. Thanks to you, the disciples of our sect avoided a great many casualties.”

“Amitabha. To think that Benefactor Jin has returned to Sichuan Murim. On behalf of Emei, I offer you my thanks once more.”

“Well, well, who do we have here! Gae-ttong, go get the others!”

The martial artists of the Sichuan Tang Clan, dressed in green uniforms, were joined by Daoists from the Qingcheng Sect, nuns from the Emei Sect, and finally even the beggars of the Beggars’ Sect.

At the sight of that enormous crowd surging in like a sea of people, Namho gaped.

“Hell, what in the world have you been doing?”

“I more or less told you what happened in Sichuan.”

“Even so, this is… It’s strange enough that people from other sects are here with the Sichuan Tang Clan, who are famous for their foul tempers. But why are they all coming out to greet you like this?”

“I just did a few things here and there.”

Namho knew some of what had happened, but I didn’t go into detail.

There was nothing more embarrassing than praising myself, and he’d find out naturally anyway.

*Still, it looks like everyone’s been doing well.*

I kept bowing my head as cheers and clasped-hand greetings poured in from every direction. A warm feeling stirred in a corner of my heart.

To be honest, I’d been a little worried.

It hadn’t even been half a year since the forces of Dark Heaven, led by the Western Heaven Demon Lord, swept across Sichuan.

The Sichuan Tang Clan had been the main target and suffered enormous losses. Qingcheng, Emei, and the Beggars’ Sect had all paid in blood, too.

But contrary to my fears, the faces surrounding me now held nothing but joy.

*Thank goodness. Thank goodness.*

The Outer Court, where dark-red bloodstains had still been visible just before we left, was now full of green grass.

The sky, once blanketed in black smoke from the fires that burned countless bodies day after day, was clear without a single cloud. Beneath it stood rows of pavilions rebuilt through everyone’s help and hard work.

I didn’t know whether they had completely moved on from the grief of that day.

But one thing was certain.

The Sichuan Tang Clan—or rather, Sichuan Murim—had risen again.

They had stopped the invisible rift that had persisted all this time, coming together to rise above their grief.

To avenge what they had lost.

And so they would never lose something precious again.

*Yeah. That’s all that matters.*

As if making a promise to myself, I repeated those words with force in my heart and climbed down from the carriage.

The crowd that had gathered all around us had already blocked the road. But more than that, I’d spotted a familiar face approaching in the distance.

*Thud. Thud. Thud.*

A body so slender it was almost emaciated. A pallid face like that of someone suffering from an illness, and footsteps landing with vigor, as if he were scolding his own frailty.

*Thud.*

Suddenly, he stopped.

The cheers gradually died down, and the crowd parted to either side.

At the end of the path, an old man looked at me with eyes gleaming a soft green.

“It’s been a long time.”

His greeting was not merely stiff—it was cold.

But the next moment, everyone watching in bated breath saw it clearly.

The old man’s back, which seemed as if it would never bend to anyone, inclining toward me.

And they heard the warm voice of that old man—a voice no one there had ever heard before.

“I, Tang Sadok, Family Head of the Sichuan Tang Clan and the Myriad-Poison Asura, have the honor of meeting my family’s Benefactor.”

The unexpected courtesy was so profound that I was at a loss for words. Tang Sadok clasped his hands in a formal salute, his sincerity plain, then smiled at me.

At the corners of his mouth, always sharp and hard as a dagger, dimples appeared—dimples I’d never seen before.

“It’s good to see you again, Blazing Flame Divine Dragon Jin Taekyung.”

At that one line, filled with the old man’s joy, the suppressed cheers rang out thunderously.

At the same time, another voice slipped through the noise and into my ear—one only I could hear.

*I have plenty I want to say, but we’ll have to save it for later. Don’t you agree?*

I belatedly smiled back and nodded. Tang Sadok’s Sound Transmission continued.

*Come with me. I’ll take you to the Old Master.*

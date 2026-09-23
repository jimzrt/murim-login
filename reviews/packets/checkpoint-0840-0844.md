# Checkpoint Review — 840–844

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

# Chapters 840–844

## Plot

At the Sichuan Tang Clan, Jin Taekyung reunites with Jeok Cheongang, who has been arguing with the Divine Physician over Jin’s treatment. After two days of talking, Jeok listens as Jin explains the modern world’s renewed monster crisis. They suspect the crises in both worlds are connected. Jin later concludes that Dark Heaven links the worlds, though he still cannot explain how it reached Murim or identify the Lord of Heaven. A prophecy recalled from the Doppelganger leaves him shaken.

Meanwhile, Hyuk Mujin wakes in the Tang Clan’s Medical Hall, bruised from Taishan’s attempt to revive him. He hears how badly Jin beat him and learns the Divine Physician is preparing a recovery pill for Jin. Ju Hwaran keeps the bickering group in line.

Elsewhere, the Blood Lord inspects Dark Heaven’s experiments on Peak masters. Dissatisfied with the seeds’ strength and duration, he orders the sorcerers to prepare selected people for later deployment. Determined not to underestimate Jin again, he sends missives by hawk after receiving the Lord of Heaven’s order to bring down the heavens.

## Continuity

- Jin is at the Sichuan Tang Clan after returning from another world. He and Jeok Cheongang have spent two days talking and trust each other deeply; their Master-Disciple bond remains unformalized.
- The Divine Physician is preparing a pill for Jin’s recovery. Jin’s [Broken Body] injury around his lower dantian remains unresolved.
- Allied martial artists remain at the Tang Clan to treat patients, rebuild, and guard against another Dark Heaven attack.
- Jin concludes that Dark Heaven links Murim and the modern world, but how it reached Murim and the Lord of Heaven’s identity remain unknown. The Doppelganger’s remembered prophecy about a great king overcoming a god’s curse troubles him.
- Dark Heaven’s experimental seeds have been developed over years; some were scattered across the Central Plains and some have blossomed. The experiments consume Peak masters, but their effects remain weak and short-lived. Their precise nature and the two effects being enhanced are unknown.
- The Blood Lord has ordered the sorcerers to prepare selected seeds for later deployment and sent missives by hawk. His arms have regenerated stronger since Mae Jonghak’s Force severed them.
- The Lord of Heaven awoke ten days earlier, ordered the Blood Lord to bring down the heavens, then returned to sleep.

## Translation Decisions

- Keep magical power distinct from mana and internal energy; Jin considers mana and internal energy equivalent in essence, both qi.
- Keep Dark Heaven’s Moving Formation distinct from modern Teleport Magic. Keep Force distinct from martial arts and magical power.
- Keep “seed” for Dark Heaven’s experimental agents or material; their precise nature is unspecified.
- Render 천하를 뒤틀다 as “the world is twisting” and 하늘을 무너트려라 as “bring down the heavens.”
- Keep “Medical Hall” for 의방 and “ointment” for 연고.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader.",
    "The supernatural Rift began at 10%; its progress increases the distribution and concentration of magical power.",
    "The System’s Status Window is inaccessible; Jin suspects an update may be responsible.",
    "Jin’s vision of a black-haired man killing Ahomed after the ritual remains unexplained; Jin believes the man was not Asmodeus.",
    "Jin’s [Broken Body] injury around his lower dantian remains unresolved; leveling up did not heal it.",
    "Jin is at the Sichuan Tang Clan after returning from another world; he and Jeok Cheongang have been talking for two days.",
    "The Divine Physician is preparing a pill for Jin’s recovery.",
    "The Sichuan Tang Clan and Sichuan Murim are rebuilding after Dark Heaven’s attack; allied martial artists remain to treat patients and guard against another attack.",
    "Jeok Cheongang and Jin Taekyung trust each other deeply; their Master-Disciple bond remains unformalized.",
    "Dark Heaven has developed experimental seeds over years of research and has scattered some across the Central Plains; some have already blossomed.",
    "The Blood Lord orders the sorcerers to prepare selected seeds for later deployment and sends missives by hawk.",
    "The Lord of Heaven recently ordered the Blood Lord to bring down the heavens, then returned to sleep."
  ],
  "continuity_sources": [
    844
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and who or what was summoned?",
    "Was Jin’s vision of the summoned being real, System-delivered, or prophetic?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, what is the Ark, and how did Dark Heaven reach Murim?",
    "What are Dark Heaven’s seeds, and what are the two effects the experiments seek to enhance?"
  ],
  "safe_through": 844,
  "temporary_decisions": [
    "Keep magical power distinct from mana; keep Blink distinct from Teleport and Warp. Extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”",
    "Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”",
    "Render 균열 as a social fracture or division, not the supernatural Rift; render 醜王 as “Disgrace King” when used as Jin’s mocking imagined epithet for Jeok Cheongang."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 840

# Chapter 840

In the Sichuan Tang Clan, a family built around its bloodline, the Family Head’s authority was absolute. No—in truth, even if Tang Sadok hadn’t been the Family Head, that fact wouldn’t have changed much.

The title Myriad-Poison Asura was enough to inspire both awe and fear.

“Our Benefactor looks tired from the long journey.”

At Tang Sadok’s words, the throng surrounding me naturally began to disperse.

The Sichuan Tang Clan’s martial artists, along with outsiders from Emei, Qingcheng, and the Beggars’ Sect, clasped their hands toward Tang Sadok and me before heading back to their posts.

They didn’t forget to urge us to visit their sects, either.

“So you’re the very pillars of the Fire Dragon Pavilion I’ve heard so much about.”

Tang Sadok had been taking a good look at the members of the Fire Dragon Pavilion while I exchanged greetings with the others. Then he suddenly paused.

“As I understand it, every member of the Fire Dragon Pavilion is young. Have you been struck by some deadly poison?”

Namho, the old young man singled out, answered with a face like he’d bitten into something foul.

“Nothing like that.”

“If not poison, then qi deviation?”

“You trying to start something with me?”

“Ah, I only asked because I couldn’t sense any internal energy. In that case, perhaps your age is…”

“Seventy-five. I’m traveling with these fellows for a while, for certain reasons.”

“I see. I spoke out of turn.”

“I understand. We’re both getting old, after all. It happens.”

Though Namho practiced no martial arts, Tang Sadok regarded his confidence with interest. He showed kindness to Ju Hwaran, granddaughter of the Escort King, and to Song Ilseom, who’d reached an impressive realm at a young age. As for Sama Pyo and Taishan, who strictly speaking belonged to the demonic, heterodox arts, he simply gave them a silent nod.

And then…

“What happened to that fellow?”

“Uh, well. Something came up on the way here.”

“It must have been quite something. I’ve never seen a face swell up that much. Was it Dark Heaven?”

“No. I actually hit him a few times.”

Silence fell for a moment.

Tang Sadok looked back and forth between me and Hyuk Mujin, who was slung over Taishan’s shoulder like a sack of luggage, then sighed.

“I’ll have someone look after your subordinates. For now, unpack and visit the Medical Hall in the Outer Court. They’ll treat him well.”

As one of the guards waiting nearby approached at Tang Sadok’s gesture, Taishan spoke in his usual flat voice.

“Taishan. And us. Not moving. No—we are not moving. Until Pavilion Master orders us.”

“Ah, of course. There should be food ready for you, too.”

“I’ll go, then, Pavilion Master. See you later.”

“……”

He really was a lunatic.

I mean, if he was going to do that, why say anything in the first place?

I stopped Ju Hwaran with a glance as she started to smack Taishan upside the head, then followed Tang Sadok toward the Inner Court.

“You seem to earn people’s trust wherever you go. Here in Sichuan, and even among subordinates who haven’t been with you long.”

I answered with a quiet laugh, then spoke as I watched the people slowly disappearing from sight.

“Seems like the same goes for you, Great Hero Tang. I didn’t expect those people to still be with the Sichuan Tang Clan.”

“It’s something I’m truly grateful for. I felt ashamed to keep relying on them, so I told them more than once that they were free to go… Yet they’ve stayed with our family all this time. They’re treating the sick who haven’t yet recovered and continuing to help rebuild the clan.”

“What I’ve seen may not be everything, but the Outer Court already looks much as it did before.”

“Rebuilding is only an excuse. They’re stationed at the family home in case Dark Heaven attacks again. I know the circumstances, so I can’t bring myself to tell them to leave.”

“What?”

“We have to face the truth. If something like last time happens again while they’re gone…I’ll have to choose one of two things as Family Head. Either abandon the home our family has built over generations and run, or make one last stand and be wiped out.”

My eyes widened before I could stop them. I hadn’t expected the Family Head of the Sichuan Tang Clan—one of the Central Plains’ most renowned great clans, known for its pride—to say something like that.

And knowing what Tang Sadok was like, the surprise hit all the harder.

“Are you surprised because I was too honest?”

“Mm. I suppose I am.”

“I understand. Especially since you knew what I was like before all this happened.”

“Of course. Back then, you really…had quite a temper.”

“Hah. I was.”

Tang Sadok let out a hearty laugh, and I gaped at him.

“Are you sure you’re feeling all right?”

“I’m perfectly fine. I’ve simply decided to change.”

“Still, be careful. They say when a person changes too suddenly, it means they’re about to die.”

“Hahaha. You’re still honest to a fault. Though that is your greatest charm.”

“Um, sorry, but I have my own preferences.”

“Yes, that sort of joke isn’t bad either.”

“I’m serious.”

“……I take back what I said just now. You do have a talent for getting under people’s skin.”

I shook my head as I walked beside Tang Sadok.

We crossed the Outer Court, then the Inner Court, and entered the Rear Court. At some point, the unseen presences that had been secretly following us from a distance disappeared completely.

“Is the old—no, is my Master staying in the Rear Court?”

“He is. He arrived two days ago.”

That timing seemed about right.

I’d woken briefly, then fallen asleep again. Three days had passed.

After assessing the situation, Jeok Cheongang had headed for Sichuan without the slightest delay. The rest of the party, who’d stayed behind to look after me while I was deep in sleep, couldn’t have traveled as fast as he did.

“I’m glad he’s still at the Tang Clan. I’d been worried something might have happened to him.”

“Worried? Have you forgotten what kind of person your Master is?”

“His title sounds terrifying, but once you get to know him, he’s full of holes. He’s softer than you’d expect, too.”

“Huh.”

Tang Sadok let out a disbelieving chuckle.

“You’re probably the only person in the world who could talk about the Fire King that way. Then again, he cares for you that much. That must be why nothing serious has happened, even under these circumstances.”

“These circumstances? Did something happen?”

“I mean…never mind. It’ll be quicker if you see for yourself.”

What on earth was going on?

There were a few things that had been bothering me, too.

For instance, Jeok Cheongang had arrived long before us, yet was still at the Sichuan Tang Clan. And Tang Sadok had seemed to deliberately leave out the Fire Dragon Pavilion members.

*No way…*

All sorts of unpleasant possibilities flashed through my mind.

Had Jeok Cheongang been attacked by Dark Heaven while traveling alone?

Or had his condition, which I thought had fully recovered, worsened after his fight with the Southern Heaven Demon Empress?

*Or maybe…*

My thoughts chased one another around in circles. That was when I spotted a small thatched cottage nestled among the varied plants in the deepest part of the Sichuan Tang Clan’s Rear Court.

And though I was more than three hundred yards away, a voice boomed like thunder and pierced my ears.

“Get up this instant!”

“I’m not getting up! I can’t get up!”

“That boy is in danger!”

“There are still patients here who need treatment!”

“He’s my Disciple!”

“They’re my patients!”

“How many times have I told you that boy’s life is in danger if you don’t go now?”

“If it were that bad, would I still be here? I heard about his condition, and I was sure he’d be all right, so I told you we should wait here! I’ve said that hundreds of times by now!”

“No, but you—! I’m telling you, I don’t think that’s what’s going on!”

“The physician decides that, and I’m the physician!”

“One martial artist knows another’s condition best. And I am Jeok Cheongang, the Fire King!”

“My Master is both the Divine Physician and the Slaughter Saint! I inherited his teachings in full, so I know better than you do, Elder!”

“Hey, are you talking back to this old man because you’re counting on that man’s backing?”

“Hey, are you insulting my Master right in front of me?”

“You insolent brat!”

“Oh, I don’t care. Go ahead and do your worst! Strike my pressure points, kidnap me—I don’t care! But if you take me by force, I refuse to treat him!”

“Would you look at this quack! Fine! I’ll count to three! If you don’t get up with that damned travel bag by then, you’d better be ready! One!”

“Two, three! There, happy?”

“You insolent little—!”

“Do whatever you want now! I’m going to gather herbs!”

Bang!

The cottage door flew open with one last shout.

An old man came bursting out as if he’d kicked it down. He smoothed his wildly mussed white hair and grumbled furiously.

“I’ve got enough work as it is, and this is more than once or twice now. I’m so sick of this I ought to just quit!”

Even with internal energy lending it force, his voice had carried a considerable distance.

It was only natural that someone inside, who’d been shouting at the top of his lungs, would be set off.

“Hey! You’re not going anywhere! You’re nothing but a baby who’s only seventy! How dare you! Is that how your Master taught—”

At that moment, the thunderous shout cut off.

A middle-aged man had rushed out of the cottage, then frozen in place when his gaze met mine.

A breeze blew in from somewhere, ruffling the man’s red hair as if it were burning like flames.

*Rustle.*

The air grew heavy. The old man, who’d been about to snap back at him, sensed something was off and turned around.

After silently staring at Tang Sadok and me, he broke the heavy silence.

“Welcome, both of you.”

His voice and smile were gentle, as if he were a Daoist immortal, as though nothing had happened. But having seen and heard everything with my own eyes and ears, I wasn’t fooled.

And at the same time, I understood what Tang Sadok had meant earlier.

I also understood why he’d left the Fire Dragon Pavilion members and the guards behind.

*Pathetic…!*

That was exactly what it was. This was just too pathetic.

The fierce argument between a seventy-year-old Divine Physician and a Fire King over a hundred had a way of making your heart shrink just listening to it.

If anyone in Murim had witnessed that scene, I would’ve been willing to bet both of Hyuk Mujin’s balls that Jeok Cheongang would earn himself another title to go with Fire King.

*The Disgrace King, Jeok Cheongang…!*

I should’ve been happy to see him again after so long. I should’ve been moved that he’d come all this way for me and was roasting the Divine Physician like a peanut over a fire. But it wasn’t easy.

But it wasn’t easy.

“Ah, what a lovely day.”

Tang Sadok’s mutter, as he gazed at a distant mountain as though he’d expected this, sounded strangely hollow.

The red-haired middle-aged man—Jeok Cheongang—looked at me with eyes heavy with emotion and spoke in a solemn voice.

“Your body…?”

“I’m fine…”

“How much…did you hear?”

I answered in a sad voice.

“Nothing… I didn’t hear anything.”

Jeok Cheongang looked up at the clear sky and sighed.

“Fuck. You heard everything…”

The Master and Disciple, reunited after so long, couldn’t look each other in the face for a while.

It was summer.
## Chapter artifact 841

# Chapter 841

Tang Sadok led Jeok Cheongang and me to a pavilion deep in the Inner Court, telling us to let him know if anything was uncomfortable or if we needed anything.

“Then I’ll be going…”

“Wait.”

At Jeok Cheongang’s quiet call, Tang Sadok—still not fully recovered—froze like a statue as he hurried to leave the pavilion.

He slowly turned around and struggled to squeeze out a voice that wouldn’t come.

“May I ask why you called me…?”

Jeok Cheongang’s gaze was deep and still. After staring at Tang Sadok in silence, he suddenly spoke.

“Forget it.”

“Pardon?”

“I said forget it. Everything you’ve seen and heard up to now.”

Myriad-Poison Asura, my ass. The man standing before him was Jeok Cheongang, the Fire King.

The current Sect Leader of the Fire Gate Clan, a venerable sect of complete thugs that popped up every now and then to turn Murim upside down whenever people least expected it.

The sect had been setting fires all over the world for more than three hundred years, generation after generation. Yet when his own residence caught fire, Jeok Cheongang had wiped out more than a thousand Demonic Cult members. The very embodiment of hypocrisy.

A bead of cold sweat he hadn’t even noticed forming rolled down Tang Sadok’s neck. He swallowed hard and answered.

“O-of course. This junior will forget everything he saw and heard.”

“Forget? You didn’t see or hear anything in the first place. What’s there to forget?”

“Ah.”

“Let’s be careful, okay? Read the room.”

Jeok Cheongang gently massaged Tang Sadok’s neck as he whispered. I’d thought he looked strangely familiar, and now I knew why. He was exactly like the high school bullies who used to hang around the alleys near my elementary school.

The only problem was that those bullies had been around seventeen, while Jeok Cheongang was at least a hundred and seventeen.

*How does someone rejuvenate a hundred years?*

He clearly wasn’t new to this.

The low voice. The half-lidded eyes. And on top of that, a masterful choice of words for the situation.

“This old man’s been in a bit of a bad mood lately. So, how do you think I’d feel if a certain kind of story got around Murim right now?”

“I-I think you’d be displeased.”

“Not just displeased. It’d ruin my whole day. I’d completely lose it.”

“I-I’m sorry, Old Master.”

“Your late father, the Poison King, and I had a decent history together. We weren’t close enough to call each other best friends, but he was someone I could trust with my back.”

The Poison King, who’d died a few months earlier at the hands of the Western Heaven Demon Lord, who was after the Myriad-Poison Ring, had been the Sichuan Tang Clan’s Grand Family Head and Tang Sadok’s father. But before that, he’d been a hero who, alongside Jeok Cheongang, had brought the Great Faction War to a victorious close as one of the Ten Kings.

“He had a bit of a gloomy streak, but he was smart and quick on the uptake. One day, he poisoned the liquor I was about to drink. Then, when he saw that Peng Cheolhu, the Thunderbolt Saber King, was getting the hell beaten out of him, he casually knocked over my cup. Do you know what happened after that?”

Tang Sadok answered in a hoarse voice.

“Yes. You said you’d let it go this once, then suddenly beat my father up three months later…”

“Do you know why I did that?”

“N-no. My father wondered about it for years, right up until a few years ago.”

“I was in a foul mood, and there wasn’t anyone around to hit. So I hit him.”

“……!”

“That’s the kind of man I am. Starting to get the picture?”

Tang Sadok’s jaw dropped as he learned the reason behind a beating that had remained a mystery for more than fifty years. And I instinctively opened my mouth.

“Isn’t that just being a lunatic?”

“……”

“……”

“Ah.”

A suffocating silence descended. Jeok Cheongang stared at me wordlessly, then slowly parted his lips.

“Get out.”

“What?”

“Get out!”

“Y-yes!”

At Jeok Cheongang’s thunderous shout, Tang Sadok looked at me with the relieved expression of a man whose fifty-year-old indigestion had finally cleared up, then shot out of the pavilion like a streak of light.

No—he ran away.

Leaving me behind.

*Was he a lizard?*

But I could hardly blame him when I’d just made a huge, beautiful mess all by myself. I took a steadying breath and spoke calmly.

“Old Master, it’s a misunderstanding.”

“What is?”

“Everything. From beginning to end.”

“Our sect’s rules say anyone who spouts bullshit from beginning to end gets beaten twice as much.”

“……Is that really one of the sect’s rules?”

“It is.”

“What lunatic—no, what esteemed person came up with that rule?”

“I did. Just now.”

*Well, I’m fucked.*

If excuses weren’t going to work, it was time to adapt. I dropped to my knees as fast as if Hyuk Mujin had possessed me.

“I’m sorry.”

“You’re admitting it faster than I expected.”

“I’ve still got a lot of life ahead of me. I can’t get beaten to death here.”

“Unlike you, this old man doesn’t think he has much life left.”

“Why not?”

“I was called a lunatic by the brat who’s supposed to be my Disciple. I ought to go die, don’t you think?”

I slowly lifted my deeply bowed head. Jeok Cheongang’s massive pectorals looked like they were at least an E-cup.

He’d recovered his youth and sharpness through Bone Transformation.

At that point, rather than him going off somewhere to die, he could tell everyone except me to go die instead.

“No, Old Master. You’ll live a long life. Though you’ve already lived one.”

“I see. But from where I’m standing, you look like you’ll die young.”

“Please don’t say things like that. You’re hurting my feelings.”

“I’m the one who ought to be more hurt. I shaved my perfectly good head clean and went all the way to Nanman pretending to be a monk, and you dare stab me in the back like this?”

I cautiously raised my head.

Then sunlight poured through the window and flashed off Jeok Cheongang’s forehead in a surprise Solar Fist attack. I reflexively squinted.

“Whoa. That’s bright.”

“……”

“Ah, sorry. And I’ve always been grateful for how much you care about me, Old Master.”

“Too late.”

“Someone once said, ‘The best time to start is when you think it’s too late.’”

“When you think it’s too late, it really is too late. Whoever said that nonsense must’ve died ages ago.”

“Then I’m sorry again.”

“Before I do anything, I want to ask you one thing.”

Jeok Cheongang looked down at me calmly and continued.

“To this old man, you seem closer to a Little Immortal than a human. So if you die, can you come back to life?”

“Why would you ask such a terrifying question…?”

“I’m simply curious.”

“But why are you curious about that…?”

“You said you came from the realm of immortals. You must be different in some way.”

“I die. I really die.”

“You, even in the realm of immortals?”

“I’m dead. I’ve only got one coin left. That was my last life from the very beginning.”

“You’re saying strange things again.”

Come on. Why would he ask something like that?

With my knees knocking, I sprang to my feet and bowed deeply to Jeok Cheongang. Once didn’t seem like enough, so I did it twice.

And as soon as I knelt again, I remembered something I’d briefly forgotten.

“Are you holding a memorial service?”

“Ah.”

“Clench your teeth. Let’s get this over with.”

Whoom.

A tremendous sound of breaking air rang out before he’d even finished speaking.

I squeezed my eyes shut on instinct and suddenly thought of Hyuk Mujin. If I made it out alive, I resolved to treat him much better than before. Then I gritted my teeth and swallowed a breath.

*Hngh…!*

And in that instant—

Tap.

Whoosh!

Along with a faint touch against my forehead, a fierce gust of wind whipped my hair around.

*Huh?*

As the hot wind died down, I opened my eyes in confusion and saw Jeok Cheongang pressing a finger to my forehead, sighing heavily with an irritated look on his face.

His eyes, however, held affection and joy at seeing me again.

“You little monster. Stop making such a fuss and get up already.”

“What?”

“If you’re going to do it, do it properly. Like…bowing, for instance.”

I blinked dumbly. Jeok Cheongang glanced toward the window, where sunlight streamed in, and muttered:

“Sure is a nice day.”

I didn’t know why laughter suddenly escaped me at that moment.

No—that wasn’t true. I already knew.

Today. The day before yesterday. Maybe for a long time now.

“Haha.”

“You little brat. What are you laughing at?”

“Nothing. Let me give you my bow. I’ll make it a proper nine-bow ritual.”

Jeok Cheongang flinched at the mention of the nine-bow ritual, then scoffed.

“We never formally established a Master-Disciple bond. What’s the point of that kind of empty ritual? Just behave yourself from now on.”

He was right. Jeok Cheongang and I had never formally established a Master-Disciple bond.

An old man who had come out into the world to eliminate the Disciple who had once been like family to him needed a new successor to carry on his sect’s teachings. And a young man struggling to stay alive needed greater strength.

They’d come together because each needed what the other had. And so the nine-bow ritual was nothing but meaningless ceremony.

Yes, that was definitely how it had been.

But…

*It stings a little, hearing him say that.*

At some point, what had once felt natural began to sting, and what had stung began to feel natural.

And this changed feeling wasn’t something only I was allowed to have.

“Later.”

A single word suddenly reached my ear.

Jeok Cheongang continued, gazing at the sunlit window. His eyes seemed to be looking at something far away.

“When the time comes, if everything returns to its proper place…”

His voice gradually grew faint, then scattered into the breeze.

But I heard him clearly.

The rest of what he’d left unsaid—not with my ears, but with my heart.

And that was enough.

At least for today.

“Old Master.”

“Why are you calling me?”

Jeok Cheongang answered without turning his head. Maybe he couldn’t bring himself to turn and face me.

“Old Master.”

“What? Why?”

His reaction was exactly what I’d expected, and it made me laugh out loud. Then I said the words I’d kept in my heart for a long time.

“It’s good to see you again. To have you still here, close by.”

“……!”

“I’m back.”

At that moment, Jeok Cheongang’s shoulders, which had gone rigid, relaxed.

He slowly turned to look at me with an expression I couldn’t quite read.

As though he’d never once had to figure out what expression to make in a moment like this, he forced his brows into a frown and twisted his lips awkwardly.

But everyone learns from experience.

No matter how much a person denies it, no matter how unfamiliar it feels, they can’t hide what’s in their heart.

That was true even of the man who had lived for more than a century with a hot, hard mask over his face—the face Murim had named the Fire King.

“Welcome…”

His voice faltered. His expression was still awkwardly tangled with feelings he hadn’t yet decided how to handle.

But the next moment, his stubborn eyes curved into a gentle arc.

A voice as warm as the sunlight reached my ear like a soft breeze.

“Welcome back.”

We smiled at each other.
## Chapter artifact 842

# Chapter 842

The young man who had suddenly awakened from sleep blinked.

An unfamiliar ceiling. A strange smell tickling his nose. And, before he could even grasp what was happening, the shape of something abruptly intruding into his field of vision.

“Ugh!”

Wham!

It happened in an instant.

The young man instinctively sat up—and immediately collapsed again with a tremendous impact.

*What was that?*

He had no idea.

No, he was in too much damn pain to care.

“Urrgh…”

Was this what it felt like to have your face smashed in with a rock?

As the young man curled up and groaned, something big and thick flew through his vision, bleached white with pain, and slapped him across the cheek.

Smack.

“Hyukmu. Wake up.”

Smack. Smack.

“Hyukmu. Hyukmu.”

At the sound of someone’s voice echoing faintly, like it was coming from a dream, the young man—no, Hyuk Mujin—realized who it belonged to.

He also realized that the solid object he’d run into as soon as he sat up had been that person’s face.

*Taishan, you son of a bitch…*

No doubt about it.

That familiar voice. That inhumanly solid body.

There were plenty of monsters around Hyuk Mujin, but only one who was a monster in the purest sense of the word.

Smack. Smack. Smack.

“Hyukmu, are you all right?”

I’m not all right because of you, you bastard.

Hyuk Mujin felt like he was going to cry. He’d only passed out for a moment from the impact, but this lunatic kept slapping him across the face so relentlessly that he hadn’t had a chance to get up.

“P-please stop…”

“Hyukmuu! Open your eyes!”

Whack!

This time, the blow landed squarely. Hyuk Mujin had just managed to open his mouth when he bit his tongue, and his body went limp.

As his vision slowly faded, his life began flashing before his eyes.

*Mother, Father. I’m sorry. You were right.*

He should’ve just taken over the family business like a good son from the start.

If he had, by now he’d be the heir to the Hyuk Family Textile Shop, being called Young Master and scattering silver nyang in the streets. Instead, he’d made a habit of mouthing off to Jin Taekyung whenever he got the chance, then getting beaten until his nose bled.

*And now I’m going to get beaten to death by that bastard Taishan.*

With his vision growing dim, Hyuk Mujin wondered: if he died like this, would it be considered an accidental death or a death in battle?

Then, just as he thought everything was over, he heard a voice like the tolling of a bell of salvation.

“Good heavens, Young Hero Taishan! Stop right now!”

At the clear voice that suddenly rang out, the hand slapping Hyuk Mujin’s cheek came to an abrupt halt.

“Huh? Uh…”

At the sight of Ju Hwaran appearing out of nowhere, Taishan blinked his calf-like eyes and continued.

“Taishan waking Hyukmu. Not doing anything bad.”

“It’s not Hyukmu. It’s Hyuk. Hyuk is your family name. And what you were doing was closer to putting him to sleep than waking him up.”

“That’s unfair. Taishan only wanted to help Hyukmu.”

“Of course. If Young Hero Hyuk had asked you to kill him because he regretted his life, that might be true.”

Ju Hwaran let out a quiet sigh and checked Hyuk Mujin’s condition.

His face, once swollen to twice its size after Jin Taekyung had beaten him, was now three times as big.

“Young Hero Hyuk. Young Hero Hyuk. Can you hear me… Are you crying?”

Realizing he was going to live, Hyuk Mujin answered as tears streamed down his face.

“No, Young Lady Ju. A real man doesn’t cry. Sniff…”

“Then should I call you Young Lady Hyuk from now on?”

“No, I’d rather you didn’t.”

“You sound fine, at least. I’m glad the physician the Tang Family sent earlier treated you well.”

Song Ilseom, who—as usual—had been standing beside Ju Hwaran, looked on and muttered.

“I think we may need to call that physician back.”

“It’s fine. At this point, just applying the ointment the physician left should be enough to make him better soon.”

Hyuk Mujin, who’d been wiping his tears, cut in.

“Young Lady Ju. I’m sorry to say this, but I’m not fine.”

“Finish wiping your tears first. Now, where was that ointment? Young Hero Taishan, did you see it beside the bed?”

“Taishan knows. You mean the ointment in the small porcelain jar?”

“That’s right. Where is it?”

“Taishan ate it. It was pretty tasty.”

“Oh…”

“Young Lady Ju, please call the physician. I think I’m going to die.”

Ju Hwaran wondered which of the two had committed the worse offense—the one who’d eaten the ointment or the one sniveling and making a fuss—but, unable to decide, she decided to have more ointment brought in.

“Captain Song, sorry, could you bring me some ointment?”

“No need to apologize. It’s just that this isn’t part of my duties, so there’ll be an extra charge…”

Song Ilseom noticed Ju Hwaran fiddling with the scabbard at her waist. His face stiffened as he continued.

“…but this doesn’t seem like the time for jokes.”

“Were you joking?”

“Probably. No, definitely.”

“You’re still here, though.”

“I’ll be right back.”

Song Ilseom hurried out the door and returned with ointment before even a few moments had passed. He wasn’t alone—the two people who hadn’t been there a moment earlier were with him.

“I brought plenty of ointment in case that idiot eats it again. Is this enough?”

“I heard Taishan caused another problem while I was away. I’m sorry.”

After Song Ilseom, who was judging the amount of ointment, came Sama Pyo, apologizing. Then Namho asked with an expectant look:

“I’m just asking, but does the Fire Dragon Pavilion have any rules for dealing with this sort of offense? Something like being dismembered into five pieces, for instance…”

At the sight of all three of them firing off whatever they wanted to say, Ju Hwaran reached for her scabbard again. She’d started doing that without thinking, some time ago.

More precisely, it had started when the Chief Escort she’d followed like family had nearly cost the Yongbong Escort Bureau to the Zhongnan Sect, and had only gotten worse after everything she’d been through in Nanman.

*Stay calm, Hwaran. Just a little longer.*

She wanted to go on a rampage, dancing around with her sword like a madwoman. But Ju Hwaran took a deep breath, summoned the last of her patience, and answered them one by one.

“That’s plenty of ointment. Young Hero Sama, don’t leave in the first place. Taishan would probably cause some other trouble even with you here, but at least he wouldn’t eat the ointment or knock Young Hero Hyuk unconscious again. And Old Master Namho.”

“Yes?”

“If you really want to deal with Young Hero Taishan so badly, do it yourself. This is the Sichuan Tang Clan, after all. Why not see if you can find some poison?”

“……”

“……”

“……”

“What is it? Does anyone else have something to say?”

At her frosty voice, everyone in the room shut their mouths and shook their heads.

Even Taishan, who was second to none in the world when it came to being oblivious, and Hyuk Mujin, who’d been groaning in pain, fell silent. They only exchanged glances with the others.

*Young Lady Ju has changed a lot. She’s had a hard time lately, but I didn’t think it was this bad. That man’s supposed to be her escort. Doesn’t he know anything?*

*Why is that unorthodox bastard staring at me? Is he finally looking for a real fight?*

*Good heavens. I thought I’d finally gained an adorable, sweet granddaughter in my old age. How did things end up like this? Well, dismembering someone into five pieces is a bit much. I should look for some poison like that girl suggested.*

*Taishan wants more ointment. It was quite a delicacy.*

*These damn people don’t care that I’m hurt at all. And what does she mean, the Sichuan Tang Clan? What the hell happened?*

Of course, not one bit of communication passed between them, but everyone except Ju Hwaran reached an unspoken agreement.

Until the mood settled down a bit, they’d keep their mouths shut.

It wasn’t until Ju Hwaran’s stiff face softened that Hyuk Mujin, who’d been furtively checking the others’ expressions while applying ointment himself, was able to hear what had happened.

“Wait, two days have passed?”

Ju Hwaran nodded.

“Yes. Exactly two days.”

“Then this really is…”

“As I said earlier, we’re at the Sichuan Tang Clan. To be more precise, we’re in the Medical Hall in the Outer Court.”

Hyuk Mujin just blinked blankly.

He couldn’t believe it. He’d only taken a nap and woken up, but two days had passed—and he’d opened his eyes in the Medical Hall of the Sichuan Tang Clan.

“What on earth happened?”

“Young Hero Hyuk, you don’t remember anything?”

“No. I only remember what the Captain and the Huang tribe member were saying at the river landing. After that, there was a flash before my eyes.”

Song Ilseom, leaning against the wall at an angle with his arms crossed, muttered:

“You remember that much.”

“What? Was that all?”

“Yes. In fact, none of us really saw what happened.”

Sama Pyo nodded without realizing it, then added:

“It was astonishingly fast. I’d never seen a punch that quick. Something blurred, then there was a sound like a drum bursting, and you fell over. That’s all.”

“Lord is wrong. That’s not all. Taishan saw everything, from beginning to end.”

Taishan abruptly cut in, his body shivering as he continued.

“Pavilion Master. Beat Hyukmu. Beat him a lot. Really fucking beat him.”

“……”

“Pavilion Master. Hyukmu already down. Stomped on him. Like mincing meat, stomped him over and over. Ah, Taishan wants meat.”

“……”

“Oh, the Pavilion Master tried to stomp on his pepper, too, but people stopped him. Taishan helped stop him. No one should do that. Ah, Taishan wants Sichuan-style five-spice pork with lots of pepper.”

Namho, puffing on his long-stemmed tobacco pipe in a corner of the Medical Hall, groaned.

“Goddamn it, I told you we should just dismember him into five pieces.”

“Taishan doesn’t know what that is. Namho know?”

“I do. You tie bastards like a certain someone to oxen or horses, then tear their arms and legs right off…”

“Oh! Then Taishan gets the leg meat!”

Crack.

Namho snapped his pipe in two and charged at Taishan with a roar like a wild beast.

Ju Hwaran sighed as she watched Sama Pyo hold him back while he struggled, then spoke.

“Anyway, that’s what happened. That part is safe, so there’s no need to check it right now.”

Taking advantage of the brief commotion, Hyuk Mujin had hurriedly checked that his most important parts were safe. He answered weakly.

“That’s a relief. Where’s the Captain?”

“He’s with Great Hero Jeok.”

“What? For two whole days?”

“Yes. It seems they had a lot to talk about. I don’t know exactly what.”

“But they were together not long ago. What could they possibly have to talk about for two days?”

“They haven’t said anything, so we can only guess. I did hear the Divine Physician is making a pill for the Pavilion Master. Perhaps they haven’t just been talking—maybe they’ve been making preparations to help the Pavilion Master recover.”

At Ju Hwaran’s reasonable guess, Hyuk Mujin nodded.

“Fair enough. He didn’t come back from some far-off foreign land, after all. How much could they have to talk about? Right, everyone?”


* * *


When you return from somewhere far away, you have a lot to talk about.

Especially if all kinds of unimaginable things are happening in that faraway place.

After I’d told Jeok Cheongang my endless story, he stayed silent for a long while. Then he summed up his thoughts in a single, short, blunt remark.

“We’re fucked.”
## Chapter artifact 843

# Chapter 843

Jeok Cheongang was a giant who had left his own footprints in the vast sandpit that was Murim.

He might not admit it himself, but everyone who had ever set foot in Murim thought so.

He was a great martial artist known as the Fire King, and a survivor who had lived through countless wars and crises over the course of more than a hundred years.

If the strong were objects of awe, then the old masters were objects of respect.

And Jeok Cheongang, the Fire King, was one of the few people who met both conditions.

His martial prowess placed him among the top ten in all the vast world. On top of that, his experience and knowledge ran deeper than anyone could guess.

But even Jeok Cheongang didn’t know everything about the world he’d lived in for more than a hundred years.

Much less about a world that wasn’t *this* one.

“We’re fucked.”

After a fairly long silence, Jeok Cheongang spat out those words and became certain.

If everything he’d heard was true, there couldn’t be a more fitting way to put it.

The young man sitting across from him nodded.

“Yes. You’ve got it exactly right, Old Master.”

The young man, Jin Taekyung, clicked his tongue bitterly.

*We’re fucked.* There was no other way to describe how bad things were in the modern world.

One disaster after another had erupted without pause.

Looking back now, Lee Jungryong seemed like a fairy. Michael Silbert and the Doppelganger had spent more than thirty years working together to bring the whole world to the brink of chaos.

No—the chaos had already well and truly begun.

“So, what was it called?”

“Monsters.”

“Right. Mosu-tuh. Those Demonic Cult-like bastards are finally coming in force to the realm of immortals where you live, is that it?”

“Yes. Just like they did thirty years ago.”

This wasn’t the first time Jeok Cheongang had heard this story.

Once, right after they left the Nanman Beast Palace. And again, from two days ago until now.

But even though Jin Taekyung’s explanation was far more detailed this time, Jeok Cheongang still couldn’t easily understand what he’d heard.

He wouldn’t have understood even if he heard it another twenty times.

*How could such a place exist?*

A distant world no one could reach, no matter how many decades or centuries they walked.

An unknown land they’d never see, even after crossing mountains and seas.

And that wasn’t all.

They could speak face-to-face with one another from tens of thousands of li away, and enormous birds made of steel soared above the clouds.

For Jeok Cheongang, whose entire life had been spent walking through a mountain of sabers and a forest of swords, it was only natural that each sentence brought both amazement and disbelief.

If anyone else had told him all this, he’d have slapped them across the face and burned them to a crisp with Flame Divine Palm.

Even if it had been the Martial God or the Son of Heaven.

But…

*Since that brat’s the one telling me, I have to believe him.*

Believe him. Jin Taekyung.

For Jeok Cheongang, it had become only natural. The old man trusted the young man, and the young man trusted the old man.

He didn’t know when it had started, but that was what their relationship had become.

They trusted each other enough to take even the most unbelievable nonsense as fact.

“If Dharma King—that bald monk—were alive and here with us, he’d have fainted dead away. That fool spent all his time staring up at the stars. Do you think he could’ve ever imagined something like this?”

Jeok Cheongang looked at Jin Taekyung, thinking of the friend who had already gone far away.

“The more I hear, the less I understand this world. And yet, in a way, it’s a lot like this one. Don’t you think?”

Jin Taekyung nodded.

At first, everything around him had felt unfamiliar and different. But not anymore.

The modern world and Murim. Murim and the modern world.

The two worlds were astonishingly alike—not in their civilizations, but in the currents of change driving them.

“If Murim has Dark Heaven, then the world I lived in has monsters. And both are headed in a bad direction.”

“Not so long ago, the Great Faction War broke out in each of our worlds, too.”

“That’s right.”

“Then you…”

Jeok Cheongang trailed off, then continued in a grave voice.

“Do you think all of this is just coincidence?”

A short silence fell.

As Jin Taekyung gazed at the oil lamp flickering in the darkness, his eyes began to glow red.

* * *

Late at night, when even the stars had fallen asleep.

Leaving Jeok Cheongang behind, I stepped out of the pavilion and walked alone through the Inner Court.

Instead of heading for any particular destination, I carried the question I’d just heard in my mind.

*Do you think all of this is just coincidence?*

If Jeok Cheongang had asked me something more specific, I would’ve hesitated to answer.

There was so much even I still didn’t know. So many secrets remained hidden in both worlds.

But at least when it came to that question, I was certain.

*Not at all.*

It wasn’t a coincidence.

That was the answer I’d given after a short silence, and it had taken me a very long time to become certain of it.

From the moment I first opened my eyes in Murim until now, I’d kept thinking about it.

And after a long, long time spent wondering, I’d reached one conclusion.

*There’s a connection. A definite connection.*

At first, everything around me had felt like a tremendous run of bad luck.

All because I’d fallen asleep in a damn old capsule. I’d had to fight one danger after another in a world where I couldn’t even tell whether it was a game or reality.

But as my surroundings changed, so did my thoughts.

I’d gone from an F-rank Hunter who lost his job overnight to a celebrity, gripping power and wealth in both hands that I never could’ve imagined before.

And that, in both worlds—the modern one and Murim.

*My bad luck turned into good luck.*

The days when I’d lamented, *How can I be this unlucky?* quickly faded into the past.

What I’d thought was bad luck turned out to be good fortune sent down from the heavens. Maybe it was even more than that—a stroke of heavenly fortune.

That is, until I began to feel a strange sense of déjà vu.

*From Shanxi Province to Henan. Across Sichuan and all the way to Hubei.*

Beneath the dark clouds of Dark Heaven, flames soaked in blood had surged upward.

The Head Elder of the Jin Family of Taiyuan, who had harbored a grudge in a corner of his heart, drew the sword he’d hidden for so many years. A revered monk, praised for his astonishing martial prowess and wisdom, met his death. And the flames that swept across Shaolin Temple spread as far as Sichuan and Hubei.

*And finally, they reached distant Nanman.*

The one saving grace was that the flames spreading in every direction hadn’t turned everything to ash.

Though countless people had died, even more had escaped the fire. And I’d found many traces left behind where that terrible disaster had swept through.

The Water God Dragon, driven insane and stripped of reason.

The fishermen and fish, transformed into grotesque creatures that looked like monsters.

Dark Heaven’s Moving Formation, so much like modern Teleport Magic that it couldn’t simply be dismissed as dark arts or a formation.

And finally…

*The rift that opened in Nanman.*

I still remembered it vividly. No—I couldn’t forget it, even if I tried.

That darkness, writhing like a living creature. The familiarity I’d felt time and again in what the martial artists called demonic qi.

*It was magical power. It had to be.*

At first, I couldn’t accept it.

It shouldn’t exist. It couldn’t exist.

But as time passed, its clear outline began to emerge, urging me to accept reality.

*This isn’t just a difference in terminology.*

Mana and internal energy were identical in their essence. They were both qi.

Something that existed everywhere and nowhere at once.

In the blue sea and the forests, in the smog-filled canyons of skyscrapers—an intangible force that most people couldn’t sense.

But magical power was different.

That evil energy, steeped in death, had flowed in from another world.

If mana and internal energy belonged to the natives, things that had always existed, then magical power was a foreign invader that had crossed over from beyond, along with the monsters.

And that very magical power had appeared.

Not in the modern world, but right here—in Murim.

*How am I supposed to make sense of this?*

Heh.

A hollow laugh escaped me at the absurdity of it all.

How was I supposed to make sense of it? It was reality, and I could no longer turn away from it, even if I wanted to. I already knew the answer.

*Dark Heaven.*

There was no doubt.

Dark Heaven was the true link connecting the modern world and Murim.

Everything I’d personally witnessed since becoming entangled with them was evidence—and served as both prosecutor and judge.

*But how?*

How on earth had they set foot in this world—in Murim?

The Great Faction War had been a major event, but in the end, it was just another war over supremacy in Murim.

If something like the Great Cataclysm had happened, I—or at the very least, Jeok Cheongang and the others who’d lived through that time—would have known.

Rumors that all sorts of hideous monsters had swept across the land would’ve reached even the most remote villages.

*But so far, all anyone knows is that Dark Heaven is the successor to the Demonic Cult and uses strange dark arts.*

And the meaning of that was clear.

*Something that shouldn’t exist appeared in Murim. During the chaos of the Great Faction War, or shortly after it ended.*

If so, the timing lined up exactly. That was when Dark Heaven first approached the Head Elder.

But one fundamental cause remained unknown. The biggest question had yet to be answered.

*The Lord of Heaven.*

The master of Dark Heaven.

No, a being beyond compare, no less than the god they worshiped.

How he could exist in Murim wasn’t what puzzled me. The Great Cataclysm thirty-odd years ago had begun much the same way.

The problem was…

*The Lord of Heaven’s true identity.*

Step.

I suddenly stopped walking.

Darkness shrouded the world, while torches set throughout the Inner Court burned red.

As I stared blankly into their flames, lost in thought, I suddenly felt a shock as if something had pierced through the top of my head.

“Could it be…?”

My voice slipped out like a groan and scattered into the darkness.

Just then—

Swish.

The shadow cast by a wavering torch touched the tips of my feet.

Like someone who had once been a cursed being, someone who no longer existed.

Like someone who had smiled even as he met his eternal Erasure.

And at the same time, a conversation buried in the depths of my memories rang in my ears like an illusion.

*The great king is one who overcame a god’s curse. He may waver, but he will not break; even if he falls, he will rise again. And at last, he will claim all the earth and water in this world as his own.*

*What?*

*That alone is the truth. A truth that cannot be stopped, even when known—a truth that will become reality in the not-too-distant future.*

“……!”

I froze like a statue, as though I’d been transported back to that moment when I’d faced the Doppelganger.
## Chapter artifact 844

# Chapter 844

“Is that it?”

The man who spoke looked to be around thirty at most. An ordinary face, the kind you might see several times in a day while walking through a marketplace.

And yet no one would dare look at him and think he was ordinary.

Because he was standing not in a marketplace, but in a pool of dark-red blood.

“It’s certainly improved, but it’s still nowhere near what I expected…”

Crunch.

The man stepped on an arm half-submerged in the pool of blood and continued.

“Did you call me here just to show me this?”

The owner of the arm? He didn’t know. He had no need to know.

It was just one of countless test subjects, one of the dozens who had met their deaths at his hands here today.

The problem was simply that the man wasn’t particularly pleased with the results of the experiment.

“Anyone with a mouth can speak up, can’t they? Hm?”

In the already icy atmosphere, the black-robed men lined up before him swallowed dryly in silence.

They knew the man before them all too well.

Whenever his temper turned sour, a storm of blood always followed—and some of the black-robed men’s own comrades had been caught in it.

They had witnessed that scene countless times. Who would dare open their mouth?

The silence now was the result of repeated lessons. But the man, for all his rage, wasn’t stupid.

“Hah. Look at you lot. I called you sorcerers and treated you like people, and this is what I get…”

The instant the man let out a quiet laugh, his figure blurred.

Thud.

Flesh and brain matter flew in every direction. One of the black-robed men—or rather, sorcerers—crumpled like a rotten tree, his head smashed to pieces.

Boom.

At the thunderous sound, the sorcerers realized what they had to do at once.

Thump.

They dropped to their knees without hesitation.

Silence wasn’t the only thing they’d learned through repeated lessons.

The sorcerers already knew that no matter how cruel the man was, he didn’t care to spill much blood when it came to them.

“P-please, calm your anger.”

“Blood Lord…!”

The man—the Blood Lord—looked down at the sorcerers crying out as they pounded their heads against the stone floor, his eyes faintly glowing red.

*Vermin.*

He wanted to tear their limbs off right then and there, but the Blood Lord forced down the urge to kill that kept welling up inside him.

*The Western Heaven Demon Lord is dead, and now the Southern Heaven Demon Empress is dead, too. We have to preserve whatever strength we can if we’re to accomplish our great cause.*

Sorcerers were precious, after all. There weren’t many in Dark Heaven who could wield the power of the supernatural, and the research they’d been conducting for many years was finally bearing considerable fruit.

It was just that today’s results hadn’t pleased the Blood Lord.

Once they produced something close to a finished result, its impact would be enough to swallow the whole world.

“Not enough. I said it’s still not enough.”

At the Blood Lord’s abrupt words, spoken as if to himself, the sorcerers bowed their heads even lower.

If it wasn’t enough, they would have to make up the difference somehow. They didn’t want to end up like their comrades who had died before them.

“Blood Lord. If you could tell us which parts you found lacking…”

“Everything. From beginning to end.”

The Blood Lord slowly turned and gestured toward the bodies scattered all around.

“They were all far too weak. And the duration still hasn’t improved at all.”

“We’re also searching for ways to improve it, but our resources are nowhere near enough to increase the potency of both effects at once. The same goes for obtaining the heads of Peak masters.”

The Blood Lord frowned at the excuse-like answer, but this time he had no choice but to accept it.

Peak masters couldn’t be made in a day.

Even in the Central Plains’ great sects, which accepted only the most gifted, it took more than ten years of grueling training to reach the Peak realm.

The time varied according to talent and effort, but that was all. Even demonic, heterodox martial arts, which could be mastered far faster than orthodox techniques, were no exception.

Nothing came easily.

With martial arts that lacked purity and depth, countless people faltered before the wall of the Peak realm.

*Those two were the exceptions.*

The Blood Lord bit his lip, unable to say it aloud.

As he recalled the not-so-distant past, a bloody gleam began to flicker in his eyes.

*Jin Taekyung. Cheongpung.*

At first, he’d thought they were earthworms. Earthworms that would pop if you stepped on them with a little force.

But at some point, those two earth dragons had become heavenly dragons. They’d escaped the mud pit filled with filth and soared freely through the blue sky.

*No. At least one of them was never an earthworm to begin with.*

Even the Blood Lord had to admit it to himself. Comparing Cheongpung to an earthworm might have been too harsh.

The youngest Disciple accepted by Sword Saint Mae Jonghak in his later years.

A martial talent bestowed by the heavens.

Cheongpung was a genius whose equal was hard to find in all of Murim’s history, a man born with the destiny of a dragon.

But…

*What the hell is Jin Taekyung?*

The Blood Lord, who had been behind Jin Yangbaek, Head Elder of the Jin Family of Taiyuan, remembered all too clearly the day he first heard a report about Jin Taekyung, long ago.

He also remembered the first words he’d said to the subordinate who had finished giving the report.

*“Investigate him again.”*

*“Pardon?”*

*“How can a piece of shit like that exist? He must be hiding something.”*

It was only natural.

His martial arts were worse than those of a Third Rate street thug, and he even had a schedule laid out for wandering around every pleasure house in sight.

If the eldest son, who struggled to raise the crumbling family back up, and the second son, who trained day and night, were the pillars of the Jin Family of Taiyuan, then Jin Taekyung was gnawing away at the remaining pillars from the roots up.

An earthworm, plain and simple.

No—a bug.

But one day, Jin Taekyung changed.

Unlike Cheongpung, Jin Taekyung had been born a bug. Then he became an earthworm, then a venomous centipede, then an imugi, and finally a dragon.

And when the Blood Lord understood the whole process, he couldn’t hide his astonishment.

*That bastard has already gone beyond common sense. By a mile.*

Cheongpung was born with the destiny of a dragon. So there was nothing strange about him being called one now.

But unlike Cheongpung, Jin Taekyung had not been granted the destiny of a dragon by the heavens.

He had been nothing but a bug, an earthworm. The only thing he could do was writhe when stepped on.

That should have been all he could do.

Throb.

The Blood Lord clenched his teeth as a sudden pain struck him.

He looked down and saw both arms, still attached and whole. Once severed by someone’s purplish Force, they had since grown back even stronger—but now they were trembling slightly.

Was it fear? No. This was anger.

And, at the same time, pain and humiliation etched into his soul.

*If Jin Taekyung hadn’t gotten in my way…*

Grinding his teeth, the Blood Lord remembered that day.

Jin Taekyung, drenched in blood, clinging to his ankle and refusing to let go—and the Sword Saint Mae Jonghak’s Force sweeping across his arm.

But what had been harder to bear than the pain was the ridicule of others.

Though two of them had already become lonely spirits.

*Western Heaven. Southern Heaven. Watch closely from wherever you are. I’ll accomplish what you two failed to do.*

The Western Heaven Demon Lord and the Southern Heaven Demon Empress had been powerful figures whom even the prideful Blood Lord couldn’t dismiss.

Their deaths were an enormous loss to Dark Heaven, but they had left him with two lessons.

First: never let his guard down when facing Jin Taekyung.

Second: to help the Lord of Heaven accomplish the great cause, he needed even greater strength and effort than before.

“Spread them.”

“What?”

The Blood Lord looked at the sorcerers, who had instinctively questioned him.

The faint red light in his eyes had gone cold.

“Now that the Great War has begun, we need to gather as much strength as we can. We can’t keep using Peak masters on experiments like these forever.”

“You mean…”

“I understand that you’ve already planted seeds throughout the Central Plains. Am I wrong?”

The head of the sorcerers bowed deeply.

“No. Some of the seeds have already blossomed.”

That was true.

Dark Heaven had created the “seeds” through vast sums of money and years of research, then scattered some of them throughout the land long ago.

Some had gone to Henan and Shaanxi, the heart of orthodox Murim; others to the border regions of Guangxi and Guangdong.

Or… to the northern plateau bordering Shanxi Province.

They were both experiments and a way to cause chaos in Central Plains Murim. Just a month ago, one had even shaken an entire city.

No—more precisely, it had *almost* shaken one.

“You failed spectacularly in Guangxi Province.”

“That was…”

“I know. If the Fire King—that old man—hadn’t happened to show up pretending to be a bald monk, it might have worked.”

The unorthodox faction’s uprising in Guangxi Province had been no coincidence.

The one who possessed a “seed” had gathered forces and even taken control of half of Guangxi.

At least, until his head was smashed by Jeok Cheongang, who had concealed his identity under the sobriquet Blood Monk.

“However, those were failures made before we improved their potency. If the ones we have now were to fall into the wrong hands…”

“It doesn’t matter.”

The Blood Lord cut off the sorcerer, who feared the blade might turn against them, and continued.

“Choose those fit to become seeds and bury them deep. Make sure they can be spread whenever the time comes.”

At the Blood Lord’s words, the sorcerers realized there was no room for further excuses.

Only two paths lay before them now.

Submission. Or death.

The Blood Lord wasn’t wrong, so they had no choice but to choose the former.

“We obey.”

The Blood Lord’s eyes flashed as he looked down at the sorcerers bowing deeply.

His conversation with the Lord of Heaven, who had awakened without warning from a long slumber just ten days ago, was etched clearly in his mind.

*“The time has come.”*

*“Lord of Heaven, what do you mean?”*

*“The world is twisting. Now… bring down the heavens.”*

The Blood Lord took a deep breath.

The Lord of Heaven had fallen asleep again after giving a single command, and had given his faithful servant an unbelievable opportunity. A chance, in the name of the Lord of Heaven, to draw the bowstring.

And at this very moment, the Blood Lord instinctively knew.

Now was the time to let the arrow fly.

“Send out missives.”

That day, dozens of hawks with black feathers took to the sky.

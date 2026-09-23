# Checkpoint Review — 890–894

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

# Chapters 890–894

## Plot

Taekyung evades attention near the Inner Palace with Ma Sanbao’s help, then reaches Jeok Cheongang’s pavilion and rejoins the Fire Dragon Pavilion group. He briefs them on the imperial crisis. They discuss So Gyo, the enemy’s apparent confidence despite Jeok’s strength, and the possibility that the coming banquet will bring a decisive battle. Their discussion turns to Ma Sanbao’s hired assassins and the old assassin Taekyung encountered, who may be the famed One-Legged Ghost Killer. Troubled by joining forces with a killer, Taekyung leaves to question Ma.

After Taekyung departs, Jeok tells the group that Hong Dao foresaw an approaching calamity and named Taekyung the Morning Star who would keep shining through the darkness. Jeok says his own cause is to protect those he still has and make good choices, and vows to stay at Taekyung’s side. In a hidden palace refuge, Ma Sanbao confirms he hired the assassins and offers to explain either that decision or So Gyo.

## Continuity

- The grand banquet is approaching, and the group expects a possible decisive battle there. The enemy’s confidence that it can win remains unexplained; the restoration army has spent more than a decade preparing for the coup.
- Ma Sanbao confirms he hired the assassins. His reasons remain unknown; he also offers to explain So Gyo.
- The old assassin Taekyung encountered may be the One-Legged Ghost Killer, a famed Qinghai assassin reputed to have killed a Supreme Peak Kunlun Elder. The identification is uncertain; the assassin is currently an ally and is expected to fight alongside the group.
- Taekyung is troubled by the alliance with the assassin and recognizes that he has killed without seeking alternatives; he is trying to become better.
- Hong Dao foresaw an unknown calamity and identified Taekyung as the Morning Star, whose light would persist through the coming darkness.
- Jeok Cheongang believes there is no absolute justice in Murim. His cause is to protect those he still has and try to make good choices; he will support Taekyung whatever path he chooses.
- The Divine Physician says his Master, the former Slaughter Saint, destroyed Salcheonmun because its members felt no regret or remorse for their deeds.
- So Gyo is identified as a highly skilled flexible-sword user serving Dark Heaven; her age and reasons for releasing Taekyung remain unknown.

## Translation Decisions

- Use “Morning Star” for 신성 and “master of the Morning Star” for 신성의 주인, referring to Taekyung.
- Render both 독각귀살 and 독각살귀 as “One-Legged Ghost Killer”; they refer to the same possibly identified assassin.

## Durable state

{
  "active_continuity": [
    "The grand banquet is approaching, and the group expects a decisive conflict may occur there.",
    "The enemy sees a decisive battle as the quickest route to controlling the Great Nation, but its confidence remains unexplained.",
    "The restoration army has spent more than a decade preparing for the coup.",
    "The old assassin Jin encountered may be the One-Legged Ghost Killer, a famed Qinghai assassin; Namho says the identification is uncertain and the man is currently an ally.",
    "Jin is troubled by the alliance with the old assassin and intends to ask Ma Sanbao why he brought the assassins into the cause.",
    "Jin recognizes that he has killed people without seeking alternatives and is trying to become better.",
    "The Divine Physician says his Master destroyed Salcheonmun because its members felt no regret or remorse for their deeds.",
    "Hong Dao foresaw an unknown calamity and identified Jin Taekyung as the Morning Star, whose light would persist through the coming darkness.",
    "Jeok Cheongang sees protecting those he still has as his cause and will support Jin whatever path he chooses.",
    "Ma Sanbao confirms that he hired the assassins; his reasons remain unknown."
  ],
  "continuity_sources": [
    893,
    894
  ],
  "open_questions": [
    "What accounts for the enemy's confidence that the decisive battle's outcome is assured?",
    "Why did Ma Sanbao hire the assassins and bring them into the cause?",
    "Is the old assassin Jin encountered truly the One-Legged Ghost Killer?",
    "What will happen at the approaching grand banquet?",
    "Who is So Gyo, and why did she release Jin?"
  ],
  "safe_through": 894,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 890

# Chapter 890

Clank. Clank.

Heavy footsteps drew closer, accompanied by the distinctive metallic clatter of heavy armor.

Hidden in the darkness just thirty feet away, I felt my heart seize up at Jeong Hogun’s sudden appearance.

*What the hell are you doing here…?*

I didn’t know why a Thousand Captain of the Embroidered Uniform Guard, responsible for the Inner Palace, was wandering around all the way out here. But one thing was certain:

At this distance, if I made even a clumsy move, Commander Jeong could spot me.

*Damn it. If I’d known this would happen, I should’ve learned the concealment technique properly first.*

Regret washed over me, but it was far, far too late for that.

I’d struggled tooth and nail to survive in Murim, and that was how I’d met Jeok Cheongang. Then, after inheriting the Fire Gate Clan’s legacy, a good old-fashioned brawl had become both my only major and my general-education requirement.

What kind of sect was the Fire Gate Clan?

Just look at the records of its past Sect Leaders. Every last one of them was a no-holds-barred tough guy. The kind of lunatic who looked like he’d take a shit standing up.

For three hundred years, this thoroughly established hipster sect had picked fights without distinguishing between the orthodox, unorthodox, or demonic paths. In a place like that, the concealment technique was practically a symbol of weakness.

One of the Fire Gate Clan’s Sect Leaders, said to have been the greatest master in the world some two hundred years ago, had even left behind this record:

> Want to learn the concealment technique?
>
> Then you’re a homosexual.

Behold the audacity of dismissing one of Murim’s essential survival skills as a martial art for fags.

If he’d said something like that in the twenty-first century, he’d have been beaten half to death with rainbow-colored clubs. But whether by good fortune or bad, this world was Murim, steeped in barbarism—and the Fire Gate Clan’s lineage had carried on uninterrupted.

The problem was that, thanks to the fine policies of those ancestors, I was the one about to get screwed now.

*Seriously, shit. In three hundred years, couldn’t one Sect Leader have learned the concealment technique?*

My lips were drying out. Maybe it was the nerves, but I was starting to need to piss.

Jeong Hogun had now come within ten feet. His expression hard, he was interrogating the Imperial Guard soldiers who’d neglected their duty.

“Answer me. Why did you leave your assigned post?”

“S-Sorry, sir. The rain was so heavy that we were shivering…”

“Would you say the same thing if someone harboring treasonous intentions slipped into the imperial palace undetected?”

“Of course not. We truly regret it, but…”

“Enough excuses. Who is your immediate superior?”

“W-Well, that is…”

“You don’t want to say? No, given how carelessly you’ve been doing your duty, perhaps you didn’t want to serve in the Imperial Guard at all?”

“N-No, sir!”

“Then is this the inside or the outside?”

“……?”

“……?”

What was this? It reminded me of Hunter boot camp.

*Is this bastard a System user…?*

As I watched the scene with my presence hidden as much as possible, entertaining a reasonable suspicion about Jeong Hogun, one remark made me doubt my ears.

“As of today, you are no longer members of the Imperial Guard. Go to your superiors immediately, report what happened here, and return your badges, uniforms, weapons, and the rest. I will guard this post myself until your replacements arrive.”

“……!”

“……!”

It was like a bolt from the blue.

For the soldiers who’d only taken shelter from the rain beneath the eaves—and for me, who’d been waiting with bated breath for Jeong Hogun to leave.

“G-General!”

“Military law is strict. This is an order from me as a Thousand Captain of the Embroidered Uniform Guard.”

No. Don’t listen to him.

You’re civilians now anyway. Just punch him once.

I fervently cheered on the middle-aged reservists—I mean, the Imperial Guard soldiers—but the two men who’d just been sent through the process of discharge still had a shred of reason left.

In the military, when they tell you to jump, you ask how high. And the Embroidered Uniform Guard was the place that could even cut off the heads of the highest officials—the sort who could make a flying bird drop from the sky.

Only two kinds of people could tell him to go to hell in a situation like this:

Lunatics. Or people hoping to join the Fire Gate Clan.

Unfortunately, the two men standing before Jeong Hogun were neither. They were perfectly normal.

“We’ll… obey your order.”

They answered in weak voices, pulled their rain hats low, and trudged off somewhere.

Or, to be precise, they tried to.

Just as with Jeong Hogun a moment ago, someone entirely unexpected appeared.

“How strange. Since when has the Embroidered Uniform Guard been able to dismiss Imperial Guard soldiers on a whim?”

Swish.

A long robe brushed across a puddle. Amid the endless sheets of rain, a figure emerged. Jeong Hogun was silent for a moment, then spoke.

“Eunuch Ma, what brings you here?”

“Nothing in particular. I was taking care of something outside and am on my way back. But…”

He, Ma Sanbao—the East Depot’s second-in-command and its de facto leader—smiled faintly before continuing.

“Could I have an answer to my earlier question, Commander Jeong?”

“……I was only enforcing military law.”

“Of course you were. I know what a fine and capable man you are. But…”

At that moment, Ma Sanbao’s voice, which had always seemed to hover somewhere between a man’s and a woman’s, dropped low.

“Follow procedure. Follow procedure.”

“That’s…”

“Even if the Embroidered Uniform Guard outranks the Imperial Guard, there’s still a proper process to follow, isn’t there? The authority to impose a final punishment clearly belongs to their superiors. That’s the military law you mentioned.”

“……!”

“That’s all I have to say. Is there anything else?”

Jeong Hogun gazed at Ma Sanbao in silence, then spoke.

“No.”

“Good. Since we’ve run into each other, why don’t we go together for a while?”

“Go together?”

“Yes. It’s been quite some time, and I’m glad to see you. I also have something important to discuss with you. You’re heading back to the Inner Palace anyway, aren’t you?”

Jeong Hogun had probably meant to answer, “No,” or “Now isn’t a good time.”

Despite his expressionless face, for just an instant his profile revealed his wariness and aversion toward Ma Sanbao.

But in the end, Ma Sanbao was half a beat faster.

“Oh, you don’t mind? Good. I knew you’d say that.”

Even though the East Depot’s authority had been curtailed after the rebellion more than a decade ago, and the Embroidered Uniform Guard had risen to prominence, Ma Sanbao was still the East Depot’s de facto leader, standing in for the seriously ill Cang Gong, who’d been confined to bed for a long time.

He smoothly seized the initiative before Jeong Hogun could get a word in, then smiled slyly and patted him on the shoulder.

“Come along. There’s plenty to tell the Embroidered Uniform Guard—and plenty to hear from them.”

Ma Sanbao was a Supreme Peak master and a skilled politician. For Jeong Hogun, who was all but a martial artist through and through, he was the worst possible opponent.

Having lost control of the conversation in an instant, he could only leave with his face rigid as a rock, following Jeong Hogun.

Not before leaving a stern warning for the two Imperial Guard soldiers who’d escaped the threat of a surprise firing, though.

“As soon as your shift ends, report what happened here to your superior. Understood?”

“Y-Yes, sir.”

“Understood!”

Of course they’d say yes now.

As I listened to the two soldiers, suddenly standing ramrod straight, give their hearty salute, Jeong Hogun turned away. I was breathing an inward sigh of relief when a strand of Sound Transmission reached my ear.

—I don’t know exactly why you’ve come all the way here, but there are many eyes watching. Be careful and use your wits. I’ll send word to you myself later.

“……!”

I whipped around. Ma Sanbao was looking this way and winking.

*He knew. From the beginning.*

It startled me a little, but when I thought about it, it made sense.

Ma Sanbao was a master of the concealment technique who’d reached the Supreme Peak realm. He might not be as skilled as the Slaughter Saint, hailed as the greatest assassin of all time, but he was more than good enough to notice my amateurish trick.

*Did he expect me and come looking? Or was it just a coincidence?*

Who knew?

I didn’t know why he’d appeared here. Or how he’d gotten the assassins of Murim involved.

But what mattered to me right now was that the remaining Imperial Guard soldiers weren’t skilled enough to detect my presence.

Whoosh.

I moved like a shadow through the thick darkness.

With the help of the relentless rain and the thunderous crashes of lightning.

After leaping over several pavilions and walls, I picked up a timely hint from a conversation between some other Imperial Guard soldiers.

“Did you see ‘that guy’?”

“Who? Oh, I think I know who you mean. He’s a monster, all right.”

“I thought he was just big, but he really does eat an insane amount. Especially five-spice pork. It hasn’t even been half a shichen, and he’s already eaten more than twenty plates. The cooks are making a fuss.”

“Good grief. I’d heard a little about it, but that much?”

“He’s a lunatic, I’m telling you. At this rate, they say he’ll eat every pig in Zhejiang Province with that mouth of his within a month. He looks like he’s got a pigsty in his stomach.”

“That’s impressive. But at that point, wouldn’t it be better to kick him out?”

“The imperial family has its reputation to consider. They can’t treat people brought here for the grand banquet poorly just because they eat a little pork. Orders have already been given to provide them with whatever they need for lodging and meals.”

“Good grief…”

They hadn’t even used his name. Just *that guy*.

Why was I embarrassed on his behalf?

*Taishan, you bastard…*

I sighed toward the heavens, then spotted a group of people hurrying somewhere.

There were more than ten of them, each carrying a large plate.

And, last of all, the rich smell of five-spice pork—strong enough to clear the nose of someone with sinusitis.

“……!”

I’d only known that the group was staying somewhere in the Outer Palace. I had no idea where they’d been assigned rooms. Who knew things would work out like this?

*Is this for real?*

I followed them like Hansel and Gretel, quietly enough that no one could notice.

And listened as a middle-aged man who looked like one of the cooks rattled off a string of curses.

“Please, just stop eating already. If you’re even human, for the love of—”

At that moment, I saw it clearly.

In his other hand, the large kitchen knife trembled.

* * *

“Food’s here.”

Creak—BANG!

The door to the pavilion flew open with a rough shove, and the Fire King, Jeok Cheongang, was surprised twice.

First, that a middle-aged cook who clearly hadn’t learned martial arts was giving off genuine killing intent.

Then, that behind the cook and his exhausted companions, who’d come carrying bundles of food, a familiar face was poking its head out from the darkness.

“Y-You…”

“What is it?”

“N-Nothing.”

“If it’s nothing, then take some of the food. My arms are about to break.”

The middle-aged cook answered sharply, then had the palace attendants who’d come with him set down the plates before leaving.

Not before warning them that if they ordered five-spice pork one more time today, he’d poison it.

And as soon as they were gone, a breeze from somewhere blew the door they’d just closed open again.

At least, that’s how it would have looked to anyone else.

“What are you waiting for? Get in here.”

At the Fire King Jeok Cheongang’s abrupt command, a young man suddenly appeared from the darkness and grinned.

“I’m here.”
## Chapter artifact 891

# Chapter 891

It had only been a few days—not long enough to call this a reunion—but it was still good to see everyone again.

And “a few days” was only on paper. It had felt more like a few months.

*There’d been so much going on.*

Still, how should I put it? Seeing familiar faces made this strange place feel, for a moment, like home. I liked that.

I smiled and waved at the group that had rushed over to me.

“Wow, it feels like ages since I’ve seen you all. How’ve you been?”

The reactions came at once.

Jeok Cheongang snorted as if nothing had happened, asking why I was making such a fuss when he’d already seen me a few shichen ago. Sama Pyo and Song Ilseom silently nodded. Ju Hwaran, who’d frozen like a statue when I suddenly appeared, came flying down the stairs in a flash. Her voice unsteady, she said,

“Y-You… Benefactor. No, Pavilion Master. Are you hurt anywhere?”

“Huh?”

“N-No, that’s not it. I misspoke. What I mean is…”

“You’re asking if I’m hurt?”

“Ah. Yes!”

The Divine Physician had come closer without my noticing. He chuckled warmly.

“I’m glad you don’t seem to have suffered too much. Young Lady Ju here can finally breathe a little easier, too.”

Ju Hwaran flinched.

“Me?”

“Is that not so? You seemed more worried than I was, and I’m the physician.”

“Th-That’s… As a member of the Fire Dragon Pavilion, isn’t it only natural that I’d worry about the Pavilion Master’s safety?”

“Ah, of course it is. Quite right.”

The Divine Physician nodded like a grandfather agreeing with his granddaughter, then winked at me.

“So she says.”

“Uh…”

What on earth was I supposed to say in this situation?

I felt strangely awkward and was frantically searching for something to say when a shadow suddenly fell over me. At the same time, something damp touched the crown of my head.

Plop. Plop.

For an instant, I thought rain was leaking through the ceiling. That was before I heard the rough breathing behind me and felt the sticky saliva.

*Oh. You bastard.*

I didn’t need to look to know who it was. I glanced up, and there he was, drooling exactly as I’d expected.

“Taishan is very, very happy and glad to see the Pavilion Master again.”

Was this lunatic for real? Look how fast he was talking.

“Pavilion Master doing well Taishan doing well Taishan ate five-spice pork and ate five-spice pork and ate five-spice pork.”

So all he’d done was stuff his face.

Even now, he wasn’t looking at me. He was staring at the mountain of plates piled in one corner.

“Taishan has finished preparing everything to help the Pavilion Master just give the order.”

“……”

He’d clearly finished preparing to eat five-spice pork, so I gave the order in a voice drained of all hope.

“Fine. Eat it before it gets cold.”

“Taishan will obey the Pavilion Master’s command!”

With an answer more enthusiastic than ever, Taishan hurled his massive body forward and began slaughtering the five-spice pork.

I watched the horrific scene through half-lidded eyes, then suddenly remembered someone I’d forgotten.

“Wait. Where’s Elder Namho?”

“I’m here.”

Namho came clomping down the stairs, one hand on his lower back, his face gloomy.

“I was resting for a moment. Maybe it’s because I’m old, but my body’s not what it used to be.”

“What happened? Did you hurt yourself?”

“I went to the privy, and then…”

“Oh no. Did you slip?”

“Palace privy or not, the place might as well have been greased. I was hanging on to a ceiling beam when my strength gave out.”

“The ceiling beam? Not the floor?”

The Divine Physician whispered to me as I stared at him in confusion.

“I believe he hid in the privy to ambush Young Hero Taishan.”

“……”

“He’ll be fine soon. He may be old, but he’s in excellent shape.”

This was a complete shitshow. Seriously.

I let out a deep sigh and looked around at the people gathered in a circle around me.

Some were normal, some weren’t, but they’d all followed me into the imperial palace—a tiger’s den—for my sake.

They knew how dangerous this mission was, and they’d risked their one and only lives. When discussing what to do, I couldn’t hide or lie about a single thing.

“I can’t stay away from my post as long as I’d like, so I’ll keep this quick.”

I took a quiet, deep breath and began to speak.

Or, I tried to.

Chomp. Chomp. *Pah-ooh.*

“……”

Please, stop eating.

* * *

As soon as I finished pouring out everything that had happened over the past few days, a hushed silence settled over the pavilion.

It made sense.

They’d already learned about some of it through the East Depot, but there were things they were hearing for the first time here.

The first to break the silence was Jeok Cheongang.

“This has gotten one hell of a mess.”

He muttered under his breath, his gaze sinking darkly.

“Six Supreme Peak masters, and Embroidered Uniform Guards of that caliber… Is this what they mean when they call it a Great Nation?”

I corrected him with a heavy heart.

“That’s only what I saw for myself. They could have other masters hidden away.”

“Hah.”

Murim and the government might look as though they were kept completely separate, but the truth was different.

A Great Nation meant a continent. The forces hunkered down in the imperial capital were so powerful that even Jeok Cheongang had to groan.

And there was another unexpected wild card.

“First, tell us more about that woman called So Gyo. Her appearance, her way of speaking. What weapon she uses and how she moves.”

Jeok Cheongang seemed more wary of So Gyo than anyone else. I told them everything I’d seen and felt myself, even going into detail about her movements during our brief clash.

Yet even Jeok Cheongang, who was among the three oldest in the martial world, and Namho, whose knowledge was second to none, couldn’t offer a clear answer.

“Her manner of speaking doesn’t give us much to go on. But I’ve never heard of a master with that appearance who uses a flexible sword.”

“I agree with Senior Jeok. If she’s serving Dark Heaven, she must be one of the demonic or heterodox martial artists. But even among the fiends the Hidden Shadow Pavilion identified during the Great Faction War, women of that caliber were very rare.”

Namho replied in a worried voice, then turned to me.

“Did you notice anything strange? We can’t rule out the possibility that she was using a finely crafted human-skin mask or a disguise technique.”

I tried to recall what I’d seen, then shook my head.

The higher one’s martial arts realm, the sharper one’s eye became.

No matter how well made a human-skin mask was, it had its limits. And maintaining a disguise technique took a constant supply of internal energy. From what I’d seen, I hadn’t felt the slightest trace of anything like that.

“No. At least, from what I felt, it didn’t seem like she was using either of those methods.”

“But we can’t rule out the possibility…”

“Enough. If that boy says so, then that’s how it is.”

Jeok Cheongang had walked the same path I had, and gone farther down it. His understanding was beyond anything Namho, who hadn’t learned martial arts, could match.

After cutting Namho off firmly, Jeok Cheongang slowly stroked his chin.

“She has a supreme footwork technique and has reached Returning to Simplicity. How old did you say she was?”

“Maybe thirty? She looked no older than her mid-thirties at most.”

“To reach that level of martial prowess around thirty is impossi—”

Jeok Cheongang met my eyes and trailed off.

“—not impossible, but about as close to it as you can get.”

“Why are you looking at me like that while we’re talking?”

“When did this old man do that?”

“Just now.”

“Do you want to get your ass kicked?”

“No.”

“Then shut up.”

“Yes, sir.”

So this was how Hyuk Mujin felt.

*Sorry. I’ll treat you better when we get back.*

I kept quiet, chastened, and Jeok Cheongang downed a cup of cold water in one go before clicking his tongue.

“Damn it. It’s one of two things. Either the Lord of Heaven took some once-in-a-millennium prodigy as his Disciple and raised her all this time, or she’s an old monster who’s gone beyond Returning to Simplicity and Returned to Youth.”

“Personally, I think it’s the latter. The Southern Heaven Demon Empress was the same.”

“That’s probably more likely. Even when the world was shaken by the Great Faction War, there were people living in seclusion in remote mountains and valleys. This old man was one of them. There’s no guarantee that the woman called So Gyo wasn’t, too.”

It was a perfectly plausible explanation.

Nearly half a century had passed since the old sky of the Demonic Cult closed and a new one, Dark Heaven, opened.

Many of the people who’d emerged under Dark Heaven’s command in the present day were old masters from a previous generation, the kind known as fiends. But key figures like the Blood Lord, the Western Heaven Demon Lord, and the Southern Heaven Demon Empress were people the world hadn’t known about at all.

*So it makes sense that So Gyo belongs in the same category.*

But there was something more important than discovering So Gyo’s identity.

Why had she let me go when she could have subdued me?

No matter how much I thought about it, I couldn’t find an easy answer.

“I don’t know. Why did So Gyo go out of her way to make that choice?”

Ju Hwaran, who’d been listening without a word, suddenly spoke up.

“I haven’t been able to understand it either. This may be rude to the Pavilion Master, but… why let a fish that’s already been caught in the net go free?”

“Perhaps they intend to catch us all at once at the grand banquet that’s coming up.”

Song Ilseom, seated beside her, answered. Ju Hwaran shook her head.

“If the information got out, it would be a problem for them instead. Now that they’ve made this move, wouldn’t we fight the decisive battle with everything we have?”

She was right.

It would’ve made sense if the people gathered here were the entirety of our side’s forces. But the restoration army that had spent more than a decade preparing under Ma Sanbao’s leadership was no joke either.

*If they didn’t have a chance of winning with their forces, they never would’ve dreamed of staging a coup in the first place.*

So did the enemy know nothing about this?

Of course not.

The current Emperor had gradually reduced the East Depot’s authority as soon as the rebellion succeeded. That was practically proof that he’d kept it in check because he’d been worried about a situation like this.

*The Embroidered Uniform Guard is no weaker than the East Depot in either force or intelligence. They must have been keeping a close watch, too.*

At least, that was the impression I’d gotten of the Emperor.

Thorough, calculating, and someone who would always uproot a future source of trouble.

A cold and ruthless ruler. The master of a continent with the power to match.

It was hard to explain why someone like that had stood by and let all this happen.

Unless there was only one possibility.

*He’s certain. No matter what we try, no matter how desperately we fight, the outcome won’t change.*

You could trample weeds again and again, and they still wouldn’t wither.

But pull out every root in one go, and the weeds would finally be gone.

*Damn it.*

The air sank heavily around us.
## Chapter artifact 892

# Chapter 892

I’d faced countless formidable enemies and fought more battles than I could count, but this was a first.

For me—and for everyone else.

“They’re planning to raise the stakes even further… If that guess is right, they’ve got to be completely insane.”

At Jeok Cheongang’s mutter, Namho nodded.

“It’s hard to believe, but for our enemies, it is the fastest shortcut to taking control of the entire Great Nation.”

He was right.

Nothing was more decisive than an all-or-nothing match. Once a single battle with everything on the line was over, the winner would survive, and the loser would disappear.

The problem was that we had no idea what lay behind our enemies’ confidence.

*Where the hell are they getting that confidence?*

It was easy to call it a single decisive battle, but this wasn’t just another life-and-death duel of the kind that happened all the time between martial artists.

It would be an enormous battle with the fate of the Great Nation at stake—and, without a doubt, a bloodbath that would paint the imperial capital red.

*If we lose this battle, the restoration army will be wiped out in an instant, and Dark Heaven and the Emperor will take complete control of the Great Nation. But is that really all?*

Namho had said it earlier.

That this was the fastest shortcut for the enemy.

But the shortcut wasn’t always the best choice. There was a reason people took the established road.

A main road was wide and straight. Even if it took a little longer, you could reach your destination easily and comfortably.

A shortcut, though, was narrow and complicated. The ground was uneven and unpaved, and sometimes you had to pass through shadowy alleys where danger—and foul smells—lurked.

*And yet the enemy chose the latter. They even used me as bait to do it.*

Even if it was for the sake of the bigger picture, a series of choices like these seemed almost reckless.

They hadn’t stopped me, even though I’d repeatedly gotten in Dark Heaven’s way. They’d deliberately made a battle they absolutely had to win that much harder.

And I wasn’t the only one thinking about it.

“Why?”

Jeok Cheongang rose and paced around, muttering as if to himself.

“Even if they didn’t know this old man was in the imperial palace, they should have at least considered the possibility if they knew what happened in Nanman.”

Dark Heaven’s intelligence network was vast. There was no way So Gyo or the Emperor hadn’t heard what even Ma Sanbao knew.

For all I knew, they’d obtained that same information themselves.

That Fire King Jeok Cheongang had intervened in the process of defeating the Southern Heaven Demon Empress, and had left Nanman with me.

And still, they’d let me go.

As if they hadn’t even considered the existence of a predator called the Fire King. As if even if that predator joined the battle, it wouldn’t make the slightest difference to the outcome.

*This… really is strange.*

No, more than strange. Suspicious.

I could understand why they might discount me: I was already in rough shape, and they might have been acting on some kind of instruction from the Lord of Heaven.

But Jeok Cheongang?

He’d already stood at the top of the Ten Kings during the Great Faction War. They said that if he’d joined the war a little earlier, he could have stood shoulder to shoulder with the Three Saints. He was a monster among monsters.

*Without the Blood Lord’s impossible ability to recover, he would’ve died instantly several times over. And during the Sichuan Blood Tragedy, he fought the Western Heaven Demon Lord with a body that had only just recovered from being poisoned.*

Of course, the Southern Heaven Demon Empress, the most recent opponent he’d faced, was an exception.

The magical power flowing from the rift had turned her halfway into a monster. And after burning her innate qi, she’d displayed a level of martial prowess beyond human limits.

But they weren’t even considering Jeok Cheongang?

*Bullshit.*

I stared into the air, my gaze sinking as I thought.

The more I considered it, the more things didn’t add up.

There was definitely something going on.

Something I didn’t know yet. A secret no one had uncovered.

And I knew one person who might help answer at least some of these questions.

“Ma Sanbao.”

At the name that slipped from my lips, Namho nodded as if he’d caught on.

“You’re going to see him?”

“Yes. I think he’d know more about what’s going on.”

“Right. The East Depot’s Brush-Holding Eunuch is famous for his resourcefulness. I suppose that’s why he’s been in charge of the East Depot for the past decade or so, acting as its de facto head.”

Mentioning Ma Sanbao brought something else to mind.

I brought up a question I’d set aside for later.

“Has the Hidden Shadow Pavilion ever gathered information on the East Depot? Or on anything else concerning the imperial household?”

“I spent all my time holed up in Nanman, so I don’t know the details. But I’ve heard that they did quite a bit of that in the past.”

“How far back?”

“Quite a while ago. Around the time of the Great Faction War… That was nearly fifty years ago now. Time really flies.”

Fifty years.

Half a century.

As the years went by, the land and its people grew old.

Namho, one of the countless people swept along by that current, patted his lower back and continued.

“When the Demonic Cult swept down into the Central Plains, the Murim Alliance was formed. The Hidden Shadow Pavilion was established in the process. Where do you think we reached out first?”

“You mean…”

Namho grinned as he watched me hesitate.

“That’s right. The place you’re thinking of. The imperial household.”

“…”

“Put simply, the Hundred Thousand Demonic Disciples amounted to an army of a hundred thousand invading from a foreign land. What’s more, unlike the Central Plains, they had a perfect center of command.”

“They did. The Heavenly Demon, that son of a bitch.”

Jeok Cheongang cut in, and Namho nodded.

“The problem was, that son of a bitch was effectively their king—or rather, practically a god.”

That was why the Great Faction War had been so fierce, and why it had ended so quickly.

Unlike the orthodox faction, whose martial world was made up of people loyal to their own schools and leaders, those who followed the Demonic Path obeyed only one person: their Cult Leader, the Heavenly Demon.

It wasn’t for nothing that people still said the world would have belonged to the Demonic Path if the orthodox faction hadn’t had a new center of command in the Martial God, and if its symbolic masters—including the Three Saints and the Ten Kings—hadn’t fought so fiercely.

And to drive out the Heavenly Demon and his hundred thousand disciples, the Murim Alliance must have needed a powerful ally.

“So the Alliance reached out to the imperial household? To drive out the Heavenly Demon together?”

“That’s right. If the Great Nation helped us, everything would’ve been much easier.”

Namho added bitterly,

“Of course, the imperial household tested the waters for a while, then spat the idea out.”

By this point, I was so curious that I couldn’t help asking more.

It was a little off from what I’d originally wanted to discuss, but I wanted to know why the imperial household hadn’t intervened in the enormous battles that had erupted across the land during the Great Faction War.

“Why did they refuse? If a hundred thousand members of the Demonic Cult had invaded the Central Plains, surely the imperial household could’ve stepped in.”

“I heard the late Emperor, who was the Son of Heaven at the time, opposed it personally.”

“The late Emperor?”

“That’s right. Several high ministers submitted memorials, but the young Emperor, who had only just ascended the throne, firmly shut his ears. The Great Nation had been founded less than twenty years earlier, so he said he needed to take care of the people.”

At Namho’s words, Jeok Cheongang snorted.

“Of course, that’s a load of convincing-sounding bullshit.”

“Senior is right. They didn’t want to risk the people’s displeasure by mobilizing troops again, and they couldn’t bear the cost of the damage. They trusted the orthodox Murim to act as a shield, then sat back to enjoy the show.”

“It was a foolish, indecisive choice. If the Demonic Cult had won the Great Faction War, the imperial household would’ve been next.”

“The Hidden Shadow Pavilion came to the same conclusion. The Heavenly Demon was strong and ambitious. In the end, he would have brought down the Great Nation and established a theocracy. But as always, history is determined by its outcome, isn’t it?”

Namho nodded and turned to me.

“After that, things went as everyone knows. The Heavenly Demon also didn’t want the imperial household to get involved, so his forces advanced deep into the Central Plains while avoiding harm to ordinary people as much as possible. After more than a decade of fierce battles, the orthodox faction won by a miracle.”

“That’s it?”

“What else would there be? Oh, if I had to add anything, there are a few things people don’t know. The indecisive young Son of Heaven, who’d only been afraid of war, became a sage king who’d protected the people through yet another conflict. And he ordered the East Depot and the Embroidered Uniform Guard to keep an even closer watch on martial artists.”

“…”

“That’s all. The imperial household had nearly been burned by an incident in the martial world, so in a way, it was only natural. After that, the Hidden Shadow Pavilion couldn’t send agents into the imperial capital anymore. If the imperial household spotted and exposed them, we’d have to fight the Great Nation instead of the Demonic Cult.”

After hearing about a past unknown to the world, I—and the other members of the Fire Dragon Pavilion—fell silent for a moment.

Even Taishan, who’d been quietly slaughtering the five-spice pork, was blinking. There was no denying it was a shocking story.

“Why are you only telling us this now?”

“Because it’s in the past. We’re busy enough focusing on the present without dragging up old, dusty matters.”

Namho shrugged, then suddenly furrowed his brow.

“Wait, how did we end up talking about this? What was it you asked me at first?”

“I asked whether the Hidden Shadow Pavilion had ever gathered information on the East Depot. It didn’t have to be the East Depot specifically—anything about the imperial household.”

“Oh, right. That’s what it was. Why did you ask?”

“Because I learned something a little unsettling a few shichen ago.”

“Something unsettling? Is it connected to the East Depot?”

“Yes. More specifically, to Ma Sanbao. Eunuch Ma.”

“If your ass feels dirty, you wipe it—even if you have to use your bare hand. Now tell me.”

Jeok Cheongang said something filthy in an unnecessarily solemn tone, his eyes gleaming. Under the many gazes fixed on me, I slowly began to speak.

“Is there anyone Ma Sanbao might personally bring in from the martial world?”

“People from the martial world? Which sect?”

“I don’t know what sect they belong to. And they’re not exactly ordinary martial artists, either.”

“What on earth are you talking about?”

“They’re assassins.”

“…”

At that moment, the gazes that had been fixed on me split in two directions.

One toward Sama Pyo.

The other toward the Divine Physician.

After a brief silence, the two of them spoke in turn, one young and one old.

“Wh-Why are you looking at me like that? I’m one of the good practitioners of demonic, heterodox arts.”

“I left that line of work a long time ago. N-No, I mean my Master…”

Was this what people meant when they said a guilty conscience needs no accuser?
## Chapter artifact 893

# Chapter 893

The reason everyone’s eyes had turned to Sama Pyo and the Divine Physician—including mine—was simple.

They were both connected to the assassin business.

“Wh-Why are you looking at me like that? I’m one of the good practitioners of demonic, heterodox arts.”

“I left that line of work a long time ago. I—No, I mean my Master…”

Of course, the two of them protested that it was unfair. Even so, there was no denying they had considerable ties to the world of assassins.

Especially someone whose Master had once been known as the terrifying Slaughter Saint.

“Now, now. I’m only asking, so calm down. Do you know anything? For example… an assassin group skilled and bold enough to sneak into the imperial palace.”

The Divine Physician looked around at us with darting eyes, then spoke as if he had no choice.

“How would I know something like that? It’s true my Master was involved with that world once, but…”

“Involved? He was swimming in it.”

At Jeok Cheongang’s mutter, I nodded without thinking.

“Whew. He was practically flying around back then.”

“Right. He flew around so much he eventually became a star.”

“You say that, and people will think he’s dead. He’s still a living legend in that world.”

“Of course. He rewrote history—with blood.”

“Still, he didn’t kill people for no reason.”

“That came later. When he was young, he was probably no different from the rest of those bastards. You know how it is when you’re young—you do what you’re told.”

The Divine Physician, who’d been listening to Jeok Cheongang and me go back and forth, gave us a look as cold as brine.

“If you’re going to put it that way, I won’t say another word.”

“Come on, don’t be like that. I’m only speaking loosely. You know how much I respect him.”

“Honestly, you’re old enough to know better. Don’t sulk. Say something. Surely you picked up a thing or two from your Master.”

After I tried to coax him, the Divine Physician hesitated for a moment, then let out a deep sigh.

“My Master was always reluctant to speak about his past.”

I could understand that. The Slaughter Saint I knew regretted the bloodshed that stained his past.

That was why, right after the Great Faction War ended, he’d put everything behind him and started walking the path of a physician.

Because he didn’t want to kill anyone anymore.

He wanted to wash away the stench of blood that no amount of scrubbing could remove—not by killing, but by saving lives.

And so the greatest assassin of all time became the Divine Physician.

“However…”

The Divine Physician trailed off, then let out the breath he’d been holding.

“Even my Master would sometimes speak of his past. Very rarely, though. Most of what he said was regretful rambling, but he did talk about other assassins, too.”

“Then, could it be…?”

“If they were assassins active in my Master’s time, I’ve probably heard of them at least once. Of course, given what assassins are like, it’s unlikely any of them are still active—”

“I’m glad we asked you first, sir.”

“Pardon? What do you mean?”

“The assassin I saw today seems to fit those conditions perfectly.”

“…”

The Divine Physician’s eyes widened with surprise. I told him—and everyone else waiting for me to continue—everything I’d seen and sensed, from beginning to end.

Even allowing for a human-skin mask or a disguise technique, the man had looked well over seventy. His martial prowess had been formidable, and he’d revealed his connection to Ma Sanbao himself.

When I finished, Ju Hwaran spoke, her eyes wide.

“That old man was a Supreme Peak master?”

“Yes. I’m sure of it.”

“But how could an assassin… Ah, I’m sorry. I didn’t mean it that way.”

At Ju Hwaran’s apology, the Divine Physician waved a hand.

“No, it’s all right. Though I’ve lived far removed from Murim, I know very well what it means for an assassin to reach the Supreme Peak realm.”

It was common knowledge in Murim, and easy enough to understand, that assassins rarely reached the higher realms.

Even if you devoted yourself to a single path with a pure body and mind, setting foot in the Supreme Peak realm was like trying to pluck a star from the sky. What chance did assassins have, when they had to learn all kinds of techniques just to survive and kill?

*It’s like trying to master your major while having to take dozens of extra electives.*

That was why, if you judged them purely by their martial arts, assassins were considered the weakest among the groups that practiced demonic, heterodox arts.

The Slaughter Saint’s title as the greatest assassin of all time came from the same principle.

But the old man I’d encountered today had been a Supreme Peak master. There was no doubt about it.

He did have a slight physical disability, though.

“You said he was lame?”

I nodded at the Divine Physician’s question.

“Yes. I took a close look just in case, but it didn’t seem faked. Besides, if he was going to disguise himself as a laborer carrying supplies, there’d be no reason to pretend.”

“If Young Hero Jin says so, then so it must be. Your reasoning makes sense. Still… lame, you say.”

“Does anyone come to mind?”

The Divine Physician thought for a moment, then answered with a doubtful look.

“I can’t say for certain, but I did hear of someone like that from my Master. He was an assassin who once dominated Qinghai Province. His epithet was, if I remember right…”

“The One-Legged Ghost Killer?”

Someone’s voice cut in, and we all turned.

When everyone’s gaze suddenly swung toward him, Sama Pyo flinched for a moment before speaking.

“I’ve heard of him. Though he was an assassin, his personal martial arts were so formidable that he sometimes killed his targets in life-and-death duels rather than through ambush.”

“How do you know that?”

“How do you think? I heard about it.”

“From who—Ah.”

That was a pointless question.

Who was Sama Pyo? He might be getting worked like a dog under me, but he was the foremost young prodigy of the unorthodox factions and the Young Sect Leader of the Black Dragon Demon Gate, which held sway over Qinghai alongside the Kunlun Sect.

*And his father was none other than the Black Night King, Sima Gong.*

The Black Night King Sima Gong was one of the Supreme Peak masters representing the demonic, heterodox arts. Despite his epithet, he wasn’t one of the Ten Kings. But he’d fought on the Murim Alliance’s side during the Great Faction War and built the Black Dragon Demon Gate into the formidable power it was today.

And since the Black Dragon Demon Gate’s stronghold was in Qinghai, it would’ve been stranger if its Young Sect Leader hadn’t heard a thing or two.

So, the One-Legged Ghost Killer.

“His epithet’s incredible. Just hearing it, he doesn’t sound like a good guy, does he?”

Sama Pyo nodded.

“He’s an assassin.”

“Why do you keep discriminating against them? Aren’t you demonic, heterodox arts yourself?”

“Even if you are the Pavilion Master, that’s harsh. I’m still one of the good, decent practitioners of demonic, heterodox arts.”

“What the fuck? Where have you ever seen a decent practitioner of demonic, heterodox arts? What are you, bright Dark Heaven or something?”

“...You really are something.”

“Fine, I get it. You’re a decent guy. Whatever. Keep talking.”

Sama Pyo glared at Song Ilseom, who’d kept quiet until now but had started grinning like a lunatic the moment I laid into Sama Pyo, then spoke.

“They say the One-Legged Ghost Killer had a fearsome reputation throughout Qinghai even before the Great Faction War. His martial prowess was impressive, but his skill as an assassin was even greater. He was said to have killed an Elder of the Kunlun Sect, who was a Supreme Peak master at the time.”

“He was that good?”

“At least, that’s what I’ve heard.”

“I see. All right. So?”

“So what?”

“Keep going.”

“That’s all. After the Great Faction War, I heard… his whereabouts became unknown.”

“…”

It felt like we’d been having a good fight, only for something to come up and cut it short. That was exactly how I felt.

Fortunately, though, I had a walking encyclopedia of Murim beside me.

“Are you certain the old man you saw was the One-Legged Killing Ghost?”

Namho spoke up, rubbing his lower back.

“According to the information the Hidden Shadow Pavilion obtained, the One-Legged Killing Ghost had only one leg. Of course, he wore a finely crafted prosthetic leg, so it was hard to tell unless you had a keen eye.”

“You mean…”

“It means there’s a good chance you mistook him for someone else. Even if the man you saw really was the One-Legged Killing Ghost… for now, he’s an ally whether we like it or not.”

Namho’s last words rang louder than the rest.

*An ally. An ally.*

Just those two words left a bad taste in my mouth.

At the same time, I finally understood why the old assassin’s presence had felt like a thorn in my throat.

*I must be repulsed by the thought of getting mixed up with people like him.*

If someone asked me whether I thought I was a good person, I wouldn’t be able to answer easily.

I’d taken countless lives myself.

*Not monsters. Real people.*

If I thought someone was an enemy, I killed them without hesitation. The faster I grew stronger, the easier killing became. I could have crippled them by destroying their dantian and severing the Sinews and Meridians in their limbs, but I couldn’t find a reason to bother.

No. I didn’t look for one.

I didn’t want to leave even the slightest chance of future trouble.

And I’d learned that the more I thought about it, the more I looked back at how I’d slowly changed, the greater the pain inside me became.

There were no truly good people in Murim.

Only people who took someone else’s life and risked their own, according to their own goals and values.

That was why I couldn’t call myself a good person, either.

I was only trying to become a little better.

Yesterday, today, and tomorrow.

And that, more than anything, was why I felt repulsed by the old assassin.

*Killing without a reason. Without even an excuse.*

An assassin had only one reason to take a job, one purpose: money.

The old assassin wouldn’t have tried to become a better person like the Slaughter Saint. He would have killed, would kill, and would keep killing people for the numbers written on a bank draft.

Yesterday, today, and tomorrow.

And now, today, he’d become our dependable ally—a comrade who would fight back-to-back with us in the not-too-distant future.

*Is this… right?*

I found myself confused.

The two words Ma Sanbao had used—*the great undertaking*—weighed heavily on my heart. So did the image of the young king held captive in Qianqing Palace, dressed in splendid but cold clothes.

Just as I quietly smacked my lips at the bitter taste in my mouth, someone spoke in a calm voice.

“I once asked my Master why he’d cut off the lineage of Salcheonmun, the sect where he was born and raised.”

It was the Divine Physician.

The old doctor, whose hair was white as snow unlike his Master’s, continued slowly.

“My Master replied that people who felt neither regret nor remorse for what they’d done deserved to die. And so he stained his hands with blood.”

“...!”

“Everyone has their own values, after all. My Master had his, and so does Young Hero Jin.”

I couldn’t listen any longer.

I stood and headed outside.

I needed to see Ma Sanbao. And I needed to get to the bottom of it—to understand why he’d brought them in.
## Chapter artifact 894

# Chapter 894

“Benefactor. No, Pavilion Master.”

At the sight of Jin Taekyung rising to his feet with a hardened expression, Ju Hwaran hurried to stop him.

Or tried to.

“Let him go.”

A quiet voice slipped into her ear.

The hand reaching toward Jin Taekyung froze in midair. Ju Hwaran looked at the door, firmly shut once more after a gust of wind and rain, then turned away.

“Was it really all right to let him go like that…?”

Jeok Cheongang, who had stopped Ju Hwaran at the last moment, answered in a calm voice.

“Who knows? How should this old man know?”

“Old Master!”

At Ju Hwaran’s reproachful cry, Jeok Cheongang gave a faint smile.

He had spent a hundred and several decades wandering the Murim. Over the years, he had seen countless kinds of people, and the number of enemies he had felled was beyond counting.

The name Fire King Jeok Cheongang was both a part of history and history in the making.

Even the leaders of the Nine Sects and One Gang and the Five Great Families wouldn’t dare raise their voices in front of him.

So what had made that child so angry in front of the Fire King himself?

Jeok Cheongang knew the answer.

He knew why his one and only Disciple had stormed out.

“I knew a monk for quite a long time. Night after night, he’d eat meat and drink liquor in some out-of-the-way place. He was a monk in name only.”

Ju Hwaran had paused at the abrupt, rambling story. Now she spoke carefully.

“Could the person you’re talking about be…?”

“That’s right. That monk was Hong Dao, the Dharma King.”

Their friendship was already widely known.

The Fire King Jeok Cheongang had a temper as fiery as his title, and he had hundreds—no, thousands—more enemies than friends. Of the few people he called friends, Hong Dao was the only one who could calm him down with a few words.

Jeok Cheongang didn’t know it, but apart from his martial arts, Hong Dao’s ability to keep Jeok Cheongang’s foul temper in check had played a large part in earning him the title Dharma King.

Of course, the most decisive reasons Hong Dao was respected by all the Murim were his gentle nature—worthy of a great and virtuous monk—and his mysterious prophetic ability.

“Sometimes, he’d read the heavenly patterns and learn the will of Heaven. Watching him do it was nothing short of miraculous.”

By now, everyone—including Ju Hwaran—was quietly listening to the story that had begun so suddenly.

The Dharma King was that symbolic a figure in the Central Plains Murim. Even if he hadn’t been the Abbot of Shaolin, the very Mount Tai and Northern Dipper of the Murim, that wouldn’t have changed.

“But one year before that monk entered Nirvana, he said something to me.”

Jeok Cheongang reached deep into his mind and pulled out a memory etched there.

It was a memory from a night that could never return, one that came back to him whenever he thought of the friend who had gone before him.

“He said the heavenly patterns were becoming distorted. They had been for decades already. Before long, clouds of an unknown calamity would gather and cover the sun, the moon, and even the stars.”

“Dark Heaven…!”

A single cry slipped from someone’s lips.

Jeok Cheongang nodded and continued in a low voice.

“That was when I began to pay serious attention to the existence of Dark Heaven.”

But that wasn’t all.

Four months before that, Hong Dao had looked up at the sky and seen something shining amid the disordered darkness.

“The Morning Star.”

Jeok Cheongang let out a breath he’d been holding.

A morning star was supposed to shine brilliantly for a moment, then fade away.

But the one that had begun to shine clearly in the north one day never faded.

If anything, its light grew larger with each passing day.

It kept shining as Jeok Cheongang and Jin Taekyung—an old man and a young man who had met by chance as though by fate—left Shanxi and reached Henan.

It kept shining as they spent a year together on Mount Jiuhua, and until the venerable monk who had first discovered the Morning Star became a handful of relics.

And, perhaps, it was still shining now.

“Do you know what the Dharma King said when he told me about the Morning Star?”

No one answered. Jeok Cheongang wasn’t waiting for one.

“He said that one insolent brat I’d kept by my side was the master of that Morning Star.”

“……!”

“He also said that even if the whole world were plunged into darkness one day, that Morning Star would never lose its light.”

The people who had been left speechless stared with their mouths agape.

The subject of this astonishing secret from the past—unknown until now—was someone they knew well.

*Jin Taekyung.*

One name pierced everyone’s mind.

The shock they felt at that moment was beyond anything they could have imagined.

The Dharma King Hong Dao had said that the master of the Morning Star would light up the world. He had said it was a star that would never lose its light, not even at the end.

But the Morning Star didn’t point to the Martial God, a legend of the past, or the Sword Saint, who was writing a new legend as the Murim Alliance Leader.

It pointed to Jin Taekyung.

A young man who had only just passed the age of twenty, yet shone brighter than anyone else amid the calamity that had befallen the land.

Clunk. Whoooosh.

Silence had settled over the pavilion when the wind and rain burst in, flinging open the firmly shut door.

The rain and wind, no less fierce than before, swept through the people, but no one said a word.

As if by agreement, they quietly turned their heads and stared into the darkness beyond, their eyes still wide with shock.

At the place where the star had been.

At the master of the Morning Star, somewhere out there.

“I once heard someone say this.”

Jeok Cheongang murmured calmly.

“Where a star shines, darkness gathers. But the star never disappears.”

At first, even Jeok Cheongang had been skeptical.

A calamity that would dwarf the Great Faction War?

Jin Taekyung—so young he was practically a baby—was the light in the middle of it?

But as time passed, and the longer Jeok Cheongang watched Jin Taekyung at his side, the more he came to understand.

*This brat is the light. A new star who’ll serve as a guide through the darkness that will one day cover the land.*

And…

*The only light Heaven has allowed this old man.*

Just as a star shone brighter in the darkness, darkness always seemed to gather wherever Jin Taekyung went.

But no darkness had ever dared to approach him. None had managed to extinguish the light he gave off.

And even if the day when that happened ever came, it wouldn’t be this time.

The complete darkness had yet to descend upon the land. Only then would the Morning Star that was Jin Taekyung shine at its brightest and largest.

*Until then… find your own path. Shine your light wherever you wish.*

Jeok Cheongang smiled faintly.

The time for weighing right and wrong in worldly affairs had passed long ago.

In the Murim he’d experienced—or in this world, for that matter—there was no such thing as justice.

Only monsters consumed by their own causes, pointing spears and swords at one another.

Just like the incomprehensible series of events unfolding right here, in the imperial palace.

*This old man is no different.*

Growing old also meant growing numb.

Death had become cheap, and the people he’d struggled to let into his heart had begun to leave one by one.

His first Disciple, Jangcheon. The Dharma King.

The justice Jeok Cheongang had chosen, his great cause, was to protect what he still had.

He only hoped to make even a slightly good choice along the way, as his one and only Disciple—who had suddenly come into his life late in the old man’s years—was doing.

That was the only difference Jeok Cheongang saw between the orthodox faction and the demonic, heterodox arts.

*Even if you write it clumsily, all crooked and awkward, does that make its meaning fade?*

Even if the handwriting was terrible, the meaning contained in the character for *upright* remained unchanged. It was simply as awkward as a child’s writing.

And his Disciple, Jin Taekyung, despised the assassins who didn’t even make that effort. He suspected Ma Sanbao’s motives for suddenly bringing martial artists into the cause.

*Whatever decision you make, it doesn’t matter. This old man will always be at your side.*

Jeok Cheongang gazed at the darkness visible through the door, thrown wide open by the wind.

The imperial palace was an unknown place, full of secrets.

Whatever happened next, it wouldn’t surprise him.

No—a storm so vast was raging that it was impossible to tell friend from foe.

*If we can’t avoid it, we’ll just have to face it.*

Jeok Cheongang muttered inwardly, then smacked Taishan on the back of the head. Taishan had been licking a bare plate clean.

Smack!

“Quit doing the dishes and close the door, you unorthodox little bastard.”

* * *

It didn’t take long for me to come face-to-face with Ma Sanbao.

Rather than me finding him, he found me first.

“He’s waiting for you.”

As I headed toward the pavilion assigned to the East Depot, recalling the layout I’d already mapped out, a eunuch in a close-fitting martial uniform approached and spoke. My eyes narrowed.

*How did he know?*

I’d made sure to stay hidden using the darkness and the terrain, and I’d kept my movements to a minimum.

No matter how skilled the East Depot eunuchs were with concealment techniques, it was hard to believe they could detect someone of my caliber so easily.

But…

*Damn it.*

Now wasn’t the time to dwell on questions. I silently stepped out of the darkness, and the eunuch led me to a small pavilion.

“He’s waiting inside.”

I quickly surveyed the area.

The imperial palace was divided into countless pavilions and sections for its various departments.

But this place wasn’t in the East Depot’s section marked on the map of the imperial palace I’d obtained beforehand through Ma Sanbao.

“Wait. This place…”

“It isn’t a building assigned to the East Depot. Officially, that is.”

“……”

“Then I’ll be going. This one will take his leave.”

A secret refuge in the imperial palace, used to avoid people’s eyes. Something like that?

The eunuch disappeared before I could say anything more, and I stepped into the pavilion.

Creak.

The foul weather came in handy for once.

The sound of the old wooden door’s groan was swallowed by the pounding rain.

*Ma Sanbao is… upstairs.*

There was only one presence on the floor above. I climbed the stairs, which creaked almost as badly as the door, and saw a lone figure standing in the pitch-black room.

“You came?”

In the darkness, I caught a glimpse of teeth far whiter than those of an ordinary person of this era.

Ma Sanbao glanced around the empty room, without even a candle or a piece of furniture, then shrugged.

“Forgive the squalor. There are too many eyes watching.”

“It’s fine. I don’t mind this kind of thing.”

“This kind of thing, eh? Sounds like you do mind the rest.”

“Since you already know, this conversation should be over quickly.”

A voice slipped between my lips, sounding strange even to me. My expression was probably as stiff as my voice.

“As expected, you’re astonishingly honest.”

“I hear that a lot.”

How often did someone get to speak to Ma Sanbao—the East Depot’s de facto leader—like that?

But his reaction wasn’t what I expected.

“So, what is it you want to hear about?”

His face was calm, as if this was what he’d been expecting. Then came his unhurried voice.

“The assassins I hired? Or… that woman, So Gyo?”

“……!”

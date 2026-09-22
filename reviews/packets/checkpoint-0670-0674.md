# Checkpoint Review — 670–674

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

# Chapters 670–674

## Plot

Baeksang betrays the Beast Miao King and confronts the fleeing escape party, while the Beast Miao King, Wonhu, and the remaining Miao warriors stay behind to delay more than a hundred Bai warriors. Jin leaves the Outer Palace carrying the unconscious Yayul Mok and initially heads toward the reconnaissance squad, but White Tiger detects Yohi’s high-grade tracking scent. The System generates the Supreme Peak-grade Sudden Quest **Yohi’s Tracking Scent**, forcing Jin to choose between escape and returning toward danger.

Jin follows the scent southeast. After ambushing and interrogating Nanman warriors, he warns them not to harm the surviving Miao warriors and burns forests, mountains, and a pasture to draw Baeksang’s pursuit away from the escapees. Meanwhile, Nanman blames Yayul Cheok and Jin for the prison raid and Western Yao Estate massacre, declares them traitors, and places Baeksang in temporary control of the Beast Palace.

The Southern Heaven Demon Empress appears before Baeksang and reveals that Dark Heaven’s decades-long undertaking is nearing completion. She identifies the Beast Miao King and Jin as the remaining major obstacles, orders Baeksang to kill the Beast Miao King within three days, and declares that Dark Heaven will handle Jin. Baeksang accepts the command despite recognizing himself as her controlled puppet. Jin and Muyaho continue south, repel several pursuit squads, and reach a dark mountain beside a black forest.

## Continuity

- Baeksang has betrayed the Beast Miao King and is now Nanman’s temporary Palace Lord under the Southern Heaven Demon Empress’s command.
- Baeksang’s left arm was severed by Force during the escape attempt; the wound has stopped bleeding but remains painful.
- The Beast Miao King, Wonhu, and the remaining Miao warriors stayed behind to delay Baeksang’s forces. Their survival is unresolved.
- Nanman has issued a general mobilization and is hunting Jin Taekyung, Yayul Cheok, Yayul Mok, and the released Han Chinese prisoners as traitors.
- Jin chose to follow Yohi’s Tracking Scent rather than immediately escape toward the reconnaissance squad; the Sudden Quest’s reward and failure conditions remain unknown.
- Muyaho can detect Yohi’s nearly odorless high-grade tracking scent and continues carrying Jin south despite exhaustion, blood, and soot.
- Jin has used forest and mountain fires as beacons to divert pursuit and protect the people who remained behind.
- Dark Heaven’s undertaking is nearing its final stage and is intended to establish a bridgehead from Nanman toward the Central Plains for the Lord of Heaven’s return.
- The Southern Heaven Demon Empress has ordered Baeksang to eliminate the Beast Miao King within three days, while Dark Heaven directly deals with Jin.
- Jin and Muyaho have reached a dark mountain beside a black forest; what awaits them there is unresolved.
- Namho, Taishan, Sama Pyo, the reconnaissance squad, and the Fire Dragon Pavilion members still need to complete their escape.

## Translation Decisions

- Use **Great Chieftain** for 대족장, **Palace Lord** for 궁주, **temporary Palace Lord** for 임시 궁주, and **Palace Lord’s Hall** for 궁주전.
- Use **Southern Heaven Demon Empress** for 남천마후 and **Dark Heaven** for 암천.
- Use **Great undertaking** for 대사 when referring to Dark Heaven’s plan.
- Retain **Yohi’s Tracking Scent**, **Muyaho**, **Western Yao Estate**, and **Force**.
- Preserve the Southern Heaven Demon Empress’s playful, taunting menace and Jin Taekyung’s crude, irreverent narration.

## Durable state

{
  "active_continuity": [
    "Nanman has issued a general mobilization order and placed Baeksang in the temporary position of Palace Lord.",
    "Baeksang's left arm was severed by Force, and he remains under the Southern Heaven Demon Empress's command.",
    "The Southern Heaven Demon Empress has ordered Baeksang to find and eliminate the Beast Miao King within three days while Dark Heaven handles Jin Taekyung.",
    "Dark Heaven's decades-long undertaking is nearing completion and is intended to open a bridgehead from Nanman toward the Central Plains.",
    "Dark Heaven expects the return of the Lord of Heaven at the end of its undertaking.",
    "Jin Taekyung and Muyaho are fleeing south after repelling multiple pursuit squads and have reached a dark mountain beside a black forest.",
    "Baeksang admits that his remaining sworn-brotherly feelings may have helped the Beast Miao King escape, but vows that such leniency will not happen again."
  ],
  "continuity_sources": [
    674
  ],
  "open_questions": [
    "What exactly is Dark Heaven's great undertaking and how will it bring about the Lord of Heaven's return?",
    "Can the Beast Miao King evade Baeksang's three-day pursuit?",
    "How will Jin Taekyung survive Dark Heaven's direct intervention?",
    "What awaits Jin Taekyung and Muyaho in the dark forest?"
  ],
  "safe_through": 674,
  "temporary_decisions": [
    "Use Great Chieftain for 대족장 and Palace Lord for 궁주.",
    "Use temporary Palace Lord for 임시 궁주 and Palace Lord's Hall for 궁주전.",
    "Use Southern Heaven Demon Empress for 남천마후 and Dark Heaven for 암천.",
    "Use Great undertaking for 대사 when it refers to Dark Heaven's plan.",
    "Preserve the Southern Heaven Demon Empress's playful, taunting menace and Jin Taekyung's crude, irreverent narration."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 670

# Chapter 670

It was a short but lengthy span of time.

Short enough to pass in the blink of an eye, yet long enough for a single moment to feel like seven days and nights.

Long enough to walk while looking back over each and every year of the past several decades. Long enough to watch a squalling newborn, crying in the arms of a mother who had died because she could not survive childbirth, grow into a tall and handsome young man.

That was how Baeksang’s deliberation had been both short and long, long and short.

And when his tightly sealed lips finally moved to break the silence, he already had his answer.

“You’ll regret this.”

The Beast Miao King calmly asked in return.

“What will I regret? Coming to find you? Or rescuing Jin Taekyung and the other Han Chinese?”

“Everything that has happened until now.”

“Just like you, Baeksang?”

“It’s different.”

Baeksang continued with a hardened expression.

“Unlike me, you still have a chance, Palace Lord. One last chance to undo your mistake.”

“One last chance…”

“If you return quietly now, I’ll forget everything I saw and heard here. As if nothing ever happened.”

“How can one cover the sky with the palm of one’s hand? I was already prepared for this when I told you to spare your subordinates guarding the underground prison.”

“If I order them to keep silent, they will obey. The Bai people’s loyalty to me is no weaker than that of the Seven Miao Tigers under your command.”

“Is that… the last affection you can show me as your sworn younger brother?”

Baeksang silently nodded.

The Beast Miao King gave him a sorrowful smile.

“Then, relying on that last bit of affection, I’ll ask you one more time. Half a shichen. Open a path for them, even if it’s only for half a shichen.”

“Palace Lord!”

“Even if I could turn back, I would not. That is the one difference between us, after spending our entire lives together.”

“……!”

The corners of Baeksang’s eyes trembled.

At this moment, he wanted with all his strength to deny those words.

*You’re wrong. Unlike you, I had only one path before me. I had no choice but to walk it.*

But his firmly closed lips would not open, and before he knew it, his hand had reached his sword hilt.

Click. Shing.

The cold scrape of metal cut through the brief silence.

The Beast Miao King’s eyes sank deeply as he looked at Baeksang, who held his beloved sword lowered at his side.

“So that is your choice?”

“I had no choice, Palace Lord. For me, right now… this is the best I can do.”

“It’s much better not to hear that awkward formal speech. It feels as though we’ve gone back to the old days.”

“You know as well as I do, Palace Lord. We can never go back to those days.”

“You think so?”

“Of course.”

At that firm answer, the Beast Miao King gave a faint smile.

Baeksang had made his decision. He did not hesitate.

Tssssss!

A dazzling halo of light illuminated the world around them.

A vast gathering of qi known as Sword Force descended toward its target.

Slice!

* * *

Three tigers ran like the wind, led by a snow-white White Tiger.

Wonhu, the eldest of the Seven Miao Tigers, watched their backs disappear into the darkness and muttered,

“Damn, they’re fast.”

That was the entirety of his impression.

Those who were leaving had left, and those who remained had stayed. He and the others had simply chosen for themselves to be the latter.

“Heh heh.”

With a relieved laugh, Wonhu pulled a gourd from inside his robes.

Pop.

The moment he removed the stopper, the scent of liquor spread through the air.

The Miao warriors nearby all lit up at once.

“Oh-ho.”

“That smells incredible. Did Big Brother brew it himself?”

“Hell, did they round up nothing but a pack of fucking mutts? Why are all your noses so sharp?”

Though Wonhu grumbled, his eyes were smiling.

With an expression that said he could not help it, Wonhu passed the gourd around to the men who had gathered.

“Nothing I can do. There isn’t much, so take turns and drink a little.”

“I swear on my life, not a single drop will reach Big Brother’s mouth.”

“Ah, I can’t pass this up.”

The Miao warriors laughed heartily and took turns tipping back the gourd.

The Nanman people were famous for their love of liquor. And with twenty grown men there, their boast that they would not leave a single drop behind seemed quite credible.

But…

“Ahh, that’s good. Now it’s Big Brother’s turn. I left a few drops out of courtesy.”

When Wonhu finally received the gourd, he could only snort with amusement.

Slosh.

He could tell just by shaking it lightly.

The liquor inside was not even half gone.

Looking at the men shamelessly carrying on about how good the liquor tasted, Wonhu let out a laugh.

“Turns out you aren’t fucking mutts after all—just a bunch of blowhards.”

“Hm? What are you talking about?”

“Indeed. Has senility already set in, now that you’re in your fifties?”

“Enough nonsense. Drink.”

At the surrounding urging, Wonhu tilted the gourd.

Not toward his mouth, but toward the ground covered in thick weeds.

Trickle.

“Don’t waste a single drop. If we survive, we’ll all sit together and drink through the night. And if we fall here, we’ll still be able to get drunk after death.”

“……!”

“……!”

The men who had watched him with hardened expressions slowly raised the corners of their mouths.

“Yeah. That sounds good.”

“Big Brother knows what he’s talking about.”

“Come to think of it, you’ve always been crazier about liquor than martial arts. Isn’t that right?”

Wonhu smiled.

So did the Seven Miao Tigers, who had spent their entire lives alongside him.

So did the Miao warriors who had willingly volunteered for this dangerous mission.

Regret?

Not in the slightest.

Even if they all died here, their one and only hope was that those who had left would survive and escape the danger.

That was why Wonhu could smile so freely.

As he thought of the one man who had always stepped forward first in everything, and who had even sent his only heir here to set an example for the others, Wonhu murmured inwardly.

*I’ll gladly accept punishment for disobeying your order… in the afterlife, my lord.*

Neither the Beast Miao King nor Yayul Mok feared death.

They did not use their subordinates as shields, nor did they retreat in terror.

The Beast Miao King loved his only child, whom he had gained late in life, more than anything in the world.

But if he learned what Wonhu had done, he would surely scold him, saying that there was no distinction between lives.

*Yes. That’s reason enough to give up our lives.*

Wonhu shook the empty gourd.

Then, as he watched the last drops of liquor fall like the tears of an ant, he smacked his lips and suddenly spoke toward somewhere in the darkness that had settled all around them.

“Hey, you got any liquor?”

A quiet reply came from the darkness.

“I thought you were on duty.”

“We both know what’s going on, so why bother? Go peel and eat a tiger’s dick.”

Wonhu grinned.

The scheduled shift change had passed long ago, and the waves of energy extending from beyond the darkness were so powerful that they sent chills down his spine.

“So, are you saying you won’t give me any?”

“I’ve heard there’s a monkey among the Miao people who likes liquor. Catch.”

Whoosh.

Wonhu snatched the object flying through the darkness.

At the same time, he recognized the rough but familiar gourd and unconsciously let out a groan.

“This is…”

There was no mistake.

It was none other than the gourd his lord, the Beast Miao King, had made himself and always carried with him.

“Does it look familiar?”

A voice suddenly pierced his ear.

Wonhu slowly raised his head.

A man stood in his field of vision.

His white robes were stained with blood and filth from unknown owners. His skin was so starkly white that *pallid* was the only word for it.

“……Baeksang.”

Baeksang answered in a dry voice.

“How dare a mere warrior casually speak the name of the Great Chieftain?”

“What happened to my lord?”

“You’ll find out soon enough.”

Swish. Papapat!

It happened in an instant.

When Baeksang shook his blood-soaked sleeve, more than a hundred Bai warriors appeared from the deep darkness and surrounded them.

*Damn it.*

Wonhu cursed inwardly and drew the broad-bladed saber tucked into his waist.

He glanced at the sky.

Today, of all days, the moon was hidden behind the clouds.

It was a particularly poor day to die, but in another sense, that was fortunate.

In a pursuit carried out under a moonless sky, the fugitives had the advantage.

*Please, both of you. You have to still be alive.*

Only one thing remained now.

Wonhu—or rather, all of them—raised their weapons and charged toward the enemy without hesitation.

A tremendous roar rose around them, so vast that fear itself could not approach it.

* * *

Whoooooosh!

The wind brushing against my entire body was cold.

Even as the landscape rushed past us, there was not a single person or one of the oddly shaped houses in sight—only thickets everywhere.

We had already left the Outer Palace behind.

*But we’re still within the territory of the Nanman Beast Palace. We can’t slow down.*

No. We might have to keep running without rest until we rescued the Fire Dragon Pavilion members included in the reconnaissance squad.

The power of the Nanman Beast Palace extended across this entire unknown land, filled with forests, plains, jungles, and swamps.

“Sorry, but I’m going to have to ask a little more of you.”

Grrr.

Just as Yayul Mok had said, this really was a spiritual creature.

Even through the roar of the fierce wind, the White Tiger seemed to understand my words. It let out a low growl and increased its speed even further.

Papapapat!

There was probably another reason it obeyed me so well.

Its master was tied to its back.

I let out a sigh as I watched Yayul Mok’s body sway faintly each time the White Tiger moved forward.

*Yayul Mok.*

We had left the Outer Palace while running frantically, but I had not woken him.

No. It would be more accurate to say I couldn’t bring myself to try.

*If he wakes up, he’ll try to go back somehow.*

But if he returned now, everything would be for nothing.

If we gave up the one and only escape route they had risked everything to open for us, all that would remain would be a meaningless death.

Of course, given his status, they probably would not execute him immediately as they intended to do with me…

But if he tried to turn back, I would stop him.

For Yayul Mok’s sake.

For the Miao people fighting for him.

And for the members of the Fire Dragon Pavilion.

It was fine if they called me selfish. I did not care if they cursed me and pointed their fingers at me, saying I only cared about saving my own life.

But damn it, this was the best course of action available to me right now.

*Damn it.*

I bit down hard on my lip.

At most, within a day—or perhaps half a day—the net over heaven and earth would be spread across all of Nanman.

Before that happened, we had to get as far away as possible and find the reconnaissance squad.

*The two tribal chiefs leading the reconnaissance squad are effectively loyal retainers of the Beast Miao King. Perhaps we’ll be able to rescue three people without much of a fight.*

Of course, that was the best possible outcome I could imagine.

With Dark Heaven’s intervention and Baeksang’s betrayal now certain, and with me having become the star of a massacre that had never been in the cards for me, no one could predict what variables might arise.

*Rescuing all the Fire Dragon Pavilion members comes first. And after that…*

But my thoughts did not get any further.

Rustle.

The White Tiger abruptly stopped.

It had been running at the front without hesitation, but its movement came to a sudden halt.

“What’s wrong?”

Grrr.

“As your master said, if we keep running northwest like this…”

Grrrr. Sniff, sniff.

What?

The White Tiger looked in two directions in succession, then buried its nose in my hand and began sniffing.

Just as it had before we set out.

*Wait. Could it be?*

And then, at that very moment—

Ding!

> **System**
>
> - A Sudden Quest, **Yohi’s Tracking Scent**, has been generated!

Along with the Quest notification piercing my ear, I remembered.

The scent pouch belonging to Yohi that I had discovered in the western Yao territory.
## Chapter artifact 671

# Chapter 671

The place where I currently found myself—the Murim—had neither the dazzling scientific civilization nor the mechanical engineering of the modern world. Nor did it have magic.

But even this world was filled with special things scattered throughout it, things no less extraordinary than magic.

Murim people who accumulated internal energy and wielded power beyond that of Hunters. Countless kinds of martial arts unavailable in the modern world, along with mysterious and bizarre spiritual creatures and elixirs.

And… tracking scent was one of them.

Ding.

> **System**
>
> A Sudden Quest, **Yohi’s Tracking Scent**, has been generated!
>
> Would you like to open the Quest window and check its contents?
>
> **Y / N**

A System notification suddenly rang out. Faced with the unexpected situation, I nodded as if entranced.

Ding.

> **System**
>
> **Quest**
>
> **Yohi’s Tracking Scent**
>
> A new path has appeared before you as you flee from pursuit.
>
> Now, you must make a choice once more.
>
> However, you cannot know what awaits you at the end of the two roads before you. All that exists are the consequences of your choice—and the responsibility that comes with it.
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Choose a direction to travel (Incomplete)
>
> **Reward:** Linked Quest
>
> **???**
>
> **Failure:** ???

*Goddamn it. What is this now?*

A holographic window filled the air before me.

At the same time, a short memory from barely a day ago flashed through my mind.

*Looks like they really went at it.*

*By the time I received the report, everything was already over. All that remained in the western Yao territory was blood and corpses. And… those things.*

I remembered everything from that day clearly. It was the only clue left behind by Heugung and Yohi, the two Great Chieftains who had vanished without a trace.

*Heugung’s wrist had been severed, and Yohi…*

That was right. She had left behind a scent pouch.

However, since I had only just arrived at the western Yao territory, I had focused on the wrist Heugung had left behind rather than the scent pouch.

If I could determine the traces of injury remaining on the severed wrist, I could at least roughly infer the opponent’s martial arts and level.

*Compared to that, Yohi’s scent pouch didn’t seem particularly important.*

The scent pouch had not even been intact. Made of silk, it had already been damaged, and the scent had escaped through a long tear in the fabric, leaving it almost odorless.

But I had not known.

No—given everything that happened one thing after another, no one had had the time to pay attention.

That it was the most important clue in the western Yao territory.

That it was a tracking scent Yohi had left behind so that someone could find her.

*The scent hadn’t escaped. It had been like that from the beginning.*

As far as I knew, tracking scent was an unusual object made for following someone’s trail, just as its name suggested.

It was by no means something commonly found, but it was not entirely unused, either.

Among the orthodox faction, for example, there were the Lower District Sect and the Beggars’ Sect.

And the fact that I had spent quite a lot of time with the Successor Beggar of the Beggars’ Sect—a man from an organization of truly enormous scale—and exchanged all kinds of stories with him had been an unexpected stroke of luck.

*Tracking scent. It’s definitely effective, but incredibly rare. The method of making it is highly secretive, too. There are only a few people in the Murim who can produce it.*

*Like the Ten-Thousand-Li Tracking Scent or something?*

*The Ten-Thousand-Li Tracking Scent? Hm. I guess even someone like you has picked up a thing or two somewhere.*

*Looks like about five of your teeth are going to fall out soon. Want me to pick those up for you too?*

*Oh. Ah…*

*Go on. Run your mouth some more.*

*Well, ahem. I’ve never actually seen the Ten-Thousand-Li Tracking Scent, either. Ten thousand li sounds impressive, but it’s hard to believe the scent could remain throughout a journey that long.*

*What? So it was a scam after all?*

*It isn’t necessarily that simple. Even if they aren’t as impressive as the Ten-Thousand-Li Tracking Scent you heard about through the grapevine, there are quite a few kinds of tracking scent actually used in the Murim. The highest grade among them is commonly called the Thousand-Li Tracking Scent.*

*The Thousand-Li Tracking Scent?*

*It has several distinguishing features. First, the manufacturing process is disgustingly difficult. Second, the manufacturing cost is disgustingly high. Third, acquiring the Thousand-Li Tracking Scent made that way requires a disgustingly large amount of gold.*

*No mistaking you for a fucking beggar. You can’t get through a sentence without working “filthy” in somewhere.*

*No matter how disgusting I am, your personality is still—*

*I’m sorry. That was a slip of the tongue. Anyway, tracking scent of that level is worth dozens of times its weight in gold. Of course, its effectiveness is just as certain.*

*For example?*

*Unlike the unverified Ten-Thousand-Li Tracking Scent, the scent of the Thousand-Li Tracking Scent really remains for about a thousand li, and it’s nearly odorless—so faint that even certain beasts with extremely developed senses of smell can’t detect it. Humans are out of the question.*

*What? Then wouldn’t applying tracking scent once solve everything?*

*The trade-off is that tracking scent lasts for seven days and nights at most. If the target burns their clothes or fully immerses themselves in water, for example, the duration will be shortened even if the scent doesn’t disappear entirely.*

*Even so, you’d have to know you’d been marked with tracking scent before you could try any of that. You said that even most beasts can’t smell it properly.*

*That’s right. But spiritual creatures are different.*

*Ah.*

*That’s why there are only two ways to pursue a target using tracking scent. Either you have someone who has mastered advanced tracking arts, or you lead a spiritual creature capable of smelling it.*

As I recalled the conversation I had once shared with Gung Gibang, I had no choice but to admit that everything he had said was true.

Grrr. Sniff, sniff.

Along with a low growl, the damp nose pressed against my palm kept twitching.

I looked down at White Tiger, who was licking my fingers with a rough tongue that stung slightly, and muttered,

“……Right. You’re here.”

A spiritual creature capable of smelling tracking scent.

Just as Gung Gibang had told me.

This White Tiger—Muyaho—was even a spiritual creature intelligent enough to understand and communicate with humans from a young age.

*Intelligence befitting a spiritual creature, and keen senses beyond those of an ordinary beast.*

Now that I thought about it, the scent pouch that had been nearly odorless had probably contained Thousand-Li Tracking Scent as well.

The highest-grade tracking scent, which supposedly lasted for seven days and nights as long as the target remained within a thousand li, barring any unusual circumstances.

I could tell that much just by looking at the two tigers standing there blankly and waiting, unlike Muyaho.

Grrr. Grrr.

Muyaho let out a low growl, as if asking me a question.

Where should he go? He wanted me to choose the path he should take.

The great head covered in snow-white fur moved back and forth between two directions.

One was northwest, where the reconnaissance squad had gone.

And the other was—

*……Southeast.*

Crack.

My clenched fist trembled.

Taishan, who had been watching me, blinked his eyes as big as saucers.

“Pavilion Master. Why?”

I wanted to answer Taishan.

*It’s nothing. Nothing’s wrong, so let’s just keep going.*

But no words came from between my parting lips.

*Fuck.*

The curse I could not bring myself to spit out lingered in my mouth.

There was no reason to hesitate. The road had already been decided, and the beasts were moving faster than I had expected.

Even if the net over heaven and earth spread the moment dawn broke, I felt that, in my current condition, I could somehow make it out of Nanman.

But… why, then, was I hesitating?

*What happens if I leave Nanman with them now? What comes after that?*

I already knew the answer to the question I had asked myself.

Perhaps I had known it from the moment I climbed onto White Tiger’s back.

*Even if I come back again… it’ll already be too late by then.*

Even if we did everything we could to shake off our pursuers and escaped the net over heaven and earth Baeksang had spread, it would take several days.

If I added the time needed to return, it would take seven days and nights.

Would the people who had set out to rescue us still be there by then?

No. If this incident had even put the Beast Miao King in danger, would Dark Heaven have any reason to hesitate before carrying out its sinister scheme?

*They’ll die. Dozens. Hundreds. Maybe even thousands of people.*

I slowly blinked.

Whether my eyes were open or closed, the world remained shrouded in darkness. There was still no sign of dawn breaking in the east.

*Fuck. It was like this when I first entered boot camp.*

The sudden thought made me let out a hollow laugh.

Thinking back, maybe those days at boot camp had been the best.

Back then, I had been in a position where I could be forgiven no matter what kind of shit I pulled.

But now, everything had changed.

I had faced the threat of death countless times. I had even survived while leaving dying comrades behind.

I had locked myself in my room for days, crying like an idiot, and sworn that I would never lose my people again.

Then, one day, I obtained the System.

When I came to my senses and looked around, I found myself with a great deal to be responsible for.

Everything happening in the world felt like it was my fault, and I pitied the innocent people losing their lives in the process.

And every time that happened, I thought,

*What if I had been there?*

But now, all I could do was laugh hollowly.

Because all those thoughts seemed like affectation and hypocrisy, like I had merely been cosplaying as a hero.

That was right.

I was neither a heroic martial artist nor some hero from a superhero movie.

But today, the people who had watched me flee until the very end were true heroic martial artists—true heroes.

*No need to thank us.*

*Of course. Nanman was only repaying the debt it owed you.*

*My hyung was on Ailao Mountain. Thanks to you, I can see him again.*

*Please take care of the Young Palace Lord.*

Dozens of faces brushed through the darkness.

Among them were young men and middle-aged men who were already growing old.

Their skill?

If I truly made up my mind to act, I could knock every one of them down within moments.

And that was precisely why they were even more remarkable.

They had not come to win.

They had stayed behind to die.

Even if all of this was nothing more than striking an egg against a rock, they would not retreat.

They would hurl their bodies against the solid stone, even if they were ultimately smashed to pieces.

*Maybe even right now.*

And I… had left those people behind.

Even knowing what fate awaited those who remained, I had gone with the empty promise that I would return.

Haa.

The air had been muggy just moments ago, yet now a single deep breath produced a cloud of white vapor.

I felt it again: this damn Nanman was a truly shitty land.

Almost as shitty as my mood.

> **System**
>
> - Select a Quest mission.

I silently stared at the holographic window floating in the air.

Then, abruptly, I spoke.

“Taishan.”

“Hm?”

“From now on…”

At the words that followed, Taishan’s eyes widened.

* * *

The old man suddenly opened his eyes.

How long had he been unconscious?

Every joint in his body ached, and the body tied to the back of a huge beast was bobbing without pause.

*A tiger?*

His gaze darted around.

Namho realized that Yayul Mok’s plan had succeeded.

And then he noticed something strange.

“……Why? Why isn’t that bastard here?”

At the old man’s voice, filled with confusion, Taishan turned his head.

“Namho. You awake?”

But Namho did not answer.

He asked instead, an ominous intuition pressing down on his chest.

“Where is he?”

“……Namho.”

“Where is he, I said! That Jin Taekyung bastard!”

Unlike the eastern sky, which was beginning to grow faintly bright, Taishan’s expression darkened.

And Namho realized that the ominous feeling he had sensed had not been an empty fear at all.
## Chapter artifact 672

# Chapter 672

Whoosh, whoosh, whoosh!

The fierce wind sent white fur rippling. Clinging to the nape of the White Tiger, I watched the scenery rushing past.

Dense undergrowth filled every direction, and trees stood tall like giants.

A snake hiding between moss-covered rocks glared at us with bright yellow eyes, while a leopard lying flat in the grass and searching for prey spotted the White Tiger and slowly began backing away.

And above all of it, the sky was gradually growing brighter.

*Already?*

I muttered inwardly, then realized that quite a lot of time had passed.

We had escaped the underground prison just after midnight, so by a rough calculation, we had been running nonstop for at least three shichen.

Growl.

Perhaps that was why the breathing of the White Tiger carrying me—Muyaho—was much rougher than before, and fatigue could be felt in every step he took.

*It’s only natural.*

I could say this with confidence after all my time in the Murim: even a Peak master who had learned a movement technique would develop varicose veins if he ran at full speed for three shichen in this godforsaken place.

And Muyaho was a great tiger—a spiritual creature even larger than an ordinary tiger.

Running across terrain so rugged that even Kim Jeong-ho[^1] would have given up on mapmaking must have rapidly drained his stamina and worn down his muscles.

[^1]: Kim Jeong-ho was a nineteenth-century Korean cartographer famous for producing detailed maps of Korea.

And on top of that, he had to carry me, a fairly large man, on his back.

I might not be a veterinarian, but even with my eyes closed, I could tell what condition Muyaho was in.

*He’s lasted this long only because he’s a spiritual creature of Muyaho’s caliber.*

As befitted one of the most renowned spiritual creatures in Nanman, his basic physical abilities were excellent. But if he kept traveling like this, he would be unable to show his strength when it truly mattered.

I stroked his nape and whispered,

“Let’s rest for a little while nearby before we go on.”

—Growl.

Understanding me without difficulty, he gave a small nod.

As luck would have it, the sound of running water was coming from not far away. We slowed down and soon found a small stream.

A few mountain animals had also come out early to drink.

Squeal?

Wild boars. Excellent.

Without hesitation, I immediately put the thought that had popped into my head into action.

*Open Inventory. Summon.*

After shoving all kinds of things into my Inventory in a desperate effort to survive, I had practically become a walking armory.

I pulled out a cheap iron spear I couldn’t even remember storing and hurled it.

Two large wild boars collapsed without even having time to scream.

Whoosh—thunk!

Squeeeeeal!

Those two must have been the piglets’ parents.

Seeing the young wild boars flee at top speed, squealing as they went, I felt a weight settle over my heart.

“Hoo.”

—Grrr.

Just as Muyaho solemnly nodded, I continued speaking with a sorrowful expression.

“The young ones have more tender meat. I should’ve caught them first.”

—……Grr?

What, you little punk?

Ignoring the look Muyaho gave me—as if wondering whether that bastard was really human—I skinned the wild boars and skewered them on the iron spear.

Fwoosh. Crackle.

Then I used Scorching Yang Qi to make a campfire. As I watched the wild boar meat cook amid the curling smoke, a quiet laugh escaped me.

There was no special reason. I simply found my own actions so absurd that I started laughing.

*I’ve made all of Nanman my enemy, and I’m throwing a barbecue party in the middle of it.*

I knew this was insane.

No, the fact that I had retraced the southeastern road toward the heart of Nanman was already insane.

But no matter how many times I thought it over, I always reached the same conclusion.

Once I had decided to follow Yohi’s Tracking Scent, this was the best method available to me.

That was also why I had committed the madness of lighting a fire here, barely a hundred li from the Outer Palace.

*The more attention I draw over here, the greater the chance that the others will survive.*

Before leaving, I had repeatedly impressed one thing upon Taishan.

Run without looking back. Persuade the chieftains of the reconnaissance squad’s tribes through Yayul Mok, then use the swift ships of the Water Dragon Stronghold to escape Nanman.

Taishan had been silent for a long while, unlike his usual self. Then he had said,

*Pavilion Master.*

*What?*

*Taishan will go too. Taishan cannot let Pavilion Master go alone.*

Maybe it was because it had been dawn, or maybe because his words had been so unexpected. For that moment, at least, I think I had been rather sentimental too.

But while my heart had been moved, my cold head had known the truth.

If even one of them came with me, neither side could remain safe.

*Wait here with the others. I’ll be back soon.*

*When? How many nights does Taishan have to wait?*

*Who knows? About ten nights?*

*Taishan doesn’t like that. Ten nights is too long.*

*Then five nights.*

*Good. It’s a promise.*

*Yeah. A promise.*

And so I had left, leaving behind a promise even I could not be certain I could keep.

Five nights.

Could I return within that time? No. Would I even be able to return at all? To be honest, I had no idea.

Even after escaping the underground prison, the Logout function remained blocked, and the countless Nanman people who had become my enemies were probably tightening the net from every direction as they searched for me.

Maybe…

Rustle.

Yes. Even now.

—Grrr.

Muyaho, who had been drooling while watching the wild boar meat turn golden brown, suddenly let out a low growl.

While calming the creature that had revealed its hostility, I sharpened my senses even further.

New information flowed in through my heightened five senses.

*About fifty people. I don’t know their tribe yet, but they’re all warriors… and there are no beasts with them. Did they leave them behind because they were worried about being discovered?*

Even if they had brought a truckload of beasts, nothing would have changed. Still, this did make things easier.

After roughly assessing the situation, I slowly began turning the iron spear on which the wild boars were skewered.

Sizzle.

Beyond the appetizing sound of meat roasting, the conversation of the uninvited guests holding their breaths faintly tickled my ears.

—That’s him. He must be, since he has that White Tiger Yayul Mok cherished at his side.

—I’m not sure. All I can see from here is his back. Instead of doing this, shouldn’t we turn back and request support?

—Pathetic. Heaven has given us this opportunity, and you want to hand the battle merit to another tribe? We’ve come this far, and you still intend to spout such cowardly nonsense?

—B-but, hyung. Even if that man really is the Han Chinese we know about, how are we supposed to deal with a monster like him?

—Even so, he’s still just a human made of flesh and blood. Judging by the fact that he’s cooking meat here dressed like a beggar, he must have been separated from the others and lost his mind. If we capture him here, we’ll gain not only ten thousand gold, but our father might even become the new Great Chieftain.

Hm. So that was it.

Listening carefully to the conversation drifting into my ears, I brushed off my backside and stood.

Then I turned around and abruptly asked,

“Really? Do I look that bad right now?”

“……!”

“……!”

Even from more than thirty zhang away, I could feel it: the trembling air and the many emotions wrapping around the enemies who had been approaching as stealthily as possible.

Shock. Astonishment. And…

“Attack!”

A rash decision born from stupidity and a vain thirst for glory.

But they did not know that, despite my ruined clothes, my body was in peak condition—and that I was already shooting toward them.

Whoooosh!

My body surged forward like a streak of light. Wind whipped up like a gale, and the thick grass burst apart.

Through the leaves shattering and scattering in every direction, I saw eyes filled with terror.

“What’s everyone doing? Aren’t you going to finish drawing your weapons?”

Despite my friendly advice, the hands gripping weapons that were not even halfway drawn remained frozen in place.

The same was true of the man leading them.

“Y-you…….”

*I feel like I’ve seen this face somewhere.*

It did not matter right now.

“Why aren’t you attacking?”

“W-what did you say?”

“You said to attack. You came all the way here, and you’re not going to?”

“Th-that is…….”

“You won’t? Then I will.”

I quietly tossed out a single word.

“Attack.”

And the next moment, a huge shadow fell across the ground.

—Raaaaar!

With a roar, the massive body that leaped over my head crashed down upon the man.

Crack. Craaack!

* * *

Someone once said that force and oppression could never be tools of communication. That to make a closed mouth open, you needed a gentle expression and a kind tone of voice.

That was not entirely wrong.

To make a closed mouth open, you did not merely need force and oppression. You needed fucking merciless force and oppression.

And I had to admit, I seemed to possess a remarkable talent in this field.

“What’s the current internal situation of the Nanman Beast Palace?”

“You bastard! Just kill me!”

“Good. Muyaho?”

Crunch!

“Gyaaaah!”

“Good job. Now spit it out.”

Ptooey.

“Urgh. Hic—hiiic.”

“Why are you bawling so pathetically? You’re a grown-ass man.”

“Hic.”

“That was your leg this time, but if you keep crying, I’ll go for your balls next. Do you understand, you fucking bastard?”

“Ghk. Gnnng……!”

“Good. Then I’ll ask again. What’s the current internal situation of the Nanman Beast Palace?”

The interrogation proceeded quickly and smoothly.

Of course, the preparations for the interrogation had also been flawless.

I had broken both arms of the men who attacked me late, and the legs of those who tried to run away.

After leaving about twenty men crippled, I used Muyaho’s one-bite-only chance. Every one of them became docile as a golden retriever.

*Is that about it?*

There was a possibility they had lied, but they had given me enough grounds and credible information that I could treat their answers as fact for now.

Besides, everyone became honest in the face of death.

Especially in the face of losing their balls.

After finishing all the interrogations, I glanced at the man Muyaho had attacked first.

His entire body had been crushed. He was barely breathing, and when our eyes met, he let out a groan.

*So that’s where I’d seen him.*

Blood ties told the truth. He was the spitting image of his father, the chieftain.

Of course, his father was not particularly important to me either.

On the first day of the Tribal Grand Council and the day of the tragedy at Yoseo Manor, he had been nothing more than a sycophant desperate to stand behind Baeksang somehow.

But that was also why I was sparing him and the others.

“Go back and tell them.”

At my quiet words, the man’s lips trembled as he looked at me with terrified eyes.

“T-tell them what?”

“That I’m here. That I’m watching you from somewhere not far away.”

“……!”

“Don’t forget everything you heard today. I won’t forget it either.”

The man—and the other Nanman people nearby, who had been watching my every move with all their senses alert—shuddered.

They would probably remember what happened today until the day they died.

My expression and tone. My voice and actions.

And the warning I had left during the interrogation, after learning that the Miao warriors who had attacked the underground prison the night before were still alive.

*If you touch them, I’ll kill every one of you. Maybe not today, but tomorrow. Or next year. Perhaps at the very moment you think everything is over and finally let your guard down.*

People feared someone’s threats because they were afraid those threats might truly become reality.

And in their eyes, I was more than capable of making mine real.

The inheritor of the Fire Gate Clan’s legacy. The successor of Jeok Cheongang, the Fire King. An unprecedented monster who had shaken the entire world at only around twenty years of age.

That was enough.

Today, I had carved an indelible fear deep into their bones. Now, that fear would spread among the Nanman people who stood on Baeksang’s side.

Quickly. Farther and farther.

Until no tribe dared harm them.

Baeksang still existed, so it was too early to call them completely safe. But this was the best I could do for them right now.

“Leave at once. Unless you want to die here.”

“……!”

“……!”

A short while later, seated on the branch of a giant tree, I watched around fifty pale-faced figures make their way out of the forest.

Like ghosts had possessed them, they fled in panic. I watched their backs until they disappeared, then slowly drew up the Scorching Yang Qi of three jiazi.

Fwoosh.

Flames gathered in both my hands.

Now it was time to light the beacon that would draw the net over heaven and earth toward me—a vivid beacon burning with an entire forest as its kindling.

Fwoosh. Whooom!

As I watched the horrifying heat and flames spread in every direction and devour the forest, a thought suddenly occurred to me.

*Old Master would swear a blue streak if he saw this.*

I let out a quiet laugh and turned away from the blazing forest.

Ahead of me, Muyaho was already running energetically with a half-charred piece of wild boar meat clenched in his mouth.
## Chapter artifact 673

# Chapter 673

This was the first turbulent period to descend upon the world since the end of the Great Faction War.

It had come to the Central Plains, known as the center of the world, and to distant Nanman, thousands of li away from the Central Plains.

“Gasp, pant… Did everyone hear the news?”

“Catch your breath before you talk. What is it this time?”

With new rumors spreading by the day, the Nanman people were no longer as shocked as they had been at first.

No, to be precise, they had begun to think there was nothing left that could surprise them.

And for good reason. The events of the past month or so had been one massive shock after another—greater than the combined impact of every incident that had occurred in Nanman since the Great Faction War ended.

The massacre of a Miao village by Han Chinese.

The attack of a Thousand-Year Spider that had suddenly appeared from Ailao Mountain, which had remained quiet for decades.

And the story of a young Han Chinese man who had not only entered the Inner Palace for the first time in the history of the Nanman Beast Palace, but had even attended the Tribal Grand Council, where only thirty-two tribal chieftains were permitted to sit.

If the series of new incidents had ended there, perhaps things would have been manageable.

But when more than a hundred Yao warriors were brutally killed in the Western Yao Estate just three days earlier, and two Great Chieftains of immense symbolic importance went missing, the situation began rushing forward like a torrent.

*The culprit! The culprit behind the Western Yao Estate incident has been revealed! It was that young Han Chinese man! Jin Taekyung!*

*Wait. Just wait a moment. Have you already forgotten that Jin Taekyung saved the warriors at Ailao Mountain the day before? Nothing has even been conclusively established yet. It’s too soon to make a judgment…*

*Too soon? Ever since those Han Chinese bastards came here, nothing but bad things have happened. There’s no reason to wait any longer!*

*You’re right!*

Only reason could overcome anger, but the voices of those few people were helplessly buried beneath the shouts of many Nanman people whose reason had already gone numb.

*Drag the Han Chinese out into the street and dismember them!*

*Great Chieftain Baeksang! You must punish those bastards!*

The festive music and laughter that had filled the streets every year when the Tribal Grand Council convened could no longer be heard.

Angry shouts echoed from every direction, and two names were always included in those cries.

Jin Taekyung. And Baeksang.

Their status differed as greatly as their origins, ages, and names.

For the Nanman people, this was only natural.

One was an outsider from the distant Central Plains—a criminal who had committed a tragedy that could never be forgiven. The other was the Great Chieftain who led the Bai people, the strongest tribe in this land after the Miao people.

The Nanman people still respected and loved their Palace Lord, who possessed martial prowess renowned throughout the world and an unpretentious personality. But it was impossible for their trust not to crack over the Western Yao Estate incident.

After all, it was none other than the Palace Lord, Yayul Cheok, who had brought the Han Chinese responsible for every recent misfortune into the Inner Palace.

Yet even those who had cheered for Great Chieftain Baeksang could not help but become flustered when they heard the new rumors that emerged at daybreak.

“What, what did you say?”

“Did I… Did I hear that wrong?”

Their pupils trembled, and their faces were filled with bewilderment.

Everyone who heard the news could only keep repeating the unbelievable story in their minds, wearing the same expression and the same look in their eyes.

*The Palace Lord… tried to harm Great Chieftain Baeksang last night, failed, and then fled?*

At first, they all thought it was a ridiculous false rumor. The Palace Lord they knew—the Great Chieftain of the Miao people, Yayul Cheok—was not that kind of person.

Before he was an excellent Palace Lord, he was a good man. More than anyone else, he was a native of this land who cared for Nanman.

But the news that followed was enough to plunge the beliefs and questions of the Nanman people into an abyss.

“Baeksang is taking office as the temporary Palace Lord? What does that mean?”

“I-I don’t know either. But the Inner Palace posted a notice. It said exactly what we heard.”

“What kind of nonsense is this? How could that possibly be true?”

“That’s not all. Apparently, the Palace Lord even mobilized the Young Palace Lord and dozens of elite warriors under his command to raid the underground prison and release the culprit, Jin Taekyung, along with the other Han Chinese.”

“……!”

“I can hardly believe it either, but the circumstances are remarkably clear. It’s an undeniable fact that the Palace Lord has been friendly toward the Han Chinese for a long time. And the whereabouts of Jin Taekyung, the Young Palace Lord, and the other Han Chinese are unknown. The Tribal Grand Council was convened last night, and they apparently declared this a betrayal against all of Nanman and issued a general mobilization order.”

“What? A general mobilization order?”

“That’s right. I heard it was decided along with the matter of the temporary Palace Lord. They must intend to hunt down and execute the rebels who have thrown Nanman into chaos. Naturally, the highest-priority targets are the Han Chinese Jin Taekyung and the Palace Lord. No—the former Palace Lord.”

“Former Palace Lord? What are you talking about?”

“I don’t know. I’m still confused myself. But how could ordinary tribesmen like us know the details? We can only follow the Tribal Grand Council’s decision.”

The contents of the notice, stamped clearly with the Inner Palace’s seal, spread in an instant, and the Nanman people’s reactions split into three groups.

Those who believed the Beast Miao King had betrayed them.

Those who refused to believe it under any circumstances.

And those who, without questioning or making any effort to seek the truth, simply submitted to the new reality placed before them.

Then, amid this whirlwind of extreme confusion, more than fifty warriors returned to the Outer Palace through the western gate, each carrying injuries of varying severity.

Their bodies trembled like aspens, and their faces bore an indelible terror. The remains of the enormous flames visible from ten li away were still etched clearly in their wavering eyes.

“Mon… monster…”

The voice that slipped between someone’s lips was frozen solid, despite the blazing sunlight pouring down overhead.

It was around noon.

* * *

Baeksang stared at his reflection in a large mirror.

He had a youthful, handsome appearance and a well-balanced physique that belied his age of more than seventy. He was even dressed in garments made from the pure white fur of a fox.

Anyone who saw him might have marveled at his dignity and bearing, saying he looked like the ruler of an entire kingdom.

But Baeksang’s gaze remained fixed on his own coldly hardened face.

*Was I wearing this expression all this time? For so many years?*

Even when he looked back over the past several decades, he could not remember when he had last laughed sincerely.

Now, he could only take out those old memories covered in dust and examine them once more.

*Yes. That was the last time.*

A memory from one particular day surfaced, and the chill in his eyes began to melt.

After a victory in a fierce battle, they had been given several days of sweet respite.

The bold boy who had set out after his father, determined to defeat the Demonic Cult, had already grown into a handsome young man. And the girl who had been lively since childhood—and therefore always covered in scrapes and bruises—had grown into a beautiful woman.

The young man’s name was Hwi. The woman’s name was Hyang.

The two of them were as radiant and fragrant as their names. They were a pair of flowers that had bloomed amid a battlefield overflowing with blood and death. Though they called each other dog-and-monkey enemies despite having grown up together, they would sometimes walk together while avoiding the eyes of others.

They probably had not known.

Back then, when they had carefully slipped away from the people drunk on victory and alcohol and walked together along a hill drenched in faint moonlight, someone had been watching them.

*…You came again?*

*…Why did you come again, hyung?*

*Do you ask because you don’t know? I came to keep watch in case Hwi, that wolf-like bastard, tried anything with my frail and beautiful Hyang.*

*I’m asking because I’m genuinely curious. Are you serious?*

*Of course I’m serious.*

*Then you must know that Little Tide Demon died in the battle three days ago.*

*Little Tide Demon? That bastard who could slap the Heavenly Demon across the face if lust were martial arts?*

*That’s right.*

*As a father with a daughter, I’d been meaning to teach him a lesson someday. Good riddance. But why are you suddenly bringing this up?*

*That bastard. Hyang killed him.*

*……*

*Apparently, Hwi was fighting Little Tide Demon and suffered a sword wound. Then Hyang suddenly appeared and smashed Little Tide Demon’s head with a pair of axes she had picked up from somewhere.*

*……*

*And apparently, that still didn’t satisfy her. She crushed the dead bastard’s balls, hurled every curse imaginable at him, and hacked his corpse to pieces. In Hwi’s words, it looked like an imperial palace chef mincing meat with uncanny skill.*

*…That’s a lie. My Hyang would never do that.*

*Even excluding Hwi, five people saw it. Three of them still can’t speak because of the shock.*

*Good. Then tell them to keep their mouths shut. Otherwise, I might have to personally do something to seal their lips… Oh. No.*

*You’re not some kind of fiend… Gasp.*

That day, the sworn brothers crouching far away in the darkness had unintentionally witnessed it.

The sight of the two children they cherished more dearly than their own lives slowly tilting their heads toward each other.

*Turn around. Quickly!*

*Lower your voice first, hyung! And I already turned around!*

*Oh, please. Good heavens. What did I just see?*

*What else? Did you leave your eyes in Nanman? They were kissing—mmph. Mmph!*

*Baeksang, you conniving bastard! You sent that wolf-like son of yours to set up a scheme like this? Do you want to become Palace Lord that badly?*

*Mmph! Hah! Me, Palace Lord? What kind of insane nonsense is that? Maybe after you or I die, but not now.*

*Oh, I see. You intend to fulfill the dream you couldn’t achieve through your son? Since Hyang could become the next Palace Lord, you’ll snatch her up and make her do nothing but housework. Isn’t that it?*

*I’m going insane. Seriously.*

*This is your last chance. Admit it while you still can.*

*No. I said no!*

*Really? Swear it to the heavens.*

*I swear it to the heavens!*

*Fine. I believe you. Then prepare for them to hold their wedding this year.*

*How many times do I have to say it isn’t… What? What did you just say?*

*Don’t ‘what’ me. Just get ready to marry off those youngsters who are crazy about each other.*

*……*

*Why are you just staring at me with that blank expression? You had already figured it out too. Unless you dislike it?*

*D-Dislike it? Of course not. As you said, I had already figured it out. But this is… What should I call it? Huh.*

*Then that settles it. No need for a long discussion. If the western front stabilizes before winter, let’s have them marry and send them back to Nanman. And although the thought makes me feel strange… if they have a child, those two will give up their stubbornness and return willingly, won’t they?*

*A child. Heh… Hehehe. Has so much time really passed already?*

*You’re younger than me, yet you’re pretending to be an old man. Enough. Promise me one thing.*

*What do you want me to promise?*

*That girl Hyang. To me, she is more precious and pitiful than anyone. Because of her worthless father, she lost two older brothers and suffered terribly.*

*Hyung…*

*Damn it. What I’m trying to say is… Shit.*

*Stop. I already know what you’re trying to say. She’s a precious child, so you want me to treat her preciously, don’t you?*

*……*

*You have nothing to worry about. Hwi will certainly do that. He’ll grow old with her not merely as a woman, but as a companion—and sometimes as a friend.*

*I suppose I can trust Hwi.*

*If you can’t trust Hwi, then trust Hyang.*

*What?*

*Look at Hyang’s temper. If Hwi so much as disappoints her, he’ll end up like Little Tide Demon. No doubt abou—!*

*Baeksang, you bastard! How dare you think of my Hyang as—!*

That last shout had been an obvious mistake.

The young man and woman, who had been sharing their first shy kiss, hurriedly pulled away from each other, and the two sworn brothers had to flee with all their strength.

Then, when they reached a quiet stream and were about to hurl a word at each other…

*Yes. We laughed. Loud enough to shake the world.*

He could no longer remember why they had laughed so loudly. It had not been merely because each other’s panic-stricken faces had looked so funny.

Perhaps it had been because they were happy that the two children who had grown up together since childhood were finally being joined together—and that the sworn brothers who had spent their entire lives together would at last become one family.

*Hyang… If she hadn’t left us like that. If only…*

Everything might have changed.

But at the same time, Baeksang knew.

The thought echoing inside his heart was nothing more than a futile wish.

That winter, when they had been waiting for the wedding that would have become a celebration for all the Nanman people—

Contrary to everyone’s hopes, the western front did not stabilize. An army of ten thousand Demonic Cult forces swept in with the cold wind.

And then… the flower withered.

After Yayul Hyang—the woman who had been as beautiful as a flower and as strong as steel—withered on the battlefield, the light vanished from Baekhwi’s face.

That must have been the reason.

On the day of the final battle at the Great Snow Mountain, he had cut down the enemy again and again as though possessed by something, stepping into ever greater danger.

Even afterward, Baeksang sometimes wondered.

Perhaps that child had seen a single flower blooming somewhere in a narrow ravine.

*Was that really what happened?*

As always, Baeksang asked a question that would receive no answer, then stared at the mirror, now gone hazy.

No. That was how the entire world before him looked now.

Drip. Drip.

The sky was clear, without a single cloud. Yet raindrops were falling from somewhere.

And then, in the next moment, someone’s voice pierced Baeksang’s ears.

“Oh my. Should I come back later?”

Baeksang slowly turned around.

Reflected in his bloodshot eyes was a woman who had appeared like a ghost.

“…Southern Heaven Demon Empress.”

At Baeksang’s call, the woman—the Southern Heaven Demon Empress—smiled broadly.

It was a smile as radiant as a flower and as wicked as a viper.
## Chapter artifact 674

# Chapter 674

There were often phenomena in this world that could not be understood through common sense.

The woman reflected in Baeksang’s bloodshot eyes at this very moment was one of them.

“…Southern Heaven Demon Empress.”

His voice quietly echoed through the space where only the two of them existed.

The woman—the Southern Heaven Demon Empress—smiled broadly.

“It’s been a while, Great Chieftain Baeksang.”

Her smile was infinitely beautiful and even more bewitching. Baeksang’s heart sank.

*How?*

It was not particularly surprising that she had infiltrated the place despite its strict security. But how could he, a man who had reached the Supreme Peak realm, have failed to sense even her presence?

It had been more than thirty years since Baeksang had first learned of the Southern Heaven Demon Empress.

Many things had changed since the days when he had been half-mad with grief over the loss of his child. But realizing that the gap between him and that demoness had not narrowed in the slightest weighed heavily on his heart.

“…What brings you here?”

At Baeksang’s stiff question, the Southern Heaven Demon Empress deliberately made a sulky face.

“What? Do you not like seeing me?”

Her question was filled with playfulness, but with the Southern Heaven Demon Empress standing before him, Baeksang could not afford to let his guard down even a fraction.

Baeksang forced himself to calm down before answering.

“I simply did not expect you to come in person. Under normal circumstances, you would have sent word through a messenger or a secret message.”

The Southern Heaven Demon Empress—or rather, Dark Heaven—had always been that way.

Meeting black-clad figures whose names and faces were never revealed, or discovering secret messages they had left in unexpected places, had long since become familiar to Baeksang.

At the same time, they were things he could never refuse.

“In four days, it will be the day we promised to meet again. Even if you had not gone to the trouble of coming all the way here, I would have gone to see you.”

It was something they had repeated for several decades.

On the first day of every month, Baeksang exchanged missives with Dark Heaven between Insi and the hour of the Rabbit. Once every three months, he would go to see them alone without informing anyone.

“Three days from now? Oh my, has it already been that long?”

The Southern Heaven Demon Empress widened her eyes as though she had completely forgotten. Baeksang felt his fist tighten on its own.

“You…”

“I’m joking, I’m joking. Getting worked up over something so out of character for you. When I see you like this, our Great Chieftain has a surprisingly cute side.”

“…!”

“I came for a few reasons. A lot has happened lately, and now you’ve finally become the ruler of Nanman, so I thought I should congratulate you in person. But…”

The Southern Heaven Demon Empress covered her mouth as she laughed.

“Who would have thought? The famously cold-blooded Great Chieftain Baeksang. No—the new Palace Lord. I never expected to see you in tears.”

The corners of her mouth were lifted, but her gaze had sunk deep.

Baeksang felt a chill creep into one corner of his heart and parted his lips.

“It was nothing. Looking at the mirror simply brought back some old memories for a moment.”

“Oh, because you thought of the son who looked exactly like you in the mirror?”

“…I would prefer to end that subject here. What matters is not the past, but what lies ahead.”

“Well, if that is what our Palace Lord wishes. That is a good attitude.”

The Southern Heaven Demon Empress smiled sweetly before continuing.

“Still, I’m a little disappointed. I thought you had been moved to tears by the gift.”

Baeksang replied in a rigid voice.

“I appreciate the mirror you gave me. I use it well.”

“That’s enough. I went to quite a bit of trouble to find it as a gift commemorating your appointment as Palace Lord, but this feels like I’m being thanked only because I demanded it.”

The Southern Heaven Demon Empress shot Baeksang a sidelong glance before slowly walking toward the window.

Below the Palace Lord’s Hall, which stood atop the highest hill in the Inner Palace, countless pavilions and houses spread out in full view.

“Wow, what a view. It really is different from a place where the Palace Lord lives. You’ll be looking at this scenery every day from now on, won’t you?”

“I am still only the temporary Palace Lord.”

“Temporary… You don’t really think that, do you?”

“…”

“My Palace Lord. Why are you pretending when you know everything?”

The Southern Heaven Demon Empress gave the silent Baeksang a smile with her eyes before turning her gaze toward the view outside.

Sunlight poured down, a cool breeze blew in from somewhere, and the sky was a vivid blue without a single cloud.

The clear weather she had encountered for the first time in a while suddenly put the Southern Heaven Demon Empress in a pleasant mood.

How could it not?

Soon, she would be able to stain this impossibly clear sky with darkness in which not even a single ray of light remained.

Whoooosh.

The wind rushed in through the wide-open window, sending her fine, silky hair rippling.

The Southern Heaven Demon Empress had been smiling with her eyes closed. Moments later, she suddenly parted her lips.

“You know, don’t you? That the great undertaking has entered its final stage.”

“……!”

Her quiet voice pierced his ears, and Baeksang’s eyelids trembled.

The decades that had passed and the face of one person flashed before his eyes.

“Of course… I do.”

“Everything is proceeding smoothly. Except for a few minor problems.”

Baeksang immediately guessed what she meant. Then, when the Southern Heaven Demon Empress spoke the names of two people, he realized that his guess had been correct.

“The Beast Miao King. And Jin Taekyung.”

Resting her chin lightly on one hand, the Southern Heaven Demon Empress continued while watching Nanman warriors file in outside the window.

“To be honest, they are more than minor problems. One of them is a Supreme Peak master whose martial prowess is great enough to place him among the Ten Kings. And the other one is, yes. That Jin Taekyung.”

Watching her back, Baeksang thought that the inevitable had finally arrived.

This was probably why the Southern Heaven Demon Empress, who had not revealed herself for such a long time, had come here in person.

“I am sorry.”

“Sorry? For what?”

“How could I not be? It was clearly my mistake.”

“Hmm.”

The Southern Heaven Demon Empress hummed softly as though singing under her breath before continuing.

“That’s right. But it was our mistake as well. I never expected the Beast Miao King to make such a terrible move either. And…”

The Southern Heaven Demon Empress glanced over her shoulder. Her gaze came to rest on Baeksang’s left arm.

Unlike the previous night, the arm hidden beneath a robe made of pure white fox fur was empty.

“I knew our new Palace Lord had made an effort in his own way.”

The bleeding had already stopped, but the pain rising from the severed end, cut through by Force, could not be dealt with in such a short time.

Baeksang endured the sudden pain before answering.

“I was no match for him. Even after I mobilized every soldier waiting nearby, he managed to break through the encirclement.”

“He may be the last among them, but one of the Ten Kings is still one of the Ten Kings. Or perhaps what saved him was… the last thread of warmth remaining under the name of sworn brothers.”

“That…”

“Isn’t that right? Are you absolutely certain?”

After a brief silence, Baeksang opened his mouth.

“Perhaps. Yes, perhaps it was. At the very least, I might have been able to buy enough time to pursue him.”

“Do you know what you are saying right now?”

“Of course. But there is one thing I can say with certainty. Nothing like that will ever happen again.”

The Southern Heaven Demon Empress stared at Baeksang’s deeply sunken eyes for a moment before letting out a soft sigh.

“Phew. That’s a relief.”

“What is?”

“That you answered honestly. If you had refused to admit it, I was planning to tear you limb from limb and kill you before long.”

“……!”

“I’m genuinely relieved. Even though we haven’t met very often, I’ve come to like you quite a lot, Palace Lord.”

The Southern Heaven Demon Empress smiled shyly like a young girl before continuing.

“You know how sometimes, when you see a tiny ant that has fallen into the water struggling desperately to survive, you want to root for it? Ah, of course, I’m not saying you’re an ant. I’m just bad at expressing myself.”

Baeksang felt as though all the blood in his body had turned cold.

The fear bearing down on his body and mind was vast enough to swallow his shame and humiliation whole.

At the same time, he realized once again.

*This woman before me is truly dangerous.*

To Dark Heaven, he was nothing more than an easily controlled puppet, a leashed animal—or something even less than that.

But…

*This is the path I chose.*

That was the cold reality.

Long ago, the Southern Heaven Demon Empress—the Dark Heaven—had reached out her hand to him, and Baeksang had taken it. In exchange, he had received hope.

That very hope had raised him back up after he collapsed beneath the grief of losing his child. It had given him a reason to continue living.

That was why he could not bring this path to an end himself.

He was riding a tiger. Now that he was on its back, all he could do was race onward with all his strength.

Thud.

It was a sight no Nanman person could have believed.

Yet what was happening inside the Palace Lord’s Hall was all real.

The new Palace Lord of the Nanman Beast Palace, the ruler of the vast Nanman, dropped to one knee and bowed.

He did so before a woman who seemed capable of being more beautiful than anything else in the world.

“Please give me your orders, Demon Empress.”

The Southern Heaven Demon Empress looked down at Baeksang and smiled languidly in the sunlight pouring through the window.

“This is why I like you.”

The Southern Heaven Demon Empress stretched out a hand toward the window.

It was as though she meant to seize the Nanman warriors endlessly pouring in response to the new Palace Lord’s general mobilization order, along with the blue sky spread above their heads.

“Three days. Find the Beast Miao King and eliminate the source of trouble within three days. As for Jin Taekyung…”

Or perhaps to turn it all into darkness in a single breath.

“We will deal with him.”

Now that everything had entered its final stage, the Southern Heaven Demon Empress had no doubt that the path opened from Nanman would become a bridgehead toward the Central Plains.

At its end, the return of the omnipotent Lord of Heaven, who ruled all things in the world, would be waiting.

* * *

I’ll stake Hyuk Mujin’s balls on it.

That was probably the most unprecedented signal fire in the history of Nanman—or perhaps in the history of the entire Murim.

Whoosh. Fwoooosh!

It was the second day since I had entrusted the others to Taishan and headed south. I was burning the seventh mountain.

Oh, the pasture too, of course.

“Wait. Was it the seventh one, or the eighth?”

Growl.

“On second thought, that’s not what matters.”

I ignored the White Tiger’s displeased expression.

Its once-white fur was filthy with blood and soot.

Of course, the blood had not come from its body. After repelling pursuit squads about six times, this kind of unfortunate accident had been unavoidable.

But before long, Muyaho’s complaints would no longer be audible.

No—to be more precise, neither of us would be able to care about things like that anymore.

Step.

The White Tiger’s enormous forepaw stepped into the mud.

And the fact that the creature that had been running like the wind all this time let out a small cry while staring at the black forest could only mean one thing.

That’s right.

“It’s here.”

I muttered while gazing at the mountain shrouded in darkness.

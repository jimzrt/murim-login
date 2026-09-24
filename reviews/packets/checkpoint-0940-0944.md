# Checkpoint Review — 940–944

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

# Chapters 940–944

## Plot

The Emperor orders Baek Yeon to announce that he will personally lead the campaign against Dark Heaven, despite his failing health. Before Taekyung leaves for Shanxi, the Emperor meets him at the North Gate, gives him the imperial dragon cloak, appoints him Marquis of Shangshan and a Thousand Captain of the Embroidered Uniform Guard, and entrusts him with a thousand guards to defend the realm. He urges Taekyung to follow what is right, not merely serve as his subject.

The Divine Physician tells the Emperor that Taekyung has found a path to survival, but it requires the Emperor to die once. He gives him an old bamboo slip from Taekyung, whose references to the Maoshan Sect and White Illusion Jiangshi Art catch the Emperor’s attention.

Taekyung’s journey toward Shanxi risks arriving too late, so he divides the party. Namho will contact the Murim Alliance for reinforcements; Song Ilseom and Sama Pyo will lead the main group onward, while Taekyung, Jeok Cheongang, and the Bow Saint take a faster mountain route. Namgung Ryong joins them with horses, provisions, and a guide, though his father, the Azure Sky Sword King, is away on an unknown mission. As they prepare to depart, an unidentified figure emerges from the shadows.

## Continuity

- The Emperor’s only known path to survival requires him to die once. The Divine Physician has the bamboo slip Taekyung provided, bearing the names Maoshan Sect and White Illusion Jiangshi Art; how it enables the treatment remains unknown.
- Dark Heaven is expected to invade Shanxi around the Double Ninth Festival. Taekyung is racing there with Jeok Cheongang and the Bow Saint; the larger party and thousand Embroidered Uniform Guards are following separately.
- Namho plans to contact the Murim Alliance and seek reinforcements. Song Ilseom and Sama Pyo lead the main group toward Shanxi.
- Namgung Ryong is helping Taekyung’s group travel to Shanxi. His father, the Azure Sky Sword King, is away on a mission for Alliance Leader Mae Jonghak, and his location is unknown.
- An unidentified figure has appeared as the group prepares to leave with Namgung Ryong.
- Taekyung’s System Quest still requires him to remove the Emperor’s Blood Soul Gu and successfully treat him.

## Translation Decisions

- Render 上山侯 as “Marquis of Shangshan” and 千戶 as “Thousand Captain.”
- Render 백환강시공 as “White Illusion Jiangshi Art.”
- Render 천뢰검 as “Heavenly Thunder Sword.”

## Durable state

{
  "active_continuity": [
    "The Emperor was poisoned with Blood Soul Gu, which reached his marrow; the Divine Physician said his vitality was at its limit and could not guarantee survival for another couple of months.",
    "The Divine Physician says the Emperor’s only path to survival requires him to die once; the method is not yet explained.",
    "The old bamboo slip Taekyung gave the Divine Physician bears the names Maoshan Sect and White Illusion Jiangshi Art; its full significance is unknown.",
    "Taekyung’s System Quest requires him to remove the Blood Soul Gu from the Emperor’s head and successfully treat him; its reward and failure consequence are unknown.",
    "The Emperor prepared for his death by transferring loyal retainers and his power base to Zhu Bao.",
    "War against Dark Heaven is imminent: its main force is targeting Shanxi as a foothold for invasion of the Central Plains, with the Double Ninth Festival as the expected date.",
    "Taekyung was appointed Marquis of Shangshan and Thousand Captain, with a thousand Embroidered Uniform Guards entrusted to him to fight the foreign enemy.",
    "The party is traveling toward Shanxi. Namho will contact the Murim Alliance and seek reinforcements from behind; Song Ilseom and Sama Pyo will lead the remaining group toward Shanxi, while Taekyung, Jeok Cheongang, and the Bow Saint advance over a mountain route.",
    "Namgung Ryong has joined Taekyung’s effort against Dark Heaven and is preparing horses, food, and a guide for the journey to Shanxi.",
    "Ma Sanbao escaped and evaded the Imperial Army’s three-day search.",
    "The Eastern Heaven Demon Lord’s hidden iron chest contained old bamboo slips, recent papers, and a small silk pouch of unknown significance.",
    "The Bow Saint says the Martial God chose her; she tested Taekyung to confirm he was the chosen one and assess his power and character."
  ],
  "continuity_sources": [
    944,
    943
  ],
  "open_questions": [
    "What is the Martial God’s identity, and what is the full nature of his connection to the chosen one and the Bow Saint?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "Where is Ma Sanbao, and what is his current status?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain, and what is their significance?",
    "Where is the Azure Sky Sword King, and who is the figure rising from the shadows?"
  ],
  "safe_through": 944,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 940

# Chapter 940

While the gers on the grasslands shivered in the cool night wind, heavy with sand, people behind a massive wall ten thousand li away were greeting the morning.

It was still far too early for sunrise. Darkness surrounded them on every side.

*Thudthudthudthud!*

Rough hoofbeats shattered the dead of night.

More than a hundred messengers passed through the Seven Gates without a single formality. Like the dozens of messenger eagles sent ahead of them, they vanished into the wind, each bound for a different destination.

And the man who had given all these orders listened as reports came in one after another, his face pale.

“All the messengers have just passed through the Seven Gates!”

“The Imperial Decree has been delivered to the high ministers of the Six Ministries!”

“The Censorate awaits Your Majesty’s command!”

“The officials of the Hanlin Academy and the Transmission Office are preparing the edict!”

“A report from the Five Tiger Commandery! In accordance with Your Majesty’s command, we are immediately preparing three hundred warships, one hundred thousand naval troops, and the Imperial Guards—”

“Enough.”

At the Emperor’s sudden command, every sound around him vanished as if washed away.

The Son of Heaven’s authority was absolute.

Though the Great Nation was only in its third generation, the power wielded by its current Emperor equaled—or perhaps surpassed—that of Taizu, who had unified the realm.

“How noisy.”

At the Emperor’s quiet murmur, everyone prostrated themselves, barely daring to breathe.

“We beg Your Majesty’s forgiveness!”

“Please execute us!”

*Rustle.*

The Emperor gave a small shake of his head and silently waved his long sleeve.

Those who understood the unspoken command backed away and disappeared with careful steps. Before long, only two people remained in the vast main hall.

“Every time I say anything, they start begging me to kill them. If I’d had to listen to that for another fifteen minutes, I might’ve bitten through my own tongue.”

At the Emperor’s bitter smile, Baek Yeon, Commander of the Embroidered Uniform Guard, spoke with a stern expression.

“Even as a joke, please don’t say such things.”

“It’s only a joke. What does it matter? Besides…”

The Emperor leaned at an angle against the throne and continued.

“I have not the slightest intention of dying in a situation like this.”

His face was still pale, but as he faced a new crisis, his eyes gleamed like luminous pearls.

“I expected trouble, but this is beyond what I imagined. I didn’t think they’d move so quickly.”

Baek Yeon wholeheartedly agreed.

Dark Heaven.

That rebellious faction, whose very name was ominous, was larger than expected—and far more methodical.

Even more so than a religious movement that had once erupted like a grass fire from a distant western land, back when Baek Yeon had served the late Emperor.

“It was more than fifty years ago. That was when the people called the Demonic Cult headed for the Central Plains.”

“The Great Faction War.”

The Emperor murmured to himself and stroked his graying beard.

Though it had happened long before he was born, everyone knew of the momentous event when no fewer than a hundred thousand so-called heretics set foot in the Central Plains.

Especially because they weren’t merely country bumpkins lured in by sweet words. They were an army armed with unwavering faith and spears and swords.

“When the Demonic Cult’s momentum reached the heavens, the martial artists of the orthodox factions petitioned the late Emperor. They said the Demonic Cult was a foreign enemy disrupting the Great Nation’s order, and asked him to raise the Imperial Army and order a campaign against them.”

“I know.”

The Emperor looked at Baek Yeon and added,

“And I know you were the strongest opponent of joining the war.”

Baek Yeon gave a small nod in acknowledgment.

It was true.

Here, in this very place, the high ministers of the court had argued fiercely for days. The late Emperor had seriously considered ordering a campaign, but Baek Yeon had pleaded with him so earnestly—more than he had ever seen him do before—that the Emperor finally gave up the idea.

“Can Your Majesty guess why I opposed it so strongly?”

“I think there were two main reasons. The first was that the Demonic Cult feared the Great Nation’s power and wasn’t harming the people. And the second was… Cang Gong.”

“That’s right. Unlike me, Cang Gong was the first to insist that we drive out the foreign enemy.”

“You made the right choice. If Father had sided with Cang Gong back then, the Great Nation would have shed a great deal of blood.”

“It was clear he intended to weaken the imperial house. That was all the more reason I had to oppose it.”

There had never been a victory without wounds, not in all of history.

Baek Yeon knew that as a commander who led an army, not merely as a martial artist. He had done everything in his power to keep the Great Nation out of the war.

Cang Gong—or rather, the Eastern Heaven Demon Lord—had already been a person of interest back then.

Of course, countless orthodox martial artists had died because of Baek Yeon’s opposition. But he didn’t regret it in the least.

He had simply made the choice that was best for the Emperor and the Great Nation—and, by extension, the people.

It wouldn’t have been too late to intervene after watching the two great powers, the Murim Alliance and the Demonic Cult, crash violently into each other.

And the result of that wait had been an orthodox victory that came close to mutual destruction.

“Back then, I actually hoped the Demonic Cult would win.”

The Emperor clicked his tongue at Baek Yeon’s words.

“You’re unusually honest today.”

“It can’t be helped. Many martial artists of the orthodox factions have the people’s trust, so we’d have no grounds to launch a campaign against them. But it would’ve been different if the Demonic Cult had survived.”

A massive boulder was too heavy even to move.

But what about a pebble left behind after being smashed and battered again and again?

And if that pebble had jagged edges sharp enough to harm the people, Baek Yeon would have taken up his hammer without the slightest hesitation.

He would have torn down the lawless fence that was Murim once and for all.

“But if things had gone as you hoped, we wouldn’t have made it to the present day.”

The Emperor’s low voice echoed through the vast hall.

He was right. It was deeply ironic, but they had relied on those very martial artists to put down the traitors and accomplish their great undertaking.

And now… it was time to set that contradiction right.

“I intend to help with everything I have. For their sake—and for all of us.”

*Thump.*

Baek Yeon lowered his head and went down on one knee.

A storm of bloodshed would soon descend—one that would make the Great Faction War seem insignificant.

Dark Heaven was more powerful than the Demonic Cult, and incomparably more dangerous.

A war was beginning that would not be confined to Murim. It would overturn the world.

“Your Majesty, ruler of all beneath the heavens, I humbly ask that you give me your orders.”

The information Jin Taekyung had delivered in the dead of night was an unexpected misfortune. But it was fortunate that they had already made thorough preparations to accomplish their great undertaking.

Hundreds of warships and thousands of officers.

Hundreds of thousands of troops, the imperial banners flying above them, were waiting for their command.

“I command Baek Yeon, Commander of the Embroidered Uniform Guard.”

With a solemn voice, the Emperor slowly rose, his ailing body standing upright.

He was no longer wearing his white sleeping robe, embroidered with a golden dragon in silk thread. Now, clad in heavy armor, he strode across the hall without hesitation.

*Clank. Clank.*

One step. Then another.

The Emperor descended from the throne and personally raised Baek Yeon to his feet.

“Announce to the entire army that I will personally lead the campaign.”

“……!”

Baek Yeon’s eyes trembled for an instant, unable to hide his shock.

It wasn’t only the impact of the Emperor taking command in person. He could feel the resolve of a man who had little time left to live.

“Your Majesty.”

But the words Baek Yeon struggled to force out never came.

The loyal subject saw the Emperor silently shake his head. All he could do was clench his teeth, his heart heavy.

“I, Baek Yeon, Commander of the Embroidered Uniform Guard… will obey Your Majesty’s solemn command.”

The Emperor gave him a faint smile instead of an answer, then walked past him.

The world beyond the wide-open iron gates was still shrouded in darkness.

Just like his own future, brief and shrouded in darkness.

*Still, this isn’t so bad.*

His body might be dying, but his mind was clearer than ever.

The first campaign he would lead in person—and the last.

To meet his end on a battlefield instead of in bed would be a blessing, not a tragedy.

And so was the fact that someone had briefly brought his will to live back to life.

“Come, Baek Yeon.”

The Emperor smiled brightly—so brightly it was hard to believe he was a dying man—and continued,

“We should see off a certain insolent rogue who’s leaving before me without keeping his promise to me.”

* * *

One shichen.

That was how much time had passed since I’d first gotten my hands on the iron chest left behind by the Eastern Heaven Demon Lord.

“Everything’s ready.”

At Hyuk Mujin’s report in my ear, I opened my eyes, which I’d kept tightly shut.

The look in his eyes and his expression were unusually grave. They seemed to say everything about how urgently the situation was unfolding.

“Let’s go.”

What else was there to say?

I gave a brief reply and stepped out of the pavilion, moving as if in a daze.

Even after circulating my qi once, my mind was still a mess.

*Half a month.*

Only half a month.

That was all the time left until the Double Ninth Festival. Or maybe even less.

The missive the Eastern Heaven Demon Lord had kept said Dark Heaven’s main force would invade Shanxi Province through the northern grasslands before the festival.

*It could be ten days. No—even tomorrow.*

I swallowed the groan rising in my throat.

This wasn’t just urgent. It was an emergency.

The distance from here, Zhejiang Province, where the imperial capital stood, to Shanxi Province was a full ten thousand li.

No matter how quickly the Imperial Court’s messenger eagles flew, the trip would take at least ten days.

*Can I get there in time?*

Even as I left the imperial palace with everyone else, doubt weighed heavily on my heart.

Then Jeok Cheongang, who had been watching me in silence the whole time, suddenly spoke.

“Was it about fifty years ago? I got into some petty dispute with that Thunderbolt Saber King bastard and ended up in a real fight.”

As though he were talking to himself, Jeok Cheongang glanced away from me and continued.

“I’d always looked down on him as someone far beneath me, so I didn’t think much of him. But when we actually traded blows, he was pretty strong. I didn’t show it, but I was surprised.”

The Bow Saint, who had been riding quietly with the reins in hand, replied.

“He’s a strong man. If it hadn’t been for you, he probably would’ve been the greatest of the Ten Kings.”

“Hmm. I suppose so.”

Jeok Cheongang nodded, then glanced at me and added,

“Still, the Hebei Peng Family didn’t become one of the Five Great Families for no reason. With that kind of strength, they could beat just about anyone. And they have enough intelligence-gathering power to keep a clear eye on what’s happening not only in Hebei but in Shanxi, too.”

Only then did I think I understood.

This completely random conversation was all meant to put me at ease.

*Heh.*

What was I supposed to say? I was just grateful.

And just as I swallowed the dry laugh threatening to slip out, someone spoke.

“So, were you planning to leave just like this without saying goodbye?”

With a breezy voice that didn’t suit him at all, the Emperor laughed aloud. He’d been waiting for me in front of the enormous iron gates.
## Chapter artifact 941

# Chapter 941

An endless stretch of city wall, and a massive iron gate controlling passage to the north.

At the head of a thousand Embroidered Uniform Guards and several court ministers standing in formation on either side, the imperial banners bearing embroidered dragons held high, stood one man.

“So, were you planning to leave just like this without saying goodbye?”

The Emperor’s sudden appearance caught me off guard. Then, following his smile, I let a faint one settle on my own face.

“Your Majesty.”

“I hope I’m not taking up your precious time.”

“My time is precious, but if it’s only for a little while, I’ll spend it on a precious meeting. As it happens, there was something I needed to tell you in person, too.”

The Emperor tilted his head, not quite grasping what I meant, then smacked his lips.

“You speak as if you knew I’d be waiting.”

“Honestly, I didn’t expect that much. But I’m glad I get to see you, even like this.”

“Enough of that empty flattery. It doesn’t suit you.”

The Emperor feigned a frown, then jerked his chin over his shoulder.

“Why not answer honestly, like you usually do? In truth, it isn’t me you’re glad to see. It’s them.”

He was right.

The Emperor wasn’t the only one waiting for me in front of the North Gate of the imperial capital.

*That’s…*

Familiar faces came into view.

The Thousand Captain of the Embroidered Uniform Guard, Jeong Hogun—the first face I’d seen at the imperial court, and the one I’d seen most often since—was only the beginning.

Baek Yeon and Hong Jin, who should have been busier than anyone else right now, were there, too. And I spotted someone I hadn’t seen in the past few days.

*Prince Shangshan. No—the Crown Prince.*

Warmth spread through a corner of my heart. That boy, whose life had once hung by a thread, was now beside his only family.

And I’d get to say goodbye before I left.

I gave Zhu Bao, who sat astride his horse and looked ready to burst into tears, a faint smile. Then I turned back to the Emperor.

“May I answer honestly, as you said?”

“No, never mind. I’ve changed my mind.”

“I’ve changed mine, too. You’re right—I’m happier to see them than I am to see Your Majesty.”

“How dare you…!”

His suppressed voice was accompanied by an air that instantly turned cold.

But the Emperor, who had glared at me with a rigid expression for just a moment, suddenly burst into the laughter he’d been holding back.

“You never cease to amaze me. No—your behavior is downright bizarre. How can you be so arrogant and rude to the father of all the people and the supreme ruler?”

“As I’ve already told you, I’m nothing more than a mere rogue. I don’t even have an identity plaque, and I have parents of my own.”

At my unhesitating reply, gasps escaped from here and there.

Most of the people—especially the court ministers who had no idea why they were even here—looked at one another as if to ask whether this was really happening.

The Emperor, of course, was still smiling.

“I understand now. You are neither my subject nor a citizen of the Great Nation.”

Without waiting for my reply, the Emperor continued.

“But you think and act according to justice, righteousness, and chivalry. You are truly a hero of your age, worthy of the admiration of all.”

Clip-clop. Clip-clop.

The Emperor rode slowly toward me until he was right in front of me. He gazed at me for a moment, then suddenly raised a hand to his shoulder.

*Slip. Thump.*

The tightly tied cord came loose. Without the slightest hesitation, the Emperor removed his own cloak and held it out to me, smiling faintly.

“What are you waiting for? Take it.”

“……!”

“……!”

An unseen shockwave swept through everyone.

The court ministers were trembling as if they’d been struck by a stroke. They could hardly believe their eyes as they stared at the cloak embroidered with a golden dragon that looked ready to spring to life.

“Y-Your Majesty!”

“T-That is…!”

Shouts came from every direction.

But their desperate voices were swallowed by the wind at the Emperor’s curt command.

“Enough.”

In the heavy silence pressing down on those around us, the Emperor turned his gaze to me and spoke.

“Take it. It’s only a small gift from me.”

I looked from the Emperor, who was urging me on, to the cloak in his hand. All I could do was blink.

Even without everyone’s vehement reaction, I knew this wasn’t some simple gift.

“This is… pretty far from ‘only a small gift.’”

It was no ordinary cloak.

The fact that the Emperor himself had worn it already made it impossible for it to be an ordinary thing. But there was something even more important.

A dragon.

A dragon embroidered on the cloak in golden thread.

Even a three-year-old knew that this was the emblem of the Son of Heaven and the authority of the imperial house.

“You seem to know what it means.”

I could only stare at him in disbelief.

“How could I not?”

“Good. Then you’ll be all the more eager to accept this precious gift before my hand falls off.”

“Wait, wait a moment.”

Taken aback by this sudden turn of events, I hesitated, but the Emperor was firm.

“Please don’t refuse. If you do, something will happen that you’ll deeply regret.”

“What?”

I stared at him blankly. The Emperor continued in a deliberately stern voice.

“If you refuse even this, I’ll be very hurt.”

“What does that—”

“No one can say what might happen. But rest assured. Surely I wouldn’t make the imperial house’s Benefactor uncomfortable over something so trivial?”

“Is it just me, or does that not make me feel reassured at all?”

“Exactly. That’s all in your head.”

The Emperor and I stared at each other in silence for a while.

Then, as if we’d agreed to it, we both let out a dry chuckle.

Though we hadn’t known each other long, we already understood.

Maybe, just a little…

*That we were alike.*

I had fought to protect what was precious to me. He, too, had made sacrifices for someone else.

He’d wagered his life without hesitation, and he didn’t regret that choice.

The only difference was where we stood and what we saw. Just like me, the Emperor was only human.

Someone who knew how to be grateful for help, who liked jokes, who feared death.

Just one person who had fought as best he could from the place he stood.

*Swish.*

I reached out, took the cloak the Emperor offered, and draped it over my shoulders. Then I respectfully clasped my hands in a salute.

“I gratefully accept this precious gift.”

“It suits you. But there’s one thing missing.”

The Emperor looked at me in my cloak with satisfaction, then took a gleaming silver plaque from between the plates of his armor and held it out.

The next moment, he said something that made me doubt my own ears.

“By the Son of Heaven’s authority, I appoint Jin Taekyung of the Jin Family of Taiyuan Marquis of Shangshan!”

His voice, strengthened with internal energy, shattered the deep night.

His cry rang out without end. Commoners who had watched the Emperor’s procession from a distance, not daring to approach, began gathering around the torches held by the Embroidered Uniform Guards.

As the Emperor’s solemn declaration continued to echo—

“I grant you as your fief more than ten counties, including Taiyuan in Shanxi Province, Honju, Yangcheon, Jeongyang, Jinzhong, Taigu, and Jiaocheng, along with ten thousand households for your stipend and a hundred thousand taels of gold and silver. In addition…”

*Shing.*

A flash of light suddenly leapt from his waist. The Emperor drew the imperial sword, his eyes gleaming as he shouted,

“From this moment, I also appoint you Thousand Captain of the Embroidered Uniform Guard. Lead a thousand guards and, in accordance with the imperial command, swiftly put down the foreign bandits who disturb the order of the realm!”

“……!”

“……!”

I could hardly breathe. My heart pounded.

*Thump. Thump. Thump!*

It wasn’t the sound of my heart.

The thousand Embroidered Uniform Guards standing in formation on either side stamped their feet with all their might. They clashed their weapons together and struck their armor.

For the Emperor.

No—for me.

*Ah.*

I swallowed the groan rising in my throat.

Only now did I understand.

The Emperor hadn’t brought a thousand Embroidered Uniform Guards here to wait for me just as an escort.

They were an army assembled by imperial command to punish the enemy.

And at the same time, they were reinforcements prepared for me.

A shield and a sword to defend Shanxi Province and the Jin Family of Taiyuan against Dark Heaven.

“Waaaah!”

*Ding. Ding-ding.*

My ears rang.

From the incessant chime of bells. From the shouts and cheers erupting all around me.

And there, at the center of it all, the Emperor smiled at me.

“Success makes you a king; failure makes you a traitor.”

Two men had plotted a revolution, but only one had survived.

Having uprooted the traitors and restored everything, the Emperor hadn’t forgotten to reward those who had helped him.

“Everything comes at a price. So, what do you think of the gift I prepared?”

What more could I say?

I let out the breath I’d been holding and answered,

“It’s incredible.”

“As a marquis, you should rightfully be my subject, but I don’t care about that.”

*Tap.*

The Emperor’s hand came to rest on my shoulder. His life force was slowly fading, and yet I could feel the warmth that reached me through his fingertips.

“Go on as you have until now.”

Keep your eyes on what is right. Let your intentions and actions follow righteousness and chivalry.

Along with his voice, flowing like water, the Emperor added quietly,

“Be not my subject, nor my citizen… Just be one person who shines brightly in this world.”

His words, low and heavy, rang in my ears like a final testament.

* * *

Meeting and parting are inseparable.

Where there’s a meeting, there’s a parting; and after a parting, another meeting awaits.

Even so, the moment of parting is always bitter and full of regret.

Especially for a child saying goodbye to someone he had relied on so deeply.

*Tap. Drip.*

Moisture fell onto the saddle.

Rather than look at his youngest brother’s silently weeping face, the Emperor gazed at the empty places left by those who had departed and spoke calmly.

“Are you really that sad?”

“N-no, I’m not.”

Zhu Bao hurriedly wiped his eyes with his sleeve.

A child was allowed to cry, but the Crown Prince was different.

As heir to the Great Nation, Zhu Bao would have to face the coming war. He had become someone who must never cry.

“I’m not sad at all.”

“That’s very strange.”

“Pardon?”

“I’m nothing but regretful, yet how can you, who haven’t even reached the age of fifteen, not be sad?”

Zhu Bao looked up in surprise. The Emperor’s smiling face was reflected clearly in his eyes.

“Bao’er.”

The Emperor spoke gently to Zhu Bao, who was staring at him blankly, having forgotten to answer.

“You don’t have to force yourself to swallow your feelings already.”

“……!”

“People say endurance is bitter and its fruit sweet, but endurance piled up like that will one day turn to poison.”

“Hyung… I mean, Your Majesty.”

“When you want to cry, cry as much as you like.”

*Tap.*

With an awkward hand, the Emperor stroked Zhu Bao’s head. Then he turned his horse around and rode away.

Along with a few words he’d once heard from someone.

“You and I are both, in the end, only human.”

As he heard the sobs rising behind him, the Emperor thought to himself:

He hoped Zhu Bao—his youngest brother—wouldn’t follow the same path he had.

*I… realized far too late.*

And just then, as a faint smile touched the Emperor’s lips, a magnificent horse came galloping through the enormous iron gate, which was slowly closing behind him.

*Wait. That man…*

Amid a situation he couldn’t understand, the Emperor saw the man who had returned and asked,

“Did you leave something behind, Divine Physician?”

“Yes.”

The Divine Physician smiled and continued,

“I left a patient behind.”
## Chapter artifact 942

# Chapter 942

“I left a patient behind.”

At the Divine Physician’s answer, the Emperor’s eyes trembled.

*Could it be…?*

Suddenly, he found it hard to breathe.

Without even realizing it, his fists clenched.

A spark of hope kindled in a heart he’d thought he’d emptied completely.

The Emperor could feel his resolve wavering—the resolve to die on a battlefield, not in his bedchamber.

*No. It can’t be.*

But deep down, the Emperor could only shake his head.

A crisis could drive a person to the edge of a cliff. But it was hope that finally sent them plunging into the abyss.

And so, even now, the Emperor forced himself to look away from the Divine Physician, who gazed back at him with a gentle smile.

“If you intend to join the military camp, I won’t stop you. Before long, there will be countless casualties, and your medical skills will be put to good use.”

“Your Majesty.”

Leaving the Divine Physician with more to say, the Emperor quietly turned away.

Jin Taekyung wasn’t the only one whose every moment mattered—the one who had left to protect the Jin Family of Taiyuan.

The Emperor’s life was truly drawing to a close.

In the brief time he had left—just a few months at most—he meant to finish everything he could.

For a better future.

For the precious people who would remain in this world after he was gone.

*That is my sole duty.*

It was at that very moment, as the Emperor steeled his resolve again, that a quiet voice sounded behind him.

“I understand, Your Majesty. I understand how you feel.”

Thud.

The Emperor’s brisk stride came to an abrupt halt.

The Divine Physician’s voice continued in his ear.

“A fleeting hope must frighten you. Nothing is more painful than a false hope.”

After a brief silence, the Emperor slowly turned around. The Divine Physician was still facing him with a gentle smile.

“You understand well.”

“Through no choice of my own, I came to.”

“You must have. As a physician, you must have met countless people standing at the crossroads between life and death.”

“That’s not the only reason.”

“Then what is?”

For an instant, the Divine Physician’s smile faded.

“A very long time ago, there was a young carpenter.”

“A carpenter? Did he come to you because he had a fatal illness, too?”

“More precisely, he came to save his wife and children from an epidemic.”

“……His wife and children.”

“They say he carried his wife, burning with fever, and his two children on a wooden frame, and climbed the mountain for three days and nights without sleep. He was trying to find a renowned physician who was staying in a nearby settlement of slash-and-burn farmers.”

The Emperor pictured the carpenter, drenched in sweat as he climbed the mountain, and muttered,

“That must have been hard. Very hard.”

“As you say, it surely was.”

“But that carpenter probably couldn’t even feel his exhaustion. He had hope that he could save his family.”

The Divine Physician nodded.

“Yes. That’s right. He didn’t set down his load and collapse until he’d finally reached his destination. Then he lay sick for a full day and a half.”

“So, did you treat the carpenter’s family?”

“Unfortunately, I couldn’t.”

The Divine Physician added bitterly, facing the Emperor, who let out a small sigh.

“By the time I finally regained consciousness, it was too late for everything.”

“……!”

“That’s why I understand so well how cruel hope can be. And what despair waits at the bottom of that cliff.”

The Emperor fell silent.

He gazed at the old physician before him—and at the young carpenter who had lost his family to the epidemic so long ago and chosen a new path. After a long while, he suddenly spoke.

“Then, does that mean you really have…?”

His voice trembled with an agitation he could not hide. He forced out the one question he’d wanted to ask from the very beginning.

“Have you found a way to treat Us?”

A light appeared in his once-subdued eyes, and hope crept into his voice.

The Divine Physician bowed deeply before the Emperor and answered.

“Yes. With the help of Heaven—or rather, Young Master Jin—I was able to find the one and only path to survival.”

“……!”

Jin Taekyung.

At the unexpected name, the Emperor closed his eyes without meaning to.

In the darkness before him, he pictured Jin Taekyung’s face and offered a silent word of thanks.

*You didn’t forget. You kept your promise to Us.*

Even as Jin Taekyung left, the Emperor had never resented him.

He’d watched Jin Taekyung walk away without a word about the promise between them, and could only be grateful for everything he had done for the imperial house.

He’d believed that was his duty—as ruler of this nation, as an older brother, and as a human being.

But Jin Taekyung had kept his promise to the Emperor after all.

He had given the finest physician beneath Heaven a hope that shone brighter than ever and sent him back.

*What more must I do for him to repay this debt?*

It didn’t matter.

Whatever Jin Taekyung wanted, the Emperor would gladly give it to him.

With a quiet chuckle, the Emperor opened his eyes and slowly spoke.

“Tell Us. What must We do to live?”

And in that instant, the Divine Physician’s smile seemed to turn strangely awkward.

“What is it?”

“Well, it’s… that is…”

“There’s no need to hesitate. We’ll believe and follow your instructions without the slightest doubt.”

“I’m sorry, but even so, there may be a slight misunderstanding…”

The Emperor could well imagine what was making the Divine Physician hesitate.

It happened all the time.

He was the Emperor, ruler of all beneath Heaven. If anything at all went wrong with the Emperor’s health, the imperial physicians might have to prepare for death themselves.

Even the finest physician beneath Heaven couldn’t help worrying about what might come after.

“Whatever you’re worried about, I assure you that nothing unfortunate will happen. We swear by Our name… No, We swear on the tombs of the late Emperors.”

At the Emperor’s gentle reassurance, the Divine Physician—who had been silently moving his lips for some time—carefully spoke up.

“Are those words truly sincere? Without the slightest falsehood?”

“Of course. From this moment on, We are a patient in need of your treatment before We are the Son of Heaven. We’ll trust you and follow your instructions, whatever they may be.”

“Very well. Since Your Majesty has gone so far, I’ll speak frankly, too.”

And in the next instant, the Emperor understood.

Why the Divine Physician had been hesitating so much.

And just how understated the words *a slight misunderstanding* had been.

“The truth is, there’s no way to save Your Majesty.”

“……?”

“To treat you, you’ll have to die once first. That’s where it begins—Your Majesty?”

The Emperor blinked. Somehow, a treasured sword had appeared in his hand.

“Wait, why is this—”

“Your Majesty? Your Majesty!”

“I’m sorry, Divine Physician. But I didn’t draw this of my own will. The sword’s moving by itself.”

“Your Majesty!”

Watching the Emperor approach with his sword, uttering words that even a passing traitor wouldn’t believe, the Divine Physician let out a shrill scream.

At the same time, he thrust out the thing he’d taken out earlier, just in case—the thing Jin Taekyung had handed him a few hours ago.

Or, more accurately, he hurled it at the Emperor.

Clack.

The Emperor reflexively reached out and caught the flying object.

*Rattle!*

The cord holding it in place came undone, and a bamboo slip unfurled—so old it had half rotted away.

“……What is this?”

For an instant, the Emperor was puzzled.

But as soon as he made out the faint characters that remained, his eyes widened.

Maoshan Sect.

White Illusion Jiangshi Art.

It was the ancient root of a sect belonging to someone who no longer existed in this world, and who had treasured it dearly.

* * *

*Dududududu!*

The thunder of galloping hooves rang out in the darkness.

The fine horses, said to have descended from Ferghana horses, lived up to their reputation. Not one of them stopped for even a moment, and none of us—including me—slackened our reins.

“Deokcheong County is just beyond that hill!”

Ju Hwaran’s shout suddenly cut through the wind rushing past us.

It was good news: we’d reached our second county just one shichen after leaving the imperial capital. But I couldn’t bring myself to smile.

*Not yet. At this speed, I can’t even be sure we’ll reach Anhui Province by noon.*

It wasn’t nearly enough.

Not the speed. Not the time.

Even the imperial messenger eagles and couriers who had left the capital about half a shichen ahead of us might not arrive before the fighting began.

We had to move as fast as possible.

“Commander Jeong!”

At my call, infused with internal energy, Jeong Hogun—his helmet pulled low over his brow—rode up beside me.

“Speak.”

“How long do you estimate until we reach Shanxi Province?”

Jeong Hogun thought for a moment in the saddle as his horse raced onward, then gave a short answer.

“At least ten days. As many as fifteen.”

A difference of no less than five days.

And I could tell well enough that fifteen days wasn’t some leisurely estimate, either.

“Be more specific.”

“Fifteen days, assuming we change horses promptly at counties with prepared relay stations and take only the bare minimum of rest.”

“Damn it. And ten days?”

“That would mean traveling only the shortest possible straight-line route. We’ll have to cross rugged mountains and rivers, so depending on the conditions, we may have to abandon our horses…”

Jeong Hogun’s voice trailed off. He glanced at the thousand Embroidered Uniform Guards charging forward as one with their horses, then at the Fire Dragon Pavilion members following behind them, and continued,

“And we can forget about rest.”

His expression and tone were as impassive as ever, but his concern came through clearly.

No, I couldn’t miss it, either.

*Reaching Shanxi Province won’t mean everything’s over.*

We didn’t know exactly when Dark Heaven would invade Shanxi Province.

If Heaven was on our side and we arrived before the fighting began, with enough time to rest, that would be fortunate. But there was every chance the opposite would happen.

*If Dark Heaven has already taken Shanxi, or we arrive just as the battle begins…*

There was no need to finish the thought.

I spat out the curse that had been circling in my mouth for a while.

“Goddamn it.”

*Shhk!*

Jeong Hogun cut through a branch hanging over the road, spat out a leaf that had flown into his mouth, and replied,

“I understand how you feel, but I doubt you called me over just to say that.”

His tone was so cold it made me dislike him on the spot. I felt my overheated thoughts cool down.

“Shit. This sucks.”

“Good. Are you done feeling sorry for yourself?”

“You cold bastard.”

“……”

“You can’t even show a little sympathy. No wonder you don’t have a single friend.”

“……No, I don’t think that counts as feeling sorry for yourself.”

“Of course it does. That was just me feeling sorry for myself.”

At my firm reply, Jeong Hogun pressed his lips together.

The eyes visible through his helmet looked a little sad. That had to be my imagination.

*Anyway, in that case…*

Ignoring Jeong Hogun’s reaction, I made a quick decision.

“We’ll split up as soon as we pass through Deokcheong County. We have too many people.”

“You mean we should split the troops…”

“All of you. And three others.”

“What?”

At Jeong Hogun’s question, I pointed toward two figures racing ahead in the distance.

“Three of us will be enough to get there first.”

Not sure if you’ve heard the saying:

The Fire King on the left, the Bow Saint on the right.
## Chapter artifact 943

# Chapter 943

“You can’t be serious!”

The moment my brief explanation ended, Hyuk Mujin cried out, his face stiff with shock. Then he let out a sigh.

“But… damn it.”

He said no more, but everyone here could tell he’d accepted reality.

“If you charge ahead in your haste, you’ll trip over a rock. I know everyone’s upset, but for now, this is the best decision.”

Namho addressed everyone with a serious expression.

It might have sounded like a speech from a seasoned elder—if he hadn’t been tucked into Taishan’s arms like a baby kangaroo.

“…I’ve been meaning to ask. Why are you sitting like that?”

“This is the most comfortable.”

Namho answered with unnecessary firmness, then added,

“If I ride in the back, my ass feels like it’s going to get crushed. If I sit on this fellow’s shoulder, I get smacked in the face by a branch every fifteen minutes. An old man like me would be dead before we even reached Shanxi Province.”

Taishan, whose thighs were softer than a leather sofa, nodded.

“Taishan save Namho.”

Since when had those two gotten so close?

I was still wondering why Taishan looked downright solemn when Namho smiled with satisfaction and pulled something from his pack.

“You’re a good boy. Open wide. Five-spice pork coming in.”

“Oh! Five! Spice! Pork!”

“…”

Right. I’d been wondering why something felt off.

I shook my head and eased my horse’s pace for a moment before speaking.

“Elder Namho, please make contact with the Murim Alliance as soon as you leave Zhejiang Province. They’ll be making preparations of their own.”

“I intended to do that anyway. As things stand, I’d only be a burden. I’ll try to lead the reinforcements and follow behind you.”

There wasn’t a single martial artist to be found in Zhejiang Province, where the imperial capital stood—not even a sect.

But Anhui and Henan, which lay along our route to Shanxi Province, were another matter.

Henan was home to the Murim Alliance headquarters, of course. And the great tree closest to our current position was the Nangong Family.

“Ilseom. Ma Pyo.”

At my call, Song Ilseom and Sama Pyo rode over and answered in turn.

“I’m listening, Pavilion Master.”

“I’ve lost count of how many times I’ve said this, but Sama is your surname, not your given name. Next time you call me…”

“I know. I’m doing it on purpose.”

At my firm reply, Sama Pyo muttered as if to himself,

“Yeah, I thought that might be the case.”

“Enough. I trust you both know what you have to do.”

Song Ilseom and Sama Pyo.

Despite their youth, both were formidable martial artists. They nodded solemnly.

“Of course.”

“Trust us. Even if something goes wrong along the way, we’ll get everyone to Shanxi Province without a problem.”

I answered their determined assurances with,

“Don’t fight with each other.”

“…”

“…”

“Don’t start bickering in front of the Embroidered Uniform Guards. It’s embarrassing. Got it?”

“…”

“…”

“Answer me.”

The two of them stared at me with flat expressions, then let out quiet laughs. They both knew better than anyone that I was only joking.

“Understood.”

“I’ll try.”

“Did you hear that, Mujin?”

Hyuk Mujin, who’d been watching me in silence, gave a small nod.

He understood the situation and didn’t say anything more, but there was no hiding the emotions in his troubled expression.

His resentment toward me for leaving him behind without hesitation, and his anger at himself for being nothing but a burden in the current situation.

“Quit looking so miserable. Your face is ugly enough already—you’re making it look even worse.”

I gave him a wry laugh. Hyuk Mujin’s expression darkened further.

“Is that all?”

“Hm?”

“Why… haven’t you asked me to do anything?”

The smile I’d been forcing onto my face loosened.

The question caught me by surprise—and, in a way, left me at a loss.

I hadn’t expected him to think of it that way.

After looking at him in silence for a moment, I answered calmly.

“Because even without me asking, you’ll do just fine on your own.”

“…”

“Shanxi Province is where you’ve lived your whole life, and the Jin Family of Taiyuan is your second home. I know well enough how you feel right now.”

Hyuk Mujin’s eyes trembled as he looked at me.

Crack.

His fists were turning white.

He glared at the reins, pulled so taut they looked ready to snap, and muttered in a quiet voice,

“Captain, you wouldn’t understand. What it feels like to have something you must protect, but not the strength to step in—to be left helpless, just watching.”

“…What?”

“No, forget it. I said something stupid. You’re the one who has it hardest right now… I sincerely apologize.”

I silently watched him bow his head, his face red.

I wanted to tell him:

I understood that feeling, too.

I’d felt it all too clearly—as my soul shattered and every bone in my body broke.

But I couldn’t bring myself to let the truth on the tip of my tongue escape.

Sometimes, comfort from the strong can make the weak feel even more powerless and wretched.

And the cruel truth that you can still fail to protect something even when you have the strength to fight—that was something Hyuk Mujin couldn’t understand yet.

So the only thing I could do was offer one short line to the man who couldn’t lift his head, weighed down by shame and guilt.

“I trust you. More than anyone.”

“…Captain.”

“I’ll see you in Shanxi—or rather, at the Jin Family of Taiyuan.”

Pat.

I patted his trembling shoulder in farewell, then kicked my horse forward.

The wind felt colder than before. I tightened my grip on the reins, and hoofbeats approached. A quiet voice reached my ears.

“Young Hero Hyuk didn’t mean what he said.”

It wasn’t just the hoofbeats drawing closer.

I caught the scent of flowers drifting from somewhere and managed a smile.

“I know.”

“Do you know something?”

“What?”

I turned, puzzled, and saw Ju Hwaran beside me, her expression calm.

Her voice was just as quiet.

“Some kinds of smiles can look so fragile they almost seem ready to break.”

“…”

“I want more than anything to go with you, too, but I know I’d only be a burden, so I won’t complain. Still…”

Ju Hwaran smiled.

Like moonlight spilling down from the sky.

“When we meet again, let’s meet with genuine smiles. Both of us.”

I watched her in silence, then suddenly spoke.

“That’s exactly what we’ll do. I promise.”

And in the next instant, I sprang from the saddle without a moment’s hesitation.

Whoosh!

Cold. The fierce wind whipped my hair around.

As a weightless feeling swept over me and I leapt high into the air, two pale figures followed behind, chasing me through the hazy moonlight.

“Come on. Let’s hurry.”

At Jeok Cheongang’s low voice, the Bow Saint quietly nodded.

I—or rather, we—shot toward the rugged mountain range where no horse could travel.

* * *

“Well, that’s strange.”

At the sudden mutter from his companion, the bandit leaning against a tree and nodding off opened his eyes to a slit.

“What is?”

He’d just woken from a light sleep. There was no reason he’d be in a good mood.

At the brusque voice of a senior bandit more than ten years his elder, his companion swallowed nervously.

“It’s nothing, sir. It’s just… the longer I’ve been here, the more something’s felt off.”

“Something’s off? I don’t see anything.”

The bandit tilted his head. His companion pointed up at the sky and continued.

“I haven’t seen any birds all day. It’s dead quiet. Doesn’t it feel a little unsettling?”

“Huh?”

The bandit’s eyes widened. Only then did he take a careful look around.

Now that he thought about it, it was true.

The sky was empty. And from the dense forest stretching in every direction, there wasn’t a single birdsong—though it should have been full of them.

*What’s going on?*

The question flashed through his mind.

But his face soon settled into indifference.

What difference would it make if a few birds were missing?

They called themselves bandits, but in the end, they were nothing but low-ranking thugs.

Their only job was to keep watch over their assigned stretch of mountain road until their eyes popped, and contact the mountain stronghold if any travelers showed up.

“Maybe a hawk came around. Those birds don’t want to get snatched up and eaten in the blink of an eye, so they’re keeping their beaks shut.”

“Oh, come to think of it, I did see a few hawks fly by earlier.”

“Earlier? When?”

“About two hours ago, I think. Four or five of them, flying like arrows.”

The bandit must have missed them while he was asleep.

He stroked his shaggy beard and muttered,

“That is a little strange. Those birds do whatever they want. I’ve hardly ever seen them travel in a flock.”

“Should I report it to the stronghold?”

“Report it? To the stronghold?”

“Yes. The deputy chief said we should report anything unusual right away.”

“Not a bad idea. If you’re hoping to get chopped up alive.”

“…”

“The deputy chief’s probably fast asleep by now. Wake him, and you won’t like what happens. Disturb him over something like that and he might throw an axe at you.”

The bandit let out a long yawn and sprawled out beneath the deep shade, stretching his arms and legs.

He’d slept sitting against a tree with last night’s hangover still weighing on him. His body was stiff. This time, he planned to sleep so soundly his back would hurt.

He left everything to his young companion, who still had plenty of enthusiasm.

“Quit straining yourself. Just keep an eye out for people. People.”

With the Double Ninth Festival coming up, merchants weren’t the only ones looking to score big.

The bigger the haul, the bigger the crumbs.

If they picked the right caravan—one belonging to a sizable trading company or Escort Bureau—the tolls alone would be enough to fill the stronghold’s storehouse.

Just like now.

“They’re—they’re coming!”

“What? What?”

Wham!

At his companion’s hushed cry, which rang out barely a moment later, the bandit sprang up as if he’d been launched from a catapult and grabbed his axe in a panic.

The sleep was gone from his eyes.

His gaze fixed on the shadowed mountain path, shining like a hawk’s.

“Contact the stronghold. Hurry!”

“Y-Yes, sir!”

The bandit glanced after his companion as he ran off, then narrowed his eyes at the mountain road.

He could see them. Clearly.

A few flags, swaying slowly.

And he could sense dozens of people.

*That idiot finally got one right.*

The bandit studied the flags fluttering between the branches.

Then he read the helpful lettering on the dark blue silk and learned the identity of these mouthwatering guests.

The Great Nangong Family.

“…”
## Chapter artifact 944

# Chapter 944

The Great Nangong Family.

The moment the bandit made out the five characters embroidered on the fluttering flag, only one thought came to mind.

*Wait. What’s the Nangong Family doing here?*

Of course, it wasn’t impossible.

This mountain range lay at the southeastern edge of Anhui Province, and the Nangong Family was, by any measure, the hegemon of Anhui.

Still, even after more than ten years of living in a mountain stronghold, the bandit had never once seen the Nangong Family’s flag appear nearby.

*Why would the Nangong Family come all the way out to a backwater like this…?*

Even if a tiger stays in its cave, every beast knows who their king is, who owns this mountain.

The Nangong Family was that tiger.

Not hidden away in a dark cave, but a beast that held Hefei, the heart of Anhui, and commanded dozens of sects.

One roar was enough to rally countless martial artists beneath the Nangong Family’s flag. That was the power and influence of one of the Five Great Families.

*There’s no reason for them to come all the way to these rugged mountains.*

The mountain range stretched from the west to the distant eastern edge, running for hundreds of li.

It was hard for a bandit to understand why the mighty Nangong Family had left the well-maintained main road behind and come here with only a few dozen people.

Of course, his fear—the kind that made his heart feel ready to burst—was even greater than his confusion.

*Goddamn it. What the hell could they possibly be here to take?*

Cursing inwardly, the bandit tried to steady himself and carefully backed away.

Fortunately, he was dozens of yards away, on a hill thick with brush. It wasn’t too difficult to retreat while holding his breath.

Rustle, rustle.

For the better part of fifteen minutes, he slowly backed away, avoiding the leaves and branches scattered across the ground.

Once he was sure he’d escaped the danger of being spotted, the bandit finally let out the breath he’d been holding.

“Hah… hah.”

His back was damp with cold sweat, and both legs trembled as if he’d suffered a stroke.

Only fifteen minutes had passed, but to a bandit who’d just escaped death, it felt longer than half a day.

“I-I’m alive. I’m alive.”

Gripping a nearby tree, he sighed with relief—then suddenly felt sorry for himself.

*You pathetic fool. What a sorry state you’re in.*

He didn’t regret becoming a bandit.

What could he do about it?

He’d somehow been born, somehow lived, and somehow ended up here.

Still, if he was going to make his living this way, he should at least have joined a sizable mountain stronghold.

If he belonged to one of the Seventy-Two Strongholds under the Green Forest Alliance, he wouldn’t feel his life was in danger just from seeing the Nangong Family’s flag.

*If you’re going to be a servant, you might as well serve at a lord’s manor.*

Had his drunkard of a father ever said anything that hit so close to home?

The bandit wiped his eyes with his ragged sleeve and started back down the rugged mountain path.

Whether it was a lord’s manor or a doghouse, in the end, it was just somewhere for a servant to live.

He had to hurry back to the stronghold and tell his brothers the news. They should be on their way here by now, having received the signal.

If they ran into the Nangong Family—not being members of the Green Forest Alliance—they’d surely be dead.

*Thank God there’s some distance between us. If I head back right now, we can all get away in time.*

And perhaps Heaven had been moved by this noble display of camaraderie, because before even fifteen minutes had passed, the bandit ran into the fifty or so brothers led by their imposing chief.

More precisely, he found their imposing chief sprawled out, while his brothers were, for some reason, lying with their heads pressed to the ground.

“I never meant to block your way, sir. So please, just—”

An unfamiliar back. An ominous feeling he couldn’t explain.

The deputy chief was earnestly explaining something to a bald man and a woman standing before everyone when he spotted the bandit watching blankly from some forty yards away. His eyes widened.

“Huh?”

Something was wrong. Something had gone terribly wrong.

The bandit sensed the danger by instinct and hurriedly spun around. That was when—

Poke.

A finger jabbed his cheek. An uninvited guest had appeared right in front of him and looked him over before asking,

“Who are you?”

“……!”

The bandit shuddered as if struck by lightning.

First, because he hadn’t sensed a trace of the man’s presence.

And second, because the uninvited guest was much younger than he’d expected.

*A master…!*

A chill ran down his spine.

Standing at the edge of life and death, the bandit barely managed to squeeze out his voice.

“I-I’m Jang Il. My name is Jang Il.”

The world was definitely unfair.

The man was absurdly young, stronger than he’d imagined, and even had the looks of a pretty boy who’d grown up in a courtesan’s house. He asked again,

“Good. Jang Il. What do you do?”

“Trees. Trees.”

“I asked what you do. What the hell do trees have to do with it? Are you a forest spirit? Jangquines, King of the Spirits?”

“N-No. I meant to say I’m a woodcutter, but…”

“Right, Jang Il. A woodcutter.”

The young man gave a small nod and glanced at the axe hanging from the bandit’s waist.

“You’ve got an axe, too. Because you’re a woodcutter, I suppose?”

“Y-Yes!”

“Then where’s your carrier frame?”

“…What?”

“Your carrier frame. Are you planning to haul all that firewood by hand after chopping it?”

“Well, I…”

The bandit hesitated, then hurriedly added,

“Down below! I left it down below.”

“You left it down below. Sure, that happens.”

The young man muttered and gave a little shrug.

“Then let’s ask.”

“……?”

There was no need to ask who he meant. Before the bandit could open his mouth, the young man called toward the thick brush.

“This woodcutter says he left his carrier frame down below. Did you happen to see it on your way up?”

At that moment—

Whoosh.

A gust of wind swept through the bushes, and a silver-haired, middle-aged man appeared as if from nowhere. He shook his head.

“I saw nothing. Aside from one bandit fleeing in a panic, that is.”

“Oh, dear.”

The young man glanced at the bandit, who looked ready to faint, and clicked his tongue. Then he respectfully clasped his hands toward the middle-aged man.

“Thank you for letting me know, Great Hero Nangong.”

The Family Head of the Nangong Family, the Heavenly Thunder Sword, Namgung Ryong, clasped his hands in return.

“It’s good to see you again, Blazing Flame Divine Dragon Jin Taekyung.”

* * *

No matter how vast the world, people with a connection are bound to meet again eventually.

Of course, this meeting wasn’t simply a matter of chance.

“We received word from the Anhui Provincial Office. Luckily, we were nearby, so we were able to reach you quickly.”

I nodded at Namgung Ryong’s brief explanation.

“So the messenger eagle reached the provincial office.”

“About two hours ago. They were in quite a state over there, saying the Son of Heaven had issued the order himself.”

Well, Namgung Ryong wasn’t Namgung Gil-dong[^1]. He couldn’t just pop up in the east one moment and the west the next.

[^1]: A play on Hong Gil-dong, a legendary Korean outlaw known for appearing in one place and then another.

The imperial messenger eagle, which had entered Anhui two hours ahead of us, had gone straight to the provincial office. After receiving the news, Namgung Ryong had immediately led his family members here. That was how it had happened.

“But how did you know where we were? Especially in a mountain range this damn huge.”

“No matter how wide it is, the paths are set. The terrain is rugged, but this was the fastest way for us to reach you.”

An answer befitting the head of the Nangong Family, who knew Anhui Province as thoroughly as the palm of his hand.

Even so, a dark shadow hung over Namgung Ryong’s face as he looked at me.

“Is it all… true?”

There was no need to ask what he meant.

The air had suddenly grown heavy when Jeok Cheongang spoke up.

“What, you don’t believe him?”

“Of course I do. I only wanted to make sure, because it’s a truth I can hardly bring myself to believe.”

Everyone felt the same way.

A storm of blood had already swept through Henan, Sichuan, and Yunnan, and even reached the imperial capital.

And before the stench of blood had faded, an even more terrible, even greater storm cloud was bearing down on us.

Especially as the head of a family, Namgung Ryong couldn’t help thinking of the many people who followed him.

“The Double Ninth Festival. The Double Ninth Festival…”

He muttered in a voice weighed down with thought, then looked at me with a troubled expression.

“My condolences. I never imagined they’d cross the northern grasslands and set their sights on Shanxi Province.”

After a brief silence, I spoke.

“They’ll be able to hold them off. They’re strong enough.”

Even as I said it, I knew the truth.

This was a lie meant to hide what I really thought—something closer to an attempt to comfort myself.

*The Jin Family of Taiyuan can’t manage it alone.*

Even Shaolin Temple, called the Mount Tai and Northern Dipper of the Murim, and the Sichuan Tang Clan, with its terrifying poisons, had suffered heavy losses.

Fortunately, Qingcheng, Emei, and the Nanman Beast Palace had kept their losses to a minimum and preserved their forces. But there was no denying that they’d faced a tremendous crisis.

And now, it was Dark Heaven’s main force.

This wasn’t an attack to steal a divine artifact or destroy a single prestigious sect. It was a true invasion, intended to establish a foothold for an advance into the Central Plains.

*At least ten thousand. Maybe more.*

Even the staggering number of ten thousand was only my hopeful estimate of the minimum.

If everything so far had been a mutation Gate, this was no different from a monster wave.

Just as the Demonic Cult had swept through the Murim half a century ago, leading a hundred thousand demonic fighters.

*Damn it.*

My chest felt tight. I couldn’t stop thinking that if I’d found the missive left by the Eastern Heaven Demon Lord even a little sooner—or if I’d logged out before then—we might have gained some time.

*Of course, it was already too late.*

I’d lost three full days unconscious, and the moment I checked the missive in the iron chest, the Quest that appeared locked the door connecting me to reality.

It had taken away my last refuge, my place of rest, and forced me to move forward.

As if this were the only path I’d been given.

*Then… I’ll have to run. With everything I’ve got.*

Quietly clenching my fist, I turned to Namgung Ryong, who seemed unable to find the words.

With the faintest glimmer of hope, I asked,

“Where is the Azure Sky Sword King?”

Nangong Cheon, the Azure Sky Sword King.

A Supreme Peak master counted among the top three of the Ten Kings, and the Grand Family Head of the Nangong Family.

If he joined us and traveled with us to Shanxi, we could hold off even more enemies than we’d expected.

I already had two peerless fighters at my side, each a match for ten thousand men: the Fire King and the Bow Saint.

But the hope I’d briefly allowed myself to feel soon faded into nothing when Namgung Ryong’s answer came with a quiet sigh.

“My father has been away from the family estate for the past couple of months.”

“Ah.”

“I’m afraid we don’t even know where he is right now. All we know is that he took on a mission at the request of Great Hero Mae Jonghak, the Alliance Leader.”

I hadn’t expected everything to go so smoothly, but I couldn’t help the disappointment that quietly rose in me all the same.

“I see.”

“Still, as Family Head of the Nangong Family, I’ll help you and the Jin Family of Taiyuan. I’ve had fine horses, a reasonable supply of food, and a family member to guide you by the fastest route standing by, so you can set off at once…”

Just as Namgung Ryong began to continue—

Grrk. Krrk.

With a muffled, strangled growl, a figure rose from the shadows.

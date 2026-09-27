# Checkpoint Review — 1075–1079

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

# Chapters 1075–1079

## Plot

At the lakeside camp, Taekyung reunites with Gung Gibang and learns that the Slaughter Saint and Cheongpung arrived in Qinghai about a month earlier to investigate possible spies. They found none, but a strange, chilling presence kept them from reaching Taiqing Hall. Kunlun Sect Leader Cheongheoja arrives by ship and says more vessels are coming to evacuate the roughly three thousand allies. He confirms Hak Woo is safe and will meet Taekyung after they leave. In private, Cheongheoja warns his disciple of a hidden ember that could bring disaster.

Elsewhere, Ma Sanbao uses a ritual bell to command mutated birds and raise surviving monsters. He finds most of his men dead, their wounds apparently inflicted by the Slaughter Saint, and learns one operative and all their bells are missing. Ma expects Taekyung to make the captive betray them, but dismisses the danger of the bells being used.

Crossing Qinghai Lake, Taekyung meets Hak Su, Cheongheoja’s Senior Disciple and Hak Woo’s senior brother. Taekyung doubts the Central Plains can send its full strength against Dark Heaven, which can use the Moving Formation. He and Mujin retrieve their bound black-robed captive from the lake. After rough interrogation nearly kills him, a physician revives him and repairs his tongue; Taekyung tells Mujin to question him.

The allies arrive in Xining to a vast welcome from people across Qinghai. Knowing the city is a last stronghold against Dark Heaven, Taekyung promises Cheongpung they will do everything they can, even at the cost of their lives.

## Continuity

- The allies have reached Xining, Qinghai’s capital and a last stronghold against Dark Heaven; crowds from across the province have gathered there.
- The Slaughter Saint and Cheongpung found no identifiable spies, but their investigation remains unresolved. A strange presence prevented them from reaching Taiqing Hall.
- The allies’ roughly three thousand fighters are being evacuated across Qinghai Lake by ship. Cheongheoja says Hak Woo is safe and will meet Taekyung after they leave.
- Cheongheoja warned of a hidden ember that could turn everything to ash; its meaning remains unknown.
- Ma Sanbao serves the Lord of Heaven, can raise the dead, and commands beasts with a ritual bell. His operative and the group’s bells are missing; he attributes the dead men’s wounds to the Slaughter Saint.
- Hak Su is Cheongheoja’s Senior Disciple, Hak Woo’s senior brother, and a possible successor to Kunlun’s leadership.
- Taekyung believes the Lord of Heaven wants him alive, but does not know why.
- The black-robed captive survived the interrogation and treatment and can speak; Mujin is to question him.

## Translation Decisions

- Use “magical power” for 마력 and “concealment technique” for 은잠술.
- Render 능공허도 as “Gliding Across the Void,” distinct from 허공답보 (“Stepping on Empty Air”).
- Use “Lord of Heaven” for 천주 and “Slaughter Saint” for 살성.
- Use Hak Su for 학수; Taekyung’s mistaken 학소 (Hakso) is a name-confusion joke.
- Keep Taekyung’s belief that the Lord of Heaven wants him alive framed as his belief, not confirmed fact.
- Render 서녕 as Xining.

## Durable state

{
  "active_continuity": [
    "The party has arrived in Xining, Qinghai's capital and a last stronghold against Dark Heaven; crowds from across the province have gathered there.",
    "Hak Su is Cheongheoja’s Senior Disciple, Hak Woo’s senior brother, and a possible successor to the Kunlun Sect leadership.",
    "Taekyung believes the Lord of Heaven does not want him killed, but does not know why.",
    "The black-robed captive survived the interrogation and treatment and can now speak; Mujin is to talk with him."
  ],
  "continuity_sources": [
    1078,
    1079
  ],
  "open_questions": [
    "Who is the black-robed captive, and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?"
  ],
  "safe_through": 1079,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1075

# Chapter 1075

Sometimes the people you’d put off seeing for a while all come flooding back at once.

Like right now.

“I’m Gung Gibang, a junior of Murim. It’s an honor to meet you, Seniors!”

At Gung Gibang’s hearty greeting—he’d run here so fast his feet must’ve been on fire—I spoke on everyone’s behalf in a stern voice.

“The Beggars’ Sect’s Successor Beggar, is it? Good. Pleased to meet you.”

“……”

“I’m Jin Taekyung. We’re about the same age, so from now on, feel free to call me Elder.”

“……You haven’t changed. Not one bit.”

I shrugged at the guy, whose already ugly face had twisted into an expression like he’d just swallowed shit.

“Of course I haven’t. If a perfectly normal person suddenly changes, it means he’s about to die.”

“I don’t think you were ever perfectly normal.”

“I was a lot better than you.”

“In what way, exactly?”

“There are plenty, but let’s start with our looks. We’re on completely different levels.”

“Damn it. I can’t deny that one.”

Gung Gibang let out a deep sigh, then chuckled.

“Still, I’m glad. You haven’t changed.”

I laughed along with him.

Those words—I haven’t changed—felt good to hear.

And I felt the same way.



* * *



Gung Gibang and the Beggars’ Sect disciples led us over to the campfires.

A winter-cold blizzard was howling all around us, but the warmth of the fires springing up here and there was enough to make us forget the cold. They’d also laid out dry rations to replenish our exhausted allies’ hunger and strength.

And plenty of them.

“Were you waiting for us?”

“Of course. We expected reinforcements to come from Gansu.”

Gung Gibang handed me some jerky and added:

“We even figured those reinforcements might make the insane choice of crossing the Qilian Mountains.”

“Was that too hasty a judgment? The missive from the Kunlun Sect made it sound like every second counted.”

“No. It was exactly the right call. We only got a chance to catch our breath a few days ago ourselves.”

As if to prove he wasn’t lying, a scab of dried blood still clung to Gung Gibang’s forehead.

A clear mark of battle.

His expression and voice were bright, but there was no doubt he’d recently fought a desperate battle for his life, too.

“Oh, this? It’s nothing. Don’t worry about it. I survived, and that’s what matters.”

Gung Gibang put on a somber look with a bitter smile. I looked him up and down and replied:

“Yeah. It really is nothing.”

“……”

“What?”

“Could you let me hit you just once?”

“Hmm. If you ask nicely, maybe.”

“And what about revenge afterward?”

“Oh, come on. What do you take me for? Of course there’ll be revenge. I’ll beat you within an inch of your life.”

“……I had you pegged perfectly.”

Gung Gibang shook his head and went on.

“Anyway, considering we stayed at the very rear until the end, we got off cheap. Though that was only possible thanks to some timely help.”

At Gung Gibang’s subtle glance, the Slaughter Saint—who’d been chewing on jerky without a word—spoke up.

“You were just lucky. We happened to be nearby.”

“I was truly shocked at first. I never imagined you’d be in Qinghai with Young Hero Cheongpung…”

“The more people who know about you, the harder it is to accomplish your goal. And I’m no Great Hero.”

In other words, he’d kept his existence hidden even from his own allies.

The Slaughter Saint answered calmly. I suddenly asked him:

“Then had you been here the whole time since we left for the Nanman Beast Palace?”

“I wouldn’t say the whole time. We only arrived in Qinghai about a month ago.”

I sifted through the time and memories that had passed.

The last time I’d seen the Slaughter Saint was just after the Two Dragons Pavilion was founded, with Cheongpung and me at its center, around the time we left for Nanman.

So even setting aside that month in Qinghai, he’d spent the past several months carrying out some kind of mission with Cheongpung…

*Why hadn’t I heard a single thing about it?*

It was strange.

Even after we parted, I’d been involved in one major incident after another, starting with the Nanman Beast Palace. Every time, the whole world’s attention had turned our way.

Rumors traveled tens of thousands of miles, even without legs.

And yet over the past several months, I hadn’t heard anything about the Slaughter Saint and Cheongpung’s movements.

The Slaughter Saint in front of me clearly didn’t want to talk about it, either.

Because the next moment, before I could say anything, he spat out the jerky he’d been chewing.

“Tough. I’ll be resting nearby for a bit. Don’t look for me.”

He hadn’t said anything directly, but his actions made his meaning clearer than words.

“Always keeping secrets. No wonder people say he’s got a foul temper.”

Jeok Cheongang clicked his tongue softly as he watched the Slaughter Saint walk away, then frowned at my expression.

“What’s with that rotten look?”

“……What did I do?”

“Explain yourself.”

“W-well, nothing. You probably know better than I do.”

“What’s that supposed to mean?”

Cheongpung, sitting near the campfire with a drowsy expression, spoke up on my behalf.

“Obviously, it means Grandpa Jeok’s temper is just as foul, doesn’t it, Benefactor?”

“……”

“Huh? Am I wrong?”

Of course he was right.

But some truths were better left unspoken. Especially when saying them out loud could get you beaten to death.

*Cheongpung, you little shit…*

I stared at him with a dead-eyed look. He’d been gone a while, but apparently he’d learned a new assassination technique from the Slaughter Saint. I did my best to ignore Jeok Cheongang’s scorching gaze beside me and changed the subject.

“So, Young Master Cheongpung, where have you been and what have you been doing for the past few months?”

“Hmm. Little Grandpa told me not to say.”

“You can tell me.”

“He knew you’d say that, so he told me not to say anything, even to you, Benefactor.”

“I’m telling you, it’s fine. If you’re worried, just whisper it to me with Sound Transmission…”

“Wow, that’s amazing. He even told me to keep quiet if you tried to convince me it would be fine to tell you by Sound Transmission.”

“……”

“He said he’d kill me if I said anything. I think I’ve heard ‘Silencing the Witnesses’ about five thousand times by now.”

“……Then I just won’t ask.”

Of course, the Slaughter Saint wouldn’t try to silence the witnesses just because Cheongpung told me everything that had happened so far.

But at this point, it was polite not to ask any further.

Well.

To be honest, I was also a little scared he really might try to silence the witnesses.

“What about what happened in Qinghai? Is that a secret, too?”

“No. He didn’t say anything about that, so I think it’s fine.”

Cheongpung answered innocently and gave us a rough account of what had happened over the past month.

First, why they’d infiltrated Qinghai without telling anyone, and what they’d hoped to accomplish.

“To start with, it was to find any spies who might be inside?”

“Yes. He said a traitor at your back is scarier than an enemy right in front of you.”

He was right.

I’d learned that the hard way more than once, so the meaning behind those words hit hard.

“So, did you find any spies?”

Jeok Cheongang asked. Cheongpung answered:

“No. At least, not as far as we could tell.”

If Cheongpung had been on his own, I might’ve checked a hundred times and still had my doubts. But if the Slaughter Saint was included in that *we*, then I could trust it.

He wouldn’t have been called the greatest assassin of all time if he weren’t that thorough.

Still…

“It’s too soon to relax. You never know what might happen in Murim.”

At Jeok Cheongang’s words, seasoned with the wisdom of an old martial artist, Cheongpung nodded.

“That’s right. Little Grandpa thought so, too. So he was going to infiltrate the Kunlun Sect to investigate further.”

There was a big difference between *wanted to* and *did*.

And I already knew why he hadn’t been able to.

“Dark Heaven attacked just then. Right?”

“Yes. It happened in an instant.”

They had an overwhelming advantage in numbers and strength.

Some of the Qinghai martial artists, including the Kunlun Sect, immediately withdrew from their main compound and retreated east. But the Slaughter Saint and Cheongpung did something different.

“We stayed behind. We hid among them and waited for the right moment.”

Anyone else who’d tried the same thing would’ve been discovered and killed long ago.

But the Slaughter Saint was an exception.

And so was the one other person who’d spent the past several months learning at his side.

“I held my breath and hid my presence, just like Little Grandpa taught me. No one noticed. Like this.”

As soon as he finished speaking, Cheongpung stopped breathing with a sharp *hup*. Instead of answering, I let out a hollow laugh.

Not because of how ridiculous he looked, but because his presence had faded to a ghostly blur, even though he was right in front of me.

*Can he really do that? After only a few months?*

The answer had been clear to me for a long time.

He could.

If the person in question was Cheongpung.

The owner of that insane talent, who seemed to be making a case that you didn’t need a System at all, could master such a difficult concealment technique in no time.

*With talent like that, and the Slaughter Saint teaching him, it makes sense they could slip past the enemy’s eyes.*

A star instructor and a heaven-sent genius.

And the result was a successful infiltration by the two of them.

Of course, even they had their limits.

“I did my best, but unfortunately, I couldn’t get as far as Taiqing Hall.”

“Taiqing Hall…?”

“It’s on the highest peak of Kunlun Mountain. It’s where the Kunlun Sect makes all its major decisions. But there was a strange energy surrounding the area.”

As if remembering the sensation, Cheongpung shuddered.

“I felt something… something sticky that I couldn’t see. It gave me chills before I knew it.”

“Sticky, and it gave you chills?”

“Yes. It made me shudder. Little Grandpa must have felt it too, because he decided we should slip in among the monsters that happened to be coming down the mountain and head back. A few days later, we met you, Benefactor.”

Even after he finished, Cheongpung’s expression didn’t improve. I watched him with a deep, steady gaze and quietly turned over the two words that had come to mind the moment I heard his story.

*Magical power.*

And at that very moment—

*Splash!*

A gentle ripple stirred in the wide, blue river beyond the thick veil of fog.
## Chapter artifact 1076

# Chapter 1076

The river there was blue, and as wide as the sea.

Perhaps that was why.

From some distant past no one remembered, an unnamed freshwater lake had grown larger over the long passage of time. And one day, people began calling it Qinghai Lake.

At this very moment, a shadow was crossing the blue waters of Qinghai Lake.

*Shhhhhh.*

A dozen or so oars pushed the water in perfect, graceful unison.

Their movement sent gentle ripples across the surface, scattering the thick mist and revealing the shadow it had concealed.

A sleek, streamlined shape.

Not especially large, but built of sturdy wood and reinforced with steel.

A sail swollen with wind—and, perched cross-legged in perfect calm atop the narrow mast, where no one would even dare set foot, an old man.

“What a tailwind. Couldn’t ask for better.”

At the old man’s voice overhead, the middle-aged man standing tall at the bow, gazing beyond the mist, answered.

“The days ahead will be the same.”

“Even though we’ve already lost our sect’s headquarters?”

“We didn’t lose it. We gave it up to save precious lives.”

The middle-aged man continued in a steadfast voice.

“A person I respect once told me that what matters is not the house, but the people. A house where no one lives becomes an abandoned ruin. But if there are people, they can build a palace even in an empty field.”

“I don’t know who told you that, but he must be an old man who sounds impressive and has nothing to show for it.”

“M-Master. How could you say that? I didn’t mean—”

“Ha ha. I know. I’m teasing.”

The old man, who had just called himself all talk and no substance, smiled at his flustered Disciple and went on.

“So the days ahead will carry us along like a tailwind… I’d wish for nothing more, if only that were possible. But the headwind that came before was so fierce. What are we to do?”

The middle-aged man shook his head at his Master’s mischievous joke, then answered in a strong voice.

“No matter how fierce the wind is, it can’t overturn a mountain instead of a ship.”

“You’re right. But what if that fierce wind carries embers?”

“……!”

“The wind isn’t what we should fear. It’s a single ember, hidden somewhere deep in the mountains where no one knows, that might soon turn everything to ash.”

The middle-aged man considered the meaning of the old man’s words. Then his expression suddenly tightened.

*Master. Do you mean…?*

A single line of Sound Transmission slipped between his trembling lips.

But before he could hear the answer, the old man slowly rose and murmured:

“Even so, there should be a chance to fight fire with fire.”

At that moment—

*Whoosh.*

Beyond the mist as it scattered in all directions, hundreds of campfires lined the banks of Qinghai Lake, reflected in the old man’s gray-white eyes.

Those sparks, carried away by the wind, were sparks of hope that could stand against disaster.



* * *



The moment a sleek ship appeared through the mist, I knew who they were.

Or, more precisely, I knew who the old man was, gazing down at the shore from atop the towering mast.

*Whoosh.*

The hem of his robe flapped, splitting to either side like wings.

The old man soared like a bird, crossed dozens of jang through the air, and descended. Exclamations rose from all around us.

“Th-that’s…”

“Stepping on Empty Air…!”

Stepping on Empty Air was the highest form of lightness skill, one that required several jiazi of internal energy and deep enlightenment.

These people had fought a desperate battle against monsters they’d never seen or heard of until two days ago. But that hadn’t made them any less awed by the highest martial arts.

My thoughts, however, were a little different.

“Now that’s a remarkable display of Stepping on Empty Air. Don’t you think so, too?”

At Jeok Cheongang’s probing question, I clicked my tongue softly.

“Do I look like an idiot to you?”

“What kind of rude thing is that to say?”

“You already know what I mean.”

“……Hm. So you’re not completely blind, after all.”

I couldn’t tell whether he was displeased that I hadn’t played along or pleased by the progress I’d made. Jeok Cheongang murmured and gazed into the air.

“Still, when it comes to lightness skills, he’s pretty good.”

I let out a quiet laugh.

Considering how Jeok Cheongang usually spoke, that was high praise. But even that fell short of the old man’s lightness skill as he slowly descended toward the ground.

*If you call Gliding Across the Void “pretty good,” every martial artist who’s learned a lightness skill should bite their tongue and die.*

There’s always another sky above the sky.

Those with shallow martial arts or no place in Murim considered Stepping on Empty Air the pinnacle. But there was a realm beyond it.

Not stepping on or kicking off the air, but moving through it as naturally as if gliding. That was Gliding Across the Void. Only a handful of Supreme Peak masters, myself included, could recognize the difference. I could see it in the old man’s feet.

*And in the past hundred years, only two people have reached the realm of Gliding Across the Void.*

I’d heard as much from Jeok Cheongang when I was training on Mount Jiuhua.

One of them had eventually come to be called a god. The other had returned to where he belonged.

To a land far to the west, to the vast slopes of a mountain that touched the sky.

*Swish.*

At last, his toes touched the ground without a sound, and his robes settled around him.

At the same time, the kindly-looking old man brought his hands together in greeting to everyone.

“I am Cheongheoja of the Kunlun Sect. My greetings to all my fellow Daoists.”

“……!”

“……!”

An invisible wave of emotion swept through the crowd.

The shock came from the identity of the old man who had appeared so suddenly with such astonishing skill: he was none other than the Sect Leader of the Kunlun Sect.

“W-We greet the Sect Leader!”

Urgent cries and formal bows erupted all around.

But, as always, there were exceptions.

“Fellow Daoist, my ass. You’ve gotten older and now you think you can treat this old man as an equal?”

The curt greeting from Murim’s veteran drill sergeant and the bane of every prestigious sect was only the beginning.

“It’s been a long time, Cheongheo. You’ve got a lot more gray hair now. The last time I saw you, you still looked pretty young.”

Over the shoulder of the bow-wielding lady, who was at least from a respectable family and had bothered to use polite speech, a human butcher appeared—the man who’d become the greatest of all time through his skill at cutting people down.

“Who would’ve thought? We’ve met before. You ended up becoming Sect Leader, then?”

“……”

“……”

The noisy atmosphere from the Kunlun Sect Leader’s arrival fell quiet in an instant.

The Slaughter Saint, the Bow Saint, and the Fire King Jeok Cheongang.

What an insane lineup. Just looking at them was enough to take your breath away.

They might look middle-aged, mature, and boyish, respectively, but with the amount of time they’d spent in Murim, they could perform the miracle of feeding five thousand with five loaves and two fish.

But Cheongheoja’s ordeal wasn’t over.

“Mm. This humble monk’s greeting is overdue. How have you been all this time—”

Perfected Being Hyeoncheon, the Sect Leader of the Kongtong Sect, had hesitated at the arrival of the old hands. He had just managed to get the words out when—

“Hello, Grandpa Cheongheoja. I’m Cheongpung! We both have the surname Cheong, so I hope we get along from now on!”

“I am Soonja. We don’t share a surname, but our names have the same last syllable, so let’s get along well enough.”

“Taishan hungry. Did you catch any meat on your way here?”

A different kind of insane lineup.

Pure, unfiltered madness.

The appearance of the hopeless trio, every bit as disastrous as the Three Saints, made my eyes glaze over. Yet, to my surprise, Cheongheoja chuckled and spoke.

“Some respected Seniors, and some juniors I’m meeting for the first time. It’s a pleasure to meet you all again.”

At that moment, I had a thought.

Maybe the greatest sect under heaven was the Kunlun Sect.

“……Wow. He can actually put up with all that.”

The exclamation slipped from my lips before I could stop it, and Cheongheoja turned his gaze toward me.

“This is the first time we’ve met this close. It’s good to meet you, Fellow Daoist Jin.”

As Cheongheoja had just said, I’d seen him before, if only from a distance.

In fact, you could say my connection to him was a little more than a passing acquaintance.

During the Star-Array Grand Banquet, Hak Woo, the Kunlun Cloud Dragon, had spent some time hanging around with Gung Gibang and the others. He was Cheongheoja’s Disciple.

“I greet the Sect Leader.”

I belatedly brought my hands together in a formal bow. Cheongheoja nodded with a warm smile.

“It’s been a long time. I’ve heard a great deal about you since then. That boy Hak Woo was especially fond of you.”

“Um, by any chance…”

As if he’d seen through the question I couldn’t quite bring myself to finish, Cheongheoja spoke gently.

“He’s doing well. You needn’t worry.”

“That’s a relief.”

I couldn’t say I’d known Hak Woo for long, but the guy I knew was a good one.

As a martial artist, and as a person.

So when Cheongheoja added one more thing, I was glad to hear it.

“You’ll see him soon. Once we’ve left this place, at least.”

“I see.”

I already knew Qinghai Lake wasn’t our home base.

Gung Gibang and the Beggars’ Sect disciples had simply come ahead to meet us. The threat from Dark Heaven hadn’t disappeared completely.

But Cheongheoja’s words did raise one question…

“Even so, the boat seems a little, well… pretty small.”

I looked dubiously at the ship, which had nearly reached the shore.

It looked like it could hold a hundred people at most—nowhere near enough to carry our three thousand allies.

“Does it look that way to you, too?”

“Sorry, but yes.”

“Ha ha.”

Cheongheoja laughed aloud at my honest answer, then spoke again.

“I suppose it might look that way. From what you can see now.”

“Pardon?”

“Ah, they’re finally here.”

Following Cheongheoja’s gaze, I turned. Or rather, we all did.

*Shhhhh.*

Only then did we see dozens of ships emerge through the thick mist.
## Chapter artifact 1077

# Chapter 1077

Around noon, a group of men dressed in black appeared atop a low hill.

*Swish.*

*Pat, pat, pat!*

At a casual wave from the man in front, several dozen black-clad men scattered in every direction.

They were here to investigate what had happened—and clean up afterward.

“So we have company already.”

The man murmured to himself as he looked down at the scene spread out below the hill.

More precisely, he looked at the vast reed beds extending for a little over ten li in every direction, and the countless birds packed into every open patch between them.

“They must have been hungry. It can’t have been an easy journey.”

Qinghai Lake, only a few days’ travel from here, was also a haven for migratory birds.

The trip was arduous. They had to beat their wings without rest across a thousand li. Even so, enormous numbers of them came to Qinghai Lake each year for its clean water and abundant food.

Of course, that was all in the past now.

*Whoooosh.*

A wind carrying a biting chill suddenly swept through the reeds. The migratory birds, busy filling their empty stomachs, shivered.

The cold was far too severe to be explained by high elevation alone.

At noon, when the sun should have been at its highest, the sky was already covered in black clouds. Untimely frost had frozen the reed beds solid.

And this sort of inexplicable phenomenon, as though the seasons had forgotten their place, had been going on for more than a day or two.

The temperature had fallen. A fierce, bitter cold held sway day and night, and the plants, deprived of sufficient sunlight, could no longer show the lushness they once had.

Elsewhere, a severe drought had struck. It was nothing short of a prank by the heavens, or some supernatural mischief.

All the more so when one considered that these changes had taken place in little more than a year.

But Ma Sanbao saw things differently.

*Crunch, crunch.*

As he slowly descended the hill, frost broke beneath his feet. His thoughts grew deeper, like the footprints forming behind him.

*This is no mere supernatural mischief. His power borders on that of a heavenly god.*

Heaven itself. An all-knowing, all-powerful god.

As he thought of his master, the Lord of Heaven, Ma Sanbao felt fear and reverence rise from the depths of his heart.

An absolute being who not only threatened the whole world, but could change the climate and even bring the dead back to life.

Ma Sanbao wondered, for a moment, whether someone like that could truly be called human.

And why had he shared a portion of that unbelievable power with Ma Sanbao, who had abandoned and fled from his own master—a man who had served the Lord of Heaven himself?

*No. I’m different from my Master. I can be of far greater use to him in every way.*

Ma Sanbao repeated the words to himself.

Though the Eastern Heaven Demon Lord, whom he had served as Master all his life, had met a weak end, Ma Sanbao would be different.

He would contribute greatly to the Lord of Heaven’s grand design, and rule over a part of this world as his new servant.

*Caw.*

Snapping out of his thoughts, Ma Sanbao gave a quiet laugh when he noticed countless pairs of eyes glinting at him.

“Looks like I’ve interrupted your meal. Don’t mind me. Go on and finish.”

His kind words made no difference. The countless migratory birds covering the reed beds let out sharp cries at the unexpected intruder, their bloodshot eyes flashing.

The killing intent in them was far too intense to belong to ordinary birds.

“Well, the changes have already begun.”

Clicking his tongue, Ma Sanbao looked at the birds with interest.

Their beaks were smeared with blood, and their feathers and claws had grown thick and sharp, like those of predators.

Below them lay the dishes that had decorated this sumptuous feast, just as horrifying in stench as they were to look at.

“Really, that instinct of yours is the problem.”

It wasn’t hard to work out what had happened.

The earlier changes in the climate had frozen the plants to death, and the beasts and insects had vanished long ago.

Unable to find food amid this unexpected famine, countless migratory birds must have left Qinghai Lake and wandered the surrounding area. Some of them had finally found a meal in this nearby reed bed.

The blood and flesh of the monsters lying there like puppets with their strings cut.

“I needed to replenish my forces anyway. This worked out nicely.”

Ma Sanbao smiled as he watched the birds begin to mutate.

Recently, some lunatic called the Great Sir had started beating down his subordinate birds indiscriminately, making them difficult to keep watch with. A flock this large was an unexpected windfall.

*Cawww!*

Of course, before that, he needed to imprint his will on the birds, now savage from eating cursed flesh and blood.

“All right. From now on, I’m your master.”

*Jingle.*

The moment Ma Sanbao shook the ritual bell in his hand—

*Whoooosh!*

The countless migratory birds that had been hurtling toward him with a rush of wings abruptly changed course and shot high into the sky.

They obeyed the command carried by the bell’s dull, eerie chime.

And the birds weren’t the only ones to respond.

*Shrrk. Rumble.*

Bent knees straightened, rigid backs unbent, and, finally, tightly shut eyes opened halfway.

“More of them survived than I expected.”

As Ma Sanbao murmured, watching the monsters rise to their full height throughout the broad reed beds, the black-clad men who had gone off earlier returned to report.

“We’ve checked everything.”

“What did you find?”

At Ma Sanbao’s question, one of the men respectfully held out something in his hand.

Except for part of its face, which had been pecked away by birds, it looked just as it had in life. Its expression was natural, without the slightest trace of disturbance—frozen in place.

It was someone’s head.

Until a few days ago, he had been Ma Sanbao’s subordinate and their comrade.

“Most of them were in this condition.”

“This…”

Ma Sanbao’s eyes widened as he examined the head.

He was a sorcerer, but also a master whose personal martial skill had reached Supreme Peak.

Even so, the sword mark on the head was so faint that it sent a chill down his spine.

“…A killing sword. And one that’s reached the highest level.”

“What does that mean?”

“There was someone called No Shadow. The Great Nation’s imperial household raised him as its finest assassin, a man who guarded the Son of Heaven from the shadows. Even the East Depot I once served couldn’t determine his true identity.”

But even No Shadow couldn’t leave a sword mark this faint.

Ma Sanbao knew that well. After a relentless investigation and pursuit, he had once obtained the corpse of one of No Shadow’s victims.

Then a face from his memory suddenly came to mind.

An old, lame man who had been killed by Jin Taekyung in the bloodbath that had taken place at the Grand Banquet a few months earlier.

*Gye Yabu.*

The last heir of Salcheonmun, the greatest assassin sect in the world, long believed to have vanished.

Why had he come to mind at this moment?

Ma Sanbao soon found the answer.

“The Slaughter Saint…”

Yes. His existence explained everything.

Why there wasn’t a single human corpse in these vast reed beds, where a fierce battle must have taken place.

And how so many monsters had avoided a second death, even after the sorcerers had been eliminated.

“He finished it quickly. He went straight for our weakness.”

Ma Sanbao spoke under his breath, then flung his subordinate’s head far away.

The power bestowed on him by the Lord of Heaven allowed him to raise the dead, but not without limit.

“We’re leaving. By now, they must have left Qinghai Lake. We’ll hurry back and carry out the next order.”

The damage was done.

They had at least recovered a considerable number of their forces and gained new subordinates. Setting aside his regret, Ma Sanbao turned to leave.

Or rather, he was about to turn away.

“However…”

Until one of the black-clad men hesitantly spoke up.

“One man is missing. Just one.”

“What?”

“We found a severed wrist, but no body anywhere else.”

“Then…”

“It seems he was captured by them.”

“……!”

Ma Sanbao’s face twisted before he could stop himself.

After all his warnings to be careful, the man hadn’t even died—he’d been captured.

But his anger and agitation lasted only a moment.

They had lost some valuable subordinates and one had been captured, but as a whole, those men were no more than minor branches.

Just as no one bothered with a minor branch, Ma Sanbao hadn’t told them much.

What bothered him a little was what his subordinate said next.

“The ritual bells they were carrying are gone, too. Every last one.”

“…What are they, thieves? They even made sure to take everything.”

Frowning, Ma Sanbao thought for a moment, then shook his head.

“No need to worry. Even if they get their hands on the bells, they won’t be able to do anything with them.”

Just as some country bumpkin couldn’t become a Supreme Peak master overnight by getting hold of a divine weapon, the bells required extensive training before they could be put to proper use.

“Besides, even if that man we lost betrays us, the most he can command is a few hundred.”

“That’s impossible. We know him. He’s loyal to the Heavenly Court, yes, but he’s also not the sort of person who would ever betray anyone…”

At the sight of his subordinates defending their captured comrade, Ma Sanbao let out a quiet laugh.

“He will.”

“Pardon?”

“He will betray us. No—Jin Taekyung will make sure he does.”

Ma Sanbao added in a low voice:

“If that son of a bitch I know is involved, he will.”

As the face of that *son of a bitch* flashed before his eyes, he reflexively reached inside his robe.

At the same time, he remembered the characters written on the note Jin Taekyung had handed him a few months earlier, claiming it was an important secret letter, all to deceive him.

Or, more accurately, the mysterious symbols that even Ma Sanbao, a man well versed in scholarship, couldn’t decipher.

—You fucking dumbass lol

Remembering the strange symbols whose meaning he still hadn’t figured out, Ma Sanbao ground his teeth.

*Just wait. I’ll pay you back soon.*

His gaze, fixed on the east, seemed to be directed at someone crossing Qinghai Lake.
## Chapter artifact 1078

# Chapter 1078

Qinghai Lake was like a small sea, just as its name suggested.

Its waters were more than ten jang deep, and it stretched for thousands of li.

If things had gone as they normally would, our allies—who’d even abandoned their horses on the way to Qinghai—would have had to travel on foot for days and nights. But the dozens of ships that arrived after Cheongheoja, the Sect Leader of the Kunlun Sect, could easily carry all three thousand of them.

*Shhhhh!*

A ship’s bow, carved with the shape of a cloud, sliced forcefully through the water.

I was silently watching the river waters of Qinghai Lake, which had a thin layer of ice in places from the bitter cold, when someone’s voice drifted to my ears.

“Isn’t it strange? Winter is still a long way off, yet we’re already seeing this.”

I turned. A sturdy-looking middle-aged Daoist had entered my field of view.

A face and voice I didn’t know yet.

But I’d exchanged a brief greeting with him when I boarded the ship yesterday, and I could easily remember his Daoist name.

“Oh, Perfected One Hakso.”

The smile on the middle-aged Daoist’s face turned awkward.

“It’s Hak Su. Not Hakso.”

“……”

“……”

The air turned awkward in an instant.

After a brief silence, I forced myself to speak.

“Uh, did you happen to change your Daoist name recently?”

“No. Not once since I joined Kunlun.”

“Then how long ago did you join?”

“Certainly not yesterday. It’s been over forty years.”

“I see.”

“Yes.”

So much for easily remembering.

With nothing left to say, I looked up at the sky and muttered, “Uh, well. Nice weather.”

*Rumble, crash!*

Thunder and lightning suddenly tore across the sky, as if something had gone to hell up there. Hakso—no, Hak Su—glanced up and replied in a dubious voice.

“You must like stormy weather.”

“……Of course. I don’t just like it—I’m absolutely crazy about it.”

I’m going to lose my mind.

It was already too late to take it back.

I was staring up at the darkening sky with a distant look, realizing how badly I’d screwed up, when Hak Su let out a quiet laugh.

“I understand. It happens now and then. It’s not as though it happens so often that it stands out.”

At that generous response, befitting a Daoist of the Kunlun Sect, I swallowed back tears and bowed my head.

“……I’m sorry.”

“There’s no need to apologize. We’ve known each other for only half a day. It’s an easy mistake to make. And besides, Fellow Daoist Jin, you have a great responsibility to attend to.”

Hak Su laughed heartily, but that didn’t change the fact that I’d committed a serious discourtesy.

Especially since the man standing before me might one day succeed Cheongheoja as the Sect Leader of the Kunlun Sect. He was its Senior Disciple, after all.

“I’ve often heard about you, so I know what sort of person you are. Just as the third one said, you’re a very amusing man.”

“By the third one, you mean…”

“You’ve guessed correctly. Hak Woo, the Kunlun Cloud Dragon—that child is my youngest Junior Brother. Though by age, he’s closer to being my Disciple than my Junior Brother.”

Hak Su looked well past forty and close to fifty, so he was old enough that taking Hak Woo, who wasn’t yet thirty, as a Disciple wouldn’t have been strange.

In reality, though, they were fellow Disciples who shared the same Master, Cheongheoja.

“Regardless, I’ve wanted to meet you for a long time. It’s unfortunate that we’ve met under these circumstances…but you came all this way to save our sect. I can’t think of anything that would make me happier.”

At Hak Su’s sudden praise, I scratched my head, feeling awkward for no reason.

I’d heard words of gratitude like this more than once, but I had no desire to play the hero, as if I were someone important.

*Besides, the real battle hasn’t even begun.*

Of course, the strength of the allies about to gather in one place was greater than anything I’d ever seen.

Two of the Three Saints had joined us, and the Fire King Jeok Cheongang—a master who could hold his own against them—was here as well.

If several other Supreme Peak masters, myself included, and our handpicked three thousand elites joined the main force, we might even have the upper hand against Dark Heaven’s massive army invading Qinghai.

But…

*No one can know how things will unfold from here.*

I couldn’t get an exact figure, but from what I could tell, Dark Heaven’s forces now numbered a hundred thousand.

And every last one of them was a monster, no different from the undead, with physical abilities far beyond an ordinary human’s.

That alone was a serious variable. But the real source of the fear weighing on my mind lately was something else.

*The Lord of Heaven.*

An absolute being lurking beyond an abyss of unfathomable depth, swallowing the world—the heavens and the earth.

I couldn’t even imagine what would happen if that bastard appeared before us soon.

*There’s a good chance the Lord of Heaven will take part in this battle. Even Dark Heaven can’t afford to back down from it.*

Four Demon Lords and a Demon Empress, who’d been like his own limbs, had already fallen to my hand, and we’d inflicted heavy losses on his forces along the way.

If he lost an army of a hundred thousand in Qinghai, the Lord of Heaven would suffer an enormous blow.

And yet, one thing still bothered me.

*Then why make such an absurd choice in Gansu?*

I quietly bit my lip and recalled the Grand Mage’s words.

*Get stronger. Even stronger than you are now.*

I remembered how she’d let me live instead of killing me, when I’d been on the verge of death.

No.

I remembered the intent of whoever had given the Grand Mage that order.

*The Lord of Heaven doesn’t want me—Jin Taekyung, the Blazing Flame Divine Dragon—to die.*

The truth I’d realized on that snowfield, covered in blood and corpses, jabbed at my mind like a sharp awl.

Leaving behind questions I couldn’t answer and suspicions I couldn’t believe.

*Maybe. Maybe the Lord of Heaven’s real purpose is…*

A headache came on without warning. I barely managed to swallow the groan that was about to escape my lips.

“……Fellow Daoist. Fellow Daoist Jin, are you all right?”

A voice broke through my thoughts.

At some point, Hak Su had begun looking at me with concern.

“Are you feeling unwell? You look…”

As his voice trailed off, I reflexively looked down at the water.

A stiff face reflected on the clear surface, then scattered in the wake of the speeding ship.

Just like my thoughts.

“I’m fine. Just a little seasick.”

A feeble excuse, especially coming from a Supreme Peak master.

Hak Su watched me for a moment before carefully parting his lips.

“I can’t claim to understand everything you’re feeling, but if there’s something weighing on your heart, you can come to me anytime.”

He let out his characteristic hearty laugh, then added:

“Of course, I wasn’t being entirely serious, so don’t worry about it. But I can at least tell you some good news that might lighten your heart a little.”

“What good news?”

“By now, word of what’s happening in Qinghai must have reached the Central Plains. Before long, the Sword Saint—no, the Alliance Leader—will lead the righteous warriors of the world here to join us.”

For a moment, I’d thought, *Could it be?* But when I heard what Hak Su meant by good news, my strength drained away.

*Could that really happen?*

*First secure yourself, then strike your enemy.*

It was an old saying from Go, meaning that you should first make sure you survive, then attack your opponent.

And in that sense, the world was like a bomb that hadn’t been defused.

Besides…

*As long as they have the Moving Formation, it’s almost impossible for us to commit all our forces to Qinghai.*

But I forced myself to swallow the words on the tip of my tongue.

I couldn’t crush the hope held by the honest, kind-looking Daoist before me.

At least not while I was still confused myself.

“Hmm.”

“Is something wrong?”

Hak Su asked, looking puzzled at my ambiguous response. I swallowed a bitter smile and shook my head.

He’d learn the cold truth soon enough.

Even if not right now.

“No. That’s even better news than I expected. It just caught me off guard. Anyway, how much farther to our destination?”

“About half a day, I think.”

“Half a day. So, two or three shichen at most.”

We’d saved a considerable amount of time by crossing Qinghai Lake directly by ship.

I nodded, thinking about what lay ahead, then muttered as I remembered something I’d almost forgotten.

“Oh, right.”

“Is there something you’re curious about?”

“No. I was just thinking it’s about time to haul him out.”

“Pardon?”

Ignoring Hak Su’s bewildered question, I shouted toward the house elf somewhere nearby.

“Head down!”

A moment later, I heard an indignant shout from a rude house elf.

“Damn it, why now?!”

“I just felt like calling you. Wanted to check your location.”

Hyuk Mujin came running over in a hurry. At my unbothered answer, he scowled like he’d swallowed shit.

“Am I some kind of stray dog?”

“Absolutely not. What sin did a good dog commit in a past life to deserve being compared to you?”

“……One day I’m going to quit this filthy job, I swear.”

“Good. Please do.”

I chuckled at his grumbling and started walking.

“Anyway, how’s the job I gave you going?”

“I was just in the middle of working on it. He’s a lot tighter-lipped than I expected.”

“And?”

“I attached a chain and a water jug to his ankle to make him even heavier. He looked like he was having the time of his life.”

“Good work. You’ve got a knack for it.”

“What can I say? I learned it all from you, Captain.”

As I walked along, chatting with Hyuk Mujin, Hak Su followed behind us, caught up in the situation. He blinked.

“Excuse me, but what exactly are you talking about?”

I shrugged at the sight of him staring blankly at the empty deck.

“You’ll see.”

“But what exactly…”

“Mujin.”

“Yes, sir.”

*Rrrrattle.*

Hyuk Mujin stepped forward briskly and grabbed a chain sticking out over the side of the deck. As he pulled, a man in black, his whole body pale blue, emerged from the water.

“Gah! I-I’ll talk! I’ll talk!”

“On your life?”

“Of course—cough—of course!”

He’d spent a full day and night as one with the blue waters of Qinghai Lake. It was hardly surprising that he might be ready to cooperate now.

But I stared at the gasping man in black with a grave expression.

“If even a little of what you say is a lie, your parents will live long, sick lives.”

“……”

“Devoted son, aren’t you? Right, Mujin?”

“Yes, sir!”

“N-No! Anything but that…!”

*Rrrrattle. Splash!*

Hyuk Mujin answered with gusto and let the chain go. The blue water swallowed the man’s desperate scream.

The ancient tradition of dipping someone in the Yangtze lived on at Qinghai Lake.
## Chapter artifact 1079

# Chapter 1079

If someone asked me whether a person could survive being dunked in a river hundreds of times over the course of a full day and night—and half a day on top of that—I’d answer without hesitation:

Of course they could.

And they might even gain a level of honesty that put their previous self to shame.

Naturally, there might be a few minor complications along the way.

“Ugh… ugh…”

“Captain, this guy’s eyes are completely glazed over.”

“If they’ve gone slack, we’ll just have to tighten them up again.”

“How?”

“Give him a good slap across the face. Nice and hard.”

“Ah.”

Hyuk Mujin nodded as if he’d just reached a great insight, then promptly raised his palm.

*Smack!*

“He’s not waking up.”

“Are you stupid?”

“Why?”

“You have to hit him harder. Until he wakes up.”

“Oh. Are you a genius?”

“Not a genius. Just exceptionally gifted.”

“Figures.”

Mujin gasped in admiration and raised both hands this time.

*Smack! Smack! Smack!*

“Uh, his eyes rolled back.”

“He’s exaggerating.”

“No, I’m serious. His body’s completely ice-cold, too.”

“Huh. So it is.”

“I told you.”

“This bastard’s cold because his heart is cold.”

“Now is not the time for nonsense. What if he dies?”

“He won’t. I’m here, and my heart’s warm.”

“What?”

The moment Mujin looked at me as if to say, *What kind of bullshit is this idiot talking about now?* I reached out without hesitation.

*Boom!*

When my palm, warmed by Scorching Yang Qi, struck his chest, the black-robed man’s body—which had been turning pale and rigid—shuddered. Then warmth returned to him, more than before.

“…Wow. He actually survived.”

“Told you. I have a warm heart.”

“Isn’t it your internal energy that’s warm, not your heart?”

“Want to warm up like him? You look a little cold.”

“I must politely decline…”

*Crack!*

“Gah!”

“What?”

“He bit his tongue! There’s so much blood!”

“Good grief. What a mess.”

“I told you not to release his Mute Acupoint! Even with his internal energy sealed, he could die in a situation like this!”

“If I’d sealed his Mute Acupoint, he might’ve drowned without getting a word out. Anyway, quit making a fuss and go fetch him.”

“Fetch who?”

“Who do you think?”

“Oh.”

A moment later, a professional two-jobber who had reached the peak of his craft in two completely opposite professions—assassin and physician—revived the emergency patient in the blink of an eye.

“I stitched him up perfectly, so he’ll have no trouble speaking once he recovers.”

“Thank you.”

“But this man—is he the one I’m thinking of?”

“Yes. The one you brought in last time.”

“He was so bloated I nearly didn’t recognize him. His wrist wound hasn’t healed yet, either, so don’t overdo it. If the wound gets infected and turns necrotic, you’ll be in trouble.”

“Oh, it’s not my body, so that’s fine.”

“True enough. But if you keep handling him so roughly, he’s liable to lose his life. In a situation like this, you’re better off stabbing him deeply three vertebrae below the cervical vertebrae, then slowly…”

“Oh, that’s a handy tip. But wouldn’t that kill him?”

“He wouldn’t die. He’d just wish he had.”

The expert, second to none in the world when it came to taking apart and treating the human body, passed on his useful tip and left. The black-robed man, who had watched the whole thing unfold right before his eyes, began to thrash.

“Mmph! Mmmph…”

“Hey, why are you acting up again? Just stay still.”

“Mmmph!”

“Can’t be helped. Mujin.”

“Yes, sir.”

“Hold him down for a bit. I’m trying to practice, but it’s hard when he keeps shaking. I used a Pressure-Point Strike, and he’s still struggling this much. How badly is he thrashing around?”

“This insolent bastard. The Captain’s trying to practice here. Heave-ho. Is this good?”

“Yeah. Perfect. All right, I’m going to stab him.”

“Wait. Are you sure that’s the right spot?”

“Isn’t it? I thought I heard it started two vertebrae below the cervical vertebrae.”

“Huh? Wasn’t it two vertebrae above?”

“No way. That’s a lethal acupoint.”

“I’m confused. Shouldn’t you go ask him again, Captain?”

“Why should I go? You go.”

“I could die if I go. And he hates having to repeat himself.”

“You think it’d be any different if I went?”

“Fair point. How about stabbing both spots?”

“That’s not a bad idea. Shall we?”

“Yes, sir. Go ahead.”

“Mmmph! Mmmmmmph!”

*Rrrrrumble!*

The deck shook as if an earthquake had hit—though that might be a slight exaggeration.

The black-robed man thrashed with all his might despite the Pressure-Point Strike. I let out a quiet laugh to myself, then released his Mute Acupoint.

“Gah! Cough, cough!”

“What is it? Got any last words?”

“Th-three vertebrae.”

“Hm?”

“Cervical vertebrae! Three down from the cervical vertebrae! Stop it, you madmen!”

There are only two reasons someone might call you a madman when you could take their life with the slightest movement of your hand.

First, they’ve resigned themselves to death.

Second, they’re no longer capable of rational thought, to the point where they don’t care about something like that.

He was clearly the latter.

*It’s over.*

The terror in his eyes and voice told me he had been reborn as a far more honest man. I stood up.

“Huh? You’re not going to stab him?”

“Why would I stab him? Get something to cover him with, then sit right beside him and have a chat.”

“What about you, Captain?”

“I’m about to get busy with something else. Isn’t that right?”

At my sudden question, Hak Su—who had been watching the whole scene with the face of a man who’d seen a ghost—swallowed hard.

“I-I’m not sure what you mean.”

“Oh, right. You can’t see it yet. Over there.”

Just as I raised my hand and pointed beyond the bow—

*Whoosh.*

The thick fog lifted, revealing the lush green land hidden behind it.

A group of people had gathered at the pier to welcome us. Over their shoulders, far in the distance, the gray walls of a city were faintly visible.

Xining, the capital of Qinghai Province and the last stronghold against Dark Heaven.

*That’s Xining.*

At that moment—

*Ding.*

A clear chime rang out above the rushing river.

* * *

The welcoming crowd was enormous.

No, it wouldn’t have been the least bit strange to call it massive.

“Waaaaaah!”

“The reinforcements are here! The Murim Alliance reinforcements have arrived!”

Was this what the triumphal processions of the Roman Empire looked like in the textbooks?

The cheers swelled as we drew closer to the walls, then shook the whole city the moment we entered. Everywhere I looked, the streets were packed with dark masses of people.

They filled the broad avenues and narrow alleys, as well as the rooftops of countless buildings—including rows of pavilions—and stretched both arms toward us as they cheered.

The crowd was so enormous that even Cheongpung, who usually loved attention, swallowed nervously and whispered:

“If we stay here much longer, I think my ears might burst, Benefactor.”

“Yeah?”

“Yes. I’m not joking. I’ve never heard anything this loud.”

“Mirror therapy works, all right.”

“Hm? What’s mirror therapy?”

“It’s… never mind. Even if I explained it, Young Hero Cheong wouldn’t change.”

Normally, Cheongpung would have been armed with pure, unbridled curiosity and pressed me to explain what mirror therapy meant. This time, though, he simply continued in a quiet voice.

“There are so many people. Seriously, so many. I stayed in Xining for a while once, but it wasn’t anything like this.”

Cheongpung had spent about a month in Qinghai Province before I had, so the change must have seemed even more striking to him.

Of course, I already had a good idea where this enormous crowd had come from.

*Everyone scattered across Qinghai Province must have gathered in Xining.*

It was only natural.

The same thing had happened earlier in Shanxi, and then in Gansu.

The Great Nation’s imperial court had already declared Dark Heaven rebels and foreign invaders. That was essential to alert the common people, many of whom still thought there was nothing to worry about.

Unlike the Great Faction War, which had barely affected the common folk, Dark Heaven’s actions had long since gone far beyond the bounds of the Murim.

If the Heavenly Demon of the past had set his sights on the Murim, the Lord of Heaven now wanted the whole world.

No—

*Maybe even more than that.*

I forced down the unease that grew sharper with every passing moment and curled my lips into a smile.

So that the countless people surrounding us, covering every direction, might feel a little more at ease when they saw me smile.

“It’s Blazing Flame Divine Dragon Jin Taekyung!”

“Marquis of Shangshan has arrived!”

“Waaaaah! Long live the Great Nation! Long live His Majesty the Emperor!”

There might have been a great many people, but most of them knew little about the affairs of the Murim.

In their eyes, I wasn’t just a young martial artist. I was a divine general, carrying out the Son of Heaven’s solemn imperial command to punish foreign invaders and save them.

At the cheers growing louder by the moment, Cheongpung’s eyes widened.

“Wow. Everyone seems to like you, Benefactor.”

I swallowed a bitter smile and replied in a low voice.

“It looks that way. At least for now.”

“They’ll keep liking you in the future, too. You’re that good a person!”

“A good person…”

I let my voice trail off and looked at the welcoming crowd filling the city.

At a glance, there were hundreds of thousands.

Or perhaps it wouldn’t have been an exaggeration to say there were even more.

At this very moment, all those people were smiling brightly and cheering for me. But I had no way of knowing how long those smiles would stay on their faces.

Or, if the worst really did come to pass, how many of them would survive.

“Young Master Cheongpung.”

“Yes?”

“Yes?”

“Let’s do this. As much as we can.”

I quietly added, still looking at the crowd:

“With our lives on the line.”

Yeah.

Just as we always had.

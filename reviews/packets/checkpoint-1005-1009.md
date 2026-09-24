# Checkpoint Review — 1005–1009

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

# Chapters 1005–1009

## Plot

After four days of travel, the Fire Dragon Pavilion rests over a feast. Taishan sits motionless instead of eating, and Namho recognizes a scent but says nothing. Meanwhile, Sima Gong explains that Gansu has assembled thirty thousand martial artists along three defensive lines and sent scouts beyond the desert. He expects Dark Heaven to target Gansu, though he also urges Jeok Cheongang to go to Qinghai.

The scouts return early and signal suspicious intruders at the wall. Jin Taekyung mistakenly orders the guards to fire on about fifty riders led by Ma Junggeol. Jeok Cheongang persuades the leaders to admit them. The riders identify themselves as Baekma Bang, reformed Ningxia mounted-bandit leaders who came to help and bring intelligence. They report seeing at least a thousand Dark Heaven tents in the western desert, closer to Gansu than Qinghai. Taekyung concludes that the forces must fight there.

## Continuity

- Gansu Murim has assembled 30,000 martial artists in three defensive lines across Dunhuang, the Great Snow Mountain, and the Qilian Mountains. The Kongtong Sect is already deployed.
- Sima Gong sent thirty scouts beyond the desert after ominous signs. They returned early and signaled the approach of suspicious riders.
- Dark Heaven’s camp in the western desert contains at least a thousand tents. Ma Junggeol’s group followed the force for a day and a half from a distance of one hundred li; its total strength and objective remain unknown.
- Baekma Bang, Ningxia’s largest group, is opening a trade route west toward Xinjiang. Its members are reformed mounted-bandit leaders guided by an unknown master more than ten years ago.
- Ma Junggeol leads Baekma Bang and arrived with six associates, collectively known as the Seven Masters of Baekma Bang. They offer help and say they have important information about Dark Heaven.
- Taishan remains unusually motionless and uneating at the feast. Namho recognized a scent connected to a recent memory; what it means remains unresolved.
- Sima Gong expects Dark Heaven to target Gansu but has urged Jeok Cheongang to go to Qinghai. The reported camp lies on a route closer to Gansu than Qinghai.

## Translation Decisions

- Render **백마방** as “Baekma Bang” and **백마칠종** as “the Seven Masters of Baekma Bang.”
- Render **곡차** in the drinking scene as “grain liquor,” not “grain tea.”
- Keep “dark-path figures” distinct from “unorthodox faction”; render **관무불가침** as the principle of government–Murim noninterference.

## Durable state

{
  "active_continuity": [
    "Baekma Bang is the largest group in Ningxia and is opening a trade route west toward Xinjiang.",
    "Baekma Bang scouts saw at least a thousand Dark Heaven tents in the western desert, on a route closer to Gansu than Qinghai.",
    "Ma Junggeol's group followed the force for a day and a half at a distance of one hundred li before returning with its report.",
    "Ma Junggeol says Baekma Bang has important information about Dark Heaven and came to offer help."
  ],
  "continuity_sources": [
    1008,
    1009
  ],
  "open_questions": [
    "Who was the unknown master who helped reform the Ningxia bandit leaders?",
    "What is Dark Heaven's full strength and objective in the western desert?"
  ],
  "safe_through": 1009,
  "temporary_decisions": [
    "Render 곡차 in this drinking scene as grain liquor."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 1005

# Chapter 1005

Four days.

You couldn’t exactly call that a long time.

But if you’d spent all four days riding hard, barely stopping to rest and catching only snatches of sleep in the saddle, that was another matter.

*Rest while you can. Who knows when we’ll have another chance?*

Jin Taekyung had left them with those words, then gone off to a meeting with the leadership. The Fire Dragon Pavilion members he’d left behind had faithfully followed their Pavilion Master’s orders.

And so, now, they’d unpacked their few belongings, finished bathing in warm water, and settled in before a sumptuous feast that had somehow already been laid out.

Naturally, Jeok Cheongang and Sama Pyo were the exceptions.

The Fire King was a towering figure of his generation. He needed no explanation. And the title of Young Sect Leader of the Black Dragon Demon Gate placed Sama Pyo well within the ranks of the leadership.

“Whew. I finally feel alive again.”

Ju Hwaran’s words might as well have spoken for every member of the Fire Dragon Pavilion.

Physical exhaustion was bad enough, but mental fatigue squeezed at the body and mind in a way that put it to shame.

What could they do?

For a martial artist, crossing the line between life and death was a lifelong fate. The grief and pain brought on by war were the lot of those living through troubled times.

It had always been that way, and it would stay that way.

At least everyone in the Fire Dragon Pavilion understood their circumstances clearly—and had accepted them.

“Our Pavilion Master was right. We have to rest as much as we can while we have the time if we’re to prepare for what comes next. With that in mind, let’s eat.”

At Song Ilseom’s invitation, Hyuk Mujin looked up, his cheeks already bulging with food.

“Wha’?”

“……”

“Wha’ did you jus’ say?”

“……”

“Sounded like you said somethin’.”

Song Ilseom stared at him in silence, then answered.

“Nothing. Don’t worry about it. Go ahead and eat. The more pain you’re in, the hungrier you get.”

“Ah, okay.”

Perhaps the bump sticking out of the crown of his head was bothering him. With the conversation interrupted, Hyuk Mujin took the opportunity to rub it, then buried his face in his plate again.

A moment later, he looked up and stared intently at Song Ilseom.

“Wait. Why’re you talkin’ down to me? I don’t like that.”

“I’ve been doing it this whole time.”

“That’s why I don’t like it. I’ve told you a bunch of times not to.”

“It’s simple. I’m older than you.”

Gulp.

Hyuk Mujin swallowed what was in his mouth and frowned.

“What a ridiculous guy. You’re only a year or two older than me.”

“Does a year or two not count as an age difference?”

“Well… I guess it does.”

“And you know perfectly well that I have more experience as a martial artist.”

“That too… I guess.”

“I’m your senior, and I’m older. So what’s the problem?”

The longer the conversation went on, the worse things seemed to get for Hyuk Mujin.

His eyes rolled around as he searched for a counterargument. Then an idea came to him.

“You know how old our Captain is, right?”

“More or less.”

“He’s way younger than me.”

“So?”

“Hey, what do you mean, ‘So?’ You use at least a polite form of speech with the Captain. Why do you get to talk down to me—”

“So?”

“……Huh?”

“So. What are you going to do about it?”

“……”

There was nothing he could say to that.

As Hyuk Mujin blinked at Song Ilseom’s absurdly confident attitude, he suddenly felt anger rising from deep in his chest.

Now that he thought about it, how unfair was this?

He could put up with Jin Taekyung giving him a hard time whenever he got the chance. That much he could gladly accept as the loyal right hand and self-proclaimed heart of his Captain.

But now he was being treated this way even by Song Ilseom—a lowly wandering martial artist who’d joined them along the way. Sure, for a mere wanderer, he was famous as hell in those circles, and, as it turned out, he came from an impressive martial family. But still!

*I mean, come on! By rank, I’m the Vice Pavilion Master of the Fire Dragon Pavilion! And the Jin Family of Taiyuan is one of the Five Great Families now!*

A fire lit in Hyuk Mujin’s eyes as he glared at Song Ilseom. The roasted chicken leg in his hand, which he’d been clutching for a while, trembled as though it were a sword resonating with its wielder.

“Planning to throw that thing you’re holding?”

“Why? Think I can’t?”

At Hyuk Mujin’s chilly reply, Song Ilseom nodded without hesitation.

“Of course you can’t.”

“That’s right. You know me well.”

“But you’ll have to deal with what happens afterward… Wait, what did you say?”

“If you throw away food, heaven will punish you. Besides, my parents always told me to get along with the people around me.”

“……”

“What? Got something to say? Then say it quickly. I’m hungry, and I don’t want the precious food to get cold.”

Was that confidence? Cowardice?

Or both?

*What is with this guy?*

How could anyone be so shameless about being such a coward?

Song Ilseom watched Hyuk Mujin with a thoroughly unimpressed look, then spoke.

“……Never mind. You had good parents.”

“They’re kind, simple people. Thanks for the compliment.”

Hyuk Mujin replied as if he’d been waiting for those words, then set to work sweeping the food in front of him into his mouth with renewed vigor. Song Ilseom sighed inwardly.

*Every last one of them is out of their minds.*

They’d been told to rest and take it easy, but who would look at that and think they were about to go into battle?

They looked more like a pack of beggars come to bankrupt an inn.

*Or do they not feel fear at all?*

Song Ilseom had spent years among wandering martial artists—a crowd of crazies so thick you could hardly turn around without running into one. But the people he’d been with for the past year or so were strange from top to bottom.

For example…

*True madness.*

The degree of it was on another level from anything he’d seen before.

And Hyuk Mujin, who was already plenty crazy himself, was merely average by Fire Dragon Pavilion standards.

First, there was Jeok Cheongang, the Fire King.

“……”

No words were needed. The proof was how Song Ilseom’s breath caught just thinking about him.

Watching Jeok Cheongang up close had driven one point home once again: the law of the jungle still ruled the world.

*If it didn’t, Jeok Cheongang would have been dead several times over by now.*

Why did he think that?

Simple.

Jeok Cheongang beat the living daylights out of anyone he didn’t like. Anyone at all. He was fair about it, at least.

Their sect, their principles, their age, their sex—it made no difference.

If they belonged to the orthodox faction, he’d dig into their hearts with a tongue sharper than a famous sword. If they were from the unorthodox faction or the dark-path underworld, he’d immediately size them up for a punch. As for fiends, he’d once said:

> *“I may as well tell you now: for many years, my fondest wish has been to reform every fiend beneath heaven and make them good.”*

Jin Taekyung had asked on everyone’s behalf if he’d gone senile. Jeok Cheongang had beaten his own Disciple senseless, then added, as brazen as ever:

> *“Of course, the only good fiend is a dead fiend.”*

That was the kind of person Jeok Cheongang was.

What else could explain his one and only Disciple saying this about his own Master?

> *“I thought about it seriously, and helping the orthodox faction during the Great Faction War was the best move that old man ever made. Now he gets to be called a king and wreak havoc wherever he wants, all perfectly legally. Am I right, everyone?”*

Jin Taekyung probably didn’t know.

Everyone had agreed with him, but the moment he turned away, they’d exchanged looks that all meant roughly the same thing.

> *“Look who’s talking.”*
>
> *“How does he have the nerve to say that?”*
>
> *“Does our Captain even know what the word ‘conscience’ means?”*
>
> *“Sorry, Young Master Jin. This is a bit much, even for you……”*
>
> *“Taishan hungry.”*

No one dared say it outright, but everyone knew the only person crazier than Jeok Cheongang was Jin Taekyung.

*That guy’s the real lunatic, in more ways than one.*

His martial arts were insane, and so was his temper.

Sometimes, for reasons known only to him, he’d act like a perfectly normal person. But when something rubbed him the wrong way, he could show a side that even surpassed his Master, Jeok Cheongang.

*In that sense, he’s even worse.*

If Song Ilseom had to fight either Jeok Cheongang or Jin Taekyung, he’d choose the former without hesitation.

Because he thought Jeok Cheongang’s martial arts were no match for his Disciple’s anymore?

Wrong.

Even if Jeok Cheongang cursed him with every filthy word in the world until he feared qi deviation, even if his Flame-Extinguishing Divine Fist crushed Song Ilseom’s Eight Extraordinary Meridians, Jeok Cheongang would still be preferable.

Because he was the Fire King.

A giant known throughout the world, an old monster who had lived through ages beyond counting.

But Jin Taekyung?

*……I don’t even want to think about it.*

Just remembering him made Song Ilseom’s stomach churn.

His martial prowess, now so far beyond Song Ilseom’s reach, was one thing. But his reputation for surpassing his Master in the art of verbal abuse was a nightmare all on its own.

The one small comfort was that his terrifying tongue always seemed to work at full strength only against enemies.

And even aside from that, Song Ilseom was one of the people who got the least grief from Jin Taekyung, along with Sama Pyo and Ju Hwaran.

Even when he did something worth getting chewed out for, Jin Taekyung would just toss out a short line and turn away.

> *“So boring.”*

Song Ilseom didn’t know exactly what the expression meant, but he could guess it wasn’t a compliment.

*He said I was “so boring.” He called Sama Pyo “ten times more boring.” But he didn’t say anything to Young Lady Ju.*

What else could that mean? It was obvious.

Song Ilseom had once spent a long time seriously puzzling over the exact meaning of the expression, but at some point he’d stopped caring.

Had he gotten used to it?

Maybe. Or maybe…

“Hmm.”

With a low hum, Song Ilseom came back to himself from his deep thoughts.

Only then did he notice what was happening around him—and realize that something was terribly wrong.

“What on earth… is going on?”

It wasn’t a question directed at anyone in particular. It was closer to a disbelieving gasp.

Song Ilseom stood frozen, eyes wide. Ju Hwaran and Hyuk Mujin, both wearing serious expressions, answered in turn.

“We don’t know either. What happened?”

“Incredibuh! Makes no shensh!”

Ju Hwaran’s answer was full of worry. Hyuk Mujin’s was full of food.

Pth, pth!

Usually, Song Ilseom would have dodged the spray of food with a quick sidestep. This time, he couldn’t.

Splut!

Something unpleasant touched his skin.

Hyuk Mujin froze, worried about what he’d done. But despite his fears, Song Ilseom didn’t move.

He could only stare at one person, stunned as if he’d come face-to-face with a living dragon.

Taishan was sitting before a feast fit for a king, yet his shoulders drooped and he didn’t move at all.

“Am I seeing things?”

Just as those disbelieving words slipped from someone’s lips—

“You’re seeing it right. But I’d like you to keep it down for now.”

The voice was quiet and low.

Namho, who’d been sitting motionless from the start, lost in thought, twitched his nose.

As if he were following the scent of a memory from a day not so long ago.
## Chapter artifact 1006

# Chapter 1006

Rrrrip.

A thick animal hide unfurled across the large table.

Its surface had been tanned by human hands and covered edge to edge with drawings and writing that depicted the terrain in detail.

“As you can see, this map was made by our sect. We’ve spent many years documenting every feature of Gansu in detail, revising each change as it occurred, until it was complete.”

Sima Gong’s voice was calm as he explained the map. But none of the leaders gathered here failed to understand what it meant.

A province might sound small, but each one was practically a nation of its own—a great or small piece of the world. Even the smallest was comparable in area to a country.

And it wasn’t as if they had drones or satellites.

Given the reality of the time, producing a map required enormous wealth and manpower. That much was only natural.

And yet the fact that they could make a map this vast and detailed showed just how much control the Black Dragon Demon Gate, led by Sima Gong, held across Gansu.

It also spoke to the reach of Sima Gong’s intelligence network.

“You must’ve spent a fortune on it. So what, do you want to brag that you’ve got this area locked down?”

At Jeok Cheongang’s blunt way of speaking, which knew nothing of beating around the bush, a faint smile appeared on Sima Gong’s lips.

“How could you think that? The Kongtong Sect is one of the pillars of the Central Plains. How could we dare?”

His words were humble, but no one was unaware of the position Sima Gong and the Black Dragon Demon Gate held in Gansu Province.

And besides…

“This is an important meeting, but that very pillar is missing.”

That was right.

The Kongtong Sect was absent from this gathering.

But even after I’d struck right at the heart of the matter, Sima Gong’s faint smile didn’t waver.

“No need to worry over that. The pillar is preparing elsewhere to hold back the torrential rain that’s about to pour down.”

“So the Kongtong Sect has already been sent to the front lines.”

Sima Gong nodded at the Wind-and-Cloud Sword Lord, who’d cut in without warning.

“Just as the Sect Leader guessed. We’ve established three lines of defense stretching across Dunhuang, the Great Snow Mountain, and the Qilian Mountains in Gansu Province.”

“Three lines? Isn’t that spreading our forces too thin?”

The people in the conference room nodded as if they shared the Wind-and-Cloud Sword Lord’s concern.

If Dark Heaven’s vast army marched into Gansu, a great battle would decide everything in a single clash.

But even in the face of everyone’s reaction, Sima Gong’s expression remained unchanged.

“Though they’re no match for Kunlun, the Great Snow Mountain and the Qilian Mountains are among the ten most treacherous mountain ranges under heaven. And our enemies have a bizarre form of dark arts they call a Moving Formation. We judged that concentrating all our forces in Dunhuang would be too dangerous.”

“I agree with Sect Leader Sima’s opinion. But the question is whether we have enough forces to hold three fronts.”

The greatest obstacle, in the end, was that we were outnumbered.

The enemy army numbered a staggering hundred thousand.

Even if they split their forces and attacked three provinces at once, a simple calculation meant more than thirty thousand of them would come rushing in like a pack of dogs.

*To face that many enemies, we need to gather in one place. And we’ll only have a chance if we make the best possible use of the terrain.*

That was what had happened in the battle in Shanxi Province not long ago. Luck and determination had come together to win us the day.

And this was common sense, even for someone with no knowledge of military strategy.

But would the Black Night King Sima Gong, who’d built the massive Black Dragon Demon Gate from the ground up, really not know something so basic?

*No way.*

I read a quiet confidence in Sima Gong as he calmly met everyone’s gaze.

“That should be more than enough. Gansu’s forces.”

At that, the smile on Sima Gong’s lips deepened.

“About a month ago, I put all of Gansu Murim on alert. Our sect and the Kongtong Sect, along with every martial faction in the area, had been keeping watch for some time. We were able to gather our forces quickly.”

“Which means…”

“Thirty thousand. That’s how many we’ve assembled so far. We’ve mobilized every resource Gansu Murim has.”

“……!”

“……!”

The leaders’ eyes widened. Mine were no different.

*Thirty thousand?*

That was an enormous army.

It was all the more astonishing when I remembered that Shanxi Province had fielded only fifteen thousand to hold Eight Spring Gorge and face the Great Steppe’s forces.

What was more, Sima Gong had specified *Gansu Murim*. That meant all thirty thousand were martial artists.

There was no comparing that to Shanxi Province, where more than half the total force had been government soldiers.

Of course, Shanxi Murim had already suffered severe losses in its conflict with the Mount Heng Sword Sect and the Head Elder’s betrayal. Even taking all of that into account, a force of thirty thousand was still almost unimaginable.

“W-where did you find that many people?”

Just as the Wind-and-Cloud Sword Lord spoke up to ask the question that must have been on everyone’s mind, Jeok Cheongang, who’d been watching with a frown, suddenly spoke.

“Unorthodox types are nothing without numbers. Isn’t that right?”

Sima Gong gave a small smile and nodded.

“I can’t deny it.”

“But still, a force of thirty thousand would be nearly impossible even for the Nine Sects and One Gang of the Central Plains.”

“That’s also true. Would the Great Nation have stood idly by if this many ruffians, liable to turn the swords at their waists against the state at any moment, had gathered?”

The phrase “the government and Murim shall not interfere in one another’s affairs” had been rendered practically meaningless ever since the Son of Heaven declared Dark Heaven a traitor. But there was a reason the principle had come into being in the first place.

It was an unspoken rule that had arisen naturally alongside Murim itself.

A stone that stuck out was bound to get hammered down sooner or later.

The countless martial factions scattered across the vast world had repeatedly checked one another and made agreements to avoid conflict. And so long as the foundations of the nation weren’t threatened, the Great Nation turned a blind eye to their existence.

People even said that when a dynasty fell, Murim remained.

But the Murim of Gansu had now crossed that unspoken line.

They’d gathered thirty thousand martial artists in the frontier, not even the Central Plains. That was an army they couldn’t have raised even if they’d turned every martial faction in Gansu Province upside down and shaken them out.

*Which means…*

There was only one possibility left.

The majority had no affiliation with any particular sect. They were the sort of people who followed only their own needs and interests.

“You even scraped together the dark-path figures. You must’ve been pretty desperate.”

The dark path.

At the mention of those who’d existed in an uneasy coexistence with Murim for ages beyond counting, several people’s expressions darkened. The Wind-and-Cloud Sword Lord’s eyes in particular sank.

“Sect Leader Sima. Is what Great Hero Jeok said true?”

Sima Gong answered calmly.

“It’s true that some of them are dark-path figures. Is that a problem?”

“……Well…”

“I’ll admit it. I’m an unorthodox martial artist, and the Yangtze River Channel League and the Green Forest Alliance are dark-path organizations to the core. Ah, and my son over there is the same.”

At his father’s sudden callout, Sama Pyo’s eyes, which had been silent all this time, wavered.

But the moment Sima Gong spoke again, the people had no choice but to turn their attention back to him.

“And everyone I just mentioned has one thing in common. Do you know what it is?”

They did. Everyone in the room did.

But the people remained silent, their faces heavy.

Everyone but one man.

“They’ve fought for the Murim Alliance—and they’re fighting for it now.”

Jeok Cheongang.

Sima Gong’s reflection appeared in his reddish, fever-bright eyes, befitting the title of Fire King.

“Unorthodox, dark-path figures, or nobodies who crawled in from God knows where—I don’t give a damn. If the weapons in their hands are pointed at Dark Heaven, that’s all that matters.”

Sima Gong nodded, his expression firm.

“As it was in the past, so it will be this time.”

“I’m not doubting you. But the kind of dark-path trash that would drift all the way out to this frontier must be rotten to the core. If something goes wrong…”

“I’ll stake my head on it.”

Then Jeok Cheongang, who’d been staring silently at Sima Gong, suddenly turned his head and swept his gaze across the room.

“What do you all think?”

There were respected elders of Gansu Murim gathered here who’d come out to greet us with Sima Gong, but Jeok Cheongang wasn’t asking them.

He was asking the senior members of the Zhongnan Sect who’d come with us.

As the Wind-and-Cloud Sword Lord, standing at their center, hesitated to answer, his Senior Brothers, the Roaring Fury Swordsman and the Taeeul Merciless Sword, spoke one after the other.

“Someone once said that it doesn’t matter whether a cat is white or black, as long as it catches mice.”

“The Sima Gong I know is a comrade-in-arms and a hero, someone who weathered the war alongside us, before he is an unorthodox martial artist. That a man like him should have to stake his life on this—isn’t that a crying shame?”

As I watched the two old Daoists pour out their words with practiced fluency, as if they’d been waiting for this, Jeok Cheongang’s gaze suddenly shifted to me.

“So, are you done stuffing your face with honey?”

At his question about why I was sitting there with my mouth full, pretending to be mute, I licked my lips and answered.

“Yeah. It was sweet.”

“You’ve been holding that precious honey in your mouth long enough. Now you must have something to say.”

“Is this something I get to decide?”

“Not a chance. Who do you think you are?”

I let out a snort, then slowly looked around.

Most of the faces were unfamiliar. I didn’t know their names or their epithets.

There were senior members of the Black Dragon Demon Gate and leaders of Gansu Murim, each of them heading a martial faction large or small.

At the center of them all stood Sima Gong.

“Can I ask a few questions?”

“Anything.”

“I can’t imagine you decided all of this on your own. Am I right?”

“Of course. The Sect Leaders gathered here and the Kongtong Sect agreed as well.”

“Then what if Dark Heaven isn’t targeting Gansu…”

“We’ll leave some forces behind and head straight for Qinghai. But that won’t happen.”

“Why not?”

“The signs are ominous. The Demonic Cult may have become Dark Heaven, but the enemies beyond the desert have always been our greatest concern. That remained true even after the Great Faction War.”

“What signs?”

“It’s too early to say. I’ve already selected people I can trust and sent them to scout beyond the desert. We’ll know for certain when they return. So…”

Sima Gong’s gaze moved from me to Jeok Cheongang.

“Please leave Gansu’s defenses to us and go to Qinghai, Senior. Even with reinforcements from Huashan and the others, Qinghai seems to be the place where every moment counts most.”

“Qinghai, Qinghai…”

Jeok Cheongang murmured the name in a low voice, almost like a groan.

That was when it happened.

“L-Lord Sect Leader!”

A frantic voice rang out from between the tightly shut doors.
## Chapter artifact 1007

# Chapter 1007

For someone born and raised in Gansu Province, the pale sandstorms that swept through in every season were nothing unusual.

Since time immemorial, from the days when the river that flowed through the region came to be called the Yellow River, their ancestors had recorded the existence of the loess-colored plateau.

No one knew exactly when it had formed or why, but the plateau was still there.

On days when a strong wind blew in from somewhere, it would sweep through the area like a waterspout, then vanish, scattering fine, soft loess like stars.

That was probably why.

The martial artists of the Black Dragon Demon Gate standing watch atop the city wall felt little as they watched a cloud of dust approach from the far north.

“Damn it. Here we go again.”

One of the martial artists frowned. The middle-aged man leading their squad pulled a scrap of cloth from inside his clothes with a practiced motion.

“Shut your mouth and put on your mask. Don’t stubbornly stand there like last time, then spend the next few days complaining.”

“No, I really couldn’t help it that time. How are you supposed to dodge when it hits you all at once? It takes your breath away.”

“Do whatever you want. If you’d rather eat a handful of sand than your next meal.”

Just then, as chuckles rippled through the group, someone watching the cloud of dust spoke up.

“Still, what’s coming now is small and cute. Looks like it’ll die down on its own before it even gets here. The scouts way out front are going to get buried, though.”

“Oh, you’re right. Captain, why’d you put on your mask?”

They’d dealt with this more times than they could count. By now, they knew the drill.

It wasn’t a sandstorm towering more than ten jang high. There was no need to make such a fuss over a little cloud of dust.

Without even bothering to check for themselves, the martial artists teased their Captain, who’d put on his mask early.

“Look at you, Captain. You’ve lost your touch.”

“The Blood-Death Sword title will be weeping. Heh.”

“Now, now. You can tell what it is at a glance. Why the rush? I used to be a mounted bandit when I was young, and I know a group of about thirty riders traveling side by side kicks up a cloud about that size. It’s nothing.”

In that instant, the Captain’s already fearsome face twisted into something monstrous.

“What?”

The laughter slowly died away.

His subordinates remembered that the Captain had once been fairly notorious in the area. They swallowed hard.

“W-we didn’t mean it like that, Captain……”

But at the Captain’s next words, the men who’d been on edge could only stare at him in confusion.

“No, not that.”

“Pardon?”

“The last thing that guy said. What was it?”

Everyone’s eyes turned toward the mounted bandit. He blinked.

“Me?”

“Yeah. Say what you said before again.”

“Uh, well, you can tell what it is at a glance, so why the rush—”

“Not that, you idiot! The next part!”

“Th-that a cloud of dust that size means about thirty mounted—”

“And how many scouts left half a shichen ago?”

“Exactly thirty. Was that when they got their horses earlier? I remember because they made a huge fuss, demanding better mounts since they had to patrol until sunset……”

His voice cut off before he could finish.

Only then did the martial artists realize something was wrong. Their eyes darted back and forth as they held an inaudible conversation among themselves.

*Wait. What’s going on?*

*An unusually small cloud of dust. Thirty mounted warriors. And, finally, thirty scouts.*

*Something feels off.*

*Why are they back already if they weren’t supposed to return until after sunset?*

*That feels even more off.*

*Maybe they had to take a dump?*

*You can shit anywhere, cover it up, and call it a latrine. What kind of lunatic would abandon a mission just to come back and relieve himself?*

*Isn’t that what everyone does? I do.*

*You’re a real lunatic.*

*This feels seriously wrong.*

No matter how hard they thought, no matter how much they wracked their brains, something was clearly amiss.

Gulp.

In the strange tension, just as someone swallowed dryly—

Fwoooosh! Boom!

Hundreds of jang away, red smoke shot up from the pale cloud of dust. The Captain recognized what the signal flare assigned to the scouts meant and forced his voice out.

“Suspicious persons spotted……!”

Suspicious persons meant people acting strangely—in other words, unfamiliar intruders.

At last realizing what was happening, the martial artists atop the wall shouted as if coughing up blood.

“Real situation! This is real!”

“What are you waiting for, you bastards? Move your asses!”

“L-let the Sect Leader know! Hurry!”

The wall erupted into chaos as if a powder magazine had exploded. Meanwhile, the flare that had burst brilliantly in the sky slowly drifted down over the thirty scouts racing toward them with all their might, raising a cloud of dust.

And on one of the dozens of hills, a group watched the scene with their backs to the shadows.

“Well…… this is a hell of a mess.”

About fifty mounted warriors of unknown identity stood there. At the front of the group, a giant let out a low groan. Beside him, another man scratched at his shaggy hair.

“Ah, damn it. This is driving me crazy. Didn’t your little brother tell you we should approach slowly and gently?”

The giant frowned.

“I didn’t think they’d panic and run. We even brought a white flag just in case. Why are those bastards so scared?”

“Do you really need to ask? Take a look at your own face, Big Brother. Do you think anyone’s going to take a white flag as a friendly gesture when you look like that?”

At someone’s chiding, agreement erupted from all around them.

“He’s right. Your face is downright terrifying. What good’s a white flag going to do?”

“They probably thought you were offering your condolences in advance to the poor bastards about to die.”

“It wouldn’t have helped if you’d gone over wearing white clothes instead of carrying a white flag.”

“Then they’d think you’d dressed in mourning ahead of time to offer your condolences to the poor bastards about to die.”

“Nothing to be done. Even the Heavenly Demon’s granddaddy couldn’t beat Big Brother when it comes to looking vicious.”

“Damn it. This whole situation’s going to shit, and now I’m starting to get nervous. What if we ride over there and they shower us with arrows?”

“Can’t be helped. Big Brother, since it’s come to this, let’s just turn around and go back.”

“Second Brother, are you scared?”

“Enough! Who’s scared? I just remembered I left something important behind!”

“Looks like you brought your shriveled-up guts along just fine…… Ah, you left your balls behind.”

“Enough! Third Brother, how dare you!”

“Honestly, you keep going on like that. It’s only cool when a Supreme Peak master does it. You can’t pull it off, Second Brother.”

“Enough! Do you have to see your own coffin before you learn your lesson?”

“I’m going to lose my mind if I have to keep listening to that. You’ve picked up a weird habit. So, Big Brother, what are you going to do?”

At the question from the man called Third Brother, the giant, who’d kept silent even as voices flew back and forth, finally spoke.

“We’re not turning back.”

His voice was as heavy as his build. With a steady gaze, the giant stared at the loess-colored wall standing tall beyond the shimmering heat.

“I know what you’re all worried about…… But this is a personal request from the Great One. If you’re men who understand loyalty, do as I say.”

“……!”

“……!”

At the giant’s stern words, the eyes of the six men who called him Big Brother trembled.

Of course, the mutters that followed weren’t the reaction the giant had hoped for.

“There he goes, putting on a show again.”

“Now we’re the bad guys.”

“He’s a bear in name only. He turns into a fox whenever it suits him. Am I right, brothers?”

“Still, we should all do as Big Brother says. Besides, this request came from the Great One himself. What choice do we have?”

“Enough……”

“Please, someone gag Second Brother. Listening to him is giving me qi deviation.”

Most of them grumbled like children who’d had their sweets taken away. But the giant—and the dozens of mounted warriors watching from behind him—knew the truth.

Even though things had turned out this way, their purpose hadn’t changed.

And the strongest proof of that conviction was the person who’d sent them here.

“Let’s go. The sun’s going to set at this rate.”

Bathed in the sunset spreading late from the west, the fifty or so mounted warriors set off over the hill, led by the giant.

Before long, they reached the wall. Waiting for them were hundreds of arrowheads trained on them, and unfamiliar faces visible between the shafts.

“Stop! Stop! Stop! Hands up! Move and we’ll shoot!”

At the shout from some young pretty boy, the giant calmly reached into his clothes to pull out the white flag he’d prepared.

Or rather, he tried to pull it out.

He didn’t get the chance—not before that young man issued a command he hadn’t expected.

“Fire!”

“……Huh?”

* * *

Fwoosh, fwoosh, fwoosh, fwoosh!

Hundreds of arrows tore through the air.

Their strength varied, but large or small, once they were imbued with internal energy, they plunged down in straight lines instead of arcs.

Straight at the unexpected visitors.

Clang-clang-clang-clang!

Sparks flew in all directions.

The giant stood ahead of his dozens of subordinates, alone. Having survived the net of arrows that had densely covered a thirty-jang radius, he bellowed.

“Are you out of your damn mind? Who starts shooting arrows without warning?”

Jeok Cheongang, standing beside me, nodded.

“He looks vicious as hell, but I can’t help agreeing with him. Have you been seized by a mind demon or something?”

“No, I’m fine.”

“Then why?”

“I told him to put his hands up, and he didn’t listen. That bastard tried to pull a fast one on me.”

“You’re insane.”

“Honestly, I didn’t think they’d really shoot. I thought they’d ignore my order. Judging by their level, though, I figured they’d survive a volley like that, so I did it as a warning. Anyway, no harm done, right?”

“Infinite Life Buddha……”

The Wind-and-Cloud Sword Lord muttered, looking appalled at my airtight conclusion. Unlike him, the Black Night King Sima Gong let out a hearty laugh.

“Haha! Straight to the point. We could’ve used someone like you on our side.”

“……”

Was that a compliment or an insult?

While I was trying to decide how to respond, the giant, whose face was so vicious it was hard to believe anyone could actually look that way, shouted again.

“Don’t shoot! I said don’t shoot! Can’t you see what I’m holding?”

*Flap.*

So that was what he’d reached into his clothes for. What the giant was waving around was a large piece of cloth.

A questionable shade of yellow, completely covered in sand and loess.

“What on earth is that supposed to mean? Why’s he waving around that dingy yellow thing?”

“Yellow cloth…… Wait, could he be a Yellow Turban?”

“That makes no sense. What era do you think this is? How could the Yellow Turbans still be around?”

At the sight of everyone debating, I felt the weighty responsibility of having to offer another clear-cut answer.

*A suspicious-looking guy with a vicious face. And the others with him look like they’ve each got at least eighteen prior convictions.*

No matter how I looked at it, there was only one solution that came to mind.

“Prepare a volley.”

“Uh……?”

“Fire!”

Fwoosh, fwoosh, fwoosh!
## Chapter artifact 1008

# Chapter 1008

To cut to the chase, by the time the third volley of arrows had ended, the leaders of the Gansu Murim had decided to welcome the fifty-odd suspicious-looking men—including the giant—inside the gates.

Of course, saying the decision reflected the opinion of the entire leadership would be misleading.

Jeok Cheongang’s presence had played a very large part in it.

“I don’t know what hole these mangy mutts crawled out of, but let them in alive for now.”

Then he added, addressing the murmuring leaders:

“What are you sitting there agonizing over? If they seem suspicious, kill them and send them back out.”

“Oh.”

“Ah.”

It was such a clear-cut answer that even Judge Bao would’ve brought his dog-headed execution blade down with a smack. The meeting that hardly deserved to be called a meeting came to an end, and the Black Night King, Sima Gong, immediately ordered his subordinates to admit the hideous-looking unwelcome guests.

*Rumble, rumble.*

The massive iron gates began to open, little by little.

The giant was the first to step through the gap. He swept his bulging eyes around the area.

He’d damn near shit blood dodging three volleys of arrows, and now he looked like he’d been dragged through a shredder. His half-rolled eyes darted about, searching for someone.

Someone like the young bastard who’d suddenly ordered the archers to fire.

“Looking for someone? Keep that up and you’ll get a crick in your neck. Want me to find them for you?”

I’d come down first to greet our unexpected visitors. I tossed out the question as I stepped forward, and the giant’s eyes widened.

“You, you…!”

“I saw it all from up there. Nice job blocking them. Nice job dodging, too.”

“You pretty little gigolo-faced bastard, how dare you!”

“What did you just call me?”

Something in my expression hardened. At the strange pressure pouring off me, the giant flinched on instinct, then forced out another strained reply.

“I said you look like a pretty little gigolo…!”

“Hold on. Just hold on a second.”

“What?”

Leaving the giant’s angry, baffled question hanging, I closed my eyes.

*He said I look like a pretty little gigolo.*

What a wonderful thing to hear.

For a man of the same sex and the same chromosomes to say that to me was the highest praise imaginable.

I held on to the lingering swell of emotion washing over me, then opened my eyes.

“Thanks. Turns out you’re a good guy.”

“…?”

“So, where are you from, our Junggeol?”

“……!”

The giant—or rather, Ma Junggeol—nearly popped his eyes out of his head.

“How did you know?!”

“Hm? Know what?”

“My, my name.”

Seeing him stumble over his words now, I answered as casually as could be.

“Didn’t I tell you? We already introduced ourselves. You’ve forgotten that fast?”

“I…?”

“You must still be rattled. Fair enough. You had to dodge all those arrows.”

Ma Junggeol would probably never know.

At this very moment, a translucent holographic window was floating like a ghost above his head.

> **System**  
> **Level:** 80  
> **Name:** Ma Junggeol

Level 80.

A person’s level wasn’t an absolute measure of their strength, but even so, it was awfully low for someone I’d suspect of being a Dark Heaven lackey.

*Going by what I saw earlier, he’s maybe a fairly seasoned Peak master?*

Still, you couldn’t let your guard down so easily.

As I slowly looked over Ma Junggeol, who still seemed dazed, the leaders atop the wall finally appeared on the stairs, Jeok Cheongang among them.

At the same time, the fifty-odd mounted men came rushing toward us.

“Stop!”

“Let’s talk! Let’s talk!”

“We don’t want to fight!”

“Big Brother! Are you all right?”

“Enough!”

“I can’t believe this. I told you to stop doing that.”

Six men, riding side by side at the very front of the group, surrounded Ma Junggeol.

*What the hell are these guys?*

I was sure everyone there was thinking something much like I was.

The lanky one. The dwarf. The bulbous-nosed one. The tiny-eyed one…

Every one of them had striking features and facial parts that seemed to have gone their own way. It was a combination you didn’t see every day. And Ma Junggeol, standing in the middle of those six men, was the finishing touch.

*Was his father Picasso?*[^1]

They all had such strong impressionist faces that even the Black Dragon Demon Gate’s martial artists—who’d been through their share of life at the bottom—instinctively reached for their sword hilts.

*Shing.*

As the faint sounds of friction from here and there heightened the tension, a low voice reached everyone’s ears.

“I guarantee that any of you who try something stupid from this point on will be spending a very hot time with this old man.”

No one present needed to ask who’d spoken.

And, naturally, not even Tokyo Hot could hold a candle to the JCK-444 Fire Show Special. No one wanted to star in it.[^2]

*Clatter, clatter, clatter.*

The sea of people parted to either side, as though fleeing a raging inferno.

Jeok Cheongang emerged through the gap, leading the other leaders. He glanced at Ma Junggeol, then turned to me.

“So, who is he, and where did he come from?”

“His name is Ma Junggeol. I don’t know where he came from yet.”

“Could he be a Dark Heaven lackey?”

“We’d have to beat the truth out of him to be sure. But, as you already know, he doesn’t look or seem capable of pulling anything clever…”

“You can’t judge by appearances alone. What do you think about the possibility that they’re deliberately hiding their strength?”

Jeok Cheongang wasn’t asking because he didn’t know. He meant for everyone listening to our conversation to hear the question. Once I understood his intent, I answered without hesitation.

“None.”

“You must have a reason for thinking so.”

“Old man—no, Master, if they were strong enough to fool you and the others here, they’d have to have reached at least Returning to Simplicity or Bone Transformation.”

“And?”

“Look at those faces. Supreme Peak masters who’d reached that level couldn’t possibly look like that.”

“……!”

“……!”

The seven vicious-looking men, Ma Junggeol included, shuddered. What could I do? It was true.

I’d suddenly found myself playing lawyer, and I felt an inexplicable sense of duty as I continued.

“Therefore, I find no grounds to charge them with ‘vicious-looking men concealing their martial arts,’ and I rest my case.”

Jeok Cheongang nodded with an expression of admiration.

“Your words are so logical that even this old man hardly dares to argue.”

“Thank you.”

“But looking at those faces—whether they’re Yellow Turbans, Dark Heaven, or at the very least men who’ve taken up important posts in the Demonic Cult—I can’t help but find them suspicious.”

“So what are you going to do?”

“Either they confess everything right now, or I’ll beat it out of them with the Flame Divine Palm.”

His voice was directed at me, but his gaze wasn’t.

Under Jeok Cheongang’s stare, which seemed to pour streams of fire, Ma Junggeol went pale and stammered:

“A-are you really the Fire King, Jeok Cheongang, Great Hero…?”

Jeok Cheongang replied with a bored look.

“Of course I’m real. Did you think I was a fake?”

“If that’s true, then the pretty little gigolo—no, the young man—is the Blazing Flame Divine Dragon…”

It was my turn to speak.

With a broad smile at hearing that pleasant description again, I tried to comfort the terrified Ma Junggeol.

“Keep calling me pretty little gigolo. Make yourself comfortable. Come to think of it, I was rude, speaking casually to you all this time. I’m sorry. Okay?”

“N-no, that’s all right. But it seems there’s been a misunderstanding for a while now. May I say something to clear it up?”

“Now you’re talking. You should’ve said—spoken up sooner.”

“I was trying to explain, but you jumped straight to—”

“Go on, then. Get to the point.”

At my gentle but forceful urging, Ma Junggeol hesitated, then straightened his shoulders and cautiously addressed the leaders, Jeok Cheongang included.

“To cut to the chase, we came from Ningxia.”

“Hold on. Ningxia? Could you be…?”

As a thought suddenly crossed my mind and I frowned, Ma Junggeol hurriedly added:

“We’re not mounted bandits!”

Jeok Cheongang muttered:

“So that’s why their faces looked so suspicious. They’re those mounted bandits who’ve been spreading filth all over Ningxia Province.”

“I-it’s true that I briefly belonged to a band of mounted bandits, but that’s not who we are now…”

Just then, the Wind-and-Cloud Sword Lord cut in.

He eyed Ma Junggeol and his men with narrowed eyes.

“Infinite Life Buddha. I shouldn’t say this as a man who pursues the Way, but as Senior Jeok said, those faces are clearly from the profession.”

People nodded here and there in agreement.

Then, as if to prove why looks ruled modern society, the mood slowly turned hostile. One person’s lips parted.

“Ma Junggeol, Ma Junggeol… Could you be that very Ma Junggeol of Baekma Bang?”

It was the Black Night King, Sima Gong.

He’d been deep in thought with his brow furrowed. At his question, Ma Junggeol and his men—whose faces had been turning more and more yellow—visibly brightened.

“Y-you know me?”

“I’ve heard of you through the grapevine. More than ten years ago, an unknown master pacified the mounted-bandit gangs in Ningxia Province. A few of their leaders changed their ways under his guidance, joined forces, and founded a horse caravan.”

“That’s right! That’s me—or rather, that’s us!”

As though he’d finally found someone he could talk to, Ma Junggeol’s color returned. His expression grew serious as he saluted everyone with clasped hands.

“I am Ma Junggeol, Chief of Baekma Bang. The Seven Masters of Baekma Bang greet the heroes of the Murim Alliance.”

“……?”

“……?”

A suffocating silence pressed in from all sides.

Their elegant titles didn’t fit their vicious faces at all. The leaders and I silently exchanged glances, while the six men, prompted belatedly by Ma Junggeol, awkwardly copied his salute and whispered among themselves.

“Uh, is this how you do the salute, hyungs?”

“You idiot. How many times have I told you to cover your left hand with your right palm?”

“What are you talking about? The youngest did it right. Fourth Hyung’s the one doing it wrong.”

“Oh, you’re right…”

“Enough! Can’t you all shut up? Do you know what kind of place this is?”

“Sheesh. A minute ago you were shouting ‘Enough! Enough!’ at the top of your lungs. Now you lower your voice because there are masters around. Being born later is my fucking crime. My crime.”

“……”

What the hell was going on with these guys?

Their voices were low, but their conversation still came through clearly. Everyone’s eyes had gone flat and dead. Only Sima Gong managed to keep his composure as he spoke.

“Yes, I’ve heard about Baekma Bang a few times. I hear you’ve fought off the nomads who invaded through the northern Great Steppe and given plenty of help to the commoners who’ve only recently begun settling there. But…”

Sima Gong let his voice trail off. His gaze suddenly sharpened.

“What brings you here so abruptly?”

Under the concentrated gaze of everyone around him, Ma Junggeol straightened his bent back and answered.

“We came here to offer our help.”

“Help with what?”

“Dark Heaven. We have important information about them.”

“……!”

[^1]: Picasso was a modern Spanish painter whose work is associated with Cubism and other avant-garde styles. Taekyung jokes that the men’s faces look like impressionist paintings.

[^2]: Tokyo Hot is a Japanese adult-video studio. JCK-444 is presented here as a particularly fiery adult-video special.
## Chapter artifact 1009

# Chapter 1009

If Ma Junggeol had given even the slightest suspicious or flimsy reason, he would’ve been thrown straight back out the gate—or stuffed into the underground prison somewhere inside the city to have a long chat with the torture specialists.

But the reason Ma Junggeol gave in his lowered voice was more important than I’d expected.

“Dark Heaven. I have important information about them.”

“……!”

The moment those words left his mouth, all of us in the leadership—including me—realized that our unwelcome visitors might be a lot more useful than we’d thought.

“Well, we’ve kept our distinguished guests standing outside for far too long. Why don’t you come in and have a cup of tea?”

At Sima Gong’s subtle invitation, Ma Junggeol, who’d straightened his shoulders as though nothing had happened, nodded.

“Sounds good. Just so you know, of all the teas, my brothers and I favor grain tea most.”

“I heard the Seven Masters of Baekma Bang were renowned drinkers. You’re every bit as forthright as they say. Come on in, then.”

Important conversations were best held where fewer people could listen in.

And so, in the space of a few moments, Ma Junggeol and his six men went from unwelcome guests to honored visitors. Or, more accurately, the Seven Masters of Baekma Bang took their places in the grand meeting hall.

“Ahhh. That’s good.”

Starting with Ma Junggeol, his six sworn brothers drained a small wine jar in one go, then smacked their lips.

“Whew, that’s really something.”

“What kind of liquor is this? It just melts on your tongue.”

“Right? It’s insane.”

“……Isn’t that what liquor does? It’s liquor, so of course it melts. What do you mean, it melts? This is why people call you idiots.”

“Enough! Fourth, is that any way to speak to your brothers?”

“Whew, look at you raising your voice again the second you’re out of trouble. Honestly, if I had my way, I’d crack this wine jar over your head right now.”

Naturally, no one’s head and a wine jar met in a tragic collision.

That was thanks to Jeok Cheongang, who’d been silently watching the seven-colored mounted-bandit rangers—or rather, the Seven Masters of Baekma Bang.

“Did you come here to drink?”

“……!”

“……!”

“You’ve wet your throats. Now, go on and spit it out.”

Ma Junggeol flinched at the menacing aura rolling off Jeok Cheongang. Then he stammered out a reply.

“F-first, I assume you already know something about the situation in Ningxia.”

“I’ve heard the basics. Because of mounted bandits like you, the place nearly became a battlefield, but it’s been quiet for the past few years. Is that right?”

“We’re no longer mounted bandits, but yes. Great Hero Jeok is right.”

“Still look like a bunch of mounted bandits to this old man, but go on.”

“There’ve been a few minor disputes over the years, but it’s become a fairly livable place. Anyone who’d done something they might feel guilty about left long ago. The ones who remain have completely turned over a new leaf and live ordinary lives, like me and my brothers. Sect Leader Sima here knows this well, too.”

Everyone’s eyes naturally turned to him. Sima Gong nodded calmly.

“It’s true. As Ningxia Province settled down, various merchant caravans began passing through, and we heard all sorts of things from them. That was when I first heard about Baekma Bang.”

Bolstered by Sima Gong’s support, Ma Junggeol quickly picked up the thread.

“I don’t know exactly what you heard, Sect Leader Sima, but Baekma Bang is by far the largest group in Ningxia Province. Recently, we’ve even been opening a new trade route to help Ningxia Province prosper.”

“Wait. This new trade route you mentioned—is it perhaps…?”

“It’s probably where you’re thinking.”

Surprise spread across Sima Gong’s face at Ma Junggeol’s answer.

Watching him, a thought suddenly crossed my mind.

“To the west. It’s west.”

“……!”

My sudden words sent an invisible ripple through the room.

Naturally.

The west I meant wasn’t Gansu or Qinghai.

“Xinjiang…”

The word slipped through the Wind-and-Cloud Sword Lord’s lips like a groan.

The Taeeul Merciless Sword and the Roaring Fury Swordsman had been watching Ma Junggeol with obvious disapproval for a while now, as though something about him rubbed them the wrong way. They frowned and spoke up, too.

“So that’s what this is about. Xinjiang, huh. Hah.”

“I can’t listen to this anymore. How long are we supposed to sit here listening to such ridiculous nonsense?”

Much as I hated to admit it, those two were the ones reacting in the most reasonable way.

What kind of place was Xinjiang?

It was even called the Land of Ruin.

A cursed land of endless deserts and Fiends who proclaimed the world belonged to the Demonic Path.

And a mere horse-caravan group—not one of the Nine Sects and One Gang or the Five Great Families—was supposed to open a trade route to Xinjiang?

*What a joke.*

But at the same time, I could feel my heart starting to beat faster and faster.

The Taeeul Merciless Sword and the Roaring Fury Swordsman had forgotten the most important thing.

This wasn’t a pitch for investment or a business presentation.

Ma Junggeol’s story wasn’t over yet. In fact, the real story was just beginning.

“That’s enough preamble, isn’t it?”

Jeok Cheongang’s low question left no doubt what he meant. Ma Junggeol took a deep breath and spoke again.

“Even after things settled down, Ningxia Province was still in bad shape. The land was barren, and the nomads from the Great Steppe along our border raided us every harvest season. We needed a new way out to change things.”

“So you wanted to cross the desert and open a trade route?”

“That was the idea, but it was nothing more than a pipe dream. Even an uneducated fool like me knew people like us couldn’t seriously dream of something so far beyond our reach. But…”

Ma Junggeol’s gaze suddenly shifted toward me.

“Not long ago, an opportunity came out of nowhere. The many nomads occupying the western Great Steppe suddenly began a mass migration.”

“Jamukha.”

A name slipped from my lips before I could stop it.

Only then did I understand what Ma Junggeol meant when he’d talked about an unexpected opportunity.

Jamukha’s massive army had controlled the western steppe.

They’d taken almost all their forces and marched into Shanxi Province. The void they left behind had become a golden opportunity for Baekma Bang.

“Then were you trying to reach Xinjiang through the steppe?”

At my question, gasps came from around the room.

That was right.

The other option—the one that had become so obvious that everyone had forgotten it—was the Great Steppe, which the people of the Central Plains had long considered another forbidden land alongside Xinjiang.

It was the fastest route across the desert.

Under everyone’s focused gaze, Ma Junggeol nodded, his face tense.

“That’s right.”

“……!”

“I picked out the men under me who were good riders, and we kept driving our horses without stopping. After riding like mad for ten whole days, we finally saw a vast yellow stretch of land in the distance. We’d reached the desert.”

Just then, his six sworn brothers, who’d been keeping an eye on everyone’s reaction behind him, nodded and chimed in.

“Man, it was a real shitshow. Honestly, I wanted to say to hell with the Chief and the whole damn venture and turn back.”

“But what could we do? We’d already come that far. We figured, since we were there, we might as well step on the sand before we went home.”

“Then we traveled for another ten days or so, right?”

“Don’t remind me. Even now, just thinking about that goddamn desert makes my knees buckle.”

“Enough! You bunch of weaklings. Even in those hard times, I trusted the Chief and followed him.”

The diminutive middle-aged man, who looked rather old, delivered a stern rebuke. The man with the bulbous nose snorted.

“They say even if a horse’s hooves go crooked, you should keep a firm grip on the reins. So at least get your story straight. When those black bastards showed up on the tenth day, what did you do, Second Hyung? You didn’t even look back—you went straight to getting ready to run.”

“Enough…!”

The dwarf’s face turned as red as a ripe persimmon. He lunged at the bulbous-nosed man, but I was much faster.

*Snatch.*

A small fist landed perfectly in my grasp.

I’d caught the dwarf’s punch with ridiculous ease. I fixed the bulbous-nosed man with a cold stare.

“Say that again.”

“W-what?”

“You just said those black bastards appeared on the tenth day after you entered the desert.”

He’d said it in passing, but every one of us in the room had heard him clearly.

And the moment we heard it, the suspicion that arose in our minds turned to certainty.

“It was Dark Heaven.”

Ma Junggeol spoke up in place of the bulbous-nosed man and continued.

“They numbered only a few dozen, but I’m certain. I’ll stake my life on it.”

Sima Gong spoke in a grave voice.

“What makes you so certain?”

“We followed them.”

“What?”

“We managed a day and a half. That was the best we could do. But I saw it with my own eyes. That night, when the moon was unusually bright, at least a thousand tents covered the sand dunes.”

“……!”

“There’s only one force in the western desert that could mobilize an army that large. Dark Heaven. Isn’t that right?”

A cold silence filled the meeting hall instead of an answer.

A thousand. Not a thousand people—he said there were a thousand tents.

What’s more, Ma Junggeol’s route across the desert was clearly closer to Gansu than Qinghai.

That meant at least several thousand, perhaps tens of thousands, of enemies were targeting Gansu Province.

*And even that might not be all of them.*

My mind went cold. Meanwhile, my heartbeat had grown so fast it was thundering in my ears.

Of course, it was too soon to be certain.

There was still a question I needed answered before I could decide anything.

“You’re lucky you made it back alive.”

Sima Gong’s low voice broke the momentary silence.

Under his deep, penetrating gaze, Ma Junggeol licked his parched lips.

“It was close. I thought my heart was going to burst.”

“You know what I’m asking. Are you pretending not to?”

“We kept a distance of exactly a hundred li. It was hard at first, but after that it got much easier as their numbers kept growing by the hour.”

“An ordinary horse-caravan group following Dark Heaven without being spotted. Is that possible?”

“I’m ashamed to say it, but we’re not an ordinary horse-caravan group, are we? We may not wear our hair in queues, but when it comes to riding or having a sharp eye, we’re no different from the nomads.”

“You could have turned back as soon as you spotted them. Why follow them for another day and a half?”

“That… that’s…”

Ma Junggeol hesitated for a moment, glanced at Sima Gong, then cautiously spoke up.

“I’d heard that if you render a service for the good of the realm, no one cares where you came from.”

“You were thinking about a reward?”

“Yes.”

It had been possible because they were a small group that was hard to spot, and because they were former mounted bandits who’d learned how to survive.

And their reason was clear, too.

After a moment’s thought, I turned to Jeok Cheongang and spoke.

“Now I know for sure where we need to fight.”

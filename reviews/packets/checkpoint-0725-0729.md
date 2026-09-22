# Checkpoint Review — 725–729

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

# Chapters 725–729

## Plot

Jin Taekyung tells Jeok Cheongang that the Lord of Heaven has taken a personal interest in him and that Dark Heaven’s fanatical servants may treat their leader as a living god. Jeok accepts Jin’s account of traveling between Murim and another world resembling the realm of immortals, recognizes the coming war’s danger, and asks Jin to reveal everything he has hidden. Jin later returns to the modern world relieved that Jeok accepts him as Jin Taekyung rather than as a mysterious Little Immortal.

At the Peace Guild, Jin reveals that he created the beginner-friendly Smiling Mana Cultivation Method and intends to distribute it worldwide. Choi Minwoo warns that major Hunters and Guilds will resist a technique that undermines their control, while Jin argues that rising mana, mutation Gates, and monster waves make widespread cultivation necessary. Jin’s recent campaign against rebels and terrorists was partly intended to reduce the danger of the method being misused. He proposes using Choi’s status as Cheon Taemin’s sole blood relative and heir to promote the release.

The Peace Guild commits to an ambitious international expansion despite the risks. Choi’s resolve is strengthened by a message left at a deceased loved one’s grave, and he brings President Baek Hanseong into the plan. Meanwhile, a ghostlike infiltrator exploits a brief blackout at a government building, steals an unknown item from underground evidence storage, bypasses the alarms, and escapes unseen.

Jin and Choi rename the method the Heaven and Earth Cultivation Technique and secure government backing. Baek announces a major, government-supported release as a Korean national project, provoking worldwide media upheaval and broad public praise. Ares Guild executives confront Choi for acting without notice, but Cheon Taemin’s name and Choi’s legitimacy restrain their opposition. After Choi apologizes, Jin challenges the executives’ silence, leaving their response unresolved.

## Continuity

- Jeok Cheongang accepts Jin Taekyung’s cross-world origin and asks him to disclose his remaining secrets.
- Dark Heaven’s full strength, the Lord of Heaven’s intentions, and the coming war remain major threats.
- Jin created the stable, beginner-accessible Smiling Mana Cultivation Method.
- The method has been renamed the Heaven and Earth Cultivation Technique and is scheduled for public release through government cooperation in two days.
- Jin and Choi Minwoo are concealing both Cheon Taemin’s unconscious condition and Jin’s authorship of the technique.
- Jin believes broad cultivation is necessary because increasing mana is producing stronger monsters, mutation Gates, and monster waves.
- Jin’s campaign against rebel groups and terrorist organizations was intended partly to reduce threats before the technique’s release.
- Choi is Peace Guild Master, controls the Ares Guild, and is Cheon Taemin’s sole blood relative and heir.
- Jin, Choi, Im Kkeokjeong, Song Song, and the Skeleton King have committed to the dangerous international expansion together.
- President Baek Hanseong has publicly committed the Blue House to the release and framed it as a Korean national project.
- The announcement has triggered intense international media attention and mostly favorable public reaction.
- Ares Guild executives remain uneasy about Choi’s unilateral authority; Jin has confronted them after Choi’s apology.
- An unidentified ghostlike entity stole an unknown item from a government evidence storage room during a blackout. A Security Team employee named Sehwan unknowingly passed near its shadow.
- Open hooks: the contents of the upcoming announcement, the technique’s distribution and regulation, the Ares executives’ response, the exposure of Cheon Taemin’s condition and Jin’s authorship, and the identity of the infiltrator and possible media leaker.

## Translation Decisions

- Render **선계** as **realm of immortals** and **소신선** as **Little Immortal**.
- Render **싱글벙글 마나 연공법** as **The Smiling Mana Cultivation Method** when discussing its original name.
- Render **천지심법** as **The Heaven and Earth Cultivation Technique** after its renaming.
- Render **구세주 코인** as **the Savior coin**.
- Render **심판의 일주일** as **The Week of Judgment**.
- Render **국뽕** as **patriotic high**.
- Preserve Jin Taekyung’s profane, self-mocking comic voice, the Skeleton King’s archaic grandeur, and the informal tone of online forum dialogue.
- Preserve uncertainty around the infiltrator, the stolen item, and the deceased person connected to Choi’s resolve.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung and Choi Minwoo are preparing a public release of Cheon Taemin's Heaven and Earth Cultivation Technique.",
    "The technique is safe and versatile enough for even the lowest-ranking Hunters to learn, though its immediate effects are limited.",
    "Baek Hanseong has committed the government to cooperation and announced an imminent major announcement through an emergency Blue House press conference.",
    "The release is being presented as a national project associated with Korea and Cheon Taemin.",
    "Jin and Choi are concealing Cheon Taemin's unconscious condition and Jin's authorship of the technique.",
    "The announcement has caused worldwide media upheaval and broad public praise.",
    "Ares Guild executives are uneasy about Choi's unilateral decision-making but are constrained by Cheon Taemin's legitimacy.",
    "Jin has confronted the executives after Choi apologized for withholding advance notice."
  ],
  "continuity_sources": [
    729
  ],
  "open_questions": [
    "What will be revealed in the major announcement two days later?",
    "How will the Heaven and Earth Cultivation Technique be distributed and regulated after its public release?",
    "Will the Ares executives accept Choi's authority or continue challenging his decisions?",
    "How long can Jin and Choi conceal the truth about Cheon Taemin and Jin's authorship?",
    "Who is leaking the unidentified sources that are fueling media speculation?"
  ],
  "safe_through": 729,
  "temporary_decisions": [
    "Render 천지심법 as The Heaven and Earth Cultivation Technique.",
    "Render 국뽕 as patriotic high.",
    "Preserve Jin's profane comic banter and the online forum's informal tone."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 725

# Chapter 725

“Let’s talk.”

At the Sound Transmission that pierced my ear, I gave a small nod and loosened my grip on the reins.

The beast noticed and gradually slowed its pace. Jeok Cheongang, who had been traveling alongside me, parted his lips.

“Is it true that the Lord of Heaven has taken an unusual interest in you?”

“Yes.”

“Huh. Strange. This old man is hearing about it for the first time.”

“I suppose so. It’s the first time I’ve mentioned it, too.”

“Why didn’t you tell me?”

“You never asked.”

Honestly, even as I answered, I expected to get hit at least once.

But Jeok Cheongang merely stared at me as I instinctively assumed a defensive stance like lightning. Then he muttered in a calm voice, as though speaking to himself.

“You don’t tell me because I didn’t ask… Hm. That isn’t entirely wrong.”

What was wrong with this old man all of a sudden?

“Um, Old Master?”

“What.”

“Are you… sulking?”

“What? Sulking? Me?”

“Yes.”

Jeok Cheongang burst into laughter, as if he had just heard an incredible joke.

“Why would this old man sulk? I’m not a five-year-old child. Of course, we had more than enough time to discuss it over the past three days, and this old man didn’t ask because he was thinking of you, but that has nothing whatsoever to do with anything, so don’t worry about it. In the end, the idiot is the one who didn’t ask, isn’t he? Hahaha.”

“……”

“People of the martial world say that a Master and Disciple should have no secrets between them. But that doesn’t apply to us, so don’t concern yourself with it. Come to think of it, this old man needed someone to carry on the Fire Gate Clan’s lineage, and you needed martial arts, so we helped each other out. That should be enough. Besides, talking about the bonds between Master and Disciple in a world like this is laughable.”

“……”

“This old man ran all the way to Nanman until something nearly fell off because I was afraid something might happen to you. I even plucked out all my perfectly good hair to hide my identity, but I’m fine. In the end, that didn’t fall off either, and my hair will grow back soon enough. Of course. Naturally.”

“……”

“Why would this old man sulk just because he didn’t hear some goddamn story? A thirsty man should dig his own well. If I waited for you to tell me when the time was right, wouldn’t I end up dried out and dead just like this old man? Hahahaha.”

Looking at Jeok Cheongang, who was laughing like an immortal, I thought:

*He’s really, really sulking.*

Could a person sulk this much?

At this point, he could have been named Forbes’ Most Sulky Person in the World and no one would have objected.

“I remember the day I first met you. Back then, this old man wasn’t in his right mind because of the infirmities of old age. That’s why they say that once you get old, you should just die…”

A suffocating pressure began to bear down on me.

As Jeok Cheongang charged ahead like a runaway locomotive, I finally managed to part my lips.

“What I said earlier was a joke. I couldn’t tell you because I was out of it, too. I needed some time to sort out my thoughts.”

“Hm.”

Jeok Cheongang’s eyes narrowed. Having recovered at least a little of his usual self, he asked gruffly,

“So the part about the Lord of Heaven was a joke, too?”

“That part is true. Unfortunately.”

“What proof do you have?”

I gave Jeok Cheongang a rough account of what had happened.

He had already heard a brief version of it when we were staying at the Nanman Beast Palace, but this time I went into far greater detail.

When I finished, Jeok Cheongang furrowed his brow.

“Those bastards tried to capture you?”

“Yes. But at some point, they must have decided that wouldn’t work, because they tried to kill me instead. The Great Snow Fiend and Black Hand Fist Demon, whom I fought at the Poisonblood Grounds, and the Southern Heaven Demon Empress, too.”

“Was their attempt to capture you an order from the Lord of Heaven?”

“That…”

I recalled what had happened for a moment before shaking my head.

“I don’t think so.”

“Why?”

“If the Lord of Heaven had truly given such an order, the Southern Heaven Demon Empress wouldn’t have tried to kill me, even if it meant meeting her end alone.”

“Loyalty that comes before one’s life… It’s almost impossible to believe.”

“It wasn’t simple loyalty.”

I answered quietly as I recalled everything about the Southern Heaven Demon Empress.

Her eyes at that moment. Her expression. Her voice buoyant with ecstasy, and everything she had said and done.

The emotion I had felt from her that day could not be expressed with the simple word *loyalty*.

It was…

“Fanaticism. To the Southern Heaven Demon Empress—or rather, to all of Dark Heaven—the Lord of Heaven is no different from a living god.”

“……!”

“Every member of Dark Heaven fears and reveres the Lord of Heaven. If he ordered them to capture me by any means necessary, then that order would be a divine command no one could disobey.”

The Blood Lord, who had been so powerful. The Western Heaven Demon Lord.

Even the Southern Heaven Demon Empress, who had met her end this time, had prostrated herself before the Lord of Heaven and claimed to be his servant.

Each of them was a monster capable of tearing apart an ordinary Supreme Peak master with their bare hands.

And the Lord of Heaven was the king and god whom those very monsters worshiped.

“I can’t be certain, but I think the Southern Heaven Demon Empress tried to capture me for one reason alone: because the Lord of Heaven had taken an interest in me.”

“Simply to earn the Lord of Heaven’s favor?”

I quietly nodded, and Jeok Cheongang muttered like a groan.

“A fanatic…”

His fading voice was swallowed by the wind.

Mounted on the back of the tiger, Jeok Cheongang silently watched the scenery rushing past us. Then he suddenly spoke.

“Have you ever seen a member of the Demonic Cult?”

“Do I look about sixty years old to you?”

“Yes. At your age, it would be natural that you hadn’t seen one. You were born long after the Great Faction War ended.”

“Why are you asking that when you already know?”

“I suddenly had a thought. Perhaps it would be better to fight the Demonic Cult of that era once more.”

“……!”

“Of course, they were fanatics, too. But the Heavenly Demon, their leader, was ultimately nothing more than a human being. The hundred thousand Demonic Path warriors beneath him knew that as well. To them, the Heavenly Demon was merely the Cult Leader guiding them—not a god.”

I understood what Jeok Cheongang was trying to say.

To the members of the Demonic Cult, the Heavenly Demon had been a human made of flesh and blood. But to every member of Dark Heaven, the Lord of Heaven was a god.

That was why they would fight for their god.

They would fight without fear of death. Even with countless blades and spears buried in their bodies, they would smile as they breathed their last.

“It will be the most terrible war in history.”

Jeok Cheongang continued, watching me with heavy eyes.

“Especially for you.”

“Because the Lord of Heaven is watching me?”

“Whether you wanted it or not, you have already drawn more attention than necessary. Even at this very moment, your name is probably echoing somewhere across the land.”

“……”

“The Three Saints and Ten Kings are old names. But you are different. You possess a talent without precedent throughout history, and no one in the world can deny that you became a master despite having only just passed the age of twenty.”

There was unmistakable pride in Jeok Cheongang’s gaze as he looked at me, along with a trace of unease.

“That is why the Lord of Heaven is watching you, too. And more importantly, he has already seen you once—your true nature and the infinite potential hidden within you.”

“……The underground prison of the Sichuan Tang Clan.”

“Yes. Using some unknown supernatural power, he saw you through the Western Heaven Demon Lord’s eyes.”

How could I forget?

The stone wall sprayed with blood, with stone dust raining down over my head.

And the words spoken by the Western Heaven Demon Lord as he stood tall and looked at me.

No—the words spoken by the Lord of Heaven, who had briefly borrowed the body of his servant.



*“Interesting. Very interesting.”*



He had definitely been smiling then.

Even as his entire body turned into a handful of ashes and scattered away, he had not forgotten to offer me one final greeting.



*“I’ll see you again.”*



Just remembering that day made my heart sink.

Jeok Cheongang silently watched me take a small, deep breath before speaking.

“Perhaps… the Lord of Heaven has an inkling of the secrets you have never told anyone.”

“……!”

“That is why I can no longer avoid asking you, either.”

In a world that had stopped as if someone had pressed a pause button, Jeok Cheongang slowly parted his lips.

“Can you tell this old man everything you’ve been hiding?”



* * *



Jeok Cheongang raised his head and looked at the sky.

The sky had poured down rain without pause for the past three days, but unlike his endlessly confused heart, it was blue and clear.

*The realm of immortals…*

The voice that had failed to escape scattered inside his mind. What else could he say? How was he supposed to understand it?

Despite having lived for an extraordinarily long time, all of it suddenly felt meaningless.

*If you were here, I could have steadied this confused heart in no time.*

Jeok Cheongang thought of the friend who had died several months earlier.

A man who loved alcohol and meat and was a sorry excuse for a monk, yet was called the Dharma King because he cared more deeply about people’s hearts than anyone.

But he soon shook his head.

The Dharma King was no longer of this world. And even if he had been alive, he would not have been able to look up at that blue sky and read the heavenly patterns.

*You said the heavenly patterns had already gone awry. That the sky no longer gave anyone any answers. You definitely said that.*

At the same time, the Dharma King had foretold a massive war.

He had said that a force capable of throwing even the heavens into confusion would spread across the world, becoming a blaze that swept in every direction.

But that was not all the Dharma King had foreseen.

*The Master of the Morning Star.*

A new star rising to illuminate the confused heavens.

The Dharma King had identified a young man as the Master of that Morning Star, and afterward Jeok Cheongang had gone to Mount Jiuhua and made that young man the successor to the Fire Gate Clan’s lineage.

“Hah… I thought he was nothing more than a drunken monk who enjoyed spouting nonsense.”

His mutter, mixed with a hollow laugh, scattered into the empty air. Jeok Cheongang stood silently as the cool breeze swept over his entire body, then suddenly shifted his gaze to the side.

A single beast was charging forward without pause.

And one person, strapped securely in place with thick leather straps, was sprawled facedown across the saddle.

No, not just any person.

Jeok Cheongang’s one and only Disciple.

*What an infuriating brat. He caused all this trouble, and now he’s sleeping like a baby.*

On the one hand, it was absurd. But after hearing a rough account from Jin Taekyung, Jeok Cheongang no longer had the strength to be surprised.

A completely different world, utterly removed from Murim. And a young man traveling back and forth between that place—one like the realm of immortals—and Murim.

*What an infuriating brat. He caused all this trouble, and now he’s sleeping like a baby.*

On the one hand, it was absurd. But after hearing a rough account from Jin Taekyung, Jeok Cheongang no longer had the strength to be surprised.

A completely different world, utterly removed from Murim. And a young man traveling back and forth between that place—one like the realm of immortals—and Murim.

Jeok Cheongang could not understand all of it, but he had already accepted that the unbelievable story he had heard was entirely true.

*Could this brat actually be some kind of Little Immortal?*

Just as he muttered the thought to himself, a long strand of drool hanging from Jin Taekyung’s mouth landed squarely on Jeok Cheongang’s cheek.

With a wet smack.

“……”

His fist tightened of its own accord.

But instead of punching his sleeping Disciple in the forehead, Jeok Cheongang sighed and adjusted the young man’s disordered posture.

*Yes. Sleep soundly. You’ve been through a lot.*

No. No, that wasn’t right.

Jeok Cheongang muttered in a voice quiet enough for only one person to hear.

“Have a safe journey.”
## Chapter artifact 726

# Chapter 726

> **System**
> - **Synchronization** begins.
> - 10, 9, 8, 7, 6…
> - **Logout** complete.

I opened my eyes to the familiar chime.

The first thing that entered my field of vision was an impossibly high ceiling.

Not a wooden ceiling that smelled of old, dry grass, but a pristine white ceiling made of solid alloy.

Amid that sense of dissonance that I could never quite get used to, I recalled my last memory in the modern world.

*The training room.*

That was right. This was the Peace Guild’s training room, a place only a very small number of people—including me—could enter.

I had left for Murim from this place, which was equipped with excellent security facilities and surveillance systems.

I had gone there immediately after finally finishing an important task I had put off after much consideration.

*Right. That’s what happened.*

Without saying a word, I stared at the ceiling.

My memories and senses of the days that had already passed had returned. Even so, I had not the slightest desire to get up.

Murim and the modern world. The modern world and Murim.

Falling into a brief state of listlessness every time I traveled between the two worlds was not unusual for me, but this time was especially bad.

*…I actually went and did it.*

I had imagined dozens of times what might happen if I revealed my secret to someone.

Of course, I had never once acted on those imaginings. And I shouldn’t have.

*Because it carried far too great a risk.*

But… it was also true that, somewhere in the back of my mind, I had thought that a day like this would come eventually.

I just hadn’t expected that day, which had always felt like a distant future, to be today.



*What did you say?*



The reaction Jeok Cheongang had shown when he first heard my confession was still vivid before my eyes.

He had not looked shocked or bewildered. No—he simply hadn’t understood it at all.



“What did you just say?”

“I said exactly what I meant. I came from somewhere much farther away than you think, Old Master.”

“Shanxi Province is pretty far from the Central Plains. But what does that have to do with your secret…?”

“Farther. Even farther than Nanman.”

“Farther than Nanman?”

“Yes. Far enough that you couldn’t reach it even if you walked your whole life.”

“You mean you have to take a boat?”

“No. It’s not that kind of concept. So… I suppose it would be more accurate to say that it’s a completely different world.”



A completely different world.

After hearing what came next, Jeok Cheongang fell silent for a long time and tried to understand my words in his own way.



“So what you’re saying is that you came from the realm of immortals.”

“…Uh. I suppose that’s one way of putting it.”

“Are you a Little Immortal?”

“I’m just an ordinary citizen.”



If Jeok Cheongang had been a modern person, we probably could have understood each other to some extent.

After all, it wasn’t as though someone from Murim entering a world where monsters and magic existed was inherently impossible to comprehend.

Of course, whether he would be sent to a psychiatric hospital or dragged into a laboratory afterward was another matter.

But to Jeok Cheongang, who had lived for over a hundred years in Murim, a world without even the internet, everything I told him could only sound confusing.



“If you fall asleep here, you go to the realm of immortals?”

“Not every time, but aside from special circumstances, yes.”

“And when you stay in the realm of immortals and try to return…”

“It’s the same. Each time, time in the other world flows extremely slowly.”

“…Damn it.”



After a brutal struggle in which he clung to common sense and reason with both hands, Jeok Cheongang finally reached one conclusion.



“Damn it. I don’t understand.”

“What?”

“No matter how much I hear, I don’t understand.”



There were truths in this world that could not be understood even after seeing them with both eyes and hearing them with both ears.

Everything Jeok Cheongang had heard from me was like that.

And yet, even amid all that confusion, there was one fact that remained unchanged.



“But the name of the idiot this old man is looking at right now is Jin Taekyung. Not some Little Immortal descended from the realm of immortals, but Blazing Flame Divine Dragon Jin Taekyung.”

“……!”

“That alone is enough.”



I hadn’t understood it back then.

Why my throat had closed the moment I heard those words. Why I had to grit my teeth to hold back something hot surging up from my chest.

But… yes. Just as Jeok Cheongang had said, that alone was enough for me, too.

And now, I thought I could understand why.

I had been afraid.

I had been afraid that my existence might be denied in another world that had already become part of my life.

*What am I, a child?*

A hollow laugh escaped me.

At the same time, the boulder that had been pressing down on one corner of my heart vanished, and everything felt completely liberating.

*Right. This is enough. At least for now.*

When had I ever lived with an eye toward the future?

Each day, each moment, I chose the path I had to walk—and that was how I had made it this far.

And the path I had chosen today was as wide and warm as a summer beach.



* * *



I had seen it on television before.

Athletes each had their own routines.

One soccer player apparently stepped onto the field with his left foot first, while a famous Major League batter spat out a sunflower seed every time he swung his bat.

To an ordinary person, it might seem ridiculous to make such a fuss over something so insignificant. But everyone had superstitions related to peace of mind and good luck.

And the profession more meticulous about routines and superstitions than any other was that of a Hunter.

Losing a soccer game did not make the sky fall.

Striking out on three pitches with the bases loaded and a chance to come from behind did not make the earth collapse.

But Hunters could die on the spot if luck turned against them.

There would be no next game for them, no next at-bat.

They would simply remember their entire life and their family’s faces just before their final breath, and think:

*Fuck, I should’ve worn blue underwear today.*

It sounded like a joke, but it was a true story.

Those were also the last words of an A-rank Hunter who died in a Gate at the height of his popularity a few years ago.

*Or was it red underwear?*

I had been too busy working myself to death at the time, so my memory was hazy. Anyway.

The important point was that I, too, had a routine I had followed with absolute precision until now—and that routine had just been broken.

Bang!

The door flew open as though it had exploded.

The lock I had installed as a precaution was destroyed. Fortunately, I had finished all my preparations one step ahead of time, so I did my best to remain calm as I welcomed the unwelcome guest.

“Well, well. You don’t even knock anymore before barging in.”

Huff. Hah.

Ragged breaths, sweat beading on his forehead, and a disheveled suit.

Looking at the unwelcome guest, I continued,

“Team Leader Choi.”

Normally, he would have been a welcome sight.

But right now, I had the urge to punch that handsome face.

However, Team Leader Choi—who now officially had to be called the Guild Master—failed to notice my displeasure.

No, it would be more accurate to say that he did not have the time to notice it.

“Huff. Hoo.”

What, had a Demon King been chasing him?

Team Leader Choi, who could now hold his own against any Peak master in the Central Plains, finally managed to catch his breath. Then he thrust out the thing in his hand and shouted,

“What is this? What the hell is this?”

“If you don’t have anything important to say, come back a little later… Ah. That?”

“That? You mean *that*? Is this really something you can just dismiss that easily?”

Rage button: ON.

As Team Leader Choi nearly collapsed over my casual reply, I realized that I would have to break an essential routine I had followed every single day since graduating from Hunter training.

And I also realized that there was no way to avoid explaining that “thing” right now.

“Calm down. Calm down. I’ll tell you everything, so put that down first. Oh, and what would you like to drink?”

“Mr. Jin Taekyung. What you drink isn’t important right n—”

“I’ll just make you coffee. What was it again? That tiger-poop coffee you gave me last time to celebrate the opening of the office.”

“Huh.”

“Is that okay?”

Team Leader Choi stared at me with a mixture of shock and disbelief before collapsing onto the sofa.

His trembling hand held a bundle of papers covered in handwriting I had written myself.

**[The Smiling Mana Cultivation Method]**

It was still a masterpiece of calligraphy.



* * *



Team Leader Choi was definitely a rich kid.

Until a moment ago, he had been snorting like a Minotaur with its horns ripped out. But the moment he smelled the rich aroma of coffee, he regained his composure.

I found myself sniffing the air as well.

“Does tiger-poop coffee have some kind of calming effect? Or is it just one of Team Leader Choi’s routines?”

Team Leader Choi answered my question in a cold voice.

“It isn’t tiger. It’s cat. A civet cat.”

“Tiger or cat, whatever.”

“And rather than poop, please say feces. The word ‘secretion’ is also available.”

“Poop.”

“Feces. Or secretion.”

“Yes. So, poop.”

“Unless you’ve forgotten, it will be dinnertime soon. If you keep saying ‘poop’ to someone’s face like that…”

“Poop.”

“……”

As the mood grew increasingly shitty, Team Leader Choi was the first to back down.

“Fine. That isn’t important right now.”

“Mm.”

Now that I thought about it, I had sounded like a complete moron.

Deeply ashamed, I calmed my prickly mood.

It was true that Team Leader Choi had caused me to break a routine I absolutely had to maintain. But when I thought about it, I was also the one who had given him a reason to do so.

**[The Smiling Mana Cultivation Method]**

Anyone who saw something like this would have run over immediately, not just Team Leader Choi.

Even if that person had been the President of the United States, it would not have changed the fact.

“Given the gravity of the matter, I’ll ask directly.”

His voice trembled slightly.

Team Leader Choi stared at me and slowly continued,

“This… No, this mana cultivation method. Where did it come from?”

I answered without hesitation.

“Who else could it be? The person sitting across from you right now.”

“……!”

“I made it myself. From beginning to end.”

A suffocating silence descended.

Team Leader Choi stared at me without a word, his eyes trembling, then exhaled the breath he had been holding.

“Hoo.”

“Why are you so surprised? Didn’t the errand boy I sent explain it to you?”

Of course, he was not merely an errand boy.

Even if he was slightly unhinged, the Skeleton King was a powerful named monster and, at the same time, a hidden S-rank Hunter working in secret for the Peace Guild.

*On top of that, he was unquestionably trustworthy.*

Team Leader Choi knew that better than anyone, and he let out a quiet laugh.

“He was a little excessive for an errand boy.”

“That’s why I entrusted it to him. I was originally going to give it to you myself, but you happened not to be there.”

“…I had somewhere to stop by.”

Team Leader Choi said no more, and I did not bother asking where he had been.

Two months ago, someone had suddenly left everyone’s side.

There was still a lingering warmth in that empty place, like the coffee cup before us that Team Leader Choi had not taken a single sip from.

“I heard what you told Skeleton King. No, Mr. King. But I’m sorry to say…”

“From your position, you had to confirm it at least once.”

“Yes. But the moment I saw what was inside, even before hearing an explanation, I knew. Jin Taekyung is the only person in the entire world who could have created a mana cultivation method like this.”

At Team Leader Choi’s praise, I awkwardly scratched the back of my head.

“Come on, it wasn’t that big a deal. It’s true that I thought hard and worked hard to make it something even beginners could learn, but…”

“There aren’t many S-rank Hunters with handwriting this terrible. And there certainly aren’t many with naming sense like this.”

“What?”

“But someone who can accomplish both at the same time? There’s no need to think any further.”

“……”

“Thanks to this, I was able to realize one thing. This mana cultivation method could only have been born through the hands of one person—Jin Taekyung.”

“……”

I silently looked back and forth between Team Leader Choi’s face, filled with certainty, and **[The Smiling Mana Cultivation Method]** lying on the table.

Then I thought:

*What the fucking hell.*

Mana cultivation method or not, I felt like tearing the whole thing to shreds.
## Chapter artifact 727

# Chapter 727

Should I tear it up or not?

Looking at Jin Taekyung, whose thoughts were written plainly across his face, Choi Minwoo let out a faint, incredulous laugh inwardly.

*I really can’t figure him out.*

Everything about his usual words, actions, and thoughts was absurdly simple.

But some of the sides Jin Taekyung occasionally showed were astonishing—so astonishing they bordered on shocking.

*It would be strange to be surprised by him anymore, but even so, this is really…*

Choi Minwoo’s gaze settled on the table.

**[The Smiling Mana Cultivation Method]**

The crooked handwriting looked like it had been written by a child, and the title was downright ridiculous.

But unlike its title, the contents of those roughly ten sheets of A4 paper were anything but ridiculous.

*He actually created an entirely new mana cultivation method.*

There was a simple reason Choi Minwoo had teased Jin Taekyung earlier, even going so far as to point out his terrible handwriting.

It was a small act of revenge for suddenly handing over something this absurd without saying a word.

The shock Choi Minwoo had experienced a few hours ago had been that immense.

*How is this even possible?*

The explanations and methods were simpler and clearer than anything he had ever seen. The mana cultivation method was exceptionally stable and faithful to the fundamentals.

And Choi Minwoo, who had by now become someone whose skill was not inferior even when compared to a Peak master of Murim, had immediately recognized the true value of this new mana cultivation method.

He also understood what the series of events that had drawn the world’s attention only a short while ago had meant to Jin Taekyung.

“The Week of Judgment.”

Breaking the brief silence, Choi Minwoo continued while staring at Jin Taekyung.

“‘Just as God created heaven and earth over the course of a week, terrorists around the world went through a Week of Judgment.’ That’s what President Doramp Jr. said during a White House press conference a few days ago.”

It had been said publicly by none other than the President of the United States.

Naturally, his outrageous words and actions had spread far and wide in less than an hour. Now that some time had passed, there was no one in Korea who did not know about them.

Probably with one exception.

“That guy said that?”

At Jin Taekyung’s question—he had been holed up in the training room the entire time—Choi Minwoo nodded.

“It was quite an aggressive statement for the president of a country, especially the United States. Some people criticized him for deliberately provoking the terrorists.”

“Hm. Why bring up something as grand as creating heaven and earth? What about retaliatory terrorism?”

“None. Not a single incident.”

“Not a single one?”

“Yes. If anything, they’ve even been keeping their mouths shut.”

The sullen expression that had remained on Jin Taekyung’s face softened slightly.

“Looks like beating the crap out of them was worth it.”

It was at that exact moment that Choi Minwoo, who had been gazing pensively at Jin Taekyung, suddenly spoke.

“So that was why.”

“Why what?”

“I thought about two things. Why you suddenly suppressed the terrorists. And what it meant that you gave me this new mana cultivation method.”

And then the answer appeared.

**[The Smiling Mana Cultivation Method]**

Lifting the papers bound together with a single staple—an object in which not even the slightest trace of effort could be found—Choi Minwoo continued.

“You intend to make this mana cultivation method public. To everyone.”

Jin Taekyung grinned.

“Our Team Leader Choi really is sharp.”

* * *

At that moment, Team Leader Choi’s expression as he looked at me was strange.

He seemed impressed, but at the same time, he also seemed to have a lot on his mind.

“Why? Is there a problem?”

“Well…”

Team Leader Choi ran a hand through his disheveled hair.

“There are too many problems. I don’t even know which one to mention first.”

“There’s nothing wrong with the mana cultivation method I made, so I assume you mean practical problems.”

“…Yes. Unfortunately, that’s right.”

“Which one is the biggest problem?”

After thinking for a moment, Team Leader Choi opened his mouth.

“To begin with, making this mana cultivation method public would itself be the first problem.”

“Go on.”

“You know very well that mana cultivation methods are a kind of know-how and secret art possessed by only a tiny minority of high-ranking Hunters. You also know how closed-off they are, and how different the world they belong to is from that of ordinary Hunters.”

“I know. I’ve been in this business for years. Of course, back when I was an F-rank Hunter, I’d never even heard of mana cultivation methods.”

No profession in the world had a wider gap between its members than that of a Hunter.

If ordinary people in society distinguished one another based on education, family background, and appearance, Hunters were divided into high and low solely according to rank.

How much mana they had been granted. How agile and strong they were. They were selected according to such primitive standards, then assigned ranks like cattle being marked for slaughter.

*There’s a reason they call F-rank Hunters slaves.*

High-ranking Hunters, on the other hand, were practically beings who lived above the clouds.

They made more money from a single raid than most Hunters could earn in a lifetime, and lived beneath envious gazes and the glare of the spotlight.

That was probably why.

Just as the nobles of the past had built castles and lived inside them, high-ranking Hunters had built walls meant only for themselves.

Walls no one but another high-ranking Hunter could cross.

Even if someone was lucky enough to receive a high rank, the door would open only with their permission.

Connected by invisible threads, those high-ranking Hunters were scattered across the world, each receiving the protection of the giant Guilds they belonged to.

“This isn’t a problem limited to Korea. If you reveal this mana cultivation method to the world, there will be far greater opposition than you expect.”

“Because they’ll think that if we release a mana cultivation method, the value of the ones they possess will drop?”

“That’s part of it, but there’s another reason.”

“What is it?”

“The problem is that it’s *us*.”

“……!”

It was a short answer, but I immediately understood what he meant.

*Have we stood out too much all this time?*

I suddenly remembered the conversation I’d had with Jeok Cheongang just before Logout.

His words about how, whether I had wanted it or not, I had already drawn far more attention than necessary.

The spotlight was bright. But everything around it was dark.

The line I had read in a novel I liked back in school had been right. The brighter I became, the deeper the darkness surrounding me grew.

In Murim. And in the modern world.

“Team Leader Choi, by any chance…?”

Realizing what I was asking, Team Leader Choi shook his head.

“There’s no major problem yet, but… invisible pressure is being brought to bear on us. That’s why we’ve temporarily put the establishment of additional overseas branches on hold.”

“That serious?”

“Every major Guild in the world is watching us right now. Even if they don’t stage a show of force, if they make a move somehow, the situation won’t be easy for us either.”

“Then why didn’t you tell me?”

Team Leader Choi answered with a stern expression.

“Did you give me a chance to tell you?”

“…That’s fair.”

Still, this place was a complete mess too.

People who already possessed a great deal naturally disliked seeing the world change.

The tiny minority of Hunters who had learned their own mana cultivation methods were no exception.

*No. At this point, it would be more accurate to call them power brokers than Hunters.*

Power brokers who might even be able to manipulate an entire country.

With their enormous wealth, fame, and overwhelming strength, they overturned even common sense. They wanted no further change. They did not want another power to appear that could stand alongside them.

People like me and Team Leader Choi, for example.

*Even so, these bastards seem worse than the Murim sects.*

They said that Murim sects would chase someone down with murder in their eyes and smash his head if their unique martial arts were leaked, but at least they wouldn’t throw a fit at a merchant for selling the Three Calamities Sword Technique in a marketplace.

But these bastards already had more than enough, and they were still ready to cause a scene because we wanted to release one little mana cultivation method?

*Huh? Now I’m pissed.*

“If we release this mana cultivation method, they’ll make a huge fuss, right?”

“Yes. And it’ll be chaos for us too.”

“Then what if I go after them?”

“What?”

“Now that I think about it, it’s fucking ridiculous. Let’s just release the mana cultivation method without overthinking it, and then go after the assholes who start making trouble. That should shut them up…”

“No! Don’t! Absolutely not!”

For Team Leader Choi’s normally low, composed voice to reach that many decibels meant one thing:

*You’ll have to walk over my corpse first, you lunatic.*

But this time, I couldn’t easily agree with him.

“I understand what you mean, Team Leader Choi, but we have to make this public. I didn’t create it so I could keep it to myself like a diary.”

The world’s mana had already increased. No—it was continuing to increase even at this very moment.

As a result, mutation Gates were appearing one after another, and now even monster waves were occurring.

“Monsters are growing stronger as the mana increases. You know that too, Team Leader. But if people learn about this mana cultivation method under the current circumstances…”

“The overall level of Hunters will rise. It’s stable enough that even the lowest-grade Hunters can learn it without difficulty.”

Team Leader Choi continued with a solemn expression.

“I understand what you’re thinking, Mr. Jin. Wasn’t that why you suppressed the various rebel groups and terrorists in the first place—to reduce the possibility of the mana cultivation method being misused as much as possible?”

“Yes. I had to consider whose hands the weapon I created would fall into before considering how sharp it was.”

About two weeks ago by modern-world time, an incident in Texas, United States, had given me a serious warning.

A terrorist attack using a Magic Gem.

Fortunately, the terrorists’ attempt had ended in failure, and there had been no casualties. But that incident had made me realize something for certain.

“When I said *everyone*, I realized that I was including all kinds of criminals and lunatics.”

Afterward, I followed Magic Johnson to the Pentagon and obtained information about them with the tacit approval of the President of the United States. Alongside the people who had come with me, I dyed the desert red with blood and cut away every element that might become a threat.

Rebel groups that trained kidnapped children in firearms. Fanatical terrorists who were willing to commit even suicide attacks…

I killed anyone who stood in the way, and the dead were bound to the Skeleton King’s undead army, which chased after those who fled.

At the same time, I issued false orders to those in distant locations through their captured leaders.

I ordered the rebel groups to attack the terrorist organizations, and the terrorist organizations to attack the rebel groups.

It was a war between bastards and motherfuckers, and after being duped by those false orders into launching all-out attacks against each other, both sides paid the price in massive losses—enough to leave them grievously wounded.

“As you know, Team Leader Choi, completely uprooting them won’t be possible this time or in the future, but we’ve already achieved our objective under the current circumstances. Even if those bastards learn this mana cultivation method, they won’t be as much of a threat as before.”

The only ones who would grow stronger through the mana cultivation method I created were not those bastards.

The overall level of Hunters would rise enough for them to respond to the monsters strengthened by the increase in mana, and that would allow us to maintain the balance.

*If the situation gets much worse than it is now…*

At that point, I intended to reveal even the Jin Family’s Cultivation Technique, which I had so far shared with only a tiny handful of people, including Team Leader Choi.

The low-ranking Hunters who knew absolutely nothing about mana cultivation methods would not be able to apply the Jin Family’s Cultivation Technique even if I handed it to them right now. But once they had learned the method, they would be able to cultivate it on their own.

I looked straight at Team Leader Choi and opened my mouth.

“We have to make it public, one way or another.”

“……”

“Fortunately, it isn’t too late yet. Public opinion and interest toward you and me are still fairly favorable.”

In fact, they were more than favorable. They were fervent.

I was being called a young hero born from the new age, while Team Leader Choi had succeeded Butler Kim, who had passed away, and taken over as Guild Master of the Peace Guild. Before the freshly made plaque had even had time to cool, he had also taken control of the Ares Guild.

On top of that, he had a more glorious halo than anyone else’s.

He was the sole blood relative and heir of Cheon Taemin, the savior who had rescued humanity from the Demon King Asmodeus.

Grab.

“Team Leader Choi.”

My hand tightened around his. When Team Leader Choi met my burning gaze, he flinched as though he had been burned.

“W-Why are you suddenly doing this?”

His reaction was almost as if he had run into Magic Johnson in a dark alley at night. But I didn’t back down and continued speaking firmly.

“If you’re really that worried, let’s try another way. Okay?”

“And what way would that be…?”

“Put your maternal grandfather’s name to work for us just this once.”

“What?”

“Come on. Let’s ride the Savior coin just once while we’re at it.”

“……!”
## Chapter artifact 728

# Chapter 728

Humans are all the same.

When success keeps coming, their confidence grows, and they inevitably begin quietly closing the eyes and ears they once kept wide open.

But before being an excellent Hunter and manager, Team Leader Choi was also a pretty decent person on a human level.

Even more so because, despite holding the decision-making authority himself, he always asked for everyone's understanding.

“……That’s why I’d like to hear everyone’s opinions.”

When Team Leader Choi finished speaking in a low voice, the people sitting on the sofa fell silent for a moment.

No, to be precise, it wasn’t *people*. At some point, a monster had naturally claimed a seat among them.

And that monster’s face was more solemn than ever.

“This body is opposed.”

Every gaze turned toward him at the firm refusal, delivered without a hint of hesitation.

But the Skeleton King continued without a care.

“The reason is obvious to everyone here. Excessive expansion of one’s forces is bound to attract suspicion, and human envy and jealousy can only invite danger. Am I wrong?”

I’d been thinking it for a while, but this bastard had really become just like a person.

When I awkwardly shook my head, the Skeleton King’s voice gained even more force.

“This body would also like to avoid attracting any more attention. If other humans learn my true identity, you will be in trouble as well. So stop spouting foolishness.”

The speech ended with that stern denunciation. Everyone, myself included, looked at one another as if we had made a pact.

He did have a point.

He definitely had a point, but…

“The bastard who wants to avoid attention made an SNS account the moment he got a phone?”

At my sharp retort, Team Leader Choi, Im Kkeokjeong, and Song Song nodded one after another.

“I agree with what Mr. Jin Taekyung said.”

“That’s true. I don’t use that sort of thing, so I didn’t know, but this fellow seems to be pretty famous.”

“Not just pretty famous. He hasn’t even had the account for very long, and he already has more than a hundred thousand followers.”

The Skeleton King, who had faltered after being struck in the heart of the matter, thrust out his chest at Song Song’s words.

“As of today, it is one hundred and twenty thousand.”

“Really?”

“Of course. Advertising offers are pouring in from every direction.”

I let out a hollow laugh as I watched him bask in his pride.

“You fucking bastard. Do you want me to split you into a hundred and twenty thousand pieces of bone?”

“……”

“Delete the account right now. This is your final warning.”

After hesitating for a moment at my threat, the Skeleton King answered in a depressed voice.

“……Understood.”

“At least you’re obedient. But you didn’t post any strange nonsense on SNS, did you?”

The reach of the internet in modern society was truly staggering.

Unlike the Murim, where people had to send messenger pigeons, wasn’t the standard around here for something to spread across the entire world with just a few movements of one’s fingers?

*It’ll be a pain in the ass if that bastard left some shit on there.*

And in response to my well-founded concern, Song Song casually cut in.

“Fortunately, there’s nothing much. I looked through everything just in case, and he’s only posted a ton of pictures of his own face.”

“Really?”

“Yeah. And most of his followers are from overseas. Men make up an overwhelming majority of them, too.”

“That’s a relief, but why are so many men following him—ah.”

An insight flashed through my mind.

I remembered whose hands had created the Skeleton King’s handsome face.

*Magic Johnson.*

The Grand Mage of the century. And the century’s gayest man.

The Skeleton King as he currently existed was the result of Magic Johnson’s taste being thoroughly reflected in his work—the very Magic Johnson who had performed unbelievable magic with two staffs.

He was handsome at a glance, but his face and physique were especially perfect for satisfying the needs of people in a certain niche.

And there were no fewer than a hundred and twenty thousand of them.

That was enough people to kick the asses of a hundred thousand practitioners of the Demonic Path, even if they came swarming back. Of course, I had to wonder whether kicking was all they would do.

*This guy was more impressive than I thought.*

To draw in that many followers in such a short time despite having no known name or face. Even the Murim Alliance Leader couldn’t do that.

Unaware of the way I was looking at him, the Skeleton King fiddled with his smartphone before opening his mouth with a mournful expression.

“I cannot bring myself to delete the account. You are the most wicked and cruel human in the world.”

“What crime did I commit in my previous life to deserve being called cruel by a monster bastard?”

“Ah, such a sudden parting. Some nameless woman who can no longer gaze upon this body’s dazzling face will surely shed endless tears.”

“……”

“What is with that strange expression?”

“Nothing. It’s better if you don’t know.”

Sometimes, the truth was more beautiful when left unrevealed.

After reaching a tacit agreement with Song Song through an exchange of glances, I looked around and spoke.

“Anyway, everyone agrees, right?”

Im Kkeokjeong nodded as though it were obvious.

“Well, if you and Team Leader Choi decided that’s what you’re going to do, I’ll follow along.”

“Song-i, what about you?”

“Hmm.”

Song Song crossed her legs at an angle and continued.

“From what I’ve heard, it’s ultimately something we’re doing for everyone. If I say I don’t want to, doesn’t that make me the only bitch here?”

“No.”

“Really?”

“Yeah. You were never particularly nice to begin with.”

“Oh, listen to this bastard.”

Song Song smiled sweetly and raised her middle finger before suddenly sighing.

“What a spectacle. When Team Leader Choi first offered me a transfer and I left the Ares Guild, I never imagined things would turn out like this.”

“You should’ve just stayed there.”

“Hey, I couldn’t. The Branch Leader was such a pervert that there was no way I could stay. I figured it would be better to work under someone young, handsome, and rich. But I had a bad feeling from the very first day, didn’t I?”

“The first day?”

“Yeah. I came here to get away from a pervert, but there was another weird bastard waiting for me. I was starving to death, and he burned every piece of meat he cooked. Then he suddenly announced that his zodiac sign was Taurus. Wasn’t he completely insane?”

“Ah-ha.”

I let out a short laugh and looked at her without saying anything else.

To be honest, I did feel sorry for Im Kkeokjeong and Song Song. Ever since the Peace Guild was founded, they had been forced to endure all sorts of turmoil they had never wanted.

“Hmm.”

“What’s with that reaction?”

“Nothing. I just wanted to tell you that it isn’t too late yet.”

“What?”

“This may be far more dangerous than you or Uncle Kkeokjeong think.”

Unlike usual, my voice held no trace of laughter. Song Song’s eyes grew serious.

“How dangerous are we talking?”

“We have to consider this beyond a domestic scale now.”

“You seem to have a tendency to underestimate yourself. You and Team Leader Choi left Korea behind a long time ago.”

That was an entirely accurate statement.

Ever since I took down the Arch Lich in China, my name had become known throughout the world. Meanwhile, Team Leader Choi had appeared in the media as the new City Lord of the Ares Guild and the successor to the living Savior.

But this was a different matter.

No, it was a problem created by everything we had achieved until now.

I shrugged.

“Someone once said that the bigger you get, the more there is to take a bite out of.”

“So how much are you planning to let people take from you?”

“I have no plans to let that happen. And I intend to keep it that way.”

Song Song stared at me for a moment before suddenly speaking.

“Do you know something?”

“What?”

“It’s already far too late for us to pull out. For both me and Uncle Kkeokjeong.”

Im Kkeokjeong quietly added to her words.

“I never intended to pull out in the first place.”

“Uncle.”

“Whether it’s too late or not doesn’t matter. Once you start something, you have to see it through to the end. At least for the sake of the one who left us first.”

“……!”

“Isn’t that right, Team Leader Choi?”

At Im Kkeokjeong’s quiet question, everyone’s gazes turned in one direction.

Team Leader Choi had fallen silent at some point. He was looking at the empty seat of someone who had been there.

A seat that had still held warmth until not long ago. The empty place left by someone who could no longer be replaced by anything.

Then he opened his mouth.

“I visited the grave today. Someone had carved words beside the gravestone. ‘Thank you for coming. I love you. Please come again.’”

No one said a word, and Team Leader Choi continued calmly.

“So next time, I’d like all of us to go visit that person together. Next year, the year after that……and even decades from now.”

It was the resolve of a man who had been forced to send someone precious on ahead.

The four words *all of us together* carried his determination not to let the same thing happen again.

*Decades from now.*

Yes. That was enough.

I didn’t know what we would look like then, but for now, the fact that we would move forward together was enough.

“Team Leader Choi.”

At my quiet call, he gave a heavy nod.

“Understood. Let’s begin.”

We had already worked out the broad strokes beforehand. Team Leader Choi took out his smartphone and called the first person.

Beep. Beep. Click.

The call connected before even three rings had sounded. A deep voice, honed by a hectic political life, came from the other end.

—You’ve reached me. This is Baek Hanseong.

There were plenty of people named Baek Hanseong in Korea. But in a situation like this, there was only one Baek Hanseong Team Leader Choi would contact first.

“Yes, Mr. President. I’m calling about something important.”

—Ha-ha. Well, putting it that way already makes me feel a little strange. I’m looking forward to it, but at the same time, I’m starting to feel uneasy.

At the appearance of a major figure who moved an entire country, Im Kkeokjeong and Song Song fell silent. The Skeleton King’s eyes widened as he whispered to me.

“If you mean President Baek Hanseong, then could it be that—”

“That’s right. Our country’s pres—”

“I know. Isn’t he the popular celebrity with more than ten million followers?”

“……”

“Damn it. A human has a hundred times this body’s following.”

As I watched the Skeleton King vent his frustration, I thought:

*Please just fucking die already…….*

Come to think of it, he already had.

* * *

The hallway was bright enough to dazzle the eyes. An A-rank Magic Gem filled with tremendous energy continuously supplied power to the entire building, while people filling every floor bustled about with their respective work.

At least, that was how things had been until sudden darkness descended.

Crackle. Whoooosh.

The light flowing from the ceiling lamps faded, and every machine stopped moving.

Confused shouts erupted from all around, shattering the momentary silence.

“What the hell is this?”

“Uh, it looks like a power outage.”

“Is that supposed to be an answer? No, fuck…… This is why I said we should replace the Magic Gem ahead of time. After sticking a straw in it and sucking it dry for more than twenty years, isn’t it practically begging us to put it out of its misery?”

“That’s what I thought, too. The experts said an A-rank Magic Gem would last at least thirty years.”

“So what, does it matter why the Magic Gem ran out ten years early? Are you so curious you’re about to go insane?”

“N-No, sir.”

“Enough. Everyone, focus! The Security Team and Technical Team will be here within two minutes, so don’t move a finger—stay exactly where you are! Anyone with spare mana lanterns, go get them right now.”

But despite the department head’s shout, the entire building lit up again before even a minute had passed. The power had returned.

“Damn it. They’ve got us running around in circles……”

The department head grumbled before waving away the Security Team, who had arrived a step too late.

“Ah, as you can see, everything’s fine. What caused the sudden outage?”

“I asked our team leader, too, and apparently it happens once every few years, although it’s rare. The Technical Team will have to investigate to find the exact cause.”

“Well, I suppose that’s their department.”

The Security Team Hunter gave an awkward smile and checked several things.

Whether anything had gone missing during the blackout. Whether anyone had been injured. Whether anyone had noticed anything suspicious during the incident, and so on.

But it was little more than a simple procedure, and there were mountains of work waiting to be handled. No one had the time or energy to devote to a blackout that had lasted barely a minute.

“Sorry, but if you have anything else to ask, can’t you do it later? Things are a little hectic for us right now.”

The Security Team employee nodded at the department head’s words.

“That shouldn’t be a problem. But you’re all much busier than usual. Did something happen?”

“A notice came down from above. Apparently, something big is going to happen sometime today.”

“Something big?”

“Yeah. We don’t know the details either, but it seems to have come down from the Blue House. Everyone’s on high alert because of it. At this rate, there’s no chance we’ll be leaving on time.”

“Oh dear. I took up your time for nothing.”

“It’s not that serious. We’re all working for the country, after all. Take care, and I’ll see you later.”

“Yes, you too.”

But as they returned to their respective positions, none of them knew.

During that short span of less than a minute, some ghostlike entity had moved through every part of the building, riding the thick darkness.

And that one item had disappeared from the evidence storage room deep underground.

The hundreds of employees going about their work, the highly skilled Hunters of the Security Team, and even the alarm magic had failed to notice.

The entity that had completed everything with ease leisurely slipped out of the building.

Step. Step.

Along with someone’s footsteps.

“Sehwan, did you check the third floor?”

“Yes, Team Leader. There were no problems. What did the Technical Team say?”

“It hasn’t even been ten minutes. Do you really think they’ve already found the cause?”

“That’s true. By the way, isn’t the weather really nice today?”

Sssrk.

A dark shadow stirred faintly behind the Security Team employee as he chatted idly with his superior.
## Chapter artifact 729

# Chapter 729

I had never gone fishing in my life, and I didn’t know how to do it.

But I did know how to catch more fish.

*Bait.*

That was what we needed.

Scatter bait about the major announcement in every direction and draw in as much interest and attention from as many fish—or rather, people—as possible.

Of course, the process required a little persuasion, too.

Team Leader Choi and I weren’t aiming merely to fill the bucket we’d brought. We wanted a boatload so enormous it would spill over.

But to make that dream a reality, we needed excellent sailors, and the first person Team Leader Choi contacted was President Baek Hanseong.

“Pardon?”

He had gone through every kind of hardship before entering the Blue House at the age of just over forty. His eyes widened at the words *Mana Cultivation Method*, and when the name of one particular person followed, he spilled his coffee.

“I-Is that true? Did he really…?”

“Yes. My maternal grandfather created it himself. He wanted to share this Mana Cultivation Method with everyone.”

“H-How can this be?”

Who was Cheon Taemin?

A living Savior and a hero who had accomplished something unmatched in human history.

Everyone had no choice but to show respect before the name of the Slayer—the man who had defeated the Demon King Asmodeus and brought the Great Cataclysm to an end.

“But why is the Mana Cultivation Method called *Smiling*…?”

“……I took out the wrong one. Please forget what you just saw.”

To be perfectly honest, if I became known as its creator, I wouldn’t care whether the Mana Cultivation Method was called *Smiling* or *As-Salamu Alaykum*.

But since the name Cheon Taemin was attached to it, Team Leader Choi and I agreed that *The Smiling Mana Cultivation Method* was a problem.

“This is the Mana Cultivation Method my maternal grandfather created.”

What Team Leader Choi placed on the table was a neatly bound booklet. Its cover bore the Mana Cultivation Method’s new name.

“*Heaven and Earth Cultivation Technique*……”

“The Heaven and Earth Cultivation Technique is versatile enough for even the lowest-ranking Hunter to learn, and it is also exceptionally safe. It may be difficult to see tremendous effects immediately after learning it, but it will certainly be of great help to Hunters.”

Of course it would. That was what I had made it for.

The name had changed because of adult circumstances, but I had come up with the new name, too.

Feeling a little proud, I added:

“In short, it’s a fucking incredible Mana Cultivation Method.”

Team Leader Choi gave me a pointed cough, but President Baek Hanseong didn’t pay any attention.

No, it would be more accurate to say that he didn’t even have the time to pay attention.

He stared as though possessed at the booklet containing the principles of the Heaven and Earth Cultivation Technique. Only after a long while did he finally come to his senses.

“But why would you bring something this important to me…?”

“We need an ally.”

The phoenix chair wasn’t something President Baek Hanseong had bought used on Oi Market.

He immediately realized why Team Leader Choi and I had come to see him.

“You want a breakwater.”

“We only hope that we can be of strength to each other.”

“But no matter how large a Guild steps forward, it will be difficult as long as he is still here.”

It was an accurate assessment.

Assuming it was true.

*Unfortunately, it isn’t.*

Avoiding interference from outside as much as possible.

That was why we were planning to reveal the Smiling—or rather, the Heaven and Earth Cultivation Technique while borrowing the name of the unconscious Cheon Taemin. Team Leader Choi had no intention of telling the truth even to President Baek Hanseong, who had always shown us a very favorable attitude.

He was a politician, after all.

“Neither I nor my maternal grandfather want any conflict or controversy. To prevent that, we need the government’s cooperation.”

“Are you saying that the Blue House may directly announce the existence of this Mana Cultivation Method?”

Team Leader Choi shook his head.

“It should be enough to announce that there has been cooperation between both sides and that a major announcement will be made in two days. That alone will draw the public’s attention.”

“So you want me to drum up interest……”

“This Mana Cultivation Method’s release will be announced as a sort of national project. If that happens, Korea’s standing will rise as well.”

“Hmm.”

The unprecedented public release of a Mana Cultivation Method. And the name Korea, which would forever accompany this historic event, along with the President’s achievement.

A faint smile appeared around President Baek Hanseong’s lips.

“That Korean flag looks especially beautiful today.”

Someone once said that the most powerful drug in the world was a patriotic high.

*Flap—*

* * *

Cheon Taemin. The public release of the Mana Cultivation Method. A national project.

Those three keywords boiled like a cauldron over charcoal, and their ignition point was none other than Korea.

> “My beloved and respected citizens. I stand before you today to make one major announcement……”

President Baek Hanseong demonstrated his promise to cooperate fully with an emergency official Blue House press conference.

His passionate speech before countless reporters and cameras, including foreign press, was broadcast live on television. Before long, it was transmitted across the world and caused an enormous upheaval.

> [The Mana Cultivation Method Made Public—An Unprecedented Event!]

> [The Savior of Humanity Saves the World Once Again!]

> [The Living Legend Finally Preparing to Reveal Himself?]

The mere mention of Cheon Taemin, who had stayed out of the public eye for so long, was already enough to make headlines. And now the Mana Cultivation Method he had created was going to be revealed to the entire world.

The response was explosive.

No, the media had already exploded.

“Hey! Reporter Park! Peace Guild! Contact the Peace Guild!”

“I-I did, of course, but nothing comes out no matter how much I poke around.”

“Then what about Ares? Don’t you have anyone you can lean on there? We’ve gotten a few sources from them before!”

“That person is in the detention center right now. You know, because he got caught up in the Go Jun incident a while back……”

“This is driving me crazy. What about Choi Minwoo?”

“Oh, don’t even ask. Getting a line into them is practically impossible, and you couldn’t get a single drop of blood out of them even if you poked them.”

“Then what about Jin Taekyung?”

“……If I touch him, I’m the one who’ll bleed. Chief, do you want to watch me get beaten to death?”

Sources of unknown origin were leaking out everywhere, but unless they made contact first, there was no way to figure out who had leaked them.

The media, driven almost to the point of madness, could do nothing but churn out clickbait articles. The situation on the internet was even worse.

> **Three-Line Summary of the Current Situation**
>
> 1. Cheon Taemin created a Mana Cultivation Method.
>
> 2. His grandson and an insanely badass junior are pushing to make it public. The government is jumping on the bandwagon.
>
> 3. There must have been Hunters who didn’t even know what a Mana Cultivation Method was, but the one Cheon Taemin created is so damn versatile that even the lowest-ranking Hunters can learn it.
>
> Wow! Level up together!

> **4. This isn’t a three-line summary.**
>
> └ **Author:** What the fuck are you talking about? I organized it neatly.
>
> └ It’s not a three-line summary when you look at it through the KakaoPage viewer.
>
> └ **Author:** You crazy bastard.

> **The Mana Cultivation Method is going public?!**
>
> └ Written by Cheon Taemin?!
>
> └ Edited by Jin Taekyung?!?!
>
> └ Wasn’t the editor Kim Gyeongsik?
>
> └ ? Who’s Kim Gyeongsik?
>
> └ The site’s shaking here too, lol.
>
> └ This one totally deserves an earthquake. Everyone in our Guild pissed themselves watching the official Blue House press conference.

> **I’m a civilian, so I don’t really know, but what exactly is a Mana Cultivation Method?**
>
> └ To put it simply, it’s a secret technique that only a tiny number of people can learn. Like the Zaha Divine Technique or the Fire Gate Divine Technique from wuxia novels. Those things are normally kept within their own circles, but this guy is saying screw that and making it available to everyone, yeah.
>
> └ I don’t read wuxia novels, so I don’t know.
>
> └ Okay, then think of it like a food recipe. Restaurants with Michelin stars all have their own recipes for the food they sell, right?
>
> └ What’s Michelin?
>
> └ LOL…… Then think of it as the sort of cooking secret every mother has.
>
> └ My mom is a terrible cook. I think she only knows the secret to making food taste bad.
>
> └ Hey. How old are you?
>
> └ Nine.
>
> └ Fuck, now I can’t even properly swear at you.
>
> └ **Fact:** Curses very refreshingly at a nine-year-old.
>
> └ Fuck off.
>
> └ I’m an avid wuxia reader, but what’s the Fire Gate Divine Technique? I know the Zaha Divine Technique.
>
> └ ? You don’t read *Login Murim*?
>
> └ Zerobic, welcome.
>
> └ He took a break over the harvest festival last year. Not Zerobic—Bastardbic.

Netizens were always divided into two camps and never stopped arguing, but when it came to articles about making the Mana Cultivation Method public, they all spoke with one voice and offered nothing but praise.

Someone was going to reveal a secret technique that others possessed but hid with all their might—and reveal it without any restrictions.

Simply out of a desire to help everyone.

For people, the public release of the Mana Cultivation Method was not something meant only for Hunters.

If Hunters became stronger, they could suppress the unsettling incidents occurring one after another much more quickly. That also meant ordinary people would become much safer.

Of course, there were also people who couldn’t hide their disappointment for an entirely different reason.

“Hmm.”

“It would have been nice if you had given us some advance notice.”

Ares Guild.

In response to the cautious complaints of the internal executives who had survived despite the rapidly changing situation within the Guild, Choi Minwoo lowered his head slightly.

“I’m sorry I couldn’t tell you beforehand. But I thought it would be better to handle things quickly before the information leaked.”

Faced with the apology from the young and capable new Vice Guild Master, the executives glanced at one another.

He had admitted his mistake and apologized first, giving them the justification they needed. This was the right time to put him in his place to ensure he would never act unilaterally again.

But the problem was the terrifying legitimacy possessed by that Vice Guild Master who was young—no, barely more than a boy.

*He actually stepped forward himself.*

*I’ve never even seen his face.*

*Does he care about his grandson that much?*

Cheon Taemin had not shown himself before everyone for an incredibly long time.

Some executives recruited from outside had never even encountered their Guild Master after joining Ares Guild, while even executives with considerable seniority had begun harboring vague suspicions after Lee Jungryong’s funeral.

*Something happened to the Guild Master.*

It was a reasonable suspicion.

Cheon Taemin had not appeared even at Lee Jungryong’s funeral, though the two had been practically sworn brothers.

Hadn’t he also refused to intervene when his grandson was sent from one overseas branch to another, practically exiled by Lee Jungryong?

But……things were different now.

No, even if they still harbored doubts in some corner of their minds, revealing them would be unbelievably foolish.

To them, the name Cheon Taemin was still the embodiment of reverence. And the fresh-faced Vice Guild Master’s winning card was not only his grandfather.

“You’re all awfully quiet.”

A low voice broke the silence. Jin Taekyung, who had been watching a webtoon on his smartphone, continued:

“When someone apologizes to you, aren’t you supposed to say something in response?”

“……!”

“Isn’t that right?”

Dozens of pairs of eyes trembled, and throats bobbed nervously.

The executives exchanged glances. Then, just as they bowed their heads with forced smiles—it happened.

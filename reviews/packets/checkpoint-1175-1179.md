# Checkpoint Review — 1175–1179

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

# Chapters 1175–1179

## Plot

Jin Taekyung tells his allies that Demon King Asmodeus lives in another world as the Lord of Heaven. They trust him, and after a final evening together, Jin promises to return and logs in. The Lord of Heaven awakens with greater strength, though his recovery is incomplete, and tells the Grand Mage that the course already set in motion cannot be stopped.

Jin returns to Murim after less than a week away, but nearly a month has passed there. He reunites with Jeok Cheongang in the Taklamakan Desert, where the group finds no living things. The Slaughter Saint suspects either a final battle in Xinjiang or that Dark Heaven has drained the region of life.

Taekyung’s secret spreads among his companions. Jeok Cheongang, the Slaughter Saint, Hyuk Mujin, Cheongpung, Ju Hwaran, and Bow Saint learn that Taekyung comes from the realm of immortals; Taekyung explains that he is human and around twenty-eight. Great Sir remains uninformed. Bow Saint privately grieves for someone she respected and admired. Great Sir mistakes her grief for romantic interest in Taekyung, but she denies it. He murmurs that a downpour is coming.

## Continuity

- The Lord of Heaven is the living Demon King Asmodeus. He has awakened with greater strength, but the process is incomplete; the Grand Mage awaits his command.
- Taekyung returned to Murim after less than a week away in the modern world; nearly a month passed in Murim.
- Taekyung’s group is crossing the Taklamakan Desert in Xinjiang, where the land appears to contain no living things. The cause remains unknown.
- Jeok Cheongang, the Slaughter Saint, Hyuk Mujin, Cheongpung, Ju Hwaran, and Bow Saint know Taekyung comes from the realm of immortals. Great Sir has not been told.
- Bow Saint grieves for someone she respected and admired; she explicitly denies that the person is Taekyung. Great Sir still remembers neither his identity nor his past.
- The Slaughter Saint offers a final battle or Dark Heaven draining the region as possible explanations for Xinjiang’s lifelessness.

## Translation Decisions

- Retain “Lord of Heaven” for 천주; Jin identifies him as Asmodeus.
- Preserve the System terms “Login” and “Logout” with initial capitals.
- Render 선계 as “the realm of immortals” and 신선 as “immortal”; distinguish these from 우화등선, “ascending to immortality.”
- Render 대인’s self-reference 본녀 as “this lady.” Great Sir’s guess about Bow Saint’s interest in Taekyung is mistaken.

## Durable state

{
  "active_continuity": [
    "Taekyung and his group are crossing the Taklamakan Desert in Xinjiang, where the land appears to contain no living things.",
    "Jeok Cheongang, the Slaughter Saint, Hyuk Mujin, Cheongpung, and Ju Hwaran know Taekyung comes from the realm of immortals; he has said he is human and around twenty-eight.",
    "Great Sir has not been told Taekyung’s secret; Jeok leaves that decision to Taekyung.",
    "Bow Saint knows Taekyung’s secret and questions whether the Martial God’s letter is truly right.",
    "The Lord of Heaven has awakened and regained greater strength; the process is not complete, but the Lord of Heaven says it will be.",
    "The Grand Mage serves the Lord of Heaven and awaits a command; none has been given.",
    "The Main Quest “Rift and Collapse” failed; “The Foreordained Collapse” warns that player choices can cause irreversible consequences.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon; Jin knows he is the Martial God and a former Player.",
    "An alert reported that Alpha had awakened; what Alpha is and what its awakening means remain unknown.",
    "Bow Saint misses and grieves for someone she respected and admired; she denies that the person is Taekyung.",
    "Jeok sent Great Sir to fetch Bow Saint; Taekyung was also looking for her after waking from a month-long sleep.",
    "Great Sir still remembers neither his identity nor his past, but showed insight into Bow Saint’s grief."
  ],
  "continuity_sources": [
    1179,
    1178
  ],
  "open_questions": [
    "What command will the Lord of Heaven give the Grand Mage?",
    "What remains to be completed, and what will happen when it is completed?",
    "What is Alpha, and what does its awakening mean?",
    "Why does the land around Taekyung’s group in Xinjiang contain no living things?",
    "Who is the person Bow Saint misses?"
  ],
  "safe_through": 1179,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1175

# Chapter 1175

Every story has an ending.

And Jin Taekyung already knew what it would take to end this nightmarish catastrophe: he had to defeat one being.

“Demon King Asmodeus.”

The name, no different from a curse to modern humanity, slipped from his lips. The air around them turned cold.

The faces of the old heroes who still vividly remembered that horrific past, even after all these decades, were especially affected.

“…Asmodeus?”

“That—that can’t be.”

Chuck Hagel and Magic Johnson spoke almost at the same time. Their reactions were exactly what Jin Taekyung had expected.

He’d shared the deepest secrets with them, but that didn’t mean they could accept everything so quickly.

No—instead, this was closer to an instinctive defense mechanism.

The human instinct to deny reality, even if only this way, rather than relive a nightmare.

“I understand. I thought the same thing. For quite a long time, too.”

Jin Taekyung meant every word.

He hadn’t experienced the Great Cataclysm firsthand, but he’d been born on its final day, in the midst of all that turmoil.

As he grew up, he’d been taught about it until he was sick of hearing it: what had happened during the Great Cataclysm, and how humanity had overcome the crisis.

And how the ruler of the Demon Realm who had caused the Great Cataclysm met his end at the hands of a great hero born of humanity, without leaving so much as a trace.

But…

“He’s definitely alive. In another world, not this one, under the name Lord of Heaven.”

Just as Cheon Taemin had existed as the Martial God, the king of demons had gained a new name beyond the borders of another world.

The beginning and the end of all this.

Jin Taekyung was certain.

To finish the path he’d walked—and still had to walk—he would have to reach that bastard.

But no one else could see the shape of the enormous puzzle Jin Taekyung had pieced together while traveling between two worlds. They could only trust the young man standing before them.

Just as the person who broke the long silence did.

“I see. Understood.”

Choi Minwoo’s voice was calm, which made it feel all the more unnatural.

As Cheon Taemin’s only direct blood relative, Choi Minwoo had the most reason of anyone present to be shaken by what he’d heard.

But after his gaze passed briefly over the others, it settled on Jin Taekyung without the slightest tremor.

“If that’s what you believe, Mr. Jin, that’s enough for us.”

This time, silence didn’t fall.

Choi Minwoo’s words had made everything clear.

They trusted Jin Taekyung.

The simple, certain meaning behind those words swept away in an instant even the faintest doubts and denials everyone had been keeping hidden in their hearts.

Even when darkness surrounds you, you can still see the torch lighting the way forward.

And to them—or rather, to all of humanity—Jin Taekyung was the one torch burning brighter than any other.

“Right. I was wrong for a moment.”

Magic Johnson muttered to himself, then suddenly chuckled.

“Still, I never thought my greatest wish would be granted like this.”

“Your wish?”

“I couldn’t make sense of anything about you, Jin. So I wanted to talk you into letting me run all kinds of experiments on you. Maybe even a little dissection, if you agreed…”

Jin Taekyung asked with genuine concern, “Are you insane?”

“Don’t worry. I’m not planning to do that anymore. Good grief, you said it was a System? That never even crossed my impoverished imagination.”

“I don’t think anyone would’ve imagined that.”

Song Song, sitting alone among the mountain-sized men, glanced at the spot beside her.

“Look at Uncle Kkeokjeong. He’s practically lost his mind.”

All eyes turned to Im Kkeokjeong, who still had a dazed look on his face. He started, as if he’d just woken up.

“Huh? Wh-what? What about me? I’m fine.”

“You don’t look fine to anyone.”

“No, I was just… listening.”

Im Kkeokjeong answered haltingly and scratched the back of his head.

“Honestly, I’m not sure I should even be hearing something this incredible.”

“Yeah, I feel the same. Team Leader Choi here—no, our Guild Master—definitely has every right to hear it. But us? Well…”

At Song Song and Im Kkeokjeong’s reaction, Jin Taekyung gave a faint laugh.

“What do you mean, ‘right’? I called you because you deserve to be here.”

That was true. They deserved to be there.

It might not have been a long time in the span of a life, but they were friends and comrades who’d shared some of the most intense, difficult days of theirs.

On the other hand, there were people he wanted to call but couldn’t.

People like Butler Kim and Pai Chen, who were no longer in this world.

Or his family, who wouldn’t be able to accept a situation like this, and Seong Jinho, his closest friend since his days at the goshiwon.

“Oh, that’s kind of touching. Didn’t know you could say things like that.”

“I’m very skilled at it, if I do say so myself.”

“Then what were you thinking at first? You know, that time we first met, when we were drinking and you were going on about Taurus and—”

“…I was wrong.”

Starting with that shameful memory, words came pouring in from every direction.

Some were about trivial things they barely remembered. Others were as vivid as if they’d happened yesterday.

For a while, they laughed and talked together.

None of them said it out loud, but they all felt it instinctively.

This might be the last time they ever sat together, facing one another with smiles like these.

Maybe that was why Jin Taekyung couldn’t bring himself to speak, even when the time came to say goodbye.

Tick. Tick.

At some point, the sound of a second hand reached him through his keen senses. Jin Taekyung closed his eyes.

The broken pocket watch.

It was moving—the thing that probably linked the modern world and Murim through the absolute force of time.

*I have to leave. Before it’s too late.*

He knew it in his head and in his heart.

But even so, Jin Taekyung felt more conflicted than ever.

Familiar faces he was always glad to see stood before him, while the faces of precious people he hadn’t been able to see shimmered before his eyes like mist.

*If only this moment could last forever.*

But that would never happen.

Time would keep moving, and neither would the enemy waiting for him in another world stop.

Not unless someone stopped him. Not ever.

*That’s why I have to go.*

It was the one thing he had to do.

The one thing only he could do.

As Jin Taekyung reminded himself of that unchanging truth and opened his eyes, every gaze around him was fixed on him.

As if they’d instinctively sensed that this was the moment they would part.

“Go on, human. Don’t make a whole thing out of it.”

The Undead King’s tone made it sound as though Jin were just popping over to the neighbor’s house. Jin Taekyung couldn’t help laughing.

Then he spoke to the smiling faces—and to those somewhere, desperately searching for him.

“I’ll come back. I promise.”

With those words, muttered like a vow to himself, Jin Taekyung logged in.

* * *

In the depths of darkness, a being suddenly awoke and drew a deep breath.

Like a child opening its eyes for the first time in a new world.

Or a pitiful evil spirit struggling to feel that it was still alive.

But this time, something was different.

The air, the energy surrounding him—all of it.

His breath, always ragged and labored, like that of someone on the verge of death, was calm. And a strength and vitality he hadn’t felt in decades welled up in his body, which had been as good as dead.

Slowly, but without stopping.

His transformation could also be felt by the devoted servant who had been waiting alone for her master in the darkness and silence.

“Congratulations, great Lord of Heaven.”

The Grand Mage’s voice, which had never wavered, trembled.

Moments earlier, she had recognized the source of the sudden sense of déjà vu. Without hesitation, she had come here and waited for her master.

“This lowly servant dared to wait for her master without permission. Please punish me.”

The next moment, an answer rang out—one she’d thought she would never hear.

Not as a mere sound, but from deep within the Grand Mage’s mind.

—You are forgiven.

What reached her could scarcely be called a voice. It was cold as ice, but the Grand Mage trembled with joy.

She’d been right.

The strange sensation she’d felt a moment ago was real, and after only a few days, her master had awoken once more and regained even greater power.

And all of this could mean only one thing.

“Has it finally been completed?”

—Far from it.

“Ah…”

The Grand Mage let out a mournful sigh before she could stop herself. Then another reverberation filled her mind, and she caught her breath.

—But it will be completed.

“Then…”

—The course already set in motion cannot be stopped by anything. By anyone.

“…”

At that pronouncement, like an oracle, the Grand Mage—prostrated with all five limbs on the ground, unable to dare face her master—bowed even lower.

The cold seeped up from the damp stone floor, but she didn’t care in the slightest.

The fierce emotion surging from deep within her heart warmed her body like a blazing fire.

“Please give your command. What should this lowly servant do?”

The servant’s question was thick with unconcealed joy. Her master answered.

Neither the eternal snows of the Tianshan Mountains, nor the sky reaching down to their peaks, nor the moon and stars beyond it—

Nor the countless armies crossing the vast continent, finally nearing the Land of Ruin beyond the desert, could hear the voice.
## Chapter artifact 1176

# Chapter 1176

Login—or Logout.

Just like the games I played as a kid, crossing an invisible boundary between two worlds had become a familiar process.

The moment everything around me vanished and my vision went dark, I found myself alone.

In darkness so deep I couldn’t see an inch ahead.

Of course, it never lasted long.

An unknown force would soon take hold of my consciousness and lead it somewhere, and at the end of that journey, the light of a new world would be waiting.

But why?

*Something’s different.*

I sensed it instinctively. Even after the thought crossed my mind, the darkness didn’t fade. That was what startled me.

*Why?*

The process and sensations that had grown as familiar as breathing felt strange now.

By all rights, my consciousness should have already crossed out of the modern world and into Murim.

Then I would recover my usual senses and consciousness in the other body I’d been apart from. It was practically a routine.

But this time, everything was different.

The darkness and silence that went on for what felt like an eternity.

The pull that came at the end of that suffocating wait.

*Whoooosh.*

My consciousness was sucked toward some unfathomably deep place, as if it had collided with a massive tornado.

I clung with all my strength to the thread of my consciousness, shaken by a force of attraction more powerful than anything I’d ever felt.

*Damn it. What the hell is this?*

If the previous trips had been limousines, this one was a locomotive.

A runaway, broken-down locomotive hurtling down tracks that were rusted and out of alignment, with no engineer to control its speed.

*Stop!*

A scream rang out in my mind before I could stop it.

But just as a school bully who was rotten to the core wouldn’t stop tormenting someone because of one short shout, the powerful wave carrying my consciousness somewhere didn’t stop either.

And at the end of that insane ride—

*Whooosh!*

A shaft of light more intense than ever burst through the darkness as if tearing it apart, swallowing my vision.

Along with it came a voice, conveyed through my senses, which had all snapped sharply into focus.

“You’ve come back.”

He didn’t ask if I’d woken up.

He asked if I’d come back.

Leaving the frantic ordeal behind me, I slowly lifted my eyelids and looked at the owner of the voice.

Several bells were ringing loudly, starting with a System message announcing that Login had succeeded. But his voice washed over my ears like spring rain.

“Yes, Master.”

*Master.*

At the natural sound of that title, the Fire King, Jeok Cheongang, widened his eyes.

Then they curved gently, like a full moon.

“Yes. Good to have you back.”

At long last, I was in Murim.

* * *

The joy of our reunion was brief.

More precisely, there was no need to draw it out.

People who knew each other better than anyone else didn’t need many words. Jeok Cheongang and I had been like that for a long time.

And for that very reason, Jeok Cheongang must have noticed right away that something was wrong with me.

“So, what kind of dogshit situation has happened this time?”

“You really can read minds. How’d you know?”

“Look at yourself. How could I not?”

“What about me? I—oh.”

Only then did I realize I was drenched in cold sweat.

It had soaked through my clothes and even the bedding beneath me. So much for having reached the realm of Unaffected by Cold and Heat a long time ago.

“When did this start?”

“Just a little while ago. You were groaning so much I thought you might shit yourself.”

“…”

Where had that warm, gentle feeling from a moment ago gone? Had I imagined the public-restroom stink in the air, too?

I grimaced and answered, “Hard to say. There are too many things that come to mind. Anyway, where’s everyone else?”

That was what I’d wanted to ask first.

No matter how I looked around, Jeok Cheongang was the only face I could see. And aside from the horses snorting as they galloped along, I couldn’t sense anyone nearby.

The answer Jeok Cheongang gave me next made my already-prickling nerves go cold.

“Gone.”

“…”

My heart dropped with a thud. That was exactly how it felt.

I asked again, my voice trembling. “Gone?”

“I said they’re gone.”

“So they were here, but—”

“Ah, they’re gone! Right now!”

Jeok Cheongang snapped, then continued.

“To be precise, they all left about two hours ago. They had to scout around and find a place to camp tonight. They’ll probably be back soon.”

What the hell was that supposed to mean?

I went quiet for a moment, then looked at Jeok Cheongang with a flat stare.

My heart had returned to its proper place long ago.

“You should’ve said that first.”

“Look at this disrespectful brat. You’re the one who didn’t listen to the end. How’s that my fault?”

As Jeok Cheongang glared at me, I turned my head slightly to the side.

Outside the window of the magnificent eight-horse carriage the emperor of the Great Nation—no, the Great Ming Empire—had sent just for me, the world lay shrouded in darkness.

“By the way, where are we…?”

“Xinjiang.”

Xinjiang.

The largest land in the world, a Land of Ruin that no one had dared invade throughout the ages.

While I’d been away from Murim, the journey that began in Qinghai had finally reached here.

Even now, grains of sand trickled through the gaps in the carriage, proving that we were in the heart of Xinjiang.

“Taklamakan Desert.”

Jeok Cheongang muttered the name under his breath, then spat out the sand in his mouth.

“Damn desert. After all the hell I’ve been through for nearly a month, I really…”

I didn’t hear the rest of what he said.

Not because he’d trailed off, or because of the fierce sandstorm beating against the carriage window.

*A month. A whole month has already passed?*

I’d spent less than a week in the modern world.

And yet a month had passed in Murim during those few days.

*The flow of time has gone badly out of sync. Beyond the point of no return.*

I’d already suspected as much.

Right after my battle with the Blood Lord in Qinghai, I’d realized the time ratio was seriously out of whack when I returned to the modern world.

But there was a difference between a sense of foreboding that existed only in your heart and one that had become reality.

Tick. Tick.

The cold ticking of the [Broken Pocket Watch] I’d tucked deep in my Inventory just before logging in seemed to ring in my ears like a phantom sound.

*But… on the other hand, maybe it’s a good thing that this much time has passed already. It means we’re that much closer to our destination.*

A month was no short stretch of time.

Especially given the situation the world faced now.

But unlike the modern world, which had suffered terrible damage in just ten days since Morgoth’s arrival, there hadn’t been any significant damage here yet.

Or at least, it felt that way for now.

Who knew what things would be like once I’d finished asking this question?

“While I was asleep, did anything happen…?”

“You mean, was there any trouble? No.”

Jeok Cheongang answered without hesitation, as if he’d guessed what I was about to ask. His voice dropped lower as he added, “It’s so peaceful it feels strange.”

“What do you mean?”

“Just what I said. The sky is murky and impossible to predict. Snow and rain fall without warning, along with heat that could melt you and even hailstones. But aside from that, there’s nothing.”

That wasn’t all that surprising.

The sudden climate changes were happening in both the modern world and Murim, and they were nothing new by now.

Besides, this was Xinjiang—the place where the Lord of Heaven had holed up—so if anything, the changes here would be worse, not better.

What caught my attention was the last thing he’d said.

“Nothing at all?”

“That’s right. On the first day, none of us noticed anything too strange. But it didn’t take long for everyone, including this old man, to realize.”

And when Jeok Cheongang went on to explain, I realized there wasn’t the slightest exaggeration or lie in what he’d said.

“At first, nobody paid it any mind. We were busy scouting the area in shifts every half shichen and standing watch through the night.”

That was only natural.

This was Xinjiang.

The thousand-year sacred land of the Hundred Thousand Demonic Disciples, who’d once swept across the land, and the base of Dark Heaven.

Dark Heaven had unleashed bloodshed across the Central Plains. It wouldn’t have been surprising if they’d turned Xinjiang, practically their own front yard, into a sea of blood.

“But strangely, it was quiet. Not a single one of those crazy fanatics who’d swarmed at us like a pack of dogs in Qinghai, not a single one of those monsters who defied all reason, not even the usual mounted bandits. At first, I thought maybe those bastards were scared.”

It wasn’t arrogance or carelessness that had led Jeok Cheongang to think that way.

Just before we set out from Qinghai, the emperor and the leaders of the alliance army—made up of the foremost figures in Murim—had divided a force of well over a hundred thousand into three groups. We were one of them.

Our group was a mere handful, fewer than twenty. But look at who was in it.

Two Saints and the strongest of the Ten Kings.

The Bow Saint, the Slaughter Saint, and the Fire King, who stood shoulder to shoulder with them.

Even with me unconscious, those three alone were more than enough to be called an army.

“But the very next day, I realized I’d been wrong from the start.”

Jeok Cheongang muttered in a low voice, then suddenly jerked his chin toward the window.

“Do you see?”

“What are you—”

I frowned at the incomprehensible gesture, then let my words trail off.

And in that instant, I understood.

In the deep darkness, that vast, endless desert was filled with nothing but sand.

At the same time, not a sound could be heard.

“Could it be…?”

“That’s right.”

Jeok Cheongang continued, his voice heavy and subdued.

“There isn’t a single living thing in this land.”
## Chapter artifact 1177

# Chapter 1177

A land of death.

Just as the words said, it was a place of utter death.

The truth I hadn’t noticed until then came upon me all at once, cold as a blade pressed to the back of my neck.

*How can there be no living things at all? How is this possible?*

The question sprang into my mind on instinct, but I quickly swallowed it down.

A foolish question.

If the Lord of Heaven—no, the Demon King Asmodeus—stood at the beginning and end of all this, then it was even less surprising.

The being who had dragged the apocalypse from the realm of imagination into reality.

From the moment I realized what he was, the word *common sense* had lost all meaning.

So the question that quickly took the place of the first was a different one.

A more practical question, closer to the heart of the matter.

I stared silently out the window at the empty landscape. Not a single bird called. Not an insect chirped. Then I spoke.

“What’s the purpose?”

It was far too late to ask how this could happen.

What mattered to me now—to us—was why.

And it seemed the person hiding in the sandstorm that had blown in from far away, whose presence had settled on the carriage roof a moment earlier, knew that too.

“Must be one of two things.”

The Slaughter Saint continued in a voice young enough to belong to a boy, yet bleak enough to betray the years he’d lived.

“The first is a final battle. One last fight, drawing on everything in Xinjiang.”

“Then the second is…”

“I don’t know exactly what’s happened, but this whole region has lost its life force. People and animals have legs, so it would make sense if they disappeared. But even every plant in the area has withered away. Dark Heaven’s probably behind it.”

Jeok Cheongang took up the conversation in a gruff tone.

“You were eavesdropping like a rat, and all you’ve got is something anyone could’ve said.”

“Watch your mouth. You never know. That rat might cut your throat tonight.”

“I wouldn’t mind. We’re running low on food anyway. A nice, crisp roast rat would make a fine breakfast tomorrow.”

“There’s no hope that way of talking will ever improve. What the hell happened to all the years you’ve lived?”

A shadow fell by the window as he answered flatly.

Like a ghost with no substance, the Slaughter Saint passed through the window as if it weren’t there and entered the carriage. He stared at me as though he could see straight through whatever I was hiding.

“Anyway, you slept a long time.”

I smacked my lips.

I’d been traveling with the Slaughter Saint for quite a while, but this was the first time I’d been away for a whole month.

And by ordinary standards, no one in the world could sleep for an entire month.

But what could I do?

The day would come when I’d tell him the truth myself. For now, though, I had to put on a straight face and bluff.

“Yeah, I’ve always been a heavy sleeper.”

“Even so, it’s impossible to stay asleep for a month.”

“I’ve got a special constitution.”

“I’ve wandered the land for fifty years, meeting all kinds of patients, and I’ve never encountered a constitution like that.”

“Congratulations. You’ve discovered a new one after fifty years.”

“…”

“…”

For a moment, suffocating silence filled the carriage.

The Slaughter Saint and even Jeok Cheongang stared at me as if I were a madman.

Fair enough. It was nonsense that didn’t even require medical knowledge to debunk.

“I’m kidding. Actually, I woke up a few times in between. You still have to take care of basic bodily functions and all that.”

“I didn’t know that.”

“You wouldn’t. Only my Master knew. Right?”

Jeok Cheongang blinked at my sudden plea for help, then scratched the back of his head.

“Uh. Well, that is…”

His reaction was a little odd, but when you’re lying, the important thing is to sound natural.

I quickly continued before the Slaughter Saint could notice anything strange.

“I woke up once a few days ago, too. After sleeping so long, I had to pee and got hungry.”

“When exactly do you mean by a few days ago?”

“Um… I wasn’t fully awake, so I’m not sure.”

“I see.”

The Slaughter Saint nodded as if he understood, then muttered to himself.

“Strange. You woke up several times, and nobody noticed.”

“Yeah. Weird, isn’t it?”

“There’s something even stranger. Want to know what it is?”

Was it just my imagination, or had the air gone a little stale?

I shook my head, uneasy for some reason.

“…No. Not particularly.”

“Surely you’re curious.”

“I’m fine. Sometimes it’s better not to know.”

“That’s a good saying. But there’s another one that fits this situation better.”

The Slaughter Saint added in a gentle voice unlike his usual one, which made it feel all the more ominous.

“Keep talking and you’ll get a beating.”

“…”

“What do you think?”

What do I think? What am I supposed to think?

I forced a smile and answered.

“I’m suddenly very curious. I’d love to hear this strange story.”

“On its own, it’s not that remarkable. To be exact, from my perspective, it was just a real nuisance.”

“What do you mean…?”

“Quite the bond between Master and Disciple. From the very first morning after we set out, that ill-tempered old man made a racket if I didn’t check on you every morning and evening. Not a single day went by in peace.”

The Slaughter Saint’s eyes sank as he glared at Jeok Cheongang, as though just remembering it exhausted him.

“Lately, his damn fits have gotten worse than ever. You hadn’t woken up in nearly a month, so it was obvious something was wrong. He kept yelling at me, demanding to know why I hadn’t found the problem.”

“…”

“That was just two days ago. Got anything to say?”

You’ve got to be kidding me.

Of course I don’t.

I’d thought something felt off. Now I knew why Jeok Cheongang had acted so strangely earlier.

With the Slaughter Saint’s eyes on him—and mine too—Jeok Cheongang stared out the window and muttered,

“Well, I didn’t yell quite that much…”

“He even called me a quack.”

“I didn’t insult you quite that directly…”

“Right. Now that I think about it, you did put it more gently. You asked if I’d learned medicine at a gambling den.”

“I did say that, but it wasn’t that harsh…”

“And what possessed you to accuse me of trying to live up to my title as the Slaughter Saint by killing your Disciple?”

“Hmm. I suppose I did go too far there. My pride won’t let me apologize, so I’ll offer my sincere regrets instead.”

The answer was steeped in the essence of the Fire Gate Clan—a clan that had been making Murim’s people furious on a regular basis for more than three hundred years. A sound almost escaped me.

Almost. Then I saw the Slaughter Saint’s expression and held it back with every bit of strength I had.

“You fucking—!”

I was very relieved Cheongpung wasn’t here.

If he’d seen this, he would’ve spouted some nonsense like, *Wow! I’ve never seen the greatest assassin of all time swear before!* Then I would’ve had to watch the greatest assassin of all time lose his temper and go on a rampage.

Fortunately, the man with another identity as the Divine Physician knew how to keep to a minimum standard of decency—unlike my dear Master—and, as a former assassin, had a near-supernatural skill for recovering his composure.

“Fine. Sure… I can understand that. People close to a patient sometimes can’t make sound judgments. That happens. I get it.”

After muttering as if trying to hypnotize himself, the Slaughter Saint took a steadying breath and turned to me.

Then, with a suddenness I could never have predicted, he blurted out a question.

“So, did you take care of things over there?”

“What?”

“Your hometown. I heard you called it the realm of immortals?”

“……!”

For just a moment, it felt as though the world had stopped.

If not for the carriage’s constant rattling, the sand slipping through the window, and Jeok Cheongang’s extremely deliberate clearing of his throat, I might’ve believed it had.

“Ahem. It came up.”

*It came up. It came up. It came up…*

His voice echoed like an echo, though we weren’t in some deep mountain valley. I closed my eyes for a moment, then opened them.

Jeok Cheongang was trying very hard to look stern.

I gazed at him in silence.

“W-why are you looking at me like that?”

“…”

“Well, I couldn’t help it. You’d been out cold for a whole month, and I was worried. The Slaughter Saint kept asking questions…”

“…”

“I explained a little. Just a little! He’s a physician. If he asks about a patient’s condition, shouldn’t he know at least something?”

I let out a long sigh at Jeok Cheongang’s halting excuses.

“Understood.”

“You used to wake up after a few days at most, but when you stayed out this long, I started wondering if you’d been poisoned by some kind of sleeping drug from the demonic, heterodox arts… What?”

“I said I understand. You had your reasons.”

Well, what was done was done.

Maybe it was just me, but I’d grown pretty close to the Slaughter Saint. He was one of my most dependable allies.

He deserved to know my secret.

Besides, the decision had been made by none other than my Master, Jeok Cheongang. He must’ve had his reasons and circumstances.

If Jeok Cheongang had slept for an entire month like a bear hibernating through winter, even I would’ve started to wonder.

Anyway…

“How much did you tell him about me?”

“Hmm. Well…”

Why did I suddenly feel so cold?

I’d only asked in case I needed to explain more, but Jeok Cheongang hesitated, glancing at me before continuing.

“I told him more or less what I knew. At first, their reactions varied, but they all believed me.”

“Oh, that’s fine. I was planning to tell you soon anyway… Wait, ‘their reactions’?”

That was strange.

There was only one of him. Why were there several reactions?

The question that flashed through my mind was answered by a shout from somewhere in the distance.

“Waaah! Benefactor! You’re back! Did you have a good trip?”

Ah.
## Chapter artifact 1178

# Chapter 1178

There are no secrets in the world that can stay secret forever.

Birds hear what’s said by day, rats hear what’s said by night, and in the end, every word slips from someone’s lips.

“I swear to Heaven, this old man told exactly one person.”

At the declaration of the one who’d first let my secret slip—as if a newborn were crying for the first time—the “one person” in question licked his lips.

“So, I was just planning to check a few facts. It’s not like I could believe a word that crazy old man said.”

I asked in a subdued voice, “And then?”

“I had no choice. I grabbed the person who seemed to know you best and asked him.”

At the Slaughter Saint’s casually shifted gaze, Hyuk Mujin, who’d been huddled in a corner of the carriage, warily watching the others, stammered out an answer.

“To be precise, you kidnapped me in the dead of night while I was sound asleep and buried me in the desert. With only my head sticking out.”

“That’s right. But he turned out to be surprisingly tight-lipped. He insisted he’d rather die than tell me anything that might put you in danger.”

Perhaps buoyed by the Slaughter Saint’s testimony, Hyuk Mujin straightened his hunched shoulders.

“You heard him, right? I’m that loyal.”

“So, I had no choice but to tell him a rough version of what I’d heard. Then the very next day, some random weirdo came asking about you.”

As if perfectly timed, that “random weirdo” suddenly stuck his face into the conversation.

“Benefactor! Benefactor! You really came from the realm of immortals? It’s true? Wow! I’ve never met anyone from the realm of immortals before!”

“Yeah. Just like that.”

The Slaughter Saint glared at Cheongpung with tired eyes, then added, “Anyway, I told exactly one person, too.”

Hyuk Mujin drew in his shoulders again and muttered, “Me too.”

Yeah. I figured.

But if I were Hyuk Mujin, I wouldn’t have spilled a “stupendous secret I couldn’t possibly keep to myself” to Cheongpung.

Why? Simple.

Because it was Cheongpung.

“Benefactor, me too! I only told Young Lady Ju!”

Maybe an innocence-proving contest had started without my noticing. Cheongpung shouted with tremendous enthusiasm, and Jeok Cheongang nodded.

“He’s not wrong. The problem was that he said it at just about that volume, at a meal where most of us were gathered.”

“…”

This was giving me a headache.

I shook my head, then happened to meet someone’s eyes.

Unlike everyone else, she’d been silent the whole time, without a reaction. Ju Hwaran.

“Ah, Young Lady Ju.”

I greeted her with an awkward smile, but she didn’t answer.

She only stared at me, her gaze pricking my face like a thin needle.

No, she wasn’t the only one looking at me.

A hush had fallen over the carriage, and everyone was watching me.

Well. I didn’t know.

I felt like I should say something, but what was I supposed to say? And how?

*Should I act like nothing happened? Or apologize for not telling them sooner…?*

My thoughts began tangling like a ball of yarn.

Then her tightly closed red lips parted.

“You’re not, are you?”

“Huh? What do you mean, all of a sudden?”

“I mean, you’re not actually an immortal or something instead of a human, are you?”

“An immortal?”

I blinked at her blankly. Then, once I understood, I let out a quiet laugh.

“What do you mean, an immortal? Do I look that impressive to you?”

“Don’t laugh.”

“…Oh. Sorry. I didn’t mean to. But really, I’m not.”

“Are you sure?”

“Of course. What else would I be if not human? Somehow, a misunderstanding piled on top of another, and I got called someone from the realm of immortals. But my hometown is just another place where people live, same as here.”

“Is that so?”

“Yeah.”

Calling them the same world would be a huge stretch.

Even setting aside the difference in technological development, you wouldn’t run into a monster on your way to the inn at the intersection by your house in this part of the world.

But I didn’t bother explaining that, and Ju Hwaran didn’t seem inclined to press the point.

Instead, she asked another question I hadn’t expected.

“Then how old are you really?”

“…Wait, what?”

“I’m just curious. You said only your soul goes back and forth, and that the other world is different from this one.”

I answered, sounding a little bewildered.

“Uh, well. Around twenty-eight?”

“Around?”

“No, I mean, that’s right. After going back and forth a few times, I got a little confused about time for a second…”

I’d started rambling out excuses without meaning to when Ju Hwaran cut me off in a voice as sharp as a blade.

“So you haven’t even turned thirty yet.”

“That’s right.”

“And you’re not an immortal or a celestial who’s lived for five hundred years since ascending to immortality.”

“…I told you, I’m human.”

Ascending to immortality? Please.

I’d been called an idiot plenty of times. By Hayeon.

And if I really were a five-hundred-year-old immortal, the one pulling this eight-horse carriage would be Cheonju, not a horse.

*Wouldn’t that be nice?*

I was lost in a thought both sweet and sad when Ju Hwaran delivered her verdict like a judge who’d finished hearing the case.

“That settles it, then.”

“Huh?”

“It’s fine. You’re human, and you’re around twenty-eight.”

It was a strange verdict.

No explanation of what the case was about. No sentence.

But that was enough.

I didn’t know what it was, but it was settled.

*No, actually, I think I do know.*

For some reason, my chest felt tight. Somewhere close to my heart.

At the same time, another part of my chest grew heavy.

I wondered if it was okay to feel this way right now. If I had any right to.

Maybe that was why I couldn’t meet her gaze easily as she kept looking steadily at me through the strange atmosphere, made even stranger by everyone else’s eyes on us.

And why, the next moment, I changed the subject for no good reason.

“Anyway, when will everyone else be back?”

“Hm? What?”

“The people who aren’t here.”

Jeok Cheongang, who’d been looking back and forth between Ju Hwaran and me, cleared his throat.

“Ahem. Why are you asking that all of a sudden?”

“I missed them. And now that it’s come to this, there’s something I want to tell everyone myself.”

“Well, they’re searching different areas, so they’ll all be back before long. But there’s no need to gather them for that. Some of them still don’t know anything about you.”

“What? But earlier, that human Cheongpung clearly—”

“Yeah, he said it all loud enough for everyone to hear. At a meal where *most* of us were gathered.”

“Oh.”

I let out a short gasp.

At the same time, it wasn’t hard to think of the person most likely not to have heard my secret yet.

“Great Sir.”

The Supreme Peak master who’d first crossed paths with us in Gansu and accompanied us all the way here.

A mysterious eccentric, as puzzling as his wild, unkempt hair—even he didn’t know who he was.

“What Great Sir? The guy can lose his mind several times a day.”

Jeok Cheongang snorted, then continued.

“He happened to be there, we couldn’t have helped it. But it still didn’t sit right with this old man to tell him that sort of thing, so I told everyone to keep quiet. He’s been useful enough, but a secret is a secret, and we don’t even know who he is.”

“Right.”

“I can guess what you’re thinking. I’m not about to force my decision on you. So do as you like about that fellow you call Great Sir. But…”

Jeok Cheongang trailed off and scratched his bushy beard.

“There’s someone else I’m more concerned about than him.”

“Someone else?”

“The people here have more or less understood and accepted it by now. But the world doesn’t work out so easily. Especially for old folks—it’s hard for them to understand something new.”

Just as I’d thought of Great Sir, I remembered another person who wasn’t here.

*Bow Saint.*

I muttered the words to myself and looked out the window.

Perhaps because of the clouds drifting across the pitch-black night sky, the stars looked especially dim tonight.

* * *

Desert nights were merciless.

By day, the heat seemed ready to burn the whole world. But once the sun set and darkness arrived, an icy chill blanketed the land.

Even through the cold that seeped into her bones, though, the faint shadow standing alone atop a sand dune didn’t waver in the slightest.

It was only natural. The master who cast the shadow had long since surpassed the realm of Unaffected by Cold and Heat.

But that wasn’t the only reason.

“The realm of immortals… The realm of immortals.”

Bow Saint gazed into the dark desert, her eyes clouded with thought.

The boundless sea of sand stretched endlessly before her, as if it resembled her heart.

As though no matter how far she walked, she’d never see its end—and as though it contained nothing but hardship and gritty grains of sand.

“So that was the secret you were hiding.”

Bow Saint murmured in a low voice.

The desert at night was an excellent listener.

It never asked anything in return. It simply let the wind pass in silence, the wind no one knew where it had come from.

But it wasn’t good company.

No, even if the desert could speak, that wouldn’t change.

The person Bow Saint wanted to talk to was someone else.

“…Martial God.”

Her fingers, as hard as steel and marked with calluses despite her translucent skin, searched inside her robe.

The old letter the Martial God had left only for her—and which, for that reason, she couldn’t tell anyone about—was caught between the folds of her clothes.

“Is this what you want?”

Bow Saint couldn’t understand.

She had believed and followed what the letter said only because the Martial God had left it. From the beginning until now, she had never been able to make sense of its contents.

And after hearing Jin Taekyung’s secret just a few days ago, she found it even harder to understand.

“Is this truly… right?”

At that moment—

*Rustle.*

A faint sound from behind reached Bow Saint’s ears.
## Chapter artifact 1179

# Chapter 1179

Her reaction was immediate.

As if she’d expected this all along, Bow Saint kicked off the ground and darted backward.

At the same time, she thrust out a palm toward the source of the sound, now wreathed in brilliant white Force.

*Boom!*

In an instant, a blinding flash engulfed the sand dune where she’d stood alone.

No—not alone anymore.

An uninvited guest had arrived.

*What a mistake…!*

Normally, she could have sensed everything within a radius of twenty-odd zhang without even drawing on her internal energy.

And yet she hadn’t noticed the enemy until they were within a dozen zhang. Bow Saint bit her lip before she knew it.

She’d been lost in thought.

The fact that her heart had been more unsettled than ever had surely played a part.

But whatever the reason, there was no excuse for such carelessness. Especially when they were in Xinjiang.

If there were two silver linings, the first was that her enemy’s stealth technique was surprisingly poor. The second was…

“Gwaaaah!”

With a strangled scream, the enemy went flying and landed with a wet smack in the distance. Their silhouette was strangely familiar.

More precisely, the horrendous stench that had arrived before him, barging in like a thief.

*…That smell.*

Bow Saint was an archer, and her eyesight was second to none. But this time, her sense of smell reacted before her eyes were even needed.

A horrendous stench—the kind she feared she might catch even in a dream.

She almost wondered how she’d only just noticed it.

Suppressing the queasy churn in her stomach, Bow Saint watched the uninvited guest groan and struggle to his feet.

“Why are you here?”

Her question carried a trace of suspicion.

And then, as always, the uninvited guest managed to leave her dumbfounded.

“Gah! An enemy! It’s Dark Heaven!”

“…”

“Reveal your mask and take off your identity! How dare you ambush me! Do you not fear the Lord of Heaven?”

Bow Saint couldn’t hold back any longer. She spoke up, stunned from beginning to end.

“It’s the other way around.”

“What?”

“You take off the mask, not your identity.”

Of course, he hadn’t been wearing a mask in the first place. She didn’t think there was any need to explain that much.

Even if she spelled it all out for him, he’d forget by tomorrow—no, in an hour.

That man, who casually referred to himself as “this lady,” was Great Sir.

*At least he knows Dark Heaven is the enemy.*

Bow Saint was sighing inwardly when Great Sir finally recognized the person before him. His eyes widened.

“Wait, why are you here, Young Lady?”

“First, I’m not young enough to be called that. And I think I’m the one who should be asking you that. I even asked you already.”

Bow Saint added in a quiet voice, “And I still haven’t heard your answer.”

The Force that had wrapped around her hand had already vanished without a trace, but appearances could be deceiving.

The internal energy accumulated within Bow Saint—several jiazi’s worth—wasn’t slowing its flow. It was circulating faster and more quietly than ever.

Ready to unleash its full strength whenever its master wished.

One mistake was enough.

If she’d made the same mistake twice, she wouldn’t be called Bow Saint, and she wouldn’t have survived the Great Faction War.

“I thought you were supposed to scout somewhere else. Am I mistaken?”

Bow Saint didn’t let her suspicion go easily.

For convenience, she called him Great Sir. In truth, he was little different from a strange eccentric, and no one knew who he really was.

Even Great Sir himself could barely keep his mind straight. How could anyone else know?

He remembered neither his name nor his past.

Not even when the Fire King, Jeok Cheongang, had confidently promised, “This’ll bring back memories from before you were born,” then given him a thorough beating with his fists.

The one thing Bow Saint knew for certain about Great Sir was that he carried on the legacy of an orthodox sect.

*His internal energy is undoubtedly pure. But that alone isn’t enough to put me at ease.*

Most of the traitors who’d joined Dark Heaven had come from orthodox factions.

Even the Murong Family, one of the Five Great Families, had rotted from its roots. What mattered wasn’t the martial arts themselves, but the heart of the person who practiced them.

*Besides, Great Sir is a Supreme Peak master. When I was staying in the Imperial Palace, I came across information about him, but… in the end, no one ever properly uncovered his past.*

Even so, there were two reasons she hadn’t objected to including him in their group.

First, though he’d joined them late, Great Sir had faced death alongside them in Gansu and Qinghai. By now, they’d built a fairly solid trust.

Second, even if he was a hidden blade planted by Dark Heaven, he posed no threat to them now.

As far as Bow Saint could tell, Great Sir was at the very beginning of the Supreme Peak realm.

That was a remarkable level in its own right. But compared with the people in their group, it was fair to call him “merely” a Supreme Peak master.

Too blunt to be a hidden blade. Too careless to be a spy.

That was precisely why she’d kept him close.

Because he was so impossible to understand, she’d kept a faint thread of suspicion alive to the very end.

Then, as Bow Saint watched him stare blankly at her, Great Sir suddenly clapped his hands.

“Oh, right! I came here because of you, Young Lady.”

“What are you talking about?”

“About half an hour ago, I finished scouting the whole area like I was told and went back to the carriage. But before I could even sit down, I got kicked right back out.”

His voice had been half tearful. Now he lowered it.

“You know that red-bearded man with the temper to match? What was his name?”

“…Great Hero Jeok Cheongang?”

“Great Hero, my foot. If that man’s a Great Hero, then this lady’s a fairy. Anyway, he was furious and told me to hurry up and find you. Sounded like something important had happened.”

Bow Saint felt her energy drain away.

“What’s this important thing?”

“How should I know? I told you, I didn’t even get to sit down. And then, after I’d come all the way here, you hit me with no mercy!”

“Sorry. I mistook you for an enemy.”

Great Sir was stamping his feet, apparently getting worked up as he spoke. Bow Saint soothed him and slowly calmed her internal energy.

She’d have to check whether what he’d said was true once they got back, but Great Sir didn’t seem to be lying.

At least, not here and now.

“But what were you thinking so hard about? You looked so cheerful from behind. I was going to call out to you, but I held back. Then you mistook me for an enemy anyway.”

Once again, he’d caught her off guard with his bizarre words and behavior. Bow Saint couldn’t help letting out a quiet laugh.

“Did I really look that cheerful?”

“You did. Standing there alone in the faint moonlight, you looked so bright and cheerful that… Oh, was that not right?”

“No, it was. And then?”

“You looked like you were muttering something to yourself, but I couldn’t make out what. Your voice was so quiet.”

That was a relief. It hadn’t been anything too serious, but it wasn’t something she wanted anyone else to hear.

This was her secret.

One no one could know about—but one she would have to decide on someday.

But Great Sir wasn’t finished.

“Who were you thinking about?”

The step she’d been about to take forward stopped in midair. Then Bow Saint’s foot slowly came down, pressing softly into the sand.

“What do you mean?”

Great Sir looked at her steadily as she made an effort to keep her voice calm.

His mind was clouded, as if covered by dark clouds, but his eyes were as clear and bright as a midsummer day.

“I don’t know, either. But… you were definitely missing someone. And you were suffering at the same time.”

“…”

For an instant, Bow Saint’s eyes trembled.

Great Sir’s voice swept into her ears and seemed to rake through her mind like a blade.

But why?

It didn’t feel like mere pain.

It was like cold water washing over a wound that had been neglected for so long it had already rotted through.

Maybe that was why her lips, which had seemed sealed forever, suddenly parted.

Perhaps it was because the only person with her in this lonely desert beneath a dim moon was an eccentric who’d forgotten his own name and wouldn’t remember anything tomorrow.

Or perhaps that was all just an excuse.

“That’s right.”

“I knew it! What do you think of this lady’s eye for people?”

Watching Great Sir delight in himself like a little child, Bow Saint let out a soft laugh.

It was so genuine that anyone from their group who’d been there would have been stunned.

“You were right. I almost wondered if you were the same person I’d known all this time.”

“It all comes from experience. I don’t remember much, but I think I used to be pretty popular in my younger days, with men and women, young and old. Anyway, who is it? The person you miss?”

“It’s a secret.”

“A secret? I like that.”

Great Sir rubbed his palms together, as impatient as a child, then asked again.

“Were you in love with him?”

After a moment’s silence, Bow Saint shook her head.

“I respected and admired him. Just as everyone else did.”

“Ah, so you never managed to tell him how you felt. What a shame.”

“I told you that’s not what I meant.”

“Words are only words. When words and actions don’t match, actions are the truth. Like how you hesitated just now.”

“…”

“Hesitation always leads to regret. And regret sometimes leads to the wrong choice. But everyone gets a chance to choose. Even if you can’t put spilled water back in the cup, you can still wipe it up.”

Was this what it felt like to have a bucket of ice-cold water thrown over her?

As if waking from a brief dream, she stared at Great Sir, her eyes wide.

“You…”

She wanted to ask.

Who was he, really? How could an eccentric like him give off such an air of profound wisdom?

But before she could finish, Great Sir whispered conspiratorially.

“So confess before it’s too late. Soon—no, today would be best. Right now.”

“What?”

“Oh, don’t take me for a fool. I knew it all along. You’ve got a deep interest in that ill-tempered man’s Disciple.”

For a brief moment, Bow Saint couldn’t understand what he meant. Then she finally managed to speak.

“…You mean Jin Taekyung?”

“Obviously, hm. You said it was a secret. I’ll keep that part to myself.”

“…”

“There’s no need to be embarrassed. Just go for it. It’ll be a relief! Sure, that fellow’s good at martial arts and comes from a good family, but you’ve got nothing to envy there. I hear your family’s Escort Bureau is doing well, too.”

Those words explained everything. Why Great Sir, a man old enough to be her son, had called her Young Lady.

Bow Saint squeezed her eyes shut.

Then, with all her strength, she reined in a great many thoughts and feelings before answering.

“That’s not me.”

“Don’t be ridiculous. I heard it from someone and everything… Hm?”

Great Sir abruptly stopped talking. He rubbed his eyes with his sleeve, then turned serious.

“Why is a heroine here?”

“…”

“Oh, right. That ill-tempered man—no, Great Hero Jeok told me to bring you over.”

Bow Saint answered with the heart of a Bodhisattva who’d almost reached enlightenment.

“Let’s go. Now, please. I won’t even ask what the important thing is.”

“I’m curious, too.”

But Bow Saint never reached true enlightenment.

At Great Sir’s next words, she felt the thread of her reason snap.

“I wonder if something’s happened—Jin Taekyung was looking for you, too. He looked full of energy after sleeping for a whole month.”

Bow Saint froze like a statue as Great Sir ambled away.

He gazed out toward the far side of the still-clouded sky, then murmured casually.

So quietly that Bow Saint, already caught in the grip of a hundred and eight earthly desires, couldn’t hear him.

“A downpour’s coming.”

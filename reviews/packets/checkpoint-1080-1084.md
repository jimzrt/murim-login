# Checkpoint Review — 1080–1084

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

# Chapters 1080–1084

## Plot

In Xining, Jin Taekyung discovers that corrupt officials left the city with food stores for at most fifteen days. After an overnight meeting, the City Lord and around a dozen other criminals are publicly executed. Hak Eui uses the meeting to present his investigation into Qinghai’s affairs. A messenger eagle then brings Taekyung an alarming message from the Murim Alliance, whose contents are not revealed.

Cheongpung learns that Potala Palace has joined Dark Heaven and that Seafaring King Pa Ryun and Green Forest Battle King Tae Gunak have turned against the Alliance. Pa Ryun and Tae Gunak coordinate a plan to seize control of the Yangtze in two days. Villagers suspect the Green Forest Alliance attacked the Blue Flower Escort Bureau after a landslide blocked a mountain road and a bureau flag was found there, but the attack is unconfirmed. Pa Ryun leads hundreds of ships and thousands of men toward the Great Nation’s warships.

Under Pa Ryun’s command, Mu Song leads the Yangtze River Channel League’s swift ships against the Great Nation’s fleet. Though he had opposed joining Dark Heaven and attacking government troops, he obeys Pa Ryun. Troubled by the soldiers’ fear, Mu Song orders his men to spare those aboard the ships they board. The League sinks more than a hundred military vessels carrying thousands of troops in two shichen, then turns west.

## Continuity

- Xining has food stores for at most fifteen days. The City Lord and around a dozen other criminals were publicly executed after an overnight meeting; Hak Eui presented his investigation into Qinghai’s affairs.
- A message from the Murim Alliance in Henan alarms Taekyung, but its contents remain unknown.
- Potala Palace has joined Dark Heaven. Pa Ryun and Tae Gunak are working together; their stated plan is to take control of the Yangtze in two days.
- Villagers suspect the Green Forest Alliance attacked the Blue Flower Escort Bureau, citing a recovered flag and a blocked road; who caused the landslide is unconfirmed.
- Pa Ryun leads the Yangtze River Channel League’s attack on the Great Nation’s fleet. Mu Song and the Iron-Water Divine Dragon opposed joining Dark Heaven and betraying the Murim Alliance, but Pa Ryun’s decision stood.
- Mu Song ordered his men to spare government soldiers aboard the ships they boarded. The League sank more than a hundred military vessels carrying thousands of troops in two shichen, then turned west.
- The black-robed captive in Qinghai’s identity and knowledge, the Lord of Heaven’s purpose for sparing Taekyung, the hidden ember Cheongheoja warned about, the Alliance’s response, and the identity of the black-robed man beside Pa Ryun remain unresolved.

## Translation Decisions

- Use Hak Eui for 학의 and retain First-Generation Disciple for 일대제자.
- Render 능지처참 as “slow slicing” in the exchange’s repeated food-and-execution wordplay.
- Use Tae Gunak for 태군악 and Blue Flower Escort Bureau for 청화 표국.
- Render 해룡선 as Sea Dragon Ship and 황하수로맹 as Yellow River Channel League.

## Durable state

{
  "active_continuity": [
    "The Yangtze River Channel League attacks the Great Nation’s military fleet under Pa Ryun’s command.",
    "Mu Song and the Iron-Water Divine Dragon opposed the League’s decision to join Dark Heaven and betray the Murim Alliance, but Pa Ryun’s decision stood.",
    "Mu Song ordered his men to spare the government soldiers aboard the ships they boarded.",
    "The League sank more than a hundred military vessels carrying thousands of troops in two shichen, then turned west."
  ],
  "continuity_sources": [
    1084
  ],
  "open_questions": [
    "What is the black-robed captive in Qinghai’s identity and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "Who is the black-robed man beside Pa Ryun?"
  ],
  "safe_through": 1084,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1080

# Chapter 1080

Even as night deepened, the lights of Xining stayed bright.

The countless people still out in the streets shared their joy without holding back, and the city’s leaders provided them with liquor and meat.

They hoped the little sparks of hope nestled in those people’s hearts would burn a little longer—and a little brighter.

But even as laughter from outside slipped through the cracks around the windows, the mood inside the pavilion remained heavy.

“Judging by those long faces, I can guess how things are going.”

Jeok Cheongang broke the silence without warning, clicking his tongue as he continued.

“Sounds like you’ve got some shitty news. Spit it out now instead of making a damn fuss later.”

“Well…”

It was the sort of thing only Jeok Cheongang could say. But because he was Jeok Cheongang, no one could bring themselves to be the first to take the plunge.

The leaders trailed off, exchanging glances. Just then, I spoke up from where I stood by the window.

“If it’s difficult to say right now, let’s start with the current situation in the city.”

The martial world might call the Fire Gate Clan a bunch of bastards, but it was only natural that a young Disciple felt easier to approach than a notorious old monster with a foul temper.

At my gentle tone, one of the leaders finally relaxed enough to speak.

“Things aren’t looking good.”

“Hmm. Not good?”

“That’s right.”

I quietly smacked my lips, then turned to the speaker.

“Understood. And may I ask your name?”

“I’m Cheok Mo, Sect Leader of Qinghai’s Gonghwa Sect. I don’t know if you’ve heard of us.”

Of course I hadn’t.

I might have known Gonghwachun, but I hadn’t memorized the names of the dozens of martial sects in Qinghai Province.

And his very first answer made it clear that I wasn’t likely to remember him in the future, either.

“All right, then. Sect Leader Cheok of the Gonghwa Sect.”

“I’m listening.”

He nodded lazily. I met his gaze and continued evenly.

“Do you want to be here?”

“…?”

“You’re free to leave. If all you’re going to do is state the obvious, that is.”

“……”

“And when did we get so familiar? What do you think, sir?”

I added the question and turned my gaze to a middle-aged official dressed in silk robes. He swallowed nervously before answering.

“H-How could I possibly contradict the Marquis of Shangshan?”

“That’s a strange answer. I don’t think I asked whether you’d contradict me.”

“Y-You are absolutely right!”

“Sure. Anyway, I’ve been standing here for a while, and my legs are getting a bit tired. Is there an open seat?”

I could have stood there for days without a problem, and there were plenty of open seats. But the middle-aged official sprang from his chair.

“There’s a seat right here!”

“Oh, you don’t have to do that. Especially when you’re so much older than me.”

“I-I don’t know what I should…”

“What do you mean, what should you do? Are you trying to set me up to get cursed out? Make it look like some kid who hasn’t even dried the blood from his head is throwing his rank around to bully his elders?”

“Th-Then I’ll sit.”

The official’s eyes darted back and forth as he cautiously started to lower himself into the chair. I muttered as if to myself:

“He’s actually sitting. Doesn’t know how to read the room.”

“…Pardon?”

“Hm? What is it?”

“I mean, what you just said…”

“Oh, did you hear me?”

“…Yes.”

“I was just talking to myself. Go ahead and sit.”

“……”

“Why do I have to keep telling you? Sit down.”

If he’d been completely clueless, he might have eased himself into the chair anyway. But the middle-aged official before me could only stare at me with eyes that seemed to shake, unable to move either way.

Then again, he must have been good at reading the room to have landed such an important post as City Lord at a relatively young age.

*And that same instinct must’ve helped him skim plenty of things off the top over the years.*

Leaving the City Lord of Qinghai sweating through an imaginary squat, I glanced to my side. Jeong Hogun was smiling with a crooked twist to his lips.

I didn’t have a hobby of bullying old men, but what I’d heard from him on the way to Xining had thoroughly washed away any guilt I might have felt.

*A textbook corrupt official.*

The Embroidered Uniform Guard—the imperial family’s foremost military force, with intelligence capabilities comparable to the East Depot—had obtained the information long ago. There was no room for doubt.

More important, though, was the state of affairs his negligence had brought about.

“I heard somewhere that the city’s food stores aren’t all that plentiful. What do you have to say about that, City Lord?”

“Th-That’s…”

“Just the numbers. No lies.”

“W-We had far too many commoners flood the city in a short time…”

“That’s a long tongue you’ve got. Want me to shorten it?”

“On-One month! One month!”

The City Lord of Qinghai blurted out his answer, then added in an uncertain voice:

“…Probably.”

“That won’t do. Thousand Captain Jeong?”

*Step.*

Jeong Hogun stepped forward at my call. The City Lord squeezed his eyes shut and cried out:

“F-Fifteen days! The food we have in storage will last that long at most!”

“Fifteen days. Are you sure about that this time?”

“I-I stake my life on it!”

Men with plenty to lose never gamble with their lives.

And in that sense, the City Lord’s answer rang with a deep sincerity—and made me furious.

A huge number of refugees had arrived in a short time, but Xining had only been like this for about seven days.

Qinghai was a border province. It was only natural that it would have more military provisions stored away than the Central Plains, in case of an invasion.

And yet there was only enough food for fifteen more days…

*He’s really been eating well.*

I sighed and looked at the City Lord. Sweat poured down his face from his impromptu leg workout, and he looked terrified.

“Why are you so scared? Anyone would think I was trying to kill you. Am I?”

“Th-Then…”

“Don’t worry. I won’t kill you.”

“Thank you!”

I smiled gently at the City Lord, whose face had brightened at once, and added:

“At least not right now.”

“I’ll devote my whole heart to serving the Marquis of Shangshan from now on… Pardon?”

“Why are you asking me to repeat myself? You heard me.”

At that moment, three or four Embroidered Uniform Guards came striding up behind the City Lord and surrounded him.

“W-Wait! You can’t do this!”

“Who says we can’t?”

It was a terrible turn of events for the City Lord, but as the man who’d saved the imperial family and been personally appointed a marquis by the Son of Heaven, I had more than enough authority and grounds to do this.

And his fate had been all but decided before I even set foot in Xining.

“Send him off at sunrise. And don’t forget to give him some company on the way. He might get lonely.”

“As you command!”

Jeong Hogun answered more firmly than ever, then gestured. At his signal, the other Embroidered Uniform Guards waiting nearby swiftly carried out their orders.

“Songak of Qinghai’s Regional Military Commission. Is that you?”

“I-I haven’t done anything wrong!”

“That’s for us to decide. Not you.”

“……”

“These are the Marquis of Shangshan’s orders. Come along quietly if you want to see tomorrow’s sunrise.”

It happened in the blink of an eye.

Generals in ornate armor and officials in robes as stiff as their necks, were dragged out one after another, their faces pale.

There wasn’t the slightest resistance throughout the whole process.

No—that wasn’t quite right. They hadn’t even dared to try.

The presence of Supreme Peak masters who could shake the world had something to do with it. But the moment they opposed the imperial Embroidered Uniform Guard, their entire families could be branded traitors.

Beheaded as corrupt officials in league with the City Lord of Qinghai, or branded traitors and wiped out along with their families: faced with those two choices of death, they had only one option.

Accept reality.

And despair without end.

But unlike those men, dragged away to wail as if everything were over, the people would grow more united and rejoice now that the tumor had been removed.

And along with that—

“Looks like we’re finally ready to have a proper discussion.”

Those dozen or so seats, emptied in an instant, meant the presence of someone had filled the void they left behind.

Me.

The presence of Jin Taekyung, the Blazing Flame Divine Dragon.

“What does everyone think?”

“……”

“……”

Suffocating silence weighed down on the pavilion.

Those close to me were smiling quietly, but the faces and eyes of those who didn’t know me had sunk into darkness as they looked at one another.

Their backs, now sitting straight. Their fingers, tapping the table slowly, but with growing impatience.

Some of them might have looked down on me in their hearts, or tried to diminish me.

Rumors always grew out of proportion.

And in an unsettled age like this, heroes were sometimes made because people needed them.

But they were wrong.

There had always been people like that, no matter the time or place. And the outcome had always been the same.

There had also always been those who watched everything in silence, their expressions impossible to read.

Like the young Daoist who now looked straight at me, unlike the few who were avoiding my gaze.

“Rumors are ultimately made through the eyes and ears of those who hear them, so I never put much stock in them, as usual.”

His Daoist robes were neat, without a single wrinkle, and his eyes had a depth impossible to fathom.

“But meeting you in person has shown me again that I was right.”

His voice was calm and unruffled, just like his neatly arranged appearance.

“It seems rumors aren’t very reliable. Sometimes they fall short—and sometimes… they exceed every expectation.”

*Rustle.*

The young Daoist rose from his seat, clasped his hands toward me in greeting, and spoke.

“I am Hak Eui, a First-Generation Disciple of the Kunlun Sect. It is an honor to meet you, Great Hero Jin Taekyung.”
## Chapter artifact 1081

# Chapter 1081

“I am Hak Eui, a First-Generation Disciple of the Kunlun Sect. It’s an honor to meet you, Great Hero Jin Taekyung, the Blazing Flame Divine Dragon.”

Slender build. Refined features.

And a natural manner—not too much, not too little.

He looked somewhere between a young man and a middle-aged one, the very picture of a Daoist. I’d guessed who he was the moment our eyes met, so I bowed in return.

“This is the first time we’ve met like this.”

I couldn’t have said that without knowing who he was. Hak Eui replied calmly, without the slightest change in expression.

“My one and only Junior Brother is rather talkative for a Daoist. So I assumed you’d already heard a thing or two about me.”

I scratched my chin as I looked at the man who was the eldest Senior Brother of Kunlun Cloud Dragon Hak Unui, Hak Su’s Junior Brother, and Cheongheoja’s second Disciple.

“Even if he’s not here, that seems a bit harsh for a judgment of your one and only Junior Brother.”

“It’s all right. I would’ve said the same thing if he were here.”

So that was why people said not to judge by appearances.

Despite his refined looks, Hak Eui had a way of coldly stating the facts. Without hesitation, he continued.

“Earlier, Great Hero Jin, you said we should have a proper discussion. Before that, there’s something I’d like to ask.”

I shrugged in assent, and Hak Eui went on.

“What do you intend to do with the City Lord of Qinghai and his associates who were just taken away?”

The question felt a little out of the blue, but I answered readily.

“Of course I intend to behead them. At daybreak, in front of everyone.”

The outcome had been decided long ago.

The City Lord of Qinghai had been able to live so comfortably as a corrupt official because of the conflict between the Son of Heaven and the Eastern Heaven Demon Lord. His embezzlement had drawn the Embroidered Uniform Guard’s attention a long time ago.

In the end, it was only a question of who would take up the sword. The owner of the neck to be cut had already been decided.

*And in a situation like this, it’d be ridiculous to let a man like him live.*

Peace had lasted a long time in the Great Nation, too.

The City Lord of Qinghai had spent years lining his pockets with gold by selling off military provisions behind everyone’s backs. There was no way the army could have been functioning properly under a man like him.

There was hardly any answer but beheading.

But Hak Eui’s next words went well beyond anything I’d expected.

“No.”

“...!”

“...!”

“I ask you to reconsider that decision.”

His firm voice sent a stir through the pavilion. Naturally.

If asking what I planned to do with them had been a little out of the blue, this was overstepping.

Even if the Son of Heaven’s decree had weakened the principle that officials and martial artists must not interfere with one another, there were still limits.

A line that someone of Hak Eui’s standing—the Kunlun Sect Leader’s second Disciple—couldn’t cross.

And the first person to react to Hak Eui stepping over that unseen line was—

“Perhaps you pursued the Dao and never learned the law. Mind your words, Daoist of the Kunlun Sect.”

Jeong Hogun’s voice was as blunt as ever, but I noticed a faint anger in his eyes as he looked at Hak Eui.

While some people tensed beneath Jeong Hogun’s aura, Cheongheoja watched his Disciple in silence.

*I don’t know him well, but he doesn’t seem like the sort to sit back and do nothing in a situation like this.*

One person makes the mess; another cleans it up.

When a Disciple did something wrong, the Master usually stepped in to handle it.

Even Jeok Cheongang, who ranked among the most hot-tempered men in the world, would sometimes remember to call me out when I acted unreasonably.

Of course, he’d take my side without a second thought first.

*But Cheongheoja is different.*

Watching Cheongheoja deal with the hopeless trio by the shores of Qinghai Lake had convinced me that the old Daoist’s character was practically saintly.

If a man like him was simply watching the situation unfold, there had to be a good reason.

“Then why?”

“...Marquis of Shangshan.”

Jeong Hogun frowned when I suddenly spoke to Hak Eui, but I ignored him and asked Hak Eui again.

“Tell me. Why should those bastards be kept alive?”

Was this the mercy of a Daoist who followed the Way of Heaven and wanted to avoid taking lives as much as possible? Or was there another reason?

By now, I was genuinely curious.

Everyone’s attention fixed on him. At last, Hak Eui’s tightly closed lips parted.

“I don’t remember saying that.”

“Hm?”

“I only asked you to reconsider beheading them.”

“No, I mean, isn’t that—”

I was about to ask what the difference was when Hak Eui added, his tone firm:

“Beheading is far too lenient. Have them executed by slow slicing in front of the people.”

“...What?”

“At times like this, one punishment should serve as a warning to a hundred. Based on the close investigation I’ve conducted into the city’s affairs over the past few days, even slow slicing seems a little too lenient.”

“...!”

“...!”

Silence fell over the pavilion. Jeok Cheongang, who’d been watching with interest, muttered under his breath.

“What a masterpiece.”

The Slaughter Saint and the Bow Saint, seated beside him, spoke with dubious expressions.

“Is he... sure he’s a Daoist?”

“How did the Kunlun Sect end up like this...”

As the elders sighed, the hopeless trio tilted their heads at the sight of everyone staring blankly at Hak Eui, then whispered among themselves.

“Wow, I’ve never heard of ‘slow slicing’ before. What does that even mean?”

“Taishan knows.”

Taishan answered confidently, swallowing as he continued.

“I ate it once. It was very tasty.”

No, that couldn’t be right.

“Oh! So it’s a kind of dish. I’ve never tried it. Great Sir, have you?”

“What sort of dish could that possibly be? Honestly, young people these days.”

For once, Great Sir looked at Taishan and Cheongpung with an expression of pure contempt, as if a normal person had possessed him. Then he added:

“‘Slow slicing’ isn’t a dish. It’s a sobriquet. The name of a great fiend who once terrorized the whole world.”

Cheongpung and Taishan gasped at the same time. Their eyes went wide, and they eagerly asked:

“What happened to that great fiend?”

“What do you think? He fell to this lord’s hand.”

No, that couldn’t be right.

“Gasp! Then what Taishan ate back then was...”

“This is driving me insane. No, it wasn’t.”

I agreed completely, but why was that guy the one saying it?

“Taishan really didn’t know. Who knew a great fiend could be so tasty?”

“How many times do I have to tell you? That’s not what it was.”

He’d said it exactly twice so far—and it hadn’t even been a great fiend.

“No. Taishan really ate it.”

“...Really?”

Don’t let him convince you now. Please.

*Are these guys actually insane?*

Their intelligence had suffered a thousand cuts, and my head was spinning from listening to them. Just then, an old man’s voice rang out.

“I urged you to follow the Dao, yet it seems this unworthy Master failed to teach his Disciple well enough.”

At last, the Kunlun Sect Leader, Cheongheoja, broke his silence. Hak Eui bowed his head slightly.

“I’m sorry, Master.”

His expression didn’t look sorry at all.

But whatever he was thinking right now didn’t matter to me. I was only interested in what his unexpected answer had revealed—the fact that had just shocked everyone.

“No need. Go on, then. Your Disciple still seems to have plenty to say.”

Hak Eui slowly raised his bowed head. A glint passed through his eyes as he looked straight at me.

“What do you mean?”

“You said it yourself. You’ve spent the past few days investigating, and doing so very thoroughly. Wasn’t that what you wanted to talk about from the start?”

“...!”

“Oh, was it not just the past few days? Have you been at it all along?”

Across the enormous table, where dozens of people were seated, Hak Eui’s eyes widened slightly. I could tell I’d hit the mark, and I let out a quiet laugh to myself.

He and I were both young.

No—we were young compared to the Sect Leaders who held sway over Qinghai’s affairs and the Kunlun elders seated here.

But even with that in common, our positions were worlds apart.

I could claim one of the few seats at the head of the table. He had to sit at the far end.

That was all the more reason he’d need a chance to speak.

Like this moment, with everyone’s attention fixed on him.

“Go ahead. Speak freely. Nobody’s going to object, right?”

“Of course not.”

Jeok Cheongang answered for me, adding a genial smile.

“If anyone has a problem, raise your hand now. This old man will personally persuade you.”

Naturally, no one raised a hand. The meeting continued through the night.

And when the long night ended, a dozen or so criminals—including the City Lord of Qinghai—were dragged into the streets amid the curses of a vast crowd.

A shrill cry rang out.

A bird of prey streaked across the high sky and arrived as if heralding their end.

No.

A messenger eagle.

—

**Henan, Murim Alliance.**

I stared silently at the five characters written on the missive, then drew in a deep breath.

And the next moment—

*Rustle.*

As soon as I unfolded the message and read its contents, a shiver ran through me, raising the hairs all over my body.

“...Damn it.”

The sky above me was dark as I looked up, the curse slipping out before I could stop it. Beneath it, the executioners’ blades flashed cruelly.

*Shhk!*

As a severed head fell, a tremendous roar erupted.
## Chapter artifact 1082

# Chapter 1082

At the same time, Jin Taekyung wasn’t the only one watching the public executions from a pavilion overlooking the streets of Xining.

*Shhk!*

A dozen or so heads rolled from the flashing blades.

As fountains of blood erupted and the headless bodies crumpled lifelessly, the crowds that blanketed the streets roared.

“Waaaaah!”

“Long live His Majesty the Emperor!”

“The Marquis of Shangshan has punished the corrupt officials!”

“You fiends! Rot in hell!”

Some people threw up their hands in celebration, while others, still too angry to be satisfied, continued to curse and jeer.

But the young man looking down at them wore a conflicted expression.

“...Hmm.”

A low groan slipped from his lips. Then someone’s voice suddenly pierced his ears.

“Oh, there you are.”

The young man spun around in alarm. When he saw who the unexpected visitor was, he let out a sigh of relief.

“You startled me! When did you get here?”

“When did I get here? We all arrived yesterday. Are you an idiot?”

“Um, Uncle… I wasn’t asking when you came to Xining…”

“Then what?”

The shabby, middle-aged man—Great Sir—looked genuinely puzzled. The young man clicked his tongue.

“No, you’re right, Uncle Great Sir. We got here yesterday.”

“As I suspected. You are an idiot. Kang Pung, you’re far too naïve for your age.”

“It’s Cheongpung.”

“That’s exactly what I said. Kang Pung.”

For a moment, the young man—no, Cheongpung—was at a loss for words. He scratched his chin.

Even with the breadth of mind to reach far beyond the limits of ordinary people, he sometimes found the middle-aged man before him difficult to understand. They’d only met a few days ago.

Of course, for most people, it probably wasn’t just sometimes. It was all the time.

“...I’ve never met anyone like you.”

“The world is vast. You should broaden your horizons like this maiden.”

“Hmm. I’ve been meaning to say this since we first met, but I thought ‘this maiden’ was what women called themselves.”

“So?”

“Huh?”

“Judging people by appearances alone is a grave mistake. What matters is the essence. Only then can you understand the truth hidden within.”

Cheongpung stared blankly at Great Sir, who seemed, for a moment, to possess some profound insight. At last, he managed to speak.

“You almost sounded like an immortal just then.”

“Did I?”

“Yeah. But at the same time, you also seemed a little… unimpressive.”

“Isn’t that a bit harsh? I don’t mind, being this maiden and all, but someone else might be hurt by that.”

“Oh! I’m sorry.”

“No need to apologize. Being stupid isn’t a sin.”

“...Okaaay.”

Cheongpung answered without thinking. He was still feeling uneasy about whether that had been the right thing to say when Great Sir, hearing the roar outside grow louder still, came over to look out the window.

“How cruel.”

Cheongpung followed his gaze, his face stiffening.

The scene was clear: some of the crowd were desecrating the bodies of the executed men.

“...It is. I shouldn’t have looked.”

“You seemed down when I saw you from behind a little while ago. Was that why?”

“I never get used to killing. If I were as strong-willed as my Benefactor, I’d be much better off.”

Muttering as if to himself, Cheongpung suddenly thought of someone.

Jin Taekyung. No matter how high the waves of hardship and adversity rose, he always faced them head-on, never wavering.

People in the world praised Cheongpung and Taekyung as the Two Dragons, but to Cheongpung, Jin Taekyung was someone to look up to.

Not because of strength or weakness, or talent in martial arts. He admired the way Taekyung lived.

Perhaps that was why, at Great Sir’s next words, Cheongpung was momentarily speechless.

“Did you know? This world calls someone who’s grown used to killing a Killing Ghost.”

“...!”

“The strong-willed ones simply don’t show it. They haven’t gotten used to it. They’re closer to being worn out and utterly exhausted. Someone I knew was like that, too.”

“Do you know someone like that, Uncle?”

“I told you. You should broaden your horizons like this maiden.”

Great Sir let out an enormous yawn, then continued.

“But he chose to accept the reality and fate he was dealt. The person you want to be like probably feels the same way.”

“...Uncle Great Sir, is this really who you are?”

“What on earth do you mean, ‘is this who I am’?”

“No, it’s nothing.”

Cheongpung blinked at the words that had flowed so easily from Great Sir’s mouth, then let out a long sigh.

“You’re right. I was so stupid that I spoke without thinking.”

“I’ll say it again: being stupid isn’t a sin. And those men being desecrated even after death aren’t the real sinners, either.”

“They aren’t?”

“Oh, of course they’re sinners. They committed crimes worthy of death, so they deserved to die. But isn’t the real sinner the one who created this asura’s hell?”

Great Sir pointed somewhere.

At the endless stretch of sky, gloomy and overcast even at midday.

“I don’t know if some so-called Lord of Heaven is up there, but I’ll bet my balls he’s not all that impressive.”

Cheongpung, who had been listening to Great Sir with a serious expression, tilted his head.

“Um, only men like me have those…”

“I told you, I have them too.”

“No, I mean, I have them too.”

“Then that settles it.”

Great Sir continued in a solemn voice.

“It’s obvious you’re a woman like me.”

If this had been the old Cheongpung, he might have wondered whether that was true. But after a little over two years of gaining some common sense, the Cheongpung of today was different.

“My Second Grandfather said I’m a man.”

“Really? And did your Second Grandfather have them, too?”

“Yeah. I caught a glimpse while he was peeing. I got caught right away and nearly died, though.”

“I see.”

Great Sir thought it over with a serious expression, then gasped.

“Now I understand.”

“What?”

“He isn’t your grandfather. From now on, call him Second Grandmother.”

“...Be careful. If that gets back to him, he might really kill you.”

“Second Grandmother can’t kill this maiden. Slow Slicing—the vicious fiend—even he eventually knelt before me. Though he ended up in Baekdu Gangsan’s belly.”

“Are you talking about Young Hero Taishan?”

“Well, same difference. How many times have I told you? What matters is the essence.”

Cheongpung rubbed his temple, feeling disoriented for some reason.

“Whenever I talk to you, I get confused. This is a first for me.”

“I understand. Your Intelligence is low.”

“I’ve lost count of how many times you’ve called me stupid. Is that why you came to find me?”

“Of course not. Do I look like I have that much free time?”

Cheongpung answered with more certainty than ever.

“Yes.”

“Not at all. The reason I came to find you was…”

Great Sir had confidently begun, but his voice faltered.

“The, um, reason…”

“Uncle Great Sir.”

“Why do you keep interrupting me? I’m trying to tell you.”

“That was the first time I called you. And be honest—you don’t remember why you came, do you?”

“What nonsense!”

Great Sir snapped, then added hesitantly:

“Truthfully, it’s a little hazy. But it can’t have been important, so let’s move on.”

“Are you sure it wasn’t important?”

“I’m sure. I think someone may have asked me to come get you, but if it had been anything terribly important, I’d remember.”

Just as Great Sir answered firmly, as if to allow no further argument, someone’s presence came rushing toward them from far away.

“Young Hero Cheongpung! Where are you? Damn it, Young Hero Cheongpung!”

A familiar voice and face.

Cheongpung raised his hand at the sight of Hyuk Mujin rushing around in every direction.

“Oh, Captain Hyuk!”

“I’m going crazy. Why are you still here? And where’d that Great Sir go?”

“Huh? Great Sir is right here with me…”

Cheongpung trailed off and blinked.

Great Sir, who had been standing right beside him just a moment ago, had somehow ducked down and hidden himself close behind Cheongpung.

“...Uncle?”

“Shh. Don’t let on that you know me. Are you really that low in Intelligence?”

Cheongpung had no time to answer.

Before he could even feel exasperated at Great Sir’s simple yet flawless concealment technique, Hyuk Mujin hurried over, panting, and said something that struck Cheongpung like a bolt of lightning.

“This is no time to stand around here! The Potala Palace in Tibet has joined forces with Dark Heaven!”

“...!”

Cheongpung’s eyes widened in an instant.

But Hyuk Mujin wasn’t finished.

No—the next news was an even greater shock, one that put the first to shame.

“And that’s not all! Seafaring King Pa Ryun and Green Forest Battle King Tae Gunak…”

Since the conflict with Dark Heaven had begun in earnest, the Murim Alliance had feared that the Murim world of Tibet would join them.

On top of that, the moment he heard the names and titles of the two giants who divided the dark-path Murim between them, Cheongpung understood what was coming next.

*Betrayal.*

And as always, his ominous suspicion soon became certainty.

* * *

“The smell of manure was wafting all the way from a hundred li away. I knew it had to be you.”

The first to break the silence was an old man with an overwhelming build.

His blazing eyes were more intense than the sharp edge of the crescent-bladed guandao in his hand, and the aura pouring from his entire body was as vast as a surging wave.

As immense as his title, the Seafaring King.

“Better than the smell of fish. You’ve spent your whole life eating it raw. Your belly must be crawling with worms by now. How about you quit your life at sea and come work under this old man?”

But the other old man facing him from more than three hundred yards away was no pushover, either.

He was pitifully small, his bones thin as twigs.

Though he was so old he looked as if he might struggle to wring a chicken’s neck, he had every right to sneer at Pa Ryun.

If the Seafaring King Pa Ryun was the king of the Yangtze, then he was the ruler of the mountains.

The man who had built the Green Forest Alliance of today—the Green Forest Battle King, Tae Gunak.

“‘This old man,’ my ass. You’re a squirt, yet you run your mouth like that. Did you swallow some rotten sewage by mistake?”

“Funny, calling me a squirt over a mere one-year age difference. And even if we’re only counting our experience in Murim, I’m clearly your Senior.”

“Is that why you named yourself a king, since no one would call you one of the Ten Kings?”

Pa Ryun fired back as if he’d been waiting for the chance. Tae Gunak’s gaze sank.

“Your tongue’s always been the problem.”

“Funny. I was about to say the same thing.”

The two old men stared at each other in silence. Their auras had taken on visible form, billowing above their shoulders.

As if they might risk their lives in a fight at any moment.

But the next instant—

*Fwoosh.*

The two giants of the dark-path Murim swiftly suppressed their auras and quietly clicked their tongues.

They had lived without hesitation, using any means necessary to get what they wanted. They didn’t know when this long-standing rivalry would end, but they both knew it wouldn’t be today.

“How’s the plan?”

“Going smoothly. Just as we were told.”

Tae Gunak looked toward the dense forest behind him, his gaze darkening, then added to Pa Ryun:

“Don’t forget. Two days. Two days from now.”

His voice was deep and low.

“Take control of the Yangtze. That’s where it begins.”
## Chapter artifact 1083

# Chapter 1083

From the moment good and evil first split apart, things that would never disappear from the world were born.

Those called bandits were among them.

They robbed and stole wealth, and sometimes even took other people’s lives in the process. They had existed since time immemorial and were the kind of people who could never be rooted out completely.

Just as shadows fell wherever there was light, the wheel could not be stopped unless people were rid of the desires and emotions everyone felt.

Perhaps that was why people had finally decided to accept this unpleasant natural order.

Rather than spill innocent blood trying to break an unbreakable cycle, they had come to tolerate a certain degree of coexistence through talking things out.

But people could sense that the long stretch of coexistence was now rushing toward its end.

“Hey, have you heard the news?”

Foreboding always ran a step ahead of hope.

The people of county towns near mountains and rivers felt the unusual atmosphere keenly.

“They say a sudden landslide last night completely blocked the road over the mountain. The herb gatherers say it doesn’t look like an ordinary landslide…”

“What do you mean, it wasn’t an ordinary landslide?”

“I’ve spent my whole fifty years plowing fields, so I can’t say for sure. But those folks can tell at a glance.”

“And?”

“The herb gatherers took one look at the cut ends of the trees swept down with the earth and sand. They hadn’t been bent and snapped clean off—it looked as though someone had given them a few halfhearted chops with an axe. Besides, there weren’t any real signs of a landslide to begin with.”

“Wait. Does that mean…”

“Who else could it be? Unless ghosts did it, it was those damn bandits.”

“Shh! ‘Those damn bandits’? Watch your mouth. It’s unlikely, but if the Green Forest Alliance hears you…”

“Green Forest Alliance, my ass. What’s wrong with calling bandits bandits? They’re highwaymen who take two days’ wages just to let you cross a mountain pass!”

“Now, now. I understand how you feel, but the Green Forest Alliance is officially on our side. By imperial decree, they’ve joined forces with the Murim Alliance against the vicious enemies in the west.”

“That man’s right. Everyone knows bandits are no good, but they’re not completely out of control like Dark Heaven. Something like this happened when we were kids, too, didn’t it?”

“Right. Though it wasn’t Dark Heaven back then, it was the Demonic Cult. Anyway, I remember the Green Forest Alliance joining forces with the Murim Alliance to fight them. The Green Forest Alliance was formed afterward.”

For middle-aged men who were getting on in years, the Great Faction War was one of those childhood memories they would never forget.

Ordinary people had suffered little harm, but the news that bloodthirsty murderers who believed in an evil doctrine had invaded the Central Plains had thrown the whole land into turmoil.

So even with these ominous rumors about the Green Forest Alliance, people couldn’t help but remain skeptical. The Green Forest Alliance they remembered was a group formed by bandits who were at least willing to talk. They had long since become a part of everyday life.

But that wasn’t the only rumor going around.

“Do you remember those men who passed through our village in the dead of night two days ago?”

“Of course. You mean those strangers? I think they called themselves the Blue Flower Escort Bureau.”

“Right, those men. I was shocked to see one of their porters, big as an ox, holding up that heavy flag without even blinking. Then I got a second shock when I saw his face—it was even more terrifying than his build.”

“Why bring that up now? Merchants and escort bureaus pass through here several times a month. It’s nothing unusual.”

At the others’ puzzled looks, the middle-aged man who’d started the conversation lowered his voice.

“They did come through, but where they went in the end—that’s what matters, isn’t it?”

“What?”

“See for yourself. Herb Gatherer Hong pulled this out of the landslide early this morning.”

The next moment, the middle-aged man pulled a bundled piece of cloth from his robe and unfolded it. Everyone who saw it widened their eyes.

More precisely, they stared at the two characters revealed as the dried mud and grains of sand fell away.

Blue Flower.

“T-This is…”

“If you remember that big porter, you’ll remember the flag he was carrying, too. That’s right. It’s their escort flag.”

The villagers looked at one another and swallowed hard.

A flag held great symbolic meaning for any group.

Just as soldiers would give their lives to protect a general’s banner, the merchants and escort bureaus they knew took pride in their own flags.

But what if an escort bureau’s flag, carried along the mountain road in the dead of night just two days ago, had turned up in the landslide?

And what if a suspicious landslide had blocked the only road through the mountains a day later?

“You can guess what this means, can’t you?”

“…You don’t think?”

“I’m not guessing. That’s exactly what happened. The Green Forest Alliance—those damned bandits—must have pulled something. For some reason, they killed to silence whoever knew, then tried to cover it up by passing it off as a landslide.”

A suffocating silence pressed down on the group.

Their unease, now unmistakably real, tightened like a noose around their necks as the pieces of the situation fell neatly into place.

“B-But what would they have to gain from doing that? They fought the Demonic Cult in the past. As a reward, they got to call themselves an alliance, like the river pirates on the Yangtze, and live pretty comfortably.”

“Do you remember what you said during the harvest two years ago?”

“Two years ago? What does that have to do with anything?”

“You were disappointed. It was the best harvest in nearly ten years, but you sighed and said it still wasn’t enough. Would those men be any different?”

“…!”

“It’s obvious. Even we farmers get greedy. What about men who make their living taking what belongs to others?”

Even if their paths were different, some things still fit.

The middle-aged tenant farmer was only speaking from what he’d learned himself and his prejudice against bandits. But his argument made plenty of sense.

The Demonic Cult had wanted only the Central Plains Murim. Dark Heaven wanted the world itself.

Anyone who won this gamble could become a true king of a nation, instead of merely being called one of the Ten Kings.

A new world.

Under a new ruler.

Among all the news that had reached this little village, there was also a story far more shocking than the still-unconfirmed rumors of the Green Forest Alliance’s betrayal.

“Even the Murong Family of the orthodox faction—the one supposedly full of Great Heroes of Benevolence and Righteousness—joined forces with those vicious enemies. What do you expect from a bunch of thieves?”

At the mention of the Murong Family, one of the Five Great Families, which had unleashed a bloodbath across the northern lands, the others shut their mouths as if on cue.

That was right.

For people born bandits, whose whole purpose in life was to take what they wanted, why would betrayal matter?

If they could win this enormous gamble and survive to the end, they would gain wealth and glory beyond anything they’d known before.

“What a turbulent age we live in.”

The old man’s quiet murmur from his place in the corner spoke for everyone. Then his next words, breathed out like a sigh, fanned the unease already boiling inside them.

“With the mountains in such an uproar, the rivers will be in turmoil, too.”

And soon enough, his words became reality.

Two days after the two giants of the dark-path Murim faced one another.

* * *

If you asked whose the vast, boundless Yangtze was, those in the Murim would answer without hesitation.

Not one of the Five Great Families or the Nine Sects and One Gang—but the Yangtze River Channel League.

But those outside the Murim would give a different answer.

To them, whether you were talking about mountains or rivers, there was only one master of all things beneath the lofty sky.

The Son of Heaven.

And the Seafaring King, Pa Ryun, had never liked that one bit.

“When this old man was a child, an old man who lived next door told me that the Son of Heaven was descended from dragons, a child of Heaven who must be served with all one’s heart and soul.”

His voice was low, but full of force. His profound internal energy made the air tremble.

“He had a bad temper, but he was a decent enough old man. When I was orphaned by one bad harvest after another, he took me in for a while.”

Pa Ryun looked back on his past, lost in thought.

He had gone over it hundreds, thousands of times already, but it was full of nothing but bad memories.

He had lost both parents before he could grow a beard, and the time he spent in harsh servitude under the old man, just managing to keep food in his mouth, had been the best part of his life.

Of course, even that didn’t last long.

“It was a damnable time. More than ten fools called themselves kings, and the so-called imperial troops could raid villages in broad daylight, looting and killing, without facing any consequences.”

Pa Ryun stroked his sparse beard.

It was the same old story.

The old man had died then.

Not at the hands of a defeated army or bandits, but the imperial troops marching forward with sharp spears and tall banners.

The twelve-year-old boy, grateful to the old man, killed the soldier who had driven a spear into the old man’s frail body, then ran.

“I ran for three days and nights without stopping. In the end, I escaped their pursuit, reached a riverbank, and collapsed. Then a thought came to me.”

Pa Ryun pointed to the sky as he continued.

“There were so many people claiming the world belonged to them. If the so-called children of Heaven were like that, who was I supposed to serve?”

In the end, the long age of chaos came to an end.

A hero of the Zhu family unified the continent and announced to all under Heaven that he alone was the Son of Heaven.

By then, the boy had become a young man, and Pa Ryun had become a river pirate instead of a servant. Watching the new Son of Heaven ascend the throne, he found the answer to his question.

“That was when I learned that anything could be won with spears and swords. That only the last one standing could prove himself by the outcome.”

But Pa Ryun knew his own limits better than anyone.

He had neither the right to claim the world nor the strength to take it.

Still, he had been able to claim this great river.

And with it, hundreds of ships and thousands of men—enough to stand against the Great Nation’s warships, now visible in the distance.

“Raise the sails. The time has come.”

*Whoosh.*

Above Pa Ryun’s bright smile, a great sheet of cloth snapped in the wind.

As countless ships surged forward beneath it, the black-robed man at Pa Ryun’s side quietly curled his lips into a smile.
## Chapter artifact 1084

# Chapter 1084

The endless waves of the Yangtze roll on.

A line from a poem left behind by a poet who flourished in his time, long ago, and was called the Poet Sage.

He had revered the Yangtze’s waters—their distant history and their beauty in itself. A man sitting at the bow with his eyes closed felt much the same.

No. Naturally, he felt it even more deeply.

He had loved the Yangtze since childhood, become a river pirate, and in time made Ship-Fire Boy a name that symbolized him.

Boom. Boom. Booooom!

At the sound of drums spreading like ripples, the man opened his eyes. Mu Song—the Seafaring King’s second Disciple and Stronghold Lord of Water Dragon Stronghold—had been sitting with them closed.

“Stronghold Lord. The order has finally come.”

Mu Song nodded gravely. Even if he hadn’t heard his subordinate, he would have known better than anyone where that drumbeat came from.

*The Sea Dragon Ship.*

His Master, the Seafaring King Pa Ryun’s vessel.

In the final battle against the Yellow River Channel League, once their only rival, it had sunk dozens of ships all by itself. It was the mightiest vessel on the river.

And now, the Sea Dragon Ship—against which no one dared stand—was cutting through the current with the greatest martial artist on the Yangtze aboard.

It was headed for the Great Nation’s military vessels, the Yangtze’s other master.

No—the Yangtze’s master in all but name.

*But today will be different.*

Today, we’ll show them that we—the Yangtze River Channel League—are the Yangtze’s true rulers.

Mu Song muttered the words to himself and thrust his fist into the air. His subordinates roared, and the wind filled the sails.

*Whoooosh!*

The ship’s bow cut forcefully through the water.

Just as they charged toward the Great Nation’s vessels like horses across an open plain, something dark and grayish emerged between the vessels that had turned obliquely to face them.

“Fire!”

At that instant—

*Boom! Boom!*

More than a hundred Hongyi cannons[^1] roared at once.

A weapon only the Great Nation’s navy could possess—not some band of river pirates.

But even as lumps of iron capable of crushing a human body in an instant came hurtling through the air from two hundred *zhang* away, Mu Song’s eyes didn’t waver.

Because he was no ordinary river pirate.

*Whoosh.*

His form blurred for an instant. He kicked off the bow and shot forward.

The great saber in his hand traced a vicious arc toward the cannonball flying at him in a curve.

*Kaboom!*

Amid the thunderous blast, the recoil from deflecting the cannonball sent Mu Song back onto the bow. His grip tingled, and he shouted:

“Charge! Charge!”

“Waaaah!”

Fueled by the roar, the swift ships the Yangtze River Channel League was so proud of began to surge forward even faster.

Every river pirate gathered here today was a handpicked elite. Their oarsmen, all trained in martial arts, rowed with strength and speed, while the Peak masters stationed at the vanguard did everything they could to shield the ships from the hail of cannonballs.

Of course, there were limits they couldn’t overcome.

*Rumble!*

“Arrrgh!”

“The ship—the ship’s sinking!”

A tremendous boom swallowed their screams. Swift ships, shattered to pieces, began to sink all around them.

Hundreds of ships gathered together made one enormous target.

The League’s ships had been built for speed rather than durability, so their hulls were small and sleek. That also meant a single cannonball could easily send one to the bottom.

*Boom! Boom!*

Even so, Mu Song narrowed his eyes as cannonballs missed the hulls by a wide margin and slammed into the water.

*As I thought, they haven’t set up a proper barrage.*

The cannonballs just fired hadn’t all come at once on a signal.

No. They hadn’t done that even once since the first volley.

Despite the constant, deafening blasts, the League’s losses were minor compared with its full strength. He could even see military vessels sinking because their own cannons had misfired.

The enemy ships were firing at their own pace, not waiting for orders from the flagship. They looked as if something were chasing them, shooting as soon as they could get ready.

The river pirates had been tense, knowing full well the power of cannons. Now, some of them were beginning to smile.

“Stronghold Lord, they look flustered.”

“Shit. I nearly pissed myself, and now I just feel embarrassed.”

At his subordinates’ cheerful remarks, Mu Song nodded.

“Just as my Master said.”

“Pardon? The Chief Stronghold Lord—no, the Alliance Leader?”

“That’s right. He said they’d be caught unprepared, with peace having lasted so long.”

Mu Song thought the same as his Master.

A predator grew lazy once the hunt was over.

For a long time now, no one had risen to challenge the Great Nation, which ruled the continent like a mountain. The Yangtze River Channel League was only an alliance of river pirates, tolerated to a certain extent. And a long stretch of peace had a way of making people weak.

Of course, the Great Nation had an elite fleet that never neglected its training in case of emergency. But that fleet was on the sea, not the river.

Ever since the Great Nation unified the continent, the only enemies it had to watch for were foreign ones.

*We’ll win this battle.*

Just as Mu Song quietly repeated the words to himself, sure of victory, one of the chuckling subordinates suddenly spoke up.

“Still, there’s something that feels a little off.”

“What do you mean?”

“It’s not that I’m complaining, exactly, but…”

The subordinate scratched the back of his head, then added hesitantly:

“Are we really supposed to be doing this?”

“What?”

“It just doesn’t feel right. We’ve managed well enough up to now, so why stab the Murim Alliance in the back and join hands with those rotten bastards in Dark Heaven…?”

As he trailed off, looking uneasy, the other subordinates exchanged glances and chimed in.

“Well, Dark Heaven does stink to high heaven. The orthodox faction may talk shit about us behind our backs, but they’re not that kind of rotten.”

“Yeah, yeah.”

“Orders are orders, so it’s right for underlings like us to follow them. But still, it doesn’t sit right.”

The subordinates had been murmuring among themselves, but when they saw their leader’s expression stiffen, they fell silent. The truth was, Mu Song wasn’t at ease either.

*Are we really supposed to be doing this?*

The more he thought about what he’d just heard, the more bitter his mouth felt.

No—perhaps it felt all the more bitter because deep down, he knew better than anyone why they were doing it.

*Even if it’s my Master’s order… this doesn’t sit right with me at all.*

Mu Song had never once thought of himself as a *junzi*.

A river pirate.

Just as those two words implied, he was a thief. That was an undeniable fact.

But he had never crossed a certain line.

He never took from anyone who looked poor, and if one of his subordinates committed murder, Mu Song punished him severely on the spot.

*But this. This is…*

Mu Song looked out over the river, cloaked in thunder and chaos, and swallowed the words rising in his throat.

At the same time, a face suddenly came to mind.

*Blazing Flame Divine Dragon Jin Taekyung.*

He’d borrowed their swift ships so many times it was practically theft, then bossed them around like servants. He was a thief worse than they were, if anything. But Jin Taekyung was still a chivalrous hero.

The fearsome Fire King—and even the Slaughter Saint.

They had fought Dark Heaven, which had plunged the world into misery, and stood against injustice.

*Come to think of it, since I helped them, was I a chivalrous hero for a little while too?*

At the absurd thought that flashed through his mind, Mu Song bit his lip without realizing it.

It was a pointless thought.

Now that they’d come this far, there was nothing he could turn back by himself.

He and his Junior Brother, the Iron-Water Divine Dragon, had already voted against this. But their Master’s resolve had held firm after the First Disciple and several key Elders persuaded him.

*At last, the time has come. This is our one chance to become the Yangtze’s true rulers.*

That had settled everything.

It was an order from his Master and Alliance Leader, the Seafaring King Pa Ryun, a man as exalted as the heavens.

For a Disciple who trusted and followed his Master as if he were a god, there could be no further objections or idle thoughts. There couldn’t be, and there shouldn’t be.

He was a river pirate, and that was what he would remain.

“…We’ll finish this quickly. Everyone, get ready.”

Leaving his subordinates to watch him anxiously, Mu Song gripped the great saber in his hand with all his might.

The Yangtze, shrouded in thick cannon smoke rising even now, looked strange and unsettling, as if he were seeing it for the first time.

*Damn it.*

Swallowing the curse on the tip of his tongue, Mu Song recalled the line from an old poet’s verse—the one he’d repeated until he was hoarse, despite never even finishing the Thousand Character Classic.

Why were the waters of the Yangtze, which should have flowed so steadily as always, churning so violently and red?

His brief reverie ended as the shadow of a military vessel drew close.

*Rumble—crash!*

A tremendous impact.

The moment the swift ship’s sharp ram slammed into the side of the military vessel—

*Whoosh!*

Mu Song kicked off the bow and leaped up, bringing his great saber down in a powerful slash.

He was aiming at a group of government troops on deck, readying themselves for battle.

At the same time, he saw them clearly.

Their eyes, brimming with terror and tension. Their spears and blades trembling, their bodies frozen in place.

“…Damn it.”

Mu Song finally let the curse escape. At the last moment, he twisted the saber with all his strength.

The blade energy coiling along its edge vanished like smoke, and the keen blade tilted to the side.

*Thud! Thump!*

The soldiers crumpled limply with dull blows instead of sharp cuts.

“Huh?”

The subordinates who climbed onto the deck behind him stared at the scene, eyes wide. But before they could say a word, Mu Song’s quiet voice rang out.

“Don’t kill them. We’ll need men to row.”

The river pirates looked at one another blankly, then grinned.

“You all hear that? The Stronghold Lord says to leave them alive.”

“Of course. Who’d dare disobey an order like that?”

Everyone knew how flimsy an excuse this was.

But the Yangtze they wanted to see was nothing like this.

*Rumble! Boom!*

As the military vessels sank one after another in flames, as cries of agony rang out from every direction, Mu Song murmured silently to himself—toward his Master aboard the Sea Dragon Ship, far away, sinking everything in its path as it advanced.

*Is this what the Yangtze you wanted so badly is supposed to look like?*

That day, in just two *shichen*, the Yangtze River Channel League sank more than a hundred military vessels carrying thousands of government troops, then turned its ships west.

Somewhere far beyond the horizon.

And the astonishing news was enough to turn the world upside down.

[^1]: Hongyi cannons were large, European-style cannons adopted by China.

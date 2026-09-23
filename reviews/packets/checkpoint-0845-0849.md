# Checkpoint Review — 845–849

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

# Chapters 845–849

## Plot

The Divine Physician gives Jin Taekyung a pill and Jeok Cheongang helps its effects spread through his body. Jin’s condition improves, but his damaged vital essence cannot be fully restored, and pain in his lower dantian persists.

The Divine Physician is summoned to treat City Lord Won Gyun of Seongju Prefecture. Won’s illness began after the Son of Heaven took his favored concubine, Aehyang, but before the physician can treat him, the City Lord dies. At the City Lord’s Hall, the Divine Physician publicly supports a diagnosis of sudden death from emotional distress and weight loss. In private, he tells Jin’s trusted companions that he found Blood Soul Gu—a rare poison from deep in Nanman—in Won’s body.

## Continuity

- Jin’s recovery is incomplete: Jeok Cheongang’s treatment improved his condition, but his lower-dantian pain remains.
- City Lord Won Gyun is dead. The public explanation is sudden death from emotional distress and weight loss; the Divine Physician secretly identified Blood Soul Gu in his body.
- Who placed the poison and how it caused Won’s death remain unresolved.

## Translation Decisions

- Render 원기 as “vital essence” in the context of Jin’s injury.
- Render 고독 as “gu poison” and 혈혼고 as “Blood Soul Gu.”
- Render 추궁과혈 descriptively as “working the channels and pressure points”; keep 점혈 as “Pressure-Point Strike.”

## Durable state

{
  "active_continuity": [
    "Jin Taekyung remains incompletely recovered; Jeok Cheongang’s treatment improved his condition, but pain persists in his lower dantian.",
    "The Divine Physician secretly found Blood Soul Gu, a rare gu poison from deep in Nanman, in the dead City Lord Won Gyun’s body; the public diagnosis remains sudden natural death."
  ],
  "continuity_sources": [
    848,
    849
  ],
  "open_questions": [
    "Who placed Blood Soul Gu in Won Gyun’s body, and how did it contribute to his death?",
    "Will Jin’s lower-dantian injury improve further, or remain beyond full recovery?"
  ],
  "safe_through": 849,
  "temporary_decisions": [
    "Render 고독 as “gu poison.”",
    "Render 혈혼고 as “Blood Soul Gu.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 845

# Chapter 845

“Chew it thoroughly before you swallow.”

“Chew it?”

“Yes. Don’t swallow it whole, and don’t spit it out halfway through. Understood?”

The Divine Physician had come first thing in the morning and was now giving me his sternest warning. I let out a faint laugh and accepted the pill he held out.

“Of course. I’m not a child, and you made it for my sake.”

The pill was about the size of a marble and dark in color.

The Appraisal System was still inaccessible, so I couldn’t tell exactly what ingredients it contained or what effects it had. But the Divine Physician must have spent several sleepless nights making it.

The deep fatigue around his eyes was proof enough.

*He must have had plenty of other patients to care for, too.*

This pill had been made for me by the best physician in the world, at the expense of his own health and time.

Even if it were as hard as a rock, I planned to chew it until the sweetness came out. It was the least I could do.

And the moment I chewed the pill with heartfelt gratitude—

Crunch.

I realized that doing the right thing as a human being could go to hell. This wasn’t the sort of thing a human being could eat.

Ptooey.

The pill I spat out on instinct stuck fast to the Divine Physician’s pristine white robe.

He gazed sorrowfully at the pill he’d spent days making and muttered, “I told you not to spit it out…”

I was trying to hold on to my fading senses while retching when I opened my mouth, completely sincere.

“Sorry, but are you in your right mind?”

“I am, and I understand exactly how you feel.”

“Have you tried eating it yourself?”

“I haven’t.”

“Then you have no idea how I feel. None.”

“Medicine that’s good for you is supposed to taste bitter. It always is.”

“No, this wasn’t just bitter. Did you put poison in it or something?”

“Enough!”

Jeok Cheongang, who’d watched the whole thing from the side, bellowed and glared at me.

“He may not be particularly trustworthy and may seem a bit of a quack, but he made that medicine with care for your sake. Poison? Where did you get the nerve to say such blasphemous nonsense?”

“Sorry.”

“Don’t apologize to me. Apologize to that quack!”

“Sorry, Divine Physician. I misspoke.”

The Divine Physician—who was not particularly trustworthy and seemed a bit of a quack—looked silently back and forth between Jeok Cheongang and me.

I could practically feel his determination to stab one of us with a large acupuncture needle if only his martial arts were up to the task. Fortunately, his sobriquet was Divine Physician, not Divine Needle.

The Divine Physician took a deep breath, as if trying to suppress his murderous urge, then spoke in a calm voice.

“It’s all right. I’ve devoted my life to medicine. Isn’t it a physician’s duty to endure unfair and filthy treatment during a patient’s care?”

“……”

“……”

“Sometimes I do wonder what my Master would think if he were here, but it’s all right. I’m a physician, after all. I should expect a pill I spent several sleepless nights making to be chewed up and spat out. Ha ha ha.”

He did not look all right at all.

At this point, it wasn’t that his words had a barb in them. There was a needle as big as an awl hidden in there.

The Divine Physician’s eyes made Jeok Cheongang and me exchange Sound Transmission in silence.

—This is all your fault.

—If you hadn’t butted in back there, it wouldn’t have come to this.

—You asked the physician who brought you medicine if he’d put poison in it. What kind of thing is that to say?

—And what kind of thing is it to call him a quack?

—What’s wrong with that?

—He’s the Divine Physician. He might take offense.

—I’m the Fire King.

—I’m the Blazing Flame Divine Dragon.

—How dare a fucking nobody like you pretend you’re on my level?

—……

—Anyway, shut up and eat it. This is all for your sake.

Still, “weakling”? That hurt.

Jeok Cheongang glared at me, and then, making a show of softening his tone, addressed the Divine Physician.

“Don’t take it to heart. I’ll give the boy a proper scolding.”

“Then who’s going to scold Sir Jeok…?”

“Hm? What was that?”

“Nothing. I misspoke.”

The Divine Physician lied without a hint of remorse as he peeled the pill off his robe.

He stared mournfully at the clear tooth marks I’d left in it, then let out a long sigh.

“Some of the medicinal properties have seeped out, but it’s not too late. This time, chew it up and swallow it properly.”

One thing was clear: the medicinal properties weren’t the only thing that had seeped out.

Jeok Cheongang caught a whiff of the hideous stench escaping the crushed pill and instinctively stepped back.

“Could this be Formless Ultimate Poison…!”

“I’m done with this treatment. I’ll toss this pill in the latrine. Find yourself another physician.”

“W-wait!”

The Fire King grabbed the Divine Physician’s robe as he turned to leave, then asked in a nasal voice.

His other hand had already moved like lightning to pinch his nose shut.

“Ah, I didn’t mean to do that. Sorry. But this stench… What in the world did you put in this pill?”

“If I told you, would you even understand?”

“……”

“It’s a secret technique my Master taught me, so don’t press me on it. And don’t worry, it’s not poison.”

If I knew Jeok Cheongang, he would have let loose a string of curses and followed it up with a scorching Flame Divine Palm. But right now, the Divine Physician held all the cards.

We were the patient and his guardian, so we kept our mouths shut and nodded. Jeok Cheongang, in particular, urged me on with an expression half full of worry and half full of interest.

“Just do as you’re told. I’m here, so don’t worry about what comes next.”

“……”

The way he put it, it sounded like I was really about to swallow Formless Ultimate Poison.

I looked at Jeok Cheongang resentfully, then squeezed my eyes shut.

I blocked out my senses as much as I could and tossed the pill into my mouth.

Crunch, crunch, crunch.

My jaw moved without pause. I curled my tongue tight against the inside of my mouth to keep from tasting even a hint of it. And, for good measure, I added one heaping spoonful of desperate effort to keep myself from retching.

*Hnnngh.*

I felt like I was going to die. No, I wouldn’t have been surprised if I was already dead.

A hideous stench burst into my mouth with every chew.

Some unidentified, viscous juice slowly trickled down my throat, and my esophagus started doing the “Zero Two,” while my guts began doing the cocaine dance.

*Urgh, shit…!*

I swear, I’d never experienced a stench or a disgust this bad in my life.

Not even when I was a novice Hunter and fell with my nose buried in a goblin’s armpit in a Gate. Not even when I screamed and flailed my arms and legs, accidentally bursting the creature’s balls with my bare hands.

“Urk! Uuugh!”

My body moved on pure instinct, beyond reason.

I bent over like a shrimp and started to throw up something hot that surged from deep in my stomach.

Or I tried to.

If someone hadn’t clamped a hand over my mouth and nose at that very moment—

Crack.

The breath caught in my throat. I struggled on reflex, but the hand holding me fast wouldn’t budge, like glue.

And there was only one person here who could restrain me so completely.

*Old Master?*

I finally pried my eyes open, which I’d squeezed shut, and saw them.

Jeok Cheongang’s eyes, glowing red from the Scorching Yang Qi. And then came a powerful blow to my Adam’s apple.

Thwack!

Maybe because Jeok Cheongang’s hand was sealed over my mouth and nose, not a sound escaped me.

As my vision, which had just brightened, turned black, I thought:

*At this point, that medicine sounds more like poison than medicine.*

That was my last thought.

I felt the finely crushed pill mix with my saliva and flow deep into my body, and then I lost consciousness.

Whoosh.

Along with a heat more familiar than anything.

* * *

Jeok Cheongang didn’t panic or hesitate.

He had lived for a hundred and several dozen years.

He had passed the age of fifty, when a man understands Heaven’s will and the natural order, long, long ago. Jeok Cheongang knew better than anyone what he had to do.

*Now.*

His whole body roared with Scorching Yang Qi, but his mind was as cold as a glacier.

His face had grown heavy and still, as if he’d never once said anything frivolous. He reached toward the unconscious Jin Taekyung.

Whoosh. Tap. Dudududud—

His movements were as swift as a flash of light, his hands terrifyingly calm.

Each time Jeok Cheongang’s hands blurred, Jin Taekyung’s body jerked.

As he struck Jin’s pressure points, the Scorching Yang Qi seeped in, melting the pill and spreading its medicinal effects throughout his body.

*Don’t rush. Stay calm.*

Jeok Cheongang repeated the words to himself as if making a vow.

From this moment on, he couldn’t afford the slightest mistake. Humans didn’t die that easily, but the body was astonishingly sensitive.

All the more so when it housed the internal energy of several jiazi.

Rumble.

A tremendous heat raged around them. The floor of the pavilion, built of solid wood, charred black, and heat shimmered around the two men like a mirage in the desert.

Hssssss.

If an ordinary physician had witnessed the scene, he would have rubbed his eyes or screamed and run away.

But the Divine Physician was the one physician who did neither.

For decades, he had followed his Master and treated countless patients, gaining even more experience from his excellent teachings.

Of course, the fact that his Master was the Slaughter Saint was another major reason.

*It’s going more smoothly than I could have hoped. It’s hard to believe he’s performing something as difficult as this technique.*

The Divine Physician watched Jeok Cheongang, his eyes filled with wonder.

Working the channels and pressure points was not something anyone could easily attempt.

He had to sweep and strike the hundreds of pressure points in the human body while pressing and tapping them, opening blocked qi and blood channels and loosening knotted muscles.

That alone took enormous mental and internal energy. If he made even a single mistake, he could suffer a serious injury himself.

*And in this case, he also has to spread the pill’s energy throughout every part of the body.*

It was by no means easy.

No—it was exceedingly difficult.

Under normal circumstances, even the Divine Physician wouldn’t have dared attempt treatment this way.

But with the Fire King, Jeok Cheongang, it was different. He was the only one among the ten Supreme Peak masters known as kings throughout the world who could be compared to the Three Saints. And he was a Master who would take any risk for his only Disciple.

Just like his own Master.

*You’re doing well somewhere, aren’t you? Aren’t you?*

The Divine Physician had just thought of the Master he’d parted from four months earlier, almost as if he’d been forced to leave, and smiled faintly when—

Whoosh.

Through the slowly dissipating heat and haze, Jeok Cheongang came into view, rising to his feet with a slightly pale face.

“Sir Jeok. Are you all right?”

“Don’t make a fuss. I’m fine.”

“Even so, at least for a moment…”

“I’m fine. Look after that reckless brat first.”

From what the Divine Physician had seen, the treatment had been flawless.

And yet, after pouring so much effort into it, Jeok Cheongang was still consumed with worry.

That he would specifically ask the Divine Physician to examine Jin was not so much a matter of trust in the physician as it was a reflection of his boundless affection for his Disciple.

And the Divine Physician understood Jeok Cheongang’s feelings.

“Understood. I’ll examine him again.”

He answered calmly and approached Jin Taekyung, who lay collapsed. By the time he looked up again, half an hour had passed.

“It’s done. The medicine has been completely absorbed.”

Only then did Jeok Cheongang’s tired eyes come alive again.

“That means…”

“I’m sorry, but he’s still a long way from a full recovery. No—speaking for myself, I can’t guarantee a full recovery at all.”

“What?”

“You already knew, Sir Jeok. His vital essence has been damaged.”

“……”

“Even steel bends when it’s heated. In the end, it becomes a lump of molten metal. What chance does a body made of flesh and blood have?”

The Divine Physician looked at Jeok Cheongang with heavy eyes.

It was hard to meet his trembling gaze, but a physician who lied about a patient’s condition was no physician at all.

“Making this pill made me realize it once again. A full recovery is impossible, but improvement is possible.”

Grind.

Jeok Cheongang clenched his teeth.

He had suspected it since Nanman. But it was a truth he couldn’t bring himself to face.

*You foolish… foolish boy.*

What in the world had happened? How fiercely had he fought, again and again, in that place turning into a hellscape?

Jeok Cheongang watched Jin Taekyung, who had fallen asleep peacefully, his eyes trembling.

Then—

Crash!

The door flew open in a rush, and the rough sound of horses’ hooves rang out from beyond the window.
## Chapter artifact 846

# Chapter 846

Dududududu!

More than twenty horsemen charged ahead without slowing.

The faces beneath their low-pulled helmets were tense. White foam had dried around the mouths of their panting horses, but the riders never once eased their reins.

Not until they reached their destination, surrounded by stone walls like a fortress.

And the first thing to greet them was a wary shout.

“Stop!”

It happened in an instant.

At the shout from atop the stone wall, a dozen or so arrows flashed through the air and pierced the edges of the horsemen’s helmets.

Shaaak! Thunk, thunk, thunk!

Their accuracy was almost supernatural, and their force tremendous.

The horsemen’s eyes wavered as they saw the arrows quivering where they’d struck the ground.

A mistake?

No. A warning.

It was also a threat: if they ignored the warning and came any closer, the arrows would pierce their throats instead of the edges of their helmets.

“Gasp…”

Sighs erupted from all around.

The more than twenty horsemen stopped where they stood as if on cue. They couldn’t hide their fear, but the man at their center was different.

*As expected. The reputation is well deserved.*

The man stared up at the stone wall, his gaze a mix of admiration and tension. A group stood there with their bows drawn, backlit by the early morning sun.

Above their heads fluttered a banner bearing four characters written in one fluid stroke.

Sichuan Tang Clan.

The Nine Sects and One Gang. The Five Great Families. Fifteen pillars that upheld the Murim of today.

And among them, the most insular and cunning of all.

But…

*He’s here. Right here.*

The man steeled himself and stepped forward alone. Instead of a sturdy shield to protect him from the arrows that could fly at any moment, he raised a silver token high above his head.

“Don’t attack! I’ve come from Seongju Prefecture!”

* * *

“Who did you say?”

“Hwang. I’m the City Lord’s Captain of the Guards.”

“The City Lord? Ah, that sickly fellow?”

“…I don’t know who you are, but you’d do well to watch your tongue.”

“If you don’t know who I am, you’re the one who should watch his tongue. You look like you’ve spent a fair bit of time in Murim. How have you not figured out something that simple?”

The man—the Captain of the Guards—swallowed hard before he even realized he was doing it.

He’d been spoken to in a thoroughly provocative manner, but he didn’t feel offended at all.

No, to be precise, the other man’s attitude and presence felt so natural that it seemed perfectly right.

*Who is this man?*

For a moment, the Captain of the Guards forgot his mission and studied the man in front of him.

He wasn’t quite a giant, but he had a solid, well-proportioned build and a face that looked around forty.

On its own, he looked like someone one might encounter anywhere in Murim.

But his gaze was so piercing it bordered on menacing. Even the Captain of the Guards, who’d seen all sorts of people since his days as a wandering martial artist, flinched.

*And he’s bald.*

The Captain of the Guards saw the middle-aged man’s scalp gleaming in the sunlight and sensed danger.

The martial artists he’d known were, for the most part, people with something important missing.

Why would anyone with a carefree, happy life throw himself into this brutal, turbulent martial world?

And in that regard, the bald martial artists in the Captain of the Guards’ memory were especially hard to read.

They were just as lacking in something inside as any other martial artist—but, unfairly, they were missing their hair, too.

“Hey.”

“Yes?”

The Captain of the Guards jumped and answered on reflex.

His speech had slipped from polite address into outright deference so naturally that even he hadn’t noticed.

“You know me?”

“N-no.”

“Then why are you staring at my head like that? It’s making me uncomfortable.”

It was hard to say which was ruder: calling someone “you” and “that bastard” the moment you met, or staring at his head. But for the Captain of the Guards, who’d already sensed danger, there was only one option left.

“I-I’m sorry.”

“Some stray mutt barges in out of nowhere, running his mouth… At least you know when to back down.”

The Captain of the Guards felt aggrieved.

He didn’t know the middle-aged man, or anything about him. He’d ridden hard since early morning to meet someone else.

*How did things go this wrong? Was the information bad from the start?*

This meeting had been arranged with the permission of Tang Sadok, Family Head of the Sichuan Tang Clan. But the person he’d come to meet was nowhere to be seen, and across from him stood a menacing bald man staring right at him.

As if he meant to eat him alive.

But that was all in the Captain of the Guards’ imagination.

The middle-aged man—Jeok Cheongang—snorted and fixed his gaze on the Captain of the Guards, his eyes sinking into thought.

Uninvited guests showing up in broad daylight.

Normally, he’d kick them out on their asses. But if they were officials, that changed things. Especially if one of them was the Captain of the Guards, one of the City Lord’s closest men.

*I can guess why they’re here.*

Jeok Cheongang had eyes and ears.

No matter how little he cared about what was going on around him, rumors still reached him. He’d heard the stories about the City Lord, who’d been confined to his sickbed for a couple of months.

“You came to see the Divine Physician?”

The Captain of the Guards, who’d been on edge, stared at him in surprise.

At that moment, he was startled twice.

First, that the Divine Physician, whom even the imperial court had failed to find, really was staying at the Sichuan Tang Clan. Then again, that Jeok Cheongang would refer to the renowned physician as casually as if he were some guy next door.

“I wasn’t sure whether to believe it, but is he really here?”

“What an ill-mannered bastard. Answer what I asked first.”

“Y-yes.”

“Why? Is it because the City Lord is ill?”

“Yes. I don’t know if you’ve already heard, but… We’re here to treat the City Lord’s illness.”

“Surely you have plenty of physicians.”

“That’s…”

The Captain of the Guards hesitated for a moment, but not for long.

He didn’t know exactly who the middle-aged man in front of him was, but he was clearly a major figure in Murim.

The fact that he’d casually inserted himself into a meeting arranged by the Family Head of the Sichuan Tang Clan was enough to raise questions.

No matter how badly the Sichuan Tang Clan had been struck, challenging Tang Sadok—the Myriad-Poison Asura’s—authority wasn’t something a man would do on a whim. It would be madness.

And then Jeok Cheongang spoke one sentence, enough to make the Captain of the Guards the most honest man in the world.

“You don’t have to force yourself to talk. Once you’ve been beaten senseless, you’ll start remembering things you’d forgotten.”

“…!”

“I must be seeing things. Your mouth still looks shut to me.”

Deeply grateful that his subordinates weren’t here, the Captain of the Guards hurriedly opened his mouth.

“The City Lord’s condition is that serious.”

“Five.”

“Pardon?”

“That answer was worth five hits. I’ll take one off for every proper answer you give from now on.”

Is this man insane?

The Captain of the Guards’ legs trembled as Jeok Cheongang threatened him without so much as blinking.

He’d been a well-known master among wandering martial artists, but for some reason, he felt like he wouldn’t stand a chance against the middle-aged man before him, who looked to be about his age.

“Now, go on. Spit it out properly.”

Jeok Cheongang held out one hand, and the Captain of the Guards squeezed his words out.

“It’s quite different from what people say. Even the renowned physicians nearby have given up.”

“So? You have to have the Divine Physician?”

“Yes. After all the effort we’ve put in, there should have been at least some improvement. Instead, his condition keeps getting worse.”

“Then it must be a race against time.”

“It is. But…”

The Captain of the Guards licked his dry lips and continued carefully.

“The City Lord’s illness is a little—no, very strange.”

“Strange…”

Jeok Cheongang murmured and folded one finger.

“Four. Keep going.”

“Sometimes he’s conscious and can move about, but at other times he thrashes around like someone who’s gone mad.”

“Isn’t that because he has gone mad, rather than being like someone who has?”

“I thought so at first, too. The clear symptoms started right after he returned from the Imperial Capital.”

“The Imperial Capital?”

“Yes. He was summoned to court over the Blood Tragedy that happened four months ago.”

The Sichuan Blood Tragedy had caused an enormous upheaval, even from the perspective of a third party with no ties to Murim.

The relationship between the authorities and Murim might have been one of noninterference, but its effects couldn’t help but spread.

In Sichuan, which was unquestionably part of the Great Nation’s territory, more than ten thousand martial artists had fought one another.

Countless people had died or been wounded in the fighting, and the smoke from the cremation of the bodies afterward had lingered for more than three days.

“The rumors spread quickly. It happened not far from Chengdu, and there were so many witnesses, so of course they did. But the biggest problem was…”

Jeok Cheongang, who’d been listening quietly, tossed out a single word.

“Dark Heaven.”

“Yes. The court learned that the people called Dark Heaven had disguised themselves as government soldiers.”

“The higher-ups must have been furious.”

“I used to be part of Murim myself, but honestly, don’t authority and saving face matter wherever you go?”

Whether you lived by the sword or by the pen, people were still people.

In that sense, the dignity and authority of a unified dynasty that had been established after an age of fierce warring states were things one simply did not touch.

And yet Dark Heaven had damaged that very authority. In broad daylight, they’d walked the streets disguised as government soldiers and ultimately carried out a horrific massacre.

*That means…*

Jeok Cheongang sorted through his tangled thoughts and spoke.

“This is more interesting than I expected. Fine. Three. Go on.”

“After returning from the Imperial Capital, the City Lord fell ill. To be exact, it started on his way back to Sichuan.”

“The higher-ups must have given him a thorough dressing-down.”

“The court’s reprimand was part of it, but he also fell ill because he lost what he cherished most in the Imperial Capital.”

“Something he treasured most?”

“Yes.”

The Captain of the Guards answered briefly, then stared intently at Jeok Cheongang. At his three fingers, to be precise.

“…You’re a crafty bastard.”

“The City Lord wouldn’t have favored me otherwise.”

“Fine. Two.”

“Give me a little more. One.”

“Want to spend the rest of your life with one eye?”

“…”

“Fine. One.”

The Captain of the Guards stared at the last finger still raised and swallowed hard before speaking.

“His favored concubine.”

“His favored concubine?”

“Yes. Her name was Aehyang. He couldn’t bear to be without her.”

“If he brought her all the way to the Imperial Capital in that damn situation, I can guess how attached he was. So what, did he lose her on the street?”

“No. To be precise, a high-ranking person in the Imperial Capital took her from him.”

“Must’ve been someone pretty important to take the City Lord’s concubine. Who?”

“Well…”

At the Captain of the Guards’ hesitation, Jeok Cheongang folded his last raised finger. Then, at the unexpected answer, his eyes widened.

“The Son of Heaven.”
## Chapter artifact 847

# Chapter 847

The world was vast.

Yet just as the two characters that made up *天下*—“all under Heaven”—suggested, there was Heaven above it all.

The wide earth and the seas. The living and the dead.

Nothing could hide from Heaven.

Even birds that flew with the clouds across the distant sky, even humans who ceaselessly rose and fell and pointed blades at one another, all looked up at Heaven.

Wondering what magnificent being might dwell up there.

That was what Heaven meant to people.

An unknown realm they could only gaze at, never reach. Something they feared and revered in equal measure.

So perhaps it was only natural that the one who possessed all under Heaven came to be called the Son of Heaven.

The blue sky that looked down on everything in the world was the ultimate symbol of authority, after all.

*But even the Son of Heaven is just a man in the end. Look at him—stealing another man’s favored concubine and all.*

The astonishment from a moment ago vanished, replaced by a quiet laugh.

At the sight of Jeok Cheongang chuckling, the Captain of the Guards looked awkward.

“It wasn’t exactly a funny story.”

“No? From where I’m sitting, it was plenty funny. The man they even call the Son of Heaven steals his subject’s favored concubine, and the poor subject gets lovesick enough to hover between life and death.”

“……!”

The Captain of the Guards was so shocked he forgot to breathe.

He’d already guessed the man was crazy, but to say something so disrespectful about the Son of Heaven—

He hurriedly checked for anyone nearby, then managed to squeeze out a voice.

“A-are you insane? I don’t know who you are, but how dare you say that about His Majesty the Emperor…!”

“What, are you scared?”

“Do you even have to ask? Good heavens, if anyone else had heard you, you’d be charged with treason on the spot.”

“Hm. Treason, you say.”

Jeok Cheongang scratched his chin as he considered it.

Maybe not in the past, but now he was a Master with a Disciple, and a member of the Murim Alliance to boot.

“That could make things a little awkward.”

“Awkward? Do you think treason is some petty offense?”

“It’s not a crime so great that it warrants wiping out all nine branches of a family. The Son of Heaven is still a person made of flesh and blood. What’s the big deal if he gets insulted a little?”

“……!”

“Your face is a sight to behold. Heh heh.”

The Captain of the Guards stood frozen with his mouth agape. Jeok Cheongang slapped his knee and laughed.

He had lived for a hundred and several dozen years.

He’d seen with his own eyes the age of warring heroes, when the blood never dried, and the birth of a new unified dynasty.

The Son of Heaven—an object of awe and reverence?

What a joke.

For as long as he could remember, the title had never meant all that much to Jeok Cheongang.

*Just someone a little more extraordinary than others, with far greater ambition and cruelty.*

That was Jeok Cheongang’s assessment. And after hearing his one and only Disciple’s stories, he was even more certain.

He’d judged it right.

The Son of Heaven wasn’t bestowed by Heaven. He was born amid countless rivers of blood and heaps of corpses.

Jeok Cheongang suddenly remembered the stories Jin Taekyung had told him: astonishing tales of a giant iron bird taking to the sky and traveling among countless stars.

As he thought of them and watched the Captain of the Guards still standing frozen, he couldn’t help letting out another laugh.

“I understand. There’s a mountain of things even this old man doesn’t know. How could a little sprout like you begin to imagine them?”

“Th-this old man? Little sprout?”

“The world is vast, and the years keep passing. Maybe Dongfang Shuo, who lived through three thousand jiazi, could have watched it all change.”[^1]

The Captain of the Guards stared at Jeok Cheongang, dazed.

The man looked about his age, yet spoke in such a strange way. And none of what he was saying made sense to him.

“What on earth does that—”

The Captain of the Guards trailed off.

“You don’t need to try to understand. Anyone listening to a story like that would have the same questions.”

“……!”

At the sudden voice that slipped into his ear, the Captain of the Guards sucked in a breath and instinctively drew the sword at his waist, swinging it.

Or he tried to.

Until a terrifyingly immense energy erupted from somewhere and pressed down on his entire body.

Whoosh!

A wave of qi, hot as flames and heavy as a mountain.

The Captain of the Guards froze, not daring even to breathe.

His head had bowed beneath the force pressing down on it. His eyes trembled with agitation as he stared at his hand, still short of the sword hilt.

*H-how?*

Only the unanswered question drifted through the Captain of the Guards’ mind, bleached white with shock.

How could this be?

He’d left Murim to join the government in search of a comfortable life, but he was still a Peak master.

And not some hothouse flower raised in the shelter of a prestigious sect. He was a Peak master who’d come up as a wandering martial artist, hardened by real combat.

He’d spent more than twenty years as a wanderer.

He’d gone to war as soon as his first downy hairs appeared, and survived by turning into a stubborn weed.

He might not have learned the fine martial arts taught to the disciples of great families, but he was proud that his experience on the brink of death surpassed theirs.

And yet…

*If I move, I die.*

He could see it clearly. Feel it plainly.

The shadow of death drawing near. A towering wall he could never overcome, even if he were reborn again and again.

Drip.

At that very moment, a bead of cold sweat that had formed without his noticing ran down from the Captain of the Guards’ chin.

“It’s a hot day. That’s a bit much to put a guest through.”

Ssshhh.

At the calm voice, the heat scattered as if it had never been there.

The Captain of the Guards let out the breath he’d been holding and took several ragged breaths. In his ears, the sound of a conversation reached him.

“A guest? He’s just some nobody here to make a request that isn’t even worth calling a request.”

“Technically, he’s my guest. He came to see me, after all.”

“What kind of guest tries to draw his sword the moment he arrives?”

“I understand. Anyone could do that if they were startled while still reeling from shock.”

“Quiet. You’d better be grateful to this old man for keeping you safe.”

“I can’t compare to you, Sir Jeok, but I did learn a thing or two from my Master. You needn’t worry.”

“No, but this brat who doesn’t even have the blood dried on his head has been talking back to me all this time—”

“As a physician, I’d point out that if the blood in your head dries up, you die.”

“You—!”

The Captain of the Guards, listening to them, lifted his head in confusion.

Far from being a child with wet blood still on his head, an old man with snow-white hair looked at him with kind eyes.

“Are you all right?”

“……!”

In that instant, the Captain of the Guards recognized the old man by instinct.

He had the bearing of an immortal. And the conversation he’d just overheard contained all the answers.

“D-Divine Physician?”

The old man—the Divine Physician—smiled wryly and nodded.

“Yes, that’s right. This old man was late, and I ended up offending you without meaning to.”

“N-no! You didn’t offend me at all!”

The Captain of the Guards hurriedly waved his hands, then glanced nervously at Jeok Cheongang.

Meeting the Divine Physician at last was wonderful, but it was nothing compared to finding out who that terrifying bald middle-aged man was.

*Could it be…?*

The scattered pieces in his mind seemed to fall into place all at once.

The way he treated the Divine Physician, who looked to be well past seventy, like a child. The overwhelming force that had bound his entire body with nothing more than its release.

No—more precisely, the Scorching Yang Qi.

And, finally, what the Divine Physician had just called him.

*He said “Sir Jeok.” He definitely did.*

The Captain of the Guards swallowed hard.

It was nonsense. A crazy thought.

But he couldn’t help it. As far as he knew, there was only one person in all the world who fit all those details.

“Th-that person, could he be F-F-Fire—”

The Captain of the Guards stammered, unable to finish. Jeok Cheongang frowned.

“That’s right. I am the Fire King. Not the F-F-Fire King.”

“Eek!”

“……His reaction is somehow getting on my nerves. I feel like the Grim Reaper.”

At Jeok Cheongang’s baffled look, the Divine Physician was reminded of something his Master had once told him.

> “As a rule, it’s best to keep your distance from martial artists.”
>
> “Why?”
>
> “Of all the kinds of people in the world, they’re the most vile, violent, and—on top of that—stupid.”
>
> “Ah, I suppose that’s true to some extent.”
>
> “……What do you mean by that?”
>
> “Nothing. But I thought not all martial artists were like that.”
>
> “True. But steer clear of those who follow the demonic, heterodox arts. Ninety-nine out of a hundred are idiots.”
>
> “I’ve heard there are righteous heroes among the orthodox faction. Should I avoid them, too?”
>
> “If you can, yes. They talk about benevolence and righteousness, but half of them are idiots.”
>
> “Then what about martial artists who belong to neither the orthodox faction nor the ranks of those who follow the demonic, heterodox arts?”
>
> “They’re so unruly, and so many of them are unknown, that it’s hard to judge. But based on my experience, you only need to remember two things.”
>
> “What are they?”
>
> “The Fire King. The Fire Gate Clan. Repeat them and burn them into your mind.”
>
> “The Fire King. The Fire Gate Clan.”
>
> “Once isn’t enough. This time, say them and engrave them on your heart.”
>
> “The Fire King. The Fire Gate Clan.”
>
> “Good. Remember those two.”
>
> “I think I’ve heard the title Fire King before, but why do I need to remember it so well?”
>
> “Avoid him.”
>
> “Pardon?”
>
> “Never meet him, no matter what. If you hear a rumor that the Fire King has appeared somewhere while I’m away, leave the entire province.”
>
> “What? What kind of person is he that I’d have to go that far?”
>
> “A lunatic.”
>
> “……?”
>
> “The Fire King—or rather, the Fire Gate Clan—are lunatics who’ve spent generations fighting orthodox martial artists and followers of the demonic, heterodox arts alike. They beat people when they’re in a bad mood, when they’re in a good mood, and some days when they’re neither happy nor upset.”
>
> “……How can people like that exist?”
>
> “They do. There’s a mad sect that’s spent more than three hundred years breeding—no, producing—one generation of insanely strong lunatics after another.”

The Divine Physician remembered that day clearly.

His Master, who always kept his composure and was known as the greatest assassin of all time, had stressed just how dangerous they were by using the word “lunatic” three times in a row.

*Then why does Sir Jeok look so offended? Everything he said sounds right.*

Of course, the Divine Physician didn’t say that out loud. He had more important things to do—like stop Jeok Cheongang, who had grabbed the Captain of the Guards by the collar and was now shouting at him.

“Do I look that vicious to you? Huh?”

“Eek! N-no!”

“Then why is your voice shaking? Are you mocking me for being bald?”

“Eek! I-I didn’t! Please spare me!”

“If your voice shakes one more time, every last hair on your body is going to…!”

“Sir Jeok, that’s enough. Please calm down.”

The Divine Physician sighed as he stopped Jeok Cheongang, then spoke to the trembling Captain of the Guards.

“I heard most of the situation without meaning to, but to get straight to the point, I can’t leave.”

“Y-yes? Why not?”

“From what you’ve told me, the City Lord is suffering from a rather unusual case of lovesickness. As a physician, I have no choice but to care for those who are sicker and in greater pain.”

“B-but his behavior is so different from usual!”

“That’s only natural. He’s had the person he loves taken from him. How could he not be suffering? If my patients improve later on, I’ll come by then, even if it’s only once…”

The Divine Physician’s voice trailed off. His gaze shifted toward the slightly open door.

A hurried footfall and ragged breathing were drawing closer, loud enough for everyone there to hear.

Along with the unmistakable clank of armor—a sound seldom heard from a martial artist.

Tap-tap-tap! Clank!

Sure enough, before long, a figure clad in gleaming armor ran up and came to a halt in front of the door, nearly collapsing.

“You…”

The Captain of the Guards’ eyes widened when he recognized a subordinate who should have been back at the City Lord’s residence. The man sucked in a ragged breath and cried out:

“C-City Lord…!”

[^1]: Dongfang Shuo is a figure in Chinese folklore associated with extraordinary longevity; a *jiazi* is a traditional sixty-year cycle.
## Chapter artifact 848

# Chapter 848

Every now and then, I find myself wondering.

Just how often do I pass out? How many times?

If the System window summarized my life, how much of it would be time I’d lost while unconscious?

Damn it. I have no idea.

The important thing was that I’d just woken up—and found myself face-to-face with some ugly creature that looked like a monster.

“Whoa, shit! You scared me. Who are you?”

The monster answered in a mumbling voice.

“It’s me.”

“Me who?”

An unusual name I’d never heard before, attached to a face I wouldn’t want to see even in my dreams.

I asked again, baffled.

“Are you from the Sichuan Tang Clan, by any chance?”

“……”

“Is your name Tang Me?”

“Captain, that joke’s a bit much.”

Captain. The three syllables that came out of the monster’s mouth left me staring with my jaw hanging open.

There was only one person who called me that these days.

“Mujin? Hyuk Mujin?”

“Yes.”

“Good heavens, what happened to your face?”

“Someone beat me up.”

When you’re busy with life, it’s easy to forget the little things.

Only then did I remember pummeling Hyuk Mujin into the dirt a few days ago. I smiled warmly.

“Ah, I almost didn’t recognize you. You got so handsome.”

“Should I thank you?”

“If you do, I’ll gladly accept. But your face wasn’t this fu—this handsome when I last saw you.”

“Some lunatic tried to put me to sleep forever. I couldn’t do a thing.”

“A lunatic? Who?”

“Some guy whose only goal in life is to stuff himself until he bursts.”

Of the people I knew, only two lunatics came to mind.

Cheongpung. And Taishan.

Of course, Cheongpung was probably traveling all over the land with the Slaughter Saint, searching for traces of Dark Heaven. There was no way he’d just pop up at the Sichuan Tang Clan.

That left one lunatic.

“Can you see my face right now? That lunatic Taishan hit me before the swelling had even gone down. It got three times worse.”

“I get it, you’re three times more handsome. Now get your face out of mine. Or help me sit up.”

“Sorry, but I can’t. If I get any closer, I’ll smell your breath. It’s hard enough just standing here as it is.”

“What?”

At first, I didn’t understand what he meant.

Not until I noticed the terrible stench seeping into my nostrils.

“Ugh.”

I barely held back a gag and pushed myself upright.

As if he’d expected that, Hyuk Mujin nodded and handed me a waterskin and a scrap of cloth.

“It really stinks, doesn’t it? Plug your nose with this, like I did, and rinse your mouth out. And try to cover your mouth when you talk, if you can…”

“If you don’t want to get even more handsome, shut up. My stomach’s already turning.”

“Sorry. But your breath really is awful, Captain. What on earth did you eat?”

“Shit.”

“Good heavens, why would you eat that?”

“……”

Was that idiot Hyuk Mujin actually taking me seriously? Or was he just trying to mess with me even a little?

After a moment’s thought, I let out a deep sigh. I stuffed the scrap of cloth he’d given me up my nostrils and rinsed my mouth out several times. Only then did it feel like I could breathe again.

*Anyway, what exactly happened?*

My last memory was Jeok Cheongang forcing me to swallow that awful pill.

No—if I’m being precise, I’d felt a warmth seep through my body just before I lost consciousness.

A warmth more familiar than anything, as if I’d returned home.

That was why it felt warm rather than hot.

*It was Old Master’s Scorching Yang Qi. I’m sure of it.*

Just as not every color in the world is one of the seven colors of the rainbow, energy follows a similar principle.

I didn’t know how many clans in the world used Scorching Yang Qi, but its roots in the Fire Gate Clan were unmistakable.

The energy I’d felt had unquestionably belonged to Jeok Cheongang.

*Which means…*

I slowly looked around.

The place was as clean and tidy as when I’d first arrived. But the stench lingering in the air and the dark smudges on the floor were still there.

“It took ages to clean that up. It was sticky and smelled so bad I thought I was going to die.”

Hyuk Mujin, quick to catch my gaze, complained.

“According to what the Divine Physician left behind, it was the impurities in your body coming out in a mucus-like form. Um. What exactly did he call it? I knew the word, but it just slipped my mind. Push… push…”

“Pushing the meridians and passing through the acupoints.”

At my offhand reply, Hyuk Mujin nodded.

“Oh, right. That thing I’d only ever heard about.”

He could only have heard about it. Pushing the meridians and passing through the acupoints required extensive preparation and a willingness to make sacrifices. It wasn’t something people attempted lightly.

Not even masters who’d reached Supreme Peak were exceptions.

It took a tremendous amount of mental strength, and the practitioner had to infuse part of their own internal energy evenly throughout the other person’s body.

*And if it failed, the damage was severe.*

But Jeok Cheongang had performed the treatment while I was unconscious, accepting all that risk and the loss of internal energy.

It wasn’t the first time he’d treated me that way, but I couldn’t help feeling grateful—and guilty.

*…He didn’t have to go this far.*

If I’d been hovering between life and death, I might have asked him to. But until now, I’d been getting by just fine.

And we were in a situation where anything could happen at any moment. For everyone’s sake, it was better to preserve even a little more of the Fire King Jeok Cheongang’s strength than the Blazing Flame Divine Dragon Jin Taekyung’s.

*Of course, if I said that in front of Old Master, he’d tear into me.*

I let out a quiet laugh and drew up the Scorching Yang Qi. The increase in my internal energy wasn’t visible, but I could feel it at once.

*Slowly. Carefully.*

Like flowing lava, I spread the Scorching Yang Qi—now a little over three jiazi—through my limbs and every acupoint in my body. At the same time, I quietly surveyed everything deep within me.

My meridians were wider and sturdier. My blood had cleared now that the impurities were gone, and my organs were working normally.

I drew in a long breath and sent the Scorching Yang Qi flowing faster.

It didn’t take long for the slow-moving lava to become a blaze sweeping across a plain.

Sssshhhh.

Once around. Twice. Three times.

The cultivation that had begun as a Small Circulation became a Great Circulation. The fire dragon swept through hundreds of major and minor acupoints, putting my insides in order once more, then finally returned to my lower dantian and coiled up.

And just when everything seemed perfect—

Throb.

A sudden pain struck my lower dantian. I finished circulating my qi and clicked my tongue bitterly.

*So this still isn’t enough.*

The effects of that horrible pill the Divine Physician had made and Jeok Cheongang’s treatment must have been the best they could do for me right now.

But even with all their efforts, they hadn’t been able to heal me completely.

The price for using power my body couldn’t handle was bitter. No matter how much I regretted it, the cold reality wouldn’t change.

A vessel faced with more water than it could hold had only two choices.

Hold as much as it could, or break under the weight of the water pouring in.

I was in the latter situation.

“…It’s only a crack for now, though.”

At my involuntary mutter, Hyuk Mujin, who’d been standing guard, asked,

“Huh? What is?”

“You don’t need to know. It’s just something.”

“Wow, that’s cold. Where are you going to find a right-hand man as loyal as me?”

“As I’ve told you time and again, you’re barely my pinky toe.”

“Now that I think about it, that’s not so bad.”

“What?”

“Your pinky toe. It hurts the most when you stub it on a doorframe.”

“……”

Was it just me, or was that guy becoming a formidable opponent?

I was briefly at a loss for words. Then I shook my head and spoke.

“Cut the nonsense. Go fetch some water. I need to wash up. I feel disgusting.”

“Now?”

“Yeah. I can’t stand this smell.”

I wrinkled my brow at the stench clinging to my clothes. Hyuk Mujin scratched the back of his head.

“Um, Captain. That might be a little difficult.”

“What did you say?”

I blinked and asked in a serious voice,

“Are you talking back to me? Is your face itching because you want to be the most handsome man of all time?”

“Please stop hitting me. I’m begging you.”

“Then why are you talking nonsense?”

“I’m not talking back. I mean it’s going to be difficult time-wise. Everyone’s already prepared and waiting for you to wake up.”

“…Prepared? Waiting for me to wake up?”

“Yes. We’ll put up with the smell somehow, so let’s just leave now.”

What the hell was he talking about?

As I stared at him, bewildered, Hyuk Mujin hurriedly rummaged through his robes and pulled out a yellowed sheet of paper.

“What’s that…?”

“It’s a letter Sir Jeok and the Divine Physician left before they departed. They told us to get everything ready and bring you as soon as you woke up, without wasting any time.”

Jeok Cheongang and the Divine Physician had left ahead of us. They’d left a letter behind.

Trying to make sense of the questions that still wouldn’t go away, I unfolded the rough-textured yellow paper. At that moment, a single line written in a strikingly vigorous hand—presumably the Divine Physician’s—seared itself into my eyes.

> City Lord of Sichuan Province. Deceased.

“……!”

* * *

The Divine Physician suddenly remembered a lesson his Master had once taught him.

His Master had amassed a fearsome tally of killings—and rescued countless people from the brink of death.

*“What do you think is the most frightening illness in the world?”*

*“Cancer, I think.”*

*“Why do you think so?”*

*“Tumors too small to see with the naked eye grow deep inside the body. It’s fortunate if you notice the signs early, but unless you can find one of the most renowned physicians, people often die without ever receiving proper treatment.”*

*“You’re not wrong. But if you find a good physician at the right time, it’s an illness you can overcome without needing help from Heaven.”*

*“Isn’t that because you’re the Divine Physician, and a master of martial arts who’s reached the rank of Grandmaster?”*

*“No. Any physician whose skill I would recognize could do it. You included.”*

*“You flatter me, Master. But I still don’t know what answer you’re looking for.”*

*“Flesh that’s been gouged or torn can be stitched together. Twisted or broken bones can be set. Even if an organ is injured, you can open the body and examine it.”*

*“Ah, I understand now.”*

*“What is it?”*

*“An illness of the mind.”*

*“That’s right. A sickness of the mind can’t be seen, stitched up, or set. It kills patients more stealthily than an assassin and more cruelly than a fiend.”*

*“Then how should we treat people like that?”*

*“First, meet them as one person to another, not as physician and patient. Second, listen without a word. Third, become their friend.”*

*“And if even that doesn’t help, and the patient chooses to die…”*

*“Carefully prepare their body for burial, and see them off on their final journey. But whoever the patient may be, always remember one thing.”*

*“What is it?”*

*“There’s no such thing as a death without a cause. Find the cause first.”*

*“……!”*

The Divine Physician came back to himself and opened his eyes.

On the broad, lavish bed lay a corpse, sprawled as if in a deep sleep.

*City Lord of Sichuan Province. What caused your death?*

Was it the grief of having his beloved concubine taken from him? Or anger at himself for being powerless to stop it?

Or perhaps…

*Was it never lovesickness at all, but something else?*

The Divine Physician gazed down at the City Lord’s corpse, his eyes calm.

A renowned physician from Sichuan had already concluded that the high-ranking man had died suddenly. But after examining the body for more than three shichen, the Divine Physician disagreed.

*What grudge did you incur?*

Puk.

Along with a question that would never reach the dead man, a long needle was drawn from an acupoint.

The Divine Physician stared at the tiny thing writhing on its sharp tip and murmured,

“…A gu poison.”
## Chapter artifact 849

# Chapter 849

One shichen.

That was how long it took us to reach the City Lord’s Hall, which served as both his residence and his government offices.

Thudududud!

Stealing Ju Wongong’s carriage—no, borrowing it—had been a stroke of genius.

The six-horse carriage, luxurious enough to be obvious at a glance, possessed a kind of magic that made the horrific traffic jam disappear.

“Stop! Stop! Halt at once!”

“State your identity and business… Wait, I’ve seen this carriage somewhere before.”

We’d turned a crowded main road into an autobahn in the blink of an eye, so of course we stood out even from a distance.

The guards’ eyes went wide when they saw the carriage racing toward them like a mad thing. But a shout from somewhere gave them not even a moment to react.

“Open it!”

“Yes, yes?”

“I said open the gate, you idiots!”

“Y-yes, sir! Open the gate!”

Rrrrmmmble!

Had they been given orders beforehand?

There was no stopping the carriage, no inspection of the sort we should have gone through.

The enormous iron gates swung open to match the carriage’s rapidly approaching speed. Hyuk Mujin, seated on the driver’s bench, didn’t ease up on the reins until we’d passed through no fewer than five gates.

Whinny. Whinny.

The six fine horses, which had been galloping at full speed without pause, snorted roughly. Just then, unfamiliar faces approached me and the Fire Dragon Pavilion members as we climbed down from the carriage.

“Are you Young Hero Jin Taekyung, the Blazing Flame Divine Dragon?”

He didn’t waste a moment before asking, as if he had no time to spare.

Yet there was something subtly different about him from the usual government officials.

Even a military officer working for the government would generally avoid directly using someone’s Murim sobriquet like that.

*A martial artist?*

As I studied the man at the front, who wore lighter armor than the others, Song Ilseom’s Sound Transmission reached my ear.

— I know him. He won’t recognize me, though.

— You know him? Who is he?

— He was fairly well-known as a wandering martial artist. I heard he retired later on…but I didn’t know he’d left Murim altogether and joined the government.

— Really?

— Yes. My memory is accurate.

— Then why are you slipping into casual speech again? Are you older than me?

— I’m fairly sure I’m much older.

Oh, right.

I’d briefly forgotten that even by modern standards, Song Ilseom was a few years older than me.

But if I let that slide, discipline in the Fire Dragon Pavilion would fall apart. I sent a Sound Transmission with all the authority I could muster as Pavilion Master.

— So what if you’re older? Want to end up like Hyuk Mujin?

— ……

— If you don’t like it, you can be Pavilion Master.

Song Ilseom looked at me with a cold, flat stare, then sighed and shook his head.

The man at the front, a former wandering martial artist, spoke again. This time, he looked straight at me.

“Are you Young Hero Jin Taekyung?”

“That’s me.”

“Those who arrived before you told me to expect you. This way, please.”

After briefly introducing himself as the Captain of the Guards for the City Lord of Sichuan Province, he led us deep into the City Lord’s Hall.

“I presume you’ve already heard about the circumstances.”

I nodded as I walked behind him.

“To some extent.”

“You must have been quite taken aback.”

“At first, a little. I thought it was someone I knew.”

“Ah, do you mean the Acting City Lord?”

“Yes.”

There were currently two City Lords in this land.

No—there had been two.

Ju Wongong, a distant imperial relative with whom I’d had some history.

And the former City Lord of Sichuan Province, who’d been bedridden for the past few months.

*What was the name of the guy who just died? Won Gyun?*

It was such a memorable name for an extra that I couldn’t forget it. He sounded like the kind of guy who’d be a complete disaster at sea, even if not on land. Maybe it was because of that enormous belly that had looked like he was twenty months pregnant, not merely about to give birth.

“I don’t know if you remember, but I once saw you up close.”

“You saw me?”

“It was just before the Sichuan Blood Tragedy. You came to see the City Lord with His Highness Prince Shangshan’s token and asked for support.”

“Oh. Right. So you were there then, too?”

“Yes. As the Captain of the Guards, I stayed by the City Lord’s side. I never imagined something like this would happen back then.”

The Captain answered with a bitter expression and kept walking.

As befitted a place that was both the City Lord’s residence and the government offices where he worked, people in well-appointed official robes were everywhere.

“The atmosphere isn’t as tense as I expected. I thought there’d already been a big uproar.”

At Ju Hwaran’s murmur behind me, the Captain of the Guards nodded.

“That’s only natural. Those who work in the City Lord’s Hall knew at least part of the City Lord’s condition.”

The calm atmosphere on the grounds was proof that the City Lord’s death hadn’t come as a sudden shock.

But I didn’t take the situation at face value.

If it were as natural and ordinary as it seemed, there’d be no reason for Jeok Cheongang and the Divine Physician to get involved.

Besides…

*If they knew only part of it, that means there’s something that hasn’t been made public yet.*

How long had we been walking, with me lost in thought?

The farther we went, the fewer people we encountered. Even the guards, who’d been everywhere before, disappeared.

At last, the Captain of the Guards stopped in front of a magnificent stone building, more like an estate than a pavilion.

“This is where the City Lord was staying. I’d like to escort you farther, but I have orders to follow.”

“Orders?”

“Orders from the Acting City Lord. He said only two people, including Young Hero Jin, are to be allowed inside.”

Two people?

I could understand if it were just me, but I had no idea who the other person was supposed to be.

I frowned, puzzled, when an unexpected name slipped from the Captain’s lips.

“Is there someone among your companions named Namho?”

“Huh?”

“Mm?”

Everyone’s eyes widened as we looked in one direction.

The Captain of the Guards nodded as if he’d figured it out when he saw Taishan, the giant standing there with a blank expression.

“Ah, that must be Great Hero Nam. His bearing is indeed tiger-like, just as his name suggests…”

Thwack! Thwack!

Namho emerged from behind Taishan’s huge frame, panting as he hammered Taishan’s thigh with his two fists, which looked unusually tiny today.

“Move! I said get out of the way! You useless freeloader!”

“Heehee. Stop it, Namho. Taishan’s ticklish. Heeheehee.”

“Son of a bitch…!”

If he’d been an actual rock, maybe, but there was no way an egg could crack Mount Taishan.

Taishan giggled at the tickling. Namho was about to unleash a torrent of curses at him, but instead gave the Captain of the Guards, who was watching him, a hearty laugh.

“I’m Namho. The tiger from the south. Namho.”

“……”

“What’s with that look?”

“N-no, it’s nothing.”

“No, explain yourself.”

The Captain of the Guards looked Namho up and down as if he were staring at an ant from the south. Then, without saying anything more, he gestured to one of his subordinates.

Creeeak.

The doors swung open to either side with an irritating squeal, as if the new intruder wasn’t welcome.

Namho hurried up beside me as I headed inside and whispered,

“What’s with his reaction? Is a tiger that funny? Huh?”

“……”

Out of respect for my elders, I couldn’t bring myself to tell him the truth.

* * *

Maybe it was because of the City Lord’s lofty station, or maybe because of the corruption of the dead City Lord. Whatever the reason, the inside of the pavilion was truly spacious and lavish.

Clop. Clop.

Our footsteps echoed over the corridor’s expensive bluestone tiles.

A dozen or so men and women walking toward us bowed deeply to Namho and me, then passed by.

“Physicians and female physicians. Looks like they came to examine the body.”

Namho murmured, calm again as if nothing had happened. The moment he entered the pavilion, he’d begun taking in everything around him.

“Heh. They even embedded night-shining pearls in the ceiling. I can only imagine how much they squeezed the people dry.”

“I don’t know much about it, but even when I was in Sichuan, people didn’t have much good to say about the dead City Lord.”

“If the bastard who put up those expensive night-shining pearls was the City Lord who just died, then good riddance to him.”

“Maybe he bought them with his own money.”

“What does that mean?”

“He paid for them himself.”

Namho snorted.

“Sometimes, you really are a sheltered young master who knows nothing about the world. Let this old man teach you something. Those with money and power always…”

“Use other people’s wealth to fill their own bellies instead of spending what they have.”

“Huh? You know? Is that how it is in Shanxi Province, too?”

“Not always, but…it’s the same everywhere. That’s just how people are.”

Namho furrowed his brow at my answer.

“That’s odd.”

“What is?”

“Well, you said it yourself—it’s not something you experienced in Shanxi Province. You sound like someone whose hometown is somewhere else.”

The sharp instincts of a Hidden Shadow Pavilion agent.

Whenever Namho let this side of himself show, even for a moment, I could tell he had years of experience behind him.

*But he’ll never guess what the truth is.*

The things I’d gained from all the incidents I’d been through weren’t limited to martial arts skill.

I smiled casually and replied,

“Do you have to taste shit to tell it from black bean sauce?”

“Someone around twenty would do exactly that. It’s a phase everyone goes through.”

“Everyone goes through it, but not everyone earns the sobriquet Blazing Flame Divine Dragon around that age. Ah, this way.”

I answered nonchalantly and changed direction.

Namho looked at me with narrowed eyes for a moment, but then followed without another word. Meanwhile, I kept an ear out for the voices slowly drawing nearer.

— So, according to the Divine Physician’s examination, it was a natural death?

— It would be more accurate to say he died suddenly from emotional distress. His rapid weight loss was one of the main causes as well.

— I see. That’s why I kept telling him to lose some weight.

— …In any case, I agree with the other physicians’ diagnoses. There’s nothing particularly suspicious about the City Lord’s—or rather, the former City Lord’s—death.

— Ah, thank you. That Captain of the Guards has been making such a fuss that even I, this Young Master, was getting a little flustered. Now that the renowned Divine Physician of the realm has stepped in, it feels like I’ve gained a thousand troops.

— You flatter me. I only did what any physician should.

— Come now, too much modesty isn’t good either. Since you’ve handled this matter so well, I, this Young Master—or rather, this City Lord—will reward you handsomely. Someone, come here!

I rounded the bend in the corridor and answered,

“I’m here.”

“Immediately summon the steward and have him give the Divine Physician wealth and grain…”

His voice trailed off.

Ju Wongong stared at me, his face darkening rapidly. After a long silence, he finally spoke.

“When…did you arrive?”

“Just now. Got anything left to do?”

“……A little.”

“Then go. I have something to talk about.”

“……I still have some things to do.”

“Put them off. You’re obviously just going to spout nonsense.”

At my firm reply, Ju Wongong lowered his head sadly. Jeok Cheongang watched him walk away, his back limp, then spoke in a serious voice.

“If you’d been a quarter-hour later, I might have had the rare experience of tearing the mouth off a member of the imperial family for the first time in my life.”

“One thing I’ll ask you for, now and forever: don’t do that.”

“This old man isn’t that crazy.”

“……”

That’s exactly the problem. He seems crazy enough to do it.

I sighed deeply and turned to the Divine Physician, pretending not to hear Jeok Cheongang asking how I was feeling.

“So, what exactly is it?”

“What do you mean?”

“You wouldn’t have told that idiot everything, would you? And seeing both of you here tells me enough.”

At my indifferent reply, the Divine Physician smiled ruefully.

“As expected of Sir Jeok’s Disciple.”

What was that supposed to mean?

I was wondering whether I should feel pleased or offended when Namho’s eyes widened at the thing the Divine Physician pulled from his sleeve.

“That’s…”

“What is it?”

“Gu poison. A very rare kind, found only deep in Nanman. It’s called Blood Soul Gu.”

Jeok Cheongang nodded as he looked at it.

“Bringing that fellow here was worthwhile.”

# Checkpoint Review — 330–334

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

# Chapters 330–334

## Plot

Ju Hwaran and Song Ilseom determine that Heo Jun could not have ruined the Yongbong Escort Bureau alone. Hwaran begins investigating at least two collaborating escort captains, while Ilseom agrees to remain for one month before traveling to Xianyang for an elixir to treat Ju Hogun’s qi deviation.

Jin Taekyung’s party encounters Mu Song, lord of Water Dragon Stronghold and the Seafaring King’s second martial Disciple, on the Yangtze. After initially clashing, Mu Song carries the party from Guang’an toward Chengdu. During the journey, Mu Song defeats river bandits led by Hwang Tae-gu. He is about to execute Hwang when Mungyeong, a young medical apprentice whose parents Hwang killed and whose life Mu Song once saved, asks that Hwang be judged under League law instead. Mu Song destroys Hwang’s dantian and sends him to League headquarters for punishment.

After three days, the party reaches Chengdu and heads toward the Sichuan Tang Clan. Mungyeong joins them, having already demonstrated medical skill and courage by saving twenty passengers during the river-bandit attack. Jeok Cheongang remains unconscious and steadily weakens; Taekyung’s True Qi Guidance can only delay his decline, leaving the unknown Divine Physician as their only known hope.

## Continuity

- Ju Hwaran is purging the Yongbong Escort Bureau’s traitors. At least two escort captains may have collaborated with Heo Jun.
- Song Ilseom will remain at the bureau for roughly one month, then seek Ju Hogun’s treatment elixir in Xianyang.
- Mu Song is the Lord of Water Dragon Stronghold, a Peak master, and the Seafaring King’s second martial Disciple. His moderate faction controls major Yangtze traffic and seeks influence within the Yangtze River Channel League.
- Mu Song has negotiated controlled access to Chengdu and promised to send subordinates for Taekyung’s party’s return journey.
- Hwang Tae-gu is alive but has lost his dantian and martial arts. He is being transported to Yangtze River Channel League headquarters for punishment.
- Mungyeong is a compassionate Level 6 medical apprentice from a humble military household. He now travels with Taekyung’s party toward the Sichuan Tang Clan and hopes to become a physician.
- Jeok Cheongang remains unconscious on the pack frame and is steadily deteriorating. The Divine Physician must be found before his remaining treatment window closes.
- Taekyung still possesses the Thousand-Year Snow Ginseng.
- Taekyung gave Mungyeong travel money and invited him to visit the Jin Family of Taiyuan after becoming a physician.
- The Zhongnan Sect’s remaining conspirators and the organizers of the broader scheme remain unidentified.
- The identity of those who sought the Guangdong Chen Family’s Peak martial arts and the fate of the family’s other members remain unresolved.

## Translation Decisions

- Use **Water Dragon Stronghold**, **Yangtze River Channel League**, **Ship-Fire Boy**, **Sichuan Tang Clan**, **Divine Physician**, and **Xianyang**.
- Render **Mungyeong** for 문경, **medical apprentice** for 의생, **League regulations** for 맹규, **League headquarters** for 본단, and **qi-sea acupoint** for 기해혈.
- Preserve the distinction between destroying Hwang Tae-gu’s dantian and killing him.
- Render Mungyeong’s repayment vow as a Jeong Mong-ju allusion and retain the explanatory footnote.
- Use **Old Master** for 노야 when Taekyung privately addresses Jeok Cheongang and **Young Master** for 공자님 when Mungyeong addresses Taekyung.
- Preserve Taekyung’s **Bermuda Quadrilateral** joke.

## Durable state

{
  "active_continuity": [
    "Mu Song has carried Taekyung's party and Mungyeong from Guang'an to Chengdu aboard a Water Dragon Stronghold fast ship; the party is now heading toward the Sichuan Tang Clan.",
    "Jeok Cheongang remains unconscious on the party's pack frame and is steadily weakening; True Qi Guidance can only slow the decline.",
    "The Divine Physician, whose identity remains unknown, is the party's only known hope for treating Jeok Cheongang and is believed to be somewhere in Sichuan.",
    "Taekyung possesses the Thousand-Year Snow Ginseng.",
    "Mungyeong is a capable, compassionate medical apprentice who now accompanies Taekyung's party toward the Sichuan Tang Clan.",
    "Mu Song's moderate faction has negotiated a practical accommodation with Chengdu's authorities, and he has promised to send subordinates for the party's return.",
    "Taekyung gave Mungyeong silver travel money and invited him to visit the Jin Family of Taiyuan after becoming a physician.",
    "Ju Hwaran remains the Yongbong Escort Bureau's Young Bureau Head and is investigating escort captains who aided Heo Jun's scheme.",
    "Song Ilseom will remain for one month to help Ju Hwaran purge the bureau's traitors, then seek an elixir for Ju Hogun in Xianyang.",
    "The Zhongnan Sect's other conspirators and the organizers behind the broader scheme remain unidentified.",
    "The identity of the person who sought the Guangdong Chen Family's Peak martial arts and the fate of the family's other members remain unresolved."
  ],
  "continuity_sources": [
    334
  ],
  "open_questions": [
    "Can the Divine Physician treat Jeok Cheongang before his remaining window closes?",
    "What punishment will Yangtze River Channel League headquarters impose on Hwang Tae-gu, and can his connections still affect his fate?",
    "Which other Yongbong Escort Bureau members collaborated with Heo Jun, and how will Song Ilseom's Guangdong Chen lineage affect the bureau and the wider Murim?",
    "How will the Zhongnan Sect's Sect Leader and Elders respond to the exposed scheme and its consequences?",
    "Who sought the Guangdong Chen Family's Peak martial arts, and what happened to the other members of the family?"
  ],
  "safe_through": 334,
  "temporary_decisions": [
    "Render 선화아 as Ship-Fire Boy and retain Mu Song for 무송.",
    "Render 사천당가 as Sichuan Tang Clan, distinct from 사천당문 when the source distinguishes the family designation.",
    "Render 공자님 as Young Master when Mungyeong addresses Taekyung.",
    "Render 화타 as Hua Tuo.",
    "Render 노야 as Old Master in Taekyung's private address for Jeok Cheongang."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 330

# Chapter 330

Around midnight.

The four figures who had left the Yongbong Escort Bureau disappeared in the blink of an eye.

The members of the bureau who had come out to see them off shivered in the cold wind, but Ju Hwaran stood there without moving.

As if someone might come back if she waited just a little longer.

It was then that she heard a voice from the darkness.

“They’re gone.”

The escorts who had been startled by the voice that appeared without warning split apart to either side. Ju Hwaran, however, remained composed.

“Yes. They’ve left.”

“Are you disappointed?”

“I’d be lying if I said I wasn’t.”

“It can’t be helped. The people who are going to leave leave, and the people who are going to stay stay. That’s the way of things.”

“The way of things…”

Ju Hwaran murmured the words quietly, then slowly turned around.

“Which side is Captain Song on?”

“Me?”

Song Ilseom gave a quiet laugh and ostentatiously swung the travel pack over his shoulder.

“Which side do you think?”

“Is that why you pretended to have passed out drunk?”

“It’s been ten years. I’d say I’ve done my duty by now…but is that still not enough?”

“No.”

“…”

“It isn’t enough. You still haven’t done your duty.”

Song Ilseom’s brow furrowed at Ju Hwaran’s unhesitating answer.

“Still not enough? Even after I protected the Yongbong Escort Bureau—and you—for ten years?”

“Can that compare to the debt of gratitude owed for my grandfather’s lifesaving deed?”

“You…”

Song Ilseom raised his voice and took a step forward. The escorts nearby flinched and gripped their sword hilts.

They had not heard the hidden truth of his origins. To them, Song Ilseom was still someone they had to be wary of. In particular, the other two escort captains who belonged to the Dragon-Phoenix Three Escorts alongside him openly showed their hostility.

“Lower your voice. It won’t do you any good.”

“We don’t know what the Young Bureau Head thinks, but we’re not convinced. No matter how we look at it, there’s something suspicious about you.”

The two escort captains stood in Song Ilseom’s way with grim expressions.

“Enough. Step aside.”

At Ju Hwaran’s calm voice, the two escort captains stammered.

“Y-Young Bureau Head.”

“But this man hasn’t completely cleared himself of suspicion yet—!”

“I said step aside. I have something important to discuss with him, so everyone return to your posts and take care of the remaining work.”

“Hmm…”

“Y-yes, ma’am.”

The two escort captains moved their lips as if they still had something to say, then slowly nodded.

Song Ilseom watched their backs as they walked away with the other escorts. Then he clicked his tongue at Ju Hwaran.

“I can’t tell whether they’re loyal or stupid. They’ve come this far and still can’t tell friend from foe.”

“Your premise is wrong.”

“What?”

“They aren’t loyal or stupid, as you assume, Captain Song.”

A question flashed through Song Ilseom’s mind.

*Could it be?*

The insight came in an instant.

He was a born fighter and a martial artist through and through, but that did not mean he was stupid.

Once he understood the situation, Song Ilseom muttered quietly,

“Well, this is a real mess.”

Ju Hwaran nodded.

“They deliberately ruined escort missions and contracts, siphoned off funds in the confusion, and manipulated the ledgers with great care. There’s no way Uncle Heo did all of this alone.”

“Just how far does this conspiracy reach?”

“We’ll have to determine the exact number and identities from this point forward…but at the very least, we should include two people.”

Ju Hwaran’s gaze swept over the backs of the two escort captains as they grew more distant, then settled on Song Ilseom.

“I’m going to root them out completely.”

“Why didn’t you reveal it right there after the Chief Escort was killed?”

“The confusion would only have grown worse. Besides, if I can’t accomplish even this with my own strength, I have no right to become the Young Bureau Head of the Yongbong Escort Bureau.”

“Are you confident?”

Ju Hwaran stared at Song Ilseom in silence.

“How about putting away that travel pack you’re carrying and taking it out again a year from now?”

“You want to use me to root them out?”

“Captain Song, I need a blade sharp enough to cut down anyone right now. As it happens, the right person is standing right in front of me.”

“I refuse. And stop calling me Captain.”

“Then how about hiring the Soul-Chasing Guest?”

“What?”

Ju Hwaran shrugged.

“The Soul-Chasing Guest of the world won’t be cheap…but given your connection to our family, perhaps you’ll make an exception?”

“So I’m supposed to repay the life-saving kindness that way?”

“If that were the case, I would have asked for something much bigger.”

“A moment ago, you said I still hadn’t done my duty in return for the Escort King’s lifesaving grace.”

“That was because there were too many eyes watching us. My grandfather told me as well. He said that all he had done was save another person.”

“Ha!”

Song Ilseom burst out laughing.

Ten years ago, Junzi Sword Ju Hogun had said the same thing to the young man who had come to him carrying a faded jade hairpin.

“Though we met a generation apart, you came to find us in the end. That’s enough. Don’t let the ties of the previous generation bind you. Live your own life.”

“Pardon?”

“My father told me that what he had done was simply save another person. I feel the same way. And…thank you for growing into such a fine young man.”

It had been a shock.

From childhood onward, Song Ilseom’s life had been one continuous struggle. His parents had died young, and when his only support—his grandmother—passed away as well, he had to make his way alone without anyone to help him.

He had stolen weapons from piles of corpses, cut down wandering martial artists who tried to rob him of his rightful pay, and proven himself through countless life-and-death duels.

*I thought he would ask me for something.*

To Song Ilseom, who had lived as a wandering martial artist, that was only natural.

If Ju Hogun had wanted him to eliminate someone, Song Ilseom would have done it willingly. It would have left a bad taste in his mouth, but it was something he had always done.

One more among the countless requests he had completed.

But Ju Hogun had been different.

He was the first “adult” Song Ilseom had met after becoming an orphan with no one in the world.

Maybe that was why the words had slipped out before he could think.

“Ten years.”

“Hmm?”

“I’ll leave after ten years. Though all I know is how to kill people, I’ll protect you and your child no matter what happens. Just as the Escort King did several decades ago.”

Song Ilseom kept his oath.

He became an escort of the Yongbong Escort Bureau and faithfully followed orders. While he remained at the bureau, he followed the Chief’s daughter like a shadow and protected her at his request.

As the years passed and the child grew into a beautiful young lady, strange rumors circulated about the two of them, but he paid them no mind.

Whether the Chief collapsed or the Escort Bureau fell apart, Song Ilseom silently remained in place.

*I’m only doing my duty.*

Song Ilseom opened his tightly shut eyes. Then he abruptly spoke to Ju Hwaran, who had been watching him.

“I’m leaving in a month.”

“…”

“If you discover the identities of the traitors, I’ll lead the way and weed them out. A month will be enough.”

Seeing Ju Hwaran’s expression, Song Ilseom spoke bluntly.

“Don’t make that face. I’m only going to Xianyang to pick up an elixir and bring it back.”

“An elixir?”

“That’s right. It should be able to cure the Chief’s illness. The Thousand-Year Snow Ginseng was too potent and might have the opposite effect, but the elixir I obtained this time should definitely work.”

“H-how did you get an elixir like that…?”

“Enough. I’m tired of talking, so don’t ask any more questions.”

Song Ilseom waved a hand.

It was an elixir he had managed to acquire after searching for more than two years. It was not a legendary elixir like the Thousand-Year Snow Ginseng, but it was better suited than anything else to restoring the Chief, who had fallen into qi deviation.

He had been forced to pour every last bit of the enormous fortune he had earned as the Soul-Chasing Guest into it, but money could always be earned again.

“Do you know something?”

Song Ilseom’s calm voice continued.

“There’s nothing more difficult than saving a person’s life. What came naturally to you…was the hardest thing for me.”

Song Ilseom had made a living by killing people.

It was only after joining the Yongbong Escort Bureau that he began protecting someone instead.

“Captain Song…”

Ju Hwaran stared at him with moist eyes, but when she saw his furrowed brow, she hastily corrected herself.

“Ah, Great Hero Song.”

“How long are you going to keep getting confused?”

“I’m sorry. I was so surprised that I said it without thinking…”

“Then why don’t you create a position while you’re at it?”

“Pardon?”

“I don’t want to be Chief Escort. I’m terrible at escort missions, and that position requires managing people.”

“Yes, yes?”

“Guard Hall Master. Yes, that sounds good.”

While Ju Hwaran was still stammering, Song Ilseom turned around and began walking away.

Not toward the gate outside, where darkness had settled, but toward his own quarters.

“I shouldn’t have packed the travel bag.”

As she watched Song Ilseom’s back recede with those quiet words trailing behind him, dimples appeared beside Ju Hwaran’s mouth.

* * *

Whoosh!

With taut rigging and sterns slicing through the current, the fast ships surged forward like the wind. Men with their bronze-colored upper bodies bare pulled ropes and rowed oars. At least fifty men were visible on the deck of each ship.

There were five fast ships in all, meaning they had nearly three hundred men.

“Faster! Faster!”

“You louts! How can you call yourselves members of the Water Dragon Stronghold when you’re this slow?”

The Water Dragon Stronghold was a major river fortress belonging to the Yangtze River Channel League.

Its members proudly called themselves the heroes of the Yangtze, but the name used by ordinary people was a great deal less flattering.

“River bandits! They’re river bandits!”

“Why the hell are those bastards here?”

The shipmaster who spotted the five fast ships promptly collapsed into his seat.

His opponents were not some band of random thugs, but the Water Dragon Stronghold of the Yangtze River Channel League. There was no way to outrun their fast ships, and he could not even dream of fighting them.

*This day has gone completely to hell.*

No. There was only one way to get through this quietly, at least.

The shipmaster called over the youngest sailor passing by with a dejected look on his face.

“Hey!”

“Yes, shipmaster.”

“Tell the passengers to pay up.”

“Pardon?”

“Collect the money! They have to pay the toll, don’t they?”

The fact that they belonged to the Yangtze River Channel League was both unfortunate and fortunate. Once they were caught, there was no way to escape, but they did not simply swing their swords without reason.

The Yangtze River Channel League insisted that they were in a different class from the common river-bandit rabble found everywhere under heaven, but in the end, one was no different from the other.

“Phew… I’ve really lost today’s business.”

The shipmaster was sighing deeply when someone tapped him on the shoulder.

“Excuse me.”

“Gah! You startled me! Who are you?”

“I’m a passenger.”

“I know that.”

The shipmaster looked at the young man who had appeared out of nowhere. Judging by the sword at his waist, he seemed to be a martial artist, but…

*He looks kind of dumb. With that protruding mouth, he looks like he talks a lot, too.*

Third Rate martial artists were a dime a dozen.

It wasn’t as if he had never dealt with one or two of them before. The shipmaster sighed and opened his mouth.

“Why did you come over? If this is about collecting money, I have nothing to say, so go back to your seat. Don’t try anything stupid and end up crossing the Sanzu River.”[^1]

The young man watched the fast ships drawing rapidly closer.

“Are they river bandits?”

“Can’t you tell by looking? They’re the Water Dragon Stronghold of the Yangtze River Channel League. There isn’t a person in Sichuan who doesn’t know them.”

“The Yangtze River Channel League…”

“Running won’t help. You’ll never escape those fast ships. Once they spot you, it’s over. Completely over!”

“That ship must be pretty fast.”

“What kind of question is—”

The shipmaster was about to answer irritably when he suddenly sucked in a breath and closed his mouth.

A shadow rose behind the young man, a full head taller than him.

The man had shaggy hair, and a great mound of hides rose high above the pack frame on his back.

The giant stared blankly at the shipmaster, then spoke to the young man.

“Mujin.”

“Yes?”

“Let’s take that ship.”

The shipmaster wondered if he had heard correctly.

[^1]: The Sanzu River is a Buddhist river believed to mark the boundary between life and death.
## Chapter artifact 331

# Chapter 331

“Ship-Fire Boy”: a child who lights fires aboard a ship.

It was a term for a boatman. At the same time, it was also a sobriquet belonging to one man.

“Stronghold Lord.”

At his subordinate’s call, the man sitting cross-legged in the center of the cabin opened his eyes.

A crystalline light flashed in his gaze. Like any tough river man, he had bronze-colored skin and a muscular body. His bulging temples revealed that he was a Peak master who had reached a considerable realm stage.

“What is it?”

A deep, low voice flowed between his dry lips. His subordinate answered with the utmost respect.

“There’s a vessel fifty zhang away.”

“A vessel? Are they brothers from our alliance?”

“No.”

If that was the case, there was only one answer.

The mighty Yangtze held only those who took and those who were taken from.

“How many?”

“A little over fifty. It doesn’t seem to be a merchant ship, either.”

“I see.”

“What should we do?”

“Deal with it quietly. Don’t cause a commotion.”

With that, the man closed his eyes once more.

If it had been a warship sent by the imperial court, that would have been different. Otherwise, the matter was too trivial for him to intervene personally.

As always, his subordinates would handle it according to his orders.

*How dare they interrupt my meditation over something like this.*

The man let go of his irritation and sank back into contemplation.

It had already been more than ten years since he reached the Peak realm. Now, however, an invisible wall stood in his way.

He had tried consuming stolen elixirs and even smoking opium, which was said to reveal sights one had never experienced before, but it had all been a waste of time.

*This is going to be difficult at this rate.*

Water Dragon Stronghold was one of the ten largest strongholds in the Yangtze River Channel League.

Thanks to its location in Sichuan, through which vast quantities of goods passed, it was known as one of the most lucrative strongholds in the alliance.

But the man, who had only just entered his forties, harbored even greater ambitions.

*Alliance Leader.*

His goal was to become the master of the Yangtze River Channel League—and, with it, the king of the Yangtze.

Anyone unaware of the circumstances might scoff at such an absurd ambition, but the man possessed the ability and background to support it.

The proof was that, more than ten years ago, he had become the lord of Water Dragon Stronghold while only just past thirty.

“Whooo…”

The man drew a long breath. As he drew in and circulated the natural qi permeating the air, his sharpened senses gathered information from his surroundings.

The damp smell of water. The movement of the fast ship as it gradually slowed. Even the shouts and laughter of his subordinates.

“Hahaha! Running into us means you bastards have the worst luck imaginable. Who owns this ship?”

“I-I do, sir.”

“You launched your ship without the permission of us heroes, so I assume you’re prepared for the consequences?”

“I-I committed a crime worthy of death by failing to recognize the heroes of the Yangtze. This isn’t much, but please accept it as a token of my sincerity…”

Wham! Crash!

A blow landed, and someone went sprawling. The man’s brow furrowed at the shrill screams that followed.

*I told them not to make a commotion.*

No martial artist enjoyed having their training interrupted. His men might be rough and ignorant, but he had not expected them to be this incapable of understanding a simple order.

The man opened his eyes wide and was about to spring to his feet when—

Bang! Crack! Boom! Brrrrrap!

A series of savage noises rang out, and the surroundings fell silent.

*It seems to be over.*

The man, somewhat mollified, closed his eyes again.

Or he would have, if not for the question that suddenly flashed through his mind.

*But…why is it so quiet?*

Step. Step. Step.

Low, resonant footsteps approached the cabin.

At last, someone stopped directly outside the door and spoke in a voice laced with a yawn.

“What are you doing? Why aren’t you coming out?”

“……!”

It was an unfamiliar voice, one he had never heard before.

An alarm rang through the man’s mind.

*An enemy!*

Everything happened in an instant.

The man rose at the speed of a streak of light and shot toward the door.

His fist, carrying enough power to smash even a massive sailing ship, shattered the thick wooden door and raced toward the enemy beyond it.

And then—

Kraaaang!

A deafening boom and its aftershock shook the fast ship.

The man stared at the enemy with his eyes wide open.

More precisely, he stared at the palm that had stopped his fist.

A boiling voice escaped between his clenched teeth.

“Who are you?”

“Me?”

The young man answered with a faint smile.

“The owner of this ship.”

Flames poured from the eyes of the man known as the Ship-Fire Boy, Mu Song.

“How dare a little pup like you… I’ll show you the sky.”

* * *

I kicked the leg of the middle-aged man sprawled out on the deck.

“How long are you going to keep staring at the sky? Get up. Quickly.”

Focus returned to his hazy eyes. The middle-aged man propped up his upper body and stared at me with a dazed expression.

“H-how did you make such easy work of the Ship-Breaking Fist…?”

“Wait. Ship-Breaking Fist?”

Now I remembered.

I had definitely seen that martial art somewhere before, but my memory had been so hazy that I had been wondering about it.

I looked the middle-aged man up and down with renewed interest.

“What’s your relationship with Cheol Soo?”

“Cheol, Cheol Soo? Who are you talking about?”

“You know. Cheol Soo. Cheol Soo…”

Gung Gibang quietly cut in.

“The Iron-Water Divine Dragon.”

“Right. The Iron-Water Divine Dragon. When I met him at the Star-Array Grand Banquet, he kept going on about the Ship-Breaking Fist, too.”

If I remembered correctly, it had been during the first preliminary round.

He had gone on about how I should consider it an honor to witness the Ship-Breaking Fist, so I had smashed a cliff apart with the Flame-Extinguishing Divine Fist.

*I heard he forfeited after that and went straight home.*

In the Murim, it had happened only a month ago. But after everything I had been through, it felt like the distant past.

In any case, the middle-aged man before me had learned the same martial arts as the Iron-Water Divine Dragon, and he was a Peak master with skills a level above Cheol Soo’s.

The middle-aged man blinked like a goldfish, then asked in a trembling voice,

“W-were you acquainted with my youngest?”

“Your youngest?”

“The Cheol Soo you’re talking about is the youngest of us three martial brothers. He’s the third Disciple, and I’m the second.”

Huh. I had heard this before, too.

People had talked endlessly about the Iron-Water Divine Dragon’s Master.

“Then, could it be…?”

The middle-aged man nodded.

“That’s right. My Master is the one known as the Seafaring King.”

“Jang Bogo!”[^1]

“……?”

“No, it’s nothing. I was just talking to myself.”

“But why are you suddenly speaking so formally…?”

“Of course I should speak formally. You’re a Senior of the martial world and a hero of the Yangtze River Channel League. Please speak comfortably with me as well, Senior.”

To be honest, the Yangtze River Channel League and the Green Forest Alliance both looked like criminal groups full of social misfits to me.

But…

*If he was the Seafaring King’s Disciple, that changed things.*

If the Seafaring King heard that I had thoroughly beaten his Disciple to steal his fast ship, he would not be pleased.

At least the Green Forest Alliance’s Heavenly Axe had possessed a clear justification, so they could not say anything to us. But in this case, we needed to smooth things over.

I helped the dazed middle-aged man to his feet and brushed the dust from his clothes.

“Look how dirty your clothes are. What are we going to do? You’ll need to take them to the dry cleaner.”

“W-why are you suddenly acting like this?”

“I said you could speak comfortably with me. A minor misunderstanding on my part led to this unfortunate incident, but if I’d known you were with the renowned Yangtze River Channel League, I would have settled everything amicably with words. You understand, right?”

“……Really?”

“Of course. Do I look like some ill-bred junior who would lie to a Senior?”

The middle-aged man stared at me for a moment, then cautiously shifted his gaze upward.

I followed his eyes and saw a flag rising high above the fast ship.

The writing on it was large enough to be visible from a hundred meters away.

Yangtze River Channel League.

“…….”

“…….”

I slowly parted my lips.

“I’m illiterate. I can’t read.”

“…….”

Yes. I knew that excuse wouldn’t fly.

I clenched my fist and looked at the middle-aged man.

“Let’s just settle this amicably.”

“……Very well.”

* * *

Whoooosh.

The fast ship cut powerfully through the waterway. Cheongpung, who had been sitting at the bow and enjoying the wind, came running over, chattering excitedly.

“Benefactor! It’s so refreshing!”

“Of course it is. It’s still early spring.”

“There are so many fish, too!”

“There should be. We’re on a river.”

“There are so many people on the ship over there, and they’re getting beaten so much!”

“They should be getting beaten, of course—what did you say?”

What had I just heard?

As I questioned my ears, Cheongpung answered with a bright smile.

“Every time the captain swings that huge oar, skin is torn and blood sprays everywhere!”

“…….”

It seemed that Mu Song had lined up his subordinates and was beating them one by one with an oar.

They had mistakenly attacked a passenger ship and suffered a tremendous humiliation, so I supposed it was understandable.

“Pretend you didn’t see it. You didn’t see anything.”

“Can I ask him to let me hit one of them just once?”

“No. Please don’t.”

I ignored the looks from the surrounding sailors, who seemed to be wondering if Cheongpung was even human, and spoke to Gung Gibang.

“Hey, if you knew, you should’ve told me beforehand.”

“Am I some kind of fortune-teller? How would I know every single person stationed at every stronghold?”

Gung Gibang answered with an incredulous expression, then muttered,

“The crazy one is the bastard who charged in even after seeing the Yangtze River Channel League’s flag. And now you’re complaining?”

“Hey, I can hear you.”

“I meant for you to hear it. Even when I tell you something, you don’t fucking listen. What the hell do you expect me to do?”

“Damn, you’ve gotten awfully bold. What do you think of this insubordinate behavior, Mujin?”

Hyuk Mujin answered,

“Uweeeeeegh!”

“……Your seasickness is pretty bad. Go rest.”

For someone who was supposedly a First Rate master, he was still in terrible shape.

Cheongpung watched Hyuk Mujin cling to the railing and dry-heave over and over, then twisted from side to side.

“I want to get seasick, too. I’ve never done it even once.”

“…….”

You sure are lucky. You have so many things you want to try.

Maybe it was because I was on a boat, but today I was experiencing the power of the Bermuda Triangle all over again.

*Am I going to end up adrift on the Yangtze?*

I was thinking that when the massive Mu Song landed on the deck with a light, elusive movement technique completely at odds with his build.

He tossed the blood-soaked oar to one of his subordinates, then approached me.

“Are you uncomfortable anywhere?”

“Ah, yes. I’m comfortable, Senior.”

Mu Song’s gaze passed over Hyuk Mujin, who was still dry-heaving.

“That fellow doesn’t look very comfortable.”

“I’m comfortable.”

“…….”

“Is there a problem?”

“No, no. In any case, you’re headed to Chengdu?”

“Yes. How long will it take?”

“Our current location is Guang’an, which could be considered the entrance to Sichuan. At our current speed, three days. If we catch a favorable wind, two days will be more than enough.”

That was about the same speed as using a movement technique, or perhaps a little faster.

An ordinary ship would have taken much longer, but that was possible because this was one of the fast ships the Yangtze River Channel League prided itself on.

I sincerely clasped my hands in a respectful salute.

“Thank you.”

“What are you talking about? It was no trouble.”

Mu Song was cooperating because he had learned who our group was.

I was the Disciple of the Fire King, Jeok Cheongang; Gung Gibang was the Successor Beggar of the Beggars’ Sect; and Cheongpung had inherited the true transmission of the Sword Saint, Mae Jonghak.

And finally, the great Jin Family of Taiyuan’s…

Ah, let’s leave that last one out.

“In any case, Chengdu is close, so rest comfortably while you wait. This Mu Song has the rivers flowing through Sichuan firmly under his control.”

“Wow. That’s impressive, Senior.”

“Without my orders, no one dares do anything foolish on the Yangtze. Hahahaha!”

That was when faint cries drifted over from far away.

“Aaaah!”

“Kill them all and take everything!”

I muttered at the distant screams,

“They seem pretty good at doing foolish things…”

Mu Song’s face flushed bright red.

“How dare anyone cause trouble on the Yangtze!”

[^1]: Jang Bogo was a ninth-century Korean maritime commander, making him Taekyung’s spontaneous guess at the historical “Seafaring King.”
## Chapter artifact 332

# Chapter 332

“Who dares cause trouble on the Yangtze!”

I didn’t expect anyone over there to answer.

Ignoring Mu Song’s shout with one ear, I circulated my internal energy and sharpened my eyesight.

The distance was easily over two hundred zhang. But my vision had improved enough that you could call me a human eagle, allowing me to take in the entire scene at a glance.

*That’s…*

River bandits.

Two ships far larger than the fast ship we were riding had surrounded a tiny boat, while black dots resembling arrows and harpoons flew at it without pause.

When I spotted the flags fluttering from the bandits’ ships, my gaze naturally shifted toward Mu Song.

“I don’t know what kind of scum they are, but they picked the wrong target. You there! Immediately deal with those rootless bastards… What’s wrong?”

“Senior, how should I put this?”

“What is it?”

“Those rootless bastards. They seem to belong to the Yangtze River Channel League.”

“……?”

“……?”

After a brief silence, Mu Song shouted,

“That’s impossible!”

“It’s not impossible. The flag says ‘Yangtze River Channel League’ in very bold lettering.”

“Didn’t you say you were illiterate a moment ago?”

Was he a river bandit or a razor blade? He had a surprisingly sharp side.

Instead of panicking, I hardened my expression and said,

“I’m a fast learner. Besides, is that the important thing right now? We need to punish those lawless thugs disrupting order on the Yangtze as quickly as possible!”

Mu Song looked like he wanted to punish me first, but he wholeheartedly agreed with my opinion.

“That’s right. In this day and age, how dare they commit murder on the Yangtze… I’ll kill those bastards with one blow!”

It was lamentable that those words had come from the mouth of a river bandit chief, but according to something Gung Gibang had casually told me, Mu Song belonged to the moderate faction within the Yangtze River Channel League.

His principle was that taking money was enough. There was no reason to take lives, too.

“……”

No, he was still taking the money.

Come to think of it, there wasn’t much difference between them after all. Still, in a Murim where people reached for their swords whenever they got bored, he really was more conscientious than most top-tier river bandits—especially one who was a Disciple of the Alliance Leader of the Yangtze River Channel League.

“Raise the red flag!”

At the booming command of their leader, Mu Song, five fast ships raised red flags signifying battle and charged forward at tremendous speed.

Whoooooosh!

The sails swelled taut in the wind that happened to blow at just the right moment. Modified to achieve maximum speed, the fast ships cut through the waves without hesitation, rapidly closing the distance.

When the two-hundred-zhang gap shrank by half in an instant, an urgent shout rang out among the river bandits preparing to attempt a boarding attack.

“F-fast ships!”

“Mu Song of Water Dragon Stronghold has appeared! Everyone, retreat!”

But Mu Song was not the sort of man to let them retreat in peace.

The distance between us and the enemy was already barely fifty zhang. As he glared at the bandits hurriedly returning to their ships, a sharp light flashed in his eyes.

“Let’s at least see what you bastards look like!”

With a teeth-grinding sound, Mu Song seized a massive harpoon, kicked off from the stern, and leaped into the air.

Boom!

The sturdy wooden deck splintered. At the same time, Mu Song’s body shot out in an arc and was roughly swallowed by the Yangtze.

*Isn’t that dangerous?*

It would be a mistake to think of the Yangtze as some valley stream in Gangwon Province.

Although this was a branch of the Yangtze that split away from the main channel, it was as wide and deep as the sea, and the current was viciously rough.

That was why even Hyuk Mujin, who had been dry-heaving, asked with a pale face,

“Shouldn’t we rescue him—ueeegh!”

“Gibang, pat that guy on the back.”

“I’m no nanny…”

Even Gung Gibang wasn’t a nanny. Who would hire a beggar as one?

Despite grumbling, Gung Gibang pounded Hyuk Mujin’s back and said,

“There’s a limit to ignorance. Do you think a river bandit chief would jump into the Yangtze without learning water-based martial arts? Especially a Disciple of the Seafaring King, who no one can match in the water?”

“Ah, right.”

“I don’t know who they are, but they picked the worst possible target. There’ll be funerals one after another today. Tsk, tsk.”

Gung Gibang’s prediction was accurate.

A few seconds later, Mu Song emerged from the water more than ten zhang ahead of the fast ship.

Spla-aaash!

Every time his massive body traced a supple curve like a wave, he surged forward like a water skier. My mouth fell open on its own.

“This can’t be happening!”

He was even faster than the fast ship.

Watching Mu Song charge toward the enemy vessel with the appearance of a fish-man, I felt my own blood begin to boil.

“Since it’s come to this, I’m going, too!”

Gung Gibang screamed,

“Going where?”

“Uweeegh!”

“Benefactor, me too!”

“Get lost, all of you! The Grand Line is calling me! The Yangtze is calling me!”

Shaking off the Bermuda Triangle, I raced across the deck and launched myself from the bow with all my strength.

Boom! Crack!

The bow shattered under the force. My body was swept up in weightlessness as wind slammed fiercely into my face.

Whoooooosh!

“Freedom! Freedom!”

I became a bird, then quickly lost momentum and began to fall.

“Senior!”

“Gasp!”

Tap!

I landed lightly on the back of a fish-man who happened to be passing by.

The angle and speed, the distance, the point where I would fall—all of it had been calculated perfectly. That was the only reason the result had been possible.

“Whew. Per-fect.”

“What part of that was perfect!”

Mu Song shouted at the unexpected free rider, but there was nothing he could do about it now that I was already aboard.

I glared at the river bandits hurriedly turning their ship around and shouted,

“Let’s go!”

“Damn it! Since it’s come to this, we’ll charge straight into the ship!”

“Yes, that’s my Senior!”

“We’ll settle this after it’s over!”

Spla-aaash!

Gritting his teeth, Mu Song increased his speed even further.

The river bandits had only just found their footing and were desperately trying to escape, but it was already too late.

We had become a single harpoon, shooting toward the side of their ship.

“Go, Senior! Fish-Man Jujutsu: Current—One-Arm Shoulder Throw!”

“Yaaaargh!”

Mu Song and I shouted at the top of our lungs as we thrust out our arms at the same time.

He held a harpoon, and I held a spear, but we had one thing in common.

Powerful qi gathered at the tips of both weapons.

Whoooooosh!

The two currents of Spear Energy cut through the wind and pierced the damp, sturdy side of the ship.

The next moment—

Kwaaang! Rumble-rumble-rumble!

A tremendous shock wave erupted along with a thunderous roar.

* * *

“Mujin.”

At my solemn voice, Hyuk Mujin finally stopped retching and answered with a pale face.

“Yes?”

“I think I may have the constitution of a river bandit.”

“What kind of nonsense is that?”

“Do you want to hear the wails?”

“I made a verbal mistake because I’m not feeling well. Thinking about it again, you do seem suited to it.”

“Right?”

“Yes. I can still vividly see the way you recklessly—no, courageously—pierced straight through the ship.”

“It was exhilarating.”

I nodded smugly and gazed at the ship that was slowly sinking.

On one side, Mu Song’s men were using the small skiffs carried aboard the fast ships to pull river bandits from the water, where they thrashed helplessly.

On the other ship, the river bandits had their heads hanging low and were being transferred to the fast ships one after another, bound together with ropes.

*One ship sunk. The other captured.*

That was an excellent result for my first naval battle.

Originally, I had planned to sink both ships. But the river bandits lost their will to fight as soon as they saw the ship carrying their comrades sink, and they surrendered.

Of course, even after surrendering, their ending was not particularly good.

“How dare scum like you tarnish the name of the Yangtze River Channel League?”

No matter how moderate Mu Song was, he was still a martial artist who had no qualms about killing and a river bandit who had lived his entire life on the harsh Yangtze.

Once Mu Song lost his temper, nothing could hold him back.

“Throw them to the fish.”

The tightly bound river bandits opened their eyes wide.

“T-this can’t be happening!”

“Stronghold Lord! Please, anything but that!”

But the only answer they received was Mu Song’s cold gaze.

“Stronghold Lord? The strongholds you belong to are different from mine. Why would I be your Stronghold Lord? And don’t worry. Your chief will be joining you soon, so you won’t be lonely.”

“We were wrong! Please, just this once…!”

“If you invaded Water Dragon Stronghold’s territory to carry out this kind of act, you should have been prepared for this much. Do you know why I had my men pull you from the water? So I could punish you with my own hands.”

At a jerk of Mu Song’s chin, his subordinates approached and dragged the river bandits away.

As the presence of death drew close enough to touch, the river bandits screamed. But their limbs had already been bound, and they sank beneath the surface with a series of splashes.

Cheongpung bit his lip with a pale face as he watched more than fifty river bandits being drowned alive one after another.

*It makes sense.*

Someone who was afraid even of blood had no chance of enduring a sight like this.

Concerned despite myself, I spoke to him quietly.

“Close your eyes. I’ll tell you when it’s over.”

“No, Benefactor. I’m fine.”

“They may deserve to die, but you’re still watching people die. It might be hard to see.”

“No.”

“Hm?”

Cheongpung’s eyes twitched as he opened his mouth.

“I’m just… trying to get used to it.”

Get used to it? I had never expected Cheongpung to say something like that.

Cheongpung was naturally kind-hearted, and unlike other young men his age, he had not been tainted by the ways of the world.

Perhaps that was why he had been afraid of blood and avoided killing. But now, I could feel a firm resolve within him.

*Was it the battle with the Blood Lord at Mount Song? Did it begin then?*

The fear and terror of death he had experienced for the first time must have awakened something inside Cheongpung.

I was proud of him in one way, but bitter in another.

*It can’t be helped. This is the Murim.*

That was right. This was the Murim—a Murim where the winds of war were gathering.

He could not remain an innocent mountain youth forever in a place like this.

*If he managed to grow even this way… maybe it was for the best.*

Cheongpung stubbornly forced strength into his eyes, which were about to close, and let out a sigh of relief. The river bandits had finally been dealt with.

But everything was not over yet.

“Hwang Tae-gu. It’s your turn now.”

Mu Song’s low voice rang out across the deck.

Unlike the other river bandits, a man in his fifties had been forced to his knees before Mu Song, tightly bound in chains.

Hwang Tae-gu was the mastermind behind this incident.

Gung Gibang muttered as he watched him.

“I was wondering why Mu Song was here. So that’s how things turned out.”

“What do you mean?”

“The Nine Sects and One Gang and the Five Great Families have their factions. How much more so would a group of river bandits like the Yangtze River Channel League?”

“That Hwang Tae-gu lost a factional struggle?”

“He was famous for being greedy and violent. Just a few years ago, he lorded over the Yangtze in Sichuan… There’s no doubt Mu Song pushed him out.”

So a loser in an internal power struggle had gone rogue and finally been caught?

I was thinking that when Hwang Tae-gu opened his mouth.

“I have nothing to say to a young brat who knows nothing about the ways of the world. Kill me.”

“You won’t need to say anything for your wish to come true. But why did you do something like this?”

“Heh heh. What a stupid question. I’m a river bandit. What’s wrong with a river bandit killing and taking whatever he wants?”

“There’s no reasoning with you. I should have killed you sooner.”

That was the moment Mu Song hardened his expression and raised his harpoon.

“Great Hero Mu Song, the Ship-Fire Boy, would you wait a moment?”

A voice suddenly rang out, piercing the ears of everyone present.
## Chapter artifact 333

# Chapter 333

“Great Hero Mu Song, the Ship-Fire Boy, could you wait a moment?”

I wanted to give the owner of that voice a standing ovation.

Think about it. Who could say something like that in a situation like this?

Especially when the person they were addressing was a river-bandit chief who had thrown more than fifty river bandits to the fish in five minutes.

But who was it?

*Judging by the way he called him a Great Hero, he obviously isn’t from this line of work.*

Mu Song’s subordinates called him Stronghold Lord or Chief, so they were excluded. None of my companions, myself included, had said a word, so they were out too.

That left…

*The passengers who were attacked by the river bandits.*

Everyone here had clearly arrived at the same conclusion as I had.

My companions and I. Even the river bandits of Water Dragon Stronghold. Everyone’s gaze turned in one direction—toward the twenty passengers who had moved onto the fast ship when their boat began to list under Hwang Tae-gu’s attack.

“Who is it? Step forward.”

At Mu Song’s fierce glare, his harpoon hanging low in one hand, his subordinates hurriedly cleared a path. There was one person at the end of it.

“It was me.”

I had guessed as much from the voice, but he was quite young. No, he even looked boyish.

*Twenty at most, if I’m being generous?*

The word boy suited him better than young man. Flustered by everyone’s attention, he hesitated, then awkwardly clasped both hands together.

“I-I’m Mungyeong.”

“Mungyeong?”

Mu Song frowned.

“That’s a name I’ve never heard before. And judging by your appearance, you’re not a martial artist either.”

Mu Song’s eye was accurate.

The aura surrounding the boy, Mungyeong, was that of an ordinary commoner. No more, no less.

Mungyeong swallowed nervously under our scrutiny and answered,

“T-That’s right. I’m merely a medical apprentice still in training. I have no connection to the Murim.”

“A medical apprentice? Then how do you know me?”

“How could I not know that there is a righteous boatman on the Yangtze in Sichuan who strictly punishes those who take lives?”

Talk about shameless flattery.

Mu Song’s mouth twitched as he went from a river-bandit chief who controlled the waterways of Sichuan and shook down travelers to a righteous boatman in the blink of an eye.

“Hmm. Is that so?”

“Wealth may come and go, but a life is something you have only once. Those who know how many lives disappeared on the Yangtze until just a few years ago call you the Great Hero of Benevolence and Righteousness.”

“Hem. There’s no need to go that far. I’m satisfied with being called the Hero of the Yangtze.”

*What a load of horseshit…*

Mu Song was reasonably sensible, but he was still a river bandit. Acting like a thug within reason didn’t make him a model citizen.

But the young medical apprentice seemed to see things differently.

“My parents died tragically on the Yangtze more than ten years ago. If Great Hero Mu Song hadn’t saved me, I would have met the same fate.”

“Oh, dear. That’s unfortunate. But if it was more than ten years ago…”

“That’s right.”

Mungyeong continued in a trembling voice.

“The man kneeling before you is my parents’ killer.”

“Huh.”

The river bandits and passengers who had been listening intently let out low groans. Mu Song nodded as if he understood and spoke.

“Now I understand why you asked me to stop. It may go against the rules of our League, but I can understand your feelings well enough. I’ll give you a chance.”

“You mean you’ll give me the right to decide whether he lives or dies?”

“Of course.”

But Mungyeong’s answer went beyond everyone’s expectations—including mine.

“Then… please let him live.”

“……!”

“……!”

Mu Song had been about to hand Mungyeong the harpoon he was holding. Even Hwang Tae-gu, who had already closed his eyes as though resigned to everything, snapped them open and stared at Mungyeong.

“W-What did you say?”

When Mu Song asked again in confusion, Mungyeong bowed at the waist.

“I desperately want to avenge my parents, but I am a medical apprentice. How can someone who deals with life bring about death? I beg you to cripple his martial arts and punish him according to strict law, so that he can never commit evil again.”

“By your own words, that bastard will be escorted to the League’s headquarters. He deserves to die, but with all the connections he’s built over the years, he might save his own life. Wouldn’t it be better to take your revenge with your own hands, right here?”

“I have no connection to the Murim, but I have heard that losing one’s martial arts is tantamount to death for a martial artist. I have not killed him, but would that not be the same as killing him already? And…”

Mungyeong looked straight at Hwang Tae-gu with clear eyes.

“This is not personal revenge, but a matter of the greater good. If the Yangtze River Channel League directly punishes him, wouldn’t it serve as a warning to others who commit slaughter?”

There was no trace of trembling left in the boy’s resolute voice. It held a strength that made everyone listening nod along.

Exclamations rose from the people watching.

“Goodness. What an extraordinary young fellow.”

“If it were me, I’d have shoved that harpoon straight into his chest.”

“He’s an impressive one. He’ll make a fine physician.”

Mu Song also seemed deeply moved by Mungyeong’s clear and orderly words. He nodded with admiration and walked over to Hwang Tae-gu.

“You heard him if your ears are working. What do you think?”

“I-I’ll survive, and I’ll tear every one of you apart!”

The killing intent flashing in Hwang Tae-gu’s eyes did not last long.

Thud!

“Guh!”

Mu Song’s toe had driven into the spot below Hwang Tae-gu’s navel—the place called the dantian.

Mu Song looked down coldly at Hwang Tae-gu, who toppled backward, vomiting blood.

“Go ahead and survive. Then do as you please. Your dantian is shattered, so even if you live, you won’t be much of a living man.”

With a sharp crack of air, the foot that had flown forward struck his dantian again.

Whooooom! Crack!

“Guh! N-No!”

By the time Hwang Tae-gu’s scream echoed hollowly across the deck, everything was already over.

Ssshhh.

*I can feel it.*

The writhing qi flowing from his seven apertures was scattering into the air.

When a cup holding water breaks, the water spills out. The moment his qi-sea acupoint was destroyed, the internal energy stored in his dantian disappeared.

“You bastards, I’ll definitely—!”

The Peak master who had once ruled the Yangtze in Sichuan while commanding countless ships no longer existed.

Hwang Tae-gu had become nothing more than a powerless man in his fifties. He continued shouting without pause until Mu Song’s Pressure-Point Strike left him rigid.

“What a noisy bastard. Throw him somewhere out of the way. We’ll escort him to headquarters later.”

“Yes, Stronghold Lord.”

A bald, copper-skinned river bandit who looked like Diglett hoisted Hwang Tae-gu onto his back and disappeared, bringing the incident to an end for the time being.

Mu Song scratched the back of his head and looked around.

“Well, this is awkward. I’ve shown you all an ugly sight. To everyone who suffered because of this incident, I offer my sincere apologies.”

*So a good bandit defeated a bad bandit?*

In any case, the commoners who had been saved by Water Dragon Stronghold’s arrival bowed repeatedly.

“Oh, no, not at all. Without the Heroes of the Yangtze, we would have died without a chance.”

“We don’t know how we could ever repay this debt…”

“Perhaps the Primordial Heavenly Venerable was watching over us. Not a single person died, so you needn’t worry.”

*Huh? Not a single person died?*

At those words, I looked over the passengers.

*It’s true.*

There were injured people here and there, but no corpses.

I and Mu Song had arrived before the fighting became a full-scale melee, but arrows and harpoons had definitely been fired from a distance.

*How had a mere twenty commoners all survived?*

The question that occurred to me was answered soon enough.

“If that young medical apprentice over there hadn’t been here, we might all have died.”

“That’s right. How could anyone remain so calm in a situation like that? He’s truly remarkable.”

The conversation I overheard went like this.

When the people spotted the approaching river bandits and fell into confusion, Mungyeong stepped forward. He had them tear up the deck and use the boards as shields, then had them break the mast.

*The deck is one thing, but he had them break the mast?*

An ordinary person would have thought first of rowing for their lives and escaping. Mungyeong was different.

He broke the sails and left the boat’s fate to the violent current of the Yangtze, which heaved and rolled like a whirlpool.

*And it worked.*

I knew roughly how naval battles worked.

After firing at one another from a distance, the usual tactic was to close in and ram the other boat, or throw ropes across and attempt to board for close combat.

But if the target had completely lost the ability to steer and was spinning and pitching wildly, it would be difficult to find an opening. Mungyeong had bought them time.

*Well, look at this guy.*

His decision regarding Hwang Tae-gu was impressive, too. He was no ordinary clever boy.

Perhaps he felt my gaze. Mungyeong, who had been smiling awkwardly at the praise directed toward him, flinched.

“Y-Young Hero. Did you need something from me?”

“What do you mean, need something? Judging by your age, you’re young enough to be my little brother. I was just thinking you’d done something really impressive.”

“Th-That’s too much praise.”

“I heard you were pretty bold. How did you come up with that?”

“Although I’m walking the path of a medical apprentice now, before my parents passed away, I read all kinds of miscellaneous books.”

“Miscellaneous books?”

“Yes. Believe it or not, my family comes from a humble military household. My grandfather was also a military officer who received a stipend from the court.”

He was trying to hide a faint wariness toward a stranger, along with a quiet sense of pride.

Seen that way, he wasn’t much different from any other boy his age.

But something about him didn’t sit right.

I studied Mungyeong carefully and muttered inwardly,

*Skill, use Qi Sense.*

Ding.

Along with the familiar chime, information about him rose into the air.

> **System**
> **Lv. 6 Mungyeong**

“I guessed wrong.”

“Pardon?”

“Nothing. Stay healthy, eat well, and grow up strong.”

“Y-Yes…”

I clicked my tongue inwardly and turned away from the bewildered Mungyeong.

Mu Song, who had been watching, spoke to me quietly.

“What is it?”

“Nothing important. I just became a little interested in him.”

“Junior, do you happen to have a taste for men?”

*You fucking bastard…*

When he saw my expression, Mu Song cleared his throat and changed the subject.

“Ahem. In any case, we should continue on our way. The current is rough, but the wind is favorable, so we should reach Xi’an soon.”

“What about the others? The boat they were originally on was listing, too.”

“The others? Ah, my men will move them safely to somewhere secure.”

Mu Song chuckled and added,

“Of course, we’ll accept a small token of their appreciation.”

“……”

Saving their lives and shaking them down for money. Was that clever or stupid?

I was momentarily speechless at this novel form of creative economics when—

“W-Wait a moment.”

“Hm?”

It was Mungyeong. He glanced around nervously, fidgeted with his fingers, and opened his mouth.

“Um, did you say you were going to Xi’an?”

“That’s right. Why?”

Mungyeong gasped and rapidly spilled out his words.

“The thing is, I happen to be on my way to Xi’an too. If you would give me a ride just this once, I’ll repay this kindness even beyond the grave, remember it to my very bones, and even if this body dies and dies, dies a thousand times over and turns to white bones, I will never forget—”

*What is this?*

I let out a long sigh at the Jeong Mong-ju villain.[^1]

“Fine. Get on.”

“Thank you!”

As Mungyeong hurried off to gather his luggage, Mu Song muttered under his breath,

“Wait, this is my ship…”

*Yeah. No.*

[^1]: Jeong Mong-ju was a Goryeo scholar-official remembered for a famous vow of loyalty that repeats dying over and over before becoming white bones.
## Chapter artifact 334

# Chapter 334

Time flowed like a river.

It was a common and worn-out metaphor, but the three days I spent aboard the fast ship had been exactly that.

*Thanks to this ship, we cut down our travel time by quite a bit.*

True to the name Yangtze River Channel League, Mu Song and the river bandits of Water Dragon Stronghold were all outstanding sailors. They knew the lower reaches of the Yangtze, which ran throughout Sichuan, as well as the palms of their hands.

“We’ll be there soon, Old Master.”

I stared at Jeok Cheongang’s wrinkled face and murmured.

Only a few weeks had passed, but his already small and thin body was gradually weakening.

I realized it every time I used True Qi Guidance to bolster his qi, just as I had today.

*Recovery is impossible. For now, slowing it down is the best I can do.*

The only reason he could endure like this was that he was a Supreme Peak master with profound internal energy.

And… our only hope was one person whose medical skills had reached the realm of the gods.

*The Divine Physician.*

A mysterious figure whose face, name, age, and even gender were unknown.

The Divine Physician first became known more than forty years ago, though, so I figured they had to be over sixty.

*I’ll find the Divine Physician no matter what… and wake you up.*

So please wait just a little longer.

Just as I added those words in a voice too quiet for anyone to hear, light footsteps approached. A murmured conversation drifted through the gap in the cabin door.

“Stop. Stop. Stop. Move, and I’ll cut you.”

“Gasp! Please don’t cut me! You know who I am.”

“I do. But I won’t let even one rat past me. That includes some youngster who rolled in from who knows where. You could be an assassin, for all I know.”

“An assassin? I’m a medical apprentice! What an outrageous thing to say!”

“Then what brings you here?”

“G-Great Hero Mu Song asked me to deliver a message.”

“Impossible. Unless you can get past Hyuk Mujin, the Vice Squad Leader of the Jin Dragon Squad of the great Jin Family of Taiyuan, no one can—!”

Bang! Thud!

Mungyeong’s jaw dropped at the sight of the Vice Squad Leader of the Jin Dragon Squad of the great Jin Family of Taiyuan collapsing after hitting his head on the corner of the door.

“He’s dead.”

“He’s not dead.”

“B-But a blow like that must have caused serious damage to his head…”

“Enough. What did Senior Mu Song tell you to say?”

The boy looked back and forth between Hyuk Mujin and me with a terrified expression before answering.

“H-He said you’re almost there, so you should get ready.”

“Oh, is that right? Fine. Gather your things, too.”

“I’m already finished.”

Mungyeong’s belongings were sparse.

He pulled acupuncture and moxibustion supplies from the small bundle he had been hugging tightly, checked Hyuk Mujin’s condition, and sighed in relief.

“Fortunately, there aren’t any tears.”

“That’s because his head’s made of rock.”

“As expected of martial artists…”

“Oh? Getting cheeky, are we?”

“Gasp! I misspoke!”

I made a gesture as though I were about to rap him on the head, and Mungyeong flinched.

A quiet laugh escaped me.

“I’m kidding, you idiot.”

“You startled me.”

Traveling aboard a fast ship that moved day and night was surprisingly exhausting.

Whenever I had finished circulating my internal energy and thinking through martial arts, I wandered around the deck to get some fresh air. Every time I did, I saw Mungyeong.

*He was always checking on everyone else’s condition.*

He was a good kid. He also seemed quite skilled, because even the river bandits who had been skeptical at first often approached him shyly to receive treatment.

*After talking with him a few times, he seems cheerful, too.*

Contrary to his mature first impression, Mungyeong had a lively, boyish side.

After hearing about our identities from someone, he seemed to have become interested in the Murim and began asking all sorts of questions.

*“Young Master Jin, you’re the Disciple of Great Hero Jeok Cheongang, the Fire King? Wow!”*

*“I’ve heard plenty about Great Hero Mae Jonghak, the Sword Saint. Young Master Cheong must be incredible, too.”*

*“Wow! The Beggars’ Sect! The Successor Beggar!”*

*“You’re the Vice Squad Leader of the Jin Dragon Squad? Ah, yes…”*

In any case, Mungyeong had naturally blended into our group over the short span of three days.

*Once we reach Chengdu, this will probably be the last time we sit across from each other and talk.*

Our paths would naturally separate once we arrived.

I grabbed Mungyeong by the shoulder as he stood on tiptoe and peeked over mine.

“Ow! That hurts!”

“What are you so curious about that you’re craning your neck like that?”

“Nothing. I just thought I saw someone’s foot through the gap in the door.”

The boy had a sharp eye. I had hurriedly covered the exposed part with leather, but he had somehow managed to see it.

Still, I answered casually without showing any sign of panic.

“You imagined it.”

“I don’t think I did…”

“Mungyeong.”

“Yes?”

“Do you really want to see what’s inside?”

At my ominous tone, he swallowed hard and began backing away.

“W-Why are you acting like this?”

“I asked you a question. Do you want to see it?”

“No. No, I don’t want to.”

“Why not? Come inside and take a look. It’ll be fun.”

“Eek!”

Thump! Bang!

Mungyeong backed away, stepped on Hyuk Mujin, and fell over before scrambling to his feet and fleeing.

Hyuk Mujin, whose back had been stepped on in the confusion, opened his eyes.

“H-Huh? I was just talking to Mungyeong.”

His bewildered face hardened with shock as he looked around.

“I didn’t even see him launch his attack. He must be an assassin who has reached the Peak realm!”

Smack!

“Argh! Why did you hit me?”

“Stop talking nonsense and gather your things. We’re almost there.”

After giving Hyuk Mujin a good whack on the back of the head, I returned to the cabin, moved Jeok Cheongang onto the pack frame, and went out onto the deck.

A giant standing at the stern of the slowing fast ship turned around and called out to me.

“Oh, Junior.”

“Yeah, Senior.”

“…Is it just me, or have your answers gotten shorter?”

“It’s entirely your imagination. My voice is naturally a little quiet.”

Mu Song, the giant, stared at me with a dubious expression before calling over one of his subordinates and giving an order.

“Lower the blue flag and raise the white one.”

“Yes, Stronghold Lord.”

It might sound like some kind of blue-flag, white-flag game, but this was the signal system used by Water Dragon Stronghold. Apparently, it meant that they were sending a message that they would not cause any trouble.

“Forgive me if this is an impertinent question, but are river bandits really allowed to come this close to such a busy area?”

“It is an impertinent question, but I’ll answer it anyway. Yes, we are.”

“How?”

“Can you see it?”

Mu Song pointed toward the pier that was slowly drawing closer.

Tall wooden buildings stood packed tightly together, while commoners passing by either glanced at the fast ship and continued on their way or looked at it with curiosity.

Although we were still far from the center, Chengdu was the capital and central city of Sichuan. Even so, that was the extent of the people’s reaction.

“Well? Doesn’t everyone look accustomed to this?”

“They do. It’s strange how little attention they’re paying us.”

“It wasn’t like this at first. Hwang Tae-gu, that bastard, had done so many things before I came along.”

His teeth ground together as he continued.

“I went through hell trying to change people’s perception of us. Well, at least the authorities turn a blind eye to us to some extent now.”

“The authorities? You mean the officials of the Great Nation?”

“That’s right. To be honest, it must have been uncomfortable for them to deal with us, too. Formally requesting a fleet from the court would have been troublesome, but keeping their guard up every time they encountered us would have exhausted everyone. So we reached a compromise.”

“What kind of compromise?”

“I’m different from Hwang Tae-gu. Only a complete idiot kills powerless commoners every time he gets the chance. It’s like killing our own customers with our own hands.”

“…”

“Of course, that’s because I dislike killing. Not because of money.”

I didn’t find that very convincing.

No matter how I looked at it, the only reason Mu Song didn’t kill people seemed to be money.

*What a money-mad river bandit.*

I couldn’t deny that Mu Song had a talent for shaking people down.

In any case, unlike Hwang Tae-gu, who robbed and killed indiscriminately, the moderate Mu Song had tried negotiating with the authorities and demonstrated considerable skill in doing so.

“Our range of activity has widened a little, while the authorities have received fewer petitions over people being killed by river bandits. Isn’t that a benefit to both sides?”

“No, even so, they allowed you to come this far?”

“Of course not on the surface. And look. They’re already coming.”

At the end of his gaze was a massive warship equipped with cannons.

When the ships had drawn close enough for even people without martial arts to distinguish one another, a middle-aged man dressed in armor suddenly stuck his head out from the stern.

“Who goes there?”

“General, it’s me! I’m here to put a few people ashore.”

“People? Who are they?”

“My juniors. I’ll vouch for their identities personally.”

A river-bandit chief’s guarantee. Surely that would work beautifully.

The official shouted energetically.

“By all means!”

*Fuck, it really works.*

Mu Song suddenly pulled something from inside his robe and tossed it with all his strength.

“Catch!”

The official caught the bundle as it came flying in a long arc and grinned.

“You don’t have to do this every time. Thank you. I’ll buy you a proper drink next time.”

“Sure, let’s do that. How is the City Lord?”

“He had a son nine days ago.”

“Oh, what wonderful news. I’ll definitely attend the doljabi.[^1]”

“Of course. The City Lord will be pleased.”

“Then take care.”

“I wish you martial fortune, Stronghold Lord!”

*For fuck’s sake. The country’s in fine shape.*

After wrapping up their warm conversation, the warship returned the way it had come, while the fast ship leisurely made its way toward the pier.

“We don’t need to drop anchor, do we?”

“Huh? Oh, no.”

“Are you shocked? That’s just how the world works. In any case, you finally look like a young prodigy your age.”

He wasn’t wrong. Worse things happened in the real world, so why should this be a problem?

I gave Mu Song, who was laughing heartily, a respectful clasped-fist salute.

“Thank you for your help, Senior. We arrived comfortably thanks to you.”

“It was nothing. Don’t call something this minor help. Just say the word. I’m Ship-Fire Boy Mu Song!”

“Ah, as expected of the greatest Senior! You’ve turned the Yangtze upside down!”

“Ha ha ha!”

I grinned along with Mu Song as he laughed loudly.

“Then I’ll have to ask for your help again when we return.”

“…”

“Senior?”

Mu Song stared at me with trembling eyes before opening his mouth.

“I’ll… send my subordinates.”

“Thank you!”

*Yangtze taxi. What a steal.*

* * *

Was it just my imagination, or did the fast ship seem to be moving much faster than usual?

I watched the ship cut urgently through the water as though it were fleeing a sea monster, then turned around.

The Bermuda Triangle and a smiling young medical apprentice were there.

“Thanks to you, we got here quickly. Thank you.”

“You should thank the people who rowed and steered the ship. I don’t know where you’re going or what you intend to do there, but stay healthy.”

Although we had only spent a few days together, I thought it had been a pretty good connection.

He was usually innocent and carefree, but he was deep down. I admired how well he had overcome the pain of losing his parents at such a young age.

I sincerely hoped that he would become a fine physician.

“I don’t have anything to give you as we part, but use this for travel expenses.”

I took out a few silver nyang and placed them in his hands. Mungyeong stared at me in surprise.

“Y-Young Master, this is…”

“It’s fine. Think of it as allowance from your hyung.”

“But this is too much.”

“Then pay me back later. Once you become a physician who can put Hua Tuo—or rather, the Divine Physician—to shame, come find me at the Jin Family of Taiyuan.”

“The Divine Physician…?”

“That’s right. If you’re going to do it, you might as well become the best.”

Mungyeong blinked, looking back and forth between the silver nyang in his hand and me. A faint smile appeared at the corners of his mouth.

“Yes. I will.”

“Good. I’m leaving now. Take care.”

The Bermuda Triangle and I turned around after exchanging farewells with Mungyeong.

Hyuk Mujin, who had suffered through prolonged seasickness, quietly came up beside me and spoke.

“Captain. I’m exhausted. Could we rest for half a day before we go?”

“No. We only have to travel for half a day, so rest once we arrive.”

“That’s only half a day if we use a movement technique. And I heard the people of the Sichuan Tang Clan are terrifying… We’ll have to be careful even when we breathe.”

“Then don’t rest. Die.”

“Is that any way to speak to your right-hand man?”

“What? I can’t hear you. Something my left pinky is saying is too quiet.”

Hyuk Mujin’s lips had just jutted out three inches when—

“Um, did you say you were going all the way to the Sichuan Tang Clan?”

“…”

“…”

We slowly turned our heads.

There stood Mungyeong, his eyes sparkling like morning stars.

“The thing is, I happen to be on my way to the Sichuan Tang Clan, too. If I could travel with you, I would never forget this favor even if this body died and died, then died ten thousand times more, until whether my soul existed or not—”

“Hey.”

“Yes?”

“I get it. Shut up and follow us.”

*Fuck. The Bermuda Quadrilateral.*

[^1]: A doljabi is a Korean first-birthday ceremony in which a child chooses from symbolic objects believed to represent their future.

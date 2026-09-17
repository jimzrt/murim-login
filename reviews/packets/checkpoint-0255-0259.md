# Checkpoint Review — 255–259

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

# Chapters 255–259

## Plot

Jongni Chu reveals himself as a Supreme Peak master who has Returned to Simplicity and overwhelms Cheongpung in the Star-Array Grand Banquet semifinal. He wounds Cheongpung and is about to kill him when Jin Taekyung intervenes. Jeok Cheongang forces the final to begin immediately, and Taekyung discovers that his eighth-stage Qi Sense Skill cannot identify Jongni because an unknown force rejects it.

Taekyung and Jongni exchange dozens of attacks. Taekyung reaches the seventh stage of Fire Dragon Divine Spear and fights through an Internal Injury, but Jongni suddenly abandons the platform after noticing something in the distance. The System awards Taekyung the official victory, restoring him and granting EXP, Fame, Points, and several level-ups. Pursuers cannot determine Jongni’s martial arts or realm.

The pursuit ends at a huge pit, where Hong Dao is found with both legs severed and fatal internal injuries. Before dying, he gives Jeok Cheongang the cryptic words “Jongni Chu, Dark Heaven, Unnamed, Buddhist Staff.” Jeok and Taekyung infer that Jongni Chu is connected to or represents Dark Heaven, and that Dark Heaven seeks the Green Jade Buddha Staff entrusted to Unnamed—the sacred treasure and symbol of Shaolin’s Abbot. Jeok orders the Murim leaders to gather at Shaolin and travels there with Taekyung.

Meanwhile, Dark Heaven operatives kill messengers, martial artists, and civilians along the route. Han Su kills a Hidden Shadow Pavilion agent and joins his longtime friend Flame Tiger; after learning that Unnamed possesses the staff, they also proceed toward Shaolin.

## Continuity

- Jin Taekyung is the official Star-Array Grand Banquet winner because Jongni Chu left the dueling platform first.
- Taekyung’s Internal Injury was completely healed by the System’s victory rewards; he gained substantial EXP, Fame, Points, and at least three visible level-ups.
- Jongni Chu is a concealed Supreme Peak master who has Returned to Simplicity, wields Sword Force through a rusted sword, and possesses immense internal energy.
- Jongni Chu escaped using Stepping on Empty Air and Jeok Cheongang’s sword force. His destination, purpose, true identity, sect, and martial-arts origin remain unresolved.
- An unknown force rejected Taekyung’s Qi Sense Skill; its nature and connection to Jongni Chu are unknown.
- Jeok Cheongang’s best friend Hong Dao is dead. His final words implicated Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff.
- Jeok Cheongang and Jin Taekyung are traveling to Shaolin, where Jeok expects a major crisis or “blood wind” may already have begun. The Murim leaders have been ordered to gather there.
- Hong Dao entrusted Unnamed with the Green Jade Buddha Staff. Dark Heaven is actively searching for Unnamed and the staff.
- Myriad-Mile Pursuit is tracking Jongni Chu, but Jeok expects the pursuit to fail.
- Han Su and Flame Tiger are longtime friends and Dark Heaven operatives heading toward Shaolin.
- The attacker who crippled Hong Dao, the meaning of his final words, the fate and location of Unnamed and the staff, and the situation at Shaolin remain unresolved.
- Shadow Killer’s fate, the Gold-Faced Young Master’s identity, and Dark Heaven’s relationship with Tianshan, the Demonic Cult, or the Demonic Path remain unknown.

## Translation Decisions

- Retain **Returning to Simplicity**, **Returned to Youth**, **Supreme Peak**, **Sword Force**, **Zaha Divine Technique**, **Thirty-Six Plum Blossom Swords**, **Fire Dragon Divine Spear**, **Flame Wheel Kick**, and **Four Ounces Deflecting a Thousand Catties**.
- Use **Buddhist Staff** for the cryptic word 불장 and **Green Jade Buddha Staff** for 녹옥불장.
- Use **Han Su** for 한수 and **Flame Tiger** for 염호.
- Retain **Dark Heaven**, **Unnamed**, **Hidden Shadow Pavilion**, **Invincible Divine Sword**, **Life-Sustaining Sword**, and **Always-Victorious Sword**.
- Preserve Han Su and Flame Tiger’s rough, familiar, casually murderous tone.

## Durable state

{
  "active_continuity": [
    "Hong Dao died in Henan after giving Jeok Cheongang the final words “Jongni Chu, Dark Heaven, Unnamed, Buddhist Staff.”",
    "Jeok Cheongang and Jin Taekyung are traveling to Shaolin; Jeok ordered the Murim leaders to gather there without delay.",
    "Jeok Cheongang identifies Jongni Chu as Dark Heaven and believes Dark Heaven's immediate objective is the Green Jade Buddha Staff.",
    "Hong Dao entrusted Unnamed with the Green Jade Buddha Staff, Shaolin's sacred treasure and the Abbot's symbol.",
    "Jeok Cheongang believes a blood wind may already have begun at Shaolin.",
    "Myriad-Mile Pursuit is tracking Jongni Chu, but Jeok Cheongang expects the pursuit to fail.",
    "Dark Heaven operatives have begun killing messengers, martial artists, and commoners around the route to Shaolin.",
    "Han Su and Flame Tiger are longtime friends and Dark Heaven operatives proceeding toward Shaolin after learning Unnamed has the Green Jade Buddha Staff."
  ],
  "continuity_sources": [
    259
  ],
  "open_questions": [
    "What drew Jongni Chu toward the distant point he watched before leaving, and what remains of his purpose beyond seizing the Green Jade Buddha Staff?",
    "What are Jongni Chu's true identity, sect, martial-arts origin, and reason for concealing his strength?",
    "What is the unknown force that rejects Taekyung's Qi Sense Skill?",
    "What is Dark Heaven's relationship to Tianshan, the Demonic Cult, the Demonic Path, or another power?",
    "Why was Shadow Killer pursuing Jongni Chu, what did the Hidden Shadow Pavilion seek, and what became of Shadow Killer after contact was lost?",
    "Who is the Gold-Faced Young Master who bet on Taekyung?",
    "Who attacked Hong Dao, and what happened during the attack?",
    "What has happened at Shaolin, and where are Unnamed and the Green Jade Buddha Staff now?"
  ],
  "safe_through": 259,
  "temporary_decisions": [
    "Use Buddhist Staff for 불장 as the generic form and Green Jade Buddha Staff for 녹옥불장.",
    "Use Han Su for 한수 and Flame Tiger for 염호."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 255

# Chapter 255

Crash!

Jeok Cheongang sprang to his feet so abruptly that he did not even notice the chair toppling behind him.

All his senses were focused on one person alone: Jongni Chu.

“This is…”

The moment was so brief it could hardly be called an instant, but he had definitely felt it.

The qi wave emanating from Jongni Chu had been so powerful that it had made his eyes fly open.

“Returning to Simplicity… He was hiding his strength.”

Dharma King Hong Dao muttered the words like a groan, his voice filled with pure astonishment.

Returning to Simplicity. It was a realm that allowed someone who had learned martial arts to appear like an ordinary person. The protruding temples flattened, and the person could freely control their aura.

To reach such a realm, one had to set foot beyond Peak.

It was a realm of supreme mastery permitted only to the greatest martial artists.

“That young punk is a Supreme Peak master? Have you all gone mad? How could that possibly make sense?”

At the Thunderbolt Saber King’s barrage of questions, Hong Dao and Jeok Cheongang shook their heads.

“Amitabha. Then, Benefactor Peng, how do you intend to explain this situation?”

“He has reached the realm of Returning to Simplicity. And he deceived even our eyes completely.”

The people seated in the seats of honor had been listening closely to the three men’s conversation. Now they sat with their mouths hanging open.

Jongni Chu had scraped through every round from the preliminaries onward. He had always advanced by the narrowest of margins. That was why people had even given him the mocking nickname Life-Sustaining Sword.

But that was no longer the case.

The qi they had sensed from that lucky young martial artist for that brief moment had been powerful enough to send chills down the spines of even the leaders of the Nine Sects and One Gang and the Family Heads of the Five Great Families.

“What in the world…”

The Thunderbolt Saber King could not continue and closed his mouth.

He, too, was a Supreme Peak master and one of the Ten Kings. In his heart, he agreed with Jeok Cheongang and Hong Dao, but he could not bring himself to accept it so easily.

“How can someone who isn’t even thirty years old become a Supreme Peak master?”

As the Thunderbolt Saber King muttered his lament, someone who had been silently observing the situation spoke up.

“It’s possible.”

“What?”

Everyone’s heads turned in the same direction.

As though demanding an explanation, their gazes fixed on Thousand-Faced Fox Song Ho, who added one more sentence.

“If he has Returned to Youth.”

“…”

Leaving the astonishment spreading throughout the crowd behind him, Song Ho leaned back against his chair. His eyes remained fixed on Jongni Chu, sunk deep in thought.

*Who are you?*

The more the question in his heart grew, the more intense the pain became at the stump where his leg had been severed decades ago.

Song Ho knew now. This was no mere coincidence.

Jongni Chu was closely connected to the day Song Ho had become a one-legged man.

*Show me your true face.*

At that moment, the judge’s flag shot powerfully toward the sky.

* * *

Whoosh!

A red slash swept through the air without hesitation. Cheongpung had been standing in place, merely blinking, and twisted his body too late.

But Jongni Chu’s strike had been faster than he expected.

Slice!

A burning pain spread from his chest. A long cut had opened across the front flap of his robe, and red beads of blood began to well up.

The sharp scent of blood pierced his nose.

“…Ah.”

Cheongpung staggered backward and looked at Jongni Chu with a dazed expression.

His friend—or rather, the man he had thought was his friend—was staring at him with an unbearably calm gaze.

“Too bad. It went in too shallow.”

Just as Jongni Chu had said, the sword wound was shallow. It had merely grazed his skin, leaving no other injury.

But Cheongpung’s wound was not limited to his flesh.

“J-Jongni Chu.”

He was Cheongpung’s first friend in the Murim—or in his entire twenty-two years of life.

The man who had extended his hand first and asked to become friends was now pointing a sword at him. Without a moment’s hesitation, he had swung it and cut Cheongpung across the chest.

“Why…?”

“I don’t understand what you mean.”

Jongni Chu casually flicked the blood from his sword.

“Isn’t this the Murim? Surely you didn’t completely trust someone you had just met after exchanging only a few words?”

“…”

Judging by Cheongpung’s expression, it seemed that was exactly what he had done.

Jongni Chu gave a short, incredulous laugh.

“Unbelievable. How have you survived this long with that kind of mind? I heard you were a Disciple of Huashan.”

Jongni Chu glanced at the Heavenly Sword True Person, the Huashan Sect Leader seated in the seats of honor, and clicked his tongue.

“The Sect Leader did a terrible job teaching his Disciple. Pathetic.”

At those words, Cheongpung’s tightly closed lips parted. Unlike before, his voice was low and formal.

“The person who taught me martial arts was my grandfather. Not him.”

“Really? Whoever he is, he must be a senile old man. What’s that old man’s epithet?”

“The Sword Saint.”

“The Sword Saint Mae Jonghak?”

When Cheongpung nodded, astonished exclamations burst from the stands, which had fallen silent.

There was not a single person here who did not know the reputation of Sword Saint Mae Jonghak. His name had long since become a living legend.

And now, after disappearing for decades, the Sword Saint’s Disciple had appeared.

Right here!

Countless people widened their eyes in shock, but Jongni Chu alone was different.

“The Sword Saint’s Disciple…”

Jongni Chu habitually stroked his smooth chin, then let out a quiet laugh.

“Then the Sword Saint must not be much.”

“…”

“A child is still a child no matter how strong he is. You shouldn’t leave one carelessly beside a river. Before you know it, the current will sweep him away.”

Cheongpung suddenly remembered something his grandfather had always said.

*Always remember this. The world is vast, and there are many strong people. Your martial arts are not yet complete, so you must always beware those who harbor malicious intent.*

At the time, those words had not meant much to him. Huashan had been peaceful, and his days with Mae Jonghak had been happy.

But his curiosity about the outside world had grown with every passing day, until he finally left without his grandfather’s knowledge.

And then…

*Ah. So this was what he meant.*

Only now did he feel that he understood those words.

It hurt, though, that he had realized their meaning only after bleeding from the sword of the first friend he had ever made.

*Grandpa.*

Cheongpung tightened his grip on the sword hilt. The scent of blood lingering at the tip of his nose faded, and his mind cleared.

Ssshing.

With a sound that made his hair stand on end, a pure white blade emerged from its sheath.

At the same time, the internal energy coiled in his dantian rose like a cloud, covering his acupoints and spreading in billowing waves.

Tzzzzzz!

The distinctive purple qi of the Zaha Divine Technique rose from Cheongpung’s entire body. His eyes, filled with the colors of the setting sun, turned toward Jongni Chu.

“You’ll regret this.”

“Then let’s see…”

Jongni Chu rested the sword he had been holding loosely across his shoulder.

“Let’s see what you can do.”

Whoosh!

Cheongpung threw his head back. Jongni Chu’s sword passed within a paper’s width of the bridge of his nose. Instead of Sword Energy, the blade was thickly coated in reddish rust.

*Fast!*

Cheongpung had mastered an ultimate eye technique in accordance with his grandfather’s teachings, but Jongni Chu’s movements surpassed even that.

The moment the warning bell rang in his head, a wave of sword attacks followed.

Whoosh! Whoosh-whoosh-whoosh!

The blade that had been about to cleave his chest bent in midair.

It seemed to thrust, but then it slashed. It seemed to slash, but then an unexpected palm strike flew toward his shoulder.

Boom!

“Urgh!”

The unexpected strike slammed into Cheongpung’s shoulder, sending him flying more than ten zhang.

His body spun like a top through the air. The instant his feet touched the ground—

Boom!

The bluestone covering the dueling platform shattered into powder.

Cheongpung surged toward Jongni Chu even faster than he had been thrown away.

The sword streaming purple Sword Energy danced gracefully and caused flowers to bloom in the air.

Ssshhh!

The Thirty-Six Plum Blossom Swords, executed with eight-tenths mastery, scattered in all directions around Jongni Chu.

Surrounded by purple Sword Energy, Jongni Chu suddenly raised the corners of his mouth. It was a smile wholly unsuited to a life-or-death situation.

“This is more than I expected.”

Before he had finished speaking, the sword in his hand moved.

A blinding flash and a deafening roar erupted, so intense that the spectators could not even open their eyes properly.

Boom! Krrrraaaash!

Exploding Sword Energy and flying fragments filled the air.

The thick cloud of dust billowed upward, then split apart to reveal a single figure.

Cheongpung’s eyes widened as far as they could when he saw Jongni Chu coughing softly behind one hand.

*This man…*

This time, he had seen it clearly.

He had seen Jongni Chu’s movements as he deflected every last strand of Sword Energy.

The dozens of Sword Energy attacks capable of piercing steel had been countered by none other than his rusted sword.

The blade did not even carry Sword Energy, yet it had let everything slide away. It had done so as smoothly as flowing water, as though it were the most natural thing in the world.

*How is that possible?*

Cheongpung was seized by astonishment—and by a strange emotion he had never felt before.

The sound of his heartbeat thundered in his ears, and his hand gripping the sword hilt refused to move.

A bead of sweat that had formed on his forehead rolled down the bridge of his nose and dropped.

“Are you afraid?”

Jongni Chu walked toward him at an unhurried pace, as though he were taking a stroll. At his deep, chilly gaze, Cheongpung’s heart lurched.

Then he realized that the word Jongni Chu had just used was the name of this strange emotion.

“…Afraid?”

It was an emotion Cheongpung had never experienced before.

Fear was a foreign feeling he had only ever heard about from his grandfather. Now it was tightening around both his body and his heart.

*Pung. Do you know fear?*

*Fear? What’s that?*

*It hides deep in everyone’s heart. Not knowing that fear is your greatest weakness.*

Sword Saint Mae Jonghak had loved his grandson deeply, despite their lack of a blood relation. He had always looked at him warmly and cared for him day and night.

Just as pretty flowers bloomed in good soil, Cheongpung had grown into a lovable child.

*This old man is at fault. I shouldn’t have done that…*

He had grown up receiving nothing but unconditional love, and so he knew only how to love.

On the mountain where the harmonious grandfather and grandson lived together, there was none of the pride, greed, jealousy, or anger that overflowed in the outside world. The child grew steadily without ever learning how frightening human malice could be or what fear truly was.

*If such a day ever comes, don’t let fear devour you. That is all I can tell you.*

Those were the words Cheongpung had heard the day before he secretly left Lotus Peak.

Perhaps his grandfather had known this would happen.

But after encountering a powerful person unlike anyone he had ever met, Cheongpung found himself backing away without even realizing it.

*Grandpa, what do I do?*

Step.

When Jongni Chu took one step forward, Cheongpung retreated.

Then another step.

And another.

From the five-zhang distance that refused to narrow, Jongni Chu raised his sword.

“This is endless. I expected more from the Sword Saint’s Disciple. Is this all you amount to?”

“I-I…”

“You do know what losing in the Murim means, don’t you?”

Ssshhh.

A ghostlike movement.

Cheongpung, trapped in fear, could not react. In a world that had slowed to a crawl, Jongni Chu was the only thing that seemed alive.

With a single step, he erased the distance that had refused to close, and his sword glided forward.

The moment the rusted blade was about to pierce Cheongpung’s throat—

Swoooosh! Boom!

A terrifying sound split the air, followed by a boom loud enough to leave his ears ringing.

Jongni Chu twisted his sword at the last instant and blocked the attack. Then he gave a sharp grin at the sight of the transparent spearhead.

“As expected, you’ve got a good friend.”

“He’s not a friend. He’s my Benefactor. But…”

Jin Taekyung spat out a wad of phlegm and continued,

“What the fuck are you?”
## Chapter artifact 256

# Chapter 256

“What the fuck are you?”

At the question, which contained so much meaning in so few words, Jongni Chu’s eyes curved like half-moons.

“Do I need to say it again?”

“Jongni Chu from Yunnan. Yeah, I know. So…”

The voice that followed was calm enough to surprise even me.

“Who are you? You.”

“Wouldn’t it be better to catch that friend of yours behind you first?”

Jongni Chu was right. I caught Cheongpung’s arm as it began to crumple.

There was a little bleeding from the shallow cut across his chest, but it was nowhere near enough to bring down a master of Cheongpung’s caliber.

“What did you do?”

“Nothing. His mental strength was merely injured.”

“If anything happens to Cheongpung…”

“You worry too much. It was only a feint. Nothing like what you’re thinking will happen.”

“A feint? That strike just now?”

“If you don’t believe me, I can’t help that. Friendship is a wonderful thing.”

As I watched Jongni Chu smile gently, my stomach burned as though I had swallowed a ball of fire.

*I was completely fooled.*

I remembered our first meeting.

A cheerful loudmouth who had asked to become friends, saying that even brushing sleeves was enough to create a connection. He had been annoying, but I hadn’t disliked him.

Now, however, I didn’t know what to think. From beginning to end, everything about him was shrouded in mystery.

My grip tightened around White Flame.

“W-Wait!”

The judge had hurriedly cut in. He was visibly flustered by the unexpected turn of events.

“Both of you, step back. And Young Hero Jin, entering a duel in progress violates the rules of the Star-Array Grand Banquet.”

Without taking my eyes off Jongni Chu, I answered,

“Then you want me to stand there and watch while someone nearly gets killed?”

“B-But he said it was only a feint!”

“That’s what he says.”

At my firm reply, the judge bit his lip.

“If you don’t withdraw now, you may be disqualified according to the rules.”

“Disqualified?”

“Of course. You don’t want to be disqualified with the final still ahead of you, do you?”

I let out a short laugh.

Winning the Star-Array Grand Banquet would certainly earn me a huge amount of EXP and Fame, or perhaps an even greater Reward.

Jin Wikyung would hug me for raising the family’s reputation, and Jeok Cheongang would be pleased as well.

*But that’s all it would be.*

The year I had spent in Fire Gate Cavern had not been for the sake of winning the Star-Array Grand Banquet.

And the same was true of the sinister bastard standing before me.

“Let’s fight.”

Jongni Chu deliberately widened his eyes.

“Now?”

“Yeah.”

“Good grief. If you don’t withdraw immediately, you’ll be disqualified.”

“I don’t give a damn about that.”

“Thank you. Thanks to you, I’ll be able to win easily and make my name known throughout the world.”

“Cut the crap. Stop the terrible acting and tell me what you really think.”

Jongni Chu paused, then grinned.

“I was right about you. You really are an interesting friend.”

“Friend? That’s not what you say in a situation like this. Especially not between you and me.”

“It does hurt a little, but… well, it can’t be helped.”

“So what’s your answer?”

“I did want to fight you at least once.”

The judge, who had been listening to us, cut in with a rigid expression.

“Did you not hear what I said? And according to the rules, the Star-Array Grand Banquet final must take place tomorrow.”

At that moment, a low voice pierced everyone’s ears.

“Then change those rules. Starting today.”

“How dare you!”

The judge spun around, roaring, and froze in place.

A tiny old man had approached like a ghost.

“G-Great Hero Jeok?”

The Fire King, Jeok Cheongang. His reddish, fever-bright eyes passed over me and Jongni Chu before settling on the judge.

“That’s right. It’s me.”

“I-I apologize. I misspoke.”

“Forget it and move on. Proceed with the next duel immediately.”

“B-But…”

“But?”

The judge swallowed hard.

“To change the schedule, we must hold a meeting and receive the presiding chair’s approval.”

“The presiding chair of the first Star-Array Grand Banquet was the Martial God. After he disappeared, it became the Abbot of Shaolin, who could be considered the organizer. Is that correct?”

“Y-Yes, that’s correct.”

“Then it’s settled.”

“Pardon?”

“Hong Dao had to step away for an urgent matter. Considering seniority and standing in the Murim, I am the presiding chair now.”

Everyone’s eyes turned toward the seats of honor a hundred zhang away. Just as Jeok Cheongang had said, the seat where Dharma King Hong Dao should have been sitting was empty.

No. There was one more person missing.

*Song Ho, the Thousand-Faced Fox.*

Two important people had left at the same time. What was going on?

A question flashed through my mind, but it soon disappeared. That wasn’t what mattered right now.

“Now we can forget about those damn rules or whatever they are. Am I wrong?”

The judge hesitated, then nodded.

“No. We’ll proceed.”

“Good. And you.”

Jongni Chu, who had been watching the scene with great interest, pointed at his own chest.

“Me?”

“Yes, you, the one whose tongue has been cut in half.”

“My tongue hasn’t been cut in half, but I understand.”

Even though he clearly knew who he was dealing with, he remained completely unruffled.

Jeok Cheongang fixed Jongni Chu with a grave, steady glare.

“I’ll ask you directly. Did you come from Tianshan?”

The Tianshan Mountains. The headquarters of the Demonic Cult.

The judge flinched as though he had touched a flame, while Jongni Chu wore a faint smile, as if enjoying the situation.

“I’ll postpone my answer to that question.”

“If you don’t want to die young, you’d better think carefully before answering.”

Jongni Chu rubbed his smooth chin.

“What will you do if some unfortunate accident occurs before you hear my answer?”

“An accident?”

“You never know what might happen in the Murim. For example, a certain master might lose his only Disciple.”

At that moment, a deathly silence pressed down on the surroundings.

Jeok Cheongang stared at Jongni Chu with emotionless eyes before opening his mouth.

“If such a regrettable thing were to happen… the master who lost his Disciple would become very angry.”

“Would you kill the culprit even if you had to cast a net over heaven and earth?”

“Of course not. I’d burn him alive. You have my word.”

“Aren’t you making quite a promise? You don’t even know who we’re talking about.”

“Coincidentally, it’s someone I know very well.”

“Oh, dear.”

Jongni Chu burst into cheerful laughter.

“Then I suppose I’ll have to go easy on him.”

“Are you underestimating my Disciple?”

“I’m looking forward to it, but he probably won’t be a match for me.”

“That’s what he says. What do you think?”

At Jeok Cheongang’s question, I tightened my grip around the spear shaft and answered,

“That bastard’s got a warped way of thinking.”

Jongni Chu looked at me with amusement.

“I can’t tell whether what you’re showing is confidence or arrogance.”

“Neither. I want to live a long, full life. But there’s one thing I do know.”

I continued, enunciating each word clearly.

“You don’t know anything until you try.”

“Good thinking. But will that be enough this time?”

“I hope it is.”

“You could die.”

“That’s why I have to give it my all. If I die after that… well, it’ll leave a bad taste in my mouth, but someone will avenge me. Won’t they?”

Jeok Cheongang nodded.

“Go in peace. I’ll avenge you, so don’t worry about what comes after.”

“Seriously? You call that comforting?”

“So stop talking nonsense and remember one thing. If that bastard kills you, I’ll kill you myself.”

“If I don’t want to die twice, I’d better work hard.”

Jongni Chu, who had been listening to us, burst into loud laughter.

“Ha-ha-ha! What an interesting Master and Disciple pair.”

I stared at him and muttered inwardly.

Before we fought, I needed to peel back even a little of the veil surrounding him.

*Skill, Qi Sense.*

A chime rang.

> **System**
>
> - You have used **Qi Sense**.
>
> - Since you are currently at the eighth stage, you can detect targets at Level 100 or below within eighty zhang.

I possessed two kinds of Qi Sense: the Qi Sense that existed as a Skill, and the Qi Sense I had developed as a martial artist.

Early after coming to the Murim, I had relied entirely on the former. But as time passed, I realized that Level and strength were not directly proportional, so I gradually reduced how often I used it.

The Murim had too many variables to judge people by Level alone.

*Show me something. Even a little. Show me what you really are.*

Whoosh!

Once Qi Sense reached the eighth stage, I could focus it entirely on a single person.

A blue line visible only to me shot forward without hesitation and reached Jongni Chu.

No—just as I thought it had reached him—

Beep!

> **System**
>
> - **Qi Sense** has failed!
>
> - Unable to identify the target!
>
> - An unknown force is rejecting the **Skill**!

“…”

What?

My eyes flew open at the unbelievable System notification. I looked at Jongni Chu in confusion.

The blue line of Qi Sense had seemed to hit something, circled around him, and then disappeared.

“What the hell did you do?”

“That’s what I’d like to ask you.”

Jongni Chu had stopped laughing. His gaze, filled with interest, turned toward me.

“You have quite an interesting trick.”

His words suddenly brought an old memory to mind.

It was a memory from a year ago, of the first person who had ever detected my Qi Sense.

*Well, aren’t you an interesting fellow?*

The Fire King, Jeok Cheongang.

As befitted a Supreme Peak master, he had been able to control his qi freely. Through that encounter, I had first realized that the System was not omnipotent.

*But even Jeok Cheongang couldn’t make the Skill bounce off him.*

And now an unknown force had rejected the Skill. I had never heard of anything like it.

The more I saw Jongni Chu violate common sense, the more one word floated through my mind.

*Demonic martial arts.*

Martial arts that defied reason.

My suspicion hardened into certainty. I finally understood the meaning behind the question Jeok Cheongang had asked him earlier.

“You really are from the Demonic Cult, aren’t you?”

“Beat me and I’ll tell you. What kind of trick did you use?”

“Even if you beat me, I won’t tell you.”

“That leaves me at a considerable disadvantage. It can’t be helped.”

Sssrk.

The rusted sword slowly rose and pointed at the space between my eyebrows.

A humming voice followed, utterly at odds with the suffocating edge of his sword.

“Come on. Let’s have some fun.”

I raised White Flame and answered,

“Yeah. Let’s have a brutal good time.”

Whoosh!

The fire dragon curled within my dantian awoke from its sleep and stretched.

*Give it everything you’ve got.*

Jeok Cheongang used Seizing an Object Through Empty Space to pull Cheongpung toward him, then stepped through the air as he retreated. At the same time, the judge’s frantic voice rang out.

“According to the revised schedule, the Star-Array Grand Banquet final will begin immediately! The Life-Sustaining Sword—no, the Always-Victorious Sword, Jongni Chu, and the Sleeping Dragon of Shanxi, Jin Taekyung…!”

The judge’s announcement became meaningless.

We were already charging toward each other.

Screeeech!

One step. The distance disappeared.

Boom!

Two steps. Two streaks of light bursting from our hands collided in midair.
## Chapter artifact 257

# Chapter 257

Boom. Boom. Boom.

The ground trembled faintly as a distant roar rolled in from far away.

The commoners who knew nothing of martial arts merely tilted their heads and continued on their way.

But the Thousand-Faced Fox, Song Ho, was different.

*This is…*

The Hidden Shadow Pavilion agents who had been secretly following Song Ho sent him messages through Sound Transmission.

—About seven hundred zhang to the north.

—Something seems to have happened at the dueling platform.

—Pavilion Master, your orders.

Song Ho hesitated. After all his years of experience, he could guess that the roar had been the aftermath of martial arts.

And not just any martial arts…

*A Supreme Peak master?*

Even if you turned the entire world upside down and scraped it bare, there might not be more than thirty Supreme Peak masters in existence.

The aftermath he had sensed clearly indicated a clash between Supreme Peak masters.

This was no ordinary matter. What had the Always-Victorious Sword, Jongni Chu, finally done?

*But we should be well prepared for something like this.*

They had already searched every inch around the Murim Alliance. They had thoroughly inspected everyone and everything in preparation for any possible situation, even taking into account the possibility that explosives might have been brought in and planted.

A tiger was still a tiger even after losing its teeth. The Hidden Shadow Pavilion might not have been what it once was, but its intelligence network was still capable of controlling Henan Province.

*And there are three of the Ten Kings here.*

On top of that, the leaders of the Nine Sects and One Gang, the Family Heads of the Five Great Families, and the elites of the sects and families they had brought with them were all present.

It would not be an exaggeration to call that place a miniature version of the Murim world.

*I must be getting old. Perhaps I worried too much.*

It was all because of those unknown beings who had yet to reveal their true identities.

Song Ho remembered clearly the conversation he had shared with Dharma King Hong Dao when the man had come to find him a year ago.



*Dark clouds are covering the sky.*

*Could they be clouds from Tianshan?*

*I don’t even know where they’re coming from or when they’ll arrive. All I have are these two words: Dark Heaven.*

*Dark Heaven…*

*Help me. I need your strength.*



Half a century had passed since the Great Faction War.

The fox who had once abandoned the secular world and lived buried in the countryside had returned to the world of martial artists.

And he was feeling the passage of time.

The Thousand-Faced Fox, Song Ho, let out a faint sigh and moved his lips.

—Tell the Abbot that I’ll go after I finish my business.

An agent from the Hidden Shadow Pavilion joined him seven and a half minutes later and replied.

—Dharma King Hong Dao left after the Pavilion Master came out.

—The Abbot left?

—Yes.

Song Ho hesitated for a moment, then shook his head. He did not know what had happened, but he trusted Hong Dao’s judgment.

Hong Dao would undoubtedly trust his judgment as well.

—Send one person to the dueling platform. Two of you stay here. Report immediately if anything happens.

—Understood.

—The rest of you, follow me. As soon as we arrive, seal off the area so tightly that not even a drop of water can escape.

—Yes, sir.

Whoosh!

Black figures scattered through the alleyways.

Song Ho sprinted across the endless line of rooftops, putting his wooden crutch to use as he employed his movement technique.

His mind was filled with the report he had received fifteen minutes earlier.



*We found Shadow Killer.*



Tap!

The force he put into his crutch increased as he accelerated with his movement technique.

The pain grew in proportion.

* * *

Bang!

The transparent spearhead of White Flame collided with the rusted blade.

One exchange.

A roar that seemed to split the heavens rang out, and a powerful blast of wind engulfed my entire body.

Kraaaaoom!

A whirlwind rose around us, blocking everyone else’s view.

Amid the dust clouds swirling in every direction, I could see Jongni Chu’s eyes widened in surprise beyond our crossed weapons.

“Impressive. I didn’t expect to be pushed back.”

As he spoke, his body slid several steps backward.

There was no doubt about it. He had been unable to withstand my strength, which had already far surpassed the limits of a human being.

But…

*What the hell is this bastard?*

If Jongni Chu was surprised, I was utterly aghast.

I was the one who had spent an entire year training with an iron ball weighing more than a thousand catties attached to me. My martial arts—and my stats—were on a completely different level from the past.

*And he withstood that?*

That exchange should not merely have given me the upper hand. I should have overwhelmed him completely.

Yet Jongni Chu had only retreated a few steps after taking that strike.

Even his rust-red sword had not broken.

*Who the hell is this guy?*

A bead of cold sweat slipped down the back of my neck.

A playful smile appeared around Jongni Chu’s mouth.

“Four ounces deflecting a thousand catties. You shouldn’t try to overpower someone with strength. You have to read the flow.”

“…”

Kaaaang!

His blade wrapped around the spearhead and changed direction.

I put more force into the hand gripping the spear shaft, but the harder I pushed, the more it felt as though I were sinking into a swamp.

Jongni Chu’s sword was a horse, and my spear was a cart. The cart had no choice but to follow the direction the horse took.

The transparent spearhead of White Flame, made from Ten-Thousand-Year Cold Iron, struck the ground.

At the same time, Jongni Chu thrust out his palm.

Boom!

Compressed air exploded in front of my chest, and my vision grew hazy.

I barely managed to keep my body from being thrown backward. Gripping the spear shaft buried deep in the ground, I spun around and reached Jongni Chu’s face.

Blue flames gathered around my right foot, which was imbued with one jiazi of internal energy.

*Flame Wheel Kick.*

The blazing flames slammed into the back of Jongni Chu’s neck.

Bang!

He slid backward and lowered his elbow.

The sleeve of his robe, burned completely black, scattered into ash.

“Too bad. I liked this outfit.”

Crack. Crack.

He twisted his neck from side to side like a Third Rate street thug, then grinned.

“But honestly, you’re amazing. I’m liking you more and more. Now then…”

Whoosh!

His figure vanished with the sharp sound of cutting wind.

A low voice pierced my ear from right beside me.

“Let’s really get started.”

Hooooong.

The wind stopped.

This time, my senses moved a step faster than my body. I crossed both arms in front of me at the last instant, and Jongni Chu’s fist slammed into them.

It was a strike carrying an enormous amount of internal energy, unlike anything he had used before.

Kra-boom!

Its power had already surpassed all ordinary limits. Even though it was only flesh striking flesh, the resulting roar sounded like a bomb exploding.

Although I used the Thousand-Catty Drop technique to anchor myself at the last moment, my body bent backward until my lower back nearly touched the ground.

Crack.

Even my superb Muscles and Bones, good enough to be called the Heavenly Martial Physique, were useless this time.

I clenched my teeth and endured the sharp pain running along my spine.

*How dare this bastard.*

Boom!

I slammed my empty left hand against the ground.

I shot upward two or three times faster than I had fallen. Jongni Chu’s brightly smiling face appeared before me.

I roared.

“I haven’t even gotten to use these hips yet!”

The fire dragon stretching through my four limbs and hundred bones charged toward my open palm.

A heatwave surged upward, carrying lava-like heat.

The martial art that had once driven me to the edge of death collided with Jongni Chu’s punch.

Flame Divine Palm.

Bang!

My ears rang, and the ground shook.

Still gripping White Flame, I was thrown backward.

When I sprang to my feet, Jongni Chu stood motionless on the dueling platform, which had been blackened from end to end, beyond the hazy cloud of dust.

“That was a poor choice. As you can see, I’m confident when it comes to internal energy.”

I glared at Jongni Chu as he smiled calmly.

Then I suddenly vomited a gush of blood.

The blood was black.

Proof that I had suffered an Internal Injury.

*Damn it.*

My opponent was a Supreme Peak master who had reached the realm of Returning to Simplicity.

I had expected him to be strong, but he was even stronger than I had imagined.

Even allowing for the fact that he had learned demonic martial arts, it was difficult to understand how someone that young could possess such martial power.

“What the hell are you, really?”

I wiped the blood from my mouth with my sleeve.

Jongni Chu let out a hollow laugh.

“That’s what I want to ask you. I never thought I’d see a monster like you in my lifetime.”

“This bastard’s trying to deceive me now, too.”

“I’m serious.”

“Serious my ass. If I’m a monster, what does that make you?”

“I’m… let’s just say I’m a little special.”

I looked at Jongni Chu’s faintly smiling face and spat out a mouthful of blood-tinged phlegm.

My insides burned from the Internal Injury.

“Is this some legendary demonic martial art, too?”

“Whenever people encounter something that lies outside common sense, they think of the word ‘demonic.’ It isn’t easy to accept something as it is.”

“Yeah, it really isn’t easy. So what kind of demonic martial art did you learn?”

“Any further questions would be a waste of time.”

Jongni Chu raised his sword and pointed it at me.

Transparent qi flowed from the blade in thin streams, gathering into a definite form.

Sword Force.

It was a manifestation of energy permitted only to those who had set foot in the supreme realm of the Supreme Peak.

Tzzzzzzzz!

Just looking at it made my blood run cold.

The aura flowing from Jongni Chu made my palms damp and my lips dry.

*This is dangerous.*

I took a deep breath.

I had lost count of how many times I had narrowly escaped death by now.

The important thing was that I had survived every time.

And it would be the same from now on.

Wasn’t that why I had followed the Fire King and endured training that had seemed utterly impossible?



*Sleep one shichen a day. The rest of your time must be spent training!*



That damn old man.

Before I had begun serious training, Jeok Cheongang had said those words.

The memory surfaced, and I let out a quiet laugh.

*Like hell I got one shichen.*

I had been allowed only half a shichen.

Without the System’s power to restore my body rapidly, those days would have been impossible to endure.

The amount of sleep I got had decreased, while the iron ball grew heavier with each passing day.

Even under those brutal conditions, I had thrown punches, kicked, and swung my spear.

“That was the key to victory.”

“Hmm?”

“My Master was right. Sleep is a luxury for a martial artist. And…”

*Status Window, open.*

As soon as I muttered the words inwardly, a holographic window filled my vision.

A lot had changed over the past year—not only the Level displayed in my Status Window, but also its numbers and the number of Titles.

But there was only one thing that mattered to me now.



> **System**
>
> **Remaining Points:** 500



“Repeat Quests are a fucking steal.”

The endless repetition of my training meant one thing: Repeat Quests.

And then there were the points I received from leveling up.

Seeing the savings I had diligently deposited for an entire year turn into a sizable lump sum filled me with satisfaction.

“This is why people need to save.”

“What does that mean?”

Jongni Chu tilted his head, unable to understand my words.

I grinned at him and lifted White Flame.

“It means things are about to get a little harder for you.”

At the same time, countless System commands rang out in my mind.

Strength. Agility. Stamina.

My Muscles and Bones. My Sinews and Meridians.

Everything advanced by one step as new power gathered, connected, and seeped into me.

In a world that had slowed to a crawl, I took a step.

Swish.

Not a sound was made.

With a single step, I appeared in front of Jongni Chu.

The Fire Dragon Divine Spear, which had reached the seventh stage, danced along the spearhead, burning the air and sound alike.

Papapapapat!

The spearhead transformed into streaks of light and poured toward every part of Jongni Chu’s body.

At the same time, his sword, enveloped in transparent Sword Force, moved.

Kwaaang!

In time that had been split apart, then split apart again, dozens of exchanges passed between us.

I could see Jongni Chu’s eyes widened in astonishment.

Roars of impact erupted without end, overlapping one another.

I wondered if this was what it would sound like if the heavens collapsed.

Screeech! Whoosh-whoosh-whoosh!

Whenever spear and sword parted, a punch and a palm strike collided.

I narrowly dodged and retreated, only to find another attack waiting where I had landed.

Krrrzzzt!

A single punch and a single kick created massive craters, laying waste to everything around us.

The dueling platform, hard beyond description, was covered in cracks and pits like a spiderweb.

But the most astonishing thing of all was Jongni Chu.

“Incredible! Truly incredible!”

He continued to unleash one form after another with a burst of laughter, his eyes shining with joy.

Even though I was fighting with all my strength, his movements were growing faster.

And stronger.

*What kind of bastard is this…?*

My mind wavered, and my hands and feet grew disordered.

My shaken composure soon led to a mistake.

Pow-pow-pow!

“Gah!”

My vision turned white, and excruciating pain surged through me.

As I staggered backward, Jongni Chu watched me with an expression filled with admiration.

“Jin Taekyung, the Sleeping Dragon of Shanxi. I’ll remember you clearly. You are the one who…”

At that moment, Jongni Chu’s expression hardened.

As if drawn by something, he stared intently at a distant point.

Then he suddenly kicked off the ground and shot upward.

Bang!

It happened in an instant.

I stared blankly at his back as he stepped on empty air and vanished.

Then I came to my senses and shouted at the top of my lungs.

“Where are you going, you son of a bitch!”
## Chapter artifact 258

# Chapter 258

I saw red.

“Where the hell are you going, you son of a bitch!”

If this had happened before, my first thought would have been *Why is he suddenly leaving?* Maybe I would even have breathed an inward sigh of relief at having escaped the crisis.

But not now.

*This bastard beats the hell out of me and then runs?*

Unlike me, who was still at the Peak realm, Jongni Chu was unquestionably a master of Supreme Peak. I acknowledged that his skill was several levels above mine.

But to leave before the duel had even been decided?

I gritted my teeth. Ignoring the Internal Injury needling my insides, I focused all my internal energy on my lower body.

“Stand right there.”

Crack. Boom!

I leaped into the air with a thunderous roar. A cold wind slapped my face, and Jongni Chu’s foot appeared right in front of me.

He was close enough to reach if I simply stretched out my hand. One certainty flashed through my mind.

*Got you.*

Whoosh!

But the spearhead I thrust out with a triumphant smile passed uselessly through empty air.

I blinked, unable to understand what had happened.

*How?*

Even with my seventh-tier grades, I knew the law of universal gravitation. Jongni Chu’s body had already reached its highest point and was falling, while I was still rising with the momentum of my leap.

He had unquestionably been close enough for me to grab his ankle with my bare hand.

But captivated by that certainty, I had overlooked one crucial fact.

Martial artists—and Supreme Peak masters in particular—were beings who shattered common sense.

“What the hell…”

A curse escaped through my parted lips. The sight unfolding before my eyes was that shocking.

Papapapat!

He was stepping on the air.

On empty space, where there were no walls or branches.

As though invisible stairs had appeared beneath his feet, Jongni Chu stepped on the air and soared higher. And higher still.

*Stepping on Empty Air…*

What the actual fuck? How was I supposed to catch him?

I muttered a curse inwardly as my falling field of vision took in the faces of the people thrown into confusion below.

Among them stood a tiny old man whose eyes shone coldly.

“You bastard! How dare you run!”

The Fire King, Jeok Cheongang.

Along with his roar, which shook the heavens, red rays shot from his wrinkled hand. A sword carrying Extreme Yang internal energy crossed dozens of zhang in an instant and struck its target.

Rumble-rumble-boom!

The trembling air and flash of light that erupted in midair stabbed at my retinas. When I opened my eyes again, I saw Jongni Chu falling.

No. I had to correct myself.

*That isn’t falling.*

Unfortunately, unlike my previous prediction, I was right this time.

Jeok Cheongang’s muffled groan was the proof, and Jongni Chu’s body shooting away like an arrow was the result.

*He blocked it.*

Jongni Chu had not only blocked Jeok Cheongang’s sword. He had also used the enormous internal energy contained in it as propulsion, accelerating toward the direction he wanted.

It was an astonishingly clever and efficient choice—one that was difficult to believe he had made in that brief instant.

Screeeeeech!

Nothing could stop Jongni Chu as he shot through the sky like a meteor from that dizzying height.

Tap.

At the same moment I landed on the devastated dueling platform after personally experiencing the law of universal gravitation, Jeok Cheongang’s furious voice rang out.

“What are you doing? Chase that bastard immediately!”

The whole thing had happened so suddenly. Only when Jeok Cheongang’s shout rang out did the leaders in the seats of honor finally realize what was happening and spring into action.

“Capture Jongni Chu, the Always-Victorious Sword!”

“Seize the Demonic Cult spy plotting some vile scheme! Whoever captures him, dead or alive, will receive a great reward!”

The Nine Sects and One Gang and the Five Great Families. On top of them, influential sects that wielded considerable power in their respective provinces.

Everyone gathered here was a key figure who moved the Murim.

Naturally, their attendants were all renowned Peak masters as well.

“Yes, sir!”

Hundreds of martial artists scattered in every direction. At their head were Jeok Cheongang, me, the Thunderbolt Saber King, and several other leaders.

Screeeeeech!

We raced ahead of everyone else. I could not keep pace with Jeok Cheongang, who had mastered the Fire Gate Clan’s signature movement technique, Flamefire Path, to the ninth stage, but I was fast enough to follow while keeping his back in sight.

*If you don’t have teeth, use your gums.*

Although my movement-technique realm was low and my martial arts were still lingering at the very edge of the Peak realm, my physical abilities had already broken free of their limits. That made it possible.

“How’s your Internal Injury?”

“I can endure it.”

I nodded at Jeok Cheongang’s voice through the fierce wind.

At that moment—

Ding.



> **System**
>
> - Under the rules, **???**, who left the dueling platform first, has been recorded as an out-of-bounds loss!
>
> - Quest, **Star-Array Grand Banquet**, completed successfully!
>
> - Great Achievement, **Star-Array Grand Banquet Victory**, achieved!
>
> - Rewards will be distributed according to the participants’ caliber and the difficulty of the competition!
>
> - You have obtained a vast amount of EXP and Fame, as well as additional Points!
>
> - Level up!
>
> - Level up!
>
> - Level up!
>
> .
>
> .
>
> .



Ding. Ding. Ding.

As the System notifications relentlessly pierced my ears, the changes began.

Vitality filled my exhausted body, and the Internal Injury that had been stabbing at my lungs was completely healed. The fire dragon in my dantian, which had lost its strength after our all-out exchange, writhed like a dragon and spread through my limbs and every part of my body.

*I never expected to win the Star-Array Grand Banquet like this.*

But I was not given even a moment to check the System messages.

Finding Jongni Chu, who had disappeared ahead of us, was the priority.

“Damn it. I don’t know what kind of bastard he is, but he sure is fast.”

As Myriad-Mile Pursuit, the Beggars’ Sect Leader and a master of movement techniques, had said, Jongni Chu was absurdly fast.

Jongni Chu’s figure had already vanished from everyone’s sight a long time ago. Jeok Cheongang rapidly issued orders.

“We’ll lose him if we continue like this. The Beggars’ Sect will take the west. The Kunlun Sect and the rest of you cover everything in between.”

“Yes, Great Hero Jeok.”

“Understood.”

Papapat!

The Sect Leaders of the Beggars’ Sect and Kunlun Sect—two sects renowned for their movement techniques—disappeared with their disciples in tow. Jeok Cheongang then turned his gaze toward the Thunderbolt Saber King.

“You take the east.”

“Then what about here?”

“I’ll handle it.”

The Thunderbolt Saber King spoke with a grim expression.

“Be careful. That bastard calling himself the Always-Victorious Sword… You’ll have a hard time handling him alone.”

*A hard time handling him?*

Those words had come from the Thunderbolt Saber King, a man whose pride was so fierce that no one could surpass him in that regard.

In other words, Jongni Chu was comparable to the Ten Kings—or perhaps even stronger.

*Jongni Chu was that powerful?*

How had someone so young reached such a realm?

He was a monster among monsters. As I swallowed my surprise, Jeok Cheongang snorted.

“That only applies to weaklings like you. You shouldn’t lump this old man in with you.”

He spoke as though he were joking, but it was obvious that he had not dismissed the Thunderbolt Saber King’s words.

Despite the corners of his mouth being raised, Jeok Cheongang’s eyes had turned cold and still.

“That’s enough grumbling. Go.”

“Damn it. Even the heavens are heartless. Why did Hong Dao, that damn monk, have to disappear at a time like this?”

After leaving behind a single lament, the Thunderbolt Saber King turned away and vanished from sight.

Now only Jeok Cheongang and I remained.

We continued moving at high speed, leaping over and passing through the hundreds of buildings stretching endlessly before us as we exchanged words.

“When you find him, do not act rashly. Understood?”

“I can’t promise that. I have a score to settle.”

“Jongni Chu is a master you cannot fight. Do not step forward until I give you permission.”

“Just how strong is he?”

After a brief silence, Jeok Cheongang’s lips parted.

“I don’t know.”

“What do you mean by that…?”

“Even with my eyes, I could not determine what martial arts he had learned or what realm he had reached.”

“…”

After the famously proud Thunderbolt Saber King, even Jeok Cheongang—who was counted among the very strongest of the Ten Kings in terms of martial power—had given that answer.

I was licking my parched lips when—

Kwoooong!

Far away, a dust cloud rose with a thunderous roar. The screams of people and the shrill sounds of whistles rang out from every direction, announcing the appearance of an enemy.

I opened my senses wide and took in the information.

*West. More than five hundred zhang away.*

That was the direction of the Beggars’ Sect.

It was also close enough to reach within a few breaths if I used my movement technique with all my strength.

“Master!”

“I know.”

Boom!

Jeok Cheongang and I shot forward like cannonballs.

The scenery around us began to change as it blurred past with every step. The pavilions that had stretched endlessly across the area grew fewer one by one, and tall city walls came into view.

The harder we ran against the fierce pressure of the wind, the heavier my chest felt.

*What is this feeling?*

Could it be the pressure of facing Jongni Chu again?

I glanced sideways. Jeok Cheongang’s expression had hardened. The emotion etched across his face was unmistakable foreboding.

A moment later, we discovered the source of that inexplicable feeling.

“Chase that bastard!”

“Master! Please come to your senses, Master!”

A massive pit more than thirty zhang wide.

Between the gathered disciples of the Beggars’ Sect, a blood-soaked Buddhist robe came into view.

A wrinkled hand trembled intermittently. Beneath the two severed legs, a pool of blood had gathered, and prayer beads stained red with their owner’s blood floated across its surface.

“…Damn monk?”

Jeok Cheongang’s steps stopped dead when he saw his friend.

* * *

Jeok Cheongang’s vision went hazy.

Their last conversation echoed endlessly in his ears.



*“Something came up. I need to step away for a while.”*

*“Now?”*

*“I’ll take care of it and be right back.”*

*“Is it something small or something serious?”*

*“Amitabha. As Shakyamuni said, if you resolve the greater matter first, the smaller matter will resolve itself.”*

*“That damn Amitabha. This is why people call you a damn monk.”*

*“What does it matter whether I’m a Buddha or a damn monk? Ha-ha-ha.”*



He remembered clearly how Hong Dao had left half a shichen ago with a laugh.

But why…

*Why are you lying here like this?*

Splash.

Mud and bloodwater splashed through the air. The Beggars’ Sect disciples surrounding the fallen old monk hurriedly stepped aside and bowed their heads.

“G-Great Hero Jeok!”

“Our Sect Leader is pursuing Jongni Chu. B-but when we arrived, it was already too late…”

“Move.”

The voice that slipped through Jeok Cheongang’s lips was dry as spent ash.

Every sound stopped. It was as though the world itself had frozen.

His senses were already focused on only one person.

“I’m here.”

It was the same greeting as always. But instead of a sly voice, a strained cough answered him.

Cough. Cough.

The Dharma King Hong Dao’s chest heaved as black blood welled from the corner of his mouth.

A grave Internal Injury. Blood mixed with fragments of his organs had come out, so there was no need to examine him to know what condition his insides were in.

“Well, well. Your friend has come to visit, and you couldn’t even wait for me before lying down again?”

Jeok Cheongang spoke calmly as he dropped down beside Hong Dao.

He grasped the blood-soaked old monk’s wrist and sent internal energy into him. His suspicions became reality.

*Beyond saving.*

That grim, heavy verdict filled Jeok Cheongang’s mind.

“Do you remember when we first met? Back when we fought Demonic Cult bastards in Gansu almost every day?”

Did Hong Dao hear him? Could he even hear him?

Everyone shared the same question, but Jeok Cheongang paid it no mind and continued speaking.

“At first, I wondered what kind of damn monk you were. But they say even dislike can become affection, and when the time came to part with you, I found myself reluctant.”

Although he had never once said it aloud, Hong Dao was the only friend Jeok Cheongang had ever opened his heart to in his entire life.

To his own Master, he had to be a reliable Disciple. To the first Disciple he would later accept, he had to become a dependable Master.

But with Hong Dao, it was different.

When he was with Hong Dao, he did not have to be anyone’s anything. He could simply be Jeok Cheongang, an ordinary human being.

“Did you know?”

Jeok Cheongang sent internal energy into Hong Dao’s Mingmen acupoint and spoke in a low voice.

“You’re my best friend.”

The breath that had been so weak it seemed ready to stop at any moment eased. The eyelids that looked as though they would remain closed forever finally opened a sliver.

A final rally.

Jeok Cheongang looked into Hong Dao’s gray eyes as the last flame of life rose within them.

“Speak. Anything is fine.”

Hong Dao’s blood-drenched lips moved faintly. Jeok Cheongang pressed his ear to Hong Dao’s mouth to hear his final words, and his expression changed from moment to moment.

Anger. Shock. The realization of something.

And the final emotion to appear was sorrow.

Slowly. Then with a soft thud.

The voice mixed with coughing fell silent. The chest that had been heaving and the eyelids that had been trembling both settled peacefully.

Hong Dao closed his eyes as though he had fallen asleep, a satisfied smile still resting at the corners of his mouth.

Jeok Cheongang stared at him for a long moment before opening his mouth.

“We’re going to Shaolin.”

His voice boiled like molten lava.
## Chapter artifact 259

# Chapter 259

Dharma King Hong Dao.

He was the Abbot of Shaolin, known as the Mount Tai and Northern Dipper of the Murim, and one of the Ten Kings.

And he had breathed his last here in Henan, of all places—the front yard of Shaolin and the site of the Star-Array Grand Banquet.

“H-How could this happen?”

“Master Hong Dao!”

Sorrow and shock pressed down on everyone gathered there, but my gaze remained fixed on only one person.

I spoke toward his back, which had gone rigid as a plaster statue.

“Old Master—no, Master.”

Jeok Cheongang, who had been looking down at Hong Dao’s corpse, turned his head.

“I’m going to Shaolin.”

His voice boiled like molten lava.

The blade-sharp aura pouring from the entire body of the Fire King, Jeok Cheongang, made it difficult to breathe and prickled my skin.

But there was only one thing that had gone cold and still: his eyes.

The man before me was suppressing the urge to tear Jongni Chu apart immediately with the last thread of his reason.

*What could possibly be important enough to take precedence over avenging his dearest friend?*

“Was that Master Hong Dao’s final wish?”

“Later. Every moment is precious right now.”

Just as Jeok Cheongang finished speaking, dozens of presences rapidly approached from far away. At the front of the group, the Thunderbolt Saber King opened his eyes wide at the sight unfolding before him.

“H-Hong Dao!”

“We have no time to be surprised, so listen carefully.”

Jeok Cheongang continued speaking without pause.

“I’m heading to Shaolin by this route. Inform everyone and gather them. We cannot delay even for a moment.”

“You intend to cast a net over heaven and earth to capture Jongni Chu?”

“The opposite.”

“What?”

“Myriad-Mile Pursuit is tracking him, but he’s certain to fail. When everyone has gathered, have them come straight to Shaolin.”

“You said Shaolin?”

“That’s right.”

Jeok Cheongang nodded heavily.

“If Hong Dao’s final words are true… a blood wind will soon blow through Shaolin. It may have already begun.”

“……!”

The gathering fell silent at those shocking words. Even the Thunderbolt Saber King was left gaping, so naturally, I was no different.

*At Shaolin Temple?*

What kind of place was Shaolin Temple?

It was a temple and martial sect of such stature that calling it the Mount Tai and Northern Dipper of the Murim was only natural. Shaolin had existed for a thousand years.

Some even claimed that the Murim had begun with the arrival of Bodhidharma.

It was the holy ground of Buddhism and the central seat of martial arts. Even if Shaolin’s power waned, its deep-rooted history and the respect of the people remained unshaken.

And now a blood wind was going to blow through that very Shaolin Temple.

“W-What do you mean? Hong Dao’s final words? And who would dare to—”

“Hah!”

Kwoooong!

Jeok Cheongang’s shout jolted everyone back to their senses. The Thunderbolt Saber King, who had been rambling, clamped his mouth shut.

“Dark Heaven. They’ve begun to move. If this old man’s guess is correct, we’ll eventually see Jongni Chu—that bastard who deserves to be torn apart—in Shaolin as well.”

“Dark Heaven…!”

Several leaders, including the Thunderbolt Saber King, opened their eyes wide. Judging by their reactions, they had clearly received at least some warning already.

“Do you understand now that every moment is precious?”

Jeok Cheongang turned away from the Thunderbolt Saber King and swept his deeply sunken gaze across the gathering.

“Do exactly as I have said. That is Hong Dao’s final will.”

There was truly no time left to waste. After exchanging a glance, Jeok Cheongang and I simultaneously unleashed our movement techniques and left the area.

Whoooosh!

As I moved my feet against the fierce wind, a cold liquid touched my cheek.

The sky was clear, without a single cloud. There was no sign of rain.

But the eyes of someone running after losing a friend and postponing his revenge must have been brimming with tears.

*No, this is rainwater. I’ll think of it as rainwater.*

*Damn it.*

I clenched my teeth as I thought of Jongni Chu.

*I have a feeling today is going to be a long day.*

* * *

Screeeeech!

“Find the culprit!”

“He could be hiding somewhere nearby!”

“Everyone, calm down. Nothing is going to happen!”

The Murim Alliance was as noisy as a hive someone had kicked apart.

The countless martial artists who had attended the Star-Array Grand Banquet were scouring the surrounding area with fire in their eyes, searching for Jongni Chu, while the commoners moved according to the orders of the people controlling the area, their faces tense with anxiety.

*It won’t do any good.*

They still did not know that Jongni Chu had already fled far away—or that Dharma King Hong Dao was dead.

For a moment, I considered telling them, but I quickly erased the thought from my mind.

*It would only make the confusion worse.*

Besides, I did not have time to go around informing the leaders one by one. It was only a matter of time. They would find out soon enough.

For now, I had to put everything I had into following Jeok Cheongang.

*Fortunately, Shaolin Temple isn’t very far away.*

That was at least one fortunate fact. After passing the preliminary competition, traveling from Mount Song to the Murim Alliance had taken about three shichen by carriage. If we used our movement techniques as we were now, the journey would be shortened dramatically.

Whoooosh!

After racing like a gale for some time, the bustling crowds and tightly packed buildings disappeared. Rice paddies came into view.

As we crossed the broad plain, Jeok Cheongang, who had been leading the way in silence the entire time, suddenly spoke.

“Jongni Chu. Dark Heaven. Unnamed. Buddhist Staff.”

The four words came out in his hoarse voice.

To someone who did not know the circumstances, they would have sounded like a random list of words. But I understood immediately.

They were the answer I had been waiting for.

“Was that Master Hong Dao’s final wish?”

“Yes. Even that took everything he had left.”

“……”

“It would not have been strange if his breath had already stopped. He held on only to deliver those words to me.”

Jeok Cheongang’s voice, which had trembled faintly for a moment, settled again.

“What do you think?”

“It’s as you suspected, Old Master.”

“It is only a suspicion, not a certainty. Speak without leaving anything out.”

“First, the first two words seem to indicate that Jongni Chu is Dark Heaven. That much hardly needs an explanation.”

“And?”

“Unnamed and the Buddhist staff… I’m not sure. To be honest, I don’t know.”

“Do you remember Hong Dao’s Disciple?”

“Oh, of course.”

The memory from a year ago was still vivid.

The young Buddhist monk I had met at an inn somewhere in Henan was none other than Dharma King Hong Dao’s Disciple. He had introduced himself as Unnamed.

*So the Unnamed Hong Dao mentioned was that Unnamed.*

*Was he asking Jeok Cheongang to look after his Disciple in his final moments?*

“But what’s a Buddhist staff? Do you mean those staffs monks carry around?”

Jeok Cheongang nodded.

“That’s right. But the Buddhist staff Hong Dao mentioned was the Green Jade Buddha Staff, Shaolin’s sacred treasure.”

“The Green Jade Buddha Staff?”

A scene suddenly came to mind from the day Jeok Cheongang and Hong Dao had reunited after a long time and chatted with laughter.



*“What choice did they have? They’re the ones who forced the Abbot’s seat on someone who said he didn’t want it.”*

*“The Green Jade Buddha Staff. To entrust Shaolin’s sacred treasure, with its immense authority after a thousand years, to a damn monk like this… They must all have been completely blind.”*



The staff Hong Dao had taken from his robes that day had been absurdly short, and a faint green light had glimmered across its smooth surface.

I had wondered what it was, but I had been quite surprised to hear that it was Shaolin’s sacred treasure.

“But why would he leave the Green Jade Buddha Staff as part of his final words?”

“Not long before his death, Hong Dao told me something. He said he had entrusted the Green Jade Buddha Staff to his Disciple.”

As I furrowed my brow slightly, Jeok Cheongang continued.

“The Green Jade Buddha Staff is not only Shaolin’s sacred treasure. It is also the symbol the Abbot always carries.”

“Ah!”

A short exclamation escaped me before I could stop it. A single thought had flashed through my mind.

Hong Dao’s final words, forced out with the last of his strength.

The reason Jeok Cheongang had turned toward Shaolin, postponing even the revenge for his dearest friend.

“The Green Jade Buddha Staff!”

“That’s right.”

Jeok Cheongang’s low voice continued.

“Dark Heaven’s true objective is not Hong Dao’s death. It is the seizure of the Green Jade Buddha Staff.”

Everything became certain.

Jongni Chu—or rather, Dark Heaven—clearly wanted Shaolin’s sacred treasure.

Hong Dao had squeezed out the last of his strength to leave those final words and reveal that fact.

Now that Dark Heaven knew the Green Jade Buddha Staff was not in Hong Dao’s possession, even a three-year-old child could tell where its path would lead.



*A blood wind will blow through Shaolin.*



As I recalled what Jeok Cheongang had said to the Thunderbolt Saber King, my mind seemed to grow cold.

* * *

“Huff… Hoo…”

Tap-tap-tap-tap!

Ragged breathing. Feet that never stopped moving.

The feet of the middle-aged man racing along the mountain path were halted by an aged voice.

“Looks like something urgent has come up for you, young friend.”

The owner of the voice was an old man with a beard that hung to his chest.

He was quite tall, and his hair was neatly arranged. At first glance, he even looked like a retired scholar.

“The weather is lovely, too. Wouldn’t it be better to walk while taking in the scenery?”

The middle-aged man’s throat bobbed heavily.

His voice, unable to conceal his tension, slipped between his lips.

“Who are you?”

“I’m just an old man who came out for a stroll. I heard the scenery around Mount Song was lovely, so I came here to kill some time.”

“To kill time?”

The middle-aged man shouted through clenched teeth.

“Cut the bullshit! You must be a vile demonic fiend yourself!”

“Hm?”

The old man opened his eyes wide before giving a quiet laugh.

“Young friend, you have quite a fiery temper. Still, you’re much better than the ones I met earlier. They were too busy doing nothing but lying.”

“You met people earlier… Don’t tell me?”

“A woodcutter, an herb gatherer. Why are there so many kinds of gatherers around here? Ah, the pair who disguised themselves as husband and wife to pray for a child were at least convincing. I almost fell for them myself.”

“……!”

“So I killed every last one of them, martial artists and commoners alike. It seemed much easier that way.”

The middle-aged man’s body trembled as though he had been struck by lightning.

There was no doubt about it. The companions who had scattered to deliver the urgent report had already met their deaths.

He would probably suffer the same fate soon.

*At least I should be grateful that my death will not be meaningless.*

Those on the ground had been caught in the net, but the sky was another matter.

That was the moment he found a sliver of comfort while watching a messenger eagle fly powerfully across the plain in the distance.

Screeeeech!

Along with a sharp, strange cry, something black swooped down upon the messenger eagle.

It was three or four times larger at a glance. The battle between the two birds that collided in midair ended far too quickly to leave any hope.

Kreee!

As the messenger eagle plummeted with a final cry, blood seeped between the middle-aged man’s tightly clenched teeth.

“Dark Heaven…”

“Oh? You know us?”

“How could I not? You old bastard who deserves the wrath of heaven and man!”

“Most of those Beggars’ Sect beggars didn’t know. Your martial arts are too decent for you to be Lower District Sect riffraff… That’s it. You’re from the Hidden Shadow Pavilion.”

The old man stroked his beard and lifted the corners of his mouth.

“But I find the phrase ‘deserves the wrath of heaven and man’ a little unpleasant. What do you think?”

“You dare do something like this and still—”

The middle-aged man opened his bloodshot eyes wide and was about to shout when the old man shook his head.

“No, not you.”

Then he raised one withered finger and pointed over the middle-aged man’s shoulder.

“I was asking that fellow.”

“……!”

Crack!

The middle-aged man could not turn his head.

The sky and earth flipped, and his vision shook.

There was only one sensation he felt at the end.

*Hot.*

Fwoosh. Thud.

The charred corpse collapsed.

Then someone’s foot crushed the head of the middle-aged man, now reduced to a lump of charcoal.

“Han Su, you bastard. What kind of bullshit are you pulling? You’re off playing with trash like this.”

The owner of the rough voice was a stocky old man. His beard had grown wildly, and, strangely enough, it was red.

At the appearance of an old friend who had been with him for decades, the old man who looked like a scholar smiled faintly.

“I was just about to wrap things up and leave. How are things up there?”

“Pretty busy having fun. Oh, apparently that Disciple of his has the Green Jade Buddha Staff.”

“Really? Then let’s go together, Flame Tiger.”

The two men exchanged faint smiles and began walking at a leisurely pace.

With every step they took, the screams coming from Shaolin Temple drew closer.

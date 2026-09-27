# Checkpoint Review — 1150–1154

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

# Chapters 1150–1154

## Plot

Vladimir Furin rejects Morgoth’s demand for surrender and triggers his secret Magic Gem-powered weapon, Vladimir. The blast destroys Moscow, but Morgoth survives and uses the released energy to build a Dragon Lair over the ruins. Furin’s final warning—that Jin Taekyung’s return will mean Morgoth’s end—only makes Morgoth look forward to facing him.

As footage of the destruction spreads, the United States President announces that the returning savior has come back. Jin watches the devastation and learns that Pie Chen died fighting Morgoth a week earlier, saving Chuck Hagel. Jin vows to prevent further sacrifices. At the Pentagon, he and President Donald Doramp Jr. discuss the crisis: twenty-three countries have surrendered, and U.S. preparations depended on the still-comatose Cheon Taemin. Jin struggles with guilt over arriving too late.

A recording shows Morgoth opening a Gate from the Demon Realm above Moscow. A vast monster army pours through and advances across Russia. Morgoth offers survival under his rule in exchange for surrender, demands Cheon Taemin and Jin as tribute, and gives humanity three days. The UN’s announcement of Jin’s return briefly raises hopes, but footage of the advancing army leaves people shaken.

## Continuity

- Morgoth destroyed Moscow with Furin’s weapon and opened a Gate from the Demon Realm above the ruins. A vast monster army is advancing across Russia.
- Morgoth offers survival to those who surrender and threatens destruction to those who resist. He demands Cheon Taemin and Jin Taekyung as tribute within three days.
- Cheon Taemin remains unconscious. Jin has returned and is widely regarded as a new-age savior.
- Furin’s weapon, Vladimir, was a Tsar Bomba transformed through decades of Magic Gem experiments and magical engineering. Morgoth is the sole survivor shown.
- Pie Chen died a week earlier after refusing to follow Morgoth and making a last stand. Chuck Hagel survived because of her sacrifice and has only his right arm left.
- Twenty-three countries have surrendered to Morgoth. The Arab League and some major South American countries are among them.
- The System notification shown to Jin remains unexplained.

## Translation Decisions

- Render 차르 봄바 as “Tsar Bomba,” 블라디미르 as “Vladimir,” and 드래곤 레어 as “Dragon Lair.”
- Render 파이 첸 as “Pie Chen,” 흑룡공 as “Black Dragon Duke,” and 소멸 as “Erasure.”
- Render 도널드 as “Donald” in Donald Doramp Jr.’s name.
- Render 외교 as “Diplomacy” for Morgoth’s distinctive ability to secure surrenders through genuine promises.
- Render 은빛 산 as “Silver Mountains,” 마계의 대공 as “Archduke of the Demon Realm,” and 모르고스’s command ᚨᚾᛊᚹᛖᚱ ᚦᛖ ᚲᚨᛚᛚ as “Answer the call.”

## Durable state

{
  "active_continuity": [
    "Morgoth destroyed Moscow and opened a Gate from the Demon Realm above its ruins; a vast monster army has invaded Earth and is advancing across Russia.",
    "Morgoth offers survival under his rule to those who surrender and demands Cheon Taemin and Jin Taekyung as tribute within three days.",
    "Cheon Taemin remains unconscious; Jin Taekyung has returned and is widely regarded by humanity as a new-age savior."
  ],
  "continuity_sources": [
    1154
  ],
  "open_questions": [
    "How will humanity respond to Morgoth’s surrender offer and demand for tribute?",
    "Can Jin Taekyung stop Morgoth and the invading army?",
    "What did the System notification shown to Jin Taekyung say?"
  ],
  "safe_through": 1154,
  "temporary_decisions": [
    "Render 은빛 산 as “Silver Mountains” and 마계의 대공 as “Archduke of the Demon Realm.”",
    "Render 모르고스’s command ᚨᚾᛊᚹᛖᚱ ᚦᛖ ᚲᚨᛚᛚ as “Answer the call.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 1150

# Chapter 1150

A handshake.

The act of two people reaching out and clasping one another’s hand—a greeting practiced more widely than any other around the world.

But the moment their hands met, Vladimir Furin felt every handshake he’d exchanged tens of thousands of times over the course of his life vanish from his mind.

“……!”

Cold. Hard.

Steel?

No.

The man—no, Morgoth’s hand closed around his as if it were made of a substance that had never existed in this world. Then it began to move slowly up and down.

Carefully, as if handling an ant in his palm.

When the brief handshake ended, a satisfied smile touched the monster’s lips.

“Just as I thought. The humans of this world are fascinating.”

A short sentence, but one that carried a great deal.

Furin wondered if he’d heard correctly, then opened his mouth.

“What… do you mean?”

“Is an explanation really necessary?”

Morgoth sat down naturally in the seat across from him and swept his gaze over the items on the table, his eyes full of wonder.

“An astonishing civilization, no matter how many times I see it. The humans in the world where I once stayed could never have dreamed of anything like this.”

“……!”

“I didn’t expect you to react like that. You already suspected it, didn’t you? That somewhere out there, another world like the Demon Realm existed.”

Morgoth was stating an undeniable fact.

Since the Great Cataclysm, countries around the world had continued to conduct countless behind-the-scenes studies into whether other worlds existed—worlds apart from the Demon Realm. Those studies were still ongoing.

But a suspicion was not the same as certainty.

Morgoth had just confirmed that another world, previously nothing more than a hypothesis, truly existed.

And told him where he had come from.

*Could it be?*

Furin thought.

What if the monster before him wasn’t simply a creature mad with bloodlust?

If that were true, there was a very real chance they might still be able to contain the nightmare that had been unfolding for the past ten days, even at this late hour.

“Then you—no, sir. Did you come from the other world you mentioned?”

Morgoth answered readily.

“That may be true, or it may not.”

“What does that mean?”

“I told you. I said I once stayed there.”

“Then…”

“Of course, the humans of that world had their share of interesting qualities. But as time went on, everything began to bore me. It was time for a change. A powerful, decisive change.”

As if he understood the meaning behind those words, Furin’s eyes widened. Morgoth smiled gently at him.

“So I left. For the Demon Realm.”

“……!”

“Entering someone else’s service wasn’t especially pleasant, but in the end, it was an excellent choice. I’ve had the chance to experience such an interesting game, after all. Don’t you agree?”

In that moment, Furin felt the hope that had been burning like a tiny flame disappear without a trace.

“……A game?”

“Yes. A game.”

“Then everything you’ve done up to now was this grand game of yours?”

At the unmistakable tremor in Furin’s voice, Morgoth let out a small sigh.

“Humans really are human.”

“What?”

“Good heavens, a game? Don’t judge me by such a base way of thinking. It was simply punishment.”

“Punishment? What are you—”

“Ignorance is a sin, too. If they had bowed down and obeyed from the start, none of this would have happened. But they rejected my generous offer, so I had no choice but to give them a fitting punishment. That’s all.”

At last, Furin understood.

Just how much darkness—how much madness—lay within the being before him.

A game? Punishment?

Both were wrong.

Everything Morgoth had done was a catastrophe and a massacre on a scale unseen since the Great Cataclysm had ended.

There had been several major incidents since the Arch Lich appeared about a year ago. But compared with what had happened over the last ten days, they were a drop in the bucket.

Estimates already put the number of dead and injured at fifty million.

The Middle East—more precisely, North Africa and West Asia—had already become a land of death with the Black Dragon’s arrival.

Those who resisted were slowly rotting or had become undead. The survivors became slaves, swearing absolute obedience.

Not Hunters chosen by God. Not even heavily armed armies.

No one could break the Black Dragon’s massive wings.

This world already belonged to him.

“You’re insane. Completely insane.”

Vladimir Furin muttered weakly.

Then Morgoth’s smile deepened.

“Insane? Me?”

“Are you going to deny it? After killing so many people?”

“Of course not. I’m simply disappointed beyond words.”

The Black Dragon’s eyes, like the depths of an abyss, fixed on the dictator before him as if to pierce straight through him.

“How can someone like you dare to say such a thing?”

“……!”

“Of course, I understand to some extent. I know from experience how shallow humans can be—and how wealth and power corrupt you. But…”

Ting.

A long, pale finger tapped the teapot. The tea once considered almost synonymous with Furin rippled inside.

“Spare me the half-baked hypocrisy. It’s an insult to my intelligence.”

“You—you…”

“Yes, I already know a great deal. Though it would be more accurate to say I learned it through you.”

He had lived for an immensely long time.

A time beyond imagining.

Yet even to Morgoth, the modern world of the twenty-first century was deeply fascinating.

Human history. The fusion of Magic and technology. The structures and ideologies of governments.

And the countless conflicts, large and small, that had taken root all over the world as a result.

This new form of civilization, unlike anything he had seen before, was more than enough to stir his thirst for knowledge. His mind, which knew neither forgetfulness nor limits, absorbed everything he saw and heard in an instant.

Among it all was information about a certain dictator who ruled the largest territory in the world.

“I found it impressive. In more ways than one.”

In that moment, Vladimir Furin felt his mind grow strangely calm.

The monster before him, a living calamity, the Dragon, already knew everything about him.

No—perhaps even more than he could imagine.

Whether that knowledge came from information Morgoth had gathered while laying waste to the Middle East and other parts of the world, or from what was stored on a tiny smartphone, no longer mattered.

All that remained were fate and choice.

And so the old dictator of the Russian Federation finally lowered the mask of hypocrisy he’d worn to the very end.

“So? Did you come here hoping to get my autograph?”

“Oh, you’ve become quite composed.”

“I have no reason to feel ashamed.”

“Good. Now I feel my visit was worthwhile.”

Morgoth looked at Furin with amusement, then continued.

“Then I’ll be direct. Surrender.”

“Become a slave?”

“Well, this world has a fine word for it: citizen.”

“But in reality, they’re slaves. Everyone knows what happened to those who surrendered to you.”

“Then this will be easy. You must know that countless humans survived thanks to the peaceful, wise decision to surrender.”

“You still don’t understand humans very well. We don’t consider scraping by day after day like mere ants to be living. And we certainly don’t want to be raised like livestock behind a fence and then slaughtered.”

It was a shameful thing for a dictator to say—one who had spent more than fifty years in power tightening his grip through control and oppression—but Furin didn’t care in the slightest.

No. His shrewd eyes gleamed as he continued to address Morgoth.

“I trust that’s answer enough. So let me ask again. Why did you really come here?”

“What?”

“Truthfully, I’ve been wondering this all along. Why would someone like you go to all this trouble? And let me make this clear in advance: don’t give me any nonsense about it being a game.”

The cigar had been lying neatly on the table. Furin picked it up and lit it.

Through the slowly rising smoke, he stared straight at Morgoth.

“After talking to you, it makes even less sense. You treat humans like livestock or ants, yet you’re trying to negotiate and conduct diplomacy this way? Well, whatever your true intentions, I find it hard to believe you.”

Different species could still follow the same path.

In that sense, Vladimir Furin thought that he and Morgoth were rather alike.

They were rulers.

Even if the gap between them was as wide as the sky and the earth, Morgoth, too, must have tyrannized countless people from a position of power.

And as far as Furin knew, anyone with overwhelming power had no need for conversation.

Shamelessness became a natural virtue, while shame turned into something as old and musty as a grandfather’s letter forgotten in a drawer.

If a mere human like him was that way, then what about a Dragon whose basic sense of the world was different?

Besides, Morgoth wasn’t the first Dragon to set foot in this world.

“Your kind destroyed Paris during the Great Cataclysm. That one was more vicious and merciless than any monster.”

Morgoth replied calmly.

“I think I know who you mean. There are a few like that.”

“The day of the battle against it, there were a million casualties. A thousand Hunters led by no fewer than four S-ranks died as well.”

Another monster, Michael Silbert, was born where the Dragon fell—but that had only been discovered recently.

Furin put the cigar, its tip now evenly lit, between his lips and added:

“So why would you, with power far greater than that young Dragon had, go to such lengths?”

A moment of silence settled over them, but it didn’t last long.

Even if the one asked didn’t answer, the one who’d asked already knew the answer.

“You’ve realized it, too. That you can’t fight every human. No, to be precise…”

Fwoosh.

Exhaling a thick cloud of cigar smoke, the old dictator, already prepared to lose everything, smiled.

“You’re afraid of someone you haven’t found yet.”

At that moment—

Click. Rrrrrumble.

As the small button that had been concealed in Furin’s wrinkled hand was pressed, a tremendous rumble rose from deep beneath the Kremlin.
## Chapter artifact 1151

# Chapter 1151

The moment he activated the secret device that only one person in the world was permitted to use, Vladimir Furin muttered to himself.

*This is as far as I go.*

Was he reluctant to let go of life? Afraid of death?

Of course he was.

The more a person had, the harder it was to let go. That was human nature. And for a man who had ruled as a dictator for nearly half a century, there was no need to ask.

He wanted to live.

He had to live.

He had to raise the name Vladimir Furin to the level of a god.

He had to become greater than the tsars, who had ruled this land for generations through their noble blood, and greater even than the Iron Marshal, against whom no one had dared rebel.

But if that proved impossible—

If someone else appeared and tried to take everything he had built—

*I’ll burn it all down. With my own hands, so no one else can have it.*

The old dictator, who had dreamed of immortality, smiled faintly.

Or rather, he tried to.

Time slowed, stretching out like a passing life flashing before his eyes. Then he saw the looter wearing a vivid smile.

“You really are an interesting human.”

“……!”

The moment his shrewd eyes flew open—

Rrrrrumble.

The enormous rumble, as if it would swallow the Kremlin—or Moscow itself—drew closer.

Slowly. Deliberately.

As though it moved at someone’s will.

At last, Vladimir Furin saw the source of this unexpected phenomenon with his own eyes.

Wooooom.

Would a swarm of thousands, tens of thousands of bees tangled together sound like this?

Furin could only stare blankly at the vortex of flames as it rose from the melting floor of his office.

Everything was red. Everything was hot.

Surrounded by an aura as dark as pitch, it had been compressed into a great sphere, blazing like a tiny sun.

And the old dictator staring at the sight in shock knew better than anyone that “tiny sun” was no exaggeration.

He also knew that a power once great enough to terrify the entire world was now in the grasp of the monster smiling at him.

*Tsar Bomba.*

The most powerful weapon in human history.

The mother and emperor of all bombs.

Only a handful of people involved knew that the most powerful hydrogen bomb of the Cold War—the one that had frozen the five oceans and six continents with fear—lay sleeping deep beneath the Kremlin.

They also knew that decades of secret experiments, carried out on the dictator’s orders, had given it a new name and destructive power far beyond anything it had possessed before.

“Remarkable. Truly remarkable. To create such powerful force. What do you humans call this weapon?”

At Morgoth’s genuinely awestruck question, Furin—sensing that everything was over—answered in a hollow voice.

“Vladimir.”

“What?”

Morgoth looked from the old dictator, already all but fallen, to the catastrophic power named after him, then burst out laughing.

“That’s a masterpiece. Or should I say, very like you?”

Morgoth found it truly amusing.

A human granted barely a hundred years could harbor such enormous ambitions.

And that these mere mortals had tried to kill him, a being with power close to immortality, using a weapon they had made.

“Did you think this alone could bring me down? With Magic Gems taken from lowly monsters, you dare challenge me?”

At Morgoth’s words, which seemed to reveal he had already seen through everything, Furin quietly swallowed.

He was right. Tsar Bomba—or rather, the weapon now given the new name Vladimir—was not merely a product of science.

The Great Cataclysm.

After that world-shaking event had overturned all the laws and common sense of the world, one thought had taken root in the mind of the dictator who had barely survived.

*I have to become stronger. So this can never happen again. So we can win any war.*

And the means were close at hand.

Magic and Magic Gems. The new knowledge born from them: magical engineering.

And so Tsar Bomba became Vladimir.

As one of the world’s great powers—and a dictatorship at that—the country had countless ways to obtain Magic Gems for experiments.

Of course, that meant violating more international treaties than anyone could count and killing even his own scientists and mages to keep everything secret…but what did that matter?

Mother Russia.

Russia—or rather, he—had to become greater still.

Even if a second Demon King descended, he and Russia alone had to survive and rewrite the world order.

*Or die together.*

Yes.

That was how it had to be.

Plop.

Ash fell away in clumps.

The decades he’d spent avoiding cigarettes counted for nothing. Furin had barely taken a few drags from the cigar. He stared at it, then suddenly spoke.

“What are you going to do now?”

Morgoth didn’t answer.

But Furin immediately understood the meaning behind the gentle curve of his lips.

“Right. It has nothing to do with me anymore.”

The cigar trembled.

No—it was Furin himself who was shaking.

“Any last words?”

At Morgoth’s kind offer, Furin raised his trembling hand and brought the cigar to his lips.

Then, after taking the deepest drag of his life, he blew the smoke toward the monster before him.

“No. But there’s one thing I have to tell you.”

Along with the name of the man who had crossed his mind just before he activated the bomb named after himself.

“If Jin comes back, you’re finished.”

At that moment—

“I look forward to it. Truly.”

Swoooosh.

With Morgoth’s calm reply, the pitch-black aura restraining the catastrophic power slowly dispersed, then enveloped its master.

Like the touch of death announcing the end of this land.

Whoosh.

A blinding flash swallowed the old, wretched dictator’s final sight.

It was warm.

* * *

Eight meters long. Two meters in diameter. Twenty-seven tons.

Its destructive power packed into a volume that could fill a large truck: 50 Mt—fifty million tons of TNT.

Those were the figures publicly known for the Tsar Bomba.

Its power could make the Little Boy that had turned Hiroshima into a land of death during World War II seem like a little boy indeed.

But no one had expected it.

No one had expected this monster from a bygone era, born of the Cold War’s arms race, to awaken again more than eighty years later.

And no one had expected the monster’s first cry after its long sleep to ring out from the Kremlin.

Gooooom.

The air trembled in an instant.

Everyone in the Kremlin—or rather, everyone in Moscow—felt that deep, ominous rumble.

The soldiers and Hunters holding their posts as they suppressed their fear. The citizens who had fled into bomb shelters and out onto the streets as Red Square collapsed.

No one was spared.

Everyone felt it and instinctively understood.

This was the last moment they would ever draw breath.

And then—

Whoooosh.

There was light.

A terrible heat beyond human perception, atomic power mingled with potent energy drawn from countless Magic Gems—it all spread out, devouring everything in its path.

Without end. Without restraint.

Kraaaaaash!

In the storm of power, everything melted.

The living died. The lifeless lost their shape.

Underground or aboveground, whatever life they had lived—it didn’t matter.

The blinding light that burst from the Kremlin made everyone equal.

Just as Icarus, who had flown too close to the sun, lost his wings and fell, the tiny sun born of a dictator’s ambition and fear swallowed countless lives, including its creator.

All of them, save one.

Rrrrrumble.

At the heart of the rumbling that shook everything around him, Morgoth lifted his head and surveyed the scene he had created.

Nothing remained.

Everything that had surrounded him just minutes earlier was gone.

Melted metal flowed like rivers, and above it rose a massive mushroom cloud, looming over the surface now transformed into a land of death.

It was quite a sight.

“Such power. I didn’t even need to use Breath.”

Morgoth felt both admiration and regret.

How could mortals be so greedy and yet so foolish?

They had saved him a great deal of trouble, but the place now shadowed by calamity was desolate beyond measure.

A city with a long history and a population of over ten million had become a land where nothing could live for hundreds of years.

“But birth awakens from within death.”

The moment Morgoth spread both hands with those quiet words—

Pop.

The air stopped. The wind stopped.

And the Magic Gem energy that had swept across the city with a deadliness greater than radiation changed in response to his will.

Darker than before. Purer still.

Wooooom.

Dragon.

Great beings blessed by mana from the moment of their birth.

Space trembled at Morgoth’s fingertips. He had been revered as the greatest of them, yet in the end he had chosen corruption of his own accord.

Gathering. Packing together. Rising up.

And at last—

Rrrrrumble.

It was built.

A gigantic castle, unlike anything ever seen in this world.

His own kingdom.

In place of concrete and marble, it stood upon pitch-black earth amid air saturated with dense magical power. It was overwhelming, yet beautiful. Morgoth smiled as he gazed at its spire piercing the clouds.

Or, more precisely, at the camera lens of the drone hidden in the thick black clouds, watching him.

“Have you seen it, humans?”

That day, people all over the world saw it.

They watched Moscow disappear and a Dragon Lair come into being.

The calamity that had reached their doorstep.
## Chapter artifact 1152

# Chapter 1152

There are no secrets in modern society.

There are cameras and the internet everywhere, and countless pieces of information spread across the world through them.

And sometimes, there are truths that are better left unknown.

Like a Pandora’s box that should never have been opened.

—KABOOOOOM!

The screen went black after one last deafening roar, too terrible to be captured in its entirety even by the speakers.

The viewers watching a famous influencer’s livestream from near the Kremlin instinctively realized that the video, which had just passed one hundred million simultaneous viewers, had made internet-broadcasting history—and that they would never see the influencer who had set this incredible record again.

“Oh, God.”

A single line suddenly appeared in the chat window, which had been frozen for several seconds. It was enough to explain everything they had seen and felt over the past thirty-odd minutes.

The dragon’s wings as it crossed the skies above Moscow, and Red Square vanishing without a trace.

Ironically, the creature had transformed into a human like them, slaughtered the Hunters and soldiers who blocked its way, and strode confidently into the Kremlin.

And then…

The disaster that engulfed Moscow.

Rrrrrumble!

The reverberation carried hundreds, even thousands of kilometers, shaking the world beyond the rectangular screen.

Countless eyes and ears—and even more cameras—captured the distant flash of light and the enormous mushroom cloud. The footage was immediately compiled into a single video and uploaded to the internet.

Its title conveyed the overwhelming despair and shock felt by humanity as the news from Moscow reached them.

—Where is God?

Where was God?

No one could answer that question.

No one.

They could only pray with all their hearts.

If God had truly abandoned them, then may someone appear who could save them.

No.

May he wake from his deep slumber as soon as possible.

Unlike God, who was so far away that their voices could not reach him, the savior of the new age answered their desperate pleas before long.

“He has returned.”

The whole world erupted once more at the first words spoken by the flushed-faced fifty-seventh President of the United States on the holographic TV.



* * *



The modern world meant something special to me.

It was the home where I’d been born and raised all my life—a place I could never forget.

That was why I’d always loved it.

Compared to Murim, where danger and trouble lurked around every corner, the modern world let me rest in relative peace.

But when had it started?

Everything began to go wrong, like a broken gear.

And the speed and fallout of that unraveling were worse and more horrifying than I could have imagined.

“So…”

What the hell was I supposed to say?

I kept trying to think, muttering words that meant nothing, but my mind had gone completely blank. Nothing came to me.

The hour-long video had just ended.

In the holographic footage, already paused, a black-haired man smiled faintly at the camera. I stared at him in silence.

Hoping someone would break the heavy quiet.

“I hear it happened three hours ago.”

At Magic Johnson’s low, subdued voice, the words I’d been holding back slipped past my dry lips.

“How many casualties?”

“……”

“Tell me. I’m prepared for it.”

Magic Johnson let out a quiet sigh before answering.

“At least twenty million, by the most conservative estimate.”

“Shit.”

“Moscow, and the surrounding cities in the metropolitan area, were swept away. We’ve thrown every resource we have at investigating, but…”

Magic Johnson trailed off and bit his lip.

“There are no signs of life. They’re probably all dead.”

Erasure.

The word flashed through my mind. It was also the most accurate way to describe what had happened.

“Vladimir. That fucking old man hid a hydrogen bomb in the Kremlin.”

At the start of the Great Cataclysm, humanity learned two very important things.

First:

No matter how airtight the security, modern science couldn’t stop spatial teleportation magic.

Second:

Spatial teleportation magic could move things, not just people.

Things like tactical nuclear weapons or hydrogen bombs.

That was why every nuclear-armed country in the world, led by the United States and Russia, had signed an international treaty and disposed of all weapons above a certain yield.

Or, to be precise, that was what we’d been told.

Until three hours ago, when a giant mushroom cloud swallowed the sky above Moscow.

“Russia is finished.”

That was true.

And for every other country, a different kind of beginning—and a crossroads—still lay ahead.

Would they resist to the bitter end?

Or surrender now and save their lives?

*Black Dragon Duke Morgoth.*

I murmured the name in my mind as I stared at the holographic screen.

On the land, blackened by magical power, a gigantic castle towered behind him. I took in his smiling face and burned it into my heart.

*Can I defeat him?*

The question came to me naturally. I realized my hand had clenched into a fist.

Dragon.

A monster without precedent, whose single appearance in the past had sent shock waves around the world.

But as his special title, Black Dragon Duke, suggested, Morgoth was no ordinary dragon.

*He’s strong. Horrifyingly strong.*

I turned my head and looked at the dozens of holographic screens filling the spacious monitor room, one after another.

They showed a predator that could bring down a forest of skyscrapers with a single flap of its wings, effortlessly deflect a barrage of magic, and trample Hunters underfoot.

Among those dying with one last scream were faces I knew.

“Die! Just die!”

On a crackling screen, a bloodied woman screamed.

Her lower body had already been crushed beyond recognition, and her stomach was split open, her entrails spilling out.

But, dazed, she kept drawing her bow at the rear of the retreating allies.

Until the dragon’s claws rushed in faster than an arrow and took both her arms too.

Crunch!

Blood spurted along with the severed flesh.

A deep shadow fell across the woman’s face, twisted with unbearable pain.

“You foolish human. Didn’t you know this would happen?”

The Black Dragon’s question rang down from high above. The woman spat blood and answered.

“I did.”

“Then why?”

“Because we were taught this is courage. Not foolishness.”

“Good. Then, brave human, will you still follow me?”

“Fuck off, you monster. And…”

The woman grinned, baring her blood-soaked teeth.

“My name is Pie Chen. I’m not just some human. I’m Pie Chen.”

“I’ll remember that, human.”

“You’d better. Soon, some amazing guy’s gonna come looking for you and ask about that name. Ask about my name, my—”

Her voice faded, and her panting stopped.

Her unfocused eyes stared into empty space.

The woman—no, Pie Chen—died just like that.

She was an S-rank Hunter Hong Kong was proud of, a hero of the last Great Cataclysm, and my friend.

She’d died a week ago.

*How about we all grab a drink?*

The memory surfaced without warning.

The day we first met in Sichuan to hunt the Arch Lich. She’d suggested we get together for drinks.

I’d asked her, “Why today of all days?” Her answer came back to me.

“Today’s the kind of day you drink.”

“Huh?”

“It might be our last chance.”

That day, we drank until we could barely stand.

Never once thinking it really might be our last drink together.

“She was a good person.”

A voice suddenly broke into my thoughts.

It was rough and gravelly, a little different from Magic Johnson’s deep voice.

“And a great Hunter.”

I didn’t ask who the unexpected visitor was.

The acrid smell of cigar smoke had seeped in a step ahead of him, before the door to the monitor room even opened. I knew who the voice belonged to.

“Thanks to her sacrifice, a lot of people survived. Even one bastard who came back alive in disgrace was among them.”

Chuck Hagel.

Also known as Uncle Chuck, he approached slowly and put a hand on my shoulder.

With his right arm—the only one he had left.

“The moment I woke up, I thought I should’ve died in Pie Chen’s place.”

“...Hagel.”

“I know. It’s all meaningless bullshit. And I’ve repeated that bullshit hundreds—no, thousands of times by now.”

Chuck Hagel blew out a cloud of cigar smoke and gave a bitter smile.

He looked at the familiar faces and the deaths playing over and over on the dozens of holographic screens.

“I swore I’d never let something like that happen again… And now look.”

What was I supposed to say?

No. What right did I have to say anything?

Whenever I needed them, they came running without hesitation. But when they needed me, I hadn’t been there.

I hadn’t stopped Morgoth from being summoned, and I hadn’t realized soon enough that the axis of time had shifted.

And this was the result.

The destruction and deaths carried out indiscriminately over the past ten days.

All of it weighed on my heart, heavier than I could bear.

Along with the anger roiling deep in my gut like lava.

“You know what?”

I let out the breath I’d been holding.

Reason and emotion tangled together, and then my mind turned cold.

At the same time, Pie Chen died again before my eyes.

“From now on, I won’t let anyone else be sacrificed.”

I stared at her on the screen, my eyes burning.

At her, using what little breath she had left to warn Morgoth that someone was coming for him.

Yes.

That’s exactly what would happen.
## Chapter artifact 1153

# Chapter 1153

Everyone dies.

No matter how much wealth and fame a person amasses—more than anyone else in the world—or how strong their body and mind become, until they’re called superhuman, they can never escape the shadow of death.

That was why we had no choice but to accept, however painfully, the tragic news of our close companions’ deaths.

No. We had to.

The reality right in front of us was simply too horrific to give in to our emotions.

“That concludes the briefing.”

The lights came on with the presenter’s exhausted voice, but the heavy silence pressing down on the room didn’t disperse so easily.

Not until someone who had kept silent throughout the meeting finally spoke.

“Rest is important, isn’t it? Especially at a time like this.”

It was a simple remark, but no one failed to understand what lay beneath it.

Anyone that oblivious wouldn’t have been allowed in this room in the first place.

“I can finally breathe a little.”

The conference room had at last emptied out. A middle-aged man walked over to the coffee machine tucked in one corner and glanced at me.

“Would you like a cup, Mr. Jin?”

His hair was greasy and disheveled, and dark circles ringed his eyes.

He looked like an office worker worn down to the bone by exhaustion. I shook my head at his offer.

“No, thank you, Mr. Presi—”

“You can just call me Donny.”

“Sure. Donny.”

At my matter-of-fact reply, Donald Doramp Jr., the fifty-seventh President of the United States, smiled faintly.

Even that was only a forced smile that appeared for a moment before vanishing without a trace.

*Of course it was.*

My eyes drifted to the hologram still hanging in the air—the catastrophic casualty figures enough to rob even a thoroughly jaded politician of a smile.

“The first time I received a report about it at the White House, I thought, ‘Is this a dream?’”

He downed a coffee heavily laced with potions and continued.

“To be honest, I still think the same thing. I keep hoping all of this is one goddamn nightmare.”

But this was reality. The numbers in the reports hadn’t leveled off; they’d climbed higher with every passing day.

Property damage in the tens of quadrillions. Tens of millions dead or injured, and even more refugees. The whole world was in a panic.

“That’s why I had to announce as soon as possible that you’d returned.”

As he said, the international community had moved quickly.

The UN Security Council, led by its permanent members, had immediately issued an emergency statement. News of my return spread around the world after I’d gone missing in the Middle East.

Before I, the person at the center of it all, had even arrived here at the Pentagon.

“Some people thought announcing it during the discussions was premature. But given the circumstances, we had no choice. What if we made the wrong call—”

“No. You didn’t.”

I waved off the President’s apology.

Because it was too late to put the genie back in the bottle now?

That was part of it, of course.

But if the news of my return hadn’t gotten out, people would have been swept into an even more uncontrollable maelstrom.

Disaster, after all, takes root in fear and confusion.

And the seed of that disaster had already blossomed.

All because of an unprecedented monster: Black Dragon Duke Morgoth.

“Jin, I’ve handled countless major crises over the past twelve years as President of the United States. But there’s always been one matter that came before all the others—the most important priority.”

I knew the answer before he could continue.

Ever since Demon King Asmodeus descended upon this world, every country had been facing the same problem.

“The war against monsters.”

Donald nodded at my words, spoken almost under my breath.

“That’s right. The Gates that remained after the Great Cataclysm, and the preparations for a possible second Great Cataclysm—they were our top priorities.”

He stared silently down at his empty coffee cup, then added weakly, “And our preparations failed. Or, more precisely…”

“Something showed up that was too strong for us to handle, even though we were preparing for it. I understand.”

Morgoth was that powerful.

Even if the footage didn’t show all of his strength, what I’d seen onscreen was beyond anything any named monster had displayed from the Great Cataclysm up to now.

There was only one being who could compare.

No one but the absolute evil known as the Demon King Asmodeus—the one called not merely a calamity, but the end of the world.

And besides…

“But your preparations couldn’t be complete without *him* there, could they?”

Donald nodded gravely.

“That’s right. Our plan lost its strength when Sky fell into a coma.”

Sky. Cheon Taemin.

If two atomic bombs had brought World War II to an end, Cheon Taemin had saved all of humanity by weathering the Great Cataclysm with his own body.

*Right. Just as the Martial God did.*

I swallowed the words on the tip of my tongue. Donald continued.

“But Sky’s absence isn’t our only problem. Morgoth’s power is a calamity all on its own…but he has something no other monster can compare to.”

Once again, I knew the answer.

“Diplomacy.”

“So you’ve noticed it too.”

“I’ve dealt with monsters enough to be sick of them.”

I couldn’t remember every meal I’d eaten in my life. In the same way, I’d taken down too many monsters to count, going all the way back to my days as an F-rank Hunter.

So I knew.

No matter how intelligent they were, no matter how strong they were, monsters were born with an instinct to kill.

*If anything, the stronger they were, the more they wanted to crush everything beneath them. They tried to solve everything with overwhelming force.*

Of course, there were exceptions.

The Skeleton King, who wasn’t here, was one. And the Doppelganger, who had helped set Morgoth’s summoning in motion, had long ago infiltrated human society and operated in secret.

But Morgoth was different.

He wasn’t just bluffing or tricking people. He offered surrender in earnest, and if they accepted, he guaranteed their survival.

*A monster that keeps its promises.*

His actions had caused more division than ever before.

“Twenty-three countries have already surrendered to Morgoth. Besides the Arab League, which suffered the heaviest losses, some major South American countries have given up resisting.”

“The Middle East has more or less fallen, but South America too?”

“The Moscow incident had a huge impact. We did everything we could to contain it, but we couldn’t stop the information from spreading.”

Disaster breeds fear, and fear leads to fractures.

Faced with the most powerful desire of all—survival—people were crumbling one after another.

“A similar thing happened early in the Great Cataclysm, but this is different. Everyone’s shaken.”

The reason humanity had managed to bring the Great Cataclysm to an end with a victory was simpler than you might think.

They united.

Ironically, it was their enemy, Asmodeus, who made that possible.

He truly lived up to the title of Demon King.

He killed those who resisted and those who surrendered.

He burned down cities and overturned mountains and seas.

Compromise? Promises?

To him, it was as if a cockroach found in his house one day had sworn to obey him in exchange for living together.

That was how humanity had been able to fight back with all its strength, united in purpose.

Fortunately, they had Cheon Taemin, a savior, and no other choice.

*But Morgoth kept his promises. Unlike Asmodeus.*

He took human form and followed human customs.

For those who resisted, he offered devastating destruction and death. For those who surrendered, he guaranteed survival.

Like a cruel conqueror from the Middle Ages.

“If you hadn’t appeared in time, I might be signing the goddamn surrender documents by now.”

President Doramp gave a bitter smile, but I couldn’t smile. My thoughts were tearing through my head.

*I came in time? Me?*

I didn’t know.

What if I hadn’t lost consciousness after defeating the Blood Lord?

If I’d woken up even a day earlier—or tried to log out just a few hours sooner…

*Drip.*

Blood drops fell, one after another. It was running from between my fingers where I’d clenched my fist without realizing it. After a brief silence, President Doramp spoke.

“Jin, what’s done is done. And nobody blames you. Unlike you, we were all in our own places, and we still couldn’t stop Morgoth.”

I knew.

Ever since I’d gained powers unlike anyone else’s, I’d struggled at every turn. And as a result, I’d saved countless lives.

But the sudden surges of anger and self-blame still refused to fade.

*They probably won’t, even after everything is over.*

People called me the savior of a new age, but I was only human, just like them.

I fixated on what I’d lost instead of what I had, and feared the danger that was coming.

And that danger was closer than I thought.

“Mr. President!”

An aide rushed into the conference room. Behind him were several familiar faces.

Every one of them wore a tight expression, their eyes downcast.

The air froze in an instant. At the aide’s touch, a holographic video sprang into the air.

*Pop.*

Through the constant crackle of static, a landscape tens of thousands of kilometers away filled the vast conference room.

A Dragon Lair rose over the blackened earth once known as Moscow, blocking everyone’s view.
## Chapter artifact 1154

# Chapter 1154

Everything in my field of vision was dark and murky.

The magical power that had erased even the radioactive fallout drifted about as a blackish fog, and the walls arranged in the shape of a pentagram towered like mountains.

And—

Goooooong.

At the center of it all stood that bastard.

Black Dragon Duke Morgoth.

KWAaaaaa!

In a moment split into ever smaller fractions, a gigantic black dragon opened its jaws, and an explosion of magical power burst forth.

A pitch-black pillar shot up from the highest spire and stretched endlessly onward.

Piercing the clouds, cleaving the sky in two, as if it meant to reach the distant, faraway moon.

No—maybe it really could.

It was the breath of the most powerful living creature in the world, and a roar filled with rage.

*Dragon Breath…!*

I barely managed to suppress the groan rising between my lips.

It was only a video, but the tremor and atmosphere within it were enough to awaken my instincts.

This was different.

I could say with certainty that it was on an entirely different level from any Breath I’d ever seen or experienced.

My heart was suddenly pounding wildly, the fine hairs all over my body stood on end, and the blood in my veins felt cold as ice. They bore witness and passed judgment.

The One-Eyed Black Wyvern that had left me with an indelible trauma years ago.

The Water God Dragon of Dongting Lake, corrupted and driven mad by magical power.

Even Michael Silbert, who had made a Dragon Heart his own.

None of them had ever unleashed a Breath that powerful.

Perhaps it was the difference in their very species, combined with the weight of power amassed over a long, long time.

*So this is a dragon.*

The terrifying power felt more real than a mere hologram. I couldn’t help but shudder—and neither could anyone else in the conference room.

We even forgot to ask the obvious question: *Why* had Morgoth fired a Dragon Breath into empty space?

But the next moment—

Fwaaaash.

As I watched the sky turn pitch-black, I suddenly understood Morgoth’s true purpose.

Rrrrrumble.

With a deafening roar, countless dark clouds surged in, covering the moon and stars. Then, like ink spreading through water, they took over the skies above Moscow for thousands of kilometers.

Like a single line dividing the world.

And the place where the abyss had settled resembled another world beyond our dimension, one humanity had only ever imagined.

The source and beginning of this entire calamity.

The Demon Realm.

“……”

“……”

Would this be what it felt like if lightning struck the crown of your head?

The air had frozen. Those who understood the meaning hidden in the glitching holographic footage could only stare, eyes wide, unable to speak.

They clenched their fists until they nearly broke them, gritted their teeth, and stared with bloodshot eyes.

At the same time, they heard it.

The black dragon stood tall atop the highest spire, crying out toward the pitch-black sky.

—ᚨᚾᛊᚹᛖᚱ ᚦᛖ ᚲᚨᛚᛚ!

The roar seemed to ring out not in my ears, but inside my head.

It was more than a sound; it reached the level of will. No one here—or anywhere in the world—could understand the mysterious language.

Except me.

“……Answer the call.”

The words slipped out as a groan.

Shaaah.

The clouds, swirling like the eye of a typhoon, parted.

The deafening roar that had shaken heaven and earth faded, and so did the wind that had been raging like mad.

All noise vanished in an instant. The world, with even the air seemingly still, looked impossibly peaceful.

Until a dreadful wave of disaster poured through the gap in the clouds.

Krrrk—KWAaaaaa!

The empty space rippled.

No—it tore open.

Hundreds, thousands of Wyverns and Drakes, their yellow eyes flashing, poured toward the ground, along with countless monsters clinging to their enormous bodies and wings.

When the Liches cast their spells in unison, the giant monsters plunging down like meteors from the distant sky drifted gently to the ground like feathers. Death Knights raced through the air on ghostly horses and led their legions to fill the vast ruins.

They roared with cries that mingled joy and bloodlust.

—GRAAAAAH!

Clang! Clang!

Countless weapons swayed like a field of reeds in the wind.

Thud. Thud. Rrrrrumble!

The giant monsters, each one like a small mountain, stamped their feet. Hundreds of Liches and Death Knights went down on one knee, while ten times as many dragonkin cut through the sky with savage beats of their wings.

A display of reverence for the one being who had brought them into this world.

But the black dragon’s eyes were fixed on the camera, not on the Gate in the clouds slowly closing above, nor on the hundreds of thousands of monsters gathered beneath it.

—In the name of my soul and my name, I, Morgoth, master of the Silver Mountains and Archduke of the Demon Realm, swear to you humans:

The moment my eyes met the monster’s through the hologram, I suddenly realized something.

This video was Morgoth’s declaration of war—and his demand for humanity’s surrender.

—If you resist, I promise you the most horrific end you have ever seen. If you surrender, I promise complete peace and survival.

But—

—If you wish to survive, come to this land, reborn under my rule, and swear your loyalty.

Even so—

—But everything has its price.

There was still one thing I hadn’t predicted.

—Three days from now, I will sit upon the throne here and gladly accept the tribute you offer as a token of our eternal pact.

Just how cunning Morgoth was.

—Just two humans—a paltry price next to the lives of billions of your kind.

What his true purpose was.

—Bring them to their knees before me.

The dragon’s eyes, like swirling abysses of obsidian, flashed.

—Cheon Taemin and Jin Taekyung.

At that moment—

Ding.

A System notification pierced my ears with a chill, and a holographic window only I could see appeared, blocking my view.



* * *



Humanity was already recovering its stability faster than the various international organizations had predicted—or perhaps even faster than that.

The footage of Moscow’s destruction was enough to plunge everyone into an abyss of shock and fear. Yet a single fact announced less than a few hours later was like a ladder of salvation to them.

*He’s* back.

└ Oh my God. Please tell me this isn’t a joke.

└ It’s true. Official UN announcement. Turn on the TV right now. It’s on every channel.

└ Holy shit, that’s incredible. I thought we were all done for.

└ What the hell happened? I’m glad he’s back, but why did he only show up after things got this bad?

└ Because while you were becoming Pornhub’s best customer, he was traveling the world and saving people. He already came close to dying in the Middle East.

└ I’m genuinely worried about you, so you should delete this stupid comment before the FBI shows up in about thirty minutes, breaks down your door, and kicks your fat ass.

└ What did I do wrong? I didn’t do anything wrong.

└ He’s got a point, actually. The poor guy’s only guilty of having a lower IQ than a dolphin.

└ Yeah, don’t be too hard on him. If you happen to run into him on the street, just put a shotgun round in him.

└ You motherfukcer, you wanna die?

└ Oh, our Korean friend is here. He’s so worked up he even made a typo. That guy won’t be able to play games properly anymore. Koreans never miss the target once they’ve locked on.

└ And the Korean who gives him a headshot will probably be a kid around twelve.

└ Anyway, the important thing is that we’re alive.

└ Right. He’s back.



People quickly found hope again.

Ever since Morgoth appeared, the internet message boards had been frozen, not even managing the most ordinary joke. Now they were full of life again.

They all knew who *he* was, even without anyone saying his name.

That was what Jin Taekyung meant to humanity now.

Stronger than anyone, impossibly devoted, and able to overcome whatever hardship came his way and prove himself in the end.

Some still called him a second Cheon Taemin, but most disagreed.

Jin Taekyung had become a savior of a new age, one who needed no embellishment.

Who else could fill Cheon Taemin’s place while he lay unconscious—and make that place his own—then clean up disasters around the world and save countless lives?

That was why people felt relieved.

Jin Taekyung was back. Surely everything that had fallen into disarray would return to its proper place.

Just as he always had, he would step in and set things right.

But less than a day later, humanity received a warning from Morgoth that reached across the world, including the Pentagon. Then they understood all too well:

—ᚨᚾᛊᚹᛖᚱ ᚦᛖ ᚲᚨᛚᛚ!

How futile the hope they had briefly felt was, faced with that great army that had invaded Earth through a Gate unlike any before it.

—But everything has its price.

And how they were already listening to the monster’s sweet offer.

—Bring them to their knees before me.

How far the desire to survive could make people stoop.

—Cheon Taemin and Jin Taekyung.

Once again, the whole world was thrown into turmoil.

Some were enraged, but others kept their mouths firmly shut.

The former called for a fight to the death; the latter hid their voices to avoid criticism.

But half a day later—

Rrrrrumble!

At last, people saw footage of the monster army that had seized all of Russia and was advancing in every direction. They had no choice but to fall silent.

All thinking the same thing, though they couldn’t bring themselves to say it to anyone.

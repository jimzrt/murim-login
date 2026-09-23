# Checkpoint Review — 800–804

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

# Chapters 800–804

## Plot

More than two hundred J1 victims are found bloodless and desiccated less than two hours after death, spreading fear through the Hunter forces. The Skeleton King cannot identify The Prophet, while Magic Johnson says The Prophet’s ability is unprecedented. Jin Taekyung follows The Prophet’s message to the Rub’ al Khali, where magical power overwhelms instruments. He refuses reinforcements, relying on the forces already guarding the rear.

Jin’s roughly one-thousand-Hunter force encounters more than ten thousand monsters, beginning the battle later called the Desert Storm. The Skeleton King’s undead help the Hunters hold formation as Jin fights with White Flame and daggers. At the same time, Amir and Hamid’s fanatics kill an A-rank Hunter and advance toward their promised land, believing the time foretold by The Prophet has come. Chuck Hagel’s search party is also attacked by an unidentified non-monster enemy.

Three S-rank monsters lead the ground assault, while a Griffon leads hundreds of flying monsters. Jin assigns Magic Johnson to aerial defense and Team Leader Choi to the front, then attacks the Scorpion King before charging toward the S-rank monsters. The Prophet remains unlocated, though Jin believes he is watching the battlefield.

## Continuity

- Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.
- Jin commands roughly one thousand Hunters against a monster force exceeding ten thousand in the Rub’ al Khali. Three S-rank monsters lead the ground force; a Griffon leads hundreds of flying monsters.
- The Prophet’s message led Jin’s force to the Rub’ al Khali, identified by Team Leader Choi as the land of the “black jewel,” likely referring to its oil fields. Magical power there exceeds the capacity of their instruments.
- Jin believes The Prophet is observing the battle from a distance, but neither Jin nor the Skeleton King has located him.
- Jin attacked the Scorpion King and charged toward the S-rank monsters. Magic Johnson is assigned to protect against aerial threats; Team Leader Choi holds the front line.
- The Skeleton King’s undead can raise fallen monsters as soldiers, limited by the magical power he bestowed.
- Amir and Hamid lead desert fanatics advancing toward their promised land, believing The Prophet’s foretold time has arrived.
- Chuck Hagel’s search party was attacked by an unidentified non-monster enemy.
- More than two hundred J1 victims were found bloodless and severely desiccated less than two hours after death; the cause remains unexplained.

## Translation Decisions

- Keep **magical power** distinct from **mana**.
- Use **Desert Storm** for 사막의 폭풍.
- Render 강기 as **Force**, distinct from **Sword Force**.
- Use **Scorpion King**, **Soldier Scorpion**, **Worker Scorpion**, and **Elite Scorpion** for the System’s scorpion labels.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "Taekyung commands roughly one thousand Hunters against a monster force exceeding ten thousand in the Rub’ al Khali.",
    "Three S-rank monsters lead the ground force, and a Griffon leads hundreds of flying monsters.",
    "Taekyung believes The Prophet is observing the battlefield from a distance, but his location is unknown.",
    "Taekyung attacked the Scorpion King and then charged toward the S-rank monsters.",
    "Magic Johnson is following Taekyung’s orders to protect allies and counter aerial threats; Team Leader Choi is holding the front line.",
    "The Skeleton King’s undead can raise fallen monsters as soldiers, limited by the magical power he bestowed.",
    "Amir and Hamid lead desert fanatics advancing toward their promised land, believing the time foretold by The Prophet has arrived."
  ],
  "continuity_sources": [
    803,
    804
  ],
  "open_questions": [
    "Where is The Prophet, and when will he enter the battle?",
    "What are the identities and capabilities of the other S-rank monsters?",
    "How will the battle against the advancing ground and aerial forces unfold?"
  ],
  "safe_through": 804,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Render 강기 as Force, distinct from Sword Force."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 800

# Chapter 800

Hunters were always close to death.

It didn’t matter whether they were S-rank Hunters known to everyone in the world or F-rank Hunters who were as common as stones in the street. No one was exempt.

The misfortune of death came equally to everyone, and Hunters were more accustomed to that fact than anyone.

But…

“Holy shit.”

The low curse spoke for everyone.

Reflected in dozens of pairs of eyes, trembling slightly in that moment, were more than two hundred corpses, shriveled nearly to nothing.

“Damn it. Has anyone here ever seen anything this insane, even once?”

Everyone fell silent at the Team Leader’s question. No—that wasn’t quite right. They’d even forgotten how to answer.

*What the hell is this?*

They might have been assigned to recover the dead in the rear, but they were Hunters all the same. They’d had more than their share of life-or-death experiences, and they’d seen enough corpses to last a lifetime.

Especially after the series of events that had unfolded one after another over the past few months. How many deaths had they witnessed?

And yet, even they couldn’t help feeling a chill run down their spines at that moment.

“……You said they’d been dead for less than two hours, didn’t you?”

The Team Leader bit his lip at someone’s question, which broke the long silence.

“It’s hard to believe, but yes. That’s exactly what I was told.”

“Then it has to be one of two things. Either you’ve gone deaf, Team Leader, or the person who told you is insane.”

“That could be. But neither is true.”

“Maybe not. But looking at these bodies, I’d say they’ve been dead for at least a couple of centuries. What kind of lunatic told you they’d been dead for less than two hours?”

“What, you planning to go argue with them?”

“We ought to check whether it’s true. And if they were talking nonsense, I’ll punch them right in the face.”

“Fine.”

The Team Leader had already taken out a cigarette and put it between his lips. He continued calmly,

“If you really want to do that, go to the command tent right now. The moment you see Magic Johnson, punch him in the face. I’ll take care of your bodies and deliver them to your families, so don’t worry about what happens afterward.”

“What?”

“Are you still here? You said you were going to find that lunatic and punch him.”

“……”

The Hunters were at a loss for words.

It wasn’t so much that the lunatic they’d just been cursing was Magic Johnson. The greater shock came from the realization that the order itself wasn’t wrong.

*So it’s all true?*

*Damn it. What’s going on?*

Becoming a veteran Hunter meant getting used to the smell of blood instead of the smell of pancakes cooking. It meant growing accustomed to sights so gruesome that, even if you quit, you could switch careers and become an undertaker.

Limbs torn off, torsos ripped open, heads crushed…

They’d seen it all more times than they could count. Most of the corpses they’d encountered belonged to monsters, but plenty had belonged to comrades they’d shared meals with, too.

Even so, they’d never seen corpses like these.

More than two hundred bodies, dried out without a single drop of blood.

If they hadn’t known the circumstances, every last one of them would have thought they’d been sent to excavate ruins.

These weren’t just corpses. They looked like mummies that had been buried deep underground for centuries.

*Damn it. Have we been bewitched?*

*They’ve been like this for less than two hours? How is that possible?*

It wasn’t gruesome. It was simply more bizarre than that.

Every moment sent goose bumps crawling over their bodies. They couldn’t take even one step toward those corpses, with not a trace of life left in them.

At the same time, one question filled everyone’s mind.

*What did this to them?*

Not *who*. *What*.

As everyone swallowed hard at the thought of an unknown enemy they couldn’t even begin to predict, the Team Leader took a deep drag on his cigarette and shouted,

“Fuck! How long are you going to stand there staring? Stop wasting time thinking about it and get moving! Now!”

The Hunters jolted as if they’d just woken up, then finally began to move, sluggishly.

Watching his subordinates force their reluctant feet toward the corpses, the Team Leader suddenly realized he still hadn’t lit his cigarette.

*……Damn it.*

He cursed to himself and threw the cigarette from his mouth onto the ground.

But his hand, now brushing over his parched lips, was trembling slightly.

* * *

“Rumors are spreading.”

Team Leader Choi spoke, his face grave.

“Everyone’s afraid. Word about the fallen Hunters’ bodies is going around under the table.”

“……”

“We need to do something before it gets any worse. If this continues…”

His voice trailed off naturally. But what he meant was already clear from what he’d said.

I finished the sentence Team Leader Choi couldn’t.

*We’ll fall apart from the inside before we even get moving.*

This wasn’t about another traitor like Michael Silbert emerging.

This was about the most fundamental force that kept an army moving: morale.

*Fear is eating away at them—and fast.*

There were some things in this world that you couldn’t stop, no matter how hard you tried.

Like this.

“There were too many witnesses. We ordered them not to talk, but it seems there was a limit to how much we could contain the rumors.”

Even an order to keep quiet had its limits.

The J1 team Yamamoto Genji belonged to had been wiped out in a bizarre fashion, and there were hundreds of people who’d reached the scene before I did.

Even the authority my name carried wasn’t enough to lock every one of their mouths.

People’s emotions.

Negative emotions like fear were almost impossible to control.

But the bigger problem was that the rumors frightening even veteran Hunters who’d been through hell and back weren’t baseless nonsense.

“And although they haven’t gained much traction yet…”

Team Leader Choi hesitated for a moment, then continued with a sigh.

“Some people are adding things to the story and spreading absurd rumors.”

“What kind of rumors?”

“That The Prophet really is God’s chosen representative, or some transcendent being like the Demon King Asmodeus…”

Bang!

“Bullshit!”

Magic Johnson shot to his feet with a shout and glared viciously.

“Tell me, Choi. Who the hell is spreading this deranged crap?”

“Like I said, it hasn’t gained much traction, and it’s only one of the rumors going around, so we can’t identify anyone in particular. The problem is that a tiny number of people truly believe it.”

“What kind of world is this, that people are going around believing in that kind of superstition… Damn it.”

Magic Johnson started to say something, then shut his mouth with a rough curse.

The hulking Grand Mage had clearly just remembered something he’d momentarily forgotten.

That Hunters were more obsessed with superstition than anyone else in the world.

In a way, it was only natural. Whatever reason they had for becoming Hunters, every human being wanted to survive.

The vast wealth an ordinary person could only dream of, the honor of being humanity’s sword and shield.

But the value Hunters put above all else was survival.

Even sports players followed all kinds of strange routines that no one else could understand, clinging to simple, childish superstitions. What about Hunters, who fought with their lives on the line?

If athletes believed in superstitions to protect their careers, Hunters couldn’t help taking them seriously when their very lives were at stake.

Especially when they faced an unknown phenomenon that no one had ever encountered before.

“Calling him a Demon King, of all things. They’re all idiots.”

I looked at the Skeleton King, who muttered in disbelief.

He’d already gotten a similar look from me several times, so he immediately understood what it meant and furrowed his brow.

“I told you. I don’t know either.”

That wasn’t the answer I’d wanted.

I suppressed my disappointment and spoke.

“Right. That’s why I gave you time to think.”

“……Damn it. I’m genuinely curious, too. What the hell is that guy called The Prophet?”

The Skeleton King let out a deep sigh and continued.

“But what do you expect me to do if I don’t know? I first regained consciousness in that place you call a Gate. Everything before that is blurry. No, I can’t even call it a memory.”

“Not even fragments?”

“A dark, ominous place. That’s all I can recall. That must be the Demon Realm, I suppose. Another world beyond the Gates. Isn’t that right?”

It was a question no one could answer. Not me, not Magic Johnson—not anyone in humanity.

Ever since the Demon King Asmodeus descended into this world, humanity had known that a land of death existed beyond the dimensions—but the place itself remained shrouded in mystery.

No one had ever learned what existed there, or what calamities lurked within.

And that was true even of the Skeleton King, who had come through a Gate from the Demon Realm.

“What I know is only a tiny fraction. Do you know what surprised me most after I set foot in this world?”

I answered without thinking.

“Clubs?”

“……What have you thought of me all this time?”

“Illegal immigrant. Dumbass. Eunuch.”

The Skeleton King gave me a look that had gone completely cold, then sighed deeply.

“Damn it. Sure, that was incredible too. But what amazed me most was the monster encyclopedia your humans made.”

“What?”

“That was when I first realized there were so many different kinds of monsters. Until then, what I knew about monsters amounted to a scrap of flesh on a pile of bones.”

“……!”

“But even you humans, who’ve spent so long researching monsters, haven’t uncovered everything. Isn’t that right?”

Magic Johnson answered with a grim expression.

“That’s true. There were limits to what we could learn by studying monsters.”

It was the kind of story that appeared only in history textbooks now.

Even after the Great Cataclysm, humanity wanted more data. In the period immediately after the war ended, Hunters weren’t hunting monsters so much as capturing them.

Then came every kind of experiment imaginable, including dissections.

But that wasn’t enough. Not every monster in the world was a low-level one like a goblin.

“The losses mounted the more we tried to capture high-level monsters. A large number of S-rank Hunters, myself included, joined the effort, but it didn’t always succeed.”

“Which means…”

“Among the highest-level monsters we most wanted to target, some Named monsters like Leviathan and the Arch Lich had disappeared completely. And there were monsters like dragons, with very few individuals. We weren’t able to learn much about those.”

I murmured,

“Then The Prophet could be one of them.”

“Right. If he really is a monster, as we suspect… he must be one of the highest-level Named monsters we failed to identify.”

Magic Johnson continued in a subdued voice.

“And I can say for certain that, from the Great Cataclysm up to now, I’ve never seen anyone with this kind of ability.”

He was an utterly unknown being.

We knew neither his identity nor his power.

And fighting an enemy whose nature you hadn’t uncovered was the stupidest, craziest thing you could do.

Of course, I’d done that crazy thing countless times.

“Then there’s only one option left.”

At my offhand remark, I saw everyone’s expression grow heavy. Before anyone could try to stop me, I continued.

“We set out immediately. I have to see that bastard’s face.”

One message.

I would use those words The Prophet had sent me through Yamamoto Genji as a signpost and track the bastard down.

Before an irreversible catastrophe struck.

Even if… it was a trap.
## Chapter artifact 801

# Chapter 801

“We’re leaving soon. Get ready.”

At that one remark, tossed out when I came back without warning, Yamamoto Genji surprisingly nodded obediently.

“Understood.”

For a guy who’d been going on about Chōsenjin when he first woke up, he was being about as polite as possible.

If Heo Jun had witnessed this astonishing change, he might have written this on the first line of the *Donguibogam*:

> A beating is the best medicine.

As a rule, you treat wounds on the body with potions and rotten minds with your fists.

Yamamoto Genji sprang out of bed in a hurry and snapped to attention like a trainee.

“I’m ready.”

“Already?”

“Yes, sir.”

“You planning to fight in that?”

“Huh?”

Yamamoto Genji blinked. Judging by that utterly innocent expression, he clearly didn’t understand what was going on. Or maybe he hadn’t heard me properly at all.

So I kindly repeated myself.

“You planning to fight in your hospital gown?”

“……!”

A brief silence.

At last, Yamamoto Genji understood what I meant by *leaving* and asked in a trembling voice,

“W-we’re going to the battlefield?”

“Where did you think we were going?”

“I assumed that, since I’m still a patient, I’d naturally be sent back to the main camp…”

“Sent back?”

“Y-yes, sir.”

“Hmm. Right. You’re still a patient, aren’t you? A patient.”

Good grief. I’d forgotten something important.

Muttering under my breath, I kicked open the firmly shut door.

“Hey! Anyone out there?”

Before the words had even left my mouth, a healer from the medical unit came running over.

“Yes, sir.”

“Um, what was it? The transport vehicle going back to the main camp hasn’t left yet, right?”

“That’s right. It’s still waiting.”

“Good. Contact the team leader right away and tell him to load one more body. I’ll take care of the cleanup, so all they have to do is come pick him up.”

“I’ll pass that along.”

“……Wait a second.”

Yamamoto Genji, who’d been listening to our conversation, asked with a foreboding look on his face,

“One more body? Cleanup? What does that mean?”

“It’s nothing. Don’t worry about it.”

“It sounds like a pretty big deal. Hey, you. Put down the phone. Who are you calling?”

The healer replied bluntly,

“I’m contacting Team Leader Jones, as the boss instructed.”

“Who’s Team Leader Jones?”

“He’s in charge of recovering the dead. He transports the fallen back to the main camp.”

“……!”

Yamamoto Genji looked back and forth between me and the healer, then spoke with a resolute expression.

“On the honor of a samurai, I’ll give my life and fight.”

“What honor? I looked you up online. Your nickname is ‘Swift No-Show.’”

“……”

“Quit talking bullshit and gear up. Get out here.”

“Yes, sir. But, by any chance…”

“What?”

“I’m still not feeling well, so could you really send me to the rear…”

*Whack!*

“Ugh!”

Even at a time like this, he was still thinking about running away. A bastard like this needed a little beating.

I let out a deep sigh and watched him stagger back to his feet.

I wanted nothing more than to beat the hell out of him, but the fact that I needed even a piece of shit like him made me feel even worse.

“Hey.”

“Y-yes? What is it?”

“I’m not going to hit you, so don’t freak out. I just want to make sure one more time.”

My voice low, I continued,

“What you said he told you back then. Are you sure?”

Before Yamamoto Genji could open his mouth, the same words I’d heard several times already replayed in my ears.

> “Rub’ al Khali. Come find me in the land where the black jewel sleeps, before it’s too late.”

The trailing hem of The Prophet’s long robe seemed close enough to reach out and grab.

* * *

The Arabian Desert covers most of the Middle East, stretching from Yemen through Oman and the Persian Gulf, as far as Jordan and Iraq.

An immense expanse, more than 2.3 million square kilometers.

Korea’s official area, as submitted to the UN, was just over 200,000 square kilometers. Compared to that, this place was simply insane.

*No wonder the estimated search time was so long. We were planning to comb an area this huge from end to end.*

But we didn’t have many options.

With mana levels rising by the day and concentrations growing denser, even the most advanced equipment couldn’t function properly. The only way to cover an area this large was to send a hundred thousand Hunters out on foot.

There was one fact that was hard to decide whether it was fortunate or unfortunate, though…

The Prophet, who’d been hiding somewhere in this vast desert, had singled out a location for us.

The Rub’ al Khali Desert.

If the Arabian Desert was the broad term for the desert regions covering the entire Middle East, then the Rub’ al Khali, in its center, was a vast desert stretching across the southern Arabian Peninsula.

It was the second-largest desert in the world, after the Sahara in Africa. Still, it wasn’t difficult to guess the specific area The Prophet had meant.

At least, not for Team Leader Choi.

“The Empty Quarter.”

“What’s that?”

“Rub’ al Khali means ‘Empty Quarter’ in Arabic. A land where no one can live. A land of nothing but blazing sunlight and sand. That must be why it was given such a desolate name.”

“Then the black jewel must mean…”

“There are oil fields there. They were supposedly once the largest in the world… Judging from The Prophet’s message, that seems like the likeliest place now.”

The hard part was searching, not getting there. Once we’d chosen our destination, our advance moved at an astonishing speed.

The thousand Hunters selected for this expedition were among the very best of those deployed to the Middle East. We crossed the Arabian Desert by the shortest route and arrived at the Rub’ al Khali.

And we immediately understood why the people of the ancient Middle East had called this place the Empty Quarter.

An endless desert and wilderness spread out like a vast ocean, dotted with small villages as sparse as reefs.

With its machinery and abandoned industrial complexes, the place looked so desolate it was hard to believe the world’s largest oil field had once been there.

It was bleak enough to make even the Skeleton King blink in confusion.

“What? This is a place where humans live? Not a Gate?”

There was a reason Team Leader Choi had used the words *once was*.

This land had already been abandoned twice.

Once, long ago, when the natives named it the Rub’ al Khali. And once again, amid the calamity known as the Great Cataclysm.

There was always a reason a place got abandoned.

“Spectacular.”

I wish those words had come from Magic Johnson, who’d come with us. Unfortunately, the voice belonged to the Skeleton King—and I felt the same way he did.

Maybe we all did.

*The concentration of magical power… It’s too dense.*

The air had started feeling heavy at some point, and it wasn’t just because of the sunlight pouring down on us.

*Clunk. Psssh.*

An engine abruptly died. As the vehicles carrying a thousand soldiers all came to a halt, Magic Johnson murmured,

“It’s starting.”

There was no way this was a simple mechanical failure.

Yamamoto Genji, who’d already experienced something similar, had gone deathly pale.

“He’s here. He’s here. He’s here…”

The Skeleton King watched him mutter without pause, then asked me,

“Can I kill that human?”

“No. Unfortunately, you can’t.”

“Why not? Didn’t we bring him along to put his body to use? If we have to keep looking at him like that, turning him into an undead might be better.”

“Oh.”

Was this bastard a genius?

I barely stopped myself from nodding at his surprisingly logical argument. Then I gave Yamamoto Genji a hard kick and got out of the vehicle.

*What do you mean, he’s here already?*

We were still a considerable distance from the oil fields The Prophet had hinted at. And other than the rising concentration of magical power, I hadn’t sensed anything unusual.

This was only a sign.

An ominous but certain sign that something we hadn’t encountered yet was somewhere in this vast desert.

Soon, a report from the measurement specialist, who was checking the magical-power distribution at regular intervals, turned my suspicion into certainty.

“We can’t get a reading. Our equipment can’t determine an accurate value.”

Even the measuring device, which had several precious A-rank Magic Gems installed in it, couldn’t do it.

I licked my dry lips and muttered,

“He told us to come find him. Guess it wasn’t just some bullshit he threw out there.”

Team Leader Choi stepped quietly up beside me and spoke.

“Should we pull our forces back and request reinforcements while we still can?”

It was a cautious suggestion, very much like Team Leader Choi. But I shook my head without hesitation.

“No. We keep moving.”

“We don’t know what kind of trap might be waiting for us.”

“Of course that’s a real possibility. You know what that bastard Prophet is like.”

“Then why…”

“Even if there’s a trap, we have to break through it. We don’t have time. And…”

Lowering my voice, I continued,

“If The Prophet’s real goal is to lure us out, then all the more reason not to request reinforcements.”

We still didn’t know the limits of The Prophet’s abilities or personal fighting strength.

But if we called an S-rank Hunter—a key part of our strength—here under these circumstances, the forces left behind would be in danger.

In this desert, The Prophet was practically a pope commanding countless fanatics.

*It’d be a problem if we brought in reinforcements only to leave the rear wide open to a raid.*

That didn’t mean I planned to fight recklessly, of course.

Under normal circumstances, I would’ve gone alone. The reason I’d brought a thousand soldiers was precisely this.

No matter how strong I was, I wasn’t invincible. And nothing was as dangerous as an enemy whose abilities were unknown.

In that sense, the force we’d assembled was neither insufficient nor excessive.

Even without me, we had two dependable powerhouses in Magic Johnson and the Skeleton King. Add the cowardly Yamamoto Genji and Team Leader Choi, and I was sure we could smash our way through whatever came.

*If we bring in more forces, he might run.*

Chuck Hagel, Faye Chen, Prince Felix, and several other S-rank Hunters were guarding the encirclement with a considerable force to our rear.

If we added or removed even a little from either side, the balance of power would shift—and our chance to eliminate The Prophet would slip that much farther away.

“No beast ever attacks an opponent that looks stronger than it is. Especially not a fox like The Prophet. Right, Jin?”

“That’s right.”

I nodded at Magic Johnson and looked at the heat haze rising over the distant desert.

“Still, that’s a relief. Looks like that quick-witted fox hasn’t gotten scared and run off.”

“What do you mean—!”

His face went rigid in an instant.

Realizing what I meant, Magic Johnson hurriedly swallowed the rest of his words and shouted, pouring his mighty mana into his voice.

“Prepare for battle!”

Right.

They were coming.
## Chapter artifact 802

# Chapter 802

*Slide.*

The sand on the hill slowly slipped downward. It was a sweltering day without a breath of wind. Beneath the blazing sun, the shadows of flying beasts fell over everyone.

*Kreeeaaak!*

A dozen or so vultures glided through the sky, letting out cries like screams.

Their enormous wings, spanning several meters, were nothing but bare white bones. And the eyes gazing down from far above weren’t made of flesh and blood—they glowed a vivid blue.

The kind of light that might shine in the eyes of something returned from the edge of death.

A being that hovered somewhere between life and death.

“Undead…”

A voice like a sigh slipped from someone’s lips.

But not one of the many people watching the vultures fly over their heads and on toward the horizon looked afraid.

They already knew.

Those undead monsters weren’t their enemies.

No—more precisely, their master was most definitely an ally.

And at least one of them thought of him as more than an ally. He was a friend.

“Hey.”

“What? Don’t talk to me. I’m concentrating.”

“How’s it going?”

“I said don’t talk to me. I’m sharing my vision.”

“Still? You’re damn slow.”

“Fuck. I’m not doing this anymore.”

“Sorry.”

“Then shut your mouth, you lunatic. You think this is some cheap Familiar like the ones humans like you use?”

The human and monster traded words as casually as old friends, then fixed their gazes on the heat haze shimmering over the desert.

They could feel the vibrations slowly crumbling the sand dunes.

“Anything yet?”

“No, actually, I finished a little while ago.”

“What? Why didn’t you say so?”

“To build the suspense.”

“You’re a nutcase.”

“I’m kidding. I didn’t say anything because I wasn’t sure how to tell you.”

“…There are that many?”

“Yeah.”

“How many?”

“At least ten thousand. After that, there were too many, so I gave up counting.”

At the Skeleton King’s answer, Jin Taekyung fell silent.

Ten thousand.

That was an enormous army.

And that was only what they’d confirmed so far. If they somehow counted the exact number, it might be far beyond their estimate.

“Fuck, they’re really going all in.”

“They must have had a good reason for drawing us all the way out here.”

“What about him?”

The Skeleton King knew who Jin meant by *him*, and shook his head.

“I still don’t know. From above, there are about three that look like serious threats, but whether one of them is The Prophet… Hmm.”

The Skeleton King let out a low groan. His expression stiffened as he continued.

“There was one in the air, too.”

“Are they all S-rank?”

“Probably. My servants couldn’t even fight back before they were defeated.”

Three on the ground. One in the air.

The news that four S-rank monsters had led an army of tens of thousands right to their doorstep shook the nearly one thousand Hunters. No matter how carefully selected and battle-hardened they were, they couldn’t simply cast aside their fear of death.

*Thud. Rumble, rumble.*

The vibrations grew more and more violent. As the sand shifted beneath their feet, the Hunters’ eyes trembled.

They could already picture the countless monsters about to surge in like a wave.

They could picture their comrades—or themselves—spattered with blood and dying amid the monsters’ roars and the fierce battle.

And it was right then that a calm voice reached everyone’s ears.

“So, want to retreat now?”

One by one, the people who’d been looking down raised their heads. Jin Taekyung stood on the hill, gazing at them with eyes sunk deep and steady.

“No, I suppose we should call it running away, not retreating. Right?”

“……!”

“Honestly, whether you call it a strategic retreat or running away, I can’t blame you. Everyone wants to survive. We all have reasons to keep living, even if we have to run like hell to do it.”

That was true of everyone in the world.

They had family bound to them by blood, and friends who felt like family even without the blood. And even if they had neither, they still had reasons to keep living.

But…

“I don’t know where it came from, but there’s a saying: There’s no paradise at the end of the road when you run away.”

It was strange.

The sunlight pouring down overhead was hot enough to set them on fire, yet the moment they heard Jin Taekyung’s voice, they felt as if someone had doused them in cold water.

He was right.

There was no paradise at the end of the road when you ran away. They lived in a time like that.

“Run away, and run away, and run away again… Then one day, after fighting tooth and nail to survive, you look around. Will there still be anything left for you to protect?”

It had been more than thirty years.

Humanity had rebuilt cities even larger and more splendid on the ruins left behind by the Great Cataclysm. The traces of that disaster remained only in records and scars.

Those who survived the war, or were born after peace arrived, didn’t know what war was like.

But Jin Taekyung was different.

“Once you start backing down, it’s over.”

Combat and war were different. So were Gates and reality.

In the Gates they’d experienced until now, they could simply retreat to avoid a fight. But the place they were standing in at that very moment was the world where they’d been born and raised.

A world with something they had to protect.

A world they had to protect, no matter what.

Jin Taekyung knew that. From the day he survived alone, leaving behind someone who’d been like an older brother, to now, when he’d come to know another world.

“If there’s something you want to protect, fight for it with your life on the line. That’s why you’re all here, isn’t it?”

Everyone wondered, but no one knew.

Why the cursed monsters had invaded this world, or how humans had come to possess such incredible power.

But everyone had some vague idea.

This power that had come to them one day like a stroke of luck had been given to them so they could protect this world from monsters.

“And for that one reason…”

*Whoosh.*

Sand whipped around Jin Taekyung. A hot wind blew in from somewhere and swept over the people.

It thawed their hands and feet, frozen like ice even beneath the sweltering sun, and made the red blood in their veins boil—unlike the monsters now appearing in the distance beside a gigantic sandstorm.

“That’s why people—why this world—calls us Hunters.”

*Fwoosh!*

An immensely powerful wave of energy jolted everyone’s senses awake. As Jin Taekyung slowly turned around, heat haze rose around him.

The heat was so intense that it made the space around him seem to warp.

The spearhead gleaming in the sunlight blazed like a blue-white sun.

“Get into formation.”

*Clang, clang, clang!*

Countless weapons were drawn at once, as if on cue.

When Magic Johnson raised his staff, dozens of transport vehicles, each weighing several tons, blocked the way ahead.

Behind them, nearly a hundred tanks drove tower shields larger than their own bodies deep into the sand.

*Boom. Rumble!*

A steel wall took shape with a series of heavy thuds.

And then…

*Rumble…*

Raising a vast cloud of sand, a wave of monsters rushed fiercely across the boundless desert.

But Jin Taekyung’s words as he watched them were so calm and matter-of-fact, they surprised everyone.

“Fuck. Hang in there, everyone. We’re going to bust our fucking asses killing all those bastards.”

Someone burst out laughing.

A Hunter who’d been staring at the comrade beside him as if he’d gone insane let out a snort, and soon everyone’s shoulders were shaking.

Kill them all? All those monsters?

Normally, they’d have thought it was absurd nonsense.

If anyone else had said it, no matter how great a Hunter they were, they’d have cursed them under their breath.

But that startlingly young Asian man was Jin Taekyung, the new Alliance Leader of the World Hunter Federation.

A hero who had proven himself.

The only one writing another legend after Cheon Taemin.

They couldn’t help believing in him.

Jin Taekyung had always fought at the very front, harder than anyone else.

That alone was reason enough to fight.

*Boom. Rumble, rumble!*

*Graaaar!*

Even as the thunderous rumbling and roars grew loud enough to make their eardrums throb, the Hunters couldn’t keep from laughing.

They watched Jin Taekyung stand tall on the sand dune like a mountain, then swing his spear.

*Crunch!*

Blood erupted like a fountain and evaporated before it could touch the ground. Torn bodies and entrails scattered in every direction.

The opening moment of the great battle that would later be called the Desert Storm.

* * *

Chuck Hagel stared silently at the cigar in his hand.

The cigar he’d taken—or, rather, acquired—from the French President not long ago was still slowly burning.

He’d heard later that it had been a direct gift from Michael Silbert. Given its provenance, it was obviously worth a fortune.

Cuban cigars made before the Great Cataclysm were impossible to find now, no matter how much money you had.

Why?

Simple. Cuba had been destroyed.

The monster wave that began in the center of Cuba’s capital had grown beyond control. It ended only after sinking three island nations in the Cayman Islands deep beneath the sea.

Perhaps that was when it started.

When a certain middle-aged man, who’d never even touched tobacco, began smoking cigars out of habit.

His mother had been in Cuba.

*Crackle.*

Ash that had been burning for a long time dropped with a soft *tap*.

After watching it in silence for a long while, Chuck Hagel abruptly spoke.

“Any request for backup?”

An aide, who’d just waved the thick cigar smoke away, answered.

“Not yet.”

“Goddamn it.”

“You don’t need to worry so much, boss.”

“Worry? About that punk?”

*He’s too strong to call a punk. And he’s your superior, too.*

The aide barely swallowed the words that had almost slipped out and clicked his tongue.

“We’re fully prepared and standing by. We’re responsible for the rear of the Rub’ al Khali Desert.”

“Damn it. That’s all well and good, but that goddamn satellite surveillance still doesn’t work. Why are the drones down? Did some defense contractor take a kickback?”

“Come on, boss. You know why. The concentration of magical power is too high.”

“I don’t know about any of that. If anything happens to the others with that punk who ran off on his own… you know the bastards who made those fucking paper airplanes will die by my hand.”

“……”

The aide was profoundly grateful that there was no one from a defense contractor around at that moment.

He was also grateful that his short-tempered superior was still guarding the main force.

Unfortunately, the relief he felt didn’t last long.

*Beep. Beep-beep.*

“…Huh?”

A sudden emergency alarm rang out, and red warning lights flashed on. Urgent shouts erupted around the command center.

“Identify the sender and the coordinates!”

“Damn it! Hurry!”

A moment later, Chuck Hagel saw the aide’s face stiffen as he read the report.

“What is it?”

“…We’re under attack. Part of the search party outside has been hit.”

“What?”

“And…”

The aide paused for breath, then let it out.

“The enemy isn’t a monster.”
## Chapter artifact 803

# Chapter 803

Human beings possess possibilities close to infinite.

With their capacity for thought surpassing that of any other living thing on Earth, they built systems of their own and developed civilization.

From the utterly primitive prehistoric age to the present.

In particular, the history and culture humans had built over the past several thousand years were truly dazzling.

Progress, progress, and more progress.

Humans kept discovering new things, and moved forward with every one of them.

Until they filled battlefields where spears and swords once clashed with the sound of gunfire, and car horns rang through streets ablaze with neon signs instead of the whinnying of horses.

Until they crossed five seas and six continents, and finally ventured into space.

*“Houston, Tranquility Base here. The Eagle has landed.”*

On the day that grand plan, named after an ancient sun god, succeeded.

What had the god, watching from somewhere, thought at that historic moment when a human first set foot on the moon and called it “one small step, one giant leap for mankind”?

No one could know the will of God, but an old man with the rather long name of Abdullah bin Abdulaziz Ali could be certain.

God must have been enraged.

Otherwise, He wouldn’t have unleashed a great flood called the Great Cataclysm.

Sending the great Prophet down to this land and commanding him to punish them surely meant that he was to punish humanity’s arrogance on God’s behalf.

“Do you not think so as well, you sinful infidel?”

“……!”

At the old man’s calm voice, the middle-aged man trembled.

Drenched in crimson blood, he stood amid his many subordinates, who had been alive and breathing only moments ago and now lay strewn across the ground.

The middle-aged man had nothing left.

Nothing but the sword in his hand and the mana still boiling through his body, his fighting spirit undiminished.

“Repent through death. Like those who went before you.”

“Go… fuck yourself!”

With a scream, the middle-aged man drew on every ounce of his strength and charged at the old fanatic.

*Whoooosh!*

Perhaps the last strike of his life.

The sword flew faster than ever before, filled with blinding aura, and—

*Shhk!*

A flash came out of nowhere, cleaving both the aura-wreathed sword and its wielder in two.

*Splatter!*

Blood gushed like a fountain.

As the headless corpse crumpled to the ground, something glinting fell at the old man’s feet.

A necklace. It was a necklace.

The old man stared at the crucifix necklace half-buried in the hot sand, then suddenly spoke.

“Any survivors?”

“None. That infidel was the last.”

The young man who had cut down the middle-aged A-rank Hunter as casually as breathing continued,

“Amir, there are more infidels not far from here. If you let me go…”

“Their main force will have heard from them on the radio this time. We’ve dealt with them easily so far, but that ends now.”

“No matter how strong the infidels’ forces are, we can defeat them!”

“Hamid, son of Hassan, you’re right. But have you forgotten what the Prophet said?”

At the old man’s piercing gaze, the young man named Hamid flinched without meaning to. Then, realizing the meaning of his words a moment later, his eyes widened.

“If you mean what the Prophet said, then could it be…?”

“Yes. The time has finally come. The time promised by the Prophet, by almighty Allah, has arrived.”

“……!”

Amazement turned to joy. Joy to fervor.

Watching the young man’s expression change by the second, the old man smiled. Then he looked down at the warriors of God surrounding them and muttered,

“Inshallah. The Prophet will lead us to the promised land!”

“Inshallah!”

“Allah hu akbar!”

With their enormous voices rising as one, the many fanatics who had lain dormant deep in the desert for decades began their advance.

Toward the promised land they had awaited for so long.

Toward that place overflowing with God’s grace.

*Rumble, rumble, rumble!*

A vast cloud of sand swept across the desert.

* * *

If this world were a chessboard, what would my role be?

A pawn that can only move forward?

A knight that can leap farther than a pawn?

A bishop that traverses the board diagonally?

Maybe a rook that moves in straight lines, a queen with the combined power of a bishop and a rook, or, ironically, the king—both the most important piece and weaker than the queen.

Honestly, I didn’t know.

Even now, as the Alliance Leader of the World Hunter Federation, even with everyone in the world knowing who I was, I still didn’t know exactly where I stood.

Or how far I could go on this chessboard.

But there was one thing I could say for sure.

If that chessboard wasn’t called the world, but the battlefield, then I could dominate it.

I could keep pushing forward like a pawn, then become a knight and leap over the enemy’s heads; I could range across the board in every direction like a bishop, rook, or queen, and swallow everything whole.

Just like right now.

*Baaang!*

Flesh and bone burst apart before the spearhead even touched them. A Troll’s body, its upper half blown away, fell like a rotten log, and someone shouted behind me.

“Damn it! How many times do I have to tell you that if you kill them like that, they’re no use as undead!”

Instead of answering, I twisted my body.

*Whoom. Boom!*

Three flails flying in from different directions tangled together.

—Kwo?

The ogres blinked stupidly, realizing what had happened a beat too late.

But White Flame’s spearhead had already swept past their necks.

*Shhk!*

Three heads flew into the air, severed from their massive bodies.

I sprang off the corpse of an ogre whose life had already left it, then plunged down toward the monsters packed tightly around me.

Fire Dragon Divine Spear, Form Two.

Heavenly Strike.

*Krrrunch!*

Blood sprayed and flesh split.

Ding. Ding, ding.

As System alerts reached my ears without pause, I plunged through the thick cloud of dust.

*Open Inventory.*

Stowed away, then summoned in the same instant.

*Pop.*

White Flame vanished from my hand like an illusion, replaced by two short daggers that firmly filled my empty palms.

In a fight at this close range, they were faster and more efficient than any divine weapon.

Among those who had used weapons like these, there was someone I’d watched up close who had earned the epithet Slaughter Saint with a single dagger.

*I watched him from right beside him.*

For one brief moment, I steadied my breathing.

I calmed my internal energy, pounding as if it would burst, and kept my toes light and my shoulders loose.

Remembering the Slaughter Saint’s advice, I imitated the movements I’d seen him perform right in front of me dozens of times.

Then I took a step.

*Ghost Illusory Slaughter Step.*

*Swish.*

The wind, which had always slammed into me with force, scattered softly.

It felt as if I were floating through the air in zero gravity.

Of course, I couldn’t claim I’d perfectly copied the Slaughter Saint’s personal martial art just by doing this much. But for dealing with these bastards right now, this much was enough.

*Shhk, shhk, shhk!*

Only after flesh and bone had been cut through did the sound of slicing reach my ears.

It wasn’t that the sound was slow.

I was simply that fast—the daggers in my hands were moving fast enough to leave the sound behind.

*Thud, thud, thud!*

Seeping in like mist, then stabbing and slashing like flashes of light, the two daggers sent dozens of monsters crashing down in sprays of blood.

No—in truth, they fell and rose again at the very same moment.

—In the king’s name, I command you: answer the call.

*Whoooooosh.*

A voice that seemed to reverberate inside my head rather than my ears rang out, and a chilling cold swept across the battlefield.

It raised the monsters that had fallen moments ago and the ones falling even now.

—Krr. Grrrk.

Slow, rasping cries.

An eerie light glimmered deep within their eyes.

The undead army, reborn as new beings at the edge of death, charged without a moment’s hesitation at the monsters surging in from every direction, obeying their king’s command.

—Kraaaaaa!

—Grr. Uh. Uh. Uh!

*Thud. Kraaang!*

The roars of monsters that were alike yet different tangled together, and weapons swung with force slammed into one another’s bodies.

But unlike the monsters still alive and therefore capable of feeling pain, the undead were creatures that had forgotten pain along with death.

—Graaah.

*Crunch! Splatter!*

Outnumbered? It didn’t matter.

Even with their limbs cut off by weapons flying in from all directions, even with their chests pierced through, they kept moving to the very end.

The Skeleton King had given them only one goal.

Before the magical power he had bestowed upon them ran out, before they met their second death, they had to create another soldier.

*Crack!*

—Kyaaaah!

A monster with its throat torn out screamed.

The undead body, already missing an arm and a leg, was ripped to shreds by the enraged monsters, but that didn’t matter.

Thanks to that, I—

No, we—had bought a little more time.

“Fire!”

“Fire Wall!”

“Lightning Spear!”

*Fwoooosh.*

Countless bolts of lightning and flames streaked through the air.

Behind the enormous transport vehicle blocking the way like a barricade, the monsters packed in so tightly there wasn’t a gap—like the first day of an E-Mart Black Friday sale—had no choice but to take the sudden barrage of attacks head-on.

*Crackle. KRAAAASH!*

—Kraaaaaa!

—Kgh! Grrrk!

Screams filled the air in every direction.

Lightning seared scales and flesh, while flames seeped through the gaps and burned bones and organs.

Many of the hundreds of monsters thrashing in agony unlike anything they had ever felt even swung their weapons at their own allies.

—Kwoooooo!

Monsters driven into each other by the ferocity of pure instinct.

But I didn’t let my guard down for even a moment.

“Hold formation! Don’t take a single step from where you are!”

At my command, carried by internal energy, the Hunters who had been advancing in the heat of battle, caught up in the excitement of gaining the upper hand, stopped in their tracks.

Battle was momentum. It was flow.

But there was a time to ride that momentum.

Against that enormous force of more than ten thousand, killing just a thousand monsters wouldn’t win this battle in an instant.

Slowly. Carefully.

We had to win while minimizing our losses.

Besides…

*I still can’t see him.*

The bastard who still hadn’t shown himself.

The Prophet.

And the S-rank monsters waiting for their moment amid that sea of monsters—or somewhere in the sky above.

Until we took them down, neither this battle nor the war would end.

*This fight… is only just beginning.*

And at that moment, just as I muttered those words deep in my heart—

*Thud. Thud. Thuuum.*

An immense magical power surged from far away, making the desert tremble.
## Chapter artifact 804

# Chapter 804

Even when a thick fog hides the sea, anyone can tell there’s an ocean beyond it. They can hear the faint cries of gulls and feel the salt in the wind.

A battlefield is the same.

Screams and blood fly in every direction. Countless blades clash, throwing off sparks. And yet, something with a special power can change the air of a battlefield simply by existing.

Just like now.

*Rrrrmmm.*

The air trembled.

A deep rumble rolling in from far away shook the desert.

The monsters that had been charging over the bodies of their own kind came to a halt as if on cue. People stiffened with a start.

What were they feeling at that moment?

A chill creeping down their spines? Or fear they’d briefly forgotten?

I didn’t know exactly what it was, but at least I wasn’t feeling either one.

What you saw depended on where you stood.

In that sense, unlike them, I was standing on the peak. I could see and feel more, and from farther away.

And that wasn’t a privilege I enjoyed alone.

“This is…”

The Skeleton King, who’d come up beside me at some point, murmured as if groaning.

Magic Johnson, who’d been saving his strength by focusing on defense in the rear, had a grim look on his face. So did Yamamoto Genji, an S-rank Hunter at least in name, and Team Leader Choi, whose Qi Sense was nearly as sharp.

“Fuck.”

“Chikushō. This is insane. I have to get out of here.”

“So the leaders are finally making their move.”

*Whack!*

There’s always a reason when some bastard gets hit.

I kicked Yamamoto Genji in the shin for spouting nonsense at a time like this. As I turned away, I stirred my internal energy and stamped down with a quake step.

*Boom!*

The ground shuddered around me, and a wall of sand surged upward.

Through the countless grains falling back down, I saw the Hunters’ faces. They looked as if they’d just been doused in cold water.

“What are you all scared of? You all that eager to die?”

“B-but this is…”

“Call them whatever rank you like—they’re still monsters. And we’re all still Hunters. So quit freezing up like you’re about to die and…”

*Thud!*

I drove a dagger into the head of an ogre that was still writhing, stubbornly clinging to its life, then continued with emphasis.

“Fight. Like Hunters.”

*Ding.*

> **System**
>
> Defeated Lv. 95 Ogre!
>
> Gained a tiny amount of EXP!
>
> The effect of the Title **One Against a Thousand** activates!
>
> **Intimidation** has greatly increased!
>
> Enemies are rapidly losing confidence due to your **Intimidation**!
>
> The status effect **Fear**, which had been applied to numerous allies, has been removed!
>
> Ally morale has greatly increased. Those who follow your leadership will have a strong bond and perform even better!
>
> Certain stats increase when facing numerous enemies!

One Against a Thousand was the Title I’d earned while fighting the Arch Lich’s army in Sichuan Province. As a reward for accomplishing such a rare feat, it was definitely effective.

“GRAAAAAH!”

A few Hunters who’d been swallowing nervously until now roared, their eyes bloodshot. A tremendous cheer soon erupted, heating the air around us.

Of course, there were always exceptions.

“No, even so, that was a bit much…”

I clicked my tongue softly at the sight of Yamamoto Genji rubbing his shin where I’d kicked it, watching me warily. Then I turned my eyes toward the monster army stretching endlessly across the vast desert.

*Clack. Clack-clack.*

Their movements were orderly now, unlike before.

A force of well over ten thousand marched with measured precision, splitting to the left and right. Three paths opened, and at last, the beings radiating an overwhelming presence appeared.

*The S-rank monsters.*

Some were huge and grotesque. Others were so small compared to the monsters around them that they barely stood out.

But the powerful demonic qi and Fear pouring from them were as immense as that of all these countless monsters combined.

Enough to make even Yamamoto Genji afraid, despite his cowardice and lack of skill—or, at least, despite his being an S-rank Hunter in name.

“So those are the commanders leading this monster army.”

At the Skeleton King’s murmur, I spoke up.

“But the most important one is still missing.”

“…The Prophet.”

“Right. The Prophet’s the head. Those guys are the hands and feet.”

“But is he here now? It pains me to admit it, but… I haven’t seen or sensed anyone I’d take to be The Prophet.”

To be honest, the same was true for me.

But there was one thing I was sure of.

The Prophet was somewhere on this battlefield.

Given how meticulous the bastard was, he was probably watching everything unfold from some distance away.

*If he came close, I’d sense him right away.*

The enemies were too numerous, and the battlefield too vast, for me to get a clear read with Qi Sense.

On top of that, the monster army’s momentum had changed with the arrival of the S-rank monsters who could only be called its commanders. It was nothing like before.

“Jin.”

Magic Johnson’s low voice reached my ears. His eyes had sunk deep, as if he could already guess what the battle about to begin again would cost us.

And he was worried about me, the one who would have to bear the weight of it all.

“If you’ll let me, I’d like to take command instead.”

I stared silently at Magic Johnson for a brief moment, then shook my head.

“No. I’m in command.”

Of course, Magic Johnson had all the skill and qualifications for it. He was a veteran who’d lived through the Great Cataclysm and a fine commander who’d led his forces to victory in around a dozen major battles.

But…

“If there’s something I have to bear, I won’t push it onto someone else.”

“…!”

“That’s one of the reasons I’m here, isn’t it?”

Magic Johnson looked at me with wide eyes, then gave a small nod.

The voice that followed held firm trust and the faintest trace of a smile.

“All right, young friend. Give us our orders.”

I took a deep breath and looked around at everyone.

A thousand Hunters in all. I didn’t know all their names or faces.

But if someone fell here and never got back up, I’d remember everything about them for the rest of my life.

Yeah. That was enough.

If I died, they would, too.

“From now on, I’ll dispense with the formalities, Magic Johnson.”

“Yes, young boss.”

“Keep the enemies in the air in check and focus on protecting our allies. All subordinate Hunters are to follow Magic Johnson’s orders until I give them another command.”

“Yes, sir!”

With that answer, shouted like a cheer, Magic Johnson rose into the air.

The Grand Mage’s eyes, sharp as blades, watched hundreds of specks slowly crossing the cloudless sky—and the eagle beating its wings at their head.

More precisely, he was watching a monster with enormous wings tens of meters across and a lion’s lower body: a Griffon.

“Choi Minwoo.”

“Yes.”

“Take a hundred troops and hold the front line. If the tanks break formation, hand in your sword and retire.”

Team Leader Choi raised the **[Hero’s Sword]**, its blade shining with transparent light, and answered.

“That won’t happen.”

Team Leader Choi was the sole blood descendant of the great hero Cheon Taemin and the master of the Ares Guild, yet he’d never once slacked off in his efforts.

Sometimes I thought that if a new S-rank Hunter emerged anytime soon, it would be him.

I let out a quiet laugh at Team Leader Choi’s calm confidence, then turned to the others still waiting.

“Skeleton King. Yamamoto Genji. You two…”

“No need to waste time saying it. There are three S-rank monsters on the ground, so we can each take one.”

“M-me too?”

I silenced Yamamoto Genji with a hard stare, then corrected what the Skeleton King had just said.

“You and him take one each. I’ll take two.”

“What?”

“Huh?”

The two of them questioned me at the same time. At that very moment, I turned away and muttered inwardly.

*Open Inventory. Summon.*

The two daggers that had served me so well in close combat disappeared. The cool, solid feel of a spear shaft filled my hand, which had been empty for an instant.

A flame warped the space around it.

*Fwoosh.*

Force formed around the transparent spearhead, wrapping it in a clear sheen.

And in that brief instant, split into ever-smaller fragments, I drove the spear down like a streak of light, gripping it in reverse.

At the unseen enemy who’d crept up from deep in the desert without anyone noticing.

*Shhk. KRAAAAAASH!*

The ground, filled with searing heat, split like tofu.

Hard sand and earth beneath my feet shot high into the air. In the ground, gouged out like a vast crater, countless writhing life-forms came into view.

Among them was a monster larger than all the rest, gleaming red.

*That’s…*

A warning light flashed in my mind.

At the same time, the blue circle of **[Qi Sense]** that extended with my spearhead reached the monster’s hard body.

*Ding. Ding. Ding.*

> **System**
>
> Your **Qi Sense** is currently at eight stars.
>
> You have detected targets within range using **Qi Sense**!
>
> Lv. 87 Soldier Scorpion
>
> Lv. 76 Worker Scorpion
>
> Lv. 99 Elite Scorpion

Countless details came to me through my eyes and ears.

But my attention was fixed on only one of them.

> **System**
>
> Lv. 140 Scorpion King

Countless scorpions as large as adult men—and one scorpion larger than dozens of them put together.

*The Scorpion King.*

That was the enemy I had to take down first.

*KRAAAAAASH! Crunch!*

Superheated flames scorched the monsters’ lair, deep beneath the ground.

Their hard carapaces, sharp pincers, even the stingers on their tails—all of it melted away.

*Kiiiiieeet!*

The scorpions—or rather, the monsters—screamed in agony, their dying cries spilling out of the pit and into the world.

Humans and monsters.

Monsters and humans.

Everyone could hear their screams, and everyone reacted.

“Kill. The. Humans!”

The Demon Realm language erupted like a roar from an S-rank monster, and a massive tremor swept in every direction.

*Rumble, rumble, rumble!*

Their numbers weren’t the problem.

Their momentum, and the quantity and quality of the demonic qi they emitted, were beyond comparison with what we’d faced before.

The elite monsters waiting in the rear charged after their commanders, the S-rank monsters at their head. More than ten thousand monsters surged behind them like a wave.

*KRAAAAAH!*

On the ground, an enormous force led by three S-rank monsters. Over everyone’s heads, hundreds of flying monsters shrieked, led by the Griffon spreading its unusually large wings.

*Kiaaaak!*

The attack began across both sky and ground.

But I didn’t feel afraid or hesitate.

*Kiaaaat!*

I simply drove a decisive, certain strike into the Scorpion King as it screamed and shot up out of the pit.

*Crunch! Fwoooooosh!*

At that moment, the flames melted the acidic blood spilling out of it.

*Ding.*

With the System alert I’d been waiting for, I charged like a beast toward the S-rank monsters.

*KRAAAAAASH!*

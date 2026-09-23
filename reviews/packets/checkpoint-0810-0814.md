# Checkpoint Review — 810–814

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

# Chapters 810–814

## Plot

After burying their 185 dead, the Hunters pursue the fleeing monsters. Jin learns they went west but tells Magic Johnson they went east, then splits the forces: the main group follows the lie while Jin, the Skeleton King, Johnson, and Yamamoto Genji head west toward the oil fields named in The Prophet’s message.

At a canyon, Jin confronts Johnson and reveals his suspicion that The Prophet is the same Muninn who taught Michael Silbert to use magical power. Jin strikes Genji, exposing him as The Prophet: a Level 170 Doppelganger titled “The Final Abyss.” It says it met Michael during the 2020 Battle of Paris and spared him in exchange for killing the surviving humans. As fanatics close in, the Doppelganger regenerates by drawing on its victims’ lives, abilities, and memories. Jin destroys its Yamamoto Genji identity with Scorching Yang Qi, but The Prophet survives in another appearance. Hunters arrive on eagles and griffins as Jin presses the attack.

## Continuity

- Jin remains the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.
- The Prophet is a Level 170 Doppelganger titled “The Final Abyss.” It has concealed itself for decades, including as Muninn, and can revive by consuming victims’ lives and reproduce their appearances, abilities, and memories.
- Jin believes The Prophet has been the same Muninn for more than thirty years and taught Michael Silbert to use magical power.
- The Prophet says it met Michael on December 25, 2020, during the Battle of Paris. Michael agreed to serve it and killed the remaining humans in exchange for being spared.
- Jin destroyed the Doppelganger’s Level 120 Yamamoto Genji identity with Scorching Yang Qi, but The Prophet survived in another appearance. The confrontation continues in the canyon.
- Fanatics are advancing through the canyon. Hunters arrive as reinforcements on eagles and griffins.
- Jin sent the main force east to pursue the fleeing monsters, although he learned they went west. The Skeleton King knows Jin lied and chose to repeat the lie.
- Magic Johnson says he helped Jin because they are friends; whether Johnson is human remains uncertain.
- Jin remains preoccupied with unanswered questions about Michael Silbert. The Prophet has not explained why it wanted to live among humans or what it ultimately wants.

## Translation Decisions

- Keep **magical power** distinct from **mana**.
- Keep Demon Realm language distinct from other languages; retain **Sound Transmission**.
- Render **도플갱어** as “Doppelganger,” **진실의 눈** as “Truthful Eye,” and **최후의 심연** as “The Final Abyss.”
- Render 지크프리트 바스만 as **Siegfried Bassman** and 이노우에 히로시 as **Hiroshi Inoue**.
- Preserve **“Jin Sama”** as the unidentified ally’s form of address.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Prophet is a Level 170 Doppelganger titled “The Final Abyss” and has concealed itself for decades, including under the name Muninn.",
    "The Prophet can revive by drawing on the lives of its victims and can reproduce their appearances, abilities, and memories.",
    "Jin destroyed the Doppelganger's Level 120 Yamamoto Genji identity with Scorching Yang Qi, but The Prophet survived in another appearance.",
    "Fanatics are advancing through the canyon; Hunters arrive as reinforcements on eagles and griffins.",
    "Magic Johnson says he helped Jin because they are friends; whether Johnson is human remains uncertain."
  ],
  "continuity_sources": [
    813,
    814
  ],
  "open_questions": [
    "Why does The Prophet want Jin to flee, and what does it ultimately want?",
    "Is Magic Johnson human?"
  ],
  "safe_through": 814,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep the Demon Realm language distinct from other languages."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 810

# Chapter 810

Perhaps intuition was just another name for wisdom.

A feeling like the instincts etched into your cells had suddenly awakened.

The sensation of countless jumbled thoughts in your head converging into one.

“Michael Silbert. Michael Silbert. Michael…”

The name that should have stayed in his mind slipped from his moving lips, but Jin Taekyung didn’t notice.

One question filled his mind in a fleeting instant. At the same time, new thoughts came one after another, each following the last.

Whenever a question he asked himself came back like a boomerang, answer and all, Jin threw it again, this time carrying another question.

And each time, the same words led the way.

What if. Suppose. Maybe…

He kept doubting, without pause, without even a single moment to breathe.

Until the thoughts that had once again begun to tangle chaotically in his head took on a shape that seemed to make sense.

Without even knowing how much time had passed.

And…

So deeply that he didn’t notice someone’s footsteps—whose, he couldn’t tell—drawing close.

*Crsh.*

The sound of grains of sand crumbling roused his sleeping five senses.

The fine hairs on his body stood on end, and instinct moved him before his brain could give the order.

*Whoosh.*

As he spun around, the spearhead slashed down, cleaving through the air.

He’d repeated this movement thousands, tens of thousands of times in training and real combat. Etched into his instincts, it was terrifyingly sharp and fast.

Fast enough to make an intruder in the darkness think of death in an instant.

But the intruder was no pushover, either.

*Vwooom.*

A flash of light flared alongside an invisible ripple of qi.

In the space that had suddenly brightened, Jin’s eyes widened as he belatedly recognized the other person.

“……!”

Control came with the realization.

The strike, moving forward with tremendous speed and force, stopped as if someone had pressed a pause button.

The spearhead halted precisely before touching a translucent barrier suffused with a faint glow. At the same time, a fierce gust of wind swept through.

*Fwoooosh!*

Sand that had somehow escaped the blood was caught in the wind and scattered.

The intruder, who’d narrowly escaped danger, spat sand out of his mouth and spoke.

“Do me a favor. If you’re going to kill me, tell me first. Give me a little time to get ready.”

Jin lowered his spear and hurriedly asked, “Damn it. I’m sorry, Johnson. Are you hurt anywhere?”

“……As you can see.”

Magic Johnson managed to answer after dispelling his defensive magic. In that brief moment, cold sweat had gathered on the back of his neck, glistening in the faint moonlight.

“I’m fine. Though I might’ve had a little accident.”

“What?”

“Just so you don’t get the wrong idea, I’m big in every way. This time, though, it was only a little.”

At his joke, Jin let out a sigh of relief.

That had been truly dangerous. If he hadn’t stopped the spearhead at the last moment, there would definitely have been blood.

“I’m sorry again.”

“I said it’s fine. More importantly, Jin, what the hell was that?”

“What was what?”

“Why did you mistake such a wonderful friend and comrade-in-arms as me for an enemy? What were you thinking about just now?”

“Ah, well…”

Jin started to answer, then suddenly shut his mouth.

Magic Johnson watched him for a moment, then shrugged.

“You don’t have to tell me. If our young boss has a reason he can’t talk about it, then I’m sure it’s a good one. But there’s one thing I have to say.”

“If there’s something you have to say…”

“It’s that it’s been nearly thirty minutes since we finished regrouping. Whatever’s troubling you right now, if we delay the pursuit any longer, we’ll lose them for good. I came to tell you that.”

What? Already?

Only then did Jin belatedly check the time and bite his lip. Everything Magic Johnson had said was true.

*When did all that time pass…?*

It felt like less than a minute had passed since Choi Minwoo stopped by, but the sky had grown darker in the meantime.

*I must’ve had that much on my mind.*

The two characters meaning *self-forgetfulness* didn’t apply only to martial arts.

Jin had been so caught up in one question after another that he hadn’t even noticed time passing. Magic Johnson, meanwhile, couldn’t guess why Jin hadn’t moved from that spot.

“I know their deaths are weighing on you. That’s why I gave you a little time. But Jin, if we lose them now or fail to find The Prophet… remember, the sacrifices made up to this point will have been for nothing.”

*Pat, pat.*

Magic Johnson patted Jin on the shoulder with his large hand, then turned away after leaving him with one last remark.

“Everyone’s waiting. We need you, Boss.”

That was all.

Jin watched the Grand Mage’s back slowly recede and wondered how much truth was in the questions he’d come up with. What, exactly, was a lie, and what was the truth?

Then he steadied his breathing and murmured, “No. Either way, there’s only one path.”

He’d barely managed to get his hands on a single clue.

If there was no other choice, there was no point in worrying any longer. Jin took a heavy step toward the darkness lurking all around him.

* * *

The desert night was cold, dark, and vast.

But not one person complained as they quietly marched on.

One hundred and eighty-five.

We’d fought shoulder to shoulder with them, even if only for a short time, and lost them. Some had been strangers; others must have been close. We’d buried their bodies in the dunes, then had to leave them behind.

Instead of gravestones fit for heroes, we planted bloodied weapons in the sand and swore we’d return to those coordinates and bring them back to their families.

That was why the survivors kept moving forward, and I was at the head of them.

*Whoooooosh!*

Countless figures sped across the desert.

The wind, thick with sand, stung my face. But sand wasn’t all it carried.

*The stench of blood. And a foul odor.*

A nauseating but familiar smell drifted to me on the wind. Sticky liquid clung to the plants and rocks we passed along the way.

Blue-green blood. It had to belong to monsters.

*Where are you?*

I spread the energy coiled inside me over a wide area. At the same time, I sensed faint breaths and the traces of an unpleasant magical power.

“Shen.”

I stopped and called out. Xiao Shen immediately understood what I meant. He drew his sword in a flash and plunged it deep into the ground beneath his feet.

*Squish!*

Blood spurted from the sand as it suddenly caved in. At the same time, the ground all around us rippled like waves.

*Shhhhh!*

The forms of monsters briefly appeared amid the scattering sand. Someone’s urgent cry pierced the night air.

“Ant Lion!”

Colloquially known as the antlion.

Even the smallest specimen was about the size of a midsize car, and these powerful monsters were classified as at least Grade B.

But the one that had just appeared had pincers far larger and mana far stronger than any Ant Lion I knew.

*It’s one of the ones that fled the battle earlier.*

It was one of more than a hundred Grade A monsters that had saved their lives by retreating from the battlefield.

I moved as soon as I’d made my judgment.

*Tap.*

A distance of around twenty meters vanished in an instant. I brought my spear down on the monster as it tried to swallow up the Hunters closest to it.

*Shhk!*

One strike. Its two pincers, harder than steel, were sliced off like tofu.

Before its anguished scream could even ring out, I twisted the spear shaft in midair and slammed it into the monster’s body.

*Crack!*

Blood spurted out along with a nauseating stench, but the injury wasn’t severe enough to kill it.

I pressed the spearhead against the spot I guessed was between its eyes and moved my lips.

In the language of monsters, a tongue that didn’t belong to this world.

—I'll ask you a few things. Think carefully before you answer.

—……!

There were scholars who studied the Demon Realm language, but humans who could speak it fluently were rarer than named monsters.

The Ant Lion’s eyes, clouded with pain, flew open. It clearly hadn’t expected this.

—You. Human. How?

Instead of answering, I tightened my grip on White Flame.

*Shhk.*

As the keen spearhead cut smoothly through skin as hard as armor, a panicked voice burst out.

—I answer! Ask. Anything!

Judging from its clumsy Demon Realm language, it wasn’t very intelligent—but it was quick to catch on.

I stopped the spearhead and spoke calmly.

—Where are the others?

—Gone. All. Sun falls that way.

—West?

—Yes! There. Many!

There was no particular reason to doubt it. The Ant Lion in front of me was stupid, and every word it said was packed with truth.

*West, huh?*

Some must have fallen behind or scattered along the way, but most of the monsters that had left the battlefield had undoubtedly headed west.

Of course, I wanted to know something else.

—Then what about The Prophet?

—The Prophet?

—Yes. The Prophet.

The Ant Lion blinked its round eyes.

—What is that? Don’t know. Me.

I clicked my tongue, realizing my mistake belatedly.

The Prophet had personally announced that title to the world. Unless the monster army had gathered somewhere in the desert to watch TV, this creature couldn’t have known it.

—Let me rephrase. Not The Prophet. Your leader. The commander who leads you and the other monsters.

—Commander? Leader? Leads us?

The Ant Lion repeated my words haltingly, then looked at me with fear and confusion in its eyes.

—Dead. You. You all killed them.

—What?

—One. Two. Three. Four. All dead. Me, everyone. Scared. So ran away.

I looked down into its eyes.

Then I confirmed once again that there wasn’t a hint of a lie in what the Ant Lion had said.

—Right. So that’s what happened.

—Me, me, believe! Didn’t. Lie.

—I know.

I pushed the spearhead deep between the Ant Lion’s eyes and added calmly, “I know how many people died because of you, too.”

*Squish. Gurgle.*

With a bubbling sound, the monster’s enormous body trembled.

I shook the blood and bodily fluids from my spear as I heard a System notification announce another death.

Magic Johnson realized the interrogation was over and came over to ask, “What did it say?”

I answered in a dry voice. “No luck. It didn’t even know The Prophet existed.”

“……Damn it. Well, it’d be strange for an A-rank monster—not even an S-rank—to know all that. Did you find out where the ones that ran off are headed?”

“Yes.”

“Where?”

I stared at Magic Johnson without answering. Then I replied as if it were nothing.

“East.”

Over Magic Johnson’s shoulder, the Skeleton King stared at me with wide eyes.
## Chapter artifact 811

# Chapter 811

“East. You mean east.”

Magic Johnson turned his head to confirm the direction. For the Skeleton King, that was unfortunate.

He had to fight to hide the shock that flashed across his face.

But the shock filling his mind didn’t fade so easily.

*Why on earth?*

To the Skeleton King, a monster, the Demon Realm language was practically his mother tongue.

Unlike Magic Johnson, who had been watching the rear of the formation, he’d stayed beside Jin Taekyung at the front the whole time. He’d heard enough of the conversation to understand it perfectly.

*He definitely said most of the monsters went west. I’m sure of it.*

His thoughts tangled together in confusion.

For a moment, he wondered if Jin Taekyung’s expression—unchanged down to the color of his face—had somehow tricked him. But no. There was no mistake.

No matter how many times he went over it, his memory of what had just happened stayed the same.

*That vile human… lied.*

So what did Jin Taekyung’s lie, and this situation now, mean?

After a brief moment of thought, the Skeleton King found the answer himself.

The answer he’d already suspected, but had tried so hard to ignore.

*No way.*

Just as the Skeleton King’s pupils trembled at last as he faced an unbelievable reality, Magic Johnson’s gaze shifted from somewhere in the darkened east to him.

“Did you send your minions east to search—hey. Are you listening to me?”

“Hm? Oh. Of course.”

“What were you looking at?”

The Skeleton King had found himself looking at Jin Taekyung, but he couldn’t exactly say so.

The instant he heard Magic Johnson’s voice, his heart had lurched. He forced himself to settle down, then gestured with his chin toward the dead Ant Lion’s corpse.

“That one. I thought it might have decent mobility if I brought it back as an undead.”

“Hmm, not a bad idea. But it can burrow deep into the sand, so humans like us couldn’t ride it. And if it moved aboveground, its size would make it too conspicuous.”

“Then I’ll give up on it. Now that I think about it, controlling something like that would take a lot of magical power.”

Had he answered convincingly? Had Magic Johnson noticed anything strange about his behavior?

As Johnson slowly stroked his chin, the Skeleton King pushed down his anxiety and hurriedly continued.

“But what were you going to ask?”

“Oh, right. I was going to ask if you’d sent your minions to search the east.”

“The eagles and griffins?”

“Right. Didn’t they go out once already and come back? If the monsters fled east, I’d think they would’ve spotted them.”

Magic Johnson was right. The Skeleton King had already sent his subordinates east.

While everyone else regrouped and rested, a dozen or so eagles and griffins had taken to the sky and chased after the monster army as it fled in a panic.

Of course, the Skeleton King had soon run low on magical power, and the undead’s pursuit had ended without yielding anything. But at the very least, the Skeleton King knew there had been few monsters heading east.

“Well…”

The Skeleton King let his voice trail off. He could feel Jin Taekyung, standing beside Magic Johnson, watching him with a gaze gone dark and still.

*Damn it.*

He didn’t know whether the choice he was about to make was the right one.

But then he remembered something Jin Taekyung had once said. The words that had calmed not only him, but everyone around him.

*If you can’t trust yourself, trust me.*

He remembered. And at the same time, he repeated the words to himself.

Then, in an instant, his hesitation ended. The Skeleton King spoke evenly.

“I lost sight of them quickly, but there’s a good chance most of the monster army fled east.”

The Skeleton King trusted Jin Taekyung’s judgment—no, his friend’s judgment.

Maybe even more than he trusted his own.

* * *

Even before we met the Ant Lion, I’d already put the conflict lingering in the back of my mind far behind me.

All that remained was to pull hard on the thread I’d barely managed to grasp and find out what this mystery really was.

*But I can’t do that right away.*

I had to be meticulous. I couldn’t leave them an opening.

After quickly sorting out my thoughts, I gathered several of the people who could be considered the leaders.

“We’ll split up our forces and move out.”

My blunt opening sent a ripple of unease through the group. Team Leader Choi was the first to object.

“Weren’t we all going east together?”

Most of the monsters had headed east.

That was what everyone knew except the Skeleton King and me, so Team Leader Choi’s question made sense.

Assuming, of course, that the information they had was true.

“Team Leader Choi.”

“Yes?”

“When did I say that?”

“……But—”

“I know what you mean.”

My voice came out dry and unfamiliar, even to me. I stared at Team Leader Choi’s stiff face and continued slowly.

“But we can’t trust information we got from the Ant Lion and act on it. It’s too dangerous.”

“Do you mean it could have been an intentional trap?”

“Yes.”

It struck me again: I was pretty good at lying.

And on top of that, I knew one of the truths of the world I’d learned by living in both the Murim and the modern world.

*Authority.*

A lie told by someone with authority carries tremendous power to persuade. It calls forth the trust of the people who believe in him.

Just like now.

“They may have lost the battle and run, but they still outnumber us by more than five to one.”

Five thousand.

An army that had once numbered well over ten thousand had been cut down to a third in a single battle. But our side had taken losses, too.

Even with such an overwhelming kill ratio, we’d lost more than two hundred people. That was a fifth of our total force.

If the monster army was a pie so big it would take several slices to finish, we were a muffin someone could swallow in one bite.

“We need to proceed carefully. We should split up and pursue them.”

Xiao Shen, who’d been listening to me, nodded.

“I also believe you’re right, Sir Jin. If we act on false information, we could walk into a trap or head in the wrong direction and lose the monsters.”

“Exactly. Splitting up would lower the risk.”

Team Leader Choi furrowed his brow.

“I understand why you want to split up, but… wouldn’t that leave us vulnerable to being picked off one by one?”

It was a concern any commander should have, but the chance of that happening was extremely low.

*The monsters fled west, not east, to begin with.*

I swallowed the words hovering at the tip of my tongue and answered without hesitation.

“We’ll keep the units close together. That way, even with the unstable communications caused by the high concentration of magical power, we can maintain a reliable connection.”

“Hmm. I agree with Jin. I’ve done a rough calculation, and a hundred kilometers or so between units should be enough.”

I looked silently at Magic Johnson, who’d spoken up without warning, then replied with a heavy heart.

“That’s right. We’ll cover more ground, too.”

The Rub’ al Khali Desert.

As the world’s second-largest desert, it was truly vast.

Even Team Leader Choi seemed to realize anew how large it was. He reluctantly nodded.

“If we assign a hundred people to each pursuit unit… we could cover the southeast and northeast as well as the east. Understood. There’s no time to waste, so we should move quickly.”

But Team Leader Choi, who’d been about to hurry off, had to turn back before he could take a single step.

It was because of what I said at that very moment.

“You’ve left one thing out.”

“Mr. Jin Taekyung, what do you mean—”

“West. I plan to send a pursuit unit west, too.”

“What?”

“That’s the complete opposite direction.”

“That’s right.”

I looked around at everyone and continued.

“But if we travel a few more hours west from here, we’ll reach the oil fields. The very place the message The Prophet left for me points to.”

“……!”

“You heard it yourself, so say it. Am I right?”

My last question was directed at Yamamoto Genji.

He’d been looking miserable ever since I’d brought up splitting the forces. Now, with everyone watching him, he glanced around nervously and nodded.

“Uh, well. He said it was a land where black jewels were buried, so I think that’s probably right…”

“Good enough. We’re going west.”

“Wait. We are?”

“Yes. Us. You, me, the Skeleton King, and Magic Johnson.”

Yamamoto Genji’s face went deathly pale.

“Jin-sama! Where does that even happen?”

“Right here.”

“This is ridiculous… Leave me out of it! I want to stay with the others!”

“No. I’m not leaving you out. I have no intention of leaving you out. Go back.”

After answering firmly, I continued speaking to the people who were blinking at this unexpected turn of events.

“Our real reason for coming here wasn’t the monster army. It was The Prophet. We need to follow his message at least as far as the place it points to. We’ll be back soon. Until then, avoid any clashes and keep pursuing the remaining monsters.”

“No!”

Team Leader Choi, who’d been staring at me blankly, shouted in protest.

“Common sense says that if The Prophet were in the west to begin with, the monsters would have no reason to run in the exact opposite direction, east!”

“That’s true. But if, like the Ant Lion, most of the monsters don’t know The Prophet exists, then they have every reason to run east.”

“Mr. Jin Taekyung. Do you really believe The Prophet is there?”

“I don’t know. But even if he isn’t, you and the others will still be pursuing the monsters, so nothing will go wrong. And if he’s in the west… we’ll have enough strength to take him on.”

There were three S-rank Hunters.

No, four, if we counted the Skeleton King. And with his abilities, he could fight alongside his undead soldiers, too.

“But…”

Team Leader Choi let his words trail off.

Just as he parted his lips to say something, I delivered the final blow.

“This is an order.”

“……!”

“Hurry. Before they get any farther away.”

With that, I turned around.

Then, toward someone who’d been standing there in silence all this time, I sent a Sound Transmission so casually it might have passed for a breath.

—From now on, don’t answer or react to anything I say. Just listen.

For a brief moment, the Skeleton King’s eyes, which had been trembling violently, settled into a deep stillness.

* * *

Immediately after the one-sided discussion ended, I finished a short session circulating my qi and set out west.

Of course, I wasn’t alone.

The Skeleton King, Magic Johnson, and Yamamoto Genji came with me.

There were only four of us, but we were a powerful force, and we moved at a speed that couldn’t compare to when we’d been traveling with the army.

*Whoosh!*

Through the landscape flashing past us, I saw puddles of thick, sticky blood.

I didn’t need to look closely to know there was a lot of it, spread over a wide area.

It couldn’t have come from a few dozen monsters. Everything the Ant Lion had said was true.

*Though that isn’t the important part.*

I kept running, muttering to myself. We crossed rolling dunes and passed through an open stretch of wilderness.

After running for a little over thirty minutes, we finally reached a canyon where two cliffs faced each other. Only then did I start to slow down.

“Hah… Hah. C-could you slow down a little?”

Seeing Yamamoto Genji panting, Magic Johnson wiped his sweat-soaked forehead and spoke to me.

“Jin. How about we rest here for a bit? I don’t see any monsters around.”

Instead of answering, I came to a complete stop and slowly looked around.

Cliffs stretching into the distance. A narrow passage. Good terrain.

Little room to move. A narrow escape route.

I looked up at the sky. In the distance, I saw a shadow flapping its wings against the faint moonlight over the desert.

*An eagle.*

Following my gaze, Magic Johnson frowned.

“Still seeing birds out here, huh? With this concentration of magical power, it should be almost impossible for them to live here.”

“Not impossible, if they aren’t ordinary eagles.”

“What?”

While Magic Johnson blinked, unable to understand what I meant, I blocked the canyon entrance.
## Chapter artifact 812

# Chapter 812

*Step.*

Feeling the earth crumble beneath the weight of his foot, Jin Taekyung wondered:

Was the sound of his footsteps echoing so loudly because the night had grown deep? Or was it because every nerve in his body was on edge?

He didn’t know. Maybe it was both.

But one thing was certain. From this moment on, no one would leave this long, narrow canyon without Jin Taekyung’s permission.

“Jin?”

In the air that had suddenly grown heavy, Magic Johnson had been staring at Jin Taekyung as if he couldn’t understand what was happening. Then he abruptly turned his head.

Beneath moonlight spilling down the sheer cliffs, a figure now stood blocking the exit, its golden eyes gleaming.

The Skeleton King.

Soundlessly moving lips murmured the figure’s identity.

At the same time, the Grand Mage’s eyes sank as he realized the situation surrounding him.

“What does this mean?”

“It doesn’t mean anything in particular. I just have a few things I need to check.”

His tone was gentle, but his eyes were cold.

The eagle in the distance had already been erased from his mind.

Magic Johnson stared at Jin Taekyung.

“If it isn’t urgent, why not check later?”

“It’s urgent. I have to check now.”

“Caution is a leader’s virtue. But I don’t think now is the right time.”

“I can see why you’d think that. But isn’t judging the right time exactly what a leader does?”

Magic Johnson fell silent for a moment, then let out a quiet laugh.

“You’re right, Jin. I didn’t know you were so good with words.”

“I’ve noticed this now and then, but test scores and running your mouth are two different things.”

Jin Taekyung smiled faintly along with him, then abruptly called out a name.

“Genji.”

“Y-yes?”

Yamamoto Genji, who had been watching Magic Johnson nervously, jumped at the sudden call.

He’d already realized that the situation was getting serious. As his eyes darted around, Jin Taekyung jerked his chin at him.

“You look uncomfortable. Come over here. You’re getting on my nerves.”

“Y-yes, sir!”

Yamamoto Genji glanced at Magic Johnson and took a step forward.

But when the hulking Grand Mage showed no reaction, he hurried over and stood beside Jin Taekyung.

“U-um. Jin-sama. What exactly is going on right now…”

“Shut up.”

Jin Taekyung answered calmly, then looked at Magic Johnson.

Even with the situation changing so abruptly, Johnson’s expression hadn’t shifted in the slightest. He was still sitting on the rough rock.

“Johnson. When did we first meet?”

It was an out-of-the-blue question, but Magic Johnson answered without hesitation.

“During the Arch Lich subjugation. It hasn’t even been a year.”

“It feels strange. It seems like it’s been ten years already.”

“A lot has happened. Things we never thought would happen again—things we couldn’t even imagine.”

“Yeah. I really didn’t think things would turn out like this.”

Jin Taekyung smiled bitterly. Two years ago—no, even just a year ago—he’d been nothing more than an unusually talented F-rank Hunter.

He’d never escaped the confines that had been set for him by fate when he awakened. He’d spent each day in a cramped, musty goshiwon room.[^1]

But everything had changed.

Last summer, which had been unusually hot. One day, without warning, he’d been handed a notice that he was fired.

And then… the beat-up capsule that had been waiting for him on the melting asphalt.

Every one of those moments was still vivid.

That night, the beat-up capsule had tossed the fool who’d been reckless enough to crawl inside it for a nap into a new world. Jin Taekyung had escaped his confines and changed his fate.

“‘Things we couldn’t even imagine.’ That’s probably the best way to put it. I know because I’ve experienced it myself. But you know what’s funny?”

Jin Taekyung didn’t wait for an answer.

The faint smile had vanished from his lips. They were now as rough and hard as the rock Magic Johnson sat on.

“Even after going through so many things I couldn’t have imagined, my imagination barely improves.”

A being called the Demon King had descended upon Earth. Countless monsters had burned cities and slaughtered people.

Humanity had won after five years of the Great War, then built a civilization even more brilliant and vast.

Impossible things. And yet, they’d happened to everyone just a few decades ago.

Jin Taekyung hadn’t lived through that era, but he’d crossed dimensions, traveled between two worlds, and gathered countless experiences.

“Sometimes I think common sense is terrifying. It keeps you thinking inside the same old box, and you end up going nowhere.”

Jin Taekyung tapped his temple with a dagger he’d somehow drawn.

Magic Johnson had watched in silence. Now he broke it.

“So this time, you tried to use your imagination a little more?”

“Yes. I went back over everything that’s happened so far. Slowly. From as objective a perspective as I could manage.”

“Jin, humans can’t be objective.”

Magic Johnson was right.

People’s judgments were always subjective. Ironically, humanity had become the master of the world because, more than any other creature on Earth, it was made up of thought and emotion.

But…

“I found I could at least try. Set aside what I know and how I feel about someone as much as possible.”

“Right. You can try to look at things objectively. That’s humanity’s greatest strength.”

“Hmm.”

Jin Taekyung licked his lips.

“That’s a dangerous thing to say.”

“Which part?”

“I don’t know. You make it sound like you’re not human.”

Magic Johnson’s clear eyes reflected Jin Taekyung. A short laugh slipped from between his lips, breaking the brief silence.

“So, Jin. Did you achieve what you wanted in the end?”

“Probably.”

Magic Johnson already knew what Jin Taekyung had been working so hard to figure out—and what he was trying to determine.

“The Prophet.”

His deep voice carried through the night air. Jin Taekyung gave a small nod.

“I started with the one most closely connected.”

“Michael Silbert. That would be the obvious place to start, considering their connection.”

“Huginn called The Prophet Muninn. The fifth Muninn, at that. One of a series of beings swapped out like spare parts to make Michael Silbert who he is today. And on top of that, The Prophet uses magic that isn’t human.”

“That’s why we suspected he was a monster.”

“Right. But isn’t something strange? Huginn only learned of the fifth Muninn three years ago, yet Michael Silbert had already been handling magical power little by little since the Great Cataclysm.”

“What’s strange about that?”

“Of course it’s strange. A human somehow made magical power and mana coexist—that’s insane. Even I can’t do it now. And that guy did it thirty years ago? No way.”

Then Jin Taekyung added one more thing.

“Unless a real monster helped him.”

Magic Johnson paused. Jin Taekyung continued without paying him any attention.

“But the timing didn’t add up. Three years ago and thirty years ago. There was too much time in between.”

“……”

“After thinking it over, I came up with one answer.”

Jin Taekyung scratched at his chin with the dagger. His stubble, which had grown in patchy after a week without shaving, was scraped and cut by the sharp blade.

“The Prophet isn’t the fifth Muninn.”

*Shhk.*

The instant a drop of blood rolled from the tip of his chin, where the blade had nicked him, a chilly voice pierced everyone’s ears.

“For more than thirty years, there has been only one Muninn.”

“……!”

“……!”

The air around them turned cold. Jin Taekyung shook the blood from his dagger and continued.

“Once I thought of it that way, things finally started to add up. What the hell, this wasn’t a claw machine. I couldn’t understand how people that powerful and loyal kept popping up every few years.”

Yamamoto Genji had been listening with wide eyes. His mouth hung open.

“Th-then…”

“Yeah. The Prophet was Michael Silbert’s teacher, the one who taught him how to handle magical power, and the two worked together toward their own goals. And he must’ve been an incredibly powerful fighter for a long time—even thirty years ago.”

The scattered pieces began to fall into place, one by one. Jin Taekyung’s voice became an unseen hand, feeling its way over countless pieces.

One. Two. Three. Ten.

He filled the blanks according to the shapes that fit. Each time he did, someone’s figure slowly began to emerge.

That was right. This was a portrait of someone—and a puzzle.

But…

*Not enough. Not nearly enough.*

There were still questions he couldn’t answer before he could put together this enormous puzzle.

Lose even one piece, and the puzzle couldn’t be completed. And filling the many empty spaces in this one was nearly impossible.

To be precise, it was impossible for Jin Taekyung to do alone.

“Johnson.”

Jin Taekyung spoke without warning.

The Grand Mage had risen from the rock. His shadow loomed large, and the staff in his hand gleamed in the moonlight.

“Can I ask you one thing?”

“Anything, Jin.”

“Why have you helped me all this time?”

“Because we’re friends.”

“Like Siegfried Bassman?”

Magic Johnson raised his staff as he answered.

“Yeah.”

“I hesitated until the end. Honestly, even now I’m not sure. It makes no sense for a monster to use mana and even potions.”

“Anyone would think that if they were human. But there’s nothing in this world that can’t happen.”

*Vwooom.*

The Magic Gem at the tip of the staff began to vibrate. It was an S-rank Magic Gem, obtained by killing a monster that had slaughtered an entire city on its own during the Great Cataclysm.

Feeling the enormous flow of mana surging with the wind, Jin Taekyung suddenly spoke.

“Do you remember what you said earlier?”

Magic Johnson gave a heavy nod.

“I remember. Humans can’t be objective.”

“You were right. I’m only human, so I couldn’t help thinking subjectively.”

“Everyone does. He’s a bit of an unusual case, but that friend is the same.”

Magic Johnson gestured with his chin at the Skeleton King behind him.

Beyond the Skeleton King, wearing a golden crown made of magical power, hundreds of pairs of eyes filled the canyon, gleaming.

“Then sending the other forces east was…”

“I didn’t want people who had nothing to do with this getting caught up in it.”

“Excellent. Was that your decision?”

“Yes, but…”

Jin Taekyung raised the dagger in his hand and continued.

“It wasn’t just a subjective judgment.”

And at that moment—

*Flash!*

A blinding light burst from Jin Taekyung’s eyes.

Everyone who faced the sudden flash in the darkness froze for an instant. But one person did not.

Jin Taekyung himself had called forth the light. He’d wanted it.

*Crack. Stab!*

The dagger shot forward like a beam of light, smashing through armor and tearing through flesh and bone. Jin Taekyung looked at Yamamoto Genji as he staggered, then spoke.

“What the hell are you?”

Yamamoto Genji’s eyes were wide with disbelief.

Then he—no, The Prophet—grinned.

[^1]: A goshiwon is a small, inexpensive room-for-rent lodging, often with very little space.
## Chapter artifact 813

# Chapter 813

*Fwoosh.*

Everything sharpened and slowed.

The dirt and sand kicked up by his staggering retreat. His eyes, wide open. Even the blood surging from his chest.

And then…

“What the fuck are you?”

With those words spat from my lips, time returned to normal.

I could clearly see Yamamoto Genji—or rather, the bastard—grinning as he curled up the corners of his mouth.

*The Prophet.*

His eyes, which had been wide with pain just moments ago, now glinted with incomprehensible joy and surprise.

*He’s happy? In this situation?*

I shoved aside the question of why and swung the dagger in my hand again.

The Prophet was staggering, clutching his blood-spurting chest. The moment he reached for the sword at his waist, a slash burst from the dagger’s blade and streaked through the darkness like a flash of light, a step ahead of him.

*Shhk.*

A faint line appeared across The Prophet’s wrist with a chilling cut.

His right hand, which had half-drawn the sword, lost its strength and fell away from his body.

*Thud. Splatter!*

Blood sprayed across the ground. It was the same red blood as any ordinary human’s, which made it all the harder to believe.

Even as I charged at him.

*Whoosh. Crack!*

I drove my heel down with the force of a thousand pounds. The flesh of his calf burst, and the joints in his bones shattered.

The Prophet had completely lost his balance and dropped to one knee. He reached out with his only remaining hand, but this time, I didn’t even need to step in.

“Stop.”

The wind died at the sound of a deep, low voice. The air trembled.

I couldn’t see it, but I could feel it.

The Grand Mage’s mighty mana wrapped around us. That power had seized The Prophet’s wrist before his hand could reach me.

*Crack.*

His hand stopped dead in midair. The sound of bones grinding out of place twisted his brow.

Just then, The Prophet’s body began to rise slowly into the air, as though an invisible giant had grabbed him and lifted him up.

*Whistle—thud, thud, thud!*

Something pure white shot toward him like a beam of light and pierced his limbs.

The long, sharp bone shards sliced through flesh and bone like tofu, pinning his body—which had been floating in the air—deep into the cliff.

*Crunch!*

The solid rock, which might have stood in that spot for hundreds or even thousands of years, made an excellent support.

Taken down in an instant, starting with my unexpected ambush, The Prophet abruptly spat out blood.

“Cough. Heh heh.”

Pain was the same for everyone.

But The Prophet laughed, curling his bloodstained lips as if he couldn’t feel a thing.

“Good. I’ll give you this much first: you did very well.”

*Wham!*

The Prophet’s head snapped back from a direct hit to the face. His skull slammed into the cliff with a boom, and he shook his head.

“It’s been a while since I felt my head ring. Having fun is nice, but let’s not overdo it.”

“……!”

I stifled the groan trying to escape my lips.

I’d already severed his wrist and shattered his knee. And that wasn’t all. My very first strike had pierced the area around his heart.

He’d pulled away at the last moment, but the tremendous Scorching Yang Qi infused into my dagger had still been enough to wreak havoc inside his body.

*An ordinary human would already be dead.*

But he wasn’t. The Prophet wasn’t.

That life force, strong to the point of being incomprehensible, didn’t belong to a human.

And unlike Michael Silbert, who had been practically half-human and half-demon, then died in the form of a monster while bleeding monster’s blood, The Prophet was still shedding red human blood.

“……Jin.”

“What… what the hell is that thing?”

Two voices pierced my ears.

Magic Johnson and the Skeleton King stared at the incomprehensible being, their gazes trembling. The Prophet laughed, his voice thick with blood.

“No one will ever be able to answer that. That’s what I am.”

No. He was wrong.

I steadied my breath, which had grown ragged without me noticing. The two eyes giving off a faint glow were as hot as flames.

This was the price of temporarily accepting a power beyond humanity.

At the same time, it was a gift the System had given to one foolish human—and the only key that could put this enormous puzzle together.

*The Truthful Eye.*

A special item I’d received as a Reward for completing the Quest **Unknown Death**, which began with Siegfried Bassman’s death.

I’d only glanced at the details of the Truthful Eye before. I recalled them again the moment I found a clue.

> **System**
>
> **Item Window**
>
> **Truthful Eye**
>
> **Type:** Single-Use Item  
> **Grade:** Special  
> **Restriction:** Jin Taekyung  
> **Description:** In the distant past, a god who would become part of myth offered up an eye to drink from the spring of wisdom. In exchange for one eye, he gained infinite wisdom, while the eye that sank to the bottom of the spring gained the power to pierce even the truths of other worlds.
>
> **Effect:** Can be applied to a single target only.

*Looking back, the System had always shown me the way.*

At first, I hadn’t known what the consumable item the System called the Truthful Eye was for. I hadn’t known what that hologram only I could see was trying to tell me.

But not anymore.

A few hours ago, I’d found the only clue. And the System had handed me the key to unravel it one step ahead of me.

A key that could be used on only one target—and therefore had to be used with even greater care.

And now, in this very moment, I’d gained the power to pierce every truth.

*Fwoooosh.*

It was hot. My vision turned white.

But the divine power dwelling within it pushed through the pain and reached out.

Toward Yamamoto Genji. Toward the Pope of the fanatics who had built a temple in this desert.

Toward the incomprehensible being who, under the name Muninn, had spent the past thirty-odd years sowing the seeds of catastrophe in this land, and was now about to make them bloom himself.

It was a thick veil that even **Qi Sense** couldn’t penetrate. But the eye of the old god called Odin saw through it all.

Pierced it. Revealed it.

*Flash!*

The instant a distant, blinding light flooded my vision, countless bells thrashed inside my mind.

System notifications and holographic windows I’d never heard or seen before raced to the ends of the earth and soared above the clouds.

*Ding. Ding. Ding. Diiiiing!*

One sound swallowed another. The translucent holographic windows multiplied from one to five, from five to dozens, then to a hundred.

They were a wave. A mountain.

“Ah…!”

A gasp escaped me before I knew it. A chill ran down my spine at the sight unfolding before my eyes.

Hundreds, perhaps thousands.

More holographic windows than I could count burst forth like fireworks. They all came from one being—the beginning and center of everything.

*The Prophet.*

I could hardly breathe. What I was looking at wasn’t mere information. They were the countless lives he had devoured, and the gravestones they had left behind.

Gravestones that held nothing but names and levels.

And the Truthful Eye within me had seen through the identity of the gravedigger who had built this enormous cemetery, filled with the names of the dead.

It stripped away the thick veil he’d wrapped around himself and revealed the truth.

*Ding.*

The final bell rang in my ears. With it, the last piece of the puzzle fell into place in my mind.

*This is…*

At last, I understood.

The Prophet’s true nature. How this cursed monster had hidden his identity and carried out everything for more than thirty years.

*Right. Now I understand.*

I stared at The Prophet, still smiling. Then, with the breath I’d been holding, I spat out a single word.

“Doppelganger.”

In that instant, I saw it clearly.

“……!”

The corners of his mouth, which had been curved like a half-moon, stiffened. The holographic window hovering above his head shone with a particularly gloomy light.

> **System**
>
> **Level 170 “The Final Abyss” Doppelganger**

* * *

Doppelganger.

A harbinger of ill fortune, a being passed down like a superstition.

Yet even as countless monsters from old myths tore through the pages of legend and leaped into reality, the doppelganger had never once shown itself. Humanity believed there were no doppelgangers among the enemies they had defeated—or those they still had to defeat.

They believed that not even in that horrifying Demon Realm did such a being exist. That it was merely an illusion born of people’s fear, nothing more than a superstition.

But they were wrong.

Doppelgangers had existed from the very beginning. Everyone had simply been mistaken because one had never once revealed itself.

At least, Jin Taekyung knew that better than anyone.

He even knew just how long this incomprehensible being, which had devoured countless lives, had been seeping into the world.

“Michael Silbert. The Great Battle of Paris.”

The young man’s voice emerged abruptly, hard as the cliff rock surrounding them. The monster’s mouth, which had stiffened for a moment, relaxed into a smooth grin.

“That’s right. On the very day you humans call Christmas, I met him and became part of this world.”

December 25, 2020.

The great battle that made a page in history—and made the name Michael Silbert known to all humanity.

As one layer of that day’s truth peeled away, Jin Taekyung swallowed hard. The Skeleton King clenched his teeth, while Magic Johnson stared at The Prophet—or rather, the doppelganger—in disbelief.

“That can’t be. The one that attacked Paris at the time was definitely…”

“A dragon. More precisely, a hatchling less than three hundred years old. It was born a dragon, so arrogance was in its nature. And it let its guard down, as young ones do. Of course, it was unexpected that a human would kill it, even so.”

The doppelganger cut Magic Johnson off, then continued.

“In the end, it was just bad luck. For that young dragon, and for the humans who miraculously survived facing it.”

The Grand Mage, who had lived through the Great Cataclysm firsthand, couldn’t hold back a groan.

“……It was a lie, then. Michael Silbert made all of it up.”

“Well, I wouldn’t say he made it all up. It was true that a dragon attacked Paris, and that he was the only one to survive.”

The doppelganger grinned.

“I knew the moment I first saw Michael. Unlike the other humans, he was quick to size up the situation. Before I’d even killed half of them, he was already on his knees before me. He begged me to let him live. Said he’d do anything.”

“……!”

“It was an interesting offer. I accepted, and he killed the rest of the humans with his own hands.”

Jin Taekyung suddenly remembered a line from the conversation he’d had with Michael Silbert just before the man met his end.

*I was struggling to survive, too!*

The cry had sounded as if he were spitting blood.

He’d been right. Michael Silbert had struggled to survive. He’d had a greater will to survive than anyone, and ambitions he hadn’t yet fulfilled.

And so, a human and a monster joined hands.

But it wasn’t a shackle. It was a contract. Two monsters who differed in appearance but shared the same nature had made a deal to achieve their own goals.

But…

“What for?”

“What?”

“I asked what it was for. What was your real reason for wanting to live among people in this world?”

At Jin Taekyung’s words, spat out as if he were grinding his teeth, the doppelganger fell silent for a moment, then curled up the corners of his mouth.

“Well, I don’t think now’s the time to wait for my answer.”

And at that moment—

*Rumble.*

A tremor coming from far away swept through the canyon.
## Chapter artifact 814

# Chapter 814

*Crack. Rumble.*

The ground shook. Clods of dirt and fragments of rock broke away from the impossibly high cliffs and began raining down overhead, one after another.

“……Damn it.”

Magic Johnson muttered with a groan. The Skeleton King and hundreds of undead, blocking the canyon’s exit, crouched low and glared into the darkness.

More precisely, at the countless enemies approaching from beyond it.

*Fwoooosh.*

I steadied my breathing and raised my Qi Sense. With my senses sharpened to their limits, I took in everything around me.

The depth and intensity of the tremors traveling through the ground. The wind blowing from the west, and the scent carried on it. And the sounds.

The distance made it impossible to determine the enemies’ exact number or strength, but I could be certain of one thing.

*They’re not monsters.*

That left only one possibility. The Doppelganger, sensing my gaze, bared its bloodstained teeth in a grin.

“Humans are such strange creatures. They’ll throw their lives away for a being they’ve never even seen, calling it a god. All it takes is a few solemn words, and they’re weeping buckets.”

“Fanatics……”

“I liked this land from the start. It was a good place to make plans and cover them up. Most of all, it was crawling with people willing to give their very souls to religion. It was astonishingly easy to win the faith of fools like that.”

*Squirm. Crack.*

The cleanly severed stump of its wrist twitched. Through the gaps in its shattered armor, I could see fresh, pale flesh already growing over the dagger wound in its chest.

It wasn’t a potion. It wasn’t magic.

And yet, even now, its broken body was healing.

An unbelievable rate of recovery—obviously not human.

A power of Regeneration that anyone would have to question.

But the fanatics who had been launching terrorist attacks around the world since before the Great Cataclysm would have seen it differently.

Perhaps they’d glimpsed the shadow of a god in the Doppelganger, who used mana and had the same red blood and flesh as them.

“A miracle.”

Its voice rang out, brimming with excitement. The Doppelganger stared at me with blazing eyes and continued.

“To them, I am not a monster but a miracle itself—the Prophet who will lead them to the promised land.”

“……!”

“They’ll fight until the very last person falls. For their god. And for me.”

I didn’t argue with the Doppelganger’s confident claim.

It was simply the truth.

No matter what we did, a clash was inevitable.

The Doppelganger had planted its followers in this desert far earlier than I’d expected. And the wave of fanatics that began there had already shaken the world in the form of terrorism.

So even if I told them the truth about the Doppelganger, nothing would change.

*If a few words were enough to make them see reason, they wouldn’t be fanatics.*

This was ultimately the joint work of monsters and madmen. And right now, I was nothing but a heretic who had to be killed.

A heretic persecuting the great Prophet chosen by God.

“Then there’s only one thing left to do.”

I muttered evenly, staring at the Doppelganger. It understood what I meant, and the corners of its mouth curled upward.

“I’m looking forward to it.”

“Yeah?”

*Thud!*

As I spoke, I thrust my dagger forward, piercing its heart.

Its limbs were bound, so there was no way it could dodge. But the Doppelganger frowned and sighed.

“Give it a rest. That hurts like hell.”

*Crack.*

The severed muscles and shattered bones returned to their proper places. Fresh, rosy blood welled up, and smooth, childlike skin covered it.

It healed at a staggering speed, as if a video were playing in fast-forward.

Even the great shards of bone that had pierced its limbs and pinned it deep into the cliff shifted slightly, pushed by the flesh and bone growing around them.

The countless Level windows I’d seen with the **Truthful Eye**—and could still see now—weren’t just numbers.

*Other lives.*

They were fuel, and they were the lives of the victims the Doppelganger had devoured.

Like an arcade game character that came back to life as soon as you fed it a coin, the bastard could revive endlessly.

*But it’s not truly immortal.*

I twisted the dagger still in my hand. Heat surged from my dantian, raced through my acupoints, and flowed into the dagger.

*Thud—boom!*

Scorching Yang Qi poured through the dagger buried deep in its chest and exploded inside the Doppelganger.

Its heart had already been pierced once, yet it had recovered like an immortal. Now it was crushed completely. The clear bell I’d been waiting for rang beside my ear.

*Ding.*

> **System**
>
> Defeated Lv. 120 Yamamoto Genji!
>
> Gained a significant amount of **EXP**!

“……!”

One life faded, and a new one took its place.

The Doppelganger was still grinning. Behind its melting skin, another unfamiliar face was ready to emerge.

“Imagine that. Jin Taekyung killed Genji. Japan’s going to lose its mind when they hear about this.”

“Shut your mouth.”

The low bridge of its nose and the crooked teeth visible in its mouth.

Judging by those distinctive features, clearly East Asian, it had to be a Hunter from J1—one of the team thought to have been wiped out, apart from Yamamoto Genji.

“Come to think of it, I forgot to introduce myself. Nice to meet you. I’m Hiroshi Inoue. I spent my childhood in Nagasaki, then moved to Tokyo…….”

I grabbed it by the throat and twisted hard.

Unable to withstand my tremendous grip, the Doppelganger’s neck snapped at once, its head lolling at a grotesque angle.

*Ding.* Another bell rang, and the twisted head straightened. The face, smiling coyly, belonged to a woman I’d never seen before.

“Oh, did you know? This woman was the lover of the man you just killed. Looks like they were planning to get married this year.”

“……!”

My hand stopped dead, as if someone had hit a pause button. The Doppelganger whistled, clearly enjoying itself.

“Wow. So passionate. Humans really are amazing when it comes to things like this. We could learn a thing or two.”

“……You.”

“Ah, sorry. I apologize if that made you uncomfortable. But what can I do? It’s my ability.”

I clenched my teeth.

The Doppelganger hadn’t just absorbed its victims’ appearances. It could reproduce their abilities exactly as they’d had them in life—and it had their memories, too.

And the memories spilling from its mouth dug into my chest like an awl, making me hesitate.

*Crack.*

Blood seeped between my clenched teeth.

Beyond the canyon, the tremors had grown stronger, and I could feel a fierce killing intent. In front of me, a monster that came back no matter how many times I killed it was smiling faintly.

“Jin!”

Magic Johnson’s urgent shout struck my eardrums. The smile on the Doppelganger’s face deepened.

“This is your last chance.”

“What?”

“Right now is your last chance to run and survive.”

“……!”

*Whoosh.*

The cool desert wind brushed my face. It felt as if I’d been doused in cold water.

The Doppelganger shrugged at me, frozen like a statue.

“I understand. It’d hurt your pride. You’d be embarrassed. But if you die here like the rest of those humans, would that be a pointless death—or a noble sacrifice by a hero?”

“……That’s……”

“You have to look at the bigger picture. You’re the World Hunter Federation’s Alliance Leader. The one and only light and hope who can save this world, like someone from the past. Aren’t you?”

Its gentle voice tickled my ear, like a snake coaxing me to steal and eat the forbidden apple.

The Doppelganger’s low whisper wound softly around my whole body.

“Run. And survive.”

*Rumble.*

The canyon shook. The footsteps of countless fanatics—and the hooves of the camels they rode—were approaching from the darkness beyond.

“Think of your family and friends. Can you even imagine how much sorrow and pain they’ll suffer because of your death?”

“……Sorrow and pain?”

“That’s right. You’ve been through it yourself.”

My lips moved without a sound.

Sorrow and pain over someone’s death. Yeah, I’d been through it. An experience that had shaken me so badly my heart had nearly collapsed.

“No one will blame you. Even I respect everything you’ve done. So even now……”

The eyes of the nameless woman—or rather, the Doppelganger—sparkled.

“Run.”

*Allahu Akbar!*

The mighty roar of countless voices merging into one rang across the darkening desert.

Brilliant radiance shimmered around Magic Johnson, while hundreds of undead stared with dimly glowing eyes at the waves of fanatics surging toward them.

And I……

Let go of the Doppelganger’s neck.

*Step.*

When I took a step back, I saw its smiling face. In a gentle voice, as if speaking to a child, it said:

“Good. You made the right choice.”

I found myself muttering:

“Is this the best option?”

“It has to be.”

“Good. Then I’m glad.”

I nodded, then murmured under my breath.

“Open. Summon.”

“Hm?”

*Shhk!*

Along with its hollow question, the Doppelganger’s head shot into the air.

A new face rose onto its shoulders, as if a page had turned, and blinked.

The heat blazing around **White Flame**’s spearhead was turning its eyes red.

“What the fuck are you, some Ditto from a failed link trade? Quit trying to pull that crap on me.”

Only then did the Doppelganger understand what had happened. It sighed.

“You crazy bastard……”

“Got anything more original? I’ve heard that one so many times I’m sick of it.”

“Why are you doing this?”

“That’s what I want to ask you.”

“What?”

“You started spouting nonsense from the get-go, and I wondered what the hell was going on. But the more I listened, the more curious I got. You’re the first monster I’ve ever seen telling a human to run. For a second, I almost called you Mom, you son of a bitch.”

“……”

“What the hell are you? You’re trying so hard not to get caught, but you keep giving yourself away. So I know you’re stupid—but what do you actually want?”

A brief silence followed. The Doppelganger stared at me without a word, then furrowed its brow.

“Damn it. This has gone to shit. Why are you so reckless? You want to be remembered by history as a hero who made a noble sacrifice?”

“Quit talking out of your ass and answer me. My dream is to be the head of a village where everyone lives to a hundred.”

“Then why the hell……!”

*Scree!*

A cry rang out from the sky, swallowing the Doppelganger’s unfinished words.

It naturally looked up at the sky, and its eyes suddenly widened.

“……What’s that?”

I already knew what the Doppelganger was seeing.

Before the forces split off, I’d used Sound Transmission to give the Skeleton King direct orders.

“They’re a little late, but they made it just in time.”

*Screee!*

Dozens of eagles and griffins glided over the canyon with their wings spread wide.

On the backs of the enormous flying beasts, I could see the Hunters who should have gone east.

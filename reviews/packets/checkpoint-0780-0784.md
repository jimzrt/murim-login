# Checkpoint Review — 780–784

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

# Chapters 780–784

## Plot

Jin Taekyung exposes Michael Silbert’s ability to absorb monsters’ magical power while concealing and balancing it with mana. Michael reveals his monstrous transformation and immense power, then turns many Hunters against Jin by threatening to expose their secrets. Jin and his allies engage Michael’s supporters while Jin confronts Michael directly.

Their fight rages across the National Assembly. Jin redirects Michael’s power away from nearby fighters, then uses martial arts, the Inventory, and Fire Dragon Armor to badly wound him. Michael’s absorbed power has repeatedly fallen out of balance with his mana; he had considered becoming a new Demon King if he could not reach the human pinnacle. Jin rejects surrendering the world to him and resolves to kill him.

As Jin raises White Flame over the wounded Michael, he turns on the S-rank Hunters still fighting for their own interests and kills Fernando Lucas and two others. Their resistance buys Michael time to transform into a dragon-like monster with immense magical power and regeneration. Jin and Michael clash again, ending in a blinding flash; the outcome is unknown.

## Continuity

- Michael Silbert has transformed into a dragon-like monster with enormous magical power and regeneration. His clash with Jin at the National Assembly is unresolved.
- Jin has a bleeding thigh wound, and his Fire Dragon Armor has lost durability. Other fighters remain engaged nearby.
- Michael can absorb monsters’ magical power while containing it alongside mana. He says the power repeatedly fell out of balance and that he considered becoming a new Demon King if he could not reach the human pinnacle.
- Michael says Cheon Taemin once frightened him; Taemin remains in a coma and is absent from the battle.
- Michael’s former supporters were pressured by his threats to expose their secrets; nearly half lowered their weapons before Jin’s allies attacked.
- Some National Assembly cameras remain operational, but the confrontation is not being broadcast. The location of Michael’s pet crow and the reason for the silence outside remain unclear.

## Translation Decisions

- Keep **magical power** distinct from **mana**.
- Render **Skeleton King** consistently; preserve **Stone King** where used in the preceding block.
- Render **용족** as **dragonkin** and **드래곤** as **Dragon**.
- Render **사량발천근** as **Four Ounces Deflecting a Thousand Catties** and **천근추** as **Thousand-Catty Drop**.

## Durable state

{
  "active_continuity": [
    "Michael Silbert has transformed into a dragon-like monster with enormous magical power and regeneration; his clash with Jin Taekyung ends in a blinding flash, with the result unknown.",
    "Jin Taekyung has a bleeding thigh wound and damaged Fire Dragon Armor; the battle at the National Assembly is unresolved."
  ],
  "continuity_sources": [
    784
  ],
  "open_questions": [
    "What was the outcome of the clash between Jin Taekyung and Michael Silbert?",
    "What is the full extent and nature of Michael Silbert’s transformation?"
  ],
  "safe_through": 784,
  "temporary_decisions": [
    "Keep magical power distinct from mana."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 780

# Chapter 780

The world was full of incidents and all the possibilities that followed from them.

The problem was that none of those possibilities was certain.

No matter how far civilization advanced, no matter how cutting-edge science reached into realms once beyond its grasp, there was no such thing as a perfect, one-hundred-percent certainty.

And that was all the more true when it came to people, rather than machines.

But at this very moment—

“Has the wound on your neck healed, Michael?”

Looking at those trembling gray eyes, I was certain.

The unbelievable question that had begun with the tiniest clue had finally revealed its dark shape.

At last, I’d driven him—Michael Silbert—to the edge of the cliff.

But I wiped the smile from my lips.

My disgust for the man standing before me outweighed any joy at having turned the tables.

I despised everything about the man drenched in gray.

“You filthy piece of shit.”

My voice slipped past my lips and shattered the silence.

And unlike when I’d revealed the Skeleton King’s identity, not one person in the room laughed at me this time.

No. They hadn’t fully understood what they’d just heard.

Or perhaps the truth was so far beyond anything they’d expected that they couldn’t bring themselves to accept it.

“What… what the hell does that mean?”

It was the Guild Master of Kronos. I kept my eyes fixed on Michael Silbert as I answered.

“Ask the man himself.”

In the suffocating silence, hundreds of pairs of eyes turned toward Michael Silbert.

Among them were some of his supporters who’d already known from their investigation, and others who hadn’t.

“From what I saw earlier, you were all busy kissing his ass. Guess none of you had anyone to tell you what was really going on. Well, that figures. Doesn’t it?”

Michael Silbert didn’t answer. He simply stared at me.

There were still ripples in his gray eyes, and I felt as if I could read all the thoughts that must be swirling around in his head.

But—

“Don’t strain yourself trying to figure it out. You already know, don’t you?”

Once every piece of the puzzle was in place, the answer was clear.

“Michael Silbert.”

It felt like I’d finally escaped a maze I’d been wandering through for ages.

And beyond the walls that had hemmed me in on every side, one person waited at the exit.

A gray monster who’d lingered somewhere between light and darkness, then crossed the river from which there was no return.

The last edge of the veil that had hidden his true nature—

“You…”

I let out the breath I’d been holding.

“You’re fucked now.”

* * *

Michael Silbert suddenly wondered:

When had things started going wrong? How? Where had it begun?

But no matter how hard he thought, he couldn’t find an answer.

Everything that had led to this moment had begun with one person.

And even if he did figure it out, the man in front of him would surely have found some other way to change the equation.

*Jin Taekyung.*

Another name for endless variables.

An Eastern young man who was far too young, reckless, and even frivolous to stand in his way.

But Michael Silbert could no longer deny it.

That young man wasn’t merely an obstacle to be removed. He was another wall that Michael should have broken through at all costs.

*So intense.*

The heat in those black eyes.

At the same time, the wound on the back of his neck—still branded there like a burn—throbbed with scorching pain.

Tap.

Without realizing it, Michael Silbert reached for his neck.

But when his fingertips met the cold armor that covered it all the way up to his throat, hiding the wound, a dry laugh escaped him.

Excuses? Damage control?

In a situation like this, they were meaningless. They would only make him look pathetic.

Like a single drop of water splitting a rock, a potion no bigger than his palm was enough to bring down the mountain that was Michael Silbert.

*Now that my body can no longer accept the mana in a potion, no excuse will do me any good.*

But one question remained.

How had Jin Taekyung learned the secret? What had made him willing to stab Michael with a double-edged sword riddled with danger and uncertainty?

So instead of making excuses, Michael Silbert chose to ask.

“I’ll ask you one thing. How did you find out?”

“……!”

It was a brief question directed at Jin Taekyung. But the shock it sent through the room was immense.

“What… what did you just say?”

“Guild Master…”

That was as good as an admission. And the people most shaken by it were the ones who had fervently supported Michael Silbert.

But he didn’t so much as glance at his allies, frozen like statues.

Just as Jin Taekyung had revealed the truth while people hurled accusations at him, Michael repeated himself.

“I asked how you found out.”

And the answer he received was shorter than the question.

“Siegfried Bassman.”

“Siegfried?”

“Yeah. Turns out the old man had investigated all sorts of things before he died.”

Whoosh!

A sheet of paper shot through the air like an arrow. Michael Silbert caught it between two fingers and murmured the title written at the top.

“…The Compatibility of Mana and Magical Power.”

“They say he was the greatest monster scholar of his age, even before you count his being a Grand Mage. Looks like he researched just about everything.”

“There shouldn’t have been any research material left.”

“Sure. That’s what people knew.”

Michael Silbert silently looked down at the paper in his hand.

His gray eyes moved quickly. It took him only an instant to read and understand the entire page.

“Studying the possibility of introducing a monster’s magical power into a human body and making the two coexist. That’s the kind of crazy idea only a lunatic like Siegfried Bassman could come up with. Of course…”

Jin Taekyung’s low voice rang in his ears.

“That wouldn’t have been true for you.”

Michael Silbert raised his head. The sheet, now hopelessly crumpled, caught fire in his grip.

*Fwoosh. Crumble.*

Ash drifted through the air. Beyond it, the eyes that had gone cold now held a reddish glow.

“Looks like Siegfried Bassman was curious about the same thing. But even he never managed to prove it. Or maybe he stopped researching because he thought he’d crossed a taboo.”

Jin Taekyung watched the ash as it drifted toward him and continued.

“Maybe he had his own reasons for not leaving this kind of material behind. Or maybe whoever killed him made sure it was gone. Either way, there was almost nothing left about that research. It took me quite a while to find that.”

“You think this is why I killed him?”

“At first, yeah.”

“At first?”

“Right. But you had another reason for killing Siegfried Bassman.”

“I won’t deny it. But I’d like to know why you think that.”

“It’s simple. You’re not careless enough to leave research materials like this lying around.”

After staring silently at Jin Taekyung for a moment, Michael Silbert laughed out loud.

“I appreciate that. I would’ve been disappointed if even you thought I was an idiot.”

“Don’t mention it. I just thought you were a piece of shit, not an idiot.”

“But you still haven’t given me a clear answer. This material alone wouldn’t have been nearly enough to make you suspect me.”

“No. It was enough.”

“Why?”

“When a crime happens, it’s only natural to suspect the ex-convict who lives nearby first.”

“……!”

“As I looked over what little research material was left, that thought suddenly crossed my mind.”

With a scornful sneer, Jin Taekyung turned his head.

The truth behind the Grand Mage’s death—a mystery from beginning to end—had now been revealed. The stunned crowd stood frozen, staring at the two men.

“What if Michael Silbert, that son of a bitch, really was already as good as half human and half demon? What if he’d already made that absurd research a reality?”

In the utter silence, Jin Taekyung recalled the moment the thought had first come to him.

Before hundreds of watching eyes and ears. On a stage someone other than him had planned meticulously from beginning to end.

He spoke like a leading man standing alone in the spotlight.

“And then… finally, all the pieces fell into place.”

That hypothesis no one else could have thought of was the last piece needed to complete this complicated puzzle.

Why Michael Silbert had realized the Skeleton King’s true identity.

Why a man who’d been just one hero among hundreds during the Great Cataclysm had risen from the dragon’s tail to its head.

Why the Odin Guild had begun to grow around the time Cheon Taemin disappeared, and why Michael hadn’t shown his face even at Lee Jungryong’s funeral, attended by prominent figures from around the world.

There was only one reason.

“Magical power.”

Jin Taekyung slowly turned around. Looking into the gray eyes that no longer wavered, he continued.

“I don’t know how you did it or what gave you the chance, but… you were able to grow stronger by absorbing magical power. Just like a monster.”

At the same time, he’d contained mana within himself, perfectly controlled the balance between the two forces, and concealed them. That was why no one had been able to uncover what he really was.

Not even the Skeleton King.

Whenever the Skeleton King talked about Michael Silbert, he’d call him an “unpleasant human.” Even he, a monster, hadn’t been able to define exactly what made Michael so unpleasant.

If there was anyone in the world Michael Silbert feared more than anyone else, anyone whose eyes he had to avoid at all costs, it was just one person.

“Cheon Taemin. He would’ve seen right through you.”

And at the moment Jin Taekyung’s low voice reached everyone’s ears, someone’s dry lips parted, breaking the long silence.

“That’s why I had to live in hiding for so long. For nearly as long as you’ve been alive.”

More than thirty years had passed, but Michael Silbert still remembered it vividly.

It had been not long after he’d gained his new power.

Among the many people gathered in one place, the absolute being’s gaze had fixed on him—precisely on him. He still remembered the fear that had seized his entire body in that moment.

Back then, he’d possessed so little magical power that the man hadn’t looked his way again. But the fear he’d felt that day never truly went away.

Even after time had passed and Cheon Taemin had vanished. Even after Michael had learned the secrets of Zone A from Siegfried Bassman.

He hadn’t even attended Lee Jungryong’s funeral.

In case the information he had was wrong.

In case he ran into Cheon Taemin there—the one person who could see through him.

But…

“There’s one thing you’ve got wrong.”

In a low voice, Michael Silbert awakened the enormous power that lay dormant deep within him.

That unprecedented, turbulent power in which light and darkness had mingled for years—but which, from a certain day onward, had been stained a deeper and deeper shade by the swelling darkness.

“The only person in this world I fear isn’t here right now.”

*Rumble, rumble, rumble.*

A vast wave of force rose and pressed down on everything around them.
## Chapter artifact 781

# Chapter 781

*Rumble, rumble, rumble!*

A roar shook everything around us.

At the same time, a murky energy, light and darkness mixed together, poured out, swallowed the room, and hung over everyone’s heads.

Dark.

It was far too early for the sun to have set, yet the National Assembly building had already entered the first page of night.

A night without a bright moon or stars scattered across the sky.

And yet, in the haze—fainter than moonlight—someone radiated a presence clearer than anything else.

*Step. Step.*

The flow of air changed with each slow step he took.

No, it wasn’t only the air that had changed.

His gray eyes were slowly turning black, like ink spreading through water.

The characteristically pale skin of a white man was covered in a thin membrane like leather, and his entire body—now longer and thicker—seemed to radiate strength and elasticity unlike anything he’d shown before.

As if…

*He wasn’t human.*

And yet, he wasn’t a monster, either.

The immense energy pouring from his body clearly held mana within it.

So what should I call that bastard—Michael Silbert?

His slow footsteps finally stopped.

My face, twisted with contempt, was reflected in his eyes, where darkness rippled.

“You monster of a bastard.”

I probably wasn’t the only one thinking that.

Shock spread across hundreds of faces.

The best of the best from countries all around the world had gathered here, but no one dared to speak or move.

Every one of them had reached a high realm. They could feel just how vast—and terrifyingly powerful—the aura Michael Silbert was giving off.

And with it, they understood the true meaning of what he’d said earlier.

*The only person I fear isn’t here right now.*

Even I had to admit it, at least to myself.

Michael Silbert hadn’t been arrogant after all.

No matter how vile and impure the source of his power was, its sheer scale was beyond anything I’d faced before.

*If I had to name one person, it would be the Southern Heaven Demon Empress.*

But the two were alike in one way and clearly different in another.

The Southern Heaven Demon Empress was constantly supplied with magical power flowing from the rift.

Michael Silbert, on the other hand, had found a way to make magical power coexist with mana—and had made it entirely his own.

*Just how much magical power has he absorbed?*

I fixed my eyes on Michael Silbert, my gaze sinking deep.

Something that was no longer human, but wasn’t a monster, either.

A monster that had spent decades building up its power while evading the notice of an absolute being stood before me.

Now, he was revealing every last bit of the strength he’d kept hidden.

With a predator’s smile, he looked at me and everyone else before finally opening his tightly closed lips.

“I told you. As long as he’s not here, there’s no one left who can stop me.”

The air had frozen cold. Eyes wavered around the room.

But not everyone here was overwhelmed by Michael Silbert’s aura.

“You’ve gotten a lot better at joking since I last saw you, Michael.”

*Whoooosh.*

A gust of wind suddenly swept through from somewhere.

No—it wasn’t wind. It was so much mana that it felt like one.

Dense smoke billowed behind Magic Johnson, who had slung his staff over his shoulder like a steel pipe.

*Crackle.*

The last stub of his cigar was crushed beneath a military boot. Chuck Hagel spat out a glob of phlegm, pretending the nicotine had brought him back to life.

Flames streamed from his eyes as he glared at Michael Silbert.

“Say that again. Go on, you damned neo-Nazi bastard.”

And he wasn’t the only one.

Faye Chen had already drawn her bow, and Prince Felix unsheathed an ornate longsword set with brilliant jewels, his bearing full of dignity.

Team Leader Choi, however, did something different.

*Shing.*

At last, the [Hero’s Sword] slid free of its scabbard. He handed it to someone else.

With a brief remark.

“Please take it. It suits you better than it does me.”

The recipient blinked at this unexpected gesture of goodwill, then nodded in thanks.

He silently looked at the sword in his hands before suddenly speaking.

“I’ve been meaning to say this for a while…”

The Skeleton King.

The King of the Dead continued, staring at Michael Silbert.

“From the moment I first met you, I’ve never liked you.”

*Kiiing.*

A golden line crossed the Skeleton King’s pure-white forehead, tracing out a crown.

At the same time, a chilling aura at odds with that brilliant light flowed through his body. But this time, no one raised a weapon against him.

Now that the truth was out, it was clear who their enemy was.

*Shhhhh.*

Weapons and dazzling radiance aimed at Michael Silbert, cutting through the murky darkness.

But the smile on his face remained.

No—he spoke with a smile that had grown even broader and brighter.

“Oh, Fabian. You too?”

“……!”

The Guild Master of Kronos, unexpectedly called by name, clenched his jaw.

His eyelids trembled, and the blade in his hand wavered.

Michael Silbert burst into hearty laughter at his obvious agitation, then turned to the others.

“Christopher, Fernando, Joanne, Marcel, Khalid…”

The names of powerful figures spilled from his lips, one after another.

The sparks that flew from Michael Silbert’s mouth spread from the Guild Master of Kronos to people throughout the room.

Every one of them was either the head of a major Guild or an S-rank Hunter, yet they froze like statues just from hearing their names.

Race, nationality, gender, age.

They were all different, but they shared one thing.

Until just a moment ago, they’d been Michael Silbert’s supporters.

And the relationships they’d built up over so many years were complex and heavy beyond anyone’s imagining.

“Even the shortest of our relationships goes back more than ten years. You all feel like old acquaintances to me. Don’t I to you?”

No answer came from anywhere. Michael Silbert smiled at those frozen in place.

“If this is what you’ve chosen, I won’t stop you… but think it over once more. Think about the trust and friendship we’ve shared all these years.”

I could feel an invisible tremor of unease and confusion spreading.

This wasn’t simply an appeal to their affection.

Michael Silbert was pressuring the people who’d turned their backs on him.

Behind the words *trust* and *friendship* lurked a shadow: the ugly secrets only those involved knew, which Michael was using as leverage.

The spark Michael Silbert had tossed into the room soon blazed into a fire, feeding on the fear and anxiety hidden deep in their hearts.

Then he spoke again, making them forget even the little conscience they had left.

“If the whole truth came out, do you think you’d be safe?”

“……!”

“But you needn’t worry. History is the spoils of the victor, after all.”

Michael Silbert slowly turned his head to look at me and added,

“And not just history. The whole world.”

That was the finishing blow.

And just as Fabian, the Guild Master of Kronos, led nearly half the Hunters in the room in lowering their weapons—

A voice, strange and cold, as if it belonged to someone else, slipped from my lips.

“Yeah. I should thank you, actually. For coming out like this, at least.”

“What?”

The confusion that crossed Michael Silbert’s face didn’t last long.

No—in almost the same instant, someone’s scream erupted and swallowed his voice.

“Argh!”

“Urgh!”

*Slash! Splatter!*

Fountains of blood shot up between overlapping screams.

The ambush began all around us the instant the weapons came down. The Guild Master of Kronos realized what was happening a moment too late and shouted,

“You fucking—!”

“I regret it too, Fabian. I didn’t want things to turn out this way.”

Magic Johnson had already risen into the air. He answered coolly as he gripped his staff.

*Vmmmm.*

The air trembled.

Along with a massive flow of mana, fire and ice filled the sky, then plunged toward the ground like streaks of light.

They were aimed at the traitors who’d once been his comrades-in-arms.

*Whoosh! Thud-thud-thud!*

“St—urgh!”

Three or four A-rank Hunters, relatively weaker than the others, dropped to their knees with dying groans.

Meanwhile, the Guild Master of Kronos, who had been about to hurl his weapon at Magic Johnson in midair, found himself facing a new guest.

“You’ve gone completely off the rails since I last saw you. Why’d you make such a stupid choice, Fabian, you dumb son of a bitch?”

The grimy military boots. The acrid scent of cigars wafting from his entire body.

The Guild Master of Kronos clenched his jaw as he faced the white man, well past middle age and nearing old age.

“Chuck Hagel.”

He was no easy opponent.

No—he was dangerous.

The Guild Master looked back, hoping for help from his allies, but that hope was in vain.

Just a few steps away, the S-rank Hunters who’d turned to Michael Silbert’s side with him were struggling against other enemies.

Faye Chen, Prince Felix, the Skeleton King—who was already raising the dead Hunters and sending them charging—and Choi Minwoo.

There wasn’t a hint of hesitation in their swift movements.

“You bastards… You planned this from the start?”

“Once you start, you have to pull it up by the roots.”

With a ferocious laugh, Chuck Hagel charged at the Guild Master of Kronos.

*Bang!*

The air burst with their collision.

But the next moment, more crashes and screams surged in from every direction like waves, drowning it out. Red blood sprayed into the air.

Right. The enemies’ blood was red.

Human blood, not monster blood.

The sight of that red blood—the one I’d hoped never to see in the world where I was born and raised—was soaking the National Assembly building and the enormous round table.

Maybe that was why, even though I’d expected things to turn out this way, my mouth tasted so bitter and my blood boiled through my whole body.

*Fwoosh.*

The fire dragon coiled in my dantian surged up.

As I felt a heat like molten lava seep through every part of my body, I suddenly spoke.

“Hell of a shitty sight, isn’t it?”

Ignoring everything unfolding right before him, Michael Silbert had been silently watching me. Instead of answering, he asked,

“Are you telling me everything happening right now is by your design?”

“What if it was?”

“I applaud your decisive action.”

*Decisive action.*

The words pierced something in my chest like an awl.

But I kept that to myself and answered calmly.

“Then don’t just flap your gums. Clap your hands, you dumbass.”

“Sorry, but I can’t do that.”

“Why not?”

“Because if I let my guard down even a little around you, I have a feeling something will happen. Of course…”

Michael Silbert’s smile faded as he continued.

“But that won’t happen.”

“Maybe. You sure about that?”

And just as silence fell for a moment—

*Whoosh.*

All the space between us vanished, and two immense forces shot toward each other.

*Kwaaaang!*
## Chapter artifact 782

# Chapter 782

*Kwaaaang!*

My ears went numb beneath the deafening crash.

But before the ringing came, an enormous shock wave traveled through our hands, which had touched for only an instant.

*Boom!*

It felt as if a giant’s palm had smacked my entire body.

The irresistible force sent me flying backward. I twisted in midair, and a blade of gray energy came rushing toward my face.

*Shhk!*

A hair’s breadth. That was all.

I snapped my head aside, and the gray energy skimmed past the tip of my nose, cleaving the ground like soft tofu. I landed lightly on the spot it had cut through.

Then I watched one man walk toward me, his entire body wrapped in gray energy.

No—something that had crossed beyond the bounds of humanity.

“Michael Silbert.”

He smiled at the sound of my voice. The shadow in his deep-set dimples seemed especially dark. That wasn’t just my imagination.

*Crack. Crack.*

The ground crumbled beneath each step he took.

The energy pouring from Michael Silbert was so overwhelming that even those fighting nearby choked on their breath and retreated as far as they could.

But not me.

I couldn’t back down. And I had no intention of doing so.

Just as I’d decided before coming here, all I could do was fight back.

To stop that leisurely approaching monster. To keep him from hurling billions of people into the flames all over again.

I stepped forward, putting my weight into it.

*Whoosh.*

One step.

The wind brushed past my body, and space folded. At the same time, two keywords completed themselves in my mind and became commands.

*Inventory open. Summon.*

A spear I’d hidden where no one could see it wrapped itself in my hand.

The world had slowed. Blue-white flames surged up along the spearhead, painting the gray eyes where darkness rippled as I brought it down.

Michael Silbert.

Straight for the crown of that monster’s head.

*Fwoosh!*

Every trace of moisture within several meters evaporated beneath the concentrated heat.

Through air hot enough to catch fire at a touch, I saw his eyes fly wide.

And the corners of his mouth were still turned up, even in the face of an attack no one here could have expected.

Then—

A sword shot upward like a streak of light and smashed into the White Flame spearhead falling toward his crown.

*Kwaang!*

A deafening crash rang out, as if the sky itself had split open.

*Grrrrk.*

The spearhead and sword blade locked together in midair, neither giving an inch. Beyond them came a low laugh.

“So that’s it. I wondered why I’d never seen that spear.”

“……!”

“So, are you done with the surprise magic trick you prepared?”

*Grit.*

The sword, wrapped in a murky aura, slowly pushed back the flame-wreathed spearhead.

A strength impossible to believe belonged to a human, and an unprecedented power that seemed to well up without end, burst forth all at once.

*Kwaaaah!*

The moment I faced that immense power head-on, I realized with absolute certainty:

Even the physical abilities I’d pushed far beyond their limits thanks to the System, even my three jiazi of internal energy—a level no one in Murim could afford to underestimate—weren’t enough to fully suppress him.

*If the fallout from this power reaches the people around us…*

I didn’t need to think hard about what would happen.

At least dozens would die. And half of them would be heroes who shouldn’t die here.

In the end, I had only one option left.

*Neutralize it.*

With that word flashing through my mind, I let go of the White Flame, which had been flung upward by the force of the clash, and threw out both hands without hesitation.

*Flicker. Boom!*

The Flame-Extinguishing Divine Fist with my right hand. The Flame Divine Palm with my left.

One fist and one palm.

Two branches from the same root—the Fire Gate Clan—sent two streams of flame surging into the murky aura.

*Grrrrk!*

The tremendous recoil sent throbbing pain through my body. The ground turned over beneath my sliding toes, revealing its ugly innards in long furrows.

But I focused only on the energy in front of me. I kept pouring the flames from both hands into the murky aura.

Not swallowing it—gnawing it away.

Not stopping it—throwing it out of balance.

At last, the mass of destructive energy had visibly shrunk. I twisted it with all my strength and hurled it behind me.

*Whoooosh—Kwaang!*

A tearing crash and tremor shook the National Assembly building.

The Skeleton King had just plunged his Bone Sword into the chest of one of the traitors, who’d staggered off balance. He shouted,

“Watch out!”

It was good advice, but half a beat too late.

Michael Silbert was already right in front of me.

*Shwack!*

An aura filled with murky light grazed the back of my neck.

I dodged his lightning-fast thrust and closed in, driving my fist at him without hesitation.

*Boom!*

Michael Silbert blocked my Flame-Extinguishing Divine Fist with a hand wrapped in layer upon layer of aura, then raised his knee.

No—he was about to raise it, but suddenly shoved me away and retreated.

*Whoosh! Thwack!*

A silver streak plunged viciously from the air, piercing exactly the spot where he’d stood a moment ago.

Watching me silently draw the White Flame, he smiled softly.

“Sure. If it were too easy, it wouldn’t be any fun.”

Fun. That was what he called it.

I looked around at the screams and blood splashing everywhere. A bitter laugh escaped me before I knew it.

“You crazy bastard. No matter how I look at it, you’re never going to be human again.”

“Even if I’m not human, what of it?”

“What?”

“I’ve experienced imbalances like this several times before. The stronger my magical power grew, the more it fell out of balance with my mana. There were even times I couldn’t control the magical power I absorbed from Magic Gems. But do you know what I thought of every time that happened?”

Michael Silbert didn’t wait for an answer.

Hundreds of Hunters were fighting a horrific civil war in the same room, but his expression was utterly at ease as he watched.

“Demon King.”

“……!”

“If someone kept getting in my way. If I couldn’t reach the pinnacle as a human because of them… I thought it wouldn’t be so bad to succeed Asmodeus as the new Demon King.”

I stared at Michael Silbert, at a loss for words. Then I realized I had to correct what I’d said earlier.

“……Now that I think about it, you’re not just crazy. You’re completely out of your fucking mind.”

“Call me whatever you like for now. By the time the sun sets, everything will be decided. Whether you and your friends live or die, and the name the world will know as my true one.”

The whole world already knew the name Michael Silbert.

But the “true name” he’d just mentioned meant something else.

Depending on how this fight turned out, he might become the Alliance Leader of the World Hunter Federation—or become a new Demon King.

Of course, to me, that was just something Michael Silbert had decided for himself.

“Idiot. What’s a leech like you going to do?”

“A leech?”

“Yeah, you leeching bastard.”

His face slowly stiffened. I let out a scornful laugh.

“An imugi that lives in a clear pond ascends to heaven. Ever seen a grub wriggling in a sewer turn into a dragon? No matter how strong you get, your nature stays the same. At best, you’re a mosquito or a leech.”

“……!”

“A mosquito drunk on power, with its straw stuck in a Magic Gem. A useless leech that does nothing but suck people’s blood. That’s what you are, you pathetic bastard.”

*Pathetic bastard.*

Those words were for me, too.

There’d been a time when I’d seriously considered giving up on everything and backing away.

If the end of that laughable ambition of his was just taking control of the World Hunter Federation, if his only goal was to stand at the top… then maybe no more disasters would happen.

I was in pain.

I had power and abilities that everyone wanted, yet I couldn’t save the cities crumbling into ruins or the countless people dying inside them.

It felt as if I were the one causing this terrible disaster by standing against Michael Silbert.

That was why, for a little while, I couldn’t help but wonder.

*No. I was afraid.*

Fine. I’d admit it.

I was afraid to keep running along this path, paved with countless deaths.

The closer I chased Michael Silbert, the more blood and bodies I feared I’d trample underfoot.

I thought that if I simply handed him the world, he’d stop The Prophet and every other disaster, if only to protect what had become his.

But… now I understood.

When I finally came out of the dark, endless tunnel I’d walked alone inside my heart, where no one else could see, there was the light I’d wanted so badly.

No. There was an answer.

All of it had come from my own weakness. My foolish hope was wrong, and Michael Silbert was a monster who wouldn’t stop running even after he crossed the finish line.

That was why I had to kill him as a human being.

“No matter how I look at it, the answer is still to stomp on leeches like you until they burst. Don’t you think?”

“……!”

“From now on, shut your mouth. You’re wasting oxygen.”

I leveled my spear at Michael Silbert.

His eyes had turned so black there was no trace of their original color. At the same time, an immense, seemingly endless power wrapped around his entire body and began to whirl.

*Kwaaaah.*

Everything the strands of power touched broke and split apart.

His voice, once gentle and unhurried, rang out as if it belonged to something from another world.

“Your corpse will be buried here today, along with every truth that will never come to light.”

At his words, I looked up at the cameras installed all around us.

Half had been destroyed, but the rest were still doing their job.

The truth, huh?

I could more or less guess. Why wasn’t Michael Silbert, who loved attention so much, broadcasting the brightest moment of his life to the whole world?

And where was that damned pet crow that always followed him like a shadow? Why was everything outside still so quiet despite all this chaos?

But at this moment, there was only one thing I could say to him.

“I said shut your mouth, you fucking bastard.”

“You…!”

*Grrrrrrk!*

As I charged toward his energy, surging like waves across a boundless sea, I suddenly wondered why that immense power—enough to make even my three jiazi of internal energy feel hopelessly inadequate—didn’t frighten me.

Why Michael Silbert, who’d absorbed a Magic Gem and gained physical abilities comparable to mine and a seemingly inexhaustible supply of magical power, seemed so small.

And as I thrust out the spearhead, I found the answer.

*Because I’m a Hunter.*

Hunters aren’t afraid of their prey.

*Whoooosh!*
## Chapter artifact 783

# Chapter 783

*Whoooosh!*

As I charged, the spearhead shot forward like a flash of light, cleaving through space. Flames surged up, burning the air and erasing the wind as they pierced the thick darkness.

*Boom!*

A single point, piercing the invisible flow with perfect precision.

Some of the magical power sweeping toward me like a wave dispersed helplessly. My vision plunged through the gap in the magical power at the same speed as my thrust—and a familiar face came into view.

No, perhaps it was more accurate to call it a face that was both familiar and strange.

Because the Michael Silbert standing there now was no longer Michael Silbert.

“You’re not bad.”

The moment that chilling voice reached my ears—

*Shhk.*

His figure vanished as if it had been erased.

Instead of panicking when my target disappeared from sight in an instant, I twisted around in a movement closer to instinct.

*Whoosh!*

A sword suddenly rose behind me, skimming my side and cutting through empty air.

If I hadn’t dodged, that strike would have pierced my heart. I spun around and thrust out a palm.

*Kwaang!*

He was supposed to have a body made of flesh and bone. Yet the instant our palms collided, a blast like an explosion rang out.

Along with a shock wave greater than an explosion—

*Grrrrk!*

The ground flipped over beneath my sliding toes. Unlike Michael Silbert, who stood rooted to the spot, I was pushed back several meters. He curled up the corner of his mouth.

“Do you understand now how foolish it was to stand against me?”

*Ptoo.*

Instead of answering, I spat the blood pooled in my mouth onto the ground. Before it even hit the earth, I stepped forward with all my strength.

*Kwaang!*

The ground beneath my toes shattered like an explosion.

The wind swept past my body, and the distance of more than ten meters disappeared in an instant. My spear and his sword flashed toward each other.

*Kaaang!*

The sharp clash burst the air around us. The sword had grown so long and massive that it could hardly be called a sword anymore, as if to prove the magical power overflowing from it. It drove my spearhead far aside.

*Crack.*

Pain shot through my wrist.

This wasn’t just a difference in physical ability. It came down to the sheer amount of power we held.

Michael Silbert’s body had undoubtedly grown much stronger after absorbing the Magic Gem. And with the magical power welling up without end, he could reinforce it even further. Of course I was being pushed back.

At least, as long as I insisted on a head-on fight.

*Grrrrk!*

Suddenly, I smoothly rotated the spearhead, and the sword blade slid along it.

Despite the enormous difference in force, Michael Silbert’s sword slipped free of its owner’s control. Certain that my hunch had been right, I thrust a fist at him.

*Fwoosh, whoom!*

Flames burst forth in a flash.

The thick darkness moved like a living creature and hurried to envelop its master, but my Flame-Extinguishing Divine Fist, thrown with all my strength, burned through the magical power and slammed into his chest.

*Kwaaaang!*

A deafening crash rang out, and his body shot away like a cannonball.

Michael Silbert hurriedly flung out both arms, pouring magical power at me to keep me in check. Then he coughed up blood.

*Kh-erk.*

I cut down every bolt of magical power flying toward me and watched him stagger. A strange feeling stirred in me.

Not because I’d finally landed a solid hit, but because the blood spilling from the corner of his mouth was red.

“So even a monster like you is still human—for now, anyway.”

At my mutter, Michael Silbert clenched his teeth.

But his eyes wavered. He hadn’t expected that blow.

“What the hell did you do?”

I answered readily.

“Four Ounces Deflecting a Thousand Catties.”

“What?”

“You don’t need to understand. There’s a shitload of things in this world you don’t know about anyway.”

“……!”

“So I don’t bother trying to understand, either. You, or those lunatics fighting over there—who knows what kind of fucked-up shit they got up to while working with you to end up in that fight? None of it makes any sense to me.”

I stared straight at Michael Silbert and continued.

“No. The moment I understood it, I’d become the same kind of idiot.”

A new emotion covered the traces of pain on his face.

Anger. Or humiliation.

Watching his face twist was far more satisfying than I’d expected.

“I told you earlier. A leech is still just a leech. Even if it died and came back to life, it could never become a dragon.”

“……You bastard.”

“Yeah. Whatever else, I’ll admit one thing.”

My breath was hot with heat, like that of a fire dragon. I stepped toward him and added,

“You’re the strongest leech I’ve ever met.”

With that, I launched White Flame, gripped in reverse, without hesitation.

*Bang!*

The air burst in layers, as if a sonic boom had just gone off.

And at the end of it stood Michael Silbert.

*Kwaang! Grrrrrung!*

An enormous explosion of flame and magical power.

The stained glass, which had barely held its shape thanks to dozens of layers of defensive magic, couldn’t withstand the shock wave and shattered. I flashed through the rain of countless shards falling overhead and thrust out both palms.

*Boom!*

A gale filled with flame swept through.

Amid the surroundings blurred by the explosion, the shadow of someone staggering was etched clearly into my eyes.

*That’s him.*

There was no room for doubt.

At the same time, I kicked off the ground and charged, reaching out to grab empty air.

No—two spears appeared as if drawn into existence by the command I shouted in my mind. I caught them and launched them once more.

*Shweeeek!*

Two streaks of light tore across the space between us.

When Michael Silbert twisted aside and dodged the spears, I tore through the darkness surrounding us again and closed in right in front of him.

“Jin Taekyung!”

*Whooom!*

Beyond his furious shout came the heavy whistle of a weapon cutting through the air.

Supplied with an absurd amount of magical power, the now-enormous sword swung down with the force to cleave me in two.

*Shwaaaak! Shhk!*

Space split open, and the sword, having missed its target, cleaved the ground.

At the same time, a dull pain spread from my chest. I’d dodged to the side at the last moment, but the pressure carried by the sword was far greater and sharper than I’d imagined.

A strength and speed that made my hair stand on end.

But just as he possessed an immense amount of power I could never have, I possessed something he did not.

In a fight where life and death hung in the balance, what mattered more than the size of one’s internal energy—

Was martial arts.

*Thump! Grrrrk!*

Just as he raised his sword again, I drew up my internal energy and stamped down.

I used the Thousand-Catty Drop to bear down on his sword with tremendous weight. Michael Silbert’s eyes widened.

“……!”

It was only natural, if this was his first encounter with martial arts. Even I’d been astonished day after day when I first learned true martial arts from Jeok Cheongang.

But to me, he wasn’t a Master or a Disciple. He was a monster I had to kill.

An enemy in the purest sense of the word, to whom I had no reason to offer a friendly explanation.

*Fwoosh.*

The Flame Divine Palm, brought to eight-tenths of its full power, poured out a dreadful heat.

It was already too late to pull away the hand gripping the sword hilt. When he hurriedly thrust out his other hand, I recited a command in my mind.

*Inventory open. Summon.*

*Thwack!*

What burst out wasn’t a deafening crash, but blood. Michael Silbert clenched his teeth as he saw the dagger that had pierced through his palm, magical power and all.

His eyes were so wide they seemed about to pop out. Some unknowable realization was mixed with the pain in them.

“This is……!”

Given Michael Silbert’s meticulous nature, he might already have vaguely guessed that I had an Inventory.

But I was stronger than he thought—and even better at improvising.

Even if he’d guessed, the result wouldn’t have changed much.

*The size of your internal energy is only one factor in deciding life or death.*

The powerful opponents who had fallen at my hands were my witnesses, jury, and judge all at once.

Some called me the greatest young prodigy and the Blazing Flame Divine Dragon. Others called me a lucky man who’d gained tremendous power through a sudden reawakening one day.

They were all wrong.

I’d been an F-rank Hunter, born in muddy water. I’d struggled and grown through countless brushes with death.

I would keep struggling with all my might until every bit of dirt filling this pit around me was gone. Until it finally became a clear pond.

And yet…… I couldn’t hand my pond over to some leech. Not a mantis, not a toad—a leech.

Especially not a leech that would fill that pond with blood instead of muddy water.

*Thrust, thrust-thrust!*

I swung my hand like a streak of light.

Still clutching Michael Silbert’s hand, pierced by the dagger, I summoned another weapon from my Inventory and slashed, stabbed, twisted, and drove it into him wherever I could.

“Graaah!”

Blood sprayed from his wide-open mouth. At the same time, the hand that had belatedly let go of the sword hilt drove into my side like a battering ram.

*Whoom!*

The air whistled with a weight that made my skin crawl.

My opponent was a monster with magical power equivalent to two or three S-rank monsters combined, and enough strength to tear apart a large monster with his bare hands.

Even with the System having given me a body like steel, I wouldn’t come out of it unscathed if I let that attack land.

At least, if I did nothing.

*Inventory open. Summon.*

*Crack!*

The tremendous impact jolted my upper body. The sound of bones shifting rang out, and a little blood welled into my mouth.

But that was all.

Michael Silbert’s punch, thrown with all his might, had neither split my skin nor broken my bones.

It had only damaged part of the red-tinged armor that had suddenly appeared and wrapped around my upper body.

*Beep.*

> **System**
> A part of the **Fire Dragon Armor** has been destroyed!
>
> Current damage: 44%
>
> At 90% damage or higher, it will be recalled to the Inventory and enter automatic repair mode.

As I heard the alert pierce my ears, I gave a bright smile to Michael Silbert, who had frozen in a daze.

“Mm-hmm. I can just repair it~”

“……!”

And at that very moment—

*Ptoo!*

I spat the blood pooled in my mouth into his face.

At the same time, I drove a punch into his body as he instinctively flailed, his face drenched in blood.

Like hammering a nail driven into the ground.

*Kwaang! Grrrrk!*

A heavy crash and tremor swept in all directions. The surrounding ground sank into a vast crater. Inside it, Michael Silbert lay flat on his back, blood pouring from his mouth after my Flame-Extinguishing Divine Fist struck him squarely in the chest.

“Khk, k-kergh……!”

The blood he kept coughing up pooled inside the crater.

The armor he’d been wearing had long since been smashed to pieces. His once-pale skin was stained a dark red with blood and soot.

“……You fucking idiot.”

I smiled bitterly. When I reached out, the shaft of White Flame shot toward me and wrapped itself in my hand.

And without hesitation, I raised the spearhead.

*Whoosh!*
## Chapter artifact 784

# Chapter 784

*Shwoosh!*

It was strange.

I’d only raised my spear. So where was this sharp whistle now piercing my ears coming from?

And what the hell gave those idiots the confidence to charge at me?

In that brief instant, split into even smaller fragments, I turned and brought my spearhead down.

*Whooom. Kaang!*

The pressure bursting along the spearhead knocked away a dozen or so daggers. At the same moment, two swords came slashing in from either side, aiming for my upper and lower body at once.

*Shhk, slice!*

It burned like I’d been scalded.

An alert sounded to tell me the durability of my Fire Dragon Armor had dropped, and a considerable stream of blood gushed from my thigh.

But if this was the price of fending off a surprise attack from three S-rank Hunters, it was a pretty good deal.

Even more so if I’d given as good as I got, instead of being the only one to take a hit.

*Pshaaa!*

Blood sprayed belatedly, soaking the ground. A middle-aged man and woman stared wide-eyed as they saw their comrade collapse, his chest split wide open.

“When did you—!”

“No, Fernando!”

It had all happened so quickly that I hadn’t had time to see who they were. But now that I was facing them, I recognized them all too well.

S-rank Hunters who each represented their country and stood as symbols of humanity.

Or rather, who *had*.

“Well, look who it is. I know all of you.”

At my greeting, tinged with a hollow laugh, the middle-aged pair swallowed hard.

Fernando Lucas, Brazil’s S-rank Hunter, had made the reckless choice to aim for my chest. Even as he spilled an enormous amount of blood, he was fumbling for a potion with trembling hands.

He looked so desperate that I spoke to him in a warm voice, like the male lead in a romance movie.

“Drink that, and I’ll kill you.”

“……!”

“But if you hang in there until this is all over, I’ll treat you. I’ll even make sure you get a nice prison. All right, then. Deal.”

Fernando Lucas stared at me blankly, as if he’d forgotten the pain.

Then, with lightning speed, he shoved the potion in his hand into his mouth.

Still in its bottle. Without even taking off the cap.

*Crack! Thud!*

Shattered glass and potion spilled into his open mouth.

But even the highest-grade potion, capable of restoring torn organs in the blink of an eye, couldn’t bring back someone who was already dead.

“I told you not to drink it.”

I murmured softly, looking at Fernando Lucas’s corpse, his forehead pierced by my Finger Qi. Just then, the two middle-aged Hunters beside him—slightly luckier than the man who’d gone to the next world first, and much more skilled—spoke with stiff faces.

“Did it really have to come to this?”

“It’s not too late, Jin. If you stop, we’ll withdraw. There’s no need for more sacrifices here, is there?”

Stop? No need for more sacrifices?

For a moment, I was at a loss for words. Then I looked around.

At the National Assembly, its interior still being stained red. At Michael Silbert, lying on the floor and twitching like an insect. Finally, at the two people standing before him.

Then I thrust out my spear.

One of the few lessons I’d learned by now was that you didn’t have to answer every stupid thing people said.

*Shhk!*

Even if they didn’t know martial arts, they were S-rank Hunters who’d seen more than enough combat.

With a sharp, startled gasp, the two barely evaded my attack and landed in front of and behind me.

But after the spearhead had come flying without warning, their eyes sank heavily.

“So this is your answer?”

“Wait. Don’t provoke him for no reason. Right now, we need to save Michael first—”

The woman understood the situation far better than the man did. But she was just as laughable.

*What the hell had they been doing all this time? How much had they done to bring things to this point?*

There’d been a time when I didn’t know anything, either.

A time when I’d gone mechanically back and forth between Gates and my goshiwon. A time when I fought monsters for money rather than out of a sense of duty as a Hunter, yet still felt vaguely offended whenever I heard someone say Hunters had fallen into corruption.

But…… now I knew too much.

And there was no going back.

It didn’t matter how great their achievements were, or how much strength they could contribute to the coming war.

If we didn’t cut out these tumors rooted deep in society, humanity would collapse before it even got the chance to fight the monsters.

Right before my eyes stood another Lee Jungryong, another Go Jun, another Michael Silbert.

The moment they turned their weapons against us despite the ugly truth having been exposed, they became tumors that had to be cut out.

“I already gave you a chance. The choice…… was yours.”

I charged without hesitation toward the people who’d once been the objects of my admiration and respect.

*Shweeeek!*


* * *


It was ironic. Pain itself was what tormented people, and yet they couldn’t feel it when death was near.

And…… that numbness was more frightening than any terrible pain.

*Ah.*

Michael Silbert blinked blankly.

His lips were slightly parted, but he couldn’t even groan. The strength was draining from his arms and legs, from which powerful energy had surged without pause. The blood that had soaked his body and was now sloshing around him felt dull and distant.

*Damn it.*

If he was going to fall like this, what had his life been for?

*Grrk. Cough.*

Instead of a hollow laugh, a bloody bubble welled in his mouth. His head tipped to the side as if he were collapsing, and he saw the corpse of a man frozen with his eyes wide open.

A familiar face.

Fernando Lucas.

He’d been a delinquent who belonged to a Brazilian gang from childhood, and he had the enthusiastic support of South America’s lower classes. Over the past ten years, Michael Silbert had done him various “favors.”

The public and the courts would, of course, interpret those “favors” differently.

*It started out small.*

But everything dulled with time, and each repetition made it grow like a snowball.

He’d eliminated a powerful rival and made it look like an accidental death. He’d used a politician with connections to him to bury tax-evasion charges. And once, he’d kidnapped a brave journalist along with his family when the journalist was preparing an article about how the hero of Brazil’s lower classes secretly ran a gang and made a fortune on the side.

The others now spilling blood and dying for him in every corner were no different.

*No. They weren’t doing this for me.*

Michael Silbert knew.

They were fighting for themselves.

They knew there was too much to lose if they admitted and accepted everything now.

In the end, he and the others had been no more than filth wallowing together in the same pit.

But thanks to that—thanks to how long he’d indulged their greed and ambition—Michael Silbert had bought himself a little time.

Precious time to cast off the bonds of humanity that he’d clung to until the end, and become something known as the Demon King.

*Slosh. Splash.*

The blood that had filled the crater rippled like a wave. Through his blurred vision, he saw a spearhead flash through the air and graze the neck of a middle-aged man.

*Slice!*

A body fell with a wet thud, and a head rolled over to meet his gaze.

The smell of blood wafting from the charred-black cross-section seemed as sweet as chocolate. That wasn’t merely his imagination.

*Heh-heh.*

Michael Silbert laughed softly. At last, he could laugh aloud, and his five senses slowly grew clear.

The sound of his heartbeat seemed to thunder in his ears.

*Thump. Thump-thump. Thump-thump-thump!*

As his heart pounded faster, the blood pooled in the crater rushed toward its owner’s body.

But it wasn’t red anymore.

It was a thick, gleaming green—the blood of something no one could call human.

The same blood as that of the unprecedented monster he’d encountered in Paris, more than thirty years ago, when the city had overflowed with blood and corpses, now filled Michael Silbert from head to toe.

Along with its endless magical power and Regeneration.

*Shhhh!*

The blood was sucked deep into his body. Severed muscles rejoined. Broken bones and ruined organs mended.

A short scream rang out, as if to celebrate his return to life from the brink of death.

“Kh-erk!”

It was a victory cry announcing the resurrection of one life—and a death rattle announcing the end of another.

A middle-aged woman staggered backward, her chest pierced through.

Like the filth in the pit Michael Silbert had chosen, she’d built up a splendid record of achievements as a hero of the Great Cataclysm. Even on the brink of death, she drove a dagger into a gap in his damaged armor. Her back arched like a bow.

*Crunch. Pshaaa!*

Blood spurted as the spearhead came free.

*Thump.*

In front of the corpse that had crumpled like a rotten log stood a young man, tall as an iron tower. Michael Silbert saw him.

—Jin Taekyung.

Michael Silbert looked at Jin Taekyung. Or rather, Jin Taekyung looked at Michael Silbert.

At him, with black eyes swallowed by absolute darkness—not the gray of before, not even the whites of his eyes remaining.

And…… at the monster spreading enormous wings made of magical power.

*Whooosh!*

The National Assembly, spanning hundreds of meters across, fell silent for a moment, along with the fierce battlefield that had been nearing its end.

Everyone was horrified. Everyone fell silent.

At the sight of Michael Silbert, who had completely lost the form of a human being.

At the scales covering his body, the two horns that had pierced through his forehead, and the name of a monster that flashed into their minds at the sight of the enormous wings resembling darkness.

A voice that sounded like a groan slipped between someone’s lips.

“……Dragon.”

The root and very embodiment of the dragonkin, a race born with nightmare-like power.

A monster of the highest order—the oldest and most evil—with magical power that never ran dry, strength that could tear apart heaven and earth, and tremendous Regeneration.

And people suddenly remembered something they’d forgotten.

During the great battle in Paris more than thirty years ago, the battle that made Michael Silbert who he was, it had been a young dragon—not even fully grown yet—that swallowed up a thousand lives, including those of four S-rank Hunters.

And the Dragon Heart that creature must have possessed had never been found anywhere.

—Yes. Do you understand now?

Michael Silbert laughed loudly.

His roar shook the entire National Assembly, and the faces of several people seized by Fear turned deathly pale.

But not one man’s.

*Whoooom.*

Jin Taekyung watched the dreadful mass of energy gathering around the two horns that had sprouted from Michael Silbert’s forehead. Even as he watched the Breath, he wasn’t flustered.

He merely looked on for a moment before tossing out a single word like a sigh.

“Fuck, you bastard. I’m already feeling like shit as it is……”

And then, the next moment—

*Whooosh!*

An immense darkness poured down, staining the whole world, and collided with the blue-white flames swirling along the spearhead.

*Gooooong.*

At the end of it all, there was a blinding flash.

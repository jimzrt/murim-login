# Checkpoint Review — 790–794

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

# Chapters 790–794

## Plot

The Main Quest [Cataclysm] reveals its true target: eliminate The Prophet within an unspecified time limit. Jin Taekyung leads the World Hunter Federation’s multinational force into the Middle East, where The Prophet is hiding and may be preparing a catastrophic attack with a large supply of unrefined Magic Gems.

During the search, the Skeleton King and Xiao Shen find twenty members of a missing squad dead in the desert. Their bodies are desiccated like Siegfried Wassmann’s, and the Skeleton King reports that an unidentified presence appeared and vanished without a trace. After the Skeleton King defeats an attacking Monster Wave, Jin connects the deaths to Siegfried’s still-incomplete [An Unknown Death] Quest and realizes Michael Silbert was not Siegfried’s killer.

Jin interrogates the captive Huginn, who identifies The Prophet as Muninn and says Muninn killed Siegfried. Jin recognizes that Huginn and Muninn are Odin’s two ravens: there was never only one Prophet.

## Continuity

- Jin is the World Hunter Federation’s Alliance Leader, pursuing [Cataclysm], which requires him to eliminate The Prophet before an unspecified deadline. At least 100,000 Hunters have been deployed to search the Middle East.
- The Prophet is Muninn, hiding somewhere in the Middle East. Jin suspects a major attack may be imminent; Muninn has a large supply of unrefined Magic Gems.
- Huginn says Muninn killed Siegfried Wassmann. Jin believes Huginn is telling the truth. Huginn remains captive and has begun disclosing what he knows; Jin has not promised to release him.
- Jin’s Supreme Peak Quest [An Unknown Death] remains incomplete, despite learning that Muninn killed Siegfried.
- The Skeleton King and Xiao Shen remain in the Middle East. The Skeleton King defeated the desert Monster Wave without casualties; more than a thousand undead remain with him.
- Twenty people found in the desert died in the same desiccated manner as Siegfried. The cause of their deaths is unknown. The unidentified presence the Skeleton King saw disappeared without leaving a trace.
- Muninn’s relationship to Michael Silbert is unresolved.

## Translation Decisions

- Keep **magical power** distinct from **mana**.
- Render **무닌** as **Muninn**; The Prophet is Muninn.
- Keep the System Quest title as **An Unknown Death** and its Grade as **Supreme Peak**.
- Do not identify the cause of the desert deaths or the vanished presence until revealed.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and is pursuing the Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Prophet, also known as Muninn, is hiding somewhere in the Middle East; Jin suspects they are preparing a major attack.",
    "Huginn says The Prophet/Muninn killed Siegfried Wassmann, and Jin is certain Huginn is telling the truth.",
    "Huginn remains a captive and has begun disclosing what he knows about The Prophet.",
    "The Supreme Peak Quest [An Unknown Death] remains incomplete; Jin now knows The Prophet/Muninn killed Siegfried Wassmann.",
    "The Skeleton King and his undead army remain with Xiao Shen after defeating the desert Monster Wave without casualties.",
    "Twenty people were found dead in the desert in the same desiccated condition as Siegfried Wassmann; the cause remains unknown."
  ],
  "continuity_sources": [
    793,
    794
  ],
  "open_questions": [
    "What caused the deaths of Siegfried Wassmann and the twenty people in the desert?",
    "What is the relationship between Muninn and Michael Silbert?",
    "What disappeared from the desert without leaving a trace, as described by the Skeleton King?",
    "Can Jin find and eliminate The Prophet before the Main Quest’s time limit expires?"
  ],
  "safe_through": 794,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Do not identify the cause of the deaths or the vanished presence until revealed."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 790

# Chapter 790

“Where is The Prophet?”

At that single question, the smile lingering on Team Leader Choi’s lips faded.

Not *What happened to him?* but *Where is he?*

A man with a keen mind, he immediately grasped the simple but clear distinction. And I already knew what the brief silence meant.

“So you still haven’t found him.”

Team Leader Choi, who’d been watching me with a grave expression, nodded.

“That’s right.”

“You haven’t even uncovered his location?”

Team Leader Choi didn’t answer. Silence was as good as a yes.

*Damn it.*

I swallowed the curse that threatened to escape and looked up at the night sky.

Just because you’re in the same place doesn’t mean you’re all looking in the same direction.

Just like Team Leader Choi and I were looking at different scenery at that very moment.

> **System**
>
> **Quest**
>
> **Cataclysm**
>
> A new era has drawn near, and the final word of this long and fierce story has yet to be written.
>
> Hope. Or despair.
>
> And at this very moment, you are the only one holding the pen.
>
> May good fortune in battle be with you.
>
> **Grade:** Main Quest
>
> **Restriction:** Jin Taekyung
>
> **Mission:** ???
>
> **Reward:** ???
>
> **Failure:** ???

I stared at the holographic window covered in question marks and muttered to myself.

*The Quest still hasn’t been completed…*

It could only mean one thing.

The being represented by those question marks in the Quest window had never been Michael Silbert in the first place.

*Why? Why the hell?*

Even I hadn’t seen this coming.

I’d firmly believed that eliminating Michael Silbert was the only key to completing this Quest and resolving the new Cataclysm.

But I’d been wrong. Completely wrong.

*The Prophet.*

That deranged fanatic who called himself God’s messenger and a prophet—the terrorist I’d thought was merely a lackey following Michael Silbert’s orders—was the real key to this Main Quest.

Or…

He was the starting point of the Cataclysm soon to come.

*Ding.*

> **System**
>
> Information for the Main Quest, **Cataclysm**, has been updated.
>
> The mission has changed in accordance with your realization.
>
> **Mission:** Eliminate **The Prophet** within the time limit (Incomplete).

New holographic windows filled my vision with a sudden notification.

At the same time, I realized:

The clock on the bomb called the Cataclysm, the one that would soon shake the world, was ticking even now.

* * *

These days, even the term “global village” had become outdated.

Countless issues arose around the world every single day—too many to keep track of.

But even people accustomed to seeing all kinds of news on TV and the internet, then promptly forgetting it, had been shaken to the core by what happened a week ago.

Like land mines detonating, armed crackdowns and arrests had begun in countries all over the world, carried out by Hunters.

Among those arrested were high-ranking politicians, including presidents, some of the wealthiest people in the world, and Hunters.

Every one of them was a heavyweight with influence over global politics, business, and security—not merely a particular region or country.

People who’d been waiting only for the new World Hunter Federation’s inaugural ceremony were thrown into confusion. Before long, that confusion turned to shock.

> “All the truth is in here.”

In Choi Minwoo’s hand as he stood before the cameras in his role as interim spokesperson was a microchip smaller than a fingernail.

Of all the many cameras installed throughout the National Assembly to capture a moment in history, it was the only one to survive the aftermath of the tremendous battle.

At the same time, it was a Pandora’s box containing a truth no one could bear to face.

The footage ran a little over three hours.

But once it was uploaded to a streaming site where the whole world could watch, it plunged the world into a pit of silence.

Choi Minwoo had been telling the truth. It contained all the truth.

Not a single edit. Not a single lie.

Only facts, plain and undeniable.

Billions of people were confronted with an unbelievable truth—and, within the Pandora’s box that had suddenly opened, they discovered something still left inside.

It was hope.

> One thing’s for sure. I’d trust them with the lives of my family.
>
> └ Agreed.
>
> └ Real heroes. Real Hunters.
>
> └ Yeah. And Jin’s the greatest hero of them all.
>
> └ Damn it. What kind of idiot talked shit about that young savior?
>
> └ Hate to admit it, but I did until recently. But I have to admit I was an idiot. Call me a fucking moron and I couldn’t argue.
>
> └ You bald piece of shit.
>
> └ Leave the bald part out before I put a bullet in your head.
>
> └ Fine, you fucking moron.
>
> └ God bless you.

> I’ve decided. I’m naming my unborn child Sibal.[^1] It’s a great name, taken from Jin Taekyung’s nickname.
>
> └ A Korean passing by here with some advice: that’s not a very good choice.

[^1]: “Sibal” sounds like *ssibal*, a common Korean profanity roughly equivalent to “fuck.”

> Wait. Am I the only one who knows that fucking monster’s out there? Why is everyone silent?
>
> └ If you’re talking about the Stone King, stop trying to derail the conversation and get lost.
>
> └ You’re insane. He’s a monster.
>
> └ Oh. So?
>
> └ Listen. My cousin was shot and killed by a Black man, but I don’t treat my Black friends like murderers.
>
> └ Michael Silbert killed countless people. The Stone King fought for them. So, which one’s the hero and which one’s the monster?
>
> └ Shit. The world’s going to end because of morons like you.
>
> └ Great. You done talking? Now get lost.
>
> └ Goodbye, idiot.

> I’m French, and at first I thought there’d been a terrorist attack or something. I was looking at social media when a video popped up of the president falling out of a window at the Élysée Palace.
>
> └ Emmanuel? He deserved to die. The bastard was in bed with Michael Silbert.
>
> └ Did you see the video of the Swiss interior minister getting arrested? Magic Johnson was beating him with that big, beautiful staff of his.
>
> └ OMG……
>
> └ Buddy. It’s not what you think. Don’t let your imagination run wild.
>
> └ It was a swift and brilliant operation. The World Hunter Federation had its ranks in order in just an hour, then rooted out the traitors planted all over the world. They didn’t have time to run or fight back.
>
> └ They kept the operation completely secret right up until it began, too. If this had been Mexico or Brazil, the information probably would’ve leaked through the gangs.

> We support you and love you. May God watch over you all.
>
> └ It’s too soon to relax. Nobody’s forgotten about the fanatical terrorist, right?
>
> └ Of course we remember. But the World Hunter Federation will protect us. That lunatic who calls himself The Prophet is keeping his head down and watching what happens.
>
> └ It’s already been two weeks since the terrorist attacks stopped. The Prophet will die soon, just like bin Laden, and then real peace will finally come.
>
> └ Jin. Please wake up soon. We’re waiting for our hero.

A week was nowhere near enough time for the whole world to recover from the shock.

Even so, humanity was quickly finding its footing again.

They had faith in the World Hunter Federation, and hope that things would get better.

But somewhere beyond their sight, a new movement had already begun.

Or perhaps it was a blaze that would devour the world.

“Concentrate every force we can mobilize in the Middle East. Now.”

Jin Taekyung’s words were relayed straight to the World Hunter Federation’s leadership through Choi Minwoo. No one questioned them.

This wasn’t a request. It was an order.

The first order from the Alliance Leader they had chosen.

And they’d known from the start what their answer would be.

“Yes, boss.”

The World Hunter Federation began to move.

* * *

“They’re coming.”

A trembling voice rang through the cave.

The Prophet silently looked down at the man prostrate at their feet, then spoke.

“What is their estimated strength?”

“Th-that is…”

“Answer.”

The hesitant man lowered his head to the floor.

“At least a hundred thousand.”

“……!”

“……!”

A hundred thousand.

The staggering number, far beyond their expectations, froze the already chilly air in the cave.

Those gathered here knew that the number didn’t mean an ordinary infantry force.

*The World Hunter Federation.*

Hunters were rare, regardless of their Grade.

Only one in a thousand had the chance to awaken, and even then, they had to undergo specific training before they could be recognized as a Hunter.

But their opponents were the World Hunter Federation.

As its name implied, it was a vast organization to which every Hunter in the world belonged. Out of humanity’s billions, millions of Hunters who’d beaten the 0.1 percent odds and been chosen by God were charging toward the desert.

No—the whole world was coming.

“The entire desert is under surveillance.”

“We’ve lost contact with our informants planted in the Pentagon.”

“The residents of nearby villages and small towns are being evacuated.”

“We have reports that the United States has moved an aircraft carrier…”

Their growing anxiety spilled out in their voices. For a long while, they poured out the information they’d managed to gather.

The situation was already hurtling toward its worst possible outcome.

A week ago, Michael Silbert’s unexpected death had marked the beginning of their downfall.

The newly born World Hunter Federation was truly bold, moving without hesitation. It had begun by bathing its inaugural ceremony in blood, then set about reaping the seeds Michael Silbert had sown. By revealing the whole truth without the slightest omission, it had won support from across the world.

Pure goodwill.

Nothing could stand against the hammer the World Hunter Federation had brought down. A president of a nation, the head of a massive corporation that could sway the world’s stock markets—every one of them had fallen, bleeding.

Half a century ago, after Osama bin Laden’s terrorist attack, Pakistan and the Middle Eastern countries that had refused to let the United States fly through their airspace would not dare oppose this action either.

They couldn’t do something as insane as making enemies of the World Hunter Federation—and the entire world.

They’d be met with countless artillery shells and a visit from countless Hunters.

But unlike those who could choose compromise, the people gathered in this cave hadn’t been given even the slightest choice.

“Prophet!”

“Please, please show us the way we must go!”

Desperate cries rang out from every corner.

Armed with fanaticism, they all knelt and prostrated themselves before one person alone.

They were afraid of the enemy closing in, but at the same time, their faith in the path they’d walked until now was unshaken.

They had devoted their lives to God and followed the prophet He had sent.

They had witnessed the Prophet’s astounding miracles.

“Teach these lost servants!”

“Defeat these infidels and proclaim God’s will to the whole world!”

*Fwoosh. Fwoosh.*

The torches lighting the cave flickered in the wind. From beneath the deeply drawn hood of a robe, the Prophet’s voice rang out—impossible to place by age or gender.

“As you wish, I shall carry out God’s will and punish them. Inshallah.”

“O-oh…!”

“God is great!”

“Inshallah. Inshallah!”

The anxiety that had threatened to burst turned to cheers. As the Prophet watched them repeatedly bow and cry out about God’s greatness, they thought:

Their long wait would soon bear fruit.
## Chapter artifact 791

# Chapter 791

As far as I knew, the Middle East played a bigger role in the world than most people realized.

It covered a vast area, from Western Asia in the narrow sense to the countries of North Africa in the broadest.

And since the Great Cataclysm, active resettlement policies had pushed the population living in the Middle East past a staggering three hundred million.

That wasn’t all.

The oil fields that had sustained the region were still doing their part, and the Gates scattered throughout the area provided Magic Gems—a resource that had rapidly overtaken oil in importance.

*Of course, half the Magic Gems obtained that way probably disappear through back channels.*

That was just how things worked around there.

There weren’t any powerful civic groups or government departments capable of digging into corruption, so even when money came in, it leaked right back out.

In the Middle East, royal families held wealth and power without limit. Terrorist groups operated openly, and hypocrites who began as revolutionary leaders had evolved into dictators.

To them, the law was nothing more than gum they could spit out whenever they’d sucked all the flavor from it.

*Michael Silbert knew exactly how to exploit that.*

Smuggling in Magic Gems and leaving them unrefined were grave crimes explicitly covered by international law, but there were plenty of loopholes.

Especially in the Middle East and Africa, where terrorist groups and rebels were everywhere.

But a man who was already dead was no longer a problem.

It was the ones still alive…

*They’re the problem.*

*Tap.*

I set down the tablet and rubbed my eyes. Staring at text for hours had worn me out.

Or maybe it was because of those three syllables that had never left my mind.

*The Prophet.*

Thinking about someone whose face I didn’t even know, I gazed out the window.

Between the plane’s wings cutting across the cloud-choked sky and the rain pouring down, it felt as if the voice I’d heard on TV were rumbling like thunder.

> “Following God’s will, we will not stop. Starting today, we will judge and punish you.”

Who was that bastard?

Even though the voice hadn’t been altered, I couldn’t make out their gender or age. Their face was hidden, too, beneath a hood pulled down low.

*Does the fact that they hid their face so carefully mean they’re already recognizable?*

That was likely, but even that wasn’t certain. The Prophet’s existence was like the storm clouds outside the window.

“The weather’s bad.”

At the sudden voice, I kept looking out the window and answered.

“It sure is. Doesn’t look like good flying weather at all.”

“It’s not just bad. It’s the worst.”

“Think The Prophet planted a mole at the weather service?”

“What makes you think that?”

“What do you mean, what makes me think that? This is a perfect setup for an assassination.”

Team Leader Choi dropped into the seat beside me and spoke.

“I can tell you two things I know. First, the airport forecast was accurate. This is just a weather shift caused by magical power. And second, if I were The Prophet, I wouldn’t bother with something so pointless.”

“Why not?”

“Even if this plane crashed, Mr. Jin Taekyung would survive.”

“…Huh.”

“Am I wrong?”

“Who knows? I’ve never been in a plane crash before.”

Even that was a ridiculous answer. A crash from this height, in weather like this, should obviously be fatal.

Team Leader Choi had probably thought something similar to me.

He shook his head, then his gaze fell on the tablet lying on the table.

“Have you read it all?”

“Yes. Enough times to be sick of it.”

Some of the material had been added, but about half of it was already familiar to me.

Before the World Hunter Federation was founded, I’d spent several nights reading through those same documents over and over.

Since they were related to Michael Silbert, it was only natural that the information on The Prophet and the Middle East was included.

“What do you make of these materials?”

“Hard to say. I think I can tell at least three things.”

I glared at the tablet, crammed with text, and continued.

“The Middle East is damn huge, so finding The Prophet quickly will be tough—and they’re damn good at hiding.”

“Then the last one is…”

“That bastard has an enormous amount of unrefined Magic Gems.”

Right. That was the problem.

The Prophet, who’d launched indiscriminate terrorist attacks around the world, had gone quiet even after Michael Silbert’s death. The public thought they were scared and had started to relax.

But…

That only made me more uneasy.

This mood. This calm before the storm.

*They’re planning something bigger. I’m sure of it.*

A Main Quest unlike any I’d seen before, and one so important the System had named it *Cataclysm*.

That was exactly why I’d mobilized the World Hunter Federation without delay.

Even after accounting for the personnel needed to prevent further terrorist attacks and monster waves, we’d sent a full hundred thousand troops to the Middle East.

Considering that every one of them was a Hunter, that was an enormous force.

Even Korea, a Hunter powerhouse recognized around the world, couldn’t mobilize that many Hunters—not even if you ignored the level of each individual Hunter.

Some people had murmured that we were deploying far too many troops from the start, but that nonsense stopped as soon as it started.

That was how great the World Hunter Federation’s authority and power were now.

The UN General Assembly, to which nearly every country on Earth belonged, had given its approval, and all of humanity supported us.

If the United States had *called itself* the world’s police, the World Hunter Federation was recognized as such by everyone—and untouchable.

Even Russia, which had clashed at every turn with the Western powers led by the United States, had promised full cooperation with the Federation and sent a warning to the Middle Eastern countries showing resistance.

—If you don’t want to die, clear a path.

The diplomatic cable was long, but that was the gist of it in one line.

Furin, Russia’s president for life, was deeply aggrieved that the terrorist attack had destroyed Red Square. He’d also been itching to settle the score with several Middle Eastern countries that had sided with Michael Silbert at the recent UN General Assembly.

So, what could they do?

The Middle Eastern leaders, who hadn’t been thrilled about a hundred thousand Hunters showing up, had thrown open their airspace and territorial waters within a few hours.

International condemnation was one thing, but they could also wake up one sunny morning and find themselves drinking radioactive tea.

But just because the whole world was cooperating with the Federation didn’t mean The Prophet would fall into our hands on their own.

“How far has the search gotten?”

Team Leader Choi answered at once.

“Everyone is doing their best, but so far, no one has found anything unusual. The area is vast, and it’s only been a day since the search began.”

I knew. That was one of the biggest reasons I was heading to the Middle East now.

Even so, I couldn’t help asking again, even if it was premature.

“How long do you expect it to take?”

“In the worst case, more than sixty days. That estimate assumes we mobilize every Federation Hunter as well as all the allied forces that joined afterward.”

“…Sixty days.”

“Again, that’s only in the worst case. If we put everything we have into it, we have a good chance of shortening that time.”

Who knew? Would we, really?

I didn’t reply, but I could feel the unease stirring inside me.

*They’re not going to be easy to deal with.*

The Prophet had evaded the eyes of the entire world even before the Federation was founded.

The worst terrorist in history, far beyond the South American drug lords or even his much older predecessor, Osama bin Laden.

Some people might have thought it was amazing we could catch someone like that within two months…

But I wasn’t one of them.

*Two months is too late.*

If my guess was right, The Prophet had an enormous quantity of Magic Gems in their possession. Unrefined, and therefore all the more dangerous—a ticking time bomb.

No one knew when that bomb would go off.

A month from now. Maybe two weeks. Or…

*It could be tomorrow.*

And the day that bomb went off, it was easy enough to imagine the Cataclysm beginning, just as the Main Quest I’d been given was titled.

If that happened, a disaster on par with—no, possibly even worse than—the terrorist attacks The Prophet had carried out so far would sweep across the world.

> “It’s your turn now. Let’s see you struggle with everything you’ve got. I’ll be watching from up there.”

A voice suddenly echoed in my ears.

Now I understood.

The true meaning of the words Michael Silbert had left behind like a last will before he died.

But just as I’d sent that bastard, who’d seemed impossible to stop, plunging into the depths of hell, I was ready to fight again.

With a suspicion that was close to certainty.

*The Prophet isn’t ready yet, either.*

A hungry person has no reason to hold back when delicious food is right in front of them.

There was a good chance The Prophet hadn’t finished preparing to set off the bomb.

They were probably lying low, holding their breath so they wouldn’t be discovered before the cooking was done.

*I have to find them before that happens. No matter what.*

I muttered to myself, then looked at Team Leader Choi.

“What about the cargo? Is it behaving?”

“The cargo? Oh.”

Realizing what I meant, Team Leader Choi replied with a wry smile.

“It’s being quiet. Though it does cause trouble every now and then.”

“Keep a close eye on it. We’ve got a mountain of things to find out about The Prophet.”

“Understood.”

I nodded and turned back to the window.

In the distance, a city shone brightly in the darkness, drawing closer through the dim storm clouds.

* * *

A cold night in the desert.

A young man with an appearance that would make anyone who saw him gasp in admiration gazed up at the dark sky and murmured.

“…I think something just passed by. Was that him?”

“What?”

“Nothing. Just talking to myself. Anyway, where did we lose contact?”

Xiao Shen tilted his head at the Skeleton King’s reaction, then answered.

“About thirty kilometers farther southeast, Mr. S.”

“Mr. S… I thought I told you not to call me that.”

“Oh. Sorry, Mr. King.”

“…It still sounds strange, but for some reason, I don’t mind it.”

“Thank you!”

“Don’t get excited, you young human brat.”

He grumbled, but the Skeleton King was in a pretty good mood as he headed toward their destination—just as he’d said.

No, he was actually quite pleased.

*That little kid doesn’t mind me at all?*

Ever since his identity had been revealed, the Skeleton King had felt people’s eyes following him wherever he went.

Some watched him with wary eyes, if not outright hostility, while others smiled brightly and treated him with kindness.

Sometimes, even a certain kind of curiosity could be burdensome in itself.

For that reason, the Skeleton King had chosen to search alone. It was better that way. At least he could get away from people’s eyes for a while.

But this little brat who’d come from China had joined him without a second thought, and he’d been right by the Skeleton King’s side ever since.

*That devious human once said the only good Chink was a dead Chink, but it seems there are exceptions, even if they’re few and far between.*

Smiling to himself, the Skeleton King reached the destination with Xiao Shen.

The area was a mix of sparse woods and desert. An hour earlier, an entire squad of the search party had lost contact there.

“This the place?”

“Yes. No doubt about it, Mr. King.”

“I don’t see anything around here. Are you sure—”

At that moment.

The Skeleton King had been frowning as he surveyed the area, but his eyes suddenly flew open.

“…What’s that?”
## Chapter artifact 792

# Chapter 792

“…What is that?”

Xiao Shen turned at the words, but he couldn’t see anything strange. The Skeleton King, however, could.

Even though Magic Johnson’s illusion magic had given him a human appearance, he was fundamentally a monster.

And not just any monster—one of the highest-ranking undead.

The sensation gripping the Skeleton King at that moment was something connected to the very source of his power.

*Damn it. This is…*

There was no doubt.

The feeling was faint, but unmistakable.

Beneath a dark sky that swallowed even the moonlight, he sensed the energy of death scattering across the endless desert.

There wasn’t a single drop of blood or a corpse in sight, but the Skeleton King recognized the energy stirring his instincts from beyond the darkness: death qi.

He knew, too, what had happened to the search squad that had suddenly gone silent about an hour ago.

“Young human brat.”

“Yes?”

“Contact the main force at once. Tell them we found the search party.”

“……!”

The desert was still, without a trace of anyone. But the Skeleton King’s words were the opposite of reassuring.

Xiao Shen finally understood what was happening. His face stiffened as he nodded, and the Skeleton King started walking, following his instincts.

*Crunch. Crunch.*

Footprints pressed into the desert as grains of sand crumbled beneath them.

After about ten steps, the Skeleton King suddenly stopped and muttered under his breath.

“Whoever did this buried them deep.”

And the next moment—

*Fwoosh!*

A section of the desert, stretching out like an endless sea, surged into the air.

A vast wave of magical power poured from a single gesture, holding the sand aloft. When the twenty bodies buried beneath it came into view, the Skeleton King froze before he could stop himself.

“……!”

A recent memory—one from not so long ago—flashed through his mind like lightning.

At the same time, an ominous premonition swept over him.

*Wait. Then could it be…*

But the Skeleton King’s thoughts didn’t get far. No—they couldn’t.

*Whoosh.*

A chill wind blew from somewhere, sweeping sand through the air.

And something was mixed in with it.

The Skeleton King stared toward some distant part of the desert, swallowed in pitch-black darkness. Then he asked Xiao Shen, who still hadn’t noticed anything.

“Have you contacted the main force?”

“Yes. They replied that they’re sending the nearby support team right away…”

“How long will it take?”

“They estimate thirty minutes at most.”

“Thirty minutes. That’s a little close.”

The Skeleton King clicked his tongue.

“I’m not sure I can protect anyone.”

“……?”

“Hmm.”

He looked Xiao Shen up and down. Then, with a sigh, he said, “Listen, young human brat. I’m giving you two missions.”

“Ah, yes! I’ll do anything you ask, Teacher King.”

“Good attitude. First, take out that damned special radio of yours and contact the main force again.”

“What should I tell them?”

“Tell them to send the best people they can, as fast as they can. Not that weak support team riding in on turtles. Got it?”

Xiao Shen had no idea why collecting the bodies would require that much urgency and manpower, but he nodded without hesitation.

The person he respected most in the world was Jin Taekyung, and the Skeleton King was Jin Taekyung’s friend.

“Understood. What’s the second mission?”

But the answer that followed was so unexpected that even Xiao Shen had to ask again.

“Pick up a weapon.”

“What?”

“And protect yourself. If you don’t think you can, you can run.”

“W-wait a second.”

What was he talking about?

Xiao Shen blinked, trying to make sense of the baffling order. It didn’t take long before he understood what the Skeleton King meant.

*Rrrumble. Rrrumble.*

An unknown tremor traveled through the ground.

As the vibration grew stronger, countless grains of sand bounced up around them. Then the Skeleton King spoke, turning Xiao Shen’s dawning suspicion into certainty.

“A lot of them.”

“……!”

Xiao Shen didn’t answer.

His mouth hung open as he stared at the far-off desert horizon. In his eyes, darkness writhed like a living thing.

No—in numbers too vast to count.

*Monster Wave…!*

At the moment the words that had become humanity’s nightmare struck Xiao Shen’s mind—

*Crunch.*

The Skeleton King walked toward the rapidly approaching tide of monsters.

There was no fear or hesitation in his steps. The mighty magical power surging from him reached ever outward.

> “By the name of the King, I command you.”

His low voice echoed across the desert. It pierced the thick darkness and roused the spirits crushed beneath the weight of ages and countless grains of sand.

> “Answer the call.”

*Rrrumble!*

A quake-like tremor swept through the desert.

At their king’s call, steeped in the energy of death, spirits that had lain in deep slumber burst through the sand and rose to the surface.

*Crackle!*

Pale sand scattered through the air. In the darkness, white bones gleamed.

*Grrr.*

An Arabian leopard, its beautiful hide lost in death, stretched its limbs. Wolves and hyenas shone with green eyes as dozens of eagles soared powerfully above them, spreading wings stripped down to bone.

*Eeeee!*

Their sharp cries split the night sky. The eagles, their wings spanning several meters, glided high overhead.

They passed above the monster army charging across the ground in a storm of sand, then scattered toward the vast desert and woods. They had only one mission:

Find a certain being who wasn’t here, by the King’s command.

> “Somewhere in this desert, there’s something that carries the scent of humans. Find it. No matter what.”

The eagles beat their wings with all their strength.

They had magical power to carry them on the wind instead of feathers, and though they’d lost the life within them, their vitality would never run dry.

*Whoosh!*

From far below, the King watched the flock of eagles disappear into the distance. Remembering the human bodies he’d uncovered moments ago, he walked toward the monster army bearing down on him.

*What kind of trace was it?*

*Whoosh—BOOM!*

A massive wave of magical power burst from the Skeleton King’s outstretched fist and swallowed the monsters at the front.

At the same time, a hundred or so beasts rushed into the empty space and tore into the enemy.

*Yowww!*

*Smack!*

An orc’s upper body went flying under the swipe of a leopard’s forepaw. A pack of hyenas nimbly dodged a club crashing down from above, then sank their teeth into a troll’s body.

*Crunch!*

The numbers were hopelessly against them.

But the moment the battle began, the Skeleton King understood: absorbing some of Michael Silbert’s magical power had strengthened his own powers enough to give even these spirits—once mere wild beasts—the strength to crush ordinary monsters in an instant.

*Splatter! Rrrumble!*

*Graaaah!*

Blood and flesh flew as the living screamed.

The enemy formation began to crumble in moments.

The Skeleton King knocked the heads off three ogres with a single strike, then looked toward some dark corner of the desert.

He couldn’t see a thing, but he knew.

Whatever had killed the search party had already left this place and disappeared somewhere out in the desert.

*What the hell are you?*

The question he asked himself went unanswered. The Skeleton King stared into the darkness with sunken eyes, then raised an ogre lying like a rotten log from the dead.

No—not just the ogre. Everything around him.

> “Answer the call.”

*Fwoosh.*

A dazzling golden radiance spread in every direction, brilliant enough to be mistaken for something other than magical power.

The immortal army, now twice its former size, descended upon the living.

*BOOM!*

*Grrrrr!*

The desert was gradually buried beneath countless screams and death.

As Xiao Shen stared blankly at the sight, he remembered the task he’d temporarily forgotten.

“Base. Base, please respond.”

*Chhh.*

The radio, enchanted with communication magic, transmitted a mana-laced signal amid a burst of static.

It pushed through the unstable magical power permeating the air, farther and farther.

And when Xiao Shen’s urgent message finally reached the main force—

“Company, halt!”

An aircraft carrying someone landed smoothly among the soldiers and Hunters standing in perfect formation along the runway.

* * *

This expedition involved a hundred thousand Hunters and a coalition of nations from across the world. It was a massive operation—or, more accurately, a war.

As a result, a considerable number of Hunters remained at the main base, and soldiers were everywhere you looked.

An army made up of different nations and races.

The World Hunter Federation had to carefully choose someone to lead the main force, in case command fractured at a critical moment. Team Leader Choi, an excellent adviser, recommended a man for the job.

Someone who’d built up extraordinary strength and a distinguished record as a Hunter, while also possessing the strategy and knowledge needed to command a large army.

A Hunter. A soldier.

The one and only man to have reached the top of the ladder in both professions.

Chuck Hagel—an S-rank Hunter active since the Great Cataclysm and the former Secretary of Defense of the good ol’ U.S. of A.

“Oh. Sleeping Beauty finally decided to show up. Or did you take a long winter’s nap?”

Chuck Hagel’s not-quite-a-greeting drew quiet laughter from the people lined up on either side of me.

It vanished without a trace the next moment.

“You’re laughing? Does this fucked-up wartime situation look like a joke to you?”

“……”

“You lunatics. From now on, anyone who laughs in front of me is getting their ass kicked, rank be damned. I don’t care if you’re some pasty Yankee dumbass who thinks white skin is your greatest achievement in life, a darkie spouting bullshit about political correctness, or a yellow monkey who can’t stop staring at his smartphone. I’ll beat every last one of you half to death. Understood?”

“Yes, sir!”

“Goddamn it. I can’t hear you!”

“Yes, sir!”

Only after everyone shouted at the top of their lungs did Chuck Hagel nod and take a drag from his cigar.

“Okay, ladies.”

“……”

That was one hell of a force of personality.

He really was a living legend by anyone’s standards. Even Senior Kim Soodan would have to admit Hagel had him beat at bringing down the house.

Of course, those thick arms like a bear’s and the violence he was born with had a lot to do with creating this brisk atmosphere.

*He really is the right man to be in charge.*

Just as I thought that, a military jeep came tearing across the runway and screeched to a stop in front of us. A soldier in dress uniform hurriedly called out.

“Monster Wave! We’ve received an urgent request for support because of a Monster Wave!”

If I’d been an ordinary traveler, I would’ve taken a day to recover from jet lag.

But my life had parted ways with the word *ordinary* a long time ago, and there was no chance of them ever getting back together.

“Where?”
## Chapter artifact 793

# Chapter 793

With the whole world tearing the place apart with its eyes peeled, the chances of The Prophet slipping into a major city full of people were close to zero.

So the tight search net spread across the Middle East, centered on the main force, was focused on monitoring underdeveloped areas. The place we headed to right away was no exception.

Wasteland stretched out on either side of a road so rough it was embarrassing to call it one.

A desert as vast as an open sea, dotted here and there with small patches of trees like reefs.

And there, familiar faces were waiting for me.

“You’re with the main force, righ—huh?”

Surprise crossed a face so young he looked more like a boy than a young man. Xiao Shen stared at me, dumbstruck, then shouted as if he were screaming.

“Mr. Jin!”

“Damn it. Why does that Chinese kid have to be so loud?”

Chuck Hagel, who’d come along in Team Leader Choi’s place in case anything happened, let out a deep sigh and continued.

“Do me a favor. Can’t you do something about that kid? Every time we run into each other, all he talks about is you. My ears are about to fall off.”

“Well, he is pretty attached to me.”

“There’s a limit to how attached someone can be. Wilson wasn’t even that bad.”

“Who’s Wilson?”

“My dog. Every time I was away for a few days and came home, he’d come at me like a maniac. Probably thought I was an intruder.”

“Maybe Wilson just had a bad temper?”

“He died three years ago. It was summer.”

“……”

Shit. He’d just pulled out two cheat codes at once.

The combination of the Talullah[^1] moment and summertime sentimentality nearly took my breath away. I was relieved to see Xiao Shen, who’d just run over like a sprinter, if only by comparison.

[^1]: A Korean internet meme about awkwardly backpedaling after unwittingly insulting someone’s loved one.

“H-how could someone as shabby as Mr. Jin come all the way to a place this precious?”

“It’s the other way around.”

“Oh.”

I patted Xiao Shen on the shoulder. He’d frozen like a statue. Then I took in the scenery around us.

It was definitely a shabby place.

Everywhere was covered in sticky blood and filled with a foul stench.

Just as I was looking at a pool of blood the size of a small lake, a familiar voice reached my ears.

“You’re slow as hell. What took you so long?”

I turned around and saw a figure walking out of the darkness.

Over his shoulder shone countless eerie monster eyes.

*Shing.*

Dozens of Hunters accompanying us as our supposed entourage reflexively drew their weapons. I stopped them with a casual wave and answered evenly.

“I got here as fast as I could.”

“Already talking nonsense. I’ve been waiting at least a week.”

“Sure, I did sleep for a long time.”

“So you left this great king in a shithole like this and took your sweet time resting?”

“More or less.”

“Damn it.”

*Scuff. Scuff.*

Despite his grumbling, his face had drawn close, and he couldn’t hide how glad he was to see me.

I greeted the Skeleton King, whom I hadn’t seen in a week.

“You’re still alive.”

“I am. Though I died a long time ago.”

They say a dog that spends three years at a village school will recite poetry.

I gave a quiet laugh at the Skeleton King’s quick retort.

Over his shoulder stood an army of monsters—well over a thousand, even by a rough estimate.

Though, technically, they were an army of the undead.

“Looks like things have mostly wrapped up. What about the rest?”

“There aren’t any. I took care of every last one.”

I nodded at the Skeleton King’s words.

If he said so, then that was that.

Even Michael Silbert, who’d kept his identity completely hidden by controlling the two energies coexisting inside him, had once aroused the Skeleton King’s suspicions.

Whether he wanted it or not, the Skeleton King was the foremost expert on magical power.

*And he’s damn good at it.*

In Murim, a Supreme Peak master is called a one-man army.

An S-rank Hunter in the modern world might not compare to a Supreme Peak master, of course, but they weren’t treated all that differently.

Every one of them was a superhuman, on a different level from ordinary people and Hunters.

Even among such people, the Skeleton King’s abilities stood out.

An S-rank Hunter worth their salt could take down an army of monsters alone. But finishing the job in less than thirty minutes without a single casualty wasn’t something just anyone could do.

“So that’s *i-mon-je-mon*—monsters against monsters.[^2]”

“*I-mon-je-mon*? What are you talking about?”

[^2]: Jin twists a Korean four-character idiom about using one enemy against another, replacing its middle syllables with “monster.”

“You don’t know the old four-character idiom? The one our wise ancestors passed down to us…”

“I don’t need it. I’m a citizen of the great United States of America.”

“If my memory’s right, a few months ago you were reading ‘alligator’ as ‘arigatou.’”

“I’m Japanese American.”

“……”

“Konnichiwa.”

Is this guy insane?

I stared at the Skeleton King, who could swap out his family tree at the drop of a hat, with some bemusement. But I didn’t have much to say. He’d held off a Monster Wave by himself. The least I could do was praise him instead of cursing him out.

But just as I was sighing and turning away, a question suddenly crossed my mind.

*Why had he called for backup?*

The Skeleton King was powerful. As long as his magical power held out, he could create an endless army of the undead, and his own fighting ability was no joke.

So why?

Just to protect Xiao Shen?

Or…

*Was it because of something else?*

I turned back to face the Skeleton King, halfway through turning away.

Maybe those thoughts showed plainly on my face. He was watching me, too, with a somber look I hadn’t seen on him a moment ago.

“What?”

“Hmm.”

“What is it?”

After a brief silence, the Skeleton King answered.

“Even this great king doesn’t know.”

“What?”

“No matter how much I thought about what did it, or how it could have happened, I couldn’t figure it out. I did my best to look for it, but it had already disappeared without a trace.”

“What do you mean, ‘it’? What the hell are you talking ab—”

“You’ll understand when you see for yourself. You’ll remember it, too.”

Remember what?

As I struggled to make sense of that—

“Bring them here.”

*Thud. Thud.*

At the Skeleton King’s gesture, three undead ogres with their heads missing approached with heavy steps. Then, with hands surprisingly careful for their size, they lowered what they were carrying.

And the moment I saw the twenty bodies—bodies that had clearly once belonged to humans—I instinctively understood what the Skeleton King had meant.

“……Shit.”

The curse slipped through my clenched teeth like a groan, mixing with the cool desert air.

Chuck Hagel had come over to inspect the bodies. The cigar in his mouth fell to the ground.

“Holy shit.”

And he wasn’t the only one.

“What the hell is this…?”

“Damn it. Henry?”

Sighs and curses erupted all around us at once.

Those who made no sound were simply struck dumb with horror.

Was it because the bodies had been so horribly mutilated?

No.

I—and the others—had seen countless horrific sights in our lives as Hunters.

On a battlefield reeking of monsters and thick with the stench of blood, losing a limb wasn’t enough to make us bat an eye.

But even people like us had never seen anyone die like this before.

Well, except for a very small handful of people, myself included.

“Fuck. Jin, is this…?”

“Yes. It is.”

I answered as calmly as I could.

Then, beneath the moonlight spilling through the clouds as they slowly broke apart, I looked at the bodies. They’d lost every trace of vitality, like mummies, their bones and skin dried against their frames.

I thought of someone who’d died the same way just a month ago, in an unnamed hideout.

“Siegfried Wassmann.”

One of the three great Grand Mages of humanity—or, rather, one of the three who had been.

Whatever had killed him was here in this desert.

*Ding!*

* * *

The distance was the same going there and coming back, but the return trip felt incomparably shorter.

My head was full of questions.

*How could this have happened?*

I wasn’t the only one. Everyone was certain.

Michael Silbert had killed Siegfried Wassmann.

Why? Simple.

Siegfried Wassmann was a Grand Mage—and unlike Magic Johnson, a War Mage specializing in combat magic, he was a scholar through and through.

That was why Magic Johnson suspected Siegfried Wassmann of being the architect of Area A.

He was a master of all kinds of barrier magic based on magic circles, and an expert on monsters.

Would a mage that skilled—and that reclusive—have just wrapped a tarp around his hideout?

Like Area A, his hideout had been concealed behind all kinds of barriers. Only a handful of people in the entire world were strong enough to break through all those spells.

And among those few, Michael Silbert was the only one who’d wanted him dead.

But…

*We got it wrong.*

The moment I saw the bodies, I realized it.

I—and all of us—had been wrong.

At least on the day Siegfried Wassmann died, it wasn’t Michael Silbert who’d gone to the Grand Mage’s hideout.

If he’d been the one to finish him off, the Quest window taking up a corner of my vision right now should have disappeared long ago.



> **System**
>
> **Quest**
>
> **An Unknown Death**
>
> The reclusive Grand Mage, Siegfried Wassmann, has died for unknown reasons.
>
> But everything has a cause.
>
> Discover how he died and who killed him.
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Discover the truth behind his death (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???



The System wasn’t all-powerful.

It only pointed you vaguely in the right direction. It didn’t tell you how far you were from your destination or what traps lay along the way.

That was probably why, even after checking all the System messages and Quest windows when I woke up, I hadn’t noticed anything strange about this one.

I’d simply assumed the Quest hadn’t been completed because I hadn’t learned the full truth about his death from Michael Silbert.

To me, the Cataclysm Main Quest was the root I needed to pull out right away. Everything else was just a branch.

That was my crucial mistake.

Branches and roots had different jobs, but they were still part of the same tree.

Follow the root upward and you’d reach the branches. Trace a branch downward and you’d find the root hidden deep underground.

It just hadn’t come to light yet.

Even if something was hidden for now, sooner or later I could find it.

And in that sense, the first person I went to see after returning to the main force was one of the largest branches on the sick tree that was Michael Silbert.

“Someone died about two hours ago. Not just one person—twenty.”

At the words I blurted out as soon as I sat down, a faint smile crossed the gaunt face across the table.

“You’re in a hurry. Can’t a guest have a cup of coffee first?”

Coffee. A smile. A guest.

I licked my parched lips.

Strangely, I wasn’t angry. No—maybe my patience had been running out from the very start.

“I’m going to ask you one thing, so listen carefully and answer, you crow bastard.”

I spoke to Huginn, frozen by my killing intent, and let out the question that hadn’t left my mind all the way back.

“Did The Prophet kill Siegfried Wassmann?”
## Chapter artifact 794

# Chapter 794

“The Prophet killed Siegfried Wassmann?”

Huginn clamped his mouth shut at the killing intent in my voice. Just as he had for the past week. Just as he would forever, it seemed.

But unlike the investigators who’d interrogated him until now, I had no intention of backing down.

Not by any means.

“What do you think of this room? Nice atmosphere, don’t you think?”

At my sudden question, Huginn’s eyebrow twitched.

I stood up and slowly paced around the spacious room, furnished with nothing but a table and chairs.

“No cameras running twenty-four hours a day, no observation window. Must feel like paradise to a prisoner, right? I know because I went through something similar once. I learned how awful it feels to be watched every second.”

“……”

“So I brought you here specially. I thought it’d be more convenient for both of us. Like I said, no prying eyes, and…”

I dropped back into my seat with a thump and added, “The soundproofing magic is perfect, too.”

He didn’t answer, but I knew.

The look in his sunken eyes told me he’d understood exactly what I meant.

After a brief silence, what slipped between Huginn’s lips wasn’t a voice but a scoff.

*Pfft.*

The airy sound grew louder, then rang through the room.

Huginn’s shoulders shook as he laughed for quite a while. At last, he spoke.

“Is that all?”

“What?”

“I asked if that’s all you’ve got. Torture, threats—whatever you’re going to do, do it properly. That’s nowhere near enough to impress me.”

This time it was my turn to keep my mouth shut. Huginn took the baton, his face full of scorn.

“You won’t get the answer you want from me, no matter what you try. Just like those bastards who came before you.”

Those bastards who came before me.

So that was why he’d grown so gaunt since I last saw him. Looks like I wasn’t the first visitor.

Of course, I’d more or less guessed as much.

A bunch of countries could join forces, form the UN, and draft an international convention against torture. In the end, if no one found out, what did it matter?

And Huginn had been Michael Silbert’s right hand, taking care of missions both big and small.

A traitor to humanity, with the most important secret in his possession, had his lips sealed tight. The US torturers, seasoned in the Middle East, had probably put their skills to work with the leadership looking the other way.

*And failed across the board.*

I gazed steadily at Huginn after his outburst.

His mana was suppressed, and his entire body bound, but he was still an S-rank Hunter. More than that, he was an exceptional fighter chosen to be Michael Silbert’s right hand.

Even torture and mental magic would have a hard time breaking that iron will.

“Just open your mouth and it’ll all be over. Like the others who were captured with you, all you have to do is tell the truth.”

“Go fuck yourself.”

“Michael Silbert left you a final message, didn’t he? You’ve already heard it, I assume.”

“I have. But this is entirely my choice. Ever since I was five—”

“Shut up. I don’t want to hear it. I don’t care if you were a piano prodigy at five or an orphan who grew to hate the world.”

Everyone had their sob story.

But I wasn’t some late-night radio host. I had no reason to listen to a villain’s tired old backstory.

I did know what he wanted most right now, though.

“If you tell the truth, I’ll promise you one thing.”

“A promise?”

“Yeah. A promise.”

“Then you won’t get an answer. I don’t need anything…”

The moment Huginn started speaking in that scornful voice, I casually dropped the one line I’d prepared.

“I’ll kill you.”

“……!”

“As painlessly as possible. Cleanly. I can’t promise to let you go—I never could—but I can do that today.”

“You bastard…”

“Don’t deny it. You’d rather die than keep living like this, wouldn’t you?”

He tried to hide it, but I could see it.

The eyes, full of resignation and spite, wavered little by little. But the tongue hiding in his mouth still wouldn’t surrender his pride.

“Cut the bullshit. There’s no way you can make me talk.”

“From what you’ve been saying, you definitely know something.”

“……”

“By the way, how old are you now, sir? Around fifty, if I remember right… Still young. You’ve got a long life ahead of you.”

In Murim, fifty was old enough to be called a grandfather without anyone batting an eye. But in the modern world, fifty was still the prime of life.

Plenty of people with money lived past a hundred, thanks to cutting-edge medicine and magical health care.

And Huginn was an S-rank Hunter. Even with his mana suppressed, his vitality was on a completely different level from an ordinary person’s.

“Our crow friend’s going to live a long time. Of course, he’ll be spending the rest of his life in prison.”

I leaned my chair way back and gazed at the pure white ceiling, my voice calm as I went on.

“In a sealed room without a ray of sunlight, under close watch twenty-four hours a day. Interrogations whenever they feel like it. Or should I say torture? You’ve done enough to deserve it, so it’ll probably be pretty brutal for a long time.”

“……”

“You’ve been tough enough to make it this far, somehow… But what happens if you do this for fifty years? Well, at least you’ll stay healthy. They’ll probably shower you with potions after every round of cutting.”

Millions of people had been killed or injured in the terrorist attacks.

In front of a humanity consumed by grief and rage, the word *human rights* had already become meaningless.

If an article appeared in the *New York Times* tomorrow morning saying Huginn had been tortured, people all over the world would be shocked—and start collecting donations.

Not for his legal fees. They’d be raising money for potions to keep extending his suffering forever.

And as time crawled by, Huginn’s mind would slowly fall apart.

Or maybe the cracks had already begun to show.

“Team Leader Choi told me something interesting on the way here. Apparently, you caused a bit of a commotion on the plane. Are you sick? Or having a seizure?”

Probably the latter.

Pain was the same for everyone, even an S-rank Hunter with a strong body and mind. He just knew how to endure it.

Pain didn’t grow dull, even when you got used to it.

“Why aren’t you answering? You’re making me feel awkward for asking. If you’re already like this, how are you going to get through the rest of your life?”

Just as I straightened up from my half-reclined position, a wet crunch sounded, and blood poured from Huginn’s mouth.

He’d bitten off his tongue.

“Ouch. That must hurt.”

I clicked my tongue and pulled a potion from my Inventory, then shoved it into Huginn’s mouth. The bleeding stopped almost at once, and his half-severed tongue healed.

“Let’s not make this harder on each other. I didn’t remove your gag so you could bite your tongue off. I’m also starting to run low on the potions I brought…”

*Crunch. Splurt.*

The instant I said I was running low, Huginn bit his tongue again. I sighed.

“I told you not to do that.”

Then I rummaged through my Inventory and took out a potion.

More precisely, I took out a box packed full of them.

*Thud.*

“Please. I’m asking you nicely. I’ve only got about three hundred left. Okay?”

“……!”

“Still, good news. This time you only cut off a little bit of your tongue.”

“……”

“Open your mouth. Come on. Say ‘ah.’”

Huginn just stared at me blankly instead of answering, so I slapped him across the face.

*Smack!*

His teeth went flying in every direction.

But I wasn’t satisfied with stopping there.

*Smack! Crunch.*

His jaw joint broke, and his mouth fell open on its own.

“That’s it. Good job. You listen so well. But you’ve got tartar buildup. When was your last cleaning?”

With his mouth smeared in blood, Huginn stammered out an answer.

“Tw-two years ago…”

“That’s a while. Potions aren’t a cure-all. Tartar isn’t an injury, so it won’t heal. You need to brush your teeth. Or go to the dentist. What are you supposed to do?”

“Brush my teeth, go to the dentist…”

“What are you talking about, dumbass? You can just use a Clean spell. Is your head just decoration? Did you only keep it around since you were born so you could use it as a weapon in an emergency? Was your dream in elementary school to become a Dullahan?”

“Why are you even—”

“But you little shit. I’ve let you get away with enough. You fucking bastard, you keep dragging this out like you’re the last royal chef of Joseon, carefully tasting everything first. What is this, a royal banquet? You’re not leaving until you’ve used every potion in this box.”

“I’ll tell you! I’ll tell you everything—!”

“Shut up.”

I didn’t know what I was saying. Or why I was acting like this.

All I knew was that the heat that had been creeping up from my gut finally reached my head.

*Grab. Wham!*

I snatched up a potion bottle and swung it at the top of his head. At the dull crash and surge of pain, his tightly bound body trembled.

“W-wait!”

“This is reinforced glass, you bastard.”

*Wham! Wham! Crash!*

Even reinforced glass only lasted about three hits.

Broken glass showered over the top of his head, now spurting blood. The potion inside came pouring down with it.

*Whoosh.*

A miracle: healing and pain, happening at the same time.

But before he’d even finished healing, I grabbed another potion bottle.

*Whack! Whack! Whaaack!*

*Crash!*

When I came to my senses, I found myself pawing at an empty box.

“Is… is it over?”

“No.”

I answered while refilling from my Inventory with a new box.

“Hang in there. There are still two hundred left.”

“……!”

“You can do it. Let’s keep at it together. I can do this all day. Maybe I wouldn’t mind doing it every single day from now on.”

Huginn stared at me wide-eyed, then spoke in a trembling voice.

“I-I said I’d talk. Why are you…”

“Bullshit. When?”

“I’ve been saying it for ages. Over and over. I’ve been trying to tell you the whole time…”

“What a ridiculous bastard. Do I look like an idiot to you?”

“I’m telling the truth! I really did!”

“Are you yelling at me right now? Do you—do you feel so wronged you can’t stand it?”

“N-no, that’s not what I—”

“Forget it. You hurt my feelings. We’ve already got the box out, so let’s finish it first, then we can talk.”

“……!”

I thought I might have heard something like that, vaguely, but what did it matter?

Thanks to Huginn’s excellent teamwork, we emptied the second box of potions, too. When I took out a third, I heard his tearful voice.

“Stop! Stooop!”

The mouth even the veteran torturers hadn’t been able to pry open was now running wild.

Maybe the genuine madness I’d shown had moved him, I thought. I closed the box I’d opened halfway.

“You finally understand how sincere I am.”

“……The promise you made earlier?”

“I’ll keep it. If you want to die that badly.”

“How can I trust you?”

“That’s up to you. But I swear on everything I have. That’s all.”

“……”

“So? Your answer?”

Huginn swallowed, then finally opened his mouth.

“He did.”

“Be precise. Again.”

“The one who killed Siegfried Wassmann… was the person they call The Prophet.”

There was no doubt. Huginn was telling the truth.

But just as my suspicion became certainty, another question came to mind.

“The person they call The Prophet?”

“……Ah.”

Maybe it was because his mind was foggy. He looked like he’d said something he didn’t need to, but it was too late to take back words once he’d let them out.

*There’s more.*

I’d thought Michael Silbert and The Prophet were connected, but I hadn’t been able to pin down exactly how.

I glared at him, my eyes sinking deep, and spoke.

“Tell me what you mean. Tell me everything you know about The Prophet.”

“T-that…”

It was ironic.

He had to struggle to die, not to live. But Huginn had already been driven to the edge of a cliff, and there were no choices left.

“He’s Muninn.”

“What?”

The moment I blurted out the question, a memory flashed through my mind: the day Huginn first came to Ares Guild.

Two ravens engraved into a corner of his business card.

And… the conversation I’d had with Team Leader Choi.



“‘Huginn’ and ‘Muninn’ are the two ravens associated with a certain god from Norse mythology.”

“Who?”

“Odin.”

“……!”



I blinked.

Odin, the supreme god. And the two ravens who served him: Huginn and Muninn.

There had never been just one crow to begin with.

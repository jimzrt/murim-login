# Checkpoint Review — 1010–1014

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

# Chapters 1010–1014

## Plot

Taekyung stays in Gansu and leads nearly three thousand martial artists toward the front, where Dark Heaven could arrive within days. His linked Quest, “Road of Blood,” requires the annihilation of hostile forces in Gansu. Ma Junggeol and the Seven Masters of Baekma Bang accompany the force, though some leaders still distrust them.

Taekyung discovers he can detect and overhear nearby Sound Transmissions. After learning more about the mysterious Lord who guided Ma and his sworn brothers, Taekyung sends six of the Seven Masters to fetch him within five days; Ma remains behind. Namho then tells Taekyung he has something important to disclose.

Meanwhile, Sama Pyo admits to Sima Gong that he disobeyed the order to return to Gansu. Sima Gong acknowledges his growth but orders two martial artists dealt with for a taboo remark about Pyo’s succession. Pyo rides back to the Black Dragon Demon Gate, not the Fire Dragon Pavilion.

## Continuity

- Taekyung remains in Gansu and marches toward the threatened front with nearly three thousand martial artists. Gansu has about thirty thousand defenders across three lines; Dark Heaven’s strength and objective remain unknown.
- Taekyung’s “Road of Blood” Quest requires annihilating hostile forces in Gansu; failure means Dark Heaven wins and Gansu’s control is lost.
- Ma Junggeol and his six sworn brothers are former Ningxia mounted bandits who say they avoided harming civilians and were guided onto a better path by the Lord. Taekyung and Jeok Cheongang judged their account truthful and did not consider them likely spies.
- The Lord advised the Seven Masters for more than ten years, helped them form Baekma Bang, and encouraged their western trade route. His identity, motives, and possible connection to Dark Heaven are unknown.
- Six of the Seven Masters left to fetch the Lord within five days of the march’s halt; Ma Junggeol stayed with Taekyung’s group.
- Taekyung can detect and eavesdrop on nearby Sound Transmissions; what he hears depends on the participants’ relative levels.
- Namho says he has something important to tell Taekyung, but has not yet disclosed it.
- Sama Pyo knowingly disobeyed Sima Gong’s order to return to Gansu and accepts responsibility. He is now riding to the Black Dragon Demon Gate.
- Sima Gong ordered that two martial artists be dealt with for their taboo remark about Sama Pyo’s succession; their fate is not shown.

## Translation Decisions

- Render **피의 길** as “Road of Blood.”
- Use “Sound Transmission” for **전음**.
- Render **대인** as “the Lord” for Ma Junggeol’s benefactor, distinct from “Lord of Heaven.”
- Render **단혈방** as “Danhyeol Bang” and **일도단애** as “One Saber Cuts the Cliff.”
- Render **표야** as “Pyo” when Sima Gong addresses Sama Pyo.

## Durable state

{
  "active_continuity": [
    "The Lord advised Ma Junggeol and his sworn brothers for more than ten years, helped them form Baekma Bang, and supported their western trade route.",
    "Six of the Seven Masters left to fetch the Lord within five days of the march’s halt; Ma Junggeol remains with Taekyung’s group.",
    "Namho has an important matter he says he can only disclose to Taekyung now.",
    "Sama Pyo disobeyed Sima Gong’s order to return to Gansu, accepted responsibility, and is now riding back to the Black Dragon Demon Gate.",
    "Sima Gong ordered that two martial artists be dealt with for making a taboo remark about Sama Pyo’s succession."
  ],
  "continuity_sources": [
    1014
  ],
  "open_questions": [
    "Who is the Lord, and what are his motives and connection, if any, to Dark Heaven?",
    "Will the six Baekma Bang men return with the Lord within Taekyung’s deadline?",
    "What does Namho need to tell Taekyung, and why can he only tell him now?",
    "What is Dark Heaven’s full strength and objective in the western desert, and have its forces begun advancing?",
    "What consequences, if any, will Sama Pyo face for disobeying Sima Gong’s order?"
  ],
  "safe_through": 1014,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1010

# Chapter 1010

“So, that’s what you’ve decided?”

At Jeok Cheongang’s question, I nodded.

“Yes. I think I need to stay here after all.”

If Ma Junggeol and his men had arrived half a day later, I’d probably already be on my way to Qinghai with the Fire Dragon Pavilion members.

*Gansu had enough forces as things stood.*

The Kongtong Sect and the Zhongnan Sect.

Two towering powers belonging to the Nine Sects and One Gang stood firm here, and the Black Dragon Demon Gate, led by Sima Gong, was every bit their equal.

The dark-path figures and unorthodox factions gathered under the Black Dragon Demon Gate might have been inferior in quality, but their sheer numbers made them an enormous force.

But now the situation had changed.

The massive Dark Heaven army—estimated to number at least tens of thousands—was a problem. But the biggest reason I’d decided to stay in Gansu was time.

The time it would take them to reach us.

“When exactly did you return to Ningxia?”

Ma Junggeol answered.

“Three days ago. We arrived in the middle of the night, so I suppose you could say it was two days ago.”

“Three days ago?”

Jeok Cheongang cut in abruptly, furrowing his brow. Ma Junggeol hurriedly continued.

“W-we were in a hurry, too. We were so busy sending urgent messages throughout Ningxia and getting our men moving that we couldn’t think of anything else.”

He’d apparently interpreted Jeok Cheongang’s reaction as, *You arrived three days ago, so why are you only coming to us now?* But I knew why Jeok Cheongang had frowned.

*That was right around the time.*

A memory suddenly came to mind.

Several hundred people had been trembling with fear, saying that mounted bandits were roaming not far away.

Ningxia Province must still have seemed lawless to them. So, with Ma Junggeol’s urgent message causing an uproar, they’d probably assumed the mounted bandits were attacking.

It was hardly surprising that even the Lower District Sect member from the Shaanxi branch knew nothing about the details. It had all happened so recently.

*So that’s what it was.*

The events of the world turn in circles, and they’re all connected at the same time.

One incident’s aftermath becomes the beginning of another, and eventually it all leads to the present.

And Ma Junggeol’s answer—that they’d arrived three days ago—was enough to leave everyone with plenty to think about.

“How long did it take you to get back?”

At the Wind-and-Cloud Sword Lord’s question, Ma Junggeol counted on his fingers.

“Let’s see. It took seven days and nights just to get out of the desert, and crossing the grasslands again took another day longer than that… About a month, I’d say.”

“Wait. Didn’t you say earlier that it took twenty days just to get there? And then you spent another day and a half following Dark Heaven.”

“That’s right. But there’s a difference between traveling a route for the first time and making the return journey. Do you think we’re mounted bandits—no, horse caravans—for nothing?”

“...Hmm.”

It was an argument he couldn’t refute.

Just as the Wind-and-Cloud Sword Lord, a Supreme Peak master, could get a sense of an opponent’s level and the kind of martial arts they practiced after seeing only a few forms, no one could match mounted bandits and horse caravans when it came to finding the fastest route.

“Too much caution can become a poison. There’s something more important here.”

Jeok Cheongang stopped the Wind-and-Cloud Sword Lord before he could respond, then fixed his gaze on Ma Junggeol.

“If you were leading an army of tens of thousands, how long would it take you to reach here?”

“W-well…”

Ma Junggeol thought hard for a moment, then let out a sigh.

“That’s hard to answer. But…”

“But?”

“Assuming we had enough camels, desert horses, and supplies—and everyone had trained enough to endure an extreme forced march… Yes. Even if there were delays, it would take a month at most.”

“One month. Just a month.”

“Of course, depending on the circumstances, it could be much shorter.”

At Ma Junggeol’s addition, delivered as he gauged the room, Sima Gong’s face stiffened.

“What circumstances do you mean?”

“Have you forgotten? We lost more time than we needed to because we crossed the grasslands. The location we’d found them in wasn’t all that far from Gansu. Even taking that enormous force into account…”

Ma Junggeol trailed off, then swallowed hard before continuing.

“A-about twenty days should be enough.”

“……!”

“……!”

The air in the meeting room turned cold.

No—it froze like a glacier.

Everyone who’d briefly forgotten that fact now realized it and looked at one another with wide eyes.

That was right.

Unlike Ma Junggeol, who had to hurry back the way he’d come, Dark Heaven had another option.

They could advance.

Instead of detouring across the grasslands, they could break through the front by sheer force.

And if they chose a direct assault, the time left before a battle began would be next to nothing.

*One day, or maybe two.*

Of course, that was the worst-case scenario.

No one knew whether Dark Heaven’s army had remained there for several more days after Ma Junggeol left—or whether they were still there now.

But at a time like this, we had to plan for the worst.

That was war.

“I think we can throw any more armchair strategizing out the window. Don’t you all agree?”

Above Jeok Cheongang’s low voice, which broke the silence, rang a clear chime that didn’t fit the situation at all.

*Ding.*

* * *

*Rumble, rumble.*

Would this be what it looked like if a small mountain were moving?

With the Black Dragon Demon Gate and the Zhongnan Sect—and the hundreds of martial artists Sima Gong had conscripted from nearby—the force had grown to more than two thousand, close to three thousand. As I looked at the endless wave of people and horses stretching out behind me, I suddenly glanced up.

More precisely, I looked toward the translucent holographic window floating somewhere in the air.

> **System**  
> The conditions for the current Quest have been met!  
> **Head West** — Complete  
> Quest **Desert Mirage** successfully completed!  
> Quest rewards have been granted!  
> Gained a large amount of EXP and Fame!  
> A new linked Quest has been generated upon completion of **Desert Mirage**.  
> Would you like to view the new Quest?

Barely half an hour.

That was far too little time for a massive army of three thousand to finish all preparations and set out. There was no way I’d have time to check the newly generated linked Quest.

*Though I had a rough idea what it would say, so there was no need to check in a hurry.*

I tightened my grip on the reins of my galloping horse and silently gave the command.

*Open Quest window.*

*Ding.*

> **System**  
>   
> **Quest**  
>   
> **Road of Blood**  
>   
> Long ago, this land was a trade route linking one continent to another. Today, it has fallen into grave peril.  
>   
> The foreign merchants, with their unfamiliar features, are gone. So are those who used to cross the desert, heading for foreign lands with wagons piled high with silk.  
>   
> The rulers of the vast desert have cut off the trade routes that once brought prosperity to the Central Plains. Now they want everything within the Great Wall.  
>   
> The old days, when silk flowed in abundance, have already become a distant, dusty past.  
>   
> Endless steel, blood, and corpses will be the present and future of this land.  
>   
> May fortune be with you.  
>   
> **Grade:** Supreme Peak  
> **Restriction:** Jin Taekyung  
> **Mission:** Annihilate hostile forces in the Gansu region — Incomplete  
> **Reward:** A large amount of EXP and Fame  
> **Linked Quest determined by your choice**  
> **Failure:** **Dark Heaven** wins  
> — Lose control of the Gansu region

*As expected.*

That was more or less what I’d expected.

Actually, I knew full well that if we failed, it wouldn’t end there.

*If the Gansu front collapses, the entire western region will be in danger.*

War was just like a line of dominoes.

No matter how carefully and thoroughly you prepared from beginning to end, one mistake could bring everything you’d built crashing down in an instant.

*I have to stop them before it’s too late.*

The one thing we had going for us was that Gansu Murim had prepared thoroughly.

Three successive defensive lines, with thirty thousand troops deployed according to each line’s importance.

And Dunhuang, the foremost of those three lines, was close enough to reach in three days if we pushed ourselves to the limit.

The Silk Road.

This area, better known to people of the modern world as the Silk Road, was one endless stretch of plains and wilderness.

There was no need to slow down for a narrow path, no rugged terrain that would force us to abandon our horses.

All we had to do was keep riding until the horses collapsed from exhaustion.

The problem was…

*Dark Heaven could do the same.*

That was why we couldn’t afford to lose even a moment.

Even with camels and desert horses, there was a limit to how fast they could travel through the desert. But once they reached land covered in soil and grass instead of sand, that would change.

Dunhuang would be the first domino to fall, and tens of thousands of enemies would soon swarm across Gansu like locusts—

“What are you staring at so intently?”

“……!”

“Checking the shape of the clouds or something?”

I wasn’t exaggerating when I said I nearly jumped out of my skin.

It wasn’t the sudden voice that startled me. It was the menacing face that filled my vision as soon as I turned around.

“Ah, damn. You scared me. What’s with you all of a sudden?”

Ma Junggeol, who looked perfectly comfortable even on a saddle bouncing violently beneath him—a former mounted bandit, current horse-caravan chief—answered.

“Nothing much. You’ve been staring into the air for a while, so I thought I’d talk to you.”

“What’s it to you where I’m looking? And I don’t think we’re close enough for you to just chat me up.”

“Of course we’re not. You’re the one who had them rain arrows down on me. Three times, no less.”

I answered Ma Junggeol, who was scowling so hard his already vicious face looked even worse.

“So?”

“...You’ve got no conscience, do you? And even if I can understand the first two times, what on earth were you thinking when you ordered them to fire that third time?”

“Just thought stopping at two would make me look cold.”

“……?”

“That’s it. Happy?”

At my offhand answer, Ma Junggeol gaped at me as if I were insane.

“What do you mean, ‘that’s it’? Are you even human?”

“Feels like that’s a question I should be asking you.”

“...What’s that supposed to mean?”

What did it mean? He knew perfectly well.

But I was too tenderhearted to hit him with the facts about his looks.

I silently shrugged, then looked at Ma Junggeol and suddenly thought:

*Still, he really is nothing like he looks.*

Judging by his face alone, he looked like some evil spirit who could plunge the world into ruin. But from the way he acted, and the bits of his personality that showed through now and then, he seemed surprisingly stupid.

Even now, at the strong insistence of a few leaders who still suspected Ma Junggeol and the other horse-caravan men, he was practically being held hostage. Yet he seemed utterly carefree.
## Chapter artifact 1011

# Chapter 1011

There was nothing particularly positive about suspecting someone.

But in a time of war like this, suspicion was just another word for caution.

The more you looked, and the deeper you dug, the clearer the truth became—and the closer you came to victory.

That was the biggest reason Ma Junggeol and the other six masters of Baekma Bang had joined our group.

Or, to be precise, the Fire Dragon Pavilion I led.

*Though I was the one who stepped forward and volunteered.*

They were originally supposed to be placed under Sima Gong’s watch. But when I explained that he had his hands full commanding a sizable force, we reached a decision in no time.

They would be assigned to the Fire Dragon Pavilion.

We were in such a hurry that no one raised any further objections. Still, I saw it clearly.

The moment the decision about the Seven Masters of Baekma Bang was made, Sima Gong’s eyes sank deeper than before.

*Am I imagining it? Or…*

I let the thought trail off and glanced at Ma Junggeol.

He’d been grumbling about how rude it was to ignore someone standing right in front of you, but at some point he’d gone quiet.

Or so it seemed.

*Thud-thud-thud!*

The horses’ hooves thundered as they galloped, and the fierce wind coiled around us and rushed past.

And…

*Wooooong.*

A faint ripple passed stealthily through it all.

*This is…*

I could feel it instinctively.

This was a flow of energy only someone who had reached a profound realm could sense.

And within that faint ripple, carried to me beneath the clamor of countless sounds, was a voice I’d never heard before.

*Ssshhh.*

This wasn’t some calculated conclusion I’d reached through reason. It was an instinct I’d forgotten I had.

Like a child who had only just learned to stand on two feet, I sent my qi toward the ripple emanating from Ma Junggeol.

It touched the ripple, mingled with it, and soon became one.

So naturally that even Ma Junggeol, the ripple’s source, didn’t notice.

Nor did his six sworn brothers, who were exchanging the same kind of ripples with one another not far away.

“…How long do we have to be dragged along like this?”

That was the moment the faint ripple—no, the Sound Transmission—rang clearly in my ears at last.

*Ding.*

> **System**  
> Hidden achievement **A Bug in My Ear** achieved!  
> You can now detect and eavesdrop on nearby **Sound Transmissions**!  
> This is another ability granted to those who reach a great realm. But don’t get too excited. The **Sound Transmissions** you can eavesdrop on are limited by the levels of both the target and the user!

*…So I can do this now.*

I blinked in a daze for a moment, then focused on the Sound Transmissions reaching my ears.

Let’s hear what sort of conspiracy they’re cooking up.

* * *

“Honestly, how long do we have to be dragged along like this?”

“Exactly. What are we, hostages?”

“Whew, Father. I miss you so much today.”

“Huh? Didn’t your father pass away more than twenty years ago?”

“That’s why I miss him even more.”

“Oh.”

At his younger brothers’ grumbling Sound Transmissions, Ma Junggeol answered in a stern voice.

“Now, now. Why are you all complaining so much? We expected this from the start.”

The second brother, who fled faster than anyone in an emergency but worshipped the Chief like the heavens the rest of the time, nodded.

“Enough! The Chief is a hundred, a thousand times right, so all of you shut up. If he hadn’t foreseen a situation like this from the beginning, would he have dragged us into such a deathtrap?”

That was the second brother for you.

There was a reason people said no younger brother could outdo his older brother.

Just then, Ma Junggeol smiled with satisfaction at the sight of the little man gently putting the others in their place.

“Didn’t you hear what the Chief said earlier?”

At the third brother’s abrupt remark—he always had to stick his foot in everything—the second brother blinked.

“Earlier? When?”

“Right before we left. He wandered off on his own, supposedly to check a perfectly good saddle, and muttered something in a tiny voice. I listened, and…”

“You listened, and?”

“No, there’s nothing to hear. It was nothing, so don’t worry about it.”

Remembering what he’d said half a shichen earlier, Ma Junggeol hurriedly tried to cut him off. But the third brother’s Sound Transmission was already riding the wind.

“We’re fucked. What do we do now?”

“……”

“……”

A wind colder than the bitter north wind swept through the group.

In the heavy silence that fell, six pairs of eyes bored mercilessly into the back of Ma Junggeol’s head. His eyes sank darkly.

“Chief…”

“Third Brother, is that true?”

“It’s not, is it? It isn’t, right?”

“If that’s true, then seriously…”

“E-enough! There’s no way the Chief would say that.”

“What do you mean, ‘there’s no way’? I heard it with my own ears.”

At a loss for words, Ma Junggeol’s eyes darted back and forth.

How was he supposed to answer that?

He’d never dreamed the third brother would hear him mutter to himself—especially when he’d let it slip without thinking.

“That, well…”

Unable to stay silent forever, he hesitantly sent his reply.

At once, his six perceptive brothers let out a collective groan.

“So it’s true.”

“It really is.”

“Ah, Mother. I want to see you so badly today.”

“Sometimes it’s like that. You miss them all the more when they passed away so long ago.”

“Are you crazy? She’s still perfectly healthy. Why are you killing her off?”

“Oh.”

“Enough…!”

“Chief, what are we actually going to do now? At this rate, they’ll drag us all the way to the front and use us to catch swords, won’t they?”

Unlike the others, who were caught up in the chaos, the third brother was at least facing reality. Ma Junggeol gave the faintest shake of his head.

“Don’t worry. Things are going a little—just a little—worse than I expected, but they won’t use us to catch swords like you said.”

“If it’s not swords, they’ll use us to catch arrows. Thanks, Chief. You’ve ruined all our lives.”

“Now, now. I said that won’t happen!”

“Then what are you basing that confidence on, Chief? Let’s be blunt. If they tell us to jump, we have to ask how high, don’t we?”

“Well…”

“Take a look around. There are already several Supreme Peak masters here—people you’d be lucky to see once in your life. If those monsters start prodding us in the back and giving us the look, what choice do guys like us have except to sprint out and fight like hell?”

The third brother’s Sound Transmission sounded like an outpouring of pent-up anger. His sworn brothers chimed in one after another.

“There are those Zhongnan Sect Daoist punks treating us like outright bandits, the Black Night King himself, the Fire King, and that young Disciple of his who looks half-mad.”

“Especially that Jin Taekyung standing right in front of the Chief. He’s not right in the head. Have you forgotten how we nearly crossed the Sanzu River[^1] before we’d even made it through the gate?”

“Damn it, is this why we quit being mounted bandits? I’ll admit our past wasn’t exactly something to brag about, but we quit before we’d even gotten to rob anyone! We spent all day, every day sharpening our swords and never even got to draw them.”

“Enough! Now that I think about it, this is downright unfair. Have we robbed anyone? Killed any innocent civilians? We were just about to get our act together and pull off one decent score when we met the Lord and turned over a new leaf. We’re trying to live a little more honestly, and this is just too much.”

“Second Brother’s right. Sure, we look like this, but if we’d gone around doing only the most vicious things like everyone else, do you think the Lord would’ve left us alone? Isn’t that right?”

Listening to their Sound Transmissions, brimming with sorrow, Ma Junggeol felt a pang in his own heart.

They were right. What had they done wrong?

Of course, he couldn’t deny that he used to be a mounted bandit. But he could swear to heaven that they’d never done anything deserving punishment.

*If we’d actually done those things, at least this treatment wouldn’t feel so unfair.*

Robbing civilians?

Even when they steeled themselves and rode out to attack, they couldn’t bring themselves to do a thing.

What could they take from people who’d already been stripped of everything by other mounted-bandit groups? Countless times, they’d even given away their own food to families holding newborns too hungry to cry.

And that wasn’t all.

Although they looked like fiends, Ma Junggeol and his six sworn brothers were timid by nature.

Robbing or killing civilians had been impossible for them from the start. And even when they occasionally came across a gutsy merchant caravan traveling to Ningxia Province, they just collected a toll and let it pass.

Why?

Simple.

*Because they were scared.*

Who would travel through a lawless place like Ningxia Province without a proper escort?

It was only natural for an Escort Bureau or merchant caravan to bring at least several dozen armed men. In that tense standoff, Ma Junggeol just had to put on his vicious face and say:

*“So, you mean to shed blood after all?”*

A fiendish-looking face paired with a stern voice made for an excellent negotiating tactic.

Whether the other party was an Escort Bureau, a merchant caravan, or a mounted-bandit group so practiced at killing that they were nearly ready to ascend to immortality.

Back then, Ma Junggeol and his six sworn brothers knew little about martial arts. That was how Ma Junggeol and his six sworn brothers, whose martial arts were still rudimentary back then, had survived as a mounted-bandit group.

Until the man they called “the Lord” appeared.

And even now, Ma Junggeol firmly believed in the Lord who had led them onto the right path.

“Enough, all of you!”

At Ma Junggeol’s forceful Sound Transmission, the grievances streaming from behind him cut off at once.

He didn’t let that brief opening go to waste.

“There’s nothing to worry about. Even if you don’t trust me, surely you trust that the Lord would have anticipated a situation like this?”

“Hmm.”

“That’s true.”

“If it’s the Lord, that’s different. The Chief, maybe not, but the Lord, yes.”

“Right. We can’t trust the Chief, but we can trust the Lord.”

“Now that you mention it, that makes sense.”

“For once, you’re saying something right.”

The answers only made him feel stranger the longer he thought about them, but Ma Junggeol continued his Sound Transmission with a vague sense of unease.

“I sent a few men back on the pretext of relaying news to Ningxia, so the Lord will surely hear about this. Until then, don’t do anything rash. Understood?”

Just then, the third brother, the one with the bulbous nose, cut in.

“But that’s only if the Lord’s in his right mind.”

“What?”

“Well, isn’t it? You know as well as anyone how he can be a little… all over the place.”

Ma Junggeol blinked a few times, then stammered out a reply.

“H-he’ll be fine. Probably.”

But even without Ma Junggeol’s uncertain answer, his sworn brothers knew it was something no one could be sure about.

“Damn. Now that Third Brother’s said it, I’ve got a bad feeling.”

“But hasn’t the Lord been more or less all right lately? That’s why he’s been telling us this and that about the direction we should head.”

“He has. But with him, you never know when he’ll snap.”

“The Lord was strange from the first time we met him. His hair was a complete mess, and his face was so black he looked like he hadn’t washed in days. He was a regular beggar. He still looks the same now, too.”

“This is bad. If the Lord’s off his rocker right now, sending the men to him will be useless, won’t it?”

As his sworn brothers’ worry deepened, Ma Junggeol scrunched up his already ugly face and thought it over. At last, he spoke.

“We have no choice. One of us should go in person. Maybe seeing some familiar faces he sees often will help him come to his senses sooner.”

“One of us? Who?”

“Hard to say. We’ll have to decide now.”

“Once we decide, how are you going to send him? That’ll be difficult in our current situation.”

“As the Chief, I’ll figure that out, so don’t worry—wait a minute.”

Ma Junggeol abruptly stopped his Sound Transmission and frowned.

“You’ve been getting awful casual with me for a while now. Did you lose half your tongue or something? Which insolent bastard is it? Huh?”

That was the exact moment.

Someone’s actual voice, from someone he hadn’t expected, pierced Ma Junggeol’s ears.

“Me.”

“…?”

“It’s me.”

No. Impossible. Surely not.

Muttering to himself, Ma Junggeol slowly raised his head. He’d been keeping it slightly lowered to hide his moving lips.

And there, facing him, was that insolent bastard, smiling menacingly.

“Uh, uhh.”

Ma Junggeol shuddered as if possessed by a ghost. Jin Taekyung smiled warmly at him.

“Looks like there’s a lot you need to tell me. Isn’t that right?”

[^1]: The Sanzu River is a Buddhist river said to lie between the world of the living and the afterlife.
## Chapter artifact 1012

# Chapter 1012

Time swept by like the wind, keeping pace with the horses’ ceaseless gallop.

Until the sunset swallowed the wilderness and the darkness that followed pressed down on the world. Until the pale dawn came creeping through the gap between them.

And when darkness fell for the second time, Ma Junggeol’s lips, which had been moving nonstop, could finally rest.

“……And that’s what happened.”

By the time he finished his long story, Ma Junggeol looked as if he’d aged ten years overnight.

Partly because he’d spent more than a full day reciting every event of the past decade or so. But the burden of his audience—which had grown one by one, starting with me—must have weighed on him even more.

Of course, nothing compared to the pressure radiating from that giant known as the Fire King.

“What do you mean, that’s what happened? Keep talking.”

At Jeok Cheongang’s low growl, Ma Junggeol, already dead on his feet, looked like he was about to cry.

“I’m really finished. I’m telling you, there’s nothing else to say.”

“If I dig around and anything comes out later, it’s ten hits per syllable. Still nothing?”

“What?”

It’s not like he had a whole stash of stories tucked away. What was there to search?

At Ma Junggeol’s pleading look, I shook my head and spoke up.

“Give it a rest. And if it’s a hundred hits per syllable, why would he say anything? Even if he had more to tell, he’d hold out even if it killed him.”

“Is that so? Then I’ll lower it to ten. Spill everything.”

“Ten would be enough to kill him.”

“Fine. One hit. That’s my final offer.”

“……You might as well tell him to make his last will. At this point, it seems like you just want to kill him.”

Jeok Cheongang frowned at my quiet rebuttal.

“You’re too soft. Sometimes you have to do this to squeeze even one more word out of someone.”

“Look at him. There’s not a drop of broth left to squeeze out of him.”

I wasn’t just saying that. Ma Junggeol was practically half out of his soul.

Think about it.

It was easy to say ten years, but he’d had to recall every single thing that happened over a whole decade, the kind of time it takes for mountains and rivers to change, without a wink of sleep. No wonder he’d turned into a half-dried squid in just over a day.

“P-please believe me. I really did tell you everything. I didn’t leave out a single thing.”

Ma Junggeol pleaded, his eyes brimming with tears. His six sworn brothers joined in.

Or, more precisely, they started to speak and then stopped.

“What our eldest brother said is righ—”

“Shut your mouths before I beat the hell out of you. Especially you.”

The shorty Jeok Cheongang had singled out froze stiff.

“M-me?”

“Yeah, you. Make one more racket and you’re dead. You don’t need to chime in after every damn sentence. What are you, some little brat?”

At Jeok Cheongang’s shout, the shorty clamped his mouth shut. Watching from the side, the bulbous-nosed one murmured in a voice full of delight:

“At last…”

At last what?

These guys were all out of their minds, but at least one thing was clear.

“Mujin.”

Hyuk Mujin understood what I meant by calling his name and clicked his tongue.

The other members, apart from Sama Pyo and Taishan, who’d joined us the day before along with the Black Dragon Demon Gate, reacted much the same way.

“Yikes. Is this really okay? I’ve got a bad feeling about it.”

“Benefactor—no, Young Master Jin—no, Pavilion Master.”

“I think we should tie them up, at least.”

“I think differently—damn it. This miserable saddle!”

Unlike Taishan’s shoulders, which were as comfortable as a cushioned seat, Namho was perched on a saddle that bounced violently beneath him. Grimacing at the pain in his backside, he continued:

“We should follow the Pavilion Master’s orders. That’s the right thing to do. And do you really think those guys would dare entertain any other ideas, even without tying them up?”

“That’s true.”

Hyuk Mujin nodded in agreement. Ju Hwaran and Song Ilseom then let go of the reins they’d each been holding.

Of course, those weren’t their own reins. They belonged to the Seven Masters of Baekma Bang, who had been riding close beside them, boxed in on all sides.

“Thank you for trusting us.”

“I’m not completely trusting you yet, so there’s no need to thank me.”

That was what I said to Ma Junggeol, whose eyes were even welling up with tears. But my thoughts were different.

*No matter how I look at it, they’re not spies sent by Dark Heaven.*

When I first overheard their Sound Transmission, my suspicions had flared up again, after I’d set them aside for a while.

At first, anyway.

But now that I’d heard Ma Junggeol’s whole story, the suspicion in my heart had quietly turned into curiosity about someone.

The mysterious master Ma Junggeol and his sworn brothers revered as “the Lord.”

—What do you think?

Jeok Cheongang’s low Sound Transmission slipped into my ear.

I already knew what he meant, so I turned my gaze naturally toward the road ahead and answered.

—I’m not sure.

—Are you holding back? Or…

—I really don’t know. That person they call the Lord seems less suspicious than… strange. Unbelievably strange.

That wasn’t an exaggeration. The mysterious Supreme Peak master they called the Lord had appeared out of nowhere one day and wiped out a band of mounted bandits who’d escaped even the authorities’ control. He was a person shrouded in mystery.

*They said they didn’t know his name, where he came from, or anything else about him.*

The Seven Masters of Baekma Bang had been serving him for more than ten years.

Yet neither Ma Junggeol nor any of the Seven Masters knew who he was. And whenever they were pressed about it, they all gave much the same answer.

*“No, it’s all true. That’s just what he’s like!”*

*“Why would we dare lie to you? Please, you have to believe us.”*

*“You’ve already heard us talking, so you know he’s a bit—no, quite a bit—all over the place. Huh? His name and age? Don’t even ask. They’re different every time. Isn’t that right, Youngest?”*

*“The others are right. Chilbok, Gaettong… Was it three years ago? He thought he was a seventeen-year-old girl named Sohyang. We gave up trying after that.”*

*“We don’t know when he started living in Ningxia Province, either. He just suddenly appeared, subdued the whole area with his absurd divine might, then shut himself away in his residence and wouldn’t budge. He’s been like that for nearly ten years. I know it’s hard to believe, but it’s true.”*

The stories kept piling up, one after another, like sweet potato vines that kept coming no matter how many you pulled.

They were so absurd that, as I listened, I couldn’t help thinking:

*What the hell is that guy?*

Everyone had their own ambitions.

Regardless of whether they were good or bad, there was bound to be some goal a person had carried in their heart at least once.

But the Lord in their stories fit none of them.

He hadn’t taken over Ningxia and ruled as a mighty conqueror. Nor was he a notorious fiend who’d slipped into the frontier to hide his identity, or a hermit master wandering where no one would find him because he was nearing the end of his life.

*If he wanted to rule as a conqueror, there’d be no reason to hole up in a cave. If he were a fiend, he’d have tried his damnedest to keep his identity hidden—or from the start, he’d have put the mounted bandits under his command.*

If he were a hermit master, there wasn’t even much to think about.

Honestly, what kind of deranged hermit would choose the frontier, with its year-round high levels of fine dust and blowing yellow sand, over some remote mountain valley with beautiful scenery and clear water?

Even I knew the famous poet Paul Valéry. If he’d lived in Ningxia Province instead of France, he would’ve written, *The yellow dust is blowing. Fuck, I want to die.*

*And it wasn’t as if he were an old man gone senile, or a dying elder who didn’t need to seek out some remote mountain valley, either.*

According to the Seven Masters of Baekma Bang, the Lord rarely washed, and grime streamed from him, but his general appearance and voice seemed to belong to a man around middle age.

What’s more, when Ma Junggeol and his sworn brothers brought him liquor and food, he’d offer them a little instruction in return. He’d stay in his residence, then occasionally head out to town.

He said staying inside all the time was stifling. He wanted to get a little human company.

He must have wandered around so often that the Seven Masters didn’t even need to hide his identity for him to blend naturally into Ningxia Province.

Like Beggar Number One.

*This is a hermit master?*

Was this what it felt like to sink into a deep mire?

Just as my disbelief and curiosity kept growing the more I thought about it, Jeok Cheongang moved his lips. He’d clearly come to the same conclusion I had.

—In my long life, I’ve seen hundreds of carts’ worth of lunatics…but I’ve never seen anyone like this.

—You’ve only just started growing hair again.

—……Do you want to die?

—No. But I agree with what you said, Old Master. There’s no figuring him out.

—Could he be one of the Lord of Heaven’s minions?

—Of course he still has hands and feet left to command. But if you were the Lord of Heaven, would you put someone like that under you?

Jeok Cheongang answered without hesitation.

—Am I crazy?

—Right?

—Even if I took a Flame-Extinguishing Divine Fist to the head, I wouldn’t take a man like that as a subordinate. Of course, that’s assuming every word those vicious-looking bastards told us is true.

—But you already believe them.

—That’s…

His Sound Transmission faded as he turned his head without thinking.

As soon as their eyes met, the Seven Masters of Baekma Bang went rigid like statues. Jeok Cheongang shook his head.

—Yes, you’re right. I can tell they aren’t lying, either. No—they aren’t even capable of it.

That much seemed clear to me, and to everyone else as well.

But even if we concluded that they and their Lord posed no danger to our side, the two of us couldn’t make every decision on nothing but our own instincts.

—What are you going to do?

As Jeok Cheongang’s Sound Transmission slipped into my ear again, I considered it briefly and made up my mind. I gradually eased up on the reins and drew my horse level with the Seven Masters of Baekma Bang.

“W-why now? What is it this time…?”

Ma Junggeol and his sworn brothers were already frightened before I’d said a word.

I looked them over in silence, then suddenly asked:

“How long would it take?”

“What do you mean…?”

“To bring the person you call the Lord to our current destination.”

“……!”
## Chapter artifact 1013

# Chapter 1013

“Y-you mean the Lord?”

It must have been the last thing they expected. Ma Junggeol and his sworn brothers stared at me with wide eyes, then belatedly came to their senses.

“No, why the Lord all of a sudden…?”

I answered Ma Junggeol, whose voice trailed off, in an even tone.

“It’s not all of a sudden. He’s connected to this situation to some extent. And I’m sure you know why I’m asking, so I don’t need to spell it out, do I?”

“You suspect me… no, us, of being Dark Heaven’s spies?”

“Not exactly. At least, not the people here.”

“Then, the Lord?”

When I answered with a shrug instead of words, Ma Junggeol and the rest of the Seven Masters of Baekma Bang stiffened.

“That’s ridiculous!”

“Damn it, how many times do we have to tell you it isn’t true?”

“As our Chief already told you, the Lord is absolutely not that kind of person. You heard it all for yourself, didn’t you?”

Of course I did.

I’d learned only that he was a highly unusual person—the kind you rarely came across.

But this wasn’t a situation where I could just think, *Huh. People like that exist,* and let it go.

“Enough! If necessary, I’ll stake my own neck on it!”

I scratched my chin as I looked at the shorty who’d shouted a beat late.

“You over there. You’re staking your own neck?”

“…Huh?”

Perhaps he hadn’t expected me to call his bluff so directly. The shorty flinched and fumbled with his lips.

“I-I mean, the neck is a bit much. Maybe my wrist…”

“A man’s word is worth its weight in gold! Of course I’ll stake it! Cut off Second Brother’s head!”

“Hey, you crazy bastard!”

While the shorty flailed at the bulbous-nosed man’s sudden offer to wager on his behalf, I spoke in a low, measured voice.

“Whether it’s a wrist or a head, the math still doesn’t work out.”

“What do you mean…?”

“I’m asking because I’m curious. Do you think all these people are taking a casual trip to the next town over just because they’re bored?”

“……!”

The mood turned heavy in an instant. Their wavering eyes were fixed on the backs of the countless people riding far ahead.

The Black Dragon Demon Gate. The Zhongnan Sect.

Martial artists from large and small sects throughout Gansu Murim.

And finally, me and the members of the Fire Dragon Pavilion.

And that wasn’t all. In the direction thousands of men and horses were riding at full speed lay tens of thousands of our allies, who could find themselves in danger at any moment.

Even if not just one shorty but all the Seven Masters of Baekma Bang staked their lives, their wager couldn’t be weighed against that burden.

“Am I the only one here who’s ever heard the saying, ‘War isn’t a gamble’?”

Ma Junggeol and the others didn’t dare answer my question, which I’d murmured almost to myself.

Naturally.

They had to know how absurd it would be to cast aside all suspicion of a mysterious Supreme Peak master based on nothing but the testimony of a few horse-caravan men.

The Great War that would decide the fate of the world was already underway, and war was no gamble.

Besides…

*There’s good reason to be suspicious. This isn’t paranoia.*

I murmured to myself and stared straight at Ma Junggeol.

Remembering the Sound Transmissions that had passed among the Seven Masters the previous day.

“I heard something very interesting in the Sound Transmission you exchanged among yourselves. What do you make of that?”

“If you heard something interesting, what was it…?”

“I heard you say the Lord had given you all kinds of advice about which direction to take. And not that long ago, either.”

I put particular emphasis on the last part. Ma Junggeol’s eyes, already lowered with worry, visibly wavered.

“T-that…”

“Now I’m curious. Exactly how recently was it? And what did he tell you? Don’t you think?”

I suddenly turned and tossed the question to Jeok Cheongang, who had been watching the situation. He nodded.

“Hearing you say that, this old man is curious too. Why did you keep something so important to yourselves until now?”

Looking back, it was more than enough to make anyone suspicious.

How had the Seven Masters of Baekma Bang—former mounted bandits, no less, and ordinary drifters who’d never distinguished themselves—come up with the bold idea of crossing the Land of Ruin?

Though I’d watched them closely for a short time, and remembered every word of their Sound Transmission, I already had a guess at the answer.

“The idea of opening a new trade route to the west wasn’t yours from the start. Am I wrong?”

“……!”

“……!”

If I hadn’t followed Namho’s advice the day before and moved back early, quite a few people might have been startled by what I’d just said.

But within a dozen or so yards, it was just us. And Ma Junggeol had only one option left.

“…There’s nothing more to hide.”

The words slipped out after a heavy silence. They were as good as an admission.

Before his sworn brothers could hurriedly shout something, I raised a hand to silence them and calmly continued my questions.

“Why did you hide it?”

“Because the Lord wouldn’t have wanted us to. Thanks to him, we changed our ways and have lived well ever since. We’re not animals—how could we go around openly blabbing about that?”

“Tell me more.”

“This wasn’t the first time. From more than ten years ago right up until today, the Lord has given my younger brothers and me all kinds of advice. When we first met him, we were so overwhelmed by his divine might that we asked to become his subordinates. He refused us outright and said…”

Ma Junggeol slowly looked over his sworn brothers, their expressions complicated, then went on.

“A caterpillar should eat pine needles. He asked if it might be better to gather mounted bandits like us, who still had a chance to repent, and make a home together. So my younger brothers and I decided to follow his advice.”

“Baekma Bang…”

“That’s right. That was how Baekma Bang began. And even after that, whenever we ran into trouble, the Lord always showed us the right way forward. The new trade route was no different.”

“Then when you said you’d been considering a western trade route for years, was that…”

Ma Junggeol immediately understood what I meant and hastily waved his hands.

“I don’t know if you’ll believe me in a situation like this, but that part is absolutely true. The Lord simply advised us to do it. Afterward, we started searching for a new route west and realized the grasslands were our only option. Of course, we hadn’t dared attempt it all that time.”

“And that must also be how you noticed the gap in the western grasslands so quickly.”

At Jeok Cheongang’s sudden mutter, Ma Junggeol nodded.

“That’s right. Of course, we had no idea things would take such an unexpected turn. The Lord probably didn’t, either.”

Naturally.

Even if Hong Dao, the Dharma King who could read the heavenly patterns, were still alive, how could he have predicted in such detail something that would happen years later?

*At that point, it wouldn’t be reading the heavenly patterns. It’d be prophecy. Prophecy.*

And from the rest of Ma Junggeol’s story, the advice from the man they called the Lord didn’t seem all that special.

He’d started by helping a few decent mounted bandits—with nowhere to go and no experience farming—put their skills to use and form Baekma Bang.

A new trade route beyond the desert?

It was a bold idea, not one an ordinary person would come up with easily. But given his martial prowess and deeds, the man was anything but ordinary.

It was also the kind of wish the heads of the great groups bordering the desert or ambitious merchant-house leaders might have entertained at least once.

But what was this strange feeling I couldn’t explain?

*What the hell?*

I shook my head to clear away my stray thoughts, then parted my lips, which had been closed for a while, toward Ma Junggeol, who was swallowing nervously.

“Then I have just one last question. Whose idea was it to come find us?”

“I’m ashamed to say it was the Lord’s advice as well.”

“Just as I thought.”

“To be honest, we could have arrived half a day earlier. But it was such a serious matter that we couldn’t decide among ourselves, so as soon as we entered Ningxia, we went to see the Lord.”

“Go on.”

“We told him what happened on the grasslands and in the desert. He knocked back several bowls of liquor as though he were listening to a dog bark, then said, ‘You idiots should’ve gone to Gansu ages ago. Why are you still sitting on your asses here?’”

“……!”

“After that, well, here we are. Damn it.”

Ma Junggeol fell silent, his face half resigned. A brief silence followed.

Then, just as only the horses’ ragged breathing and the clatter of their hooves thundering along could be heard, the bulbous-nosed man glanced around and cautiously spoke up.

“Seven days and nights. I think that should do it.”

“What the hell are you talking about all of a sudden?”

Jeok Cheongang frowned at the out-of-nowhere remark. The bulbous-nosed man panicked and hurriedly pointed at me.

“Y-your Disciple over there asked us earlier how long it would take to bring the Lord back, didn’t he? That’s what I was answering.”

The first time is hard. After that, it gets easier.

Ma Junggeol’s sworn brothers, who’d been moving their lips without managing to say anything, finally chimed in.

“Third Brother’s right for once. Seven days and nights will be plenty.”

“Just leave it to us. We’ll bring him back, even if we have to give it everything we’ve got.”

“W-well, it’d take seven days and nights if we’re going to the Qilian Mountains. It might take longer if it’s the Great Snow Mountain or Dunhuang.”

“It’s not as if the Lord’s some fiendishly evil fiend. Rather than staying cooped up in some remote village, why not take this chance to enter the Murim Alliance’s service? What do you think?”

“Hah! ‘Not a bad idea,’ you say? He’s already done a great service by sending the seven of us to warn you about Dark Heaven. It’s bound to be an excellent choice for the Lord too, since…”

Whoosh! Wham!

“Gah!”

“You little shit! I told you to stop shouting ‘Hah!’ Did my words go in one ear and out the other?”

Jeok Cheongang moved like a ghost, kicked off the saddle, soared through the air, and smacked the shorty on the back of the head. Then he returned and turned to me.

“So, what will you do?”

I slowly swept my gaze across the Seven Masters of Baekma Bang and answered.

“Six days. No—five.”

“Huh?”

“Let’s make it five days. Whether this march stops at the Qilian Mountains, the Great Snow Mountain, or Dunhuang, you’ll be back within that time.”

“……!”

“Of course, one person has to stay behind, no matter what. You know who that is. I don’t have to say it out loud.”

“W-wait. You mean our Chief…!”

The Seven Masters of Baekma Bang began to object all at once, having realized what my words meant. Then Ma Junggeol suddenly spoke.

“Fine.”

“Chief!”

“I can stay here. You all go bring the Lord back as quickly as you can. Go!”

Perhaps they sensed something in Ma Junggeol’s firm manner.

The others, their lips moving as if they wanted to say something, turned their horses in a hurry and left the formation at my quiet nod.

*Thud-thud-thud!*

Ma Junggeol watched the six grassland horses disappear into the darkness, his gaze deep and steady.

And though his face was resolute, his barely moving lips held the words he couldn’t bring himself to say aloud.

“Fuck. I’m so fucking screwed…”

“……”

“……”

*What the hell kind of guy is this?*

Just as Jeok Cheongang and I were staring at Ma Junggeol, whose eyes had grown damp, in disbelief, Namho came over, performing an almost acrobatic routine on his bouncing saddle.

“There’s something I need to talk to you about. Got a minute?”

I was planning to report this to the command staff right away, so I shook my head.

No, more precisely, I was going to shake my head.

Until the next moment, when Namho lowered his voice and whispered into my ear.

“It’s important. I can only tell you now.”
## Chapter artifact 1014

# Chapter 1014

*Thud-thud-thud!*

Thousands of men and horses raced across the vast open plain. At their head, the martial artists of the Black Dragon Demon Gate were doing an excellent job as both vanguard and guides.

Of course, some of them were more preoccupied with sneaking curious glances at someone far off to the side.

“I’d only heard about him, but he’s much younger than I expected. He doesn’t look much older than me.”

“They said he was around thirty at most, so that makes sense. Still, blood tells. His face is the spitting image of the Sect Leader.”

“The Black Dragon Saber… What a killer sobriquet. So, is that rumor true?”

The young man asking out of nowhere looked barely twenty.

The middle-aged man frowned as if annoyed by the question from the youngster, who still had the down on his cheeks.

“What rumor are you talking about? You know I’m just as clueless about the inner workings as you are, so you’re not asking because you think I’d know.”

When the older man openly showed his displeasure, the young one hurriedly waved his hands.

“It’s nothing. I just heard our Young Sect Leader is stronger than the Ten Dragons and Phoenixes of the Central Plains.”

“Who knows? I’ve never even seen the Ten Dragons and Phoenixes.”

“Right. The Ten Dragons and Phoenixes.”

“What?”

“No, I didn’t mean you’d necessarily met the Young Sect Leader, Uncle.”

The middle-aged man glared at the young one as he slyly looked away, then shook his head.

“I don’t know which idiot’s been running his mouth, but don’t believe everything you hear. It’s all ridiculous bullshit.”

“Bullshit?”

“Yeah.”

“That’s strange. You told me yourself last time, Uncle. When you were dead drunk.”

“……!”

“So it’s true, then? Five years ago, the man who single-handedly wiped out the One Saber Cuts the Cliff, the former chief of Danhyeol Bang, and twenty of his men…”

“That’s enough. Don’t say another word.”

The middle-aged man’s firm voice cut off the young one before he could finish. But the awe in his eyes never left the man he’d been sneaking glances at.

The Black Dragon Saber, Sama Pyo.

The Young Sect Leader of the Black Dragon Demon Gate, to which the two men belonged, and the heir who would one day follow the Black Night King, Sima Gong, in leading the unorthodox Murim.

The young man wore a stiff martial uniform that hadn’t yet lost its creases, proof he’d only recently joined the Black Dragon Demon Gate. He couldn’t hide his amazement.

*So the whole story was true.*

Everyone knew about the bloody tragedy that had unfolded at Danhyeol Bang, once one of the powers of Gansu Murim.

The chief of Danhyeol Bang, One Saber Cuts the Cliff, had been one of the ten greatest saber masters in Gansu. He and his closest men had all been found brutally murdered on the same day.

And after that?

What was there to say?

A body without a head was bound to fall. Especially in Gansu, which had become the de facto headquarters of the unorthodox Murim under the Black Dragon Demon Gate’s influence.

Danhyeol Bang had once commanded three hundred members. That was how it fell, and five years later, people had naturally forgotten it.

No. No one had bothered to remember.

Not that, shortly before the massacre, Danhyeol Bang and the Black Dragon Demon Gate had been involved in a minor dispute.

Not that, on the day the mysterious killer came, the Captain of the Guards—who should have been protecting the pleasure house where the chief and leaders of Danhyeol Bang had gathered to drink—had left with his men.

And not that, less than a month later, that same Captain of the Guards had become the Black Dragon Demon Gate’s Outer Hall Master.

It had all been forgotten. It had to be.

The identity of the killer skilled enough to slay one of Gansu’s ten greatest saber masters, the background of whoever had ordered the killing, and even where all of Danhyeol Bang’s property and farmland had gone.

But that was only the surface. The unorthodox martial artists who knew the whole story were certain of what had happened.

And they were in awe.

Just like the young man who, as an unorthodox martial artist himself, now looked at Sama Pyo with admiration.

“That’s really, really incredible. Don’t you think? It’s no wonder he became the heir over his older half-brothers—”

The young man drew in a sharp breath.

Reflected in his trembling eyes was the middle-aged man, face twisted as he gripped his sword hilt.

“You really have a death wish, don’t you?”

The voice was so low that even the young man riding right beside him wouldn’t have heard it if he hadn’t been listening closely.

But the killing intent in it seemed to squeeze the heart of the young man, still a raw novice.

“W-why all of a sudden…?”

“Shut your mouth if you want to live even a few more days.”

The older man cut off his stammering without mercy, then quickly scanned their surroundings.

Perhaps it was because they were racing across such a vast plain.

Fortunately, there was plenty of distance between the riders, and the thunder of thousands of hooves and the fierce wind swallowed their conversation before anyone else could hear it.

“You idiot.”

“U-Uncle.”

“I won’t say it twice. Keep your mouth shut if you want to live.”

“I-I understand.”

Leaving the trembling young man behind, the middle-aged man kicked his horse into a faster pace, his cold expression unchanged as he sighed inwardly.

The kid probably didn’t know.

He had no idea what a careless, stupid mistake he’d just made.

Nor that if those words—practically taboo within the Black Dragon Demon Gate—made their way up to the higher-ups, passed from one person’s mouth to another’s ears, he’d lose his life in vain.

*Maybe he’ll never know.*

It takes quite a while for a person to mature.

But the war that came out of nowhere—and the enemies—would take that time away before it could run its course.

The middle-aged man’s eyes sank into thought as he considered the battle about to begin. Then his body flinched.

*What was that?*

An inexplicable sense of déjà vu seized him for an instant.

He hurriedly turned his head to look around, but in the end, he couldn’t figure out where the feeling had come from. He had to refocus on his duty.

He never realized that two pairs of eyes had swept over him from more than thirty yards away.

“Hyah!”

The fine horse raced on, breathing hard.

The young man, who had only just come back to his senses, hurried after the middle-aged man as his face turned deathly pale.

“W-wait for me!”

* * *

One person speaking alone produced only speech. Ten voices became a shout, and more than a hundred became a roar.

Yet even as three thousand men and horses raced in the same direction, the conversation between father and son carried clearly to each other’s ears.

“There are a lot of faces I don’t recognize.”

“That’s how things turned out.”

“And a few who look useful, too.”

“Even when you scrape together mud in a hurry, you can find a pearl or two. Though they can crack easily over nothing.”

The son knew what his father meant by that last remark, and fell silent. His father didn’t miss it.

Just as always. Just as he always had.

“Are those people bothering you?”

At the Black Night King Sima Gong’s quiet question, Sama Pyo—who’d been silently watching the road ahead—spoke.

“I don’t know what you mean.”

“After seeing the sights of the Central Plains, you’ve gotten better at playing with words.”

“There wasn’t much worth seeing. Maybe bad luck was following me. Everywhere I went, I found a sea of corpses and blood. Though I’m sure you already knew that.”

“Yes, I heard the reports. But for some reason, the messenger pigeons stopped returning one day, and I had to take matters into my own hands. The distance made it difficult to get information in time, and the Inner Hall Master had quite a hard time of it.”

“It couldn’t be helped. Yunnan wasn’t exactly a good place for sending messages back and forth.”

“I’m not scolding you. Your father knows well what happened at the Nanman Beast Palace, too. But…”

Sama Pyo listened in silence.

He hoped his father’s next words would be what he wanted to hear.

But it didn’t happen.

As always, not this time either.

“Why didn’t you send a missive after that?”

“A missive…?”

“Yes. I understand you had several chances even after leaving Yunnan. In the Imperial Capital, and at the Jin Family of Taiyuan. Am I wrong?”

What was he supposed to say?

His mouth felt gritty, as if he’d chewed a fistful of sand. Sama Pyo felt the wind battering his whole body and spoke.

“You’re half right and half wrong.”

“What?”

“In the Imperial Capital, I had to hide my identity and even disguise myself to avoid the eyes watching me. The journey there wasn’t smooth, either. And once we entered the Imperial Palace, things only got worse.”

Sima Gong studied his son’s profile.

As if he meant to find even the tiniest crack.

“Go on.”

“Things didn’t improve right after the incident in the Imperial Palace was over. We had to remain inside the palace for a short time, and then we had to head straight for Shanxi without getting proper rest.”

“I was under the impression that you suffered no serious injuries in Shanxi, unlike at the Imperial Palace. Am I mistaken?”

“You’re right. That’s when I was finally able to receive the missive from our sect.”

“Then you certainly saw the order.”

“Yes. I saw it. There’s no doubt.”

At that answer, given without even a hint of hesitation, Sima Gong’s eyes sank deeper.

“The Fire King and his Disciple were supposed to go to Qinghai, not here. Was that what the order said?”

“It was.”

“It said our sect was in danger, and that you, at least, were to return to Gansu by any means necessary. Was that right, too?”

“Exactly.”

“Then, lastly—do you have a proper reason or justification for seeing my seal and still not carrying out the order?”

At that moment, Sama Pyo turned his head and looked his father straight in the eye.

“No.”

“……!”

“I won’t make excuses. I won’t give you any reason. I failed to carry out the order properly, so I’ll accept whatever punishment I deserve. Please forgive me.”

Sima Gong fell silent for a moment, surprised by the son before him.

Then the brief silence between them was broken by the low laugh that slipped from Sima Gong’s lips.

“Ha. Hahaha.”

None of the men surrounding the two of them like a guard reacted to the sudden laughter.

They were all Peak masters, the Black Night King’s loyal hands and feet, but before their lord they were little better than the blind and deaf.

Sama Pyo was different.

He watched his father with calm eyes.

The laughter abruptly stopped, and a voice filled the silence.

“Pyo. My son.”

The voice at his ear was soft as silk, but the eyes revealed between those lips were sharp as blades.

“If you dared to lie to my face—if you did…”

His voice trailed off before he could finish, fading as Sima Gong’s eyes curved into crescents.

“Only now do I realize how right I was to send you to the Central Plains.”

Pat. Pat.

Perhaps it was the wind sweeping across the open plain.

With an unusually cold hand, Sima Gong patted his son on the shoulder and spoke with satisfaction.

“You’ve grown. Very well.”

With that, he turned his horse and rode away. His son simply watched his father’s back in silence.

“Take care of those two from a moment ago.”

Sima Gong had decided the fate of the two nameless martial artists with a single sentence, for a careless remark they’d made, however briefly. Sama Pyo watched until his father had completely disappeared from view.

Then Taishan came over—an old friend who had been as steady as the mountain he was named for since childhood—and asked in a trembling voice,

“M-My lord. Are you all right?”

At Taishan’s worried question, Sama Pyo answered calmly.

“Yes. I’m fine.”

It was strange.

Why did his chest feel so tight as they rode across this vast plain?

Why did a few faces flit through his mind beneath the gray sky stretching over everyone?

But Sama Pyo didn’t turn his horse around.

The place he belonged now was the Black Dragon Demon Gate, not the Fire Dragon Pavilion.

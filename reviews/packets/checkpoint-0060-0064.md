# Checkpoint Review — 60–64

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

# Chapters 60–64

## Plot

At Eight Spring Gorge, Taekyung and the reconnaissance squad surround the Head Elder, but his Finger-Flicking Technique kills numerous allied martial artists. Jin Wikyung arrives and joins the assault. Taekyung uses One Flash to destroy the Head Elder’s arm, while the elder cuts apart Wikyung’s ancestral sword and reveals that his betrayal grew from revenge for an old Great Faction War disaster.

The wounded Head Elder forms Sword Force for a final attack. Lee Cheonbaek ambushes him with a dagger, giving Taekyung the opening to finish him with One Flash. Lee dies from the effort. The System records the defeats of Lee Cheonbaek and Jin Baekyang, completes the Traitor Chain Quest, grants Taekyung multiple level-ups and increased Fame, and awards him the Sleeping Dragon of Shanxi title. The First Elder dies after warning Wipeng about Dark Heaven, and the surviving black-clad forces surrender.

Dark Heaven then appears on the cliff. Its agent kills Jin Chung and the Gunggwimun disciples who stayed behind, explaining that Dark Heaven rescued the conspirators from the Demonic Cult decades earlier and implanted gu in their heads. The agent deliberately spares Taekyung.

Five days later, rumors credit the Sleeping Dragon of Shanxi with the Jin Family’s victory. Mount Heng Sword Sect is collapsing after Lee Seogeun and Lee Cheonbaek’s deaths, and its First Young Master is killed by bandits. Jin Mukyung, the Heaven Shaking Sword and Taekyung’s lookalike second older brother, returns after three years at Heaven’s Gate Temple. Taekyung reaches Level 50, advances the Jin Family’s Cultivation Technique to the Eighth Stage, and gains 100 unassigned points.

Mukyung immediately tests Taekyung with the Reformation Fist and grappling techniques. Despite using no internal energy, Mukyung overwhelms him. Taekyung spends ten of his points on Agility, briefly reads Mukyung’s movements, and is struck again. Their spar remains unresolved.

## Continuity

- Jin Baekyang, the former Head Elder, is dead. Lee Cheonbaek died helping Taekyung defeat him.
- The Eight Spring Gorge battle is over; the black-clad conspirators surrendered after the Head Elder’s death.
- The First Elder is dead after naming Dark Heaven. The Second and Third Elders are dead. Wipeng and the surviving senior members’ subsequent fate is unresolved.
- Dark Heaven rescued the conspirators from the Demonic Cult, implanted gu in them, and is pursuing a larger plan. Its agents, purpose, and reason for sparing Taekyung remain unresolved.
- Jin Chung and the Gunggwimun disciples who stayed with him were killed by Dark Heaven.
- Taekyung is Level 50 with Fame 1,180, fifteen years of Internal Energy, and 90 unassigned points after spending 10 on Agility. His four Titles include Sleeping Dragon of Shanxi, Scion of a Prestigious Family, Novice Trainee, and Gambler.
- Sleeping Dragon of Shanxi is a Peak-grade Title granting All Stats +10 and Fame +100.
- Taekyung’s Jin Family’s Cultivation Technique is at the Eighth Stage, but his Internal Energy remains fifteen years because accumulation is slow.
- Jin Mukyung is twenty-three, the Heaven Shaking Sword, a Peak-level martial genius, and Taekyung’s second older brother. He studied at Heaven’s Gate Temple in Henan for three years and is far stronger than Taekyung.
- Taekyung’s spar with Mukyung remains unresolved.
- Mount Heng Sword Sect is near collapse; Lee Seogeun and Lee Cheonbaek are dead, and the First Young Master was killed by mounted bandits.

## Translation Decisions

- Preserve **Dark Heaven**, **Sleeping Dragon of Shanxi**, **Heaven Shaking Sword**, **Sword Force**, **One Flash**, **Reformation Fist**, **Peak**, **Eighth Stage**, **Qi Circulation**, and **Internal Energy**.
- Use **gu** in italics at first use with the established footnote explaining its venomous-creature origin.
- Retain **hyung** for Taekyung’s address to Mukyung.
- Render 금나수 as **grappling technique** rather than assigning an unsupported proper name.
- Keep **Captain of the Gatekeepers**, **Gunggwimun**, **Heaven’s Gate Temple**, and **Mount Heng Sword Sect** consistent with prior chapters.

## Durable state

{
  "active_continuity": [
    "Jin Mukyung is Taekyung's second older brother, twenty-three years old, the Heaven Shaking Sword, and a Peak-level martial genius who studied at Heaven's Gate Temple in Henan for three years.",
    "Jin Mukyung is stronger and more skilled than Taekyung and can overwhelm him while using the Reformation Fist without internal energy.",
    "Taekyung has one hundred unassigned points from ten level-ups and spent ten on Agility during the spar with Mukyung."
  ],
  "continuity_sources": [
    64
  ],
  "open_questions": [
    "The outcome of Taekyung's spar with Jin Mukyung remains unresolved."
  ],
  "safe_through": 64,
  "temporary_decisions": [
    "Use Reformation Fist for 갱생권.",
    "Render 금나수 as grappling technique.",
    "Retain hyung for 형 in Taekyung's greeting."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 60

# Chapter 60

The Head Elder thought,

*Have I lived too long?*

The Murim he remembered was not like this. Martial artists were not like this.

Ganging up was shameful, ambushes were condemned, and anyone who got so much as dirt on their back became a laughingstock.

And yet…

“Throw dirt! Keep throwing it!”

In eighty years of life, he had never seen anything like this. What? Throw dirt?

It was a cheap, cowardly trick even the Demonic Cultists he had fought like sworn enemies decades ago had never used.

*Is that bastard really a martial artist?*

What left him even more speechless was the reaction of those so-called subordinates.

“Squad Leader’s orders! Throw dirt!”

“Open the distance! Watch the Sword Energy!”

Watching them obey without a word made him dizzy.

*Have I ever seen bastards this fit to die?*

These were not martial artists.

No, they were not even human.

This was an insult to martial artists—and an insult to the Head Elder himself, who had given his whole life to the sword.

“How dare you…”

He was drawing his sword when it happened.

“You idiots!”

A stern shout burst out half a beat sooner. A young man whose face was swollen as if bees had stung him swept a fierce look around them.

“What the hell do you think you’re doing?”

He looked ridiculous, but he had real mettle. Yes. That was how a martial artist was supposed to act.

*At least there’s one decent one here.*

The Head Elder was just nodding to himself when—

“Think dirt’s going to cut it? Mix in rocks too!”

“…!”

The Head Elder shuddered like a man struck by lightning.

In a humiliation he had never felt in his life, he even forgot to swing his sword as a clod of dirt flew at his face.

Splat!

He could say this without hesitation: looking back on eighty years, he had never taken a hit so humiliating, or so completely undefended.

Through the dirt pattering down, he spotted a chunk of stone mixed in nice and solid.

“Uh-heh, uh-heh-heh-heh.”

The Head Elder laughed like a madman.

Then the laugh cut off.

At the same time—

Tssssss.

Sword Energy surged up, loaded with sixty years of internal energy.

“Are you prepared?”

Jin Taekyung watched and muttered,

“Shouldn’t have mixed in the rocks…”

The words were barely out before the Head Elder charged like a lion. The dozen or so sheep screamed and scattered.

“Scatter! Scatter!”

“Throw dirt too!”

Even while they ran, they did not forget to throw dirt.

* * *

Fwoooosh—

A fierce gale tore from the tip of the Head Elder’s sword. Sand, dirt, stones—whatever it was, it made no difference. In the face of that much power, it only shattered and scattered.

*How are we supposed to fight this guy?*

A head-on fight?

Calling us melee damage dealers was putting it nicely. Leave the reconnaissance squad on the Head Elder and they’d be dying in piles before I could blink.

I’d gotten attached to the bastards, though. I couldn’t let them die a pointless dog’s death.

“Squad Leeeader!”

That one deserved to die, sure.

*So why mix in rocks? The rocks.*

The Head Elder’s first target was Hyuk Mujin. Naturally. He’d thrown the first punch without a shred of fear.

I let out a long breath and threw myself toward him.

Shiiiiing!

I drove my spear at the Head Elder’s chest with everything I had.

At the same time, the Sword Energy about to cut through Hyuk Mujin’s back changed direction.

Shing.

That damned Sword Energy.

No time to check the spearhead, sliced off clean. I snatched terrified Hyuk by the scruff of the neck.

“Run!”

But the Head Elder was not the type to let go.

Swoooosh!

A tearing whistle through the air, and my side went hot. Even a graze ripped out a handful of flesh and sent blood spraying.

*Kh.*

It hurt like hell. In this situation, though, even a scream was a luxury.

*I need to buy time.*

I shoved Hyuk aside and turned. The Head Elder raised an eyebrow at that.

“You?”

Only one word, but the meaning came through perfectly. *The likes of you, stopping me?* That was the idea.

I answered like I was calm.

“Yeah. Me.”

“Don’t you value your life?”

“If I say it’s damn precious, will you let me live?”

“Heh heh. Look at this one. Young as you are, you’ve got quite a mouth.”

“Gramps, does your pepper still stand?”

Tssssss.

It stood ramrod straight.

Large, beautiful Sword Energy.

“…You’re still going strong.”

My grip on the spear went slick with sweat.

*I’m going to have to shake out every last reserve I’ve got to survive this.*

I had a lot more secrets than the Head Elder knew.

Attacks that used my Inventory.

A Skill that dumped several times my strength into a single blow—One Flash.

*I never showed them, just in case something like this happened.*

Was this what they called a last-resort technique in Murim?

One thing was certain: neither the Head Elder nor anyone else in Murim would see it coming.

And on top of that…

“Encircling formation. Form up.”

Shff.

Hyuk Mujin and the reconnaissance squad began closing in from every side.

A flimsy net for a fish as big as the Head Elder.

But with a sharp harpoon, it was a fight we could try.

“You think this will be enough?”

“To catch one old man? This is plenty.”

The Head Elder smiled like he was entertained.

“What a fearless brat. The kind who only comes to his senses after a beating.”

But that wish of his did not come true. A voice cut in out of nowhere.

“I think I heard you wrong. Say that again.”

A mountain of a man with fierce, piercing eyes. The voice from between his thick lips was cold as ice.

“You were going to lay a hand on our boy?”

Fwoooosh.

Sword Energy climbed his blade like wildfire and pointed at the Head Elder.

Jin Wikyung, appearing like a savior, winked at me.

“Well? Big brother looks cool, doesn’t he?”

Still the same.

* * *

The first time I had seen that face in a month.

The moment Jin Wikyung appeared, the tension in my body melted away.

I was glad.

Just glad.

*Thank goodness he’s alive.*

Wikyung was covered in blood, like he’d just come through a brutal fight. Large and small wounds showed through the tears in his clothes.

But that was enough. The fact that he was alive was what mattered.

*I have a lot I want to say, but it can wait.*

A reunion after this war ended would not be too late. Wikyung seemed to think the same. He looked forward.

Where we were looking, the Head Elder slowly spoke.

“The fact that you made it this far means…”

Jin Wikyung’s chilly voice cut him off.

“The Second and Third Elders are dead. The First Elder is only a matter of time.”

Good news. If Wikyung put it that way, the Elders had been no small part of this war—and the Head Elder’s hands and feet had just been cut off.

“Did the two of them… go peacefully?”

“Probably.”

The Head Elder nodded readily.

“They were always saying they wanted to die fighting like martial artists. They got their wish, so that’s fortunate.”

“They’ll be remembered as traitors, not martial artists. Every last one of you.”

“History is written by the victors.”

The Head Elder pointed his sword at us. Even with dozens of people in front of him, including me and Jin Wikyung, he stood there utterly composed.

“Now, let’s see who the victor is.”

Jin Wikyung looked like he had something to say. His mouth opened, then shut tight.

The next moment, a thunderous roar burst from him.

“Strike down the rebels!”

Shing. Shrrring.

Dozens of weapons drawn at once, all aimed at a single man. It was quite a spectacle.

“Yes, sir!”

With a huge shout, dozens of martial artists charged as one mass. I was no exception. My grip tightened on the spear, and my chest felt ready to burst.

*We can win. No. We win, no matter what.*

A full-on brawl with no formation to speak of. But we had Jin Wikyung, a Peak master, and dozens of martial artists following him.

*And there’s me.*

The Head Elder had trusted his own strength too much. He had thrown every man into the front line without leaving even a minimal escort, and now the black-clad men were pinned down by the combined assault of the Jin Family of Taiyuan and the Mount Heng Sword Sect.

The Head Elder…

dies right here.

*It’s over!*

It did not take long for that certainty to shatter to pieces.

Shushushushush!

Dozens of tiny points shot out of nowhere. They cut through the air faster and harder than anyone had expected.

“Finger-Flicking Technique!”

Jin Wikyung’s shout. I was not given time to think about what that even was.

Pow-pow-pow-pow!

Clang!

“Aaargh!”

“Guh!”

Some went down. Others knocked the shots aside. The ones who fell did not get up again.

*Don’t tell me…*

It had lasted only an instant, but I saw it clearly. Tiny points packed into the area around their hearts and across their faces like buckshot.

*Stones?*

They were closer to fragments now, but they had definitely been stones. Stones that could not take the Head Elder’s internal energy had shattered as they were fired at us.

*Is this possible?*

I got goose bumps, but it was not over.

The Head Elder was stretching a hand this way.

“Scatter!”

This time Wikyung and I shouted together. The martial artists, already wound tight, scattered in an instant.

*Good. We weren’t late this ti—*

The relief lasted only a moment.

Swoooosh!

What shot at us this time was not the Finger-Flicking Technique. It was the Head Elder. He drove in among the martial artists and went berserk like a wild beast.

Slash. Slash. Slash.

“Grrk.”

“Hhk.”

Every time a sword flashed through the dark, another life went out. Wherever the Head Elder tore through, only stifled screams and corpses were left.

“Head Elder—!”

Jin Wikyung charged in a fury. By then the Head Elder had already finished five people. And still not a drop of blood on that white face, enough to make you think of a ghost.

“You’ve come?”

“How dare you!”

“You’re all clumsy. Peace must have lasted too long.”

There was one fact you could not deny. The Head Elder was a hero of the Great Faction War.

He was stronger and more seasoned than anyone here. A Peak martial artist finished in countless real fights.

Shiiiiing!

The Sword Energy Jin Wikyung drew out stabbed through empty air. The Head Elder slipped it with nothing more than a slight tilt of his head, then flicked a finger.

The target was me.

Shhk!

I could not see a thing. Instinct knew anyway.

*Internal energy.*

That was literally a lump of qi itself. I rolled without wasting a beat.

Pshk.

“Guh.”

I should have blocked with the spear, but the attack was too unfamiliar to think that far. The price was an unnamed ally’s death.

I felt rotten.

“Naryeotagon? What a donkey of a man.”[^1]

I spat out the dirt that had gotten in my mouth.

“If you want to live, what won’t you do?”

“Haha. You’ve already become a proper man of Murim.”

Clang! Clang-clang-clang!

Had anyone ever seen a monster like that. Even while talking, he knocked aside every last bit of Jin Wikyung’s Sword Energy. I was speechless.

Thud!

Even then, a fist loaded with internal energy smashed the skull of a martial artist who’d gone for his back.

“You’re still twenty years too early.”

The fight had barely started. Not even the time to drink a cup of tea had passed, and already nearly twenty martial artists had turned into cold corpses.

“You bastard!”

Shiiiiing!

A middle-aged warrior whose face looked vaguely familiar lost his head to Sword Energy.

“Die!”

Boom!

A young man with a baby face that might have been twenty had his chest caved in and dropped to his knees.

Not NPCs. Real people.

Faces I had run into at least once at the Jin Family of Taiyuan. Faces I had shaken hands with. I gritted my teeth at that.

*I’m sorry.*

I was not apologizing because I lacked the power to stop it. I was apologizing because I had used their deaths.

Shhk!

Another person dropped to the Head Elder’s Finger-Flicking Technique like a puppet with its strings cut. But the corpse that looked about to topple backward popped up like a roly-poly toy. Then it pitched toward the Head Elder.

“Cheap trick!”

Boom! Bang!

With one hand, the Head Elder took Jin Wikyung’s sword. With the other, he sent a palm strike at the corpse.

And then…

*Now.*

I had hidden behind the corpse as it sailed through the air. I thrust my spear.

“One Flash.”

The next instant—

Goooooong.

There was a roar that stuffed the ears.

[^1]: *Naryeotagon* is a martial-arts term for dropping and rolling on the ground to evade an attack; the Head Elder’s remark also compares Taekyung to a donkey.
## Chapter artifact 61

# Chapter 61

Gooooong.

The Head Elder felt the air tremble. In the same instant, he understood how much destructive power the spearhead shooting toward his chest carried.

*This is… dangerous.*

A threat to his life he had felt only a handful of times. Every hair on his body stood on end, and the world slowed.

Shiiiiing!

Jin Taekyung’s spear came from the front, while Jin Wikyung’s sword flew in from behind. The two brothers’ pincer attack meshed with perfect timing.

A truly life-or-death moment.

Fwoooosh.

The sixty years of internal energy coiled in the Head Elder’s dantian spread through every limb and bone. It poured vitality into his aging muscles and woke his blood vessels. The change did not stop there.

Tssssss.

The Sword Energy that had risen nearly a foot—thirty centimeters—compressed to half its size.

That was not a loss of power. It was condensation.

The Sword Energy that had fluttered like a thread wrapped the entire blade and took the shape of another sword.

Sword Force.

The symbol of the superhuman masters who had broken through the wall of the Peak realm and opened a great new domain.

It was still incomplete, only half-formed, but it was unmistakably Sword Force—the distilled essence of the martial arts the Head Elder had spent his life mastering.

Shhk.

Even the Jin Family of Taiyuan’s ancestral treasure sword was cut apart, Sword Energy and all. Jin Wikyung’s internal energy scattered in an instant, and his insides were wrenched. His face went pale.

One stroke would have been enough to take his neck.

But the Head Elder had no time.

Shwack!

He reached for the spear now almost at his chest. His wrinkled hand, too, was wrapped in a dazzling radiance of qi.

This, too, was an incomplete Hand Force, but it was enough to stop Jin Taekyung’s spear.

No. It looked like enough.

Kraaaaaash!

Until the vortex spilling from the spearhead swallowed him whole.

* * *

A deathly silence settled. It felt as if the dozens of people here—or perhaps everyone standing on the battlefield—were watching us.

No.

Not us.

One man.

“This…”

At the end of countless gazes, the Head Elder slowly opened his mouth.

“What form was that?”

I answered.

“One Flash.”

Even speaking the words brought on a vicious hunger. Every muscle in my body stung, and not a scrap of internal energy was left inside me.

But that was all.

Unlike with Jopil, I didn’t pass out or crumple pathetically to the ground.

*My body can handle it now.*

I had grown enough to take One Flash’s side effects. And as much as I had grown, One Flash’s power had grown with me.

The Head Elder’s current state was proof of that.

“One Flash. One Flash…”

He muttered it under his breath and pressed an acupoint on his shoulder.

The bleeding stopped, but that was all. The arm ground to nothing by the vortex One Flash had unleashed did not come back.

“I never thought I’d end up one-armed at this age. Heh heh.”

The Head Elder gave a hollow laugh and turned toward Jin Wikyung.

“You’ve got a frightening younger brother.”

Jin Wikyung asked, his face wan,

“Does that child frighten you?”

“What about you?”

“I’m proud of him.”

Not a hint of hesitation. A smile bloomed over his pale face.

“I raised him like gold and jade, but he grew into steel. That’s the kind of child Taekyung is.”

The Head Elder stared at that smile.

“You’re a fairly impressive talent. Enough to shoulder the future of the Jin Family of Taiyuan.”

“Am I?”

“But not as much as your younger brothers.”

Jin Mukyung reaching the Peak realm at twenty was one thing. Getting ranked that high myself was almost more than I could take, but…

*What is he getting at?*

As if he’d read my mind, the Head Elder went on.

“Power is what you don’t even share with your own blood. When that time comes, will you still be so proud of your younger brothers?”

The air around us went ice-cold in an instant.

Everyone facing the Head Elder at close range belonged to the Jin Family of Taiyuan. Cautious looks clung to my cheeks, then quietly slid away.

*Family Head? I have no intention of doing anything like that, you bastards.*

That was when Jin Wikyung spoke.

“So that was it.”

Bitterness and relief both sat in his voice. The Head Elder’s brow twitched.

“What are you talking about?”

“The reason you betrayed us. The reason a day like today happened.”

“…!”

The Head Elder’s trembling eyes answered for him. I sighed inwardly.

*So that was what this was about.*

A succession fight.

It felt like a huge puzzle piece had clicked into place. The smaller pieces that still hadn’t found their spots were fitting together one by one through their conversation.

“What happened?”

Jin Wikyung asked in a respectful tone.

The shift was so natural no one else there even noticed.

“Do you know anything about your grandfather?”

“I’ve heard nothing. Father never said a word about him.”

“He was a cold man. Toward his children, and toward his only younger brother. And…”

The Head Elder gave a dry little laugh.

“He was a petty man. For a lot of reasons, we brothers, who had once been close, drifted apart. And then that happened.”

“The Great Faction War.”

“Have you heard of the Ten Myriad Demonic Forces? They came in endless waves. The Murim Alliance was formed, but it was only an alliance of the Nine Sects and One Gang, and they were too busy defending their own bases.”

That was also when the Head Elder had begun making a real name for himself.

Under the Jin Family of Taiyuan’s banner, he rallied Shanxi’s martial artists and finally drove out the Demonic Cult’s forces.

“The last battle was right here, at Eight Spring Gorge.”

His gaze seemed to grope toward some distant point in the past.

“It was a long war. Many people died, and everyone was exhausted. But there was hope, too. Hope that they could finally return to their families. The three hundred volunteers sworn to die all shared that same hope.”

“In the end, you won a great victory.”

Three hundred against three thousand.

The result was the Demonic Cult’s annihilation.

It was a glorious victory, and the reason the Head Elder was still remembered. Everyone had believed that without question.

Until just now.

“There was an ambush.”

*What?*

“We fought as we fell back deep into the gorge, but we were hopelessly outnumbered. Even as I swung my sword like a madman, one question would not leave me.”

The Head Elder’s voice was unnervingly calm.

“How could they have set an ambush in advance? My elder brother should have been blocking the road into Eight Spring Gorge.”

“…!”

Silent shock spread through the crowd. What little color was left in Jin Wikyung’s already pale face vanished.

“The battle lasted half a day. We fought waiting for reinforcements that never came, and it was useless. Of the three hundred volunteers, only eight survived. When we finally returned to the family, I have never been able to forget the look on my brother’s face when he saw me.”

“Is that… true?”

“Enough time has passed for mountains and rivers to change several times over. Did you think I came this far on mere suspicion?”

Decades were more than enough to turn suspicion into certainty. The Head Elder laughed hollowly.

“My brother turned the war into an opportunity. I became a hero on the battlefield, but he became Family Head. Everyone who had followed me either died in battle or vanished afterward.”

“Then going straight into the Elder Council—was that why?”

“Because that was the only way he would feel at ease. The only way I and my people could stay alive.”

*My people?*

I thought back to what he had said. The eight survivors who had followed the Head Elder and lived to the end.

Guessing who they were was not hard.

*The Elders and the Sect Leaders of the Five Gates of Shanxi.*

The survivors had sworn revenge. Revenge on the Family Head and the family that had betrayed them.

The Head Elder slowly swept his gaze over the crowd.

“It had been a very long wait.”

Silence swallowed them. Disbelief, shock, shame. The feelings differed, but no one could easily speak.

Well. No one except me.

“You sure dragged that bullshit out.”

“…!”

I couldn’t hold back the little snorts of laughter leaking out of me.

I had listened all the way through to see where this was going, and this was what I got.

“In the end, you’ve only got one goal.”

I flicked my thumb at the Head Elder.

“Revenge, my ass. You’re trying to become this, aren’t you?”

“What did you say?”

“I’m right, aren’t I? Clear away everything in the way—the Jin Family of Taiyuan, the Mount Heng Sword Sect—and swallow Shanxi whole.”

“You insolent—!”

Had the old man swallowed a locomotive boiler? Oh, right. No trains here.

“Revenge? Sure. Fine, revenge…”

I picked at my ear and went on.

“But why now?”

This had happened a full forty years ago. Even counting the Head Elder’s age, he had waited half his life.

“How many of the people who stabbed you in the back are even still alive? There’s late, and then there’s this late. And please, I’m begging you—don’t start with that bullshit about a gentleman waiting ten years to take revenge.”

If holding out ten years made you a gentleman, did holding out forty make the Head Elder Jesus?

It was nothing more than a crazy old man’s self-justification.

“You run your mouth just because you’ve got one.”

“I did. What are you going to do about it?”

“Do you think you know everything?”

“Do I have to? After it’s gone this far?”

The question was so obvious I snorted a laugh and pointed at the battlefield.

A mountain of corpses, a sea of blood. Utter pandemonium. The scene in front of us was exactly that.

“That…”

The chill in the Head Elder’s eyes wavered. But only for an instant.

“I see. What more is there to say?”

He muttered it like a jab at himself, then raised his sword.

“Head Elder.”

Jin Wikyung’s lips moved, and that was all.

A fight that ended only when one side died. They had come too far to turn back.

“Come.”

I wasn’t about to decline.

“Attack!”

It was time to hunt the wounded beast.

* * *

I remembered the first day I saw the Head Elder.

A bearing and dignity that made his age meaningless. His white beard called an immortal to mind.

Fwoosh!

Of course, there were no immortals who mercilessly cut people in half.

*Even rotten, a prized fish is still a prized fish.*

Drenched in blood, he swung his sword without pause. Looks mixed with awe and fear poured toward him.

“Monster…”

He had lost an arm, but the Head Elder was still strong.

He just clearly wasn’t as strong as before.

*This is doable.*

Peak master or not, the martial artists here were the Jin Family of Taiyuan’s elite. Men who had fought across the battlefield under Jin Wikyung, skilled enough to have survived the earlier clash with the Head Elder.

Clang-clang-clang!

The Head Elder knocked aside blades driving in from every direction, his face darkening. In the old days, he would have cut down everything in his path with Sword Energy.

Proof that the internal energy that had once seemed like a spring that never ran dry had finally hit bottom.

On top of that, his aged body had reached its limit.

Shraaaak!

Sword wounds began to multiply across the Head Elder’s body. Unlike before, most of the blood was his.

*Now!*

I wasn’t about to miss that opening. The spear I drove with everything I had tore a handful of flesh from his side.

“Hk!”

Even through the pain, the Head Elder cut down a martial artist and charged me. He meant it this time; a faint Sword Energy gathered along the swinging blade.

But…

Shhk.

The Sword Energy scattered in a rising spray of blood. Jin Wikyung appeared behind the staggering Head Elder.

“I’d forgotten you were there.”

The Head Elder turned with a twisted face.

“Did my elder brother teach you to put a knife in someone’s back?”

“My family members are dying. Is a sneak attack really that important?”

“Aren’t you ashamed, as a martial artist?”

“I am the Lesser Family Head before I am a martial artist.”

“The Lesser Family Head, is it? Heh heh.”

Jin Wikyung looked at the Head Elder with a complicated expression.

“The tide has already turned.”

“So? Are you going to ask me to surrender?”

“Please stop this meaningless fight.”

The flow of the battlefield had been ours for a long time. But the black-clad men kept resisting stubbornly, and the screams and corpses still showed no sign of thinning out.

“You’re right. It may be a meaningless fight. But…”

The staggering Head Elder straightened his back. A sharp gleam was already flashing in his eyes, and a blade-like aura began to rise.

“We’ve come too far to stop.”

A last desperate struggle?

No. More than that. Someone suddenly came to mind.

Jopil.

The last sight of him as he was dying overlapped with the Head Elder now.

*Innate qi. He’s drawing up his innate qi.*

If internal energy was acquired power, piled up by circulating qi and taking elixirs, innate qi was the opposite. It was the root of the human body—life force itself, for all intents.

The Head Elder was staking his life to use it.

“Cough.”

He spat blood and raised his sword. His life was going out fast, but his sword shone more brilliantly than it ever had.

The moment I saw that overwhelming sight, a single word slipped out of me.

“Sword Force…”

It was instinct.

My heart pounded just from looking at it. I could feel a terrifying power that far outstripped Sword Energy.

And then—

“Yes. You were here.”

His red eyes, the capillaries bursting one after another, locked on me.

Jin Wikyung lunged to stop the Head Elder.

“No!”

But the Head Elder was already gone from that spot.

In a single step he compressed fifty feet and brought his sword down on me.

Whoooong.

*So this is how I die.*

An attack I couldn’t dodge or block.

I was dead. I was going to die.

But…

*I can’t die like this.*

I wrung every muscle in my body. The last scant handful of internal energy raced for the spearhead.

It was a final struggle, and a show of respect for the life I had lived so fiercely until now.

“One Flash.”

Shiiiiiiing!

The last strike, carrying every bit of strength I had left, shot forward.
## Chapter artifact 62

# Chapter 62

The world seemed to stop.

My heartbeat thundered in my ears, and I could see every last grain of dirt drifting through the air.

And then…

Whoooosh.

A flash of light.

The glow pouring from the Sword Force was beautiful—and precise. I could feel a destructive power in it that looked ready to split not only the spearhead, but my body itself, in two.

*It's over.*

I had done my best. It would be a lie to say I had no regrets at all, but that wouldn't change the outcome.

All I could do was smash into it with everything I had left.

Shwaaaak!

The spearhead tore through the wind. The Sword Force erased it.

That was the instant death came striding in.

Shreeeek! Thunk!

The Head Elder's eyes flew wide.

A freak of unknown identity had risen at lightning speed and driven a dagger into his dantian.

“You…”

“You should've struck a vital acupoint.”

It was an ambush no one could have expected.

Until a moment ago, he had been nothing more than one of the countless corpses scattered around us.

But he wasn't.

The freak had only been waiting, with extreme patience, for his moment—the moment he could avenge his child.

The Head Elder cried out like a scream.

“Lee Cheonbaek!”

“Kahahaha!”

The instant Lee Cheonbaek burst into maniacal laughter, my spearhead punched into his back.

It tore through flesh and bone, driving forward without resistance.

> **System**
>
> - You have defeated Lv. 75 Lee Cheonbaek!
> - Level up!
> - Level up!
> - Level up!
> - …
> - All status ailments have been recovered due to the stacked effect of the level-ups!

The change came at once.

My aching muscles, my heavy feet, my empty dantian—all of them swelled with new strength.

At the same time, I knew what I had to do.

*One Flash.*

Once more, a white vortex erupted.

Kraaaack!

* * *

A narrow escape.

Never in my life had those four syllables hit so close to home.

I had really died and come back. I'd even seen a vision of going through hell's immigration, sharing a passionate hug with King Yama, and snapping a commemorative photo together.

If it hadn't been for Lee Cheonbaek, that vision would have become reality.

*Good thing I saved him.*

I wanted to close Lee Cheonbaek's eyes so he could go in peace, but there was still work to do.

“So live a little nicer. Come on.”

The Head Elder let out a faint laugh at that. He looked horrific.

One Flash had swallowed his remaining arm, and it hadn't stopped there—it had punched a hole the size of a fist through his chest.

“What a nasty-hearted brat. Have you no manners toward a dying old man?”

“The old folks I know spend their later years enjoying their grandchildren's antics. They're not old bastards like you, running around trying to kill their own grandchildren.”

“Why, you brat! Play at being a grandson first, then say something like that.”

He laughed heartily. He looked hollow, and yet relieved, as if he had finally shaken everything off.

“Taekyung is a good kid. If you had opened your heart first, the two of you might have had a good grandfather-grandson relationship.”

The Head Elder turned his head.

Jin Wikyung stood there, sword in hand.

“Are you planning to stab me with that sword?”

“I'm considering it.”

“You'd better finish considering it quickly. I don't have much time left.”

His words were true.

Even now, as he talked as if nothing were wrong, blood poured like a waterfall from the severed stumps of both arms and from his lower abdomen.

On top of that, there was the backlash from drawing up his innate qi.

The fact that he was still alive felt like a miracle.

“You look like you're having a hard time.”

“No. I'm getting comfortable.”

The answer was firm.

“I was barely thirty when the Great Faction War began. After that, I never once rested easy—not even for a moment. No…”

The Head Elder went on in a strained voice.

“In truth, perhaps I've been tired for a very long time.”

I muttered, appalled.

“You did all that, and now you're coming out with this?”

“Taekyung!”

Jin Wikyung sent me a look of mild reproach, but the Head Elder did not seem offended. A breathy laugh leaked from behind the lips he had pressed shut.

“Puh-huh. Yes, you're right. Just think of it as a senile old man's bullshit.”

“Looks like it really is time for you to die.”

“Hey! You little brat!”

“What? It's not like I said anything wrong.”

The Head Elder watched Jin Wikyung and me bicker with a fading gaze.

“We had a time like yours too. Yes. There was definitely a time when we were like that.”

But he no longer had time left even to linger over those memories.

“Cough! Guaaack!”

The Head Elder staggered after vomiting what had to be a bowlful of blood.

He was at death's door. Every capillary in his eyes had burst, and the blood pouring from his body had long since pooled at his feet.

Anyone could see there was no hope left for him.

*He's really dying? That Head Elder?*

Everyone dies.

Hundreds of lives had vanished on this battlefield alone—perhaps more than a thousand.

But the Head Elder's death was something I had never even been able to imagine.

That was how overwhelming his martial prowess had been. It made his current state look all the more wretched.

And that only made me more curious.

“Why are you holding on this hard?”

The Head Elder answered.

“Because I want to tell those who left before me… that I did my best.”

“Regrets?”

“None.”

He smiled broadly and thrust out his chest.

“Finish it. With your own hands.”

I raised my spear.

Jin Wikyung wore a troubled expression, but he did not try to stop me.

Shhk!

A single gust of wind passed, and the Head Elder's knees—which had never seemed capable of buckling—touched the ground.

A peaceful smile rose on his wrinkled face.

At the final moment, his lips moved, but no sound came out.

That was all.

> **System**
>
> - You have defeated Lv. 95 Jin Baekyang!
> - Quest **Traitor** completed!
> - Your Level has increased greatly!
> - Your Fame has increased greatly!

For a very brief moment, silence fell.

Then a colossal roar erupted—unlike anything I had ever heard.

“The Sleeping Dragon of Shanxi, Jin Taekyung, has cut down the Blade of Flowers, Jin Baekyang!”

> **System**
>
> - You have acquired the Title **Sleeping Dragon of Shanxi**!

Dozens.

Maybe hundreds.

Everyone who had survived was shouting my name.

*The Sleeping Dragon of Shanxi.*

I rather liked my new name.

* * *

“Third Young Master Jin Taekyung of the Jin Family of Taiyuan cut down the Head Elder!”

“The Sleeping Dragon of Shanxi defeated the Blade of Flowers!”

“The Sleeping Dragon of Shanxi…”

Wipeng gave a faint smirk.

He was the wastrel Third Young Master who had never even been called an earth dragon.

But now, there was no denying it.

He was a sleeping dragon.

If he obtained the dragon pearl, he could roam the heavens.

“What do you make of it?”

The First Elder answered.

“Do you believe that?”

“Everyone is shouting that the Head Elder is dead.”

“That is because my lord wanted it that way. A mere Third Young Master killing him? It's laughable.”

“You can see that from here? Sharp eyes.”

“This is what comes of letting your attention wander. Hahaha.”

He was leaning diagonally against a heap of corpses.

A sword wound split him on a slant from about the shoulder to the waist, and blood poured from it in torrents.

“Surrender. If we treat you now, you can live.”

“No. This old man's end was decided long ago. A very painful death.”

Wipeng shook his head.

“I won't allow it.”

“My death does not require permission. Neither you nor even I can do anything about it.”

“What does that mean?”

Wipeng furrowed his brow, unable to follow, when—

“Beware Dark Heaven… Grrk.”

It happened in an instant.

Blood poured from all seven of the First Elder's orifices. His eyes rolled back, and his entire body convulsed.

“First Elder!”

By the time Wipeng hurried over, the First Elder's breath had already stopped.

Just as he had said, he had met a painful death. His face was twisted grotesquely.

*This is…*

*Poison? Or a restriction?*

There was no way to know yet.

Wipeng carved the single word that had become the First Elder's last deep into his mind.

*Dark Heaven. He definitely said Dark Heaven.*

The only clue the First Elder had left behind.

Wipeng stared at the dead man's face with complicated feelings, then turned away.

“I, Wipeng, cut down the First Elder!”

Despair spread across the faces of the black-clad men.

Faced with two paths—death or surrender—they chose the latter.

Clang. Clatter-clatter.

Weapons fell weakly to the ground.

It was the end of the war.

* * *

Where there were the dead, there were also those who had lived.

The Sect Leader of Gunggwimun,[^1] Jin Chung, was one of them. He had climbed to the top of the cliff before the battle began.

“How hollow.”

It had been a grand scheme to which he had devoted half his life.

The result was horrific.

The Head Elder he had served as his lord, the Elders he had called brother, and the Sect Leaders of the Five Gates of Shanxi had all died.

The survivors' last desperate struggle had ended as well.

Now, only he remained.

*So this is how it ends.*

Jin Chung turned around.

Fifty martial artists of Gunggwimun were waiting for his orders.

“Leave.”

An invisible stir ran through them.

One of the nearest martial artists spoke cautiously.

“Sect Leader, what do you mean…?”

“This fight is already over. I will not force you to sacrifice yourselves. Leave by this road. Scatter as widely as you can and get out of Shanxi. If you do, you may at least save your lives.”

The martial artist nodded resolutely.

“I will follow you until I die.”

“I… will remain here.”

“What?”

The confusion lasted only a moment before the martial artist's voice began to tremble with feeling.

“Is it because of us?”

“Not at all.”

Jin Chung answered firmly, but his thoughts were different.

*If I followed them, the Jin Family of Taiyuan would hunt them relentlessly.*

The Five Gates of Shanxi were many, yet one.

One, yet many.

They had been created for the same purpose, but each sect had raised its martial artists in a different way.

Jin Chung had not raised them as weapons.

He had taken them in as disciples.

“Sect Leader!”

“Please lead us!”

Every one of them had been an orphan with nowhere to go.

For at least ten years—twenty or more in some cases—he had fed them, sheltered them, and taught them martial arts.

If the grand scheme had succeeded, they would have become the backbone of Shanxi's Murim.

Now that it had failed, they were nothing more than traitors.

“Do you not understand how this is going?”

“Even if we die, we will die with you, Sect Leader.”

“You brat!”

“Please allow us.”

The martial artist who had stepped forward first slammed his forehead against the stone floor.

Then, one by one, his disciples began to kneel.

Jin Chung looked up at the sky and lamented.

“If only the grand scheme had not been delayed. If only they had stepped forward!”

Talk of *them* was a secret known only to the eight at the top.

To speak those words aloud was no different from deciding to share his final moments with his disciples.

*This too must be heaven's will.*

Jin Chung turned his gaze from the dark night sky and helped the prostrate martial artist to his feet.

He felt endlessly sorry—and deeply moved—by the loyalty the man had shown.

“That's enough. Get up.”

At the warmth in his voice, the martial artist lifted his head.

He flicked his tongue over the trickle of blood running down his forehead, then gave a crooked grin.

“Yes.”

Thuck!

Jin Chung stared at the martial artist with a blank look.

The shock was so great he could not even feel pain.

*What in the world…?*

Shwaaak!

The martial artist pulled his hand from Jin Chung's chest.

A glow brighter than moonlight clung to it—a blood-red Force that inspired dread just to look at.

“You…”

“You already know, so why ask? Oh, and about what you just said—I'll give you a simple answer.”

The martial artist's smile deepened.

“Why would we step forward? Your role ends right here.”

Jin Chung's eyes flew wide.

*Them.*

The unknown beings who had never revealed themselves until the very end.

Dark Heaven!

“You bastards!”

“Don't look at me like you've been used. Forgotten who got you out of that hell alive?”

Jin Chung remembered the nightmare from forty years ago.

The corpses of allies covering the ground around him.

The endless army of the Demonic Cult surging in.

They had gathered around the Head Elder and prepared themselves to die.

That was before Dark Heaven appeared.

“We saved your lives and gave you a chance at revenge. What more did you want?”

He was right.

Dark Heaven had annihilated the Demonic Cult's army, then proposed a deal.

They had accepted.

They had to have a gu planted in their heads, but they would have done anything for revenge.[^2]

But…

“Wasn't your real aim to use us to rule Shanxi?”

“Well, maybe that was the plan at first.”

“Then what was it all for?”

The martial artist grinned.

“A bigger picture.”

At the same time, his bloodstained hand pressed against Jin Chung's chest.

Boom.

A small explosion went off inside Jin Chung's body.

The energy burst his eardrums, severed his blood vessels strand by strand, and reached his heart.

*Just like this…*

The thought went no further.

Jin Chung's body, already dead, flew like a bird and plunged off the cliff.

Shiiiiik! Crash!

The martial artist glanced down and grimaced.

“Ouch. That must've hurt.”

When he turned around, screams and blood were waiting for him.

Ten black-clad men who had appeared out of nowhere were massacring Gunggwimun's disciples.

“Let's finish this quickly and go.”

“As you command.”

Shreeeeek! Thud!

The martial artist turned his gaze toward the bottom of the cliff.

Screams erupted all around him, but below the cliff the air was filled with cheers and shouts.

“The Sleeping Dragon of Shanxi!”

“Jin Taekyung! Jin Taekyung!”

“The Sleeping Dragon of Shanxi…”

The plan had succeeded.

But Jin Taekyung's appearance had been a variable even he had not anticipated.

He did not like that.

*Take him out, or let him be?*

If he set his mind to it, he could rip him out by the roots.

His deepening gaze turned toward Jin Taekyung, ringed by cheers.

“Our youngest! My little brother!”

“Let go! Let go, you bastard!”

A snort of laughter escaped him.

*I'll let you live. For today.*

The martial artist turned away.

Some fifty corpses lay like a carpet in his wake.

[^1]: 弓鬼門, lit. Bow Ghost Gate.
[^2]: A *gu* is a traditional poison associated with venomous creatures; in Murim fiction, it may be implanted in a person's body.
## Chapter artifact 63

# Chapter 63

Creeeak.

The man entered the inn around early afternoon.

The old wooden door creaked, but no one inside turned to look. Not even the owner or the waiter, who should have been rushing to greet a customer.

“So? So what happened?”

“Quit keeping us in suspense and tell us already!”

At the crowd’s eager urging, the old man tapped his empty bowl.

Only after the owner filled it to overflowing with bamboo-leaf wine did the old man—the storyteller—go on.

“A fierce battle broke out. Blood Wolf Sword Lee Cheonbaek brought no fewer than thirty thousand men. Compared to that, the Jin Family of Taiyuan had only three hundred elites.”

“Thirty thousand!”

“My word, thirty thousand!”

“Does that make any sense? Mount Heng Sword Sect isn’t one of the Nine Sects and One Gang…”

The storyteller stopped mid-sip and spat the wine back out.

“Fuck this. This booze tastes like shit. I’m leaving. You can hear the rest from the guy who brought up the Nine Sects and One Gang.”

“Now, hold on. Why are you acting like this?”

“Who just said that?”

The mood turned ugly, and a young man was shoved back, half-stumbling.

Only then did the storyteller set his half-raised ass back down. His stomach had turned, and his nerve had thickened to match.

Tap, tap.

Everyone frowned as the storyteller tapped his empty bowl. Now they had to give him money, not more wine. They were in the middle of an unspoken standoff when—

Ting.

“Huh?”

The storyteller’s narrowed eyes flew open. A gleaming silver tael had come flying from somewhere.

“Well. Whoever that is, they’re a big spender.”

“Who was it?”

“Why are you looking at me? You want my wife to beat me to death?”

That was when someone spoke from behind the crowd.

“I’d like to hear more.”

The voice was quiet but resonant. It belonged to the man who had entered the inn earlier. His face was hidden under a bamboo hat pulled low, and the cloak wrapped around him was caked with dust.

*A martial artist.*

No one needed to say it aloud. Everyone in the inn had reached the same conclusion.

The storyteller looked from the silver to the man and swallowed.

“Thank you, Great Hero. Is there something in particular you’d like to hear…?”

In his experience, there was only a hair’s breadth between a ruffian and a martial artist. He was an old man who had lived his share of years, but he had no desire to get stabbed to death in a place like this.

Fortunately, the man in the bamboo hat was the latter.

“Keep it simple. Just the facts.”

Judging by the voice, he was clearly a young bastard—but a young bastard who had learned martial arts. The storyteller couldn’t treat him carelessly. He rubbed his palms together.

“I’ll tell you everything I know, sir. Every last bit.”

“That battle you mentioned. How many days ago was it?”

“Five days ago.”

“Who won?”

“The Jin Family of Taiyuan wiped the floor with them. I heard the Sleeping Dragon of Shanxi played a major role.”

“Then Mount Heng Sword Sect… What did you just say?”

“Excuse me?”

“Shanxi, what?”

“Ah, you mean the Sleeping Dragon of Shanxi?”

“That’s right. I’ve never heard that alias before.”

“If you’re from out of town, that would make sense. Young Master Jin only rose to prominence recently.”

“You mean Young Master Jin Wikyung, the Lesser Family Head?”

“What? Not at all. The Lesser Family Head is impressive too, but the one who played the biggest role this time was Young Master Jin.”

“So that Young Master Jin… Wait. Is the Sleeping Dragon of Shanxi somehow related to Third Young Master Jin Taekyung?”

“They’re the same person.”

The man, who had been silent until then, snapped his fingers. A second silver tael landed perfectly in the storyteller’s bowl.

“I believe I asked you to keep it simple and stick to the facts.”

“I’ll stake my balls on it.”

The man sighed at the storyteller’s resolute answer.

“Let’s say that’s true. What happened to Mount Heng Sword Sect?”

“They’re on the verge of closing their gates. Second Young Master Lee Seogeun was already dead, and their Sect Leader, Blood Wolf Sword Lee Cheonbaek, fell in battle. Two days later, even the heir—the First Young Master—was killed fighting a band of mounted bandits.”

“Mounted bandits?”

“These gutsy bastards heard the Blood Wolf Sword was dead and stormed Mount Heng Sword Sect. Word is they’d been circling nearby from the start, waiting for their chance.”

“What a dog’s mess.”

“A horse’s mess, more like. They’re mounted bandits, aren’t they?”

The inn went dead quiet. Everyone expected the big-spending martial artist to drive a third silver tael into the storyteller’s forehead.

Instead, the man rose from his seat without a word.

“I heard you.”

Even after the man left, the storyteller’s tale went on. They drank without pause, and the snacks never ran out.

Everyone joined in, talking about the struggle for supremacy among martial artists. Victory and defeat. The young hero who had risen like a morning star.

“It won’t be long before the Jin Family of Taiyuan steps beyond Shanxi and stands tall in the Central Plains. The Lesser Family Head, who excels in both civil and martial arts, the Sleeping Dragon of Shanxi, who rose to prominence this time, and… and who else was it?”

“Heaven Shaking Sword?”

“Ah, right. Second Young Master Jin Mukyung!”

“That young man is incredible too. They say he’s a martial arts genius who appears once in a hundred years, if that.”

“But where is he now? What’s he doing?”

“Dunno. At this hour, he’s probably asleep.”

Even as the drinking continued inside the inn, the man rode in silence. His mouth was firmly shut, but his ears were wide open.

“Did you hear?”

“The Sleeping Dragon again? My ears are bleeding. Give it a rest.”

“Yeah, but this is grade-one intel. I heard it from a gate guard of the Jin Family of Taiyuan.”

“What’s the fuss?”

“You know the Heavenly Axe?”

“The Heavenly Axe of the Eighteen Strongholds of Green Forest? That mountain bandit who’s supposed to be a Peak master?”

“That’s the one. Word is the Sleeping Dragon of Shanxi took him out too!”

“Isn’t that just a rumor? Why would someone like the Heavenly Axe come all the way to Shanxi to play bandit?”

“How would I know? What’s even more surprising is that Yama Whip was there too.”

“Yama Whip too?!”

“They say he’s disguised as a coachman at Honghwaru. If you ever have reason to go there, watch yourself.”

Two names came up more than any others in the endless chatter.

The Sleeping Dragon of Shanxi.

And Jin Taekyung.

The closer the man came to his destination, the more the rumors swelled like a snowball, growing larger and larger.

*The most handsome man of all time. A heaven-bestowed martial physique. A chivalrous hero who cannot stand injustice.*

The man in the bamboo hat spurred his horse. Hearing so much as the *Shan* in Sleeping Dragon of Shanxi made his stomach churn and his head ache, as if he had taken an internal injury.

He finally reached his destination the next morning.

*It’s been a while.*

The place he had returned to after several years was unchanged.

If there was any difference worth mentioning—

“Stop right there! I am the hegemon of Shanxi, Captain of the Gatekeepers of the Great Jin Family of Taiyuan, and the right-hand man of the Sleeping Dragon of Shanxi—Hyuk Mujin! State your identity and purpose, and—”

—it was that a guy who looked like hell was serving as Captain of the Gatekeepers.

The man in the bamboo hat, Jin Mukyung, sighed.

“Shut up and open the gate.”

* * *

Whoooosh.

The water flowed. Calm, and unimpeded.

The internal energy that had emerged from my dantian raced through hundreds of acupoints before finally returning to its rightful place.

Ding!

> **System**
>
> - You have successfully completed **Qi Circulation**.
>
> - The realm of the **Jin Family’s Cultivation Technique** has risen to the Eighth Stage.

I opened my eyes as I listened to the System notification.

*The Eighth Stage.*

It was clearly good news, but I couldn’t help feeling a little disappointed.

The notification I had been waiting for was a different one.

*Could’ve at least bumped my internal energy.*

Today marked two months since I had been able to use the System. Circulating my qi had become a habit, but my internal energy was still going nowhere.

*At this rate, it’ll take another ten years.*

The greatest strength of the Jin Family’s Cultivation Technique I had learned was its stability. Unlike ordinary internal cultivation techniques, I could even run it while moving.

The problem was…

*The accumulation speed is fucking terrible.*

For a martial artist, a lack of internal energy was a fatal weakness.

I could handle First Rate and Second Rate opponents easily enough, but if I ran into a Peak master as an enemy, even two lives wouldn’t be enough.

I had felt that clearly after tasting the Head Elder’s martial might firsthand.

*That old man was incredible.*

Even after five days, I still couldn’t forget it.

No. Forget five days.

Even fifty years from now, I would never forget that sight.

The Sword Energy and Sword Force that had swept across the battlefield. And that absurd number—Level 95.

*How long could I have lasted against him one-on-one?*

Even if I had wrung out every last ounce of strength, I doubted I could have held on for a minute.

But unexpected variables had overturned the result, and I had been able to drive my spear through his chest.

And the System hadn’t forgotten my reward.

“Open Status Window.”

Ding!

> **System**
>
> **Status Window**
>
> **Lv. 50 Jin Taekyung**
>
> **Class:** First Rate Martial Artist
> **Fame:** 1,180 (+150)
> **Titles:** 4 (Title effects active)
>
> - **Sleeping Dragon of Shanxi** — All Stats +10, Fame +100
> - **Scion of a Prestigious Family** — All Stats +5, Fame +50
> - **Novice Trainee** — Training Speed +10%
> - **Gambler** — Combat-related Stats +10% in one-on-one combat
>
> **Strength:** 135 (+15)
> **Stamina:** 142 (+15)
> **Agility:** 130 (+15)
> **Intelligence:** 25 (+15)
> **Charm:** 25 (+15)
> **Internal Energy:** 15 years
>
> **Remaining Points:** 100
>
> - Distribute your Remaining Points.

“Ohhh.”

I had checked that Status Window dozens of times over the past few days, but I never got tired of it. It felt like carbonation popping in my veins.

*Fighting the Head Elder was worth it.*

It had been a gamble with my life on the line, so the reward was stacked.

I had jumped thirteen levels in one stroke, my Fame had entered the triple digits, and my Titles had changed.

“Check Titles.”

Ding!

> **System**
>
> **Status Window**
>
> **Sleeping Dragon of Shanxi**
>
> **Grade:** Peak
> **Effect:** All Stats +10, Fame +100
> **Description:** Your fame has now spread throughout Shanxi. But the world is vast and masters are many. Never become complacent!

I wasn’t a nationwide name yet, but in Shanxi—my local district—I apparently had some real clout…

*So that’s why it’s called the Sleeping Dragon of Shanxi?*

Goyang’s Honey Fist. Incheon’s Sea of Blood. That kind of thing.

Either way, it was good for me. I had a solid new Title, and Family Shame, the tag that had clung to me until recently, was gone. It felt as good as having an aching tooth pulled.

*I’ve gotten stronger again.*

I suddenly remembered the conversation I’d had with Team Leader Choi before returning to Murim. I’d told him that the next time he saw me, he would have to revise my contract.

He had probably taken it as a bluff, but I had made it a reality.

*I’ll get as strong as I can, then go back.*

I would return with every scrap of power I could obtain.

Internal energy, martial arts, stats. Whatever it was, all of it.

On my next Logout, I’d be a B-rank Hunter—no, an A-rank Hunter—and return home in glory…

“Huh?”

No, wait.

I felt like I was forgetting something incredibly important.

*What is it?*

I stopped everything I was doing and tried to pin down that sense of déjà vu.

That was when—

“Is this the place?”

“Yessir. No mistake.”

Two voices murmured outside the door. The instant I recognized one of them as Hyuk Mujin’s—

Boom!

The door was ripped off its hinges with a thunderous crash.

* * *

I take basic common sense seriously.

Tissues go in the trash. Cigarettes belong in the smoking area. Porn comes from Japan.

And when you enter someone else’s room, you knock.

I especially believe that anyone who barges into a room a man uses alone, without knocking, deserves life in prison.

By that standard, the bastard in front of me got the death penalty.

Smashing the door earned him life. Speaking down to me on our first meeting was an aggravating offense.

I answered him politely.

“Yeah. I’m here.”

The bastard’s eyes went round. His face was black with grime, as if he had spent twenty years working in the Aoji Coal Mine.[^1]

Young. Shabbily dressed. The story practically wrote itself.

*Wandering Martial Artist #1.*

An extra who had come running after hearing of the Sleeping Dragon of Shanxi’s fame.

I turned to Hyuk Mujin, who was wearing a similar expression.

“What’s with this guy?”

Hyuk Mujin froze solid. He looked like he had seen a ghost.

“You don’t know him?”

“How would I know, idiot? You have to introduce people.”

Grumbling, I raised my Qi Sense. A blue circle stretched toward the two of them.

> **System**
>
> **Lv. ??? Jin Mukyung**

*Jin Mukyung. Guess he’s pretty high-level.*

“Huh? Jin Mukyung?”

I looked at the Level window once.

Then at his face.

I repeated that three or four times before approaching him with a trembling heart.

“Uh, hold on a second.”

“…”

Rub, rub.

My clean sleeve turned black. Beneath the grime, a handsome face emerged. I thought it looked familiar, then realized it was the same face I saw every morning when I washed up.

*Carbon copies.*

Heh.

I gave him an awkward smile. Wandering Martial Artist #1 glared back at me with icy eyes.

“Long time no see, hyung.”

[^1]: Aoji Coal Mine was a notorious coal mine in North Korea, associated with harsh working conditions.
## Chapter artifact 64

# Chapter 64

*Slowly. No need to rush.*

Jin Wikyung steadied his breathing. This was an important moment. He couldn't ruin everything with one mistake.

*I've done well so far. I just have to keep going like this.*

A bead of cold sweat slid down his cheek. But Jin Wikyung, exerting the utmost concentration, didn't feel even that.

His pupils contracted. His thin, trembling breath stopped.

*Now!*

It was the instant Jin Wikyung's eyes flew open and his hand shot out like lightning.

Bang!

“My lord!”

Wipeng burst into the study amid a thunderous crash and spoke with an urgent expression.

“There’s chaos outside… Why are you like this?”

A trembling voice escaped Jin Wikyung's lips.

“I was almost finished.”

“What?”

“I poured my heart into it for two hours. All for this moment.”

“I don’t know what you’re talking about, but that isn’t important right—”

“It is important!”

With a cry that sounded almost like a scream, he grabbed his hair.

“It was important! Who are you to decide that?”

Tremble, tremble.

Jin Wikyung looked so sorrowful and full of resentment that Wipeng forgot about the urgent situation and stared at his lord.

*I was too hasty.*

It had been five days since the war ended. Jin Wikyung had been suffering under an unprecedented workload because of the postwar cleanup. Of course he would be sensitive. It was clearly Wipeng's fault for making a normally generous man this angry.

“I apologize. I was too anxious and lost my head.”

Jin Wikyung's anger eased at Wipeng's sincere apology.

“Please be more careful next time.”

But even that couldn't do anything about the sorrow that seeped so deeply into his voice. Feeling even more guilty, Wipeng spoke.

“If there’s anything I can handle, I’ll help.”

“No use. The water’s already spilled. I have no choice but to start from the beginning.”

“I can draw it for you instead—what?”

Wipeng approached Jin Wikyung with a trembling heart. A huge sheet of paper completely covered the table.

“What is this?”

His voice was drier than desert sand, but Jin Wikyung didn't notice.

“I tried to transfer the battle from five days ago onto paper.”

“Not the battle. The Third Young Master.”

“They’re the same thing. Anyway, it was almost perfect. All I had left was to draw Taekyung's eyes…”

“I came in and ruined the brushwork.”

“No. Come to think of it, this is for the best.”

Jin Wikyung sighed.

“Heaven must not have permitted someone with my pitiful skill to portray Taekyung. Don’t you think?”

“…”

Wipeng silently picked up the paper.

Rip! Rip-rip-rip!

“No! My *Birth of a Hero*!”

“You even gave it a title?”

As he listened to the mournful scream, Wipeng pressed a hand to his forehead. Whenever—very occasionally—Jin Wikyung got like this, Wipeng felt like moving back to the countryside.

*Should I just open a martial arts school?*

Seeing his lord gather up the scraps of paper with a devastated expression made him feel even more desperate to retire.

“I was going to keep it in my private collection!”

“To hell with your private collection—you need to get outside right now.”

“Why?”

“Jin Young Master has returned.”

Jin Wikyung stopped picking up the paper and tilted his head.

“Has the youngest been somewhere?”

“Not that Young Master Jin.”

At the disbelief in Jin Wikyung’s eyes, Wipeng nodded.

“Yes. The Second Young Master has returned.”

“Mukyung!”

His face lit up. It was his second younger brother, back after three years. He wanted to run out and greet him immediately.

“All right. Where is he?”

“The Third Young Master's residence.”

“That Mukyung, who hated the youngest so much, went to find him the moment he arrived? Maybe he’s finally going to act like an older brother. He’s grown up. Hahaha!”

That was when Jin Wikyung let out a hearty laugh.

Rumble-rumble-rumble.

Suddenly, a thunderous crash shook the estate, followed by people's screams.

—The building is collapsing! Everyone, get out of the way!

—Call for people!

—The Third Young Master’s residence is collapsiiiing!

Jin Wikyung blinked.

“I think I just heard that the youngest’s residence collapsed.”

“Brothers grow up by fighting, don’t they?”

“What are you talking about… Surely—”

“It’s nothing. Just draw a new one.”

Wipeng answered with an expression of enlightenment and spread a fresh sheet of paper over the study table.

“I think this painting should be titled *The Hero Being Beaten Like a Dog by His Second Brother*.”

Whoooosh!

Using a Peak movement technique, Jin Wikyung dashed away like the wind. Wipeng watched his back disappear and sighed.

*Should I really open a martial arts school?*

His worries had only been growing lately.

* * *

Jin Mukyung.

Twenty-three years old. His epithet was Heaven Shaking Sword.

A martial arts genius who had reached the Peak realm at barely twenty.

But more important than that was the fact that he was this body’s—Jin Taekyung's—second older brother. So, naturally, I was curious.

*I can’t remember what Jin Mukyung—or rather, my second brother—was like.*

Amnesia was an excellent excuse. When I asked Jin Wikyung that question, he told me everything about him.

*You won’t be able to see him right away. He’s very far away.*

*Where is he?*

*At Heaven’s Gate Temple in Henan. That heartless brat hasn’t shown his face once in three years.*

His words were harsh, but Jin Wikyung looked proud.

He looked like a parent whose child had been accepted to Harvard.

*What’s his personality like?*

*Hmm. He’s kind. People often misunderstand him, but he’s definitely a good kid.*

*Were we close?*

*…We were. I think we were? Yes, we were close.*

*Ah. Right.*

I hadn't thought much of it at the time. Once I learned how far Henan was from the Jin Family of Taiyuan, I lost interest altogether.

*What, was I seriously going to still be in Murim by then?*

It was a distance that required several weeks of nonstop travel on horseback.

That was also why Jin Mukyung hadn't shown so much as the tip of his nose before the war ended. But…

*I never thought I’d meet him like this.*

His appearance was completely unexpected.

I gave him an awkward smile and held out my hand.

“Long time no see, hyung.”

The “hyung” who had been staring at me quietly took my hand.

“Yes. It’s been a long time.”

*This guy seems nicer than I expected.*

Just as Jin Wikyung had said, people must have misunderstood him because of his fierce eyes.

Thinking that eased my tension, and I was able to smile more naturally.

“How have you been?”

Jin Mukyung gave me a faint smile in return.

“More or less. But, youngest.”

“Yeah?”

“Your speech has gotten casual.”

Whoom!

The next moment, when I came to my senses, I was flying toward the wall. Jin Mukyung had thrown me with tremendous strength.

*What the hell?*

I twisted my body in midair. Then I lightly stepped off the wall and landed on the ground. Jin Mukyung watched me and gave a quiet snort.

“Well, well.”

I wasn't particularly fond of where this was going.

I scratched the back of my head.

“Weren’t we close?”

“We were. My fist and your body.”

“Ah.”

I was a lunatic for believing Jin Wikyung. Wasn’t he the type who absolutely doted on his younger brothers?

*Shit. He should’ve explained himself properly.*

Jin Mukyung extended his fist.

“This is your oldest friend. Say hello.”

“Hello.”

Unfortunately, his smile grew even wider.

“Our youngest has grown a lot. Acting cocky in front of your big brother.”

Whoooosh!

Jin Mukyung rushed forward like lightning and threw a punch. The air tore apart before his fist.

*He’s serious?*

No internal energy was behind the blow, but it contained incredible force.

I jerked my head aside in alarm.

Bang!

The wooden wall exploded. Fists rained down through the wooden fragments scattering in the air.

Bababang!

Face, chest, shoulder, stomach.

His attacks looked wild and random, but his movements were smooth, and his range of attack was as tightly woven as a net.

“Fist technique?”

“Been a while since you had a taste of the Reformation Fist, hasn’t it?”

*Fuck, what kind of name is that for a fist technique?*

As I cursed inwardly, the first form of the Reformation Fist slammed into my abdomen.

Whump!

“Hup.”

“It’s not over yet.”

I endured the pain that knocked the breath from me and blocked the incoming punch with my forearm. My bones throbbed at the dull impact.

“You blocked?”

Babababam!

It hurt. It hurt like hell.

Jin Mukyung had the advantage over me in every way—strength, speed, everything.

But how should I put it…

*It’s more manageable than I expected.*

Was it because he wasn't using internal energy?

At first, all I could do was take a one-sided beating. But after a little time passed, his attacks gradually began to come into view.

Whoosh!

Jin Mukyung's fist sliced through empty air. A precise prediction. A clean evasion.

He looked at me with an expression of surprise.

“You’ve improved quite a bit.”

I steadied my breathing and grinned.

Since things had come to this, I figured we might as well have a satisfying fight.

“Not quite a bit. A lot. Haven’t you heard the rumors?”

“I have. Until I’m sick of them.”

Jin Mukyung gave a quiet laugh.

“Then prove how much of them is true.”

Shwaaak!

With a sharp sound of air being split, his hand shot toward my wrist.

*Like hell!*

I widened my eyes and slapped the incoming hand away.

No, I tried to slap it away.

Tap, tat-tat-tat!

In a brief instant lasting less than a second, five attacks and blocks passed between us. And the winner was decided almost immediately.

Clamp!

“What the hell is this pathetic grappling technique?”

Jin Mukyung finally twisted my wrist into a painful lock with a strange movement, then spoke with an expression of contempt.

Being caught so helplessly had already made my stomach churn, but his next words set my chest on fire.

“Again.”

“…What are you trying to do?”

“I knew right away that the rumors were nonsense. Now I need to correct the habits of a little brother who doesn’t know his place.”

Jin Mukyung released my wrist and crooked one finger.

“Come at me. I won’t hold back this time.”

I stared at him without speaking.

Jin Mukyung was unquestionably more skilled than me. The wall separating me from the Peak realm was too high for my current abilities to overcome.

I knew that. I knew it all.

*This is pissing me off.*

And suddenly, I was curious.

How far could I go?

Just how strong was the genius named Jin Mukyung, whose reputation had spread so far?

This was competitive pride—not as a Hunter, but as a martial artist of Murim.

*Let’s do this.*

Jin Mukyung was the first to notice the change in me.

“I didn’t know you could make a face like that.”

“This is my normal face.”

He laughed as though he were enjoying himself.

“Fine. That’s all well and good… but are you still talking so casually?”

At that moment, Jin Mukyung's fist blurred.

Whoosh! Whump!

My vision flashed. Even though I had been concentrating to the extreme, I hadn't managed to avoid the attack completely.

Jin Mukyung looked back and forth between his fist and me.

“That shouldn’t have happened.”

The punch had been aimed at my temple. If it had landed cleanly, that would have been the last blow.

Even though he hadn't used internal energy, I had managed to partially evade a Peak master's full-powered One Strike.

“You see? I’ve improved a lot.”

“I admit it. But you’re not even a quarter as good as the rumors claim.”

“Don’t worry. I’ll catch up little by little from here on.”

“You’ll catch up to me? How long do you think that’ll take?”

I answered.

“Starting right now.”

“Hold out for a quarter of an hour. Then you’re my big brother.”

Jin Mukyung's form blurred once again. But this time, I was a step faster.

*Assign ten points to Agility.*

Ten level-ups gained through the war. And the hundred points that had been lying dormant in my Status Window.

Some of them answered my command.

Shwaaaak!

The change was instantaneous. At the same time, I became certain.

I was certain I could perfectly evade Jin Mukyung's fist flying toward my face.

Whoosh!

*Too slow.*

Without hesitation, I turned my head.

Whump!

*…Damn it. I should’ve used ten more points.*

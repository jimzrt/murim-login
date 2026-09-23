# Checkpoint Review — 820–824

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

# Chapters 820–824

## Plot

Jin Taekyung breaks through the fanatics by awakening a new use of his Middle Dantian: he suspends arrows and other weapons in the air, then turns them against the enemy. He kills Amir and the elite troops in a steel storm. After the Skeleton King’s words shake the followers’ faith, Jin kills Hamid Shah Masoud, ending the battle at dawn.

Though exhausted, with his Middle Dantian at its limit and his mental strength depleted, Jin pursues the Doppelganger with the Skeleton King. Magic Johnson teleports them toward the place the Doppelganger first revealed, while staying behind to guard the battlefield.

The Doppelganger reaches a ruined oil field where its master once stayed during the Great Cataclysm. It confirms Jin is the Chosen One, then manipulates and massacres twenty of its personal guards to absorb their vitality and souls. Blue-white flames suddenly erupt from above and engulf it.

## Continuity

- Jin remains the World Hunter Federation’s Alliance Leader, pursuing Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.
- The Prophet is a Level 170 Doppelganger titled “The Final Abyss.” It can resurrect by consuming absorbed lives and reproduce victims’ appearances, abilities, and memories. It still wears Siegfried Bassman’s face and has his Grand Mage abilities.
- The Doppelganger confirmed Jin is the Chosen One and believes its master will be pleased. Its master, plan, and the meaning of the designation remain unknown.
- Jin can control weapons within a radius of dozens of meters with the force from his Middle Dantian, steering them around allies and toward selected targets.
- Jin killed Amir and Hamid Shah Masoud; the battle against the fanatics ended at dawn. The Skeleton King’s argument against the fanatics’ faith helped shake their resolve.
- Jin’s Middle Dantian is at its limit and his mental strength is depleted; the System cannot restore either condition. Jin and the Skeleton King pursued the Doppelganger by Teleport, leaving Magic Johnson to guard the battlefield.
- The Doppelganger killed twenty members of its personal guard and absorbed their vitality and souls. Blue-white flames engulfed it at the ruined oil field; their source and effect are unknown.

## Translation Decisions

- Keep **magical power** distinct from **mana**.
- Keep **Blink** distinct from **Teleport** and **Warp**; extended-range Blink causes severe strain. The unusually high concentration of magical power makes the Teleport attempt especially dangerous.
- Keep **Fire Storm** and **Aqua Storm** as distinct named spells.
- Render **[영웅의 검]** as “Hero’s Sword” and **등가교환** as “Equivalent Exchange.”
- Keep the Doppelganger’s performed religious devotion distinct from its motives; it manipulates its followers’ faith.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades, including under the name Muninn.",
    "The Doppelganger can resurrect by consuming absorbed lives and reproduce absorbed people’s appearances, abilities, and memories; it has taken Siegfried Bassman’s face and Grand Mage abilities.",
    "The Doppelganger’s absorbed lives were dwindling after it forced Blink beyond its normal range; it has now killed twenty of its followers and absorbed their vitality and souls.",
    "The Doppelganger confirmed Jin is the Chosen One and believes its master will be pleased.",
    "Blue-white flames erupted above the ruined oil field where the Doppelganger arrived; their source and effect are unknown.",
    "Jin defeated Hamid Shah Masoud and ended the battle against the fanatics, but his Middle Dantian is at its limit and his mental strength is depleted.",
    "Jin and the Skeleton King pursued the Doppelganger by Teleport; Magic Johnson stayed behind to guard the battlefield."
  ],
  "continuity_sources": [
    823,
    824
  ],
  "open_questions": [
    "Who is the Doppelganger’s master, what is the plan, and why must the target be avoided until it is complete?",
    "What does the Chosen One designation mean?",
    "What caused the blue-white flames, and what happened to the Doppelganger?",
    "Is Magic Johnson human?"
  ],
  "safe_through": 824,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 820

# Chapter 820

Everything that lives is born with a destiny of struggle.

Humans, monsters, animals living in the wild or behind fences, even green plants—all the same.

Even when survival itself wasn’t the reason to struggle, you had to fight and take what you wanted.

And under this absolute law, I was no exception.

*Crunch!*

The least force. The least speed.

But that was enough. I twisted away, leaving behind the fanatic collapsing with his brains splattered everywhere.

*Whoosh!*

The air split. A flash dropped from empty space and skimmed past me by half a handspan.

Between the pitch-black robe and turban that covered him completely, I saw his eyes widen. The White Flame’s spearhead was reflected in them.

*Thump. Splurt!*

A head flew up. More enemies and their auras surged through the spraying blood.

Watching blades rush at me from every direction, I tightened my grip on the spear shaft, slick with blood.

*Hoo.*

I breathed out. The world slowed. My relaxed muscles loosened, and the flames coiling around my spearhead flickered.

Like the tail of something caught in the wind.

*Fire Dragon’s Single Tail.*

Flames surged. The enemies’ auras flashing from every direction drove away the darkness racing toward the dim dawn.

And I smoothly spun my whole body.

*Shiiiiing!*

Blue-white flames streaked across the space. They were faster than any aura bearing down on me, sharper than anything anyone could stop.

*Slice.*

With a cool, clean cut, a sword in someone’s hand tilted to one side.

No—faint lines had already appeared across the bodies of dozens of fanatics, frozen in place.

“Ghk. Ghrk…”

Trembling pupils. A fading voice.

But no words or actions could stop death from bearing down without mercy.

*Fwoooooosh!*

Flames raced along the faint lines, devouring the enemies’ lives.

Dense mists of blood spewed in every direction, blanketing the battlefield’s thick, low-lying steam.

*Thud-thud-thud!*

A rain of blood fell from overhead.

At the same time, human flesh, bones, and organs—shattered by a single horizontal strike—tumbled across the ground. Just like the hundreds of fanatics who had fallen before them.

“De…mon…”

Someone’s voice reached my ears. Of course, it belonged to one of the fanatics, someone whose face and name I didn’t know—and an enemy I had to kill.

*Pfft!*

A familiar bell rang as Finger Qi shot from the hand I thrust out without even looking.

*Ding.*

Another notification of death.

The fanatics surrounding me stopped moving.

Most of them probably hadn’t understood even a fraction of what had just happened before their eyes.

How their comrades had died. Why they couldn’t wound me, even with so many fighters.

And those questions would remain unanswered even after they died.

Except for one man.

*Whoom. Boom!*

A straight spearhead collided with the curved blade of a saber shaped like a crescent moon.

The thunderous impact made my ears ring. I blocked the attack before its piercing whistle reached me, then looked at the old man beyond the white scimitar’s blade.

“You lousy old bastard. Finally crawled out, did you?”

“I was waiting for my prey to tire.”

The old man with the long name, Yahya Muhammad Ahmad Bedouin, twisted his scimitar as he answered.

*Ka-ga-gak!*

Auras of different colors collided, sparking like lightning. A small explosion waited at their tips.

*Boom!*

The impact roared like cannon fire and traveled along my spearhead.

Unable to withstand its incredible force, I staggered backward. Seeing the old man standing firm in place, I realized something.

“Don’t tell me…”

“You’ve finally understood, King of the heathens.”

A smile formed on the old man’s wrinkled lips.

Two entirely different energies, never before revealed, coexisted along the scimitar’s blade, still pointed at me.

*Mana. And magical power.*

As those two words crossed my mind, the old man continued.

“I, Yahya Muhammad Ahmad Bedouin, am a warrior chosen by God.”

“Huh.”

A hollow laugh escaped me before I could stop it.

The Doppelganger hadn’t raised only Michael Silbert. It had chosen its most loyal, most insane fanatic and taught him how to wield magical power.

If there had been more fanatics gifted enough to accept two opposing energies, the Doppelganger would’ve churned out half-human, half-demon monsters like they were coming off an assembly line.

“I knew you were out of your mind from the start…but you’re one seriously crazy old bastard.”

“If that is what you wish to believe, then believe it.”

The old man shook his head and looked at me with gray eyes.

“You know nothing. Dozens, hundreds died trying to be chosen by God. But I alone survived.”

“So this ‘chosen by God’ thing you’re talking about just means mixing a human and a monster half and half? Then does that make a half-and-half order of black-bean noodles and spicy seafood noodles God’s warrior too?”

“The great Prophet said that monsters, too, are God’s creations—and calamities sent to punish the fallen humans of this world.”

“Bullshit. Anyone listening would think you lived in some other world, not this one. By your logic, you’re one of those fallen humans too, you crazy old bastard.”

“Though fallen, I was given a chance at salvation. I inherited two powers that can never coexist. That is who I am: a warrior and a punisher chosen by God.”

With every word, the madness in his faith showed through.

But a madman doesn’t know he’s saying crazy things.

Even if the Doppelganger gathered every fanatic in one place and offered a nationally televised apology, they wouldn’t believe it.

Their faith was their entire lives, their reason for living, even something tied to the afterlife.

In the end, there was only one thing I could say to fanatics like that.

“You fucking lunatics. It’s a waste of time talking to you.”

“Remember one thing.”

*Step.*

The old man approached me. The fanatics, who had hesitated for a moment, once again burned with fighting spirit.

“Your steps will never reach the Prophet.”

“Fuck off.”

*Whoosh.*

I shot forward like the wind as I answered.

That brief exchange had given my body a moment to recover from the strain of the fierce battle. It had also been enough to assess the situation.

*It’s even. Fierce, but we’re holding our own.*

The Hunters’ shouts, which had been distant, were drawing closer.

But to overcome a disadvantage of more than ten to one and win this fight, we had to cut off the head.

It was the best I could do before chasing the Doppelganger, which was still fleeing even now.

*Thwack! Crunch!*

My spear pierced through three fanatics and emerged on the other side.

Without a trace of hesitation, the old man used his subordinates as bait and swung his scimitar at my neck.

*Whoosh! Slice!*

I bent at the waist and dodged the slash. It cut apart the fanatics charging at me from behind.

The old man sprang back to prepare for my counterattack and shouted in a cold voice.

“That demon is trying to harm the great Prophet! Stop him with your lives!”

Damn old bastard.

He might’ve been the most fanatical of the fanatics, but the experience he’d gained over the years was no joke.

He knew exactly what his job was, and he stayed cool-headed even in the heat of battle.

*If this drags on any longer…I’ll really lose him for good.*

I thought—or rather, calculated—as I cut down the fanatics charging from every direction like moths to a flame.

How much strength I could bring to bear right now.

How I could end this fight as quickly as possible.

And finally, how much strength I’d have left by the time I could chase the Doppelganger again.

Then, amid the unending blood and screams, I realized I’d been thinking about something stupid.

*When the hell did I start calculating every little thing like this?*

When had it started? Every moment was a struggle.

Whenever that happened, I had to forget the past and erase the future from my mind.

That was how you survived. Only by betting everything on the present could you think about the past and move toward the future.

*Slice!*

A searing pain ran down my back. My exhausted body felt as heavy as a waterlogged cotton blanket. Weapons came at me like big and small gears turning in tandem, leaving wounds all over my body.

But because of that, my hesitant body and mind woke up completely.

*Grit.*

I clenched my teeth against the pain and hurled the spear I held in a reverse grip at the fanatics charging straight at me.

There was barely room to throw a spear, but one step was all I needed.

*Cr-r-runch!*

Flesh and blood were crushed. The pain was enough to make them forget their faith, and they screamed.

The old man’s command rang out among them.

“Now!”

Now? Now what?

Oh. My weapon?

“So what?”

I spat out the blood running between my lips and reached out. The Flame Divine Palm I’d been saving for a more efficient fight erupted.

The fanatics crowding around me went down, engulfed in flames.

I sensed them hesitate at the sight of their comrades writhing in hideous agony.

*One more.*

*Fwoosh—BOOM!*

Blue-white flames lit up the darkness, scorching flesh and turning the blood and bones within to ash.

“Aaaaaagh!”

“Hng…!”

That was when it happened.

One fanatic, who had unconsciously stepped backward before that cruel, dazzling sight of a mass execution by fire, suddenly had his head fly into the air.

*Slice!*

Along with the belated sound of a blade cutting through flesh, the old man—who had vanished from sight to escape my notice—gave a chilly command.

“Fire.”

*Whooooosh!*

Dozens of arrows whistled through the air, one after another.

By the time I spotted the archers with dark-colored bows among the now much thinner ranks of fanatics, it was already too late.

*Thud-thud-thud!*

“Guh!”

“Ghk.”

Indiscriminate fire rained down on friend and foe alike.

The fanatics hesitating around me fell like straw, and the arrows, brimming with mana, pierced their bodies and came straight for me.

*Whoosh.*

An unusually long whistle dragged through the air.

And dark arrowheads, wrapped in blood and mana.

In the moment the world slowed, a thought came to me with absolute certainty.

*I can’t dodge this.*

Of course, I could knock aside half of them. Of the rest, I could somehow twist my body to evade half.

But the Fire Dragon Armor hadn’t finished repairing itself, and that didn’t change the fact that I’d have to take some damage.

But why?

A strange feeling came over me.

It was as if my instincts were rejecting the judgment my mind had made.

And I had a sense of déjà vu, as if my whole body’s awareness were taking another step into a realm I didn’t know existed.

*I can do this.*

A strange certainty, like a conviction, took over my body and mind. An inexplicable tickling sensation began around the center of my chest and spread through my entire body.

*Right now.*

I reached out like a man in a trance, toward the dozens of arrows almost at my face.

No—not just the arrows. Everything around them.

*Shhhhaaa.*

Time began to move again, but no one spoke.

I stared silently at the arrows stopped in midair, then snapped my fingers.

*Swish.*

The arrows pointed toward the enemy. And once again, the power of my newly advanced Middle Dantian pressed down on the space around us.

*Ding. Ding. Ding.*

As the clear chimes pierced my ears, I smiled at the old man, frozen like a statue.

“Whoa. I did it?”

“T-This is—!”

“Refund, you fucking bastard.”

*Whoosh-whoosh-whoosh-whoosh!*

The arrows’ powerful whistle swallowed the words he was about to say.
## Chapter artifact 821

# Chapter 821

The moment dozens of arrows stopped in midair, the old man doubted his own eyes.

*Magic?*

No. That couldn’t be.

Mages and warriors shared the same root—mana—but their trunks and branches stretched in entirely different directions.

That was why the Spellblade was considered just as impossible as the coexistence of mana and magical power. Perhaps even more so.

*But if it isn’t magic, how…?*

The old man had long since reached the realm of the superhuman.

In his youth, he had ranged across battlefields amid the turbulent politics of the Middle East, protecting his tribe. Then, as the Great Cataclysm began in his middle age, he awakened to a power he had never known existed.

Even without accepting magical power, he would have been strong enough to stand shoulder to shoulder with the heroes of the Great Cataclysm.

That was why he found this all the harder to believe.

There was a clear, undeniable limit to what a warrior like him could move using mana.

*And those are arrows. Dozens of them, fired from close range.*

Worse, the unit that had been holding back in the rear was made up of the elite troops he had personally trained. Swords and shields he had saved and saved for the most crucial moment.

And now the arrows those very elites had loosed were stopped.

No—they were under control.

Dozens of arrows, shot with ferocious force and brimming with mana, all at the wave of a hand.

*Whoooosh.*

The air stopped. The wind, thick with the stench of blood, disappeared.

In that space where everything had vanished like a desert mirage, the wave of steel pouring toward one man turned its head.

*Flick.*

Dozens of arrowheads, still brimming with mana, glinted in the darkness. They were pointed at the former masters who had sent them flying. And…

“Wow. It actually worked.”

They were ready to obey the will of their new master.

*Jin Taekyung.*

The old man stared at the young man’s face, smiling beneath a coating of blood, and clenched his teeth without meaning to.

A groan slipped through his bloodless lips.

“Th-This is…!”

*What is this? What have you done?*

He wanted to ask, but the young man didn’t wait for the words of an old fool blinded by false faith.

“Refund, you fucking bastard.”

*Whoosh-whoosh-whoosh!*

A fierce whistle of air shattered the silence. Hundreds of fanatics surrounding them watched the unbelievable sight with vacant eyes.

As if an invisible giant had drawn a bowstring, dozens of steel arrows came raining down—far faster and harder than before.

All aimed at one man.

The old commander-in-chief who led and commanded every fanatic.

“Block—!”

*Boom!*

The unfinished shout vanished beneath a small explosion.

A sword swung to knock the arrows aside shot into the air, along with its wielder’s arm.

“Gaaah!”

A scream erupted a moment later. Then came dozens of streaks of light, sweeping in and cutting through and smashing everything in their way.

*Grit.*

The metallic taste of blood filled his mouth.

The old man bit down so hard that blood ran from his lips, but he didn’t even notice. He brought down the scimitar in his hand, unleashing a murky energy in which magical power and mana were mixed together.

*Whoooooom!*

The immense pressure of wind that poured along the blade forced away the arrows flying in from the front.

Unlike Jin Taekyung, who had been surrounded and forced to face arrows coming from every direction, the old man had fanatics around him who would lay down their lives to stop the arrows for him.

Perhaps that was why the old man had switched to the offensive at once and stepped forward. Why he trusted the dozens of followers surrounding him like shields.

But the next moment, that faith vanished without a trace.

*Whish.*

At the faint whistle of air, the old man’s eyes flew open.

In his seasoned gray eyes, arrows were flying toward him as if alive, avoiding the fanatics.

*This is impossible…!*

A cry like a scream rose to his tongue, then disappeared. No—he wasn’t even given time to let it out.

The old man sucked in a breath and hurriedly swung his scimitar.

And as he watched the streaks of light fill the air around him, he knew by instinct:

*Damn it.*

Unlike Jin Taekyung, he couldn’t escape this attack.

*Crack!*

The arrows caught in the scimitar’s path bent and broke.

But even the old man, who had reached the superhuman realm, couldn’t deflect or dodge every last one.

*Thud-thud-thud!*

“Guh!”

Blood poured through his clenched teeth. His vision blurred for an instant, and he felt the pain pulsing through his body.

His ribs, legs, chest, back…

He felt the arrowheads pierce his armor and flesh, shatter bone. He also felt the hot energy packed into their tips seep into his insides.

“Cough.”

His once-sturdy legs trembled. As the old man staggered, more than ten arrows buried deep in his body, the fanatics supporting him shouted like they were screaming in despair.

“No!”

“Amir! Amir! Please, stay with us!”

“What are you waiting for? Get him somewhere safe!”

The fanatics finally grasped what had happened, and they were more shaken than ever.

If the Doppelganger, under the name of the Prophet, had been their spiritual pillar, the old man was the warrior chief favored by God, the general who led them.

Then a voice pierced their ears like a spike.

“Who said you could?”

“……!”

“……!”

The shock hit like a bucket of cold water.

At the same time, heavy footsteps moved forward.

“I asked you. Who said you could move?”

His voice was low and his face was etched with fatigue.

But the fanatics who stepped back without realizing it neither saw nor felt any of that.

Their eyes were wide, and they could see only one thing:

The flames flickering in his eyes.

“Did all you bastards eat a load of dates together? Not one of you can answer me.”

His blood-crusted lips twitched. As Jin Taekyung smiled and reached out, an immense invisible force pressed down on the space around them.

No—it ruled it.

*Hssssss.*

The air stopped. The wind scattered.

Jin Taekyung felt an intangible force welling up from his chest, from his Middle Dantian.

A radius of dozens of meters already belonged to him. The hundreds of fanatics staring at him in shock were invaders. Demons defiling not only this land, but the entire world.

*No. To you, I’m the demon.*

Jin Taekyung looked down at the frozen fanatics with a gaze full of disgust.

He didn’t want to kill them. He only wanted peace.

He wasn’t a Killing Ghost, forever thirsting for blood. Every time one of the Hunters who had united under a single banner for the sake of the world fell, he felt pain and sorrow.

But…

In the end, this too was a struggle for each side’s own purpose.

To gain peace, they had to wage war. And in that war, rivers of blood and death would flow.

There was no other choice.

“It’s too late to turn back now. For me, and for you.”

The moment Jin Taekyung’s quiet voice rang out—

*Rooooom.*

The air and wind that had stopped woke again.

The old man, whose recovery was no longer human thanks to the help of magical power, got back to his feet under his own strength. Waiting for him was a spectacle of steel filling the air.

“This is…”

The old man couldn’t finish. And it wasn’t just him. No one could have.

All they could do was stare, dumbfounded.

Spears. Sabers. Swords. Axes. Countless arrows and fragments of broken blades.

The wave of steel had left the side of its former master, who had met his death, and welcomed a new one. It rolled through the air.

Its cold body glinted as it turned toward each of its targets.

And at the center of it all stood Jin Taekyung.

“Any last words?”

Facing a reality he couldn’t believe, the old man let out a sigh. A murky force—neither monster nor human—overflowed through the scimitar gripped in his hand.

“Inshallah.”

*May it be God’s will.*

With the prayer ringing in his heart, the old man stepped forward alone.

He left behind his followers, paralyzed with fear and waiting only for death. He went forward carrying the sense of duty and pride of a warrior chosen by God.

And yet, why?

*Is this— is this really what God wanted?*

For the first time, the old man, who had believed in God and the Prophet more than anyone, felt doubt.

But even now, as he charged like a streak of light and watched the rain of steel pour from the sky, brimming with lava-hot mana, he couldn’t find an answer.

*Answer me. Is this truly the promised land you spoke of?*

But the old man’s god did not answer.

Just as it had never answered, from the distant past until now. And just as it would never answer in the future.

Only a faint voice reached his ears—a voice that might belong to God or to a demon.

“Die, old man.”

*Fwoooosh!*

A gale swept through. A wave of steel, falling in place of damp rain, swallowed him.

As his body and power—part monster, part human—were smashed to pieces, the old man heard a terrible scream ringing faintly in the distance.

“Gaaah!”

His vision darkened. His consciousness scattered. And the warriors of God met their brutal end.

*Ah.*

He finally knew the answer to his question.

This was not the promised land. It was the land of death.

*Thud.*

His lifeless body crumpled to the ground.

But even though he found the answer in his final moment, the old man’s face was twisted with anger and disbelief.

* * *

It happened in an instant.

The weapons swinging at one another stopped in midair, and the shouts bursting from hoarse throats abruptly cut off.

Then everyone turned to look in the same direction.

*Fwaaaash!*

It was a roar and a scream at once.

A scream of steel raining through the air. And a scream of terror from people who sensed their own deaths.

*Kwaaaang!*

Dust billowed upward. Through the sand surging like a whirlwind, streams of blood spurted like fountains.

*Splash—splat!*

The fanatics standing dozens of meters away stared blankly at the sight and blinked.

Blood poured over their heads and ran down in sticky streams, along with something hard and something soft.

It didn’t take them long to realize what those things were: human bone and flesh.

“Ah… ah…”

Their hands and feet trembled. The clatter of their teeth spread among the fanatics like an epidemic.

They already knew. The most carefully chosen elite troops had been waiting in the rear to join the fight with the commander-in-chief.

But from this moment on, that fact belonged to the past.

Annihilation.

Everyone on the battlefield understood it by instinct.

No one could survive in that steel storm raging now.

No—if there was anyone who could, it was one person alone.

*Jin Taekyung.*

As the name surfaced in everyone’s mind—

*Kwaaaaa.*

The whirlwind slowly settled. Within it, someone’s silhouette wavered like heat haze.
## Chapter artifact 822

# Chapter 822

In the wake of the Great Cataclysm, the boundary between what humanity considered common sense and nonsense crumbled like a sandcastle.

Awakened people, monsters, magic, Gates.

Things that had existed only in novels and movies became reality.

Calamity became a neighbor, and the word *death* lost its value.

But humans are adaptable creatures.

They quickly accepted the unbelievable reality that had come upon them and recognized the absurd as the new normal.

They thought nothing like this would ever happen again in human history.

No—they hoped, please, that it wouldn’t.

But at this very moment, in an unnamed canyon in the Rub’ al Khali Desert, those who had been piling up blood and bodies without end had no choice but to admit it.

The common sense they had accepted had crumbled once more.

*Rooooar.*

The rain of steel that had lashed down through the darkness stopped. The whirlwind that had seemed ready to swallow the entire desert slowly died away.

And amid the silence and shock that swallowed everyone, thousands of eyes finally settled on the figure who had appeared.

“Oh my God.”

“What the hell did I just see?”

The Hunters stared in awe and elation.

“He’s a demon. That thing has to be a demon.”

“Inshallah. God…”

The fanatics trembled with fear and hatred.

And among all the people gathered there, the one being who wasn’t human spat out the one word they had all wanted to say.

“Monster.”

The Skeleton King curled up the corners of his mouth and looked at the man before him.

“I told you, didn’t I? Let’s finish this before someone scarier than me shows up.”

“……!”

The man’s eyes flew wide open. His hair was disheveled, and large and small wounds covered his body.

He had already been fighting a difficult battle against the Skeleton King, but now he couldn’t care less about his injuries.

“How… How can someone do that?”

The man muttered in a dazed voice.

His bulging eyes stared beyond the whirlwind, where nothing remained but blood and corpses.

A thousand.

There had been a thousand warriors waiting in the rear.

An elite force he had saved for the final blow. And on top of that, Amir—the finest warrior and commander.

No. He *had* been there.

Until that enormous whirlwind of steel swept them away.

*They’re all dead? By the hand of one man?*

A reality he couldn’t believe or understand.

The man’s hand trembled around the hilt of his sword. A groan slipped through his clenched teeth.

“Th-That’s impossible—”

“—It’s possible.”

The man’s wavering voice cut off abruptly.

The Skeleton King, cutting off his words like a guillotine’s blade, continued in an even tone.

“Jin Taekyung could do it.”

“Shut your mouth!”

The man’s furious roar split the desert. He glared at the Skeleton King with blazing eyes.

*Shhhhh.*

The immense killing intent and aura he unleashed swallowed up the space around him.

It was a presence strong enough to leave an ordinary Hunter unable even to breathe. But the Skeleton King didn’t so much as blink.

Killing intent was the most familiar energy in the world to the undead.

Simply by existing, he was already in contact with death.

The aura the man brought forth was no different.

*At most, half as strong as that guy.*

Thinking of *that guy*, shimmering in the distance like a mirage, the Skeleton King let out a quiet snort.

The world called monsters like him monsters, but the real monster was someone else.

“Why did you have to do something like this? If you’d stayed quietly tucked away in some corner of the desert, you wouldn’t have made that guy angry.”

“……God, God chose us. The great God Himself sent the Prophet to lead His warriors to the promised land!”

“The promised land?”

The Skeleton King glanced around as he echoed the words.

Corpses littered the ground in every direction.

Blood flowed like a river, rising to their ankles. Limbs and chunks of flesh—no one knew whose—bloomed across the desert like flowers.

“Is this the promised land you’ve been blathering on about all this time?”

“……!”

“If you mean you promised God that you’d all die here together, then sure, I’ll give you that one.”

The man’s eyes wavered. So did those of every fanatic around him.

The Skeleton King’s voice, infused with magical power, carried far.

Far enough to reach the ears of every Hunter and fanatic.

Each word doused the flames of their fanaticism, which had blazed as though they would never go out. And his words made the Hunters take up their weapons once more.

“There were humans. No—there were many humans. Frail beyond comparison to me, born with death as their fate.”

The Skeleton King remembered.

Countless faces he had encountered since coming out into the world flashed before his eyes.

“They fought countless battles and died again and again. But they didn’t do it just for the gods they believed in.”

They had families and friends. People they loved. Values worth protecting.

“I couldn’t understand those stupid humans. I couldn’t even accept that there were different kinds of death.”

But not anymore.

The Skeleton King had watched humans from closer than any monster.

He had been with them.

And finally, he understood.

The countless deaths he had witnessed weren’t all the same kind of thing. Some of them couldn’t simply be called death.

“They were sacrifices.”

Some people killed for money and power. They abandoned their parents and children, betrayed their partners and friends.

But there were others, too, who burned like torches and then vanished like wildfires.

People who marched forward prepared to die.

People who stood their ground and fought for others, for a better world, even in the face of death.

The world called them heroes.

It called their deaths sacrifices.

“But what should I call you? What should I call your deaths?”

“……!”

“If you have a mouth, then answer me. You foolish people who brought calamity upon the world after being deceived by an illusion.”

*Kiiiiing.*

The man swallowed a breath as the fading golden crown above the Skeleton King’s brow began to shine.

His bewildered gaze passed over the countless faces surrounding him.

Hatred and contempt.

Resentment and confusion.

And it wasn’t just the Hunters.

Even the fanatics under his command were wavering.

Some of them looked at him with eyes clouded by resentment and confusion, then turned away. The sight struck the man as though something solid inside him had suddenly collapsed.

“I, I… I…”

He wanted to speak.

He wanted to shout at the people wavering before him.

Tell them not to be taken in by a demon’s silver tongue.

Tell them not to dare question the great God and His Prophet.

But his tongue wouldn’t move. The hand gripping his sword seemed to be losing its strength.

In his whitened mind, all that repeated was the demon’s whisper from a moment ago.

> *But what should I call you? What should I call your deaths?*

Without realizing it, the man clenched his teeth. A sharp pain flared from a broken molar, but it felt impossibly distant, like a dream.

The corpses of his followers filling every direction.

The sticky pools of blood gathered at his feet.

*Is this really…*

Was this the promised land that was supposed to be beautiful and green?

Was it heaven, prepared by an omnipotent God and His Prophet for His people?

The voice he had just managed to swallow echoed in his mind as a question.

And through his dreamlike, hazy vision, a dazzling shaft of light illuminated the darkness.

*Whoooooom.*

Golden radiance rose along the many-colored blade.

The light felt so warm. So sacred.

The man even forgot that the Skeleton King was the one holding the sword.

The Skeleton King held the [Hero’s Sword], shining with a brilliant light reserved for the chosen, and stared at him. The man found himself asking the demon:

“Are you… really a demon?”

It was at that very moment.

*Step.*

In a world where everything had stopped, a single person’s footfall rang out.

At the same time, a calm voice reached the man’s ears.

“You see what you want to believe. Just like you called a monster the Prophet and worshiped it.”

The wind held its breath.

Everyone turned their heads in the same direction.

And at the end of all those gazes stood Jin Taekyung.

“Hamid Shah Masoud.”

The man stared blankly at Jin Taekyung.

It was a name no one knew except Amir. It was also a name his opponent couldn’t possibly know.

“How could you know?”

“If I said God told me, would you believe me?”

“……!”

“You’re an easy bunch to read. You saw what you wanted to believe, and believed what you wanted to see. You thought all of this was God’s will.”

*Splash.*

His rough footsteps carried him forward.

The pool of blood, with pieces of flesh floating in it, splashed in every direction. But the young man, who looked no different from a man drenched in blood, didn’t care.

“Tens of thousands are dead because of idiots like you. No—hundreds of thousands.”

Cities burned. A massive tidal wave swept through a harbor.

Countless people died in sudden disasters. Happy families were torn apart, and children who lost their parents were sent to orphanages.

And none of it had been a natural disaster.

It had been man-made.

“There is no God. And even if there is, He’d have to be an idiot to watch over trash like you.”

Jin Taekyung spat out each word as he looked across the countless fanatics.

Some swayed on their feet, stunned. Others wept as they belatedly realized what they had done.

But if a few short words could change their hearts, then the disasters of the past would never have happened.

“How dare you, you wicked heretic!”

“God is great!”

*Papapat!*

At the sharp shouts, figures rushed in from all sides like streaks of light.

A cold smile touched Jin Taekyung’s lips as he met their hate-filled gazes.

“Good. That’s more like it.”

At that moment—

*Shwoosh!*

Silver flashes shot up from every direction, splitting the wind.

They tore through space, piercing and slicing the bodies and blades hurtling toward him.

*Whoooosh! Slice!*

*Thud-thud-thud-thud!*

Then the survivors finally understood.

What the whirlwind that had come before had been.

And how the people caught within its range had died.

*Krrrunch!*

An eerie sound swallowed up everything within a radius of more than ten meters.

Blood poured like a rain shower. Arrows and daggers that had shot through the air turned around and flew back to where they had come from, taking their owners’ lives.

“Guh…!”

They were lucky if they managed to get out a dying gasp.

Of the hundred or so fanatics who had charged all at once, half were torn to pieces, hardly a recognizable shape left behind.

*Thud, thud, thud.*

Flesh, blood, and bone fragments filled the empty spaces where screams had been.

And from the hand of Hamid Shah Masoud, the man who could only stare wide-eyed at it all, the sword hilt slipped free.

*Clang.*

No one spoke.

Not the Hunters. Not the fanatics.

Not the Skeleton King, holding the Hero’s Sword lowered at his side, nor Magic Johnson, standing upright in midair.

At this moment, only one person could speak.

Only he was the judge and the one who could grant forgiveness.

So Hamid Shah Masoud had no choice but to plead for mercy in a trembling voice. If he wanted to survive, he had to beg for his one and only life.

He dropped his sword and fell to his knees.

He threw away the faith in his heart, shattered beyond recognition, as if tossing it into a trash can.

“P-Please spare me.”

A desperate plea.

Jin Taekyung looked down at him with an unwavering gaze, then suddenly reached out his hand.

A searing heat gathered at the tips of his bloodstained fingers.

*Thwip. Thud.*

A single blast of hot wind.

That was all. The man fell quietly and never got up again.

*At last.*

Jin Taekyung let out the breath he had been holding and lifted his head.

*Clang. Thud-thud.*

Countless still-sharp weapons and knees covered the blood-soaked sand.

Victory had come at the break of dawn. The battle was over.

But Jin Taekyung’s gaze was fixed on the west, still shrouded in darkness.
## Chapter artifact 823

# Chapter 823

*Clang. Clatter.*

Countless weapons fell onto the blood-soaked ground. Thousands of fanatics sank to their knees like a wave.

The faint light of dawn, rising in the east, shone on the scene.

The battlefield where victory had finally arrived.

And the young man who had brought about this unbelievable victory.

*Jin Taekyung.*

The defeated, kneeling before that name, did not dare raise their heads. The victors gazed at their young Alliance Leader with eyes full of wonder.

Outnumbered by more than ten to one.

Mad fanatics who charged without fear of death.

The Hunters had been afraid.

Afraid they would never see their families again. Afraid that if they fell in this nameless canyon, an even greater calamity would swallow up those who remained alive.

But their brief fear had been rendered meaningless. Jin Taekyung had ended this massive battle in an instant.

He had been overwhelming—and, in a way, divine.

Everyone who survived knew it.

Jin Taekyung hadn’t just cut through the enemy’s flesh and bone. He had broken the fanatics’ spirits. He had made them lay down their weapons of their own accord.

Like a scene from a myth.

*If miracles exist… this must be what one looks like.*

Magic Johnson suddenly felt something stir in his chest. The Grand Mage’s gaze, fixed on Jin Taekyung, trembled like ripples on a pond.

*He reminds me of him. Astonishingly so.*

Old memories rose like heat haze, drifting across his eyes.

Memories more than thirty years old, worn with time. Yet every moment he had spent with *him* remained vivid.

The miracle Magic Johnson had witnessed with his own eyes—*his* great achievement—would be remembered forever, as long as humanity endured.

And so would the young hero standing alone at the center of the now-quiet battlefield, in this very moment.

But Magic Johnson also knew.

To gain anything in this world—even a miracle—one had to pay a price.

*Equivalent exchange is the one unchanging law.*

Just then, as Magic Johnson’s gaze settled deeply on Jin Taekyung, dazzling light streamed from the tip of the staff he slowly raised.

*Fwoooosh.*

A flash that heralded the end of the fierce battle drove back the darkness and lit the dawn.

The Hunters touched by that light, carrying a gentle warmth, finally understood the reality they could hardly believe.

They had won.

Today, they had written a new line in history.

*Clang-clang-clang!*

Blades smeared with blood and flesh thrust toward the sky.

“Waaaaaaah!”

A tremendous roar shook the canyon.

It was joy at their victory, mourning for their dead comrades, and reverence offered wholly to one man.

But most of them neither knew nor saw it.

The young hero standing tall amid the cheers pouring in from every direction, his eyes twitching.

His fingers, gripping the spear shaft as tightly as they could because it kept slipping from his grasp, had turned white.

*…Fuck.*

Jin Taekyung swallowed a curse and suppressed the hot surge rising from deep in his chest.

His vision kept blurring. In his ringing ears, the Hunters’ cheers and the System notifications crowded together in a jumble.

> **System**
> - You have defeated Lv. 140 Hamid Shah Masoud!
> - You have gained a substantial amount of EXP and Fame!
> - Level Up!
> - All status ailments have been removed as a Level Up effect!
> - Some wounds have been healed as a Level Up effect!
> - Special debuff Broken Body rejects the healing effect!
> - Status ailment Mental Strength Depleted rejects the healing effect!
> - Middle Dantian has reached its limit! Rest as soon as possible to recover your mental strength!

Jin Taekyung’s situation was exactly as the System had described.

His physical wounds and fatigue had recovered, but his Middle Dantian was beyond the System’s power to heal. The catastrophic force he had unleashed earlier was never something he could wield for a cheap price.

*Throb.*

He had already wrung himself out to his limit—and then beyond it. Even standing took more strength than he had.

Pain radiating from around his heart and mental exhaustion gnawed at him without pause, whispering:

The battle is over.

Your part is done. Rest now.

“Yeah. I did enough, didn’t I?”

The empty murmur scattered from his lips.

Through his blurred vision, Jin Taekyung looked at the cheering Hunters.

Faces he had grown familiar with after fighting alongside them several times.

He could see a few gaps here and there, but he could tell that not many Hunters had lost their lives in this battle.

If he hadn’t pushed the Middle Dantian beyond its limits, more than half of the Hunters who had survived would probably be sprawled across the battlefield by now, growing cold.

Jin Taekyung wasn’t exaggerating.

He had turned a grueling battle into a swift victory and stopped more blood from being spilled.

He had single-handedly brought a battle that would go down in history to an end.

But…

*It’s not over yet.*

Jin Taekyung tightened his grip around the spear shaft. He forced his eyes open, though they kept trying to close, and looked toward the west, where desert and wilderness stretched into the distance.

*There’s still something I have to do.*

The light in the young man’s eyes had not gone out as he stared at the endless horizon.

His gaze was already chasing someone who had vanished from sight.

*The Doppelganger.*

Even now, as dawn arrived, the western land where the Doppelganger had disappeared remained shrouded in darkness.

As though its shadow had fallen over it. As though it were a warning of the great war to come.

*I have to go.*

The thought that flashed through Jin Taekyung’s mind was more than a matter of will. It was almost a duty.

He had to move forward. He couldn’t stop here.

He had to pursue the Doppelganger, vanished far to the west, and stop the calamity that would strike in the not-too-distant future.

*Step.*

He moved forward as if entranced.

But his mental strength, already drained to the dregs, wouldn’t let his body move.

He staggered.

*Walk forward.*

His legs failed to receive that simple command in time. A wrenching pain squeezed at his chest, interfering with both body and mind.

*Damn it.*

He’d hit a wall after only his second step.

Feeling his vision slowly tilt, Jin Taekyung stifled a hollow laugh. And just as everything suddenly seemed to go dark—

*Slide. Tap.*

His forehead, pitching forward, touched something solid.

Then a hand reached out from behind him and pulled his collapsing body upright. Two voices slipped into his ringing ears.

“You did good, Jin.”

“Pull yourself together, human.”

Jin Taekyung blinked.

He thought he finally knew who owned the hand holding him up, and what the solid wall in front of him was.

*Magic Johnson. And the Skeleton King.*

They had come.

A human and a monster. No—his friends had come.

To help him.

*Crack.*

The vision that had blurred with that distant pain grew clear again.

Jin Taekyung swallowed the blood on his tongue and raised his head. Familiar faces were waiting for him.

“Ha.”

At the laugh that slipped from his lips, the Skeleton King turned to Magic Johnson, his expression stiff.

“Why’s that ugly bastard grinning like an idiot? Is he finally going crazy?”

“You’re the one who should quit saying idiotic things and shut your mouth. Hey, Jin. Can you hear me?”

“Human. How many fingers am I holding up?”

Jin Taekyung answered weakly.

“I can hear you fine. And I can see your fingers.”

“Tell me how many, you ugly, dim-witted bastard.”

“One. But if you don’t want me to break it, quit waving it around and lower it.”

The Skeleton King had been waggling his middle finger in front of him. He nodded.

“Good. You’re still sane.”

Jin Taekyung gave a quiet snort, then coughed.

“Team Leader Choi… *cough*, how is he?”

“He’s fine. A little injured, but he’s all right.”

“Really? You’re sure?”

“Trust me. I’m not lying.”

Jin Taekyung let out a relieved sigh and straightened his back with effort.

His breathing was still ragged, and his senses dull. But he couldn’t stop here.

“Johnson.”

Sometimes a small gesture or a single word could say everything.

Magic Johnson sensed what he meant from Jin Taekyung’s brief call and answered.

“No.”

“I have to go. You know that.”

“I do.”

Magic Johnson added, his expression hard:

“I also know you need to rest.”

The Grand Mage could see it clearly. Jin Taekyung was barely holding on to consciousness through sheer force of will, already at his limit.

But recklessness belonged to the young.

As it always had with the young man before him.

“Please use Teleport magic.”

“Damn it, Jin. Are you crazy?”

“This isn’t a request.”

“Then as of this moment, I’m leaving the World Hunter Federation.”

“Then do that.”

Looking up at Magic Johnson, who was a head taller than him, Jin Taekyung continued:

“But until I accept your resignation, you’ll have to follow my orders.”

“……!”

“Come on, Johnson.”

Magic Johnson felt his words catch in his throat.

All this talk about resigning was just a clumsy play on words.

But the will in Jin Taekyung’s eyes, that sense of duty holding him to an awareness that seemed on the verge of going out, was the unvarnished truth.

*Damn it.*

He couldn’t bring himself to look into those eyes. He was ashamed of himself for having no choice but to make it.

Magic Johnson squeezed his eyes shut without meaning to, then opened them and gritted his teeth.

“……This is insane. Using Teleport magic with the magical power concentration this high is practically suicide.”

Jin Taekyung smiled faintly.

“That takes me back.”

“What?”

“Sichuan, China. You said the same thing there. And we pulled it off just fine.”

“……!”

“Send me to the place the Prophet—no, the Doppelganger—first revealed.”

Magic Johnson’s pupils trembled as he looked at Jin Taekyung.

He had to stop him. He absolutely had to stop him.

But the Grand Mage’s mind was already calculating, already reaching a reasonable conclusion.

*There’s a good chance it’ll work.*

They had already tried casting Teleport under magical power concentrations like this once, during the battle to defeat the Arch Lich.

It had been possible because Magic Johnson was one of the best mages alive—and because the person he was transporting was Jin Taekyung.

*If it isn’t Teleport magic, if it isn’t Jin… no one else can stop the Doppelganger.*

Jin Taekyung’s proposal was reckless, but it was also a reality he couldn’t ignore.

A considerable amount of time had already passed since the Doppelganger fled the battlefield. Catching up to it would be almost impossible.

But if they used Teleport magic—

And if there was someone who could endure Teleport magic this dangerous, things would be different.

How cruel.

“Fuck.”

Magic Johnson muttered a curse weakly. Jin Taekyung was standing on his own now, without anyone’s help, looking straight at him.

And at Jin Taekyung’s side stood someone who had volunteered to join him on this dangerous journey.

“I’m going with him. You stay here and protect this place.”

The Skeleton King. Lord of the undead, who had overcome even death.

The moment Magic Johnson saw him, he realized there was nowhere left to retreat.

“Promise me one thing.”

*Whummm.*

The staff, filled with mana, trembled. Beyond the dazzling flash, his voice rang out faintly.

“Come back alive. You hear me?”

*Fwoooosh.*

An overwhelming flash of light swallowed the space around them.
## Chapter artifact 824

# Chapter 824

When dawn comes, the darkness retreats.

It was one of those truths as obvious as water flowing downhill. But for those fleeing someone’s pursuit, it wasn’t exactly welcome news.

Especially when the pursuer was such a monster that it was hard to believe he was even human.

*Already?*

The Doppelganger bit its lip as it watched the sky slowly brighten.

It was too soon. No—in truth, it had wasted more time than expected.

*Everything should have been over before daybreak at the latest.*

The Doppelganger knew that no amount of regret or brooding would change reality.

Its carefully laid plans had gone off course long ago. And at the center of it all, at the very beginning, was that bastard.

*Jin Taekyung.*

Throb.

Just thinking of his name sent stabbing pains through the Doppelganger’s body.

Having died at Jin Taekyung’s hands hundreds of times, the Doppelganger shuddered as it remembered his terrifying might.

*I should never have approached him in the first place.*

It had been a mistake. Greed.

After absorbing Yamamoto Genji, it should have left in a hurry—or never revealed itself at all.

*I only needed to take a little more. Just a little.*

Its original targets had been other humans.

The many Hunters left behind in the rear. If it could absorb their mana and life force, it would have achieved its goal.

*Damn it.*

But Jin Taekyung hadn’t let the Doppelganger go easily.

He’d handled it like a slave, never allowing it to leave his sight.

That had been a misfortune for the Doppelganger—and good fortune for every Hunter besides Jin Taekyung.

If the Doppelganger had escaped his grasp, put on Yamamoto Genji’s skin, and headed for the main force in the rear… it would have led countless monsters and fanatics to turn the desert red with blood.

Of course, the outcome had been the opposite.

The monster army was crushed, and the fanatics it had spent considerable effort raising were used as a shield to ensure its escape.

*I can’t believe I got beaten this badly.*

The Doppelganger’s mouth turned bitter.

It had lost a force tens of thousands strong. More than their strength, it regretted losing its private army, soldiers who obeyed its every command without question.

*Still, I confirmed he’s the Chosen One… Master will be pleased.*

Thinking of its master, whose intentions and depths it could never fathom, the Doppelganger shook its head.

For decades, it had secretly manipulated the world from behind an unseen curtain. Yet even it was nothing but a lowly servant before its master.

Just like the foolish humans following it now.

“Are we still far?”

The Doppelganger asked in a deliberately grave voice. The man in black, wrapped from head to toe in a black turban, answered.

“We will arrive shortly, O great Prophet.”

“You’re unbearably slow. At this rate, we could be caught. Pick up the pace.”

“You say we could be caught?”

“Yes. He’s a greater monster than I expected. I don’t know what he might do.”

At the Doppelganger’s words, laced with an unusual mixture of impatience and fear, the dozens of men in black running around it like an escort exchanged glances.

They’d been running at full speed for nearly an hour. And now it wanted them to go even faster?

The man in black carrying the Doppelganger on his back to conserve its strength glanced at it, then finally spoke with care.

“I’m sorry to say this, but… we cannot go any faster.”

“What?”

“Forgive us for our shortcomings, O Prophet.”

Even as he spoke, his feet never stopped moving.

The Doppelganger stared at the back of the fanatic carrying it, then suddenly spoke.

“I see. This is my fault. I pressed you without considering that you were already pushing yourselves.”

“We are unworthy of such words. Please, take them back.”

“No. How could I not understand your hearts? You must have been troubled to leave behind the brothers and sisters you grew up with and abandon the battlefield.”

“That’s…”

“You must have struggled to accept why we had to flee like this, chased away by evil heretics. Isn’t that so?”

The eyes of the men in black wavered beneath their turbans.

Every word from the Doppelganger struck home, as if it could see straight into their hearts.

They had been raised by their leader, Amir, to serve as a personal guard for the Prophet alone.

But the Promised Land they had all longed for was nothing but a barren canyon, and instead of green life and hope, heretics awaited them.

Then came the fierce battle, and their brothers and sisters fell, their blood spraying across the ground.

But they hadn’t cared. They had believed it was a holy war to uphold God’s will.

They had believed their brothers’ and sisters’ deaths were holy martyrdom.

At least, they had—until the Prophet they so revered appeared in a wretched state and left the battlefield.

*Was this really the right choice?*

Escorting the Prophet, they crossed desert and wilderness toward the endless western lands, passing oases along the way.

As they ran without a moment’s rest, a question that had once flickered through their minds began to grow.

God was omniscient and omnipotent. The Prophet was a great oracle.

Then why were they running? Why were they cowardly abandoning the battlefield to flee an enemy force less than a tenth their size?

No matter how hard they tried to suppress them with the unwavering faith they had built over a lifetime, questions they couldn’t quite bury kept welling up from inside.

And at last, in that very moment, the questions spilled from their lips.

“To be honest, I don’t understand.”

The Prophet on his back gave no answer.

Taking the silence as permission, the man in black cautiously continued, eyes fixed on their destination, now visible in the distance.

“If we fought back, we could win. Didn’t you always tell us that God was with us? That we would always be blessed with victory and glory?”

*Whoooosh.*

Wind roared around the figures hurtling forward. Other voices from the men in black joined in.

“We abandoned our brothers and sisters and ran.”

“We’re afraid God will abandon us.”

“Prophet, dare we ask what the Almighty told you?”

That was when the Prophet—no, the Doppelganger, which had been listening in silence—spoke.

“Stop.”

The men in black, who hadn’t paused for even a moment, came to a halt.

Having recovered some strength while being carried on their backs, the Doppelganger set its feet on the ground and muttered:

“We’ve finally arrived.”

The area was desolate and barren.

There was no sign of what had once been said to be the world’s second-largest oil field. On the land where not a blade of grass grew, bleached bones of unknown origin lay scattered.

A land of death.

That was what came to the men in black as they took in the sight. One of them found the courage to ask:

“Where are we?”

The others were just as curious. They were mere servants, following orders; they could hardly presume to guess the will of the great Prophet.

Then, at the next words they heard, everyone’s eyes flew wide open.

“During the time of tribulation known as the Great Cataclysm, this was the land where He stayed, if only for a while.”

“……!”

“……!”

“My master. The master of all creation. He told me: Go to the humans. Wait there for the time to come.”

For a moment, it was as if the air had stopped.

Staring around in a daze, the men in black dropped to their knees as one and cried out at the top of their lungs.

“Ooh, oooooh…!”

“Inshallah!”

“God is great!”

Their reaction was only natural.

The Prophet served only one person, and this was the land where that person had once descended. It was worthy of being called the Sacred Land.

Then, above their heads as they lay flat and cried out for God’s blessing, came a voice.

“You said you were afraid God would abandon you.”

Its tone was gentle, like someone soothing a fussy child.

“You said you wanted to hear what He had told me.”

A hand brushed over the hair of the worshipers prostrating themselves upon finally reaching the Sacred Land. It was warm, like a hand tending the painful wound of a patient groaning in agony.

“Then I’ll tell you.”

But the gaze looking down on them was neither gentle nor warm.

It was a change like the desert sun turning into a bitter northern blizzard. The voice that followed was cold as ice.

“Just how worthless you are.”

At that moment—

*Boom! Thud-thud.*

The men in black, overcome with emotion, blinked.

When they raised their heads from the ground, red blood and pieces of flesh were scattered all around them.

“Huh…?”

A dazed voice slipped from someone’s lips.

It was a pure question—and a reality they couldn’t accept.

Before they could find an answer, a deep darkness fell over the men in black.

*Whoooosh.*

A chill ran down their spines. Their hands and feet, beyond their control, stiffened like stone.

Their bodies, honed through a lifetime of training, their mana, and the swords at their waists were all useless now.

Ah.

A single groan.

Overcome by a vast terror and shock they had never felt before, the men in black stared at the darkness bearing down on them.

The darkness was as smooth as a mirror, and their faces were reflected in it, clear as day.

*This is…*

Their voices wouldn’t come out. Their bodies had gone rigid.

Unable even to scream, the men in black moved their eyes. Above the darkness enveloping them, they saw a face.

The great Prophet who would lead them all to the Promised Land.

No—the thing they had believed was the Prophet was looking down at them, smiling.

It was leading them not to death, or anything else, but into a bottomless pit within a dreadful abyss.

“Listen, you fools. You weak, worthless humans.”

*Fwoooosh.*

The darkness drained the fresh vitality from their bodies. Dozens of pale souls flowed as if entranced toward the Doppelganger within the darkness.

“There is only one king in this world.”

The darkness swallowed the blood flowing from the seven openings in their faces. Their taut skin shriveled, and their bones crumbled.

Death drawing near. Or perhaps the abyss.

As their vision plunged headlong into the bottomless pit, they heard the devil’s final words.

—God…

Had already abandoned you.

The words echoed faintly.

That was the end.

Where the darkness had fallen, twenty mummified corpses remained, kneeling as though in worship.

And only one being remained, having taken new life as it had for the past several hundred years.

Or so it thought.

*Fwoooosh.*

That was, until a dazzling beam of light erupted in the air above the ruins.

Until blue-white flames surged and poured forth from within that distant radiance.

*Kwaaaaaang!*

Powerful flames washed the Doppelganger’s eyes blue.

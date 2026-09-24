# Checkpoint Review — 965–969

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

# Chapters 965–969

## Plot

Peng Cheolhu and two thousand Hebei Peng Family fighters arrive at Eight Spring Gorge, breaking the steppe army’s formation and interrupting Jamukha’s attack on Jin Mukyung. Cheolhu and Jamukha resume their duel while Jin Wikyung leads Shanxi’s fighters toward the gorge. An unidentified force fires thousands of arrows into the battlefield.

Cheolhu recognizes Jamukha as the eastern-steppe chieftain he defeated more than fifty years earlier. Jamukha reveals that Murong Baek spared and recruited him, helping him rebuild his power in the west as part of Dark Heaven. Murong’s larger organization is preparing a bridgehead for an advance into the Central Plains, and supplied the Temporary Strength Pills scattered across the steppe. As Cheolhu nearly defeats Jamukha, Murong arrives and betrays Cheolhu, his longtime friend and former rival, striking him from behind. Cheolhu is buried beneath a collapsing cliff but remains alive.

Murong rebukes Jamukha for disobeying orders and nearly taking an improved Temporary Strength Pill, whose severe addictive effects make it too dangerous for him. Murong then finds Jin Mukyung, Cheol Mubaek, and Wipeng beneath the rubble and moves to attack them. A blue-white-flamed spear smashes through the cliff, interrupting him.

## Continuity

- Murong Baek spared Jamukha decades ago, recruited him into Dark Heaven, and directs his military role. Jamukha’s crescent saber is shattered; his shoulder is nearly half severed, and he expects to recover by regulating his qi.
- Murong betrayed Peng Cheolhu, who remains alive beneath the rubble. Murong plans to ambush the arriving Huashan and Zhongnan reinforcements and eliminate witnesses to Dark Heaven’s actions.
- Jin Mukyung, Cheol Mubaek, and Wipeng are beneath the collapsed cliff; their condition is unresolved. An unidentified spear bearing blue-white flames has interrupted Murong’s attack.
- The identity of the force that fired thousands of arrows is unknown.
- The awakened figure behind Jamukha’s recruiter and the larger organization’s plan remain unknown. The Emperor’s Blood Soul Gu treatment and the Martial God’s identity and connection to the chosen one and the Bow Saint remain unresolved.

## Translation Decisions

- Retain “Temporary Strength Pill” for 잠력단 and “Force” for 강기.
- Render 모용백 as “Murong Baek”; use “Family Head Murong” for 모용가주 when used as a form of address.
- Distinguish Peng Cheolhu’s former title, “Thunderbolt Saber,” from his current title, “Thunderbolt Saber King.”

## Durable state

{
  "active_continuity": [
    "Murong Baek spared Jamukha decades ago, recruited him into Dark Heaven, and now directs his military role.",
    "Murong betrayed his longtime friend Peng Cheolhu and intends to kill him; Peng is alive beneath the rubble.",
    "Murong plans to ambush the arriving Huashan and Zhongnan reinforcements and eliminate witnesses to Dark Heaven's actions.",
    "Jamukha did not take the improved Temporary Strength Pill, whose severe addictive effects make it unsuitable for him; his shoulder is nearly half severed.",
    "Jin Mukyung, Cheol Mubaek, and Wipeng are beneath the collapsed cliff; their condition is unresolved.",
    "An unidentified spear bearing blue-white flames has interrupted Murong's attack.",
    "The identity of the larger organization’s awakened figure and its plan remain unknown.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment requiring him to die once remains unresolved.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown."
  ],
  "continuity_sources": [
    969
  ],
  "open_questions": [
    "Who wielded the blue-white-flamed spear, and what happens to the people beneath the rubble?",
    "What is Murong Baek’s full plan for Dark Heaven and the arriving reinforcements?",
    "Who is the awakened figure behind Jamukha’s recruiter, and what is the larger organization’s plan?",
    "What are the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "Can the Emperor be treated for Blood Soul Gu, and what does the treatment requiring him to die once entail?"
  ],
  "safe_through": 969,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 965

# Chapter 965

*Boooo! Boooooo!*

The horns echoed in wave after wave, but their sound was quite different from before.

What should have joined into one great roar was breaking off in fits and starts, and there was even a hint of urgency in it.

So even the people of Shanxi, who didn’t know exactly what the horns meant, could sense that something unexpected had happened to the enemy before them.

And they could sense, too, that this unforeseen turn might bring them a stroke of luck they’d never imagined.

“Now! Now’s our chance!”

“Don’t fall back! Keep pressing them!”

At this moment, not one person among the people of Shanxi wondered what had happened.

Not a single one.

They had all already steeled themselves to die. They had stayed here to protect their homes, their families, and their friends, and were facing the invaders head-on.

Those who came to take, and those who stayed to protect.

The depth of their desperation was different. So was the weight of their resolve.

The people of Shanxi summoned every last ounce of strength, took unsteady steps, and swung weapons that felt heavier than ever.

At the enemies who had faltered, realizing what the horns meant.

At the cruel invaders from the steppe.

*Klang!*

*Thud, thud!*

Sparks burst from the clash of sharp blades.

The Keshiks, frozen in confusion, rushed to fight back. But that moment of distraction gave the Shanxi defenders, burning with fury, their opening.

*Shhk!*

Saber Force surged along a crescent saber, sending limbs flying from three or four men. Yet even as they writhed in agony, the wounded men whose lives still clung to them threw themselves at a Keshik squad leader with all their strength.

“Y-you crazy bastards…!”

*Crack!*

A sickening sound of flesh splitting. The shout cut off abruptly.

There weren’t many people who could survive an axe embedded in the crown of their head.

No—there weren’t any.

“That’s what you get for setting your sights on Shanxi Province, you damned barbarian.”

*Ptooey.*

An unknown martial artist spat phlegm onto the squad leader’s corpse, whose eyes were still wide open in death. Then, carefully, he pried the sword from the hand of his comrade, who had fulfilled his final duty and closed his eyes in peace.

In a muffled voice, he said goodbye.

“Rest here a little while. I’ll kill just ten more and be right back.”

He knew the truth.

No—all the people of Shanxi knew.

They might never come back.

They might never meet again in this life.

But knowing that changed nothing.

Nothing but their resolve to fight to the death.

“Yaaaaah!”

A cry like a scream shook the gorge.

It roused the deep night, pierced the resonance pouring from dozens of horns, and kept traveling farther and farther away.

It swept past grass darkened by night and ground packed hard by countless hooves, until at last it reached a host of horsemen cresting a high hill and charging toward the battlefield.

The towering old man at their head smiled as he heard the fierce cry rising from the people of Shanxi.

“Yes. I hear you loud and clear. This old man does—and so do we all.”

*Thud, thud, thud!*

The thunder of pounding hooves shook the earth.

The wind carried the stench of blood deep into their nostrils. The ceaseless clangor of steel made blood that had gone cold begin to boil.

“Thank you. You’ve held out well.”

His mutter faded beneath the wind rushing past his whole body.

The towering old man spoke from the heart, to those who had fought without giving an inch in the worst of circumstances.

To those still desperately facing an overwhelming enemy.

He offered them his respect, his gratitude, and his apology.

“We swore to stand together beneath one banner. But some of us turned away when our neighbors were in danger, afraid our own fence would come crashing down.”

His voice rang clear amid the pounding hooves.

It was a shame he reminded himself of—and a rebuke he cast at everyone racing behind him.

“What’s spilled can’t be poured back into the cup, and an arrow loosed from the bow can’t be called back. But…”

The Jin Family of Taiyuan and the people of Shanxi had not been easily broken.

They were still here, burning like a fire fed by countless lives.

Their cup had not yet shattered, and the enemies’ arrows might still be on the string.

“Look at them. And remember this well!”

A shout, rising suddenly like a wildfire, tore through the night air.

The old man pointed toward the gorge, where a fierce battle was raging.

The steppe army was moving toward them with horns blaring, just below the hill and rapidly drawing closer. He ignored it and continued shouting.

“They are our neighbors, our friends, our comrades-in-arms—people who swore beneath the same banner! And they are the very people our family tried to turn its back on!”

The old man was ashamed.

Ashamed of the family that had tried to abandon the people of Shanxi. Ashamed that he had wavered, if only for a moment, at such a shameful proposal.

But he had not forgotten.

He remembered the vow they had made in days gone by: to rise together against the injustice of Dark Heaven and save a world sunk in misery.

That was why he had ridden here with all his strength.

Over and over, he had prayed they would hold out until the end.

Over and over, he had prayed they would not arrive too late.

And the people of Shanxi had not betrayed his desperate wish.

They had given him another chance to unfurl the banner he had been too ashamed to raise.

“What are you?”

At the old man’s roar, like the bellow of a beast, the tightly shut lips of two thousand men opened as one.

“We are fighters!”

Fighters.

For a very long time, they had called themselves fighters, not martial artists.

To them, martial arts were not something to practice and polish for its own sake. They were tools for battle.

“And what is an enemy to you?”

At the old man’s question, shouted once more, the eyes of those advancing beyond the darkness flashed.

“Weak losers who will kneel before a fighter’s spear and blade!”

*Thud, thud, thud!*

*Boooooo!*

The thunder of hooves and the blare of horns rang out one after another.

The sight of countless horsemen charging toward them through a hazy cloud of dust, just over three hundred yards away, did not shake a single one of them.

They were valiant fighters, and those men were losers soon to be broken and crushed.

“I’ll ask you one last time!”

The old man cried out. The enormous saber in his hand now scattered dazzling flashes of light.

“Who are we!”

The distance to the enemy closed. Looking at the wave of lances glinting in the darkness, the two thousand fighters shouted with one voice:

“We are the masters of Hebei!”

At that very moment—

*Flap.*

The twenty or so standard-bearers, who had waited for this moment and this moment alone for the past several days, raised their flags with all their strength.

A blue tiger that looked ready to leap to life, and four characters stitched in a rough hand, billowed fiercely in the rushing wind.

At last, they revealed themselves to everyone on the battlefield.

The Hebei Peng Family.

The Tiger of the North. One of the Five Great Families of the world.

And the towering old man leading them all was a great tiger, grown even stronger through the long years.

“Charge!”

With a roar that shook earth and sky, the old man kicked off his saddle and shot toward the countless enemies surging right up to him.

*Rrrumble.*

Thunder that froze body and mind.

The old man—no, the Thunderbolt Saber King’s great saber became a massive bolt of lightning, sweeping through the dense forest of spears and blades.

*Kaboom!*

Dazzling light and a deafening boom swallowed everything around them.

Behind the old tiger, who rampaged wildly and shattered the enemy formation, two thousand fighters burst through the thick haze of blood and split the enemy ranks like a single spear.

*Crack!*

In the deep of night, when even the birds slept—

The battle, and the Double Ninth Festival, were not over yet.

* * *

Everyone heard it.

And everyone saw it.

The strange thunder that rang out from the ground, not the sky.

Beyond the dazzling flash that accompanied the boom, dozens of flags flapped, heavy with blood, and the enemy shrieked.

“The Hebei Peng Family! It’s the Hebei Peng Family!”

“T-The Thunderbolt Saber King…!”

The first was the Shanxi defenders’ cry of joy; the second, the nomads’ lament.

Peng Cheolhu, the Thunderbolt Saber King.

His name and title were no relics of a bygone age.

An old tiger in a pack might lose its strength and standing, but the teeth and claws of the great tiger called the Thunderbolt Saber King had only grown sharper.

What’s more, the Hebei Peng Family was a renowned great family that ruled the north alongside the Murong Family.

In that sense, the Thunderbolt Saber King and the martial artists of Hebei following him were showing exactly how they had earned the titles of Ten Kings and one of the Five Great Families.

*Boooo! Boooooo!*

Listening to the horns blaring without pause, Jamukha suddenly thought:

*This is going to be a long night.*

But he wasn’t flustered.

The Shanxi defenders, united around the Jin Family of Taiyuan, had fought harder than he’d expected. But the Hebei Peng Family’s support was still within the range of what he had anticipated.

And so was the Thunderbolt Saber King himself.

“Just as that person said.”

At Jamukha’s words, spoken almost to himself, Jin Mukyung’s face stiffened. He had been trying to steady himself against his own emotions.

“What did you just say?”

“The Thunderbolt Saber King has such a fiery temper that he’ll act without thinking about what comes after. So even if he were to lead the Hebei Peng Family to Shanxi’s aid, it wouldn’t be surprising.”

Jamukha continued smoothly, then added in a low voice:

“That’s what they said. I remember clearly.”

“……!”

“Don’t look at me like that. If you thought we hadn’t anticipated even something this obvious, I’d be very disappointed in you.”

“W-we?”

“Yes. We.”

Jamukha nodded slightly, then clicked his tongue as he looked at Jin Mukyung.

“Too bad. If you’d taken my hand, you could have been part of ‘we,’ too.”

*Step.*

The moment Jamukha began walking as casually as if he were out for a stroll—

*Shwack!*

The crescent saber in his hand cut through the air.

The strike was so precise and swift it made Jin Mukyung’s skin crawl. He widened his eyes and twisted his body aside.

*Shhk!*

His hair fluttered. Blood sprayed from the gash cut into his forehead by the pressure alone, blinding him.

*Damn it.*

Jin Mukyung’s body jerked to a halt for an instant. His two years of training had made losing his sight no problem—but the blood in his eyes was enough to shake his composure.

And for Jamukha, it was the perfect opening.

A chance to uproot the young Sword Demon, still unfinished but full of potential.

“If you’d put that collar on yourself, this wouldn’t have happened.”

Jamukha raised his crescent saber, his voice low.

Calmness, personal martial prowess—

He surpassed the Demon Bird in every respect. Even facing Jin Mukyung, exhausted to the limit, he did not let his guard down.

He simply, steadily and without a word, found the fastest, most precise path and brought his blade down.

*Farewell, young Sword Demon.*

And just as blue-green Force ran along the smooth blade, about to cut through the air—

*Whoosh! Whoom!*

With a fearsome whistle, a great saber shot in like a bolt of lightning and plunged between Jamukha and Jin Mukyung.

*Kaboom!*

Beyond the boom that sounded as though the sky had split and the cloud of dust rising pale in its wake, the towering old man appeared. He bared his teeth in a grin at Jamukha.

“Ready to die?”

Drenched in blood from head to toe, the Thunderbolt Saber King drew a smooth reply from Jamukha, in fluent Chinese.

“Thanks for saying what I was about to.”

Nothing had changed for Jamukha.

Nothing at all.
## Chapter artifact 966

# Chapter 966

Assuming two martial artists were evenly matched, what was the most decisive factor in a life-and-death duel? For ages, that question had been a favorite topic among the gossips of the martial world.

Some said it was superior internal energy and peerless martial arts. Others named the presence of a divine weapon as the most important factor. Still others insisted it was an unshakable mindset and outstanding physical ability.

Yet every one of those opinions was both right and wrong.

Masters who had reached a certain realm knew. They had felt it firsthand.

In a life-and-death duel, a single difference—however small, however trivial it might seem—could decide the outcome.

That was why they often all agreed on this:

*It doesn’t matter all that much what martial art you’ve learned. What matters most is having the eyes and instincts to see through your opponent’s movements.*

And in that moment, everyone filling the gorge understood exactly what those words meant—words that had once seemed so far removed from them.

*Whoosh! Kaboom!*

They couldn’t see it. They couldn’t sense it, either.

They simply stared, dazed, for a moment forgetting even to swing their blades at the enemies in front of them.

Beyond the endless flashes and thunderous booms, three figures were locked together, moving too fast to see.

*Whoom!*

An absurdly massive saber cleaved through the air. The mighty Force along its edge tore through Jamukha’s body with the wind.

Or seemed to.

*Shhk.*

A single step.

Jamukha’s form blurred for an instant, then reappeared about ten feet away.

He had dodged the attack with a ghostly movement. Just as he surged toward the Thunderbolt Saber King, a faint whistle sounded from beyond his blind spot.

*Shwaa!*

In that instant, Jamukha realized anew:

The enemy he had to defeat here today wasn’t just the Thunderbolt Saber King.

*Shk—KABOOM!*

The crescent saber met a gleaming white blade.

Amid the shock wave and deafening boom that reverberated through the gorge, Jamukha took a step back, caught off guard. A smile formed at the corner of his mouth.

*Impressive. Even better than I expected.*

His gaze fell on Jin Mukyung, who had been driven back, carving a deep furrow through the ground.

The young Sword Demon of the Jin Family of Taiyuan had delivered an unexpected strike with a body battered from head to toe.

And at last, Jamukha understood.

How Jin Mukyung, who had only just broken through the Supreme Peak barrier, had defeated the Demon Bird, a master who had reached full mastery of his realm.

There was neither form nor pattern to the sword Mukyung wielded—nothing that could be called the fundamentals of martial arts.

Only One Strike.

He simply found the fastest, most perfect path to end his opponent’s life, then moved along it.

And that strike, imbued with an intent to kill, had far greater power than Mukyung’s own martial prowess should have allowed.

Powerful enough to defeat the Demon Bird, a superior master, in the realm of Supreme Peak, where a single form could decide the fight.

But…

*This is as far as it goes.*

Without a word anyone could hear, Jamukha shook out both arms.

Green Force, like the vast grasslands where he had been born and raised, surged along his crescent saber and his empty hand.

*Fwoosh!*

Beyond the blinding flash swelling to an immense size, the two streams of Force shot in different directions.

One toward the Thunderbolt Saber King, who was bringing his great saber down with enough force to cleave the world in two.

The other toward Jin Mukyung, who was staggering and swallowing blood.

The result was far beyond what one man had expected.

*Craaaack!*

The Thunderbolt Saber King’s eyes widened as he stared at the two blades locked together without the slightest give.

*What in the—!*

He was a warrior to the bone. Even now, a living legend who had made his name in the great upheaval of the Great Faction War, he never underestimated an opponent standing before him.

And yet his full-powered strike had been blocked.

With astonishing ease.

As if his opponent had seen through the form—and the flow—of the martial art he had just used.

“How could you…!”

A voice thick with confusion and anger slipped through his lips.

The two blades remained locked in midair, their wielders’ bodies still apart. Jamukha looked at the Thunderbolt Saber King with calm eyes.

“I’m disappointed. Shouldn’t you have saved your much younger junior first, Thunderbolt Saber King?”

“……!”

The Thunderbolt Saber King’s wide eyes wavered for an instant.

Over Jamukha’s shoulder, he belatedly saw Jin Mukyung on his knees, vomiting blood, unable to withstand the might of the palm strike.

*Damn it.*

It was a mistake.

No—a devastating misjudgment.

Jamukha was stronger than he had thought, and he was a far more formidable master, with deeper secrets.

*BOOM!*

After their strength had been locked in a fierce contest, the sabers finally tore apart with a deafening boom.

The Thunderbolt Saber King let the force of the impact roll through him, then brought his great saber down at Jamukha again.

*Fwoosh!*

A strike combining his innate divine strength with several jiazi of internal energy.

Born the third son of the Hebei Peng Family, he had become its Family Head and the Thunderbolt Saber King through the family’s peerless martial art, the Primordial Thunderbolt Saber. Now it fell like a bolt of lightning.

With enough force to split the world in two along with the enemy before him.

*Shing! KRAAAASH!*

A keen slicing sound rang out as the gorge shook.

But the Thunderbolt Saber King, whose strike had lived up to the name of one of the Ten Kings, swept his deep-set gaze across the area as a hazy cloud of dust billowed into the air.

*Where is he?*

He had swung his saber countless times and cut down more than a thousand people, by his estimate.

So he knew better than anyone:

The strike he had just delivered had cut through wind and earth—not a man’s flesh and bone.

“You bastard!”

The Thunderbolt Saber King roared like a tiger and swung his great saber.

Beyond the dust cloud scattering under the force of his blow, Jamukha was there, crouched and silent, like a wolf preparing to hunt.

*Hup.*

Neither waited for the other.

As if on cue, both men shot toward each other.

No one there could see the teeth and claws of the great tiger from the Hebei Peng Family or the wolf of the Great Steppe—so fast and so powerful were they.

*BOOM! BOOM! KRAAA-BOOM!*

Every time the two sabers collided, a boom like cannon fire rang out.

The screams of those swept up in the tremendous shock waves surging across the gorge piled over the noise.

“Gwaaaah!”

Arms and legs tore from bodies. Fountains of blood shot into the air.

Beyond a thick haze of blood, flashes of light kept sparking without pause. The nomads caught at the heart of the calamity fled for their lives.

Some ran toward the entrance at the rear, where it was relatively safe.

Others ran toward the exit on the opposite side.

But those with no choice but to take the latter route found themselves face-to-face with a forest of spears and blades, now almost upon them.

*Thud-thud-thud!*

Dozens of nomads, unable to dodge the arrows raining down from the still-standing earthen rampart, fell like pincushions. The blades in the hands of Shanxi fighters flashed as they pressed forward, trampling the crumbling bodies.

*Shhk!*

His body was exhausted, but his sword had lost none of its sharpness.

Jin Wikyung, who had cut through a crescent saber and its wielder, steadied his ragged breathing and moved forward.

Toward the enemies inside the gorge, who had seemed endless no matter how many they killed, but were now being swept away like a wave.

Toward the heart of the gorge, where two monsters were locked in a fierce battle.

Danger?

It didn’t matter.

The arrow had already been loosed. If they retreated now, only a defeat they could never undo awaited them all.

*We have to seize the gorge and drive them out as soon as possible. That’s our only chance.*

The arrival of the Hebei Peng Family, led by the Thunderbolt Saber King, had greatly improved the desperate battle situation. But Jin Wikyung’s cool head saw every detail of the position his side was in.

*This momentum is only temporary. If the enemy regains their composure, the tide will turn again.*

The Hebei Peng Family was undoubtedly strong.

Beyond its home province of Hebei, it was a power that ruled the entire north alongside the Murong Family. And the Thunderbolt Saber King, a peerless Supreme Peak master, was a force who could take on an army all by himself.

But their enemy was just as strong.

Jamukha was fighting the Thunderbolt Saber King without giving up an inch, and beyond the gorge, tens of thousands of steppe warriors were still fighting the Hebei Peng Family.

Their morale had been broken, but they still outnumbered the enemy ten to one—perhaps more.

Even after thousands of their soldiers had been killed or put out of action in the narrow gorge, the fundamental gap in their forces remained.

There was only one answer.

To win a battle that was still so evenly matched, they had to keep advancing with everything they had until the very end.

“Follow me!”

Jin Wikyung shouted at the top of his lungs and charged.

Dragging along his now blood-soaked body, he plunged into the collapsing enemy line and swung his sword like a madman.

*Craaaack!*

He had too much to protect.

The people who followed him, ready to give their lives.

The land where they had been born and raised.

And finally, his little brother, staggering back to his feet in the distance despite his grievous internal injuries.

Jin Wikyung couldn’t give up a single thing.

Not one.

* * *

Apart from everything else, Jin Wikyung’s judgment had been right.

Outside the gorge, where the terrain opened into a broad basin instead of narrowing like a jar at its entrance, the battle was continuing without either side giving an inch.

*Thud-thud-thud!*

*Shhk! KRAAA-BOOM!*

The Hebei Peng Family and the nomads.

The nomads and the Hebei Peng Family.

The two forces had shared a border and spent many years at odds. Now they swung their weapons and screamed at each other as if they’d met their sworn enemy in the fight of their lives.

“They’re weak barbarians! Crush them in one blow!”

“Brothers of the Great Steppe! Are you going to retreat before a handful of Han Chinese?”

Those cries, carried on the wind as they rang out against each other, perfectly reflected the situation they were in.

Each individual martial artist of the Hebei Peng Family was a cut above the nomads. But outnumbering them more than ten to one, the nomads pressed in without pause, surrounding them on all sides.

“Attack! Don’t fall back—surround them!”

“Break through!”

The clash of sharp spears and enormous shields.

If the Thunderbolt Saber King had stayed here, the Hebei Peng Family would have held the advantage. But after shaking the enemy ranks in a fierce assault, he had headed into the gorge with a portion of his elite. The nomads had quickly closed the breach in their encirclement and launched a counterattack.

A trace of unease lingered in their hearts.

*If this keeps up…*

*This is bad. Very bad.*

The Keshik centurions Jamukha had left outside the gorge exchanged grim looks.

The Hebei Peng Family’s sudden arrival had sent the morale of the Shanxi fighters soaring, while brutally crushing the nomads’ momentum.

The imposing presence of a master like the Thunderbolt Saber King.

And the fame of the Hebei Peng Family, which had kept the nomads from daring to encroach on Hebei.

Some of the centurions were already unconsciously reaching inside their robes.

*If we use that now, we could turn this battle around in an instant.*

But the thought that had crossed their minds quickly faded.

They remembered Jamukha’s order—the command of the absolute ruler of the Great Steppe, the lord they served.

*“No one uses it without my order. This won’t be the last battle we have to fight.”*

There wasn’t the slightest hint of objection or doubt.

Not simply because of the relationship between lord and subject, but because it was Jamukha who had said it.

Jamukha was always coolheaded and decisive. Everything he had said so far had been right, and he would be right this time, too.

That wouldn’t change even if the opponent was the Thunderbolt Saber King.

There was only one small question.

*What made him so certain?*

Before they reached Shanxi Province, Jamukha had already predicted that other enemies would help the Jin Family of Taiyuan oppose them.

And he had declared with an unwavering voice:

*“Nothing will change. Nothing at all.”*

The centurions, recalling those words from several days ago, watched the battlefield with questioning eyes.

*Rrrrattle.*

Beyond the vast basin, where tens of thousands of enemies and allies were tangled together, a group suddenly emerged from the darkness. All at once, they drew their bows.

*Shwaaaaa!*

Beneath the storm clouds, thousands of arrowheads flashed as they sliced through the wind and plunged down.
## Chapter artifact 967

# Chapter 967

To a martial artist, martial arts are like fingerprints: no two are quite alike.

Even when disciples study under the same master, learn the same martial arts, and perform the same movements according to the same formulas, their styles differ according to their temperaments and physical traits.

A man who doesn’t fear death might use a sword technique more boldly than prescribed. Someone with short arms and legs might widen their stride when using a footwork technique.

And in that sense, at this very moment, Peng Cheolhu, the Thunderbolt Saber King, was feeling a strange sense of déjà vu.

*BOOM! BOOM! KRAAA-BOOM!*

The two saber blades clashed without pause, accompanied by a barrage of fierce impacts.

Beyond them, Jamukha’s calm face—and each and every one of his movements—seemed more familiar to the Thunderbolt Saber King the longer he watched.

*What is it?*

For a martial artist who had reached a high realm, letting his mind wander during a life-and-death duel was a taboo.

Yet the Thunderbolt Saber King kept his eyes on Jamukha, violating that taboo, until at last he recalled a scene buried deep in the dusty recesses of his memory.

*Could it be?*

His eyes suddenly flew wide.

Jamukha didn’t miss the instant opening the Thunderbolt Saber King showed. He swung his crescent saber down with all his might.

*BOOM! KRRRACK!*

Two sabers worthy of being called treasured blades met, scattering flashes of light.

As their blades strained against each other without giving an inch, the Thunderbolt Saber King looked past them at Jamukha, his gaze sinking deep.

“I wondered where a barbarian like you had come from… Now I see we’ve met before.”

Jamukha fell silent for a moment, then spoke.

His Central Plains language was so fluent that no nomad from the western steppe, so far removed from the Central Plains, should have been able to speak it.

“Now that you finally remember, I see your head’s still as thick as ever, Thunderbolt Saber Peng Cheolhu.”

“Thunderbolt Saber. There was a time when they called me that.”

The Thunderbolt Saber King murmured as if to himself.

It was only one character different from his current title, but the years contained in that difference were vast indeed.

The first time the two had crossed paths was before the unprecedented Great War called the Great Faction War, back when Peng Cheolhu was the Lesser Family Head of the Hebei Peng Family.

*I suspected as much. He’s that barbarian from back then.*

The Thunderbolt Saber King looked at Jamukha with fresh eyes.

It was a fragment of a memory from more than half a century ago.

And yet he could still dredge up that tiny fragment from his aging mind because the young nomad, who had rampaged like a wolf despite his terrible injuries, had left such a powerful impression on him.

*Right. That’s how it was.*

Nomads crossed the Great Wall and invaded the borders.

People stood against them to protect their homes and possessions.

Such things happened all the time along the frontier near the Great Steppe. Hebei, adjacent to the vast grasslands and home to the great tree that was the Peng Family, was no exception.

But what made the two men’s encounter unusual was that a young chieftain, rising to prominence amid the turmoil of the eastern steppe, had led thousands of warriors to attack Hebei.

Even along the frontier, where raids and defenses came in endless cycles, such a thing was far from common.

No—in those days, it was the first large-scale invasion in over a decade.

Peng Cheolhu, then the Lesser Family Head, led his family in place of its ailing Family Head. The Murong Family, recognizing the gravity of the situation, sent a thousand elite fighters, including their own Lesser Family Head, to help.

The Hebei Peng Family and the Murong Family, each occupying a place among the Five Great Families.

And on top of that, the elite forces led by the two families’ Lesser Family Heads, who were emerging as the greatest young masters of their generation.

Before the Great Faction War, the two families had been at odds over supremacy in the north. Their dramatic alliance proved enough to secure a fitting reward.

A flawless victory, without a single misstep.

Or perhaps a glorious triumph.

No one in the world questioned the use of those words.

Their victory had been that complete. The young chieftain of the eastern steppe, thoroughly defeated by the Hebei Peng Family led by Peng Cheolhu, barely evaded the pursuing Murong Family, which had arrived in time, and disappeared.

Leaving behind only the blood of the countless warriors who had followed him.

Just like that, he vanished without a trace.

That was what everyone had believed, including the Thunderbolt Saber King.

Until they met again here today.

“I never thought you’d still be alive. You sure have a stubborn hold on life.”

They said a needle in a bag would eventually poke through.

Those as sharp as needles would inevitably reveal themselves.

Even if the bag wasn’t a bag at all, but the vast steppe.

Yet the young chieftain, with ambition to match his skill, had not shown himself for more than half a century. The nomads never invaded Hebei again.

That was why the Thunderbolt Saber King had forgotten Jamukha for so long.

Barbarian though he was, the man had been skilled enough that there must have been some reason he hadn’t risen again.

The Thunderbolt Saber King had assumed that his injuries from that day had killed him, or that he had fallen victim to another conflict on the steppe.

Whatever the reason, the conclusion was the same: he was dead.

That was what he had believed.

“I should’ve done whatever it took to root you out back then—to tear out the source of this trouble.”

Beyond their locked blades, the Thunderbolt Saber King let out a quiet sigh. His figure was reflected in Jamukha’s gleaming eyes.

“I couldn’t die. Not before I repaid an old debt.”

Jamukha spat the words out.

How could he forget that bitter past?

Defeated, he had left the eastern steppe with the surviving members of his tribe. After marching for thousands of li, he reached the distant western edge and raised a ger of his own.

A place where he couldn’t see the hated banners of the Hebei Peng Family.

A place where he could escape the wolves waiting to tear him apart if he fell—and where he could settle anew and wait for his chance to rise again.

Fifty years had flowed by like a river.

So much had changed.

The new name he had taken to avoid a possible pursuit—Jamukha—had become a symbol of authority across the western steppe. His ranks teemed with fine steeds and warriors like hunting dogs. The few dozen gers he had started with had grown into tens of thousands of households.

But even after he had become all but the king of the steppe, Jamukha had never forgotten.

Peng Cheolhu’s saber, which had torn through his body like a bolt of lightning.

The memory of the day he had suffered that humiliating defeat.

*Wooooom.*

The green Force of the crescent saber vibrated through the air as it swelled larger and larger.

At this moment, Jamukha’s gaze on the Thunderbolt Saber King held the past, still unavenged.

“Thunderbolt Saber. No—Thunderbolt Saber King Peng Cheolhu.”

The young chieftain, once driven by the ambition to restore his ancestors’ achievements, had returned as the absolute ruler of the steppe, leading a mighty army. The Lesser Family Head of the Hebei Peng Family, who had taken everything from him, had risen through the Great Faction War to become one of the Ten Kings, a great tree that held up the martial world.

But one thing had never changed: their old grudge.

“Do you still not understand?”

*Krrrrk.*

The crescent saber, engulfed in radiant green Force, pressed down on the great saber.

The Thunderbolt Saber King groaned as his blade trembled. Jamukha’s lips twisted.

“I waited. I waited for you—for the Hebei Peng Family—to show up here.”

“……!”

The Thunderbolt Saber King’s eyes flew wide at the unexpected words.

*KA-BOOM!*

With a thunderclap that seemed to split the sky, the great saber—until then like a colossal wall—was forced back, unable to withstand the crescent saber’s power.

*KRAAAASH!*

A gale swept through.

Part of the rocky cliff cracked and burst apart under the terrible pressure.

Yet even amid the dust clouds swirling all around him, Jamukha moved with precision and speed.

*Shwaa!*

Space split along the saber’s path.

Green Force streamed from the crescent-shaped blade and surged toward the Thunderbolt Saber King as he retreated.

*BOOM! BOOM!*

The roar of the two sabers colliding had already gone beyond the realm of steel.

Jamukha’s gaze, which had been so deeply composed throughout, and his voice, slipping between his lips, were now boiling like lava.

Just like—

“I’ll kill every last one of you!”

—some young chieftain from long ago, forced to leave after losing everything in a bitter defeat.

*FWOOOSH!*

Green Force erupted in a burst, overflowing with all his strength.

Like the first light of dawn arriving early, that dazzling, mighty beam illuminated the gorge as it slashed diagonally toward the Thunderbolt Saber King.

*Shhk!*

Amid the brilliant flash, a single, chilling sound of a blade cutting through flesh rang out.

“Cough.”

*Thud, thud.*

The Thunderbolt Saber King stumbled backward, spat out a mouthful of blood, and looked at Jamukha.

His deeply furrowed brow was twisted with pain from his internal injuries.

“…Impressive. Truly impressive.”

There was no sarcasm or pretense in his words. He meant them.

At this moment, the Thunderbolt Saber King was admiring him as a martial artist, and as a warrior who had carried on the Peng Family’s legacy.

Jamukha’s patience, which had endured such a long stretch of time in order to avenge his defeat.

His astonishing martial prowess.

And…

Jamukha himself—a man who had held on to his reason until the very end, even with revenge almost within reach.

“How did you think to pull back? You had the perfect chance.”

Even an enemy deserved proper respect if he had shown courage and fighting spirit worthy of praise.

But Jamukha didn’t answer the Thunderbolt Saber King’s question.

No—he couldn’t answer.

*Crack.*

A faint fracture, so slight it could only be heard if you listened closely. The crescent saber trembled, and in the next instant—

*KA-BOOM!*

—his crescent saber shattered into pieces. Blood spraying from Jamukha’s shoulder blade rained onto the steel fragments.

*FWASH! THUD-THUD-THUD!*

The blood that burst through his skin was red. The pain from his deeply cut shoulder and his internal organs surged up like lightning, hot as fire.

Amid that searing agony, Jamukha steadied his staggering body and spoke.

“Cough. How—how did you…”

Jamukha couldn’t understand.

The martial arts of the Hebei Peng Family were the very embodiment of domineering power.

For generations, the family had made its name throughout the world through strength honed by training and cultivation techniques that produced explosive internal energy. That reliance was also its one limitation.

That was why Jamukha had pursued only speed.

For the past fifty years, he had trained in saber techniques of the utmost speed and analyzed the Thunderbolt Saber King’s martial arts, all to bring him down.

He had believed that the speed he perfected would overcome the Hebei Peng Family’s overwhelming strength.

But…

“Why? How…!”

As the Thunderbolt Saber King approached, steadying himself despite his internal injuries, Jamukha cried out, his voice thick with blood.

Unlike Jamukha, who couldn’t answer the question he’d been asked earlier, the Thunderbolt Saber King replied with a calm expression.

“The Great Faction War. I realized it on that damn battlefield. There are plenty of monsters in this world even worse than this old man.”

There was no end to enlightenment.

Progress wasn’t a privilege reserved for the young.

Especially not for an old master like the Thunderbolt Saber King.

“Among them, there was this crazy old man who toyed with me and laughed at me. Said I was built like a bear and moved like molasses.”

The Fire King, Jeok Cheongang.

To surpass that deranged old monster someday, he had never stopped training—even after peace returned.

Not for a single day in all those years.

“Still don’t understand?”

The Thunderbolt Saber King straightened his massive great saber as he looked at Jamukha, clutching his half-severed shoulder and groaning.

“How Peng Cheolhu, the Thunderbolt Saber, became the Thunderbolt Saber King?”

It was the difference of only one character.

But in this vast world, only ten great martial artists had earned the right to be called kings—standing tall beneath the endless sky and three stars.

“The only place you can be called a king is out there on the steppe.”

Looking at Jamukha, whose eyes were wide with shock, Peng Cheolhu, the Thunderbolt Saber King, laughed aloud.
## Chapter artifact 968

# Chapter 968

Someone once said:

*When three people walk together, there is always one who can be my teacher.*

Of course, the Thunderbolt Saber King didn’t know for certain whether Confucius or Mencius had said it.

But the biggest reason he was smiling at that very moment was that someone who wasn’t there had come to mind.

*If not for the Fire King, that crazy old man, I wouldn’t have gotten any stronger.*

He had always lived a life in the spotlight.

Not only because he had been born into the Hebei Peng Family, one of the Five Great Families of the world, but even more because he had the talent and skill to deserve it.

Nangong Cheon. Murong Baek. And Peng Cheolhu.

Among the children of countless prestigious families, these three rising martial artists stood out above the rest. But while unexpected misfortune kept Murong Baek from reaching the same heights, the other two came to be called the Sword King and the Saber King.

But the Thunderbolt Saber King knew the truth.

Fire King Jeok Cheongang.

It was because that old man had constantly ridden him whenever he got the chance that he had grown stronger, instead of remaining stuck where he was.

“I’ll tell you something. That grassland where you were born and raised isn’t as vast as you think.”

The Thunderbolt Saber King slowly raised his great saber.

Toward Jamukha, trembling as he clutched the shoulder that had been half-severed by the Thunderbolt Saber King’s Force.

Toward the king of the steppe, holding back a groan before the giant who stood tall beneath heaven.

“Now, let’s see this through to the end.”

*Whoosh.*

Space disappeared with a single step.

The Thunderbolt Saber King’s blurred form moved so fast it was hard to believe his enormous frame could move that way. The great saber that plunged down like lightning traced a path that was precise and calm.

*Shhk!*

With a single slicing sound and a pain that spread like flames, Jamukha clenched his teeth to hold back the scream rising in his throat.

*Ghk…!*

He’d dodged. He should have dodged.

But even now, the wound in his shoulder kept crying out in pain, and the Thunderbolt Saber King’s internal energy had seeped through it and shaken his internal organs, holding his steps in place.

*Wooooom.*

A resonant hum burrowed into everyone’s ears.

Unlike Jamukha’s crescent saber, now shattered into pieces, the Thunderbolt Saber King’s great saber had only a few scratches. It trembled, then surged forward once more.

No—it split apart as it advanced.

The blade, which should have been one, became five, then ten, then dozens.

The dozens of afterimages formed a massive net and shot toward the space ahead.

Along with the Thunderbolt Saber King’s low voice.

“Go.”

At that moment, what filled the Thunderbolt Saber King’s voice and gaze as he faced Jamukha was certainty.

There wasn’t even a trace of carelessness toward the severely wounded, bleeding enemy—only certainty, born of his strike and his mastery.

*Fwoooosh!*

The net of Force descended. The tremendous energy hot on Jamukha’s heels as he leaped backward cut through everything it touched.

The cliffs lining both sides. The rocks and corpses scattered everywhere.

Even the loyal subordinates who had rushed in to save Jamukha.

“Stop him! The Khan is in danger—!”

*Puk! Fwoooooosh!*

In the end, there were no screams.

Those who had rushed forward with desperate cries crumpled into dozens of chunks of flesh. Jamukha, teeth clenched, reached for a weapon abandoned by its owner.

*Woom.*

The air shuddered. As a crescent saber he had drawn toward himself with Seizing an Object Through Empty Space flew into his grasp, he unleashed a burst of Force.

*BOOM!*

Part of the net of Force scattered, but the enormous impact that shook his whole body made Jamukha swallow the blood surging up his throat.

His saber techniques, wielded with only one arm, were slower. Every time he met a strike head-on, the impact battered his insides, which kept screaming in pain.

But—

*Do you think I’ll die like this? And at your hands?*

With that cry in his heart, Jamukha sent his crescent saber flashing in every direction.

The thunderous booms that followed filled his vision with flashes of light. Beyond them, the distant past swept through his mind like a lantern show.

Memories of his youth, when he had struggled to stay alive, clenched his teeth until they bled, and vowed revenge. And the voice of someone who had willingly reached out to him then.



*“Don’t you want to live?”*



He’d thought everything was over.

The warriors who had once numbered in the thousands had been all but wiped out by the Hebei Peng Family’s elite, led by Peng Cheolhu. His rivals, who had been waiting for him to fall, would take his livestock and possessions—and enslave the few members of his tribe who remained.

That was the law of the steppe, handed down through nothing but the survival of the fittest.

But just as he thought everything was over, his last chance came.

The young chieftain, slumped before his shattered ambitions and his subordinates’ corpses, seized the hand of salvation reaching toward him—the lifeline dropped from the heavens—with all his strength.



*“I want to live. No—I must survive, no matter what!”*

*“If you want to live, what for?”*

*“Revenge. I’ll repay today’s humiliation and grudge, no matter what. If you save me, I swear by Tengri…”*

*“I’m not helping you.”*

*“What do you mean?”*

*“I’m going to use you.”*

*“……!”*



He didn’t deliberate for long. The decision he made in that fleeting moment was as firm as an iron tower.



*“Show me the path I must follow, my lord.”*



The savior smiled, pleased at the sight of him prostrating himself like a slave. Pointing beyond the endless horizon, he said:



*“Go. Build a new home where neither the Hebei Peng Family nor the eyes of the Central Plains can reach you.”*

*“You mean I should head west?”*

*“Don’t worry. That land is still in utter chaos, and you won’t be alone anymore. You’ll be with ‘us.’”*

*“Us…”*

*“That’s right. We’ll help you. Jamukha, warrior of the Great Steppe, reborn here today.”*



The savior had been right.

The young chieftain who left with a new name soon made a name for himself on the western steppe, and the greatest reason he was able to build such a powerful force was the savior’s support.

Countless livestock and goods. Even people and information.



*“They’re quite capable. Make good use of them.”*



That was how Jamukha’s personal guard, the Keshik, came into being.



*“These are supreme martial arts and the Hebei Peng Family’s techniques, suitable for you to learn. They aren’t the secret techniques passed down to only a handful of people, but studying them will surely help you greatly.”*



Before long, he was even given a sword and shield to face the lifelong enemy who would come to be known as the Thunderbolt Saber King.

*Clang!*

A thunderous crash shattered his reverie. Blood burst from his torn palm. Jamukha swung his crescent saber like a madman at the net of Force bearing down without end.

One arm, its flesh, bones, and even muscles torn apart, was unusable. But the mighty internal energy and supreme martial arts he had built up over a long life still flowed through his fingertips.

Along with a memory from long after he had settled on the western steppe.



*“Tell me. When should we set out?”*

*“Not yet. Wait for the right moment. You must never leave the west until you receive a clear order.”*

*“Not yet? How much longer am I supposed to wait?”*

*“What?”*

*“If I wait only for that order, we’ll miss our chance. Now that the Central Plains are in turmoil because of the Great Faction War, we should strike at Hebei instead…”*

*“Amazing. A hunting dog that can talk like a person.”*

*“……!”*

*“Draw your saber. Right now.”*



Under the savior’s murderous gaze, Jamukha didn’t refuse. He charged.

And he met a wall—higher and more imposing than the one he had faced in his youth, when he had fought the Thunderbolt Saber King—and was forced to kneel.

Only then did he understand.



*“Remember this. Until we receive an order from ‘that person,’ we will never move.”*

*“……That person?”*



Even the savior, who had been like the heavens to him, was nothing more than someone else’s hunting dog.

And the “us” the savior had spoken of from the beginning held a meaning far deeper and more powerful than Jamukha had ever imagined.



*“Keep it in your heart until the day you take your revenge and claim the steppe. You will not be forgiven twice.”*



At that moment, Jamukha hadn’t felt humiliation or defiance.

He had shuddered with fear and joy.

If he followed the owner of the leash around his neck, he could reach the destination that had seemed to grow ever more distant.

The leash’s owner, who had swallowed the world, would toss this vast Great Steppe to a hunting dog who had completed his mission well.



*“…As you command.”*



From that day on, the defiance in Jamukha’s heart vanished without a trace. Then, after time had settled on his hair like frost, he realized at last that the moment had come.



*“What is this?”*

*“A kind of pill. It lets you temporarily wield more strength than your limit—but you’ll pay a price to match.”*



Its effects were far too ominous for it to be called a spiritual elixir. The savior called it a Temporary Strength Pill.



*“Why are you giving this to me?”*

*“Call it an experiment. For the near future.”*

*“Then could it be…”*

*“That person has awakened. From now on, build a bridgehead for our advance into the Central Plains.”*

*“……!”*



The final few years added to his fifty-year wait passed in a flash.

Following his orders, Jamukha scattered pills across the steppe, along with a few martial arts manuals. Each pill found its own owner, and those who gained power they could never have imagined before threw everything into chaos, disrupting the established order.

Not only on the steppe, but in the Central Plains beyond the Great Wall as well.

Pung Yang.

The leader of the mounted bandits known as the Red Wind Band on the eastern steppe was a man of considerable ambition.

With the aid of the Temporary Strength Pill, he built his forces at an astonishing pace. At last he turned his horse toward Shanxi Province, where he met his end.

At the hands of a member of a borderland martial family in slow decline, who bore the unfamiliar epithet Sleeping Dragon of Shanxi.



*“Jin Taekyung. Jin Taekyung…”*



About two years passed, and so much had happened.

The Jin Family of Taiyuan had risen to become the power of Shanxi Province. On the eastern steppe, where his old name had been forgotten, two young upstarts named Temur and Chinggen had begun to stand out. Far away in the Central Plains, the Star-Array Grand Banquet was held.

Then, like dams giving way one after another, all the events that had been held back burst forth in succession.

The bloodshed began with Shaolin Temple in Henan as its first victim, then swept through Sichuan and Anhui before spreading as far as distant Yunnan.

The Sleeping Dragon of Shanxi came to be called the Divine Dragon. The people of the Central Plains, sensing danger, gathered beneath the Murim Alliance’s banner, while even the great sects shrank back from the blades of enemies who might strike at any moment.

Of course, none of this applied to Jamukha.

The enemy everyone in the Central Plains feared, Dark Heaven, was “us” to him.

This was the moment Jamukha had waited for all his life.



*“By the coming Double Ninth Festival, seize the eastern steppe and gather every soldier to conquer Shanxi.”*



Jamukha immediately summoned his warriors.

His movements were as swift as lightning, all the quicker for the long wait.

At last, he raised a great army that encompassed the entire steppe, while the savior relayed news from beyond the Great Wall as it came.

Shanxi Province’s forces, gathered around the Jin Family of Taiyuan. The place expected to become the fiercest battlefield.

And finally…



*“The Thunderbolt Saber King will go there for certain.”*



Even the end point of a grudge grown stale with age, one he absolutely had to wipe away.

And it had all gone as predicted.

Except for one thing.

*Why? Why?!*

With a cry that circled only on the tip of his tongue, Jamukha twisted his unsteady body around.

*Shhk! Puh-puh-puk!*

Pain like a branding iron.

Even as his eyes saw it and his mind recognized it, his body moved too slowly.

The net of Force that had pursued him relentlessly had faded after leaving dozens of large and small wounds across his body. But beyond it stood a great tiger that would never let its prey escape.

Lips pressed tightly together. Eyes flickering with cold fire.

And in his hands, gripping the immense great saber so tightly that his palms had gone white, brilliant flashes wrapped around the blade without leaving a gap.

*Whoooom.*

The Thunderbolt Saber King swung without hesitation. Jamukha watched the terrible strike, a fusion of defeat and swiftness, cut through the air.

And understood.

He had only one choice left.

Even if he lost his strength and fell in this narrow gorge, the choice he was about to make would be a hundred, a thousand times better than dying at the Thunderbolt Saber King’s hands.

*Shk.*

With Force flying toward him from several yards away and the world slowing down, Jamukha pulled something from inside his robe.

He tossed the small, blood-red pill into his mouth without hesitation.

Or tried to.

Until, at that very moment, a flash of light came plunging down from above.

*Thuk!*

In Jamukha’s eyes, filled with a moment’s pain and disbelief, he saw a spearhead shining in five colors.

It pierced the back of his hand—and the Temporary Strength Pill he held in it, his last hope.

“……!”

Forgetting even the pain, Jamukha raised his head.

The owner of the spear, which had fallen from the sky shrouded in deep darkness, spoke not to Jamukha, but to the Thunderbolt Saber King.

“With people like this, no amount of caution is ever enough. Don’t you agree?”

*Shwaa!*

The great saber, which seemed poised to sweep everything away in a single stroke, let out a shrill whistle and stopped in midair.

At the sight of the familiar face, a smile of surprise appeared at the corner of the Thunderbolt Saber King’s mouth.

“I knew you’d come.”

The Thunderbolt Saber King continued, his voice thick with emotion, to the middle-aged man with graying hair who looked twenty years younger than his actual age.

“It’s been a long time, Murong Baek. Or should I call you Family Head Murong now?”

Seeing Murong Baek—once his rival for supremacy in the north, but now his true comrade-in-arms and friend after the Great Faction War—the Thunderbolt Saber King grinned broadly and lowered his great saber.

Good.

The war was over.

Jamukha was already out of action, and the elite Murong Family troops Murong Baek had brought with him must have joined the battlefield by now.

And just as he expected, a shout rang out from beyond the gorge.

“The Murong Family! It’s the Murong Family!”

The Thunderbolt Saber King felt the tension that had gripped his entire body slacken.

At least, until a panicked shout from someone who was surely a member of the Hebei Peng Family followed in the next moment.

“Grand Family Head! The enemy—the Murong Family—!”

What?

In that instant, the Thunderbolt Saber King’s mind went blank, and he felt a chill creep through his body.

*Shhk!*

Beyond the blinding pain, a quiet voice rang out.

“I told you. No matter how careful you are, it’s never enough.”

“……!”

As his vision blurred and faded, the Thunderbolt Saber King suddenly understood.

Jamukha.

The young chieftain who should have lost all his power and died a defeated man—how had he shaken off his pursuers and survived until now?

*The Murong Family.*

That was it.

On that day, more than fifty years ago, the one who had pursued him was none other than Murong Baek.

The true root of all this calamity.
## Chapter artifact 969

# Chapter 969

The people of Shanxi didn’t see that fleeting moment.

They were throwing all their strength into driving back the enemies filling the gaps among the corpses of men and horses and between the scattered rocks.

No—even if they’d been nearby, they wouldn’t have seen anything.

The strike was so natural and swift that it could deceive the Qi Sense of a Supreme Peak master ranked among the top three of the Ten Kings.

*Shhk!*

Amid pain so sharp it felt like he was burning, the Thunderbolt Saber King summoned superhuman endurance to straighten his collapsing body.

He trembled at the unbelievable truth that had struck his mind like a gigantic iron hammer.

*So that’s what happened.*

At last, he understood. He finally realized.

Why the young chieftain who crossed the Great Wall and invaded Hebei had survived.

The man had possessed skill worthy of his ambition, but he’d still been no more than an exceptional nomad. Why had he been able to acquire powerful internal energy and supreme martial arts nowhere to be found on the steppe?

That day, Jamukha hadn’t survived.

He’d been spared.

By the Murong Family that pursued him. By the man who led them.

*Murong Baek.*

His vision blurred with rage and pain. The Thunderbolt Saber King pressed a trembling hand to the deep gash in his chest to stop the bleeding, and stared in shock at the middle-aged man before him.

A man with exotic features, as though he stood somewhere between the Han Chinese and the nomads.

“Impressive. To react that well even in those circumstances…”

His voice was as still as a quiet pond.

But his sword, no one knew when he’d drawn it, was already slicing down at lightning speed.

*Whoosh!*

The air screamed.

The Thunderbolt Saber King’s eyes flew open at the unrestrained strike from Murong Baek, whom he had believed to be his friend.

He’d twisted instinctively at the last moment, saving his life—but that was all.

The Force that had raked deep across his chest left his whole body heavy as soaked cotton.

*Boom! Krrrk!*

His great saber wavered as it barely blocked the sword.

Murong Baek let out a quiet exclamation at the Thunderbolt Saber King’s ability to stop the attack despite his disrupted internal energy.

“As expected, you’re still absurdly strong.”

“Murong Baek, how could you…!”

The Thunderbolt Saber King clenched his teeth until they bled.

The Murong Family and the Hebei Peng Family.

The Hebei Peng Family and the Murong Family.

It was true that there had been a time when the two families, known to everyone under heaven, had been at odds.

But that was in the past.

A stale relic of days long gone, carried away by the passage of time.

That was why the Thunderbolt Saber King still couldn’t believe it, even now.

That Murong Baek—his comrade-in-arms, who had fought back-to-back with him in the Great Faction War, and the rival of his youth who had become a friend and grown old alongside him—had betrayed him.

No. That he had betrayed everyone on this land.

“When? Just when did you…”

His breathing grew ragged with anger and shock.

The Thunderbolt Saber King moved his split lips toward the traitor visible beyond the trembling blades.

“When did you join hands with Dark Heaven?”

The answer came in the form of Murong Baek’s sword, pressing down on his great saber with even greater force, and the Force gathered along its edge.

*Shhk.*

The Thunderbolt Saber King swallowed the groan rising in his throat.

It was hot. Murong Baek’s Force reached his skin before the sword did, digging into his collarbone.

Slowly, little by little.

It cut through the flesh and bone of his collarbone, as though it wouldn’t stop until it reached the heart beneath.

“Graaaah!”

Blood spurted between his clenched teeth.

Roaring like a furious tiger, the Thunderbolt Saber King swept his great saber upward.

He erased the pain with his rage and poured all his internal energy into the blade, using the Chaos Thunderbolt Divine Art, a technique reserved for the Hebei Peng Family Head.

*BOOM!*

With a crash like the sky splitting apart, Murong Baek’s sword was knocked away.

Agonizing pain surged from his ruined internal acupoints and his collarbone, split by Force. But the Thunderbolt Saber King endured it with a will harder than steel and reached out.

“You bastard!”

*Poom!*

Compressed air burst outward.

A single strike of the Hebei Peng Family’s proud technique, the Great Strength Vajra Palm, swept toward Murong Baek with a ferocious force that outran its own sound.

At least, that was how it looked for the briefest moment.

*Shwaa!*

A flash of light—and it was over.

Murong Baek’s figure blurred as he cut apart the palm force flying with the wind. The instant the Thunderbolt Saber King thought he saw him disappear, a red warning light flashed in his mind.

*Shifting Form and Position!*

There was no time to stop the bleeding from his collarbone or swing his great saber.

The Thunderbolt Saber King could only twist his body with all his strength. Turning toward the faint presence he sensed behind him, he swung a punch.

*Whoosh.*

It connected.

Not with a human body of flesh and bone, but with the wind, crushed beneath his fist.

At the same time, he felt it.

A flash of light, scattering icy killing intent as it shot beneath the fist he’d swung into empty air.

“……!”

The world slowed. The Thunderbolt Saber King opened his eyes wide and moved by instinct, not reason.

He let go of the great saber he had never once been without, and reached for the flash closing in on his chest.

*Thuk.*

The sound of flesh being pierced rang out, clear and slow.

The pointed sword tip tore through the Palm Force he’d hastily summoned as if it were tofu, sliced through the flesh and bone of his hand, and emerged from the back of it.

As if that obstacle meant nothing, it continued toward its destination.

Until the Thunderbolt Saber King, stifling the scream about to burst from him, gripped it with all his strength.

*Krrrk!*

At that moment, the sword stopped.

No—more precisely, it broke.

*Plip.*

Fragments of the blade fell with his blood.

The Thunderbolt Saber King’s whole body went rigid as he failed to withstand the immense pain of his hand being crushed in an instant.

With his eyes wide, he could only stare at Murong Baek, who was looking back at him. Then, dazed, he watched as Murong Baek—his body not injured in the slightest—thrust out one palm.

*Fwoosh.*

Beyond the dazzling light that filled his vision, Murong Baek’s quiet voice reached the Thunderbolt Saber King’s ears, faint as a dream.

“You fought well. Like a true warrior.”

And then—

*Poom.*

With a single explosion echoing deep inside his body, the Thunderbolt Saber King’s world turned upside down.

* * *

A massive tremor swept through the gorge.

*KABOOM!*

The ground shook. Amid the thunderous crash, part of the cliff collapsed.

If even nature’s work, built up over ages so long no one could say when it had begun, could be brought down like this, then there was no need to say what would happen to a human body of flesh.

*Krrr…*

Rocks that had been part of the cliff, along with enormous quantities of earth and sand, came crashing down. At the same time, they scattered wildly in every direction.

Yet even in the pale dust cloud where he couldn’t see a hand in front of him, Murong Baek kept his eyes fixed on one spot.

He slowly clenched the hand that had caused something like a natural disaster, taking in everything within a radius of several dozen *zhang* with his Qi Sense.

Even the faint cough that had just leaked out from between the shifting mounds of earth.

*Khk.*

Murong Baek didn’t even turn his head. Instead, he quietly reached out and lightened the weight of the earth pressing down on the person who had coughed.

Along with an object that had once belonged to him.

*Wooooom.*

The air shuddered as an immense force flowed from his gesture. Then, as if pulled by invisible strings, a spear buried deep in the ground was caught in his hand.

Red blood ran down it, evidence that it had pierced someone’s flesh and bone.

“Thank you.”

At Jamukha’s voice behind him, Murong Baek spoke.

“Why didn’t you follow my instructions? I told you to buy as much time as possible.”

“Well…”

“I suppose you underestimated the Thunderbolt Saber King.”

Jamukha, who had been about to reply, bit his lip.

Murong Baek was right. He had disobeyed his savior’s command.

He’d gotten greedy when he managed to hold his own against the Thunderbolt Saber King, and little by little, he’d pushed Murong Baek’s order to wait until he arrived out of his mind.

And there was one more thing.

He had also forgotten the order that, at least, he must never use the Temporary Strength Pill himself.

“I have no excuse.”

“Right. You don’t. If you’d swallowed it, you wouldn’t be talking to me now.”

The Temporary Strength Pill was a double-edged sword.

That was true of the early versions that had found their way into the hands of various people, including Pung Yang, the Red Wind Band Leader. But the new, improved pill also had tremendous addictiveness and side effects.

The ordinary foot soldiers might take it, but Jamukha could not. He was the commander-in-chief of a great army, with much yet to do.

Especially from Murong Baek’s point of view, with Jamukha as his vanguard.

“How are you?”

“Not as bad as you might think. Once I finish regulating my qi, my Internal Injury should heal soon.”

Contrary to his words, nearly half of one shoulder had been cut away. But even though the injury threatened his future as a saber fighter, Jamukha’s expression wasn’t the least bit troubled.

He knew.

He knew how mysterious and powerful the Dark Heaven his savior belonged to was—the Dark Heaven Murong Baek had called “us” long ago.

So, with a face untouched by even a trace of worry, he continued:

“Though that bastard will be wandering the Nine Springs now, unlike me.”

That was when Murong Baek’s gaze, fixed in one direction the entire time, shifted to Jamukha.

“You still have a long way to go.”

“What do you mean…?”

Jamukha let his words trail off. For a moment, he realized what Murong Baek had meant and bit his lip.

“Are you saying he’s alive? The Thunderbolt Saber King? Even now?”

It was a natural question.

He had seen it with his own eyes.

The Thunderbolt Saber King crumbling beneath Murong Baek’s merciless hand, without a trace of hesitation or mercy.

He’d been struck by a palm of truly terrifying force and driven deep into the cliff, looking like a corpse as he spat blood.

But unlike Jamukha, Murong Baek could sense the faintest breath coming from beneath that place, buried under countless mounds of earth and rocks.

*Stubborn bastard. Just as always.*

When he thought about it, Peng Cheolhu—the Thunderbolt Saber King in Murong Baek’s memories—had always been like that.

With his natural strength and sturdy body, he’d stood out among the young prodigies of the Hebei Peng Family and the entire world. He’d been no different even on the countless battlefields he’d fought on.

*He always survived. Always.*

That was why Murong Baek intended to finish the Thunderbolt Saber King off with his own hands.

Besides, now that the cliffs had collapsed in front and behind them, cutting off every eye in the vicinity, he needed to eliminate every survivor—including the Thunderbolt Saber King, a possible danger.

The later the secret came to light, the better.

That way, he could deal another devastating blow to the next reinforcements arriving from the Nine Sects and One Gang.

*At least half a day until Huashan and Zhongnan arrive.*

There was still plenty of time.

Once he was ready, Murong Baek planned to meet the orthodox faction’s reinforcements right here.

By then, the Thunderbolt Saber King would be gone, along with the Hebei Peng Family martial artists collapsing beneath the unexpected ambush from the Murong Family beyond the gorge.

The people of Shanxi slaughtering the nomads behind the suddenly collapsed cliff would be dealt with, too.

Of course, before that, he couldn’t afford to forget the rats hiding beneath the earth, holding their breath as they waited to survive.

*Shhk.*

The spearhead swept through like a streak of light, cleaving through a massive rock and mound of earth as easily as tofu.

Murong Baek looked down impassively at Jin Mukyung, who was holding the bloodied Cheol Mubaek and Wipeng in his arms.

Without a word, he brought the spear in his hand straight down.

No—he was about to bring it down.

*Whoooom.*

At the terrifying sound of something cutting through the air from somewhere, Murong Baek turned his head on instinct.

And saw it.

*KABOOOM!*

A spear crashed through, bringing down the mountain of cliffs as it smashed them to pieces.

Its icy, translucent spearhead bore a blue-white flame.

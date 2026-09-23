# Checkpoint Review — 815–819

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

# Chapters 815–819

## Plot

Hunters led by Choi Minwoo break through the fanatics’ line in the canyon, but the battle’s shock helps free the Doppelganger. Jin Taekyung repeatedly kills it as it resurrects by consuming its dwindling supply of absorbed lives. The Doppelganger recognizes Jin as the Chosen One its master warned it to avoid, takes Siegfried Bassman’s face and Grand Mage abilities, then escapes with an extended-range Blink that tears off its arm and leaves it badly injured.

Jin interferes with the spell and arrives among the Doppelganger’s followers, surviving the journey but suffering severe nausea. As he fights through the fanatics, their real commander, Yahya Muhammad Ahmad Bedouin, confronts him with more than thirty elite assassins. Meanwhile, the Hunters and roughly ten thousand fanatics clash around the canyon. Fanatics use Aqua Storms to counter Magic Johnson’s Fire Storm and concentrate their attacks on Johnson and the Skeleton King to prevent pursuit. Minwoo is severely wounded and passes out; the Skeleton King takes the Hero’s Sword from his hand as a furious blond man arrives.

## Continuity

- Jin remains the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.
- The Prophet is a Level 170 Doppelganger titled “The Final Abyss.” It resurrects by consuming absorbed lives and can reproduce its victims’ appearances, abilities, and memories. It has completed at least 145 resurrections; its remaining lives are dwindling.
- The Doppelganger says its master sent it to this world and ordered it to avoid the Chosen One until its plan was complete. The master’s identity, plan, and the meaning of “Chosen One” remain unknown.
- The Doppelganger fled with a small escort, wearing Siegfried Bassman’s face and using his Grand Mage abilities. Jin interfered with its extended-range Blink and arrived among the followers; the spell cost the Doppelganger dozens of lives to heal, and Jin remains nauseated and weaker than usual.
- Yahya Muhammad Ahmad Bedouin is the fanatics’ real commander. Roughly ten thousand fanatics, including more than thirty A-rank War Mages, are fighting the Hunters.
- Magic Johnson’s Fire Storm was nearly countered by the War Mages’ Aqua Storms. The fanatics are pinning down Johnson and the Skeleton King while the Doppelganger escapes.
- Choi Minwoo was severely wounded and passed out. The Skeleton King caught him and took the Hero’s Sword from his hand.
- A furious blond man arrived at the Skeleton King’s position; his identity is not established.
- Magic Johnson’s humanity remains uncertain.

## Translation Decisions

- Keep **magical power** distinct from **mana**; keep mana interference distinct from ordinary spellcasting.
- Keep Demon Realm language distinct from other languages.
- Keep **Blink** distinct from **Teleport** and **Warp**; extending Blink beyond its normal range causes severe strain.
- Keep **Fire Storm** and **Aqua Storm** as distinct named spells.
- Use **Yahya Muhammad Ahmad Bedouin** for 야흐야 무함마드 아흐마드 베두인; retain the glossary rendering **Muhammad** for 무함마드.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades, including under the name Muninn.",
    "The Doppelganger can resurrect by consuming absorbed lives and reproduce absorbed people’s appearances, abilities, and memories; it has taken Siegfried Bassman’s face and Grand Mage abilities.",
    "The Doppelganger’s absorbed lives are dwindling; its left arm was torn off, and its regeneration is slow after forcing Blink beyond its normal range.",
    "Jin interfered with the Doppelganger’s extended-range Blink and arrived with it; the attempt cost the Doppelganger dozens of lives to heal and left Jin severely nauseated and weaker than usual.",
    "The Doppelganger is fleeing the battlefield with a small escort; Jin intends to stop the plan it has spent over thirty years building.",
    "Yahya Muhammad Ahmad Bedouin commands the fanatics; roughly ten thousand fanatics, including more than thirty A-rank War Mages, fight the Hunters.",
    "The fanatics nearly countered Magic Johnson’s Fire Storm with Aqua Storm and are using their numbers to pin down Johnson and the Skeleton King.",
    "Choi Minwoo was severely wounded holding the line, passed out after the Skeleton King caught him, and left the Hero’s Sword in the Skeleton King’s hand.",
    "A furious blond man arrived at the Skeleton King’s position; his identity is not stated in this chapter."
  ],
  "continuity_sources": [
    819
  ],
  "open_questions": [
    "Who is the Doppelganger’s master, what is the plan, and why must the target be avoided until it is complete?",
    "What does the Chosen One designation mean?",
    "Will Jin reach the Doppelganger before it escapes?",
    "Is Magic Johnson human?"
  ],
  "safe_through": 819,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Demon Realm language distinct from other languages.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 815

# Chapter 815

*Whoooosh.*

The cold night wind swept over him from head to toe. Choi Minwoo brushed back his windblown hair and looked down at the canyon rushing toward them.

*There it is.*

The spearhead, spilling a frigid light, stood out at a glance even in the deep darkness.

He had collected countless masterpieces and artifacts over the years, but he still couldn’t help marveling at the strength and sharpness of the spear named White Flame.

*Though not as much as its owner.*

Choi Minwoo thought of Jin Taekyung.

When he first met him, he never could have imagined that the young man his age who’d joined a raid as a porter would reach the pinnacle of Hunters around the world in less than a year.

But Jin Taekyung had made the unimaginable real.

He had prevented countless disasters and achieved dazzling growth through the arduous journey.

The boldness and courage he showed in every crisis had time and again far outstripped even Choi Minwoo’s expectations, though he’d watched him from closer than anyone.

Just like today.

*I could tell something was different from usual…but Mr. Jin keeps moving another step ahead.*

When the Skeleton King’s undead had relayed what was happening, Choi had felt both surprised and a little left out. Before long, though, those feelings had turned to joy.

Solving alone a problem no one else could crack was proof that Jin had grown to the next level.

*With him, we can win.*

Jin Taekyung was the commander in chief leading them all, the general directing the battlefield—and the vanguard charging toward the enemy ahead of everyone else.

There was no way not to trust him, and no reason not to love him.

Even if countless obstacles and dangers lay along the path Jin Taekyung walked, that would never change.

*That’s a lot of them.*

Choi Minwoo gazed down at the ground, his eyes calm.

Hundreds of meters below, a black mass of enemies poured into the canyon like a wave.

Too many to count.

Their footsteps shook the earth, and a tremendous chorus of shouts rang out from every direction.

“—Allahu Akbar!”

“—Brothers and sisters, charge! To the promised land!”

“—The salvation God has granted us awaits!”

The fanatics who’d hidden from the world bellowed.

Ironically, the weapons in the hands of those crying out for God’s salvation were instruments of blood and death.

*They’re not people like us. They’re just enemies we have to bring down.*

Choi Minwoo repeated the thought to himself like a vow. No—all the Hunters looking down at the scene felt the same way.

They’d already seen it. They’d learned it the hard way.

Humans could be more good—or more evil—than any other living creature.

And monsters weren’t the only things that threatened this world.

Before Demon King Asmodeus descended, the people who had brought about countless wars and deaths had also been human, just like them.

Humanity had suffered because of them, and through that suffering learned a lesson it must never forget.

*There are monsters with red blood, too.*

And the Hunters gathered here existed for one reason, with one duty alone: to hunt those monsters.

*Shing.*

Blades appeared here and there, their cold edges gleaming.

The Hunters were visibly more exhausted than usual after their battle against the monster horde, but the determination in their eyes was stronger than ever.

*Fwoooosh!*

The wind grew fiercer. Their hearts pounded faster.

Dozens of eagles and griffins tilted their enormous wings and plunged toward the ground.

The fanatics’ shouts, which had sounded like an echo returning from far away, now thundered in everyone’s ears.

“Fight to the last person! Don’t fall back!”

Choi Minwoo swallowed. The wind of the battlefield stung his skin. The fanatics poured into the canyon, their madness so palpable it seemed he could reach out and touch it.

A massive Grand Mage and the Skeleton King, with hundreds of undead at his command, stood in their way. But not one of them was afraid.

To those people, this battle was a holy war. Even if they died, they would join the ranks of holy martyrs and stand by God’s side.

The warriors of God, who had already experienced the miracle of awakening, kicked off their camels and shot forward at blinding speed.

Three hundred meters. One hundred meters. Fifty meters.

The distance closed in a rush.

And then…

Impact.

*Boom! Kaa-boooom!*

“Graaagh!”

Flames devoured the darkness.

The vanguard, struck head-on by Magic Johnson’s attack magic, went up in flames with a scream. The brief gap left by their deaths was instantly filled by other fanatics, who charged the undead without hesitation.

*Crunch, craaack!*

The canyon wasn’t absurdly narrow, but it wasn’t wide, either.

Even so, the fanatics whom the Doppelganger had cultivated for many years shattered the undead battle line in an instant.

The fanatics’ convictions and hearts might already have been no different from a monster’s, but they were fundamentally unlike monsters.

Like any Hunter, they were strong and clever—and, most of all, they had two excellent commanders.

“Those are fallen demons! Wipe them all out!”

“Inshallah.”

One man rampaged at the front, shouting roughly. An old man watched the battlefield with a composed expression from the rear.

The two stood out amid the chaos. The moment Choi Minwoo spotted them, he instinctively understood.

The scale of their power.

*S-rank Hunters—or should I call them fanatics?*

They were powerful foes he couldn’t take on as he was now.

And yet, strangely, he wasn’t afraid.

The next moment, the old man glanced up at the sky, and his gaze met Choi’s. Still, Choi’s heart didn’t waver in the slightest.

*Shhk. Slice!*

The strike was a flash of light.

A streak of aura sprang from the old man’s waist and cleanly severed the neck of the griffin Choi Minwoo was riding.

The huge flying monster, its strength gone, tilted to one side.

*Fwoosh. Rattle!*

The wind turned violent, and Choi’s body pitched wildly.

But he didn’t panic. The dive had become a fall, and for some reason, the corners of his mouth lifted.

He didn’t care about the screams of the Hunters clinging to the griffin’s spine or the way they stared at him as if he were crazy.

*I don’t regret any of the choices I’ve made. I’ll just fight as hard as I can.*

His mind was calm. The sword in his hand felt as light as a feather. He felt as if he could do anything today.

The ground rushed closer, and the roar of some nameless fanatic struck his eardrums.

“For the great God, for the Prophet!”

Choi Minwoo laughed aloud, then suddenly spoke.

“For our Alliance Leader.”

His voice was low but powerful. It was the signal.

*Papat!*

Choi Minwoo—and all the Hunters—kicked off the body of the griffin plummeting straight toward the ground and soared away.

*Tap.*

His feet touched the ground first. The sword in his hand blurred.

*Whoosh! Chaaash!*

A sharp wind rose along the blade, cutting through the limbs of fanatics rushing at him from all sides.

A streak of light shot between the bodies collapsing in sprays of blood.

*Whoosh—bang!*

Choi raised his sword in time to block it, but that was all he could do.

Unable to withstand the tremendous force, he was driven back several steps. A voice, sunk low, reached his ears.

“I thought I knew that face. Now I see—you’re Sky’s blood.”

The Arab man approached, a sword wrapped in aura in his hand, his eyes full of malice.

Amid the chaos of the battlefield, Choi Minwoo spoke in his heart to someone he couldn’t see.

*I don’t know. I don’t know how long I—or we—can hold out.*

But there was one thing he knew better than anyone.

He had to fight. He couldn’t fall before the enemy did.

Even against an opponent far stronger than himself.

*Swish.*

Choi Minwoo pointed his sword at the man. The **Hero’s Sword**, imbued with brilliant aura, shone brightly.

The eight hundred or so Hunters who’d dropped from the sky gathered around the light spreading through the darkness.

“Damn heretics. I’ll send you all to hell.”

The man’s body vanished from sight, a vicious smile on his face. The sword strike that burst forth at the same time grazed Choi’s neck as he instinctively ducked.

The Skeleton King, who’d been holding off the fanatics swarming from all directions, shot toward the man.

*Boom!*

Countless roars and screams swept through the canyon. The ground heaved, and the solid bedrock split apart.

The wind and shock of a battle unlike anything the cliffs had experienced in hundreds of years traveled all the way to them.

Even to the center of the canyon, dozens of meters beyond its entrance.

And those tiny cracks helped, if only a little, to free someone who should never have escaped.

*Thud-thud. Bang!*

A bone shard as long as a spear and thicker than one blasted outward. At the same time, new flesh and blood welled up from the severed ends of countless shattered limbs.

*Slide. Crack.*

A high-speed recovery impossible to believe, even with his own eyes.

No—Regeneration.

The Doppelganger, having completed its one hundred and forty-fifth resurrection, grinned, baring teeth stained with blood.

“Oh. I thought this was just getting started. Are you tired already?”

*Thwack!*

A streak of light pierced the space between its eyes instead of answering. The young man holding the spear moved his dry, cracked lips.

“No. I think I’ve got a little more in me now.”

And at that moment—

*Ding.*

A bell rang out clearly, audible to one person alone.

* * *

The moment I reached the Supreme Peak realm, I’d already entered the ranks of the superhuman. That much was a fact no one could deny.

But even those called superhuman were ultimately just human beings.

They felt pain when injured, tensed up when facing a strong opponent, and eventually grew tired if they kept moving without rest.

I was one of those people, too.

Except for one thing.

*Ding.*

> **System**
>
> Lv. 78 Brody Woods defeated!
>
> Gained a tiny amount of EXP!
>
> Level Up!
>
> The effects of leveling up fill you with healing power!
>
> Special Debuff: Broken Body rejects the healing power!
>
> Status Effect: Fatigue removed!
>
> Status Effect: Muscle Pain removed!
>
> Status Effect: Internal Energy Depletion…
>
> …
>
> …

As System messages appeared one after another, my fading vision cleared.

I felt the fatigue melting away and my internal energy filling back up as I muttered:

“Brody Woods. Brody Woods…”

That was a name I had to remember to the end. He was a hero who’d saved me when I was nearing my limit.

So were each and every one of the victims who’d faced death twice.

With that in mind…

“Die.”

*Slice.*

The Doppelganger, staggering back to its feet, had its upper body slide diagonally away along the path traced by the spearhead.

And at the same time, the sight I’d grown sick of seeing played out before my eyes once again.

*Slither.*

Blood and flesh welled up at a terrifying speed. The Doppelganger rose, whole again, looking more relaxed than ever.

“That’s enough. You must be close to your limit by now.”

“Nope. I’m doing fine.”

*Thrust!*

“You can’t have much left. No need to bluff.”

“I told you, I’m fine.”

*Thud, splatter!*

“This really is the last—”

“Hey.”

*Slice!*

The Doppelganger, resurrected yet again, muttered:

“What the fuck is wrong with this bastard…?”
## Chapter artifact 816

# Chapter 816

What the hell was going on?

The Doppelganger had no choice but to be bewildered. Dying the moment it came back to life was one thing. It had fully expected to be unable to put up much of a fight, either.

Its limbs had been bound, and Jin Taekyung was stronger than any human it had ever seen.

But there was one thing it simply couldn’t understand.

*What is this?*

He wasn’t getting tired. He wasn’t getting tired at all.

More precisely, just when he thought he was tired, he was back to normal again. Even the Doppelganger, which had experienced death more times than it could count, was starting to let loose a string of curses.

“What the fuck is this bastard……?”

*Slice!*

Before the curse was even out, a flash of light. A spearhead, its power and speed precisely controlled, cut across its throat.

One life faded away, and another life and memory it had absorbed in the past filled the empty space.

*What the hell is this bullshit?*

After passing through a brief moment of pain, the Doppelganger came back to life. Its eyelids trembled. A spearhead flying at it without pause entered its field of vision.

*Whoosh!*

A lightning-fast strike.

But this time, the Doppelganger had no intention of going down so easily.

The person it had been a moment ago was nothing more than a middling B-rank Hunter. But now, after its latest resurrection, it was indisputably an A-rank Hunter.

And not just any A-rank Hunter—a ranker who’d been among the top twenty in France.

*Jean the Swift.*

Recalling the nickname from the memories it had absorbed, the Doppelganger stepped onto the ground with feet that felt unusually light.

*Swish.*

A breeze skimmed past its chest by a hair’s breadth.

Its form, wavering like a heat haze, reappeared several meters behind.

It had dodged the strike without difficulty, and a relaxed smile spread across its lips.

“From here on, things won’t be so ea—”

*Shwhack! Thunk!*

A streak of Finger Qi pierced its forehead. The Doppelganger, which had died without putting up a fight, blinked as soon as it came back to life.

*Huh? That’s not right.*

It hadn’t even seen what happened. The one small consolation was that, for some reason, Jin Taekyung had briefly stopped attacking this time.

“Huh? What was that just now?”

At the sight of him asking in apparent surprise, the Doppelganger felt sure of itself.

*That’s right. That last strike must’ve been pure luck.*

From the Doppelganger’s perspective, that was the natural conclusion.

The man it had just absorbed had been a top-ranked Hunter in his country, with lightning-fast movements that had earned him the name Jean the Swift. An assassin-type Hunter.

If he’d decided from the start to dodge, even Michael Silbert himself would have found him a real nuisance.

*No matter how special Jin Taekyung is, he can’t possibly be that far above Michael Silbert.*

But the Doppelganger had no idea what Jin Taekyung’s question had really meant.

*Jean Pierre? Who’s this guy, and why does he give so much EXP?*

It was a name he’d never heard before. The Hunter world might be small, but unless a Hunter was famous worldwide, there was no way he could know every foreign Hunter’s name by heart.

*Anyway, thank you. Rest in peace.*

After offering his gratitude and condolences to the Hunter who’d been absorbed, Jin Taekyung raised his lowered spearhead.

That was enough respect for the dead. What he needed to do next was already decided.

Before even more people were sacrificed, he had to copy the EXP—no, completely destroy the Doppelganger.

“Don’t want to waste time. Let’s die at least one more time.”

*Thrust! Crack!*

“Gah……!”

With a final cry, another flame of life flickered out.

In less than ten minutes, the Doppelganger had already died over two hundred times. Its eyes began to waver with unease.

*This can’t go on. I underestimated him.*

The Doppelganger had greedily devoured countless lives.

For the past thirty-odd years, it had absorbed human souls, memories, and powers all over the world, becoming something close to immortal.

It was a unique ability, unlike any among the countless kinds of monsters in the Demon Realm.

But the Doppelganger knew the precise limits of its power.

*I’m not completely immortal, and I can’t combine the powers I’ve absorbed into one.*

When the firewood runs out, the fire dies down. Even if you join thousands of different fragments together, they can never become one.

That alone was an incredible ability—but not for the tiny handful of beings born to rule over all others.

Yes, like the one who had sent it down to this land.

*Until every part of the plan is complete, I must never come face-to-face with the target.*

*Whump!*

Its vision went black. Another death—how many now, it couldn’t tell—cut off the voice echoing in the Doppelganger’s mind.

“Cough.”

Regenerated into life along with the pain, the Doppelganger’s face flickered with regret.

*I shouldn’t have gotten close to him in the first place.*

The cause of its failure was obvious.

For more than thirty years, the Doppelganger had been freer than ever. And after Cheon Taemin disappeared, it had manipulated the world from the shadows.

That freedom and power had gone to its head.

In the Demon Realm, it had been subject to someone else. In this world, it was no different from a king, able to do whatever it pleased.

The more arrogant the Doppelganger became, the less weight it gave to its orders—and the heavier its own complacency grew.

Michael Silbert?

In the end, even he had been no more than a minion and a tool to the Doppelganger. It was rather admirable how obedient he was, but when the time came, he’d be a piece that had served its purpose and could be discarded.

Preparing the plan had taken a considerable amount of time, but it had been only one step away from completion.

And yet……

*Damn it.*

*Slice.*

Something hot cut across its chest. Pain it still couldn’t get used to took over its entire body.

*Hoo.*

The Doppelganger felt the new life arrive with its death and exhaled the breath that had been cut off.

The moment it opened its eyes, someone’s fist filled its vision.

*Thwack.*

Its vision swam. Only after it came to again did it realize its head had been smashed apart.

The Doppelganger stumbled backward without meaning to, then slipped as its foot landed in the brain matter it had spilled moments earlier.

“Internal energy’s wasted on a bastard like you.”

Jin Taekyung’s voice reached its ears. He sounded so calm that it was chilling—and that chill left the Doppelganger breathless.

The next moment, a foot came down on its chest with tremendous weight, taking even that breath away.

*Crack! Crunch! Splatter!*

Its vision went dark, then bright, over and over without pause.

Within a single instant, chopped into smaller and smaller fractions of a second, the Doppelganger died and came back to life several times.

Even after it broke free of its restraints, nothing changed. If anything, an even greater variety of deaths and agonies awaited it.

*Why? Why the hell?!*

The Doppelganger gave vent to its anger and regret in a silent scream.

Only now could it truly understand its master’s command never to meet the target before the plan was complete.

*This man…… is different.*

He was unlike any of the humans it had absorbed over the years, or any it had watched from afar, licking its lips while trying not to draw attention.

No—he didn’t seem human at all.

Just like Cheon Taemin.

*Whoom! Boom!*

With a heavy rush of air, an outstretched palm struck its chest. Tremendous force shattered its bones, and the heat within burned its organs.

*Cough.*

The Doppelganger spat dead blood and looked at Jin Taekyung with dimming eyes.

Jin’s face, filling its slowly darkening vision, was blurry. But the powerful aura radiating from his entire body was clearer than anything else in the world.

“The C-Chosen One……”

The words slipped out like a groan. Its head drooped limply.

Jin Taekyung’s fist, shooting forward like a meteor to deliver another death, touched the Doppelganger’s forehead as gently as a blade of grass.

*Tap. Fwoosh!*

The wind swept around them, unable to keep up with the speed of his punch. Jin Taekyung’s cold gaze settled on the Doppelganger’s new face.

“What did you just say?”

“……!”

The Doppelganger swallowed. It had let something slip without meaning to.

A gap created by its fading consciousness, blurred between the endless deaths and resurrections in that brief moment.

“I didn’t say anything……”

“Really?”

*Grab. Crack!*

Before it could finish speaking, the Doppelganger’s vision went black.

It couldn’t even keep track of how many deaths it had suffered now. The countless lives that had filled its body had dwindled to less than half.

The Doppelganger opened its eyes amid bedrock shattered along with its skull. It felt something beyond regret now: fear.

Fear of death itself.

*At this rate…… I’ll be erased.*

The Doppelganger’s life wasn’t infinite. To survive, it had absorbed the life force of others and burned it as firewood, just as its kin had once done.

*And they, too, met Erasure.*

There had once been a time when the Doppelganger species held sway over the Demon Realm.

But long years and a brutal purge had followed. Of the hundreds of its kin, it was the only one left alive.

That was why “Doppelganger” had become a name for a single being—and why it was called “The Final Abyss.”

*I can’t—I can’t be erased. I have to survive!*

The Doppelganger gritted its teeth and opened its eyes. New life force and mana, along with the powers of humans it had absorbed, filled its body.

*Vrrrrm.*

Mana filled its fist, coating it in a faint aura. The Doppelganger sprang to its feet and punched toward Jin Taekyung’s face.

*Whoosh!*

The thunderous rush of air came a moment later. A hard, thick palm blocked its fist.

No—it squeezed it.

*Crack.*

“……!”

The pain nearly made its mind go blank.

The Doppelganger realized its fist had been crushed like tofu. It realized, too, that it wouldn’t be able to avoid death this time either.

“Hey, what are you doing?”

*Whoom! Boom!*

The world turned upside down. Its consciousness returned with a deafening crash that seemed to burst its eardrums.

The Doppelganger came back to life in the center of a small crater and immediately kicked off the ground.

Away from Jin Taekyung.

*I’ll survive. Somehow!*

It had long since forgotten all shame. Its opponent—Jin Taekyung—was the “Chosen One” its master had once mentioned.

The Doppelganger drew out every bit of its newly granted power in an explosive surge and launched itself forward.

*Pop!*

Its blurred form cut through space.

Or tried to.

Until a streak of light came flying at it, just as the Doppelganger took its second step.

*Slice!*

Its headless body slammed into the ground. Several meters away, the Doppelganger came back to life, only for a lightning-fast strike to cleave down over its head.

*Fwoosh!*

A fountain of blood burst from its body, split in two.

But Jin Taekyung didn’t stop. The spearhead, wreathed in heat, kept cutting through the air.

*Shh-shh-shhk!*

A flash of light cut across its tilting body. Its limbs, chopped into dozens of pieces, hit the ground—and immediately began to grow back at a terrifying speed.

“Gyaaaah!”

The Doppelganger roared as it came back to life in the midst of a gruesome death.

The lingering traces of pain were still there, gnawing at its senses like bugs.

If Jin Taekyung had just used up a considerable amount of internal energy with that last strike, the Doppelganger had to sacrifice a dozen or more lives.

But now it understood. To escape Jin Taekyung’s grasp, it would have to use up even the lives it had been saving.

*Fwooooo.*

Vast mana poured over both its hands. Looking at a face he seemed to recognize, Jin Taekyung muttered like a groan:

“Siegfried Bassman?”
## Chapter artifact 817

# Chapter 817

The Doppelganger’s new face was all too familiar to Jin Taekyung.

The only time he’d seen it in person had been when it was shriveled like a mummy, but while investigating Michael Silbert, he’d seen that very face in photographs so many times he was sick of it.

And on top of that…

*Whoooosh.*

That immense magical power, so close he could almost reach out and touch it.

He didn’t need to check the Level window to know the answer.

“Siegfried Bassman?”

At Jin Taekyung’s voice, which came out almost like a mutter to himself, the Doppelganger snapped its fingers instead of answering.

*Crackle.*

A white flash flared.

The faint current flowing along its finger transformed into dozens of bolts of lightning and came crashing down in no more than an instant.

*Zzap!*

Jin Taekyung’s vision filled with blinding light.

His eyes closed before he knew it, but he could still feel it clearly.

The immense electricity transmitted through the rock surrounding him, the air, and the ground. Through everything.

*Boom!*

The ground, made of solid rock and earth, split like a spiderweb.

Jin Taekyung kicked off the ground and shot upward, thrusting out one palm. The heat of Flame Divine Palm blazed toward the lightning, burning it away.

*KABOOOOOM!*

A tremendous boom shook the canyon.

But Jin Taekyung pushed his eyesight to its limits and took in everything that had happened in that brief moment.

The rising flames and acrid smoke.

And even the Doppelganger, which had vanished like a ghost just before it all exploded.

*Blink.*

If Teleport and Warp were long-distance spatial movement magic, Blink was a short-range instant movement spell that made the user disappear in the blink of an eye, just as its name suggested.

That also meant its range was short, while Jin Taekyung’s senses and field of vision covered the entire canyon.

*There.*

He couldn’t see it. But he could feel it.

Jin Taekyung drew in a breath. He trusted his five senses and his abilities.

He stepped on empty air with the tips of his feet, powered by internal energy, and shot toward the Doppelganger beyond the drifting embers and acrid smoke.

*Whoosh! Boom!*

The air burst under the force of his speed. Smoke and embers scattered like an explosion, and his vision cleared.

At the end of the path he’d blazed through like a streak of fire was the Doppelganger, fleeing toward the followers who could help it.

“……!”

A chill prickling its back, the Doppelganger instinctively turned around and widened its eyes.

In a slowed world, Jin Taekyung was already right in front of it, filling its vision.

*How the hell?*

The brief moment had lasted less than a second.

Yet Jin Taekyung had not only figured out where the Blink spell would take it in that instant, he’d also crossed more than ten meters and caught up.

*You’ve got to be fucking kidding me…!*

The Doppelganger swallowed the curse that almost escaped its lips.

No—to be precise, it hadn’t even had time to curse.

If it did, it would lose forever the power of the Grand Mage, an asset far more precious than any of the other lives it had discarded countless times before.

*Shwaa!*

A reddish-hot spearhead tore through the wind. The killing intent, cold in contrast, froze its body in place.

But at least in that moment, the mana and abilities inhabiting the Doppelganger’s body belonged to one of only three Grand Mages in the entire world.

*Blin—k!*

*Fwoosh, boom!*

Flames exploded along the spearhead and devoured the air.

At the same time, the Doppelganger appeared more than ten meters away, a chill running down its spine.

Was it because it had narrowly escaped danger?

No.

It was because of the pair of eyes staring right at it.

*Jin Taekyung.*

Their gazes had only met, but its heart sank. An instinct honed over centuries of struggle whispered to it.

Run.

If it didn’t want that beast to tear out the back of its neck, it couldn’t let its guard down for even a moment.

And the next instant, as the Doppelganger cast Blink again without a moment’s rest, it knew for certain.

Its instincts had been right.

*Whoosh! Slice!*

The Doppelganger opened its eyes in a new space and let out the breath it had been holding.

The back of its armor, which had long since lost its original shape and purpose, had been seared hot by the heat that had grazed past it in an instant.

*He cut me. His speed is catching up to Blink.*

It had been a hair’s breadth.

A shiver ran through it. Of all the humans it had absorbed or encountered in passing, it had never met a monster like that.

Except for the one person it had feared—and deliberately avoided because of that fear.

*Cheon Taemin.*

The savior of humanity.

The only Adversary to face the Demon King Asmodeus with the body and mind of a frail human, a divine man.

The Doppelganger neither denied nor felt ashamed of its fear of Cheon Taemin.

He wasn’t someone it could call “nothing more than human.”

That was why, even after absorbing Siegfried Bassman years ago and learning about Cheon Taemin’s condition, it still hadn’t dared to challenge him.

But even the Doppelganger could never have imagined this.

That it would feel this much fear toward a human other than Cheon Taemin.

*Blink, Blink, Blink!*

If it hesitated even a little, it might face permanent Erasure.

The desperate Doppelganger leaped through space again and again.

Each time its form disappeared as if erased by an eraser, it drew closer to the exit of the canyon, where a fierce battle was underway.

And closer to the hunter pursuing his breathless, fleeing prey.

*Whsssh!*

A sharp whistle split the air.

A dozen or so daggers flashed toward the Doppelganger from every direction. The attack had been predicted so perfectly that it left no room to cast Blink.

Realizing it had no choice, the Doppelganger gritted its teeth and spread both hands.

*Vrrrrm, crack!*

The mana shield shattered before it could even finish forming. The daggers ricocheted off and embedded themselves in the cliffs and ground on either side.

But in the brief moment it had spent blocking them, Jin Taekyung was already right in front of the Doppelganger.

“Got you.”

“……!”

*Crack!*

There was no time to react.

The Doppelganger’s mouth fell open at the tremendous pain shooting through its wrist.

Siegfried Bassman had been a great Grand Mage in life, but Jin Taekyung’s terrifying strength couldn’t be stopped by any magic in his memories.

*Crreeeak!*

“Gyaaaah!”

The scream burst from its lips, unable to bear the awful pain.

Just from Jin Taekyung gripping its hand hard, its flesh and muscles were crushed and its bones shattered.

The Doppelganger’s vision went white for an instant. It saw the sky and the ground tilt.

*I’m turning over. No—I’m going to die.*

The Doppelganger realized it instinctively.

After this terrifying feeling of weightlessness, death awaited: its body crushed as it hit the ground.

*No!*

Siegfried Bassman was the most precious of all the lives it had absorbed.

Hunting an S-rank Hunter known to the world was difficult enough, but a Grand Mage was especially valuable—their ability to use magic was so useful.

*If I lose magic, I’m finished. In that case, I’d rather…!*

The stream of thought brought on by fear was as fast as a flash of light, and its resolve was firm.

*Whoooom!*

The instant it was about to slam into the ground with a fierce rush of air, the Doppelganger summoned every last bit of its strength and drew up its mana.

*Blink!*

*Flash.*

The world slowed.

Space, warped by mana, swallowed the Doppelganger whole. But unlike before, the amount of mana was different, and so was its stability.

The Doppelganger’s gaze was fixed on the battlefield hundreds of meters away, far beyond the limit of the Blink spell.

*I have to do it.*

A taboo that went beyond the limits of spatial magic.

But it was better than dying here. His fanatics, who worshiped him like a god, were there—followers he’d spent decades carefully cultivating.

*Crreeeak!*

Its bones and flesh twisted along with space.

It felt as if an invisible hand were squeezing its heart until it burst, but it didn’t matter.

Jin Taekyung.

If it could escape the hands of this monstrous human right now…

If it could flee under its followers’ protection and carry out the plan it had been preparing for so long…

*Farewell. See you next time.*

The Doppelganger thought this to itself and bared its blood-soaked teeth in a grin.

*Grrk, whoooosh!*

Mana surged like a storm, and warped space swallowed it whole.

At the same time, darkness fell over its vision. New light, noise, and faces swept over it like waves.

*Boom! KABOOOOOM!*

*Shing! Krrrrk!*

“Gah!”

“Warriors of God, do not fear death!”

“Go fuck yourselves, you insane fanatics!”

Booms and screams erupted all around it. Shouts from both sides pounded against its ruptured eardrums.

But what mattered to the Doppelganger was that the faces in its blurry vision belonged to its followers.

“W-wait!”

“Prophet!”

Fanatics in turbans spotted it and surrounded it. The Doppelganger spat out bloody fluid mixed with bits of its entrails, then laughed aloud.

“Cough. Heh-heh…”

Pain?

It was fine. It would recover soon enough.

Bones throughout its body were shattered, and the left arm Jin Taekyung had grabbed had been torn off from the shoulder. But what mattered was that the Blink spell, pushed beyond its limits, had succeeded.

*If I’d been an ordinary human, I’d definitely have died.*

It had been lucky.

It succeeded because Siegfried Bassman was a Grand Mage, and the Doppelganger survived these injuries because it was a Doppelganger.

*Slide. Crack.*

Pale, childlike flesh slowly grew from the stump of its severed arm. The torn muscles reconnected, and pure white bone grew back.

The recovery was incomparably slower than before. The Doppelganger clicked its tongue bitterly.

*Damn it.*

The countless lives it had absorbed were already running low.

By the time it got completely away from here, it might have only enough lives left to count on its fingers.

*But it doesn’t matter. I have things willing to lay down their lives for me.*

A sea of fanatics filled the area around it.

Smiling to itself, the Doppelganger staggered to its feet.

Even as fierce fighting raged around the canyon exit, the rear where it had fled by Blink was peaceful, with a large number of troops still there.

Including the elite forces the Doppelganger had taken considerable care to raise.

“Amir.”

At the Doppelganger’s low voice, the fanatics surrounding it stepped aside.

An old man holding a staff approached and fell to his knees before it.

“I have been waiting for you, great Prophet.”

His face and voice were full of wonder.

The Doppelganger looked down at him with an air of authority worthy of the name Prophet.

“God has led me elsewhere, so I must leave this place first. You will fight with all your might to hold back Jin Taekyung and the other heretics.”

The names God and Prophet were absolute.

But Amir asked again, looking bewildered.

“Jin Taekyung, you say?”

“What, are you afraid of him?”

“No. But… hadn’t you already subdued him, Prophet?”

The Doppelganger frowned.

“What do you mean? You weren’t there to see it.”

“Yes. But you personally subdued him and brought him here.”

“What?”

As the Doppelganger blinked, unable to understand what he meant, Jin Taekyung, who had been lying motionless behind it as if dead, blearily opened his eyes.

“Uh, shit. Where the hell am I now?”

“……!”
## Chapter artifact 818

# Chapter 818

“Uh, shit. Where the hell am I now?”

“……!”

The moment Jin Taekyung’s voice reached the Doppelganger’s ears, two questions surfaced in its mind, frozen like a statue.

*Why is he here?*

Magic manifested solely according to the caster’s will.

And, naturally, the Doppelganger had used Blink only on itself.

Even a full-blown psychopath with a mind that had spun around thirty-five times wouldn’t do something insane like cast a dangerous movement spell alongside Jin Taekyung—a man who could break the Doppelganger’s neck thirty-six times in the blink of an eye.

In the end, there was only one answer.

*Regardless of my will… he interfered with the Blink spell.*

Mana interference.

A theory completed after years of research by the scholarly Grand Mage named Siegfried Bassman surfaced among the memories it had absorbed.

The Doppelganger felt a chill sweep through its entire body. As it watched Jin Taekyung stagger to his feet, a second unanswered question lingered in its eyes.

*How? How did he survive?*

It could accept the mana interference. The man was a monster, after all.

It was absurd—utterly absurd—but perhaps this close-combat Hunter really did have mana control that surpassed even a Grand Mage’s.

But the Blink spell just now had been an utterly irrational and dangerous attempt.

The Doppelganger had nearly been torn apart for breaking the taboo, and it had to sacrifice dozens of lives to heal its body. There was no point saying more.

And yet…

“Ugh, my body’s all numb.”

Hearing Jin Taekyung mumble, the Doppelganger’s mind went hazy for a moment.

*Numb? He’s numb?*

That made no sense.

It felt betrayed. Even if Jin Taekyung were an ogre, shouldn’t he at least have lost an arm or a leg or two, out of basic decency?

*His body isn’t made of steel. So how?*

The Doppelganger had no idea that Jin Taekyung’s physique—once called the Heavenly Martial Physique in Murim—had long since surpassed its limits, enough to withstand even a Blink spell that broke the taboo.

Still, even without knowing the circumstances, the Doppelganger could easily grasp one truth.

*Jin Taekyung is weaker now than he’s ever been.*

The thoughts brought on by that immense shock were long and complicated, but the time swept away by it lasted no more than an instant.

Just a few seconds.

And at the end of the suffocating silence pressing down on everything came the Doppelganger’s shout, ringing out like a scream.

“Stop him!”

“……!”

“……!”

The silence shattered.

At the same time, the world that had momentarily stopped began moving again. The fanatics, who had been staring blankly back and forth between Jin Taekyung and their great Prophet in that slowed-down moment, sprang into action.

“Inshallah!”

“God is great!”

*Whoosh! Fwoooooosh!*

Shouts and the sharp whistle of incoming attacks rang out from every direction.

Looking at the countless flashes hurtling toward him, Jin Taekyung suddenly opened his mouth.

No—he let it all out.

“Ugh. Bwaaaaaagh!”

His vomit scattered before a drop of blood could.

The price of hitching a ride on the Blink spell was a hellish bout of motion sickness.

* * *

I tried to hold it in. I thought I could.

But life doesn’t always go the way you want.

“Bwaaaagh!”

Goddammit. I’d been about to say something cool.

Instead, vomit came pouring out of my mouth, splattering in a rush. Bent over like a grub, I hurriedly rolled across the ground.

*Slice! Spurt!*

A chill. I felt a sharp blade cut off a whole handful of my hair.

As the auras flying in from all sides grazed my body, stinging pain flared across my skin.

*After coming all this way, I have to roll around like a lazy donkey?*

Tears blurred my vision. The one small mercy was that those fanatics hadn’t expected this either.

*…It’d be weirder if they had.*

What kind of lunatic lands in the middle of a crowd of enemies and starts vomiting? I forced my churning stomach to settle and swung the thing in my hand.

*Thwack!*

Flesh and blood flew with a dull impact.

The Prophet’s arm, torn off in the aftermath of the Blink spell, made an excellent club.

“Oh, power attack.”

“You bastard! How dare you profane His sacred flesh—”

“Then let me rephrase. Holy attack.”

*Wham! Wham! Wham!*

The three fanatics nearest me fell like dominoes.

I hurled the ruined arm like an axe, then stamped down with a stomp in the middle of the enemies packed tightly around me.

*Thud!*

A shock wave packed with a tremendous rumble plunged the ground several meters around me.

The fanatics lost their footing and staggered. Their weapons, thrown off course along with their owners, whistled past my body.

*Whoosh! Spurt!*

I felt the aura and wind pressure carried by the blades graze my skin, leaving tiny cuts.

That alone told me they were skilled fighters.

*More than half are B-rank or higher.*

I’d counted hundreds of them.

The followers the Doppelganger had raised somewhere in a desolate desert no one could find were every bit as capable as the elite forces of the World Hunter Federation, fighting a fierce battle just a hundred meters away.

*Crazy bastard. No—crazy bastards.*

The Doppelganger and these disgusting followers of its were all shit from the same cesspit.

I swallowed the curses rising in me and stretched out both hands.

The fanatics who looked like tanks raised round, enchanted shields to block the way. But they were too late to stop the ten Finger Qi attacks I fired.

*Fwoosh! Thud-thud-thud!*

A gust of wind swept through, and ten fanatics fell like reed leaves.

Through the opening that appeared for an instant, I caught a glimpse of the back of someone who had disappeared from view.

*There you are.*

It was only for the briefest moment, but I saw it clearly and put the pieces together.

The bastard was leaving the battlefield.

Using the countless followers it had raised as bait. Stepping across their blood like a carpet as it fled somewhere beyond my reach.

Just as it always had. And…

*It’ll keep doing the same thing from now on.*

Too many people had already died.

I still didn’t know what plan the bastard had spent more than thirty years building, but I had to bring it down with my own hands here today.

If I didn’t, my world—and the people in it—would fall apart.

“You won’t get past—!”

*Crack. Thud-thud!*

I broke the neck of the fanatic blocking my way and used his body to block an arrow flying in from ahead.

The mana-infused arrowhead pierced the corpse, grazed my cheek, then lodged in the eye of a fanatic who happened to be nearby.

“Gyaaaaaah!”

A cry of pain rang out amid the spray of blood.

But the scream faded away as if washed clean, before long.

With a cold slicing sound.

*Slice.*

A red line crossed the fanatic’s neck. A heavy voice, announcing his death, rang out.

“Hassan. Brave warrior of God. We shall meet again in the Kingdom of Heaven, far in the future.”

*Thud.*

The screaming stopped. His head fell.

The body crumpled like a scarecrow and never moved again. Only then did faint beads of blood begin to well along the cut surface of the severed neck.

*This is…*

Even I, who had faced countless powerful fighters, couldn’t help being astonished by the skill.

I came to a stop and looked at the speaker, eyes wide.

Among the fanatics surrounding us on every side, a sturdy old man stood tall as an iron tower, looking at me.

“This is the first time we’ve met face to face, Jin Taekyung, king of the wicked heretics.”

A turban was wrapped tightly around his head, not a single strand of hair showing. His back was straight, his gaze deep and still.

I’d felt it ever since I first opened my eyes in this place: the old man was immensely powerful.

Not just as an Awakened one of the kind known in the modern world as a Hunter, but as a martial artist in his own right.

At the same time, I realized instinctively:

If the Doppelganger was the inviolable symbol of divinity, revered by the fanatics, then this old man was the real commander-in-chief—and the core of their fighting force.

“Yahya Muhammad Ahmad Bedouin… Is that right? That’s one hell of a long name.”

As I read aloud the information in the holographic window floating above his head, the old man’s eyes widened in surprise.

“How do you know my name?”

“God told me, you crazy old bastard.”

“Lies. God would never tell something like that to the king of the wicked heretics.”

“You’re the one talking nonsense. I’m an atheist, so I’m not a heretic—and I’m definitely not a king.”

“Do not deny the existence of the great God with your vile tongue, demon.”

“Come on, sir. It’s time to take your pills.”

*Slide. Thump.*

His robe slipped from his shoulder and spread over the ground.

The old man held a crooked staff in one hand and a scimitar—in Murim, you might call it a curved saber—in the other. As he stepped forward, the air around us turned cold and the circle closing in around me tightened.

*Step. Sssssss.*

Killing intent from every direction made my whole body prickle.

It wasn’t just the old man in front of me. I could see more than thirty men in black, wrapped head to toe in black robes and turbans, scattered among the fanatics.

*Those are the real deal.*

Every last one of them was a skilled fighter who could hold their own anywhere in the world.

And unlike Hunters, who weren’t used to killing other people, they showed not a hint of hesitation.

*Seasoned killers.*

It might not have been a mere trick of the eye that made the black-clad men overlap with the martial artists of Dark Heaven in my mind.

They resembled each other to a disturbing degree.

They were alike in their blind loyalty and faith in one being, and even more so in their willingness to do any terrible thing for that being.

And…

*I’ve killed countless people like them.*

There were too many people in the world who deserved to be killed. That was all.

Deep down, I had a vague sense that an absolute being called God might exist in this world. But I didn’t believe in him or pledge my loyalty to him.

In the end, it was people who achieved things in the face of hardship.

I’d survived that way, just like countless others.

But if that god was the one who’d slipped a beat-up capsule to someone who’d suddenly lost his job a year ago—to a young man climbing a steep alley, worried about how he’d get through this month… Well, in that case, I might be willing to believe in him a little.

“Then your deaths at my hands will be God’s will, too.”

With a low mutter, I grabbed at the empty air. In that place where there had been nothing but air and dust, I caught a spear that had been away from my side for a while.

A stubborn crease formed between the old man’s brows as he witnessed something magic couldn’t explain.

“Demon. You truly are a demon.”

I wanted to tell the old man in front of me, and the fanatics all around us, that the real demon was running away and leaving them behind. That the monster they called a prophet was racing toward a new catastrophe.

But instead of answering, I stepped forward. The wind burst and space vanished as I charged.

*Whoosh.*

A wave of scorching heat swept away the darkness. The White Flame spearhead traced a path no one could block.

*Slice—KRRRUNCH!*

A thick mist of blood settled over everything.
## Chapter artifact 819

# Chapter 819

Fanatics and Hunters.

The battle between two forces, waged around the canyon, could be summed up in four characters:

Advance and retreat.

The fighting was that fierce, and everyone on both sides had put their lives on the line.

Some fought for a faith they had believed in all their lives—a faith they couldn’t even imagine might be false.

Others fought for their unshakable convictions.

And so they fought.

It was a clash of faith and conviction, and at the same time, a holy war.

But in a place awash with blood and death, religion no longer mattered.

Demons.

They were human beings with the same appearance, but each held a different standard for good and evil. Their eyes met between the blades lunging toward one another, burning with murderous intent.

“Die!”

*Clang!*

Swords and sabers clashed. A sharp screech rang out, and vivid blue sparks flew. Blood spurted amid broken shouts, impossible to tell who had cried out.

*Slice—shaaak!*

No scream followed. The fanatic, his throat cut, glared at the Hunter before him with venom in his eyes, then collapsed.

Blue light flashed above the fallen body.

“Watch out!”

*Whoosh! Boom!*

A panicked shout and a roar of impact collided. A tank stared at an arrowhead that had pierced halfway through his enormous tower shield, right in front of his face, and sucked in a breath.

If he’d raised his shield just a little—just a fraction—later, he would have died.

But Hunters were closer to death than anyone. And everyone here had survived countless brushes with death just like this one.

The tank grabbed the arrow and snapped it in two, then shouted in a hoarse voice.

“They’re coming! Hold formation!”

*Rumble!*

Countless flashes rained down. Blades flashed, heavy clubs swung, and even fanatics on the verge of death forced themselves upright and charged.

The impacts pounding their shields were so immense that even the veteran tanks, hardened by years of combat, thought of death.

“Arrrgh!”

*Grit.*

They squeezed out the strength they had left in their shouts and clenched their teeth until they felt ready to break. Their feet slid backward under the pressure, carving deep furrows into the ground.

“Hold the line! If we break, it’s over!”

Even the commanders’ shouts seemed distant.

The enemy had an overwhelming numerical advantage.

It had been less than three hours since the battle against the monster army ended.

The strain of that fierce fight was eating away at their bodies and minds alike, and the fanatics they now faced were the worst possible opponents.

Ten thousand of them.

They kept charging even after their chests were cut open or their limbs were severed, their eyes alight with venom.

More than thirty years ago, the Doppelganger had raised these fanatics somewhere in this barren desert, out of the world’s sight, under the name of the Prophet. Now they were monsters of another kind.

*Thrust!*

A sword blade bearing a faint aura pierced a chest and burst out the other side.

It was a grievous wound. Even if he used a potion right away, there was no telling whether he’d live or die. Yet the fanatic whose chest had been pierced bared his blood-soaked teeth and smiled.

“I-Inshallah…”

“……!”

The madness in that fading voice made the Hunter’s body seize up.

A chill swept over him from head to toe.

But by the time he came to his senses, it was too late.

*Whoosh!*

A single whistle of air pierced his ear. At the same instant, his vision went dark.

*Slump. Thud.*

“Hans! Hans!”

The Hunter who caught his falling comrade clenched his lips.

But the comrade with whom he had saved each other’s life time and again never answered.

The dagger had pierced him exactly between the eyes, taking his voice and his life at once.

*Goddammit.*

The Hunter’s eyes darkened as he laid down the body.

The canyon was an ideal battlefield for facing a larger force, but no matter how efficiently they fought, casualties were unavoidable.

Especially against madmen who thought of death as martyrdom.

It was just as their ranks were about to crumble before the wave of fanatics charging without regard for their lives—

*Fwoosh.*

A fierce heat washed over everyone’s heads.

Before anyone could look up, a rain of fire came pouring down like a meteor shower, accompanied by a sharp whistle.

*Whoooooosh!*

Dozens of balls of fire appeared above the Hunters and fell toward the battlefield, toward the fanatics who charged without end.

As everyone stared up at the sight, mouths hanging open, one name flashed through their minds.

*Magic Johnson.*

The Grand Mage said to have received the blessing of mana. Among Grand Mages, he was the world’s greatest War Mage, proven so during the Great Cataclysm. At last, he was showing his true strength.

With a powerful area spell that could turn the tide of battle.

*That’s it. If he can do that…*

Every Hunter thought the same thing. No—they were certain of it.

With Jin Taekyung nowhere to be seen, Magic Johnson was their surest bet to lead them to victory.

At least, that was what they thought—until blue waves surged up from this parched land, where all there was in every direction was sand and stone.

“Aqua Storm!”

“Aqua Storm!”

“Aqua Storm!”

*Fwoooooosh!*

Dozens of voices rang as one. Spheres of water stacked upon spheres of water, rising into an enormous tidal wave.

And then…

*BOOM!*

A roar like the sky splitting apart shook the air.

Water and fire. Fire and water.

Two forces, opposites of one another, twisted together. They collided.

With a shockwave that shook everything within hundreds of meters, they exploded above the heads of the Hunters and fanatics.

*Fwoosh! Boom-boom!*

“Gyaaaah!”

“M-My God!”

Someone screamed from beyond the steam that swept through the area on the wind.

The thick steam blocked the view, leaving everyone unable to make out what had happened. But Magic Johnson, the one who had cast the spell, knew better than anyone.

His magic had been canceled out.

*It was blocked. Almost completely.*

He said almost because part of his Fire Storm had swallowed some of the fanatics. But he could tell the damage was far less than he had expected.

*They were ready for it.*

Magic Johnson had seen them clearly: thirty mages under an ironclad escort.

Their turbans were pulled low over their brows. Every last one of them was A-rank, and, like him, a War Mage specialized in combat.

*The Doppelganger…*

Magic Johnson swallowed a groan.

There was no need to wonder who had created all that overwhelming power in front of him.

The Great Cataclysm had been a time of immense chaos. Thirty years was long enough for nature itself to change, and the desert must have been the perfect place to hide something.

So what Magic Johnson wanted to know wasn’t how the Doppelganger had gathered and trained them.

His question reached back to the beginning and end of all this.

*What on earth did you want that you prepared so thoroughly?*

But Magic Johnson’s question reached no one. Even if the Doppelganger had known what he was wondering, it wouldn’t have answered.

No—it wouldn’t even have had time.

At that very moment, the Doppelganger was leaving the battlefield with a small escort.

*I have to chase it. I can’t let it get away.*

But despite his determination, Magic Johnson couldn’t move easily.

Unlike monsters, the fanatics had been trained rigorously, and they knew what mattered most in this battle.

They used their more-than-tenfold numbers to attack in rotating waves.

And…

“Stop them! Those two must not get through!”

“Open fire!”

Magic Johnson and the Skeleton King.

The two strongest members of their force—and its commanders—were under concentrated attack.

*Whoosh-whoosh-whoosh!*

*Boom-boom!*

Arrows and magic rained down. No matter that Magic Johnson was a Grand Mage; attacks he couldn’t afford to take lightly kept flying in from every direction.

He had already spent a great deal of his stamina and mana. The fanatics, by contrast, kept drawing on their strength as they cried out for a holy war.

The Skeleton King was in the same situation.

*Slice. Slice. Slice!*

The Bone Sword, made of bone, swept in smooth arcs.

But before the bodies crumpling in sprays of blood could hit the ground, dazzling flashes cut through the falling bodies and shot toward the Skeleton King.

“This is insane…!”

The Skeleton King was aghast. Since coming into this world, he’d never faced anyone this crazy. The fact that there were ten thousand of them made it all the more unbelievable.

*They’re insane. Completely insane.*

The Skeleton King wielded the power of death, but even he was nearly overwhelmed by the endless wave of fanatics.

Everyone feared death. No—he himself, an undead monster, feared Erasure. It was a problem like a fate bestowed the moment one was born.

So why weren’t the humans before him afraid to die?

No—what had made them this way?

*These people are the real monsters…*

*Thrust-thrust-thrust!*

Swallowing a groan, he swung his Bone Sword and cut through a human body.

But each time the Skeleton King took one down, three more came. When he took down three, ten showed up. And when he felled those, fanatics poured in from every direction, swinging the weapons in their hands.

“Die, demon!”

*Crunch!*

A chilling sound of a blade slicing through flesh rang out, but naturally, there was no pain.

The Skeleton King sighed as he looked at the sword that had pierced his chest.

“Who are you calling a demon?”

*Whoosh—thrust!*

A bone shard shot from his turned wrist and pierced an enemy’s throat.

With a gurgling sound, the fanatic fell. The Skeleton King kicked him hard, clearing some space. At that moment—

*Whoom.*

A dark shape flew toward him with a heavy whistle. The Skeleton King hurriedly caught it.

It coughed up blood. It was a human, and still alive.

More than that, it was familiar.

*Goddammit. This guy…*

There was no doubt. Though blood covered his entire body, the Skeleton King recognized him at once.

The Skeleton King had raised the undead monster with his magical power slowly running dry. He tapped the man’s cheek.

“Hey. Human with a fine-looking build. Can you hear me?”

*Cough.* Choi Minwoo spat up blood again, then answered in a voice on the verge of fading.

“Yes. Very clearly.”

“Good. We’re short on time, so listen carefully. You’re not going to die, so don’t worry. And even if you do, I’ll bring you back as an undead, so don’t—dammit. He passed out.”

The Skeleton King clicked his tongue and stood up, then added, almost as an afterthought:

“Well, he held out damn well, all things considered. Don’t you think?”

*Whoooosh! Slice!*

An aura slashed past the Skeleton King’s head instead of an answer.

He watched blond hair flutter through the air, muttered a string of curses, then faced forward. Through the thick steam, he saw a man.

“Not at all. He’s trash.”

His hair was a mess, and a wound ran across his cheek.

The Skeleton King gave a short laugh at the man’s eyes, burning with rage.

“No matter how I look at it, he fought well. When he wakes up, I’ll have to praise him myself.”

“Shut your filthy mouth, cursed demon.”

“You’ll find out when you die. Which of us was the demon.”

The Skeleton King pulled the hilt of the sword from Choi Minwoo’s hand. Sacred light spread along the blade of the [Hero’s Sword].

“Get in here, quick. Before someone scarier than me shows up.”

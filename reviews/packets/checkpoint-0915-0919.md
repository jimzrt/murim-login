# Checkpoint Review — 915–919

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

# Chapters 915–919

## Plot

Jin Taekyung and Jeok Cheongang attack the Eastern Heaven Demon Lord, racing to defeat him before their exhausted allies are overwhelmed by the undead. When Golden Ox Palace attacks Jeok, Taekyung takes a grievous strike meant for his Master. Jeok’s grief unleashes a vast white fire dragon that incinerates Golden Ox Palace and drives the Demon Lord to defend himself with death energy.

As Jeok nears victory, the Demon Lord summons the assassin Heaven’s Slaughter. Taekyung returns from the brink of death, mysteriously healed, and interrupts the assassin’s ambush with a blazing spear. He and Jeok turn the tables, killing Gye Yabu and routing his remaining followers. The Demon Lord survives, though he loses all four limbs, and reveals that his rebellion has powerful supporters beyond the banquet hall and that he knows more about Dark Heaven and the Lord of Heaven. Then thousands of soldiers arrive, only to be struck by a tremendous beam of light; the Demon Lord cries out So Gyo’s name.

## Continuity

- Jin Taekyung returned from a seemingly fatal injury with his body and internal energy restored; the cause is unexplained.
- Jeok Cheongang’s white fire incinerated the undead Golden Ox Palace. Jeok was exhausted after the fight, but survived alongside Taekyung.
- The Eastern Heaven Demon Lord is alive but has lost all four limbs. His rebellion has powerful military and political supporters, and he claims to have information about Dark Heaven and the Lord of Heaven.
- Jin Taekyung killed Gye Yabu of the Salcheonmun. The System warns that the sect will pursue Taekyung if it learns of his role.
- Gye Yabu vowed that the Salcheonmun would pursue Mungyeong, the Slaughter Saint, regardless of cost or delay.
- Thousands of soldiers were struck by a powerful beam of light. Their fate is unknown; the Demon Lord called out So Gyo’s name.
- So Gyo’s identity and allegiance remain unknown.

## Translation Decisions

- Keep “Force” for 강기 distinct from “death energy” for 사기.
- Render 천살 as “Heaven’s Slaughter” and 계야부 as “Gye Yabu.”

## Durable state

{
  "active_continuity": [
    "Jin Taekyung killed Gye Yabu of the Salcheonmun; the System warns that the sect will pursue him if it learns of his role.",
    "The Salcheonmun vowed to pursue Mungyeong, the Slaughter Saint, regardless of the cost or delay.",
    "Jeok Cheongang and Jin Taekyung survived the confrontation with the assassins and the Eastern Heaven Demon Lord.",
    "The Eastern Heaven Demon Lord is alive but has lost all four limbs.",
    "The Eastern Heaven Demon Lord's rebellion has powerful military and political supporters beyond the banquet hall.",
    "Thousands of soldiers arrived, but a powerful beam of light struck them; the outcome is unknown."
  ],
  "continuity_sources": [
    919
  ],
  "open_questions": [
    "What enabled Jin Taekyung to return from his seemingly fatal injuries?",
    "Will the Salcheonmun pursue Mungyeong, and will it discover Taekyung killed Gye Yabu?",
    "What happened to the thousands of soldiers struck by the beam of light?",
    "What is So Gyo's identity and allegiance, and why did the Eastern Heaven Demon Lord call her name?",
    "What information does the Eastern Heaven Demon Lord hold about Dark Heaven and the Lord of Heaven?"
  ],
  "safe_through": 919,
  "temporary_decisions": [
    "Keep “Force” for 강기 distinct from “death energy” for 사기."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 915

# Chapter 915

“You got here fast. Much faster than I expected.”

After a brief silence, the Eastern Heaven Demon Lord continued, his gaze sunk deep.

“Which means you’ll die all the sooner.”

His cold, gray eyes moved between Jeok Cheongang and me.

More precisely, they lingered on the large and small wounds etched across our bodies.

*Damn. He’s sharp as hell.*

The smile I’d forced onto my face slackened. I ignored the pain coming from every part of my body and lowered my stance.

Jiangshi. Or undead.

I’d lost count of how many of those things I’d taken down. I couldn’t even decide what to call them.

All I’d done was fight the monsters pouring in without end, then fight some more.

I swung anything I could get my hands on. When there was nothing left to swing, I smashed them apart with my fists and feet.

If they’d been ordinary humans, it wouldn’t have been this hard.

But they weren’t.

I had to hit them at least three or four times with attacks that should’ve killed them in one blow just to render them unable to fight.

*It would’ve been a lot easier if I’d had enough internal energy…*

Jeok Cheongang and I had both spent a considerable amount of internal energy in the fight.

The Extreme Yang Scorching Yang Qi accumulated through the Fire Gate Clan’s secret cultivation technique was the polar opposite of the death energy the dead possessed. But we couldn’t draw on it without limit.

Especially with a powerful enemy like the Eastern Heaven Demon Lord still ahead of us.

“You both look exhausted. Why don’t you turn back now, while you still can?”

The Eastern Heaven Demon Lord glanced over our shoulders.

“Before everyone left behind is dead.”

*Clench.*

His words hit a little too close to home, and my hand tightened around the spear before I realized it.

Because he was right.

His judgment was that accurate.

Jeok Cheongang and I had broken through one section of the encirclement to reach him, but plenty of monsters remained behind us. The Embroidered Uniform Guard led by Jeong Hogun and the Fire Dragon Pavilion members were fighting with everything they had.

Their numbers fell far short of even half the enemy’s.

And the enemy were genuine monsters—things that didn’t tire and wouldn’t die easily.

But we’d had no choice but to leave them behind. We’d decided this was the only right answer.

*This battle won’t end unless we take out the Eastern Heaven Demon Lord.*

He’d raised the dead twice already. There was no guarantee it wouldn’t become three times, or four.

And if the same thing happened again…

*We’d die. Every last one of us.*

As time passed, our allies died while the enemy multiplied.

It wouldn’t matter even if reinforcements arrived—assuming they ever did, and assuming the Emperor had prepared any at all.

*But if we take out their leader, things will change.*

Before I was a Murim martial artist, I’d lived as a Hunter. I knew that the fastest, most efficient way to bring down an undead army was to eliminate the Lich who’d raised them from the dead.

The problem was time.

Fifteen minutes at most.

We had to take him down somehow within that time. If it went longer, the gap left by Jeok Cheongang and me would be filled with the bodies of our allies.

The result would be the same if the other front, where So Gyo and Baek Yeon were holding the line, collapsed.

The only way to turn this situation around was to defeat the Eastern Heaven Demon Lord before the balance of the two fronts tipped.

But…

*Can we do it? In that short a time?*

The doubt that suddenly surfaced refused to leave.

I didn’t know if this was the right choice.

Maybe saving Prince Shangshan and the Fire Dragon Pavilion members and escaping this damn imperial palace was the best we could do. Maybe surviving, even if that was all we managed, was the right answer. The question stabbed at a corner of my heart like an awl.

*GRAAAH!*

*Clang! Cough!*

The roars I’d been trying to ignore behind me, the screams of people and the clash of blades, rang sharply in my ears. They kept tearing through my thoughts.

*Damn it.*

I swallowed the curse rising to my lips and gripped the spear shaft until it felt ready to burst.

—You can do it.

“……!”

—Trust me.

At Jeok Cheongang’s Sound Transmission, as if he could see straight through my thoughts, my wavering heart settled into a surprising calm.

That’s right.

I can do this. No—I have to.

If it’s the Old Master, if I’m with Jeok Cheongang, it’s possible.

Because I’m not alone. It’s *us*.

Even if we’re facing three Supreme Peak masters.

Even if every one of them is a monster who’s already left humanity far behind.

I have to fight.

I have to take them down.

—Now!

At the forceful words that pierced my ear, Jeok Cheongang and I stepped forward at the same time.

*Whoosh.*

As space vanished in an instant, we thrust out our palms as if we’d planned it long ago.

*Fwoosh! KABOOM!*

A raging blaze devoured the air.

* * *

*BOOM!*

It was unbearably hot. And terrifying.

As the fight became a three-way battle, the Eastern Heaven Demon Lord leaped clear of the flames and suddenly thought of a three-legged cauldron.

*If even one leg gives way, the whole cauldron loses its balance.*

The overall battle was certainly in his favor.

So Gyo, the one he had to be most wary of, was tied down fighting the well over a thousand monsters alongside Baek Yeon. The best the Embroidered Uniform Guard led by Jeong Hogun and the Fire Dragon Pavilion members could do was hold on.

But even a three-legged cauldron, which would topple if a single leg disappeared, had one leg more important than the others.

That leg was the Eastern Heaven Demon Lord himself.

*That’s why they broke through the encirclement at such a cost.*

*Boom!*

After easily dodging the first missed attack and then the second, the Eastern Heaven Demon Lord calmly watched the two men charging at him.

They’d grasped the heart of the matter in an instant.

Amid the chaos of fallen enemies and comrades alike rising again, they’d seen through his weakness.

So which of the two had made the call—the Master or the Disciple?

Jeok Cheongang?

Or Jin Taekyung?

*If it was the former, I’d expect nothing less of the Fire King. But if it was the latter… I understand why that person wants him so badly.*

Powerful enough to defy his age. On top of that, a composure that never wavered, and the bold judgment to see through the heart of a battle in any situation.

Even the armies of the Great Nation, numbering a million, had many fierce generals.

But truly great commanders were rare.

And Jin Taekyung had both qualities. At barely past twenty.

*Could that person intend for this boy to fill the vacancies left by those who have departed?*

Over the past few months, the Western Heaven Demon Lord had died, and so had the Southern Heaven Demon Empress.

Though many powerful figures remained, including the Eastern Heaven Demon Lord himself, the forces lost with those who had departed had to be replenished somehow.

For his revenge.

For the great undertaking that remained.

And in that sense, Jin Taekyung looked to the Eastern Heaven Demon Lord like a fine prospect—one who could more than fill the gap they’d left behind.

His Master, of course, could never be allowed to live.

*Jingle.*

As the Eastern Heaven Demon Lord moved with fluid evasions, a bell rang out.

At the same moment, Golden Ox Palace—the commander-in-chief of the Imperial Guards and a Supreme Peak master of the Twelve Palaces of the Zodiac—reacted at once.

*Whoosh!*

A greatsword, larger than most grown men, cut through the air.

Jeok Cheongang had been relentlessly pressing the retreating Eastern Heaven Demon Lord. Now he let out a shout like a burst of flame.

“How dare a bastard like you!”

In that moment—

*Fwoosh! KABOOM!*

The Force of the greatsword, stronger than it had been in life, met the heat of the Flame-Extinguishing Divine Fist.

No—it was swept away by it.

*Crack. KABOOM!*

A faint sound, like something splitting apart.

The Force, unable to withstand the terrifying power, shattered along with the greatsword. The blazing flames melted the dozens of fragments and sent them flying back.

Straight toward the wielder of the greatsword, who had dared to challenge the name of the Fire King.

*Papat! Thud!*

More than ten blood-streaked shards shot into him like flashes of light, shattering flesh and bone as they lodged inside.

The impact shook Golden Ox Palace’s body, and the blood still left inside him gushed out like a fountain.

*Splaaat!*

Any physician in the land would have looked at the wound and been certain he was dead on the spot.

But Golden Ox Palace had become a monster, and with that came a cursed tenacity—a life that refused to end. He also had a mission that had to be completed, no matter how many times he died.

—Kill the Fire King.

His master’s command, driven deep into the empty consciousness that had opened before him. His sole mission, engraved in the sound of the bell, poured strength into the swaying corpse. It sent him charging forward without a care for the pain he’d already forgotten.

Just as he was now.

*GRAAAH!*

With his whites showing and a roar that made anyone who heard it feel fear, the commander of the Imperial Guards, once called Golden Ox Palace, shot forward. His broken golden armor gleamed, proof of the fame he’d earned in life.

*Whoosh!*

The wind buckled. Space vanished.

Even as the armor and flesh of his body melted together in the heat and flames blocking his path, he didn’t stop.

Like an enraged bull, true to the name Golden Ox Palace, he charged with all his might.

At one person alone.

The giant known as the Fire King.

And to carry out the order of his master, who meant to use him as a shield to bring that giant down.

*Tssss!*

Force surged over what could no longer be called a greatsword, with barely a handspan of blade left.

But in that moment, Jeok Cheongang’s keen senses detected another attack closing in from an angle.

“……!”

The Eastern Heaven Demon Lord. It was him.

A man as powerful as he was cunning, a vengeful spirit willing to turn himself into a living monster to avenge his sect’s grudge, twisted his body and shot toward Jeok Cheongang like a flash of light.

Alongside another monster, one who paid no heed to the flames of the Flame-Extinguishing Divine Fist.

*Damn it.*

In the slowed world, a flicker of conflict crossed Jeok Cheongang’s eyes.

They were less than one *jang* away.

It was too late to retreat.

Dodge?

Of course, that would be best if he could manage it. But if he failed, and ended up with an even more serious injury…

*I’ll die. No question.*

And Jeok Cheongang wasn’t worried about his own life.

It was the one fighting not far away.

His proud Disciple was exhausted to the limit, yet still driving Ma Sanbao back.

*If this old man falls here, it’s all over.*

That was why he couldn’t avoid the attack bearing down on him.

He had no choice but to fight back.

Even if he suffered an injury he’d never recover from, even if his life ended, he had to win this clash.

He had to give those monsters a certain death they would never overcome again.

*Yes. That’s the only way…*

The boy would live.

*Fwoosh.*

In the slow-moving time, a single flame blossomed beautifully.

*I’ll kill you. I’ll kill you until you die.*

The Fire King Jeok Cheongang swung both arms, unleashing flames more fierce than ever before.

*KABOOM!*

The deafening boom and the flash that filled his vision returned time to motion. Within that shuddering moment, a streak of swordlight mingled with a familiar cry.

“Old Master!”

*Thud!*

Hot blood fell.
## Chapter artifact 916

# Chapter 916

It happened in an instant.

In that brief span of time, split and split again until it was barely a moment, everything began and ended like a flash of light.

*Thwack!*

Jeok Cheongang heard it clearly. He saw it, too.

The single, chilling sound of something bursting against his ear. At the same time, something sticky splashed across his vision, turning it red.

*Drip. Splaaash.*

In that moment, the world Jeok Cheongang was looking at stopped.

Everything was red. The blood covering his face was hot.

And… it hurt.

More than anything ever had.

*Why?*

The hollow question that surfaced in his mind faded helplessly.

No—perhaps what was fading was Jeok Cheongang’s consciousness.

His mind was trying to process a sight that should never have happened, while pain and emotion boiled up from his chest, driving him into a confusion and rage he had never known before.

*Slide.*

He was falling. Tilting.

In the slowed world, a familiar figure was slowly flung away, his back to Jeok Cheongang as scarlet blood sprayed from him. The sight burned itself into Jeok Cheongang’s wide-open eyes like a brand.

“……!”

The Fire King Jeok Cheongang understood. He accepted it.

That every unbelievable thing unfolding before his eyes was real.

And what the second Disciple he had taken in late in life meant to him.

And, moreover, that he was not the only one who felt this way.

*Thump.*

His hand reached out through time as it flowed slowly, supporting that familiar back.

It was firm and warm.

Like the heart of the Disciple who had thrown himself forward with all his might to save his Master in danger.

Like the blood spilling from his chest, split wide open.

*You foolish, foolish boy.*

He had lived for well over a hundred years. He had seen countless kinds of people across the vast land, watched them rise and fall, and found his own path amid it all.

Every step he had taken along that path.

He had always been decisive and unhesitating.

But even Jeok Cheongang didn’t know what to say in this moment.

What could he say to that fearless bastard who had thrown himself in front of Force in place of his Master—to that unfilial Disciple who dared to leave before his Master?

There was only one thing he knew he had to do.

He could not let the moment his Disciple had bought with his life go to waste. He had to trust the vitality of the boy who had survived, as if by miracle, in every kind of hell.

*You have to survive. No matter what.*

With a silent plea, the old Master made the flames still burning in both his hands flare even more fiercely.

*Tssss.*

The air burned. The moisture evaporated.

And within it, time—once stopped—began to flow again.

At its end—

*Fwoooosh!*

There was a massive blaze that swallowed even death.

* * *

*Hummm.*

In that moment, everyone saw it.

No—they felt it through all five senses.

They saw the space warp in the dreadful heat, felt pain in their muffled ears, and trembled at the terror that suddenly came through the scorching air and wind.

Not one person was spared.

The living and the dead alike.

Even the Eastern Heaven Demon Lord—who had been watching with wide eyes as So Gyo tirelessly cut down the charging monsters and Jin Taekyung fell, spraying blood—felt a chill crawl down his spine.

No. It was heat, as if his insides were melting.

*This is…*

In that moment, the Eastern Heaven Demon Lord instinctively understood that this strike contained something that could not be explained by internal energy alone.

The grief and rage of the old Master had drawn out a latent power he himself had not known he possessed.

*I’ll die.*

The fear of death, forgotten and believed to be something he would never feel again, awakened.

A killing intent more intense and horrifying than the one he had felt while facing So Gyo over a decade ago surged around him.

Toward the Eastern Heaven Demon Lord himself—and everyone else.

“Ru—”

And in that instant—

*KABOOOOOM!*

With a tremendous roar that swallowed the Eastern Heaven Demon Lord’s scream, a pillar of blazing white fire shot forth.

*CRACK! RRRRUMBLE!*

The fire dragon thrashed. It melted the ground and incinerated everything.

The fire dragon, swallowing the field of vision as it surged in like a wave, greedily chewed up everything its enormous body touched.

It burned and vaporized it, as if it would leave not even a drop of moisture behind.

The blades rolling on the ground, abandoned by their owners; the impossibly hard bluestone; the soil and rock beneath it.

Even bodies that had already transcended death once.

*KABOOOOOM!*

The Eastern Heaven Demon Lord saw it clearly. He heard it without a doubt.

Golden Ox Palace, reborn as one of his followers—the Supreme Peak master whose martial prowess had been so formidable in life that he was counted among the Twelve Palaces of the Zodiac—was engulfed in white flames.

He heard Golden Ox Palace’s dying scream.

*GRAAAAH!*

It was impossible. How could someone who no longer felt pain scream so horribly?

How could he thrash about so desperately?

*How…?*

The Eastern Heaven Demon Lord was appalled. At the same time, he felt the Extreme Yang heat that seemed capable of burning his very soul.

At its center, he saw the red glow of one man’s eyes.

“You shouldn’t have touched my Disciple.”

The Fire King Jeok Cheongang.

*ROOOOAR!*

As he heard the fire dragon’s roar, loud enough to shake the whole imperial capital, the Eastern Heaven Demon Lord prepared to die. He seized and drew out every bit of strength he had left.

He blamed the subordinate who had been so damned faithful to his orders that he couldn’t stop, and blamed himself for bringing about the touch upon the reverse scale of the dragon called the Fire King.

But…

*It’s not over yet.*

Not his life. Not his revenge, which he had carried for more than half a century.

*Fwoooosh.*

The death energy of the dead wrapped itself around the Eastern Heaven Demon Lord’s entire body. The flames breathed out by an old, weary dragon struck over it.

*KABOOOOOM!*

* * *

I don’t know.

How much time had passed. If I died like this, how much time I had left.

My dulled senses and blurry vision couldn’t tell me much.

The ground shook as if there’d been an earthquake. A deafening roar kept pounding against my muffled ears.

And… heat.

It was hot. My body was sprawled out any which way, beyond my control, but I could feel the heat more clearly than anything else.

*Old Master’s pissed as hell.*

I wanted to cackle out loud, but the next moment, something sticky slipped between my trembling lips. It wasn’t laughter.

*Cough.*

Blood. Dark red blood, with little clots mixed in.

When I felt the squishy texture as I touched my mouth, I paused to wonder.

Was that my lip? Or a piece of my insides?

*…Damn it. I know which.*

I let out a small sigh.

It was almost sad to hear myself say it, but it wasn’t as if this was the first time.

One thing that was both strange and a little unfair was that I’d never been this badly injured back when I was an F-rank Hunter.

*Of course, I’m only alive in this state because I got stronger.*

I forced what little strength I had left into lifting my head. Dust and ashes filled every direction. Through the aftermath, which had yet to clear, all I could see was my own body.

A body covered in wounds, large and small.

And a chest left horribly exposed—flesh and bone torn open where Force had ripped through it.

*Cough. Cough.*

I spat up blood again. This time, it was even darker.

Proof that the sword strike I’d taken earlier had reached not only my flesh and bones, but my internal organs as well.

*That was insane.*

Yeah. It had definitely been insane.

Something I wouldn’t have done if I’d been thinking straight. No—even a reasonably crazy bastard wouldn’t have dared try it.

But I did.

I had to.

*How could I just stand there and watch?*

If I hadn’t thrown myself forward at the last moment, even turning my back on Ma Sanbao, then the one lying here now would have been Jeok Cheongang, not me.

The Eastern Heaven Demon Lord wasn’t just a sorcerer who commanded the dead. He was also an incredibly skilled fighter, and no matter how formidable Jeok Cheongang was, it would have been too much for him to fight the Eastern Heaven Demon Lord and another Supreme Peak master at the same time.

Of course, a part of me had hoped that maybe it would work.

To the Eastern Heaven Demon Lord, I wasn’t only an enemy he had to defeat. I was someone the Lord of Heaven wanted.

*So much for taking me alive. He just went and stabbed me.*

I laughed, coughing up blood foam.

I’d gambled my life and failed spectacularly.

And this was the result.

Lying sprawled out like a corpse, feeling my senses slowly slipping away as I waited to die.

But the reason I could still laugh was that I was the only one who’d lost this gamble.

The outcome of the massive gamble taking place on this battlefield today wouldn’t be decided by my life alone.

Some would pay for defeat with their lives; others would survive by winning.

I was the former. That was all.

Regrets?

It’d be a lie to say I had none.

But I knew my own condition better than anyone. No—maybe even this was just human instinct.

Death.

I could see it.

The thing that had already taken a father from my family—the unwelcome visitor I’d narrowly avoided through every danger I’d faced—had finally come for me.

Even now, through my fading vision, a black shape seemed to waver amid the falling ash and dust.

*Don’t come.*

I tried to squeeze out a voice with all my strength, but all that came from between my lips was a little blood and a ragged breath.

But I didn’t give up.

Clinging to a consciousness that seemed ready to go out at any moment, I swallowed the blood pooling in my mouth and forced myself to stay alert.

I was afraid. Of death.

I was afraid to leave everyone behind like this.

There was still so much I had to do. So many things I wanted to do with the people I loved, who loved me.

But, but why?

Why was that shadow coming closer to me?

Why wouldn’t it stop walking, even now?

I wasn’t ready yet. I didn’t want to die like this.

*Just a little longer. Even for the briefest moment.*

I gasped for breath and begged.

I asked it to wait just a little longer. Even if it took me away after that, I wanted time to say goodbye. I desperately prayed for one last chance to see the faces of the people I’d been connected to. My family.

I prayed to a god I had never seen.

No.

To the System.

“Please…”

And in the moment those words escaped me, wrung from the last of my strength—

*Ding.*

A clear chime that only I could hear rang out across the whole world.
## Chapter artifact 917

# Chapter 917

*Fwoosh.*

A fierce gale roared through the air. Layers of black ash that had piled up across the ground, along with embers that still hadn’t gone out, rode the wind and scattered in every direction.

Then, from within that pale haze that blocked everyone’s view, a fist wreathed in flames cleaved through space.

*BOOM! KABOOOOOM!*

Compressed air burst apart. Beyond the scorching air, white flames surged.

It was a fire nothing could stop.

The breath of a dragon. Its roar. A rage so vast it could not be measured.

The flames of the old dragon poured down on those who had dared touch his reverse scale, burning more fiercely than ever.

So fiercely that someone who had already become nearly immortal found himself thinking of the word *death* without even realizing it.

*Ah.*

The Eastern Heaven Demon Lord let out a quiet groan.

His gray eyes, now a mix of fear and awe, remained fixed on the man approaching him, endlessly pouring out flames.

Jeok Cheongang, the Fire King.

It was him.

Only him.

The ten Kings who had failed to reach that lofty heaven.

And now, the foremost among them—the Emperor of Fire—was finally spreading the wings he had kept hidden and soaring upward.

Toward the three stars adorning the heaven called the Martial God.

Pouring out his rage at the enemies who had touched what they should never have touched.

*Rumble.*

A tremendous impact hammered his entire body.

The death energy that had surrounded the Eastern Heaven Demon Lord without a gap shuddered beneath a palm strike imbued with unprecedented power.

His legs, planted in the ground with roughly six tons of force, carved deep furrows as they were driven backward.

*BAM! BAM! KABOOM!*

One advanced.

The other had no choice but to retreat.

Jeok Cheongang was the former; the Eastern Heaven Demon Lord, the latter.

He was like a sinner hunched low, desperately dodging the thunderbolts raining down without pause like divine punishment.

*How? How in the world…?*

How could that exhausted body, already covered in wounds great and small, wield such strength?

How could he feel such rage?

The Eastern Heaven Demon Lord swallowed the sigh that rose to his lips.

And found himself understanding the fierce anger of Jeok Cheongang, approaching with an overwhelming aura—his rage so intense it felt as if he could reach out and touch it.

Because he was the same.

*BAM!*

He had lost his family.

*BAM!*

He had lost his sect.

*BAM!*

When he thought he had lost everything, he found something left in a corner of his emptied heart.

*Rage.*

They said a person was human because they could feel joy, anger, sorrow, and pleasure.

They said a being was alive because it could laugh, rage, grieve, and feel joy.

But the Eastern Heaven Demon Lord had lost three of those things.

With nothing left but rage, he had finally given up on being human and become a monster.

A monster called a vengeful spirit.

That was why, in a way, he understood Jeok Cheongang—the feelings of an old Master who had seen his Disciple standing at the crossroads between life and death.

He understood, too, the rage held within that mighty flame, which was trying to burn even the death energy he had summoned with all his might.

*KABOOOOOM!*

In that instant,

the Eastern Heaven Demon Lord felt it.

The death energy encircling him had finally reached its limit.

At this moment, Jeok Cheongang’s rage had surpassed his own.

*Crack.*

The sound announcing a rift reached the Eastern Heaven Demon Lord’s ears. The energy that had poured ceaselessly from deep within his body was scattering.

At the starting point of that rift was a fist wreathed in pure white flames—and a pair of eyes pouring out stream after stream of fire and an even greater heat, flames that would bring down his last line of defense.

“Understand this clearly.”

The light in Jeok Cheongang’s eyes seemed capable of turning anything it faced to ash.

“Understand what you’ve touched.”

Yet his voice was as cold as the glaciers of the North Sea. It froze the Eastern Heaven Demon Lord’s spine and seeped into his soul.

It awakened a fear he had long forgotten, ever since the day he rose from death.

*Hah.*

The Eastern Heaven Demon Lord trembled without meaning to. A hollow laugh escaped him.

And suddenly, he understood.

*Perhaps the Three Saints… or even beyond.*

At least at this moment, there was nothing that could stop the old dragon’s rage.

Nothing.

*CRASH!*

At last, it split and shattered.

As everything surrounding him broke to pieces, the Eastern Heaven Demon Lord thrust out his fist toward the white flames flooding his vision.

*Whoosh!*

A movement faster than sound.

The dead clashed with the living.

In a world turned pure white, the Flame-Extinguishing Divine Fist advanced slowly and met the Eastern Heaven Demon Lord’s fist.

No.

It swept right through it.

*BAM!*

The clash lasted only an instant. A tremendous boom rang out.

But the time their fists met was far too brief, and the balance of power had already tipped.

*Crack.*

Heat swallowed the scattered death energy and crushed his skin. It melted his acupoints and sinews, then shattered his bones.

The stronger body and resilience the Eastern Heaven Demon Lord had gained by abandoning his life as a human were of no use.

*KABOOOOOM!*

Jeok Cheongang’s fist was lava and lightning at once.

As its name implied, the flames he unleashed—the Flame-Extinguishing Divine Fist—shot forward, reducing everything to ash.

They swallowed not only the Eastern Heaven Demon Lord’s fist, but his entire arm.

*Fwoosh. BOOM!*

The flames erupted at their peak.

But there was no blood, no scraps of flesh, not even the common fragments of bone that ought to have burst from the wound.

They had all vaporized or turned to ash. They had vanished beyond any hope of recovery unless time itself could be turned back.

The Eastern Heaven Demon Lord knew that better than anyone.

So did Jeok Cheongang.

*Step.*

With a single stride, Jeok Cheongang folded the space before him.

The Eastern Heaven Demon Lord, thrown backward like a misfired cannonball, gritted his teeth and twisted around.

*Crack. BAM!*

The fist that grazed his side—though “grazed” meant it had pulverized a chunk of flesh and bone a handspan wide—slammed into the ground.

At the same time, a tremendous boom split the sky, and a massive crater opened in the earth.

A chill ran through him.

The Eastern Heaven Demon Lord felt as though the hairs all over his body were standing on end.

If he could feel pain like an ordinary human, if he had fought Jeok Cheongang as he was now, how long would he have lasted?

How many times would he have died?

*This is…*

He had thought himself immortal. Unless the Martial God, who had vanished long ago, returned, he had been confident no one who came for him could bring him down.

But that wasn’t true.

*If I can’t dodge, I’ll die.*

The Eastern Heaven Demon Lord wanted to live.

Even if he had already died once, he wanted to keep living this life.

At the very least, he had to bring down the Imperial House, heir to that loathsome bloodline, and this Great Nation, Taizu’s achievement and legacy.

Until his revenge was complete, he could not fall.

For his family and fellow members of his sect, who had met such horrific deaths.

And for himself—the Eastern Heaven Demon Lord, who had chosen to become a monster for the sake of this very day.

*I. I…*

*Grind.*

The Eastern Heaven Demon Lord clenched his teeth. With no blood left, pieces of flesh fell away instead.

*I cannot fall. Not ever.*

Even the Eastern Heaven Demon Lord himself couldn’t tell what it was.

Was it the rage that had carried him this far? His obsession with revenge?

Or the last fighting spirit of a martial artist who had finally met the greatest enemy of his life?

One thing was certain.

Just as Jeok Cheongang had moments earlier, the Eastern Heaven Demon Lord had also surpassed his former limits.

*Whoosh!*

In the blink of an eye, Finger Qi streaked across space like lightning and pierced Jeok Cheongang’s neck.

No—it only looked as though it had pierced him.

The Jeok Cheongang who had charged at the retreating Eastern Heaven Demon Lord like a streak of flame—whose image should have fallen with blood spraying from its pierced neck—did not unravel like a heat haze until then.

“……!”

At the instant those four characters flashed through the Eastern Heaven Demon Lord’s mind—Shifting Form and Position—he spun around and swung the bell clutched in his only remaining arm.

*Whoosh!*

The bell sliced down with a fierce whistle, gleaming as it brimmed with death energy.

A single blow. If even one strike landed cleanly, no one could come away unscathed.

That was the nature of battles between the Supreme Peak masters called superhuman.

The Fire King and the Eastern Heaven Demon Lord—monsters whose martial prowess could not be fully expressed even by the three words “Supreme Peak.”

But—

*Crack.*

Not against someone who, at least in this moment, had reached a new realm—one he might never reach again, perhaps not even after today.

*Was that all you had?*

It wasn’t a voice spoken aloud, nor was it Sound Transmission.

But the Eastern Heaven Demon Lord heard it clearly. He saw it, too.

In the fire-wreathed hand that gripped the bell and the fiery gaze that fixed on him; in Jeok Cheongang’s tightly closed lips, he heard a voice that made no sound.

At the same time, he saw his own arm engulfed in flames in the next instant.

*Fwoosh! KABOOOOOM!*

A fire that spread over a mountainside might burn for days before it died out. But the Scorching Yang Qi that rose at its master’s Will did not.

It carried a dreadful heat, but it began in an instant and faded just as quickly.

It melted the Eastern Heaven Demon Lord’s only remaining arm without leaving a trace.

But the punishment of the enraged Master did not end there.

*CRACK!*

The Eastern Heaven Demon Lord’s vision shook.

As his arm melted away without a trace, a fist smashed into his side. It crushed flesh and bone, then poured flames into his long-rotted internal organs.

*No!*

Every blow from Jeok Cheongang brought death one step closer.

*SHWAAAA!*

Half the Eastern Heaven Demon Lord’s upper body had been scorched black by the previous attack. He didn’t resist the force throwing him backward.

Instead, he poured all the energy left in his still-healthy legs into his escape.

He had already lost both arms and the bell.

He had to put as much distance between them as possible.

But as he kicked off the ground with all his strength, he felt a force of roughly six tons seize his ankle.

*Crack.*

A force that crushed flesh and shattered bone.

And at the same time—

*Whoooosh!*

The world turned upside down. Through the crushing wind, the ground rushed up to meet him.

*KABOOOOOM!*

A thunderous roar drowned out his ears, and the earth’s crust surged upward.

His eyelids trembled as he lay buried deep in the ground, breaking through dirt and rock in a place that had hardened as solid as granite.

*This is…*

For well over half a century, he had operated in the shadows of the Imperial Palace and observed countless Supreme Peak masters.

That was why he knew.

This wasn’t a matter of speed or strength.

It was simply that Jeok Cheongang now stood in a realm beyond his.

*Rumble.*

He couldn’t feel even a shred of pain. That was why he felt it all the more clearly.

One of the two legs he had left had just been torn off.

And that meant one thing.

*There’s nowhere left to retreat.*

The Eastern Heaven Demon Lord let out a hollow laugh.

Was it the smile of someone who had finally accepted the death bearing down on him?

No.

It was the bitter laugh of someone who had waited so long for revenge, but had been forced to choose between that and his life—and who had decided to reveal the hidden sword he had meant to draw at the very end.

“—Come out, Heaven’s Slaughter.”

And just as a faint line of Sound Transmission, its meaning unclear, slipped between his moving lips—

*Shiver.*

The empty air wavered.

An assassin dropped through the drifting ash and embers. An old man shot forward like a flash of light, his limp belying his speed, and slashed a dagger down at the crown of Jeok Cheongang’s head.

*Whoosh!*

An ambush close to perfect—no, a perfect ambush that no one could deny—was about to succeed when—

*SHWAAAA!*

A spear, a streak of flame, cut through space.
## Chapter artifact 918

# Chapter 918

*Whoosh!*

In the slowed world, the Eastern Heaven Demon Lord knew instinctively as the old man plunged down like a flash of light, dagger in hand.

*It’s over.*

It was an utterly perfect ambush.

An unavoidable strike for even the Fire King Jeok Cheongang as he was now—no, all the more unavoidable because he had lost his composure and was angrier than ever.

Even if he somehow managed to block or dodge it and escape death, the Eastern Heaven Demon Lord judged that severe injuries were inevitable.

The limping old man he had called Heaven’s Slaughter was one of the finest assassins in the Central Plains, comparable even to the Slaughter Saint.

*I kept that sword hidden for the Emperor.*

It was bitter, but there was nothing to be done.

The grand plan was already on the verge of falling apart.

Survival came first now.

No matter how long it took or what means he had to use, he had to finish his revenge with his own hands.

He could not die until he had watched with his own two eyes as the imperial family, heirs to that cursed bloodline, was wiped out—and offered a memorial rite for his Master and fellow disciples, who had met untimely deaths.

But to begin a revenge that might never come again, he first had to bring down the monster bearing down on him.

The Fire King Jeok Cheongang.

That monster rampaging like a fire demon sweeping across a boundless plain.

*Die.*

The Eastern Heaven Demon Lord was certain of it. At the same time, he prayed fervently for it.

And then, just as the dagger in the old man’s hand—its blade dulled by a coating of ash—brought Force to bear, about to cut Jeok Cheongang in two—

*SHWAAAAK! BOOM!*

A sound of something piercing the air rang out from somewhere, reaching the Eastern Heaven Demon Lord’s ears.

It drowned out every other sound as it tore through the air in a furious rush.

The Eastern Heaven Demon Lord’s eyes flew wide. A blue-white flash had reached its destination before its sound did, filling his vision.

*What is that…?*

A spear of a common, unremarkable design—the sort one could find anywhere.

But the light upon it shone as brightly as the sun overhead, and its heat, hotter than the sun itself, burned even the air as it raced onward.

Toward Jeok Cheongang.

No—to be exact, toward the old man falling above his head.

“……!”

“……!”

“……!”

At that moment, everyone’s movements stopped. The world they saw stopped with them.

Jeok Cheongang, who had belatedly realized the assassin had appeared out of nowhere. The old man plunging down at him like a bolt of lightning. And the Eastern Heaven Demon Lord, watching it all unfold.

*Shwoosh!*

They all watched the spearhead cut through the air toward them, moving as if in slow motion. They felt the power within the blue-white flames coiling around its point.

And at the same time, they understood.

Who owned that spear.

What root that horrifyingly intense Scorching Yang Qi came from.

Before the three-syllable name that had suddenly surfaced could even take shape in their minds, the spearhead had raced forward, erasing the space between them, and reached its destination in an instant.

At the life-or-death moment, the old man frantically changed the direction of his dagger and brought it up to block the spearhead that had come within inches of him.

*Whoom—KABOOOOOM!*

Blue-white flames swelled as they met the Force surging from the dagger. A thunderous boom shook heaven and earth, and the shockwave lashed out in every direction.

*KRRRACK!*

The earth shuddered as if struck by an earthquake. Wind whipped about madly.

In that muffled world filled with nothing but ash, the Eastern Heaven Demon Lord finally pieced together one man’s name and screamed it like a wail.

“Jin Taekyung!”

At that moment—

*Fwoooosh.*

The hazy world split apart.

A blood-soaked man, from head to toe, approached with movements lighter and quicker than ever. He showed his white teeth and grinned.

“Don’t say my name. I might get attached.”

Then he shrugged toward one man standing dazed and motionless at the feet of the Eastern Heaven Demon Lord, who was sprawled there, stiff as a statue.

“Looks like this bastard still hasn’t come to his senses. Should I pull out his tongue while I’m at it?”

“……”

“Old Master?”

The Fire King Jeok Cheongang, his old Master, didn’t answer.

No—he couldn’t answer.

He silently gazed at his Disciple, who had come back as he always did. Then he burst out laughing.

He was so delighted that tears came to his eyes.

At the same time, he felt all the anger and sorrow that had held his whole body in its grip come crashing down, and he grasped his Disciple’s arm tightly.

“Thank you.”

*Grip.*

“For coming back. For coming back to me like this.”

“……!”

The blood-dried corner of the blood-soaked man’s eye—no, Jin Taekyung’s eye—trembled.

*Thank you. For coming back.*

It was a brief sentence, but it was enough.

He could feel the warmth conveyed through that arm, and the sincerity that seeped into every syllable of his Master’s words.

That feeling meant everything.

And so, there was no need for them to say anything more.

This brief reunion between the two men who had carried on the Fire Gate Clan’s lineage would soon become the deaths of their enemies.

That was how the Fire Gate Clan had survived for the past three hundred years. It was the way of these two, bound together as Master and Disciple by a connection no one could explain.

*We’ll smash and burn everything in our way.*

Whatever it is.

We will. Without fail.

*Step.*

Master and Disciple moved forward at the same time. Beyond the dust cloud and ash that had yet to settle, a sticky killing intent crept toward them in secret, wrapping around them.

*Whoooosh!*

* * *

The limping old man, Heaven’s Slaughter, blended into the darkness and quietly waited for his moment.

Even as he watched his subordinates die less than a dozen *jang* away, there wasn’t a trace of agitation in his cool, sunken eyes.

*Whoosh. Slice!*

Before the blade dulled by ash could even reach its target, a head sprang into the air.

Anyone who saw this would find it hard to believe.

Each of those men crumpling like straw dummies was an elite assassin he had spent at least thirty years cultivating.

*I thought I could take down even the Three Saints with those children.*

No—perhaps he really could have.

His ambush just moments earlier had been that perfect. He could have erased the giant known as the Fire King Jeok Cheongang from this world with his own hands.

If not for the unwelcome visitor who had appeared out of nowhere.

*Blazing Flame Divine Dragon Jin Taekyung.*

Heaven’s Slaughter swallowed the groan that threatened to escape him.

It wasn’t just the pain in his broken wrist, which had snapped as he deflected the spear filled with immense energy at the last moment before success.

*So the real monster wasn’t the Master…*

He had seen it with his own eyes in the darkness.

Jin Taekyung, falling with an injury beyond recovery. The shadow of death stirring at the edge of his life as he coughed up blood mixed with pieces of his organs.

*And yet, how could he possibly…?*

Those who roam the martial world with death for a companion are martial artists. And among them, assassins stand closest to death.

That was why Heaven’s Slaughter knew better than anyone.

Since the time he had been trained as an assassin, he had killed people with his own hands using every means at his disposal. For the weight of those deeds, he had even reached death’s threshold himself.

*If Dark Heaven hadn’t helped me, this old man would have turned to a handful of dirt long ago.*

Heaven’s Slaughter’s survival was a miracle. But even that seemed insignificant beside what Jin Taekyung had shown just now.

There was no doubt. Force had pierced straight through his chest.

It had split flesh and bone, destroyed his acupoints, and seeped into his organs, tearing them to shreds from within.

This was an injury no one could recover from—not even with the Great Firmament Immortal’s care, or if Yama himself erased their name from the book of the dead.

And yet Jin Taekyung had come back alive.

Though he looked like a man drenched in blood, his exposed skin was smooth, and his perfectly formed Muscles and Bones—the reason he was known as having a Heavenly Martial Physique—were plain to see.

And that wasn’t all.

His formidable internal energy, amounting to several *jiazi*’s worth—impossible to believe in someone who had only just passed the age of twenty—had also filled back up as if nothing had happened.

As if someone had filled an empty teacup with water.

As if it were only natural.

*This is… something I can’t explain.*

An ability that transcended all reason.

Heaven’s Slaughter’s deeply sunken eyes trembled.

Now, his composure—barely held together until this moment—had finally crumbled. He was truly torn between two choices.

Flight and duty.

And he wondered who would kill him: Dark Heaven or Jin Taekyung.

Several decades ago, when Heaven’s Slaughter had been gasping at death’s door, Dark Heaven had made him an offer he could not refuse. It had never been out of pure kindness.

A blade forged by Dark Heaven.

A human butcher who moved only at Dark Heaven’s command.

That was the new identity Heaven’s Slaughter had exchanged his life for. A shackle he could never break, no matter how far he ran.

If he abandoned his mission and fled, punishment was all that awaited him.

A horrible death in unbearable pain, beyond even what a man who had spent his life committing countless murders could imagine.

There was nowhere to hide. Nowhere to run.

That was Dark Heaven—or rather, the Lord of Heaven.

*Heh. Heheheh.*

Heaven’s Slaughter laughed without a sound.

He thought himself a fool for agonizing over a problem whose answer had already been decided.

There had never been a choice to make.

There had only ever been one path in front of him. One option.

*Kill or be killed.*

Heaven’s Slaughter moved quietly through the darkness.

He silenced his breathing and erased his presence. Watching the elite assassins he had carefully raised with Dark Heaven’s help get slaughtered, he slowly approached Jeok Cheongang and Jin Taekyung.

*If I can take down even one of them, I can survive—even if I fail the mission and flee.*

The grand plan had already gone awry.

But if he brought back something of equal value—if he brought back the Fire King Jeok Cheongang’s head—he might be given another chance.

A chance to carry on his unfulfilled revenge, to keep this stubborn life going.

And, to his great fortune, even the heavens, usually so indifferent, seemed to be on Heaven’s Slaughter’s side today.

*Whoosh! Whoosh! Slice!*

Another life vanished with a piercing sound. But unlike Jin Taekyung, who was rampaging as if possessed, Jeok Cheongang looked utterly exhausted to Heaven’s Slaughter.

*Patapat. Splurt!*

Hidden weapons came flying from every direction, grazing Jeok Cheongang’s body. Then, after killing with a single palm strike the assassin who had dropped down from above, the old dragon exhaled raggedly through his lips.

*Huff. Huff.*

His lips were dry and tinged pale blue. His body trembled faintly, even as he continued to unleash attacks of terrifying power.

At the sight of Jeok Cheongang, who seemed to have forgotten the fearsome martial prowess he had displayed only moments ago, Heaven’s Slaughter muttered to himself.

*He’s reached his limit.*

In a way, it was only natural.

Jeok Cheongang had already drawn out martial prowess beyond his limits against the Eastern Heaven Demon Lord, and his body had been covered in large and small wounds even before that.

And that opening was Heaven’s Slaughter’s only chance.

*This strike will end it. No matter what.*

Heaven’s Slaughter calmed his mind. He erased even his killing intent—the very energy anyone about to kill someone would carry.

No one feels murderous intent when killing livestock instead of a human.

After living his whole life as a butcher under the name of assassin, he finally shot straight forward with all his might.

At the same time, he realized.

Though he himself was still cloaked by his concealment technique, he saw Jin Taekyung staring straight at him. He felt that gaze pierce his entire body.

*He knew from the beginning…*

*Puhk.*

A blazing flame pierced his chest.
## Chapter artifact 919

# Chapter 919

There are two main ways a predator hunts its prey.

It can chase it down itself—or make the prey come to it.

The first is simple. The second is hard.

But the harder the hunt, the greater the chance of success.

Luring prey right up to you means you’ve made it lower its guard.

Or…

*You’ve made the prey mistake itself for the predator.*

One thing was certain.

At that very moment, the body touched by the spearhead flashing through the air belonged unmistakably to the latter.

*Puhk!*

A gruesome sound of flesh being pierced announced the hunt’s success, and the air rippled.

Where only ash and dust had been swirling, an old man—no one knew when he had appeared—quivered like a fish skewered on a harpoon.

“Wha—how…? Cough!”

Blood spilled from his mouth, running down his chin before he could finish speaking.

I looked at the old man’s face, twisted into a Fiendish mask of pain, and spoke in a calm voice.

“I saw you. Clear as day.”

“That’s impossible. It can’t be.”

The old man gasped for breath. The assassins—now barely a dozen—came rushing from every direction to save their leader in his moment of danger.

Like moths throwing themselves into a flame, even though they knew they would burn.

But the ending to this short story had already been decided.

From the moment I opened my eyes to the sound of a clear bell.

And from the moment Jeok Cheongang showed weakness to lure in prey that might flee at any moment.

*Boom!*

The heat of the Flame Divine Palm warped the air.

When the predator known as the Fire King swung his flame-cloaked claws, the moths fell without even a dying cry.

*Rustle. Thud.*

The last assassin, his upper body charred black, dropped to his knees.

There was no need to check. He was dead.

With his last hope extinguished right before his eyes, the old man’s voice sank into an oddly calm murmur.

“So you showed an opening to lure in your target. You have more of an assassin’s nature than I expected.”

I furrowed my brow, pretending to take offense.

“That sounds like a compliment, but somehow it feels like an insult. Every assassin I’ve ever met has been trash, except for one.”

“Of course.”

The old man gave a tiny, spasmodic nod and continued.

“Mungyeong. Is that bastard still the same?”

“What?”

My brow furrowed before I could stop it.

Mungyeong was the Slaughter Saint’s real name.

And fewer than five people in all the world knew that.

Maybe even fewer than that.

Even if you counted me.

“How do you…”

“You’re asking how I know that name?”

The old man coughed up blood again, then added, “I couldn’t not know. He told me himself.”

In that moment, I thought I realized who the old man was.

A few months ago, while I was in Sichuan, the Slaughter Saint had mentioned Salcheonmun in passing. It was one of the few things he’d revealed about his otherwise shrouded past.

“Salcheonmun.”

The greatest assassin sect in the world, once feared by all.

But it had been destroyed by the dagger it had forged—the Slaughter Saint—and was now just a remnant of the past, forgotten by most.

At those three words, which had slipped from my lips, the old man nodded and smiled faintly.

“Mungyeong. Make sure you tell him this.”

A fierce light flashed in the dying man’s eyes. His lips were still pouring blood, but a voice full of killing intent slipped out between them.

“Tell him we—the Salcheonmun—will come for him. No matter the sacrifice, no matter how many years pass, we will come.”

Hmm…

Judging by that, it definitely wasn’t a reunion for Salcheonmun’s twelfth class.

The kind of reasonable, beautiful ending where they meet up, polish off a few bottles of Jiannan Chun, call a designated driver, and ride home in a carriage wasn’t something the assassin world did.

Especially if the Slaughter Saint himself had brought about Salcheonmun’s destruction.

*First the Maoshan Sect, and now the Salcheonmun.*

I’d thought something was off from the moment I first saw him.

The chain of gratitude and grudges went on and on, no matter how far I dug. I let out a small sigh.

“I’m touched you went out of your way to give me such a thorough heads-up. Don’t worry. I’ll pass on every word exactly as I heard it.”

I looked the old man straight in the eye and added, “That’s what Gye Yabu of the Salcheonmun said.”

“……!”

The old man’s eyes, which had seemed ready to close at any moment, flew open.

The calm acceptance of his approaching death had vanished. His voice burst out along with a spray of blood, filled with undisguised shock.

“How—how do you know that?”

“I told you. I can see you.”

“……What?”

Instead of answering, I jerked my chin toward the space above his head.

Floating in the empty air was a translucent roster that no one but me in this world could see.



[Lv. 140 Gye Yabu]



It was a simple difference.

The old man—no, Gye Yabu—possessed concealment techniques bordering on the miraculous. I had a System that could be called a miracle itself.

And that difference had turned Gye Yabu into prey.

“Goodbye.”

With that farewell to mark the end of our brief encounter, I twisted the spear shaft in my grip.

*Crunch.*

My long-lost weapon, White Flame, at last, cut through bone and flesh like tofu and reached his heart.

The flames clinging to its transparent blade seeped inside him.

*Boom.*

His body staggered with a small explosion.

Gye Yabu poured dark-red blood from his seven apertures. He looked like a candle caught in a typhoon.

*Puhk! Splurt!*

I pulled out the spear and turned away. As I walked off, leaving his crumpling body behind, the long-awaited bell rang in my ears.

*Ding.*



> **System**
>
> You have defeated Lv. 140 Gye Yabu!
>
> You have gained a large amount of Fame!
>
> You have gained a large amount of EXP!
>
> If this becomes known, you will be pursued by the Salcheonmun.
>
> The Salcheonmun will not forget Gye Yabu’s death.



The System notification told me two things.

First, that Gye Yabu hadn’t been lying when he spoke before he died.

Second, that I’d grown strong enough not to level up even after killing a Level 140 enemy—and not to care even when warned I’d become a target of the Salcheonmun.

*It’s a little unsettling, though.*

Either way, I could just kill whoever came after me—and whoever left.

I didn’t know how many hardened human butchers the Salcheonmun had, but I already had the Lord of Heaven’s undivided attention.

How much hotter could a jalapeño really get if you added a Cheongyang chili?

I’d just have to drink a nice, cold glass of milk beforehand.

Living milk packed with EXP instead of calcium—the kind that could put an end to this damnable fighting.

“Sorry I’m a little late. Get bored waiting?”

*Step.*

My foot came to a stop in front of someone crawling away, scrabbling with the only leg he had left intact.

The Eastern Heaven Demon Lord confirmed it was me, then smiled through his twisted face.

“Yeah, you monster.”



* * *



Those who failed despaired.

They wept and sank into deep despair.

But the Eastern Heaven Demon Lord did not.

He neither despaired nor wept. He did not give in.

His revenge wasn’t over yet. There was still hope.

The grand plan had failed, but he was still alive.

*Even if a branch breaks, the tree doesn’t die.*

As long as the roots remained, the tree wouldn’t fall. Someday, it could grow new, sturdy branches and fresh leaves.

Just as everything from the Maoshan Sect, destroyed by Taizu long ago, had passed down to him.

That was why he struggled.

With just one leg, his undying body squirmed as he tried to escape.

*Not yet. It’s not over yet.*

Golden Ox Palace was dead. Ma Sanbao had disappeared, and he didn’t even know whether he was alive or dead.

And there was more.

He had lost the means to control the jiangshi, and the Salcheonmun assassins—including Gye Yabu—were dead.

But if that was all he had prepared for today, the Eastern Heaven Demon Lord would never have begun this grand plan.

*I need time. Time.*

It had been half a century since he had infiltrated the imperial court under the identity of a eunuch.

The shadow of darkness the Eastern Heaven Demon Lord had cast over the Great Nation was deeper and larger than anyone could imagine.

From commanders leading armies of tens of thousands to admirals commanding fleets.

And even the political heavyweights who could wield enormous influence with a few quiet words or a handful of hastily written lines.

The Eastern Heaven Demon Lord had more than satisfied their greed, and those who swore loyalty had willingly climbed aboard the same ship.

They had staked everything they possessed—their strength, their influence, their authority.

This great rebellion, meant to overturn the Great Nation, was not confined to the grand banquet hall.

And that was precisely why the Eastern Heaven Demon Lord could still smile at this very moment.

Why he could smile even as he faced a monster greater than himself.

“Sorry I’m a little late. Get bored waiting?”

*Step.*

The voice was light, as if greeting an old friend. But the footstep blocking his way was heavy and firm.

*Jin Taekyung.*

The face of one man crossed his mind, then appeared in the Eastern Heaven Demon Lord’s vision.

“Yeah, you monster.”

And at that very moment—

*Crack!*

With a gruesome sound of flesh being crushed, the only leg he had left was smashed to pieces.

Now missing all four limbs, the Eastern Heaven Demon Lord calmly spoke to another opponent through pain he could no longer feel.

“The world would be astonished to learn that the Fire King, famed for his rough ways, cares so deeply for his Disciple…”

*Crack!*

A booming crash drowned out the rest of his words.

Then, as the Eastern Heaven Demon Lord was driven deep into the ground, a voice reached his ears, growling like a beast.

“Shut your mouth. Before I rip out your tongue.”

“My tongue? You’d rip out my tongue?”

The Eastern Heaven Demon Lord gave a short laugh.

“That’s not a bad idea. It would be a new experience for me, too.”

“You bastard!”

“My ears are ringing. Stop shouting and try it. Right now.”

“……!”

“What are you waiting for? I said, rip out my tongue.”

But even after he urged him again and again, no answer came. The Eastern Heaven Demon Lord’s smile deepened.

“Right. You can’t. You won’t. If you rip out my tongue here and now, you’ll never get the answers you want.”

The Eastern Heaven Demon Lord already knew.

Unless they were in a desperate fight for their lives, they couldn’t kill him now, when the advantage was already theirs.

He knew a great deal about Dark Heaven and the Lord of Heaven. One word from the Eastern Heaven Demon Lord could change the course of a great war that would decide the future of the world.

A war that would put hundreds of thousands, perhaps millions, of lives at stake.

That was the last hope he clung to.

“Listen, Fire King.”

*Rumble. Rumble.*

Feeling the faint vibrations travel through the ground, growing stronger by the moment, the Eastern Heaven Demon Lord burst into hearty laughter.

“It seems Heaven hasn’t abandoned me after all.”

At that moment—

*CRAAASH!*

With a roar that shook the earth, thousands of soldiers poured through the outer wall, which had crumbled to pieces.

The Eastern Heaven Demon Lord laughed aloud.

No—he was about to laugh.

*Gooooooom.*

Until an enormous beam of light shot from somewhere, wrapped around them, and burst.

*KABOOM!*

Faced with that unbelievable power, the Eastern Heaven Demon Lord’s eyes flew wide.

At the same time, he screamed one person’s name.

“So Gyo…!”

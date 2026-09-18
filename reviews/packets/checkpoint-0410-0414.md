# Checkpoint Review — 410–414

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

# Chapters 410–414

## Plot

The Arch Lich’s Darkened fog strengthens the monsters around Suining City, but Jin Taekyung leads the suicide squad through repeated Magic Traps and the enemy’s elite rear forces. His One Annihilation destroys ten high-level Death Knights and Liches, countless elite monsters, and the Arch Lich’s observing Familiars. Jin gains four Levels, immense EXP and Fame, the Title One Against a Thousand, and the Intimidation stat, while the surviving monsters are terrified and the suicide squad charges through the breach.

Elsewhere, Wu Heixing and roughly three hundred Red Guard Gang Hunters suffer heavy losses against a Lich and two Death Knights. Lee Jungryong kills the Lich with one spear throw, Wu defeats one Death Knight, and Lee deliberately delays Ares Guild’s intervention so the Red Guard Gang will be weakened and can later be replaced by Ares as a source of influence. Jin confronts Wu over the casualties, but Lee prevents the dispute from becoming a fight.

Lee then reveals that approximately fifty thousand monsters remain in reserve only twenty kilometers away. Team Leader Choi realizes that the Arch Lich withheld this army because the coalition’s front-line forces were weaker than expected and S-rank Hunters could function as one-person armies. Prince Felix, Faye Chen, and Magic Johnson arrive through a dangerous teleport, followed by ten thousand Hunters from the Western and Eastern Fronts. With roughly five hundred suicide-squad members near the Arch Lich and the reinforcements approaching, Team Leader Choi declares victory, and Jin believes him.

## Continuity

- Jin Taekyung, Lee Jungryong, Wu Heixing, and roughly five hundred suicide-squad members are within twenty kilometers of the Arch Lich.
- The Arch Lich’s Darkened fog strengthens monsters within its range.
- Jin’s One Annihilation destroyed ten empowered elite undead, numerous monsters, and the Arch Lich’s Familiars, severing its Familiar Link and causing backlash.
- Jin now has the Title **One Against a Thousand** and the **Intimidation** stat. The Title improves his battlefield performance, reduces fatigue consumption, frightens enemies, and raises allied morale.
- The Arch Lich suspects Jin may be the ancient human Adversary who defeated it in the past.
- The Arch Lich has retained an estimated fifty thousand monsters as a reserve force.
- Lee Jungryong intends to let the Red Guard Gang collapse so Ares can replace it as a source of influence and opportunity.
- Wu Heixing and the Red Guard Gang suffered heavy losses; Wu defeated one Death Knight, while Lee killed the attacking Lich.
- Go Jun is stronger and more controlled than before and can suppress his killing intent under Jin’s provocation.
- Prince Felix, Faye Chen, and Magic Johnson have arrived through a dangerous teleport.
- Ten thousand Hunters from the Western and Eastern Fronts are advancing as reinforcements.
- Team Leader Choi believes the coalition can win, and Jin shares that belief.
- The Arch Lich’s remaining defenses and the coalition’s ability to break through the reserve army remain unresolved.

## Translation Decisions

- Render **어둠에 물든** as **Darkened**.
- Render **일섬** as **One Annihilation**.
- Render **일기당천** as **One Against a Thousand**.
- Render **위압** as **Intimidation**.
- Render **대적자** as **the Adversary**.
- Render **홍위방** as **Red Guard Gang**.
- Render **결사대** as **suicide squad**.
- Render **일인군단** as **one-person army**.
- Render **영웅의 혼** as **Hero’s Soul**.
- Render **아크 리치** as **Arch Lich**.
- Render **장유유서** as **Respect your elders**.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung, Lee Jungryong, Wu Heixing, and roughly five hundred suicide-squad members are twenty kilometers from the Arch Lich.",
    "The Arch Lich has an estimated fifty thousand monsters in reserve.",
    "Team Leader Choi believes the Arch Lich withheld its reserve because the front-line battle required fewer forces than expected.",
    "Go Jun has improved in strength and patience and can suppress his killing intent under provocation.",
    "Prince Felix, Faye Chen, and Magic Johnson have arrived through a dangerous teleport.",
    "Ten thousand Hunters from the Western and Eastern Fronts are advancing to reinforce the coalition.",
    "Team Leader Choi has declared that the coalition will win, and Jin Taekyung shares that belief."
  ],
  "continuity_sources": [
    414,
    413
  ],
  "open_questions": [
    "Can the combined forces break through the Arch Lich's fifty-thousand-monster reserve and reach it?",
    "What further defenses await the coalition beyond the Arch Lich's reserve army?"
  ],
  "safe_through": 414,
  "temporary_decisions": [
    "Render 아크 리치 as Arch Lich.",
    "Render 결사대 as suicide squad.",
    "Render 일인군단 as one-person army.",
    "Render 영웅의 혼 as Hero's Soul.",
    "Render 장유유서 as Respect your elders."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 410

# Chapter 410

*Has it been more than thirty years?*

Lee Jungryong muttered to himself.

The stench of countless monsters and the smell of blood drifted in on the wind. It was the scent of a battlefield, one that stirred up nostalgia for the past.

*Yes. It truly has been a long time.*

With a shrewd gaze that seemed at odds with his appearance, he watched the fog slowly draw nearer. The pale fog, where thousands of monsters were presumably lurking, radiated an ominous feeling simply by being there.

Most of the troops were shaken, but to Lee Jungryong—a living witness to the Great Cataclysm—it was an entirely familiar sight.

“How old are you?”

At Lee Jungryong’s sudden question, Go Jun, the head of his security team standing one step behind him, answered.

“Thirty-five.”

“That’s a good age. Looking back, I was the same. I had to survive one brush with death after another every day, but I had dreams back then.”

Lee Jungryong gazed into the empty air with deep eyes.

It was as if his younger self were passing somewhere in the distance—a young man carrying the will to survive and the ambition to become the best.

But more than thirty years later, the man standing here was an old man nearing seventy.

“Sometimes, doubt creeps in. Doubt that everything I’ve built might come crashing down.”

“I have not the slightest doubt.”

“Why not?”

Go Jun’s lips moved.

“Because you are here, Master.”

Lee Jungryong gave a quiet laugh.

“What would you do if I fell?”

“I can guarantee that will never happen.”

“There was a time when I thought of someone that way too. Someone stronger than anyone else, a wall I could never overcome even if I devoted my entire life to it.”

“……!”

“He was the beginning and the end of the Great Cataclysm. He was everything. He was humanity’s savior, no different from a new god. But he, too, was nothing more than a human being.”

The hero who had accomplished immortal feats had not shown himself for a long time, and only a handful of people knew the secrets surrounding him.

As one of those few, Lee Jungryong continued in a low voice.

“Nothing is eternal, and nothing is certain. I’ve been thinking that a lot lately.”

“……Is this because of Jin Taekyung?”

“When a crack begins, collapse comes in an instant. That bastard is the crack itself.”

“Then we must seal it before everything collapses.”

Lee Jungryong watched the fog slide across the desolate plain. A gentle voice with a hidden blade flowed from between his lips.

“Are you ready?”

“I am at your command.”

Go Jun bowed deeply and drew his sword.

*Shing! Clatter!*

Hundreds, then thousands, of weapons were drawn at the same time behind him.

They were the Ares Guild’s elites, forged through countless raids and training. The weapons held by them and by countless Chinese Hunters gleamed and rippled like waves.

“Please give the command.”

Lee Jungryong slowly began to walk.

There was no place here for soldiers or firearms. This was purely a battle between superhumans known as Hunters and monsters, and Lee Jungryong would reign as the god of the battlefield.

“Let’s go.”

With that single word, Lee Jungryong shot forward like the wind. The fog filling the plain split apart on both sides along the path of his sword.

*Kraaash!*

* * *

*Splurt!*

The young man drenched in green blood that reeked horribly barely managed to suppress his gagging.

No—that was not quite right. More accurately, he had not even been given time to gag.

*Whoosh! Boom!*

The upper section of his tower shield shattered, and a sharp fragment grazed the tip of his nose. Blood spurted out, and the scent of it pierced his nostrils.

The foul stench faded somewhat thanks to that, but an undead ogre that appeared to have died only recently was raising a massive iron club in front of him.

“Grrrraaaaah!”

*Whoooooosh.*

The terrifying sound of something tearing through the air was enough to make the hair on his head stand on end.

The young man gritted his teeth and bent his legs. He used the mana-infused tower shield to protect his head.

*Boom!*

A tremendous impact swept through his entire body. His head rang, and his arm hurt as if it had been broken.

*No. Maybe it’s already broken.*

But a broken arm was nowhere near important enough to count among his concerns.

Especially not when a five-meter-tall monster roaring ferociously was swinging an iron club as large as an adult man like a pinwheel.

*Boom! Boom! Boom!*

Under the monster’s insane assault, the young man let out a scream edged with tears.

“You turtle-dicked bastard! Why are you so strong?!”

The young man was a veteran B-rank Hunter, and of course, he had fought ogres before.

As befitted an A-rank monster, an ogre possessed tremendous strength and stamina, but they had never been this strong.

They definitely hadn’t been…

*Boom!*

The young man stared blankly as the high-strength tower shield he had bought for a fortune at the beginning of the year was smashed to pieces in only five blows.

*What the hell… Did all of these things take drugs together?*

They were far too strong. As he watched the iron club rise once more through the pale fog, the young man sensed his end.

At the same time, a name flashed through his mind.

*Jin Taekyung.*

This was all that bastard’s fault.

If Jin Taekyung had simply pretended not to know him and walked past that day, he would never have gotten his shins kicked by some big shot or been drafted as a frontline tank.

And he would not be about to die like this.

*Whoooooosh!*

He did not even dare think about dodging. He lacked the courage even to look straight at the iron club rushing toward him and filling his entire field of vision.

The young man squeezed his eyes shut and unconsciously let out a scream.

“Jin Taekyung, you bangzi bastard!”[^1]

[^1]: *Bangzi* is a derogatory Chinese term for a Korean. Jin twists the insult into a threat to make the Hunter run bread for him, echoing Korean school slang for a bullied errand-runner.

And then, the next moment—

*Slash! Rattle-rattle-rattle!*

His vision was dyed pitch-black. A cool breeze brushed across his entire body, and something poured down like a sudden shower.

Soon, a voice pierced his ears.

“What kind of bastard?”

“……Huh?”

The young man’s eyes flew open. Green blood was scattering through the air in droplets. The enormous body of the undead ogre, now missing its head, was slowly toppling over.

And there was the face of a man scowling deeply.

“……Huh?”

“You’re that bastard from last time. Burdian.”

*Whoosh! Splurt!*

He could not see it. He could not even follow it.

The man reached out, and a streak of light that seemed to be a dagger pierced through three or four monsters. They collapsed like puppets with their strings cut.

An answer escaped the young man’s lips before he could think.

“Uh, no, I’m not.”

“No, my ass. You fucking bastard.”

*Slash! Bang!*

“You looked like you were in danger, so I saved you, and you call me a bangzi? You’d better survive. I’ll make you run bread for me until you die of old age.”

*Slash! Sssshk!*

*Is this a dream?*

Every time the young man blinked, the monsters around him were falling like bundles of straw.

Blue flames erupted, and whenever the air split with a shriek, the space that had been packed so tightly there was nowhere to step was swept clean.

Everything began at a single man’s fingertips, and none of it looked like something a human being could have done.

The young man stared at him blankly and asked,

“Are you… perhaps a god?”

After a moment of silence, the man—Jin Taekyung—asked in return.

“Are you perhaps… a fucking idiot?”

*Graaaaaaak!*

Blue flames swept across the earth. Steel melted, and monsters caught in the blaze screamed in agony.

After wiping out dozens of monsters with a single swing, Jin Taekyung glanced at the young man.

“Hey.”

“Yes? Yes?”

“Survive. I’m going to make you run bread for me.”

“Excuse me?”

“I’m not joking. If you die, I’ll kill you myself.”

“……!”

“Oh, and this.”

*Whoosh! Crack!*

Something flew toward the young man like a ray of light and struck him in the forehead, shattering.

Before he could react, the young man was drenched in translucent liquid, and a quiet voice reached his ears.

“You’ll be fine now, so get back to fighting. Don’t go picking fights with ogres for no reason. Stick to the weaker ones. Got it?”

*Hissss.*

The liquid—no, the potion—seeped into him with a faint warmth.

The young man felt the wounds covering his entire body and his broken arm begin to heal. He nodded blankly.

“Yes, yes.”

“Then I’m off.”

“P-Please be careful, sir.”

Forgetting that he was in the middle of a battlefield, the young man bowed deeply at the waist.

When he raised his head again, Jin Taekyung was gone, and a group was rushing past him.

*Whoosh-whoosh-whoosh! Slash!*

More than two hundred Hunters raced forward without hesitation along the path Jin Taekyung had opened, swinging their weapons.

Two people at the very front stood out above all the rest.

“&*^%!”

“The formation has collapsed! Charge!”

A handsome man spouting incomprehensible Korean and a Hunter who looked especially young.

The two moved like the wind, and their sword blades, wrapped in dazzling aura, cut the monsters apart.

*The suicide squad.*

He had heard the story. Some of the S-rank Hunters, including Jin Taekyung, would lead the suicide squads on each front in a charge against the Arch Lich.

Only yesterday, he had thought it was impossible nonsense…

*Amazing.*

*Could I become like that too?*

As the young man gazed blankly at the scene, his chest suddenly grew hot. Some unknown strength surged up from within him, and he could not contain it.

He raised his half-destroyed tower shield and charged toward the nearest monster.

“Yaaaaaaaah!”

“Grrrraaaaah!”

*Whoosh! Boom!*

“……”

Damn it. It was an ogre.

The young man stared at his completely destroyed tower shield, then immediately turned and ran.

*Orcs. Where are the orcs?!*

* * *

*Thud!*

*It’s over.*

The sensation traveling through the end of my fist was exactly right. With that certainty flashing through my mind, the head of the Lycanthrope snapping its teeth toward the back of my neck exploded.

> **System**
> *Ding!*
> - You defeated Lv. 92 Darkened Lycanthrope!
> - You gained a small amount of EXP!

A Lycanthrope at level 90-something?

I already knew that Level was not an absolute measure, but the monsters gathered on this battlefield were definitely different from the ones I had seen in Gates.

*They’re stronger.*

Their Levels were somewhat higher, and their Agility and strength were superior too.

If it had been one or two monsters, I might have brushed it off. But everything from F-rank goblins to A-rank monsters was like this. You would have to be an idiot not to find it strange.

“Mr. Jin Taekyung!”

“Hyung!”

I turned at the urgent voices coming from behind me and saw monsters filling the path I had opened without leaving a single gap.

The suicide squad was fighting desperately against them.

“Get the hell out of here—all of you.”

*Boom-boom-boom-boom!*

For the monsters, I was an existence they could neither block nor evade.

Dozens of fist shadows shot out like cannonballs and rained down over their heads.

Some were sent flying into the distance as bloody pulp. Others simply collapsed where they stood.

I charged into the space that had momentarily been emptied.

*Slash-slash-slash!*

A spearhead imbued with Force cut through bone and flesh, hacking in every direction. As the monsters fell, System notifications rang out without pause.

> **System**
> *Ding! Ding! Ding!*
> - You defeated Lv. 55 Darkened Orc Warrior!
> - You gained an extremely small amount of EXP!
> - You defeated Lv. 83 Darkened Lizard Mage!
> - You gained an extremely small amount of EXP…

Then came the cheerful chime I had not heard in a long time.

> **System**
> *Ding!*
> - **Level Up!**
> - The effects of leveling up relieve fatigue and heal some injuries!
> - You obtained 10 points!
> - Your physical condition is at its peak!

I could feel it. The internal energy that had been slowly draining away was filling to the brim, and the fatigue accumulated in my body was vanishing as if it had been washed away.

But there was something more important.

“Team Leader Choi! Shao Shen!”

“Yes!”

“Give us your orders!”

I shouted in a voice loud enough to shake the entire battlefield.

“Fog! Get as far outside the fog’s range as possible!”

This was not merely unpleasant, damp fog. It was a kind of magic wielded by the Arch Lich.

Magic that strengthened the monsters within its range—or rather, made them *Darkened*.

*Damn magic.*

At that very moment, as I glared at the mysterious fog filling the area around me—

*Kraaaa-boom!*

A thunderous roar that made it seem as if the sky had split apart echoed across heaven and earth.
## Chapter artifact 411

# Chapter 411

For a moment, it felt as though the world had stopped.

My instincts reacted before my brain could process the situation.

The breathing of the people around me and the monsters’ howls receded into the distance, as if they were coming from several kilometers away. My senses, sharper than ever, took in every detail around me.

*Fwoooosh.*

Droplets of blood, dirt, and dust drifted slowly through the air. Fog hung close enough to grasp if I reached out my hand.

And then…

*Qi.*

I could feel it—the immense movement of qi surrounding an area several hundred meters in every direction. As a red alarm began blaring in my head, I kicked off the ground and shot upward.

“Get clear—!”

*Kraaa-boooom!*

A flash of light was followed by a tremendous roar that shook heaven and earth. From more than ten meters in the air, I looked down over the battlefield.

The area within a radius of several hundred meters, centered on the spot where I had been standing only a few seconds earlier, had been devastated.

Through the fog that had not yet dissipated and the clouds of dust rising from the ground, I could see green blood covering the earth and monster corpses blown to pieces.

*A Magic Trap.*

Fighting an enemy who refused to show itself meant preparing for every situation that could possibly occur.

*There’s no compassion in war.*

The countless wars recorded throughout human history were witness, prosecutor, and judge.

Even humans committed all kinds of horrific atrocities against one another during war. Expecting compassion from monsters that were not even human was laughable.

That was why vigilance was an essential virtue in war. It reduced the chances of falling into an enemy’s trap and minimized casualties.

Just like now.

*Tap.*

I landed lightly and reached out my hand.

*Bang!*

Compressed air burst outward, scattering the clouds of dust.

Among the blood and corpses filling every direction, familiar faces finally emerged.

“Team Leader Choi.”

Team Leader Choi took a deep breath and nodded. Behind him stood more than two hundred members of the suicide squad, their faces pale with terror.

“A few people are injured…but everyone’s safe.”

“That’s a relief.”

“It was an unbelievably powerful trap. Without this, most of us—including me—would probably have died.”

*Shk. Wooooong.*

Team Leader Choi reached out and touched the transparent barrier spread out before him.

It covered every member of the suicide squad, and it was a Barrier spell painstakingly engraved into a scroll by one of the top three mages among the billions of people in the world.

“When the battle is over, I should find Mr. Johnson first. His magic saved our lives.”

“Are you planning to give him a kiss as thanks?”

“If you’re asking what I feel like doing right now, there’s nothing I wouldn’t do.”

Shao Shen exhaled the breath he had been holding and joined in.

“I’m capable of more than that. This is truly…”

He could not finish and simply looked around.

The explosion had been that tremendous. In its aftermath, more than a thousand monsters had been killed or rendered incapable of fighting.

A trap that had not distinguished friend from foe. The Arch Lich had thrown countless subordinates into it as kindling to catch me and the suicide squad.

*Look at this bastard…*

I had expected as much to some extent, but the Arch Lich’s cunning and boldness went beyond anything I had imagined.

If my signal had been even slightly late, or if I had not volunteered to be bait while breaking through the path ahead, every member of the suicide squad would have been buried here.

*Just like that day.*

A memory I could never forget. A tragedy like that could never happen again.

I turned and spoke.

“Keep your distance and follow me. Our objective isn’t to fight the monsters. It’s to break through them.”

The suicide squad answered with a thunderous shout.

The monster army, confused after suddenly losing a large number of its forces in the explosion, hesitated and began to retreat.

This was the moment when a crisis became an opportunity. We could not let the momentum slip away.

“Charge!”

With an azure dragon’s roar charged with internal energy, I shot forward.

*Slash!*

The head of a retreating monster flew into the air.

The two hundred members of the suicide squad drove into the gap in the monster army like an awl. The main force in the rear followed behind them, surging forward like a wave.

“Waaaaaaaaah!”

A deafening roar shook the battlefield.

Green blood spread through the fog.

And high above, a flock of crows circled as they looked down upon the battlefield.

* * *

The being sitting atop a throne made of white bones, as if asleep, suddenly opened its eyes.

Intense light flared from the pupils of its empty skull, and a low mutter escaped its mouth.

“Not bad.”

The Arch Lich had hundreds of eyes and ears.

Even now, the Familiars placed throughout the battlefield were taking in every detail without missing a thing.

Humans and monsters locked in fierce close combat.

And the group of humans rapidly breaking through the battlefield.

*The suicide squad. That was what they called them, wasn’t it?*

The Arch Lich suddenly recalled something.

It was an old, stale memory—one it had been unable to forget despite spending an eternity submerged in the River of Death. No. One it could not forget.

*The Adversary.*

How could it forget?

A single human who had stood at the center of everything. The human suicide squad that had charged alongside the Adversary, risking death.

*That bastard was the one who drove a sword into my body.*

The Arch Lich looked down at its body, formed from pitch-black bones.

In the past, it had not been some lowly existence like an undead. It had been a noble and mighty being, trusted by a king and commanding countless monsters.

But on the day of the final battle, it had fallen alongside its king.

At the hands of a mere human, no less.

“But…where is the Adversary?”

The Arch Lich’s voice was filled with doubt.

It had surveyed every front through its Familiars, yet the Adversary, who should have appeared, was nowhere to be seen. It had found several humans from its memories, but that was all.

*Could it be?*

The Arch Lich’s eyes flared violently as it realized something.

It was impossible to believe.

But what if—what if the Adversary had died?

What if the Adversary had met the fate of a mortal?

“Kha…khahahaha!”

The body that had been rigid as a statue began to shake.

The laughter, infused with magic, made the ground tremble and the air quiver.

Realizing that something had changed in their master’s mood, the guards dropped to the ground and prostrated themselves.

“My lord.”

“Why do you laugh so?”

The honor guard was an impressive group. There were Death Knights, each comparable to a Named Monster, as well as Liches with their robes pulled deeply over their heads. Their total number came to twenty.

They were creations made to fight the Adversary.

But now, the Arch Lich’s thoughts had changed.

After laughing with delight, the Arch Lich finally spoke.

“Listen, my faithful servants.”

“Give us your command.”

The Arch Lich rose from its seat and looked down upon its loyal retainers. A chilling voice soon echoed through the space.

“Go to the battlefield. Trample those insignificant humans and wipe them out.”

The twenty Death Knights and Liches bowed without the slightest hesitation.

The Arch Lich was the lord of every undead present. When it came to obeying its commands, there was no room for even the smallest doubt.

“We shall carry out our lord’s command.”

They answered in unison and set off in their respective directions.

The space was empty once more.

The Arch Lich, laughing alone, sat down on the skeletal throne and focused its mind.

As it watched the battlefield through the eyes and ears of countless Familiars, it suddenly stopped.

“But…what in the world is that human?”

In the pitch-black eyes of a crow soaring through the sky, the image of a young human cutting through monsters amid a spray of blood was reflected.

It was a face that did not exist in the memories of the past.

But it was also a face the Arch Lich had seen through its Familiars several days earlier.

“That’s the human who defeated the Death Knight Lord.”

The Death Knight Lord, created from Lei Fei, was the Arch Lich’s finest masterpiece among everything it had ever brought into existence.

Although it had been unable to subjugate him completely because of his powerful soul, there could be no doubt about his strength. The Arch Lich had directly bestowed a portion of its own power upon him.

And yet, because of that insignificant human, it had lost its greatest asset and wasted precious mana.

“He’s irritating. I should deal with him properly while I have the chance.”

Having decided to eliminate him, the Arch Lich sent out a thought.

Half of the guards heading toward the various fronts changed direction in accordance with their master’s command.

* * *

*Kra-d-d-d-d-k!*

Wind, weapons, and the bodies of monsters harder than stone.

Everything caught in the path of the spearhead was cut apart.

Heads flew into the air, and thick limbs spun through the sky.

A Troll that was still breathing was chopped to pieces before it had a chance to regenerate. An ogre that had become undead while still half-rotten staggered, only for a sword that came flying a moment later to take off its upper body.

*Slash! Slash! Slash!*

After cutting down three or four monsters in an instant with Hero’s Soul, Team Leader Choi shouted toward me.

“Mr. Jin Taekyung! The monster assault is too strong!”

He was right. Once we broke through the front line, the number of monsters decreased, but the quality of the forces grew even higher.

*I knew it would be like this.*

The monsters in front, used as kindling for the Magic Trap meant to catch us, had mostly been mid- or low-level.

The Arch Lich had placed its elites in the rear and used the other monsters as both bait and meat shields.

*To wear down our strength.*

On top of that, the fog had grown even thicker than before, making the battle more difficult.

The monsters becoming stronger under the fog’s influence was bad enough, but in fog this thick, visibility was limited and sound did not carry well.

It was an unavoidable advantage for monsters, whose senses were superior to those of humans.

Of course…

*I’m the exception.*

*Whoooosh! Bang!*

My spear lashed out with all my strength, skewering six or seven monsters like meat on a skewer.

Shao Shen and the Hunters in the suicide squad, having escaped the crisis, gave me grateful looks.

“Everyone, group up around me!”

“But we only have a few magic scrolls left. If another Magic Trap is activated…”

“No time to explain! Stop talking and move!”

Team Leader Choi and Shao Shen nodded at my shout and advanced with the suicide squad.

I knew what they were thinking, but we had already made it through three Magic Traps, and this was the rear where the Arch Lich had gathered its elites. The chances of another trap being activated were slim.

“Focus on defense instead of attacking. Advance!”

The battle itself had become more difficult, but the reduced chance of suddenly being caught in another trap left me feeling lighter.

Pulling myself out of danger would not be difficult. But the lives of the other members of the suicide squad were at risk.

*We’re right next to our final destination. Minimize casualties and join up with Lee Jungryong and Wu Heixing.*

*Slash! Kra-d-d-d-d-k!*

I was at the front, cutting a path through the monsters, when I suddenly felt the fatigue building in my body.

“Everyone. Fall. Back!”

“Human. By my lord’s command, I shall take my own life.”

The curtain of monsters split apart to the left and right like the parting of the Red Sea.

I stared blankly, my mouth hanging open, as the beings behind it revealed themselves.

> **System**
> - **Lv. 120 Darkened Lich**
> - **Lv. 115 Darkened Death Knight**

There were ten of them, all hovering around Level 120.

For a moment, I could barely breathe, and my hands and feet began to tremble.

Team Leader Choi shouted at me in a voice filled with despair.

“We have to retreat right now!”

“T-Team Leader Choi.”

“Get a grip, Mr. Jin Taekyung!”

“The lunchbox delivery is here.”

“If we keep going like this, we’ll be wiped out…huh?”

With trembling eyes, I stared at the ten monsters.

No—the ten lunchboxes.

“The lunchbox delivery is here.”

“…?”

“…?”

“…?”

Put those question marks away, you bastards.

*One Annihilation, coming up.*
## Chapter artifact 412

# Chapter 412

*Fwoooosh.*

A crow landed on an ancient tree in the middle of the battlefield, its eyes flashing brightly.

The Arch Lich had perched its Familiar in a spot with an excellent view, and it watched the situation with considerable pleasure.

*What will you do, human?*

One person was reflected in the crow’s endlessly gleaming black eyes.

An open mouth. Hands trembling slightly.

Looking at Jin Taekyung like that, the Arch Lich suddenly found itself wondering.

*Was the Death Knight Lord really defeated by a human this cowardly?*

The Death Knight Lord may have had a few flaws, but it was undoubtedly an undying masterpiece.

The Arch Lich had been unable to resist coveting Lei Fei, an excellent material with a noble spirit and formidable martial power.

That was why it had personally granted him a portion of the mana that could be called its own source. Thanks to that, Lei Fei had become an existence that surpassed the limits of an ordinary Death Knight.

There was no way such a Death Knight Lord could have been defeated by some mere coward.

*What exactly happened?*

That day, the Arch Lich had not watched the battle between Jin Taekyung and Lei Fei to the end. No—it had not thought there was any need to watch.

By the time that young human arrived, the human army had already been wiped out. To the Arch Lich, the situation on another front was more important than watching an obvious conclusion unfold.

By the time it belatedly noticed the destruction of its precious retainer and sent a Familiar, everything was already over.

All the Arch Lich had been able to see was Jin Taekyung, now accompanied by several thousand humans who had appeared out of nowhere—and the monster army, annihilated without a single survivor.

*That human clearly couldn’t have done it alone. Was it simply a matter of luck?*

But that luck ended here.

As many as ten Death Knights and Liches possessed the strength of an entire legion, if not more.

*And unlike last time, there aren’t any suitable people around to help him.*

There was only one path left for that human now.

He would helplessly watch his companions die before falling himself.

That was the only possible ending—and the punishment the Arch Lich had chosen for him.

*Cawww!*

The crow, taking on its master’s mood, let out an unpleasant cry.

Step. Step.

That was the exact moment when the human who had been fearlessly approaching its retainers stopped walking.

Then he raised a trembling hand toward the Death Knights and Liches radiating immense mana.

*Is he planning to surrender?*

The Arch Lich had thought he was merely a cowardly human. It had not expected him to be this stupid as well.

If he thought surrendering would convince the Arch Lich to spare him, he was making a terrible mistake—

“One, two, three, four…”

—…?

The Arch Lich was flustered for the first time in a very long while.

First, because fluent Demon Realm language had flowed from Jin Taekyung’s mouth.

Second, because it could not understand what he was doing.

*What in the world is he up to?*

It did not have to wonder for long.

“…Nine, ten.”

As soon as he finished speaking, a droplet of saliva fell from Jin Taekyung’s chin with a soft *plop*.

He wiped his mouth with his sleeve, a satisfied smile spreading across his face.

“Plating is an art, seriously. I hereby award it three Jin-shelin stars.”

—?

—?

The Arch Lich and its loyal retainers had no idea what the words *plating* or *Jin-shelin* meant.

But they understood the meaning of Jin Taekyung’s next action.

*Gooooooong.*

At a speed too fast for the eye to follow, a terrifying force gathered along the spearhead, which had already been drawn far back.

At that sight, the Arch Lich felt a shock as though its cold, hardened heart had dropped into its stomach.

A bone-deep chill ran through it, and a thought burst forth.

“Dodge—!”

But the spear shot forward faster than the thought could be conveyed.

*Woooooong!*

The wind tore apart.

*Kraaaaaaaaaash!*

Space split open.

Within time that had been divided and divided again into a single instant, a massive vortex filled with blue flames swallowed everything.

Countless monsters. Death Knights and Liches.

Even the flock of crows perched on an ancient tree not far away, watching everything unfold.

*Fwoooooosh!*

A blinding flash covered everyone’s vision.

* * *

*Whoooooosh.*

A wind that had come from somewhere seeped through my entire body.

It was a wind only I could feel—and a new power that had come to me.

*Yes. This is it.*

I smiled as I looked at the empty space visible beyond the slowly fading light.

It was the exact place where the Death Knights, Liches, and countless other monsters had been standing.

Everything there had been cleanly erased, and the area was filled with System notifications.

*Ding. Ding. Ding…*

> **System**
> - You defeated **Lv. 115 Darkened Death Knight**!
> - You defeated **Lv. 120 Darkened Lich**!
> - You defeated **Lv. 122 Darkened Death Knight**!
> - …
> - You have defeated too many monsters!
> - You have gained a massive amount of EXP and Fame!
> - Level Up!
> - Level Up!
> - Level Up!
> - You have accomplished an exceptional feat!
> - As a Reward for your achievement, you have obtained the Title **One Against a Thousand**!
> - Due to the effect of the Title **One Against a Thousand**, all Stats rise by a set amount when facing multiple enemies, and fatigue consumption is greatly reduced! During battle, enemies will be intimidated, while allies’ morale rises dramatically!
> - Because you have accomplished an exceptional feat, a massive amount of EXP and additional Rewards will be granted!
> - Level Up!
> - A new stat, **Intimidation**, has been created!
> - Due to the effect of the Title **One Against a Thousand**, **Intimidation** has increased significantly!
> - Enemies who face you will feel fear and terror!

I closed my eyes and savored the afterglow given to me by the System.

A feast of System notifications ringing without pause.

So this was what the bells of heaven sounded like.

Four Level Ups that completely washed away the fatigue of One Annihilation. A Title capable of displaying exceptional effects on a large-scale battlefield like this one. And on top of that, a new stat called Intimidation.

*It’s thrilling. It’s always fresh. The System is the best.*

If every day could be like this, I felt I could die without regrets.

“Is that true? Oh, ohhh…!”

That fucking bastard.

The Skeleton Warlord’s mood-killing words made me open my eyes. The first thing I saw was a large number of humans and monsters frozen like statues.

“…Mr. Jin Taekyung.”

「H-Hyung.」

Team Leader Choi and Shao Shen stared at me with dazed expressions.

No, it was not only those two.

All two hundred or so members of the suicide squad were the same.

There was unmistakable awe in their eyes and voices as they looked at me.

「Good heavens.」

「W-What in the world just happened?」

「There were ten Death Knights and Liches. Right there! I saw them with my own eyes!」

Yeah. They had been there.

But now they were gone.

“Goddamn! Holy shit! What the fuck is this? Fucking! Fucking kimchi! Jesus kimchi!”

“Eeeh, eeeeeh? Nani? Naiii?!”

“…”

Some of the Hunters had been dispatched by mercenary companies or the UN, so their reactions varied greatly depending on their nationality.

I turned toward Team Leader Choi, who still could not seem to form a sentence.

“Why are you so surprised? It’s not like this is your first time seeing it.”

“Was that what you used last time, when you defeated the Black Drake…?”

“That’s right.”

Team Leader Choi had seen One Annihilation once or twice before, and he swallowed hard.

“…I remember it not having this kind of power.”

“I was holding back then.”

That was an obvious lie.

In truth, even I was so stunned by what I had done that I had no idea what to say.

The first and last time I had used One Annihilation after reaching the Supreme Peak realm was during my battle with the Western Heaven Demon Lord. Since my fatigue had been at its limit, I had lost consciousness immediately afterward.

*I didn’t know it would be this powerful either.*

There had been ten Death Knights and Liches, each one close to Named level.

I had considered it a success if I managed to kill six or seven of them.

After all, monsters at Level 100 or above gave a considerable amount of EXP. With all the other small fry thrown in, there would be enough to level up, so I’d figured there was no way I’d collapse from exhaustion and make a spectacle of myself.

*…But this is more than I expected.*

A double-edged sword.

No—a double-edged spear.

But it was undeniably one hell of a powerful strike.

It had blown away not only the hundreds of elite monsters packed tightly together, but also the Death Knights and Liches.

Thanks to that, a massive gap had opened in the monster army surrounding me and the suicide squad. The monsters themselves also appeared to be in confusion.

*I’d be an idiot to let this opportunity pass.*

Without hesitation, I raised my spear.

The unexpected situation had temporarily halted the battle on both sides. But if the monster army recovered and the suicide squad, already suffering from an overwhelming numerical disadvantage, was surrounded again, I could make no guarantees.

“What are you waiting for, you bastards?”

“Huh?”

“What?”

“Eeeeeh?”

I shouted at the people who had been jolted back to their senses by my cry charged with internal energy.

There was no time for honorifics or anything else.

Right now, there was only one thing to think about.

“Wipe out everything in your path!”

“……!”

*Ding.*

> **System**
> - Due to the effect of the Title **One Against a Thousand**, the morale of your allies has risen dramatically! Those who follow your command will possess strong cohesion and display even greater performance!
> - Due to the effect of the Title **One Against a Thousand**, the enemy has become greatly intimidated!
> - Due to the Title **One Against a Thousand**, the effect of **Intimidation** has increased!
> - Under the influence of **Intimidation**, the enemy feels fear and takes a step backward!

The System messages described exactly what was happening.

The monsters still alive after witnessing the divine might I had displayed slowly retreated. Even the undead monsters, which had already lost their minds, were intimidated and flinched.

But what about us?

“Charge!”

*Whoosh! Kra-d-d-d-d-k!*

With a thunderous shout, I leaped into the gap created by One Annihilation and swung my spear in every direction.

The roughly two hundred members of the suicide squad surged forward as one, letting out a roar loud enough to make my ears ring.

「Waaaaaaaaah!」

「Follow Mr. Jin! Wipe them all out!」

“Fucking! Fucking Jin Genghis Khan! Jesus Kimchiman!”

“Eeeeeeeh?!”

*Splat! Shraaaaaak!*

Green blood sprayed through the air, and undead bones shattered into countless pieces.

*Slash!*

I cleanly split the upper body of a Troll trying to turn its back and flee.

The Skeleton Warlord shouted at me in an enraged voice.

“Wicked human! Over there! Kill that one!”

“What? Who?”

“Kill that strange human who keeps going ‘eeeeeeh’!”

“…”

“Or I’ll kill him myself! If he does it one more time, I swear I’ll kill him!”

“Yeah, okay.”

I had been hearing it too, and it was starting to piss me off.

* * *

“Ghk!”

The Arch Lich let out a strangled groan.

As if the Link with its Familiar being forcibly severed were not enough, all ten of its guards had vanished in an instant.

Unlike ordinary monsters, they were retainers empowered by the Arch Lich itself.

The Arch Lich could not avoid taking damage.

“This is insane. How can a mere human…”

After gathering its disrupted mana, the Arch Lich stopped short, unable to continue.

*A mere human?*

That was wrong.

Humans were certainly insignificant beings, but they could never be underestimated.

The Arch Lich already had a painful history to prove it.

*Could that guy…?*

At the ominous possibility that suddenly flashed through its mind, the light in the Arch Lich’s eyes burned fiercely.
## Chapter artifact 413

# Chapter 413

*Fwoooosh! Kraaaash!*

A massive greatsword smashed into the ground. Wu Heixing’s body shot upward like lightning, having dodged the attack by the exact distance of half a span.

*Thud!*

The blade that had driven up beneath the ogre’s jaw jutted out above the crown of its head.

A precise, no-frills strike.

Wu Heixing pulled out his sword, stepped on the shoulder of the falling ogre, and dropped among the monsters.

The sword in his hand traced countless lines through the air.

*The Twelve Blood Net Sword.*

Some people had condemned the Cultural Revolution that lasted from 1966 to 1976 as an atrocity that outraged both heaven and humanity. To someone else, however, it had been the opportunity of a lifetime.

Wu Heixing’s grandfather, a longtime political companion of Mao Zedong, had risen spectacularly and embezzled an astronomical fortune. Using his son—a member of the Red Guards—as a stepping stone, he had smuggled away all kinds of cultural artifacts and ancient books.[^1]

The Twelve Blood Net Sword Wu Heixing had learned was one of the countless ancient books his grandfather had acquired at the time.

*Shreeeeek!*

Twelve strands of a net spread out, covering more than ten meters in every direction.

The net of red aura sliced through skin and flesh, cutting bones apart. Dozens of high-tier monsters were shredded and collapsed.

It was truly the prowess of an S-rank Hunter.

Thoroughly emboldened, Wu Heixing shouted.

“Red Guard Gang! What are you doing? Sweep them all away, you bastards!”

“Yes, sir!”

A shout infused with powerful mana shook the battlefield.

The roughly three hundred elite Hunters of the Red Guard Gang, which Wu Heixing’s family had personally founded and raised as a private army, charged into every opening without hesitation.

*Shreeeek! Splurt!*

*Whoosh! Slash!*

—Krrk, khrrrk!

“Aaaaargh!”

The screams of humans and monsters mingled with splashing blood from every direction.

The Red Guard Gang’s Hunters, whom Wu Heixing had kept in reserve until the very end, were unquestionably strong. But their enemies were high-tier monsters as well.

The elite monsters positioned in the rear darted through the thick fog as they fought the Hunters. Regardless of the difference in level, the monsters outnumbered them three or four to one.

And yet…

“You filthy, stinking bastards dare!”

*Stab-stab-stab!*

The existence of an S-rank Hunter named Wu Heixing was enough to turn the unfavorable situation around.

He might have been widely criticized for his debauched behavior and personality, but he was still a genius who had grown up in the best possible environment.

Besides, unlike when he had first been deployed to the front lines, Wu Heixing had become more experienced. After passing through battlefields where death ran rampant, his skills had advanced by another step.

*I can do this! I’m Wu Heixing!*

Feeling exhilaration surge from the depths of his chest, Wu Heixing swung his sword without pause.

His opponents were a monster army numbering in the tens of thousands. He had been afraid at first, but somehow he had made it this far.

Whenever he suffered even a minor injury or began to tire, he gulped down expensive potions like water. He also used the Red Guard Gang’s Hunters as shields when he needed to pull back.

And now, there was no monster capable of blocking his red aura blade.

*I’ll make sure no one can ever look down on me again. Lei Fei. That fucking bangzi bastard. No one!*

That was the moment Wu Heixing ground his teeth at the humiliating memory.

*Fwoooooosh! Boom!*

A spear flew in at blinding speed, skewering three or four Hunters like meat on a skewer before burying itself deep in the ground.

A three-meter-long lance—something rarely seen on a battlefield like this.

Wu Heixing hurriedly turned his head to identify the enemy, then his eyes flew wide.

“Death Knight!”

*Thud-thud-thud-thud!*

The figure riding a skeletal horse and cutting across the battlefield was unmistakably a Death Knight.

And there were two of them, not one.

The other Death Knight that had just appeared raised its lance from horseback.

“Everyone, watch—!”

*Fwoooooosh! Boom!*

Before he could finish his warning, the second lance tore through the air and pierced six or seven Hunters clustered together.

It was a strike that even the finest armor could not stop. Arms and legs flew through the air, while bodies that had lost their upper halves collapsed with a thud.

The sudden appearance of the Death Knights.

Then, as the Red Guard Gang’s Hunters froze at the horrifying sight unfolding before their eyes—

—D-a-r-k. V-i-n-e!

A gloomy voice, scraping like metal, rang out. At the same time, the changes began.

*Crack! Kra-d-d-d-d-k!*

The solid ground split apart like a spiderweb, and black vines surged up through the cracks.

Filled with magical power, they moved like living creatures. Some seized human arms and legs, while others wormed through gaps left exposed by armor and pierced their victims.

*Shrrrrk! Stab-stab!*

“Kyaaaaargh!”

“Black magic! It’s black magic!”

“Don’t panic! Cut the vines! Get out of the area now!”

Screams and shouts rang out everywhere.

*Crack.*

Wu Heixing bit down hard on his lip as he tore up the black vines winding around his body and flung them away like roots.

It was not because his Hunters were dying.

He understood what this entire series of events meant.

“Lich…!”

Wu Heixing’s guess was correct.

High above their heads, a death mage riding atop the head of a giant Wyvern that prowled through the gray sky raised a staff made of skulls and bones and pointed it at the ground.

—C-o-n-f-u-s-i-n-g!

*Whoooooosh!*

With the eerie cry, magical power poured down like dark storm clouds and swallowed the entire area.

The Hunters struggling to escape the black vines suddenly writhed as hallucinations and phantom voices seized them. They became easy prey for the monsters lurking around them.

—Sssssss!

—Gwoooooar!

*Smash! Kra-d-d-d-d-k!*

“Krrk, khk!”

“P-Please, save me!”

“Mother! You can’t die, Mother!”

Some fell with a final scream.

Others continued to howl even as they died, unable to escape the hallucinations and phantom voices.

But there were also those who broke free of the spell through sheer mental strength.

“You have to go!”

“Young Master!”

Despite the shouts of the A-rank Hunters surrounding him, Wu Heixing’s face had gone as pale as a sheet of paper.

Only one question circled through his mind.

*What—what the hell am I supposed to do?*

The Lich was in the sky, while two Death Knights were rapidly approaching from the ground.

Could they retreat?

If they did, where would they go, and how?

Wu Heixing might have been able to face the two Death Knights alone, but what about the Lich’s magic and the countless monsters surrounding the area so tightly that not even water could pass through?

No matter how much he thought about it, he could not find an answer.

*This…this fucking situation…*

*Crack.*

Wu Heixing was grinding his teeth hard enough to break them when—

*Fwoooosh! Bang!*

Along with the sharp crack of compressed air bursting apart, a streak of light shot up from the distant ground and sliced through the sky.

The next moment, the massive body of the Wyvern began to fall, robbed of its head.

“This…”

Wu Heixing muttered the word like a groan.

Everyone forgot the situation around them and looked up at the sky.

Before their eyes, the Wyvern’s body plummeted faster and faster, while a heap of black bones—the being that had once been called a Lich—tumbled down after it.

“…This is impossible.”

The Lich was dead.

And it had died in a single strike.

Someone had pierced through dozens of layers of defensive magic and accurately intercepted a target in midair?

Even an S-rank Hunter could not easily guarantee such a feat.

Wu Heixing had never seen an attack so fast or so powerful.

But to someone else, it was as natural as breathing.

The man who had been quietly watching what he had done from a short distance away suddenly opened his mouth.

“It has been a long time since I threw a spear. I’m definitely not as good as I used to be.”

The man standing behind him like an iron tower answered in a stiff tone.

“You were magnificent.”

“Hmm. No, I wasn’t. I seem to have gotten rusty. I suppose it’s proof that I’ve grown older.”

“How could that be?”

At the Head of Security’s usual flat voice, the man—Lee Jungryong—smiled gently.

“I saw Death Knights.”

Go Jun silently nodded.

“Yes. Two of them in total.”

“Do you think Wu Heixing can stop them?”

“If you mean the Death Knights, he should be able to defeat them without much difficulty.”

Go Jun added in a low voice.

“If there were no monsters around them.”

“So you mean it would be difficult under the current circumstances.”

“The black magic’s influence has disappeared, but the Hunters have already suffered considerable losses, while the monsters are far too numerous.”

“Then they’ll have to struggle with all they’ve got.”

“It will be a fierce and difficult battle.”

“Oh my. Then I suppose we should help them.”

“Would it not be better to watch a little longer?”

Lee Jungryong deliberately widened his eyes.

“Why?”

Go Jun had been taught by Lee Jungryong since childhood. He knew that every one of these moments was a test from his Master.

He also knew what answer he was supposed to give.

“Would they not be more grateful if we helped them when the situation was more precarious?”

Only then, after hearing his Disciple’s answer, did the Master smile in satisfaction. His manner of speaking changed as well.

“Yes. Exactly.”

“The Red Guard Gang has been a nuisance for some time.”

“They’re amusing fellows. They shout about the people and communism, then form a private army out of Hunters behind the scenes.”

“But the Crown Prince Party, which supports the Red Guard Gang, is friendly toward us.”

“That is why the Red Guard Gang must disappear. They have always sat beneath a tree’s shade to avoid the sunlight. Now that the tree has been uprooted, what else can they do?”

“Find another tree or buy a parasol.”

“We will become their new tree. If that happens, even more opportunities will open up.”

Go Jun nodded, then suddenly spoke.

“May I ask one more thing?”

“Go ahead.”

“The reason you had Wu Heixing participate in this operation… Is it related to Jin Taekyung?”

It was a question Go Jun had continued to harbor.

Even if Wu Heixing was an S-rank Hunter, why bring along an idiot like him?

*That man is immensely powerful. Even if Master is using Wu Heixing, what use could he possibly be?*

Sometimes, this happened.

Just when Go Jun thought he had grown accustomed to his Master’s thoughts and actions, he would find himself unable to understand Lee Jungryong’s true intentions.

And whenever that happened, Lee Jungryong would always wear an inscrutable smile.

Just like now.

“Team Leader Seok.”

His tone and the atmosphere both changed.

Returning to his position as the Head of Security for Ares Guild, Go Jun bowed deeply.

“Yes, Vice Guild Master.”

“It seems the time has come for you to step in. What do you think?”

Go Jun raised his head and looked past Lee Jungryong’s shoulder at the fierce battle.

The carefully selected elite Hunters of the Red Guard Gang were being killed by monsters, while Wu Heixing had just defeated one of the two Death Knights.

“I’ll be going.”

“Be careful not to get hurt.”

Go Jun answered with a brief bow and led the waiting Ares Guild members toward the battlefield.

They did not shout as they charged the monsters, but the force they radiated was more than enough to overwhelm everything before them.

*Kra-d-d-d-d-k! Slash!*

Lee Jungryong watched with satisfaction as one flank of the monster army collapsed in an instant.

Then he suddenly caught the smell of blood carried on the wind.

A wind blowing from the west.

A signal announcing the arrival of the person he had been waiting for.

“He arrived right on time.”

Lee Jungryong muttered under his breath and looked toward the distant horizon.

As he raised his qi, his senses sharpened like a razor, and he heard a man shouting.

—Fuck, kill them all! And that bastard who’s been going “Eeeeeeh” this whole time—if he does it one more time, I’m counting him as a monster. Got it?

Lee Jungryong let out a low chuckle and stretched out his hand.

Then he clenched his fist toward Jin Taekyung, who was somewhere out there.

[^1]: The Red Guards were radical youth organizations active during China’s Cultural Revolution.
## Chapter artifact 414

# Chapter 414

Some faces are never a welcome sight, no matter how many times you see them. For me, Lee Jungryong and Wu Heixing fell squarely into that category.

Even so, I was the one who spoke first because Wu Heixing looked almost presentable today.

“Fancy seeing you here. I thought I’d never see you again.”

At my cheerful greeting, Wu Heixing—looking like he had been dragged through a war—shot me a venomous glare.

“Shut up.”

“Oh…”

“Say one more word, and on my grandfather’s honor, I’ll tear you limb from limb.”

*A Chinese knockoff of Kindaichi, is he?* I could never understand why people like him treated their late grandfathers’ honor like a credit card.

I opened my mouth with a serious expression.

“Were you and your grandfather not on good terms?”

“What?”

“No, I mean, think about it. Why swear on your grandfather’s honor over something impossible? You’d be much better off swearing on getting torn limb from limb yourself…”

“You fucking bastard!”

As Wu Heixing sprang to his feet with an enraged shout, Lee Jungryong raised a hand to stop him.

“That’s enough.”

“Mr. Lee! But this bastard…”

“Fighting among allies when we’re about to face the final battle is entirely counterproductive. Calm yourself.”

*Crack.*

Wu Heixing ground his teeth hard enough to splinter them, then glared at me.

“Yes, sir. Since Mr. Lee has gone so far as to say that, I’ll stop here.”

“Good thinking.”

*Was he really the type to back down so obediently?*

As I watched Lee Jungryong, who wore a gentle smile around his lips, I turned my head slightly.

I could read countless thoughts in the brief glance I exchanged with Team Leader Choi.

“What about you, Jin Taekyung?”

I broke eye contact with Team Leader Choi and casually shrugged.

“When an elder speaks, you have to listen.”

“I didn’t know you were the sort to care about things like that.”

“Respect your elders, right?”

At my calm, unruffled answer, Lee Jungryong gave a hearty laugh whose meaning I could not decipher. Wu Heixing glared at me as if he wanted to kill me all over again.

“Respect your elders? Spare me that bullshit. What about me? I’m seven years older than you.”

“If you don’t want to write your will, start by making your eyes look nicer.”

“You turtle-dick-looking bastard…!”

“Don’t bullshit me.”

Wu Heixing’s second outburst was cut short.

I fixed him with a cold stare and continued.

“If you still have enough energy left to lose your temper over something this trivial, go check on the condition of the friends you brought here.”

“…”

“They followed you this far with their lives on the line. They’re not disposable supplies you use once and throw away.”

I made no attempt to hide my contempt.

There were barely fifty Hunters left around Wu Heixing.

According to the report from headquarters, the suicide squad had set out with five hundred people. Most of them had either died or fallen behind.

“Losses? Sure, that can happen. We’re in the middle of a battle. But…”

Even though Wu Heixing’s armor was drenched in blood, its exterior was still intact. That meant he had fought while taking care to protect himself even as his comrades died around him.

“Got anything to say, you fucking idiot?”

A line from an old superhero movie I had seen as a kid came to mind.

*With great power comes great responsibility.*

And that did not apply only to someone bitten by a radioactive spider.

If you were someone who could draw an aura blade instead of spiderwebs, someone who had used it to amass immense wealth and fame while covering up the crimes you had committed, then you had a responsibility to bear. At the very least, that was what I believed.

“You might be S-rank, but you’re no Hunter. So from now on, when you introduce yourself, don’t say you’re a Hunter. Just say, ‘I’m Wu Heixing, the lucky S-rank.’ Got it?”

“…”

As Wu Heixing silently trembled with his fists clenched, Lee Jungryong spoke in his place.

“He did his best.”

“Looking at that armor, I’m not so sure. It looks like I could wipe it down and put it on Junggonara as used equipment right now.”

[^1]: Junggonara is a popular Korean online marketplace for secondhand goods.

“Wearing sturdy, high-quality armor is not a reason to criticize him.”

“I’ve felt this since last time, but you take his side an awful lot. Did that bastard happen to get some kind of leverage over you?”

“Everyone has weaknesses. And I happen to be quite good at hiding mine.”

“Have your computer checked. Who knows? Maybe Chinese hackers have shared videos of the Vice Guild Master watching porn in a group chat.”

“I’ll keep that in mind.”

*He really is a formidable opponent.*

Lee Jungryong smiled without the slightest sign of disturbance, but the man standing behind him was different.

I waved at the man radiating a faint killing intent.

“Look who it is. Team Leader Seok. Isn’t that our Go Jun?”

Lee Jungryong’s Head of Security and Disciple.

I distinctly remembered beating him half to death before we left for China, but the man standing before me looked not merely fine, but even more solid than before.

Even from his deeper, more penetrating gaze, I could tell that his skills had advanced another step.

*And he’s developed patience, too.*

Go Jun was the most loyal of all the loyal hounds Lee Jungryong had raised.

In the past, he would have rushed at me without hesitation. But this time, he had gathered up his killing intent until not a trace remained and chosen silence instead of drawing his weapon.

Lee Jungryong looked pleased by his Disciple’s behavior and opened his mouth.

“We’ve made it right to the Arch Lich’s doorstep. According to the coordinates, only twenty kilometers remain.”

I swept back my hair, which was sticky with blood.

“Probably the longest and fiercest twenty kilometers on Earth.”

“That’s right. The Arch Lich has kept sufficient forces in reserve.”

“How many?”

“An estimated fifty thousand.”

The moment those words left his mouth, a single groan escaped from among the suicide squad, who had all been listening to our conversation with every nerve.

The suicide squads led by me, Lee Jungryong, and Wu Heixing numbered roughly five hundred in total.

Even by a simple estimate, the thought of breaking through an army a hundred times larger to reach the Arch Lich was enough to fill them with horrifying despair.

Perhaps that was why someone shouted in a trembling voice.

“We should retreat while we still can!”

Like a collapsing dam, the cries of other Hunters followed.

“Fuck!”

“There are too many monsters!”

“We’ll all be wiped out if we keep this up!”

“I came here to defeat the Arch Lich, not to die a meaningless death!”

The roughly two hundred members of the Western Front’s suicide squad, who had made it this far with barely any losses, were no exception.

And yet, even amid fear spreading like wildfire, two people remained unshaken.

Shao Shen, looking at me with unwavering trust, and…

“There’s a possibility.”

Team Leader Choi had gone beyond simply trusting me. He had independently deduced one possible explanation for the situation. He continued in a calm voice.

“An estimated fifty thousand is far beyond the number predicted by the High Command.”

“Then shouldn’t we obviously retreat?”

At the shout from one of the suicide squad members, Team Leader Choi immediately shook his head.

“And the number of monsters we faced was also lower than expected.”

“Huh?”

“There were certainly many of them, but the monster forces we encountered on the front lines were not as overwhelming as we anticipated.”

“Then…”

“The Arch Lich may have been wary of exactly this situation. Rather than commit all its forces to the front lines, it kept an army of fifty thousand in reserve as a final move that could respond to any situation.”

The Hunters staring at Team Leader Choi grew rigid. Not because they had properly understood what he was saying, but because of the vibrations growing steadily stronger beneath their feet.

*Grk. Gr-r-r-r-rk.*

The rumbling could be felt from dozens of kilometers away, and everyone’s body trembled.

A ruined road stretched before us, with vast plains on either side. Beyond the thick fog filling every direction, the roars and footsteps of tens of thousands of monsters merged into one faint, distant thunder.

“Grooooooar!”

“This is insane…”

“Run. We have to run. This is a battle we can’t win.”

People began to shuffle backward.

The only exception was the Ares Guild members, who stood firm without wavering. In front of them, Lee Jungryong watched Team Leader Choi with interest.

“So?”

Their eyes met across the open air. I saw Team Leader Choi’s grip tighten around **Hero’s Soul**.

“Although the High Command’s prediction was wrong, the front lines must have had forces to spare because the Arch Lich did not launch an all-out attack.”

“Even so, our forces were still insufficient compared to the enemy.”

“That is exactly why those people were left behind.”

*Grk. Gr-r-r-rk.*

The vibrations and roars grew even stronger. Amid the murmuring of people filled with anxiety and agitation, a single sentence from Team Leader Choi, carried by mana, pierced everyone’s ears.

“People who can overturn the entire course of a battle in an instant. S-rank Hunters—individuals who can each be called a one-person army.”

At that exact moment—

*Fwoooooosh!*

A dazzling mass of light burst above everyone’s heads.

Amid the brilliant radiance, the air split apart as if sliced by a sharp sword. Three people descended, stepping on invisible air as though it were a staircase.

“When I was a child, my great-grandmother would sit me on her lap and often tell me that royalty must fulfill the duties befitting their station. Of course, commoners like you would not understand.”

I let out a snort and bowed at the waist. He was usually annoying beyond belief, but this time I had no choice but to play along.

“His Highness, Prince Felix.”

“It is pleasing to hear it from your lips, Jin. Hunter of the Orient.”

At Prince Felix’s lofty, self-important attitude, the beautiful woman beside him clicked her tongue.

“Can’t you do something about him? At least tape his mouth shut.”

“I think we should indulge him today, big sis.”

“Oh my.”

Faye Chen opened her eyes wide at my answer, then broke into a bright smile.

“That sounds nice. Coming here was worth it after all. Don’t you agree?”

At Faye Chen’s question, the last person laughed heartily.

“Does this mean I can hope for something as well? What do you think, Jin?”

“What, should I kiss you?”

“Oh, that wouldn’t be bad. But I’ll politely decline. I’m already married to my beloved Fred, and I have five adopted children.”

*Fwoosh. Thump.*

Sliding down through the air, Magic Johnson patted my shoulder with a palm as large as a pot lid.

“Jin. You brave little rascal. How did you even think of attempting such a dangerous teleport? I almost gave up several times.”

“But you did it too, Johnson.”

“The odds were different. This time, there was only a ten percent chance of failure. You’re at least eighty percent braver than I am.”

Courage didn’t come in sizes.

Simply by risking death to come here, they had proved themselves worthy of being called the greatest Hunters in the world.

And the people who had received this unexpected reinforcement stared wide-eyed as if they could not believe what they were seeing.

“F-Faye Chen?”

“Prince Felix and Magic Johnson are here too!”

“They’re S-rank Hunters! S-rank Hunters came to help us!”

“I love you, Johnson! Fucking nice gay!”

But that was not the end.

*Boom. Boom. Boom.*

Another vibration, different from the one we had felt moments earlier.

It was the signal announcing the arrival of countless forces advancing in step. Far away, they appeared as a thin line of dots stretching across the distant horizon.

“Did you think we came all this way without a plan?”

Faye Chen continued with a grin.

“Ten thousand from the Western and Eastern Fronts combined. That should be enough to buy you time to get out.”

A dazed voice escaped someone’s lips.

“Now we can survive…”

“No.”

It was Team Leader Choi.

He raised **Hero’s Soul**.

Even through the dense fog, the transparent blade shone beautifully.

“We’re going to win.”

*I believed it too.*

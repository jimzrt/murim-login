# Checkpoint Review — 755–759

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

# Chapters 755–759

## Plot

The Skeleton King commands an enormous undead marine legion against Leviathan while Jin Taekyung delivers a final hellfire-infused spear strike. Leviathan escapes the deep-sea battle but crashes into a Japanese aircraft carrier, where Choi Minwoo captures it. Before Jin kills it with White Flame, Leviathan reveals that it was drawn by an unrefined S-rank Magic Gem and warns that humanity must survive until the end of the world. The System confirms Leviathan’s defeat, rewards Jin with massive EXP and Fame, grants him the Hope of the Sea Title, and activates the Main Quest: Cataclysm.

Jin secretly stores Leviathan’s corpse and the two Japanese-provided S-rank Magic Gems in his Inventory while publicly claiming they were destroyed. After a brief press conference restores public confidence in him, he accepts Germany’s request for help with an impending Monster Wave in Munich. Michael Silbert is also requested, but his forces are still fighting a Monster Wave in Cape Town, where an unidentified figure effortlessly kills the empowered Troll leader.

The Munich disaster breaches its barrier and releases an army of Minotaurs led by an S-rank Minotaur Lord. German forces fail to stop them, and Joel Schumacher is gravely wounded after confronting the monster. Jin arrives just as the Minotaur Lord is about to kill Schumacher and steps between them.

## Continuity

- Leviathan is dead; Jin secretly possesses its corpse and the two Japanese-government S-rank Magic Gems.
- Jin has obtained the Hope of the Sea Title; his Broken Body debuff and battle fatigue remain active.
- The Main Quest: Cataclysm is active, but its objective, rewards, and failure conditions remain unknown.
- Monster Waves can now arise naturally and increasingly often, suggesting a new disaster age beyond the Great Cataclysm.
- The Munich Monster Wave has breached its barrier and released an army led by an S-rank Minotaur Lord.
- Joel Schumacher, Germany’s S-rank Hunter and national symbol, is severely wounded; Jin is defending him.
- Germany has evacuated Munich, deployed military forces and roughly ten thousand Hunters, and prepared Uran as a nuclear last resort.
- Michael Silbert remains engaged in the Cape Town Monster Wave.
- Jin suspects Michael Silbert lured Leviathan with an unrefined S-rank Magic Gem but has no proof.
- An unidentified figure defeated the Cape Town Troll leader and said that a friend was waiting.
- Leviathan’s warning that humanity and the world awakened it remains unexplained.

## Translation Decisions

- Retain **Skeleton King**, **Leviathan**, **Broken Body**, **Hope of the Sea**, **Main Quest: Cataclysm**, **Great Cataclysm**, **Minotaur Lord**, **Uran**, and **Übermensch**.
- Render **마력** as **magical power**, distinct from **mana**.
- Render **격변** as **Cataclysm** in the Main Quest title and **대격변** as **Great Cataclysm**.
- Render **수상 구조대원** as **Aquatic Rescue Worker** and preserve the enhanced-title continuity.
- Render **무운을 빕니다** as **May martial fortune be with you**.

## Durable state

{
  "active_continuity": [
    "The Munich Monster Wave has breached its barrier, releasing an army of Minotaurs led by an S-rank Minotaur Lord.",
    "Germany has evacuated most civilians from Munich and deployed military forces and roughly ten thousand Hunters against the Monster Wave.",
    "Germany has prepared Uran, its nuclear-weapon contingency, as a last resort.",
    "Joel Schumacher, Germany's S-rank Hunter and national symbol, was severely wounded fighting the Minotaur Lord.",
    "Jin Taekyung has arrived in Munich and is protecting Schumacher from the Minotaur Lord.",
    "Jin's Broken Body debuff and battle fatigue remain active.",
    "Jin secretly stored Leviathan's corpse and the two Japanese-government S-rank Magic Gems in his Inventory while publicly claiming they were destroyed.",
    "Jin suspects Michael Silbert lured Leviathan with an unrefined S-rank Magic Gem, but he has no proof.",
    "Jin acquired the Hope of the Sea Title after the Aquatic Rescue Worker Title was enhanced and renamed.",
    "The Main Quest: Cataclysm is active, but its mission, reward, and failure conditions are unknown.",
    "Michael Silbert remains engaged in the Cape Town Monster Wave after his forces began suppressing the South African disaster."
  ],
  "continuity_sources": [
    759
  ],
  "open_questions": [
    "Can Jin defeat the Minotaur Lord and stop the Munich Monster Wave?",
    "What does the Main Quest: Cataclysm require, and what new age of disaster is approaching?",
    "Can Jin prove that Michael Silbert lured Leviathan with an unrefined S-rank Magic Gem?",
    "What did Leviathan mean by saying that humanity and the world awakened it?",
    "Who is the unidentified figure in Cape Town, and which friend is waiting?"
  ],
  "safe_through": 759,
  "temporary_decisions": [
    "Render 망가진 신체 as Broken Body.",
    "Render 수상 구조대원 as Aquatic Rescue Worker.",
    "Render 바다의 희망 as Hope of the Sea.",
    "Render 격변 as Cataclysm in the Main Quest title, distinct from 대격변 as Great Cataclysm.",
    "Render 미노타우로스 로드 as Minotaur Lord, 우란 as Uran, and 위버맨쉬 as Übermensch."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 755

# Chapter 755

The Skeleton King’s existence was like a demonic sword.

It possessed a blade sharp enough to cut through anything and tremendous killing power, yet it was something that could only be kept sheathed.

A demonic sword that had to be drawn and wielded only when absolutely necessary, and only where no one was watching.

In that sense, the deep sea, where darkness had swallowed every direction, was truly the perfect place.

*Shwoooooosh!*

A wave of bones surged and churned through the water.

The corpses of marine creatures, accumulated over hundreds—perhaps thousands—of years, awoke at the call of a single being.

The moment they opened their eyes, countless bones raced toward one another, obeying commands that bound their souls like chains.

*Crack. Clatter-clatter!*

They connected.

They merged.

And at last, they were complete.

A massive bone gateway that blocked the entrance to the deep sea.

A sturdy shield of wraiths that permitted not even a single breath to pass through.

And at the center of this wondrous phenomenon stood the king who had awakened the wraiths sleeping deep beneath the seabed.

—Stop.

*Fwoooooosh.*

A massive force swelled.

Brilliant blond hair swayed with the current. A faint silver radiance appeared above his fully exposed forehead and took shape.

A crown.

It was a mark granted to one who had ascended the throne by his own power, and the force it represented shone far too brilliantly to be called mere magical power.

—This is a royal command.

A voice filled with dignity and eyes filled with arrogance.

When Leviathan saw him staring back with shining golden eyes, it finally realized the true identity of the traitor who had dared to betray his own kind.

*The Skeleton King…!*

The king of wraiths.

One of the lords of the seventy-two legions who had sworn loyalty to the Demon King Asmodeus, and a being who had met its end after leading an endlessly resurrecting immortal legion against humanity.

But that traitor blocking Leviathan’s path with a dazzling crown was no longer the Skeleton King preserved in its memories.

*How?*

Where there was erasure, there was birth.

It was only natural that someone else would sit upon a throne left vacant. Yet the newly enthroned king of the wraiths was different—far too different.

—How can you stand on the side of mere humans while possessing such tremendous magical power?!

A shriek filled with equal parts bewilderment and rage.

Leviathan’s massive body, hundreds of meters in diameter, shot forward like a ray of light.

*Kwaaaaaa!*

Violent whirlpools spun in every direction.

Leviathan did not hesitate for even an instant as it advanced toward the wall of pure-white bones.

No. It had no other choice.

It had to break through. If it overcame the wall blocking its path and entered the deeper waters, it could survive.

Leviathan was a being that had first opened its eyes in the deep sea. Within that pitch-black space that no one could invade, it was confident that victory would be within reach.

At least, that was what Leviathan believed.

Until it felt the agony that arrived with a low voice.

“Where are you off to in such a hurry? We haven’t even settled the bill yet.”

*Crunch!*

—GRAAAAAAAH!

Leviathan’s massive body, which had been shooting forward like a ray of light, writhed violently.

Jin Taekyung had one hand tightly wrapped around the spear shaft driven deep into the monster’s brow. With his other hand, he had rammed a sword—no one knew when he had drawn it—into the monster’s enormous eye.

He muttered in a whisper.

“If we count one hit per person, it’ll take three days and four nights. Let’s make it a clean thousand.”

The number of casualties confirmed in less than a day already exceeded one hundred thousand.

They were strangers whose faces and names Jin did not know, but as he stared into the writhing Leviathan’s eyes, his own gaze burned with cold fury.

“We’ll have to get paid back for all that blood, won’t we?”

Monster and human.

Human and monster.

This was a fate decided from the moment the Demon King Asmodeus first set foot on this land more than thirty years ago.

The young man who had once been a boy remembered his father clearly—the father who had one day left and never returned.

He also remembered the pain of all those who had been placed in the same situation by this disaster.

*Inventory open. Summon.*

Spear, sword, axe.

It did not matter.

Countless weapons he had shoved deep into his Inventory whenever he had the chance flashed into his hands one after another, then plunged toward their targets in the blink of an eye.

*Thrust-thrust-thrust! Crunch!*

Scales shattered.

Bone and flesh were crushed.

The precise circulation of internal energy he usually employed was nowhere to be seen, but even that was enough.

The mythical monster that had reigned as the calamity of the sea for its entire life writhed in horrible agony unlike anything it had ever experienced.

—GRAAAAAAAH!

*Ruuuuumble!*

Magical power erupted from Leviathan and shook the sea.

Marine creatures swept along by the waves were unable to resist the overwhelming Fear. Their eyes rolled back until only white showed, and then a low voice breathed new souls into their dead bodies.

—Rise.

The fin of a blue whale that had been slowly sinking twitched.

Dozens of sturgeon whose bodies had been torn apart only hours earlier to serve as a monster’s meal bared their sawlike teeth.

—Grrrrrrr.

—Grk. Grk.

They were dead, yet not dead.

The countless marine creatures that had finally become a single legion moved as one body. And at their head stood the king of wraiths who had awakened them.

—My legion!

*Craaaaaack!*

At the Skeleton King’s cry, the wall of bones collapsed.

No—it transformed into a massive monster made of bones and charged toward Leviathan.

*Kwaaaaaa!*

Beyond a field of vision dyed entirely green with blood, Leviathan saw the Skeleton Legion charging toward it as one body and let out a roar.

—How dare you! You filthy little things!

*Gooooong. Boom!*

Deep beneath the water, compressed seawater shot out like cannonballs. Hundreds of waves shattered and broke countless bones.

But even Leviathan, who reigned as the calamity of the sea, could not control everything.

This vast ocean belonged entirely to it, but the countless deaths and wraiths flowing within the waves followed only the owner of the crown.

—Open your eyes.

Massive magical power writhed around the Skeleton King.

Through the raging whirlpools, wraiths that had been fading away raised their heads.

—Raise Skeleton.

*Clatter-clatter-clatter!*

Leviathan opened wide the eye that Jin Taekyung had half-crushed.

—…!

The bones that had been swept away by the waves gathered once more.

They reassembled their shattered joints, transformed into different shapes, and clung to Leviathan’s massive body.

They seeped through the cracks in its strength and clung to the monster’s magical power, which still had not run dry, draining it like leeches.

*Shhhhhhh!*

*What the hell…?*

Leviathan was stunned. Even the Skeleton King of the past had never been able to rebuild his legion so easily or so quickly.

Then what was that abundant magical power?

What was that absurd power of domination that made them attack Leviathan, a monster clearly superior to them?

And besides…

*It isn’t affected by my magical power at all.*

The relationship between monsters was governed solely by the ruthless logic of strength.

But the Skeleton King—the traitor who had newly ascended the throne of the wraiths—was different.

Even if he felt fear, he was not controlled by Leviathan’s magical power. And once they entered deeper waters, he was instead rampaging to his heart’s content.

*How?*

If Leviathan had fully recovered its former strength, or if it had maintained its composure as much as possible, it would have realized.

It would have realized that the Skeleton King’s power possessed a nature entirely different from ordinary magical power.

And it would have realized that the Skeleton King, who had absorbed a considerable amount of magical power after defeating the Arch Lich and Behemoth—both named monsters among the S-rank monsters—was not far beneath Leviathan in standing.

But the Leviathan of today was different.

For the mythical monster that had awoken from a long sleep only days ago, been gravely wounded, and grown exhausted, the entire situation was simply too confusing to believe.

Confusing enough to make it forget reality for one brief moment.

Then the horrific searing pain arrived and jolted Leviathan’s hazy mind awake.

*Fwoosh. Sizzle-sizzle!*

Leviathan gritted its teeth, half of which had already fallen out.

It had fought countless humans called Hunters during the Great Cataclysm, but it had never experienced pain like this.

Even when cut by a blade cloaked in aura, it had felt no more than a faint sting. And its worst injuries had always healed quickly after it absorbed another monster’s magical power and rested.

But the flames tearing through its enormous head even now, turning flesh and bone to ash, were different.

So was that tiny human.

“Fifty. Fifty-one. Fifty-two. Fifty-three…”

*Thrust-thrust-thrust!*

He was different from the humans Leviathan had fought before.

No—his level was different.

He kept muttering without pause as he drove weapons of unknown origin into various parts of Leviathan’s body and twisted them around. There was even a madness in his muttering that not even monsters could approach.

“We’re halfway there already. Come on, let’s keep it up a little longer.”

“Sir, just one more set.”

“Don’t move. Hold still, or you’ll break a bone.”

“Of course, it’ll break even if you don’t move. If you want to die in even more pain than this, go ahead and try something.”

—GRAAAAAAAAAH!

Leviathan let out a horrible cry.

No.

It was not a roar.

It was a scream.

The Fear that had once shaken the shores of the continent beyond the five oceans had become true terror, binding Leviathan itself.

And it was being caused by a single human who was unimaginably small compared to it.

*Die? I’m going to die? Me?*

The survival instinct it had forgotten after living as a predator for its entire life awakened.

One eye had already been crushed so badly that Leviathan could no longer properly distinguish its surroundings. Its body was drawing closer to death with every passing moment.

As the pain gradually grew duller, Leviathan swiftly judged the reality of its situation.

*Just once. I need to find a single opening, shake them off, and run as far away as possible.*

Fortunately, hope still remained.

Its tenacious vitality.

The magical power it had only used up halfway.

And the fact that its enemies were different from when it had first encountered them.

Especially that human who had dealt it such devastating damage with a single attack the day before.

*If he could display the same power as then, I would already be dead. Something must have happened to him too.*

Leviathan was a highly intelligent monster. Its judgment was accurate enough to be cunning, and its decision to risk its life was swift.

—Kwoooooo!

Its massive body, hundreds of meters in diameter, writhed with all its strength and released its magical power. A tremendous force surged outward like something inflating, pushing away everything around it.

*Kwaaaaaa!*

Dozens of whirlpools formed amid the enormous water pressure.

Leviathan shook off the Skeletons that had clung to it like leeches and were draining its magical power, then charged in a single direction.

*Whoooooosh!*

The water flowing over its enormous body became violent whirlpools and churned wildly.

The Skeleton King narrowly missed Leviathan and cried out like a scream.

—Human! Get out of the way!

It was already too late.

Swallowing those words, Leviathan shot forward with all its strength.

Toward a cliff that had taken root deep beneath the seabed thousands of years ago.

Toward the wall it needed to use to shake off this wretched human.

And then—

*Ruuuuumble!*

An enormous wave shook the sea as the two collided.

* * *

I had tried to avoid it.

I could have avoided it easily.

I had simply forgotten one important fact in the heat of battle.

Some of the powers I possessed had an expiration date.

*Beep.*

> **System**
>
> - The duration of the **Aquatic Rescue Worker** Title has ended!
>
> - The effects of the **Aquatic Rescue Worker** Title have disappeared!
>
> - The **Webbed Feet of the Aquatic Rescue Worker** have disappeared!
>
> - The **Gills of the Aquatic Rescue Worker** have disappeared!
>
> - Reactivation will be possible in **6 days 23 hours 59 seconds**!

Damn it.

Before I could even spit out that single curse, a massive boulder covered in green moss and seaweed had come up right behind me.

*Crack!*

“Urgh!”

A powerful impact.

Then pain squeezed my entire body.

Through the momentarily whitened field of vision, I saw Leviathan’s back as it staggered toward the surface, fleeing despite being unable to fully absorb the force of the collision.

I also saw the Skeleton King chasing after it while riding a half-dismembered shark.

*Clatter-clatter-clatter!*

Bone Binding.

A net of bones shot across the current and blocked the enormous body, but it could not restrain the monster thrashing with a desperate will to survive.

*Crunch!*

The bones shattered and scattered in every direction.

But it was not over yet.

I resisted the water pressure crushing my entire body and tightened my grip around the spear shaft.

*Craaaaack.*

Dark, freezing seawater seeped toward my mouth and nose, but I was fine.

My sharpened five senses were still fixed on the target.

The blue-white hellfire burning along the transparent spearhead was aimed at the body of the enormous monster fleeing in the distance.

So were my muscles, taut and ready to erupt.

*Shhhhhhh.*

Every sensation in my body sharpened.

The situation was the same as yesterday.

But a certainty took hold of my body and mind.

This time would be different.

*There won’t be a second time.*

Faith in myself.

And with the will to deliver a killing blow, I launched the spear with all my strength.

*Shhwaaaak!*

A single streak of flame crossed the sea.

At its tip waited the scream I had been expecting.

—GRAAAAAAAAAH!

The hunt was over.
## Chapter artifact 756

# Chapter 756

The desire to live is not granted to humans alone.

As long as a creature still has breath in its lungs and the intelligence to think, it can do nothing but struggle until the very moment its breath runs out.

Even more so when it is a born predator that has never once even considered death.

*Shwoosh! Splurch!*

—GRAAAAAAAAAH!

A spear fired from behind dug into a body as massive as a lava flow.

For an instant, Leviathan's vision turned white. The mythical monster, screaming from the pain, ground its broken teeth together.

*I won't die. This body won't die. Never!*

Leviathan swam with all its might.

But unlike its survival instinct, which was burning more fiercely than ever, its fins and tail—once capable of cleaving through the vast ocean like rays of light—barely moved.

No.

Its entire body, which had always been full of vitality, was gradually growing heavier.

*Why the hell…?*

Leviathan gasped for breath. But it could not stop here.

It had finally, barely, succeeded in shaking them off. A path to survival had opened. All that remained was to run as far away as possible and hide.

Even if it took decades or centuries, as long as it survived here, it could always take revenge.

Unlike humans, born with a mortal fate that lasted barely a hundred years, Leviathan could sustain a life close to immortality as long as it had water and magical power.

*In the end, I'm the one who will survive. Not you bastards. This Leviathan!*

Leviathan forcibly raised its body, which kept trying to sink.

It rode the waves surging in the aftermath of the battle and was swept along by the current toward the refuge waiting somewhere far away.

No.

It believed it could.

Until something cold and hard blocked its path.

*Boom.*

A dull roar, followed by the sensation of resistance.

*A reef?*

Through its hazy confusion, Leviathan raised its head. Reflected in the monster's half-crushed eye was a steel ship gleaming in the sunlight.

And standing above it, looking down at Leviathan, was a human.

“Operation complete. We will capture the target now.”

The quiet voice, addressed to no one Leviathan could identify, reached its ears.

Although it could not understand the human language, it was not difficult to guess the meaning.

—…Not yet. Not yet.

Leviathan gathered every ounce of strength remaining within its body. It raised the tail that had once smashed dozens of aircraft carriers apart in a single blow and lashed out at the human.

And then—

*Splash.*

As it watched water scatter helplessly instead of the tail that had measured dozens of meters, the monster of myth finally realized.

Its magnificent tail was already gone.

The streak of flame fired from behind had melted away half of its body.

—Ah.

Leviathan groaned.

And Choi Minwoo, the human who had crushed even the monster's final hope, gave a faint smile as he watched the silhouettes of two people approaching in the distance.

* * *

“Thank you for your hard work.”

“Waaaaaaaaah!”

“Uhyooooo! Leviathan getto da ze!”

At Team Leader Choi's single remark, the sailors from the Japan Maritime Self-Defense Force aboard the aircraft carrier let out a tremendous cheer.

I had vomited up enough seawater to fill a kettle before barely managing to open my mouth.

“Make them shut up. My head's ringing.”

The Skeleton King, so thoroughly soaked that he looked pickled in seawater, added his own comment.

“Tell them to quit making a fuss after everything’s already over and just steer the ship quietly. If they keep making so much noise, this body will summon the vengeful spirits of Pearl Harbor. You know what happens then, right?”

Team Leader Choi nodded.

“Yes. We'd run another raid right here.”

“…Are you serious?”

“I was joking.”

Leaving the Skeleton King behind with a wounded expression on his face, I headed toward the rear of the aircraft carrier.

The enormous monster was bound tightly in a magic-infused net, struggling to draw breath.

—You…

Even with its crushed eye, it somehow recognized me and muttered like a groan. I brushed back my wet hair and waved.

“Yeah, it's me, you son of a bitch.”

—K-kill me. I have not the slightest intention of suffering humiliation at the hands of a mere human.

I blinked silently. Then I asked Team Leader Choi,

“Did anyone say they were going to keep this thing alive?”

“Certainly not me.”

“Not me either. What about you?”

The Skeleton King, who had followed me over, answered curtly.

“Are you insane?”

“Right? I was wondering what the hell that bullshit was about.”

I shrugged and drove the White Flame I had recovered on the way into Leviathan's body.

*Splurch!*

A faint groan escaped it.

*Grrrk…*

It seemed as if death, which had drawn close once again, flickered in Leviathan's eyes.

Half of its body was already gone. No matter how tenacious its vitality was, an injury this severe could not be recovered from.

But before that, I had an answer I needed to hear.

“You should've stayed asleep. What made you crawl all the way here?”

—…Kill me.

“Ah, you can put that worry aside.”

*Splurch! Crack.*

I slowly rotated the spearhead embedded in its torso. Leviathan convulsed from the pain of having its bones literally scraped away and hurriedly answered.

—F-food! I smelled food!

“An S-rank Magic Gem.”

That was more or less what I had expected. I continued rotating the spearhead as I asked my next question.

“What woke you up?”

—Woke me up?

“We wouldn't know. You would.”

I tightened my grip around the spear shaft. But the answer that came with a groan did not change.

—Ghk. Ghk. I-I don't know. I only sensed magical power coming from the sea while I was starving after such a long hunger.

Was it telling the truth?

I did not have to think about it for long.

Everyone became honest in the face of death. And in Leviathan, which had already lost its will to live, I could not see the slightest trace of a lie.

*Damn it.*

I swallowed my disappointment.

It was obvious who had lured the monster here with an unrefined S-rank Magic Gem.

*Michael Silbert.*

The problem was whether I could prove it. Without evidence that he was the cause of this disaster, no one would believe me.

That was the kind of standing Odin Guild—and Michael Silbert—currently enjoyed in the world.

He had gone beyond merely holding the title of a hero of the Great Cataclysm. He had reached a position where he could even aspire to a realm only one person in human history had ever attained.

*Normally, it would be impossible even if I died and came back to life… But things are different now.*

Cheon Taemin.

If Prometheus had given fire to humanity, Cheon Taemin had defeated the Demon King Asmodeus and given humanity peace.

And he had accomplished it not in some myth riddled with all kinds of fabrications, but in reality, only a few decades ago—a feat never achieved before or since.

But before anyone realized it, he too had become part of the past.

To those living in the present rather than the past, Cheon Taemin was a great but unreachable figure—someone they remained grateful to, yet resented more than anyone else.

The world now cheered for a hero who acted in full view of everyone rather than one who had withdrawn from the world.

For Michael Silbert, one of the countless people who had been overshadowed by the name Cheon Taemin.

*…Damn it.*

The strength drained out of me. I pulled the spear shaft from deep inside Leviathan's body and aimed it at its neck.

The hunt was already over.

Now it was time to take the life of this tiresome monster.

“Goodbye. Just don't go finding peace in the next life.”

With that brief farewell, I raised the spearhead.

Blue-white flames had already gathered along the transparent blade.

One Strike.

A single strike was all it would take to end everything here.

The monster's body, having completely exhausted its strength, would be split apart like tofu by Force.

And I did not hesitate.

*Whoom.*

The moment the flames advanced, burning through the wind—

Leviathan, staring blankly at the falling spearhead, suddenly opened its mouth.

—The time has come.

What?

At the same time as the question rose in my mind, I twisted the spearhead. But my body, drenched in fatigue as deep as the salt in the seawater around us, reacted half a beat too late.

*Shhk! Shwaaaaaak!*

The thick neck, several meters in diameter, was sliced in half.

Beyond the green blood surging up like a wave, my eyes met the monster's eyes, already overshadowed by irreversible death.

Along with its final thought, which rang out not in my ears but in my mind—

—Magical power stirred my hunger, but you—and this world—are what woke me from my deep sleep.

“……!”

—The time has come, human. Please survive. Survive to the very end. Survive until the end of this world, and see with your own eyes the day I never got to see…

*Splash.*

The thought slowly scattered, then finally ended like an echo.

At the same time, the enormous maw that had been trembling violently slammed into the surface of the water.

And as I stared at the light fading from its eyes, confused, a clear ringing filled my ears.

*Ding. Ding. Ding.*

> **System**
>
> - You have defeated **Lv. 170 Leviathan**!
>
> - You have successfully completed **Quest: Calamity of the Sea**!
>
> - You have acquired a massive amount of **EXP** and **Fame**!
>
> - **Level Up!**
>
> - Special **Debuff: Broken Body** rejects the power of healing!
>
> - **Leviathan** is a powerful S-rank monster and the only Named monster. Since you have accumulated remarkable achievements, an additional **Reward** will be granted!
>
> - The effects of **Title: Aquatic Rescue Worker** have been enhanced!
>
> - The name of **Title: Aquatic Rescue Worker** will be changed!
>
> - You have newly acquired **Title: Hope of the Sea**!
>
> - …
>
> - …
>
> - …

Even as the bells rang without pause like a celebratory salute, I was seized by an inexplicable sense of foreboding and could not move.

*The time has come.*

And just as Leviathan's final words echoed through my mind once again, I suddenly realized.

*Ding.*

> **System**
>
> - **Main Quest: Cataclysm** has been generated!

A change too vast to measure had already come striding toward this world.

* * *

The death of Leviathan.

This brief but powerful news was first delivered to Japan's Ministry of Defense before spreading beyond the Japanese mainland and throughout the world.

[**Jin Taekyung succeeds in Leviathan raid!**]

[**The Calamity of the Sea finally meets its death!**]

[**The miracle of twenty-four hours. Asia's star takes flight after falling to rock bottom!**]

The people who had desperately prayed for the raid's success while suppressing their fear erupted in cheers, and the media outlets around the world that had watched Japan with bated breath poured out articles as though they had been waiting for this moment.

[**The dazzling rise of a young hero.**]

[**Japanese Prime Minister boldly declares at a press conference, defying everyone's expectations: “I kept it. Because it was a promise.”**]

[**Japanese Defense Minister abruptly dismissed. A lament from a senior Ministry of Defense official: “The Defense Minister was considering a kamikaze operation.”**]

[**A great achievement accomplished by only two S-rank Hunters!**]

[**Japanese netizens condemn the government and praise the hero. “What on earth was Japan's S-rank Hunter Yamamoto doing?” “Let's enthrone Jin Taekyung as shogun!”**]

[**Korean netizens mock Japan: “Yamamoto must have been cleaning.”**]

Countless articles and news reports swept across the internet like waves, and at the center of it all was always the same person's name.

Jin Taekyung.

Asia's star.

A bird that had taken flight once more after an endless fall.

But even amid the praise and cheers of the entire world, he could not smile.
## Chapter artifact 757

# Chapter 757

Twenty-eight hours.

That was all the time we spent in Japan.

If we had answered every interview and press conference that came one after another without pause, even twenty-eight days probably wouldn’t have been enough.

To be honest, I hadn’t really intended to stand in front of the cameras at first.

Not until I heard Team Leader Choi say:

“Those who survived need courage and hope.”

In the end, those words changed my mind.

Prime Minister Koizumi, who had possessed such an attention-seeking streak since his youth that people had treated him like a lunatic, welcomed my decision with open arms.

And the first things to greet me when I entered the press conference hall were the people’s cheers and a barrage of camera flashes.

“Waaaaaaaaah!”

*Pop-pop-pop-pop!*

It was strange.

Less than a month had passed since everything happened, yet it all felt like a long time ago.

Standing in front of reporters of my own free will. The media showing me favor, just as they were now.

Of course, that was separate from the fact that I hated wasting time.

I still had a problem I hadn’t been able to tell anyone about, and even now, another fire must have been flaring somewhere in the world.

“Let’s finish this quickly.”

But the Japanese media, which made up more than half the people in the hall, weren’t easy to handle. Not by a long shot, and in more ways than one.

“Jin-sama! Please become Japan’s shogun! You are the only one who can save these islands!”

I answered the first reporter’s question—or rather, his shout—as soon as he seized the microphone.

“Get him out.”

The members of the Self-Defense Forces assigned to security grabbed the reporter by both arms.

As he was dragged away, the microphone fell from his hand with a thud. Another Japanese reporter quickly picked it up.

“Leviathan was feared by our Japanese people to the point that it was called Susanoo. But Jin Taekyung-sama defeated it without much difficulty.”

*What the hell is he talking about? It was insanely difficult.*

But I didn’t let it show and answered calmly.

“It wasn’t an easy fight, but I did my best while thinking of those who lost their lives to Leviathan.”

“Ahhh…!”

“I would also like to offer my heartfelt condolences to the bereaved families.”

When I bowed my head, moisture glimmered in the eyes of many reporters. A Japanese reporter wiped the corner of his eye with his sleeve before continuing.

“Thank you for saying that.”

“I only did what had to be done.”

“Then I’m sorry, but may I ask you just one more thing?”

Normally, the answer would have been no. The rule here was one question and one answer, and I had no intention of letting this press conference drag on.

But I nodded at the reporter in front of me, who had asked a good question.

“Go ahead.”

“Are you familiar with Amaterasu, the sun goddess?”

“What? Which terrace?”

“I’m asking seriously. Jin Taekyung-sama, who defeated Susanoo—are you perhaps the reincarnation of Amaterasu, the sun goddess?”

“No, for fuck’s sake…”

The Self-Defense Forces waiting nearby rushed in, covered the reporter’s mouth, and snatched away his microphone.

Of course, that didn’t mean the Japanese reporters who remained began asking normal questions.

“If you could name just three Japanese anime series you like… Mmph!”

Patriotism was one thing, but weren’t these people completely insane?

And after realizing that subduing each reporter and dragging them out took a considerable amount of time, I chose to break through head-on.

“What have you generally thought of Japan?”

“An island. Next.”

“Japan has traditionally been a nation that values peace and etiquette—”

“Wakō pirates, the Imjin War, the Second Japanese Invasion of Korea, the Japanese colonial period, World War II. Next.”[^1]

“Our country’s S-rank Hunter Yamamoto Genji expressed his personal regret. He claims that if he had conducted a joint operation with you, we could have raided Leviathan much more easily. What do you think?”

“Then he should’ve arrived on time. Next.”

“No, please wait a moment! Yamamoto-san had circumstances that prevented him from coming!”

“A reporter… talking back?”

“……!”

I moved through the press conference like Zhao Zilong cutting through an army of a hundred thousand.

There were plenty of idiots whose questions made me wonder whether they even qualified as questions, but there were also quite a few sharp ones.

For instance, questions about the Skeleton King—not me.

They also asked about how the raid had succeeded, what had happened to Leviathan’s corpse, which had vanished in the explosion, and where the two S-rank Magic Gems provided by the Japanese government had gone.

If Team Leader Choi hadn’t anticipated questions like these, I might have stumbled a little.

“Skel—no, Stone King is an excellent Hunter who played a decisive role in this raid as well. Please understand that he was unable to attend because of exhaustion.”

“The raid’s details are classified, so I cannot disclose them.”

“Unfortunately, the corpse disappeared. The S-rank Magic Gem used as bait to lure Leviathan was also lost in the process. We offer our deepest apologies for this.”

“Ah…”

“How could such a thing…”

The corpse of a high-ranking monster was a treasure of immense value in itself.

The loss of Leviathan’s corpse was a tremendous blow, but the disappearance of the S-rank Magic Gems owned by the Japanese government was more than enough to draw sighs from the reporters.

Of course, if the truth—that all of it was a lie—ever came to light, those sighs would turn into fury.

*Team Leader Choi could become an actor now.*

I muttered as I watched him finish speaking without even twitching an eyebrow.

Leviathan’s corpse? The Magic Gems?

Of course we had taken everything.

The safest and most discreet place in the world.

My Inventory.

The sudden magical-power explosion that occurred while Leviathan’s corpse was being transferred to the aircraft carrier had been the Skeleton King’s handiwork. I had used that opening to quickly stuff everything into my Inventory.

The sailors of the Maritime Self-Defense Force realized that everything had vanished before their eyes and were left utterly devastated.

*I do feel a little bad, though…*

But what else could I do? Leviathan’s corpse was originally my share, and the S-rank Magic Gems provided by the Japanese government could be considered a long-term loan.

Even the finest sword in the world becomes nothing more than a kitchen knife in a cook’s hands. This was a time when I had to move like this, even if it meant selling my conscience.

*…Cataclysm.*

If only to resolve that question-riddled Quest that weighed so heavily on my mind.

* * *

Even during the Great Cataclysm, and now, decades after the war had ended, the symbolism and weight carried by the monster known as Leviathan had been enormous.

So enormous that, despite disasters large and small occurring all over the world, every eye had turned toward Japan.

And so enormous that it had been enough to etch the name of a young hero—whose light had been gradually fading—into everyone’s minds once again.

[**Grand Mage Magic Johnson: “I’m a mage, but Jin is magic itself.”**]

[**Prince Felix: “His nobility lies not in the blood flowing through his veins, but in his very existence.”**]

[**S-rank Hunter Pi Chen, speaking to reporters after suppressing a Monster Wave in downtown Hong Kong: “Free Hong Kong, Great Jin.”**]

[**He has returned.**]

[**The star of Asia who never lost his light despite countless condemnations. No—the star of the world.**]

[**A life-and-death struggle at sea. Hope triumphs over calamity.**]

[**The world’s worst terrorist, who turned a hero’s goodwill into evil. The masses, seized by fear, lost their judgment.**]

[**Head of North America’s largest media association finally speaks amid mounting criticism: “We have always reported only the facts. The claim that we targeted Jin Taekyung is nothing more than a malicious rumor.”**]

The media outlets representing countries around the world were the first to change their stance.

Journalists who had maintained a neutral position from the beginning, or who had supported Jin Taekyung, paid the greatest respect they could to Leviathan’s death. But those who had already joined hands with Odin Guild could not easily change course.

Public opinion flipping in an instant at the whim of the fickle masses was certainly something to be wary of.

But Michael Silbert had gone beyond being someone to watch out for.

He was frightening.

However, contrary to their anxious hearts, the public was slowly waking from the media’s incitement and the terror of the attacks.

“Simon. Why are you still in the office? Weren’t you supposed to be covering the anti–Jin Taekyung protest in the square today?”

“Um, the protest was canceled.”

“What?”

“Apparently, most of the participants dropped out. The expected turnout was thirty thousand, but when fewer than five hundred people remained, the protest naturally disbanded.”

“How could a protest that large fall apart so easily… Damn it. Fine. What about the protest leader? You know, the guy who acted like he was about to bomb Korea at any moment. Was his name Daniel?”

“Oh, Daisuke?”

“Yeah, him. Tell him we’ll give him extensive coverage, so he needs to gather some people right away—”

The news director, who had been badgering the reporter, suddenly frowned.

“Wait. Who’s Daisuke? We’re talking about Daniel.”

“Yes. Daniel. Daniel Daisuke. That’s the protest leader’s full name.”

“……Don’t tell me.”

“I regret having to say this myself, but I’m afraid that’s exactly what you think, boss.”

The reporter let out a put-upon sigh and explained everything to his superior point by point.

First. As could be inferred from the name Daisuke, the protest leader was Japanese.

Second. The fact that Japanese and Koreans disliked each other was almost as natural as universal gravitation. That was why Daniel Daisuke had stepped forward more than anyone else to organize this protest.

Third. Jin Taekyung had saved Japan, and the exceedingly devoted Daniel Daisuke’s mother was a Japanese woman from Tokyo.

“He’s the hero who saved his mother’s hometown. That’s basically what happened.”

The news director had remained silent through the concise, no-frills explanation made entirely of facts. He answered with a single short word.

“Fuck.”

His head throbbed.

Although the cancellation of the protest wasn’t their fault, would the “anonymous sponsor” who had promised a massive investment in exchange for a little biased reporting see it that way?

*Damn it. Management is going to raise hell.*

As he sighed with a complicated expression, his eyes fell on the television screen playing silently in the background.

[**Breaking News: Magical-power readings spike in Berlin. A Monster Wave is highly likely.**]

[**German government issues a Class 2 disaster warning.**]

[**German Prime Minister Markus makes an emergency announcement. A formal request for assistance has been sent to Korea.**]

Another Monster Wave.

The news director shook his head in disbelief. Then he spoke to the reporter, who had been watching his mood.

“What are you waiting for? Why aren’t you rushing to Berlin right now?”

* * *

“Mr. Jin Taekyung. The German government has requested assistance.”

At Team Leader Choi’s words, I answered without hesitation.

“I’ll go.”

The fatigue from the battle had not yet faded, and the Broken Body debuff was still active, but this was what I had to do.

“I’ll get ready right away.”

And just as I rose from my seat, Team Leader Choi’s voice pierced my ears.

“At the same time… we also requested assistance from Michael Silbert.”

I slowly turned around.

[^1]: The wakō were Japanese pirates who raided the coasts of Korea and China; the Imjin War and Second Japanese Invasion of Korea refer to Japan’s invasions of Korea in 1592 and 1597.
## Chapter artifact 758

# Chapter 758

“At the same time… we also requested assistance from Michael Silbert.”

The name that Team Leader Choi suddenly blurted out.

Michael Silbert.

I hesitated for a moment, but I wasn’t particularly surprised.

When someone is drowning, it’s only natural for them to reach out in every direction.

The German government had sensed the disaster that was about to descend upon them and was simply crying out for the best people who could save them.

Me, and Michael Silbert.

“You mean that gloomy, unpleasant human bastard?”

The Skeleton King continued with a displeased expression.

“I’d rather avoid running into him if possible.”

“No one here wants to run into him.”

At my retort, he clicked his tongue.

“Well, that’s true, but that human gave me a terrible feeling from the moment I first saw him… No, never mind. In any case, we need to arrive before those bastards do.”

This wasn’t some kind of sport to see who could save more lives, but I agreed with the Skeleton King’s final remark.

*If things continue like this, no one will be able to stop him.*

The greatest beneficiary of this meticulously engineered catastrophe was, without question, Michael Silbert.

From the first terrorist attack until now, Odin Guild had suppressed more than ten Monster Waves around the world. Michael Silbert had personally slain S-rank monsters in most of those battles, accomplishing spectacular feats and receiving thunderous applause.

For a while, he had even made people forget the name Cheon Taemin.

*I have to stop him now, while there’s still time. Somehow.*

I didn’t know what Michael Silbert’s ultimate goal was.

But if a monster like that gained unchecked fame and power, if he reached the same level of inviolable sanctity as Cheon Taemin…

I was certain that a disaster even worse than the current one would occur.

“Team Leader Choi.”

Understanding the meaning behind my call, Team Leader Choi nodded.

“The pilots are already waiting.”

We were in a situation where we had to move as quickly as possible.

Team Leader Choi, the Skeleton King, and I hurried toward the aircraft that had already been prepared, exchanging words as we went.

“What’s the situation in Germany?”

“A Class 2 disaster warning has been issued, centered around Munich. According to the information provided by the German government, a Monster Wave will occur within five hours at the latest.”

“The government saying five hours at the maximum means…”

Team Leader Choi nodded.

“It could happen at any moment, in practical terms.”

Running on wishful thinking in the face of disaster was a universal human trait. Or at least governments responsible for evacuating people had no choice but to do so.

The moment the German government officially admitted, “We’re fucked,” a major city like Munich would descend into chaos in an instant.

“Damn it.”

“Fortunately, their response so far has been excellent. Every country in the world has been on high alert since the terrorist attack on the Paris branch, and more than three thousand Hunters have gathered in Munich since the Class 2 disaster warning was issued. Our Ares Guild is one of them.”

“That’s something, at least. What about Odin—or rather, that man?”

Team Leader Choi answered the Skeleton King’s question.

“Of course, Hunters from the Odin Guild branch in Munich are standing by as well, but… the core forces led by Michael Silbert are currently in Africa.”

“Africa?”

“Yes. According to the information we received, they’re currently suppressing a Monster Wave that occurred in South Africa. They’ll finish up there and head straight to Munich.”

“That man has it easy. He starts trouble everywhere, then cleans it up one place at a time?”

The Skeleton King sneered, but I shook my head.

“That’s not it.”

“Hm?”

“If it had been part of his calculations from the beginning, he would have left for Munich by now. So at least the incident in Munich wasn’t a terrorist attack he had a hand in.”

“That’s right. Which is why it’s even more dangerous.”

“Why is that more dangerous? If it wasn’t his intention, then wouldn’t that actually—”

The Skeleton King’s voice trailed off.

His face, which had been filled with confusion as he questioned Team Leader Choi and me, hardened.

“Ah.”

It seemed he had finally realized it, too.

What this incident meant, and how much danger and anxiety it contained.

*Even without an artificial terrorist attack, Monster Waves can now occur naturally.*

Of course, Monster Waves had still occurred after peace had arrived.

But the problem was that disasters which had once happened *very rarely* had reached a point where their frequency could now be described as *occasionally* or even *often*.

Enough to make humanity remember the days when corpses piled up like mountains and rivers flowed red with blood.

The Great Cataclysm.

Humanity had recorded that horrific past in those three characters. But at this very moment, a question suddenly occurred to me.

What name would be given to the new age of disaster that was about to begin—or perhaps had already begun?

And…

What was this System, which had given me happiness and pain at the same time, trying to tell me?

*Open Quest window.*

*Ding.*

> **System**
>
> **Quest**
>
> **Cataclysm**
>
> The new era has already drawn close, and the final word of this long and fierce story has yet to be decided.
>
> Hope. Or despair.
>
> And at this very moment, you are the only person holding the pen.
>
> May martial fortune be with you.
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

A quest description with no clear answer, and a mission filled with question marks.

But more than anything else, what weighed heavily on my chest was the brief line written under the quest’s grade.

Those five characters that stabbed painfully into my eyes.

*Main Quest.*

I had received more quests than I could count.

They had ranged from the easiest Third Rate quests to Supreme Peak quests that required me to stake my life. Their grades differed according to difficulty, and there had been various types, such as sudden quests.

But…

This was my first Main Quest.

More precisely, it was my first one since the day I opened my eyes in the unfamiliar world of Murim.

Yes, since the day everything had begun.

*What the hell does this mean?*

I didn’t know what the mission was. I didn’t know what this new era that was about to arrive meant, either.

No. Deep down, I had an inkling, but I was desperately insisting it couldn’t be that.

Because I was afraid.

Just as the System had said, I was the only person holding the pen at this very moment.

The days when I had laughed as I read web novels packed with exhilarating wish fulfillment were long gone. Now I had to write the story myself.

With a pen. With a spear.

With blood and death whose owners I didn’t know.

“…man. Human?”

The voice that seemed to come from far away awakened my mind from its thoughts.

I blinked and looked around.

The area around me was filled with unfamiliar faces and noise.

The propeller spinning with a roar. The pilots’ tense faces visible beyond the aircraft windows.

And two people looking at me with worried expressions.

No. One person and one monster.

“Mr. Jin Taekyung, are you all right?”

“Wicked human. Look carefully. How many fingers am I holding up?”

I looked at the Skeleton King, who was slowly waving his hand in front of my face.

“I can’t see a single one.”

“Wrong. One. Your condition is more serious than I thought—”

“I deliberately didn’t count the finger you’re waving because I’m going to pull it out soon.”

“……”

“You’re still waving it. Fold that finger while I’m asking nicely.”

As the Skeleton King quietly folded the middle finger he had been enthusiastically waving, Team Leader Choi spoke in a subdued voice.

“If there’s a problem, we can move after you’ve rested. We don’t know what kind of S-rank monster will appear, but there are forces on-site capable of responding to it, so…”

“No. I’m fine.”

I cut Team Leader Choi off firmly.

Although the mental fatigue and the effects of the Broken Body debuff had left my body weaker than before, it was obvious that the later we arrived, the greater the damage would be.

The mission given to me now was to stop the disaster.

The disaster that would occur in Munich.

And, beyond that, the disaster that would swallow this world.

“Let’s go. Before we lose any more time.”

With those few words, I climbed aboard the fighter jet.

I thought of the name of the man at the center of the disaster—the enemy I would soon face again.

*Michael Silbert.*

*Come to Munich.*

The mutter that would never reach him lingered in my mouth before scattering away.

* * *

South Africa.

Commonly known in Korea by the abbreviation Nam-agong, this country was Africa’s most highly developed industrial nation. Because it had few Gates, it was also one of the countries that had suffered the least damage from monsters, from the Great Cataclysm until now.

At least until half a day ago.

*Rumble!*

Smoke mixed with flames blotted out the clear sky.

Cape Town, the capital of South Africa, where the wealthy and countless tourists from around the world came and went, was now filled with screams, death, and the grotesque cries of monsters.

*Crunch! Crash!*

“Graaah!”

“Ghk!”

A group of Trolls charged in after taking over the road, swinging the clubs in their hands indiscriminately.

The steel clubs, wielded with the powerful strength unique to large monsters, struck the people fleeing in all directions. They collapsed with dying cries.

*Crack!*

—Kwoooaar!

The leader stomped down on a fallen corpse’s head and crushed it, then let out a savage roar.

After tasting human blood for the first time in a long while, the monsters under its command moved according to instinct.

*Craaaack!*

They grabbed a moving car and slammed it into the ground. Dozens of them rushed in and smashed buildings of all sizes, bringing them down.

Countless explosions erupted, but their tough skin and the Trolls’ incredible Regeneration were completely unaffected.

*Boom!*

Flames surged fiercely with another explosion.

The leader smiled with satisfaction as its damaged hide regenerated in an instant, as if it refused to tolerate even the slightest wound.

At the leader’s large, thick feet lay the corpses of Hunters whose limbs had been twisted or whose torsos had been split in half.

—Grrrk.

Easy.

Far too easy.

If this had happened not long ago, it would not have been able to deal with the humans who crossed through the Gate and invaded its territory so effortlessly.

But things were different now.

—Ha. Ha. Ha!

The world was changing.

The monsters’ bodies were filled with purer and more powerful magical power than ever before, and the humans could not stop them.

Everything was returning to its proper place.

The humans who had transformed from prey into hunters over the past several decades…

Had once again fallen back into the role of prey.

—I. WILL. KILL. EVERY. LAST. ONE!!

It was the moment when the rage of the long years of oppression—of having their territories invaded and being hunted by humans—erupted as a roar.

*Whoosh! Boom!*

The leader’s vision suddenly went black.

No. Its head had disappeared.

But the leader was not surprised.

Trolls could survive even if their heads were blown off. Unless their bodies were pulverized, their immense Regeneration would allow them to survive—

*Whoosh-whoosh-whoosh! Boom-boom-boom!*

Along with the sound of air splitting, the leader’s consciousness snapped off.

Its terrifying Regeneration and body as hard as steel were useless at this moment.

*Slip. Thud.*

Without even having time to wonder what had happened, its body dropped to its knees.

Silence descended with the leader’s death.

—Kwo?

As the Trolls looked around in confusion, a calm voice reached their ears.

“Let’s finish this quickly.”

*Step.*

With the footstep moving forward, a colossal force bore down on everything around them.

“My friend is waiting for me.”
## Chapter artifact 759

# Chapter 759

The inside of the command center was hot and muggy, like a steam sauna.

No. In truth, that was only an illusion brought on by the extreme anxiety and unease pressing down on everyone’s hearts.

As if to prove it, despite the temperature being perfectly controlled around the clock by Magic, cold sweat poured down the forehead of Markus, the German prime minister.

“Magical power levels are surging!”

“We expect them to reach Class 1 within thirty minutes!”

“The range of the magical-power increase is expanding!”

“Intelligence has recalculated the enemy’s size! At least ten thousand troops!”

“A report from Commander Scholz! He requests authorization to use ‘Uran’ as a precaution!”

At the final report, Prime Minister Markus bit his lip.

Uran.

Those two characters, treated as the most classified of secrets, stood for uranium. In other words, nuclear weapons.

Naturally, Germany, a nation defeated in the Second World War, was not allowed to possess nuclear weapons. But in this world, there were truths that could not be revealed.

*They want to use Uran? Now of all times?*

Commander Scholz, who was in charge of Munich’s blockade, was not an idiot who spoke without thinking. He was one of the few excellent commanders to achieve military success during the Great Cataclysm, and a man of cold, rational judgment.

“Your Excellency.”

At his aide’s call, Prime Minister Markus squeezed his eyes shut. Then he forced his mouth open.

“Prepare Uran.”

“B-but…”

“It is merely a measure for the worst-case scenario. I am giving this order as the head of this nation’s government.”

The generals and aides, who had stared wide-eyed at the unexpected order, soon nodded.

They already knew. Against superior monsters that were no different from demons, modern weapons capable of inflicting meaningful damage were almost exclusively nuclear weapons.

And…

*If this truly is the worst-case scenario, even nuclear weapons won’t be of any use.*

Nuclear weapons were double-edged swords.

If there was a monster among the enemy comparable to a high-ranking mage, it could use spatial teleportation to drop a nuclear missile with horrific destructive power over the skies of a major city.

If the nuclear attack succeeded, Munich—the city known as Germany’s third city—would be wiped off the map. And if it failed…

He did not even want to imagine it.

“What about the citizens?”

“The evacuation operation is still underway. At present, only around ten percent of Munich’s population remains in the danger zone.”

“Hurry it up. Once things begin, there will be no turning back.”

“Yes, sir.”

The capital, Berlin, had taken a direct hit in the earlier terrorist attack.

They could not stand by and let Munich go through the same process. Even counting only the human and material damage caused by Monster Waves so far, the losses had already reached astronomical levels.

*This time, we have to stop it.*

Even if it meant blowing the entire city away with nuclear weapons, the people had to survive.

A nation could exist because there were people living within its borders.

And to make that wish a reality, they absolutely needed reinforcements.

A Hunter who was a one-man army, capable of doing the work of a thousand—or even ten thousand—single-handedly.

“What happened to them?”

*Them.*

It was only two words, with no name attached, but no one in the command center failed to understand what they meant. Reports poured in simultaneously from every direction.

“Michael Silbert is engaged in combat in Cape Town!”

“The battle is heavily in our favor! We expect it to end within thirty minutes!”

“Damn it. Why did it have to be Africa?”

Just as an anonymous voice let out a sigh, one of the aides quickly continued.

“Jin Taekyung is traveling to Munich. His estimated time of arrival at the site is approximately one hour.”

“What? An entire hour?”

“Didn’t you say there were only thirty minutes left before it reached a Class 1 disaster?”

“I-I’m sorry. He’s traveling as quickly as possible by fighter jet, but the distance is over eight thousand kilometers…”

“Goddamn it!”

Amid the people who had completely forgotten the meaning of composure, Prime Minister Markus rubbed his forehead with a handkerchief already damp with sweat.

“Everyone, stay calm. Even if the predicted size of the monsters has grown, we are by no means outmatched. First, evacuate all remaining citizens within the time we have left, and deploy every available force.”

The main forces surrounding the danger zone currently numbered five thousand.

If they also deployed all the reserves waiting in the rear, they would have an army of Hunters numbering no fewer than ten thousand.

Moreover, at its head stood Schumacher, an S-rank Hunter Germany was proud of.

Thud.

Prime Minister Markus sprang to his feet and spoke in a resolute voice.

“This is a fight we have a good chance of winning. Thirty minutes. If we can hold out for a mere thirty minutes, we can minimize the damage and bring this situation to an end—”

And at that very moment—

“An emergency report from Commander Scholz!”

Along with the scream-like cry that swallowed the rest of the prime minister’s words, a massive shock swept through the command center.

“T-the magical power! The magical power has broken through the critical point!”

A breakthrough of the critical point.

There was only one thing that could mean.

Monster Wave.

At last, the sturdy dam—the barrier that had separated humans from monsters—had collapsed.

* * *

Rumble-rumble-rumble!

A tremendous vibration swept through Munich.

The concrete-covered ground split apart, and high-rise buildings designed to withstand even earthquakes collapsed like dominoes.

Kaboom!

And beyond the thunderous roar that shook the world, people could finally hear it. Finally see it.

Ssshhh!

The sound of the air splitting apart as if cleaved by a sword, and the cries of countless monsters revealing themselves from within.

—Grrrk.

Ssssss.

A mist darker than gray—black, in fact—flowed out and seeped into every corner.

Monsters with the heads of bulls and arms and legs like humans.

The Minotaurs that emerged without end drew harsh breaths and looked around.

An unfamiliar world filled with every kind of noise they had never heard before.

Yet the magical power permeating it was sweeter than anything they had ever tasted, and the sight of countless humans in the distance awakened the ferocity they had been born with.

—Krrk, kaaaaa!

*Kill them. Kill the humans and conquer this world.*

The Minotaurs let out a unified roar and charged across the ground.

Toward the humans who had formed a wall of steel with their enormous shields.

For more blood and magical power!

Rumble-rumble-rumble!

And at the moment when countless hooves pounded the earth—

Whoooosh.

With a heavy roar of air being torn apart, countless streaks crossed the sky and plunged down over the monsters’ heads.

KABOOM!

A barrage of missiles poured down by the German federal forces waiting in the rear.

Massive explosions accompanied by flames swallowed everything around them. Everything left behind in the area, where most of the citizens had already been evacuated, was reduced to ash and melted beneath the horrific firepower.

Or at least, that was what they wished would happen.

Even though they knew that the firepower born of science could not stop those monsters.

Kaaaaa…

The bombardment that seemed as though it would continue forever finally ended.

Amid the silence that settled over the city in an instant, one of the Hunters staring at the mist that had not disappeared muttered quietly.

“They’re coming.”

And that one word, which everyone had thought, soon became a prophecy.

Thud-thud-thud-thud-thud!

A fierce vibration shook the earth. Beyond the dark mist, an uncountable number of monster horns flashed.

Along with the roar of a monster radiating a presence more overwhelming than any Minotaur’s—

—Kraaaaaa!

The Fear of the S-rank monster, the Minotaur Lord, spread in every direction.

At the head of the army he led, the chieftain had blown away everything blocking the broad road and forcefully kicked off the ground.

Boom! Fwoosh!

The ground sank as deeply as a sinkhole.

As the monster’s massive body charged forward with a tremendous roar, a figure shot toward it at the speed of a beam of light.

“How dare you!”

The cry was filled with undisguised fury.

Once Germany’s representative fencing gold medalist, he had become Germany’s very symbol—the S-rank Hunter Joel Schumacher. A sabre moved in accordance with his hand.

Whoosh!

A silver streak crossed the air with a sharp roar.

And at the moment when the enormous halberd, swung with brutal force, met it head-on—

BOOM!

A muffled roar and shock wave shook everything around them.

It was the signal announcing the beginning of the battle, and the two species, bound to a fate they could not escape, charged toward each other.

“Formation!”

“Don’t fall back! Kill them all!”

—Kaaaaa!

Rumble-rumble-rumble!

Shhk-shhk-shhk! Splurt!

Countless roars and screams.

And death following close behind the screams as they echoed through the battlefield.

It was the beginning of a horrific bloodbath that could end only after they had killed and been killed by one another.

* * *

Joel Schumacher fought as if possessed.

He was so consumed that he could not even feel the passage of time, much less know who around him was dying or how many had fallen.

He had no choice. If he looked away for even a single moment, that enormous halberd would tear his body to pieces.

Whoom, splurt!

The halberd’s blade passed right in front of him with a heavy roar of air, making the fine hairs on his body stand on end.

But at the same time, his body—seasoned by countless repetitions of training and battle—moved as naturally as flowing water.

Fwoosh, bang!

Compressed air burst from the tip of the sabre he thrust out with his step.

The Minotaur Lord took a step back with agility unsuited to its massive frame, its face twisting.

—Krrk?

A cry filled with confusion and pain. At some point, a hole the size of a child’s fist had appeared in its shoulder.

*I did it.*

Schumacher felt a tingling rush of pleasure run down his spine.

The movement just now had been so natural and fast that even he had not been aware of it. It had been as if invisible strings were controlling his body.

*What was that? Have I lost too much blood?*

The fight against the Minotaur Lord was by no means easy.

No. To be honest, it was grueling.

The rusted spearhead of the halberd tore chunks of flesh away with the slightest graze, and the tremendous force transmitted every time their weapons collided rapidly drained his Stamina.

Strength: overwhelmingly inferior.

Speed: slightly superior.

That had been the result so far, and the enormous fatigue and blood loss were making Schumacher’s vision hazy.

But…

For some reason, he felt as if he could do anything now.

As if he could bring down that terrifying monster and become the superhuman who saved this land.

*Yes. The Übermensch.*

The father of German philosophy, Friedrich Nietzsche, had said it long ago.

The Übermensch was a superhuman who rose even amid tragedy, a great overcomer who sought to realize his potential to the utmost.

And now, at this very moment, Joel Schumacher was rising another step—not through an idea, but through martial force.

From the countless years of training and experience he had accumulated as the world’s greatest fencer.

And through his desire to survive.

Whoosh! Shhhh!

Countless streaks of light crossed the air.

Every time the sabre danced, swung with the least movement and the greatest speed, the Minotaur staggered backward, spraying blood.

Stab. Slash.

He stabbed and slashed.

The monster’s body, reflected in Schumacher’s hazy eyes, was filled with countless openings, and his senses, sharpened to their peak, were focused on one thing alone.

The Minotaur Lord.

*Now!*

Slash! Fwoosh!

As he watched a fountain of blood shoot into the air, Joel Schumacher blinked.

*Huh?*

Something was strange.

The monster’s blood should have been green or blue, yet the blood raining down over his head was red like a rose.

As if it were human blood.

“…Cough.”

Blood spilled between his cracked lips.

At the same time, the dreamlike haze vanished from his senses, and the reality that rushed in all at once awakened his consciousness.

*I’d been cut.*

Not *I cut it.*

*I’d been cut.*

Schumacher staggered as fiery pain radiated from his back.

At the last moment, while all his senses were fixed on the chieftain, a Minotaur had slashed his back with a rusty sword. His comrades hacked its head off and caught him as he staggered.

“Schumacher!”

“Damn it! Get him out of—”

Whoooosh, splurt!

Along with the heavy roar of air being torn apart, the hands supporting him and the breath of his comrade disappeared.

Schumacher lost his balance and collapsed, then raised his head while gasping for breath.

The Minotaur Lord.

The leader of the monsters that had come to Munich was looking down at him.

With an enormous double-bladed axe raised overhead.

*…Goddamn it.*

It was over.

For Munich.

For the Hunters here.

And for the Übermensch his homeland, Germany, had wanted so desperately.

Joel Schumacher closed his eyes with a hollow laugh.

No. It was at the moment he was about to close them.

“You’re going to die like this?”

The unfamiliar voice that pierced his ear awakened his fading consciousness.

In his dizzy vision, Schumacher slowly blinked and saw someone’s back blocking the way in front of him.

A back broader than the Minotaur Lord’s, radiating a calm yet overwhelming presence.

And a spear held in that person’s hand.

At the same time, Joel Schumacher realized.

“Jin… Taekyung.”

Asia’s Übermensch had arrived on the battlefield.

# Checkpoint Review — 760–764

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

# Chapters 760–764

## Plot

Jin Taekyung leads the counterattack against the Munich Monster Wave, killing the Lv. 140 Minotaur Lord and ordering the surviving Minotaurs exterminated. Munich is secured, but roughly fifteen hundred humans are casualties, including nearly one thousand dead. Michael Silbert arrives after completing the Cape Town operation, where The Prophet had helped coordinate the disaster campaign.

Before the international press, Michael announces that magical power has crossed a critical point and that a second war—possibly a second Great Cataclysm—is imminent. He questions whether Demon King Asmodeus was truly erased and proposes reviving the World Hunter Federation as an organization above national laws. Jin recognizes Michael’s plan as an attempt to establish a personal kingdom and rejects it publicly.

Michael then reveals that he knows the Skeleton King is a monster, using the threat of exposure to force Jin into a private meeting. Jin orders Team Leader Choi to obtain Magic Johnson’s complete investigation into Michael and the evidence from Siegfried Wassman’s hideout before boarding Michael’s aircraft. During their confrontation, Jin identifies himself as the Blazing Flame Divine Dragon and threatens Michael with death if he exposes the Skeleton King.

## Continuity

- The Munich Monster Wave is defeated; the Minotaur Lord is dead, but human forces suffered roughly fifteen hundred casualties.
- Michael Silbert completed the Cape Town operation and remains the principal human threat behind the coordinated Monster Waves.
- Michael claims global magical power has crossed its critical point and that another war or Great Cataclysm is approaching.
- Michael publicly casts doubt on Demon King Asmodeus’s destruction and promotes the World Hunter Federation as humanity’s ark.
- The historical World Hunter Federation followed Cheon Taemin during the Great Cataclysm; the surviving organization is the International Hunter Federation.
- Jin rejects Michael’s proposed federation as a personal kingdom and believes destroying Michael’s plans—or killing Michael—is central to completing the Main Quest: Cataclysm.
- Michael knows the Skeleton King’s identity and is currently withholding that information to coerce Jin.
- Jin has tasked Team Leader Choi with obtaining Magic Johnson’s investigation of Michael and all evidence from Siegfried Wassman’s hideout.
- The Skeleton King remains under orders to suppress his magical power and conceal his identity from humans.
- Joel Schumacher remains unconscious under the Skeleton King’s protection.
- Jin remains affected by the Broken Body debuff and battle fatigue.
- Jin secretly retains Leviathan’s corpse and the two Japanese-government S-rank Magic Gems.
- The Main Quest: Cataclysm remains active, with its completion conditions still unknown.

## Translation Decisions

- Keep **Skeleton King**, **Michael Silbert**, **Minotaur Lord**, **Main Quest: Cataclysm**, **Great Cataclysm**, **World Hunter Federation**, **International Hunter Federation**, **Broken Body**, and **Übermensch**.
- Render **마력** as **magical power**, distinct from **mana**.
- Render **좆 까** as **Go fuck yourself** to preserve Jin’s blunt profanity.
- Render **간웅** as **unscrupulous schemer**.
- Continue distinguishing the historical **World Hunter Federation** from the surviving **International Hunter Federation**.

## Durable state

{
  "active_continuity": [
    "Michael Silbert has publicly declared that a second war is approaching because global magical power has crossed its critical point.",
    "Michael has publicly suggested that Demon King Asmodeus may not have been truly erased despite claiming to have witnessed his destruction.",
    "Michael has proposed resurrecting the World Hunter Federation as an international organization encompassing every country and transcending ordinary laws and restrictions.",
    "The historical World Hunter Federation followed Cheon Taemin during the Great Cataclysm and returned to its members' respective places after victory; its surviving remnant is now called the International Hunter Federation.",
    "Jin publicly rejected Michael's proposal and considers Michael's intended federation a kingdom built for one man.",
    "Michael now knows the Skeleton King's identity and is using the threat of public exposure to force Jin into private negotiations.",
    "Jin has ordered Team Leader Choi to obtain Magic Johnson's complete investigation of Michael and the evidence from Siegfried Wassman's hideout.",
    "The Main Quest: Cataclysm remains active, and Jin believes it will not end until Michael's plans are destroyed or Michael himself is killed.",
    "Jin remains exhausted and affected by the Broken Body debuff after the Munich battle.",
    "Joel Schumacher remains unconscious and under the Skeleton King's protection.",
    "Jin still secretly possesses Leviathan's corpse and the two Japanese-government S-rank Magic Gems while publicly claiming they were destroyed.",
    "The Skeleton King must continue suppressing his magical power and concealing his authority from humans unless using it becomes unavoidable."
  ],
  "continuity_sources": [
    764
  ],
  "open_questions": [
    "Is a second Great Cataclysm truly imminent, and what caused global magical power to cross its critical point?",
    "Was Demon King Asmodeus actually erased during the original victory?",
    "How did Michael obtain certainty about the Skeleton King's identity, and what evidence does he possess?",
    "Can Jin prevent Michael from reviving the World Hunter Federation and turning it into a personal kingdom?",
    "What exactly does the Main Quest: Cataclysm require before it can end?"
  ],
  "safe_through": 764,
  "temporary_decisions": [
    "Render 스켈레톤 킹 consistently as Skeleton King, not Stone King.",
    "Render 세계 헌터 연맹 as World Hunter Federation and 국제 헌터 연맹 as International Hunter Federation, keeping the historical and surviving organizations distinct.",
    "Render 좆 까 as Go fuck yourself to preserve Jin's blunt, profane rejection.",
    "Render 간웅 as unscrupulous schemer.",
    "Continue rendering 마력 as magical power, distinct from mana."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 760

# Chapter 760

“Über, what?”

He had definitely called my name before muttering something, but when I glanced back, Joel Schumacher was already collapsed against a pile of concrete with his head resting on it.

*He really burned himself out.*

And it was understandable. From what I had seen, he had clearly been fighting in a state of Trance.

A dreamlike moment when one gained enlightenment and advanced into a greater realm.

Unfortunately, Schumacher had been ambushed before he could reach the end of that moment, but when he opened his eyes again, he would probably be stronger than before.

“Should I wake him?”

“He won’t be able to get up even if you wake him right now, so just leave him. Make sure that man doesn’t die.”

“You heard him, right? Handsome per—no, Team Leader Choi?”

“…Understood.”

Seeing how naturally that bastard dumped the work on someone else, I realized he had truly become human.

Of course, in a situation like this, the Skeleton King would be far more useful as a fighting force. So instead of scolding him, I quietly sent a message through Sound Transmission.

*You know what you need to do, right?*

*You treat this body like a child.*

*Recite it.*

A curt thought came back.

*There are human eyes watching, so suppress your magical power as much as possible. And when using your power is unavoidable, make absolutely certain that no one notices.*

*Good.*

*Are you satisfied now?*

*This is enough to make you about middle-school age, not a child.*

*…How dare you, a human who is not even thirty yet. This body is an elder who has lived for over a hundred years.*

*Strictly speaking, haven’t you been dead for over a hundred years?*

“What!”

At the Skeleton King’s outraged shout, spoken aloud, I let out a quiet laugh and lowered the spearhead at an angle.

“I’ve said everything I needed to say, so go. Now.”

My voice was unfamiliar, like someone else’s, and dry as sand.

The trace of laughter that had briefly touched my lips was already gone without a trace.

I crooked a finger at the enormous monster glaring at me, its movements hesitant.

“You. Come here.”

—Grrr…

The Minotaur Lord.

A low growl escaped its maw along with an unpleasant stench.

Its blood-red eyes were already filled with wariness.

—Who. Are. You.

“Me?”

In the center of the battlefield, which had fallen into a lull with my arrival, I slowly took a step forward and continued speaking.

“The Majang-dong Spearman.[^1]”

[^1]: Majang-dong is a Seoul district known for its livestock and meat markets.

—…Strong. Hu. Man.

Most Minotaurs were cow-headed idiots who could not even count, but no matter what kind of monster it was, the higher its grade, the more its intelligence developed.

S-rank monsters in particular were creatures granted exceptional strength even among their kind.

That was why, from the moment I appeared, the Minotaur Lord had stopped moving, as if fixed to the ground.

It had already realized instinctively.

That it could never defeat me with its own strength.

“You’re pretty quick on the uptake. The fact that you haven’t charged me yet proves it.”

—…!

Step. Boom.

Two footsteps overlapped.

The Minotaur Lord, which had retreated as far as I had advanced, suddenly roared like a wild beast.

—Moooooo!

Fwoosh!

Magical power swelled around its massive body and spread into every corner of the battlefield.

At the same time, thousands of Minotaurs that had sensed something strange long ago and gradually stopped attacking flashed murderous eyes and charged.

Not at the Hunters fighting them.

At us.

—Kwooooo!

Rumble-rumble-rumble!

The earth shook beneath their monstrous cries. The Skeleton King looked at the countless herds of bulls surging in from every direction and muttered,

“But we haven’t left yet…”

“That’s why we should’ve left sooner.”

“Then can I use a little power in this situation? I think we need an army.”

“If you want to announce that you’re a monster, why not start an internet broadcast? You could rake in virtual gifts with a ‘Skeleton Army Creation’ stream.”

“Damn it. They wouldn’t listen even if I asked them to make way now, would they?”

Team Leader Choi answered the Skeleton King’s bullshit.

“Stop worrying about that and draw your weapon.”

Shing.

At the same time as his voice, a silver blade slid free. The **Hero’s Sword**, pointed toward the monsters, radiated a dazzling aura.

Then Team Leader Choi’s calm voice clearly pierced everyone’s ears.

“Get in formation.”

Clack-clack-clack!

We were not the only ones who had come to save Munich.

More than two hundred Hunters from the Ares Guild and Peace Guild had come with us as well. Though they had not played much of a role in the battle against Leviathan, they were the elite of the elite and prepared to face the enemy without the slightest hesitation.

“Please give us our orders.”

Team Leader Choi.

The Skeleton King.

Even the Hunters on the battlefield who had barely survived one crisis while continuing their grueling fight.

Everyone was looking at my mouth.

Waiting for a command from me alone.

And at this very moment, there was only one thing I could say to them.

“Kill every last one.”

Whoooooosh.

The fire dragon coiled within my lower dantian awakened and seeped into every part of my body.

Taking the crowd’s thunderous roar as my signal, I kicked off the ground with all my strength.

Boom!

A fierce wind brushed past my entire body.

Dozens of meters disappeared in an instant, and the Minotaur army charging like bulls in a fighting ring came stomping right up to my face.

No.

It was not them that had come closer.

It was me.

Whoosh.

As I exhaled, I stopped breathing and raised the spear shaft I had been holding diagonally. Powerful Scorching Yang Qi became flames and settled into the transparent spearhead.

And then…

I unleashed it.

*Right now.*

Fire Dragon Divine Spear, first form.

Fire Dragon’s Single Tail.

Whoom—fwoooosh!

A line of flame cut across the air amid a wave of superheated wind.

The energy curved smoothly like a dragon’s tail and swept across everything in front of me. It melted the horns that could pierce alloy with ease and burned through the monsters’ bones and hides.

Kaaaaaaboom!

One strike.

The flames that poured out like a wave swallowed dozens of Minotaurs, and there were no screams anywhere.

The sight of them burning black without even managing a final cry was so horrific that even the Minotaurs charging in behind them stopped their advance and faltered.

—Kwooooo!

The leader’s roar, urging its subordinates forward, could not be heard by those seized by instinctive fear.

And they paid dearly for that brief hesitation.

Slash!

Heads and limbs floated into the air with the sound of cutting flesh.

I plunged straight into their midst and went berserk.

I cleaved apart one Minotaur’s body along with the mace it had swung after belatedly regaining its senses, then struck the thick hide covering another’s chest with the back of my hand.

Crack!

With a chilling sound, its bones shattered and its massive body was flung away, disrupting the formation.

As the Minotaurs hurriedly got back to their feet, pushing away the bodies of their already dead comrades, countless spells and arrows flew over their heads.

Whish, thud-thud-thud!

Boom! Bzzzzzt!

The ones whose heads and eyes were pierced by aura-coated arrows were among the fortunate. They received relatively peaceful deaths.

Fireballs created from mana burned their hides, while electricity split into dozens of streams and poured down, lighting up every direction.

—Krrk, krrrk!

Boom! Thud.

The monsters collapsed one after another amid violent spasms. Through the acrid smoke created by the fire and electricity, a familiar face burst out first.

“Graaaaaah! You goddamn monsters!”

Whoooosh—crack!

Putting aside the natural monster-on-monster slaughter, where had he even found that?

The Skeleton King, gripping an enormous halberd, cleaved three or four Minotaurs in half at once.

And just as he was about to swing again at the ones charging in behind them, a blue aura shot through the smoke.

Slash!

With clean movements and only the minimum force necessary, Team Leader Choi opened his mouth after neatly cleaving through a neck.

“Charge.”

His voice was quiet but powerful.

The instant that single word, infused with mana, became a shout and spread through every corner of the battlefield—

“Waaaaaah!”

“You fucking bastards!”

“Kill them all! Protect our homeland!”

Thud-thud-thud-thud!

Along with the enormous roar, an army of Hunters came surging in like a wave.

It was neither as high nor as vast as the wave Leviathan had raised, but the power burning in their flashing eyes surpassed it.

The will to never let this land be taken from them.

The grief they felt for the comrades who had died here today, and the thirst for revenge they had saved for the monsters in front of them.

And at the very front of them, there I was.

Whoom—boom!

Compressed air exploded from the end of the punch I drove forward like a beam of light.

A monster whose head had vanished without a trace collapsed like a rotten log, and countless spear strikes rained down upon the enemies newly revealed behind it.

Whish-whish-whish!

I cut, stabbed, twisted, and crushed all at once.

Nothing could block the Ten-Thousand-Year Cold Iron wrapped in Force.

The spearhead that sliced through sturdy weapons like tofu split apart the owners hiding behind them as well, and despite the effects of the special debuff, my body—which had already transcended its limits—stood far beyond even the monsters.

Just like now.

—Kwooooo!

Whoooom!

A heavy roar of air being split apart bored toward my side along with the monster’s cry.

After skewering three Minotaurs like meat on a skewer, I extended my remaining hand the moment I sensed the attack.

Thud.

A fist as large as a manhole cover was blocked.

By my much smaller palm.

And with laughable ease.

—Kwo?

The Minotaur blinked innocently, like the yellow ox at Scholar Kim’s house.

I let out a quiet laugh at the absurd sight and gently redirected the force of the fist trembling against my palm upward.

Whoom!

Its fist struck the air a handspan above.

But unlike the monster, which had lost its target in an instant, the tip of my foot shot forward like lightning and struck the monster’s chest with perfect force and timing.

Crack!

With a chilling burst, its body, unable to withstand the force, was sent flying.

Far away. Very far away.

It swept away every comrade in its straight-line path.

Toward its own leader, which had been watching the entire scene from behind.

And then…

Slash! Fwoooosh!

The already lifeless body was cleaved in half. Through the blood that gushed upward like a fountain, the Minotaur Lord glared at me.

Blood-red eyes.

A double-bladed axe stained with the blood of its subordinate.

But I already knew.

I knew what was crouching deep within those eyes.

The emotion that had changed from wariness to fear was making the monster retreat step by step.

“Do you want to run?”

—…!

“Of course you might want to run. But…”

Whoooom! Crack!

Dozens of Minotaurs that had rushed in from every direction to protect their leader were flung away. At last, after the monsters had been reduced to gruesome heaps of blood and flesh, the path ahead lay wide open.

I shook the blood from my spearhead and slowly continued.

“You came here however the fuck you pleased, but leaving isn’t up to you.”

—You…!

Boom!

The belated cry was swallowed by the thunderous sound exploding from my toes.

As I erased the distance and shot forward like a beam of light, the Minotaur Lord clenched its teeth and threw its double-bladed axe.

Whoooooosh!

Darkness came rushing toward me with a roar of air being split apart.

No.

Magical power.

I had crossed the low air like a beam of light with a single push off the ground, and I twisted my body.

Whoom.

A fierce wind thick with the smell of blood brushed past the tip of my nose, and I thrust out my spear.

“Die.”

Crack!

This time, too, there was no final cry.
## Chapter artifact 761

# Chapter 761

No matter how powerful a monster was, unless it possessed regenerative abilities equal to or greater than a Troll’s, it was bound to die if its neck or heart was pierced.

Just like now.

*Whoosh!*

The neck jerked backward in a desperate attempt to evade me. But it was already too late to avoid the spearhead driving forward without hesitation.

No, my strike was simply too fast and precise for me to miss.

*Crunch!*

The spearhead dug into its throat, slicing through the flesh and bone inside before bursting out the other side.

Its eyes were wide with pain. From its slightly open mouth came the sound of blood and phlegm bubbling together.

*Grrk. Grrrk…*

What tenacious vitality.

But it was time to put a period to it.

“Goodbye.”

*Boom!*

The flames carried by the spearhead exploded. The tree-thick neck was severed in an instant, and the head launched into the air.

> **System**
>
> - Defeated **Lv. 140 Minotaur Lord**!
> - Gained a large amount of **EXP** and **Fame**!
> - **Level Up!**

As the System notification rang in my ears, I slowly turned around.

The battlefield had fallen silent.

Only moments ago, every human and monster had been locked in fierce combat. Now, they were all staring at me.

At me, standing before the corpse of the monster that had collapsed like a ruined building.

At me, who looked like hope to some and nothing short of disaster to others.

Then, toward those who had stopped as if by prior agreement, I kicked the Minotaur Lord’s severed head where it lay on the ground.

*Whoooosh—clang!*

The severed head soared high into the sky before falling into the center of the battlefield.

The kickoff announcing the second half of the battle.

No—the final overtime period.

But to get players who had been left dazed moving again, a word from the referee was necessary.

“What are you waiting for? Wipe them all out.”

“……!”

—…!

The eyes of two completely different species opened wide at the same time, but the emotions within them were different.

Joy in the humans.

Fear in the monsters.

And at the moment countless gazes filled with those different emotions left me and met one another—

“Waaaaaaaah!”

Along with a thunderous roar that made my ears ring, a wave of humans certain of victory swept over the monsters.

*Shreeeek! Crunch!*

“All of you, come at me! You fucking monsters!”

“……”

But why was that bastard always at the front?

*The monster world’s Yi Wan-yong, or something.[^1]*

I shook my head in disbelief at the sight of the Skeleton King hacking through monsters indiscriminately with a halberd, then charged toward the monsters’ already half-collapsed formation.

*Whoosh-whoosh-whoosh! Slash!*

That was right.

The battle was not over yet.

There was simply nothing left but slaughter.

* * *

The slaughter that began around sunset did not end until deep into the night.

The Minotaur army, seized by fear after losing its leader, collapsed in an instant and scattered in every direction. By then, I had somehow become the field commander, and I decided the monsters’ fate with a simple order.

“Chase them. Turn the whole city upside down if you have to.”

After that, it was hunting time.

Just like their name suggested, the Hunters became hunters and ground the already shattered Minotaur army into dust.

“You bastards!”

“This is revenge for Jonas! Kill every last one of them!”

*Whoooosh! Crunch!*

—Kaaaaaah!

They said a Hunter’s life was one where a stroke of bad luck could send you to your grave, but how many people could truly accept a comrade’s death as something ordinary?

The grief they had felt countless times that day became tremendous rage, and another name for victory was revenge.

“Minotaurs spotted! They’re moving toward the international airport!”

“What should we do?”

“Excuse me?”

“Please give us your orders!”

“……?”

I was slightly taken aback.

Setting aside the military commander in charge of the rear guard, every group had its own leader. I had no idea why they were asking me, an outsider, but giving them a simple answer was easy enough.

“What are you waiting for? Instead of wasting time asking me this, go kill them.”

“Thank you! Team Three, follow me!”

“Waaaaaah!”

“Übermensch has ordered us to slaughter every last monster!”

“Follow Übermensch! Crush their flesh and bones, and drink their blood!”

“Übermensch! Übermensch!”

“Flesh and bone! Bone and flesh!”

“……”

What the fuck. That was scary.

Judging by the shouts echoing from every direction, this wasn’t Germany anymore. It was the Aztec Empire at minimum.

Of course, there was one major difference: they were hunting invading monsters, not humans.

“Still, it would probably be better not to drink the blood…”

“What did you say?”

“Nothing. Never mind.”

Team Leader Choi looked at me strangely, wiped the blood from his face, and spoke.

“It seems most of them have been dealt with. The German Federal Army deployed the rear guard they had held back, and I hear they’re right on the verge of annihilating the rest.”

“Quite a few still escaped, though.”

“They’re tracking all of them with drones, so they won’t be able to get away.”

I nodded and asked about the most important thing.

“What about the casualties?”

“According to what we’ve determined so far, around fifteen hundred. Nearly a thousand of them are dead. The rest suffered severe injuries, but none are in life-threatening condition.”

This was a world where science and magic had merged.

Most injuries could be treated with surgery, and with healing magic and potions added to the mix, even someone who had lost a limb could recover enough to move around without difficulty within a month.

But at this moment, it was the number of dead weighing down my heart.

“A thousand…”

Far too many people had lost their lives.

Even though I had arrived as quickly as possible, even though I had fought with everything I had, I still could not prevent their deaths.

“Mr. Jin.”

At Team Leader Choi’s quiet call, I shook my head.

“I’m fine. I know what you’re going to say.”

From an objective point of view, today’s battle had clearly been a resounding victory.

We had crushed an army of nearly ten thousand Minotaurs, killed the S-rank monster leading them, and minimized our own casualties.

But suffering a relatively minor injury did not mean you felt no pain.

The Hunters hunting monsters for revenge despite being utterly exhausted were proof enough.

We had won a great victory, but at the same time, we were groaning in pain.

*For a very long time. Right up until now.*

That was what war was.

In reality, it was a painful wheel with no true victor or loser, its outcome decided by who inflicted the greater wounds.

And yet, even knowing all of that, fighting was the duty I had been given.

So was stopping the person who had reached out from an unseen darkness and begun spinning that wheel—stopped for only a brief moment—at a furious pace.

—What about him? Michael Silbert?

Team Leader Choi heard my Sound Transmission and moved his lips without so much as twitching an eyebrow.

—He’s on his way to Munich after wrapping things up in South Africa, or so I heard.

—He was a step too late this time.

—This situation was never part of the plan.

The scale of Odin Guild was truly immense.

Naturally, with branches in countries all over the world, they could respond quickly. But even so, it would have been impossible for them to achieve the kind of feat we had accomplished today.

This disaster had been brought about by using the Prophet as a tool.

To everyone else, it might look like the indiscriminate terror attack of a mad fanatic. But Michael Silbert, who had manipulated everything from behind the scenes, knew exactly when and where the terror would occur.

*The South Africa Monster Wave was probably one of them, too.*

But every situation had its exception.

I had intervened in the Munich Monster Wave, something Michael Silbert had failed to predict, and stopped the disaster before he could.

No.

At the same time, I had gained the strength to stand in his way.

The public’s support had returned.

And their trust, too.

“……”

“What is it?”

“Nothing. It’s nothing.”

I answered briefly and looked around.

A ruined city.

Corpses and pools of blood filling every street.

I suddenly felt disgusted.

Because it felt as though I had used the lives of more than a thousand people as a means to an end.

Because it felt as though I had become a monster no different from Michael Silbert or the Prophet.

But…

I had truly done my best. They could call it self-justification or a victory in my own head—I did not care.

I had worked to save as many lives as possible, and fought while gritting my teeth to prevent an even greater disaster.

And as a result, I had become the only—and greatest—obstacle in this world capable of standing against Michael Silbert.

*Open Quest window.*

*Ding.*

A familiar chime rang out, and a holographic window unfolded.

The very same Main Quest, unchanged in the slightest from the moment I had first seen it.

> **System**
>
> **Main Quest: Cataclysm**

*Cataclysm.*

I silently repeated the title reflected in my eyes.

Even after killing the Minotaur Lord—the greatest cause of this Monster Wave—and annihilating no fewer than ten thousand monsters, the System remained silent.

As if there was still a long way to go.

As if it would only finish the mission assigned to me after I had shattered all of Michael Silbert’s plans and brought him to complete ruin—or ended his life.

And it was at that very moment, while I was silently staring at the holographic window floating in the air, that—

*Whooooom.*

“……!”

I suddenly turned my head.

Far away, in the darkened sky beyond the range of an ordinary person’s vision, a faint light was approaching.

*What is that?*

A question.

A suspicion.

And then certainty.

My tangled thoughts passed through three stages before arriving at the answer.

Team Leader Choi noticed something was wrong a moment after I did and spoke in a subdued voice.

“He’s arrived.”

“Yes.”

*Crrk.*

The hand gripping the spear shaft turned white. I stared at the rapidly approaching light and muttered,

“He’s here.”

* * *

Simon, a reporter entering his tenth year in the field, was caught up in tremendous excitement and tension.

*This is a scoop. A scoop.*

The smartphone in his hand was already filled with every kind of note and provisional headline he had entered hours earlier.



An army of monsters led by the S-rank monster Minotaur Lord.

Estimated number: ten thousand. A massive force.

Central Munich. Urban warfare begins.

The battle turns against humanity. And then Jin Taekyung finally appears.

S-rank Hunter Joel Schumacher in crisis, saved by a true transcendent being. Is Jin Taekyung Übermensch?

A great victory! A scoop! Are you watching, News Director? You bastard, you’re worse than a pig’s asshole. Why am I the one getting shit for the rally being canceled because of Daniel Daisuke—

*Tap. Tap-tap.*

Simon stopped the fingers busily tapping at the screen and deleted the last note.

He had been shouted at by the news director about the rally against Jin Taekyung being canceled around half a day earlier, but his irritation eased somewhat when he remembered that the same man had sent him here.

*Yeah. I guess that can happen. Upper management has been breathing down his neck lately.*

Covering for your superior was also part of a subordinate’s duty. Simon nodded and entered a new note.



The meeting of two heroes.

Jin Taekyung and Michael Silbert. Encountering each other once again in Munich!



And just as Simon typed the final exclamation point, a powerful wind blew toward him and the countless other reporters.

*Whoooosh.*

“They’re here!”

“Is that Odin Guild?”

“It’s definitely them! That’s the Guild Master’s private aircraft!”

Shouts erupted from every direction.

Simon stared in awe as the massive aircraft slowly descended into a nearby open lot, then hurriedly moved along with the reporters beginning to surge forward like a wave.

Without imagining what would happen there today.

[^1]: Yi Wan-yong was a Korean official who collaborated with Japan during the colonial period.
## Chapter artifact 762

# Chapter 762

*Damn.*

Huginn clicked his tongue softly.

Through the specially treated windows that prevented anyone from seeing inside, the ground was slowly drawing closer—and an astonishing number of reporters were plainly visible outside.

*They really came out in force.*

Of course, it was hardly unusual.

Even in ordinary times, the name Michael Silbert was always a subject of interest for reporters. After the terrorist attacks began, they had become so desperate that the mere sight of the Guild Master’s private aircraft sent them rushing over, eyes gleaming.

But as far as Huginn could remember, there had never been this many reporters gathered at once in the past several years.

*The problem is that all those cameras are focused somewhere other than us.*

The power of the media was tremendous.

The easily manipulated masses treated cameras as their eyes and speakers as their ears.

So what would happen if, at a moment this important, every spotlight were directed at Jin Taekyung?

*It would be troublesome. Very troublesome.*

Just as Huginn muttered that inwardly and pulled his smartphone from his pocket—

“Leave them be.”

“……!”

A voice suddenly slipped into his ear, and Huginn’s heart lurched.

*How?*

After serving him for so long, Huginn already knew who that voice belonged to.

But the reason he was startled was that he had failed to sense even the slightest presence from someone standing only a few steps away.

Even though he himself was an exceptionally skilled S-rank Hunter.

“……You’ve arrived, sir.”

Michael Silbert abruptly asked after detecting the agitation Huginn had failed to completely hide in his carefully restrained voice.

“Was I that unexpected?”

Huginn thought for a moment before answering.

“No.”

“You looked surprised.”

“I was, for the first moment. But I am not anymore.”

“Why is that?”

“Because you are the Guild Master.”

“You really are a born flatterer.”

“I mean it. I’ll stake my life on it.”

“Don’t go staking such a precious life so easily.”

“It is fine. I gave my life to you long ago.”

Michael let out a quiet laugh at Huginn’s effortless reply and turned his gaze toward the window.

“It is rather noisy outside.”

“I was just about to have them dispersed.”

“I thought you might. That is what you would do.”

Then he added one short sentence.

“Still, leave them be.”

Huginn ran his fingers over the smartphone in his hand. A single phone call would be enough to send all the reporters gathered outside away.

Even if he had to use coercive methods in the process, not a single line about it would appear in the newspapers.

That was what Odin Guild was like. That was what this world was like.

But more important than anything else to Huginn was the will of the superior he served with his life.

Even so, this time, even he could not easily understand it.

“May I ask why?”

“Why?”

“Yes. Why you came all the way to Munich, where you have nothing to gain. Why you intend to meet Jin Taekyung in front of all those reporters.”

It was the question Huginn had carried with him ever since leaving South Africa.

The Monster Wave that had occurred in Munich had been entirely unexpected. By the time they launched the private aircraft, Jin Taekyung had already moved several steps ahead of them and was wrapping up the entire situation.

In short, Jin Taekyung was the star of the stage prepared for today.

“Public opinion toward Jin Taekyung has changed dramatically. The demonstrations against him that had broken out in countries around the world immediately after the Leviathan incident have all been disbanded one after another. Even the media outlets that joined hands with us are being cautious now. That is the situation we are facing, is it not?”

“So?”

“At least today, here at this location, Jin Taekyung is receiving more attention than you are, Guild Master. In such circumstances, is there really any reason to meet him and draw even more attention?”

“It sounds as though you are saying I am nothing more than a supporting act. A spotlight meant to make Jin Taekyung shine brighter.”

“……I am sorry to say this, but yes.”

Huginn lowered his head after finishing.

Though his words had come from loyalty, he lacked the courage to face the anger his superior was bound to display.

*But this is reality.*

The tide had already turned.

Michael’s Odin Guild had built an impressive record during the terrorist crisis by suppressing more than ten Monster Waves. Yet Jin Taekyung had restored his steadily declining reputation in only two battles.

There were certainly reasons for that: Leviathan’s infamy after practically ruling the seas during the Great Cataclysm, and Jin’s overwhelming victory over the Munich Monster Wave, which had occurred on a scale far beyond anyone’s expectations.

But Huginn believed there was another, more fundamental reason why public opinion had changed so easily and so dramatically.

*Yes. Jin Taekyung.*

Those who already possessed much were bound to be envied and resented before they were admired.

But to the people, Jin Taekyung was a familiar and devoted hero above all others.

A young man from a family whose circumstances had never been easy. The moment he Awakened, he had taken responsibility for his family’s livelihood, going from Gate to Gate without a single day of rest. Only a year ago, he had been living in a shabby goshiwon barely five pyeong in size, eating ramen for his meals.[^1]

That was why, even after the young, impoverished, lowest-level Hunter found everywhere in the world had seized tremendous wealth and fame, the Jin Taekyung of those days remained etched in people’s hearts.

Even when he had recklessly stormed into a massive Guild alone to take revenge.

Even when he had stained a desert red with blood to accomplish his goal.

Even when he had broken countless laws and procedures along the way, he had been able to escape with nothing more than simple condemnation.

Huginn was certain that was why.

*This world…… the public loves Jin Taekyung.*

Even when they launched an offensive using the media, Jin Taekyung’s supporters remained firmly in place. Those who had condemned him after becoming trapped in fear of terrorism collapsed like sandcastles after only one or two displays of his ability.

*Of course. It’s Jin Taekyung, after all.*

They acknowledged him.

And instead, they blamed themselves for having wavered, even if only briefly.

*This is a kind of pardon. An invisible pardon the public gave Jin Taekyung.*

The very pardon that no one but Cheon Taemin had possessed, the one Michael had worked so hard to obtain—Jin Taekyung already had it.

*That is exactly why we cannot make him stand out any more than this.*

It was at that moment, as Huginn muttered inwardly, that a slight vibration passed through the aircraft and the pilot’s voice came from the speakers installed inside.

—Landing successful. The door will open shortly. Please let me know once you have finished preparing.

“Not yet. Do not open the door. Wait until—”

“Open it.”

“……!”

Huginn hurriedly raised his head. Seeing the confusion filling his subordinate’s face, Michael let out a hearty laugh.

“Huginn, my overly cautious friend.”

“Guild Master!”

“Do not worry. I have no intention whatsoever of becoming someone else’s spotlight.”

“What does that—”

—I will open the door now. Please step away from the entrance.

*Psssh.*

Huginn’s unfinished voice was swallowed by the noise that erupted the instant the door opened, like a dam collapsing.

*Click, click-click-click!*

“Michael! Michael! Please look this way!”

“We’re from TBC Broadcasting! Just a few words, please!”

“I understand this is your second meeting. What kind of relationship do you normally have with Mr. Jin?”

“Now that nearly every crisis has been resolved, why did you specifically come to Munich?”

“What do you think of Mr. Jin’s performance?”

“According to the German government’s announcement, the Munich Monster Wave was nearly ten times the size of the one in Cape Town! Given that, don’t you think the Cape Town wave took far too long to suppress?”

Huginn’s face hardened as flashes burst without pause and the reporters shouted out their questions.

As expected.

Most of the questions being thrown at them revolved around Jin Taekyung. One audacious reporter had even gone so far as to compare them.

“……Even if the Guild Master has something in mind, it would be better to postpone the interview for now.”

But at Huginn’s words, Michael calmly shook his head and strode toward the entrance.

With a single remark that seemed to have nothing to do with the current situation.

“I watched the video you obtained in Japan. It was very interesting.”

“Pardon?”

“Let us go. We cannot keep him waiting any longer, can we?”

*Step.*

Michael Silbert strode down the private aircraft’s stairs without hesitation and stood tall before the countless cameras and flashes.

Then, spotting someone approaching over the shoulders of the reporters clamoring for a scoop and the German Federal Army soldiers holding them back, he broke into a broad smile.

“At last, the young hero has arrived.”

*Flash!*

The night was illuminated by the most dazzling burst of flashes yet.

As countless reporters hurriedly parted with gasps of admiration, the two heroes slowly approached each other and finally stood face-to-face.

“Here we are, meeting again, Jin.”

*Slide.*

Along with the greeting delivered in a warm voice, Michael extended his hand.

Jin Taekyung silently stared at the enemy’s smiling face before accepting the handshake.

His voice was low and hoarse, almost as though it were boiling.

“……Michael Silbert.”

*Crack.*

The hands clasped tightly by the two men turned white.

* * *

Everyone lives behind a mask of their own.

For the sake of getting along in society. For the sake of earning a living. Or to avoid pointless fights.

But the mask worn by Michael Silbert was harder and thicker than any I had ever encountered.

I could not even begin to guess what might be hiding behind it.

*Crack.*

The bones in our clasped hands shifted with a grinding sound. Feeling the force transmitted through his grip, I widened my eyes.

*What the hell……?*

His grip strength was unbelievable.

Of course, with all those eyes on us, I was not using my full strength either. But I could not hide my surprise at the force of his hand, which far exceeded anything I had expected.

*How?*

My physical abilities, enhanced through the System, were superhuman in the truest sense of the word.

That was why neither a Supreme Peak master nor an S-rank Hunter could approach me in pure physical ability.

No. That was what I had thought.

Until I clasped his hand.

—This seems like enough of a greeting. Don’t you think?

“……!”

—We’re in front of the cameras. It would be better for both of us to be a little more careful.

I came to my senses belatedly and looked around.

We had already been standing there holding hands for dozens of seconds, and several reporters were eyeing us suspiciously.

“Ah.”

“My friend here must be very happy to see me. I feel the same way.”

*Pat, pat.*

The reporters smiled faintly at Michael as he tapped my shoulder with a friendly smile.

But between him and me, a private conversation was taking place—one that their cameras and microphones could never capture.

—What the hell are you playing at?

—Who can say? I do not understand what you mean. Is coming to congratulate a young junior on his victory some kind of trick?

—Even a passing dog would laugh at that. You son of a bitch.

—You really refuse to believe me.

—Sorry, but I’m not that much of an idiot. You’re already a step too late.

Michael Silbert let out a quiet laugh and moved his lips.

—Actually, you’re right. I came here to make a very important announcement.

—An important announcement?

—Yes. An announcement that will turn this entire world upside down.

—……What?

What the hell was he talking about?

I stared blankly at him in response to his unexpected words.

Then, all at once, Michael Silbert wiped the smile from his lips and looked straight into the cameras.

And then…… he hurled a bombshell at the world—something no one present had expected.

[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement, often with shared facilities.
## Chapter artifact 763

# Chapter 763

A thought is only a thought until it becomes reality. But the moment it forms a complete sentence and flows out as a voice, it gains influence.

Just like now.

“I have witnessed countless deaths throughout my life.”

A sorrowful voice rang out. Standing tall before countless cameras and microphones, Michael Silbert slowly continued.

“In the slums of Paris, teeming with flies and gangs. On the countless battlefields of the Great Cataclysm. And ever since the day of victory when the Demon King Asmodeus fell. I have continued to witness them.”

*Bzzzz.*

The faint noise of cameras operating sounded unusually loud.

In the silence, where not even the sound of someone swallowing could be heard, the reporters gazing at Michael Silbert had eyes gleaming with inexplicable anticipation.

*This is…*

*There’s something more!*

At first, they had wondered if he had suddenly started spouting nonsense.

All they had wanted was a friendly two-shot of two heroes—one old enough to be the other’s father—standing with their arms around each other’s shoulders, along with a few warm words.

The main character of today’s event was undoubtedly Jin Taekyung, while Michael was merely a reliable lighting fixture whose job was to illuminate him more brightly than anyone else.

At least, that was true until Michael opened his mouth.

“Yet even after witnessing so many deaths, there was one hope I could not bring myself to abandon. I had a dream. Now that the Demon King Asmodeus and his monster army were gone, I believed that all conflicts would eventually end and complete peace would arrive.”

His tone rose and fell distinctly, and his expression was filled with appeal.

Michael Silbert’s appearance, compelling everyone who saw and heard him to focus, was reflected in the camera lenses.

People watching the entire scene live naturally leaned closer to the televisions in their living rooms, their computer monitors, and the smartphones in their hands.



“Mom. Dad. I have to watch my cartoon…”

“Shh. Be quiet for a moment, Peter.”



- Ah, what the fuck is that crazy bastard No Jaehun doing? I called for a gank, but he never came, and now he’s gone AFK as hell.

- Why? Did he get into a fight with his girlfriend? Is this game heading for a surrender?

“It’s not that. I was watching an iTube live stream for a moment. Never mind. I’ll post the link in the group chat. You guys should take a look, too.”

- What the fuck? That bastard doesn’t have a girlfriend. He’s just not in his promotion match, so he’s being a total—Munich live? What is this?



Dozens of television channels and internet streaming sites broadcasting live around the world lit up with activity, and the number of viewers multiplied exponentially as they watched the screens, holding their breath.

The image of grim-faced Jin Taekyung and Michael Silbert, standing one step in front of him as he continued speaking, passed through the camera lenses and into countless eyes.

Along with a powerful voice that drilled into everyone’s ears.

“After a long period of waiting and hesitation, I stand before you today. To tell you this one thing. For our faith in peace and for a better future.”

After pouring out that speech, Michael Silbert caught his breath.

No—everyone watching him did the same.

And then, in the next moment, a voice as dry as scattered grains of sand slipped between his lips.

“Now, a second war is approaching.”

“……!”

“……!”

Invisible agitation and shock waves swept through every direction.

The office worker sitting on the sofa after work and mindlessly switching through television channels. The affectionate couple walking beneath a huge electronic billboard that decorated the street. The teenager watching a live stream to kill time with his game paused.

The reporters witnessing and hearing everything at the scene were no different.

At that moment, they doubted their own eyes and ears before falling into extreme confusion.

A second war.

No one was ignorant of what that short phrase meant. A groan-like voice slipped from someone’s lips.

“The Great Cataclysm…?”

How could they not know?

The clearest nightmare humanity had ever known, a memory etched into them as terror.

The worst great war in human history—the one that had covered the Five Oceans and Six Continents in blood and corpses.

And now Michael Silbert was saying that very Great Cataclysm would begin again. He was declaring that a second war had arrived.

Before them.

No—in front of the entire world.

*This… This is impossible.*

*It can’t happen. It can’t.*

But unlike the denial that immediately rose in their minds, their lips refused to move easily.

More precisely, they were paralyzed by one thought that had struck them at the same time as their denial.

*What if everything he’s saying is true?*

A second Great Cataclysm.

It was something that could never happen—and must never happen.

Yet people had a vague suspicion. Deep in their hearts, they were feeling out the shape of the anxiety writhing within them.

There had already been enough signs.

Magical power levels rising day by day. Abnormal phenomena occurring more frequently as time passed.

Only a few months ago, an Arch Lich had emerged in Sichuan Province, China, while monster-wave phenomena using Magic Gems had occurred one after another throughout the world.

Methods of terrorism like these had already been studied by academia long ago, but the leading scholars in the field of magical power had all insisted as one that it was impossible.

At least for now.

Unless magical power levels reached their limit.

And today, Michael Silbert was announcing that they had reached precisely that limit.

“Perhaps the expression ‘second’ is incorrect. But one thing is certain: what I, along with all of you, believed was the end of the war was nothing more than a ceasefire.”

“……!”

“I say this here today. The magical power distributed throughout the world we live in has already broken through its critical point, and a disaster like the one in the past will descend upon the entire world.”

People could no longer even breathe properly.

This was not the rambling of a drunkard idly wasting time in a neighborhood bar.

Michael Silbert. A hero who had fought brilliantly from the time of the Great Cataclysm until today, and the leader of the world’s greatest Guild—a giant making a declaration.

Among the reporters unable to recover from the shock, someone asked in a trembling voice,

“D-Does that mean the Demon King—the Demon King Asmodeus—is coming back?”

“On the Day of Victory, during the final battle that decided humanity’s fate, the Demon King was undoubtedly erased without leaving so much as a trace. I saw it clearly with my own eyes, so that is an indisputable fact. However…”

Michael Silbert hesitated briefly before adding one sentence.

“Now, no one can be certain. No one can be certain what will happen in the future, or even whether the Demon King Asmodeus was truly erased.”

“Ah… Ahh.”

“How could this happen…?”

The cameras trembled slightly, and the reporters’ sighs mixed into the microphones before being broadcast in their entirety.

But no one watching the scene on a screen from wherever they happened to be complained or paid any attention to it.

Their situation was no different from that of the people at the scene.

Without realizing it, they were trembling at the truth they had pretended not to see because they lacked the courage to face the terror that had finally revealed its true form.

A future no one could predict anymore.

No—a disaster.

And the fear of the terrifying being known as the Demon King Asmodeus returning.

Feelings like dark storm clouds gnawed away at and devoured people’s minds.

The eyes of those staring at Michael Silbert—whether through a screen or with their own eyes—trembled at his prediction of disaster.

They wanted him to take back everything he had said so far. They even clung to the absurd hope that he would laugh and say it had all been a joke.

But Michael Silbert’s next words utterly crushed the last handful of hope remaining in their hearts.

“Peace—or the time we believed was peace—is over.”

Michael Silbert stared into the camera. The sorrow and anger flowing from him were so vivid that they seemed tangible.

At least, that was how it appeared to the people watching.

“The war has already begun, and we must stand and fight without the slightest hesitation or retreat.”

His voice trembled between his lips like a wave. Michael Silbert poured out his words as though sobbing, as though pleading, then clenched his teeth.

“Together! United more firmly than ever!”

A gaze like flame poured from his reddened eyes, and a thunderous cry rang through the microphones.

The cameras no longer showed Jin Taekyung. The dazzling lights and spotlights were directed at only one person.

Michael Silbert.

In the eyes of the people, he looked like a fighter filled with determination.

No—in his own mind, he was already a hero and a king.

A hero who had shown people in crisis a new path.

A sovereign who would reign over this world.

And amid the trembling air and countless gazes, Michael Silbert took his final step.

He spoke the words he had been waiting to say for this very day.

“The World Hunter Federation.”

At that single phrase, everyone swallowed.

The air and wind stopped.

The overwhelming aura radiating from Michael Silbert crushed everything around him.

“A federation encompassing every country in the world, subject to no restrictions. The resurrection of that very World Hunter Federation that saved us—all of humanity on Earth—from the disaster known as the Great Cataclysm…”

His voice trailed off.

Michael Silbert’s eyes shone fiercely.

He gazed at the hundreds of millions, perhaps billions, of people watching him from every corner of the world, then exhaled the breath he had been holding.

“I dare to propose it here today.”

“……!”

“……!”

The resurrection of an international organization transcending every law and restriction.

At those words, an unseen wave swept across the crowd.

It burrowed into every corner of the world through cameras and microphones, through countless broadcasts.

And just as everyone watching the scene was seized by an immense shock and inexplicable emotion—

“Go fuck yourself.”

A single voice rang out, shattering it all.



* * *



Hundreds of reporters.

The German Armed Forces and police officers controlling them.

And the other Hunters who had arrived at the scene late.

An uncountable number of eyes were turned toward me.

Beyond the gleaming camera lenses, it felt as though unseen gazes and voices were pouring over me like waves.

But I did not care about any of it.

No. More accurately, I was incapable of caring.

*So this was it.*

The shock felt like I had been struck in the back of the head, and my vision reeled.

Inside my mind, which looked as though a kindergartner’s playroom had been turned upside down, the words I had just heard rang out with perfect clarity.

*The World Hunter Federation.*

Now, roughly thirty years later, the remnants of those old heroes remained under the name International Hunter Federation.

Age, gender, nationality, and race.

They had even transcended the law to follow the savior Cheon Taemin. That organization of Hunters had been the World Hunter Federation.

They had fought solely for humanity’s survival, winning victory after spilling countless drops of blood. And immediately after the Demon King Asmodeus fell, they had returned to their respective places.

*But he’s going to resurrect that very World Hunter Federation?*

Of course, I respected the people who had fought back then, just like everyone else.

Because they had fought for everyone.

And because they had relinquished that incredible power and walked away without regret as soon as the war ended.

But this was different.

The World Hunter Federation Michael Silbert dreamed of was nothing more than a kingdom built for one man.

That was why, at this very moment, I could say it once more in front of everyone watching.

“Go fuck yourself.”

“……!”

“……!”

And just as the people who had been doubting their own ears opened their eyes wide, a quiet voice rang in my ears.

It shook my mind once again.

—Think it over one more time before you speak.

Michael Silbert.

The man who had driven this world into crisis and intended to use that crisis as a staircase to climb onto the throne.

An unscrupulous schemer wearing a hero’s mask was looking toward me with a smile.

His snake-like eyes glimmered as he looked at someone over my shoulder.

—If only for the sake of your monster friend.
## Chapter artifact 764

# Chapter 764

For a moment, it felt as though the world had stopped.

The hundreds of people staring at me with their mouths hanging open. The cameras and microphones poking up between them. The dazzling lights illuminating the wide-open lot instead of the moonlight.

Everything around me grew slower and blurred at the same time.

Everything except the one person who had brought my world to a halt.

Michael Silbert.

An unscrupulous schemer unlike anyone I had ever seen was staring at me.

His eyes, always calm and subdued, now held unmistakable laughter and triumph. The voice that once again burrowed into my ears was perfectly clear.

—You seem rather surprised.

I came to my senses at those words and belatedly steadied my breathing.

*A painful mistake.*

No matter what he said, I could not let him see me shaken.

The moment I showed an opening to an enemy, my weakness would be exposed. And when that enemy was Michael Silbert, I had to be even more careful.

*It’s not too late. As far as I know, the Skeleton King’s identity is perfectly secure, and he still hasn’t produced any evidence.*

I had to keep my composure from this point onward. If I could respond properly without being rattled by whatever he said next…

*Damn it.*

*Crack.*

The sound of bones shifting rang out from my tightly clenched fist.

No matter how much I reassured myself, it was already too late. From the moment my eyes met his gray ones, my instincts had been screaming.

That his previous remark had not been a simple probe.

That Michael Silbert had not come here with a guess, but with certainty.

And the voice that followed put a period at the end of that thought.

—You have two choices now. Ah, of course, you don’t really have much of a choice, but listening to them for fun shouldn’t be too bad.

His tone and voice were relaxed. With his back to the cameras, Michael Silbert moved his lips with a more pleased expression than ever.

—The first is that your friend’s identity is revealed in front of the entire world. The second is that you leave this noisy place and have a private conversation with me, just the two of us.

—……!

—So, what will you do?

*Damn it.*

At the curse that slipped out in a whisper, the bastard gave me a faint smile and approached.

*Brush. Pat.*

Just as his slowly extended hand brushed the dried blood and dust from my shoulder, the reporters who had finally come to their senses belatedly released the shouts they had been holding back.

“Mr. Jin Taekyung! Did your statement just now mean that you oppose the World Hunter Federation?”

“W-Wait! Please tell us the exact meaning of your profanity!”

“Mr. Jin!”

*Click. Flash-flash-flash!*

Flashes erupted from every direction as the cameras kept rolling.

Amid the waves of noise pouring out as the dam of silence collapsed, Michael Silbert quietly raised a hand to calm the crowd before speaking.

“My friend here is already a hero watched by the entire world, but he is also still a young man full of youthful vigor. He must be exhausted after all the battles and incidents he has faced recently, so I ask for your understanding.”

“Are you saying that Mr. Jin is suffering from post-traumatic stress disorder?”

“Well, I’m sorry, but let us discuss that another time. There is only one thing I wanted to tell you all here today.”

Michael Silbert continued, staring into the cameras.

“The war has begun again, and for humanity to survive the coming flood of blood, we need an ark known as the World Hunter Federation.”

“……!”

“That is all. I hope you all have a pleasant evening.”

Those were his final words.

Leaving the reporters shouting behind the German Armed Forces and police officers who blocked their way, Michael Silbert turned and walked toward his private aircraft, which had landed in the center of the open lot.

Along with a short remark only I could hear.

—I’ll be making coffee for you, so I hope you won’t be late.

*Grind.*

My teeth clenched on their own.

I already knew why he had left me those words.

“Mr. Jin!”

“Mr. Jin Taekyung! Please, just give us a statement!”

As I turned away from the cameras as though fleeing, I saw two figures rapidly approaching.

Their expressions were mixed with confusion and shock, and their voices were low enough for only me to hear.

“We’ve been played. This was what it was all for.”

“Damn it, what the hell is this mess? What’s this World Hunter Federation thing, anyway?”

I remained silent despite the two of them firing off their words like rapid gunshots.

*What should I say?*

*Where should I even begin, and how should I explain it?*

After wrestling with all those questions, one person’s face suddenly came to mind.

“Magic Johnson.”

“What?”

At the name that abruptly slipped out, the Skeleton King frowned.

“Why are you suddenly bringing up that man? Before that, what exactly is going on here… Wait, is there something on my face?”

I had been staring blankly at his face without even realizing it. I shook my head.

“……No. Nothing at all.”

I still was not certain.

Whether I should tell him what had just happened. What choice I—or we—should make.

But some emotions could not be hidden simply because one wanted to hide them.

Only then did Team Leader Choi belatedly realize that something was concealed beneath the surface. His face hardened, and his lips moved.

—What is it? What happened for you to suddenly ask for Mr. Johnson?

—…….

—Tell me. Right now.

The thoughts tangled inside my head were long, but their wait was short.

After several dozen seconds that felt like an hour, I sent my voice toward Team Leader Choi through Sound Transmission.

—The Skeleton King’s identity has been discovered.

—……!

—Contact Magic Johnson. I need everything he has found through his investigation so far, based on the materials taken from the hideout of the late Siegfried Wassman, along with every piece of information concerning Michael Silbert. Everything. Do not leave out a single thing.

His eyes trembled.

Team Leader Choi remained silent as though he had lost his voice, then slowly nodded. I took a deep breath and began walking.

The open lot had already emptied of people.

Toward the enormous private aircraft standing at its center like an impregnable fortress.

And toward the one person waiting for me inside.

*Michael Silbert.*

Yes. The bastard was right.

The war had already begun.

* * *

Michael Silbert kept at least one promise.

“Come in.”

When I stepped into the private aircraft’s spacious, suite-like interior, the first thing I saw was a coffee cup sitting on the table.

The beans must have been brewed only moments ago. The aroma was rich, and beyond the steam rising from the cup, gray eyes somewhere between darkness and light were staring at me.

“Fortunately, you came quickly. I was worried the coffee might get cold.”

I sat down and quietly looked at the full cup. As the silence stretched on, Huginn, who had been standing at attention behind him, spoke.

“If it does not suit your taste, shall I prepare a different coffee for you?”

His tone was polite, but the words were filled with mockery and sarcasm.

I did not bother to respond. Instead, I took my eyes off the cup and jerked my chin toward Michael Silbert.

“I won’t say anything about keeping a pet, but hearing a crow caw over and over is really getting on my nerves.”

*Whoosh.*

The air grew heavier, accompanied by a faint noise that pierced my ears.

I spoke to Huginn, who had taken another step closer behind me.

“If you don’t want to walk on your arms from today onward, get back where you were. Shut your mouth before I rip it open.”

“……!”

“What? You think I can’t do it?”

My voice was directed at Huginn, but my eyes remained fixed on his master. Michael Silbert had been looking at me in silence when he blinked.

“You’re serious.”

“I am.”

“You would cripple Huginn right in front of me?”

“I might kill you both.”

An ordinary person probably would not have been able to endure such a taunt.

If they knew my fatal weakness, they might have threatened me with it. If they were a powerful person I could not afford to let my guard down around, they might have tried to threaten me physically.

But Michael Silbert was different.

He met both conditions, yet he was also the sort of person who belonged to neither category.

“Huh.”

Michael Silbert let out an exclamation whose meaning was unclear and stared at me with interest.

“Setting aside whether you could succeed, isn’t that rather reckless?”

“If I had been cautious, I wouldn’t have made it this far.”

At my immediate answer, he let out a quiet laugh.

“Yes, that is true. The last few years of your life, as far as I have observed them, have been nothing but a series of reckless acts. That must be how you gained the public’s love and trust.”

“Who knows? Could it really be only that? There must be things even you failed to see.”

“I once heard there was a saying in the East called empty bluster. Let us not waste time with meaningless words. I already know everything about you.”

He was wrong.

Michael Silbert knew nothing.

He did not know what kind of life I had truly lived, or how much recklessness it had taken to overcome every crisis and survive until today.

That was a secret no one in this world could even guess at, and a weapon that would one day become a dagger driven into an enemy’s heart.

Michael Silbert had no way of knowing that. When I let out a quiet laugh, the smile at the corners of his mouth disappeared.

“Why are you laughing?”

“Because I’m enjoying this situation.”

“Then does the situation you are enjoying include the fact that the Stone King’s identity is that of a monster?”

He was clearly trying to shake me, but once had been enough. I had no intention of being thrown into such an undignified panic again.

If anything, someone else was more unsettled by his words than I was.

At the movement trembling behind me, I shrugged.

“It seems that friend didn’t know.”

“Now he does.”

“He’s been getting on my nerves for a while, so I couldn’t say anything.”

“Leave now, Huginn.”

After a brief hesitation, the loyal retainer bowed and exited the private aircraft. His master then opened his mouth.

“As you already know, I could have revealed everything in front of the cameras.”

“Yeah.”

I nodded readily.

“And one of us would have been finished by now.”

“That’s right. But I didn’t. Do you know why?”

“Because you were scared shitless?”

*Clink.*

The teaspoon Michael had been gently stirring through the coffee stopped.

His gray eyes stared straight at me.

“You really are… a unique person.”

“And you’re a real fucking bastard.”

Honestly, I had no idea whether this was the right move.

But even a rat backed into a corner bites the cat.

Michael Silbert was formidable enough that even calling him a tiger would undersell him, but at least right now, I was the Blazing Flame Divine Dragon.

*Hiss.*

Terrible heat surged through the palm I had placed on the table. As vapor billowed up, overpowering the steam from the coffee cup, I whispered in a low voice.

“Go ahead. If you’re ready to die.”

# Checkpoint Review — 975–979

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

# Chapters 975–979

## Plot

Jin Taekyung kills Jamukha, then joins Jeok Cheongang and the Bow Saint to defeat Murong Baek, the North Heaven Demon Lord. Before dying, Murong reveals that the Lord of Heaven has awakened and warns that a war has begun, with at most half a year remaining. Elsewhere, an unnamed being awakens, sensing the fall of the fourth heaven and the loss of another faithful servant.

The Jin Family of Taiyuan arrives to reinforce the battered Hebei Peng warriors. Taekyung displays Murong and Jamukha’s heads, and Jin Wikyung offers the nomads surrender. Temur submits to Wikyung, but the battle against the Murong Family resumes. In a memory, Jin Mukyung recalls his childhood and his father apologizing after Mukyung’s mother died in childbirth. As the memory fades, a familiar voice asks if he is awake.

## Continuity

- Murong Baek and Jamukha are dead. The battle against the Murong Family resumed after Jin Family reinforcements arrived; its outcome is unknown.
- Temur submitted to Jin Wikyung as his lord.
- Murong Baek said the Lord of Heaven had awakened, the war had begun, and at most half a year remained.
- An unnamed being in the darkness sensed the fall of the fourth heaven and the disappearance of another faithful servant; its identity and awaited day remain unknown.
- Jin Mukyung recognized his father in a childhood memory; a familiar voice asks if he is awake, but the speaker is unidentified.
- The conditions of Cheol Mubaek, Wipeng, and Peng Cheolhu remain unknown.
- The Emperor remains gravely ill with Blood Soul Gu; the treatment said to require him to die once remains unresolved.

## Translation Decisions

- Keep Taekyung’s mocking nickname 뽀삐 as “Poppy”; it is not an established name.
- Render 이룡신창 as “Divine Spear of the Imugi” and 모용위진 as “Murong Wijin”.
- Record Temur’s deferential address to Jin Wikyung as “my lord,” and Wikyung’s formal address to Temur as “you.”

## Durable state

{
  "active_continuity": [
    "Temur submitted to Jin Wikyung and the Jin Family of Taiyuan as his lord.",
    "The battle against the Murong Family resumed after the Jin Family’s reinforcements arrived.",
    "Jin Mukyung recalled his childhood and his father’s apology following his mother’s death in childbirth.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment said to require him to die once remains unresolved.",
    "The conditions of Cheol Mubaek, Wipeng, and Peng Cheolhu remain unknown."
  ],
  "continuity_sources": [
    979
  ],
  "open_questions": [
    "What does the Lord of Heaven intend, and how will the war unfold?",
    "Who is the being in the darkness, and what is the day it has awaited?",
    "What are the conditions of Cheol Mubaek, Wipeng, and Peng Cheolhu?",
    "Can the Emperor be treated for Blood Soul Gu, and what does the treatment requiring him to die once entail?",
    "Who spoke to Jin Mukyung as he awoke?"
  ],
  "safe_through": 979,
  "temporary_decisions": [
    "Render Taekyung’s mocking nickname 뽀삐 as “Poppy”; it is not an established name."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 975

# Chapter 975

No matter how well trained a hunting dog was, it couldn’t take down a predator on its own.

The difference in what they were born to be was unavoidable.

But Jamukha was different. Born a predator, he had become a hunting dog to achieve his own ends.

He was a trained beast.

He possessed both the strength of a predator who could face any enemy and the loyalty of a hunting dog.

That was why, the moment he heard his master call, he could throw himself into action without a second’s hesitation.

“Jamukha!”

The signal he’d been waiting for came, and Jamukha immediately unleashed his curved blade with all his might.

*BOOM!*

Two waves of Force collided in midair.

The dark green Force of his blade, made darker and larger by the effects of the Temporary Strength Pill, pushed back the blue-white flames, if only for a moment. Just then, Jamukha’s foot shot forward like an arrow.

*Whoosh.*

His figure blurred in an instant.

With Shifting Form and Position, unleashed in the space of a heartbeat, Jamukha became a streak of wind and crossed more than a dozen *zhang*.

He was heading for the Fire King—a predator more ferocious and powerful than any quarry he’d ever faced.

*One strike. One strike is all it takes.*

Near-certainty filled Jamukha’s movements, and it was no baseless boast.

For more than fifty years, he had pursued nothing but the utmost speed, honing his martial arts to counter the Hebei Peng Family’s overbearing style.

Jamukha had no doubt that even Jin Taekyung, called the Divine Dragon, had his limits. He couldn’t make up for the difference of all those long years.

And besides…

*With this power, I can do anything.*

Everything had changed. It was as if he’d shed a layer and been reborn like a caterpillar emerging as a butterfly. The whole world looked new.

His feet, skimming over the ground, and the beloved weapon gripped in both hands felt lighter than ever.

The Temporary Strength Pill had drawn out every ounce of his power and then some. Even now, it seethed ceaselessly in the depths of his body.

His sixth sense, opened beyond the five, let him easily evade even a single streak of flame striking from behind.

*Shweeeee!*

Jamukha increased his speed and turned his head. A spearhead that had left Jin Taekyung’s hand tore through the air, grazed the back of his neck, and buried itself in the cliff face.

*KABOOM!*

Sharp fragments of rock flew in every direction. Jamukha leaped over the rising cloud of dust, his figure rushing onward as if erasing the wind itself.

*I’ll bring him down. No matter what.*

The resolve in Jamukha’s heart wasn’t the loyalty of a hunting dog toward its master.

No—he couldn’t have called it loyalty from the start.

It hadn’t come from his heart. The other man’s strength and his own ambitions had simply combined to force him into submission.

But that was enough.

Even if his loyalty was false and feigned, the North Heaven Demon Lord had promised him a sure reward. The power of Dark Heaven was enough to make him king of the steppe and ruler of the north.

And right now, Jamukha’s mighty downward slash was bringing him one step closer to his grand ambition.

*Shwack.*

In the slowed world, Jeok Cheongang’s back remained turned to him, as if he couldn’t even react. Still facing the North Heaven Demon Lord, the old man was utterly exposed.

Dark green Force, arriving before its own sound, filled Jamukha’s eyes.

*It’s over.*

Jamukha was certain of it.

No one could dodge this strike.

Even if his opponent was the giant known as the Fire King, Jeok Cheongang, the outcome would be the same: death.

But it took only a heartbeat for that certainty, which had appeared like an exclamation point, to turn into a question mark.

*Fwoosh.*

A terrible heat suddenly washed over him from behind.

At the same time, someone’s fingertips flashed out and touched Jamukha’s long hair, braided into a queue in the custom of the steppe.

No—by the time he felt them touch, his head was already being wrenched backward.

*Grab.*

A hand seized his hair with brutal force. His upper body bent backward, and the curved blade in his grip wavered off its original course.

Amid the sudden pain and shock, Jamukha finally understood why Jeok Cheongang hadn’t even turned his head in the face of such danger.

*He wasn’t unable to react.*

No doubt about it.

Jeok Cheongang had known from the beginning.

No—he’d trusted him.

His one and only Disciple.

His Disciple’s might, something no number of years could measure.

*Whoosh!*

The dark green Force skimmed past Jeok Cheongang’s head by a hair and slashed through empty air.

A quiet voice reached Jamukha’s ear as he clenched his teeth against the pain and frustration.

“Nice braid.”

“……!”

“Looks easy to rip right off.”

*Krrk, krrrunch!*

The world before Jamukha’s eyes turned white.

The pain of having his hair and scalp torn off together drew a silent scream from him. He spun around and swung his curved blade.

*Whoooosh!*

The dark green Force hadn’t died out despite his terrible pain. If anything, it surged even more fiercely, tearing through space.

A blade technique perfected over more than half a century, its speed unsurpassed.

But Jamukha had no idea.

More precisely, he could never have anticipated it.

That the strength and speed with which he’d subdued the vast steppe in a flash were inferior to the enlightenment and rewards Jin Taekyung had gained over the past two years, constantly crossing the line between life and death.

*Poom!*

Flame Divine Palm.

The tremendous blaze swept in at that instant, burning even the air. Jamukha’s upper body lurched. Heat beyond anything he could imagine burned through and ravaged the acupoints all over his body.

*Ah.*

Through his fading vision, Jamukha swallowed the blood surging up from deep in his dantian.

But even as he endured that horrifically powerful strike, he could still feel a spark of hope that hadn’t gone out.

The Temporary Strength Pill.

An inexhaustible source of power.

The wellspring of vitality keeping Jamukha’s body upright, though it should have already crumpled.

*Not yet. Not yet…!*

Jamukha gritted his teeth.

With all his might, he tightened his grip around the hilt as it began to slip from his hand and drove the blade toward Jin Taekyung’s chest.

*Ka-drrk, crack!*

Two opposing sounds mingled in midair.

And then—

“Ah, that hurt like hell.”

Looking at Jin Taekyung, who was drenched in dark red blood and groaning in pain, Jamukha forced out a question.

“How…?”

His voice broke apart like stepping-stones in a stream.

He couldn’t understand it.

Setting everything else aside, he genuinely wanted to know.

How had Jin Taekyung blocked that strike?

What kind of sorcery had he used to make a red-tinged suit of armor appear over the bare skin that had been showing through his tattered clothes just moments ago?

“This… *cough*, this doesn’t make—”

*Krrrunch.*

His voice scattered with a silent scream.

Twisting the five fingers he’d driven hooklike into Jamukha’s flank, Jin Taekyung answered with a tired expression.

“Why don’t we both make this easy and get it over with? Why are you so damn stubborn? I was saving this for later.”

What did he mean?

How was any of this possible?

With his unanswered questions, Jamukha tightened his grip as if in a daze.

He’d forgotten that the Force, once surging like waves, and the blade, once so razor-sharp, had both dulled and died away.

*Scrape. Clang.*

At last, the curved blade failed to pierce Fire Dragon Armor. It scraped across the armor’s surface, as if giving voice to its owner’s regret, then slipped from his hand.

*Poom.*

With another burst of heat from Flame Divine Palm, Jamukha heard an explosion reverberate from deep within his body.

“Guh—!”

His vision dimmed. His ears went muffled.

Everything felt strange, as if it belonged to someone else.

It seemed so far away, like he was watching from hundreds of miles off.

The heat of blood spilling from his lips. The shouts that could only belong to the North Heaven Demon Lord.

And yet one thing remained vivid.

The blows that kept pounding and breaking his body.

*Poom. Poom. Pooom.*

Jamukha’s figure staggered. Even as he was battered by terrifying force, he couldn’t even step back.

Amid pain so intense it felt as if his soul were burning white, the five fingers buried in his flank held his body fast like a hook.

One punch, one palm strike—each carrying terrifying power—filled his vision, raining down in a blue-white torrent.

They kept coming until everything the Temporary Strength Pill had given him was spent.

Until the vast sea of power, which had seemed as if it would spring forth forever, had dried up.

And at some point, Jamukha realized he couldn’t feel any more pain.

*Thud.*

Like a leaf falling at the end of autumn, Jamukha crumpled.

His eyes weakly rolled upward. Reflected in them were the endless, dark night sky and Jin Taekyung, standing tall as a giant.

*You… What are…*

What are you?

With that unfinished thought, Jamukha’s world tilted.

*Thud.*

The heat rose like a wavering haze. Jin Taekyung looked down at the King of the Steppe, blackened and lifeless, then let out a breath he’d been holding.

*Hoo.*

A quiet sigh.

But despite unleashing one powerful strike after another, each infused with tremendous internal energy, his lips, which had gone white, were beginning to flush red.

As if time were running backward.

As if everything that had been spent and worn away were returning to its original state.

*Ding. Ding. Ding.*

> **System**
>
> You have defeated Lv. 173 Jamukha!
>
> You have gained a tremendous amount of EXP!
>
> You have gained a tremendous amount of Fame!
>
> Your Fame makes the Great Steppe tremble!
>
> .
>
> .
>
> .

Clear chimes rang in only one person’s ears as translucent letters filled the air.

At the end of them were the words he’d been waiting for so long.

> **System**
>
> Level Up!

“Now I’m finally feeling alive.”

Feeling the well-timed stroke of luck through his whole body, Jin Taekyung trembled.

Then, over Jeok Cheongang’s shoulder, standing firm as Mount Taishan, he smiled at the North Heaven Demon Lord, who was staring at him with wide eyes.

“There were two of you. Now you’re alone.”

*Crack.*

The North Heaven Demon Lord clenched his teeth hard enough to break them, then forced Jeok Cheongang back with all his might.

*Krrrunch! Bang!*

With a tremendous clash of power, the two figures were flung in opposite directions.

Rather than slow himself to absorb the shock wave, the North Heaven Demon Lord used it to speed up his retreat. Jeok Cheongang immediately saw through his intent and shouted.

“You—!”

But the North Heaven Demon Lord didn’t stop.

He cut through the wind and seemed to erase the space around him as he shot toward the narrow gorge’s exit.

*Shweeeee! Boom!*

The massive rocks filling the gorge shattered with a casually thrown punch. Then, toward the people of Shanxi who were unable to advance because obstacles blocked their way at every turn and the force of the collisions kept them pinned down, the North Heaven Demon Lord thrust out his spear.

*Rrrrrum.*

Space warped. At its center, the spearhead gave off a blindingly ominous flash.

But that strike, carrying an unprecedented force, never swept across the people of Shanxi.

*Shwack!*

A gigantic arrow of light tore through the air and plunged toward the North Heaven Demon Lord.
## Chapter artifact 976

# Chapter 976

The instant he sensed a chilling force plunge down behind him like a bolt of lightning, the North Heaven Demon Lord spun around at lightning speed and swung his spear.

*BOOOOM!*

A tremendous collision.

Yet even as the unprecedented force carried on his spearhead swallowed the arrow of light, the North Heaven Demon Lord’s face remained as hard as stone.

Because the attack aimed at him wasn’t over.

*Shwaaa!*

The wind split apart.

The eyes of the North Heaven Demon Lord, watching a dozen or so streaks of light rush at him from beyond the pitch-black sky, turned red.

“Bow Saint—!”

With an angry shout, the North Heaven Demon Lord realized he had no choice left and thrust out his spear.

Space warped along the path of the spearhead in his hand.

*BOOOOM!*

*Krrrrk!*

Space shuddered as if struck by an earthquake. A tremendous shock wave burst forth with a deafening roar and swept across a radius of more than a dozen *zhang*.

An enormous cloud of dust swallowed the narrow gorge in an instant. From within it, two gusts of wind blew.

Hotter than the air on a midsummer afternoon, more suffocating than the scorching desert sands far to the west.

*Fwoosh.*

The North Heaven Demon Lord felt that sudden blast of heat all too clearly.

And he saw them.

Two figures shooting toward him through the flash of light.

Two fists, grown from the same root, wreathed in flames of different colors.

*Gooooong.*

Flame-Extinguishing Divine Fist.

As he stared down the terrifying heat burning its way through space, the North Heaven Demon Lord thrust out his spearhead with all his strength.

*Rrrrrum!*

At its tip, a distant flash of light blazed.

* * *

It all began and ended in the blink of an eye.

Pangu.[^1]

As if the primordial giant who was said to have split the world with a single axe had drawn in a deep breath, the air all around tightened taut. Then it burst outward, sweeping everything away.

*Rrrrrum!*

What should this be called?

An explosion? Or a catastrophe?

Jin Wikyung and the people of Shanxi couldn’t find an answer.

Crushed beneath an overwhelming force they had never experienced before—no, one they couldn’t even have imagined—they could only watch as a vast wave of power swept toward them.

*KABOOM! KAAAAABOOM!*

The world turned upside down.

To keep themselves from being swept up and flung away by the invisible shock wave, the people of Shanxi braced one another and drove their blades deep into the ground.

Their ears rang.

Instinctive awe and terror tightened around their entire bodies.

That was true of everyone except the few people who had caused this tremendous shock wave.

*Shhk.*

A spearhead cleaved through space.

In a realm neither eyes nor ears could perceive, Jin Taekyung and Jeok Cheongang dodged the Force shooting along the spearhead and thrust out their fists.

*Poom!*

Air erupted with a blast of terrible heat.

But when the flames, launched before the delayed boom, coiled through space, the North Heaven Demon Lord was already swooping down over their heads.

*Shwaa!*

A spearhead slashed down at an angle.

Just as Jin Taekyung twisted his body, the Force carried on the spearhead swelled larger still and came crashing toward his shoulder.

*Shhk.*

*I cut him.*

That certainty flashed through the North Heaven Demon Lord’s mind. It was absolutely true.

Except what he had just cut wasn’t flesh and bone, but armor that glowed faintly red.

*Pshk!*

Blood spurted from the split in the Fire Dragon Armor, cut open by the Force.

That tiny trickle—not even a handful—was all the North Heaven Demon Lord had managed to draw. The Master and Disciple didn’t let the opportunity slip.

*Crack.*

The instant Jin Taekyung clamped both hands around the shaft like hooks, the North Heaven Demon Lord understood on instinct.

Even with the Temporary Strength Pill’s immense boost to his physical abilities, and even with several centuries’ worth of internal energy surging without end, he couldn’t withstand the strength of the young man before him.

*What kind of monster is this…!*

The higher you climbed, the farther you could see.

But even across the North Heaven Demon Lord’s vast world, Jin Taekyung was a monster the likes of which he had never seen.

An achievement unbelievable for his age.

Physical abilities far beyond even those called superhuman. And for some reason, ever since defeating Jamukha, his movements and internal energy had grown faster and stronger still.

That alone made him a dangerous opponent. But what chilled the North Heaven Demon Lord’s spine even more in that moment was the old monster fighting alongside the young one.

*Whoom.*

The moisture in the cold dawn air evaporated in an instant.

Jeok Cheongang charged in with a palm strike brimming with terrifying heat. A reddish glow lit the North Heaven Demon Lord’s eyes.

*The Fire King…!*

There were no choices left, not even time to look for another.

The North Heaven Demon Lord released the beloved weapon he had carried for years and kicked off the ground.

*Sss!*

A burning pain that seemed to seep into his very soul.

The flames surged after their retreating target. Even a glancing touch melted armor and scorched skin.

And as the North Heaven Demon Lord endured that instant of pain and stumbled backward in a desperate retreat, the spearhead that had left him for a new master flashed toward him.

*Shshshshk!*

Dozens of spear images poured down, covering the space. The spearhead relentlessly pursued the North Heaven Demon Lord as he twisted and flipped his body without respite, drawing on every sense. Blue-white flames surged from its tip.

*Fwoosh! Shhk!*

Hot.

Blood welled from the gaps in the armor, melted open as it was cut. More than the blood Jin Taekyung had shed, it poured out in a dark, deep crimson stream, staining the North Heaven Demon Lord’s vision as it swam for a moment.

Along with a quiet voice that suddenly reached his ear.

“It’s not over yet.”

“……!”

“Grit your teeth.”

*Shhk, shhk, shhk!*

It took a long time to build something up, but it could all come crashing down in an instant.

The spearhead kept swinging, one strike after another, leaving the armor that had covered the North Heaven Demon Lord’s whole body all but useless.

*Clank. Clatter!*

Blood sprayed across the shattered iron plates.

The North Heaven Demon Lord gritted his teeth against the searing pain.

The flames that kept crashing down on him melted and broke things apart without resistance. And what was falling to pieces wasn’t only the armor he wore.

Everything.

Everything he had accomplished as Murong Baek, everything he had hoped to accomplish as the North Heaven Demon Lord—his past and future, all of it—was turning to ashes and scattering, bit by bit.

*Why!*

The North Heaven Demon Lord screamed in his heart. He gathered the vast force that had yet to fade into his fist and flung it outward.

*BOOM!*

Space shook with a roar that sounded as if the heavens had split apart.

Yet the strike, powerful enough to bring down a mountain, tore through empty air without touching a thing.

“Long ago, every time I saw you, I always had the same thought.”

The Fire King, Jeok Cheongang.

The old monster of Mount Jiuhua, who had lived for well over a hundred years, took a step toward the North Heaven Demon Lord.

*Whoosh.*

His figure vanished as if it had evaporated. At the same time, enormous heat scorched the North Heaven Demon Lord’s side.

*Fwoosh.*

Blinding light-flames swallowed the darkness. The North Heaven Demon Lord instinctively looked up, his eyes turning white with their light.

“You really do have the kind of eyes no one can trust.”

In that instant,

the North Heaven Demon Lord saw it.

A savage blaze at odds with Jeok Cheongang’s calm voice.

A dazzling wave of fire, neither red nor blue.

*BOOOOM!*

The roar came too late to keep up with the movement, then shook everything around them.

Unable to withstand the force, the North Heaven Demon Lord crashed deep into the cliff wall and swallowed the blood surging up his throat.

*Not yet. Not yet.*

It wasn’t over. He couldn’t fall.

He sensed his vision blurring and pushed himself up from the cliff that cradled him like a nest.

No—he tried to.

Until a flash of light flickered through the dust cloud rising pale beyond the countless rock fragments raining down from the collision.

*Thud! Krrrk!*

The spearhead, wreathed in blue-white flame and cloaked in dreadful heat, pierced his shoulder. It smashed through bone and flesh and drove deep into the cliff.

“……!”

His entire body quivered with indescribable pain.

But the North Heaven Demon Lord refused to give up. Through the pain that turned his vision white, he fought with all his strength.

“GRAAAAAH!”

*Crack! Fwoosh!*

At last, the spearhead came free—or rather, his body did.

Instead of pulling out the spear lodged deep in the cliff through his shoulder, the North Heaven Demon Lord gritted his teeth and tore his shoulder free. Then he kicked off the ground and shot upward.

He burst through the churning dust cloud, bounding off the cliff face and the very air.

Away from the two monsters who had pushed him to the brink of death.

Toward the only path of escape before him.

*Shweee!*

His body should have already collapsed from his terrible pain and injuries. His internal energy should have dwindled to a mere handful. But the Temporary Strength Pill’s effects made him forget all of it.

The North Heaven Demon Lord pushed onward with every ounce of strength he had.

Thinking of the prey who would be frozen in disbelief beyond the thick dust cloud settling all around.

Thinking of the only lifeline that could save him from his predicament.

*Jin Wikyung.*

The Lesser Family Head of the Jin Family of Taiyuan, and Alliance Leader of Shanxi Province’s forces in today’s battle.

And, to someone, a precious member of the family.

*If I take him hostage, I can escape.*

He had spent his entire life as the heir—and then the Family Head—of the Murong Family, one of the Five Great Families.

His insides had been black, but his outward face was clean.

How many years had he spent hiding the teeth of a beast while living alongside them within the orthodox faction’s fence?

The North Heaven Demon Lord understood the people called orthodox better than anyone.

Their nature, their habits, their way of thinking—all of it.

He also knew that the young upstart of the Jin Family of Taiyuan who had cornered him alongside the Fire King was bound more tightly than anyone else by the word *righteousness*.

*That’s why. It’s the biggest reason you can’t defeat me—or us.*

They had lost a battle in which both sides had given everything they had, and the grand plan they had been certain would succeed had gone up in smoke.

But that didn’t mean it was the end.

As long as he survived, another chance would come.

And the North Heaven Demon Lord would return.

In the not-too-distant future, before the sting of his defeat and his enemies’ cheers had faded, he would once more unfurl the Murong Family’s banner and stride across the land.

Beneath a dark sky, with his hidden fangs bared to the fullest.

*I will return. Even if I have to stake everything I have.*

The North Heaven Demon Lord thought back on the defeat and humiliation he had suffered that day and renewed his resolve.

In that moment, his reason—numbed by pain and hope—couldn’t even recognize the foolishness of his decision.

He couldn’t even properly wonder why Jeok Cheongang and Jin Taekyung weren’t chasing him, even in this situation.

And at last, beyond the dispersing cloud of dust, the North Heaven Demon Lord saw Jin Wikyung—the man he had wanted so desperately to find.

He also saw the person standing tall before him, directly in front of Jin Wikyung, who had led everyone from the front from the very beginning.

“Bow… Saint.”

*Splash.*

A low moan slipped between the North Heaven Demon Lord’s lips.

Just as his steps—which had seemed as if they would go on forever—stopped in a pool of blood, he stared at the Bow Saint with hollow eyes. Then someone’s voice drifted into his ears.

“Poppy. Where did you go, Poppy?”

An anxious voice rang out through the cloud of dust.

Moments later, Jin Taekyung suddenly emerged from within it and stared wide-eyed at the North Heaven Demon Lord.

“Oh my god, Poppy! What are you doing here?”

“……!”

The North Heaven Demon Lord’s eyelids twitched.

[^1]: Pangu is a primordial giant in Chinese creation mythology, said to have separated heaven and earth.
## Chapter artifact 977

# Chapter 977

Shame was only one of the many emotions every human being felt, but its weight varied enormously from person to person.

For a slave scorned from the moment they were in their mother’s womb, shame might be no different from fate. For the noble and the wealthy, it could tear at the heart more cruelly and sharply than any blade.

And the North Heaven Demon Lord was very much the latter.

“Our Poppy! I was wondering where you’d run off to in such a panic. There you are.”

A face and voice full of concern.

And a smile whose lopsidedly raised corners made that concern look all the more absurd.

“I was so worried. I thought I might’ve lost you for good.”

With every mocking word Jin Taekyung spoke, the North Heaven Demon Lord’s eyelids twitched.

As if it weren’t bad enough that he’d walked into an obvious trap of his own accord, now he was being treated like a dog that had run away from home.

The shame and despair wrapping around the North Heaven Demon Lord’s entire body were unlike anything he had ever felt before.

“How dare a nobody like you—”

“Shut up.”

Beyond the faintly scattering cloud of dust, Jeok Cheongang appeared. His gaze sank deep as he cut off the North Heaven Demon Lord’s voice.

“Who do you think you are, running your mouth like that? You’re a nobody.”

The North Heaven Demon Lord gritted his teeth.

Why was this happening?

Somehow, Jeok Cheongang’s figure in his eyes had grown large and blazed as fiercely as it had long ago, during the Great Faction War.

As if he were looking once again at his former self, unconsciously shrinking before the giant known as the Fire King.

*Step.*

The sound of footsteps rang unusually clear in his ears.

But Jeok Cheongang, walking toward the North Heaven Demon Lord, suddenly stopped and let out a short laugh.

“I’ve walked a good ten paces, yet the distance hasn’t closed at all. I feel like I’ve been bewitched. Don’t you?”

At his Master’s question, Jin Taekyung furrowed his brow as if puzzled.

“Come on, that can’t be right. Maybe you’re imagining it?”

“Imagining it?”

“That makes no sense. It’s not like you’re walking in place. Why wouldn’t the distance get smaller?”

Scratching his chin, Jin Taekyung continued as casually as could be, glancing at the North Heaven Demon Lord’s stiff face.

“Unless some coward got scared and started backing away.”

“……!”

“Oh, wait. Is that it? Seriously?”

*Crack.*

The skin split and blood flowed.

The North Heaven Demon Lord clenched his teeth until his lips burst, then looked down at his own legs, which had instinctively stepped backward.

Or perhaps he’d looked away because he couldn’t bear to face that bloodied brat’s mocking expression.

If he didn’t do at least that much, he felt he might truly lose the last thread of reason he had left.

“Wow, it really was true. A minute ago, you were acting all high and mighty and throwing a damn fit just because you’d taken a pill.”

With that taunt, Jin Taekyung’s footsteps once again drew nearer, one confident stride at a time.

But this time, the North Heaven Demon Lord didn’t retreat.

No—that wasn’t it. He couldn’t retreat.

*Shhk.*

Unlike the master and disciple blocking his path, the footsteps behind him were light as feathers.

The North Heaven Demon Lord half-turned, and in his field of vision appeared a woman approaching like a gentle breeze.

*The Bow Saint.*

Caught between them. Surrounded on all sides.

No expression could begin to describe the situation.

Three Supreme Peak masters.

One was a member of the Three Saints, known to all under heaven. Another was an old sovereign who stood shoulder to shoulder with her. And the last was a young Divine Dragon, soaring toward the heavens with the dragon pearl of that old sovereign’s teachings in his grasp.

*This can’t be happening. It can’t.*

The words slipped out alone from a hollow corner of his heart.

Then, at some point, the trembling in the North Heaven Demon Lord’s eyes subsided. His gaze sank deep.

“Even if you defeat me here today, nothing will change.”

Jin Taekyung shot back without hesitation.

“Do you people go around memorizing speeches or something? Is there some kind of punishment if you get even one word wrong? Like losing your internal energy for a week?”

“Say whatever you want. It makes no difference. That is the only truth.”

“For something that won’t change anything, we’ve done a pretty good job stopping you so far. Today included.”

At Jin Taekyung’s reply, the North Heaven Demon Lord let out a short laugh without meaning to.

“If that’s what you believe, then so be it. There’s nothing wrong with holding on to hope.”

“What?”

“Being in this situation made me wonder. Why did the Western Heaven Demon Lord, the Southern Heaven Demon Empress, and the Eastern Heaven Demon Lord fail? How did a plan they’d spent so long preparing fall apart in an instant?”

At those unexpected words, Jin Taekyung’s face hardened. So did everyone else’s.

“What are you trying to say?”

Jeok Cheongang’s voice was cold.

Jeok Cheongang looked ready to burn him alive on the spot, but the North Heaven Demon Lord answered calmly.

“I don’t know. I’m not sure what I’m trying to say.”

“You bastard—!”

“Don’t rush, Fire King. Even if you don’t push me, we don’t have much time left.”

With his mind emptied, his voice was calm as well. The North Heaven Demon Lord looked inward, contemplating the energy that remained in his body, and continued.

“Half a year at most. That’s all.”

The war had already begun.

From the day the absolute ruler in the darkness awoke from a long slumber.

No—from much earlier than that.

“Power beyond anything the hundred thousand followers of the Demonic Path possessed. Unbelievable powers. ‘A new heaven’ refers to that person.”

No one here could mistake who the North Heaven Demon Lord meant by “that person.”

“The Lord of Heaven…”

The Bow Saint murmured to herself, then lifted her clear eyes to look at the North Heaven Demon Lord.

“Was that why you abandoned the comrades who shared life and death with you, and betrayed the world?”

“Comrades? Did you just call them comrades?”

The North Heaven Demon Lord suddenly burst into a hearty laugh.

Comrades. People walking the same path together.

The meaning held in those two words—their utterly worthless value and the past they called to mind—made him laugh in spite of himself.

“It seems you lived in a different world from me. Well, what could you possibly know, when you shut yourselves away in remote mountain valleys without roots, turning your backs on the world?”

His bloodshot eyes passed over Jeok Cheongang and the Bow Saint in turn.

Neither of them had been known by name before the Great Faction War. They had been eccentric, reclusive masters.

But the North Heaven Demon Lord—Murong Baek—was different.

As a direct descendant of the Murong Family, one of the Five Great Families, he had seen the world. He had to wage covert battles against others who shared the same orthodox fold.

“Everyone smiled and talked about righteousness, all while hiding invisible blades in their sleeves. Is that what you call comrades? Is this the orthodox faction?”

Even the stars looking down on the world from the heavens would one day lose their light and fade.

Everything grew old and withered in time.

The world of martial artists was no different.

As time flowed on, the martial world had disappeared. All that remained was the cold world of Murim.

The value of chivalry had grown dimmer and dimmer, while the orthodox faction—including the Nine Sects and One Gang and the Five Great Families—poured their strength into settling scores with one another.

It was commonplace for them to take in countless lay disciples and expand the sects under their control.

Some even committed the taboo of bringing the unorthodox faction into their fold. Others caused numerous casualties in clashes waged in secret.

Expansion could only end in an explosion.

The power they had accumulated over the years was now eating away at the orthodox faction in the form of conflict.

And the lands of the north, far from the Central Plains, were no exception.

If anything, it was worse there.

At least for the Murong Family.

“You can’t claim you don’t know, either. You know what kind of roots I—or rather, the Murong Family—have.”

The North Heaven Demon Lord looked down at the pool of blood gathered beneath his feet.

He had the handsome features and imposing presence of a man who had spent his life as the Family Head of a prestigious great house.

Yet even after all the years the Murong Family had been rooted in Liaoning Province, the faint traces of his foreign ancestry still flowed through his veins.

Enough to bring to mind, for a moment, the face of Jamukha lying dead.

“Nomad?”

At Jin Taekyung’s half-muttered question, the North Heaven Demon Lord’s fist tightened by instinct until his knuckles turned white.

He’d heard that word countless times.

The pointing fingers and voices from out of sight, always there, remained in his eyes and ears.

Nomad. Invader. Outsider.

And barbarian.

Long ago, the people of the northeast who were called the Murong Xianbei had occupied the edge of the continent and founded a nation.

It was a time of chaos.

Five foreign peoples and sixteen small kingdoms had struggled for supremacy.

But the divided land found stability again, and the invaders who had taken advantage of the turmoil to charge across the continent with spears and composite bows were either driven beyond the Great Wall or absorbed.

The Murong Xianbei were the latter.

They remained in Liaoning and laid new foundations there, establishing the framework of a great family.

The Murong Family was born.

A family of invaders descended from barbarian blood.

They had risen to become a towering force in Murim through their peerless martial arts and superb horsemanship. Yet the other towering forces—the Nine Sects and One Gang and the Five Great Families—had looked down on them and treated them with contempt, though never openly.

“Sometimes I wondered: if the Great Faction War had never happened, would the Murong Family have survived to this day?”

Expansion ended in an explosion, but the aftermath of an explosion beyond anyone’s imagination could leave reconciliation and peace behind.

The arrival of the Demonic Cult, an external enemy, changed everything.

To survive, everyone had to join forces and fight together. The Murim Alliance, formed around the Martial God, brought the feuding orthodox faction together as one.

But Murong Baek—and the Murong Family—hadn’t forgotten.

They remembered it all clearly.

“There is no more chivalry. No more benevolence or righteousness. In the end, after all these years, the only ones who survive are the strong.”

The strong prey on the weak.

That was the only truth of the world the North Heaven Demon Lord had learned.

The only value and purpose of Murim, built on violence.

And so Murong Baek became the North Heaven Demon Lord.

“That was why. Nothing else.”

*Rumble. Rumble.*

A powerful tremor spread across the ground.

The North Heaven Demon Lord’s eyes were now so red that “bloodshot” no longer described them. His blood-red gaze swept over everyone in the gorge as he roared.

“Who dares! What hypocrite has the right to condemn me!”

*BOOOOM!*

The force behind his aged shout exploded into a mighty sonic wave.

The aura was truly terrifying.

Blood flowed from the ears of the people of Shanxi, frozen like statues. Several who had been shaken to their cores by the roar alone coughed up blood and dropped to their knees.

*Vrrrrm.*

A terrifying power churned around one man.

Though gravely wounded, his immense aura squeezed the air all around him until it tingled. Jeok Cheongang realized the North Heaven Demon Lord had already crossed the point of no return.

Innate qi.

Just like the heads of Dark Heaven who had gone to the afterlife before him, the North Heaven Demon Lord was burning up everything he had been given in that moment.

Even knowing death waited at the end.

“If I tell you to back off, will you?”

At Jeok Cheongang’s quiet question, his Disciple wordlessly reached out.

*Whoosh—tap.*

A spear shaft shot from behind him like an arrow and was caught in his firm grip. Blue-white flames surged upward, winding around the almost transparent spearhead—a wordless answer.

“I’ve been listening to this bullshit for so long my whole body aches.”

“You’re too young to have aches all over.”

Jeok Cheongang gave a short laugh, and Jin Taekyung laughed along with him.

“I’ll go on ahead. You two can take your time catching up.”

At the same moment, dirt and rock crumbled beneath Jin Taekyung’s toes.

*Crack—BOOM!*

The ground split like a spiderweb. A streak of flame shot forward.

The two old monsters blurred, following the Divine Dragon as he charged ahead with greater speed and force than ever.

*Flash.*

Within the distance that vanished in an instant, a blood-red glow surged upward.
## Chapter artifact 978

# Chapter 978

Every now and then, I find myself realizing that I’ve changed.

In the middle of this miserable fight, where I have to risk my life every moment, I keep moving forward with an inexplicable joy in my heart.

“Jin Taekyung!”

A shout like a lion’s roar lashed at my ears.

Beyond the wind whipping around me, I brought White Flame down on the blood-red light bursting from the North Heaven Demon Lord’s fingertips.

*Shhk!*

The enormous Palm Force split in two along the path of my spearhead.

Leaving behind the tremendous impact and explosion as the deflected Palm Force shook the cliffs on either side, I planted my foot on the ground once more.

*Tap.*

The flames that should have burst forth from Flamefire Path were nowhere to be seen.

The tips of my feet, infused with the Slaughter Saint’s teachings, felt lighter than ever, and my body shot forward at such speed it was like a flash of light.

Like a beam that had suddenly struck from far across the gorge.

*Shwaaa!*

Compressed air tore apart. The North Heaven Demon Lord swung a fist, seething with rage and internal energy, at the arrow of light that had overtaken even sound and closed in.

*BOOOOM!*

Contact. Then an explosion.

Within the distant, swelling flash of light, I saw it clearly: the beam the Bow Saint had shot fading beneath the dark red glow.

And I saw the North Heaven Demon Lord’s eyes, reflecting my figure as I closed in, already right in front of him, without missing that opening.

*I can see it.*

The world slowed in an instant.

Everything around me was sharp and vivid.

His lips moving slowly, as though he were trying to say something.

His eyes, so red there wasn’t a trace of white left in them.

And the condensed Palm Force blocking the spearhead I had thrust forward with all my might.

*Krrrk!*

Two different Forces collided. The blue-white flames meeting in midair mingled with the dark red shadows and sent out a powerful wave of force.

“Just… this much.”

His voice came in broken fragments.

The North Heaven Demon Lord glared at me, gripping my spearhead in one hand. Streams of blazing red seemed to pour from his eyes.

“Did you think you could defeat me—Murong Baek—with this?”

*Zzzzzzt!*

An unprecedented energy flared up like a wildfire, pressing down on the flames carried by my spearhead. The power the North Heaven Demon Lord had gained by burning even his own life came at a steep and tremendous price: a death already set in stone.

Even though all my fatigue and injuries had completely healed after I took down Jamukha, I still couldn’t imagine victory.

But…

*Yeah. This is about what I expected.*

I smiled.

The strength I sensed from the North Heaven Demon Lord was within the range I’d expected.

And the energy crashing down from behind me at a speed like a flash of light was just as immense as his.

*Now.*

There had been no shouted warning, no Sound Transmission.

But I knew. He knew, too.

Even if we couldn’t see each other, we knew each other too well.

So, without the slightest fear or hesitation, we moved as the thought flashed through our minds.

*Slip.*

The instant I let go of the spear shaft and turned halfway around—

A streak of flame, hidden behind my body—a frame massive enough to be called a giant—filled the space I’d left and exploded.

*Gooooong.*

Like the breath of a fire dragon from legend, pure white hellfire blazed across the darkness.

It burned away the dew lingering in the dawn air, vaporizing it as it rushed toward the North Heaven Demon Lord.

Fire. King.

His lips moved ever so slightly, forming a soundless cry. His eyes, heated by the scorching air, wavered, losing their focus.

Confusion and fear he couldn’t hide.

And those emotions instinctively showing on the North Heaven Demon Lord’s face meant that someone else had appeared—not me or Jeok Cheongang.

*Shwaaa!*

Behind the North Heaven Demon Lord, two gently curved blades traced a beautiful arc.

The strike carried an energy every bit as deadly as the furious flames crashing straight at him, though utterly different in nature.

“……!”

In the slowed world, the North Heaven Demon Lord’s eyes flew wide.

Jeok Cheongang’s Flame-Extinguishing Divine Fist was coming from the front. From behind, the Bow Saint’s two curved blades—whose shape had changed—were coming down on him.

Two Supreme Peak masters unleashed a terrifying combined attack, leaving him neither time nor room to dodge. He had no choice left.

*BOOM! KAAAAAABOOM!*

In an instant, all the darkness that had covered the gorge lifted.

A blood-red glow burst out, wrapping around the North Heaven Demon Lord’s entire body.

*Krrrrrk!*

The world shook. A relentless wave of force swept in every direction, and the ground crumbled beneath the three combatants.

*Crack! Krrrk!*

The ground split like a spiderweb, unable to withstand the tremendous pressure.

As I had done at the last moment, the North Heaven Demon Lord twisted his body and changed direction. His whole frame shuddered violently like a tree caught in a typhoon.

His face twisted like a Fiend’s as he caught Jeok Cheongang’s fist in one hand and the Bow Saint’s two curved blades in the other.

*No. He was already a Fiend. Had been for a long time.*

No matter how many years a monster spent wearing a human face, its nature didn’t disappear.

The North Heaven Demon Lord—Murong Baek—had crossed a river from which there was no return.

Like so many other monsters who had pursued the Demonic Path for their own reasons, heading off somewhere beyond it.

*Crack—splatter!*

Blood gushed from the flesh and joints of bone, slowly being cut and crushed.

The North Heaven Demon Lord convulsed with pain the likes of which he’d never imagined.

Both his hands, holding off the Fire King and the Bow Saint, were slowly losing their shape even now.

And yet there was one thing that would remain unchanged until the very end: those eyes filled with bitter hatred.

“Why? Why…?”

I could feel all the pain and hatred in the North Heaven Demon Lord’s voice, as if he were grinding the words out through clenched teeth hard enough to draw blood.

And I could feel the sliver of fear he couldn’t quite hide as I slowly approached.

“I… won’t… die.”

The North Heaven Demon Lord’s words broke apart with his gasping breaths. Jeok Cheongang answered, his expression calm.

“Everyone dies. People and monsters alike.”

The blood-red light that seemed about to devour the whole world and the force that had been pressing down on everything around us were nowhere to be seen now.

Even if some remained, they were fading like a lamp before the wind.

*Krrrk.*

The pressure was more than one hand could withstand.

Before the white hellfire Jeok Cheongang drew forth with all his strength, alongside his quiet reply, the North Heaven Demon Lord finally dropped to one knee.

*BOOM!*

The ground caved in deeply. The Bow Saint’s voice reached the North Heaven Demon Lord, his eyes bulging as if they might burst.

“A person is born human, and makes choices by their own judgment. There is no right answer. This is simply… the consequence of your choice.”

What life has a right answer?

Life isn’t multiple choice. It isn’t some test graded with short answers or essays, either.

Whatever life a person has lived, looking back, there will always be at least one thing they regret. That is what human life is.

But both the judgment and the consequences are your own. That’s all.

“Murong Baek, the Divine Spear of the Imugi. No—the North Heaven Demon Lord. It’s time to accept the consequence of your choice.”

There’s a reason and a history behind every martial artist’s sobriquet.

So when I heard the unfamiliar one slip from the Bow Saint’s lips, I had a vague sense that I understood the life Murong Baek had lived.

The imugi.

An imugi that never became a dragon.

And at the same time, an imugi that had wanted to become a dragon more than anyone.

Maybe that was why.

Why he had struggled so desperately to obtain the dragon pearl.

Why he’d remained in the shadow of Dark Heaven, searching for every excuse and justification he could find, all so he could become a dragon soaring freely through the azure heaven.

But knowing something and understanding it are different.

And even if every story he’d told us himself was true, I would never understand Murong Baek, the North Heaven Demon Lord.

No. I would refuse to understand him.

The day I understood him would be the day I became a monster, too, one of those existing across the dark, deep river.

“Before you go, remember this.”

With a quiet voice, I reached out.

The pure white spear shaft the North Heaven Demon Lord had been forced to let go of to face Jeok Cheongang and the Bow Saint flew into my grip as though drawn there.

“Not everyone in the world makes the same choices you did.”

The weak are cast aside, and the strong survive.

That’s how this world has always been—always, without fail.

The law of the jungle existed not just in Murim, but in the modern world, too. And it would continue to exist.

Even if people used other means instead of spears and swords.

But if everyone made the same choice as the North Heaven Demon Lord out of fear of being cast aside, the world would already have become a hellscape.

A place without even the barest sense of decency or benevolence.

A terrible world, endlessly perpetuating itself through one purpose alone: devouring one another, and being devoured.

But not everyone is like the North Heaven Demon Lord. That’s why I think this world is still worth living in.

And I believe, too—

That among the countless people scattered like stars across the night sky, whoever gave such inexplicable power to an unremarkable F-rank Hunter must feel the same way.

“Now, go.”

I didn’t wait for an answer.

I simply thrust my spearhead, wreathed in blue-white flames, into him—quietly and without hesitation.

Into the North Heaven Demon Lord, who was still struggling, refusing to give up even at the last moment, burning every bit of life left in his body.

Into the chest of a monster who had lived not merely to protect what was precious to him, but to seize and hoard what belonged to others.

*Thud.*

The blazing flames pierced through flesh and bone.



* * *



As if someone had lit a candle, the being in the darkness suddenly opened its eyes.

How long had it been asleep?

How much time had passed in that abyssal dream where everything had become a jumble?

It didn’t know.

The question was familiar, and the conclusion was always the same.

It had always been that way for the being in the darkness.

Whenever it woke from time to time, the world had always changed.

It had once slept for decades. What more was there to say?

But as the intervals grew shorter with the passing years, the being in the darkness was gradually beginning to realize:

The day it had thought it would never reach had, at some point, drawn right up to its doorstep.

*Fwoooosh.*

A cold wind swept through the area. Soon, it became a raging gale.

It put out the torches faintly illuminating the thick darkness and shook the ground and roof.

And that sudden change, like a raging current rising in a tranquil lake, was also proof that the being in the darkness had realized why it had opened its eyes.

North Heaven.

The fourth heaven had fallen. Another faithful servant had disappeared.

But as the being in the darkness faced the fact that would soon shock everyone beneath the heavens, it smiled alone.
## Chapter artifact 979

# Chapter 979

At some point, everyone realized.

“Waaaaah!”

A tremendous roar shook heaven and earth as it rolled over the narrow gorge called Eight Spring Gorge.

The fighters who had been locked in fierce battle across the vast basin all turned their heads at once.

Their lips were cracked like drought-stricken fields. Their hands and feet trembled with utter exhaustion and fear of death.

After hours of fighting, they were covered in blood from head to toe. With desperate eyes, they stared toward the gorge’s entrance.

They prayed that the thunderous roar racing closer—and the countless footsteps pounding the earth—belonged to their allies.

Then, beyond the darkness slowly beginning to thin, a streak of light suddenly flashed.

*Shwaaaaa! BOOM!*

In an instant, a deafening crash mingled with screams.

But Iron Blood Saber Peng Cheolyeong, Family Head of the Hebei Peng Family, recognized the light—and laughed with all his might.

“Ha! Hahahaha!”

*Crack!*

With that booming laugh, he swung his great saber and swept through a dozen nomads in a single stroke.

Beneath the fountain of blood that soared into the air, the fewer than one thousand remaining warriors of Hebei pressed forward behind their Family Head.

Just moments ago, their bodies and weapons had felt as heavy as waterlogged cotton. Now, they were impossibly light.

As they advanced, laughing like madmen, a thick mist of blood rose around them.

*Shhk! Shhk-shhk!*

“Aaargh!”

“Guh!”

Screams erupted from every direction. Neither the Murong Family’s martial artists, trained in their clan’s secret arts, nor the nomads who had once struck fear across the land with lance and bow could stop the Hebei Peng Family.

No—more precisely, they had frozen at the sight of the unbelievable scene unfolding before them.

*Rumble!*

The ground shuddered.

With dawn approaching and the darkness fading, thousands of shadows poured from the narrow gorge’s entrance. A blood-soaked banner rose high above them.

The Great Taiyuan Jin Family.

“……!”

“……!”

It could mean only one thing.

Eyes fixed on the characters embroidered on the banner trembled.

Some with shock and despair. Others with hope and joy.

But there were also those who belonged to neither side.

“Enough! What do you think you’re doing?”

The Murong Family’s Head Elder, Murong Wijin, who had been directing the battlefield in Murong Baek’s place, shouted, channeling his internal energy into his voice.

His followers flinched beneath his venomous glare.

“Don’t fall for their petty tricks! This is—this is just…”

Murong Wijin clenched his teeth, unable to finish.

What else could he say?

Anyone who wasn’t a fool could see what was happening.

Reality was cruel enough to make them shudder.

They had lost. Their enemies had won.

And the ones who had returned to finish it all were neither Jamukha nor Murong Baek. They were the people of Shanxi.

The Taiyuan Jin Family’s banner was held so high it seemed to pierce the sky. Their ranks advanced in tight formation, their steps filled with certainty.

Certainty of victory.

Perhaps certainty in the four people leading them.

“Hold on. I’ve seen that guy’s face somewhere.”

His hair had grown into prickly stubble, like a lazy monk’s, and was so red it seemed to be on fire.

Facing the monster who looked decades younger than he ought to, Murong Wijin trembled.

“F-Fire King…!”

“Oh, now I vaguely remember. Murong… whatever. Right?”

At Jeok Cheongang’s nod, as if he’d finally figured it out, the woman beside him sighed.

“Murong Wijin. Not ‘whatever’—Wijin. And if he’s wearing the Murong Family’s uniform, obviously his surname is Murong.”

“Wijin? Who’s that?”

“That’s understandable. During the Great Faction War, he wasn’t even thirty. He was a child.”

Though Murong Wijin was nearing eighty, he couldn’t say a word.

In front of two monsters like the Fire King and the Bow Saint, he was still no more than a hot-blooded, inexperienced youth.

In age and in martial arts.

And there was someone else here who gave no damn at all about either.

“Hey, what’s your name again? Murong… thingy.”

Murong Wijin’s face had stiffened after being forcibly renamed by both Master and Disciple. Just then, Jin Taekyung stepped forward and suddenly swung his spear.

*Whoosh!*

A fierce roar split the air, crossing dozens of yards. The round object impaled on his spearhead fell right at Murong Wijin’s feet.

*Thump.*

When Murong Wijin saw what touched the tips of his shoes—an object that was, in fact, a person’s head—a groan escaped him before he could stop it.

“……Family Head.”

Once words were spoken, there was no taking them back.

Murong Wijin belatedly realized his mistake and clamped his mouth shut, but the damage was done.

“You… You dare…”

“What? Not enough? Want another?”

Jin Taekyung swung his spear again, and another head sailed through the air.

This time, the nomads bit their lips as they recognized Jamukha—the greatest warrior of the steppe and its Great Chieftain.

“If you need more, say so. No, wait. I take that back.”

Jin Taekyung shook his head and started walking.

*Thud.*

His footsteps rang out with unusual weight and clarity.

His reddish, smoldering eyes swept across the vast basin.

“There are too many to bring here one by one, so I guess it’d be better to make them right here. Fresh from the source.”

“……!”

“……!”

The Murong Family and the nomads—without exception, everyone instinctively took a step back.

Even though they still had an army of nearly ten thousand, an overwhelming aura and killing intent flowed from Jin Taekyung. No one dared challenge him.

And in the suffocating silence, a voice suddenly rang out.

“If you lay down your weapons and surrender now, I promise you’ll at least keep your lives.”

One man had been overshadowed by the three Supreme Peak masters.

He had neither several jiazi of internal energy nor the godlike power to stand shoulder to shoulder with them. Yet he commanded an inexplicable authority.

Perhaps it was an authority only someone who had raised a declining family and become the Alliance Leader of Shanxi Province could possess.

“I give you my word. In my name, and in the name of the authority held by the Jin Family of Taiyuan.”

Jin Wikyung continued calmly.

At the far end of his gaze stood a young chieftain who looked especially haggard.

“Choose, Temur.”

“……!”

“I know you. I know you didn’t come here of your own will.”

Temur clenched his teeth.

“We’ve… come too far.”

His brother, with whom he’d shared years of hardship, was dead. And Temur had submitted.

He meant what he said.

He had come too far to return to the steppe, to his homeland.

But Jin Wikyung shook his head.

“It’s not too late. Not yet.”

“……Why? Why are you offering me this?”

“Because too much blood has already been spilled. If I can prevent more people from dying, I’ll do anything.”

Unlike his composed voice, a tear ran down Jin Wikyung’s cheek.

“That’s all.”

Seeing Jin Wikyung weep—and feeling the sincerity behind it—left Temur breathless.

He thought of how different a path he’d chosen.

He thought of all the tribespeople who had died here today because he’d surrendered to survive.

“What… do you want me to do?”

“Bastard!”

At Murong Wijin’s furious shout, the Murong Family’s martial artists moved. But a dense forest of lances had already closed in around them.

Standing before the army of ten thousand, now split in two in the blink of an eye, Jin Wikyung spoke.

“Surrender and submit. Completely.”

“……!”

“Too much? Then you can refuse. I don’t care if you join forces with the Murong Family right now. But…”

Jin Wikyung’s voice hardened. Then it burst into a mighty shout.

“We will fight. We will cross the Great Wall and trample the steppe. Whatever the cost, we will drive you out of there!”

At that moment, a chill ran down Temur’s spine.

The thousands of surviving nomads felt it, too.

They all heard and felt Jin Wikyung’s resolve—to repay this grudge, even if it took hundreds of years and cost countless lives.

They heard the sincerity in his tightly restrained voice, seeping through clenched teeth.

And then, Temur had no choice but to decide.

“……Temur of the Golden Clan.”

Temur—the only chieftain who could fill Jamukha’s place—bowed his head.

To the Han Chinese beyond the Great Wall.

To the Alliance Leader of Shanxi and the Lesser Family Head of the Jin Family of Taiyuan.

“I offer my greetings, my lord.”

In that instant, time on the battlefield—which had stood still—began to flow again.

*Shhk-shhk-shhk!*

The forest of lances swallowed the Murong Family. Behind them, thousands of people of Shanxi charged beneath the fluttering banner of the Jin Family of Taiyuan.

The blood-soaked night of the Double Ninth Festival finally woke to the dawn.



* * *



In the hazy space between dream and reality, the young man had forgotten even that he existed, trapped in the layers of memory piled up in his mind.

*Shwaack!*

He looked no older than four or five.

The child’s hands swung a wooden sword as tall as he was, each stroke cutting the air with a sharp hiss. His face was serious in a way that didn’t suit his age.

No one knew when he’d begun or how many times he’d swung it. His tiny body was already soaked with sweat.

People standing at one side of the training ground watched in amazement, repeatedly letting out cries of admiration.

*“Incredible. A child who’s held a sword for only six months, and he can already deliver a strike like that.”*

*“Good heavens. What a martial talent.”*

*“Look at that speed and trajectory. Fast and precise. It’s hard to believe he’s so young.”*

*“More than anything, what’s truly amazing is that he knows how to work hard. Think about it, all of you. Have you ever seen a child like this in your life?”*

*“Never. Even the Head Elder, who was called Shanxi Province’s greatest prodigy in his youth, wasn’t like this. Though it’s true there are so many outstanding talents in the Central Plains.”*

*“The Lesser Family Head was so promising as a child, but then one day he got more interested in books than martial arts.”*

*“What a shame. If he’d kept training with the sword, he’d have reached at least the Supreme First Rate realm by now.”*

*“What can you do? It’s all in the past. The Family Head is so unpredictable, after all. I suppose his son inherited that from him.”*

Family Head.

At the two words someone let slip, everyone clicked their tongues.

But the silence, accompanied by strange glances exchanged between them, lasted only a moment.

As they watched the child practice his sword with flawless form, over and over, they resumed their conversation as if nothing had happened.

*“In any case, I don’t know much about the great sects of the Central Plains, but I doubt they have many talents like him. No, they must be quite rare.”*

*“Our family has surely been blessed. It does trouble me that he’s grown so gloomy for a child his age since the Family Head’s wife died in childbirth not long ago…”*

*“Mm.”*

At someone’s faltering words, everyone’s faces darkened.

*“It’s tragic, but there’s nothing to be done.”*

*“What can we do? It’s the fate ordained by Heaven.”*

*“Fate? What fate?”*

At the voice that came from somewhere, the murmured conversation abruptly stopped.

The next moment, as if they’d planned it, everyone fell silent and hurriedly turned their eyes in one direction.

So did the young man, who had been watching it all from a spot neither near nor far.

“F-Family Head!”

Hearing someone blurt out the cry in a rush, the young man—who had just turned his head—furrowed his brow.

Perhaps it was the sunset spreading from the west. He couldn’t make out the face of the man slowly approaching.

All he could hear was a voice that felt strangely familiar, tinged with a lingering sadness.

*“Well, judging by everyone’s reaction, I must be an unwelcome guest.”*

He was an ordinary-looking man.

Nothing more to add, nothing to take away.

But even though he couldn’t see the man’s face, the young man could sense the distinctive air around him as he scratched the back of his head.

The others facing the man, of course, couldn’t hide their confusion.

*“N-No, of course not.”*

*“Don’t give me that. Do I look that oblivious?”*

Beneath the face hidden by the sunset, his faintly visible lips curved into a smile.

The man looked over the people who were silently watching him, then spoke again.

*“I was just passing by and thought I’d stop in. Don’t mind me. It looks like you were watching my second son train.”*

*“We could hardly claim to be teaching him. The Second Young Master is so gifted that there’s nothing we dare try to correct.”*

*“Of course he is. Whose son do you think he is?”*

The man puffed out his chest as though he were proud, and he certainly looked it. But the young man saw clearly as the smile at the man’s lips turned bitter and fell apart.

Nor were the people who’d been restless ever since the man appeared any different.

*“We’re sorry, Family Head.”*

*“We spoke out of turn. Please punish us.”*

Their voices and expressions were heavy.

Watching them lower their heads one by one, the young man clicked his tongue softly without realizing it.

He didn’t know who he was or where he was, but he could infer what was happening from what he’d heard and seen.

To speak of Heaven’s fate in front of a Family Head who had recently lost his wife…

Whatever they’d meant by it, they deserved punishment.

Just as a nation needed strict laws to stand firm, a family had things it must uphold.

But the man called Family Head answered in a way that went far beyond the young man’s expectations.

*“Punishment? What are you talking about all of a sudden?”*

*“Pardon?”*

*“I told you, I just stopped by on my way past. Oh, was that talk about fate and all that related to me? I wondered what profound conversation you were having.”*

*“W-Well, that is…”*

*“Now that you’ve gone this far, I’m starting to get the picture. I know how this goes. You were bad-mouthing the Family Head who does nothing but laze around every day again, weren’t you?”*

*“F-Family Head, that’s not…”*

*“Enough. You people, honestly. I may be the Family Head, but you can’t just gossip about me behind my back.”*

The man folded his arms. The people, on tenterhooks, glanced at one another.

Should they tell the truth, or let it go?

As they agonized, their lips growing parched, the man let out a deep sigh.

*“Whew. You’ve confessed this much, so there’s no choice. As Family Head, I can’t just pretend I didn’t hear it. I’ll punish you now.”*

Here and there, people let out breaths they’d been holding.

Better to be punished than to carry the weight of guilt. Their faces relaxing, they listened as the man continued.

*“House arrest. Half a day.”*

*“F-Family Head…”*

*“You’ve looked tired lately. Stay under house arrest for half a day, then get back to work. Oh, and especially help our eldest a lot.”*

That was all.

The man waved away the family retainers trying to say something and dismissed them. Then he looked toward the child, who continued swinging his sword without even knowing anyone had arrived.

Only after every pair of eyes around them had turned away did he murmur softly.

*“Fate. Fate…”*

His eyes lifted suddenly to the sky, empty. His next words were filled with nothing but bitterness.

*“No. It’s all my fault.”*

Then he turned his head abruptly and added,

*“I’m sorry, Mukyung.”*

Under that gaze, fixed straight on him, the young man’s—Jin Mukyung’s—vision turned white.

*“Father.”*

At that moment—

*Rrrrrumble.*

The entire world surrounding Jin Mukyung crumbled away. Brilliant light poured down from above, and a familiar voice reached his ears.

“Hey, you awake?”

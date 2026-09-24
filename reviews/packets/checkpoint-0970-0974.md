# Checkpoint Review — 970–974

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

# Chapters 970–974

## Plot

Jin Taekyung returns to save his unconscious brother, Jin Mukyung, Cheol Mubaek, and Wipeng from Murong Baek, the North Heaven Demon Lord. Jeok Cheongang and the Bow Saint join Taekyung; their attacks break the nomad encirclement and help the Hebei Peng Family, though the Bow Saint leaves the gorge to aid its fighters when pill-enhanced Keshiks break their formation.

Murong Baek takes a Temporary Strength Pill and attacks alongside Jamukha, who also commits his Keshiks to the battle with pills. Jeok Cheongang confronts Murong, his former comrade, while Taekyung faces them both. Jeok catches Murong’s spear but is badly wounded in the hands; a razor-sharp gust then shoots toward his back.

## Continuity

- Murong Baek is the North Heaven Demon Lord and a Dark Heaven agent. He has taken a Temporary Strength Pill and is fighting Taekyung and Jeok Cheongang.
- Jeok Cheongang’s hands are badly wounded while holding Murong’s spear. A razor-sharp gust has just shot toward his back; its source and outcome are unknown.
- Jamukha has taken or is taking a Temporary Strength Pill and has vowed to deliver victory and Taekyung’s head in exchange for the Hebei Peng Family’s lands and lives.
- The Bow Saint has left the gorge to aid the Hebei Peng Family, where roughly two thousand fighters remain and pill-enhanced Keshiks have broken their formation.
- Jin Mukyung, Cheol Mubaek, and Wipeng are unconscious; their conditions remain unknown. Peng Cheolhu remains alive beneath the rubble, but his condition is unknown.
- The Emperor remains gravely ill with Blood Soul Gu; the treatment said to require him to die once remains unresolved.

## Translation Decisions

- Retain “Temporary Strength Pill,” “Linked Tyrant King Formation,” and “Flame Divine Palm.”
- Use “North Heaven Demon Lord” for Murong Baek’s title in Taekyung’s perspective; use “Murong Baek” when Jeok Cheongang refers to their shared past.
- Render 귀물 as “strange artifact”; its nature is unidentified.

## Durable state

{
  "active_continuity": [
    "The Bow Saint has left the gorge to aid the Hebei Peng Family, where roughly two thousand fighters remain and pill-enhanced Keshiks have broken their formation.",
    "The North Heaven Demon Lord, Murong Baek, has taken a Temporary Strength Pill and is fighting Taekyung and Jeok Cheongang alongside Jamukha.",
    "Jeok Cheongang is badly wounded in the hands while holding off the Demon Lord’s spear; a razor-sharp gust has just shot toward his back, with its source and outcome unknown.",
    "Jamukha has vowed to deliver Jin Taekyung’s head and victory in exchange for the Hebei Peng Family’s lands and lives.",
    "The conditions of Jin Mukyung, Cheol Mubaek, Wipeng, and Peng Cheolhu remain unknown.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment said to require him to die once remains unresolved."
  ],
  "continuity_sources": [
    973,
    974
  ],
  "open_questions": [
    "Who sent the razor-sharp gust toward Jeok Cheongang, and what happens to him?",
    "How will the renewed confrontation with Murong Baek and Jamukha unfold?",
    "Can the Hebei Peng Family withstand the pill-enhanced Keshiks?",
    "What are the conditions of Jin Mukyung, Cheol Mubaek, Wipeng, and Peng Cheolhu?",
    "Can the Emperor be treated for Blood Soul Gu, and what does the treatment requiring him to die once entail?"
  ],
  "safe_through": 974,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 970

# Chapter 970

In the hazy darkness where he couldn’t see an inch ahead, Jin Mukyung stared—not with his eyes, but with his heart—at the only path laid out before him.

A future that couldn’t be the future.

Eternal death.

*So this is the end.*

Even Jin Mukyung was surprised by how calmly he accepted reality in that moment.

He’d already done everything he could.

He’d fought with all his strength, enough to look up at the heavens without a shred of shame. At last, that strength had run out.

Body and soul.

He’d poured everything into the fight. There was nothing left.

In a world that had slowed to a crawl, he couldn’t even twitch a finger as a spear rose slowly and the death dwelling in its blade drew near.

And yet, if a thread of regret still remained somewhere deep in his heart, it was for those he would leave behind in this world.

*What will happen to them now?*

He didn’t care what the afterlife was like.

Even if a pale-faced Grim Reaper, dressed head to toe in black, appeared right now, bound him in chains, and dragged him before Yama, it wouldn’t matter.

He had lived an honorable life as a martial artist, as the Jin Family of Taiyuan’s Second Young Master.

The blood on his hands had come from protecting others, not from a desire to kill.

But now he had to leave.

He had to leave everyone behind and be dragged beyond the unknown darkness.

Not by his own choice, but by someone else’s.

Leaving here everything he had wanted to protect, but in the end had failed to save.

*…No. Anything but that.*

In that instant, Jin Mukyung clenched his teeth.

He forced his fading consciousness awake and screamed silently in his heart.

Everything he could?

What did that even mean?

How could he accept death so weakly?

If he was still alive, then it wasn’t over until his last breath was gone.

He had to get up. He had to fight until the very moment his pounding heart stopped.

*I—I…!*

His fingertips trembled.

The taste of blood filled his mouth between his clenched teeth.

But the body he’d tried to rouse, even by biting his own tongue, had long since reached its limit. The cruel reality didn’t change.

*Whoosh.*

The sound of something cutting through the air rang clearly in his ears. In his blurred vision, the slanting flash seemed unusually slow.

Slow enough for him to look back on his entire life.

Slow enough for him to think of the most irritating person in the world.

*If you’d been here in my place… things would’ve been different. Everything.*

As the spearhead fell toward his head, Jin Mukyung sent his words into the void, where they would reach no one.

To his only younger brother, who wasn’t here.

*Looks like I won’t be able to keep that promise after all.*

Two years ago, the brothers had made a promise with the wall of the training hall between them.

They’d meet at the Star-Array Grand Banquet.

At the feast of countless stars that illuminated the world.

In the end, Jin Mukyung had failed to keep that promise.

Because he’d been ashamed. Because he felt his own achievements were nowhere near enough.

When he’d first picked up a sword, he’d wanted to become a great martial artist. After that, he’d wanted to become the pride of the Jin Family of Taiyuan—and a younger brother his elder brother could be proud of.

But there had been another reason, the greatest one, that he’d spent the past two years swinging his sword without rest in suffocating darkness.

He’d wanted to become a brother who could hold his head high.

He wanted to become strong enough to surpass the wall that was Cheongpung, so his younger brother, who’d become the Divine Dragon and soared freely through the sky, wouldn’t be ashamed of him.

But…

*So this is how it ends.*

Jin Mukyung, the Heaven Shaking Sword.

The time of opportunity granted to a young genius, overshadowed by other monsters, was over.

The sword he’d honed in the dark had shone brilliantly enough to light up this gorge today, but that fleeting ray would be swallowed by the long, deep night.

Forever.

*Damn it.*

Jin Mukyung struggled to lift his half-closed eyelids.

Refusing to close his eyes even in the face of death was his pride as a martial artist and proof that his fighting spirit remained unbroken. It was also his chance to say one last goodbye to his troublesome younger brother.

Even if his voice would reach no one.

“…I’m sorry.”

And just as the words were forced through Jin Mukyung’s lips—

*KABOOOOOM!*

The sky and earth shook.

Jin Mukyung’s world, dark and hazy until then, turned blue-white. The flash falling toward his head abruptly changed course, whipped aside.

Toward the terrible heat that came crashing in faster than light, faster even than the sound of the explosion.

No—to a spear carrying that terrible heat.

*Wooooom.*

The wind vanished. The air stopped.

The two currents of energy met for an instant, embracing the space around them for dozens of *zhang* before swelling enormously.

*KWAaaaa!*

A tremendous shock wave tore across the gorge, its roar deafening.

Lying in the deep pit, Jin Mukyung reached out on instinct.

He clutched the unconscious Cheol Mubaek and Wipeng with all his strength, and watched as the corpses of men and horses, along with countless chunks of rock, were swept up like leaves in a storm and hurled in every direction.

In the distant flash of light that engulfed everything around him, he also made out someone’s hazy back.

*Cough.*

Jin Mukyung spat up dark-red blood and suddenly wondered if he might already be dead.

Perhaps, unable to let go of his attachments from life, he was seeing things even after death.

But…

*No.*

It was vivid.

Everything he could see, hear, and feel in that moment was too real to believe it could be granted to the dead.

The stinging pain in his skin where the rock fragments had scraped past. The muscles screaming throughout his body. The blood surging from his insides, twisted by severe Internal Injury.

And, finally, the familiar voice that reached his ears.

“What are you throwing up for? Did you drink too much last night?”

Jin Mukyung’s body went rigid.

His eyes flew wide, a storm raging in their depths.

It was certain.

Not a hallucination. Not a trick of the ears.

This was…

“I’d pat you on the back, but, well, the situation’s a little tricky.”

The voice came through clearly, beyond the roar that was slowly dying away.

The figure stood out in the fading light.

That irritating voice alone was enough to make his fist clench.

The back of the wastrel, who had somehow grown broader and sturdier than his own.

“You…!”

Where had that strength come from?

Jin Mukyung squeezed out a voice rough as scraping metal and raised his hand.

His fingertips trembled like a leaf in a storm, his body already past its limit, as he reached for his only younger brother’s sleeve.

*Rustle.*

A tiny sound of friction, so faint he had to strain to hear it.

Perhaps it was the wind, not Jin Mukyung’s hand, that brushed the edge of his tattered robe.

But that was enough.

What he wanted to convey wasn’t just a touch. It was his desperate wish for his brother to protect everyone.

*Thud.*

His hand fell limply. His whole body went slack.

At last, after spending every last bit of his strength, the pathetic older brother lost consciousness.

Before him stood his wastrel younger brother, returned from two years away.

He faced an unfamiliar, graying middle-aged man who stood a dozen *zhang* away, staring straight at him with a somber gaze.

“I have one question.”

Flames poured from his eyes. His voice, by contrast, was cold as ice.

“Was it you who beat up my hyung?”

The wastrel had returned.

As a dragon whose roar shook the heavens.

Beyond his low voice, the people of Shanxi raised tearful cheers that rang out through the gorge.

* * *

A little while ago, someone had told me:

Don’t try to carry everything alone.

Try trusting them a little more.

And in that moment, I realized that person had been right.

I could tell as soon as I reached the battlefield.

Blood was everywhere. Severed limbs had fallen from bodies I couldn’t identify, and countless corpses of people and horses had piled up into small hills, filling the narrow gorge.

Most of them were nomads.

The enemy outnumbered us by at least two to one. But even with the odds stacked against them—not just in numbers, but in fighting strength—the people of Shanxi hadn’t given in.

No. They were squeezing out every last bit of strength to fight back.

The Imperial Army. The martial artists. Even ordinary people who hadn’t learned so much as a single move of martial arts.

And, finally, Jin Mukyung.

*They did everything they could. They even overcame their fear of death.*

I already knew how hard it was for the weak to stand against the strong.

And I’d taken Jin Mukyung’s wish to heart: there must be no more sacrifices like theirs.

*Wooooom. BOOM!*

I reached out, and a spear buried deep in the cliff twisted like a living creature and came flying toward me with a thunderous crash.

White Flame, back from its brief journey, trembled faintly in my grasp.

The blue-white flames coiling around its blade lit up the pitch-black darkness, heating the cold night air as they surged toward the enemy before me.

> **System**
> Lv.??? Murong Baek

The silver-haired, middle-aged man stood gripping a dark, ashen spear shaped much like the charging spears used by the nomads.

I’d be lying if I said the System window I read with my razor-sharp Qi Sense hadn’t caught me off guard. But the reality before my eyes was the truth.

I looked at him with a steady gaze—the Family Head of the Murong Family, whose name I’d heard but never met.

Another blade Dark Heaven had hidden in the vast forest of the Central Plains’ Murim: the North Heaven Demon Lord.

“I asked you. Was it you who beat up my hyung?”

The North Heaven Demon Lord was silent for a moment before he spoke.

“Well, this is a problem.”

His gaze swept over me. He let out a small sigh at the uninvited guest who’d shown up.

“A headache, in more ways than one.”

I bet it was. In more ways than one.

I raised my spear, ready to strike at any moment, and answered.

“Why the headache? You’re making me worry.”

It didn’t matter why or when the Family Head of the Murong Family had become Dark Heaven’s lackey.

I had only one thing to do: take down Murong Baek, without a doubt the North Heaven Demon Lord, and the nomad behind him, standing there with a thoroughly stiff expression.

“So why not just crack your skull while we’re at it? Then it won’t hurt anymore.”

*Step.*

The North Heaven Demon Lord took a step forward and replied calmly.

“That’s a treatment I’ve never heard of.”

“I know more about medicine than I look. I learned by watching the Divine Physician.”

“Maybe. Even so, I suspect that method would be a problem.”

The North Heaven Demon Lord looked at me with a clear gaze that seemed to see through everything, then added:

“Especially in your current condition.”

I wanted to deny it, but his judgment was accurate.

I’d paid a steep price to cross ten thousand *li* without proper sleep, meals, or time to circulate my qi.

So I answered without hesitation.

“Yeah, you’re right.”

*Step.*

The footsteps that had been steadily closing the distance suddenly stopped. The North Heaven Demon Lord furrowed his brow as he looked at me.

“What did you say?”

“I said you’re right. Honestly, as I am now, it’d be pretty tough. No, really tough.”

“What are you…”

His voice trailed off. I shrugged at the North Heaven Demon Lord, who was staring at me as if I were crazy.

“So I brought someone along. Figured I might as well.”

Before the North Heaven Demon Lord could understand what I meant, two cutting whistles swept through the air.
## Chapter artifact 971

# Chapter 971

Human senses provide far more information than you might imagine.

That was especially true of martial artists, whose five senses were incomparably sharper than those of ordinary people.

Living by the law of the jungle, they honed those senses through brutal training until they could detect events unfolding far beyond what the naked eye could see.

Just as the North Heaven Demon Lord did now.

“So, while I was at it, I brought someone I know.”

Jin Taekyung, the Blazing Flame Divine Dragon.

The moment the North Heaven Demon Lord heard the easygoing voice of the young upstart, who looked plainly exhausted despite the overwhelming force of his arrival, alarm bells went off in his head.

Along with it came the title and name of someone who naturally sprang to mind.

*The Fire King, Jeok Cheongang.*

A giant who straddled the orthodox and unorthodox factions, an old monster of Mount Jiuhua.

And a master, too—the man who had taken the wastrel Third Young Master of the Jin Family of Taiyuan as his Disciple.

The North Heaven Demon Lord’s eyes widened as he thought of him.

*If that’s the case…*

The North Heaven Demon Lord was certain.

He didn’t know when or where things had gone wrong, but something had.

Not every plan went exactly as intended. Still, at the very least, Jin Taekyung and Jeok Cheongang were not supposed to be here.

*The information leaked.*

But that thought never led to the question of who had leaked it, or how.

No—that wasn’t quite right. He hadn’t even been given the chance to wonder.

*Whoosh! Whoooooom!*

One sound was quiet yet swift. The other was like a furious gale, whirling out of control.

The two streaks of sound reached him through senses that had gone beyond the five and touched the sixth. The North Heaven Demon Lord furrowed his brow.

Not one. Two.

That meant something.

More than the fact that the sounds had come from the cliffs to either side, not from the ground ahead.

*KABOOOOOM!*

A thunderous crash rang out from the top of the cliffs, more than thirty *zhang* high.

Mixed with it were the horrific screams of many people. It sounded like thunder.

Thunder that swallowed someone’s life and summoned an untimely shower.

*Drip. Drip-drip.*

Jamukha, who’d been standing beside the North Heaven Demon Lord, silently looking up at the shadowed cliff, suddenly felt a hot liquid touch his face.

Red, sticky blood.

“……!”

Jamukha’s lips trembled. The North Heaven Demon Lord’s gaze sank, dark and still.

They both knew what it meant.

Annihilation.

The nomads they’d sent up the cliff at considerable cost were gone.

They had all been killed or captured in less time than it took to blink.

And the most important thing to the North Heaven Demon Lord was the identity of the two monsters who’d swept across the cliff in an instant.

“One of them is obviously your master. Who’s the other?”

At the North Heaven Demon Lord’s dry question, the young monster—still a little green—put on a stern expression and replied.

“Now, now. You should figure it out for yourself. What kind of upbringing did you have, asking to peek at the answer sheet at your age?”

For a moment, the North Heaven Demon Lord felt an urge to crack open Jin Taekyung’s skull and see what was inside. But the monsters on the cliff wouldn’t even let him take a step.

*Shwaa!*

The narrow gorge lit up. The North Heaven Demon Lord swung the spear in his hand without hesitation toward a streak of light hurtling through the air.

*BOOM!*

The crash was too loud to have come from two metal blades clashing.

The flash ricocheted from the impact and buried itself deep in the ground. The North Heaven Demon Lord frowned as he recognized it.

“A charging spear?”

No doubt about it. It was the most ordinary sort of charging spear used by the nomads of the steppe.

And yet the strike had been so swift it was hard to believe it was a simple throw.

Like an arrow shot by someone.

*Wait. Then could it be…?*

The North Heaven Demon Lord suddenly looked up.

Just then, moonlight slipped through the scattered clouds, revealing a woman holding a bow so enormous it could have been mistaken for a long spear.

“……The Bow Saint.”

The words left his lips like a groan.

At the same moment, flashes rained down once more.

*KABOOOM!*

The bowstring moved too fast to follow, and the sound of its release rang through the gorge.

The Bow Saint had fired more than ten charging spears as lightly as arrows. Now she slowly pulled the bowstring back, gathering her strength.

*Wooooom.*

Space trembled.

Along a silver line formed from internal energy, a brilliant mass of power took shape like an arrow. Then it shot forth, carrying immense force.

Not toward the North Heaven Demon Lord, but toward the other enemies.

*FWOOSH!*

The deep darkness tore open.

Everyone on the battlefield could see that dazzlingly destructive flash.

The Shanxi martial artists, hacking their way through the enemies in the gorge with hoarse, unrelenting battle cries.

The nomads being slaughtered helplessly by them.

And the martial artists of the Hebei Peng Family, fighting desperately in the broad basin beyond the gorge while surrounded by nomads and the Murong Family.

“What in the world is that—”

The Keshik centurion had only just spotted the dozen or so streaks of light raining down from the sky. He had no idea that the bewildered words leaving his lips would soon be his last.

Nor that those streaks of light would be the last thing he and hundreds of his comrades saw in this world.

*KABOOOOOM!*

The earth turned over with a terrifying crash.

Someone’s arms and legs shot up amid fountains of blood. Flesh and pieces of organs—some so mangled they were barely recognizable—flew in every direction.

*Krrrsh. Splatter.*

Blood and flesh pattered down onto the ground, their late arrival ringing in everyone’s ears.

Peng Cheolyeong, Family Head of the Hebei Peng Family and the Iron Blood Saber, had been covered in blood, surrounded on all sides because of the Murong Family’s betrayal. He blinked blankly.

*What just happened?*

With his back to the gorge, he’d been fighting dozens of enemies alone. He hadn’t seen a thing.

He’d only felt the sky brighten. A chill had run down his spine, and his instincts had made his hand stop.

And… and that was all.

When he shut his eyes against the dazzling light stabbing into them, then opened them again, the enemies that had filled the area had vanished.

No. To be precise, they were still there.

Just no longer in a shape that could be called human.

Some had lost their upper bodies. Others had been torn apart, limbs missing.

“Ugh—aaah!”

“Graaaah!”

The body feels pain first, but the brain is what understands it.

Only when they grasped the unbelievable reality did the survivors let out desperate screams.

Unlike the hundreds swept away by the flash, those lucky enough to survive writhed in pain. Before the horrific screams that had frozen everyone in place could die down, the sky lit up once more.

*FWOOSH.*

In that moment, Peng Cheolyeong understood.

That dazzling beam of light—which he would normally have stared at in a daze—meant death.

And that death was not meant for him or the martial artists of the Hebei Peng Family.

“Attack!”

Fear is contagious. Hope catches fire.

With the brilliant flash over the basin of blood and corpses behind them, the martial artists of the Hebei Peng Family surged forward, ripping apart the encirclement that had already crumbled.

Their fierce cries rang out loudly enough for everyone on the battlefield to hear.

Loud enough to echo all the way into the depths of the narrow gorge in the distance.

“Sounds nice. Not for you, though.”

The North Heaven Demon Lord silently watched Jin Taekyung’s smiling face.

The young bastard’s eyes were deep and steady, despite his mischievous voice. In them, the North Heaven Demon Lord saw his own face, stiff with tension.

*The Bow Saint.*

He hadn’t anticipated her presence.

She was a ghost from the distant past, far too long gone to appear here.

“So that’s why you were so relaxed.”

After a brief silence, the North Heaven Demon Lord finally spoke. It seemed he’d pieced together the general situation.

“So it was the Imperial Palace.”

With the Bow Saint’s appearance, the scattered threads in his mind came together.

Why Jin Taekyung could have appeared here. Whether Dark Heaven’s plan centered on the Imperial Capital had succeeded.

And finally, where the Bow Saint had been staying after vanishing without a trace.

“But how did you figure it out so quickly?”

Jin Taekyung answered the North Heaven Demon Lord’s sudden question.

“Your friend told me.”

“My friend?”

“The Eastern Heaven Demon Lord.”

“……!”

“So you should’ve been a little friendlier. Had meals together more often, swapped catalog numbers like any upstanding members of the martial world. Well, I’m just glad I found out before it was too late.”

Jin Taekyung shrugged with an obnoxious look, then added:

“When you see him in a bit, thank him for me. He deserved to die, but at the end, I found myself a little concerned about him.”

The North Heaven Demon Lord understood what he meant and smiled bitterly.

“I’ll have to politely decline.”

“What, were you two really that unfriendly? Were you in a love triangle or something?”

“Crazy bastard. Does your tongue ever get tired?”

“I was about to stop anyway. I can move a little now.”

The smile lingering on Jin Taekyung’s lips faded.

He had already shaken off the weakness left by the strike he’d launched with all his strength to save Jin Mukyung, exhausted as he was.

“Thanks. For waiting until I caught my breath.”

The North Heaven Demon Lord looked at him with a subdued gaze.

He hadn’t given Jin Taekyung time of his own accord. He’d simply had no choice, because someone else had forced him to.

“Enough of this. Why don’t you come out now, Fire King?”

At the North Heaven Demon Lord’s words, addressed to empty air, a figure that had blended into the darkness drifted gently down.

“What a shame. If you’d taken even one step, I’d have burned your limbs off.”

“I wonder if you really could.”

As he replied, the North Heaven Demon Lord gripped his spear at an angle.

From the spearhead surged an unprecedented power—one that Jeok Cheongang had never sensed in the distant past, when they’d faced each other on the battlefield.

“You’ve grown bold, haven’t you? A mere pup, speaking to this old man like an equal and even daring to act tough.”

Jeok Cheongang grinned, baring his teeth. White hellfire rippled over his outstretched hands.

“When did you start working with them?”

“What a strange thing. The two of you, who were like cats and dogs, asking me the same question here today.”

At that moment, the smile disappeared from Jeok Cheongang’s lips.

He knew whom the North Heaven Demon Lord meant—and that his life was hanging by a thread.

“……My Disciple owes the Peng bastard a great debt. I’ll repay it with your life.”

“You’ll both be going together—to the afterlife.”

The North Heaven Demon Lord replied calmly, then tossed what he was holding into his mouth.

*Slip.*

A red pill melted across his tongue. At the same time, Jin Taekyung’s spearhead flashed behind him.
## Chapter artifact 972

# Chapter 972

Jeok Cheongang and Jin Taekyung.

Jin Taekyung and Jeok Cheongang.

From the moment it all began, Master and Disciple moved as if they were one.

And as the heat drew close in a single step, hot enough to set his whole body ablaze, the North Heaven Demon Lord realized once more:

He had made the right choice.

To make this plan—which had gone wildly off course from what he’d expected—succeed, he had to use everything he’d been given as quickly as possible.

*Fwoosh!*

Hot. The world before him turned red.

As the world slowed, the North Heaven Demon Lord felt a heat that seemed to burn through his entire body.

But it wasn’t only the power of the Fire Gate Divine Technique, passed down for more than three hundred years, that made him feel that way.

*KABOOOOOM!*

A tremendous roar, audible only to the North Heaven Demon Lord, reverberated from deep within his body.

At the same time, the qi throughout his body surged.

Lava-hot energy raced through hundreds of acupoints, swelling and surging as if it might burst at any moment.

A colossal wave of power, born from some strange artifact he had never once used, was partly tearing down the high, sturdy wall that had always stood in his way.

*Ah…!*

The North Heaven Demon Lord groaned amid a haze of pain and ecstasy.

Everything in his reddened field of vision—or even things he couldn’t see—felt slow and vivid.

The wind. The air. The qi held within it.

And the two streams of flame rushing toward him, smashing everything in their path to pieces.

*So this is what it feels like. This is what it is.*

The North Heaven Demon Lord thought.

He felt he could almost understand the world the Heavenly Demon had seen as he ruled over the Ten Thousand Demonic Paths with heaven-reaching martial prowess and sought to conquer the world—and the world the Martial God had seen when he defeated him and brought peace to it.

Perhaps that was why he could smile, even amid heat so fierce it melted his Body-Protecting Qi.

*Whoooom.*

Perhaps that was why their movements looked so slow and weak.

*Is that all you’ve got?*

The scenery changed with the vantage point.

In that moment, seized by the sensation that the Temporary Strength Pill had carried him over the summit and above the clouds, the North Heaven Demon Lord looked down on them with disdain.

He surveyed the entire battlefield beyond the narrow gorge, even the old monster and the young Divine Dragon—men whose very names made the land tremble.

At the same time, he flung out both arms with a speed and power he had imagined countless times, yet always felt as distant as a dream.

*Fwoooosh!*

Space warped under the unprecedented energy. A spearhead and a fist, their forms obscured beneath dark crimson Force, shot in opposite directions.

Toward the foolish descendants of the Fire Gate Clan, who dared not recognize the power of an absolute being.

*Die.*

In the North Heaven Demon Lord’s red-hot vision, Jeok Cheongang and Jin Taekyung stared wide-eyed at the overwhelming power before them.

The dark crimson Force swept toward them like a wave.

*KABOOOOOM!*

The entire gorge shook. The shock wave swelled and exploded, sweeping everything within a radius of more than ten *zhang*.

No—“stole” and “swallowed” would have been better words for it.

The blinding light and thunderous noise robbed everyone in the gorge of sight and hearing. Everything within reach of the shock wave was erased, unable to hold its shape.

*Rrrrrumble!*

Part of the cliff collapsed, unable to withstand the aftershock.

The pools of blood and countless corpses scattered all around had vanished into dust. In their place, the North Heaven Demon Lord drew a slow breath.

He shuddered at the power welling up without end from deep inside him, even after that outburst—and at the thought that he himself had unleashed a calamity like a natural disaster with his own two hands.

Then he turned his head and looked somewhere beyond the choking silence and clouds of dust.

No—he sensed it.

The presences that had survived this horrific disaster, not yet entirely extinguished.

“You managed to survive. As you should have.”

The North Heaven Demon Lord’s voice was calm and relaxed.

The Temporary Strength Pill had given him martial prowess far beyond what he’d possessed only moments ago. Still, he had never expected to win with a single strike.

His opponent was the old monster of Mount Jiuhua, returned stronger than he’d been fifty years ago. And his Disciple had grown beyond a young prodigy into a towering figure, leaving his mark on this vast land.

Even so, the North Heaven Demon Lord could remain at ease because he knew better than anyone the size of the enormous power throbbing within him, ready to burst.

Even if someone else intervened, that wouldn’t change.

Just as it hadn’t now.

*Whoom! KABOOM!*

In the blink of an eye, a mass of concentrated energy struck the spearhead the North Heaven Demon Lord had swung, bouncing off from an unseen blind spot.

The North Heaven Demon Lord’s lips curved into a faint smile as he looked toward the figure standing atop a fractured, crumbling cliff, more than thirty *zhang* high.

“You’ve had a rough time, Bow Saint.”

The North Heaven Demon Lord had now taken the latest attack and confirmed it once more. His martial prowess was above the Three Saints.

He had set foot, if only by one step, into the realm of those called the Invincible or the absolute.

*KRAKAKAKANG!*

A mass of light packed with such tremendous power it could hardly be called an arrow.

The North Heaven Demon Lord deflected a barrage of those flashes, each powerful enough to kill even a skilled Peak master with one strike. His smile deepened.

“You should’ve come a little slower. If you’d taken your time and saved some strength, a lot might have turned out differently.”

The distance from Zhejiang Province, where the Imperial Capital stood, to Shanxi Province was well over a few thousand *li*.

And for those three to have crossed that distance and appeared here without catching the North Heaven Demon Lord’s attention meant they’d moved faster than a messenger eagle or a courier.

They had rushed here, unwilling to spare even a moment, without proper rest to prepare for battle.

That guess was enough to convince the North Heaven Demon Lord that victory was certain.

“Unfortunately, it’s too late to turn back now.”

*Shhhh…*

Dark crimson energy rose from his whole body like heat haze.

Watching the Bow Saint’s attacks bounce off without penetrating his highly condensed Force, the North Heaven Demon Lord was swept up in a stronger exhilaration than he’d ever felt.

An absolute being.

Here, today, he was the absolute being.

The two Master and Disciple of the Fire Gate Clan, who must be collapsed and groaning beyond that cloud of dust, and even the Bow Saint could not stand against him now.

They were all exhausted, while his power continued to well up without end.

*Crack.*

A deep rumble spread from the tip of his foot as he stepped forward lightly.

A colossal power that had frozen everyone in the gorge.

An unprecedented energy no one had ever imagined a human could possess expanded his dantian and raced through hundreds of acupoints.

The North Heaven Demon Lord laughed aloud, thinking:

*It feels like I could do anything right now.*

No—he could.

And just as the North Heaven Demon Lord’s senses stretched endlessly and wrapped around the entire gorge—

—Old Master, that bastard’s laughing.

—Leave him be. He must think he’s the Lord of Heaven just because he took a Temporary Strength Pill.

The North Heaven Demon Lord’s smile vanished as two voices exchanged words through Sound Transmission in the dust cloud that had yet to settle.

—Uh, he’s not laughing anymore.

—He was ugly to begin with, but now he’s scowling. His face looks like shit.

—Why would you say it like that? My little guy is handsome and looks plenty clever.

—All right, I get it. Take your damn hand off your pants right now, before I turn you into a eunuch with one palm strike.

The North Heaven Demon Lord’s eyes sank. His gaze, carrying unmistakable confusion and shock, turned in one direction.

—Uh, he’s looking this way.

—Must’ve just gotten lucky. This old man knows at a glance.

—We need to jump him all at once. What if he’s spotted us? Why don’t you move a little to the side?

—I was about to. Stop pushing me. How dare you touch this old man’s body?

—That’s not a hand.

—Huh?

At that moment, the North Heaven Demon Lord’s mouth twitched.

“Come out.”

At the low words that slipped between his lips, a breathless silence descended.

No—more precisely, it seemed to.

—He says come out. He’s looking right at us.

—Didn’t I tell you? He definitely guessed.

—I don’t think so. Wait, can he hear our Sound Transmission?

—So he took a little pill. So what? There’s no way that bastard can do that. I’ll stake that Hyuk bastard’s balls on it.

*Tap.*

As if the last thread of his patience had snapped, a cold voice slipped through the North Heaven Demon Lord’s clenched teeth.

“What a shame. Whoever that is, he’s going to lose his balls.”

At last, he received the answer he’d been waiting for.

*Poom!*

Beyond the dust cloud, which split as if a sword had cut through it, Jeok Cheongang emerged in tattered clothes. He brushed the dirt from his shoulder and replied:

“That’s fine. Just in case, I didn’t stake my own.”

Behind his Master, who’d uttered something so embarrassing with an unnecessarily solemn expression, his Disciple—several heads taller—spoke with an uneasy look.

“Why stake the balls of someone who isn’t even here? You won’t need them anyway. You might as well stake your own.”

“Isn’t that true of you, too?”

“Hey, now you’ve crossed a line. Why would you say—”

*KABOOM!*

A thunderous crash swallowed the words before they could continue.

And not long after, a cough sounded.

“Cough. Jeez, look at all this fine dust. Wouldn’t want anyone thinking you’re not a Chinese bastard.”

“Ahem. Don’t be a baby. You’ll bring shame on the Fire Gate Clan.”

“My God, is there even more shame left to bring?”

At the sight of Jin Taekyung and Jeok Cheongang standing there unharmed, the North Heaven Demon Lord’s gaze sank.

*How…?*

The attack hadn’t been at full power, but they’d dodged a strike backed by more than seventy percent of his strength. That proved they still had plenty in reserve.

The North Heaven Demon Lord had no choice but to admit that, at some point, he’d come to trust too much in the power he’d been given.

And with it came the realization that he’d underestimated the enemies before him.

“Jamukha.”

At the quiet call that slipped from the North Heaven Demon Lord’s lips, the hunting dog he’d commanded for decades answered.

“Give your command, my lord.”

“We won’t wait any longer. Change the plan.”

“You mean…”

“I will not tolerate any more interference. Before things go wrong, use every last bit of our strength and wipe them out at once.”

Jamukha understood exactly what the North Heaven Demon Lord meant by using every last bit of their strength.

Today, the Thunderbolt Saber King and the Hebei Peng Family had been invited guests on this battlefield. The three Supreme Peak masters who had appeared unexpectedly, however, were uninvited.

The die had been cast. They had to secure victory before the whole game was overturned.

As the North Heaven Demon Lord had just done, they would bring every means at their disposal to bear.

“Understood.”

With that curt reply, Jamukha pulled the cord of the signal flare he’d taken from his robes without hesitation.

*Fwish! Fwish! Fwish!*

Smoke rose into the night.

The Bow Saint’s arrows of light swiftly swept away most of the smoke, but even she couldn’t catch every wisp that scattered through the air.

*Poom! Poom! Poom!*

Fireworks blossomed across the blackened sky.

At his master’s command, Jamukha had let the countless hunting dogs under his command off their leashes. Now he tipped the Temporary Strength Pill he hadn’t been able to take because the North Heaven Demon Lord had stopped him into his mouth.

Beyond the gorge, the Keshiks who had just seen the signal did the same.

*Swish. Shhhh…*

Red heat haze began to rise throughout the battlefield.
## Chapter artifact 973

# Chapter 973

The word *unavoidable* applied to everyone.

To farmers who faced drought before the harvest, and to the sick, lying in bed and waiting for death to draw closer by the moment.

And to a woman whose astonishing power made it hard to believe she was human like them.

*I should have stopped them.*

The Bow Saint let out a low groan.

High atop a sheer cliff, she stared down at the ground. Reflected in her eyes was a group of people spewing streams of ghastly blood-red light.

*Shhk! Krrrunch!*

Every one of them had bloodshot eyes. A thick mist of blood gathered in the wake of their heedlessly advancing spears and blades.

In this vast battlefield, where tens of thousands clashed, two hundred was only a handful. But thanks to the effects of the Temporary Strength Pill, each of them had broken past their limits—and they were more dangerous than anything else.

Especially to the Hebei Peng Family’s fighters, of whom only about two thousand remained.

*Graaaah!*

A harrowing scream rang through the night air.

As their enemies finally broke through the Hebei Peng Family’s vaunted Linked Tyrant King Formation, the Bow Saint lowered her taut bowstring and bit her lip.

The enemy was not only dangerous, but clever.

After suffering heavy losses from the Bow Saint’s attacks several times over, they had immediately split up. They had plunged straight into the heart of her allies’ formation to guard against her follow-up attacks.

*If I keep attacking like this, my allies will get caught in it too.*

Even without the two hundred or so Keshiks, there were more enemies than she could handle, and more appeared with every passing moment.

The steppe army seemed endless, no matter how many she killed.

The battle had already dragged on for several *shichen*. The steppe army had certainly suffered far greater losses than the people of Shanxi—and yet, nearly twenty thousand soldiers remained.

It was obvious that if she stayed on the high ground atop the cliff and rained arrows down on them until she ran out of strength, she could inflict tremendous damage.

But there was only one choice before her.

For every gain, there was a loss.

If she kept attacking, she could take down countless enemies. But by then, every last fighter of the Hebei Peng Family would be dead.

She had made up her mind. There was no need to hesitate any longer.

*I have to go. I have to do it myself.*

*Click.*

She twisted the enormous bow with all her strength. Two strangely shaped curved blades appeared.

Feeling their cool touch in both hands, the Bow Saint kicked off the cliff and soared into the sky.

*Whoosh.*

The cold night wind brushed her whole body, setting her long hair fluttering.

As if stepping on invisible stairs, she moved through the empty air toward the ground. Then she suddenly turned her head to look behind her.

Deep inside the narrow gorge, amid the waves of powerful qi, she silently addressed someone in a place now swallowed by darkness and hidden from view.

*Survive. Then prove yourself once more.*

The Chosen One.

The Blazing Flame Divine Dragon, Jin Taekyung.

With his name weighing heavily on her heart, the Bow Saint plunged toward the distant ground.

*Shwaa!*

The two curved blades in her hands became razor-sharp winds, carving through space.


* * *


The Bow Saint was gone.

She had left for another battlefield beyond the gorge.

Not to help me and Jeok Cheongang, who remained here, but to aid the Hebei Peng Family’s fighters.

Even as I watched her disappear far away across the open sky, I didn’t feel hurt that she’d left. Jeok Cheongang met my eyes and simply nodded, his expression calm.

Of course, there was someone else here who felt differently.

“I expected as much, but it still amazes me.”

The North Heaven Demon Lord spoke up out of nowhere, then continued without waiting for a reply.

“Why do you people always choose such foolish options? Every single time.”

He shook his head with a hollow laugh. I replied calmly.

“Sure. Guys like you would never understand, even if you died and came back dozens of times.”

The North Heaven Demon Lord thought of his followers as nothing more than pawns to secure victory. He could never understand that all of us here were risking our lives not to kill someone, but to protect someone.

And that the small difference between those two things was the most important measure separating the righteous from the demonic.

“What a rotten age. The Murong Family Head goes and stabs someone in the back, then starts popping pills the moment things get a little rough. Right?”

Jeok Cheongang spoke up in response to my question.

“If you live long enough, you’ll occasionally meet things worse than beasts. Creatures wearing human skin and pretending to be people, living with fine words and smiles while hiding the darkness in their hearts.”

His voice was cold, but his eyes burned hot.

At that moment, Jeok Cheongang’s anger was directed entirely at the North Heaven Demon Lord.

“I used to think you just had a sly streak… If I’d known it would come to this, I should have killed you back then.”

He was the North Heaven Demon Lord to me, but Murong Baek to Jeok Cheongang.

Unlike me, a man who had never met him before, Jeok Cheongang had once fought on battlefields alongside him as a comrade. The two men’s eyes met in midair.

“Why didn’t you, Fire King? That must have been your first and last chance to kill me.”

At the North Heaven Demon Lord’s mocking reply, Jeok Cheongang’s eyes sank.

“Your first and last, you say. Do you truly believe that?”

“You don’t?”

*Rrrrumble.*

The space around them shook as if an earthquake had begun. A mighty aura rose from the North Heaven Demon Lord’s whole body, pressing down on everything around him.

It was rougher and greater than Jeok Cheongang’s—an unprecedented force.

“I’ll make it clear to you now. You’ll never get a second chance.”

As his low voice sank into everyone’s ears, the North Heaven Demon Lord vanished.

*Swish.*

His movements outpaced even the faint whistle of his passage.

But I could see him, if only faintly. No—I could sense him.

The North Heaven Demon Lord’s figure shot forward, faster than the speed of sound.

I sensed his spearhead sweeping through space—and the loyal hunting dog rushing after its master.

*Shwaa!*

A belated gust of wind rose in the wake of the descending spearhead.

At that instant, I swung White Flame up toward the flash of light driving into my upper body.

*BANG!*

The roar was impossible to believe had come from two spears colliding.

The tremendous pressure traveled from White Flame’s spearhead to my toes. The ground split into a spiderweb of cracks.

Beyond the blocked spearhead, I met the North Heaven Demon Lord’s eyes for a split second. It felt as though an inaudible voice rang in my ears.

*How can a brat like you…?*

I knew that look all too well.

The wide-open eyes. The question mark within them.

And every enemy I’d faced up until now had to replace that question mark with an exclamation point before its echo had even faded.

Just like now.

*Ka-drrrk!*

I gritted my teeth and thrust the shaft of my spear upward.

The muscles throughout my body swelled as if they were about to burst. A power no one but me could understand—supernatural powers—surged up and shook off the tremendous pressure bearing down on the spearhead.

*KABOOOOOM!*

At the very moment the North Heaven Demon Lord’s eyes widened and his body was driven back by the thunderous crash, the hunting dog reached its destination a step behind its master and bared its teeth.

*Shwaek!*

Before the dust cloud kicked up by the shock wave could even rise, it split apart.

A curved blade swept through space in a flash, trying to split the top of my head. Then the air behind me flared with heat.

*Fwoosh.*

A terrible heat, as if a mere touch could melt someone’s flesh and bones and burn even their soul.

*Flame Divine Palm.*

The instant I felt that familiar energy swell, I ducked without a moment’s hesitation.

*Paaang!*

A mass of concentrated flame skimmed past the back of my head.

Feeling the back of my head grow hot, as if it had been scorched, I looked up again. The old nomad, who had been swinging his curved blade down like a beast, was already flying backward at tremendous speed.

*Krrrunch!*

A deep furrow stretched behind his heels.

Jeok Cheongang sniffed at the old nomad, who had been driven back nearly three *zhang*.

“Damn it. I was wondering where that horse shit smell was coming from. Turns out some barbarian wandered in.”

“……!”

“Your face is quite a sight. What, after getting a taste of that fiery welcome, do you miss the steppe, full of horse shit and weeds?”

Style may be temporary, but class is forever.

Just as the old nomad’s face went stiff at Jeok Cheongang’s inspired verbal assault, a low voice rang out.

“Still the same. That tongue of yours, always twisting people’s insides.”

One word for Jeok Cheongang. At the same time, the North Heaven Demon Lord’s gaze stayed fixed on me.

Jeok Cheongang tapped my shoulder.

“When it comes to running his mouth, this brat is several steps ahead of this old man.”

“He’s surpassed his Master in all the wrong ways.”

Jeok Cheongang let out a quiet laugh.

“Come now. You know it isn’t just that.”

The North Heaven Demon Lord said nothing. He simply looked at me with an expression that said he couldn’t make sense of me.

In truth, it was only natural that he felt that way.

And it wasn’t just the North Heaven Demon Lord. Anyone would.

The Blood Lord, the Western Heaven Demon Lord, the Southern Heaven Demon Empress, and the Eastern Heaven Demon Lord.

And all the other enemies I’d faced.

To them, my existence was an incomprehensible mystery, something they couldn’t make sense of no matter how they looked at it. Not one of the enemies I’d encountered had found the answer, and as time passed, the question had only grown.

No—more accurately…

*I’d gotten that much stronger.*

Looking back, every battle I’d fought amid the countless events of the last two years had been hard.

My enemies were always strong, and I was always weaker than they were.

I’d had to struggle with everything I had just to survive, just to win.

But then, one day, I suddenly realized something.

The reason I was constantly standing at the crossroads of life and death wasn’t that I was weak. It was that even stronger enemies kept appearing.

At some point, I’d started catching up to them.

The Head Elder, whose martial prowess had been so mighty. Pung Yang, whom I’d barely managed to defeat in a joint attack with Jin Mukyung.

The Demon Lords and Demon Empresses of Dark Heaven, each of whom had possessed power that made them nightmares all on their own.

When I traced back through those fights with the enemies who’d brought me to the brink of death time and again, I’d sometimes find myself thinking:

*Back then. If I’d moved like this in that moment, I could’ve won so much more easily.*

Now I understood.

What I’d thought was nothing more than regret and lingering misgivings was proof that I’d grown.

Beyond the numbers shown in the System window, it was a clear sign that I’d developed as a martial artist.

And maybe that growth was continuing even now.

“Hey. This is just something I’m curious about, so I’m asking.”

I spoke out of nowhere, then carefully directed my question at the North Heaven Demon Lord.

Like a student raising his hand to ask a professor about a difficult assignment.

“Wouldn’t it have been a lot better just now if I kicked you in the balls instead of knocking your spear up?”

At that moment, the professor’s face contorted beyond description.
## Chapter artifact 974

# Chapter 974

Sometimes, no matter how you live, your true feelings just don’t reach the other person.

It was sad to cause a misunderstanding you’d never intended, but in a way, it couldn’t be helped.

It wasn’t the kind of relationship you could fix by talking in the first place.

“That mouth of yours…”

The words died before he could finish, leaving only a breath that scattered into the air.

The professor—or rather, the North Heaven Demon Lord—seemed dizzy with rage. His face twisted as he steadied his breathing.

I spoke first, taking the words right out of the mouth of a guy who looked like he was struggling.

“I’ll tear it open.”

“What?”

“That’s what you were going to say, right? I’ve heard it plenty of times. I know.”

The North Heaven Demon Lord stared at me, momentarily at a loss for words, then clenched his teeth.

“Shut up.”

“Come on. People should be able to say what they want. Even if they’re shameless pill-popping bastards.”

“I said shut up.”

“But I’ve heard that line so many times, it’s starting to feel a little stale. ‘I’ll tear your mouth open so you can never wag that unruly tongue again.’ Doesn’t that have a bit more flavor?”

“You’re truly impossible to deal with using words.”

“You won’t manage with force, either. The guys who said that to me and died could line up in a column, count off, and stretch twice around the Murim Alliance training ground.”

Jeok Cheongang, standing beside me, added, “For the record, mine would stretch more than ten times around.”

“That’s because you’ve lived a lot longer than me.”

“If you don’t like it, then live a long, healthy life yourself.”

“You lived a long, sickly life. Don’t you remember? When I first met you…”

*Fwoosh!*

A sharp whistle swallowed the words that were about to follow.

I ducked on instinct, without a moment’s hesitation. A dagger shot past overhead at the speed of a streak of light and slammed into the cliff face.

*KABOOM!*

It hit with the force of a cannonball.

But no matter how much power an attack carried, it didn’t matter if it missed.

I brushed off the grit that had jumped up with the shock wave and stared wide-eyed at the North Heaven Demon Lord, who had thrown the dagger.

“Wow. That almost hit me.”

“……!”

“Those pills really do make you strong. Old Master, I don’t think I could take him one-on-one by myself.”

Jeok Cheongang frowned. “Do you even need to ask? Of course you couldn’t. If you keep doing what you’ve been doing, you might have a chance in a year or two.”

Only a year or two.

Considering Jeok Cheongang knew my past and even my deepest secrets, that was a fairly reasonable assessment. But to someone listening, it was an intolerable insult.

“Jamukha.”

There was no anger left on the North Heaven Demon Lord’s face. At his low voice, the old nomad bowed his head.

“Give your command.”

“Do you remember the promise we made long ago?”

“I have never forgotten it for a single moment.”

“Then stake your life on it.”

“……!”

“If you survive, I’ll give you Hebei along with the vast grasslands. Everything the Peng Family possessed—even their lives—I’ll put in your hands.”

The old nomad, Jamukha, trembled.

“That is the very reason I have lived until now.”

“Then what will you give me?”

“Today’s victory. And the head of Jin Taekyung, the Blazing Flame Divine Dragon.”

“Yes. That is the answer I wanted.”

*Step. Shhhhh…*

As he took a heavy step, the dark crimson energy rising around him like heat haze gathered thickly, turning into mist.

The two men had finally drawn out every last drop of their strength. Watching them, Jeok Cheongang spoke calmly.

“Taekyung.”

“Yes?”

“Do you remember the promise we made long ago?”

I answered without hesitation. “No.”

“……”

“And what do you mean, ‘long ago’? It’s only been two years since we first met.”

Jeok Cheongang fell silent for a moment, then sighed.

“Do you have some kind of disease that makes blood gush from your seven apertures and kills you if you play along at a time like this?”

“What’s the point of playing along? We can’t even get our timing right. It’s much better to land one more hit on those bastards.”

“Hmm. Hard to argue with that.”

“Just do what you’ve always done. Be the Fire King.”

Jeok Cheongang’s gaze, fixed on the North Heaven Demon Lord and Jamukha as they approached slowly and cautiously, shifted to me.

“What? Is there something else you want to say?”

“No, nothing much. It just struck me that accepting you as my Disciple was the right choice.”

For a moment, I didn’t know what to say. Jeok Cheongang’s quiet voice reached my ear.

“We never made any embarrassing promises to each other, but keep one thing in mind, as always.”

“What should I keep in mind…?”

“This old man is always by your side.”

“……!”

“So don’t do anything stupid like risking your life in a fight. Even if Yama comes for you, this old man will kick him in the ass and send him packing.”

The more I learned, the stranger it seemed.

We were both human, made of flesh and blood, and yet our thoughts could be so completely different.

One person asked another to give up his life in return for everything he wanted. Another needed nothing at all—he only wanted the other person to survive.

And that was exactly what I wanted to say to Jeok Cheongang, too.

“If I keep that promise, what will you give me?”

Step by step, the two enemies drew closer. I watched the dark crimson mist grow thicker as I spoke, and Jeok Cheongang gave a dry laugh.

“You shameless bastard. Fine, what do you want?”

“Nothing much. You’ve already been sick once, so a long, healthy life is out of the question. At least make sure you live a long, sickly one from now on.”

“Living a long time at my age, huh? Seems I have a good reason to live at least another hundred years.”

Jeok Cheongang laughed heartily, clearly delighted.

Pale light-flames gathered in his outstretched hands. Alongside them, blue-white flames surged over the spearhead of White Flame, burning away the chill of the deep night.

*Fwoooosh.*

Beyond the darkness melting in the heat of two flames—alike, yet different—I stepped forward toward the ominously thick dark crimson mist.

No. We did, as if we’d made a promise to do so at the same time.

*Shwaa!*

* * *

Everyone who faced the mist—red as blood and frighteningly thick—felt a chill sink deep into their spines and stopped moving.

No. They had no choice but to stop.

Their instincts knew it before their reason could.

*If I get close, I’ll die.*

The sight alone was chilling.

That thick blanket of mist was energy made almost completely tangible. It was no different from a forest of blades and spears, ready to slice and tear anyone who entered to pieces.

But the biggest reason so many people from Shanxi were held back was the terrifying battle raging inside that dangerous space.

*KABOOM! KABOOOOM!*

Was there any phrase that could describe what was happening better than “heaven and earth overturned”?

Beyond the mist, writhing like a living creature, four Supreme Peak masters were entangled with one another at the speed of flashes of light.

Without a moment’s pause.

Even now.

*Shhk!*

Force sliced through the hard ground as if it were tofu.

Jeok Cheongang narrowly dodged the North Heaven Demon Lord’s strike and clenched his fist.

The wrinkles had vanished from his face with his regained youth. Pale light-flames surged over his knuckles.

*Fwoosh!*

Flame-Extinguishing Divine Fist.

A tremendous blaze, brought to the tenth level of mastery after more than a century of training, erupted.

It stained the air and shot toward the enemy before him—toward the North Heaven Demon Lord.

*KABOOOOOM!*

Compressed air exploded in layers.

But even amid the enormous impact, which melted the ground and shook the cliff walls, the North Heaven Demon Lord’s figure blurred in the final instant and disappeared.

Or, more accurately, it disappeared from the sight of a human with such obvious limits.

*Whoosh.*

A tiny, faint whistle slipped quietly into his ear.

But Jeok Cheongang knew well that movement beyond sound could fool even hearing.

*Above!*

He could feel it.

His opponent’s presence, descending from the invisible space above his head.

And, at the same time, the massive Force carried on the spearhead that thrust forward, erasing the wind in its wake.

*Poom!*

Jeok Cheongang struck out with both palms without hesitation.

The dark crimson mist that had wrapped around the area scattered in an instant.

The full force of Flame Divine Palm surged upward in a pillar of fire.

He aimed it at his opponent, who had tried to erase his presence as much as possible, but whose immense energy made it impossible to conceal him completely.

And in the next moment, Jeok Cheongang realized something anew.

The North Heaven Demon Lord, drawing on the power of the Temporary Strength Pill, was a great enemy who could look down on even him—who had reached his current realm through several breakthroughs in insight—as half a step beneath him.

*Shwaa!*

The spearhead pierced a single precise point.

The immense Force carried at its tip split the flames that seemed capable of burning the whole world. The distance between the two men vanished.

“……!”

Overwhelmed by that force, Jeok Cheongang’s eyes widened.

This wasn’t a question of martial enlightenment.

The North Heaven Demon Lord’s movements, enhanced to an extreme, made everything possible—along with internal energy so powerful it made Jeok Cheongang wonder if he had drawn out every last bit of his innate qi.

*Damn it.*

Jeok Cheongang swallowed the curse rising to his lips and pulled up every ounce of his internal energy.

He slammed both hands together against the spearhead plunging toward his chest.

*Krrrrk!*

The spearhead trembled between his palms, pressed together as if in prayer.

Dark crimson Force that his Body-Protecting Qi could not fully stop tore into his flesh and bones. Jeok Cheongang clenched his teeth to endure the pain.

*Crack.*

The pain of his molars breaking was nothing beside what he felt in his two hands, growing more mangled by the second.

As Jeok Cheongang swallowed the blood surging up his throat and held on to the spearhead, the North Heaven Demon Lord bared his teeth in a grin.

“Why not stop now and get some rest? You look exhausted.”

A mocking voice slipped between Jeok Cheongang’s clenched teeth.

“I’ll give you that advice right back.”

The North Heaven Demon Lord’s eyes sank.

He, too, could feel with his whole body that Jeok Cheongang’s words weren’t an empty boast.

*What kind of monster is this old man?*

*Crack. Krrrunch.*

The spearhead was clearly being driven forward with all his strength, yet it could go no farther.

Jeok Cheongang’s skin was crushed by the Force, but his toes were dug deep into the ground, perfectly still.

The old monster of Mount Jiuhua, returned decades younger, was far stronger than the North Heaven Demon Lord remembered.

Strong enough that even now, after taking the Temporary Strength Pill, he couldn’t knock him down easily.

*But…*

It ends here.

As that thought took shape, the North Heaven Demon Lord twisted the spear shaft.

With every ounce of strength he could bring to bear.

Enough to make even Jeok Cheongang unable to endure the pain this time.

*Crack.*

At the grisly sound of flesh splitting, Jeok Cheongang’s body trembled. Then a thunderous shout burst from between Jamukha’s lips.

“Jamukha!”

At that instant—

*KABOOM! Shhk!*

With a thunderous crash, a razor-sharp gust of wind shot toward Jeok Cheongang’s back.

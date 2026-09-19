# Checkpoint Review — 420–424

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

# Chapters 420–424

## Plot

Jin Taekyung confronts the Arch Lich, who reveals that it serves the great king Asmodeus and seeks to corrupt Jin as a powerful vessel. After Gravity repels White Flame, the Arch Lich attacks with curses, poison, Dark Hands, Dark Vines, Bone Spears, Sonic Buster, and other spells. Jin’s sixth sense and newly opened Middle Dantian let him perceive the true essence, centers, and mana flows of the Arch Lich’s magic. He breaks through its defenses with Heavenly Strike, White Flame, and Flame-Extinguishing Divine Fist, destroying Great Bone Wall and striking the Arch Lich.

The Arch Lich survives Jin’s attacks, though Jin pierces its chest with White Flame and destroys its left arm with One Annihilation. Jin is left severely injured, bleeding, exhausted, and unable to reach his lost top-grade potion. The Arch Lich begins opening an enormous Gate over the ruined city and threatens Jin’s allies and family. When the Arch Lich returns White Flame against Jin, the Skeleton Warlord manifests a body, takes up Lei Fei’s Hero’s Soul, and sacrifices itself to protect him. Bone Explosion then destroys the Warlord, leaving Hero’s Soul embedded in the ground.

## Continuity

- Jin’s Middle Dantian is open, granting improved qi control and allowing him to perceive and sever the centers and mana flows of spells.
- Jin’s earlier Curse and attribute reductions were removed by a level-up, but he now has Severe Injury, Excessive Bleeding, and Exhaustion. His Strength, Agility, and Stamina are sharply reduced.
- Jin’s Endurance transformed into Will, and temporary Indomitable slightly raised all attributes and reduced fatigue.
- The Arch Lich survived One Annihilation with its left arm destroyed and remains active, weakened, and still capable of powerful magic.
- White Flame remains lodged in the Arch Lich’s chest until it is removed and returned to Jin; the Arch Lich then launches it back at him.
- The Skeleton Warlord sacrificed itself to save Jin and was destroyed by Bone Explosion. Hero’s Soul remains embedded in the ground, with the Warlord’s hand still gripping its hilt. Whether the Warlord was irreversibly erased is unresolved.
- The Arch Lich is creating an enormous incomplete Gate over the ruined city. Its completion threatens Team Leader Choi, Xiao Shen, the Peace Guild, Jin’s family, and the surrounding area.
- The Arch Lich identifies Jin as a possible Adversary, the king’s eternal nemesis, but the connection and the alleged god’s machinations remain unconfirmed.
- The Arch Lich claims to serve Asmodeus; Asmodeus’s current status and location remain unknown.
- Choi Minwoo continues leading the allied forces against the monster army outside.
- The Quest **One Who Returned from Death** remains active, keeping Login unavailable until the Quest ends.

## Translation Decisions

- Render **중단전** as **Middle Dantian**, **단중혈** as **Tanzhong acupoint**, and **대적자** as **the Adversary**.
- Render **소닉 바스터** as **Sonic Buster**, **그레이트 본 월** as **Great Bone Wall**, **멸염신권** as **Flame-Extinguishing Divine Fist**, **블러드 익스플로젼** as **Blood Explosion**, and **본 익스플로젼** as **Bone Explosion**.
- Render **탈진** as **Exhaustion**, **의지** as **Will**, **불굴** as **Indomitable**, **영웅의 혼** as **Hero’s Soul**, and **소멸** as **Erasure**.
- Preserve the Arch Lich’s archaic, contemptuous register, the Skeleton Warlord’s gruff vulnerability, and Jin’s profanity.
- Retain established terms including **Asmodeus**, **Gravity**, **White Flame**, **Force**, **Scorching Yang Qi**, and **three jiazi**.

## Durable state

{
  "active_continuity": [
    "Jin's Middle Dantian is open, allowing him to perceive the center and grain of magic and sever spells.",
    "Jin has Severe Injury, Excessive Bleeding, and Exhaustion; his Strength, Stamina, and Agility are temporarily greatly reduced.",
    "Endurance transformed into Will, and Indomitable is temporarily active, slightly raising all attributes and reducing fatigue.",
    "The Arch Lich survived One Annihilation with its left arm destroyed and remains weakened but active.",
    "The Arch Lich used Blood Explosion, took White Flame, and launched the spear back at Jin.",
    "The Skeleton Warlord sacrificed itself to save Jin and was destroyed by Bone Explosion; Hero's Soul remains embedded in the ground with its hand.",
    "The Arch Lich continues creating the enormous incomplete Gate in the ruined city.",
    "The Gate threatens Team Leader Choi, Xiao Shen, the Peace Guild members, and Jin's family.",
    "The Arch Lich continues to regard Jin as a possible Adversary.",
    "The Quest One Who Returned from Death remains active, keeping Login unavailable until the Quest ends."
  ],
  "continuity_sources": [
    424,
    423
  ],
  "open_questions": [
    "Is the Skeleton Warlord irreversibly erased, and can Jin recover Hero's Soul?",
    "Can Jin survive his catastrophic injuries and Exhaustion well enough to continue fighting?",
    "Can Jin defeat the Arch Lich and recover White Flame?",
    "Can Jin stop or disrupt the enormous incomplete Gate before it becomes a catastrophe?",
    "What is Asmodeus's current status and location?"
  ],
  "safe_through": 424,
  "temporary_decisions": [
    "Render 탈진 as Exhaustion, 의지 as Will, and 불굴 as Indomitable.",
    "Render 블러드 익스플로젼 as Blood Explosion and 본 익스플로젼 as Bone Explosion.",
    "Render 영웅의 혼 as Hero's Soul and 소멸 as Erasure.",
    "Render 중단전 as Middle Dantian and 단중혈 as Tanzhong acupoint.",
    "Preserve the Arch Lich's archaic, contemptuous register and Jin's profanity while retaining established wuxia and System terminology."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 420

# Chapter 420

What did people feel when they first encountered a monster?

Surprise, terror, fear, confusion?

I had no idea. It happened before I was born—or, if you wanted to be technical, back when I was on my father’s side rather than inside my mother’s womb.

But those who had stood at the scene of that history must have thought of the countless legends and myths passed down from ancient times.

Just as I was now.

*Demon.*

That was the word that flashed through my mind the instant I saw it. A massive body reaching three meters tall. Bones covered in a black sheen. A shape resembling a human’s, yet fundamentally something else.

*Fwoooosh.*

Like the wings of a demon from mythology, the robe draped over its body fluttered like a living creature.

A demon that darkened the world simply by appearing—or rather, the Arch Lich’s red eyes cast an eerie light.

“Human.”

Just one word.

The air around me trembled. From inside my inventory, the Skeleton Warlord muttered like a groan.

“The lord of the undead…”

His voice was steeped in fear. The law of power applied to monsters, too.

Yes. Just as the Skeleton Warlord had said, the Arch Lich was likely the lord of every undead monster in existence.

“Human. It is not too late. Even now…”

Instead of answering, I gave a small nod.

The Skeleton Warlord was right. It was not too late, and I still had more than enough opportunity left.

*An opportunity to stop that bastard, that is.*

If this enormous metropolis transformed into a single Gate, there would truly be no turning back.

Countless undead monsters would spread like a plague, and the Arch Lich’s power would grow even stronger.

*Now or never.*

After taking a deep breath, I extended my hand. The shaft of White Flame, pulled toward me with Seizing an Object Through Empty Space, landed in my grasp.

I stepped over the piles of collapsed concrete and trudged outside. A ruined wasteland filled with nothing but thick fog awaited me.

Up and down. Left and right.

No matter where I looked, there was no sign of a monster.

Ah, scratch that. There was one.

“Nice to meet you, you fucking bastard.”

More than twenty meters above me, the Arch Lich stood on empty air and looked down. Its red eyes gleamed.

“So it’s true. You know the language of the Demon Realm. I did not mishear you.”

“I studied hard. But you know me, don’t you?”

“I am an entity with hundreds of eyes and ears. I have watched you all along, human.”

I frowned.

“All along?”

“Yes. Your performance on the battlefield was remarkable.”

*A Familiar spell.*

I muttered inwardly but did not let it show. Instead, I clicked my tongue.

“So you’re a hidden-camera creep. You didn’t install one in my bathroom, did you?”

“A hidden-camera creep? You speak nonsense, human.”

“True. If you’d seen me through a hidden camera in my bathroom, you would’ve vanished from shock already. No one has ever survived looking my enormous black anaconda in the eye.”

“Do you mean a Basilisk?”

A Basilisk was a monster from mythology that inflicted a petrification curse simply by making eye contact.

It was also a Named Monster that had appeared exactly once during the Great Cataclysm.

“Something like that.”

At least the part about being so startled that you froze was the same, right?

But the Arch Lich’s response to my answer was unexpected.

“So that is the reason. The reason you feel strangely familiar to me.”

“What?”

“Human. I sense the energy of death from you. A dense, dark energy like my own.”

“…”

I was secretly startled. I thought I knew what the Arch Lich meant by the energy of death.

There was someone who could not hide his agitation at every word the creature spoke.

*The Skeleton Warlord.*

No matter how powerful a Named Monster he was, the Skeleton Warlord was still undead.

Had the Arch Lich caught the scent that had seeped into my body from spending so much time with him? Or had it seen through even that other unknown space called an inventory?

If the latter was true…

*How far do that bastard’s abilities reach?*

I activated Qi Sense. Along with a System notification, a blue line shot up into the sky.

At the same time, the Arch Lich’s red eyes, flickering between its bones, curved like crescent moons.

“How interesting.”

In the next instant, black mana shot from the Arch Lich’s entire body and lashed against the blue line.

*Beep!*

> **System**
>
> - **???** protects itself with a powerful, incomprehensible force!
> - **Qi Sense** failed! Unable to determine the designated target!

I’d had a feeling, and sure enough.

The Arch Lich looked down at my stiffened face and let out a low laugh.

“What an interesting human. Truly. Perhaps… my guess is correct after all.”

“What guess? The guess that you’re about to die?”

“That will not happen. I am the lord of all undead. I am different from those weak and foolish humans.”

The Arch Lich raised a hand made of black, glossy bone and pointed toward Wu Heixing, whose breath had stopped, and Lee Jungryong, who had been reduced to black ash.

“It was a most entertaining sight. Watching you humans kill one another brought me immense joy for the first time in a very long while. I thank you for helping me understand how insignificant humans are.”

“Get lost.”

“Anger makes humans stronger. Is that true of you as well?”

*Fwoooosh.*

The fog filling every direction began to move like a living creature. As though someone were drawing in empty space, it formed a scene and shape.

A ruined city.

At the center of a horrific battlefield where rivers of blood flowed and corpses piled up like mountains, a man was rising with his sword as a cane.

I had seen his face only once, but I could not forget it.

The Arch Lich’s low voice echoed through the air.

“Lei Fei. That was certainly his name.”

“…”

“He possessed a great, radiant soul. He was so dazzling that I coveted him simply by watching from afar.”

With another small gesture, the fog shifted and painted a new scene.

Lei Fei staggering toward the Arch Lich.

Lei Fei dropping to his knees before he could reach it.

Lei Fei glaring at the sky with a face filled with rage and resentment as he breathed his last.

And then…

Lei Fei reborn as a corrupted being by the Arch Lich, kneeling before his new master.

No.

The Death Knight Lord.

*Fwoooosh.*

A wind blew from somewhere, scattering the fog. The Arch Lich continued slowly.

“Do you know? Humans with noble souls wield even greater power after they fall. He truly was the finest material… It was unfortunate, but he did not turn out so badly.”

I slowly nodded.

“Keep talking.”

“I have found new material. You, human—with an even stronger and more massive soul!”

The chilling voice thundered through the air.

Mana flowed from the Arch Lich’s entire body, covering the sky like dark storm clouds and staining the city in darkness.

At the center of it all, its red eyes burned like an ominous sun.

I stood silently and watched the scene. Then I suddenly opened my mouth.

“Yeah, so… are you done talking now?”

My stomach was burning.

The anger I had been storing up and suppressing until I met the Arch Lich was rising to the surface.

It surged like lava in a volcanic region.

“If you’ve said everything you wanted to say…”

Something snapped in my head.

The hours of battle I had endured while leading the suicide squad, along with the mental fatigue that had built up while fighting Lee Jungryong and Wu Heixing, vanished from my mind in that instant.

“Then get down here, you fucking bastard.”

If the Arch Lich’s voice had been thunder, my shout was lava.

A fire dragon raced along the hundreds of acupoints boiling like an active volcano. Blue flames covered White Flame’s transparent spearhead, radiating heat of unimaginable intensity.

And then—

*Shweeeeeek! Boom!*

The spear of flame I launched with all my strength blew apart the dark clouds of mana and tore through the darkness.

* * *

*Rumble-rumble-rumble! Fwoom!*

Along with a vibration that shook the earth, dazzling blue flames spread across the sky.

Several kilometers away, the humans and monsters locked in a fierce battle momentarily forgot even their own circumstances and stared blankly at the spectacle.

“Grrrrr…”

“What is that…?”

The light that burst from the enormous city shrouded in thick fog was warmer and more dazzling than anything else.

At least, that was how it seemed to one man standing tall and gazing at the city.

Choi Minwoo.

*Mr. Jin.*

There was no one else it could be.

Jin Taekyung was alive, and he was fighting the Arch Lich.

No. Perhaps he was fighting someone else, too.

*Lee Jungryong. Wu Heixing.*

Others might call his concern premature and his suspicions a false accusation, but Choi Minwoo knew how evil a person could become.

At least, that was what the Lee Jungryong he had known had been like.

And at the same time…

He knew Jin Taekyung well, too.

*You’re strong. Stronger than anyone I know.*

Choi Minwoo had said those words to Jin Taekyung once.

Some people might have laughed at him, but Choi Minwoo had been sincere.

He believed that no S-rank Hunter—not even Cheon Taemin, his maternal grandfather and the man who had defeated the Demon King Asmodeus—could be stronger than Jin Taekyung.

It was not a matter of skill. Nor was it even a question of whose aura was greater or stronger.

It was something possessed only by those who had experienced Jin Taekyung.

*Faith.*

Jin Taekyung had given Choi Minwoo faith.

Cheon Taemin, the hero who had saved humanity, had turned away from his young grandson after the boy lost his parents.

Jin Taekyung had not.

He had rejected the temptations around him that whispered of wealth and honor, remained with the Peace Guild, and protected his people no matter what danger they faced.

No matter who stood against him.

*“Our opponent is the Ares Guild. It’ll be a dangerous road.”*

*“I’m something of a specialist in thorny roads.”*

*“A road more dangerous than anything we’ve faced so far.”*

*“Team Leader.”*

*“Yes?”*

*“Sometimes it’s okay to be honest.”*

*“…”*

It was the first time.

No one had ever said anything like that to him before.

Butler Kim, who had always been by his side since childhood, was thoughtful and warm, but he had never given Choi Minwoo that certainty.

Jin Taekyung had, and that gave Choi Minwoo the courage to speak.

*“Will you… continue staying with the Peace Guild?”*

*“Yeah. That’s more like it.”*

Choi Minwoo could never forget Jin Taekyung’s crooked grin.

The day he gained people he could call *us*, rather than Guild members connected by a few sheets of paper called a contract.

*So this is what it was.*

He had always been alone.

Isolated and lonely.

From his earliest memories, he had been separated from everything around him.

The children he met as a boy were wary of him, and the adults whispered among themselves.

He had been hurt, but he never let it show. Only the aging Butler Kim had been someone he could truly confide in.

But not anymore.

Choi Minwoo suddenly smiled.

Far in the distance, he watched the flames rising through the thick fog and darkness, then gripped his sword once more.

*Shhk!*

A monster’s body split apart beneath a flash of dazzling aura.

As the brief silence and stillness that had settled over the battlefield shattered, a tremendous cry burst from Choi Minwoo’s lips.

“Attack—!”

Raising his sword and charging toward the monsters, he resembled someone Lee Jungryong had seen several decades ago.
## Chapter artifact 421

# Chapter 421

There was an old saying passed down among Hunters.

Mages came in two kinds: archmages, and everyone else.

Magic Johnson had proven that saying true with his own body.

Among the seven billion people on Earth, there were only three archmages.

And even among those three, he was the strongest War Mage. During the Great Cataclysm, he had slain countless monsters and led innumerable battles to victory.

But even Magic Johnson, despite all those incredible achievements, had encountered someone before whom he had been forced to swallow his pride.

*I hate to say this, but the Arch Lich’s magic is a level above mine. Be careful, Jin.*

The Arch Lich was that powerful. There could be no hesitation or carelessness—not even for an instant—when facing it.

—Human, hurry!

*I know, damn it.*

I let the Skeleton Warlord’s shriek wash in one ear and out the other as I poured internal energy into both legs.

*Crack-crack-crack!*

The solid concrete floor sank beneath me, unable to withstand the pressure transmitted into it. I bent my knees slightly, then kicked off with all my strength.

*Boom!*

With a thunderous roar like an explosion, I shot into the air like a streak of light.

The fierce wind swept across my entire body, and the Arch Lich’s form rapidly drew closer, its black robe spread like wings.

—You…

I could see them.

The creature’s trembling red eyes.

White Flame, launched with all my strength, had shattered the invisible barrier surrounding the Arch Lich and was now falling with everything it had.

*Come.*

I stretched out my hand. The shaft of White Flame, pulled across several meters with Seizing an Object Through Empty Space, landed in my grasp.

*Now!*

I thrust the spear forward with all my strength. Three jiazi of Scorching Yang Qi surged up from my dantian and raced onward without restraint. Blue Force, like hellfire, erupted over the transparent spearhead.

*Fwoooooom!*

And just as I became certain of my success—

—Gravity.

*Fwoosh!*

“Hngh!”

Along with that sinister voice, something invisible pressed down on my entire body.

No.

It struck me.

I swallowed a breath and reached out as far as I could, but before the spearhead brimming with Force could touch the Arch Lich’s foot, my body was already falling toward the ground.

The Arch Lich’s form, which had seemed close enough to touch, receded in an instant.

“You fucking—”

*Booooom!*

As I crashed down like a meteor, a laugh like scraping metal rang out above my head.

—Not bad. That was rather entertaining.

*Damn skeleton bastard.*

I spat thickly and looked up at the Arch Lich looming over me as though it were a god.

“Good to hear. It’s only going to get more entertaining from here.”

—Humans are always dreaming futile dreams. I have seen it countless times: you challenge what cannot be surpassed, driven by anger and longing, only to finally realize reality and fall into despair.

“That sounds a lot like the bullshit spewed by all the guys who’ve died by my hand… Do you people share a *Hundred Questions and Answers for Dealing with Jin Taekyung* or something? Do you hold study sessions every now and then, too?”

—Even so, those who died by your hand were still insignificant humans. But I am different.

“Of course you’re different, you son of a bitch. You’re already dead.”

—…!

The Arch Lich fell silent for a moment, so I continued.

“Looking at your current state, that means someone killed you, too. Was it a human? Why have you been showing off your inferiority complex this whole time?”

—You…

“Yep. This bastard was killed by a human.”

—Will you shut your mouth!

At the thunderous shout, the magic surrounding the Arch Lich surged violently. Its red eyes had grown far brighter than before as they glared down at me.

—I am a servant who follows a great king. I am not a being who can be compared to insignificant creatures like you!

I was about to fire back again when I froze at the unexpected word that came from its mouth.

*Wait. A king?*

*Did I hear that wrong?*

A question flashed through my mind, and the Skeleton Warlord answered in a trembling voice.

—The commander heard it clearly, too. Wretched human. Th-then, could it be…

*No way. It can’t be.*

I swallowed dryly and asked,

“Is the great king you just mentioned the Demon King Asmodeus?”

—Do not speak the name of His Highness.

Never say never, I guess.

And it turned out to be the Demon King Asmodeus after all.

The Skeleton Warlord sucked in a breath despite not needing to breathe, while I muttered in disbelief,

“Huh. Asmodeus? Seriously?”

—The name of His Highness…

“But I was sure Asmodeus had been destroyed.”

—The name of His Highness…

“Is Asmodeus still alive? As an Arch Demon King or something?”

—His Highness…

“Yeah, yeah, I get it—he’s fucking adorable. Now answer me. Asmodeus died back then, didn’t he? Or did he resurrect? If he came back as an undead like you, where is he and what’s he doing now?”

At that moment, the Skeleton Warlord murmured in a fearful voice,

—If it is this time of day, he might be sleeping…

“What the fuck are you talking about? You don’t sleep, either.”

—I do not, but His Highness might be different.

“What is the Demon King, some good little schoolboy? Do you think he turns off the television, brushes his teeth, and goes to bed when the sun goes down? And why are you using such an honorific?”

—Ah! I did not realize I was doing it… But is it not natural from the commander’s perspective?

*That’s true.*

—It is. Because I am a monster.

“Then don’t use it.”

—Why not…?

“The Demon King is far away, and my fist is close.”

—Ah.

The Skeleton Warlord let out an exclamation of realization, then added,

—But, human. It seems the Arch Lich’s magic will be getting closer in a moment.

*Damn it. He’s right.*

I hurriedly threw myself aside. A green mist grazed my body by a hair and covered the spot where I had been standing only a moment before.

*Ssssssssss!*

Stone, steel, and even concrete melted away, leaving a gaping hole in a space several dozen meters wide.

The Arch Lich had fired a poison cloud of terrifying power. Its eyes were not merely clear—they burned like torches.

—I intended to take you as one of my servants.

“Uh, what brought that on all of a sudden?”

—I would have subdued your soul and body and used you as the vanguard of my glorious undead army.

“How much does it pay?”

—But I have changed my mind.

“No, I asked how much it pays. Don’t tell me you people pay in passion, too?”

—Your flesh will be torn to pieces, and your soul will wander the River of Death for all eternity.

“Are you acquainted with the deacon at the church I went to as a kid? He said something similar to me. That a devil like me would go to hell. If my mom hadn’t stopped me, he would’ve become the first martyr in that church’s history.”

—You insignificant human. Pay the price for insulting His Highness and defiling his name.

“For once, we agree on something. Paying the price. I like that.”

I nodded and lowered White Flame at an angle.

“So I’m planning to make you pay the price, too… What do you think?”

The Arch Lich opened its mouth.

The four-syllable incantation, uttered in a voice deeper and more sinister than ever, was not an answer to my question.

It was a curse that called forth death.

—Dark Hand.

*Whoooom!*

A pair of black hands burst through the thick fog. They charged fiercely from both sides, as though coming together in prayer.

I leaped to avoid the Dark Hands—and another spell was waiting for me.

—Curse.

I twisted my body to evade the black fog descending like a net, but this time, I was too late.

No.

Perhaps the Arch Lich had anticipated my movement.

The fog had already been closing in before I finished dodging the Dark Hands.

*Shhk.*

The difference was no more than a single sheet of paper.

At the instant the sticky fog grazed the tip of my little finger—

*Beep!*

> **System**
>
> - You have been afflicted with the status effect **Curse**!
> - Due to **Curse**, all physical attributes have been temporarily reduced!
> - **Strength** has temporarily decreased by 20!
> - **Stamina** has temporarily decreased by 20!
> - **Agility**…

As soon as the System notification rang out, I felt my body grow heavier and clicked my tongue inwardly.

*Damn it.*

Even when I was short on points, I had been hit with a debuff from a curse.

Not one or two points, either. With twenty points stripped away at once from each attribute, I could definitely feel the difference.

But even with a debuff, I was not so helpless that I could do nothing but take his attacks.

Just like now.

—Dark Vine.

*Crack! Whoooosh!*

Hundreds of thorny vines burst through the ground and filled the air in every direction as they shot toward me.

I exhaled briefly and swung my spear. *Shhk.* A line of blue flame traced through the air, slicing apart every vine made of magic.

—Dark Vine. Dark Vine. Dark Vine.

*Shwoooooosh!*

From the severed ends of the thorny vines, which had been collapsing after losing their strength, new vines began to grow.

They sprouted, formed thorns, and grew even larger in barely a second.

But one second was the same as a minute to me.

*Fwoom! Shhk!*

A thorny vine measuring several meters around was cut apart in a single blow.

The dark plant, severed from its magical connection, toppled over and crashed into a half-collapsed high-rise building.

Through the cloud of dust rising with the thunderous impact, I sensed an ominous wave of energy.

*Magic.*

My prediction was right.

*Shhh-shhh-shhh-shhh!*

A spear stained a dull black.

A Bone Spear made entirely of bones became a streak of light and shot toward me.

No.

That wasn’t it.

*There isn’t just one.*

—Be careful, human!

Along with the Skeleton Warlord’s desperate shout—

*Boom!*

The dust cloud exploded with compressed air.

An uncountable number of Bone Spears surged toward me.

Some flew in straight lines. Some fell like meteors. Others traced curving paths through the air.

“Huh…”

—Ah.

The Skeleton Warlord and I groaned at the same time.

*How many are there? Hundreds? No, thousands?*

The overwhelming sight left me speechless for a moment.

A chill ran down my spine, and my mouth fell open on its own. A bead of cold sweat that had formed on my forehead slid down the bridge of my nose.

And then…

Everything stopped.

*This is…*

It was the very situation that sometimes came to me in times of crisis.

My five senses grew razor-sharp, and the world slowed down. In the space between those moments, something unfamiliar came creeping toward me.

A new sense.

A sixth sense that could not be explained scientifically.

I knew its name.

*The sixth sense.*

At the same time, something inside me shed its shell.

My eyes, sweeping over the enormous net formed by hundreds—thousands—of Bone Spears, gradually slowed.

*Because I had already given up everything?*

No.

What mattered was the essence.

A form could be layered over it, but the essence itself did not change.

And at this very moment, I was seeing the essence.

My lips, cracked completely dry, parted, and an exclamation escaped me.

“Ah.”

*So that was it. That’s what it was.*

It was something I still had not realized, even after reaching the Supreme Peak.

Along with a flash of insight that streaked through my mind like lightning, the slowed world returned to its proper speed.

Before the rain of spears pouring down and filling every direction, I raised my spear absentmindedly.

I brought White Flame down along the path I could see.

*Heavenly Strike.*

*Fwoooooom!*

The flames that erupted swallowed everything.

The Bone Spears, too numerous to count, vanished.

No.

The things that vanished the instant the flames touched them were illusions made of magic.

Only the essence collided with my strike, and unable to withstand its power, it burned away.

*Shhhhhhh.*

Ash scattered in the wind that blew from somewhere.

Amid the breeze, I heard a bright, cheerful ringing.

*Ding. Ding. Ding…*

It was such a pleasant sound that I found myself smiling without realizing it.
## Chapter artifact 422

# Chapter 422

*Ding. Ding. Ding.*

> **System**
>
> - There is always an opportunity in a crisis. You have gained a new insight in a battle where life and death hung in the balance!
>
> - **Middle Dantian** has been opened!
>
> - The opening of the **Middle Dantian** has increased all attributes by 20!
>
> - The effect of **circulating your qi** has greatly improved!
>
> - Your ability to perceive and control the flow of qi has greatly improved!
>
> - **Muscles and Bones** and **Sinews and Meridians** have increased!


The System notifications kept ringing in my ears without pause.

A breeze stirred my sweat-soaked hair, and I felt the new power and changes permeating my entire body.

Even the clear bell that rang at the very end.

*Ding.*

> **System**
>
> - As a reward for your enlightenment, you have gained a large amount of EXP!
>
> - As a reward for your enlightenment, you have gained 50 points!
>
> - Level Up!
>
> - As an effect of leveling up, all status ailments and fatigue have been cleared, and some injuries have healed!
>
> - The status effect **Curse** has been removed!
>
> - Your temporarily reduced attributes have returned to normal!

And I was not the only one who sensed these changes.

A master could not fail to know what his own hands had done. Realizing that his curse magic had been dispelled, the Arch Lich asked in a voice filled with disbelief,

“How in the world?”

I shrugged at the single word that encompassed every question it had.

“Well.”

“‘Well’?”

“Yeah. Well.”

“Do you think that explains anything?”

“Of course not. But why should I have to explain it to you?”

The emotion of sheer incredulity came across clearly in the Arch Lich’s faintly trembling eye-lights.

“You are clearly not a mage.”

“I wanted to be one. Their allowances are higher. But I had no talent. I wasn’t smart, either.”

“Even those humans you call archmages could not dispel my magic so easily.”

“They can’t. But it’s done.”

“What utter nonsense!”

I had to admit it.

The Arch Lich’s magic—no, its skill—was unquestionably superior to mine.

Even I, who had already far surpassed the limits of an ordinary Hunter, had been unable to avoid its curse magic. And the large-scale illusion magic using Bone Spears had been truly dangerous.

If I had not gained that insight, I might not even have been standing here now.

But…

“So what are you going to do about it?”

“……!”

I had the System, and I had merely done my best with the power and effort I had been given to overcome the crisis.

If it felt so unfair, it could use the System, too.

“That’s how the world works. Even if it feels like shit and pisses you off, you just have to put up with it and move on. What else can you do? It’s already happened. Right?”

The Skeleton Warlord, who had been screaming only moments ago, muttered,

“Wow. You sure know how to phrase things nicely.”

I could be like that sometimes.

“But, devious human, that one does not appear to have any intention of simply putting up with it and moving on.”

The Skeleton Warlord was right.

The next moment, an enormous vortex of mana formed, and an eerie voice rang out.

“Explode. Sonic Buster.”

And at the same time—

*Fwoooooosh! Boom!*

Highly compressed wind burst outward all at once.

Just brushing against the sphere of wind fired at the speed of sound was enough to pulverize concrete and snap steel reinforcing bars.

The windows of the high-rise buildings, unable to withstand the aftershock, shattered one after another, and countless shards of glass were swept up in the wind.

In a single instant—before I could even blink—the enormous mass of wind had reached the tip of my nose.

“Human!”

The Skeleton Warlord’s scream, hurled from inside my inventory, echoed like a cry from far away.

Was that bastard worried about its own safety, or mine?

It didn’t matter. Whatever the real reason was, it made no difference.

There was a world of difference between me a few minutes ago and me now.

*Ah.*

The area around my chest grew hot.

The spot martial artists called the Tanzhong acupoint, or the Middle Dantian, had opened wide.

It allowed me to take in everything surrounding me, feel it against my skin, and see it with my eyes.

*So that’s what it was.*

The world slowed down, and everything became clear enough to see and understand.

The enormous sphere made of wind whipping like blades.

And the flow of mana that made it possible.

*Shh-shh-shh-shh-shhk!*

Everything had a center. Magic was no exception.

And now, I could see that center.

*Now.*

I swung my spear through the slowed world.

The sphere of wind that looked as though it could sweep away everything in its path split in two along the blade of White Flame.

The wind blades that had split from one enormous whole into hundreds and thousands broke free of the mana controlling them, scattering left and right and tearing through everything around them.

*Shhk! Kwa-gwa-gwa-gwa!*

The raging wind whipped my clothes and hair around. With a faint smile on my lips, I looked up at the Arch Lich.

“Come down. My neck hurts.”

“You…!”

“Or I can come to you.”

*Crack-crackle! Boom!*

A single stomp.

The solid ground caved in, and I shot upward toward the ash-gray sky.

* * *
The instant Jin Taekyung shot up from the ground, the Arch Lich realized what it had to do.

*I must not let that human approach.*

Avoiding close combat was something every mage knew, but the meaning of it was different for the Arch Lich.

*This body is feeling threatened by a mere human.*

It prided itself on having already reached the pinnacle of dark magic.

Although it had lost a considerable amount of power during the process of being resurrected as an Arch Lich, even now it possessed enough mana to regard archmages as beings a level beneath it.

But the human flying toward it now…

*He is dangerous.*

*Yes, just like that bastard back then.*

It was a memory the Arch Lich never wanted to recall again. Clenching its still-intact teeth, it cast a spell.

“Gravity!”

Unlike before, the shout carried power. Invisible gravity pressed down over a radius of several dozen meters.

At the moment that pressure, impossible even for an S-rank Hunter to resist, was about to cover Jin Taekyung’s entire body—

*Pop!*

Compressed air burst from the tip of Jin Taekyung’s foot.

His body escaped the range of the gravity magic with *Stepping on Empty Air*, then stepped on the empty air again.

The nimble movements he displayed resembled those of a hawk, but his speed was beyond comparison with any mere flying creature.

*What is this?*

At the sight of Jin Taekyung racing through the air toward it, the Arch Lich’s eye-lights sank.

Jin Taekyung had not only precisely grasped the range of the gravity magic—he had even evaded it with some strange technique.

*As I thought. He did not dispel the illusion magic through mere luck. Then…*

*Whoooooooom!*

Mana flowed from the Arch Lich’s entire body and shook the surrounding space.

“Gravity. Gravity. Gravity.”

A high-level spell that even a fairly advanced mage would need to chant for quite some time poured out without pause.

The Arch Lich was certain that this time, it could knock Jin Taekyung down.

*You, human. Fall.*

This time, it reduced the power of its gravity magic in exchange for expanding its range.

How could Jin Taekyung possibly evade gravity pressing down over a radius of several hundred meters—

*Shhk!*

The Arch Lich’s eye-lights trembled.

At the same time, the gravity magic pressing down on Jin Taekyung scattered, and the mana connected to the Arch Lich was severed like a thread.

The Arch Lich froze for an instant at the fact that its magic had been dispelled.

Then Jin Taekyung stepped on the empty air once more and shot toward it like a cannon shell.

*Bang! Whoooosh!*

With a sharp crack through the air, Jin Taekyung flew before the Arch Lich—no, a step above it—and swung White Flame downward.

*Fwoom!*

A line of blue flame shot toward the Arch Lich.

*Crash!*

In the slowed world, the invisible barrier surrounding the Arch Lich shattered into pieces.

The flames of Force, fueled by three jiazi[^1] of Scorching Yang Qi, smashed through dozens of layered defensive spells and advanced toward the Arch Lich’s body.

[^1]: A jiazi is a traditional sixty-year cycle.

At that very moment—

“Great Bone Wall!”

With an eerie cry, a wall made of black bones rose from the air.

The highest-level defensive spell, manifested barely a meter away, collided with the flame-wreathed spearhead.

High above the ash-gray sky, an enormous shock wave and thunderous roar erupted around the two people facing each other with the bone wall between them.

*Kwaaang!*

Compressed wind burst outward.

The clouds circling far above scattered. Buildings that had barely maintained their shape collapsed, and half-rotted corpses were swept away by the wind.

Yet the two beings responsible for all those phenomena looked at each other beyond the barrier without so much as a tremor.

“That was close, wasn’t it?”

“Yes, quite impressive. No…”

The Arch Lich continued speaking as it stared at the transparent spearhead that had pierced through the center of the wall.

“I shall call it dangerous.”

The length of the spearhead that had passed through the bone barrier was no more than the width of a finger joint, but the Force that erupted in that instant had reached the tip of the Arch Lich’s nose.

For the Arch Lich, it had been a fortunate escape.

For Jin Taekyung, it had been unfortunate.

“You got lucky.”

“You are arrogant, human. But I will admit this much.”

“What?”

The Arch Lich slowly continued speaking toward the bewildered Jin Taekyung.

“You have earned the right to be so arrogant. If you truly are the Adversary.”

“……The Adversary?”

“That is right. The king’s Adversary. An eternal nemesis bound to him by a god’s machinations. I cannot be certain yet, but… that must also be why I was able to rise again after stepping into the River of Death.”

Jin Taekyung frowned.

What was the king’s Adversary? And what kind of nonsense was this about a god’s machinations?

“Are you suffering from middle-school syndrome? Get rid of those bones and show me your right hand. I want to see if you have a Black Flame Dragon.”

The Arch Lich shook its head.

“This is something that neither you nor I can understand. But one thing is certain.”

The deeply sunken red eye-lights flared fiercely.

At first, it had thought Jin Taekyung was merely a strong and unusual human.

But not anymore.

It recalled the memory of sweeping across this planet while serving the king decades ago.

It also recalled the figure of the human it had encountered on the day it lost everything and fell into the River of Death—the first and last time it had ever met that human.

*The Adversary.*

The human who had killed it and even assassinated the king.

The one it had tried to stop but could not, the one it had tried to approach but could not reach—the only human it had ever feared.

And today, in its battle with Jin Taekyung, the Arch Lich had remembered that day.

“You… will definitely die here.”

The eerie voice that rang out was more resolute than ever.

Jin Taekyung’s answer was simple.

“What the hell are you talking about, dumbass?”

And the next moment—

“Eat this, fucker.”

*Fwoom! Kwaaaaaa!*

Along with his low voice, a fist carrying blue hellfire shot forward, erasing everything that stood in its way.

It struck the curtain of black bones.

Flame-Extinguishing Divine Fist.

*Crack-crack-crack!*

The bone barrier that looked as though it could block any attack collapsed.

Beyond the countless fragments of bone scattering in every direction, the face of the Arch Lich came into view.

Jin Taekyung spoke with an expressionless face.

“See? Isn’t this much better? My neck doesn’t hurt, either.”

“……!”

“Down you go.”

*Wham!*

A single punch, fired like a ray of light, smashed into the Arch Lich’s jaw.
## Chapter artifact 423

# Chapter 423

*Wham!*

At the very moment the Arch Lich was knocked back toward the ground by the heavy impact, I gathered my internal energy and kicked off the air.

*Bang!*

With the sound of compressed air bursting, I shot toward the Arch Lich’s rapidly falling body at terrifying speed.

The Skeleton Warlord let out a cry that could have been either a scream or a cheer.

—You did it, human! Finish it quickly!

*Finish what?*

Unfortunately, its judgment was wrong. At least, I knew that much from having driven my fist directly into the Arch Lich’s jaw.

*It cast a defensive spell in that split second…!*

Before my all-out Flame-Extinguishing Divine Fist could make contact, it had overlaid its face with Bone Shield to protect itself.

Given the power of the blow, it could not have escaped completely unharmed—but it was not an opponent who would fall from something like that.

And my prediction proved correct. The Arch Lich’s body, which had been plummeting like a meteor, came to an abrupt stop, and immense mana rippled through the air.

—Darkness Hold.

*Fwoooooosh!*

A pair of enormous hands burst out of thin air. At a glance, they looked similar to Dark Hand, but as its name implied, Darkness Hold was a spell designed solely to bind its target.

I slashed my spear down toward the two hands hurtling toward me.

*I can see it.*

Everything had a grain—a pattern running through it. Living creatures had one. So did the wind, and even invisible energy.

After opening my Middle Dantian, I had gained the ability to sense and see the center and grain of things.

Just like now.

*Shhk!*

Flames blossomed, and the darkness split apart. As the black hands writhed as if in pain before dispersing into mist, the Arch Lich’s eye-lights flashed.

The next moment, its hand—formed from dark, weathered bones—clawed through the air.

—Dark Claw!

*Fsssssh, shhk!*

The black mist that had been dispersing transformed into the claws of a beast and poured down.

Countless attacks rushed in from every direction, each following a different trajectory. If I made up my mind to stop them, it would not be difficult.

But if I did that, I would lose the Arch Lich after only just managing to close the distance.

*I have to choose.*

I could not catch two rabbits at once. Especially when my opponent was not a rabbit, but a tiger.

After making my decision in that brief instant, I sent White Flame flying with all my strength.

Not toward the magic surrounding me, but toward the Arch Lich.

*Fwoooooom!*

White Flame, blazing with blue hellfire, shot forward like a flash of light, cleaving through everything in its path.

The Arch Lich’s voice burst out, more urgent than ever.

—Bone Shi—

Too late, you son of a bitch.

*Fwoooooosh!*

Blue hellfire swallowed the Arch Lich’s body.

The bone shield, not even fully formed, turned to ash and crumbled before the ultrahigh heat.

*Crunch!*

The spearhead of White Flame pierced through the Arch Lich’s chest. Impaled like meat on a skewer, the falling Arch Lich let out a scream unlike anything I had ever heard from it.

And at that moment, I felt a chill wind slicing in from every direction.

—Human, danger…!

I already knew. I did not need the Skeleton Warlord to shout a warning.

I knew, and I did it anyway. To take the bones, I had to give up flesh. Even knowing that I would not emerge unscathed, I believed this was the right decision.

As I watched the claws of mana raining down from all directions, I thought to myself,

*…Maybe I should have just blocked them.*

But there was no taking it back now.

*Shh-shh-shh-shh-shhk!*

A single gust of wind swept over my entire body.

It was not an illusion like Bone Spear, nor was it slow enough to block. I twisted my body as much as possible and gathered my internal energy, but there was a definite limit.

*Shhk! Shhk! Shhk! Fwoooooosh!*

My shoulder, side, thigh, arm…

Countless claws of mana slashed and raked across my body. Blood burst from my deeply split skin, and overwhelming pain surged through me.

*Damn it.*

It hurt. Enough to kill me.

Enough to make me want to die.

No matter how many times I experienced it, pain was something that was difficult to grow accustomed to.

My vision blurred, and the strength left my body before I even realized it.

It was a brief moment of pain, but it felt eternal.

When I opened my eyes after passing through it all, the first thing I saw was an enormous pile of concrete that had somehow rushed right up to my face.

—Get a hold of yourself, human!

“……!”

The Skeleton Warlord’s frantic shout snapped me back to my senses.

I forced internal energy into my stiffened body. Along with the tearing pain in my acupoints, the senses that had fallen asleep awakened.

*Now!*

Without the slightest hesitation, I flipped my body around.

*Crash!*

A thunderous roar rose with a cloud of dust. Violent vibrations and pain slowly crawled up the leg with which I landed roughly on the concrete pile.

“Urgh.”

I clenched my teeth against the pain, and the Skeleton Warlord spoke to me.

—Human, you do not… appear to be all right.

I answered while breathing harshly.

“Huff. If you know that, huff, then shut up. My head’s ringing.”

It was not just something I was saying. It really was.

The System notifications drilling into my ears alone were enough to make me feel like throwing up.

*Beep.*

> **System**
>
> - The status effect **Severe Injury** has been applied!
>
> - The status effect **Excessive Bleeding** has been applied!
>
> - Due to severe injuries, your physical attributes have been drastically reduced!
>
> - **Strength**, **Agility**, and **Stamina** have each decreased by 200 points!
>
> - You have suffered severe injuries! Immediate treatment is required!

Yeah. I thought so, too.

Whether it was because I had lost too much blood or because the excruciating pain kept coming, my vision was hazy and my thoughts were barely functioning.

But even in that state, there was someone whose existence I could not forget.

“The Arch Lich. Where is the Arch Lich?”

At the sound of my cracked voice, the Skeleton Warlord roared.

—Have you gone completely insane, human?! Treat yourself first!

“I haven’t gotten a kill notification yet. That means it’s still ali—”

—Who cares about a kill notification or whatever! Treat yourself first!

“Hngh.”

I said, don’t shout.

With my head spinning, I leaned against the concrete pile. Blood dripped from my entire body, which was soaked from head to toe, while my arms and legs trembled like aspen leaves beyond my control.

*Damn it.*

I had really taken a beating.

The one small consolation was that the Arch Lich had to be in even worse shape than I was—or at least no better.

—You stupid human!

*I know. I know.*

As I listened to the shout reverberating through my head, I slowly opened my palm. Then I muttered inwardly.

*Inventory open. Summon.*

*Pop!*

Everything happened at the same time as the thought.

The subspace pocket originally owned by Lee Jungryong—now belonging to me—yielded one item.

*Top-grade potion.*

Had Lee Jungryong ever imagined it? That both of the top-grade potions he had brought along just in case would be used for my sake.

With a finely trembling hand, I uncorked the top-grade potion. Then I drank it down in one gulp, like the elixir of life.

Or rather, I was just about to drink it.

*Tap—fwoooooosh!*

“……Huh?”

It all happened in an instant.

A black thorny vine shot up from between the concrete piles and lashed my wrist. In the slowed world, the top-grade potion went flying and disappeared beyond the pale haze.

I stared blankly at the few drops of potion scattered through the air as they soaked into the ground. Then I suddenly spoke.

“Dark Vine.”

Someone’s all-too-familiar magic.

The Skeleton Warlord muttered like it was groaning.

—It is him.

I slowly raised my head. Beyond the thick fog, a pair of red eye-lights like torches was drawing closer.

A three-meter-tall body with a black sheen. It resembled a human, but it was something that could not be called human. It emerged through the fog with heavy footsteps.

—You, human.

Its low voice carried unmistakable fury.

Deep inside my inventory, the Skeleton Warlord trembled. I smiled faintly.

“You son of a bitch. You stole the food right out of my mouth.”

—Your futile struggle ends here.

*Shhk! Pop!*

I did not even have time to reach out. The moment the Arch Lich snapped its fingers, Lee Jungryong’s subspace pocket, which looked like an ordinary leather pouch, was swept up by Dark Vine and flung far out of sight.

—No more cheap tricks will work.

With every word the Arch Lich spoke, the mana surrounding it reacted.

But just as I had suffered a severe injury, the power it emitted was also weaker than before.

The White Flame piercing the center of its chest had to be the decisive cause.

*I can do this.*

I forced myself to stand. As I reached out, a spear summoned from my inventory landed in my hand.

“The spear sticking out of your chest looks nice. Want me to plant another one?”

—Will you have the opportunity to do so?

“Of course. Looking at the state you’re in, I think it’ll be more than possible.”

—Humans never know the difference between courage and recklessness. How foolish. Truly, how foolish.

The Arch Lich laughed aloud and spread both arms.

The robe that had been reduced to ash by the earlier attack was gone. In its place, pitch-black mana flowed from the Arch Lich’s entire body and took shape.

*That’s…*

A vortex of mana that felt ominous merely to look at.

I instinctively realized what the Arch Lich was about to do.

*Gate.*

It was unstable, as though it might explode at any moment, but it had unmistakably taken the shape of a Gate.

And the Arch Lich’s next words transformed my guess into certainty.

—It is not yet complete, but… if I can merely bring you down, I should be able to complete everything.

At the same time, a low voice that seemed to come from the heavens reverberated through the space.

—Descend upon this place. Gate Open.

“……!”

I had to stop it somehow. But the pain slowed my body, and the transformation had already begun.

I stared wide-eyed at the sight that unfolded the next moment.

*Kwaaaaaaaaaaang!*

The few rays of sunlight faintly shining through the ash-gray sky disappeared completely.

With a thunderous roar, the sky split open. A storm swept across everything, and in the empty space left behind, a thick darkness rose like an ancient giant standing up.

*Fwoooooosh!*

The rippling darkness surged up from the center of the ruined city.

As tall as a high-rise building and wider than a soccer stadium, it was larger than any Gate I had ever seen. It inspired a fear that seeped deep into my bones.

—Ah… ahh.

Even the Skeleton Warlord, an undead monster, trembled at the sight.

I stood there with my mouth hanging open, staring blankly at the Gate. Then I suddenly realized something I had forgotten.

*I have to stop it. No matter what.*

Even if it was not yet a complete Gate, if things continued like this, an uncontrollable disaster would begin.

Millions, perhaps tens of millions, could die.

And among them…

Some might be my people.

Team Leader Choi, who was on the battlefield, and Xiao Shen, whom I had grown attached to despite our short time together.

If the Arch Lich crossed from China to the Korean Peninsula… the members of the Peace Guild and even my beloved family would be in danger.

*I have to go.*

My will moved the body that had been paralyzed by pain and shock.

I gathered my internal energy with every last ounce of strength I had. The acupoints suffering from internal injuries cried out in pain, and blood burst once more from various places across my body.

But I did not stop.

For one opportunity. Just one.

*Flamefire Path.*

My battered leg pushed against the ground. Along with shattering pain, a path of flames opened.

At its end stood one being.

The being that had started all of this.

The being that could end it all at the same time.

*Die.*

*One Annihilation.*

In the slowed world, I drew back my spear as far as I could and thrust it forward.

The vortex I sent flying with all my strength reached the Arch Lich.

*Kwaaaaaaaaaaang!*

And amid the blue flames filling the world, a single laughter-laced word from the Arch Lich pierced my ears.

—Blink.
## Chapter artifact 424

# Chapter 424

*Kwaaaaaaaaaaang!*

The vortex carrying blue flames devoured everything that stood in its way.

Buildings with their concrete walls collapsed and skeletal steel frames exposed. The corpses of humans and monsters scattered and mixed together throughout the ruins.

The ultrahigh heat burned and melted countless things.

Everything except one.

—Blink.

Everything except him.

*Beep.*

> **System**
>
> - Skill **One Annihilation** has been used!
>
> - All **internal energy** has been consumed!
>
> - Everything comes at a price. Despite your severe injuries, you have expended an excessive amount of power.
>
> - The status effect **Exhaustion** has been applied!
>
> - **Strength**, **Stamina**, and **Agility** have temporarily decreased drastically!

I felt the strength drain from my entire body. I could barely hear the System notification drilling into my ears—or the Skeleton Warlord’s shouts from inside my inventory.

My body was as heavy as waterlogged cotton, and only one thought kept circling through my mind, which had gone cold and numb.

*That was my last chance.*

Why? Why hadn’t I known? Why hadn’t I guessed?

The Arch Lich had clearly said that it had watched me through Familiars planted throughout the battlefield.

If so, I should have taken into account the fact that I had used One Annihilation against the Liches and Death Knights on my way here.

I should have suspected it, even if I couldn’t be certain.

*Idiot.*

A self-deprecating laugh escaped me. I had sworn I would never let my guard down again… and in the most important moment of all, I had made the biggest mistake.

The fact that I had no choice was no excuse. A fight was not about the process but the result.

And this was the result of letting my guard down.

*Clang!*

The iron spear slipped between my fingers and rolled across the ground. My legs, drained of strength, slowly gave way.

As I knelt and lowered my head, a deep darkness fell over me.

—You, human. How does it feel to pay the price for your rash arrogance?

I barely lifted my head and met a pair of burning red eye-lights. A voice squeezed through my cracked lips.

“Of course it feels like shit, you fucking bastard.”

—It was a fearsome strike. I shall at least commend you for that.

The Arch Lich’s voice was steeped in triumph.

It seemed that even its teleportation magic had not allowed it to evade One Annihilation completely. Its left arm had vanished.

But in the end, it was the one standing here as the victor.

The red eye-lights looking down at me, kneeling like a criminal, glimmered with joy.

—I waited until the very end. I held back and endured even the humiliation of suffering at a human’s hands. And finally… victory belongs to me.

Smart. Cunning.

Just as I had expected, it had been waiting for One Annihilation from the beginning.

Earlier, I had swept away the Liches and Death Knights with One Annihilation and recovered my stamina by leveling up. But the Arch Lich had not missed the fact that I had momentarily exhausted all my strength.

—Do you understand now? This is your limit. The limit of humanity.

Limit.

That one word pierced deep into my chest.

The limit called F-rank, which I had been unable to escape no matter how hard I worked. The very limit I had continued to break through day after day after obtaining the System.

*Is this really as far as I go?*

I had worked until I nearly died. For myself, and for the people I loved. No matter what danger came at me, I had gritted my teeth and fought my way through it.

That was how I had lived.

All of it had been a process of breaking through my limits.

“It’s not… over yet.”

A strange voice escaped between my lips, unfamiliar enough to sound as if it belonged to someone else, with not even a trace of life in it.

I looked up at the Arch Lich through my hazy eyes.

—What?

“It’s not over yet.”

A life-and-death duel ended only when one of the two fell.

So this fight was not over yet.

When one of us finally died, the one left standing at the end would be the victor.

I mumbled in my dazed state.

*Inventory open. Summon.*

At the same time as the command, one of the spears in my inventory appeared in my hand.

No—I thought I had caught it, but I dropped it immediately.

*Clang!*

I realized it again.

I no longer had the strength to hold a spear, let alone the energy to swing one.

—Kehat! Kahahahah!

The Arch Lich burst into mad laughter at the sight of me.

But I did not give up.

I couldn’t.

*Inventory open. Summon.*

I continued summoning weapons.

*Clang!*

Even when I continued dropping them.

*Inventory open. Summon.*

*Clang!*

—Human. You foolish, stupid human!

Even if the Arch Lich mocked me.

I did not stop.

The courage to humbly accept death? If that was what people called courage, I would rather be a coward.

I would… survive, no matter what.

I believed that was the final courtesy owed to the life I had struggled through until now—and the right answer.

*Inventory open. Summon.*

It happened at that very moment.

*Ding.*

> **System**
>
> - **Endurance** has increased drastically.
>
> - The attribute **Endurance** has changed into **Will**!
>
> - Those with strong wills are not easily broken, and they do not fall. They will burn their will until the very end and fight with every ounce of their strength.
>
> - A strong will can sometimes produce the power to transcend one’s limits!
>
> - The special effect **Indomitable** has manifested. All attributes temporarily increase slightly, and fatigue is reduced!

I felt warmth spread from deep within my body.

Compared to the power I had possessed originally, it was infinitesimal. And yet, in another sense, it was warmer than anything else.

It was the System’s response to my desperate plea.

My final chance.

With my hand still trembling faintly, I gripped the cold shaft of a spear.

—You…

I was not the only one who noticed the change.

The Arch Lich had been watching me like a monkey at the zoo, but its eye-lights opened wide. At that moment, I gathered every bit of strength I had and threw myself forward.

In a world that had slowed to a crawl, I extended the spear in my hand toward the Arch Lich standing tall before me.

*Fwoooooosh!*

And at the instant the spearhead cut through the air with a piercing roar, I saw it clearly.

The Arch Lich’s eye-lights curved like crescent moons.

It was mocking me.

—Blood Explosion.

*Boom!*

An explosion.

Then a shock wave swept over my entire body.

The body I had launched forward with every ounce of my strength suddenly locked up, and the spear slipped from my grasp and stabbed diagonally into the ground.

I blinked with both eyes, their tiny blood vessels burst. In a world dyed entirely red, something sticky and wet fell from the air and touched my face.

*Drip. Drip-drip-drip.*

*…Ah.*

Blood.

The blood gushing from my entire body like fountains was pouring down to the ground like a rain shower.

I lifted my arm, trembling like an aspen leaf, and saw ragged flesh and stark-white bone exposed beneath it.

Blood Explosion.

An explosion of blood.

Beyond my fading consciousness, I heard the Skeleton Warlord’s cry.

—…Human!

How long had it been shouting?

I wanted to answer, but what flowed between my lips was not an answer. It was blood mixed with bits of my organs.

“Cough.”

My vision spun.

I reached toward the Arch Lich, barely visible through the blood covering my face, but I could neither touch it nor reach it.

Perhaps I never would.

—Get a hold of yourself! You have to live!

Like that needed saying.

Of course I did.

I had to survive, defeat the Arch Lich, and return to the place where I belonged.

But…

*Could I really do that?*

At that moment, the world slowly began to tilt.

No. The world was still, and I was the one tilting.

My body, unable to withstand the continuing bleeding and injuries, was collapsing with all the strength it had left.

*No. If I fall, everything is over.*

I supported myself with the ankle that was already broken.

The faint pain, like a thorn prick, was proof that I was dying. The Skeleton Warlord’s shouts, coming intermittently through the static like a radio with a bad signal, were proof that I was still alive.

—…do it, human! Hurry!

Do what? What?

—Summon me right n—!

My eardrums had already burst, and my fading consciousness could not properly process the Skeleton Warlord’s voice.

Even if I had heard its words clearly, I would not have been able to stop what the Arch Lich did next.

—You possess an interesting item.

At some point, a familiar object had appeared in the Arch Lich’s hand.

White Flame, the treasured spear that had fought alongside me through countless battles, caused flames to flare up in the grasp of a stranger.

But even as its finger bones burned, the Arch Lich merely laughed.

—I have received an extravagant gift. I should return it to its owner now.

The Arch Lich drew its arm back. Powerful mana that had subdued White Flame’s flames surged toward the spearhead.

—Farewell, new Adversary—or perhaps merely a foolish human who might have been the Adversary.

*Fwoosh!*

The sound of the spear cutting through the air was brief, but the moment stretched into eternity.

I silently watched White Flame shoot toward me like a flash of light. Countless possibilities flashed through my mind, and at last, I reached a conclusion.

*I can’t avoid it.*

Then there was only one ending left to me.

Death.

I had fought countless battles from seven years ago until now, but death had never felt as close as it did at this moment.

All I could do was watch it approach.

*Yes. It’s over.*

At the very moment I calmly repeated those words to myself—

*Crack!*

White Flame’s spearhead shattered bone as it punched through a chest, and I froze with my eyes wide open.

Not because of the pain.

Because of the shock.

“You…”

—What?

I could not find the words. I stared at the blue eye-lights flickering right in front of me.

From a skull barely the size of a soccer ball, the Skeleton Warlord had transformed into a two-meter-tall body. In a gruff voice, it said,

—Do not ask how I managed to come out on my own. This commander has no idea, either.

“Then why? Why did you…”

I looked at it as I asked.

The spearhead that had pierced through the Skeleton Warlord’s back and chest had stopped exactly a handspan away from me.

If someone had not blocked it, that distance would certainly have been enough to kill me.

It had just thrown itself in front of me and saved my life.

—…I don’t know that either. Damn it. I don’t know anything anymore. Maybe this sword bewitched me.

Only then did I recognize the sword in the Skeleton Warlord’s hand.

“Hero’s Soul.”

Lei Fei’s only remaining keepsake.

A sword that could not even be held by someone who lacked the qualifications to become a hero.

That very Hero’s Soul was now in the Skeleton Warlord’s hand.

In the hand of a named monster that was not even human.

—Hero’s Soul. That is a decent name for something named by humans. No, to be honest, it is cool. It is a shame I was too late to swing it properly…

The Skeleton Warlord’s voice faded.

The light was slowly disappearing from its blue eye-lights, which had always shone so clearly.

I knew what this situation meant.

*Erasure.*

There was no doubt.

Even now, the Arch Lich’s mana carried on the spearhead of White Flame was rapidly eating away at the Skeleton Warlord.

“You…”

—Do not say anything more. I already regret this as it is.

I did not believe it.

Because I heard a low laugh that did not match its gruff tone.

—Human. There is something I wish to ask.

The Arch Lich was approaching over the Skeleton Warlord’s slowly crumbling shoulder, but I silently nodded.

“Anything.”

The Skeleton Warlord hesitated for a moment before asking in a small voice,

—What you said last time. Were you serious?

“If you mean last time, what are you—ah.”

I suddenly remembered.

It had been right after Lei Fei’s death, when the Skeleton Warlord had been thinking about its forgotten past.

And the words I had casually offered it then.



*“Well, I think he was probably a pretty decent guy.”*

*“…Huh? Were you saying that to this commander?”*

*“No. Just talking to myself.”*

*“Ahem. Right?”*



That was why.

That was what it had been about.

For the Skeleton Warlord, which had awakened from a spirit that had lost all its memories and gained strength, I might have been its only friend—the one who had always been by its side.

A single word I had tossed out like a small stone had sent ripples across the pond that held its heart.

*What an idiot.*

What did it matter? What was so important about that one little thing that it had to go this far?

For a moment, I could not speak, and something hot rose inside me. I forced it back and barely opened my mouth.

“Of course I meant it.”

—Yes. I see.

At the moment the blue eye-lights, flickering precariously, curved into a smile, a chilling voice rang out and brought everything to an end.

—Have you finished saying your farewells?

“……!”

—Bone Explosion.

*Boom!*

I instinctively crossed both arms in front of my face. The shock wave swept across my entire body and sent me flying.

When I barely managed to push myself upright, I saw a skull soaring high into the air and bones shattering into pieces.

And…

That was all.

There was no sign of the Skeleton Warlord anywhere.

*Thud!*

Hero’s Soul fell from the air and plunged deep into the ground.

Along with the hand of someone who had not let go of its hilt until the very end.

# Checkpoint Review — 260–264

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

# Chapters 260–264

## Plot

Cheongpung learns that Hong Dao has been killed and rushes to Shaolin despite remembering Jongni Chu’s terrifying power and still believing Jongni Chu is his friend. Shaolin is attacked by masked warriors serving the Lord of Heaven. Flame Tiger and Han Su, the Yin-Yang Twin Freaks, battle Hongcheon and Unnamed while seeking the Green Jade Buddha Staff. Jeok Cheongang and Jin Taekyung arrive during the massacre, defeat Flame Tiger, and Jeok kills him. Han Su escapes with the staff and delivers it to the Blood Lord, who beheads him after revealing that Jongni Chu was neither the culprit nor an accomplice but the plan’s greatest variable.

The Blood Lord claims responsibility for luring Hong Dao away with a false Heaven-Shaking Thunder threat and confronts Jeok and Taekyung. Cheongpung joins them, identifying himself as Huashan’s Invincible Divine Sword. The Blood Lord overwhelms all three, splitting Jeok’s completed Flame Divine Palm and treating their attacks as a test. Taekyung uses the System to resummon White Flame and pierce the Blood Lord’s Body-Protecting Qi and chest, creating an opening for Jeok to unleash the Dance of the Fire God and Demon. Jeok appears to defeat him but collapses from the exertion. The Blood Lord then rises apparently unharmed, leaving the Life-or-Death Crisis unresolved.

## Continuity

- Shaolin suffered a large-scale massacre; part of the Hundred and Eight Arhats Formation was destroyed, and many monks and civilians were killed.
- Hongcheon survived but lost an arm and was gravely wounded. Flame Tiger was killed by Jeok Cheongang.
- Unnamed’s fate remains unresolved after Han Su reached the Face-Wall Cave; Han Su escaped with the Green Jade Buddha Staff.
- Han Su delivered the Green Jade Buddha Staff to the Blood Lord before being killed.
- The Blood Lord claims to have killed Hong Dao and says Taekyung’s intervention advanced his plan by one day. Jongni Chu was the plan’s greatest variable, not its culprit or accomplice.
- The Blood Lord is an apparently young but extremely old Dark Heaven figure whose power may equal or exceed the Three Saints. His exact identity and rank remain unknown.
- The Blood Lord knows Cheongpung is Sword Saint Mae Jonghak’s Disciple and grandson.
- Taekyung pierced the Blood Lord’s chest by exploiting the System’s Inventory resummoning function for White Flame.
- Jeok Cheongang used the Dance of the Fire God and Demon, a technique previously used only once to kill a thousand Demonic Cult members, and is incapacitated or severely weakened by the exertion.
- The Blood Lord survived the Dance of the Fire God and Demon apparently without lasting injury. The outcome of the confrontation and the Life-or-Death Crisis remains unresolved.

## Translation Decisions

- Use **Hongcheon**, **Hundred-Step Divine Fist**, **Yin-Yang Twin Freaks**, **Lord of Heaven**, and **Face-Wall Cave**.
- Use **Yin Ghost** for Han Su’s epithet, **Blood Lord** for 혈주, **Heaven-Shaking Thunder** for 진천뢰, and **Four Saints** for 사성.
- Use **Life-or-Death Crisis** for 절체절명 and **Yama** for 염라, with Yama understood as the Buddhist lord of the underworld.
- Retain **Green Jade Buddha Staff**, **Exploding Blood Demonic Art**, **Unshakable Mind**, **Dance of the Fire God and Demon**, **Body-Protecting Qi**, **Invincible Divine Sword**, and **Returned to Simplicity**.
- Preserve the Blood Lord’s lightly mocking, confident tone during combat.

## Durable state

{
  "active_continuity": [
    "Cheongpung has joined Jin Taekyung and Jeok Cheongang against the Blood Lord at Mount Song.",
    "The Blood Lord knows Cheongpung is Huashan's Invincible Divine Sword and Sword Saint Mae Jonghak's Disciple and grandson.",
    "The Blood Lord can split Jeok Cheongang's completed Flame Divine Palm and repel Taekyung and Cheongpung with ease.",
    "The Blood Lord deliberately yielded three forms before beginning his real attack.",
    "Taekyung pierced the Blood Lord's Body-Protecting Qi and chest by resummoning White Flame through the System.",
    "Jeok Cheongang unleashed the Dance of the Fire God and Demon, then staggered from the exertion after apparently defeating the Blood Lord.",
    "The Blood Lord rose apparently unharmed after Jeok's final attack."
  ],
  "continuity_sources": [
    264
  ],
  "open_questions": [
    "How did the Blood Lord survive the Dance of the Fire God and Demon, and what is his true condition?",
    "What is the Blood Lord's true identity and exact position within Dark Heaven?",
    "What will be the result of the Life-or-Death Crisis after the Blood Lord's apparent recovery?",
    "Can Jeok Cheongang continue fighting after using the Dance of the Fire God and Demon?"
  ],
  "safe_through": 264,
  "temporary_decisions": [
    "Use Yama for 염라.",
    "Use Life-or-Death Crisis for 절체절명.",
    "Keep the Blood Lord's dialogue lightly mocking and confident during combat."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 260

# Chapter 260

“Cheong Young Hero. Young Hero Cheong, wake up.”

Smack! Smack!

“Umm…”

Cheongpung opened his eyes with a groan.

Someone was vigorously slapping his cheeks. It was fascinating in a way, since it was his first time being slapped, but strangely, it also felt rather unpleasant.

*Ah. So this is why people hate being slapped.*

With that small insight, Cheongpung opened his mouth.

“Excuse me.”

Smack! Smack!

“I’m aw—”

Smack! Smack!

“I’m awake…”

Smack!

Only after delivering one final blow did the hand finally stop.

A young man with a familiar face spoke with a stiff expression.

“You’re awake. Do you remember who I am?”

“It’s been a while, Warrior Hyuk Mujin.”

Hyuk Mujin sighed.

“So you do remember me.”

“Of course. I just never expected we’d meet like this.”

Cheongpung remembered Hyuk Mujin as a good person.

But when a good person he had not seen in a year was slapping him in the face, even Cheongpung could not help but feel wounded.

“I apologize if you were offended. I suddenly remembered the money I lost.”

“What?”

“No, the situation was so urgent that I committed a breach of etiquette.”

“Oh…”

If that was the reason, then Cheongpung could understand.

He nodded and looked around. Shouts rang out from every direction, and people were running about everywhere.

“Is this a festival?”

“……Does this look like a festival?”

“It isn’t?”

“No.”

Hyuk Mujin answered firmly before explaining the general situation.

Dharma King Hong Dao had been found dead, and the culprit was none other than…

“Jongni Chu?”

“Yes. The Always-Victorious Sword, Jongni Chu. That bastard. His exact identity is unknown, but the prevailing opinion is that he was an assassin sent by the Demonic Cult.”

“The Demonic Cult…”

It was a name Cheongpung had heard countless times from his grandfather, the Sword Saint. The place where the fiends and vile murderers who had once stained the entire world with blood had gathered.

And Jongni Chu was an assassin from that very Demonic Cult.

Without realizing it, Cheongpung shook his head.

“No.”

“What do you mean…”

Hyuk Mujin continued with an incredulous expression.

“You were attacked by him yourself, and you still don’t understand? The shock must have been so great that you can’t remember, but you nearly died at his hands.”

No. Cheongpung remembered everything clearly.

The helplessness and fear he had felt against a master whose strength nothing could overcome. Even the final moment, when he had thought of death for the first time in his life.

*I was scared. Truly scared.*

Even thinking about it made the fine hairs on his body rise, and his palms grow damp.

But why?

Why did Jongni Chu’s face keep floating before his eyes—that face smiling brightly as he asked Cheongpung to become his friend?

After remaining tightly shut for a moment, Cheongpung’s lips parted.

“He’s my friend.”

“……What?”

“That man is my friend. He couldn’t have done it.”

“Young Hero Cheong!”

Hyuk Mujin was startled and anxiously glanced around.

Only after confirming that no one was paying attention to them did he speak in a hushed voice.

“Are you insane? Jongni Chu is already practically an enemy of the entire Murim. You’re calling someone like that your friend…”

He was an assassin who had murdered the Abbot of Shaolin Temple and fled. Merely being acquainted with Jongni Chu could be enough to earn Cheongpung a sound thrashing.

Even if he was the disciple the Sword Saint had raised like his own flesh and blood, people would still glare at him.

“Never mention him out loud again. Do you understand?”

“But…”

Cheongpung was about to say something, but he closed his mouth at the look in Hyuk Mujin’s eyes.

“He’s a demonic fiend. I don’t know what kind of underhanded trick he used to win your favor, but it was all an act intended to assassinate Master Hong Dao.”

“Are you certain? Did anyone see him kill him?”

“All the circumstances point to it. The pursuit party formed to capture him and the thousands of heroes who gathered to save Shaolin have finished preparing to depart.”

“Shaolin…”

“The Demonic Cult’s vile scheme has placed Shaolin in danger. Great Hero Jeok and the Captain already left ahead of us.”

Cheongpung slowly closed his eyes.

In the pitch-black darkness, the faces of Jin Taekyung and Jongni Chu flashed before him one after the other.

He did not deliberate for long.

“I’ll go ahead.”

“What?”

By the time Hyuk Mujin asked in a dazed voice, Cheongpung’s figure had already shot far into the distance.

The direction his toes pointed toward was Mount Song.

* * *

Mount Song was peaceful and beautiful enough to be counted among the Five Sacred Mountains.

But the place that should have been green and lovely was being stained with blood and screams.

“Aaaaaagh!”

“Kill every last one of them.”

Slash! Shhhhhhk!

Blood spurted from every direction whenever a flash of sword light gleamed.

On that peaceful Baekjung Day,[^1] in broad daylight, hundreds of masked men appeared out of nowhere and continued their slaughter with emotionless eyes.

“Protect the pilgrims! Do not retreat!”

Shaolin martial monks with Buddhist precept seals carved into their foreheads stood in their way, but the situation did not improve easily.

The masked men were all exceptional masters, making them difficult enough to fight on their own. On top of that, the martial monks had to protect the untrained scholarly monks, the young novice monks, and the countless pilgrims.

“What in the—!”

“Kraaagh!”

No one had expected anything like this to happen today.

Who would dare invade Shaolin Temple’s grounds in the very heart of the Central Plains, at the temple of the Mount Tai and Northern Dipper of the Murim?

The monks were being driven back in a rout beneath the swords of the cruel and despicable masked men.

That was when—

“You bastards! Do you even know where you are?”

The one who appeared with a thunderous shout was a short old monk barely five feet tall.

The old monk glared at the masked men staining Shaolin Temple’s grounds with blood. Blue sparks flew from his eyes.

“Demonic martial arts! So you’re the demonic fiends of Tianshan!”

Palm force burst from the old monk’s hands and swept across the area.

Kwoooong!

The masked men, who had only belatedly noticed the old monk and were rushing toward him, were caught in the palm force and killed.

It was an overwhelming sight. More than ten masters were crushed by a single attack.

However…

“The Lord of Heaven has commanded us. Kill the enemy.”

“Follow Heaven’s command. Kill them all.”

The hundreds of masked men did not stop.

They possessed neither agitation nor hesitation. They merely muttered as though possessed by ghosts and swung their swords.

Slash. Slash. Slash.

The old monk’s expression hardened at the sight.

*How ruthless…*

Even when their limbs were severed and their intestines spilled out, they did not so much as twitch an eyebrow.

The sight of masked men carrying out slaughter without feeling pain or fear, then collapsing abruptly like puppets with their strings cut, sent a chill through him.

*These things aren’t human. They’re demons in the flesh.*

If even an old monk who had fought his way through the Great Faction War felt that way, how much worse must it have been for everyone else?

The more experienced middle-aged martial monks were struggling valiantly, but the young monks witnessing such carnage for the first time trembled with fear.

Even so, they did not retreat.

It was probably because of the sense of duty possessed by disciples of the Buddhist faith when standing before demons.

*I never thought such a day would come.*

The old monk lamented inwardly.

During the last Great Faction War, Shaolin had been at the forefront more than anyone and shed more blood than anyone.

It had been a noble sacrifice that saved the Murim, but Shaolin had lost many elders and much martial knowledge. And the sacrifices of that era had returned today as tragedy.

*Of all times, this had to happen while my Senior Brother, the Abbot, was away!*

There was no helping it. He was the only person capable of protecting Shaolin now.

The old monk, Hongcheon, clenched his teeth and let out a lion’s roar.

“This is Shaolin!”

Although his name had been overshadowed by that of his Senior Brother, Hong Dao, he too was a master at the Supreme Peak realm.

His abilities were unknown outside the temple, but thanks to his relentless dedication to martial arts, his martial prowess had already surpassed Hong Dao’s.

“Come at me, all of you!”

Kwoooong!

It was at that moment that his palm force, filled with powerful Buddhist internal energy, swept in every direction.

“Oh-ho. The Hundred-Step Divine Fist?”

“We get to see that damn martial art again.”

Two voices pierced Hongcheon’s ears.

Two men slowly entered the temple grounds and came into view. At the same time, the masked men lowered their swords and withdrew in perfect unison.

“Was it you bastards?”

At Hongcheon’s words, spat out between clenched teeth, the red-bearded old man picked his nose and answered.

“That’s right. This old man right here.”

“You’re the vile demonic fiends of Tianshan.”

“Tianshan’s demonic fiends? Well, half of that is right and half is wrong. But I’ll let it pass.”

Hongcheon paused.

“You’re not from the Demonic Cult?”

“What does that matter? All you need to know is that I’m the one who’ll grab your shiny pate and rip it off.”

The old man with the air of a great scholar answered with a quiet smile.

“Flame Tiger, are you going to handle him?”

“Naturally. Now that I’ve seen the Hundred-Step Divine Fist, I can’t just let it go.”

“I keep telling you to rein in your temper.”

“I’ll think about it later. Right now, I want to kill that bald monk more than I care about my temper.”

Hongcheon glared at the two old men in turn.

The name Flame Tiger.

And the overwhelming auras radiating from the two old men, whose atmospheres were complete opposites.

“Could you two be…”

Flame Tiger gave a ferocious laugh and nodded.

“You’re only realizing it now? You’re still a youngster. All the monks of the Beom generation have been dead for ages… Are you the Dharma King’s youngest Junior Brother?”

“……!”

“Judging by that reaction, I guess I’m right. Han Su, what was the name of the old monk you killed at the end?”

“Beomgong.”

At the Dharma name of the Martial Uncle who had died during the Great Faction War, Hongcheon’s fist trembled.

*There’s no doubt about it. It’s them.*

How could he not recognize the names Flame Tiger and Han Su?

Or the epithets of the villains who had killed countless Shaolin disciples?

“The Yin-Yang Twin Freaks.”

It was a story from the distant past.

The two demonic fiends had each ruled over the tropical rainforests of Nanman and the great snowy mountains of the north. They had come to the Central Plains and stained the world with blood, while the orthodox faction’s net over heaven and earth, spread to pursue them, had been torn apart by the Demonic Cult’s invasion.

The two fiends had barely survived, entered the service of the Demonic Cult, and earned a terrifying reputation during the Great Faction War.

“The Yin-Yang Twin Freaks… It’s been a long time since I heard that from someone else’s lips.”

“Those were good times. Few things have ever been as enjoyable.”

Flame Tiger shook his head as he smiled fondly at the horrible past.

“No, no. Still, I prefer things as they are now.”

“Of course. We couldn’t even come to Henan back then.”

“It was all because of that damned Martial God.”

“But the Martial God is gone now.”

“Hardly any of those so-called Ten Kings and Three Saints remain, either.”

Han Su watched Flame Tiger with a faint smile. Then he suddenly brought his palms together toward Hongcheon.

“Ah, come to think of it, I’d forgotten for a moment. Please accept my condolences.”

Hongcheon, who had stiffened at the appearance of the two old monsters, sensed something ominous and asked:

“Condolences? What are you talking about?”

“On our way here, we heard that someone had died. Dharma King Hong Dao—your Senior Brother.”

“……!”

Shock struck him, making the world before his eyes seem to go dim.

His Senior Brother, who should have been at the Murim Alliance, was dead?

That was impossible.

“Nonsense!”

Han Su gave a short laugh as he looked at the shaken Hongcheon.

“Whether it’s true or not is for you to decide. And…”

Flame Tiger’s heated voice continued.

“All the monks here, including you, will die. That’s our judgment.”

Rustle.

As if they had sensed their leader’s aura, the masked men took a step forward with emotionless eyes.

A deadly edge rising from hundreds of sword blades filled Shaolin Temple.

Hongcheon’s eyelids trembled as he watched.

*Senior Brother… Is it true?*

But the trembling soon subsided, and light returned to his eyes.

The old monk, who had devoted eighty years to martial arts, clenched his fists.

“I never thought I’d have to face the Yin-Yang Twin Freaks at the same time. Come, you damned old monsters.”

“Wahahaha! This friend has quite a foul mouth for a monk. I like that you’re still so full of youthful vigor.”

Flame Tiger burst into hearty laughter and stepped forward.

“Unfortunately, one old man is enough for you. Han Su has a more pressing matter to attend to.”

“A very pressing matter.”

Han Su smiled faintly and continued.

“So will you step aside? I have to go to the Face-Wall Cave.”

The Face-Wall Cave.

At that word from Han Su, Hongcheon felt as though his heart had dropped.

Unnamed was there. His Senior Brother’s only Disciple.

And…

*The Green Jade Buddha Staff.*

At last realizing the enemies’ objective, Hongcheon let out a lion’s roar.

“Stop them by whatever means necessary!”

“Stop us? That won’t be enough.”

The Yin-Yang Twin Freaks flicked their hands, dark smiles on their faces.

As though they had returned to the days of fifty years ago, horrifying killing intent surged from their entire bodies.

“Kill them all.”

Fwoooooosh!

[^1]: Baekjung is a traditional Korean Buddhist observance held on the fifteenth day of the seventh lunar month.
## Chapter artifact 261

# Chapter 261

Blood welled up.

The beard streaked here and there with white was soaked in blood. The middle-aged monk forced out a broken voice.

“D-Demon. You’re a demon.”

A calm voice slipped into his ear.

“Shakyamuni drove away the demons’ temptations and attained enlightenment beneath the Bodhi tree, or so I’ve heard. But…”

Shaaak!

A hand carrying razor-cold blue force emerged from the monk’s chest.

The gaping wound had already frozen over, and frost-covered droplets of blood fell to the ground like shards of ice.

“No enlightenment can endure in the face of death.”

The monk trembled as a chill swept through his entire body.

He did not know whether it was because of the extreme Yin-Cold Technique that had frozen even his internal organs, or because of the aura of death that had reached his very eyes.

No. He could not know.

Ssslip. Thud.

The old man looked down at the monk, who had died with his eyes wide open.

The eyes of Yin Ghost Han Su sank deeply.

*That was dangerous. More dangerous than I expected.*

He looked around. At the entrance to the collapsed Face-Wall Cave lay four corpses, including the middle-aged monk who had just fallen.

*The Four Great Vajras.*

As martial monks counted among Shaolin’s finest, each one possessed formidable martial arts.

The last bald monk in particular had been a master who had reached the early stages of the Supreme Peak realm. If Han Su had not traded flesh for bone, he might have lost his life to the Four Great Vajras’ combined attack.

*Persistent bastards. Somehow, they’ve kept their lineage alive.*

Shaolin had suffered losses approaching ninety percent during the last Great Faction War.

The damage had been so catastrophic that Shaolin could no longer compare to its former days as the greatest sect under heaven. Even so, the power built over a thousand years still remained.

*But that ends today.*

Every part of the plan was proceeding smoothly. Dharma King Hong Dao was dead, the Four Great Vajras had fallen, and Hongcheon would soon meet his end at Flame Tiger’s hands.

Hundreds of killers stripped of every sensation would cover Mount Song in blood and withdraw only after burning the martial arts manuals in the Scripture Depository.

If Shaolin lost its leading masters as well as its martial arts, its decline would be certain.

And there was a mission that took priority over everything else.

*The Green Jade Buddha Staff.*

Han Su could not guess why the sacred treasure of Shaolin was so important, but he had to accomplish his task.

Because it was none other than the Lord of Heaven’s command.

Was that not why *he*, the one who enjoyed absolute trust, had come with them?

*“I’ll take care of Hong Dao. You bastards take care of Shaolin. If you fail to find the Green Jade Buddha Staff… I’ll leave what happens next to your imagination.”*

Han Su’s face hardened as he recalled the final words *he* had spoken.

There could not be a single mistake. If he failed, he would pay the price in full.

Boom!

Han Su flicked his sleeve, revealing the entrance to the Face-Wall Cave that had been blocked off.

Even the massive stone gate that now appeared could not stop his advance.

Rumble!

The stone gate collapsed with a deafening roar. Beyond the cloud of dust and stone powder, a pair of eyes shone with piercing light.

“Benefactor. What brings you here?”

Han Su saw the young monk slowly rise from his cross-legged position and curled up the corners of his mouth.

“Are you Hong Dao’s Disciple?”

“And what will you do if I am?”

“I came to receive an item.”

“I have nothing to give you, Benefactor.”

“Then let me correct myself. I came to take it.”

“Someone reeking of blood cannot be allowed to take even a single grain of rice.”

“Don’t trouble yourself with hesitation. I’ll take your life along with it.”

“Amitabha.”

With his palms joined and his prayer beads wound around one hand, Unnamed’s eyes gleamed with determination.

“It won’t be easy.”

* * *

Hongcheon and Flame Tiger.

The battle between the two fist masters who had reached the Supreme Peak realm was fierce.

Screeeech! Boom!

Every movement—each thrust, swing, and rising kick—carried tremendous power.

It was a battle between superhuman beings who had stepped into the lofty realm known as Supreme Peak, one in which no one dared interfere.

But as time passed, the scales began to tip.

Boom!

The moment their two fists, wrapped in qi force, collided, a line of red blood ran from one man’s mouth.

“Cough.”

The gray robes worn by the monk were stained bright red.

Flame Tiger bared his yellow teeth as Hongcheon was driven back a dozen steps, as if swept away by an invisible wind.

“Brat. When you were still suckling at your mother’s breast, this old man was rampaging through Nanman. You’re still thirty years too young.”

Hongcheon wiped his mouth with his sleeve. Despite his pale complexion, the old monk’s eyes burned fiercely.

“You truly are an old monster. How about getting into your coffin already?”

“Even when the orthodox faction cast a net over heaven and earth, they couldn’t catch this old man. A bald monk like you doesn’t stand a chance.”

Hongcheon bit his lip as Flame Tiger’s aura blazed even more fiercely.

He knew those words were not mere confidence. They were simply the truth.

*What kind of monster is he to still be flying around like that?*

During the Great Faction War, the Yin-Yang Twin Freaks had already passed sixty.

And yet, despite clearly being well over a hundred years old, Flame Tiger showed no sign of fatigue.

Internal energy whose limits could not be guessed. Experience forged through countless killings. Even his one weakness—aging—seemed to have passed Flame Tiger by.

The future looked bleak.

*But there’s still hope.*

Hongcheon’s eyes shifted slightly. His gaze moved toward the more than one hundred martial monks fighting the masked men.

Precisely one hundred and eight men.

They were the Hundred and Eight Arhats, the face and pride of Shaolin Temple.

As the most elite of the elite, selected only after careful screening, they swung their precept blades and Zen staffs and steadily drove the masked men back.

“They are the greatest criminals under heaven. Show them no mercy!”

“Open the Killing Gate!”

The true strength of the Hundred and Eight Arhats was revealed when they deployed the Hundred and Eight Arhats Formation.

And every one of them was carrying out his assigned role flawlessly.

They were calmly reproducing in actual combat what they had practiced hundreds and thousands of times.

Clang-clang-clang! Slash!

Under the pressure of the Hundred and Eight Arhats Formation, which bore down on them like the palm of the Tathagata, the masked men began falling one after another, spraying blood.

Unlike the one-sided disadvantage at the beginning, the battle had now become evenly matched.

*If things continue like this… we can do it.*

The Murim Alliance was only a few shichen away. If reinforcements arrived, the Yin-Yang Twin Freaks and the masked men would be the ones in trouble.

It was at that very moment that a glimmer of hope crossed Hongcheon’s eyes.

“Wahahaha!”

“...?”

“Your thoughts are written all over your face. What an innocent monk you are.”

Hongcheon’s face hardened. He had noticed something strange in Flame Tiger’s attitude.

*Did he already know this would happen?*

But why?

Before the question could continue, a deafening roar shook the earth and left his ears ringing.

Kwooooom!

Hongcheon stared at the scene before him with his mouth hanging open.

In a world that seemed to have slowed down, human limbs and blood pouring down like a sudden rain could be seen among the mounds of earth that had shot more than ten zhang into the air.

And one section of the Hundred and Eight Arhats Formation had vanished, as though swallowed by a gigantic monster.

“No!”

Along with Hongcheon’s scream, the flow of time returned to normal.

An area more than ten zhang across had been reduced to a wasteland by the explosion. More than twenty Arhat monks had been turned into chunks of flesh.

The masked men surged into that place like a wave.

Slash. Slash. Slash!

The Arhat monks were still only human.

Before their eyes, frozen by the shock, flashing sword light filled their entire field of vision.

This was a battlefield that allowed no moment of carelessness.

The price of hesitation was horrific.

“Aaaaaagh!”

“Junior Brother!”

The Hundred and Eight Arhats Formation, which had been no different from an invincible shield, collapsed helplessly. Several old monks belatedly tried to restore the formation, but it was all in vain.

Their opponents were not ordinary people.

They were beings worthy of being called demons.

“The Lord of Heaven has commanded us. Kill the enemy.”

Tss-tss-tss-tss.

As one masked man muttered in a toneless voice, red light seeped from the seven openings of his face.

The Arhat monks widened their eyes in stunned disbelief at the strange phenomenon they were witnessing for the first time in their lives.

“W-What is that?”

“Demonic martial arts! It’s demonic martial arts! Everyone, get away!”

But it was already too late.

The red light had expanded until it wrapped around the masked man’s entire body before bursting in every direction, enveloping dozens of Arhat monks and several masked men.

Boom!

An explosion. A deafening roar. Screams.

Someone’s limbs flew through the sky, and the rain pattering down was red.

Red veins spread across Hongcheon’s eyes as he stared blankly at the scene.

“H-How dare you...”

Shaolin was collapsing.

Shaolin Temple, which had remained unshaken even during the Great Faction War, was now overflowing with corpses and death.

The young Disciple who had greeted him with a smile every morning had breathed his last. The Junior Brother with whom he had built a friendship over decades had vanished without a trace.

As the hellscape unfolded before his eyes, drops of blood fell from his tightly clenched fist.

“This can’t... This can’t be happening.”

Flame Tiger threw back his head and laughed heartily at Hongcheon’s muttering.

“It’s called the Exploding Blood Demonic Art. It’s incredibly tricky, so it’s difficult to master, but it’s perfect for situations like this. I brought along a couple of them... They’re even more useful than I expected.”

“How dare you bastards—!”

With a cry that was almost a scream, Hongcheon shot forward.

But waiting for him was a fist wrapped in red qi force.

Bababoom!

His Body-Protecting Qi shattered, and a barrage of powerful punches battered Hongcheon’s limbs.

The pain was so intense that his vision went dark. Blood gushed from his mouth, mixed with pieces of his internal organs.

“Gwaaaargh!”

Through Hongcheon’s blurred vision, Flame Tiger approached with leisurely steps.

“You stupid bastard. You studied Shaolin’s martial arts until that age, and you forgot about an unshakable mind?”

“Cough. Cough!”

It was an obvious mistake. No matter what happened, he should not have lost his composure. Whatever he saw, he should have responded calmly.

His opponent was a monster who had already been comparable to the Ten Kings during the Great Faction War.

The best course of action had been to maintain the standoff somehow and buy time.

“You bastard...”

Even so, Hongcheon rose to his feet, breathing heavily.

Not yet.

If he fell, Shaolin would fall with him. He had to defend this place until his final breath.

For one more moment. So that even one more person might escape alive.

That was the old monk’s final duty after devoting his entire life to Shaolin.

“Come.”

Flame Tiger frowned at the fire burning in Hongcheon’s eyes.

“This is why I hate monk bastards. They’re about to die, but they still insist on acting tough.”

“What would a demonic fiend like you know?”

“I think I know one thing.”

Flame Tiger laughed savagely.

“You’re dying right now.”

Whoosh!

Hongcheon, already suffering severe injuries, was too slow to keep up.

Before he knew it, Flame Tiger had reached him. His fist slammed into Hongcheon’s shoulder.

Thud!

With a heavy sound, the qi force carried by that single punch cleaved through flesh and bone.

Hongcheon screamed, his arm gone from the shoulder down.

“Aaaaaagh!”

“You damned bald monk. You dared dodge this old man’s fist? Let’s see you dodge this one, too.”

As Hongcheon writhed in pain and injury, Flame Tiger’s foot pressed down on his head.

Even a tenth—no, a hundredth—of his strength would crush Hongcheon’s head like a watermelon.

“What do people say at a time like this? Ah, right.”

Flame Tiger tapped his forehead theatrically and continued.

“May you be reborn in paradise.”

Grrrrk.

The pressure increased slowly.

Death was bearing down on Hongcheon’s eyes.

“Take that filthy foot off him. Before I turn your filthy spirit into ash.”

“Let’s crisp up his chili pepper.”

Two voices pierced Flame Tiger’s ears.

The first belonged to an old man. The other was young—young enough to be almost startlingly green.

Flame Tiger turned his head toward the direction of the voices.

His face hardened.

“The Fire King...!”
## Chapter artifact 262

# Chapter 262

What awaited us when we arrived at full speed was a scene so horrific it was almost impossible to look at.

Corpses, pools of blood, arms and legs with no owners…

If the Shaolin Temple I had seen with my own eyes a year ago had been a beautiful painting of a utopian paradise, then what lay before me now was a painting of hell.

*These fucking lunatics.*

They had clearly been killing civilians and Murim warriors alike, indiscriminately.

Beyond the masked men fighting Shaolin’s monks, I saw an old man with a red beard.

“The Fire King…!”

Without taking my eyes off the old man, I asked:

“Do you know him?”

“No.”

“What about the monk pinned beneath him?”

“Hongcheon. Hong Dao’s youngest Junior Brother. He’s grown a lot since I last saw him.”

“……That’s for sure.”

He had grown so much he looked well over seventy.

Just as I was left speechless, the old man’s burning gaze swept over us.

“Are you the only ones?”

Jeok Cheongang answered in an indifferent voice.

“What if we are?”

“Heh heh. Looks like you’ve finally found a place to die, old man.”

“Even if your head is empty, you should still speak properly. It isn’t a place to die. It’s a place to kill—and that includes every one of you.”

The old man’s eyebrow twitched.

“How arrogant. You haven’t changed.”

“Haven’t changed? Have we met before?”

“I saw you once from a distance. I regretted it for years that we never got to test which of us was stronger.”

“What’s your name?”

“Flame Tiger! I am the tiger of Nanman!”

“The Yin-Yang Twin Freaks? Good. There should be one more of you, so there’s no need to capture you alive. Killing you will be fine.”

Jeok Cheongang clicked his tongue.

“Still, you’re one hell of a lucky bastard. You turned around with the Sanzu River right in front of you.”

“Is that really so?”

Flame Tiger’s eyes blazed. At the same time, fist force gathered around his rough, rock-hard fist.

I had expected as much, but the old man was also a Supreme Peak master. He had even trained in the same kind of Scorching Yang Qi as us.

“You arrived much sooner than I’d heard… but that changes nothing.”

*Than he’d heard?*

For an instant, I wondered how Flame Tiger could have received information so quickly.

*Even if he used a messenger pigeon, we should have been faster.*

But I had to put that question aside for the moment. Flame Tiger had tightened his grip around Hongcheon’s head as though he intended to crush it.

Blood trickled from the mouth of the old monk, who was drenched in it from head to toe.

“Cough. Cough.”

“Do you want to keep this monk alive?”

“……”

I felt Jeok Cheongang’s body tense.

The distance between Flame Tiger and us was more than thirty *jang*.[^1] Even Jeok Cheongang could not recklessly charge forward. If he did, Hongcheon’s head would be crushed like tofu.

“Put him down at once.”

Beneath Jeok Cheongang’s calm voice, I could feel anger boiling like lava.

Flame Tiger grinned.

“I heard you were close to that bald monk, Dharma King Hong Dao. I guess it’s true. Did he ask you to look after his Junior Brother as he died?”

“Hong Dao was a wiser and more virtuous monk than anyone. His name is not fit to pass through your filthy mouth.”

“He’s already dead, either way. I wonder if he’s crossing the Sanzu River by now.”

Jeok Cheongang stared at Flame Tiger with sunken eyes before parting his lips.

“Keep going.”

“What?”

“I said keep going. Do you really think you can shake this old man with that?”

“Y-You damn old monster.”

Flame Tiger’s face flushed red as he shook Hongcheon’s head.

“You’re saying it doesn’t matter if this monk dies?”

“It doesn’t.”

“What?”

“It’s regrettable that I can’t save him, but Hong Dao did not ask me to look after his Junior Brother. He entrusted Shaolin to me.”

Tss-tss-tss-tss!

At that moment, immense internal energy gathered in Jeok Cheongang’s hand.

It quickly took shape and shot forward like an arrow.

Not at Flame Tiger, but at the masked men who had been ceaselessly swinging their swords.

Kwooooooong!

The terrifying mass of internal energy unleashed from Jeok Cheongang’s hand pierced straight through the center of the masked men.

Like a hungry fire dragon, it rampaged through them, devouring and burning everything it brushed against.

Whoosh!

For the first time, emotion appeared in the masked men’s otherwise lifeless eyes.

Fear and pain.

“Aaaaaagh!”

“Aaaaargh!”

Flames surged into the air amid horrific screams.

Several dozen men staggered away with their bodies ablaze. Several dozen more had already stopped breathing.

The masked men froze at the sight, and the monks’ precept blades and Zen staffs flew toward them.

“We’re not finished yet!”

“Drive out the evil fiends!”

Fwoosh! Slash!

Jeok Cheongang had overturned the situation in an instant. He glared coldly at Flame Tiger.

“If you’re going to kill him, kill him. If not, put him down properly. Don’t try to play the fox when you’re a bear, you bastard.”

“Y-You damn old man!”

Whoosh!

Flame Tiger kept pretending to be a fox until the very end.

He threw Hongcheon at us and charged in close behind him.

His intention was obvious. He planned to use Hongcheon’s body as a shield and exploit the opening.

—You take Hongcheon.

A single thread of Sound Transmission pierced my ear.

Without waiting for the other to move, Jeok Cheongang and I kicked off the ground.

Four silhouettes shot toward one another.

I caught Hongcheon’s body, while Jeok Cheongang leaped over him and attacked the fox—or rather, the bear—hiding behind him.

Kwoooong!

I let myself ride the pressure wave that erupted from the terrifying clash.

After sliding more than twenty *jang*, I laid Hongcheon down in a nearby patch of grass. Then I leaped toward the two Supreme Peak masters locked in a fierce exchange.

Of course, Flame Tiger was not the sort of man who would stand there grinning and watch me come at him.

“You bastard!”

Fwoosh—thud!

My knee rang with a sharp vibration as it blocked a foot as thick as a log.

But that was all.

The gap between Supreme Peak and Peak was impossible to bridge, no matter how much luck one had.

But I did not have mere luck.

I had heaven’s luck.

*The System.*

*I can take him.*

I could not handle him one-on-one under normal circumstances, but Flame Tiger was already struggling just to contend with Jeok Cheongang.

The old man’s only mistake was underestimating my existence far too much.

“I’m confiscating your dentures for four months.”

At my broad grin, Flame Tiger’s face turned red enough to burst.

“You green little brat!”

“You yellow old geezer!”

“Kraaaagh!”

Flame Tiger threw off Jeok Cheongang and charged at me with a roar.

“I’ll kill you first!”

Whoosh!

It was a tremendously powerful punch. If I took that fist wrapped in fist force with my bare body, I would not escape unscathed.

I stepped back, grabbed White Flame from my back, and swung it.

Clang!

The punch stopped with a thunderous sound.

Flame Tiger’s eyes grew as wide as lanterns.

“Ten-Thousand-Year Cold Iron?”

“As expected, expensive weapons are the best. Isn’t that right, Old Master?”

Jeok Cheongang did not answer.

Instead, his fist, dyed blue-white, was already flying toward Flame Tiger.

Kwoong!

The ground shook with the thunderous impact.

The two fists had met perfectly, but one man’s fist had its bones crushed and was charred black.

Flame Tiger muttered with a dazed expression.

“H-How?”

“Did you think everyone who practiced Scorching Yang Qi was the same?”

Jeok Cheongang spoke indifferently, but lava burned in his eyes.

Heat incomparable to the flames of Flame Tiger surged from his entire body and pressed down on everything around him.

Flame Tiger muttered like a groan.

“The Fire King…”

“That’s right. I am Jeok Cheongang, the Fire King and the eighteenth-generation successor of the Fire Gate Clan.”

“This can’t be… Cough!”

I launched myself at Flame Tiger as he spat blood and tried to flee.

“Where do you think you’re going?”

Crack!

My foot came down hard, crushing his instep and driving deep into the ground.

A pained groan escaped between Flame Tiger’s teeth, followed by a spray of blood.

The next moment, two streaks of light pierced into his abdomen as his upper body staggered.

Whoosh!

The difference in realm meant a difference in power, but the martial art itself was the same.

*Flame-Extinguishing Divine Fist.*

Thud!

The Body-Protecting Qi wrapped around his entire body like armor shattered.

A fountain of blood erupted from Flame Tiger’s wide-open mouth.

“Gueeegh!”

They were both Supreme Peak masters, but the difference between them was enormous.

Jeok Cheongang looked down at Flame Tiger, who was panting from his severe Internal Injury.

“Your luck ends here.”

“Cough. W-Wait a moment.”

“There is neither a reason nor time for that.”

“I’ll tell you everything! R-Right, Dark Heaven! Everything about Dark Heaven…”

“Didn’t this old man tell you not to play the fox?”

Fwoosh—thud!

There was not the slightest hesitation in Jeok Cheongang’s hand.

Flame Tiger’s head vanished. His body swayed before collapsing into a pool of blood.

I casually wiped the blood splattered across my face and said:

“Wouldn’t it have been better to keep him alive?”

“You don’t reveal important secrets to a bear as stupid as that.”

“Even so…”

“The bear is dead. Now we have to catch the fox.”

With those cryptic words, Jeok Cheongang turned his head.

More than a hundred *jang* away, an old man stood perfectly still, watching us.

A short staff glowing with green light was held in his hand.

“The Green Jade Buddha Staff!”

“Yin Ghost Han Su. He’s next.”

The next moment, as though he had understood those words, Han Su’s figure shot away at blinding speed.

* * *

Whoosh!

Han Su poured all his strength into his movement technique.

He could feel two auras drawing closer behind him, little by little—ever so slowly.

*Damn it!*

He had recognized him at first sight.

The Fire King, Jeok Cheongang.

He had never expected that a monster reputed to be among the very first of the Ten Kings would arrive so quickly.

*But who’s the other young man?*

The question briefly crossed his mind, but he soon erased it.

The identity of that young brat was unimportant.

What mattered was that Flame Tiger, whose martial prowess was equal to his own, had died at their hands.

*What an idiot. He attacked the Fire King instead of the Thunderbolt Saber King.*

Han Su had first met Flame Tiger during the Great Faction War and had spent several decades with him, but they were not sworn brothers who had pledged a Peach Garden Oath.[^2] Han Su had no intention of dying on the same day and at the same hour as Flame Tiger.

*Just a little farther. Just a little more!*

His mission was complete.

The Green Jade Buddha Staff in his hand was proof of that. If he reached the designated location and rendezvoused with *him*…

He would survive for certain.

Because *he* was a master even the Fire King could not handle.

*Flame Tiger. If that happens, I’ll avenge you.*

Just as Han Su tightened his grip around the Green Jade Buddha Staff, his face hardened.

*This is…!*

Another aura was drawing closer in the distance.

This time, it was not behind him.

It was ahead.

At first, he thought it might be reinforcements from the orthodox faction, but the aura he sensed this time belonged to only one person. Its momentum was not particularly strong, either.

*Damn it. Things are getting complicated.*

If his path was obstructed even briefly, the Fire King might catch him.

Han Su bit down hard on his lip and squeezed every last ounce of strength from his body. The moment he broke through the undergrowth—

“Ah!”

A short exclamation escaped him, and his face filled with joy.

No emotion could compare to the relief of surviving when death had seemed certain.

Han Su called out to *him* in a voice filled with happiness.

“Blood Lord!”

* * *

As though we had planned it, Jeok Cheongang and I stopped at the same time.

Han Su, who had transformed from a frantic fugitive into a swaggering predator, was waiting for us.

“There they are! The Fire King—that goddamn old man—and the young brat killed Flame Tiger!”

No.

Han Su was not a predator.

He was merely a fox borrowing the might of a tiger.

The real predator was the man standing quietly beside Han Su.

It was strange that I could not sense anything from him.

And that made him seem even more dangerous.

Jeok Cheongang, however, was different.

His face stiffened as he asked:

“Who are you?”

“Your enemy.”

The young man smiled faintly before continuing.

“The enemy who killed your most precious friend.”

……What?

[^1]: A *jang* is a traditional Korean unit of distance, roughly three meters, though its exact length varied historically.

[^2]: The Peach Garden Oath refers to the famous oath of sworn brotherhood in *Romance of the Three Kingdoms*.
## Chapter artifact 263

# Chapter 263

“That makes me the enemy who killed your most precious friend.”

At those words, I froze.

The same thought must have crossed Jeok Cheongang’s mind.

*What did I just hear?*

For a moment, I couldn’t understand it. The words that had come from the mouth of a young man with an unfamiliar face tangled together in my head.

*Wait…*

*He killed Hong Dao? That bastard?*

Memories etched deep into my mind surfaced before vanishing again.

Jongni Chu disappearing in the middle of the duel. Hong Dao gasping at death’s door. And the four words he had left as his final message.

*Jongni Chu. Dark Heaven. Unnamed. Buddhist Staff.*

What, exactly, had everything I had seen and heard until now meant?

Where had it all begun, and how had it unfolded?

I stood frozen like a stone statue, desperately trying to grasp the thread connecting everything. But before I could put my thoughts in order, a dry voice slipped between Jeok Cheongang’s lips.

“You killed Hong Dao?”

His words came in broken fragments, soaked in patience, rage, and disbelief.

At the sight of Jeok Cheongang, the young man smiled faintly and nodded.

“I told you, didn’t I? It was much easier than I expected. I told him I was going to set off a Heaven-Shaking Thunder in the spectator stands, and he followed me without a fuss.”[^1]

“Heaven-Shaking Thunder? Had you planted explosives?”

“Ah, that? Of course it was a lie.”

“……What?”

“Why do people lie? Because there are idiots who occasionally fall for it.”

Blood dripped from Jeok Cheongang’s fist as he clenched it hard enough to crush something.

“He wasn’t fooled. He let himself be fooled. That was the kind of person Hong Dao was.”

“He let himself be fooled? I suppose that’s possible. If you say he was trying to prevent some unforeseen slaughter because he was a bald bastard who happened to be the Abbot of Shaolin, it sounds plausible.”

“You bastard!”

“Don’t give me too much grief. I hadn’t planned anything this shoddy, either. But things became tangled in a place I never expected. Of course, you had something to do with that, too…”

The young man’s gaze suddenly shifted toward me.

“Jin Taekyung, the Sleeping Dragon of Shanxi. You played your part.”

My body seemed to stiffen just from meeting his eyes.

I didn’t know whether it was because of the hostility I felt toward him or because I could sense the overwhelming difference in power between us.

*Maybe both.*

I bit my lip and glared at the young man.

“What the fuck are you talking about?”

“Because you suddenly joined the duel, I had to move the plan forward by a day. The biggest variable among them was the Always-Victorious Sword, Jongni Chu.”

“……!”

That confirmed it.

Jongni Chu had not been the culprit—or even an accomplice.

“Well, in the end, everything was taken care of neatly.”

The young man extended a hand.

Realizing what he wanted, Han Su hurriedly held out an object.

“The sacred treasure of Shaolin—the Green Jade Buddha Staff.”

“So this is the…”

The young man’s long fingers slowly brushed over the softly glowing Green Jade Buddha Staff.

But the next moment, he stared intently at Han Su’s face.

His wrinkled hand was still holding on to the staff.

“You can let go now.”

Han Su swallowed hard before answering.

“B-Blood Lord, I have one request.”

“A request? Go ahead and tell me. You worked hard, so I’ll do my utmost to grant it.”

It was a strange sight—no, a bizarre one.

An old man groveling before a young man who looked young enough to be his grandson.

And it was even stranger because that old man was the great demonic fiend who had turned Shaolin Temple into a river of blood.

*What the hell is that bastard’s identity?*

There were only two possibilities.

His status within Dark Heaven was unimaginably high, or he was much older than he looked.

There was also a good chance that both were true.

Whatever the case, Han Su’s face brightened at the young man’s answer.

“R-Really?”

The Blood Lord clicked his tongue.

“Have you spent your whole life being deceived? You completed your mission perfectly, so a Reward is only natural. But I wonder what kind of difficult request our Senior Yin Ghost is taking so long to bring up.”

“It is not that difficult a request.”

“But it’s difficult for you to do yourself?”

“……I am ashamed to admit it, but yes.”

“Ah. I have a rough idea what it is.”

The Blood Lord jerked his chin toward Jeok Cheongang and me.

“You want me to kill those two, don’t you? Is that it?”

Han Su nodded with killing intent in his eyes.

The Blood Lord gave a short laugh.

“Well, this is unexpected. I suppose the two of you were closer than I thought.”

“He was at my side for half a lifetime. I will not be satisfied with anything less.”

“Loyalty… Well, that is good, too.”

“Kill them as cruelly as possible. I will lend a hand.”

“Will that be enough? If the orthodox faction comes swarming in, things will become troublesome. If we want to finish quickly and leave, you’ll have to sweat a little, Senior.”

“Then?”

“You take the Sleeping Dragon of Shanxi. I’ll take the Fire King. We should be able to finish within an ildagyeong at the latest.”[^2]

“You want me to take that young brat? Wahahaha! Very well!”

Their conversation was absurd. They spoke of our lives as if they were objects in their pockets.

At the same time, a chill ran down my spine.

*He means every word.*

The Blood Lord had just declared that he could kill the Fire King, Jeok Cheongang, within the time it took to drink a cup of tea.

The way Jeok Cheongang’s face had stiffened proved that those words were not mere boasting.

—If the situation becomes unfavorable, run.

At the Sound Transmission that suddenly reached my ear, I gave the slightest shake of my head.

A fierce battle was already raging above us. We could not expect help from Shaolin.

If I withdrew, Jeok Cheongang would have no choice but to face the concentrated assault of two Supreme Peak masters.

*The best course is to hold out here until the very end.*

Jeok Cheongang knew that, too.

And yet he had told me to run because he was warmer and more concerned than people realized.

*This is going to be genuinely dangerous this time.*

I licked my parched lips and gripped White Flame tightly.

Han Su sneered at the sight.

“Pathetic fool. Do you think anything will change because you hold that? Your attainment is commendable, but even if you died and came back to life, you could never defeat this old man.”

“Go fuck yourself.”

I spat a wad of phlegm onto the ground for all to see.

“Give me a few shichen of sleep in this world, and when I wake up, you’ll die by my hand.”

“What kind of bullshit is that?”

“If you don’t believe me, test it.”

“How dare this green little brat!”

It was unfortunate.

If I hadn’t been in the middle of a battle, and if time stopped completely when I used Logout instead of merely slowing down, I could have used an infinite amount of time to escape this crisis.

But those thoughts were nothing more than personal wishful thinking.

Now was the time to face reality, not indulge in delusions.

“I’ll freeze you alive.”

Step. Step. Crack.

Now I understood exactly why that damned old man was known as the Yin Ghost.

The ground froze beneath every step he took, and frost settled over the branches of the trees.

“What vicious Yin-Cold Earth Qi. But…”

Jeok Cheongang stepped in front of me.

“You dare not lay a hand on my Disciple.”

Whoosh!

If Han Su’s Yin-Cold Earth Qi was an iceberg, Jeok Cheongang’s Scorching Yang Qi was the sun.

If Flame Tiger’s martial arts had truly been equal to Han Su’s, then Jeok Cheongang’s overwhelming victory had been inevitable.

But Han Su’s expression was relaxed.

He knew there was a tiger behind him.

“Blood Lord, you will have to step forward.”

“Of course. We should get started.”

The Blood Lord tucked the Green Jade Buddha Staff into his robes as carefully as if it were a priceless treasure.

Then he moved.

No—he vanished.

And in the next moment—

Slash! Thump!

Along with a horrifying sound, a round object flew through the air and rolled to a stop at my feet.

White hair. A dignified-looking face. A faint smile still lingered around the mouth.

“……!”

“……!”

Jeok Cheongang and I widened our eyes at the same time.

Han Su, the infamous great demonic fiend and Supreme Peak master known as the Yin Ghost, had been beheaded in a single strike.

By the hand of the ally he had trusted without question.

Unlike Jeok Cheongang and me, who stood frozen in shock, the Blood Lord—the one responsible for everything—was perfectly calm.

“Fucking old man. This is why you should never take in people with no roots.”

He clicked his tongue and casually nudged Han Su’s headless body.

Splash!

The corpse toppled like a dead tree, spraying a fountain of blood across the ground.

“If you’re a sword, act like a sword. Go wherever the person holding you swings you. How dare you…”

Thud! Thud! Crack!

His kicks, loaded with internal energy, tore through flesh and crushed bone.

After stamping and grinding Han Su’s lifeless corpse beneath his feet several times, the Blood Lord swept his fallen hair back.

“There are always people who don’t know their place. They don’t know how strong they are or how far they should stick their necks out. Sleeping Dragon of Shanxi, don’t you agree?”

*…Me?*

What was I supposed to say?

I hesitated, then answered honestly.

“No. You just look like a crazy bastard to me.”

For a moment, the Blood Lord stared blankly at me.

Then a smile spread across his lips.

“You’re bold for a young one.”

“You’re still a young brat yourself, and you already seem a little unhinged.”

“Thank you for thinking of me as young. I’m older than I look.”

“Not that old.”

“Don’t push it. I’ve lived at least twice as long as you have.”

I looked him up and down with disbelief.

He stood at roughly my eye level, his body perfectly proportioned.

His face made him look like an inexperienced young man in his early to mid-twenties at most.

This could not be explained simply by calling him youthful-looking.

But if there was anywhere that anything could happen, it was the Murim.

“What? Surprised because I’m much older than you expected?”

I shook my head.

“No. If what you’re saying is true, I was thinking you’re a bastard who doesn’t act his age.”

“Wahahaha!”

The Blood Lord burst into cheerful laughter.

His behavior and speech were light—so light they bordered on frivolous.

And that was precisely why he felt even more dangerous.

Even now, as he bent forward laughing, I could not see the slightest opening.

Jeok Cheongang, who had been glaring at him as his shoulders shook, suddenly spoke.

“You will regret this.”

“Regret?”

The Blood Lord stopped laughing and frowned.

“Why would I regret it?”

“If you wanted to finish this cleanly, you should not have killed the Yin Ghost.”

“He was a rusty sword. Its usefulness had run out, so disposing of it was only natural.”

“A Supreme Peak master is a rusty sword… Then what does that make this old man?”

The Blood Lord stroked his chin.

“You are worth rating highly, Fire King. If the Great Faction War had continued for one more year, you probably would have become one of the Four Saints instead of merely one of the Three Saints.”

“Looks like my edge has not gone dull yet.”

“You are good enough to be called a fine sword.”

“What would happen if that fine sword were driven into your heart?”

“Who knows… I’m sturdier than I look. I don’t think that would draw even a drop of blood.”

“When Hong Dao died, this old man swore to heaven.”

The Blood Lord smiled faintly as Jeok Cheongang’s eyes sank into darkness.

“Even if the culprit were a demon god instead of a human, I would see this revenge through to the end.”

“That is touching and all, but…”

The Blood Lord’s smile vanished as he caressed the sword hilt at his waist.

“I have a feeling the Fire Gate Clan’s lineage will end today.”

Without taking his eyes off the Blood Lord, Jeok Cheongang asked me:

“What do you think of what he said?”

“I think your mouth needs a circumcision. It’s been spewing nothing but dickhead bullshit since earlier.”

The smile disappeared from the Blood Lord’s face.

“……You really are an interesting one.”

Step.

The Blood Lord took one step toward Jeok Cheongang and me before suddenly speaking.

“But how long does that little rat hiding over there plan to stay hidden?”

Rustle.

A strange man emerged from the distant grass and scratched the back of his head.

“Benefactor. I’m sorry. I’ve never been this frightened in my life…”

I had never been so happy to see Cheongpung.

[^1]: *Heaven-Shaking Thunder* is the literal name of a powerful gunpowder explosive.

[^2]: An *ildagyeong* is the short time it takes to drink a cup of tea.
## Chapter artifact 264

# Chapter 264

I never expected to be this happy to see that dumpling ghost. With even a cat’s paw being welcome at a time like this, Cheongpung joining us could be an enormous help.

Before I knew it, a cry of delight burst from my lips.

“Cheongpung!”

“Yes, Benefactor.”

As Cheongpung answered hesitantly, the Blood Lord recognized him.

“Oh-ho. I was wondering what kind of rat it was, but aren’t you Huashan’s Invincible Divine Sword?”

I had been hoping otherwise, but it was just as I feared. That was all the Blood Lord knew about Cheongpung’s identity.

It had been revealed during the duel that Cheongpung was a disciple of Huashan, but there was no way he knew that Sword Saint Mae Jonghak had raised his youngest disciple with the same love he would have shown his own blood.

This was the perfect chance to lull him into carelessness…

“Or should I call you the Sword Saint’s Disciple? Or perhaps his grandson?”

“……”

That son of a bitch. There was nothing he didn’t know.

Then again, Dark Heaven had recruited and planted the Head Elder decades ago. The Blood Lord was clearly one of Dark Heaven’s highest-ranking members.

*It would be strange if he didn’t know.*

The Blood Lord gave a quiet laugh at my disappointed expression.

“You don’t have to look so disappointed. It wouldn’t change anything even if that friend of yours joined you.”

Look at this guy…

Although Cheongpung and I had yet to move beyond the upper reaches of Peak, neither of us could be compared to an ordinary Peak master.

I had overwhelming stats and abundant combat experience. Cheongpung had innate martial talent and a genius-like combat sense that allowed him to combine dozens of martial arts at exactly the right moments.

And on top of that, we had the Fire King Jeok Cheongang—the greatest of the Ten Kings.

I thought this was a fight we could win.

“You’re underestimating us too much.”

“It’s a fact.”

“What?”

“If you wanted to kill me, you should have brought the Sword Saint instead of his Disciple.”

“……You little bastard.”

“There’s only one thing left to do.”

The Blood Lord answered in a relaxed voice and beckoned to us with one finger.

“Prove it with your martial arts.”

That was the only thing he had said so far that was actually right.

He was correct. A martial artist had to prove himself through martial arts.

Victory would prove our strength. Defeat would prove our weakness.

“When you meet Yama, tell him the Fire King sent you.”

Whoosh!

Along with his dry, ashy voice, Jeok Cheongang’s figure shot forward. At the same time, a familiar alert pierced my ears.

Ding.

> **System**
>
> - A sudden Quest, **Life-or-Death Crisis**, has been generated!
>
> - You cannot refuse the Quest. The Quest will be forcibly accepted!

Damn it. What an incredible Quest title.

I kicked off the ground and charged forward. I did not forget to call out someone’s name in place of a curse.

“Cheongpung! Now!”

Cheongpung flinched, bit down on his lip, and charged as well. The blue-steel sword in his hand danced smoothly, drawing plum blossoms through the air.

Fwoosh! Shhhhk!

On a quiet mountain path, Scorching Yang Qi heated the cool mountain breeze, while spear and sword tore through the burning air.

The Blood Lord watched us charge from the front and rear before his lips moved.

“Well then… Let’s see what you can do.”

* * *

Crack-crack-crack!

Jeok Cheongang flicked his hand. A palm force filled with Scorching Yang Qi burst from his wrinkled palm.

It was the Flame Divine Palm, already at Great Completion. Just as the Extreme Yang palm technique, said to burn even the soul, was about to engulf the Blood Lord’s entire body—

Whoosh!

A single gust of wind blew.

A saber had appeared in the Blood Lord’s hand. Before the saber force blazing an ominous red, the palm force of the Flame Divine Palm split in two.

Whoom! Boom!

The massive trees lining both sides of the path exploded.

Flames surged into the air amid a thunderous roar, while dirt, roots, and splinters of wood poured down like a sudden rainstorm.

And two streaks of light pierced through it all.

Whoosh! Shhhk!

A spear and a sword shot forward from the front and rear.

The Blood Lord twisted up the corners of his mouth and released the saber. At the same time, his newly freed fists struck the empty air.

Boom!

Compressed air exploded outward, unleashing a violent gale. Both the viciously thrusting spearhead and the plum blossoms blooming from the sword’s tip were swept away by the wind pressure.

Jin Taekyung and Cheongpung’s eyes widened as their bodies were pushed back against their will.

“……Fuck. He’s insanely strong.”

“H-How can this be?”

Crack.

The Blood Lord twisted his neck and retrieved his saber from the air. He had fought the two of us while using Seizing an Object Through Empty Space.

“Is that all you’ve got?”

“……!”

Jeok Cheongang’s eyelids trembled.

Who would have thought that a single form of the Flame Divine Palm at Great Completion could be defeated so easily? The Blood Lord had not dodged or deflected it.

He had cut it apart.

Jeok Cheongang’s heart sank as he realized that the Blood Lord was an even greater master than he had imagined.

*His words about bringing the Sword Saint if we wanted to kill him… They weren’t empty boasts.*

His opponent was a master who could easily be compared to the Three Saints.

No—perhaps he was even stronger.

Neither his internal energy nor his enlightenment in martial arts fell short of Jeok Cheongang’s own.

On top of that, the Blood Lord possessed a young, vigorous body capable of unleashing all of it without the slightest deficiency.

That day, Jeok Cheongang felt that his wrinkled hands looked smaller and more wretched than ever.

*If only I were thirty years younger… No, even twenty…*

When his body had been whole, he had lacked enlightenment. By the time he had acquired that enlightenment, his body had grown too old.

Water leaked from an old jar full of holes.

That was what Jeok Cheongang was like now.

*Perhaps this place will become my grave.*

The Blood Lord did not miss the way Jeok Cheongang’s eyes sank into silence.

He twisted up the corners of his mouth and chuckled.

“Old man. Are you starting to understand now? Do you grasp the situation?”

Jeok Cheongang calmly shook his head.

He knew that Jin Taekyung and Cheongpung were watching his mouth. He could not destroy their morale with careless words.

“You talk too much. We have only just begun.”

“You three have, perhaps. But I haven’t even started yet.”

“What did you say?”

“I heard that the orthodox factions show courtesy by allowing a master to yield three forms to a junior. I decided to imitate them.”

“……!”

The Blood Lord pointed one long finger at each of them in turn.

The three of them had each unleashed one form, making three in all. Just as he said, he had yielded three forms without moving from his spot.

“Now I’ll be going first. Go ahead and struggle.”

A red glow surged from the Blood Lord’s eyes. At the same time, his whites became stained red, and a massive, terrifying qi spread outward from his body.

And then—

Rumble, rumble, rumble!

Mount Song trembled.

* * *

Shhhhk! Boom!

Streaks of light filled every direction. A dazzling cluster of radiance, bright enough to blind anyone watching, accompanied the nonstop thunder of explosions.

The most overwhelming sight was a single saber scattering black-red qi.

Boom!

Powerful saber force swung through the air, leaving behind a pale trail of light.

Its destructive trajectory erased everything that stood in its path, and the attacks flying toward the Blood Lord were helplessly knocked aside.

Mine, of course, was among them.

Boom!

The spearhead of White Flame rang sharply. The shaft I gripped with all my strength vibrated violently in my palm.

Even though I had poured an enormous amount of internal energy into it, the force was unbelievable.

It was difficult to believe it belonged to a human being.

*What a monster.*

I gritted my teeth and twisted my body around.

Whoosh!

The black-red blade passed within a hair’s breadth of my head, slicing off a few strands of hair.

But the skin that could not withstand the wind pressure split slightly, and blood began to flow.

I caught the droplets running down the bridge of my nose and swallowed them before swinging my spear.

“Hah!”

Whirrrrrl!

The violently spinning spearhead aimed for the Blood Lord’s chest.

Perhaps because I had poured in all the Points I had received as the reward for winning the Star-Array Grand Banquet, my movement and strength had risen another level.

But then—

Crack!

The Blood Lord’s free hand snatched the spearhead out of the air.

It was a bare hand, but not truly bare. Immense internal energy blazing black and red enveloped his palm.

“This won’t do.”

Along with his low voice, tremendous force pulled the spearhead toward him.

Then the Blood Lord’s eyebrows shot upward.

The spearhead that had been caught in his grip only a moment ago had vanished.

It was as if it had never existed in the first place.

“You—!”

Before his startled voice could escape, I had already plunged deep into his reach.

*Inventory Open. Summon.*

In the space of an instant, White Flame—heated by Scorching Yang Qi—was back in my hand.

Ten-Thousand-Year Cold Iron, harder and sharper than anything else in the world, tore through his Body-Protecting Qi and pierced the flesh concealed beneath it.

Thud! Boom!

The Blood Lord shook his sleeve, and a powerful penetrating force slammed into my abdomen.

After being driven back ten steps in a row, I saw the Blood Lord’s wide-eyed face—and the fountain of blood erupting from his chest.

*I did it.*

It was an attack only I could have pulled off—and one that had worked because I was nothing more than me.

It had landed because I used the System, which no one could have anticipated, and because the Blood Lord had not considered an attack from someone like me worth guarding against.

*This is my chance.*

This was perhaps the perfect opportunity that would never come again. The last lifeline I could not afford to let go.

I swallowed the blood rising in my throat and shouted.

“Old Master!”

My voice rang across the devastated mountain path. It pierced the air, rode the wind, and reached one man’s ears.

A heated voice slipped between his lips.

“Well done.”

The old man shooting toward the Blood Lord had transformed into the Fire King.

Boom!

An enormous blaze of heat burst from his small body. It burned the air and crushed the wind.

If the Blood Lord’s qi was something so ominous that merely looking at it made one uneasy, then Jeok Cheongang’s was heat itself—as though it could burn the world.

“Fucking hell…”

The Blood Lord muttered the words like a groan.

But it was already too late. He did not know, but I did. I knew what Jeok Cheongang was doing and what kind of power that technique possessed.

He had used it only once before, becoming a legend by killing a thousand members of the Demonic Cult.

*Dance of the Fire God and Demon.*

At that moment, Jeok Cheongang’s figure vanished.

He approached the Blood Lord on light footsteps, as though dancing, while his hands and feet blurred like mist.

Red and blue fire qi filled the entire area. It was a beautiful flash of light, but terrifyingly destructive.

“Fire King!”

Whoosh!

At the Blood Lord’s rough shout, black-red saber force mingled with the fire qi. A thunderous roar rang out, as though cliffs were collapsing and the sky itself were being torn apart.

*This is…*

It was an exchange of attacks that was difficult even to follow with my eyes. It lasted for less time than could be called a moment, but I still understood.

Hundreds of attacks carrying tremendous power had passed between them in that brief instant.

And I knew who had won.

Boom!

A wave of heat swallowed the black-red saber force. Something flashing shot into the sky and plunged deep into the churned-up earth.

A saber.

The man who should have been holding it was receiving the final blow.

“This old man told you, didn’t he? Even if you were a demon god instead of a human, I would kill you.”

Along with his quiet voice, a palm struck the Blood Lord’s chest.

Sizzle.

His flesh burned, and his breastbone collapsed. After vomiting a mouthful of blood, the Blood Lord fell to his knees with a hazy look in his eyes.

And that was it.

Jeok Cheongang stared down at the Blood Lord’s motionless crown before his figure began to stagger.

“Old Master!”

“Grandpa Jeok!”

Cheongpung and I hurried over, supported Jeok Cheongang, and moved him to a nearby patch of grass that was still more or less intact.

The Dance of the Fire God and Demon.

There was no flame that burned forever. When the dance ended, the fire went out and the heat faded.

That was why Jeok Cheongang, who had lived through an age-spanning lifetime, had only been able to use it once.

“How was it? Wasn’t it exactly as this old man told you?”

“What are you talking about?”

“The Dance of the Fire God and Demon. Wasn’t it incredible?”

At Jeok Cheongang’s faint smile, I let out a sigh of relief.

Then I smiled along with him.

“It was incredible.”

I meant it. Everything about it had been incredible.

If not for the voice that came from behind us the next moment.

“The Dance of the Fire God and Demon… That’s one cool name.”

We slowly turned our heads.

Our eyes filled with the sight of the Blood Lord standing up as if nothing had happened.

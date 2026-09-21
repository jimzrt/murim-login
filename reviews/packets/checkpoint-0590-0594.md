# Checkpoint Review — 590–594

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

# Chapters 590–594

## Plot

Jin Taekyung tears through Ares Guild headquarters, incapacitating its defenders and forcing Song Cheonwoo’s faction and other executives into open revolt. Go Se-won reveals that Go Jun is hiding in the concealed Area A. Jin spares Se-won after learning that Go Jun, rather than Se-won’s own choices, made him believe he was abandoning his family.

Go Jun remains in Area A to face Jin. He remembers how Lee Jungryong found him among the war orphans and made him his Disciple, while the black jewel in his treasured necklace mysteriously allows Jin to breach Area A’s barriers. Their battle reveals that Go Jun has absorbed multiple S-grade Magic Gems and gained immense power, including corrupted demonic energy, an Aura Blade, and extraordinary regeneration. When Go Jun threatens Jin’s family and allies, Jin commits fully to killing him.

Jin uses White Flame, the Flame-Extinguishing Divine Fist, Striking Second, Hitting First, and Fire Dragon Armor to overcome Go Jun’s attacks and pierce his chest. Go Jun regenerates anyway, mutating into a grotesque hybrid with Troll-like recovery. Jin exhausts the mutation’s regenerative power, decapitates him, and finally receives the System’s kill chime. The confirmed revenge leaves Jin hollow rather than relieved.

## Continuity

- Jin Taekyung has destroyed Ares Guild’s headquarters defenses, triggered an internal revolt, and killed Go Jun in concealed Area A. Go Jun’s final death was confirmed by the System.
- Go Jun was Lee Jungryong’s Disciple and direct protégé. He absorbed multiple S-grade Magic Gems, including power from a powerful Troll, and mutated into a hybrid monster with unstable regeneration.
- Go Se-won remains alive. He opposed Go Jun’s crimes, revealed Area A, and has a pregnant wife and a four-year-old child.
- The black jewel in Go Jun’s necklace emitted strange light and disrupted Area A’s barriers, but its nature and purpose remain unknown.
- Cheon Taemin collapsed more than twenty years ago and remains unconscious at an unknown location. Area A is still only a suspected connection; what it contains and how it relates to Taemin remain unresolved.
- The unidentified being involved in Go Jun’s plan, the object Song Cheonwoo carried, and the darkness and light released by that object remain unexplained.
- Kim Hwajong is dead after restraining Behemoth, and Choi Minwoo remains unconscious. Behemoth’s Turbid Abyss still requires purification before use.

## Translation Decisions

- Use **Area A**, **White Flame**, **Flamefire Path**, **Tower Shield**, **hellfire**, **Scorching Yang Qi**, **Force**, **Sword Energy**, and **Aura** according to the established distinctions.
- Use **Aura Blade**, **Flame Divine Palm**, **Flame-Extinguishing Divine Fist**, **Fire Dragon Armor**, **Striking Second, Hitting First**, and **Troll-like regeneration**.
- Render 마력 as **demonic energy**, distinct from **mana** and **Magic**.
- Retain **Mutation**, **Named Monster**, **Skeleton King**, **Young Master**, **Internal Energy Depletion**, and **Supreme Peak Magic Gem**.
- Preserve Jin’s profane, accusatory voice, his deliberate protection of Se-won, and the emotional emptiness following Go Jun’s confirmed death.

## Durable state

{
  "active_continuity": [
    "Kim Hwajong died after sacrificing himself to restrain Behemoth, and Choi Minwoo remains unconscious after being transported from the battlefield.",
    "Behemoth's Turbid Abyss is a Supreme Peak Magic Gem that absorbed another source of mana and requires purification before use.",
    "Jin has devastated Ares Guild headquarters, incapacitated its elite defenders, triggered an internal revolt, and entered concealed Area A while pursuing Go Jun.",
    "Go Jun was Lee Jungryong's Disciple and direct protégé; Lee found him among the war orphans and recognized him as special.",
    "Go Jun absorbed multiple S-grade Magic Gems, including one from a powerful Troll, and transformed into a grotesque hybrid monster with unstable regenerative power.",
    "Go Se-won openly opposed Go Jun's crimes, intended to resign, revealed Area A, and has a pregnant wife and a four-year-old child.",
    "Cheon Taemin collapsed more than twenty years ago and remains unconscious at an unknown location, with Area A only suspected.",
    "Song Cheonwoo and Lee Jungryong concealed Taemin's condition and purged those who knew the truth.",
    "Busan's Kraken is dead, but more than one thousand Mermen remain across Haeundae and Gwangalli.",
    "Go Jun seized Song Cheonwoo's children, used S-grade Magic Gems to cause the Busan Monster Wave, and targeted Choi Minwoo.",
    "Song Cheonwoo was killed by an unidentified monster after falling into an abyss; the object in his pocket released darkness that became light.",
    "Jin Taekyung ultimately killed and decapitated the mutated Go Jun in Area A, and the System confirmed his final death."
  ],
  "continuity_sources": [
    594
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What is inside Area A, and what is the unidentified being involved in Go Jun's plan?",
    "What was the object Song Cheonwoo kept in his pocket, and what did its release of darkness and light accomplish?",
    "What is the black jewel in Go Jun's necklace, and what function does it serve?"
  ],
  "safe_through": 594,
  "temporary_decisions": [
    "Use Area A for A구역, White Flame for 백염, Flamefire Path for 염화일로, Tower Shield for 타워 실드, and hellfire for 겁화.",
    "Use Scorching Yang Qi for 열양지기 and Force for 강기; distinguish Sword Energy from Aura when the source contrasts them, and use Aura Blade for 오러 블레이드.",
    "Use Seizing an Object Through Empty Space for 허공섭물, Flame Divine Palm for 화염신장, Finger Qi for 지풍, and grappling technique for 금나수.",
    "Use hunting dog for 사냥개 and impregnable fortress for 철옹성.",
    "Use Executive Director for 전무 and Managing Director for 상무 in Ares Guild's executive hierarchy; render 마력 as demonic energy, and use Troll for 트롤, Mutation for 변이, and Named Monster for 네임드 몬스터."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 590

# Chapter 590

Everything began and ended in an instant.

Fwoosh.

Flame-Extinguishing Divine Fist. True to its name, its overwhelming heat transformed into blue-white flames and surged upward.

Kuwaaaaaang!

The tremendous roar that erupted the next moment swallowed every other sound.

Layer after layer of powerful defensive Magic—and even the ceiling, made from exceptionally durable magical materials—collapsed and melted beneath the extreme heat.

Boom! Boom! KABOOM!

One, three, five. Ten.

Whenever one ceiling disappeared, another appeared, and then yet another ceiling blocked my path.

But I surged upward as a pillar of fire, smashing, piercing, and melting everything that stood in my way.

Boom. Crackle.

How high had I risen? How many ceilings had I destroyed?

At last, when my body came to a stop, beyond the wavering flames…

“Fire!”

There were people waiting for me—no, enemies who had finished making every possible preparation.

Screeeeech!

As if they had been waiting for this moment alone, the enemies fired arrows, Magic, and everything else at once.

And at the moment countless rays of light shot toward me, I muttered a command in my mind that no one could hear.

*Inventory. Store.*

Swish.

The cool sensation of the spear shaft disappeared from my grip. I gathered the flames that had not yet died down into both hands and thrust out my palms.

*Flame Divine Palm.*

Fwoosh. Whoooooosh!

Flame Divine Palm at eight-tenths mastery. A fire dragon burst from both palms and writhed through the air.

Terrible heat swept through the wide corridor stretching out on either side. Magic, arrows, and even people were caught in it.

“Graaaaaaaaaah!”

“Healer! Healeeer!”

What remained where the flames subsided was screaming and foul stench. The smell of flesh roasting and cries of agony overflowed from every direction.

If I had used my full strength, more than half of them would have burned to death without even managing to scream.

“H-How could this…?”

I turned my head toward the voice.

At the end of the corridor, a dozen or so healers stood with their mouths hanging open, staring at the scene before them.

“What are you doing? Run your asses over here and save your comrades.”

At my flat remark, a middle-aged woman who looked like a Team Leader bit her lip.

“Mr. Jin Taekyung, why on earth are you…?”

“Because there’s something I absolutely have to do. And because you people got in my way.”

“I don’t know what your circumstances are, but still… This is too much, isn’t it?”

When I met her eyes, filled with fear and anger, I felt like the worst bastard in the world. Maybe that was why a hollow laugh escaped me.

The Ares Guild emblem sewn into their clothes irritated me, and their shameless behavior was absurd.

That was precisely why I stopped instead of simply walking away.

“Too much? Fuck, you’re the ones who went too far.”

“W-What?”

“I don’t think people who came swarming over to kill me over those words—Code Red—have any right to say that.”

“……”

“I said meeting one person would be enough. I even tried to avoid an unnecessary fight. But you were the ones who attacked first, and you’re the ones who went down.”

I understood. They had no direct connection to Kim Hwajong’s death. How could the hands and feet know what the head had planned?

But the fact that an order had been given did not erase what they had done. They had gathered at an order to kill one person.

“Why are you doing this? I don’t know what your circumstances are, but…”

Above the low groans, a quiet voice slipped between my lips and echoed through the blackened corridor.

“Don’t spout bullshit. You should’ve thought about it before asking. Why did that bastard Jin Taekyung suddenly start acting like this? Why did a guy everyone praised for saving people and killing monsters come to our Guild and cause a scene, demanding that we bring out Go Jun? And why was an order given to kill him?”

These days, people called me a hero.

To give them the conclusion first: I wasn’t.

I lacked any noble spirit of self-sacrifice. I cared about money. And rather than living for strangers I had never met, I wanted to live for my own people.

But… at the same time, I thought I had lived without shame.

After gaining this power far beyond my station, I believed I had used it for other people whenever possible.

What kind of person was I? Was this choice right? I questioned myself again and again.

“Then why? Why? Why?”

I kept throwing out those empty questions. The vacant faces in my view disgusted and repulsed me.

“When you’re told to kill a person, why did you come here without even questioning the order?”

No one answered, but I already knew the answer myself.

Because they were nothing more than fingernails—not even Go Jun’s hands and feet. Because they were dogs living off the food Go Jun and Ares Guild gave them.

They could gain more wealth and honor by carrying out their mission. That was why, just as they had always done, they had stood in my way.

“Do you even have any idea what that bastard Go Jun has done? What if the Monster Waves in Busan and Pyeongchang were artificially caused by him?”

The moment I finished speaking, shouts erupted from every direction.

“Bullshit!”

“That’s impossible!”

Right. I knew they would react like this. That was why I had come all the way here.

Looking at their distrustful expressions, I let out a hearty laugh.

It was fascinating. They remained silent about why a man called a hero had invaded Ares Guild, yet when it came to other matters, they immediately denied everything.

“What did the higher-ups promise you in exchange for taking me down? A lightning-fast promotion within the Guild? Enough wealth to feed several generations?”

“……”

“Please, don’t give me bullshit about not having enough money to raise your kids or needing to support your widowed mother. You’re not starving right now.”

Every person here had succeeded in life. Whether they had wanted it or not, they had awakened one day and displayed enough skill to enter Ares Guild.

I had no intention of blaming them for the wealth and honor they had gained. I had once dreamed of that kind of life myself.

But the reason their choices disgusted me today was… that they had made the wrong choice to gain more, then tried to justify themselves.

That was how a group made up of individuals who had remained silent learned to fall silent as one. That was how they became the defenders of Ares, an impregnable fortress.

“So.”

I drew a deep breath. Mental exhaustion, anger, disgust, and countless other emotions churned in my chest.

“Stop spouting this fucking nonsense and lie down. Suck down your potions and get healed while you think about it. *Today is my second birthday.* Think of it that way.”

“……”

“……”

Silence filled every direction. Even the groans that had constantly seeped through the corridor could no longer be heard.

Those still standing and those lying on the ground alike either closed their eyes or firmly shut their mouths.

Ignoring their trembling gazes, I started walking. I didn’t leave out one final greeting.

“Fucking morons.”

I had no interest in whether they realized something after hearing my words or whether they still possessed the mentality of hunting dogs. My only target was one person.

And to reach that fucking bastard who still had not shown himself… there were plenty of obstacles left to break through.

Step.

My foot landed on neatly trimmed grass.

The world was still in the middle of a bitterly cold winter, but after passing through the corridor, the garden spread out at its center was a lush spring.

I had no idea what floor this was. Hundreds of flowers bloomed in profusion, and a smaller number of enemies waited for me among them.

“A lot of you gathered. You fucking bastards.”

Swish!

Instead of an answer to my greeting, an arrow packed with mana flew back at me.

Judging by how precisely it aimed for my eye, the archer who had fired it was a mean bastard. And considering the amount of mana infused into it, there was no doubt he had fired to kill.

So in this case, returning what I had received was the right thing to do.

At least, that was my way.

Clack. Swish!

I caught the arrow in my hand and flung it away in the same motion.

The arrowhead flashed as it returned to its owner twice as fast and twice as powerfully as when it had first been fired.

Kang!

A white blade trembled with a sharp metallic ring.

A middle-aged man in his fifties stared at me with deeply sunken eyes. He had deflected the arrow with an enormous greatsword.

His seasoned bearing and aura, which had reached the far edge of Peak, reminded me of a Murim martial artist.

“You’re as hot-tempered as I heard, junior.”

“It’s nice to meet you, Senior.”

With the polite attitude of a junior, I cracked my knuckles.

Crack.

The hardened joints, caked with dried blood, gave a sound like bones shifting out of place.

“If you withdraw now, I’ll pass through quietly. Ah, except for the bastard who fired that arrow.”

Slap!

The instant I finished speaking, one man’s head snapped to the side.

The middle-aged man slapped the archer on his right across the face with lightning speed, then looked at me.

“He’s still young and stupid. I ask for your leniency.”

“That wasn’t a mistake. I’ll have to break his wrist.”

“That much should be more than enough to be grateful for. Surviving is what matters.”

*What was with this guy?*

He was different from the Ares Guild members I had fought so far. As I stared at him suspiciously, the middle-aged man continued in a calm voice.

“Your offer is appreciated, but I’m afraid I have to decline. Even if I don’t look it, I’m a Guild executive. I have to cling to your trouser leg and hang on.”

“You won’t see a pretty sight.”

“What can I do? I’m a hunting dog too, in the end. Given the situation, the result is obvious, but I’d appreciate it if you went easy on me.”

What was it about his attitude?

I silently studied the middle-aged man. Then I suddenly arrived at a conclusion and opened my mouth.

“Song Cheonwoo. No—you’re with Director Song’s faction.”

The middle-aged man’s eyes widened at my words.

That meant I was right.

And it also meant I had no reason to fight them.

Song Cheonwoo had led his own faction within Ares Guild and openly opposed Go Jun. The middle-aged man in front of me must have shared his convictions.

“You… knew?”

“I heard it from someone close to him. There’s no need for us to fight, so step aside.”

The middle-aged man let out a hollow laugh.

“The enemy of my enemy is my ally?”

“At least for now, I don’t want to waste my strength or time.”

Step.

The instant I started walking again, the middle-aged man raised his greatsword diagonally.

It was an unmistakable stance preparing to attack. His troubled voice reached my ears.

“Stop. I don’t want to do this either, but I have no choice.”

I answered without stopping.

“If you don’t want to do this, why are you here? Because you’re just a hunting dog who can do nothing but obey orders?”

“……”

“If you’re afraid of Go Jun, then say you’re afraid. Don’t cover it up by saying you have no choice.”

It wasn’t only the middle-aged man. Everyone looking at me had trembling eyes.

As I continued forward without caring, the more than one hundred people in front of me also began backing away.

An invisible crack appeared across the middle-aged man’s calm expression.

“The tide has already turned. I heard Director Song returned to the United Kingdom this morning. What do you think that means? I had to find some way to survive. Even if it meant becoming a hunting dog.”

Song Cheonwoo had gone to the United Kingdom that morning? It was obviously a lie.

Certain that Go Jun had put forward a stand-in, I let out a quiet snort of laughter.

“What if that hunting dog’s master dies today?”

“……”

Everyone’s eyes opened wide.

I stretched a hand toward the empty air. At the same time, White Flame, summoned from my Inventory, slashed down diagonally.

Swish!

A single line cut across the air.

Everyone sucked in a breath, but no blood sprayed out, and no one died.

The Force shot along the white spearhead had cut something that was not human.

Slice. Crash!

The enormous stone statue standing atop the ornate fountain at the center of the garden broke into pieces and collapsed.

The remains of a statue modeled after a man who was already dead crushed the flowers beneath it.

Its head, severed from the body, rolled and rolled until it reached my feet.

The statue was too lifelike to be called a mere stone figure, and I recognized the face without difficulty.

*Lee Jungryong.*

That was right.

Today, this magnificent palace built by an ambitious warlord who had wanted to possess everything would collapse.

Along with his disciple, who had become a monster.

I tossed out a single remark toward the dumbstruck people.

“There are two choices. Put down your weapons and clear a path, or watch my back.”

“……”
## Chapter artifact 591

# Chapter 591

Beep. Beep. Beep.

The ringing continued for a long while through the smartphone before abruptly cutting off.

At the same time, instead of the voice he had been waiting for, a familiar yet still strange female voice slipped into his ear.

“Your call cannot be connected. After the beep, you will be connected to voicemail…”

Under normal circumstances, he would have hung up. No—he would never have called in the first place.

But the middle-aged man had a vague suspicion. The voice he was about to record might become the last words he left for his family.

Beeeeeeep.

The tone began, but his lips refused to move.

What was he supposed to say? To his wife, who was carrying their second child, and his child, who had only just turned four?

And just as the middle-aged man—Go Se-won—was finally about to speak after much thought…

Rumble…

A faint vibration shook the entire building. At the same time, the voice of a security-team member waiting outside seeped through the crack in the door.

“Team Leader, I think you need to come out.”

“……”

“Team Leader?”

“Wait. I’m coming.”

With that brief reply, Go Se-won ended the call.

*Yes. Maybe this is a sign from someone. A sign telling me to stay alive and meet my family again.*

*If it isn’t…*

*Then I suppose I don’t even deserve to leave a will.*

Go Se-won muttered bitterly to himself before opening the door. A security-team member with a hard, expressionless, familiar face was waiting for him.

“I’m sorry. It’s just that something happened outside…”

“I know. Let’s go.”

Go Se-won calmly cut him off and started walking. After crossing the unlit corridor, he soon saw it.

A massive circular hall worthy of the top floor, and more than a hundred fully armed elite Guild members.

And…

A holographic image filling the hall.

*BOOM!*

A flash erupted with a deafening explosion.

*Fwoooooosh!*

Rays of light surged from both formations and shot toward each other.

“Graaaaaah!”

“Tanks! Reorganize the formation!”

Screams and shouts erupted everywhere. Hundreds of Hunters tangled with one another in a scene so vivid that it seemed to be happening right in front of them.

Only a few minutes ago, they had belonged to the same Guild.

Now they were fighting as enemies.

*That’s…*

Go Se-won watched the fierce battle in the hologram with deeply sunken eyes.

The familiar faces fighting at the very front were Guild executives from the faction led by Song Cheonwoo.

*An anti-Ares faction… So this is how it ends.*

A body without a head was bound to collapse.

But not this time.

Song Cheonwoo, the head, had been removed, but an even more powerful head had grown from the severed neck.

That was why a body sentenced to death had been able to rise again.

In the hologram, a young man walked forward covered in the blood of humans and monsters. He was the new focal point of those people.

“A monster…”

Someone staring at the hologram muttered the word like a groan.

At that moment, hellfire blazed around the young man—Jin Taekyung.

*Fwoosh! KABOOOOOM!*

A single streak of flame scorched everything in its path as it tore across the space.

Large, sturdy Tower Shields shattered into pieces. Dozens of tanks who had stood firm as an iron wall were sent flying all at once, and the balance that had held steady collapsed in an instant.

“Graaaaaah!”

“Now! Hit them!”

Amid surging blood and falling bodies, the flames that had incapacitated an entire raid team in one blow continued to shoot forward without stopping.

*Screeeeeech!*

They were flames that could not be extinguished and a meteor that could not be stopped.

The ceiling that was supposedly capable of withstanding bombardment collapsed like a line of dominoes, and the forces waiting on each floor fell like bundles of straw.

Whenever the holographic image shook because it could not keep up with the speed of the moving flames, he was already on another floor, cutting down a new group of enemies.

“St-Stop him…!”

*KABOOOOOM!*

Overwhelming force that nothing could block.

Jin Taekyung had become a single streak of flame, shooting forward without obstruction.

As the troops waiting on each floor collapsed helplessly, the Guild executives from Song Cheonwoo’s faction—who had remained uncertain and unable to make a decision—finally turned their weapons around.

“W-We’re on the eighty-fifth floor! Managing Director Kim Jong-pil and Team Thirteen have betrayed us. Gah!”

“Headquarters, respond! There’s a revolt on the ninety-seventh floor…!”

*Fwoosh! Boom!*

When a current grows stronger, it becomes a wave. The farther a snowball rolls, the larger it becomes.

That was exactly what was happening now.

The flames that had burned fiercely in one direction had broken free and were spreading everywhere.

And Go Se-won knew.

The flame called Jin Taekyung would not go out until his anger had settled—until it had finally swallowed one person whole.

“The target has broken through the hundredth floor!”

“Engagements are taking place simultaneously across twelve floors! Dangerous elements have joined the target and are engaging our forces!”

“The target is moving alone! He’s on the 103rd floor! No—he’s entered the 104th!”

Urgent shouts rained down from every direction. When they had first been summoned to the top floor, the executives had worn relaxed expressions. Now, their faces were colored with anxiety.

“H-Hey, Team Leader Go. May I ask you something?”

Go Se-won answered without taking his eyes off the hologram.

“Go ahead, Executive Director Choi.”

“I’ve been wondering about this for a while…”

The man’s throat bobbed.

Executive Director Choi, whose hair was half gray, swallowed dryly before opening his mouth on behalf of everyone present.

“Where… where on earth is the Vice Guild Master?”

Go Se-won suddenly turned his head and looked around.

Among the nearly one hundred people gathered there, the face of the one man who should have been fighting at the very front was nowhere to be seen.

Yet contrary to the bleak reality, Go Se-won’s heart felt lighter.

*Yes. This should be enough.*

When he was told to fetch, he fetched. When he was told to bark, he barked.

He had been one of the countless war orphans born from the Great Cataclysm. The reason he had risen to his current position was that he had lived as a faithful hunting dog.

Ironically, that fact made him disgusted with himself.

*With this, I’ve repaid every debt I owed you. Whether I live or die from now on has nothing to do with you anymore.*

Go Se-won muttered those words in his heart toward the person who still refused to appear, then firmly drew his sword.

*Shing.*

His calm voice mingled with the sharp metallic sound.

“The Vice Guild Master… He isn’t coming.”

“W-What did you say?”

“So if you want to live, fight. You’ve consumed so much food from him that there’s no way you can vomit it all back up now.”

Everyone in that room was a hunting dog.

They had accepted the food their master gave them and enjoyed lives of prosperity. They had no choices left.

*Yes. I’m the same.*

A hollow laugh escaped Go Se-won.

The executives opened their eyes wide at the sight.

Then a scream rang through the enormous hall.

“The 119th floor! The target has broken through the 119th floor!”

“……!”

“……!”

There was no one who failed to understand what those words meant.

At the very least, everyone knew that the skyscraper where they reported to work every day was made up of 120 floors.

*He’s coming.*

An unavoidable battle.

Wearing full-body armor, Go Se-won held a sword in one hand and a spear in the other as he opened his mouth with a heavy heart.

“Formation. Prepare for battle.”

His quiet voice reached the ears of a hundred people.

At that moment—

Rumble! KABOOM!

With a deafening roar accompanied by a tremendous vibration, one of the world’s most famous skyscrapers shook.

An uninvited guest had set foot on the top floor of an impregnable fortress that no one had ever been able—or willing—to challenge.

*Step.*

A lone silhouette appeared through the rising cloud of dust.

Go Se-won felt every hair on his body stand on end. With all his strength, he hurled the spear in his hand.

*Whoosh! Screeeeeech!*

* * *

*Slice!*

A spear rushing toward me split apart along with the cloud of dust.

Beyond the view cleared by the path of White Flame, I caught sight of a middle-aged man’s face that seemed strangely familiar.

*Where have I seen him before?*

As the question crossed my mind, a recent memory surfaced.

At Lee Jungryong’s national funeral, there had been a new Head of Security standing beside Go Jun like a shadow.

That was the identity of the middle-aged man.

The name I had heard in passing back then was probably…

“Go Se-won.”

At my quiet call, the middle-aged man’s—Go Se-won’s—eyes trembled faintly.

I didn’t know whether it was because I knew his name or because I had deflected his earlier attack so easily.

What I did know was that I had finally found someone who could give me a proper answer to my question.

I asked the same question I had thrown out dozens of times since entering the lobby.

“Where is Go Jun?”

Before I had even finished speaking, a flash of light shot from Go Se-won’s hand.

*Whoosh! KABOOM!*

The thrown spear missed me by a hair and embedded itself in the floor, creating a small crater.

That was the signal.

*Fwish-fwish-fwish!*

Go Se-won wasn’t the only one waiting for me on the final top floor.

More than a hundred Ares Guild members filled the enormous hall. Every one of them was skilled enough to be called a high-level Hunter, and they unleashed their attacks all at once.

*Fwoosh!*

Massive qi churned.

The hall filled with blue, red, and brilliant light.

Faced with an attack whose power and dense barrage could not even be compared to anything I had encountered so far, I stepped forward alone.

*Step.*

The instant my foot, charged with internal energy, touched the ground, flames rose and heated the air.

*Flamefire Path.*

*Fwoosh! Screeeeeech!*

A single step was enough.

After erasing a dozen meters of space, I swung a palm strike into the air.

Arrows melted before the blue-white hellfire, and every spell flying through the air was dispelled.

*BOOM!*

Water, earth, wind, and flame.

The superheated air summoned by Scorching Yang Qi ignored even elemental affinities.

As the attack Magic made up of the four elements exploded outward in every direction, the tanks at the front swiftly raised their Tower Shields.

*KABOOM!*

Despite the tremendous impact, they did not shake even an inch.

The Tower Shields tilted diagonally after blocking the aftermath of the Magic without suffering the slightest damage.

At the same time, nearly twenty figures surged upward, using the steel wall as a set of stairs.

*Pat-pat-pat!*

I realized it instinctively.

Everyone gathered here was an elite capable of being classified among Ares Guild’s best.

But these people rushing toward me were on another level.

*Killing intent.*

Their movements were concise and swift. A practiced killer’s scent wafted from their calm, emotionless eyes.

More than twenty weapons stabbed and slashed at the speed of light, flashing brightly.

*Screeeeeech!*

Faced with the fierce wind shooting toward my entire body, I couldn’t help letting out a quiet laugh.

“What a load of bullshit. You fucking morons.”

“……!”

In the slowed world, I could see astonishment rise over their emotionless faces.

But it was already too late to turn back.

For them and for me.

*Slice!*

The moment blue-white Force extended along White Flame’s spearhead, the incoming weapons lost their strength and the bodies attached to them split apart to either side.

With a single strike, I demonstrated the magic of turning five bodies into ten.

Then I thrust my fist toward the empty air.

*BOOM!*

What burst apart was not merely compressed air.

As an assassin who had been approaching stealthily tilted over as a headless corpse, the chain sickle in his hand was already moving according to my Will.

*Whoosh! Thud!*

Wielded by *Seizing an Object Through Empty Space*, the chain sickle embedded itself in someone’s neck.

The calm eyes widened at the sudden arrival of death.

At that moment, I planted my palm against his chest as he began to fall.

*BOOM!*

The palm force of *Flame Divine Palm* was not aimed at confirming the kill.

It was aimed at another enemy who had tried to use his already-dead comrade as a shield while thrusting his spear.

“Graaaaaah!”

Blood burst from his seven apertures with his scream.

Before the man whose heart meridians had been severed throughout his body could even lower his head, I was already moving toward another enemy.

*Crack!*

My extended fist crushed his head.

*Fwish! Fwoosh!*

The Finger Qi I fired at high speed pierced his neck and chest.

He dropped his weapon and tried to block the neck from which blood was gushing, but it was useless.

“Ghk. Guh…”

The light rapidly faded from his eyes.

I watched the last enemy collapse limply with a cold gaze.

*You brought this on yourselves.*

If it had been any other day, I might have left them alive.

But today—right now—was different.

Just as when Uncle Kkeokjeong had been attacked by the Black Hunters, I had no intention of stopping.

I couldn’t stop.

*I have to show them here. So the same thing never happens again.*

I had been a Hunter long before I became a martial artist of the Murim.

I had also been a modern man born in the twenty-first century, someone who had lived in a civilized society where reason and the law existed.

That was why I had been unable to eliminate Go Jun in Sichuan.

Unlike Lee Jungryong, whom I had been able to eliminate amid chaos and destruction, Go Jun had been protected by a fence built from the two-syllable Korean term for the rule of law.

But now…

None of it mattered anymore.

Go Jun had survived because of my choice, then crossed a river from which he could never return.

And I—or rather, we—had lost Kim Hwajong.

I would never again see the silver-haired old butler who had always spoken to me with a polite, gentle smile.

That was why I had come here.

Why I had torn down the fence called the rule of law and made myself an outlaw.

*Splash.*

My footsteps, soaked in blood, rang unusually loudly.

The enormous hall had fallen into suffocating silence.

The people frozen by the slaughter that had taken place before their eyes.

But the face I was looking for was nowhere to be seen.

Neither was the only person who could give me the most certain answer to my question.

*Go Se-won.*

I turned my head to search for Go Jun’s right hand.

At that moment, a faint and stealthy sound of something cutting through the air reached my senses.

*Whoosh!*

I turned around and slammed my hands together as though in prayer.

*KABOOM!*

The razor-sharp blade caught between my hands stopped just above my forehead.

The owner of the sword, Go Se-won, spoke in a calm voice.

“Were you looking for me?”

“Yes.”

As I answered, I tightened my grip with both hands.

At the same time, the Sword Energy—or rather, Aura—formed from tremendous mana yielded before the blue-white Force.

The sword blade, unable to withstand my overwhelming internal energy, glowed red and melted.

*Drip, drip. Hiss!*

The metal that had once been called a sword fell to the ground.

I thrust out the hand that held a tremendous amount of heat.

*BOOM!*

A single palm strike was enough.

Layered defensive Magic shattered, and his armor broke apart.

But despite the impact shaking his insides, Go Se-won did not fall.

He swallowed the blood surging up his throat and grabbed my shoulder with his gauntlet.

No—he tried to grab it.

*Tap-tap-tap! BOOM!*

A flowing grappling technique followed seamlessly.

Then, as heat erupted once more, Go Se-won staggered backward and thrust out his hand.

*Fwish!*

A blade shot out between the gauntlet’s plates and grazed my chin.

I felt a stinging pain, grabbed his wrist, and twisted.

*Crack! KRAK!*

Under a grip far beyond human limits, the gauntlet shattered.

His flesh tore, and stark white bone thrust out.

It must have been agonizing beyond anything he had imagined, but Go Se-won did not scream.

His face had gone pale as he casually spoke one word.

“Is it over?”

“No. Not yet.”

I answered without hesitation and grabbed his other arm.

*KRAK!*

“Hk…”

He sucked in a hollow breath.

In the end, Go Se-won could not endure the pain. Blood seeped between his lips as his trembling voice escaped.

“Take it easy… and finish it.”

“That’s the plan. After I hear where that bastard Go Jun is.”

“What if I can’t tell you because of the confidentiality agreement stipulated in my employment contract?”

I grabbed Go Se-won by the collarbone and answered.

“Then it definitely won’t end with just taking it easy.”

Go Se-won laughed weakly.

“Looks like you couldn’t find him, no matter how much you rummaged around. Naturally.”

Unfortunately, that was true.

Even after beating down the endless stream of hunting dogs and reducing the inside of the building to ruins, he still had not appeared.

If there was one thing I had gained from all the information I had collected so far, it was the identity of the secret area where he was staying.

“Area A. I’m guessing you know where it is.”

*Cough.*

Go Se-won spat out blood and muttered.

“I got unlucky. I was planning to submit my resignation soon.”

“Your tongue’s getting long. Shut up and spill it.”

“It isn’t difficult. But I have one condition.”

“T-Team Leader Go. Surely that crazy bastard isn’t—!”

There was always at least one person who failed to read the situation.

But the nameless executive who stepped forward soon fell silent.

Being oblivious was one thing. Few people could keep talking after taking Finger Qi to the throat.

“Your condition?”

“Yes.”

What Go Se-won said next was something I hadn’t expected, either.

“You… want me to kill you?”

Go Se-won gave a small nod.

Even as pain wracked his body, his eyes remained calm, reflecting my face.

“It’s too late to go back to the way things were. Do it cleanly, here. That’s enough.”

“……”

“I think you understand.”

Breathing heavily, Go Se-won raised a trembling finger and pointed somewhere.

And when I finally learned the identity of Area A, I couldn’t help stopping in surprise.

*Empty air?*

It was difficult to understand at a glance, but the world called such things Magic.

Besides, I had personally experienced things even more dangerous and mysterious than Magic.

*Where is it?*

I stared intently at the empty air for a moment.

Then, from my body drenched in exhaustion, I felt an unfamiliar sensation emerge.

*What is this?*

I couldn’t see it.

But I could feel it.

Another space, surrounded by an enormous and highly concealed energy.

It was hidden so perfectly that it could only be detected by someone who recognized its existence.

Go Se-won had kept his promise.

His lips, turning blue, moved.

“Now… kill me…”

Rumble…

Before he could finish speaking, a vibration sounded from somewhere.

Then, the full-body armor broke apart, and the smartphone slipped from the trouser pocket of the suit beneath it. It rolled across the floor.

*Clunk. Bzzzt.*

The cracked screen lit up with a family photograph beneath the caller name: **Wife**.

A young child and a wife smiling brightly.

And Go Se-won with an impassive expression.

“……”

Silence fell.

Without saying a word, I looked at Go Se-won’s cracked expression, resembling the photograph on the cracked smartphone screen.

I recalled the words with which he had asked me to kill him, and the calm voice that had said it was too late to return.

Then I opened my mouth.

“Let me ask you one thing.”

“……?”

“Why is today your last day at work?”

Go Se-won hesitated before answering with a sigh.

“After working here, I realized it wasn’t suited to me. Especially… my boss is a fucking asshole.”

“Yeah. Got it.”

Did Go Se-won know?

Did he know that his answer had just decided his fate?

I quietly raised my internal energy.

Not toward my fist.

Toward my legs.

“You…”

*KABOOM!*

The rest of his voice was swallowed by the explosion.

I was already surging upward into the distant empty air.

I felt the fierce wind, the sensation of floating as though invisible hands had seized me, and the unknown space that refused entry to anyone without permission.

But…

I was an outlaw.

I didn’t need permission.

*There.*

Everything had a flow.

I took a deep breath and closed my eyes.

At the same time, blue-white Force burst from the spearhead in my hand and tore through the empty air.

*Swoooooosh!*
## Chapter artifact 592

# Chapter 592

Whoooosh.

A red mist rose with his exhaled breath.

It was a long, slow breath—so long and slow that one might mistake him for not breathing at all. It was also a secret technique he had learned from his Master long ago.

*I had been watching you all this time.*

*M-Me?*

Nearly thirty years had passed, but Go Jun could never forget that day.

It was the day he had first found a dream.

He had lost his parents, been abandoned by his relatives, and drifted from one orphanage to another. Then—

*The children who live with you are talented, too. But you’re different. You’re very special.*

The Great Cataclysm had left behind more than death and peace. It had created an enormous number of war orphans, and Go Jun was one of them.

Just one among countless war orphans. If he had remained ordinary, he would have been raised like a chicken trapped in a chicken farm, then released into society.

But after meeting his Master, Lee Jungryong, he had become someone special.

That was the greatest reason he had remained alone in Area A, waiting for someone who would soon come crashing in after everyone else had disappeared.

He could not flee from his Master’s enemy while standing in the very place where his Master had once lived.

“……Jin Taekyung.”

With that chilling voice, Go Jun’s tightly shut eyes slowly opened.

After suppressing the red glow in his eyes, he instinctively reached for his neck.

*Clink.*

His fingers touched the cold surface of metal.

This cheap necklace—whose original owner he did not even know—had gradually become both the keepsake his Master had left him and his most precious possession.

Simply because it was the only thing in that place that had retained its shape after everything else had turned to ash.

*Are you watching, Master?*

Go Jun clenched his fist. Red qi shimmered like heat haze over the skin stretched taut across his prominent veins.

Only two months ago, Jin Taekyung had trampled him mercilessly.

But things were different now.

The reason Go Jun had been able to overcome his fear was the hatred that exceeded it—and the power he had newly acquired.

*I’ll kill him. Today. With these hands.*

Was it a delusion? Or a coincidence?

It was at that very moment that the black jewel set into the necklace emitted a strange light.

*Rumble!*

A tremendous vibration shook the space.

Its meaning was obvious.

This was a place where anyone who had not been granted permission could not even become aware of its existence. Now, at last, it had allowed someone to intrude.

Countless spells and barriers that had never once been broken since their creation were collapsing even now.

“He’s here.”

Go Jun muttered quietly, released his cross-legged position, and slowly rose to his feet. Top-grade magic armor surged up around his body, wrapping around him according to his will.

*Clatter-clatter-clatter!*

The transformation began and ended in an instant.

By the time Go Jun stood firmly on both feet in blackened full-body armor, blue-white flames were flickering like will-o’-the-wisps at the end of the unlit corridor.

No.

They were the glow of someone’s eyes.

“Jin Taekyung……!”

Three syllables, spat out with hatred.

The owner of that name willingly answered Go Jun’s call.

“Yeah. So you were here.”

Unlike the burning glow in his eyes, his voice was cold.

But Go Jun could clearly feel it—the ember hidden inside that voice. The fuse that had refused to burn while waiting for this one moment.

And then—

“Thanks.”

*Fwoosh.*

At last, the flame caught fire. A voice boiling like lava heated the dark corridor.

“For staying here all this time.”

An unprecedented qi pressed down on the space.

*Rrrrmmble!*

There would be no more waiting.

Within the shaking world, two figures transformed into streaks of light and shot across the corridor toward each other.

The instant the blue and red streaks of light collided—

*Whoom, KABOOM!*

A blinding flash and a deafening roar that seemed to split the sky erupted, coloring the entire area.

* * *

The most important thing when facing an enemy was composure. When reason grew clouded, the mind became unsettled, and when the mind became unsettled, the hands and feet lost their coordination.

That was why maintaining composure was the surest way to seize victory.

It was an absolute law that applied in both the modern world and the Murim, and I had always followed it.

But……

“Jin Taekyung.”

The moment I heard the hatred in his voice.

The moment I saw that fucking face clearly beyond the dark corridor.

I realized something.

In the face of anger that reason could not contain, composure was no shield at all.

Once a fire began to burn, it could not be controlled.

“Thanks.”

My eyes grew hot. My heart, which had not wavered even once while breaking through a 120-story skyscraper and around a thousand enemies, began to churn.

I thought of the silver-haired old butler collapsed against a snow-covered rock and continued.

“……For staying here all this time.”

There was not even a drop of falsehood in those words. I was sincerely grateful to Go Jun.

Because he had stayed instead of running, I could end his life with my own hands.

*Rrrrmmble!*

My dantian was half empty from the internal energy I had continuously expended. But that was enough.

A massive wave spread out from me and shook Area A.

At this moment, I could forget both the fatigue accumulated through the endless battles and my limbs, which had grown heavy.

*I’ll kill him.*

With that single thought, I took a step forward.

*Flamefire Path.*

Flames rose from the tips of my feet as I kicked off the ground and surged forward. They drove back the darkness that had conquered the corridor and illuminated the way.

At the far end, a figure was streaking across the corridor as a beam of light.

*Go Jun.*

I saw his red eyes through the gap between his clenched teeth and the helmet pulled low over his head.

The instant light flashed from the waist of the man charging toward me without hesitation, I raised White Flame’s shaft.

*Whoom, KABOOM!*

Amid the deafening roar, two enormous energies of different colors became intertwined.

A tremendous recoil.

A wave of qi that became a blade and slashed in every direction.

Through the weapons pressed against each other, I saw his eyes glowing red. Then his voice pierced my ears.

“You’re not much, are you? Don’t you think?”

“……!”

My eyes widened despite myself.

His feet, which should have been thrown backward, were firmly planted in the ground.

And that was not the only thing I had failed to anticipate.

*Crunch. Crrrunch.*

An unbelievable pressure traveled up White Flame’s shaft. An enormous power, large enough that it would not have been strange for it to explode at any moment, continued to flow out and wrap around the sword blade.

Slowly, but without stopping, it continued to grow in size and crushed White Flame’s shaft.

*What is this?*

This was the first time I had encountered Force this immense—or rather, an Aura Blade of this magnitude.

As I froze with my eyes wide, Go Jun’s eyes filled with delight.

“You should’ve used that stupid head of yours and thought about why I stayed.”

“You……!”

Before I could finish speaking, the Aura Blade wrapped around his sword blade exploded outward, rapidly swelling in size.

*Craaaack, KABOOM!*

A roar that left my ears ringing. A powerful shock that swept through my entire body.

Along with the red flash that filled my vision, I was thrown backward.

Before I could fully feel the fierce wind brushing past my ears, my back struck a wall made of solid marble.

*KRAK!*

The defensive Magic layered around the wall scattered, and the entire surface caved in.

I was embedded in the exact center of the wall, leaving behind a crater large enough for three or four people to stand inside. I blinked.

My vision trembled faintly from the impact to my head. Through it, I saw Go Jun charging toward me with his teeth bared.

“I’ll kill you.”

*Whoooooosh!*

His movement was faster than his words.

A red cluster of light burst forth along the trajectory of the sword as it slashed diagonally down through the empty air.

Then, in the next instant, a crescent-shaped Aura Blade that had crossed dozens of meters came rushing right up to my face.

*Slice! KRAAAAAASH!*

It had been a hair’s breadth.

I instinctively moved my aching body and avoided the attack. As I looked at the space shredded apart by the Aura Blade, I thought:

*What if I had blocked it head-on?*

The answer was not difficult to find.

I was far more exhausted and fatigued than even I realized.

While suppressing two Monster Waves, I had borne the full aftermath of One Annihilation. Then, immediately after entering Ares Guild, I had been forced to fight while carefully regulating my strength so I would not kill most of my opponents.

If I had faced that attack head-on under these circumstances……

The result would not have been good.

“Jin Taekyung. Jin Taekyung. Jin Taekyung.”

Go Jun hummed my name like a tune, then continued with a grin.

“You should see your face. You’re not a hero. You’re just a rat. You’ll die begging and crying for your life.”

I stared blankly at him as he approached in a lighthearted tone. Then, when a certain thought suddenly crossed my mind, I opened my mouth.

“Did you juice yourself up?”

“What?”

“No, wait. In this case, should I call it a Magic Gem instead of drugs?”

“……!”

At that moment, the smile on Go Jun’s lips faded.

I no longer needed to hear his answer. The expression on his face was the answer itself.

“Hah.”

I let out a small, hollow laugh.

The rage that had paralyzed my mind and body for a moment began to fade, and only then was I finally able to see the cold reality in front of me.

“Of course. That’s what happened.”

“Seeing someone in a new light” and “improving by leaps and bounds” were nothing more than four-character idioms.

At least when it came to martial arts.

Martial strength had to be honed through relentless training and actual combat.

Even I, despite using the System, could not become stronger at such an absurd rate. And if the person in question was Go Jun, that was even more impossible.

A person simply could not become this strong in only two months.

So in the end, there had only ever been one answer.

“You juiced up. You really did. You fucking idiot.”

I finally failed to hold back and laughed out loud.

Not because I found it amusing, but because I found it disgusting.

Go Jun had chosen to abandon his humanity and become a monster. He was so pathetic that I could not stop laughing.

“Fuck, I’ve never seen an idiot like you before. You thought you couldn’t possibly face me through any normal means, so you started sucking down Magic Gems? If you were going to do that, you should’ve gone to Magic Johnson instead. That guy would’ve taken good care of you with his magic wand.”

Go Jun had been struck squarely in the sore spot, and his face stiffened. His already-red eyes grew even darker.

“Shut that fucking—”

“Just shut up and listen, you son of a bitch.”

*Thud. Thud.*

As I rose, rubble and pieces of marble tumbled down.

I cracked my stiff neck from side to side, then continued while staring at Go Jun.

“What? You set off a few Monster Waves with an S-grade Magic Gem and got high on the performance? Did watching people die from nothing more than a flick of your finger make you feel like a god? No, sir, you fucking moron. You’re just a monster. Even if I give you the most generous description possible, you’re nothing more than an idiot side character who made a Named Monster his constellation.”

“Shut up!”

“Fuck off. Want me to give it a title, too? *Go Jun Swallows an S-Grade Magic Gem.*”

“Jin Taekyuuung—!”

*Fwoooooosh!*

A gale rose together with a tremendous wave of qi and swept through the area.

But I calmly answered as I watched that unprecedented power swell until it looked ready to burst.

“What, you fucking idiot?”

There had never been any fear.

Instead, faced with the facts that had finally become clear, I no longer had any reason to hesitate.

He was a monster who had crossed the line.

And he had to die by my hand here today.

For the old butler who had fallen into a darkness from which he would never return.

For the people and Hunters who had died in the Monster Waves.

And……

For myself, who was furious at this goddamned reality.

“You have to die.”

The instant I bit out those words with all my sincerity, Go Jun’s blood-red figure blurred.

*Whoooooosh! KABOOM!*

The red Aura Blade stopped above my head.

The tremendous pressure transmitted through White Flame’s spearhead made my wrists throb, and my ankles sank deep into the ground.

But I did not retreat.

At the very least, the power I possessed had been built through countless hours of training and insight, with the good fortune of the System added on top.

“Get lost, you drugged-up bastard.”

*Rrrrmmble!*

I grinned as I looked into Go Jun’s wide-open eyes, then thrust my fist forward with all my strength.

*Wham!*
## Chapter artifact 593

# Chapter 593

*Wham!*

With a dull impact, the punch I threw with all my strength slammed into Go Jun’s chest.

The layered defensive Magic shattered in an instant, and part of his impossibly sturdy full-body armor caved inward. Gritting his teeth, he roared in fury.

“Jin Taekyung!”

An ordinary high-level Hunter or Peak master would have suffered severe Internal Injury from that punch and been rendered unable to fight.

But Go Jun was different. Perhaps because of the Magic Gem, even my Inner-Family Heavy Hand failed to inflict any serious damage on him.

*An S-rank Hunter. And more.*

Whatever the circumstances, he was already a formally recognized S-rank Hunter.

Not only had he learned internal cultivation techniques known in the modern world as mana cultivation techniques, he had also absorbed the energy of an S-grade Magic Gem obtained from a Named Monster. His strength was tremendous.

“Die!”

*Whoooooom! KABOOM!*

The energy, which had gone beyond red and taken on the unmistakable color of blood, burst outward like an explosion.

White Flame’s shaft trembled under the Taishan-like pressure pouring from the enormous Aura Blade.

*I’ve never been pushed back this badly before.*

At this moment, even three jiazi of internal energy and physical abilities beyond the limits of humanity felt insufficient.

Perhaps it was the fatigue that had accumulated without pause throughout the day. Or perhaps the amount of magical power Go Jun had absorbed was simply that immense.

But one thing was certain……

This idiot I was fighting had gained strength far beyond anything I had expected.

*Rrrrrumble. Crack!*

Under the tremendous pressure descending from above, my body and the ground sank together. By the time I was buried in the ground up to my ankles, Go Jun bared his teeth and grinned.

“Starting to get the picture? Hmm? Are you finally beginning to feel like you’re well and truly fucked?”

A low laugh escaped him.

Go Jun was genuinely enjoying himself now. He was delighted by the thought that he could finally avenge his Master.

“From the day my Master died, I killed you every night, over and over again. I lived while waiting for a moment just like this.”

I watched for an opening and answered.

“No wonder I felt like I was being reborn every morning. I thought it was because I kept dreaming about Jungryong dying every night and waking up refreshed.”

*Fwoosh!*

The instant the blood-red energy shook violently, I pulled my deeply buried foot free and kicked upward.

*Boom!*

My toes, swinging like a beam of light, were blocked by his shin with a thunderous crash. Go Jun, who had been about to pour out his anger, let out a hollow laugh.

“It’s too late to struggle now. Since things have come this far, killing every last one of them will be easy.”

“What?”

I blinked, unable to properly understand what he meant. Then Go Jun’s quiet voice pierced my ear.

“You and that goddamned Peace Guild. And your parents and that bitch of a little sister waiting at home… Ah. Your old man was already dead, wasn’t he? Well, it doesn’t really matter. Even if he were still alive, he would’ve died following his son soon enough.”

“……”

“Did you enjoy being called a hero by the world? Did you think you’d all live happily ever after? It was all bullshit. Kim Hwajong, that old man, was only the beginning.”

His sticky, unpleasant breath washed over my face. A cackling laugh followed.

“This time it’s you, then Choi Minwoo. After that, I don’t care who it is. I’ll kill everyone with even the slightest connection to you, one by one. Sweeping them all away with a Monster Wave sounds good, too. What do you think?”

As his voice continued to pour into my ears, I blinked blankly.

*What the fuck is this bastard saying right now……?*

It was strange. The thing standing before me clearly had the appearance of a human being, but the mouth that kept taunting me without pause produced nothing but the barking of a dog.

A monster wearing a human shell stood before me.

*So he’s going to kill them? All my people?*

I suddenly felt nauseated.

I hated Go Jun for being the kind of person who could turn words like these into action. And when I imagined the people who had become indispensable to me lying dead, my mind seemed to go blank.

*Mother. Hayeon. Team Leader Choi. Uncle Kkeokjeong, Song Song, Jin-ho hyung……*

Familiar faces flashed before my eyes one after another. The silver-haired old butler who had met his death on the snow-covered mountain was among them.

*He’s going to kill them all, and he’s asking what I think?*

The next moment, a calm voice escaped between my lips.

“Fine. I understand.”

“What?”

“Go ahead. Just try.”

The smile lingering around Go Jun’s mouth faded. At the same time, I summoned every last bit of strength in my body.

*Grrrrrkk.*

The spear that had been slowly sinking under the terrifying pressure stopped. My knees, which had been bending, stopped in place as well.

At least for this moment, I forgot my fatigue. The muscles throughout my body still throbbed as though they might tear from the lingering aftermath of One Annihilation, but I forgot that pain, too.

The anger layered over my fatigue and pain covered and paralyzed everything else.

Internal energy like molten lava boiled within the Eight Extraordinary Meridians buried deep inside my body and hundreds of acupoints.

A voice as hot as flame flowed from between my parted lips.

“You shouldn’t have said that.”

“……!”

“You shouldn’t have talked about my people that way. At the very least, you shouldn’t have.”

I had suspected it. I knew that Go Jun was the kind of bastard who was capable of doing something like this.

But suspecting it myself and hearing it directly from his mouth were entirely different matters.

“Don’t you agree, you inhuman piece of shit?”

Go Jun was a monster. I did not know whether he had been one from the beginning or whether I had created him, but none of that mattered anymore.

He had to die for my people to live. They had to live for me to live.

*Grrrrrrkk!*

I forcefully pulled my foot from the ground. My stalled knee straightened.

When I put strength into my waist and arms, the spear shaft that had been forced downward by the Aura Blade began to rise against it.

Slowly, little by little. But without stopping.

“How are you……?”

The instant Go Jun’s eyes widened, I whispered a command that no one else could hear.

*Inventory open. Store White Flame.*

*Pop.*

It happened in the blink of an eye.

The blue-white flames that had been opposing the enormous Aura Blade vanished together with the spear. The balance of the tense struggle collapsed, and the blood-red energy slammed downward.

*Whoooooom! Slice!*

Space was cleaved apart amid a terrifying shriek of displaced air.

But I was no longer there.

Dozens of strands of hair severed by the sword pressure scattered over my shoulder. Before they even fell, my fist was already deep inside Go Jun’s guard, wreathed in blue-white hellfire.

*Flame-Extinguishing Divine Fist.*

The world slowed.

Space warped in the ultra-high temperature heat. It looked almost like the expression Go Jun was making now.

“No—”

Too late.

Along with a reply he could not hear, I threw my punch.

*Fwoosh—KABOOM!*

His voice, which had been about to continue, was buried beneath the thunderous impact. My fist, extending like a beam of light while burning through the air, slammed into his solar plexus.

I launched myself after his body as the tremendous impact sent him flying like a cannonball.

*Whoooooosh!*

A fierce wind brushed past my ears.

In a moment too brief to even call an instant, I crossed more than ten meters in a single burst and overtook Go Jun. As his body flew back toward the spot where I stood, I brought my clasped hands down like a hammer.

*CRASH! KRAKAKAK!*

The blow struck his abdomen. His armor’s upper body, battered by the consecutive impacts, melted under the Scorching Yang Qi.

Go Jun slammed into the ground, shattering it with his back, and a fountain of blood burst from his mouth.

*Pshhh!*

I moved to drive my fist down into the fallen Go Jun, only to be drenched in the blood he spat out.

My vision turned completely red. My movements instinctively faltered, and a sharp instinct rang out like a warning alarm.

*Danger!*

This was not a mistake. It was part of an attack he had deliberately set up.

The instant I realized it, I kicked off the ground. Red energy shot toward my body as I moved backward.

*Shhk! Slice!*

Hot pain spread from my side.

I had moved as quickly as possible, but the Aura erupting from the sword Go Jun had never once let go of was too large and massive to evade completely.

*Drip. Drip-drip.*

I staunched the blood pouring from my side while wiping the blood from my eyes.

Through my cleared vision, I saw Go Jun charging toward me after rising to his feet. He had thrown off his helmet.

A furious shout filled the devastated corridor.

“You fucking bastard!”

*Whoooooosh!*

The blood-red Aura released from the tip of his sword pierced through the air with a fierce shriek.

I narrowly avoided the attack by repeatedly retreating, then quickly flung both arms outward.

Along with the Magic that only I was permitted to use.

*Inventory open. Summon.*

*Shhk-shhk-shhk!*

Handles appeared in my empty hands, and several daggers shot forward at the same time.

Multiple streaks of light flew toward him without warning. Go Jun, now desperate, turned his sword sideways and held the blade across his front.

*Clang-clang-clang-clang!*

The four daggers bounced away amid sharp scraping noises and embedded themselves in the walls and ceiling. At the same moment, I drew up my internal energy and sent it flowing into my lower body. Flames rose from the tip of my advancing foot.

*Flamefire Path.*

*Fwoosh! Whoooooosh!*

I became a streak of flame and shot toward Go Jun. Seeing me charging without my spear, he let out a roar.

“I’ll kill you!”

His eyes had taken on the unmistakable color of blood. Red light gleamed from them in the darkness.

The next moment, an unprecedented energy burst from his entire body and swept in every direction.

*WHOOOOOOOOOM!*

It was a raging storm and an inescapable fog. Rather than tiring, Go Jun was emitting an even stronger wave of energy.

But I continued forward without stopping. I shot through the murky, violent fog of magical power.

And the enemy beyond the fog was doing the same.

*Zzzzzzzzz!*

An absurdly oversized Aura Blade, a full two meters long, flew toward me and cleaved through space.

Every time I twisted my body and narrowly avoided an attack, flesh tore and blood flowed beneath the Sword Pressure cutting through everything around me.

But it was fine.

As long as I did not fall.

As long as I could bring him down, make him pay the price for Kim Hwajong’s death, and protect those who remained from another threat.

*Slice!*

A moment later, pain like a burn swept across my chest.

My clothes and armor had long since been torn away by the aftermath of the fierce battle. A thin line appeared across my exposed skin, then turned red.

*Fwoosh!*

Blood surged from my chest. The wound was shallow, but the immense energy forcing its way inside through the cut made my vision swim.

I straightened my staggering body and kicked off the ground.

*Boom!*

I shot forward like a beam of light, leaving the thunderous boom behind me. At the end of my path stood a monster that had willingly abandoned its humanity.

“Jin Taekyuuung!”

Go Jun charged with a shout, his sword held upright. The Aura Blade wrapped around the weapon had taken on a murky, dark-red glow.

The closer I drew, the more clearly I felt that sticky, unpleasant energy.

*That can no longer be called mana.*

The corrupted and ominous energy opposite to pure mana was known by another name in this world.

*Demonic energy.*

The instant those two words surfaced in my mind, I realized that I had to bring out every move I had.

Me and Go Jun. Go Jun and me.

The distance between us had grown close enough for either of us to kill the other.

I could see the fury in his eyes and smell the foul odor mixed into his hot breath.

And then……

Go Jun and I extended our arms at almost the exact same moment.

*Shhk!*

The world slowed to a crawl. The wind split apart, and space was erased.

Faint delight spread across Go Jun’s face as he thrust his sword toward my chest.

*I won.*

His eyes seemed to say as much.

Unlike me, who was empty-handed, Go Jun wielded a sword wrapped in murky magical power. It was powerful, and it had a long reach. Of course he was certain of victory.

But he was wrong.

*Inventory open. Summon.*

Thought was faster than light, and the System answered my call without a moment’s hesitation.

My beloved weapon, shining pure white, appeared in my grasp as though it had been there from the beginning.

Blue-white hellfire coated its transparent spearhead.

*Fwoosh!*

Ultra-high-temperature heat shot forward, burning the surrounding air.

It had clearly started later than Go Jun’s sword, yet its speed was so strangely fast that it brushed past the murky Aura Blade and reached its target.

*Fwoosh!*

The horrifying sound of flesh being pierced was followed by the smell of burning skin.

Go Jun’s eyes were wide open as though they might burst from their sockets, but there was no longer any delight in them.

He looked down at the spear piercing through his chest, his eyes filled with shock and pain, and forced the words out of his throat.

“What is this……?”

I answered calmly.

“Striking Second, Hitting First. Someone who gained strength from a Magic Gem like you would never understand it, even if you died and came back to life.”

Every battle and every movement had a flow.

If you knew and predicted your opponent’s movements, you could arrive faster even if you started later.

Through my training and experience, I had mastered the intricacies of Striking Second, Hitting First. Go Jun had sought nothing but greater power.

That was what decided the outcome of this fight.

“Idiot. You should’ve used that rock of a head at least once to think about why your dead Master never recommended Magic Gems to you in the first place.”

“……!”

At the sound of my voice, filled with anger and disgust, Go Jun’s eyes trembled as though he had resigned himself to his fate.

Then the sword that had dropped limply without reaching me shot upward like lightning.

*Shing!*

It happened in an instant.

The murky energy, visibly smaller than before, gathered at the tip of the sword and stabbed toward my heart.

And just before it reached me, I recited another command in my mind.

*Inventory open. Summon.*

*KRAK!*

The mass of energy, packed with terrifying destructive and cutting power, was blocked.

In Go Jun’s eyes, which had widened once more, the armor with a faint red glow was reflected.

Fire Dragon Armor.

“What, what is this……?”

“What do you think it is, idiot? Life insurance.”

The reason I had kept the Fire Dragon Armor hidden all the way to the top floor—even after taking a minor wound to the chest—was to save it for an unexpected moment like this.

And my prediction had been exactly right.

“You…… What the hell are you……?”

I looked into the fear in his eyes.

Into the eyes of a human—or rather, a monster—driven to the edge.

Then I put strength into the spear embedded in Go Jun’s chest.

*KRAK!*
## Chapter artifact 594

# Chapter 594

*Crack!*

Along with that grisly tearing sound, a sensation I had experienced hundreds—thousands—of times traveled through my fingertips.

The feeling of flesh splitting and bones breaking.

It was a sensation I had grown used to at some point, and one that occasionally left a bitter taste in my mouth.

Because becoming accustomed to something like this meant I had taken that many lives with my own hands.

But at least this time, things were different. As I looked down at the dying man, I felt not the slightest trace of bitterness.

“Urgh……!”

A final groan escaped with a deflating sound. At the same time, the solidly built man dropped to his knees.

*Thud.*

The blood-red glow in his eyes, once terrifying enough to make anyone flinch, gradually faded. His entire body trembled faintly before the death rushing toward him.

No—perhaps what the man, Go Jun, feared was not death itself, but me, the one who had sentenced him to it.

“J-Jin Taekyung.”

His voice and eyes seemed ready to go out at any moment.

But I felt no pity.

Because my opponent wasn’t human like me. He was a monster.

Just as the members of the Peace Guild, myself included, had lost Kim Hwajong today, thousands of people whose names I did not even know had lost their beloved families and friends.

For the price of committing such madness, his death felt almost too easy. It was unfair.

“Cough. I-I can’t die like this……”

I looked down coldly at Go Jun, who was convulsing in pain on his knees.

“Die. Oxygen is wasted on a piece of shit like you.”

I had no intention of listening to some long-winded last words, nor did I feel like giving him the chance to leave any behind.

I wrenched White Flame out of his chest.

*Fwoosh!*

The instant the transparent spearhead came free, blood that had not yet evaporated sprayed out like a fountain.

With a fist-sized hole in his chest, Go Jun stared blankly up at me. Then his body slowly tilted.

*Splash.*

That was the end.

He plunged his face into a puddle made from his own blood and stopped moving with his eyes still wide open.

As I looked down at the corpse of the monster, no breath or spark of life remaining, I suddenly realized it.

*It’s over.*

The Disciple who had served Lee Jungryong faithfully for decades—and the de facto master of Ares Guild, one of the foremost Guilds in the world—had died by my hand.

He had caused two Monster Waves on purpose, creating thousands of casualties and costing Kim Hwajong and some twenty members of the Peace Guild their lives.

He had paid for it with his life.

*So this really is the end……*

But why?

Why did my heart feel hollow even after my revenge was complete? It was as though the hole was not in Go Jun’s chest, but in mine.

It was probably because I knew that the people who had left my side would never return.

*Are you still cold? Is it still dark?*

I turned away, asking questions that would never reach them.

Resisting fatigue and drowsiness heavy enough to crush my entire body, I slowly crossed the dark corridor, devastated by the fierce battle.

*Step.*

With every step, faces and memories rose before my eyes and obscured my vision.

I saw Gwangan Bridge collapsing and heard the screams of people consumed by terror. In the family photograph hanging from the rearview mirror of a passenger car, I remembered a promise I had made long ago by linking my pinky with someone I missed more than words could say.



“When Hayeon gets a little older, and you, Taekyung, start middle school, let’s come see the sea again. All right?”

“Really?”

“Of course. Here, promise.”



But today, the place from the promise I had kept deep in my heart had collapsed.

Innocent people had died, and monsters had spread like a plague. I had done everything I could, but I had failed to save more lives.

*Step.*

My heart was just as unsteady as my staggering footsteps. Amid that confusion, a warm voice rang out in my mind.



“It wasn’t your fault.”

“……!”

“You did your best.”



The silver-haired old butler who had comforted me even as he died had departed on a journey from which he could not return.

Whether the world he had reached was night or day. Whether it was cold or warm. I had no way of knowing.

I could only hope.

That his world was at least a little brighter. That he, who had trembled in the cold, was somewhere warmer.

And…… that he had believed my lie to the very end—the lie that the person he had wanted to see one last time had come.

*Step.*

Nothing happens without consequences. I believed someone had to pay the price. I believed that being punished for doing wrong was only natural.

That was why I had come here. I had thrown open the gates of a palace no one had dared approach and brought down an impregnable fortress.

I had fought, and fought, and fought again. And after finally killing the monster wearing a human face, I suddenly felt hollow inside and found myself wondering:

*What am I supposed to do now?*

I had thought that if I killed Go Jun, the root of all this evil, at least some of my anger would disappear. I thought I might even laugh out loud in relief.

But I hadn’t.

I could create and fill a massive pit with a single gesture, yet I could not fill the emptiness in my heart.

It had been the same three years ago, and it was the same now.

*Damn it.*

My mouth tasted bitter.

In the end, enduring the wounds was left entirely to those who remained.

I even found myself regretting that I might have given Go Jun a death that was too painless……

*Step.*

I suddenly stopped walking.

By then, an inexplicable sense of wrongness had seized my entire body. A cold chill slowly crawled up my spine.

*What is this feeling?*

Was it because of my extreme fatigue? Or perhaps because of my complicated emotions? My mind was hazy, shrouded in fog.

But after standing motionless and thinking for a moment, I finally realized the source of that wrongness.

*Go Jun should definitely be dead. So why……*

Why had the System window announcing his kill still not appeared?

I had driven a spearhead into the center of his chest and burned his organs. I had watched and felt him stop breathing with my own eyes.

“Don’t tell me.”

I muttered under my breath and turned around.

The corridor, horribly destroyed by the fierce battle, was shrouded in unusually deep darkness.



* * *



The System was absolute and immediate.

I knew that better than anyone. I simply had not noticed anything strange because I had been overwhelmed by exhaustion and deep thoughts in the moment of victory.

That was why I was not terribly surprised when I saw that the puddle of blood where Go Jun had been lying was empty.

*He’s alive. Go Jun is alive.*

That much had become certain.

What I wanted to know was how it was possible.

There had been only two people in Area A: Go Jun and me. And Go Jun had unquestionably been dead.

His heart had stopped and his breathing had ceased. Even if he had soaked in a half-body bath of top-grade potion, reviving him should have been impossible.

*Then how?*

With that question in mind, I began moving after the traces Go Jun had left behind.

Area A had a maze-like structure, befitting a secret zone permitted to only a handful of people. But following the trail of blood leading in one direction was not difficult.

I quickly crossed the space, taking in the information around me.

*There was no accomplice. He didn’t have the time or the chance to erase his traces.*

There was a sense of urgency in the marks he had left behind. It was almost as if I could see him crawling desperately along the floor, pressed flat against it by himself.

And then……

*He finally stood up on two legs. Right here.*

Two clear footprints had been stamped into the blood. Countless handprints marked the walls beside them.

What had happened?

Why had he writhed in agony?

Before long, I found the answer.

*That’s……*

It was blood.

Not the bright-red blood of a human, but blue drops of monster blood with a faint azure sheen.

The meaning of this was obvious.

I silently stared at the monster’s blood that had touched my hand, then shot forward.

*Whoosh!*

Amid the wind brushing past me on either side, I smelled a thick scent of blood and a foul stench. Even while exhausted to the point of collapse, I could sense someone’s presence drawing closer.

And when my footsteps carried me into another corridor—

I finally saw it with my own eyes.

The man who looked so completely different from the last time I had seen him.

“Go Jun.”

My voice echoed quietly between my lips.

At the same time, Go Jun—or rather, the *monster*—turned around as he staggered down the corridor.

“Krrk. Kurruk.”

The metallic growl, impossible to understand, was the least of it.

His enormous body stood four meters tall, while his arms and legs were grotesquely swollen as though they might burst. His appearance was horrifying, as if creatures of different species had been fused together, each part retaining its own shape and characteristics.

If there was one thing that had preserved its original form, it was the human face half-covered in scales, with blood-red eyes shining through the gaps.

“Jin…… Taekyung. Karruk.”

His eyes, filled with both fear and hatred, turned toward me.

I looked him up and down, then opened my mouth with disgust.

“Did you want to survive that badly? Even if it meant becoming a monster?”

“Shut…… up. This…… this wasn’t what I wanted either—”

*Crack! KRAK!*

It happened in an instant.

Before Go Jun could finish speaking, his right arm suddenly twisted as though moved by an invisible hand, and blue blood burst from it.

“GRAAAAH!”

A scream filled with pain rang out.

At the same time, rapid changes began throughout Go Jun’s grotesque body.

*Shlk. Crackle!*

The thick skin covered in hide and scales like a monster’s began to heal, while his crushed joints fitted themselves back together like puzzle pieces.

“Hah. Hah.”

Go Jun panted, the pain not yet gone.

Looking at him, I felt as though I understood how he had made it this far.

“Troll. Right?”

“……!”

At my casually tossed-out question, his eyelids trembled.

That meant I was correct.

A Troll was a monster with overwhelmingly powerful regenerative abilities. There was no question about that.

The Named Monster that had originally owned the S-grade Magic Gem Go Jun had absorbed this time must have been an extremely powerful Troll.

And……

*The S-grade Magic Gem he absorbed wasn’t the only one, was it?*

I could tell just by looking at him.

His grotesquely swollen body and tremendous regenerative power were characteristics of a Troll, but the scales and hide covering half his body were traces of another monster.

*Mutation. Pure and simple.*

Unlike mana, demonic energy was dark and turbid—a force that corrupted human beings.

So it was only natural that disharmony had occurred after he absorbed two S-grade Magic Gems containing an immense amount of demonic energy.

“Kurruk. I could have become stronger. Stronger than this. But you. You……”

I calmly cut him off.

“Not stronger. You would’ve become an even more horrifying monster. Look at yourself.”

“……!”

“You’re worse than a monster. You’re nothing but a monster—neither Hunter nor human. That’s what you are.”

*Step.*

I moved forward as I spoke.

Go Jun stared at me with his eyes wide open, then shouted like a scream.

“Don’t come any closer! Krrk! Don’t come near me!”

“That’s a problem. There’s a monster right in front of me.”

“T-This can’t be!”

His bloodshot eyes were now filled with fear.

He probably knew it, too.

With a body already showing signs of collapse simply from standing still, he had no chance of fighting me.

*Tap-tap-tap!*

So when Go Jun turned his back and began to flee, I was not surprised in the slightest.

I reversed my grip on White Flame’s shaft and hurled it.

*SHWAAAAK! BOOM!*

A streak of light wreathed in flames blasted through his legs and embedded itself in the ground.

As Go Jun, now without either leg, thrashed and screamed, flesh and bone rapidly regenerated from the severed ends.

Of course, I had no intention of standing around and watching.

“Go ahead and regenerate. Keep doing it as long as you can.”

*Thud!*

I gathered up the internal energy I had left and surged forward. I planted my foot on his back, seized his two thick arms, and pulled.

*Crack. KRAKAKAK!*

After losing both legs, Go Jun lost both arms as well and let out a scream.

But I did not so much as blink. I simply continued moving my hands.

*Slice! Stab!*

I pulled the spear from the ground and slashed and stabbed his body in several places. I seared the sections trying to regenerate with the Flame Divine Palm, then gripped them tightly and tore them apart.

It was a level of brutality I would never have shown under ordinary circumstances.

But the me standing here now did not hesitate even for a moment.

*KRAKAKAK!*

Regeneration and destruction continued without end.

And the first one to collapse beneath this never-ending cycle of agony was Go Jun.

“GRAAAAH! S-Stop!”

His eyes were not as red as before when he screamed in a thoroughly hoarse voice.

His regenerative power had begun slowing down at some point.

Now it had stopped completely.

“Now…… kill me……”

“I was planning to anyway.”

So that he could never come back to life again.

In a way even more certain than before.

I looked into Go Jun’s eyes and continued speaking.

“Whether you’re going to heaven or hell, go there first and wait for me. When I get there, I’ll kill you as much as I please.”

“……!”

That was all.

Those were the final words Go Jun would ever hear in this world.

*It’s over now.*

I did not wait for his answer.

Without the slightest hesitation, I brought the transparent spearhead down.

*Slice! Thud!*

With a sharp cutting sound, the head separated from the body and rolled across the ground.

That was the end of the monster who had become neither a hero like Cheon Taemin nor an ambitious warlord like his Master, Lee Jungryong.

*Ding.*

Along with the familiar chime piercing my ears, I picked up Go Jun’s head from the puddle of blood.

Then, with slow, staggering steps, I crossed the space where I alone remained.

I was tired.

# Checkpoint Review — 360–364

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

# Chapters 360–364

## Plot

The Western Heaven Demon Lord defeats Jin Taekyung in the underground prison, crippling his limbs and leaving him near death, but the Heavenly Power Demon breaks free and transfers three jiazi of internal energy to Taekyung in exchange for a promise to kill the Demon Lord. Taekyung returns to the treatment room, where the Demon Lord overwhelms the Divine Physician, crushes his lower dantian, and takes the Myriad-Poison Ring. Taekyung steals the ring through the Inventory and intercepts the Demon Lord’s attack aimed at the unconscious Jeok Cheongang.

The Divine Physician survives while shielding Jeok, but loses his dantian, martial arts, and suffers a broken wrist. Taekyung cannot appraise or destroy the ring, which the Demon Lord identifies as an indestructible sacred treasure. During their renewed fight, Taekyung breaks the Demon Lord’s ankle and gains insight into sensing his qi-controlled sword, but is again nearly killed.

Jeok Cheongang awakens from his long dream of his former life as Jangcheon. When the Demon Lord threatens Taekyung and demands Jeok’s death, Taekyung tears free the wrist holding him, enabling Jeok to attack with the Flame Divine Palm. Taekyung receives three Level Ups, partially recovering his injuries and internal energy, and breaks through into the Supreme Peak realm. He draws White Flame through Seizing an Object Through Empty Space, releasing a fire dragon from its spearhead as the confrontation continues.

## Continuity

- Jin Taekyung has reached the Supreme Peak realm and remains severely injured but partially restored after three Level Ups.
- White Flame is in Taekyung’s grasp, and its spearhead has manifested a fire dragon.
- Jeok Cheongang has awakened but remains physically weakened and incompletely recovered; he is fighting alongside Taekyung.
- The Western Heaven Demon Lord remains alive and hostile despite his crushed ankle and the destruction of his wrist. His confrontation with Taekyung and Jeok is unresolved.
- The Myriad-Poison Ring is in Taekyung’s possession, cannot be appraised by the System, and is identified as an indestructible sacred treasure.
- The Divine Physician remains alive but unconscious after losing his dantian and martial arts and suffering a broken wrist.
- The Heavenly Power Demon escaped after transferring three jiazi of internal energy to Taekyung and asked him to kill the Western Heaven Demon Lord.
- The underground prison continues to collapse.
- Cheongpung remains engaged in his unresolved confrontation with First Fiend.
- The Western Heaven Demon Lord serves the unidentified Lord of Heaven as one of four servants.
- The reported destruction of the Tang Clan, Qingcheng, and Emei remains unconfirmed.

## Translation Decisions

- Use **Supreme Peak**, **Dance of the Fire God and Demon**, and **hellfire** for the established terms.
- Render 신물 as **sacred treasure** and 이기어검 as **Qi-Controlled Sword** or the art of controlling a sword with qi.
- Retain **White Flame**, **Seizing an Object Through Empty Space**, **Sword Force**, **Scorching Yang Qi**, and **underground prison**.
- Preserve Jin Taekyung’s vulgar, self-mocking first-person voice and Jeok Cheongang’s rough, profane, fiercely protective voice.

## Durable state

{
  "active_continuity": [
    "Jeok Cheongang has awakened after his prolonged coma but remains physically weakened and incompletely recovered.",
    "The Western Heaven Demon Lord remains alive and hostile after suffering a crushed ankle and having his wrist torn free by Jin Taekyung; their confrontation is unresolved.",
    "Jin Taekyung has reached the Supreme Peak realm through enlightenment.",
    "White Flame is in Jin Taekyung's grasp after being drawn through Seizing an Object Through Empty Space, and a fire dragon manifested from its spearhead.",
    "The Divine Physician remains alive but unconscious after the battle and has lost his dantian and martial arts.",
    "The Myriad-Poison Ring remains in Jin Taekyung's possession and cannot be appraised by the System.",
    "Cheongpung remains engaged in his confrontation with First Fiend.",
    "The underground prison remains in the process of collapsing.",
    "The Western Heaven Demon Lord serves the unidentified Lord of Heaven.",
    "The reported destruction of the Tang Clan, Qingcheng, and Emei remains unconfirmed."
  ],
  "continuity_sources": [
    364
  ],
  "open_questions": [
    "What will be the outcome of the unresolved confrontation between Jin Taekyung, Jeok Cheongang, and the Western Heaven Demon Lord?",
    "What is the full nature and purpose of the Myriad-Poison Ring?",
    "Can the Divine Physician survive after losing his dantian and martial arts?",
    "What is the actual outcome of the attacks on the Tang Clan, Qingcheng, and Emei?",
    "Can Cheongpung survive or escape his confrontation with First Fiend?"
  ],
  "safe_through": 364,
  "temporary_decisions": [
    "Render 신물 as sacred treasure.",
    "Render 이기어검 as Qi-Controlled Sword or the art of controlling a sword with qi.",
    "Render 화신귀무 as Dance of the Fire God and Demon, 겁화 as hellfire, and 초절정 as Supreme Peak.",
    "Preserve Jin Taekyung's vulgar, self-mocking voice and Jeok Cheongang's rough, profane protective voice.",
    "Use established renderings for White Flame, Seizing an Object Through Empty Space, Sword Force, Scorching Yang Qi, and underground prison."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 360

# Chapter 360

I don't know how much time had passed.

My time moved infinitely slowly, while the Western Heaven Demon Lord's passed as quickly and violently as the current of the Yangtze I had seen a few weeks ago.

One thing was certain: even now, at this very moment, time was passing.

Thud!

I failed to see either his preparatory movement or his actual motion. By the time I realized the Western Heaven Demon Lord had taken a step, my head had already snapped backward.

Before I could even regain my balance, the sound of splitting air pierced my ears.

Shhk, thud! Thud-thud-thud!

Shoulder, chest, stomach.

A palm strike and a punch infused with internal energy flowed over my upper body like water.

Through the agony and the white haze filling my vision as my bones shifted, I gritted my teeth.

Crk.

One of my molars shattered, and for a brief moment, my mind cleared.

“Raaaagh!”

Whoosh!

With a cry squeezed out from the depths of my lungs, I swung my fist.

The Western Heaven Demon Lord caught the fist riddled with openings and slow beyond belief, then clicked his tongue.

“You still have strength left?”

“……!”

Crack!

Even muscles and bones hardened like steel were nothing more than kindling before the Western Heaven Demon Lord.

His hand, curled like a hook, seized my wrist and twisted. Flesh and bone shattered together.

The bones in my left arm, which had already been broken once, splintered into pieces, sending horrific pain through me.

“Gaaaaaagh!”

“Do not worry. I will call some skilled healers to treat you later.”

“Go… fuck yourself!”

I thrust out my still-usable right arm at the Western Heaven Demon Lord, who was wiping the blood splashed across his face.

The spearhead of White Flame, wrapped in a faint Spear Energy, stabbed toward his lower body.

Screech. Clang.

But the spearhead was blocked with absurd ease.

Not by the Black Dragon Armor or Body-Protecting Qi.

By the Western Heaven Demon Lord's hand.

“Futile.”

His hand, wrapped in ink-colored Force, tightened around the spearhead. The energy that had been dimly gathering disappeared as though swallowed by darkness.

“Give up. The outcome will not change anyway.”

With a quiet voice, the Western Heaven Demon Lord pulled on the spearhead.

I stubbornly clung to the shaft as it tried to slip from my flayed, blood-soaked grip.

A searing pain surged through me, but it was bearable.

I had endured more than enough pain in the past—and in the present.

Whoosh, crash!

I tumbled forward with the spear shaft. A handful of dirt entered my mouth and mixed with the blood.

The ice-cold, foul-smelling floor of the underground prison felt strangely more comfortable than ever.

*I'm sleepy.*

If I closed my eyes now, I felt as though I could fall asleep immediately.

After sleeping through a long dream that lasted for days, perhaps I would wake up not in the Murim but in the modern world.

A soft seat on a private plane headed for Sichuan, China, would be fine. So would the one-room at Hope Goshiwon, with its lingering smell of a stale bachelor.[^1]

*Maybe all of this is a dream.*

In the more than year I had spent here, I had gone through too much.

From F-rank Hunter Jin Taekyung to the Third Young Master of the Jin Family of Taiyuan. From a disgrace who brought shame to his family name to the Sleeping Dragon of Shanxi.

I had witnessed horrific wars and countless deaths. I had met so many people.

Jin Wikyung, who absolutely doted on his younger brother, and Jin Mukyung, who would have loved to kill his. Hyuk Mujin, who had shared life and death with me while always remaining at my side. Cheongpung, who was both my friend and my rival.

And…

*Old Master.*

My eyelids, which had been slowly closing without my realizing it, stopped.

That's right. The Fire King, Jeok Cheongang.

He was behind me, and I was in front of him.

That was why I could not fall. I could not run away.



*That insolent bastard. Taekyung, go on ahead.*

*H-hyung!*

*I'll catch up soon.*



Three years had already passed, but I would never forget what happened that day.

I had failed to protect the people precious to me, and I had survived through their sacrifice.

Yet even after gaining power beyond anything my past self could have imagined, I had repeated the same mistake.



*How about it? Dance of the Fire God and Demon. Isn't it incredible?*



Jeok Cheongang had been smiling then.

That smile held the joy of avenging his closest friend—and the relief of protecting one little brat he couldn't tell was his disciple or his enemy.

“Yes. It's incredible…”

A small voice leaked through my torn and swollen lips.

At some point, the floor of the underground prison no longer felt comfortable.

Feeling its unpleasant cold and stench, I began to raise myself.

I planted my still-usable right arm on the floor and supported myself on both knees.

My body felt as though it might break apart at any moment, and my movements were slow, but I did not give up.

When I finally stood upright on my trembling legs, the first thing I encountered was a pair of deeply sunken eyes.

“Impressive. To the point of looking foolish.”

Thud!

My nose broke, and my head snapped backward. But I did not fall or stagger back.

The Western Heaven Demon Lord's hand had seized my shoulder like a shackle.

“How many times must I tell you? It is already over.”

Crack.

My shoulder blade was crushed. The spear shaft slipped limply from my weakened hand.

Horrific pain should have followed, but the pain I actually felt was faint.

“If you are waiting for help, you are mistaken. The Sichuan Tang Clan will be destroyed. No, perhaps everything is already over by now.”

Crack!

This time, it was my legs.

The shins of both legs, which had been the only parts of me left intact, broke simultaneously. I lost my balance.

Ironically, the only reason I was still standing was that the Western Heaven Demon Lord had not let go of me.

“Will someone come to your aid as they did in Henan? The Sword Saint, who will only hear the news after half a month? The Sword Saint's successor, who is probably fighting desperately even now? If not…”

The Western Heaven Demon Lord turned his head.

Beyond the empty underground prison, destroyed and collapsed by our clash, his gaze settled on a tightly shut iron door.

“Your master, who still has not regained consciousness?”

“Cough.”

“Nothing will change. Today, the Tang Clan, Qingcheng, and Emei will be destroyed, and all of you…”

“Cough!”

The Western Heaven Demon Lord could not continue.

A sticky liquid of dirt and blood covered his face.

He clearly had not expected someone whose limbs had already been crushed to do something like this.

In a moment brief enough to call an instant, I drove my head forward with every ounce of strength I had at the man who had frozen while gripping my neck.

Thud!

With a heavy impact, the Western Heaven Demon Lord's head snapped backward.

My internal energy had run dry long ago, and my severe Internal Injuries made it difficult to move even a single finger. I did not know where that strength had come from. I did not even know myself.

And…

*I don't have time to think anymore anyway.*

That had been the last desperate struggle I could manage.

The Western Heaven Demon Lord stroked his reddened forehead and let out a quiet laugh.

“You really are… a dangerous man.”

I answered in a hazy voice.

“I should've cracked your skull.”

“If I had not raised my Body-Protecting Qi at the last moment, you might have.”

“You monstrous bastard.”

“Hah. It feels strange hearing that from you.”

Unfathomable emotions flickered through the Western Heaven Demon Lord's eyes as he looked at me.

At first glance, they seemed like anger. At the same time, they felt almost like admiration.

But before I could identify those emotions, an unexpected boom rang out.

Rumble-rumble-rumble, boom!

The source of the sound was neither me nor the Western Heaven Demon Lord.

The underground prison.

This entire space, stretching for several thousand feet, was trembling. Fist-sized stones fell from the ceiling, and the ground began to split apart.

The noise and vibrations soon ceased, but deep furrows appeared between the Western Heaven Demon Lord's brows.

“…I had better hurry.”

The instant he muttered that while casting a quick glance at the ceiling, the sky and earth flipped.

Then a small impact reached me through my back.

Boom!

A wall.

He had thrown me into the wall.

“Cough.”

I spat out blood, and a calm voice reached my ears.

“Sit there for a while. I will be back soon.”

“You…”

“If you are still alive by then, I will take you with me. If you happen to be dead…”

The Western Heaven Demon Lord fell silent briefly before continuing.

“That would not be so bad either. You are a dangerous person.”

“W-wait.”

I stretched out my hand with all the strength I had left toward the Western Heaven Demon Lord's retreating back.

I had to stop him. I had to prevent him from capturing Jeok Cheongang and the Divine Physician.

But not a single part of my body moved as I wanted it to.

“Cough. Gaaaagh!”

Dark-red blood poured from my open mouth.

The clotted pieces mixed into it were…

*Damn it. Those are pieces of my organs.*

It was neither the first time I had seen something like this nor an unexpected sight, but a profound despair weighed down my entire body.

My limbs were crippled, and I had suffered a fatal Internal Injury.

My mind stood in the Western Heaven Demon Lord's way, but with my crushed arms and legs, I could not move even a single step.

“Ah.”

I raised my head blankly with a groan.

The corridor where the Western Heaven Demon Lord had disappeared was empty.

The place, devastated by our clash, was filled with traces of craters large and small, collapsed walls, and other destruction.

The prison where prisoners had still been confined half a day earlier was now strewn with bent bars, fallen rocks, and things like broken chains.

At that sight, I realized.

*It's over.*

I had fought, and I had lost.

I had tried to stop him, but I had failed. I had tried to protect them, but I had failed.

The Western Heaven Demon Lord had been telling the truth.

The kind of luck we had seen in Henan would not happen again. The Tang Clan, Emei, and Qingcheng were headed for destruction, and Cheongpung could not handle them all alone.

*He'll probably die or be captured.*

I wanted him to run away instead, but that would never happen.

That was the kind of person Cheongpung was. Even covered in blood, he would return to the underground prison to save his Benefactor.

I stared into the darkness beyond, where the exit lay, and laughed weakly.

*Damn it…*

Everything felt like my fault.

Cheongpung. Jeok Cheongang. Even the Divine Physician, who had been dragged into this mess for no reason and would suffer because of it.

At least Hyuk Mujin and Gung Gibang had not come with me. That was the only thing I could be grateful for.

Rumble-rumble-rumble.

A small vibration reached me along with a roar that seemed to rise from the depths of the earth.

The sound announcing the end of the match.

There had been no need to go twelve rounds like in boxing. I had fallen after only three, and I would probably die soon.

*I'm sorry. All of you.*

The simple rule written in the capsule's instruction manual.

If you die in the Murim, you die in reality, too.

Everything I had built by traveling between the two worlds was crumbling little by little, just like this underground prison.

“I didn't think I'd die like this…”

My vision blurred. The pain throughout my body and the sounds reaching me through my ears slowly grew distant.

Then, just as I was about to slip away from all sensation, an old man's face suddenly entered my field of vision.

A chain with marks where something had torn it away.

A body so thin that its bones protruded, attached to an unusually tall frame.

I called out to him in a feeble voice.

“…Heavenly Power Demon.”

[^1]: A goshiwon is a very small, inexpensive room-for-rent arrangement common in South Korea.
## Chapter artifact 361

# Chapter 361

Step. Step.

There was not the slightest trace of urgency or hesitation in the Western Heaven Demon Lord’s stride.

Even when bits of rock fell from the ceiling overhead, announcing the beginning of the collapse, and even when pitch-black darkness blocked his path, that did not change.

The Four Great Demon Lords were beings entitled to walk that way.

There was only one thing that concerned him: the possibility that he might fail to carry out the exalted Lord of Heaven’s command.

*Jin Taekyung. That child held me up for quite some time.*

He had never imagined that Taekyung would delay him for so long.

As the thought of Jin Taekyung suddenly crossed his mind, the Western Heaven Demon Lord unconsciously rubbed his forehead.

Along with a throbbing pain, he felt the swollen lump there. It bothered him more than his torn palm or the blood running down his forearm.

*A lump.*

Jin Taekyung had been hanging there with all four limbs broken.

His internal energy had clearly been exhausted, and his Internal Injury was severe enough that it would not have been strange for an ordinary Peak master to have died already…

“To think I couldn’t completely block it even with Body-Protecting Qi.”

The Western Heaven Demon Lord let out a hollow laugh.

Jin Taekyung had pierced his Body-Protecting Qi with a mere scrap of cloth and wounded him. By ordinary common sense, such a thing was utterly impossible.

Two words surfaced in the Western Heaven Demon Lord’s mind.

*With everything he had.*

*Prepared to die.*

*Is this not supernatural powers in its truest form?*

It was unbearably fascinating. At the same time, it sent a chill through his chest.

In terms of martial arts realm, Cheongpung, who had already reached the Supreme Peak realm, was unquestionably ahead.

But there was another reason Jin Taekyung felt dangerous.

*He is strong simply because he is human.*

Martial arts that were impossible to believe belonged to a Peak master. And a level of tenacity beyond imagination.

If Jin Taekyung’s strength had not run out just then, the Western Heaven Demon Lord would have ended his life without hesitation.

But now, everything was proceeding smoothly toward its conclusion.

“Is this the place?”

The Western Heaven Demon Lord stopped before a firmly shut iron door. In this place, where most of the underground prison consisted of barred cells, the enormous iron door to the treatment room stood out immediately.

Of course, even without that, it could not have escaped the Western Heaven Demon Lord’s Qi Sense.

*No mistake.*

Without hesitation, the Western Heaven Demon Lord brought down a hand blade.

The Force infused into the edge of his hand easily cut through the iron door, made of steel a handspan thick, along with its locking mechanism.

Shhk! Boom!

The iron door, split in half, collapsed with a thunderous crash.

The Western Heaven Demon Lord strode into the treatment room. When he spotted someone, he smiled faintly.

“Are you the Divine Physician?”

Beside a bed made of Cold-Ice Stone, an old man sitting in a chair opened his closed eyes.

A calm voice slipped between his lips.

“That is merely a false title bestowed upon me by the people of this world.”

“I have heard plenty of rumors about you. They say no one knows your name or age—not even whether you are a man or a woman. I have wanted to meet you at least once.”

“And now that you have seen me, what do you think?”

“You look more or less as I imagined. You even look more like an immortal than those Daoist bastards who pretend to be lofty like celestial beings above the clouds.”

The Divine Physician sighed.

“I wish that were true. If this old man were an immortal, I would also possess the power to drive away fiends.”

“Do I look like a fiend?”

The Western Heaven Demon Lord spread both arms wide and spun around in place.

With his ordinary face and build, he would have looked like any unremarkable middle-aged man if not for his long robe, torn to shreds and soaked in blood.

“When the Lord of Heaven descends from the heavens to the mortal realm, four loyal servants stand beneath His almighty power.”

The Western Heaven Demon Lord continued in a gentle voice.

“I am neither a fiend nor an immortal. I am merely one servant who follows His command.”

“……!”

The sincerity contained in those words made the Divine Physician’s eyelids tremble.

Lord of Heaven? Servant? Whatever he meant, the man before him was unquestionably insane.

“What nonsense! If you are not a fiend despite slaughtering people without hesitation, then what are you?”

“It is unfortunate. But what can I do? Erasing those who oppose His will is also my duty.”

“Y-you are…”

The Divine Physician was rendered speechless when the Western Heaven Demon Lord let out a small sigh.

The thick scent of blood soaked into every word he spoke and every small movement he made, enough to make nausea rise in the Divine Physician’s throat.

“Get out.”

“Hm? What did you say?”

“I said get out. No one is permitted to enter during treatment. Especially a fiend like you.”

The Western Heaven Demon Lord stared at the Divine Physician’s stiffened face, then laughed aloud.

“I thought you were an inflexible physician, but you tell jokes as well. Divine Physician, the treatment is already over.”

“It is not over.”

With an amused expression, the Western Heaven Demon Lord moved forward. In the direction of his steps lay Jeok Cheongang, lying motionless as though dead.

“I believe the patient should be moved somewhere else.”

“Before that… you should ask the physician’s permission.”

The Divine Physician rose from his seat, his face rigid.

At that very moment—

Pa-pa-pat!

Dozens of rays of light shot out from within his billowing sleeves. Needles of various sizes flew in straight lines, while others traced arcs toward the lethal acupoint behind the neck.

Yet the Western Heaven Demon Lord’s smile only deepened as he watched the rays shoot toward him.

“How interesting.”

Tudududuk!

He made no movement whatsoever.

The powerful Body-Protecting Qi surrounding his entire body simply did its job.

Dozens of needles struck the Body-Protecting Qi and trembled violently.

“And unfortunate.”

Crack.

The Western Heaven Demon Lord clenched and then opened his hand. Invisible energy, following its master’s will, snatched up the needles and crushed them.

The Divine Physician might have learned martial arts, but the gap between him and the Western Heaven Demon Lord was as vast as the distance between heaven and earth.

“I will say it again. The treatment is over.”

“……!”

Along with the Western Heaven Demon Lord’s quiet voice, the Divine Physician’s body rose into the air.

The art of Seizing an Object Through Empty Space—a feat only someone with terrifying internal energy could perform.

Flung through the air as though something had struck him, the Divine Physician turned deathly pale as the Western Heaven Demon Lord caught him by the throat.

“F-fiend…”

“That hardly seems like something a physician who unleashed a killing move without hesitation should say. Wait, wouldn’t that make you a fiend too?”

“If I think of the blood that will stain your hands, I will gladly become one!”

Whoosh. Thunk.

The Divine Physician’s palm strike, thrust out with a shout that brought up blood, was blocked with ease.

Crack-crack.

The Western Heaven Demon Lord applied force and broke the old physician’s hand. A strange glint passed through his eyes.

“The Tang Family Head was right. You had it.”

The Western Heaven Demon Lord’s gaze settled on the Divine Physician’s hand.

Around his wrinkled finger was something that did not suit a physician in the slightest.

“So this is the Myriad-Poison Ring…”

The ring gave off a soft glow, while its jewel looked as though it had trapped light and darkness together within it.

The Western Heaven Demon Lord gazed at the objective of this mission with a rapturous expression, as though he had been bewitched. He carefully removed the Myriad-Poison Ring from the Divine Physician’s hand and slipped it onto his own.

“The Lord of Heaven will be pleased.”

The Divine Physician, who had watched everything unfold, let out a suppressed groan.

“W-what are you planning to do?”

“Do not worry about it. Your role ends here anyway.”

Whoosh! Thud!

A palm strike that shot forward like a blade pierced the Divine Physician’s abdomen.

Along with the pain of his lower dantian being crushed, the Divine Physician was flung far away and vomited blood.

“Bweeeeegh!”

“It seems I no longer need the physician’s permission. Wouldn’t you agree?”

The Divine Physician despaired, and the Western Heaven Demon Lord laughed heartily.

Everything was over. He had finally obtained the Myriad-Poison Ring the Lord of Heaven desired, and he had erased the three sects that held sway over the world from this land.

There was now nothing left that could stand in his way. It was time to end everything and return.

“Come. We should go together. There is someone who wants to see you.”

The Western Heaven Demon Lord whispered toward Jeok Cheongang, who slept peacefully atop the Cold-Ice Stone, then used Seizing an Object Through Empty Space to pull his body toward him.

Or rather, he was about to pull him closer when—

Woooooong.

“……!”

A low, small sound, like the buzzing of bees.

Only the Western Heaven Demon Lord could have noticed it. It was a tremor in the air, a faint vibration that slowly drew nearer.

*Could the collapse have already begun?*

The Western Heaven Demon Lord turned his head toward the source of the sound.

Outside the treatment room, where the iron door had disappeared, a faint light flickered within the pitch-black darkness.

“What is that…”

He deliberately furrowed his brow.

Then, in the next moment, the Western Heaven Demon Lord’s eyes widened.

Woooooong! Rumble-rumble-rumble!

The vibration grew stronger. Wind and air tore apart.

And then—

KRAAAAAA!

A huge light shot forward, erasing the space before it.

No—a spear wreathed in blue flames.

At the name that flashed through the Western Heaven Demon Lord’s mind, he burst out laughing.

“Supernatural powers! Truly, this is supernatural powers!”

Along with his skyward laughter, a vast darkness rose and shot forward.

White Flame, engulfed in blue fire, collided with the darkness.

KABOOOOOM!

Amid the thunderous roar that shook the underground prison, a voice rang out.

“The sickroom is off-limits unless you’re family or a Disciple. You fucking bastard.”

* * *

Step. Step.

I pushed through the cloud of dust and moved forward.

The rocks pouring from the ceiling like a rain shower could not stop my steps. Neither could the pitch-black darkness blocking my vision.

I simply continued toward the one person somewhere beyond it.

*What a monster. I never expected him to die from something like this.*

I could not see him, but I could feel him. The immense energy coiled within the Western Heaven Demon Lord’s body.

But it did not frighten me as much as before.

I calmly clenched my fist. The powerful internal energy overflowing from my entire body felt almost tangible in my hand.

*Heavenly Power Demon.*

The clash between me and the Western Heaven Demon Lord had been a new opportunity for him.

The rocks that fell when the ceiling collapsed had broken his restraints, and the old man called a fiend had been able to leave the underground prison for the first time in decades.

And the Heavenly Power Demon’s first words to me had been completely unexpected.



*You killed all the other prisoners.*

*Cough. So?*

*You bastard. Why did you leave me alive?*

*Did that bother you so much?*

*Answer the question. I can cut off your breath right now.*

*Wait a little longer. It’ll cut itself off.*

*You bastard!*



It had been a conversation between two idiots.

One man with all four limbs crushed. One whose Sinews and Meridians had already been severed.

But the Heavenly Power Demon had one advantage over me.

At least his internal energy was intact.

I had already been dying, and I was afraid of the approaching death.

I wanted to continue one last conversation with the person watching me die.



*I didn’t want to kill you.*

*Why not?*

*Because at least the person I knew wasn’t a fiend.*

*……!*

*I think a good person from the Demonic Cult is better than a bad person from the orthodox faction. If I killed someone like that, I felt like I’d become the same kind of fiend.*



In truth, I had hesitated again and again. If I killed the Heavenly Power Demon, I could gain a massive amount of EXP and level up several times.

And after much deliberation, I chose to give it up.

Looking back, it had probably been for the best. The Western Heaven Demon Lord was not someone I could defeat by leveling up once or twice.

Rather than dying with an unpleasant feeling in my chest, I thought it was better to leave this world feeling relieved.



*Well… this isn’t so bad either.*



The Heavenly Power Demon had stared at me with a complicated gaze for quite some time before making me an offer.

*An offer I couldn’t possibly refuse.*

I remembered the Heavenly Power Demon’s final words and swept my hand through the air.

A tremendous blast of wind scattered the dust cloud, revealing his figure.

“Hyung’s here.”

“Kha! Hahahaha!”

I looked over the shoulder of the Western Heaven Demon Lord, who was bent forward like a shrimp and roaring with laughter.

A dozen meters behind him, someone stood unsteadily in the treatment room with its door gone.

The Divine Physician. His face deathly pale, he nodded.

It meant that Jeok Cheongang was safe.

*Thank goodness. I’m not too late.*

Just as I let out a sigh of relief, the Western Heaven Demon Lord finally stopped laughing and raised his head.

“You have changed so much that I hardly recognize you.”

“I received a gift. From someone I never expected.”

“A gift?”

“Yeah. I received internal energy.”

The Western Heaven Demon Lord let out an exclamation.

“Transmitting Internal Energy Across the Body!”

“Some people call it that.”

“Did you use that power you mentioned? The one like the Essence-Siphoning Great Technique?”

“No.”

“You had a fortuitous encounter. Ha-ha!”

“It wasn’t free. I was asked to do one thing.”

“A favor?”

“Yeah.”

I quietly nodded. I remembered the Heavenly Power Demon’s words as he transferred his internal energy to me.



*The Western Heaven Demon Lord…*



“He asked me to kill you.”

Tudududuk. Grab.

When I reached out, White Flame was pulled free from deep within the wall and caught in my hand.

The fire dragon, swollen by three jiazi of internal energy, spread its wings.

“You’re dead.”

The Western Heaven Demon Lord smiled broadly.
## Chapter artifact 362

# Chapter 362

The Western Heaven Demon Lord spoke with a laugh.

“I admit it. You are the very embodiment of supernatural powers.”

He had crushed all four of Jin Taekyung’s limbs with his own hands and inflicted severe Internal Injuries.

A cripple? If things had ended there, it would have been a blessing. The injuries were more than enough to kill him.

And yet the young man, Jin Taekyung, had survived.

He had returned to stand before the Western Heaven Demon Lord with his limbs restored without a single scar and his internal energy more powerful than ever.

*Even dozens of sorcerers working together couldn’t achieve this level of recovery.*

Was this not the very manifestation of supernatural powers—a miracle?

The Western Heaven Demon Lord trembled with a sudden surge of excitement and wonder.

Seeing him like that, Jin Taekyung tilted his head and sneered.

“What? Thinking about dying soon making you need to take a piss? Why are you shaking so much?”

“Do you know how many years I have lived?”

“No. I don’t want to know, either.”

The Western Heaven Demon Lord nodded.

“Of course. To be honest, I don’t know myself.”

“Are you an idiot?”

“As I grew older, counting the years began to feel meaningless. If I had continued living as I was, I might have grown so weary of boredom that I chose death.”

“Can’t you die now? I’m seriously willing to kneel.”

“I’m sorry, but I’m enjoying myself more than ever. Just as I once met the Lord of Heaven, I have met you today.”

The Western Heaven Demon Lord smiled brightly once more.

For him, the past several decades had been a tedious period of endurance.

He missed war and blood. He wanted something he had never experienced before.

A novelty that even the Poison King and the Heaven-Shaking Venerable Nun had failed to provide.

That very thing the Western Heaven Demon Lord had longed for was present in the young man before him.

“I have only one request.”

The corners of the Western Heaven Demon Lord’s mouth stretched wide.

His grotesquely distorted face looked like a fiend from the Lotus Sutra.[^1]

“If possible, hold out for a long time.”

Rumble-rumble-rumble!

The ground shook violently.

Black qi streamed from the Western Heaven Demon Lord’s entire body, pressing down on everything around him.

When an absolute master wielding power that could shatter heaven brought down a sword steeped in darkness, ink-black Sword Force surged forward, erasing the space in its path.

Whoooooosh!

“I have one request, too.”

The young man, Jin Taekyung, gripped his spear.

Blue flames wrapped around the spearhead, illuminating the darkness like sacred fire.

“If possible, die quickly.”

KABOOM!

* * *

A deafening boom shook heaven and earth, and a massive impact traveled along the spearhead.

Krrrk!

I felt a surge of joy as I looked at the ink-black Sword Force clashing with White Flame.

*I have a good chance of winning.*

That certainty came from this single exchange.

Sword Force and Spear Energy collided.

If you asked which one was superior, ninety-nine out of a hundred people would answer Sword Force.

The remaining one would probably scold you for asking something so obvious.

But…

*This is doable.*

During my first battle against the Western Heaven Demon Lord, I had been forced to retreat after suffering an Internal Injury with every exchange.

But the enormous internal energy the Heavenly Power Demon had given me through Transmitting Internal Energy Across the Body changed everything.

I had retreated only a single step.

The Western Heaven Demon Lord, who had seemed impossibly distant, had become someone I could reach simply by stretching out my hand.

“Internal energy sure is nice, huh? Don’t you think?”

Zzzzzzt.

The Spear Energy, massive to the point of absurdity, did not lose even a bit of its light against the ink-black Sword Force.

Between the crossed weapons, the Western Heaven Demon Lord looked at me with admiration.

“I guarantee you, there has never been a Peak master like you in the history of the Murim.”

“Of course not. They probably didn’t have more than three jiazi of internal energy.”

I looked straight at him and added,

“And this ability, too.”

Before I had even finished speaking, I was already giving a command in my mind.

*Strength, Agility—fifty points each.*

The Heavenly Power Demon had given me more than internal energy.

Through ten Level Ups, I had recovered from all my injuries, and the Stat Points that came with them had remained untouched.

Whoooooosh.

A dazzling halo of light enveloped my entire body.

A change only I could feel happened in an instant.

And now it was time to see that change with my own eyes.

“Put all your strength into your ‘don’t-go.’”

“Your don’t-go?”

“Your asshole, dumbass.”

I would make him shit himself.

I gritted my teeth and put strength into the hand gripping the spear shaft.

Grrrrrk.

What were my stats now?

I didn’t know the exact numbers, but one thing was certain.

At the very least, this body had already gone far beyond the limits of a human being.

Under the tremendous pressure, the smile disappeared from the Western Heaven Demon Lord’s face.

“This is ridiculously crude…!”

“You’re poking me where it hurts.”

It was unbelievably crude, but it was also the most certain method possible.

The proof was that the spear, which had been gradually pushed back under the pressure of the Sword Force, had begun to tilt ever so slightly toward the Western Heaven Demon Lord.

*If I lack martial arts, I make up for it with my body.*

It was a method only I could use in this world.

At the same time, it meant that the Western Heaven Demon Lord possessed martial arts several levels above mine.

“Ha!”

Krrrk!

The moment a short shout burst from the Western Heaven Demon Lord’s mouth, the sword in his hand traced a strange line and coiled around the spearhead.

It was a redirection technique based on the principle of Four Ounces Deflecting a Thousand Catties.

When the spearhead stabbed into empty air, compressed air exploded.

As I staggered for an instant, the Western Heaven Demon Lord reached out.

Whoosh-whoosh-whoosh!

Invisible, formless qi.

I couldn’t see it, but I could feel it—the moment it would come and the direction it would take.

Along with that realization, my body moved like flowing water.

I bent backward until my back nearly touched the ground.

Pfft!

Five strands of Finger Qi fired by the Western Heaven Demon Lord grazed my philtrum.

Blood spattered, and the coppery scent of it filled my nose.

When I rose with a carp-leaping maneuver, the ink-black Sword Force was already slicing diagonally toward my body.

Whoooooosh! Shhk!

The Sword Force missed me by the width of a hair and tore through space.

That alone was enough to bring down a pillar three zhang away and split the bars of the underground prison like tofu.

It was too close a distance to swing my spear.

But I already knew how to move.

*Inventory open. Store.*

White Flame disappeared from my hand, and I thrust both arms toward the Western Heaven Demon Lord’s chest.

Whooosh!

Hot air mixed with my exhalation.

Just as my two palms, imbued with the power of Flame Divine Palm, shot forward, the Western Heaven Demon Lord released his grip on the sword hilt.

His hands blurred, and he suddenly slammed both palms forward.

KABOOM!

The moment our four palms, each carrying tremendous internal energy, collided, a violent gale erupted around us.

The rocky ground caved inward, and the force of the collision was strong enough to blow apart everything nearby.

But that was not the real problem.

*Hngh!*

I suppressed the groan trying to escape.

A massive wave of energy poured forth from our touching palms and intertwined fingers, making my vision swim.

*This bastard, Western Heaven Demon Lord. What the hell is with his internal energy…?*

The internal energy I currently possessed amounted to three jiazi.

In terms of internal energy alone, I was more than qualified to stand shoulder to shoulder with the Sect Leaders of the Nine Sects and One Gang and the Five Great Families.

But the Western Heaven Demon Lord—the monster standing before me—was on an entirely different level.

*This is insane.*

Hissssss.

The heat gathered in my hands gradually faded, and darkness began to swallow the flames.

The Western Heaven Demon Lord’s quiet voice slipped between his lips.

“You have no need to feel so wronged. A tower built easily is bound to collapse just as easily.”

“……!”

“You are merely a strong child. That is the limit of those who have failed to cross the wall.”

Limit?

At that single word, my teeth clenched on their own.

It was a word I had heard to the point of exhaustion throughout my life.

A bastard raised without a father. A bastard from a poor family. A bastard doomed to remain an F-rank Hunter until the day he died…

At the end of every sharp word aimed at me, the word *limit* had always been attached like a tag.

Even now, after I had accomplished so much.

“I swear, I’m going to…”

A question mark appeared over the Western Heaven Demon Lord’s face at my suppressed voice.

I held back the endless flow of his internal energy and muttered as though groaning,

“I’m going to circumcise that mouth of yours.”

“……!”

It did not take long for the question mark to become an exclamation mark.

I ground my teeth and summoned every last bit of strength I had. My body, which had been pushed backward, began to move forward little by little.

I slowly bent the Western Heaven Demon Lord’s intertwined fingers.

Crack!

The sound of bones twisting out of place made him frown.

“Your strength is the greatest beneath heaven. But this is as far as you go.”

Crack-crack-crack!

It happened in an instant.

The Western Heaven Demon Lord stepped on empty air and launched himself into the air, driving his knee into my face.

The bridge of my nose, which had only just recovered, caved in, and several broken teeth flew through the air.

I hurriedly pulled my hand away and wiped the blood covering my eyes.

“Ghk!”

“Your limit is clear.”

Whoosh—bang!

A fist flew toward me with a powerful crack through the air.

I raised my arm to shield myself, but the shockwave ruptured my eardrums.

As I staggered for a moment, punches and kicks poured down on me like rain.

Thud-thud-thud-thud-thud!

My chest, stomach, legs.

The attacks came without pause, battering my entire body.

But unlike in our first battle, I did not allow the attacks so easily, nor did I fall.

*I’ve already been through this once. I’m not going to take it twice.*

I reached toward a pale afterimage and caught something solid.

The Western Heaven Demon Lord’s arm—the part even the Black Dragon Armor did not cover.

Without the slightest hesitation, I twisted his arm.

No.

I wrung it out like laundry.

Krrrk!

His skin tore, and splintered bone protruded.

No matter how great a master someone was, pain could still be felt.

With a suppressed groan, the Western Heaven Demon Lord threw a punch.

Unlike before, his movements had become duller and rougher.

There was no reason I could not avoid it.

Bang!

Compressed air exploded half a span away from my face.

The instant I shot out my arm like lightning and caught his fist—

“Huh?”

I discovered something familiar and froze in place.

A ring set with a small gemstone that radiated a mysterious light.

It was strange that I had only noticed it now.

*Why does he have the Myriad-Poison Ring…?*

In that brief instant, split into countless smaller moments, all kinds of thoughts flashed through my mind.

And after the flash of insight came the Western Heaven Demon Lord’s attack.

Crack!

I had been distracted at a time like this.

Of course I couldn’t avoid it.

After being sent tumbling, I rose while clutching my ringing head.

I had been hit, but I began laughing like a madman.

The Western Heaven Demon Lord frowned at me.

“Why are you laughing? Have you lost your mind?”

“Lost my mind? You’re the one who’s lost his mind, dumbass.”

Laughing, I shook the object in my hand.

Can you see it?

The brand-new Item I had just stored in my Inventory and pulled back out. Still warm.

“What are you going to do if you lose something important? Huh?”

“……!”

A multitude of emotions crossed the Western Heaven Demon Lord’s face when he saw the Myriad-Poison Ring.

Shock. Surprise. Confusion.

And anger.

The Western Heaven Demon Lord looked down at his suddenly empty hand and spoke in a heavy voice.

“How?”

“Who knows? Maybe it’s the power of supernatural powers you’re so fond of.”

A single brush had been enough.

The Myriad-Poison Ring had left the Western Heaven Demon Lord’s hand, been safely stored in my private secret vault—the Inventory, which no one else could access—and was now being slipped onto my middle finger.

“Since it’s a sacred treasure, it certainly has a different look to it. Don’t you think?”

“Give it back. It is not something the likes of you can possess.”

I raised my middle finger toward the Western Heaven Demon Lord.

“What do you think? Pretty?”

“……!”

The Western Heaven Demon Lord’s body trembled with rage.

His usual composure had vanished without a trace.

And seeing him like that, I was finally certain.

“The Myriad-Poison Ring. This was your objective from the very beginning.”

The moment I saw the ring on the Western Heaven Demon Lord’s finger, the first thing that came to mind was the Green Jade Buddha Staff, the sacred treasure of Shaolin Temple that the Blood Lord had stolen during the massacre at Shaolin.

“I figured there had to be something important when that bastard clung to it while running away… Are you guys collecting orbs or something? I heard that if you gather seven, a dragon appears and grants you a wish.”

The Western Heaven Demon Lord’s eyes sank into darkness.

“I told you to give it back.”

“Yeah. Fuck off.”

I waved the middle finger wearing the Myriad-Poison Ring for him to see.

At the same time, I muttered inwardly.

*Inventory open. Store.*

The Western Heaven Demon Lord’s eyes widened as the Myriad-Poison Ring vanished without a trace, as though erased by an eraser.

“You…!”

Rumble-rumble-rumble.

The qi surrounding the Western Heaven Demon Lord surged violently.

The sword he had pulled through Seizing an Object Through Empty Space flew into his hand.

Tss-tss-tss-tss!

Along with the ink-black Sword Force burning more fiercely and violently than ever, the Western Heaven Demon Lord spoke.

“This is the last time. Hand it over.”

The Western Heaven Demon Lord was different now that he had lost the most important object.

With his composure shaken, his sword was bound to waver as well.

At this level, the tide could still be turned.

“I’ll answer one last time. No.”

The moment the Western Heaven Demon Lord’s eyes sank deeply at my answer—

“You brought this upon yourself.”

Along with his emotionless voice, the ink-black Sword Force coiling around the blade shot out like an arrow.

But the destructive force was not aimed at my arms, legs, or neck.

At the end of the devastated corridor stood the treatment room.

“No!”

I launched myself forward with a scream.

The muscles throughout my body, swollen as though they might burst, cried out in pain.

The internal energy I desperately dragged up scraped against my heart meridian.

But it was fine.

As long as I could block it.

As long as I was not too late.

*Old Master!*

Along with a cry that never escaped my lips, I kicked off the ground once more.

KABOOOOOM!

In the slowed world, a deafening roar like the splitting of heaven filled my ears, and a blinding flash flooded my vision.

[^1]: The Lotus Sutra, one of the major scriptures of Mahayana Buddhism.
## Chapter artifact 363

# Chapter 363

KABOOOOOM!

A tremendous roar and shockwave slammed into my entire body.

For a moment, my vision went distant. The ceiling and floor turned upside down, and my hair fluttered in the air. My body flew helplessly through the room and crashed into a corner of the treatment room.

Crack!

A sharp current raced up my spine, and something hot surged up from deep within my lungs.

“Ghk!”

Dark red blood spilled across the floor. It was obvious proof that I had suffered a serious Internal Injury.

And it was true.

*Damn it. How long has it even been since I recovered?*

The only consolation was that my injuries were not as severe as before, and that I had successfully protected the treatment room from the Western Heaven Demon Lord’s Sword Force.

“Are you all right?”

At my question, the Divine Physician lifted his head from where he had curled up in a corner of the treatment room.

His body was covered in pale dust, and Jeok Cheongang was held in his arms. After letting out a small groan, he answered,

“Thanks to Young Master Jin blocking it, I am unharmed.”

But despite his answer, the Divine Physician’s condition was clearly far from normal.

His beard, white as an immortal’s, was stained with blood. His wrist was bent at a strange angle, and through the tears in his clothes, I could see his lower abdomen covered in dark bruises.

*That’s…*

There was no doubt about it. The Divine Physician’s dantian was ruined. Having lost all the martial arts he possessed, he was now nothing more than an ordinary old man.

No, with his qi-sea acupoint destroyed and his arm broken, his situation was anything but good.

*Even in the middle of all that, he still protected Old Master…*

Not a single scratch marred Jeok Cheongang’s body. That was because the old physician had ignored his own condition to protect his patient.

“Old Man Dong.”

“This old man is fine, so do not worry.”

The Divine Physician gave me a faint smile, then looked at me with concern.

“More importantly, I am worried about Young Master Jin’s condition. This old man will go to you, so just wait a moment—”

Instead of answering, I reached out a hand.

Formless internal energy flowed from my fingertips and gently pushed away the Divine Physician, who had been trying to approach me.

“Y-Young Master Jin?”

Before the Divine Physician could finish speaking, a streak of Finger Qi shot through the air from somewhere beyond us and pierced the wall.

It had passed through the exact spot where the Divine Physician’s head had been only moments ago.

Shhk! Pfft!

Had I been even one second later—no, even a quarter of a second—the Divine Physician would already have been dead.

I gestured for the physician, who had frozen like a rock, to get out of the way. Then I turned my head and stared straight ahead.

“That’s pretty low, going after a helpless old man.”

Beyond the clouds of dust splitting apart like the Red Sea, the Western Heaven Demon Lord finally appeared.

His chilling voice slipped between his lips.

“Low? You were the one who threw away the opportunity I gave you.”

The relaxed attitude and refined tone he had always maintained had disappeared long ago. I could feel the concentrated killing intent in his eyes as he stared at me.

“You touched something you should not have touched.”

“Fuck, anyone listening to you would think the Myriad-Poison Ring was an erogenous zone. You’re so old you can’t even get it up anymore, asshole.”

“……!”

I used White Flame as a cane and pushed myself to my feet.

Every bone in my body throbbed as if it were about to break. Judging by the pain, some of them probably had cracked. On top of that, I had suffered a severe Internal Injury.

*Damn it. He was already a monster to begin with.*

For a moment, I regretted provoking him.

I had never imagined that a Supreme Peak master like the Western Heaven Demon Lord would resort without hesitation to tactics fit for some Third Rate dark-path thug.

But…

“This must be that important to you. Right?”

I shook the Myriad-Poison Ring I had just taken out of my Inventory.

The Western Heaven Demon Lord’s footsteps, which had seemed impossible to stop, came to an abrupt halt.

“Hand it over at once—”

“You want me to give it back? That won’t be difficult.”

“You intend to negotiate?”

“You catch on fast.”

The Myriad-Poison Ring was nothing more than a strange ring to me—no more and no less.

But it was different for the Western Heaven Demon Lord.

He considered this tiny ring more important than the destruction of the Sichuan Tang Clan, Qingcheng, and Emei.

Just like the Blood Lord, who had desperately taken the Green Jade Buddha Staff with him even while losing an arm.

“Take your lackeys outside and withdraw at once. Otherwise, you will never see the Myriad-Poison Ring again.”

“Never see it again…”

The Western Heaven Demon Lord brushed back his hair, stiff with blood.

After a brief silence, a low voice slipped from his lips.

“Ridiculous.”

“What?”

“How could it not be ridiculous? I could simply kill everyone and take it.”

“……”

“Nothing will change. Not you, not your Master, not the Divine Physician. No one can escape death.”

Even if I explained it, the Western Heaven Demon Lord could not properly understand the concepts of subspace or the Inventory.

Perhaps, just as he said, killing me really would cause everything inside my Inventory to spill out.

But the Western Heaven Demon Lord had overlooked one thing.

“Well, that sounds plausible enough. But you should have considered the possibility that I might destroy the Myriad-Poison Ring first.”

I possessed enough grip strength to crumple steel like paper. Even without circulating internal energy, turning this little ring into powder would be easy.

“So don’t get any bright ideas. Back off. If you take even one more step—”

Step.

I could not finish my sentence.

The Western Heaven Demon Lord took a step forward without hesitation and smiled.

“What? Are you flustered?”

He did not wait for my answer. With a face that looked unable to contain its delight, he continued,

“It is truly amusing. You call it a sacred treasure, yet you do not actually believe it is one.”

“What is that supposed to mean?”

“My mistake. I thought you would understand after hearing that much.”

The smile vanished from the Western Heaven Demon Lord’s lips. His eyes bored into me, filled with scorn and contempt.

“Did you really think a mere human made of flesh and blood could do anything to a sacred treasure imbued with such great power?”

“……!”

I looked down at the Myriad-Poison Ring resting in my palm.

A sacred treasure passed down through the generations of the Sichuan Tang Clan. One of the old legends of the Murim. A strange ring said to detoxify and absorb any poison under heaven.

And…

*The Myriad-Poison Ring cannot even be appraised by the System.*

Sacred treasure.

The single word flashed through my mind, and my heart seemed to drop into my stomach. Something ran down my back—whether it was blood or cold sweat, I could not tell.

Drip. Drip.

My fist clenched reflexively, and drops of blood fell from it.

Even beneath my terrifying grip, the Myriad-Poison Ring did not bend. Instead, it dug into my palm like a thorn.

“Damn it.”

I muttered under my breath.

There could be no further compromise or retreat.

The Western Heaven Demon Lord took another light step toward me.

“I regret what this means for the Blood Lord, but…”

Tss-tss-tss-tss!

“I will have to kill you.”

The black mist pouring from his entire body swallowed the treatment room.

* * *

Pa-pa-pat!

The Western Heaven Demon Lord’s figure vanished.

He erased the distance of several zhang in a single step, then swung his ink-black Sword Force. Solid rock split apart like tofu.

I bent at the waist and avoided the attack, then thrust my spear forward like a fired arrow.

Bang!

The spearhead stabbed into empty air, and compressed air exploded.

The Western Heaven Demon Lord caught the shaft with a hand wreathed in Force and clicked his tongue.

“You still cannot let go.”

At the same time, the tip of his foot struck my wrist.

It was an attack aimed not at the bone, but at an acupoint. Pain like a massive needle stabbing into my veins shot through me, and the spear fell from my grip.

But I did not give up.

*I had been prepared for mutual destruction from the beginning.*

I could not fall from something like this.

Either he died, or I died.

And if even that was impossible, then we would die together, even if I had to throw away my own life to make it happen.

Without the help of the others, it would not have been strange if I had already died several times.

Now it was time to pay back the debt—with interest.

“Hngh!”

With a shout that was almost a groan, I grabbed the Western Heaven Demon Lord’s ankle.

He let out a roar and struck forward with one palm.

Boom!

A small explosion went off inside my body.

Unpleasant internal energy penetrated deep through bone and flesh, tearing my heart meridian to shreds.

My vision blurred, and the strength drained from my legs.

But the hand wrapped around the Western Heaven Demon Lord’s ankle like a shackle continued moving according to the will and instinct carved into my mind.

Krrrk!

I saw the Western Heaven Demon Lord’s eyes widen from the pain.

His Body-Protecting Qi could block my Spear Energy, but it could not prevent his ankle from breaking under pure physical strength.

*Damn it, my hand…*

Of course, I had to pay the price for my own reckless act.

The hand that had seized his Body-Protecting Qi barehanded was blackened as though it had been shocked by high-voltage electricity. On top of that, I had suffered another Internal Injury that worsened my already terrible condition.

At the moment my grip loosened against my will and my body staggered—

“GRAH!”

A belated scream burst from the Western Heaven Demon Lord’s mouth.

His ankle had been wrung like a piece of laundry beneath my tremendous grip. White bone showed through, and the torn flesh was drenched in blood.

No matter how far someone had advanced into the Supreme Peak realm, everyone had limits.

The Western Heaven Demon Lord had displayed unbelievable martial prowess up until now, but he did not possess infinite internal energy or stamina.

And unlike me, he could not recover through Level Ups.

*This is my only chance.*

I charged at the staggering Western Heaven Demon Lord.

I endured the pain that made it feel as though my limbs were being torn apart and drew up internal energy. It flowed toward both my fists, then flared into flames.

Whoooooosh!

“Jin Taekyung!”

Heat filled the space.

The Western Heaven Demon Lord stood right in front of me, calling my name with bloodshot eyes.

His hand was empty, having dropped his sword from the pain, and it was too late for him to block my attack.

If I reached out—if I merely extended my hand—I could inflict a devastating blow on the Western Heaven Demon Lord.

*But then. Then why…*

Why did I feel this way?

I was seized by a strange sensation.

The world had slowed down.

Everything moving within it was so slow that it made me want to yawn.

It was the same sensation I had felt when facing Hwangbo Eom, the Taeeul Merciless Sword.

But this time, the sensation was incomparably sharper. An alarm rang in my mind, and at the same time, I sensed something chilling digging into the back of my neck from behind.

*Ah.*

*So this was it.*

A single realization struck my mind.

I withdrew the hand reaching toward the Western Heaven Demon Lord and twisted my head to the side.

At that moment, time—which had briefly seemed to have its pause button pressed—began moving again.

Swoooooosh!

It was as though a dam had burst. Several things happened at once.

The Western Heaven Demon Lord’s sword, wrapped in ink-black Sword Force, grazed the back of my neck.

When I thrust both palms forward again, the Western Heaven Demon Lord’s fist smashed into my side.

KRAK!

My ribs broke, and blood surged up my throat.

I was sent flying at bullet-like speed, then raised my head with difficulty.

Through my distant, hazy vision, I saw the Western Heaven Demon Lord standing upright.

Perhaps it was because of that strange sensation.

Or perhaps it was because of the pain.

The face I saw was filled not with joy or satisfaction, but with shock and fury.

“You dodged my qi-controlled sword?”

Yes, the art of controlling a sword with qi.

I had forgotten that he could do that, too.

I laughed weakly as I spat out blood.

The Western Heaven Demon Lord’s eyes trembled as he watched me.

“Enlightenment, even in a moment like this… You are someone who must never be allowed to live.”

Enlightenment.

So that was what this was.

I flexed my fingers.

The flow of qi and the sensations running through me were clearer than ever.

Even the pain that already ruled my entire body.

*But it’s too late.*

Step. Step.

The Western Heaven Demon Lord’s approaching footsteps rang like thunder.

I faced his steadily approaching figure with hazy eyes.

Amid the darkness filled with falling stone dust and clouds of dust, the Western Heaven Demon Lord seemed to ripple as a darkness even deeper than the surrounding shadows.

“Supernatural powers. You truly were such a being.”

I bared my bloodstained teeth and laughed.

A wavering voice, like that of a drunk, slipped past my lips.

“Fuck off, you… fucking moron.”

“Farewell.”

The Western Heaven Demon Lord’s eyes flashed red in the darkness.

His hand, wrapped in deep darkness, rose high before slowly descending toward the crown of my head.

Whoooooosh.

And then—

“Do not touch even a hair on him.”

Fwoosh!

Flames bloomed in the darkness, accompanied by a hoarse voice, as though its owner had not spoken in a very long time.

Over the Western Heaven Demon Lord’s rigid shoulder, someone was rising to his feet.

“Take your hands off what belongs to this old man.”

A small frame.

But a presence as immense as a giant.

I laughed, and the Western Heaven Demon Lord groaned.

“The Fire King…!”
## Chapter artifact 364

# Chapter 364

I had a very long dream. A dream of walking through a hundred years of time.

The vagrant who had wandered the continent, begging for scraps, met a master, learned martial arts, and made his name known throughout the world. Then, one day, he saw his former self in a young beggar stuffing a dirt-covered dumpling into his mouth.

“What's your name?”

“……I don't know.”

“Jangcheon. From now on, your name is Jangcheon.”

They were dark, cold memories. On a day when heavy rain poured from the sky, the disciple who had been like his own flesh and blood left, while his master was left behind.

It was only after a truly long time that he returned to the world.

And then…

“You're an interesting fellow. Who did you say you were?”

“Jin Taekyung. Jin Taekyung of the Jin Family of Taiyuan.”

He met someone.

A young brat whose crooked tone and rebellious gaze were impossible to hide, and whom he had disliked for them.

But why had that been?

Whenever he looked around, that fellow was always by his side, and he could never get him out of his mind.

Perhaps that was when his heart had begun to move.

“This old man is already afflicted with the infirmities of old age. Can you learn martial arts from someone like me?”

“Yes.”

“I'll say it again…”

“I believe in you, Old Master. That's enough.”

Light and warmth seeped into memories that had once been dark and cold.

He had never regretted the decision he made that day—not even when he performed the Dance of the Fire God and Demon, which would be his final act in this life.

“How was it? The Dance of the Fire God and Demon. Pretty incredible, right?”

“Yes. It was incredible.”

That single sentence had been enough. He wanted for nothing more. He had avenged his friend and saved his one and only Disciple.

But, unbelievably, the enemy rose again, and that was where his memories ended.

In the darkness where everything had vanished, he wondered.

*Am I dead? Where is this place, where neither Yama nor the dead can be found?*

“Could I be wandering through the underworld?”

The question soon disappeared.

At some point, he forgot the flow of time. He even forgot who he was and how he had lived.

No, it was just as he was beginning to forget.

“Old Master. Did you know?”

Someone's voice echoed faintly in the distance. A voice he had heard somewhere before. Yet they were words he had never heard that person say.

“I always wanted to call you Master.”

He understood.

At the same time, he remembered the person he had briefly forgotten. The sturdy dam of his memories collapsed and swallowed him whole.

“I felt the same.”

Fwoosh.

Flames bloomed.

Both hands wrapped in Blazing Flame tore through the air. The darkness surrounding him in every direction cracked apart, and light seeped through.

The passage was narrow, as though telling him that he was not yet ready to awaken. But without hesitation, he stepped toward the light.

“He's calling for me.”

Fwoosh!

Along with a blinding white light that filled his vision, the Fire King, Jeok Cheongang, opened his eyes.

* * *

“Don't touch even a hair on him.”

His voice was hoarse from not speaking for so long. But when he turned to face him, the Western Heaven Demon Lord could feel it.

The heat contained within that small old man's body.

The flames burning in his eyes.

“Take your hands off what belongs to this old man.”

“The Fire King…!”

The Western Heaven Demon Lord let out a low groan.

Of all times, the old monster from Mount Jiuhua had to awaken now.

Under normal circumstances, perhaps things would have been different. But one of his ankles had already been crushed, and he had expended a considerable amount of strength.

His opponent, meanwhile, was the Supreme Peak master known as the greatest among the Ten Kings.

*This is bad. Very bad.*

At this rate, he might have to brace himself for a fight that would leave them both gravely wounded.

The Western Heaven Demon Lord had no intention of dying here after failing the mission personally ordered by the Lord of Heaven.

*I have no choice.*

His pride as a martial artist stung, but he had to resolve this by the easiest method available.

The Western Heaven Demon Lord bit down on his lip and stretched out a hand. Jin Taekyung's limp body, barely clinging to consciousness, flew into his grasp like a piece of iron drawn to a magnet.

He seized Jin Taekyung by the throat and shook him conspicuously at Jeok Cheongang.

“It would be best if you stopped there. If you want to save the life of your one and only Disciple.”

Thud.

Jeok Cheongang's approaching footsteps stopped abruptly.

The old master stared at the Western Heaven Demon Lord, then slowly parted his lips.

“Have you ever seen such a motherless, fatherless, fucking son of a bitch…?”

“……!”

“Did you hear what this old man said through your asshole? I said it clearly. Don't touch even a hair on him.”

The thick profanity left the Western Heaven Demon Lord momentarily stunned.

Then a sneer spread across his lips.

“Oh, did you?”

At the same time, a stifled groan escaped between Jin Taekyung's lips.

The Western Heaven Demon Lord had tightened his grip.

Crack.

A faint sound of bones slipping out of place echoed through the prison.

Jeok Cheongang's eyes sank deep.

“How dare you…”

“I have many eyes and ears. They all told me the same thing. That the Fire King of the world cherishes his Disciple as though he were his own flesh and blood.”

“……What do you want?”

The Western Heaven Demon Lord answered without hesitation.

“If you don't want to lose your Disciple, kill yourself.”

“Kill myself?”

Jeok Cheongang let out a hollow laugh and opened his mouth.

“You've got quite a bark. Did you learn it from some marketplace mongrel?”

“They say a master and Disciple resemble each other. You're saying exactly the same things as your Disciple.”

The Western Heaven Demon Lord clicked his tongue softly and tightened his grip.

Crack!

Along with a sharper, louder cracking sound, Jin Taekyung's limp toes swung through the air.

Deep furrows appeared between Jeok Cheongang's brows.

“You bastard!”

“This is my final offer. If you accept it, you can save your Disciple and preserve the lineage of your martial school. But if you refuse…”

The Western Heaven Demon Lord continued in a chilling voice.

“I will break this fellow's neck right now and engage you in a life-and-death duel. And most likely, you will be the first to fall.”

This was not a mere bluff.

The Western Heaven Demon Lord knew that Jeok Cheongang was not in perfect condition, either.

That was only natural. Jeok Cheongang had spent more than a month hovering between life and death after fighting the Blood Lord, and had only just awakened.

“What will you do?”

Jeok Cheongang's eyelids trembled.

The old master looked at his Disciple, held in the enemy's grasp, with an indescribable gaze before opening his mouth.

“Promise me… that you will keep your word.”

“Of course.”

It was, of course, a lie.

The Western Heaven Demon Lord had no intention of letting a single person live.

The Sichuan Tang Clan, certainly. The Fire King, Jeok Cheongang. The Divine Physician, who had passed out behind them from the aftereffects of the battle. And…

*The Sleeping Dragon of Shanxi, Jin Taekyung. This one especially must not be allowed to live.*

The Sword Saint's successor was dangerous enough, but Jin Taekyung was particularly dangerous.

If they had fought for another half a shichen—no, even another fifteen minutes—the brat might have gained enlightenment and broken through the wall of the Supreme Peak realm.

It was a blessing that he had defeated Jin Taekyung before that enlightenment could continue.

*The Lord of Heaven is aiding me.*

The Western Heaven Demon Lord barely suppressed the corners of his mouth, which were trying to curl upward.

Jeok Cheongang, who had been staring at him, abruptly opened his mouth.

“Is that enough now?”

The unexpected question made the Western Heaven Demon Lord frown.

“What are you talking about?”

“You sly bastard. You've become even more of a monster since I last saw you.”

“What kind of nonsense are you—”

But the Western Heaven Demon Lord could not finish speaking.

No, he was unable to.

Grab.

Crack-crack-crack!

A fiery pain began at his wrist.

The next moment, reflected in the Western Heaven Demon Lord's widened eyes were his wrist, twisted as though a giant had wrung it, and a young man whose hand clamped around it like a hook.

“Jin Taekyuuung!”

How?

A furious roar filled with pain, disbelief, and shock rang through the underground prison.

But Jin Taekyung did not hear him—could not hear him.

His eyes were hazy, as though he were drunk, and he moved only according to instinct.

Crack!

An irresistible force tore the Western Heaven Demon Lord's wrist out like a weed being pulled from the ground.

A fountain of blood erupted, along with searing pain.

For an instant, the Western Heaven Demon Lord's vision went white.

Then a streak of flame bloomed before him.

“I told you.”

The old master, wrapped from head to toe in blazing hellfire, continued as though spitting the words out.

“Don't touch my Disciple. Not even a hair.”

KABOOOOOM!

A massive pillar of fire surged upward.

* * *

I felt dazed.

As though I could fall asleep at any moment. Or as though I had just woken from sleep.

Everything felt blurred and distant.

*This has to be a dream.*

It definitely was.

The fact that I was alive even though I should have died long ago. The fact that Jeok Cheongang had awakened even though he should have needed several more days before he was ready to wake up.

But…

*Is this a dream, too?*

Ding.

> **System**
>
> - **Jeok Cheongang** has awakened from a long sleep!
> - You have successfully completed all related chain Quests, and your noble devotion and sacrifice will be rewarded!
> - Level Up!
> - Level Up!
> - Level Up!
> - **Stamina**, **Strength**, **Agility**, and **Internal Energy** have been restored!
> - Your physical injuries have been partially restored through a total of three Level Ups!

Ding. Ding. Ding.

The bright ringing of bells echoed around me.

At the same time, an energy like warm sunlight spread throughout my body.

Broken bones fused together, and torn flesh healed. My damaged and shredded organs and acupoints also began returning to their proper places.

Slowly.

But steadily.

Crack.

My toes stepped on empty air.

Before I knew it, the Western Heaven Demon Lord was holding me by the throat.

My burst eardrums should have healed by now, but the sound of the conversation between the two men still felt distant.

*What is this feeling?*

Hummm. Hummm.

A strange noise that words could not describe circled inside my head.

Then, in the next moment, Jeok Cheongang's voice pierced clearly into my ears.

“How long do you intend to stay like that?”

*I don't really know, Old Master. I just… I just can't summon any strength. I don't even know if this is a dream or reality.*

I wanted to answer the familiar face, but no voice came out.

The hand pressing against my throat suddenly felt uncomfortable.

*Then… I should loosen it.*

By the time the thought crossed my mind, my hand had already moved.

My hand shot out so quickly that even I was unaware of it and seized the Western Heaven Demon Lord's wrist.

Crack-crack-crack!

Solid joints collapsed, and a scream burst forth.

Without hesitation, I twisted his wrist and pulled it straight out.

A fountain of blood erupted after the cracking sound.

Before even a drop could reach the floor, a streak of flame crossed the air.

“It's been a while, you reckless little brat.”

The voice stretched out, carrying a hint of laughter.

Hellfire flickered from Jeok Cheongang's palm as it passed by me.

The Flame Divine Palm, perfected to its highest level, slammed into the Western Heaven Demon Lord's chest as he writhed in pain.

KABOOOOOM!

A massive pillar of fire surged upward, scorching the ceiling.

The flames that seemed destined to burn forever were extinguished by ink-colored Sword Force.

Ssssssssh!

“Die!”

The Western Heaven Demon Lord's entire body was shrouded in black clouds.

His lips were soaked in blood, and every blood vessel in his eyes had burst, staining them red.

He looked like a madman, but the power carried by his sword seemed capable of cleaving the heavens.

Whoooooosh!

At the moment the darkness spewed from his blade and shot forward, slicing through the pillar of fire—

“Ugh.”

A small groan escaped between Jeok Cheongang's lips as he tried to draw up his Scorching Yang Qi.

I could feel the qi lying coiled inside his still-unrecovered body waver.

I watched the entire scene with empty eyes.

The darkness rushing toward me through my hazy vision.

Jeok Cheongang's swaying body.

And then—

“Ah.”

A single exclamation escaped my lips.

I was here, and at the same time, I was not.

I could feel and see everything.

Everything surrounding me felt vivid and clear.

*So that's what it was. That's what this meant.*

A blinding flash pierced through my entire body, from the crown of my head to the tips of my toes.

Everything that had blocked me until now cracked and collapsed.

The world that had looked hazy, as though I were drunk, cleared up. My dazed mind became as clear as a summer sky.

At the end of it all, there was a light called enlightenment.

Ding.

> **System**
>
> - Congratulations. You have finally crossed the wall and set foot into a great realm!
> - You have reached the **Supreme Peak** realm!

Ding. Ding. Ding.

Listening to bells that rang louder and clearer than ever before, I took a step.

Space vanished, and the natural qi within it surged.

A fire dragon roared from the spearhead of White Flame as it was drawn through Seizing an Object Through Empty Space.

KRAAOOOOOO!

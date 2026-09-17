# Checkpoint Review — 265–269

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

# Chapters 265–269

## Plot

The Blood Lord regenerates from the wounds inflicted by Jeok Cheongang’s Dance of the Fire God and Demon, revealing that he was responsible for the war that followed Taekyung’s killing of Jin Baekyang. With Jeok unconscious, Taekyung and Cheongpung fight him. Taekyung exhausts his final One Annihilation, while Cheongpung overcomes his fear and chooses to fight rather than retreat. As the Blood Lord is about to kill them, Jongni Chu reveals himself as Sword Saint Mae Jonghak, Cheongpung’s grandfather.

Mae, who has attained higher enlightenment and Returned to Youth, attacks with a divine Thirty-Six Plum Blossom Swords technique. Taekyung restrains the Blood Lord long enough for Mae to sever his remaining arm, but the Blood Lord escapes through black radiance while carrying the Green Jade Buddha Staff. The Life-or-Death Crisis completes, fully healing Taekyung and granting him two levels.

After the Shaolin bloodbath, Henan Province falls into turmoil as the orthodox factions mobilize. Mae treats Taekyung’s allies and publicly confirms his identity. Jeok remains unconscious, while Cheongpung begins recovering. Mae and Taekyung discuss whether Dark Heaven is an independent force, a smokescreen, or a subordinate organization of the Demonic Cult. The Blood Lord, the Temporary Strength Pill, and the Exploding Blood Demonic Art bear the Cult’s scent, but his sorcery is darker and unfamiliar. Hong Dao’s letter identifies Taekyung as the Morning Star who will drive away the darkness. Taekyung returns to Jeok’s room, orders the guards to admit no one until morning, and logs out to rest.

## Continuity

- Sword Saint Mae Jonghak is publicly revealed as Jongni Chu, Cheongpung’s grandfather. He reached Great Completion, attained higher enlightenment, and unexpectedly Returned to Youth.
- Mae’s restored sword can perform a divine version of the Thirty-Six Plum Blossom Swords.
- The Blood Lord escaped through black radiance with the Green Jade Buddha Staff after losing both arms and sustaining severe sword wounds. He possesses extraordinary regeneration and now vows to personally kill Mae, Jeok, Cheongpung, and Taekyung.
- The Blood Lord is the cherished Disciple of an unidentified “that person.” His identity, rank, destination, and connection to the Green Jade Buddha Staff remain unknown.
- The Life-or-Death Crisis completed after the Blood Lord’s escape, restoring Taekyung’s body and granting him enormous EXP and two level-ups.
- Jeok Cheongang remains unconscious after exhausting himself with the Dance of the Fire God and Demon. The Luoyang Strange Physician confirmed that his life is not currently in danger but found no treatment.
- Cheongpung suffered internal injuries but is recovering and can move; he wanted to visit Taekyung as soon as he awoke.
- Song Ho and hundreds of martial artists arrived after the Shaolin massacre, while Peng Cheolhu handled the Shaolin response. Henan’s orthodox leaders are gathering as a larger war appears imminent.
- Dark Heaven’s relationship with the Demonic Cult is unresolved. The Blood Lord’s arts resemble the Cult’s, but his final sorcery is darker and unlike anything Mae recognizes.
- Hong Dao’s letter names Taekyung the Morning Star who will drive away the darkness.
- Taekyung regards Jeok as both his Master and the equivalent of a close grandfather. He has logged out to rest until morning.

## Translation Decisions

- Retain **Blood Lord**, **Green Jade Buddha Staff**, **Sword Saint**, **Returned to Youth**, **Great Completion**, **Thirty-Six Plum Blossom Swords**, **Dance of the Fire God and Demon**, **Life-or-Death Crisis**, **Temporary Strength Pill**, and **Exploding Blood Demonic Art**.
- Render **술사** as **sorcerer** and **술법** as **sorcery**, distinct from movement techniques and lightness skills.
- Use **Luoyang Strange Physician** for 낙양괴의 and **Morning Star** for 신성.
- Preserve Mae’s calm, warm manner toward Cheongpung and Taekyung, and the Blood Lord’s confident, lightly mocking combat tone.
- Render the Yama-related joke as borrowing from **Yama** or **Yama’s debt**.

## Durable state

{
  "active_continuity": [
    "Mae Jonghak is publicly recognized as the Sword Saint despite his Returned to Youth appearance.",
    "Cheongpung can move again and wanted to see Taekyung as soon as he woke; dumplings quieted him.",
    "Jeok Cheongang remains unconscious; the Luoyang Strange Physician examined him but said there was no treatment available for now.",
    "Taekyung considers Jeok both his Master and the equivalent of a close grandfather.",
    "Mae suspects Dark Heaven may seek direct confrontation or may be a smokescreen or subordinate organization of the Demonic Cult.",
    "The Blood Lord, Temporary Strength Pill, and Exploding Blood Demonic Art carry the Demonic Cult's scent, but the Blood Lord's sorcery is darker and unfamiliar.",
    "Hong Dao's letter calls Taekyung the Morning Star who will drive away darkness.",
    "Taekyung has logged out to rest until morning."
  ],
  "continuity_sources": [
    269
  ],
  "open_questions": [
    "Will Jeok Cheongang regain consciousness and recover?",
    "Is the Blood Lord affiliated with the Demonic Cult?",
    "Is Dark Heaven a front or subordinate organization of the Demonic Cult?",
    "Why was the Blood Lord so intent on taking the Green Jade Buddha Staff?",
    "What is the nature and scope of the Blood Lord's unfamiliar sorcery and the method used to make the attackers appear?"
  ],
  "safe_through": 269,
  "temporary_decisions": [
    "Render 낙양괴의 as Luoyang Strange Physician.",
    "Render 술법 as sorcery, distinct from movement techniques and lightness skills.",
    "Retain Morning Star for 신성.",
    "Render the 염왕채 joke as borrowing from Yama or Yama's debt."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 265

# Chapter 265

I was certain—absolutely certain—that he had died.

Even if his breath had not completely left his body, I was convinced he could no longer be considered a living human being.

But…

*Slither. Crack-crack!*

It was a sight I couldn’t believe even while watching it happen.

The skin that had been burned black, so charred it looked ready to crumble at the slightest touch, was covered by pale new flesh. The bones that had jutted out disappeared as they slid back into place.

*What the hell is this?*

What should I even call it? Recovery? No. This was regeneration.

A regenerative ability beyond the limits of humanity—something more like a monster’s.

Cheongpung let out a strangled gasp at the horrifying sight.

“Ah, aah…”

By then, the final change was complete. The face, which had been stripped down to the muscle, rapidly regenerated.

Crack.

The Blood Lord rubbed his neck and flashed us a crooked grin.

“You should have crushed my head. Thoroughly.”

Jeok Cheongang, who had been frozen like a statue, finally managed to part his lips.

“How?”

The Blood Lord answered casually.

“For now, let’s just call it demonic martial arts. To orthodox faction types like you, isn’t it all the same anyway?”

“You… Cough!”

“Old Master!”

I was startled and hurried to support Jeok Cheongang. His face had gone pale, and a stream of red blood ran down his chin.

*This is bad.*

Jeok Cheongang had already exhausted all his strength.

Even the Dance of the Fire God and Demon, performed by gathering up every last bit of his power, had come to nothing. The man in my arms was no longer the Fire King, but merely an exhausted old man.

“R-Run…”

Jeok Cheongang could not finish speaking and lowered his head. I hurriedly checked his pulse. It was faint, but still beating.

*He’s still all right.*

But it was far too soon to sigh in relief.

“By the look of things, even the Fire King of all under heaven has reached his limit.”

The Blood Lord took a step forward, his face filled with delight.

“This was more entertaining than I expected. No, to be honest, it was even frightening. I never imagined things would reach this point.”

“You smell like shit. Shut your mouth.”

I stood, tightening my grip around White Flame, which I had briefly set down.

Jeok Cheongang was already out of the fight. If he expended any more strength here… then something truly irreversible would happen.

“You intend to stop me alone? What a commendable thought.”

“Did you trade one of your eyes for taffy? There are two of us.”

The Blood Lord shook his head.

“No. There’s only one. I don’t count terrified little rats as people.”

*Terrified little rat?*

I turned my head to the side. Cheongpung stood there, frozen.

His pupils were shaking uncontrollably. The hand gripping his sword hilt trembled violently.

*Fear.*

That was the only emotion I could sense from Cheongpung.

“To send a youngster who still reeks of milk out into the martial world. The Sword Saint spoiled his Disciple far too much.”

Step.

He was still more than fifty paces away. But when the Blood Lord took a single step, Cheongpung flinched and retreated as though he had been burned.

*This is…*

My heart sank.

I knew exactly what it meant.

The path I had experienced myself, the path so many others had walked, Cheongpung was walking it late.

*Of all times, it had to happen now.*

It was a growing pain every martial artist and Hunter had to experience, but for the genius standing before me, the timing was unbearably late.

The Blood Lord read the thought on my face and grinned.

“You know it too, don’t you? He’s already finished. The helplessness he feels for the first time, the fear of death… Once you’re caught by things like that, it’s not easy to escape.”

“…Jongni Chu.”

There was no doubt. It was because of his duel with Jongni Chu.

Jongni Chu was the one who had planted the seed of fear in Cheongpung. And that seed had sprouted after meeting another powerful figure—the Blood Lord.

“Exactly. I have no idea where that fellow came from, but he did quite a job. He drew the attention of the orthodox factions and even neatly disposed of the Sword Saint’s Disciple. Ha-ha!”

My mouth felt gritty, as if I were chewing sand.

Cheongpung was still terrified, while the Blood Lord leisurely closed the distance between us with every step.

*Damn it.*

Fortunately, I still had one final move left.

The problem was that it really was my *final* move.

Even if I succeeded, I could not guarantee the result. If I failed, death was all that remained.

*But I have no choice.*

I slowly drew up what little remained of my internal energy—not even ten percent.

One Annihilation—the only way was to pour every last bit of strength into one strike and crush his head.

I neatly folded up the thought *Can I do it?* and burned it away.

*I have to do it. Somehow.*

I had to move with conviction rather than doubt, and with desperate resolve rather than conviction. Only by staking my life on every tiny movement would even the faintest possibility appear.

“Young Hero Cheong.”

*Click. Clack.*

I knew what it was without looking.

The sound of Cheongpung’s teeth chattering.

I shouted with all my might.

“Cheongpung!”

Cheongpung let out a startled gasp and raised his head sharply.

“I won’t say this twice. Listen carefully and decide for yourself.”

“Y-Yes?”

“You have two choices. First, carry Old Master and run as far away as possible.”

“Benefactor!”

“I’m not finished. Second, stop trembling like a coward and fight that bastard with me using every last ounce of strength you have.”

“……!”

His breath trembled with agitation. Then the feet that had retreated several steps began moving forward again.

Step.

We stood side by side in front of the unconscious Jeok Cheongang.

“Your answer. I still haven’t heard it.”

“This is my answer.”

“Be honest.”

“I’m scared, Benefactor.”

“Fuck, you’re brutally honest.”

“But I really am scared. I’ve never felt anything like this before.”

I kept my eyes fixed on the Blood Lord as he approached and asked,

“If you’re so scared, why don’t you run?”

“I don’t know either. I just feel like if I run away from here… I’ll regret it for the rest of my life.”

That regret.

I knew what it meant.

I glanced at Cheongpung. He was still terrified, his hands still trembling, but the feet he had planted forward were firm. He had rooted himself deeply and would not retreat.

Yes.

For now, this was enough.

It was at that moment that I gave a small nod.

“Regret? Run away?”

Twenty paces away, the Blood Lord stopped and laughed aloud as though he had just heard an incredible joke.

“Such audacious nonsense from a pair of fledglings. I’m the one who decides that. That is the right of the strong and the inevitability of the weak.”

“Well, part of that is true…”

I raised my spear and aimed it at him. White Flame’s transparent spearhead shattered the sunlight into countless fragments.

“But why is every single thing that comes out of your mouth such utter bullshit?”

“Truth is uncomfortable. Especially for the weak.”

“That won’t do. Open your mouth, patient. We’re starting your circumcision. It’ll hurt a little since I’m doing it with a spear and no anesthesia.”

“Pfft—ha-ha-ha!”

“You’re laughing? You think it won’t happen to you? But that’s how life goes. I should’ve realized something was up when Mom told me we were going out to eat something delicious.”

The smile around his mouth deepened.

“Sleeping Dragon of Shanxi. The more I see you, the more entertaining you become. Strange martial arts I can’t identify, and plenty of spirit… I like you.”

“If you like me, then?”

“Come under me. I might even spare the Fire King.”

“Why don’t you eat a dick, sir? After today, I’ll never have to deal with a bastard like you again.”

“Who was it that said this? Once is coincidence. Twice is a connection. A third meeting is destiny.”

“Listen to this son of a bitch, acting like he’s writing a romance novel.”

The Blood Lord shrugged.

“Perhaps. It isn’t a relationship between a man and a woman, but if we’ve crossed paths twice in this vast world, wouldn’t that make it a connection?”

“Twice?”

For a moment, I didn’t understand.

What the hell was he talking about?

“Have you ever seen me at the Star-Array Grand Banquet?”

“Of course I have.”

His voice continued, brimming with playfulness.

“At Eight Spring Gorge.”

“…What?”

“It was quite a spectacle. Corpses piled up into mountains and blood flowing like a river… Watching you take Jin Baekyang’s life was particularly memorable. That must have been when people started calling you the Sleeping Dragon of Shanxi, wasn’t it?”

“What are you talking about…”

“Jin Baekyang, the Blade of Flowers. He was a useless bastard. At first, he acted as though he would hand over his liver and gallbladder, but as he grew older, perhaps he developed some ridiculous doubts and ruined everything. What incompetent bastard recruited such a half-assed fool? Tsk, tsk.”

I stared blankly at the Blood Lord as he clicked his tongue. Every word spilling from his mouth sounded hollow and alien.

“Oh, what about that Third Rate sect called the Mount Heng Sword Sect? Is it still around? I did hear from one of my subordinates that one of its Sect Leader’s sons had been killed. I lost interest after Eight Spring Gorge, so I haven’t paid much attention.”

“……!”

A shiver ran through my spine like a bolt of lightning had pierced me.

“Then, you were…”

“I told you.”

The Blood Lord’s eyes curved into crescents. His voice that followed was soft, completely at odds with his appearance.

“Once is coincidence. Twice is a connection. A third meeting is destiny. What do you think? Wouldn’t you say there’s a connection between us?”

For a moment, I couldn’t breathe.

The bastard standing before me was the one who had caused that war.

The Blood Lord saw my expression and guffawed.

“Why the long face? Things worked out smoothly thanks to me. The Jin Family of Taiyuan is the foremost family in Shanxi. You became the Fire King’s Disciple and even seized victory at the Star-Array Grand Banquet. Shouldn’t you thank me?”

I did not answer.

My mind was filled with one thought.

*How many people died again?*

I didn’t know.

A thousand? Two thousand?

Countless people had died in a great war that had been meaningless from beginning to end. There had been no complete victor or loser.

Martial artists who swung their weapons because they were ordered to, and commoners with no connection to the conflict, had died. Even more war orphans were left behind.

When Shanxi’s Murim reeled, the mounted bandits of Gaoyuan ran rampant. Not long after the war ended, the same history repeated itself.

*And he expects me to thank him.*

I licked my dry, cracked lips. My grip around the spear shaft tightened on its own.

An unknown strength filled my exhausted body.

A stat that did not appear in the System window.

Anger.

“Hey.”

“Hmm?”

“You know that bullshit about once being coincidence, twice making a connection, or whatever?”

I took a deep breath. Without it, I felt as though fireballs might pour from my mouth.

“You and I are a different case. Let’s skip straight to destiny.”

“Destiny?”

“Yeah. The destiny for one of us to die.”

Before I had even finished speaking, I kicked off the ground.

The distance vanished in an instant, revealing his smiling face.

*One Annihilation.*

*Gooooong!*

The spearhead cleaved through space.

* * *

Crack!

“Gaaaaah!”

His arm broke, and white bone burst through the skin.

The young man screamed at the unbearable agony unlike anything he had ever experienced. The blood spurting upward splattered across its owner’s face.

The foul smell of blood made nausea rise in his throat. As the young man bent over to gag, a thick leg slammed into his abdomen.

Thud. Boom!

“You pathetic fool. I feel sorry for the Sword Saint, having a half-wit like you as his Disciple.”

The young man was sent flying. Cheongpung struggled to roll his body over.

It hurt.

He wanted to collapse.

His entire body screamed with pain, while a deep sense of despair pressed heavily down on him.

*My body… My body won’t listen to me.*

In the end, he could not stand. He slumped down, and the vast sky spread across his field of vision.

The sky seen from Huashan’s Lotus Peak had always been clear and beautiful. Clouds shone during the day, stars glittered at night, and roe deer and rabbits bounded energetically across the mountain.

But…

*Why is the sky here so red?*

The sky here was different.

Red and bleak.

As Cheongpung blinked, he realized that the tiny blood vessels in his eyes had burst. It was the first time that had happened, but he was not surprised.

*My bones have already broken for the first time, and I’ve lost so much blood.*

Thinking about his condition made his breathing quicken without him realizing it.

As Cheongpung lay sprawled out and gasped for breath, a chilling sound pierced his ears.

*Whoosh—crack!*

“Urk!”

“You bastard!”

Cheongpung turned his head toward the sound. Two figures locked in a bloody battle appeared in his tilted field of vision.

No.

It could no longer be called a fight.

Thud! Thud! Thud!

“Hngh!”

“You’re still not dead? Even after this? Even after this?”

*Bam-bam-bam! Crash!*

His nose collapsed. His ankle broke, and his shoulder was wrenched out of place.

Once. Three times. Ten times…

But no matter what injuries he suffered, no matter how many times he fell, he rose again.

It would be the same even after a hundred times.

That was the kind of person the young man Cheongpung knew was.

*Benefactor.*

Reality was cold, unlike hope.

The outcome was decided almost immediately.

Cheongpung did not know what martial art it was, but Jin Taekyung’s strike had been overwhelmingly powerful. It had shattered the Blood Lord’s red saber, infused with Sword Force, and struck his body.

But in less than a moment, the Blood Lord’s body recovered, and he drove them into a corner.

“Madman… There’s no one else under heaven as tenacious as you.”

Everything was about to end.

The Blood Lord shook his head, looking thoroughly appalled. His entire body was drenched in blood as well.

Unlike before, however, he could no longer heal his wounds. His ever-present relaxed smile had vanished, and he breathed roughly as he pulled Jin Taekyung’s spear from where it had been driven deep into the ground.

“Huff, huff… Fine. I’ll kill you.”

*Kill.*

The moment Cheongpung heard the word, his palm pressed against the ground. The pain from his broken arm and leg, the smell of blood—everything seemed to fade.

Only a sensation of floating remained, dominating his entire body.

*What is this?*

He did not know.

At the end of his staggering steps stood the Blood Lord.

“Huh. What’s this now? Do you want to die too?”

When he met the Blood Lord’s feral gaze, his hands began to tremble.

But when he saw Jin Taekyung lying behind the Blood Lord, the trembling gradually subsided.

“Benefactor. Benefactor.”

“What a bunch of lunatics…”

The Blood Lord let out an incredulous, hollow laugh and swung the spear.

*Slash!*

Cheongpung twisted his body unsteadily, and blood spurted from the front of his chest.

*It hurts.*

But his steps did not stop.

He did not fall.

The sword hilt had long since slipped from his powerless grip.

“What the…”

The Blood Lord stared at him in disbelief before grabbing Cheongpung by the throat with one powerful hand.

“Ghk!”

“What’s wrong with you people? Why are you all making such a fuss as if you can’t bear to die first?”

His voice held genuine curiosity.

Cheongpung opened his mouth as his consciousness began to fade. His voice came out heavily suppressed.

“Because… I think I’d regret it for the rest of my life if I backed down.”

“That’s your reason? A cowardly bastard like you refuses to retreat for such a pathetic reason?”

His killing intent grew even more savage.

But something was strange.

For some reason, Cheongpung was not afraid at all.

As though he had returned to the days he spent on Lotus Peak, he unconsciously lifted the corners of his mouth.

“Hehe. Yes.”

The Blood Lord’s face twisted viciously.

Cheongpung had smiled.

He had smiled while standing before him.

It was impossible. It was something that should never have happened.

“I heard your last words loud and clear.”

He was about to drive the spearhead into Cheongpung’s chest when—

“You’ve broken free of your shell.”

A clear voice rang out.

A voice exactly like the blue sky over Huashan that Cheongpung remembered.

It was a voice he felt he finally recognized.
## Chapter artifact 266

# Chapter 266

“You’ve broken free of your shell.”

A clear voice rang out.

While Cheongpung thought of the sunlight and blue sky over Lotus Peak, the Blood Lord felt a shock that made his heart sink.

He had failed to sense a presence barely two hundred feet away. He, of all people.

His eyes narrowed as he watched a man walking up the mountain path.

*That bastard…*

He had a slender build and an approachable face. He looked like a young man in his mid-twenties at most.

The sword thrust carelessly into his waist without even a scabbard was completely covered in reddish rust.

A dry voice slipped between the Blood Lord’s lips.

“The Always-Victorious Sword?”

The young man, Jongni Chu, smiled faintly.

“I was always worried.”

“What?”

“What kind of storm an innocent child who knows no fear would face after entering the martial world.”

“What the hell are you talking about…”

The Blood Lord was about to continue when he suddenly realized it.

From the very beginning, every word Jongni Chu had spoken and every action he had taken had been directed at only one person.

“But now, it’s all right. You overcame it so well.”

His gaze and voice were warm.

At last, a faint smile appeared around Cheongpung’s lips as he struggled to catch his breath.

Watching that, the Blood Lord let out a hollow laugh.

“Well, look at these two…”

Wasn’t this the same as treating him as though he did not exist?

Him—the man who inspired fear and awe in countless people, even within Dark Heaven.

His grip tightened on its own at the young fledglings’ blatant disregard.

*Crack.*

“Ghk!”

With the sound of bones twisting out of place, a gush of blood burst from between Cheongpung’s lips.

As Cheongpung let out a pained groan and lost consciousness, Jongni Chu’s quiet voice rang beside the Blood Lord’s ear.

“That’s enough.”

The Blood Lord felt much better when he saw Jongni Chu’s face, the smile gone from it.

He grinned and opened his mouth.

“So now you can finally see me.”

“I saw you from the beginning. I just lost sight of you while chasing your disappearing back.”

The Blood Lord frowned as he listened.

“Was it you? That fearless bastard who interfered with me?”

“I was one step too late. It’s unfortunate.”

As Jongni Chu answered calmly, the Blood Lord slowly looked him up and down.

*The Always-Victorious Sword, Jongni Chu. This is that man?*

Jongni Chu had intervened just as the Blood Lord was about to finish off Dharma King Hong Dao. The rapidly approaching presence had forced him to turn away before he could see it through.

*From what I sensed then, his aura was at least beyond the Ten Kings.*

Even the Blood Lord would be in trouble if he were held back inside the Murim Alliance. After withdrawing and leaving the dying Hong Dao behind, that bastard had continued chasing him for quite some time.

*I almost got caught.*

Fortunately, the martial arts the Blood Lord had learned lay far beyond common sense.

And to think that the mysterious master had been Jongni Chu. The Blood Lord shot him a suspicious look.

“You’ve already chased me this far. You’re quick on your feet.”

“Not as quick as you. You were using a movement technique I’ve never seen or heard of.”

The Blood Lord’s eyes narrowed.

His opponent was impossibly young. He also seemed to have a close relationship with Cheongpung, and his martial arts were so outstanding they were difficult to believe.

“You. What relation do you have to the Martial God?”

Jongni Chu habitually stroked his smooth chin.

“The Martial God… I did receive a few teachings from him.”

“Are you his Disciple?”

“Even a suckling infant has something to teach us. Everyone we encounter in life is both our teacher and our student.”

“Stop with the vague Zen riddles. Answer me before I break this brat’s neck.”

But instead of an answer, Jongni Chu gave him a calm look.

His eyes were so deep that one felt they could be drawn into them forever. Yet at the same time, they were as still as a lake on a windless day.

*What is this feeling?*

It was strange. He had only met Jongni Chu’s eyes, yet his hand would not tighten properly.

No—instead, it felt as though his strength was slowly draining away. As though something invisible had seized his wrist and refused to let go.

*This is almost…*

At the thought that followed, the Blood Lord clenched his teeth.

No.

That was impossible. How dare he think of *that person* while looking at some worthless orthodox-faction stray?

*It can’t be. I only need to cut down a bastard like him in one stroke.*

He forcibly steadied his mind. But an unknown unease was rising inside him.

Could he truly defeat this man? Could he escape this place?

The Blood Lord slowly licked his parched lips.

“You… Who exactly are you?”

Dark Heaven’s information network stretched wide and ran deep throughout the land. Yet it had failed to uncover the identity of one person: Jongni Chu.

A mysterious figure whose face and origins could not even be guessed.

Jongni Chu tilted his head.

“Is that important?”

“What?”

“If a few words could make you stop, I would have answered. But you won’t stop.”

His calm voice continued.

“There are still people hovering between life and death. If you don’t want to stop on your own, I’ll have to stop you myself.”

*Slither.*

When he finished speaking, Jongni Chu drew the sword carelessly thrust into his waist. As its horribly rusted blade emerged, a sneer spread across the Blood Lord’s lips.

“You’ll stop me? With that thing that doesn’t even look like a sword?”

“Well, it still seems more useful than one might think.”

“Have you ever cut anyone with that sword?”

“I’ve cut countless people. It’s not a memory I’m particularly proud of.”

“You shouldn’t compare me to some random nobody. Who was the last person you cut? A bandit no better than a slash-and-burn farmer? Or perhaps…”

At that moment, a low voice slipped from Jongni Chu’s lips.

“The Heaven-Poison Demon Lord.”

The Blood Lord’s body abruptly went rigid.

The Heaven-Poison Demon Lord.

No martial artist could possibly be unfamiliar with that title.

During the Great Faction War, he had been an archfiend among archfiends, sweeping across the land while worshiping the Heavenly Demon, leader of the Heavenly Demon Divine Cult, as a god.

The second-in-command of the Demonic Cult that had once devoured half the world.

That was the Heaven-Poison Demon Lord.

But he, too, had been unable to escape the fate of an ordinary martial artist.

One day, after his evil reputation had grown darker with every passing day, he encountered a certain person. The Heaven-Poison Demon Lord met his death that day, and the one who killed him gained a new name.

“The Sword Saint…!”

The Blood Lord’s body trembled as though lightning had pierced through it.

Sword Saint Mae Jonghak.

That name had briefly crossed his mind when he tried to guess Jongni Chu’s identity. But he had soon shaken his head.

It was impossible.

It was something that could never be allowed to happen.

A voice he had barely managed to squeeze out escaped his lips.

“You… How could you…?”

Jongni Chu—or rather, Sword Saint Mae Jonghak—ran his fingers along the blade and answered.

“When the Great Faction War ended, I suddenly found myself wondering what I should do next. I didn’t have to think for long. I simply loved martial arts.”

*Scrape. Scrape.*

Each time the violet force coating his hand brushed against the blade, the reddish rust fell away, revealing the sword’s transparent original form.

“I devoted myself to martial arts without stopping. The child who came to me late in life, like a grandson, became my Disciple, and sometimes he became my teacher as well. The moment I thought I had reached Great Completion, I saw another wall before me.”

Sword Saint Mae Jonghak.

The great martial artist, who had already reached an exalted realm decades ago, had stepped into a new domain once again.

For a man who had already prepared himself in every way, a higher enlightenment had arrived.

“Even I didn’t expect to be Returned to Youth. Anyway, when my body grew younger without warning, I became curious about the outside world. I also found myself thinking about that aggravating grandson of mine who ran away a year ago.”

And so, Sword Saint Mae Jonghak entered the world and traveled throughout the land under the name Jongni Chu.

He was already a figure from the distant past. No one suspected that Mae Jonghak had returned to the body of a twenty-year-old.

Not even Dark Heaven, whose web extended throughout the land.

“It was an enjoyable time. Until you people appeared.”

*Shhk!*

The last of the rust covering the blade peeled away.

At last, the cherished sword regained its true form and cast a cold gleam.

Hundreds, perhaps thousands. A sword that had drunk the blood of countless demon heads pointed toward the Blood Lord.

“This sword is still useful, just as I said, isn’t it?”

The next moment, a violet flash erupted.

*Slash!*

“…Huh?”

The Blood Lord blinked.

In the slowed flow of time, Cheongpung’s body came into view as it slowly fell.

And so did the familiar wrist of someone gripping the neck of the already unconscious Cheongpung.

*That’s…*

*My hand.*

The thought that should have followed was buried beneath the surging blood and pain. A scream burst from his mouth, which had fallen open without his realizing it.

“Gaaaaah!”

But it was not over yet.

As the Blood Lord staggered backward with a scream, a cold voice followed him.

“You’ve piled up sins that can never be washed away. Shouldn’t you pay the price?”

*Whoosh!*

The Blood Lord felt as though every hair on his body had risen.

It was like a hallucination. The entire landscape vanished, and the only thing that seized his every sense was a single sword aimed at his chest.

*Slither.*

A sword drifted through the empty air. The violet qi of the Zaha Divine Technique transformed into thirty-six plum blossoms and scattered in every direction.

Faced with the beautiful sight, the Blood Lord muttered like a groan.

“The Thirty-Six Plum Blossom Swords.”

But it was different.

There was no doubt that it was different.

If the Thirty-Six Plum Blossom Swords Cheongpung had used earlier were a supreme technique, then what Mae Jonghak was displaying now was a divine technique beyond martial arts.

That very divine technique was boring into the vital points throughout the Blood Lord’s body.

*I can’t stop this.*

At that moment, the horrified Blood Lord hurriedly tried to leap away.

*Grab!*

Someone’s hand seized his ankle.

Jin Taekyung, whom he had believed had already exhausted himself and lost consciousness, was grinning with blood-stained teeth.

“Where do you think you’re going, you fucking bastard?”

“You—!”

*Papapapat!*

The Blood Lord could not finish speaking.

Violet flashes filled his eyes. Blood sprayed and flesh was cut apart. The immense agony turned his mind blank for an instant.

“Ghk!”

The difference was on another level. There was no way to block the Sword Energy hurtling across more than a hundred feet.

*Slash! Slash!*

Then, as his consciousness began to fade, a spark flashed in the Blood Lord’s eyes.

*No. If I use that—if I use that, I can survive.*

His mission was already complete. The Green Jade Buddha Staff in his hand—the only one left—was proof of that.

It was unfortunate that he had failed to kill the Fire King, but…

As long as he remained alive—as long as he survived—he could always settle things another day.

He glared at Jin Taekyung with a resentful gaze. Even as he vomited clots of blood, Taekyung was smiling.

“Wait. I’ll kill you with my own hands.”

“What?”

“Stay alive until then. No matter what.”

The Blood Lord’s lips curled upward.

Mae Jonghak, who sensed what he intended, stiffened and sent Sword Energy flying with a rigid expression.

“Stop!”

*Shriek! Slash!*

The Blood Lord’s last remaining arm was cleanly severed from the shoulder.

“Lord of Heaven!”

*Whoosh!*

With a shout, he gathered up the last of his strength and shot forward like lightning. His hard teeth clamped down on his severed arm—or rather, on the Green Jade Buddha Staff it held.

And then—

*Fwoom!*

A black radiance, ominous even to look at, swallowed his entire body.

The Blood Lord vanished along with it.

As though it had never existed in the first place.
## Chapter artifact 267

# Chapter 267

*Fwoom!*

I merely blinked at the black light that exploded like a flash.

That was all I did…

*Where the fuck did that bastard go?*

The shock was enough to make me forget my pain. I stood there with my mouth hanging open.

He was gone. As though he had been erased with an eraser.

The blood spattered around us and the Blood Lord’s wrist, still gripping Cheongpung’s neck, were the only proof that he had ever existed.

*Ding.*

> **System**
>
> - Quest, **Life-or-Death Crisis**, has been successfully completed!
> - You have gained an enormous amount of EXP!
> - Level Up!
> - Level Up!

Along with the System notifications, my body rapidly recovered.

My broken bones knitted back together, and my cut and mangled flesh healed. My empty dantian filled to the brim, and vitality surged through my muscles.

But one thing remained unchanged: my utter bewilderment.

“What the actual fuck was that?”

The Blood Lord. I should have killed that bastard by any means necessary.

I was muttering dejectedly while staring at the ground when a familiar voice spoke, and a hand suddenly appeared in front of me.

“Are you all right?”

I was mentally exhausted, but my body was fine. I grabbed Jongni Chu’s hand and stood up.

“Yeah, I’m fine. I owe you my life.”

“That’s a relief. Then, first, help me tend to the injured… What did you just say?”

Jongni Chu blinked.

His face clearly said, *What did I just hear?*

“Why?”

“W-Well?”

“Is there a problem?”

Jongni Chu stared at me blankly for a moment before waving his hand.

“No, no. What problem could there be? But didn’t you hear… that thing earlier?”

“That thing? What are you talking about? I did pass out for a moment.”

There was a limit to how much punishment I could take. I had been hit, gotten back up, been knocked down again, and gotten back up dozens of times over.

Then, at some point, I took a direct blow to the jaw and briefly lost consciousness.

“When I opened my eyes, it was almost over. I saw that bastard’s ankle, so I grabbed it right away.”

“…I see.”

Jongni Chu moved his lips as though he wanted to say something, then firmly closed them.

I wanted to ask how everything had unfolded—and who Jongni Chu really was—but I held back.

*The important thing is that he’s on our side.*

That was enough for now. There were more urgent matters everywhere I looked.

“Old Master!”

Cheongpung was important, but I was more worried about the elderly Jeok Cheongang’s injuries.

I ran over and examined his condition. His pulse was faint, and his breathing was shallow, but both were still there.

“Would you step aside for a moment?”

After carefully lowering Cheongpung, whom he had finished treating, Jongni Chu placed a hand on Jeok Cheongang’s Mingmen acupoint.

As internal energy flowed into him, I could see the strain ease from his face.

“How is he?”

“His injuries aren’t that serious. He expended too much energy all at once, so he probably won’t regain consciousness for a while.”

“What about Cheongpung?”

“The same. He has internal injuries, but he’s young. He should recover soon.”

“Phew…”

“It’s a blessing in disguise.”

Jongni Chu smiled faintly at my relieved sigh.

That was when—

*Shshshshk!*

Countless presences rapidly approached from below. Their aura was vicious beyond description.

*Don’t tell me there’s another one?*

As I gripped my spear shaft with a hardened expression, Jongni Chu waved his hand.

“Put it down. They’re allies.”

He was telling the truth. Soon, several familiar faces appeared among the hundreds of martial artists at the front of the group.

This person from the Nine Sects and One Gang, that person from the Five Great Families.

They were the people who had occupied the seats of honor during the Star-Array Grand Banquet.

For some reason, however, several key figures—including the Thunderbolt Saber King—were nowhere to be seen.

“Stop.”

The footsteps of the hundreds of martial artists, which had seemed as though they would never stop, came to an abrupt halt in front of us.

The person who had given the order limped toward Jongni Chu and me. Sunlight filtering through the leaves flashed brightly against his steel prosthetic leg.

*The Thousand-Faced Fox, Song Ho.*

As his sharp gaze swept over Jongni Chu and me, I suddenly remembered something I had forgotten.

They didn’t know that Jongni Chu was an ally. To them, Jongni Chu was a public enemy of the Murim who had assassinated Dharma King Hong Dao and brought a bloody storm to Shaolin Temple.

*Step. Step.*

As the Thousand-Faced Fox planted his prosthetic leg, hundreds of martial artists moved with him.

This looked like it was about to turn into a bloody clash over a stupid misunderstanding.

“W-Wait a second. I think you’ve got a serious misunderstanding here…”

I was about to step forward in the ominous atmosphere when Jongni Chu suddenly spoke.

“Thousand-Faced Fox Song Ho.”

“Gasp.”

Was this bastard insane?

At a time when explaining the situation and clearing up the misunderstanding should have been the bare minimum, he had started by speaking informally.

“Hey, hey!”

I hurriedly jabbed him in the side, but it was already too late. A bombshell burst from Jongni Chu’s mouth.

“How’s your leg?”

“…!”

Was he actually crazy?

I couldn’t help staring at Jongni Chu with my mouth hanging open.

This time, he had crossed the line completely. First the casual speech, and now he was mocking a disabled person.

I hurriedly stepped forward before the Thousand-Faced Fox could rip off his prosthetic leg and charge at Jongni Chu.

“I’m sorry. He’s not usually like this. Let me explain. So, what happened was—”

“Hm? I could explain it myself.”

“Explain? What the fuck are you going to explain in this situation? Apologize first, you bastard.”

To hell with him being my lifesaver.

Before things got any bigger, I grabbed Jongni Chu by the back of the neck and forced his head down.

When I raised my own head, I saw the Thousand-Faced Fox’s face, stiff and frozen as though he had seen a ghost.

*He’s really pissed.*

Of course he was. If he wasn’t angry in this situation, he wouldn’t be human. He’d have to be Jesus or Buddha.

But the thoughts spinning frantically in my head as I tried to defuse the situation came to a complete stop when I heard the Thousand-Faced Fox’s answer.

“It’s been a long time.”

Jongni Chu nodded with a genial, old-man-like chuckle.

“It’s good to see you doing well. I thought you would be the first to notice.”

“It took me quite some time. Until two shichen[^1] ago, I thought the Blood Ghost Sword Demon—that damn bastard—had Returned to Youth.”

“Oh dear. You’ve grown old, too.”

“Being able to grow old like this is thanks to you, Great Hero. If you hadn’t saved me back then, I wouldn’t be here.”

The Thousand-Faced Fox laughed as he lightly tapped his prosthetic leg, then continued.

“I discovered Shadow Killer two shichen ago. You were playing a mischievous prank.”

“Ah, that fellow. Come to think of it, it should be about time he woke up.”

“Someone who should have died was alive. That was when I realized I had been barking up the wrong tree.”

“I didn’t want to be found out. I wanted to keep it hidden until the Star-Array Grand Banquet ended, at least.”

Jongni Chu added with a bitter expression,

“I never imagined something like this would happen, though.”

“I feel the same way. Despite taking such thorough precautions, a bloodbath broke out at Shaolin of all places…”

“You wouldn’t be here if the matter at Shaolin hadn’t been settled. Did the Thunderbolt Saber King go?”

“Yes. As soon as he grasped the situation, he divided the forces and moved along two separate routes. Great Hero Peng should be dealing with Shaolin by now.”

“The casualties are too severe. Something that should never have happened has happened.”

“I have much to tell you about that.”

“So do I.”

A heavy silence settled over the area.

I had been listening to their conversation in a half-dazed state, but somehow managed to speak.

“Hey, no. Excuse me.”

Jongni Chu—or rather, *he*—blinked.

“Are you talking to me?”

“Yes. Um, there’s something I’d like to ask you…”

“Ask me anything.”

Hundreds of pairs of eyes poured toward my face. Every one of them looked as though they were thinking, *That lunatic finally came to his senses.*

“May I ask your name?”

The answer came without hesitation.

“Mae Jonghak.”

“…Oh. Mae Jonghak.”

Every hair on my body stood on end.

From our first meeting to this moment, every conversation I’d had with him and everything I’d done flashed rapidly before my eyes.

“I think it’s a coincidence, but your name is the same as someone I know.”

“Is that so?”

I took a deep breath. The sound of my heartbeat rang in my ears like thunder.

*It’s cold.*

A dagger had flown straight into my chest. But don’t worry. There were more people with the same name than you might think.

Maybe he was Fake Jonghak. I clung to that final hope and opened my mouth.

“Do you happen to have an epithet…?”

“The Sword Saint.”

“Ah. Yes.”

*Fuck, he’s the real thing.*

As darkness swallowed my vision, a voice filled with laughter slipped into my ear.

“Let’s stay close from now on. Friend.”

“…”

*I want to die.*

* * *

An enormous cavern whose depth and location were impossible to guess.

At its center, where complex patterns and characters no one could decipher had been carved into the stone, black radiance erupted.

*Whoosh!*

The deep darkness stretched, dimming even the fiercely burning torches.

When the pitch-black darkness vanished a moment later, agitation spread among the dozens of black-clad men surrounding the cavern’s center.

“The Blood Lord!”

“What is going on…?”

Their gazes turned toward a man who was staggering as he bled.

A young man covered in blood, breathing heavily.

Sword wounds covered the Blood Lord’s entire body, and blood gushed nonstop from the severed stumps of both arms.

“Call the sorcerer! Bring the sorcerer here!”

“The Blood Lord has suffered severe injuries!”

As the desperate shouts echoed through the cavern, the Blood Lord slowly opened his mouth.

The severed arm he had held in his mouth until the very end thudded to the floor. Its hand still clutched a short staff.

Even in the darkness, it emitted a faint green light. Someone let out a small gasp.

“The Green Jade Buddha Staff…!”

It was none other than Shaolin’s sacred treasure, preserved for a thousand years.

No one had been able to guarantee the success of their mission. Yet although their superior had ended up in a miserable state, he had completed it splendidly.

Just as expected of the Disciple cherished by *that person*.

“Congratulations!”

“Congratulations?”

The Blood Lord’s eyes glowed red as he stared at the subordinate who had cupped one fist in the other hand and bowed deeply.

*Whoosh—crack!*

The subordinate’s chest was crushed, and he slammed into the wall in a spray of blood.

His body trembled with a wheezing sound, then went still. There was no need to check. He was dead.

“Throw that bastard to the beasts.”

The moment the Blood Lord’s frigid voice left his lips, one of his subordinates hoisted the corpse over his shoulder and disappeared.

This was hardly the first or second time it had happened. They merely felt their superior’s terror once again. Not one of them mourned or became agitated over the death of the ignorant newcomer who had stepped forward.

“Blood Lord, you need treatment first…”

“I’m dizzy. Begin.”

The Blood Lord surrendered himself to the sorcerers who had just arrived.

He wanted to slaughter everything in sight, but barely managed to suppress his murderous impulse.

He needed to conserve his strength for now. He had to recover as quickly as possible so he could tear those bastards apart and kill them.

*The Sword Saint, the Fire King, Cheongpung, and…*

*The Sleeping Dragon of Shanxi, Jin Taekyung.*

The sight of that bastard grinning with his blood-soaked teeth made the Blood Lord’s blood rush to his head.

Unable to contain his fury, he slammed his fist into a sorcerer’s head.

*Boom. Thud.*

The headless body collapsed like a rotten old tree. Feeling the frightened gazes of the other sorcerers, the Blood Lord muttered through clenched teeth.

“I can’t afford to kill any more valuable sorcerers. Continue.”

The treatment, which had briefly stopped, resumed. It was a bizarre sight that defied explanation. Broken bones knitted together, and flesh filled in.

The Blood Lord clenched his teeth against the pain that accompanied the recovery. As his vision began to turn white, one man’s face appeared before him.

*You… I’ll kill you with my own hands. I swear.*

[^1]: A traditional time unit of approximately two hours.
## Chapter artifact 268

# Chapter 268

The death of Dharma King Hong Dao. And the mysterious bloodbath at Shaolin Temple, the Mount Tai and Northern Dipper of the Murim.

Nothing travels faster than the human voice—not even a galloping horse.

Through the mouths of countless eyewitnesses, the rumor spread far and wide.

“Did you all hear the news? About the Star-Array Grand Banquet…”

“Martial artists are surrounding Mount Song. I hear there was a bloodbath at Shaolin Temple.”

Henan Province, which had been buzzing with festive excitement in anticipation of the Star-Array Grand Banquet, was thrown into an uproar.

The elderly were reminded of the Demonic Cult’s rampage across the land several decades ago, while the younger generation realized that the war they had dismissed as a dusty relic of the past had come knocking on reality’s door.

“The Demonic Cult has appeared? That’s terrible. Absolutely terrible.”

“I heard some people say it wasn’t the Demonic Cult, but someone else who did it.”

“Are you saying there’s someone besides the Demonic Cult capable of committing such a thing?”

“I don’t know the exact facts myself. I just heard it while passing by.”

“That can’t be right. They say the leader of the culprits who attacked Shaolin this time was the terrifying Yin-Yang Twin Freaks.”

“The Yin-Yang Twin Freaks? I heard the Heavenly Demon of the Demonic Cult personally made a move.”

“T-The Heavenly Demon?”

As one rumor piled onto another, the story grew like a snowball.

It was only natural that the attention of the people confused by the mixture of truth and lies should turn toward one place.

The former site of the Murim Alliance.

The place where the great and small pillars of the orthodox faction stood.



* * *



“I heard what happened. About Jongni Chu—or rather, Great Hero Sword Saint Mae Jonghak.”

“…”

“Keep your chin up. These things happen in life.”

“…”

“I’m completely broke myself this time, whew… Anyway, that’s how things turned out. But when I heard your news, Captain, I felt my strength surge.”

“Why?”

“Pardon?”

“I asked why your strength surged.”

“Isn’t it obvious? As the ancient sages said, pain becomes lighter when it’s shared…”

*Thwack!*

“Guh.”

Hyuk Mujin bent at the waist with the wind knocked out of him after taking a precise blow to the solar plexus.

When I saw the back of his head sitting wide open, my hand moved on its own. It just moved.

*Smack!*

“Your strength surging? Huh?”

“W-Wait a second. You hit me in the solar plexus. The solar plexus.”

“Your bullshit is making my blood pressure surge. It’s making my blood run backward!”

*Smack-smack-smack!*

After pounding the back of his head like a storm, I finally felt a little better.

I was already troubled enough, and this bastard just had to come along and rile me up.

“The mood is serious right now, so watch what you say. Got it?”

Hyuk Mujin rubbed the back of his head and muttered,

“I was trying to lighten things up because you looked so serious.”

“Just keep quiet.”

“…Yes, sir.”

After silencing Hyuk Mujin, I quietly gazed out the window.

Martial artists moved frantically in every direction, and though no one openly showed it, tension hung thick in the air.

Yet even in the midst of all that, the sky was brilliantly clear.

Hyuk Mujin’s subdued voice pierced my ears.

“This feels strange.”

“What does?”

“Everything. It doesn’t feel real. That only one day has passed.”

“I feel the same way.”

Even the word *tumultuous* wasn’t enough to describe it. Nothing that had happened the day before felt real. It all seemed like a dream.

Hong Dao exhaling his final breath. The sight of Shaolin stained with blood. The appearance of the Yin-Yang Twin Freaks and the Blood Lord. The arrival of Sword Saint Mae Jonghak.

It all flashed before my eyes like a panorama.

*The problem is, this is only the prologue.*

If this were a movie theater, it wouldn’t be strange for the end credits to start rolling by now. But this was nothing more than an ominous prelude.

The vague sense of crisis that everyone anticipated was so palpable I could feel it on my skin.

*Something is changing.*

The world had already become a massive powder keg. The orthodox faction held the fuse, but Dark Heaven had a flint in its hand.

And just yesterday, the fuse had been lit.

I didn’t know how all of this would end, but I could guess what would happen along the way.

*There’s going to be a war.*

A war on an entirely different scale from the one in Shanxi Province.

There was no way the people at the top didn’t know what I had already begun to suspect.

The leaders of the orthodox faction were already fully occupied with containing the aftermath of the incident and holding meetings.

“Come to think of it, Captain, didn’t you attend yesterday’s meeting too?”

I nodded slightly.

The Jin Family of Taiyuan might not compare to the Nine Sects and One Gang or the Five Great Families, but it was still the undisputed hegemon of Shanxi Province.

And since Shanxi Province was where Dark Heaven had first revealed itself, it was only natural that the leaders would take a keen interest in it.

“What did they say?”

“They asked about the Head Elder and the Red Wind Band. I answered everything I knew.”

“The Head Elder is one thing, but the Red Wind Band?”

“The Temporary Strength Pill used by Pung Yang, the Red Wind Band Leader, is connected to Dark Heaven.”

“Ah.”

Hyuk Mujin was now a high-ranking member of his family, so he knew at least some of the circumstances. The same was true of the Temporary Strength Pill and Dark Heaven.

“Did they say anything else?”

“I just left. My eldest brother will hear the important news and pass it on anyway…”

My voice slipped out low without me realizing it.

“I was worried about leaving Old Master alone for too long.”

My gaze, which had been fixed on the window, naturally turned toward one person.

A small elderly man lay on the bed as though he were deeply asleep.

When I took his wrinkled hand, I could feel his pulse. The slight rise and fall of his body told me he was breathing. But even now, a full day later, he still hadn’t regained consciousness.

“When do you think he’ll wake up?”

“That’s the problem. We don’t know.”

“Didn’t some physician with a reputation as a famous healer come by?”

“He said there was nothing he could do. Since Old Master wasn’t seriously injured like the others, he told us to wait and see for now.”

The Dance of the Fire God and Demon. The supreme technique of the Fire Gate Clan.

It possessed enough power to contend with a thousand martial artists, but everything came with a price to match.

For a man well over a hundred years old, there simply wasn’t enough stamina or strength left to endure the aftermath.

*Maybe…*

A thought suddenly occurred to me, but I shook my head and cast it away.

I would put the negative thoughts aside.

The Sword Saint and the physician had both said that his life was not in danger. For now, the best thing I could do was remain by Jeok Cheongang’s side and watch over him.

“There haven’t been any suspicious people while I was gone, have there?”

The Abbot of Shaolin had been assassinated inside the Murim Alliance. No one could be called safe. Just as Jeok Cheongang had protected me from the Blood Lord, I had to protect him.

Hyuk Mujin nodded confidently.

“The Jin Dragon Squad has surrounded the pavilion without leaving a single opening. Don’t worry.”

“The Jin Dragon Squad? The one that’s supposed to be the Taiyuan Jin Family’s elite?”

“Yes. The Lesser Family Head was worried about Great Hero Jeok’s safety, so he assigned me here. Who do you think I am? Hyuk Mujin, Vice Squad Leader of the Jin Dragon Squad.”

“Uh…”

I looked him up and down before subtly averting my gaze.

Hyuk Mujin’s previously confident expression immediately turned sour.

“What was that reaction just now?”

“Nothing. I just realized I shouldn’t leave this place in the future.”

“Don’t tell me you don’t trust the strength of the Jin Dragon Squad, the family’s finest?”

“Now, now. I said that’s not it. Let it go.”

Hyuk Mujin glared at me with narrowed eyes before abruptly standing up.

“Fine. I’ll report to the Lesser Family Head and have them withdraw us.”

“Hey, hey. Why are you putting it like that? Are you going through puberty again?”

“Isn’t it because you’re being so hurtful, Captain? Is this the first time?!”

“Lower your voice. You’ll wake Old Master.”

“It would be nice if he woke up.”

“…”

He had a point.

While I was momentarily at a loss for words, Hyuk Mujin turned toward the door.

It was obvious from one glance that he wanted me to stop him. In moments like this, I had to live up to expectations.

“Hey, where are you going?”

Hyuk Mujin said angrily,

“Forget it. I can put up with everything else, but I won’t tolerate you insulting the subordinates I care about!”

“Gasp.”

“What now?”

“I didn’t expect words like that to come out of your mouth. Mujin, you’ve really grown up. You won’t need circumcision on your mouth.”

“…I’m really leaving.”

“Fine, fine. Sit down. Calm down and have a glass of water.”

“Hmph. No.”

“Ha-ha. Our Mujin really has grown a lot. You made me say it twice.”

“…!”

Hyuk Mujin stopped, then slowly lowered himself onto the chair.

“Even so, I deserve an apology.”

“Huh? An apology for what?”

“For insulting my subordinates.”

“Why should I apologize? I never insulted them.”

“You just said you didn’t trust them. Wasn’t that because you look down on them for being weaker in martial arts than you?”

I took a sip of the cold tea.

“Well, we’re not the Nine Sects and One Gang or the Five Great Families, so of course there’s a difference in level between us and them. But you said the Jin Dragon Squad members are all young and talented, didn’t you? They performed brilliantly yesterday too. Weren’t they the ones who saved Unnamed?”

Shaolin was a great tree. Yesterday’s incident had knocked down a major branch named Dharma King and countless fruits, but the roots remained.

Shaolin’s martial arts. And the existence of Unnamed, who had survived.

Those were its roots.

Ah, didn’t they say an old monk named Hongcheon had survived too?

“That’s right. They fought Dark Heaven without giving an inch.”

Hyuk Mujin puffed out his chest, his face full of pride.

“Exactly. Then what’s the problem? The kids looked sharp enough to me. And they’re deeply loyal to the family. But there’s one thing that bothers me.”

“What’s that?”

“That you’re their Vice Squad Leader.”

“…”

“The subordinates are standing straight on duty down there, while their Vice Squad Leader is up here shooting the breeze?”

“Th-That’s…”

“You said you cared about your subordinates. That you were proud of them.”

“It’s true! Do you know how much I care about those guys…?”

Hyuk Mujin had faltered for a moment, but he quickly pulled himself together and began pouring out words as though he had been waiting for the chance.

“And the mission I was assigned this time is to guard Great Hero Jeok and you, Captain.”

“And before that?”

“Pardon?”

“I asked what your previous mission was.”

“That was obviously guarding the Lesser Family Head.”

“Really?”

I chuckled and pulled *that thing* from inside my robes, then tossed it onto the table.

*Clatter.*

At the metallic clatter, Hyuk Mujin sucked in a breath as he spotted the gold mask gleaming on the table.

“Gasp! W-Where did you get that…?”

“Where do you think? I knew you weren’t usually that kind of guy, but you stuck to me like a bad smell after the preliminaries.”

“Wait a second. You’ve got it wrong. I was genuinely so busy with guard duty I barely had time to open my eyes—”

“A misunderstanding? Fine. Want me to make sure you never open them again?”

*Crack!*

The golden mask crumpled into a little ball, unable to withstand the strength of my hand. Hyuk Mujin’s eyes shook as though an earthquake had struck.

“You were handling an escort at a gambling house, you bastard? You were so famous I didn’t even need to ask around. Apparently, some guy won a hundred thousand silver nyang in one go, then lost a hundred thousand silver nyang right afterward. They were treating him like a legend—no, an absolute legend.”

If even I had heard about it despite the serious mood, that said everything.

I’d even heard a story about one of the servants working at the Murim Alliance hitting the jackpot on Toto—no, Dodo—then slapping the Chief Steward across the face and walking out.

“If you cared about your subordinates that much, you should’ve collected dues and placed the bet with their money. Did you really gobble it down by yourself because you were afraid the payout odds would drop?”

“…”

Silence. Utter speechlessness.

Even if he had ten mouths, he wouldn’t have anything to say. Hyuk Mujin stood there frozen and pale before finally forcing out a few words.

“Life is… all about one big score.”

“…”

This bastard still hadn’t come to his senses.

I stared at Hyuk Mujin in disbelief and raised my fist.

That was when—

*Swish. Tap.*

There had been no noticeable presence or sound.

A young man—or rather, an old man—had risen more than ten jang into the air as though by magic and landed on the windowsill. He grinned and waved.

“Want to talk for a moment, friend?”

*Friend, my ass.*

I let out a deep sigh inwardly as I looked at Sword Saint Mae Jonghak.
## Chapter artifact 269

# Chapter 269

It felt like sitting on a bed of thorns—or rather, walking a thorny path.

Every time I moved alongside Mae Jonghak, the countless gazes flying my way made my face prickle.

Those gazes were filled with awe and curiosity.

Everyone knew now. The young martial artist who had been treated as nothing more than a lucky country bumpkin just days ago was, in fact, a great martial artist known as the Sword Saint.

“Is that really him? Great Hero Mae Jonghak, the Sword Saint.”

“Good heavens, he looks so young. I thought Returned to Youth was nothing more than an absurd fairy tale.”

“As expected of Great Hero Mae Jonghak. He’s turned the Murim upside down.”

The people’s hushed conversations pierced my ears.

“But who’s the guy next to him?”

“That’s the Sleeping Dragon of Shanxi, Jin Taekyung. I heard from someone yesterday that he grabbed Great Hero Mae Jonghak by the neck and talked to him like he was some punk, and—well, you know?”

“Good heavens. At that point, shouldn’t he be called the Mad Dragon instead of the Sleeping Dragon of Shanxi?”

“…”

Fuck. Did I do that on purpose? I didn’t. I just didn’t know.

When I glared at the whispering people, Mae Jonghak burst out laughing.

“It’s all right. Friends can act that way with each other. No need to worry.”

He was killing me twice over.

We moved to a quiet rear garden, away from the crowd.

It was still early spring, but the weather was warm and the flowers were in full bloom. Mae Jonghak walked while gazing at flowers whose names I didn’t know, then opened his mouth.

“First, I should thank you.”

“For what…?”

“I heard you gave Cheongpung a great deal of help.”

“It was nothing worth calling help.”

“I don’t know the details, but if he went so far as to call you his Benefactor, he must have received considerable assistance.”

“…”

He didn’t know the details. He really didn’t know them at all.

I wondered what expression would cross Mae Jonghak’s face if he found out that I had merely given Cheongpung a few candied hawthorn skewers[^1] and earned the title of Benefactor.

“To be honest, I was very worried about that boy. But after meeting you this time, I was able to put my mind at ease. I owe you a debt.”

“Oh. Right.”

I decided not to mention the candied hawthorn skewers. There was no reason to cut into my own flesh when the Sword Saint said he owed me a debt.

“How is Young Hero Cheongpung?”

“He’s recovered enough to move around. The moment he opened his eyes, he threw a fit and insisted on coming to see you.”

“Oh, dear. And what happened?”

“Hmm? He quieted down when I gave him dumplings.”

Twenty years of child-rearing experience hadn’t gone to waste. He knew exactly how to handle Cheongpung.

“And Great Hero Jeok?”

“He still hasn’t regained consciousness. I actually wanted to ask you about that…”

“Ask me anything.”

I had a hard time forcing the words out.

“Is there a possibility that he might never wake up…?”

“Hmm.”

Mae Jonghak stroked his smooth chin.

“What did the physician I sent say?”

“Ah, that man?”

Remembering the old physician who had briefly visited yesterday and looked like a mouse, my mood soured.

“He seemed like a complete quack.”

“A quack? You mean the Luoyang Strange Physician?”

“The Luoyang Strange Physician or whatever. He took a quick look, said there was nothing he could do for him right now, and stormed out. How is that not quackery?”

What kind of old man had such a fierce temper? When I grabbed his arm in sheer disbelief, he screamed so loudly my ears nearly fell off.

He shouted that he would never examine Jeok Cheongang again, leaving me no choice but to let him go.

Mae Jonghak clicked his tongue after hearing the story.

“The Luoyang Strange Physician is a renowned doctor throughout the Central Plains. His personality is as eccentric as his nickname suggests, but there is no question about his skill.”

“Then…”

My heart sank when Mae Jonghak nodded.

My thoughts must have shown plainly on my face, because he patted me on the back.

“Don’t worry too much. If Great Hero Jeok’s life had been in immediate danger, the Luoyang Strange Physician wouldn’t have simply left.”

His words were warm and comforting, but they didn’t completely dispel my unease.

Jeok Cheongang had seemed like he would shake everything off and get back on his feet in no time.

For the past year, he had been my Master, freely passing everything he had on to me. At the same time, he was as good as my own grandfather.

*No. He’ll be all right.*

I forced down the anxiety rising inside me.

A martial artist counted among the top ten in the world and a renowned physician had already examined Jeok Cheongang. For now, the best I could do was trust them.

When I finished thinking, I changed the subject.

“Have you learned anything more about Dark Heaven?”

“Dark Heaven…”

Mae Jonghak gazed at the flower garden with a strange expression.

“I can’t make heads or tails of it.”

“What parts are you talking about?”

“All of it.”

“What?”

“Let me ask you something. Did you notice anything strange about this incident?”

I thought deeply for a moment before answering.

So much had happened so urgently yesterday that I hadn’t noticed it at the time, but there were certainly several things that raised questions.

“There are a few things that seemed strange to me…”

“What are they?”

“For one thing, I don’t understand what those bastards were trying to accomplish.”

“Go on.”

“If Dark Heaven intended to deal a serious blow to the Murim, they should have prepared something much bigger.”

The leaders of the orthodox faction’s Murim had all gathered in one place.

If Dark Heaven’s goal was to destroy the orthodox faction and take control of the world, they should have at least planted explosives.

Whether or not it would have succeeded, it was a perfect opportunity to wipe out the enemy’s leadership all at once.

“Yet only Dharma King Hong Dao and Shaolin Temple had paid the price. They chose clear targets and acted from the very beginning.”

“Coming out into the open like this means they must have made at least some preparations for a fight… Yet it feels like they openly revealed themselves only to pick up iron coins instead of silver nyang.”

Mae Jonghak, who had been listening in silence, suddenly spoke.

“That comparison is wrong. Shaolin Temple is a symbol of the orthodox faction. Dark Heaven destroyed that symbol to make their existence known.”

“Was that really necessary?”

“Several theories have emerged. The first is that they wanted a direct confrontation.”

“Surely not.”

“Don’t underestimate demonic practitioners. They are people ruled solely by blood and power. The Demonic Cult during the Great Faction War was no different. They’re impossible to read.”

Mae Jonghak shook his head and continued.

“The second theory is that Dark Heaven is nothing more than a smokescreen.”

“A smokescreen?”

“Do you know who caused the bloodbath at Shaolin Temple?”

“The Yin-Yang Twin Freaks… Ah.”

“That’s right. They were great demonic figures who made their names feared beneath the Demonic Cult’s banner during the Great Faction War. A great deal of time has passed, but there’s still a strong possibility that they continue to follow the Demonic Cult.”

So Dark Heaven could be a franchise of the Demonic Cult. No, a subordinate organization.

As Mae Jonghak said, it was a possibility that made perfect sense.

But there was one thing that bothered me…

“What about the Blood Lord? Is he part of the Demonic Cult, too?”

“I don’t know.”

Mae Jonghak answered without the slightest hesitation, then scratched his chin.

“The Temporary Strength Pill you acquired, the Exploding Blood Demonic Art used by those who attacked Shaolin, and the Blood Lord himself. They all clearly carry the scent of the Demonic Cult, but… something is different. It has become darker and stranger.”

Mae Jonghak was a living witness to the Great Faction War, having lived through it himself. He must have fought countless enemies and experienced their martial arts firsthand.

In the orthodox Murim, he was one of the foremost authorities on demonic martial arts. His word was practically the established theory of the field.

“Especially that sorcery I saw at the end. Even I had never experienced anything like it.”

It wasn’t a movement technique or a lightness skill. It was sorcery.

I had heard that the Demonic Cult possessed all sorts of bizarre sorceries, but I never imagined something like that was possible.

Even I, who was used to magic, had been left gaping in astonishment.

*Wasn’t that practically magic?*

Martial artists had searched the surrounding area thoroughly, keeping every possibility in mind, but the Blood Lord was nowhere to be found. He had truly vanished as though the earth itself had swallowed him.

“There has also been considerable debate over where such a large number of enemies appeared from. If they can use that kind of sorcery on a large scale…”

“That’s horrifying just to think about.”

Calling it a surprise attack was laughable. If the enemies could appear here and there like Hong Gil-dong, it would be no different from being struck by lightning.

*The leadership must be in chaos, too.*

The atmosphere had already been disorderly when I briefly attended the meeting the day before. By now, it could only have gotten worse.

I was clicking my tongue at the thought when Mae Jonghak asked,

“Have you ever wondered why they were so obsessed with the Green Jade Buddha Staff?”

“Who knows? Because it’s Shaolin Temple’s sacred treasure?”

“They could have just broken it.”

“I think they were more focused on taking it. To be honest, I’m not even sure what they planned to do with it.”

As far as I knew, the Green Jade Buddha Staff was nothing more than a slightly special staff.

I thought it only seemed more impressive because it carried the authority of Shaolin’s Abbot and the history of a thousand-year-old Shaolin Temple.

It wasn’t the Elder Wand or anything. What were they going to do with a glowing green staff?

“Yes, that’s possible. That was what the others thought as well.”

After saying that, Mae Jonghak fell into thought for a while before suddenly speaking again.

“Did you know that Master Hong Dao left me a letter?”

“This is the first I’ve heard of it since I grew pubic hair.”

“Perhaps he sensed his own fate and left some arrangements behind. In the letter, he wrote that you were the Morning Star who would drive away the darkness.”

“…”

“You’re a genius unlike anyone I’ve ever seen. Look around you. Who else your age has reached such a realm?”

I thought for a moment before answering.

“Cheongpung.”

“Oh. I see.”

“…”

“Pung broke through the wall to the Peak realm when he was eighteen. I’d have thought you had done about the same by that age.”

“I was doing well in another sense back then. My epithet was the Night King.”

“Oh, something about being a match for the Ten Kings? Is that what it means?”

“No. I went in and out of pleasure houses too often.”

“Oh. I see.”

“…”

“…”

An icy silence descended.

Mae Jonghak scratched the back of his head, unable to find anything to say, then let out a hollow laugh.

“As expected of my grandson.”

“…I think I’ll be going now.”

As I turned away, Mae Jonghak shouted behind me.

“I’ll drop by again soon! I’ll bring news that will surprise you, too!”

Ugh. Why did I feel so drained?

* * *

“Have you returned?”

When I returned to the room where Jeok Cheongang lay, Hyuk Mujin bowed and greeted me. Unlike before, he looked thoroughly disciplined, and I smiled with satisfaction.

“That’s how you stand watch. You can draw your sword at any moment. What could be better?”

“Of course. I will guard this place like an iron fortress.”

“Yeah. You can go now.”

“Yes, sir!”

Hyuk Mujin was about to hurry out of the room when I spoke.

“Put the gold lump in your sleeve back down.”

“…”

“If it isn’t down by the time I count to three, you’ll be killed today. One, two.”

*Clatter.*

Hyuk Mujin put down the gold mask he had crumpled with his strength earlier and lowered his head dejectedly.

“Ah. You knew?”

“Do I look like an easy mark?”

“Captain, please. I even took out a loan from Yama himself this time…[^2]”

A hundred thousand silver nyang hadn’t been enough, so he had even borrowed from a loan shark. What a lunatic.

I clicked my tongue and tucked the gold lump into my robes.

“We’ll see, depending on how you behave.”

“Gasp. Does that mean…?”

“I’m going to rest now, so don’t let anyone in. Not even my eldest brother.”

“E-Even the Lesser Family Head?”

“That’s right. Tell them I’m exhausted and asleep.”

I looked out the window. The sky was gradually turning red.

“The deadline is tomorrow morning. Can you do it?”

Hyuk Mujin nodded resolutely.

“I will give my life.”

“I know you’re not going to do that anyway, so just do what I told you.”

“Yes, sir!”

Some “yes, sir.”

Hyuk Mujin’s face lit up, and he moved aside with a broad grin.

I gazed at Jeok Cheongang’s face, which looked as though he were sleeping soundly, then lay down on the bed beside him.

*How long had it been since I’d done this?*

The past year had been a nonstop rush. Now, I desperately wanted to ease off the reins a little and return to my family’s embrace.

*Logout.*

Ding.

With the familiar notification sound, my vision went black.

[^1]: Candied hawthorn skewers are fruit skewers coated in hardened sugar.

[^2]: A joking term for a loan so ruinous that it may as well send the borrower to Yama’s realm.

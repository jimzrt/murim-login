# Checkpoint Review — 485–489

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

# Chapters 485–489

## Plot

At the Water God Dragon’s former rampage site, Jin Taekyung discovers that the fissure is a mostly nonfunctional Gate. It cannot be entered or generate a Gate Conquest Quest, but it leaks faint demonic qi and mana. Taekyung suspects that Dark Heaven’s regeneration, Teleport, and Moving Formation are forms of Magic connected to the Gate. He tells Jeok Cheongang that he came from another world and fears that a dangerous force from it is linked to Dark Heaven. Jeok responds by beating him, while privately beginning to fear that Taekyung may be telling the truth.

The crippled Gate’s residual mana has mutated local life. Hyuk Mujin captures roughly a hundred Level 5 Mutated Minnows, locally called Blood Fish, from the sealed entrance waterways. The fish are highly toxic, kill one another, and may still number far more than those captured. The Water God Dragon, a sacred spirit creature far beyond ordinary spirit beasts, absorbed the Gate’s mana; Dongting Lake has since returned to calm.

Jeok asks Mungyeong to protect Taekyung and teach him the mindset and secret martial arts needed for the coming crisis. Mungyeong then reveals his true identity as the Slaughter Saint, history’s greatest assassin. Formerly known as Killing Ghost, he later saved countless people as the Divine Physician. He agrees to train Taekyung without entering a formal Master-Disciple relationship, insisting that he alone will control the training and turn Taekyung into a true Murim martial artist. Taekyung accepts, triggering and immediately completing the Fake Murim Martial Artist Quest through its bizarre “Agh” option.

## Continuity

- The Gate at the Water God Dragon site is mostly nonfunctional, cannot be entered, and cannot generate a Gate Conquest Quest. It continues to leak faint mana and demonic qi.
- The leaked mana has produced Level 5 Mutated Minnows, locally called Blood Fish. About one hundred have been captured; the remaining population is unknown, and the sealed waterways have limited their escape.
- The Water God Dragon absorbed all the Gate’s mana. Its mutated rampage nearly overturned Dongting Lake, which is now calm again.
- Taekyung believes Dark Heaven’s regeneration, Teleport, and Moving Formation are manifestations of Magic connected to the Gate. He has told Jeok that he comes from another world and that an evil force from there may be connected to Dark Heaven.
- Jeok’s innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician’s treatment. He fears he may not survive the coming battles.
- Mungyeong is the Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history. He was formerly called Killing Ghost and later became the Divine Physician.
- Mungyeong will teach Taekyung his secret martial arts at Jeok’s request, but will not become his formal master. Taekyung accepted the Fake Murim Martial Artist Quest.
- Honglan, the Southern Heaven Demon Empress, is traveling toward Yunnan after corrupting the Dongting Lake imugi and causing mass deaths. Her purpose there remains unknown.
- The Dongting Fisherman remains severely injured, and his exact connection to Dark Heaven and the destruction of the secret refuge is unresolved.

## Translation Decisions

- Render 독문 무공 as **secret martial arts**, 사승 as **Master-Disciple relationship**, 살귀 as **Killing Ghost**, and 가짜 무림인 as **Fake Murim Martial Artist**; preserve **Agh** in the Quest interface.
- Render 기억의 파편 as **Memory Fragment**, 게이트 공략 as **Gate Conquest**, 텔레포트 as **Teleport**, 마법 as **Magic**, 혈어 as **Blood Fish**, and 변이된 송사리 as **Mutated Minnow**.
- Retain **Water God Dragon**, **Dark Heaven**, **Gate**, **Force**, **Sword Energy**, **Hellfire**, **Water Breath**, **Old Master**, and **sea of corpses and blood**.
- Render 선천지기 as **innate qi**, 진원진기 as **true-origin qi**, 천기 as **heavenly patterns**, 심마 as **Heart Demon**, 비급 as **martial arts manual**, 송문고검 as **Pine-Pattern Ancient Sword**, 반로환동 as **Returned to Youth**, 강강수월래 as **Ganggangsullae**, 생사부 as **Book of Life and Death**, and 기막 as **qi curtain**.
- Preserve Taekyung’s profane contemporary humor, Jeok’s blunt violence and threats, Cheongpung’s literal innocence, and Mungyeong’s calm, coercive authority.

## Durable state

{
  "active_continuity": [
    "The functionally crippled Gate continues leaking faint mana; its residual mana is mutating local life, and the Water God Dragon has absorbed all of that mana.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, have been captured in the Gate's entrance waterways; the remaining population is unknown, and the fish fight and kill one another.",
    "Dongting Lake is calm again after the Water God Dragon's mutated rampage nearly overturned it with thunder and waves.",
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of Magic connected to the Gate.",
    "Taekyung told Jeok that he came from another world, that an evil force from it is linked to Dark Heaven, that the corrupted imugi was their work, and that a fully opened Gate could release monsters.",
    "Jeok trusts Taekyung more deeply than anyone else, despite interpreting Taekyung's attempted explanation of his origin as a drawn-out declaration that he wanted to die.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people; the severely injured Dongting Fisherman may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense.",
    "Jeok's innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician's treatment.",
    "Mungyeong is the Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; before becoming the Slaughter Saint, he was called Killing Ghost, and he saved countless people as the Divine Physician.",
    "Mungyeong has agreed to teach Taekyung his secret martial arts at Jeok's request, but will not form a formal Master-Disciple relationship; Taekyung accepted the Fake Murim Martial Artist Quest."
  ],
  "continuity_sources": [
    489,
    488
  ],
  "open_questions": [
    "What lies beyond the exposed Gate, why has it lost most of its functions, and how far has its residual mana's mutation spread?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What secret martial arts will Mungyeong teach Taekyung, and what training will make him a true Murim martial artist?"
  ],
  "safe_through": 489,
  "temporary_decisions": [
    "Render 독문 무공 as secret martial arts, 사승 as Master-Disciple relationship, 살귀 as Killing Ghost, and 가짜 무림인 as Fake Murim Martial Artist; preserve 악 as Agh in the Quest interface.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, and 변이된 송사리 as Mutated Minnow.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, and 천기 as heavenly patterns.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, and 기막 as qi curtain."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 485

# Chapter 485

Boom. Boom.

The sound of my heartbeat echoing inside my body was as loud as thunder.

One step, then another. The closer I got to *it*, the harder my heart pounded.

My mouth felt gritty, as though I had shoveled in a handful of sand and chewed it. My eyes, opened wide without me realizing it, felt dry and stiff.

And the moment my hand finally touched the fissure in the cliff, I was able to confirm the true nature of this foreboding.

*Beep.*

> **System**
>
> - This Gate has already lost most of its functions!
>
> - Entry into the Gate is impossible!
>
> - The **Gate Conquest** Quest cannot be generated!

The notification drilling into my ears, the holographic window filling my vision, the gazes of everyone watching me…

In the face of all of it, I slowly uttered a single word.

“...Fuck.”

Crunch.

Before I realized it, my clenched hand dug into the cliff.

The faintest trace of demonic qi flowing from the fissure—or rather, from the Gate—made my vision swim.

*I’d hoped it wouldn’t be this until the very end.*

That damn Gate. It really was a Gate.

How? Why?

Even long afterward, those questions with no answers continued to haunt my mind.

* * *

My thoughts were a mess. I had suspected it might be possible ever since I saw it through the *Memory Fragment*, but when I came face-to-face with a reality this difficult to believe, I couldn’t speak easily.

*A Gate in the Murim.*

This was a gigantic rift. A sign that the laws surrounding this world were collapsing—and the first step toward a disaster.

*Dark Heaven.*

Their true nature was far deeper and darker than I had ever imagined.

Separated from the others, I gazed at the blackened waters of Dongting Lake. Then I picked up a loose stone from the ground and tossed it into the lake.

Splash.

*The bloodshed at Shaolin led to Sichuan, and eventually reached this place.*

The past several months had been one continuous sea of corpses and blood.

While the Star-Array Grand Banquet was taking place in Henan, Shaolin—the Mount Tai and Northern Dipper of the orthodox Murim—was attacked, and the flames of Dark Heaven spread to Sichuan.

The important thing was that inexplicable phenomena had occurred along the way.

*The Blood Lord, the Western Heaven Demon Lord, and the Moving Formation.*

I could still vividly recall the sight of the Blood Lord recovering even after being struck by Jeok Cheongang’s Dance of the Fire God and Demon—a technique that staked his life itself.

*No. It wasn’t even accurate to call that recovery.*

That was right. What the Blood Lord had shown was closer to regeneration than recovery.

New flesh sprouting as if time were reversing. Bones sliding back into place. Everything burned pitch-black like ash regenerating in an instant.

As I watched that unbelievable sight, I had thought of something more familiar than anything else.

*Trolls. Yeah, he was just like a troll.*

Or maybe a potion…

*Damn it. A troll and a potion? What the hell was I thinking?*

What was even crazier was that it might actually have been true.

I picked up another stone and threw it farther.

Splash.

The strange phenomenon the Blood Lord had displayed hadn’t ended there. When the arrival of the Sword Saint put him on the defensive, hadn’t he cried out for the Lord of Heaven before vanishing without a trace?

At the time, everyone had concluded that it was one of the demonic, heterodox arts known as monstrous martial arts and supreme techniques. But now that I knew about the Gate, things looked different.

*Teleport.*

It might have differed slightly from the teleportation I had experienced through Magic Johnson, but if that wasn’t teleportation, I’d burn Hyuk Mujin’s palm myself.

*Come to think of it, there had been more than one thing that didn’t add up about the Western Heaven Demon Lord.*

During the Sichuan Blood Tragedy, the Western Heaven Demon Lord had sacrificed one arm to defeat the Poison King.

But when I confronted him in the underground prison beneath the Sichuan Tang Clan, he already had a new arm.

And no matter how many angles I considered or how many possibilities I went through, there were only two things that could have made that possible.

Either the Western Heaven Demon Lord was a living plastic model, or some unknown power had been at work.

Naturally, the former was impossible.

Though, personally, I wouldn’t have minded if it were true.

*The existence of the Moving Formation was the same.*

The Moving Formation. A wondrous formation capable of transporting hundreds of Dark Heaven’s black-robed men at once.

Dark Heaven was called the successor to the Demonic Cult. If the Demonic Cult had possessed something like that, they would have used it more than fifty years ago.

If they had, the Great Faction War would have ended in victory for the Demonic Cult, and instead of becoming the Third Young Master of the Jin Family of Taiyuan, I would have become the Third Young Master of the Black Dragon Gang—or some other dark-path sect.

*Why hadn’t I realized it?*

Even I, the only outsider in the world known as the Murim, had failed to predict the truth.

The faint suspicion that had occasionally brushed across my mind had been buried beneath the claim that these were monstrous martial arts and supreme techniques from the Thousand-Year Demonic Path. Then it had been erased by the power the Western Heaven Demon Lord called supernatural powers.

But things were different now.

I had confirmed the existence of the Gate. I had realized that the common sense and laws of the Murim, which had gradually become familiar to me, were collapsing.

And I had realized that the strange abilities of Dark Heaven—which martial artists called monstrous martial arts and supernatural powers—could be explained with just one word.

*Magic.*

At the single word filling my mind, my vision brightened, and my forehead, which had been burning hot, slowly cooled.

Along with it, another word referring to an existence that had yet to reveal itself slipped between my lips.

“...Lord of Heaven.”

The one who reigned at the summit of Dark Heaven.

An overwhelming existence whom people like the Blood Lord, the Western Heaven Demon Lord, and the Southern Heaven Demon Empress called themselves lowly servants before.

*What the hell are you?*

Just thinking about the Lord of Heaven made the blood throughout my body feel cold.

If—just if—that bastard called the Lord of Heaven was the very existence I had unconsciously thought of at this moment…

Splash!

“...!”

A spray of water shot high into the air, and the lake rippled.

I snapped out of my thoughts with a start, like someone who had been doused in cold water. When I turned my head, a familiar face had appeared in my vision. I had no idea when he had approached.

“What are you spacing out for?”

His voice was gruff. But the emotion in his eyes, visible between the deep wrinkles on his face, was concern and worry.

I let out a quiet laugh at Jeok Cheongang’s expression and opened my mouth.

“You startled me. What brings you here?”

“You’d been gone for so long, I came to see what you were doing.”

“If you were coming, you could have come quietly. Why did you suddenly throw a rock?”

“Watching you fiddle around with pebbles like a seven-year-old child was making this old man frustrated. Do you have a problem with that?”

“What if I do?”

Whoosh!

Before the words had even left my mouth, I ducked. A vicious sound split the air where my head had been, brushing past my hair.

Jeok Cheongang smacked his lips in disappointment after his attack on the back of my head failed.

“You’ve got remarkably sharp instincts.”

“Do you think this is the first time? I can dodge it with my eyes closed now.”

“Close them.”

“...I’d rather not.”

“You insolent brat. Then why were you so distracted earlier? In the Murim, spacing out like that is a good way to get yourself killed.”

“So you were planning to kill me?”

“Of course. If that’s what you want, this old man can certainly oblige.”

“Then you’ll have to find another Disciple. Oh, wait. Since I’m not actually your Disciple, I guess it doesn’t matter.”

“Ahem. Ahem-ahem!”

Jeok Cheongang forced out several fake coughs before suddenly opening his mouth.

“So what has the idiot with nothing but shit in his head so troubled?”

“I was wondering where to take a shit.”

Smack!

Damn it. I couldn’t dodge that one.

Jeok Cheongang finally succeeded in smacking the back of my head, even using a grappling technique to do it, and glared at me.

“Do you want to shit blood?”

“Why? You said my head was full of shit, and I said I was thinking about shit. What’s the problem?”

“Answer properly before I switch your mouth and ass around.”

“Ah. Yes, sir.”

Rubbing my throbbing head, I thought for a moment before speaking.

“The truth is, I’m not from this world. And I think the evil force that exists in the world I originally came from is deeply connected to Dark Heaven. You know that imugi that went berserk this time? It was all their doing. The rift in the cliff is a Gate. If it ever fully breaks open, monsters will come pouring out.”

“...”

“When that happens, everything is over. Completely over. And there’s probably no way it’s true, but there’s a bastard called Demon King Asmodeus. If he’s still alive and has his sights set on the Murim, then we’re all completely fucked—”

“I understand.”

I swallowed the rest of my words at Jeok Cheongang’s response.

It was a ridiculous story that no one would believe anyway. I had been laying it all out without restraint, but his reaction left me speechless.

“Excuse me?”

“I said I understand.”

“...”

“I understood everything you said well enough. There is no need to say anything more.”

What was with that reaction?

I was so confused that I could hardly think straight. At the same time, an emotion too difficult to describe suddenly surged up from deep within my chest.

*He believes me? He believes this ridiculous story? No… he believes me?*

As I stared silently into Jeok Cheongang’s eyes, my chest suddenly felt full, and my throat tightened.

A little over a year—a period that could be called short or long.

In the old man’s eyes, after we had experienced and endured more together than anyone else, there was something that could be called absolute trust.

*...He trusted me that much.*

Sometimes that happened. I would be seized by some inexplicable emotion, unable to say a word. Unable even to figure out what I should say.

But at that moment, I realized that it was time to say the words I had been turning over in my heart for some time.

“Old Master. No…”

It was the first word I had managed to draw out after a long hesitation.

And as I opened my mouth with a trembling heart, Jeok Cheongang smiled kindly and nodded.

“I understood you perfectly. You sure take a long time to say that you want to die.”

“M—yes?”

“What do you mean, ‘yes,’ you damn bastard.”

Whap-whap-whap!

What the fuck?

My brain ground to a halt. I stared blankly, mouth hanging open, clutching the back of my head as his furious voice rang out.

“Do you take this old man for an idiot? What? You’re not from this world? ‘I Was a Mere Civilian in Another World, but Now I’m a Supreme Peak Master in the Murim.’ Is that it?”

“That title’s surprisingly trendy and pretty good—no, that’s not the point. Just hear me out.”

“I already did. Your last words.”

“Whoa, whoa. Hold on!”

“‘Hold on’? After all the times I’ve beaten you, you still haven’t come to your senses, and now you’re talking to me like an equal again, you insolent little…!”

Whap-whap-whap!

Dozens of palm shadows filled my vision and hammered every inch of my body.

As I felt the searing heat digging into my body, I thought,

*Master, my ass. Fuck.*

I was an idiot for getting moved, even for a moment.

* * *

“If you spout that kind of bullshit again, I’ll tear you in half and kill you. Understood?”

At Jeok Cheongang’s grim death threat, Jin Taekyung—who had been beaten indiscriminately for fifteen minutes—let out a groan.

“Ugh, hold on. I think I’m actually going to die.”

“Quiet. You’re slower than this old man’s grandmother!”

“...Old Master, since we’re on the subject, you don’t happen to sneak your smartphone out and use it whenever you go take a leak, do you?”

Smack!

After delivering one final blow to Jin Taekyung, who had once again spouted something incomprehensible, Jeok Cheongang clicked his tongue and left.

The murderous aura radiating from his entire body made everyone swallow hard and clear a path.

Step. Step.

He walked toward somewhere.

Now alone, Jeok Cheongang wore a complicated expression that was impossible to decipher.

*...That brat. Spouting such incomprehensible nonsense.*

Still, who knew? Jeok Cheongang had never believed in rumors or superstitions—not even a little—in his entire life. But if Jin Taekyung was the one saying it, things were different.

That brat was more special to him than anyone else.

*Come to think of it, he seemed to be about to say something starting with “M—.”*

Could it be? No. Of course not.

Jeok Cheongang sighed and looked up at the moon hanging over the cliff.

Beneath the bright moonlight, he saw someone in the same predicament standing nearby and gazing at the lake.

“Can we talk for a moment?”

At Jeok Cheongang’s words, Mungyeong answered,

“No. Get lost.”
## Chapter artifact 486

# Chapter 486

“Can we talk for a moment?”

“No. Get lost.”

“I see.”

At Jeok Cheongang’s approach without a moment’s hesitation, Mungyeong’s brow twitched.

“I said no.”

“I heard you. So?”

“You really are impossible to reason with. Did you eat your age through your ass?”

“Young punk, you really say anything to an elder. This old man is at least six or seven years older than you.”

“Just how old are you to say some—”

“Thigh meat, you wet-behind-the-ears brat.”[^1]

[^1]: The Korean word *sal* can mean both “years of age” and “flesh,” allowing Jeok Cheongang to twist Mungyeong’s question about his age into “thigh meat.”

“What a goddamn—Forget it. I shouldn’t bother talking to you.”

Mungyeong, who had felt his temper flare for a moment, shook his head over and over.

He looked like a boy—young enough to seem almost childish—but he had also lived a full century or more.

Yet whenever he spoke with Jeok Cheongang, he felt like a child who had lost his composure.

*He’s a master at pissing people off. Master and Disciple really are two peas in a pod.*

With those two—Jeok Cheongang and Jin Taekyung—it seemed entirely possible for them to talk someone to death with nothing but their three-inch tongues.

Compared to them, the old Disciple currently caring for patients in Sichuan was practically the reincarnation of Buddha.

*I miss him. I wonder if he’s doing well.*

As Mungyeong thought about his kind Disciple, Jeok Cheongang approached with a loose, shambling gait and sat down on a rock.

“What were you looking at?”

“There’s no reason I need to answer that.”

“Not a bad choice. Then let’s sit here until dawn. Just the two of us old men, enjoying some quality time together.”

“You understand one thing and miss the other. I can simply leave.”

“You seem to understand two things while missing three. Do you think this old man is only going to do this today?”

“...!”

“Today, tomorrow, the day after tomorrow. The day after that. I’ve already gotten old enough that I barely sleep and spend most of my time bored. This might not be so bad.”

Mungyeong, who had been about to turn away, stopped dead. He stared at Jeok Cheongang with trembling eyelids, then muttered with a sigh,

“You vicious old bastard.”

“Hm. Looks like you’re finally ready to talk.”

“Tell me why you came.”

“This might take a while.”

“Make it as short as possible.”

“‘As short as possible,’ huh?”

Jeok Cheongang gazed at the river, its waters dyed pitch-black, and tossed out a single sentence.

“Look after that brat from now on.”

“What?”

After furrowing his brow for a moment, Mungyeong spoke.

“By ‘that brat,’ you mean Jin Taekyung?”

“Yes. Who else would I mean besides that brat Jin Taekyung?”

“Why are you asking me to do that?”

“Who knows? I’m not sure myself.”

Jeok Cheongang suddenly lifted his head and looked up at the sky.

The full moon hung brilliantly overhead. Its light poured down from that unreachable place, unusually bright.

“I suddenly started wondering how long I’d be able to stay with that brat.”

A hundred years was a very long time.

Mountains and rivers had changed, and dynasties had risen and fallen. And… a young boy had become a white-haired old man.

Mungyeong gazed at Jeok Cheongang and murmured quietly,

“You’ve grown old.”

“Yes. I’ve grown old.”

It was not only the body that grew old and worn with the passing of time. Invisible emotions and the heart itself were also slowly ground down until they disappeared.

A person realized they had grown old when they suddenly thought of death, or wondered how much longer they could remain beside someone.

Just as Jeok Cheongang was doing now.

And Mungyeong was the only person who could understand Jeok Cheongang’s feelings better than anyone else.

“Has the Heart Demon come calling?”

“The Heart Demon? That was a long time ago.”

Jeok Cheongang let out a self-deprecating laugh.

After the former Disciple he had raised like a son grew into a murderous fiend and left, a thick cloud had hung over his heart.

The sorrow and guilt he had felt then had bound Jeok Cheongang’s body and mind like shackles for decades.

Until the light called Jin Taekyung suddenly appeared one day and shone down upon him.

“It’s a painful memory now. I only remember it. It doesn’t hurt anymore.”

“Then why?”

“Because I’ve grown anxious.”

The Heart Demon had no fixed form. It was any obstacle that disturbed the heart and interfered with enlightenment.

The Heart Demon that had seized Jeok Cheongang now was anxiety.

“I wish I’d met that boy twenty years earlier. No, even ten years earlier would have been good… But I met him too late.”

Jeok Cheongang raised a hand and covered the moon. He hated how that bright moonlight—which had not aged even a day, unlike him—illuminated his wrinkled face.

“I’m not what I used to be. Not my body, nor my heart. The only reason I’ve managed to endure this long is because of that boy.”

Jin Taekyung was not the only one who had grown during the year they spent on Mount Jiuhua.

Through teaching Taekyung, Jeok Cheongang had also gained a small measure of enlightenment, and thanks to that, he had managed to halt the rapid advance of his infirmities of old age.

But still—

“You already knew, didn’t you? That my innate qi had been damaged.”

Innate qi, also called true-origin qi, was the source of everything that made up the human body. It was life force itself.

Remembering what had happened in Henan, Jeok Cheongang wore a bitter smile.

“I don’t regret it. I would have done anything to save that boy.”

Jeok Cheongang meant every word. Even if he could go back ten times or a hundred times, he would have made the same choice. The situation had been that desperate.

He had drawn upon the innate qi that was practically his life force to make up for his insufficient internal energy.

The Dance of the Fire God and Demon, which had once dragged the Blood Lord to the brink of death, carried the resolve of an old Master who had burned his own life force as fuel.

“I had fully prepared myself for it. Even if I survived, I knew I wouldn’t be the same as before.”

Mungyeong watched Jeok Cheongang in silence before speaking in a low voice.

“You wouldn’t have been. Not without the Thousand-Year Snow Ginseng that boy brought back.”

“Yes. It was all heavenly luck. Even the fact that he found you.”

But the two men knew the truth.

Not even the Thousand-Year Snow Ginseng, a legendary elixir, or the treatment of the Divine Physician, whose medical skill was said to reach the heavens, could restore Jeok Cheongang’s innate qi.

All of it was merely a stopgap.

Even if one blocked a collapsed dam with a massive boulder, the water trapped behind the dam would continue to seep through a small gap—slowly, little by little, without pause.

“Is that why you came to me? To ask me to look after him?”

“Who knows? What do you think?”

Mungyeong clicked his tongue softly at Jeok Cheongang’s question and continued,

“You’ve grown more worried with age. It wouldn’t be too late to worry about that a few years from now.”

Every person possessed a different amount of qi and a different vessel to contain it.

If an ordinary commoner or Third Rate martial artist was a small stream, Jeok Cheongang was an endless sea.

He would slowly lose strength as his innate qi continued to disappear, but Mungyeong already understood the state of Jeok Cheongang’s body. From his perspective, there was no denying that Jeok Cheongang’s concern was premature.

“This is my body. I know it well. At least I won’t die today.”

“Then stop thinking foolish thoughts and go back. You’d be better off spending this time grabbing that brat and teaching him one more move.”

“But no one knows what might happen tomorrow.”

“What?”

“Do you think I came because I’m worried that my innate qi will gradually disappear and I’ll suddenly drop dead one day?”

Jeok Cheongang stared at Mungyeong’s furrowed brow and continued slowly.

“I can feel it. I can feel myself growing weaker. I’ve already survived several brushes with death unlike anything I faced even during the Great Faction War. Whether someone like me will be able to endure the countless battles ahead… Only some damned bastard watching from up in the heavens knows.”

“...!”

“Hong Dao once said something to me. That the heavenly patterns were becoming distorted, and a calamity greater than the Great Faction War was approaching.”

Dharma King Hong Dao’s prediction had become reality.

Only a year later, Shaolin—the Mount Tai and Northern Dipper of the Murim—had been covered in blood and corpses, and the wise high monk who loved alcohol and meat had met his death.

By then, the dark cloud called Dark Heaven had spread over Henan, Sichuan, and Hubei.

And Jeok Cheongang understood. That dark cloud would soon cover the entire world.

“Listen, Slaughter Saint.”

Deep regret showed in Jeok Cheongang’s eyes as he looked at Mungyeong.

“Things we cannot understand are happening. Everything we knew is collapsing.”

People often compared the Murim to the Yangtze.

*The waves behind on the Yangtze push the waves ahead.* That was why the saying existed.

But the strange phenomena and events Dark Heaven was causing throughout the world now… were not like the Yangtze. They were more like an act of defying heaven itself—turning heaven and earth upside down.

Everything Jeok Cheongang and Mungyeong had known, every law they had understood across more than a century of life, was shattering and collapsing.

*If what Jin Taekyung said is true, then even more so. No. No, that can’t be. It mustn’t be.*

Jeok Cheongang forcibly brushed the thought from his mind as it flashed through it.

It was nothing more than another ridiculous piece of nonsense tossed out like a joke, just as Jin Taekyung always did.

More precisely, that was what Jeok Cheongang wanted to believe.

His body and heart had already grown old and worn. He was not yet ready to accept such a shocking story.

“Anyway, I’m only asking to put my mind at ease. Anything can happen in this goddamn Murim. It would hardly be surprising if an old man growing weaker by the day were to die.”

Mungyeong stared at Jeok Cheongang with a strange look in his eyes.

The giant known as the Fire King seemed unusually small today, and his calm voice as he spoke of a death that could come at any moment lingered in Mungyeong’s ears.

*Asking. He’s asking me.*

It was hard to believe that word had come from the mouth of the Fire King himself.

Mungyeong silently watched Jeok Cheongang rise to his feet.

*Damn. I’ve grown old too.*

Though his body had grown young, his heart was old.

That must have been why one corner of his heart—which had not felt a single drop of rain in many years—was growing damp.

“...Hah.”

Just as Mungyeong let out a small sigh, Jeok Cheongang had already hauled his heavy backside to his feet and was turning away with a wave.

“I’ll be going. Enjoy the moonlight.”

“What?”

What was he talking about?

Mungyeong’s mind briefly stopped working. With difficulty, he opened his mouth.

“You’re leaving?”

“Of course. Shouldn’t you be grateful that this nuisance is leaving?”

“I haven’t answered you yet.”

“What do you mean? I believe I’ve already heard your answer.”

“Wait. What are you—”

“I heard your answer loud and clear, young friend.”

“No, what kind of crazy old bastard—”

The composure that rarely broke came crashing down all at once.

Mungyeong stared at Jeok Cheongang’s retreating back with an incredulous expression and shouted,

“What do you expect me to do?”

“Teach him a few things. The mindset he needs, for example. And if any of your secret martial arts might be useful, slip him a manual.”

“Your secret martial arts? A manual?”

For a moment, Mungyeong wondered if he had heard correctly.

An individual’s or sect’s secret martial arts were practically the crystallized essence of everything they had learned. They were too precious to hand over even for ten thousand pieces of gold and more valuable than one’s life.

Yet Jeok Cheongang was telling him to teach those secret arts to someone else’s Disciple.

Mungyeong asked with complete sincerity,

“...Have you grown senile and forgotten what secret martial arts are?”

“I know exactly what they are. Unless you’re planning to save them for wiping your ass, why don’t you teach him?”

“You insane bastard.”

“You don’t have anyone else to teach them to anyway. Let your old Disciple in Sichuan keep saving people, and teach our boy how to kill properly.”

Was that something he could say with a straight face?

Mungyeong was so dumbfounded that he lost the power of speech. Meanwhile, having finished saying everything he wanted to say, Jeok Cheongang was already sprinting away into the distance.

*Whoosh!*

“What the… Goddamn it.”
## Chapter artifact 487

# Chapter 487

After confirming the Gate’s existence, my thoughts had been a mess, but Jeok Cheongang’s help had cleared them right up.

“...”

Actually, screw that. It wasn’t help. He had beaten me so thoroughly that every joint in my body ached.

When I encountered Hyuk Mujin later, he saw me groaning and gave me a thumbs-up.

“Wow, as expected of you, Captain! You can still get back up after taking that kind of beating!”

“Mujin.”

“Yes?”

“Put that thumb away while I’m still asking nicely. Before I pound the top of your head and turn you into Thumb Princess.”

With my Strength, a compression press would be totally doable.

I had no idea what exactly a Thumb Princess was supposed to be, but the murderous atmosphere had clearly gotten through to him.

Hyuk Mujin hastily lowered his thumb and muttered,

“He’s always picking on me. If only he’d stayed laid up with his injuries...”

“Mujin, what did you say?”

“I was saying that the Captain has risen rapidly to become a Morning Star of the Murim!”

“...”

Look at that heartfelt lie.

It would not be an exaggeration to say he had elevated quick thinking to the realm of art. Feeling a sudden pang of pity, I patted Hyuk Mujin on the shoulder.

“Yeah. You hang in there, too. You’ve been shooting up lately.”

“Me?”

“Yeah. I heard it in the marketplace on the way here.”

Hyuk Mujin might be treated like a nobody here, but he was a martial artist who had earned the impressive sobriquet Swift Wind Sword after helping the Jin Family of Taiyuan pacify northern Gaoyuan.

And since he was always walking around with a blue-chip stock like me, his own stock had naturally begun to rise as well.

“Listening to the commoners talk, you sounded like some legendary war hero.”

“Ahem. Is that so?”

“Yeah. At least a Supreme Peak master. If that isn’t shooting up, what is?”

Hyuk Mujin had been grinning happily when he suddenly looked me up and down suspiciously.

“What’s with that disrespectful look?”

“I thought you might say I was on the rise, then hit me and leave me laid up.”

“...You crazy bastard.”

It was a decent scenario, though. But still, was my image really that bad?

*Come to think of it, I have beaten him quite a lot.*

I suddenly felt sorry for him. How many times had he been hit for him to develop this level of persecution complex?

I gazed at Hyuk Mujin with pity, let out a deep sigh, and spoke.

“No. I told you, I heard it in the marketplace myself.”

“Really? You swear on everything?”

“I stake both your balls.”

“Oh. I guess it must be true, then. At last, the fame of the Jin Family’s prodigy, the Swift Wind Sword Hyuk Mujin, has spread throughout the Murim—”

Hyuk Mujin, who had been grinning from ear to ear, suddenly stopped.

“Wait a minute. Something feels wrong.”

“What?”

“Why are you staking my balls?”

I answered calmly.

“Because they’re your balls, obviously.”

“What? Why is that obvious?”

“Because you’re Hyuk Mujin.”

“What the hell does that even mean...”

His expression was a sight to behold.

If I lost every single one of the countless bets I had made involving Hyuk Mujin, saying that even thirty balls wouldn’t be enough would hardly be an exaggeration. There was no need to spell that out.

“Want to cut one off and plant it? A tree might grow.”

“Plant what?”

“What else?”

Following my gaze, Hyuk Mujin answered with the expression of someone looking at a lunatic.

“I’ve never heard of a tree like that.”

“That’s why you’d be the first.”

“I’ll leave that honor to you, Captain.”

“Enough. What were you doing that you only showed up now? You were nowhere to be seen earlier.”

Immediately after the Water God Dragon fell, we had split into two groups. Cheongpung and Hyuk Mujin had followed Zhuge Feng, so this was the first time I had seen them in exactly two days.

At my question, Hyuk Mujin shook the net he was holding.

“What’s that?”

“Fish. I’ve been capturing them.”

“Fish?”

“Yes. I’ve been catching them since yesterday, but it hasn’t been easy.”

Well, obviously. How hard could catching fish be?

I looked back and forth between Hyuk Mujin and the net, where fish were thrashing around, then nodded faintly.

“I see. Our Mujin was busy fishing.”

“I’m not joking. These things are so violent and strong that they’ve nearly drained me dry—”

*Smack!*

“Gah!”

“You call that draining you dry? You abandoned your direct superior, the person you’re supposed to serve with all your loyalty, and came here to enjoy fishing? Just looking at you is draining me dry!”

Hyuk Mujin staggered backward while clutching his head, then shouted furiously,

“That’s not what you think!”

“You dare raise your voice at me? You said you were catching fish, didn’t you?”

“It wasn’t fishing! It was capturing! Capturing!”

“Capturing? Young Hero Cheongpung, capture this bastard!”

“Ah! Yes, Benefactor!”

Cheongpung, who had been loitering nearby, rushed over and seized Hyuk Mujin.

How could Hyuk Mujin possibly resist the grappling technique of Huashan’s Morning Star, a Supreme Peak master who had inherited the Sword Saint’s legacy?

I looked down at Hyuk Mujin, who had been subdued without the slightest resistance, and solemnly declared,

“Even if the Murim perishes tomorrow, I shall plant a single testicle tree.”

“Wait. Wait!”

“I have a question. Is the left one yours, or is the right one yours?”

“They’re both mine! What kind of bullshit is that?”

“You’re an honest fellow. As a reward, I’ll take both.”

“Let go! I said let go! You crazy bastards!”

That was exactly when Hyuk Mujin’s screams rang through the air.

*Hiss!*

“If we bury it somewhere sunny, it’ll grow nice and strong... Whoa, that startled me.”

It happened in an instant.

Something long and pure white shot out of Cheongpung’s arms like a streak of light. Cheongpung immediately sprang to his feet, releasing Hyuk Mujin.

“Where are you going, Mimi?”

“Phew!”

Finally freed from Cheongpung’s hold, Hyuk Mujin pointed at the net he had dropped on the ground and shouted,

“Capture! Not fishing—capture! See for yourself!”

As it turned out, Hyuk Mujin’s protests were pointless.

The moment Mimi sprang out of Cheongpung’s arms and headed for the net, my gaze had already locked onto her.

And the moment I saw the scene unfolding before me, a single thought crossed my mind.

*One mountain after another.*

*Hiss! Snap!*

Mimi flicked her tongue, slipped between the gaps in the net, and tore into one of the fish’s gills.

*I’m not even sure that thing should be called a fish.*

*Thud! Flap-flap!*

Its eyes were bright blood-red. Its teeth were sharp as saw blades, and its body was larger than an adult man’s forearm.

And on its tail… Fuck. What the hell was that?

“...A spike?”

I stared at it in disbelief and muttered.

Hyuk Mujin, who had gotten back to his feet while panting, answered gruffly,

“You may be hard of hearing when it comes to what people say, but your eyesight is excellent.”

“What kind of fish has a spike on its tail?”

“Maybe it’s a special weapon.”

“...Are you going to keep talking bullshit?”

“I told you, didn’t I? What fishing? Fishing, my ass. It was capturing. Capturing! How could you catch something like that with a fishing rod?”

“Huh.”

Capture. Now that I heard it again, there really was no better word for catching something like that.

Grumbling to himself, Hyuk Mujin walked over and picked up the net he had dropped. I only realized it then, but it wasn’t an ordinary net. It was a metal mesh reinforced with iron and steel.

“What the hell is that?”

“As you can see, their teeth are incredibly sharp. An ordinary net would be cut apart with a single bite—”

“I’m not talking about the net. What are the things inside it?”

“Oh.”

*Clang!*

Hyuk Mujin frowned as the things inside thrashed violently, nearly tearing the metal mesh apart.

“For now, everyone calls them Blood Fish.”

“Blood Fish?”

“Yes. Because their eyes are blood-red.”

Blood Fish. It was certainly a fitting name for their sinister appearance. But I wanted to know the exact name of these grotesque creatures.

*Qi Sense.*

*Whoosh... Beep.*

As the wave of Qi Sense spreading from me reached them, a System notification appeared, and Level windows rose above their massive bodies.

> **System**
>
> **Level 5 Mutated Minnow**
>
> - A new fish species has been discovered!
>
> - Information on **Mutated Minnow** has been updated!
>
> **Item Window**
>
> **Mutated Minnow**
>
> **Type:** Fish
>
> **Grade:** None
>
> **Restriction:** None
>
> **Description:** A mutated species born from exposure to weak mana. It has grown incomparably stronger and possesses considerable toxicity, but it might taste delicious once cooked.

“...”

*This is a minnow?*

I stared at the thing, which was larger than an ordinary adult man’s forearm.

*Where did the minnows I know go?*

*At this point, they might as well tell me this isn’t Dongting Lake but the Amazon.*

First, I was shocked that this monster was a fish with a Level as high as 5. Then I was shocked all over again by the System window’s bullshit saying that it was incredibly strong and poisonous but might taste good.

*It might taste good once cooked? You said it was poisonous, you crazy bastards.*

*Still, there could only be one cause.*

This transformation had undoubtedly been caused by the mana flowing out of the Gate.

The Water God Dragon had sacrificed itself to absorb most of the Gate’s mana, but it couldn’t have done anything about the residue.

And according to what I had confirmed personally just one or two shichen earlier, the Gate was still leaking a faint amount of mana despite having ceased to function.

*What will happen if things like these spread throughout the world? What if they’re contagious?*

I already knew the answer to that question.

*We’d be fucked. That’s what.*

The tributaries of Dongting Lake flowed into the Yangtze, and the Yangtze was both a vast natural ecosystem and a maritime route traveled by countless people.

I wasn’t part of some environmental organization, so the destruction of the ecosystem was a secondary concern. But if some infectious agent caused mutated creatures to flood onto land, then it would be the end of everything.

“...This is driving me insane.”

“Why do you say that?”

“Benefactor. Are you all right?”

“No. Not even a little.”

I answered firmly and turned toward Cheongpung.

“Young Hero Cheongpung, how many of these things are there?”

“I wasn’t assigned to this area, so I don’t know. But Mimi likes them. They must taste good!”

Cheongpung gazed at Mimi with an expression of utter adoration. She had already swallowed a Blood Fish several times larger than her own body.

“Eat lots, Mimi!”

“...Right. Asking you makes me the idiot. Then, Mujin.”

“Yes. We’ve captured around a hundred Blood Fish so far, but we haven’t determined how many more there are.”

I never knew the presence of a normal person could be this comforting.

I looked at Hyuk Mujin with a deeply moved expression and asked again,

“Great Hero Zhuge Feng knows about this too?”

“Of course. As soon as the Blood Fish were discovered, Great Hero Zhuge Feng ordered the waterway by the entrance to be completely sealed off.”

“What about the Blood Fish that already escaped?”

“Well, for now, it seems there are hardly any.”

“What?”

According to the past I had glimpsed through the *Memory Fragment*, the Gate had opened at least a month ago.

Judging by the fact that the Gate was still leaking faint mana, a considerable number of fish should have mutated by now...

“Are you sure?”

“It’s just a guess, but they were fighting one another.”

“Fighting?”

“They’ve become so ferocious that they seem to have lost the concept of allies. They’re probably killing one another even now.”

“...”

*Should I be happy about this or not?*

Their ferocity meant they were dangerous, but since they had started a war among themselves and were reducing their own numbers, it was certainly something to celebrate.

*At least that’s a relief.*

I had just let out a sigh of relief when—

“There you are, Young Master Jin.”

A clear, infuriatingly sweet voice came from behind me.

When I turned around, Mungyeong was already standing there and looking at me.

“They’re looking for you.”

“I’m busy. The grown-ups are working, so wait.”

“...I was told to bring you no matter what. They have something to say to you.”

“Who?”

A murderous Sound Transmission bored into my ear.

—Me.

“...Oh.”

Then I had better go.
## Chapter artifact 488

# Chapter 488

The Water God Dragon was definitely a sacred creature.

In the broadest sense, it could be called a spirit beast. But it possessed power far beyond that of ordinary spirit beasts, which was probably why it had been able to absorb all the mana from the Gate.

*You could tell just by looking at the weather.*

As expected of an imugi that had lived for five hundred years, there was something different about it.

When the Water God Dragon had rampaged in its mutated state, thunder and waves had nearly overturned Dongting Lake. Now, however, the lake was calm, as though nothing had ever happened.

But unlike the peaceful-looking Dongting Lake, my heart was being swept by raging waves.

*...Is this what they mean by the calm before the storm?*

I glanced at Mungyeong’s back as he walked ahead of me.

He was a head shorter than me and had a slender frame. But in reality, he was a beast wearing the hide of a harmless herbivore.

*Why did he suddenly call me out? What could he possibly want to say?*

This was so unfair.

Could he still be angry because I had spoken casually to him during the battle?

He hadn’t called me out here just to have a little “physical conversation,” had he?

My unease continued to grow as Mungyeong kept leading me toward increasingly secluded places.

That was when—

“Stop.”

*Whoosh!*

There was only one voice, but seven figures surrounded us.

They were all Peak masters with considerable internal energy, and each had a sword hanging from his waist. The blades were engraved with pine patterns.

*Pine-Pattern Ancient Swords.*

As expected, a middle-aged Daoist dressed in Wudang robes emerged from beyond the deep darkness.

Judging by his age, the middle-aged Daoist was clearly their presiding chair. He opened his mouth toward us.

“This area is closed to visitors after the hour of the Dog. Please turn back—No, wait a moment. Could that be the Blazing Flame Divine Dragon?”

“What?”

The middle-aged Daoist spotted me over Mungyeong’s shoulder and asked with wide eyes,

“Young Hero Jin Taekyung? No, Great Hero Jin Taekyung?”

“I’m no Great Hero, but my name is Jin Taekyung.”

“Oh! My guess was correct after all. I knew your face looked familiar.”

*You may recognize me, but you’re a complete stranger to me.*

The middle-aged Daoist seemed delighted to see me, as though I were his son who had just been discharged from the army. Then he suddenly remembered something and asked,

“But what brings you here at this late hour? You must have already been assigned temporary lodgings.”

“...Uh. Well.”

*I was being dragged away by the Slaughter Saint.*

I swallowed the words rising to my throat and was about to make up some vague excuse when a flash of insight passed through my mind.

Thinking about it again, this was the final escape opportunity God had granted me.

“Is this where access is restricted?”

“That’s right. We’re taking turns standing watch in case of an emergency. But who is this young-looking man accompanying you?”

“Slaugh—”

“Hm?”

“—The breeze is blowing softly.”

“Oh, ha ha. I see.”

*Slaughter Saint! Mister! That bastard is the Slaughter Saint!*

I could finally understand how the barber who shouted that the emperor had donkey ears must have felt.

But when I met the deep, predatory gaze of the beast standing before me, I forced a smile and answered,

“We simply got to know each other somehow.”

“If you know each other, then precisely what kind of—”

“We met in Sichuan and have traveled together ever since. He isn’t a martial artist. He’s a medical apprentice.”

“Ah. I remember now. I heard there was a young medical apprentice with the skills of a renowned physician. So this is him.”

“Yes. This is that fellow.”

“But why did you come all the way here at such a late hour?”

“Uh, we have something important to discuss.”

“You must be quite close.”

I could let the other things pass, but I couldn’t accept that.

I answered with a straight face.

“No. We aren’t close.”

“Hm. In that case, I’m afraid there’s a problem. I apologize, Great Hero Jin, but regulations require a reliable guarantee before we can allow anyone through—”

“Ah, I see. Thank you for your hard work. Mungyeong, let’s go!”

—Instant execution.

“...”

—Back in position.

The Sound Transmission stabbed into me with icy force.

I had already turned halfway around, but I helplessly turned back.

—Say we’re close.

“I was joking. We’re actually very close.”

The middle-aged Daoist looked back and forth between Mungyeong and me before muttering,

“You don’t seem very close. You were walking apart without saying a word to each other...”

—Answer properly.

“We’re the kind of people who understand each other just by looking into one another’s eyes.”

“But you turned your head away. How could you see each other’s eyes...?”

“We used to understand each other just by looking into each other’s eyes. These days, I can tell what he’s thinking just by looking at the back of his head.”

“...”

—I’m asking this out of genuine curiosity. Does the Fire Gate Clan’s sect rule say to recruit only fucking idiots?

*For fuck’s sake. What am I supposed to do?*

As the middle-aged Daoist stared at me with lukewarm eyes, Mungyeong’s Sound Transmission continued.

—Come closer.

“...?”

—Put your arm around my shoulder.

“...!”

*What am I, some kind of avatar?*

But what could I do? In the Murim, the strong were the law—and the gods.

I trudged over, draped an arm over Mungyeong’s shoulder, and put on a dying expression.

“Whew. We’re really close.”

—Smile.

“Ha ha ha! We’re really close!”

—Make it louder.

“Wahahahahaha!”

—I can see you signaling with the corner of your eye. Do that one more time, and I’ll make you see the world with your heart instead of your eyes.

He had found a remarkably elegant way to say he would dig out my eyes.

I gave up my desperate attempts to look sideways and muttered,

“Anyway, we’re close.”

And throughout this entire situation, the Wudang martial artists—including the middle-aged Daoist—stared at us with expressions suggesting they were watching the greatest horror movie of the summer.

I had put on a dying expression, then laughed like a madman, all while constantly sneaking glances at Mungyeong. Anyone who failed to notice something strange would have to put down their Pine-Pattern Ancient Sword and leave Wudang.

The middle-aged Daoist soon moved his lips, his face suggesting he had made some kind of decision.

—Perhaps I’m worrying over nothing, but if something is happening to you without your realizing it, blink three times. If nothing is wrong, blink twice.

—I heard everything. Blink three times, and your body will be cut into three pieces.

*Mister! You bastard! This bastard is the Slaughter Saint! This bastard has a wiretap in his ear!*

But my shout never escaped, and I quietly blinked twice.

No matter how suspicious they became, there was no way they would guess that the young medical apprentice before them was a Supreme Peak master who had Returned to Youth.

And if I looked at things objectively, the Slaughter Saint was clearly an ally.

—Are you sure?

Even if he asked, my answer had already been decided.

Even among Supreme Peak masters, Jeok Cheongang and the Slaughter Saint were on a different level of enlightenment, making them biological wiretaps capable of eavesdropping on other people’s Sound Transmissions.

—Yes. Why would I lie about something like this? We’re simply friends who built a friendship while traveling together.

Though someone seemed to have built up murderous intent instead of friendship.

Still, something had been built.

The middle-aged Daoist let out a quiet snort of laughter after hearing my Sound Transmission.

—Indeed. How could anything happen to the Blazing Flame Divine Dragon of all people? Great Hero Jin, please forgive me for being so suspicious. I suppose the recent events have made me more sensitive than usual.

*No, you’re insensitive. Please get just a little more sensitive.*

But contrary to my hopes, the middle-aged Daoist spoke with a warm smile.

“In that case, very well. If it’s Great Hero Jin and no one else, I can trust you. You may pass!”

“W-Wait a moment.”

“Ha ha. I wondered why you had come all the way here, and it seems you truly have something important to discuss. I understand. Regulations prohibit it, but... I’ll give you some privacy for a little while.”

“What?”

“About half an hour. Will that be enough?”

*Of course it won’t, you idiot. Enough for what?*

But before I could answer, Mungyeong bowed politely with a clear smile.

“That will be sufficient.”

“...!”

Why did that brief answer sound like a death threat to me?

The middle-aged Daoist did not notice my trembling eyelids. He stroked his beard and smiled warmly.

“What a polite young man. You should examine me sometime as well.”

“Of course, Daoist.”

“Ha ha. Then I’ll return in half an hour.”

*Whoosh!*

The seven Peak masters—including the middle-aged Daoist—or rather, the seven witnesses, shot away.

I stared blankly at their backs as they rapidly disappeared into the distance. Then I slowly turned around, feeling layers of qi barriers enclose the area around us.

Sound and impact.

All of it was cut off from the outside by the qi curtain that now surrounded the space.

And within that space was a pair of eyes emitting a sharp, icy light even through the darkness.

“Master and Disciple are exactly alike in the one thing that makes people tired.”

“...!”

The voice alone made my chest turn cold.

The young man who had looked like an innocent medical apprentice had transformed into the greatest assassin in history. He leaned his back against a large rock.

He released no aura of qi, but I could still feel them—the countless blades concealed throughout his body.

*The Slaughter Saint.*

This was Mungyeong’s hidden name and his true nature.

I didn’t know what he had been like in the past. But I would stake Hyuk Mujin’s balls on this: even after spending more than forty years away from the Murim, the blades Mungyeong possessed had not grown dull in the slightest.

No. They had almost certainly grown sharper and more keen.

*Ah. I miss Mom.*

I knew the truth. Mungyeong truly would not harm me.

But the head and the heart thought differently.

Even if you knew the beast before you would not sink its teeth into your throat right away, human nature still made you reluctant to approach it.

*Gulp.*

After swallowing dryly, I carefully opened my mouth.

“Why did you suddenly...?”

Mungyeong stared at me with icy eyes.

“You sound like you disliked being called out.”

“Gasp. No, I don’t.”

“It really seems that way.”

“How could it? I’m just bad at expressing my emotions. In fact, I’m so happy I could die.”

“Die?”

“…I’ll carefully take that part back. I should’ve watched my mouth. I guess I won’t come to my senses until I see a coffin.”

“See a coffin?”

“...Please spare me.”

“Spare you?”

*Goddamn it.*

They said on the internet that repeating a woman’s last words was the kind of conversational technique that made her heart flutter.

This was the kind of conversation that would make the Grim Reaper’s heart flutter.

I could almost see Yama returning excitedly with the Book of Life and Death after clocking out of work right on time.

*What the hell is this, seriously? Why did he call me out?*

Had he really called me here again because I had spoken casually to him last time?

If I knew what this was about, I could at least feel at ease. But I couldn’t guess at anything beyond that, and the frustration was driving me crazy.

Mungyeong looked at me with displeasure, then suddenly furrowed his brow.

“What is this?”

“What?”

“Have you perhaps not heard yet?”

“Heard what?”

“The Fire King, Jeok Cheongang. Your Master.”

“...?”

“The Fire King, Jeok Cheongang.”

*So what am I supposed to do with that?* I didn’t understand what he meant, so I didn’t even know how to respond.

After hesitating for a moment, I carefully opened my mouth, just in case.

“Ganggangsullae?”[^1]

“Jeok Cheongang said something... What?”

“Oh, isn’t this a word-chain game?”

“...What kind of lunatic are you?”

“If there’s a character limit, is there one? But Fire King Jeok Cheongang is five characters in Korean too, so it should be fine...”

The atmosphere turned ominous.

Mungyeong stared at me with eyes filled with anger and regret, then looked up at the heavens and sighed.

“I can’t believe I have to pass down secret martial arts to a fucking blockhead like this.”

“...”

*For fuck’s sake. Even so, calling someone a blockhead right to his face was too much. That was going too far...*

*Huh?*

*What did I just hear?*

*Secret martial arts?*

[^1]: *Ganggangsullae* is a traditional Korean circle dance and folk song. Taekyung treats the last syllable of Jeok Cheongang’s name as the start of a word-chain answer.
## Chapter artifact 489

# Chapter 489

Secret martial arts.

The moment I heard those words, the four syllables *fucking blockhead* were wiped clean from my mind.

After blinking for a moment, I asked in a faltering voice,

“Secret… martial arts? You’re saying you’ll teach me your secret martial arts?”

To a martial artist, secret martial arts were as important as life itself—no, more important than life.

Even in martial arts novels, there were countless people who threw themselves at danger like moths to a flame just to obtain a single martial arts manual.

And after experiencing the Murim firsthand, I learned that reality was no different. If anything, it was worse.

*But he’s offering to teach me his secret martial arts? And he’s an incredible master on the level of the Slaughter Saint?*

Even though I had heard it directly from him, I couldn’t believe it. No, even before that, one huge question mark had appeared.

“Why?”

At my question, which was filled with doubt, a deep furrow formed between Mungyeong’s smooth brows.

“What do you mean?”

“No, I mean, why are you suddenly acting like this toward me?”

“I suspected as much, but it seems that the Fire King, that old man, really didn’t give you any heads-up.”

“In that case, could it be…”

“That’s right. Your guess is correct. The Fire King…”

“Am I being transferred? Did my affiliation change from the Fire Gate Clan to the Slaughter Saint Clan or something?”

“…”

Mungyeong stared at me with an expression that made it clear he wanted to kill someone, then continued with a sigh.

“The Fire King came to me personally and asked me to teach you martial arts.”

“What?”

It was a relief that this wasn’t a sect-to-sect trade, but it was still an unbelievable story in its own way.

I looked at Mungyeong suspiciously.

“What is that look?”

“It sounds like a lie no matter how I think about it.”

“A lie?”

“First. Our Old Master has a foul temper and a strong sense of pride. He isn’t the kind of person who asks someone else for anything.”

A warm glow passed over Mungyeong’s face, which had previously been surrounded by a chilly aura.

“Hm. You’ve assessed him rather accurately. Continue.”

“Second. The person he asked is just as foul-tempered and prideful as our Old Master. He isn’t the kind of person who would willingly teach someone his secret martial arts.”

“…”

“In any case, for those two reasons, I wouldn’t believe it even with a knife pressed to my throat.”

“I see. So that’s how it is.”

Mungyeong muttered softly, then stared at me with eyes gone cold.

“If a knife were pressed to your throat, you’d believe me. I heard you clearly.”

At that moment, something glinted from the end of Mungyeong’s sleeve. When I saw a short sword slowly emerge, I quietly changed my words.

“I completely believe you now.”

“Suddenly?”

“Actually, I believed you firmly from the very beginning.”

“You’re a fucking lunatic. Is something wrong with your character?”

“Gah!”

“Even by lunatic standards, you’re completely insane.”

*Ah, he really wants to kill me.*

His expression said exactly that.

Mungyeong toyed with the short sword for a moment, his eyes conflicted, then abruptly spoke.

“Come to think of it, what you said isn’t entirely wrong.”

“What?”

“First. As you said, the Fire King does have a foul temper and a strong sense of pride. But he seems to be an exception when it comes to matters concerning his Disciple.”

“…”

“Of course, even if I say that, he’ll stubbornly insist that you aren’t his formal Disciple. Regardless, the Fire King cares about you. Very much.”

Hmm.

I didn’t know what to say. For some reason, a corner of my chest felt ticklish, and my throat felt tight.

It was just… like that.

As I kept my mouth firmly shut, Mungyeong continued in a dry voice.

“Second. I’m not exactly a man of gentle temperament either. But if there is sufficient reason, I’m willing to teach my secret martial arts even to a lunatic like you.”

“Even though I’m a lunatic?”

“Because that lunatic will become a major obstacle to Dark Heaven’s actions from this point forward.”

His quiet voice spread through the night air. Mungyeong continued while gazing at the gently flowing waters of Dongting Lake.

“I have lived as a martial artist for more than half my life. No, I lived as an assassin. It was not a life I chose. It was the life I was given from the beginning. That is why the path I walked was a bloodstained road covered in blood and corpses.”

The Slaughter Saint—the sobriquet given to the greatest assassin in history—had not been earned overnight. He had killed, killed, and killed again until he reached a position everyone had no choice but to acknowledge and fear.

But everyone had their own circumstances.

And in this world, there were more things hidden than I knew.

Mungyeong, standing before me, had probably lived such a life.

His eyes filled with emotions I couldn’t decipher, Mungyeong gazed beyond the darkness and continued quietly.

“If passing on my martial arts to you can be of even the slightest help in the great war already at our doorstep, then it doesn’t seem like such a bad idea. That is all.”

He spoke as though it were nothing important, but it could not have been an easy decision.

It was easy to receive something that belonged to someone else. Giving away something of your own was difficult.

If the people who had fought in the Great Faction War had thought and acted as Mungyeong did now, half the martial artists in the world would have learned the martial arts of the Nine Sects and One Gang by now.

In that sense, Mungyeong seemed different from before.

“Is that… what you call a great cause?”

“A great cause?”

“You made that decision for other people. Sacrificing yourself for someone else. Isn’t that what a great cause means?”

Mungyeong shook his head.

“A great cause is not something a man like me can speak of. An assassin who once killed others for the sake of survival speaking of a great cause? The very thought makes me cringe.”

“The Old Master told me before that the Slaughter Saint only kills people who deserve to die. He said you were a pretty decent assassin.”

“To make a single sword, you must hammer it hundreds of times and put it through the tempering process. I was no different. Before I became the Slaughter Saint, there was a time when I was called the Killing Ghost. That is why I cannot discuss a great cause.”

“In that case…”

I looked Mungyeong straight in the eye and continued.

“What about a great cause as the Divine Physician, rather than as the Slaughter Saint?”

“…”

His slender body suddenly went rigid.

Unlike the utterly calm waters of Dongting Lake, ripples spread through Mungyeong’s eyes.

A moment later, a deep, sunken voice broke the brief silence.

“The Divine Physician… I never liked that sobriquet.”

“Why not?”

“Being called the Divine Physician does not erase my past. Because I know that if my past were revealed, people would curse me and fear me.”

“But you saved people. Countless people. They won’t forget their gratitude.”

A long time passed, but Mungyeong did not answer.

He remained lost in thought, silently staring at the river, then suddenly whipped his head around to face me.

“Gasp! You scared me. What’s wrong?”

“I was thinking about what to do with you for daring to say something so presumptuous to me.”

“Isn’t this normally called comforting someone?”

“Comforting me? You?”

His icy gaze made my insides feel refreshed.

Yeah, fuck. To hell with the Blazing Flame Divine Dragon—to the Slaughter Saint, I was still just *you*.

Rather than talk back and get hit by the backlash, changing the subject was probably the secret to longevity.

“Wow, the moon is bright tonight.”

Mungyeong’s eyebrow twitched as I immediately pretended nothing had happened.

“I don’t know how the conversation ended up here. From now on, refrain from useless words and actions.”

“The breeze is nice and cool, too.”

“Want me to cool off everything above your shoulders too?”

“…I’ll keep what you just said in mind.”

*Shhk.*

The short sword, which had been half-drawn, slipped back into his sleeve.

Mungyeong returned to his usual dry, stiff expression, as though nothing had happened, and opened his mouth.

“So I’ll ask you. What do you intend to do?”

“About what?”

“I can’t tell whether you’re stupid or hard of hearing. I mean studying martial arts under me.”

“…I’m not stupid. I just didn’t know you would give me a choice.”

“Why would I force someone who doesn’t want to learn to stay and teach him?”

He had a point, but hearing such a perfectly normal statement from the mouth of an abnormal person felt incredibly strange.

Of course, I didn’t say that aloud.

If I did, Mungyeong would personally drag my soul out of my body.

“So? What is your answer?”

At Mungyeong’s urging, I scratched the back of my head.

*The Slaughter Saint’s secret martial arts…*

Of course I wanted them.

Everyone had martial arts suited to them, and if a martial art did not suit someone, it could become poison instead. But this was the secret martial art of the Slaughter Saint, a Supreme Peak master counted among the greatest in the world.

If I could understand even half—or a quarter—of the insights embedded in his martial arts and make them my own, I felt that my realm could advance another step.

There was only one thing bothering me.

“It seems the Fire King is weighing on your mind.”

“Have you learned mind-reading or something?”

“What use would mind-reading be? Every thought you have is written plainly on your face.”

Mungyeong looked at me as though I were utterly hopeless and continued.

“A proper martial artist must know how to conceal his feelings. The Fire King is quite something. To think he failed to teach you even something this basic.”

“Take back what you just said.”

At my frown, Mungyeong’s gaze sank deeply.

“Was I wrong?”

“Yes. Even if your mouth is crooked, shouldn’t you speak the truth correctly?”

“You dare…”

“He didn’t fail to teach me. He couldn’t teach me. The Old Master is even worse at hiding his expressions than I am. How could he teach me something he doesn’t know?”

“…You’re beyond my imagination.”

Mungyeong sighed and shook his head.

“In any case, don’t worry too much about the Fire King. This is something he personally asked me to do, and I have no intention whatsoever of entering into a Master-Disciple relationship with someone like you.”

“Ah. Right.”

Come on. Even so, *someone like you*?

It stung a little to hear him say it, but his firm declaration still made me feel much more at ease.

*But why do I feel like I’m betraying the Old Master?*

Jeok Cheongang himself had asked Mungyeong to do this, and considering the difficult battles ahead, it was something that would help me.

Looking at the circumstances, there was no problem at all. So why did I feel so uncomfortable?

Thinking of Jeok Cheongang, who had disappeared without saying a word, I smacked my lips and finally nodded.

“All right.”

“Think carefully before you answer. Beginning is your choice, but ending it is different.”

“What? What does that mean?”

“I alone will decide how you move. But if you complete this training, you will become a martial artist unlike the one you have been until now.”

What was this?

I had expected something like this to a certain extent, considering who I would be studying under, but for some reason, a chill ran down my spine.

As I swallowed dryly, a familiar chime rang in my ears alongside Mungyeong’s hard voice.

“You may be a martial artist of considerable skill, but a martial artist and a Murim martial artist are not the same thing. You’re still only half-formed. I’ll turn you into a true Murim martial artist.”

*Ding.*

> **System**
>
> - Sudden Quest, **Fake Murim Martial Artist**, has been generated!
>
> **Will you accept Fake Murim Martial Artist?**
>
> **Agh** / **N**

“…”

Why was there an Agh instead of a Y in the choices?

I stared at the Quest window with an incredulous expression, then muttered without even realizing it.

“Agh?”

*Ding.*

> **System**
>
> - Quest accepted. **Agh!**

“…Ah.”

This was driving me crazy.

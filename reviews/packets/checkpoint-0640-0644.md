# Checkpoint Review — 640–644

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

# Chapters 640–644

## Plot

Jin Taekyung kills the final injured Thousand-Year Spider after the Beast Miao King brings it to him. Deeper in the Poisonblood Grounds, they discover a moonlit swamp serving as a spider slaughterhouse and storehouse, containing hundreds of web-wrapped victims—including roughly two hundred elite warriors who disappeared at Ailao Mountain—and countless pure-white eggs. The webs shield the paralyzed survivors from the Poison Mist, so Jin and Cheok leave them wrapped for safe evacuation.

Muyaho summons the rescue party, returning the survivors and Nanman forces to the Beast Palace. Jin completes the swamp quest, earning experience, Fame, five Top-Grade Poison-Warding Pearls, the Achievement *How’d You Get Back?*, and the Title *Poisonblood Grounds Pioneer*. At the tribal grand council, Jin is admitted as its first outsider despite Baeksang’s opposition. Yayul Cheok formally authorizes his attendance, and Jin receives the Supreme Peak-grade Quest [Tribal Grand Council]: secure the Nanman Beast Palace’s entry into the alliance.

The council reports that an unidentified bald martial artist called the Blood Monk has killed hundreds in Guizhou while carrying a Zen staff. Jin challenges Baeksang’s dismissal of the matter, suspecting concealment or a connection to a wider threat. The torches suddenly go out as a freezing presence and powerful martial aura surround him. Elsewhere, an unidentified entity who recognizes Jin’s name kills two informants and remarks that it has been a long time since their last meeting.

## Continuity

- Jin Taekyung, Yayul Cheok, the Beast Miao King, and the rescue party returned from the Poisonblood Grounds; the swamp quest was completed.
- Approximately two hundred Ailao Mountain elite warriors survived inside Thousand-Year Spider webs and await safe evacuation; the webs protect them from the Poison Mist.
- The missing ferocious beasts remain unaccounted for. The pure-white eggs in the swamp remain unexplained.
- Jin’s suspicion that Dark Heaven influenced the Thousand-Year Spider attack remains unconfirmed.
- Jin has joined the Nanman Tribal Grand Council with majority support. Yayul Cheok authorized his attendance as Palace Lord and great chieftain of the Miao people; Baeksang opposed but did not overturn the decision.
- The active quest [Tribal Grand Council] requires Jin to secure the Nanman Beast Palace’s entry into the alliance. Its reward and failure condition are unknown.
- The Blood Monk is an unidentified bald martial artist with a Zen staff who has killed hundreds in Guizhou. A captured witness who might have identified his destination died before speaking.
- An unidentified hostile entity knows Jin and claims a long-standing prior connection; its identity, motives, and relationship to the Blood Monk remain unknown.
- Ailao Mountain’s Wraith has not revealed its purpose.

## Translation Decisions

- Use **Poisonblood Grounds**, **Poison Mist**, **Thousand-Year Spider**, **Beast King Stone**, and **Beast Miao King**.
- Use **Poisonblood Grounds Pioneer** for the Title and **How’d You Get Back?** for the Achievement.
- Use **Tribal Grand Council** for 부족 대회의 and **Blood Monk** for 혈승.
- Use **Top-Grade Poison-Warding Pearls**, **Poison-Warding Pearl**, and **Paralytic Venom**.
- Retain **Yayul Cheok**, **Baeksang**, **Yayul Mok**, **Muyaho**, **Fire King**, and **Fire Gate Clan**.
- Use **Sword Demon** for 검마 and **two-headed horn snake** for 쌍두각사.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung has been admitted to the Nanman tribal grand council with majority support.",
    "Yayul Cheok formally authorized Jin's attendance as Palace Lord and great chieftain of the Miao people.",
    "Baeksang opposed Jin's admission but accepted the majority decision without blocking it.",
    "Chieftains support Jin because he saved their people at Ailao Mountain or because their tribes owe historical debts to the Fire King and Fire Gate Clan.",
    "The Quest [Tribal Grand Council] requires Jin to secure the Nanman Beast Palace's entry into the alliance; its Reward and failure condition remain unknown.",
    "Approximately two hundred elite warriors of Ailao Mountain remain alive inside the Thousand-Year Spider webs and await evacuation.",
    "The Thousand-Year Spider webs appear to shield their victims from the Poison Mist.",
    "The missing ferocious beasts have not been found in the Poisonblood Grounds.",
    "Dark Heaven's involvement in the Thousand-Year Spider attack remains suspected, and the purpose of Ailao Mountain's Wraith remains unknown.",
    "The nature of the pure-white eggs in the Poisonblood Grounds remains unknown.",
    "An unidentified entity who knows Jin Taekyung has killed two informants after learning of his council attendance and implied a long-standing prior connection.",
    "The Blood Monk is an unidentified bald martial artist carrying a Zen staff who has killed hundreds in Guizhou; the captured witness who might have revealed his destination has died, and Jin suspects a possible connection to Dark Heaven or a threat to Nanman."
  ],
  "continuity_sources": [
    644
  ],
  "open_questions": [
    "Who is the hidden entity that recognizes Jin Taekyung, and what is the nature of their past connection?",
    "Where did the missing ferocious beasts go?",
    "Did Dark Heaven influence the Thousand-Year Spider attack, and is the Blood Monk connected to Dark Heaven or heading toward Nanman?",
    "What does Ailao Mountain's Wraith intend to do?",
    "What are the pure-white eggs in the swamp, and what will emerge from them?"
  ],
  "safe_through": 644,
  "temporary_decisions": [
    "Use Tribal Grand Council for 부족 대회의.",
    "Use Blood Monk for 혈승.",
    "Use Sword Demon for 검마.",
    "Use two-headed horn snake for 쌍두각사.",
    "Use Thousand-Year Spider for 천년지주."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 640

# Chapter 640

One Annihilation is a technique that doesn’t merely destroy its target—it erases it.

Because it momentarily draws out every ounce of power and produces several times the usual strength, the higher the user’s martial attainment, the more powerful One Annihilation becomes.

Even so, it had one fatal drawback…

*Beep. Beep. Beep-beep-beep!*

> **System**
>
> - You have exhausted all your power!
>
> - Warning! Warning! The aftereffects of overusing your abilities will return to you in full!
>
> - Status abnormality: **Internal Injury** applied!
>
> - Status abnormality: **Exhaustion** applied!
>
> - Status abnormality: **Anemia** applied!
>
> - Status abnormality: **Paralyzed** applied!
>
> - Due to the stacked status abnormalities, all stats temporarily decrease by 100!

The more powerful One Annihilation became, the more severe its aftereffects became as well.

*……Ah. Damn it.*

My entire body trembled as if I’d been electrocuted, and my once-clear vision grew hazy, like a screen covered in static.

The price for turning thousands of venomous beasts into ash was anything but small.

*Still, I thought I’d at least level up once.*

The higher your Level, the less EXP you gained.

Back when I had been a low-level nobody who could barely stand up to a single Peak master, leveling up could cover for that weakness to some extent. But now that my vessel had grown larger, I needed far more EXP to fill it, and even leveling up had become difficult.

“……Hng.”

Internal Injury and Exhaustion weren’t enough—I also had anemia and paralysis. It was a miracle I hadn’t lost consciousness.

As I staggered through my dizzy vision, I somehow moved my hand and drove White Flame into the ground.

*Thud!*

As I leaned pitifully against the spear for support, I couldn’t help wishing Jeok Cheongang had taught me the Dance of the Fire God and Demon.

I knew exactly what answer I’d get if I begged him.

*Dance of the Fire God and Demon? Is dying young your life’s ambition?*

That was because it was far too dangerous, but at most, it would be the difference between a pistol and an automatic rifle.

To be honest, at this rate, I felt like I might die far from home using One Annihilation before then.

Of course, I had no intention of dying in a foreign land in a place this horrible.

*That’s why I took out insurance.*

Just as I muttered that inwardly, the insurance agent who had realized his client had gotten into an accident fell from the sky.

*Whoooosh. Boom!*

The heavily built old man landed on the ground using the Thousand-Year Spider—so enormous that “huge” suited it better than “large”—as a cushion while it convulsed with barely any life left in it.

His face flushed red, the Beast Miao King spread both arms toward me.

“Uh, that’s really crossing the line—”

*Wham! Crack!*

“What an incredible bastard!”

“Argh! Aaaagh!”

“How did you do that? Was it the Fire Gate Clan’s unique martial art? Or the final ultimate technique Old Man Jeok taught you?”

*Whap! Whap!*

“Uuuugh!”

“What a monster! I couldn’t believe it even while watching!”

“Aaaaaagh! You crazy bastard!”

“What? Crazy bastard! Yes! That’s right! You’re the madman the Central Plains gave birth to!”

I nearly died far from home.

I wasn’t joking. I mean it.

And when the madman Nanman had given birth to finally let go of me, I heard a sad notification in my ear.

*Beep.*

> **System**
>
> - Status abnormality: **Mild Ligament Tear** applied!
>
> - **Strength** decreases by 20 until recovery!
>
> - **Agility** decreases by 20 until recovery!

“…….”

This was why Doctor Octopus was a villain.

But I no longer had the strength to say anything. Wheezing from the pain, I glared at the Beast Miao King and barely managed to open my lips.

“Spider. Spider.”

“Spider? Oh. The Thousand-Year Spider?”

“Quick. Hurry.”

The Beast Miao King nodded with admiration at my pitiful gestures.

“I wondered if that was what you meant, but are you planning to use the Thousand-Year Spider to figure out the Poisonblood Grounds? You really are something.”

“Ah, please.”

“Haha, all right. Just as you asked, I brought it here alive and well—”

At that moment, just as the Beast Miao King was continuing to spout nonsense—

“Gnnngh!”

I squeezed out the last of my strength, pulled White Flame free, and thrust it straight into the Thousand-Year Spider’s head.

With the heart of a patient collecting a random insurance payout.

*Thud!*

—Ssssit! Kieeeek!

Along with the monster’s short death cry, heavenly bells rang out from somewhere.

*Ding. Ding. Ding.*

> **System**
>
> - You defeated **Level 119 Thousand-Year Spider**!
>
> - Additional EXP has been awarded for defeating a rare entity!
>
> - Level Up!
>
> - The damaged body has been substantially restored!
>
> - All status abnormalities have been removed!
>
> - Warning! Your physical condition is not yet perfect! A little treatment and rest are required!

Ah. This was why I took out insurance.

If the EXP from a single venomous beast was an ant’s tear, then the Thousand-Year Spider was a downpour from heaven.

When I added the EXP from killing thousands of venomous beasts at once to the Thousand-Year Spider’s EXP, vitality immediately flooded back into my dying body.

“Buuuurp.”

Last hit. Sweet.

The ancient sages once said that a single Level Up made the five loaves and two fish look like nothing.

I don’t know exactly who said it, but that was how it went. And it was true.

*Whew. I almost died.*

I had barely turned back from the threshold of a nursing home when I felt fullness rising through my entire body and rubbed my stomach.

Then, the next moment, my eyes met those of someone staring at me with a deeply unimpressed expression.

“Why?”

“…….”

“What?”

“…….”

After a moment of silence, the Beast Miao King opened his mouth with a look of utter disbelief.

“Then why the hell did you tell me to keep it alive?”

*Why else? Obviously so I could harvest the EXP.*

But years of working for a shitty small Guild had given me something I had never possessed before: social awareness and people skills.

I answered with a mournful, rigid expression.

“I wanted to take revenge with my own hands.”

“What?”

“For the Nanman warriors who fell victim to the hands……no, the slime and webs of those bastards I could tear to pieces and still not feel satisfied.”

“……!”

Ripples stirred in the Beast Miao King’s wide-open eyes.

He stared at me in silence with trembling eyes, then opened his mouth in a choked voice.

“Hmm. I truly don’t know what to say.”

“Shh. Don’t say anything. I already know everything without you saying it.”

“You—you little bastard!”

A romantic atmosphere……Fuck that. Go away. It was making me gag.

But one thing was certain: the Beast Miao King couldn’t hide how moved he was.

*Well, I guess it’s fine if the result is good.*

I didn’t think I needed to feel guilty.

It was true that I mourned the deaths of the Nanman warriors, and it was also true that I needed EXP to recover my body.

What mattered was that my quick excuse had led to an even better result.

*If this news spreads through Nanman, maybe the odds of the Nanman Beast Palace joining the Murim Alliance will go up by about ten percent.*

Even so, it was also true that one corner of my heart felt heavy.

I felt guilty because I hadn’t been able to prevent hundreds of people from being massacred less than two shichen away.

*……Damn it.*

My mouth tasted bitter.

Even now, countless people were probably dying throughout the modern world and the Murim.

Their causes of death might be as simple as traffic accidents, or they might have been killed by monsters.

If they were Murim people, they might get into an argument at an inn, draw their swords, and die a violent death.

There might even be some nameless chivalrous warrior who lost their life while fighting an evildoer.

I knew it. I knew I couldn’t save all of them.

But I couldn’t help it. I was human, and I hated seeing people like me die.

And I felt regret, too. Regret that if I had been there, perhaps I could have saved innocent people.

*Great power comes with great responsibility.*

That line I had heard in some superhero movie had, at some point, turned into a massive boulder weighing down my body and mind.

Even while circulating my qi, when I should have been concentrating with all my might, I felt it.

*Perhaps this is a Heart Demon, too.*

With a small sigh, I shook my head and began moving again, leaving the Thousand-Year Spider’s corpse behind.

Toward the deeper, more secluded interior of the Poisonblood Grounds.

*Splash. Splash.*

The Beast Miao King and I became even more cautious with every step.

The area was quiet because we had killed five Thousand-Year Spiders and an enormous number of venomous beasts, but it was still too soon to let our guard down.

*That bastard is the biggest problem of all.*

Ailao Mountain’s Wraith.

The Black Tiger that perfectly matched the name given by the System was our top-priority target for vigilance.

Its enormous body and windlike movements. The powerful yet eerie qi I had felt for that brief moment. All of it proved that the creature was far beyond the limits of an ordinary spiritual creature or venomous beast.

—Where do you think it is now?

Having someone beside me who thought the same way was a major advantage.

In response to the Beast Miao King’s Sound Transmission drilling into my ear, I moved my lips.

—Who knows? But one thing is certain: it’s still in the Poisonblood Grounds.

—That is what I have been wondering. After going to all the trouble of luring us here, why has it still not appeared? If it had shown up fifteen minutes ago, we would certainly have been fighting at a disadvantage.

The Beast Miao King was absolutely right.

The five Thousand-Year Spiders had been easier opponents than their notorious reputation suggested, and the thousands of venomous beasts had been the same. But if Ailao Mountain’s Wraith had joined in, the situation would have been completely different.

*If it had joined the fight from the beginning, we could probably have put up a decent fight. But if it had appeared right after I used One Annihilation……*

Even if we had responded in the best possible way, it would have been an extremely difficult battle.

The creature had teeth capable of enduring Force, incredible speed, and a presence that was impossible to sense, like a wraith befitting its name.

One of the two of us might have died, or we might have had to leave a limb behind.

And in the worst-case scenario, there was no question that we would both have died.

*But why? Why didn’t it appear even under those circumstances?*

I didn’t know the exact reason, but of all the thoughts running through my head, only two hypotheses seemed even remotely possible.

First: the classic island-nation-style plot.

*Heh heh. The Thousand-Year Spider is merely the weakest of our Four Great Venomous Beasts.*

And second—

*The Wraith of Ailao Mountain has no intention of harming us.*

As I continued thinking while carefully moving forward, I immediately struck the second hypothesis from consideration. No matter how I thought about it, it seemed completely implausible.

Before I could continue thinking, the Beast Miao King, who had been following behind while keeping watch over our flanks and rear, placed his thick palm on my shoulder.

*Tap.*

*Oh, shit.*

That scared the hell out of me. My heart nearly fell out of my chest.

After calming my startled nerves, I turned my head in the direction his finger was pointing.

Beyond the Poison Mist growing denser by the moment and the dark jungle thick with trees on every side, I spotted a mysterious light faintly spilling out.

*Could it be?*

No more words were necessary. My instincts had told me before my thoughts could.

*Rustle. Crackle.*

Crossing the grass that carried a faint trace of poison, we reached the space where the light had emerged.

At last, we saw the scene spread out before us and stood there with our mouths hanging open.

“This is……!”

A vast swamp bathed in faint moonlight.

What awaited us there was a great many things hanging from the air, all tightly wrapped in transparent spiderwebs—and pure-white eggs.
## Chapter artifact 641

# Chapter 641

Sometimes, there are moments when merely witnessing something is enough to send a chill down your spine and make your hair stand on end.

Like every scene unfolding before my eyes right now.

*Fwoosh.*

The faint moonlight pouring through the swaying leaves was as mysterious as a scene from a myth, but what it illuminated was not a peaceful blue lake.

*What the……*

A swamp steeped in darkness and desolation. Hundreds of enormous shapes, layered in spiderwebs like silkworm cocoons, and pure-white eggs that were smaller but several times more numerous.

*What the hell are they?*

An ominous question pressed down on my heart, as if it were something I wasn’t supposed to learn the answer to.

But contrary to that thought, the hand I had extended on instinct was already touching the unidentified cocoon hanging closest to me.

*Tap.*

An unpleasant sensation traveled through my fingertip. At the same time, a System notification pierced my ear.

*Beep. Ding.*

> **System**
>
> - You have been **Poisoned** by **Thousand-Year Spider’s Paralytic Venom**!
>
> - If you are not detoxified quickly, you may enter **Full-Body Paralysis** and **Unconsciousness**!
>
> - The potential effect of the **Myriad-Poison Ring** has been activated!
>
> - All status abnormalities related to **Poison** have been removed!

My fingertip, which had felt numb for a moment, soon grew cool and clear.

The Myriad-Poison Ring was a sacred artifact that could even absorb Formless Ultimate Poison. No matter how special a venomous creature the Thousand-Year Spider was, it couldn’t do anything to me.

*If these really are the Thousand-Year Spider’s webs……*

A guess suddenly flashed through my mind. I put more strength into my hands and pulled the webbing apart from side to side.

*Crack. Riiiiip.*

The hundreds of layers of tangled web tore helplessly under my terrifying grip.

And when the shape concealed inside was revealed, the Beast Miao King, who had been watching from beside me, muttered like he was groaning.

“Is that a person?”

He was right.

A face as white as a sheet of paper. A body that did not move even an inch.

The Beast Miao King checked the unknown man’s slow pulse and let out a sigh of relief.

“Fortunately, he’s still breathing.”

That was something I had expected as well.

According to what the System had told me earlier, the Thousand-Year Spider’s webs did not contain poison powerful enough to kill their victims.

And the reason was probably……

*To keep them fresh. That way, they can fill their bellies whenever they want.*

Now I understood why the hair on my body had risen the moment I first set foot here.

*A slaughterhouse.*

Before being the Thousand-Year Spider’s habitat, this swamp was a slaughterhouse—and a gigantic food storage facility.

Only then did I notice the deep scent of blood hidden beneath the stench drifting in from every direction. I muttered under my breath.

“Spider bastards. They’ve sure been stuffing their faces for a long time.”

Hundreds. No, perhaps thousands.

If the Nanman Beast Palace’s records claiming that the Five Poisons Sect had created the Poisonblood Grounds were true, then the number of people who had died here over all those years would be impossible to count.

Ironically, the Thousand-Year Spiders’ habits had made it possible for us to save a great many people today.

*It really was strange. More people had disappeared than died.*

There had been about three hundred elite warriors stationed at Ailao Mountain.

The five Thousand-Year Spiders had definitely killed around a hundred of them on the spot, then, after satisfying their hunger, dragged the rest to the Poisonblood Grounds.

Those people would have been turned into meals one by one before long, but now we had a chance to save them.

“Would you look at these goddamn bastards! They deserve to die!”

I calmed the Beast Miao King, whose eyes had reddened with fury.

“Uh, sorry to interrupt, but you already killed them.”

“Tearing them to pieces wouldn’t be enough!”

“Uh……”

Well, I had nothing to say to that. Still, this was a time to focus on dealing with the current situation rather than getting angry.

After calming down a little, the Beast Miao King looked around with a devastated expression.

“To think they dared to do something like this.”

“You said there hadn’t been any major losses until now, didn’t you?”

“That is the truth. At least while I have been the Palace Lord, there was never a problem.”

“That’s strange. Five Thousand-Year Spiders suddenly appeared and attacked the warriors at a time like this.”

The Beast Miao King fell silent for a moment at my clearly pointed words, then abruptly spoke.

“……Dark Heaven. Do you think this was their doing?”

I nodded without hesitation.

“I don’t know whether they directly laid a hand on this, but they must have exerted some influence. It isn’t strange for a venomous creature like the Thousand-Year Spider to attack people, but considering the timing, we can’t help but suspect them.”

“But if this truly was Dark Heaven’s doing, they could have waited until after you left. Causing this on the final day of the tribal competition would only harm them.”

“That…….”

My voice trailed off despite myself. The Beast Miao King’s answer had been sharper than expected, and he had offered evidence I couldn’t easily refute.

*He’s not wrong. If I were Southern Heaven Demon Empress—that bitch—I wouldn’t have gone to the trouble of doing this.*

Even without any interference, it was practically certain that the Nanman Beast Palace’s entry into the Murim Alliance would fall through. Dark Heaven had no reason to stir up Nanman for nothing.

*Then why?*

Everything was shrouded in questions.

Ailao Mountain’s Wraith had appeared out of nowhere and still hadn’t shown itself. Five Thousand-Year Spiders had suddenly begun a massacre. And there was the question of whether they were connected to Dark Heaven.

I had been frowning in thought for some time when the Beast Miao King’s voice brought me back.

“More importantly, the immediate problem is moving these people. It is a blessing that they are still breathing, but getting back out of the Poisonblood Grounds is another matter.”

I stopped thinking and answered.

“If you ask me, I think it would be better to leave the others as they are.”

“Leave them? You mean keep them here?”

“……Do I look insane to you? Of course we have to take them back to the Nanman Beast Palace. I told White Tiger to bring the people here, so it would be best to wait. Though I’m not sure he understood me properly.”

“You must mean Muyaho. He is more intelligent than most people. I am sure he understood you well enough.”

“…….”

“Why are you making that expression?”

“Oh. It’s nothing. Nothing at all.”

I almost lost it.

Muyaho. The more I heard that name, the less I could get used to it. I barely pulled my crumbling expression back together and continued.

“And I think we should leave the webs intact instead of tearing them off.”

“Because of the poison.”

“Yes.”

The journey here had been difficult, but the way back would be far worse.

We would have to make our way through the Poison Mist with more than two hundred patients who had only just awakened after spending the past several shichen in a state of full-body paralysis and unconsciousness.

*I’m not even sure how much the Myriad-Poison Ring can cover.*

The Myriad-Poison Ring certainly possessed mysterious power, but I couldn’t put two hundred lives through a fifty-fifty gacha roll just by trusting in this one item.

They were safer wrapped in the webs like this.

“At the very least, they don’t seem to be affected by the Poison Mist while they’re inside. If that weren’t the case, they would have all died on the way here.”

“That is true. The Thousand-Year Spider’s poison permeating the webs may be preventing other miscellaneous poisons from getting in.”

In a way, it was similar to using poison to suppress poison.

On the way here, the webs had been coffins.

From now on, they would be cryogenic capsules protecting their lives from the Poison Mist.

Even if I took them out one by one and detoxified them, there was a clear limit to what I could do.

At most, our conversation would go something like this.

*All right, patient. Slowly open your eyes. Can you see the fingers I’m waving in front of you? If you can, tell me how many there are.*

“Uuuh. One……one.”

*What finger is it?*

“The middle one.”

*Correct. It means fuck you.*

“Huh? What are you talking about all of a sudden……?”

*It was a simple test. Anyway, good. You can see and hear clearly now. Both your sight and hearing have recovered.*

“Thank you. Thank you so much, Han Chinese sir.”

*Ha ha. Think nothing of it. By the way, since you’ve been detoxified, your paralysis should have disappeared. Can you move your fingers?*

“Of course. I can move them just fine now.”

*Good. I have something for you to do with those fingers. But before that, may I ask your name?*

“Me? I’m Jang Sam.”

*Excellent. I’ll give you this dagger. Now write what I say on this wooden tablet.*

“Yes, yes.”

*All right. Write exactly what I say. Jang Sam.*

“Jang. Sam.”

*Lies here.*

“Lies here. Huh?”

*Actually, I didn’t tell you because I was worried you’d panic, but we have to go back the way we came. And we don’t have any poison-warding pearls left. Of course, I’m fine because I have the Myriad-Poison Ring.*

“……!”

*I’m ‘invincible.’ The Myriad-Poison Ring is a ‘god.’*

Hmm.

There was going to be a two-hundred-to-one bloodbath over the Myriad-Poison Ring.

Maybe two hundred to two. The Beast Miao King also possessed a large, beautiful, top-grade poison-warding pearl.

“……Why are you looking at me like that?”

“It’s nothing.”

“Is it Dark Heaven?”

“No. I mean heaven as in the sky.”

The Beast Miao King’s expression hardened.

“Is he really insane……?”

If my department head had been here, he would have laughed. But it seemed the Palace Lord didn’t get the joke.

The Beast Miao King looked me over with an expression like he was staring at a Thousand-Year Spider walking on two legs, then began gathering the warriors wrapped in webs into one place.

*Slice. Slice.*

Every time his straightened palm moved, the people hanging in midair were neatly stacked together.

There were two hundred of them.

Just as I had guessed, it was almost the same as the number of warriors who had disappeared from Ailao Mountain.

*Wait. What about the ferocious beasts?*

I had been helping the Beast Miao King move the survivors when I suddenly raised my head at a thought I had temporarily forgotten.

One of the questions I had had while searching Ailao Mountain in the beginning: the missing ferocious beasts were nowhere to be seen.

The Beast Miao King soon noticed it as well and wore a puzzled expression.

“That is strange. There is no sign of the ferocious beasts.”

“Could they be timid? Maybe they tuck their tails and run away when they meet people they’ve never seen before.”

“I’m asking because I’m curious, but do you perhaps not know what ‘ferocious beast’ means?”

Of course I did. Ferocious. Beast.

That was precisely why it was strange. So many ferocious beasts wouldn’t have abandoned their master and run off somewhere.

*It’s not as if the Thousand-Year Spiders are picky eaters, either.*

This was one thing I knew well. Hope Goshiwon, where I had lived for nearly seven years, had more spiders than hope.[^1]

Eventually, I had even grown fond enough of them to share my ramen.

*Then where the hell did they go?*

We would have to search the Poisonblood Grounds more thoroughly to find out, but the Thousand-Year Spiders didn’t seem meticulous enough to sort their food into separate categories.

And it was at that exact moment, while the Beast Miao King and I were looking around with puzzled expressions—

*Rustle.*

Along with a small noise, I sensed a faint presence more than ten zhang away.

[^1]: A goshiwon is a small, inexpensive room-for-rent housing arrangement, often with shared facilities.
## Chapter artifact 642

# Chapter 642

*Rustle.*

Along with the faint noise came a presence rapidly drawing closer from far away. The moment I noticed it, I aimed White Flame toward the source at lightning speed.

The same thought must have flashed through the Beast Miao King’s mind as he immediately drew up his internal energy.

*The Wraith of Ailao Mountain.*

But the next moment, that prediction missed spectacularly. When I caught sight of a pure-white shape beyond the blackened grass, I lowered the spearhead with a sigh.

“Muyaho?”

- Grrr!

*Shasha-shasha!*

White Tiger came running like the wind with a short but powerful cry, happily rushed toward me…… then passed right by without a second glance and flopped onto its back at the Beast Miao King’s feet.

- Pant. Pant. Pant.

“Yes, yes. You managed to find your way here. What a clever little fellow.”

At this point, I wondered if we should call it a silver retriever instead of a white tiger. Of course, it was about the size of ten retrievers put together.

*Come to think of it, the fact that this guy came back means……*

As if he had read the thought that surfaced in my mind, the Beast Miao King stroked White Tiger’s belly while it did its utmost to charm him and asked,

“Where are the others?”

- Grrrr.

White Tiger rose with a pleased growl, then suddenly let out a mighty roar. The beast’s cry rang through the thick darkness and Poison Mist. Before long, torchlight flickered in the distance.

The torches numbered roughly several dozen to a hundred.

And at the front were some familiar faces.

“Palace Lord.”

“Father! Are you all right?”

Baeksang, Yayul Mok, and the warriors of the Nanman Beast Palace approached, their faces unusually grim. The Fire Dragon Pavilion members came running toward me behind them.

“Captain!”

“Mujin, just in case you’re wondering, if you throw yourself into my arms or anything like that, you won’t die a pleasant death.”

“……Yes, sir.”

I immediately cut off Hyuk Mujin, who was charging toward me as if he had been possessed by the heroine of a tragic romance. Then I shrugged at the other members, who were just opening their mouths.

“To tell the whole story from the beginning would take a while…… Do you want to hear it here, or outside?”

There was no need to hear their answer.

Maybe if we were in a pleasant café with sentimental pop music playing in the background. But no one wanted to listen to a long story in the Poisonblood Grounds, with its desolate atmosphere and drifting Poison Mist.

And the System did not forget to remind me of the Quest I had briefly forgotten.

*Beep. Ding.*

> **System**
>
> - **Quest: My Love, Don’t Cross That Swamp** has been successfully completed!
>
> - **Quest Reward** will be granted!
>
> - You have acquired a considerable amount of **EXP** and **Fame**!
>
> - You have acquired **5 Top-Grade Poison-Warding Pearls**!
>
> - You have earned the very rare **Achievement: How’d You Get Back?**!
>
> - You have acquired the rare **Title: Poisonblood Grounds Pioneer**!

* * *

That night, Nanman’s darkness was unusually deep and long.

But everything had a beginning and an end.

Deep in the night, while everyone slept, the hundred elite warriors who had hurried to Ailao Mountain were still on their way back. By the time they returned to the Nanman Beast Palace, dawn was breaking, and quite a few people witnessed their arrival.

“Did you hear the story? Apparently something huge happened last night.”

“What story?”

“Well, you know. I heard it from old man Mong, who lives near the west gate of the Outer Palace……”

“Gasp!”

“What? I haven’t even started yet.”

“Was that old man still alive? I was sure he died last year.”

“Ah, fuck.”

The gist of the rumor that spread rapidly with the morning sunlight was as follows.

Something major had happened somewhere in Nanman the previous night. Baeksang, the great chieftain of the Bai people, and the Young Palace Lord Yayul Mok had led a hundred elite warriors out of the Outer Palace. And after returning only a few shichen later, the Beast Miao King and Jin Taekyung had been at the head of their procession.

The Nanman Beast Palace normally did not intervene in disputes between the tribes by force. Because of that, the fact that the Palace Lord had personally taken action meant that this was a fairly major incident.

But the rumor did not end there.

“But I heard the place where the trouble happened was none other than Ailao Mountain.”

“Ailao Mountain? You mean that Ailao Mountain?”

“Are there any other Ailao Mountains in Nanman? Yao merchants who live in a village a hundred li away told us about it at first light, so it must be true. Apparently they happened to see it while staying up late to finish their ledgers.”

To the people of Nanman, the name Five Poisons Sect was an everlasting yoke that could never be erased. Their ancestors had fought against the Five Poisons Sect, and only after countless sacrifices had they managed to establish the order and laws that existed today.

And yet, of all places, the incident had occurred in Ailao Mountain, the Five Poisons Sect’s former headquarters.

Under normal circumstances, it was a forbidden land they did not even want to mention. But if something had happened there, that changed things.

“What the hell? Keep going! Hurry!”

The marketplace, lined with endless street stalls. Secluded alleys. Inns where people came and went without end……

The voices that left one person’s mouth traveled from ear to ear, then flowed out through someone else’s lips.

And the chieftains who had gathered for the tribal grand council being held today were well aware of the commotion and the rumors.

They also knew that the rumors spreading throughout both the Outer Palace and Inner Palace were far more accurate than expected.

“The whole place is in an uproar over that rumor. There isn’t a single person who doesn’t know.”

“The bigger problem is that it isn’t merely a baseless rumor. Isn’t that right?”

The chieftains had gathered in one place for the first time in a year for the grand council, but they had no time to exchange pleasantries.

The chieftains, who had claimed their places early in the enormous main hall of the Inner Palace, continued their conversation with grave expressions.

“You all received advance word, so you already know this, but this is no ordinary matter. Ailao Mountain. Nearly a hundred elites have already been sacrificed to the creatures that were supposed to be in the Poisonblood Grounds.”

“I heard that Thousand-Year Spiders appeared. To be honest, I find that difficult to believe. Even more so when there were five of them, not just one.”

“It may be difficult to believe, but it is all true. Their corpses are still there, so it cannot be a lie. Enraged by the deaths of the warriors stationed at Ailao Mountain, the Palace Lord pursued them all the way to the Poisonblood Grounds and hunted them down.”

The middle-aged chieftain who had answered without hesitation added one more thing in a low voice.

“That young Han Chinese warrior from the Murim Alliance. Blazing Flame Divine Dragon Jin Taekyung was with him as well.”

The chieftains gathered here were lords who each governed a part of Nanman, regardless of the size of their tribe. Naturally, they all knew about the young outsider, and their reactions varied.

“Oh.”

“Hmm.”

“Ahem.”

One chieftain nodded with an exclamation of admiration. Another gave an uncomfortable cough and stared pointlessly into the empty air.

But if there was one clear difference from the atmosphere of a few days ago, it was that not a single person called him a “damned Han Chinese bastard” this time.

Even the chieftains who normally disliked Han Chinese people knew that Jin Taekyung’s contribution to resolving this incident had been far from insignificant.

“If it weren’t for him, this matter would not have ended so quickly. Perhaps the Palace Lord, who rashly went after them, might even have suffered harm instead……”

*Bang!*

A sudden boom swallowed the rest of his words.

At the same time, more than thirty pairs of eyes turned toward the same spot. One of the chieftains, who had worn an unpleasant expression ever since Jin Taekyung was mentioned, had struck the stone table.

“I tried to hold my tongue, but I can’t sit here and listen any longer. Watch your words, Chief Jang. The Palace Lord is far stronger than you think. No, the same goes for everyone in Nanman. We have no need for help from some weak Han Chinese bastard!”

The middle-aged chieftain who had been leading the conversation frowned.

“What brave and prideful words. Truly moving. But didn’t you hear that weak Han Chinese bastard dealt with two Thousand-Year Spiders and thousands of venomous beasts in the Poisonblood Grounds? That he is a renowned warrior of the Central Plains who inherited the Fire King’s legacy?”

“Th-that……”

“And five years ago, despite the Palace Lord personally mediating the matter, who was it that invaded our tribe’s territory? You, wasn’t it? Even if a venomous snake has bitten your mouth, let’s call things what they are. The one you swear loyalty to is not the Palace Lord, but Great Chieftain Baeksang. Everyone in Nanman knows that you are his loyal dog.”

“What? Loyal dog! You son of a bitch!”

“Son of a bitch? You piece of poisonous refuse left behind by the Five Poisons Sect—how dare you……”

*Bang!*

At that very moment, as the two chieftains leaped to their feet and snarled at each other as if they were about to draw their swords—

*Rumble……*

The enormous stone gate, which had been tightly shut, opened. Three figures stepped into the hall.

*Thud. Thud.*

Their footsteps echoed through the interior, which had suddenly fallen silent. The man at the front stopped, and a voice carrying a chill flowed from between his lips.

“Looks like I interrupted your conversation.”

“……!”

“……!”

“Don’t mind me. Carry on.”

But no voice emerged from anywhere.

As if nothing had happened, the shouting that had filled the hall only moments ago vanished in an instant, replaced by a heavy silence that pressed down on everyone. At the same time, the expressions of the two opposing chieftains split between joy and sorrow.

“Welcome, Great Chieftain Baeksang.”

Baeksang cast a sidelong glance at the groveling loyal dog, then fixed his gaze on the middle-aged chieftain.

“That was an interesting conversation. Interesting enough that I would like to hear more.”

“……”

“You seem to have become much quieter since I last saw you, Chief Jang.”

The middle-aged chieftain bit his lip and lowered his head.

“I greet Great Chieftain Baeksang.”

Yohi, the great chieftain of the Yao people, who stood at Baeksang’s right, let out a quiet laugh.

“We must be invisible. Right, Big Brother Heugung?”

“Hm? Oh, yes. That won’t do. To fail to show proper courtesy even with our lovely Yohi standing before them…… That won’t do at all.”

Heugung had been staring at Yohi with a goofy grin. He put on a deliberately stern expression, but Baeksang’s icy gaze made him hunch his plump body.

“S-sorry, Uncle Baek. But did I do something wrong……”

“Aww, what did you do wrong? Our good and handsome Big Brother Heugung hasn’t done anything wrong. Right?”

“R-right. Yohi’s right.”

Baeksang silently watched the two of them, clicked his tongue, and resumed walking.

There was only one head seat at the enormous table, which was large enough for several dozen people to sit around. The three seats closest to it belonged to the three great chieftains besides the Palace Lord.

*Scrape. Clack.*

The twenty-eight chieftains who had arrived earlier in turn, and the three great chieftains who had just arrived.

A total of thirty-one seats had found their owners.

But amid this familiar scene that Baeksang had seen every year, he suddenly felt something out of place and opened his mouth.

“Two seats are empty.”

The words slipped out unexpectedly.

At first, no one realized what Baeksang meant. But the chieftains’ brief puzzlement soon vanished when Yohi spoke in a voice filled with laughter.

“That’s true. How strange. Why would two seats be empty?”

Only thirty-two seats were prepared for the grand council. That had been true a hundred years ago, and it was still true now. Anyone who was not a chieftain—even the Young Palace Lord—was expected to stand in attendance.

There should have been only one empty seat.

Today, there were two.

“Why in the world……”

And just as a puzzled murmur escaped someone’s lips—

*Rumble……*

Beyond the enormous stone gate that began moving once again, two figures finally appeared.

Baeksang’s eyes sank deeply as soon as he saw them.
## Chapter artifact 643

# Chapter 643

*Rumble!*

The stone gate behind me descended with a heavy noise.

Inside the spacious main hall, illuminated by spreading lamplight, thirty-one pairs of eyes flew toward my face like arrows and lodged there amid a silence in which no one spoke.

*Why are you coming out of there?*

That was the look in their eyes. But the emotion permeating them was closer to pure surprise than hostility toward a Han Chinese man, and several of the chieftains even regarded me with goodwill.

Of course, there was one absolute exception.

“One of two things must be true. Either my eyes are deceiving me, or the rules of the tribal grand council have changed without anyone, myself included, knowing.”

The middle-aged man who broke the silence was Baeksang, the great chieftain of the Bai people. He continued in a cold voice.

“Explain yourself. Why have you allowed an ordinary Han Chinese man—who is neither a chieftain nor even a Nanman—to enter this place?”

The person Baeksang demanded an explanation from was neither the Beast Miao King, who was not currently present, nor me.

Yayul Mok, standing to my right, answered calmly.

“Because he is qualified to do so.”

“Qualified.”

Baeksang muttered the word under his breath before continuing.

“It sounds like the rash judgment of an immature brat who has not even reached thirty.”

“It is also the judgment of another person who has yet to arrive.”

“……!”

“My father. No, the Palace Lord said that he is qualified to attend the tribal grand council.”

Baeksang’s gaze sank deeper. After a brief silence, he abruptly spoke.

“Why has the Palace Lord not come?”

“He will be here soon. And by then, I expect only one seat will remain.”

“Impossible.”

Baeksang tapped the table with a callused finger.

“The tribal grand council is a solemn gathering where the chieftains representing all of Nanman come together to exchange their views. If one is not a chieftain, no one may take a seat here except the Young Palace Lord. This man’s qualification is merely the will of the Palace Lord alone. We will not permit it.”

Watching the situation unfold, I muttered,

“That sounds strange. Isn’t that ultimately just your personal opinion too?”

It was clearly an aside, but not one of the several dozen chieftains gathered here possessed martial arts so weak that they could not hear my voice.

That went without saying for Baeksang, whose martial arts were particularly formidable.

He turned his gaze toward me and spoke in a chilly voice.

“What did you just say?”

“Oh, did you hear me?”

“Did you think I wouldn’t?”

“No. Actually, I did mean for you to hear it. Glad you caught that.”

“……!”

I shrugged as I looked at Baeksang’s stiff expression.

“Since the subject has come up, let me say this. We may call ourselves ‘we,’ but isn’t this ultimately just your personal opinion as well? You haven’t even asked what the other chieftains think, yet you say you won’t permit it. What exactly are we supposed to do with that?”

As my words continued to flow smoothly, I could feel an invisible stir spreading among the seated chieftains.

Baeksang was the great chieftain of the Bai people, the most powerful tribe in Nanman after the Miao people, as well as a Supreme Peak master who represented Nanman alongside the Beast Miao King.

No one had probably ever dared to speak to him so bluntly.

Except for me.

“Great Hero Yayul told me this when he sent me ahead. ‘Yayul Cheok, the great chieftain of the Miao people, recognizes your qualification, but Yayul Cheok, the Palace Lord of the Nanman Beast Palace, cannot make this decision unilaterally. So obtain the consent of the other chieftains.’ That is what he said.”

Nanman was a place where even breathing was difficult for outsiders, and the tribal grand council held only once a year was a rigid ceremony with not even enough room for a needle to pass through.

*If the Beast Miao King hadn’t shown me favor, I would have been stopped before I even made it inside.*

Thanks to that favor, I had forced my way through those rigid rules. I intended to claim a seat here.

Of course, I would do so by earning the support of the other chieftains.

“So, that is why I’m asking.”

I looked each chieftain in the eye in turn and continued.

“What do the rest of you think?”

*Fwoosh.*

A breeze blew in from somewhere, making the torches illuminating the hall flicker.

The faces revealed by their reddish light were twisted with discomfort, filled with confusion, or wearing expressions far more positive than I had expected.

Like the middle-aged chieftain who had just begun to speak.

“Everyone here, including the Zang people, knows about the incident that occurred at Ailao Mountain last night.”

From what I had heard and seen in Nanman, the Zang people possessed enough power to stand directly behind Nanman’s four great tribes, even if they did not belong among them.

The middle-aged chieftain, who appeared to be the leader of such a tribe, slowly continued.

“We shed much blood because of an unforeseen disaster, but through a swift response, we were able to prevent an even greater loss of life. We owe it all to Great Chieftain Yayul, our wise Palace Lord, and to a young Han Chinese man who aided him.”

His powerful voice rang throughout the hall. After watching the chieftains’ expressions change from moment to moment, he looked at me and smiled faintly.

“Though late, I would like to express our gratitude here. Thanks to your help, our Zang people were able to save twenty-two brave and excellent warriors. One of them was even a member of my own family.”

“Ah.”

Around two hundred warriors had been dragged into the Poisonblood Grounds, and I had not heard every one of their names and identities.

It was a fact I had not known—and could not have known—but the events of last night were returning to me now in the form of goodwill and gratitude.

“On behalf of the Zang people, I welcome Blazing Flame Divine Dragon Jin Taekyung’s attendance at the tribal grand council.”

When he finished speaking, he offered me a respectful salute. Not with the etiquette of the land where I had been born and raised, but with a Central Plains cupped-fist salute.

And that was only the beginning.

*Scrape. Scrape.*

One by one, unfamiliar chieftains rose from their seats. Different in appearance and clothing, they spoke with expressions of goodwill.

“We cannot pretend not to notice after receiving such a kindness. The Hui people also support him.”

“The Man people have no objection either. I merely wish to thank him for saving my worthless son.”

These chieftains ruled tribes large and small.

But they were not only chieftains. They were also heads of households, fathers and mothers with beloved children.

With painfully awkward cupped-fist salutes, they each offered me their thanks in turn.

The warriors I had rescued from the Poisonblood Grounds the previous night had all been their people and their families.

But the chieftains supporting my attendance at the grand council were not all doing so because of last night’s events.

“The Bouyei people also support him. He is more than qualified.”

At the words of the middle-aged female chieftain, one of the chieftains who still had not risen from his seat frowned.

“Wait. What reason do the Bouyei people have? There weren’t any Bouyei among the warriors stationed at Ailao Mountain, were there?”

“Because Nanman is my homeland.”

“What does that—”

“Even beasts that cannot speak know how to repay a kindness. Blazing Flame Divine Dragon Jin Taekyung risked his life and fought for my homeland last night. Isn’t that alone enough to qualify him to attend this gathering?”

“……Ahem.”

The chieftain who had asked the question shut his mouth with an uncomfortable cough, while goodwill-filled smiles spread across the faces of the others.

And amid this atmosphere, so clearly different from the one only a few days ago, I felt a tickle in one corner of my chest.

*Repaying someone for the help they gave you. When you think about it, it’s only natural.*

In this world, however, there were times when something so natural ceased to be natural.

I had not gone to the Poisonblood Grounds expecting repayment from them, but at this very moment, quite a few chieftains were repaying me with gratitude and trust.

Because of the help they had received last night.

Or because of something that had happened in the distant past.

“My late father, who was once a great chieftain, often said things like this after returning from the Great Faction War. ‘If it hadn’t been for the Fire King, I would have gone to the Nine Springs instead of returning to Nanman.’ I had completely forgotten those words after his death, but they have finally come back to me.”

“My ancestor destroyed the Five Poisons Sect alongside the Sect Leader of the Fire Gate Clan at the time. If it hadn’t been for him, our tribe would not have survived to this day. I support him as well.”

The water that had been still began to flow.

The chieftains who had remained seated in silence rose one after another like the current of flowing water and began to speak. Before long, the number of people standing had surpassed the number still seated.

And amid this unexpected situation, the final person who would bring it to an end finally appeared.

*Rumble, rumble—boom!*

A giant nearly eight feet tall lifted the stone gate, which weighed a thousand geun, with one hand.

Casting a long, enormous shadow across the hall, the Beast Miao King spoke in a low voice.

“Looks like a conclusion has been reached.”

At the far end of the Beast Miao King’s gaze, Baeksang slowly rose from his seat and offered a cold salute.

“I greet you, Palace Lord.”

“Unless my eyes and ears deceive me, he seems more than qualified. Don’t you agree, little brother?”

“It is the wrong choice. You are destroying the rules of a tribal grand council with a venerable tradition.”

“More than half of the chieftains have already recognized his right to attend. And the scholars of the Central Plains call this a consensus.”

Baeksang closed his eyes instead of answering, and the Beast Miao King did not wait any longer.

“I, Yayul Cheok, great chieftain of the Miao people and Palace Lord of the Nanman Beast Palace, hereby permit Jin Taekyung—the Fire Dragon Pavilion Master of the Murim Alliance and successor to the Fire Gate Clan—to attend the tribal grand council.”

At that exact moment, a clear bell tone pierced my ears.

*Ding.*

> **System**
>
> - **Quest: Tribal Grand Council** has been created!

* * *

A damp, sweltering space.

Somewhere in the darkness between pitch-blackness and the abyss, a voice that could not be heard drifted through the air.

—The grand council has begun in the Inner Palace.

—And him?

—He attended the grand council as well. But……

—Continue. Don’t hesitate.

—Th-that is……

There was a brief hesitation.

Even the man sending the Sound Transmission could not have expected that it would cost him his life.

*Swish. Slice.*

With a faint noise, the figure concealed in the darkness crumpled helplessly.

When the white fingers that had wiped the blood from their cheek moved, the lifeless corpse flew beyond the darkness and vanished.

—So? What happened?

A life had vanished in an instant, but the empty space was quickly filled by someone new. A tense Sound Transmission rang out in succession.

—Jin Taekyung. Jin Taekyung attended the grand council.

—Who? Jin Taekyung?

—Yes! Apparently he gained permission with the support of the Beast Miao King and the other chieftains.

After a brief silence, someone in the darkness clicked their tongue.

—Those barbarian bastards…… But what about you? You just stood by and watched it happen?

—W-what?

—Then again, how could a worm like you be at fault? It was my mistake for keeping a useless worm under my command.

—……!

The person reporting to the entity in the darkness immediately realized the danger, but he could not escape death either.

*Swish. Thrust!*

Death passed by once again. The entity gazed down at the corpse buried in the darkness and muttered quietly.

“Jin Taekyung. It’s been a while.”
## Chapter artifact 644

# Chapter 644

*Ding. Ding. Ding.*

> **System**
>
> - A new Quest, **Tribal Grand Council**, has been created!
>
> **Quest**
>
> **Tribal Grand Council**
>
> You have become the first outsider in the history of the Nanman Beast Palace to earn the right to attend the tribal grand council.
>
> This is an achievement that even the Fire Gate Clan’s fifth Sect Leader of the past failed to accomplish.
>
> Why? Because he destroyed the Five Poisons Sect and left before the grand council could even begin!
>
> At this momentous meeting, where the major and minor affairs of Nanman will be decided, you must achieve the best possible result!
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Nanman Beast Palace’s entry into the alliance *(Incomplete)*
>
> **Reward:** ???
>
> **Failure:** ???

I stared at the Quest window and inwardly sighed.

No matter how favorably public opinion had shifted toward me, getting the Nanman Beast Palace to join the alliance was no simple task. It was every bit as brutal as the Quest’s Supreme Peak Grade suggested.

*And what was that bit about the fifth Sect Leader…?*

The Fire Gate Clan really was something else.

They were a venerable sect of thugs that had continued for hundreds of years through one-person succession.

Among the successive Sect Leaders of the Fire Gate Clan, I had heard that some had lived long lives secluded from the world, while others had gone out into the Murim, burned like flames, and died young. But every one of them had been a monster whose might ranked among the top five in the world.

*That’s probably one of the reasons I’m allowed to sit here.*

Though it had happened more than two hundred years ago, the Nanman Beast Palace and the Fire Gate Clan had been fairly close.

By K-Murim logic, it was basically a sect founded by Grandfather Dangun’s best friend.[^1]

[^1]: Dangun is the legendary founder of Korea’s first kingdom; “Grandfather Dangun” is a familiar, joking way to invoke remote shared ancestry.

The problem was that while I had a talent for beating people up, I had absolutely no talent for persuasion.

*Still, I have to do my best.*

I straightened my back and looked at the thirty-two chieftains seated around the table.

The Beast Miao King occupied the highest seat. To his left and right sat the great chieftains Baeksang, Yohi, and Heugung, in that order, while the others appeared to have been assigned their seats without regard to the strength of their factions.

There might not have been many of them, but each and every one was a chieftain commanding anywhere from several hundred to tens of thousands of tribespeople.

When I considered that, this gathering was practically Nanman itself.

And just as I was studying their faces, the Beast Miao King, seated at the head of the table, broke the brief silence.

“Well, then.”

His expression was solemn, and his gaze was filled with dignity. At last, he opened his mouth, and the air in the room drew taut like a bowstring.

The Beast Miao King radiated the charisma befitting the master of the Nanman Beast Palace and uttered a historic first sentence in a grave voice.

“Did everyone eat before coming here?”

“……?”

“We’ve had some unpleasant things happen lately, but you still shouldn’t skip your meals. In particular, Chief Jang, you seem to have lost a little weight compared to last year.”

“……!”

*Historic, my ass.*

*What did I just hear?*

While I was still doubting my ears at that completely unexpected opening, Chief Jang—the first person to offer me a cupped-fist salute earlier—answered.

“As expected, nothing gets past the Palace Lord’s keen eyes. I have lost a little weight, in fact.”

*No. He’s actually going along with this?*

“I thought so. But a man who calls himself a chieftain cannot be neglecting himself like that. You should take care of your health for the sake of your tribespeople. Now, how old are you again?”

“I am sixty.”

“You’re still in the prime of life. Eat more from now on.”

“Jonmyeong.”[^2]

Now I was hearing things too, because *jonmyeong* sounded like *jonmang*—“fucked.”

*Nanman is fucked.*

[^2]: *Jonmyeong* is a formal acknowledgment meaning “As you command”; it differs by one vowel from *jonmang*, crude slang for being utterly ruined.

I looked at the thirty-two chieftains with a dazed expression.

Representing all of Nanman, they had taken the Beast Miao King’s first words as a starting signal and were now exchanging conversations in various corners that made my heart feel cramped just listening to them.

“Chief Gal, I heard the news. Your sixth child had their coming-of-age ceremony?”

“My seventh.”

“I got confused. If only you’d stopped at one or two. No matter how vigorous you are, how can you have fifteen?”

“Seventeen.”

“……At last year’s grand council, you definitely had fifteen.”

“I had two more. Twins.”

“Oh.”

On one side was a conversation with a super-sperm man who seemed intent on founding a Nanman soccer league.

“Chief Gu. Return the livestock you stole a while ago.”

“What livestock?”

“The fifty-two dairy cows that vanished from the pasture without a trace. Did you think I wouldn’t know your tribespeople did it?”

“I have never done such a thing.”

“Of course you’d say that. Return them while I’m still asking nicely.”

“Oh, for real! I said I never did that!”

“I said hand over the cows while I’m asking nicely! You cow-udder bastard!”

On the other side, a furious argument raged over the question of who had stolen all those cows.

“It comes back to me as clearly as yesterday—the day you bastards trespassed into our tribal territory.”

“Damn it, this guy does this every year. You’re barely forty, so why do you keep bringing up something that happened eighty years ago?”

“I inherited the spirits of my ancestors. In that sense, hand over the land.”

“How does that make any sense? Why do you keep dragging up something that was settled by the previous generation?”

“Hand over the land.”

“No, seriously……”

“Hand over the land.”

Elsewhere, a land ghost insisting he had been reincarnated continued his back-and-forth struggle.

And while I was watching this entire absurd situation, someone’s voice slipped into my ear through Sound Transmission.

—You have a funny expression.

I subtly turned my head to find the owner of the voice. At the same time, my eyes met Yohi’s as she looked in my direction and smiled as though she were enjoying herself.

—The tribal grand council is always like this. Well, everyone is scattered across Nanman and only gathers once a year, so I suppose it’s natural.

After thinking for a moment, I answered honestly.

—Even taking that into consideration, this is too much of a shitshow.

—The tribal grand council is where all the major and minor affairs of Nanman are discussed. Literally, that means even small matters are included in the meeting.

—……That matter is way too small, though.

—How else could thirty-two tribes live together in harmony? They settle things one by one when everyone is gathered. That is how they clear away old grudges.

*Crash!*

“You goddamn mutt!”

“Has this bastard lost his mind……?”

“You think your martial arts are that strong? Shut your mouth and come outside.”

I watched the two chieftains who had finally grabbed each other by the collars after their heated argument over the cows. Yohi added:

—Of course, there are exceptions.

—……

—It’ll be settled soon. The real grand council starts after that.

“Ah. Give me land. I said give me land.”

“Gaaah. You Thousand-Year Spider bastard.”

“Come to think of it, a thousand years ago, our ancestors……”

“Stop! Stoooop!”

*It’ll be settled soon,* she said.

Hmm. I didn’t think so.

*Are these people really just a bunch of barbarians……?*

I was muttering the thought I could not bring myself to say aloud when, just as Yohi had said, the chaotic situation around us began to settle one piece at a time, and new topics started flowing in.

“Thirty Man warriors were wounded and twenty-two were killed in this year’s ferocious-beast hunt. The beasts seem to have become especially rampant lately, so before the losses grow any larger, we request that the Inner Palace take action……”

“Sudden torrential rain caused a flood. The pasture and around fifty nearby homes were submerged……”

“I hereby report that the dispute between the Huang and Dong tribes has come to an end. In accordance with the agreement, both sides have drawn up an official document, and peace will be maintained for the next ten years……”

The situation surrounding the ferocious-beast hunt. Natural disasters and disputes.

Once the appetizers were finished, the main dishes began to arrive.

And among the stories being brought up, there was also information that demanded some serious attention.

“They say a strange figure has appeared in the northeast.”

*A strange figure?*

As the question arose in my mind, the Beast Miao King—who until then had merely nodded along with short replies—straightened his posture and spoke.

“A strange figure. This is the first I have heard of it.”

“W-well, the thing is……”

The chieftain who had first brought up the matter of the strange figure answered with an uncertain expression.

“I cannot speak with confidence because the information has not been confirmed……”

“Where did the information come from?”

“Three days ago, we captured a Han Chinese man who had crossed the northeastern border. He told us about it. Apparently, an unidentified strange man appeared out of nowhere and is stirring up a bloodbath in Guizhou.”

Guizhou was a border region touching Nanman, along with Sichuan and Guangxi. With a little exaggeration, it was practically close enough to trip and bump your nose against.

*But a strange man appeared in Guizhou? So suddenly?*

It felt wrong. No, it felt more than wrong—it grated on me.

And I was not the only one to sense that something was just as inscrutable as the strange man’s identity.

“More details.”

At the Beast Miao King’s furrowed brow, the chieftain swallowed nervously.

“Nothing is known about the strange man’s name or age. However, they say he is bald like the monks of the Central Plains and carries a single Zen staff. He has beaten several hundred people to death in Guizhou alone, and because of that, they say he is known by the sobriquet Blood Monk.”

“Blood Monk?”

“Yes. The Han Chinese man we captured appeared to be a fairly skilled martial artist himself, but he could not hide his fear whenever he spoke about the Blood Monk.”

The Blood Monk was frightening enough as a sobriquet, but there was no doubt that its owner possessed truly astonishing martial arts.

*Guizhou is unquestionably orthodox faction territory. The Murim Alliance couldn’t possibly have just stood by and done nothing.*

And yet the man had killed several hundred people and earned a notorious reputation. It would have been impossible without at least Supreme Peak-level martial prowess.

Besides, it bothered me that he had appeared in Guizhou—a region directly adjacent to Nanman.

*Could it be……?*

An unidentified strange man who had appeared out of nowhere at an unusual time. Martial prowess powerful enough to sweep through Guizhou, a land of the orthodox faction, single-handedly.

I could not help but consider a connection to Dark Heaven. Even if he was not a great figure on the level of the Southern Heaven Demon Empress, the possibility was more than sufficient.

The Blood Lord and the Western Heaven Demon Lord had also kept Supreme Peak masters such as the Yin-Yang Twin Ghosts and the Qilian Three Fiends under their command.

*And what if the Blood Monk’s target is Nanman……?*

When my thoughts reached that point, I spoke to the chieftain for the first time.

“Is it possible to know where the Blood Monk is headed?”

“I would have liked to ask him myself, but there is no way to know now.”

“What do you mean……”

The chieftain shook his head with a faint sigh and answered.

“He is dead.”

“What?”

“He died before I could ask him anything else. He was already suffering from serious injuries, to begin with, and it seems he was unable to adapt to the sudden change in environment. A torrential rain came down at just the wrong time and caused a flood, so we could not take proper measures.”

“……!”

The Blood Monk’s appearance.

And now, the death of the only witness we had.

As silence descended over the room, someone who had remained silent since the grand council began abruptly spoke.

“Injury, endemic disease, and death. Such things happen from time to time.”

At the sudden voice, everyone’s gaze turned toward the same place.

Baeksang.

It was him.

“The Slaughter Saint appearing in the Central Plains is no different. Han Chinese have always been that way. Despite being one people, they have maintained the present world by killing and being killed among themselves. In short……”

His tone was calm, and his expression was utterly composed. Baeksang’s cold voice continued.

“There is no reason to pay the slightest attention to affairs in the Central Plains. At least not for Nanman.”

I did not know whether the thought that came to me then was merely a misunderstanding.

But one thing was certain: this conversation felt strange and alien to me.

Baeksang was the great chieftain of the Bai people, who possessed Nanman’s second-largest faction and the second-largest population. And yet he was trying to ignore an event unfolding right beside him.

As I silently stared at Baeksang, I suddenly opened my mouth.

“What will you do if the Blood Monk is heading south?”

The chieftains who understood what I meant opened their eyes wide, while Baeksang answered without a hint of wavering.

“Nanman is not the only place bordering Guizhou. If he passes through Guangxi, a vast open sea spreads before him. With a favorable wind, he can reach Hainan after sailing for ten days.”

“Meaning that the possibility of the Blood Monk invading Nanman is low?”

“What reason would he have to come all the way here? Rather than face venomous beasts, ferocious beasts, and countless Nanman warriors, he could simply head to the sea through Guangxi……”

“There is one reason. A single, unmistakable reason. But……”

I forcefully cut him off before he could continue, fixing Baeksang with a grave, steady gaze as I went on.

“Strangely enough, you seem to be the only one who doesn’t know that.”

“What?”

“Or……”

I paused before continuing.

“Did you make some kind of agreement with someone to pretend from the very beginning that you didn’t know?”

At that moment—

*Fwoosh. Whoomph.*

The wavering torchlight went out.

And amid the darkness that descended over the enormous hall, there was a pair of eyes radiating a piercing, icy chill.

“You have finally crossed the line.”

*Whoosh!*

“Well.”

I felt the enormous martial aura squeezing my entire body from every direction and muttered calmly.

“It seems you’re the one crossing the line.”
